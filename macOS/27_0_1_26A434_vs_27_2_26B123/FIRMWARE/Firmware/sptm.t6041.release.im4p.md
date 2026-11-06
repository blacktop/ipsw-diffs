## sptm.t6041.release.im4p

> `Firmware/sptm.t6041.release.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__chain_starts`
- `__DATA.__auth_ptr`

```diff

-820.0.22.0.0
-  __TEXT.__cstring: 0x15790
+820.40.24.0.0
+  __TEXT.__cstring: 0x15c64
   __TEXT.__const: 0xa74
   __TEXT.__binname: 0x40
   __TEXT.__chain_starts: 0x14
-  __DATA_CONST.__const: 0x7bf0
-  __LATE_CONST.__late_const: 0x7c9b0
-  __TEXT_EXEC.__text: 0x5f074
+  __DATA_CONST.__const: 0x7c00
+  __LATE_CONST.__late_const: 0x8c9b0
+  __TEXT_EXEC.__text: 0x603c0
   __TEXT_EXEC.__exc: 0x2000
   __LAST.__pinst: 0xc
   __DATA.__data: 0xf

   __DATA.__bss: 0x60a8
   __DATA.__common: 0x17088
   __BOOTDATA.__data: 0x18000
-  Functions: 398
+  Functions: 401
   Symbols:   1
-  CStrings:  2527
+  CStrings:  2553
 
CStrings:
+ "%s(%s:%d) - fte(%p), new_type(%s), page_flags(%u), read_refcnt(%d) iommu_read_refcnt(%u)\n"
+ "%s: %s: iommu_read_refcnt (0x%hhx) > read_refcnt(0x%x) for FTE %p"
+ "%s: Failed to verify TLBI"
+ "%s: The GMMU TLBI verification register should be 8B-aligned"
+ "%s: UAT Dekker gate acquisition timed out after %llu ns (spun for %llu cycles)"
+ "%s: UAT Dekker lock acquisition timed out after %llu ns (spun for %llu cycles)"
+ "%s: dart %p (%s:%u): Inconsistent unganged clock protection configuration"
+ "%s: dart %p (%s:%u): relaxed_rw_protections and allow_pte_remap are not supported together"
+ "%s: gmmu-tlbi-verification-bit (%llu) is unset or out of range [0, 63]"
+ "%s: unexpected size %u for property '%s'"
+ "%s: verify-gmmu-tlbis-at-sync is enabled but gmmu-tlbi-verification-reg is not set"
+ "(&dart_gapf_ungang_map[state->gapf_ungang_map_index].lock)"
+ "/chosen/manifest-properties"
+ "0x4B1D000000000003ULL"
+ "SPTM-820.40.24|2026-10-07:21:08:19.808229|"
+ "VIOLATION_NVME_ILLEGAL_HIBERNATION_QUEUE_LATCH"
+ "VIOLATION_T8110_DART_UNGANG_GAPF_RACE"
+ "enforce_no_hib_latch"
+ "gmmu-tlbi-verification-bit"
+ "gmmu-tlbi-verification-reg"
+ "hib_header_copy->handoffPageCount < HIB_HANDOFF_PAGECOUNT_LIMIT"
+ "internal-use-only-unit"
+ "iuos"
+ "sptm_allow_vm_isa_internal_guests"
+ "sptm_is_iuou_or_iuos_device"
+ "sptm_t8110dart_skip_disable_clock_protection_write"
+ "uat_dekker_gate_lock"
+ "uat_dekkerlock_lock"
+ "uat_sync_outer_tlb_sapt_flush"
+ "verify-gmmu-tlbis-at-sync"
- "%s(%s:%d) - fte(%p), new_type(%s), page_flags(%u), read_refcnt(%d)\n"
- "0x4B1D000000000002ULL"
- "SPTM-820.0.22|2026-08-08:13:06:06.975686|"
- "wrprot"
```
