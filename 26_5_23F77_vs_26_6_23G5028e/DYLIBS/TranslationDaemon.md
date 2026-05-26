## TranslationDaemon

> `/System/Library/PrivateFrameworks/TranslationDaemon.framework/TranslationDaemon`

```diff

-365.13.0.0.0
-  __TEXT.__text: 0x1af97c
+365.14.0.0.0
+  __TEXT.__text: 0x1afb78
   __TEXT.__auth_stubs: 0x1900
-  __TEXT.__objc_methlist: 0x1a148
+  __TEXT.__objc_methlist: 0x1a150
   __TEXT.__const: 0xa34
-  __TEXT.__gcc_except_tab: 0x1b390
+  __TEXT.__gcc_except_tab: 0x1b398
   __TEXT.__cstring: 0x5f83
   __TEXT.__oslogstring: 0xcf40
   __TEXT.__dlopen_cstrs: 0xb2

   __TEXT.__unwind_info: 0xf9e8
   __TEXT.__eh_frame: 0x400
   __TEXT.__objc_classname: 0x486e
-  __TEXT.__objc_methname: 0x1c0bf
+  __TEXT.__objc_methname: 0x1c15f
   __TEXT.__objc_methtype: 0xe256
-  __TEXT.__objc_stubs: 0x131e0
-  __DATA_CONST.__got: 0xeb8
+  __TEXT.__objc_stubs: 0x13280
+  __DATA_CONST.__got: 0xec0
   __DATA_CONST.__const: 0x42e0
   __DATA_CONST.__objc_classlist: 0x11c8
   __DATA_CONST.__objc_catlist: 0x138
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6a18
+  __DATA_CONST.__objc_selrefs: 0x6a40
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x1120
   __DATA_CONST.__objc_arraydata: 0x3c0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: EB4627CE-DB47-30D4-9EB7-F2228A871BB8
-  Functions: 10354
-  Symbols:   34640
-  CStrings:  9349
+  UUID: 0016C9A1-D58B-317F-8ACE-D507079E613F
+  Functions: 10355
+  Symbols:   34648
+  CStrings:  9353
 
Symbols:
+ -[_LTClientConnection languagesForText:configuration:completion:]
+ -[_LTTranslationServer _lidSupportedLanguagesFromAssetCacheForConfiguration:completion:]
+ -[_LTTranslationServer _lidSupportedLocalesForConfiguration:completion:]
+ -[_LTTranslationServer languagesForText:configuration:completion:]
+ _OBJC_CLASS_$__LTLanguageDetectionConfiguration
+ ___49-[_LTTranslationServer scheduleAssetCleanupWork:]_block_invoke.83
+ ___59-[_LTTranslationServer installedLocalesForTask:completion:]_block_invoke.77
+ ___66-[_LTTranslationServer languagesForText:configuration:completion:]_block_invoke
+ ___66-[_LTTranslationServer languagesForText:configuration:completion:]_block_invoke_2
+ ___72-[_LTTranslationServer _lidSupportedLocalesForConfiguration:completion:]_block_invoke
+ ___72-[_LTTranslationServer _lidSupportedLocalesForConfiguration:completion:]_block_invoke_2
+ ___88-[_LTTranslationServer _lidSupportedLanguagesFromAssetCacheForConfiguration:completion:]_block_invoke
+ ___88-[_LTTranslationServer _lidSupportedLanguagesFromAssetCacheForConfiguration:completion:]_block_invoke.71
+ ___88-[_LTTranslationServer _lidSupportedLanguagesFromAssetCacheForConfiguration:completion:]_block_invoke.75
+ ___88-[_LTTranslationServer _lidSupportedLanguagesFromAssetCacheForConfiguration:completion:]_block_invoke_2
+ ___88-[_LTTranslationServer _lidSupportedLanguagesFromAssetCacheForConfiguration:completion:]_block_invoke_3
+ ___88-[_LTTranslationServer _lidSupportedLanguagesFromAssetCacheForConfiguration:completion:]_block_invoke_3.cold.1
+ ___block_descriptor_72_e8_32s40s48s56bs64w_e17_v16?0"NSArray"8lw64l8s32l8s40l8s48l8s56l8
+ ___block_literal_global.64
+ ___block_literal_global.74
+ ___block_literal_global.80
+ _objc_msgSend$_lidSupportedLanguagesFromAssetCacheForConfiguration:completion:
+ _objc_msgSend$_lidSupportedLocalesForConfiguration:completion:
+ _objc_msgSend$initWithTaskHint:
+ _objc_msgSend$languagesForText:configuration:completion:
+ _objc_msgSend$lt_stringByReplacingInvalidUTF8Characters
+ _objc_msgSend$model
+ _objc_msgSend$strategy
- -[_LTClientConnection languagesForText:usingModel:strategy:taskHint:completion:]
- -[_LTTranslationServer _lidSupportedLocalesForTask:completion:]
- -[_LTTranslationServer languagesForText:usingModel:strategy:taskHint:completion:]
- ___49-[_LTTranslationServer scheduleAssetCleanupWork:]_block_invoke.84
- ___59-[_LTTranslationServer installedLocalesForTask:completion:]_block_invoke.78
- ___63-[_LTTranslationServer _lidSupportedLocalesForTask:completion:]_block_invoke
- ___63-[_LTTranslationServer _lidSupportedLocalesForTask:completion:]_block_invoke.70
- ___63-[_LTTranslationServer _lidSupportedLocalesForTask:completion:]_block_invoke.75
- ___63-[_LTTranslationServer _lidSupportedLocalesForTask:completion:]_block_invoke_2
- ___63-[_LTTranslationServer _lidSupportedLocalesForTask:completion:]_block_invoke_2.74
- ___63-[_LTTranslationServer _lidSupportedLocalesForTask:completion:]_block_invoke_2.76
- ___63-[_LTTranslationServer _lidSupportedLocalesForTask:completion:]_block_invoke_3
- ___63-[_LTTranslationServer _lidSupportedLocalesForTask:completion:]_block_invoke_3.cold.1
- ___81-[_LTTranslationServer languagesForText:usingModel:strategy:taskHint:completion:]_block_invoke
- ___81-[_LTTranslationServer languagesForText:usingModel:strategy:taskHint:completion:]_block_invoke_2
- ___block_descriptor_80_e8_32s40s48bs56w_e17_v16?0"NSArray"8lw56l8s32l8s40l8s48l8
- ___block_literal_global.63
- ___block_literal_global.68
- ___block_literal_global.81
- _objc_msgSend$_lidSupportedLocalesForTask:completion:
- _objc_msgSend$languagesForText:usingModel:strategy:taskHint:completion:
CStrings:
+ "_lidSupportedLanguagesFromAssetCacheForConfiguration:completion:"
+ "_lidSupportedLocalesForConfiguration:completion:"
+ "initWithTaskHint:"
+ "languagesForText:configuration:completion:"
+ "lt_stringByReplacingInvalidUTF8Characters"
+ "model"
+ "strategy"
+ "v40@0:8@\"NSArray\"16@\"_LTLanguageDetectionConfiguration\"24@?<v@?@\"_LTTextLanguageDetectionResult\">32"
- "_lidSupportedLocalesForTask:completion:"
- "languagesForText:usingModel:strategy:taskHint:completion:"
- "v56@0:8@\"NSArray\"16Q24Q32q40@?<v@?@\"_LTTextLanguageDetectionResult\">48"
- "v56@0:8@16Q24Q32q40@?48"

```
