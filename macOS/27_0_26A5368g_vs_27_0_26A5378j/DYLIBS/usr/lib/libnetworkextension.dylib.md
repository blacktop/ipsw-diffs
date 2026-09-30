## libnetworkextension.dylib

> `/usr/lib/libnetworkextension.dylib`

```diff

-  __TEXT.__text: 0x350bc
+  __TEXT.__text: 0x35da4
   __TEXT.__objc_methlist: 0x2ac
   __TEXT.__const: 0x26c
-  __TEXT.__cstring: 0x2ea6
-  __TEXT.__oslogstring: 0x810d
-  __TEXT.__unwind_info: 0x768
+  __TEXT.__cstring: 0x2ed9
+  __TEXT.__oslogstring: 0x8203
+  __TEXT.__unwind_info: 0x778
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1060
+  __DATA_CONST.__const: 0x1080
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x3a0
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__got: 0x1c0
-  __AUTH_CONST.__const: 0x11d0
+  __AUTH_CONST.__const: 0x11f0
   __AUTH_CONST.__cfstring: 0xb20
   __AUTH_CONST.__objc_const: 0x5d8
   __AUTH_CONST.__objc_intobj: 0x90

   __AUTH.__objc_data: 0x230
   __DATA.__objc_ivar: 0x2c
   __DATA.__data: 0x48
-  __DATA.__bss: 0xcd8
+  __DATA.__bss: 0xd10
   __DATA.__common: 0x3d
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x1b6

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 639
-  Symbols:   1585
-  CStrings:  1112
+  Functions: 645
+  Symbols:   1597
+  CStrings:  1119
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ ___ne_copy_cached_bundle_identifier_for_uuid_plist_locked_block_invoke
+ ___ne_copy_cached_bundle_identifier_for_uuid_plist_locked_block_invoke_2
+ ___ne_copy_cached_uuids_for_bundle_identifier_plist_locked_block_invoke
+ ___ne_copy_uuid_cache_plist_locked_block_invoke
+ ___ne_ensure_uuid_cache_mapped_locked_block_invoke
+ _g_uuid_cache_map
+ _ne_copy_uuid_cache_plist_locked
+ _ne_ensure_uuid_cache_mapped_locked
+ _ne_uuid_cache_bsearch_fwd
+ _ne_uuid_cache_bsearch_rev
+ _ne_uuid_cache_changed
+ ne_copy_uuid_cache_plist_locked.g_my_boot_session_uuid_plist
+ ne_copy_uuid_cache_plist_locked.g_my_os_version_plist
+ ne_copy_uuid_cache_plist_locked.once_token_plist
+ ne_ensure_uuid_cache_mapped_locked.g_my_boot_session_uuid
+ ne_ensure_uuid_cache_mapped_locked.g_my_os_version
+ ne_ensure_uuid_cache_mapped_locked.once_token
- ___ne_copy_cached_bundle_identifier_for_uuid_block_invoke
- ___ne_copy_cached_bundle_identifier_for_uuid_block_invoke_2
- ___ne_copy_cached_uuids_for_bundle_identifier_block_invoke
- ___ne_copy_uuid_cache_locked_block_invoke
- ne_copy_uuid_cache_locked.g_my_boot_session_uuid
- ne_copy_uuid_cache_locked.g_my_os_version
- ne_copy_uuid_cache_locked.once_token
CStrings:
+ "%s size invalid: %lu"
+ "Failed to mmap %s: [%d] %s"
+ "Invalid call to flow_director_handle_cfil_verdict."
+ "Not using UUID cache bin: OS version mismatch (%.*s vs %s)"
+ "Not using UUID cache bin: boot UUID mismatch"
+ "UUID cache bin sandbox check failed"
+ "UUID cache bin: size mismatch (header %u, file %lu)"
+ "UUID cache sandbox plist check failed"
- "UUID cache sandbox check failed"

```
