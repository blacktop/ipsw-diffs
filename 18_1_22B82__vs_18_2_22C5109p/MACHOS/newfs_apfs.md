## newfs_apfs

> `/System/Library/Filesystems/apfs.fs/newfs_apfs`

```diff

-2313.40.10.0.0
-  __TEXT.__text: 0x50ab4
+2317.60.14.0.2
+  __TEXT.__text: 0x51bdc
   __TEXT.__auth_stubs: 0x7d0
-  __TEXT.__cstring: 0xf8e7
+  __TEXT.__cstring: 0xfd39
   __TEXT.__const: 0x7f40
-  __TEXT.__unwind_info: 0x840
+  __TEXT.__unwind_info: 0x890
   __DATA_CONST.__auth_got: 0x3e8
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__auth_ptr: 0x20

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  Functions: 695
+  Functions: 714
   Symbols:   140
-  CStrings:  1297
+  CStrings:  1324
 
CStrings:
+ "!((err == 0) && (*crypto_id == 0) && fs_is_content_protected(apfs))"
+ "!(ino->iflags & (JI_RAW_ENCRYPTED))"
+ "!apfs->apfs_readonly"
+ "%!s(MISSING):%!d(MISSING): %!s(MISSING) %!s(MISSING): could not create dstream for obj-id %!l(MISSING)ld (name: %!s(MISSING))\n"
+ "%!s(MISSING):%!d(MISSING): %!s(MISSING) *** failed to fetch the dstream pointer for %!l(MISSING)ld (ret %!d(MISSING))\n"
+ "%!s(MISSING):%!d(MISSING): %!s(MISSING) *** failed to set dstream as an extended field of ino %!l(MISSING)ld (ret %!d(MISSING))\n"
+ "%!s(MISSING):%!d(MISSING): %!s(MISSING) cannot insert new ep %!l(MISSING)lu because the policy cache is full\n"
+ "%!s(MISSING):%!d(MISSING): %!s(MISSING) crypto_obj_insert of new crypto_id %!l(MISSING)ld should not have failed (ret %!d(MISSING))\n"
+ "%!s(MISSING):%!d(MISSING): %!s(MISSING) danger - crypto id %!l(MISSING)ld had refcnt %!d(MISSING)\n"
+ "%!s(MISSING):%!d(MISSING): %!s(MISSING) failed to insert new dstream_id %!l(MISSING)lu (ret %!d(MISSING))"
+ "%!s(MISSING):%!d(MISSING): %!s(MISSING) invalid crypto object type %!u(MISSING)\n"
+ "%!s(MISSING):%!d(MISSING): %!s(MISSING) was NOT able to update/decrement crypto state %!l(MISSING)ld, err = %!d(MISSING)\n"
+ "((&crypto_cache->free_list)->tqh_first == ((void *)0))"
+ "2317.60.14.0.2"
+ "crypto object retain count %!d(MISSING) is not valid (crypto-id %!l(MISSING)ld, type %!u(MISSING) apfs %!p(MISSING))\n"
+ "crypto_hash_insert"
+ "crypto_obj_free"
+ "fs_create_dstream"
+ "fs_is_content_protected(apfs)"
+ "get_vol_crypto(apfs) == VOL_CPROTECTED"
+ "get_vol_crypto(apfs) == VOL_PFKEY"
+ "icp_dec_ref"
+ "icp_new_crypto"
+ "ino"
+ "ino_has_vnode(ino)"
+ "ino_poison_vnode(apfs, inode)"
+ "invalid crypto id"
+ "xid"
- "2313.40.10"

```
