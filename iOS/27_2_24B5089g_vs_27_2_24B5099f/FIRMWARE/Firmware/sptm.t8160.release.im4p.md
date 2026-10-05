## sptm.t8160.release.im4p

> `Firmware/sptm.t8160.release.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__chain_starts`
- `__DATA_CONST.__const`
- `__DATA.__auth_ptr`

```diff

-820.40.20.0.0
-  __TEXT.__cstring: 0x16072
+820.40.23.0.0
+  __TEXT.__cstring: 0x1632c
   __TEXT.__const: 0xaa4
   __TEXT.__binname: 0x40
   __TEXT.__chain_starts: 0x14
   __DATA_CONST.__const: 0x7c00
-  __LATE_CONST.__late_const: 0x7c890
-  __TEXT_EXEC.__text: 0x6040c
+  __LATE_CONST.__late_const: 0x8c890
+  __TEXT_EXEC.__text: 0x61160
   __TEXT_EXEC.__exc: 0x2000
   __LAST.__pinst: 0xc
   __DATA.__data: 0xf
   __DATA.__auth_ptr: 0x18
   __DATA.__common: 0x9208
   __BOOTDATA.__data: 0x18000
-  Functions: 406
+  Functions: 408
   Symbols:   1
-  CStrings:  2586
+  CStrings:  2599
 
CStrings:
+ "%s: Failed to verify TLBI"
+ "%s: The GMMU TLBI verification register should be 8B-aligned"
+ "%s: UAT Dekker gate acquisition timed out after %llu ns (spun for %llu cycles)"
+ "%s: UAT Dekker lock acquisition timed out after %llu ns (spun for %llu cycles)"
+ "%s: dart %p (%s:%u): relaxed_rw_protections and allow_pte_remap are not supported together"
+ "%s: gmmu-tlbi-verification-bit (%llu) is unset or out of range [0, 63]"
+ "%s: verify-gmmu-tlbis-at-sync is enabled but gmmu-tlbi-verification-reg is not set"
+ "0x4B1D000000000003ULL"
+ "SPTM-820.40.23|2026-09-27:19:59:11.633384|"
+ "gmmu-tlbi-verification-bit"
+ "gmmu-tlbi-verification-reg"
+ "hib_header_copy->handoffPageCount < HIB_HANDOFF_PAGECOUNT_LIMIT"
+ "uat_dekker_gate_lock"
+ "uat_dekkerlock_lock"
+ "uat_sync_outer_tlb_sapt_flush"
+ "verify-gmmu-tlbis-at-sync"
- "0x4B1D000000000002ULL"
- "SPTM-820.40.20|2026-09-13:19:38:35.360456|"
- "wrprot"
```
