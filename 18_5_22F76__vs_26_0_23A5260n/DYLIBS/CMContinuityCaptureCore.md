## CMContinuityCaptureCore

> `/System/Library/PrivateFrameworks/CMContinuityCaptureCore.framework/CMContinuityCaptureCore`

```diff

-587.122.6.0.2
-  __TEXT.__text: 0x8fd4c
-  __TEXT.__auth_stubs: 0x1010
-  __TEXT.__objc_methlist: 0x5624
-  __TEXT.__const: 0x2a8
-  __TEXT.__gcc_except_tab: 0x4320
-  __TEXT.__cstring: 0x763c
-  __TEXT.__oslogstring: 0xa0a4
+650.0.0.122.4
+  __TEXT.__text: 0x8bc78
+  __TEXT.__auth_stubs: 0x1060
+  __TEXT.__objc_methlist: 0x5d30
+  __TEXT.__const: 0x308
+  __TEXT.__gcc_except_tab: 0x3154
+  __TEXT.__cstring: 0x7b29
+  __TEXT.__oslogstring: 0xa8f9
   __TEXT.__dlopen_cstrs: 0x54
-  __TEXT.__unwind_info: 0x2090
-  __TEXT.__objc_classname: 0xd65
-  __TEXT.__objc_methname: 0xbd3e
-  __TEXT.__objc_methtype: 0x280e
-  __TEXT.__objc_stubs: 0x90a0
-  __DATA_CONST.__got: 0x750
-  __DATA_CONST.__const: 0x1b28
-  __DATA_CONST.__objc_classlist: 0x1f0
+  __TEXT.__unwind_info: 0x20c8
+  __TEXT.__objc_classname: 0xdf1
+  __TEXT.__objc_methname: 0xd874
+  __TEXT.__objc_methtype: 0x2f0c
+  __TEXT.__objc_stubs: 0x95e0
+  __DATA_CONST.__got: 0x7a8
+  __DATA_CONST.__const: 0x1bd0
+  __DATA_CONST.__objc_classlist: 0x200
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x110
+  __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2a48
+  __DATA_CONST.__objc_selrefs: 0x2e70
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x1e0
+  __DATA_CONST.__objc_superrefs: 0x1f0
   __DATA_CONST.__objc_arraydata: 0x80
-  __AUTH_CONST.__auth_got: 0x818
-  __AUTH_CONST.__const: 0xa00
-  __AUTH_CONST.__cfstring: 0x4000
-  __AUTH_CONST.__objc_const: 0x9d00
+  __AUTH_CONST.__auth_got: 0x840
+  __AUTH_CONST.__const: 0xa20
+  __AUTH_CONST.__cfstring: 0x4260
+  __AUTH_CONST.__objc_const: 0xa468
   __AUTH_CONST.__objc_intobj: 0x510
   __AUTH_CONST.__objc_doubleobj: 0x80
-  __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x1220
-  __DATA.__objc_ivar: 0x854
-  __DATA.__data: 0xcd0
-  __DATA.__bss: 0x158
-  __DATA.__common: 0x80
+  __AUTH_CONST.__objc_arrayobj: 0x48
+  __AUTH_CONST.__objc_dictobj: 0x50
+  __AUTH.__objc_data: 0x12c0
+  __DATA.__objc_ivar: 0x890
+  __DATA.__data: 0xd98
+  __DATA.__bss: 0x168
+  __DATA.__common: 0x90
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__bss: 0x38
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /System/Library/PrivateFrameworks/MediaSafetyNet.framework/MediaSafetyNet
   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
+  - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 23FFF334-36BE-3D86-B054-BF4DF305D340
-  Functions: 2327
-  Symbols:   8299
-  CStrings:  4521
+  UUID: E7A6C510-1F37-3AF6-B5D9-116E471B0030
+  Functions: 2399
+  Symbols:   8552
+  CStrings:  4792
 
Symbols:
+ +[CMContinuityCaptureParticipantInfo supportsSecureCoding]
+ +[CMContinuityCaptureUIStateTracker sharedInstance]
+ +[CMContinuityCaptureUIStateTracker sharedInstance].cold.1
+ -[CMContinuityCaptureActiveSession initWithDevice:transport:initiatedOnCommunalDevice:micOnly:]
+ -[CMContinuityCaptureActiveSession isMicOnly]
+ -[CMContinuityCaptureConfiguration audioBlockSize]
+ -[CMContinuityCaptureConfiguration setAudioBlockSize:]
+ -[CMContinuityCaptureDiscoverySession _isSignedInDevice:]
+ -[CMContinuityCaptureDiscoverySession isSessionMicOnly]
+ -[CMContinuityCaptureDiscoverySession showIncompatibleDeviceNotificationIfApplicable]
+ -[CMContinuityCaptureEventQueue notifyCompletionForIdentifier:]
+ -[CMContinuityCaptureNWClient presentError:userInfo:]
+ -[CMContinuityCaptureNWClient remoteSessionTerminationForIdentifier:]
+ -[CMContinuityCaptureParticipantInfo .cxx_destruct]
+ -[CMContinuityCaptureParticipantInfo copyWithZone:]
+ -[CMContinuityCaptureParticipantInfo description]
+ -[CMContinuityCaptureParticipantInfo dictionaryRepresentation]
+ -[CMContinuityCaptureParticipantInfo displayName]
+ -[CMContinuityCaptureParticipantInfo encodeWithCoder:]
+ -[CMContinuityCaptureParticipantInfo groupSessionIdentifier]
+ -[CMContinuityCaptureParticipantInfo initWithCoder:]
+ -[CMContinuityCaptureParticipantInfo initWithDictionary:]
+ -[CMContinuityCaptureParticipantInfo initWithGroupSessionIdentifier:socialProfileIdentifier:displayName:]
+ -[CMContinuityCaptureParticipantInfo initWithMRParticipant:]
+ -[CMContinuityCaptureParticipantInfo isEqual:]
+ -[CMContinuityCaptureParticipantInfo setDisplayName:]
+ -[CMContinuityCaptureParticipantInfo setGroupSessionIdentifier:]
+ -[CMContinuityCaptureParticipantInfo setSocialProfileIdentifier:]
+ -[CMContinuityCaptureParticipantInfo socialProfileIdentifier]
+ -[CMContinuityCaptureSessionStateManager _startSessionWithDevice:forTransportType:validateTransport:initiatedOnCommunalDevice:micOnly:outError:]
+ -[CMContinuityCaptureSessionStateManager startSessionWithDevice:forTransportType:validateTransport:initiatedOnCommunalDevice:micOnly:outError:]
+ -[CMContinuityCaptureUIConfiguration micOnly]
+ -[CMContinuityCaptureUIConfiguration participantInfo]
+ -[CMContinuityCaptureUIConfiguration remoteDisplayIdentifier]
+ -[CMContinuityCaptureUIConfiguration setMicOnly:]
+ -[CMContinuityCaptureUIConfiguration setParticipantInfo:]
+ -[CMContinuityCaptureUIConfiguration setRemoteDisplayIdentifier:]
+ -[CMContinuityCaptureUIStateTracker .cxx_destruct]
+ -[CMContinuityCaptureUIStateTracker _aquireAppSuspendAssertion]
+ -[CMContinuityCaptureUIStateTracker _refreshInFaceTime]
+ -[CMContinuityCaptureUIStateTracker _releaseAppSuspendAssertion]
+ -[CMContinuityCaptureUIStateTracker _sessionDidUpdateWithConfiguration:]
+ -[CMContinuityCaptureUIStateTracker _sessionDidUpdateWithConfiguration:].cold.1
+ -[CMContinuityCaptureUIStateTracker _tearDownShield]
+ -[CMContinuityCaptureUIStateTracker activeConfiguration]
+ -[CMContinuityCaptureUIStateTracker activeConfiguration].cold.1
+ -[CMContinuityCaptureUIStateTracker active]
+ -[CMContinuityCaptureUIStateTracker connectionType]
+ -[CMContinuityCaptureUIStateTracker conversationManager:activeRemoteParticipantsChangedForConversation:]
+ -[CMContinuityCaptureUIStateTracker conversationManager:remoteMembersChangedForConversation:]
+ -[CMContinuityCaptureUIStateTracker init]
+ -[CMContinuityCaptureUIStateTracker isDedicatedSession]
+ -[CMContinuityCaptureUIStateTracker isInFaceTime]
+ -[CMContinuityCaptureUIStateTracker neighborhoodActivityConduit:splitSessionEnded:]
+ -[CMContinuityCaptureUIStateTracker neighborhoodActivityConduit:splitSessionStarted:]
+ -[CMContinuityCaptureUIStateTracker neighborhoodActivityConduit:tvDeviceAppeared:]
+ -[CMContinuityCaptureUIStateTracker neighborhoodActivityConduit:tvDeviceDisappeared:]
+ -[CMContinuityCaptureUIStateTracker presentError:userInfo:]
+ -[CMContinuityCaptureUIStateTracker serverXPCConnectionInterrupted]
+ -[CMContinuityCaptureUIStateTracker sessionDidUpdateWithConfiguration:]
+ -[CMContinuityCaptureUIStateTracker setConnectionType:]
+ -[CMContinuityCaptureUIStateTracker setUIConfiguration:]
+ -[CMContinuityCaptureUIStateTracker setUiState:]
+ -[CMContinuityCaptureUIStateTracker tearDownShield]
+ -[CMContinuityCaptureUIStateTracker uiState]
+ -[CMContinuityCaptureXPCClientCCD presentError:userInfo:]
+ -[CMContinuityCaptureXPCClientCCD setupSingSessionFromURL:remoteDisplayIdentifier:]
+ -[CMContinuityCaptureXPCClientCCD setupSingSessionWithMediaRouteIdentifier:remoteDisplayIdentifier:]
+ -[CMContinuityCaptureXPCServerCCD presentShieldError:userInfo:]
+ -[CMContinuityCaptureXPCServerCCD setupSingSessionFromURL:remoteDisplayIdentifier:]
+ -[CMContinuityCaptureXPCServerCCD setupSingSessionWithMediaRouteIdentifier:remoteDisplayIdentifier:]
+ -[CVPixelBufferCoder initWithCoder:].cold.2
+ -[CVPixelBufferCoder initWithCoder:].cold.3
+ GCC_except_table40
+ GCC_except_table45
+ _AVCMediaStreamNegotiatorRemoteMicChannelCount
+ _CFPreferencesGetAppIntegerValue
+ _CMContinuityCaptureControlNameDeskViewCameraZoomFactor
+ _CMContinuityCaptureMediaIdentifiersForCapabilities
+ _CMContinuityCaptureUIStateErrorNotification
+ _CMContinuityCaptureUIStateTrackerActiveConfigurationKVOKey
+ _CMContinuityCaptureUIStateTrackerActiveFaceTimeContinuitySessionKVOKey
+ _CMContinuityCaptureUIStateTrackerActiveKVOKey
+ _CMContinuityCaptureUIStateTrackerErrorCodeKey
+ _CVPixelBufferGetIOSurface
+ _ContinuityCaptureVoiceAmplificationModeInputASBD
+ _ContinuityCaptureVoiceAmplificationModeOutputASBD
+ _IOSurfaceGetID
+ _MobileGestalt_copy_hwModelDescriptionForCamera_obj
+ _MobileGestalt_get_current_device
+ _OBJC_CLASS_$_CMContinuityCaptureParticipantInfo
+ _OBJC_CLASS_$_CMContinuityCaptureUIStateTracker
+ _OBJC_CLASS_$_NSThread
+ _OBJC_CLASS_$_RBSAssertion
+ _OBJC_CLASS_$_RBSDomainAttribute
+ _OBJC_CLASS_$_RBSProcessIdentifier
+ _OBJC_CLASS_$_RBSTarget
+ _OBJC_IVAR_$_CMContinuityCaptureActiveSession._micOnly
+ _OBJC_IVAR_$_CMContinuityCaptureConfiguration._audioBlockSize
+ _OBJC_IVAR_$_CMContinuityCaptureParticipantInfo._displayName
+ _OBJC_IVAR_$_CMContinuityCaptureParticipantInfo._groupSessionIdentifier
+ _OBJC_IVAR_$_CMContinuityCaptureParticipantInfo._socialProfileIdentifier
+ _OBJC_IVAR_$_CMContinuityCaptureSidecarTransportBase._mediaIdentifiers
+ _OBJC_IVAR_$_CMContinuityCaptureSidecarTransportBase._sidebandIdentifiers
+ _OBJC_IVAR_$_CMContinuityCaptureUIConfiguration._micOnly
+ _OBJC_IVAR_$_CMContinuityCaptureUIConfiguration._participantInfo
+ _OBJC_IVAR_$_CMContinuityCaptureUIConfiguration._remoteDisplayIdentifier
+ _OBJC_IVAR_$_CMContinuityCaptureUIStateTracker._active
+ _OBJC_IVAR_$_CMContinuityCaptureUIStateTracker._activeConfiguration
+ _OBJC_IVAR_$_CMContinuityCaptureUIStateTracker._appSuspendAssertion
+ _OBJC_IVAR_$_CMContinuityCaptureUIStateTracker._connectionType
+ _OBJC_IVAR_$_CMContinuityCaptureUIStateTracker._inFaceTime
+ _OBJC_IVAR_$_CMContinuityCaptureUIStateTracker._queue
+ _OBJC_IVAR_$_CMContinuityCaptureUIStateTracker._uiState
+ _OBJC_METACLASS_$_CMContinuityCaptureParticipantInfo
+ _OBJC_METACLASS_$_CMContinuityCaptureUIStateTracker
+ _RPOptionSenderSessionPairingID
+ _RPOptionStatusFlags
+ __OBJC_$_CLASS_METHODS_CMContinuityCaptureParticipantInfo
+ __OBJC_$_CLASS_METHODS_CMContinuityCaptureUIStateTracker
+ __OBJC_$_CLASS_PROP_LIST_CMContinuityCaptureParticipantInfo
+ __OBJC_$_INSTANCE_METHODS_CMContinuityCaptureParticipantInfo
+ __OBJC_$_INSTANCE_METHODS_CMContinuityCaptureUIStateTracker
+ __OBJC_$_INSTANCE_VARIABLES_CMContinuityCaptureParticipantInfo
+ __OBJC_$_INSTANCE_VARIABLES_CMContinuityCaptureUIStateTracker
+ __OBJC_$_PROP_LIST_CMContinuityCaptureParticipantInfo
+ __OBJC_$_PROP_LIST_CMContinuityCaptureUIStateTracker
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_TUConversationManagerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_TUNeighborhoodActivityConduitDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_TUNeighborhoodActivityConduitDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_TUConversationManagerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_TUNeighborhoodActivityConduitDelegate
+ __OBJC_$_PROTOCOL_REFS_TUConversationManagerDelegate
+ __OBJC_$_PROTOCOL_REFS_TUNeighborhoodActivityConduitDelegate
+ __OBJC_CLASS_PROTOCOLS_$_CMContinuityCaptureParticipantInfo
+ __OBJC_CLASS_PROTOCOLS_$_CMContinuityCaptureUIStateTracker
+ __OBJC_CLASS_RO_$_CMContinuityCaptureParticipantInfo
+ __OBJC_CLASS_RO_$_CMContinuityCaptureUIStateTracker
+ __OBJC_LABEL_PROTOCOL_$_TUConversationManagerDelegate
+ __OBJC_LABEL_PROTOCOL_$_TUNeighborhoodActivityConduitDelegate
+ __OBJC_METACLASS_RO_$_CMContinuityCaptureParticipantInfo
+ __OBJC_METACLASS_RO_$_CMContinuityCaptureUIStateTracker
+ __OBJC_PROTOCOL_$_TUConversationManagerDelegate
+ __OBJC_PROTOCOL_$_TUNeighborhoodActivityConduitDelegate
+ ___143-[CMContinuityCaptureSessionStateManager startSessionWithDevice:forTransportType:validateTransport:initiatedOnCommunalDevice:micOnly:outError:]_block_invoke
+ ___51+[CMContinuityCaptureUIStateTracker sharedInstance]_block_invoke
+ ___51-[CMContinuityCaptureUIStateTracker tearDownShield]_block_invoke
+ ___55-[CMContinuityCaptureUIStateTracker _refreshInFaceTime]_block_invoke
+ ___63-[CMContinuityCaptureDeviceBase _stopStream:option:completion:]_block_invoke.40
+ ___63-[CMContinuityCaptureEventQueue notifyCompletionForIdentifier:]_block_invoke
+ ___63-[CMContinuityCaptureXPCServerCCD presentShieldError:userInfo:]_block_invoke
+ ___67-[CMContinuityCaptureTimeSyncClock startEmittingHeartBeatSignposts]_block_invoke
+ ___70-[CMContinuityCaptureDeviceBase stateMachineStopStreamOnEvent:option:]_block_invoke.52
+ ___70-[CMContinuityCaptureDeviceBase stateMachineStopStreamOnEvent:option:]_block_invoke.54
+ ___70-[CMContinuityCaptureDeviceBase stateMachineStopStreamOnEvent:option:]_block_invoke_2.55
+ ___70-[CMContinuityCaptureXPCServerCCD listener:shouldAcceptNewConnection:]_block_invoke.86
+ ___70-[CMContinuityCaptureXPCServerCCD listener:shouldAcceptNewConnection:]_block_invoke.87
+ ___70-[CMContinuityCaptureXPCServerCCD listener:shouldAcceptNewConnection:]_block_invoke.91
+ ___71-[CMContinuityCaptureDeviceBase stateMachineStartStreamOnEvent:option:]_block_invoke.51
+ ___71-[CMContinuityCaptureUIStateTracker sessionDidUpdateWithConfiguration:]_block_invoke
+ ___73-[CMContinuityCaptureDeviceBase stateMachineReStartStreamOnEvent:option:]_block_invoke.48
+ ___73-[CMContinuityCaptureDeviceBase stateMachineReStartStreamOnEvent:option:]_block_invoke.49
+ ___80-[CMContinuityCaptureXPCClientCCD connectToContinuityCaptureServerWithDelegate:]_block_invoke.79
+ ___80-[CMContinuityCaptureXPCClientCCD connectToContinuityCaptureServerWithDelegate:]_block_invoke.80
+ ___80-[CMContinuityCaptureXPCClientCCD connectToContinuityCaptureServerWithDelegate:]_block_invoke_2.81
+ ___CMContinuityCapturePromptOpenTapToRadar_block_invoke.275
+ ___CMContinuityCapturePromptOpenTapToRadar_block_invoke.275.cold.1
+ ___block_descriptor_32_e24_B16?0"TUConversation"8l
+ ___block_descriptor_48_e8_32s40w_e39_v24?0"NSDictionary"8"NSDictionary"16lw40l8s32l8
+ ___block_descriptor_48_e8_32s_e25_v16?0"NSXPCConnection"8ls32l8
+ ___block_descriptor_75_e8_32s40s48r56r_e5_v8?0lr48l8s32l8s40l8r56l8
+ ___block_literal_global.143
+ ___block_literal_global.215
+ ___block_literal_global.278
+ ___block_literal_global.34
+ ___block_literal_global.44
+ ___block_literal_global.47
+ ___block_literal_global.90
+ ___block_literal_global.96
+ __uiStateTracker
+ _gCMContinuityCaptureTimeSyncClockTrace
+ _gGMFigKTraceEnabled
+ _kCMContinuityCaptureAudioDeviceStartOptionsKey_blockSize
+ _kCMContinuityCaptureSessionExitReasonGroupSessionFailed
+ _kdebug_trace
+ _objc_msgSend$_aquireAppSuspendAssertion
+ _objc_msgSend$_isSignedInDevice:
+ _objc_msgSend$_refreshInFaceTime
+ _objc_msgSend$_releaseAppSuspendAssertion
+ _objc_msgSend$_sessionDidUpdateWithConfiguration:
+ _objc_msgSend$_startSessionWithDevice:forTransportType:validateTransport:initiatedOnCommunalDevice:micOnly:outError:
+ _objc_msgSend$_tearDownShield
+ _objc_msgSend$acquireWithError:
+ _objc_msgSend$activeConversations
+ _objc_msgSend$activeSplitSessionTV
+ _objc_msgSend$addDelegate:queue:
+ _objc_msgSend$attributeWithDomain:name:
+ _objc_msgSend$audioBlockSize
+ _objc_msgSend$auditToken
+ _objc_msgSend$avMode
+ _objc_msgSend$availableClockIdentifiers
+ _objc_msgSend$canPullBackConversation:
+ _objc_msgSend$conversationManager
+ _objc_msgSend$groupSessionIdentifier
+ _objc_msgSend$identifierForCurrentProcess
+ _objc_msgSend$identity
+ _objc_msgSend$initWithDevice:transport:initiatedOnCommunalDevice:micOnly:
+ _objc_msgSend$initWithExplanation:target:attributes:
+ _objc_msgSend$initWithFormat:
+ _objc_msgSend$initWithGroupSessionIdentifier:socialProfileIdentifier:displayName:
+ _objc_msgSend$isMainThread
+ _objc_msgSend$isSessionMicOnly
+ _objc_msgSend$micOnly
+ _objc_msgSend$participantInfo
+ _objc_msgSend$postNotificationName:object:userInfo:
+ _objc_msgSend$presentError:userInfo:
+ _objc_msgSend$remoteDisplayIdentifier
+ _objc_msgSend$remoteSessionTerminationForIdentifier:
+ _objc_msgSend$removeDelegate:
+ _objc_msgSend$setDisplayName:
+ _objc_msgSend$setGroupSessionIdentifier:
+ _objc_msgSend$setMicOnly:
+ _objc_msgSend$setParticipantInfo:
+ _objc_msgSend$setPreferredIOBufferDuration:
+ _objc_msgSend$setRemoteDisplayIdentifier:
+ _objc_msgSend$setSocialProfileIdentifier:
+ _objc_msgSend$setupSingSessionFromURL:remoteDisplayIdentifier:
+ _objc_msgSend$setupSingSessionWithMediaRouteIdentifier:remoteDisplayIdentifier:
+ _objc_msgSend$shieldDidConnect:
+ _objc_msgSend$showIncompatibleDeviceNotificationIfApplicable
+ _objc_msgSend$socialProfileIdentifier
+ _objc_msgSend$startSessionWithDevice:forTransportType:validateTransport:initiatedOnCommunalDevice:micOnly:outError:
+ _objc_msgSend$targetWithPid:
- -[CMContinuityCaptureActiveSession initWithDevice:transport:initiatedOnCommunalDevice:]
- -[CMContinuityCaptureDiscoverySession showIncompatableDeviceNotificationIfApplicable]
- -[CMContinuityCaptureEventQueue notifyCompletionForIdentfier:]
- -[CMContinuityCaptureNWClient remoteSessionTerminationForIdentfier:]
- -[CMContinuityCaptureSessionStateManager _startSessionWithDevice:forTransportType:validateTransport:initiatedOnCommunalDevice:outError:]
- -[CMContinuityCaptureSessionStateManager startSessionWithDevice:forTransportType:validateTransport:initiatedOnCommunalDevice:outError:]
- GCC_except_table138
- GCC_except_table139
- GCC_except_table152
- GCC_except_table153
- GCC_except_table154
- GCC_except_table155
- GCC_except_table156
- GCC_except_table26
- GCC_except_table29
- GCC_except_table94
- GCC_except_table96
- GCC_except_table97
- _CMContinuityCaptureMediaIdentfiersForCapabilities
- _OBJC_IVAR_$_CMContinuityCaptureSidecarTransportBase._mediaIdentfiers
- _OBJC_IVAR_$_CMContinuityCaptureSidecarTransportBase._sidebandIdentfiers
- ___135-[CMContinuityCaptureSessionStateManager startSessionWithDevice:forTransportType:validateTransport:initiatedOnCommunalDevice:outError:]_block_invoke
- ___62-[CMContinuityCaptureEventQueue notifyCompletionForIdentfier:]_block_invoke
- ___63-[CMContinuityCaptureDeviceBase _stopStream:option:completion:]_block_invoke.44
- ___70-[CMContinuityCaptureDeviceBase stateMachineStopStreamOnEvent:option:]_block_invoke.56
- ___70-[CMContinuityCaptureDeviceBase stateMachineStopStreamOnEvent:option:]_block_invoke.58
- ___70-[CMContinuityCaptureDeviceBase stateMachineStopStreamOnEvent:option:]_block_invoke_2.59
- ___70-[CMContinuityCaptureXPCServerCCD listener:shouldAcceptNewConnection:]_block_invoke.81
- ___70-[CMContinuityCaptureXPCServerCCD listener:shouldAcceptNewConnection:]_block_invoke_3
- ___70-[CMContinuityCaptureXPCServerCCD listener:shouldAcceptNewConnection:]_block_invoke_4
- ___71-[CMContinuityCaptureDeviceBase stateMachineStartStreamOnEvent:option:]_block_invoke.55
- ___73-[CMContinuityCaptureDeviceBase stateMachineReStartStreamOnEvent:option:]_block_invoke.52
- ___73-[CMContinuityCaptureDeviceBase stateMachineReStartStreamOnEvent:option:]_block_invoke.53
- ___80-[CMContinuityCaptureXPCClientCCD connectToContinuityCaptureServerWithDelegate:]_block_invoke_3
- ___80-[CMContinuityCaptureXPCClientCCD connectToContinuityCaptureServerWithDelegate:]_block_invoke_4
- ___80-[CMContinuityCaptureXPCClientCCD connectToContinuityCaptureServerWithDelegate:]_block_invoke_5
- ___CMContinuityCapturePromptOpenTapToRadar_block_invoke.272
- ___CMContinuityCapturePromptOpenTapToRadar_block_invoke.272.cold.1
- ___block_descriptor_74_e8_32s40s48r56r_e5_v8?0lr48l8s32l8s40l8r56l8
- ___block_literal_global.124
- ___block_literal_global.137
- ___block_literal_global.209
- ___block_literal_global.275
- ___block_literal_global.46
- ___block_literal_global.48
- ___block_literal_global.51
- ___block_literal_global.72
- ___block_literal_global.92
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_msgSend$_startSessionWithDevice:forTransportType:validateTransport:initiatedOnCommunalDevice:outError:
- _objc_msgSend$initWithDevice:transport:initiatedOnCommunalDevice:
- _objc_msgSend$remoteSessionTerminationForIdentfier:
- _objc_msgSend$shieldDidConnect
- _objc_msgSend$showIncompatableDeviceNotificationIfApplicable
- _objc_msgSend$startSessionWithDevice:forTransportType:validateTransport:initiatedOnCommunalDevice:outError:
CStrings:
+ "%@ %s %@ %@"
+ "%@ %{public}s device %{public}@ unavailable"
+ "%@ Failed to acquire app suspend assertion with error %@"
+ "%@ NW Connect Received Data %@"
+ "%@ NW Connect Received Packet %@"
+ "%@ NW Path evaluator %@"
+ "%@ NW listener state %d error %@"
+ "%@ Received control %{public}@ update"
+ "%@ Successfully acquired app suspend assertion"
+ "%@ User Disconnect for idsIdentifier: %{public}@ sessionPairingIdentifier: %@ reason: %{public}@"
+ "%@ activeConfiguration change (%{public}@ -> %{public}@)"
+ "%@ activeConfiguration should not be set to nil, returning"
+ "%@ activeConfiguration shouldn't be nil"
+ "%@ idsID %@ spID %@ deviceIdentifier %@"
+ "%@ teardown shieldUI"
+ "%@: Entity:%d SVE:%d PE:%d CS:%d FCST:%lu CSRI:%@ CSFM:%ld FD:%d HBD:%d HFBD:%d AsyncStill:%d MQP:%d SL:%d BR:%d FR:%u MnFR:%u VideoZoomFactor:%.2f Format:%@ DVCM:%u ADM:%u ABS:%.3f, GID:%llx PEA:%f SLI:%f PA[x:%f,y:%f] MFD:%@ FoVTW:%d [%p]"
+ "%{public}@ Message GID %{public}@ identifier %{public}@ selector %{public}@ send error %@"
+ "%{public}@ Skipped creating capture device for entity %d"
+ ", micOnly=%d"
+ ", participantInfo=%@"
+ ", remoteDisplayIdentifier=%@"
+ "-[CMContinuityCaptureSessionStateManager _startSessionWithDevice:forTransportType:validateTransport:initiatedOnCommunalDevice:micOnly:outError:]"
+ "-[CMContinuityCaptureTimeSyncClock initWithClock:]"
+ "-[CMContinuityCaptureTimeSyncClock startEmittingHeartBeatSignposts]"
+ "-[CMContinuityCaptureTimeSyncClock startEmittingHeartBeatSignposts]_block_invoke"
+ "-[CMContinuityCaptureUIStateTracker presentError:userInfo:]"
+ "-[CMContinuityCaptureXPCClientCCD connectToContinuityCaptureServerWithDelegate:]_block_invoke_2"
+ "-[CMContinuityCaptureXPCClientCCD presentError:userInfo:]"
+ "-[CMContinuityCaptureXPCServerCCD listener:shouldAcceptNewConnection:]_block_invoke_2"
+ "-[CMContinuityCaptureXPCServerCCD presentShieldError:userInfo:]"
+ "-[CMContinuityCaptureXPCServerCCD setupSingSessionFromURL:remoteDisplayIdentifier:]"
+ "-[CVPixelBufferCoder _createPixelBufferForImage:fillWidth:fillHeight:]"
+ "-[CVPixelBufferCoder encodeWithCoder:]"
+ "-[CVPixelBufferCoder initWithCoder:]"
+ "-[NSCoder(CVPixelBuffer) decodeCVPixelBufferForKey:expectSourceMedia:]"
+ "<<<< CMContinuityCaptureTimeSyncClock >>>> %s: %@ %lld: (%lld) %lld -> %lld"
+ "<<<< CMContinuityCaptureTimeSyncClock >>>> %s: %@ starting heart beat signposts with interval %lu seconds"
+ "<<<< CMContinuityCaptureTimeSyncClock >>>> %s: Failed to create PTP clock with identifier %llu, available identifiers %@"
+ "<<<< CMContinuityCaptureXPCClientCCD >>>> %s: connection interrupted %@. Scheduling reconnect in 3 seconds."
+ "<<<< CMContinuityCaptureXPCClientCCD >>>> %s: connection invalidated %@"
+ "<<<< CMContinuityCaptureXPCServer >>>> %s: %@ %@ %@"
+ "<<<< CMContinuityCaptureXPCServer >>>> %s: %@: %@ %@"
+ "<<<< CMContinuityCaptureXPCServer >>>> %s: connection interrupted %@"
+ "<<<< CMContinuityCaptureXPCServer >>>> %s: connection invalidated %@"
+ "<<<< NSCoding+CVPixelBufferRef >>>> %s: Could not create pixel buffer: %d"
+ "<<<< NSCoding+CVPixelBufferRef >>>> %s: Could not read source media %@, falling back to pixel buffer copy"
+ "<<<< NSCoding+CVPixelBufferRef >>>> %s: Could not serialize pixel buffer, error %d"
+ "<<<< NSCoding+CVPixelBufferRef >>>> %s: Error creating pixel buffer %zu x %zu: %d"
+ "<<<< NSCoding+CVPixelBufferRef >>>> %s: Expected source media but pixel buffer data was found instead (not fatal)"
+ "<<<< NSCoding+CVPixelBufferRef >>>> %s: Failed to create pixel buffer %zu x %zu"
+ "<<<< NSCoding+CVPixelBufferRef >>>> %s: Fallback not using atom data, outdated peer connection for pixel buffer"
+ "<<<< NSCoding+CVPixelBufferRef >>>> %s: No pixel data"
+ "<<<< NSCoding+CVPixelBufferRef >>>> %s: bad source image offset"
+ "<<<< NSCoding+CVPixelBufferRef >>>> %s: image planes don't match, encoded %d allocated %d"
+ "<<<< NSCoding+CVPixelBufferRef >>>> %s: source image offset overrun"
+ "<<<< NSCoding+CVPixelBufferRef >>>> %s: source image stride overrun"
+ "<CMContinuityCaptureParticipantInfo displayName:%@ groupSessionIdentifier:%@ socialProfileIdentifier:%@>"
+ "@\"CMContinuityCaptureParticipantInfo\""
+ "@\"CMContinuityCaptureUIConfiguration\""
+ "@\"RBSAssertion\""
+ "@40@0:8@16q24B32B36"
+ "B16@?0@\"TUConversation\"8"
+ "B52@0:8@16q24B32B36B40^@44"
+ "CMContinuityCaptureParticipantInfo"
+ "CMContinuityCaptureUIStateErrorNotification"
+ "CMContinuityCaptureUIStateTracker"
+ "CMContinuityCaptureUIStateTrackerErrorCodeKey"
+ "DeskViewCameraZoomFactor"
+ "DoCapture"
+ "Group session join failed"
+ "Shield Terminate XPC"
+ "T@\"CMContinuityCaptureParticipantInfo\",C,N,V_participantInfo"
+ "T@\"CMContinuityCaptureUIConfiguration\",R,&"
+ "T@\"NSString\",C,N,V_displayName"
+ "T@\"NSString\",C,N,V_groupSessionIdentifier"
+ "T@\"NSString\",C,N,V_remoteDisplayIdentifier"
+ "T@\"NSString\",C,N,V_socialProfileIdentifier"
+ "TB,N,V_micOnly"
+ "TB,R,GisMicOnly,V_micOnly"
+ "TB,R,N,GisDedicatedSession"
+ "TB,R,N,GisInFaceTime"
+ "TUConversationManagerDelegate"
+ "TUNeighborhoodActivityConduitDelegate"
+ "Td,N,V_audioBlockSize"
+ "_appSuspendAssertion"
+ "_aquireAppSuspendAssertion"
+ "_audioBlockSize"
+ "_connectionType"
+ "_displayName"
+ "_groupSessionIdentifier"
+ "_inFaceTime"
+ "_isSignedInDevice:"
+ "_mediaIdentifiers"
+ "_micOnly"
+ "_participantInfo"
+ "_refreshInFaceTime"
+ "_releaseAppSuspendAssertion"
+ "_remoteDisplayIdentifier"
+ "_sessionDidUpdateWithConfiguration:"
+ "_sidebandIdentifiers"
+ "_socialProfileIdentifier"
+ "_startSessionWithDevice:forTransportType:validateTransport:initiatedOnCommunalDevice:micOnly:outError:"
+ "_tearDownShield"
+ "_uiState"
+ "acquireWithError:"
+ "activeConversations"
+ "activeSplitSessionTV"
+ "addDelegate:queue:"
+ "attributeWithDomain:name:"
+ "audioBlockSize"
+ "auditToken"
+ "avMode"
+ "availableClockIdentifiers"
+ "canPullBackConversation:"
+ "cmcontinuitycapturetimesyncclock_trace"
+ "com.apple.ContinuitySingShieldUI"
+ "connectionType"
+ "continuitycapture_timesync_heartbeat_interval"
+ "conversationManager"
+ "conversationManager:activeRemoteParticipantsChangedForConversation:"
+ "conversationManager:activeRemoteParticipantsChangedForConversation:fromOldConversation:"
+ "conversationManager:activitySessionsChangedForConversation:"
+ "conversationManager:activitySessionsChangedForConversation:fromOldConversation:"
+ "conversationManager:addedActiveConversation:"
+ "conversationManager:avModeChangedForConversation:"
+ "conversationManager:avModeChangedForConversation:fromOldConversation:"
+ "conversationManager:cameraMixedWithScreenDidChangeForConversation:"
+ "conversationManager:cameraMixedWithScreenDidChangeForConversation:fromOldConversation:"
+ "conversationManager:changedActivityAuthorizationForBundleIdentifier:"
+ "conversationManager:collaborationChanged:forConversation:collaborationState:"
+ "conversationManager:conversation:addedMembersLocally:"
+ "conversationManager:conversation:buzzedMember:"
+ "conversationManager:conversation:didChangeSceneAssociationForActivitySession:"
+ "conversationManager:conversation:didChangeStateForActivitySession:"
+ "conversationManager:conversation:launchStateChanged:forActivitySession:"
+ "conversationManager:conversation:participant:addedCollaborationNotice:"
+ "conversationManager:conversation:participant:addedNotice:"
+ "conversationManager:conversation:receivedActivitySessionEvent:"
+ "conversationManager:conversation:requestedScreenShareForParticipant:"
+ "conversationManager:conversation:screenSharingChangedForParticipant:"
+ "conversationManager:conversation:updatedMessagesGroupPhoto:"
+ "conversationManager:conversationUpdatedMessagesGroupName:"
+ "conversationManager:conversationUpdatedMessagesGroupName:fromOldConversation:"
+ "conversationManager:conversationUpdatedMessagesGroupUUID:"
+ "conversationManager:didChangeActivatedLinks:"
+ "conversationManager:didChangeConversationAdvertisement:"
+ "conversationManager:handoffEligibilityChangedForConversation:"
+ "conversationManager:handoffEligibilityChangedToConversation:fromPreviousConversation:"
+ "conversationManager:ignoreLMIRequestsChangedForConversation:"
+ "conversationManager:kickedMembersChangedForConversation:"
+ "conversationManager:kickedMembersChangedForConversation:fromOldConversation:"
+ "conversationManager:letMeInRequestStateChangedForConversation:"
+ "conversationManager:letMeInRequestStateChangedForConversation:fromOldConversation:"
+ "conversationManager:linkChangedForConversation:"
+ "conversationManager:linkChangedForConversation:fromOldConversation:"
+ "conversationManager:linkInvitedMemberHandlesChangedForConversation:"
+ "conversationManager:linkInvitedMemberHandlesChangedForConversation:fromOldConversation:"
+ "conversationManager:localParticipantClusterDidChangeForConversation:"
+ "conversationManager:localParticipantClusterDidChangeForConversation:fromOldConversation:"
+ "conversationManager:localVideoToggledForConversation:"
+ "conversationManager:localVideoToggledForConversation:fromOldConversation:"
+ "conversationManager:migratingFromConversation:toConversation:"
+ "conversationManager:nearbySharePlayToggledForConversation:"
+ "conversationManager:nearbySharePlayToggledForConversation:fromOldConversation:"
+ "conversationManager:oneToOneModeChangedForConversation:"
+ "conversationManager:oneToOneModeChangedForConversation:fromOldConversation:"
+ "conversationManager:otherInvitedHandlesChangedForConversation:"
+ "conversationManager:otherInvitedHandlesChangedForConversation:fromOldConversation:"
+ "conversationManager:pendingMembersChangedForConversation:"
+ "conversationManager:pendingMembersChangedForConversation:fromOldConversation:"
+ "conversationManager:presentationContextChangedForConversation:"
+ "conversationManager:presentationContextChangedForConversation:fromOldConversation:"
+ "conversationManager:rejectedMembersChangedForConversation:"
+ "conversationManager:rejectedMembersChangedForConversation:fromOldConversation:"
+ "conversationManager:remoteMembersChangedForConversation:"
+ "conversationManager:remoteMembersChangedForConversation:fromOldConversation:"
+ "conversationManager:remoteScreenShareAttributesChanged:isLocallySharing:"
+ "conversationManager:remoteScreenShareEndedWithReason:"
+ "conversationManager:removedActiveConversation:"
+ "conversationManager:resolvedAudioVideoModeChangedForConversation:"
+ "conversationManager:resolvedAudioVideoModeChangedForConversation:fromOldConversation:"
+ "conversationManager:screenSharingAvailableChanged:"
+ "conversationManager:screenSharingRequestsChangedForConversation:fromOldConversation:"
+ "conversationManager:screeningChangedForConversation:"
+ "conversationManager:sharePlayAvailableChanged:"
+ "conversationManager:stateChangedForConversation:"
+ "conversationManager:stateChangedForConversation:fromOldConversation:"
+ "conversationManager:systemActivitySessionsChangedForConversation:"
+ "conversationManager:systemActivitySessionsChangedForConversation:fromOldConversation:"
+ "conversationManager:trackedPendingMember:forConversationLink:"
+ "conversationManager:updatedIncomingPendingConversations:"
+ "conversationsChangedForConversationManager:"
+ "dedicatedSession"
+ "groupSessionIdentifier"
+ "identifierForCurrentProcess"
+ "identity"
+ "inFaceTime"
+ "initWithDevice:transport:initiatedOnCommunalDevice:micOnly:"
+ "initWithExplanation:target:attributes:"
+ "initWithFormat:"
+ "initWithGroupSessionIdentifier:socialProfileIdentifier:displayName:"
+ "initWithMRParticipant:"
+ "isDedicatedSession"
+ "isInFaceTime"
+ "isMainThread"
+ "isMicOnly"
+ "isSessionMicOnly"
+ "micOnly"
+ "neighborhoodActivityConduit:splitSessionEnded:"
+ "neighborhoodActivityConduit:splitSessionStarted:"
+ "neighborhoodActivityConduit:suggestionUpdated:"
+ "neighborhoodActivityConduit:tvDeviceAppeared:"
+ "neighborhoodActivityConduit:tvDeviceDisappeared:"
+ "notifyCompletionForIdentifier:"
+ "participantInfo"
+ "postNotificationName:object:userInfo:"
+ "presentError:userInfo:"
+ "presentShieldError:userInfo:"
+ "remoteDisplayIdentifier"
+ "remoteSessionTerminationForIdentifier:"
+ "removeDelegate:"
+ "serverDisconnectedForConversationManager:"
+ "session:didUpdateDLTDOAMeasurements:"
+ "setAudioBlockSize:"
+ "setConnectionType:"
+ "setDisplayName:"
+ "setGroupSessionIdentifier:"
+ "setMicOnly:"
+ "setParticipantInfo:"
+ "setPreferredIOBufferDuration:"
+ "setRemoteDisplayIdentifier:"
+ "setSocialProfileIdentifier:"
+ "setUIConfiguration:"
+ "setUiState:"
+ "setupSingSessionFromURL:remoteDisplayIdentifier:"
+ "setupSingSessionWithMediaRouteIdentifier:remoteDisplayIdentifier:"
+ "shieldDidConnect:"
+ "showIncompatibleDeviceNotificationIfApplicable"
+ "socialProfileIdentifier"
+ "startSessionWithDevice:forTransportType:validateTransport:initiatedOnCommunalDevice:micOnly:outError:"
+ "targetWithPid:"
+ "uiState"
+ "v24@0:8@\"TUConversationManager\"16"
+ "v28@0:8@\"TUConversationManager\"16B24"
+ "v32@0:8@\"NSString\"16@\"NSString\"24"
+ "v32@0:8@\"NSURL\"16@\"NSString\"24"
+ "v32@0:8@\"TUConversationManager\"16@\"NSArray\"24"
+ "v32@0:8@\"TUConversationManager\"16@\"NSError\"24"
+ "v32@0:8@\"TUConversationManager\"16@\"NSString\"24"
+ "v32@0:8@\"TUConversationManager\"16@\"TUConversation\"24"
+ "v32@0:8@\"TUConversationManager\"16@\"TUConversationActivityAdvertisement\"24"
+ "v32@0:8@\"TUNeighborhoodActivityConduit\"16@\"TUNearbyDeviceHandle\"24"
+ "v32@0:8@\"TUNeighborhoodActivityConduit\"16@\"TUNearbySuggestion\"24"
+ "v32@0:8q16@\"NSDictionary\"24"
+ "v36@0:8@\"TUConversationManager\"16@\"<TUScreenShareAttributes>\"24B32"
+ "v36@0:8@16@24B32"
+ "v40@0:8@\"TUConversationManager\"16@\"TUConversation\"24@\"NSData\"32"
+ "v40@0:8@\"TUConversationManager\"16@\"TUConversation\"24@\"NSSet\"32"
+ "v40@0:8@\"TUConversationManager\"16@\"TUConversation\"24@\"TUConversation\"32"
+ "v40@0:8@\"TUConversationManager\"16@\"TUConversation\"24@\"TUConversationActivityEvent\"32"
+ "v40@0:8@\"TUConversationManager\"16@\"TUConversation\"24@\"TUConversationActivitySession\"32"
+ "v40@0:8@\"TUConversationManager\"16@\"TUConversation\"24@\"TUConversationMember\"32"
+ "v40@0:8@\"TUConversationManager\"16@\"TUConversation\"24@\"TUConversationParticipant\"32"
+ "v40@0:8@\"TUConversationManager\"16@\"TUConversationMember\"24@\"TUConversationLink\"32"
+ "v48@0:8@\"TUConversationManager\"16@\"SWCollaborationHighlight\"24@\"TUConversation\"32q40"
+ "v48@0:8@\"TUConversationManager\"16@\"TUConversation\"24@\"TUConversationParticipant\"32@\"TUCollaborationNotice\"40"
+ "v48@0:8@\"TUConversationManager\"16@\"TUConversation\"24@\"TUConversationParticipant\"32@\"TUConversationNotice\"40"
+ "v48@0:8@\"TUConversationManager\"16@\"TUConversation\"24Q32@\"TUConversationActivitySession\"40"
+ "v48@0:8@16@24@32q40"
+ "v48@0:8@16@24Q32@40"
- "%@ %{public}s device %{public}@ unavialble"
- "%@ NW Connect Recieved Data %@"
- "%@ NW Connect Recieved Packet %@"
- "%@ NW Path evaulator %@"
- "%@ NW lsitener state %d error %@"
- "%@ Recieved control %{public}@ update"
- "%@ User Disconnect for %{public}@ reason %{public}@"
- "%@ deviceIdentifier %@"
- "%@: Entity:%d SVE:%d PE:%d CS:%d FCST:%lu CSRI:%@ CSFM:%ld FD:%d HBD:%d HFBD:%d AsyncStill:%d MQP:%d SL:%d BR:%d FR:%u MnFR:%u VideoZoomFactor:%.2f Format:%@ DVCM:%u ADM:%u GID:%llx PEA:%f SLI:%f PA[x:%f,y:%f] MFD:%@ FoVTW:%d [%p]"
- "%{public}@ Message GID %{public}@ indentifier %{public}@ selector %{public}@ send error %@"
- "-[CMContinuityCaptureSessionStateManager _startSessionWithDevice:forTransportType:validateTransport:initiatedOnCommunalDevice:outError:]"
- "-[CMContinuityCaptureXPCClientCCD connectToContinuityCaptureServerWithDelegate:]_block_invoke_5"
- "-[CMContinuityCaptureXPCServerCCD listener:shouldAcceptNewConnection:]_block_invoke_4"
- "@36@0:8@16q24B32"
- "AVCMediaStreamNegotiatorRemoteMicChannelCount"
- "B48@0:8@16q24B32B36^@40"
- "HWModelStr"
- "_mediaIdentfiers"
- "_sidebandIdentfiers"
- "_startSessionWithDevice:forTransportType:validateTransport:initiatedOnCommunalDevice:outError:"
- "initWithDevice:transport:initiatedOnCommunalDevice:"
- "notifyCompletionForIdentfier:"
- "remoteSessionTerminationForIdentfier:"
- "shieldDidConnect"
- "showIncompatableDeviceNotificationIfApplicable"
- "startSessionWithDevice:forTransportType:validateTransport:initiatedOnCommunalDevice:outError:"

```
