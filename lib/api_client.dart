import 'dart:convert';
import 'package.http/http.dart' as http;
import 'package:flutter_riverpod/flutter_riverpod.dart';

// 1. Create a provider that will hold our API key string.
//    It throws an error by default, because we will provide the
//    real value when the app starts.
final apiKeyProvider = Provider<String>((ref) {
  throw UnimplementedError('API Key not provided');
});


// The TranslationApiClient class remains completely unchanged.
class TranslationApiClient {
  static const String _baseUrl = 'https://api.x.ai/v1/chat/completions';
  final String _apiKey;
  TranslationApiClient({required String apiKey}) : _apiKey = apiKey;

  Future<String> fetchTranslation(String textToTranslate, Map<String, List<String>> glossaryTerms) async {
    // ... all the existing fetchTranslation code remains here ...
    if (_apiKey.isEmpty || _apiKey == 'YOUR_API_KEY_HERE') {
      throw Exception('API Key not set.');
    }

    String systemPrompt = "You are a professional translator specializing in business communication for the printing industry. Translate the user's Chinese email into professional, natural-sounding English. Do not add any commentary, preamble, or notes. Provide only the translated English text.";
    if (glossaryTerms.isNotEmpty) {
      String glossaryInstruction = "\n\nCRITICAL: You must use the following specific translations for these terms. For terms with multiple options, choose the one that best fits the context:\n";
      for (var entry in glossaryTerms.entries) {
        glossaryInstruction += "- For '${entry.key}', use one of: [${entry.value.join(', ')}]\n";
      }
      systemPrompt += glossaryInstruction;
    }

    final url = Uri.parse(_baseUrl);
    final requestBody = jsonEncode({
      "model": "llama3-70b-8192",
      "messages": [
        {"role": "system", "content": systemPrompt},
        {"role": "user", "content": textToTranslate}
      ],
      "temperature": 0.3,
      "max_tokens": 2048,
    });

    try {
      final response = await http.post(
        url,
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer $_apiKey',
        },
        body: requestBody,
      );

      if (response.statusCode == 200) {
        final responseBody = jsonDecode(response.body);
        return responseBody['choices'][0]['message']['content'].trim();
      } else {
        throw Exception('Failed to translate text. Status code: ${response.statusCode}\nBody: ${response.body}');
      }
    } catch (e) {
      throw Exception('Failed to connect to the translation service: $e');
    }
  }
}
```
```dart
// === File: lib/translation_service.dart (UPDATED) ===
// This service will now get the API key from the new provider.

import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'api_client.dart';
import 'glossary_manager.dart';

// 2. Update the translationServiceProvider
final translationServiceProvider = Provider<TranslationService>((ref) {
  // Get the API key from the new apiKeyProvider
  final apiKey = ref.watch(apiKeyProvider);
  
  // Create the ApiClient with the key we just retrieved
  final apiClient = TranslationApiClient(apiKey: apiKey);
  
  return TranslationService(apiClient);
});


// The TranslationService class remains completely unchanged.
class TranslationService {
  final TranslationApiClient _apiClient;
  TranslationService(this._apiClient);

  Future<String> translate(String text, WidgetRef ref) async {
    final glossaryManager = await ref.read(glossaryManagerProvider.future);
    final foundTerms = glossaryManager.findTermsInText(text);
    return _apiClient.fetchTranslation(text, foundTerms);
  }
}
```
```dart
// === File: lib/main.dart (UPDATED) ===
// We will now load the config file here and override the provider.

import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'translator_screen.dart';
import 'glossary_manager.dart';
import 'api_client.dart'; // Import the file with apiKeyProvider

// 3. Make the main function async
Future<void> main() async {
  // This line is required to use 'await' before 'runApp'
  WidgetsFlutterBinding.ensureInitialized();

  // Load the config file from assets
  final configString = await rootBundle.loadString('lib/config.json');
  final config = jsonDecode(configString);
  final apiKey = config['apiKey'] as String;

  // 4. Update runApp to override the provider
  runApp(
    ProviderScope(
      overrides: [
        // Provide the real API key value to our apiKeyProvider
        apiKeyProvider.overrideWithValue(apiKey),
      ],
      child: const TranslationApp(),
    ),
  );
}


// The TranslationApp class remains mostly unchanged.
class TranslationApp extends ConsumerWidget {
  const TranslationApp({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final glossaryAsyncValue = ref.watch(glossaryManagerProvider);
    return MaterialApp(
      title: 'AI Email Translator',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        useMaterial3: true,
      ),
      debugShowCheckedModeBanner: false,
      home: glossaryAsyncValue.when(
        data: (_) => const TranslatorScreen(),
        loading: () => const Scaffold(body: Center(child: CircularProgressIndicator())),
        error: (err, stack) => Scaffold(body: Center(child: Text('Error initializing app: $err'))),
      ),
    );
  }
}
