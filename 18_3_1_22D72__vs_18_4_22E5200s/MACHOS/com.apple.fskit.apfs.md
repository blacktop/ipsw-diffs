## com.apple.fskit.apfs

> `/System/Library/ExtensionKit/Extensions/com.apple.fskit.apfs.appex/com.apple.fskit.apfs`

```diff

-2317.82.1.0.0
-  __TEXT.__text: 0x60000
-  __TEXT.__auth_stubs: 0xa80
+2332.100.53.0.6
+  __TEXT.__text: 0x5f87c
+  __TEXT.__auth_stubs: 0xac0
   __TEXT.__objc_stubs: 0x460
-  __TEXT.__objc_methlist: 0x5c
-  __TEXT.__cstring: 0x14d99
-  __TEXT.__const: 0x80a0
+  __TEXT.__objc_methlist: 0x1d4
+  __TEXT.__cstring: 0x14e5e
+  __TEXT.__const: 0x8138
   __TEXT.__gcc_except_tab: 0x14
   __TEXT.__oslogstring: 0xd1
-  __TEXT.__objc_classname: 0x9a
-  __TEXT.__objc_methname: 0x4d3
-  __TEXT.__objc_methtype: 0x1dc
-  __TEXT.__unwind_info: 0xa40
-  __DATA_CONST.__auth_got: 0x550
+  __TEXT.__objc_classname: 0x59
+  __TEXT.__objc_methname: 0x4b6
+  __TEXT.__objc_methtype: 0x209
+  __TEXT.__unwind_info: 0xa08
+  __DATA_CONST.__auth_got: 0x570
   __DATA_CONST.__got: 0x70
-  __DATA_CONST.__auth_ptr: 0x38
-  __DATA_CONST.__const: 0x5f8
+  __DATA_CONST.__auth_ptr: 0x40
+  __DATA_CONST.__const: 0x600
   __DATA_CONST.__cfstring: 0x220
   __DATA_CONST.__objc_classlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x28
+  __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x4f0
-  __DATA.__objc_selrefs: 0x148
+  __DATA.__objc_const: 0x240
+  __DATA.__objc_selrefs: 0x1f0
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0x390
+  __DATA.__data: 0x2e0
   __DATA.__bss: 0xa9
   __DATA.__common: 0x430
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 1176
-  Symbols:   703
-  CStrings:  1933
+  Functions: 1189
+  Symbols:   712
+  CStrings:  1943
 
Symbols:
+ _apfs_reset_parent_nlink
+ _authapfs_digest
+ _ccsha3_256_di
+ _ccsha3_384_di
+ _ccsha3_512_di
+ _cp_to_ino_class
+ _io_container_is_external
+ _nx_unmount_internal
+ _objc_autorelease
+ _objc_release_x28
- _objc_release_x27
CStrings:
+ "!sm->sm_fxc[ss.dev] || !ss.fxc_need_scan_finish"
+ "%s:%d: Hit an error flushing the hint list, %d dev_name = %s\n"
+ "%s:%d: conflicting mount options: probe %d temporary %d sbindex %d\n"
+ "%s:%d: hinting %d blocks from hint_list failed w/: %d (entry %lld:%lld ; %lld:%lld)\n"
+ "2332.100.53.0.6"
+ "@\"NSProgress\"40@0:8@\"FSTask\"16@\"FSTaskOptions\"24^@32"
+ "SNAP_DELETE_TXN"
+ "addr < dev->dev_block_count"
+ "authapfs_digest"
+ "authapfs_digest.c"
+ "count <= (dev->dev_block_count - addr)"
+ "digest_size <= APFS_HASH_MAX_SIZE"
+ "fd_dev_hint"
+ "fd_dev_hint_flush"
+ "hint"
+ "sha3_256"
+ "sha3_256_4k"
+ "sha3_384"
+ "sha3_384_4k"
+ "sha3_512"
+ "sha3_512_4k"
+ "sm->sm_reserved_space[dev] <= sm->sm_phys->sm_dev[dev].sm_free_count"
+ "spaceman_alloc_iterate_chunks"
+ "startCheckWithTask:options:error:"
+ "startFormatWithTask:options:error:"
+ "v40@0:8@\"FSResource\"16@\"FSTaskOptions\"24@?<v@?@\"NSArray\"@\"NSError\">32"
+ "v40@0:8@\"FSResource\"16@\"FSTaskOptions\"24@?<v@?@\"NSError\">32"
- "!sm->sm_fxc[dev] || !fxc_need_scan_finish"
- "%s%s:%s%s%s%s%u:%s%u:%s cmd: %d, result: %d%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s purging %s%s\n"
- "%s:%d: %s sanity check of recently-changed structures failed: %d\n"
- "%s:%d: conflicting mount options: load from temporary checkpoint AND checkpoint descriptor index %d\n"
- "2317.82.1"
- "@\"NSProgress\"40@0:8@\"FSTask\"16@\"NSArray\"24^@32"
- "FSBlockDeviceOperations"
- "FSManageableResourceSimpleMaintenanceOps"
- "filevault_purge_group"
- "obj_cache_lock_by_state, invalid oc_lock_state %d\n"
- "obj_cache_unlock_by_state, invalid oc_lock_state %d\n"
- "setState:replyHandler:"
- "startCheckWithTask:parameters:error:"
- "startFormatWithTask:parameters:error:"
- "v32@0:8q16@?24"
- "v40@0:8@\"FSResource\"16@\"FSTaskOptionsBundle\"24@?<v@?@\"NSArray\"@\"NSError\">32"

```
