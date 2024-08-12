## Security

> `/System/Library/Frameworks/Security.framework/Security`

```diff

-61439.40.9.0.0
-  __TEXT.__text: 0x1671fc
+61439.40.30.0.1
+  __TEXT.__text: 0x1677e8
   __TEXT.__auth_stubs: 0x3d40
   __TEXT.__objc_methlist: 0x4868
-  __TEXT.__const: 0x9750
-  __TEXT.__cstring: 0x17539
-  __TEXT.__gcc_except_tab: 0x8c1c
-  __TEXT.__oslogstring: 0xeb21
+  __TEXT.__const: 0x9760
+  __TEXT.__cstring: 0x175b4
+  __TEXT.__gcc_except_tab: 0x8c48
+  __TEXT.__oslogstring: 0xeb99
   __TEXT.__dlopen_cstrs: 0x359
   __TEXT.__ustring: 0x406
   __TEXT.__dof_codesign: 0x1ffd
   __TEXT.__dof_security_: 0x325
-  __TEXT.__unwind_info: 0x5cf8
+  __TEXT.__unwind_info: 0x5d18
   __TEXT.__objc_classname: 0xa03
   __TEXT.__objc_methname: 0xa9ea
   __TEXT.__objc_methtype: 0x32a1
   __TEXT.__objc_stubs: 0x7e80
   __DATA_CONST.__got: 0x6f8
-  __DATA_CONST.__const: 0x11b48
+  __DATA_CONST.__const: 0x11b50
   __DATA_CONST.__objc_classlist: 0x2c0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xf8

   __DATA_CONST.__objc_arraydata: 0xe8
   __AUTH_CONST.__auth_got: 0x1eb8
   __AUTH_CONST.__auth_ptr: 0x18
-  __AUTH_CONST.__const: 0x4340
-  __AUTH_CONST.__cfstring: 0x14ac0
+  __AUTH_CONST.__const: 0x4320
+  __AUTH_CONST.__cfstring: 0x14b40
   __AUTH_CONST.__objc_const: 0x9e50
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_intobj: 0x120

   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x48
   __DATA.__objc_ivar: 0x518
-  __DATA.__data: 0x20b8
+  __DATA.__data: 0x20b0
   __DATA.__bss: 0x9e8
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x190

   - /usr/lib/libcoretls_cfhelpers.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 6573
-  Symbols:   9156
-  CStrings:  7808
+  Functions: 6578
+  Symbols:   9162
+  CStrings:  7816
 
Symbols:
+ _SecPolicyCreateParakeetService
+ _kSecPolicyAppleParakeetService
CStrings:
+ "1.2.840.113635.100.1.118"
+ "Failed to get exception for epoch check."
+ "NSString *getkSecurityRTCEventNameRPDDeleteAllRecords(void)"
+ "ParakeetService"
+ "Skipping general names after the first %!d(MISSING)"
+ "Skipping subtrees after the first %!d(MISSING)"
+ "Unable to get digest of certificate at index %!l(MISSING)ld"
+ "fresh"
+ "kSecurityRTCEventNameRPDDeleteAllRecords"
+ "verify"
- "SecKeychainStaticPersistentRefs"
- "Static Persistent Refs are %!@(MISSING) (via feature flags)"

```
