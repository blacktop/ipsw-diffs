## MobileSpotlightIndex

> `/System/Library/PrivateFrameworks/MobileSpotlightIndex.framework/MobileSpotlightIndex`

```diff

-2314.8.0.0.0
-  __TEXT.__text: 0x3dc634
-  __TEXT.__auth_stubs: 0x3690
+2314.10.1.0.8
+  __TEXT.__text: 0x3ea5d0
+  __TEXT.__auth_stubs: 0x36a0
   __TEXT.__objc_methlist: 0x20
-  __TEXT.__const: 0x933e
-  __TEXT.__cstring: 0x1e898
+  __TEXT.__const: 0x974e
+  __TEXT.__cstring: 0x1ee4e
   __TEXT.__gcc_except_tab: 0x1b24
-  __TEXT.__oslogstring: 0x18edd
+  __TEXT.__oslogstring: 0x194dc
   __TEXT.__dlopen_cstrs: 0x150
   __TEXT.__ustring: 0x20
   __TEXT.__dof_mds: 0x29b
-  __TEXT.__unwind_info: 0x5248
+  __TEXT.__unwind_info: 0x52b0
   __TEXT.__eh_frame: 0x178
   __TEXT.__objc_classname: 0x19
   __TEXT.__objc_methname: 0x4fe
   __TEXT.__objc_methtype: 0x34
   __TEXT.__objc_stubs: 0x800
   __DATA_CONST.__got: 0x250
-  __DATA_CONST.__const: 0x7b90
+  __DATA_CONST.__const: 0x7d18
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x210
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x1b58
+  __AUTH_CONST.__auth_got: 0x1b60
   __AUTH_CONST.__auth_ptr: 0x18
-  __AUTH_CONST.__const: 0x7200
-  __AUTH_CONST.__cfstring: 0x4760
+  __AUTH_CONST.__const: 0x7208
+  __AUTH_CONST.__cfstring: 0x4440
   __AUTH_CONST.__objc_const: 0x138
   __AUTH.__objc_data: 0x50
   __AUTH.__data: 0x1508
   __DATA.__objc_ivar: 0x14
-  __DATA.__data: 0x1028
-  __DATA.__bss: 0x103e0
+  __DATA.__data: 0x10a0
+  __DATA.__bss: 0x10448
   __DATA_DIRTY.__data: 0x3f8
-  __DATA_DIRTY.__bss: 0x2cc98
+  __DATA_DIRTY.__bss: 0x2ccf0
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 6467
-  Symbols:   7716
-  CStrings:  7027
+  Functions: 6522
+  Symbols:   7772
+  CStrings:  7112
 
Symbols:
+ _CFDateFormatterCreateStringWithAbsoluteTime
+ _CFErrorCopyDescription
+ _CFPropertyListCreateWithStream
+ _CFPropertyListWrite
+ _CFReadStreamClose
+ _CFReadStreamCreateWithFile
+ _CFReadStreamOpen
+ _CFWriteStreamClose
+ _CFWriteStreamCreateWithFile
+ _CFWriteStreamOpen
+ _SIExecuteResumeActivityCallback
+ _SIGetPreviousError
+ __SIGetFieldNameForId
+ __SIIsSystemStatusBusy
+ __SIResumeWatchdog
+ __SISetSystemStatusBusy
+ __SISuspendWatchdog
+ _pthread_threadid_np
- _MDTrieClose
- _MDTrieCreate
- _MDTrieGetFd
- _MDTrieSync
- _SpotlightCacheAttributes
- _SpotlightCacheDelete
- _SpotlightCacheDeleteEntry
- _SpotlightCacheInsertEntry
- _SpotlightCacheLookup
- _SpotlightCachePayload
CStrings:
+ "### change index prefix [%!d(MISSING)] %!s(MISSING) to %!s(MISSING)"
+ "%!d(MISSING), %!u(MISSING), %!u(MISSING), %!s(MISSING)"
+ "%!s(MISSING) complete write tmp header with count: %!d(MISSING)"
+ "%!s(MISSING)%!d(MISSING)."
+ "%!s(MISSING).%!s(MISSING)"
+ "%!s(MISSING).%!s(MISSING)%!d(MISSING)."
+ "%!s(MISSING):%!d(MISSING): %!p(MISSING) write index state error:%!d(MISSING)"
+ "%!s(MISSING):%!d(MISSING): %!u(MISSING) of %!u(MISSING) vectors has vectorId=0"
+ "%!s(MISSING):%!d(MISSING): (%!u(MISSING)) Could not open/create error file: %!d(MISSING)"
+ "%!s(MISSING):%!d(MISSING): (%!u(MISSING)) Could not truncate error file: %!d(MISSING)"
+ "%!s(MISSING):%!d(MISSING): (%!u(MISSING)) Error %!d(MISSING) writing to error file"
+ "%!s(MISSING):%!d(MISSING): (%!u(MISSING)) Error opening error file: %!d(MISSING)"
+ "%!s(MISSING):%!d(MISSING): (%!u(MISSING)) Error writing to error file %!l(MISSING)ld != %!l(MISSING)ld"
+ "%!s(MISSING):%!d(MISSING): (%!u(MISSING)) lseek error on error file: %!d(MISSING)"
+ "%!s(MISSING):%!d(MISSING): (%!u(MISSING)) pread error on error file %!l(MISSING)ld != %!l(MISSING)ld"
+ "%!s(MISSING):%!d(MISSING): (%!u(MISSING)) pread error on error file: %!d(MISSING)"
+ "%!s(MISSING):%!d(MISSING): CIMetaInfoOpenAndLock error %!d(MISSING)"
+ "%!s(MISSING):%!d(MISSING): CIMetaInfoRead error %!d(MISSING)"
+ "%!s(MISSING):%!d(MISSING): Index count too high; ignore split"
+ "%!s(MISSING):%!d(MISSING): Index count too high; start merge"
+ "%!s(MISSING):%!d(MISSING): InsertMergedIndex failed at %!s(MISSING)"
+ "%!s(MISSING):%!d(MISSING): Invalid ContentIndexDocSetRef:%!p(MISSING) docId:%!l(MISSING)ld"
+ "%!s(MISSING):%!d(MISSING): [%!s(MISSING)] %!s(MISSING) with %!u(MISSING) vectors reset for error: %!s(MISSING)"
+ "%!s(MISSING):%!d(MISSING): [%!s(MISSING)] open %!s(MISSING) indexId %!u(MISSING) doesn't match previous assigned %!u(MISSING)"
+ "%!s(MISSING):%!d(MISSING): [VILoss] Error reading from vi drop file: %!s(MISSING)"
+ "%!s(MISSING):%!d(MISSING): [VILoss] Error writing to vi drop file: %!s(MISSING)"
+ "%!s(MISSING):%!d(MISSING): [VILoss] Failed reading from vi drop file"
+ "%!s(MISSING):%!d(MISSING): [VILoss] Failed to open/create VI drop file"
+ "%!s(MISSING):%!d(MISSING): [VILoss] Failed to read from VI drop file"
+ "%!s(MISSING):%!d(MISSING): [VILoss] Failed to write to vi drop file"
+ "%!s(MISSING):%!d(MISSING): [VILoss] Failed writing to vi drop file"
+ "%!s(MISSING):%!d(MISSING): _SIOpenIndexFilesWithState error %!d(MISSING)"
+ "%!s(MISSING):%!d(MISSING): data id %!l(MISSING)ld invalid indexId %!u(MISSING) offset 0x%!l(MISSING)lx meta 0x%!x(MISSING)"
+ "%!s(MISSING):%!d(MISSING): errno:%!d(MISSING) %!s(MISSING) -> %!s(MISSING)"
+ "%!s(MISSING):%!d(MISSING): fd_no_cache err: %!d(MISSING)"
+ "%!s(MISSING):%!d(MISSING): fd_open source err: %!d(MISSING)"
+ "%!s(MISSING):%!d(MISSING): info: %!l(MISSING)ld freq:%!d(MISSING) read posting:%!d(MISSING) of %!d(MISSING)"
+ "%!s(MISSING):%!d(MISSING): info: %!l(MISSING)ld freq:%!d(MISSING) remaining posting:%!d(MISSING) of %!d(MISSING)"
+ "%!s(MISSING):%!d(MISSING): invalid pc_priority %!u(MISSING)"
+ "%!s(MISSING):%!d(MISSING): vector at %!u(MISSING) vectorId=0"
+ "%!s(MISSING):%!d(MISSING): write index state fd:%!d(MISSING) rs:%!l(MISSING)d error:%!d(MISSING)"
+ "%!s(MISSING):%!u(MISSING): %!s(MISSING)"
+ "%!s(MISSING):%!u(MISSING): failed assertion '%!s(MISSING)' %!s(MISSING) Attempted to add past beginning of flipped WPC buffer; position: %!x(MISSING), lastInput: %!x(MISSING), offset: %!z(MISSING)u, intCount: %!l(MISSING)d, line: %!d(MISSING)"
+ "%!s(MISSING):%!u(MISSING): failed assertion '%!s(MISSING)' %!s(MISSING) [round-%!d(MISSING)] docId:%!d(MISSING) newDocID:%!d(MISSING) posStart:%!p(MISSING) next:%!d(MISSING)"
+ "%!s(MISSING):%!u(MISSING): failed assertion '%!s(MISSING)' %!s(MISSING) [round-%!d(MISSING)] unexpected zero newDocID. docId:%!d(MISSING) posStart:%!p(MISSING)  next:%!d(MISSING)"
+ "%!s(MISSING):%!u(MISSING): failed assertion '%!s(MISSING)' %!s(MISSING) readVInt32_boundschecked: exceeds max size for uint32_t"
+ "%!s(MISSING):%!u(MISSING): failed assertion '%!s(MISSING)' %!s(MISSING) sig 0x%!x(MISSING) (0x%!x(MISSING)) != 0x%!x(MISSING) (0x%!x(MISSING))"
+ "%!s(MISSING):%!u(MISSING): failure log '%!s(MISSING)' %!s(MISSING) flat store, pageSize = %!u(MISSING), pageEnd = %!u(MISSING)"
+ "%!s(MISSING):%!u(MISSING): failure log '%!s(MISSING)' %!s(MISSING) flat store, pageSize = %!u(MISSING), sizeShift = %!d(MISSING)"
+ "%!s(MISSING)||%!s(MISSING)||%!u(MISSING)"
+ "(%!u(MISSING)) No error file"
+ "*warn* %!s(MISSING)"
+ "*warn* Invalid indexId %!u(MISSING) for vid: %!l(MISSING)lu"
+ "*warn* [%!s(MISSING)] %!s(MISSING) with %!u(MISSING) vectors dropped for error: %!s(MISSING)"
+ "*warn* metaFile %!s(MISSING) not valid"
+ "======= fd_system_status_set_busy:%!d(MISSING)"
+ "CIMetaInfoCreateWithPrefix"
+ "CIMetaInfoOpenAndLock failed with %!d(MISSING)"
+ "CIMetaInfoRead failed %!d(MISSING)"
+ "CIMetaInfoRead failed with %!d(MISSING)"
+ "CIReadPostings"
+ "CIWritePostings"
+ "ContentIndexDocSetInRangeDocId"
+ "ContentIndexOpenBulk err %!d(MISSING), %!d(MISSING)"
+ "ContentIndexOpenBulk failed %!d(MISSING), %!d(MISSING)"
+ "Corrupted"
+ "Create"
+ "Failure renaming index"
+ "IVFMinVectorsUseANN"
+ "IVFVectorIndexRoot_s"
+ "InsertMergedIndex %!p(MISSING) live count %!d(MISSING) current %!d(MISSING)"
+ "InsertMergedIndex success at %!s(MISSING)"
+ "None"
+ "Open"
+ "Purged"
+ "VersionMismatch"
+ "[%!s(MISSING)] cancelMerge %!s(MISSING)"
+ "[%!s(MISSING)] recoverIds from %!s(MISSING) %!s(MISSING)purgeable"
+ "_SIOpenIndexFilesWithState failed with -1"
+ "__builtin_popcount(pageSize+int_sizeof(*page)) == 1"
+ "__si_write_error_to_file"
+ "_data_map32_sync_header_to_tmp"
+ "_si_load_error_from_file"
+ "_swapIndex"
+ "content index open failed %!d(MISSING)"
+ "count == 0"
+ "create index error 1"
+ "create index error 2"
+ "db_scan_lost_ids for %!u(MISSING) dropped vectors"
+ "db_update_datastore_state failed %!d(MISSING), %!d(MISSING)"
+ "ds dirty, rs needs shadow"
+ "errorFile"
+ "failed to acquire lock for meta info"
+ "failed to create meta info fd %!d(MISSING)"
+ "failed to flock meta info %!d(MISSING)"
+ "failed to open meta info %!d(MISSING)"
+ "failed to statfs meta info %!d(MISSING)"
+ "fd_msync(%!p(MISSING)) err %!d(MISSING)"
+ "get datastore failed"
+ "in_store.signature==ref->store->signature"
+ "indexId == savedIndexId"
+ "indexState.aside"
+ "indexVersion"
+ "init index error %!d(MISSING)"
+ "invalid datastore %!d(MISSING), %!d(MISSING)"
+ "invalid index version recovering %!d(MISSING), %!d(MISSING)"
+ "invalid index version reindexing %!d(MISSING), %!d(MISSING)"
+ "invalid meta info %!d(MISSING), %!d(MISSING)"
+ "invalid reverse store %!d(MISSING)"
+ "kMDQueryConstantOrphanOID"
+ "live."
+ "non-"
+ "open datastore failed %!d(MISSING)"
+ "open from fast flush canceled %!d(MISSING)"
+ "open index state failed %!d(MISSING), %!d(MISSING)"
+ "pageSize > 0 && pageEnd <= pageSize"
+ "rebuild activity journal name"
+ "rebuilding index because of huge journals or merge files"
+ "recover datastore error %!d(MISSING)"
+ "recoverIds %!u(MISSING) vectors lost"
+ "recoverIds for %!u(MISSING) vectors"
+ "rename_transitional_state"
+ "repeated crashes"
+ "rescan_needed"
+ "restore db dirty pages failed %!d(MISSING)"
+ "restore rs dirty pages failed %!d(MISSING)"
+ "restoring term update set failed %!d(MISSING)"
+ "reverseStoreUpdateState err %!d(MISSING)"
+ "si_recompute_sizes end (%!d(MISSING))"
+ "si_recompute_sizes start"
+ "si_store_index_state"
+ "si_write_index_state err %!d(MISSING)"
+ "si_write_index_state failed %!d(MISSING), %!d(MISSING)"
+ "syncSet->indexCount == 0"
+ "tmp.%!s(MISSING).rehash"
+ "tmp.indexState"
+ "tmp.live.%!d(MISSING)."
+ "tmp.movePlan"
+ "tmp.spotlight.state.transition"
+ "tmp.victim"
+ "too many live indexes %!d(MISSING), %!d(MISSING)"
+ "v40@?0^{__SI=Q{SIFileOps=^?^?^?}{SIGuardedFd=iQ}isII^{SIWatchDog}^{__CFDictionary}{_opaque_pthread_rwlock_t=q[192c]}{si_missing_oids_s={os_unfair_lock_s=I}^{__RLEOIDArray}^{__RLEOIDArray}}{si_missing_oids_s={os_unfair_lock_s=I}^{__RLEOIDArray}^{__RLEOIDArray}}{os_unfair_lock_s=I}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}^{__CFDictionary}^{_MDPlistContainer}Bi[18^{si_scheduler_token_s}]iI[4^{dispatch_semaphore_s}]{?=[18^{_si_work_scheduler}][20^{_si_workqueue}]^{si_workqueue_list_s}}^{dispatch_queue_s}^{datastore_info}{CIMetaInfo=i^{fd_obj}iQIIIIIIIIqqiiBI}^{DocStore}QQ{_opaque_pthread_mutex_t=q[56c]}^{ContentIndexList}^{ContentIndexList}iII^{_SI_PersistentIDStore}{__SIStoreToken={?=CCCCCCCCCCCCCCCC}^{__CFUUID}}ACAII{os_unfair_lock_s=I}ddBiI^{__CFDictionary}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{os_unfair_lock_s=I}^{__CFBag}{_opaque_pthread_mutex_t=q[56c]}^{__CFSet}^{__CFDictionary}Q^{__CFBag}^{__CFDictionary}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}iIIIIIIIIIIIIIIIIIIIBBAq^{__CFDictionary}^{__CFBitVector}^{si_mobile_journal}^{si_mobile_journal}^{si_mobile_journal}AqAqAqd^?^vdd{?=^{fd_obj}IIIq{os_unfair_lock_s=I}BB}III^{FinderDateFields}{_opaque_pthread_mutex_t=q[56c]}^{fd_obj}^{fd_obj}^{fd_obj}iii^{_SIIndexCallbacks}^{__CFArray}^{__CFArray}qqqQIIiiBBBBBBBABB^{si_scheduler_token_s}BBBBBQq[4096c]{os_unfair_lock_s=I}{os_unfair_lock_s=I}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b2b1^i^{__CFSet}^{__CFDictionary}^{__SIUINT64Set}^{ReverseDirStore_s}^{FileTree_Overlay_s}^{__CFSet}^{TermUpdateSet}{_opaque_pthread_rwlock_t=q[192c]}[16C]Bi^{datastore_info}AIBB[5i]*iI^vB^{fd_obj}iiii{AccumulatedCounts_s={_opaque_pthread_mutex_t=q[56c]}[256q][256I]}}8^{_xpc_activity_s=}16^B24^{dispatch_group_s=}32"
+ "v44@?0r*8I16S20i24i28B32i36I40"
+ "vectorIndexDrops.plist"
+ "write state:%!s(MISSING)"
+ "writeVectorIndexDrop"
- "!found"
- "%!p(MISSING) write state:%!s(MISSING)"
- "%!s(MISSING):%!d(MISSING): %!p(MISSING) write index state fd:%!d(MISSING) rs:%!l(MISSING)d error:%!d(MISSING)"
- "%!s(MISSING):%!d(MISSING): Could not create new live index %!@(MISSING)"
- "%!s(MISSING):%!d(MISSING): InsertNewIndex failed at %!s(MISSING)"
- "%!s(MISSING):%!d(MISSING): [%!s(MISSING)] %!s(MISSING) reset for error %!d(MISSING)"
- "%!s(MISSING):%!d(MISSING): [%!s(MISSING)] open %!s(MISSING) indexId: %!u(MISSING) doesn't match previous assigned %!u(MISSING)"
- "%!s(MISSING):%!d(MISSING): data id %!l(MISSING)ld invalid index_id %!u(MISSING) offset 0x%!l(MISSING)lx meta 0x%!x(MISSING)"
- "%!s(MISSING):%!d(MISSING): open meta info error %!d(MISSING)"
- "%!s(MISSING):%!u(MISSING): failed assertion '%!s(MISSING)' %!s(MISSING) offset:%!l(MISSING)ld, free_region:%!l(MISSING)ld"
- "*warn* Vector index missing: %!s(MISSING)"
- "*warn* [%!s(MISSING)] metaFile %!s(MISSING) not valid"
- "CIMetaInfoCreate"
- "InsertNewIndex %!p(MISSING) live count %!d(MISSING) current %!d(MISSING)"
- "InsertNewIndex success at %!s(MISSING)"
- "Rebuilding index"
- "Rebuilding index because of huge journals or merge files"
- "Rebuilding index because of repeated crashes"
- "SIQuery.cpp"
- "SpotlightCache delete do not support bundleID %!@(MISSING)"
- "SpotlightCache insert do not support bundleID %!@(MISSING)"
- "_kMDItemAppEngagementData"
- "_kMDItemAppEntitySN"
- "_kMDItemEngagementData"
- "_kMDItemKnowledgeIndexVersion"
- "_kMDItemRenderData"
- "com.apple.parsec.itunes.iosSoftware"
- "com.apple.parsec.maps"
- "com.apple.parsec.sports"
- "com.apple.parsec.stocks"
- "com.apple.searchd.indexes.makeunavailable"
- "com.apple.spotlight.category"
- "com.apple.spotlight.contacts"
- "create index error"
- "ds dirty, rs needs shadow "
- "error"
- "init index error"
- "invalid datastore"
- "invalid index version recovering"
- "invalid index version reindexing"
- "invalid meta info"
- "invalid reverse store"
- "invalid term update set "
- "kMDItemKeyphraseVersion"
- "kMDItemTextContentLanguage"
- "msync(%!p(MISSING)) err %!d(MISSING)"
- "open datastore failed"
- "open index error"
- "open meta info error"
- "options"
- "pc"
- "qp->_free_cache_data==(void*)ContentIndexQueryNodeDispose"
- "reason"
- "rebuildActivityJournalName"
- "ref->syncSet->indexCount == 0"
- "restore db dirty pages failed"
- "restore rs dirty pages failed"
- "restoring term update set failed"
- "spotlightcache"
- "strstr(pathPtr, \"tmp.\") == 0"
- "v40@?0^{__SI=Q{SIFileOps=^?^?^?}{SIGuardedFd=iQ}isII^{SIWatchDog}^{__CFDictionary}{_opaque_pthread_rwlock_t=q[192c]}{si_missing_oids_s={os_unfair_lock_s=I}^{__RLEOIDArray}^{__RLEOIDArray}}{si_missing_oids_s={os_unfair_lock_s=I}^{__RLEOIDArray}^{__RLEOIDArray}}{os_unfair_lock_s=I}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}{si_comm_dates_s=^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}^{__CFBag}}^{__CFDictionary}^{_MDPlistContainer}Bi[18^{si_scheduler_token_s}]iI[4^{dispatch_semaphore_s}]{?=[18^{_si_work_scheduler}][20^{_si_workqueue}]^{si_workqueue_list_s}}^{dispatch_queue_s}^{datastore_info}{CIMetaInfo=i^{fd_obj}iQIIIIIIIIqqiiB}^{_MDTrie}^{DocStore}QQ{_opaque_pthread_mutex_t=q[56c]}^{ContentIndexList}^{ContentIndexList}iII^{_SI_PersistentIDStore}{__SIStoreToken={?=CCCCCCCCCCCCCCCC}^{__CFUUID}}ACAII{os_unfair_lock_s=I}ddBiI^{__CFDictionary}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{os_unfair_lock_s=I}^{__CFBag}{_opaque_pthread_mutex_t=q[56c]}^{__CFSet}^{__CFDictionary}Q^{__CFBag}^{__CFDictionary}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}iIIIIIIIIIIIIIIIIIIIBBAq^{__CFDictionary}^{__CFBitVector}^{si_mobile_journal}^{si_mobile_journal}^{si_mobile_journal}AqAqAqd^?^vdd{?=^{fd_obj}IIIq{os_unfair_lock_s=I}BB}III^{FinderDateFields}{_opaque_pthread_mutex_t=q[56c]}^{fd_obj}^{fd_obj}^{fd_obj}iii^{_SIIndexCallbacks}^{__CFArray}^{__CFArray}qqqQIIiiBBBBBBBABB^{si_scheduler_token_s}BBBBBQq[4096c]{os_unfair_lock_s=I}{os_unfair_lock_s=I}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b2b1^i^{__CFSet}^{__CFDictionary}^{__SIUINT64Set}^{ReverseDirStore_s}^{FileTree_Overlay_s}^{__CFSet}^{TermUpdateSet}{_opaque_pthread_rwlock_t=q[192c]}[16C]Bi^{datastore_info}AIBB[5i]*iI^vB^{fd_obj}iiii{AccumulatedCounts_s={_opaque_pthread_mutex_t=q[56c]}[256q][256I]}}8^{_xpc_activity_s=}16^B24^{dispatch_group_s=}32"

```
