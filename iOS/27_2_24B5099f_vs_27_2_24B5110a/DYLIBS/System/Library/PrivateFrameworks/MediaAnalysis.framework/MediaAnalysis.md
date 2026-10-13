## MediaAnalysis

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/MediaAnalysis`

```diff

-460.12.1.0.0
-  __TEXT.__text: 0x4c518c
+460.14.1.1.0
+  __TEXT.__text: 0x4c5548
   __TEXT.__delay_stubs: 0xc0
   __TEXT.__delay_helper: 0x284
-  __TEXT.__objc_methlist: 0x22d60
-  __TEXT.__const: 0x16608
-  __TEXT.__gcc_except_tab: 0x686bc
-  __TEXT.__cstring: 0x2cef1
-  __TEXT.__oslogstring: 0x3312b
+  __TEXT.__objc_methlist: 0x22d80
+  __TEXT.__const: 0x16638
+  __TEXT.__gcc_except_tab: 0x68700
+  __TEXT.__cstring: 0x2cf21
+  __TEXT.__oslogstring: 0x331eb
   __TEXT.__dlopen_cstrs: 0x4b8
   __TEXT.__ustring: 0x40
   __TEXT.__swift5_typeref: 0x9dc

   __TEXT.__swift_as_ret: 0x90
   __TEXT.__swift_as_cont: 0xd8
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x18938
+  __TEXT.__unwind_info: 0x18950
   __TEXT.__eh_frame: 0x1a30
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x7c90
+  __DATA_CONST.__const: 0x7c98
   __DATA_CONST.__objc_classlist: 0x15c0
   __DATA_CONST.__objc_catlist: 0x1c8
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0xf198
+  __DATA_CONST.__objc_selrefs: 0xf1a0
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0xfa8
-  __DATA_CONST.__objc_arraydata: 0x12c8
+  __DATA_CONST.__objc_arraydata: 0x12e8
   __DATA_CONST.__got: 0x2578
   __AUTH_CONST.__const: 0x75e8
   __AUTH_CONST.__cfstring: 0x1ed60
-  __AUTH_CONST.__objc_const: 0x41de8
+  __AUTH_CONST.__objc_const: 0x41df8
   __AUTH_CONST.__weak_auth_got: 0x80
   __AUTH_CONST.__objc_floatobj: 0x300
-  __AUTH_CONST.__objc_arrayobj: 0xd08
+  __AUTH_CONST.__objc_arrayobj: 0xd20
   __AUTH_CONST.__objc_doubleobj: 0x490
-  __AUTH_CONST.__objc_intobj: 0x3930
+  __AUTH_CONST.__objc_intobj: 0x3948
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__auth_got: 0x2590
   __AUTH.__objc_data: 0x50

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 20216
-  Symbols:   28628
-  CStrings:  9033
+  Functions: 20221
+  Symbols:   28631
+  CStrings:  9036
 
Symbols:
+ -[MADServicePhotosVideoAsset isPhotosAsset]
+ -[MADServiceVideoAsset isPhotosAsset]
+ -[MADServiceVideoSafetyProcessingTask storeSafetyClassificationResults]
+ __ZL17shapeElementCountP7NSArrayIP8NSNumberE
- -[MADServiceVideoSafetyProcessingTask storeSafetyClassificationResultsForSharedAsset]
CStrings:
+ "Failed to generate MADImageEmbeddingResult: expected shape %@ (%lu fp16 elements), got %lu elements"
+ "Failed to populate the composition from the original asset (%@)"
+ "Missing video track (processed %lu, composition %lu)"
+ "VCPMADImageEmbeddingTask expected shape %@ (%lu fp16 elements) but got %lu elements"
+ "[%@] Failed to obtain analysis result for Photos asset."
- "Failed to generate MADImageEmbeddingResult"
- "[%@] Failed to obtain analysis result for shared Photos asset."
```
