## installcoordination_proxy

> `/System/Library/PrivateFrameworks/InstallCoordination.framework/Support/installcoordination_proxy`

```diff

-755.0.0.0.0
-  __TEXT.__text: 0x122cc
-  __TEXT.__auth_stubs: 0x970
-  __TEXT.__objc_stubs: 0x1f40
-  __TEXT.__objc_methlist: 0xcec
+763.0.0.502.1
+  __TEXT.__text: 0x12588
+  __TEXT.__auth_stubs: 0x9b0
+  __TEXT.__objc_stubs: 0x1f80
+  __TEXT.__objc_methlist: 0xd14
   __TEXT.__const: 0xb8
   __TEXT.__gcc_except_tab: 0xc0
-  __TEXT.__cstring: 0x2152
+  __TEXT.__cstring: 0x228e
   __TEXT.__objc_classname: 0x18c
-  __TEXT.__objc_methname: 0x2bbe
+  __TEXT.__objc_methname: 0x2c74
   __TEXT.__oslogstring: 0x1a5f
-  __TEXT.__objc_methtype: 0x7b1
-  __TEXT.__unwind_info: 0x420
-  __DATA_CONST.__auth_got: 0x4c8
-  __DATA_CONST.__got: 0x198
+  __TEXT.__objc_methtype: 0x7e2
+  __TEXT.__unwind_info: 0x430
+  __DATA_CONST.__auth_got: 0x4e8
+  __DATA_CONST.__got: 0x1a0
   __DATA_CONST.__const: 0x4b8
-  __DATA_CONST.__cfstring: 0xbe0
+  __DATA_CONST.__cfstring: 0xc40
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38

   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA.__objc_const: 0x1b28
-  __DATA.__objc_selrefs: 0xa18
+  __DATA.__objc_selrefs: 0xa40
   __DATA.__objc_ivar: 0xb4
   __DATA.__objc_data: 0x2d0
   __DATA.__data: 0x2b0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 11D8B446-AADE-3794-94B1-B124F8A0D26D
-  Functions: 401
-  Symbols:   212
-  CStrings:  963
+  UUID: FAF6997B-83D1-3E2F-B6D5-EE6B9033472A
+  Functions: 404
+  Symbols:   217
+  CStrings:  980
 
Symbols:
+ _SANDBOX_EXTENSION_DEFAULT
+ _sandbox_extension_consume
+ _sandbox_extension_issue_file
+ _sandbox_extension_release
+ _strlen
CStrings:
+ "-[IXFileManager consumeSandboxExtension:error:]"
+ "-[IXFileManager issueSandboxExtensionForURL:withExtensionClass:error:]"
+ "-[IXFileManager releaseSandboxExtensionToken:error:]"
+ "22:31:51"
+ "@40@0:8@16r*24^@32"
+ "B32@0:8q16^@24"
+ "Jun 16 2025"
+ "UTF8String"
+ "consumeSandboxExtension:error:"
+ "initWithBytesNoCopy:length:encoding:freeWhenDone:"
+ "issueSandboxExtensionForURL:withExtensionClass:error:"
+ "q32@0:8@16^@24"
+ "releaseSandboxExtensionToken:error:"
+ "sandbox_extension_consume for %s failed: %s."
+ "sandbox_extension_issue_file for path %@ failed: %s"
+ "sandbox_extension_release for %lld failed: %s."
- "04:44:44"
- "May 23 2025"

```
