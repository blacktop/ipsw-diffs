## TranslationDaemon

> `/System/Library/PrivateFrameworks/TranslationDaemon.framework/TranslationDaemon`

```diff

 350.1.0.0.0
-  __TEXT.__text: 0x1931e0
+  __TEXT.__text: 0x19337c
   __TEXT.__auth_stubs: 0xd20
   __TEXT.__objc_methlist: 0x19bc0
   __TEXT.__const: 0x450
   __TEXT.__gcc_except_tab: 0x1b308
-  __TEXT.__cstring: 0x5ac1
-  __TEXT.__oslogstring: 0xc0ac
+  __TEXT.__cstring: 0x5ad7
+  __TEXT.__oslogstring: 0xc0da
   __TEXT.__dlopen_cstrs: 0xb2
   __TEXT.__unwind_info: 0xf448
   __TEXT.__objc_classname: 0x4749
-  __TEXT.__objc_methname: 0x1b146
+  __TEXT.__objc_methname: 0x1b178
   __TEXT.__objc_methtype: 0xdfac
-  __TEXT.__objc_stubs: 0x128e0
-  __DATA_CONST.__got: 0xc98
+  __TEXT.__objc_stubs: 0x12940
+  __DATA_CONST.__got: 0xca0
   __DATA_CONST.__const: 0x3f50
   __DATA_CONST.__objc_classlist: 0x1198
   __DATA_CONST.__objc_catlist: 0x138
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6778
+  __DATA_CONST.__objc_selrefs: 0x6790
   __DATA_CONST.__objc_superrefs: 0x1108
-  __DATA_CONST.__objc_arraydata: 0x1a8
+  __DATA_CONST.__objc_arraydata: 0x230
   __AUTH_CONST.__auth_got: 0x6a8
   __AUTH_CONST.__const: 0xa80
-  __AUTH_CONST.__cfstring: 0x7660
+  __AUTH_CONST.__cfstring: 0x7680
   __AUTH_CONST.__objc_const: 0x2c470
-  __AUTH_CONST.__objc_arrayobj: 0xc0
+  __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x150

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libmorphun.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F445A13F-BC34-3D95-BCEC-C3A5A750438D
+  UUID: 27F12F27-99C8-3274-89F0-B5ABF9F4E610
   Functions: 9945
-  Symbols:   33778
-  CStrings:  9042
+  Symbols:   33782
+  CStrings:  9048
 
Symbols:
+ _OBJC_CLASS_$_LTTextUtilities
+ ___block_literal_global.394
+ _objc_msgSend$modelInfo
+ _objc_msgSend$tasks
+ _objc_msgSend$trimPrependingPunctuation:locale:
- ___block_literal_global.388
Functions:
~ +[_LTDASRAssetService isSupportedTaskHint:] : 32 -> 36
~ +[_LTDASRAssetService supportedLanguagesForTaskHint:] : 136 -> 176
~ +[_LTDASRAssetService _supportedGASRLocaleIdentifiers] : 116 -> 164
~ -[_LTDASRConfigurationModel assetTypeForTaskHint:localeIdentifier:] : 360 -> 364
~ -[_LTDASRConfigurationModel supportedLocaleIdentifiersForTaskHint:] : 364 -> 368
~ +[_LTDConfigurationService supportedLocalePairsForTask:error:] : 392 -> 396
~ ___67+[_LTDConfigurationService supportedIdentifiersForTask:completion:]_block_invoke : 344 -> 348
~ -[_LTDMAAssetModel supportsTaskHint:] : 52 -> 56
~ -[_LTDUAFAssetModel supportsTaskHint:] : 52 -> 56
~ -[_LTSpeechRecognitionResult(Daemon) _transcriptionWithResult:locale:] : 708 -> 772
~ ___99-[_LTSpeechRecognizer startRecognitionWithAutoStop:enableStreamingSpeechTranslation:resultHandler:]_block_invoke : 452 -> 684
CStrings:
+ "Falling back to task name: %@ for language %@"
+ "LiveTranscription"
+ "asr_languages_all"
+ "modelInfo"
+ "tasks"
+ "trimPrependingPunctuation:locale:"
- "asr_languages"

```
