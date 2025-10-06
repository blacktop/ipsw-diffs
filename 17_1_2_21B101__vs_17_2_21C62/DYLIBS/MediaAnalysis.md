## MediaAnalysis

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/MediaAnalysis`

```diff

-200.8.1.0.0
-  __TEXT.__text: 0x2abb7c
+205.6.1.0.0
+  __TEXT.__text: 0x2abffc
   __TEXT.__auth_stubs: 0x2da0
-  __TEXT.__objc_methlist: 0x15590
+  __TEXT.__objc_methlist: 0x15598
   __TEXT.__const: 0x13000
-  __TEXT.__gcc_except_tab: 0x39b78
-  __TEXT.__cstring: 0x101fb
-  __TEXT.__oslogstring: 0x1a051
+  __TEXT.__gcc_except_tab: 0x39c28
+  __TEXT.__cstring: 0x1023b
+  __TEXT.__oslogstring: 0x1a023
   __TEXT.__dlopen_cstrs: 0x4a3
   __TEXT.__ustring: 0x40
   __TEXT.__swift5_typeref: 0x4f

   __TEXT.__swift5_reflstr: 0xd
   __TEXT.__swift5_fieldmd: 0x28
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0xc1e4
+  __TEXT.__unwind_info: 0xc1f0
   __TEXT.__eh_frame: 0x168
   __TEXT.__objc_classname: 0x3221
-  __TEXT.__objc_methname: 0x31088
-  __TEXT.__objc_methtype: 0xb407
-  __TEXT.__objc_stubs: 0x21900
+  __TEXT.__objc_methname: 0x310d6
+  __TEXT.__objc_methtype: 0xb40d
+  __TEXT.__objc_stubs: 0x21920
   __DATA_CONST.__got: 0xd38
   __DATA_CONST.__const: 0x5528
   __DATA_CONST.__objc_classlist: 0xdd0

   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x20858
-  __DATA_CONST.__objc_selrefs: 0x9d48
+  __DATA_CONST.__objc_selrefs: 0x9d50
   __DATA_CONST.__objc_arraydata: 0xd98
   __AUTH_CONST.__objc_floatobj: 0x1c0
   __AUTH_CONST.__objc_const: 0x240
-  __AUTH_CONST.__cfstring: 0x105c0
+  __AUTH_CONST.__cfstring: 0x105e0
   __AUTH_CONST.__objc_doubleobj: 0x3c0
   __AUTH_CONST.__objc_intobj: 0x2400
   __AUTH_CONST.__objc_arrayobj: 0x858

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 75D696A1-21B8-316F-AA14-0A3BFA0ECD7D
-  Functions: 9736
-  Symbols:   35855
-  CStrings:  15943
+  UUID: 92027F46-3764-3074-A917-551371E67BA4
+  Functions: 9737
+  Symbols:   35859
+  CStrings:  15947
 
Symbols:
+ +[VCPFaceUtils isBestResourceForFaceProcessing:fromResources:]
+ -[VCPFaceAnalyzer _refineAnalysis:requestHandler:forAsset:resource:isBestResource:orientedWidth:orientedHeight:]
+ -[VCPFaceAnalyzer analyzeAsset:withResource:resourceURL:isBestResource:quickMode:results:]
+ _objc_msgSend$_refineAnalysis:requestHandler:forAsset:resource:isBestResource:orientedWidth:orientedHeight:
+ _objc_msgSend$analyzeAsset:withResource:resourceURL:isBestResource:quickMode:results:
+ _objc_msgSend$isBestResourceForFaceProcessing:fromResources:
- -[VCPFaceAnalyzer _refineAnalysis:requestHandler:forAsset:resource:orientedWidth:orientedHeight:]
- -[VCPFaceAnalyzer analyzeAsset:withResource:resourceURL:quickMode:results:]
- _objc_msgSend$_refineAnalysis:requestHandler:forAsset:resource:orientedWidth:orientedHeight:
- _objc_msgSend$analyzeAsset:withResource:resourceURL:quickMode:results:
CStrings:
+ "%@ Face faceprint version %d"
+ "%@ face-%.3f|%dpx(%dpx), torso-%.3fx%.3f|%dpx(%dpx)"
+ "DisableSubjectLiftingIVS"
+ "Scaler: sets CleanAperture on input pixel buffer (not iosurface-backed)"
+ "[FaceAnalyzer][FC][SmallFace][%@][%@]"
+ "_refineAnalysis:requestHandler:forAsset:resource:isBestResource:orientedWidth:orientedHeight:"
+ "analyzeAsset:withResource:resourceURL:isBestResource:quickMode:results:"
+ "i56@0:8@16@24@32B40B44^@48"
+ "i68@0:8^@16@24@32@40B48Q52Q60"
+ "isBestResourceForFaceProcessing:fromResources:"
- "[FaceAnalyzer][FC][SmallFace][%@] Face faceprint version %d"
- "[FaceAnalyzer][FC][SmallFace][%@] Ignore non-human face"
- "[FaceAnalyzer][FC][SmallFace][%@] face-%.3f|%dpx(%dpx), torso-%.3fx%.3f|%dpx(%dpx)"
- "_refineAnalysis:requestHandler:forAsset:resource:orientedWidth:orientedHeight:"
- "analyzeAsset:withResource:resourceURL:quickMode:results:"
- "i52@0:8@16@24@32B40^@44"
- "i64@0:8^@16@24@32@40Q48Q56"

```
