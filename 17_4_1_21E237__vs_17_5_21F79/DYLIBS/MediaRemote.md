## MediaRemote

> `/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote`

```diff

-4023.510.2.0.0
-  __TEXT.__text: 0x2a60d0
+4023.610.3.0.0
+  __TEXT.__text: 0x2a6710
   __TEXT.__auth_stubs: 0x1620
-  __TEXT.__objc_methlist: 0x253e8
+  __TEXT.__objc_methlist: 0x25430
   __TEXT.__const: 0x380
-  __TEXT.__cstring: 0x28e1a
-  __TEXT.__oslogstring: 0xcc54
-  __TEXT.__gcc_except_tab: 0x4e74
+  __TEXT.__cstring: 0x29274
+  __TEXT.__oslogstring: 0xccb0
+  __TEXT.__gcc_except_tab: 0x4e4c
   __TEXT.__ustring: 0x12
-  __TEXT.__unwind_info: 0xa244
+  __TEXT.__unwind_info: 0xa140
   __TEXT.__objc_classname: 0x4567
-  __TEXT.__objc_methname: 0x43c7e
-  __TEXT.__objc_methtype: 0x848f
-  __TEXT.__objc_stubs: 0x238e0
+  __TEXT.__objc_methname: 0x43dc2
+  __TEXT.__objc_methtype: 0x84cb
+  __TEXT.__objc_stubs: 0x23940
   __DATA_CONST.__got: 0x1c0
-  __DATA_CONST.__const: 0xa2d0
+  __DATA_CONST.__const: 0xa418
   __DATA_CONST.__objc_classlist: 0xff0
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x228
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x34f88
-  __DATA_CONST.__objc_selrefs: 0xd0d0
+  __DATA_CONST.__objc_const: 0x35048
+  __DATA_CONST.__objc_selrefs: 0xd108
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_classrefs: 0x10e8
   __DATA_CONST.__objc_superrefs: 0xe28
   __DATA_CONST.__objc_arraydata: 0x1f0
-  __AUTH_CONST.__cfstring: 0x1e0a0
+  __AUTH_CONST.__cfstring: 0x1e4e0
   __AUTH_CONST.__objc_const: 0xb988
   __AUTH_CONST.__const: 0x3000
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__objc_intobj: 0x3c0
+  __AUTH_CONST.__objc_intobj: 0x438
   __AUTH_CONST.__objc_arrayobj: 0x138
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0xb20
-  __AUTH.__objc_data: 0x7670
+  __AUTH.__objc_data: 0x73f0
   __AUTH.__data: 0x1e0
-  __DATA.__objc_ivar: 0x2d10
-  __DATA.__data: 0x1ce8
-  __DATA.__bss: 0x4c8
+  __DATA.__objc_ivar: 0x2d18
+  __DATA.__data: 0x1d78
+  __DATA.__bss: 0x420
   __DATA.__common: 0x0
-  __DATA_DIRTY.__objc_data: 0x28f0
+  __DATA_DIRTY.__objc_data: 0x2b70
   __DATA_DIRTY.__data: 0x1e8
-  __DATA_DIRTY.__bss: 0x6a8
+  __DATA_DIRTY.__bss: 0x6d0
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 18079
-  Symbols:   49158
-  CStrings:  17882
+  Functions: 18090
+  Symbols:   49228
+  CStrings:  17929
 
Symbols:
+ -[MRAVDistantRoutingDiscoverySession configurationWithCompletion:]
+ -[MRAVRoutingDiscoverySession configuration]
+ -[MRAVRoutingDiscoverySession setConfiguration:]
+ -[MRNowPlayingOriginClient initWithOrigin:routingContextID:]
+ -[MRNowPlayingOriginClientManager _createOriginClientForPlayerPath:routingContextID:]
+ -[MRNowPlayingOriginClientManager createCustomOriginClientForOrigin:routingContextID:]
+ -[MRSharedSettings verboseImageLoadingLogging]
+ -[MRUserSettings groupSessionNearbyGroupCreateTimeout]
+ -[MRUserSettings groupSessionNearbyGroupJoinTimeout]
+ -[MRUserSettings groupSessionNearbyInvitationCreateTimeout]
+ -[MRUserSettings verboseImageLoadingLogging]
+ -[_MRGroupSessionJoinResponseProtobuf hasJoinURL]
+ -[_MRGroupSessionJoinResponseProtobuf joinURL]
+ -[_MRGroupSessionJoinResponseProtobuf setJoinURL:]
+ GCC_except_table121
+ GCC_except_table122
+ GCC_except_table126
+ GCC_except_table131
+ GCC_except_table137
+ GCC_except_table138
+ GCC_except_table145
+ GCC_except_table153
+ GCC_except_table154
+ OBJC_IVAR_$__MRGroupSessionJoinResponseProtobuf._joinURL
+ _OBJC_IVAR_$_MRAVRoutingDiscoverySession._configuration
+ ___44-[MRUserSettings verboseImageLoadingLogging]_block_invoke
+ ___55-[MRAVDistantRoutingDiscoverySession setDiscoveryMode:]_block_invoke.80
+ ___60-[MRAVDistantRoutingDiscoverySession devicePresenceDetected]_block_invoke.82
+ ___60-[MRAVDistantRoutingDiscoverySession devicePresenceDetected]_block_invoke.82.cold.1
+ ___71-[MRNowPlayingOriginClient _prepareToRestoreClientStateWithCompletion:]_block_invoke.88
+ ___72-[MRAVDistantRoutingDiscoverySession setHostedRoutingSessionConnection:]_block_invoke.84
+ ___72-[MRAVDistantRoutingDiscoverySession setHostedRoutingSessionConnection:]_block_invoke.85
+ ___72-[MRAVDistantRoutingDiscoverySession setHostedRoutingSessionConnection:]_block_invoke_2.86
+ ___87-[MRAVDistantRoutingDiscoverySession _initializeHostedRoutingConnectionWithCompletion:]_block_invoke.cold.3
+ ___Block_byref_object_copy_.62
+ ___Block_byref_object_dispose_.63
+ ___MRAnalyticsSendEvent_block_invoke.321
+ ____MRMediaRemoteGetDeviceUIDWithRetryIntervals_block_invoke.360
+ ____MRMediaRemoteGetDeviceUIDWithRetryIntervals_block_invoke.361
+ ___block_literal_global.111
+ ___block_literal_global.223
+ ___block_literal_global.252
+ ___block_literal_global.317
+ ___block_literal_global.358
+ ___block_literal_global.477
+ ___block_literal_global.522
+ ___block_literal_global.94
+ __unnamed_array_storage.502
+ _kMREventErrorDomainKey
+ _kMREventGroupSessionAutoApproveReasonBiome
+ _kMREventGroupSessionAutoApproveReasonDisabled
+ _kMREventGroupSessionAutoApproveReasonHomeUser
+ _kMREventGroupSessionAutoApproveReasonNone
+ _kMREventGroupSessionAutoApproveReasonSharedSecret
+ _kMREventGroupSessionCreate
+ _kMREventGroupSessionEnd
+ _kMREventGroupSessionIsHostKey
+ _kMREventGroupSessionJoin
+ _kMREventGroupSessionJoinAttempt
+ _kMREventGroupSessionJoinAttemptWHAConnectionDurationKey
+ _kMREventGroupSessionJoinAttemptWHAReconDurationKey
+ _kMREventGroupSessionJoinPresenceAssertionDurationKey
+ _kMREventGroupSessionJoinProviderJoinDurationKey
+ _kMREventGroupSessionJoinRequestAutoApprovedReasonKey
+ _kMREventGroupSessionJoinRequestHasOOBKeysKey
+ _kMREventGroupSessionJoinRequestIsProxy
+ _kMREventGroupSessionJoinRequestReceived
+ _kMREventGroupSessionJoinRequestSent
+ _kMREventGroupSessionJoinResponseApprovedKey
+ _kMREventGroupSessionJoinResponseReceived
+ _kMREventGroupSessionJoinResponseSent
+ _kMREventGroupSessionJoinResponseSentByHostKey
+ _kMREventGroupSessionJoinSessionYieldDurationKey
+ _kMREventGroupSessionJoinStateConnectedDurationKey
+ _kMREventGroupSessionJoinStateJoinedDurationKey
+ _kMREventGroupSessionLeaderLost
+ _kMREventGroupSessionNearbyNotificationDisplayed
+ _kMREventGroupSessionPreLMIRequestReceived
+ _kMREventGroupSessionPreLMIResponseSent
+ _kMREventJoinSessionModeKey
+ _kMREventJoinSessionModeProximity
+ _kMREventJoinSessionModeQRCode
+ _kMREventJoinSessionModeWHAAutoJoin
+ _kMREventNearbyNotificationTypeInAppBanner
+ _kMREventNearbyNotificationTypeKey
+ _kMREventNearbyNotificationTypeLockScreen
+ _kMREventSessionCreatedNearbyGroupDurationKey
+ _kMREventSessionCreatedNearbyInvitationDurationKey
+ _kMREventSessionCreatedRouteKey
+ _objc_msgSend$createCustomOriginClientForOrigin:routingContextID:
+ _objc_msgSend$initWithOrigin:routingContextID:
+ _objc_msgSend$setJoinURL:
+ _objc_msgSend$verboseImageLoadingLogging
+ _verboseImageLoadingLogging.__once
+ _verboseImageLoadingLogging.__should
- -[MRNowPlayingOriginClient initWithOrigin:]
- -[MRNowPlayingOriginClient routingContextID]
- -[MRNowPlayingOriginClient setRoutingContextID:]
- -[MRNowPlayingOriginClientManager _createOriginClientForPlayerPath:]
- -[MRNowPlayingOriginClientManager createCustomOriginClientForOrigin:]
- -[MRUserSettings minorUserState]
- -[MRUserSettings setMinorUserState:]
- GCC_except_table124
- GCC_except_table129
- GCC_except_table132
- GCC_except_table135
- GCC_except_table143
- GCC_except_table144
- GCC_except_table151
- GCC_except_table156
- GCC_except_table157
- ___55-[MRAVDistantRoutingDiscoverySession setDiscoveryMode:]_block_invoke.76
- ___60-[MRAVDistantRoutingDiscoverySession devicePresenceDetected]_block_invoke.78
- ___60-[MRAVDistantRoutingDiscoverySession devicePresenceDetected]_block_invoke.78.cold.1
- ___71-[MRNowPlayingOriginClient _prepareToRestoreClientStateWithCompletion:]_block_invoke.78
- ___72-[MRAVDistantRoutingDiscoverySession setHostedRoutingSessionConnection:]_block_invoke.80
- ___72-[MRAVDistantRoutingDiscoverySession setHostedRoutingSessionConnection:]_block_invoke.81
- ___72-[MRAVDistantRoutingDiscoverySession setHostedRoutingSessionConnection:]_block_invoke_2.82
- ___Block_byref_object_copy_.52
- ___Block_byref_object_dispose_.53
- ___MRAnalyticsSendEvent_block_invoke.219
- ____MRMediaRemoteGetDeviceUIDWithRetryIntervals_block_invoke.357
- ____MRMediaRemoteGetDeviceUIDWithRetryIntervals_block_invoke.358
- ___block_literal_global.107
- ___block_literal_global.215
- ___block_literal_global.221
- ___block_literal_global.250
- ___block_literal_global.355
- ___block_literal_global.451
- ___block_literal_global.471
- ___block_literal_global.513
- __unnamed_array_storage.499
- _objc_msgSend$createCustomOriginClientForOrigin:
CStrings:
+ "\x02,"
+ "-[MRNowPlayingOriginClientManager _createOriginClientForPlayerPath:routingContextID:]"
+ "ClientNotEntitled"
+ "GroupSessionNearbyGroupCreateTimeout"
+ "GroupSessionNearbyGroupJoinTimeout"
+ "GroupSessionNearbyInvitationCreateTimeout"
+ "MRXPC_DISCOVERY_FEATURES_KEY"
+ "T@\"MRAVRoutingDiscoverySessionConfiguration\",C,N,V_configuration"
+ "T@\"NSString\",&,N,V_joinURL"
+ "[DistantDiscoverySession] %@ ERROR: Failed to fetch hosted routing XPC endpoint. %{public}@"
+ "_joinURL"
+ "autoApproveReasonEnum"
+ "com.apple.mediaremote.group-session.create"
+ "com.apple.mediaremote.group-session.end"
+ "com.apple.mediaremote.group-session.join"
+ "com.apple.mediaremote.group-session.join-attempt"
+ "com.apple.mediaremote.group-session.join-request-received"
+ "com.apple.mediaremote.group-session.join-request-sent"
+ "com.apple.mediaremote.group-session.join-response-received"
+ "com.apple.mediaremote.group-session.join-response-sent"
+ "com.apple.mediaremote.group-session.leader-lost"
+ "com.apple.mediaremote.group-session.nearby-notification-displayed"
+ "com.apple.mediaremote.group-session.pre-lmi-request"
+ "com.apple.mediaremote.group-session.pre-lmi-response"
+ "configurationWithCompletion:"
+ "createCustomOriginClientForOrigin:routingContextID:"
+ "errorDomain"
+ "groupSessionNearbyGroupCreateTimeout"
+ "groupSessionNearbyGroupJoinTimeout"
+ "groupSessionNearbyInvitationCreateTimeout"
+ "hasJoinURL"
+ "hasOobKeys"
+ "initWithOrigin:routingContextID:"
+ "joinModeEnum"
+ "joinURL"
+ "nearbyGroupDuration"
+ "nearbyInvitationDuration"
+ "presenceAssertionDuration"
+ "providerJoinDuration"
+ "routeEnum"
+ "sentByHost"
+ "sessionYieldDuration"
+ "setJoinURL:"
+ "stateConnectedDuration"
+ "stateJoinedDuration"
+ "v24@0:8@?<v@?@\"MRAVRoutingDiscoverySessionConfiguration\">16"
+ "verboseImageLoadingLogging"
+ "whaConnectionDuration"
+ "whaReconDuration"
- "\x02+"
- "-[MRNowPlayingOriginClientManager _createOriginClientForPlayerPath:]"
- "MinorUserState"
- "createCustomOriginClientForOrigin:"
- "minorUserState"
- "setMinorUserState:"

```
