## PhotosUIFoundation

> `/System/Library/PrivateFrameworks/PhotosUIFoundation.framework/PhotosUIFoundation`

```diff

-910.33.102.0.0
-  __TEXT.__text: 0xf5a30
-  __TEXT.__objc_methlist: 0xfbe4
+912.0.111.0.0
+  __TEXT.__text: 0xf6238
+  __TEXT.__objc_methlist: 0xfc64
   __TEXT.__const: 0x7160
   __TEXT.__swift5_typeref: 0x2df4
   __TEXT.__constg_swiftt: 0x3a64

   __TEXT.__swift5_assocty: 0x9d0
   __TEXT.__swift5_proto: 0x3b0
   __TEXT.__swift5_types: 0x264
-  __TEXT.__cstring: 0xba44
+  __TEXT.__cstring: 0xba5d
   __TEXT.__swift5_capture: 0xe08
   __TEXT.__swift5_protos: 0x98
   __TEXT.__oslogstring: 0x1a3a

   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__gcc_except_tab: 0xce4
   __TEXT.__ustring: 0x124
-  __TEXT.__unwind_info: 0x5718
+  __TEXT.__unwind_info: 0x5730
   __TEXT.__eh_frame: 0x1ce8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3f40
+  __DATA_CONST.__const: 0x3f68
   __DATA_CONST.__objc_classlist: 0x788
   __DATA_CONST.__objc_catlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x348
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x77d0
+  __DATA_CONST.__objc_selrefs: 0x7850
   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0x518
   __DATA_CONST.__objc_arraydata: 0x300
   __DATA_CONST.__got: 0xe98
   __AUTH_CONST.__const: 0x6060
-  __AUTH_CONST.__cfstring: 0x7dc0
-  __AUTH_CONST.__objc_const: 0x1f0c8
+  __AUTH_CONST.__cfstring: 0x7de0
+  __AUTH_CONST.__objc_const: 0x1f108
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_doubleobj: 0x1e0
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x168
-  __AUTH_CONST.__auth_got: 0x1940
+  __AUTH_CONST.__auth_got: 0x1958
   __AUTH.__objc_data: 0x49e0
   __AUTH.__data: 0x1b70
-  __DATA.__objc_ivar: 0x10e0
+  __DATA.__objc_ivar: 0x10e4
   __DATA.__data: 0x4880
   __DATA.__bss: 0x6ad0
   __DATA.__common: 0x10

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 9550
-  Symbols:   13717
-  CStrings:  1581
+  Functions: 9564
+  Symbols:   13742
+  CStrings:  1583
 
Symbols:
+ +[PXUserTransformView doubleTapZoomScaleForContentSize:inBoundsSize:defaultScale:preferToFillOnDoubleTap:floorZoomScale:]
+ +[UIImage(PhotosUIFoundation) px_symbolImageNamed:withConfiguration:]
+ -[PXUserTransformView _clampedContentOffset:toContentSize:boundsSize:contentInsets:centeringSmallContent:]
+ -[PXUserTransformView _resolvedContentSize]
+ -[PXUserTransformView _updateScrollViewScrollEnabled]
+ -[PXUserTransformView _zoomOutToScale:animated:]
+ -[PXUserTransformView contentRegionSize]
+ -[PXUserTransformView doubleTapFloorZoomScale]
+ -[PXUserTransformView isFullyZoomedOut]
+ -[PXUserTransformView preferredMinimumZoomScale]
+ -[PXUserTransformView setContentRegionSize:]
+ -[PXUserTransformView setDoubleTapFloorZoomScale:]
+ -[PXUserTransformView setPreferredMinimumZoomScale:]
+ -[PXUserTransformView setPreferredMinimumZoomScale:animated:]
+ -[PXUserTransformView zoomOutToPreferredMinimumScale:]
+ -[UIScrollView(PhotosUICore) px_setBottomEdgePocketHidden:]
+ -[UIScrollView(PhotosUICore) px_setPocketPreferredUserInterfaceStyleForTopEdge:]
+ GCC_except_table1131
+ GCC_except_table1135
+ GCC_except_table1138
+ GCC_except_table1141
+ GCC_except_table1149
+ GCC_except_table1153
+ GCC_except_table1160
+ GCC_except_table1162
+ GCC_except_table1164
+ GCC_except_table1166
+ GCC_except_table1168
+ GCC_except_table1170
+ GCC_except_table1172
+ GCC_except_table1178
+ GCC_except_table1240
+ GCC_except_table1305
+ GCC_except_table1567
+ GCC_except_table1577
+ GCC_except_table1602
+ GCC_except_table1628
+ GCC_except_table1848
+ GCC_except_table1869
+ GCC_except_table1878
+ GCC_except_table1880
+ GCC_except_table1897
+ GCC_except_table1936
+ GCC_except_table1939
+ GCC_except_table2076
+ GCC_except_table2091
+ GCC_except_table2109
+ GCC_except_table2149
+ GCC_except_table2237
+ GCC_except_table2401
+ GCC_except_table2619
+ GCC_except_table2654
+ GCC_except_table2681
+ GCC_except_table2950
+ GCC_except_table3049
+ GCC_except_table3051
+ GCC_except_table3104
+ GCC_except_table3118
+ GCC_except_table3122
+ GCC_except_table3129
+ GCC_except_table3136
+ GCC_except_table3151
+ GCC_except_table3158
+ GCC_except_table3172
+ GCC_except_table3441
+ GCC_except_table3476
+ GCC_except_table3497
+ GCC_except_table3577
+ GCC_except_table3579
+ GCC_except_table3614
+ GCC_except_table3645
+ GCC_except_table3649
+ GCC_except_table3665
+ GCC_except_table3712
+ GCC_except_table3728
+ GCC_except_table4028
+ GCC_except_table4038
+ GCC_except_table4101
+ GCC_except_table4255
+ GCC_except_table4366
+ GCC_except_table4387
+ GCC_except_table4392
+ GCC_except_table4543
+ GCC_except_table4662
+ GCC_except_table4952
+ GCC_except_table4963
+ GCC_except_table4966
+ GCC_except_table4990
+ GCC_except_table4998
+ GCC_except_table5002
+ GCC_except_table5006
+ GCC_except_table5039
+ GCC_except_table5098
+ GCC_except_table5124
+ GCC_except_table5165
+ _OBJC_IVAR_$_PXUserTransformView._contentRegionSize
+ _OBJC_IVAR_$_PXUserTransformView._doubleTapFloorZoomScale
+ _OBJC_IVAR_$_PXUserTransformView._preferredMinimumZoomScale
+ _PXResolvedPocketUserInterfaceStyle
+ ___48-[PXUserTransformView _zoomOutToScale:animated:]_block_invoke
+ ___61-[PXUserTransformView zoomInOnLocationFromProvider:animated:]_block_invoke_2
+ ___block_descriptor_42_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_64_e8_32s_e5_v8?0ls32l8
+ _objc_msgSend$_clampedContentOffset:toContentSize:boundsSize:contentInsets:centeringSmallContent:
+ _objc_msgSend$_hiddenPocketEdges
+ _objc_msgSend$_resolvedContentSize
+ _objc_msgSend$_setHiddenPocketEdges:
+ _objc_msgSend$_updateScrollViewScrollEnabled
+ _objc_msgSend$_zoomOutToScale:animated:
+ _objc_msgSend$contentRegionSize
+ _objc_msgSend$convertPoint:toView:
+ _objc_msgSend$doubleTapFloorZoomScale
+ _objc_msgSend$doubleTapZoomScaleForContentSize:inBoundsSize:defaultScale:preferToFillOnDoubleTap:floorZoomScale:
+ _objc_msgSend$preferredMinimumZoomScale
+ _objc_msgSend$setPreferredMinimumZoomScale:
+ _objc_msgSend$setPreferredMinimumZoomScale:animated:
- +[PXUserTransformView doubleTapZoomScaleForContentSize:inBoundsSize:defaultScale:preferToFillOnDoubleTap:]
- -[PXUserTransformView _preferredMinimumZoomScale]
- -[PXUserTransformView _setPreferredMinimumZoomScale:]
- -[PXUserTransformView minimumZoomScale]
- -[PXUserTransformView setMinimumZoomScale:]
- -[PXUserTransformView setMinimumZoomScale:animated:]
- GCC_except_table1130
- GCC_except_table1134
- GCC_except_table1137
- GCC_except_table1140
- GCC_except_table1148
- GCC_except_table1152
- GCC_except_table1159
- GCC_except_table1161
- GCC_except_table1163
- GCC_except_table1165
- GCC_except_table1167
- GCC_except_table1169
- GCC_except_table1171
- GCC_except_table1177
- GCC_except_table1239
- GCC_except_table1304
- GCC_except_table1566
- GCC_except_table1576
- GCC_except_table1601
- GCC_except_table1627
- GCC_except_table1847
- GCC_except_table1868
- GCC_except_table1877
- GCC_except_table1879
- GCC_except_table1896
- GCC_except_table1934
- GCC_except_table1938
- GCC_except_table2075
- GCC_except_table2090
- GCC_except_table2108
- GCC_except_table2148
- GCC_except_table2236
- GCC_except_table2400
- GCC_except_table2618
- GCC_except_table2652
- GCC_except_table2680
- GCC_except_table2949
- GCC_except_table3048
- GCC_except_table3050
- GCC_except_table3103
- GCC_except_table3117
- GCC_except_table3121
- GCC_except_table3128
- GCC_except_table3135
- GCC_except_table3150
- GCC_except_table3157
- GCC_except_table3171
- GCC_except_table3440
- GCC_except_table3475
- GCC_except_table3496
- GCC_except_table3576
- GCC_except_table3578
- GCC_except_table3613
- GCC_except_table3644
- GCC_except_table3648
- GCC_except_table3664
- GCC_except_table3711
- GCC_except_table3727
- GCC_except_table4024
- GCC_except_table4034
- GCC_except_table4097
- GCC_except_table4251
- GCC_except_table4362
- GCC_except_table4383
- GCC_except_table4388
- GCC_except_table4539
- GCC_except_table4658
- GCC_except_table4937
- GCC_except_table4939
- GCC_except_table4953
- GCC_except_table4972
- GCC_except_table4977
- GCC_except_table4989
- GCC_except_table4993
- GCC_except_table5026
- GCC_except_table5085
- GCC_except_table5111
- GCC_except_table5152
- _OBJC_IVAR_$_PXUserTransformView.__preferredMinimumZoomScale
- _OBJC_IVAR_$_PXUserTransformView._minimumZoomScale
- ___31-[PXUserTransformView zoomOut:]_block_invoke
- ___block_descriptor_43_e8_32s_e5_v8?0ls32l8
- _objc_msgSend$_setPreferredMinimumZoomScale:
- _objc_msgSend$doubleTapZoomScaleForContentSize:inBoundsSize:defaultScale:preferToFillOnDoubleTap:
- _objc_msgSend$setMinimumZoomScale:animated:
CStrings:
+ "a\"!2"
+ "custom.photos"
+ "preferredMinimumZoomScale >= 0"
+ "\x81"
- "Q\"!B"
- "minimumZoomScale >= 0"
```
