## MediaExperience

> `/System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience`

```diff

-385.10.1.0.0
-  __TEXT.__text: 0x253af8
+390.6.1.0.0
+  __TEXT.__text: 0x257ad4
   __TEXT.__delay_helper: 0x304
   __TEXT.__lazy_helpers: 0xfc
-  __TEXT.__objc_methlist: 0x8c18
-  __TEXT.__cstring: 0x39bc8
-  __TEXT.__const: 0x1d30
-  __TEXT.__gcc_except_tab: 0x5028
-  __TEXT.__oslogstring: 0x52afd
+  __TEXT.__objc_methlist: 0x8d80
+  __TEXT.__cstring: 0x39f51
+  __TEXT.__const: 0x1d40
+  __TEXT.__gcc_except_tab: 0x5068
+  __TEXT.__oslogstring: 0x533cf
   __TEXT.__dlopen_cstrs: 0x613
-  __TEXT.__unwind_info: 0x8210
+  __TEXT.__unwind_info: 0x82c0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x73c0
-  __DATA_CONST.__objc_classlist: 0x330
+  __DATA_CONST.__const: 0x7438
+  __DATA_CONST.__objc_classlist: 0x348
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5688
+  __DATA_CONST.__objc_selrefs: 0x5750
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x300
+  __DATA_CONST.__objc_superrefs: 0x318
   __DATA_CONST.__objc_arraydata: 0xf8
-  __DATA_CONST.__got: 0xd38
-  __AUTH_CONST.__const: 0x4a28
-  __AUTH_CONST.__cfstring: 0x1c4c0
-  __AUTH_CONST.__objc_const: 0xd630
+  __DATA_CONST.__got: 0xd58
+  __AUTH_CONST.__const: 0x4ac8
+  __AUTH_CONST.__cfstring: 0x1c7e0
+  __AUTH_CONST.__objc_const: 0xd9c8
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__lazy_load_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x78

   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x18b0
+  __AUTH.__objc_data: 0x19a0
   __AUTH.__data: 0x630
-  __DATA.__objc_ivar: 0xcf0
+  __DATA.__objc_ivar: 0xd1c
   __DATA.__data: 0x1450
   __DATA.__common: 0x5d0
   __DATA_DIRTY.__objc_data: 0x730
-  __DATA_DIRTY.__bss: 0xce8
+  __DATA_DIRTY.__bss: 0xd00
   __DATA_DIRTY.__common: 0x60
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 10247
-  Symbols:   13721
-  CStrings:  10082
+  Functions: 10310
+  Symbols:   13809
+  CStrings:  10137
 
Symbols:
+ +[MXMusicVADPlaybackTracker sharedInstance]
+ +[MXSysdiagnoseVolumeLogging sharedInstance]
+ -[MXAirPlayPredictedRouting prepareForConversationalAppEndpointActivation]
+ -[MXCoreSession isAirPlayOdeonSetupSession]
+ -[MXCoreSession setIsAirPlayOdeonSetupSession:]
+ -[MXCoreSession updateDetailedRouteDescriptionForInputIfNeeded:]
+ -[MXCoreSession updateDetailedRouteDescriptionForOutputIfNeeded:]
+ -[MXMusicVADPlaybackTracker bundleIDForSession:]
+ -[MXMusicVADPlaybackTracker cachePlaybackStateForMusicVADSession:]
+ -[MXMusicVADPlaybackTracker cachePlaybackStateForMusicVADSessionsOnRouteChange]
+ -[MXMusicVADPlaybackTracker dealloc]
+ -[MXMusicVADPlaybackTracker init]
+ -[MXMusicVADPlaybackTracker musicVADWasCreated]
+ -[MXMusicVADPlaybackTracker musicVADWasDestroyed]
+ -[MXMusicVADPlaybackTracker resetMusicVADLifetimeState]
+ -[MXMusicVADPlaybackTracker sendPlaybackSummaryWithAppSwitchOccurred:]
+ -[MXPendingVolumeOperationLog clientName]
+ -[MXPendingVolumeOperationLog dealloc]
+ -[MXPendingVolumeOperationLog framework]
+ -[MXPendingVolumeOperationLog initWithClientName:framework:reason:volumeButtonClientName:logSuppressed:]
+ -[MXPendingVolumeOperationLog logSuppressed]
+ -[MXPendingVolumeOperationLog reason]
+ -[MXPendingVolumeOperationLog volumeButtonClientName]
+ -[MXSysdiagnoseVolumeLogging clear]
+ -[MXSysdiagnoseVolumeLogging dealloc]
+ -[MXSysdiagnoseVolumeLogging pendingLog]
+ -[MXSysdiagnoseVolumeLogging setPendingLog:]
+ -[MXSysdiagnoseVolumeLogging setupVolumeOperationLogWithClientName:framework:reason:volumeButtonClientName:logSuppressed:]
+ -[MXSysdiagnoseVolumeLogging writeVolumeOperationLogForCategory:route:routeIdentifier:routeSubtype:volume:]
+ GCC_except_table120
+ GCC_except_table64
+ GCC_except_table727
+ _CFStringGetRangeOfComposedCharactersAtIndex
+ _OBJC_CLASS_$_MXMusicVADPlaybackTracker
+ _OBJC_CLASS_$_MXPendingVolumeOperationLog
+ _OBJC_CLASS_$_MXSysdiagnoseVolumeLogging
+ _OBJC_CLASS_$_NSLocale
+ _OBJC_IVAR_$_MXAirPlayPredictedRoutesRegistry.mConversationalAppBundleIDs
+ _OBJC_IVAR_$_MXAirPlayPredictedRoutesRegistry.mDiscoveryTxtRecordsByBundleID
+ _OBJC_IVAR_$_MXCoreSession._isAirPlayOdeonSetupSession
+ _OBJC_IVAR_$_MXMusicVADPlaybackTracker.mDidAppSwitchOccur
+ _OBJC_IVAR_$_MXMusicVADPlaybackTracker.mFirstAppThatPlayedToMusicVAD
+ _OBJC_IVAR_$_MXMusicVADPlaybackTracker.mIsMusicVADPresent
+ _OBJC_IVAR_$_MXPendingVolumeOperationLog.mClientName
+ _OBJC_IVAR_$_MXPendingVolumeOperationLog.mFramework
+ _OBJC_IVAR_$_MXPendingVolumeOperationLog.mLogSuppressed
+ _OBJC_IVAR_$_MXPendingVolumeOperationLog.mReason
+ _OBJC_IVAR_$_MXPendingVolumeOperationLog.mVolumeButtonClientName
+ _OBJC_IVAR_$_MXSysdiagnoseVolumeLogging.mPendingLog
+ _OBJC_METACLASS_$_MXMusicVADPlaybackTracker
+ _OBJC_METACLASS_$_MXPendingVolumeOperationLog
+ _OBJC_METACLASS_$_MXSysdiagnoseVolumeLogging
+ _PVMIsGlobalVolumeCategory
+ __OBJC_$_CLASS_METHODS_MXMusicVADPlaybackTracker
+ __OBJC_$_CLASS_METHODS_MXSysdiagnoseVolumeLogging
+ __OBJC_$_INSTANCE_METHODS_MXMusicVADPlaybackTracker
+ __OBJC_$_INSTANCE_METHODS_MXPendingVolumeOperationLog
+ __OBJC_$_INSTANCE_METHODS_MXSysdiagnoseVolumeLogging
+ __OBJC_$_INSTANCE_VARIABLES_MXMusicVADPlaybackTracker
+ __OBJC_$_INSTANCE_VARIABLES_MXPendingVolumeOperationLog
+ __OBJC_$_INSTANCE_VARIABLES_MXSysdiagnoseVolumeLogging
+ __OBJC_$_PROP_LIST_MXPendingVolumeOperationLog
+ __OBJC_$_PROP_LIST_MXSysdiagnoseVolumeLogging
+ __OBJC_CLASS_RO_$_MXMusicVADPlaybackTracker
+ __OBJC_CLASS_RO_$_MXPendingVolumeOperationLog
+ __OBJC_CLASS_RO_$_MXSysdiagnoseVolumeLogging
+ __OBJC_METACLASS_RO_$_MXMusicVADPlaybackTracker
+ __OBJC_METACLASS_RO_$_MXPendingVolumeOperationLog
+ __OBJC_METACLASS_RO_$_MXSysdiagnoseVolumeLogging
+ ___107-[MXSysdiagnoseVolumeLogging writeVolumeOperationLogForCategory:route:routeIdentifier:routeSubtype:volume:]_block_invoke
+ ___43+[MXMusicVADPlaybackTracker sharedInstance]_block_invoke
+ ___44+[MXSysdiagnoseVolumeLogging sharedInstance]_block_invoke
+ ___44+[MXSysdiagnoseVolumeLogging sharedInstance]_block_invoke_2
+ ___44+[MXSysdiagnoseVolumeLogging sharedInstance]_block_invoke_3
+ ___block_descriptor_202_e5_v8?0l
+ ___block_descriptor_57_e8_32r40r_e5_v8?0lr32l8r40l8
+ ___block_descriptor_68_e8_32o40o48o56o_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_93_e8_32r40r_e5_v8?0lr32l8r40l8
+ ___cmsmCopySystemSoundVolumeBehaviorForCurrentVAD_block_invoke
+ ___mxsvlGetTimestampFormatter_block_invoke
+ _cmsmGetAudioHardwareControlFlagsForSystemSound
+ _cmsmSetVolumeForSystemSound
+ _cmsmUpdateAudioHardwareControlFlagsOnActiveSessions
+ _cmsmUpdateSystemSoundVolume
+ _gVolumeOperationQueue
+ _gVolumeOperationSampleStartTimes
+ _gVolumeOperations
+ _kCMSession_AudioBehaviorKey_SystemSound_OutputVAD
+ _kMXMusicVADPlaybackLog_AppSwitchOccurredDuringAirPlay
+ _kMXMusicVADPlaybackLog_SessionPlaybackSummary
+ _kMXSessionProperty_IsAirPlayOdeonSetupSession
+ _kMXSession_InSystemSoundDetailsKey_VolumeRequeryOnly
+ _mxsvlGetNewestOperationDate
+ _mxsvlGetOperationIdentity
+ _mxsvlGetTimestampFormatter.onceToken
+ _mxsvlGetTimestampFormatter.sTimestampFormatter
+ _mxsvlSanitizeOperationField
+ _mxsvlShouldRetainRouteForever
+ _mxsvlWriteOperationsPreference
+ _mxvcSetupVolumeOperationLogForSysdiagnose
- -[MXCoreSession copyDetailedRouteDescriptionForContinuityScreenOutput:]
- -[MXSystemController hasEntitlementForRemoteDeviceControlByConversationApp]
- -[MXSystemController setHasEntitlementForRemoteDeviceControlByConversationApp:]
- GCC_except_table109
- GCC_except_table725
- GCC_except_table96
- _OBJC_IVAR_$_MXSystemController._hasEntitlementForRemoteDeviceControlByConversationApp
- _OUTLINED_FUNCTION_165
- _OUTLINED_FUNCTION_166
- ___block_descriptor_194_e5_v8?0l
- ___block_descriptor_85_e8_32r40r_e5_v8?0lr32l8r40l8
- _pvmIsGlobalVolumeCategory
CStrings:
+ " (newest)"
+ " (oldest)"
+ "%@(%@)"
+ "%@~%.3f~%@~%@~%@"
+ "%@~%@"
+ "%@~%@~%@~%@"
+ "-CMSessionMgr- %s: Allow session '%{public}@' activation because it has PebbleInteraction predicted routes and is eligible to become the NowPlayingApp"
+ "-CMSessionMgr- %s: Skipping begin interruption for %{public}@ because it is the AirPlay Odeon setup session and a Measurement mode session is active"
+ "-FigRoutingManager_iOS- %s: Local AirPlay endpoint name=%{public}@ is dissociated, not adding it to the system music aggregate"
+ "-FigRoutingManager_iOS- %s: Local AirPlay endpoint: name=%{public}@, uid=%{public}@, isDissociated=%{BOOL}u"
+ "-MXAirPlayPredictedRouting- %s: Skipping routing to predicted routes because session '%{public}@' isn't a Pebble-initiated conversational app and isn't on SystemMusic routing context"
+ "-MXMusicVADPlaybackTracker- %s: MusicVAD was created, starting to track apps playing to it"
+ "-MXMusicVADPlaybackTracker- %s: MusicVAD was destroyed without a tracked lifetime, skipping playback summary"
+ "-MXMusicVADPlaybackTracker- %s: Sending playback summary: %{public}@"
+ "-MXMusicVADPlaybackTracker- %s: Session '%{public}@' playing to MusicVAD on behalf of %{public}@ after %{public}@; multiple apps played during this AirPlay session"
+ "-MXMusicVADPlaybackTracker- %s: Session '%{public}@' playing to MusicVAD on behalf of %{public}@, the first app to play during this AirPlay session"
+ "-MXSysdiagnoseVolumeLogging- %s: \t \t \t -> %{public}@%{public}@"
+ "-MXSysdiagnoseVolumeLogging- %s: \t \t Category = %{public}@ (%ld operations)"
+ "-MXSysdiagnoseVolumeLogging- %s: \t Route [%ld] = %{public}@"
+ "-MXSysdiagnoseVolumeLogging- %s: \t Route [%ld] = %{public}@ (untouched for over %ld days, newest operation only)"
+ "-MXSysdiagnoseVolumeLogging- %s: === Volume Operations Cache Dump ==="
+ "-MXSysdiagnoseVolumeLogging- %s: No volume operations cached"
+ "-MXSysdiagnoseVolumeLogging- %s: Total routes cached: %ld"
+ "-MXSystemSounds-"
+ "-MXSystemSounds- %s: Recomputed volume for SSID = %d is silent on output VAD: %{public}@"
+ "-MXSystemSounds- %s: SSID = %d with systemSoundCategory = %{public}@ re-queried: OutVolume = %f for output VAD: %{public}@"
+ "-MXSystemSounds- %s: Volume re-query for SSID = %d by PID = %d; recalculating volume for the current output VAD only, not starting a new sound"
+ "-MXSystemSounds- %s: pOutBehavior is NULL"
+ "-[MXMusicVADPlaybackTracker cachePlaybackStateForMusicVADSession:]"
+ "-[MXMusicVADPlaybackTracker musicVADWasCreated]"
+ "-[MXMusicVADPlaybackTracker musicVADWasDestroyed]"
+ "-[MXMusicVADPlaybackTracker sendPlaybackSummaryWithAppSwitchOccurred:]"
+ "-stark mode- %s: Dropping Shell fade reason: not valid UTF-8"
+ "AVSystemController"
+ "AppSwitchOccurredDuringAirPlay"
+ "CMSessionManager_Utilities"
+ "CarPlayScreenFadeReason"
+ "IsAirPlayOdeonSetupSession"
+ "MXVolume"
+ "MXVolumeOperations"
+ "OutputVAD"
+ "SharePlayCallFollowsMedia"
+ "SharePlayMediaFollowsCall"
+ "VADVolumeChange"
+ "VolumeRequeryOnly"
+ "cmsmCopySystemSoundVolumeBehaviorForCurrentVAD"
+ "cmsmCopySystemSoundVolumeBehaviorForCurrentVAD_block_invoke"
+ "com.apple.MediaExperience.MusicVAD.SessionPlaybackSummary"
+ "com.apple.MediaExperience.sysdiagnoseVolumeLogging"
+ "en_US_POSIX"
+ "fsm_copyShellFadeReason"
+ "isAirPlayOdeonSetupSession ="
+ "mxsvlDumpOperations"
+ "volumeOperations"
+ "yyyy-MM-dd HH:mm:ss"
```
