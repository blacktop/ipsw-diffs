## com.apple.fskit.apfs

> `/System/Library/ExtensionKit/Extensions/com.apple.fskit.apfs.appex/com.apple.fskit.apfs`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-3288.40.13.0.0
-  __TEXT.__text: 0xe4654
+3288.40.14.0.0
+  __TEXT.__text: 0xe4748
   __TEXT.__auth_stubs: 0x1050
   __TEXT.__objc_stubs: 0x1240
   __TEXT.__objc_methlist: 0x83c
   __TEXT.__const: 0x8bb0
-  __TEXT.__cstring: 0x3b898
+  __TEXT.__cstring: 0x3b87a
   __TEXT.__objc_methname: 0x1eb1
   __TEXT.__oslogstring: 0x1dd3
   __TEXT.__objc_classname: 0x13d
Functions:
~ _spaceman_chunk_zone_info_init : 68 -> 84
~ _spaceman_create : 2580 -> 2588
~ sub_100022078 -> sub_100022090 : 1044 -> 1056
~ _spaceman_iterate_free_extents_internal : 3932 -> 3952
~ sub_100025318 -> sub_100025350 : 3588 -> 3632
~ sub_10002611c -> sub_100026180 : 3600 -> 3720
~ _jobj_validate_key_val : 572 -> 596
CStrings:
+ "3288.40.14"
+ "CI_COUNT(chunk_info->ci_free_count) >= bcount"
- "3288.40.13"
- "CI_COUNT(chunk_info->ci_free_count) == CI_COUNT(chunk_info->ci_block_count)"
```
