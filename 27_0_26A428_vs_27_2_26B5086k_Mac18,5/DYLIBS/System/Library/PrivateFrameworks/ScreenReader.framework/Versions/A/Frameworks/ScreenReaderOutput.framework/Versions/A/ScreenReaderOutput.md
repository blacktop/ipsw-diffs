## ScreenReaderOutput

> `/System/Library/PrivateFrameworks/ScreenReader.framework/Versions/A/Frameworks/ScreenReaderOutput.framework/Versions/A/ScreenReaderOutput`

```diff

-1048.3.0.0.0
-  __TEXT.__text: 0xa34d0
-  __TEXT.__objc_methlist: 0x93d0
+1050.3.0.0.0
+  __TEXT.__text: 0xa4518
+  __TEXT.__objc_methlist: 0x95c0
   __TEXT.__const: 0x1938
-  __TEXT.__cstring: 0x6581
+  __TEXT.__cstring: 0x65ee
   __TEXT.__swift5_typeref: 0xeec
   __TEXT.__constg_swiftt: 0x960
   __TEXT.__swift5_builtin: 0xb4
   __TEXT.__swift5_types: 0xa4
-  __TEXT.__oslogstring: 0x285d
+  __TEXT.__oslogstring: 0x285a
   __TEXT.__swift5_reflstr: 0x605
   __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_fieldmd: 0x7f8

   __TEXT.__swift_as_ret: 0x5c
   __TEXT.__swift_as_cont: 0x9c
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__gcc_except_tab: 0x1940
+  __TEXT.__gcc_except_tab: 0x1954
   __TEXT.__ustring: 0x9e
-  __TEXT.__unwind_info: 0x3510
+  __TEXT.__unwind_info: 0x3578
   __TEXT.__eh_frame: 0xa28
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4948
+  __DATA_CONST.__objc_selrefs: 0x4a18
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x218
   __DATA_CONST.__objc_arraydata: 0x3f8
   __DATA_CONST.__got: 0x808
-  __AUTH_CONST.__const: 0x44e8
-  __AUTH_CONST.__cfstring: 0x64e0
-  __AUTH_CONST.__objc_const: 0xc148
+  __AUTH_CONST.__const: 0x44f8
+  __AUTH_CONST.__cfstring: 0x6580
+  __AUTH_CONST.__objc_const: 0xc238
   __AUTH_CONST.__objc_intobj: 0x1218
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_doubleobj: 0x10

   __AUTH_CONST.__auth_got: 0xef0
   __AUTH.__objc_data: 0x400
   __AUTH.__data: 0x70
-  __DATA.__objc_ivar: 0x90c
-  __DATA.__data: 0x1680
+  __DATA.__objc_ivar: 0x918
+  __DATA.__data: 0x1690
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x1d10
   __DATA_DIRTY.__data: 0xc20

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4083
-  Symbols:   7922
-  CStrings:  1182
+  Functions: 4119
+  Symbols:   7983
+  CStrings:  1185
 
Symbols:
+ -[SCROBrailleClient setTabularFocusRow:col:]
+ -[SCROBrailleClient setTabularZoomLevel:]
+ -[SCROBrailleClientXPC setTabularFocusRow:col:]
+ -[SCROBrailleClientXPC setTabularZoomLevel:]
+ -[SCROBrailleDisplay handleCommandTabularZoomInEvent:forDispatcher:]
+ -[SCROBrailleDisplay handleCommandTabularZoomOutEvent:forDispatcher:]
+ -[SCROBrailleDisplayCommandDispatcher _handleTabularZoomInEvent:]
+ -[SCROBrailleDisplayCommandDispatcher _handleTabularZoomOutEvent:]
+ -[SCROBrailleDisplayManager _eventQueue_stepTabularZoomIn:]
+ -[SCROBrailleDisplayManager brailleDisplay:structuredBrailleRouterHitTabularCellWithKey:tableRow:tableCol:appToken:]
+ -[SCROBrailleDisplayManager brailleDisplay:structuredBrailleRouterHitTabularFocusedCellWithKey:appToken:]
+ -[SCROBrailleDisplayManager brailleDisplay:structuredBrailleRouterHitTabularStatusLineWithKey:appToken:]
+ -[SCROBrailleDisplayManager brailleDisplay:tabularZoomInWithKey:]
+ -[SCROBrailleDisplayManager brailleDisplay:tabularZoomOutWithKey:]
+ -[SCROBrailleDisplayManager setTabularFocusRow:col:]
+ -[SCROBrailleDisplayManager setTabularZoomLevel:]
+ -[SCROBrailleDisplayManager tabularZoomDidChange:]
+ -[SCROBrailleHandler handleTabularZoomDidChange:]
+ -[SCROBrailleHandlerXPC handleTabularZoomDidChange:]
+ -[SCROBrailleHandlerXPC setTabularFocusRow:col:]
+ -[SCROBrailleHandlerXPC setTabularZoomLevel:]
+ -[SCROBrailleKey _resetTabularCellRoute]
+ -[SCROBrailleKey isTabularCellRoute]
+ -[SCROBrailleKey setIsTabularCellRoute:]
+ -[SCROBrailleKey setTabularCellCol:]
+ -[SCROBrailleKey setTabularCellRow:]
+ -[SCROBrailleKey tabularCellCol]
+ -[SCROBrailleKey tabularCellRow]
+ GCC_except_table1108
+ GCC_except_table1172
+ GCC_except_table1174
+ GCC_except_table1176
+ GCC_except_table1178
+ GCC_except_table1242
+ GCC_except_table1272
+ GCC_except_table1279
+ GCC_except_table128
+ GCC_except_table1283
+ GCC_except_table1286
+ GCC_except_table1288
+ GCC_except_table129
+ GCC_except_table1318
+ GCC_except_table132
+ GCC_except_table1325
+ GCC_except_table1455
+ GCC_except_table1664
+ GCC_except_table1788
+ GCC_except_table1929
+ GCC_except_table1931
+ GCC_except_table1940
+ GCC_except_table1952
+ GCC_except_table2036
+ GCC_except_table2081
+ GCC_except_table2087
+ GCC_except_table2201
+ GCC_except_table2222
+ GCC_except_table2231
+ GCC_except_table2239
+ GCC_except_table2342
+ GCC_except_table2526
+ GCC_except_table2547
+ GCC_except_table2657
+ GCC_except_table2658
+ GCC_except_table2659
+ GCC_except_table2663
+ GCC_except_table2668
+ GCC_except_table2669
+ GCC_except_table2670
+ GCC_except_table2671
+ GCC_except_table2672
+ GCC_except_table2674
+ GCC_except_table2675
+ GCC_except_table2676
+ GCC_except_table2680
+ GCC_except_table2685
+ GCC_except_table2687
+ GCC_except_table2690
+ GCC_except_table3034
+ GCC_except_table3052
+ GCC_except_table3071
+ GCC_except_table3072
+ GCC_except_table3073
+ GCC_except_table3136
+ GCC_except_table3138
+ GCC_except_table3140
+ GCC_except_table3141
+ GCC_except_table3143
+ GCC_except_table3145
+ GCC_except_table444
+ GCC_except_table457
+ GCC_except_table489
+ GCC_except_table490
+ GCC_except_table513
+ GCC_except_table514
+ GCC_except_table524
+ GCC_except_table526
+ GCC_except_table548
+ GCC_except_table549
+ GCC_except_table555
+ GCC_except_table558
+ GCC_except_table568
+ GCC_except_table588
+ GCC_except_table590
+ GCC_except_table591
+ GCC_except_table599
+ GCC_except_table601
+ GCC_except_table609
+ GCC_except_table623
+ GCC_except_table625
+ GCC_except_table626
+ GCC_except_table632
+ GCC_except_table64
+ GCC_except_table641
+ GCC_except_table660
+ GCC_except_table663
+ GCC_except_table927
+ GCC_except_table968
+ GCC_except_table970
+ OBJC_IVAR_$_SCROBrailleKey._isTabularCellRoute
+ OBJC_IVAR_$_SCROBrailleKey._tabularCellCol
+ OBJC_IVAR_$_SCROBrailleKey._tabularCellRow
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BRLLayoutManagerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SCROBrailleDisplayDelegate
+ ___104-[SCROBrailleDisplayManager brailleDisplay:structuredBrailleRouterHitTabularStatusLineWithKey:appToken:]_block_invoke
+ ___104-[SCROBrailleDisplayManager brailleDisplay:structuredBrailleRouterHitTabularStatusLineWithKey:appToken:]_block_invoke_2
+ ___105-[SCROBrailleDisplayManager brailleDisplay:structuredBrailleRouterHitTabularFocusedCellWithKey:appToken:]_block_invoke
+ ___105-[SCROBrailleDisplayManager brailleDisplay:structuredBrailleRouterHitTabularFocusedCellWithKey:appToken:]_block_invoke_2
+ ___116-[SCROBrailleDisplayManager brailleDisplay:structuredBrailleRouterHitTabularCellWithKey:tableRow:tableCol:appToken:]_block_invoke
+ ___116-[SCROBrailleDisplayManager brailleDisplay:structuredBrailleRouterHitTabularCellWithKey:tableRow:tableCol:appToken:]_block_invoke_2
+ ___49-[SCROBrailleDisplayManager setTabularZoomLevel:]_block_invoke
+ ___52-[SCROBrailleDisplayManager setTabularFocusRow:col:]_block_invoke
+ ___52-[SCROBrailleHandlerXPC handleTabularZoomDidChange:]_block_invoke
+ ___59-[SCROBrailleDisplayManager _eventQueue_stepTabularZoomIn:]_block_invoke
+ ___block_descriptor_80_e8_32s40s48s56s_e5_v8?0l
+ _kSCROBraillePrintTextRowsAttribute
+ _objc_msgSend$_eventQueue_stepTabularZoomIn:
+ _objc_msgSend$_resetTabularCellRoute
+ _objc_msgSend$brailleDisplay:structuredBrailleRouterHitTabularCellWithKey:tableRow:tableCol:appToken:
+ _objc_msgSend$brailleDisplay:structuredBrailleRouterHitTabularFocusedCellWithKey:appToken:
+ _objc_msgSend$brailleDisplay:structuredBrailleRouterHitTabularStatusLineWithKey:appToken:
+ _objc_msgSend$brailleDisplay:tabularZoomInWithKey:
+ _objc_msgSend$brailleDisplay:tabularZoomOutWithKey:
+ _objc_msgSend$currentPrintTextRows
+ _objc_msgSend$cycleTabularZoom
+ _objc_msgSend$decreaseTabularZoom
+ _objc_msgSend$handleCommandTabularZoomInEvent:forDispatcher:
+ _objc_msgSend$handleCommandTabularZoomOutEvent:forDispatcher:
+ _objc_msgSend$handleTabularZoomDidChange:
+ _objc_msgSend$increaseTabularZoom
+ _objc_msgSend$routingKeyHitTestAtCellIndex:elementToken:isTextLine:brailleOffset:printTextOffset:statusCellIndex:shouldPerformActions:routerClickCount:tableRow:tableCol:
+ _objc_msgSend$setIsTabularCellRoute:
+ _objc_msgSend$setTabularCellCol:
+ _objc_msgSend$setTabularCellRow:
+ _objc_msgSend$setTabularFocusRow:col:
+ _objc_msgSend$setTabularZoomLevel:
+ _objc_msgSend$updateTabularFocusToRow:col:
- GCC_except_table1084
- GCC_except_table1148
- GCC_except_table1150
- GCC_except_table1152
- GCC_except_table1154
- GCC_except_table1220
- GCC_except_table1250
- GCC_except_table1257
- GCC_except_table126
- GCC_except_table1261
- GCC_except_table1264
- GCC_except_table1266
- GCC_except_table127
- GCC_except_table1296
- GCC_except_table130
- GCC_except_table1303
- GCC_except_table1425
- GCC_except_table1630
- GCC_except_table1752
- GCC_except_table1893
- GCC_except_table1895
- GCC_except_table1904
- GCC_except_table1916
- GCC_except_table2000
- GCC_except_table2045
- GCC_except_table2051
- GCC_except_table2165
- GCC_except_table2186
- GCC_except_table2195
- GCC_except_table2203
- GCC_except_table2306
- GCC_except_table2490
- GCC_except_table2511
- GCC_except_table2621
- GCC_except_table2622
- GCC_except_table2623
- GCC_except_table2627
- GCC_except_table2632
- GCC_except_table2633
- GCC_except_table2634
- GCC_except_table2635
- GCC_except_table2636
- GCC_except_table2638
- GCC_except_table2639
- GCC_except_table2640
- GCC_except_table2644
- GCC_except_table2649
- GCC_except_table2651
- GCC_except_table2654
- GCC_except_table2998
- GCC_except_table3016
- GCC_except_table3035
- GCC_except_table3036
- GCC_except_table3037
- GCC_except_table3100
- GCC_except_table3102
- GCC_except_table3104
- GCC_except_table3105
- GCC_except_table3107
- GCC_except_table3109
- GCC_except_table442
- GCC_except_table455
- GCC_except_table487
- GCC_except_table488
- GCC_except_table509
- GCC_except_table510
- GCC_except_table520
- GCC_except_table522
- GCC_except_table544
- GCC_except_table545
- GCC_except_table547
- GCC_except_table550
- GCC_except_table564
- GCC_except_table584
- GCC_except_table586
- GCC_except_table587
- GCC_except_table595
- GCC_except_table597
- GCC_except_table605
- GCC_except_table619
- GCC_except_table62
- GCC_except_table620
- GCC_except_table621
- GCC_except_table622
- GCC_except_table629
- GCC_except_table655
- GCC_except_table656
- GCC_except_table903
- GCC_except_table944
- GCC_except_table946
- ___isBrailleXPCOn_block_invoke
- _isBrailleXPCOn
- _objc_msgSend$routingKeyHitTestAtCellIndex:elementToken:isTextLine:brailleOffset:printTextOffset:statusCellIndex:shouldPerformActions:routerClickCount:
- isBrailleXPCOn.brailleXPCOn
- isBrailleXPCOn.onceToken
CStrings:
+ "SCRBraille.tabularZoomIn"
+ "SCRBraille.tabularZoomOut"
+ "SCROBraillePrintTextRowsAttribute"
+ "_isTabularCellRoute"
+ "_tabularCellCol"
+ "_tabularCellRow"
+ "setTabularFocusRow requires XPC"
+ "setTabularZoomLevel ignoring out-of-range level"
+ "setTabularZoomLevel requires XPC"
- "Braille_XPC"
- "Braille_XPC_Off"
- "SCROBrailleClient using Mach"
- "SCROBrailleClient using XPC"
- "SCROBrailleHandler using Mach"
- "SCROBrailleHandler using XPC"
```
