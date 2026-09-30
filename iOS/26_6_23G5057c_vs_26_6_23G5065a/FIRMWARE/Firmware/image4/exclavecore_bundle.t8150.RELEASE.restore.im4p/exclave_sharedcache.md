## exclave_sharedcache

> `Firmware/image4/exclavecore_bundle.t8150.RELEASE.restore.im4p/exclave_sharedcache`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift5_entry`
- `__DATA.__TIGHTBEAM_VT`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA.__mod_init_func`
- `__DATA.__auth_ptr`
- `__DATA.__shared_cache`
- `__DATA.__got`
- `__DATA.__thread_vars`
- `__DATA.__bss`
- `__DATA.__common`
- `__PDATA.__data`
- `__PDATA.__const`
- `__PDATA.__shared_cache`
- `__PDATA.__mod_init_func`
- `__PDATA.__auth_ptr`
- `__PDATA.__bss`
- `__PDATA.__common`

```diff

-  __TEXT.__text: 0x5d5be8
+  __TEXT.__text: 0x5d5f98
   __TEXT.__lcxx_override: 0x34c
-  __TEXT.__cstring: 0x48ed1
+  __TEXT.__cstring: 0x48ef1
   __TEXT.__const: 0x112ee4
   __TEXT.__swift5_typeref: 0x11e5a
   __TEXT.__swift5_reflstr: 0xf688

   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x0
   __TEXT.__chain_fixups: 0xa8
-  __TEXT.__eh_frame: 0x329b0
+  __TEXT.__eh_frame: 0x329d0
   __DATA.__TIGHTBEAM_VT: 0x600
   __DATA.__TIGHTBEAM: 0x190
   __DATA.__data: 0x14138

   __PDATA.__common: 0x2520
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  Functions: 23506
+  Functions: 23508
   Symbols:   1
-  CStrings:  6792
+  CStrings:  6793
 
CStrings:
+ "freed slot was not most recently allocated"
```
