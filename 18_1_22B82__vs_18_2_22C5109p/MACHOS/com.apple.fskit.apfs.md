## com.apple.fskit.apfs

> `/System/Library/ExtensionKit/Extensions/com.apple.fskit.apfs.appex/com.apple.fskit.apfs`

```diff

-2313.40.10.0.0
-  __TEXT.__text: 0x5f2d0
+2317.60.14.0.2
+  __TEXT.__text: 0x6004c
   __TEXT.__auth_stubs: 0xa80
   __TEXT.__objc_stubs: 0x460
-  __TEXT.__objc_methlist: 0x74
-  __TEXT.__cstring: 0x14a98
-  __TEXT.__const: 0x8080
+  __TEXT.__objc_methlist: 0x5c
+  __TEXT.__cstring: 0x14d9e
+  __TEXT.__const: 0x80a0
   __TEXT.__gcc_except_tab: 0x14
-  __TEXT.__oslogstring: 0xe8
+  __TEXT.__oslogstring: 0xd1
   __TEXT.__objc_classname: 0x9a
-  __TEXT.__objc_methname: 0x502
-  __TEXT.__objc_methtype: 0x207
-  __TEXT.__unwind_info: 0xa08
+  __TEXT.__objc_methname: 0x4d3
+  __TEXT.__objc_methtype: 0x1dc
+  __TEXT.__unwind_info: 0xa40
   __DATA_CONST.__auth_got: 0x550
   __DATA_CONST.__got: 0x70
   __DATA_CONST.__auth_ptr: 0x38

   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x4f0
-  __DATA.__objc_selrefs: 0x158
+  __DATA.__objc_selrefs: 0x148
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x390
   __DATA.__bss: 0xa9

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 1156
-  Symbols:   692
-  CStrings:  1914
+  Functions: 1176
+  Symbols:   703
+  CStrings:  1933
 
Symbols:
+ _apfs_kb_supports_class
+ _cp_dec_ref
+ _crypto_state_init
+ _fs_create_dstream
+ _fs_reset_dstream
+ _get_new_crypto_id
+ _get_vol_crypto
+ _ino_get_class_check
+ _ino_is_class_v
+ _xf_get_ptr_and_size
+ _xf_remove
CStrings:
+ "!((err == 0) && (*crypto_id == 0) && fs_is_content_protected(apfs))"
+ "!(ino->iflags & (JI_RAW_ENCRYPTED))"
+ "!(ino->iflags & JI_CRYPTO_STATE_RETAINED)"
+ "%!s(MISSING):%!d(MISSING): %!s(MISSING) %!s(MISSING): could not create dstream for obj-id %!l(MISSING)ld (name: %!s(MISSING))\n"
+ "%!s(MISSING):%!d(MISSING): %!s(MISSING) *** failed to fetch the dstream pointer for %!l(MISSING)ld (ret %!d(MISSING))\n"
+ "%!s(MISSING):%!d(MISSING): %!s(MISSING) *** failed to set dstream as an extended field of ino %!l(MISSING)ld (ret %!d(MISSING))\n"
+ "%!s(MISSING):%!d(MISSING): %!s(MISSING) danger - crypto id %!l(MISSING)ld had refcnt %!d(MISSING)\n"
+ "%!s(MISSING):%!d(MISSING): %!s(MISSING) failed to insert new dstream_id %!l(MISSING)lu (ret %!d(MISSING))"
+ "%!s(MISSING):%!d(MISSING): %!s(MISSING) was NOT able to update/decrement crypto state %!l(MISSING)ld, err = %!d(MISSING)\n"
+ "2317.60.14.0.2"
+ "@\"NSProgress\"40@0:8@\"FSTask\"16@\"NSArray\"24^@32"
+ "@40@0:8@16@24^@32"
+ "apfs.c"
+ "fs_create_dstream"
+ "fs_is_content_protected(apfs)"
+ "fs_reset_dstream"
+ "get_next_apfs_obj_ids"
+ "get_vol_crypto"
+ "get_vol_crypto(apfs) == VOL_CPROTECTED"
+ "get_vol_crypto(apfs) == VOL_PFKEY"
+ "icp_dec_ref"
+ "ino_get_class_check"
+ "ino_has_vnode(ino)"
+ "ino_poison_vnode(apfs, inode)"
+ "invalid crypto id"
+ "is_retainable_internal"
+ "startCheckWithTask:parameters:error:"
+ "startFormatWithTask:parameters:error:"
- "%!s(MISSING): Finished launching"
- "-[APFSFileSystem didFinishLaunching]"
- "-[APFSFileSystem didFinishLoading]"
- "2313.40.10"
- "checkWithParameters:connection:taskID:replyHandler:"
- "didFinishLoading"
- "formatWithParameters:connection:taskID:replyHandler:"
- "v48@0:8@\"NSArray\"16@\"FSMessageConnection\"24@\"NSUUID\"32@?<v@?@\"NSProgress\"@\"NSError\">40"
- "v48@0:8@16@24@32@?40"

```
