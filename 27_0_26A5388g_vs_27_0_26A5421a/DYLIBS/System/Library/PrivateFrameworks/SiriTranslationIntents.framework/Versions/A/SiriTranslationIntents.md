## SiriTranslationIntents

> `/System/Library/PrivateFrameworks/SiriTranslationIntents.framework/Versions/A/SiriTranslationIntents`

```diff

-3600.10.2.0.0
-  __TEXT.__text: 0x5b754
+3600.10.5.0.0
+  __TEXT.__text: 0x5db5c
   __TEXT.__objc_methlist: 0x550
-  __TEXT.__const: 0x39d4
-  __TEXT.__swift5_typeref: 0xf48
-  __TEXT.__constg_swiftt: 0x17d4
-  __TEXT.__swift5_reflstr: 0xd83
-  __TEXT.__swift5_fieldmd: 0x11b8
-  __TEXT.__cstring: 0xf03
-  __TEXT.__swift5_proto: 0x278
-  __TEXT.__swift5_types: 0x124
-  __TEXT.__swift5_assocty: 0x278
+  __TEXT.__const: 0x3ba4
+  __TEXT.__swift5_typeref: 0xff4
+  __TEXT.__constg_swiftt: 0x1828
+  __TEXT.__swift5_builtin: 0x3c
+  __TEXT.__swift5_reflstr: 0xde3
+  __TEXT.__swift5_fieldmd: 0x1214
+  __TEXT.__swift5_assocty: 0x2a8
+  __TEXT.__swift5_proto: 0x290
+  __TEXT.__swift5_types: 0x128
+  __TEXT.__cstring: 0xfe3
   __TEXT.__swift_as_entry: 0x130
   __TEXT.__swift_as_ret: 0x17c
   __TEXT.__swift_as_cont: 0x208
   __TEXT.__swift5_protos: 0x20
-  __TEXT.__oslogstring: 0x2968
-  __TEXT.__swift5_capture: 0xb48
-  __TEXT.__swift5_builtin: 0x28
-  __TEXT.__unwind_info: 0x19f0
-  __TEXT.__eh_frame: 0x3288
+  __TEXT.__oslogstring: 0x28d8
+  __TEXT.__swift5_capture: 0xb58
+  __TEXT.__unwind_info: 0x1ad0
+  __TEXT.__eh_frame: 0x33e0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x430
+  __DATA_CONST.__objc_selrefs: 0x440
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x32e0
-  __AUTH_CONST.__objc_const: 0x2e80
-  __AUTH_CONST.__auth_got: 0x10b8
+  __AUTH_CONST.__const: 0x35d0
+  __AUTH_CONST.__objc_const: 0x2ea0
+  __AUTH_CONST.__auth_got: 0x1130
   __AUTH.__objc_data: 0xc20
-  __AUTH.__data: 0x1fc0
-  __DATA.__data: 0x1260
-  __DATA.__bss: 0x4b80
+  __AUTH.__data: 0x1fd0
+  __DATA.__data: 0x12c0
+  __DATA.__bss: 0x4e80
   __DATA.__common: 0x2c0
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Intents.framework/Versions/A/Intents
+  - /System/Library/Frameworks/NaturalLanguage.framework/Versions/A/NaturalLanguage
   - /System/Library/Frameworks/Translation.framework/Versions/A/Translation
   - /System/Library/PrivateFrameworks/DialogEngine.framework/Versions/A/DialogEngine
   - /System/Library/PrivateFrameworks/SAObjects.framework/Versions/A/SAObjects

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftRegexBuilder.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2575
-  Symbols:   970
-  CStrings:  365
+  Functions: 2648
+  Symbols:   987
+  CStrings:  391
 
Symbols:
+ _OBJC_CLASS_$_NLLanguageRecognizer
+ _associated conformance So10NLLanguageaSHSCSQ
+ _associated conformance So10NLLanguageas20_SwiftNewtypeWrapperSCSY
+ _associated conformance So10NLLanguageas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
+ _objc_msgSend$processString:
+ _objc_msgSend$setLanguageConstraints:
+ _swift_getForeignTypeMetadata
+ _symbolic $ss21_ObjectiveCBridgeableP
+ _symbolic SbIegd_
+ _symbolic So8NSStringC
+ _symbolic _____ 22SiriTranslationIntents11NLConverterC14ResolvedSourceV
+ _symbolic _____ So10NLLanguagea
+ _symbolic _____3key_Sd5valuet So10NLLanguagea
+ _symbolic _____Iegd_ s5Int32V
+ _symbolic _____Iegr_ s5Int32V
+ _symbolic _____y_____3key_Sd5valuetG s23_ContiguousArrayStorageC So10NLLanguagea
+ _symbolic _____y_____G s23_ContiguousArrayStorageC So10NLLanguagea
+ _type_layout_string So10NLLanguagea
- _OUTLINED_FUNCTION_136
CStrings:
+ "Capitalized intentPhrase: "
+ "DI src=%s toSrc=%{bool}d"
+ "IntentSourceLanguage: "
+ "IntentTargetLanguage: "
+ "Setting translateToSourceLanguage TRUE, intentPhrase is %s."
+ "Source unsupported in Siri and Translate app: %s"
+ "Will respond with unsupported translation because source language is the same as target language and Translate app is unavailable: %s"
+ "ar"
+ "de"
+ "en"
+ "es"
+ "fr"
+ "hi"
+ "id"
+ "intentSourceLanguage: "
+ "intentTargetLanguage: "
+ "it"
+ "ja"
+ "ko"
+ "macOS has no Translate app; translating inline: %s"
+ "nl"
+ "pl"
+ "pt"
+ "ru"
+ "th"
+ "tr"
+ "translateToSourceLanguage=TRUE (localized uso entity), intentPhrase=%s."
+ "tw"
+ "uk"
+ "vi"
+ "yue"
+ "zh"
- "Capitalized intentPhrase: %s intentSourceLanguage: %s"
- "IntentPhrase: %s IntentTargetLanguage: %s IntentSourceLanguage: %s Reference: %s"
- "Will offer user to use Translate App because source language is not the same as the current Siri locale: %s"
- "Will offer user to use Translate App for intent because source language is the same as target language: %s"
- "Will respond with unsupported translation because source language isn't supported in both Siri and Translate App: %s"
- "intentTargetLanguage: %s intentPhrase: %s intentSourceLanguage: %s"
```
