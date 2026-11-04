## apfs_checkseal

> `/System/Library/Filesystems/apfs.fs/apfs_checkseal`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-3288.42.1.0.0
-  __TEXT.__text: 0x4fbf8
+3288.60.7.0.0
+  __TEXT.__text: 0x4fb78
   __TEXT.__auth_stubs: 0x760
   __TEXT.__const: 0x4c0
-  __TEXT.__cstring: 0x10117
-  __TEXT.__unwind_info: 0xb40
+  __TEXT.__cstring: 0x10169
+  __TEXT.__unwind_info: 0xb50
   __DATA_CONST.__const: 0x7b8
   __DATA_CONST.__cfstring: 0x160
   __DATA_CONST.__auth_got: 0x3b0

   - /System/Library/PrivateFrameworks/AppleFSCompression.framework/AppleFSCompression
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  Functions: 748
+  Functions: 751
   Symbols:   133
-  CStrings:  1295
+  CStrings:  1296
 
CStrings:
+ "%s:%d: %s error: chunk info index %u out of range for cib %u chunk info count %u\n"
```
