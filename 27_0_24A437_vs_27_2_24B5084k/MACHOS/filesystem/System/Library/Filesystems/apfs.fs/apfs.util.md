## apfs.util

> `/System/Library/Filesystems/apfs.fs/apfs.util`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__got`
- `__DATA.__data`

```diff

-3288.2.1.0.0
-  __TEXT.__text: 0x2efc
-  __TEXT.__auth_stubs: 0x330
-  __TEXT.__cstring: 0x1c29
+3288.40.13.0.0
+  __TEXT.__text: 0x2f88
+  __TEXT.__auth_stubs: 0x340
+  __TEXT.__cstring: 0x1c44
   __TEXT.__const: 0x40
   __TEXT.__unwind_info: 0x128
   __DATA_CONST.__const: 0x68
-  __DATA_CONST.__cfstring: 0x20
-  __DATA_CONST.__auth_got: 0x198
+  __DATA_CONST.__cfstring: 0x60
+  __DATA_CONST.__auth_got: 0x1a0
   __DATA_CONST.__got: 0x30
   __DATA.__data: 0xc
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  Functions: 45
-  Symbols:   60
-  CStrings:  180
+  Functions: 46
+  Symbols:   61
+  CStrings:  182
 
Symbols:
+ _CFEqual
Functions:
~ sub_100001a48 : 112 -> 140
+ sub_100001ad4
CStrings:
+ "IOMatchCategory"
+ "mount_apfs"
```
