## ScreenReaderOutput

> `/System/Library/PrivateFrameworks/ScreenReaderOutput.framework/ScreenReaderOutput`

```diff

-467.3.3.0.0
-  __TEXT.__text: 0x99e14
-  __TEXT.__objc_methlist: 0x9248
+467.3.4.0.0
+  __TEXT.__text: 0x9abbc
+  __TEXT.__objc_methlist: 0x9328
   __TEXT.__const: 0x184c
   __TEXT.__cstring: 0x5bf5
   __TEXT.__swift5_typeref: 0xeec

   __TEXT.__swift_as_ret: 0x5c
   __TEXT.__swift_as_cont: 0x9c
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__gcc_except_tab: 0x1964
+  __TEXT.__gcc_except_tab: 0x1984
   __TEXT.__ustring: 0x9e
-  __TEXT.__unwind_info: 0x3428
+  __TEXT.__unwind_info: 0x3470
   __TEXT.__eh_frame: 0xa30
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1298
+  __DATA_CONST.__const: 0x1310
   __DATA_CONST.__objc_classlist: 0x328
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4878
+  __DATA_CONST.__objc_selrefs: 0x48c0
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x210
   __DATA_CONST.__objc_arraydata: 0x380
   __DATA_CONST.__got: 0x790
   __AUTH_CONST.__const: 0x3280
   __AUTH_CONST.__cfstring: 0x5720
-  __AUTH_CONST.__objc_const: 0xbda0
+  __AUTH_CONST.__objc_const: 0xbdd0
   __AUTH_CONST.__objc_intobj: 0xa68
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_doubleobj: 0x10

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4015
-  Symbols:   5820
+  Functions: 4032
+  Symbols:   5840
   CStrings:  1080
 
Symbols:
+ -[SCROBrailleClientXPC handleBrailleDidPlanarPanPageDown:elementToken:appToken:displayToken:]
+ -[SCROBrailleClientXPC handleBrailleDidPlanarPanPageUp:elementToken:appToken:displayToken:]
+ -[SCROBrailleDisplay _getStructuredStatusCellIndex:forRawRouterIndex:]
+ -[SCROBrailleDisplay _linePanWindow]
+ -[SCROBrailleDisplay _structuredBraillePanWindow:isBackward:]
+ -[SCROBrailleDisplay _structuredBraillePlanarPanIsPageUp:]
+ -[SCROBrailleDisplayManager _dispatchPlanarPanPageForDisplay:isPageUp:success:elementToken:appToken:]
+ -[SCROBrailleDisplayManager brailleDisplay:didPlanarPanPageDown:elementToken:appToken:]
+ -[SCROBrailleDisplayManager brailleDisplay:didPlanarPanPageUp:elementToken:appToken:]
+ -[SCROBrailleHandler handleBrailleDidPlanarPanPageDown:elementToken:appToken:displayToken:]
+ -[SCROBrailleHandler handleBrailleDidPlanarPanPageUp:elementToken:appToken:displayToken:]
+ -[SCROBrailleHandlerXPC handleBrailleDidPlanarPanPageDown:elementToken:appToken:displayToken:]
+ -[SCROBrailleHandlerXPC handleBrailleDidPlanarPanPageUp:elementToken:appToken:displayToken:]
+ GCC_except_table1025
+ GCC_except_table1093
+ GCC_except_table1095
+ GCC_except_table1162
+ GCC_except_table1199
+ GCC_except_table1202
+ GCC_except_table1204
+ GCC_except_table1235
+ GCC_except_table1242
+ GCC_except_table1374
+ GCC_except_table1587
+ GCC_except_table1711
+ GCC_except_table1850
+ GCC_except_table1852
+ GCC_except_table1860
+ GCC_except_table1870
+ GCC_except_table1954
+ GCC_except_table1999
+ GCC_except_table2003
+ GCC_except_table2115
+ GCC_except_table2136
+ GCC_except_table2141
+ GCC_except_table2147
+ GCC_except_table2246
+ GCC_except_table2433
+ GCC_except_table2451
+ GCC_except_table2579
+ GCC_except_table2581
+ GCC_except_table2582
+ GCC_except_table2584
+ GCC_except_table2585
+ GCC_except_table2586
+ GCC_except_table2590
+ GCC_except_table2595
+ GCC_except_table2597
+ GCC_except_table2600
+ GCC_except_table2948
+ GCC_except_table2964
+ GCC_except_table2983
+ GCC_except_table2984
+ GCC_except_table2985
+ GCC_except_table3048
+ GCC_except_table3050
+ GCC_except_table3052
+ GCC_except_table3053
+ GCC_except_table3055
+ GCC_except_table3057
+ GCC_except_table444
+ GCC_except_table456
+ GCC_except_table488
+ GCC_except_table489
+ GCC_except_table511
+ GCC_except_table512
+ GCC_except_table522
+ GCC_except_table524
+ GCC_except_table542
+ GCC_except_table543
+ GCC_except_table549
+ GCC_except_table552
+ GCC_except_table562
+ GCC_except_table582
+ GCC_except_table584
+ GCC_except_table585
+ GCC_except_table593
+ GCC_except_table595
+ GCC_except_table601
+ GCC_except_table615
+ GCC_except_table617
+ GCC_except_table618
+ GCC_except_table624
+ GCC_except_table625
+ GCC_except_table631
+ GCC_except_table650
+ GCC_except_table653
+ GCC_except_table851
+ GCC_except_table892
+ GCC_except_table894
+ ___101-[SCROBrailleDisplayManager _dispatchPlanarPanPageForDisplay:isPageUp:success:elementToken:appToken:]_block_invoke
+ ___101-[SCROBrailleDisplayManager _dispatchPlanarPanPageForDisplay:isPageUp:success:elementToken:appToken:]_block_invoke_2
+ ___92-[SCROBrailleHandlerXPC handleBrailleDidPlanarPanPageUp:elementToken:appToken:displayToken:]_block_invoke
+ ___94-[SCROBrailleHandlerXPC handleBrailleDidPlanarPanPageDown:elementToken:appToken:displayToken:]_block_invoke
+ ___block_descriptor_64_e8_32s40s48s56s_e41_v16?0"<SCROBrailleClientCallbacksXPC>"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_73_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_81_e8_32s40s48s56s64s72s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
- GCC_except_table1021
- GCC_except_table1085
- GCC_except_table1087
- GCC_except_table1153
- GCC_except_table1181
- GCC_except_table1186
- GCC_except_table1193
- GCC_except_table1226
- GCC_except_table1233
- GCC_except_table1363
- GCC_except_table1572
- GCC_except_table1694
- GCC_except_table1833
- GCC_except_table1835
- GCC_except_table1843
- GCC_except_table1853
- GCC_except_table1937
- GCC_except_table1982
- GCC_except_table1986
- GCC_except_table2098
- GCC_except_table2119
- GCC_except_table2124
- GCC_except_table2130
- GCC_except_table2229
- GCC_except_table2416
- GCC_except_table2434
- GCC_except_table2550
- GCC_except_table2551
- GCC_except_table2552
- GCC_except_table2556
- GCC_except_table2561
- GCC_except_table2562
- GCC_except_table2563
- GCC_except_table2564
- GCC_except_table2565
- GCC_except_table2583
- GCC_except_table2931
- GCC_except_table2947
- GCC_except_table2966
- GCC_except_table2967
- GCC_except_table2968
- GCC_except_table3031
- GCC_except_table3033
- GCC_except_table3035
- GCC_except_table3036
- GCC_except_table3038
- GCC_except_table3040
- GCC_except_table440
- GCC_except_table452
- GCC_except_table484
- GCC_except_table485
- GCC_except_table507
- GCC_except_table508
- GCC_except_table518
- GCC_except_table520
- GCC_except_table538
- GCC_except_table539
- GCC_except_table541
- GCC_except_table544
- GCC_except_table558
- GCC_except_table578
- GCC_except_table580
- GCC_except_table581
- GCC_except_table589
- GCC_except_table591
- GCC_except_table597
- GCC_except_table611
- GCC_except_table612
- GCC_except_table613
- GCC_except_table614
- GCC_except_table621
- GCC_except_table623
- GCC_except_table645
- GCC_except_table646
- GCC_except_table847
- GCC_except_table888
- GCC_except_table890
```
