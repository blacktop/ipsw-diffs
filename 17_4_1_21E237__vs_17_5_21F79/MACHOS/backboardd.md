## backboardd

> `/usr/libexec/backboardd`

```diff

-599.124.0.0.0
-  __TEXT.__text: 0x99e7c
-  __TEXT.__auth_stubs: 0x1c00
-  __TEXT.__objc_stubs: 0xe980
-  __TEXT.__objc_methlist: 0x667c
-  __TEXT.__const: 0x3e8
-  __TEXT.__gcc_except_tab: 0x3e84
-  __TEXT.__objc_methname: 0x14b0c
-  __TEXT.__cstring: 0x747b
-  __TEXT.__objc_classname: 0x1a87
-  __TEXT.__objc_methtype: 0x408a
-  __TEXT.__oslogstring: 0x96e4
+599.328.0.0.0
+  __TEXT.__text: 0x9b810
+  __TEXT.__auth_stubs: 0x1c20
+  __TEXT.__objc_stubs: 0xece0
+  __TEXT.__objc_methlist: 0x67f4
+  __TEXT.__const: 0x3f8
+  __TEXT.__gcc_except_tab: 0x3ec4
+  __TEXT.__objc_methname: 0x15028
+  __TEXT.__cstring: 0x75ec
+  __TEXT.__objc_classname: 0x1ac6
+  __TEXT.__objc_methtype: 0x413f
+  __TEXT.__oslogstring: 0x997e
   __TEXT.__ustring: 0x2a
   __TEXT.__dlopen_cstrs: 0x62
-  __TEXT.__unwind_info: 0x286c
+  __TEXT.__unwind_info: 0x28cc
   __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__auth_got: 0xe18
+  __DATA_CONST.__auth_got: 0xe28
   __DATA_CONST.__got: 0x388
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x4bc8
-  __DATA_CONST.__cfstring: 0x8020
-  __DATA_CONST.__objc_classlist: 0x578
+  __DATA_CONST.__const: 0x4c10
+  __DATA_CONST.__cfstring: 0x81a0
+  __DATA_CONST.__objc_classlist: 0x588
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x200
+  __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x68
-  __DATA_CONST.__objc_classrefs: 0xa50
-  __DATA_CONST.__objc_superrefs: 0x3f0
+  __DATA_CONST.__objc_classrefs: 0xa70
+  __DATA_CONST.__objc_superrefs: 0x3f8
   __DATA_CONST.__linkguard: 0x18
   __DATA_CONST.__objc_intobj: 0x348
   __DATA_CONST.__objc_doubleobj: 0x40
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x130d0
-  __DATA.__objc_selrefs: 0x4488
-  __DATA.__objc_ivar: 0xe68
-  __DATA.__objc_data: 0x36b0
-  __DATA.__data: 0x18b0
-  __DATA.__bss: 0x3c8
+  __DATA.__objc_const: 0x13518
+  __DATA.__objc_selrefs: 0x4580
+  __DATA.__objc_ivar: 0xea4
+  __DATA.__objc_data: 0x3750
+  __DATA.__data: 0x1910
+  __DATA.__bss: 0x3e8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary
+  - /System/Library/PrivateFrameworks/AppleHIDFeedback.framework/AppleHIDFeedback
   - /System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation
   - /System/Library/PrivateFrameworks/BackBoardHIDEventProcessors.framework/BackBoardHIDEventProcessors
   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsp.dylib
-  Functions: 3046
-  Symbols:   743
-  CStrings:  6142
+  Functions: 3080
+  Symbols:   747
+  CStrings:  6228
 
Symbols:
+ _IOHIDEventGetVendorDefinedData
+ _NSStringFromBKSHIDForceStageTransition
+ _OBJC_CLASS_$_AHFManager
+ _OBJC_CLASS_$_BKSHIDHapticFeedbackRequest
CStrings:
+ "\x01\x13"
+ "\x12\x18A\x11#!\x1f\x04\x12"
+ " -> force stage:%u transition:%{public}@ progress:%f nextThreshold:%f pressedThreshold:%f releasedThreshold:%f"
+ "#\xf0A\xf0Q\xf1\xb1\xb1!B"
+ "%s: Error unarchiving feedback request"
+ "@\"<BKHIDHapticFeedbackInterface>\""
+ "@\"BKTouchDeliveryGenericGestureFocusObserver\""
+ "ActuationStrength"
+ "B20@0:8i16"
+ "B28@0:8@16i24"
+ "BKHIDEventSmartCoverMatcherQueue"
+ "BKHIDHapticFeedbackController"
+ "BKHIDHapticFeedbackInterface"
+ "BKMousePointerController.displayLinkPauseTimer"
+ "Events paused"
+ "Events unpaused"
+ "Force stage event size mismatch want:%lu got:%ld"
+ "Haptic feedback request %{public}@ failed with error %{public}@"
+ "Haptic feedback request %{public}@ from pid %d could not be validated due to destination mismatch"
+ "Haptic feedback request %{public}@ from pid %d could not be validated due to missing entitlement"
+ "Haptic feedback request %{public}@ successful"
+ "HapticFeedback"
+ "MKWakeAnimation"
+ "SqueezeIsSystemShortcut"
+ "T@\"BKIOHIDServiceMatcher\",&,N,V_magicKeyboardExtendedMatcher"
+ "T@\"NSMutableSet\",&,N,V_magicKeyboardExtendedServices"
+ "TB,N,GisPaused"
+ "TB,R,N,V_forceDidChange"
+ "TI,R,N,V_stage"
+ "Td,R,N,V_force"
+ "_BKHIDXXRequestHapticFeedback"
+ "_HIDHapticFeedbackInterface"
+ "_displayLinkPauseTime"
+ "_displayLinkPauseTimer"
+ "_displayLinkPaused"
+ "_displayLinkUnpauseTime"
+ "_eventsPaused"
+ "_force"
+ "_forceDidChange"
+ "_forceEvent"
+ "_genericGestureFocusObserver"
+ "_magicKeyboardExtendedMatcher"
+ "_magicKeyboardExtendedServices"
+ "_restartDisplayLinkPauseTimer"
+ "_routeSqueezeEventToSystem"
+ "_stage"
+ "_validateHapticFeedbackRequest:forAuditToken:"
+ "_validatePencilHapticFeedbackRequest:forPID:"
+ "_validateTrackpadHapticFeedbackRequest:forPID:"
+ "_wakeAnimationStyle"
+ "addForceEvent:fromSender:"
+ "bs_secureObjectFromData:ofClass:"
+ "clickHapticStrength"
+ "com.apple.backboard.requestHapticFeedback"
+ "destinationPIDMatchesHapticFeedbackRequestPID:"
+ "deviceType"
+ "displayLink unpaused after %.2fs of pausing, took %.2fms to fire after unpause"
+ "extended"
+ "force"
+ "force: %.4g stage %u"
+ "forceDidChange"
+ "initWithHIDHapticFeedbackInterface:"
+ "isPaused"
+ "isSqueezeForSystemShortcutEnabled"
+ "magicKeyboardExtendedMatcher"
+ "magicKeyboardExtendedServices"
+ "mouse.force"
+ "observeMouseForceDidChange:stage:"
+ "pattern"
+ "pause"
+ "paused"
+ "playFeedback:powerSourceID:timestamp:error:"
+ "playFeedback:senderID:timestamp:error:"
+ "playHapticFeedbackRequest:"
+ "postHapticFeedbackRequest:forAuditToken:"
+ "powerSourceID"
+ "reevaluateDisplayLink: %{public}@ %{public}@"
+ "reevaluateDisplayLink: wants:%{BOOL}u devices:%{BOOL}u eventsDisabled:%{BOOL}u eventsPaused:%{BOOL}u allowed:%{BOOL}u has:%{BOOL}u paused:%{BOOL}u -- %{public}@"
+ "setMagicKeyboardExtendedMatcher:"
+ "setMagicKeyboardExtendedServices:"
+ "setPaused:"
+ "setSupportsLightClick:"
+ "setSupportsSystemHaptics:"
+ "stage"
+ "unpause"
+ "v24@0:8@\"BKSHIDHapticFeedbackRequest\"16"
+ "v28@0:8d16I24"
+ "v32@0:8@16^{?=[8I]}24"
+ "v32@?0@\"NSString\"8@\"BKSHIDEventDeferringResolution\"16^B24"
- "\x12\x18A\x13!\x1f\x04\x12"
- "#\xf0A\xf0Q\xf1\xb1\xb1\x11\""
- "reevaluateDisplayLink: wants:%{BOOL}u devices:%{BOOL}u eventsDisabled:%{BOOL}u allowed:%{BOOL}u has:%{BOOL}u -- %{public}@"

```
