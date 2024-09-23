## Vision

> `/System/Library/Frameworks/Vision.framework/Vision`

```diff

-8.0.39.0.0
-  __TEXT.__text: 0x3a7c70
-  __TEXT.__auth_stubs: 0x4180
-  __TEXT.__objc_methlist: 0x17f8c
-  __TEXT.__cstring: 0x265a2
-  __TEXT.__swift5_typeref: 0x61b0
-  __TEXT.__const: 0x370d0
-  __TEXT.__swift5_reflstr: 0x4c7d
-  __TEXT.__swift5_assocty: 0x10f8
-  __TEXT.__constg_swiftt: 0x54e0
-  __TEXT.__swift5_fieldmd: 0x5b30
+8.0.40.0.0
+  __TEXT.__text: 0x3abae0
+  __TEXT.__auth_stubs: 0x41b0
+  __TEXT.__objc_methlist: 0x17ffc
+  __TEXT.__cstring: 0x26682
+  __TEXT.__swift5_typeref: 0x638c
+  __TEXT.__const: 0x37180
+  __TEXT.__swift5_reflstr: 0x4d0d
+  __TEXT.__swift5_assocty: 0x1200
+  __TEXT.__constg_swiftt: 0x55d8
+  __TEXT.__swift5_fieldmd: 0x5b5c
   __TEXT.__swift5_builtin: 0x26c
-  __TEXT.__swift5_proto: 0x1f28
+  __TEXT.__swift5_proto: 0x1f34
   __TEXT.__swift5_types: 0xa0c
-  __TEXT.__swift5_protos: 0x80
+  __TEXT.__swift5_protos: 0x84
   __TEXT.__swift5_capture: 0x2f4
   __TEXT.__swift5_mpenum: 0x30
-  __TEXT.__gcc_except_tab: 0x36288
+  __TEXT.__gcc_except_tab: 0x36488
   __TEXT.__dlopen_cstrs: 0x51d
   __TEXT.__oslogstring: 0x6
-  __TEXT.__unwind_info: 0x156e0
-  __TEXT.__eh_frame: 0x71b0
+  __TEXT.__unwind_info: 0x15820
+  __TEXT.__eh_frame: 0x73e8
   __TEXT.__objc_classname: 0x5740
-  __TEXT.__objc_methname: 0x2edea
-  __TEXT.__objc_methtype: 0x110f0
-  __TEXT.__objc_stubs: 0x1a800
+  __TEXT.__objc_methname: 0x2f017
+  __TEXT.__objc_methtype: 0x11922
+  __TEXT.__objc_stubs: 0x1a920
   __DATA_CONST.__got: 0x1878
-  __DATA_CONST.__const: 0x5d40
+  __DATA_CONST.__const: 0x5d70
   __DATA_CONST.__objc_classlist: 0x1558
   __DATA_CONST.__objc_catlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x80d0
+  __DATA_CONST.__objc_selrefs: 0x8120
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x1178
   __DATA_CONST.__objc_arraydata: 0xbb0
-  __AUTH_CONST.__auth_got: 0x20d8
-  __AUTH_CONST.__auth_ptr: 0xd78
-  __AUTH_CONST.__const: 0x13638
-  __AUTH_CONST.__cfstring: 0x19340
-  __AUTH_CONST.__objc_const: 0x2f558
+  __AUTH_CONST.__auth_got: 0x20f0
+  __AUTH_CONST.__auth_ptr: 0xcb8
+  __AUTH_CONST.__const: 0x13588
+  __AUTH_CONST.__cfstring: 0x193e0
+  __AUTH_CONST.__objc_const: 0x2f690
   __AUTH_CONST.__objc_intobj: 0x1038
   __AUTH_CONST.__objc_arrayobj: 0x390
   __AUTH_CONST.__objc_floatobj: 0x2f0
   __AUTH_CONST.__objc_doubleobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x7e20
-  __AUTH.__data: 0x5840
-  __DATA.__objc_ivar: 0x173c
-  __DATA.__data: 0x68d8
-  __DATA.__bss: 0x40000
-  __DATA.__common: 0x2cd
+  __AUTH.__objc_data: 0x7d80
+  __AUTH.__data: 0x5af0
+  __DATA.__objc_ivar: 0x1748
+  __DATA.__data: 0x6988
+  __DATA.__bss: 0x40158
+  __DATA.__common: 0x2b5
   __DATA_DIRTY.__objc_data: 0x5320
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0x354

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 19455
-  Symbols:   12956
-  CStrings:  12875
+  Functions: 19532
+  Symbols:   12975
+  CStrings:  12901
 
Symbols:
+ _VNImageSegmentationCategoryStrand
+ _swift_initClassMetadata2
+ _swift_allocateGenericClassMetadata
+ _swift_willThrowTypedImpl
+ _VNImageSegmentationCategoryShadow
- _swift_dynamicCastClassUnconditional
CStrings:
+ " has no observations for "
+ "_TtCC6Vision18TrackObjectRequest5State"
+ "B80@0:8@16@24@32r^v40@48@56@64^@72"
+ "generateInstanceConnectedComponentsFromMask:fillGapsAreaRatio:"
+ "fillMaskGaps"
+ "setFillGapsAreaRatio:"
+ "_fillGapsInMask"
+ "fillGapsInMask"
+ "@96@0:8@16@24@32@40^{__CVBuffer=}48Q56{CGRect={CGPoint=dd}{CGSize=dd}}64"
+ "instancesForCategory:error:"
+ "TB,N,V_fillGapsInMask"
+ "VNImageSegmentationCategoryShadow"
+ "B80@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48"
+ "initWithOriginatingRequestSpecifier:instanceLowResMaskArray:instanceFeatureKeyIndexMap:instanceCategoryKeyIndexMap:instanceMask:numComponents:regionOfInterest:"
+ "createAllInstancesMaskFromForegroundCC:backgroundCC:options:error:"
+ "generateInstanceConnectedComponentsFromMask:inverseColor:"
+ "^{__CVBuffer=}48@0:8r^v16r^v24@32^@40"
+ "_addInstanceMaskBuffersForCategory:instanceFeatures:toInstanceMaskArray:connectedComponentResult:featureInstanceMaskMap:categoryInstanceMaskMap:options:error:"
+ "_instanceCategoriesMap"
+ "fillGapsAreaRatio"
+ "modifyMask:forLabel:fromConnectedComponents:error:"
+ "foregroundbackgroundsegmenter"
+ "_TtCC6Vision21TrackRectangleRequest5State"
+ "_fillGapsAreaRatio"
+ "Tf,V_fillGapsAreaRatio"
+ "generateInstanceConnectedComponentsFromMLMultiArray:maskThreshold:queryID:inverseColor:"
+ "\x01c"
+ "setFillGapsInMask:"
+ "isFullyIntersection:withRect2:"
+ "null mask image"
+ "v48@0:8^{vImage_Buffer=^vQQQ}16Q24r^v32^@40"
+ "VNImageSegmentationCategoryStrand"
+ "B24@?0@\"VNFgBgE5MLInstanceFeature\"8@\"NSDictionary\"16"
+ "{ConnectedComponentResult={unique_ptr<unsigned long[], std::default_delete<unsigned long[]>>={__compressed_pair<unsigned long *, std::default_delete<unsigned long[]>>=^Q}}{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q{__compressed_pair<unsigned long *, std::allocator<unsigned long>>=^Q}}{vector<apple::vision::fgbg::ConnectedComponentResult::CCBoundary, std::allocator<apple::vision::fgbg::ConnectedComponentResult::CCBoundary>>=^{CCBoundary}^{CCBoundary}{__compressed_pair<apple::vision::fgbg::ConnectedComponentResult::CCBoundary *, std::allocator<apple::vision::fgbg::ConnectedComponentResult::CCBoundary>>=^{CCBoundary}}}{vector<CGPoint, std::allocator<CGPoint>>=^{CGPoint}^{CGPoint}{__compressed_pair<CGPoint *, std::allocator<CGPoint>>=^{CGPoint}}}{vector<std::vector<CGPoint>, std::allocator<std::vector<CGPoint>>>=^v^v{__compressed_pair<std::vector<CGPoint> *, std::allocator<std::vector<CGPoint>>>=^v}}QQiQBB}52@0:8{vImage_Buffer=^vQQQ}16f48"
+ "{ConnectedComponentResult={unique_ptr<unsigned long[], std::default_delete<unsigned long[]>>={__compressed_pair<unsigned long *, std::default_delete<unsigned long[]>>=^Q}}{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q{__compressed_pair<unsigned long *, std::allocator<unsigned long>>=^Q}}{vector<apple::vision::fgbg::ConnectedComponentResult::CCBoundary, std::allocator<apple::vision::fgbg::ConnectedComponentResult::CCBoundary>>=^{CCBoundary}^{CCBoundary}{__compressed_pair<apple::vision::fgbg::ConnectedComponentResult::CCBoundary *, std::allocator<apple::vision::fgbg::ConnectedComponentResult::CCBoundary>>=^{CCBoundary}}}{vector<CGPoint, std::allocator<CGPoint>>=^{CGPoint}^{CGPoint}{__compressed_pair<CGPoint *, std::allocator<CGPoint>>=^{CGPoint}}}{vector<std::vector<CGPoint>, std::allocator<std::vector<CGPoint>>>=^v^v{__compressed_pair<std::vector<CGPoint> *, std::allocator<std::vector<CGPoint>>>=^v}}QQiQBB}36@0:8@16f24i28B32"
+ "{ConnectedComponentResult={unique_ptr<unsigned long[], std::default_delete<unsigned long[]>>={__compressed_pair<unsigned long *, std::default_delete<unsigned long[]>>=^Q}}{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q{__compressed_pair<unsigned long *, std::allocator<unsigned long>>=^Q}}{vector<apple::vision::fgbg::ConnectedComponentResult::CCBoundary, std::allocator<apple::vision::fgbg::ConnectedComponentResult::CCBoundary>>=^{CCBoundary}^{CCBoundary}{__compressed_pair<apple::vision::fgbg::ConnectedComponentResult::CCBoundary *, std::allocator<apple::vision::fgbg::ConnectedComponentResult::CCBoundary>>=^{CCBoundary}}}{vector<CGPoint, std::allocator<CGPoint>>=^{CGPoint}^{CGPoint}{__compressed_pair<CGPoint *, std::allocator<CGPoint>>=^{CGPoint}}}{vector<std::vector<CGPoint>, std::allocator<std::vector<CGPoint>>>=^v^v{__compressed_pair<std::vector<CGPoint> *, std::allocator<std::vector<CGPoint>>>=^v}}QQiQBB}52@0:8{vImage_Buffer=^vQQQ}16B48"
- "_TtC6Vision22ImageRegistrationState"
- "generateInstanceConnectedComponentsFromMLMultiArray:maskThreshold:queryID:"
- "{ConnectedComponentResult={unique_ptr<unsigned long[], std::default_delete<unsigned long[]>>={__compressed_pair<unsigned long *, std::default_delete<unsigned long[]>>=^Q}}{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q{__compressed_pair<unsigned long *, std::allocator<unsigned long>>=^Q}}{vector<apple::vision::fgbg::ConnectedComponentResult::CCBoundary, std::allocator<apple::vision::fgbg::ConnectedComponentResult::CCBoundary>>=^{CCBoundary}^{CCBoundary}{__compressed_pair<apple::vision::fgbg::ConnectedComponentResult::CCBoundary *, std::allocator<apple::vision::fgbg::ConnectedComponentResult::CCBoundary>>=^{CCBoundary}}}{vector<CGPoint, std::allocator<CGPoint>>=^{CGPoint}^{CGPoint}{__compressed_pair<CGPoint *, std::allocator<CGPoint>>=^{CGPoint}}}{vector<std::vector<CGPoint>, std::allocator<std::vector<CGPoint>>>=^v^v{__compressed_pair<std::vector<CGPoint> *, std::allocator<std::vector<CGPoint>>>=^v}}QQiQBB}32@0:8@16f24i28"
- "\x01b"
- "_addInstanceMaskBuffersForCategory:toInstanceMaskArray:connectedComponentResult:featureInstanceMaskMap:options:error:"
- "@88@0:8@16@24@32^{__CVBuffer=}40Q48{CGRect={CGPoint=dd}{CGSize=dd}}56"
- "_TtC6Vision13TrackingState"
- "B64@0:8@16@24r^v32@40@48^@56"
- "initWithOriginatingRequestSpecifier:instanceLowResMaskArray:instanceFeatureKeyIndexMap:instanceMask:numComponents:regionOfInterest:"

```
