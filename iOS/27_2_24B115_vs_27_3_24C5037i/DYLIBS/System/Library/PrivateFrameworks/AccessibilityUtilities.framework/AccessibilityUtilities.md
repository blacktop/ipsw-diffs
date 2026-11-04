## AccessibilityUtilities

> `/System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities`

```diff

-3245.8.9.0.0
-  __TEXT.__text: 0x2068b4
-  __TEXT.__objc_methlist: 0x1017c
-  __TEXT.__dlopen_cstrs: 0xb89
-  __TEXT.__const: 0x8e58
-  __TEXT.__swift5_typeref: 0x272c
-  __TEXT.__swift5_capture: 0x2a64
-  __TEXT.__cstring: 0x1e377
-  __TEXT.__constg_swiftt: 0x1760
-  __TEXT.__swift5_reflstr: 0xb7cc
-  __TEXT.__swift5_fieldmd: 0x4500
-  __TEXT.__swift5_builtin: 0x5dc
-  __TEXT.__swift5_assocty: 0x978
-  __TEXT.__swift5_proto: 0x5ec
-  __TEXT.__swift5_types: 0x244
-  __TEXT.__swift_as_entry: 0x110
-  __TEXT.__swift_as_ret: 0x158
-  __TEXT.__swift_as_cont: 0x1a0
-  __TEXT.__oslogstring: 0x710a
+3245.8.14.0.0
+  __TEXT.__text: 0x211ca4
+  __TEXT.__objc_methlist: 0x10304
+  __TEXT.__dlopen_cstrs: 0xbe5
+  __TEXT.__const: 0x9190
+  __TEXT.__swift5_typeref: 0x27e2
+  __TEXT.__swift5_capture: 0x2b08
+  __TEXT.__cstring: 0x1e63a
+  __TEXT.__constg_swiftt: 0x1868
+  __TEXT.__swift5_reflstr: 0xbb5c
+  __TEXT.__swift5_fieldmd: 0x46dc
+  __TEXT.__swift5_builtin: 0x604
+  __TEXT.__swift5_assocty: 0x990
+  __TEXT.__swift5_proto: 0x5f4
+  __TEXT.__swift5_types: 0x25c
+  __TEXT.__swift_as_entry: 0x12c
+  __TEXT.__swift_as_ret: 0x178
+  __TEXT.__swift_as_cont: 0x1e4
+  __TEXT.__oslogstring: 0x74e7
+  __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__gcc_except_tab: 0x13b8
+  __TEXT.__gcc_except_tab: 0x13d0
   __TEXT.__ustring: 0x18c
-  __TEXT.__unwind_info: 0xc4c0
-  __TEXT.__eh_frame: 0x7ac0
+  __TEXT.__unwind_info: 0xc850
+  __TEXT.__eh_frame: 0x7fe0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5bf0
-  __DATA_CONST.__objc_classlist: 0x4d8
+  __DATA_CONST.__const: 0x5cc8
+  __DATA_CONST.__objc_classlist: 0x4f0
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa4d8
+  __DATA_CONST.__objc_selrefs: 0xa598
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0x308
+  __DATA_CONST.__objc_superrefs: 0x310
   __DATA_CONST.__objc_arraydata: 0xad8
-  __DATA_CONST.__got: 0x2428
-  __AUTH_CONST.__const: 0xa638
-  __AUTH_CONST.__cfstring: 0x141c0
-  __AUTH_CONST.__objc_const: 0x1c750
+  __DATA_CONST.__got: 0x24f8
+  __AUTH_CONST.__const: 0xa920
+  __AUTH_CONST.__cfstring: 0x14280
+  __AUTH_CONST.__objc_const: 0x1cc50
   __AUTH_CONST.__objc_intobj: 0x17e8
   __AUTH_CONST.__objc_arrayobj: 0x378
   __AUTH_CONST.__objc_dictobj: 0x348
   __AUTH_CONST.__objc_doubleobj: 0x70
-  __AUTH_CONST.__auth_got: 0x2e50
-  __AUTH.__objc_data: 0x2a98
-  __AUTH.__data: 0x9a8
-  __DATA.__objc_ivar: 0xc38
-  __DATA.__data: 0x5278
-  __DATA_DIRTY.__objc_data: 0x3250
+  __AUTH_CONST.__auth_got: 0x3008
+  __AUTH.__objc_data: 0x2ae8
+  __AUTH.__data: 0xb98
+  __DATA.__objc_ivar: 0xc40
+  __DATA.__data: 0x5398
+  __DATA.__common: 0x8
+  __DATA_DIRTY.__objc_data: 0x32b0
   __DATA_DIRTY.__data: 0x898
   __DATA_DIRTY.__bss: 0x3850
   __DATA_DIRTY.__common: 0x20

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 15535
-  Symbols:   11155
-  CStrings:  4520
+  Functions: 15769
+  Symbols:   11222
+  CStrings:  4556
 
Symbols:
+ +[AXDiagnosticBrokerConnection sharedInstance]
+ -[AXDiagnosticBrokerConnection .cxx_destruct]
+ -[AXDiagnosticBrokerConnection _init]
+ -[AXDiagnosticBrokerConnection connectionWithServiceWasInterruptedForUserInterfaceClient:]
+ -[AXDiagnosticBrokerConnection sendMessage:withIdentifier:completion:]
+ -[AXDiagnosticBrokerConnection serverClient]
+ -[AXNamedReplayableGesture copyWithZone:]
+ -[AXPageTurningReplayableGesture copyWithZone:]
+ -[AXReplayableGesture copyWithZone:]
+ -[AXSettings(LegacyImplementation) setVoiceOverShortcutsRotorItems:]
+ -[AXSettings(LegacyImplementation) voiceOverShortcutsRotorEnabled]
+ -[AXSettings(LegacyImplementation) voiceOverShortcutsRotorItems]
+ -[AXSiriShortcutsManager voiceOverShortcutsRotorEnabledShortcuts]
+ -[AXSiriShortcutsManager voiceOverShortcutsRotorItems]
+ -[AXSpringBoardServer volumeLevelWithCompletion:]
+ -[AXVoiceOverServer captureDiagnosticStateIntoSnapshotDirectory:completion:]
+ -[AXVoiceOverServer fileQuickRadarWithCompletion:]
+ -[AXVoiceOverServer fileQuickRadarWithOutputDirectory:completion:]
+ GCC_except_table1007
+ GCC_except_table1019
+ GCC_except_table1023
+ GCC_except_table1036
+ GCC_except_table1050
+ GCC_except_table107
+ GCC_except_table1172
+ GCC_except_table120
+ GCC_except_table126
+ GCC_except_table1280
+ GCC_except_table1371
+ GCC_except_table138
+ GCC_except_table1394
+ GCC_except_table1429
+ GCC_except_table143
+ GCC_except_table154
+ GCC_except_table157
+ GCC_except_table1627
+ GCC_except_table166
+ GCC_except_table1717
+ GCC_except_table1725
+ GCC_except_table173
+ GCC_except_table1732
+ GCC_except_table1736
+ GCC_except_table1752
+ GCC_except_table1755
+ GCC_except_table1757
+ GCC_except_table1912
+ GCC_except_table1933
+ GCC_except_table1934
+ GCC_except_table1935
+ GCC_except_table1937
+ GCC_except_table1938
+ GCC_except_table1939
+ GCC_except_table1940
+ GCC_except_table2278
+ GCC_except_table2281
+ GCC_except_table2284
+ GCC_except_table2286
+ GCC_except_table2288
+ GCC_except_table2290
+ GCC_except_table2292
+ GCC_except_table2380
+ GCC_except_table241
+ GCC_except_table2418
+ GCC_except_table2486
+ GCC_except_table2495
+ GCC_except_table2524
+ GCC_except_table2560
+ GCC_except_table2569
+ GCC_except_table2584
+ GCC_except_table2611
+ GCC_except_table265
+ GCC_except_table2753
+ GCC_except_table2812
+ GCC_except_table2833
+ GCC_except_table2987
+ GCC_except_table3057
+ GCC_except_table3068
+ GCC_except_table3070
+ GCC_except_table3077
+ GCC_except_table308
+ GCC_except_table3191
+ GCC_except_table3203
+ GCC_except_table3554
+ GCC_except_table3558
+ GCC_except_table3587
+ GCC_except_table3591
+ GCC_except_table3704
+ GCC_except_table3717
+ GCC_except_table3728
+ GCC_except_table3833
+ GCC_except_table3838
+ GCC_except_table3925
+ GCC_except_table431
+ GCC_except_table4447
+ GCC_except_table4456
+ GCC_except_table4464
+ GCC_except_table4465
+ GCC_except_table4473
+ GCC_except_table4477
+ GCC_except_table4479
+ GCC_except_table4586
+ GCC_except_table4599
+ GCC_except_table4812
+ GCC_except_table4816
+ GCC_except_table4843
+ GCC_except_table5015
+ GCC_except_table5049
+ GCC_except_table5096
+ GCC_except_table5115
+ GCC_except_table53
+ GCC_except_table68
+ GCC_except_table686
+ GCC_except_table693
+ GCC_except_table696
+ GCC_except_table757
+ GCC_except_table774
+ GCC_except_table837
+ GCC_except_table843
+ GCC_except_table847
+ GCC_except_table896
+ GCC_except_table90
+ GCC_except_table95
+ GCC_except_table959
+ _AXDiagnosticFileDraftEntitlement
+ _AXLogDiagnostics
+ _AXRecognitionActionForActionButtonSetting
+ _AXSpringBoardActionKeyVolumeLevel
+ _AXVoiceOverShortcutsRotorItemsForShortcutNames
+ _HardwareButtonKeySuffix
+ _OBJC_CLASS_$_AXDiagnosticBrokerConnection
+ _OBJC_CLASS_$_NSISO8601DateFormatter
+ _OBJC_IVAR_$_AXDiagnosticBrokerConnection._lock
+ _OBJC_IVAR_$_AXDiagnosticBrokerConnection._serverClient
+ _OBJC_METACLASS_$_AXDiagnosticBrokerConnection
+ __DATA__TtC22AccessibilityUtilitiesP33_AD7F0F39DEA978E92C2A1C6C92850B3B10MessageBox
+ __DATA__TtC22AccessibilityUtilitiesP33_AD7F0F39DEA978E92C2A1C6C92850B3B11CaptureGate
+ __IVARS__TtC22AccessibilityUtilitiesP33_AD7F0F39DEA978E92C2A1C6C92850B3B10MessageBox
+ __IVARS__TtC22AccessibilityUtilitiesP33_AD7F0F39DEA978E92C2A1C6C92850B3B11CaptureGate
+ __METACLASS_DATA__TtC22AccessibilityUtilitiesP33_AD7F0F39DEA978E92C2A1C6C92850B3B10MessageBox
+ __METACLASS_DATA__TtC22AccessibilityUtilitiesP33_AD7F0F39DEA978E92C2A1C6C92850B3B11CaptureGate
+ __OBJC_$_CLASS_METHODS_AXDiagnosticBrokerConnection
+ __OBJC_$_CLASS_METHODS_AXSSAccessibilityActionStorage(AccessibilityUtilities|AccessibilityUtilities1)
+ __OBJC_$_INSTANCE_METHODS_AXDiagnosticBrokerConnection
+ __OBJC_$_INSTANCE_METHODS_AXSSAccessibilityActionStorage(AccessibilityUtilities|AccessibilityUtilities1)
+ __OBJC_$_INSTANCE_VARIABLES_AXDiagnosticBrokerConnection
+ __OBJC_$_PROP_LIST_AXDiagnosticBrokerConnection
+ __OBJC_CLASS_PROTOCOLS_$_AXDiagnosticBrokerConnection
+ __OBJC_CLASS_RO_$_AXDiagnosticBrokerConnection
+ __OBJC_METACLASS_RO_$_AXDiagnosticBrokerConnection
+ ___46+[AXDiagnosticBrokerConnection sharedInstance]_block_invoke
+ ___49-[AXSpringBoardServer volumeLevelWithCompletion:]_block_invoke
+ ___50-[AXVoiceOverServer fileQuickRadarWithCompletion:]_block_invoke
+ ___66-[AXVoiceOverServer fileQuickRadarWithOutputDirectory:completion:]_block_invoke
+ ___76-[AXVoiceOverServer captureDiagnosticStateIntoSnapshotDirectory:completion:]_block_invoke
+ ___AXVoiceOverShortcutsRotorItemsForShortcutNames_block_invoke
+ ___block_descriptor_40_e8_32bs_e35_v24?0"NSString"8"NSDictionary"16ls32l8
+ ___block_descriptor_40_e8_32s_e31_q24?0"NSString"8"NSString"16ls32l8
+ ___swift_closure_destructor.1064Tm
+ ___swift_closure_destructor.137Tm
+ ___swift_closure_destructor.143Tm
+ ___swift_closure_destructor.157Tm
+ ___swift_closure_destructor.161Tm
+ ___swift_closure_destructor.39Tm
+ ___swift_closure_destructor.711Tm
+ ___swift_memcpy0_1
+ _get_enum_tag_for_layout_string 22AccessibilityUtilities24AXDiagnosticCaptureErrorO
+ _kAXSVoiceOverTouchRotorItemShortcuts
+ _keypath_get.456Tm
+ _keypath_get.496Tm
+ _keypath_get.520Tm
+ _keypath_get.622Tm
+ _keypath_get.722Tm
+ _keypath_get.738Tm
+ _keypath_get.798Tm
+ _keypath_get.994Tm
+ _keypath_set.673Tm
+ _keypath_set.923Tm
+ _keypath_set.925Tm
+ _swift_cvw_enumFn_getEnumTag
+ _symbolic Say_____G 15AXCoreUtilities26AXDiagnosticFeatureCaptureV
+ _symbolic ScCy___________pG 15AXCoreUtilities22AXDiagnosticDraftReplyV s5ErrorP
+ _symbolic ScCyyt______pG s5ErrorP
+ _symbolic So6NSLockC
+ _symbolic _____ 15AXCoreUtilities16AXDiagnosticModeO
+ _symbolic _____ 22AccessibilityUtilities10MessageBox33_AD7F0F39DEA978E92C2A1C6C92850B3BLLC
+ _symbolic _____ 22AccessibilityUtilities11CaptureGate33_AD7F0F39DEA978E92C2A1C6C92850B3BLLC
+ _symbolic _____ 22AccessibilityUtilities20AXDiagnosticCapturerV
+ _symbolic _____ 22AccessibilityUtilities24AXDiagnosticCaptureErrorO
+ _symbolic _____ 22AccessibilityUtilities32AXDiagnosticCaptureConfigurationV
+ _symbolic _____ So039AXSVoiceOverActionButtonItemRecognitionC0V
+ _symbolic _____Sg 15AXCoreUtilities21AXDiagnosticComponentV
+ _symbolic _____Sg 15AXCoreUtilities26AXDiagnosticClassificationO
+ _symbolic _____Sg 15AXCoreUtilities27AXDiagnosticReproducibilityO
+ _symbolic _____yS2SG s18_DictionaryStorageC
+ _symbolic _____y_____G 15AXCoreUtilities15AXSettingRecordC So039AXSVoiceOverActionButtonItemRecognitionG0V
+ _symbolic _____y_____G 15AXCoreUtilities27AXDiagnosticDeadlineOutcomeO AA0C10DraftReplyV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 15AXCoreUtilities25AXDiagnosticRemoteFeatureV
+ _symbolic _____y_____GSg 15AXCoreUtilities15AXSettingRecordC So039AXSVoiceOverActionButtonItemRecognitionG0V
+ _type_layout_string 22AccessibilityUtilities24AXDiagnosticCaptureErrorO
- +[AXTripleClickHelpers _loadAuxiliaryBundleIfNeeded]
- GCC_except_table1008
- GCC_except_table1020
- GCC_except_table1024
- GCC_except_table1037
- GCC_except_table1051
- GCC_except_table109
- GCC_except_table1173
- GCC_except_table122
- GCC_except_table128
- GCC_except_table1281
- GCC_except_table1372
- GCC_except_table1395
- GCC_except_table142
- GCC_except_table1430
- GCC_except_table145
- GCC_except_table156
- GCC_except_table159
- GCC_except_table168
- GCC_except_table1708
- GCC_except_table1716
- GCC_except_table1723
- GCC_except_table1727
- GCC_except_table1734
- GCC_except_table1737
- GCC_except_table1739
- GCC_except_table175
- GCC_except_table1882
- GCC_except_table1918
- GCC_except_table1919
- GCC_except_table1920
- GCC_except_table1922
- GCC_except_table1923
- GCC_except_table1924
- GCC_except_table1925
- GCC_except_table2263
- GCC_except_table2266
- GCC_except_table2269
- GCC_except_table2271
- GCC_except_table2273
- GCC_except_table2275
- GCC_except_table2277
- GCC_except_table2365
- GCC_except_table2403
- GCC_except_table243
- GCC_except_table2470
- GCC_except_table2479
- GCC_except_table2508
- GCC_except_table2544
- GCC_except_table2553
- GCC_except_table2568
- GCC_except_table2595
- GCC_except_table267
- GCC_except_table2737
- GCC_except_table2796
- GCC_except_table2817
- GCC_except_table2971
- GCC_except_table3041
- GCC_except_table3052
- GCC_except_table3054
- GCC_except_table3061
- GCC_except_table310
- GCC_except_table3175
- GCC_except_table3187
- GCC_except_table3538
- GCC_except_table3542
- GCC_except_table3571
- GCC_except_table3575
- GCC_except_table3686
- GCC_except_table3699
- GCC_except_table3709
- GCC_except_table3814
- GCC_except_table3819
- GCC_except_table3906
- GCC_except_table433
- GCC_except_table4425
- GCC_except_table4433
- GCC_except_table4434
- GCC_except_table4442
- GCC_except_table4443
- GCC_except_table4451
- GCC_except_table4457
- GCC_except_table4564
- GCC_except_table4577
- GCC_except_table4790
- GCC_except_table4794
- GCC_except_table4799
- GCC_except_table4993
- GCC_except_table5027
- GCC_except_table5070
- GCC_except_table5089
- GCC_except_table55
- GCC_except_table688
- GCC_except_table695
- GCC_except_table70
- GCC_except_table700
- GCC_except_table758
- GCC_except_table775
- GCC_except_table838
- GCC_except_table844
- GCC_except_table848
- GCC_except_table897
- GCC_except_table92
- GCC_except_table960
- GCC_except_table97
- __AXSBPopArrangementTitle.onceToken
- __AXSBPopArrangementTitle.popBundle
- __AXSLoadAuxiliaryBundlesWithName
- __CATEGORY_CLASS_METHODS_AXSSAccessibilityActionStorage_$_AccessibilityUtilities
- __CATEGORY_CLASS_PROPERTIES_AXSSAccessibilityActionStorage_$_AccessibilityUtilities
- __CATEGORY_INSTANCE_METHODS_AXSSAccessibilityActionStorage_$_AccessibilityUtilities
- ___52+[AXTripleClickHelpers _loadAuxiliaryBundleIfNeeded]_block_invoke
- ____AXSBPopArrangementTitle_block_invoke
- ___swift_closure_destructor.1047Tm
- ___swift_closure_destructor.132Tm
- ___swift_closure_destructor.138Tm
- ___swift_closure_destructor.152Tm
- ___swift_closure_destructor.156Tm
- ___swift_closure_destructor.705Tm
- __loadAuxiliaryBundleIfNeeded.onceToken
- _keypath_get.452Tm
- _keypath_get.492Tm
- _keypath_get.516Tm
- _keypath_get.616Tm
- _keypath_get.711Tm
- _keypath_get.727Tm
- _keypath_get.787Tm
- _keypath_get.977Tm
- _keypath_set.667Tm
- _keypath_set.908Tm
- _keypath_set.910Tm
- _symbolic Say_____G 26AccessibilitySharedSupport0A12ShortcutInfoV
CStrings:
+ "\n\nTime of issue: "
+ "$actionButtonItemRecognitionAction"
+ "$brailleGesturesSingleHandActivationGestureEnabled"
+ "$mouseBubbleModeEnabled"
+ "$shareAcrossDisplays"
+ "$typingFeedbackOnlyWithHeadphonesEnabled"
+ "$watchShortcutsRotorEnabled"
+ "AXDiagnosticBrokerConnection.m"
+ "AXDiagnostics-%@-%@"
+ "AXDiagnosticsBroker"
+ "AXSAssistiveTouchMouseBubbleModeEnabled"
+ "AXSVoiceOverActionButtonItemRecognitionActionPreference"
+ "AXSVoiceOverTouchBrailleGesturesSingleHandActivationGestureEnabled"
+ "AXSpringBoardActionKeyVolumeLevel"
+ "AXWallpaperDescriptions-StandByInfra"
+ "Captured diagnostic snapshot %s for %s"
+ "Diagnostic capture refused: another capture is already in progress"
+ "Diagnostic capture refused: not an internal install"
+ "Diagnostic capture requested. initiator: %{public}s, mode: %{public}s, local features: %s"
+ "Diagnostic state request to VoiceOver failed: %@"
+ "Diagnostics broker did not reply in time"
+ "Diagnostics broker request failed: %@"
+ "Diagnostics request accepted for %s, local: %{bool}d"
+ "Failed to prune diagnostic snapshots: %@"
+ "Failed to remove unused diagnostic snapshot: %@"
+ "Identifier"
+ "Missing snapshot directory"
+ "NONE"
+ "Not adding preferred voice %s, it is already in the list"
+ "Quick radar request to VoiceOver failed: %@"
+ "Running scheduled cleanup after diagnostic snapshot %s"
+ "Scheduled diagnostic snapshot cleanup failed: %@"
+ "Sending diagnostics draft request to the broker. initiator: %{public}s, component: %{public}s, classification: %{public}s, reproducibility: %{public}s"
+ "TypingFeedbackOnlyWithHeadphonesEnabled"
+ "VoiceOver is not running"
+ "VoiceOverShortcutsRotorItems"
+ "VoiceOverWatchShortcutsRotorEnabled"
+ "ZoomShareAcrossDisplays"
+ "_ACTION_BUTTON"
+ "_ACTION_BUTTON_CAMERA_CONTROL"
+ "_CAMERA_CONTROL"
+ "com.apple.accessibility.diagnostics.file-draft"
+ "localCollectionParameters"
+ "outputDirectory"
+ "q24@?0@\"NSString\"8@\"NSString\"16"
+ "search.rotor.shortcuts"
+ "snapshotDirectory"
+ "v24@?0@\"NSString\"8@\"NSDictionary\"16"
- "ARRANGEMENT_DISMISS_LEFT_APP_FULL_WIDTH"
- "ARRANGEMENT_DISMISS_RIGHT_APP_FULL_WIDTH"
- "ARRANGEMENT_FULLSCREEN_LEFT_APP_FULL_WIDTH"
- "ARRANGEMENT_FULLSCREEN_RIGHT_APP_FULL_WIDTH"
- "ARRANGEMENT_PIN_PAIR_FULL_WIDTH"
- "ARRANGEMENT_SPLIT_APP_LEFT"
- "ARRANGEMENT_SPLIT_APP_RIGHT"
- "ARRANGEMENT_SWAP_FULL_WIDTH"
- "ARRANGEMENT_UNPIN_PAIR_FULL_WIDTH"
- "AccessibilityUtilities"
- "LocalizedStrings-AXAction"
- "SpringBoardPopFramework.axbundle"
```
