## ToneLibrary

> `/System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary`

```diff

-651.0.0.0.0
-  __TEXT.__text: 0x49590
+653.0.0.0.0
+  __TEXT.__text: 0x4ace4
   __TEXT.__auth_stubs: 0x920
-  __TEXT.__objc_methlist: 0x2d60
+  __TEXT.__objc_methlist: 0x2dd0
   __TEXT.__const: 0x158
-  __TEXT.__gcc_except_tab: 0x16e8
-  __TEXT.__cstring: 0x5c85
-  __TEXT.__oslogstring: 0xd18a
+  __TEXT.__gcc_except_tab: 0x16ec
+  __TEXT.__cstring: 0x5d12
+  __TEXT.__oslogstring: 0xdcdf
   __TEXT.__ustring: 0x4
   __TEXT.__dlopen_cstrs: 0x534
-  __TEXT.__unwind_info: 0x1240
-  __TEXT.__objc_classname: 0x595
-  __TEXT.__objc_methname: 0xa90d
-  __TEXT.__objc_methtype: 0x10fc
-  __TEXT.__objc_stubs: 0x6ee0
+  __TEXT.__unwind_info: 0x1270
+  __TEXT.__objc_classname: 0x597
+  __TEXT.__objc_methname: 0xacec
+  __TEXT.__objc_methtype: 0x1136
+  __TEXT.__objc_stubs: 0x7100
   __DATA_CONST.__got: 0x458
-  __DATA_CONST.__const: 0x1910
+  __DATA_CONST.__const: 0x1950
   __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2070
+  __DATA_CONST.__objc_selrefs: 0x2100
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x120
   __DATA_CONST.__objc_arraydata: 0x58
   __AUTH_CONST.__auth_got: 0x4a8
   __AUTH_CONST.__const: 0x380
-  __AUTH_CONST.__cfstring: 0x5aa0
-  __AUTH_CONST.__objc_const: 0x4d50
+  __AUTH_CONST.__cfstring: 0x5b40
+  __AUTH_CONST.__objc_const: 0x4e40
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0x430
+  __DATA.__objc_ivar: 0x44c
   __DATA.__data: 0x3e0
   __DATA.__common: 0x4
-  __DATA.__bss: 0x238
+  __DATA.__bss: 0x240
   __DATA_DIRTY.__objc_data: 0xbe0
   __DATA_DIRTY.__bss: 0x1d0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 34C587C8-E995-3274-905E-072C8A98383A
-  Functions: 1392
-  Symbols:   5251
-  CStrings:  3781
+  UUID: C45A3319-D38E-37FF-BC44-BE8ED9DD38CE
+  Functions: 1409
+  Symbols:   5310
+  CStrings:  3848
 
Symbols:
+ -[TLAlertPlaybackBeginEvent _initWithAudioSessionReporterID:isForMusicPlayback:]
+ -[TLAlertPlaybackBeginEvent isForMusicPlayback]
+ -[TLAlertQueuePlayerController _applyAudioVolume:forAlert:isForMusicPlayback:phase:]
+ -[TLAlertQueuePlayerController _didEndPlayingAlertForStateDescriptor:isForMusicPlayback:]
+ -[TLAlertQueuePlayerController _didPrepareToPlayMusicForStateDescriptor:withError:]
+ -[TLAlertQueuePlayerController _ensureMusicPlaybackStartedForStateDescriptor:]
+ -[TLAlertQueuePlayerController _ensureMusicPlaybackStartedForStateDescriptor:].cold.1
+ -[TLAlertQueuePlayerController _notifyPlaybackObserverForStateDescriptor:isForMusicPlayback:]
+ -[TLAlertQueuePlayerController _prepareAudioEnvironmentForStateDescriptor:isForMusicPlayback:]
+ -[TLAlertQueuePlayerController _reportAudioStartEventForStateDescriptor:]
+ -[TLAlertQueuePlayerController _restoreAudioEnvironmentForStateDescriptor:isForMusicPlayback:]
+ -[TLAlertQueuePlayerController _startMusicPlaybackForStateDescriptor:mediaItem:]
+ -[TLAlertQueuePlayerController _stopMusicPlayback]
+ -[TLAlertQueuePlayerController _vibrationPatternDictionaryForStateDescriptor:allowsArtificiallyRepeatingPropertyListRepresentation:]
+ -[TLAlertQueuePlayerController _vibrationPatternDictionaryForStateDescriptor:allowsArtificiallyRepeatingPropertyListRepresentation:].cold.1
+ -[TLAlertQueuePlayerController _willBeginPlayingAlertForStateDescriptor:isForMusicPlayback:]
+ -[TLToneManager _toneIdentifierForMediaLibraryItemIdentifier:]
+ GCC_except_table184
+ GCC_except_table38
+ _OBJC_IVAR_$_TLAlertPlaybackBeginEvent._forMusicPlayback
+ _OBJC_IVAR_$_TLAlertQueuePlayerController._hasPreviousAudioVolume
+ _OBJC_IVAR_$_TLAlertQueuePlayerController._isPlayingMusic
+ _OBJC_IVAR_$_TLAlertQueuePlayerController._musicPlaybackCheckTimerSource
+ _OBJC_IVAR_$_TLAlertQueuePlayerController._musicPlaybackVibrationSoundID
+ _OBJC_IVAR_$_TLAlertQueuePlayerController._musicPlayer
+ _OBJC_IVAR_$_TLAlertQueuePlayerController._previousAudioVolume
+ ___78-[TLToneManager _handleTonePreferencesChangedNotificationForPreferencesKinds:]_block_invoke.979
+ ___78-[TLToneManager _handleTonePreferencesChangedNotificationForPreferencesKinds:]_block_invoke.980
+ ___80-[TLAlertQueuePlayerController _startMusicPlaybackForStateDescriptor:mediaItem:]_block_invoke
+ ___83-[TLAlertQueuePlayerController _didPrepareToPlayMusicForStateDescriptor:withError:]_block_invoke
+ ___83-[TLAlertQueuePlayerController _didPrepareToPlayMusicForStateDescriptor:withError:]_block_invoke.150
+ ___85-[TLAlertQueuePlayerController _reloadPlaybackForStateDescriptor:withToneIdentifier:]_block_invoke.39
+ ___93-[TLAlertQueuePlayerController _notifyPlaybackObserverForStateDescriptor:isForMusicPlayback:]_block_invoke
+ ___93-[TLAlertQueuePlayerController _notifyPlaybackObserverForStateDescriptor:isForMusicPlayback:]_block_invoke.57
+ ___94-[TLAlertQueuePlayerController _prepareAudioEnvironmentForStateDescriptor:isForMusicPlayback:]_block_invoke
+ ___94-[TLAlertQueuePlayerController _prepareAudioEnvironmentForStateDescriptor:isForMusicPlayback:]_block_invoke_2
+ ___block_descriptor_48_e8_32s40s_e17_v16?0"NSError"8ls32l8s40l8
+ ___getMPMediaItemCollectionClass_block_invoke
+ ___getMPMediaItemCollectionClass_block_invoke.cold.1
+ ___getMPMusicPlayerApplicationControllerClass_block_invoke
+ ___getMPMusicPlayerApplicationControllerClass_block_invoke.cold.1
+ _getMPMediaItemCollectionClass.softClass
+ _getMPMusicPlayerApplicationControllerClass.softClass
+ _objc_msgSend$_applyAudioVolume:forAlert:isForMusicPlayback:phase:
+ _objc_msgSend$_didEndPlayingAlertForStateDescriptor:isForMusicPlayback:
+ _objc_msgSend$_didPrepareToPlayMusicForStateDescriptor:withError:
+ _objc_msgSend$_ensureMusicPlaybackStartedForStateDescriptor:
+ _objc_msgSend$_initWithAudioSessionReporterID:isForMusicPlayback:
+ _objc_msgSend$_notifyPlaybackObserverForStateDescriptor:isForMusicPlayback:
+ _objc_msgSend$_prepareAudioEnvironmentForStateDescriptor:isForMusicPlayback:
+ _objc_msgSend$_reportAudioStartEventForStateDescriptor:
+ _objc_msgSend$_restoreAudioEnvironmentForStateDescriptor:isForMusicPlayback:
+ _objc_msgSend$_startMusicPlaybackForStateDescriptor:mediaItem:
+ _objc_msgSend$_stopMusicPlayback
+ _objc_msgSend$_toneIdentifierForMediaLibraryItemIdentifier:
+ _objc_msgSend$_vibrationPatternDictionaryForStateDescriptor:allowsArtificiallyRepeatingPropertyListRepresentation:
+ _objc_msgSend$_willBeginPlayingAlertForStateDescriptor:isForMusicPlayback:
+ _objc_msgSend$artist
+ _objc_msgSend$collectionWithItems:
+ _objc_msgSend$currentPlaybackRate
+ _objc_msgSend$initWithClientIdentifier:queue:
+ _objc_msgSend$prepareToPlayWithCompletionHandler:
+ _objc_msgSend$setDisableAutomaticCanBeNowPlaying:
+ _objc_msgSend$setQueueWithItemCollection:
+ _objc_msgSend$setRepeatMode:
+ _objc_msgSend$sleepForTimeInterval:
- -[TLAlertPlaybackBeginEvent _initWithAudioSessionReporterID:]
- -[TLAlertQueuePlayerController _applyAudioVolume:forAlert:]
- -[TLAlertQueuePlayerController _didEndPlayingAlertForStateDescriptor:]
- -[TLAlertQueuePlayerController _prepareAudioEnvironmentForStateDescriptor:]
- -[TLAlertQueuePlayerController _reloadPlaybackForStateDescriptor:withToneIdentifier:].cold.5
- -[TLAlertQueuePlayerController _restoreAudioEnvironmentForStateDescriptor:]
- -[TLAlertQueuePlayerController _startPlaybackForStateDescriptor:usingConfirmedPlayableAsset:hasAlreadyDetectedUserAttention:].cold.4
- -[TLAlertQueuePlayerController _willBeginPlayingAlertForStateDescriptor:]
- GCC_except_table183
- GCC_except_table31
- GCC_except_table52
- ___125-[TLAlertQueuePlayerController _startPlaybackForStateDescriptor:usingConfirmedPlayableAsset:hasAlreadyDetectedUserAttention:]_block_invoke.61
- ___125-[TLAlertQueuePlayerController _startPlaybackForStateDescriptor:usingConfirmedPlayableAsset:hasAlreadyDetectedUserAttention:]_block_invoke_3
- ___75-[TLAlertQueuePlayerController _prepareAudioEnvironmentForStateDescriptor:]_block_invoke
- ___75-[TLAlertQueuePlayerController _prepareAudioEnvironmentForStateDescriptor:]_block_invoke_2
- ___78-[TLToneManager _handleTonePreferencesChangedNotificationForPreferencesKinds:]_block_invoke.976
- ___78-[TLToneManager _handleTonePreferencesChangedNotificationForPreferencesKinds:]_block_invoke.977
- ___85-[TLAlertQueuePlayerController _reloadPlaybackForStateDescriptor:withToneIdentifier:]_block_invoke.40
- ___getMPMediaItemPropertyFilePathSymbolLoc_block_invoke
- _getMPMediaItemPropertyFilePathSymbolLoc.ptr
- _objc_msgSend$_applyAudioVolume:forAlert:
- _objc_msgSend$_didEndPlayingAlertForStateDescriptor:
- _objc_msgSend$_initWithAudioSessionReporterID:
- _objc_msgSend$_prepareAudioEnvironmentForStateDescriptor:
- _objc_msgSend$_restoreAudioEnvironmentForStateDescriptor:
- _objc_msgSend$_willBeginPlayingAlertForStateDescriptor:
CStrings:
+ "%{public}@: -_applyAudioVolume:(%f) forAlert:(%{public}@) isForMusicPlayback:(%{BOOL}d) phase:(%{public}@): Policy for applying audio volume: %{public}@."
+ "%{public}@: -_applyAudioVolume…: Adjusted volume on %{public}@ for MediaExperience audio category %{public}@ from %f to %f for %{public}@; did succeed: %{BOOL}d."
+ "%{public}@: -_didEndPlayingAlertForStateDescriptor:(%{public}@) isForMusicPlayback:(%{BOOL}d)."
+ "%{public}@: -_didPrepareToPlayMusicForStateDescriptor:(%{public}@) withError:(%{public}@)."
+ "%{public}@: -_didPrepareToPlayMusicForStateDescriptor:(%{public}@)…: Succeeded!"
+ "%{public}@: -_didPrepareToPlayMusic…: Calling -play on %{public}@."
+ "%{public}@: -_didPrepareToPlayMusic…: Calling AudioServicesPlaySystemSoundWithOptions with a non-nil pattern for soundID: %lu."
+ "%{public}@: -_didPrepareToPlayMusic…: Playing alert for %{public}@ is no longer actually playing; aborting playback initiation."
+ "%{public}@: -_didPrepareToPlayMusic…: Running completion block for AudioServicesPlaySystemSoundWithOptions for soundID: %lu."
+ "%{public}@: -_didPrepareToPlayMusic…: Setting timer for %.1f seconds to check if music playback actually started."
+ "%{public}@: -_didPrepareToPlayMusic…: Should vibrate: %{BOOL}d."
+ "%{public}@: -_ensureMusicPlaybackStartedForStateDescriptor:(%{public}@)"
+ "%{public}@: -_ensureMusicPlaybackStarted…: Music appears to be playing just fine!"
+ "%{public}@: -_ensureMusicPlaybackStarted…: Music playback appears to have failed unexpectedly. Stopping music playback before starting over with fallback tone."
+ "%{public}@: -_ensureMusicPlaybackStarted…: Music playback rate: %.3f."
+ "%{public}@: -_notifyPlaybackObserverForStateDescriptor:(%{public}@) isForMusicPlayback:(%{BOOL}d)."
+ "%{public}@: -_notifyPlaybackObserver…: Calling -alert:didBeginPlayingWithEvent: on playback observer %{public}@ with %{public}@ for %{public}@."
+ "%{public}@: -_notifyPlaybackObserver…: Calling -alertDidBeginPlaying: on playback observer %{public}@ for %{public}@."
+ "%{public}@: -_prepareAudioEnvironment. Skipping setup of audio session as we prepare for music playback."
+ "%{public}@: -_prepareAudioEnvironmentForStateDescriptor:(%{public}@) isForMusicPlayback:(%{BOOL}d). alertForAudioEnvironmentSetup = %{public}@"
+ "%{public}@: -_reloadPlayback…: Found a media item for the specified external tone information: %{public}@ (“%{public}@” from “%{public}@”)."
+ "%{public}@: -_reportAudioStartEventForStateDescriptor:(%{public}@)."
+ "%{public}@: -_restoreAudioEnvironmentForStateDescriptor:(%{public}@) isForMusicPlayback:(%{BOOL}d)."
+ "%{public}@: -_restoreAudioEnvironment…: Restoring audio volume to %f after deactivation for %{public}@."
+ "%{public}@: -_restoreAudioEnvironment…: Restoring audio volume to %f before deactivation for %{public}@."
+ "%{public}@: -_startMusicPlaybackForStateDescriptor:(%{public}@) mediaItem:(%{public}@)."
+ "%{public}@: -_startMusicPlayback…: Created music player: %{public}@."
+ "%{public}@: -_startMusicPlayback…: Disabled automatic plumbing for becoming Now Playing app: %{public}@."
+ "%{public}@: -_startMusicPlayback…: Preparing to play music with %{public}@."
+ "%{public}@: -_startMusicPlayback…: Setting queue with collection %{public}@ [%{public}@] on %{public}@."
+ "%{public}@: -_startMusicPlayback…: Setting repeat mode to .all on %{public}@."
+ "%{public}@: -_stopMusicPlayback: Calling -stop on %{public}@."
+ "%{public}@: -_stopMusicPlayback: Calling AudioServicesStopSystemSound for soundID: %lu with inStopNow = %{bool}d."
+ "%{public}@: -_stopMusicPlayback: Ended delay of %.1fs to avoid a perceptible glitch upon restoring previous audio volume for Media Playback."
+ "%{public}@: -_stopMusicPlayback: Start delay of %.1fs to avoid a perceptible glitch upon restoring previous audio volume for Media Playback."
+ "%{public}@: -_vibrationPatternDictionaryForStateDescriptor:(%{public}@) allowsArtificiallyRepeatingPropertyListRepresentation:(%{BOOL}d)."
+ "%{public}@: -_vibrationPatternDictionary…: Failed to wrap external vibration pattern as an instance of TLVibrationPattern. Falling back to passing the external vibration pattern through."
+ "%{public}@: -_willBeginPlayingAlertForStateDescriptor:(%{public}@) isForMusicPlayback:(%{BOOL}d)."
+ "; isForMusicPlayback = YES"
+ "@\"MPMusicPlayerApplicationController\""
+ "@28@0:8q16B24"
+ "MPMediaItemCollection"
+ "MPMusicPlayerApplicationController"
+ "MediaPlayback"
+ "TB,R,N,GisForMusicPlayback,V_forMusicPlayback"
+ "_applyAudioVolume:forAlert:isForMusicPlayback:phase:"
+ "_didEndPlayingAlertForStateDescriptor:isForMusicPlayback:"
+ "_didPrepareToPlayMusicForStateDescriptor:withError:"
+ "_ensureMusicPlaybackStartedForStateDescriptor:"
+ "_forMusicPlayback"
+ "_hasPreviousAudioVolume"
+ "_initWithAudioSessionReporterID:isForMusicPlayback:"
+ "_isPlayingMusic"
+ "_musicPlaybackCheckTimerSource"
+ "_musicPlaybackVibrationSoundID"
+ "_musicPlayer"
+ "_notifyPlaybackObserverForStateDescriptor:isForMusicPlayback:"
+ "_prepareAudioEnvironmentForStateDescriptor:isForMusicPlayback:"
+ "_previousAudioVolume"
+ "_reportAudioStartEventForStateDescriptor:"
+ "_restoreAudioEnvironmentForStateDescriptor:isForMusicPlayback:"
+ "_startMusicPlaybackForStateDescriptor:mediaItem:"
+ "_stopMusicPlayback"
+ "_toneIdentifierForMediaLibraryItemIdentifier:"
+ "_vibrationPatternDictionaryForStateDescriptor:allowsArtificiallyRepeatingPropertyListRepresentation:"
+ "_willBeginPlayingAlertForStateDescriptor:isForMusicPlayback:"
+ "artist"
+ "collectionWithItems:"
+ "currentPlaybackRate"
+ "dynamic-update"
+ "forMusicPlayback"
+ "initWithClientIdentifier:queue:"
+ "isForMusicPlayback"
+ "prepareToPlayWithCompletionHandler:"
+ "preparing-audio-environment"
+ "restoring-audio-environment"
+ "setDisableAutomaticCanBeNowPlaying:"
+ "setQueueWithItemCollection:"
+ "setRepeatMode:"
+ "sleepForTimeInterval:"
+ "v40@0:8f16@20B28q32"
- "%{public}@: -_applyAudioVolume:(%f) forAlert:(%{public}@): Policy for applying audio volume: %{public}@."
- "%{public}@: -_applyAudioVolume…: Adjusted volume on %{public}@ for MediaExperience audio category %{public}@ to %f for %{public}@; did succeed: %{BOOL}d."
- "%{public}@: -_didEndPlayingAlertForStateDescriptor:(%{public}@)."
- "%{public}@: -_prepareAudioEnvironmentForStateDescriptor:(%{public}@). alertForAudioEnvironmentSetup = %{public}@"
- "%{public}@: -_reloadPlayback…: found external media library asset at path %{public}@ for identifier %llu."
- "%{public}@: -_restoreAudioEnvironmentForStateDescriptor:(%{public}@)."
- "%{public}@: -_restoreAudioEnvironment…: Reverted volume of %{public}@ to %f for %{public}@."
- "%{public}@: -_startPlayback… hasAlreadyDetected…: Calling -alert:didBeginPlayingWithEvent: on playback observer %{public}@ with %{public}@ for %{public}@."
- "%{public}@: -_startPlayback… hasAlreadyDetected…: Calling -alertDidBeginPlaying: on playback observer %{public}@ for %{public}@."
- "%{public}@: -_startPlayback… hasAlreadyDetected…: Failed to wrap external vibration pattern as an instance of TLVibrationPattern. Falling back to passing the external vibration pattern through."
- "%{public}@: -_willBeginPlayingAlertForStateDescriptor:(%{public}@)."
- "MPMediaItemPropertyFilePath"
- "_applyAudioVolume:forAlert:"
- "_didEndPlayingAlertForStateDescriptor:"
- "_initWithAudioSessionReporterID:"
- "_prepareAudioEnvironmentForStateDescriptor:"
- "_restoreAudioEnvironmentForStateDescriptor:"
- "_willBeginPlayingAlertForStateDescriptor:"
- "v28@0:8f16@20"

```
