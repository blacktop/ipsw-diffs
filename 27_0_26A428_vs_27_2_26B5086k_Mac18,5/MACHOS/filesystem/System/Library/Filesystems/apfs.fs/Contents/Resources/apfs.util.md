## apfs.util

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs.util`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__got`
- `__DATA.__data`

```diff

-3288.1.3.0.0
-  __TEXT.__text: 0x2ef0
-  __TEXT.__auth_stubs: 0x330
-  __TEXT.__cstring: 0x1bd9
+3288.40.13.0.0
+  __TEXT.__text: 0x2f7c
+  __TEXT.__auth_stubs: 0x340
+  __TEXT.__cstring: 0x1bf4
   __TEXT.__const: 0x40
   __TEXT.__unwind_info: 0x128
   __DATA_CONST.__const: 0x68
-  __DATA_CONST.__cfstring: 0x20
-  __DATA_CONST.__auth_got: 0x198
+  __DATA_CONST.__cfstring: 0x60
+  __DATA_CONST.__auth_got: 0x1a0
   __DATA_CONST.__got: 0x30
   __DATA.__data: 0xc
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/APFS.framework/Versions/A/APFS
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  Functions: 45
-  Symbols:   60
-  CStrings:  179
+  Functions: 46
+  Symbols:   61
+  CStrings:  181
 
Symbols:
+ _CFEqual
Functions:
~ sub_100001a68 : 112 -> 140
+ sub_100001af4
CStrings:
+ "IOMatchCategory"
+ "mount_apfs"
```
