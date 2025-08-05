## apfs_checkseal

> `/System/Library/Filesystems/apfs.fs/apfs_checkseal`

```diff

-2632.0.68.0.3
-  __TEXT.__text: 0x4ef08
+2632.0.77.0.1
+  __TEXT.__text: 0x4f34c
   __TEXT.__auth_stubs: 0x750
   __TEXT.__const: 0x510
-  __TEXT.__cstring: 0xff62
+  __TEXT.__cstring: 0xff23
   __TEXT.__unwind_info: 0x8b8
   __DATA_CONST.__auth_got: 0x3a8
   __DATA_CONST.__got: 0x50

   - /System/Library/PrivateFrameworks/AppleFSCompression.framework/AppleFSCompression
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: A49197E1-C394-34FE-9317-8BDFD64105C5
-  Functions: 722
+  UUID: FE2FAD6C-8612-3B91-BD47-67FE036BA5E8
+  Functions: 723
   Symbols:   131
-  CStrings:  1301
+  CStrings:  1300
 
CStrings:
+ "%s:%d: %s %s: ENOSPC: ttype %s (r %lld d %lld tx %d) blocks %lld free %lld txn %lld # %d th %lld rr %lld sh %lld fq %lld lim %d %d freeup %d wait %d er %d\n"
- "%s:%d: %s %s: ENOSPC: ttype %s (r %lld d %lld tx %d) blocks %lld free %lld txn %lld # %d th %lld rr %lld sh %lld fq %lld lim %d %d freeup %d wait %d\n"
- "%s:%d: %s unentitled reserve: reserved space underflow: %lld (%lld)\n"

```
