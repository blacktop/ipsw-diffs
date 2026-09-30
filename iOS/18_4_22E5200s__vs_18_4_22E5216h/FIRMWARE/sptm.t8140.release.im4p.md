## sptm.t8140.release.im4p

> `sptm.t8140.release.im4p`

```diff

-392.100.137.0.0
-  __TEXT.__cstring: 0xe447
+392.100.145.0.0
+  __TEXT.__cstring: 0xe522
   __TEXT.__binname: 0x40
   __TEXT.__const: 0xb00
   __TEXT.__chain_starts: 0x78
   __DATA_CONST.__const: 0x68c8
   __LATE_CONST.__late_const: 0x5d660
-  __TEXT_EXEC.__text: 0x5045c
+  __TEXT_EXEC.__text: 0x5078c
   __LAST.__pinst: 0x8
   __DATA.__auth_ptr: 0x18
   __DATA.__data: 0x6
   __DATA.__common: 0x5810
   __DATA.__bss: 0x5c20
   __BOOTDATA.__data: 0x14000
-  Functions: 353
+  Functions: 354
   Symbols:   1
-  CStrings:  1800
+  CStrings:  1809
 
CStrings:
+ "%s: Physical address %#llx is not page-aligned"
+ "VIOLATION_INVALID_PAPT_RANGE"
+ "base_addr"
+ "is_page_in_sapt_region"
+ "override_flags"
+ "override_mask"
+ "papt_to_phys(0) encountered."
+ "sptm_switch_root"
+ "uat_instance->ttbat_region.paddr"
+ "validate_papt_address_range"
- "uat_instance->ttbat_paddr"

```
