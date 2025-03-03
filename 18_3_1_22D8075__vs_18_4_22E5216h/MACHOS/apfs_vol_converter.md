## apfs_vol_converter

> `/System/Library/Filesystems/apfs.fs/apfs_vol_converter`

```diff

-2317.82.1.0.0
-  __TEXT.__text: 0x573bc
-  __TEXT.__auth_stubs: 0x980
+2332.100.75.502.1
+  __TEXT.__text: 0x57260
+  __TEXT.__auth_stubs: 0x9e0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__cstring: 0x11824
-  __TEXT.__const: 0x238
-  __TEXT.__gcc_except_tab: 0x56c
-  __TEXT.__unwind_info: 0xbc8
-  __DATA_CONST.__auth_got: 0x4c8
+  __TEXT.__cstring: 0x11896
+  __TEXT.__const: 0x2c0
+  __TEXT.__gcc_except_tab: 0x570
+  __TEXT.__unwind_info: 0xb98
+  __DATA_CONST.__auth_got: 0x4f8
   __DATA_CONST.__got: 0x78
-  __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0xa60
+  __DATA_CONST.__auth_ptr: 0x20
+  __DATA_CONST.__const: 0xa68
   __DATA_CONST.__cfstring: 0xb00
-  __DATA.__data: 0x368
+  __DATA.__data: 0x378
   __DATA.__bss: 0x64
   __DATA.__common: 0xf84
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libutil.dylib
-  Functions: 848
-  Symbols:   177
-  CStrings:  1575
+  Functions: 837
+  Symbols:   183
+  CStrings:  1577
 
Symbols:
+ _cc_clear
+ _ccdigest_init
+ _ccdigest_update
+ _ccsha3_256_di
+ _ccsha3_384_di
+ _ccsha3_512_di
CStrings:
+ "!((apfs)->apfs_main_apfs != ((void*)0))"
+ "%s:%d: Hit an error flushing the hint list, %d dev_name = %s\n"
+ "%s:%d: conflicting mount options: probe %d temporary %d sbindex %d\n"
+ "%s:%d: hinting %d blocks from hint_list failed w/: %d (entry %lld:%lld ; %lld:%lld)\n"
+ "2332.100.75.502.1"
+ "SNAP_DELETE_TXN"
+ "fd_dev_hint_flush"
+ "spaceman_alloc_iterate_chunks"
- "!((apfs)->apfs_main_apfs != ((void *)0))"
- "%s:%d: %s sanity check of recently-changed structures failed: %d\n"
- "%s:%d: conflicting mount options: load from temporary checkpoint AND checkpoint descriptor index %d\n"
- "-"
- "2317.82.1"
- "no"

```
