## MediaExperience

> `/System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience`

```diff

 385.10.1.0.0
-  __TEXT.__text: 0x24fd98
+  __TEXT.__text: 0x253af8
   __TEXT.__delay_helper: 0x304
   __TEXT.__lazy_helpers: 0xfc
-  __TEXT.__objc_methlist: 0x8a80
-  __TEXT.__cstring: 0x39659
-  __TEXT.__const: 0x1d20
-  __TEXT.__gcc_except_tab: 0x4ef8
-  __TEXT.__oslogstring: 0x51d97
+  __TEXT.__objc_methlist: 0x8c18
+  __TEXT.__cstring: 0x39bc8
+  __TEXT.__const: 0x1d30
+  __TEXT.__gcc_except_tab: 0x5028
+  __TEXT.__oslogstring: 0x52afd
   __TEXT.__dlopen_cstrs: 0x613
-  __TEXT.__unwind_info: 0x8138
+  __TEXT.__unwind_info: 0x8210
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x7340
-  __DATA_CONST.__objc_classlist: 0x320
+  __DATA_CONST.__const: 0x73c0
+  __DATA_CONST.__objc_classlist: 0x330
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x55d8
+  __DATA_CONST.__objc_selrefs: 0x5688
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x2f0
+  __DATA_CONST.__objc_superrefs: 0x300
   __DATA_CONST.__objc_arraydata: 0xf8
-  __DATA_CONST.__got: 0xd28
-  __AUTH_CONST.__const: 0x49c8
-  __AUTH_CONST.__cfstring: 0x1c300
-  __AUTH_CONST.__objc_const: 0xd2a8
+  __DATA_CONST.__got: 0xd38
+  __AUTH_CONST.__const: 0x4a28
+  __AUTH_CONST.__cfstring: 0x1c4c0
+  __AUTH_CONST.__objc_const: 0xd630
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__lazy_load_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x78

   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x1810
+  __AUTH.__objc_data: 0x18b0
   __AUTH.__data: 0x630
-  __DATA.__objc_ivar: 0xcbc
+  __DATA.__objc_ivar: 0xcf0
   __DATA.__data: 0x1450
   __DATA.__common: 0x5d0
   __DATA_DIRTY.__objc_data: 0x730

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 10170
-  Symbols:   13635
-  CStrings:  10014
+  Functions: 10247
+  Symbols:   13721
+  CStrings:  10082
 
Symbols:
+ +[MXRoutingPrewarmingController sharedSystemMusicPrewarmingController]
+ -[MXAirPlayPredictedRouting sessionHasPebbleInteractionPredictedRoutes:]
+ -[MXCoreSessionBase prefersAggressiveEchoCancellation]
+ -[MXCoreSessionBase setPrefersAggressiveEchoCancellation:]
+ -[MXRoutingPrewarmingController cancelPrewarmingIfNotIdle:]
+ -[MXRoutingPrewarmingController dealloc]
+ -[MXRoutingPrewarmingController finishPrewarmBlock]
+ -[MXRoutingPrewarmingController initWithRoutingContextUUID:]
+ -[MXRoutingPrewarmingController predictedRoutesDidChange:forBundleID:]
+ -[MXRoutingPrewarmingController prewarmFinishedWithChannel:predictedRoutes:]
+ -[MXRoutingPrewarmingController prewarmingState]
+ -[MXRoutingPrewarmingController routingContextUUID]
+ -[MXRoutingPrewarmingController sessionDidStartPlaying:shouldMuteSession:]
+ -[MXRoutingPrewarmingController sessionRequiresPrewarming:]
+ -[MXRoutingPrewarmingController setFinishPrewarmBlock:]
+ -[MXRoutingPrewarmingControllerImpl bundleID]
+ -[MXRoutingPrewarmingControllerImpl cancelBlock]
+ -[MXRoutingPrewarmingControllerImpl channel]
+ -[MXRoutingPrewarmingControllerImpl dealloc]
+ -[MXRoutingPrewarmingControllerImpl finishPrewarmBlock]
+ -[MXRoutingPrewarmingControllerImpl prewarmedRouteUUIDs]
+ -[MXRoutingPrewarmingControllerImpl prewarmingState]
+ -[MXRoutingPrewarmingControllerImpl setBundleID:]
+ -[MXRoutingPrewarmingControllerImpl setCancelBlock:]
+ -[MXRoutingPrewarmingControllerImpl setChannel:]
+ -[MXRoutingPrewarmingControllerImpl setFinishPrewarmBlock:]
+ -[MXRoutingPrewarmingControllerImpl setPrewarmedRouteUUIDs:]
+ -[MXRoutingPrewarmingControllerImpl setPrewarmingState:]
+ -[MXVolumeManager(RestingMediaVolume) startRestingMediaVolumeTimer]
+ -[MXVolumeManager(RestingMediaVolume) stopRestingMediaVolumeTimer:]
+ -[MXVolumeManager(RestingMediaVolume) updateMediaVolume:updateHigherThreshold:]
+ GCC_except_table725
+ _AudioObjectSetPropertyData
+ _CMSMDeviceState_ItsAHomeAccessory
+ _CMSMVAUtility_SetPrefersAggressiveEchoCancellation
+ _MX_FeatureFlags_IsBundleIDPredictedRoutingEnabled.isBundleIDPredictedRoutingEnabled
+ _MX_FeatureFlags_IsBundleIDPredictedRoutingEnabled.onceToken
+ _MX_FeatureFlags_IsTopologyPrewarmingEnabled
+ _MX_FeatureFlags_IsTopologyPrewarmingEnabled.isTopologyPrewarming
+ _MX_FeatureFlags_IsTopologyPrewarmingEnabled.onceToken
+ _OBJC_CLASS_$_MXRoutingPrewarmingController
+ _OBJC_CLASS_$_MXRoutingPrewarmingControllerImpl
+ _OBJC_IVAR_$_MXAirPlayPredictedRoutesRegistry.mPebbleInteractionInitiatedRoutes
+ _OBJC_IVAR_$_MXCoreSessionBase._prefersAggressiveEchoCancellation
+ _OBJC_IVAR_$_MXRoutingPrewarmingController._routingContextUUID
+ _OBJC_IVAR_$_MXRoutingPrewarmingController.mPrewarmingControllerImpl
+ _OBJC_IVAR_$_MXRoutingPrewarmingController.mRoutingContextController
+ _OBJC_IVAR_$_MXRoutingPrewarmingControllerImpl._bundleID
+ _OBJC_IVAR_$_MXRoutingPrewarmingControllerImpl._cancelBlock
+ _OBJC_IVAR_$_MXRoutingPrewarmingControllerImpl._channel
+ _OBJC_IVAR_$_MXRoutingPrewarmingControllerImpl._finishPrewarmBlock
+ _OBJC_IVAR_$_MXRoutingPrewarmingControllerImpl._prewarmedRouteUUIDs
+ _OBJC_IVAR_$_MXRoutingPrewarmingControllerImpl._prewarmingState
+ _OBJC_IVAR_$_MXVolumeManager.mRestingVolumeTimer
+ _OBJC_IVAR_$_MXVolumeManager.mTimerDuration
+ _OBJC_METACLASS_$_MXRoutingPrewarmingController
+ _OBJC_METACLASS_$_MXRoutingPrewarmingControllerImpl
+ __OBJC_$_CLASS_METHODS_MXRoutingPrewarmingController
+ __OBJC_$_INSTANCE_METHODS_MXRoutingPrewarmingController
+ __OBJC_$_INSTANCE_METHODS_MXRoutingPrewarmingControllerImpl
+ __OBJC_$_INSTANCE_METHODS_MXVolumeManager(Internal|RestingMediaVolume)
+ __OBJC_$_INSTANCE_VARIABLES_MXRoutingPrewarmingController
+ __OBJC_$_INSTANCE_VARIABLES_MXRoutingPrewarmingControllerImpl
+ __OBJC_$_INSTANCE_VARIABLES_MXVolumeManager
+ __OBJC_$_PROP_LIST_MXRoutingPrewarmingController
+ __OBJC_$_PROP_LIST_MXRoutingPrewarmingControllerImpl
+ __OBJC_CLASS_RO_$_MXRoutingPrewarmingController
+ __OBJC_CLASS_RO_$_MXRoutingPrewarmingControllerImpl
+ __OBJC_METACLASS_RO_$_MXRoutingPrewarmingController
+ __OBJC_METACLASS_RO_$_MXRoutingPrewarmingControllerImpl
+ ___59-[MXRoutingPrewarmingController cancelPrewarmingIfNotIdle:]_block_invoke
+ ___67-[MXVolumeManager(RestingMediaVolume) startRestingMediaVolumeTimer]_block_invoke
+ ___67-[MXVolumeManager(RestingMediaVolume) stopRestingMediaVolumeTimer:]_block_invoke
+ ___70+[MXRoutingPrewarmingController sharedSystemMusicPrewarmingController]_block_invoke
+ ___70-[MXRoutingPrewarmingController predictedRoutesDidChange:forBundleID:]_block_invoke
+ ___70-[MXRoutingPrewarmingController predictedRoutesDidChange:forBundleID:]_block_invoke_2
+ ___CMSMVAUtility_CreateMusicVADIfNeeded_block_invoke
+ ___MX_FeatureFlags_IsBundleIDPredictedRoutingEnabled_block_invoke
+ ___MX_FeatureFlags_IsTopologyPrewarmingEnabled_block_invoke
+ ___PVMSetCurrentState_block_invoke
+ ___block_descriptor_56_e8_32o40o48w_e36_v16?0"MXRoutingPrewarmingChannel"8ls32l8w48l8s40l8
+ ___block_descriptor_56_e8_32o40o48w_e5_v8?0ls32l8s40l8w48l8
+ _cmsmGetMaxVoiceOverVolumeOnVADUID
+ _cmsmShouldJBLSystemSoundSetMediaVolumeOnSiriOutputVAD
+ _getRestingMediaVolumeReasonAsString
+ _kFigEndpointDescriptorKey_AudioRouteSubType_HomeAccessory
+ _kMXSessionProperty_PrefersAggressiveEchoCancellation
+ _sharedSystemMusicPrewarmingController.onceToken
+ _sharedSystemMusicPrewarmingController.sharedController
- GCC_except_table720
- _CMSystemSoundMgrGetMaxVoiceOverVolumeOnSystemLocalVAD
- __OBJC_$_INSTANCE_METHODS_MXVolumeManager(Internal)
CStrings:
+ "-CMSUtilities- %s: Allowing interrupting CurrentlyAirPlayingNowPlayingSession because session '%{public}@' has PebbleInteraction predicted routes"
+ "-CMSessionMgr- %s: Disallow session '%{public}@' activation because it has PebbleInteraction predicted routes and it is NOT eligible to become the NowPlayingApp"
+ "-CMSessionMgr- %s: Session '%{public}@' setting PrefersAggressiveEchoCancellation to %{BOOL}u on input VAD %u"
+ "-CMVAEndptUtl- %s: Error setting kVirtualAudioDevicePropertyAggressiveEC, err = '%c%c%c%c'"
+ "-CMVAEndptUtl- %s: kVirtualAudioDevicePropertyAggressiveEC set to %u for vadID %u"
+ "-MXAirPlayPredictedRoutesRegistry- %s: \t mPebbleInteractionInitiatedRoutes = {"
+ "-MXAirPlayPredictedRoutesRegistry- %s: PebbleInteractionInitiated: BundleID cannot be nil!"
+ "-MXAirPlayPredictedRoutesRegistry- %s: PebbleInteractionInitiated: Removing predicted routes for BundleID='%{public}@'"
+ "-MXAirPlayPredictedRoutesRegistry- %s: PebbleInteractionInitiated: Updating predicted routes for BundleID='%{public}@' to [%{public}@]"
+ "-MXAirPlayPredictedRouting- %s: Session '%{public}@' with BundleID='%{public}@' has PebbleInteractionInitiated predicted routes ['%{public}@']"
+ "-MXCoreSessionSecureCommon- %s: Client %{public}@ setting PrefersAggressiveEchoCancellation to %{BOOL}u"
+ "-MXRoutingPrewarming- %s: Called. predictedRoutesUUIDs: %{public}@ forBundleID: %{public}@. prewarmedRoutesUUIDs: %{public}@ prewarmedBundleID: %{public}@"
+ "-MXRoutingPrewarming- %s: Cancelling prewarming once we get the channel back."
+ "-MXRoutingPrewarming- %s: Found predicted routes: %{public}@ for bundleID: %{public}@."
+ "-MXRoutingPrewarming- %s: Got the channel back. Closing it because something interupted prewarming."
+ "-MXRoutingPrewarming- %s: No predicted routes found for bundleID %{public}@."
+ "-MXRoutingPrewarming- %s: Not doing anything because the controller's routingContextUUID doesn't match the session's routingContextUUID."
+ "-MXRoutingPrewarming- %s: Predicted routes didn't change. State remains unmodified."
+ "-MXRoutingPrewarming- %s: Predicted routes were cleared. Cancelling prewarming."
+ "-MXRoutingPrewarming- %s: Prewarming finished got channel (%p). prewarmingState %ld"
+ "-MXRoutingPrewarming- %s: Resetting state to idle"
+ "-MXRoutingPrewarming- %s: There was an error while prewarming. Resetting state to idle."
+ "-MXSystemSounds- %s: VoiceOver system sound %{public}@ is playing to Siri output VAD while Siri is inactive; using Audio/Video volume %1.3f"
+ "-MXVolumeManager- %s: Current Media Volume is %f, will try and update it."
+ "-MXVolumeManager- %s: Not starting the timer because timer is already running = %{public}@ or someSessionIsPlaying = %{BOOL}u"
+ "-MXVolumeManager- %s: Setting resting volume to %f on route = %{public}@~%{public}@~%{public}@ "
+ "-MXVolumeManager- %s: Starting resting media volume timer. Duration = %llu"
+ "-MXVolumeManager- %s: Stopping resting media volume timer now."
+ "-MXVolumeManager- %s: Stopping timer because '%{public}@'."
+ "-MXVolumeManager- %s: Stopping timer because of reason = %{public}@"
+ "-MXVolumeManager- %s: Stopping timer because timer expired. Updating resting media volumes (if needed)"
+ "-MXVolumeManager- %s: This is a bug, we should never come here. Please file a bug for MediaExperience Session | All."
+ "-MXVolumeManager- %s: Timer fired. Updating resting media volumes (if needed)."
+ "-MX_FeatureFlags- %s: MediaExperience/BundleIDPredictedRouting feature is %{public}s"
+ "-MX_FeatureFlags- %s: Topology Prewarming feature is %{public}s"
+ "-[MXRoutingPrewarmingController cancelPrewarmingIfNotIdle:]"
+ "-[MXRoutingPrewarmingController cancelPrewarmingIfNotIdle:]_block_invoke"
+ "-[MXRoutingPrewarmingController predictedRoutesDidChange:forBundleID:]"
+ "-[MXRoutingPrewarmingController prewarmFinishedWithChannel:predictedRoutes:]"
+ "-[MXRoutingPrewarmingController sessionDidStartPlaying:shouldMuteSession:]"
+ "-[MXRoutingPrewarmingController sessionRequiresPrewarming:]"
+ "-[MXVolumeManager(RestingMediaVolume) startRestingMediaVolumeTimer]"
+ "-[MXVolumeManager(RestingMediaVolume) startRestingMediaVolumeTimer]_block_invoke"
+ "-[MXVolumeManager(RestingMediaVolume) stopRestingMediaVolumeTimer:]"
+ "-[MXVolumeManager(RestingMediaVolume) updateMediaVolume:updateHigherThreshold:]"
+ "BundleIDPredictedRouting"
+ "CMSMVAUtility_CreateMusicVADIfNeeded_block_invoke"
+ "CMSMVAUtility_SetPrefersAggressiveEchoCancellation"
+ "CMSUtility_IsSessionAllowedToInterruptCurrentlyAirPlayingNowPlayingSession"
+ "EndpointSubType_HomeAccessory"
+ "HomeAccessory"
+ "ItsAHomeAccessory ="
+ "MXRoutingPrewarming.m"
+ "MX_FeatureFlags_IsBundleIDPredictedRoutingEnabled_block_invoke"
+ "MX_FeatureFlags_IsTopologyPrewarmingEnabled_block_invoke"
+ "MeterClient_HP"
+ "MeterClient_LP"
+ "Perception"
+ "PrefersAggressiveEchoCancellation"
+ "RouteChanged"
+ "SessionActuallyPlayingAudio"
+ "SharedDSP"
+ "TopologyPrewarming"
+ "UNKNOWN(%d)"
+ "VolumeChanged"
+ "prefersAggressiveEchoCancellation ="
+ "restingVolumeTimerDuration"
+ "v16@?0@\"MXRoutingPrewarmingChannel\"8"
```
