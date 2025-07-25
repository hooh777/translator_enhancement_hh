// In lib/main.dart
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'translator_screen.dart';

void main() {
  runApp(const ProviderScope(child: TranslationApp()));
}

class TranslationApp extends StatelessWidget {
  const TranslationApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'AI Email Translator',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        useMaterial3: true,
      ),
      debugShowCheckedModeBanner: false,
      // Set the home property to our new TranslatorScreen
      home: const TranslatorScreen(),
    );
  }
}