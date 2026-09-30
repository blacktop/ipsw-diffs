## MediaAnalysis

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/MediaAnalysis`

```diff

-345.77.1.3.0
-  __TEXT.__text: 0x3cac80
+375.6.1.0.0
+  __TEXT.__text: 0x3cad80
   __TEXT.__auth_stubs: 0x3f40
   __TEXT.__delay_stubs: 0x84
   __TEXT.__delay_helper: 0xa4
-  __TEXT.__objc_methlist: 0x1cd80
+  __TEXT.__objc_methlist: 0x1cd90
   __TEXT.__const: 0x14b58
-  __TEXT.__gcc_except_tab: 0x56964
+  __TEXT.__gcc_except_tab: 0x56980
   __TEXT.__cstring: 0x1964a
   __TEXT.__oslogstring: 0x2795b
   __TEXT.__dlopen_cstrs: 0x4b8

   __TEXT.__unwind_info: 0x10970
   __TEXT.__eh_frame: 0x940
   __TEXT.__objc_classname: 0x4363
-  __TEXT.__objc_methname: 0x3cc5e
-  __TEXT.__objc_methtype: 0xce0d
-  __TEXT.__objc_stubs: 0x292c0
+  __TEXT.__objc_methname: 0x3cc85
+  __TEXT.__objc_methtype: 0xce1b
+  __TEXT.__objc_stubs: 0x292e0
   __DATA_CONST.__got: 0x1cb8
   __DATA_CONST.__const: 0x6700
   __DATA_CONST.__objc_classlist: 0x1278
   __DATA_CONST.__objc_catlist: 0x1b8
   __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc968
+  __DATA_CONST.__objc_selrefs: 0xc970
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0xec8
   __DATA_CONST.__objc_arraydata: 0x11e0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: CB24A2FD-FE8C-3448-9D69-04CB91EAF1DF
-  Functions: 13266
-  Symbols:   48053
-  CStrings:  21227
+  UUID: 3E14B210-EFD6-30FC-B1AF-00C4506A523F
+  Functions: 13267
+  Symbols:   48056
+  CStrings:  21229
 
Symbols:
+ -[MADChangeRequest(Asset) setAnalysisVersion:forLocalIdentifier:]
+ _objc_msgSend$setAnalysisVersion:forLocalIdentifier:
Functions:
~ -[VCPMADImageSafetyClassificationTask run] : 4252 -> 4388
~ -[MADFetchRequest(BackgroundAnalysisProgressHistory) fetchAssetCountForTaskID:totalAssets:processedAssets:] : 620 -> 704
~ -[MADChangeRequest(Asset) bumpAnalysisVersionForAssetWithLocalIdentifier:] : 1024 -> 20
+ -[MADChangeRequest(Asset) setAnalysisVersion:forLocalIdentifier:]
~ __ZNKSt3__114default_deleteIN13sentencepiece4util6Status3RepEEclB8ne200100EPS4_ : 92 -> 112
CStrings:
+ "setAnalysisVersion:forLocalIdentifier:"
+ "text_safety_md7_v2.espresso.net"
+ "v28@0:8i16@20"
- "text_safety_md7_v1.espresso.net"

```
