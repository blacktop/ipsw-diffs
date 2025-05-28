## MediaExperience

> `/System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience`

```diff

-125.13.1.2.0
-  __TEXT.__text: 0x18ceec
+130.14.1.1.0
+  __TEXT.__text: 0x190afc
   __TEXT.__auth_stubs: 0x1db0
-  __TEXT.__objc_methlist: 0x36a4
-  __TEXT.__cstring: 0x2395d
-  __TEXT.__const: 0x1930
-  __TEXT.__gcc_except_tab: 0x1650
-  __TEXT.__oslogstring: 0x2afd7
+  __TEXT.__objc_methlist: 0x374c
+  __TEXT.__cstring: 0x23fce
+  __TEXT.__const: 0x1938
+  __TEXT.__gcc_except_tab: 0x169c
+  __TEXT.__oslogstring: 0x2b63b
   __TEXT.__dlopen_cstrs: 0x503
-  __TEXT.__unwind_info: 0x386c
+  __TEXT.__unwind_info: 0x38e4
   __TEXT.__objc_classname: 0x388
-  __TEXT.__objc_methname: 0xf13e
-  __TEXT.__objc_methtype: 0x18bc
-  __TEXT.__objc_stubs: 0x9420
-  __DATA_CONST.__got: 0x7e8
-  __DATA_CONST.__const: 0x5ad0
+  __TEXT.__objc_methname: 0xf470
+  __TEXT.__objc_methtype: 0x18d6
+  __TEXT.__objc_stubs: 0x95c0
+  __DATA_CONST.__got: 0x7f0
+  __DATA_CONST.__const: 0x5bc8
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x5970
-  __DATA_CONST.__objc_selrefs: 0x2800
+  __DATA_CONST.__objc_const: 0x5a70
+  __DATA_CONST.__objc_selrefs: 0x2870
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__cfstring: 0x14e00
-  __AUTH_CONST.__const: 0x32a8
+  __AUTH_CONST.__cfstring: 0x15120
+  __AUTH_CONST.__const: 0x32c8
   __AUTH_CONST.__objc_const: 0xca0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_ptr: 0x8

   __AUTH.__objc_data: 0xa0
   __DATA.__objc_classrefs: 0x210
   __DATA.__objc_superrefs: 0xe8
-  __DATA.__objc_ivar: 0x5e4
-  __DATA.__data: 0x1fd8
+  __DATA.__objc_ivar: 0x5fc
+  __DATA.__data: 0x1fe0
   __DATA.__common: 0xd0
-  __DATA.__bss: 0x850
+  __DATA.__bss: 0x858
   __DATA_DIRTY.__objc_data: 0x910
   __DATA_DIRTY.__bss: 0x150
   __DATA_DIRTY.__common: 0x60

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4768
-  Symbols:   15417
-  CStrings:  8526
+  Functions: 4804
+  Symbols:   15538
+  CStrings:  8611
 
Symbols:
+ -[MXCoreSession badgeType]
+ -[MXCoreSession preferredOutputSampleRateSetByClient]
+ -[MXCoreSession sessionPropertiesLock]
+ -[MXCoreSession setBadgeType:]
+ -[MXCoreSession setPreferredOutputSampleRateSetByClient:]
+ -[MXCoreSession setSessionPropertiesLock:]
+ -[MXCoreSession setSupportedOutputChannelLayouts:]
+ -[MXCoreSession supportedOutputChannelLayouts]
+ -[MXSession(InternalUse) copyCurrentlyPlayingBufferedAudioSourceFormatInfo]
+ -[MXSession(InternalUse) setCurrentlyPlayingBufferedAudioFormatInfo:]
+ -[MXSession(InternalUse) updateBadgeType]
+ -[MXSessionManager updateSupportedOutputChannelLayouts]
+ -[MXSessionManager(Utilities) copyEvaluatedBadgeType:]
+ -[MXSessionManager(Utilities) isBTRouteSameDeviceWithDifferentProfile:newNumRoutes:oldRouteTypes:newRouteTypes:oldRouteIdentifiers:newRouteIdentifiers:]
+ GCC_except_table107
+ GCC_except_table109
+ GCC_except_table223
+ GCC_except_table61
+ _CMSMNotificationUtility_PostBadgeTypeDidChange
+ _CMSMNotificationUtility_PostSupportedBufferedAudioCapabilitiesDidChange
+ _CMSMUtility_GetStringForVolumeOperationType
+ _CMSMUtility_UpdateBadgeType
+ _CMSMUtility_UpdateSupportedOutputChannelLayouts
+ _FigPredictedRouting_IsPreemptivePortLogicEnabled
+ _FigRoutingManagerContextUtilities_CacheSupportedOutputChannelLayouts
+ _FigRoutingManagerContextUtilities_CopySupportedOutputChannelLayouts
+ _FigRoutingManagerUtilities_GetEvaluatedBadgeType
+ _FigRoutingManagerUtilities_IsEndpointTypeVehicle
+ _FigRoutingManagerUtilities_RegisterAirPlayStreamCapabilitiesDidChangeListener
+ _FigRoutingManagerUtilities_UnRegisterAirPlayStreamCapabilitiesDidChangeListener
+ _MX_FeatureFlags_IsBufferedBadgingAndCapabilitiesEnabled
+ _MX_FeatureFlags_IsBufferedBadgingAndCapabilitiesEnabled.isBufferedBadgingAndCapabilitiesEnabled
+ _MX_FeatureFlags_IsBufferedBadgingAndCapabilitiesEnabled.onceToken
+ _OBJC_IVAR_$_MXCoreSession._badgeType
+ _OBJC_IVAR_$_MXCoreSession._preferredOutputSampleRateSetByClient
+ _OBJC_IVAR_$_MXCoreSession._sessionPropertiesLock
+ _OBJC_IVAR_$_MXCoreSession._supportedOutputChannelLayouts
+ _OBJC_IVAR_$_MXSession.mBadgeType
+ _OBJC_IVAR_$_MXSession.mCurrentlyPlayingBufferedAudioFormatInfo
+ ___CMSMNotificationUtility_PostBadgeTypeDidChange_block_invoke
+ ___CMSMNotificationUtility_PostSupportedBufferedAudioCapabilitiesDidChange_block_invoke
+ ___CMSMUtility_UpdateSharePlayVolumeBehaviours_block_invoke.398
+ ___FigRoutingManagerContextUtilities_CacheSupportedOutputChannelLayouts_block_invoke
+ ___FigRoutingManagerContextUtilities_CopySupportedOutputChannelLayouts_block_invoke
+ ___FigRoutingManagerUtilities_UnRegisterAirPlayStreamCapabilitiesDidChangeListener_block_invoke
+ ___MX_FeatureFlags_IsBufferedBadgingAndCapabilitiesEnabled_block_invoke
+ ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_48_e8_32o40w_e5_v8?0lw40l8s32l8
+ ___block_literal_global.397
+ ___block_literal_global.406
+ ___block_literal_global.408
+ ___block_literal_global.96
+ ___routingManagerUtilities_handleAirPlayAggregateCapabilitiesChangedNotification_block_invoke
+ _kFigEndpointStreamType_BufferedAudio
+ _kFigRoutingContextGlobalModificationOption_PreemptivePortConnection
+ _kMXSessionNotificationKey_BadgeTypeDidChange_BadgeType
+ _kMXSessionNotificationKey_SupportedOutputChannelLayoutsDidChange_ChannelLayouts
+ _kMXSessionNotification_BadgeTypeDidChange
+ _kMXSessionNotification_SupportedOutputChannelLayoutsDidChange
+ _kMXSessionProperty_BadgeType
+ _kMXSessionProperty_CurrentlyPlayingBufferedAudioFormatInfo
+ _kMXSessionProperty_SupportedOutputChannelLayouts
+ _kMXSessionVolumeChangeLog_MXSessionVolumeOperationType
+ _kMXSession_BadgeType_DolbyAtmos
+ _kMXSession_BadgeType_DolbyAudio
+ _kMXSession_BadgeType_NotApplicable
+ _kMXSession_BadgeType_SpatialAudio
+ _kMXSession_BadgeType_Stereo
+ _kMXSession_BadgeType_Surround
+ _kMXSession_CurrentlyPlayingBufferedAudioFormatInfoKey_ContentType
+ _kMXSession_CurrentlyPlayingBufferedAudioFormatInfo_ContentType_AppleSpatialAudio
+ _kMXSession_CurrentlyPlayingBufferedAudioFormatInfo_ContentType_DolbyAtmos
+ _kMXSession_CurrentlyPlayingBufferedAudioFormatInfo_ContentType_DolbyAudio
+ _kMXSession_CurrentlyPlayingBufferedAudioFormatInfo_ContentType_Stereo
+ _kMXSession_CurrentlyPlayingBufferedAudioFormatInfo_ContentType_Surround
+ _objc_msgSend$badgeType
+ _objc_msgSend$copyCurrentlyPlayingBufferedAudioSourceFormatInfo
+ _objc_msgSend$copyEvaluatedBadgeType:
+ _objc_msgSend$isBTRouteSameDeviceWithDifferentProfile:newNumRoutes:oldRouteTypes:newRouteTypes:oldRouteIdentifiers:newRouteIdentifiers:
+ _objc_msgSend$preferredOutputSampleRateSetByClient
+ _objc_msgSend$sessionPropertiesLock
+ _objc_msgSend$setBadgeType:
+ _objc_msgSend$setCurrentlyPlayingBufferedAudioFormatInfo:
+ _objc_msgSend$setPreferredOutputSampleRateSetByClient:
+ _objc_msgSend$setSupportedOutputChannelLayouts:
+ _objc_msgSend$supportedOutputChannelLayouts
+ _objc_msgSend$updateBadgeType
+ _objc_msgSend$updateSupportedOutputChannelLayouts
+ _routingManagerUtilities_handleAirPlayAggregateCapabilitiesChangedNotification
+ _routingManager_doesVAEndpointRepresentAirPlayDevice
- GCC_except_table57
- GCC_except_table58
- ___CMSMUtility_UpdateSharePlayVolumeBehaviours_block_invoke.388
- ___block_literal_global.387
- ___block_literal_global.396
- ___block_literal_global.398
- ___block_literal_global.88
CStrings:
+ "-CMSMUtilities- %s: Clearing SupportedOutputChannelLayouts to session %{public}@ "
+ "-CMSMUtilities- %s: Have not found applicable session badge type update."
+ "-CMSMUtilities- %s: Have not found applicable session criteria for supportedOutputChannelLayouts, caching supportedOutputChannelLayouts %{public}@"
+ "-CMSMUtilities- %s: Updating SupportedOutputChannelLayouts %{public}@ to session %{public}@ "
+ "-CMSessionMgr- %s: Returning default output volume = %{public}@"
+ "-CMVAEndptMgr- %s: Skipping updating InEarbasedPlaybackState as BT route is same and only suffix has changed oldType = %{public}@ oldRouteID = %{public}@ newType = %{public}@ newRouteID = %{public}@"
+ "-CMVAEndptUtl- %s: Checking if we should create MusicVAD with ports %{public}@"
+ "-CMVAEndptUtl- %s: Creating MusicVAD with port: %d!!!!"
+ "-FigRoutingManager- %s: Coriander airplay connection, let's set mute state on default VAD so audio doesn't escape"
+ "-FigRoutingManager-Utilities %s: Aggregate is not empty continue registration"
+ "-FigRoutingManager-Utilities %s: Already registered."
+ "-FigRoutingManager-Utilities %s: Endpoint with ID %{private}@, name %{public}@ with badgeType %{public}@, isSystemMusicIndependent %{BOOL}u, isAPACSurroundSupported %{public}@"
+ "-FigRoutingManager-Utilities %s: Fake endpoint. Use case is not supported."
+ "-FigRoutingManager-Utilities %s: Stream EndpointID %{public}@ supportedCapabilities='%{public}@'"
+ "-MXCoreSession_Embedded- %s: Setting badgeType from %{public}@ to %{public}@ for MXCoreSession %{public}@"
+ "-MXSession- %s: %{public}@ Setting CurrentlyPlayingBufferedAudioFormatInfo to %{public}@"
+ "-MXSession- %s: Applying badgeType %{public}@ to session %{public}@ "
+ "-MXSession- %s: Session %{public}@ is not applicable for nowPlaying consideration, badgeType does not apply."
+ "-MXSessionManager- %s: Capabilities %{public}@ have not changed for session %{public}@ "
+ "-MXSessionManager- %s: Updating SupportedOutputChannelLayouts %{public}@ to session %{public}@ "
+ "-MXSessionManager- %s: Updating device sample rate cache.."
+ "-MX_FeatureFlags- %s: AirPlay/BufferedBadgingAndCapabilities feature is %{public}s"
+ "-[MXCoreSession setBadgeType:]"
+ "-[MXSession(InternalUse) setCurrentlyPlayingBufferedAudioFormatInfo:]"
+ "-[MXSession(InternalUse) updateBadgeType]"
+ "-[MXSessionManager updateSupportedOutputChannelLayouts]"
+ "21:32:49"
+ "AppleSpatialAudio"
+ "AudioCapabilitiesChanged"
+ "Automatic"
+ "B56@0:8I16I20@24@32@40@48"
+ "BadgeType"
+ "BadgeTypeDidChange"
+ "BufferedBadgingAndCapabilities"
+ "CMSMNotificationUtility_PostBadgeTypeDidChange"
+ "CMSMNotificationUtility_PostSupportedBufferedAudioCapabilitiesDidChange"
+ "CMSMUtility_UpdateBadgeType"
+ "CMSMUtility_UpdateSupportedOutputChannelLayouts"
+ "ContentType"
+ "CurrentlyPlayingBufferedAudioFormatInfo"
+ "DeviceSupportsUSBTypeC"
+ "DolbyAtmos"
+ "DolbyAudio"
+ "FakeAirPlayAggregate"
+ "FigRoutingManagerContextUtilities_CacheSupportedOutputChannelLayouts"
+ "FigRoutingManagerContextUtilities_CopySupportedOutputChannelLayouts"
+ "FigRoutingManagerCreateEndpointActivateOptions"
+ "FigRoutingManagerUtilities_GetEvaluatedBadgeType"
+ "FigRoutingManagerUtilities_RegisterAirPlayStreamCapabilitiesDidChangeListener"
+ "FigRoutingManagerUtilities_UnRegisterAirPlayStreamCapabilitiesDidChangeListener"
+ "FigRoutingManager_Utilities_Embedded.m"
+ "MXSessionVolumeOperationType"
+ "MX_FeatureFlags_IsBufferedBadgingAndCapabilitiesEnabled_block_invoke"
+ "Nov 13 2023"
+ "PreemptivePortConnection"
+ "SpatialAudio"
+ "SupportedAudioCapabilities"
+ "SupportedAudioCapabilities_SupportedChannelLayoutTags"
+ "SupportedOutputChannelLayouts"
+ "SupportedOutputChannelLayoutsDidChange"
+ "SupportsDCXForSpatialAudio"
+ "Surround"
+ "T@\"NSArray\",&,V_supportedOutputChannelLayouts"
+ "T@\"NSDictionary\",&,N,V_devicesSampleRates"
+ "T@\"NSLock\",&,N,V_sessionPropertiesLock"
+ "T@\"NSString\",&,N,V_badgeType"
+ "TB,N,V_preferredOutputSampleRateSetByClient"
+ "_badgeType"
+ "_preferredOutputSampleRateSetByClient"
+ "_sessionPropertiesLock"
+ "_supportedOutputChannelLayouts"
+ "badgeType"
+ "copyCurrentlyPlayingBufferedAudioSourceFormatInfo"
+ "copyEvaluatedBadgeType:"
+ "isBTRouteSameDeviceWithDifferentProfile:newNumRoutes:oldRouteTypes:newRouteTypes:oldRouteIdentifiers:newRouteIdentifiers:"
+ "mBadgeType"
+ "mCurrentlyPlayingBufferedAudioFormatInfo"
+ "preferredInputSampleRate ="
+ "preferredNumberOfInputChannels ="
+ "preferredNumberOfOutputChannels ="
+ "preferredOutputSampleRate ="
+ "preferredOutputSampleRateSetByClient"
+ "preferredOutputSampleRateSetByClient ="
+ "routingManagerUtilities_handleAirPlayAggregateCapabilitiesChangedNotification"
+ "sessionPropertiesLock"
+ "setBadgeType:"
+ "setCurrentlyPlayingBufferedAudioFormatInfo:"
+ "setPreferredOutputSampleRateSetByClient:"
+ "setSessionPropertiesLock:"
+ "setSupportedOutputChannelLayouts:"
+ "supportedOutputChannelLayouts"
+ "updateBadgeType"
+ "updateSupportedOutputChannelLayouts"
+ "vaemHandleNewDeviceConfiguration"
- "-CMSessionMgr- %s: Client '%{public}@' resetting WantsToPauseSpokenAudio while it's active"
- "-CMSessionMgr- %s: Client '%{public}@' setting WantsToPauseSpokenAudio to '%{BOOL}u'"
- "-CMSessionMgr- %s: Error converting the volume to dB. Resetting to 0."
- "-CMSessionMgr- %s: Returning default output volume = %{public}@, OutputVAD = %d"
- "-CMVAEndptUtl- %s: Attempting to create MusicVAD with ports %{public}@"
- "-CMVAEndptUtl- %s: Creating MusicVAD with port: %d"
- "20:15:44"
- "Oct 30 2023"
- "T@\"NSDictionary\",&,V_devicesSampleRates"

```
