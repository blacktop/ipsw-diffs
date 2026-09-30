## MediaExperience

> `/System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__lazy_load_got`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-360.66.1.11.1
-  __TEXT.__text: 0x2e8944
+360.70.2.0.0
+  __TEXT.__text: 0x2ebccc
   __TEXT.__delay_helper: 0x304
   __TEXT.__lazy_helpers: 0xfc
-  __TEXT.__objc_methlist: 0x8748
-  __TEXT.__cstring: 0x4e3ed
-  __TEXT.__const: 0x1cd8
-  __TEXT.__gcc_except_tab: 0x51a8
-  __TEXT.__oslogstring: 0x782da
+  __TEXT.__objc_methlist: 0x87e8
+  __TEXT.__cstring: 0x4e827
+  __TEXT.__const: 0x1cf8
+  __TEXT.__gcc_except_tab: 0x5248
+  __TEXT.__oslogstring: 0x790b0
   __TEXT.__dlopen_cstrs: 0x613
-  __TEXT.__unwind_info: 0x6370
+  __TEXT.__unwind_info: 0x6410
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x7330
+  __DATA_CONST.__const: 0x7350
   __DATA_CONST.__objc_classlist: 0x310
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x53a8
+  __DATA_CONST.__objc_selrefs: 0x5420
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x2e0
   __DATA_CONST.__objc_arraydata: 0xf8
   __DATA_CONST.__got: 0xd08
-  __AUTH_CONST.__const: 0x48e8
-  __AUTH_CONST.__cfstring: 0x1c360
-  __AUTH_CONST.__objc_const: 0xce50
+  __AUTH_CONST.__const: 0x4908
+  __AUTH_CONST.__cfstring: 0x1c3e0
+  __AUTH_CONST.__objc_const: 0xcec0
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__lazy_load_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x78

   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x1d10
   __AUTH.__data: 0x5f0
-  __DATA.__objc_ivar: 0xc64
+  __DATA.__objc_ivar: 0xc70
   __DATA.__data: 0x1408
-  __DATA.__bss: 0x12b0
+  __DATA.__bss: 0x12b8
   __DATA.__common: 0x680
   __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__bss: 0xd90

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 11549
-  Symbols:   16110
-  CStrings:  14173
+  Functions: 11574
+  Symbols:   16164
+  CStrings:  14222
 
Symbols:
+ -[MXCustomRoutingController currentSystemMirroringRoutes]
+ -[MXCustomRoutingSession releasePlaybackAssertion]
+ -[MXCustomRoutingSession takePlaybackAssertion]
+ -[MXNowPlayingAppManager canCurrentCustomRoutingSessionBeNowPlaying]
+ -[MXNowPlayingAppManager currentCustomRoutingSession]
+ -[MXNowPlayingAppManager customRoutingSessionPlaybackStateDidChangeCallback:]
+ -[MXNowPlayingAppManager doesCurrentCustomRoutingSessionEligibleForNowPlayingMatchPID:]
+ -[MXNowPlayingAppManager isCurrentCustomRoutingSessionNowPlaying]
+ -[MXNowPlayingAppManager routingSessionControllerCurrentSessionDidChangeCallback:]
+ -[MXNowPlayingAppManager setCurrentCustomRoutingSession:]
+ -[MXNowPlayingAppManager updateCurrentCustomRoutingSession]
+ -[MXSessionManager(Utilities) isVolumeScalableCategory:]
+ -[MXSessionManager(Utilities) synchronizeSessionVolumeWithMediaVolumeIfNeeded:mediaWasPlaying:route:]
+ -[MXSessionManager(Utilities) tryToTakeControlFlagsOnDefaultVAD:routingFlagIsNotControlled:]
+ -[MXSessionResumptionContext copyActiveRoutesOnContextCreationIfAwaitingActivation]
+ -[MXSessionResumptionContext updateActiveRoutesOnContextCreationIfChangedAfterActivationForSession:previousActiveRoutes:]
+ -[MXSystemCastingExtensionInstance handleForSelf]
+ GCC_except_table145
+ GCC_except_table89
+ _CMSUtility_GetVolumeScalingFactorForCategory
+ _CMSUtility_GetVolumeScalingFactorForCategory.onceToken
+ _CMSUtility_GetVolumeScalingFactorForCategory.sAlarmScalingFactors
+ _CMSUtility_GetVolumeScalingFactorForCategory.sVoiceOverScalingFactors
+ _CMSystemSoundMgrGetMaxVoiceOverVolumeOnSystemLocalVAD
+ _CMSystemSoundMgrIsJBLSystemSoundPlayingOverSystemLocalVAD
+ _FigXPCCommonServerTimeoutHandler
+ _MXCustomRoutingSessionControllerCurrentSessionDidChangeNotification
+ _MX_CoreServices_CopyLocalizedApplicationName
+ _OBJC_IVAR_$_MXCustomRoutingController.mSystemMirroringContext
+ _OBJC_IVAR_$_MXCustomRoutingSession.mLock
+ _OBJC_IVAR_$_MXCustomRoutingSession.mPlaybackAssertion
+ _OBJC_IVAR_$_MXNowPlayingAppManager._currentCustomRoutingSession
+ _OBJC_IVAR_$_MXNowPlayingAppManager.mCustomRoutingSessionController
+ _PVMGetRawVolumeForRouteFromVolume
+ ___77-[MXNowPlayingAppManager customRoutingSessionPlaybackStateDidChangeCallback:]_block_invoke
+ ___82-[MXNowPlayingAppManager routingSessionControllerCurrentSessionDidChangeCallback:]_block_invoke
+ ___CMSUtility_GetVolumeScalingFactorForCategory_block_invoke
+ ___customEndpoint_timeoutActivationIfWaitingForPort_block_invoke
+ _figXPC_ServerTimeout_EndpointUIAgent
+ _figXPC_ServerTimeout_FigSTS
+ _figXPC_ServerTimeout_FigSystemController
+ _figXPC_ServerTimeout_FigVolumeClient
+ _figXPC_ServerTimeout_FigVolumeController
+ _figXPC_ServerTimeout_RouteDiscoverer
+ _figXPC_ServerTimeout_RoutingContext
+ _figXPC_ServerTimeout_RoutingSessionManager
+ _figXPC_ServerTimeout_StarkModeController
+ _figXPC_ServerTimeout_SystemMediaCastingController
+ _gMDEDeviceTimerPolicy
+ _kFigEndpointUIAgentPromptInfo_FailureDetails_MediaAppName
+ _kMXSessionAudioCategory_HomeDeviceHourlyChime
+ _objc_msgSend$canCurrentCustomRoutingSessionBeNowPlaying
+ _objc_msgSend$copyActiveRoutesOnContextCreationIfAwaitingActivation
+ _objc_msgSend$currentCustomRoutingSession
+ _objc_msgSend$currentSystemMirroringRoutes
+ _objc_msgSend$doesCurrentCustomRoutingSessionEligibleForNowPlayingMatchPID:
+ _objc_msgSend$handleForSelf
+ _objc_msgSend$isCurrentCustomRoutingSessionNowPlaying
+ _objc_msgSend$isVolumeScalableCategory:
+ _objc_msgSend$localizedName
+ _objc_msgSend$releasePlaybackAssertion
+ _objc_msgSend$setCurrentCustomRoutingSession:
+ _objc_msgSend$synchronizeSessionVolumeWithMediaVolumeIfNeeded:mediaWasPlaying:route:
+ _objc_msgSend$takePlaybackAssertion
+ _objc_msgSend$tryToTakeControlFlagsOnDefaultVAD:routingFlagIsNotControlled:
+ _objc_msgSend$updateActiveRoutesOnContextCreationIfChangedAfterActivationForSession:previousActiveRoutes:
+ _objc_msgSend$updateCurrentCustomRoutingSession
+ _sCarPlayVideoBannerUUID
+ _updateControlFlagsAfterRouteChange:systemLocalVADState:musicVADState:.sIsUpdatingControlFlagsAfterRouteChange
+ _vaemSuppressVolumeForwardingOnVAD
- -[MXSessionManager(Utilities) isVolumeScalableSession:]
- -[MXSessionManager(Utilities) synchronizeSessionVolumeWithMediaVolumeIfNeeded:]
- -[MXSessionManager(Utilities) tryToTakeControlFlagsOnDefaultVAD:]
- GCC_except_table144
- GCC_except_table80
- GCC_except_table86
- _OBJC_IVAR_$_MXSystemCastingExtensionInstance.mProcessHandle
- _OBJC_IVAR_$_MXSystemCastingExtensionManager.mProcessHandle
- _OUTLINED_FUNCTION_422
- ___cmsutility_getScalingFactorForSessionCategory_block_invoke
- _cmsutility_getScalingFactorForSessionCategory.onceToken
- _cmsutility_getScalingFactorForSessionCategory.sAlarmScalingFactors
- _cmsutility_getScalingFactorForSessionCategory.sVoiceOverScalingFactors
- _objc_msgSend$isVolumeScalableSession:
- _objc_msgSend$synchronizeSessionVolumeWithMediaVolumeIfNeeded:
- _objc_msgSend$tryToTakeControlFlagsOnDefaultVAD:
CStrings:
+ "-CMSM_CoreServices- %s: Failed to find a localized name for %{public}@"
+ "-CMSUtilities- %s: Mixable voice assistant session interrupting CarPlay video session '%@'"
+ "-CMSessionManager_NowPlaying- %s: Current NowPlaying app is based on custom routing session, appDisplayID: %{public}@"
+ "-CMSessionMgr- %s: Not switching NowPlayingApp to %{public}@ because system media casting is active"
+ "-CMSessionMgr_MDE- %s: Audio policy: isSomeClientPlayingAudio = %{public}s, shouldStartTimer = %{public}s"
+ "-CMSessionMgr_MDE- %s: MDE idle timer fired (audio): isSomeClientPlayingAudio = %{public}s, stillIdle = %{public}s"
+ "-CMSessionMgr_MDE- %s: MDE idle timer fired (mirroring): screenIsBlanked = %{public}s, isSomeClientPlayingAudio = %{public}s, stillIdle = %{public}s"
+ "-CMSessionMgr_MDE- %s: Mirroring policy: screenIsBlanked = %{public}s, isSomeClientPlayingAudio = %{public}s, shouldStartTimer = %{public}s"
+ "-CMSessionMgr_MDE- %s: creating gCMSM.disconnectMDEDeviceTimer for policy %{public}d, timer delay = %{public}f"
+ "-CMSessionMgr_MDE- %s: gCMSM.disconnectMDEDeviceTimer already armed for policy %{public}d, leaving in place"
+ "-CMVAEndptMgr- %s: CMSMVAUtility_AudioObjectSetPropertyData(kVirtualAudioDevicePropertySuppressVolumeForwarding) failed with err = %d = %c%c%c%c"
+ "-CMVAEndptMgr- %s: Suppressing volume forwarding on VAD %u"
+ "-CMVAEndptMgr- %s: kVirtualAudioDevicePropertySuppressVolumeForwarding is not supported on VAD %u"
+ "-FigCustomEndpoint- %s: Port-publication timeout: deactivate completed result=%{private}@"
+ "-FigRoutingManagerContextUtilities- %s: Activation timeout - removing stale entry and posting EndedFailed for uuid=%{public}@"
+ "-FigRoutingManagerContextUtilities- %s: Posting coalesced notification for original SET operation (entryOptions=%{public}@)"
+ "-FigRoutingManagerContextUtilities- %s: picking timer fired for '%@' '%@' (pickingState=%u)"
+ "-MXCustomRoutingController- %s: Allow session with bundleID: %{public}@ to play using protocolID %{public}@ because we're currently mirroring."
+ "-MXCustomRoutingSession- %s: Failed to take playback assertion for pid %d bundleID %{public}@"
+ "-MXCustomRoutingSession- %s: Invalid pid %d, cannot take playback assertion for %{public}@"
+ "-MXCustomRoutingSession- %s: Releasing playback assertion %p for pid %d bundleID %{public}@"
+ "-MXCustomRoutingSession- %s: Took playback assertion %p for pid %d bundleID %{public}@"
+ "-MXNowPlayingAppManager- %s: \t-------------------------- Custom Routing Information --------------------------"
+ "-MXNowPlayingAppManager- %s: \tCustomRoutingAppPID = %{public}@, CustomRoutingAppDisplayID = %{public}@, CustomRoutingAppIsPlaying = %{BOOL}u, CustomRoutingAppCanBeNowPlaying = %{BOOL}u"
+ "-MXNowPlayingAppManager- %s: Current custom routing app is allowed to be NowPlaying; pid=%d, displayID=%{public}@"
+ "-MXNowPlayingAppManager- %s: CustomRoutingSession displayID=%{public}@, pid=%d, isPlaying=%{BOOL}u, canBeNowPlayingApp=%{BOOL}u, currentNowPlayingAppPID=%d"
+ "-MXNowPlayingAppManager- %s: INTERRUPTING '%{public}@' for system casting Now Playing app"
+ "-MXNowPlayingAppManager- %s: PID %d associated with playing custom routing session is the new playing app"
+ "-MXNowPlayingAppManager- %s: Previous customRoutingSession=%{public}@, displayID=%{public}@, pid=%d, isPlaying=%{BOOL}u; Current customRoutingSession=%{public}@, displayID=%{public}@, pid=%d, isPlaying=%{BOOL}u."
+ "-MXNowPlayingAppManager- %s: Received: %{public}@"
+ "-MXSessionContext- %s: Updating the resumption context current active routes for client %{public}@ as it changed after activation"
+ "-MXSessionManagerUtilities- %s: Resumption context diverged by interruptor but no interruptor session found"
+ "-MXSessionManagerUtilities- %s: Resumption context diverged due to low priority session, skip processing resumption context"
+ "-MXSessionManagerUtilities- %s: Sending resumption context diverged info for %{public}@ ReporterStarted = %{BOOL}u"
+ "-MXSessionManagerUtilities- %s: Skipping flag takeover for %{public}@ to prevent VSYL oscillation."
+ "-MXSessionManagerUtilities- %s: updateControlFlagsAfterRouteChange called re-entrantly; skipping to prevent VSYL oscillation."
+ "-MXSystemSounds- %s: VoiceOver system sounds on VSYL: base volume=%1.3f, scaling factor=%1.3f, scaled volume=%1.3f"
+ "-[MXCustomRoutingSession releasePlaybackAssertion]"
+ "-[MXCustomRoutingSession takePlaybackAssertion]"
+ "-[MXNowPlayingAppManager customRoutingSessionPlaybackStateDidChangeCallback:]"
+ "-[MXNowPlayingAppManager customRoutingSessionPlaybackStateDidChangeCallback:]_block_invoke"
+ "-[MXNowPlayingAppManager routingSessionControllerCurrentSessionDidChangeCallback:]"
+ "-[MXNowPlayingAppManager updateCurrentCustomRoutingSession]"
+ "-[MXSessionManager(Utilities) processSessionResumptionContextIfNeeded:]"
+ "-[MXSessionManager(Utilities) synchronizeSessionVolumeWithMediaVolumeIfNeeded:mediaWasPlaying:route:]"
+ "-[MXSessionManager(Utilities) tryToTakeControlFlagsOnDefaultVAD:routingFlagIsNotControlled:]"
+ "-[MXSessionManager(Utilities) updateControlFlagsAfterRouteChange:systemLocalVADState:musicVADState:]"
+ "-[MXSessionResumptionContext updateActiveRoutesOnContextCreationIfChangedAfterActivationForSession:previousActiveRoutes:]"
+ "-[MXSystemCastingExtensionInstance handleForSelf]"
+ "22:44:50"
+ "CMSMNP_GetNowPlayingAppIsPlaying"
+ "CMSystemSoundMgrGetMaxVoiceOverVolumeOnSystemLocalVAD"
+ "CustomRoutingSessionChanged"
+ "HomeDeviceHourlyChime"
+ "Jul 10 2026"
+ "MX_CoreServices_CopyLocalizedApplicationName"
+ "MediaAppName"
+ "MediaExperience.%d.\"%@\".customRoutingSessionPlaybackAssertion"
+ "PVMGetRawVolumeForRouteFromVolume"
+ "customEndpoint_timeoutActivationIfWaitingForPort_block_invoke"
+ "vaemSuppressVolumeForwardingOnVAD"
- "-CMSessionMgr_MDE- %s: MDE idle timer fired: screenIsBlanked = %{public}s, isSomeClientPlayingTo3PEndpoint = %{public}s, extensionIsMirroring = %{public}s"
- "-CMSessionMgr_MDE- %s: creating gCMSM.disconnectMDEDeviceTimer, timer delay = %{public}f"
- "-CMSessionMgr_MDE- %s: screenIsBlanked = %{public}s, isSomeClientPlayingTo3PEndpoint = %{public}s, extensionIsMirroring = %{public}s, shouldStartTimer = %{public}s"
- "-FigRoutingManagerContextUtilities- %s: picking timer fired for '%@' '%@'"
- "-MXSessionManagerUtilities- %s: Sending resumption context divereged info for %{public}@ ReporterStarted = %{BOOL}u"
- "-MXSystemMediaCastingController_Client- %s: Called"
- "-[MXSessionManager(Utilities) synchronizeSessionVolumeWithMediaVolumeIfNeeded:]"
- "-[MXSessionManager(Utilities) tryToTakeControlFlagsOnDefaultVAD:]"
- "-[MXSystemMediaCastingController_Client didReceiveMediaSourceUpdate:]"
- "21:27:17"
- "Jun 29 2026"
- "cmsmGetMaxVolumeForVoiceOverSystemSound"
```
