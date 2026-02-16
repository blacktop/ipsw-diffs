## sptm.t8150.release.im4p

> `sptm.t8150.release.im4p`

```diff

-611.80.38.0.0
-  __TEXT.__cstring: 0x11a5c
+611.100.110.0.0
+  __TEXT.__cstring: 0x12302
   __TEXT.__const: 0xa00
   __TEXT.__binname: 0x40
   __TEXT.__chain_starts: 0x24
-  __DATA_CONST.__const: 0x73f0
-  __LATE_CONST.__late_const: 0x718c8
-  __TEXT_EXEC.__text: 0x5aa1c
+  __DATA_CONST.__const: 0x5c98
+  __LATE_CONST.__late_const: 0x7c1f0
+  __TEXT_EXEC.__text: 0x5d4d8
   __LAST.__pinst: 0x8
-  __DATA.__auth_ptr: 0x18
   __DATA.__data: 0xf
+  __DATA.__auth_ptr: 0x18
   __DATA.__bss: 0x60a8
-  __DATA.__common: 0x6208
+  __DATA.__common: 0x8608
   __BOOTDATA.__data: 0x14000
-  UUID: B0767037-8B0B-3BF2-8CAF-FA14FF90975B
-  Functions: 376
+  UUID: 292A4D09-85A0-3772-BC1B-C1CB85011090
+  Functions: 386
   Symbols:   1
-  CStrings:  2245
+  CStrings:  2299
 
CStrings:
+ "%s"
+ "%s\n"
+ "%s-data%s-base"
+ "%s-data%s-size"
+ "%s: %llu is not a valid dispatch id (valid dispatch IDs are 0 - %u)"
+ "%s: %s: No leaf table present for PAPT va %p"
+ "%s: %s: invalid papt returned by iommu_bootstrap_register_io_range"
+ "%s: %u is not a valid type ID (valid type IDs are 0 - %u)"
+ "%s: Child table FTE has not been acquired %p %u %d"
+ "%s: Execution Modes cannot be supported by more than one domain"
+ "%s: IOMMU %s (%d): %#llx length is greater than 64K pages (%zu)"
+ "%s: IOMMU %s (%d): Attempted to register an empty IO range %p %zu"
+ "%s: IOMMU %s (%d): Attempted to register managed page as an IO range %p %zu"
+ "%s: IOMMU %s (%d): Attempted to register unaligned IO range %p %zu"
+ "%s: IOMMU %s (%d): IO frame does not have a valid type for IO range %p %u"
+ "%s: IOMMU %s (%d): IO frame number of pages %llu does not match IO range number of pages %u"
+ "%s: IOMMU %s (%d): IO frame starting index %llu does not match IO range starting index %u"
+ "%s: IOMMU %s (%d): Non-refcounted frame found while attempting to modify refcnt %p %u"
+ "%s: IOMMU %s (%d): Number of IO ranges exhausted"
+ "%s: IOMMU %s (%d): State objects exhausted"
+ "%s: IOMMU %s (%d): Unexpected frame found while attempting to modify refcnt %p %u"
+ "%s: IOMMU %s (%d): attempted to increment refcnt of unexpected frame %p"
+ "%s: IOMMU %s (%d): attempted to release unexpected frame %p"
+ "%s: IOMMU %s (%d): attempted to request cache flush for non-generic frame %p %u"
+ "%s: IOMMU %s (%d): attempted to unregister illegal mapping"
+ "%s: IOMMU %s (%d): cache mode (%u) does not match with pmap-io-ranges (%u) for IO range %p %u"
+ "%s: IOMMU %s (%d): pmap-io-ranges does not exist for IO range %p %u"
+ "%s: Invalid Execution Mode permissions for type %d"
+ "%s: Invalid permissions found for the PAPT mapping (type_id = %d)"
+ "%s: Leaf page table FTE is somehow NULL even though prev_pte is valid"
+ "%s: Parent table FTE has not been acquired %p %u %d"
+ "%s: Synchronous external abort in early boot before XNU bootstrap. LLC_ERR_STS: %#llx, LLC_ERR_ADR: %#llx, LLC_ERR_INF: %#llx"
+ "%s: The %s data%s segment base(%#llx) is not page-aligned"
+ "%s: The %s data%s segment size(%#llx) is not a multiple of the page size"
+ "%s: Total size of pmap-io-ranges (%u) is not a multiple of pmap_io_range_t size (%zu)"
+ "%s: [%s] %s at pc 0x%016llx, lr 0x%016llx\n\t  x0:  0x%016llx x1:  0x%016llx  x2:  0x%016llx  x3:  0x%016llx\n\t  x4:  0x%016llx x5:  0x%016llx  x6:  0x%016llx  x7:  0x%016llx\n\t  x8:  0x%016llx x9:  0x%016llx  x10: 0x%016llx  x11: 0x%016llx\n\t  x12: 0x%016llx x13: 0x%016llx  x14: 0x%016llx  x15: 0x%016llx\n\t  x16: 0x%016llx x17: 0x%016llx  x18: 0x%016llx  x19: 0x%016llx\n\t  x20: 0x%016llx x21: 0x%016llx  x22: 0x%016llx  x23: 0x%016llx\n\t  x24: 0x%016llx x25: 0x%016llx  x26: 0x%016llx  x27: 0x%016llx\n\t  x28: 0x%016llx fp:  0x%016llx  lr:  0x%016llx  sp:  0x%016llx\n\t  pc:  0x%016llx cpsr: 0x%08x         esr: 0x%016llx          far: 0x%016llx\n"
+ "%s: [SPTM]: somehow a violation was triggered in early boot. That shouldn't be possible, %s: %s"
+ "%s: dart %p (%s:%u): %s: invalid papt returned by iommu_bootstrap_register_io_range"
+ "%s: init_get_image_region returned NULL for a non-optional region"
+ "%s: pmap-io-range %u has a length (0x%llx) that is not page-aligned. sig: %c%c%c%c, addr: 0x%llx, wimg: 0x%x"
+ "%s: pmap-io-range %u has an address (0x%llx) that is not page-aligned. sig: %c%c%c%c, len: 0x%llx, wimg: 0x%x"
+ "%s: pmap-io-range %u overlaps with managed physical memory. sig: %c%c%c%c, addr: 0x%llx, len: 0x%llx, wimg: 0x%x"
+ "%s: pmap-io-range %u wraps around. sig: %c%c%c%c, addr: 0x%llx, len: 0x%llx, wimg: 0x%x"
+ "(!cpylen && !cpylen) || (cpylen == ~((size_t)0)) || !((uintptr_t)src < (uintptr_t)dst + cpylen && (uintptr_t)dst < (uintptr_t)src + cpylen)"
+ "-shared-ro"
+ "-shared-rw"
+ "/Library/Caches/com.apple.xbs/4192B60F-4F03-4629-B5DD-E933AD1A96EB/TemporaryDirectory.AI0DHu/Sources/SPTM/sptm/boot/hib/hibernate_restore.c"
+ "/Library/Caches/com.apple.xbs/4192B60F-4F03-4629-B5DD-E933AD1A96EB/TemporaryDirectory.AI0DHu/Sources/SPTM/sptm/core/sptm_hibentry.c"
+ "/Library/Caches/com.apple.xbs/4192B60F-4F03-4629-B5DD-E933AD1A96EB/TemporaryDirectory.AI0DHu/Sources/SPTM/sptm/iommu/dart/t8110dart.c"
+ "0x4B1D000000000002ULL"
+ "1410"
+ "DISPATCH_ID_SPTM_CORE"
+ "EXEC_MODE_SPTM_DEFAULT"
+ "EXEC_MODE_TXM_DEFAULT"
+ "EXEC_MODE_XNU_DEFAULT"
+ "EXEC_MODE_XNU_ROZONE_RW"
+ "EXEC_MODE_XNU_USER_DEFAULT"
+ "EXEC_MODE_XNU_USER_JIT_RW"
+ "EXEC_MODE_XNU_USER_TPRO_RW"
+ "IOMMU_ID_CPUTRACE"
+ "IOMMU_ID_DART_GEN3"
+ "IOMMU_ID_DART_T6000"
+ "IOMMU_ID_DART_T8020"
+ "IOMMU_ID_DART_T8110"
+ "IOMMU_ID_NVME"
+ "IOMMU_ID_SART"
+ "IOMMU_ID_SHART"
+ "IOMMU_ID_UAT"
+ "IS_BIT_SET(header->kernelSlide, 63)"
+ "IS_BIT_SET(start_vaddr, 63)"
+ "SPTM"
+ "SPTM-611.100.110|2026-01-29:00:26:48.732123|"
+ "TXM"
+ "VIOLATION_ILLEGAL_IO_RANGE_SIZE"
+ "VIOLATION_ILLEGAL_PERMS"
+ "VIOLATION_ILLEGAL_SPTM_CALL_IN_PANIC"
+ "VIOLATION_ILLEGAL_UNCONDEMN"
+ "VIOLATION_INVALID_IO_FILTER_ENTRY"
+ "VIOLATION_NVME_ILLEGAL_SEG_COUNT"
+ "VIOLATION_NVME_INVALID_NLB"
+ "VIOLATION_UAT_ILLEGAL_MAP_FOUND_OCCUPIED_PTE"
+ "VIOLATION_UAT_ILLEGAL_UNMAP_FOUND_FREE_PTE"
+ "VIOLATION_UAT_INVALID_MICROPPL_MAGIC_VALUE"
+ "XNU"
+ "XNU_COPROCESSOR_RO_IO"
+ "XNU_USER_TPRO"
+ "[SPTM] Synchronous exception taken from guest before XNU bootstrap"
+ "__strlcpy_chk"
+ "dispatch_id_to_string"
+ "io_range"
+ "io_range->len"
+ "new_tte"
+ "populate_execution_modes"
+ "populate_overlay_indices"
+ "prev_perms"
+ "seg_cnt"
+ "sptm_drop_table_refcnts"
+ "sptm_early_platform_error"
+ "sptm_leaf_table_condemn_op"
+ "sptm_types.h"
+ "src/libc/string/strlcpy.c"
+ "table_acquire_if_present"
+ "template->NLB"
+ "uat_instance->handoff_region->micro_magic"
+ "width"
- "%s-data-base"
- "%s-data-size"
- "%s: %#llx length is greater than 64K pages (%zu)"
- "%s: %d is not a valid type ID (valid type IDs are 0-%d)"
- "%s: %s at pc 0x%016llx, lr 0x%016llx\n\t  x0:  0x%016llx x1:  0x%016llx  x2:  0x%016llx  x3:  0x%016llx\n\t  x4:  0x%016llx x5:  0x%016llx  x6:  0x%016llx  x7:  0x%016llx\n\t  x8:  0x%016llx x9:  0x%016llx  x10: 0x%016llx  x11: 0x%016llx\n\t  x12: 0x%016llx x13: 0x%016llx  x14: 0x%016llx  x15: 0x%016llx\n\t  x16: 0x%016llx x17: 0x%016llx  x18: 0x%016llx  x19: 0x%016llx\n\t  x20: 0x%016llx x21: 0x%016llx  x22: 0x%016llx  x23: 0x%016llx\n\t  x24: 0x%016llx x25: 0x%016llx  x26: 0x%016llx  x27: 0x%016llx\n\t  x28: 0x%016llx fp:  0x%016llx  lr:  0x%016llx  sp:  0x%016llx\n\t  pc:  0x%016llx cpsr: 0x%08x         esr: 0x%016llx          far: 0x%016llx\n"
- "%s: %u addr 0x%llx is not page-aligned"
- "%s: %u addr 0x%llx length 0x%llx wimg %#x overlaps managed physical memory"
- "%s: %u addr 0x%llx length 0x%llx wraps around"
- "%s: %u length 0x%llx is not page-aligned"
- "%s: Attempted to register an empty IO range %p %zu"
- "%s: Attempted to register managed page as an IO range %p %zu"
- "%s: Attempted to register unaligned IO range %p %zu"
- "%s: IO frame does not have a valid type for IO range %p %u"
- "%s: IO frame number of pages %llu does not match IO range number of pages %u"
- "%s: IO frame starting index %llu does not match IO range starting index %u"
- "%s: IOMMU %d attempted to increment refcnt of unexpected frame %p"
- "%s: IOMMU %s with ID %d attempted to request cache flush for non-generic frame %p %u"
- "%s: IOMMU %s with id %d attempted to release unexpected frame %p"
- "%s: IOMMU %s with id %d attempted to unregister illegal mapping"
- "%s: Invalid microPPL magic value found in the handoff region. Expected: 0x%llx, Actual: 0x%llx"
- "%s: Invalid pinning action %d"
- "%s: NLB (0x%x) doesn't match seg count (0x%x)"
- "%s: Non-refcounted frame found while attempting to modify refcnt (IOMMU %u) %p %u"
- "%s: SPRR index is invalid"
- "%s: State objects exhausted for IOMMU %s with ID %d"
- "%s: The %s data segment base(%#llx) is not page-aligned"
- "%s: The %s data segment size(%#llx) is not a multiple of the page size"
- "%s: Unexpected frame found while attempting to modify refcnt (IOMMU %u) %p %u"
- "%s: [SPTM]: somehow a violation was triggered in early boot. That shouldn't be possible. %u"
- "%s: assert '!__builtin_add_overflow(frame_vaddr, SPTM_PAGE_SIZE, &frame_end)' failed."
- "%s: assert 'region_start' failed."
- "%s: cache mode (%u) does not match with pmap-io-ranges (%u) for IO range %p %u"
- "%s: dart %p (%s:%u): Invalid level %d"
- "%s: found io_range %p, but the size is not page size"
- "%s: no matching pmap-io-filters entry found"
- "%s: pmap-io-ranges does not exist for IO range %p %u"
- "%s: seg_cnt %x is too small for unaligned PRP1"
- "(header->kernelSlide & SET_BIT(63))"
- "(start_vaddr & SET_BIT(63))"
- "/Library/Caches/com.apple.xbs/Sources/SPTM/sptm/boot/hib/hibernate_restore.c"
- "/Library/Caches/com.apple.xbs/Sources/SPTM/sptm/core/sptm_hibentry.c"
- "/Library/Caches/com.apple.xbs/Sources/SPTM/sptm/iommu/dart/t8110dart.c"
- "1365"
- "SPTM-611.80.38|2026-01-21:21:50:31.695462|"
- "VIOLATION_ILLEGAL_SPRR_INDEX"
- "VIOLATION_UAT_ILLEGAL_PTE"
- "cur_level"
- "new_sprr_index"
- "prev_sprr_index"
- "pte_set_sprr_perms"
- "table_pa"

```
