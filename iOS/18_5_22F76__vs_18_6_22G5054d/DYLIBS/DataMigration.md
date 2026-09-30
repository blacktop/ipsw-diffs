## DataMigration

> `/System/Library/PrivateFrameworks/DataMigration.framework/DataMigration`

```diff

-2830.1.0.0.0
-  __TEXT.__text: 0x64e4
-  __TEXT.__auth_stubs: 0x890
+2830.1.2.0.0
+  __TEXT.__text: 0x64fc
+  __TEXT.__auth_stubs: 0x8a0
   __TEXT.__objc_methlist: 0x840
-  __TEXT.__cstring: 0x1525
+  __TEXT.__cstring: 0x154f
   __TEXT.__const: 0x18
   __TEXT.__gcc_except_tab: 0x4c
   __TEXT.__unwind_info: 0x278

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x5b8
   __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x458
+  __AUTH_CONST.__auth_got: 0x460
   __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0xe40
+  __AUTH_CONST.__cfstring: 0xe60
   __AUTH_CONST.__objc_const: 0xc68
   __AUTH_CONST.__objc_doubleobj: 0x10
   __DATA.__objc_ivar: 0x74

   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C25FCC63-7D14-3855-B16C-B7C02E3B2202
+  UUID: 04A7F5C7-E47A-3262-A542-DB99F2CD8507
   Functions: 217
-  Symbols:   864
-  CStrings:  553
+  Symbols:   865
+  CStrings:  555
 
Symbols:
+ _xpc_init_services
Functions:
~ -[DMXPCConnection initWithServiceName:] : 448 -> 472
CStrings:
+ "DMXPCConnection calling xpc_init_services"

```
