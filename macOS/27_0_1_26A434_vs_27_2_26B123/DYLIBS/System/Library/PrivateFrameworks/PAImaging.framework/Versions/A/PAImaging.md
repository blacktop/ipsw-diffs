## PAImaging

> `/System/Library/PrivateFrameworks/PAImaging.framework/Versions/A/PAImaging`

```diff

-911.0.134.0.0
-  __TEXT.__text: 0x79828
-  __TEXT.__objc_methlist: 0x7dbc
+916.58.114.0.0
+  __TEXT.__text: 0x79c4c
+  __TEXT.__objc_methlist: 0x7dd4
   __TEXT.__const: 0x320
   __TEXT.__gcc_except_tab: 0xb6c
-  __TEXT.__cstring: 0xfae4
+  __TEXT.__cstring: 0xfb08
   __TEXT.__oslogstring: 0x1eed
   __TEXT.__ustring: 0xae
-  __TEXT.__unwind_info: 0x2310
+  __TEXT.__unwind_info: 0x2318
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x400
+  __DATA_CONST.__const: 0x408
   __DATA_CONST.__objc_classlist: 0x3b8
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5280
+  __DATA_CONST.__objc_selrefs: 0x5278
   __DATA_CONST.__objc_superrefs: 0x2f0
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__got: 0xd70
   __AUTH_CONST.__const: 0x2e08
-  __AUTH_CONST.__cfstring: 0x6d40
-  __AUTH_CONST.__objc_const: 0xc110
+  __AUTH_CONST.__cfstring: 0x6d60
+  __AUTH_CONST.__objc_const: 0xc0d0
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_intobj: 0x228
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__auth_got: 0xb90
+  __AUTH_CONST.__auth_got: 0xba8
   __AUTH_CONST.__auth_ptr: 0x0
   __AUTH.__objc_data: 0x1360
-  __DATA.__objc_ivar: 0x914
+  __DATA.__objc_ivar: 0x910
   __DATA.__data: 0x940
   __DATA.__bss: 0x150
   __DATA.__common: 0x20

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3093
-  Symbols:   7921
+  Functions: 3095
+  Symbols:   7920
   CStrings:  1755
 
Symbols:
+ +[PAContentTransform _transformCoveringViewBounds:transform:contentBounds:]
+ +[PAContentTransform contentTransformWithBounds:scale:origin:anchor:contentBounds:contentPointToAlign:coveringViewBounds:]
+ +[PAContentTransform contentTransformWithBounds:scale:originPoint:anchorPoint:contentBounds:contentPointToAlign:coveringViewBounds:]
+ -[PACanvasItemView convertRect:toContentViewFromView:]
+ -[PACropController _cropRectFittingSize:nearCenter:]
+ -[PAItemView _notifyGeometryDidChange]
+ GCC_except_table1008
+ GCC_except_table1018
+ GCC_except_table1020
+ GCC_except_table1023
+ GCC_except_table1053
+ GCC_except_table1115
+ GCC_except_table1221
+ GCC_except_table1351
+ GCC_except_table1368
+ GCC_except_table1481
+ GCC_except_table1501
+ GCC_except_table1532
+ GCC_except_table1768
+ GCC_except_table1831
+ GCC_except_table1855
+ GCC_except_table1898
+ GCC_except_table198
+ GCC_except_table2093
+ GCC_except_table2095
+ GCC_except_table2098
+ GCC_except_table2106
+ GCC_except_table2108
+ GCC_except_table2116
+ GCC_except_table2118
+ GCC_except_table2147
+ GCC_except_table2157
+ GCC_except_table2170
+ GCC_except_table2177
+ GCC_except_table2205
+ GCC_except_table2206
+ GCC_except_table2246
+ GCC_except_table2261
+ GCC_except_table2267
+ GCC_except_table2287
+ GCC_except_table2290
+ GCC_except_table2502
+ GCC_except_table2513
+ GCC_except_table2516
+ GCC_except_table2526
+ GCC_except_table2556
+ GCC_except_table2567
+ GCC_except_table2945
+ GCC_except_table2984
+ GCC_except_table3000
+ GCC_except_table3032
+ GCC_except_table315
+ GCC_except_table320
+ GCC_except_table327
+ GCC_except_table351
+ GCC_except_table363
+ GCC_except_table433
+ GCC_except_table470
+ GCC_except_table473
+ GCC_except_table489
+ GCC_except_table502
+ GCC_except_table552
+ GCC_except_table652
+ GCC_except_table681
+ GCC_except_table771
+ GCC_except_table773
+ GCC_except_table788
+ GCC_except_table791
+ GCC_except_table796
+ GCC_except_table806
+ GCC_except_table862
+ GCC_except_table886
+ GCC_except_table946
+ GCC_except_table948
+ GCC_except_table950
+ _CGRectApplyAffineTransform
+ _CGRectContainsRect
+ _PAItemViewGeometryDidChangeNotification
+ _PFDeviceIsVirtualMachine
+ _objc_msgSend$_notifyGeometryDidChange
+ _objc_msgSend$_transformCoveringViewBounds:transform:contentBounds:
+ _objc_msgSend$contentTransformWithBounds:scale:origin:anchor:contentBounds:contentPointToAlign:coveringViewBounds:
+ _objc_msgSend$contentTransformWithBounds:scale:originPoint:anchorPoint:contentBounds:contentPointToAlign:coveringViewBounds:
+ _objc_msgSend$cropRectFittingSize:nearCenter:
- -[PACanvasOverlayView .cxx_destruct]
- -[PACanvasOverlayView magnifyWithEvent:]
- -[PACanvasOverlayView setViewForMagnificationEvents:]
- -[PACanvasOverlayView viewForMagnificationEvents]
- GCC_except_table1007
- GCC_except_table1015
- GCC_except_table1019
- GCC_except_table1022
- GCC_except_table1052
- GCC_except_table1114
- GCC_except_table1217
- GCC_except_table1347
- GCC_except_table1364
- GCC_except_table1477
- GCC_except_table1497
- GCC_except_table1528
- GCC_except_table1764
- GCC_except_table1827
- GCC_except_table1851
- GCC_except_table1894
- GCC_except_table197
- GCC_except_table2089
- GCC_except_table2091
- GCC_except_table2094
- GCC_except_table2096
- GCC_except_table2102
- GCC_except_table2110
- GCC_except_table2112
- GCC_except_table2143
- GCC_except_table2153
- GCC_except_table2166
- GCC_except_table2173
- GCC_except_table2201
- GCC_except_table2202
- GCC_except_table2238
- GCC_except_table2257
- GCC_except_table2263
- GCC_except_table2283
- GCC_except_table2286
- GCC_except_table2497
- GCC_except_table2508
- GCC_except_table2511
- GCC_except_table2521
- GCC_except_table2551
- GCC_except_table2562
- GCC_except_table2943
- GCC_except_table2982
- GCC_except_table2998
- GCC_except_table3030
- GCC_except_table314
- GCC_except_table319
- GCC_except_table326
- GCC_except_table350
- GCC_except_table362
- GCC_except_table432
- GCC_except_table469
- GCC_except_table472
- GCC_except_table488
- GCC_except_table501
- GCC_except_table551
- GCC_except_table651
- GCC_except_table680
- GCC_except_table770
- GCC_except_table772
- GCC_except_table787
- GCC_except_table790
- GCC_except_table795
- GCC_except_table805
- GCC_except_table861
- GCC_except_table885
- GCC_except_table945
- GCC_except_table947
- GCC_except_table949
- OBJC_IVAR_$_PACanvasOverlayView._viewForMagnificationEvents
- __OBJC_$_INSTANCE_VARIABLES_PACanvasOverlayView
- __OBJC_$_PROP_LIST_PACanvasOverlayView
- _objc_msgSend$contentTransformWithBounds:scale:originPoint:anchorPoint:contentBounds:contentPointToAlign:
- _objc_msgSend$hitTest:
- _objc_msgSend$indexOfObjectIdenticalTo:
- _objc_msgSend$locationInWindow
- _objc_msgSend$magnifyWithEvent:
- _objc_msgSend$phase
- _objc_msgSend$setViewForMagnificationEvents:
- _objc_msgSend$superview
- _objc_msgSend$viewForMagnificationEvents
CStrings:
+ "1048"
+ "1050"
+ "1085"
+ "1087"
+ "1134"
+ "1138"
+ "1144"
+ "1204"
+ "252"
+ "273"
+ "277"
+ "37"
+ "382"
+ "517"
+ "582"
+ "62"
+ "684"
+ "693"
+ "737"
+ "772"
+ "780"
+ "840"
+ "PAItemViewGeometryDidChangeNotification"
- "1049"
- "1051"
- "1086"
- "1088"
- "1115"
- "1139"
- "1145"
- "1205"
- "229"
- "247"
- "268"
- "36"
- "383"
- "518"
- "583"
- "61"
- "685"
- "694"
- "738"
- "773"
- "781"
- "788"
- "841"
```
