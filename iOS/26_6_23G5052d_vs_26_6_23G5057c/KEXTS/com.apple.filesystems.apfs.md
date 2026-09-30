## com.apple.filesystems.apfs

> `com.apple.filesystems.apfs`

```diff

   __TEXT.__const: 0x9a8
-  __TEXT.__cstring: 0x4d4ae
-  __TEXT_EXEC.__text: 0x148330
+  __TEXT.__cstring: 0x4d93c
+  __TEXT_EXEC.__text: 0x148bdc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x70c
   __DATA.__bss: 0xd48
-  __DATA_CONST.__auth_got: 0x1180
+  __DATA_CONST.__auth_got: 0x11a0
   __DATA_CONST.__got: 0x198
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0x6720
-  __DATA_CONST.__kalloc_type: 0x5080
+  __DATA_CONST.__kalloc_type: 0x5000
   __DATA_CONST.__kalloc_var: 0x2990
   __DATA_CONST.__assert: 0x14
-  Functions: 2334
+  Functions: 2341
   Symbols:   0
-  CStrings:  6692
+  CStrings:  6717
 
Sections:
~ __TEXT.__const : content changed
~ __DATA.__data : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__assert : content changed
CStrings:
+ "%s:%d: %s checking for existing proposed vek\n"
+ "%s:%d: %s commit failed, err = %d (will retry on next boot)\n"
+ "%s:%d: %s commit succeeded\n"
+ "%s:%d: %s failed to allocate buffer for deferred commit\n"
+ "%s:%d: %s failed to clean-up proposed wvek record in nx keybag, err = %d\n"
+ "%s:%d: %s failed to commit proposed wvek record, err = 0x%x (%d more retries)\n"
+ "%s:%d: %s failed to enter tx to store proposed wvek record, err = %d\n"
+ "%s:%d: %s failed to enter tx to update wvek record, err = %d\n"
+ "%s:%d: %s failed to flush tx storing proposed wvek record in nx keybag, err = %d\n"
+ "%s:%d: %s failed to get vek blob state, err = 0x%x\n"
+ "%s:%d: %s failed to load volume class keys, error = %x\n"
+ "%s:%d: %s failed to look up vek, err = %d\n"
+ "%s:%d: %s failed to recover existing proposed vek, err = %d\n"
+ "%s:%d: %s failed to recover vek before first-unlock\n"
+ "%s:%d: %s failed to store proposed wvek record in nx keybag, err = %d\n"
+ "%s:%d: %s failed to unwrap vek, err = 0x%x\n"
+ "%s:%d: %s failed to update wvek record in nx keybag, err = %d\n"
+ "%s:%d: %s found existing proposed wvek record in nx keybag (from previous failure)\n"
+ "%s:%d: %s no commit pending\n"
+ "%s:%d: %s no existing proposed vek to recover\n"
+ "%s:%d: %s received migrated vek during unwrap\n"
+ "%s:%d: %s scheduled deferred commit\n"
+ "%s:%d: %s successfully loaded volume class keys\n"
+ "%s:%d: %s successfully recovered existing proposed vek\n"
+ "%s:%d: failed to lookup existing proposed wvek record in nx keybag, err = %d\n"
+ "11212221111111222222222211112222222222111222221111221122211112211222111122112221111221122211112211212212212222211111112222221112221111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111122222111112112111222222211111212222211212222222222222222222222222221222212222222222211222211221111111111122112212212222221122221212222222122222221222222222111111111111111122221121222222212212222221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221"
+ "2026/06/28"
+ "20:04:07"
+ "2811.160.7"
+ "Jun 28 2026"
+ "apfs-2811.160.7"
+ "apfs->apfs_vek.wvek == ((void*)0)"
+ "apfs->apfs_vek.wvek == wvek"
+ "apfs_vek_commit_cb"
+ "apfs_vek_commit_enter"
+ "apfs_vek_commit_internal"
+ "apfs_vek_unwrap"
+ "kb"
+ "wvek->data"
+ "wvek->len <= 512"
- "%s:%d: failed to add proposed wvek record in nx keybag, err = %d\n"
- "%s:%d: failed to clean-up proposed wvek record in nx keybag, err = %d\n"
- "%s:%d: failed to commit proposed wvek record, err = 0x%x (%d more retries)\n"
- "%s:%d: failed to get vek blob state, err = 0x%x\n"
- "%s:%d: failed to unwrap volume key, err = 0x%x\n"
- "%s:%d: failed to update wvek record in nx keybag, err = %d\n"
- "11212221111111222222222211112222222222111222221111221122211112211222111122112221111221122211112211212212212222211111112222221112221111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111122222111112112111222222211111212222222222222222222222222221222212222222222211222211221111111111122112212212222221122221212222222122222221222222222111111111111111122221121222222212212222221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221"
- "19:08:34"
- "2026/06/21"
- "2811.160.6"
- "Jun 21 2026"
- "apfs-2811.160.6"
- "apfs_commit_update_volume_key"
- "nx_keybag_lookup_vek"
- "site.struct aks_fv_data_s"

```
