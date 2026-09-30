## PhotoImaging

> `/System/Library/PrivateFrameworks/PhotoImaging.framework/PhotoImaging`

```diff

-830.0.111.0.0
-  __TEXT.__text: 0x19bb7c
+830.0.140.0.0
+  __TEXT.__text: 0x19bc1c
   __TEXT.__auth_stubs: 0x2160
-  __TEXT.__delay_helper: 0x158
+  __TEXT.__delay_helper: 0x1bc
   __TEXT.__objc_methlist: 0x10cc0
   __TEXT.__const: 0x80c4
   __TEXT.__dlopen_cstrs: 0x23a

   __TEXT.__unwind_info: 0x3e58
   __TEXT.__eh_frame: 0x2d0
   __TEXT.__objc_classname: 0x2b04
-  __TEXT.__objc_methname: 0x2840e
-  __TEXT.__objc_methtype: 0x4295
+  __TEXT.__objc_methname: 0x2841d
+  __TEXT.__objc_methtype: 0x42a6
   __TEXT.__objc_stubs: 0x1e580
   __DATA_CONST.__got: 0x1d38
   __DATA_CONST.__const: 0x30f0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D658DAEC-4345-37B9-BD38-28744D89E871
+  UUID: 87309DB7-5E26-3CA4-A6B2-C11D43098236
   Functions: 6559
   Symbols:   23343
-  CStrings:  14366
+  CStrings:  14367
 
Symbols:
+ +[PISegmentationHelper topEdgeHasNoContactWithInspectionMatte:classification:context:]
+ _objc_msgSend$topEdgeHasNoContactWithInspectionMatte:classification:context:
- +[PISegmentationHelper topEdgeHasNoContactWithInspectionMatte:context:]
- _objc_msgSend$topEdgeHasNoContactWithInspectionMatte:context:
Functions:
~ -[PIParallaxSegmentationItem saveSegmentationDataToURL:error:] : 2344 -> 2460
~ +[PISegmentationHelper topEdgeHasNoContactWithInspectionMatte:context:] -> +[PISegmentationHelper topEdgeHasNoContactWithInspectionMatte:classification:context:] : 264 -> 284
~ -[_PIPosterLayoutJob generateOrientedLayoutsForFullExtent:layoutConfiguration:layoutRegions:segmentationMatteImage:segmentationClassification:error:] : 4500 -> 4524
CStrings:
+ "B40@0:8@16Q24@32"
+ "topEdgeHasNoContactWithInspectionMatte:classification:context:"
- "topEdgeHasNoContactWithInspectionMatte:context:"

```
