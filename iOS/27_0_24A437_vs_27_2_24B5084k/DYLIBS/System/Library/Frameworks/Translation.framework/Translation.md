## Translation

> `/System/Library/Frameworks/Translation.framework/Translation`

### Sections with Same Size but Changed Content

- `__TEXT.__oslogstring`

```diff

-389.1.0.0.0
-  __TEXT.__text: 0x59fac
-  __TEXT.__objc_methlist: 0x5e10
+393.1.0.0.0
+  __TEXT.__text: 0x5a190
+  __TEXT.__objc_methlist: 0x5e70
   __TEXT.__const: 0xf68
-  __TEXT.__cstring: 0x3464
+  __TEXT.__cstring: 0x3494
   __TEXT.__oslogstring: 0x5336
   __TEXT.__gcc_except_tab: 0xb44
   __TEXT.__ustring: 0x90

   __TEXT.__swift_as_entry: 0x4c
   __TEXT.__swift_as_ret: 0x50
   __TEXT.__swift_as_cont: 0x84
-  __TEXT.__unwind_info: 0x23c8
+  __TEXT.__unwind_info: 0x23d8
   __TEXT.__eh_frame: 0x8e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1ed0
+  __DATA_CONST.__const: 0x1f00
   __DATA_CONST.__objc_classlist: 0x330
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2898
+  __DATA_CONST.__objc_selrefs: 0x28b8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x2b0
   __DATA_CONST.__objc_arraydata: 0x1a0
   __DATA_CONST.__got: 0x5a0
   __AUTH_CONST.__const: 0x1050
-  __AUTH_CONST.__cfstring: 0x3e40
-  __AUTH_CONST.__objc_const: 0xc0f8
+  __AUTH_CONST.__cfstring: 0x3ec0
+  __AUTH_CONST.__objc_const: 0xc1a8
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0xa60
   __AUTH.__objc_data: 0x138
   __AUTH.__data: 0x338
-  __DATA.__objc_ivar: 0x8e0
+  __DATA.__objc_ivar: 0x8ec
   __DATA.__data: 0xb70
   __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0x1e28

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2897
-  Symbols:   5325
-  CStrings:  952
+  Functions: 2907
+  Symbols:   5342
+  CStrings:  956
 
Symbols:
+ -[_LTLanguageDetectionConfiguration aiInferenceLocation]
+ -[_LTLanguageDetectionConfiguration setAiInferenceLocation:]
+ -[_LTLanguageStatusConfiguration isIndeterminate]
+ -[_LTLanguageStatusConfiguration wantsAIStatusUpdates]
+ -[_LTTranslationContext aiInferenceLocation]
+ -[_LTTranslationContext setAiInferenceLocation:]
+ -[_LTTranslationRequest aiInferenceLocation]
+ -[_LTTranslationRequest setAiInferenceLocation:]
+ GCC_except_table133
+ GCC_except_table67
+ GCC_except_table70
+ GCC_except_table74
+ GCC_except_table77
+ _OBJC_IVAR_$__LTLanguageDetectionConfiguration._aiInferenceLocation
+ _OBJC_IVAR_$__LTTranslationContext._aiInferenceLocation
+ _OBJC_IVAR_$__LTTranslationRequest._aiInferenceLocation
+ __LTAIInferenceLocationString
+ ___33-[_LTLanguageStatus cachedStatus]_block_invoke
+ ___block_descriptor_40_e8_32s_e14_"NSArray"8?0ls32l8
+ _objc_msgSend$aiInferenceLocation
+ _objc_msgSend$setAiInferenceLocation:
- GCC_except_table131
- GCC_except_table68
- GCC_except_table72
- GCC_except_table75
CStrings:
+ "@\"NSArray\"8@?0"
+ "Using single-paragraph sub-request"
+ "ai-mt-expert-server"
+ "aiInferenceLocation"
+ "any"
+ "on-device"
- "Fallback to text to speech translation"
- "ai_adapter_inference"
```
