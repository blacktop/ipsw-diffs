## libcopyfile.dylib

> `/usr/lib/system/libcopyfile.dylib`

```diff

-240.0.0.0.0
-  __TEXT.__text: 0x7670 sha256:21156c1e70c2a7f879f7488027f0c1dc5d7a453ba16777edcda2a7fadf7dee8a
-  __TEXT.__auth_stubs: 0x660 sha256:7b5dd30d6bb0dea45a05a67f24009077dad78e0b261fe08669339b10dd1a41fa
-  __TEXT.__const: 0x1c8 sha256:632a014503931a20b8dd811b33ed85436e75dbc6c16287727388d5662c2fe087
-  __TEXT.__cstring: 0x1a67 sha256:c9015ad60a5426af31a52f54e0b3ee6675b4e1cf6a2d2543739f296f63aa37f3
-  __TEXT.__unwind_info: 0xd8 sha256:86928390466945c492a86789d8c85cee6b57e5e45fe612645b445426baed3674
-  __DATA_CONST.__got: 0x28 sha256:2c34ce1df23b838c5abf2a7f6437cca3d3067ed509ff25f11df6b11b582b51eb
-  __DATA_CONST.__const: 0x3b0 sha256:4376c3e83601f463a60b0a58fccba02e21c942081c465a877bccef895be378d9
-  __AUTH_CONST.__auth_got: 0x330 sha256:0645a4a67dcec462dc9f335bb0564e6e39bf12ea7e40cf8de81418210102c2d1
-  __AUTH_CONST.__const: 0xe0 sha256:9c5e56d7130e0d06e6a603055a4aa185474ccee2e352a55e6d65cc65e1ffc6ef
+257.0.0.0.0
+  __TEXT.__text: 0x7a34 sha256:e9ca8ff09bb82c9322fc644b2262db616305ebd1825659a23b97ee59d2456300
+  __TEXT.__const: 0x1c8 sha256:5db97f3feaff0604a6741364dd7dbb5f2717ed0815c33116cee5156461a5a02a
+  __TEXT.__cstring: 0x1bf1 sha256:9d9ab94edd7203a9ab6440a7aaa77f9c2a3651aa3c27d278832d0e12ea2b62f6
+  __TEXT.__unwind_info: 0xf8 sha256:825fa96a0998fbb4c5807ee22f9ab5b936f626084ebbd8059fd930a50d1ff1f0
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__const: 0x3b0 sha256:0d7c2ec5e38098c4a2f4393830ea6833a202c5172fe46aaaebf8dfdc5519ea0a
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0xe0 sha256:6bdb7cc5081c0d50c23e5cea221971adb919ec31202ff17c02d66c6f0f33a513
+  __AUTH_CONST.__auth_got: 0x318 sha256:52f033ec34066343ced3a1bed745100fe4efe6577154125a6d9483c6b482219a
   __DATA_DIRTY.__bss: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
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
