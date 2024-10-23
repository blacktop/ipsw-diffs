## VoiceTriggerUI

> `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/VoiceTriggerUI`

```diff

-3401.18.2.11.4
-  __TEXT.__text: 0x61748
-  __TEXT.__auth_stubs: 0x1760
-  __TEXT.__objc_methlist: 0x3a64
-  __TEXT.__const: 0x1c74
-  __TEXT.__gcc_except_tab: 0x96c
-  __TEXT.__cstring: 0x5cce
-  __TEXT.__oslogstring: 0x1fd5
-  __TEXT.__swift5_typeref: 0x27f8
+3402.3.1.0.0
+  __TEXT.__text: 0x61d14
+  __TEXT.__auth_stubs: 0x1750
+  __TEXT.__objc_methlist: 0x3a7c
+  __TEXT.__const: 0x1c84
+  __TEXT.__gcc_except_tab: 0x9a8
+  __TEXT.__cstring: 0x5e2e
+  __TEXT.__oslogstring: 0x2035
+  __TEXT.__swift5_typeref: 0x27e4
   __TEXT.__swift5_capture: 0x2e4
-  __TEXT.__swift5_fieldmd: 0x638
+  __TEXT.__swift5_fieldmd: 0x62c
   __TEXT.__constg_swiftt: 0xa2c
-  __TEXT.__swift5_reflstr: 0x78b
+  __TEXT.__swift5_reflstr: 0x77b
   __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_assocty: 0x1c0
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_proto: 0x74
   __TEXT.__swift5_types: 0x78
-  __TEXT.__unwind_info: 0x1640
+  __TEXT.__unwind_info: 0x1658
   __TEXT.__eh_frame: 0x4b8
-  __TEXT.__objc_classname: 0x903
-  __TEXT.__objc_methname: 0xd1f3
-  __TEXT.__objc_methtype: 0x2c5a
-  __TEXT.__objc_stubs: 0x85a0
-  __DATA_CONST.__got: 0x968
-  __DATA_CONST.__const: 0xa70
+  __TEXT.__objc_classname: 0x930
+  __TEXT.__objc_methname: 0xd254
+  __TEXT.__objc_methtype: 0x2c7d
+  __TEXT.__objc_stubs: 0x85c0
+  __DATA_CONST.__got: 0x970
+  __DATA_CONST.__const: 0xa98
   __DATA_CONST.__objc_classlist: 0x1d8
-  __DATA_CONST.__objc_protolist: 0xf8
+  __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2b28
+  __DATA_CONST.__objc_selrefs: 0x2b38
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x130
   __DATA_CONST.__objc_arraydata: 0x358
-  __AUTH_CONST.__auth_got: 0xbc0
-  __AUTH_CONST.__auth_ptr: 0x718
+  __AUTH_CONST.__auth_got: 0xbb8
+  __AUTH_CONST.__auth_ptr: 0x6d0
   __AUTH_CONST.__const: 0x10c8
-  __AUTH_CONST.__cfstring: 0x2a80
-  __AUTH_CONST.__objc_const: 0x9148
+  __AUTH_CONST.__cfstring: 0x2ae0
+  __AUTH_CONST.__objc_const: 0x9190
   __AUTH_CONST.__objc_arrayobj: 0x138
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x3a8
   __AUTH.__objc_data: 0x14d8
   __AUTH.__data: 0x8e0
   __DATA.__objc_ivar: 0x5e4
-  __DATA.__data: 0x13e0
+  __DATA.__data: 0x1438
   __DATA.__bss: 0xf50
   __DATA.__common: 0x40
   __DATA_DIRTY.__objc_data: 0x320
-  - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AVKit.framework/AVKit
   - /System/Library/Frameworks/Combine.framework/Combine

   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/AssistantUI.framework/AssistantUI
   - /System/Library/PrivateFrameworks/BaseBoardUI.framework/BaseBoardUI
+  - /System/Library/PrivateFrameworks/CameraUI.framework/CameraUI
   - /System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/CloudSubscriptionFeatures
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreSpeech.framework/CoreSpeech

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2188
-  Symbols:   1929
-  CStrings:  3272
+  Functions: 2195
+  Symbols:   1936
+  CStrings:  3288
 
Symbols:
+ _AFDeviceSupportsSAE
+ _OBJC_CLASS_$_CAMCameraButtonBuddyViewController
+ _OBJC_CLASS_$_NSThread
+ _dispatch_get_global_queue
- _AFDeviceSupportsSAEByDeviceCapabilityAndFeatureFlags
- _AFLocaleSupportsSAE
- _OBJC_CLASS_$_AVAudioPlayer
CStrings:
+ "\x01\x14$\x16\x1b\x11\x11!J"
+ "%!s(MISSING) Continue to Camera Button Buddy"
+ "%!s(MISSING) Continue to Siri Buddy"
+ "%!s(MISSING) GM to Summarization"
+ "%!s(MISSING) GM to next buddy"
+ "%!s(MISSING) Preloading Camera Button Buddy"
+ "%!s(MISSING) Summarization to next buddy"
+ "%!s(MISSING) To Camera Button Buddy"
+ "-[VTUIEnrollTrainingViewController _continueToCameraButtonBuddy]"
+ "-[VTUIEnrollTrainingViewController _continueToNextFromGM]"
+ "-[VTUIEnrollTrainingViewController _continueToNextFromSummarization]"
+ "-[VTUIEnrollTrainingViewController _continueToSummarizationFromGM]"
+ "-[VTUIEnrollTrainingViewController _prepareCameraButtonBuddy]"
+ "-[VTUIEnrollTrainingViewController _showCameraButtonBuddyControlOrSiriIntro]"
+ "-[VTUIEnrollTrainingViewController _showSiriIntroView]"
+ "-[VTUIEnrollTrainingViewController _showSiriIntroView]_block_invoke_2"
+ "@\"CAMCameraButtonBuddyViewController\""
+ "CAMCameraButtonBuddyViewControllerDelegate"
+ "H:|[cameraBuddyView]|"
+ "R"
+ "V:|[cameraBuddyView]|"
+ "_cameraButtonBuddyViewController"
+ "_continueToCameraButtonBuddy"
+ "_continueToNextFromGM"
+ "_continueToNextFromSummarization"
+ "_isCameraControlPagePreLoaded"
+ "_prepareCameraButtonBuddy"
+ "_showCameraButtonBuddyControlOrSiriIntro"
+ "_showSiriIntroView"
+ "cameraBuddyView"
+ "cameraButtonBuddyViewControllerDidFinish:"
+ "createViewControllerWithIntroViewControllerDelegate:"
+ "loadAssetsWithCompletion:"
+ "sleepForTimeInterval:"
+ "v24@0:8@\"CAMCameraButtonBuddyViewController\"16"
- "\x01\x14$\x17\x1a\x11\x11!J"
- "%!@(MISSING)/Siri+ Buddy V1 F 240321_ML.caf"
- "%!s(MISSING) deviceSupportsSAEByDeviceCapabilityAndFeatureFlags = %!d(MISSING), localeSupportsSAE = %!d(MISSING), deviceSupportsSAE = %!d(MISSING)"
- "-[VTUIEnrollTrainingViewController _showIntroView]"
- "-[VTUIEnrollTrainingViewController _showIntroView]_block_invoke_2"
- "-[VTUIEnrollmentSetupIntroViewControllerOrb _isDeviceEligibleForSAE]"
- "@60@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@48C56"
- "C"
- "_backgroundOnly"
- "_continueToIntroFromGM"
- "_continueToIntroFromSummarization"
- "_gmBackgroundViewController"
- "_isDeviceEligibleForSAE"
- "createViewControllerWithIntroViewControllerDelegate:backgroundOnly:"
- "initWithContentsOfURL:error:"
- "initWithFrame:delegate:backgroundOnly:"
- "play"
- "resourcePath"

```
