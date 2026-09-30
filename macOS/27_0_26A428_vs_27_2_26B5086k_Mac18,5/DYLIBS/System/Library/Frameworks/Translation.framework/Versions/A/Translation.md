## Translation

> `/System/Library/Frameworks/Translation.framework/Versions/A/Translation`

### Sections with Same Size but Changed Content

- `__TEXT.__oslogstring`

```diff

-389.0.0.0.0
-  __TEXT.__text: 0x5faa4
-  __TEXT.__objc_methlist: 0x5e10
+393.1.0.0.0
+  __TEXT.__text: 0x5fe60
+  __TEXT.__objc_methlist: 0x5e88
   __TEXT.__const: 0xfa0
-  __TEXT.__cstring: 0x3464
+  __TEXT.__cstring: 0x34e4
   __TEXT.__oslogstring: 0x5336
   __TEXT.__gcc_except_tab: 0xb4c
   __TEXT.__ustring: 0x90

   __TEXT.__swift_as_entry: 0x4c
   __TEXT.__swift_as_ret: 0x50
   __TEXT.__swift_as_cont: 0x84
-  __TEXT.__unwind_info: 0x2488
+  __TEXT.__unwind_info: 0x24a0
   __TEXT.__eh_frame: 0x8c0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x6c8
+  __DATA_CONST.__const: 0x6d0
   __DATA_CONST.__objc_classlist: 0x330
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2898
+  __DATA_CONST.__objc_selrefs: 0x28c8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x2b0
   __DATA_CONST.__objc_arraydata: 0x1a0
   __DATA_CONST.__got: 0x5c8
-  __AUTH_CONST.__const: 0x2c40
-  __AUTH_CONST.__cfstring: 0x3e40
-  __AUTH_CONST.__objc_const: 0xc0f8
+  __AUTH_CONST.__const: 0x2c70
+  __AUTH_CONST.__cfstring: 0x3f40
+  __AUTH_CONST.__objc_const: 0xc1d8
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x920
-  __AUTH.__objc_data: 0x98
+  __AUTH.__objc_data: 0x138
   __AUTH.__data: 0x338
-  __DATA.__objc_ivar: 0x8e0
+  __DATA.__objc_ivar: 0x8f0
   __DATA.__data: 0xba0
   __DATA.__common: 0x30
-  __DATA_DIRTY.__objc_data: 0x1ec8
+  __DATA_DIRTY.__objc_data: 0x1e28
   __DATA_DIRTY.__data: 0x3a8
-  __DATA_DIRTY.__bss: 0xc0
+  __DATA_DIRTY.__bss: 0xb8
   __DATA_DIRTY.__common: 0x50
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2956
-  Symbols:   5433
-  CStrings:  952
+  Functions: 2968
+  Symbols:   5456
+  CStrings:  961
 
Symbols:
+ -[_LTLanguageDetectionConfiguration aiInferenceLocation]
+ -[_LTLanguageDetectionConfiguration setAiInferenceLocation:]
+ -[_LTLanguageStatusConfiguration allowsPrivateCloudComputeLanguages]
+ -[_LTLanguageStatusConfiguration isIndeterminate]
+ -[_LTLanguageStatusConfiguration setAllowsPrivateCloudComputeLanguages:]
+ -[_LTLanguageStatusConfiguration wantsAIStatusUpdates]
+ -[_LTTranslationContext aiInferenceLocation]
+ -[_LTTranslationContext setAiInferenceLocation:]
+ -[_LTTranslationRequest aiInferenceLocation]
+ -[_LTTranslationRequest setAiInferenceLocation:]
+ GCC_except_table144
+ GCC_except_table74
+ GCC_except_table78
+ GCC_except_table83
+ OBJC_IVAR_$__LTLanguageDetectionConfiguration._aiInferenceLocation
+ OBJC_IVAR_$__LTLanguageStatusConfiguration._allowsPrivateCloudComputeLanguages
+ OBJC_IVAR_$__LTTranslationContext._aiInferenceLocation
+ OBJC_IVAR_$__LTTranslationRequest._aiInferenceLocation
+ __LTAIInferenceLocationString
+ ___33-[_LTLanguageStatus cachedStatus]_block_invoke
+ ___block_descriptor_40_e8_32s_e14_"NSArray"8?0l
+ _objc_msgSend$aiInferenceLocation
+ _objc_msgSend$allowsPrivateCloudComputeLanguages
+ _objc_msgSend$setAiInferenceLocation:
+ _objc_msgSend$setAllowsPrivateCloudComputeLanguages:
- GCC_except_table142
- GCC_except_table81
CStrings:
+ "@\"NSArray\"8@?0"
+ "PCC-included"
+ "PCCLanguageExpansion"
+ "Using single-paragraph sub-request"
+ "ai-mt-expert-server"
+ "aiInferenceLocation"
+ "allowsPrivateCloudComputeLanguages"
+ "any"
+ "no-PCC"
+ "on-device"
+ "pcc"
- "Fallback to text to speech translation"
- "ai_adapter_inference"
```
