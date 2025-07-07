## ClockKitUI

> `/System/Library/PrivateFrameworks/ClockKitUI.framework/ClockKitUI`

```diff

-2483.297.0.0.0
-  __TEXT.__text: 0x341c0
+2483.306.0.0.0
+  __TEXT.__text: 0x34158
   __TEXT.__auth_stubs: 0x1240
   __TEXT.__objc_methlist: 0x420c
   __TEXT.__const: 0x7a76

   __TEXT.__unwind_info: 0x1070
   __TEXT.__eh_frame: 0xb8
   __TEXT.__objc_classname: 0x6c2
-  __TEXT.__objc_methname: 0xa454
+  __TEXT.__objc_methname: 0xa455
   __TEXT.__objc_methtype: 0x1a35
   __TEXT.__objc_stubs: 0x7960
   __DATA_CONST.__got: 0x4f8

   - /System/Library/PrivateFrameworks/BaseBoardUI.framework/BaseBoardUI
   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
+  - /System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry
   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 60F12046-1661-368A-98E2-EF5A6DC0FCA8
+  UUID: 833D3C3B-D462-317B-AC58-A9657FE22F67
   Functions: 1682
   Symbols:   5744
   CStrings:  2695
Symbols:
+ _PDRVersionIsGreaterThanOrEqual
+ _objc_msgSend$pdrDeviceVersion
- _NRVersionIsGreaterThanOrEqual
- _objc_msgSend$nrDeviceVersion
Functions:
~ -[CLKUIDigitalClockView layoutSubviews] : 344 -> 240
CStrings:
+ "pdrDeviceVersion"
- "nrDeviceVersion"

```
