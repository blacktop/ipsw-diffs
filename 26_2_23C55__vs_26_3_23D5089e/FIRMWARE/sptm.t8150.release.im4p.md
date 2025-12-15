## sptm.t8150.release.im4p

> `sptm.t8150.release.im4p`

```diff

-611.60.3.0.0
-  __TEXT.__cstring: 0x114e7
+611.80.31.0.0
+  __TEXT.__cstring: 0x11705
   __TEXT.__const: 0xa00
   __TEXT.__binname: 0x40
   __TEXT.__chain_starts: 0x24
   __DATA_CONST.__const: 0x73e0
   __LATE_CONST.__late_const: 0x718c8
-  __TEXT_EXEC.__text: 0x5931c
+  __TEXT_EXEC.__text: 0x59aa8
   __LAST.__pinst: 0x8
   __DATA.__auth_ptr: 0x18
   __DATA.__data: 0xf
   __DATA.__bss: 0x60a8
   __DATA.__common: 0x6208
   __BOOTDATA.__data: 0x14000
-  UUID: 580C70DC-64D4-3651-8495-541E5293F86A
+  UUID: E6165125-3162-37FF-AEDF-153907F20B11
   Functions: 375
   Symbols:   1
-  CStrings:  2205
+  CStrings:  2222
 
Functions:
~ sub_fffffff0270ac6ac : 1032 -> 728
~ sub_fffffff0270bd070 -> sub_fffffff0270bcf40 : 372 -> 1220
~ sub_fffffff0270c2b8c -> sub_fffffff0270c2dac : 4372 -> 4836
~ sub_fffffff0270c3ec0 -> sub_fffffff0270c42b0 : 1892 -> 2096
~ sub_fffffff0270c8084 -> sub_fffffff0270c8540 : 15084 -> 15784
~ sub_fffffff0270d0288 -> sub_fffffff0270d0a00 : 292 -> 408
~ sub_fffffff0270e2998 -> sub_fffffff0270e3184 : 2564 -> 2468
~ sub_fffffff0270ed2d8 -> sub_fffffff0270eda64 : 72 -> 76
CStrings:
+ "%s: /chosen/lock-regs not found (your iBoot or EDT may be too old)"
+ "%s: dart %p (%s:%u): Invalid 'piogw_ps_protection' size (%d)"
+ "%s: dart %p (%s:%u): Invalid PIOGW instance %u"
+ "%s: dart %p (%s:%u): Invalid PIOGW slice (%d) or address (%#llx)"
+ "PIOGW"
+ "SPTM-611.80.31|2025-12-04:22:40:29.400392|"
+ "ctrr_dt_get_force_flush_offset"
+ "ctrr_dt_get_memcache_enable_status"
+ "ctrr_dt_get_uint64"
+ "ctrr_set_mc_hint_in_cpm"
+ "early-memcache-enable"
+ "force-flush-offset"
+ "mc-hint-cpm-impl-mask"
+ "mc-hint-cpm-impl-offset"
+ "mc-hint-cpm-impl-val"
+ "piogw-ps-protection"
+ "state->piogws[instance].register_base"
+ "t8110dart_bootstrap_piogw_instance_properties"
+ "t8110dart_read_piogw_reg"
+ "t8110dart_write_piogw_reg"
- "%s: Only CPU pages may need a GPU TLBI on retype"
- "SPTM-611.60.3|2025-11-12:20:49:58.866563|"
- "perform_gmmu_tlbi_if_needed"

```
