## libcopyfile.dylib

> `/usr/lib/system/libcopyfile.dylib`

```diff

-240.160.2.702.1
-  __TEXT.__text: 0x7cf8
+240.160.2.703.1
+  __TEXT.__text: 0x7d90
   __TEXT.__auth_stubs: 0x6e0
   __TEXT.__const: 0x1c8
-  __TEXT.__cstring: 0x1bee
-  __TEXT.__unwind_info: 0xe8
+  __TEXT.__cstring: 0x1c51
+  __TEXT.__unwind_info: 0xf0
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__const: 0x3b0
   __AUTH_CONST.__auth_got: 0x370

   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libxpc.dylib
-  Functions: 41
-  Symbols:   167
-  CStrings:  199
+  Functions: 43
+  Symbols:   169
+  CStrings:  203
 
Symbols:
+ _open_dst_rsrc_fork
+ _open_src_rsrc_fork
+ _openat
- _snprintf
CStrings:
+ "%s:%d:%s() input block size: %zu output block size: %zu\n"
+ "%s:%d:%s() returning %d errno %d\n"
+ "%s:%d:%s() rounding up block size from fsize: %lld to multiple of %zu\n"
+ "%s:%d:%s() setting flags: 0x%x\n"
+ "..namedfork/rsrc"
+ "error closing source rsrc file descriptor: %d: %m"
+ "open on %s resource fork: %d: %m"
+ "open/malloc/stat on %s resource fork: %d: %m"
+ "open_dst_rsrc_fork"
+ "open_src_rsrc_fork"
+ "unknown"
- "%s:%d:%s() input block size: %zu output block size: %zu\n\n"
- "%s:%d:%s() returning %d errno %d\n\n"
- "%s:%d:%s() rounding up block size from fsize: %lld to multiple of %zu\n\n"
- "%s:%d:%s() setting flags: %d\n"
- "/..namedfork/rsrc"
- "error closing source rsrc file descriptor: %m"
- "malloc/stat/open on %s: %m"
```
