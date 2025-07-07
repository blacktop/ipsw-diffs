## apfs_vol_converter

> `/System/Library/Filesystems/apfs.fs/apfs_vol_converter`

```diff

-2632.0.36.0.1
-  __TEXT.__text: 0x57ab0
-  __TEXT.__auth_stubs: 0x9e0
+2632.0.54.0.2
+  __TEXT.__text: 0x58000
+  __TEXT.__auth_stubs: 0x9f0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__cstring: 0x11ac6
   __TEXT.__const: 0x2c0
+  __TEXT.__cstring: 0x11b24
   __TEXT.__gcc_except_tab: 0x5cc
-  __TEXT.__unwind_info: 0xb90
-  __DATA_CONST.__auth_got: 0x4f8
+  __TEXT.__unwind_info: 0xbb0
+  __DATA_CONST.__auth_got: 0x500
   __DATA_CONST.__got: 0x78
   __DATA_CONST.__auth_ptr: 0x20
   __DATA_CONST.__const: 0xb20
   __DATA_CONST.__cfstring: 0xb00
-  __DATA.__data: 0x380
+  __DATA.__data: 0x378
   __DATA.__bss: 0x64
   __DATA.__common: 0xf84
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libutil.dylib
-  UUID: 87EC1E55-01E4-338C-BF20-B3AE46B7B2DD
-  Functions: 841
-  Symbols:   183
-  CStrings:  1674
+  UUID: 5DC35821-E60A-383D-A61C-924A9379109F
+  Functions: 847
+  Symbols:   184
+  CStrings:  1676
 
Symbols:
+ _CFStringCreateWithCString
CStrings:
+ "%s:%d: failed to open connection for multikey crypto i/o on device %s: %s\n"
+ "2632.0.54.0.2"
+ "multiKeyEncryption"
- "2632.0.36.0.1"

```
