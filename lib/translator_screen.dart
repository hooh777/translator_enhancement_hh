// === File: lib/translator_screen.dart ===

import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'translator_state.dart';

class TranslatorScreen extends ConsumerWidget {
  const TranslatorScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final translatorState = ref.watch(translatorProvider);
    final notifier = ref.read(translatorProvider.notifier);
    
    final inputController = TextEditingController();

    return Scaffold(
      appBar: AppBar(title: const Text('AI Email Translator')),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            TextField(
              controller: inputController,
              maxLines: 8,
              decoration: const InputDecoration(
                hintText: 'Paste the Chinese email text here...',
                border: OutlineInputBorder(),
              ),
            ),
            const SizedBox(height: 16),
            
            ElevatedButton(
              onPressed: translatorState.state == AppState.loading
                  ? null
                  : () => notifier.translateText(inputController.text),
              style: ElevatedButton.styleFrom(padding: const EdgeInsets.all(16)),
              child: const Text('Translate', style: TextStyle(fontSize: 16)),
            ),
            const SizedBox(height: 24),
            
            Expanded(
              child: Container(
                padding: const EdgeInsets.all(12.0),
                decoration: BoxDecoration(
                  border: Border.all(color: Colors.grey.shade300),
                  borderRadius: BorderRadius.circular(8.0),
                  color: Colors.grey[100],
                ),
                child: _buildOutput(translatorState),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildOutput(TranslatorState state) {
    switch (state.state) {
      case AppState.loading:
        return const Center(child: CircularProgressIndicator());
      case AppState.error:
        return Center(
          child: Text(
            'An error occurred:\n${state.errorMessage}',
            style: const TextStyle(color: Colors.red),
            textAlign: TextAlign.center,
          ),
        );
      case AppState.data:
      case AppState.idle:
      default:
        return SingleChildScrollView(child: Text(state.translatedText));
    }
  }
}