## APFS

> `/System/Library/PrivateFrameworks/APFS.framework/APFS`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-3288.40.13.0.0
-  __TEXT.__text: 0x53fd8
+3288.40.14.0.0
+  __TEXT.__text: 0x540f4
   __TEXT.__const: 0x8540
   __TEXT.__cstring: 0xe88d
   __TEXT.__oslogstring: 0x11b8
Functions:
~ _spaceman_chunk_zone_info_init : 68 -> 84
~ _spaceman_iterate_process_bitmap_block : 1028 -> 1040
~ _spaceman_iterate_free_extents_internal : 3788 -> 3852
~ _spaceman_alloc_iterate_chunks : 3476 -> 3520
~ _spaceman_modify_bits : 3588 -> 3712
~ _jobj_validate_key_val : 572 -> 596
CStrings:
+ "3288.40.14"
- "3288.40.13"
```
