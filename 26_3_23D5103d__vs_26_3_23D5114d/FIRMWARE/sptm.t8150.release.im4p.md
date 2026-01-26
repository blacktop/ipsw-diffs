## sptm.t8150.release.im4p

> `sptm.t8150.release.im4p`

```diff

-611.80.35.0.0
-  __TEXT.__cstring: 0x117a3
+611.80.38.0.0
+  __TEXT.__cstring: 0x11a5c
   __TEXT.__const: 0xa00
   __TEXT.__binname: 0x40
   __TEXT.__chain_starts: 0x24
-  __DATA_CONST.__const: 0x73e0
+  __DATA_CONST.__const: 0x73f0
   __LATE_CONST.__late_const: 0x718c8
-  __TEXT_EXEC.__text: 0x59ee4
+  __TEXT_EXEC.__text: 0x5aa1c
   __LAST.__pinst: 0x8
   __DATA.__auth_ptr: 0x18
   __DATA.__data: 0xf
   __DATA.__bss: 0x60a8
   __DATA.__common: 0x6208
   __BOOTDATA.__data: 0x14000
-  UUID: 0401F7CC-45B6-30BE-B9C2-8F7A8FC8D756
-  Functions: 375
+  UUID: 747DE2EA-69A0-320B-B53C-828250661A32
+  Functions: 376
   Symbols:   1
-  CStrings:  2226
+  CStrings:  2245
 
CStrings:
+ "%s: dart %p (%s:%u): PTE remap from carveout is present but remap itself isn't allowed"
+ "%s: dart %s:%s:%d: Failed to clear WR_DIS bit"
+ "%s: dart %s:%s:%d: Failed to set WR_DIS bit"
+ "%s: dart %s:%s:%d: Invalid ps wr_dis id"
+ "%s: dart %s:%s:%d: ps refcount overflow"
+ "%s: dart %s:%s:%d: ps refcount underflow"
+ "%s: dart %s:%s:%d: unexpected size for 'dart-ps-wr-dis-entries'"
+ "(&ps_wr_dis_lock)"
+ "PSWRDIS"
+ "SPTM-611.80.38|2026-01-21:00:54:46.155189|"
+ "VIOLATION_T8110_DART_PS_WR_DIS_RACE"
+ "clock-protection-dart-state"
+ "clock-protection-wr-dis-id"
+ "dart-ps-wr-dis-entries"
+ "dart_ps_wr_dis_map"
+ "pte-remap-carveout-only"
+ "t8110dart_bootstrap_ps_wr_dis_instance_properties"
+ "t8110dart_ps_wr_dis_decrement_refcount"
+ "t8110dart_ps_wr_dis_increment_refcount"
+ "t8110dart_set_ps_wr_dis"
- "SPTM-611.80.35|2025-12-20:15:51:08.815688|"

```
