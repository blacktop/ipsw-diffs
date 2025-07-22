## AccessibilityUtilities

> `/System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities`

```diff

-3185.4.0.0.0
-  __TEXT.__text: 0x141bd4
-  __TEXT.__auth_stubs: 0x4bd0
-  __TEXT.__objc_methlist: 0xece4
-  __TEXT.__cstring: 0x19476
+3187.1.0.0.0
+  __TEXT.__text: 0x141308
+  __TEXT.__auth_stubs: 0x4b60
+  __TEXT.__objc_methlist: 0xeda4
+  __TEXT.__cstring: 0x19586
   __TEXT.__const: 0x3c64
   __TEXT.__gcc_except_tab: 0x12ec
-  __TEXT.__oslogstring: 0x5da9
+  __TEXT.__oslogstring: 0x5ed9
   __TEXT.__dlopen_cstrs: 0xba9
   __TEXT.__ustring: 0x68
-  __TEXT.__swift5_typeref: 0x1238
-  __TEXT.__swift5_capture: 0xcb8
-  __TEXT.__constg_swiftt: 0x9c8
-  __TEXT.__swift5_reflstr: 0x16fc
-  __TEXT.__swift5_fieldmd: 0xca8
+  __TEXT.__swift5_typeref: 0x116a
+  __TEXT.__swift5_capture: 0xbf8
+  __TEXT.__constg_swiftt: 0x9d0
+  __TEXT.__swift5_reflstr: 0x174c
+  __TEXT.__swift5_fieldmd: 0xcc0
   __TEXT.__swift5_builtin: 0x17c
   __TEXT.__swift5_assocty: 0x2b8
   __TEXT.__swift5_proto: 0x1fc
   __TEXT.__swift5_types: 0xc0
-  __TEXT.__swift_as_entry: 0x130
-  __TEXT.__swift_as_ret: 0x19c
-  __TEXT.__unwind_info: 0x5bd8
-  __TEXT.__eh_frame: 0x2a90
+  __TEXT.__swift_as_entry: 0x11c
+  __TEXT.__swift_as_ret: 0x188
+  __TEXT.__unwind_info: 0x5bc0
+  __TEXT.__eh_frame: 0x28c0
   __TEXT.__objc_classname: 0xd77
-  __TEXT.__objc_methname: 0x29317
-  __TEXT.__objc_methtype: 0x307c
-  __TEXT.__objc_stubs: 0x14e00
-  __DATA_CONST.__got: 0x1b78
-  __DATA_CONST.__const: 0x3960
+  __TEXT.__objc_methname: 0x295c5
+  __TEXT.__objc_methtype: 0x308d
+  __TEXT.__objc_stubs: 0x14fa0
+  __DATA_CONST.__got: 0x1b80
+  __DATA_CONST.__const: 0x3b40
   __DATA_CONST.__objc_classlist: 0x438
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x97a8
+  __DATA_CONST.__objc_selrefs: 0x9848
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x2f8
   __DATA_CONST.__objc_arraydata: 0x770
-  __AUTH_CONST.__auth_got: 0x25f8
-  __AUTH_CONST.__const: 0x4640
-  __AUTH_CONST.__cfstring: 0x14020
-  __AUTH_CONST.__objc_const: 0x12fa8
+  __AUTH_CONST.__auth_got: 0x25c0
+  __AUTH_CONST.__const: 0x4518
+  __AUTH_CONST.__cfstring: 0x14280
+  __AUTH_CONST.__objc_const: 0x13018
   __AUTH_CONST.__objc_intobj: 0x1428
   __AUTH_CONST.__objc_arrayobj: 0x210
   __AUTH_CONST.__objc_dictobj: 0x2d0
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH.__objc_data: 0x2680
-  __AUTH.__data: 0x790
+  __AUTH.__data: 0x7a0
   __DATA.__objc_ivar: 0xb50
-  __DATA.__data: 0x2178
-  __DATA.__bss: 0x3db0
+  __DATA.__data: 0x2188
+  __DATA.__bss: 0x3dc8
   __DATA.__common: 0x28
-  __DATA_DIRTY.__objc_data: 0xc40
+  __DATA_DIRTY.__objc_data: 0xc48
   __DATA_DIRTY.__data: 0x2f0
   __DATA_DIRTY.__bss: 0xd28
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 091D0B72-8C47-394D-9F32-CCD065338EDE
-  Functions: 9011
-  Symbols:   19618
-  CStrings:  13258
+  UUID: 4CE4ED62-B50F-3350-AC8A-FDF5361C2334
+  Functions: 9019
+  Symbols:   19682
+  CStrings:  13327
 
Symbols:
+ +[AXEventRepresentation setSwipeFromEdge:]
+ +[AXEventRepresentation swipeFromEdge]
+ -[AXAirPodSettingsManager _applySettingsForAddress:].cold.6
+ -[AXAirPodSettingsManager _retrieveSettingsForAddress:].cold.4
+ -[AXAirPodSettingsManager caseTonesVolumeForDeviceAddress:]
+ -[AXAirPodSettingsManager defaultCaseTonesVolumeForDeviceAddress:]
+ -[AXAirPodSettingsManager setCaseTonesVolume:forDeviceAddress:]
+ -[AXAirPodSettingsManager supportsCaseTonesVolumeForDeviceAddress:]
+ -[AXSCATProfile recipeCount]
+ -[AXSCATProfile switchCount]
+ -[AXSettings(AccessibilitySupportFacade) headsetCaseTonesVolumeChangedNotification]
+ -[AXSettings(AccessibilitySupportFacade) headsetCaseTonesVolumeForDeviceAddress:]
+ -[AXSettings(AccessibilitySupportFacade) headsetUpdatedDictionaryForPreference:forDeviceAddress:value:]
+ -[AXSettings(AccessibilitySupportFacade) headsetsValueForPreference:forDeviceAddress:expectedType:]
+ -[AXSettings(AccessibilitySupportFacade) headsetsValueForPreference:forDeviceAddress:expectedType:].cold.1
+ -[AXSettings(AccessibilitySupportFacade) setHeadsetCaseTonesVolume:forDeviceAddress:]
+ -[AXSettings(AccessibilitySupportFacade) setHeadsetPreference:forDeviceAddress:value:]
+ -[AXSettings(AccessibilitySupportFacade) setHeadsetPreference:forDeviceAddress:value:].cold.1
+ GCC_except_table102
+ GCC_except_table1030
+ GCC_except_table1034
+ GCC_except_table1111
+ GCC_except_table279
+ GCC_except_table468
+ GCC_except_table470
+ GCC_except_table60
+ GCC_except_table65
+ GCC_except_table702
+ GCC_except_table712
+ GCC_except_table763
+ _AXDeviceSupportsMultitasking._isFlexibleWindowingEnabled
+ _AXDeviceSupportsMultitasking.cold.1
+ _AXDeviceSupportsMultitasking.onceToken
+ _AXLiveCaptionsAnalyticsEnabledEvent
+ _AXLiveCaptionsAnalyticsEnabledKey
+ _AXLiveCaptionsAnalyticsLanguageKey
+ _AXLiveCaptionsAnalyticsLanguageSelectedEvent
+ _AXSwitchControlLocalizedString
+ _OBJC_CLASS_$_NSMutableAttributedString
+ ___29+[AXSpringBoardServer server]_block_invoke.431
+ ___37-[AXUserEventTimer userEventOccurred]_block_invoke_2
+ ___68-[AXSettings(LegacyImplementation) setSwitchControlSelectedProfile:]_block_invoke
+ ___AXDeviceSupportsMultitasking_block_invoke
+ ___AXFallbackDeviceSizeMM_block_invoke.297
+ ___AXFallbackDeviceSizeMM_block_invoke.297.cold.1
+ ___AXLoadPunctuationTable_block_invoke.117
+ ___block_descriptor_32_e22_B24?0"AXSwitch"8^B16l
+ ___block_literal_global.133
+ ___block_literal_global.197
+ ___block_literal_global.202
+ ___block_literal_global.2052
+ ___block_literal_global.2064
+ ___block_literal_global.2129
+ ___block_literal_global.213
+ ___block_literal_global.2137
+ ___block_literal_global.2185
+ ___block_literal_global.220
+ ___block_literal_global.2208
+ ___block_literal_global.2246
+ ___block_literal_global.2250
+ ___block_literal_global.244
+ ___block_literal_global.247
+ ___block_literal_global.266
+ ___block_literal_global.279
+ ___block_literal_global.285
+ ___block_literal_global.290
+ ___block_literal_global.291
+ ___block_literal_global.296
+ ___block_literal_global.305
+ ___block_literal_global.306
+ ___block_literal_global.316
+ ___block_literal_global.322
+ ___block_literal_global.324
+ ___block_literal_global.329
+ ___block_literal_global.331
+ ___block_literal_global.333
+ ___block_literal_global.337
+ ___block_literal_global.342
+ ___block_literal_global.347
+ ___block_literal_global.352
+ ___block_literal_global.357
+ ___block_literal_global.359
+ ___block_literal_global.362
+ ___block_literal_global.364
+ ___block_literal_global.367
+ ___block_literal_global.379
+ ___block_literal_global.384
+ ___block_literal_global.394
+ ___block_literal_global.409
+ ___block_literal_global.414
+ ___block_literal_global.419
+ ___block_literal_global.424
+ ___block_literal_global.432
+ ___block_literal_global.440
+ ___block_literal_global.445
+ ___block_literal_global.450
+ ___block_literal_global.458
+ ___block_literal_global.463
+ ___block_literal_global.468
+ ___block_literal_global.473
+ ___block_literal_global.478
+ ___block_literal_global.483
+ ___block_literal_global.490
+ ___block_literal_global.496
+ ___block_literal_global.4979
+ ___block_literal_global.501
+ ___block_literal_global.506
+ ___block_literal_global.511
+ ___block_literal_global.516
+ ___block_literal_global.521
+ ___block_literal_global.526
+ ___block_literal_global.531
+ ___block_literal_global.536
+ ___block_literal_global.541
+ ___block_literal_global.546
+ ___block_literal_global.551
+ ___block_literal_global.561
+ ___block_literal_global.566
+ ___block_literal_global.571
+ ___block_literal_global.576
+ ___block_literal_global.581
+ ___block_literal_global.586
+ ___block_literal_global.587
+ ___block_literal_global.591
+ ___block_literal_global.596
+ ___block_literal_global.601
+ ___block_literal_global.606
+ ___block_literal_global.611
+ ___block_literal_global.616
+ ___block_literal_global.621
+ ___block_literal_global.626
+ ___block_literal_global.631
+ ___block_literal_global.636
+ ___block_literal_global.641
+ ___block_literal_global.646
+ ___block_literal_global.651
+ ___block_literal_global.656
+ ___block_literal_global.661
+ ___block_literal_global.666
+ ___block_literal_global.671
+ ___block_literal_global.676
+ ___block_literal_global.681
+ ___block_literal_global.686
+ ___block_literal_global.691
+ ___block_literal_global.696
+ ___block_literal_global.701
+ ___block_literal_global.706
+ ___block_literal_global.711
+ ___block_literal_global.716
+ ___block_literal_global.721
+ ___block_literal_global.727
+ ___block_literal_global.732
+ ___block_literal_global.743
+ ___block_literal_global.748
+ ___block_literal_global.754
+ ___block_literal_global.760
+ ___block_literal_global.765
+ ___block_literal_global.770
+ ___block_literal_global.775
+ ___block_literal_global.780
+ ___block_literal_global.785
+ ___block_literal_global.790
+ ___block_literal_global.795
+ ___block_literal_global.800
+ ___block_literal_global.805
+ ___block_literal_global.810
+ ___block_literal_global.815
+ ___block_literal_global.820
+ ___block_literal_global.825
+ ___block_literal_global.830
+ ___block_literal_global.835
+ ___block_literal_global.840
+ ___block_literal_global.845
+ ___block_literal_global.850
+ ___block_literal_global.855
+ ___block_literal_global.860
+ ___block_literal_global.872
+ ___block_literal_global.876
+ ___block_literal_global.920
+ __eventMasksForEdgeSwipe
+ _block_copy_helper.65
+ _block_copy_helper.71
+ _block_copy_helper.74
+ _block_descriptor.67
+ _block_descriptor.73
+ _block_descriptor.76
+ _block_destroy_helper.66
+ _block_destroy_helper.72
+ _block_destroy_helper.75
+ _kAXSHeadsetCaseTonesVolumePreference
+ _keypath_get_selector_showSpeechController
+ _objc_msgSend$headsetCaseTonesVolumeChangedNotification
+ _objc_msgSend$headsetCaseTonesVolumeForDeviceAddress:
+ _objc_msgSend$headsetUpdatedDictionaryForPreference:forDeviceAddress:value:
+ _objc_msgSend$headsetsValueForPreference:forDeviceAddress:expectedType:
+ _objc_msgSend$isPersonalVoice
+ _objc_msgSend$setHeadsetCaseTonesVolume:forDeviceAddress:
+ _objc_msgSend$setHeadsetPreference:forDeviceAddress:value:
+ _objc_msgSend$setSwipeFromEdge:
+ _objc_msgSend$speechUtteranceWithAttributedString:
+ _objc_msgSend$supportsCaseTonesForDeviceAddress:
+ _objc_msgSend$swipeFromEdge
+ _objc_msgSend$synthesisProviderVoice
+ _objc_msgSend$voiceWithIdentifier:
+ _objectdestroy.347Tm
+ _server.onceToken.430
+ _swipeFromEdge
- GCC_except_table101
- GCC_except_table1029
- GCC_except_table1033
- GCC_except_table1109
- GCC_except_table112
- GCC_except_table278
- GCC_except_table467
- GCC_except_table469
- GCC_except_table59
- GCC_except_table701
- GCC_except_table711
- GCC_except_table762
- ___29+[AXSpringBoardServer server]_block_invoke.434
- ___AXFallbackDeviceSizeMM_block_invoke.295
- ___AXFallbackDeviceSizeMM_block_invoke.295.cold.1
- ___AXLoadPunctuationTable_block_invoke.114
- ___block_literal_global.195
- ___block_literal_global.200
- ___block_literal_global.2061
- ___block_literal_global.209
- ___block_literal_global.2126
- ___block_literal_global.2134
- ___block_literal_global.218
- ___block_literal_global.2182
- ___block_literal_global.2205
- ___block_literal_global.2243
- ___block_literal_global.2247
- ___block_literal_global.242
- ___block_literal_global.245
- ___block_literal_global.264
- ___block_literal_global.282
- ___block_literal_global.288
- ___block_literal_global.289
- ___block_literal_global.293
- ___block_literal_global.294
- ___block_literal_global.297
- ___block_literal_global.304
- ___block_literal_global.309
- ___block_literal_global.314
- ___block_literal_global.319
- ___block_literal_global.325
- ___block_literal_global.327
- ___block_literal_global.334
- ___block_literal_global.335
- ___block_literal_global.336
- ___block_literal_global.340
- ___block_literal_global.345
- ___block_literal_global.350
- ___block_literal_global.360
- ___block_literal_global.361
- ___block_literal_global.365
- ___block_literal_global.366
- ___block_literal_global.370
- ___block_literal_global.375
- ___block_literal_global.382
- ___block_literal_global.392
- ___block_literal_global.402
- ___block_literal_global.407
- ___block_literal_global.412
- ___block_literal_global.417
- ___block_literal_global.422
- ___block_literal_global.435
- ___block_literal_global.443
- ___block_literal_global.448
- ___block_literal_global.453
- ___block_literal_global.461
- ___block_literal_global.466
- ___block_literal_global.471
- ___block_literal_global.476
- ___block_literal_global.481
- ___block_literal_global.486
- ___block_literal_global.493
- ___block_literal_global.4965
- ___block_literal_global.499
- ___block_literal_global.504
- ___block_literal_global.509
- ___block_literal_global.514
- ___block_literal_global.519
- ___block_literal_global.524
- ___block_literal_global.529
- ___block_literal_global.534
- ___block_literal_global.539
- ___block_literal_global.549
- ___block_literal_global.554
- ___block_literal_global.559
- ___block_literal_global.564
- ___block_literal_global.569
- ___block_literal_global.574
- ___block_literal_global.579
- ___block_literal_global.584
- ___block_literal_global.589
- ___block_literal_global.590
- ___block_literal_global.594
- ___block_literal_global.599
- ___block_literal_global.604
- ___block_literal_global.609
- ___block_literal_global.614
- ___block_literal_global.619
- ___block_literal_global.624
- ___block_literal_global.629
- ___block_literal_global.634
- ___block_literal_global.639
- ___block_literal_global.644
- ___block_literal_global.649
- ___block_literal_global.654
- ___block_literal_global.659
- ___block_literal_global.664
- ___block_literal_global.669
- ___block_literal_global.674
- ___block_literal_global.679
- ___block_literal_global.684
- ___block_literal_global.689
- ___block_literal_global.694
- ___block_literal_global.699
- ___block_literal_global.704
- ___block_literal_global.709
- ___block_literal_global.714
- ___block_literal_global.719
- ___block_literal_global.724
- ___block_literal_global.730
- ___block_literal_global.735
- ___block_literal_global.746
- ___block_literal_global.751
- ___block_literal_global.757
- ___block_literal_global.763
- ___block_literal_global.768
- ___block_literal_global.773
- ___block_literal_global.778
- ___block_literal_global.783
- ___block_literal_global.788
- ___block_literal_global.793
- ___block_literal_global.798
- ___block_literal_global.803
- ___block_literal_global.808
- ___block_literal_global.813
- ___block_literal_global.818
- ___block_literal_global.823
- ___block_literal_global.828
- ___block_literal_global.833
- ___block_literal_global.838
- ___block_literal_global.843
- ___block_literal_global.848
- ___block_literal_global.853
- ___block_literal_global.858
- ___block_literal_global.863
- ___block_literal_global.866
- ___block_literal_global.879
- ___block_literal_global.923
- _block_copy_helper.61
- _block_copy_helper.67
- _block_copy_helper.70
- _block_descriptor.63
- _block_descriptor.69
- _block_descriptor.72
- _block_destroy_helper.62
- _block_destroy_helper.68
- _block_destroy_helper.71
- _objectdestroy.103Tm
- _objectdestroy.341Tm
- _server.onceToken.433
- _symbolic SSSgIegHr_
- _symbolic SSSgSg
- _symbolic SfIegHr_
- _symbolic So17AXCVoiceSelectionCSgIegHr_
- _symbolic So17AXCVoiceSelectionCSgSg
- _symbolic So21OS_dispatch_semaphoreC
- _symbolic xSgz_SSSg_lXX
- _symbolic xSgz_Sf_lXX
- _symbolic xSgz_So17AXCVoiceSelectionCSg_lXX
- _symbolic xSgz_yt_lXX
- _symbolic ytIegHr_
- _symbolic ytSg
CStrings:
+ "$brailleUsesUnderlineCursor"
+ "@40@0:8@16@24#32"
+ "AXSVoiceOverTouchBrailleUsesUnderlineCursor"
+ "F1"
+ "F10"
+ "F11"
+ "F12"
+ "F2"
+ "F3"
+ "F4"
+ "F5"
+ "F6"
+ "F7"
+ "F8"
+ "F9"
+ "Need to pass in the device address to %@"
+ "No device address for setting %@"
+ "Set case tones volume: %@ on %@"
+ "Set click and hold speed for AirPods: %@ [click %f, hold %f, ANC: (BT:%@, setting:%d)] Vol Swipe [%d, %lf]"
+ "Set click speed: [%f > %d] on %@"
+ "Setting AirPods %@:%@ %@"
+ "TC,N"
+ "_$brailleUsesUnderlineCursor_Storage"
+ "_WATCH"
+ "_showSpeechController"
+ "accessibility.page"
+ "caseTonesVolumeForDeviceAddress:"
+ "com.apple.accessibility.guestpass.enabled"
+ "com.apple.accessibility.livecaptions.enabled"
+ "com.apple.accessibility.livecaptions.language.selected"
+ "could not get case tones volume [%d] for headset: %@"
+ "could not get click speed [%d] for air pods: %@ -> [%d]"
+ "could not set case tones volume for headset: %@ -> [%@]"
+ "defaultCaseTonesVolumeForDeviceAddress:"
+ "headsetCaseTonesVolumeChangedNotification"
+ "headsetCaseTonesVolumeForDeviceAddress:"
+ "headsetUpdatedDictionaryForPreference:forDeviceAddress:value:"
+ "headsetsValueForPreference:forDeviceAddress:expectedType:"
+ "isPersonalVoice"
+ "kAXSHeadsetCaseTonesVolumePreference"
+ "recipeCount"
+ "retrieved case tones volume for air pods: %@ -> [%@]"
+ "setCaseTonesVolume:forDeviceAddress:"
+ "setHeadsetCaseTonesVolume:forDeviceAddress:"
+ "setHeadsetPreference:forDeviceAddress:value:"
+ "setSwipeFromEdge:"
+ "setVoiceOverTouchBrailleUsesUnderlineCursor:"
+ "speechUtteranceWithAttributedString:"
+ "supportsCaseTonesVolumeForDeviceAddress:"
+ "swipeFromEdge"
+ "switchCount"
+ "synthesisProviderVoice"
+ "voiceOverTouchBrailleUsesUnderlineCursor"
+ "voiceWithIdentifier:"
- "AccessibilityUtilities/AXSettings.swift"
- "Failed to get result."
- "Potential Structural Swift Concurrency Issue: unsafeForcedSync called from Swift Concurrent context."
- "Set click and hold speed for airpod: %@ [click %f, hold %f, ANC: (BT:%@, setting:%d)] Vol Swipe [%d, %lf]"
- "Set double click mode: %d on %@"
- "could not get click speed[%d] for air pods: %@ -> [%d]"

```
