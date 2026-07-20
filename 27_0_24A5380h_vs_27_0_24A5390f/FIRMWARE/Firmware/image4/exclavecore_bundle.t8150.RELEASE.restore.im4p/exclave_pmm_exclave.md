## exclave_pmm_exclave

> `Firmware/image4/exclavecore_bundle.t8150.RELEASE.restore.im4p/exclave_pmm_exclave`

### Sections with Same Size but Changed Content

- `__TEXT.__eh_frame`
- `__DATA.__const`
- `__DATA.__data`
- `__DATA.__auth_ptr`
- `__DATA.__shared_cache`
- `__DATA.__mod_init_func`

```diff

-1490.0.5.0.0
-  __TEXT.__text: 0x4d054
-  __TEXT.__const: 0x1d160
-  __TEXT.__cstring: 0x11e26
+1490.0.20.0.0
+  __TEXT.__text: 0x4d00c
+  __TEXT.__const: 0x1d140
+  __TEXT.__cstring: 0x11dbd
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0
   __TEXT.__term_offsets: 0x0

   __DATA.__thread_vars: 0x0
   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x0
-  __DATA.__bss: 0x4edf8
+  __DATA.__bss: 0x4ee08
   __DATA.__common: 0x91b0
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
   __PDATA.__mod_init_func: 0x0
   __PDATA.__shared_cache: 0x0
-  Functions: 1212
+  Functions: 1211
   Symbols:   4
-  CStrings:  1514
+  CStrings:  1513
 
CStrings:
+ "OWNERINFO"
- "[xrt] liblibc_plat_cl4_entry:xrt__init_mapped_nonroot:default"
- "no fixup data for faultable range [%#lx, %#lx) found"
```
