## coreautha

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/coreautha.bundle/Contents/MacOS/coreautha`

```diff

-  __TEXT.__text: 0x14c28
-  __TEXT.__auth_stubs: 0x510
-  __TEXT.__objc_stubs: 0x38a0
+  __TEXT.__text: 0x14cc0
+  __TEXT.__auth_stubs: 0x530
+  __TEXT.__objc_stubs: 0x38c0
   __TEXT.__objc_methlist: 0x191c
-  __TEXT.__const: 0x180
-  __TEXT.__objc_methname: 0x3d8e
+  __TEXT.__const: 0x188
+  __TEXT.__objc_methname: 0x3da0
   __TEXT.__objc_classname: 0x388
   __TEXT.__objc_methtype: 0xfc3
   __TEXT.__gcc_except_tab: 0x1b0
-  __TEXT.__oslogstring: 0x110d
+  __TEXT.__oslogstring: 0x1149
   __TEXT.__cstring: 0x1750
-  __TEXT.__unwind_info: 0x538
-  __DATA_CONST.__const: 0x6d0
+  __TEXT.__unwind_info: 0x540
+  __DATA_CONST.__const: 0x6f0
   __DATA_CONST.__cfstring: 0xca0
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_catlist: 0x10

   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_intobj: 0x120
-  __DATA_CONST.__auth_got: 0x298
-  __DATA_CONST.__got: 0x320
+  __DATA_CONST.__auth_got: 0x2a8
+  __DATA_CONST.__got: 0x340
   __DATA.__objc_const: 0x4b30
-  __DATA.__objc_selrefs: 0x1268
+  __DATA.__objc_selrefs: 0x1270
   __DATA.__objc_ivar: 0x184
   __DATA.__objc_data: 0x780
   __DATA.__data: 0x7e0

   - /System/Library/PrivateFrameworks/login.framework/Versions/A/login
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 487
-  Symbols:   204
-  CStrings:  1351
+  Functions: 488
+  Symbols:   207
+  CStrings:  1353
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ _LACLogSessions
+ _OBJC_CLASS_$_LACUIWindowSessionDisconnectionMonitor
+ _getuid
Functions:
~ sub_100014d1c : 320 -> 372
+ sub_100015e50
CStrings:
+ "Exiting so launchd respawns coreautha into the live session"
+ "startWithHandler:"

```
