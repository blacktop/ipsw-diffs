## MultitouchSupport

> `/System/Library/PrivateFrameworks/MultitouchSupport.framework/MultitouchSupport`

```diff

-9150.2.0.0.0
-  __TEXT.__text: 0x1e3f8
+9160.1.0.0.0
+  __TEXT.__text: 0x1e4e0
   __TEXT.__auth_stubs: 0xe50
   __TEXT.__objc_methlist: 0x2ec
   __TEXT.__const: 0x1ff8
   __TEXT.__cstring: 0x169e
-  __TEXT.__oslogstring: 0x1136
+  __TEXT.__oslogstring: 0x11b0
   __TEXT.__tpad_act_plist: 0xe22d
   __TEXT.__unwind_info: 0x6e0
   __TEXT.__objc_classname: 0x49

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 340C64FE-2C92-3052-92EC-03EE6890188C
-  Functions: 668
-  Symbols:   1430
-  CStrings:  619
+  UUID: 70C6C603-06C6-31DE-9D25-A8B62530E3CC
+  Functions: 669
+  Symbols:   1432
+  CStrings:  621
 
Symbols:
+ _mtalg_MaxContacts
Functions:
~ _mt_ForwardBinaryContacts : 612 -> 624
~ _mt_UncompressTouchpadCodecV1Force : 624 -> 796
+ _mtalg_MaxContacts
~ _MTParse_CompactV10BinaryPath : 456 -> 468
~ _MTParse_HostPathAndImage : 404 -> 416
CStrings:
+ "Force sensor position(%d) calculation hit a critical error"
+ "Raw force sensor position(%d) calculation hit a critical error"

```
