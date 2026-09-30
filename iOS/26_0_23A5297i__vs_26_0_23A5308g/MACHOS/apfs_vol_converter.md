## apfs_vol_converter

> `/System/Library/Filesystems/apfs.fs/apfs_vol_converter`

```diff

-2632.0.68.0.3
-  __TEXT.__text: 0x581d0
+2632.0.77.0.1
+  __TEXT.__text: 0x587c8
   __TEXT.__auth_stubs: 0x9f0
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0x2c0
-  __TEXT.__cstring: 0x11b2a
-  __TEXT.__gcc_except_tab: 0x5cc
-  __TEXT.__unwind_info: 0xbb0
+  __TEXT.__cstring: 0x11be9
+  __TEXT.__gcc_except_tab: 0x604
+  __TEXT.__unwind_info: 0xbb8
   __DATA_CONST.__auth_got: 0x500
   __DATA_CONST.__got: 0x78
   __DATA_CONST.__auth_ptr: 0x20

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libutil.dylib
-  UUID: 33C14A33-5903-3AC8-8FFA-30ECE9E49349
-  Functions: 847
+  UUID: BFA366D1-F71E-31B5-8FC9-417BAEB8051B
+  Functions: 848
   Symbols:   184
-  CStrings:  1676
+  CStrings:  1678
 
CStrings:
+ "%s:%d: %s %s: ENOSPC: ttype %s (r %lld d %lld tx %d) blocks %lld free %lld txn %lld # %d th %lld rr %lld sh %lld fq %lld lim %d %d freeup %d wait %d er %d\n"
+ "%s:%u Dbg: apfs_crypto_io_enable returned EBUSY, retrying after delay. %u attempts left\n"
+ "%s:%u Dbg: nx_mount returned EPROTO, retrying after delay. %u attempts left\n"
+ "%s:%u Dbg: volume_make_multikey returned EBUSY, retrying after delay. %u attempts left\n"
+ "2632.0.77.0.1"
- "%s:%d: %s %s: ENOSPC: ttype %s (r %lld d %lld tx %d) blocks %lld free %lld txn %lld # %d th %lld rr %lld sh %lld fq %lld lim %d %d freeup %d wait %d\n"
- "%s:%d: %s unentitled reserve: reserved space underflow: %lld (%lld)\n"
- "2632.0.68.0.3"

```
