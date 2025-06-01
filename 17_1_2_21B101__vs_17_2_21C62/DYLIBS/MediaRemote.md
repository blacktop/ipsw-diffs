## MediaRemote

> `/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote`

```diff

-4023.210.1.0.0
-  __TEXT.__text: 0x298634
+4023.310.5.0.0
+  __TEXT.__text: 0x2a0960
   __TEXT.__auth_stubs: 0x1610
-  __TEXT.__objc_methlist: 0x244b8
+  __TEXT.__objc_methlist: 0x24bd0
   __TEXT.__const: 0x378
-  __TEXT.__cstring: 0x279da
-  __TEXT.__oslogstring: 0xcacd
-  __TEXT.__gcc_except_tab: 0x4e0c
+  __TEXT.__cstring: 0x2873a
+  __TEXT.__oslogstring: 0xcc4a
+  __TEXT.__gcc_except_tab: 0x4ddc
   __TEXT.__ustring: 0x12
-  __TEXT.__unwind_info: 0x9ff8
-  __TEXT.__objc_classname: 0x4483
-  __TEXT.__objc_methname: 0x42222
-  __TEXT.__objc_methtype: 0x82aa
-  __TEXT.__objc_stubs: 0x22c20
+  __TEXT.__unwind_info: 0xa168
+  __TEXT.__objc_classname: 0x44dd
+  __TEXT.__objc_methname: 0x431fe
+  __TEXT.__objc_methtype: 0x83c4
+  __TEXT.__objc_stubs: 0x233e0
   __DATA_CONST.__got: 0x1c0
-  __DATA_CONST.__const: 0x9ff8
-  __DATA_CONST.__objc_classlist: 0xfa8
+  __DATA_CONST.__const: 0xa180
+  __DATA_CONST.__objc_classlist: 0xfb8
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x230
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x33fb0
-  __DATA_CONST.__objc_selrefs: 0xcba0
+  __DATA_CONST.__objc_const: 0x348c0
+  __DATA_CONST.__objc_selrefs: 0xce98
   __DATA_CONST.__objc_arraydata: 0x1d0
-  __AUTH_CONST.__cfstring: 0x1c5e0
-  __AUTH_CONST.__objc_const: 0xb628
-  __AUTH_CONST.__const: 0x3000
+  __AUTH_CONST.__cfstring: 0x1d5e0
+  __AUTH_CONST.__objc_const: 0xb6b8
+  __AUTH_CONST.__const: 0x3040
   __AUTH_CONST.__objc_intobj: 0x390
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0xb18
-  __AUTH.__objc_data: 0x73a0
-  __AUTH.__data: 0x1d0
+  __AUTH.__objc_data: 0x7490
+  __AUTH.__data: 0x1f0
   __DATA.__objc_protorefs: 0x88
   __DATA.__objc_classrefs: 0x10d0
-  __DATA.__objc_superrefs: 0xdf0
-  __DATA.__objc_ivar: 0x2c0c
+  __DATA.__objc_superrefs: 0xe00
+  __DATA.__objc_ivar: 0x2c8c
   __DATA.__data: 0x1d00
-  __DATA.__bss: 0x4e0
+  __DATA.__bss: 0x500
   __DATA.__common: 0x0
-  __DATA_DIRTY.__objc_data: 0x28f0
+  __DATA_DIRTY.__objc_data: 0x28a0
   __DATA_DIRTY.__data: 0x210
   __DATA_DIRTY.__bss: 0x6f8
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3E101B0B-EA53-3B4A-B311-B02D67CD4B10
-  Functions: 17745
-  Symbols:   48253
-  CStrings:  21015
+  UUID: 9AE0A774-1911-389E-8845-644295614FB3
+  Functions: 17929
+  Symbols:   48737
+  CStrings:  21433
 
Symbols:
+ +[MRAVEndpoint _notifyGroupSessionInfoDidChange:endpoint:]
+ +[MRAVEndpoint connectToEndpointContainingOutputDeviceUID:options:details:completion:]
+ +[MRGroupSessionHostInfo supportsSecureCoding]
+ +[MRNowPlayingRequest isMostRecentMediaPlaybackRelevantReasonWithinInternal:]
+ +[MRNowPlayingRequest isMostRecentMediaPlaybackRelevantWithinInterval:]
+ +[_MRGroupSessionJoinRequestProtobuf oobKeysType]
+ +[_MRGroupSessionMemberSyncMessageProtobuf pendingParticipantsType]
+ -[MRAVDistantEndpoint _handleGroupSessionTokenDidChangeNotification:]
+ -[MRAVDistantEndpoint _registerNotificationsForExternalDevice:]
+ -[MRAVDistantEndpoint _unregisterNotificationsForExternalDevice:]
+ -[MRAVDistantEndpoint groupSessionInfo]
+ -[MRAVEndpoint connectToExternalDeviceWithOptions:details:completion:]
+ -[MRAVEndpoint groupContainsDiscoverableGroupLeader]
+ -[MRAVEndpoint migrateToEndpointOrModifyTopology:migrationRequest:topologyModificationRequest:withReplyQueue:completion:]
+ -[MRAVLocalEndpoint handleLocalGroupSessionDidChangeNotification:]
+ -[MRAVLocalEndpoint registerNotifications]
+ -[MRCodableGroupSessionParticipant isGuest]
+ -[MRCodableGroupSessionParticipant setGuest:]
+ -[MRContentItemMetadataAudioFormat hasRenderingMode]
+ -[MRContentItemMetadataAudioFormat renderingMode]
+ -[MRContentItemMetadataAudioFormat setRenderingMode:]
+ -[MRDeviceInfo groupSessionToken]
+ -[MRDeviceInfo setGroupSessionToken:]
+ -[MRDiscoveredGroupSession copyWithZone:]
+ -[MRDiscoveredGroupSession initWithIdentifier:hostInfo:]
+ -[MRDistantExternalDevice _hack_publishLocalGroupSessionChange:]
+ -[MRDistantExternalDevice groupSessionToken]
+ -[MRDistantExternalDevice hostedExternalDeviceGroupSessionTokenDidChange:]
+ -[MRExternalDevice groupSessionToken]
+ -[MRExternalDevice setGroupSessionTokenCallback:withQueue:]
+ -[MRGroupSessionHostInfo .cxx_destruct]
+ -[MRGroupSessionHostInfo copyWithZone:]
+ -[MRGroupSessionHostInfo description]
+ -[MRGroupSessionHostInfo displayName]
+ -[MRGroupSessionHostInfo encodeWithCoder:]
+ -[MRGroupSessionHostInfo hash]
+ -[MRGroupSessionHostInfo initWithCoder:]
+ -[MRGroupSessionHostInfo initWithRouteType:displayName:]
+ -[MRGroupSessionHostInfo isEqual:]
+ -[MRGroupSessionHostInfo isLockScreenAffordanceAllowed]
+ -[MRGroupSessionHostInfo localizedSessionName]
+ -[MRGroupSessionHostInfo routeType]
+ -[MRGroupSessionInfo effectiveIdentifier]
+ -[MRGroupSessionInfo equivalentMediaIdentifier]
+ -[MRGroupSessionInfo initWithIdentifier:hostInfo:isHosted:equivalentMediaIdentifier:]
+ -[MRGroupSessionInfo initWithToken:isHosted:]
+ -[MRGroupSessionToken copyWithZone:]
+ -[MRGroupSessionToken effectiveIdentifier]
+ -[MRGroupSessionToken equivalentMediaIdentifier]
+ -[MRGroupSessionToken hostInfo]
+ -[MRGroupSessionToken initWithHostInfo:invitationData:]
+ -[MRGroupSessionToken initWithHostInfo:invitationData:sharedSecret:sessionIdentifier:equivalentMediaIdentifier:]
+ -[MRGroupSessionToken initWithProtobuf:]
+ -[MRGroupSessionToken protobuf]
+ -[MRGroupSessionToken sessionIdentifier]
+ -[MRGroupSessionToken sharedSecret]
+ -[MRGroupTopologyModificationRequest muteUntilFinished]
+ -[MRGroupTopologyModificationRequest setMuteUntilFinished:]
+ -[MRMediaRemoteService createTokenWithInvitationData:equivalentMediaIdentifier:]
+ -[MRNowPlayingAudioFormatContentInfo renderingMode]
+ -[MRNowPlayingAudioFormatContentInfo setRenderingMode:]
+ -[MROriginClientPropertiesMessage devicePlaybackSessionID]
+ -[MROriginClientPropertiesMessage initWithLastPlayingDate:devicePlaybackSessionID:]
+ -[MRRemoteControlGroupSession parseInitialState:]
+ -[MRRemoteControlGroupSession session:didConnectWithInitialState:]
+ -[MRRemoteControlGroupSession shouldOmitHost]
+ -[MRRequestDetails requestReasonID]
+ -[MRStaticRouteBannerRequest actionImageName]
+ -[MRStaticRouteBannerRequest setActionImageName:]
+ -[MRUpdateActiveSystemEndpointRequest demoteWhenSyncingToCompanion]
+ -[MRUpdateActiveSystemEndpointRequest disableDuration]
+ -[MRUpdateActiveSystemEndpointRequest setDemoteWhenSyncingToCompanion:]
+ -[MRUpdateActiveSystemEndpointRequest setDisableDuration:]
+ -[MRUserSettings computeDevicePlaybackSessionID]
+ -[MRUserSettings enableRouteRecommendations]
+ -[MRUserSettings groupSessionAutoApproveHomeParticipants]
+ -[MRUserSettings groupSessionGenerateSharedSecret]
+ -[MRUserSettings groupSessionListenForProxyJoinRequests]
+ -[MRUserSettings groupSessionSynchronizePendingParticipants]
+ -[MRUserSettings needsMXApplications]
+ -[NSArray(MRAVAdditions) mr_containsVideoOutputDevice]
+ -[_MRAudioFormatProtobuf StringAsRenderingMode:]
+ -[_MRAudioFormatProtobuf hasRenderingMode]
+ -[_MRAudioFormatProtobuf renderingModeAsString:]
+ -[_MRAudioFormatProtobuf renderingMode]
+ -[_MRAudioFormatProtobuf setHasRenderingMode:]
+ -[_MRAudioFormatProtobuf setRenderingMode:]
+ -[_MRDeviceInfoMessageProtobuf groupSessionToken]
+ -[_MRDeviceInfoMessageProtobuf hasGroupSessionToken]
+ -[_MRDeviceInfoMessageProtobuf setGroupSessionToken:]
+ -[_MRGroupSessionInfoProtobuf equivalentMediaIdentifier]
+ -[_MRGroupSessionInfoProtobuf hasEquivalentMediaIdentifier]
+ -[_MRGroupSessionInfoProtobuf setEquivalentMediaIdentifier:]
+ -[_MRGroupSessionJoinRequestProtobuf addOobKeys:]
+ -[_MRGroupSessionJoinRequestProtobuf clearOobKeys]
+ -[_MRGroupSessionJoinRequestProtobuf hasIdentifier]
+ -[_MRGroupSessionJoinRequestProtobuf identifier]
+ -[_MRGroupSessionJoinRequestProtobuf oobKeysAtIndex:]
+ -[_MRGroupSessionJoinRequestProtobuf oobKeysCount]
+ -[_MRGroupSessionJoinRequestProtobuf oobKeys]
+ -[_MRGroupSessionJoinRequestProtobuf setIdentifier:]
+ -[_MRGroupSessionJoinRequestProtobuf setOobKeys:]
+ -[_MRGroupSessionJoinResponseMessageProtobuf .cxx_destruct]
+ -[_MRGroupSessionJoinResponseMessageProtobuf approved]
+ -[_MRGroupSessionJoinResponseMessageProtobuf copyTo:]
+ -[_MRGroupSessionJoinResponseMessageProtobuf copyWithZone:]
+ -[_MRGroupSessionJoinResponseMessageProtobuf description]
+ -[_MRGroupSessionJoinResponseMessageProtobuf dictionaryRepresentation]
+ -[_MRGroupSessionJoinResponseMessageProtobuf hash]
+ -[_MRGroupSessionJoinResponseMessageProtobuf isEqual:]
+ -[_MRGroupSessionJoinResponseMessageProtobuf mergeFrom:]
+ -[_MRGroupSessionJoinResponseMessageProtobuf participantIdentifier]
+ -[_MRGroupSessionJoinResponseMessageProtobuf readFrom:]
+ -[_MRGroupSessionJoinResponseMessageProtobuf setApproved:]
+ -[_MRGroupSessionJoinResponseMessageProtobuf setParticipantIdentifier:]
+ -[_MRGroupSessionJoinResponseMessageProtobuf writeTo:]
+ -[_MRGroupSessionJoinResponseMessageProtobuf writeTo:].cold.1
+ -[_MRGroupSessionMemberSyncMessageProtobuf addPendingParticipants:]
+ -[_MRGroupSessionMemberSyncMessageProtobuf clearPendingParticipants]
+ -[_MRGroupSessionMemberSyncMessageProtobuf pendingParticipantsAtIndex:]
+ -[_MRGroupSessionMemberSyncMessageProtobuf pendingParticipantsCount]
+ -[_MRGroupSessionMemberSyncMessageProtobuf pendingParticipants]
+ -[_MRGroupSessionMemberSyncMessageProtobuf setPendingParticipants:]
+ -[_MRGroupSessionParticipantProtobuf guest]
+ -[_MRGroupSessionParticipantProtobuf hasGuest]
+ -[_MRGroupSessionParticipantProtobuf setGuest:]
+ -[_MRGroupSessionParticipantProtobuf setHasGuest:]
+ -[_MRGroupSessionRemoveRequestProtobuf .cxx_destruct]
+ -[_MRGroupSessionRemoveRequestProtobuf copyTo:]
+ -[_MRGroupSessionRemoveRequestProtobuf copyWithZone:]
+ -[_MRGroupSessionRemoveRequestProtobuf description]
+ -[_MRGroupSessionRemoveRequestProtobuf dictionaryRepresentation]
+ -[_MRGroupSessionRemoveRequestProtobuf hash]
+ -[_MRGroupSessionRemoveRequestProtobuf isEqual:]
+ -[_MRGroupSessionRemoveRequestProtobuf mergeFrom:]
+ -[_MRGroupSessionRemoveRequestProtobuf participantIdentifier]
+ -[_MRGroupSessionRemoveRequestProtobuf readFrom:]
+ -[_MRGroupSessionRemoveRequestProtobuf setParticipantIdentifier:]
+ -[_MRGroupSessionRemoveRequestProtobuf writeTo:]
+ -[_MRGroupSessionRemoveRequestProtobuf writeTo:].cold.1
+ -[_MRGroupSessionTokenProtobuf .cxx_destruct]
+ -[_MRGroupSessionTokenProtobuf StringAsRouteType:]
+ -[_MRGroupSessionTokenProtobuf copyTo:]
+ -[_MRGroupSessionTokenProtobuf copyWithZone:]
+ -[_MRGroupSessionTokenProtobuf description]
+ -[_MRGroupSessionTokenProtobuf dictionaryRepresentation]
+ -[_MRGroupSessionTokenProtobuf displayName]
+ -[_MRGroupSessionTokenProtobuf equivalentMediaIdentifier]
+ -[_MRGroupSessionTokenProtobuf hasDisplayName]
+ -[_MRGroupSessionTokenProtobuf hasEquivalentMediaIdentifier]
+ -[_MRGroupSessionTokenProtobuf hasSessionIdentifier]
+ -[_MRGroupSessionTokenProtobuf hasSharedSecret]
+ -[_MRGroupSessionTokenProtobuf hash]
+ -[_MRGroupSessionTokenProtobuf invitationData]
+ -[_MRGroupSessionTokenProtobuf isEqual:]
+ -[_MRGroupSessionTokenProtobuf mergeFrom:]
+ -[_MRGroupSessionTokenProtobuf readFrom:]
+ -[_MRGroupSessionTokenProtobuf routeTypeAsString:]
+ -[_MRGroupSessionTokenProtobuf routeType]
+ -[_MRGroupSessionTokenProtobuf sessionIdentifier]
+ -[_MRGroupSessionTokenProtobuf setDisplayName:]
+ -[_MRGroupSessionTokenProtobuf setEquivalentMediaIdentifier:]
+ -[_MRGroupSessionTokenProtobuf setInvitationData:]
+ -[_MRGroupSessionTokenProtobuf setRouteType:]
+ -[_MRGroupSessionTokenProtobuf setSessionIdentifier:]
+ -[_MRGroupSessionTokenProtobuf setSharedSecret:]
+ -[_MRGroupSessionTokenProtobuf sharedSecret]
+ -[_MRGroupSessionTokenProtobuf writeTo:]
+ -[_MRGroupSessionTokenProtobuf writeTo:].cold.1
+ -[_MRGroupTopologyModificationRequestProtobuf hasMuteUntilFinished]
+ -[_MRGroupTopologyModificationRequestProtobuf muteUntilFinished]
+ -[_MRGroupTopologyModificationRequestProtobuf setHasMuteUntilFinished:]
+ -[_MRGroupTopologyModificationRequestProtobuf setMuteUntilFinished:]
+ -[_MRMRNowPlayingAudioFormatContentInfoProtobuf hasRenderingMode]
+ -[_MRMRNowPlayingAudioFormatContentInfoProtobuf renderingMode]
+ -[_MRMRNowPlayingAudioFormatContentInfoProtobuf setHasRenderingMode:]
+ -[_MRMRNowPlayingAudioFormatContentInfoProtobuf setRenderingMode:]
+ -[_MRMediaRemoteMessageProtobuf hasReplyIdentifier]
+ -[_MRMediaRemoteMessageProtobuf replyIdentifier]
+ -[_MRMediaRemoteMessageProtobuf setReplyIdentifier:]
+ -[_MROriginClientPropertiesMessageProtobuf .cxx_destruct]
+ -[_MROriginClientPropertiesMessageProtobuf devicePlaybackSessionID]
+ -[_MROriginClientPropertiesMessageProtobuf hasDevicePlaybackSessionID]
+ -[_MROriginClientPropertiesMessageProtobuf setDevicePlaybackSessionID:]
+ -[_MRUpdateActiveSystemEndpointRequestProtobuf demoteWhenSyncingToCompanion]
+ -[_MRUpdateActiveSystemEndpointRequestProtobuf disableDuration]
+ -[_MRUpdateActiveSystemEndpointRequestProtobuf hasDemoteWhenSyncingToCompanion]
+ -[_MRUpdateActiveSystemEndpointRequestProtobuf hasDisableDuration]
+ -[_MRUpdateActiveSystemEndpointRequestProtobuf setDemoteWhenSyncingToCompanion:]
+ -[_MRUpdateActiveSystemEndpointRequestProtobuf setDisableDuration:]
+ -[_MRUpdateActiveSystemEndpointRequestProtobuf setHasDemoteWhenSyncingToCompanion:]
+ -[_MRUpdateActiveSystemEndpointRequestProtobuf setHasDisableDuration:]
+ GCC_except_table193
+ GCC_except_table204
+ GCC_except_table205
+ GCC_except_table257
+ GCC_except_table77
+ GCC_except_table96
+ OBJC_IVAR_$__MRAudioFormatProtobuf._renderingMode
+ OBJC_IVAR_$__MRDeviceInfoMessageProtobuf._groupSessionToken
+ OBJC_IVAR_$__MRGroupSessionInfoProtobuf._equivalentMediaIdentifier
+ OBJC_IVAR_$__MRGroupSessionJoinRequestProtobuf._identifier
+ OBJC_IVAR_$__MRGroupSessionJoinRequestProtobuf._oobKeys
+ OBJC_IVAR_$__MRGroupSessionJoinResponseMessageProtobuf._approved
+ OBJC_IVAR_$__MRGroupSessionJoinResponseMessageProtobuf._participantIdentifier
+ OBJC_IVAR_$__MRGroupSessionMemberSyncMessageProtobuf._pendingParticipants
+ OBJC_IVAR_$__MRGroupSessionParticipantProtobuf._guest
+ OBJC_IVAR_$__MRGroupSessionRemoveRequestProtobuf._participantIdentifier
+ OBJC_IVAR_$__MRGroupSessionTokenProtobuf._displayName
+ OBJC_IVAR_$__MRGroupSessionTokenProtobuf._equivalentMediaIdentifier
+ OBJC_IVAR_$__MRGroupSessionTokenProtobuf._invitationData
+ OBJC_IVAR_$__MRGroupSessionTokenProtobuf._routeType
+ OBJC_IVAR_$__MRGroupSessionTokenProtobuf._sessionIdentifier
+ OBJC_IVAR_$__MRGroupSessionTokenProtobuf._sharedSecret
+ OBJC_IVAR_$__MRGroupTopologyModificationRequestProtobuf._muteUntilFinished
+ OBJC_IVAR_$__MRMRNowPlayingAudioFormatContentInfoProtobuf._renderingMode
+ OBJC_IVAR_$__MRMediaRemoteMessageProtobuf._replyIdentifier
+ OBJC_IVAR_$__MROriginClientPropertiesMessageProtobuf._devicePlaybackSessionID
+ OBJC_IVAR_$__MRUpdateActiveSystemEndpointRequestProtobuf._demoteWhenSyncingToCompanion
+ OBJC_IVAR_$__MRUpdateActiveSystemEndpointRequestProtobuf._disableDuration
+ _AVOutputContextAddOutputDeviceOptionMuteUntilContextModificationIsFinishedFunction
+ _AVOutputContextSetOutputDeviceMuteUntilContextModificationIsFinishedKeyFunction
+ _AVOutputContextSetOutputDevicesOptionMuteUntilContextModificationIsFinishedFunction
+ _INPrivatePlayMediaIntentDataFunction
+ _MRAVEndpointGroupSessionInfoDidChangeNotification
+ _MRAVEndpointGroupSessionInfoUserInfoKey
+ _MRExternalDeviceGroupSessionTokenDidChangeNotification
+ _MRExternalDeviceGroupSessionTokenUserInfoKey
+ _OBJC_CLASS_$_MRGroupSessionHostInfo
+ _OBJC_CLASS_$__MRGroupSessionJoinResponseMessageProtobuf
+ _OBJC_CLASS_$__MRGroupSessionRemoveRequestProtobuf
+ _OBJC_CLASS_$__MRGroupSessionTokenProtobuf
+ _OBJC_IVAR_$_MRCodableGroupSessionParticipant._guest
+ _OBJC_IVAR_$_MRContentItemMetadataAudioFormat._hasRenderingMode
+ _OBJC_IVAR_$_MRContentItemMetadataAudioFormat._renderingMode
+ _OBJC_IVAR_$_MRDeviceInfo._groupSessionToken
+ _OBJC_IVAR_$_MRDistantExternalDevice._groupSessionToken
+ _OBJC_IVAR_$_MRDistantExternalDevice._hasFetchedGroupSessionInfo
+ _OBJC_IVAR_$_MRGroupSessionHostInfo._displayName
+ _OBJC_IVAR_$_MRGroupSessionHostInfo._routeType
+ _OBJC_IVAR_$_MRGroupSessionInfo._equivalentMediaIdentifier
+ _OBJC_IVAR_$_MRGroupSessionToken._effectiveIdentifier
+ _OBJC_IVAR_$_MRGroupSessionToken._equivalentMediaIdentifier
+ _OBJC_IVAR_$_MRGroupSessionToken._hostInfo
+ _OBJC_IVAR_$_MRGroupSessionToken._sessionIdentifier
+ _OBJC_IVAR_$_MRGroupSessionToken._sharedSecret
+ _OBJC_IVAR_$_MRGroupTopologyModificationRequest._muteUntilFinished
+ _OBJC_IVAR_$_MRNowPlayingAudioFormatContentInfo._renderingMode
+ _OBJC_IVAR_$_MRStaticRouteBannerRequest._actionImageName
+ _OBJC_IVAR_$_MRUpdateActiveSystemEndpointRequest._demoteWhenSyncingToCompanion
+ _OBJC_IVAR_$_MRUpdateActiveSystemEndpointRequest._disableDuration
+ _OBJC_METACLASS_$_MRGroupSessionHostInfo
+ _OBJC_METACLASS_$__MRGroupSessionJoinResponseMessageProtobuf
+ _OBJC_METACLASS_$__MRGroupSessionRemoveRequestProtobuf
+ _OBJC_METACLASS_$__MRGroupSessionTokenProtobuf
+ __MRGroupSessionJoinResponseMessageProtobufReadFrom
+ __MRGroupSessionRemoveRequestProtobufReadFrom
+ __MRGroupSessionTokenProtobufReadFrom
+ __MRMediaRemotePlaybackDidTimeoutNotification
+ __OBJC_$_CLASS_METHODS_MRGroupSessionHostInfo
+ __OBJC_$_CLASS_METHODS__MRGroupSessionJoinRequestProtobuf
+ __OBJC_$_CLASS_PROP_LIST_MRGroupSessionHostInfo
+ __OBJC_$_INSTANCE_METHODS_MRGroupSessionHostInfo
+ __OBJC_$_INSTANCE_METHODS__MRGroupSessionJoinResponseMessageProtobuf
+ __OBJC_$_INSTANCE_METHODS__MRGroupSessionRemoveRequestProtobuf
+ __OBJC_$_INSTANCE_METHODS__MRGroupSessionTokenProtobuf
+ __OBJC_$_INSTANCE_VARIABLES_MRGroupSessionHostInfo
+ __OBJC_$_INSTANCE_VARIABLES__MRGroupSessionJoinResponseMessageProtobuf
+ __OBJC_$_INSTANCE_VARIABLES__MRGroupSessionRemoveRequestProtobuf
+ __OBJC_$_INSTANCE_VARIABLES__MRGroupSessionTokenProtobuf
+ __OBJC_$_PROP_LIST_MRGroupSessionHostInfo
+ __OBJC_$_PROP_LIST__MRGroupSessionJoinResponseMessageProtobuf
+ __OBJC_$_PROP_LIST__MRGroupSessionRemoveRequestProtobuf
+ __OBJC_$_PROP_LIST__MRGroupSessionTokenProtobuf
+ __OBJC_CLASS_PROTOCOLS_$_MRGroupSessionHostInfo
+ __OBJC_CLASS_PROTOCOLS_$__MRGroupSessionJoinResponseMessageProtobuf
+ __OBJC_CLASS_PROTOCOLS_$__MRGroupSessionRemoveRequestProtobuf
+ __OBJC_CLASS_PROTOCOLS_$__MRGroupSessionTokenProtobuf
+ __OBJC_CLASS_RO_$_MRGroupSessionHostInfo
+ __OBJC_CLASS_RO_$__MRGroupSessionJoinResponseMessageProtobuf
+ __OBJC_CLASS_RO_$__MRGroupSessionRemoveRequestProtobuf
+ __OBJC_CLASS_RO_$__MRGroupSessionTokenProtobuf
+ __OBJC_METACLASS_RO_$_MRGroupSessionHostInfo
+ __OBJC_METACLASS_RO_$__MRGroupSessionJoinResponseMessageProtobuf
+ __OBJC_METACLASS_RO_$__MRGroupSessionRemoveRequestProtobuf
+ __OBJC_METACLASS_RO_$__MRGroupSessionTokenProtobuf
+ ___105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke.529
+ ___105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke.531
+ ___105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke.536
+ ___105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke.545
+ ___105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke_2.532
+ ___121-[MRAVEndpoint migrateToEndpointOrModifyTopology:migrationRequest:topologyModificationRequest:withReplyQueue:completion:]_block_invoke
+ ___122-[MRAVEndpoint willStartingPlaybackToOutputDevicesInterruptPlayback:originatingOutputDeviceUID:duration:queue:completion:]_block_invoke.508
+ ___122-[MRAVEndpoint willStartingPlaybackToOutputDevicesInterruptPlayback:originatingOutputDeviceUID:duration:queue:completion:]_block_invoke.518
+ ___122-[MRDistantExternalDevice _onSerialQueue_prepareToConnectWithOptions:userInfo:connectionAttemptDetails:connectionHandler:]_block_invoke.280
+ ___122-[MRDistantExternalDevice _onSerialQueue_prepareToConnectWithOptions:userInfo:connectionAttemptDetails:connectionHandler:]_block_invoke_2.281
+ ___37-[MRDistantExternalDevice deviceInfo]_block_invoke.223
+ ___37-[MRDistantExternalDevice deviceInfo]_block_invoke_2.224
+ ___39-[MRDistantExternalDevice customOrigin]_block_invoke.227
+ ___39-[MRDistantExternalDevice customOrigin]_block_invoke_2.229
+ ___44-[MRDistantExternalDevice groupSessionToken]_block_invoke
+ ___44-[MRDistantExternalDevice groupSessionToken]_block_invoke.221
+ ___44-[MRDistantExternalDevice groupSessionToken]_block_invoke_2
+ ___44-[MRDistantExternalDevice groupSessionToken]_block_invoke_3
+ ___48-[MRDistantExternalDevice externalOutputContext]_block_invoke.218
+ ___48-[MRDistantExternalDevice personalOutputDevices]_block_invoke.298
+ ___49-[MRRemoteControlGroupSession parseInitialState:]_block_invoke
+ ___51-[MRGroupSessionXPCConnection initializeConnection]_block_invoke.58
+ ___52-[MRAVEndpoint outputDeviceVolume:queue:completion:]_block_invoke.413
+ ___54-[MRRemoteControlGroupSession session:didChangeState:]_block_invoke.338
+ ___54-[NSArray(MRAVAdditions) mr_containsVideoOutputDevice]_block_invoke
+ ___56-[MRRemoteControlGroupSession session:didUpdateMembers:]_block_invoke.341
+ ___57-[MRAVEndpoint outputDeviceVolumeMuted:queue:completion:]_block_invoke.438
+ ___60-[MRRemoteControlGroupSession removeParticipant:completion:]_block_invoke.327
+ ___60-[MRRemoteControlGroupSession removeParticipant:completion:]_block_invoke.327.cold.1
+ ___60-[MRRemoteControlGroupSession removeParticipant:completion:]_block_invoke.328
+ ___61-[MRRemoteControlGroupSession session:didUpdateParticipants:]_block_invoke.339
+ ___62-[MRRemoteControlGroupSession session:didInvalidateWithError:]_block_invoke.345
+ ___65-[MRDistantExternalDevice hostedExternalDeviceEndpointDidChange:]_block_invoke.302
+ ___65-[MRRemoteControlGroupSession denyPendingParticipant:completion:]_block_invoke.318
+ ___65-[MRRemoteControlGroupSession denyPendingParticipant:completion:]_block_invoke.318.cold.1
+ ___65-[MRRemoteControlGroupSession denyPendingParticipant:completion:]_block_invoke.319
+ ___66-[MRDistantExternalDevice connectWithOptions:userInfo:completion:]_block_invoke.264
+ ___66-[MRDistantExternalDevice hostedExternalDeviceDidAddOutputDevice:]_block_invoke.307
+ ___66-[MRRemoteControlGroupSession session:didConnectWithInitialState:]_block_invoke
+ ___67+[MRAVEndpoint directEndpointForOutputDeviceUIDs:queue:completion:]_block_invoke.481
+ ___67+[MRAVEndpoint hostedEndpointForOutputDeviceUIDs:queue:completion:]_block_invoke.474
+ ___67-[MRDistantExternalDevice hostedExternalDeviceDeviceInfoDidChange:]_block_invoke.300
+ ___67-[MRRemoteControlGroupSession assertSessionManagementScreenVisible]_block_invoke.323
+ ___67-[MRRemoteControlGroupSession assertSessionManagementScreenVisible]_block_invoke.326
+ ___67-[MRRemoteControlGroupSession assertSessionManagementScreenVisible]_block_invoke.326.cold.1
+ ___68-[MRAVEndpoint performMigrationToEndpoint:request:queue:completion:]_block_invoke.356
+ ___68-[MRAVEndpoint performMigrationToEndpoint:request:queue:completion:]_block_invoke.364
+ ___68-[MRRemoteControlGroupSession approvePendingParticipant:completion:]_block_invoke.312
+ ___68-[MRRemoteControlGroupSession approvePendingParticipant:completion:]_block_invoke.312.cold.1
+ ___68-[MRRemoteControlGroupSession approvePendingParticipant:completion:]_block_invoke.314
+ ___68-[MRRemoteControlGroupSession session:didUpdatePendingParticipants:]_block_invoke.340
+ ___69-[MRDistantExternalDevice hostedExternalDeviceDidChangeOutputDevice:]_block_invoke.308
+ ___69-[MRDistantExternalDevice hostedExternalDeviceDidRemoveOutputDevice:]_block_invoke.309
+ ___69-[MRRemoteControlGroupSession session:didUpdateSynchronizedMetadata:]_block_invoke.344
+ ___71-[MRAVEndpoint outputDeviceVolumeControlCapabilities:queue:completion:]_block_invoke.399
+ ___71-[MRAVOutputContextModification _notifyWillAddDevices:toOutputContext:]_block_invoke.183
+ ___74-[MRDistantExternalDevice hostedExternalDeviceGroupSessionTokenDidChange:]_block_invoke
+ ___74-[MRDistantExternalDevice hostedExternalDeviceGroupSessionTokenDidChange:]_block_invoke.310
+ ___74-[MRDistantExternalDevice hostedExternalDeviceGroupSessionTokenDidChange:]_block_invoke_2
+ ___76+[MRAVEndpoint createEndpointWithOutputDeviceUIDs:options:queue:completion:]_block_invoke.488
+ ___76+[MRAVEndpoint createEndpointWithOutputDeviceUIDs:options:queue:completion:]_block_invoke.492
+ ___76-[MRAVEndpoint setOutputDeviceVolume:outputDevice:details:queue:completion:]_block_invoke.409
+ ___76-[MRAVOutputContextModification _notifyRequestToAddDevices:toOutputContext:]_block_invoke.176
+ ___76-[MRAVOutputContextModification _notifyWillRemoveDevices:fromOutputContext:]_block_invoke.197
+ ___77-[MRAVEndpoint muteOutputDeviceVolume:outputDevice:details:queue:completion:]_block_invoke.434
+ ___77-[MRDistantExternalDevice hostedExternalDeviceDidReceiveCustomData:withName:]_block_invoke.301
+ ___79-[MRAVEndpoint adjustOutputDeviceVolume:outputDevice:details:queue:completion:]_block_invoke.421
+ ___79-[MRDistantExternalDevice hostedExternalDeviceVolumeDidChange:forOutputDevice:]_block_invoke.305
+ ___80-[MRAVEndpoint migrateToOrAddOutputDevices:initiator:withReplyQueue:completion:]_block_invoke.188
+ ___80-[MRAVEndpoint migrateToOrAddOutputDevices:initiator:withReplyQueue:completion:]_block_invoke.198
+ ___80-[MRAVEndpoint migrateToOrSetOutputDevices:initiator:withReplyQueue:completion:]_block_invoke.207
+ ___80-[MRDistantExternalDevice hostedExternalDeviceIsMutedDidChange:forOutputDevice:]_block_invoke.306
+ ___81-[MRAVOutputContextModification _notifyRequestToRemoveDevices:fromOutputContext:]_block_invoke.190
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.228
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.232
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.241
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.248
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.275
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.279
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.286
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.297
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.315
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.325
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.344
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_2.233
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_2.252
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_2.280
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_2.290
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_2.304
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_2.328
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_2.351
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_3.259
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_3.305
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_3.331
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_4.262
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_4.333
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_5.263
+ ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_5.334
+ ___86+[MRAVEndpoint connectToEndpointContainingOutputDeviceUID:options:details:completion:]_block_invoke
+ ___86+[MRAVEndpoint connectToEndpointContainingOutputDeviceUID:options:details:completion:]_block_invoke.180
+ ___86+[MRAVEndpoint connectToEndpointContainingOutputDeviceUID:options:details:completion:]_block_invoke.cold.1
+ ___86+[MRAVEndpoint connectToEndpointContainingOutputDeviceUID:options:details:completion:]_block_invoke_2
+ ___87-[MRAVOutputContextModification performModificationWithOutputContext:queue:completion:]_block_invoke.123
+ ___87-[MRAVOutputContextModification performModificationWithOutputContext:queue:completion:]_block_invoke.129
+ ___87-[MRAVOutputContextModification performModificationWithOutputContext:queue:completion:]_block_invoke.137
+ ___87-[MRAVOutputContextModification performModificationWithOutputContext:queue:completion:]_block_invoke.143
+ ___87-[MRAVOutputContextModification performModificationWithOutputContext:queue:completion:]_block_invoke.162
+ ___87-[MRAVOutputContextModification performModificationWithOutputContext:queue:completion:]_block_invoke_2.138
+ ___87-[MRAVOutputContextModification performModificationWithOutputContext:queue:completion:]_block_invoke_2.153
+ ___87-[MRAVOutputContextModification performModificationWithOutputContext:queue:completion:]_block_invoke_2.163
+ ___87-[MRAVOutputContextModification performModificationWithOutputContext:queue:completion:]_block_invoke_3.155
+ ___90-[MRDistantExternalDevice setOutputDeviceVolume:outputDeviceUID:details:queue:completion:]_block_invoke.287
+ ___91-[MRDistantExternalDevice hostedExternalDeviceVolumeCapabilitiesDidChange:forOutputDevice:]_block_invoke.304
+ ___91-[MRDistantExternalDevice muteOutputDeviceVolume:outputDeviceUID:details:queue:completion:]_block_invoke.296
+ ___93-[MRDistantExternalDevice adjustOutputDeviceVolume:outputDeviceUID:details:queue:completion:]_block_invoke.292
+ ___MRGroupSessionJoinSessionWithToken_block_invoke.267
+ ___MRGroupSessionJoinSessionWithToken_block_invoke.271
+ ___block_descriptor_40_e8_32s_e29_v16?0"MRGroupSessionToken"8ls32l8
+ ___block_descriptor_64_e8_32s40s48bs56r_e34_v24?0"MRAVEndpoint"8"NSError"16ls32l8s48l8s40l8r56l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e17_v16?0"NSError"8ls56l8s32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e34_v24?0"MRAVEndpoint"8"NSError"16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48bs56r64r_e5_v8?0lr56l8s32l8r64l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48bs56r64r_e5_v8?0ls48l8s32l8s40l8r56l8r64l8
+ ___block_descriptor_72_e8_32s40s48s56bs64r_e5_v8?0ls56l8s32l8s40l8s48l8r64l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72bs80r_e34_v24?0"MRAVEndpoint"8"NSError"16ls32l8s40l8s48l8s56l8s72l8s64l8r80l8
+ ___block_descriptor_96_e8_32s40s48s56s64bs72r80r88r_e34_v24?0"MRAVEndpoint"8"NSError"16lr72l8s32l8s40l8s48l8s56l8s64l8r80l8r88l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72bs80r88r_e34_v24?0"MRAVEndpoint"8"NSError"16lr80l8s32l8s40l8s48l8s56l8s72l8s64l8r88l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80bs88r_e34_v24?0"MRAVEndpoint"8"NSError"16ls32l8s40l8s48l8s56l8s64l8s80l8s72l8r88l8
+ ___block_literal_global.118
+ ___block_literal_global.180
+ ___block_literal_global.187
+ ___block_literal_global.19
+ ___block_literal_global.192
+ ___block_literal_global.194
+ ___block_literal_global.199
+ ___block_literal_global.200
+ ___block_literal_global.21
+ ___block_literal_global.214
+ ___block_literal_global.235
+ ___block_literal_global.243
+ ___block_literal_global.282
+ ___block_literal_global.300
+ ___block_literal_global.318
+ ___block_literal_global.327
+ ___block_literal_global.330
+ ___block_literal_global.336
+ ___block_literal_global.346
+ ___block_literal_global.366
+ ___block_literal_global.441
+ ___block_literal_global.528
+ _classINPrivatePlayMediaIntentData
+ _constantValAVOutputContextAddOutputDeviceOptionMuteUntilContextModificationIsFinished
+ _constantValAVOutputContextSetOutputDeviceMuteUntilContextModificationIsFinishedKey
+ _constantValAVOutputContextSetOutputDevicesOptionMuteUntilContextModificationIsFinished
+ _getAVOutputContextAddOutputDeviceOptionMuteUntilContextModificationIsFinished
+ _getAVOutputContextSetOutputDeviceMuteUntilContextModificationIsFinishedKey
+ _getAVOutputContextSetOutputDevicesOptionMuteUntilContextModificationIsFinished
+ _getINPrivatePlayMediaIntentDataClass
+ _initINPrivatePlayMediaIntentData
+ _initValAVOutputContextAddOutputDeviceOptionMuteUntilContextModificationIsFinished
+ _initValAVOutputContextSetOutputDeviceMuteUntilContextModificationIsFinishedKey
+ _initValAVOutputContextSetOutputDevicesOptionMuteUntilContextModificationIsFinished
+ _objc_msgSend$_notifyGroupSessionInfoDidChange:endpoint:
+ _objc_msgSend$actionImageName
+ _objc_msgSend$addOobKeys:
+ _objc_msgSend$addPendingParticipants:
+ _objc_msgSend$alternativeProviderBundleIdentifier
+ _objc_msgSend$ampPAFDataSetID
+ _objc_msgSend$appInferred
+ _objc_msgSend$appSelectionEnabled
+ _objc_msgSend$appSelectionSignalsEnabled
+ _objc_msgSend$appSelectionSignalsFrequencyDenominator
+ _objc_msgSend$audioSearchResults
+ _objc_msgSend$clearOobKeys
+ _objc_msgSend$clearPendingParticipants
+ _objc_msgSend$connectToExternalDeviceWithOptions:details:completion:
+ _objc_msgSend$createTokenWithInvitationData:equivalentMediaIdentifier:
+ _objc_msgSend$demoteWhenSyncingToCompanion
+ _objc_msgSend$devicePlaybackSessionID
+ _objc_msgSend$disableDuration
+ _objc_msgSend$entityConfidenceSignalsEnabled
+ _objc_msgSend$entityConfidenceSignalsFrequencyDenominatorInternal
+ _objc_msgSend$entityConfidenceSignalsFrequencyDenominatorProd
+ _objc_msgSend$entityConfidenceSignalsMaxItemsToDisambiguate
+ _objc_msgSend$equivalentMediaIdentifier
+ _objc_msgSend$getGroupSessionTokenWithCompletion:
+ _objc_msgSend$groupSessionToken
+ _objc_msgSend$hasRenderingMode
+ _objc_msgSend$immediatelyStartPlayback
+ _objc_msgSend$initWithAppSelectionEnabled:appInferred:audioSearchResults:privateMediaIntentData:appSelectionSignalsEnabled:appSelectionSignalsFrequencyDenominator:shouldSuppressCommonWholeHouseAudioRoutes:immediatelyStartPlayback:isAmbiguousPlay:isPersonalizedRequest:internalSignals:entityConfidenceSignalsEnabled:entityConfidenceSignalsFrequencyDenominatorInternal:entityConfidenceSignalsFrequencyDenominatorProd:entityConfidenceSignalsMaxItemsToDisambiguate:alternativeProviderBundleIdentifier:ampPAFDataSetID:
+ _objc_msgSend$initWithHostInfo:invitationData:sharedSecret:sessionIdentifier:equivalentMediaIdentifier:
+ _objc_msgSend$initWithIdentifier:hostInfo:
+ _objc_msgSend$initWithIdentifier:hostInfo:isHosted:equivalentMediaIdentifier:
+ _objc_msgSend$initWithRouteType:displayName:
+ _objc_msgSend$initWithToken:isHosted:
+ _objc_msgSend$internalSignals
+ _objc_msgSend$isAmbiguousPlay
+ _objc_msgSend$isGuest
+ _objc_msgSend$isMostRecentMediaPlaybackRelevantReasonWithinInternal:
+ _objc_msgSend$isPersonalizedRequest
+ _objc_msgSend$muteUntilFinished
+ _objc_msgSend$oobKeysAtIndex:
+ _objc_msgSend$oobKeysCount
+ _objc_msgSend$parseInitialState:
+ _objc_msgSend$pendingParticipantsAtIndex:
+ _objc_msgSend$pendingParticipantsCount
+ _objc_msgSend$privateMediaIntentData
+ _objc_msgSend$privatePlayMediaIntentData
+ _objc_msgSend$renderingMode
+ _objc_msgSend$requestReasonID
+ _objc_msgSend$sessionIdentifier
+ _objc_msgSend$setActionImageName:
+ _objc_msgSend$setDemoteWhenSyncingToCompanion:
+ _objc_msgSend$setDevicePlaybackSessionID:
+ _objc_msgSend$setDisableDuration:
+ _objc_msgSend$setEquivalentMediaIdentifier:
+ _objc_msgSend$setGroupSessionToken:
+ _objc_msgSend$setGuest:
+ _objc_msgSend$setInvitationData:
+ _objc_msgSend$setMuteUntilFinished:
+ _objc_msgSend$setPrivatePlayMediaIntentData:
+ _objc_msgSend$setRenderingMode:
+ _objc_msgSend$setSessionIdentifier:
+ _objc_msgSend$setSharedSecret:
+ _objc_msgSend$sharedSecret
+ _objc_msgSend$shouldOmitHost
+ _objc_msgSend$supportGroupSessionHome
+ _objc_msgSend$supportNowPlayingPIP
- +[MRGroupSessionPersonInformation supportsSecureCoding]
- +[MRNearbyInvitation supportsSecureCoding]
- +[MRNowPlayingRequest isMostRecentMediaPlaybackRelevant]
- -[MRAVEndpoint migrateToEndpointOrSetOutputDevices:request:queue:completion:]
- -[MRDiscoveredGroupSession initWithIdentifier:hostInfo:routeType:]
- -[MRDiscoveredGroupSession routeType]
- -[MRGroupSessionInfo initWithIdentifier:hostInfo:routeType:isHosted:]
- -[MRGroupSessionInfo routeType]
- -[MRGroupSessionPersonInformation .cxx_destruct]
- -[MRGroupSessionPersonInformation displayImageData]
- -[MRGroupSessionPersonInformation displayName]
- -[MRGroupSessionPersonInformation encodeWithCoder:]
- -[MRGroupSessionPersonInformation initWithCoder:]
- -[MRGroupSessionPersonInformation initWithDisplayName:displayImageData:]
- -[MRGroupSessionPersonInformation setDisplayImageData:]
- -[MRGroupSessionPersonInformation setDisplayName:]
- -[MRGroupSessionToken initWithInvitation:invitationData:]
- -[MRGroupSessionToken invitation]
- -[MRMediaRemoteService createTokenWithInvitationData:]
- -[MRNearbyInvitation .cxx_destruct]
- -[MRNearbyInvitation description]
- -[MRNearbyInvitation displayName]
- -[MRNearbyInvitation encodeWithCoder:]
- -[MRNearbyInvitation hash]
- -[MRNearbyInvitation initWithCoder:]
- -[MRNearbyInvitation isEqual:]
- -[MRNearbyInvitation localizedSessionName]
- -[MRNearbyInvitation routeType]
- -[MRNearbyInvitation setDisplayName:]
- -[MRNearbyInvitation setLocalizedSessionName:]
- -[MRNearbyInvitation setRouteType:]
- -[MROriginClientPropertiesMessage initWithLastPlayingDate:]
- -[_MRMediaRemoteMessageProtobuf hasIdentifier]
- -[_MRMediaRemoteMessageProtobuf identifier]
- -[_MRMediaRemoteMessageProtobuf setIdentifier:]
- GCC_except_table109
- GCC_except_table183
- GCC_except_table196
- GCC_except_table197
- GCC_except_table248
- GCC_except_table74
- OBJC_IVAR_$__MRMediaRemoteMessageProtobuf._identifier
- _OBJC_CLASS_$_MRGroupSessionPersonInformation
- _OBJC_CLASS_$_MRNearbyInvitation
- _OBJC_IVAR_$_MRDiscoveredGroupSession._routeType
- _OBJC_IVAR_$_MRGroupSessionInfo._routeType
- _OBJC_IVAR_$_MRGroupSessionPersonInformation._displayImageData
- _OBJC_IVAR_$_MRGroupSessionPersonInformation._displayName
- _OBJC_IVAR_$_MRGroupSessionToken._invitation
- _OBJC_IVAR_$_MRNearbyInvitation._displayName
- _OBJC_IVAR_$_MRNearbyInvitation._localizedSessionName
- _OBJC_IVAR_$_MRNearbyInvitation._routeType
- _OBJC_METACLASS_$_MRGroupSessionPersonInformation
- _OBJC_METACLASS_$_MRNearbyInvitation
- __OBJC_$_CLASS_METHODS_MRGroupSessionPersonInformation
- __OBJC_$_CLASS_METHODS_MRNearbyInvitation
- __OBJC_$_CLASS_PROP_LIST_MRGroupSessionPersonInformation
- __OBJC_$_CLASS_PROP_LIST_MRNearbyInvitation
- __OBJC_$_INSTANCE_METHODS_MRGroupSessionPersonInformation
- __OBJC_$_INSTANCE_METHODS_MRNearbyInvitation
- __OBJC_$_INSTANCE_VARIABLES_MRGroupSessionPersonInformation
- __OBJC_$_INSTANCE_VARIABLES_MRNearbyInvitation
- __OBJC_$_PROP_LIST_MRGroupSessionPersonInformation
- __OBJC_$_PROP_LIST_MRNearbyInvitation
- __OBJC_CLASS_PROTOCOLS_$_MRGroupSessionPersonInformation
- __OBJC_CLASS_PROTOCOLS_$_MRNearbyInvitation
- __OBJC_CLASS_RO_$_MRGroupSessionPersonInformation
- __OBJC_CLASS_RO_$_MRNearbyInvitation
- __OBJC_METACLASS_RO_$_MRGroupSessionPersonInformation
- __OBJC_METACLASS_RO_$_MRNearbyInvitation
- ___105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke.516
- ___105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke.518
- ___105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke.523
- ___105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke.532
- ___105-[MRAVEndpoint _willStartingPlaybackToOutputDeviceInterruptPlayback:duration:requestID:queue:completion:]_block_invoke_2.519
- ___122-[MRAVEndpoint willStartingPlaybackToOutputDevicesInterruptPlayback:originatingOutputDeviceUID:duration:queue:completion:]_block_invoke.495
- ___122-[MRAVEndpoint willStartingPlaybackToOutputDevicesInterruptPlayback:originatingOutputDeviceUID:duration:queue:completion:]_block_invoke.505
- ___122-[MRDistantExternalDevice _onSerialQueue_prepareToConnectWithOptions:userInfo:connectionAttemptDetails:connectionHandler:]_block_invoke.270
- ___122-[MRDistantExternalDevice _onSerialQueue_prepareToConnectWithOptions:userInfo:connectionAttemptDetails:connectionHandler:]_block_invoke_2.271
- ___37-[MRDistantExternalDevice deviceInfo]_block_invoke.213
- ___37-[MRDistantExternalDevice deviceInfo]_block_invoke_2.214
- ___39-[MRDistantExternalDevice customOrigin]_block_invoke.217
- ___39-[MRDistantExternalDevice customOrigin]_block_invoke_2.219
- ___48-[MRDistantExternalDevice externalOutputContext]_block_invoke.210
- ___48-[MRDistantExternalDevice personalOutputDevices]_block_invoke.288
- ___51-[MRGroupSessionXPCConnection initializeConnection]_block_invoke.55
- ___51-[MRRemoteControlGroupSession initializeConnection]_block_invoke.261
- ___52-[MRAVEndpoint outputDeviceVolume:queue:completion:]_block_invoke.400
- ___54-[MRRemoteControlGroupSession session:didChangeState:]_block_invoke.294
- ___56-[MRRemoteControlGroupSession session:didUpdateMembers:]_block_invoke.297
- ___57-[MRAVEndpoint outputDeviceVolumeMuted:queue:completion:]_block_invoke.425
- ___60-[MRRemoteControlGroupSession removeParticipant:completion:]_block_invoke.291
- ___60-[MRRemoteControlGroupSession removeParticipant:completion:]_block_invoke.291.cold.1
- ___60-[MRRemoteControlGroupSession removeParticipant:completion:]_block_invoke.292
- ___61-[MRRemoteControlGroupSession session:didUpdateParticipants:]_block_invoke.295
- ___62-[MRRemoteControlGroupSession session:didInvalidateWithError:]_block_invoke.301
- ___65-[MRDistantExternalDevice hostedExternalDeviceEndpointDidChange:]_block_invoke.292
- ___65-[MRRemoteControlGroupSession denyPendingParticipant:completion:]_block_invoke.282
- ___65-[MRRemoteControlGroupSession denyPendingParticipant:completion:]_block_invoke.282.cold.1
- ___65-[MRRemoteControlGroupSession denyPendingParticipant:completion:]_block_invoke.283
- ___66-[MRDistantExternalDevice connectWithOptions:userInfo:completion:]_block_invoke.254
- ___66-[MRDistantExternalDevice hostedExternalDeviceDidAddOutputDevice:]_block_invoke.297
- ___67+[MRAVEndpoint directEndpointForOutputDeviceUIDs:queue:completion:]_block_invoke.468
- ___67+[MRAVEndpoint hostedEndpointForOutputDeviceUIDs:queue:completion:]_block_invoke.461
- ___67-[MRDistantExternalDevice hostedExternalDeviceDeviceInfoDidChange:]_block_invoke.290
- ___67-[MRRemoteControlGroupSession assertSessionManagementScreenVisible]_block_invoke.287
- ___67-[MRRemoteControlGroupSession assertSessionManagementScreenVisible]_block_invoke.290
- ___67-[MRRemoteControlGroupSession assertSessionManagementScreenVisible]_block_invoke.290.cold.1
- ___68-[MRAVEndpoint performMigrationToEndpoint:request:queue:completion:]_block_invoke.343
- ___68-[MRAVEndpoint performMigrationToEndpoint:request:queue:completion:]_block_invoke.351
- ___68-[MRRemoteControlGroupSession approvePendingParticipant:completion:]_block_invoke.276
- ___68-[MRRemoteControlGroupSession approvePendingParticipant:completion:]_block_invoke.276.cold.1
- ___68-[MRRemoteControlGroupSession approvePendingParticipant:completion:]_block_invoke.278
- ___68-[MRRemoteControlGroupSession session:didUpdatePendingParticipants:]_block_invoke.296
- ___69-[MRDistantExternalDevice hostedExternalDeviceDidChangeOutputDevice:]_block_invoke.298
- ___69-[MRDistantExternalDevice hostedExternalDeviceDidRemoveOutputDevice:]_block_invoke.299
- ___69-[MRRemoteControlGroupSession session:didUpdateSynchronizedMetadata:]_block_invoke.300
- ___71-[MRAVEndpoint outputDeviceVolumeControlCapabilities:queue:completion:]_block_invoke.386
- ___71-[MRAVOutputContextModification _notifyWillAddDevices:toOutputContext:]_block_invoke.180
- ___76+[MRAVEndpoint createEndpointWithOutputDeviceUIDs:options:queue:completion:]_block_invoke.475
- ___76+[MRAVEndpoint createEndpointWithOutputDeviceUIDs:options:queue:completion:]_block_invoke.479
- ___76-[MRAVEndpoint setOutputDeviceVolume:outputDevice:details:queue:completion:]_block_invoke.396
- ___76-[MRAVOutputContextModification _notifyRequestToAddDevices:toOutputContext:]_block_invoke.173
- ___76-[MRAVOutputContextModification _notifyWillRemoveDevices:fromOutputContext:]_block_invoke.194
- ___77-[MRAVEndpoint migrateToEndpointOrSetOutputDevices:request:queue:completion:]_block_invoke
- ___77-[MRAVEndpoint migrateToEndpointOrSetOutputDevices:request:queue:completion:]_block_invoke_2
- ___77-[MRAVEndpoint migrateToEndpointOrSetOutputDevices:request:queue:completion:]_block_invoke_3
- ___77-[MRAVEndpoint muteOutputDeviceVolume:outputDevice:details:queue:completion:]_block_invoke.421
- ___77-[MRDistantExternalDevice hostedExternalDeviceDidReceiveCustomData:withName:]_block_invoke.291
- ___79-[MRAVEndpoint adjustOutputDeviceVolume:outputDevice:details:queue:completion:]_block_invoke.408
- ___79-[MRDistantExternalDevice hostedExternalDeviceVolumeDidChange:forOutputDevice:]_block_invoke.295
- ___80-[MRAVEndpoint migrateToOrAddOutputDevices:initiator:withReplyQueue:completion:]_block_invoke.166
- ___80-[MRAVEndpoint migrateToOrAddOutputDevices:initiator:withReplyQueue:completion:]_block_invoke.176
- ___80-[MRAVEndpoint migrateToOrSetOutputDevices:initiator:withReplyQueue:completion:]_block_invoke.185
- ___80-[MRDistantExternalDevice hostedExternalDeviceIsMutedDidChange:forOutputDevice:]_block_invoke.296
- ___81-[MRAVOutputContextModification _notifyRequestToRemoveDevices:fromOutputContext:]_block_invoke.187
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.213
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.217
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.226
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.233
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.262
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.266
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.273
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.284
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.302
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.312
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke.331
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_2.218
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_2.238
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_2.267
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_2.277
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_2.291
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_2.315
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_2.338
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_3.245
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_3.292
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_3.318
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_4.249
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_4.320
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_5.250
- ___83-[MRAVEndpoint performMigrationToOutputDevices:request:initiator:queue:completion:]_block_invoke_5.321
- ___87-[MRAVOutputContextModification performModificationWithOutputContext:queue:completion:]_block_invoke.120
- ___87-[MRAVOutputContextModification performModificationWithOutputContext:queue:completion:]_block_invoke.126
- ___87-[MRAVOutputContextModification performModificationWithOutputContext:queue:completion:]_block_invoke.134
- ___87-[MRAVOutputContextModification performModificationWithOutputContext:queue:completion:]_block_invoke.140
- ___87-[MRAVOutputContextModification performModificationWithOutputContext:queue:completion:]_block_invoke.158
- ___87-[MRAVOutputContextModification performModificationWithOutputContext:queue:completion:]_block_invoke_2.135
- ___87-[MRAVOutputContextModification performModificationWithOutputContext:queue:completion:]_block_invoke_2.150
- ___87-[MRAVOutputContextModification performModificationWithOutputContext:queue:completion:]_block_invoke_2.159
- ___90-[MRDistantExternalDevice setOutputDeviceVolume:outputDeviceUID:details:queue:completion:]_block_invoke.277
- ___91-[MRDistantExternalDevice hostedExternalDeviceVolumeCapabilitiesDidChange:forOutputDevice:]_block_invoke.294
- ___91-[MRDistantExternalDevice muteOutputDeviceVolume:outputDeviceUID:details:queue:completion:]_block_invoke.286
- ___93-[MRDistantExternalDevice adjustOutputDeviceVolume:outputDeviceUID:details:queue:completion:]_block_invoke.282
- ___MRGroupSessionJoinSessionWithToken_block_invoke.224
- ___MRGroupSessionJoinSessionWithToken_block_invoke.228
- ___block_descriptor_64_e8_32s40bs48r56r_e5_v8?0lr48l8s32l8r56l8s40l8
- ___block_descriptor_64_e8_32s40s48bs56r_e34_v24?0"MRAVEndpoint"8"NSError"16ls32l8r56l8s48l8s40l8
- ___block_descriptor_88_e8_32s40s48s56s64s72bs80r_e34_v24?0"MRAVEndpoint"8"NSError"16ls32l8s40l8s48l8s56l8r80l8s72l8s64l8
- ___block_descriptor_96_e8_32s40s48s56s64bs72r80r88r_e34_v24?0"MRAVEndpoint"8"NSError"16lr72l8s32l8s40l8s48l8r80l8r88l8s64l8s56l8
- ___block_descriptor_96_e8_32s40s48s56s64s72bs80r88r_e34_v24?0"MRAVEndpoint"8"NSError"16lr80l8s32l8s40l8s48l8s56l8r88l8s72l8s64l8
- ___block_descriptor_96_e8_32s40s48s56s64s72s80bs88r_e34_v24?0"MRAVEndpoint"8"NSError"16ls32l8s40l8s48l8s56l8s64l8r88l8s80l8s72l8
- ___block_literal_global.16
- ___block_literal_global.172
- ___block_literal_global.177
- ___block_literal_global.179
- ___block_literal_global.184
- ___block_literal_global.186
- ___block_literal_global.191
- ___block_literal_global.193
- ___block_literal_global.232
- ___block_literal_global.242
- ___block_literal_global.269
- ___block_literal_global.276
- ___block_literal_global.287
- ___block_literal_global.305
- ___block_literal_global.314
- ___block_literal_global.317
- ___block_literal_global.323
- ___block_literal_global.333
- ___block_literal_global.353
- ___block_literal_global.428
- ___block_literal_global.480
- _kMRMediaRemoteLocalPlaybackDidTimeoutNotification
- _objc_msgSend$createTokenWithInvitationData:
- _objc_msgSend$initWithIdentifier:hostInfo:routeType:isHosted:
- _objc_msgSend$invitation
- _objc_msgSend$isMostRecentMediaPlaybackRelevantReason
CStrings:
+ "\x021\x12\x13\x12\x11\x17"
+ "\x03\x12"
+ "\b"
+ "\x114"
+ "\x18\x12\x15\x12\x13\x12\x16"
+ " actionImageName: %@"
+ ", id=%@"
+ ", mediaID=%@"
+ ", secret=%@"
+ "-[MRExternalDevice groupSessionToken]"
+ "-[MRExternalDevice setGroupSessionTokenCallback:withQueue:]"
+ "-[_MRGroupSessionJoinResponseMessageProtobuf writeTo:]"
+ "-[_MRGroupSessionRemoveRequestProtobuf writeTo:]"
+ "-[_MRGroupSessionTokenProtobuf writeTo:]"
+ "1\x11\x11"
+ "<%@: identifier=%@, hosted=%@, mediaID=%@>"
+ "<%@: identifier=%@, identity=%@, local=%@, pending=%@, connected=%@, guest=%@>"
+ "<%@:%p %@"
+ "@\"MRGroupSessionHostInfo\""
+ "@\"_MRGroupSessionTokenProtobuf\""
+ "@24@0:8d16"
+ "@28@0:8C16@20"
+ "@44@0:8@16@24B32@36"
+ "AVOutputContextAddOutputDeviceOptionMuteUntilContextModificationIsFinished"
+ "AVOutputContextSetOutputDeviceMuteUntilContextModificationIsFinishedKey"
+ "AVOutputContextSetOutputDevicesOptionMuteUntilContextModificationIsFinished"
+ "AdjustVolume"
+ "AudioFadeResponse"
+ "B24@0:8d16"
+ "ClientUpdatesConfiguration"
+ "ConfigureConnection"
+ "CreatedHostedEndpointRequest"
+ "CreatedHostedEndpointResponse"
+ "CryptoPairing"
+ "DeviceInfo"
+ "DeviceInfoUpdate"
+ "DiscoveryUpdateEndpoints"
+ "DiscoveryUpdateOutputDevices"
+ "DolbyAtmos"
+ "DolbyAudio"
+ "EnableRoutePrediction"
+ "GameController"
+ "GameControllerProperties"
+ "Generic"
+ "GetKeyboardSession"
+ "GetRemoteTextInputSession"
+ "GetState"
+ "GetVoiceInputDevices"
+ "GetVoiceInputDevicesResponse"
+ "GetVolume"
+ "GetVolumeControlCapabilities"
+ "GetVolumeControlCapabilitiesResult"
+ "GetVolumeMuted"
+ "GetVolumeMutedResult"
+ "GetVolumeResult"
+ "INPrivatePlayMediaIntentData"
+ "Keyboard"
+ "LastMessageType"
+ "LegacyVolumeControlCapabilitiesDidChange"
+ "MRAVEndpointGroupSessionInfoDidChangeNotification"
+ "MRAVEndpointGroupSessionInfoUserInfoKey"
+ "MRExternalDeviceGroupSessionTokenDidChangeNotification"
+ "MRExternalDeviceGroupSessionTokenUserInfoKey"
+ "MRGroupSessionHostInfo"
+ "MRGroupSessionToken * _Nonnull MRGroupSessionTokenCreateWithInvitationData(NSData *__strong _Nonnull, NSString * _Nullable __strong)"
+ "MRXPC_GROUP_SESSION_EQUIVALENT_MEDIA_ID_KEY"
+ "ModifyOutputContextRequest"
+ "MonoStereo"
+ "Notification"
+ "PlayDestination"
+ "PlaybackSessionMigrateBegin"
+ "PlaybackSessionMigrateEnd"
+ "PlaybackSessionMigrateRequest"
+ "PlaybackSessionMigrateResponse"
+ "PlaybackSessionRequest"
+ "PlaybackSessionResponse"
+ "PlayerClientParticipantsUpdate"
+ "PresentRouteAuthorizationStatus"
+ "PromptForRouteAuthorization"
+ "PromptForRouteAuthorizationResponse"
+ "RegisterForGameControllerEvents"
+ "RegisterGameController"
+ "RegisterGameControllerResponse"
+ "RegisterHIDDevice"
+ "RegisterHIDDeviceResult"
+ "RegisterVoiceInputDevice"
+ "RegisterVoiceInputDeviceResponse"
+ "RemoteJoinResponse"
+ "RemoteRemoveRequest"
+ "RemoteTextInput"
+ "RemoveClient"
+ "RemoveEndpoints"
+ "RemoveFromParentGroup"
+ "RemoveOutputDevices"
+ "RemovePlayer"
+ "SendButtonEvent"
+ "SendCommand"
+ "SendCommandResult"
+ "SendHIDEvent"
+ "SendHIDReport"
+ "SendLyricsEventMessage"
+ "SendPackedVirtualTouchEvent"
+ "SendVirtualTouchEvent"
+ "SendVoiceInput"
+ "SetArtwork"
+ "SetConnectionState"
+ "SetConversationDetectionEnabled"
+ "SetDefaultSupportedCommands"
+ "SetDiscoveryMode"
+ "SetHiliteMode"
+ "SetListeningMode"
+ "SetNowPlayingClient"
+ "SetNowPlayingPlayer"
+ "SetOriginClientProperties"
+ "SetPlayerClientProperties"
+ "SetReadyState"
+ "SetState"
+ "SetVoiceInputRecordingState"
+ "SetVolume"
+ "SetVolumeMuted"
+ "SpatialAudio"
+ "StringAsRenderingMode:"
+ "T@\"MRGroupSessionHostInfo\",R,N,V_hostInfo"
+ "T@\"MRGroupSessionToken\",C,N,V_groupSessionToken"
+ "T@\"NSData\",&,N,V_invitationData"
+ "T@\"NSMutableArray\",&,N,V_oobKeys"
+ "T@\"NSMutableArray\",&,N,V_pendingParticipants"
+ "T@\"NSString\",&,N,V_actionImageName"
+ "T@\"NSString\",&,N,V_devicePlaybackSessionID"
+ "T@\"NSString\",&,N,V_equivalentMediaIdentifier"
+ "T@\"NSString\",&,N,V_replyIdentifier"
+ "T@\"NSString\",&,N,V_sessionIdentifier"
+ "T@\"NSString\",&,N,V_sharedSecret"
+ "T@\"NSString\",R,N,V_effectiveIdentifier"
+ "T@\"NSString\",R,N,V_equivalentMediaIdentifier"
+ "T@\"NSString\",R,N,V_sessionIdentifier"
+ "T@\"NSString\",R,N,V_sharedSecret"
+ "T@\"_MRGroupSessionTokenProtobuf\",&,N,V_groupSessionToken"
+ "T@\"_MRGroupSessionTokenProtobuf\",R,N"
+ "TB,N,GisGuest,V_guest"
+ "TB,N,V_approved"
+ "TB,N,V_demoteWhenSyncingToCompanion"
+ "TB,N,V_guest"
+ "TB,N,V_muteUntilFinished"
+ "TB,R,N,GisGuest"
+ "TB,R,N,GisLockScreenAffordanceAllowed"
+ "TB,R,N,V_hasRenderingMode"
+ "Td,N,V_disableDuration"
+ "TextInput"
+ "Ti,N,V_renderingMode"
+ "Tq,N,V_renderingMode"
+ "UnregisterGameController"
+ "UpdateActiveSystemEndpoint"
+ "UpdateClient"
+ "UpdateContentItemArtwork"
+ "UpdateContentItems"
+ "UpdateEndpoints"
+ "UpdateOutputDevices"
+ "UpdatePlayer"
+ "VolumeControlCapabilitiesDidChange"
+ "VolumeDidChange"
+ "VolumeMutedDidChange"
+ "WakeDevice"
+ "[MRDistantExternalDevice] Distant external device %{public}@ failed to fetch groupSessionToken: %{public}@"
+ "[MRDistantExternalDevice] Hosted external device connection for distant device %p did change groupSession token %{public}@ for endpoint %{public}@"
+ "[MRDistantExternalDevice] [debug] %@ NOTIFICATION HACK FOR MUSIC with: %@"
+ "[MRGroupSession] <%p> Connected after initialization"
+ "_MRGroupSessionJoinResponseMessageProtobuf"
+ "_MRGroupSessionJoinResponseMessageProtobuf.m"
+ "_MRGroupSessionRemoveRequestProtobuf"
+ "_MRGroupSessionRemoveRequestProtobuf.m"
+ "_MRGroupSessionTokenProtobuf"
+ "_MRGroupSessionTokenProtobuf.m"
+ "_MRMediaRemotePlaybackDidTimeoutNotification"
+ "_actionImageName"
+ "_approved"
+ "_demoteWhenSyncingToCompanion"
+ "_devicePlaybackSessionID"
+ "_disableDuration"
+ "_effectiveIdentifier"
+ "_equivalentMediaIdentifier"
+ "_groupSessionToken"
+ "_guest"
+ "_handleGroupSessionTokenDidChangeNotification:"
+ "_hasFetchedGroupSessionInfo"
+ "_hasRenderingMode"
+ "_muteUntilFinished"
+ "_notifyGroupSessionInfoDidChange:endpoint:"
+ "_oobKeys"
+ "_renderingMode"
+ "_sessionIdentifier"
+ "_sharedSecret"
+ "actionImageName"
+ "addOobKeys:"
+ "addPendingParticipants:"
+ "ain"
+ "alternativeProviderBundleIdentifier"
+ "ampPAFDataSetID"
+ "appInferred"
+ "appSelectionEnabled"
+ "appSelectionSignalsEnabled"
+ "appSelectionSignalsFrequencyDenominator"
+ "approved"
+ "audioSearchResults"
+ "clearOobKeys"
+ "clearPendingParticipants"
+ "com.apple.coremedia"
+ "computeDevicePlaybackSessionID"
+ "connectToEndpointContainingOutputDeviceUID:options:details:completion:"
+ "connectToEndpointWithOutputDeviceUID"
+ "connectToExternalDeviceWithOptions:details:completion:"
+ "createTokenWithInvitationData:equivalentMediaIdentifier:"
+ "demoteWhenSyncingToCompanion"
+ "devicePlaybackSessionID"
+ "disableDuration"
+ "emi"
+ "enableRouteRecommendations"
+ "entityConfidenceSignalsEnabled"
+ "entityConfidenceSignalsFrequencyDenominatorInternal"
+ "entityConfidenceSignalsFrequencyDenominatorProd"
+ "entityConfidenceSignalsMaxItemsToDisambiguate"
+ "equivalentMediaIdentifier"
+ "getGroupSessionTokenWithCompletion:"
+ "groupSessionAutoApproveHomeParticipants"
+ "groupSessionGenerateSharedSecret"
+ "groupSessionListenForProxyJoinRequests"
+ "groupSessionSynchronizePendingParticipants"
+ "groupSessionToken"
+ "guest"
+ "h"
+ "handleLocalGroupSessionDidChangeNotification:"
+ "hasDemoteWhenSyncingToCompanion"
+ "hasDevicePlaybackSessionID"
+ "hasDisableDuration"
+ "hasEquivalentMediaIdentifier"
+ "hasGroupSessionToken"
+ "hasGuest"
+ "hasMuteUntilFinished"
+ "hasRenderingMode"
+ "hasReplyIdentifier"
+ "hasSessionIdentifier"
+ "hasSharedSecret"
+ "hi"
+ "hostedExternalDeviceGroupSessionTokenDidChange:"
+ "immediatelyStartPlayback"
+ "initWithAppSelectionEnabled:appInferred:audioSearchResults:privateMediaIntentData:appSelectionSignalsEnabled:appSelectionSignalsFrequencyDenominator:shouldSuppressCommonWholeHouseAudioRoutes:immediatelyStartPlayback:isAmbiguousPlay:isPersonalizedRequest:internalSignals:entityConfidenceSignalsEnabled:entityConfidenceSignalsFrequencyDenominatorInternal:entityConfidenceSignalsFrequencyDenominatorProd:entityConfidenceSignalsMaxItemsToDisambiguate:alternativeProviderBundleIdentifier:ampPAFDataSetID:"
+ "initWithHostInfo:invitationData:"
+ "initWithHostInfo:invitationData:sharedSecret:sessionIdentifier:equivalentMediaIdentifier:"
+ "initWithIdentifier:hostInfo:"
+ "initWithIdentifier:hostInfo:isHosted:equivalentMediaIdentifier:"
+ "initWithLastPlayingDate:devicePlaybackSessionID:"
+ "initWithRouteType:displayName:"
+ "initWithToken:isHosted:"
+ "internalSignals"
+ "isAmbiguousPlay"
+ "isGuest"
+ "isLockScreenAffordanceAllowed"
+ "isMostRecentMediaPlaybackRelevantReasonWithinInternal:"
+ "isMostRecentMediaPlaybackRelevantWithinInterval:"
+ "isPersonalizedRequest"
+ "lockScreenAffordanceAllowed"
+ "mediaID"
+ "migrateToEndpointOrModifyTopology:migrationRequest:topologyModificationRequest:withReplyQueue:completion:"
+ "mr_containsVideoOutputDevice"
+ "muteUntilFinished"
+ "needsMXApplications"
+ "nil != self->_invitationData"
+ "nil != self->_participantIdentifier"
+ "oobKeys"
+ "oobKeysAtIndex:"
+ "oobKeysCount"
+ "oobKeysType"
+ "outputDevice = <%@>, client = <%@>, reason = <%@>, operation = <%@>, changeType = <%@>, type = <%@>, demote = <%@> disableDuration = <%lf>"
+ "parseInitialState:"
+ "pendingParticipantsAtIndex:"
+ "pendingParticipantsCount"
+ "pendingParticipantsType"
+ "privateMediaIntentData"
+ "privatePlayMediaIntentData"
+ "r"
+ "renderingMode"
+ "renderingModeAsString:"
+ "requestReasonID"
+ "session:didConnectWithInitialState:"
+ "setActionImageName:"
+ "setApproved:"
+ "setDemoteWhenSyncingToCompanion:"
+ "setDevicePlaybackSessionID:"
+ "setDisableDuration:"
+ "setEquivalentMediaIdentifier:"
+ "setGroupSessionToken:"
+ "setGroupSessionTokenCallback:withQueue:"
+ "setGuest:"
+ "setHasDemoteWhenSyncingToCompanion:"
+ "setHasDisableDuration:"
+ "setHasGuest:"
+ "setHasMuteUntilFinished:"
+ "setHasRenderingMode:"
+ "setInvitationData:"
+ "setMuteUntilFinished:"
+ "setOobKeys:"
+ "setPrivatePlayMediaIntentData:"
+ "setRenderingMode:"
+ "setSessionIdentifier:"
+ "setSharedSecret:"
+ "sharedSecret"
+ "shouldOmitHost"
+ "si"
+ "ss"
+ "v16@?0@\"MRGroupSessionToken\"8"
+ "v24@0:8@\"MRGroupSessionToken\"16"
+ "v24@0:8@?<v@?@\"MRGroupSessionToken\">16"
+ "v32@0:8@\"NSString\"16@\"NSDictionary\"24"
+ "v44@0:8@16I24@28@?36"
+ "{?=\"audioFormat\"b1\"audioSessionID\"b1\"channelCount\"b1\"intendedSpatialExperience\"b1\"pid\"b1\"renderingMode\"b1\"resolvedSpatialExperience\"b1\"eligibleForSpatialization\"b1\"spatialized\"b1}"
+ "{?=\"bitDepth\"b1\"bitrate\"b1\"sampleRate\"b1\"channelLayout\"b1\"codec\"b1\"renderingMode\"b1\"tier\"b1\"multiChannel\"b1\"spatialized\"b1}"
+ "{?=\"connected\"b1\"guest\"b1}"
+ "{?=\"disableDuration\"b1\"type\"b1\"changeType\"b1\"demoteWhenSyncingToCompanion\"b1\"pairedDeviceSync\"b1}"
+ "{?=\"type\"b1\"fadeAudio\"b1\"muteUntilFinished\"b1\"shouldNotPauseIfLastDeviceRemoved\"b1\"suppressErrorDialog\"b1}"
+ "\x83"
+ "\xcf\n\x14"
- "\x021\x12\x13\x12'"
- "\x11$"
- "\x18\x12\x14\x12\x13\x12\x16"
- "1\x12"
- "<%@: identifier=%@, hosted=%@>"
- "<%@: identifier=%@, identity=%@, local=%@, pending=%@, connected=%@>"
- "@\"MRGroupSessionPersonInformation\""
- "@\"MRNearbyInvitation\""
- "@40@0:8@16@24C32B36"
- "MRGroupSessionPersonInformation"
- "MRGroupSessionToken * _Nonnull MRGroupSessionTokenCreateWithInvitationData(NSData *__strong _Nonnull)"
- "MRNearbyInvitation"
- "PlayDesination"
- "T@\"MRGroupSessionPersonInformation\",R,N,V_hostInfo"
- "T@\"MRNearbyInvitation\",R,N,V_invitation"
- "T@\"NSData\",&,N,V_displayImageData"
- "T@\"NSString\",&,N,V_localizedSessionName"
- "TB,R,N,GisCompanion"
- "TB,R,N,GisGizmo"
- "Unkown"
- "_displayImageData"
- "_invitation"
- "_localizedSessionName"
- "companion"
- "createTokenWithInvitationData:"
- "di"
- "displayImageData"
- "gizmo"
- "initWithDisplayName:displayImageData:"
- "initWithIdentifier:hostInfo:routeType:"
- "initWithIdentifier:hostInfo:routeType:isHosted:"
- "initWithInvitation:invitationData:"
- "initWithLastPlayingDate:"
- "invitation"
- "isMostRecentMediaPlaybackRelevant"
- "kMRMediaRemoteLocalPlaybackDidTimeoutNotification"
- "migrateToEndpointOrSetOutputDevices:request:queue:completion:"
- "outputDevice = <%@>, client = <%@>, reason = <%@>, operation = <%@>, changeType = <%@>, type = <%@>"
- "s"
- "setDisplayImageData:"
- "setLocalizedSessionName:"
- "{?=\"audioFormat\"b1\"audioSessionID\"b1\"channelCount\"b1\"intendedSpatialExperience\"b1\"pid\"b1\"resolvedSpatialExperience\"b1\"eligibleForSpatialization\"b1\"spatialized\"b1}"
- "{?=\"bitDepth\"b1\"bitrate\"b1\"sampleRate\"b1\"channelLayout\"b1\"codec\"b1\"tier\"b1\"multiChannel\"b1\"spatialized\"b1}"
- "{?=\"connected\"b1}"
- "{?=\"type\"b1\"changeType\"b1\"pairedDeviceSync\"b1}"
- "{?=\"type\"b1\"fadeAudio\"b1\"shouldNotPauseIfLastDeviceRemoved\"b1\"suppressErrorDialog\"b1}"
- "\xcf\n\x13"

```
