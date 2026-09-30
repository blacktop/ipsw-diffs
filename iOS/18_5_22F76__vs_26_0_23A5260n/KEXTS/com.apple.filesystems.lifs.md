## com.apple.filesystems.lifs

> `com.apple.filesystems.lifs`

```diff

-531.120.18.0.2
-  __TEXT.__os_log: 0x12f9
-  __TEXT.__cstring: 0x217f
+737.0.2.0.1
+  __TEXT.__os_log: 0x13b7
+  __TEXT.__cstring: 0x2203
   __TEXT.__const: 0x2c0
-  __TEXT_EXEC.__text: 0x1b14c
+  __TEXT_EXEC.__text: 0x1b9b8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x5d0
   __DATA.__common: 0x138
   __DATA.__bss: 0x90
-  __DATA_CONST.__auth_got: 0x7d0
+  __DATA_CONST.__auth_got: 0x7e8
   __DATA_CONST.__got: 0x80
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
-  __DATA_CONST.__const: 0x16a0
+  __DATA_CONST.__const: 0x16b8
   __DATA_CONST.__kalloc_type: 0xbc0
-  UUID: 42A35CBF-86AB-3A79-8ED6-3732A38C86A4
-  Functions: 401
+  __DATA_CONST.__kalloc_var: 0xf0
+  UUID: 8BF620AE-FA7C-319D-B712-0C32C851252F
+  Functions: 406
   Symbols:   0
-  CStrings:  393
+  CStrings:  402
 
CStrings:
+ "%s: Got block_size = 0. Using the device's block size instead."
+ "%s: failed to find request for op %u with id %llu"
+ "11112222222222222222"
+ "111222222222222222222222222222222222222222222222223322221222222222222222121111111112222222222222222122222221122"
+ "11211223222222222222"
+ "2222222222222222222222222222222222222222222222222222222222222222221111222111222211222222222222222222222222222222212121221122222"
+ "Failed to allocate fsids buffer."
+ "Failed to start unmount dangling thread, kern_return %d"
+ "Found %d dangling mount(s)."
+ "_O_f_preallocate"
+ "lifs_getattr"
+ "lifs_setup_mount_for_devvp"
+ "lifs_unmount_dangling"
+ "lifs_wait_for_device_idle"
+ "site.fsid_t"
- "%s: failed to find request with id %llu"
- "111122222"
- "11122222222222222222222222222222222222222222222222332222122222222222222121111111112222222222222222122222221122"
- "112112232"
- "2222222222222222222222222111122222222222222222222222222222111222211222222212122222222222222222222222221221122"
- "lifs_setup_mount_for_koio"

```
