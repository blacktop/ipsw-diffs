## ktrace

> `/System/Library/PrivateFrameworks/ktrace.framework/ktrace`

```diff

-676.0.0.0.0
-  __TEXT.__text: 0xbfda4
+676.82.2.0.0
+  __TEXT.__text: 0xbfcf0
   __TEXT.__auth_stubs: 0x3490
   __TEXT.__objc_methlist: 0x3e0
   __TEXT.__const: 0x5a7a

   - /usr/lib/swift/libswift_DarwinFoundation2.dylib
   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: BD5321E4-4C3E-37F4-99F7-2C74268BFBD2
+  UUID: EA1CE1AE-EF9D-3D0D-BD52-34FCFAC5098B
   Functions: 3841
   Symbols:   6909
   CStrings:  1833
Functions:
~ _ktrace_merge_ioreg_service : 304 -> 288
~ __ZL24visit_inode_while_lockedP16operating_system4fsid8fsobj_id : 964 -> 948
~ __ZL18make_image_summary10_CSTypeRefb : 684 -> 668
~ _ktrace_symbolicator_get_description : 832 -> 816
~ __ZL8cfstringPKc : 96 -> 76
~ _ktrace_dsym_search_configuration_add_dstroot_path : 164 -> 148
~ _ktrace_dsym_search_configuration_add_recursive_search_path : 164 -> 148
~ _ktrace_dsym_search_configuration_copy_plist : 484 -> 468
~ ____ZL18make_image_summary10_CSTypeRefb_block_invoke : 452 -> 436
~ ____ZL13visit_processP16operating_systemj_block_invoke.194 : 564 -> 548
~ ____ZL33make_image_summary_with_dyld_infoP12dyld_image_sb_block_invoke : 344 -> 328

```
