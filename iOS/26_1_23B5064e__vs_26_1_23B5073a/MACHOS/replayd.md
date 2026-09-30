## replayd

> `/usr/libexec/replayd`

```diff

-680.5.1.0.0
-  __TEXT.__text: 0x64f5c
+680.7.1.1.1
+  __TEXT.__text: 0x65f24
   __TEXT.__auth_stubs: 0x1120
-  __TEXT.__objc_stubs: 0x8ce0
-  __TEXT.__objc_methlist: 0x4644
+  __TEXT.__objc_stubs: 0x8f00
+  __TEXT.__objc_methlist: 0x4734
   __TEXT.__const: 0x1b4
-  __TEXT.__oslogstring: 0x9ef9
-  __TEXT.__cstring: 0xd054
-  __TEXT.__objc_methname: 0xd0b8
-  __TEXT.__objc_classname: 0x6d3
-  __TEXT.__objc_methtype: 0x23c3
-  __TEXT.__gcc_except_tab: 0x848
-  __TEXT.__unwind_info: 0x1350
+  __TEXT.__oslogstring: 0xa1cd
+  __TEXT.__cstring: 0xd342
+  __TEXT.__objc_methname: 0xd393
+  __TEXT.__objc_classname: 0x6d5
+  __TEXT.__objc_methtype: 0x23db
+  __TEXT.__gcc_except_tab: 0x894
+  __TEXT.__unwind_info: 0x1380
   __DATA_CONST.__auth_got: 0x8a0
-  __DATA_CONST.__got: 0x7d8
+  __DATA_CONST.__got: 0x7e0
   __DATA_CONST.__const: 0x1978
-  __DATA_CONST.__cfstring: 0x3c80
+  __DATA_CONST.__cfstring: 0x3cc0
   __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xe8

   __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_intobj: 0x360
   __DATA_CONST.__objc_doubleobj: 0x40
-  __DATA.__objc_const: 0x9ab0
-  __DATA.__objc_selrefs: 0x2cc8
-  __DATA.__objc_ivar: 0x5c4
+  __DATA.__objc_const: 0x9bb0
+  __DATA.__objc_selrefs: 0x2d70
+  __DATA.__objc_ivar: 0x5dc
   __DATA.__objc_data: 0xeb0
   __DATA.__data: 0xaf8
   __DATA.__bss: 0x1d0

   - /System/Library/Frameworks/MediaToolbox.framework/MediaToolbox
   - /System/Library/Frameworks/Photos.framework/Photos
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
+  - /System/Library/Frameworks/ReplayKit.framework/ReplayKit
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/Frameworks/UIKit.framework/UIKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EC491D20-B680-34DE-98EA-6BD69F50B561
-  Functions: 2023
-  Symbols:   540
-  CStrings:  4705
+  UUID: A84EAE52-F83E-30E9-A05E-828192E79151
+  Functions: 2048
+  Symbols:   541
+  CStrings:  4758
 
Symbols:
+ _OBJC_CLASS_$_RPBackgroundActivity
CStrings:
+ " [ERROR] %{public}s:%d Failed to decode broadcastConfig from data"
+ " [ERROR] %{public}s:%d Unarchiver error: %@"
+ " [INFO] %{public}s:%d Background activity activated successfully"
+ " [INFO] %{public}s:%d Background activity tapped by user"
+ " [INFO] %{public}s:%d Clearing background activity UI"
+ " [INFO] %{public}s:%d Pausing recording timer"
+ " [INFO] %{public}s:%d RPHighQualityLocalRecordingSession overriding clearSystemRecordingUI to clear background activity"
+ " [INFO] %{public}s:%d Resuming recording timer, total paused time: %.1f seconds"
+ " [INFO] %{public}s:%d Setting up purple background activity for HQLR recording"
+ " [INFO] %{public}s:%d Starting recording timer for Dynamic Island"
+ " [INFO] %{public}s:%d Stopping recording timer"
+ "-[RPHighQualityLocalRecordingSession clearBackgroundActivityUI]"
+ "-[RPHighQualityLocalRecordingSession clearSystemRecordingUI]"
+ "-[RPHighQualityLocalRecordingSession pauseRecordingTimer]"
+ "-[RPHighQualityLocalRecordingSession resumeRecordingTimer]"
+ "-[RPHighQualityLocalRecordingSession setupBackgroundActivityUI]"
+ "-[RPHighQualityLocalRecordingSession setupBackgroundActivityUI]_block_invoke"
+ "-[RPHighQualityLocalRecordingSession startRecordingTimer]"
+ "-[RPHighQualityLocalRecordingSession stopRecordingTimer]"
+ "-[RPSystemBroadcastSession setupSystemBroadcastWithHostBundleID:broadcastExtensionBundleID:broadcastConfigurationData:userInfo:handler:]_block_invoke"
+ "@\"RPBackgroundActivity\""
+ "T@\"NSTimer\",&,N,V_elapsedTimeTimer"
+ "T@\"RPBackgroundActivity\",&,N,V_backgroundActivity"
+ "T@\"RPStatusBarAssertion\",&,N,V_statusBarAssertion"
+ "Td,N,V_recordingStartTime"
+ "_backgroundActivity"
+ "_elapsedTimeTimer"
+ "_recordingStartTime"
+ "activateWithUserInteractionHandler:"
+ "backgroundActivity"
+ "clearBackgroundActivityUI"
+ "com.apple.systemstatus.background-activity.replaykit.callrecording.recording"
+ "deactivate"
+ "elapsedTimeTimer"
+ "initWithBackgroundActivityIdentifier:"
+ "pauseRecordingTimer"
+ "recordingStartTime"
+ "resumeRecordingTimer"
+ "setBackgroundActivity:"
+ "setClass:forClassName:"
+ "setElapsedTimeTimer:"
+ "setRecordingStartTime:"
+ "setStatusBarAssertion:"
+ "setupBackgroundActivityUI"
+ "shouldSetupBackgroundActivityUIForSystemBannerEnabled:"
+ "startRecordingTimer"
+ "statusBarAssertion"
+ "stopRecordingTimer"
+ "timeIntervalSinceReferenceDate"
+ "updateRecordingTimer:"

```
