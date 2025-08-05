## newfs_apfs

> `/System/Library/Filesystems/apfs.fs/newfs_apfs`

```diff

-2632.0.68.0.3
-  __TEXT.__text: 0x514fc
+2632.0.77.0.1
+  __TEXT.__text: 0x51960
   __TEXT.__auth_stubs: 0x8d0
-  __TEXT.__cstring: 0xfb95
+  __TEXT.__cstring: 0xfb56
   __TEXT.__const: 0x8380
   __TEXT.__unwind_info: 0x840
   __DATA_CONST.__auth_got: 0x468

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: 0308128F-CBED-33BA-B96A-1E4D5BC88DDF
-  Functions: 703
+  UUID: 57D3AB19-FDE9-398D-993E-E9DE1E8304AD
+  Functions: 704
   Symbols:   156
-  CStrings:  1343
+  CStrings:  1342
 
CStrings:
+ "%s:%d: %s %s: ENOSPC: ttype %s (r %lld d %lld tx %d) blocks %lld free %lld txn %lld # %d th %lld rr %lld sh %lld fq %lld lim %d %d freeup %d wait %d er %d\n"
+ "2632.0.77.0.1"
- "%s:%d: %s %s: ENOSPC: ttype %s (r %lld d %lld tx %d) blocks %lld free %lld txn %lld # %d th %lld rr %lld sh %lld fq %lld lim %d %d freeup %d wait %d\n"
- "%s:%d: %s unentitled reserve: reserved space underflow: %lld (%lld)\n"
- "2632.0.68.0.3"

```
