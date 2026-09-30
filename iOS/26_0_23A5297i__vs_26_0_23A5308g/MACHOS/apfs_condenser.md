## apfs_condenser

> `/System/Library/Filesystems/apfs.fs/apfs_condenser`

```diff

-2632.0.68.0.3
-  __TEXT.__text: 0x4c234
+2632.0.77.0.1
+  __TEXT.__text: 0x4c6c8
   __TEXT.__auth_stubs: 0x780
-  __TEXT.__cstring: 0xf6c2
+  __TEXT.__cstring: 0xf683
   __TEXT.__const: 0x260
   __TEXT.__unwind_info: 0x7e8
   __DATA_CONST.__auth_got: 0x3c0

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: 6BF80240-AD87-34A6-8243-13905C008B0B
-  Functions: 659
+  UUID: E9C1C559-A4C7-30A8-BBAF-9E5CC4140840
+  Functions: 660
   Symbols:   134
-  CStrings:  1273
+  CStrings:  1272
 
CStrings:
+ "%s:%d: %s %s: ENOSPC: ttype %s (r %lld d %lld tx %d) blocks %lld free %lld txn %lld # %d th %lld rr %lld sh %lld fq %lld lim %d %d freeup %d wait %d er %d\n"
+ "2632.0.77.0.1"
- "%s:%d: %s %s: ENOSPC: ttype %s (r %lld d %lld tx %d) blocks %lld free %lld txn %lld # %d th %lld rr %lld sh %lld fq %lld lim %d %d freeup %d wait %d\n"
- "%s:%d: %s unentitled reserve: reserved space underflow: %lld (%lld)\n"
- "2632.0.68.0.3"

```
