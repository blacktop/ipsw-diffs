## audioaccessoryd

> `/usr/libexec/audioaccessoryd`

```diff

 30.59.1.9.0
-  __TEXT.__text: 0x1e9550
+  __TEXT.__text: 0x1f5704
   __TEXT.__auth_stubs: 0x2ad0
-  __TEXT.__objc_stubs: 0x16e80
-  __TEXT.__objc_methlist: 0xb6c4
-  __TEXT.__const: 0x39d0
-  __TEXT.__gcc_except_tab: 0x4a4c
-  __TEXT.__cstring: 0x3fad3
-  __TEXT.__objc_classname: 0xa1f
-  __TEXT.__objc_methname: 0x22a9d
-  __TEXT.__objc_methtype: 0x3266
+  __TEXT.__objc_stubs: 0x18160
+  __TEXT.__objc_methlist: 0xbafc
+  __TEXT.__const: 0x39e0
+  __TEXT.__gcc_except_tab: 0x4e18
+  __TEXT.__cstring: 0x426c3
+  __TEXT.__objc_classname: 0xa26
+  __TEXT.__objc_methname: 0x24089
+  __TEXT.__objc_methtype: 0x327c
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__oslogstring: 0x83ca
   __TEXT.__ustring: 0x10
-  __TEXT.__constg_swiftt: 0x190c
+  __TEXT.__constg_swiftt: 0x1954
   __TEXT.__swift5_typeref: 0x1844
   __TEXT.__swift5_builtin: 0xa0
-  __TEXT.__swift5_reflstr: 0x17db
-  __TEXT.__swift5_fieldmd: 0x1664
+  __TEXT.__swift5_reflstr: 0x187b
+  __TEXT.__swift5_fieldmd: 0x16c4
   __TEXT.__swift5_assocty: 0x168
   __TEXT.__swift5_proto: 0x350
   __TEXT.__swift5_types: 0xf0
   __TEXT.__swift5_capture: 0x193c
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_mpenum: 0x14
-  __TEXT.__unwind_info: 0x54c8
+  __TEXT.__unwind_info: 0x5748
   __TEXT.__eh_frame: 0x2070
   __DATA_CONST.__auth_got: 0x1578
-  __DATA_CONST.__got: 0xc38
+  __DATA_CONST.__got: 0xc98
   __DATA_CONST.__auth_ptr: 0x570
-  __DATA_CONST.__const: 0xa7d8
-  __DATA_CONST.__cfstring: 0x9540
+  __DATA_CONST.__const: 0xaab8
+  __DATA_CONST.__cfstring: 0x9a60
   __DATA_CONST.__objc_classlist: 0x2f0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x140

   __DATA_CONST.__objc_arraydata: 0x2f0
   __DATA_CONST.__objc_dictobj: 0x500
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0x19e70
-  __DATA.__objc_selrefs: 0x7618
-  __DATA.__objc_ivar: 0x1454
-  __DATA.__objc_data: 0x2a08
+  __DATA.__objc_const: 0x1a1f0
+  __DATA.__objc_selrefs: 0x7a70
+  __DATA.__objc_ivar: 0x1498
+  __DATA.__objc_data: 0x2a68
   __DATA.__data: 0x4218
-  __DATA.__bss: 0x6ac0
-  __DATA.__common: 0x380
+  __DATA.__bss: 0x6ad0
+  __DATA.__common: 0x398
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 96D2E1C1-7AE1-320A-95D0-D8C065F70F5C
-  Functions: 9055
-  Symbols:   1225
-  CStrings:  14147
+  UUID: 6279CE43-94DC-3CC7-87D1-11E5D3DB59E7
+  Functions: 9285
+  Symbols:   1237
+  CStrings:  14596
 
Symbols:
+ _FBSOpenApplicationOptionKeyPromptUnlockDevice
+ _OBJC_CLASS_$_AAOVADSensorInfo
+ _OBJC_CLASS_$_CBProductInfo
+ _OBJC_CLASS_$_DRClientManager
+ _OBJC_CLASS_$_EKEvent
+ _OBJC_CLASS_$_EKEventStore
+ _OBJC_CLASS_$_NSDateInterval
+ _OBJC_CLASS_$_PKPassLibrary
+ _OBJC_CLASS_$_PKPassRelevantDate
+ _OBJC_CLASS_$_SGEventMetadata
+ _OBJC_CLASS_$__LTTranslationToolKit
+ __LTTranslationErrorDomain
CStrings:
+ "### SRDataRelay: Add data types failed, %{error}"
+ "### SRDataRelay: Remove data types failed, %{error}"
+ "### XPC receive Personal Translation message failed: %@"
+ "%s event is deprecated"
+ "+[AAChargingManager handleChangeOfDynamicEndOfChargeState:forDevice:]"
+ ", HK Data Wr %s"
+ ", HRM Cap %s"
+ ", deoc Cap %s"
+ ", deoc En %s"
+ ", haV2 Cap %s"
+ ", heartRateMonitorCapability: "
+ ", hpPPE Cap %s"
+ ", hpPPE En %s"
+ "-[AAChargingManager _deocTempDisableIntervalAACPMessageIfNeededForDevice:]"
+ "-[AAChargingManager _isFlightEventWithId:]"
+ "-[AAChargingManager _loadUserTempDisableDEOCIntervals]"
+ "-[AAChargingManager _persistUserTempDisableDEOCIntervals]"
+ "-[AAChargingManager _walletTravelInterval]"
+ "-[AAChargingManager deocTempDisableIntervalAACPMessageWithInterval:]"
+ "-[AAController _personalTranslationMessageReceived:fromDevice:]"
+ "-[AAController _personalTranslationMessageReceived:fromDevice:]_block_invoke"
+ "-[AAController sendDEOCTempDisableIntervalMessage:destinationIdentifier:completionHandler:]_block_invoke"
+ "-[AADeviceManagerDaemon _sendDEOCTempDisableIntervalIfNeeded:]_block_invoke"
+ "-[AADeviceManagerDaemon _sendEnableDEOCIfNeeded:]"
+ "-[AADeviceManagerDaemon _sendEnableDEOCIfNeeded:]_block_invoke"
+ "-[AAFeatureOnboarding _deocNotificationShownForDeviceWithBluetoothAddress:]"
+ "-[AAFeatureOnboarding _deocNotificationShownForDeviceWithBluetoothAddress:]_block_invoke"
+ "-[AAFeatureOnboarding _dismissFitEducationNotificationForDisconnectedDevice:]"
+ "-[AAFeatureOnboarding _fitEducationNotificationsShownForDevice:]"
+ "-[AAFeatureOnboarding _incrementFitEducationNotificationsShownForIdentifier:]"
+ "-[AAFeatureOnboarding _launchDEOCProxCardForDeviceWithBTAddress:]"
+ "-[AAFeatureOnboarding _launchDEOCProxCardForDeviceWithBTAddress:]_block_invoke"
+ "-[AAFeatureOnboarding _launchDEOCProxCardForDeviceWithBTAddress:]_block_invoke_3"
+ "-[AAFeatureOnboarding _loadPreferences]"
+ "-[AAFeatureOnboarding _postDEOCOnboardingIfNeeded:]"
+ "-[AAFeatureOnboarding _presentDeocNotification:]_block_invoke_2"
+ "-[AAFeatureOnboarding _receivedAssetManagerNotificationAction:forDevice:withAddress:]"
+ "-[AAFeatureOnboarding _receivedDEOCNotificationAction:forDeviceWithAddress:]"
+ "-[AAFeatureOnboarding _receivedFitEducationNotificationAction:forDevice:withAddress:]"
+ "-[AAFeatureOnboarding _saveFitEducationNotificationsShown:withCount:]_block_invoke"
+ "-[AAFeatureOnboarding showAssetManagerShowDownloadNotificationForDevice:withErrorHandler:]_block_invoke"
+ "-[AAFeatureOnboarding showAssetManagerShowDownloadNotificationForDevice:withErrorHandler:]_block_invoke_4"
+ "-[AAFeatureOnboarding showFitEducationNotificationForIdentifier:withErrorHandler:]_block_invoke_2"
+ "-[AAFeatureOnboarding showFitEducationNotificationForIdentifier:withErrorHandler:]_block_invoke_4"
+ "-[AAGestureControl _handleDualBudLongPressGesture]"
+ "-[AAGestureControl _handleDualBudLongPressGesture]_block_invoke"
+ "-[AASensorServiceDaemon _aaControllerEnsureStarted]_block_invoke_3"
+ "-[AASensorServiceDaemon _personalTranslationMessageReceived:fromDeviceAddress:]_block_invoke"
+ "-[AAServicesXPCConnection assetManagerShowDownloadNotificationForBTAddress:completionHandler:]_block_invoke_2"
+ "-[AAServicesXPCConnection systemStateMonitorShowFitEducationNotificationForIdentifier:completionHandler:]_block_invoke_2"
+ "-[BTServicesDaemon _audioQualityShowBanner:title:deviceAddressString:messageKey:messageArgs:timeoutSeconds:]_block_invoke"
+ "-[BTServicesDaemon openRadarforAudioQuality]"
+ "-[BTSmartRoutingDaemon _dataRelayAddRequestedDataTypesForServer:]_block_invoke"
+ "-[BTSmartRoutingDaemon _dataRelayAddRequestedDataTypesForServer:]_block_invoke_2"
+ "-[BTSmartRoutingDaemon _dataRelayClientMonitorEnsureStarted]"
+ "-[BTSmartRoutingDaemon _dataRelayClientMonitorEnsureStarted]_block_invoke_2"
+ "-[BTSmartRoutingDaemon _dataRelayClientMonitorEnsureStarted]_block_invoke_5"
+ "-[BTSmartRoutingDaemon _dataRelayRemoveRequestedDataTypesForServer:]_block_invoke"
+ "-[BTSmartRoutingDaemon _dataRelayRemoveRequestedDataTypesForServer:]_block_invoke_2"
+ "-[BTSmartRoutingDaemon _evaluateNearbyHRMDevice:]"
+ "-[BTSmartRoutingDaemon _handleFitnessPlusDRServerTeardown]_block_invoke"
+ "-[BTSmartRoutingDaemon _prewarmAudioAccessoriesForFitnessWorkout]"
+ "-[BTSmartRoutingDaemon _selectHRMCapableDeviceFromDiscoveredDevices]_block_invoke"
+ "-[BTSmartRoutingDaemon _workoutStateChanged]_block_invoke"
+ "-[BTSmartRoutingDaemon _workoutStateChanged]_block_invoke_2"
+ "-[BTSmartRoutingDaemon dataRelayAddAvailableDataTypesWithDevice:]"
+ "-[BTSmartRoutingDaemon dataRelayAddAvailableDataTypesWithDiscoveredDevice:]"
+ "-[BTSmartRoutingDaemon dataRelayRemoveAvailableDataTypesWithDevice:]"
+ "-[BTSmartRoutingDaemon dataRelayRemoveAvailableDataTypesWithDiscoveredDevice:]"
+ "-[SRConnectionManager _isHRMHeadphoneEligibleForTipiV2:]_block_invoke"
+ "-[SRConnectionManager _isHRMHeadphonePrerequisiteMet:connectType:]_block_invoke"
+ "-[SRConnectionManager evaluateNearbyHRMDeviceForConnection:]"
+ "-[SRWxDevice checkDataRelayServerPublishEligibility]"
+ "1551854"
+ "815886"
+ "@\"DRClientManager\""
+ "AAAssetManagerNotificationUserNotifications"
+ "AADynamicEndOfChargeTrainingUserNotifications"
+ "AAFeatureOnboardingDynamicEndOfCharge"
+ "AAFitEducationNotificationUserNotifications"
+ "ATV is not DR compatible"
+ "Active HRM device elected"
+ "Adding available data types for server %@"
+ "Adding available data types with discovered device for server %@"
+ "AirPods3,4"
+ "Asset Download notification not shown due to %{error}"
+ "Asset Download notification shown for btAddress %@"
+ "AssetManager download notification delivered. deviceId: %@"
+ "AssetManager download notification not delivered. deviceId: %@, error: %@"
+ "Bad source BT address: %@"
+ "BatteryDEOC"
+ "Bluetooth Audio Quality Feedback"
+ "Both"
+ "Bringing down Fitness+ server %@"
+ "CBLocalizable"
+ "Check Data Relay Server Publish eligibility routed %s isHRMCapable %s otherDeviceIsNotIdle %s isDeviceRoutedAndStreamingFromTipiDevice %s, dataRelayServerPublished %s isWorkoutActive %s"
+ "Clearing temporarily disabled DEOC for device: %@"
+ "CoreBluetooth - HFP Audio | iOS"
+ "Creating DEOC temp disable interval AACP message from: %@"
+ "DEOC Notification: failed to save prox card version for onboarding notification error %@"
+ "DEOC Notification: saving prox card version"
+ "DEOC enabled sent to device: %@"
+ "DEOC not enabled for device: %@"
+ "DEOC onboarding notification delivered. deviceId: %@, notificationId: %@"
+ "DEOC onboarding prox card dismissed: %@"
+ "DEOC onboarding prox launched: %@"
+ "DEOC onboarding was not delivered. deviceId: %@, error: %@"
+ "DEOC_ONBOARDING_BODY_FORMAT"
+ "DEOC_ONBOARDING_TITLE"
+ "DR Server found"
+ "DR Server lost"
+ "Data Relay Server discovery start"
+ "Data types added to DR Server when found"
+ "Device added %@"
+ "Device address not found in notification userinfo: %@"
+ "Device charging DEOC is missing BT Address: %@"
+ "Device doesn't support fit education notice action"
+ "Device is NOT charging DEOC for the first time, caching onboarding: %@"
+ "Device is charging DEOC for the first time: %@"
+ "Device is charging DEOC, already onboarded: %@"
+ "Device isn't connected, skip showing fit education notification"
+ "Device not an iPhone, iPad or Watch platform, ineligible for DR"
+ "Device1,22034"
+ "Device1,8232"
+ "Device1,8233"
+ "Device1,8239"
+ "Dismiss fit education notification for %@ as device disconnected"
+ "Dual Click Hold"
+ "DualBudLongPress"
+ "Dynamic End of Charging Engaged"
+ "DynamicEndOfCharge"
+ "Eligible for DR from nearby ATV isAllowedFromNearbyDevice %s isAllowedFromPairedDevice %s"
+ "Enabling DEOC on first connection after paring device: %@"
+ "EvaluateNearbyHRMDevice wx %@ TipiConnect %s"
+ "FIT_EDUCATION_BODY_FORMAT"
+ "FIT_EDUCATION_TITLE"
+ "Failed to deserialize user temp disable deoc intervals: %@"
+ "Failed to enable DEOC: %@"
+ "Failed to send DEOC Temp disable interval: %@"
+ "Failed to serialize user temp disable DEOC intervals '%@' for map: %@"
+ "Fit Education Notification threshold met"
+ "Fit education notification delivered. deviceId: %@"
+ "Fit education notification not delivered. deviceId: %@, error: %@"
+ "Fit education notification not shown due to %{error}"
+ "Fit education notification shown for identifier %@"
+ "Fit education notification: Saved fit education notification"
+ "Fit education notification: failed to save fit education notification count for device %@ error %@"
+ "Fit education threshold : %d"
+ "Fit education threshold override off"
+ "Found %lu passes"
+ "Found DR Server %@"
+ "Found DR Server to remove data types %@"
+ "Found Fitness+ server %@"
+ "Found flight event from %@-%@"
+ "Found pass with relevant dates: %@ - %@"
+ "HRM Capability changed, saving device record: %@"
+ "HRM not available"
+ "HRM not supported"
+ "HearingAidV2"
+ "HearingProtectionPPE"
+ "HeartRate"
+ "Identifier not found in notification userinfo: %@"
+ "Incremented fit education notifications shown value for device %@ to %d"
+ "Invalid PT inMessageData"
+ "IsHRMHeadphoneEligibleForTipiV2: Skip, Wx %@ reason: %@"
+ "Keywords"
+ "Launching DEOC prox card for device: %@"
+ "Localizable-Translation"
+ "No address found for received PT message"
+ "No paired device found"
+ "No passes with relevant dates"
+ "No prox card record exists for device %@"
+ "No temp disable interval, checking for travel event."
+ "No travel event, DEOC disable interval not needed."
+ "Other tipi device is not DR compatible"
+ "PERSONAL_TRANSLATOR_READY_BODY"
+ "PERSONAL_TRANSLATOR_READY_TITLE"
+ "PT inMessageData subtype %d signalState %d"
+ "Performance"
+ "Personal Translation message received: source %@, data <%@>"
+ "Prox card record for device %@ %@"
+ "Removing available data types for server %@"
+ "Removing available data types with discovered device for server %@"
+ "Returning without playing error tone as client has already played it"
+ "SRDataRelay Add data types success"
+ "SRDataRelay Remove data types success"
+ "Selected discovered device as HRM %@"
+ "Sent DEOC Temp disable interval to device with identifier: %@"
+ "T@\"AAProxCardHandler\",&,N,V_deocProxCardHandler"
+ "T@\"NSMutableDictionary\",&,N,V_fitEducationNotificationIdsForDeviceIds"
+ "T@\"NSMutableSet\",&,N,V_deocOnboardedDeviceIdentifiers"
+ "T@?,C,N,V_personalTranslationMessageHandler"
+ "TC,N,V_dynamicEndOfChargeCapability"
+ "TC,N,V_enableDynamicEndOfCharge"
+ "TC,N,V_enableHearingProtectionPPE"
+ "TC,N,V_hearingAidV2SourceRegionSupport"
+ "TC,N,V_heartRateMonitorCapability"
+ "TC,N,VhaRegionStatusV2"
+ "TC,N,VheartRateMonitorCapability"
+ "TC,N,VhpPPERegionStatus"
+ "Tc,N,V_dynamicEndOfChargeEnabled"
+ "Tc,N,V_healthKitDataWriteAllowed"
+ "Tq,N,V_fitEducationNotificationThreshold"
+ "URLWithString:"
+ "Unknown PT msg subtype: %d"
+ "User clicked on AssetManager download notification for device: %@, open settings page for device %@ URL %@"
+ "User clicked on Fit Education notification for device: %@, open settings page for device %@ URL %@"
+ "User dismissed AssetManager download notification for device: %@"
+ "User dismissed DEOC notification for device: %@"
+ "User dismissed Fit Education notification for device: %@"
+ "User temp disable DEOC intervals loaded[%lu]: %@"
+ "User temp disable DEOC intervals persisted: %lu total"
+ "User temporarily disabled DEOC for device: %@"
+ "UserTempDisableDEOCIntervals"
+ "_calendarTravelInterval"
+ "_currentUserDidTempDisableDEOCForDevice:"
+ "_currentUserTempDisableDEOCIntervalForIdentifier:"
+ "_dataRelayAddRequestedDataTypesForServer:"
+ "_dataRelayAvailableServerSet"
+ "_dataRelayClientMonitor"
+ "_dataRelayClientMonitorEnsureStarted"
+ "_dataRelayClientMonitorStarted"
+ "_dataRelayRemoveRequestedDataTypesForServer:"
+ "_deocNotificationShownForDeviceWithBluetoothAddress:"
+ "_deocOnboardedDeviceIdentifiers"
+ "_deocProxCardHandler"
+ "_deocTempDisableIntervalAACPMessageIfNeededForDevice:"
+ "_dismissFitEducationNotificationForDisconnectedDevice:"
+ "_dynamicEndOfChargeCapability"
+ "_dynamicEndOfChargeEnabled"
+ "_earliestDateConsideredForDEOCEvent"
+ "_enableDynamicEndOfCharge"
+ "_enableHearingProtectionPPE"
+ "_evaluateNearbyHRMDevice:"
+ "_fitEducationNotificationIdsForDeviceIds"
+ "_fitEducationNotificationThreshold"
+ "_fitEducationNotificationsShownForDevice:"
+ "_handleDualBudLongPressGesture"
+ "_handleDualBudLongPressGesture called"
+ "_handleFitnessPlusDRServerTeardown"
+ "_healthKitDataWriteAllowed"
+ "_hearingAidV2SourceRegionSupport"
+ "_heartRateMonitorCapability"
+ "_incrementFitEducationNotificationsShownForIdentifier:"
+ "_isFlightEventWithId:"
+ "_isHRMHeadphoneEligibleForTipiV2:"
+ "_isHRMHeadphonePrerequisiteMet:connectType:"
+ "_latestDateConsideredForDEOCEvent"
+ "_launchDEOCProxCardForDeviceWithBTAddress:"
+ "_loadUserTempDisableDEOCIntervals"
+ "_nearbyHRMDeviceEligibleToConnectTo"
+ "_nearbyHRMEnabledDevice"
+ "_notificationContentForAssetManagerDownload:"
+ "_notificationContentForDEOCTrainingWithDevice:"
+ "_notificationContentForFitEducationNotificationForDevice:"
+ "_persistUserTempDisableDEOCIntervals"
+ "_personalTranslationMessageHandler"
+ "_personalTranslationMessageReceived:fromDevice:"
+ "_personalTranslationMessageReceived:fromDeviceAddress:"
+ "_postDEOCOnboardingIfNeeded:"
+ "_presentDeocNotification:"
+ "_receivedAssetManagerNotificationAction:forDevice:withAddress:"
+ "_receivedDEOCNotificationAction:forDeviceWithAddress:"
+ "_receivedFitEducationNotificationAction:forDevice:withAddress:"
+ "_removeUserTempDisableDEOCIntervalforIdentifier:"
+ "_saveFitEducationNotificationsShown:withCount:"
+ "_selectHRMCapableDeviceFromDiscoveredDevices"
+ "_sendDEOCTempDisableIntervalIfNeeded:"
+ "_sendEnableDEOCIfNeeded:"
+ "_setUserTempDisableDEOCInterval:forIdentifier:"
+ "_travelIntervalFromCalendarAndWallet"
+ "_userTempDisableDEOCIntervalForIdentifier:"
+ "_userTempDisableDEOCIntervalMap"
+ "_walletTravelInterval"
+ "addAvailableDataTypes:dataTypes:wxAddress:"
+ "addRequestedDataTypes:completion:"
+ "apple_airpods_case"
+ "apple_magic_keyboard"
+ "apple_magic_keyboard_keypad"
+ "apple_magic_keyboard_touch"
+ "apple_magic_keyboard_touch_keypad"
+ "apple_magic_mouse"
+ "apple_magic_trackpad"
+ "apple_mighty_mouse"
+ "apple_wireless_keyboard"
+ "apple_wireless_mouse"
+ "audioQuality - File Radar"
+ "audioQuality banner timeout"
+ "audioQuality user click, openradar"
+ "audioQuality user dismiss"
+ "audioQuality: banner action: %s, %{error}"
+ "audioQuality: banner error for device %@"
+ "availableDataTypes"
+ "availableDataTypesFromServer"
+ "bundleWithIdentifier:"
+ "calendar"
+ "categoryDescription"
+ "changeDynamicEndOfChargeState"
+ "chargingDEOC"
+ "com.apple.CoreBluetooth"
+ "dataRelayAddAvailableDataTypesWithDevice:"
+ "dataRelayAddAvailableDataTypesWithDiscoveredDevice:"
+ "dataRelayRemoveAvailableDataTypesWithDevice:"
+ "dataRelayRemoveAvailableDataTypesWithDiscoveredDevice:"
+ "deoE"
+ "deoc"
+ "deocOnboardedDeviceIdentifiers"
+ "deocProxCardHandler"
+ "deocTempDisableIntervalAACPMessageIfNeededForDevice:"
+ "deocTempDisableIntervalAACPMessageWithInterval:"
+ "distantFuture"
+ "distantPast"
+ "dynamicEndOfChargeCapability"
+ "dynamicEndOfChargeEnabled"
+ "dynamicEndOfChargeNotification"
+ "dynamicEndOfChargeNotificationVersion"
+ "dynamicEndOfChargeState"
+ "dynamicEndOfChargeTempDisabled"
+ "eDec"
+ "earliestDate"
+ "enableDynamicEndOfCharge"
+ "enableHearingProtectionPPE"
+ "endDate"
+ "evaluateNearbyHRMDeviceForConnection:"
+ "eventMetadataFromEKEvent:"
+ "eventObjectIDsMatchingPredicate:"
+ "findDateFromDates:option:"
+ "fitEducationNotificationIdsForDeviceIds"
+ "fitEducationNotificationThreshold"
+ "fitEducationNotificationsShownOverride"
+ "flight"
+ "hV2R"
+ "haRegionStatusV2"
+ "haRegionStatusV2: "
+ "haV2"
+ "handleChangeOfDynamicEndOfChargeState:forDevice:"
+ "hearingAidV2SourceRegionSupport"
+ "heartRateMonitorCapability"
+ "heartRateMonitorCapabilityChanged"
+ "heartRateMonitorCapabilityValueOriginatedFromDevice"
+ "hpPPERegionStatus"
+ "hpPPERegionStatus: "
+ "hrCp"
+ "initWithBTAddress:"
+ "initWithEKOptions:"
+ "initWithStartDate:endDate:"
+ "isAllDay"
+ "laterDate:"
+ "latestDate"
+ "localizedCaseInsensitiveContainsString:"
+ "openSensitiveURL:withOptions:"
+ "passesOfStyles:"
+ "personalTranslationMessageHandler"
+ "personalTranslator"
+ "personalTranslatorVersion"
+ "ppeC"
+ "ppeE"
+ "ppeL"
+ "predicateForEventsWithStartDate:endDate:calendars:loadDefaultProperties:"
+ "productInfoWithProductID:"
+ "publicObjectWithObjectID:"
+ "relevantDates"
+ "removeAvailableDataTypes:dataTypes:wxAddress:"
+ "removeRequestedDataTypes:completion:"
+ "requestedDataTypes"
+ "send DEOCTempDisableInterval message to destination %@"
+ "sendDEOCTempDisableIntervalMessage:destinationIdentifier:completionHandler:"
+ "serverLostHandler"
+ "setChangeDynamicEndOfChargeState:"
+ "setDeocOnboardedDeviceIdentifiers:"
+ "setDeocProxCardHandler:"
+ "setDisconnectHandler:"
+ "setDynamicEndOfChargeCapability:"
+ "setDynamicEndOfChargeEnabled:"
+ "setDynamicEndOfChargeNotificationVersion:"
+ "setDynamicEndOfChargeTempDisabled:"
+ "setEnableDynamicEndOfCharge:"
+ "setEnableHearingProtectionPPE:"
+ "setFitEducationNotificationIdsForDeviceIds:"
+ "setFitEducationNotificationThreshold:"
+ "setHaRegionStatusV2:"
+ "setHearingAidV2SourceRegionSupport:"
+ "setHeartRateMonitorCapability:"
+ "setHeartRateMonitorCapabilityChanged:"
+ "setHpPPERegionStatus:"
+ "setPersonalTranslationMessageHandler:"
+ "setPersonalTranslatorVersion:"
+ "setServerFoundHandler:"
+ "setServerLostHandler:"
+ "setUserTempDisableDEOCIntervalMap:"
+ "settings-navigation://com.apple.Settings.Bluetooth/HeadphoneDetail/?identifier=%@&Selection=heartRateSensorSpecifierID"
+ "settings-navigation://com.apple.Settings.Bluetooth/HeadphoneDetail/AboutFitFeature/?identifier=%@"
+ "settings-navigation://com.apple.Settings.Bluetooth/HeadphoneDetail/LiveTranslation-LanguageDownload/?identifier=%@"
+ "showAssetManagerShowDownloadNotificationForDevice:withErrorHandler:"
+ "showFitEducationNotificationForIdentifier:withErrorHandler:"
+ "startDate"
+ "startPersonalTranslationSession returned with error %@"
+ "startPersonalTranslationSession:"
+ "suggestionInfo"
+ "upcomingEventIDs"
+ "update:"
+ "updateDevice:withOBCState:deocTempDisabled:"
+ "userTempDisableDEOCIntervalMap"
+ "v16@?0@\"DRServer\"8"
+ "v32@0:8@16c24c28"
+ "v32@?0@\"NSString\"8@\"DRServer\"16^B24"
+ "visibleBatteryCombinedLeftRight"
+ "visibleBatteryLeft"
+ "visibleBatteryRight"
+ "wallet"
- "-[AASensorServiceDaemon _aaControllerEnsureStarted]_block_invoke_2"
- "Platform not supported for Asset Download notification"
- "Platform not supported for fit education notification"
- "updateDevice:withOBCState:"
- "v28@0:8@16c24"

```
