## sptm.t8150.release.im4p

> `sptm.t8150.release.im4p`

```diff

-611.120.6.0.0
-  __TEXT.__cstring: 0x12318
+611.160.8.0.0
+  __TEXT.__cstring: 0x12429
   __TEXT.__const: 0xa80
   __TEXT.__binname: 0x40
   __TEXT.__chain_starts: 0x24
   __DATA_CONST.__const: 0x5c98
   __LATE_CONST.__late_const: 0x7c1f0
-  __TEXT_EXEC.__text: 0x5d55c
+  __TEXT_EXEC.__text: 0x5ef6c
   __LAST.__pinst: 0x8
   __DATA.__data: 0xf
   __DATA.__auth_ptr: 0x18
   __DATA.__bss: 0x60a8
   __DATA.__common: 0x8608
   __BOOTDATA.__data: 0x14000
-  UUID: B604FFBC-89E2-32A5-9E3F-FBAB25082E44
-  Functions: 386
+  UUID: 5967F76F-5229-3007-BA12-8A47EA8219E0
+  Functions: 392
   Symbols:   1
-  CStrings:  2300
+  CStrings:  2307
 
CStrings:
+ "%s: Nonrecoverable PIO error detected: vaddr: %p, value: 0x%016llx_%016llx, llc_err_sts:0x%llx, llc_err_adr:0x%llx, llc_err_inf:0x%llx"
+ "%s: bad idx"
+ "SPTM-611.160.8|2026-05-14:23:21:13.337295|"
+ "avoid-tlbi-in-map"
+ "pio_write_verify_llc_err_inf_nrec"
+ "sart_write_throttle_cfg"
+ "t8110dart_write_gapf_reg"
+ "t8110dart_write_smmu_reg"
- "SPTM-611.120.6|2026-04-18:15:30:21.251059|"

```
