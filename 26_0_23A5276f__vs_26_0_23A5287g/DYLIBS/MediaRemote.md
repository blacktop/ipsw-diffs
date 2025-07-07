## MediaRemote

> `/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote`

```diff

-4025.110.97.1.0
-  __TEXT.__text: 0x2e59c0
+4025.100.103.0.0
+  __TEXT.__text: 0x2ea364
   __TEXT.__auth_stubs: 0x16d0
-  __TEXT.__objc_methlist: 0x2a398
-  __TEXT.__const: 0x598
-  __TEXT.__cstring: 0x2b182
-  __TEXT.__oslogstring: 0xd831
-  __TEXT.__gcc_except_tab: 0x6208
+  __TEXT.__objc_methlist: 0x2a8d8
+  __TEXT.__const: 0x5f8
+  __TEXT.__cstring: 0x2b51c
+  __TEXT.__oslogstring: 0xd851
+  __TEXT.__gcc_except_tab: 0x6270
   __TEXT.__dlopen_cstrs: 0x514
   __TEXT.__ustring: 0x7a2
-  __TEXT.__unwind_info: 0xaaf0
-  __TEXT.__objc_classname: 0x4c34
-  __TEXT.__objc_methname: 0x4b598
-  __TEXT.__objc_methtype: 0x8e62
-  __TEXT.__objc_stubs: 0x27360
-  __DATA_CONST.__got: 0x1420
-  __DATA_CONST.__const: 0xac48
-  __DATA_CONST.__objc_classlist: 0x1160
+  __TEXT.__unwind_info: 0xb010
+  __TEXT.__objc_classname: 0x4cd3
+  __TEXT.__objc_methname: 0x4c33e
+  __TEXT.__objc_methtype: 0x8eb7
+  __TEXT.__objc_stubs: 0x279a0
+  __DATA_CONST.__got: 0x1430
+  __DATA_CONST.__const: 0xacc8
+  __DATA_CONST.__objc_classlist: 0x1178
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x250
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xea18
+  __DATA_CONST.__objc_selrefs: 0xec80
   __DATA_CONST.__objc_protorefs: 0x88
-  __DATA_CONST.__objc_superrefs: 0xf98
+  __DATA_CONST.__objc_superrefs: 0xfb0
   __DATA_CONST.__objc_arraydata: 0x260
   __AUTH_CONST.__auth_got: 0xb78
   __AUTH_CONST.__const: 0x3040
-  __AUTH_CONST.__cfstring: 0x227c0
-  __AUTH_CONST.__objc_const: 0x44838
+  __AUTH_CONST.__cfstring: 0x22ce0
+  __AUTH_CONST.__objc_const: 0x44f58
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_intobj: 0x4e0
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x7f30
+  __AUTH.__objc_data: 0x8020
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0x3148
+  __DATA.__objc_ivar: 0x318c
   __DATA.__data: 0x1c20
   __DATA.__bss: 0x8a0
   __DATA.__common: 0x8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 048F7BA3-D020-332A-81A4-67A4064A18FE
-  Functions: 19791
-  Symbols:   54332
-  CStrings:  23896
+  UUID: 223E80E8-ABE0-37DF-8B35-3EEB2032EF58
+  Functions: 19932
+  Symbols:   54707
+  CStrings:  24105
 
Symbols:
+ -[MRAVOutputDevice isSystemCaptureDevice]
+ -[MRDeviceInfo preferredClusterLeaderID]
+ -[MRDeviceInfo setPreferredClusterLeaderID:]
+ -[MRDeviceInfo(MRNowPlayingSessionManagerDataSourceAdditions) mr_effectiveRoutingContextID]
+ -[MRMediaRemoteService mediaSuggestionDeviceUIDWithQueue:completion:]
+ -[MRMediaRemoteServiceClient addMediaSuggestionElectedDeviceObserver:]
+ -[MRMediaRemoteServiceClient currentSessionRoutingContextID]
+ -[MRMediaRemoteServiceClient removeMediaSuggestionElectedDeviceObserver:]
+ -[MRMediaRemoteServiceClient setCurrentSessionRoutingContextID:]
+ -[MRMediaSuggestionElectedDeviceObserver dealloc]
+ -[MRMediaSuggestionElectedDeviceObserver debugDescription]
+ -[MRMediaSuggestionElectedDeviceObserver isObserving]
+ -[MRMediaSuggestionElectedDeviceObserver setElectedDeviceIdentifier:]
+ -[MRMediaSuggestionElectedDeviceObserver setObserving:]
+ -[MRNowPlayingOriginClient playbackSessionMigratePostCallback]
+ -[MRNowPlayingOriginClient setPlaybackSessionMigratePostCallback:]
+ -[MRNowPlayingPlayerClientCallbacks playbackSessionMigratePostCallback]
+ -[MRNowPlayingPlayerClientCallbacks setPlaybackSessionMigratePostCallback:]
+ -[MRPlaybackSessionMigrateAnalytics .cxx_destruct]
+ -[MRPlaybackSessionMigrateAnalytics data]
+ -[MRPlaybackSessionMigrateAnalytics destinationPlayAudioGap]
+ -[MRPlaybackSessionMigrateAnalytics deviceTypeFromMRDeviceClass:]
+ -[MRPlaybackSessionMigrateAnalytics dictionaryRepresentation]
+ -[MRPlaybackSessionMigrateAnalytics durationApply]
+ -[MRPlaybackSessionMigrateAnalytics durationApply_SetPlaybackSessionCommand]
+ -[MRPlaybackSessionMigrateAnalytics durationDetermineRecipe]
+ -[MRPlaybackSessionMigrateAnalytics durationFinalize]
+ -[MRPlaybackSessionMigrateAnalytics durationPrepare]
+ -[MRPlaybackSessionMigrateAnalytics errorLevelCore_0]
+ -[MRPlaybackSessionMigrateAnalytics errorLevelCore_1]
+ -[MRPlaybackSessionMigrateAnalytics errorLevel_0]
+ -[MRPlaybackSessionMigrateAnalytics errorLevel_1]
+ -[MRPlaybackSessionMigrateAnalytics errorOnion]
+ -[MRPlaybackSessionMigrateAnalytics handoffAppBundle]
+ -[MRPlaybackSessionMigrateAnalytics handoffDestinationPerformanceClass]
+ -[MRPlaybackSessionMigrateAnalytics handoffDestination]
+ -[MRPlaybackSessionMigrateAnalytics handoffInitiator]
+ -[MRPlaybackSessionMigrateAnalytics handoffQueueSize]
+ -[MRPlaybackSessionMigrateAnalytics handoffSourcePerformanceClass]
+ -[MRPlaybackSessionMigrateAnalytics handoffSource]
+ -[MRPlaybackSessionMigrateAnalytics init]
+ -[MRPlaybackSessionMigrateAnalytics isSuccess]
+ -[MRPlaybackSessionMigrateAnalytics playPerfFields]
+ -[MRPlaybackSessionMigrateAnalytics postDuration]
+ -[MRPlaybackSessionMigrateAnalytics preDuration]
+ -[MRPlaybackSessionMigrateAnalytics setData:]
+ -[MRPlaybackSessionMigrateAnalytics setHandoffAppBundleFromString:]
+ -[MRPlaybackSessionMigrateAnalytics setHandoffDestinationFromMRDeviceClass:]
+ -[MRPlaybackSessionMigrateAnalytics setHandoffInitiatorFromString:]
+ -[MRPlaybackSessionMigrateAnalytics setHandoffSourceFromMRDeviceClass:]
+ -[MRPlaybackSessionMigrateAnalytics setPlayPerfFields:]
+ -[MRPlaybackSessionMigrateAnalytics set_destinationPlayAudioGap:]
+ -[MRPlaybackSessionMigrateAnalytics set_durationApply:]
+ -[MRPlaybackSessionMigrateAnalytics set_durationApply_SetPlaybackSessionCommand:]
+ -[MRPlaybackSessionMigrateAnalytics set_durationDetermineRecipe:]
+ -[MRPlaybackSessionMigrateAnalytics set_durationFinalize:]
+ -[MRPlaybackSessionMigrateAnalytics set_durationPrepare:]
+ -[MRPlaybackSessionMigrateAnalytics set_errorLevelCore_0:]
+ -[MRPlaybackSessionMigrateAnalytics set_errorLevelCore_1:]
+ -[MRPlaybackSessionMigrateAnalytics set_errorLevel_0:]
+ -[MRPlaybackSessionMigrateAnalytics set_errorLevel_1:]
+ -[MRPlaybackSessionMigrateAnalytics set_errorOnion:]
+ -[MRPlaybackSessionMigrateAnalytics set_handoffAppBundle:]
+ -[MRPlaybackSessionMigrateAnalytics set_handoffDestination:]
+ -[MRPlaybackSessionMigrateAnalytics set_handoffDestinationPerformanceClass:]
+ -[MRPlaybackSessionMigrateAnalytics set_handoffInitiator:]
+ -[MRPlaybackSessionMigrateAnalytics set_handoffQueueSize:]
+ -[MRPlaybackSessionMigrateAnalytics set_handoffSource:]
+ -[MRPlaybackSessionMigrateAnalytics set_handoffSourcePerformanceClass:]
+ -[MRPlaybackSessionMigrateAnalytics set_isSuccess:]
+ -[MRPlaybackSessionMigrateAnalytics set_postDuration:]
+ -[MRPlaybackSessionMigrateAnalytics set_preDuration:]
+ -[MRPlaybackSessionMigrateAnalytics set_sourcePauseAudioGap:]
+ -[MRPlaybackSessionMigrateAnalytics set_userPerceivedHandoffTime:]
+ -[MRPlaybackSessionMigrateAnalytics sourcePauseAudioGap]
+ -[MRPlaybackSessionMigrateAnalytics userPerceivedHandoffTime]
+ -[MRPlaybackSessionMigratePostMessage error]
+ -[MRPlaybackSessionMigratePostMessage initWithRequest:playerPath:setPlaybackSessionCommandID:]
+ -[MRPlaybackSessionMigratePostMessage metrics]
+ -[MRPlaybackSessionMigratePostMessage playerPath]
+ -[MRPlaybackSessionMigratePostMessage request]
+ -[MRPlaybackSessionMigratePostMessage setMetrics:]
+ -[MRPlaybackSessionMigratePostMessage setPlaybackSessionCommandID]
+ -[MRPlaybackSessionMigratePostMessage type]
+ -[MRPlaybackSessionMigrateRequest gatherAnalytics]
+ -[MRPlaybackSessionMigrateRequest setAnalyticsDurationForEvent:duration:]
+ -[MRUserSettings systemBootAllowance]
+ -[_MRMediaRemoteMessageProtobuf hasPlaybackSessionMigratePostMessage]
+ -[_MRMediaRemoteMessageProtobuf playbackSessionMigratePostMessage]
+ -[_MRMediaRemoteMessageProtobuf setPlaybackSessionMigratePostMessage:]
+ -[_MRPlaybackSessionMigratePostMessageProtobuf .cxx_destruct]
+ -[_MRPlaybackSessionMigratePostMessageProtobuf copyTo:]
+ -[_MRPlaybackSessionMigratePostMessageProtobuf copyWithZone:]
+ -[_MRPlaybackSessionMigratePostMessageProtobuf description]
+ -[_MRPlaybackSessionMigratePostMessageProtobuf dictionaryRepresentation]
+ -[_MRPlaybackSessionMigratePostMessageProtobuf error]
+ -[_MRPlaybackSessionMigratePostMessageProtobuf hasError]
+ -[_MRPlaybackSessionMigratePostMessageProtobuf hasMetrics]
+ -[_MRPlaybackSessionMigratePostMessageProtobuf hasPlayerPath]
+ -[_MRPlaybackSessionMigratePostMessageProtobuf hasRequest]
+ -[_MRPlaybackSessionMigratePostMessageProtobuf hasSetPlaybackSessionCommandID]
+ -[_MRPlaybackSessionMigratePostMessageProtobuf hash]
+ -[_MRPlaybackSessionMigratePostMessageProtobuf isEqual:]
+ -[_MRPlaybackSessionMigratePostMessageProtobuf mergeFrom:]
+ -[_MRPlaybackSessionMigratePostMessageProtobuf metrics]
+ -[_MRPlaybackSessionMigratePostMessageProtobuf playerPath]
+ -[_MRPlaybackSessionMigratePostMessageProtobuf readFrom:]
+ -[_MRPlaybackSessionMigratePostMessageProtobuf request]
+ -[_MRPlaybackSessionMigratePostMessageProtobuf setError:]
+ -[_MRPlaybackSessionMigratePostMessageProtobuf setMetrics:]
+ -[_MRPlaybackSessionMigratePostMessageProtobuf setPlaybackSessionCommandID]
+ -[_MRPlaybackSessionMigratePostMessageProtobuf setPlayerPath:]
+ -[_MRPlaybackSessionMigratePostMessageProtobuf setRequest:]
+ -[_MRPlaybackSessionMigratePostMessageProtobuf setSetPlaybackSessionCommandID:]
+ -[_MRPlaybackSessionMigratePostMessageProtobuf writeTo:]
+ GCC_except_table116
+ GCC_except_table118
+ GCC_except_table120
+ GCC_except_table121
+ GCC_except_table136
+ GCC_except_table139
+ GCC_except_table141
+ GCC_except_table142
+ GCC_except_table150
+ GCC_except_table151
+ GCC_except_table153
+ GCC_except_table158
+ GCC_except_table163
+ GCC_except_table164
+ GCC_except_table165
+ GCC_except_table166
+ GCC_except_table185
+ GCC_except_table186
+ GCC_except_table303
+ GCC_except_table77
+ OBJC_IVAR_$_MRAVConcreteOutputDevice._supportsMultiplayerOverride
+ OBJC_IVAR_$__MRMediaRemoteMessageProtobuf._playbackSessionMigratePostMessage
+ OBJC_IVAR_$__MRPlaybackSessionMigratePostMessageProtobuf._error
+ OBJC_IVAR_$__MRPlaybackSessionMigratePostMessageProtobuf._metrics
+ OBJC_IVAR_$__MRPlaybackSessionMigratePostMessageProtobuf._playerPath
+ OBJC_IVAR_$__MRPlaybackSessionMigratePostMessageProtobuf._request
+ OBJC_IVAR_$__MRPlaybackSessionMigratePostMessageProtobuf._setPlaybackSessionCommandID
+ _MRMediaRemotePlaybackSessionSetMigratePostCallback
+ _MRMediaRemotePlaybackSessionSetMigratePostCallbackForOrigin
+ _MRMediaRemoteSendPlaybackSessionMigratePost
+ _MRMediaRemoteServiceSendPlaybackSessionMigratePost
+ _MRServiceClientPlaybackSessionMigratePostCallback
+ _OBJC_CLASS_$_MRPlaybackSessionMigrateAnalytics
+ _OBJC_CLASS_$_MRPlaybackSessionMigratePostMessage
+ _OBJC_CLASS_$__MRPlaybackSessionMigratePostMessageProtobuf
+ _OBJC_IVAR_$_MRDeviceInfo._preferredClusterLeaderID
+ _OBJC_IVAR_$_MRMediaRemoteServiceClient._currentSessionPlayerPathDate
+ _OBJC_IVAR_$_MRMediaRemoteServiceClient._currentSessionRoutingContextID
+ _OBJC_IVAR_$_MRMediaRemoteServiceClient._currentSessionRoutingContextIDDate
+ _OBJC_IVAR_$_MRMediaRemoteServiceClient._weakMediaSuggestionElectedDeviceObservers
+ _OBJC_IVAR_$_MRMediaSuggestionElectedDeviceObserver._observing
+ _OBJC_IVAR_$_MRNowPlayingOriginClient._playbackSessionMigratePostCallback
+ _OBJC_IVAR_$_MRNowPlayingPlayerClientCallbacks._playbackSessionMigratePostCallback
+ _OBJC_IVAR_$_MRPlaybackSessionMigrateAnalytics._data
+ _OBJC_IVAR_$_MRPlaybackSessionMigrateAnalytics._playPerfFields
+ _OBJC_IVAR_$_MRPlaybackSessionMigrateRequest._analytics
+ _OBJC_METACLASS_$_MRPlaybackSessionMigrateAnalytics
+ _OBJC_METACLASS_$_MRPlaybackSessionMigratePostMessage
+ _OBJC_METACLASS_$__MRPlaybackSessionMigratePostMessageProtobuf
+ __MRPlaybackSessionMigratePostMessageProtobufReadFrom
+ __OBJC_$_INSTANCE_METHODS_MRDeviceInfo(MRNowPlayingSessionManagerDataSourceAdditions|MRActiveRoutesObserverAdditions|MRProtocolMessageLoggerAdditions)
+ __OBJC_$_INSTANCE_METHODS_MRPlaybackSessionMigrateAnalytics
+ __OBJC_$_INSTANCE_METHODS_MRPlaybackSessionMigratePostMessage
+ __OBJC_$_INSTANCE_METHODS__MRPlaybackSessionMigratePostMessageProtobuf
+ __OBJC_$_INSTANCE_VARIABLES_MRPlaybackSessionMigrateAnalytics
+ __OBJC_$_INSTANCE_VARIABLES__MRPlaybackSessionMigratePostMessageProtobuf
+ __OBJC_$_PROP_LIST_MRPlaybackSessionMigrateAnalytics
+ __OBJC_$_PROP_LIST_MRPlaybackSessionMigratePostMessage
+ __OBJC_$_PROP_LIST__MRPlaybackSessionMigratePostMessageProtobuf
+ __OBJC_CLASS_PROTOCOLS_$__MRPlaybackSessionMigratePostMessageProtobuf
+ __OBJC_CLASS_RO_$_MRPlaybackSessionMigrateAnalytics
+ __OBJC_CLASS_RO_$_MRPlaybackSessionMigratePostMessage
+ __OBJC_CLASS_RO_$__MRPlaybackSessionMigratePostMessageProtobuf
+ __OBJC_METACLASS_RO_$_MRPlaybackSessionMigrateAnalytics
+ __OBJC_METACLASS_RO_$_MRPlaybackSessionMigratePostMessage
+ __OBJC_METACLASS_RO_$__MRPlaybackSessionMigratePostMessageProtobuf
+ ___37-[MRUserSettings systemBootAllowance]_block_invoke
+ ___47-[MRMediaRemoteServiceClient _resumeConnection]_block_invoke.46
+ ___47-[MRMediaSuggestionElectedDeviceObserver start]_block_invoke
+ ___48-[MRMediaRemoteServiceClient _registerCallbacks]_block_invoke_12
+ ___48-[MRMediaRemoteServiceClient _registerCallbacks]_block_invoke_13
+ ___50-[MRPlaybackSessionMigrateRequest gatherAnalytics]_block_invoke
+ ___60-[MRMediaRemoteServiceClient currentSessionRoutingContextID]_block_invoke
+ ___62-[MRNowPlayingOriginClient playbackSessionMigratePostCallback]_block_invoke
+ ___64-[MRMediaRemoteServiceClient setCurrentSessionRoutingContextID:]_block_invoke
+ ___66-[MRNowPlayingOriginClient setPlaybackSessionMigratePostCallback:]_block_invoke
+ ___69-[MRMediaRemoteService mediaSuggestionDeviceUIDWithQueue:completion:]_block_invoke
+ ___71-[MRNowPlayingPlayerClientCallbacks playbackSessionMigratePostCallback]_block_invoke
+ ___74-[MRNowPlayingClient enqueueCommand:options:playerPath:commandCompletion:]_block_invoke.310
+ ___75-[MRNowPlayingPlayerClientCallbacks setPlaybackSessionMigratePostCallback:]_block_invoke
+ ___89-[MRMediaSuggestionElectedDeviceObserver deviceAvailableForMediaSuggestionsNotification:]_block_invoke
+ ___MRMediaRemoteSendPlaybackSessionMigratePost_block_invoke
+ ___MRMediaRemoteSendPlaybackSessionMigratePost_block_invoke.cold.1
+ ___MRMediaRemoteServiceSendPlaybackSessionMigratePost_block_invoke
+ ___MRServiceClientPlaybackSessionMigratePostCallback_block_invoke
+ ____MRMediaRemoteGetDeviceUIDWithRetryIntervals_block_invoke.450
+ ____MRMediaRemoteGetDeviceUIDWithRetryIntervals_block_invoke.451
+ ____MRPSMPerformLegacyMigration_block_invoke.139
+ ____MRPSMPerformLegacyMigration_block_invoke_2.143
+ ____MRPSMPerformLegacyMigration_block_invoke_29
+ ____MRPSMPerformLegacyMigration_block_invoke_3.144
+ ____MRPSMPerformLegacyMigration_block_invoke_30
+ ____MRPSMPerformLegacyMigration_block_invoke_31
+ ____MRPSMPerformLegacyMigration_block_invoke_32
+ ____MRPSMPerformLegacyMigration_block_invoke_33
+ ____MRPSMPerformLegacyMigration_block_invoke_34
+ ____MRPSMPerformLegacyMigration_block_invoke_35
+ ____MRPSMPerformLegacyMigration_block_invoke_36
+ ____MRPSMPerformLegacyMigration_block_invoke_36.cold.1
+ ____MRPSMPerformLegacyMigration_block_invoke_4.145
+ ___block_descriptor_110_e8_32s40s48s56s64s72s80s_e19_"NSDictionary"8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_descriptor_40_e8_32s_e30_v24?0"NSString"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32s_e57_v24?0"MRPlaybackSessionMigratePostMessage"8"NSError"16ls32l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e57_v24?0"MRPlaybackSessionMigratePostMessage"8"NSError"16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_68_e8_32s40s48s56bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56bs64r_e24_v16?0?<v?"NSError">8ls32l8s56l8s40l8s48l8r64l8
+ ___block_descriptor_94_e8_32s40s48s56s64s72s_e34_v24?0"MRDeviceInfo"8"NSError"16ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.202
+ ___block_literal_global.243
+ ___block_literal_global.245
+ ___block_literal_global.249
+ ___block_literal_global.264
+ ___block_literal_global.276
+ ___block_literal_global.286
+ ___block_literal_global.38
+ ___block_literal_global.42
+ ___block_literal_global.448
+ ___block_literal_global.589
+ ___block_literal_global.592
+ ___block_literal_global.619
+ ___block_literal_global.654
+ _objc_msgSend$addMediaSuggestionElectedDeviceObserver:
+ _objc_msgSend$currentSessionRoutingContextID
+ _objc_msgSend$electedDeviceIdentifier
+ _objc_msgSend$initWithRequest:playerPath:setPlaybackSessionCommandID:
+ _objc_msgSend$isObserving
+ _objc_msgSend$mediaSuggestionDeviceUIDWithQueue:completion:
+ _objc_msgSend$mr_deviceInfo
+ _objc_msgSend$mr_effectiveRoutingContextID
+ _objc_msgSend$mr_origin
+ _objc_msgSend$msv_analyticSignature
+ _objc_msgSend$msv_underlyingError
+ _objc_msgSend$playPerfFields
+ _objc_msgSend$playbackSessionMigratePostCallback
+ _objc_msgSend$playbackSessionMigratePostMessage
+ _objc_msgSend$preferredClusterLeaderID
+ _objc_msgSend$removeMediaSuggestionElectedDeviceObserver:
+ _objc_msgSend$setCurrentSessionRoutingContextID:
+ _objc_msgSend$setElectedDeviceIdentifier:
+ _objc_msgSend$setHandoffAppBundleFromString:
+ _objc_msgSend$setHandoffDestinationFromMRDeviceClass:
+ _objc_msgSend$setHandoffInitiatorFromString:
+ _objc_msgSend$setHandoffSourceFromMRDeviceClass:
+ _objc_msgSend$setObserving:
+ _objc_msgSend$setPlayPerfFields:
+ _objc_msgSend$setPlaybackSessionCommandID
+ _objc_msgSend$setPlaybackSessionMigratePostCallback:
+ _objc_msgSend$setPlaybackSessionMigratePostMessage:
+ _objc_msgSend$setPreferredClusterLeaderID:
+ _objc_msgSend$setSetPlaybackSessionCommandID:
+ _objc_msgSend$set_durationApply:
+ _objc_msgSend$set_durationApply_SetPlaybackSessionCommand:
+ _objc_msgSend$set_durationDetermineRecipe:
+ _objc_msgSend$set_durationFinalize:
+ _objc_msgSend$set_durationPrepare:
+ _objc_msgSend$set_errorLevelCore_0:
+ _objc_msgSend$set_errorLevelCore_1:
+ _objc_msgSend$set_errorLevel_0:
+ _objc_msgSend$set_errorLevel_1:
+ _objc_msgSend$set_errorOnion:
+ _objc_msgSend$set_handoffAppBundle:
+ _objc_msgSend$set_handoffDestination:
+ _objc_msgSend$set_handoffDestinationPerformanceClass:
+ _objc_msgSend$set_handoffInitiator:
+ _objc_msgSend$set_handoffQueueSize:
+ _objc_msgSend$set_handoffSource:
+ _objc_msgSend$set_handoffSourcePerformanceClass:
+ _objc_msgSend$set_isSuccess:
+ _objc_msgSend$set_postDuration:
+ _objc_msgSend$set_preDuration:
+ _objc_msgSend$systemUptime
+ _systemBootAllowance.onceToken
+ _systemBootAllowance.support
- -[MRDeviceInfo clusterLeaderID]
- -[MRDeviceInfo setClusterLeaderID:]
- -[MRPlaybackSessionMigrateRequest analyticsPayload]
- GCC_except_table104
- GCC_except_table119
- GCC_except_table122
- GCC_except_table123
- GCC_except_table124
- GCC_except_table125
- GCC_except_table126
- GCC_except_table140
- GCC_except_table145
- GCC_except_table146
- GCC_except_table147
- GCC_except_table154
- GCC_except_table161
- GCC_except_table162
- GCC_except_table187
- GCC_except_table188
- GCC_except_table299
- GCC_except_table50
- GCC_except_table53
- GCC_except_table73
- _MRNowPlayingSessionManagerLocalDeviceRoutingContextID.__lock
- _MRNowPlayingSessionManagerLocalDeviceRoutingContextID.__routingContextID
- _OBJC_IVAR_$_MRDeviceInfo._clusterLeaderID
- __OBJC_$_INSTANCE_METHODS_MRDeviceInfo(MRActiveRoutesObserverAdditions|MRProtocolMessageLoggerAdditions)
- ___47-[MRMediaRemoteServiceClient _resumeConnection]_block_invoke.43
- ___51-[MRPlaybackSessionMigrateRequest analyticsPayload]_block_invoke
- ___74-[MRNowPlayingClient enqueueCommand:options:playerPath:commandCompletion:]_block_invoke.306
- ___78-[MRV2NowPlayingController _onQueue_retrieveEndpointForContextUID:completion:]_block_invoke
- ___78-[MRV2NowPlayingController _onQueue_retrieveEndpointForContextUID:completion:]_block_invoke_2
- ____MRMediaRemoteGetDeviceUIDWithRetryIntervals_block_invoke.447
- ____MRMediaRemoteGetDeviceUIDWithRetryIntervals_block_invoke.448
- ____MRPSMPerformLegacyMigration_block_invoke.134
- ____MRPSMPerformLegacyMigration_block_invoke_2.138
- ____MRPSMPerformLegacyMigration_block_invoke_28.cold.1
- ____MRPSMPerformLegacyMigration_block_invoke_3.139
- ____MRPSMPerformLegacyMigration_block_invoke_4.140
- ___block_descriptor_106_e8_32s40s48s56s64s72s80s_e19_"NSDictionary"8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
- ___block_descriptor_32_e55_B16?0"_MRPlaybackSessionMigrateRequestEventProtobuf"8l
- ___block_descriptor_72_e8_32s40s48s56bs64r_e24_v16?0?<v?"NSError">8ls32l8s56l8s40l8r64l8s48l8
- ___block_descriptor_90_e8_32s40s48s56s64s72s_e34_v24?0"MRDeviceInfo"8"NSError"16ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_literal_global.107
- ___block_literal_global.162
- ___block_literal_global.195
- ___block_literal_global.236
- ___block_literal_global.238
- ___block_literal_global.240
- ___block_literal_global.262
- ___block_literal_global.274
- ___block_literal_global.282
- ___block_literal_global.445
- ___block_literal_global.583
- ___block_literal_global.586
- ___block_literal_global.613
- ___block_literal_global.648
CStrings:
+ "\v"
+ "    electedDeviceIdentifier = %@\n    observing = %d\n"
+ " cluster-leader"
+ "<%@:%p %s\"%@\" uid=\"%@\" %@ %@bluetooth_id=%@%@ type=%@ subtype=%@%@ clusterType=%@%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%@%s%s%s%s%@ %@%@%@%@>"
+ "@\"MRPlaybackSessionMigrateAnalytics\""
+ "@\"_MRPlaybackSessionMigratePostMessageProtobuf\""
+ "Command"
+ "MRNowPlayingSessionManagerDataSourceAdditions"
+ "MRPlaybackSessionMigrateAnalytics"
+ "MRPlaybackSessionMigratePostMessage"
+ "Migration Analytics: %{public}@"
+ "NoLocalEndpointConnection (recent reboot detected)"
+ "PlaybackSessionMigratePost"
+ "Post"
+ "T@\"NSMutableDictionary\",&,N,V_data"
+ "T@\"NSMutableDictionary\",&,N,V_playPerfFields"
+ "T@\"NSNumber\",&,D,N,Sset_destinationPlayAudioGap:"
+ "T@\"NSNumber\",&,D,N,Sset_durationApply:"
+ "T@\"NSNumber\",&,D,N,Sset_durationApply_SetPlaybackSessionCommand:"
+ "T@\"NSNumber\",&,D,N,Sset_durationDetermineRecipe:"
+ "T@\"NSNumber\",&,D,N,Sset_durationFinalize:"
+ "T@\"NSNumber\",&,D,N,Sset_durationPrepare:"
+ "T@\"NSNumber\",&,D,N,Sset_handoffQueueSize:"
+ "T@\"NSNumber\",&,D,N,Sset_isSuccess:"
+ "T@\"NSNumber\",&,D,N,Sset_postDuration:"
+ "T@\"NSNumber\",&,D,N,Sset_preDuration:"
+ "T@\"NSNumber\",&,D,N,Sset_sourcePauseAudioGap:"
+ "T@\"NSNumber\",&,D,N,Sset_userPerceivedHandoffTime:"
+ "T@\"NSString\",&,D,N,Sset_errorLevelCore_0:"
+ "T@\"NSString\",&,D,N,Sset_errorLevelCore_1:"
+ "T@\"NSString\",&,D,N,Sset_errorLevel_0:"
+ "T@\"NSString\",&,D,N,Sset_errorLevel_1:"
+ "T@\"NSString\",&,D,N,Sset_errorOnion:"
+ "T@\"NSString\",&,N,V_setPlaybackSessionCommandID"
+ "T@\"NSString\",C,N,V_preferredClusterLeaderID"
+ "T@\"_MRDictionaryProtobuf\",&,N,V_metrics"
+ "T@\"_MRPlaybackSessionMigratePostMessageProtobuf\",&,N,V_playbackSessionMigratePostMessage"
+ "TB,N,GisObserving,V_observing"
+ "TQ,D,N,Sset_handoffAppBundle:"
+ "TQ,D,N,Sset_handoffDestination:"
+ "TQ,D,N,Sset_handoffDestinationPerformanceClass:"
+ "TQ,D,N,Sset_handoffInitiator:"
+ "TQ,D,N,Sset_handoffSource:"
+ "TQ,D,N,Sset_handoffSourcePerformanceClass:"
+ "TQ,N,V_playbackSessionSize"
+ "Valeria"
+ "_MRPlaybackSessionMigratePostMessageProtobuf"
+ "_analytics"
+ "_currentSessionPlayerPathDate"
+ "_currentSessionRoutingContextID"
+ "_currentSessionRoutingContextIDDate"
+ "_observing"
+ "_playPerfFields"
+ "_playbackSessionMigratePostCallback"
+ "_playbackSessionMigratePostMessage"
+ "_preferredClusterLeaderID"
+ "_setPlaybackSessionCommandID"
+ "_supportsMultiplayerOverride"
+ "_weakMediaSuggestionElectedDeviceObservers"
+ "addMediaSuggestionElectedDeviceObserver:"
+ "com.apple.Podcasts"
+ "com.apple.SonicMusic"
+ "com.apple.SonicPodcasts"
+ "com.apple.mediaremote.qhop"
+ "currentSessionPlayerPath = %@ (%lf seconds ago\n"
+ "currentSessionRoutingContextID"
+ "currentSessionRoutingContextID = %@ (%lf seconds ago)\n"
+ "destinationPlayAudioGap"
+ "durationApply"
+ "durationApply_SetPlaybackSessionCommand"
+ "durationDetermineRecipe"
+ "durationFinalize"
+ "durationPrepare"
+ "errorLevelCore_0"
+ "errorLevelCore_1"
+ "errorLevel_0"
+ "errorLevel_1"
+ "errorOnion"
+ "event forcefully closed"
+ "handoffAppBundle"
+ "handoffDestination"
+ "handoffDestinationPerformanceClass"
+ "handoffInitiator"
+ "handoffQueueSize"
+ "handoffSource"
+ "handoffSourcePerformanceClass"
+ "hasPlaybackSessionMigratePostMessage"
+ "hasSetPlaybackSessionCommandID"
+ "initWithRequest:playerPath:setPlaybackSessionCommandID:"
+ "internal"
+ "isObserving"
+ "isSuccess"
+ "isSystemCaptureDevice"
+ "mediaSuggestionDeviceUIDWithQueue:completion:"
+ "mediaSuggestionElectedDeviceObservers = %@\n"
+ "mr_effectiveRoutingContextID"
+ "msv_analyticSignature"
+ "msv_underlyingError"
+ "observing"
+ "playPerfFields"
+ "playbackSessionMigratePostCallback"
+ "playbackSessionMigratePostMessage"
+ "postDuration"
+ "preDuration"
+ "preferredClusterLeaderID"
+ "removeMediaSuggestionElectedDeviceObserver:"
+ "sendPlaybackSessionMigratePost"
+ "setCurrentSessionRoutingContextID:"
+ "setElectedDeviceIdentifier:"
+ "setHandoffAppBundleFromString:"
+ "setHandoffDestinationFromMRDeviceClass:"
+ "setHandoffInitiatorFromString:"
+ "setHandoffSourceFromMRDeviceClass:"
+ "setObserving:"
+ "setPlayPerfFields:"
+ "setPlaybackSessionCommandID"
+ "setPlaybackSessionMigratePostCallback:"
+ "setPlaybackSessionMigratePostMessage:"
+ "setPreferredClusterLeaderID:"
+ "setSetPlaybackSessionCommandID:"
+ "set_destinationPlayAudioGap:"
+ "set_durationApply:"
+ "set_durationApply_SetPlaybackSessionCommand:"
+ "set_durationDetermineRecipe:"
+ "set_durationFinalize:"
+ "set_durationPrepare:"
+ "set_errorLevelCore_0:"
+ "set_errorLevelCore_1:"
+ "set_errorLevel_0:"
+ "set_errorLevel_1:"
+ "set_errorOnion:"
+ "set_handoffAppBundle:"
+ "set_handoffDestination:"
+ "set_handoffDestinationPerformanceClass:"
+ "set_handoffInitiator:"
+ "set_handoffQueueSize:"
+ "set_handoffSource:"
+ "set_handoffSourcePerformanceClass:"
+ "set_isSuccess:"
+ "set_postDuration:"
+ "set_preDuration:"
+ "set_sourcePauseAudioGap:"
+ "set_userPerceivedHandoffTime:"
+ "sourcePauseAudioGap"
+ "systemBootAllowance"
+ "systemUptime"
+ "upTime"
+ "userPerceivedHandoffTime"
+ "v24@?0@\"MRPlaybackSessionMigratePostMessage\"8@\"NSError\"16"
- "%@Duration"
- "<%@:%p %s\"%@\" uid=\"%@\" %@ %@bluetooth_id=%@%@ type=%@ subtype=%@%@ clusterType=%@%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%@%s%s%s%s%@ %@%@%@%@>"
- "B16@?0@\"_MRPlaybackSessionMigrateRequestEventProtobuf\"8"
- "T@\"NSString\",C,N,V_clusterLeaderID"
- "Tq,N,V_playbackSessionSize"
- "com.apple.mediaremote.queue-handoff"
- "currentSessionPlayerPath = %@\n"
- "\xa1"

```
