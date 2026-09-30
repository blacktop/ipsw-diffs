## AccessibilityUtilities

> `/System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities`

```diff

-3191.7.24.0.0
-  __TEXT.__text: 0x155840
-  __TEXT.__auth_stubs: 0x4bd0
-  __TEXT.__objc_methlist: 0xf19c
-  __TEXT.__cstring: 0x1b416
-  __TEXT.__const: 0x41e4
-  __TEXT.__gcc_except_tab: 0x136c
-  __TEXT.__oslogstring: 0x6134
-  __TEXT.__dlopen_cstrs: 0xba9
+3191.19.0.0.0
+  __TEXT.__text: 0x15c744
+  __TEXT.__auth_stubs: 0x4f30
+  __TEXT.__objc_methlist: 0xf1f4
+  __TEXT.__cstring: 0x17e72
+  __TEXT.__const: 0x5244
+  __TEXT.__gcc_except_tab: 0x132c
+  __TEXT.__oslogstring: 0x6244
+  __TEXT.__dlopen_cstrs: 0xc07
   __TEXT.__ustring: 0x68
-  __TEXT.__swift5_typeref: 0x1088
-  __TEXT.__swift5_capture: 0xd0c
-  __TEXT.__constg_swiftt: 0x984
-  __TEXT.__swift5_reflstr: 0x286c
-  __TEXT.__swift5_fieldmd: 0x11cc
-  __TEXT.__swift5_builtin: 0x1a4
-  __TEXT.__swift5_assocty: 0x2d0
-  __TEXT.__swift5_proto: 0x20c
-  __TEXT.__swift5_types: 0xc0
-  __TEXT.__swift_as_entry: 0x100
-  __TEXT.__swift_as_ret: 0x144
-  __TEXT.__unwind_info: 0x6010
-  __TEXT.__eh_frame: 0x3898
-  __TEXT.__objc_classname: 0xda5
-  __TEXT.__objc_methname: 0x2a1fe
-  __TEXT.__objc_methtype: 0x30d9
-  __TEXT.__objc_stubs: 0x154a0
-  __DATA_CONST.__got: 0x1c08
-  __DATA_CONST.__const: 0x3cd8
-  __DATA_CONST.__objc_classlist: 0x458
+  __TEXT.__swift5_typeref: 0x1454
+  __TEXT.__swift5_capture: 0xd24
+  __TEXT.__constg_swiftt: 0xc6c
+  __TEXT.__swift5_reflstr: 0x2b4c
+  __TEXT.__swift5_fieldmd: 0x15b4
+  __TEXT.__swift5_builtin: 0x1b8
+  __TEXT.__swift5_assocty: 0x3a8
+  __TEXT.__swift5_proto: 0x308
+  __TEXT.__swift5_types: 0x100
+  __TEXT.__swift_as_entry: 0x108
+  __TEXT.__swift_as_ret: 0x14c
+  __TEXT.__unwind_info: 0x6658
+  __TEXT.__eh_frame: 0x4058
+  __TEXT.__objc_classname: 0x13b6
+  __TEXT.__objc_methname: 0x2d363
+  __TEXT.__objc_methtype: 0x338b
+  __TEXT.__objc_stubs: 0x15e20
+  __DATA_CONST.__got: 0x1c80
+  __DATA_CONST.__const: 0x3da8
+  __DATA_CONST.__objc_classlist: 0x470
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9a98
+  __DATA_CONST.__objc_selrefs: 0x9b08
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x300
-  __DATA_CONST.__objc_arraydata: 0x7c8
-  __AUTH_CONST.__auth_got: 0x25f8
-  __AUTH_CONST.__const: 0x4850
-  __AUTH_CONST.__cfstring: 0x149e0
-  __AUTH_CONST.__objc_const: 0x14238
-  __AUTH_CONST.__objc_intobj: 0x1440
+  __DATA_CONST.__objc_arraydata: 0x7d0
+  __AUTH_CONST.__auth_got: 0x27a8
+  __AUTH_CONST.__const: 0x4f38
+  __AUTH_CONST.__cfstring: 0x14a60
+  __AUTH_CONST.__objc_const: 0x14690
+  __AUTH_CONST.__objc_intobj: 0x1458
   __AUTH_CONST.__objc_arrayobj: 0x228
   __AUTH_CONST.__objc_dictobj: 0x2d0
   __AUTH_CONST.__objc_doubleobj: 0x70
-  __AUTH.__objc_data: 0x2860
-  __AUTH.__data: 0x650
-  __DATA.__objc_ivar: 0xb64
-  __DATA.__data: 0x25b8
-  __DATA.__bss: 0x3df8
-  __DATA_DIRTY.__objc_data: 0x10b0
-  __DATA_DIRTY.__data: 0x310
-  __DATA_DIRTY.__bss: 0xf58
+  __AUTH.__objc_data: 0x2690
+  __AUTH.__data: 0x8c8
+  __DATA.__objc_ivar: 0xb6c
+  __DATA.__data: 0x26e0
+  __DATA.__bss: 0x5988
+  __DATA_DIRTY.__objc_data: 0x1280
+  __DATA_DIRTY.__data: 0x4a8
+  __DATA_DIRTY.__bss: 0x1358
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1EEE2F66-B202-3F9C-AFCB-8197AAF1A0FC
-  Functions: 9425
-  Symbols:   19949
-  CStrings:  13680
+  UUID: A67CDA82-8D73-3DD6-8088-D59897DE6A9F
+  Functions: 9715
+  Symbols:   20298
+  CStrings:  13628
 
Symbols:
+ -[AXEventProcessor initWithHIDTapIdentifier:HIDEventTapPriority:shouldMonitorHIDEventsOnly:shouldSeparateHIDStreamsBySenderID:systemEventTapIdentifier:systemEventTapPriority:]
+ -[AXEventProcessor setShouldSeparateHIDStreamsBySenderID:]
+ -[AXEventProcessor shouldSeparateHIDStreamsBySenderID]
+ -[AXEventTapManager installEventTap:identifier:type:skipDeviceMatching:shouldSeparateHIDStreamsBySenderID:filterEvents:matchingServiceHandler:]
+ -[AXEventTapPair setShouldSeparateHIDStreamsBySenderID:]
+ -[AXEventTapPair shouldSeparateHIDStreamsBySenderID]
+ -[AXSettings(AccessibilitySupportFacade) hoverTypingContentSize]
+ -[AXSettings(AccessibilitySupportFacade) setHoverTypingContentSize:]
+ GCC_except_table104
+ GCC_except_table34
+ GCC_except_table45
+ GCC_except_table55
+ GCC_except_table70
+ _AXAssistiveTouchIconTypeDisplayAppearance
+ _AXIsBeatsDevice
+ _AXSSIsAppleInternalBuild
+ _CGFontCopyFullName
+ _HearingUtilitiesLibrary
+ _HearingUtilitiesLibrary.cold.1
+ _MACaptionAppearancePrefCopyFontForStyle
+ _NSURLCreationDateKey
+ _OBJC_CLASS_$_NSFileAccessIntent
+ _OBJC_CLASS_$_NSFileCoordinator
+ _OBJC_IVAR_$_AXEventProcessor._shouldSeparateHIDStreamsBySenderID
+ _OBJC_IVAR_$_AXEventTapPair._shouldSeparateHIDStreamsBySenderID
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __DATA__TtC22AccessibilityUtilities25AXLiveOnCollectionManager
+ __DATA__TtCC22AccessibilityUtilities25AXLiveOnCollectionManagerP33_D8726E7DC8A860BC324A391CEA7FFF7624LiveOnCollectionSettings
+ __DATA__TtCE22AccessibilityUtilitiesCSo10AXSettings15LiveRecognition
+ __IVARS__TtC22AccessibilityUtilities25AXLiveOnCollectionManager
+ __IVARS__TtCC22AccessibilityUtilities25AXLiveOnCollectionManagerP33_D8726E7DC8A860BC324A391CEA7FFF7624LiveOnCollectionSettings
+ __IVARS__TtCE22AccessibilityUtilitiesCSo10AXSettings15LiveRecognition
+ __METACLASS_DATA__TtC22AccessibilityUtilities25AXLiveOnCollectionManager
+ __METACLASS_DATA__TtCC22AccessibilityUtilities25AXLiveOnCollectionManagerP33_D8726E7DC8A860BC324A391CEA7FFF7624LiveOnCollectionSettings
+ __METACLASS_DATA__TtCE22AccessibilityUtilitiesCSo10AXSettings15LiveRecognition
+ ___175-[AXEventProcessor initWithHIDTapIdentifier:HIDEventTapPriority:shouldMonitorHIDEventsOnly:shouldSeparateHIDStreamsBySenderID:systemEventTapIdentifier:systemEventTapPriority:]_block_invoke
+ ___29+[AXSpringBoardServer server]_block_invoke.482
+ ___61+[AXTripleClickHelpers _toggleSmartInvertColorsOffMainThread]_block_invoke.592
+ ___61+[AXTripleClickHelpers _toggleSmartInvertColorsOffMainThread]_block_invoke.599
+ ___64+[AXTripleClickHelpers _localToggleAccessibilityShortcutOption:]_block_invoke.626
+ ___66+[AXTripleClickHelpers _localValueForAccessibilityShortcutOption:]_block_invoke
+ ___66+[AXTripleClickHelpers _localValueForAccessibilityShortcutOption:]_block_invoke_2
+ ___66+[AXTripleClickHelpers _localValueForAccessibilityShortcutOption:]_block_invoke_3
+ ___AXFallbackDeviceSizeMM_block_invoke.300
+ ___AXFallbackDeviceSizeMM_block_invoke.300.cold.1
+ ___block_descriptor_40_e8_32r_e44_v44?0"NSDictionary"8Q16"NSString"24B32Q36lr32l8
+ ___block_descriptor_40_e8_32r_e8_v12?0B8lr32l8
+ ___block_descriptor_57_e8_32s40r_e8_v12?0B8ls32l8r40l8
+ ___block_literal_global.120
+ ___block_literal_global.128
+ ___block_literal_global.136
+ ___block_literal_global.145
+ ___block_literal_global.148
+ ___block_literal_global.200
+ ___block_literal_global.205
+ ___block_literal_global.2127
+ ___block_literal_global.214
+ ___block_literal_global.216
+ ___block_literal_global.2202
+ ___block_literal_global.2210
+ ___block_literal_global.223
+ ___block_literal_global.2260
+ ___block_literal_global.2321
+ ___block_literal_global.2325
+ ___block_literal_global.2364
+ ___block_literal_global.250
+ ___block_literal_global.269
+ ___block_literal_global.294
+ ___block_literal_global.304
+ ___block_literal_global.306
+ ___block_literal_global.330
+ ___block_literal_global.347
+ ___block_literal_global.352
+ ___block_literal_global.357
+ ___block_literal_global.363
+ ___block_literal_global.368
+ ___block_literal_global.373
+ ___block_literal_global.375
+ ___block_literal_global.376
+ ___block_literal_global.380
+ ___block_literal_global.381
+ ___block_literal_global.382
+ ___block_literal_global.389
+ ___block_literal_global.394
+ ___block_literal_global.398
+ ___block_literal_global.399
+ ___block_literal_global.400
+ ___block_literal_global.404
+ ___block_literal_global.408
+ ___block_literal_global.409
+ ___block_literal_global.414
+ ___block_literal_global.419
+ ___block_literal_global.424
+ ___block_literal_global.429
+ ___block_literal_global.434
+ ___block_literal_global.439
+ ___block_literal_global.441
+ ___block_literal_global.446
+ ___block_literal_global.451
+ ___block_literal_global.456
+ ___block_literal_global.461
+ ___block_literal_global.466
+ ___block_literal_global.471
+ ___block_literal_global.476
+ ___block_literal_global.484
+ ___block_literal_global.492
+ ___block_literal_global.497
+ ___block_literal_global.510
+ ___block_literal_global.5103
+ ___block_literal_global.515
+ ___block_literal_global.520
+ ___block_literal_global.525
+ ___block_literal_global.530
+ ___block_literal_global.535
+ ___block_literal_global.542
+ ___block_literal_global.55
+ ___block_literal_global.606
+ ___block_literal_global.609
+ ___block_literal_global.625
+ ___block_literal_global.69
+ ___block_literal_global.743
+ ___block_literal_global.748
+ ___block_literal_global.753
+ ___block_literal_global.758
+ ___block_literal_global.763
+ ___block_literal_global.768
+ ___block_literal_global.773
+ ___block_literal_global.778
+ ___block_literal_global.784
+ ___block_literal_global.789
+ ___block_literal_global.800
+ ___block_literal_global.805
+ ___block_literal_global.810
+ ___block_literal_global.816
+ ___block_literal_global.821
+ ___block_literal_global.826
+ ___block_literal_global.831
+ ___block_literal_global.836
+ ___block_literal_global.841
+ ___block_literal_global.846
+ ___block_literal_global.851
+ ___block_literal_global.856
+ ___block_literal_global.861
+ ___block_literal_global.866
+ ___block_literal_global.871
+ ___block_literal_global.876
+ ___block_literal_global.886
+ ___block_literal_global.891
+ ___block_literal_global.896
+ ___block_literal_global.901
+ ___block_literal_global.906
+ ___block_literal_global.911
+ ___block_literal_global.916
+ ___block_literal_global.919
+ ___block_literal_global.922
+ ___block_literal_global.93
+ ___block_literal_global.932
+ ___block_literal_global.974
+ ___getHUAccessoryCompatibilityUtilitiesClass_block_invoke
+ ___getHUAccessoryCompatibilityUtilitiesClass_block_invoke.cold.1
+ ___getHUAccessoryCompatibilityUtilitiesClass_block_invoke.cold.2
+ ___getHUAccessoryManagerClass_block_invoke
+ ___getHUAccessoryManagerClass_block_invoke.cold.1
+ ___getPASettingsClass_block_invoke.cold.2
+ ___swift_memcpy0_1
+ ___swift_memcpy112_8
+ ___swift_memcpy24_8
+ ___swift_memcpy88_8
+ __swift_stdlib_bridgeErrorToNSError
+ _associated conformance 22AccessibilityUtilities25AXLiveOnCollectionManagerC04LivedE8Settings33_D8726E7DC8A860BC324A391CEA7FFF76LLC06AXCoreB0012AXObservableH0AA11Observation10Observable
+ _associated conformance 22AccessibilityUtilities25AXLiveOnCollectionManagerC04LivedE8Settings33_D8726E7DC8A860BC324A391CEA7FFF76LLC06AXCoreB0012AXObservableH0AaG18AXSelectorRoutable
+ _associated conformance 22AccessibilityUtilities25AXLiveOnCollectionManagerC04LivedE8Settings33_D8726E7DC8A860BC324A391CEA7FFF76LLC06AXCoreB018AXSelectorRoutableAaG13AXReflectable
+ _associated conformance 22AccessibilityUtilities25AXLiveOnCollectionManagerC06LoadedE4ItemVs12IdentifiableAA2IDsAFP_SH
+ _associated conformance 22AccessibilityUtilities25AXLiveOnCollectionManagerC0E4ItemV10CodingKeys33_D8726E7DC8A860BC324A391CEA7FFF76LLOSHAASQ
+ _associated conformance 22AccessibilityUtilities25AXLiveOnCollectionManagerC0E4ItemV10CodingKeys33_D8726E7DC8A860BC324A391CEA7FFF76LLOs0H3KeyAAs23CustomStringConvertible
+ _associated conformance 22AccessibilityUtilities25AXLiveOnCollectionManagerC0E4ItemV10CodingKeys33_D8726E7DC8A860BC324A391CEA7FFF76LLOs0H3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 22AccessibilityUtilities25AXLiveOnCollectionManagerC0E4ItemVSHAASQ
+ _associated conformance 22AccessibilityUtilities25AXLiveOnCollectionManagerC0E4ItemVSLAASQ
+ _associated conformance 22AccessibilityUtilities25AXLiveOnCollectionManagerC0E4ItemVs12IdentifiableAA2IDsAFP_SH
+ _associated conformance 22AccessibilityUtilities25AXLiveOnCollectionManagerC0E7Context33_D8726E7DC8A860BC324A391CEA7FFF76LLV10CodingKeysOSHAASQ
+ _associated conformance 22AccessibilityUtilities25AXLiveOnCollectionManagerC0E7Context33_D8726E7DC8A860BC324A391CEA7FFF76LLV10CodingKeysOs0P3KeyAAs23CustomStringConvertible
+ _associated conformance 22AccessibilityUtilities25AXLiveOnCollectionManagerC0E7Context33_D8726E7DC8A860BC324A391CEA7FFF76LLV10CodingKeysOs0P3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 22AccessibilityUtilities25AXLiveOnCollectionManagerC12UserFeedback33_D8726E7DC8A860BC324A391CEA7FFF76LLV10CodingKeysOSHAASQ
+ _associated conformance 22AccessibilityUtilities25AXLiveOnCollectionManagerC12UserFeedback33_D8726E7DC8A860BC324A391CEA7FFF76LLV10CodingKeysOs0Q3KeyAAs23CustomStringConvertible
+ _associated conformance 22AccessibilityUtilities25AXLiveOnCollectionManagerC12UserFeedback33_D8726E7DC8A860BC324A391CEA7FFF76LLV10CodingKeysOs0Q3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 22AccessibilityUtilities25AXLiveOnCollectionManagerC14ExportMetadata33_D8726E7DC8A860BC324A391CEA7FFF76LLV10CodingKeysOSHAASQ
+ _associated conformance 22AccessibilityUtilities25AXLiveOnCollectionManagerC14ExportMetadata33_D8726E7DC8A860BC324A391CEA7FFF76LLV10CodingKeysOs0Q3KeyAAs23CustomStringConvertible
+ _associated conformance 22AccessibilityUtilities25AXLiveOnCollectionManagerC14ExportMetadata33_D8726E7DC8A860BC324A391CEA7FFF76LLV10CodingKeysOs0Q3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 22AccessibilityUtilities25AXLiveOnCollectionManagerC5TopicOSHAASQ
+ _associated conformance 22AccessibilityUtilities25AXLiveOnCollectionManagerC5TopicOs12CaseIterableAA8AllCasessAFP_Sl
+ _associated conformance 22AccessibilityUtilities25AXLiveOnCollectionManagerC5TopicOs12IdentifiableAA2IDsAFP_SH
+ _associated conformance So10AXSettingsC22AccessibilityUtilitiesE15LiveRecognitionC06AXCoreC018AXSelectorRoutableAcF13AXReflectable
+ _associated conformance So10AXSettingsC22AccessibilityUtilitiesE15LiveRecognitionC06AXCoreC020AXObservableSettingsAC11Observation10Observable
+ _associated conformance So10AXSettingsC22AccessibilityUtilitiesE15LiveRecognitionC06AXCoreC020AXObservableSettingsAcF18AXSelectorRoutable
+ _associated conformance So10AXSettingsC22AccessibilityUtilitiesE22PreferredOneShotSourceOSHACSQ
+ _associated conformance So10AXSettingsC22AccessibilityUtilitiesE22PreferredOneShotSourceOs12IdentifiableAC2IDsAFP_SH
+ _associated conformance So16NSURLResourceKeyaSHSCSQ
+ _associated conformance So16NSURLResourceKeyas20_SwiftNewtypeWrapperSCSY
+ _associated conformance So16NSURLResourceKeyas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
+ _getHUAccessoryCompatibilityUtilitiesClass
+ _getHUAccessoryCompatibilityUtilitiesClass.softClass
+ _getHUAccessoryManagerClass
+ _getHUAccessoryManagerClass.softClass
+ _objc_msgSend$AX_FloatProbablyEqual::
+ _objc_msgSend$_AXConvertAudioBalanceValueFromDisplay:
+ _objc_msgSend$_AXConvertAudioBalanceValueToDisplay:
+ _objc_msgSend$_colorProbablyEqual::
+ _objc_msgSend$_convertCaptionColor:
+ _objc_msgSend$_convertTextEdgeStyle:
+ _objc_msgSend$_createCaptionStyles
+ _objc_msgSend$accessibilityReaderEnabled
+ _objc_msgSend$assistiveTouchAxisSweepSpeed
+ _objc_msgSend$assistiveTouchCursorColor
+ _objc_msgSend$assistiveTouchMouseDwellControlKeyboardKeyActivationTimeout
+ _objc_msgSend$assistiveTouchScannerCursorHighVisibilityEnabled
+ _objc_msgSend$contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:
+ _objc_msgSend$convertColor:
+ _objc_msgSend$convertEdgeStyle:
+ _objc_msgSend$coordinateAccessWithIntents:queue:byAccessor:
+ _objc_msgSend$defaultTableForLocale:
+ _objc_msgSend$deviceIsAirPodsWithAXSettings:
+ _objc_msgSend$deviceIsBeatsDevice:
+ _objc_msgSend$deviceIsBeatsProductWithAXSettings:
+ _objc_msgSend$effects
+ _objc_msgSend$enableVoiceOverCaptions
+ _objc_msgSend$fileExistsAtPath:
+ _objc_msgSend$fullKeyboardAccessFocusRingColor
+ _objc_msgSend$fullKeyboardAccessFocusRingHighContrastEnabled
+ _objc_msgSend$fullKeyboardAccessLargeFocusRingEnabled
+ _objc_msgSend$getCurrentRouteSupportingHeadphoneAccommodationsWithCompletion:
+ _objc_msgSend$getSSLEnabledForAddress:withCompletion:
+ _objc_msgSend$getSSLSupportStateForAddress:withCompletion:
+ _objc_msgSend$hoverTextContentSize
+ _objc_msgSend$increaseContrastEnabled
+ _objc_msgSend$initWithBool:
+ _objc_msgSend$initWithDouble:
+ _objc_msgSend$initWithFloat:
+ _objc_msgSend$initWithHIDTapIdentifier:HIDEventTapPriority:shouldMonitorHIDEventsOnly:shouldSeparateHIDStreamsBySenderID:systemEventTapIdentifier:systemEventTapPriority:
+ _objc_msgSend$initWithInteger:
+ _objc_msgSend$installEventTap:identifier:type:skipDeviceMatching:shouldSeparateHIDStreamsBySenderID:filterEvents:matchingServiceHandler:
+ _objc_msgSend$isDarkModeActive
+ _objc_msgSend$isOrientationLocked
+ _objc_msgSend$liveCaptionsTranscriberVersion
+ _objc_msgSend$liveSpeechVoiceIdentifierForKeyboardID:
+ _objc_msgSend$moveItemAtURL:toURL:error:
+ _objc_msgSend$postInit
+ _objc_msgSend$readingIntentWithURL:options:
+ _objc_msgSend$selectedSpeechVoiceIdentifiersWithLanguageSource
+ _objc_msgSend$selection
+ _objc_msgSend$setAssistiveTouchAxisSweepSpeed:
+ _objc_msgSend$setAssistiveTouchCursorColor:
+ _objc_msgSend$setAssistiveTouchMouseDwellControlActivationTimeout:
+ _objc_msgSend$setAssistiveTouchMouseDwellControlKeyboardKeyActivationTimeout:
+ _objc_msgSend$setAssistiveTouchScannerCursorHighVisibilityEnabled:
+ _objc_msgSend$setCameraSwitch:
+ _objc_msgSend$setEnableVoiceOverCaptions:
+ _objc_msgSend$setIncreaseContrastEnabled:
+ _objc_msgSend$setLeftRightBalanceValue:
+ _objc_msgSend$setOrientationLocked:
+ _objc_msgSend$setSelection:
+ _objc_msgSend$setShouldSeparateHIDStreamsBySenderID:
+ _objc_msgSend$setShowSpeechController:
+ _objc_msgSend$setSpeechControllerIdleOpacity:
+ _objc_msgSend$setSwitchControlPointPickerSelectionStyle:
+ _objc_msgSend$setUserDefinedName:
+ _objc_msgSend$setVoiceOverEffectiveSpeakingRate:
+ _objc_msgSend$setVoiceOverEffectiveSpeakingVolume:
+ _objc_msgSend$setVoiceOverLargeCursorEnabled:
+ _objc_msgSend$setVoiceOverSpeakingRate:
+ _objc_msgSend$shouldSeparateHIDStreamsBySenderID
+ _objc_msgSend$showSpeechController
+ _objc_msgSend$speechControllerIdleOpacity
+ _objc_msgSend$switchControlPointPickerSelectionStyle
+ _objc_msgSend$toggleDarkMode
+ _objc_msgSend$tripleClickOptionsForAccessibilityShortcutControlCenterModuleIncludingGuidedAccess:
+ _objc_msgSend$userDefinedName
+ _objc_msgSend$voiceOverEffectiveSpeakingRate
+ _objc_msgSend$voiceOverEffectiveSpeakingVolume
+ _objc_msgSend$voiceOverLargeCursorEnabled
+ _objc_msgSend$voiceOverSpeakingRate
+ _objc_msgSend$voiceSettings
+ _objectdestroy.62Tm
+ _objectdestroy.68Tm
+ _objectdestroy.83Tm
+ _objectdestroy.87Tm
+ _server.onceToken.481
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain_n
+ _swift_defaultActor_deallocate
+ _swift_defaultActor_destroy
+ _swift_defaultActor_initialize
+ _swift_deletedAsyncMethodErrorTu
+ _swift_dynamicCastObjCClass
+ _symbolic $ss12CaseIterableP
+ _symbolic BD
+ _symbolic SDySS_____G 10Foundation4DataV
+ _symbolic SDy__________G 22AccessibilityUtilities25AXLiveOnCollectionManagerC5TopicO 10Foundation4DateV
+ _symbolic SS5label_SS5valuet
+ _symbolic SS5label_SS5valuetSg
+ _symbolic SS5label______9imageDatat 10Foundation4DataV
+ _symbolic SaySS5label_SS5valuetG
+ _symbolic SaySS5label______9imageDatatG 10Foundation4DataV
+ _symbolic Say_____G 10Foundation11JSONEncoderC16OutputFormattingV
+ _symbolic Say_____G 22AccessibilityUtilities25AXLiveOnCollectionManagerC5TopicO
+ _symbolic ScCy___________pG 10Foundation3URLV s5ErrorP
+ _symbolic So18NSFileAccessIntentC
+ _symbolic _____ 10Foundation3URLV
+ _symbolic _____ 10Foundation4DateV
+ _symbolic _____ 22AccessibilityUtilities25AXLiveOnCollectionManagerC
+ _symbolic _____ 22AccessibilityUtilities25AXLiveOnCollectionManagerC04LivedE8Settings33_D8726E7DC8A860BC324A391CEA7FFF76LLC
+ _symbolic _____ 22AccessibilityUtilities25AXLiveOnCollectionManagerC06LoadedE4ItemV
+ _symbolic _____ 22AccessibilityUtilities25AXLiveOnCollectionManagerC0E4ItemV
+ _symbolic _____ 22AccessibilityUtilities25AXLiveOnCollectionManagerC0E4ItemV10CodingKeys33_D8726E7DC8A860BC324A391CEA7FFF76LLO
+ _symbolic _____ 22AccessibilityUtilities25AXLiveOnCollectionManagerC0E7Context33_D8726E7DC8A860BC324A391CEA7FFF76LLV
+ _symbolic _____ 22AccessibilityUtilities25AXLiveOnCollectionManagerC0E7Context33_D8726E7DC8A860BC324A391CEA7FFF76LLV10CodingKeysO
+ _symbolic _____ 22AccessibilityUtilities25AXLiveOnCollectionManagerC12UserFeedback33_D8726E7DC8A860BC324A391CEA7FFF76LLV
+ _symbolic _____ 22AccessibilityUtilities25AXLiveOnCollectionManagerC12UserFeedback33_D8726E7DC8A860BC324A391CEA7FFF76LLV10CodingKeysO
+ _symbolic _____ 22AccessibilityUtilities25AXLiveOnCollectionManagerC14ExportMetadata33_D8726E7DC8A860BC324A391CEA7FFF76LLV
+ _symbolic _____ 22AccessibilityUtilities25AXLiveOnCollectionManagerC14ExportMetadata33_D8726E7DC8A860BC324A391CEA7FFF76LLV10CodingKeysO
+ _symbolic _____ 22AccessibilityUtilities25AXLiveOnCollectionManagerC5ErrorO
+ _symbolic _____ 22AccessibilityUtilities25AXLiveOnCollectionManagerC5TopicO
+ _symbolic _____ So10AXSettingsC22AccessibilityUtilitiesE15LiveRecognitionC
+ _symbolic _____ So10AXSettingsC22AccessibilityUtilitiesE22PreferredOneShotSourceO
+ _symbolic _____ So16NSURLResourceKeya
+ _symbolic _____Sg_ABt 12TextToSpeech15CoreSynthesizerC5VoiceV
+ _symbolic ___________t 22AccessibilityUtilities25AXLiveOnCollectionManagerC5TopicO 10Foundation4DateV
+ _symbolic ______pSg 15AXCoreUtilities17AXSettingProtocolP
+ _symbolic _____ySDy__________GG 15AXCoreUtilities15AXSettingRecordC 013AccessibilityB025AXLiveOnCollectionManagerC5TopicO 10Foundation4DateV
+ _symbolic _____ySDy__________GGSg 15AXCoreUtilities15AXSettingRecordC 013AccessibilityB025AXLiveOnCollectionManagerC5TopicO 10Foundation4DateV
+ _symbolic _____ySS5label_SS5valuetG s23_ContiguousArrayStorageC
+ _symbolic _____ySS5label______9imageDatatG s23_ContiguousArrayStorageC 10Foundation4DataV
+ _symbolic _____ySS_____G s18_DictionaryStorageC 10Foundation4DataV
+ _symbolic _____y_____G 15AXCoreUtilities15AXSettingRecordC So10AXSettingsC013AccessibilityB0E22PreferredOneShotSourceO
+ _symbolic _____y_____G s11_SetStorageC So16NSURLResourceKeya
+ _symbolic _____y_____G s22KeyedDecodingContainerV 22AccessibilityUtilities25AXLiveOnCollectionManagerC0H4ItemV10CodingKeys33_D8726E7DC8A860BC324A391CEA7FFF76LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 22AccessibilityUtilities25AXLiveOnCollectionManagerC0H7Context33_D8726E7DC8A860BC324A391CEA7FFF76LLV10CodingKeysO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 22AccessibilityUtilities25AXLiveOnCollectionManagerC12UserFeedback33_D8726E7DC8A860BC324A391CEA7FFF76LLV10CodingKeysO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 22AccessibilityUtilities25AXLiveOnCollectionManagerC14ExportMetadata33_D8726E7DC8A860BC324A391CEA7FFF76LLV10CodingKeysO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 22AccessibilityUtilities25AXLiveOnCollectionManagerC0H4ItemV10CodingKeys33_D8726E7DC8A860BC324A391CEA7FFF76LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 22AccessibilityUtilities25AXLiveOnCollectionManagerC0H7Context33_D8726E7DC8A860BC324A391CEA7FFF76LLV10CodingKeysO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 22AccessibilityUtilities25AXLiveOnCollectionManagerC12UserFeedback33_D8726E7DC8A860BC324A391CEA7FFF76LLV10CodingKeysO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 22AccessibilityUtilities25AXLiveOnCollectionManagerC14ExportMetadata33_D8726E7DC8A860BC324A391CEA7FFF76LLV10CodingKeysO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 10Foundation11JSONEncoderC16OutputFormattingV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 10Foundation3URLV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 22AccessibilityUtilities25AXLiveOnCollectionManagerC0H4ItemV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC So16NSURLResourceKeya
+ _symbolic _____y_____GSg 15AXCoreUtilities15AXSettingRecordC So10AXSettingsC013AccessibilityB0E22PreferredOneShotSourceO
+ _symbolic _____y__________G s18_DictionaryStorageC 22AccessibilityUtilities25AXLiveOnCollectionManagerC5TopicO 10Foundation4DateV
+ _type_layout_string 22AccessibilityUtilities25AXLiveOnCollectionManagerC0E7Context33_D8726E7DC8A860BC324A391CEA7FFF76LLV
+ _type_layout_string 22AccessibilityUtilities25AXLiveOnCollectionManagerC12UserFeedback33_D8726E7DC8A860BC324A391CEA7FFF76LLV
+ _type_layout_string 22AccessibilityUtilities25AXLiveOnCollectionManagerC14ExportMetadata33_D8726E7DC8A860BC324A391CEA7FFF76LLV
+ _type_layout_string 22AccessibilityUtilities25AXLiveOnCollectionManagerC5ErrorO
- +[AXTripleClickHelpers _localValueForAccessibilityShortcutOption:].cold.1
- -[AXEventRepresentation resetInitialTouchCountValueForHidStreamIdentifier:]
- GCC_except_table16
- GCC_except_table31
- GCC_except_table39
- GCC_except_table43
- GCC_except_table68
- GCC_except_table69
- _AXIsBeatsProductId
- _AX_CGPointInset
- _PersonalAudioLibrary
- _PersonalAudioLibrary.cold.1
- ___140-[AXEventProcessor initWithHIDTapIdentifier:HIDEventTapPriority:shouldMonitorHIDEventsOnly:systemEventTapIdentifier:systemEventTapPriority:]_block_invoke
- ___29+[AXSpringBoardServer server]_block_invoke.443
- ___61+[AXTripleClickHelpers _toggleSmartInvertColorsOffMainThread]_block_invoke.545
- ___61+[AXTripleClickHelpers _toggleSmartInvertColorsOffMainThread]_block_invoke.552
- ___64+[AXTripleClickHelpers _localToggleAccessibilityShortcutOption:]_block_invoke.579
- ___AXFallbackDeviceSizeMM_block_invoke.297
- ___AXFallbackDeviceSizeMM_block_invoke.297.cold.1
- ___block_literal_global.117
- ___block_literal_global.125
- ___block_literal_global.133
- ___block_literal_global.140
- ___block_literal_global.143
- ___block_literal_global.197
- ___block_literal_global.202
- ___block_literal_global.2085
- ___block_literal_global.211
- ___block_literal_global.213
- ___block_literal_global.2160
- ___block_literal_global.2168
- ___block_literal_global.220
- ___block_literal_global.2218
- ___block_literal_global.2241
- ___block_literal_global.2279
- ___block_literal_global.2322
- ___block_literal_global.244
- ___block_literal_global.266
- ___block_literal_global.291
- ___block_literal_global.296
- ___block_literal_global.297
- ___block_literal_global.301
- ___block_literal_global.303
- ___block_literal_global.305
- ___block_literal_global.313
- ___block_literal_global.318
- ___block_literal_global.323
- ___block_literal_global.328
- ___block_literal_global.334
- ___block_literal_global.343
- ___block_literal_global.344
- ___block_literal_global.345
- ___block_literal_global.349
- ___block_literal_global.354
- ___block_literal_global.359
- ___block_literal_global.364
- ___block_literal_global.369
- ___block_literal_global.374
- ___block_literal_global.378
- ___block_literal_global.379
- ___block_literal_global.390
- ___block_literal_global.391
- ___block_literal_global.393
- ___block_literal_global.395
- ___block_literal_global.397
- ___block_literal_global.401
- ___block_literal_global.403
- ___block_literal_global.405
- ___block_literal_global.410
- ___block_literal_global.411
- ___block_literal_global.421
- ___block_literal_global.426
- ___block_literal_global.438
- ___block_literal_global.444
- ___block_literal_global.452
- ___block_literal_global.457
- ___block_literal_global.462
- ___block_literal_global.470
- ___block_literal_global.475
- ___block_literal_global.480
- ___block_literal_global.485
- ___block_literal_global.490
- ___block_literal_global.495
- ___block_literal_global.5057
- ___block_literal_global.508
- ___block_literal_global.513
- ___block_literal_global.518
- ___block_literal_global.523
- ___block_literal_global.528
- ___block_literal_global.533
- ___block_literal_global.538
- ___block_literal_global.543
- ___block_literal_global.559
- ___block_literal_global.562
- ___block_literal_global.571
- ___block_literal_global.599
- ___block_literal_global.66
- ___block_literal_global.744
- ___block_literal_global.749
- ___block_literal_global.760
- ___block_literal_global.765
- ___block_literal_global.771
- ___block_literal_global.777
- ___block_literal_global.782
- ___block_literal_global.787
- ___block_literal_global.792
- ___block_literal_global.797
- ___block_literal_global.802
- ___block_literal_global.807
- ___block_literal_global.812
- ___block_literal_global.817
- ___block_literal_global.822
- ___block_literal_global.827
- ___block_literal_global.832
- ___block_literal_global.837
- ___block_literal_global.842
- ___block_literal_global.847
- ___block_literal_global.852
- ___block_literal_global.857
- ___block_literal_global.862
- ___block_literal_global.867
- ___block_literal_global.872
- ___block_literal_global.877
- ___block_literal_global.884
- ___block_literal_global.893
- ___block_literal_global.90
- ___block_literal_global.935
- ___getHUComfortSoundsSettingsClass_block_invoke.cold.2
- ___getpaBluetoothDeviceSupportsSSLSymbolLoc_block_invoke
- ___getpaCurrentBluetoothDeviceSupportingTransparencyAccommodationsSymbolLoc_block_invoke
- ___getpaCurrentRouteSupportsTransparencyAccommodationsSymbolLoc_block_invoke
- ___swift_mutable_project_boxed_opaque_existential_1
- _getpaBluetoothDeviceSupportsSSLSymbolLoc.ptr
- _getpaCurrentBluetoothDeviceSupportingTransparencyAccommodationsSymbolLoc.ptr
- _getpaCurrentRouteSupportsTransparencyAccommodationsSymbolLoc.ptr
- _keypath_setTm
- _malloc
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$listeningMode
- _objc_msgSend$sslEnabledForAddress:
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
- _objectdestroy.69Tm
- _objectdestroy.75Tm
- _objectdestroy.90Tm
- _objectdestroy.94Tm
- _server.onceToken.442
- _soft_paBluetoothDeviceSupportsSSL
- _soft_paBluetoothDeviceSupportsSSL.cold.1
- _soft_paCurrentRouteSupportsTransparencyAccommodations
- _soft_paCurrentRouteSupportsTransparencyAccommodations.cold.1
- _swift_makeBoxUnique
CStrings:
+ "$defaultActor"
+ "$includeEnvironmentInSceneDescriptions"
+ "$limitSceneDescriptionsToSingleImage"
+ "$preferredOneShotSource"
+ "$topicEnablementDeadlines"
+ "%@-%llx"
+ "-[AXEventProcessor initWithHIDTapIdentifier:HIDEventTapPriority:shouldMonitorHIDEventsOnly:shouldSeparateHIDStreamsBySenderID:systemEventTapIdentifier:systemEventTapPriority:]"
+ "/Library/Caches/com.apple.xbs/7C126D7A-075C-4FD4-8FBE-1C3F919E1EFC/TemporaryDirectory.OP8WH1/Sources/AccessibilityFrameworks/Source/AXDeviceMonitor.m"
+ "/Library/Caches/com.apple.xbs/7C126D7A-075C-4FD4-8FBE-1C3F919E1EFC/TemporaryDirectory.OP8WH1/Sources/AccessibilityFrameworks/Source/AccessibilityUtilities/AXAssertion.m"
+ "/Library/Caches/com.apple.xbs/7C126D7A-075C-4FD4-8FBE-1C3F919E1EFC/TemporaryDirectory.OP8WH1/Sources/AccessibilityFrameworks/Source/AccessibilityUtilities/AXDevice.m"
+ "/Library/Caches/com.apple.xbs/7C126D7A-075C-4FD4-8FBE-1C3F919E1EFC/TemporaryDirectory.OP8WH1/Sources/AccessibilityFrameworks/Source/AccessibilityUtilities/AXDialectMap.m"
+ "/Library/Caches/com.apple.xbs/7C126D7A-075C-4FD4-8FBE-1C3F919E1EFC/TemporaryDirectory.OP8WH1/Sources/AccessibilityFrameworks/Source/AccessibilityUtilities/AXDisplayLinkManager.m"
+ "/Library/Caches/com.apple.xbs/7C126D7A-075C-4FD4-8FBE-1C3F919E1EFC/TemporaryDirectory.OP8WH1/Sources/AccessibilityFrameworks/Source/AccessibilityUtilities/AXEventProcessor.m"
+ "/Library/Caches/com.apple.xbs/7C126D7A-075C-4FD4-8FBE-1C3F919E1EFC/TemporaryDirectory.OP8WH1/Sources/AccessibilityFrameworks/Source/AccessibilityUtilities/AXEventRepresentation.m"
+ "/Library/Caches/com.apple.xbs/7C126D7A-075C-4FD4-8FBE-1C3F919E1EFC/TemporaryDirectory.OP8WH1/Sources/AccessibilityFrameworks/Source/AccessibilityUtilities/AXEventTapManager.m"
+ "/Library/Caches/com.apple.xbs/7C126D7A-075C-4FD4-8FBE-1C3F919E1EFC/TemporaryDirectory.OP8WH1/Sources/AccessibilityFrameworks/Source/AccessibilityUtilities/AXIPCClient.m"
+ "/Library/Caches/com.apple.xbs/7C126D7A-075C-4FD4-8FBE-1C3F919E1EFC/TemporaryDirectory.OP8WH1/Sources/AccessibilityFrameworks/Source/AccessibilityUtilities/AXIPCMessage.m"
+ "/Library/Caches/com.apple.xbs/7C126D7A-075C-4FD4-8FBE-1C3F919E1EFC/TemporaryDirectory.OP8WH1/Sources/AccessibilityFrameworks/Source/AccessibilityUtilities/AXIPCServer.m"
+ "/Library/Caches/com.apple.xbs/7C126D7A-075C-4FD4-8FBE-1C3F919E1EFC/TemporaryDirectory.OP8WH1/Sources/AccessibilityFrameworks/Source/AccessibilityUtilities/AXLanguageManager.m"
+ "/Library/Caches/com.apple.xbs/7C126D7A-075C-4FD4-8FBE-1C3F919E1EFC/TemporaryDirectory.OP8WH1/Sources/AccessibilityFrameworks/Source/AccessibilityUtilities/AXLocalization.m"
+ "/Library/Caches/com.apple.xbs/7C126D7A-075C-4FD4-8FBE-1C3F919E1EFC/TemporaryDirectory.OP8WH1/Sources/AccessibilityFrameworks/Source/AccessibilityUtilities/AXOrator.m"
+ "/Library/Caches/com.apple.xbs/7C126D7A-075C-4FD4-8FBE-1C3F919E1EFC/TemporaryDirectory.OP8WH1/Sources/AccessibilityFrameworks/Source/AccessibilityUtilities/AXReplayableGesture.m"
+ "/Library/Caches/com.apple.xbs/7C126D7A-075C-4FD4-8FBE-1C3F919E1EFC/TemporaryDirectory.OP8WH1/Sources/AccessibilityFrameworks/Source/AccessibilityUtilities/AXReplayer.m"
+ "/Library/Caches/com.apple.xbs/7C126D7A-075C-4FD4-8FBE-1C3F919E1EFC/TemporaryDirectory.OP8WH1/Sources/AccessibilityFrameworks/Source/AccessibilityUtilities/AXSpringBoardServer.m"
+ "/Library/Caches/com.apple.xbs/7C126D7A-075C-4FD4-8FBE-1C3F919E1EFC/TemporaryDirectory.OP8WH1/Sources/AccessibilityFrameworks/Source/AccessibilityUtilities/AXSwitchRecipe.m"
+ "/Library/Caches/com.apple.xbs/7C126D7A-075C-4FD4-8FBE-1C3F919E1EFC/TemporaryDirectory.OP8WH1/Sources/AccessibilityFrameworks/Source/Settings/AXAssistiveTouchSettings.m"
+ "/Library/Caches/com.apple.xbs/7C126D7A-075C-4FD4-8FBE-1C3F919E1EFC/TemporaryDirectory.OP8WH1/Sources/AccessibilityFrameworks/Source/Settings/AXSettings.m"
+ "@48@0:8@16i24B28B32@36i44"
+ "@60@0:8@?16@24i32B36B40@44@?52"
+ "AFM Plus Response"
+ "AXAirPodSettingsManager.m"
+ "AXAssistiveTouchIconTypeDisplayAppearance"
+ "AXLiveOnExport_liveRecognitionVQA_"
+ "AXSettings"
+ "Archiving failed: "
+ "Automatic"
+ "Class getHUAccessoryCompatibilityUtilitiesClass(void)_block_invoke"
+ "Class getHUAccessoryManagerClass(void)_block_invoke"
+ "Classic ImgCap Response"
+ "Could not create LiveOn collection directory for topic '%s'. %@"
+ "Could not delete export URL after archiving: %@"
+ "Could not extract file: %s. %@"
+ "Could not purge LiveOn collection directory for topic '%s'. %@"
+ "Failed to move archiveURL: "
+ "Found %ld items to extract"
+ "Found BT device: %d, %d, isAirPods: %d, isBeats: %d"
+ "HUAccessoryCompatibilityUtilities"
+ "HUAccessoryManager"
+ "HoverTypingContentSize"
+ "Library/Accessibility/LiveOn/Collection/liveRecognitionVQA"
+ "Live Recognition VQA"
+ "LiveOnCollectionSettingsTopicEnablementDeadlines"
+ "LiveRecognitionIncludeEnvironmentInSceneDescriptions"
+ "LiveRecognitionLimitSceneDescriptionsToSingleImage"
+ "LiveRecognitionPreferredOneShotSource"
+ "No content found to extract"
+ "TB,N,V_shouldSeparateHIDStreamsBySenderID"
+ "_$includeEnvironmentInSceneDescriptions_Storage"
+ "_$limitSceneDescriptionsToSingleImage_Storage"
+ "_$lock_includeEnvironmentInSceneDescriptions"
+ "_$lock_limitSceneDescriptionsToSingleImage"
+ "_$lock_preferredOneShotSource"
+ "_$lock_topicEnablementDeadlines"
+ "_$preferredOneShotSource_Storage"
+ "_$topicEnablementDeadlines_Storage"
+ "_TtC22AccessibilityUtilities25AXLiveOnCollectionManager"
+ "_TtCC22AccessibilityUtilities25AXLiveOnCollectionManagerP33_D8726E7DC8A860BC324A391CEA7FFF7624LiveOnCollectionSettings"
+ "_TtCE22AccessibilityUtilitiesCSo10AXSettings15LiveRecognition"
+ "_shouldSeparateHIDStreamsBySenderID"
+ "appearance.darkmode"
+ "ask.sheet.option.dark.mode"
+ "classicImageCaptionResponse"
+ "com.apple.NanoUniverse.AegirProxyApp.AegirPoster:V01-Earth-Full"
+ "com.apple.NanoUniverse.AegirProxyApp.AegirPoster:V02-Moon-Full"
+ "com.apple.Posters.WeatherPosterApp.WeatherPoster:weather-poster-gallery"
+ "com.apple.PridePoster.PridePosterExtension:grid"
+ "contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:"
+ "coordinateAccessWithIntents:queue:byAccessor:"
+ "createZippedArchive(_:)"
+ "deviceIsAirPodsWithAXSettings:"
+ "deviceIsBeatsDevice:"
+ "deviceIsBeatsProductWithAXSettings:"
+ "fileExistsAtPath:"
+ "getCurrentRouteSupportingHeadphoneAccommodationsWithCompletion:"
+ "getSSLEnabledForAddress:withCompletion:"
+ "getSSLSupportStateForAddress:withCompletion:"
+ "hoverTypingContentSize"
+ "initWithHIDTapIdentifier:HIDEventTapPriority:shouldMonitorHIDEventsOnly:shouldSeparateHIDStreamsBySenderID:systemEventTapIdentifier:systemEventTapPriority:"
+ "installEventTap:identifier:type:skipDeviceMatching:shouldSeparateHIDStreamsBySenderID:filterEvents:matchingServiceHandler:"
+ "liveRecognition"
+ "liveRecognitionVQA"
+ "moveItemAtURL:toURL:error:"
+ "readingIntentWithURL:options:"
+ "setHoverTypingContentSize:"
+ "setShouldSeparateHIDStreamsBySenderID:"
+ "settings"
+ "shouldSeparateHIDStreamsBySenderID"
+ "v16@?0@\"NSError\"8"
+ "v44@?0@\"NSDictionary\"8Q16@\"NSString\"24B32Q36"
+ "yyyy-MM-dd_HH-mm-ss"
- "-[AXEventProcessor initWithHIDTapIdentifier:HIDEventTapPriority:shouldMonitorHIDEventsOnly:systemEventTapIdentifier:systemEventTapPriority:]"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityFrameworks/Source/AXDeviceMonitor.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityFrameworks/Source/AccessibilityUtilities/AXAssertion.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityFrameworks/Source/AccessibilityUtilities/AXDevice.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityFrameworks/Source/AccessibilityUtilities/AXDialectMap.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityFrameworks/Source/AccessibilityUtilities/AXDisplayLinkManager.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityFrameworks/Source/AccessibilityUtilities/AXEventProcessor.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityFrameworks/Source/AccessibilityUtilities/AXEventRepresentation.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityFrameworks/Source/AccessibilityUtilities/AXEventTapManager.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityFrameworks/Source/AccessibilityUtilities/AXIPCClient.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityFrameworks/Source/AccessibilityUtilities/AXIPCMessage.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityFrameworks/Source/AccessibilityUtilities/AXIPCServer.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityFrameworks/Source/AccessibilityUtilities/AXLanguageManager.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityFrameworks/Source/AccessibilityUtilities/AXLocalization.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityFrameworks/Source/AccessibilityUtilities/AXOrator.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityFrameworks/Source/AccessibilityUtilities/AXReplayableGesture.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityFrameworks/Source/AccessibilityUtilities/AXReplayer.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityFrameworks/Source/AccessibilityUtilities/AXSpringBoardServer.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityFrameworks/Source/AccessibilityUtilities/AXSwitchRecipe.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityFrameworks/Source/Settings/AXAssistiveTouchSettings.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityFrameworks/Source/Settings/AXSettings.m"
- "7420"
- "AegirPoster:V01-Earth-Full"
- "AegirPoster:V02-Moon-Full"
- "BOOL soft_paBluetoothDeviceSupportsSSL(BluetoothDevice *__strong)"
- "BOOL soft_paCurrentRouteSupportsTransparencyAccommodations(void)"
- "BluetoothDevice *soft_paCurrentBluetoothDeviceSupportingTransparencyAccommodations(void)"
- "CollectionsPoster:7420"
- "Found BT device: %d, %d"
- "PridePosterExtension:grid"
- "VoiceOverRotorItems"
- "listeningMode"
- "paBluetoothDeviceSupportsSSL"
- "paCurrentBluetoothDeviceSupportingTransparencyAccommodations"
- "paCurrentRouteSupportsTransparencyAccommodations"
- "poster:weather-poster-gallery"
- "resetInitialTouchCountValueForHidStreamIdentifier:"
- "sslEnabledForAddress:"

```
