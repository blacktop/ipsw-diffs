## hfs.util

> `/System/Library/Filesystems/hfs.fs/hfs.util`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__got`

```diff

-753.40.3.0.0
-  __TEXT.__text: 0x47cc
-  __TEXT.__auth_stubs: 0x410
+753.40.4.0.0
+  __TEXT.__text: 0x49f8
+  __TEXT.__auth_stubs: 0x420
   __TEXT.__const: 0xa8
-  __TEXT.__cstring: 0x12a3
-  __TEXT.__unwind_info: 0xe8
-  __DATA_CONST.__auth_got: 0x208
+  __TEXT.__cstring: 0x12cf
+  __TEXT.__unwind_info: 0x100
+  __DATA_CONST.__auth_got: 0x210
   __DATA_CONST.__got: 0x18
   __DATA.__data: 0x5e
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libSystem.B.dylib
-  Functions: 28
-  Symbols:   70
-  CStrings:  127
+  Functions: 31
+  Symbols:   71
+  CStrings:  128
 
Symbols:
+ _warnx
CStrings:
+ "couldn't convert volume status database: %s"
```
