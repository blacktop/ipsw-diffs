## ControlCenter

> `/System/Library/PrivateFrameworks/ControlCenter.framework/Versions/A/ControlCenter`

```diff

-  __TEXT.__text: 0x8d300
-  __TEXT.__objc_methlist: 0x3fc
-  __TEXT.__const: 0x5fb0
+  __TEXT.__text: 0x8eb48
+  __TEXT.__objc_methlist: 0x704
+  __TEXT.__const: 0x5fd8
   __TEXT.__constg_swiftt: 0x21cc
-  __TEXT.__swift5_typeref: 0x1958
-  __TEXT.__swift5_fieldmd: 0x1c6c
+  __TEXT.__swift5_typeref: 0x192a
+  __TEXT.__swift5_fieldmd: 0x1c78
   __TEXT.__swift5_builtin: 0x140
-  __TEXT.__swift5_reflstr: 0x1af1
+  __TEXT.__swift5_reflstr: 0x1b11
   __TEXT.__swift5_assocty: 0x5a0
   __TEXT.__swift5_proto: 0x3e8
   __TEXT.__swift5_types: 0x200
-  __TEXT.__cstring: 0x1d85
+  __TEXT.__cstring: 0x1e57
   __TEXT.__swift5_protos: 0x24
-  __TEXT.__swift5_capture: 0x22a4
-  __TEXT.__oslogstring: 0x1bc2
+  __TEXT.__swift5_capture: 0x1fb8
+  __TEXT.__oslogstring: 0x2100
   __TEXT.__swift5_types2: 0x4
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__gcc_except_tab: 0x3c
-  __TEXT.__unwind_info: 0x2648
-  __TEXT.__eh_frame: 0x1c28
+  __TEXT.__unwind_info: 0x26c0
+  __TEXT.__eh_frame: 0x1bb0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x498
-  __DATA_CONST.__objc_classlist: 0x170
+  __DATA_CONST.__const: 0x4a0
+  __DATA_CONST.__objc_classlist: 0x180
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6c0
+  __DATA_CONST.__objc_selrefs: 0x900
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x18
-  __DATA_CONST.__got: 0x6a8
-  __AUTH_CONST.__const: 0x8b48
-  __AUTH_CONST.__cfstring: 0x320
-  __AUTH_CONST.__objc_const: 0x29c8
-  __AUTH_CONST.__auth_got: 0x1300
-  __AUTH.__objc_data: 0x518
-  __AUTH.__data: 0x2100
-  __DATA.__objc_ivar: 0x20
-  __DATA.__data: 0x14c8
-  __DATA.__bss: 0x6900
-  __DATA.__common: 0x390
+  __DATA_CONST.__objc_superrefs: 0x28
+  __DATA_CONST.__got: 0x6c8
+  __AUTH_CONST.__const: 0x84c8
+  __AUTH_CONST.__cfstring: 0x460
+  __AUTH_CONST.__objc_const: 0x2e58
+  __AUTH_CONST.__auth_got: 0x1390
+  __AUTH.__objc_data: 0x5b8
+  __AUTH.__data: 0x2120
+  __DATA.__objc_ivar: 0x88
+  __DATA.__data: 0x14e8
+  __DATA.__bss: 0x6908
+  __DATA.__common: 0x398
   __DATA_DIRTY.__objc_data: 0x2b8
   __DATA_DIRTY.__data: 0x1f88
   __DATA_DIRTY.__bss: 0x1080

   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices
+  - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox
   - /System/Library/Frameworks/Combine.framework/Versions/A/Combine
   - /System/Library/Frameworks/CoreAudio.framework/Versions/A/CoreAudio
   - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5138
-  Symbols:   2972
-  CStrings:  406
+  Functions: 5135
+  Symbols:   3110
+  CStrings:  451
 
Sections:
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift5_types2 : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ +[AppleSoundSettings sharedSoundSettings]
+ -[AppleSoundSettings activateSettingsForCurrentUser]
+ -[AppleSoundSettings alertSoundVolume]
+ -[AppleSoundSettings audioMonitor]
+ -[AppleSoundSettings balance]
+ -[AppleSoundSettings beepFeedbackChanged:]
+ -[AppleSoundSettings beepVolume]
+ -[AppleSoundSettings canSetVolume]
+ -[AppleSoundSettings dealloc]
+ -[AppleSoundSettings deviceChanged:]
+ -[AppleSoundSettings hasBalance]
+ -[AppleSoundSettings hasMute]
+ -[AppleSoundSettings hasOutputDevice]
+ -[AppleSoundSettings hasVolume]
+ -[AppleSoundSettings init]
+ -[AppleSoundSettings isMuted]
+ -[AppleSoundSettings mainVolume]
+ -[AppleSoundSettings playUIEffects]
+ -[AppleSoundSettings playVolumeKeyFeedback]
+ -[AppleSoundSettings postFeedbackChanged:]
+ -[AppleSoundSettings resyncStateAfterSleep:]
+ -[AppleSoundSettings setAlertSoundVolume:]
+ -[AppleSoundSettings setBalance:]
+ -[AppleSoundSettings setBeepVolume:]
+ -[AppleSoundSettings setMainVolume:]
+ -[AppleSoundSettings setMute:]
+ -[AppleSoundSettings setPlayUIEffects:]
+ -[AppleSoundSettings setPlayVolumeKeyFeedback:]
+ -[SSAudioMonitor balance]
+ -[SSAudioMonitor canSetLevel]
+ -[SSAudioMonitor canSetProperty:forChannel:]
+ -[SSAudioMonitor copyProperty:forChannel:dataSize:dataPtr:]
+ -[SSAudioMonitor dealloc]
+ -[SSAudioMonitor defaultOutputDevice]
+ -[SSAudioMonitor dirtyChangeMask:]
+ -[SSAudioMonitor getProperty:forChannel:dataSize:dataPtr:]
+ -[SSAudioMonitor getStringProperty:forChannel:]
+ -[SSAudioMonitor hasBalance]
+ -[SSAudioMonitor hasLevel]
+ -[SSAudioMonitor hasMute]
+ -[SSAudioMonitor hasProperty:forChannel:dataSize:writable:]
+ -[SSAudioMonitor inHogMode]
+ -[SSAudioMonitor init]
+ -[SSAudioMonitor isMuted]
+ -[SSAudioMonitor level]
+ -[SSAudioMonitor monitorDevice:]
+ -[SSAudioMonitor notifyServiceChange]
+ -[SSAudioMonitor outputDevice]
+ -[SSAudioMonitor readVolumeLimit]
+ -[SSAudioMonitor setBalance:]
+ -[SSAudioMonitor setLevel:]
+ -[SSAudioMonitor setMute:]
+ -[SSAudioMonitor setProperty:forChannel:dataSize:dataPtr:]
+ -[SSAudioMonitor stopAllMonitoring]
+ -[SSAudioMonitor syncBalance]
+ -[SSAudioMonitor syncDeviceChannels]
+ -[SSAudioMonitor syncDeviceProperties]
+ -[SSAudioMonitor syncHardware]
+ -[SSAudioMonitor syncLevel]
+ -[SSAudioMonitor syncMute]
+ -[SSAudioMonitor updateAlertDeviceMute]
+ -[SSAudioMonitor updateMute]
+ OBJC_IVAR_$_AppleSoundSettings._monitor
+ OBJC_IVAR_$_AppleSoundSettings._playVolumeKeyFeedback
+ OBJC_IVAR_$_AppleSoundSettings._syncNeeded
+ OBJC_IVAR_$_SSAudioMonitor._balance
+ OBJC_IVAR_$_SSAudioMonitor._canSetLevel
+ OBJC_IVAR_$_SSAudioMonitor._changeLock
+ OBJC_IVAR_$_SSAudioMonitor._changeMask
+ OBJC_IVAR_$_SSAudioMonitor._clampValue
+ OBJC_IVAR_$_SSAudioMonitor._deviceIsClamped
+ OBJC_IVAR_$_SSAudioMonitor._hardwareListener
+ OBJC_IVAR_$_SSAudioMonitor._hasBalance
+ OBJC_IVAR_$_SSAudioMonitor._hasLeftMute
+ OBJC_IVAR_$_SSAudioMonitor._hasLevel
+ OBJC_IVAR_$_SSAudioMonitor._hasMasterMute
+ OBJC_IVAR_$_SSAudioMonitor._hasRightMute
+ OBJC_IVAR_$_SSAudioMonitor._hwBalance
+ OBJC_IVAR_$_SSAudioMonitor._hwLevel
+ OBJC_IVAR_$_SSAudioMonitor._isMuted
+ OBJC_IVAR_$_SSAudioMonitor._leftChannel
+ OBJC_IVAR_$_SSAudioMonitor._level
+ OBJC_IVAR_$_SSAudioMonitor._outputDevice
+ OBJC_IVAR_$_SSAudioMonitor._propertyListener
+ OBJC_IVAR_$_SSAudioMonitor._queue
+ OBJC_IVAR_$_SSAudioMonitor._rightChannel
+ OBJC_IVAR_$_SSAudioMonitor._updateLock
+ OBJC_IVAR_$_SSAudioMonitor._updateQueue
+ _AudioObjectAddPropertyListenerBlock
+ _AudioObjectRemovePropertyListenerBlock
+ _AudioServicesGetProperty
+ _AudioServicesSetProperty
+ _CFNumberCreate
+ _CFNumberGetTypeID
+ _CFPreferencesCopyValue
+ _NSLog
+ _NSWorkspaceDidWakeNotification
+ _NSWorkspaceSessionDidBecomeActiveNotification
+ _OBJC_CLASS_$_AppleSoundSettings
+ _OBJC_CLASS_$_NSLock
+ _OBJC_CLASS_$_NSNotification
+ _OBJC_CLASS_$_SSAudioMonitor
+ _OBJC_METACLASS_$_AppleSoundSettings
+ _OBJC_METACLASS_$_SSAudioMonitor
+ _SSDeviceCanSetProperty
+ _SSDeviceCopyProperty
+ _SSDeviceCopyStringProperty
+ _SSDeviceGetProperty
+ _SSDeviceHasProperty
+ _SSDeviceSetProperty
+ _SSPrefsGetBooleanWithDefault
+ _SSPrefsSetBoolean
+ __22-[SSAudioMonitor init]_block_invoke
+ __Block_object_assign
+ __Block_object_dispose
+ __OBJC_$_CLASS_METHODS_AppleSoundSettings
+ __OBJC_$_INSTANCE_METHODS_AppleSoundSettings
+ __OBJC_$_INSTANCE_METHODS_SSAudioMonitor
+ __OBJC_$_INSTANCE_VARIABLES_AppleSoundSettings
+ __OBJC_$_INSTANCE_VARIABLES_SSAudioMonitor
+ __OBJC_CLASS_RO_$_AppleSoundSettings
+ __OBJC_CLASS_RO_$_SSAudioMonitor
+ __OBJC_METACLASS_RO_$_AppleSoundSettings
+ __OBJC_METACLASS_RO_$_SSAudioMonitor
+ ___22-[SSAudioMonitor init]_block_invoke
+ ___34-[SSAudioMonitor dirtyChangeMask:]_block_invoke
+ ___44-[AppleSoundSettings resyncStateAfterSleep:]_block_invoke
+ ___block_descriptor_40_e8_32o_e44_v20?0I8r^{AudioObjectPropertyAddress=III}12l
+ ___block_descriptor_40_e8_32o_e5_v8?0l
+ ___copy_helper_block_e8_32o
+ ___destroy_helper_block_e8_32o
+ __gSSAudioMonitorMaxLevel
+ __os_log_default
+ __swift_closure_destructor.108Tm
+ __swift_closure_destructor.127Tm
+ _dispatch_after
+ _dispatch_async
+ _dispatch_get_global_queue
+ _dispatch_queue_create
+ _dispatch_release
+ _dispatch_time
+ _exp
+ _gSharedSoundSettings
+ _kSSAlertVolumeChangedNotification
+ _kSSBalanceKey
+ _kSSDeviceUpdateNotification
+ _kSSLevelKey
+ _kSSMuteKey
+ _kSSPrefsBeepFeedbackKey
+ _kSSPrefsChangedNotification
+ _log
+ _objc_alloc
+ _objc_autorelease
+ _objc_msgSend$addObserver:selector:name:object:
+ _objc_msgSend$addObserver:selector:name:object:suspensionBehavior:
+ _objc_msgSend$alertSoundVolume
+ _objc_msgSend$audioMonitor
+ _objc_msgSend$balance
+ _objc_msgSend$boolValue
+ _objc_msgSend$canSetLevel
+ _objc_msgSend$canSetProperty:forChannel:
+ _objc_msgSend$canSetVolume
+ _objc_msgSend$cancelPreviousPerformRequestsWithTarget:
+ _objc_msgSend$cancelPreviousPerformRequestsWithTarget:selector:object:
+ _objc_msgSend$defaultOutputDevice
+ _objc_msgSend$dictionaryWithObject:forKey:
+ _objc_msgSend$dirtyChangeMask:
+ _objc_msgSend$getProperty:forChannel:dataSize:dataPtr:
+ _objc_msgSend$hasBalance
+ _objc_msgSend$hasLevel
+ _objc_msgSend$hasMute
+ _objc_msgSend$inHogMode
+ _objc_msgSend$initWithCapacity:
+ _objc_msgSend$isMuted
+ _objc_msgSend$level
+ _objc_msgSend$lock
+ _objc_msgSend$mainVolume
+ _objc_msgSend$monitorDevice:
+ _objc_msgSend$notificationCenter
+ _objc_msgSend$notificationWithName:object:userInfo:
+ _objc_msgSend$notifyServiceChange
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$numberWithFloat:
+ _objc_msgSend$outputDevice
+ _objc_msgSend$performSelector:withObject:afterDelay:
+ _objc_msgSend$playVolumeKeyFeedback
+ _objc_msgSend$postNotification:
+ _objc_msgSend$postNotificationName:object:userInfo:
+ _objc_msgSend$postNotificationName:object:userInfo:options:
+ _objc_msgSend$readVolumeLimit
+ _objc_msgSend$removeObserver:
+ _objc_msgSend$setAlertSoundVolume:
+ _objc_msgSend$setBalance:
+ _objc_msgSend$setLevel:
+ _objc_msgSend$setMainVolume:
+ _objc_msgSend$setMute:
+ _objc_msgSend$setProperty:forChannel:dataSize:dataPtr:
+ _objc_msgSend$sharedSoundSettings
+ _objc_msgSend$stopAllMonitoring
+ _objc_msgSend$syncBalance
+ _objc_msgSend$syncDeviceChannels
+ _objc_msgSend$syncDeviceProperties
+ _objc_msgSend$syncHardware
+ _objc_msgSend$syncLevel
+ _objc_msgSend$syncMute
+ _objc_msgSend$tryLock
+ _objc_msgSend$unlock
+ _objc_msgSend$updateAlertDeviceMute
+ _objc_msgSend$updateMute
+ _objc_msgSend$userInfo
- _OUTLINED_FUNCTION_100
- _OUTLINED_FUNCTION_101
- _OUTLINED_FUNCTION_102
- _OUTLINED_FUNCTION_103
- _OUTLINED_FUNCTION_104
- _OUTLINED_FUNCTION_105
- _OUTLINED_FUNCTION_106
- _OUTLINED_FUNCTION_107
- _OUTLINED_FUNCTION_108
- _OUTLINED_FUNCTION_109
- _OUTLINED_FUNCTION_110
- _OUTLINED_FUNCTION_111
- _OUTLINED_FUNCTION_98
- _OUTLINED_FUNCTION_99
- __swift_closure_destructor.109Tm
- __swift_closure_destructor.128Tm
- _swift_runtimeSupportsNoncopyableTypes
- _swift_willThrowTypedImpl
- _symbolic ______pSgXwz_Xx 13ControlCenter17HUDActionDelegateP
- get_type_metadata 15Synchronization5MutexVy13ControlCenter22KeyboardBrightnessImplC5StateVG noncopyable
- get_type_metadata 15Synchronization5MutexVySDySS10Foundation8IndexSetVGSgG noncopyable
- get_type_metadata 15Synchronization5MutexVySDySS7Combine10PublishersO5ShareCy_AD18PassthroughSubjectCyyts5NeverOGGGG noncopyable
- get_type_metadata 15Synchronization5MutexVySbG noncopyable
- get_type_metadata 15Synchronization6AtomicVySiG noncopyable
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bsOEiJ/Sources/ControlCenter_frameworks/Framework/CoreAudioController.swift"
+ "<SoundSettings> (DeviceID %d) setLevel: Setting balance to %f"
+ "<SoundSettings> (DeviceID %d) setLevel: Setting main volume to %f"
+ "<SoundSettings> (DeviceID %d) setMute called"
+ "<SoundSettings> (DeviceID %d) syncBalance called"
+ "<SoundSettings> (DeviceID %d) syncMute called"
+ "<SoundSettings> (DeviceID %d) updateMute called"
+ "<SoundSettings> setBalance: Balance set"
+ "<SoundSettings> setBalance: _hwBalance is %f"
+ "<SoundSettings> setLevel: Balance set"
+ "<SoundSettings> setLevel: Setting balance to %f"
+ "<SoundSettings> setLevel: _hwBalance is %f"
+ "<SoundSettings> setMute: _hasMasterMute = %d, _hasLeftMute = %d, _hasRightMute = %d"
+ "<SoundSettings> setMute: left mute set"
+ "<SoundSettings> setMute: master mute set"
+ "<SoundSettings> setMute: muteValue = %d"
+ "<SoundSettings> setMute: right mute set"
+ "<SoundSettings> syncBalance: _balance = %f, _hwBalance = %f"
+ "<SoundSettings> syncBalance: _hasBalance = %d, balance = %f"
+ "<SoundSettings> syncMute: _hasLeftMute = %d, _hasRightMute = %d, leftValue = %d, rightValue = %d"
+ "<SoundSettings> syncMute: _hasMasterMute = %d, masterValue = %d"
+ "<SoundSettings> updateMute: _hasMasterMute = %d, _hasLeftMute = %d, _hasRightMute = %d"
+ "<SoundSettings> updateMute: left mute set"
+ "<SoundSettings> updateMute: master mute set"
+ "<SoundSettings> updateMute: right mute set"
+ "<SoundSettings> updateMute: value = %d"
+ "ClockPreferences did change"
+ "Error %i setting system sound volume"
+ "Failed to set system volume to %f"
+ "OutBalance"
+ "OutLevel"
+ "OutMute"
+ "VolumeLimit"
+ "__viewDidDisappear"
+ "__viewWillAppear"
+ "com.apple.sound.alertVolumeChanged"
+ "com.apple.soundsettings.deviceUpdate"
+ "init(logger:qos:presentationQueue:)"
+ "init(logger:queue:presentationQueue:)"
+ "set system volume: %f -> %f"
+ "v20@?0I8r^{AudioObjectPropertyAddress=III}12"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GTPf3b/Sources/ControlCenter_frameworks/Framework/CoreAudioController.swift"
- "Failed to set system volume to "
- "Trying to change system volume when the device cannot change volume, returning %f"
- "init(logger:qos:)"
- "init(logger:queue:)"
- "set system volume for %x: %f -> %f: %f"

```
