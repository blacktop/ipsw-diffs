## rsync.openrsync

> `/usr/libexec/rsync/rsync.openrsync`

```diff

-91.0.1.0.0
-  __TEXT.__text: 0x295e8
-  __TEXT.__auth_stubs: 0xb70
+91.0.3.0.0
+  __TEXT.__text: 0x296bc
+  __TEXT.__auth_stubs: 0xba0
   __TEXT.__const: 0x5678
-  __TEXT.__cstring: 0x677d
-  __TEXT.__unwind_info: 0x550
+  __TEXT.__cstring: 0x6768
+  __TEXT.__unwind_info: 0x548
   __TEXT.__eh_frame: 0x48
-  __DATA_CONST.__auth_got: 0x5b8
+  __DATA_CONST.__auth_got: 0x5d0
   __DATA_CONST.__got: 0x48
-  __DATA_CONST.__auth_ptr: 0x18
+  __DATA_CONST.__auth_ptr: 0x20
   __DATA_CONST.__const: 0x17a8
   __DATA.__data: 0x760
   __DATA.__bss: 0x788

   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libsbuf.dylib
   - /usr/lib/libutil.dylib
-  Functions: 630
-  Symbols:   207
-  CStrings:  1340
+  Functions: 625
+  Symbols:   210
+  CStrings:  1338
 
Symbols:
+ ___memcpy_chk
+ _printf
+ _puts
CStrings:
+ "%!s(MISSING): flist_normalize_path"
+ "%!s(MISSING): received file metadata: size %!j(MISSING)d, mtime %!j(MISSING)d, mode %!o(MISSING), rdev (%!d(MISSING), %!d(MISSING)), flag %!x(MISSING)"
+ "/./"
+ "rsync version 2.6.9 compatible"
- "%!s(MISSING): received file metadata: size %!j(MISSING)d, mtime %!j(MISSING)d, mode %!o(MISSING), rdev (%!d(MISSING), %!d(MISSING))"
- "S_ISDIR(wfl[0].st.mode)"
- "cargvs == 1"
- "flist_gen_local"
- "j == cargvs"
- "strcmp(wfl[i].wpath, \".\")"

```
