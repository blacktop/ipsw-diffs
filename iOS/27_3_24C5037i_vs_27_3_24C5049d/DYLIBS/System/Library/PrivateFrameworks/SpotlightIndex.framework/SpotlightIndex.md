## SpotlightIndex

> `/System/Library/PrivateFrameworks/SpotlightIndex.framework/SpotlightIndex`

```diff

-2465.2.7.101.0
-  __TEXT.__text: 0x47f2fc
+2465.2.13.0.0
+  __TEXT.__text: 0x482640
   __TEXT.__objc_methlist: 0x404
-  __TEXT.__const: 0xa56a
-  __TEXT.__cstring: 0x2f62d
+  __TEXT.__const: 0xa5ea
+  __TEXT.__cstring: 0x2f77d
   __TEXT.__gcc_except_tab: 0x29c
-  __TEXT.__oslogstring: 0x1e4a4
+  __TEXT.__oslogstring: 0x1ea56
   __TEXT.__ustring: 0x2aa
   __TEXT.__dof_mds: 0x29b
-  __TEXT.__unwind_info: 0x71e8
+  __TEXT.__unwind_info: 0x7250
   __TEXT.__eh_frame: 0x220
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x8a90
+  __DATA_CONST.__const: 0x8aa0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x670

   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x1f38
+  __AUTH_CONST.__auth_got: 0x1f58
   __AUTH.__objc_data: 0xa0
   __AUTH.__data: 0x18d8
   __DATA.__objc_ivar: 0x60

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 7768
-  Symbols:   10281
-  CStrings:  8105
+  Functions: 7794
+  Symbols:   10310
+  CStrings:  8133
 
Symbols:
+ GCC_except_table3830
+ GCC_except_table3835
+ GCC_except_table5078
+ GCC_except_table5081
+ GCC_except_table6794
+ _CFNumberCompare
+ __ZNSt3__16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_EENS5_IS8_EEE20__throw_length_errorB9fqn220106Ev
+ __ZNSt3__16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_EENS5_IS8_EEE24__emplace_back_slow_pathIJS7_S7_EEEPS8_DpOT_
+ ___si_scan_client_objects_block_invoke
+ ___topk_sources_are_complete_block_invoke
+ _blob_table_may_be_recreated
+ _db2_iterate_objects_in_range_with_system_objs
+ _fd_caller_handles_shortage_begin
+ _fd_caller_handles_shortage_end
+ _fd_thread_resource_error_count
+ _index_file_may_be_recreated
+ _si_adopt_field_slot
+ _si_classify_client_object
+ _si_compare_group_slots
+ _si_copy_bundles_by_slot
+ _si_copy_group_assignments
+ _si_create_over_cap_property_data
+ _si_create_property_data
+ _si_group_prefix_fits
+ _si_group_slot_persist_barrier
+ _si_log_group_slot_conflict
+ _si_mark_group_slot_used
+ _si_note_group_slot_field
+ _si_object_string_field
+ _si_persist_group_slot_to_sdb
+ _si_persist_one_group_slot
+ _si_persist_unpersisted_group_slots
+ _si_queue_property_only_slot
+ _si_restore_deleted_group_slot
+ _si_sync_slot_object_system_flag
+ _topk_open
- GCC_except_table3823
- GCC_except_table3828
- GCC_except_table5071
- GCC_except_table5074
- GCC_except_table6767
- ____ZN16IVFVectorIndex_s20completeChangePrefixEiPKcS1_S1__block_invoke_2
- ___si_populateClientStates_block_invoke
CStrings:
+ "%s head open failed for lack of fds (%d); not recovering"
+ "%s:%d: %s open fail, %d; kept, not recreated"
+ "%s:%d: <si:%s> - %ld group slots are assigned to more than one bundle"
+ "%s:%d: <si:%s> - Failed to mark the store dirty after a group slot write, rc:%d"
+ "%s:%d: <si:%s> - Failed to store group slot %u for %@, rc:%d; will retry"
+ "%s:%d: <si:%s> - Giving up storing group slot %u for %@ after %ld attempts, rc:%d; it is durable only while GroupAssignments fits in kMDStoreProperties"
+ "%s:%d: <si:%s> - GroupAssignments property has slot %@ for %@ but its searchd object has %@; using the object's"
+ "%s:%d: <si:%s> - Ignoring malformed %s for %@, type:%d, length:%u"
+ "%s:%d: <si:%s> - Skipping identity-only system client-state object 0x%llx"
+ "%s:%d: <si:%s> - Unreadable fields on system client-state object 0x%llx, rc:%d; loading what is readable"
+ "%s:%d: IVFVectorIndex::completeChangePrefix leaving catalog at %s"
+ "%s:%d: IVFVectorIndex::completeChangePrefix oldPrefix %s newPrefix %s failed to set dir"
+ "%s:%d: IVFVectorIndex::completeChangePrefix rename %s to %s failed %d"
+ "%s:%d: IVFVectorIndex::completeChangePrefix rename catalog %s to %s failed %d"
+ "*warn* out of fds opening %s; the index opens without it, and the store's topK is kept until the index reopens or is merged"
+ "2465.2.13"
+ "<si:%s> - %ld group slots read from searchd objects, %ld queued for them"
+ "Could not open %s/%s for lack of fds (%d); not recovering"
+ "_kMDGroupAssignment"
+ "db_iterate_objects_in_range_with_system_objs"
+ "int si_persist_group_slot_to_sdb(SIRef, CFStringRef, uint8_t)"
+ "read index state, %d"
+ "si_log_group_slot_conflict"
+ "si_log_group_slot_failure"
+ "si_merge_group_slot_fields"
+ "si_note_group_slot_field"
+ "si_persist_group_slot_to_sdb"
+ "si_scan_reads_system_object"
+ "topK not rebuilt: an index opened without its topK for lack of fds"
+ "v40@?0^{__SI=Q{SIFileOps=^?^?^?}{SIGuardedFd=iQ}isII^{SIWatchDog}^{__CFDictionary}{_opaque_pthread_rwlock_t=q[192c]}{si_missing_oids_s={os_unfair_lock_s=I}^{__RLEOIDArray}^{__RLEOIDArray}}{si_missing_oids_s={os_unfair_lock_s=I}^{__RLEOIDArray}^{__RLEOIDArray}}{os_unfair_lock_s=I}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}^{__CFDictionary}^{_MDPlistContainer}Bi[18^{si_scheduler_token_s}]iI[4^{dispatch_semaphore_s}]{?=[18^{_si_work_scheduler}][20^{_si_workqueue}]^{si_workqueue_list_s}}^{dispatch_queue_s}^{datastore_info}{CIMetaInfo=i^{fd_obj}iQIIIIIIIIqqiiBI}^{DocStore}QQ{_opaque_pthread_mutex_t=q[56c]}^{ContentIndexList}^{ContentIndexList}iII^{_SI_PersistentIDStore}{__SIStoreToken={?=CCCCCCCCCCCCCCCC}^{__CFUUID}}ACAII{os_unfair_lock_s=I}ddBiI^{__CFDictionary}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{os_unfair_lock_s=I}^{__CFBag}{_opaque_pthread_mutex_t=q[56c]}^{__CFSet}^{__CFDictionary}Q^{__CFBag}^{__CFDictionary}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}iIIIIIIIIIIIIIIIIIIIIBBBAq^{__CFDictionary}^{__CFBitVector}^{__CFSet}^{__CFDictionary}qq^{__CFDictionary}^{__CFArray}^{si_mobile_journal}^{si_mobile_journal}^{si_mobile_journal}AqAqAq^{dispatch_source_s}^{__CFDictionary}{_opaque_pthread_mutex_t=q[56c]}^{__CFArray}Cd^?^vdd{?=^{fd_obj}IIIq{os_unfair_lock_s=I}BB^vQQQQAB}III^{FinderDateFields}{_opaque_pthread_mutex_t=q[56c]}^{fd_obj}^{fd_obj}^{fd_obj}iii^{_SIIndexCallbacks}^{__CFArray}^{__CFArray}qqqQIIiiBBBBBBBABB^{si_scheduler_token_s}BBBBBBQq[4096c]{os_unfair_lock_s=I}{os_unfair_lock_s=I}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b2b1b1^i^{__CFSet}^{__CFDictionary}^{__SIUINT64Set}^{ReverseDirStore_s}^{FileTree_Overlay_s}^{__CFSet}^{TermUpdateSet}{_opaque_pthread_rwlock_t=q[192c]}[16C]Bi^{datastore_info}AIBB[5i]*iI^vB^{fd_obj}iiii{AccumulatedCounts_s={_opaque_pthread_mutex_t=q[56c]}[256q][256I][256I]}BB^{si_analytics_s}}8^{_xpc_activity_s=}16^B24^{dispatch_group_s=}32"
- "2465.2.7.101"
- "v40@?0^{__SI=Q{SIFileOps=^?^?^?}{SIGuardedFd=iQ}isII^{SIWatchDog}^{__CFDictionary}{_opaque_pthread_rwlock_t=q[192c]}{si_missing_oids_s={os_unfair_lock_s=I}^{__RLEOIDArray}^{__RLEOIDArray}}{si_missing_oids_s={os_unfair_lock_s=I}^{__RLEOIDArray}^{__RLEOIDArray}}{os_unfair_lock_s=I}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}^{__CFDictionary}^{_MDPlistContainer}Bi[18^{si_scheduler_token_s}]iI[4^{dispatch_semaphore_s}]{?=[18^{_si_work_scheduler}][20^{_si_workqueue}]^{si_workqueue_list_s}}^{dispatch_queue_s}^{datastore_info}{CIMetaInfo=i^{fd_obj}iQIIIIIIIIqqiiBI}^{DocStore}QQ{_opaque_pthread_mutex_t=q[56c]}^{ContentIndexList}^{ContentIndexList}iII^{_SI_PersistentIDStore}{__SIStoreToken={?=CCCCCCCCCCCCCCCC}^{__CFUUID}}ACAII{os_unfair_lock_s=I}ddBiI^{__CFDictionary}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{os_unfair_lock_s=I}^{__CFBag}{_opaque_pthread_mutex_t=q[56c]}^{__CFSet}^{__CFDictionary}Q^{__CFBag}^{__CFDictionary}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}iIIIIIIIIIIIIIIIIIIIIBBBAq^{__CFDictionary}^{__CFBitVector}^{__CFDictionary}^{__CFArray}^{si_mobile_journal}^{si_mobile_journal}^{si_mobile_journal}AqAqAq^{dispatch_source_s}^{__CFDictionary}{_opaque_pthread_mutex_t=q[56c]}^{__CFArray}Cd^?^vdd{?=^{fd_obj}IIIq{os_unfair_lock_s=I}BB^vQQQQAB}III^{FinderDateFields}{_opaque_pthread_mutex_t=q[56c]}^{fd_obj}^{fd_obj}^{fd_obj}iii^{_SIIndexCallbacks}^{__CFArray}^{__CFArray}qqqQIIiiBBBBBBBABB^{si_scheduler_token_s}BBBBBBQq[4096c]{os_unfair_lock_s=I}{os_unfair_lock_s=I}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b2b1b1^i^{__CFSet}^{__CFDictionary}^{__SIUINT64Set}^{ReverseDirStore_s}^{FileTree_Overlay_s}^{__CFSet}^{TermUpdateSet}{_opaque_pthread_rwlock_t=q[192c]}[16C]Bi^{datastore_info}AIBB[5i]*iI^vB^{fd_obj}iiii{AccumulatedCounts_s={_opaque_pthread_mutex_t=q[56c]}[256q][256I][256I]}BB^{si_analytics_s}}8^{_xpc_activity_s=}16^B24^{dispatch_group_s=}32"
```
