## IdleTimerServices

> `/System/Library/PrivateFrameworks/IdleTimerServices.framework/Versions/A/IdleTimerServices`

```diff

-37.0.0.0.0
-  __TEXT.__text: 0x2514
+37.4.1.0.0
+  __TEXT.__text: 0x25f0
   __TEXT.__auth_stubs: 0x280
-  __TEXT.__objc_methlist: 0x2d4
+  __TEXT.__objc_methlist: 0x4b4
   __TEXT.__const: 0x88
   __TEXT.__cstring: 0x1f3
   __TEXT.__oslogstring: 0x434
   __TEXT.__gcc_except_tab: 0x34
-  __TEXT.__unwind_info: 0x150
+  __TEXT.__unwind_info: 0x160
   __TEXT.__objc_classname: 0x13d
   __TEXT.__objc_methname: 0xa65
   __TEXT.__objc_methtype: 0x37a

   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x258
+  __DATA_CONST.__objc_selrefs: 0x2f0
   __DATA_CONST.__objc_superrefs: 0x28
   __AUTH_CONST.__auth_got: 0x150
   __AUTH_CONST.__const: 0xd0
   __AUTH_CONST.__cfstring: 0x260
-  __AUTH_CONST.__objc_const: 0x1310
+  __AUTH_CONST.__objc_const: 0xfb8
   __AUTH.__objc_data: 0x280
   __DATA.__objc_ivar: 0x3c
   __DATA.__data: 0x248

   - /System/Library/PrivateFrameworks/BoardServices.framework/Versions/A/BoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0B76BC1A-B07F-39B8-93FB-F9640FB5299B
-  Functions: 73
-  Symbols:   324
+  UUID: 8698D873-B9AB-33EA-8CCC-3E9875E57637
+  Functions: 79
+  Symbols:   330
   CStrings:  242
 
Symbols:
+ +[ITIdleTimerState sharedInstance].cold.1
+ -[ITIdleTimerState newAssertionToDisableIdleTimerForReason:error:].cold.1
+ -[ITIdleTimerState newIdleTimerAssertionWithConfiguration:forReason:error:].cold.2
+ -[ITIdleTimerStateModel _access_newIdleTimerAssertionWithConfiguration:forReason:error:].cold.1
+ -[ITIdleTimerStateModel newIdleTimerAssertionWithConfiguration:forReason:error:].cold.1
+ ITLogIdleTimer.cold.1

```
