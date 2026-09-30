## libsystem_networkextension.dylib

> `/usr/lib/system/libsystem_networkextension.dylib`

```diff

-  __TEXT.__text: 0x15800
+  __TEXT.__text: 0x16628
   __TEXT.__const: 0x110
   __TEXT.__cstring: 0x19e7
-  __TEXT.__oslogstring: 0x2d9a
-  __TEXT.__unwind_info: 0x398
+  __TEXT.__oslogstring: 0x2e90
+  __TEXT.__unwind_info: 0x3c0
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0xcf0
+  __DATA_CONST.__const: 0xd10
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x1c0
+  __AUTH_CONST.__const: 0x1e0
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__data: 0x2c
-  __DATA.__bss: 0x618
-  __DATA_DIRTY.__data: 0xc
-  __DATA_DIRTY.__bss: 0x158
+  __DATA.__data: 0x28
+  __DATA.__bss: 0x668
+  __DATA_DIRTY.__data: 0x10
+  __DATA_DIRTY.__bss: 0x140
   __DATA_DIRTY.__common: 0x2
   - /usr/lib/system/libcommonCrypto.dylib
   - /usr/lib/system/libdispatch.dylib

   - /usr/lib/system/libsystem_sandbox.dylib
   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libxpc.dylib
-  Functions: 271
-  Symbols:   666
-  CStrings:  539
+  Functions: 277
+  Symbols:   684
+  CStrings:  545
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__cstring : content changed
Symbols:
+ ___ne_copy_cached_bundle_identifier_for_uuid_plist_locked_block_invoke
+ ___ne_copy_cached_bundle_identifier_for_uuid_plist_locked_block_invoke_2
+ ___ne_copy_cached_uuids_for_bundle_identifier_plist_locked_block_invoke
+ ___ne_copy_uuid_cache_plist_locked_block_invoke
+ ___ne_ensure_uuid_cache_mapped_locked_block_invoke
+ _g_uuid_cache_map
+ _ne_copy_uuid_cache_plist_locked
+ _ne_copy_uuid_cache_plist_locked.g_my_boot_session_uuid_plist
+ _ne_copy_uuid_cache_plist_locked.g_my_os_version_plist
+ _ne_copy_uuid_cache_plist_locked.once_token_plist
+ _ne_ensure_uuid_cache_mapped_locked
+ _ne_ensure_uuid_cache_mapped_locked.g_my_boot_session_uuid
+ _ne_ensure_uuid_cache_mapped_locked.g_my_os_version
+ _ne_ensure_uuid_cache_mapped_locked.once_token
+ _ne_uuid_cache_bsearch_fwd
+ _ne_uuid_cache_bsearch_rev
+ _ne_uuid_cache_changed
- ___ne_copy_cached_bundle_identifier_for_uuid_block_invoke
- ___ne_copy_cached_bundle_identifier_for_uuid_block_invoke_2
- ___ne_copy_cached_uuids_for_bundle_identifier_block_invoke
- ___ne_copy_uuid_cache_locked_block_invoke
- _ne_copy_uuid_cache_locked.g_my_boot_session_uuid
- _ne_copy_uuid_cache_locked.g_my_os_version
- _ne_copy_uuid_cache_locked.once_token
CStrings:
+ "%s size invalid: %lu"
+ "Failed to mmap %s: [%d] %s"
+ "Not using UUID cache bin: OS version mismatch (%.*s vs %s)"
+ "Not using UUID cache bin: boot UUID mismatch"
+ "UUID cache bin sandbox check failed"
+ "UUID cache bin: size mismatch (header %u, file %lu)"
+ "UUID cache sandbox plist check failed"
- "UUID cache sandbox check failed"

```
