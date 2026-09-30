## afpLoad

> `/System/Library/Filesystems/AppleShare/afpLoad`

```diff

-521.0.0.0.0
-  __TEXT.__text: 0xac8
-  __TEXT.__auth_stubs: 0x180
+523.0.0.0.0
+  __TEXT.__text: 0xb18
+  __TEXT.__auth_stubs: 0x190
   __TEXT.__const: 0x18
   __TEXT.__oslogstring: 0x192
-  __TEXT.__cstring: 0xbd
+  __TEXT.__cstring: 0x1f0
   __TEXT.__unwind_info: 0x78
-  __DATA_CONST.__auth_got: 0xc0
-  __DATA_CONST.__got: 0x20
+  __DATA_CONST.__auth_got: 0xc8
+  __DATA_CONST.__got: 0x28
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x48
   __DATA_CONST.__cfstring: 0x40

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   Functions: 18
-  Symbols:   31
-  CStrings:  20
+  Symbols:   33
+  CStrings:  23
 
Symbols:
+ ___stderrp
+ _fwrite
CStrings:
+ "*** AFP Network Disk Obsoletion Warning ***\n"
+ "*** AFP client is deprecated in the current version and will be removed in a future version of macOS. ***\n"
+ "*** We encourage users to explore alternatives and migrate their workflows before upgrading to the version which removes support for the AFP client. ***\n\n"

```
