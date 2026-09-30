## com.apple.filesystems.apfs

> `com.apple.filesystems.apfs`

```diff

-2811.120.5.0.0
-  __TEXT.__const: 0x990
-  __TEXT.__cstring: 0x4d27e
-  __TEXT_EXEC.__text: 0x147ca8
+2811.120.10.0.1
+  __TEXT.__const: 0x9a8
+  __TEXT.__cstring: 0x4d4b8
+  __TEXT_EXEC.__text: 0x148314
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x70c
-  __DATA.__bss: 0xd60
-  __DATA_CONST.__auth_got: 0x1170
+  __DATA.__bss: 0xd48
+  __DATA_CONST.__auth_got: 0x1178
   __DATA_CONST.__got: 0x198
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x10

   __DATA_CONST.__kalloc_type: 0x5080
   __DATA_CONST.__kalloc_var: 0x2990
   __DATA_CONST.__assert: 0x14
-  UUID: E04F44FD-50E8-377E-AAE1-46190E2C2DA1
-  Functions: 2332
+  UUID: 6CB1DF37-5465-3156-B2A3-0D6097F5B61D
+  Functions: 2334
   Symbols:   0
-  CStrings:  6678
+  CStrings:  6692
 
CStrings:
+ "%s:%d: %s caching volume key is only supported on the boot container\n"
+ "%s:%d: %s caching volume key not supported in TDM\n"
+ "%s:%d: %s failed to alloc context for volume key, error = %d\n"
+ "%s:%d: %s failed to cache volume key, error = %d\n"
+ "%s:%d: %s failed to unwrap volume key, error = %d\n"
+ "%s:%d: %s only SEP-wrapped volume keys may be cached\n"
+ "%s:%d: Volume role 0x%x is not allowed on this container"
+ "2026/04/05"
+ "21:36:20"
+ "2811.120.10.0.1"
+ "Apr  5 2026"
+ "aks_fv_unwrap_vek"
+ "apfs-2811.120.10.0.1"
+ "borrowed->key == cpx_key(vek)"
+ "com.apple.private.apfs.volume-cache-key"
+ "fv_unwrap_vek"
+ "len <= cpx_max_key_len(vek)"
+ "options & apfs_fv_options_secret_is_acm"
+ "unwrap_and_cache_vek"
+ "volumeCacheKey"
- "%s:%d: Volume role 0x%x is not supported"
- "18:33:59"
- "2026/03/20"
- "2811.120.5"
- "Mar 20 2026"
- "apfs-2811.120.5"

```
