## carkitd

> `/usr/libexec/carkitd`

```diff

-746.24.2.0.0
-  __TEXT.__text: 0x8ae8c
-  __TEXT.__auth_stubs: 0x14c0
-  __TEXT.__objc_stubs: 0x108a0
-  __TEXT.__objc_methlist: 0x750c
-  __TEXT.__const: 0x244
-  __TEXT.__cstring: 0x612a
-  __TEXT.__gcc_except_tab: 0x1f54
-  __TEXT.__objc_methname: 0x16d2c
-  __TEXT.__oslogstring: 0xf69d
-  __TEXT.__objc_classname: 0x107c
-  __TEXT.__objc_methtype: 0x447f
+774.8.0.0.0
+  __TEXT.__text: 0x92d24
+  __TEXT.__auth_stubs: 0x1460
+  __TEXT.__objc_stubs: 0x10da0
+  __TEXT.__objc_methlist: 0x75fc
+  __TEXT.__const: 0x242
+  __TEXT.__gcc_except_tab: 0x1ec4
+  __TEXT.__cstring: 0x6052
+  __TEXT.__objc_classname: 0x10ab
+  __TEXT.__objc_methname: 0x176db
+  __TEXT.__oslogstring: 0x1042d
+  __TEXT.__objc_methtype: 0x4697
   __TEXT.__dlopen_cstrs: 0x16e
-  __TEXT.__swift5_typeref: 0xca
   __TEXT.__constg_swiftt: 0x74
-  __TEXT.__swift5_reflstr: 0x45
+  __TEXT.__swift5_typeref: 0xca
   __TEXT.__swift5_fieldmd: 0x44
-  __TEXT.__swift5_capture: 0x30
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x1ed8
+  __TEXT.__swift5_reflstr: 0x45
+  __TEXT.__swift5_capture: 0x30
+  __TEXT.__unwind_info: 0x2258
   __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__auth_got: 0xa70
-  __DATA_CONST.__got: 0x880
+  __DATA_CONST.__auth_got: 0xa40
+  __DATA_CONST.__got: 0x8e0
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA_CONST.__const: 0x31a8
-  __DATA_CONST.__cfstring: 0x6f60
-  __DATA_CONST.__objc_classlist: 0x2a8
+  __DATA_CONST.__const: 0x3258
+  __DATA_CONST.__cfstring: 0x6fc0
+  __DATA_CONST.__objc_classlist: 0x290
   __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x248
+  __DATA_CONST.__objc_protolist: 0x258
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xa8
-  __DATA_CONST.__objc_superrefs: 0x1d8
-  __DATA_CONST.__objc_intobj: 0x8e8
+  __DATA_CONST.__objc_superrefs: 0x1d0
+  __DATA_CONST.__objc_intobj: 0x900
   __DATA_CONST.__objc_arraydata: 0x968
   __DATA_CONST.__objc_arrayobj: 0xc0
   __DATA_CONST.__objc_floatobj: 0x10
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x13a60
-  __DATA.__objc_selrefs: 0x4c18
-  __DATA.__objc_ivar: 0x754
-  __DATA.__objc_data: 0x1b70
-  __DATA.__data: 0x1ab8
+  __DATA.__objc_const: 0x13b68
+  __DATA.__objc_selrefs: 0x4da0
+  __DATA.__objc_ivar: 0x784
+  __DATA.__objc_data: 0x1a80
+  __DATA.__data: 0x1b80
   __DATA.__bss: 0x148
   __DATA.__common: 0x18
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 582ADBDA-611C-3C69-83F6-DD9088CFCA52
-  Functions: 3101
-  Symbols:   631
-  CStrings:  7292
+  UUID: 8F58A219-AD50-3C3A-B80F-D3E75E39F69D
+  Functions: 3153
+  Symbols:   638
+  CStrings:  7431
 
Symbols:
+ _CAREventPayload
+ _CAREventType
+ _CARSessionVideoPlaybackAvailabilityChangedNotification
+ _CRZoomFactorKey
+ _CarVideoLogging
+ _OBJC_CLASS_$_CARSessionRequestBonjourHost
+ _OBJC_CLASS_$_CARSessionRequestDisplayConfiguration
+ _OBJC_CLASS_$_CREnhancedSiriOverrides
+ _OBJC_CLASS_$_CRSubtitleStyle
+ _OBJC_CLASS_$_DNDModeAssertionService
+ _OBJC_CLASS_$_DNDMutableModeAssertionDetails
+ _OBJC_CLASS_$_NSMutableIndexSet
+ _OBJC_CLASS_$_NSPropertyListSerialization
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x10
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
CStrings:
+ "@\"<CRVideoFocusModeDelegate>\""
+ "@\"<CRVideoPropertyKeyObserving>\""
+ "@\"CRVideoProperties\""
+ "@\"DNDModeAssertion\""
+ "@\"DNDModeAssertionService\""
+ "@16@?0@\"CRSubtitleStyle\"8"
+ "@16@?0@\"NSDictionary\"8"
+ "@64@0:8B16@20@28B36B40B44B48B52B56B60"
+ "@72@0:8@16@24@32@40@48q56@64"
+ "CARAnalytics: payload information for connectionSessionFailure event was nil or empty. Unable to submit."
+ "CARAnalytics: sent connectionSessionFailure event"
+ "CRVideoFocusModeDelegate"
+ "CRVideoProperties"
+ "CRVideoPropertyKeyObserving"
+ "CarPlay onboarding/welcome confirmed"
+ "CarkitdAdditions"
+ "Connection success -- cleaning failure"
+ "Consolidated %lu intermediate iAP events into CARiAPAuthComplete payload for event type %@"
+ "Consolidating CARiAP2EndpointCreated timestamp into payload"
+ "Consolidating CARiAPAuthStarted timestamp into payload"
+ "Consolidating CARiAPNCMStart timestamp into payload"
+ "Consolidating CARiAPStartSessionReceived timestamp into payload"
+ "Extracted iAP2EndpointCreated from consolidated payload: %@"
+ "Extracted iAPAuthStarted from consolidated payload: %@"
+ "Extracted iAPStartSessionReceived from consolidated payload: %@"
+ "Invalid failure information provided - missing required keys or empty dictionary"
+ "Invalid information provided around session failure. Check dictionary information provided or that vehicle information from session was present at time of call."
+ "Onboarding CarPlay"
+ "Recording vehicle information of current session"
+ "Session failure information recorded: %@"
+ "T@\"<CRVideoFocusModeDelegate>\",W,N,V_focusModeDelegate"
+ "T@\"<CRVideoPropertyKeyObserving>\",W,N,V_keyObserver"
+ "T@\"CRVideoProperties\",R,N,V_properties"
+ "T@\"DNDModeAssertion\",&,N,V_focusModeAssertion"
+ "T@\"DNDModeAssertionService\",&,N,V_dndAssertionService"
+ "T@\"NSArray\",C,N,V_customSubtitleStyles"
+ "T@\"NSDictionary\",&,N,V_sessionFailureInformation"
+ "T@\"NSDictionary\",&,N,V_vehicleInformation"
+ "T@\"NSNumber\",C,N,V_focusModeEnabled"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_analysisQueue"
+ "T@\"NSString\",C,N,V_selectedSubtitleStyle"
+ "TB,R,N,V_supportsDolbyAtmos"
+ "TB,R,N,V_supportsEnhancedSiriVoice"
+ "TB,R,N,V_supportsLiveActivities"
+ "TB,R,N,V_supportsSiriMixable"
+ "TB,R,N,V_supportsSpatialAudio"
+ "TB,R,N,V_supportsVideoPlayback"
+ "TQ,N,V_nextPropertiesMessageID"
+ "Transitioning pairing step from: [%{public}@] to [%{public}@]"
+ "Unable to coalesce failure information - missing required vehicle information"
+ "Using iAP2EndpointCreated from individual event: %@"
+ "Using iAPAuthStarted from individual event: %@"
+ "Using iAPStartSessionReceived from individual event: %@"
+ "[DISPLAY_CONFIGURATION] Adding displayScaleMode=%ld to CARSessionRequestHost for vehicle %@"
+ "[DISPLAY_CONFIGURATION] Adding zoomFactor=%@ from capabilities for vehicle %@"
+ "[DISPLAY_CONFIGURATION] Adding zoomFactor=%@ to CARSessionRequestHost for vehicle %@"
+ "[DISPLAY_CONFIGURATION] BLE session: creating CARSessionRequestHost with displayScaleMode=%ld, zoomFactor=%@ for vehicle %@"
+ "[DISPLAY_CONFIGURATION] BLE session: fetched zoomFactor=%@ from capabilities for vehicle %@"
+ "[DISPLAY_CONFIGURATION] Building displayConfig for vehicle %@: displayScaleMode=%ld"
+ "[DISPLAY_CONFIGURATION] Starting USB Bonjour advertising with host: %@"
+ "[DISPLAY_CONFIGURATION] Starting WIFI Bonjour advertising with host: %@"
+ "[DISPLAY_CONFIGURATION] fetchCarPlayControlAdvertisingForUSBWithReply: Requested advertising with host"
+ "[DISPLAY_CONFIGURATION] fetchCarPlayControlAdvertisingForUSBWithReply: YES for vehicle %@"
+ "[DISPLAY_CONFIGURATION] fetchCarPlayControlAdvertisingForUSBWithReply: _isRestricted, should not advertise"
+ "[DISPLAY_CONFIGURATION] fetchCarPlayControlAdvertisingForWiFiUUID: nil UUID"
+ "[DISPLAY_CONFIGURATION] fetchCarPlayControlAdvertisingForWiFiUUID: yes"
+ "[DISPLAY_CONFIGURATION] fetchCarPlayControlAdvertisingForWiFiUUID:%@ CarPlay restricted"
+ "_analysisQueue"
+ "_channelQueue_handlePropertiesMessage:"
+ "_channelQueue_handleRequestForPropertyKeys:messageID:"
+ "_channelQueue_sendPropertiesMessage:asReplyForMessageID:"
+ "_consolidateCurrentSessionIAPEventsInPlace:sessionIdentifier:transportType:"
+ "_consolidateIAPEventsForTransport:"
+ "_customSubtitleStyles"
+ "_dndAssertionService"
+ "_focusModeAssertion"
+ "_focusModeDelegate"
+ "_focusModeEnabled"
+ "_handleVideoAvailablilityChanged:"
+ "_invalidSessionFailureInformationError"
+ "_invalidateFocusModeAssertion"
+ "_keyObserver"
+ "_nextPropertiesMessageID"
+ "_notifyObserverOfValue:forPropertyKey:isInitialValue:"
+ "_presentOnboarding:"
+ "_properties"
+ "_selectedSubtitleStyle"
+ "_sessionFailureInformation"
+ "_supportsDolbyAtmos"
+ "_supportsEnhancedSiriVoice"
+ "_supportsLiveActivities"
+ "_supportsSiriMixable"
+ "_supportsSpatialAudio"
+ "_supportsVideoPlayback"
+ "_updateRestrictedModeAuthorizationsForVehicle:"
+ "_vehicleInformation"
+ "addIndex:"
+ "analysisQueue"
+ "applied updated restricted mode authorizations"
+ "applyUpdatedRestrictedModeAuthorizations:forCertificateSerial:completion:"
+ "applying updated restricted mode authorizations: %lu vehicleID: %@"
+ "bs_compactMap:"
+ "bs_map:"
+ "carkitd"
+ "changedProperties"
+ "com.apple.airplay"
+ "com.apple.airplay.jarvisParametersChanged"
+ "com.apple.carkit.connectionAnalysisQueue"
+ "com.apple.carplay.video"
+ "completedFirstConnection"
+ "connectionSessionFailure"
+ "controlMessage"
+ "couldn't decode properties request: %@"
+ "customSubtitleStyles"
+ "dataWithPropertyList:format:options:error:"
+ "didSetInitialValue:forPropertyKey:"
+ "didUpdateValue:forPropertyKey:"
+ "dismiss/finished"
+ "dismissing pairing flow due to restriction"
+ "dndAssertionService"
+ "dolbyAtmosAudioSupported"
+ "failed to apply updated restricted mode authorizations: %@"
+ "failed to enabled focus mode: %@"
+ "failed to encode properties message: %@"
+ "failed to invalidate focus mode assertion: %@"
+ "fetchCarPlayControlAdvertisingForUSBWithReply:"
+ "fetchCarPlayControlAdvertisingForWiFiUUID:%@ didn't match criteria for vehicle %@"
+ "fetchCarPlayControlAdvertisingForWiFiUUID:reply:"
+ "fetchEnhancedSiriOverridesWithCompletion:"
+ "fetched enhanced Siri overrides: %{public}@"
+ "focusModeAssertion"
+ "focusModeDelegate"
+ "focusModeEnabled"
+ "indexSet"
+ "initWithDisplayConfiguration:"
+ "initWithDisplayName:authenticationCertificateSerial:pairedVehicleIdentifier:wiFiUUID:bleStartSessionMessage:displayScaleMode:zoomFactor:"
+ "initWithDisplayName:wiredIPv6Addresses:wirelessIPv6Addresses:port:carplayWiFiUUID:deviceIdentifier:publicKey:sourceVersion:supportsMutualAuthentication:authenticationCertificateSerial:pairedVehicleIdentifier:wiredCarPlaySimulator:remoteDeviceConnected:displayScaleMode:zoomFactor:"
+ "initWithDisplayScaleMode:zoomFactor:"
+ "initWithSupportsRouteSharing:userVisibleReason:brand:supportsVideoPlayback:supportsLodWidgets:supportsSiriMixable:supportsEnhancedSiriVoice:supportsDolbyAtmos:supportsSpatialAudio:supportsLiveActivities:"
+ "initWithVoiceTriggerMode:timestampOffset:language:"
+ "insertObjects:atIndexes:"
+ "invalidateActiveModeAssertionWithError:"
+ "jarvisOverrideLanguage"
+ "jarvisTimestampRollback"
+ "jarvisVoiceModelLanguage"
+ "jarvisVoiceTriggerMode"
+ "keyObserver"
+ "kind"
+ "language"
+ "messageID"
+ "nextPropertiesMessageID"
+ "no property values to send in response"
+ "params"
+ "posted enhanced Siri settings changed"
+ "presentOnboardingForVehicleName:features:appClipIDs:confirmationHandler:"
+ "presentOnboardingPromptForVehicleName:features:appClipIDs:confirmationHandler:"
+ "properties request did not have any keys: %@"
+ "property"
+ "propertyChanged"
+ "propertyListWithData:options:format:error:"
+ "property_key_captionstyles_customstyles"
+ "property_key_captionstyles_selectedstyle"
+ "property_key_dndButtonState"
+ "reached onboarding without waiting on the session first!"
+ "received request for custom subtitle styles: %@"
+ "received request for focus mode, enabled: %@"
+ "received request for properties: %@"
+ "received request for selected subtitle style: %@"
+ "received request for unknown key: %@"
+ "received set for custom subtitle styles: %@"
+ "received set for focus mode, enabled: %@"
+ "received set for selected style: %@"
+ "received set for unknown key: %@"
+ "removeObjectsAtIndexes:"
+ "response"
+ "restrictedModeAuthorizations"
+ "restrictedModeAuthorizations: %lu"
+ "restrictedModeAuthorizations: matching vehicle is not paired"
+ "restrictedModeAuthorizations: no matching vehicle"
+ "restrictedModeAuthorizationsForCertificateSerial: nil"
+ "restrictedModeAuthorizationsForCertificateSerial:reply:"
+ "selectedSubtitleStyle"
+ "sendConnectionSessionFailureInformation:completion:"
+ "sender"
+ "sending initial property %{public}@ : %@"
+ "sending properties message data: %@"
+ "sending properties message: %@"
+ "sending property update %{public}@ : %@"
+ "sessionConnectionFailureWithPayload:"
+ "sessionFailureInformation"
+ "setAnalysisQueue:"
+ "setCompletedFirstConnection:"
+ "setCustomSubtitleStyles:"
+ "setDndAssertionService:"
+ "setEnhancedSiriOverrides:completion:"
+ "setFocusModeAssertion:"
+ "setFocusModeDelegate:"
+ "setFocusModeEnabled:"
+ "setKeyObserver:"
+ "setNextPropertiesMessageID:"
+ "setProperty"
+ "setReason:"
+ "setSelectedSubtitleStyle:"
+ "setSessionFailureInformation:"
+ "setSupportsEnhancedSiriVoice:"
+ "setValue:forPropertyKey:"
+ "setVehicleInformation:"
+ "setting enhanced Siri overrides: %{public}@"
+ "setting focus mode %{public}@"
+ "spatialAudioSupported"
+ "startAdvertisingCarPlayControlForUSBWithHost:"
+ "startAdvertisingCarPlayControlForWiFiUUID:host:"
+ "supportsDolbyAtmos"
+ "supportsEnhancedSiriVoice"
+ "supportsLiveActivities"
+ "supportsRouteSharing: %@, supportsVideoPlayback: %@, supportsLodWidgets: %@, supportsSiriMixable:%@, supportsEnhancedSiriVoice: %@, supportsDolbyAtmos: %@, supportsSpatialAudio: %@, supportsLiveActivities: %@"
+ "supportsSpatialAudio"
+ "supportsVideoPlayback"
+ "takeModeAssertionWithDetails:error:"
+ "timestampOffset"
+ "unhandled properties message: %@"
+ "v24@0:8@?<v@?@\"CREnhancedSiriOverrides\"@\"NSError\">16"
+ "v24@0:8@?<v@?B@\"CARSessionRequestBonjourHost\"@\"NSError\">16"
+ "v32@0:8@\"CREnhancedSiriOverrides\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"NSDictionary\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?B@\"CARSessionRequestBonjourHost\"@\"NSError\">24"
+ "v32@0:8@16@\"NSString\"24"
+ "v40@0:8@16@24q32"
+ "v48@0:8@\"NSString\"16Q24@\"NSArray\"32@?<v@?B>40"
+ "v48@0:8@16Q24@32@?40"
+ "valueForPropertyKey:"
+ "values"
+ "videoPlaybackAvailable"
+ "videoWantsFocusModeEnabled:"
- "@40@0:8B16@20@28B36"
- "CROutstandingVehiclePairingAlert"
- "CROutstandingWiredVehicleApprovalAlert"
- "CROutstandingWirelessVehicleApprovalAlert"
- "CRVehicleEnhancedIntegrationAlert"
- "Doesn't support wired BT pairing."
- "ENHANCED_INTEGRATION_ALERT_ACCEPT"
- "ENHANCED_INTEGRATION_ALERT_CANCEL"
- "ENHANCED_INTEGRATION_ALERT_MESSAGE"
- "ENHANCED_INTEGRATION_ALERT_TITLE_%@"
- "Enhanced integration alert cancelled"
- "PAIRING_CARPLAY_ALERT_ACCEPT"
- "PAIRING_CARPLAY_ALERT_DECLINE"
- "PAIRING_CARPLAY_ALERT_DONTUSE"
- "PAIRING_CARPLAY_ALERT_MESSAGE_IPHONE"
- "PAIRING_CARPLAY_ALERT_MESSAGE_IPHONE_BT_ON"
- "PAIRING_CARPLAY_ALERT_NOTNOW"
- "PAIRING_CARPLAY_ALERT_TITLE_%@"
- "PAIRING_CARPLAY_ALERT_TITLE_GENERIC"
- "Presented Wired BT pairing alert"
- "Presented approval alert"
- "Presenting enhanced integration alert"
- "REMEMBER_CARPLAY_ALERT_ACCEPT"
- "REMEMBER_CARPLAY_ALERT_CANCEL"
- "REMEMBER_CARPLAY_ALERT_MESSAGE_IPHONE"
- "REMEMBER_CARPLAY_ALERT_TITLE_%@"
- "REMEMBER_CARPLAY_ALERT_TITLE_GENERIC"
- "Supports USB - setting USB decline type."
- "T@\"NSMutableArray\",&,N,V_outstandingApprovalAlerts"
- "T@\"NSMutableArray\",&,N,V_outstandingEnhancedIntegrationAlerts"
- "T@\"NSMutableArray\",&,N,V_outstandingPairingAlerts"
- "TB,N,V_shouldEnableBluetooth"
- "TB,N,V_shouldEnableWiFi"
- "TQ,N,V_declineType"
- "Temporary vehicle removed."
- "USE_CARPLAY_ALERT_ACCEPT"
- "USE_CARPLAY_ALERT_ACCEPT_WIFI_ON"
- "USE_CARPLAY_ALERT_CANCEL"
- "USE_CARPLAY_ALERT_MESSAGE_WIRELESS_IPHONE"
- "USE_CARPLAY_ALERT_TITLE_%@"
- "USE_CARPLAY_ALERT_TITLE_GENERIC"
- "Unable to remove temporary vehicle %@"
- "VideoSettings"
- "Wired BT pairing alert cancelled"
- "Wired BT powering on"
- "_currentlyConnectedVehicleSupportsMixableAudio"
- "_declineType"
- "_declineTypeForOOBPairingMessagingVehicle:"
- "_dismissApprovalAlertForMessagingVehicle:"
- "_dismissApprovalAlerts"
- "_dismissEnhancedIntegrationAlertForMessagingVehicle:"
- "_dismissEnhancedIntegrationAlerts"
- "_dismissPairingAlertForMessagingVehicle:"
- "_dismissPairingAlerts"
- "_isVehicleActionable:"
- "_outstandingApprovalAlerts"
- "_outstandingEnhancedIntegrationAlerts"
- "_outstandingPairingAlerts"
- "_presentApprovalUsingAlertsForMessagingVehicle:"
- "_presentAssetReadyPromptWithCompletion:"
- "_presentEnhancedIntegrationAlertForMessagingVehicle:"
- "_presentWiredBluetoothPairingAlertForMessagingVehicle:storedVehicle:"
- "_shouldEnableBluetooth"
- "_shouldEnableWiFi"
- "approval alert accepted"
- "approval alert cancelled"
- "approval alert declined"
- "asset ready"
- "asset ready prompt was confirmed"
- "com.apple.carkit.enhancedIntegrationAlert"
- "com.apple.carkit.vehicleApprovalAlert"
- "com.apple.carkit.wiredBTApprovalAlert"
- "declineType"
- "finished"
- "initWithDisplayName:authenticationCertificateSerial:pairedVehicleIdentifier:wiFiUUID:bleStartSessionMessage:"
- "initWithDisplayName:wiredIPv6Addresses:wirelessIPv6Addresses:port:carplayWiFiUUID:deviceIdentifier:publicKey:sourceVersion:supportsMutualAuthentication:authenticationCertificateSerial:pairedVehicleIdentifier:wiredCarPlaySimulator:remoteDeviceConnected:"
- "initWithSupportsRouteSharing:userVisibleReason:brand:supportsLodWidgets:"
- "isCarPlaySetupEnabled"
- "next pairing step: [%{public}@]"
- "outstandingApprovalAlerts"
- "outstandingEnhancedIntegrationAlerts"
- "outstandingPairingAlerts"
- "presentAssetReadyForVehicleName:appClipIDs:confirmationHandler:"
- "presentAssetReadyPromptForVehicleName:appClipIDs:confirmationHandler:"
- "setDeclineType:"
- "setOutstandingApprovalAlerts:"
- "setOutstandingEnhancedIntegrationAlerts:"
- "setOutstandingPairingAlerts:"
- "setShouldEnableBluetooth:"
- "setShouldEnableWiFi:"
- "shouldEnableBluetooth"
- "shouldEnableWiFi"
- "startAdvertisingCarPlayControlForUSB"
- "startAdvertisingCarPlayControlForWiFiUUID:"
- "supportsRouteSharing: %@, supportsLodWidgets: %@"
- "v40@0:8@\"NSString\"16@\"NSArray\"24@?<v@?>32"

```
