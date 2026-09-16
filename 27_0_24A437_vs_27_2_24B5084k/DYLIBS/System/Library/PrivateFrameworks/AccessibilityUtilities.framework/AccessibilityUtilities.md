## AccessibilityUtilities

> `/System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities`

```diff

-3240.9.0.0.0
-  __TEXT.__text: 0x1ffde8
-  __TEXT.__objc_methlist: 0xfd5c
+3245.7.1.0.0
+  __TEXT.__text: 0x2046b8
+  __TEXT.__objc_methlist: 0xff24
   __TEXT.__dlopen_cstrs: 0xb89
-  __TEXT.__const: 0x8e28
-  __TEXT.__swift5_typeref: 0x2714
-  __TEXT.__swift5_capture: 0x2a24
-  __TEXT.__cstring: 0x1ddea
-  __TEXT.__constg_swiftt: 0x1760
-  __TEXT.__swift5_reflstr: 0xb79c
-  __TEXT.__swift5_fieldmd: 0x44e8
+  __TEXT.__const: 0x8f48
+  __TEXT.__swift5_typeref: 0x2732
+  __TEXT.__swift5_capture: 0x2ab4
+  __TEXT.__cstring: 0x1e008
+  __TEXT.__constg_swiftt: 0x178c
+  __TEXT.__swift5_reflstr: 0xb91c
+  __TEXT.__swift5_fieldmd: 0x45ac
   __TEXT.__swift5_builtin: 0x5dc
   __TEXT.__swift5_assocty: 0x978
-  __TEXT.__swift5_proto: 0x5ec
-  __TEXT.__swift5_types: 0x244
+  __TEXT.__swift5_proto: 0x5fc
+  __TEXT.__swift5_types: 0x248
   __TEXT.__swift_as_entry: 0x10c
   __TEXT.__swift_as_ret: 0x154
   __TEXT.__swift_as_cont: 0x198
-  __TEXT.__oslogstring: 0x6d72
+  __TEXT.__oslogstring: 0x6ea1
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__gcc_except_tab: 0x136c
+  __TEXT.__gcc_except_tab: 0x13dc
   __TEXT.__ustring: 0x68
-  __TEXT.__unwind_info: 0xc340
-  __TEXT.__eh_frame: 0x7a28
+  __TEXT.__unwind_info: 0xc580
+  __TEXT.__eh_frame: 0x7b50
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5b28
-  __DATA_CONST.__objc_classlist: 0x4c0
+  __DATA_CONST.__const: 0x5c20
+  __DATA_CONST.__objc_classlist: 0x4d0
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa258
+  __DATA_CONST.__objc_selrefs: 0xa328
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0x300
+  __DATA_CONST.__objc_superrefs: 0x308
   __DATA_CONST.__objc_arraydata: 0x9d8
-  __DATA_CONST.__got: 0x23d8
-  __AUTH_CONST.__const: 0xa498
-  __AUTH_CONST.__cfstring: 0x13ba0
-  __AUTH_CONST.__objc_const: 0x1c0f8
-  __AUTH_CONST.__objc_intobj: 0x16c8
+  __DATA_CONST.__got: 0x23e0
+  __AUTH_CONST.__const: 0xa620
+  __AUTH_CONST.__cfstring: 0x13ca0
+  __AUTH_CONST.__objc_const: 0x1c560
+  __AUTH_CONST.__objc_intobj: 0x16e0
   __AUTH_CONST.__objc_arrayobj: 0x330
   __AUTH_CONST.__objc_dictobj: 0x2f8
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__auth_got: 0x2df8
-  __AUTH.__objc_data: 0x29a8
+  __AUTH.__objc_data: 0x2a40
   __AUTH.__data: 0x9b0
-  __DATA.__objc_ivar: 0xbe8
-  __DATA.__data: 0x5238
-  __DATA_DIRTY.__objc_data: 0x3240
-  __DATA_DIRTY.__data: 0x880
-  __DATA_DIRTY.__bss: 0x37c0
+  __DATA.__objc_ivar: 0xc00
+  __DATA.__data: 0x52b8
+  __DATA_DIRTY.__objc_data: 0x3320
+  __DATA_DIRTY.__data: 0x8c8
+  __DATA_DIRTY.__bss: 0x39c0
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 15406
-  Symbols:   13875
-  CStrings:  4453
+  Functions: 15555
+  Symbols:   13966
+  CStrings:  4476
 
Symbols:
+ +[AXTripleClickHelpers beginClassicInvertColorsRequestWithValue:]
+ +[AXTripleClickHelpers beginSmartInvertColorsRequestWithValue:]
+ +[AXTripleClickHelpers classicInvertColorsEnabled]
+ +[AXTripleClickHelpers commitClassicInvertColorsRequestIfCurrent:]
+ +[AXTripleClickHelpers commitSmartInvertColorsRequestIfCurrent:]
+ +[AXTripleClickHelpers smartInvertColorsEnabled]
+ +[AXTripleClickHelpers toggleChatterbox]
+ -[AXCustomizableMouse removeAllCustomActions]
+ -[AXInvertColorsSettingsEvent .cxx_destruct]
+ -[AXInvertColorsSettingsEvent dictionaryRepresentation]
+ -[AXInvertColorsSettingsEvent feature]
+ -[AXInvertColorsSettingsEvent initWithDictionaryRepresentation:]
+ -[AXInvertColorsSettingsEvent initWithFeature:state:source:]
+ -[AXInvertColorsSettingsEvent isEnabled]
+ -[AXInvertColorsSettingsEvent processName]
+ -[AXInvertColorsSettingsEvent source]
+ -[AXInvertColorsSettingsEvent timestamp]
+ -[AXSettings(LegacyImplementation) latestInvertColorsSettingsEventDictionaries]
+ -[AXSettings(LegacyImplementation) latestInvertColorsSettingsEvents]
+ -[AXSettings(LegacyImplementation) registerInvertColorsSettingsEvent:]
+ -[AXSettings(LegacyImplementation) registerInvertColorsSettingsEventWithFeature:state:source:]
+ -[AXSettings(LegacyImplementation) setLatestInvertColorsSettingsEventDictionaries:]
+ -[AXSettings(LegacyImplementation) setLatestInvertColorsSettingsEvents:]
+ GCC_except_table1003
+ GCC_except_table1007
+ GCC_except_table1020
+ GCC_except_table1034
+ GCC_except_table1156
+ GCC_except_table120
+ GCC_except_table1264
+ GCC_except_table132
+ GCC_except_table134
+ GCC_except_table1355
+ GCC_except_table137
+ GCC_except_table1378
+ GCC_except_table1413
+ GCC_except_table144
+ GCC_except_table1458
+ GCC_except_table146
+ GCC_except_table148
+ GCC_except_table1487
+ GCC_except_table152
+ GCC_except_table1550
+ GCC_except_table156
+ GCC_except_table1574
+ GCC_except_table1578
+ GCC_except_table1580
+ GCC_except_table1583
+ GCC_except_table1589
+ GCC_except_table165
+ GCC_except_table1679
+ GCC_except_table1687
+ GCC_except_table1705
+ GCC_except_table1708
+ GCC_except_table1710
+ GCC_except_table1714
+ GCC_except_table1717
+ GCC_except_table1719
+ GCC_except_table172
+ GCC_except_table1853
+ GCC_except_table1868
+ GCC_except_table1889
+ GCC_except_table1890
+ GCC_except_table1891
+ GCC_except_table1893
+ GCC_except_table1894
+ GCC_except_table1895
+ GCC_except_table1896
+ GCC_except_table2234
+ GCC_except_table2237
+ GCC_except_table2240
+ GCC_except_table2242
+ GCC_except_table2244
+ GCC_except_table2246
+ GCC_except_table2248
+ GCC_except_table2336
+ GCC_except_table2374
+ GCC_except_table240
+ GCC_except_table2441
+ GCC_except_table2450
+ GCC_except_table2479
+ GCC_except_table2515
+ GCC_except_table2524
+ GCC_except_table2540
+ GCC_except_table2567
+ GCC_except_table264
+ GCC_except_table2708
+ GCC_except_table2767
+ GCC_except_table2788
+ GCC_except_table2942
+ GCC_except_table3012
+ GCC_except_table3023
+ GCC_except_table3025
+ GCC_except_table3032
+ GCC_except_table307
+ GCC_except_table3146
+ GCC_except_table3158
+ GCC_except_table3498
+ GCC_except_table3502
+ GCC_except_table3531
+ GCC_except_table3535
+ GCC_except_table3644
+ GCC_except_table3657
+ GCC_except_table3667
+ GCC_except_table3772
+ GCC_except_table3777
+ GCC_except_table3863
+ GCC_except_table423
+ GCC_except_table4357
+ GCC_except_table4365
+ GCC_except_table4366
+ GCC_except_table4374
+ GCC_except_table4375
+ GCC_except_table4383
+ GCC_except_table4387
+ GCC_except_table4389
+ GCC_except_table4496
+ GCC_except_table4509
+ GCC_except_table4722
+ GCC_except_table4726
+ GCC_except_table4731
+ GCC_except_table4753
+ GCC_except_table4959
+ GCC_except_table5002
+ GCC_except_table5021
+ GCC_except_table671
+ GCC_except_table678
+ GCC_except_table681
+ GCC_except_table683
+ GCC_except_table712
+ GCC_except_table741
+ GCC_except_table758
+ GCC_except_table821
+ GCC_except_table827
+ GCC_except_table831
+ GCC_except_table880
+ GCC_except_table943
+ GCC_except_table991
+ _AXDeviceSupportsChatterbox
+ _AXInvertColorsSettingsEventFeatureClassicInvert
+ _AXInvertColorsSettingsEventFeatureSmartInvert
+ _AXInvertColorsSettingsEventSourceAccessibilityShortcut
+ _AXInvertColorsSettingsEventSourceSettingsApp
+ _AXInvertColorsSettingsEventSourceUnknown
+ _OBJC_CLASS_$_AXInvertColorsSettingsEvent
+ _OBJC_CLASS_$__TtCE22AccessibilityUtilitiesCSo10AXSettings10Chatterbox
+ _OBJC_IVAR_$_AXInvertColorsSettingsEvent._feature
+ _OBJC_IVAR_$_AXInvertColorsSettingsEvent._processName
+ _OBJC_IVAR_$_AXInvertColorsSettingsEvent._source
+ _OBJC_IVAR_$_AXInvertColorsSettingsEvent._state
+ _OBJC_IVAR_$_AXInvertColorsSettingsEvent._timestamp
+ _OBJC_IVAR_$_AXServer._serverIdentifierLock
+ _OBJC_METACLASS_$_AXInvertColorsSettingsEvent
+ _OBJC_METACLASS_$__TtCE22AccessibilityUtilitiesCSo10AXSettings10Chatterbox
+ __DATA__TtCE22AccessibilityUtilitiesCSo10AXSettings10Chatterbox
+ __INSTANCE_METHODS__TtCE22AccessibilityUtilitiesCSo10AXSettings10Chatterbox
+ __IVARS__TtCE22AccessibilityUtilitiesCSo10AXSettings10Chatterbox
+ __METACLASS_DATA__TtCE22AccessibilityUtilitiesCSo10AXSettings10Chatterbox
+ __OBJC_$_INSTANCE_METHODS_AXInvertColorsSettingsEvent
+ __OBJC_$_INSTANCE_VARIABLES_AXInvertColorsSettingsEvent
+ __OBJC_$_PROP_LIST_AXInvertColorsSettingsEvent
+ __OBJC_CLASS_RO_$_AXInvertColorsSettingsEvent
+ __OBJC_METACLASS_RO_$_AXInvertColorsSettingsEvent
+ __PROPERTIES__TtCE22AccessibilityUtilitiesCSo10AXSettings10Chatterbox
+ ___28-[AXServer serverIdentifier]_block_invoke
+ ___48+[AXTripleClickHelpers smartInvertColorsEnabled]_block_invoke
+ ___50+[AXTripleClickHelpers classicInvertColorsEnabled]_block_invoke
+ ___63+[AXTripleClickHelpers beginSmartInvertColorsRequestWithValue:]_block_invoke
+ ___64+[AXTripleClickHelpers commitSmartInvertColorsRequestIfCurrent:]_block_invoke
+ ___65+[AXTripleClickHelpers beginClassicInvertColorsRequestWithValue:]_block_invoke
+ ___66+[AXTripleClickHelpers commitClassicInvertColorsRequestIfCurrent:]_block_invoke
+ ___68-[AXSettings(LegacyImplementation) latestInvertColorsSettingsEvents]_block_invoke
+ ___72-[AXSettings(LegacyImplementation) setLatestInvertColorsSettingsEvents:]_block_invoke
+ ___block_descriptor_32_e37_16?0"AXInvertColorsSettingsEvent"8l
+ ___block_descriptor_40_e8_32s_e34_v24?0"NSDictionary"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_49_e34_v24?0"NSDictionary"8"NSError"16l
+ ___swift_closure_destructor.1047Tm
+ __block_invoke.count
+ __classicInvertColorsRequestGeneration
+ __invertColorsRequestLock
+ __pendingClassicInvertColorsValue
+ __pendingSmartInvertColorsValue
+ __smartInvertColorsRequestGeneration
+ _associated conformance So10AXSettingsC22AccessibilityUtilitiesE10ChatterboxC06AXCoreC018AXSelectorRoutableAcF13AXReflectable
+ _associated conformance So10AXSettingsC22AccessibilityUtilitiesE10ChatterboxC06AXCoreC020AXObservableSettingsAC11Observation10Observable
+ _associated conformance So10AXSettingsC22AccessibilityUtilitiesE10ChatterboxC06AXCoreC020AXObservableSettingsAcF18AXSelectorRoutable
+ _keypath_get.711Tm
+ _keypath_get.727Tm
+ _keypath_get.787Tm
+ _keypath_get.977Tm
+ _keypath_set.908Tm
+ _keypath_set.910Tm
+ _objc_msgSend$beginClassicInvertColorsRequestWithValue:
+ _objc_msgSend$beginSmartInvertColorsRequestWithValue:
+ _objc_msgSend$chatterboxEnabled
+ _objc_msgSend$classicInvertColorsEnabled
+ _objc_msgSend$commitClassicInvertColorsRequestIfCurrent:
+ _objc_msgSend$commitSmartInvertColorsRequestIfCurrent:
+ _objc_msgSend$initWithFeature:state:source:
+ _objc_msgSend$latestInvertColorsSettingsEventDictionaries
+ _objc_msgSend$latestInvertColorsSettingsEvents
+ _objc_msgSend$registerInvertColorsSettingsEvent:
+ _objc_msgSend$registerInvertColorsSettingsEventWithFeature:state:source:
+ _objc_msgSend$setChatterboxEnabled:
+ _objc_msgSend$setLatestInvertColorsSettingsEventDictionaries:
+ _objc_msgSend$setLatestInvertColorsSettingsEvents:
+ _objc_msgSend$smartInvertColorsEnabled
+ _objc_msgSend$toggleChatterbox
+ _symbolic _____ So10AXSettingsC22AccessibilityUtilitiesE10ChatterboxC
- -[AXServer setServerIdentifier:]
- GCC_except_table1005
- GCC_except_table1140
- GCC_except_table119
- GCC_except_table1248
- GCC_except_table131
- GCC_except_table133
- GCC_except_table1339
- GCC_except_table136
- GCC_except_table1362
- GCC_except_table1397
- GCC_except_table1442
- GCC_except_table1471
- GCC_except_table1534
- GCC_except_table1558
- GCC_except_table1562
- GCC_except_table1564
- GCC_except_table1567
- GCC_except_table157
- GCC_except_table1573
- GCC_except_table1663
- GCC_except_table1671
- GCC_except_table1678
- GCC_except_table1682
- GCC_except_table1689
- GCC_except_table1692
- GCC_except_table1701
- GCC_except_table1703
- GCC_except_table1837
- GCC_except_table1852
- GCC_except_table1873
- GCC_except_table1874
- GCC_except_table1875
- GCC_except_table1877
- GCC_except_table1878
- GCC_except_table1879
- GCC_except_table1880
- GCC_except_table2209
- GCC_except_table2212
- GCC_except_table2215
- GCC_except_table2217
- GCC_except_table2219
- GCC_except_table2221
- GCC_except_table2223
- GCC_except_table225
- GCC_except_table2311
- GCC_except_table2349
- GCC_except_table2416
- GCC_except_table2425
- GCC_except_table2454
- GCC_except_table249
- GCC_except_table2490
- GCC_except_table2499
- GCC_except_table2514
- GCC_except_table2541
- GCC_except_table2682
- GCC_except_table2741
- GCC_except_table2762
- GCC_except_table291
- GCC_except_table2916
- GCC_except_table2986
- GCC_except_table2997
- GCC_except_table2999
- GCC_except_table3006
- GCC_except_table3120
- GCC_except_table3132
- GCC_except_table3464
- GCC_except_table3468
- GCC_except_table3497
- GCC_except_table3501
- GCC_except_table3610
- GCC_except_table3623
- GCC_except_table3633
- GCC_except_table3738
- GCC_except_table3743
- GCC_except_table3829
- GCC_except_table407
- GCC_except_table4323
- GCC_except_table4331
- GCC_except_table4332
- GCC_except_table4340
- GCC_except_table4341
- GCC_except_table4349
- GCC_except_table4353
- GCC_except_table4355
- GCC_except_table4462
- GCC_except_table4475
- GCC_except_table4688
- GCC_except_table4692
- GCC_except_table4697
- GCC_except_table4719
- GCC_except_table4891
- GCC_except_table4968
- GCC_except_table4987
- GCC_except_table655
- GCC_except_table662
- GCC_except_table665
- GCC_except_table667
- GCC_except_table696
- GCC_except_table725
- GCC_except_table742
- GCC_except_table805
- GCC_except_table811
- GCC_except_table815
- GCC_except_table864
- GCC_except_table927
- GCC_except_table976
- GCC_except_table988
- GCC_except_table992
- ___block_descriptor_32_e34_v24?0"NSDictionary"8"NSError"16l
- ___block_descriptor_33_e34_v24?0"NSDictionary"8"NSError"16l
- ___swift_closure_destructor.1041Tm
- _keypath_get.707Tm
- _keypath_get.723Tm
- _keypath_get.783Tm
- _keypath_get.971Tm
- _keypath_set.904Tm
- _keypath_set.906Tm
- _serverIdentifier.count
CStrings:
+ "$cobaltTextScale"
+ "$debugRotorEnabled"
+ "$liveTypingEnabled"
+ "$showKeyboardInput"
+ "@16@?0@\"AXInvertColorsSettingsEvent\"8"
+ "AA: StartFlow - Attempt-to-enter-ClarityBoard message acknowledged with no error (client: %@)."
+ "AA: StartFlow - Attempting to enter ClarityBoard via Triple-Click/Accessibility Shortcut."
+ "AA: StartFlow - Error attempting to enter ClarityBoard: %@ (client: %@)"
+ "AA: StartFlow - Sending attempt-to-enter-ClarityBoard message with client identifier: %@"
+ "AXWallpaperDescriptions-V64"
+ "AXWallpaperDescriptions-V68"
+ "AccessibilityShortcut"
+ "Chatterbox"
+ "ChatterboxCobaltTextScale"
+ "ChatterboxEnabled"
+ "ChatterboxLiveTypingEnabled"
+ "ChatterboxShowKeyboardInput"
+ "ChatterboxSpeakOnSend"
+ "ClassicInvert"
+ "InvertColorsSettingsEvents"
+ "SmartInvert"
+ "SpringBoardPopFramework.axbundle"
+ "Unable to format non-finite duration"
+ "VoiceOverDebugRotorEnabled"
+ "v68"
+ "v6x"
- "Error attempting to enter ClarityBoard: %@"
- "SpringBoardPopAccessibility.axbundle"
- "com.apple.accessibility.AccessibilityReader"
```
