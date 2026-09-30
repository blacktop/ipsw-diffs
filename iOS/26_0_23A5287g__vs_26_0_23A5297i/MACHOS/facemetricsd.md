## facemetricsd

> `/usr/libexec/facemetricsd`

```diff

-17.0.0.0.0
-  __TEXT.__text: 0x4eb0
-  __TEXT.__auth_stubs: 0x520
-  __TEXT.__objc_stubs: 0xd00
-  __TEXT.__objc_methlist: 0x440
-  __TEXT.__const: 0x58
-  __TEXT.__oslogstring: 0xc4b
-  __TEXT.__cstring: 0x199
-  __TEXT.__objc_classname: 0x97
-  __TEXT.__objc_methtype: 0x564
+18.0.0.0.0
+  __TEXT.__text: 0x5734
+  __TEXT.__auth_stubs: 0x5a0
+  __TEXT.__objc_stubs: 0xde0
+  __TEXT.__objc_methlist: 0x468
+  __TEXT.__cstring: 0x1bb
+  __TEXT.__const: 0x60
+  __TEXT.__objc_methname: 0x10da
+  __TEXT.__oslogstring: 0xdd6
+  __TEXT.__objc_classname: 0x98
+  __TEXT.__objc_methtype: 0x596
   __TEXT.__gcc_except_tab: 0x9c
-  __TEXT.__objc_methname: 0x1004
-  __TEXT.__unwind_info: 0x178
-  __DATA_CONST.__auth_got: 0x2a0
-  __DATA_CONST.__got: 0x218
-  __DATA_CONST.__const: 0x140
+  __TEXT.__unwind_info: 0x190
+  __DATA_CONST.__auth_got: 0x2e0
+  __DATA_CONST.__got: 0x208
+  __DATA_CONST.__const: 0x190
   __DATA_CONST.__cfstring: 0x120
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0xa28
-  __DATA.__objc_selrefs: 0x438
-  __DATA.__objc_ivar: 0x54
+  __DATA.__objc_const: 0xaa8
+  __DATA.__objc_selrefs: 0x468
+  __DATA.__objc_ivar: 0x64
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x180
-  __DATA.__bss: 0x20
+  __DATA.__bss: 0x1c
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/SensorKit.framework/SensorKit
   - /System/Library/PrivateFrameworks/AppleCVA.framework/AppleCVA
+  - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/HealthAlgorithms.framework/HealthAlgorithms

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D4E7630C-0B01-31B2-A65D-99AA2B6678F7
-  Functions: 133
-  Symbols:   159
-  CStrings:  342
+  UUID: 52F7EE7C-FD75-3EF1-8799-59B4886CB025
+  Functions: 143
+  Symbols:   165
+  CStrings:  361
 
Symbols:
+ _BiomeLibrary
+ __Block_object_dispose
+ _dispatch_assert_queue$V2
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _dispatch_queue_attr_make_with_qos_class
+ _dispatch_queue_create
+ _dispatch_sync
+ _objc_retain_x3
- _OBJC_CLASS_$_BMStreams
- __dispatch_main_q
CStrings:
+ "@\"NSObject<OS_dispatch_queue>\""
+ "App"
+ "DSLPublisher"
+ "InFocus"
+ "QQ!"
+ "T@\"NSMutableDictionary\",&,N,V_cachedBundleIdEligibility"
+ "_cachedBundleIdEligibility"
+ "_cmTimeForMetrics:"
+ "_deviceUnlockTimerExpiration"
+ "_foregroundTimerStartTime"
+ "_handleBiomeEvent:"
+ "_handleDeviceLockAtTimestamp:"
+ "_handleDeviceUnlockAtTimestamp:"
+ "_handleEligibilityStatus:bundleId:event:"
+ "_handleLockStatusNotificationAtTimestamp:"
+ "_handleMessageAppBackgroundedWithTimestamp:"
+ "_handleMessageAppForegroundedWithTimestamp:"
+ "_handleMessageAppStatusNotification:"
+ "_isPacketWithinRangeForTimestamp:withSessionStartTime:andSessionStopTime:"
+ "_machContinuousTimeForMetrics:"
+ "_packetFromMetrics:"
+ "_queue"
+ "_registerForLockStatusNotifications"
+ "_registerForMessagesAppForegroundedNotifications"
+ "_reportSkBundleIdEligibilityCheckLatencyWithStartTimestamp:andStopTimestamp:"
+ "_requestToStopCameraSession"
+ "_retrieveCmTimeForAbsoluteTimestamp:"
+ "_setupCameraSession"
+ "_stopCameraSession"
+ "_unlockTimerStartTime"
+ "activating app foregrounded timer"
+ "activating unlock timer"
+ "app foreground timer took (%f s) to fire"
+ "app foreground timer took (%f s) which is longer than %f seconds to fire"
+ "cachedBundleIdEligibility"
+ "com.apple.facemetricsd.controller"
+ "d"
+ "ignore request to stop camera session due to a timer being active"
+ "initWithQueue:"
+ "lock_session_id = %llu, seconds from device unlocked to packet = %f, message_session_id = %llu, seconds from message app session start to packet = %f, session_id = %llu"
+ "on unlock, camera session is not nil and active reason is unlocked (a double unlock occurred)"
+ "seconds from start of camera session to packet: %f"
+ "setCachedBundleIdEligibility:"
+ "starting"
+ "timeIntervalSinceReferenceDate"
+ "unlock timer took (%f s) to fire"
+ "unlock timer took (%f s) which is longer than %f seconds to fire"
+ "v40@0:8q16@24@32"
+ "\xd1"
- "Qa"
- "T@\"NSMutableDictionary\",&,N,V_cachedBundleIdElgibility"
- "_cachedBundleIdElgibility"
- "appLaunch"
- "cachedBundleIdElgibility"
- "camera session expected to be nil on device unlock"
- "cmTimeForMetrics:"
- "handleDeviceLockAtTimestamp:"
- "handleDeviceUnlockAtTimestamp:"
- "handleLockStatusNotificationAtTimestamp:"
- "handleMessageAppBackgroundedWithTimestamp:"
- "handleMessageAppForegroundedWithTimestamp:"
- "handleMessageAppStatusNotification:"
- "ignore reqeust to stop camera session due to a timer being active"
- "isPacketWithinRangeForTimestamp:withSessionStartTime:andSessionStopTime:"
- "isStarting"
- "lock_session_id = %llu, secondsFromStart = %f, message_session_id = %llu, secondsFromStart = %f, session_id = %llu"
- "machContinuousTimeForMetrics:"
- "packetFromMetrics:"
- "publisher"
- "registerForLockStatusNotifications"
- "registerForMessagesAppForegroundedNotifications"
- "reportSkBundleIdEligibilityCheckLatencyWithStartTimestamp:andStopTimestamp:"
- "requestToStopCameraSession"
- "retrieveCmTimeForAbsoluteTimestamp:"
- "seconds from start: %f"
- "setCachedBundleIdElgibility:"
- "setupCameraSession"
- "stopCameraSession"
- "\xb1"

```
