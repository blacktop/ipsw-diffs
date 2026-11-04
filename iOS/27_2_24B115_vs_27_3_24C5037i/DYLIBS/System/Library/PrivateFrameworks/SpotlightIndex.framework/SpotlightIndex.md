## SpotlightIndex

> `/System/Library/PrivateFrameworks/SpotlightIndex.framework/SpotlightIndex`

```diff

-2465.1.9.0.0
-  __TEXT.__text: 0x47e17c
+2465.2.7.101.0
+  __TEXT.__text: 0x47f2fc
   __TEXT.__objc_methlist: 0x404
   __TEXT.__const: 0xa56a
-  __TEXT.__cstring: 0x2f54f
+  __TEXT.__cstring: 0x2f62d
   __TEXT.__gcc_except_tab: 0x29c
-  __TEXT.__oslogstring: 0x1e59a
+  __TEXT.__oslogstring: 0x1e4a4
   __TEXT.__ustring: 0x2aa
   __TEXT.__dof_mds: 0x29b
-  __TEXT.__unwind_info: 0x71f0
+  __TEXT.__unwind_info: 0x71e8
   __TEXT.__eh_frame: 0x220
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x8aa0
+  __DATA_CONST.__const: 0x8a90
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x670

   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x1f40
+  __AUTH_CONST.__auth_got: 0x1f38
   __AUTH.__objc_data: 0xa0
   __AUTH.__data: 0x18d8
   __DATA.__objc_ivar: 0x60

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
   Functions: 7768
-  Symbols:   10286
-  CStrings:  8110
+  Symbols:   10281
+  CStrings:  8105
 
Symbols:
+ GCC_except_table221
+ GCC_except_table228
+ GCC_except_table245
+ GCC_except_table3823
+ GCC_except_table3828
+ GCC_except_table503
+ GCC_except_table5071
+ GCC_except_table5074
+ GCC_except_table520
+ GCC_except_table6767
+ __CIIndexSetAddRange_Bitmap_Src
+ __CIIndexSetAddRange_Bitmap_Src_SparseDst_Enumerate
+ __CIIndexSetAddRange_Bitmap_Src_SparseDst_Words
+ __CIIndexSetWordWalkFlush
+ __SISampleStringFieldCensus
+ ___si_hardlinked_journal_sweep_schedule_block_invoke
+ _db2_census_fetch_page
+ _fieldIdsInternStringsVerbatim
+ _si_sample_string_field_census
+ _x_fstatat
- GCC_except_table220
- GCC_except_table227
- GCC_except_table244
- GCC_except_table3831
- GCC_except_table3836
- GCC_except_table502
- GCC_except_table5079
- GCC_except_table5082
- GCC_except_table519
- GCC_except_table6768
- _SpotlightCacheBundleID
- __sdb_cache_check_fault
- __tus_check_fault
- __tus_protect
- __tus_unprotect
- __wrcache_arm_slot
- __wrcache_free_page
- _db_cache_call_with_entry
- _db_cache_dealloc
- _db_cache_protect_entry
- _db_cache_unprotect_entry
- _s_mprotect_registry
- _s_mprotect_registry_capacity
- _s_mprotect_registry_count
- _s_mprotect_registry_lock
CStrings:
+ "%s/%d/%s"
+ "%s:%d: <si:%s> - SpotlightIndex#si_hardlinked_journal_sweep fdopendir failed: %d"
+ "%s:%d: <si:%s> - SpotlightIndex#si_hardlinked_journal_sweep fstatat(%s) failed: %d"
+ "%s:%d: <si:%s> - SpotlightIndex#si_hardlinked_journal_sweep openat(%s) failed: %d"
+ "%s:%d: <si:%s> - SpotlightIndex#si_hardlinked_journal_sweep recheck fstatat(%s) failed: %d"
+ "%s:%d: <si:%s> - SpotlightIndex#si_hardlinked_journal_sweep unlinkat(%s) failed: %d"
+ "%s:%d: <si:%s> - SpotlightIndex#si_mobile_journal_hardlink_new_journal Could not get index realpath for journal: %s.%ld"
+ "../"
+ ".journal"
+ ".toc"
+ "2465.2.7.101"
+ "<si:%s> - %p string field census: rc:%d entries:%llu visited:%llu failed:%llu objects:%llu regular:%llu localized:%llu variants:%llu"
+ "SearchUnifiedEmbeddingMD10"
+ "db2_census_slot_result_t db2_census_fetch_page(datastore_info *, db_map_entry, db2_census_page_counts_t *)"
+ "si_hardlinked_journal_sweep_opendir"
+ "si_hardlinked_journal_sweep_recheck_and_unlink"
+ "si_hardlinked_journal_sweep_should_reclaim"
- "2465.1.9"
- "???"
- "ARM"
- "DISARM"
- "FREE"
- "NONE"
- "PROTECT"
- "SDB cache %p slot %d op[oldest+%d]: %{public}s dbp=%p"
- "SDB cache %p slot %d: dbp=%p guarded=%d eligible=%d sz=%zu pgnum=0x%x"
- "SearchUnifiedEmbeddingMD8"
- "TUS kMDSTagUpdateSetPositionInfo guard fault: addr=%p base=%p size=%zu"
- "TUS kMDSTagUpdateSetPositionTable guard fault: addr=%p base=%p size=%zu"
- "TUS kMDSTagUpdateSetPostings guard fault: addr=%p base=%p size=%zu"
- "TUS kMDSTagUpdateSetTerms (dataAllocator) guard fault: addr=%p slab=%p size=%zu"
- "TUS kMDSTagUpdateSetTerms (termSlab) guard fault: addr=%p slab=%p size=%zu"
- "UNPROTECT"
- "Write cache %p: page lost mprotect eligibility after resize (new_ptr=%p, aligned=%d, dbp_sz=%d, page_sz=%zu)"
- "Write cache %p: slot %d page %p armed for mprotect guard"
- "Write cache %p: slot %d page %p freed (was guarded, sz=%zu)"
- "Write cache %p: slot %d page changed from %p to %p after flush — clearing stale mprotect guard"
- "mprotect failed: ptr=%p sz=%zu prot=%d errno=%d"
- "mprotect guard fault at %p: could not acquire registry lock"
```
