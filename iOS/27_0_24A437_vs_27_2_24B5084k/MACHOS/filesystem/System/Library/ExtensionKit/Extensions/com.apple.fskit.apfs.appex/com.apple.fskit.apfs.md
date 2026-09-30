## com.apple.fskit.apfs

> `/System/Library/ExtensionKit/Extensions/com.apple.fskit.apfs.appex/com.apple.fskit.apfs`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__DATA_CONST.__const`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-3288.2.1.0.0
-  __TEXT.__text: 0xe414c
+3288.40.13.0.0
+  __TEXT.__text: 0xe4654
   __TEXT.__auth_stubs: 0x1050
   __TEXT.__objc_stubs: 0x1240
   __TEXT.__objc_methlist: 0x83c
   __TEXT.__const: 0x8bb0
-  __TEXT.__cstring: 0x3b8b3
+  __TEXT.__cstring: 0x3b898
   __TEXT.__objc_methname: 0x1eb1
   __TEXT.__oslogstring: 0x1dd3
   __TEXT.__objc_classname: 0x13d

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x30c0
+  __TEXT.__unwind_info: 0x30c8
   __DATA_CONST.__const: 0x1240
-  __DATA_CONST.__cfstring: 0x3a0
+  __DATA_CONST.__cfstring: 0x3c0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3287
+  Functions: 3286
   Symbols:   1567
-  CStrings:  5386
+  CStrings:  5387
 
Symbols:
+ _decrement_dstream_id_for_deletion
+ _fsck_repairs_count
- _decrement_dstream_id_for_deletion_ex
- _iteratively_remove_extents_of_file
CStrings:
+ "%s:%d: %s failed to remove extents iteratively\n"
+ "3288.40.13"
+ "BTOFF_IS_VALID(offsets[i].off)"
+ "The volume %s with UUID %s was found to have minor issues that can be repaired."
+ "decrement_dstream_id_for_deletion"
+ "dstream->alloced_size == 0"
+ "fsck_repairs_apply_cb"
+ "mount_apfs"
- "3288.2.1"
- "The volume %s with UUID %s could not be verified completely and can not be repaired."
- "decrement_dstream_id_for_deletion_ex"
- "fsck_repairs_apply"
- "offsets[i].off != BTOFF_INVALID && offsets[i].off != BTOFF_MT_GHOST"
- "offsets[i].off != BTOFF_MT_GHOST"
- "offsets[midpoint].off != BTOFF_MT_GHOST"
```
