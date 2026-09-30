## AccessibilitySharedSupport

> `/System/Library/PrivateFrameworks/AccessibilitySharedSupport.framework/AccessibilitySharedSupport`

```diff

-545.14.0.0.0
-  __TEXT.__text: 0xc1dac
+545.15.0.0.0
+  __TEXT.__text: 0xc1c64
   __TEXT.__auth_stubs: 0x2430
   __TEXT.__objc_methlist: 0x4484
   __TEXT.__const: 0xc3ec
-  __TEXT.__cstring: 0x5203
-  __TEXT.__oslogstring: 0x337d
+  __TEXT.__cstring: 0x51f3
+  __TEXT.__oslogstring: 0x335d
   __TEXT.__gcc_except_tab: 0x1024
   __TEXT.__ustring: 0x182
   __TEXT.__dlopen_cstrs: 0x1a7

   __TEXT.__objc_classname: 0xc58
   __TEXT.__objc_methname: 0xc3e1
   __TEXT.__objc_methtype: 0x2097
-  __TEXT.__objc_stubs: 0x8ae0
+  __TEXT.__objc_stubs: 0x8aa0
   __DATA_CONST.__got: 0x940
   __DATA_CONST.__const: 0x1770
   __DATA_CONST.__objc_classlist: 0x260

   __DATA_CONST.__objc_arraydata: 0x440
   __AUTH_CONST.__auth_got: 0x1228
   __AUTH_CONST.__const: 0x6f90
-  __AUTH_CONST.__cfstring: 0x4b20
+  __AUTH_CONST.__cfstring: 0x4b00
   __AUTH_CONST.__objc_const: 0x76e8
   __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH_CONST.__objc_intobj: 0x978

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F2B8CFE7-1EA2-3B6F-95C8-4E994E529BFA
-  Functions: 5682
+  UUID: D5580991-D423-359F-91F7-948822800BE3
+  Functions: 5681
   Symbols:   7918
-  CStrings:  4221
+  CStrings:  4218
 
Symbols:
+ ___block_literal_global.38
- -[AXSSMotionTrackingHIDManager _deviceNotification:added:].cold.4
- ___block_literal_global.41
- _objc_msgSend$_axss_iAPInterfaceExistsForHIDDeviceService:
- _objc_msgSend$service
Functions:
~ +[AXSSMotionTrackingVirtualEyeTracker _eyeTrackerHIDDeviceProperties] : 264 -> 244
~ +[AXSSMotionTrackingUtilities axss_HIDDeviceIsMFiAuthenticated:] : 172 -> 8
~ -[AXSSMotionTrackingHIDManager _deviceNotification:added:] : 676 -> 608
~ -[AXSSMotionTrackingHIDManager startMonitoring].cold.1 : 80 -> 84
~ -[AXSSMotionTrackingHIDManager stopMonitoring].cold.1 : 80 -> 84
~ -[AXSSMotionTrackingHIDManager _deviceNotification:added:].cold.1 : 148 -> 152
~ -[AXSSMotionTrackingHIDManager _deviceNotification:added:].cold.2 : 80 -> 84
~ -[AXSSMotionTrackingHIDManager _deviceNotification:added:].cold.3 : 80 -> 132
- -[AXSSMotionTrackingHIDManager _deviceNotification:added:].cold.4
CStrings:
- "%s: device is not MFi authenticated!: %@"
- "Authenticated"

```
