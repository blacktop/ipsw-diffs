## Security

> `/System/Library/Frameworks/Security.framework/Security`

```diff

-61439.80.12.0.0
-  __TEXT.__text: 0x1704bc
-  __TEXT.__auth_stubs: 0x3d80
+61439.82.1.0.0
+  __TEXT.__text: 0x170994
+  __TEXT.__auth_stubs: 0x3d90
   __TEXT.__objc_methlist: 0x5308
-  __TEXT.__const: 0x9b38
-  __TEXT.__cstring: 0x17927
-  __TEXT.__gcc_except_tab: 0x8cf8
-  __TEXT.__oslogstring: 0xed40
+  __TEXT.__const: 0xa5f0
+  __TEXT.__cstring: 0x179aa
+  __TEXT.__gcc_except_tab: 0x8d38
+  __TEXT.__oslogstring: 0xedc1
   __TEXT.__dlopen_cstrs: 0x359
   __TEXT.__ustring: 0x406
   __TEXT.__dof_codesign: 0x1ffd
   __TEXT.__dof_security_: 0x325
-  __TEXT.__unwind_info: 0x5f00
+  __TEXT.__unwind_info: 0x5f18
   __TEXT.__objc_classname: 0xadd
   __TEXT.__objc_methname: 0xb655
   __TEXT.__objc_methtype: 0x34b7

   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x2c0
   __DATA_CONST.__objc_arraydata: 0xf8
-  __AUTH_CONST.__auth_got: 0x1ed8
+  __AUTH_CONST.__auth_got: 0x1ee0
   __AUTH_CONST.__auth_ptr: 0x18
   __AUTH_CONST.__const: 0x4360
-  __AUTH_CONST.__cfstring: 0x15280
+  __AUTH_CONST.__cfstring: 0x152e0
   __AUTH_CONST.__objc_const: 0xae00
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_intobj: 0x138

   - /usr/lib/libcoretls_cfhelpers.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 6814
-  Symbols:   9407
-  CStrings:  8082
+  Functions: 6818
+  Symbols:   9412
+  CStrings:  8088
 
Symbols:
+ _CFDictionaryReplaceValue
CStrings:
+ "%p fixed osinstallersetupd entitlements"
+ "%p unable to fixup entitlement dictionary"
+ "Fixed TCC entitlements for osinstallerstupd %d"
+ "SecTaskLoadEntitlements: failed to get cs_flags, error=%d, pid=%d"
+ "com.apple.installer.osinstallersetupd"
+ "com.apple.private.tcc.allow"
+ "kTCCServiceSystemPolicyAllFiles"
- "Failed to get cs_flags, error=%d"

```
