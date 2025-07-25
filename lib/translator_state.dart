// === File: lib/translator_state.dart ===

import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'translation_service.dart';

enum AppState { idle, loading, data, error }

class TranslatorState {
  final AppState state;
  final String translatedText;
  final String errorMessage;

  TranslatorState({
    this.state = AppState.idle,
    this.translatedText = 'Translation will appear here...',
    this.errorMessage = '',
  });

  TranslatorState copyWith({
    AppState? state,
    String? translatedText,
    String? errorMessage,
  }) {
    return TranslatorState(
      state: state ?? this.state,
      translatedText: translatedText ?? this.translatedText,
      errorMessage: errorMessage ?? this.errorMessage,
    );
  }
}

class TranslatorNotifier extends StateNotifier<TranslatorState> {
  final Ref _ref;
  TranslatorNotifier(this._ref) : super(TranslatorState());

  Future<void> translateText(String text) async {
    if (text.trim().isEmpty) return;
    
    state = state.copyWith(state: AppState.loading);

    try {
      final translationService = _ref.read(translationServiceProvider);
      final result = await translationService.translate(text);
      state = state.copyWith(state: AppState.data, translatedText: result);
    } catch (e) {
      state = state.copyWith(state: AppState.error, errorMessage: e.toString());
    }
  }
}

final translatorProvider = StateNotifierProvider<TranslatorNotifier, TranslatorState>((ref) {
  return TranslatorNotifier(ref);
});