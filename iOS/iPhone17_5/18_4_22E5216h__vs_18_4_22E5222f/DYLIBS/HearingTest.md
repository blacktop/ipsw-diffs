## HearingTest

> `/System/Library/PrivateFrameworks/HearingTest.framework/HearingTest`

```diff

-240.29.0.0.0
-  __TEXT.__text: 0xa2c94
-  __TEXT.__auth_stubs: 0x1760
+240.30.0.0.0
+  __TEXT.__text: 0xa7a78
+  __TEXT.__auth_stubs: 0x1730
   __TEXT.__objc_methlist: 0x44c
-  __TEXT.__const: 0x3a80
+  __TEXT.__const: 0x3f50
   __TEXT.__cstring: 0x237a
-  __TEXT.__constg_swiftt: 0x1acc
-  __TEXT.__swift5_typeref: 0x11d2
-  __TEXT.__swift5_proto: 0x1fc
-  __TEXT.__swift5_types: 0x140
-  __TEXT.__swift5_capture: 0x1f28
-  __TEXT.__swift5_reflstr: 0x2057
-  __TEXT.__swift5_fieldmd: 0x1c5c
-  __TEXT.__oslogstring: 0x5f21
+  __TEXT.__constg_swiftt: 0x1c58
+  __TEXT.__swift5_typeref: 0x129c
+  __TEXT.__swift5_builtin: 0x168
+  __TEXT.__swift5_reflstr: 0x2147
+  __TEXT.__swift5_fieldmd: 0x1d14
+  __TEXT.__swift5_assocty: 0x3a0
+  __TEXT.__swift5_proto: 0x22c
+  __TEXT.__swift5_types: 0x15c
+  __TEXT.__swift5_capture: 0x2190
+  __TEXT.__oslogstring: 0x5d71
   __TEXT.__swift_as_entry: 0x58
   __TEXT.__swift_as_ret: 0x50
-  __TEXT.__swift5_assocty: 0x2b0
   __TEXT.__swift5_protos: 0x20
-  __TEXT.__swift5_builtin: 0x104
   __TEXT.__swift5_mpenum: 0xd0
-  __TEXT.__unwind_info: 0x15c0
-  __TEXT.__eh_frame: 0x1e80
+  __TEXT.__unwind_info: 0x1768
+  __TEXT.__eh_frame: 0x1fd8
   __TEXT.__objc_classname: 0x63
   __TEXT.__objc_methname: 0xe6b
   __TEXT.__objc_methtype: 0x3f3
   __DATA_CONST.__got: 0x518
-  __DATA_CONST.__const: 0x188
+  __DATA_CONST.__const: 0x170
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x550
   __DATA_CONST.__objc_protorefs: 0x28
-  __AUTH_CONST.__auth_got: 0xbb0
-  __AUTH_CONST.__auth_ptr: 0x6a8
-  __AUTH_CONST.__const: 0x9188
-  __AUTH_CONST.__objc_const: 0x2e58
-  __AUTH.__objc_data: 0xe18
-  __AUTH.__data: 0x1688
-  __DATA.__data: 0x10d8
-  __DATA.__bss: 0x3d00
-  __DATA.__common: 0x31
+  __AUTH_CONST.__auth_got: 0xb98
+  __AUTH_CONST.__auth_ptr: 0x710
+  __AUTH_CONST.__const: 0x9888
+  __AUTH_CONST.__objc_const: 0x2d98
+  __AUTH.__objc_data: 0xf50
+  __AUTH.__data: 0x1590
+  __DATA.__data: 0x1238
+  __DATA.__bss: 0x4300
+  __DATA.__common: 0x39
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices
-  - /System/Library/PrivateFrameworks/Coherence.framework/Coherence
   - /System/Library/PrivateFrameworks/HID.framework/HID
   - /System/Library/PrivateFrameworks/HearingModeService.framework/HearingModeService
   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2887
-  Symbols:   548
-  CStrings:  923
+  Functions: 3085
+  Symbols:   585
+  CStrings:  908
 
Symbols:
+ _OBJC_CLASS_$_NSRecursiveLock
+ _swift_checkMetadataState
- _objc_release_x1
- _objc_retain_x1
CStrings:
+ "[%{public}s] No connected device after resetting discovery"
+ "_HearingTestMode"
+ "_canSwitchAirpods"
+ "_centralMgr"
+ "_centralMgrPoweredOn"
+ "_centralMgrQueue"
+ "_connectedCBDevice"
+ "_connectedDiscovery"
+ "_connectedDiscoveryCount"
+ "_deviceLost"
+ "_deviceLostHandler"
+ "_discoveryActivated"
+ "_enforceStrictQueues"
+ "_hearingTestActive"
+ "_isAudioSessionActivatedByTonePlayer"
+ "_isHTModeDisabledByTonePlayer"
+ "_isLeftUseOccludedCalibrationTable"
+ "_isNewObserverWaitingOnConnectedCBDevice"
+ "_isRightUseOccludedCalibrationTable"
+ "_lostPeripheral"
+ "_pendingInvalidDevice"
+ "_peripheral"
+ "_placementDisabled"
+ "_queue"
+ "_requirementStatusManager"
+ "com.apple.HearingTest.HTAccessoryAHPSManager.SafeVariablesQueue"
+ "com.apple.HearingTest.HTRequirementStatusManager.SafeVariablesQueue"
- "$__lazy_storage_$_accessoryManager"
- "?"
- "HearingTestMode"
- "No"
- "Unknown"
- "Yes"
- "[%{public}s] Accessory manager not found"
- "[%{public}s] Invalid accessory manager"
- "[%{public}s] No connected deivce after resetting discovery"
- "[%{public}s] Notifying 'discovery' again after resetting discovery"
- "[%{public}s] accessory manager not available for fetch occlusion"
- "[%{public}s] failed to reset noise counter"
- "[%{public}s] handleDeviceChanged no accessory manager!"
- "[%{public}s] handleDeviceLost no accessory manager!"
- "canSwitchAirpods"
- "centralMgr"
- "centralMgrPoweredOn"
- "centralMgrQueue"
- "clientCount"
- "clientID"
- "connectedCBDevice"
- "connectedDeviceLock"
- "connectedDiscovery"
- "connectedDiscoveryCount"
- "connectedIdentifier"
- "deviceLost"
- "deviceLostHandler"
- "enforceStrictQueues"
- "hearingTestActive"
- "isAudioSessionActivatedByTonePlayer"
- "isHTModeDisabledByTonePlayer"
- "isLeftUseOccludedCalibrationTable"
- "isNewObserverWaitingOnConnectedCBDevice"
- "isRightUseOccludedCalibrationTable"
- "lostPeripheral"
- "noiseInterruption"
- "noiseInterruptionLock"
- "noiseSimInProgressTimer"
- "pendingInvalidDevice"
- "peripheral"
- "placementDisabled"
- "requirementStatusManager"

```
