## ScreenReaderOutput

> `/System/Library/PrivateFrameworks/ScreenReader.framework/Versions/A/Frameworks/ScreenReaderOutput.framework/Versions/A/ScreenReaderOutput`

```diff

-1048.3.0.0.0
-  __TEXT.__text: 0xa7b74
-  __TEXT.__objc_methlist: 0x93d0
+1050.3.5.0.0
+  __TEXT.__text: 0xaa644
+  __TEXT.__objc_methlist: 0x96f8
   __TEXT.__const: 0x1938
-  __TEXT.__cstring: 0x6581
+  __TEXT.__cstring: 0x65f9
   __TEXT.__swift5_typeref: 0xeec
   __TEXT.__constg_swiftt: 0x960
   __TEXT.__swift5_builtin: 0xb4
   __TEXT.__swift5_types: 0xa4
-  __TEXT.__oslogstring: 0x285d
+  __TEXT.__oslogstring: 0x28a1
   __TEXT.__swift5_reflstr: 0x605
   __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_fieldmd: 0x7f8

   __TEXT.__swift_as_ret: 0x5c
   __TEXT.__swift_as_cont: 0x9c
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__gcc_except_tab: 0x1940
+  __TEXT.__gcc_except_tab: 0x1984
   __TEXT.__ustring: 0x9e
-  __TEXT.__unwind_info: 0x2968
+  __TEXT.__unwind_info: 0x29f0
   __TEXT.__eh_frame: 0xa28
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4948
+  __DATA_CONST.__objc_selrefs: 0x4a80
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x218
   __DATA_CONST.__objc_arraydata: 0x3f8
   __DATA_CONST.__got: 0x808
-  __AUTH_CONST.__const: 0x44e8
-  __AUTH_CONST.__cfstring: 0x64e0
-  __AUTH_CONST.__objc_const: 0xc148
+  __AUTH_CONST.__const: 0x4588
+  __AUTH_CONST.__cfstring: 0x6580
+  __AUTH_CONST.__objc_const: 0xc2c0
   __AUTH_CONST.__objc_intobj: 0x1218
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_doubleobj: 0x10

   __AUTH_CONST.__auth_ptr: 0x2c8
   __AUTH.__objc_data: 0x400
   __AUTH.__data: 0x70
-  __DATA.__objc_ivar: 0x90c
-  __DATA.__data: 0x1680
-  __DATA.__bss: 0x1110
+  __DATA.__objc_ivar: 0x920
+  __DATA.__data: 0x1690
+  __DATA.__bss: 0x1100
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x1d10
   __DATA_DIRTY.__data: 0xc20

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4083
-  Symbols:   7922
-  CStrings:  1182
+  Functions: 4143
+  Symbols:   8026
+  CStrings:  1186
 
Symbols:
+ -[SCROBrailleClient setTabularFocusRow:col:]
+ -[SCROBrailleClient setTabularZoomLevel:]
+ -[SCROBrailleClientXPC handleBrailleDidPanLeft:elementToken:appToken:lineOffset:displayToken:]
+ -[SCROBrailleClientXPC handleBrailleDidPanRight:elementToken:appToken:lineOffset:displayToken:]
+ -[SCROBrailleClientXPC handleBrailleDidPlanarPanPageDown:elementToken:appToken:displayToken:]
+ -[SCROBrailleClientXPC handleBrailleDidPlanarPanPageUp:elementToken:appToken:displayToken:]
+ -[SCROBrailleClientXPC setTabularFocusRow:col:]
+ -[SCROBrailleClientXPC setTabularZoomLevel:]
+ -[SCROBrailleDisplay _cancelPendingCellWrites]
+ -[SCROBrailleDisplay _getStructuredStatusCellIndex:forRawRouterIndex:]
+ -[SCROBrailleDisplay _linePanWindow]
+ -[SCROBrailleDisplay _structuredBraillePanWindow:isBackward:]
+ -[SCROBrailleDisplay _structuredBraillePlanarPanIsPageUp:]
+ -[SCROBrailleDisplay handleCommandTabularZoomInEvent:forDispatcher:]
+ -[SCROBrailleDisplay handleCommandTabularZoomOutEvent:forDispatcher:]
+ -[SCROBrailleDisplayCommandDispatcher _handleTabularZoomInEvent:]
+ -[SCROBrailleDisplayCommandDispatcher _handleTabularZoomOutEvent:]
+ -[SCROBrailleDisplayManager _dispatchPlanarPanPageForDisplay:isPageUp:success:elementToken:appToken:]
+ -[SCROBrailleDisplayManager _eventQueue_stepTabularZoomIn:]
+ -[SCROBrailleDisplayManager brailleDisplay:didPlanarPanPageDown:elementToken:appToken:]
+ -[SCROBrailleDisplayManager brailleDisplay:didPlanarPanPageUp:elementToken:appToken:]
+ -[SCROBrailleDisplayManager brailleDisplay:structuredBrailleRouterHitTabularCellWithKey:tableRow:tableCol:appToken:]
+ -[SCROBrailleDisplayManager brailleDisplay:structuredBrailleRouterHitTabularFocusedCellWithKey:appToken:]
+ -[SCROBrailleDisplayManager brailleDisplay:structuredBrailleRouterHitTabularStatusLineWithKey:appToken:]
+ -[SCROBrailleDisplayManager brailleDisplay:tabularZoomInWithKey:]
+ -[SCROBrailleDisplayManager brailleDisplay:tabularZoomOutWithKey:]
+ -[SCROBrailleDisplayManager setTabularFocusRow:col:]
+ -[SCROBrailleDisplayManager setTabularZoomLevel:]
+ -[SCROBrailleDisplayManager tabularZoomDidChange:]
+ -[SCROBrailleHandler handleBrailleDidPanLeft:elementToken:appToken:lineOffset:displayToken:]
+ -[SCROBrailleHandler handleBrailleDidPanRight:elementToken:appToken:lineOffset:displayToken:]
+ -[SCROBrailleHandler handleBrailleDidPlanarPanPageDown:elementToken:appToken:displayToken:]
+ -[SCROBrailleHandler handleBrailleDidPlanarPanPageUp:elementToken:appToken:displayToken:]
+ -[SCROBrailleHandler handleTabularZoomDidChange:]
+ -[SCROBrailleHandlerXPC handleBrailleDidPanLeft:elementToken:appToken:lineOffset:displayToken:]
+ -[SCROBrailleHandlerXPC handleBrailleDidPanRight:elementToken:appToken:lineOffset:displayToken:]
+ -[SCROBrailleHandlerXPC handleBrailleDidPlanarPanPageDown:elementToken:appToken:displayToken:]
+ -[SCROBrailleHandlerXPC handleBrailleDidPlanarPanPageUp:elementToken:appToken:displayToken:]
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
+ -[SCROMobileBrailleDisplayInputManager _storedUserDefaultsForModelIdentifier:]
+ -[SCROMobileBrailleDisplayInputManager _userDefaultsForDisplayWithToken:]
+ -[SCROMobileBrailleDisplayInputManager userDefaultsForModelIdentifier:productName:driverIdentifier:]
+ -[SCROMobileBrailleDisplayInputManagerCacheObject modelIdentifierForPlist]
+ -[SCROMobileBrailleDisplayInputManagerCacheObject setModelIdentifierForPlist:]
+ GCC_except_table1113
+ GCC_except_table1177
+ GCC_except_table1179
+ GCC_except_table1181
+ GCC_except_table1183
+ GCC_except_table1254
+ GCC_except_table128
+ GCC_except_table1284
+ GCC_except_table129
+ GCC_except_table1291
+ GCC_except_table1295
+ GCC_except_table1298
+ GCC_except_table1300
+ GCC_except_table132
+ GCC_except_table1330
+ GCC_except_table1337
+ GCC_except_table1469
+ GCC_except_table1682
+ GCC_except_table1808
+ GCC_except_table1949
+ GCC_except_table1951
+ GCC_except_table1960
+ GCC_except_table1972
+ GCC_except_table2056
+ GCC_except_table2101
+ GCC_except_table2107
+ GCC_except_table2221
+ GCC_except_table2242
+ GCC_except_table2251
+ GCC_except_table2259
+ GCC_except_table2362
+ GCC_except_table2546
+ GCC_except_table2567
+ GCC_except_table2677
+ GCC_except_table2678
+ GCC_except_table2679
+ GCC_except_table2683
+ GCC_except_table2688
+ GCC_except_table2689
+ GCC_except_table2690
+ GCC_except_table2691
+ GCC_except_table2692
+ GCC_except_table2694
+ GCC_except_table2695
+ GCC_except_table2696
+ GCC_except_table2700
+ GCC_except_table2705
+ GCC_except_table2707
+ GCC_except_table2710
+ GCC_except_table3058
+ GCC_except_table3076
+ GCC_except_table3095
+ GCC_except_table3096
+ GCC_except_table3097
+ GCC_except_table3160
+ GCC_except_table3162
+ GCC_except_table3164
+ GCC_except_table3165
+ GCC_except_table3167
+ GCC_except_table3169
+ GCC_except_table448
+ GCC_except_table462
+ GCC_except_table494
+ GCC_except_table495
+ GCC_except_table518
+ GCC_except_table519
+ GCC_except_table529
+ GCC_except_table531
+ GCC_except_table553
+ GCC_except_table556
+ GCC_except_table559
+ GCC_except_table560
+ GCC_except_table563
+ GCC_except_table573
+ GCC_except_table593
+ GCC_except_table596
+ GCC_except_table604
+ GCC_except_table606
+ GCC_except_table614
+ GCC_except_table630
+ GCC_except_table631
+ GCC_except_table638
+ GCC_except_table64
+ GCC_except_table642
+ GCC_except_table646
+ GCC_except_table664
+ GCC_except_table665
+ GCC_except_table668
+ GCC_except_table932
+ GCC_except_table973
+ GCC_except_table975
+ OBJC_IVAR_$_SCROBrailleDisplay._driverModelIdentifierForAnalytics
+ OBJC_IVAR_$_SCROBrailleKey._isTabularCellRoute
+ OBJC_IVAR_$_SCROBrailleKey._tabularCellCol
+ OBJC_IVAR_$_SCROBrailleKey._tabularCellRow
+ OBJC_IVAR_$_SCROMobileBrailleDisplayInputManagerCacheObject._modelIdentifierForPlist
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BRLLayoutManagerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SCROBrailleDisplayDelegate
+ ___101-[SCROBrailleDisplayManager _dispatchPlanarPanPageForDisplay:isPageUp:success:elementToken:appToken:]_block_invoke
+ ___101-[SCROBrailleDisplayManager _dispatchPlanarPanPageForDisplay:isPageUp:success:elementToken:appToken:]_block_invoke_2
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
+ ___92-[SCROBrailleHandlerXPC handleBrailleDidPlanarPanPageUp:elementToken:appToken:displayToken:]_block_invoke
+ ___94-[SCROBrailleHandlerXPC handleBrailleDidPlanarPanPageDown:elementToken:appToken:displayToken:]_block_invoke
+ ___95-[SCROBrailleHandlerXPC handleBrailleDidPanLeft:elementToken:appToken:lineOffset:displayToken:]_block_invoke
+ ___96-[SCROBrailleHandlerXPC handleBrailleDidPanRight:elementToken:appToken:lineOffset:displayToken:]_block_invoke
+ ___block_descriptor_72_e8_32s40s48s56s64s_e41_v16?0"<SCROBrailleClientCallbacksXPC>"8l
+ ___block_descriptor_73_e8_32s40s48s56s64s_e5_v8?0l
+ ___block_descriptor_80_e8_32s40s48s56s64s72s_e5_v8?0l
+ ___block_descriptor_80_e8_32s40s48s56s_e5_v8?0l
+ ___block_descriptor_81_e8_32s40s48s56s64s72s_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48s56s64s72s
+ ___destroy_helper_block_e8_32s40s48s56s64s72s
+ _kSCROBrailleDisplayModelIdentifierForAnalytics
+ _kSCROBraillePrintTextRowsAttribute
+ _objc_msgSend$_cancelPendingCellWrites
+ _objc_msgSend$_dispatchPlanarPanPageForDisplay:isPageUp:success:elementToken:appToken:
+ _objc_msgSend$_eventQueue_stepTabularZoomIn:
+ _objc_msgSend$_getStructuredStatusCellIndex:forRawRouterIndex:
+ _objc_msgSend$_linePanWindow
+ _objc_msgSend$_resetTabularCellRoute
+ _objc_msgSend$_storedUserDefaultsForModelIdentifier:
+ _objc_msgSend$_structuredBraillePanWindow:isBackward:
+ _objc_msgSend$_structuredBraillePlanarPanIsPageUp:
+ _objc_msgSend$_userDefaultsForDisplayWithToken:
+ _objc_msgSend$brailleDisplay:didPlanarPanPageDown:elementToken:appToken:
+ _objc_msgSend$brailleDisplay:didPlanarPanPageUp:elementToken:appToken:
+ _objc_msgSend$brailleDisplay:structuredBrailleRouterHitTabularCellWithKey:tableRow:tableCol:appToken:
+ _objc_msgSend$brailleDisplay:structuredBrailleRouterHitTabularFocusedCellWithKey:appToken:
+ _objc_msgSend$brailleDisplay:structuredBrailleRouterHitTabularStatusLineWithKey:appToken:
+ _objc_msgSend$brailleDisplay:tabularZoomInWithKey:
+ _objc_msgSend$brailleDisplay:tabularZoomOutWithKey:
+ _objc_msgSend$currentPrintTextRows
+ _objc_msgSend$cycleTabularZoom
+ _objc_msgSend$decreaseTabularZoom
+ _objc_msgSend$handleBrailleDidPanLeft:elementToken:appToken:lineOffset:displayToken:
+ _objc_msgSend$handleBrailleDidPanRight:elementToken:appToken:lineOffset:displayToken:
+ _objc_msgSend$handleBrailleDidPlanarPanPageDown:elementToken:appToken:displayToken:
+ _objc_msgSend$handleBrailleDidPlanarPanPageUp:elementToken:appToken:displayToken:
+ _objc_msgSend$handleCommandTabularZoomInEvent:forDispatcher:
+ _objc_msgSend$handleCommandTabularZoomOutEvent:forDispatcher:
+ _objc_msgSend$handleTabularZoomDidChange:
+ _objc_msgSend$increaseTabularZoom
+ _objc_msgSend$modelIdentifierForAnalytics
+ _objc_msgSend$routingKeyHitTestAtCellIndex:elementToken:isTextLine:brailleOffset:printTextOffset:statusCellIndex:shouldPerformActions:routerClickCount:tableRow:tableCol:
+ _objc_msgSend$setIsTabularCellRoute:
+ _objc_msgSend$setTabularCellCol:
+ _objc_msgSend$setTabularCellRow:
+ _objc_msgSend$setTabularFocusRow:col:
+ _objc_msgSend$setTabularZoomLevel:
+ _objc_msgSend$updateTabularFocusToRow:col:
+ _objc_msgSend$userDefaultsForModelIdentifier:productName:driverIdentifier:
- -[SCROBrailleClientXPC handleBrailleDidPanLeft:elementToken:appToken:lineOffset:]
- -[SCROBrailleClientXPC handleBrailleDidPanRight:elementToken:appToken:lineOffset:]
- -[SCROBrailleHandler handleBrailleDidPanLeft:elementToken:appToken:lineOffset:]
- -[SCROBrailleHandler handleBrailleDidPanRight:elementToken:appToken:lineOffset:]
- -[SCROBrailleHandlerXPC handleBrailleDidPanLeft:elementToken:appToken:lineOffset:]
- -[SCROBrailleHandlerXPC handleBrailleDidPanRight:elementToken:appToken:lineOffset:]
- -[SCROMobileBrailleDisplayInputManager userDefaultsForModelIdentifier:]
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
- GCC_except_table551
- GCC_except_table564
- GCC_except_table584
- GCC_except_table586
- GCC_except_table587
- GCC_except_table597
- GCC_except_table605
- GCC_except_table619
- GCC_except_table62
- GCC_except_table620
- GCC_except_table621
- GCC_except_table622
- GCC_except_table624
- GCC_except_table655
- GCC_except_table656
- GCC_except_table659
- GCC_except_table903
- GCC_except_table944
- GCC_except_table946
- ___82-[SCROBrailleHandlerXPC handleBrailleDidPanLeft:elementToken:appToken:lineOffset:]_block_invoke
- ___83-[SCROBrailleHandlerXPC handleBrailleDidPanRight:elementToken:appToken:lineOffset:]_block_invoke
- ___block_descriptor_72_e8_32s40s48s56s64s_e5_v8?0l
- ___isBrailleXPCOn_block_invoke
- _isBrailleXPCOn
- _objc_msgSend$handleBrailleDidPanLeft:elementToken:appToken:lineOffset:
- _objc_msgSend$handleBrailleDidPanRight:elementToken:appToken:lineOffset:
- _objc_msgSend$routingKeyHitTestAtCellIndex:elementToken:isTextLine:brailleOffset:printTextOffset:statusCellIndex:shouldPerformActions:routerClickCount:
- _objc_msgSend$userDefaultsForModelIdentifier:
- isBrailleXPCOn.brailleXPCOn
- isBrailleXPCOn.onceToken
CStrings:
+ "Braille: copied %lu command assignments for %{public}@ from %{public}@"
+ "BrailleDisplayModelIdentifierForAnalytics"
+ "SCRBraille.tabularZoomIn"
+ "SCRBraille.tabularZoomOut"
+ "SCRBrailleAssignmentsMigratedFrom"
+ "SCROBraillePrintTextRowsAttribute"
+ "_isTabularCellRoute"
+ "_tabularCellCol"
+ "_tabularCellRow"
+ "setTabularFocusRow requires XPC"
+ "setTabularZoomLevel ignoring out-of-range level"
+ "setTabularZoomLevel requires XPC"
- "Braille_XPC"
- "Braille_XPC_Off"
- "NLS eReader Humanware"
- "SCROBrailleClient using Mach"
- "SCROBrailleClient using XPC"
- "SCROBrailleHandler using Mach"
- "SCROBrailleHandler using XPC"
- "com.apple.scrod.braille.driver.nls.ereader"
```
