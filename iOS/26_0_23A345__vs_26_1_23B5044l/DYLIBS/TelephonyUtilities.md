## TelephonyUtilities

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`

```diff

-1575.100.1.2.16
-  __TEXT.__text: 0x16cea0
+1576.200.36.2.2
+  __TEXT.__text: 0x16e1c0
   __TEXT.__auth_stubs: 0x2370
-  __TEXT.__objc_methlist: 0x1a1d8
-  __TEXT.__cstring: 0x13388
+  __TEXT.__objc_methlist: 0x1a2c8
+  __TEXT.__cstring: 0x13598
   __TEXT.__const: 0x1044
-  __TEXT.__oslogstring: 0x12422
-  __TEXT.__gcc_except_tab: 0x18f4
+  __TEXT.__oslogstring: 0x124f2
+  __TEXT.__gcc_except_tab: 0x1960
   __TEXT.__ustring: 0xde
   __TEXT.__dlopen_cstrs: 0x8df
   __TEXT.__constg_swiftt: 0x578

   __TEXT.__swift_as_ret: 0x84
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x5d60
+  __TEXT.__unwind_info: 0x5de0
   __TEXT.__eh_frame: 0x1378
-  __TEXT.__objc_classname: 0x2727
-  __TEXT.__objc_methname: 0x3c217
-  __TEXT.__objc_methtype: 0x7f13
-  __TEXT.__objc_stubs: 0x20d00
+  __TEXT.__objc_classname: 0x274f
+  __TEXT.__objc_methname: 0x3c4ed
+  __TEXT.__objc_methtype: 0x7f80
+  __TEXT.__objc_stubs: 0x20ec0
   __DATA_CONST.__got: 0xe60
-  __DATA_CONST.__const: 0x3620
+  __DATA_CONST.__const: 0x3678
   __DATA_CONST.__objc_classlist: 0x830
   __DATA_CONST.__objc_catlist: 0xb8
-  __DATA_CONST.__objc_protolist: 0x408
+  __DATA_CONST.__objc_protolist: 0x410
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xaf28
+  __DATA_CONST.__objc_selrefs: 0xafb0
   __DATA_CONST.__objc_protorefs: 0x108
   __DATA_CONST.__objc_superrefs: 0x6b0
   __DATA_CONST.__objc_arraydata: 0x6f8
   __AUTH_CONST.__auth_got: 0x11c8
-  __AUTH_CONST.__const: 0x3128
+  __AUTH_CONST.__const: 0x3188
   __AUTH_CONST.__cfstring: 0x11ca0
-  __AUTH_CONST.__objc_const: 0x28268
+  __AUTH_CONST.__objc_const: 0x283a8
   __AUTH_CONST.__objc_intobj: 0x540
   __AUTH_CONST.__objc_arrayobj: 0x228
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH.__objc_data: 0x26c0
   __AUTH.__data: 0x5e8
-  __DATA.__objc_ivar: 0x17e8
-  __DATA.__data: 0x3320
-  __DATA.__bss: 0x1890
+  __DATA.__objc_ivar: 0x17fc
+  __DATA.__data: 0x3380
+  __DATA.__bss: 0x18b0
   __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x2be8
   __DATA_DIRTY.__data: 0x30

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F0F3DBE5-94D9-3109-BFF2-33BD38047868
-  Functions: 10020
-  Symbols:   29950
-  CStrings:  16406
+  UUID: 463AF421-9FAE-3433-960D-B7A154D296E4
+  Functions: 10058
+  Symbols:   30058
+  CStrings:  16497
 
Symbols:
+ -[TUAudioRoute bluetoothProductIdentifierAsUInt32]
+ -[TUAudioRoute bluetoothProductIdentifierAsUInt32].cold.1
+ -[TUAudioRoute bluetoothProductIdentifierAsUInt32].cold.2
+ -[TUAudioRoute bluetoothProductIdentifierAsUInt32].cold.3
+ -[TUAudioRoute cachedModelIdentifier]
+ -[TUAudioRoute modelIdentifierCached]
+ -[TUAudioRoute modelIdentifier]
+ -[TUAudioRoute modelIdentifier].cold.1
+ -[TUAudioRoute modelIdentifier].cold.2
+ -[TUAudioRoute modelIdentifier].cold.3
+ -[TUAudioRoute modelIdentifier].cold.4
+ -[TUAudioRoute mxBluetoothProductIdentifier]
+ -[TUAudioRoute mxBluetoothProductIdentifier].cold.1
+ -[TUAudioRoute setCachedModelIdentifier:]
+ -[TUAudioRoute setModelIdentifierCached:]
+ -[TUCallCenter validateIMAVPush:]
+ -[TUCallServicesInterface validateIMAVPush:]
+ -[TUConfigurationProvider isCallHapticsAvailable]
+ -[TUConfigurationProvider isCallHapticsEnabled]
+ -[TUConfigurationProvider setCallHapticsEnabled:]
+ -[TUFeatureFlags IMAVSunsetEnabled]
+ -[TUMetadataCache updateCacheWithDestinationIDs:didMakeChanges:]
+ -[TURoute modelIdentifier]
+ -[TURoute setModelIdentifier:]
+ -[TUSmartHoldingEvent confidenceScore]
+ -[TUSmartHoldingEvent initWithType:text:date:confidenceScore:]
+ -[TUSoundPlayer configurationProvider]
+ -[TUUserConfiguration isCallHapticsEnabled]
+ -[TUUserConfiguration setCallHapticsEnabled:]
+ -[TUVideoDeviceControllerProvider invalidateInputDevicesCache]
+ -[TUVideoDeviceControllerProvider queryAVCaptureDeviceWithType:mediaType:position:]
+ GCC_except_table109
+ GCC_except_table112
+ GCC_except_table157
+ GCC_except_table170
+ _AAFMediaTypeXML_block_invoke.once
+ _OBJC_CLASS_$_NSRegularExpression
+ _OBJC_IVAR_$_TUAudioRoute._cachedModelIdentifier
+ _OBJC_IVAR_$_TUAudioRoute._modelIdentifierCached
+ _OBJC_IVAR_$_TURoute._modelIdentifier
+ _OBJC_IVAR_$_TUSmartHoldingEvent._confidenceScore
+ _OBJC_IVAR_$_TUSoundPlayer._configurationProvider
+ _OBJC_IVAR_$_TUVideoDeviceControllerProvider._cachedInputDevices
+ _TUCallHapticsEnabledKey
+ _TUSoundPlayerInfiniteIterations_block_invoke._kAudioServicesPlaySystemSoundOptionFlagsKey
+ _TUSoundPlayerInfiniteIterations_block_invoke._pred__kAudioServicesPlaySystemSoundOptionFlagsKey
+ _TUUserManuallySetDefaultCallingApp
+ _TUUserManuallySetDefaultCallingAppKey
+ __OBJC_$_CLASS_PROP_LIST_TUFeatureFlags.666
+ __OBJC_$_PROP_LIST_TUFeatureFlags.670
+ __OBJC_$_PROP_LIST_TUVideoDeviceControllerProvider.298
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_TUFaceTimeIMAVPushValidatorXPCServer
+ __OBJC_$_PROTOCOL_METHOD_TYPES_TUFaceTimeIMAVPushValidatorXPCServer
+ __OBJC_$_PROTOCOL_REFS_TUFaceTimeIMAVPushValidatorXPCServer
+ __OBJC_LABEL_PROTOCOL_$_TUFaceTimeIMAVPushValidatorXPCServer
+ __OBJC_PROTOCOL_$_TUFaceTimeIMAVPushValidatorXPCServer
+ __TUUserManuallySetDefaultCallingApp
+ ___103-[TUSenderIdentityCapabilities _sendNotificationsAndCallbacksComparingToOldSenderIdentityCapabilities:]_block_invoke.12
+ ___103-[TUSenderIdentityCapabilities _sendNotificationsAndCallbacksComparingToOldSenderIdentityCapabilities:]_block_invoke.15
+ ___103-[TUSenderIdentityCapabilities _sendNotificationsAndCallbacksComparingToOldSenderIdentityCapabilities:]_block_invoke.18
+ ___103-[TUSenderIdentityCapabilities _sendNotificationsAndCallbacksComparingToOldSenderIdentityCapabilities:]_block_invoke.21
+ ___129-[TUConversationManagerXPCClient launchApplicationForActivitySessionUUID:authorizedExternally:forceBackground:completionHandler:]_block_invoke.44
+ ___170-[TUAudioController(Internal) _requestUpdatedValueWithBlock:object:isRequestingPointer:forceNewRequest:scheduleTimePointer:notificationString:notificationUserInfo:queue:]_block_invoke.9
+ ___28-[TUSoundPlayer stopPlaying]_block_invoke.30
+ ___31-[TUAudioSystemController init]_block_invoke.39
+ ___34-[TUCallCenter answerWithRequest:]_block_invoke.245
+ ___34-[TUCallCenter answerWithRequest:]_block_invoke.246
+ ___36-[TUMomentsControllerXPCClient init]_block_invoke.3
+ ___38-[TUConversationManagerXPCClient init]_block_invoke.2
+ ___38-[TUConversationManagerXPCClient init]_block_invoke.7
+ ___38-[TUConversationManagerXPCClient init]_block_invoke_2.3
+ ___38-[TUConversationManagerXPCClient init]_block_invoke_2.8
+ ___40-[TUCallHistoryControllerXPCClient init]_block_invoke.2
+ ___42-[TUAudioSystemController setUplinkMuted:]_block_invoke.76
+ ___42-[TUAudioSystemController setUplinkMuted:]_block_invoke.76.cold.1
+ ___42-[TUCallServicesInterface defaultGreeting]_block_invoke.55
+ ___44-[TUAudioSystemController setDownlinkMuted:]_block_invoke.81
+ ___44-[TUAudioSystemController setDownlinkMuted:]_block_invoke.81.cold.1
+ ___44-[TUCallCapabilitiesXPCClient xpcConnection]_block_invoke.8
+ ___44-[TUCallCapabilitiesXPCClient xpcConnection]_block_invoke_2.9
+ ___44-[TUCallServicesInterface fetchCurrentCalls]_block_invoke.26
+ ___44-[TUCallServicesInterface fetchCurrentCalls]_block_invoke.27
+ ___44-[TUCallServicesInterface validateIMAVPush:]_block_invoke
+ ___44-[TUCallServicesInterface validateIMAVPush:]_block_invoke.96
+ ___44-[TUCallServicesInterface validateIMAVPush:]_block_invoke.cold.1
+ ___45-[TUCallCapabilitiesXPCClient _retrieveState]_block_invoke.12
+ ___45-[TUMomentsControllerXPCClient xpcConnection]_block_invoke.12
+ ___45-[TUMomentsControllerXPCClient xpcConnection]_block_invoke_2.13
+ ___46-[TUCallHistoryManagerXPCClient xpcConnection]_block_invoke.70
+ ___46-[TUCallHistoryManagerXPCClient xpcConnection]_block_invoke_2.71
+ ___46-[TUCallServicesInterface _setUpXPCConnection]_block_invoke.18
+ ___46-[TUCallServicesInterface _setUpXPCConnection]_block_invoke.20
+ ___46-[TUCallServicesInterface _setUpXPCConnection]_block_invoke.21
+ ___46-[TUConversationProviderManagerXPCClient init]_block_invoke.2
+ ___46-[TUUIXPCClientConnection fetchInCallUIState:]_block_invoke.92
+ ___47-[TUCallProviderManagerXPCClient xpcConnection]_block_invoke.23
+ ___47-[TUCallProviderManagerXPCClient xpcConnection]_block_invoke_2.24
+ ___47-[TUConversationManagerXPCClient xpcConnection]_block_invoke.92
+ ___47-[TUConversationManagerXPCClient xpcConnection]_block_invoke.93
+ ___49-[TUCallHistoryControllerXPCClient xpcConnection]_block_invoke.9
+ ___49-[TUCallHistoryControllerXPCClient xpcConnection]_block_invoke_2.10
+ ___49-[TUCallProviderManagerXPCClient sortedProviders]_block_invoke.17
+ ___50-[TUAudioRoute bluetoothProductIdentifierAsUInt32]_block_invoke
+ ___50-[TUCallServicesInterface fetchCurrentCallUpdates]_block_invoke.58
+ ___51-[TUMomentsControllerXPCClient _registerConnection]_block_invoke.8
+ ___52-[TUCallProviderManagerXPCClient defaultAppProvider]_block_invoke.13
+ ___52-[TUUserNotificationProviderXPCClient xpcConnection]_block_invoke.7
+ ___52-[TUUserNotificationProviderXPCClient xpcConnection]_block_invoke_2.8
+ ___53-[TUCallServicesInterface resetCallProvisionalStates]_block_invoke.119
+ ___54-[TUCallProviderManagerXPCClient _requestInitialState]_block_invoke.29
+ ___54-[TUCallServicesInterface dialWithRequest:completion:]_block_invoke.29
+ ___54-[TUCallServicesInterface dialWithRequest:completion:]_block_invoke_2.30
+ ___54-[TUConversationManagerXPCClient isSharePlayAvailable]_block_invoke.18
+ ___54-[TUConversationManagerXPCClient pseudonymsByCallUUID]_block_invoke.15
+ ___55-[TUConversationProviderManagerXPCClient xpcConnection]_block_invoke.10
+ ___55-[TUConversationProviderManagerXPCClient xpcConnection]_block_invoke.9
+ ___55-[TUConversationProviderManagerXPCClient xpcConnection]_block_invoke_2.11
+ ___55-[TUNeighborhoodActivityConduitXPCClient xpcConnection]_block_invoke.11
+ ___55-[TUNeighborhoodActivityConduitXPCClient xpcConnection]_block_invoke_2.12
+ ___56-[TUCallCenter joinConversationWithConversationRequest:]_block_invoke.259
+ ___56-[TUCallServicesInterface customGreetingForAccountUUID:]_block_invoke.49
+ ___56-[TUConversationManagerXPCClient advertisementsOnSystem]_block_invoke.12
+ ___58-[TUConversationManagerXPCClient isScreenSharingAvailable]_block_invoke.21
+ ___59-[TUSimulatedConversationControllerXPCClient xpcConnection]_block_invoke.12
+ ___59-[TUSimulatedConversationControllerXPCClient xpcConnection]_block_invoke.13
+ ___59-[TUSimulatedConversationControllerXPCClient xpcConnection]_block_invoke_2.14
+ ___60-[TUConversationManagerXPCClient activatedConversationLinks]_block_invoke.16
+ ___60-[TUMetadataCache updateCacheWithDestinationIDs:completion:]_block_invoke
+ ___63-[TUUIXPCClientConnection initWithListenerEndpoint:callCenter:]_block_invoke.84
+ ___63-[TUUIXPCClientConnection initWithListenerEndpoint:callCenter:]_block_invoke_2.85
+ ___64-[TUProxyCall remoteVideoClient:remoteVideoAttributesDidChange:]_block_invoke.56
+ ___65-[TUProxyCall remoteVideoClient:remoteScreenAttributesDidChange:]_block_invoke.55
+ ___66-[TUCallCenter _existingCallsAllowDialRequest:allowVoiceWithData:]_block_invoke.220
+ ___66-[TUCallCenter initWithQueue:wantsCallNotifications:featureFlags:]_block_invoke.173
+ ___66-[TUCallCenter initWithQueue:wantsCallNotifications:featureFlags:]_block_invoke.176
+ ___66-[TUCallServicesInterface policyForAddresses:forBundleIdentifier:]_block_invoke.103
+ ___67-[TUMetadataCache dataProvider:requestedRefreshWithDestinationIDs:]_block_invoke.26
+ ___69-[TUCallHistoryController callHistoryManagerRecentCallsDispatchBlock]_block_invoke.64
+ ___69-[TUCallServicesInterface willRestrictAddresses:forBundleIdentifier:]_block_invoke.106
+ ___69-[TUIDSLookupManager filteredDestinationForMultiway:completionBlock:]_block_invoke.107
+ ___69-[TUIDSLookupManager filteredDestinationForMultiway:completionBlock:]_block_invoke_2.109
+ ___69-[TUIDSLookupManager filteredDestinationForMultiway:completionBlock:]_block_invoke_3.110
+ ___70+[TUCallCapabilities _sendNotificationsAndCallbacksAfterRunningBlock:]_block_invoke.104
+ ___70+[TUCallCapabilities _sendNotificationsAndCallbacksAfterRunningBlock:]_block_invoke.109
+ ___70+[TUCallCapabilities _sendNotificationsAndCallbacksAfterRunningBlock:]_block_invoke.114
+ ___70+[TUCallCapabilities _sendNotificationsAndCallbacksAfterRunningBlock:]_block_invoke.69
+ ___70+[TUCallCapabilities _sendNotificationsAndCallbacksAfterRunningBlock:]_block_invoke.74
+ ___70+[TUCallCapabilities _sendNotificationsAndCallbacksAfterRunningBlock:]_block_invoke.79
+ ___70+[TUCallCapabilities _sendNotificationsAndCallbacksAfterRunningBlock:]_block_invoke.84
+ ___70+[TUCallCapabilities _sendNotificationsAndCallbacksAfterRunningBlock:]_block_invoke.89
+ ___70+[TUCallCapabilities _sendNotificationsAndCallbacksAfterRunningBlock:]_block_invoke.94
+ ___70+[TUCallCapabilities _sendNotificationsAndCallbacksAfterRunningBlock:]_block_invoke.99
+ ___70-[TUCallServicesInterface routesByUniqueIdentifierForRouteController:]_block_invoke.83
+ ___70-[TUCallServicesInterface routesByUniqueIdentifierForRouteController:]_block_invoke.85
+ ___70-[TUCallServicesInterface routesByUniqueIdentifierForRouteController:]_block_invoke.85.cold.1
+ ___70-[TUCallServicesInterface routesByUniqueIdentifierForRouteController:]_block_invoke.88
+ ___72-[TUCallServicesInterface _handleCurrentCallsChanged:callsDisconnected:]_block_invoke.118
+ ___72-[TUCallServicesInterface filterStatusForAddresses:forBundleIdentifier:]_block_invoke.112
+ ___73-[TUConversationManagerXPCClient incomingPendingConversationsByGroupUUID]_block_invoke.14
+ ___74-[TUIDSLookupManager handleIDSQueryResultWithDestinationStatus:onService:]_block_invoke.87
+ ___74-[TUIDSLookupManager handleIDSQueryResultWithDestinationStatus:onService:]_block_invoke.88
+ ___74-[TUIDSLookupManager handleIDSQueryResultWithDestinationStatus:onService:]_block_invoke.89
+ ___74-[TUIDSLookupManager handleIDSQueryResultWithDestinationStatus:onService:]_block_invoke.90
+ ___74-[TUIDSLookupManager handleIDSQueryResultWithDestinationStatus:onService:]_block_invoke.91
+ ___76-[TUConversationManagerXPCClient _requestInitialStateWithCompletionHandler:]_block_invoke.77
+ ___76-[TUConversationManagerXPCClient _requestInitialStateWithCompletionHandler:]_block_invoke.78
+ ___76-[TUConversationManagerXPCClient _requestInitialStateWithCompletionHandler:]_block_invoke.84
+ ___76-[TUConversationManagerXPCClient _requestInitialStateWithCompletionHandler:]_block_invoke.86
+ ___76-[TUConversationManagerXPCClient _requestInitialStateWithCompletionHandler:]_block_invoke_2.83
+ ___76-[TUConversationManagerXPCClient _requestInitialStateWithCompletionHandler:]_block_invoke_2.83.cold.1
+ ___76-[TUConversationManagerXPCClient _requestInitialStateWithCompletionHandler:]_block_invoke_2.85
+ ___76-[TUConversationManagerXPCClient _requestInitialStateWithCompletionHandler:]_block_invoke_2.87
+ ___78-[TUCallHistoryController callHistoryManagerLoadOlderRecentCallsDispatchBlock]_block_invoke.66
+ ___80-[TUMetadataCache _updateCacheWithDestinationIDs:onlyEmptyProviders:completion:]_block_invoke.12
+ ___80-[TUSoundPlayer playSound:iterations:pauseDurationBetweenIterations:completion:]_block_invoke.6
+ ___80-[TUSoundPlayer playSound:iterations:pauseDurationBetweenIterations:completion:]_block_invoke_2.18
+ ___80-[TUSoundPlayer playSound:iterations:pauseDurationBetweenIterations:completion:]_block_invoke_2.cold.4
+ ___80-[TUSoundPlayer playSound:iterations:pauseDurationBetweenIterations:completion:]_block_invoke_2.cold.5
+ ___80-[TUSoundPlayer playSound:iterations:pauseDurationBetweenIterations:completion:]_block_invoke_3
+ ___81-[TUMetadataCache updateCacheForEmptyDataProvidersWithDestinationIDs:completion:]_block_invoke
+ ___82-[TUCallServicesInterface isUnknownAddress:normalizedAddress:forBundleIdentifier:]_block_invoke.116
+ ___88-[TUCallServicesInterface routesByUniqueIdentifierForRouteController:completionHandler:]_block_invoke.91
+ ___88-[TUCallServicesInterface routesByUniqueIdentifierForRouteController:completionHandler:]_block_invoke.91.cold.1
+ ___92-[TUCallServicesInterface shouldRestrictAddresses:forBundleIdentifier:performSynchronously:]_block_invoke.109
+ ___93-[TUCallServicesInterface containsRestrictedHandle:forBundleIdentifier:performSynchronously:]_block_invoke.100
+ ___block_descriptor_40_e8_32bs_e8_v12?0B8ls32l8
+ ___block_descriptor_56_e8_32s40bs48r_e5_v8?0ls40l8r48l8s32l8
+ ___block_descriptor_68_e8_32s_e14_v16?0?<v?>8ls32l8
+ ___block_descriptor_76_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_literal_global.103
+ ___block_literal_global.109
+ ___block_literal_global.115
+ ___block_literal_global.116
+ ___block_literal_global.135
+ ___block_literal_global.15
+ ___block_literal_global.171
+ ___block_literal_global.172
+ ___block_literal_global.196
+ ___block_literal_global.202
+ ___block_literal_global.211
+ ___block_literal_global.213
+ ___block_literal_global.215
+ ___block_literal_global.217
+ ___block_literal_global.219
+ ___block_literal_global.222
+ ___block_literal_global.261
+ ___block_literal_global.263
+ ___block_literal_global.267
+ ___block_literal_global.27
+ ___block_literal_global.29
+ ___block_literal_global.348
+ ___block_literal_global.382
+ ___block_literal_global.387
+ ___block_literal_global.392
+ ___block_literal_global.48
+ ___block_literal_global.5
+ ___block_literal_global.52
+ ___block_literal_global.54
+ ___block_literal_global.58
+ ___block_literal_global.67
+ ___block_literal_global.7
+ ___block_literal_global.9
+ ___block_literal_global.91
+ ___block_literal_global.95
+ ___block_literal_global.99
+ _bluetoothProductIdentifierAsUInt32.onceToken
+ _bluetoothProductIdentifierAsUInt32.productIdRegex
+ _objc_msgSend$bluetoothProductIdentifierAsUInt32
+ _objc_msgSend$cachedModelIdentifier
+ _objc_msgSend$confidenceScore
+ _objc_msgSend$firstMatchInString:options:range:
+ _objc_msgSend$initWithType:text:date:confidenceScore:
+ _objc_msgSend$invalidateInputDevicesCache
+ _objc_msgSend$isCallHapticsAvailable
+ _objc_msgSend$isCallHapticsEnabled
+ _objc_msgSend$modelIdentifierCached
+ _objc_msgSend$mxBluetoothProductIdentifier
+ _objc_msgSend$queryAVCaptureDeviceWithType:mediaType:position:
+ _objc_msgSend$rangeAtIndex:
+ _objc_msgSend$regularExpressionWithPattern:options:error:
+ _objc_msgSend$setCachedModelIdentifier:
+ _objc_msgSend$setCallHapticsEnabled:
+ _objc_msgSend$setModelIdentifierCached:
+ _objc_msgSend$substringWithRange:
+ _objc_msgSend$validateIMAVPush:
+ _objc_msgSend$validateIMAVPush:reply:
- +[TUCallCapabilities callNotificationEligibleDevices]
- +[TUCallCapabilities devicesAvailableForCallNotifications]
- -[TUAudioController .cxx_destruct]
- -[TUAudioRoute bluetoothProductIdentifier]
- -[TUAudioRoute bluetoothProductIdentifier].cold.1
- -[TUCallCapabilitiesState callNotificationEligibleDevices]
- -[TUCallCapabilitiesState setCallNotificationEligibleDevices:]
- GCC_except_table107
- GCC_except_table110
- GCC_except_table36
- _IDSBAASignerErrorDomain_block_invoke.once
- _OBJC_CLASS_$_AKRemoteDevice
- _OBJC_IVAR_$_TUCallCapabilitiesState._callNotificationEligibleDevices
- _TUCallCapabilitiesCallsOnOtherDevicesChangedNotification
- __OBJC_$_CLASS_PROP_LIST_TUFeatureFlags.663
- __OBJC_$_PROP_LIST_TUFeatureFlags.667
- __OBJC_$_PROP_LIST_TUVideoDeviceControllerProvider.293
- ___103-[TUSenderIdentityCapabilities _sendNotificationsAndCallbacksComparingToOldSenderIdentityCapabilities:]_block_invoke.30
- ___103-[TUSenderIdentityCapabilities _sendNotificationsAndCallbacksComparingToOldSenderIdentityCapabilities:]_block_invoke.33
- ___103-[TUSenderIdentityCapabilities _sendNotificationsAndCallbacksComparingToOldSenderIdentityCapabilities:]_block_invoke.36
- ___103-[TUSenderIdentityCapabilities _sendNotificationsAndCallbacksComparingToOldSenderIdentityCapabilities:]_block_invoke.39
- ___129-[TUConversationManagerXPCClient launchApplicationForActivitySessionUUID:authorizedExternally:forceBackground:completionHandler:]_block_invoke.60
- ___170-[TUAudioController(Internal) _requestUpdatedValueWithBlock:object:isRequestingPointer:forceNewRequest:scheduleTimePointer:notificationString:notificationUserInfo:queue:]_block_invoke.11
- ___28-[TUSoundPlayer stopPlaying]_block_invoke.26
- ___31-[TUAudioSystemController init]_block_invoke.57
- ___34-[TUCallCenter answerWithRequest:]_block_invoke.263
- ___34-[TUCallCenter answerWithRequest:]_block_invoke.264
- ___36-[TUMomentsControllerXPCClient init]_block_invoke.19
- ___38-[TUConversationManagerXPCClient init]_block_invoke.18
- ___38-[TUConversationManagerXPCClient init]_block_invoke.23
- ___38-[TUConversationManagerXPCClient init]_block_invoke_2.19
- ___38-[TUConversationManagerXPCClient init]_block_invoke_2.24
- ___40-[TUCallHistoryControllerXPCClient init]_block_invoke.18
- ___42-[TUAudioSystemController setUplinkMuted:]_block_invoke.94
- ___42-[TUAudioSystemController setUplinkMuted:]_block_invoke.94.cold.1
- ___42-[TUCallServicesInterface defaultGreeting]_block_invoke.73
- ___44-[TUAudioSystemController setDownlinkMuted:]_block_invoke.99
- ___44-[TUAudioSystemController setDownlinkMuted:]_block_invoke.99.cold.1
- ___44-[TUCallCapabilitiesXPCClient xpcConnection]_block_invoke.26
- ___44-[TUCallCapabilitiesXPCClient xpcConnection]_block_invoke_2.27
- ___44-[TUCallServicesInterface fetchCurrentCalls]_block_invoke.44
- ___44-[TUCallServicesInterface fetchCurrentCalls]_block_invoke.45
- ___45-[TUCallCapabilitiesXPCClient _retrieveState]_block_invoke.30
- ___45-[TUMomentsControllerXPCClient xpcConnection]_block_invoke.28
- ___45-[TUMomentsControllerXPCClient xpcConnection]_block_invoke_2.29
- ___46-[TUCallHistoryManagerXPCClient xpcConnection]_block_invoke.88
- ___46-[TUCallHistoryManagerXPCClient xpcConnection]_block_invoke_2.89
- ___46-[TUCallServicesInterface _setUpXPCConnection]_block_invoke.36
- ___46-[TUCallServicesInterface _setUpXPCConnection]_block_invoke.38
- ___46-[TUCallServicesInterface _setUpXPCConnection]_block_invoke.39
- ___46-[TUConversationProviderManagerXPCClient init]_block_invoke.18
- ___46-[TUUIXPCClientConnection fetchInCallUIState:]_block_invoke.108
- ___47-[TUCallProviderManagerXPCClient xpcConnection]_block_invoke.41
- ___47-[TUCallProviderManagerXPCClient xpcConnection]_block_invoke_2.42
- ___47-[TUConversationManagerXPCClient xpcConnection]_block_invoke.110
- ___47-[TUConversationManagerXPCClient xpcConnection]_block_invoke.111
- ___49-[TUCallHistoryControllerXPCClient xpcConnection]_block_invoke.27
- ___49-[TUCallHistoryControllerXPCClient xpcConnection]_block_invoke_2.28
- ___49-[TUCallProviderManagerXPCClient sortedProviders]_block_invoke.35
- ___50-[TUCallServicesInterface fetchCurrentCallUpdates]_block_invoke.76
- ___51-[TUMomentsControllerXPCClient _registerConnection]_block_invoke.24
- ___52-[TUCallProviderManagerXPCClient defaultAppProvider]_block_invoke.31
- ___52-[TUUserNotificationProviderXPCClient xpcConnection]_block_invoke.25
- ___52-[TUUserNotificationProviderXPCClient xpcConnection]_block_invoke_2.26
- ___53-[TUCallServicesInterface resetCallProvisionalStates]_block_invoke.134
- ___54-[TUCallProviderManagerXPCClient _requestInitialState]_block_invoke.47
- ___54-[TUCallServicesInterface dialWithRequest:completion:]_block_invoke.47
- ___54-[TUCallServicesInterface dialWithRequest:completion:]_block_invoke_2.48
- ___54-[TUConversationManagerXPCClient isSharePlayAvailable]_block_invoke.34
- ___54-[TUConversationManagerXPCClient pseudonymsByCallUUID]_block_invoke.31
- ___55-[TUConversationProviderManagerXPCClient xpcConnection]_block_invoke.27
- ___55-[TUConversationProviderManagerXPCClient xpcConnection]_block_invoke.28
- ___55-[TUConversationProviderManagerXPCClient xpcConnection]_block_invoke_2.29
- ___55-[TUNeighborhoodActivityConduitXPCClient xpcConnection]_block_invoke.29
- ___55-[TUNeighborhoodActivityConduitXPCClient xpcConnection]_block_invoke_2.30
- ___56-[TUCallCenter joinConversationWithConversationRequest:]_block_invoke.277
- ___56-[TUCallServicesInterface customGreetingForAccountUUID:]_block_invoke.67
- ___56-[TUConversationManagerXPCClient advertisementsOnSystem]_block_invoke.28
- ___58-[TUConversationManagerXPCClient isScreenSharingAvailable]_block_invoke.37
- ___59-[TUSimulatedConversationControllerXPCClient xpcConnection]_block_invoke.30
- ___59-[TUSimulatedConversationControllerXPCClient xpcConnection]_block_invoke.31
- ___59-[TUSimulatedConversationControllerXPCClient xpcConnection]_block_invoke_2.32
- ___60-[TUConversationManagerXPCClient activatedConversationLinks]_block_invoke.32
- ___63-[TUUIXPCClientConnection initWithListenerEndpoint:callCenter:]_block_invoke.100
- ___63-[TUUIXPCClientConnection initWithListenerEndpoint:callCenter:]_block_invoke_2.101
- ___64-[TUProxyCall remoteVideoClient:remoteVideoAttributesDidChange:]_block_invoke.74
- ___65-[TUProxyCall remoteVideoClient:remoteScreenAttributesDidChange:]_block_invoke.73
- ___66-[TUCallCenter _existingCallsAllowDialRequest:allowVoiceWithData:]_block_invoke.238
- ___66-[TUCallCenter initWithQueue:wantsCallNotifications:featureFlags:]_block_invoke.191
- ___66-[TUCallCenter initWithQueue:wantsCallNotifications:featureFlags:]_block_invoke.194
- ___66-[TUCallServicesInterface policyForAddresses:forBundleIdentifier:]_block_invoke.118
- ___67-[TUMetadataCache dataProvider:requestedRefreshWithDestinationIDs:]_block_invoke.25
- ___69-[TUCallHistoryController callHistoryManagerRecentCallsDispatchBlock]_block_invoke.82
- ___69-[TUCallServicesInterface willRestrictAddresses:forBundleIdentifier:]_block_invoke.121
- ___69-[TUIDSLookupManager filteredDestinationForMultiway:completionBlock:]_block_invoke.125
- ___69-[TUIDSLookupManager filteredDestinationForMultiway:completionBlock:]_block_invoke_2.127
- ___69-[TUIDSLookupManager filteredDestinationForMultiway:completionBlock:]_block_invoke_3.128
- ___70+[TUCallCapabilities _sendNotificationsAndCallbacksAfterRunningBlock:]_block_invoke.100
- ___70+[TUCallCapabilities _sendNotificationsAndCallbacksAfterRunningBlock:]_block_invoke.105
- ___70+[TUCallCapabilities _sendNotificationsAndCallbacksAfterRunningBlock:]_block_invoke.110
- ___70+[TUCallCapabilities _sendNotificationsAndCallbacksAfterRunningBlock:]_block_invoke.115
- ___70+[TUCallCapabilities _sendNotificationsAndCallbacksAfterRunningBlock:]_block_invoke.120
- ___70+[TUCallCapabilities _sendNotificationsAndCallbacksAfterRunningBlock:]_block_invoke.125
- ___70+[TUCallCapabilities _sendNotificationsAndCallbacksAfterRunningBlock:]_block_invoke.130
- ___70+[TUCallCapabilities _sendNotificationsAndCallbacksAfterRunningBlock:]_block_invoke.135
- ___70+[TUCallCapabilities _sendNotificationsAndCallbacksAfterRunningBlock:]_block_invoke.90
- ___70+[TUCallCapabilities _sendNotificationsAndCallbacksAfterRunningBlock:]_block_invoke.95
- ___70-[TUCallServicesInterface routesByUniqueIdentifierForRouteController:]_block_invoke.101
- ___70-[TUCallServicesInterface routesByUniqueIdentifierForRouteController:]_block_invoke.103
- ___70-[TUCallServicesInterface routesByUniqueIdentifierForRouteController:]_block_invoke.103.cold.1
- ___70-[TUCallServicesInterface routesByUniqueIdentifierForRouteController:]_block_invoke.106
- ___72-[TUCallServicesInterface _handleCurrentCallsChanged:callsDisconnected:]_block_invoke.133
- ___72-[TUCallServicesInterface filterStatusForAddresses:forBundleIdentifier:]_block_invoke.127
- ___73-[TUConversationManagerXPCClient incomingPendingConversationsByGroupUUID]_block_invoke.30
- ___74-[TUIDSLookupManager handleIDSQueryResultWithDestinationStatus:onService:]_block_invoke.105
- ___74-[TUIDSLookupManager handleIDSQueryResultWithDestinationStatus:onService:]_block_invoke.106
- ___74-[TUIDSLookupManager handleIDSQueryResultWithDestinationStatus:onService:]_block_invoke.107
- ___74-[TUIDSLookupManager handleIDSQueryResultWithDestinationStatus:onService:]_block_invoke.108
- ___74-[TUIDSLookupManager handleIDSQueryResultWithDestinationStatus:onService:]_block_invoke.109
- ___76-[TUConversationManagerXPCClient _requestInitialStateWithCompletionHandler:]_block_invoke.102
- ___76-[TUConversationManagerXPCClient _requestInitialStateWithCompletionHandler:]_block_invoke.104
- ___76-[TUConversationManagerXPCClient _requestInitialStateWithCompletionHandler:]_block_invoke.93
- ___76-[TUConversationManagerXPCClient _requestInitialStateWithCompletionHandler:]_block_invoke.94
- ___76-[TUConversationManagerXPCClient _requestInitialStateWithCompletionHandler:]_block_invoke_2.101
- ___76-[TUConversationManagerXPCClient _requestInitialStateWithCompletionHandler:]_block_invoke_2.101.cold.1
- ___76-[TUConversationManagerXPCClient _requestInitialStateWithCompletionHandler:]_block_invoke_2.103
- ___76-[TUConversationManagerXPCClient _requestInitialStateWithCompletionHandler:]_block_invoke_2.105
- ___78-[TUCallHistoryController callHistoryManagerLoadOlderRecentCallsDispatchBlock]_block_invoke.84
- ___80-[TUMetadataCache _updateCacheWithDestinationIDs:onlyEmptyProviders:completion:]_block_invoke.11
- ___80-[TUSoundPlayer playSound:iterations:pauseDurationBetweenIterations:completion:]_block_invoke.4
- ___80-[TUSoundPlayer playSound:iterations:pauseDurationBetweenIterations:completion:]_block_invoke_2.17
- ___82-[TUCallServicesInterface isUnknownAddress:normalizedAddress:forBundleIdentifier:]_block_invoke.131
- ___88-[TUCallServicesInterface routesByUniqueIdentifierForRouteController:completionHandler:]_block_invoke.109
- ___88-[TUCallServicesInterface routesByUniqueIdentifierForRouteController:completionHandler:]_block_invoke.109.cold.1
- ___92-[TUCallServicesInterface shouldRestrictAddresses:forBundleIdentifier:performSynchronously:]_block_invoke.124
- ___93-[TUCallServicesInterface containsRestrictedHandle:forBundleIdentifier:performSynchronously:]_block_invoke.114
- ___block_descriptor_64_e8_32s_e14_v16?0?<v?>8ls32l8
- ___block_descriptor_72_e8_32s40bs_e5_v8?0ls32l8s40l8
- ___block_literal_global.100
- ___block_literal_global.110
- ___block_literal_global.112
- ___block_literal_global.114
- ___block_literal_global.117
- ___block_literal_global.120
- ___block_literal_global.121
- ___block_literal_global.122
- ___block_literal_global.123
- ___block_literal_global.126
- ___block_literal_global.132
- ___block_literal_global.134
- ___block_literal_global.143
- ___block_literal_global.145
- ___block_literal_global.147
- ___block_literal_global.149
- ___block_literal_global.155
- ___block_literal_global.183
- ___block_literal_global.190
- ___block_literal_global.21
- ___block_literal_global.214
- ___block_literal_global.220
- ___block_literal_global.229
- ___block_literal_global.231
- ___block_literal_global.235
- ___block_literal_global.237
- ___block_literal_global.240
- ___block_literal_global.246
- ___block_literal_global.279
- ___block_literal_global.281
- ___block_literal_global.34
- ___block_literal_global.360
- ___block_literal_global.38
- ___block_literal_global.400
- ___block_literal_global.405
- ___block_literal_global.410
- ___block_literal_global.42
- ___block_literal_global.44
- ___block_literal_global.51
- ___block_literal_global.75
- ___block_literal_global.88
- ___block_literal_global.92
- ___block_literal_global.97
- ___block_literal_global.98
- _objc_msgSend$areCallsOnOtherDevicesEnabled
- _objc_msgSend$bluetoothProductIdentifier
- _objc_msgSend$callNotificationEligibleDevices
- _objc_msgSend$devicesAvailableForCallNotifications
- _objc_msgSend$setCallNotificationEligibleDevices:
CStrings:
+ " confidenceScore=%f"
+ " mI=%@"
+ " mxPID=%@"
+ "%@ isCallHapticsEnabled called"
+ "%@ setCallHapticsEnabled called %d"
+ ",(\\d+)$"
+ "@\"TUConfigurationProvider\""
+ "@48@0:8q16@24@32d40"
+ "ATVRemote1,1"
+ "ATVRemote1,2"
+ "AirPods1,1"
+ "AirPods1,3"
+ "AirPods3,4"
+ "AirPodsPro1,1"
+ "ApGn"
+ "AppleTV11,1"
+ "AppleTV5,3"
+ "AppleTV6,2"
+ "AudioAccessory1,1"
+ "AudioAccessory1,2"
+ "AudioAccessory5,1"
+ "BeatsSolo3,1"
+ "BeatsSoloPro1,1"
+ "BeatsStudio3,2"
+ "BeatsStudioBuds1,1"
+ "BeatsStudioBuds1,2"
+ "BeatsStudioPro1,1"
+ "BeatsX1,1"
+ "Beginning animation to PIP with currentInputDevice"
+ "Beginning animation to preview with currentInputDevice"
+ "C!"
+ "Device1,21760"
+ "Device1,22034"
+ "Device1,8202"
+ "Device1,8208"
+ "Device1,8210"
+ "Device1,8211"
+ "Device1,8212"
+ "Device1,8213"
+ "Device1,8216"
+ "Device1,8217"
+ "Device1,8218"
+ "Device1,8219"
+ "Device1,8220"
+ "Device1,8222"
+ "Device1,8223"
+ "Device1,8224"
+ "Device1,8228"
+ "Device1,8229"
+ "Device1,8230"
+ "Device1,8232"
+ "Device1,8233"
+ "Device1,8239"
+ "Ending animation to PIP with currentInputDevice"
+ "Ending animation to preview with currentInputDevice"
+ "Error when requesting synchronous push validation: %@"
+ "Executing contact fetch request %{sensitive}@ using contact store %{sensitive}@"
+ "Extracted product ID %u from '%@' for route: %@"
+ "Failed to parse product ID from '%@' for route: %@"
+ "HeGn"
+ "IMAVSunset"
+ "IMAVSunsetEnabled"
+ "Ignoring start preview with currentInputDevice"
+ "No Bluetooth product identifier available for route: %@"
+ "Pausing preview with currentInputDevice"
+ "PowerBeats3,1"
+ "Powerb3,1"
+ "Powerbeats4,1"
+ "PowerbeatsPro1,1"
+ "Resolved model identifier '%@' for Bluetooth device: %@"
+ "Stopping preview with currentInputDevice"
+ "T@\"NSString\",C,N,V_cachedModelIdentifier"
+ "T@\"TUConfigurationProvider\",R,N,V_configurationProvider"
+ "TB,N,GisCallHapticsEnabled,SsetCallHapticsEnabled:"
+ "TB,N,V_modelIdentifierCached"
+ "TB,R,N,GisCallHapticsAvailable"
+ "TUCallHapticsEnabled"
+ "TUFaceTimeIMAVPushValidatorXPCServer"
+ "Td,R,N,V_confidenceScore"
+ "T{os_unfair_lock_s=I},N,V_modifyingStateLock"
+ "UserManuallySetDefaultCallingApp"
+ "Vv32@0:8@\"NSString\"16@?<v@?B>24"
+ "_cachedInputDevices"
+ "_cachedInputDevices = %@"
+ "_cachedModelIdentifier"
+ "_confidenceScore"
+ "_configurationProvider"
+ "_modelIdentifierCached"
+ "bluetoothProductIdentifierAsUInt32"
+ "cachedModelIdentifier"
+ "callHapticsAvailable"
+ "callHapticsEnabled"
+ "confidenceScore"
+ "device is not bluetooth: %@"
+ "firstMatchInString:options:range:"
+ "initWithType:text:date:confidenceScore:"
+ "invalid pid for Bluetooth device: %@"
+ "invalidateInputDevicesCache"
+ "isCallHapticsAvailable"
+ "isCallHapticsEnabled"
+ "kAudioServicesPlaySystemSoundOptionFlagsKey"
+ "modelIdentifierCached"
+ "mxBluetoothProductIdentifier"
+ "preferredFrontCaptureDevice: %@, preferredBackCaptureDevice: %@"
+ "queryAVCaptureDeviceWithType:mediaType:position:"
+ "rangeAtIndex:"
+ "regularExpressionWithPattern:options:error:"
+ "setCachedModelIdentifier:"
+ "setCallHapticsEnabled:"
+ "setModelIdentifierCached:"
+ "substringWithRange:"
+ "unable to create NSString from CB product string for pid: %u on device: %@"
+ "updateCacheWithDestinationIDs:didMakeChanges:"
+ "v20@0:8{os_unfair_lock_s=I}16"
+ "validateIMAVPush:"
+ "validateIMAVPush:reply:"
- "    callNotificationEligibleDevices: %@\n"
- "    devicesAvailableForCallNotifications: %d\n"
- " bluetoothProductIdentifier=%@"
- "B!"
- "Beginning animation to PIP with self.currentInputDevice: %@"
- "Beginning animation to preview with self.currentInputDevice: %@"
- "Calls on Other Devices capabilities changed from (devicesAvailable=%@ enabled=%d) to (devicesAvailable=%@ enabled=%d)"
- "Ending animation to PIP with self.currentInputDevice: %@"
- "Ending animation to preview with self.currentInputDevice: %@"
- "Executing contact fetch request %{private}@ using contact store %{private}@"
- "Ignoring start preview with self.currentInputDevice: %@"
- "Pausing preview with self.currentInputDevice: %@"
- "Stopping preview with self.currentInputDevice: %@"
- "T@\"NSArray\",&,N,V_callNotificationEligibleDevices"
- "T@\"NSObject<OS_dispatch_semaphore>\",&,N,V_modifyingStateLock"
- "TUCallCapabilitiesCallsOnOtherDevicesChangedNotification"
- "_callNotificationEligibleDevices"
- "backTripleCameraDevices.count=%lu, backDualCameraDevices.count=%lu,  backDualWideCameraDevices.count =%lu, backWideCameraDevices.count=%lu"
- "bluetoothProductIdentifier"
- "callNotificationEligibleDevices"
- "com.apple.preferences.sounds"
- "currentLanguageIdentifier = %@"
- "devicesAvailableForCallNotifications"
- "effects-haptic"
- "setCallNotificationEligibleDevices:"

```
