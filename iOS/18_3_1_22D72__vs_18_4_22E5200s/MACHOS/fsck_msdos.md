## fsck_msdos

> `/System/Library/Filesystems/msdos.fs/fsck_msdos`

```diff

-720.80.2.0.0
-  __TEXT.__text: 0x5458
-  __TEXT.__auth_stubs: 0x1e0
-  __TEXT.__const: 0x8
-  __TEXT.__cstring: 0x117f
-  __TEXT.__unwind_info: 0x118
-  __DATA_CONST.__auth_got: 0xf0
+747.100.19.0.0
+  __TEXT.__text: 0x6270
+  __TEXT.__auth_stubs: 0x210
+  __TEXT.__const: 0x90
+  __TEXT.__cstring: 0x12e7
+  __TEXT.__unwind_info: 0x108
+  __DATA_CONST.__auth_got: 0x108
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x60
   __DATA.__common: 0x68
   __DATA.__bss: 0x560
   - /usr/lib/libSystem.B.dylib
-  Functions: 68
-  Symbols:   41
-  CStrings:  137
+  Functions: 67
+  Symbols:   44
+  CStrings:  146
 
Symbols:
+ _asprintf
+ _ftruncate
+ _strdup
CStrings:
+ "%s-%d"
+ "%s/shadow-%d"
+ "%s/shadow-r%s"
+ "Can't open\n"
+ "Failed to open shadow file at %s (%d)\n"
+ "Failed to shadow at offset 0x%llx, length 0x%x (errno %d)"
+ "Failed to shadow at offset 0x%llx, length 0x%zx (errno %d)"
+ "Failed to shadow offset 0, length 0x%x (errno: %d)"
+ "Failed to shadow offset 0x%x, length 0x%x (errno %d)"
+ "Failed to truncate shadow file to size 0x%x (errno %d)"
+ "Usage: fsck_msdos [-fnpqy] [-M <integer>[k|K|m|M]] [-S path] filesystem ... "
+ "Warning: (NO WRITE)\n"
+ "pynfqM:S:"
- "Can't open"
- "Usage: fsck_msdos [-fnpqy] [-M <integer>[k|K|m|M]] filesystem ... "
- "Warning:  (NO WRITE)\n"
- "pynfqM:"

```
