## exclave_sharedcache

> `Firmware/image4/exclavecore_bundle.t8150.RELEASE.restore.im4p/exclave_sharedcache`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_types2`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_entry`
- `__DATA.__TIGHTBEAM_VT`
- `__DATA.__TIGHTBEAM`
- `__DATA.__mod_init_func`
- `__DATA.__auth_ptr`
- `__DATA.__shared_cache`
- `__DATA.__got`
- `__DATA.__thread_vars`
- `__DATA.__bss`
- `__DATA.__common`
- `__PDATA.__auth_ptr`
- `__PDATA.__const`
- `__PDATA.__mod_init_func`
- `__PDATA.__data`
- `__PDATA.__shared_cache`
- `__PDATA.__common`

```diff

-1777.0.16.0.0
-  __TEXT.__text: 0x5e7b24
+1777.0.20.0.0
+  __TEXT.__text: 0x5e784c
   __TEXT.__lcxx_override: 0xe4
-  __TEXT.__cstring: 0x4f291
-  __TEXT.__const: 0x122134
+  __TEXT.__cstring: 0x4f381
+  __TEXT.__const: 0x1221a4
   __TEXT.__swift5_typeref: 0x14022
-  __TEXT.__swift5_reflstr: 0x11ef8
+  __TEXT.__swift5_reflstr: 0x11f68
   __TEXT.__swift5_assocty: 0x7a20
-  __TEXT.__swift5_fieldmd: 0x1bfc8
-  __TEXT.__constg_swiftt: 0x27e48
+  __TEXT.__swift5_fieldmd: 0x1c010
+  __TEXT.__constg_swiftt: 0x27e80
   __TEXT.__swift5_protos: 0x970
   __TEXT.__swift5_proto: 0x3cb4
   __TEXT.__swift5_types: 0x2474

   __TEXT.__swift5_builtin: 0x1590
   __TEXT.__swift5_capture: 0x1018
   __TEXT.__objc_methtype: 0xe1
-  __TEXT.__swift5_mpenum: 0x3cc
+  __TEXT.__swift5_mpenum: 0x39c
   __TEXT.__swift_as_entry: 0x994
   __TEXT.__swift_as_ret: 0xb08
   __TEXT.__swift_as_cont: 0x11f8

   __TEXT.__swift5_replace: 0x0
   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x0
-  __TEXT.__chain_fixups: 0xb8
-  __TEXT.__eh_frame: 0x34f10
+  __TEXT.__chain_fixups: 0xb0
+  __TEXT.__eh_frame: 0x35038
   __DATA.__TIGHTBEAM_VT: 0x8a0
   __DATA.__TIGHTBEAM: 0x238
-  __DATA.__const: 0x3d578
-  __DATA.__data: 0x186b0
+  __DATA.__const: 0x3d1f0
+  __DATA.__data: 0x186e8
   __DATA.__mod_init_func: 0x40
   __DATA.__ENDPOINTS: 0x1a221
   __DATA.__auth_ptr: 0x2338

   __PDATA.__data: 0x2af0
   __PDATA.__ENDPOINTS: 0x838
   __PDATA.__shared_cache: 0x70
-  __PDATA.__bss: 0xc4a8
+  __PDATA.__bss: 0xc4b8
   __PDATA.__common: 0x2578
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  Functions: 22927
+  Functions: 22941
   Symbols:   1
-  CStrings:  7283
+  CStrings:  7292
 
CStrings:
+ "1"
+ "OWNERINFO"
+ "Stop prox policy (reset)"
+ "[B] Stop prox policy (reset)"
+ "exbright_mot_enable"
+ "failed to shutdown host with exit code: %d"
+ "freed slot was not most recently allocated"
+ "integer value bound to non-value generic parameter"
+ "integer value where a type is required"
+ "policy-override-chill-pill"
+ "policy-override-chill-pill exceeds MOT, setting back to default to "
+ "yes"
- "[SCHED] Scheduling %s 0x%04hx (%zu/%zu)\n"
- "no fixup data for faultable range [%#lx, %#lx) found"
- "non-zero exit return: %d"
```
