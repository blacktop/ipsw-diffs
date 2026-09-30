## ActivitySharing

> `/System/Library/PrivateFrameworks/ActivitySharing.framework/ActivitySharing`

```diff

-2026.3.2.0.0
-  __TEXT.__text: 0x44824
-  __TEXT.__auth_stubs: 0x910
-  __TEXT.__objc_methlist: 0x4dbc
-  __TEXT.__const: 0x2b8
-  __TEXT.__cstring: 0x3074
-  __TEXT.__oslogstring: 0x1e13
+2026.4.6.0.0
+  __TEXT.__text: 0x45f0c
+  __TEXT.__auth_stubs: 0x890
+  __TEXT.__objc_methlist: 0x4adc
+  __TEXT.__const: 0x2c8
+  __TEXT.__cstring: 0x2f5b
+  __TEXT.__oslogstring: 0x1df4
   __TEXT.__gcc_except_tab: 0x94
-  __TEXT.__unwind_info: 0xee0
-  __TEXT.__objc_classname: 0x6c0
-  __TEXT.__objc_methname: 0xb065
-  __TEXT.__objc_methtype: 0xea4
-  __TEXT.__objc_stubs: 0x6640
-  __DATA_CONST.__got: 0x368
-  __DATA_CONST.__const: 0xeb8
-  __DATA_CONST.__objc_classlist: 0x1a8
+  __TEXT.__unwind_info: 0x1210
+  __TEXT.__objc_classname: 0x694
+  __TEXT.__objc_methname: 0xa704
+  __TEXT.__objc_methtype: 0xc2f
+  __TEXT.__objc_stubs: 0x63c0
+  __DATA_CONST.__got: 0x350
+  __DATA_CONST.__const: 0xbe8
+  __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x50
+  __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2780
-  __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x170
+  __DATA_CONST.__objc_selrefs: 0x25f8
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_superrefs: 0x168
   __DATA_CONST.__objc_arraydata: 0x100
-  __AUTH_CONST.__auth_got: 0x498
+  __AUTH_CONST.__auth_got: 0x458
   __AUTH_CONST.__const: 0x660
-  __AUTH_CONST.__cfstring: 0x3b00
-  __AUTH_CONST.__objc_const: 0x8a28
+  __AUTH_CONST.__cfstring: 0x3aa0
+  __AUTH_CONST.__objc_const: 0x81f0
   __AUTH_CONST.__objc_intobj: 0x2d0
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0xb90
-  __DATA.__objc_ivar: 0x548
-  __DATA.__data: 0x410
+  __DATA.__objc_ivar: 0x538
+  __DATA.__data: 0x350
   __DATA.__bss: 0x20
-  __DATA_DIRTY.__objc_data: 0x500
+  __DATA_DIRTY.__objc_data: 0x4b0
   __DATA_DIRTY.__bss: 0x58
   __DATA_DIRTY.__common: 0x50
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F31F5ED3-1B0A-301F-AE41-811259499E07
-  Functions: 1971
-  Symbols:   6059
-  CStrings:  3178
+  UUID: 82552CE1-2E35-3E3A-8983-38CABA651502
+  Functions: 1884
+  Symbols:   5817
+  CStrings:  3088
 
Symbols:
+ -[ASActivityDataNotification setSharingFriend:]
+ -[ASActivityDataNotification sharingFriend]
+ _ASAllGoalsMetForSummary
+ _OBJC_IVAR_$_ASActivityDataNotification._sharingFriend
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _objc_msgSend$activeEnergyBurned
+ _objc_msgSend$activeEnergyBurnedGoal
+ _objc_msgSend$appleExerciseTime
+ _objc_msgSend$appleExerciseTimeGoal
+ _objc_msgSend$appleMoveTime
+ _objc_msgSend$appleMoveTimeGoal
+ _objc_msgSend$appleStandHours
+ _objc_msgSend$appleStandHoursGoal
+ _objc_msgSend$sharingFriend
- -[ASActivityDataNotification friend]
- -[ASActivityDataNotification setFriend:]
- -[ASClient .cxx_destruct]
- -[ASClient _clientQueueSuccessCompletion:]
- -[ASClient _remoteProxy:errorHandler:]
- -[ASClient acceptCompetitionRequestFromFriendWithUUID:completion:]
- -[ASClient acceptInviteRequestFromFriendWithUUID:completion:]
- -[ASClient allFriendsWithCompletion:]
- -[ASClient clearFriendListWithCompletion:]
- -[ASClient cloudKitAccountStatusWithCompletion:]
- -[ASClient completeCompetitionWithFriendWithUUID:completion:]
- -[ASClient connectionInvalidated]
- -[ASClient expireChangeTokenWithCompletion:]
- -[ASClient exportedInterface]
- -[ASClient fetchAllDataIfTimeSinceLastFetchIsGreaterThan:completion:]
- -[ASClient fetchAllDataWithCompletion:]
- -[ASClient fetchAreMultipleDevicesSharingDataForSnapshotIndex:withCompletion:]
- -[ASClient friendWithRemoteUUID:completion:]
- -[ASClient handleNotificationResponse:completion:]
- -[ASClient ignoreCompetitionRequestFromFriendWithUUID:completion:]
- -[ASClient ignoreInviteRequestFromFriendWithUUID:completion:]
- -[ASClient initWithHealthStore:]
- -[ASClient pushActivityDataToAllFriendsWithCompletion:]
- -[ASClient pushFakeActivityDataToAllFriendsWithCompletion:]
- -[ASClient queryAppBadgeCountWithCompletion:]
- -[ASClient remoteInterface]
- -[ASClient removeFriendWithUUID:completion:]
- -[ASClient sendCompetitionRequestToFriendWithUUID:completion:]
- -[ASClient sendInviteRequestToDestination:callerID:serviceIdentifier:completion:]
- -[ASClient sendWithdrawInviteRequestToFriendWithUUID:completion:]
- -[ASClient setActivityDataVisible:toFriendWithUUID:completion:]
- -[ASClient setMuteEnabled:forFriendWithUUID:completion:]
- _ASActivitySharingDaemonEnabled
- _ASClientTaskIdentifier
- _ASServerInterface
- _OBJC_CLASS_$_ASClient
- _OBJC_CLASS_$_HKTaskServerProxyProvider
- _OBJC_CLASS_$_NSXPCInterface
- _OBJC_IVAR_$_ASActivityDataNotification._friend
- _OBJC_IVAR_$_ASClient._clientQueue
- _OBJC_IVAR_$_ASClient._proxyProvider
- _OBJC_IVAR_$_ASClient._serverProxy
- _OBJC_IVAR_$_ASClient._serverQueue
- _OBJC_METACLASS_$_ASClient
- __OBJC_$_INSTANCE_METHODS_ASClient
- __OBJC_$_INSTANCE_VARIABLES_ASClient
- __OBJC_$_PROP_LIST_ASClient
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_ASServerInterface
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT__HKXPCExportable
- __OBJC_$_PROTOCOL_INSTANCE_METHODS__HKXPCExportable
- __OBJC_$_PROTOCOL_METHOD_TYPES_ASServerInterface
- __OBJC_$_PROTOCOL_METHOD_TYPES__HKXPCExportable
- __OBJC_$_PROTOCOL_REFS_ASServerInterface
- __OBJC_$_PROTOCOL_REFS__HKXPCExportable
- __OBJC_CLASS_PROTOCOLS_$_ASClient
- __OBJC_CLASS_RO_$_ASClient
- __OBJC_LABEL_PROTOCOL_$_ASServerInterface
- __OBJC_LABEL_PROTOCOL_$__HKXPCExportable
- __OBJC_METACLASS_RO_$_ASClient
- __OBJC_PROTOCOL_$_ASServerInterface
- __OBJC_PROTOCOL_$__HKXPCExportable
- __OBJC_PROTOCOL_REFERENCE_$_ASServerInterface
- ___37-[ASClient allFriendsWithCompletion:]_block_invoke
- ___37-[ASClient allFriendsWithCompletion:]_block_invoke_2
- ___37-[ASClient allFriendsWithCompletion:]_block_invoke_3
- ___38-[ASClient _remoteProxy:errorHandler:]_block_invoke
- ___38-[ASClient _remoteProxy:errorHandler:]_block_invoke_2
- ___38-[ASClient _remoteProxy:errorHandler:]_block_invoke_2.cold.1
- ___39-[ASClient fetchAllDataWithCompletion:]_block_invoke
- ___39-[ASClient fetchAllDataWithCompletion:]_block_invoke_2
- ___42-[ASClient _clientQueueSuccessCompletion:]_block_invoke
- ___42-[ASClient _clientQueueSuccessCompletion:]_block_invoke_2
- ___42-[ASClient clearFriendListWithCompletion:]_block_invoke
- ___42-[ASClient clearFriendListWithCompletion:]_block_invoke_2
- ___42-[ASClient clearFriendListWithCompletion:]_block_invoke_3
- ___42-[ASClient clearFriendListWithCompletion:]_block_invoke_4
- ___44-[ASClient expireChangeTokenWithCompletion:]_block_invoke
- ___44-[ASClient expireChangeTokenWithCompletion:]_block_invoke_2
- ___44-[ASClient friendWithRemoteUUID:completion:]_block_invoke
- ___44-[ASClient friendWithRemoteUUID:completion:]_block_invoke_2
- ___44-[ASClient friendWithRemoteUUID:completion:]_block_invoke_3
- ___44-[ASClient friendWithRemoteUUID:completion:]_block_invoke_4
- ___44-[ASClient friendWithRemoteUUID:completion:]_block_invoke_5
- ___44-[ASClient removeFriendWithUUID:completion:]_block_invoke
- ___44-[ASClient removeFriendWithUUID:completion:]_block_invoke_2
- ___45-[ASClient queryAppBadgeCountWithCompletion:]_block_invoke
- ___45-[ASClient queryAppBadgeCountWithCompletion:]_block_invoke_2
- ___45-[ASClient queryAppBadgeCountWithCompletion:]_block_invoke_3
- ___48-[ASClient cloudKitAccountStatusWithCompletion:]_block_invoke
- ___48-[ASClient cloudKitAccountStatusWithCompletion:]_block_invoke_2
- ___48-[ASClient cloudKitAccountStatusWithCompletion:]_block_invoke_3
- ___48-[ASClient cloudKitAccountStatusWithCompletion:]_block_invoke_4
- ___50-[ASClient handleNotificationResponse:completion:]_block_invoke
- ___50-[ASClient handleNotificationResponse:completion:]_block_invoke_2
- ___55-[ASClient pushActivityDataToAllFriendsWithCompletion:]_block_invoke
- ___55-[ASClient pushActivityDataToAllFriendsWithCompletion:]_block_invoke_2
- ___56-[ASClient setMuteEnabled:forFriendWithUUID:completion:]_block_invoke
- ___56-[ASClient setMuteEnabled:forFriendWithUUID:completion:]_block_invoke_2
- ___59-[ASClient pushFakeActivityDataToAllFriendsWithCompletion:]_block_invoke
- ___59-[ASClient pushFakeActivityDataToAllFriendsWithCompletion:]_block_invoke_2
- ___61-[ASClient acceptInviteRequestFromFriendWithUUID:completion:]_block_invoke
- ___61-[ASClient acceptInviteRequestFromFriendWithUUID:completion:]_block_invoke_2
- ___61-[ASClient completeCompetitionWithFriendWithUUID:completion:]_block_invoke
- ___61-[ASClient completeCompetitionWithFriendWithUUID:completion:]_block_invoke_2
- ___61-[ASClient ignoreInviteRequestFromFriendWithUUID:completion:]_block_invoke
- ___61-[ASClient ignoreInviteRequestFromFriendWithUUID:completion:]_block_invoke_2
- ___62-[ASClient sendCompetitionRequestToFriendWithUUID:completion:]_block_invoke
- ___62-[ASClient sendCompetitionRequestToFriendWithUUID:completion:]_block_invoke_2
- ___63-[ASClient setActivityDataVisible:toFriendWithUUID:completion:]_block_invoke
- ___63-[ASClient setActivityDataVisible:toFriendWithUUID:completion:]_block_invoke_2
- ___65-[ASClient sendWithdrawInviteRequestToFriendWithUUID:completion:]_block_invoke
- ___65-[ASClient sendWithdrawInviteRequestToFriendWithUUID:completion:]_block_invoke_2
- ___66-[ASClient acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke
- ___66-[ASClient acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke_2
- ___66-[ASClient ignoreCompetitionRequestFromFriendWithUUID:completion:]_block_invoke
- ___66-[ASClient ignoreCompetitionRequestFromFriendWithUUID:completion:]_block_invoke_2
- ___69-[ASClient fetchAllDataIfTimeSinceLastFetchIsGreaterThan:completion:]_block_invoke
- ___69-[ASClient fetchAllDataIfTimeSinceLastFetchIsGreaterThan:completion:]_block_invoke_2
- ___78-[ASClient fetchAreMultipleDevicesSharingDataForSnapshotIndex:withCompletion:]_block_invoke
- ___78-[ASClient fetchAreMultipleDevicesSharingDataForSnapshotIndex:withCompletion:]_block_invoke_2
- ___78-[ASClient fetchAreMultipleDevicesSharingDataForSnapshotIndex:withCompletion:]_block_invoke_3
- ___81-[ASClient sendInviteRequestToDestination:callerID:serviceIdentifier:completion:]_block_invoke
- ___81-[ASClient sendInviteRequestToDestination:callerID:serviceIdentifier:completion:]_block_invoke_2
- ___block_descriptor_40_e8_32bs_e17_v16?0"NSError"8ls32l8
- ___block_descriptor_40_e8_32bs_e23_v24?0B8B12"NSError"16ls32l8
- ___block_descriptor_40_e8_32bs_e29_v16?0"<ASServerInterface>"8ls32l8
- ___block_descriptor_40_e8_32bs_e31_v28?0"NSData"8B16"NSError"20ls32l8
- ___block_descriptor_40_e8_32bs_e33_v28?0"NSNumber"8B16"NSError"20ls32l8
- ___block_descriptor_40_e8_32bs_e44_v28?0"ASCodableFriendList"8B16"NSError"20ls32l8
- ___block_descriptor_48_e8_32bs_e29_v16?0"<ASServerInterface>"8ls32l8
- ___block_descriptor_48_e8_32s40bs_e20_v20?0B8"NSError"12ls40l8s32l8
- ___block_descriptor_48_e8_32s40bs_e23_v24?0B8B12"NSError"16ls40l8s32l8
- ___block_descriptor_48_e8_32s40bs_e29_v16?0"<ASServerInterface>"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40bs_e29_v16?0"<ASServerInterface>"8ls40l8s32l8
- ___block_descriptor_48_e8_32s40bs_e33_v28?0"ASFriend"8B16"NSError"20ls32l8s40l8
- ___block_descriptor_49_e8_32s40bs_e29_v16?0"<ASServerInterface>"8ls32l8s40l8
- ___block_descriptor_49_e8_32s40bs_e5_v8?0ls40l8s32l8
- ___block_descriptor_50_e8_32s40bs_e5_v8?0ls40l8s32l8
- ___block_descriptor_56_e8_32s40bs48bs_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_57_e8_32s40s48bs_e5_v8?0ls48l8s32l8s40l8
- ___block_descriptor_64_e8_32s40s48s56bs_e29_v16?0"<ASServerInterface>"8ls32l8s40l8s48l8s56l8
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_clientQueueSuccessCompletion:
- _objc_msgSend$_remoteProxy:errorHandler:
- _objc_msgSend$fetchProxyWithHandler:errorHandler:
- _objc_msgSend$friend
- _objc_msgSend$initWithHealthStore:taskIdentifier:exportedObject:taskUUID:
- _objc_msgSend$interfaceWithProtocol:
- _objc_msgSend$remote_acceptCompetitionRequestFromFriendWithUUID:completion:
- _objc_msgSend$remote_acceptInviteRequestFromFriendWithUUID:completion:
- _objc_msgSend$remote_clearFriendListWithCompletion:
- _objc_msgSend$remote_cloudKitAccountStatusWithCompletion:
- _objc_msgSend$remote_completeCompetitionWithFriendWithUUID:completion:
- _objc_msgSend$remote_expireChangeTokenWithCompletion:
- _objc_msgSend$remote_fetchAllDataIfTimeSinceLastFetchIsGreaterThan:completion:
- _objc_msgSend$remote_fetchAllDataWithCompletion:
- _objc_msgSend$remote_fetchAllFriendsWithCompletion:
- _objc_msgSend$remote_fetchAreMultipleDevicesSharingDataForSnapshotIndex:withCompletion:
- _objc_msgSend$remote_friendWithRemoteUUID:completion:
- _objc_msgSend$remote_handleNotificationResponse:completion:
- _objc_msgSend$remote_ignoreCompetitionRequestFromFriendWithUUID:completion:
- _objc_msgSend$remote_ignoreInviteRequestFromFriendWithUUID:completion:
- _objc_msgSend$remote_pushActivityDataWithCompletion:
- _objc_msgSend$remote_pushFakeActivityDataWithCompletion:
- _objc_msgSend$remote_queryAppBadgeCountWithCompletion:
- _objc_msgSend$remote_removeFriendWithUUID:completion:
- _objc_msgSend$remote_sendCompetitionRequestToFriendWithUUID:completion:
- _objc_msgSend$remote_sendInviteRequestToDestination:callerID:serviceIdentifier:completion:
- _objc_msgSend$remote_sendWithdrawInviteRequestToFriendWithUUID:completion:
- _objc_msgSend$remote_setActivityDataVisible:toFriendWithUUID:completion:
- _objc_msgSend$remote_setMuteEnabled:forFriendWithUUID:completion:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x10
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x8
CStrings:
+ "T@\"ASFriend\",&,N,V_sharingFriend"
+ "_sharingFriend"
+ "activeEnergyBurned"
+ "activeEnergyBurnedGoal"
+ "appleExerciseTime"
+ "appleExerciseTimeGoal"
+ "appleMoveTime"
+ "appleMoveTimeGoal"
+ "appleStandHours"
+ "appleStandHoursGoal"
+ "setSharingFriend:"
+ "sharingFriend"
- "@\"<ASServerInterface>\""
- "@\"HKProxyProvider\""
- "@\"NSXPCInterface\"16@0:8"
- "@?24@0:8@?16"
- "ASClient"
- "ASServerInterface"
- "ActivitySharingDaemonEnabled"
- "T@\"ASFriend\",&,N,V_friend"
- "Unable to get plugin proxy: %@"
- "_HKXPCExportable"
- "_clientQueue"
- "_clientQueueSuccessCompletion:"
- "_friend"
- "_proxyProvider"
- "_remoteProxy:errorHandler:"
- "_serverProxy"
- "_serverQueue"
- "acceptCompetitionRequestFromFriendWithUUID:completion:"
- "acceptInviteRequestFromFriendWithUUID:completion:"
- "allFriendsWithCompletion:"
- "clearFriendListWithCompletion:"
- "client"
- "cloudKitAccountStatusWithCompletion:"
- "completeCompetitionWithFriendWithUUID:completion:"
- "connectionConfigured"
- "connectionInterrupted"
- "connectionInvalidated"
- "expireChangeTokenWithCompletion:"
- "exportedInterface"
- "fetchAllDataIfTimeSinceLastFetchIsGreaterThan:completion:"
- "fetchAllDataWithCompletion:"
- "fetchAreMultipleDevicesSharingDataForSnapshotIndex:withCompletion:"
- "fetchProxyWithHandler:errorHandler:"
- "friendWithRemoteUUID:completion:"
- "handleNotificationResponse:completion:"
- "ignoreCompetitionRequestFromFriendWithUUID:completion:"
- "ignoreInviteRequestFromFriendWithUUID:completion:"
- "initWithHealthStore:"
- "initWithHealthStore:taskIdentifier:exportedObject:taskUUID:"
- "interfaceWithProtocol:"
- "pushActivityDataToAllFriendsWithCompletion:"
- "pushFakeActivityDataToAllFriendsWithCompletion:"
- "queryAppBadgeCountWithCompletion:"
- "remoteInterface"
- "remote_acceptCompetitionRequestFromFriendWithUUID:completion:"
- "remote_acceptInviteRequestFromFriendWithUUID:completion:"
- "remote_clearFriendListWithCompletion:"
- "remote_cloudKitAccountStatusWithCompletion:"
- "remote_completeCompetitionWithFriendWithUUID:completion:"
- "remote_expireChangeTokenWithCompletion:"
- "remote_fetchAllDataIfTimeSinceLastFetchIsGreaterThan:completion:"
- "remote_fetchAllDataWithCompletion:"
- "remote_fetchAllFriendsWithCompletion:"
- "remote_fetchAreMultipleDevicesSharingDataForSnapshotIndex:withCompletion:"
- "remote_friendWithRemoteUUID:completion:"
- "remote_handleNotificationResponse:completion:"
- "remote_ignoreCompetitionRequestFromFriendWithUUID:completion:"
- "remote_ignoreInviteRequestFromFriendWithUUID:completion:"
- "remote_pushActivityDataWithCompletion:"
- "remote_pushFakeActivityDataWithCompletion:"
- "remote_queryAppBadgeCountWithCompletion:"
- "remote_removeFriendWithUUID:completion:"
- "remote_sendCompetitionRequestToFriendWithUUID:completion:"
- "remote_sendInviteRequestToDestination:callerID:serviceIdentifier:completion:"
- "remote_sendWithdrawInviteRequestToFriendWithUUID:completion:"
- "remote_setActivityDataVisible:toFriendWithUUID:completion:"
- "remote_setMuteEnabled:forFriendWithUUID:completion:"
- "removeFriendWithUUID:completion:"
- "sendCompetitionRequestToFriendWithUUID:completion:"
- "sendInviteRequestToDestination:callerID:serviceIdentifier:completion:"
- "sendWithdrawInviteRequestToFriendWithUUID:completion:"
- "server"
- "setActivityDataVisible:toFriendWithUUID:completion:"
- "setFriend:"
- "setMuteEnabled:forFriendWithUUID:completion:"
- "v16@?0@\"<ASServerInterface>\"8"
- "v16@?0@\"NSError\"8"
- "v20@?0B8@\"NSError\"12"
- "v24@0:8@?<v@?@\"ASCodableFriendList\"B@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSNumber\"B@\"NSError\">16"
- "v24@0:8@?<v@?B@\"NSError\">16"
- "v24@0:8@?<v@?BB@\"NSError\">16"
- "v24@?0B8B12@\"NSError\"16"
- "v28@?0@\"ASCodableFriendList\"8B16@\"NSError\"20"
- "v28@?0@\"ASFriend\"8B16@\"NSError\"20"
- "v28@?0@\"NSData\"8B16@\"NSError\"20"
- "v28@?0@\"NSNumber\"8B16@\"NSError\"20"
- "v32@0:8@\"ASUserNotificationResponse\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"NSNumber\"16@?<v@?BB@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSData\"B@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@16@?24"
- "v32@0:8@?16@?24"
- "v32@0:8Q16@?<v@?B@\"NSError\">24"
- "v36@0:8B16@\"NSString\"20@?<v@?B@\"NSError\">28"
- "v36@0:8B16@20@?28"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@?<v@?B@\"NSError\">40"
- "v48@0:8@16@24@32@?40"

```
