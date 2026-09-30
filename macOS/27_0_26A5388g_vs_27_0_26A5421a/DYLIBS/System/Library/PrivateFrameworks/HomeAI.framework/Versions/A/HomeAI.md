## HomeAI

> `/System/Library/PrivateFrameworks/HomeAI.framework/Versions/A/HomeAI`

```diff

-377.0.0.0.0
-  __TEXT.__text: 0x182564
+378.0.0.0.0
+  __TEXT.__text: 0x182844
   __TEXT.__init_offsets: 0x10
-  __TEXT.__objc_methlist: 0x9f6c
+  __TEXT.__objc_methlist: 0x9fb4
   __TEXT.__const: 0x492d
-  __TEXT.__cstring: 0xd9a8
+  __TEXT.__cstring: 0xd9e9
   __TEXT.__gcc_except_tab: 0xc04c
   __TEXT.__oslogstring: 0xda01
   __TEXT.__swift5_typeref: 0x21

   __TEXT.__swift5_reflstr: 0x74
   __TEXT.__swift5_fieldmd: 0x4c
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x5008
+  __TEXT.__unwind_info: 0x5010
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x4628
+  __DATA_CONST.__objc_selrefs: 0x4658
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x5d8
   __DATA_CONST.__objc_arraydata: 0x618
   __DATA_CONST.__got: 0xbc8
   __AUTH_CONST.__const: 0x79f0
-  __AUTH_CONST.__cfstring: 0x87a0
-  __AUTH_CONST.__objc_const: 0x155e0
+  __AUTH_CONST.__cfstring: 0x8800
+  __AUTH_CONST.__objc_const: 0x15670
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x570
   __AUTH_CONST.__objc_arrayobj: 0x360

   __AUTH_CONST.__auth_got: 0xd48
   __AUTH.__objc_data: 0x4150
   __AUTH.__data: 0x350
-  __DATA.__objc_ivar: 0xcb0
+  __DATA.__objc_ivar: 0xcbc
   __DATA.__data: 0xd3c
   __DATA.__bss: 0x3f0
   __DATA_DIRTY.__objc_data: 0x370

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5401
-  Symbols:   11896
-  CStrings:  3096
+  Functions: 5407
+  Symbols:   11910
+  CStrings:  3099
 
Symbols:
+ -[HMIVideoGenerativeAnalysisResult initWithRequestUUID:clipUUID:embeddingsByVersion:caption:histogramsByEventType:modelIdentifier:isHistogramDuplicate:isEmbeddingDuplicate:error:]
+ -[HMIVideoGenerativeAnalysisResult initWithRequestUUID:clipUUID:error:]
+ -[HMIVideoGenerativeAnalysisResult initWithRequestUUID:clipUUID:modelIdentifier:error:]
+ -[HMIVideoGenerativeAnalysisResult isEmbeddingDuplicate]
+ -[HMIVideoGenerativeAnalysisResult isHistogramDuplicate]
+ -[HMIVideoGenerativeAnalysisResult modelIdentifier]
+ OBJC_IVAR_$_HMIVideoGenerativeAnalysisResult._isEmbeddingDuplicate
+ OBJC_IVAR_$_HMIVideoGenerativeAnalysisResult._isHistogramDuplicate
+ OBJC_IVAR_$_HMIVideoGenerativeAnalysisResult._modelIdentifier
+ _objc_msgSend$initWithRequestUUID:clipUUID:embeddingsByVersion:caption:histogramsByEventType:modelIdentifier:isHistogramDuplicate:isEmbeddingDuplicate:error:
+ _objc_msgSend$initWithRequestUUID:clipUUID:error:
+ _objc_msgSend$initWithRequestUUID:clipUUID:modelIdentifier:error:
+ _objc_msgSend$isEmbeddingDuplicate
+ _objc_msgSend$isHistogramDuplicate
+ _objc_msgSend$modelIdentifier
- _objc_msgSend$initWithRequestUUID:error:
CStrings:
+ "Is Embedding Duplicate"
+ "Is Histogram Duplicate"
+ "Model Identifier"
```
