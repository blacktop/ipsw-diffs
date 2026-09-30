## usermanagerd

> `/usr/libexec/usermanagerd`

```diff

-452.0.0.0.0
-  __TEXT.__text: 0xb15a4
+458.0.0.502.1
+  __TEXT.__text: 0xb1a74
   __TEXT.__auth_stubs: 0x18c0
-  __TEXT.__objc_stubs: 0x22a0
-  __TEXT.__objc_methlist: 0x19e8
+  __TEXT.__objc_stubs: 0x22c0
+  __TEXT.__objc_methlist: 0x19f8
   __TEXT.__const: 0x1384
   __TEXT.__gcc_except_tab: 0x16c4
-  __TEXT.__cstring: 0x6dbb
+  __TEXT.__cstring: 0x6df5
   __TEXT.__objc_classname: 0x39a
-  __TEXT.__objc_methname: 0x37f1
+  __TEXT.__objc_methname: 0x3856
   __TEXT.__objc_methtype: 0x146e
-  __TEXT.__oslogstring: 0x118be
-  __TEXT.__unwind_info: 0x14b8
+  __TEXT.__oslogstring: 0x11a01
+  __TEXT.__unwind_info: 0x14c0
   __DATA_CONST.__auth_got: 0xc70
   __DATA_CONST.__got: 0x1c0
   __DATA_CONST.__auth_ptr: 0x58
-  __DATA_CONST.__const: 0x2740
+  __DATA_CONST.__const: 0x2770
   __DATA_CONST.__cfstring: 0x1ca0
   __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_protolist: 0x80

   __DATA_CONST.__objc_arraydata: 0xe0
   __DATA_CONST.__objc_arrayobj: 0xa8
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x4678
-  __DATA.__objc_selrefs: 0xcd8
-  __DATA.__objc_ivar: 0x1e0
+  __DATA.__objc_const: 0x46a0
+  __DATA.__objc_selrefs: 0xce0
+  __DATA.__objc_ivar: 0x1e4
   __DATA.__objc_data: 0xa00
   __DATA.__data: 0x12a0
   __DATA.__bss: 0x371

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  UUID: D47321E1-6DCC-38CE-8F04-2E8E96979720
-  Functions: 2195
+  UUID: 07F196DF-6969-3D55-85BD-D63ABDA8C39D
+  Functions: 2202
   Symbols:   466
-  CStrings:  3558
+  CStrings:  3567
 
CStrings:
+ "/.exclave"
+ "FAILED TO MOUNT USER DATA VOLUME with ERROR: %d"
+ "Token Validated as VerifyPassword  is successful,"
+ "Unable to verify the token with Error:%ld"
+ "Updated Persona Generation Count for Persona Creation:%llu"
+ "Updated Persona Generation Count for Post Persona Deletion:%llu"
+ "Updated Persona Generation Count for Pre Persona Deletion:%llu"
+ "Updated Persona Generation Count for Updation of BundleID:%llu"
+ "Updated Persona Generation Count for updation of  Multi Persona BundleID:%llu"
+ "Volume already mounted, returning success.."
+ "_verifyIdentityPasswordErrorOverride"
+ "updateAPFSDevWithCurrentBootContainer failed with error:%d"
+ "verifyIdentityPasswordInSession:passcode:isACMCredential:error:"
- "AKSLoadIdentity after check failed with Error:%d"
- "Token Validated as Unlock with it is successful, attempting locking the identity"
- "Unable to unlock the idenitity with Error:%ld"
- "Volume already mounted"

```
