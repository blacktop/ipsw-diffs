## AXSoundDetectionUI

> `/System/Library/PrivateFrameworks/AXSoundDetectionUI.framework/AXSoundDetectionUI`

```diff

-488.0.0.0.0
-  __TEXT.__text: 0x5378c
-  __TEXT.__auth_stubs: 0x11f0
-  __TEXT.__objc_methlist: 0x273c
+490.2.0.0.0
+  __TEXT.__text: 0x54530
+  __TEXT.__auth_stubs: 0x1200
+  __TEXT.__objc_methlist: 0x274c
   __TEXT.__const: 0x980
-  __TEXT.__gcc_except_tab: 0x404
-  __TEXT.__oslogstring: 0x5a34
-  __TEXT.__cstring: 0x1c37
+  __TEXT.__gcc_except_tab: 0x408
+  __TEXT.__oslogstring: 0x5ff4
+  __TEXT.__cstring: 0x1c17
   __TEXT.__dlopen_cstrs: 0x1a8
   __TEXT.__swift5_typeref: 0x75a
   __TEXT.__swift5_capture: 0x2d8
-  __TEXT.__constg_swiftt: 0x81c
-  __TEXT.__swift5_reflstr: 0x301
-  __TEXT.__swift5_fieldmd: 0x33c
+  __TEXT.__constg_swiftt: 0x824
+  __TEXT.__swift5_reflstr: 0x2e1
+  __TEXT.__swift5_fieldmd: 0x330
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x44
   __TEXT.__swift5_types: 0x38
   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x2c
-  __TEXT.__unwind_info: 0x12a8
+  __TEXT.__unwind_info: 0x12b8
   __TEXT.__eh_frame: 0x908
   __TEXT.__objc_classname: 0x482
-  __TEXT.__objc_methname: 0x52ae
+  __TEXT.__objc_methname: 0x52dd
   __TEXT.__objc_methtype: 0xe36
-  __TEXT.__objc_stubs: 0x48e0
-  __DATA_CONST.__got: 0x678
+  __TEXT.__objc_stubs: 0x4900
+  __DATA_CONST.__got: 0x688
   __DATA_CONST.__const: 0x880
   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1710
+  __DATA_CONST.__objc_selrefs: 0x1720
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0xb8
-  __AUTH_CONST.__auth_got: 0x908
+  __AUTH_CONST.__auth_got: 0x910
   __AUTH_CONST.__const: 0x10a8
   __AUTH_CONST.__cfstring: 0x1120
-  __AUTH_CONST.__objc_const: 0x3938
+  __AUTH_CONST.__objc_const: 0x3918
   __AUTH_CONST.__objc_intobj: 0xf0
-  __AUTH.__objc_data: 0x15b8
+  __AUTH.__objc_data: 0x15b0
   __AUTH.__data: 0x300
   __DATA.__objc_ivar: 0x1c8
-  __DATA.__data: 0xaa0
+  __DATA.__data: 0xac0
   __DATA.__bss: 0x930
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__bss: 0x50

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 222C2627-95EC-3835-BFFE-3D35371ED717
-  Functions: 1741
-  Symbols:   3742
-  CStrings:  1914
+  UUID: 4F4FD48E-8078-3C3F-B6BF-614A46E0DF7D
+  Functions: 1748
+  Symbols:   3757
+  CStrings:  1931
 
Symbols:
+ -[AXSDListenEngine _carPlayIsConnectedDidChange:].cold.1
+ -[AXSDListenEngine _deactivateNotifications]
+ -[AXSDListenEngine _handleAudioSessionInterruption:].cold.1
+ -[AXSDListenEngine _handleConfigurationChangeNotification:].cold.1
+ -[AXSDListenEngine _mediaServicesWereReset:].cold.1
+ -[AXSDListenEngine _restartSoundRecognitionIfNecesary].cold.1
+ -[AXSDSettings(AXSoundDetectionUIAdditions) disableKShotDetector:]
+ _block_copy_helper.84
+ _block_descriptor.86
+ _block_destroy_helper.85
+ _objc_msgSend$_deactivateNotifications
- _block_copy_helper.85
- _block_descriptor.87
- _block_destroy_helper.86
CStrings:
+ "AXSDKShotMonitor: %ld seconds has elapsed. Checking status of detectors."
+ "AXSDKShotMonitor: Attempting to retrain detector. Detector: %@"
+ "AXSDKShotMonitor: Checking custom detectors for potential retraining."
+ "AXSDKShotMonitor: Checking enabled custom detectors - verifying that enabled identifiers still have a corresponding detector."
+ "AXSDKShotMonitor: Detector is already marked as failed. Not attempting retraining. Detector: %@"
+ "AXSDKShotMonitor: Disabling detector with identifier: %s - model no longer exists."
+ "AXSDKShotMonitor: Enabled Identifier: %s has a valid detector: %s"
+ "AXSDKShotMonitor: Ignoring custom detector because we do not need to attempt to retrain it. Detector: %@."
+ "AXSDKShotMonitor: Ignoring detector because its not custom. Detector: %@."
+ "AXSDKShotMonitor: It's too early to attempt retrain of detector. Waiting: %f. Current time difference is: %f. Not attempting retraining. Detector: %@"
+ "AXSDKShotMonitor: No KShot Model currently being trained. Checking detectors."
+ "AXSDKShotMonitor: No date set for last attempted training date. Setting to: %s for Detector: %@"
+ "AXSDKShotMonitor: Will check status of detectors every %ld seconds."
+ "Medina Device with Medina Support enabled. AVAudioSession is handled by SoundAnalysis. We shouldn't be restarting SR."
+ "Medina Device with Medina Support enabled. Ignoring CarPlay connection change."
+ "Medina Device with Medina Support enabled. Ignoring audio config change."
+ "Medina Device with Medina Support enabled. Ignoring audio session interruption."
+ "Medina Device with Medina Support enabled. Ignoring media reset notification."
+ "Medina Support is Enabled on a Medina Device. No need to setup notifications."
+ "_deactivateNotifications"
+ "disableKShotDetector:"
- "Attempting to retrain detector. Detector: %@"
- "Detector is already marked as failed. Not attempting retraining. Detector: %@"
- "It's too early to attempt retrain of detector. Waiting: %f. Current time difference is: %f. Not attempting retraining. Detector: %@"
- "isActivelyTraining"

```
