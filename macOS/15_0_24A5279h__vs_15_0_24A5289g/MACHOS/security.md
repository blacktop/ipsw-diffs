## security

> `/usr/bin/security`

```diff

-61439.0.77.0.0
-  __TEXT.__text: 0x21de8
-  __TEXT.__auth_stubs: 0x1ee0
-  __TEXT.__objc_stubs: 0x8c0
+61439.0.101.0.0
+  __TEXT.__text: 0x23200
+  __TEXT.__auth_stubs: 0x1ef0
+  __TEXT.__objc_stubs: 0x9e0
   __TEXT.__objc_methlist: 0x128
   __TEXT.__const: 0x820
-  __TEXT.__gcc_except_tab: 0xb28
-  __TEXT.__cstring: 0xbc5b
-  __TEXT.__oslogstring: 0x2e4
-  __TEXT.__objc_methname: 0x67a
+  __TEXT.__gcc_except_tab: 0xbd0
+  __TEXT.__cstring: 0xc0c4
+  __TEXT.__oslogstring: 0x326
+  __TEXT.__dlopen_cstrs: 0x10b
   __TEXT.__objc_classname: 0x12
+  __TEXT.__objc_methname: 0x714
   __TEXT.__objc_methtype: 0xed
-  __TEXT.__dlopen_cstrs: 0x5d
   __TEXT.__dof_security_: 0x2a0
-  __TEXT.__unwind_info: 0x858
-  __DATA_CONST.__auth_got: 0xf88
-  __DATA_CONST.__got: 0x3f0
+  __TEXT.__unwind_info: 0x880
+  __DATA_CONST.__auth_got: 0xf90
+  __DATA_CONST.__got: 0x3f8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x1a08
-  __DATA_CONST.__cfstring: 0xb40
+  __DATA_CONST.__const: 0x1a58
+  __DATA_CONST.__cfstring: 0xbc0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8

   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA.__objc_const: 0x220
-  __DATA.__objc_selrefs: 0x278
+  __DATA.__objc_selrefs: 0x2c0
   __DATA.__objc_ivar: 0x20
   __DATA.__objc_data: 0x50
   __DATA.__data: 0xa8
-  __DATA.__bss: 0x16e0
+  __DATA.__bss: 0x1700
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 442
-  Symbols:   643
-  CStrings:  1039
+  Functions: 448
+  Symbols:   645
+  CStrings:  1075
 
Symbols:
+ _OBJC_CLASS_$_NSMutableSet
+ ___strncpy_chk
CStrings:
+ "%!l(MISSING)d. %!s(MISSING)\n"
+ "/System/Library/PrivateFrameworks/PlatformSSOCore.framework/Contents/MacOS/PlatformSSOCore"
+ "/System/Library/PrivateFrameworks/StorageKit.framework/Contents/MacOS/StorageKit"
+ "Archiver failed: %!s(MISSING)\n"
+ "Class getPOLoginUserCoreClass(void)_block_invoke"
+ "Class getSKManagerClass(void)_block_invoke"
+ "EBC6C064-0000-11AA-AA11-00306543ECAC"
+ "Enter user name: "
+ "Failure\n"
+ "Handles Platform SSO specific settings and overrides."
+ "No PlatformSSO support on this machine for this command\n"
+ "No avaiable users\n"
+ "POLoginUserCore"
+ "Please select volume which contain user %!s(MISSING):\n"
+ "Recovery Key: "
+ "SKManager"
+ "Success"
+ "Unable to get the credentials\n"
+ "User %!s(MISSING) is not available\n"
+ "User was not specified.\n"
+ "Volume %!@(MISSING) (name %!@(MISSING), UUUD %!@(MISSING))"
+ "Volume %!s(MISSING) is not available\n"
+ "Volume %!s(MISSING) selected.\n"
+ "Volume users error %!d(MISSING)\n"
+ "Volume was not specified.\n"
+ "Wrong line number, please enter 1-%!l(MISSING)u.\n"
+ "Your choice: "
+ "bypass-login-policy"
+ "bypass-login-policy [-u user] [-v volumeUUID]\n  -u user name\n  -v APFS volume UUID (case insensitive)\n  If any argument is missing, the tool will prompt for it\n"
+ "dnode"
+ "platformsso"
+ "psso.m"
+ "u:v:"
+ "void *PlatformSSOCoreLibrary(void)"
+ "void *StorageKitLibrary(void)"
+ "voluid"

```
