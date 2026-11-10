## sptm.t8152.release.im4p

> `Firmware/sptm.t8152.release.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__chain_starts`
- `__DATA.__auth_ptr`

```diff

-820.0.22.0.0
-  __TEXT.__cstring: 0x14de7
+820.40.24.0.0
+  __TEXT.__cstring: 0x151dd
   __TEXT.__const: 0xa4c
   __TEXT.__binname: 0x40
   __TEXT.__chain_starts: 0x14
-  __DATA_CONST.__const: 0x7bf0
-  __LATE_CONST.__late_const: 0x7c940
-  __TEXT_EXEC.__text: 0x5b8f4
+  __DATA_CONST.__const: 0x7bf8
+  __LATE_CONST.__late_const: 0x8c950
+  __TEXT_EXEC.__text: 0x5c8b8
   __TEXT_EXEC.__exc: 0x2000
   __LAST.__pinst: 0xc
   __DATA.__data: 0xf

   __DATA.__bss: 0x60a8
   __DATA.__common: 0x12388
   __BOOTDATA.__data: 0x18000
-  Functions: 392
+  Functions: 395
   Symbols:   1
-  CStrings:  2470
+  CStrings:  2492
 
CStrings:
+ "%s(%s:%d) - fte(%p), new_type(%s), page_flags(%u), read_refcnt(%d) iommu_read_refcnt(%u)\n"
+ "%s: %s: iommu_read_refcnt (0x%hhx) > read_refcnt(0x%x) for FTE %p"
+ "%s: Failed to verify TLBI"
+ "%s: The GMMU TLBI verification register should be 8B-aligned"
+ "%s: UAT Dekker gate acquisition timed out after %llu ns (spun for %llu cycles)"
+ "%s: UAT Dekker lock acquisition timed out after %llu ns (spun for %llu cycles)"
+ "%s: dart %p (%s:%u): relaxed_rw_protections and allow_pte_remap are not supported together"
+ "%s: gmmu-tlbi-verification-bit (%llu) is unset or out of range [0, 63]"
+ "%s: unexpected size %u for property '%s'"
+ "%s: verify-gmmu-tlbis-at-sync is enabled but gmmu-tlbi-verification-reg is not set"
+ "/chosen/manifest-properties"
+ "0x4B1D000000000003ULL"
+ "SPTM-820.40.24|2026-10-07:21:08:19.808229|"
+ "VIOLATION_NVME_ILLEGAL_HIBERNATION_QUEUE_LATCH"
+ "enforce_no_hib_latch"
+ "gmmu-tlbi-verification-bit"
+ "gmmu-tlbi-verification-reg"
+ "hib_header_copy->handoffPageCount < HIB_HANDOFF_PAGECOUNT_LIMIT"
+ "internal-use-only-unit"
+ "iuos"
+ "sptm_allow_vm_isa_internal_guests"
+ "sptm_is_iuou_or_iuos_device"
+ "uat_dekker_gate_lock"
+ "uat_dekkerlock_lock"
+ "uat_sync_outer_tlb_sapt_flush"
+ "verify-gmmu-tlbis-at-sync"
- "%s(%s:%d) - fte(%p), new_type(%s), page_flags(%u), read_refcnt(%d)\n"
- "0x4B1D000000000002ULL"
- "SPTM-820.0.22|2026-08-08:13:06:06.975686|"
- "wrprot"
```
