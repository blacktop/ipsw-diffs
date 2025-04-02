## check_afp

> `/System/Library/Filesystems/AppleShare/check_afp.app/Contents/MacOS/check_afp`

```diff

-521.0.0.0.0
-  __TEXT.__text: 0x20bc
-  __TEXT.__auth_stubs: 0x3d0
+523.0.0.0.0
+  __TEXT.__text: 0x2110
+  __TEXT.__auth_stubs: 0x3e0
   __TEXT.__objc_stubs: 0x80
   __TEXT.__const: 0x10
-  __TEXT.__cstring: 0x10f2
+  __TEXT.__cstring: 0x1225
   __TEXT.__objc_methname: 0x4e
   __TEXT.__unwind_info: 0xb0
-  __DATA_CONST.__auth_got: 0x1f0
-  __DATA_CONST.__got: 0x30
+  __DATA_CONST.__auth_got: 0x1f8
+  __DATA_CONST.__got: 0x38
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x48
   __DATA_CONST.__cfstring: 0x1e0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 23
-  Symbols:   71
-  CStrings:  118
+  Symbols:   73
+  CStrings:  121
 
Symbols:
+ ___stderrp
+ _fwrite
CStrings:
+ "*** AFP Network Disk Obsoletion Warning ***\n"
+ "*** AFP client is deprecated in the current version and will be removed in a future version of macOS. ***\n"
+ "*** We encourage users to explore alternatives and migrate their workflows before upgrading to the version which removes support for the AFP client. ***\n\n"

```
