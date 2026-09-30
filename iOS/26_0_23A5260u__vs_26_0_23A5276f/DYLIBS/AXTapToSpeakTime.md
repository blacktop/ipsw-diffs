## AXTapToSpeakTime

> `/System/Library/PrivateFrameworks/AXTapToSpeakTime.framework/AXTapToSpeakTime`

```diff

-3180.6.1.0.0
-  __TEXT.__text: 0x767c
-  __TEXT.__auth_stubs: 0x5b0
-  __TEXT.__objc_methlist: 0x86c
+3183.1.0.0.0
+  __TEXT.__text: 0x7514
+  __TEXT.__auth_stubs: 0x590
+  __TEXT.__objc_methlist: 0x87c
   __TEXT.__const: 0xc0
-  __TEXT.__cstring: 0x8d5
-  __TEXT.__oslogstring: 0xdfe
+  __TEXT.__cstring: 0x8f7
+  __TEXT.__oslogstring: 0xdc3
   __TEXT.__gcc_except_tab: 0x100
-  __TEXT.__unwind_info: 0x270
+  __TEXT.__unwind_info: 0x260
   __TEXT.__objc_classname: 0xb4
-  __TEXT.__objc_methname: 0x1b7c
-  __TEXT.__objc_methtype: 0x460
-  __TEXT.__objc_stubs: 0x1620
+  __TEXT.__objc_methname: 0x1b8f
+  __TEXT.__objc_methtype: 0x463
+  __TEXT.__objc_stubs: 0x1700
   __DATA_CONST.__got: 0x1a8
-  __DATA_CONST.__const: 0x2a8
+  __DATA_CONST.__const: 0x2e0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7e0
+  __DATA_CONST.__objc_selrefs: 0x808
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x50
-  __AUTH_CONST.__auth_got: 0x2e8
+  __AUTH_CONST.__auth_got: 0x2d8
   __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0xac0
+  __AUTH_CONST.__cfstring: 0xae0
   __AUTH_CONST.__objc_const: 0x910
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x60

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B688472C-E699-30D4-8579-D09B328C02DB
-  Functions: 194
-  Symbols:   836
-  CStrings:  627
+  UUID: DAE7E067-F137-3CEB-8158-C394D61FC737
+  Functions: 192
+  Symbols:   838
+  CStrings:  634
 
Symbols:
+ -[AXTapToSpeakTimeManager _getPreferredSpeechSynthesisVoice]
+ -[AXTapticChimesScheduler _outputTapticChime:atDate:isPreview:]
+ -[AXTapticChimesScheduler _outputTapticChime:atDate:isPreview:].cold.1
+ -[AXTapticChimesScheduler _outputTapticChime:atDate:isPreview:].cold.2
+ -[AXTapticChimesScheduler _outputTapticChime:atDate:isPreview:].cold.3
+ -[AXTapticChimesScheduler _outputTapticChime:atDate:isPreview:].cold.4
+ _AXLanguageConvertToCanonicalForm
+ _OBJC_CLASS_$_TTSAlternativeVoices
+ ___32-[AXTapticChimesScheduler _init]_block_invoke.304
+ ___60-[AXTapToSpeakTimeManager _getPreferredSpeechSynthesisVoice]_block_invoke
+ ___63-[AXTapticChimesScheduler _outputTapticChime:atDate:isPreview:]_block_invoke
+ ___63-[AXTapticChimesScheduler _outputTapticChime:atDate:isPreview:]_block_invoke.370
+ ___block_descriptor_48_e8_32s40s_e32_B16?0"AVSpeechSynthesisVoice"8ls32l8s40l8
+ ___block_literal_global.306
+ ___block_literal_global.322
+ ___block_literal_global.328
+ ___block_literal_global.398
+ _objc_msgSend$_canOutputPremiumVoice
+ _objc_msgSend$_currentLanguageCode
+ _objc_msgSend$_getPreferredSpeechSynthesisVoice
+ _objc_msgSend$_outputTapticChime:atDate:isPreview:
+ _objc_msgSend$_speechVoicesIncludingSiri
+ _objc_msgSend$ax_firstObjectUsingBlock:
+ _objc_msgSend$containsString:
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$isSiriVoiceIdentifier:
+ _objc_msgSend$language
+ _objc_msgSend$lowercaseString
+ _objc_msgSend$quality
+ _objc_retain
- -[AXTapToSpeakTimeManager _ttsSiriVoiceAssetForAFVoice:language:]
- -[AXTapToSpeakTimeManager _ttsSiriVoiceAssetForAFVoice:language:].cold.1
- -[AXTapToSpeakTimeManager _ttsSiriVoiceAssetForAFVoice:language:].cold.2
- -[AXTapticChimesScheduler _outputTapticChime:atDate:].cold.1
- -[AXTapticChimesScheduler _outputTapticChime:atDate:].cold.2
- -[AXTapticChimesScheduler _outputTapticChime:atDate:].cold.3
- -[AXTapticChimesScheduler _outputTapticChime:atDate:].cold.4
- _AXCLanguageConvertToCanonicalForm
- _OBJC_CLASS_$_TTSSiriAssetManager
- _TTSSupportsNeuralVoices
- ___32-[AXTapticChimesScheduler _init]_block_invoke.298
- ___53-[AXTapticChimesScheduler _outputTapticChime:atDate:]_block_invoke
- ___53-[AXTapticChimesScheduler _outputTapticChime:atDate:]_block_invoke.367
- ___block_literal_global.302
- ___block_literal_global.319
- ___block_literal_global.325
- ___block_literal_global.395
- __os_log_debug_impl
- _objc_msgSend$_ttsSiriVoiceAssetForAFVoice:language:
- _objc_msgSend$_voiceFromInternalVoiceListWithIdentifier:
- _objc_msgSend$footprint
- _objc_msgSend$installedAssetForLanguage:gender:footprint:voiceName:voiceType:
- _objc_msgSend$installedAssetsForLanguage:voiceType:
- _objc_retain_x26
CStrings:
+ ""
+ "B16@?0@\"AVSpeechSynthesisVoice\"8"
+ "B36@0:8@16@24B32"
+ "Current time is not in scheduled interval. Should not play chimes"
+ "Default to system voice for current langauge: %@"
+ "Siri voice language: %@ does not match system general language: %@"
+ "Siri voice name is invalid"
+ "Siri voice output is unsupported"
+ "Starting time is after ending time and current time is in scheduled interval. Can play chimes"
+ "Starting time is before ending time and current time is in scheduled interval. Can play chimes"
+ "Unable to find Siri voice for language: %@"
+ "_getPreferredSpeechSynthesisVoice"
+ "_outputTapticChime:atDate:isPreview:"
+ "_speechVoicesIncludingSiri"
+ "ax_firstObjectUsingBlock:"
+ "containsString:"
+ "isEqualToString:"
+ "isSiriVoiceIdentifier:"
+ "language"
+ "lowercaseString"
+ "quality"
- "@32@0:8@16@24"
- "Current time is in schedule interval. Can play chimes"
- "Current time is not in schedule interval. Should not play chimes"
- "Neural voice not found for name: %@. Will try looking for Gryphon voice."
- "Siri TTS voice identifier: %@"
- "Siri voice language: %@ does not match system general language: %@. Will default to current locale system voice."
- "TTSSiriAssetManager installedAssetForLanguage:%@ gender:%ld footprint:%ld voiceName:%@ voiceType:%ld"
- "TTSSiriAssetManager installedAssetsForLanguage: %@ voiceType: %ld\n%@"
- "TTSSupportsNeuralVoices: %d"
- "_ttsSiriVoiceAssetForAFVoice:language:"
- "_voiceFromInternalVoiceListWithIdentifier:"
- "footprint"
- "installedAssetForLanguage:gender:footprint:voiceName:voiceType:"
- "installedAssetsForLanguage:voiceType:"

```
