## TelephonyUtilities

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`

```diff

-1431.200.71.2.11
-  __TEXT.__text: 0x10dd54
+1431.300.81.2.2
+  __TEXT.__text: 0x11053c
   __TEXT.__auth_stubs: 0x1160
-  __TEXT.__objc_methlist: 0x11ec4
-  __TEXT.__cstring: 0xec45
-  __TEXT.__oslogstring: 0xd785
+  __TEXT.__objc_methlist: 0x121fc
+  __TEXT.__cstring: 0xeebc
+  __TEXT.__oslogstring: 0xd984
   __TEXT.__const: 0xc4
-  __TEXT.__gcc_except_tab: 0x1224
+  __TEXT.__gcc_except_tab: 0x1238
   __TEXT.__ustring: 0xde
   __TEXT.__dlopen_cstrs: 0x72a
-  __TEXT.__unwind_info: 0x4338
-  __TEXT.__objc_classname: 0x2032
-  __TEXT.__objc_methname: 0x2fb59
-  __TEXT.__objc_methtype: 0x6b06
-  __TEXT.__objc_stubs: 0x1b520
+  __TEXT.__unwind_info: 0x43e0
+  __TEXT.__objc_classname: 0x2086
+  __TEXT.__objc_methname: 0x30393
+  __TEXT.__objc_methtype: 0x6c63
+  __TEXT.__objc_stubs: 0x1b7c0
   __DATA_CONST.__got: 0x298
-  __DATA_CONST.__const: 0x2db0
-  __DATA_CONST.__objc_classlist: 0x628
+  __DATA_CONST.__const: 0x2de8
+  __DATA_CONST.__objc_classlist: 0x640
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x398
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1efe0
-  __DATA_CONST.__objc_selrefs: 0x8ca8
-  __DATA_CONST.__objc_arraydata: 0x80
-  __AUTH_CONST.__cfstring: 0xda60
-  __AUTH_CONST.__objc_const: 0x5c30
+  __DATA_CONST.__objc_const: 0x1f598
+  __DATA_CONST.__objc_selrefs: 0x8da8
+  __DATA_CONST.__objc_arraydata: 0xd0
+  __AUTH_CONST.__cfstring: 0xdd80
+  __AUTH_CONST.__objc_const: 0x5e28
   __AUTH_CONST.__objc_intobj: 0x4e0
-  __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH_CONST.__const: 0x1cc8
+  __AUTH_CONST.__objc_arrayobj: 0x90
+  __AUTH_CONST.__const: 0x1ce8
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__auth_got: 0x8c0
-  __AUTH.__objc_data: 0x1a90
+  __AUTH.__objc_data: 0x1b80
   __DATA.__objc_protorefs: 0xc8
-  __DATA.__objc_classrefs: 0x798
-  __DATA.__objc_superrefs: 0x568
-  __DATA.__objc_ivar: 0x12dc
+  __DATA.__objc_classrefs: 0x7b8
+  __DATA.__objc_superrefs: 0x580
+  __DATA.__objc_ivar: 0x132c
   __DATA.__data: 0x2fa8
   __DATA.__bss: 0x5a0
   __DATA.__common: 0x1

   - /System/Library/PrivateFrameworks/IMFoundation.framework/IMFoundation
   - /System/Library/PrivateFrameworks/IMTransferServices.framework/IMTransferServices
   - /System/Library/PrivateFrameworks/IncomingCallFilter.framework/IncomingCallFilter
+  - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/PhoneNumbers.framework/PhoneNumbers
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/RTCReporting.framework/RTCReporting

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 7533
-  Symbols:   23834
-  CStrings:  11205
+  Functions: 7607
+  Symbols:   24063
+  CStrings:  11320
 
Symbols:
+ +[TUCallHistoryController callHistoryControllerWithCoalescingStrategy:options:shouldUpdateMetadataCache:]
+ +[TUContinuityCall supportsSecureCoding]
+ +[TUFeatureFlags civicBlurAvatarsEnabled]
+ +[TUFeatureFlags civicBlurPosterEnabled]
+ +[TUJoinContinuityConversationRequest requestForJoinWithUUID:isAudioEnabled:isVideoEnabled:]
+ +[TUJoinContinuityConversationRequest requestForStagingAreaWithUUID:]
+ +[TUJoinContinuityConversationRequest supportsSecureCoding]
+ +[TUNearbyConversationInfo supportsSecureCoding]
+ -[TUCallCenter customGreetingForAccountUUID:]
+ -[TUCallHistoryController initWithCoalescingStrategy:options:dataSource:shouldUpdateMetadataCache:]
+ -[TUCallHistoryController shouldUpdateMetadataCache]
+ -[TUCallHistoryManager reportRecentCallForConversation:withStartDate:avMode:]
+ -[TUCallHistoryManagerXPCClient reportRecentCallForConversation:withStartDate:avMode:]
+ -[TUCallServicesInterface customGreetingForAccountUUID:]
+ -[TUContinuityCall .cxx_destruct]
+ -[TUContinuityCall conversationUUID]
+ -[TUContinuityCall description]
+ -[TUContinuityCall displayName]
+ -[TUContinuityCall encodeWithCoder:]
+ -[TUContinuityCall initWithCoder:]
+ -[TUContinuityCall initWithUUID:displayName:status:conversationUUID:]
+ -[TUContinuityCall status]
+ -[TUContinuityCall uuid]
+ -[TUContinuityConversation avMode]
+ -[TUContinuityConversation initWithUUID:displayName:avMode:remoteMemberCount:remoteMemberContactIdentifiers:]
+ -[TUContinuityConversation remoteMemberContactIdentifiers]
+ -[TUContinuityConversation remoteMemberCount]
+ -[TUContinuitySessionInfo calls]
+ -[TUContinuitySessionInfo initWithDevice:calls:activeConversations:recentCalls:recentCallsContacts:]
+ -[TUFeatureFlags lagunaAudioCallsEnabled]
+ -[TUIDSLookupManager beginBatchQueryWithDestinations:services:]
+ -[TUIDSLookupManager beginCachedQueryWithDestinations:services:]
+ -[TUIDSLookupManager beginQueryWithDestinations:services:]
+ -[TUJoinContinuityConversationRequest .cxx_destruct]
+ -[TUJoinContinuityConversationRequest description]
+ -[TUJoinContinuityConversationRequest encodeWithCoder:]
+ -[TUJoinContinuityConversationRequest initWithCoder:]
+ -[TUJoinContinuityConversationRequest initWithUUID:isAudioEnabled:isVideoEnabled:wantsStagingArea:]
+ -[TUJoinContinuityConversationRequest isAudioEnabled]
+ -[TUJoinContinuityConversationRequest isVideoEnabled]
+ -[TUJoinContinuityConversationRequest uuid]
+ -[TUJoinContinuityConversationRequest wantsStagingArea]
+ -[TUNearbyConversationInfo .cxx_destruct]
+ -[TUNearbyConversationInfo avMode]
+ -[TUNearbyConversationInfo conversationUUID]
+ -[TUNearbyConversationInfo copyWithZone:]
+ -[TUNearbyConversationInfo description]
+ -[TUNearbyConversationInfo deviceHandle]
+ -[TUNearbyConversationInfo encodeWithCoder:]
+ -[TUNearbyConversationInfo hash]
+ -[TUNearbyConversationInfo initWithCoder:]
+ -[TUNearbyConversationInfo initWithConversationUUID:userProfileIdentifier:deviceHandle:avMode:]
+ -[TUNearbyConversationInfo isEqual:]
+ -[TUNearbyConversationInfo isEqualToConversationInfo:]
+ -[TUNearbyConversationInfo userProfileIdentifier]
+ -[TUNearbyDeviceHandleCapabilities initWithAVLessCapable:lagunaCapable:audioCallCapable:]
+ -[TUNearbyDeviceHandleCapabilities isAudioCallCapable]
+ -[TUNeighborhoodActivityConduit _shouldReconnect]
+ -[TUNeighborhoodActivityConduit conduitLifecycleController]
+ -[TUNeighborhoodActivityConduit isRingingFaceTimeCallsOnConnectedTVDeviceChanged:]
+ -[TUNeighborhoodActivityConduit isRingingFaceTimeCallsOnConnectedTVDevice]
+ -[TUNeighborhoodActivityConduit setConduitLifecycleController:]
+ -[TUNeighborhoodActivityConduit setIsRingingFaceTimeCallsOnConnectedTVDevice:]
+ -[TUNeighborhoodActivityConduit startConversationWith:on:completion:]
+ -[TUNeighborhoodActivityConduitXPCClient isRingingFaceTimeCallsOnConnectedTVDeviceChanged:]
+ -[TUNeighborhoodActivityConduitXPCClient isRingingFaceTimeCallsOnConnectedTVDeviceWithCompletion:]
+ -[TUNeighborhoodActivityConduitXPCClient startConversationWith:on:completion:]
+ GCC_except_table103
+ GCC_except_table123
+ GCC_except_table144
+ GCC_except_table155
+ GCC_except_table193
+ GCC_except_table214
+ GCC_except_table219
+ GCC_except_table41
+ GCC_except_table55
+ GCC_except_table65
+ _OBJC_CLASS_$_MCProfileConnection
+ _OBJC_CLASS_$_TUContinuityCall
+ _OBJC_CLASS_$_TUJoinContinuityConversationRequest
+ _OBJC_CLASS_$_TUNearbyConversationInfo
+ _OBJC_IVAR_$_TUCallHistoryController._shouldUpdateMetadataCache
+ _OBJC_IVAR_$_TUContinuityCall._conversationUUID
+ _OBJC_IVAR_$_TUContinuityCall._displayName
+ _OBJC_IVAR_$_TUContinuityCall._status
+ _OBJC_IVAR_$_TUContinuityCall._uuid
+ _OBJC_IVAR_$_TUContinuityConversation._avMode
+ _OBJC_IVAR_$_TUContinuityConversation._remoteMemberContactIdentifiers
+ _OBJC_IVAR_$_TUContinuityConversation._remoteMemberCount
+ _OBJC_IVAR_$_TUContinuitySessionInfo._calls
+ _OBJC_IVAR_$_TUJoinContinuityConversationRequest._isAudioEnabled
+ _OBJC_IVAR_$_TUJoinContinuityConversationRequest._isVideoEnabled
+ _OBJC_IVAR_$_TUJoinContinuityConversationRequest._uuid
+ _OBJC_IVAR_$_TUJoinContinuityConversationRequest._wantsStagingArea
+ _OBJC_IVAR_$_TUNearbyConversationInfo._avMode
+ _OBJC_IVAR_$_TUNearbyConversationInfo._conversationUUID
+ _OBJC_IVAR_$_TUNearbyConversationInfo._deviceHandle
+ _OBJC_IVAR_$_TUNearbyConversationInfo._userProfileIdentifier
+ _OBJC_IVAR_$_TUNearbyDeviceHandleCapabilities._audioCallCapable
+ _OBJC_IVAR_$_TUNeighborhoodActivityConduit._conduitLifecycleController
+ _OBJC_IVAR_$_TUNeighborhoodActivityConduit._isRingingFaceTimeCallsOnConnectedTVDevice
+ _OBJC_METACLASS_$_TUContinuityCall
+ _OBJC_METACLASS_$_TUJoinContinuityConversationRequest
+ _OBJC_METACLASS_$_TUNearbyConversationInfo
+ _TUCallScreeningDisabledMDMProfile
+ __OBJC_$_CLASS_METHODS_TUContinuityCall
+ __OBJC_$_CLASS_METHODS_TUFeatureFlags
+ __OBJC_$_CLASS_METHODS_TUJoinContinuityConversationRequest
+ __OBJC_$_CLASS_METHODS_TUNearbyConversationInfo
+ __OBJC_$_CLASS_PROP_LIST_TUContinuityCall
+ __OBJC_$_CLASS_PROP_LIST_TUFeatureFlags
+ __OBJC_$_CLASS_PROP_LIST_TUFeatureFlags.282
+ __OBJC_$_CLASS_PROP_LIST_TUJoinContinuityConversationRequest
+ __OBJC_$_CLASS_PROP_LIST_TUNearbyConversationInfo
+ __OBJC_$_INSTANCE_METHODS_TUContinuityCall
+ __OBJC_$_INSTANCE_METHODS_TUJoinContinuityConversationRequest
+ __OBJC_$_INSTANCE_METHODS_TUNearbyConversationInfo
+ __OBJC_$_INSTANCE_VARIABLES_TUContinuityCall
+ __OBJC_$_INSTANCE_VARIABLES_TUJoinContinuityConversationRequest
+ __OBJC_$_INSTANCE_VARIABLES_TUNearbyConversationInfo
+ __OBJC_$_PROP_LIST_TUContinuityCall
+ __OBJC_$_PROP_LIST_TUFeatureFlags.286
+ __OBJC_$_PROP_LIST_TUJoinContinuityConversationRequest
+ __OBJC_$_PROP_LIST_TUNearbyConversationInfo
+ __OBJC_$_PROTOCOL_CLASS_METHODS_TUFeatureFlags
+ __OBJC_CLASS_PROTOCOLS_$_TUContinuityCall
+ __OBJC_CLASS_PROTOCOLS_$_TUJoinContinuityConversationRequest
+ __OBJC_CLASS_PROTOCOLS_$_TUNearbyConversationInfo
+ __OBJC_CLASS_RO_$_TUContinuityCall
+ __OBJC_CLASS_RO_$_TUJoinContinuityConversationRequest
+ __OBJC_CLASS_RO_$_TUNearbyConversationInfo
+ __OBJC_METACLASS_RO_$_TUContinuityCall
+ __OBJC_METACLASS_RO_$_TUJoinContinuityConversationRequest
+ __OBJC_METACLASS_RO_$_TUNearbyConversationInfo
+ ___42-[TUCallServicesInterface defaultGreeting]_block_invoke.51
+ ___46-[TUCallHistoryManagerXPCClient xpcConnection]_block_invoke.69
+ ___46-[TUCallHistoryManagerXPCClient xpcConnection]_block_invoke_2.70
+ ___50-[TUCallServicesInterface fetchCurrentCallUpdates]_block_invoke.54
+ ___53-[TUCallServicesInterface resetCallProvisionalStates]_block_invoke.103
+ ___53-[TUNeighborhoodActivityConduit _requestInitialState]_block_invoke_2.204
+ ___53-[TUNeighborhoodActivityConduit _requestInitialState]_block_invoke_2.204.cold.1
+ ___56-[TUCallServicesInterface customGreetingForAccountUUID:]_block_invoke
+ ___56-[TUCallServicesInterface customGreetingForAccountUUID:]_block_invoke.45
+ ___56-[TUCallServicesInterface customGreetingForAccountUUID:]_block_invoke.cold.1
+ ___58-[TUIDSLookupManager beginQueryWithDestinations:services:]_block_invoke
+ ___63-[TUIDSLookupManager beginBatchQueryWithDestinations:services:]_block_invoke
+ ___63-[TUIDSLookupManager beginBatchQueryWithDestinations:services:]_block_invoke_2
+ ___64-[TUIDSLookupManager beginCachedQueryWithDestinations:services:]_block_invoke
+ ___66-[TUCallServicesInterface policyForAddresses:forBundleIdentifier:]_block_invoke.87
+ ___69-[TUCallHistoryController callHistoryManagerRecentCallsDispatchBlock]_block_invoke.65
+ ___69-[TUCallServicesInterface willRestrictAddresses:forBundleIdentifier:]_block_invoke.90
+ ___70-[TUCallServicesInterface routesByUniqueIdentifierForRouteController:]_block_invoke.75
+ ___70-[TUCallServicesInterface routesByUniqueIdentifierForRouteController:]_block_invoke.77.cold.1
+ ___70-[TUCallServicesInterface routesByUniqueIdentifierForRouteController:]_block_invoke.80
+ ___72-[TUCallServicesInterface _handleCurrentCallsChanged:callsDisconnected:]_block_invoke.102
+ ___72-[TUCallServicesInterface filterStatusForAddresses:forBundleIdentifier:]_block_invoke.96
+ ___78-[TUCallHistoryController callHistoryManagerLoadOlderRecentCallsDispatchBlock]_block_invoke.67
+ ___78-[TUNeighborhoodActivityConduitXPCClient startConversationWith:on:completion:]_block_invoke
+ ___78-[TUNeighborhoodActivityConduitXPCClient startConversationWith:on:completion:]_block_invoke_2
+ ___78-[TUNeighborhoodActivityConduitXPCClient startConversationWith:on:completion:]_block_invoke_2.cold.1
+ ___82-[TUCallServicesInterface isUnknownAddress:normalizedAddress:forBundleIdentifier:]_block_invoke.100
+ ___86-[TUCallHistoryManagerXPCClient reportRecentCallForConversation:withStartDate:avMode:]_block_invoke
+ ___86-[TUCallHistoryManagerXPCClient reportRecentCallForConversation:withStartDate:avMode:]_block_invoke_2
+ ___86-[TUCallHistoryManagerXPCClient reportRecentCallForConversation:withStartDate:avMode:]_block_invoke_2.cold.1
+ ___91-[TUNeighborhoodActivityConduitXPCClient isRingingFaceTimeCallsOnConnectedTVDeviceChanged:]_block_invoke
+ ___92-[TUCallServicesInterface shouldRestrictAddresses:forBundleIdentifier:performSynchronously:]_block_invoke.93
+ ___93-[TUCallServicesInterface containsRestrictedHandle:forBundleIdentifier:performSynchronously:]_block_invoke.83
+ ___98-[TUNeighborhoodActivityConduitXPCClient isRingingFaceTimeCallsOnConnectedTVDeviceWithCompletion:]_block_invoke
+ ___98-[TUNeighborhoodActivityConduitXPCClient isRingingFaceTimeCallsOnConnectedTVDeviceWithCompletion:]_block_invoke_2
+ ___98-[TUNeighborhoodActivityConduitXPCClient isRingingFaceTimeCallsOnConnectedTVDeviceWithCompletion:]_block_invoke_2.cold.1
+ ___block_descriptor_40_e8_32s_e20_v20?0B8"NSError"12ls32l8
+ ___block_literal_global.143
+ ___block_literal_global.1455
+ ___block_literal_global.186
+ ___block_literal_global.214
+ ___block_literal_global.246
+ ___block_literal_global.273
+ ___block_literal_global.278
+ ___block_literal_global.64
+ ___block_literal_global.66
+ ___block_literal_global.68
+ ___block_literal_global.70
+ ___block_literal_global.72
+ ___block_literal_global.80
+ ___block_literal_global.95
+ ___block_literal_global.99
+ __unnamed_array_storage.228
+ _objc_msgSend$_shouldReconnect
+ _objc_msgSend$beginBatchQueryWithDestinations:services:
+ _objc_msgSend$beginCachedQueryWithDestinations:services:
+ _objc_msgSend$beginQueryWithDestinations:services:
+ _objc_msgSend$callHistoryControllerWithCoalescingStrategy:options:shouldUpdateMetadataCache:
+ _objc_msgSend$canCreateConversations
+ _objc_msgSend$conduitLifecycleController
+ _objc_msgSend$conversationUUID
+ _objc_msgSend$customGreetingForAccountUUID:
+ _objc_msgSend$customSandboxedURLGreetingForAccountUUID:withCompletion:
+ _objc_msgSend$initWithAVLessCapable:lagunaCapable:audioCallCapable:
+ _objc_msgSend$initWithCoalescingStrategy:options:dataSource:shouldUpdateMetadataCache:
+ _objc_msgSend$initWithConversationUUID:userProfileIdentifier:deviceHandle:avMode:
+ _objc_msgSend$initWithDevice:calls:activeConversations:recentCalls:recentCallsContacts:
+ _objc_msgSend$initWithUUID:displayName:avMode:remoteMemberCount:remoteMemberContactIdentifiers:
+ _objc_msgSend$initWithUUID:displayName:status:conversationUUID:
+ _objc_msgSend$initWithUUID:isAudioEnabled:isVideoEnabled:wantsStagingArea:
+ _objc_msgSend$isAudioCallCapable
+ _objc_msgSend$isEqualToConversationInfo:
+ _objc_msgSend$isLiveVoicemailAllowed
+ _objc_msgSend$isRingingFaceTimeCallsOnConnectedTVDeviceChanged:
+ _objc_msgSend$isRingingFaceTimeCallsOnConnectedTVDeviceWithCompletion:
+ _objc_msgSend$languageIdentifier
+ _objc_msgSend$mergedActiveRemoteParticipants
+ _objc_msgSend$reportRecentCallForConversation:withStartDate:avMode:
+ _objc_msgSend$sharedConnection
+ _objc_msgSend$shouldKeepConduitAlive
+ _objc_msgSend$shouldUpdateMetadataCache
+ _objc_msgSend$startConversationWith:on:completion:
+ _objc_msgSend$userProfileIdentifier
- -[TUCallHistoryController initWithCoalescingStrategy:options:dataSource:]
- -[TUCallHistoryManager reportRecentCallForConversation:withStartDate:]
- -[TUCallHistoryManagerXPCClient reportRecentCallForConversation:withStartDate:]
- -[TUContinuityConversation initWithUUID:displayName:]
- -[TUContinuitySessionInfo initWithDevice:activeConversations:recentCalls:recentCallsContacts:]
- -[TUNearbyDeviceHandleCapabilities initWithAVLessCapable:lagunaCapable:]
- GCC_except_table102
- GCC_except_table120
- GCC_except_table126
- GCC_except_table154
- GCC_except_table192
- GCC_except_table213
- GCC_except_table218
- GCC_except_table40
- __OBJC_$_PROP_LIST_TUFeatureFlags.276
- ___42-[TUCallServicesInterface defaultGreeting]_block_invoke.47
- ___46-[TUCallHistoryManagerXPCClient xpcConnection]_block_invoke.68
- ___46-[TUCallHistoryManagerXPCClient xpcConnection]_block_invoke_2.69
- ___50-[TUCallServicesInterface fetchCurrentCallUpdates]_block_invoke.51
- ___53-[TUCallServicesInterface resetCallProvisionalStates]_block_invoke.100
- ___65-[TUIDSLookupManager beginQueryWithDestinations:includeMessages:]_block_invoke
- ___66-[TUCallServicesInterface policyForAddresses:forBundleIdentifier:]_block_invoke.84
- ___69-[TUCallHistoryController callHistoryManagerRecentCallsDispatchBlock]_block_invoke.64
- ___69-[TUCallServicesInterface willRestrictAddresses:forBundleIdentifier:]_block_invoke.87
- ___70-[TUCallServicesInterface routesByUniqueIdentifierForRouteController:]_block_invoke.72
- ___70-[TUCallServicesInterface routesByUniqueIdentifierForRouteController:]_block_invoke.74
- ___70-[TUCallServicesInterface routesByUniqueIdentifierForRouteController:]_block_invoke.74.cold.1
- ___70-[TUIDSLookupManager beginBatchQueryWithDestinations:includeMessages:]_block_invoke
- ___70-[TUIDSLookupManager beginBatchQueryWithDestinations:includeMessages:]_block_invoke_2
- ___71-[TUIDSLookupManager beginCachedQueryWithDestinations:includeMessages:]_block_invoke
- ___72-[TUCallServicesInterface _handleCurrentCallsChanged:callsDisconnected:]_block_invoke.99
- ___72-[TUCallServicesInterface filterStatusForAddresses:forBundleIdentifier:]_block_invoke.93
- ___78-[TUCallHistoryController callHistoryManagerLoadOlderRecentCallsDispatchBlock]_block_invoke.66
- ___79-[TUCallHistoryManagerXPCClient reportRecentCallForConversation:withStartDate:]_block_invoke
- ___79-[TUCallHistoryManagerXPCClient reportRecentCallForConversation:withStartDate:]_block_invoke_2
- ___79-[TUCallHistoryManagerXPCClient reportRecentCallForConversation:withStartDate:]_block_invoke_2.cold.1
- ___82-[TUCallServicesInterface isUnknownAddress:normalizedAddress:forBundleIdentifier:]_block_invoke.97
- ___92-[TUCallServicesInterface shouldRestrictAddresses:forBundleIdentifier:performSynchronously:]_block_invoke.90
- ___93-[TUCallServicesInterface containsRestrictedHandle:forBundleIdentifier:performSynchronously:]_block_invoke.80
- ___block_literal_global.113
- ___block_literal_global.1443
- ___block_literal_global.184
- ___block_literal_global.199
- ___block_literal_global.221
- ___block_literal_global.248
- ___block_literal_global.253
- ___block_literal_global.57
- ___block_literal_global.69
- ___block_literal_global.75
- ___block_literal_global.83
- _objc_msgSend$beginBatchQueryWithDestinations:includeMessages:
- _objc_msgSend$beginCachedQueryWithDestinations:includeMessages:
- _objc_msgSend$beginQueryWithDestinations:includeMessages:
- _objc_msgSend$initWithAVLessCapable:lagunaCapable:
- _objc_msgSend$initWithCoalescingStrategy:options:dataSource:
- _objc_msgSend$initWithDevice:activeConversations:recentCalls:recentCallsContacts:
- _objc_msgSend$initWithUUID:displayName:
- _objc_msgSend$localeIdentifier
- _objc_msgSend$reportRecentCallForConversation:withStartDate:
CStrings:
+ "\x02!"
+ "\x05"
+ " avMode=%lu"
+ " avMode=%zd"
+ " callsCount=%zd"
+ " canCreateConversations=%@"
+ " conversationUUID=%@"
+ " deletionDate=%@"
+ " isAudioCallCapable=%d"
+ " remoteMemberContactIdentifiersCount=%zd"
+ " remoteMemberCount=%zd"
+ " self.groupUUID=%@"
+ " self.invitedMemberHandles=%@"
+ " self.originatorHandle=%@"
+ " status=%i"
+ " userProfileIdentifier=%@"
+ "&\x11"
+ "1\x18"
+ "@\"<TUConduitLifecycleController>\""
+ "@28@0:8B16B20B24"
+ "@32@0:8@16B24B28"
+ "@36@0:8@16B24B28B32"
+ "@36@0:8Q16Q24B32"
+ "@44@0:8@16@24i32@36"
+ "@44@0:8Q16Q24@32B40"
+ "@48@0:8@16@24@32Q40"
+ "@56@0:8@16@24Q32q40@48"
+ "ALERT_BLOCKED_REMOTE_PARTICIPANT_REMOTE_JOINING_TITLE"
+ "ALERT_BLOCKED_REMOTE_PARTICIPANT_SELF_JOINING_TITLE"
+ "Error starting conversation on %@: %@"
+ "Error using remote object proxy when requesting custom greeting: %@"
+ "FaceTimeApp"
+ "Failed to get initial state for ringing status: %@"
+ "LVMAllowAllLocales"
+ "LVMAllowAllLocales set, allowing everything"
+ "LVMLocales"
+ "LagunaAudioCallsEnabled"
+ "NeighborhoodActivityConduitClientsShouldConnectNotification"
+ "Process does initialize conduitLifeCycleController, are we keeping NAC alive? %d"
+ "Process does not initialize conduitLifecycleController, deferring to processes that do"
+ "Proxying defaultGreetingForAccountUUID:"
+ "SystemWake"
+ "T@\"<TUConduitLifecycleController>\",&,N,V_conduitLifecycleController"
+ "T@\"NSArray\",R,N,V_calls"
+ "T@\"NSArray\",R,N,V_remoteMemberContactIdentifiers"
+ "T@\"NSString\",R,C,N,V_userProfileIdentifier"
+ "T@\"NSUUID\",R,C,N,V_conversationUUID"
+ "T@\"NSUUID\",R,N,V_conversationUUID"
+ "T@\"TUNearbyDeviceHandle\",R,C,N,V_deviceHandle"
+ "TB,N,V_isRingingFaceTimeCallsOnConnectedTVDevice"
+ "TB,R,N,GisAudioCallCapable,V_audioCallCapable"
+ "TB,R,N,V_isAudioEnabled"
+ "TB,R,N,V_isVideoEnabled"
+ "TB,R,N,V_shouldUpdateMetadataCache"
+ "TB,R,N,V_wantsStagingArea"
+ "TQ,R,N,V_avMode"
+ "TUConduitXPCClient: NeighborhoodActivityConduit restarted and requested re-connection"
+ "TUContinuityCall"
+ "TUJoinContinuityConversationRequest"
+ "TUNearbyConversationInfo"
+ "Ti,R,N,V_status"
+ "Tq,R,N,V_remoteMemberCount"
+ "Using LVMSupportedLocales from default: %@"
+ "Using LVMSupportedLocales from serverBag: %@"
+ "Vv32@0:8@\"NSUUID\"16@?<v@?@\"TUSandboxExtendedURL\">24"
+ "Vv40@0:8@\"TUConversation\"16@\"NSDate\"24Q32"
+ "Vv40@0:8@16@24Q32"
+ "_audioCallCapable"
+ "_conduitLifecycleController"
+ "_conversationUUID"
+ "_isAudioEnabled"
+ "_isRingingFaceTimeCallsOnConnectedTVDevice"
+ "_isVideoEnabled"
+ "_remoteMemberContactIdentifiers"
+ "_remoteMemberCount"
+ "_shouldReconnect"
+ "_shouldUpdateMetadataCache"
+ "_status"
+ "_userProfileIdentifier"
+ "audioCallCapable"
+ "beginBatchQueryWithDestinations:services:"
+ "beginCachedQueryWithDestinations:services:"
+ "beginQueryWithDestinations:services:"
+ "callHistoryControllerWithCoalescingStrategy:options:shouldUpdateMetadataCache:"
+ "civicBlurAvatars"
+ "civicBlurAvatarsEnabled"
+ "civicBlurPoster"
+ "civicBlurPosterEnabled"
+ "conduitLifecycleController"
+ "conversationUUID"
+ "customGreetingForAccountUUID:"
+ "customSandboxedURLGreetingForAccountUUID:withCompletion:"
+ "en-CA"
+ "en-GU"
+ "en-UM"
+ "en-US"
+ "en-VI"
+ "initWithAVLessCapable:lagunaCapable:audioCallCapable:"
+ "initWithCoalescingStrategy:options:dataSource:shouldUpdateMetadataCache:"
+ "initWithConversationUUID:userProfileIdentifier:deviceHandle:avMode:"
+ "initWithDevice:calls:activeConversations:recentCalls:recentCallsContacts:"
+ "initWithUUID:displayName:avMode:remoteMemberCount:remoteMemberContactIdentifiers:"
+ "initWithUUID:displayName:status:conversationUUID:"
+ "initWithUUID:isAudioEnabled:isVideoEnabled:wantsStagingArea:"
+ "isAudioCallCapable"
+ "isEqualToConversationInfo:"
+ "isLiveVoicemailAllowed"
+ "isRingingFaceTimeCallsOnConnectedTVDevice"
+ "isRingingFaceTimeCallsOnConnectedTVDeviceChanged:"
+ "isRingingFaceTimeCallsOnConnectedTVDeviceWithCompletion:"
+ "lagunaAudioCallsEnabled"
+ "languageIdentifier"
+ "lvm-supported-locales"
+ "remoteMemberContactIdentifiers"
+ "remoteMemberCount"
+ "reportRecentCallForConversation:withStartDate:avMode:"
+ "requestForJoinWithUUID:isAudioEnabled:isVideoEnabled:"
+ "requestForStagingAreaWithUUID:"
+ "setConduitLifecycleController:"
+ "setIsRingingFaceTimeCallsOnConnectedTVDevice:"
+ "sharedConnection"
+ "shouldKeepConduitAlive"
+ "shouldUpdateMetadataCache"
+ "startConversationWith:on:completion:"
+ "systemWake"
+ "userProfileIdentifier"
+ "v24@0:8@?<v@?B@\"NSError\">16"
+ "v40@0:8@\"NSSet\"16@\"TUNearbyDeviceHandle\"24@?<v@?@\"NSUUID\"@\"NSError\">32"
+ "v40@0:8@\"TUConversation\"16@\"NSDate\"24Q32"
+ "v40@0:8@16@24Q32"
- "\x16"
- "!\x18"
- "@24@0:8B16B20"
- "@40@0:8Q16Q24@32"
- "TUConduitXPCClient: callservicesd restarted and requested re-connection"
- "Vv32@0:8@\"TUConversation\"16@\"NSDate\"24"
- "en_CA"
- "en_US"
- "initWithAVLessCapable:lagunaCapable:"
- "initWithCoalescingStrategy:options:dataSource:"
- "initWithDevice:activeConversations:recentCalls:recentCallsContacts:"
- "initWithUUID:displayName:"
- "localeIdentifier"
- "reportRecentCallForConversation:withStartDate:"
- "v32@0:8@\"TUConversation\"16@\"NSDate\"24"

```
