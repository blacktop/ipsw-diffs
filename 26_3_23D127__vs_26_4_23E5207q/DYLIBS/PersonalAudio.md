## PersonalAudio

> `/System/Library/PrivateFrameworks/PersonalAudio.framework/PersonalAudio`

```diff

-496.4.8.0.0
-  __TEXT.__text: 0x14f50
-  __TEXT.__auth_stubs: 0x510
-  __TEXT.__objc_methlist: 0xd90
-  __TEXT.__const: 0x118
-  __TEXT.__gcc_except_tab: 0x460
-  __TEXT.__cstring: 0x12a6
-  __TEXT.__oslogstring: 0xb8e
-  __TEXT.__dlopen_cstrs: 0x1c1
-  __TEXT.__unwind_info: 0x590
+496.13.0.0.0
+  __TEXT.__text: 0x1512c
+  __TEXT.__auth_stubs: 0x4e0
+  __TEXT.__objc_methlist: 0xea8
+  __TEXT.__const: 0x110
+  __TEXT.__gcc_except_tab: 0x39c
+  __TEXT.__cstring: 0x1247
+  __TEXT.__oslogstring: 0xc39
+  __TEXT.__dlopen_cstrs: 0x163
+  __TEXT.__unwind_info: 0x5e8
   __TEXT.__objc_classname: 0xdb
-  __TEXT.__objc_methname: 0x2fda
-  __TEXT.__objc_methtype: 0x40b
-  __TEXT.__objc_stubs: 0x2e40
-  __DATA_CONST.__got: 0x198
-  __DATA_CONST.__const: 0x940
+  __TEXT.__objc_methname: 0x32b7
+  __TEXT.__objc_methtype: 0x419
+  __TEXT.__objc_stubs: 0x2e60
+  __DATA_CONST.__got: 0x190
+  __DATA_CONST.__const: 0x720
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe50
+  __DATA_CONST.__objc_selrefs: 0xe98
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0x298
+  __AUTH_CONST.__auth_got: 0x280
   __AUTH_CONST.__const: 0x300
-  __AUTH_CONST.__cfstring: 0x1740
-  __AUTH_CONST.__objc_const: 0xf78
+  __AUTH_CONST.__cfstring: 0x1500
+  __AUTH_CONST.__objc_const: 0x1038
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0xa0
+  __AUTH.__data: 0x18
+  __DATA.__objc_ivar: 0xa8
   __DATA.__data: 0xc0
-  __DATA.__bss: 0xc0
+  __DATA.__bss: 0x98
   __DATA_DIRTY.__objc_data: 0x320
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0xe0
+  __DATA_DIRTY.__bss: 0xd0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 21252DD3-FE2B-3306-99E6-4A10794D07C9
-  Functions: 447
-  Symbols:   1693
-  CStrings:  1111
+  UUID: 932021CC-DC75-308B-B241-C47DD23BAAAE
+  Functions: 437
+  Symbols:   1634
+  CStrings:  1077
 
Symbols:
+ -[PAConfiguration audiogramValidForPSE]
+ -[PAConfiguration setAudiogramValidForPSE:]
+ -[PADatabaseManager _currentConfigurations]
+ -[PADatabaseManager contentDidUpdateRemotely:]
+ -[PADatabaseManager currentPMEConfiguration]
+ -[PADatabaseManager currentPSEConfiguration]
+ -[PADatabaseManager savePMEConfiguration:pseConfiguration:]
+ -[PADatabaseManager updatePersonalAudioSettings]
+ -[PAEnrollmentNode isEnrollingPSE]
+ -[PAEnrollmentNode setIsEnrollingPSE:]
+ -[PAHMSManager regionSupportsHearingAssistForAddress:]
+ -[PASettings customTransparencyConfigurationByRouteUID]
+ -[PASettings customTransparencyConfigurationForRouteUID:]
+ -[PASettings customTransparencyConfiguration]
+ -[PASettings personalMediaAutomationMockAudiogramAvailable]
+ -[PASettings personalMediaAutomationMockNonYodelRegion]
+ -[PASettings personalMediaAutomationMockTransparencyAvailable]
+ -[PASettings personalMediaAutomationMockTransparencyCustomized]
+ -[PASettings setCustomTransparencyConfiguration:]
+ -[PASettings setCustomTransparencyConfiguration:forRouteUID:]
+ -[PASettings setCustomTransparencyConfigurationByRouteUID:]
+ -[PASettings setPersonalMediaAutomationMockAudiogramAvailable:]
+ -[PASettings setPersonalMediaAutomationMockNonYodelRegion:]
+ -[PASettings setPersonalMediaAutomationMockTransparencyAvailable:]
+ -[PASettings setPersonalMediaAutomationMockTransparencyCustomized:]
+ GCC_except_table12
+ GCC_except_table15
+ GCC_except_table50
+ GCC_except_table51
+ _HMHealthKitUtilitiesFunction
+ _HealthKitLibrary
+ _HearingModeService_PrivateLibrary.sLib
+ _HearingModeService_PrivateLibrary.sOnce
+ _OBJC_IVAR_$_PAConfiguration._audiogramValidForPSE
+ _OBJC_IVAR_$_PAEnrollmentNode._isEnrollingPSE
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _PARegionSupportsHearingAid
+ _PARegionSupportsHearingAid.cold.1
+ __AXSAutomationEnabled
+ ___43-[PADatabaseManager _currentConfigurations]_block_invoke
+ ___59-[PADatabaseManager savePMEConfiguration:pseConfiguration:]_block_invoke
+ ___73+[PAAudiogramUtilities normalizedOffsetsFromLeftOffsets:andRightOffsets:]_block_invoke.52
+ ___HearingModeService_PrivateLibrary_block_invoke
+ ___block_descriptor_72_e8_32s40s48r56r64r_e5_v8?0ls32l8s40l8r48l8r56l8r64l8
+ ___block_literal_global.39
+ ___block_literal_global.56
+ ___block_literal_global.60
+ ___block_literal_global.77
+ ___block_literal_global.83
+ ___getHKFeatureIdentifierHearingAidSymbolLoc_block_invoke
+ _classHMHealthKitUtilities
+ _getHKFeatureIdentifierHearingAidSymbolLoc.ptr
+ _getHMHealthKitUtilitiesClass
+ _initHMHealthKitUtilities
+ _initHMHealthKitUtilities.cold.1
+ _objc_autorelease
+ _objc_msgSend$_currentConfigurations
+ _objc_msgSend$audiogramValidForPSE
+ _objc_msgSend$currentPMEConfiguration
+ _objc_msgSend$currentPSEConfiguration
+ _objc_msgSend$customTransparencyConfiguration
+ _objc_msgSend$customTransparencyConfigurationByRouteUID
+ _objc_msgSend$customTransparencyConfigurationForRouteUID:
+ _objc_msgSend$decodeBoolForKey:
+ _objc_msgSend$encodeBool:forKey:
+ _objc_msgSend$getRegionSupportStatusForFeatureID:
+ _objc_msgSend$hearingAssistRegionStatus
+ _objc_msgSend$isEnrollingPSE
+ _objc_msgSend$personalMediaAutomationMockNonYodelRegion
+ _objc_msgSend$personalMediaAutomationMockTransparencyAvailable
+ _objc_msgSend$setAudiogramValidForPSE:
+ _objc_msgSend$setCustomTransparencyConfiguration:
+ _objc_msgSend$setCustomTransparencyConfiguration:forRouteUID:
+ _objc_msgSend$setCustomTransparencyConfigurationByRouteUID:
+ _objc_msgSend$setIsEnrollingPSE:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$updatePersonalAudioSettings
+ _objc_retain_x26
+ _objc_retain_x27
- -[PADatabaseManager currentConfiguration]
- -[PADatabaseManager saveConfiguration:]
- GCC_except_table10
- GCC_except_table27
- GCC_except_table28
- GCC_except_table39
- GCC_except_table40
- GCC_except_table42
- GCC_except_table48
- GCC_except_table49
- _OBJC_CLASS_$_BluetoothManager
- _PAAudioRouteBluetoothProductIdentifierAirPods
- _PAAudioRouteBluetoothProductIdentifierAirPods2
- _PAAudioRouteBluetoothProductIdentifierAirPodsPro
- _PAAudioRouteBluetoothProductIdentifierB463
- _PAAudioRouteBluetoothProductIdentifierB494
- _PAAudioRouteBluetoothProductIdentifierB494b
- _PAAudioRouteBluetoothProductIdentifierB498
- _PAAudioRouteBluetoothProductIdentifierB515
- _PAAudioRouteBluetoothProductIdentifierB515c
- _PAAudioRouteBluetoothProductIdentifierB607
- _PAAudioRouteBluetoothProductIdentifierB688
- _PAAudioRouteBluetoothProductIdentifierB698
- _PAAudioRouteBluetoothProductIdentifierB698C
- _PAAudioRouteBluetoothProductIdentifierB768che
- _PAAudioRouteBluetoothProductIdentifierB768e
- _PAAudioRouteBluetoothProductIdentifierB768m
- _PAAudioRouteBluetoothProductIdentifierB788
- _PAAudioRouteBluetoothProductIdentifierBeatsSolo
- _PAAudioRouteBluetoothProductIdentifierBeatsSoloPro
- _PAAudioRouteBluetoothProductIdentifierBeatsStudio
- _PAAudioRouteBluetoothProductIdentifierBeatsStudio2
- _PAAudioRouteBluetoothProductIdentifierBeatsX
- _PAAudioRouteBluetoothProductIdentifierPowerbeats
- _PAAudioRouteBluetoothProductIdentifierPowerbeats2
- _PAAudioRouteBluetoothProductIdentifierPowerbeats4
- _PAAudioRouteBluetoothProductIdentifierPowerbeatsPro
- ___39-[PADatabaseManager saveConfiguration:]_block_invoke
- ___41-[PADatabaseManager currentConfiguration]_block_invoke
- ___73+[PAAudiogramUtilities normalizedOffsetsFromLeftOffsets:andRightOffsets:]_block_invoke.123
- ___block_descriptor_32_e32_B32?0"BluetoothDevice"8Q16^B24l
- ___block_descriptor_40_e8_32bs_e22_v16?0"NSDictionary"8ls32l8
- ___block_descriptor_40_e8_32bs_e5_v8?0ls32l8
- ___block_descriptor_40_e8_32r_e15_v32?0816^B24lr32l8
- ___block_descriptor_40_e8_32s_e22_B24?0"NSString"8^B16ls32l8
- ___block_descriptor_40_e8_32s_e32_B32?0"BluetoothDevice"8Q16^B24ls32l8
- ___block_descriptor_48_e8_32s40s_e29_v32?0"NSDictionary"8Q16^B24ls32l8s40l8
- ___block_descriptor_57_e8_32s40s48s_e15_v32?0816^B24ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48r56r_e5_v8?0lr48l8s32l8s40l8r56l8
- ___block_literal_global.127
- ___block_literal_global.169
- ___block_literal_global.27
- ___block_literal_global.76
- ___getHURouteKeyAudioRouteName_HeadphoneSymbolLoc_block_invoke
- ___getHURouteKeyAudioRouteName_HeadsetSymbolLoc_block_invoke
- ___getHURouteKeyAudioRouteSubTypeSymbolLoc_block_invoke
- ___getHURouteKeyBTDetails_ProductIDSymbolLoc_block_invoke
- ___getHURouteKeyRouteCurrentlyPickedSymbolLoc_block_invoke
- ___getHURouteKeyRouteNameSymbolLoc_block_invoke
- ___getHURouteKeyRouteUIDSymbolLoc_block_invoke
- ___getHUUtilitiesClass_block_invoke
- ___getHUUtilitiesClass_block_invoke.cold.1
- ___paAvailableBluetoothDevicesSupportingTransparencyAccommodations_block_invoke
- ___paAvailableBluetoothDevicesSupportingTransparencyAccommodations_block_invoke_2
- ___paCurrentBluetoothDeviceSupportingANCAndHeadphoneAccommodations_block_invoke
- ___paCurrentBluetoothDeviceSupportingTransparencyAccommodationsAsync_block_invoke
- ___paCurrentBluetoothDeviceSupportingTransparencyAccommodations_block_invoke
- ___paCurrentRouteSupportingAudioAccommodationsAsync_block_invoke
- ___paCurrentRouteSupportsAudioAccommodationsAsync_block_invoke
- ___paHeadphoneRouteAvailable_block_invoke
- ___paHeadphoneRouteAvailable_block_invoke.cold.1
- ___paHeadphoneRouteAvailable_block_invoke.cold.2
- ___paHeadphoneRouteAvailable_block_invoke.cold.3
- ___paPairedDevicesSupportingTransparencyAccommodations_block_invoke
- ___paRoutesOfSubtypeOrProduct_block_invoke
- ___paRoutesOfSubtypeOrProduct_block_invoke.cold.1
- ___paRoutesOfSubtypeOrProduct_block_invoke.cold.2
- ___paRoutesOfSubtypeOrProduct_block_invoke.cold.3
- ___paRoutesOfSubtypeOrProduct_block_invoke_2
- ___paRoutesOfSubtypeOrProduct_block_invoke_3
- __os_feature_enabled_impl
- _dispatch_async
- _getHURouteKeyAudioRouteName_HeadphoneSymbolLoc.ptr
- _getHURouteKeyAudioRouteName_HeadsetSymbolLoc.ptr
- _getHURouteKeyAudioRouteSubTypeSymbolLoc.ptr
- _getHURouteKeyBTDetails_ProductIDSymbolLoc.ptr
- _getHURouteKeyRouteCurrentlyPickedSymbolLoc.ptr
- _getHURouteKeyRouteNameSymbolLoc.ptr
- _getHURouteKeyRouteUID
- _getHURouteKeyRouteUID.cold.1
- _getHURouteKeyRouteUIDSymbolLoc.ptr
- _getHUUtilitiesClass
- _getHUUtilitiesClass.softClass
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$addObject:
- _objc_msgSend$address
- _objc_msgSend$containsString:
- _objc_msgSend$currentConfiguration
- _objc_msgSend$currentPickableAudioRoutes
- _objc_msgSend$featureCapability:
- _objc_msgSend$getAACPCapabilityInteger:
- _objc_msgSend$hasPrefix:
- _objc_msgSend$indexOfObjectPassingTest:
- _objc_msgSend$indexesOfObjectsPassingTest:
- _objc_msgSend$isAppleAudioDevice
- _objc_msgSend$isTemporaryPaired
- _objc_msgSend$objectsAtIndexes:
- _objc_msgSend$objectsPassingTest:
- _objc_msgSend$pairedDevices
- _objc_msgSend$productId
- _objc_msgSend$setListeningMode:
- _objc_msgSend$sharedUtilities
- _objc_msgSend$stringByReplacingOccurrencesOfString:withString:
- _objc_msgSend$vendorId
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x8
- _objc_retain_x9
- _paAnyRouteSupportsAudioAccommodations
- _paAvailableBluetoothDevicesSupportingTransparencyAccommodations
- _paBluetoothDeviceSupportsSSL
- _paCurrentBluetoothDeviceSupportingANCAndHeadphoneAccommodations
- _paCurrentBluetoothDeviceSupportingTransparencyAccommodations
- _paCurrentBluetoothDeviceSupportingTransparencyAccommodationsAsync
- _paCurrentBluetoothDeviceSupportingTransparencyAccommodations_CC
- _paCurrentRouteSupportingAudioAccommodations
- _paCurrentRouteSupportingAudioAccommodationsAsync
- _paCurrentRouteSupportingTransparencyAccommodations
- _paCurrentRouteSupportsAudioAccommodations
- _paCurrentRouteSupportsAudioAccommodationsAsync
- _paCurrentRouteSupportsTransparencyAccommodations
- _paHeadphoneRouteAvailable
- _paPairedDeviceSupportsTransparencyAccommodations
- _paPairedDevicesSupportingTransparencyAccommodations
- _paProductsIdentifiersSupportingTransparencyAccommodations
- _paProductsIdentifiersSupportingTransparencyAccommodations.AudioRouteProductIDs
- _paRouteOfSubtypeOrProduct
- _paRoutesOfSubtypeOrProduct
- _paSupportedWirelessRoutes
- _paSupportedWirelessRoutes.AudioRouteProductIDs
- _setCurrentDeviceToTransparencyMode
CStrings:
+ "/System/Library/PrivateFrameworks/HearingModeService_Private.framework/HearingModeService_Private"
+ "3"
+ "B32@0:8@16@24"
+ "Database was updated, will update local prefs if not already set."
+ "HKFeatureIdentifierHearingAid"
+ "HMHealthKitUtilities"
+ "Ignoring PSE config update %d, %d"
+ "PAConfigAudiogramValidForPSEKey"
+ "PersonalMediaAutomationMockAudiogramAvailablePreference"
+ "PersonalMediaAutomationMockNonYodelRegionPreference"
+ "PersonalMediaAutomationMockTransparencyAvailablePreference"
+ "PersonalMediaAutomationMockTransparencyCustomized"
+ "Setting custom transparency config from database, since the local pref was unset"
+ "Setting personal media config from database, since the local pref was unset"
+ "TB,N,V_audiogramValidForPSE"
+ "TB,N,V_isEnrollingPSE"
+ "Updating custom transparency configs %@"
+ "_audiogramValidForPSE"
+ "_currentConfigurations"
+ "_isEnrollingPSE"
+ "audiogramValidForPSE"
+ "contentDidUpdateRemotely:"
+ "currentPMEConfiguration"
+ "currentPSEConfiguration"
+ "customTransparencyConfiguration"
+ "customTransparencyConfigurationByRouteUID"
+ "customTransparencyConfigurationForRouteUID:"
+ "decodeBoolForKey:"
+ "encodeBool:forKey:"
+ "getRegionSupportStatusForFeatureID:"
+ "hearingAssistRegionStatus"
+ "isEnrollingPSE"
+ "personalMediaAutomationMockAudiogramAvailable"
+ "personalMediaAutomationMockNonYodelRegion"
+ "personalMediaAutomationMockTransparencyAvailable"
+ "personalMediaAutomationMockTransparencyCustomized"
+ "pmeConfig"
+ "pseConfig"
+ "regionSupportsHearingAssistForAddress:"
+ "savePMEConfiguration:pseConfiguration:"
+ "setAudiogramValidForPSE:"
+ "setCustomTransparencyConfiguration:"
+ "setCustomTransparencyConfiguration:forRouteUID:"
+ "setCustomTransparencyConfigurationByRouteUID:"
+ "setIsEnrollingPSE:"
+ "setObject:forKeyedSubscript:"
+ "setPersonalMediaAutomationMockAudiogramAvailable:"
+ "setPersonalMediaAutomationMockNonYodelRegion:"
+ "setPersonalMediaAutomationMockTransparencyAvailable:"
+ "setPersonalMediaAutomationMockTransparencyCustomized:"
+ "updatePersonalAudioSettings"
- "#"
- "%d,%d"
- "76,8194"
- "76,8195"
- "76,8197"
- "76,8198"
- "76,8201"
- "76,8202"
- "76,8203"
- "76,8204"
- "76,8205"
- "76,8206"
- "76,8207"
- "76,8210"
- "76,8211"
- "76,8212"
- "76,8214"
- "76,8217"
- "76,8219"
- "76,8221"
- "76,8222"
- "76,8223"
- "76,8228"
- "76,8230"
- "76,8231"
- "76,8239"
- ":"
- "B24@?0@\"NSString\"8^B16"
- "B32@?0@\"BluetoothDevice\"8Q16^B24"
- "BluetoothFeatures"
- "Checking route %d = %@"
- "Found PSE version %@"
- "Found transparency devices %@"
- "HURouteKeyAudioRouteName_Headphone"
- "HURouteKeyAudioRouteName_Headset"
- "HURouteKeyAudioRouteSubType"
- "HURouteKeyBTDetails_ProductID"
- "HURouteKeyRouteCurrentlyPicked"
- "HURouteKeyRouteName"
- "HURouteKeyRouteUID"
- "HUUtilities"
- "Route not supported %@ - %@ = %@"
- "SSL"
- "Setting ANC for %@"
- "addObject:"
- "address"
- "containsString:"
- "currentConfiguration"
- "currentPickableAudioRoutes"
- "featureCapability:"
- "getAACPCapabilityInteger:"
- "hasPrefix:"
- "indexOfObjectPassingTest:"
- "indexesOfObjectsPassingTest:"
- "isAppleAudioDevice"
- "isTemporaryPaired"
- "objectsAtIndexes:"
- "objectsPassingTest:"
- "pairedDevices"
- "productId"
- "saveConfiguration:"
- "setListeningMode:"
- "sharedUtilities"
- "stringByReplacingOccurrencesOfString:withString:"
- "v16@?0@\"NSDictionary\"8"
- "v32@?0@\"NSDictionary\"8Q16^B24"
- "v32@?0@8@16^B24"
- "vendorId"

```
