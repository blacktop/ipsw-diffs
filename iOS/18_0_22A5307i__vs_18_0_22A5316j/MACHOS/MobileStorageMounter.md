## MobileStorageMounter

> `/usr/libexec/MobileStorageMounter`

```diff

-330.0.0.0.0
-  __TEXT.__text: 0x1c75c
-  __TEXT.__auth_stubs: 0xda0
+331.0.0.0.0
+  __TEXT.__text: 0x1c794
+  __TEXT.__auth_stubs: 0xdc0
   __TEXT.__objc_stubs: 0xd20
   __TEXT.__objc_methlist: 0xbc
   __TEXT.__const: 0x68bc
   __TEXT.__gcc_except_tab: 0x314
   __TEXT.__objc_classname: 0x25
-  __TEXT.__cstring: 0x2392
+  __TEXT.__cstring: 0x23ca
   __TEXT.__oslogstring: 0x1da5
   __TEXT.__objc_methtype: 0x60
   __TEXT.__objc_methname: 0x944
   __TEXT.__unwind_info: 0x448
-  __DATA_CONST.__auth_got: 0x6e0
+  __DATA_CONST.__auth_got: 0x6f0
   __DATA_CONST.__got: 0x198
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__const: 0x16c8
-  __DATA_CONST.__cfstring: 0x2680
+  __DATA_CONST.__cfstring: 0x26a0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   - /System/Library/PrivateFrameworks/DiskImages2.framework/DiskImages2
   - /System/Library/PrivateFrameworks/InstallCoordination.framework/InstallCoordination
   - /System/Library/PrivateFrameworks/ServiceManagement.framework/ServiceManagement
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcryptex.dylib
   - /usr/lib/libimage4.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 341
-  Symbols:   285
-  CStrings:  713
+  Symbols:   287
+  CStrings:  715
 
Symbols:
+ _MGCopyAnswer
+ _os_variant_is_recovery
CStrings:
+ "3kmXfug8VcxLI5yEmsqQKw"
+ "com.apple.mobile.storage_mounter"

```
