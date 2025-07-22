## IOKit

> `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`

```diff

-100222.0.0.0.0
-  __TEXT.__text: 0xa4f08
+100222.0.1.0.0
+  __TEXT.__text: 0xa4fc4
   __TEXT.__auth_stubs: 0x2120
   __TEXT.__objc_methlist: 0x150
   __TEXT.__const: 0x104cc

   - /usr/lib/libenergytrace.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 6CC02118-7017-37FD-80E7-44AC87B5F752
+  UUID: 65E313E6-01A0-381C-80D2-7F15E71723F7
   Functions: 3460
   Symbols:   6653
   CStrings:  3489
Functions:
~ __IOHIDEventSystemPropertyChanged : 208 -> 296
~ _IOHIDEventSystemRegisterPropertyChangedNotification : 88 -> 132
~ _IOHIDEventSystemUnregisterPropertyChangedNotification : 64 -> 96
~ _IOHIDManagerUnscheduleFromRunLoop.cold.1 : 104 -> 128
CStrings:
+ "OSKEXT_BUILD_DATE 20:04:56 Jul 11 2025"
- "OSKEXT_BUILD_DATE 17:53:04 Jun 24 2025"

```
