## ScreenReaderOutput

> `/System/Library/PrivateFrameworks/ScreenReaderOutput.framework/ScreenReaderOutput`

```diff

-467.3.12.0.0
-  __TEXT.__text: 0x9e9c0
-  __TEXT.__objc_methlist: 0x9618
+467.3.22.0.0
+  __TEXT.__text: 0x9ea0c
+  __TEXT.__objc_methlist: 0x9598
   __TEXT.__const: 0x185c
-  __TEXT.__cstring: 0x5d80
+  __TEXT.__cstring: 0x5d78
   __TEXT.__swift5_typeref: 0xeec
   __TEXT.__constg_swiftt: 0x960
   __TEXT.__swift5_builtin: 0xb4

   __TEXT.__swift_as_ret: 0x5c
   __TEXT.__swift_as_cont: 0x9c
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__gcc_except_tab: 0x1984
+  __TEXT.__gcc_except_tab: 0x19b8
   __TEXT.__ustring: 0x9e
   __TEXT.__unwind_info: 0x3528
   __TEXT.__eh_frame: 0xa30

   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4aa0
+  __DATA_CONST.__objc_selrefs: 0x4ac8
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x220
   __DATA_CONST.__objc_arraydata: 0x380
   __DATA_CONST.__got: 0x790
   __AUTH_CONST.__const: 0x32a0
-  __AUTH_CONST.__cfstring: 0x5960
-  __AUTH_CONST.__objc_const: 0xc370
+  __AUTH_CONST.__cfstring: 0x5940
+  __AUTH_CONST.__objc_const: 0xc390
   __AUTH_CONST.__objc_intobj: 0xa68
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_doubleobj: 0x10

   __AUTH_CONST.__auth_got: 0x10b0
   __AUTH.__objc_data: 0x4a0
   __AUTH.__data: 0x88
-  __DATA.__objc_ivar: 0x920
+  __DATA.__objc_ivar: 0x924
   __DATA.__data: 0x16a0
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x1d10

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4106
+  Functions: 4102
   Symbols:   5962
-  CStrings:  1119
+  CStrings:  1118
 
Symbols:
+ +[SCROBrailleClientXPC listenerEndpointForTesting]
+ +[SCROBrailleClientXPC setListenerEndpointForTesting:]
+ -[SCROBrailleDisplay _performWithContentLockIfValid:]
+ -[SCROBrailleDisplay shouldHandleCursorMovementForDispatcher:]
+ -[SCROBrailleDisplayManager _dispatchPlanarPanPageForDisplay:isPageUp:action:elementToken:appToken:]
+ -[SCROBrailleHandlerXPC initWithBrailleDisplayManager:listener:]
+ GCC_except_table1070
+ GCC_except_table1134
+ GCC_except_table1136
+ GCC_except_table1138
+ GCC_except_table1140
+ GCC_except_table1207
+ GCC_except_table123
+ GCC_except_table1235
+ GCC_except_table124
+ GCC_except_table1240
+ GCC_except_table1244
+ GCC_except_table1247
+ GCC_except_table1249
+ GCC_except_table127
+ GCC_except_table1280
+ GCC_except_table1287
+ GCC_except_table1419
+ GCC_except_table1628
+ GCC_except_table1753
+ GCC_except_table1888
+ GCC_except_table1890
+ GCC_except_table1898
+ GCC_except_table1908
+ GCC_except_table1994
+ GCC_except_table2039
+ GCC_except_table2155
+ GCC_except_table2176
+ GCC_except_table2181
+ GCC_except_table2187
+ GCC_except_table2286
+ GCC_except_table2472
+ GCC_except_table2490
+ GCC_except_table2606
+ GCC_except_table2607
+ GCC_except_table2608
+ GCC_except_table2617
+ GCC_except_table2618
+ GCC_except_table2619
+ GCC_except_table2620
+ GCC_except_table2634
+ GCC_except_table2636
+ GCC_except_table2639
+ GCC_except_table3015
+ GCC_except_table3031
+ GCC_except_table3050
+ GCC_except_table3051
+ GCC_except_table3052
+ GCC_except_table3118
+ GCC_except_table3120
+ GCC_except_table3123
+ GCC_except_table3125
+ GCC_except_table484
+ GCC_except_table499
+ GCC_except_table503
+ GCC_except_table558
+ GCC_except_table568
+ GCC_except_table570
+ GCC_except_table589
+ GCC_except_table59
+ GCC_except_table591
+ GCC_except_table595
+ GCC_except_table598
+ GCC_except_table608
+ GCC_except_table628
+ GCC_except_table631
+ GCC_except_table639
+ GCC_except_table641
+ GCC_except_table647
+ GCC_except_table664
+ GCC_except_table666
+ GCC_except_table671
+ GCC_except_table673
+ GCC_except_table677
+ GCC_except_table696
+ GCC_except_table699
+ GCC_except_table897
+ GCC_except_table938
+ GCC_except_table940
+ _OBJC_IVAR_$_SCROBrailleHandlerXPC._isMachServiceListener
+ __ListenerEndpointForTesting
+ __OBJC_$_CLASS_PROP_LIST_SCROBrailleClientXPC
+ ___100-[SCROBrailleDisplayManager _dispatchPlanarPanPageForDisplay:isPageUp:action:elementToken:appToken:]_block_invoke
+ ___100-[SCROBrailleDisplayManager _dispatchPlanarPanPageForDisplay:isPageUp:action:elementToken:appToken:]_block_invoke_2
+ ___47-[SCROBrailleDisplay _throttledFlushTimerFired]_block_invoke
+ ___48-[SCROBrailleDisplay _sendCellsToDriver:length:]_block_invoke
+ ___53-[SCROBrailleDisplay _updateWithWindow:isMainWindow:]_block_invoke
+ ___53-[SCROBrailleDisplay _updateWithWindow:isMainWindow:]_block_invoke_2
+ ___block_descriptor_64_e8_32s40s48s_e41_v16?0"<SCROBrailleClientCallbacksXPC>"8ls32l8s40l8s48l8
+ ___block_descriptor_73_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_81_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- -[SCROBrailleClient resetEditingManager]
- -[SCROBrailleClient selectAllForToken:]
- -[SCROBrailleClient setFocused:forToken:]
- -[SCROBrailleClient setSelection:forToken:]
- -[SCROBrailleClient unselectAllForToken:]
- -[SCROBrailleClientXPC selectAllForToken:]
- -[SCROBrailleClientXPC setFocused:forToken:]
- -[SCROBrailleClientXPC setSelection:forToken:]
- -[SCROBrailleClientXPC unselectAllForToken:]
- -[SCROBrailleDisplayManager _dispatchPlanarPanPageForDisplay:isPageUp:success:elementToken:appToken:]
- -[SCROBrailleHandlerXPC selectAllForToken:]
- -[SCROBrailleHandlerXPC setFocused:forToken:]
- -[SCROBrailleHandlerXPC setSelection:forToken:]
- -[SCROBrailleHandlerXPC unselectAllForToken:]
- GCC_except_table1069
- GCC_except_table1133
- GCC_except_table1135
- GCC_except_table1137
- GCC_except_table1139
- GCC_except_table1206
- GCC_except_table1234
- GCC_except_table1239
- GCC_except_table1243
- GCC_except_table1246
- GCC_except_table1248
- GCC_except_table1279
- GCC_except_table128
- GCC_except_table1286
- GCC_except_table129
- GCC_except_table132
- GCC_except_table1418
- GCC_except_table1631
- GCC_except_table1755
- GCC_except_table1894
- GCC_except_table1896
- GCC_except_table1904
- GCC_except_table1914
- GCC_except_table1998
- GCC_except_table2047
- GCC_except_table2159
- GCC_except_table2180
- GCC_except_table2185
- GCC_except_table2191
- GCC_except_table2290
- GCC_except_table2476
- GCC_except_table2494
- GCC_except_table2610
- GCC_except_table2611
- GCC_except_table2616
- GCC_except_table2622
- GCC_except_table2627
- GCC_except_table2628
- GCC_except_table2633
- GCC_except_table2638
- GCC_except_table2640
- GCC_except_table2643
- GCC_except_table3019
- GCC_except_table3035
- GCC_except_table3054
- GCC_except_table3055
- GCC_except_table3056
- GCC_except_table3124
- GCC_except_table3126
- GCC_except_table3129
- GCC_except_table3131
- GCC_except_table489
- GCC_except_table501
- GCC_except_table556
- GCC_except_table567
- GCC_except_table569
- GCC_except_table587
- GCC_except_table590
- GCC_except_table593
- GCC_except_table597
- GCC_except_table607
- GCC_except_table627
- GCC_except_table629
- GCC_except_table638
- GCC_except_table64
- GCC_except_table640
- GCC_except_table646
- GCC_except_table660
- GCC_except_table665
- GCC_except_table669
- GCC_except_table672
- GCC_except_table676
- GCC_except_table694
- GCC_except_table698
- GCC_except_table896
- GCC_except_table937
- GCC_except_table939
- ___101-[SCROBrailleDisplayManager _dispatchPlanarPanPageForDisplay:isPageUp:success:elementToken:appToken:]_block_invoke
- ___101-[SCROBrailleDisplayManager _dispatchPlanarPanPageForDisplay:isPageUp:success:elementToken:appToken:]_block_invoke_2
- ___block_descriptor_64_e8_32s40s48s56s_e41_v16?0"<SCROBrailleClientCallbacksXPC>"8ls32l8s40l8s48l8s56l8
- ___block_descriptor_73_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_81_e8_32s40s48s56s64s72s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
CStrings:
+ "action"
- "focused"
- "selection"
```
