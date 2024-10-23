## rsync.openrsync

> `/usr/libexec/rsync/rsync.openrsync`

```diff

-91.40.3.0.0
-  __TEXT.__text: 0x40990
-  __TEXT.__auth_stubs: 0xc00
-  __TEXT.__const: 0x56d8
-  __TEXT.__cstring: 0x67c1
-  __TEXT.__oslogstring: 0x28bb
-  __TEXT.__unwind_info: 0x598
+91.60.3.0.0
+  __TEXT.__text: 0x42860
+  __TEXT.__auth_stubs: 0xc40
+  __TEXT.__const: 0x56e8
+  __TEXT.__cstring: 0x68e9
+  __TEXT.__oslogstring: 0x28fd
+  __TEXT.__unwind_info: 0x5b8
   __TEXT.__eh_frame: 0x48
-  __DATA_CONST.__auth_got: 0x600
+  __DATA_CONST.__auth_got: 0x620
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__auth_ptr: 0x20
   __DATA_CONST.__const: 0x17c8
   __DATA.__data: 0x760
-  __DATA.__bss: 0x788
-  __DATA.__common: 0x28
+  __DATA.__bss: 0x7a0
+  __DATA.__common: 0x100
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libsbuf.dylib
   - /usr/lib/libutil.dylib
-  Functions: 1015
-  Symbols:   216
-  CStrings:  1765
+  Functions: 1039
+  Symbols:   220
+  CStrings:  1779
 
Symbols:
+ _raise
+ _setpgid
+ _siglongjmp
+ _sigsetjmp
CStrings:
+ "%!s(MISSING): file truncated while hashing"
+ "%!s(MISSING): file truncated while reading"
+ "extern.h"
+ "fmap.c"
+ "fmap_close"
+ "fmap_sigbus_handler"
+ "fmap_trapped != fm && fmap_trapped_prev != fm"
+ "fmap_trapped == NULL || fmap_trapped_prev == NULL"
+ "fmap_trapped == fm"
+ "fmap_untrap"
+ "hash.c"
+ "p->map != NULL"
+ "p->state != DOWNLOAD_FLUSH_REMOTE"
+ "p->state == DOWNLOAD_READ_REMOTE || p->state == DOWNLOAD_FLUSH_REMOTE"
+ "setpgid"
+ "sig == SIGBUS"
+ "up->stat.map != NULL"
+ "up.stat.map == NULL"
- "download_cleanup"
- "p->map != MAP_FAILED"
- "p->mapsz"
- "p->state == DOWNLOAD_READ_REMOTE"
- "up->stat.map != MAP_FAILED"
- "up.stat.map == MAP_FAILED"

```
