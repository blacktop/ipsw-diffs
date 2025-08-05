## TelephonyUtilities

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`

```diff

-1571.100.7.1.3
-  __TEXT.__text: 0x16c4c4
+1574.100.5.0.0
+  __TEXT.__text: 0x16cd40
   __TEXT.__auth_stubs: 0x2370
-  __TEXT.__objc_methlist: 0x1a148
-  __TEXT.__cstring: 0x13238
+  __TEXT.__objc_methlist: 0x1a1c8
+  __TEXT.__cstring: 0x132f8
   __TEXT.__const: 0x1044
-  __TEXT.__oslogstring: 0x12442
-  __TEXT.__gcc_except_tab: 0x18e0
+  __TEXT.__oslogstring: 0x12432
+  __TEXT.__gcc_except_tab: 0x18f4
   __TEXT.__ustring: 0xde
   __TEXT.__dlopen_cstrs: 0x8df
   __TEXT.__constg_swiftt: 0x578

   __TEXT.__swift_as_ret: 0x84
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x5d38
+  __TEXT.__unwind_info: 0x5d50
   __TEXT.__eh_frame: 0x1378
   __TEXT.__objc_classname: 0x2727
-  __TEXT.__objc_methname: 0x3c013
-  __TEXT.__objc_methtype: 0x7eff
-  __TEXT.__objc_stubs: 0x20bc0
-  __DATA_CONST.__got: 0xe50
-  __DATA_CONST.__const: 0x35e0
+  __TEXT.__objc_methname: 0x3c208
+  __TEXT.__objc_methtype: 0x7f13
+  __TEXT.__objc_stubs: 0x20ce0
+  __DATA_CONST.__got: 0xe60
+  __DATA_CONST.__const: 0x3610
   __DATA_CONST.__objc_classlist: 0x830
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x408
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xaed0
+  __DATA_CONST.__objc_selrefs: 0xaf20
   __DATA_CONST.__objc_protorefs: 0x108
   __DATA_CONST.__objc_superrefs: 0x6b0
   __DATA_CONST.__objc_arraydata: 0x6f8
   __AUTH_CONST.__auth_got: 0x11c8
-  __AUTH_CONST.__const: 0x30d0
-  __AUTH_CONST.__cfstring: 0x11cc0
-  __AUTH_CONST.__objc_const: 0x281b8
+  __AUTH_CONST.__const: 0x3128
+  __AUTH_CONST.__cfstring: 0x11c00
+  __AUTH_CONST.__objc_const: 0x28258
   __AUTH_CONST.__objc_intobj: 0x540
   __AUTH_CONST.__objc_arrayobj: 0x228
   __AUTH_CONST.__objc_doubleobj: 0x40
-  __AUTH.__objc_data: 0x2788
+  __AUTH.__objc_data: 0x26c0
   __AUTH.__data: 0x5e8
-  __DATA.__objc_ivar: 0x17e0
+  __DATA.__objc_ivar: 0x17e8
   __DATA.__data: 0x3320
   __DATA.__bss: 0x1890
   __DATA.__common: 0x28
-  __DATA_DIRTY.__objc_data: 0x2b20
+  __DATA_DIRTY.__objc_data: 0x2be8
   __DATA_DIRTY.__data: 0x30
   __DATA_DIRTY.__bss: 0x230
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 8A349496-A178-34FF-A784-1012B59BF874
-  Functions: 10000
-  Symbols:   29894
-  CStrings:  16390
+  UUID: 718DA868-B6A2-395B-9FB1-8672C48E0907
+  Functions: 10017
+  Symbols:   29943
+  CStrings:  16396
 
Symbols:
+ +[TUCallCapabilities areCallsOnOtherDevicesEnabled]
+ +[TUCallCapabilities callNotificationEligibleDevices]
+ +[TUCallCapabilities devicesAvailableForCallNotifications]
+ -[TUCall isSmartHoldingGASRAvailable]
+ -[TUCallCapabilitiesState callNotificationEligibleDevices]
+ -[TUCallCapabilitiesState setCallNotificationEligibleDevices:]
+ -[TUCallCapabilitiesXPCClient performBlockOnQueue:]
+ -[TUCallCapabilitiesXPCClient queueContext]
+ -[TUCallHistoryController callsWithPredicate:limit:offset:batchSize:]
+ -[TUCallUpdate isHostEligibleForScreening]
+ -[TUConversationActivitySession didAssociateScene]
+ -[TUConversationActivitySession setDidAssociateScene:]
+ GCC_except_table107
+ GCC_except_table110
+ GCC_except_table154
+ GCC_except_table49
+ GCC_except_table61
+ GCC_except_table69
+ GCC_except_table70
+ _IDSBAASignerErrorDomain_block_invoke.once
+ _OBJC_CLASS_$_AKRemoteDevice
+ _OBJC_CLASS_$__NSLocalizedStringResource
+ _OBJC_IVAR_$_TUCallCapabilitiesState._callNotificationEligibleDevices
+ _OBJC_IVAR_$_TUConversationActivitySession._didAssociateScene
+ _TUCallCapabilitiesCallsOnOtherDevicesChangedNotification
+ _TUReceptionistEnabled
+ _TUResolvedPhoneResource
+ _TUResolvedPhoneString
+ ___103-[TUSenderIdentityCapabilities _sendNotificationsAndCallbacksComparingToOldSenderIdentityCapabilities:]_block_invoke.30
+ ___103-[TUSenderIdentityCapabilities _sendNotificationsAndCallbacksComparingToOldSenderIdentityCapabilities:]_block_invoke.33
+ ___103-[TUSenderIdentityCapabilities _sendNotificationsAndCallbacksComparingToOldSenderIdentityCapabilities:]_block_invoke.36
+ ___103-[TUSenderIdentityCapabilities _sendNotificationsAndCallbacksComparingToOldSenderIdentityCapabilities:]_block_invoke.39
+ ___129-[TUConversationManagerXPCClient launchApplicationForActivitySessionUUID:authorizedExternally:forceBackground:completionHandler:]_block_invoke.60
+ ___31-[TUAudioSystemController init]_block_invoke.57
+ ___34-[TUCallCenter answerWithRequest:]_block_invoke.263
+ ___34-[TUCallCenter answerWithRequest:]_block_invoke.264
+ ___34-[TURouteController requeryRoutes]_block_invoke
+ ___34-[TURouteController requeryRoutes]_block_invoke_2
+ ___36-[TUMomentsControllerXPCClient init]_block_invoke.19
+ ___38-[TUConversationManagerXPCClient init]_block_invoke.18
+ ___38-[TUConversationManagerXPCClient init]_block_invoke.23
+ ___38-[TUConversationManagerXPCClient init]_block_invoke_2.19
+ ___38-[TUConversationManagerXPCClient init]_block_invoke_2.24
+ ___40-[TUCallHistoryControllerXPCClient init]_block_invoke.18
+ ___42-[TUAudioSystemController setUplinkMuted:]_block_invoke.94
+ ___42-[TUAudioSystemController setUplinkMuted:]_block_invoke.94.cold.1
+ ___42-[TUCallServicesInterface defaultGreeting]_block_invoke.73
+ ___44-[TUAudioSystemController setDownlinkMuted:]_block_invoke.99
+ ___44-[TUAudioSystemController setDownlinkMuted:]_block_invoke.99.cold.1
+ ___44-[TUCallCapabilitiesXPCClient xpcConnection]_block_invoke.26
+ ___44-[TUCallCapabilitiesXPCClient xpcConnection]_block_invoke_2.27
+ ___44-[TUCallServicesInterface fetchCurrentCalls]_block_invoke.44
+ ___44-[TUCallServicesInterface fetchCurrentCalls]_block_invoke.45
+ ___45-[TUCallCapabilitiesXPCClient _retrieveState]_block_invoke.30
+ ___45-[TUMomentsControllerXPCClient xpcConnection]_block_invoke.28
+ ___45-[TUMomentsControllerXPCClient xpcConnection]_block_invoke_2.29
+ ___46-[TUCallHistoryManagerXPCClient xpcConnection]_block_invoke.88
+ ___46-[TUCallHistoryManagerXPCClient xpcConnection]_block_invoke_2.89
+ ___46-[TUCallServicesInterface _setUpXPCConnection]_block_invoke.36
+ ___46-[TUCallServicesInterface _setUpXPCConnection]_block_invoke.38
+ ___46-[TUCallServicesInterface _setUpXPCConnection]_block_invoke.39
+ ___46-[TUConversationProviderManagerXPCClient init]_block_invoke.18
+ ___46-[TUUIXPCClientConnection fetchInCallUIState:]_block_invoke.108
+ ___47-[TUCallProviderManagerXPCClient xpcConnection]_block_invoke.41
+ ___47-[TUCallProviderManagerXPCClient xpcConnection]_block_invoke_2.42
+ ___47-[TUConversationManagerXPCClient xpcConnection]_block_invoke.110
+ ___47-[TUConversationManagerXPCClient xpcConnection]_block_invoke.111
+ ___49-[TUCallHistoryControllerXPCClient xpcConnection]_block_invoke.27
+ ___49-[TUCallHistoryControllerXPCClient xpcConnection]_block_invoke_2.28
+ ___49-[TUCallProviderManagerXPCClient sortedProviders]_block_invoke.35
+ ___50-[TUCallServicesInterface fetchCurrentCallUpdates]_block_invoke.76
+ ___51-[TUMomentsControllerXPCClient _registerConnection]_block_invoke.24
+ ___52-[TUCallProviderManagerXPCClient defaultAppProvider]_block_invoke.31
+ ___52-[TUUserNotificationProviderXPCClient xpcConnection]_block_invoke.25
+ ___52-[TUUserNotificationProviderXPCClient xpcConnection]_block_invoke_2.26
+ ___53-[TUCallServicesInterface resetCallProvisionalStates]_block_invoke.134
+ ___54-[TUCallProviderManagerXPCClient _requestInitialState]_block_invoke.47
+ ___54-[TUCallServicesInterface dialWithRequest:completion:]_block_invoke.47
+ ___54-[TUCallServicesInterface dialWithRequest:completion:]_block_invoke_2.48
+ ___54-[TUConversationManagerXPCClient isSharePlayAvailable]_block_invoke.34
+ ___54-[TUConversationManagerXPCClient pseudonymsByCallUUID]_block_invoke.31
+ ___55-[TUConversationProviderManagerXPCClient xpcConnection]_block_invoke.27
+ ___55-[TUConversationProviderManagerXPCClient xpcConnection]_block_invoke.28
+ ___55-[TUConversationProviderManagerXPCClient xpcConnection]_block_invoke_2.29
+ ___55-[TUNeighborhoodActivityConduitXPCClient xpcConnection]_block_invoke.29
+ ___55-[TUNeighborhoodActivityConduitXPCClient xpcConnection]_block_invoke_2.30
+ ___56-[TUCallCenter joinConversationWithConversationRequest:]_block_invoke.277
+ ___56-[TUCallServicesInterface customGreetingForAccountUUID:]_block_invoke.67
+ ___56-[TUConversationManagerXPCClient advertisementsOnSystem]_block_invoke.28
+ ___58-[TUConversationManagerXPCClient isScreenSharingAvailable]_block_invoke.37
+ ___59-[TUSimulatedConversationControllerXPCClient xpcConnection]_block_invoke.30
+ ___59-[TUSimulatedConversationControllerXPCClient xpcConnection]_block_invoke.31
+ ___59-[TUSimulatedConversationControllerXPCClient xpcConnection]_block_invoke_2.32
+ ___60-[TUConversationManagerXPCClient activatedConversationLinks]_block_invoke.32
+ ___63-[TUUIXPCClientConnection initWithListenerEndpoint:callCenter:]_block_invoke.100
+ ___63-[TUUIXPCClientConnection initWithListenerEndpoint:callCenter:]_block_invoke_2.101
+ ___64-[TUProxyCall remoteVideoClient:remoteVideoAttributesDidChange:]_block_invoke.74
+ ___65-[TUProxyCall remoteVideoClient:remoteScreenAttributesDidChange:]_block_invoke.73
+ ___66-[TUCallCenter _existingCallsAllowDialRequest:allowVoiceWithData:]_block_invoke.238
+ ___66-[TUCallCenter initWithQueue:wantsCallNotifications:featureFlags:]_block_invoke.191
+ ___66-[TUCallCenter initWithQueue:wantsCallNotifications:featureFlags:]_block_invoke.194
+ ___66-[TUCallServicesInterface policyForAddresses:forBundleIdentifier:]_block_invoke.118
+ ___69-[TUCallHistoryController callHistoryManagerRecentCallsDispatchBlock]_block_invoke.82
+ ___69-[TUCallHistoryController callsWithPredicate:limit:offset:batchSize:]_block_invoke
+ ___69-[TUCallServicesInterface willRestrictAddresses:forBundleIdentifier:]_block_invoke.121
+ ___69-[TUIDSLookupManager filteredDestinationForMultiway:completionBlock:]_block_invoke.125
+ ___69-[TUIDSLookupManager filteredDestinationForMultiway:completionBlock:]_block_invoke_2.127
+ ___69-[TUIDSLookupManager filteredDestinationForMultiway:completionBlock:]_block_invoke_3.128
+ ___70+[TUCallCapabilities _sendNotificationsAndCallbacksAfterRunningBlock:]_block_invoke.100
+ ___70+[TUCallCapabilities _sendNotificationsAndCallbacksAfterRunningBlock:]_block_invoke.105
+ ___70+[TUCallCapabilities _sendNotificationsAndCallbacksAfterRunningBlock:]_block_invoke.110
+ ___70+[TUCallCapabilities _sendNotificationsAndCallbacksAfterRunningBlock:]_block_invoke.115
+ ___70+[TUCallCapabilities _sendNotificationsAndCallbacksAfterRunningBlock:]_block_invoke.120
+ ___70+[TUCallCapabilities _sendNotificationsAndCallbacksAfterRunningBlock:]_block_invoke.125
+ ___70+[TUCallCapabilities _sendNotificationsAndCallbacksAfterRunningBlock:]_block_invoke.130
+ ___70+[TUCallCapabilities _sendNotificationsAndCallbacksAfterRunningBlock:]_block_invoke.135
+ ___70+[TUCallCapabilities _sendNotificationsAndCallbacksAfterRunningBlock:]_block_invoke.90
+ ___70+[TUCallCapabilities _sendNotificationsAndCallbacksAfterRunningBlock:]_block_invoke.95
+ ___70-[TUCallServicesInterface routesByUniqueIdentifierForRouteController:]_block_invoke.101
+ ___70-[TUCallServicesInterface routesByUniqueIdentifierForRouteController:]_block_invoke.103
+ ___70-[TUCallServicesInterface routesByUniqueIdentifierForRouteController:]_block_invoke.103.cold.1
+ ___70-[TUCallServicesInterface routesByUniqueIdentifierForRouteController:]_block_invoke.106
+ ___72-[TUCallServicesInterface _handleCurrentCallsChanged:callsDisconnected:]_block_invoke.133
+ ___72-[TUCallServicesInterface filterStatusForAddresses:forBundleIdentifier:]_block_invoke.127
+ ___73-[TUConversationManagerXPCClient incomingPendingConversationsByGroupUUID]_block_invoke.30
+ ___74-[TUIDSLookupManager handleIDSQueryResultWithDestinationStatus:onService:]_block_invoke.105
+ ___74-[TUIDSLookupManager handleIDSQueryResultWithDestinationStatus:onService:]_block_invoke.106
+ ___74-[TUIDSLookupManager handleIDSQueryResultWithDestinationStatus:onService:]_block_invoke.107
+ ___74-[TUIDSLookupManager handleIDSQueryResultWithDestinationStatus:onService:]_block_invoke.108
+ ___74-[TUIDSLookupManager handleIDSQueryResultWithDestinationStatus:onService:]_block_invoke.109
+ ___75-[TUConversationActivitySession launchApplicationWithForcedURL:completion:]_block_invoke.138
+ ___76-[TUConversationManagerXPCClient _requestInitialStateWithCompletionHandler:]_block_invoke.102
+ ___76-[TUConversationManagerXPCClient _requestInitialStateWithCompletionHandler:]_block_invoke.104
+ ___76-[TUConversationManagerXPCClient _requestInitialStateWithCompletionHandler:]_block_invoke.93
+ ___76-[TUConversationManagerXPCClient _requestInitialStateWithCompletionHandler:]_block_invoke.94
+ ___76-[TUConversationManagerXPCClient _requestInitialStateWithCompletionHandler:]_block_invoke_2.101
+ ___76-[TUConversationManagerXPCClient _requestInitialStateWithCompletionHandler:]_block_invoke_2.101.cold.1
+ ___76-[TUConversationManagerXPCClient _requestInitialStateWithCompletionHandler:]_block_invoke_2.103
+ ___76-[TUConversationManagerXPCClient _requestInitialStateWithCompletionHandler:]_block_invoke_2.105
+ ___78-[TUCallHistoryController callHistoryManagerLoadOlderRecentCallsDispatchBlock]_block_invoke.84
+ ___82-[TUCallServicesInterface isUnknownAddress:normalizedAddress:forBundleIdentifier:]_block_invoke.131
+ ___88-[TUCallServicesInterface routesByUniqueIdentifierForRouteController:completionHandler:]_block_invoke.109
+ ___88-[TUCallServicesInterface routesByUniqueIdentifierForRouteController:completionHandler:]_block_invoke.109.cold.1
+ ___92-[TUCallServicesInterface shouldRestrictAddresses:forBundleIdentifier:performSynchronously:]_block_invoke.124
+ ___93-[TUCallServicesInterface containsRestrictedHandle:forBundleIdentifier:performSynchronously:]_block_invoke.114
+ ___block_descriptor_80_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_literal_global.100
+ ___block_literal_global.110
+ ___block_literal_global.114
+ ___block_literal_global.117
+ ___block_literal_global.120
+ ___block_literal_global.121
+ ___block_literal_global.122
+ ___block_literal_global.123
+ ___block_literal_global.126
+ ___block_literal_global.132
+ ___block_literal_global.133
+ ___block_literal_global.134
+ ___block_literal_global.143
+ ___block_literal_global.145
+ ___block_literal_global.147
+ ___block_literal_global.149
+ ___block_literal_global.155
+ ___block_literal_global.183
+ ___block_literal_global.2014
+ ___block_literal_global.2020
+ ___block_literal_global.208
+ ___block_literal_global.21
+ ___block_literal_global.214
+ ___block_literal_global.220
+ ___block_literal_global.229
+ ___block_literal_global.231
+ ___block_literal_global.233
+ ___block_literal_global.235
+ ___block_literal_global.237
+ ___block_literal_global.240
+ ___block_literal_global.246
+ ___block_literal_global.279
+ ___block_literal_global.281
+ ___block_literal_global.34
+ ___block_literal_global.360
+ ___block_literal_global.38
+ ___block_literal_global.397
+ ___block_literal_global.402
+ ___block_literal_global.407
+ ___block_literal_global.42
+ ___block_literal_global.44
+ ___block_literal_global.51
+ ___block_literal_global.75
+ ___block_literal_global.88
+ ___block_literal_global.92
+ ___block_literal_global.97
+ ___block_literal_global.98
+ _defaultDialingAppLSBundleIdentifier
+ _defaultDialingAppLSBundleIdentifier.cold.1
+ _objc_msgSend$areCallsOnOtherDevicesEnabled
+ _objc_msgSend$callNotificationEligibleDevices
+ _objc_msgSend$callsWithPredicate:limit:offset:batchSize:
+ _objc_msgSend$devicesAvailableForCallNotifications
+ _objc_msgSend$didAssociateScene
+ _objc_msgSend$initWithKey:table:locale:bundleURL:
+ _objc_msgSend$isHostEligibleForScreening
+ _objc_msgSend$isSmartHoldingGASRAvailable
+ _objc_msgSend$setCallNotificationEligibleDevices:
+ _objc_msgSend$setDidAssociateScene:
- GCC_except_table106
- GCC_except_table109
- GCC_except_table59
- _AAFMediaTypeXML_block_invoke.once
- ___103-[TUSenderIdentityCapabilities _sendNotificationsAndCallbacksComparingToOldSenderIdentityCapabilities:]_block_invoke.12
- ___103-[TUSenderIdentityCapabilities _sendNotificationsAndCallbacksComparingToOldSenderIdentityCapabilities:]_block_invoke.15
- ___103-[TUSenderIdentityCapabilities _sendNotificationsAndCallbacksComparingToOldSenderIdentityCapabilities:]_block_invoke.18
- ___103-[TUSenderIdentityCapabilities _sendNotificationsAndCallbacksComparingToOldSenderIdentityCapabilities:]_block_invoke.21
- ___129-[TUConversationManagerXPCClient launchApplicationForActivitySessionUUID:authorizedExternally:forceBackground:completionHandler:]_block_invoke.44
- ___31-[TUAudioSystemController init]_block_invoke.39
- ___34-[TUCallCenter answerWithRequest:]_block_invoke.245
- ___34-[TUCallCenter answerWithRequest:]_block_invoke.246
- ___36-[TUMomentsControllerXPCClient init]_block_invoke.3
- ___38-[TUConversationManagerXPCClient init]_block_invoke.2
- ___38-[TUConversationManagerXPCClient init]_block_invoke.7
- ___38-[TUConversationManagerXPCClient init]_block_invoke_2.3
- ___38-[TUConversationManagerXPCClient init]_block_invoke_2.8
- ___40-[TUCallHistoryControllerXPCClient init]_block_invoke.2
- ___42-[TUAudioSystemController setUplinkMuted:]_block_invoke.76
- ___42-[TUAudioSystemController setUplinkMuted:]_block_invoke.76.cold.1
- ___42-[TUCallServicesInterface defaultGreeting]_block_invoke.55
- ___44-[TUAudioSystemController setDownlinkMuted:]_block_invoke.81
- ___44-[TUAudioSystemController setDownlinkMuted:]_block_invoke.81.cold.1
- ___44-[TUCallCapabilitiesXPCClient xpcConnection]_block_invoke.8
- ___44-[TUCallCapabilitiesXPCClient xpcConnection]_block_invoke_2.9
- ___44-[TUCallServicesInterface fetchCurrentCalls]_block_invoke.26
- ___44-[TUCallServicesInterface fetchCurrentCalls]_block_invoke.27
- ___45-[TUCallCapabilitiesXPCClient _retrieveState]_block_invoke.12
- ___45-[TUMomentsControllerXPCClient xpcConnection]_block_invoke.12
- ___45-[TUMomentsControllerXPCClient xpcConnection]_block_invoke_2.13
- ___45-[TURouteController routesByUniqueIdentifier]_block_invoke
- ___45-[TURouteController routesByUniqueIdentifier]_block_invoke_2
- ___46-[TUCallHistoryManagerXPCClient xpcConnection]_block_invoke.70
- ___46-[TUCallHistoryManagerXPCClient xpcConnection]_block_invoke_2.71
- ___46-[TUCallServicesInterface _setUpXPCConnection]_block_invoke.18
- ___46-[TUCallServicesInterface _setUpXPCConnection]_block_invoke.20
- ___46-[TUCallServicesInterface _setUpXPCConnection]_block_invoke.21
- ___46-[TUConversationProviderManagerXPCClient init]_block_invoke.2
- ___46-[TUUIXPCClientConnection fetchInCallUIState:]_block_invoke.92
- ___47-[TUCallProviderManagerXPCClient xpcConnection]_block_invoke.23
- ___47-[TUCallProviderManagerXPCClient xpcConnection]_block_invoke_2.24
- ___47-[TUConversationManagerXPCClient xpcConnection]_block_invoke.92
- ___47-[TUConversationManagerXPCClient xpcConnection]_block_invoke.93
- ___49-[TUCallHistoryControllerXPCClient xpcConnection]_block_invoke.9
- ___49-[TUCallHistoryControllerXPCClient xpcConnection]_block_invoke_2.10
- ___49-[TUCallProviderManagerXPCClient sortedProviders]_block_invoke.17
- ___50-[TUCallServicesInterface fetchCurrentCallUpdates]_block_invoke.58
- ___51-[TUMomentsControllerXPCClient _registerConnection]_block_invoke.8
- ___52-[TUCallProviderManagerXPCClient defaultAppProvider]_block_invoke.13
- ___52-[TUUserNotificationProviderXPCClient xpcConnection]_block_invoke.7
- ___52-[TUUserNotificationProviderXPCClient xpcConnection]_block_invoke_2.8
- ___53-[TUCallServicesInterface resetCallProvisionalStates]_block_invoke.116
- ___54-[TUCallProviderManagerXPCClient _requestInitialState]_block_invoke.29
- ___54-[TUCallServicesInterface dialWithRequest:completion:]_block_invoke.29
- ___54-[TUCallServicesInterface dialWithRequest:completion:]_block_invoke_2.30
- ___54-[TUConversationManagerXPCClient isSharePlayAvailable]_block_invoke.18
- ___54-[TUConversationManagerXPCClient pseudonymsByCallUUID]_block_invoke.15
- ___55-[TUConversationProviderManagerXPCClient xpcConnection]_block_invoke.10
- ___55-[TUConversationProviderManagerXPCClient xpcConnection]_block_invoke.9
- ___55-[TUConversationProviderManagerXPCClient xpcConnection]_block_invoke_2.11
- ___55-[TUNeighborhoodActivityConduitXPCClient xpcConnection]_block_invoke.11
- ___55-[TUNeighborhoodActivityConduitXPCClient xpcConnection]_block_invoke_2.12
- ___56-[TUCallCenter joinConversationWithConversationRequest:]_block_invoke.259
- ___56-[TUCallServicesInterface customGreetingForAccountUUID:]_block_invoke.49
- ___56-[TUConversationManagerXPCClient advertisementsOnSystem]_block_invoke.12
- ___58-[TUConversationManagerXPCClient isScreenSharingAvailable]_block_invoke.21
- ___59-[TUSimulatedConversationControllerXPCClient xpcConnection]_block_invoke.12
- ___59-[TUSimulatedConversationControllerXPCClient xpcConnection]_block_invoke.13
- ___59-[TUSimulatedConversationControllerXPCClient xpcConnection]_block_invoke_2.14
- ___60-[TUConversationManagerXPCClient activatedConversationLinks]_block_invoke.16
- ___63-[TUUIXPCClientConnection initWithListenerEndpoint:callCenter:]_block_invoke.84
- ___63-[TUUIXPCClientConnection initWithListenerEndpoint:callCenter:]_block_invoke_2.85
- ___64-[TUProxyCall remoteVideoClient:remoteVideoAttributesDidChange:]_block_invoke.56
- ___65-[TUProxyCall remoteVideoClient:remoteScreenAttributesDidChange:]_block_invoke.55
- ___66-[TUCallCenter _existingCallsAllowDialRequest:allowVoiceWithData:]_block_invoke.220
- ___66-[TUCallCenter initWithQueue:wantsCallNotifications:featureFlags:]_block_invoke.173
- ___66-[TUCallCenter initWithQueue:wantsCallNotifications:featureFlags:]_block_invoke.176
- ___66-[TUCallServicesInterface policyForAddresses:forBundleIdentifier:]_block_invoke.100
- ___69-[TUCallHistoryController callHistoryManagerRecentCallsDispatchBlock]_block_invoke.64
- ___69-[TUCallServicesInterface willRestrictAddresses:forBundleIdentifier:]_block_invoke.103
- ___69-[TUIDSLookupManager filteredDestinationForMultiway:completionBlock:]_block_invoke.107
- ___69-[TUIDSLookupManager filteredDestinationForMultiway:completionBlock:]_block_invoke_2.109
- ___69-[TUIDSLookupManager filteredDestinationForMultiway:completionBlock:]_block_invoke_3.110
- ___70+[TUCallCapabilities _sendNotificationsAndCallbacksAfterRunningBlock:]_block_invoke.104
- ___70+[TUCallCapabilities _sendNotificationsAndCallbacksAfterRunningBlock:]_block_invoke.109
- ___70+[TUCallCapabilities _sendNotificationsAndCallbacksAfterRunningBlock:]_block_invoke.114
- ___70+[TUCallCapabilities _sendNotificationsAndCallbacksAfterRunningBlock:]_block_invoke.69
- ___70+[TUCallCapabilities _sendNotificationsAndCallbacksAfterRunningBlock:]_block_invoke.74
- ___70+[TUCallCapabilities _sendNotificationsAndCallbacksAfterRunningBlock:]_block_invoke.79
- ___70+[TUCallCapabilities _sendNotificationsAndCallbacksAfterRunningBlock:]_block_invoke.84
- ___70+[TUCallCapabilities _sendNotificationsAndCallbacksAfterRunningBlock:]_block_invoke.89
- ___70+[TUCallCapabilities _sendNotificationsAndCallbacksAfterRunningBlock:]_block_invoke.94
- ___70+[TUCallCapabilities _sendNotificationsAndCallbacksAfterRunningBlock:]_block_invoke.99
- ___70-[TUCallServicesInterface routesByUniqueIdentifierForRouteController:]_block_invoke.83
- ___70-[TUCallServicesInterface routesByUniqueIdentifierForRouteController:]_block_invoke.85
- ___70-[TUCallServicesInterface routesByUniqueIdentifierForRouteController:]_block_invoke.85.cold.1
- ___70-[TUCallServicesInterface routesByUniqueIdentifierForRouteController:]_block_invoke.88
- ___72-[TUCallServicesInterface _handleCurrentCallsChanged:callsDisconnected:]_block_invoke.115
- ___72-[TUCallServicesInterface filterStatusForAddresses:forBundleIdentifier:]_block_invoke.109
- ___73-[TUConversationManagerXPCClient incomingPendingConversationsByGroupUUID]_block_invoke.14
- ___74-[TUIDSLookupManager handleIDSQueryResultWithDestinationStatus:onService:]_block_invoke.87
- ___74-[TUIDSLookupManager handleIDSQueryResultWithDestinationStatus:onService:]_block_invoke.88
- ___74-[TUIDSLookupManager handleIDSQueryResultWithDestinationStatus:onService:]_block_invoke.89
- ___74-[TUIDSLookupManager handleIDSQueryResultWithDestinationStatus:onService:]_block_invoke.90
- ___74-[TUIDSLookupManager handleIDSQueryResultWithDestinationStatus:onService:]_block_invoke.91
- ___75-[TUConversationActivitySession launchApplicationWithForcedURL:completion:]_block_invoke.133
- ___76-[TUConversationManagerXPCClient _requestInitialStateWithCompletionHandler:]_block_invoke.77
- ___76-[TUConversationManagerXPCClient _requestInitialStateWithCompletionHandler:]_block_invoke.78
- ___76-[TUConversationManagerXPCClient _requestInitialStateWithCompletionHandler:]_block_invoke.84
- ___76-[TUConversationManagerXPCClient _requestInitialStateWithCompletionHandler:]_block_invoke.86
- ___76-[TUConversationManagerXPCClient _requestInitialStateWithCompletionHandler:]_block_invoke_2.83
- ___76-[TUConversationManagerXPCClient _requestInitialStateWithCompletionHandler:]_block_invoke_2.83.cold.1
- ___76-[TUConversationManagerXPCClient _requestInitialStateWithCompletionHandler:]_block_invoke_2.85
- ___76-[TUConversationManagerXPCClient _requestInitialStateWithCompletionHandler:]_block_invoke_2.87
- ___78-[TUCallHistoryController callHistoryManagerLoadOlderRecentCallsDispatchBlock]_block_invoke.66
- ___82-[TUCallServicesInterface isUnknownAddress:normalizedAddress:forBundleIdentifier:]_block_invoke.113
- ___88-[TUCallServicesInterface routesByUniqueIdentifierForRouteController:completionHandler:]_block_invoke.91
- ___88-[TUCallServicesInterface routesByUniqueIdentifierForRouteController:completionHandler:]_block_invoke.91.cold.1
- ___92-[TUCallServicesInterface shouldRestrictAddresses:forBundleIdentifier:performSynchronously:]_block_invoke.106
- ___93-[TUCallServicesInterface containsRestrictedHandle:forBundleIdentifier:performSynchronously:]_block_invoke.96
- ___block_literal_global.103
- ___block_literal_global.109
- ___block_literal_global.115
- ___block_literal_global.116
- ___block_literal_global.15
- ___block_literal_global.165
- ___block_literal_global.172
- ___block_literal_global.196
- ___block_literal_global.2009
- ___block_literal_global.2015
- ___block_literal_global.202
- ___block_literal_global.211
- ___block_literal_global.213
- ___block_literal_global.215
- ___block_literal_global.217
- ___block_literal_global.222
- ___block_literal_global.230
- ___block_literal_global.261
- ___block_literal_global.263
- ___block_literal_global.27
- ___block_literal_global.29
- ___block_literal_global.343
- ___block_literal_global.380
- ___block_literal_global.385
- ___block_literal_global.390
- ___block_literal_global.48
- ___block_literal_global.5
- ___block_literal_global.52
- ___block_literal_global.54
- ___block_literal_global.58
- ___block_literal_global.67
- ___block_literal_global.7
- ___block_literal_global.9
- ___block_literal_global.91
- ___block_literal_global.95
- ___block_literal_global.99
- _objc_msgSend$routesByUniqueIdentifierForRouteController:
CStrings:
+ "    callNotificationEligibleDevices: %@\n"
+ "    devicesAvailableForCallNotifications: %d\n"
+ " didAssociateScene=%d"
+ "%@ isSilenceUnknownCallersEnabledForFaceTime called, returning %d"
+ "%@ isSilenceUnknownCallersEnabledForPhone called, returning %d"
+ "%@ setSilenceUnknownCallersEnabledForFaceTime called, set to %d"
+ "%@ setSilenceUnknownCallersEnabledForPhone called, set to %d"
+ "@48@0:8@16Q24Q32Q40"
+ "ALERT_RELAY_FAILED_LEARN_MORE_GUIDANCE_MESSAGE"
+ "Calls on Other Devices capabilities changed from (devicesAvailable=%@ enabled=%d) to (devicesAvailable=%@ enabled=%d)"
+ "Intelligent Call Screening: setSelectedIntelligentCallScreeningMenuOptionForFaceTime DONE, now we have silenceUnknownCallersEnabledForFaceTime = %d"
+ "PHONE_CN_IPAD"
+ "Phone"
+ "T@\"NSArray\",&,N,V_callNotificationEligibleDevices"
+ "TB,N,V_didAssociateScene"
+ "TB,R,N,GareCallsOnOtherDevicesEnabled"
+ "TUCallCapabilitiesCallsOnOtherDevicesChangedNotification"
+ "_callNotificationEligibleDevices"
+ "_didAssociateScene"
+ "areCallsOnOtherDevicesEnabled"
+ "callNotificationEligibleDevices"
+ "callsOnOtherDevicesEnabled"
+ "callsWithPredicate:limit:offset:batchSize:"
+ "devicesAvailableForCallNotifications"
+ "didAssociateScene"
+ "initWithKey:table:locale:bundleURL:"
+ "isEligibleForScreening: NO, Answering Machine is not currently available for host"
+ "isHostEligibleForScreening"
+ "isSmartHoldingGASRAvailable"
+ "setCallNotificationEligibleDevices:"
+ "setDidAssociateScene:"
+ "smartHoldingAvailability=%i, validRemoteParticipantCount=%i validNotConferenced=%i, validSystemProvider=%i, validNotEmergencyCall=%i, validCallStatus=%i(%i), validEndpointOnCurrentDevice=%i, validIsNotVideo=%i, validLocale=%i(%@), validCaptioningAvailable=%i, isGASRAvailable=%i"
+ "smartHoldingHoldDetectionAvailability=%i, isHoldAssistDetectionEnabled=%i, isTelephonyProvider=%i, lowPowerModeEnabledBlock=%i, smartHoldingAvailability=%i, isOutgoing=%i, isEmergency=%i, isUnknownContact=%i"
- "%@ isSilenceUnknownCallersEnabledForFaceTime called"
- "%@ isSilenceUnknownCallersEnabledForPhone called"
- "%@ setSilenceUnknownCallersEnabledForFaceTime called"
- "%@ setSilenceUnknownCallersEnabledForPhone called"
- "Intelligent Call Screening: getSelectedIntelligentCallScreeningMenuOptionForFaceTime %ld"
- "Intelligent Call Screening: getSelectedIntelligentCallScreeningMenuOptionForPhone %ld"
- "Intelligent Call Screening: isReceptionistAvailable FALSE, returning default IntelligentCallScreeningMenuOptionNever"
- "Intelligent Call Screening: setSelectedIntelligentCallScreeningMenuOptionForFaceTime DONE, now we have receptionistEnabled = %d, silenceUnknownCallersEnabledForFaceTime = %d"
- "de_DE"
- "en_AU"
- "en_CA"
- "en_GB"
- "en_IN"
- "en_SG"
- "en_US"
- "es_ES"
- "es_MX"
- "es_US"
- "fr_FR"
- "ja_JP"
- "pt_BR"
- "smartHoldingAvailability=%i, validRemoteParticipantCount=%i validNotConferenced=%i, validSystemProvider=%i, validNotEmergencyCall=%i, validCallStatus=%i(%i), validEndpointOnCurrentDevice=%i, validIsNotVideo=%i, validLocale=%i(%@), validCaptioningAvailable=%i"
- "smartHoldingHoldDetectionAvailability=%i, isHoldAssistDetectionEnabled=%i, isTelephonyProvider=%i, lowPowerModeEnabledBlock=%i, smartHoldingAvailability=%i, isOutgoing=%i, isEmergency=%i"
- "zh_CN"

```
