## exclave_scheduler

> `exclave_scheduler`

```diff

-839.100.252.0.1
-  __TEXT.__text: 0x2f9548
+839.100.267.502.1
+  __TEXT.__text: 0x2fb078
   __TEXT.__lcxx_override: 0x200
-  __TEXT.__cstring: 0x1e7f0
-  __TEXT.__const: 0xd23ce
-  __TEXT.__constg_swiftt: 0xa528
-  __TEXT.__swift5_typeref: 0x5b2c
+  __TEXT.__cstring: 0x201e0
+  __TEXT.__const: 0xd7e9e
+  __TEXT.__constg_swiftt: 0xa4c8
+  __TEXT.__swift5_typeref: 0x5b20
   __TEXT.__swift5_builtin: 0xa8c
   __TEXT.__swift5_reflstr: 0x2441
-  __TEXT.__swift5_fieldmd: 0x60ec
+  __TEXT.__swift5_fieldmd: 0x609c
   __TEXT.__swift5_assocty: 0x48e8
   __TEXT.__swift5_proto: 0x14a8
-  __TEXT.__swift5_types: 0x8fc
+  __TEXT.__swift5_types: 0x8f4
   __TEXT.__swift5_protos: 0x228
   __TEXT.__swift5_types2: 0x8
   __TEXT.__swift5_mpenum: 0xe8

   __DATA.__got: 0x8
   __DATA.__auth_ptr: 0x50
   __DATA.__mod_init_func: 0x48
-  __DATA.__const: 0x193b8
+  __DATA.__const: 0x19358
   __DATA.__objc_imageinfo: 0x8
   __DATA.__ENDPOINTS: 0xc54
   __DATA.__data: 0x46a8

   __DATA.__mod_term_func: 0x0
   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x38
-  __DATA.__bss: 0x49460
-  __DATA.__common: 0x1edc
+  __DATA.__bss: 0x49470
+  __DATA.__common: 0x1efc
   __PDATA.__shared_cache: 0x0
   __PDATA.__mod_init_func: 0x0
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  Functions: 11421
+  Functions: 11456
   Symbols:   24
-  CStrings:  3777
+  CStrings:  3891
 
CStrings:
+ "!_operation_span_tree_remove(opdata, span_b)"
+ "!rl->rl_active"
+ "!vas->mapping_siptable"
+ "!vas_core_operation_refresh_pftes(&opdata, vas, cur_saddr, len_left, VAS_PFTE_REFILL)"
+ "!vas_core_operation_start(&opdata, vas, 0, 0, 1, 0, 0, 0)"
+ "!vas_core_operation_start(&opdata, vas, saddr, len, 0, 0, 0, 1)"
+ "!vas_core_operation_start(opdata, vas, saddr, len, 0, 0, 0, 0)"
+ "(rl)->rl_active"
+ "/AppleInternal/Library/BuildRoots/e3acf947-f363-11ef-bc4c-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.4.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
+ "A >= B || C >= D"
+ "BAMUM LETTER PHASE-A MAEMGBIEE"
+ "CUNEIFORM SIGN KALAM"
+ "EGYPTIAN HIEROGLYPH-"
+ "MENDE KIKAKUI SYLLABLE M172 MBO"
+ "MENDE KIKAKUI SYLLABLE M174 MBOO"
+ "WARNING: destroying a span that still has spanmap contents (type %u). The PMM won't be informed of these slots' deletion.\n"
+ "[VAS abort in function %s at line %d] Couldn't find span %p in %p's fault table\n"
+ "[VAS abort in function %s at line %d] [%s] destroying span after failed prepopulate\n"
+ "[VAS abort in function %s at line %d] [%s] merging free spans %p and %p should not fail\n"
+ "[VAS abort in function %s at line %d] [%s] spanmap_merge failed\n"
+ "[VAS abort in function %s at line %d] [%s] split of a free span must never fail\n"
+ "[VAS abort in function %s at line %d] [true: %llx %s %llx]%#zx requested > %#zx max\n"
+ "[VAS abort in function %s at line %d] [true: %llx %s %llx]Ended up with wrong start address\n"
+ "[VAS abort in function %s at line %d] [true: %llx %s %llx]Spans not in address order\n"
+ "[VAS abort in function %s at line %d] [true: %llx %s %llx]cn %p (%#lx): slot %#lx's idx %#lx too big\n"
+ "[VAS abort in function %s at line %d] [true: %llx %s %llx]empty rangelock\n"
+ "[VAS abort in function %s at line %d] [true: %llx %s %llx]faulttables: %#zx requested > %#zx max\n"
+ "[VAS abort in function %s at line %d] [true: %llx %s %llx]getting fault table from empty opdata %p\n"
+ "[VAS abort in function %s at line %d] [true: %llx %s %llx]getting pagefault hashtable from empty opdata %p\n"
+ "[VAS abort in function %s at line %d] [true: %llx %s %llx]getting pagefault tblentry from empty opdata %p\n"
+ "[VAS abort in function %s at line %d] [true: %llx %s %llx]getting segmentinfo from empty opdata %p\n"
+ "[VAS abort in function %s at line %d] [true: %llx %s %llx]getting span from empty opdata %p\n"
+ "[VAS abort in function %s at line %d] [true: %llx %s %llx]must split span into two pieces\n"
+ "[VAS abort in function %s at line %d] [true: %llx %s %llx]not initialized to match usage\n"
+ "[VAS abort in function %s at line %d] [true: %llx %s %llx]opdata %p fault table count is crazy\n"
+ "[VAS abort in function %s at line %d] [true: %llx %s %llx]opdata %p pagefault hashtable count is crazy\n"
+ "[VAS abort in function %s at line %d] [true: %llx %s %llx]opdata %p pagefault tblentry count is crazy\n"
+ "[VAS abort in function %s at line %d] [true: %llx %s %llx]opdata %p segmentinfo count is crazy\n"
+ "[VAS abort in function %s at line %d] [true: %llx %s %llx]opdata %p span count is crazy\n"
+ "[VAS abort in function %s at line %d] [true: %llx %s %llx]segments: %#zx requested > %#zx max\n"
+ "[VAS abort in function %s at line %d] [true: %lx %s %lx]Corrupted state of rl->vas\n\n"
+ "[VAS abort in function %s at line %d] [true: %lx %s %lx]mismatched VAS pointer\n"
+ "[VAS abort in function %s at line %d] [true: %lx %s %lx]opdata %p faulttables not emptied\n"
+ "[VAS abort in function %s at line %d] [true: %lx %s %lx]opdata %p pgfault_hashtables not emptied\n"
+ "[VAS abort in function %s at line %d] [true: %lx %s %lx]opdata %p pgfault_tblentries not emptied\n"
+ "[VAS abort in function %s at line %d] [true: %lx %s %lx]opdata %p segmentinfos not emptied\n"
+ "[VAS abort in function %s at line %d] [true: %lx %s %lx]opdata %p spans not emptied\n"
+ "[VAS abort in function %s at line %d] [true: %lx %s %lx]opdata not set up\n"
+ "[VAS abort in function %s at line %d] [true: %lx %s %lx]opdata not vas %p's active operation\n"
+ "[VAS abort in function %s at line %d] [true: %lx %s %lx]page %p in vas %p raced to get mapped\n"
+ "[VAS abort in function %s at line %d] [true: %lx %s %lx]rangelock not initialized for vas\n"
+ "[VAS abort in function %s at line %d] [true: %lx %s %lx]siptable %p mapspan set\n"
+ "[VAS abort in function %s at line %d] [true: %lx %s %lx]we assume the first span is the passed in span\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] Unable to start operation to initialize vas %p\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] added a new segmentinfo, but no space\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] empty operation starts should always succeed\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] failed but has merged span\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] failed to allocate fault entries\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] fault_done called on inactive faulthandler\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] grabbed vas %p vas_lock, but active operation %p listed\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] opdata %p returning NULL fault table\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] opdata %p returning NULL pagefault hashtable\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] opdata %p returning NULL pagefault tblentry\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] opdata %p returning NULL segmentinfo\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] opdata %p returning NULL span\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] rangelock %p not active\n\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] rangelock already active\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] ranges must not be empty\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] rl %p active at destruction\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] rounded up len must be non-zero\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] segmentinfo table already set up\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] should not have to grow multiple times\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] spans %p and %p must be free\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] spans %p must be free\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] split of %p at %#zx failed but least one non-NULL span %p %p\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] split of %p at %#zx succeeded but at least one NULL span %p %p\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] success but nos merged span\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] unable to preallocate fault resources\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] vas %p mapping_siptable cleared\n"
+ "[VAS abort in function %s at line %d] rangelock %p not active in vas %p\n"
+ "__span_alloc_operation"
+ "_alloc_frame_locked"
+ "_is_allocated(span)"
+ "_is_allocated(span_a) || _is_allocated(span_b)"
+ "_objret == NULL"
+ "_span_destroy_operation"
+ "_span_merge_free_operation"
+ "_span_merge_operation"
+ "_span_operation_cleanup"
+ "_span_operation_do_return_segmentinfo"
+ "_span_operation_get_segmentinfo"
+ "_span_operation_get_span"
+ "_span_operation_return_span"
+ "_span_split_free_operation"
+ "added"
+ "address_range_overlaps"
+ "cnd_wait(&rl->rl_cnd, &vas->vas_lock)"
+ "first_span != NULL || second_span != NULL"
+ "first_span == NULL || second_span == NULL"
+ "grew"
+ "len == 0"
+ "mtx_init(&process_table.segmentinfo_table_lock, mtx_plain)"
+ "mtx_init(&result->spanmap_lock, mtx_plain)"
+ "mtx_lock(&psit->segmentinfo_table_lock)"
+ "mtx_lock(&result->spanmap_lock)"
+ "mtx_lock(&second_span->spanmap_lock)"
+ "mtx_lock(&span_b->spanmap_lock)"
+ "mtx_lock(&vas->vas_lock)"
+ "mtx_unlock(&psit->segmentinfo_table_lock)"
+ "mtx_unlock(&result->spanmap_lock)"
+ "mtx_unlock(&second_span->spanmap_lock)"
+ "mtx_unlock(&span_b->spanmap_lock)"
+ "mtx_unlock(&vas->vas_lock)"
+ "rl->rl_active"
+ "vas->span_active_operation != NULL"
+ "vas_core_fault_table_remove_locked"
+ "vas_core_fault_table_split"
+ "vas_core_operation_finish"
+ "vas_core_operation_get_faulttable"
+ "vas_core_operation_get_pfht"
+ "vas_core_operation_get_pfte"
+ "vas_core_operation_lock"
+ "vas_core_operation_lock_rangelock"
+ "vas_core_operation_refresh_pftes"
+ "vas_core_operation_return_faulttable"
+ "vas_core_operation_return_pfht"
+ "vas_core_operation_return_pfte"
+ "vas_core_operation_setup_and_prealloc"
+ "vas_core_operation_start_empty"
+ "vas_core_rangelock_fini"
+ "vas_core_rangelock_hold"
+ "vas_core_rangelock_install_locked"
+ "vas_core_rangelock_release"
+ "vas_core_set_faultstate"
+ "vas_core_siptable_map_tables"
+ "vas_lock_ensure_no_conflicts"
+ "vas_lock_ensure_rangelock"
+ "vas_return_code(ret) != VAS_SUCCESS"
+ "xrt_process_info_is_set( XRT_PROCESS_INFO_VAS, XRT__PLATFORM_INFO_VAS_SEGMENTINFO_TABLE )"
- "!_span_tree_remove(vas_core_vas_span_tree(span_b->vas), span_b)"
- "!entry"
- "/AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.4.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
- "WARNING: destroying a span that still has spanamp contents (type %u). The PMM won't be informed of these slots' deletion.\n"
- "[VAS abort in function %s at line %d] Could not allocate a fault table entry\n"
- "[VAS abort in function %s at line %d] [true: %llx %s %llx]Cannot map %p[%ld]: page %p already mapped\n"
- "[VAS abort in function %s at line %d] [true: %llx %s %llx]Cannot map %p[%ld]: slot >= %ld\n"
- "[VAS abort in function %s at line %d] [true: %llx %s %llx]no space for segmentinfo page\n"
- "[VAS abort in function %s at line %d] [true: %lx %s %lx]Cannot map %p[%ld]: no sip\n"
- "[VAS abort in function %s at line %d] [true: %lx %s %lx]Corrupted state of faulthandle->vas\n\n"
- "[VAS abort in function %s at line %d] [true: %lx %s %lx]Could not allocate initial span for address space\n\n"
- "[VAS abort in function %s at line %d] [true: %lx %s %lx]adding new page should put it at front of freelist\n"
- "[VAS abort in function %s at line %d] [true: (%s)] Corrupted state of faulthandle(not active)\n\n"
- "[VAS abort in function %s at line %d] [true: (%s)] Couldn't find faultable span in fault table\n"
- "[VAS abort in function %s at line %d] [true: (%s)] len must be non-zero\n"
- "[VAS abort in function %s at line %d] [true: (%s)] spanmap merge failed%s (0x%04hx)\n"
- "_get_fault_lock"
- "_get_fault_lock_ensure_no_conflicts"
- "cnd_wait(&fh->active_cnd, &vas->faultstate.fault_lock)"
- "len_arg == 0"
- "mtx_init(&unallocated->spanmap_lock, mtx_plain)"
- "mtx_lock(&vas->faultstate.fault_lock)"
- "mtx_unlock(&vas->faultstate.fault_lock)"
- "vas_core_fault_table_insert"
- "vas_core_fault_table_remove"

```
