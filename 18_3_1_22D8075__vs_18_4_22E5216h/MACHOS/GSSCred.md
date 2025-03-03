## GSSCred

> `/System/Library/Frameworks/GSS.framework/Helpers/GSSCred`

```diff

-693.60.3.0.0
-  __TEXT.__text: 0x1c728
-  __TEXT.__auth_stubs: 0x1020
+693.100.10.0.0
+  __TEXT.__text: 0x1aed0
+  __TEXT.__auth_stubs: 0x1000
   __TEXT.__objc_stubs: 0xb00
-  __TEXT.__objc_methlist: 0x180
-  __TEXT.__const: 0x40
+  __TEXT.__objc_methlist: 0x2bc
+  __TEXT.__const: 0x48
   __TEXT.__gcc_except_tab: 0x260
   __TEXT.__cstring: 0x1367
   __TEXT.__oslogstring: 0xfb7

   __TEXT.__objc_methtype: 0x25c
   __TEXT.__dlopen_cstrs: 0x66
   __TEXT.__unwind_info: 0x308
-  __DATA_CONST.__auth_got: 0x820
-  __DATA_CONST.__got: 0x1b0
+  __DATA_CONST.__auth_got: 0x810
+  __DATA_CONST.__got: 0x1c0
   __DATA_CONST.__const: 0xae0
   __DATA_CONST.__cfstring: 0xe40
   __DATA_CONST.__objc_classlist: 0x30

   __DATA_CONST.__objc_intobj: 0x60
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x870
-  __DATA.__objc_selrefs: 0x308
+  __DATA.__objc_const: 0x628
+  __DATA.__objc_selrefs: 0x3a8
   __DATA.__objc_ivar: 0x10
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x150

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 269
+  Functions: 283
   Symbols:   325
   CStrings:  526
 
CStrings:
+ "Failed to store credentials for cache %u: %s"
+ "new connection from %@, asid: %u"
+ "unable to acquire credential without attributes %u"
+ "unable to acquire credential without attributes: %u"
+ "unable to acquire credential without cache uuid %u"
+ "unable to acquire credential without password %u"
+ "unable to acquire credential without principal: %u"
+ "unable to find cache %u, %d"
+ "unable to init cred context %u, %d"
+ "unable to retrieve principal %u, %d"
+ "unable to save cred in cache: %u, %d"
+ "unable to set password %u, %d"
- "Failed to store credentials for cache %d: %s"
- "new connection from %@, asid: %d"
- "unable to acquire credential without attributes %d"
- "unable to acquire credential without attributes: %d"
- "unable to acquire credential without cache uuid %d"
- "unable to acquire credential without password %d"
- "unable to acquire credential without principal: %d"
- "unable to find cache %d, %d"
- "unable to init cred context %d, %d"
- "unable to retrieve principal %d, %d"
- "unable to save cred in cache: %d, %d"
- "unable to set password %d, %d"

```
