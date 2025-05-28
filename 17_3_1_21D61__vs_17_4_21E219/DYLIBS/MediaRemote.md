## MediaRemote

> `/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote`

```diff

-4023.410.2.0.0
-  __TEXT.__text: 0x2a0b98
-  __TEXT.__auth_stubs: 0x1610
-  __TEXT.__objc_methlist: 0x24c30
-  __TEXT.__const: 0x378
-  __TEXT.__cstring: 0x2873a
-  __TEXT.__oslogstring: 0xcc4a
-  __TEXT.__gcc_except_tab: 0x4de8
+4023.510.2.0.0
+  __TEXT.__text: 0x2a60d0
+  __TEXT.__auth_stubs: 0x1620
+  __TEXT.__objc_methlist: 0x253e8
+  __TEXT.__const: 0x380
+  __TEXT.__cstring: 0x28e1a
+  __TEXT.__oslogstring: 0xcc54
+  __TEXT.__gcc_except_tab: 0x4e74
   __TEXT.__ustring: 0x12
-  __TEXT.__unwind_info: 0xa178
-  __TEXT.__objc_classname: 0x44ef
-  __TEXT.__objc_methname: 0x4324e
-  __TEXT.__objc_methtype: 0x83da
-  __TEXT.__objc_stubs: 0x23440
+  __TEXT.__unwind_info: 0xa244
+  __TEXT.__objc_classname: 0x4567
+  __TEXT.__objc_methname: 0x43c7e
+  __TEXT.__objc_methtype: 0x848f
+  __TEXT.__objc_stubs: 0x238e0
   __DATA_CONST.__got: 0x1c0
-  __DATA_CONST.__const: 0xa180
-  __DATA_CONST.__objc_classlist: 0xfc0
+  __DATA_CONST.__const: 0xa2d0
+  __DATA_CONST.__objc_classlist: 0xff0
   __DATA_CONST.__objc_catlist: 0x60
-  __DATA_CONST.__objc_protolist: 0x230
+  __DATA_CONST.__objc_protolist: 0x228
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x34920
-  __DATA_CONST.__objc_selrefs: 0xceb0
-  __DATA_CONST.__objc_arraydata: 0x1d0
-  __AUTH_CONST.__cfstring: 0x1d5e0
-  __AUTH_CONST.__objc_const: 0xb748
-  __AUTH_CONST.__const: 0x3040
+  __DATA_CONST.__objc_const: 0x34f88
+  __DATA_CONST.__objc_selrefs: 0xd0d0
+  __DATA_CONST.__objc_protorefs: 0x88
+  __DATA_CONST.__objc_classrefs: 0x10e8
+  __DATA_CONST.__objc_superrefs: 0xe28
+  __DATA_CONST.__objc_arraydata: 0x1f0
+  __AUTH_CONST.__cfstring: 0x1e0a0
+  __AUTH_CONST.__objc_const: 0xb988
+  __AUTH_CONST.__const: 0x3000
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__objc_intobj: 0x390
-  __AUTH_CONST.__objc_arrayobj: 0x108
+  __AUTH_CONST.__objc_intobj: 0x3c0
+  __AUTH_CONST.__objc_arrayobj: 0x138
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0xb18
-  __AUTH.__objc_data: 0x74e0
-  __AUTH.__data: 0x1f0
-  __DATA.__objc_protorefs: 0x88
-  __DATA.__objc_classrefs: 0x10d8
-  __DATA.__objc_superrefs: 0xe08
-  __DATA.__objc_ivar: 0x2c94
-  __DATA.__data: 0x1d00
-  __DATA.__bss: 0x500
+  __AUTH_CONST.__auth_got: 0xb20
+  __AUTH.__objc_data: 0x7670
+  __AUTH.__data: 0x1e0
+  __DATA.__objc_ivar: 0x2d10
+  __DATA.__data: 0x1ce8
+  __DATA.__bss: 0x4c8
   __DATA.__common: 0x0
-  __DATA_DIRTY.__objc_data: 0x28a0
-  __DATA_DIRTY.__data: 0x210
-  __DATA_DIRTY.__bss: 0x6f8
+  __DATA_DIRTY.__objc_data: 0x28f0
+  __DATA_DIRTY.__data: 0x1e8
+  __DATA_DIRTY.__bss: 0x6a8
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 17935
-  Symbols:   48763
-  CStrings:  17680
+  Functions: 18079
+  Symbols:   49158
+  CStrings:  17882
 
Symbols:
+ +[MRAVEndpoint pauseOutputDeviceUIDs:details:queue:completion:]
+ +[MRAVRoutingDiscoverySession discoverySessionFactories]
+ +[MRAVRoutingDiscoverySession registerDiscoverySessionFactory:]
+ +[MRCriticalSectionCoordinator enterCriticalSection]
+ +[MRCriticalSectionCoordinator enterCriticalSection].cold.1
+ +[MRCriticalSectionCoordinator enterCriticalSection].cold.2
+ +[MRCriticalSectionCoordinator exitCriticalSection:]
+ +[MRCriticalSectionCoordinator exitCriticalSection:].cold.1
+ +[MRCriticalSectionCoordinator exitCriticalSectionUsingRequestID:]
+ +[MRCriticalSectionCoordinator exitCriticalSectionUsingRequestID:].cold.1
+ +[MRCriticalSectionCoordinator exitCriticalSectionUsingRequestID:].cold.2
+ +[MRGroupSessionEligibilityStatus supportsSecureCoding]
+ +[MRMediaUserState supportsSecureCoding]
+ -[MRAVDistantEndpoint _handleActiveGroupSessionDidChangeNotification:]
+ -[MRAVDistantEndpoint _registerGlobalNotifications]
+ -[MRAVEndpoint waitForPlaybackWithTimeout:queue:completion:]
+ -[MRAVLightweightReconnaissanceSession searchEndpointsForOutputDeviceUID:timeout:details:queue:completion:]
+ -[MRAVLocalEndpoint handleActiveGroupSessionDidChangeNotification:]
+ -[MRAVOutputContextEndpoint groupContainsDiscoverableGroupLeader]
+ -[MRAVOutputDevice isW3Device]
+ -[MRAVReconnaissanceSession _descriptionObjectFromResultOfOutputDevices:endpoints:unanimousEndpoint:]
+ -[MRAVReconnaissanceSession _onQueue_beginSearchWithTimeout:]
+ -[MRAVReconnaissanceSession _onQueue_invokeCompletionWithMatchingDevices:matchingEndpoints:unanimousEndpoint:error:]
+ -[MRAVReconnaissanceSession details]
+ -[MRAVReconnaissanceSession initWithDetails:outputDeviceUIDs:outputDeviceGroupID:features:]
+ -[MRAVReconnaissanceSession setShouldWaitForUnanimousEndpoints:]
+ -[MRAVReconnaissanceSession shouldWaitForUnanimousEndpoints]
+ -[MRCodableGroupSessionParticipant initWithIdentifier:identity:connected:guest:hidden:]
+ -[MRCodableGroupSessionParticipant isHidden]
+ -[MRCodableGroupSessionParticipant setHidden:]
+ -[MRConcreteEndpoint isConnected]
+ -[MRCriticalSectionToken .cxx_destruct]
+ -[MRCriticalSectionToken dealloc]
+ -[MRCriticalSectionToken description]
+ -[MRCriticalSectionToken init]
+ -[MRCriticalSectionToken invalidated]
+ -[MRCriticalSectionToken requestID]
+ -[MRCriticalSectionToken setInvalidated:]
+ -[MRDeviceInfo leaderDeviceInfo]
+ -[MRDeviceInfo setLeaderDeviceInfo:]
+ -[MRGroupSessionEligibilityMonitor .cxx_destruct]
+ -[MRGroupSessionEligibilityMonitor addObserver:]
+ -[MRGroupSessionEligibilityMonitor init]
+ -[MRGroupSessionEligibilityMonitor lock]
+ -[MRGroupSessionEligibilityMonitor observers]
+ -[MRGroupSessionEligibilityMonitor registerNotifications]
+ -[MRGroupSessionEligibilityMonitor removeObserver:]
+ -[MRGroupSessionEligibilityMonitor setLock:]
+ -[MRGroupSessionEligibilityMonitor setObservers:]
+ -[MRGroupSessionEligibilityMonitor status]
+ -[MRGroupSessionEligibilityMonitor updateStatus:]
+ -[MRGroupSessionEligibilityStatus .cxx_destruct]
+ -[MRGroupSessionEligibilityStatus copyWithZone:]
+ -[MRGroupSessionEligibilityStatus currentMediaUserState]
+ -[MRGroupSessionEligibilityStatus description]
+ -[MRGroupSessionEligibilityStatus dictionaryDescription]
+ -[MRGroupSessionEligibilityStatus differenceFrom:]
+ -[MRGroupSessionEligibilityStatus encodeWithCoder:]
+ -[MRGroupSessionEligibilityStatus idsAccountIsValid]
+ -[MRGroupSessionEligibilityStatus initWithCoder:]
+ -[MRGroupSessionEligibilityStatus isEligibleForHostingGroupSession]
+ -[MRGroupSessionEligibilityStatus isEligibleForJoiningGroupSession]
+ -[MRGroupSessionEligibilityStatus isEqual:]
+ -[MRGroupSessionEligibilityStatus isManateeEnabled]
+ -[MRGroupSessionEligibilityStatus mediaAccountHostingState]
+ -[MRGroupSessionEligibilityStatus mediaAccountJoiningState]
+ -[MRGroupSessionEligibilityStatus mediaUserStates]
+ -[MRGroupSessionEligibilityStatus routeIsValidForHosting]
+ -[MRGroupSessionEligibilityStatus routeType]
+ -[MRGroupSessionEligibilityStatus setCurrentMediaUserState:]
+ -[MRGroupSessionEligibilityStatus setIdsAccountIsValid:]
+ -[MRGroupSessionEligibilityStatus setIsEligibleForHostingGroupSession:]
+ -[MRGroupSessionEligibilityStatus setIsEligibleForJoiningGroupSession:]
+ -[MRGroupSessionEligibilityStatus setIsManateeEnabled:]
+ -[MRGroupSessionEligibilityStatus setMediaAccountHostingState:]
+ -[MRGroupSessionEligibilityStatus setMediaAccountJoiningState:]
+ -[MRGroupSessionEligibilityStatus setMediaUserStates:]
+ -[MRGroupSessionEligibilityStatus setRouteIsValidForHosting:]
+ -[MRGroupSessionEligibilityStatus setRouteType:]
+ -[MRGroupSessionRequestManager eligibilityStatus]
+ -[MRGroupSessionRequestManager setEligibilityStatus:]
+ -[MRGroupSessionRequestManager updateGroupSessionEligibility:]
+ -[MRGroupSessionToken initWithHostInfo:invitationData:sharedSecret:sessionIdentifier:equivalentMediaIdentifier:version:]
+ -[MRGroupSessionToken version]
+ -[MRGroupTopologyModificationRequest description]
+ -[MRMediaRemoteService createTokenWithInvitationData:equivalentMediaIdentifier:version:]
+ -[MRMediaRemoteService presentProximityCardWithDeviceName:modelIdentifier:color:url:queue:completion:]
+ -[MRMediaSuggestionRequestOptions description]
+ -[MRMediaUserState .cxx_destruct]
+ -[MRMediaUserState copyWithZone:]
+ -[MRMediaUserState description]
+ -[MRMediaUserState encodeWithCoder:]
+ -[MRMediaUserState groupSessionsSupportedForAccountRegion]
+ -[MRMediaUserState hasAcceptedDisplayNameAcknowledgement]
+ -[MRMediaUserState hasAcceptedPrivacyAcknowledgement]
+ -[MRMediaUserState hash]
+ -[MRMediaUserState identifier]
+ -[MRMediaUserState identitySupportsCollaboration]
+ -[MRMediaUserState initWithCoder:]
+ -[MRMediaUserState isEqual:]
+ -[MRMediaUserState isFullSubscriber]
+ -[MRMediaUserState isMinor]
+ -[MRMediaUserState setGroupSessionsSupportedForAccountRegion:]
+ -[MRMediaUserState setHasAcceptedDisplayNameAcknowledgement:]
+ -[MRMediaUserState setHasAcceptedPrivacyAcknowledgement:]
+ -[MRMediaUserState setIdentifier:]
+ -[MRMediaUserState setIdentitySupportsCollaboration:]
+ -[MRMediaUserState setIsFullSubscriber:]
+ -[MRMediaUserState setIsMinor:]
+ -[MRMediaUserState setStorefrontCountryCode:]
+ -[MRMediaUserState setUserIdentity:]
+ -[MRMediaUserState storefrontCountryCode]
+ -[MRMediaUserState userIdentity]
+ -[MRNotificationServiceClient _handleActiveGroupSessionInfoDidChangeNotification:]
+ -[MRNotificationServiceClient _handleLocalGroupSessionEligibilityDidChangeNotification:]
+ -[MRPlayerPath initWithOrigin:bundleIdentifier:player:]
+ -[MRRemoteControlGroupSession canHandleJoinRequests]
+ -[MRRemoteControlGroupSession canManageParticipants]
+ -[MRRequestDetails description]
+ -[MRSharedSettings supportAirPlayLeaderInfoSync]
+ -[MRSharedSettings supportGroupSessionHomePodBoop]
+ -[MRUserSettings preferRoutesMatchingMediaType]
+ -[MRUserSettings supportCriticalSectionManagement]
+ -[MRUserSettings supportLiveActivityBanner]
+ -[MRUserSettings waveformNonVariableFramerate]
+ -[NSError(MRAdditions) mr_isMediaRemoteError]
+ -[_MRAirPlayLeaderInfoProtobuf .cxx_destruct]
+ -[_MRAirPlayLeaderInfoProtobuf copyTo:]
+ -[_MRAirPlayLeaderInfoProtobuf copyWithZone:]
+ -[_MRAirPlayLeaderInfoProtobuf description]
+ -[_MRAirPlayLeaderInfoProtobuf deviceInfo]
+ -[_MRAirPlayLeaderInfoProtobuf dictionaryRepresentation]
+ -[_MRAirPlayLeaderInfoProtobuf hasDeviceInfo]
+ -[_MRAirPlayLeaderInfoProtobuf hash]
+ -[_MRAirPlayLeaderInfoProtobuf isEqual:]
+ -[_MRAirPlayLeaderInfoProtobuf mergeFrom:]
+ -[_MRAirPlayLeaderInfoProtobuf readFrom:]
+ -[_MRAirPlayLeaderInfoProtobuf setDeviceInfo:]
+ -[_MRAirPlayLeaderInfoProtobuf writeTo:]
+ -[_MRCommandInfoProtobuf StringAsSleepTimerStopMode:]
+ -[_MRCommandInfoProtobuf hasSleepTimerFireDate]
+ -[_MRCommandInfoProtobuf hasSleepTimerStopMode]
+ -[_MRCommandInfoProtobuf hasSleepTimerTime]
+ -[_MRCommandInfoProtobuf setHasSleepTimerFireDate:]
+ -[_MRCommandInfoProtobuf setHasSleepTimerStopMode:]
+ -[_MRCommandInfoProtobuf setHasSleepTimerTime:]
+ -[_MRCommandInfoProtobuf setSleepTimerFireDate:]
+ -[_MRCommandInfoProtobuf setSleepTimerStopMode:]
+ -[_MRCommandInfoProtobuf setSleepTimerTime:]
+ -[_MRCommandInfoProtobuf sleepTimerFireDate]
+ -[_MRCommandInfoProtobuf sleepTimerStopModeAsString:]
+ -[_MRCommandInfoProtobuf sleepTimerStopMode]
+ -[_MRCommandInfoProtobuf sleepTimerTime]
+ -[_MRCommandOptionsProtobuf StringAsSleepTimerStopMode:]
+ -[_MRCommandOptionsProtobuf hasSleepTimerStopMode]
+ -[_MRCommandOptionsProtobuf hasSleepTimerTime]
+ -[_MRCommandOptionsProtobuf setHasSleepTimerStopMode:]
+ -[_MRCommandOptionsProtobuf setHasSleepTimerTime:]
+ -[_MRCommandOptionsProtobuf setSleepTimerStopMode:]
+ -[_MRCommandOptionsProtobuf setSleepTimerTime:]
+ -[_MRCommandOptionsProtobuf sleepTimerStopModeAsString:]
+ -[_MRCommandOptionsProtobuf sleepTimerStopMode]
+ -[_MRCommandOptionsProtobuf sleepTimerTime]
+ -[_MRDeviceInfoMessageProtobuf hasLeaderDeviceInfo]
+ -[_MRDeviceInfoMessageProtobuf leaderDeviceInfo]
+ -[_MRDeviceInfoMessageProtobuf setLeaderDeviceInfo:]
+ -[_MRGroupSessionParticipantProtobuf hasHidden]
+ -[_MRGroupSessionParticipantProtobuf hidden]
+ -[_MRGroupSessionParticipantProtobuf setHasHidden:]
+ -[_MRGroupSessionParticipantProtobuf setHidden:]
+ -[_MRGroupSessionTokenProtobuf hasVersion]
+ -[_MRGroupSessionTokenProtobuf setHasVersion:]
+ -[_MRGroupSessionTokenProtobuf setVersion:]
+ -[_MRGroupSessionTokenProtobuf version]
+ GCC_except_table102
+ GCC_except_table115
+ GCC_except_table118
+ GCC_except_table119
+ GCC_except_table183
+ GCC_except_table184
+ GCC_except_table192
+ GCC_except_table213
+ GCC_except_table214
+ GCC_except_table269
+ GCC_except_table285
+ GCC_except_table98
+ OBJC_IVAR_$__MRAirPlayLeaderInfoProtobuf._deviceInfo
+ OBJC_IVAR_$__MRCommandInfoProtobuf._sleepTimerFireDate
+ OBJC_IVAR_$__MRCommandInfoProtobuf._sleepTimerStopMode
+ OBJC_IVAR_$__MRCommandInfoProtobuf._sleepTimerTime
+ OBJC_IVAR_$__MRCommandOptionsProtobuf._sleepTimerStopMode
+ OBJC_IVAR_$__MRCommandOptionsProtobuf._sleepTimerTime
+ OBJC_IVAR_$__MRDeviceInfoMessageProtobuf._leaderDeviceInfo
+ OBJC_IVAR_$__MRGroupSessionParticipantProtobuf._hidden
+ OBJC_IVAR_$__MRGroupSessionTokenProtobuf._has
+ OBJC_IVAR_$__MRGroupSessionTokenProtobuf._version
+ _BMPublisherOptionsFunction
+ _BiomeLibraryLibrary.sLib
+ _BiomeLibraryLibrary.sOnce
+ _BiomeStreamsLibrary.sLib
+ _BiomeStreamsLibrary.sOnce
+ _MRActiveGroupSessionInfoDidChangeNotification
+ _MRActiveGroupSessionInfoUserInfoKey
+ _MRCreateEndpointFromXPCMessage
+ _MRCriticalSectionTransitionKey
+ _MRCriticalSectionTransitionNotification
+ _MREndpointFromXPCMessage
+ _MRGroupSessionAllowsMigrationForEndpoint
+ _MRGroupSessionEligibilityDidChangeNotification
+ _MRGroupSessionEligibilityStatusUserInfoKey
+ _MRGroupSessionRouteTypeForOutputDevices
+ _MRGroupSessionTokenVersion
+ _MRMediaRemoteAirPlayReceiverCopyAirPlayLeaderInfoData
+ _MRMediaRemoteSendCommandErrorDescription
+ _OBJC_CLASS_$_MRCriticalSectionCoordinator
+ _OBJC_CLASS_$_MRCriticalSectionToken
+ _OBJC_CLASS_$_MRGroupSessionEligibilityMonitor
+ _OBJC_CLASS_$_MRGroupSessionEligibilityStatus
+ _OBJC_CLASS_$_MRMediaUserState
+ _OBJC_CLASS_$__MRAirPlayLeaderInfoProtobuf
+ _OBJC_IVAR_$_MRAVReconnaissanceSession._completion
+ _OBJC_IVAR_$_MRAVReconnaissanceSession._details
+ _OBJC_IVAR_$_MRCodableGroupSessionParticipant._hidden
+ _OBJC_IVAR_$_MRCriticalSectionToken._invalidated
+ _OBJC_IVAR_$_MRCriticalSectionToken._requestID
+ _OBJC_IVAR_$_MRDeviceInfo._leaderDeviceInfo
+ _OBJC_IVAR_$_MRGroupSessionEligibilityMonitor._lock
+ _OBJC_IVAR_$_MRGroupSessionEligibilityMonitor._observers
+ _OBJC_IVAR_$_MRGroupSessionEligibilityMonitor._status
+ _OBJC_IVAR_$_MRGroupSessionEligibilityStatus._currentMediaUserState
+ _OBJC_IVAR_$_MRGroupSessionEligibilityStatus._idsAccountIsValid
+ _OBJC_IVAR_$_MRGroupSessionEligibilityStatus._isEligibleForHostingGroupSession
+ _OBJC_IVAR_$_MRGroupSessionEligibilityStatus._isEligibleForJoiningGroupSession
+ _OBJC_IVAR_$_MRGroupSessionEligibilityStatus._isManateeEnabled
+ _OBJC_IVAR_$_MRGroupSessionEligibilityStatus._mediaAccountHostingState
+ _OBJC_IVAR_$_MRGroupSessionEligibilityStatus._mediaAccountJoiningState
+ _OBJC_IVAR_$_MRGroupSessionEligibilityStatus._mediaUserStates
+ _OBJC_IVAR_$_MRGroupSessionEligibilityStatus._routeIsValidForHosting
+ _OBJC_IVAR_$_MRGroupSessionEligibilityStatus._routeType
+ _OBJC_IVAR_$_MRGroupSessionRequestManager._eligibilityStatus
+ _OBJC_IVAR_$_MRGroupSessionToken._version
+ _OBJC_IVAR_$_MRMediaSuggestionController._suggestions
+ _OBJC_IVAR_$_MRMediaUserState._groupSessionsSupportedForAccountRegion
+ _OBJC_IVAR_$_MRMediaUserState._hasAcceptedDisplayNameAcknowledgement
+ _OBJC_IVAR_$_MRMediaUserState._hasAcceptedPrivacyAcknowledgement
+ _OBJC_IVAR_$_MRMediaUserState._identifier
+ _OBJC_IVAR_$_MRMediaUserState._identitySupportsCollaboration
+ _OBJC_IVAR_$_MRMediaUserState._isFullSubscriber
+ _OBJC_IVAR_$_MRMediaUserState._isMinor
+ _OBJC_IVAR_$_MRMediaUserState._storefrontCountryCode
+ _OBJC_IVAR_$_MRMediaUserState._userIdentity
+ _OBJC_METACLASS_$_MRCriticalSectionCoordinator
+ _OBJC_METACLASS_$_MRCriticalSectionToken
+ _OBJC_METACLASS_$_MRGroupSessionEligibilityMonitor
+ _OBJC_METACLASS_$_MRGroupSessionEligibilityStatus
+ _OBJC_METACLASS_$_MRMediaUserState
+ _OBJC_METACLASS_$__MRAirPlayLeaderInfoProtobuf
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_9
+ __MRAirPlayLeaderInfoProtobufReadFrom
+ __MRGroupSessionEligibilityDidChangeNotification
+ __MRGroupSessionEligibilityStatusDataUserInfoKey
+ __MRUnarchiveObjectForKey
+ __OBJC_$_CLASS_METHODS_MRCriticalSectionCoordinator
+ __OBJC_$_CLASS_METHODS_MRGroupSessionEligibilityStatus
+ __OBJC_$_CLASS_METHODS_MRMediaUserState
+ __OBJC_$_CLASS_PROP_LIST_MRAVRoutingDiscoverySession
+ __OBJC_$_CLASS_PROP_LIST_MRGroupSessionEligibilityStatus
+ __OBJC_$_CLASS_PROP_LIST_MRMediaUserState
+ __OBJC_$_INSTANCE_METHODS_MRCriticalSectionToken
+ __OBJC_$_INSTANCE_METHODS_MRGroupSessionEligibilityMonitor
+ __OBJC_$_INSTANCE_METHODS_MRGroupSessionEligibilityStatus
+ __OBJC_$_INSTANCE_METHODS_MRMediaUserState
+ __OBJC_$_INSTANCE_METHODS__MRAirPlayLeaderInfoProtobuf
+ __OBJC_$_INSTANCE_VARIABLES_MRCriticalSectionToken
+ __OBJC_$_INSTANCE_VARIABLES_MRGroupSessionEligibilityMonitor
+ __OBJC_$_INSTANCE_VARIABLES_MRGroupSessionEligibilityStatus
+ __OBJC_$_INSTANCE_VARIABLES_MRMediaUserState
+ __OBJC_$_INSTANCE_VARIABLES__MRAirPlayLeaderInfoProtobuf
+ __OBJC_$_PROP_LIST_MRCriticalSectionToken
+ __OBJC_$_PROP_LIST_MRGroupSessionEligibilityMonitor
+ __OBJC_$_PROP_LIST_MRGroupSessionEligibilityStatus
+ __OBJC_$_PROP_LIST_MRMediaUserState
+ __OBJC_$_PROP_LIST__MRAirPlayLeaderInfoProtobuf
+ __OBJC_CLASS_PROTOCOLS_$_MRGroupSessionEligibilityStatus
+ __OBJC_CLASS_PROTOCOLS_$_MRMediaUserState
+ __OBJC_CLASS_PROTOCOLS_$__MRAirPlayLeaderInfoProtobuf
+ __OBJC_CLASS_RO_$_MRCriticalSectionCoordinator
+ __OBJC_CLASS_RO_$_MRCriticalSectionToken
+ __OBJC_CLASS_RO_$_MRGroupSessionEligibilityMonitor
+ __OBJC_CLASS_RO_$_MRGroupSessionEligibilityStatus
+ __OBJC_CLASS_RO_$_MRMediaUserState
+ __OBJC_CLASS_RO_$__MRAirPlayLeaderInfoProtobuf
+ __OBJC_METACLASS_RO_$_MRCriticalSectionCoordinator
+ __OBJC_METACLASS_RO_$_MRCriticalSectionToken
+ __OBJC_METACLASS_RO_$_MRGroupSessionEligibilityMonitor
+ __OBJC_METACLASS_RO_$_MRGroupSessionEligibilityStatus
+ __OBJC_METACLASS_RO_$_MRMediaUserState
+ __OBJC_METACLASS_RO_$__MRAirPlayLeaderInfoProtobuf
+ ___102-[MRMediaRemoteService presentProximityCardWithDeviceName:modelIdentifier:color:url:queue:completion:]_block_invoke
+ ___103-[MRAVLightweightReconnaissanceSession searchEndpointsForCompanionWithTimeout:reason:queue:completion:]_block_invoke.109
+ ___104-[MRAVLightweightReconnaissanceSession searchForLogicalOutputDeviceUID:timeout:reason:queue:completion:]_block_invoke.130
+ ___105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke.547
+ ___105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke.549
+ ___105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke.554
+ ___105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke.561
+ ___105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke_2.550
+ ___106-[MRAVLightweightReconnaissanceSession searchForOutputDevices:categories:timeout:reason:queue:completion:]_block_invoke.168
+ ___106-[MRAVLightweightReconnaissanceSession searchForOutputDevices:categories:timeout:reason:queue:completion:]_block_invoke.178
+ ___106-[MRAVLightweightReconnaissanceSession searchForOutputDevices:categories:timeout:reason:queue:completion:]_block_invoke_2.179
+ ___107-[MRAVLightweightReconnaissanceSession searchEndpointsForMyGroupLeaderWithTimeout:reason:queue:completion:]_block_invoke.146
+ ___107-[MRAVLightweightReconnaissanceSession searchEndpointsForOutputDeviceUID:timeout:details:queue:completion:]_block_invoke
+ ___107-[MRAVLightweightReconnaissanceSession searchEndpointsForOutputDeviceUID:timeout:details:queue:completion:]_block_invoke.31
+ ___107-[MRAVLightweightReconnaissanceSession searchEndpointsForOutputDeviceUID:timeout:details:queue:completion:]_block_invoke.45
+ ___107-[MRAVLightweightReconnaissanceSession searchEndpointsForOutputDeviceUID:timeout:details:queue:completion:]_block_invoke.68
+ ___107-[MRAVLightweightReconnaissanceSession searchEndpointsForOutputDeviceUID:timeout:details:queue:completion:]_block_invoke.74
+ ___107-[MRAVLightweightReconnaissanceSession searchEndpointsForOutputDeviceUID:timeout:details:queue:completion:]_block_invoke.83
+ ___107-[MRAVLightweightReconnaissanceSession searchEndpointsForOutputDeviceUID:timeout:details:queue:completion:]_block_invoke.cold.1
+ ___107-[MRAVLightweightReconnaissanceSession searchEndpointsForOutputDeviceUID:timeout:details:queue:completion:]_block_invoke_2
+ ___107-[MRAVLightweightReconnaissanceSession searchEndpointsForOutputDeviceUID:timeout:details:queue:completion:]_block_invoke_3
+ ___108-[MRAVLightweightReconnaissanceSession searchEndpointsForRoutingContextUID:timeout:reason:queue:completion:]_block_invoke.142
+ ___112-[MRAVLightweightReconnaissanceSession searchEndpointsForLeaderOutputDeviceUID:timeout:reason:queue:completion:]_block_invoke.113
+ ___122-[MRAVEndpoint willStartingPlaybackToOutputDevicesInterruptPlayback:originatingOutputDeviceUID:duration:queue:completion:]_block_invoke.529
+ ___122-[MRAVEndpoint willStartingPlaybackToOutputDevicesInterruptPlayback:originatingOutputDeviceUID:duration:queue:completion:]_block_invoke.537
+ ___122-[MRDistantExternalDevice _onSerialQueue_prepareToConnectWithOptions:userInfo:connectionAttemptDetails:connectionHandler:]_block_invoke.281
+ ___122-[MRDistantExternalDevice _onSerialQueue_prepareToConnectWithOptions:userInfo:connectionAttemptDetails:connectionHandler:]_block_invoke_2.282
+ ___25-[MRMediaControls _reset]_block_invoke.69
+ ___31-[MRUIController xpcConnection]_block_invoke.135
+ ___36+[MRIRRoute routeWithOutputDevices:]_block_invoke.107
+ ___37-[MRDistantExternalDevice deviceInfo]_block_invoke.224
+ ___37-[MRDistantExternalDevice deviceInfo]_block_invoke_2.225
+ ___39-[MRDistantExternalDevice customOrigin]_block_invoke.228
+ ___39-[MRDistantExternalDevice customOrigin]_block_invoke_2.230
+ ___44-[MRDistantExternalDevice groupSessionToken]_block_invoke.222
+ ___47-[MROutputContextController _inititalizeVolume]_block_invoke.264
+ ___47-[MROutputContextController _inititalizeVolume]_block_invoke.266
+ ___48-[MRDistantExternalDevice externalOutputContext]_block_invoke.219
+ ___48-[MRDistantExternalDevice personalOutputDevices]_block_invoke.299
+ ___54-[MRRemoteControlGroupSession session:didChangeState:]_block_invoke.365
+ ___55-[MRAVDistantRoutingDiscoverySession setDiscoveryMode:]_block_invoke.76
+ ___55-[MRAVReconnaissanceSession _onQueue_processSearchLoop]_block_invoke.45
+ ___55-[MRAVReconnaissanceSession _onQueue_processSearchLoop]_block_invoke.48
+ ___56+[MRAVRoutingDiscoverySession discoverySessionFactories]_block_invoke
+ ___56-[MRRemoteControlGroupSession session:didUpdateMembers:]_block_invoke.368
+ ___58-[MRV2NowPlayingController _configureReloadTimerForError:]_block_invoke.188
+ ___60-[MRAVDistantRoutingDiscoverySession devicePresenceDetected]_block_invoke.78
+ ___60-[MRAVDistantRoutingDiscoverySession devicePresenceDetected]_block_invoke.78.cold.1
+ ___60-[MRAVEndpoint waitForPlaybackWithTimeout:queue:completion:]_block_invoke
+ ___60-[MRAVEndpoint waitForPlaybackWithTimeout:queue:completion:]_block_invoke.447
+ ___60-[MRAVEndpoint waitForPlaybackWithTimeout:queue:completion:]_block_invoke.cold.1
+ ___60-[MRAVEndpoint waitForPlaybackWithTimeout:queue:completion:]_block_invoke_2
+ ___60-[MRAVEndpoint waitForPlaybackWithTimeout:queue:completion:]_block_invoke_3
+ ___60-[MRAVEndpoint waitForPlaybackWithTimeout:queue:completion:]_block_invoke_4
+ ___60-[MRAVEndpoint waitForPlaybackWithTimeout:queue:completion:]_block_invoke_5
+ ___60-[MRAVEndpoint waitForPlaybackWithTimeout:queue:completion:]_block_invoke_6
+ ___60-[MRRemoteControlGroupSession removeParticipant:completion:]_block_invoke.354
+ ___60-[MRRemoteControlGroupSession removeParticipant:completion:]_block_invoke.354.cold.1
+ ___60-[MRRemoteControlGroupSession removeParticipant:completion:]_block_invoke.355
+ ___61-[MRRemoteControlGroupSession session:didUpdateParticipants:]_block_invoke.366
+ ___62-[MRRemoteControlGroupSession session:didInvalidateWithError:]_block_invoke.372
+ ___63+[MRAVEndpoint pauseOutputDeviceUIDs:details:queue:completion:]_block_invoke
+ ___63+[MRAVEndpoint pauseOutputDeviceUIDs:details:queue:completion:]_block_invoke.515
+ ___63+[MRAVEndpoint pauseOutputDeviceUIDs:details:queue:completion:]_block_invoke.cold.1
+ ___65-[MRDistantExternalDevice hostedExternalDeviceEndpointDidChange:]_block_invoke.303
+ ___65-[MRRemoteControlGroupSession denyPendingParticipant:completion:]_block_invoke.341
+ ___65-[MRRemoteControlGroupSession denyPendingParticipant:completion:]_block_invoke.341.cold.1
+ ___65-[MRRemoteControlGroupSession denyPendingParticipant:completion:]_block_invoke.342
+ ___66-[MRAVReconnaissanceSession beginSearchWithTimeout:mapCompletion:]_block_invoke.26
+ ___66-[MRAVReconnaissanceSession beginSearchWithTimeout:mapCompletion:]_block_invoke.cold.1
+ ___66-[MRDistantExternalDevice connectWithOptions:userInfo:completion:]_block_invoke.265
+ ___66-[MRDistantExternalDevice hostedExternalDeviceDidAddOutputDevice:]_block_invoke.308
+ ___67+[MRAVEndpoint directEndpointForOutputDeviceUIDs:queue:completion:]_block_invoke.494
+ ___67+[MRAVEndpoint hostedEndpointForOutputDeviceUIDs:queue:completion:]_block_invoke.487
+ ___67-[MRDistantExternalDevice hostedExternalDeviceDeviceInfoDidChange:]_block_invoke.301
+ ___67-[MRRemoteControlGroupSession assertSessionManagementScreenVisible]_block_invoke.348
+ ___67-[MRRemoteControlGroupSession assertSessionManagementScreenVisible]_block_invoke.348.cold.1
+ ___67-[MRRemoteControlGroupSession assertSessionManagementScreenVisible]_block_invoke.350
+ ___67-[MRRemoteControlGroupSession assertSessionManagementScreenVisible]_block_invoke.353
+ ___67-[MRRemoteControlGroupSession assertSessionManagementScreenVisible]_block_invoke.353.cold.1
+ ___68-[MRAVEndpoint modifyTopologyWithRequest:withReplyQueue:completion:]_block_invoke.cold.1
+ ___68-[MRNowPlayingController sendCommand:options:appOptions:completion:]_block_invoke_2
+ ___68-[MRRemoteControlGroupSession approvePendingParticipant:completion:]_block_invoke.335
+ ___68-[MRRemoteControlGroupSession approvePendingParticipant:completion:]_block_invoke.335.cold.1
+ ___68-[MRRemoteControlGroupSession approvePendingParticipant:completion:]_block_invoke.337
+ ___68-[MRRemoteControlGroupSession session:didUpdatePendingParticipants:]_block_invoke.367
+ ___68-[MRV2NowPlayingController _handlePlaybackQueueChangedNotification:]_block_invoke.139
+ ___69-[MRDistantExternalDevice hostedExternalDeviceDidChangeOutputDevice:]_block_invoke.309
+ ___69-[MRDistantExternalDevice hostedExternalDeviceDidRemoveOutputDevice:]_block_invoke.310
+ ___69-[MRRemoteControlGroupSession session:didUpdateSynchronizedMetadata:]_block_invoke.371
+ ___70-[MRMediaSuggestionRequest performWithPreferences:options:completion:]_block_invoke.93
+ ___70-[MRMediaSuggestionRequest performWithPreferences:options:completion:]_block_invoke_2.96
+ ___70-[MRMediaSuggestionRequest performWithPreferences:options:completion:]_block_invoke_2.96.cold.1
+ ___70-[MRMediaSuggestionRequest performWithPreferences:options:completion:]_block_invoke_5
+ ___72-[MRAVDistantRoutingDiscoverySession setHostedRoutingSessionConnection:]_block_invoke.81
+ ___72-[MRAVDistantRoutingDiscoverySession setHostedRoutingSessionConnection:]_block_invoke_2.82
+ ___72-[MRV2NowPlayingController _handleSupportedCommandsChangedNotification:]_block_invoke.144
+ ___74-[MRDistantExternalDevice hostedExternalDeviceGroupSessionTokenDidChange:]_block_invoke.311
+ ___76+[MRAVEndpoint createEndpointWithOutputDeviceUIDs:options:queue:completion:]_block_invoke.501
+ ___76+[MRAVEndpoint createEndpointWithOutputDeviceUIDs:options:queue:completion:]_block_invoke.505
+ ___77-[MRDistantExternalDevice hostedExternalDeviceDidReceiveCustomData:withName:]_block_invoke.302
+ ___79-[MRDistantExternalDevice hostedExternalDeviceVolumeDidChange:forOutputDevice:]_block_invoke.306
+ ___80-[MRDistantExternalDevice hostedExternalDeviceIsMutedDidChange:forOutputDevice:]_block_invoke.307
+ ___81-[MRV2NowPlayingController _resolveForUnresolvedPlayerPath:requestID:completion:]_block_invoke.102
+ ___81-[MRV2NowPlayingController _resolveForUnresolvedPlayerPath:requestID:completion:]_block_invoke.103
+ ___81-[MRV2NowPlayingController _resolveForUnresolvedPlayerPath:requestID:completion:]_block_invoke.103.cold.1
+ ___83-[MRV2NowPlayingController _resolveForEndpoint:client:player:requestID:completion:]_block_invoke.94
+ ___83-[MRV2NowPlayingController _resolveForEndpoint:client:player:requestID:completion:]_block_invoke.95
+ ___83-[MRV2NowPlayingController _resolveForEndpoint:client:player:requestID:completion:]_block_invoke.95.cold.1
+ ___86+[MRNowPlayingController sendCommand:toDestination:options:appOptions:withCompletion:]_block_invoke_4
+ ___90-[MRDistantExternalDevice setOutputDeviceVolume:outputDeviceUID:details:queue:completion:]_block_invoke.288
+ ___90-[MRV2NowPlayingController _resolveForOutputDeviceUID:client:player:requestID:completion:]_block_invoke.86.cold.1
+ ___91-[MRAVReconnaissanceSession initWithDetails:outputDeviceUIDs:outputDeviceGroupID:features:]_block_invoke
+ ___91-[MRAVReconnaissanceSession initWithDetails:outputDeviceUIDs:outputDeviceGroupID:features:]_block_invoke_2
+ ___91-[MRAVReconnaissanceSession initWithDetails:outputDeviceUIDs:outputDeviceGroupID:features:]_block_invoke_3
+ ___91-[MRAVReconnaissanceSession initWithDetails:outputDeviceUIDs:outputDeviceGroupID:features:]_block_invoke_4
+ ___91-[MRAVReconnaissanceSession initWithDetails:outputDeviceUIDs:outputDeviceGroupID:features:]_block_invoke_5
+ ___91-[MRAVReconnaissanceSession initWithDetails:outputDeviceUIDs:outputDeviceGroupID:features:]_block_invoke_6
+ ___91-[MRDistantExternalDevice hostedExternalDeviceVolumeCapabilitiesDidChange:forOutputDevice:]_block_invoke.305
+ ___91-[MRDistantExternalDevice muteOutputDeviceVolume:outputDeviceUID:details:queue:completion:]_block_invoke.297
+ ___91-[MRV2NowPlayingController _loadNowPlayingStateForResolvedPlayerPath:requestID:completion:]_block_invoke.110
+ ___91-[MRV2NowPlayingController _loadNowPlayingStateForResolvedPlayerPath:requestID:completion:]_block_invoke.110.cold.1
+ ___91-[MRV2NowPlayingController _loadNowPlayingStateForResolvedPlayerPath:requestID:completion:]_block_invoke.111
+ ___91-[MRV2NowPlayingController _resolveForOutputContextUID:client:player:requestID:completion:]_block_invoke.cold.1
+ ___92-[MRAVLightweightReconnaissanceSession searchOutputDevices:reason:timeout:queue:completion:]_block_invoke.154
+ ___93-[MRDistantExternalDevice adjustOutputDeviceVolume:outputDeviceUID:details:queue:completion:]_block_invoke.293
+ ___97-[MRAVLightweightReconnaissanceSession searchForOutputDeviceUID:timeout:reason:queue:completion:]_block_invoke.120
+ ___97-[MRAVLightweightReconnaissanceSession searchForOutputDeviceUID:timeout:reason:queue:completion:]_block_invoke.122
+ ___97-[MRAVLightweightReconnaissanceSession searchForOutputDeviceUID:timeout:reason:queue:completion:]_block_invoke.126
+ ___99-[MRAVLightweightReconnaissanceSession searchEndpointsForGroupUID:timeout:reason:queue:completion:]_block_invoke.105
+ ___99-[MRAVLightweightReconnaissanceSession searchEndpointsForGroupUID:timeout:reason:queue:completion:]_block_invoke.97
+ ___BiomeLibraryLibrary_block_invoke
+ ___BiomeStreamsLibrary_block_invoke
+ ___MRCreateDecodedUserInfo_block_invoke.105
+ ___MRCreateDecodedUserInfo_block_invoke.96
+ ___MRCreateDecodedUserInfo_block_invoke_2.110
+ ___MRCreateDecodedUserInfo_block_invoke_2.99
+ ___MRCreateDecodedUserInfo_block_invoke_3.102
+ ___MRCreateDecodedUserInfo_block_invoke_3.113
+ ___MRCreateDecodedUserInfo_block_invoke_4.116
+ ___MRCreateDecodedUserInfo_block_invoke_5.119
+ ___MRCreateEncodedUserInfo_block_invoke.148
+ ___MRCreateEncodedUserInfo_block_invoke_11
+ ___MRCreateEncodedUserInfo_block_invoke_11.cold.1
+ ___MRCreateEncodedUserInfo_block_invoke_2.152
+ ___MRCreateEncodedUserInfo_block_invoke_3.155
+ ___MRCreateEncodedUserInfo_block_invoke_4.159
+ ___MRCreateEncodedUserInfo_block_invoke_5.163
+ ___MRCreateEncodedUserInfo_block_invoke_6.167
+ ___MRGroupSessionJoinSessionWithToken_block_invoke.290
+ ___MRGroupSessionJoinSessionWithToken_block_invoke.294
+ ___MRMediaRemoteGetClientProperties_block_invoke.523
+ ___MRMediaRemoteGetPlaybackStateForPlayer_block_invoke.563
+ ___MRMediaRemoteGetPlayerProperties_block_invoke.554
+ ___MRMediaRemoteNowPlayingResolvePlayerPathWithID_block_invoke.84
+ ___MRMediaRemoteNowPlayingResolvePlayerPathWithID_block_invoke.99
+ ___MRMediaRemoteSetPlaybackStateForPlayerWithTimestamp_block_invoke.581
+ ___MRNowPlayingSessionManagerStartSession_block_invoke.44
+ ___MRNowPlayingSessionManagerStartSession_block_invoke.57
+ ___MRNowPlayingSessionManagerStartSession_block_invoke.61
+ ___MRServiceClientRemotePlayerPathCommandCallback_block_invoke.97
+ ____MRMediaRemoteSendCommandToPlayerWithResult_block_invoke_2.cold.2
+ ____MRServiceClientRemoteResolvedPlayerPathCommandCallback_block_invoke.74
+ ____MRServiceClientRemoteResolvedPlayerPathCommandCallback_block_invoke.74.cold.1
+ ____MRServiceClientRemoteResolvedPlayerPathCommandCallback_block_invoke.74.cold.2
+ ____MRServiceClientRemoteResolvedPlayerPathCommandCallback_block_invoke.75
+ ____MRServiceClientRemoteResolvedPlayerPathCommandCallback_block_invoke.76
+ ____MRUnarchiveObjectForKey_block_invoke
+ ____MRUnarchiveObjectForKey_block_invoke.cold.1
+ ___block_descriptor_40_e8_32bs_e36_v16?0"MRNowPlayingPlayerResponse"8ls32l8
+ ___block_descriptor_40_e8_32s_e16_16?0"NSData"8ls32l8
+ ___block_descriptor_56_e8_32s40s48bs_e42_v32?0"NSArray"8"NSString"16"NSError"24ls32l8s48l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e5_B8?0ls32l8r48l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e22_B16?0"BMStoreEvent"8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s_e25_v16?0"MRCommandResult"8ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs56r_e17_v16?0"NSArray"8lr56l8s32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e54_v40?0"NSArray"8"NSString"16"NSArray"24"NSError"32ls32l8s40l8s48l8s56l8
+ ___block_descriptor_68_e8_32s40s48s56bs_e25_v16?0"MRCommandResult"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e23_v16?0"BPSCompletion"8ls32l8s40l8s48l8s64l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e25_v16?0"MRCommandResult"8ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_76_e8_32s40s48s56bs_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_76_e8_32s40s48s56s64r_e5_v8?0ls32l8s40l8s48l8s56l8r64l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72bs_e25_v16?0"MRCommandResult"8ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_92_e8_32s40s48s56s64s72bs80bs_e5_v8?0ls32l8s72l8s40l8s48l8s56l8s64l8s80l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80bs88r_e17_v16?0"NSError"8ls32l8r88l8s40l8s48l8s56l8s64l8s80l8s72l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80r_e22_B16?0"BMStoreEvent"8ls32l8s40l8s48l8s56l8s64l8s72l8r80l8
+ ___block_literal_global.107
+ ___block_literal_global.108
+ ___block_literal_global.115
+ ___block_literal_global.117
+ ___block_literal_global.123
+ ___block_literal_global.129
+ ___block_literal_global.139
+ ___block_literal_global.141
+ ___block_literal_global.147
+ ___block_literal_global.149
+ ___block_literal_global.154
+ ___block_literal_global.162
+ ___block_literal_global.165
+ ___block_literal_global.172
+ ___block_literal_global.179
+ ___block_literal_global.183
+ ___block_literal_global.203
+ ___block_literal_global.209
+ ___block_literal_global.220
+ ___block_literal_global.221
+ ___block_literal_global.231
+ ___block_literal_global.237
+ ___block_literal_global.250
+ ___block_literal_global.257
+ ___block_literal_global.259
+ ___block_literal_global.275
+ ___block_literal_global.454
+ ___block_literal_global.50
+ ___block_literal_global.559
+ ___block_literal_global.603
+ ___block_literal_global.679
+ ___block_literal_global.80
+ ___block_literal_global.95
+ ___block_literal_global.98
+ __os_signpost_emit_with_name_impl
+ __unnamed_array_storage.87
+ _classBMPublisherOptions
+ _discoverySessionFactories.factories
+ _discoverySessionFactories.onceToken
+ _getBMPublisherOptionsClass
+ _initBMPublisherOptions
+ _initBiomeLibrary
+ _kMRMediaRemoteCommandInfoSleepTimerFireDate
+ _kMRMediaRemoteCommandInfoSleepTimerStopMode
+ _kMRMediaRemoteCommandInfoSleepTimerTime
+ _kMRMediaRemoteOptionSleepTimerStopMode
+ _kMRMediaRemoteOptionSleepTimerTime
+ _objc_msgSend$App
+ _objc_msgSend$Intent
+ _objc_msgSend$commandResultWithSendError:description:
+ _objc_msgSend$createTokenWithInvitationData:equivalentMediaIdentifier:version:
+ _objc_msgSend$currentMediaUserState
+ _objc_msgSend$dictionaryDescription
+ _objc_msgSend$discoverySessionFactories
+ _objc_msgSend$eligibilityStatus
+ _objc_msgSend$eventBody
+ _objc_msgSend$exitCriticalSectionUsingRequestID:
+ _objc_msgSend$filterWithIsIncluded:
+ _objc_msgSend$groupSessionMonitor:statusDidChange:
+ _objc_msgSend$groupSessionsSupportedForAccountRegion
+ _objc_msgSend$hasAcceptedDisplayNameAcknowledgement
+ _objc_msgSend$hasAcceptedPrivacyAcknowledgement
+ _objc_msgSend$hasSleepTimerFireDate
+ _objc_msgSend$hasSleepTimerStopMode
+ _objc_msgSend$hasSleepTimerTime
+ _objc_msgSend$hasVersion
+ _objc_msgSend$identitySupportsCollaboration
+ _objc_msgSend$idsAccountIsValid
+ _objc_msgSend$initWithDetails:outputDeviceUIDs:outputDeviceGroupID:features:
+ _objc_msgSend$initWithHostInfo:invitationData:sharedSecret:sessionIdentifier:equivalentMediaIdentifier:version:
+ _objc_msgSend$initWithIdentifier:identity:connected:guest:hidden:
+ _objc_msgSend$initWithStartDate:endDate:maxEvents:lastN:reversed:
+ _objc_msgSend$invalidated
+ _objc_msgSend$isEligibleForHostingGroupSession
+ _objc_msgSend$isEligibleForJoiningGroupSession
+ _objc_msgSend$isFullSubscriber
+ _objc_msgSend$isHidden
+ _objc_msgSend$isManateeEnabled
+ _objc_msgSend$isMinor
+ _objc_msgSend$leaderDeviceInfo
+ _objc_msgSend$localParticipant
+ _objc_msgSend$matchingOutputDeviceGroupID
+ _objc_msgSend$mediaAccountHostingState
+ _objc_msgSend$mediaAccountJoiningState
+ _objc_msgSend$mediaUserStates
+ _objc_msgSend$publisherWithOptions:
+ _objc_msgSend$routeIsValidForHosting
+ _objc_msgSend$searchEndpointsForOutputDeviceUID:timeout:details:queue:completion:
+ _objc_msgSend$setByAddingObjectsFromSet:
+ _objc_msgSend$setCurrentMediaUserState:
+ _objc_msgSend$setGroupSessionsSupportedForAccountRegion:
+ _objc_msgSend$setHasAcceptedDisplayNameAcknowledgement:
+ _objc_msgSend$setHasAcceptedPrivacyAcknowledgement:
+ _objc_msgSend$setIdentitySupportsCollaboration:
+ _objc_msgSend$setIdsAccountIsValid:
+ _objc_msgSend$setInvalidated:
+ _objc_msgSend$setIsEligibleForHostingGroupSession:
+ _objc_msgSend$setIsEligibleForJoiningGroupSession:
+ _objc_msgSend$setIsFullSubscriber:
+ _objc_msgSend$setIsManateeEnabled:
+ _objc_msgSend$setIsMinor:
+ _objc_msgSend$setLeaderDeviceInfo:
+ _objc_msgSend$setMediaAccountHostingState:
+ _objc_msgSend$setMediaAccountJoiningState:
+ _objc_msgSend$setMediaUserStates:
+ _objc_msgSend$setRouteIsValidForHosting:
+ _objc_msgSend$setShouldWaitForUnanimousEndpoints:
+ _objc_msgSend$setSleepTimerFireDate:
+ _objc_msgSend$setSleepTimerStopMode:
+ _objc_msgSend$setSleepTimerTime:
+ _objc_msgSend$setStorefrontCountryCode:
+ _objc_msgSend$setUserIdentity:
+ _objc_msgSend$shouldWaitForUnanimousEndpoints
+ _objc_msgSend$sinkWithCompletion:shouldContinue:
+ _objc_msgSend$sleepTimerFireDate
+ _objc_msgSend$sleepTimerStopMode
+ _objc_msgSend$sleepTimerTime
+ _objc_msgSend$startGroupSessionsForAllRouteSubtypes
+ _objc_msgSend$storefrontCountryCode
+ _objc_msgSend$supportCriticalSectionManagement
+ _objc_msgSend$supportGroupSessionHomePodBoop
+ _objc_msgSend$updateGroupSessionEligibility:
+ _objc_msgSend$userIdentity
+ _os_signpost_enabled
+ _softLinkBiomeLibrary
- -[MRAVLocalEndpoint handleLocalGroupSessionDidChangeNotification:]
- -[MRCodableGroupSessionParticipant initWithIdentifier:identity:]
- -[MRDistantExternalDevice _hack_publishLocalGroupSessionChange:]
- -[MRGroupSessionToken initWithHostInfo:invitationData:]
- -[MRGroupSessionToken initWithHostInfo:invitationData:sharedSecret:sessionIdentifier:equivalentMediaIdentifier:]
- -[MRMediaRemoteService createTokenWithInvitationData:equivalentMediaIdentifier:]
- -[MRMediaSuggestionController _applicationSupportsMediaSuggestions:]
- -[MRMediaSuggestionController _notifyDelegateOfError:]
- -[MRMediaSuggestionController _notifyDelegateOfUpdatedSuggestions]
- -[MRMediaSuggestionController _onQueue_registerObservers]
- -[MRMediaSuggestionController _onQueue_unregisterObservers]
- -[MRMediaSuggestionController _onQueue_updateForMediaSuggestionWithCoreDuetIdentifier:]
- -[MRMediaSuggestionController _originatedFromSystemMediaApp:]
- -[MRMediaSuggestionController _reloadWithReason:]
- -[MRMediaSuggestionController applicationsDidInstall:]
- -[MRMediaSuggestionController applicationsDidUninstall:]
- -[MRMediaSuggestionController dealloc]
- -[MRMediaSuggestionController setInternalSuggestions:]
- -[MRMediaSuggestionRequest _queryEventsFromStore:withPredicate:offset:error:]
- -[MRMediaSuggestionRequest performWithUUID:completion:]
- -[MRMediaSuggestionRequest performWithUUID:completion:].cold.1
- -[MRNotificationServiceClient _handleLocalGroupSessionInfoDidChangeNotification:]
- -[MRRemoteControlGroupSession shouldOmitHost]
- -[MRRequestDetails date]
- GCC_except_table104
- GCC_except_table112
- GCC_except_table117
- GCC_except_table120
- GCC_except_table121
- GCC_except_table193
- GCC_except_table204
- GCC_except_table205
- GCC_except_table257
- GCC_except_table283
- GCC_except_table53
- GCC_except_table75
- _CoreDuetContextLibrary.sLib
- _CoreDuetContextLibrary.sOnce
- _CoreDuetLibrary.sLib
- _CoreDuetLibrary.sOnce
- _MRCreateDistantEndpointFromXPCMessage
- _OBJC_CLASS_$_LSApplicationWorkspace
- _OBJC_CLASS_$_NSCompoundPredicate
- _OBJC_IVAR_$_MRAVReconnaissanceSession._callback
- _OBJC_IVAR_$_MRGroupSessionToken._effectiveIdentifier
- _OBJC_IVAR_$_MRMediaSuggestionController._changeRegistration
- _OBJC_IVAR_$_MRMediaSuggestionController._clientContext
- _OBJC_IVAR_$_MRMediaSuggestionController._delegateQueue
- _OBJC_IVAR_$_MRMediaSuggestionController._internalSuggestions
- _OBJC_IVAR_$_MRMediaSuggestionController._preferences
- _OBJC_IVAR_$_MRMediaSuggestionController._queue
- _OBJC_IVAR_$_MRMediaSuggestionController._registeredForChanges
- _OBJC_IVAR_$_MRRequestDetails._date
- __CDClientContextFunction
- __CDContextQueriesFunction
- __CDContextualChangeRegistrationFunction
- __CDContextualPredicateFunction
- __DKEventQueryFunction
- __DKIntentMetadataKeyFunction
- __DKKnowledgeStoreFunction
- __DKQueryFunction
- __DKSystemEventStreamsFunction
- __NSIsNSDictionary
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_LSApplicationWorkspaceObserverProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_LSApplicationWorkspaceObserverProtocol
- __OBJC_$_PROTOCOL_REFS_LSApplicationWorkspaceObserverProtocol
- __OBJC_CLASS_PROTOCOLS_$_MRMediaSuggestionController
- __OBJC_LABEL_PROTOCOL_$_LSApplicationWorkspaceObserverProtocol
- __OBJC_PROTOCOL_$_LSApplicationWorkspaceObserverProtocol
- ___103-[MRAVLightweightReconnaissanceSession searchEndpointsForCompanionWithTimeout:reason:queue:completion:]_block_invoke.97
- ___104-[MRAVLightweightReconnaissanceSession searchForLogicalOutputDeviceUID:timeout:reason:queue:completion:]_block_invoke.118
- ___105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke.529
- ___105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke.531
- ___105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke.536
- ___105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke.545
- ___105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke_2.532
- ___106-[MRAVLightweightReconnaissanceSession searchEndpointsForOutputDeviceUID:timeout:reason:queue:completion:]_block_invoke
- ___106-[MRAVLightweightReconnaissanceSession searchEndpointsForOutputDeviceUID:timeout:reason:queue:completion:]_block_invoke.18
- ___106-[MRAVLightweightReconnaissanceSession searchEndpointsForOutputDeviceUID:timeout:reason:queue:completion:]_block_invoke.40
- ___106-[MRAVLightweightReconnaissanceSession searchEndpointsForOutputDeviceUID:timeout:reason:queue:completion:]_block_invoke.63
- ___106-[MRAVLightweightReconnaissanceSession searchEndpointsForOutputDeviceUID:timeout:reason:queue:completion:]_block_invoke.69
- ___106-[MRAVLightweightReconnaissanceSession searchEndpointsForOutputDeviceUID:timeout:reason:queue:completion:]_block_invoke.cold.1
- ___106-[MRAVLightweightReconnaissanceSession searchEndpointsForOutputDeviceUID:timeout:reason:queue:completion:]_block_invoke_2
- ___106-[MRAVLightweightReconnaissanceSession searchEndpointsForOutputDeviceUID:timeout:reason:queue:completion:]_block_invoke_3
- ___106-[MRAVLightweightReconnaissanceSession searchForOutputDevices:categories:timeout:reason:queue:completion:]_block_invoke.153
- ___106-[MRAVLightweightReconnaissanceSession searchForOutputDevices:categories:timeout:reason:queue:completion:]_block_invoke.163
- ___107-[MRAVLightweightReconnaissanceSession searchEndpointsForMyGroupLeaderWithTimeout:reason:queue:completion:]_block_invoke.134
- ___108-[MRAVLightweightReconnaissanceSession searchEndpointsForRoutingContextUID:timeout:reason:queue:completion:]_block_invoke.130
- ___112-[MRAVLightweightReconnaissanceSession searchEndpointsForLeaderOutputDeviceUID:timeout:reason:queue:completion:]_block_invoke.101
- ___122-[MRAVEndpoint willStartingPlaybackToOutputDevicesInterruptPlayback:originatingOutputDeviceUID:duration:queue:completion:]_block_invoke.508
- ___122-[MRAVEndpoint willStartingPlaybackToOutputDevicesInterruptPlayback:originatingOutputDeviceUID:duration:queue:completion:]_block_invoke.518
- ___122-[MRDistantExternalDevice _onSerialQueue_prepareToConnectWithOptions:userInfo:connectionAttemptDetails:connectionHandler:]_block_invoke.280
- ___122-[MRDistantExternalDevice _onSerialQueue_prepareToConnectWithOptions:userInfo:connectionAttemptDetails:connectionHandler:]_block_invoke_2.281
- ___25-[MRMediaControls _reset]_block_invoke.68
- ___31-[MRUIController xpcConnection]_block_invoke.134
- ___35-[MRMediaSuggestionController stop]_block_invoke
- ___36+[MRIRRoute routeWithOutputDevices:]_block_invoke.106
- ___37-[MRDistantExternalDevice deviceInfo]_block_invoke.223
- ___37-[MRDistantExternalDevice deviceInfo]_block_invoke_2.224
- ___38-[MRMediaSuggestionController dealloc]_block_invoke
- ___39-[MRDistantExternalDevice customOrigin]_block_invoke.227
- ___39-[MRDistantExternalDevice customOrigin]_block_invoke_2.229
- ___42-[MRMediaSuggestionController suggestions]_block_invoke
- ___44-[MRDistantExternalDevice groupSessionToken]_block_invoke.221
- ___47-[MROutputContextController _inititalizeVolume]_block_invoke.258
- ___47-[MROutputContextController _inititalizeVolume]_block_invoke.260
- ___48-[MRDistantExternalDevice externalOutputContext]_block_invoke.218
- ___48-[MRDistantExternalDevice personalOutputDevices]_block_invoke.298
- ___49-[MRMediaSuggestionController _reloadWithReason:]_block_invoke
- ___49-[MRMediaSuggestionController _reloadWithReason:]_block_invoke_2
- ___49-[MRMediaSuggestionController _reloadWithReason:]_block_invoke_3
- ___54-[MRMediaSuggestionController _notifyDelegateOfError:]_block_invoke
- ___54-[MRMediaSuggestionController applicationsDidInstall:]_block_invoke
- ___54-[MRRemoteControlGroupSession session:didChangeState:]_block_invoke.338
- ___55-[MRAVDistantRoutingDiscoverySession setDiscoveryMode:]_block_invoke.75
- ___55-[MRAVReconnaissanceSession _onQueue_processSearchLoop]_block_invoke.26
- ___55-[MRAVReconnaissanceSession _onQueue_processSearchLoop]_block_invoke.29
- ___55-[MRMediaSuggestionRequest performWithUUID:completion:]_block_invoke
- ___55-[MRMediaSuggestionRequest performWithUUID:completion:]_block_invoke.cold.1
- ___56-[MRMediaSuggestionController applicationsDidUninstall:]_block_invoke
- ___56-[MRRemoteControlGroupSession session:didUpdateMembers:]_block_invoke.341
- ___57-[MRMediaSuggestionController _onQueue_registerObservers]_block_invoke
- ___57-[MRMediaSuggestionController _onQueue_registerObservers]_block_invoke.19
- ___57-[MRMediaSuggestionController _onQueue_registerObservers]_block_invoke.21
- ___58-[MRV2NowPlayingController _configureReloadTimerForError:]_block_invoke.190
- ___60-[MRAVDistantRoutingDiscoverySession devicePresenceDetected]_block_invoke.77
- ___60-[MRAVDistantRoutingDiscoverySession devicePresenceDetected]_block_invoke.77.cold.1
- ___60-[MRRemoteControlGroupSession removeParticipant:completion:]_block_invoke.327
- ___60-[MRRemoteControlGroupSession removeParticipant:completion:]_block_invoke.327.cold.1
- ___60-[MRRemoteControlGroupSession removeParticipant:completion:]_block_invoke.328
- ___61-[MRRemoteControlGroupSession session:didUpdateParticipants:]_block_invoke.339
- ___62-[MRRemoteControlGroupSession session:didInvalidateWithError:]_block_invoke.345
- ___65-[MRDistantExternalDevice hostedExternalDeviceEndpointDidChange:]_block_invoke.302
- ___65-[MRRemoteControlGroupSession denyPendingParticipant:completion:]_block_invoke.318
- ___65-[MRRemoteControlGroupSession denyPendingParticipant:completion:]_block_invoke.318.cold.1
- ___65-[MRRemoteControlGroupSession denyPendingParticipant:completion:]_block_invoke.319
- ___66-[MRAVReconnaissanceSession beginSearchWithTimeout:mapCompletion:]_block_invoke.20
- ___66-[MRDistantExternalDevice connectWithOptions:userInfo:completion:]_block_invoke.264
- ___66-[MRDistantExternalDevice hostedExternalDeviceDidAddOutputDevice:]_block_invoke.307
- ___66-[MRMediaSuggestionController _notifyDelegateOfUpdatedSuggestions]_block_invoke
- ___67+[MRAVEndpoint directEndpointForOutputDeviceUIDs:queue:completion:]_block_invoke.481
- ___67+[MRAVEndpoint hostedEndpointForOutputDeviceUIDs:queue:completion:]_block_invoke.474
- ___67-[MRDistantExternalDevice hostedExternalDeviceDeviceInfoDidChange:]_block_invoke.300
- ___67-[MRRemoteControlGroupSession assertSessionManagementScreenVisible]_block_invoke.323
- ___67-[MRRemoteControlGroupSession assertSessionManagementScreenVisible]_block_invoke.326
- ___67-[MRRemoteControlGroupSession assertSessionManagementScreenVisible]_block_invoke.326.cold.1
- ___67-[MRRemoteControlGroupSession assertSessionManagementScreenVisible]_block_invoke_2
- ___67-[MRRemoteControlGroupSession assertSessionManagementScreenVisible]_block_invoke_2.cold.1
- ___68-[MRRemoteControlGroupSession approvePendingParticipant:completion:]_block_invoke.312
- ___68-[MRRemoteControlGroupSession approvePendingParticipant:completion:]_block_invoke.312.cold.1
- ___68-[MRRemoteControlGroupSession approvePendingParticipant:completion:]_block_invoke.314
- ___68-[MRRemoteControlGroupSession session:didUpdatePendingParticipants:]_block_invoke.340
- ___68-[MRV2NowPlayingController _handlePlaybackQueueChangedNotification:]_block_invoke.141
- ___69-[MRDistantExternalDevice hostedExternalDeviceDidChangeOutputDevice:]_block_invoke.308
- ___69-[MRDistantExternalDevice hostedExternalDeviceDidRemoveOutputDevice:]_block_invoke.309
- ___69-[MRRemoteControlGroupSession session:didUpdateSynchronizedMetadata:]_block_invoke.344
- ___70-[MRMediaSuggestionRequest performWithPreferences:options:completion:]_block_invoke.97
- ___70-[MRMediaSuggestionRequest performWithPreferences:options:completion:]_block_invoke.97.cold.1
- ___70-[MRMediaSuggestionRequest performWithPreferences:options:completion:]_block_invoke.99
- ___72-[MRAVDistantRoutingDiscoverySession setHostedRoutingSessionConnection:]_block_invoke.79
- ___72-[MRAVDistantRoutingDiscoverySession setHostedRoutingSessionConnection:]_block_invoke_2.81
- ___72-[MRV2NowPlayingController _handleSupportedCommandsChangedNotification:]_block_invoke.146
- ___74-[MRDistantExternalDevice hostedExternalDeviceGroupSessionTokenDidChange:]_block_invoke.310
- ___76+[MRAVEndpoint createEndpointWithOutputDeviceUIDs:options:queue:completion:]_block_invoke.488
- ___76+[MRAVEndpoint createEndpointWithOutputDeviceUIDs:options:queue:completion:]_block_invoke.492
- ___77-[MRDistantExternalDevice hostedExternalDeviceDidReceiveCustomData:withName:]_block_invoke.301
- ___79-[MRDistantExternalDevice hostedExternalDeviceVolumeDidChange:forOutputDevice:]_block_invoke.305
- ___80-[MRDistantExternalDevice hostedExternalDeviceIsMutedDidChange:forOutputDevice:]_block_invoke.306
- ___81-[MRV2NowPlayingController _resolveForUnresolvedPlayerPath:requestID:completion:]_block_invoke.104
- ___81-[MRV2NowPlayingController _resolveForUnresolvedPlayerPath:requestID:completion:]_block_invoke.105
- ___81-[MRV2NowPlayingController _resolveForUnresolvedPlayerPath:requestID:completion:]_block_invoke.105.cold.1
- ___83-[MRAVReconnaissanceSession initWithOutputDeviceUIDs:outputDeviceGroupID:features:]_block_invoke
- ___83-[MRAVReconnaissanceSession initWithOutputDeviceUIDs:outputDeviceGroupID:features:]_block_invoke_2
- ___83-[MRAVReconnaissanceSession initWithOutputDeviceUIDs:outputDeviceGroupID:features:]_block_invoke_3
- ___83-[MRAVReconnaissanceSession initWithOutputDeviceUIDs:outputDeviceGroupID:features:]_block_invoke_4
- ___83-[MRAVReconnaissanceSession initWithOutputDeviceUIDs:outputDeviceGroupID:features:]_block_invoke_5
- ___83-[MRAVReconnaissanceSession initWithOutputDeviceUIDs:outputDeviceGroupID:features:]_block_invoke_6
- ___83-[MRV2NowPlayingController _resolveForEndpoint:client:player:requestID:completion:]_block_invoke.96
- ___83-[MRV2NowPlayingController _resolveForEndpoint:client:player:requestID:completion:]_block_invoke.97
- ___83-[MRV2NowPlayingController _resolveForEndpoint:client:player:requestID:completion:]_block_invoke.97.cold.1
- ___87-[MRMediaSuggestionController _onQueue_updateForMediaSuggestionWithCoreDuetIdentifier:]_block_invoke
- ___87-[MRMediaSuggestionController _onQueue_updateForMediaSuggestionWithCoreDuetIdentifier:]_block_invoke_2
- ___90-[MRDistantExternalDevice setOutputDeviceVolume:outputDeviceUID:details:queue:completion:]_block_invoke.287
- ___90-[MRV2NowPlayingController _resolveForOutputDeviceUID:client:player:requestID:completion:]_block_invoke.87
- ___90-[MRV2NowPlayingController _resolveForOutputDeviceUID:client:player:requestID:completion:]_block_invoke.87.cold.1
- ___91-[MRDistantExternalDevice hostedExternalDeviceVolumeCapabilitiesDidChange:forOutputDevice:]_block_invoke.304
- ___91-[MRDistantExternalDevice muteOutputDeviceVolume:outputDeviceUID:details:queue:completion:]_block_invoke.296
- ___91-[MRV2NowPlayingController _loadNowPlayingStateForResolvedPlayerPath:requestID:completion:]_block_invoke.112
- ___91-[MRV2NowPlayingController _loadNowPlayingStateForResolvedPlayerPath:requestID:completion:]_block_invoke.112.cold.1
- ___91-[MRV2NowPlayingController _loadNowPlayingStateForResolvedPlayerPath:requestID:completion:]_block_invoke.113
- ___91-[MRV2NowPlayingController _resolveForOutputContextUID:client:player:requestID:completion:]_block_invoke.92
- ___91-[MRV2NowPlayingController _resolveForOutputContextUID:client:player:requestID:completion:]_block_invoke.92.cold.1
- ___92-[MRAVLightweightReconnaissanceSession searchOutputDevices:reason:timeout:queue:completion:]_block_invoke.142
- ___93-[MRDistantExternalDevice adjustOutputDeviceVolume:outputDeviceUID:details:queue:completion:]_block_invoke.292
- ___97-[MRAVLightweightReconnaissanceSession searchForOutputDeviceUID:timeout:reason:queue:completion:]_block_invoke.108
- ___97-[MRAVLightweightReconnaissanceSession searchForOutputDeviceUID:timeout:reason:queue:completion:]_block_invoke.110
- ___97-[MRAVLightweightReconnaissanceSession searchForOutputDeviceUID:timeout:reason:queue:completion:]_block_invoke.114
- ___99-[MRAVLightweightReconnaissanceSession searchEndpointsForGroupUID:timeout:reason:queue:completion:]_block_invoke.86
- ___99-[MRAVLightweightReconnaissanceSession searchEndpointsForGroupUID:timeout:reason:queue:completion:]_block_invoke.93
- ___CoreDuetContextLibrary_block_invoke
- ___CoreDuetLibrary_block_invoke
- ___MRCreateDecodedUserInfo_block_invoke.103
- ___MRCreateDecodedUserInfo_block_invoke.94
- ___MRCreateDecodedUserInfo_block_invoke_2.108
- ___MRCreateDecodedUserInfo_block_invoke_2.97
- ___MRCreateDecodedUserInfo_block_invoke_3.100
- ___MRCreateDecodedUserInfo_block_invoke_3.111
- ___MRCreateDecodedUserInfo_block_invoke_4.114
- ___MRCreateDecodedUserInfo_block_invoke_5.117
- ___MRCreateDecodedUserInfo_block_invoke_7
- ___MRCreateEncodedUserInfo_block_invoke.145
- ___MRCreateEncodedUserInfo_block_invoke_10.cold.1
- ___MRCreateEncodedUserInfo_block_invoke_2.149
- ___MRCreateEncodedUserInfo_block_invoke_3.152
- ___MRCreateEncodedUserInfo_block_invoke_4.156
- ___MRCreateEncodedUserInfo_block_invoke_5.160
- ___MRCreateEncodedUserInfo_block_invoke_6.164
- ___MRGroupSessionJoinSessionWithToken_block_invoke.267
- ___MRGroupSessionJoinSessionWithToken_block_invoke.271
- ___MRMediaRemoteGetClientProperties_block_invoke.524
- ___MRMediaRemoteGetPlaybackStateForPlayer_block_invoke.564
- ___MRMediaRemoteGetPlayerProperties_block_invoke.555
- ___MRMediaRemoteNowPlayingResolvePlayerPathWithID_block_invoke.81
- ___MRMediaRemoteNowPlayingResolvePlayerPathWithID_block_invoke.96
- ___MRMediaRemoteSetPlaybackStateForPlayerWithTimestamp_block_invoke.582
- ___MRNowPlayingSessionManagerStartSession_block_invoke.50
- ___MRNowPlayingSessionManagerStartSession_block_invoke.63
- ___MRNowPlayingSessionManagerStartSession_block_invoke.67
- ___MRServiceClientRemotePlayerPathCommandCallback_block_invoke.94
- ____MRServiceClientRemoteResolvedPlayerPathCommandCallback_block_invoke.71
- ____MRServiceClientRemoteResolvedPlayerPathCommandCallback_block_invoke.71.cold.1
- ____MRServiceClientRemoteResolvedPlayerPathCommandCallback_block_invoke.71.cold.2
- ____MRServiceClientRemoteResolvedPlayerPathCommandCallback_block_invoke.72
- ____MRServiceClientRemoteResolvedPlayerPathCommandCallback_block_invoke_2.73
- ___block_descriptor_104_e8_32s40s48s56s64bs72r80r88r_e34_v24?0"MRDeviceInfo"8"NSError"16lr72l8s32l8s40l8s48l8s56l8s64l8r80l8r88l8
- ___block_descriptor_104_e8_32s40s48s56s64s72s80s88s96bs_e34_v24?0"MRAVEndpoint"8"NSError"16ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
- ___block_descriptor_40_e8_32s_e39_v24?0"MRMediaSuggestion"8"NSError"16ls32l8
- ___block_descriptor_40_e8_32w_e35_v24?0"NSString"8"NSDictionary"16lw32l8
- ___block_descriptor_48_e8_32s40bs_e31_v24?0"MRArtwork"8"NSError"16ls32l8s40l8
- ___block_descriptor_48_e8_32s_e25_v16?0"MRCommandResult"8ls32l8
- ___block_descriptor_60_e8_32s40s48bs_e25_v16?0"MRCommandResult"8ls32l8s40l8s48l8
- ___block_descriptor_68_e8_32s40s48bs_e17_v16?0"NSError"8ls32l8s40l8s48l8
- ___block_descriptor_68_e8_32s40s48s56r_e5_v8?0ls32l8s40l8s48l8r56l8
- ___block_descriptor_80_e8_32s40s48s56s64bs72r_e25_v16?0"MRCommandResult"8lr72l8s32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_80_e8_32s40s48s56s64bs72r_e42_v32?0"NSArray"8"NSString"16"NSError"24lr72l8s32l8s40l8s48l8s64l8s56l8
- ___block_descriptor_84_e8_32s40s48s56s64bs72bs_e5_v8?0ls64l8s32l8s40l8s48l8s56l8s72l8
- ___block_descriptor_88_e8_32s40s48s56s64s72bs80r_e25_v16?0"MRCommandResult"8lr80l8s32l8s40l8s48l8s56l8s64l8s72l8
- ___block_literal_global.102
- ___block_literal_global.109
- ___block_literal_global.111
- ___block_literal_global.113
- ___block_literal_global.124
- ___block_literal_global.131
- ___block_literal_global.136
- ___block_literal_global.138
- ___block_literal_global.146
- ___block_literal_global.155
- ___block_literal_global.159
- ___block_literal_global.164
- ___block_literal_global.167
- ___block_literal_global.171
- ___block_literal_global.174
- ___block_literal_global.202
- ___block_literal_global.205
- ___block_literal_global.207
- ___block_literal_global.214
- ___block_literal_global.216
- ___block_literal_global.219
- ___block_literal_global.236
- ___block_literal_global.243
- ___block_literal_global.253
- ___block_literal_global.255
- ___block_literal_global.274
- ___block_literal_global.441
- ___block_literal_global.5
- ___block_literal_global.528
- ___block_literal_global.56
- ___block_literal_global.604
- ___block_literal_global.677
- ___block_literal_global.76
- ___block_literal_global.96
- ___block_literal_global.99
- _class_CDClientContext
- _class_CDContextQueries
- _class_CDContextualChangeRegistration
- _class_CDContextualPredicate
- _class_DKEventQuery
- _class_DKIntentMetadataKey
- _class_DKKnowledgeStore
- _class_DKQuery
- _class_DKSystemEventStreams
- _get_CDClientContextClass
- _get_CDContextQueriesClass
- _get_CDContextualChangeRegistrationClass
- _get_CDContextualPredicateClass
- _get_DKEventQueryClass
- _get_DKIntentMetadataKeyClass
- _get_DKKnowledgeStoreClass
- _get_DKQueryClass
- _get_DKSystemEventStreamsClass
- _init_CDClientContext
- _init_CDContextQueries
- _init_CDContextualChangeRegistration
- _init_CDContextualPredicate
- _init_DKEventQuery
- _init_DKIntentMetadataKey
- _init_DKKnowledgeStore
- _init_DKQuery
- _init_DKSystemEventStreams
- _objc_msgSend$_parameterCombinationsForClassName:
- _objc_msgSend$addObserver:
- _objc_msgSend$andPredicateWithSubpredicates:
- _objc_msgSend$appIntentsStream
- _objc_msgSend$controller:didUpdateSuggestions:
- _objc_msgSend$createTokenWithInvitationData:equivalentMediaIdentifier:
- _objc_msgSend$defaultWorkspace
- _objc_msgSend$deregisterCallback:
- _objc_msgSend$eventQueryWithPredicate:eventStreams:offset:limit:sortDescriptors:
- _objc_msgSend$executeQuery:error:
- _objc_msgSend$initWithDictionary:copyItems:
- _objc_msgSend$initWithHostInfo:invitationData:sharedSecret:sessionIdentifier:equivalentMediaIdentifier:
- _objc_msgSend$insertObject:atIndex:
- _objc_msgSend$intentClassKey
- _objc_msgSend$intentDKObjUUIDKey
- _objc_msgSend$intentSourceBundleIDKey
- _objc_msgSend$keyPathForIntentsDataDictionary
- _objc_msgSend$knowledgeStore
- _objc_msgSend$knowledgeStoreWithDirectReadOnlyAccess
- _objc_msgSend$localWakingRegistrationWithIdentifier:contextualPredicate:clientIdentifier:callback:
- _objc_msgSend$notPredicateWithSubpredicate:
- _objc_msgSend$orPredicateWithSubpredicates:
- _objc_msgSend$predicateForEventsWithBundleID:
- _objc_msgSend$predicateForKeyPath:withPredicate:
- _objc_msgSend$predicateForObjectWithUUID:
- _objc_msgSend$predicateForObjectsWithMetadataKey:andStringValue:
- _objc_msgSend$predicateWithFormat:
- _objc_msgSend$predicateWithValue:
- _objc_msgSend$registerCallback:
- _objc_msgSend$setExecuteConcurrently:
- _objc_msgSend$setGuest:
- _objc_msgSend$setUserDisplayPreferencesDidChangeCallback:
- _objc_msgSend$shouldOmitHost
- _objc_msgSend$source
- _objc_msgSend$startDateSortDescriptorAscending:
- _objc_msgSend$suggestions
- _objc_msgSend$suggestionsDisabledInContext:
- _objc_msgSend$supportProactiveSuggestion
- _objc_msgSend$userContext
CStrings:
+ "\x02#\x13"
+ "\x13\x1d\x12"
+ "\x18\x12\x15\x13\x13\x12\x16"
+ "!self.completion"
+ "%@-%lf"
+ "%@<%@>:%@ UserInitiated=%u, qos=%u"
+ ", currentMediaUserState=%@"
+ ", displayNameAck=%d"
+ ", eligibleForJoining=%d"
+ ", fullSub=%d"
+ ", idsAccountValid=%d"
+ ", manatee=%d"
+ ", mediaAccountHostingState=%@"
+ ", mediaAccountJoiningState=%@"
+ ", mediaUserStates=%@"
+ ", min=%d"
+ ", privacyAck=%d"
+ ", routeType=%d"
+ ", routeValidForHosting=%d"
+ ", storefront=%@"
+ ", supportedRegion=%d"
+ ", supportsCollab=%d"
+ ", userIdentity=%@"
+ ", version=%@"
+ "/System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary"
+ "/System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams"
+ "<%@: "
+ "<%@: bundles=%@, contexts=%@>"
+ "<%@: identifier=%@, identity=%@, local=%@, pending=%@, connected=%@, guest=%@, hidden=%@>"
+ "@\"MRGroupSessionEligibilityStatus\""
+ "@\"MRMediaUserState\""
+ "@44@0:8@16@24@32I40"
+ "@44@0:8@16@24B32B36B40"
+ "@64@0:8@16@24@32@40@48@56"
+ "App"
+ "ApplicationTerminated"
+ "B16@?0@\"BMStoreEvent\"8"
+ "BMPublisherOptions"
+ "BiomeLibrary"
+ "Cache Miss: Request: %{public}@<%{public}@> for %@ %@"
+ "Changed from nil"
+ "Changed to nil"
+ "ChapterEnd"
+ "Completion was not called for originCommandHandler=%@<%@>"
+ "DontPause/"
+ "Endpoint.modifyTopologyWithRequest<%@> %@"
+ "Endpoint.waitForPlaybackWithTimeout"
+ "FadeAudio/"
+ "GROUPSESSION_ROUTE_HOMEPOD_MINI"
+ "GroupSessionRouteTypeHomePodMini"
+ "HomePodMini"
+ "Indeterminate"
+ "Intent"
+ "ItemEnd"
+ "MRActiveGroupSessionInfoDidChangeNotification"
+ "MRActiveGroupSessionInfoUserInfoKey"
+ "MRCriticalSectionCoordinator"
+ "MRCriticalSectionToken"
+ "MRCriticalSectionTransitionNotification"
+ "MRGroupSessionEligibilityDidChangeNotification"
+ "MRGroupSessionEligibilityMonitor"
+ "MRGroupSessionEligibilityStatus"
+ "MRGroupSessionEligibilityStatusUserInfoKey"
+ "MRGroupSessionToken * _Nonnull MRGroupSessionTokenCreateWithInvitationData(NSData *__strong _Nonnull, NSString * _Nullable __strong, NSNumber *__strong _Nonnull)"
+ "MRMediaUserState"
+ "MRXPC_CRITICAL_SECTION_IDENTIFIER_KEY"
+ "MRXPC_CRITICAL_SECTION_TRANSITION_KEY"
+ "MRXPC_GROUP_SESSION_VERSION_KEY"
+ "MRXPC_REQUEST_DETAILS"
+ "MuteUntilFinished"
+ "Not attempting to migrate because endpoint is migration-restricted group session endpoint"
+ "Operation was manually canceled via a explict call to CancelSearch"
+ "OutputContext claims supportsVolumeControl for local device: %@ %@"
+ "Proactive endpoint is QHO-restricted group session endpoint."
+ "ReconSession"
+ "ReconnaissanceSession.search"
+ "RemoteRemoveAllRequest"
+ "SendCommandOrigin"
+ "SendCommandPlayer"
+ "SendCommandPlayerMain"
+ "SendCommandWithResult"
+ "SendCommandXPCResultFromApp"
+ "SendCommandXPCResultFromDaemon"
+ "SendCommandXPCToApp"
+ "SendCommandXPCToDaemon"
+ "StringAsSleepTimerStopMode:"
+ "SuppressErrorDialog/"
+ "T@\"MRDeviceInfo\",&,N"
+ "T@\"MRDeviceInfo\",C,N,V_leaderDeviceInfo"
+ "T@\"MRGroupSessionEligibilityStatus\",&,N,V_eligibilityStatus"
+ "T@\"MRGroupSessionEligibilityStatus\",R,N,V_status"
+ "T@\"MRMediaUserState\",&,N,V_currentMediaUserState"
+ "T@\"MRRequestDetails\",R,N,V_details"
+ "T@\"MRUserIdentity\",&,N,V_userIdentity"
+ "T@\"NSArray\",&,N,V_mediaUserStates"
+ "T@\"NSDictionary\",R,N,V_suggestions"
+ "T@\"NSHashTable\",&,N,V_observers"
+ "T@\"NSMutableArray\",R,N"
+ "T@\"NSNumber\",R,N,V_version"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSUUID\",R,N,V_requestID"
+ "T@\"_MRDeviceInfoMessageProtobuf\",&,N,V_deviceInfo"
+ "T@\"_MRDeviceInfoMessageProtobuf\",&,N,V_leaderDeviceInfo"
+ "TB,N,GisHidden,V_hidden"
+ "TB,N,V_groupSessionsSupportedForAccountRegion"
+ "TB,N,V_hasAcceptedDisplayNameAcknowledgement"
+ "TB,N,V_hasAcceptedPrivacyAcknowledgement"
+ "TB,N,V_hidden"
+ "TB,N,V_identitySupportsCollaboration"
+ "TB,N,V_idsAccountIsValid"
+ "TB,N,V_invalidated"
+ "TB,N,V_isEligibleForHostingGroupSession"
+ "TB,N,V_isEligibleForJoiningGroupSession"
+ "TB,N,V_isFullSubscriber"
+ "TB,N,V_isManateeEnabled"
+ "TB,N,V_isMinor"
+ "TB,N,V_routeIsValidForHosting"
+ "TB,N,V_shouldWaitForUnanimousEndpoints"
+ "TB,R,N,GisHidden"
+ "TI,N,V_version"
+ "TQ,N,V_mediaAccountHostingState"
+ "TQ,N,V_mediaAccountJoiningState"
+ "Td,N,V_sleepTimerFireDate"
+ "Td,N,V_sleepTimerTime"
+ "Ti,N,V_sleepTimerStopMode"
+ "Time"
+ "T{os_unfair_lock_s=I},N,V_lock"
+ "Valid"
+ "WaveformNonVariableFramerate"
+ "[MRGroupSessionRequestManager] Updating group session eligibility: %@"
+ "[MRGroupSession] Failed to leave session with error: %@"
+ "[MRGroupSession] Requesting to join session with token: %@"
+ "[MRGroupSession] Requesting to leave session with identifier: %@"
+ "[MRMediaSuggestionRequest] Performing preference-respecting request %{public}@ with preferences %@, options: %@."
+ "[MRNowPlaying] MRMediaRemoteSetCanBeNowPlayingApplication set to %@"
+ "[MRSerializationUtility] unarchive failed with error: %@"
+ "_MRAirPlayLeaderInfoProtobuf"
+ "_MRGroupSessionEligibilityDidChangeNotification"
+ "_MRGroupSessionEligibilityStatusDataUserInfoKey"
+ "_currentMediaUserState"
+ "_eligibilityStatus"
+ "_groupSessionsSupportedForAccountRegion"
+ "_handleActiveGroupSessionDidChangeNotification:"
+ "_handleActiveGroupSessionInfoDidChangeNotification:"
+ "_handleLocalGroupSessionEligibilityDidChangeNotification:"
+ "_hasAcceptedDisplayNameAcknowledgement"
+ "_hasAcceptedPrivacyAcknowledgement"
+ "_hidden"
+ "_identitySupportsCollaboration"
+ "_idsAccountIsValid"
+ "_isEligibleForHostingGroupSession"
+ "_isEligibleForJoiningGroupSession"
+ "_isFullSubscriber"
+ "_isManateeEnabled"
+ "_isMinor"
+ "_leaderDeviceInfo"
+ "_mediaAccountHostingState"
+ "_mediaAccountJoiningState"
+ "_mediaUserStates"
+ "_onQueue_beginSearchWithTimeout:"
+ "_onQueue_endSearch"
+ "_routeIsValidForHosting"
+ "_sleepTimerFireDate"
+ "_sleepTimerStopMode"
+ "_sleepTimerTime"
+ "_suggestions"
+ "_userIdentity"
+ "acv"
+ "canHandleJoinRequests"
+ "canManageParticipants"
+ "cilantro_cta"
+ "cmus"
+ "col"
+ "color"
+ "createTokenWithInvitationData:equivalentMediaIdentifier:version:"
+ "critical section management is disabled. dropping message"
+ "currentMediaUserState"
+ "dictionaryDescription"
+ "differenceFrom:"
+ "discoverySessionFactories"
+ "dsn"
+ "ehgs"
+ "ejgS"
+ "eligibilityStatus"
+ "eligibleForHosting=%d"
+ "enterCriticalSection"
+ "eventBody"
+ "exitCriticalSection:"
+ "exitCriticalSectionUsingRequestID:"
+ "failed to enter critical section. error: %@"
+ "failed to exit critical section for requestID: %@. error: %@"
+ "filterWithIsIncluded:"
+ "groupSessionMonitor:statusDidChange:"
+ "groupSessionsSupportedForAccountRegion"
+ "handleActiveGroupSessionDidChangeNotification:"
+ "hasAcceptedDisplayNameAcknowledgement"
+ "hasAcceptedPrivacyAcknowledgement"
+ "hasDeviceInfo"
+ "hasHidden"
+ "hasLeaderDeviceInfo"
+ "hasSleepTimerFireDate"
+ "hasSleepTimerStopMode"
+ "hasSleepTimerTime"
+ "hidden"
+ "id=%@"
+ "identitySupportsCollaboration"
+ "idsAccountIsValid"
+ "initWithDetails:outputDeviceUIDs:outputDeviceGroupID:features:"
+ "initWithHostInfo:invitationData:sharedSecret:sessionIdentifier:equivalentMediaIdentifier:version:"
+ "initWithIdentifier:identity:connected:guest:hidden:"
+ "initWithOrigin:bundleIdentifier:player:"
+ "initWithStartDate:endDate:maxEvents:lastN:reversed:"
+ "invalidated"
+ "isEligibleForHostingGroupSession"
+ "isEligibleForJoiningGroupSession"
+ "isFullSubscriber"
+ "isHidden"
+ "isManateeEnabled"
+ "isMinor"
+ "isW3Device"
+ "kMRMediaRemoteCommandInfoSleepTimerFireDate"
+ "kMRMediaRemoteCommandInfoSleepTimerStopMode"
+ "kMRMediaRemoteCommandInfoSleepTimerTime"
+ "kMRMediaRemoteOptionSleepTimerStopMode"
+ "kMRMediaRemoteOptionSleepTimerTime"
+ "leaderDeviceInfo"
+ "live_activity_banner"
+ "mediaAccountHostingState"
+ "mediaAccountJoiningState"
+ "mediaUserStates"
+ "mhs"
+ "mjs"
+ "mr_isMediaRemoteError"
+ "mte"
+ "mus"
+ "outputDeviceID"
+ "pauseOutputDeviceUIDs"
+ "pauseOutputDeviceUIDs:details:queue:completion:"
+ "playerPathDescription"
+ "preferRoutesMatchingMediaType"
+ "presentProximityCardWithDeviceName:modelIdentifier:color:url:queue:completion:"
+ "prv"
+ "publisherWithOptions:"
+ "registerDiscoverySessionFactory:"
+ "requestID: %@"
+ "routeIsValidForHosting"
+ "rvH"
+ "searchEndpointsForOutputDeviceUID:timeout:details:queue:completion:"
+ "setByAddingObjectsFromSet:"
+ "setCurrentMediaUserState:"
+ "setEligibilityStatus:"
+ "setGroupSessionsSupportedForAccountRegion:"
+ "setHasAcceptedDisplayNameAcknowledgement:"
+ "setHasAcceptedPrivacyAcknowledgement:"
+ "setHasHidden:"
+ "setHasSleepTimerFireDate:"
+ "setHasSleepTimerStopMode:"
+ "setHasSleepTimerTime:"
+ "setHidden:"
+ "setIdentitySupportsCollaboration:"
+ "setIdsAccountIsValid:"
+ "setInvalidated:"
+ "setIsEligibleForHostingGroupSession:"
+ "setIsEligibleForJoiningGroupSession:"
+ "setIsFullSubscriber:"
+ "setIsManateeEnabled:"
+ "setIsMinor:"
+ "setLeaderDeviceInfo:"
+ "setLock:"
+ "setMRInfo"
+ "setMediaAccountHostingState:"
+ "setMediaAccountJoiningState:"
+ "setMediaUserStates:"
+ "setObservers:"
+ "setRouteIsValidForHosting:"
+ "setShouldWaitForUnanimousEndpoints:"
+ "setSleepTimerFireDate:"
+ "setSleepTimerStopMode:"
+ "setSleepTimerTime:"
+ "setUserIdentity:"
+ "shouldWaitForUnanimousEndpoints"
+ "sinkWithCompletion:shouldContinue:"
+ "sleepTimerFireDate"
+ "sleepTimerStopMode"
+ "sleepTimerStopModeAsString:"
+ "sleepTimerTime"
+ "srg"
+ "stf"
+ "sub"
+ "supportAirPlayLeaderInfoSync"
+ "supportCriticalSectionManagement"
+ "supportGroupSessionHomePodBoop"
+ "supportLiveActivityBanner"
+ "timeout"
+ "transition"
+ "updateGroupSessionEligibility:"
+ "updateStatus:"
+ "url"
+ "userIdentity"
+ "usr"
+ "v16@?0@\"BPSCompletion\"8"
+ "v20@0:8{os_unfair_lock_s=I}16"
+ "v40@0:8d16@24@?32"
+ "v40@?0@\"NSArray\"8@\"NSString\"16@\"NSArray\"24@\"NSError\"32"
+ "waitForPlaybackWithTimeout:queue:completion:"
+ "waveformNonVariableFramerate"
+ "wrangler_homepod_boop"
+ "{?=\"assistantCommandSendTimestamp\"b1\"assistantTTSEndTimestamp\"b1\"commandTimeout\"b1\"playbackPosition\"b1\"radioStationID\"b1\"sleepTimerTime\"b1\"trackID\"b1\"playbackQueueDestinationOffset\"b1\"playbackQueueInsertionPosition\"b1\"playbackQueueOffset\"b1\"playbackRate\"b1\"playbackSessionPriority\"b1\"prepareForSetQueueProactiveReasonType\"b1\"queueEndAction\"b1\"rating\"b1\"repeatMode\"b1\"replaceIntent\"b1\"sendOptions\"b1\"shuffleMode\"b1\"skipInterval\"b1\"sleepTimerStopMode\"b1\"vocalsControlLevel\"b1\"vocalsControlMaxLevel\"b1\"vocalsControlMinLevel\"b1\"alwaysIgnoreDuringCall\"b1\"alwaysIgnoreDuringSharePlay\"b1\"beginSeek\"b1\"endSeek\"b1\"externalPlayerCommand\"b1\"negative\"b1\"originatedFromRemoteDevice\"b1\"prepareForSetQueueIsProactive\"b1\"preservesQueueEndAction\"b1\"preservesRepeatMode\"b1\"preservesShuffleMode\"b1\"requestDefermentToPlaybackQueuePosition\"b1\"shouldBeginRadioPlayback\"b1\"shouldOverrideManuallyCuratedQueue\"b1\"trueCompletion\"b1\"verifySupportedCommands\"b1\"vocalsControlActive\"b1\"vocalsControlContinuous\"b1}"
+ "{?=\"connected\"b1\"guest\"b1\"hidden\"b1}"
+ "{?=\"sleepTimerFireDate\"b1\"sleepTimerTime\"b1\"canScrub\"b1\"command\"b1\"currentQueueEndAction\"b1\"disabledReason\"b1\"maximumRating\"b1\"minimumRating\"b1\"numAvailableSkips\"b1\"preferredPlaybackRate\"b1\"presentationStyle\"b1\"repeatMode\"b1\"shuffleMode\"b1\"skipFrequency\"b1\"skipInterval\"b1\"sleepTimerStopMode\"b1\"upNextItemCount\"b1\"vocalsControlLevel\"b1\"vocalsControlMaxLevel\"b1\"vocalsControlMinLevel\"b1\"active\"b1\"enabled\"b1\"supportsSharedQueue\"b1\"vocalsControlActive\"b1\"vocalsControlContinuous\"b1}"
+ "{?=\"version\"b1}"
+ "\x7f\x05$\x13\x11\x11\"\x12\x15"
+ "\xcf\n\x15"
+ "\xf01\x12!\x113"
- "\x02\"\x14"
- "\x13\x1c\x12"
- "\x15"
- "\x18\x12\x15\x12\x13\x12\x16"
- "'"
- "/System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet"
- "/System/Library/PrivateFrameworks/CoreDuetContext.framework/CoreDuetContext"
- "<%@: identifier=%@, identity=%@, local=%@, pending=%@, connected=%@, guest=%@>"
- "@\"MRMediaSuggestionPreferences\""
- "@\"_CDClientContext\""
- "@\"_CDContextualChangeRegistration\""
- "Application inside current suggestions was uninstalled"
- "Application inside current suggestions was updated"
- "Cache Miss: Request: %{public}@<%{public}@> for %{public}@ %{public}@"
- "LSApplicationWorkspaceObserverProtocol"
- "MRGroupSessionToken * _Nonnull MRGroupSessionTokenCreateWithInvitationData(NSData *__strong _Nonnull, NSString * _Nullable __strong)"
- "MRLocalGroupSessionInfoDidChangeNotification"
- "MRLocalGroupSessionInfoUserInfoKey"
- "Not attempting to migrate because endpoint is group session endpoint"
- "Proactive endpoint is group session endpoint."
- "T@\"MRDeviceInfo\",&,N,V_deviceInfo"
- "T@\"NSData\",R,N,V_date"
- "T@\"NSString\",R,N,V_effectiveIdentifier"
- "User preferences changed"
- "[MRDistantExternalDevice] [debug] %@ NOTIFICATION HACK FOR MUSIC with: %@"
- "[MRMediaSuggestionController] %@"
- "[MRMediaSuggestionController] Error requesting suggestion: %@"
- "[MRMediaSuggestionController] Querying for new INPlayMediaIntent."
- "[MRMediaSuggestionController] Registering observers."
- "[MRMediaSuggestionController] Reloading because %@."
- "[MRMediaSuggestionRequest] Intent %@ is not valid for suggestions."
- "[MRMediaSuggestionRequest] Performing preference-respecting request %{public}@ with preferences %@."
- "[MRMediaSuggestionRequest] Performing request %{public}@ with UUID %{private}@."
- "[MRMediaSuggestionRequest] Request %{public}@ failed with error %@"
- "[MRMediaSuggestionRequest] Unexpected intent %@"
- "[MRMediaSuggestionRequest] received non media intent %@ from event. Skipping."
- "[MRNowPlaying] MRMediaRemoteSetCanBeNowPlayingApplication set to %@ by caller %@."
- "_CDClientContext"
- "_CDContextQueries"
- "_CDContextualChangeRegistration"
- "_CDContextualPredicate"
- "_DKEventQuery"
- "_DKIntentMetadataKey"
- "_DKKnowledgeStore"
- "_DKQuery"
- "_DKSystemEventStreams"
- "_changeRegistration"
- "_clientContext"
- "_effectiveIdentifier"
- "_handleLocalGroupSessionInfoDidChangeNotification:"
- "_internalSuggestions"
- "_parameterCombinationsForClassName:"
- "_preferences"
- "_registeredForChanges"
- "andPredicateWithSubpredicates:"
- "appIntentsStream"
- "applicationIconDidChange:"
- "applicationInstallsArePrioritized:arePaused:"
- "applicationInstallsDidCancel:"
- "applicationInstallsDidChange:"
- "applicationInstallsDidPause:"
- "applicationInstallsDidPrioritize:"
- "applicationInstallsDidResume:"
- "applicationInstallsDidStart:"
- "applicationInstallsDidUpdateIcon:"
- "applicationStateDidChange:"
- "applicationsDidChangePersonas:"
- "applicationsDidFailToInstall:"
- "applicationsDidFailToUninstall:"
- "applicationsDidInstall:"
- "applicationsDidUninstall:"
- "applicationsWillInstall:"
- "applicationsWillUninstall:"
- "com.apple.MediaRemote.MRMediaSuggestionController.delegateQueue"
- "com.apple.MediaRemote.MRMediaSuggestionController.queue"
- "com.apple.mediaremote.MRMediaSuggestionController"
- "controller:didUpdateSuggestions:"
- "coriander"
- "createTokenWithInvitationData:equivalentMediaIdentifier:"
- "databaseWasRebuilt"
- "defaultWorkspace"
- "deregisterCallback:"
- "deviceManagementPolicyDidChange:"
- "eventQueryWithPredicate:eventStreams:offset:limit:sortDescriptors:"
- "executeQuery:error:"
- "handleLocalGroupSessionDidChangeNotification:"
- "helperPlaceholdersInstalled:"
- "helperPlaceholdersUninstalled:"
- "initWithDictionary:copyItems:"
- "initWithHostInfo:invitationData:"
- "initWithHostInfo:invitationData:sharedSecret:sessionIdentifier:equivalentMediaIdentifier:"
- "insertObject:atIndex:"
- "intentClassKey"
- "intentDKObjUUIDKey"
- "intentSourceBundleIDKey"
- "keyPathForIntentsDataDictionary"
- "knowledgeStore"
- "knowledgeStoreWithDirectReadOnlyAccess"
- "localWakingRegistrationWithIdentifier:contextualPredicate:clientIdentifier:callback:"
- "networkUsageChanged:"
- "notPredicateWithSubpredicate:"
- "o\x05$\x13\x11\x11\"\x12\x15"
- "observeLaunchProhibitedApps"
- "orPredicateWithSubpredicates:"
- "pluginsDidInstall:"
- "pluginsDidUninstall:"
- "pluginsWillUninstall:"
- "predicateForEventsWithBundleID:"
- "predicateForKeyPath:withPredicate:"
- "predicateForObjectWithUUID:"
- "predicateForObjectsWithMetadataKey:andStringValue:"
- "predicateWithFormat:"
- "predicateWithValue:"
- "registerCallback:"
- "self.%@.value.%@ == %@"
- "setExecuteConcurrently:"
- "shouldOmitHost"
- "startDateSortDescriptorAscending:"
- "userContext"
- "v24@?0@\"MRMediaSuggestion\"8@\"NSError\"16"
- "v24@?0@\"NSString\"8@\"NSDictionary\"16"
- "v32@0:8@\"NSArray\"16@\"NSArray\"24"
- "{?=\"assistantCommandSendTimestamp\"b1\"assistantTTSEndTimestamp\"b1\"commandTimeout\"b1\"playbackPosition\"b1\"radioStationID\"b1\"trackID\"b1\"playbackQueueDestinationOffset\"b1\"playbackQueueInsertionPosition\"b1\"playbackQueueOffset\"b1\"playbackRate\"b1\"playbackSessionPriority\"b1\"prepareForSetQueueProactiveReasonType\"b1\"queueEndAction\"b1\"rating\"b1\"repeatMode\"b1\"replaceIntent\"b1\"sendOptions\"b1\"shuffleMode\"b1\"skipInterval\"b1\"vocalsControlLevel\"b1\"vocalsControlMaxLevel\"b1\"vocalsControlMinLevel\"b1\"alwaysIgnoreDuringCall\"b1\"alwaysIgnoreDuringSharePlay\"b1\"beginSeek\"b1\"endSeek\"b1\"externalPlayerCommand\"b1\"negative\"b1\"originatedFromRemoteDevice\"b1\"prepareForSetQueueIsProactive\"b1\"preservesQueueEndAction\"b1\"preservesRepeatMode\"b1\"preservesShuffleMode\"b1\"requestDefermentToPlaybackQueuePosition\"b1\"shouldBeginRadioPlayback\"b1\"shouldOverrideManuallyCuratedQueue\"b1\"trueCompletion\"b1\"verifySupportedCommands\"b1\"vocalsControlActive\"b1\"vocalsControlContinuous\"b1}"
- "{?=\"canScrub\"b1\"command\"b1\"currentQueueEndAction\"b1\"disabledReason\"b1\"maximumRating\"b1\"minimumRating\"b1\"numAvailableSkips\"b1\"preferredPlaybackRate\"b1\"presentationStyle\"b1\"repeatMode\"b1\"shuffleMode\"b1\"skipFrequency\"b1\"skipInterval\"b1\"upNextItemCount\"b1\"vocalsControlLevel\"b1\"vocalsControlMaxLevel\"b1\"vocalsControlMinLevel\"b1\"active\"b1\"enabled\"b1\"supportsSharedQueue\"b1\"vocalsControlActive\"b1\"vocalsControlContinuous\"b1}"
- "{?=\"connected\"b1\"guest\"b1}"
- "\xcf\n\x14"
- "\xf0\x11\x12!\x11#"

```
