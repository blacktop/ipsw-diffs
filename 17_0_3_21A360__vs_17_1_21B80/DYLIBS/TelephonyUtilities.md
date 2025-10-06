## TelephonyUtilities

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`

```diff

-1431.100.4.2.39
-  __TEXT.__text: 0x10ce2c
-  __TEXT.__auth_stubs: 0x1150
-  __TEXT.__objc_methlist: 0x11df4
-  __TEXT.__cstring: 0xebf8
-  __TEXT.__oslogstring: 0xd617
+1431.200.71.2.11
+  __TEXT.__text: 0x10dd54
+  __TEXT.__auth_stubs: 0x1160
+  __TEXT.__objc_methlist: 0x11ec4
+  __TEXT.__cstring: 0xec45
+  __TEXT.__oslogstring: 0xd785
   __TEXT.__const: 0xc4
-  __TEXT.__gcc_except_tab: 0x1288
+  __TEXT.__gcc_except_tab: 0x1224
   __TEXT.__ustring: 0xde
-  __TEXT.__dlopen_cstrs: 0x7de
-  __TEXT.__unwind_info: 0x4374
-  __TEXT.__objc_classname: 0x2035
-  __TEXT.__objc_methname: 0x2f933
-  __TEXT.__objc_methtype: 0x6c09
-  __TEXT.__objc_stubs: 0x1b4c0
+  __TEXT.__dlopen_cstrs: 0x72a
+  __TEXT.__unwind_info: 0x4338
+  __TEXT.__objc_classname: 0x2032
+  __TEXT.__objc_methname: 0x2fb59
+  __TEXT.__objc_methtype: 0x6b06
+  __TEXT.__objc_stubs: 0x1b520
   __DATA_CONST.__got: 0x298
-  __DATA_CONST.__const: 0x2e60
+  __DATA_CONST.__const: 0x2db0
   __DATA_CONST.__objc_classlist: 0x628
   __DATA_CONST.__objc_catlist: 0xb8
-  __DATA_CONST.__objc_protolist: 0x3a0
+  __DATA_CONST.__objc_protolist: 0x398
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1ef08
-  __DATA_CONST.__objc_selrefs: 0x8c80
-  __DATA_CONST.__objc_arraydata: 0xa0
-  __AUTH_CONST.__cfstring: 0xd920
-  __AUTH_CONST.__objc_const: 0x5ba0
-  __AUTH_CONST.__objc_intobj: 0x4f8
-  __AUTH_CONST.__objc_arrayobj: 0x90
-  __AUTH_CONST.__const: 0x1ca8
+  __DATA_CONST.__objc_const: 0x1efe0
+  __DATA_CONST.__objc_selrefs: 0x8ca8
+  __DATA_CONST.__objc_arraydata: 0x80
+  __AUTH_CONST.__cfstring: 0xda60
+  __AUTH_CONST.__objc_const: 0x5c30
+  __AUTH_CONST.__objc_intobj: 0x4e0
+  __AUTH_CONST.__objc_arrayobj: 0x60
+  __AUTH_CONST.__const: 0x1cc8
   __AUTH_CONST.__objc_doubleobj: 0x40
-  __AUTH_CONST.__auth_got: 0x8b8
+  __AUTH_CONST.__auth_got: 0x8c0
   __AUTH.__objc_data: 0x1a90
   __DATA.__objc_protorefs: 0xc8
-  __DATA.__objc_classrefs: 0x788
+  __DATA.__objc_classrefs: 0x798
   __DATA.__objc_superrefs: 0x568
-  __DATA.__objc_ivar: 0x12c8
-  __DATA.__data: 0x3020
-  __DATA.__bss: 0x578
+  __DATA.__objc_ivar: 0x12dc
+  __DATA.__data: 0x2fa8
+  __DATA.__bss: 0x5a0
   __DATA.__common: 0x1
   __DATA_DIRTY.__objc_data: 0x2300
   __DATA_DIRTY.__bss: 0x228

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F9E7CBB3-46EC-36C4-8B4F-EF2B91EE0B6E
-  Functions: 7527
-  Symbols:   23820
-  CStrings:  12932
+  UUID: EAF4A032-94A1-3B43-B838-FA81076974E9
+  Functions: 7533
+  Symbols:   23834
+  CStrings:  12952
 
Symbols:
+ +[TUContinuityConversation supportsSecureCoding]
+ +[TUMomentsController sharedInstance]
+ +[TUMomentsMessageSendRequest supportsSecureCoding]
+ +[TUNeighborhoodActivityConduit isConduitAvailable]
+ -[TUAudioSystemController clearUplinkMutedCache]
+ -[TUBatchFetchRequestProcessingResult .cxx_destruct]
+ -[TUBatchFetchRequestProcessingResult allHandlesFromFetchRequests]
+ -[TUBatchFetchRequestProcessingResult fetchRequestResults]
+ -[TUBatchFetchRequestProcessingResult handleToFetchRequest]
+ -[TUBatchFetchRequestProcessingResult handlesToBatchFetch]
+ -[TUBatchFetchRequestProcessingResult initWithHandleToFetchRequest:handlesToBatchFetch:allHandlesFromFetchRequests:fetchRequestResults:]
+ -[TUCallCenter requestVideoUpgradeForCall:originatingUIType:]
+ -[TUContactsDataProvider executeBatchFetchRequests:]
+ -[TUContactsDataProvider processBatchFetchRequests:]
+ -[TUContactsDataProvider resultForSingleHandleFetchRequest:fetchedContacts:]
+ -[TUContactsDataProvider shouldIgnoreHandle:withFetchRequest:]
+ -[TUContinuityConversation .cxx_destruct]
+ -[TUContinuityConversation description]
+ -[TUContinuityConversation displayName]
+ -[TUContinuityConversation encodeWithCoder:]
+ -[TUContinuityConversation initWithCoder:]
+ -[TUContinuityConversation initWithUUID:displayName:]
+ -[TUContinuityConversation uuid]
+ -[TUContinuitySessionInfo activeConversations]
+ -[TUContinuitySessionInfo copyWithZone:]
+ -[TUContinuitySessionInfo initWithDevice:activeConversations:recentCalls:recentCallsContacts:]
+ -[TUConversation isContinuitySession]
+ -[TUConversation updateParticipantMediaPrioritiesWithConversation:].cold.1
+ -[TUConversationActivitySession initWithActivity:state:uuid:endpoint:locallyInitiated:timestamp:isFirstJoin:activeRemoteParticipants:isLocalParticipantActive:applicationState:]
+ -[TUConversationActivitySession isLocalParticipantActive]
+ -[TUConversationMember(DisplayName) needsContactLookupForDisplayName]
+ -[TUFeatureFlags faceTimeCallSpamReportEnabled]
+ -[TUFeatureFlags faceTimeGroupCallSpamReportEnabled]
+ -[TUFeatureFlags lagunaIncomingCallsEnabled]
+ -[TUFeatureFlags videoMessagingSpamReportEnabled]
+ -[TUIDSLookupManager batchQuerySearchShareNameAndPhotoController]
+ -[TUIDSLookupManager beginQueryWithRefreshForDestination:onService:]
+ -[TUIDSLookupManager idsNameAndPhotoStatuses]
+ -[TUIDSLookupManager isNameAndPhotoAvailableForDestination:]
+ -[TUIDSLookupManager setBatchQuerySearchShareNameAndPhotoController:]
+ -[TUMomentsController addDelegate:]
+ -[TUMomentsController delegates]
+ -[TUMomentsController initWithDataSource:]
+ -[TUMomentsController removeDelegate:]
+ -[TUMomentsController sendVideoMessageWithRequest:completion:]
+ -[TUMomentsController setDelegates:]
+ -[TUMomentsControllerXPCClient sendVideoMessageWithRequest:completion:]
+ -[TUMomentsMessageSendRequest .cxx_destruct]
+ -[TUMomentsMessageSendRequest conversationID]
+ -[TUMomentsMessageSendRequest destinationHandles]
+ -[TUMomentsMessageSendRequest encodeWithCoder:]
+ -[TUMomentsMessageSendRequest initWithCoder:]
+ -[TUMomentsMessageSendRequest initWithSessionUUID:conversationID:senderHandle:destinationHandles:]
+ -[TUMomentsMessageSendRequest senderHandle]
+ -[TUMomentsMessageSendRequest sessionUUID]
+ -[TUNearbyDeviceHandleCapabilities initWithAVLessCapable:lagunaCapable:]
+ -[TUNeighborhoodActivityConduitXPCClient xpcConnection].cold.1
+ GCC_except_table154
+ GCC_except_table170
+ GCC_except_table192
+ GCC_except_table213
+ GCC_except_table218
+ GCC_except_table39
+ GCC_except_table42
+ _MGGetStringAnswer
+ _OBJC_CLASS_$_TUBatchFetchRequestProcessingResult
+ _OBJC_CLASS_$_TUContinuityConversation
+ _OBJC_CLASS_$_TUMomentsMessageSendRequest
+ _OBJC_IVAR_$_TUBatchFetchRequestProcessingResult._allHandlesFromFetchRequests
+ _OBJC_IVAR_$_TUBatchFetchRequestProcessingResult._fetchRequestResults
+ _OBJC_IVAR_$_TUBatchFetchRequestProcessingResult._handleToFetchRequest
+ _OBJC_IVAR_$_TUBatchFetchRequestProcessingResult._handlesToBatchFetch
+ _OBJC_IVAR_$_TUContinuityConversation._displayName
+ _OBJC_IVAR_$_TUContinuityConversation._uuid
+ _OBJC_IVAR_$_TUContinuitySessionInfo._activeConversations
+ _OBJC_IVAR_$_TUConversationActivitySession._localParticipantActive
+ _OBJC_IVAR_$_TUIDSLookupManager._batchQuerySearchShareNameAndPhotoController
+ _OBJC_IVAR_$_TUIDSLookupManager._idsNameAndPhotoStatuses
+ _OBJC_IVAR_$_TUMomentsController._delegates
+ _OBJC_IVAR_$_TUMomentsMessageSendRequest._conversationID
+ _OBJC_IVAR_$_TUMomentsMessageSendRequest._destinationHandles
+ _OBJC_IVAR_$_TUMomentsMessageSendRequest._senderHandle
+ _OBJC_IVAR_$_TUMomentsMessageSendRequest._sessionUUID
+ _OBJC_IVAR_$_TUNearbyDeviceHandleCapabilities._avLessCapable
+ _OBJC_IVAR_$_TUNearbyDeviceHandleCapabilities._lagunaCapable
+ _OBJC_METACLASS_$_TUBatchFetchRequestProcessingResult
+ _OBJC_METACLASS_$_TUContinuityConversation
+ _OBJC_METACLASS_$_TUMomentsMessageSendRequest
+ _TUActionLiveVoicemailSettings
+ _TUBundleIdentifierNameAndPhotoUtilities
+ _TUIsStoreDemoModeEnabled
+ _TUIsStoreDemoModeEnabled.onceToken
+ _TUIsStoreDemoModeEnabled.storeDemoModeEnabled
+ __OBJC_$_CLASS_METHODS_TUContinuityConversation
+ __OBJC_$_CLASS_METHODS_TUConversationMember(DisplayName)
+ __OBJC_$_CLASS_METHODS_TUMomentsMessageSendRequest
+ __OBJC_$_CLASS_METHODS_TUNeighborhoodActivityConduit
+ __OBJC_$_CLASS_PROP_LIST_TUContinuityConversation
+ __OBJC_$_CLASS_PROP_LIST_TUMomentsMessageSendRequest
+ __OBJC_$_CLASS_PROP_LIST_TUNeighborhoodActivityConduit
+ __OBJC_$_INSTANCE_METHODS_TUBatchFetchRequestProcessingResult
+ __OBJC_$_INSTANCE_METHODS_TUContinuityConversation
+ __OBJC_$_INSTANCE_METHODS_TUConversationMember(DisplayName)
+ __OBJC_$_INSTANCE_METHODS_TUMomentsMessageSendRequest
+ __OBJC_$_INSTANCE_VARIABLES_TUBatchFetchRequestProcessingResult
+ __OBJC_$_INSTANCE_VARIABLES_TUContinuityConversation
+ __OBJC_$_INSTANCE_VARIABLES_TUMomentsMessageSendRequest
+ __OBJC_$_PROP_LIST_TUBatchFetchRequestProcessingResult
+ __OBJC_$_PROP_LIST_TUContinuityConversation
+ __OBJC_$_PROP_LIST_TUFeatureFlags.276
+ __OBJC_$_PROP_LIST_TUMomentsMessageSendRequest
+ __OBJC_CLASS_PROTOCOLS_$_TUContinuityConversation
+ __OBJC_CLASS_PROTOCOLS_$_TUMomentsMessageSendRequest
+ __OBJC_CLASS_RO_$_TUBatchFetchRequestProcessingResult
+ __OBJC_CLASS_RO_$_TUContinuityConversation
+ __OBJC_CLASS_RO_$_TUMomentsMessageSendRequest
+ __OBJC_METACLASS_RO_$_TUBatchFetchRequestProcessingResult
+ __OBJC_METACLASS_RO_$_TUContinuityConversation
+ __OBJC_METACLASS_RO_$_TUMomentsMessageSendRequest
+ ___35-[TUMomentsController addDelegate:]_block_invoke
+ ___37+[TUMomentsController sharedInstance]_block_invoke
+ ___38-[TUMomentsController removeDelegate:]_block_invoke
+ ___42-[TUAudioSystemController setUplinkMuted:]_block_invoke.69
+ ___42-[TUAudioSystemController setUplinkMuted:]_block_invoke.69.cold.1
+ ___42-[TUMomentsController initWithDataSource:]_block_invoke
+ ___44-[TUAudioSystemController setDownlinkMuted:]_block_invoke.74
+ ___44-[TUAudioSystemController setDownlinkMuted:]_block_invoke.74.cold.1
+ ___51+[TUNeighborhoodActivityConduit isConduitAvailable]_block_invoke
+ ___51-[TUMomentsController registerProvider:completion:]_block_invoke.47
+ ___53-[TUNeighborhoodActivityConduit _requestInitialState]_block_invoke.195
+ ___53-[TUNeighborhoodActivityConduit _requestInitialState]_block_invoke.198
+ ___53-[TUNeighborhoodActivityConduit _requestInitialState]_block_invoke.201
+ ___53-[TUNeighborhoodActivityConduit _requestInitialState]_block_invoke_2.200
+ ___53-[TUNeighborhoodActivityConduit _requestInitialState]_block_invoke_2.200.cold.1
+ ___55-[TUNeighborhoodActivityConduitXPCClient xpcConnection]_block_invoke.11
+ ___55-[TUNeighborhoodActivityConduitXPCClient xpcConnection]_block_invoke_2.12
+ ___62-[TUMomentsController sendVideoMessageWithRequest:completion:]_block_invoke
+ ___62-[TUMomentsController sendVideoMessageWithRequest:completion:]_block_invoke_2
+ ___68-[TUIDSLookupManager beginQueryWithRefreshForDestination:onService:]_block_invoke
+ ___69-[TUIDSLookupManager filteredDestinationForMultiway:completionBlock:]_block_invoke.94
+ ___69-[TUIDSLookupManager filteredDestinationForMultiway:completionBlock:]_block_invoke_2.96
+ ___69-[TUIDSLookupManager filteredDestinationForMultiway:completionBlock:]_block_invoke_3.97
+ ___71-[TUMomentsControllerXPCClient sendVideoMessageWithRequest:completion:]_block_invoke
+ ___71-[TUMomentsControllerXPCClient sendVideoMessageWithRequest:completion:]_block_invoke_2
+ ___71-[TUMomentsControllerXPCClient sendVideoMessageWithRequest:completion:]_block_invoke_2.cold.1
+ ___74-[TUIDSLookupManager handleIDSQueryResultWithDestinationStatus:onService:]_block_invoke.76
+ ___74-[TUIDSLookupManager handleIDSQueryResultWithDestinationStatus:onService:]_block_invoke.77
+ ___74-[TUIDSLookupManager handleIDSQueryResultWithDestinationStatus:onService:]_block_invoke.78
+ ___75-[TUConversationActivitySession launchApplicationWithForcedURL:completion:]_block_invoke.109
+ ___TUIsStoreDemoModeEnabled_block_invoke
+ ___block_literal_global.105
+ ___block_literal_global.108
+ ___block_literal_global.110
+ ___block_literal_global.130
+ ___block_literal_global.1443
+ ___block_literal_global.189
+ ___block_literal_global.221
+ ___block_literal_global.248
+ ___block_literal_global.253
+ ___block_literal_global.371
+ ___block_literal_global.51
+ __unnamed_array_storage.147
+ _isConduitAvailable.onceToken
+ _isConduitAvailable.sIsConduitAvailable
+ _objc_msgSend$allHandlesFromFetchRequests
+ _objc_msgSend$batchQuerySearchShareNameAndPhotoController
+ _objc_msgSend$clearUplinkMutedCache
+ _objc_msgSend$destinationHandles
+ _objc_msgSend$executeBatchFetchRequests:
+ _objc_msgSend$fetchRequestResults
+ _objc_msgSend$handleToFetchRequest
+ _objc_msgSend$handlesToBatchFetch
+ _objc_msgSend$idsNameAndPhotoStatuses
+ _objc_msgSend$initWithAVLessCapable:lagunaCapable:
+ _objc_msgSend$initWithActivity:state:uuid:endpoint:locallyInitiated:timestamp:isFirstJoin:activeRemoteParticipants:isLocalParticipantActive:applicationState:
+ _objc_msgSend$initWithDevice:activeConversations:recentCalls:recentCallsContacts:
+ _objc_msgSend$initWithHandleToFetchRequest:handlesToBatchFetch:allHandlesFromFetchRequests:fetchRequestResults:
+ _objc_msgSend$initWithSessionUUID:conversationID:senderHandle:destinationHandles:
+ _objc_msgSend$initWithUUID:displayName:
+ _objc_msgSend$isConduitAvailable
+ _objc_msgSend$isLocalParticipantActive
+ _objc_msgSend$needsContactLookupForDisplayName
+ _objc_msgSend$processBatchFetchRequests:
+ _objc_msgSend$requestVideoUpgradeForCall:originatingUIType:
+ _objc_msgSend$resultForSingleHandleFetchRequest:fetchedContacts:
+ _objc_msgSend$sendVideoMessageWithRequest:completion:
+ _objc_msgSend$senderHandle
+ _objc_msgSend$senderIdentityForHandle:
+ _objc_msgSend$shouldIgnoreHandle:withFetchRequest:
+ _sharedInstance.pred
- -[TUAbstractScreenTimeObserver .cxx_destruct]
- -[TUAbstractScreenTimeObserver accessorLock]
- -[TUAbstractScreenTimeObserver addDelegate:queue:]
- -[TUAbstractScreenTimeObserver dealloc]
- -[TUAbstractScreenTimeObserver delegateController]
- -[TUAbstractScreenTimeObserver initWithQueue:dataSource:notificationName:]
- -[TUAbstractScreenTimeObserver isScreenTimeEnabled]
- -[TUAbstractScreenTimeObserver notifyObserver]
- -[TUAbstractScreenTimeObserver removeDelegate:]
- -[TUAbstractScreenTimeObserver screenTimeDataSource]
- -[TUAbstractScreenTimeObserver setScreenTimeEnabled:]
- -[TUAbstractScreenTimeObserver updateScreenTimeEnabled]
- -[TUCall deviceTypeBlock]
- -[TUCall setDeviceTypeBlock:]
- -[TUCallUpdate deviceTypeBlock]
- -[TUCallUpdate setDeviceTypeBlock:]
- -[TUContinuityHandleAnonym localizedDisplayNameAfter112873359]
- -[TUContinuitySessionInfo initWithDevice:recentCalls:recentCallsContacts:]
- -[TUConversation isMirageBehaviorEnabled]
- -[TUConversationActivitySession initWithActivity:state:uuid:endpoint:locallyInitiated:timestamp:isFirstJoin:activeRemoteParticipants:applicationState:]
- -[TUConversationManagerXPCClient dataSourceDelegateQueue]
- -[TUConversationManagerXPCClient setDataSourceDelegateQueue:]
- -[TUConversationParticipant isMirageBehaviorEnabled]
- -[TUConversationParticipantCapabilities isMirageAvailable]
- -[TUMomentsController delegate]
- -[TUMomentsController initWithDelegate:]
- -[TUMomentsController initWithDelegate:dataSource:]
- -[TUMomentsController sendVideoMessageWithUUID:callUUID:toHandles:completion:]
- -[TUMomentsControllerXPCClient sendVideoMessageWithUUID:callUUID:toHandles:completion:]
- -[TUMutableConversationParticipantCapabilities setMirageAvailable:]
- -[TUNearbyDeviceHandleCapabilities .cxx_destruct]
- -[TUNearbyDeviceHandleCapabilities initWithSourceVersion:]
- -[TUNearbyDeviceHandleCapabilities initWithSourceVersion:modelString:]
- -[TUNearbyDeviceHandleCapabilities modelString]
- -[TUNearbyDeviceHandleCapabilities sourceVersion]
- -[TUNeighborhoodActivityConduit nearbyTVDevice:isCapableOfHandoffForConversation:]
- -[TUNeighborhoodActivityConduit nearbyTVDevice:isCapableOfHandoffForConversation:].cold.1
- -[TUScreenTimeDataSource .cxx_destruct]
- -[TUScreenTimeDataSource init]
- -[TUScreenTimeDataSource screenTimeManagementState]
- -[TUScreenTimeDataSource screenTimeStateWithCompletionHandler:]
- -[TUScreenTimeObserver initWithQueue:]
- -[TUScreenTimeObserver initWithQueue:].cold.1
- GCC_except_table153
- GCC_except_table169
- GCC_except_table191
- GCC_except_table212
- GCC_except_table217
- GCC_except_table41
- GCC_except_table46
- GCC_except_table59
- GCC_except_table61
- GCC_except_table64
- GCC_except_table71
- _OBJC_CLASS_$_TUAbstractScreenTimeObserver
- _OBJC_CLASS_$_TUScreenTimeDataSource
- _OBJC_CLASS_$_TUScreenTimeObserver
- _OBJC_IVAR_$_TUAbstractScreenTimeObserver._accessorLock
- _OBJC_IVAR_$_TUAbstractScreenTimeObserver._delegateController
- _OBJC_IVAR_$_TUAbstractScreenTimeObserver._notifyObserver
- _OBJC_IVAR_$_TUAbstractScreenTimeObserver._screenTimeDataSource
- _OBJC_IVAR_$_TUAbstractScreenTimeObserver._screenTimeEnabled
- _OBJC_IVAR_$_TUCall._deviceTypeBlock
- _OBJC_IVAR_$_TUCallUpdate._deviceTypeBlock
- _OBJC_IVAR_$_TUConversationManagerXPCClient._dataSourceDelegateQueue
- _OBJC_IVAR_$_TUMomentsController._delegate
- _OBJC_IVAR_$_TUNearbyDeviceHandleCapabilities._modelString
- _OBJC_IVAR_$_TUNearbyDeviceHandleCapabilities._sourceVersion
- _OBJC_IVAR_$_TUScreenTimeDataSource._screenTimeManagementState
- _OBJC_METACLASS_$_TUAbstractScreenTimeObserver
- _OBJC_METACLASS_$_TUScreenTimeDataSource
- _OBJC_METACLASS_$_TUScreenTimeObserver
- _ScreenTimeCoreLibraryCore.frameworkLibrary
- _TUActionVoicemailLearnMore
- __OBJC_$_CLASS_METHODS_TUConversationMember
- __OBJC_$_INSTANCE_METHODS_TUAbstractScreenTimeObserver
- __OBJC_$_INSTANCE_METHODS_TUConversationMember
- __OBJC_$_INSTANCE_METHODS_TUMutableConversationParticipantCapabilities
- __OBJC_$_INSTANCE_METHODS_TUScreenTimeDataSource
- __OBJC_$_INSTANCE_METHODS_TUScreenTimeObserver
- __OBJC_$_INSTANCE_VARIABLES_TUAbstractScreenTimeObserver
- __OBJC_$_INSTANCE_VARIABLES_TUScreenTimeDataSource
- __OBJC_$_PROP_LIST_TUAbstractScreenTimeObserver
- __OBJC_$_PROP_LIST_TUConversationMember
- __OBJC_$_PROP_LIST_TUFeatureFlags.264
- __OBJC_$_PROP_LIST_TUScreenTimeDataSource
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_TUScreenTimeStateDataSource
- __OBJC_$_PROTOCOL_METHOD_TYPES_TUScreenTimeStateDataSource
- __OBJC_$_PROTOCOL_REFS_TUScreenTimeStateDataSource
- __OBJC_CLASS_PROTOCOLS_$_TUScreenTimeDataSource
- __OBJC_CLASS_RO_$_TUAbstractScreenTimeObserver
- __OBJC_CLASS_RO_$_TUScreenTimeDataSource
- __OBJC_CLASS_RO_$_TUScreenTimeObserver
- __OBJC_LABEL_PROTOCOL_$_TUScreenTimeStateDataSource
- __OBJC_METACLASS_RO_$_TUAbstractScreenTimeObserver
- __OBJC_METACLASS_RO_$_TUScreenTimeDataSource
- __OBJC_METACLASS_RO_$_TUScreenTimeObserver
- __OBJC_PROTOCOL_$_TUScreenTimeStateDataSource
- ___20-[TUCallUpdate init]_block_invoke_3
- ___42-[TUAudioSystemController setUplinkMuted:]_block_invoke.67
- ___42-[TUAudioSystemController setUplinkMuted:]_block_invoke.67.cold.1
- ___44-[TUAudioSystemController setDownlinkMuted:]_block_invoke.72
- ___44-[TUAudioSystemController setDownlinkMuted:]_block_invoke.72.cold.1
- ___51-[TUMomentsController initWithDelegate:dataSource:]_block_invoke
- ___51-[TUMomentsController registerProvider:completion:]_block_invoke.50
- ___53-[TUAbstractScreenTimeObserver setScreenTimeEnabled:]_block_invoke
- ___53-[TUAbstractScreenTimeObserver setScreenTimeEnabled:]_block_invoke_2
- ___53-[TUNeighborhoodActivityConduit _requestInitialState]_block_invoke.187
- ___53-[TUNeighborhoodActivityConduit _requestInitialState]_block_invoke.190
- ___53-[TUNeighborhoodActivityConduit _requestInitialState]_block_invoke.193
- ___53-[TUNeighborhoodActivityConduit _requestInitialState]_block_invoke_2.192
- ___53-[TUNeighborhoodActivityConduit _requestInitialState]_block_invoke_2.192.cold.1
- ___55-[TUAbstractScreenTimeObserver updateScreenTimeEnabled]_block_invoke
- ___55-[TUAbstractScreenTimeObserver updateScreenTimeEnabled]_block_invoke.cold.1
- ___55-[TUNeighborhoodActivityConduitXPCClient xpcConnection]_block_invoke.10
- ___55-[TUNeighborhoodActivityConduitXPCClient xpcConnection]_block_invoke_2.11
- ___63-[TUScreenTimeDataSource screenTimeStateWithCompletionHandler:]_block_invoke
- ___69-[TUIDSLookupManager filteredDestinationForMultiway:completionBlock:]_block_invoke.90
- ___69-[TUIDSLookupManager filteredDestinationForMultiway:completionBlock:]_block_invoke_2.92
- ___69-[TUIDSLookupManager filteredDestinationForMultiway:completionBlock:]_block_invoke_3.93
- ___72-[TUConversationManagerXPCClient mediaPrioritiesChangedForConversation:]_block_invoke_2
- ___74-[TUAbstractScreenTimeObserver initWithQueue:dataSource:notificationName:]_block_invoke
- ___74-[TUIDSLookupManager handleIDSQueryResultWithDestinationStatus:onService:]_block_invoke.73
- ___74-[TUIDSLookupManager handleIDSQueryResultWithDestinationStatus:onService:]_block_invoke.74
- ___75-[TUConversationActivitySession launchApplicationWithForcedURL:completion:]_block_invoke.104
- ___78-[TUMomentsController sendVideoMessageWithUUID:callUUID:toHandles:completion:]_block_invoke
- ___78-[TUMomentsController sendVideoMessageWithUUID:callUUID:toHandles:completion:]_block_invoke_2
- ___83-[TUCall initWithUniqueProxyIdentifier:endpointOnCurrentDevice:notificationCenter:]_block_invoke_4
- ___87-[TUMomentsControllerXPCClient sendVideoMessageWithUUID:callUUID:toHandles:completion:]_block_invoke
- ___87-[TUMomentsControllerXPCClient sendVideoMessageWithUUID:callUUID:toHandles:completion:]_block_invoke_2
- ___87-[TUMomentsControllerXPCClient sendVideoMessageWithUUID:callUUID:toHandles:completion:]_block_invoke_2.cold.1
- ___ScreenTimeCoreLibraryCore_block_invoke
- ___block_descriptor_32_e5_q8?0l
- ___block_descriptor_40_e8_32s_e20_v24?0q8"NSError"16ls32l8
- ___block_descriptor_41_e8_32s_e84_v32?0"<TUAbstractScreenTimeObserverDelegate>"8"NSObject<OS_dispatch_queue>"16^B24ls32l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s64l8s40l8s48l8s56l8
- ___block_literal_global.1455
- ___block_literal_global.181
- ___block_literal_global.220
- ___block_literal_global.247
- ___block_literal_global.368
- ___block_literal_global.59
- ___block_literal_global.70
- ___block_literal_global.72
- ___getSTManagementStateClass_block_invoke
- ___getSTManagementStateClass_block_invoke.cold.1
- ___getSTManagementStateClass_block_invoke.cold.2
- ___getSTSettingsDidChangeNotificationSymbolLoc_block_invoke
- ___getSTSettingsDidChangeNotificationSymbolLoc_block_invoke.cold.1
- __unnamed_array_storage.109
- __unnamed_array_storage.29
- _audit_stringScreenTimeCore
- _getSTManagementStateClass.softClass
- _getSTSettingsDidChangeNotificationSymbolLoc.ptr
- _objc_msgSend$_findConversationForUUID:
- _objc_msgSend$beginObserving
- _objc_msgSend$compare:options:
- _objc_msgSend$dataSourceDelegateQueue
- _objc_msgSend$deviceTypeBlock
- _objc_msgSend$endObserving
- _objc_msgSend$initWithActivity:state:uuid:endpoint:locallyInitiated:timestamp:isFirstJoin:activeRemoteParticipants:applicationState:
- _objc_msgSend$initWithDelegate:dataSource:
- _objc_msgSend$initWithDevice:recentCalls:recentCallsContacts:
- _objc_msgSend$initWithNotificationName:queue:
- _objc_msgSend$initWithSourceVersion:modelString:
- _objc_msgSend$modelString
- _objc_msgSend$screenTimeDataSource
- _objc_msgSend$screenTimeManagementState
- _objc_msgSend$screenTimeObserver:didChangeScreenTimeEnabled:
- _objc_msgSend$screenTimeStateWithCompletionHandler:
- _objc_msgSend$sendVideoMessageWithUUID:callUUID:toHandles:completion:
- _objc_msgSend$setCallback:
- _objc_msgSend$setDataSourceDelegateQueue:
- _objc_msgSend$setScreenTimeEnabled:
- _objc_msgSend$sourceVersion
- _objc_msgSend$updateScreenTimeEnabled
CStrings:
+ "\x0f\x03"
+ "\x12\x16"
+ " activeConversationsCount=%zd"
+ " displayName=%@"
+ " isLocalParticipantActive=%d"
+ " ssA=%@"
+ " uuid=%@"
+ "@24@0:8B16B20"
+ "@84@0:8@16Q24@32@40B48@52B60@64B72Q76"
+ "AudioAccessory"
+ "Clearing uplink mute cache for AVSystemController"
+ "DeviceClass"
+ "DisplayName"
+ "Executed fetchRequest: %@ fetched contacts: %@ result: %@"
+ "Fetch request did not contain any handles or only contained one pseudonym handle: %@ "
+ "Fetch request does not contain exactly one handle %@"
+ "LagunaIncomingCalls"
+ "LiveVoicemailSettings"
+ "Not clearing uplink mute cache for AVSystemController since it does not conform to clearUplinkMutedCache"
+ "Results from batch fetch request: %@"
+ "Sending video message with request: %@"
+ "Stopping preview due to error. shouldRetryPreview=%d because hasRefreshedPreviewAfterError=%d, error.code=%ld wantsPreview=%d"
+ "StoreDemoMode"
+ "T@\"<TUIDSBatchIDQueryController>\",&,N,V_batchQuerySearchShareNameAndPhotoController"
+ "T@\"NSArray\",R,N,V_activeConversations"
+ "T@\"NSDictionary\",R,N,V_handleToFetchRequest"
+ "T@\"NSMutableArray\",R,N,V_allHandlesFromFetchRequests"
+ "T@\"NSMutableArray\",R,N,V_handlesToBatchFetch"
+ "T@\"NSMutableDictionary\",R,N,V_fetchRequestResults"
+ "T@\"NSSet\",R,C,N,V_destinationHandles"
+ "T@\"NSString\",R,N,V_displayName"
+ "T@\"NSUUID\",R,C,N,V_conversationID"
+ "T@\"NSUUID\",R,C,N,V_sessionUUID"
+ "T@\"NSUUID\",R,N,V_uuid"
+ "T@\"TUHandle\",R,C,N,V_senderHandle"
+ "T@\"TULocked\",R,N,V_idsNameAndPhotoStatuses"
+ "TB,D,N,GisLocalParticipantActive"
+ "TB,R,N,GisAVLessCapable,V_avLessCapable"
+ "TB,R,N,GisConduitAvailable"
+ "TB,R,N,GisLagunaCapable,V_lagunaCapable"
+ "TB,R,N,GisLocalParticipantActive,V_localParticipantActive"
+ "TUBatchFetchRequestProcessingResult"
+ "TUContactsDataProvider.m"
+ "TUContinuityConversation"
+ "TUMomentsMessageSendRequest"
+ "TUNeighborhoodActivityConduitXPCClient connection requested while conduit is disabled (runtime)."
+ "Updating destinations for name and photo service: %@"
+ "V"
+ "Vv32@0:8@\"TUMomentsMessageSendRequest\"16@?<v@?@\"NSError\">24"
+ "[WARN] Store demo mode is enabled. There could be some restrictions enabled."
+ "_activeConversations"
+ "_allHandlesFromFetchRequests"
+ "_avLessCapable"
+ "_batchQuerySearchShareNameAndPhotoController"
+ "_destinationHandles"
+ "_displayName"
+ "_fetchRequestResults"
+ "_handleToFetchRequest"
+ "_handlesToBatchFetch"
+ "_idsNameAndPhotoStatuses"
+ "_lagunaCapable"
+ "_localParticipantActive"
+ "_senderHandle"
+ "allHandlesFromFetchRequests"
+ "batchQuerySearchShareNameAndPhotoController"
+ "beginQueryWithRefreshForDestination:onService:"
+ "clearUplinkMutedCache"
+ "com.apple.InCallService.NameAndPhotoUtilities"
+ "com.apple.demo-settings"
+ "com.apple.private.alloy.nameandphoto"
+ "conduitAvailable"
+ "destinationHandles"
+ "dialerCallButtonDoubleTap"
+ "executeBatchFetchRequests:"
+ "faceTimeCallSpamReport"
+ "faceTimeCallSpamReportEnabled"
+ "faceTimeGroupCallSpamReport"
+ "faceTimeGroupCallSpamReportEnabled"
+ "fetchRequestResults"
+ "handleToFetchRequest"
+ "handlesToBatchFetch"
+ "idsNameAndPhotoStatuses"
+ "initWithAVLessCapable:lagunaCapable:"
+ "initWithActivity:state:uuid:endpoint:locallyInitiated:timestamp:isFirstJoin:activeRemoteParticipants:isLocalParticipantActive:applicationState:"
+ "initWithDevice:activeConversations:recentCalls:recentCallsContacts:"
+ "initWithHandleToFetchRequest:handlesToBatchFetch:allHandlesFromFetchRequests:fetchRequestResults:"
+ "initWithSessionUUID:conversationID:senderHandle:destinationHandles:"
+ "initWithUUID:displayName:"
+ "isConduitAvailable"
+ "isContinuitySession"
+ "isLocalParticipantActive"
+ "isNameAndPhotoAvailableForDestination:"
+ "lagunaIncomingCallsEnabled"
+ "localParticipantActive"
+ "needsContactLookupForDisplayName"
+ "processBatchFetchRequests:"
+ "requestVideoUpgradeForCall:originatingUIType:"
+ "resultForSingleHandleFetchRequest:fetchedContacts:"
+ "sendVideoMessageWithRequest:completion:"
+ "senderHandle"
+ "setBatchQuerySearchShareNameAndPhotoController:"
+ "shouldIgnoreHandle:withFetchRequest:"
+ "v32@0:8@\"TUMomentsMessageSendRequest\"16@?<v@?@\"NSError\">24"
+ "videoMessagingSpamReport"
+ "videoMessagingSpamReportEnabled"
+ "\x8e\x12%AB1"
- "\x02\x13"
- "\x0f\x01"
- "\x12\x17"
- " modelString=%@"
- " sourceVersion=%@"
- "-[TUMomentsController init]"
- "400"
- "500"
- "@\"<TUMomentsControllerDelegate>\""
- "@\"<TUNotifyObserver>\""
- "@\"<TUScreenTimeStateDataSource>\""
- "@\"NSObject<OS_dispatch_queue>\"16@0:8"
- "@\"STManagementState\""
- "@\"TUDelegateController<TUAbstractScreenTimeObserverDelegate>\""
- "@80@0:8@16Q24@32@40B48@52B60@64Q72"
- "AppleTV5,3"
- "AppleTV6,2"
- "Class getSTManagementStateClass(void)_block_invoke"
- "Conversation is AVLess. NearbyTVDevice: %@ capable of handoff: %d"
- "Conversation not AVLess. TV is capable of handoff."
- "Conversation not found for %@. TV incapable of handoff"
- "Fetching ScreenTime state failed with error: %@"
- "STManagementState"
- "STSettingsDidChangeNotification"
- "Sending video message with UUID: %@"
- "T@\"<TUMomentsControllerDelegate>\",R,W,N,V_delegate"
- "T@\"<TUNotifyObserver>\",R,N,V_notifyObserver"
- "T@\"<TUScreenTimeStateDataSource>\",R,N,V_screenTimeDataSource"
- "T@\"NSObject<OS_dispatch_queue>\",&,N"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_dataSourceDelegateQueue"
- "T@\"NSString\",R,C,N,V_modelString"
- "T@\"NSString\",R,C,N,V_sourceVersion"
- "T@\"NSString\",R,N,V_localizedDisplayName"
- "T@\"STManagementState\",R,N,V_screenTimeManagementState"
- "T@\"TUDelegateController<TUAbstractScreenTimeObserverDelegate>\",R,N,V_delegateController"
- "T@?,C,N,V_deviceTypeBlock"
- "TB,N,GisMirageAvailable"
- "TB,N,GisScreenTimeEnabled,V_screenTimeEnabled"
- "TB,R,N,GisAVLessCapable"
- "TB,R,N,GisLagunaCapable"
- "TB,R,N,GisMirageAvailable"
- "TB,R,N,GisMirageBehaviorEnabled"
- "TUAbstractScreenTimeObserver"
- "TUScreenTimeDataSource"
- "TUScreenTimeDataSource.m"
- "TUScreenTimeObserver"
- "TUScreenTimeObserver.m"
- "TUScreenTimeStateDataSource"
- "Vv48@0:8@\"NSUUID\"16@\"NSUUID\"24@\"NSSet\"32@?<v@?@\"NSError\">40"
- "W"
- "_dataSourceDelegateQueue"
- "_deviceTypeBlock"
- "_modelString"
- "_notifyObserver"
- "_screenTimeDataSource"
- "_screenTimeEnabled"
- "_screenTimeManagementState"
- "_sourceVersion"
- "compare:options:"
- "const char *const getSTSettingsDidChangeNotification(void)"
- "dataSourceDelegateQueue"
- "deviceTypeBlock"
- "initWithActivity:state:uuid:endpoint:locallyInitiated:timestamp:isFirstJoin:activeRemoteParticipants:applicationState:"
- "initWithDelegate:dataSource:"
- "initWithDevice:recentCalls:recentCallsContacts:"
- "initWithQueue:dataSource:notificationName:"
- "initWithSourceVersion:"
- "initWithSourceVersion:modelString:"
- "isEligbibleForScreening: NO because the device is not an iphone"
- "isMirageAvailable"
- "isMirageBehaviorEnabled"
- "isScreenTimeEnabled"
- "localizedDisplayNameAfter112873359"
- "mediaPrioritiesChangedForConversation: %@"
- "mirageAvailable"
- "mirageBehaviorEnabled"
- "modelString"
- "nearbyTVDevice:isCapableOfHandoffForConversation:"
- "notifyObserver"
- "q8@?0"
- "screenTimeDataSource"
- "screenTimeEnabled"
- "screenTimeManagementState"
- "screenTimeObserver:didChangeScreenTimeEnabled:"
- "screenTimeStateWithCompletionHandler:"
- "sendVideoMessageWithUUID:callUUID:toHandles:completion:"
- "setDataSourceDelegateQueue:"
- "setDeviceTypeBlock:"
- "setMirageAvailable:"
- "setScreenTimeEnabled:"
- "softlink:r:path:/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore"
- "sourceVersion"
- "updateScreenTimeEnabled"
- "v24@0:8@\"NSObject<OS_dispatch_queue>\"16"
- "v24@0:8@?<v@?q@\"NSError\">16"
- "v32@?0@\"<TUAbstractScreenTimeObserverDelegate>\"8@\"NSObject<OS_dispatch_queue>\"16^B24"
- "v48@0:8@\"NSUUID\"16@\"NSUUID\"24@\"NSSet\"32@?<v@?@\"NSError\">40"
- "voicemailLearnMore"
- "void *ScreenTimeCoreLibrary(void)"
- "\x8e\x12&AB1"

```
