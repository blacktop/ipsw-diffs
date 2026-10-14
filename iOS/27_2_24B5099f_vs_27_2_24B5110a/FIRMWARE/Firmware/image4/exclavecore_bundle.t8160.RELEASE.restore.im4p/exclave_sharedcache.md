## exclave_sharedcache

> `Firmware/image4/exclavecore_bundle.t8160.RELEASE.restore.im4p/exclave_sharedcache`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_types2`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_entry`
- `__TEXT.__chain_fixups`
- `__TEXT.__eh_frame`
- `__DATA.__TIGHTBEAM_VT`
- `__DATA.__TIGHTBEAM`
- `__DATA.__mod_init_func`
- `__DATA.__auth_ptr`
- `__DATA.__shared_cache`
- `__DATA.__got`
- `__PDATA.__auth_ptr`
- `__PDATA.__const`
- `__PDATA.__data`

```diff

-1777.40.34.0.0
-  __TEXT.__text: 0x5fc7fc
+1777.40.37.0.0
+  __TEXT.__text: 0x5fcc54
   __TEXT.__lcxx_override: 0xd0
-  __TEXT.__cstring: 0x50e61
+  __TEXT.__cstring: 0x50f61
   __TEXT.__const: 0x124124
   __TEXT.__swift5_typeref: 0x1452c
-  __TEXT.__swift5_reflstr: 0x13508
+  __TEXT.__swift5_reflstr: 0x13528
   __TEXT.__swift5_assocty: 0x7d10
-  __TEXT.__swift5_fieldmd: 0x1cdf4
-  __TEXT.__constg_swiftt: 0x28aa8
+  __TEXT.__swift5_fieldmd: 0x1ce0c
+  __TEXT.__constg_swiftt: 0x28b08
   __TEXT.__swift5_protos: 0x998
   __TEXT.__swift5_proto: 0x3e98
   __TEXT.__swift5_types: 0x2524

   __TEXT.__eh_frame: 0x36060
   __DATA.__TIGHTBEAM_VT: 0x8a0
   __DATA.__TIGHTBEAM: 0x238
-  __DATA.__const: 0x3e798
-  __DATA.__data: 0x19150
+  __DATA.__const: 0x3e7a8
+  __DATA.__data: 0x191a0
   __DATA.__mod_init_func: 0x40
   __DATA.__ENDPOINTS: 0x1a84b
   __DATA.__auth_ptr: 0x2498

   __DATA_CONST.__mod_term_func: 0x0
   Functions: 657
   Symbols:   1
-  CStrings:  7436
+  CStrings:  7442
 
Functions:
~ sub_828053c : 288992 -> 290032
~ sub_859590c -> sub_8595d1c : 406796 -> 406868
CStrings:
+ "Start not allowed: camera disabled by EDT policy"
+ "Status not allowed: camera disabled by EDT policy"
+ "])\n  deviceStateDisplayWake: allowance="
+ "fpwm-frequency-hz"
+ "policy-sil-disable"
+ "sil-disable-config"
+ "sil-disable-offset"
- "])\n  medinaStateDisplayWake: allowance="
```
