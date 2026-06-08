## AppleCredentialManagerDaemon

> `/System/Library/PrivateFrameworks/AppleCredentialManager.framework/AppleCredentialManagerDaemon`

```diff

-864.120.2.0.0
-  __TEXT.__text: 0x148d8
-  __TEXT.__auth_stubs: 0x4c0
+944.0.0.0.0
+  __TEXT.__text: 0x1396c
+  __TEXT.__auth_stubs: 0x4f0
   __TEXT.__objc_stubs: 0x580
   __TEXT.__objc_methlist: 0x14c
   __TEXT.__objc_methname: 0x447
-  __TEXT.__objc_classname: 0x2f
+  __TEXT.__objc_classname: 0x2d
+  __TEXT.__cstring: 0x28bf
   __TEXT.__objc_methtype: 0x92
   __TEXT.__const: 0x128
-  __TEXT.__cstring: 0x2888
-  __TEXT.__oslogstring: 0x7cf
-  __TEXT.__unwind_info: 0x368
-  __DATA_CONST.__auth_got: 0x268
-  __DATA_CONST.__got: 0x88
-  __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x178
+  __TEXT.__oslogstring: 0x763
+  __TEXT.__unwind_info: 0x3a0
+  __DATA_CONST.__const: 0x1e0
   __DATA_CONST.__cfstring: 0x1c0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
+  __DATA_CONST.__auth_got: 0x280
+  __DATA_CONST.__got: 0x88
+  __DATA_CONST.__auth_ptr: 0x18
   __DATA.__objc_const: 0x160
   __DATA.__objc_selrefs: 0x170
   __DATA.__objc_ivar: 0x4

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5C314E6D-C2CD-3CE7-BCD9-870062CB5764
-  Functions: 502
-  Symbols:   102
+  UUID: 552E0763-0CC7-323D-8B6B-070D195F0B92
+  Functions: 495
+  Symbols:   105
   CStrings:  421
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x21
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x22
CStrings:
+ "%s: %s: XPC Event: %@ (%s).\n"
+ "ACMCredential - ACMCredentialDataPKITokenValidated"
+ "ACMCredential - ACMCredentialDataPKITokenValidated2"
+ "ACMGetEnvironmentVariableData"
+ "distnoted"
+ "fsevents"
+ "iokit"
+ "notifyd"
- "%s: %s: XPC Event: %@ (distnoted).\n"
- "%s: %s: XPC Event: %@ (fsevents).\n"
- "%s: %s: XPC Event: %@ (iokit).\n"
- "%s: %s: XPC Event: %@ (notifyd).\n"
- "processing distnoted.matching"
- "processing fsevents.matching"
- "processing iokit.matching"
- "processing notifyd.matching"

```
