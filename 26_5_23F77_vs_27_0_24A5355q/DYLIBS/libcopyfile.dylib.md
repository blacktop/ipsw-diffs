## libcopyfile.dylib

> `/usr/lib/system/libcopyfile.dylib`

```diff

-240.0.0.0.0
-  __TEXT.__text: 0x7670
-  __TEXT.__auth_stubs: 0x660
+257.0.0.0.0
+  __TEXT.__text: 0x7a34
   __TEXT.__const: 0x1c8
-  __TEXT.__cstring: 0x1a67
-  __TEXT.__unwind_info: 0xd8
-  __DATA_CONST.__got: 0x28
+  __TEXT.__cstring: 0x1bf1
+  __TEXT.__unwind_info: 0xf8
+  __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x3b0
-  __AUTH_CONST.__auth_got: 0x330
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0xe0
+  __AUTH_CONST.__auth_got: 0x318
   __DATA_DIRTY.__bss: 0x10
   - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libdispatch.dylib

   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: D6293DB7-8AA3-37A9-B4F7-11FC91985672
-  Functions: 37
-  Symbols:   188
-  CStrings:  192
+  UUID: C6A37537-FCD9-3962-A729-8C3AF3704D51
+  Functions: 41
+  Symbols:   193
+  CStrings:  202
 
Symbols:
+ _copyfile_set_dst_permissions
+ _copyfile_validate_dst
+ _open_dst_rsrc_fork
+ _open_src_rsrc_fork
+ _openat
- _chmod
- _chmodx_np
- _chown
- _snprintf
CStrings:
+ "%s:%d:%s() input block size: %zu output block size: %zu\n"
+ "%s:%d:%s() returning %d errno %d\n"
+ "%s:%d:%s() rounding up block size from fsize: %lld to multiple of %zu\n"
+ "%s:%d:%s() setting flags: 0x%x\n"
+ "..namedfork/rsrc"
+ "cannot open destination for permission elevation: %s: %m"
+ "destination file %s changed behind our feet: %m"
+ "error closing source rsrc file descriptor: %d: %m"
+ "fchmodx_np on destination readonly fd: %m"
+ "fstat failed on destination readonly fd: %s: %m"
+ "fstat failed on readonly fd during validation: %m"
+ "fstat failed on writable fd during validation: %m"
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
