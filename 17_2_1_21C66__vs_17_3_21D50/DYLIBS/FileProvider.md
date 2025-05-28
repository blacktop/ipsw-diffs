## FileProvider

> `/System/Library/Frameworks/FileProvider.framework/FileProvider`

```diff

-1703.62.4.0.0
-  __TEXT.__text: 0x11b158
-  __TEXT.__auth_stubs: 0x19c0
+1703.80.16.0.0
+  __TEXT.__text: 0x11b274
+  __TEXT.__auth_stubs: 0x19d0
   __TEXT.__objc_methlist: 0xb840
   __TEXT.__const: 0x3b0
   __TEXT.__gcc_except_tab: 0x778c
-  __TEXT.__cstring: 0x13246
+  __TEXT.__cstring: 0x13247
   __TEXT.__oslogstring: 0xc8cc
   __TEXT.__dlopen_cstrs: 0x7ed
   __TEXT.__ustring: 0x8
   __TEXT.__unwind_info: 0x4e7c
   __TEXT.__objc_classname: 0x1e1e
-  __TEXT.__objc_methname: 0x20af0
+  __TEXT.__objc_methname: 0x20af6
   __TEXT.__objc_methtype: 0x5bae
   __TEXT.__objc_stubs: 0x129a0
   __DATA_CONST.__got: 0x4b0

   __AUTH_CONST.__objc_arrayobj: 0x168
   __AUTH_CONST.__auth_ptr: 0x30
   __AUTH_CONST.__objc_intobj: 0x108
-  __AUTH_CONST.__auth_got: 0xcf0
+  __AUTH_CONST.__auth_got: 0xcf8
   __AUTH.__objc_data: 0x190
   __AUTH.__data: 0x10
   __DATA.__objc_protorefs: 0x128

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 6815
-  Symbols:   21634
+  Functions: 6816
+  Symbols:   21636
   CStrings:  9408
 
Symbols:
+ +[FPFileVersion etagForVersion:providerDomainID:]
+ _faccessat
+ _fpfs_lp_faccessat
+ _objc_msgSend$etagForVersion:providerDomainID:
- +[FPFileVersion etagForVersion:identifier:]
- _objc_msgSend$etagForVersion:identifier:
CStrings:
+ "1703.80.16"
+ "etagForVersion:providerDomainID:"
- "1703.62.4"
- "etagForVersion:identifier:"

```
