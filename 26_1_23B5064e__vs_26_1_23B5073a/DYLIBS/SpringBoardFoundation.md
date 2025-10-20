## SpringBoardFoundation

> `/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`

```diff

-4557.1.18.101.0
-  __TEXT.__text: 0xb6cc0
-  __TEXT.__auth_stubs: 0x1a00
+4557.1.19.106.0
+  __TEXT.__text: 0xb6d54
+  __TEXT.__auth_stubs: 0x1a10
   __TEXT.__objc_methlist: 0x815c
   __TEXT.__const: 0x2350
   __TEXT.__cstring: 0xe12c
   __TEXT.__gcc_except_tab: 0x7bc
   __TEXT.__dlopen_cstrs: 0x4d2
-  __TEXT.__oslogstring: 0x302b
+  __TEXT.__oslogstring: 0x307a
   __TEXT.__ustring: 0x2ea
   __TEXT.__unwind_info: 0x22a0
   __TEXT.__objc_classname: 0x1a1d

   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x348
   __DATA_CONST.__objc_arraydata: 0x508
-  __AUTH_CONST.__auth_got: 0xd10
+  __AUTH_CONST.__auth_got: 0xd18
   __AUTH_CONST.__const: 0xd20
   __AUTH_CONST.__cfstring: 0xb8a0
   __AUTH_CONST.__objc_const: 0x1a0e8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C501D07B-A68A-3A00-BFFD-6A484D0B2843
-  Functions: 3734
-  Symbols:   12856
-  CStrings:  8669
+  UUID: CF996415-08F6-3FC8-8F7F-984BC7A49F1E
+  Functions: 3735
+  Symbols:   12859
+  CStrings:  8671
 
Symbols:
+ -[SBFMachNextMinuteDateProvider _nextMinuteDateWithContinuousTime:machContinuousTimeForNextMinute:]
+ _SBLogStatusBarish
- -[SBFMachNextMinuteDateProvider _nextMinuteDateWithAbsoluteTime:machAbsoluteTimeForNextMinute:]
CStrings:
+ "Arming timer for %lu"
+ "Handle clock change notification"
+ "Handle mach timer callback"
+ "Re-arming timer at %@ for %lu"
+ "Tear down timer"
- "_updateHandlers %@"
- "onMachTimer"
- "onNotifyClockSet"

```
