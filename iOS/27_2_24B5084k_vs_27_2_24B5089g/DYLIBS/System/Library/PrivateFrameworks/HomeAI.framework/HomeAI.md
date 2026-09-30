## HomeAI

> `/System/Library/PrivateFrameworks/HomeAI.framework/HomeAI`

```diff

-381.0.0.0.0
-  __TEXT.__text: 0x17a9e4
+382.0.0.0.0
+  __TEXT.__text: 0x17af04
   __TEXT.__init_offsets: 0x10
-  __TEXT.__objc_methlist: 0xa67c
+  __TEXT.__objc_methlist: 0xa6b4
   __TEXT.__const: 0x497d
-  __TEXT.__cstring: 0xda5c
-  __TEXT.__gcc_except_tab: 0xc210
-  __TEXT.__oslogstring: 0xe87d
+  __TEXT.__cstring: 0xdb8d
+  __TEXT.__gcc_except_tab: 0xc234
+  __TEXT.__oslogstring: 0xe8b0
   __TEXT.__dlopen_cstrs: 0x16e
   __TEXT.__swift5_typeref: 0x21
   __TEXT.__constg_swiftt: 0x28
   __TEXT.__swift5_reflstr: 0x74
   __TEXT.__swift5_fieldmd: 0x4c
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x5b70
+  __TEXT.__unwind_info: 0x5b80
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3998
+  __DATA_CONST.__const: 0x39a0
   __DATA_CONST.__objc_classlist: 0x718
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x4820
+  __DATA_CONST.__objc_selrefs: 0x4848
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x610
   __DATA_CONST.__objc_arraydata: 0x6e8
   __DATA_CONST.__got: 0xc48
   __AUTH_CONST.__const: 0x48b0
-  __AUTH_CONST.__cfstring: 0x8ae0
-  __AUTH_CONST.__objc_const: 0x16420
+  __AUTH_CONST.__cfstring: 0x8c40
+  __AUTH_CONST.__objc_const: 0x16480
   __AUTH_CONST.__weak_auth_got: 0x28
-  __AUTH_CONST.__objc_intobj: 0x588
+  __AUTH_CONST.__objc_intobj: 0x570
   __AUTH_CONST.__objc_arrayobj: 0x390
   __AUTH_CONST.__objc_doubleobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x1b8

   __AUTH_CONST.__auth_got: 0xe98
   __AUTH.__objc_data: 0x42e0
   __AUTH.__data: 0x350
-  __DATA.__objc_ivar: 0xd64
+  __DATA.__objc_ivar: 0xd6c
   __DATA.__data: 0xd3c
   __DATA_DIRTY.__objc_data: 0x410
   __DATA_DIRTY.__bss: 0x2d8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5516
-  Symbols:   12195
-  CStrings:  3222
+  Functions: 5524
+  Symbols:   12207
+  CStrings:  3233
 
Symbols:
+ +[NSError(HMIError) hmiErrorWithCode:reason:]
+ -[HMIVideoAnalyzerConfiguration fragmentBufferDuration]
+ -[HMIVideoAnalyzerConfiguration setFragmentBufferDuration:]
+ -[HMIVideoGenerativeAnalysisResult initWithRequestUUID:clipUUID:embeddingsByVersion:caption:histogramsByEventType:modelIdentifier:isHistogramDuplicate:isEmbeddingDuplicate:isDegraded:error:]
+ -[HMIVideoGenerativeAnalysisResult isDegraded]
+ _HMIFragmentBufferDurationKey
+ _OBJC_IVAR_$_HMIVideoAnalyzerConfiguration._fragmentBufferDuration
+ _OBJC_IVAR_$_HMIVideoGenerativeAnalysisResult._isDegraded
+ ___block_descriptor_104_e8_32s40r48r56r64r72r80r88r96r_e28_v24?0"MADHKSVCaption"8^B16lr40l8s32l8r48l8r56l8r64l8r72l8r80l8r88l8r96l8
+ _objc_msgSend$fragmentBufferDuration
+ _objc_msgSend$hmiErrorWithCode:reason:
+ _objc_msgSend$initWithRequestUUID:clipUUID:embeddingsByVersion:caption:histogramsByEventType:modelIdentifier:isHistogramDuplicate:isEmbeddingDuplicate:isDegraded:error:
+ _objc_msgSend$isDegraded
+ _objc_msgSend$setFragmentBufferDuration:
- ___block_descriptor_96_e8_32s40r48r56r64r72r80r88r_e28_v24?0"MADHKSVCaption"8^B16lr40l8s32l8r48l8r56l8r64l8r72l8r80l8r88l8
- _objc_msgSend$hmiPrivateErrorWithCode:reason:
CStrings:
+ "Caption flagged as sensitive content"
+ "Caption flagged as unsafe content"
+ "Caption parsing failed"
+ "Fragment Buffer Duration"
+ "HMIErrorCodeCaptionNoActivity"
+ "HMIErrorCodeCaptionParsingFailed"
+ "HMIErrorCodeCaptionSensitiveContent"
+ "HMIErrorCodeCaptionUnsafeContent"
+ "Is Degraded"
+ "Result is degraded"
+ "[%{public}@] Result is degraded"
+ "fragmentBufferDurationSeconds"
- "fragmentBufferSize"
```
