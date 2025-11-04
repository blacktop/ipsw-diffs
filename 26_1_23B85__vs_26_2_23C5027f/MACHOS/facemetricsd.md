## facemetricsd

> `/usr/libexec/facemetricsd`

```diff

-18.0.0.0.0
-  __TEXT.__text: 0x5734
-  __TEXT.__auth_stubs: 0x5a0
-  __TEXT.__objc_stubs: 0xde0
-  __TEXT.__objc_methlist: 0x468
+19.0.0.0.0
+  __TEXT.__text: 0x58b4
+  __TEXT.__auth_stubs: 0x5b0
+  __TEXT.__objc_stubs: 0xe60
+  __TEXT.__objc_methlist: 0x4a0
   __TEXT.__cstring: 0x1bb
   __TEXT.__const: 0x60
-  __TEXT.__objc_methname: 0x10da
-  __TEXT.__oslogstring: 0xdd6
+  __TEXT.__objc_methname: 0x1142
+  __TEXT.__oslogstring: 0xe42
   __TEXT.__objc_classname: 0x98
   __TEXT.__objc_methtype: 0x596
   __TEXT.__gcc_except_tab: 0x9c
-  __TEXT.__unwind_info: 0x190
-  __DATA_CONST.__auth_got: 0x2e0
+  __TEXT.__unwind_info: 0x1a0
+  __DATA_CONST.__auth_got: 0x2e8
   __DATA_CONST.__got: 0x208
   __DATA_CONST.__const: 0x190
   __DATA_CONST.__cfstring: 0x120

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0xaa8
-  __DATA.__objc_selrefs: 0x468
+  __DATA.__objc_const: 0xab0
+  __DATA.__objc_selrefs: 0x488
   __DATA.__objc_ivar: 0x64
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x180

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A6767542-BF8E-3FB3-8C75-7D60C545033E
+  UUID: E5920C0A-9E1A-3984-9BF9-B36427A3DBD1
   Functions: 143
-  Symbols:   165
-  CStrings:  361
+  Symbols:   166
+  CStrings:  366
 
Symbols:
+ _dispatch_source_cancel
CStrings:
+ "_stopForegroundCameraSession"
+ "_stopForegroundTimerSession"
+ "_stopUnlockCameraSession"
+ "current time (%f s) is past the message app foreground run time, ending app foreground camera session"
+ "current time (%f s) is past the unlock run time, ending unlock camera session"
+ "discarding this packet since a camera session is no longer active"
+ "sessionTimeoutExpired"
- "app foreground timer took (%f s) which is longer than %f seconds to fire"
- "unlock timer took (%f s) which is longer than %f seconds to fire"

```
