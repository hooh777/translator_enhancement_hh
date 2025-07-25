import 'dart:convert';
import 'package:http/http.dart' as http;

/// A client responsible for handling all communication with the Grok API from x.ai.
/// This represents a key part of our Data Access Layer.
class TranslationApiClient {
  
  // The base URL for the Grok API chat completions endpoint.
  static const String _baseUrl = 'https://api.x.ai/v1/chat/completions';

  // The API key is now passed into the constructor.
  final String _apiKey;
  TranslationApiClient({required String apiKey}) : _apiKey = apiKey;

  /// Fetches a translation from the Grok API.
  ///
  /// Takes the [textToTranslate] as input and returns the translated
  /// English text as a [Future<String>].
  /// Throws an [Exception] if the API call fails.
  Future<String> fetchTranslation(String textToTranslate) async {
    if (_apiKey.isEmpty || _apiKey == 'YOUR_API_KEY_HERE') {
      throw Exception('API Key not set. Please set your x.ai API key.');
    }

    final url = Uri.parse(_baseUrl);

    // The Grok API uses a "messages" array for its prompt structure.
    // We create a "system" message to define the AI's persona and a "user"
    // message to provide the text we want to translate.
    final requestBody = jsonEncode({
      "model": "grok-3", // The model name for Grok
      "messages": [
        {
          "role": "system",
          "content": "You are a professional translator specializing in business communication for the printing industry. Translate the user's Chinese email into professional, natural-sounding English. Do not add any commentary, preamble, or notes. Provide only the translated English text."
        },
        {
          "role": "user",
          "content": textToTranslate
        }
      ],
      "temperature": 0.3, // Lower temperature for more predictable, less "creative" output
      "max_tokens": 2048,
    });

    try {
      // Make the POST request to the API.
      // Note the new 'Authorization' header required by Grok.
      final response = await http.post(
        url,
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer $_apiKey', // Grok uses a Bearer token
        },
        body: requestBody,
      );

      // Check if the request was successful.
      if (response.statusCode == 200) {
        final responseBody = jsonDecode(response.body);
        // Navigate through the JSON response to find the translated text.
        // This structure is specific to the Grok/OpenAI API format.
        final translatedText = responseBody['choices'][0]['message']['content'];
        return translatedText.trim();
      } else {
        // If the server did not return a 200 OK response, throw an error.
        throw Exception('Failed to translate text. Status code: ${response.statusCode}\nBody: ${response.body}');
      }
    } catch (e) {
      // Catch any other exceptions, such as network errors.
      throw Exception('Failed to connect to the translation service: $e');
    }
  }
}
