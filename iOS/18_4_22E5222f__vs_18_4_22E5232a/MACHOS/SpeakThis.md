## SpeakThis

> `/System/Library/AccessibilityBundles/SpeakThis.axuiservice/SpeakThis`

```diff

-3148.15.10.0.0
-  __TEXT.__text: 0x15154
-  __TEXT.__auth_stubs: 0x6d0
-  __TEXT.__objc_stubs: 0x4860
-  __TEXT.__objc_methlist: 0x1754
-  __TEXT.__objc_methname: 0x5486
-  __TEXT.__cstring: 0x769
-  __TEXT.__objc_classname: 0x220
-  __TEXT.__objc_methtype: 0xc6c
-  __TEXT.__const: 0x158
-  __TEXT.__gcc_except_tab: 0x1d4
-  __TEXT.__oslogstring: 0xee9
-  __TEXT.__unwind_info: 0x570
-  __DATA_CONST.__auth_got: 0x378
-  __DATA_CONST.__got: 0x308
-  __DATA_CONST.__const: 0x5f0
-  __DATA_CONST.__cfstring: 0x760
-  __DATA_CONST.__objc_classlist: 0x40
+3148.15.11.2.0
+  __TEXT.__text: 0x16920
+  __TEXT.__auth_stubs: 0x750
+  __TEXT.__objc_stubs: 0x4c20
+  __TEXT.__objc_methlist: 0x19dc
+  __TEXT.__const: 0x148
+  __TEXT.__objc_methname: 0x5983
+  __TEXT.__cstring: 0x7ea
+  __TEXT.__objc_classname: 0x28f
+  __TEXT.__objc_methtype: 0xcd5
+  __TEXT.__gcc_except_tab: 0x1fc
+  __TEXT.__oslogstring: 0xf7d
+  __TEXT.__unwind_info: 0x5f8
+  __DATA_CONST.__auth_got: 0x3b8
+  __DATA_CONST.__got: 0x318
+  __DATA_CONST.__const: 0x750
+  __DATA_CONST.__cfstring: 0x780
+  __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x60
+  __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x40
+  __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_intobj: 0x120
   __DATA_CONST.__objc_arraydata: 0x48
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x1b68
-  __DATA.__objc_selrefs: 0x15a8
-  __DATA.__objc_ivar: 0x198
-  __DATA.__objc_data: 0x280
-  __DATA.__data: 0x488
-  __DATA.__bss: 0x38
+  __DATA.__objc_const: 0x1f48
+  __DATA.__objc_selrefs: 0x16b8
+  __DATA.__objc_ivar: 0x1d0
+  __DATA.__objc_data: 0x320
+  __DATA.__data: 0x548
+  __DATA.__bss: 0x50
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
+  - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/AssertionServices.framework/AssertionServices
   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
+  - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SpeakThisServices.framework/SpeakThisServices
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 489
-  Symbols:   243
-  CStrings:  1190
+  Functions: 554
+  Symbols:   257
+  CStrings:  1260
 
Symbols:
+ _CFNotificationCenterRemoveObserver
+ _MKBGetDeviceLockState
+ _OBJC_CLASS_$_AXDeviceEventMonitor
+ _OBJC_CLASS_$_AXDeviceScreenLockMonitor
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSHashTable
+ _OBJC_METACLASS_$_AXDeviceEventMonitor
+ _OBJC_METACLASS_$_AXDeviceScreenLockMonitor
+ _SBSRequestPasscodeUnlockUI
+ _dispatch_assert_queue$V2
+ _dispatch_sync
+ _mach_absolute_time
+ _mach_timebase_info
+ _objc_opt_respondsToSelector
CStrings:
+ "\x01\x11B\"\x15\x11"
+ "\x02"
+ "\a\x11\x17\"\x1e"
+ "@\"AXDeviceScreenLockMonitor\""
+ "@\"NSHashTable\""
+ "AXDeviceEventMonitor"
+ "AXDeviceEventMonitor queue"
+ "AXDeviceEventMonitorObserver"
+ "AXDeviceScreenLockMonitor"
+ "AXDeviceScreenLockMonitorObserver"
+ "Error starting screen detector: %@"
+ "Serial EventMonitor queue"
+ "Started monitoring device lock/unlock state"
+ "Stopped monitoring device lock/unlock state"
+ "Stopping screen detector"
+ "T@\"NSHashTable\",&,N,V_observers"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
+ "TB,N,GisDeviceLocked,V_deviceLocked"
+ "TB,N,V_deviceLocked"
+ "TB,N,V_screenDetectorRunning"
+ "Td,N,V_lastDeviceLockedTimestamp"
+ "Td,N,V_lastDevicePausedTimestamp"
+ "Td,N,V_lastDeviceUnlockedTimestamp"
+ "_deviceLocked"
+ "_instructUnlockToResume"
+ "_isScreenLocked"
+ "_isScreenTimedOut"
+ "_isSessionProtected"
+ "_lastDeviceLockedTimestamp"
+ "_lastDevicePausedTimestamp"
+ "_lastDeviceUnlockedTimestamp"
+ "_notifyObserver:isDeviceLocked:timestamp:"
+ "_queryIsDeviceLocked"
+ "_queue"
+ "_screenDetectorRunning"
+ "_startMonitoringWithQueue:"
+ "_startScreenLockDetector"
+ "_stopMonitoring"
+ "_stopScreenLockDetector"
+ "_subscribeEventMonitor"
+ "_unsubscribeEventMonitors"
+ "com.apple.mobile.keybagd.lock_status"
+ "deviceEventMonitorDidReceiveEvent:"
+ "deviceLockMonitor:didReceiveDeviceLockStateChanged:timestamp:"
+ "deviceLockStateChanged:"
+ "deviceLocked"
+ "enumerateObservers:"
+ "enumerateObserversInQueue:"
+ "isDeviceLocked"
+ "lastDeviceLockedTimestamp"
+ "lastDevicePausedTimestamp"
+ "lastDeviceUnlockedTimestamp"
+ "monitor"
+ "notifyObserver:"
+ "queue"
+ "sbs_unlockDeviceIfNeededAndPerform:"
+ "screenDetectorRunning"
+ "screenTimeOutCheck"
+ "setDeviceLocked:"
+ "setLastDeviceLockedTimestamp:"
+ "setLastDevicePausedTimestamp:"
+ "setLastDeviceUnlockedTimestamp:"
+ "setQueue:"
+ "setScreenDetectorRunning:"
+ "startWithCompletion:"
+ "stop"
+ "timeIntervalSinceReferenceDate"
+ "v12@?0C8"
+ "v16@?0@8"
+ "v20@?0B8@\"NSError\"12"
+ "v36@0:8@\"AXDeviceScreenLockMonitor\"16B24d28"
+ "v36@0:8@16B24d28"
+ "weakObjectsHashTable"
- "\x01\x11R\x15\x11"
- "\a\x11\x16\"\x1e"
- "\xa1"

```
