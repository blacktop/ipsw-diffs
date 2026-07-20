## libcopyfile.dylib

> `/usr/lib/system/libcopyfile.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`

```diff

-260.0.0.0.0
-  __TEXT.__text: 0x7ef8
+260.0.1.0.0
+  __TEXT.__text: 0x7f20
   __TEXT.__const: 0x1c8
   __TEXT.__cstring: 0x1c51
   __TEXT.__unwind_info: 0x100

   __DATA_CONST.__const: 0x3b0
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__auth_got: 0x370
+  __AUTH_CONST.__auth_got: 0x368
   __DATA_DIRTY.__bss: 0x10
   - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libdispatch.dylib
Functions:
~ _copyfile : 4160 -> 4180
~ _copyfile_set_dst_permissions : 480 -> 504
~ _copyfile_unpack_xattr : 484 -> 480
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BTKVGG/Sources/copyfile/copyfile.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bhGYBQ/Sources/copyfile/copyfile.c"
```
