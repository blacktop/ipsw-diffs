## Security

> `/System/Library/Frameworks/Security.framework/Security`

```diff

-61439.40.34.0.0
-  __TEXT.__text: 0x167bf0
+61439.40.45.0.1
+  __TEXT.__text: 0x167ed0
   __TEXT.__auth_stubs: 0x3d40
   __TEXT.__objc_methlist: 0x4880
   __TEXT.__const: 0x9b38
-  __TEXT.__cstring: 0x175ae
+  __TEXT.__cstring: 0x175df
   __TEXT.__gcc_except_tab: 0x8c48
   __TEXT.__oslogstring: 0xebd4
   __TEXT.__dlopen_cstrs: 0x359
   __TEXT.__ustring: 0x406
   __TEXT.__dof_codesign: 0x1ffd
   __TEXT.__dof_security_: 0x325
-  __TEXT.__unwind_info: 0x5d20
+  __TEXT.__unwind_info: 0x5d18
   __TEXT.__objc_classname: 0xa03
-  __TEXT.__objc_methname: 0xaa1a
+  __TEXT.__objc_methname: 0xaa28
   __TEXT.__objc_methtype: 0x32a1
   __TEXT.__objc_stubs: 0x7ec0
   __DATA_CONST.__got: 0x700
-  __DATA_CONST.__const: 0x11b58
+  __DATA_CONST.__const: 0x11b78
   __DATA_CONST.__objc_classlist: 0x2c0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xf8

   __AUTH_CONST.__auth_got: 0x1eb8
   __AUTH_CONST.__auth_ptr: 0x18
   __AUTH_CONST.__const: 0x4320
-  __AUTH_CONST.__cfstring: 0x14b60
+  __AUTH_CONST.__cfstring: 0x14bc0
   __AUTH_CONST.__objc_const: 0x9e50
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_intobj: 0x120

   - /usr/lib/libcoretls_cfhelpers.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 6580
-  Symbols:   9165
-  CStrings:  7819
+  Functions: 6582
+  Symbols:   9169
+  CStrings:  7822
 
Symbols:
+ _SecPolicyCheckCertValidLeaf
+ _SecPolicyCreateDCAttestation
+ _kSecPolicyAppleDCAttestation
+ _kSecPolicyCheckValidLeaf
CStrings:
+ "clearCliqueFromAccount:resetReason:reply:"
+ "clearCliqueFromAccount:error:"
+ "1.2.840.113635.100.1.119"
+ "ValidLeaf"
+ "DCAttestation"
- "resetAcountData:resetReason:reply:"
- "resetAcountData:error:"

```
