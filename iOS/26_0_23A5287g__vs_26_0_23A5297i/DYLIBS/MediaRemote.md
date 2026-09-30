## MediaRemote

> `/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote`

```diff

-4025.100.103.0.0
-  __TEXT.__text: 0x2ea364
+4025.100.108.0.0
+  __TEXT.__text: 0x2ebbb4
   __TEXT.__auth_stubs: 0x16d0
-  __TEXT.__objc_methlist: 0x2a8d8
+  __TEXT.__objc_methlist: 0x2a990
   __TEXT.__const: 0x5f8
-  __TEXT.__cstring: 0x2b51c
-  __TEXT.__oslogstring: 0xd851
-  __TEXT.__gcc_except_tab: 0x6270
+  __TEXT.__cstring: 0x2b68d
+  __TEXT.__oslogstring: 0xd869
+  __TEXT.__gcc_except_tab: 0x6330
   __TEXT.__dlopen_cstrs: 0x514
   __TEXT.__ustring: 0x7a2
-  __TEXT.__unwind_info: 0xb010
+  __TEXT.__unwind_info: 0xb040
   __TEXT.__objc_classname: 0x4cd3
-  __TEXT.__objc_methname: 0x4c33e
-  __TEXT.__objc_methtype: 0x8eb7
-  __TEXT.__objc_stubs: 0x279a0
+  __TEXT.__objc_methname: 0x4c59c
+  __TEXT.__objc_methtype: 0x8ed3
+  __TEXT.__objc_stubs: 0x27b40
   __DATA_CONST.__got: 0x1430
-  __DATA_CONST.__const: 0xacc8
+  __DATA_CONST.__const: 0xae40
   __DATA_CONST.__objc_classlist: 0x1178
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x250
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xec80
+  __DATA_CONST.__objc_selrefs: 0xecd8
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0xfb0
   __DATA_CONST.__objc_arraydata: 0x260
   __AUTH_CONST.__auth_got: 0xb78
-  __AUTH_CONST.__const: 0x3040
-  __AUTH_CONST.__cfstring: 0x22ce0
-  __AUTH_CONST.__objc_const: 0x44f58
+  __AUTH_CONST.__const: 0x3020
+  __AUTH_CONST.__cfstring: 0x22e20
+  __AUTH_CONST.__objc_const: 0x44fd8
   __AUTH_CONST.__objc_arrayobj: 0x180
-  __AUTH_CONST.__objc_intobj: 0x4e0
+  __AUTH_CONST.__objc_intobj: 0x4c8
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x8020
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0x318c
+  __DATA.__objc_ivar: 0x3198
   __DATA.__data: 0x1c20
-  __DATA.__bss: 0x8a0
+  __DATA.__bss: 0x890
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x2e90
   __DATA_DIRTY.__data: 0x48

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 223E80E8-ABE0-37DF-8B35-3EEB2032EF58
-  Functions: 19932
-  Symbols:   54707
-  CStrings:  24105
+  UUID: 2F0A30DD-6A02-39F1-A318-C68493FF1AC6
+  Functions: 19964
+  Symbols:   54793
+  CStrings:  24139
 
Symbols:
+ -[MRAVLightweightReconnaissanceSession searchOutputDeviceUIDs:matchingPredicate:timeout:details:queue:completion:]
+ -[MRAVReconnaissanceSession setShouldLog:]
+ -[MRAVReconnaissanceSession shouldLog]
+ -[MRDeviceInfo resolveOutputDeviceUIDs:]
+ -[MRNowPlayingRequest nowPlayingPlayerPathWithCompletion:]
+ -[MRNowPlayingRequest nowPlayingPlayerPathWithCompletion:].cold.1
+ -[MRNowPlayingRequest requestClientPropertiesWithCompletion:]
+ -[MRNowPlayingRequest requestClientPropertiesWithCompletion:].cold.1
+ -[MRNowPlayingRequest requestDeviceLastPlayingDateWithCompletion:]
+ -[MRNowPlayingRequest requestDeviceLastPlayingDateWithCompletion:].cold.1
+ -[MRNowPlayingRequest requestLastPlayingDateWithCompletion:]
+ -[MRNowPlayingRequest requestLastPlayingDateWithCompletion:].cold.1
+ -[MRNowPlayingRequest requestNowPlayingInfoWithCompletion:]
+ -[MRNowPlayingRequest requestNowPlayingInfoWithCompletion:].cold.1
+ -[MRNowPlayingRequest requestNowPlayingItemArtworkWithCompletion:]
+ -[MRNowPlayingRequest requestNowPlayingItemArtworkWithCompletion:].cold.1
+ -[MRNowPlayingRequest requestNowPlayingItemMetadataWithCompletion:]
+ -[MRNowPlayingRequest requestNowPlayingItemMetadataWithCompletion:].cold.1
+ -[MRNowPlayingRequest requestProxiableSupportedCommandsWithCompletion:]
+ -[MRNowPlayingRequest requestProxiableSupportedCommandsWithCompletion:].cold.1
+ -[MRNowPlayingRequest requestSupportedCommandsWithCompletion:]
+ -[MRNowPlayingRequest requestSupportedCommandsWithCompletion:].cold.1
+ -[MRPlaybackSessionMigrateAnalytics durationApply_SetPlaybackSession]
+ -[MRPlaybackSessionMigrateAnalytics handoffDestinationDeviceType]
+ -[MRPlaybackSessionMigrateAnalytics handoffSourceDeviceType]
+ -[MRPlaybackSessionMigrateAnalytics set_durationApply_SetPlaybackSession:]
+ -[MRPlaybackSessionMigrateAnalytics set_handoffDestinationDeviceType:]
+ -[MRPlaybackSessionMigrateAnalytics set_handoffSourceDeviceType:]
+ -[MRPlaybackSessionMigrateAnalytics set_userPerceivedAudioContinuity:]
+ -[MRPlaybackSessionMigrateAnalytics userPerceivedAudioContinuity]
+ -[MRUpdateActiveSystemEndpointRequest previousOutputDeviceUID]
+ -[MRUpdateActiveSystemEndpointRequest setPreviousOutputDeviceUID:]
+ -[_MRUpdateActiveSystemEndpointRequestProtobuf hasPreviousOutputDeviceUID]
+ -[_MRUpdateActiveSystemEndpointRequestProtobuf previousOutputDeviceUID]
+ -[_MRUpdateActiveSystemEndpointRequestProtobuf setPreviousOutputDeviceUID:]
+ OBJC_IVAR_$__MRUpdateActiveSystemEndpointRequestProtobuf._previousOutputDeviceUID
+ _MRBannerEventDescription
+ _MRPerformAsyncOperationsUntilSuccess
+ _OBJC_IVAR_$_MRAVReconnaissanceSession._shouldLog
+ _OBJC_IVAR_$_MRUpdateActiveSystemEndpointRequest._previousOutputDeviceUID
+ __MRPerformAsyncOperationsUntilSuccess
+ ___114-[MRAVLightweightReconnaissanceSession searchOutputDeviceUIDs:matchingPredicate:timeout:details:queue:completion:]_block_invoke
+ ___114-[MRAVLightweightReconnaissanceSession searchOutputDeviceUIDs:matchingPredicate:timeout:details:queue:completion:]_block_invoke.204
+ ___114-[MRAVLightweightReconnaissanceSession searchOutputDeviceUIDs:matchingPredicate:timeout:details:queue:completion:]_block_invoke.cold.1
+ ___114-[MRAVLightweightReconnaissanceSession searchOutputDeviceUIDs:matchingPredicate:timeout:details:queue:completion:]_block_invoke_2
+ ___114-[MRAVLightweightReconnaissanceSession searchOutputDeviceUIDs:matchingPredicate:timeout:details:queue:completion:]_block_invoke_3
+ ___114-[MRAVLightweightReconnaissanceSession searchOutputDeviceUIDs:matchingPredicate:timeout:details:queue:completion:]_block_invoke_4
+ ___114-[MRAVLightweightReconnaissanceSession searchOutputDeviceUIDs:matchingPredicate:timeout:details:queue:completion:]_block_invoke_5
+ ___40-[MRDeviceInfo resolveOutputDeviceUIDs:]_block_invoke
+ ___58-[MRNowPlayingRequest nowPlayingPlayerPathWithCompletion:]_block_invoke
+ ___59-[MRNowPlayingRequest requestNowPlayingInfoWithCompletion:]_block_invoke
+ ___60-[MRNowPlayingRequest requestLastPlayingDateWithCompletion:]_block_invoke
+ ___60-[MRNowPlayingRequest requestLastPlayingDateWithCompletion:]_block_invoke_2
+ ___60-[MRNowPlayingRequest requestLastPlayingDateWithCompletion:]_block_invoke_2.cold.1
+ ___61-[MRNowPlayingRequest requestClientPropertiesWithCompletion:]_block_invoke
+ ___62-[MRNowPlayingRequest requestSupportedCommandsWithCompletion:]_block_invoke
+ ___66-[MRNowPlayingRequest requestDeviceLastPlayingDateWithCompletion:]_block_invoke
+ ___66-[MRNowPlayingRequest requestDeviceLastPlayingDateWithCompletion:]_block_invoke.80
+ ___66-[MRNowPlayingRequest requestDeviceLastPlayingDateWithCompletion:]_block_invoke.86
+ ___66-[MRNowPlayingRequest requestDeviceLastPlayingDateWithCompletion:]_block_invoke.cold.1
+ ___66-[MRNowPlayingRequest requestDeviceLastPlayingDateWithCompletion:]_block_invoke_2
+ ___66-[MRNowPlayingRequest requestNowPlayingItemArtworkWithCompletion:]_block_invoke
+ ___67-[MRNowPlayingRequest requestNowPlayingItemMetadataWithCompletion:]_block_invoke
+ ___71-[MRNowPlayingRequest requestProxiableSupportedCommandsWithCompletion:]_block_invoke
+ ____MRMediaRemoteGetDeviceUIDWithRetryIntervals_block_invoke.453
+ ____MRMediaRemoteGetDeviceUIDWithRetryIntervals_block_invoke.454
+ ____MRPerformAsyncOperationsUntilSuccess_block_invoke
+ ___block_descriptor_106_e8_32s40s48s56s64s72s80s_e19_"NSDictionary"8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_descriptor_40_e8_32s_e18_16?0"NSString"8ls32l8
+ ___block_descriptor_48_e8_32s40bs_e30_v24?0"MRClient"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e31_v24?0"MRArtwork"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e38_v24?0"MRAVOutputDevice"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e43_v24?0"MRContentItemMetadata"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40r_e22_B16?0"MRAVEndpoint"8lr40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48r_e35_v24?0"MRDestination"8"NSError"16ls40l8r48l8s32l8
+ ___block_descriptor_56_e8_32s40s48r_e26_B16?0"MRAVOutputDevice"8lr48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs56r_e24_v24?0^v8^{__CFError=}16lr56l8s48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e35_v24?0"MRDestination"8"NSError"16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56bs64bs_e17_v16?0"NSArray"8ls32l8s56l8s64l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56bs64r_e28_v24?0"NSDate"8"NSError"16lr64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e28_v24?0"NSDate"8"NSError"16ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_77_e8_32s40s48s_e19_"NSDictionary"8?0ls32l8s40l8s48l8
+ ___block_descriptor_84_e8_32s40s48s56bs_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72bs80r_e38_v24?0"MRAVOutputDevice"8"NSError"16ls32l8r80l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_90_e8_32s40s48s56s64s72s_e34_v24?0"MRDeviceInfo"8"NSError"16ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.451
+ ___block_literal_global.595
+ ___block_literal_global.622
+ ___block_literal_global.657
+ _objc_msgSend$nowPlayingPlayerPathWithCompletion:
+ _objc_msgSend$previousOutputDeviceUID
+ _objc_msgSend$requestClientPropertiesWithCompletion:
+ _objc_msgSend$requestDeviceLastPlayingDateWithCompletion:
+ _objc_msgSend$requestLastPlayingDateWithCompletion:
+ _objc_msgSend$requestNowPlayingInfoWithCompletion:
+ _objc_msgSend$requestNowPlayingItemArtworkWithCompletion:
+ _objc_msgSend$requestNowPlayingItemMetadataWithCompletion:
+ _objc_msgSend$requestProxiableSupportedCommandsWithCompletion:
+ _objc_msgSend$requestSupportedCommandsWithCompletion:
+ _objc_msgSend$setPreviousOutputDeviceUID:
+ _objc_msgSend$setTransitionStyle:
+ _objc_msgSend$set_durationApply_SetPlaybackSession:
+ _objc_msgSend$set_handoffDestinationDeviceType:
+ _objc_msgSend$set_handoffSourceDeviceType:
+ _objc_msgSend$sharedSystemAudioLocalEndpoint
- -[MRNowPlayingRequest nowPlayingPlayerPathOnQueue:completion:].cold.1
- -[MRNowPlayingRequest requestClientPropertiesOnQueue:completion:].cold.1
- -[MRNowPlayingRequest requestDeviceLastPlayingDateOnQueue:completion:].cold.1
- -[MRNowPlayingRequest requestLastPlayingDateOnQueue:completion:].cold.1
- -[MRNowPlayingRequest requestNowPlayingInfoOnQueue:completion:].cold.1
- -[MRNowPlayingRequest requestNowPlayingItemArtworkOnQueue:completion:].cold.1
- -[MRNowPlayingRequest requestNowPlayingItemMetadataOnQueue:completion:].cold.1
- -[MRNowPlayingRequest requestProxiableSupportedCommandsOnQueue:completion:].cold.1
- -[MRNowPlayingRequest requestSupportedCommandsOnQueue:completion:].cold.1
- -[MRPlaybackSessionMigrateAnalytics destinationPlayAudioGap]
- -[MRPlaybackSessionMigrateAnalytics durationApply_SetPlaybackSessionCommand]
- -[MRPlaybackSessionMigrateAnalytics handoffDestination]
- -[MRPlaybackSessionMigrateAnalytics handoffSource]
- -[MRPlaybackSessionMigrateAnalytics set_destinationPlayAudioGap:]
- -[MRPlaybackSessionMigrateAnalytics set_durationApply_SetPlaybackSessionCommand:]
- -[MRPlaybackSessionMigrateAnalytics set_handoffDestination:]
- -[MRPlaybackSessionMigrateAnalytics set_handoffSource:]
- -[MRPlaybackSessionMigrateAnalytics set_sourcePauseAudioGap:]
- -[MRPlaybackSessionMigrateAnalytics sourcePauseAudioGap]
- -[MRUserSettings systemBootAllowance]
- ___37-[MRUserSettings systemBootAllowance]_block_invoke
- ___64-[MRNowPlayingRequest requestLastPlayingDateOnQueue:completion:]_block_invoke.69
- ___64-[MRNowPlayingRequest requestLastPlayingDateOnQueue:completion:]_block_invoke_2.cold.1
- ___66-[MRAVReconnaissanceSession beginSearchWithTimeout:mapCompletion:]_block_invoke.cold.1
- ___70-[MRNowPlayingRequest requestDeviceLastPlayingDateOnQueue:completion:]_block_invoke.76
- ___70-[MRNowPlayingRequest requestDeviceLastPlayingDateOnQueue:completion:]_block_invoke.83
- ___70-[MRNowPlayingRequest requestDeviceLastPlayingDateOnQueue:completion:]_block_invoke.cold.1
- ___70-[MRNowPlayingRequest requestDeviceLastPlayingDateOnQueue:completion:]_block_invoke_3
- ____MRMediaRemoteGetDeviceUIDWithRetryIntervals_block_invoke.450
- ____MRMediaRemoteGetDeviceUIDWithRetryIntervals_block_invoke.451
- ___block_descriptor_110_e8_32s40s48s56s64s72s80s_e19_"NSDictionary"8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
- ___block_descriptor_32_e8_B16?08l
- ___block_descriptor_40_e8_32r_e22_B16?0"MRAVEndpoint"8lr32l8
- ___block_descriptor_64_e8_32s40s48bs56r_e35_v24?0"MRDestination"8"NSError"16ls48l8r56l8s32l8s40l8
- ___block_descriptor_72_e8_32s40s48s56bs64r_e24_v24?0^v8^{__CFError=}16lr64l8s32l8s56l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e35_v24?0"MRDestination"8"NSError"16ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_76_e8_32s40s48s56bs_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8
- ___block_descriptor_77_e8_32s40s48s56s_e19_"NSDictionary"8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_80_e8_32s40s48s56s64bs72r_e28_v24?0"NSDate"8"NSError"16lr72l8s32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_80_e8_32s40s48s56s64s72bs_e28_v24?0"NSDate"8"NSError"16ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_descriptor_94_e8_32s40s48s56s64s72s_e34_v24?0"MRDeviceInfo"8"NSError"16ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_literal_global.448
- ___block_literal_global.589
- ___block_literal_global.619
- ___block_literal_global.654
- ___trackAnalyticsSendCommand_block_invoke_3
- _objc_msgSend$set_durationApply_SetPlaybackSessionCommand:
- _objc_msgSend$set_handoffDestination:
- _objc_msgSend$set_handoffSource:
- _systemBootAllowance.onceToken
- _systemBootAllowance.support
CStrings:
+ "Dismissed"
+ "GetPlaybackSession callback unavailable"
+ "LOCAL_DEVICE"
+ "LongPress"
+ "MRAVLightweightReconnaissanceSession.searchOutputDeviceUIDsWithPredicate"
+ "MigrateBegin callback unavailable"
+ "MigrateFinalize callback unavailable"
+ "MigratePost callback unavailable"
+ "NoMatchingOutputDevicesFound"
+ "Presented"
+ "T@\"NSNumber\",&,D,N,Sset_durationApply_SetPlaybackSession:"
+ "T@\"NSNumber\",&,D,N,Sset_userPerceivedAudioContinuity:"
+ "T@\"NSString\",&,N,V_previousOutputDeviceUID"
+ "T@\"NSString\",C,N,V_previousOutputDeviceUID"
+ "TQ,D,N,Sset_handoffDestinationDeviceType:"
+ "TQ,D,N,Sset_handoffSourceDeviceType:"
+ "Tapped"
+ "Unknown (Use CommandResult.error for more accurate errors)"
+ "[ReconnaissanceSession] WHAPRO: Discovery found %@ in %f seconds %{public}@"
+ "_previousOutputDeviceUID"
+ "durationApply_SetPlaybackSession"
+ "handoffDestinationDeviceType"
+ "handoffSourceDeviceType"
+ "hasPreviousOutputDeviceUID"
+ "nowPlayingPlayerPathWithCompletion:"
+ "predicate"
+ "previousOutputDeviceUID"
+ "requestClientPropertiesWithCompletion:"
+ "requestDeviceLastPlayingDateWithCompletion:"
+ "requestLastPlayingDateWithCompletion:"
+ "requestNowPlayingInfoWithCompletion:"
+ "requestNowPlayingItemArtworkWithCompletion:"
+ "requestNowPlayingItemMetadataWithCompletion:"
+ "requestProxiableSupportedCommandsWithCompletion:"
+ "requestSupportedCommandsWithCompletion:"
+ "resolveOutputDeviceUIDs:"
+ "searchOutputDeviceUIDs:matchingPredicate:timeout:details:queue:completion:"
+ "setPreviousOutputDeviceUID:"
+ "set_durationApply_SetPlaybackSession:"
+ "set_handoffDestinationDeviceType:"
+ "set_handoffSourceDeviceType:"
+ "set_userPerceivedAudioContinuity:"
+ "userPerceivedAudioContinuity"
+ "v24@?0@\"MRContentItemMetadata\"8@\"NSError\"16"
+ "v64@0:8@16@?24d32@40@48@?56"
- "B16@?0@8"
- "T@\"NSNumber\",&,D,N,Sset_destinationPlayAudioGap:"
- "T@\"NSNumber\",&,D,N,Sset_durationApply_SetPlaybackSessionCommand:"
- "T@\"NSNumber\",&,D,N,Sset_sourcePauseAudioGap:"
- "TQ,D,N,Sset_handoffDestination:"
- "TQ,D,N,Sset_handoffSource:"
- "WHAPRO: Discovery found %@ in %f seconds %{public}@"
- "destinationPlayAudioGap"
- "durationApply_SetPlaybackSessionCommand"
- "event forcefully closed"
- "handoffDestination"
- "handoffSource"
- "internal"
- "set_destinationPlayAudioGap:"
- "set_durationApply_SetPlaybackSessionCommand:"
- "set_handoffDestination:"
- "set_handoffSource:"
- "set_sourcePauseAudioGap:"
- "sourcePauseAudioGap"
- "systemBootAllowance"

```
