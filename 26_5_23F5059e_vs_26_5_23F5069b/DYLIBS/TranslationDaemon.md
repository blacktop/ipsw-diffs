## TranslationDaemon

> `/System/Library/PrivateFrameworks/TranslationDaemon.framework/TranslationDaemon`

```diff

-365.10.0.0.0
-  __TEXT.__text: 0x1af4fc
+365.13.0.0.0
+  __TEXT.__text: 0x1af97c
   __TEXT.__auth_stubs: 0x1900
-  __TEXT.__objc_methlist: 0x1a118
-  __TEXT.__const: 0xa14
-  __TEXT.__gcc_except_tab: 0x1b36c
+  __TEXT.__objc_methlist: 0x1a148
+  __TEXT.__const: 0xa34
+  __TEXT.__gcc_except_tab: 0x1b390
   __TEXT.__cstring: 0x5f83
-  __TEXT.__oslogstring: 0xceff
+  __TEXT.__oslogstring: 0xcf40
   __TEXT.__dlopen_cstrs: 0xb2
-  __TEXT.__swift5_typeref: 0x355
+  __TEXT.__swift5_typeref: 0x35f
   __TEXT.__swift5_capture: 0xd0
   __TEXT.__constg_swiftt: 0x118
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_reflstr: 0x63
-  __TEXT.__swift5_fieldmd: 0xd0
+  __TEXT.__swift5_reflstr: 0x83
+  __TEXT.__swift5_fieldmd: 0xdc
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x40
   __TEXT.__swift5_types: 0x18
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0xc
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0xf9d8
+  __TEXT.__unwind_info: 0xf9e8
   __TEXT.__eh_frame: 0x400
   __TEXT.__objc_classname: 0x486e
-  __TEXT.__objc_methname: 0x1bf9f
+  __TEXT.__objc_methname: 0x1c0bf
   __TEXT.__objc_methtype: 0xe256
-  __TEXT.__objc_stubs: 0x13160
+  __TEXT.__objc_stubs: 0x131e0
   __DATA_CONST.__got: 0xeb8
   __DATA_CONST.__const: 0x42e0
   __DATA_CONST.__objc_classlist: 0x11c8
   __DATA_CONST.__objc_catlist: 0x138
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x69f8
+  __DATA_CONST.__objc_selrefs: 0x6a18
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x1120
   __DATA_CONST.__objc_arraydata: 0x3c0
   __AUTH_CONST.__auth_got: 0xc98
-  __AUTH_CONST.__const: 0x1058
+  __AUTH_CONST.__const: 0x1080
   __AUTH_CONST.__cfstring: 0x7aa0
-  __AUTH_CONST.__objc_const: 0x2ce20
+  __AUTH_CONST.__objc_const: 0x2ceb0
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_intobj: 0x348
   __AUTH_CONST.__objc_dictobj: 0xc8

   __AUTH.__objc_data: 0xa5d8
   __AUTH.__data: 0x108
   __DATA.__objc_ivar: 0x11cc
-  __DATA.__data: 0xdb0
+  __DATA.__data: 0xdc8
   __DATA.__bss: 0x8d0
   __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0xc58

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 21AD662E-E9CA-3E4F-9566-148434A5B295
-  Functions: 10344
-  Symbols:   34633
-  CStrings:  9340
+  UUID: EB4627CE-DB47-30D4-9EB7-F2228A871BB8
+  Functions: 10354
+  Symbols:   34640
+  CStrings:  9349
 
Symbols:
+ ___49-[_LTTranslationServer scheduleAssetCleanupWork:]_block_invoke.84
+ ___59-[_LTTranslationServer installedLocalesForTask:completion:]_block_invoke.78
+ ___63-[_LTTranslationServer _lidSupportedLocalesForTask:completion:]_block_invoke.70
+ ___63-[_LTTranslationServer _lidSupportedLocalesForTask:completion:]_block_invoke.75
+ ___63-[_LTTranslationServer _lidSupportedLocalesForTask:completion:]_block_invoke_2.74
+ ___63-[_LTTranslationServer _lidSupportedLocalesForTask:completion:]_block_invoke_2.76
+ ___81-[_LTTranslationServer languagesForText:usingModel:strategy:taskHint:completion:]_block_invoke_2
+ ___block_literal_global.63
+ ___block_literal_global.68
+ ___block_literal_global.81
+ _objc_msgSend$appleIntelligenceIsAvailable
+ _objc_msgSend$appleIntelligenceIsReadyToTranslate
+ _objc_msgSend$appleIntelligenceIsSupported
+ _objc_msgSend$clearCachedValuesForStatusChange
+ _symbolic Say_____G 10Foundation6LocaleV
+ _type_layout_string 17TranslationDaemon24DefaultLLMStatusProviderV
- ___49-[_LTTranslationServer scheduleAssetCleanupWork:]_block_invoke.83
- ___59-[_LTTranslationServer installedLocalesForTask:completion:]_block_invoke.77
- ___63-[_LTTranslationServer _lidSupportedLocalesForTask:completion:]_block_invoke.68
- ___63-[_LTTranslationServer _lidSupportedLocalesForTask:completion:]_block_invoke.74
- ___63-[_LTTranslationServer _lidSupportedLocalesForTask:completion:]_block_invoke_2.72
- ___63-[_LTTranslationServer _lidSupportedLocalesForTask:completion:]_block_invoke_2.75
- ___81-[_LTTranslationServer languagesForText:usingModel:strategy:taskHint:completion:]_block_invoke.cold.1
- ___block_literal_global.65
- ___block_literal_global.71
- ___block_literal_global.80
CStrings:
+ "Got request to LID %zu string(s)"
+ "Languages for text result: %{public}@"
+ "Supported locales for LID: %{public}@"
+ "appleIntelligenceIsAvailable"
+ "appleIntelligenceIsReadyToTranslate"
+ "appleIntelligenceIsSupported"
+ "cachedAppleIntelligenceIsAvailable"
+ "cachedAppleIntelligenceIsReadyToTranslate"
+ "cachedAppleIntelligenceIsSupported"
+ "clearCachedValuesForStatusChange"
- "XPC languages for text result: %{public}@"

```
