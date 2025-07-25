// === File: lib/translation_service.dart ===
// This file defines the service that calls our API client.

import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'api_client.dart'; // Make sure this is importing your updated api_client.dart

// 1. This Provider creates the TranslationService instance.
//    The UI will use this provider to access the service.
final translationServiceProvider = Provider<TranslationService>((ref) {
  // IMPORTANT: This is the line you need to change.
  // Replace "YOUR_API_KEY_HERE" with your actual Grok API key from x.ai
  final apiClient = TranslationApiClient(apiKey: "xai-wPyCj4LvyJaJC4c3qW2ieuT8Q6ThPW7GzOPoXvn0uYSxTorIP0XJdMje9OxIhp1Kxdk9PwEv4RbP8jlf");
  
  return TranslationService(apiClient);
});


// 2. This is the Business Logic Layer class.
//    Its only job is to call the Data Access Layer (the ApiClient).
class TranslationService {
  final TranslationApiClient _apiClient;
  TranslationService(this._apiClient);

  /// This is the public method the UI will call.
  /// It simply forwards the request to the API client's translate method.
  Future<String> translate(String text) {
    return _apiClient.fetchTranslation(text);
  }
}