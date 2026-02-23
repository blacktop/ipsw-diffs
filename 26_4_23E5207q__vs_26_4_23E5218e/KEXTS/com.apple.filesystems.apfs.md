## com.apple.filesystems.apfs

> `com.apple.filesystems.apfs`

```diff

-2811.100.177.0.1
+2811.100.184.0.1
   __TEXT.__const: 0x990
-  __TEXT.__cstring: 0x4d19c
-  __TEXT_EXEC.__text: 0x147b50
+  __TEXT.__cstring: 0x4d293
+  __TEXT_EXEC.__text: 0x147ca8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x70c
   __DATA.__bss: 0xd60

   __DATA_CONST.__kalloc_type: 0x5080
   __DATA_CONST.__kalloc_var: 0x2990
   __DATA_CONST.__assert: 0x14
-  UUID: 8F0238C5-5C1C-3991-8C1C-C5A33819D0A1
+  UUID: 0B770B5D-E71C-39FB-B849-FF6EB51E7F23
   Functions: 2332
   Symbols:   0
-  CStrings:  6675
+  CStrings:  6679
 
Functions:
~ sub_fffffe000a52dbb4 -> sub_fffffe000a507474 : 52 -> 216
~ __ZN19AppleAPFSUserClient11clientCloseEv : 532 -> 428
~ sub_fffffe000a566f48 -> sub_fffffe000a540844 : 760 -> 888
~ _apfs_setxattr_internal : 2704 -> 2860
CStrings:
+ "%s:%d: %s %s: unsetting SF_DATALESS bsd_flag on ino %llu (%s) old flags (0x%x) new flags (0x%x)\n"
+ "%s:%d: %s update ino %llu failed after %s SF_DATALESS, prev_bsd_flags 0x%x, inode_bsd_flags 0x%x, xattr '%s' size %llu, error %d\n"
+ "/Library/Caches/com.apple.xbs/3546AB46-573A-4157-9A3C-7323A5299E4A/TemporaryDirectory.uLOdqE/Sources/apfs/kext/apfs_vnops.c"
+ "/Library/Caches/com.apple.xbs/3546AB46-573A-4157-9A3C-7323A5299E4A/TemporaryDirectory.uLOdqE/Sources/apfs/nx/jobj.c"
+ "2026/02/17"
+ "21:36:24"
+ "21:36:25"
+ "2811.100.184.0.1"
+ "Feb 17 2026"
+ "apfs-2811.100.184.0.1"
+ "clientDied"
- "/Library/Caches/com.apple.xbs/B3E9A9A5-17CE-4785-B5AC-1460AC9D62AE/TemporaryDirectory.iMypLl/Sources/apfs/kext/apfs_vnops.c"
- "/Library/Caches/com.apple.xbs/B3E9A9A5-17CE-4785-B5AC-1460AC9D62AE/TemporaryDirectory.iMypLl/Sources/apfs/nx/jobj.c"
- "2026/02/04"
- "22:48:03"
- "2811.100.177.0.1"
- "Feb  4 2026"
- "apfs-2811.100.177.0.1"

```
