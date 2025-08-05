## APFS

> `/System/Library/PrivateFrameworks/APFS.framework/APFS`

```diff

-2632.0.68.0.3
-  __TEXT.__text: 0x500c0
+2632.0.77.0.1
+  __TEXT.__text: 0x50518
   __TEXT.__auth_stubs: 0xb60
   __TEXT.__const: 0x8410
-  __TEXT.__cstring: 0xdde8
+  __TEXT.__cstring: 0xdda3
   __TEXT.__oslogstring: 0xb0e
   __TEXT.__gcc_except_tab: 0x18
   __TEXT.__unwind_info: 0x918

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libutil.dylib
-  UUID: 3140C128-5875-3D95-8D08-A648700C550D
-  Functions: 807
-  Symbols:   1760
-  CStrings:  1443
+  UUID: 597D1798-9BE2-3A6C-9056-74219E0AB037
+  Functions: 808
+  Symbols:   1762
+  CStrings:  1442
 
Symbols:
+ _spaceman_entitled_reserve_active
Functions:
+ _spaceman_ip_bm_block_address
~ _spaceman_currently_available_space : 304 -> 312
~ _spaceman_available_space : 272 -> 416
~ _spaceman_info : 620 -> 700
~ _spaceman_alloc : 5276 -> 5304
~ _spaceman_check_available_space : 768 -> 852
~ _spaceman_modify_bits : 3504 -> 3544
~ _spaceman_free_handle_entitled_reserve : 164 -> 264
~ _spaceman_reserve : 596 -> 608
~ _spaceman_unreserve : 848 -> 736
~ _obj_write_prepare : 1576 -> 1612
~ _obj_release : 976 -> 984
~ _obj_cache_remove : 628 -> 884
~ _obj_cache_remove_reverted_fs_objects : 860 -> 1032
~ _obj_cache_remove_new_fs_objects : 584 -> 792
~ _obj_create_internal : 1812 -> 1800
CStrings:
+ "2632.0.77.0.1"
- "%s:%d: %s unentitled reserve: reserved space underflow: %lld (%lld)\n"
- "2632.0.68.0.3"

```
