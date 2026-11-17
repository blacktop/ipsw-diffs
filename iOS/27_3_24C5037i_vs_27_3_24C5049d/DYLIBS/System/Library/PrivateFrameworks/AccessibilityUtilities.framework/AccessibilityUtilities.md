## AccessibilityUtilities

> `/System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities`

```diff

-3245.8.14.0.0
-  __TEXT.__text: 0x211ca4
-  __TEXT.__objc_methlist: 0x10304
-  __TEXT.__dlopen_cstrs: 0xbe5
-  __TEXT.__const: 0x9190
+3245.8.23.0.0
+  __TEXT.__text: 0x217ff8
+  __TEXT.__objc_methlist: 0x1050c
+  __TEXT.__dlopen_cstrs: 0xc43
+  __TEXT.__const: 0x9310
   __TEXT.__swift5_typeref: 0x27e2
-  __TEXT.__swift5_capture: 0x2b08
-  __TEXT.__cstring: 0x1e63a
-  __TEXT.__constg_swiftt: 0x1868
-  __TEXT.__swift5_reflstr: 0xbb5c
-  __TEXT.__swift5_fieldmd: 0x46dc
+  __TEXT.__swift5_capture: 0x2ba8
+  __TEXT.__cstring: 0x1eb96
+  __TEXT.__constg_swiftt: 0x1880
+  __TEXT.__swift5_reflstr: 0xbfbc
+  __TEXT.__swift5_fieldmd: 0x47e4
   __TEXT.__swift5_builtin: 0x604
   __TEXT.__swift5_assocty: 0x990
   __TEXT.__swift5_proto: 0x5f4

   __TEXT.__swift_as_entry: 0x12c
   __TEXT.__swift_as_ret: 0x178
   __TEXT.__swift_as_cont: 0x1e4
-  __TEXT.__oslogstring: 0x74e7
+  __TEXT.__oslogstring: 0x76c6
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__gcc_except_tab: 0x13d0
+  __TEXT.__gcc_except_tab: 0x13f4
   __TEXT.__ustring: 0x18c
-  __TEXT.__unwind_info: 0xc850
-  __TEXT.__eh_frame: 0x7fe0
+  __TEXT.__unwind_info: 0xcad8
+  __TEXT.__eh_frame: 0x81a0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5cc8
-  __DATA_CONST.__objc_classlist: 0x4f0
+  __DATA_CONST.__const: 0x5de0
+  __DATA_CONST.__objc_classlist: 0x4f8
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa598
+  __DATA_CONST.__objc_selrefs: 0xa6f0
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0x310
+  __DATA_CONST.__objc_superrefs: 0x318
   __DATA_CONST.__objc_arraydata: 0xad8
-  __DATA_CONST.__got: 0x24f8
-  __AUTH_CONST.__const: 0xa920
-  __AUTH_CONST.__cfstring: 0x14280
-  __AUTH_CONST.__objc_const: 0x1cc50
-  __AUTH_CONST.__objc_intobj: 0x17e8
-  __AUTH_CONST.__objc_arrayobj: 0x378
+  __DATA_CONST.__got: 0x2500
+  __AUTH_CONST.__const: 0xaaa8
+  __AUTH_CONST.__cfstring: 0x144a0
+  __AUTH_CONST.__objc_const: 0x1d0b8
+  __AUTH_CONST.__objc_intobj: 0x1800
+  __AUTH_CONST.__objc_arrayobj: 0x360
   __AUTH_CONST.__objc_dictobj: 0x348
   __AUTH_CONST.__objc_doubleobj: 0x70
-  __AUTH_CONST.__auth_got: 0x3008
-  __AUTH.__objc_data: 0x2ae8
-  __AUTH.__data: 0xb98
-  __DATA.__objc_ivar: 0xc40
-  __DATA.__data: 0x5398
+  __AUTH_CONST.__auth_got: 0x3018
+  __AUTH.__objc_data: 0x2b38
+  __AUTH.__data: 0xbc8
+  __DATA.__objc_ivar: 0xc4c
+  __DATA.__data: 0x5448
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x32b0
+  __DATA_DIRTY.__objc_data: 0x3340
   __DATA_DIRTY.__data: 0x898
   __DATA_DIRTY.__bss: 0x3850
   __DATA_DIRTY.__common: 0x20

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 15769
-  Symbols:   11222
-  CStrings:  4556
+  Functions: 15945
+  Symbols:   11282
+  CStrings:  4603
 
Symbols:
+ +[AXTripleClickHelpers _enabledTypingFeedbackOptions]
+ +[AXTripleClickHelpers _setEnabledTypingFeedbackOptions:]
+ +[AXTripleClickHelpers toggleTypingFeedback]
+ -[AXBackBoardServer _hardwareKeyboardAttachmentReasonsDidReset]
+ -[AXBackBoardServer _registerForHardwareKeyboardAttachmentReasonsReset]
+ -[AXBackBoardServer _sendHardwareKeyboardAttachmentReason:active:]
+ -[AXBackBoardServer setHardwareKeyboardAttachmentReason:active:]
+ -[AXBackBoardServer setHitTestOverrideFrame:contextId:displayId:]
+ -[AXHardwareKeyboardAttachmentState .cxx_destruct]
+ -[AXHardwareKeyboardAttachmentState _actionForReasonsChangeFrom:]
+ -[AXHardwareKeyboardAttachmentState effectiveAttached]
+ -[AXHardwareKeyboardAttachmentState hasActiveReasons]
+ -[AXHardwareKeyboardAttachmentState init]
+ -[AXHardwareKeyboardAttachmentState realKeyboardPresenceDidChange:]
+ -[AXHardwareKeyboardAttachmentState realKeyboardPresent]
+ -[AXHardwareKeyboardAttachmentState reconcileWithSystemAttached:]
+ -[AXHardwareKeyboardAttachmentState removeReasonsForPID:]
+ -[AXHardwareKeyboardAttachmentState seedRealKeyboardPresent:]
+ -[AXHardwareKeyboardAttachmentState setReason:active:forPID:]
+ -[AXHardwareKeyboardAttachmentState stateDescription]
+ -[AXSpringBoardServer _setReachabilityActive:direction:]
+ -[AXSpringBoardServer arrangementScreenRegionForHomeGestureAtLocationX:]
+ -[AXSpringBoardServer showArrangementDestination:inScreenRegion:]
+ -[AXSpringBoardServer toggleReachabilityInDirection:]
+ GCC_except_table1014
+ GCC_except_table1026
+ GCC_except_table1030
+ GCC_except_table1043
+ GCC_except_table1057
+ GCC_except_table1180
+ GCC_except_table123
+ GCC_except_table129
+ GCC_except_table1309
+ GCC_except_table1400
+ GCC_except_table141
+ GCC_except_table1423
+ GCC_except_table1458
+ GCC_except_table146
+ GCC_except_table1509
+ GCC_except_table1545
+ GCC_except_table160
+ GCC_except_table1608
+ GCC_except_table1632
+ GCC_except_table1636
+ GCC_except_table1638
+ GCC_except_table1641
+ GCC_except_table1647
+ GCC_except_table1656
+ GCC_except_table169
+ GCC_except_table1754
+ GCC_except_table176
+ GCC_except_table1761
+ GCC_except_table1765
+ GCC_except_table1772
+ GCC_except_table1775
+ GCC_except_table1777
+ GCC_except_table1781
+ GCC_except_table1784
+ GCC_except_table1786
+ GCC_except_table1926
+ GCC_except_table1941
+ GCC_except_table1962
+ GCC_except_table1963
+ GCC_except_table1964
+ GCC_except_table1966
+ GCC_except_table1967
+ GCC_except_table1968
+ GCC_except_table1969
+ GCC_except_table2307
+ GCC_except_table2310
+ GCC_except_table2313
+ GCC_except_table2315
+ GCC_except_table2317
+ GCC_except_table2319
+ GCC_except_table2321
+ GCC_except_table2409
+ GCC_except_table244
+ GCC_except_table2447
+ GCC_except_table2517
+ GCC_except_table2526
+ GCC_except_table2555
+ GCC_except_table2591
+ GCC_except_table2600
+ GCC_except_table2616
+ GCC_except_table2643
+ GCC_except_table2648
+ GCC_except_table268
+ GCC_except_table2788
+ GCC_except_table2847
+ GCC_except_table2868
+ GCC_except_table3022
+ GCC_except_table3092
+ GCC_except_table3103
+ GCC_except_table3105
+ GCC_except_table311
+ GCC_except_table3112
+ GCC_except_table3226
+ GCC_except_table3238
+ GCC_except_table3589
+ GCC_except_table3593
+ GCC_except_table3622
+ GCC_except_table3626
+ GCC_except_table3739
+ GCC_except_table3752
+ GCC_except_table3763
+ GCC_except_table3868
+ GCC_except_table3873
+ GCC_except_table3960
+ GCC_except_table434
+ GCC_except_table4482
+ GCC_except_table4490
+ GCC_except_table4491
+ GCC_except_table4499
+ GCC_except_table4500
+ GCC_except_table4508
+ GCC_except_table4512
+ GCC_except_table4514
+ GCC_except_table4621
+ GCC_except_table4634
+ GCC_except_table4847
+ GCC_except_table4851
+ GCC_except_table4856
+ GCC_except_table4878
+ GCC_except_table5050
+ GCC_except_table5084
+ GCC_except_table5131
+ GCC_except_table5150
+ GCC_except_table700
+ GCC_except_table703
+ GCC_except_table705
+ GCC_except_table736
+ GCC_except_table764
+ GCC_except_table781
+ GCC_except_table844
+ GCC_except_table850
+ GCC_except_table854
+ GCC_except_table903
+ GCC_except_table966
+ _AXAssistiveTouchIconTypeTypingFeedback
+ _AXDeviceHasSideTouchIDButton
+ _AXDeviceHasSideTouchIDButton.hasSideTouchIDButton
+ _AXDeviceHasSideTouchIDButton.onceToken
+ _AXDeviceIsConfirmWithEnrolled
+ _AXDeviceSiriUsesIntelligenceMode
+ _AXHardwareKeyboardAttachmentActionDescription
+ _AXHardwareKeyboardAttachmentReasonDescription
+ _AXHardwareKeyboardAttachmentReasonsResetNotification
+ _AXSpringBoardAlertDataDisableSwitchControlOnConfirm
+ _ActiveHardwareKeyboardAttachmentReasons
+ _OBJC_CLASS_$_AXHardwareKeyboardAttachmentState
+ _OBJC_IVAR_$_AXHardwareKeyboardAttachmentState._hasObservedRealKeyboardChange
+ _OBJC_IVAR_$_AXHardwareKeyboardAttachmentState._realKeyboardPresent
+ _OBJC_IVAR_$_AXHardwareKeyboardAttachmentState._reasonsByPID
+ _OBJC_METACLASS_$_AXHardwareKeyboardAttachmentState
+ _SiriAvailabilityLibraryCore.frameworkLibrary
+ __OBJC_$_INSTANCE_METHODS_AXHardwareKeyboardAttachmentState
+ __OBJC_$_INSTANCE_VARIABLES_AXHardwareKeyboardAttachmentState
+ __OBJC_$_PROP_LIST_AXHardwareKeyboardAttachmentState
+ __OBJC_CLASS_RO_$_AXHardwareKeyboardAttachmentState
+ __OBJC_METACLASS_RO_$_AXHardwareKeyboardAttachmentState
+ ___64-[AXBackBoardServer setHardwareKeyboardAttachmentReason:active:]_block_invoke
+ ___71-[AXBackBoardServer _registerForHardwareKeyboardAttachmentReasonsReset]_block_invoke
+ ___71-[AXBackBoardServer _registerForHardwareKeyboardAttachmentReasonsReset]_block_invoke_2
+ ___AXDeviceHasSideTouchIDButton_block_invoke
+ ___SiriAvailabilityLibraryCore_block_invoke
+ ___block_descriptor_40_e8_32s_e8_v12?0i8ls32l8
+ ___getSOFetchSiriAvailabilitySymbolLoc_block_invoke
+ ___swift_closure_destructor.1094Tm
+ ___swift_closure_destructor.144Tm
+ ___swift_closure_destructor.150Tm
+ ___swift_closure_destructor.164Tm
+ ___swift_closure_destructor.168Tm
+ ___swift_closure_destructor.717Tm
+ __registerForHardwareKeyboardAttachmentReasonsReset.onceToken
+ _audit_stringSiriAvailability
+ _getSOFetchSiriAvailabilitySymbolLoc.ptr
+ _keypath_get.1022Tm
+ _keypath_get.460Tm
+ _keypath_get.500Tm
+ _keypath_get.524Tm
+ _keypath_get.628Tm
+ _keypath_get.742Tm
+ _keypath_get.758Tm
+ _keypath_get.818Tm
+ _keypath_get_selector_assistiveTouchMouseDwellControlKeyboardKeyActivationTimeoutEnabled
+ _keypath_get_selector_speechControllerColor
+ _keypath_get_selector_speechControllerSizeScale
+ _keypath_set.679Tm
+ _keypath_set.949Tm
+ _keypath_set.951Tm
- GCC_except_table1007
- GCC_except_table1019
- GCC_except_table1023
- GCC_except_table1036
- GCC_except_table1050
- GCC_except_table1172
- GCC_except_table120
- GCC_except_table126
- GCC_except_table1280
- GCC_except_table1371
- GCC_except_table138
- GCC_except_table1394
- GCC_except_table140
- GCC_except_table1429
- GCC_except_table1480
- GCC_except_table1516
- GCC_except_table154
- GCC_except_table1579
- GCC_except_table1603
- GCC_except_table1607
- GCC_except_table1609
- GCC_except_table1612
- GCC_except_table1618
- GCC_except_table1627
- GCC_except_table166
- GCC_except_table1717
- GCC_except_table1725
- GCC_except_table173
- GCC_except_table1732
- GCC_except_table1736
- GCC_except_table1743
- GCC_except_table1748
- GCC_except_table1752
- GCC_except_table1755
- GCC_except_table1757
- GCC_except_table1897
- GCC_except_table1912
- GCC_except_table1933
- GCC_except_table1934
- GCC_except_table1935
- GCC_except_table1937
- GCC_except_table1938
- GCC_except_table1939
- GCC_except_table1940
- GCC_except_table2278
- GCC_except_table2281
- GCC_except_table2284
- GCC_except_table2286
- GCC_except_table2288
- GCC_except_table2290
- GCC_except_table2292
- GCC_except_table2380
- GCC_except_table241
- GCC_except_table2418
- GCC_except_table2486
- GCC_except_table2495
- GCC_except_table2524
- GCC_except_table2560
- GCC_except_table2569
- GCC_except_table2584
- GCC_except_table2611
- GCC_except_table265
- GCC_except_table2753
- GCC_except_table2812
- GCC_except_table2833
- GCC_except_table2987
- GCC_except_table3057
- GCC_except_table3068
- GCC_except_table3070
- GCC_except_table3077
- GCC_except_table308
- GCC_except_table3191
- GCC_except_table3203
- GCC_except_table3554
- GCC_except_table3558
- GCC_except_table3587
- GCC_except_table3591
- GCC_except_table3704
- GCC_except_table3717
- GCC_except_table3728
- GCC_except_table3833
- GCC_except_table3838
- GCC_except_table3925
- GCC_except_table431
- GCC_except_table4447
- GCC_except_table4455
- GCC_except_table4456
- GCC_except_table4464
- GCC_except_table4465
- GCC_except_table4473
- GCC_except_table4477
- GCC_except_table4479
- GCC_except_table4586
- GCC_except_table4599
- GCC_except_table4812
- GCC_except_table4816
- GCC_except_table4821
- GCC_except_table4843
- GCC_except_table5015
- GCC_except_table5049
- GCC_except_table5096
- GCC_except_table5115
- GCC_except_table686
- GCC_except_table696
- GCC_except_table698
- GCC_except_table729
- GCC_except_table757
- GCC_except_table774
- GCC_except_table837
- GCC_except_table843
- GCC_except_table847
- GCC_except_table896
- GCC_except_table959
- ___swift_closure_destructor.1064Tm
- ___swift_closure_destructor.137Tm
- ___swift_closure_destructor.143Tm
- ___swift_closure_destructor.157Tm
- ___swift_closure_destructor.161Tm
- ___swift_closure_destructor.711Tm
- _keypath_get.456Tm
- _keypath_get.496Tm
- _keypath_get.520Tm
- _keypath_get.622Tm
- _keypath_get.722Tm
- _keypath_get.738Tm
- _keypath_get.798Tm
- _keypath_get.994Tm
- _keypath_set.673Tm
- _keypath_set.923Tm
- _keypath_set.925Tm
CStrings:
+ "$brailleAlwaysShowsTextFieldLabels"
+ "$mouseDwellControlKeyboardKeyActivationTimeoutEnabled"
+ "$speaksDuringSiri"
+ "$speechControllerColor"
+ "$speechControllerSizeScale"
+ "$touchBrailleGesturesDidLockOnMainDisplay"
+ "$touchBrailleGesturesSecondaryDisplayLockedOrientation"
+ "$touchBrailleGesturesSecondaryDisplayLockedTypingMode"
+ "$typingFeedbackShortcutSavedOptions"
+ "%@(pid %@)"
+ "AXAssistiveTouchIconTypeTypingFeedback"
+ "AXKEYBOARD: client: backboardd reset reasons, resending %lu"
+ "AXKEYBOARD: client: backboardd unreachable after reset"
+ "AXKEYBOARD: client: backboardd unreachable; active reasons will be resent when it is ready"
+ "AXKEYBOARD: client: reason %{public}@ active=%d"
+ "AXSTypingFeedbackShortcutSavedOptions"
+ "AXSVoiceOverSpeaksDuringSiri"
+ "AXSpringBoardAlertDataDisableSwitchControlOnConfirm"
+ "AssistiveTouchMouseDwellControlKeyboardKeyActivationTimeoutEnabledPreference"
+ "Disable Switch Control alert answered: %ld"
+ "SOFetchSiriAvailability"
+ "SOSiriAvailability *soft_SOFetchSiriAvailability(void)"
+ "Skipping connected peripheral without allowed service: %@"
+ "SpeechControllerColor"
+ "SpeechControllerSizeScale"
+ "Typing Feedback turned off from shortcut, saved options: %ld"
+ "Typing Feedback turned on from shortcut, restored options: %ld"
+ "Unknown(%ld)"
+ "VoiceOverBraille"
+ "VoiceOverBrailleAlwaysShowsTextFieldLabels"
+ "VoiceOverBrailleGesturesDidLockOnMainDisplay"
+ "VoiceOverBrailleGesturesSecondaryDisplayLockedOrientation"
+ "VoiceOverBrailleGesturesSecondaryDisplayLockedTypingMode"
+ "ask.sheet.option.typing.feedback"
+ "character.cursor.ibeam"
+ "com.apple.accessibility.backboard.hardware-keyboard-reasons-reset"
+ "destination"
+ "direction"
+ "locationX"
+ "none"
+ "real=%d reasons=[%@] effective=%d"
+ "screenRegion"
+ "set attached"
+ "set detached"
+ "softlink:o:path:/System/Library/PrivateFrameworks/SiriAvailability.framework/SiriAvailability"
+ "venice"
+ "void *SiriAvailabilityLibrary(void)"
```
