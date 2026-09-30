## libsystem_networkextension.dylib

> `/usr/lib/system/libsystem_networkextension.dylib`

```diff

-  __TEXT.__text: 0x14be0
-  __TEXT.__const: 0x100
+  __TEXT.__text: 0x15a0c
+  __TEXT.__const: 0x110
   __TEXT.__cstring: 0x1873
-  __TEXT.__oslogstring: 0x2910
-  __TEXT.__unwind_info: 0x378
+  __TEXT.__oslogstring: 0x2a06
+  __TEXT.__unwind_info: 0x398
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0x6a8
+  __DATA_CONST.__const: 0x6c8
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x830
+  __AUTH_CONST.__const: 0x850
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__data: 0x29
-  __DATA.__bss: 0x608
-  __DATA_DIRTY.__data: 0xc
-  __DATA_DIRTY.__bss: 0xf0
+  __DATA.__data: 0x25
+  __DATA.__bss: 0x658
+  __DATA_DIRTY.__data: 0x10
+  __DATA_DIRTY.__bss: 0xd8
   __DATA_DIRTY.__common: 0x2
   - /usr/lib/system/libcommonCrypto.dylib
   - /usr/lib/system/libdispatch.dylib

   - /usr/lib/system/libsystem_sandbox.dylib
   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libxpc.dylib
-  Functions: 273
-  Symbols:   561
-  CStrings:  514
+  Functions: 279
+  Symbols:   573
+  CStrings:  520
 
Sections:
~ __TEXT.__cstring : content changed
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
+ "Not using UUID cache bin: OS version mismatch (%.*s vs %s)"
+ "Not using UUID cache bin: boot UUID mismatch"
+ "UUID cache bin sandbox check failed"
+ "UUID cache bin: size mismatch (header %u, file %lu)"
+ "UUID cache sandbox plist check failed"
- "UUID cache sandbox check failed"

```
