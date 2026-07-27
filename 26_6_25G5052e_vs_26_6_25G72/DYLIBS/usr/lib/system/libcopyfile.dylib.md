## libcopyfile.dylib

> `/usr/lib/system/libcopyfile.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`

```diff

-240.160.2.0.0
-  __TEXT.__text: 0x7ca4
-  __TEXT.__auth_stubs: 0x6e0
+240.160.2.0.1
+  __TEXT.__text: 0x7cd0
+  __TEXT.__auth_stubs: 0x6d0
   __TEXT.__const: 0x1c8
   __TEXT.__cstring: 0x1bee
   __TEXT.__unwind_info: 0xe8
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__const: 0x3b0
-  __AUTH_CONST.__auth_got: 0x370
+  __AUTH_CONST.__auth_got: 0x368
   __AUTH_CONST.__const: 0xe0
   __DATA_DIRTY.__bss: 0x10
   - /usr/lib/system/libcompiler_rt.dylib
Functions:
~ _copyfile : 4160 -> 4180
~ _copyfile_set_dst_permissions : 476 -> 500
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.eXFjt8/Sources/copyfile/copyfile.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DJhFSZ/Sources/copyfile/copyfile.c"
```
