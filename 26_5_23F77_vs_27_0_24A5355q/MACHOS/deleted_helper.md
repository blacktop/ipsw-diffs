## deleted_helper

> `/System/Library/PrivateFrameworks/CacheDelete.framework/deleted_helper`

```diff

-819.120.2.0.0
-  __TEXT.__text: 0x5d08
-  __TEXT.__auth_stubs: 0x640
-  __TEXT.__objc_stubs: 0x5a0
-  __TEXT.__objc_methlist: 0xd4
-  __TEXT.__const: 0x14c
-  __TEXT.__gcc_except_tab: 0xf8
-  __TEXT.__objc_methname: 0x401
-  __TEXT.__cstring: 0x76b
-  __TEXT.__oslogstring: 0xfc6
-  __TEXT.__objc_classname: 0x15
-  __TEXT.__objc_methtype: 0x7a
-  __TEXT.__unwind_info: 0x110
-  __DATA_CONST.__auth_got: 0x330
-  __DATA_CONST.__got: 0x60
-  __DATA_CONST.__const: 0x3e0
-  __DATA_CONST.__cfstring: 0x4a0
-  __DATA_CONST.__objc_classlist: 0x8
+901.0.0.0.1
+  __TEXT.__text: 0x9324
+  __TEXT.__auth_stubs: 0x7c0
+  __TEXT.__objc_stubs: 0x8e0
+  __TEXT.__objc_methlist: 0x1cc
+  __TEXT.__const: 0x1ac
+  __TEXT.__gcc_except_tab: 0x44c
+  __TEXT.__objc_classname: 0x40
+  __TEXT.__objc_methname: 0x777
+  __TEXT.__objc_methtype: 0xc5
+  __TEXT.__cstring: 0x874
+  __TEXT.__oslogstring: 0x1cc2
+  __TEXT.__unwind_info: 0x188
+  __DATA_CONST.__const: 0x4e0
+  __DATA_CONST.__cfstring: 0x600
+  __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x78
-  __DATA_CONST.__objc_arraydata: 0xe0
-  __DATA_CONST.__objc_dictobj: 0x50
-  __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x160
-  __DATA.__objc_selrefs: 0x1b8
-  __DATA.__objc_ivar: 0x10
-  __DATA.__objc_data: 0x50
-  __DATA.__bss: 0x50
+  __DATA_CONST.__objc_arraydata: 0xf0
+  __DATA_CONST.__objc_dictobj: 0xa0
+  __DATA_CONST.__auth_got: 0x3f0
+  __DATA_CONST.__got: 0x98
+  __DATA.__objc_const: 0x488
+  __DATA.__objc_selrefs: 0x280
+  __DATA.__objc_ivar: 0x30
+  __DATA.__objc_data: 0x140
+  __DATA.__bss: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/MobileCoreServices.framework/MobileCoreServices

   - /System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CF06E96B-C043-30C9-98CC-419FA4FE4282
-  Functions: 47
-  Symbols:   263
-  CStrings:  256
+  UUID: 9AA0F5E7-E657-304B-B46F-3E8CB6DCFD9E
+  Functions: 80
+  Symbols:   392
+  CStrings:  373
 
Symbols:
+ -[CDBundleCloneInfo groupPurgeableClonesSize]
+ -[CDBundleCloneInfo purgeableClonesSize]
+ -[CDBundleCloneInfo setGroupPurgeableClonesSize:]
+ -[CDBundleCloneInfo setPurgeableClonesSize:]
+ -[CDCloneAnalyzer .cxx_destruct]
+ -[CDCloneAnalyzer _shouldAnalyzeBundleMap]
+ -[CDCloneAnalyzer _shouldAnalyzePartialClones]
+ -[CDCloneAnalyzer _shouldAnalyzePurgeableClones]
+ -[CDCloneAnalyzer analyzeClonesForVolume:urgency:error:]
+ -[CDCloneAnalyzer initWithOptions:]
+ -[CDCloneAnalyzer initWithOptions:dirStatIDToBundleMap:tagHashToBundleIDMap:]
+ -[CDCloneInfo .cxx_destruct]
+ -[CDCloneInfo bundleCloneInfo]
+ -[CDCloneInfo setBundleCloneInfo:]
+ -[CDCloneInfo setTotalPurgeableClones:]
+ -[CDCloneInfo setTotalPurgeablePartialClones:]
+ -[CDCloneInfo totalPurgeableClones]
+ -[CDCloneInfo totalPurgeablePartialClones]
+ GCC_except_table22
+ GCC_except_table26
+ GCC_except_table27
+ GCC_except_table35
+ GCC_except_table38
+ GCC_except_table44
+ GCC_except_table49
+ OBJC_IVAR_$_CDBundleCloneInfo._groupPurgeableClonesSize
+ OBJC_IVAR_$_CDBundleCloneInfo._purgeableClonesSize
+ OBJC_IVAR_$_CDCloneAnalyzer._dirStatIDToBundleMap
+ OBJC_IVAR_$_CDCloneAnalyzer._options
+ OBJC_IVAR_$_CDCloneAnalyzer._tagHashToBundleIDMap
+ OBJC_IVAR_$_CDCloneInfo._bundleCloneInfo
+ OBJC_IVAR_$_CDCloneInfo._totalPurgeableClones
+ OBJC_IVAR_$_CDCloneInfo._totalPurgeablePartialClones
+ _CDGetPurgeSignpostLogHandle
+ _NSLocalizedDescriptionKey
+ _OBJC_CLASS_$_CDBundleCloneInfo
+ _OBJC_CLASS_$_CDCloneAnalyzer
+ _OBJC_CLASS_$_CDCloneInfo
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSLock
+ _OBJC_CLASS_$_NSSet
+ _OBJC_METACLASS_$_CDBundleCloneInfo
+ _OBJC_METACLASS_$_CDCloneAnalyzer
+ _OBJC_METACLASS_$_CDCloneInfo
+ __OBJC_$_INSTANCE_METHODS_CDBundleCloneInfo
+ __OBJC_$_INSTANCE_METHODS_CDCloneAnalyzer
+ __OBJC_$_INSTANCE_METHODS_CDCloneInfo
+ __OBJC_$_INSTANCE_VARIABLES_CDBundleCloneInfo
+ __OBJC_$_INSTANCE_VARIABLES_CDCloneAnalyzer
+ __OBJC_$_INSTANCE_VARIABLES_CDCloneInfo
+ __OBJC_$_PROP_LIST_CDBundleCloneInfo
+ __OBJC_$_PROP_LIST_CDCloneInfo
+ __OBJC_CLASS_RO_$_CDBundleCloneInfo
+ __OBJC_CLASS_RO_$_CDCloneAnalyzer
+ __OBJC_CLASS_RO_$_CDCloneInfo
+ __OBJC_METACLASS_RO_$_CDBundleCloneInfo
+ __OBJC_METACLASS_RO_$_CDCloneAnalyzer
+ __OBJC_METACLASS_RO_$_CDCloneInfo
+ __RegisterCacheDeleteOrphanDirHandlerService_block_invoke.180
+ __RegisterPurgeSpecificAppsService_block_invoke.207
+ __RegisterPurgeSpecificAppsService_block_invoke.208
+ __RegisterPurgeSpecificAppsService_block_invoke.217
+ __RegisterPurgeSpecificAppsService_block_invoke.218
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ___NSDictionary0__struct
+ ___RegisterPurgeSpecificAppsService_block_invoke
+ ___RegisterPurgeSpecificAppsService_block_invoke_2
+ ___block_descriptor_108_e8_32s40s48s56s64s72s80r88r_e5_v8?0ls32l8s40l8s48l8s56l8s64l8r80l8r88l8s72l8
+ ___block_descriptor_76_e8_32s40s48s56s64r_e5_v8?0lr64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_84_e8_32s40s48s56s64r_e5_v8?0lr64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_92_e8_32s40s48s56s64s72s80r_e5_v8?0ls32l8s40l8s48l8s56l8s64l8r80l8s72l8
+ ___fsPurge_block_invoke
+ ___fsPurgeable_block_invoke
+ ___kCFBooleanFalse
+ ___kCFBooleanTrue
+ __block_literal_global.118
+ __block_literal_global.137
+ __block_literal_global.149
+ __block_literal_global.151
+ __block_literal_global.158
+ __block_literal_global.161
+ __block_literal_global.164
+ __block_literal_global.169
+ __block_literal_global.171
+ __block_literal_global.177
+ __block_literal_global.182
+ __block_literal_global.184
+ __block_literal_global.190
+ __block_literal_global.210
+ __block_literal_global.220
+ __block_literal_global.241
+ __main_block_invoke.114
+ __main_block_invoke.115
+ __main_block_invoke.120
+ __main_block_invoke.134
+ __main_block_invoke.147
+ __main_block_invoke.156
+ __main_block_invoke.159
+ __main_block_invoke_2.162
+ __os_feature_enabled_impl
+ __os_signpost_emit_with_name_impl
+ __purge_orphans_block_invoke.239
+ _analyzePurgeableRecordsForApps
+ _climbDirStatHierarchy
+ _climbDirStatHierarchyForOwner
+ _dispatch_async
+ _dispatch_group_create
+ _dispatch_group_enter
+ _dispatch_group_leave
+ _dispatch_group_wait
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _ffsctl
+ _fsPurgeableSingleVolume
+ _fsgetpath
+ _objc_autorelease
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_shouldAnalyzeBundleMap
+ _objc_msgSend$_shouldAnalyzePartialClones
+ _objc_msgSend$_shouldAnalyzePurgeableClones
+ _objc_msgSend$analyzeClonesForVolume:urgency:error:
+ _objc_msgSend$bundleCloneInfo
+ _objc_msgSend$code
+ _objc_msgSend$dictionary
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$firstObject
+ _objc_msgSend$groupPurgeableClonesSize
+ _objc_msgSend$initWithOptions:
+ _objc_msgSend$initWithOptions:dirStatIDToBundleMap:tagHashToBundleIDMap:
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$lock
+ _objc_msgSend$longLongValue
+ _objc_msgSend$numberWithLongLong:
+ _objc_msgSend$prunerWithFileAge:dirAge:
+ _objc_msgSend$purgeableClonesSize
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$setBundleCloneInfo:
+ _objc_msgSend$setGroupPurgeableClonesSize:
+ _objc_msgSend$setPurgeableClonesSize:
+ _objc_msgSend$setTotalPurgeableClones:
+ _objc_msgSend$setTotalPurgeablePartialClones:
+ _objc_msgSend$setWithArray:
+ _objc_msgSend$stringValue
+ _objc_msgSend$totalPurgeableClones
+ _objc_msgSend$totalPurgeablePartialClones
+ _objc_msgSend$unlock
+ _objc_opt_class
+ _objc_opt_isKindOfClass
+ _objc_retain
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x26
+ _objc_retain_x28
+ _objc_retain_x3
+ _objc_sync_enter
+ _objc_sync_exit
+ _os_signpost_enabled
+ _os_signpost_id_make_with_pointer
+ _performSingleVolumePurgeWithInfo
- GCC_except_table16
- GCC_except_table2
- _OBJC_CLASS_$_NSConstantArray
- __RegisterCacheDeleteOrphanDirHandlerService_block_invoke.109
- ___block_descriptor_32_e51_B24?0r*8^{?=BBqiIQQQ{timespec=qq}{timespec=qq}B}16l
- ___periodic_block_invoke
- __block_literal_global.100
- __block_literal_global.106
- __block_literal_global.111
- __block_literal_global.123
- __block_literal_global.172
- __block_literal_global.51
- __block_literal_global.70
- __block_literal_global.83
- __block_literal_global.85
- __block_literal_global.92
- __block_literal_global.95
- __block_literal_global.98
- __main_block_invoke.47
- __main_block_invoke.48
- __main_block_invoke.53
- __main_block_invoke.67
- __main_block_invoke.81
- __main_block_invoke.90
- __main_block_invoke.93
- __main_block_invoke_2.96
- _objc_msgSend$numberWithBool:
- _objc_msgSend$objectForKey:
- _objc_msgSend$setObject:forKey:
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x25
- _os_variant_has_internal_diagnostics
CStrings:
+ ""
+ "!"
+ "%d purge_orphans urgency: %d, pruning /tmp/"
+ "%d purge_orphans urgency: %d, pruning tmp dirs"
+ "(none found)"
+ "/"
+ "@\"NSDictionary\""
+ "@24@0:8Q16"
+ "@36@0:8@16i24^@28"
+ "@40@0:8Q16@24@32"
+ "APFSPurgeCall"
+ "APP_PURGEABLE_SIZES"
+ "Analyze clones DONE for vol %@"
+ "BUNDLE_IDS"
+ "CACHE_DELETE_TOKEN"
+ "CACHE_DELETE_VOLUME_RESULTS"
+ "CDBundleCloneInfo"
+ "CDCloneAnalyzer"
+ "CDCloneInfo"
+ "CacheDelete"
+ "Clone analysis failed with errno %d: %s"
+ "DIR_STAT_ID_TO_BUNDLE_MAP"
+ "Failed to analyze clones for volume %s: %@"
+ "Failed to get purgeable records for volume %@ with error %s"
+ "FairPurging"
+ "Missing required parameters"
+ "No space could be purged at urgency %d across %lu volumes"
+ "PurgeSpecificApps purge returning: %@"
+ "PurgeSpecificApps purge: FairPurging feature flag is disabled, returning 0"
+ "PurgeSpecificApps purge: Missing required parameters"
+ "PurgeSpecificApps purgeable returning: %@"
+ "PurgeSpecificApps purgeable: FairPurging feature flag is disabled, returning 0"
+ "PurgeSpecificApps purgeable: Missing required parameters"
+ "PurgeSpecificApps: Cancel callback invoked - setting cancellation flag"
+ "Purged file %llu: %llu bytes (owner: %@)"
+ "Q"
+ "Requesting fsPurgeable for volume %{public}@ urgency %d with APFS_PURGEABLE urgency %0llx"
+ "Starting FS purgeable record analysis for volume: %@. Urgency: %d, shouldPurge: %s, purgeLimit: %llu, targetApps: %lu"
+ "T@\"NSDictionary\",&,N,V_bundleCloneInfo"
+ "TAG_HASH_TO_BUNDLE_ID_MAP"
+ "TQ,N,V_groupPurgeableClonesSize"
+ "TQ,N,V_purgeableClonesSize"
+ "TQ,N,V_totalPurgeableClones"
+ "TQ,N,V_totalPurgeablePartialClones"
+ "_bundleCloneInfo"
+ "_dirStatIDToBundleMap"
+ "_groupPurgeableClonesSize"
+ "_options"
+ "_purgeableClonesSize"
+ "_shouldAnalyzeBundleMap"
+ "_shouldAnalyzePartialClones"
+ "_shouldAnalyzePurgeableClones"
+ "_tagHashToBundleIDMap"
+ "_totalPurgeableClones"
+ "_totalPurgeablePartialClones"
+ "adjustBundleSizesForClones: Bundle %@ - Record: %llu, Purgeable clones: %llu, Group purgeable: %llu, Adjusted: %lld"
+ "adjustBundleSizesForClones: Bundle %@ adjustment resulted in negative size (%lld), keeping original. Record: %llu, Purgeable clones: %llu, Group purgeable: %llu"
+ "analyzeClonesForVolume:urgency:error:"
+ "analyzePurgeableRecordsForApps: Cancellation detected at file %llu of %llu, aborting"
+ "analyzePurgeableRecordsForApps: Cancellation detected before fsctl, aborting"
+ "analyzePurgeableRecordsForApps: Cancellation detected before purging file %llu, aborting"
+ "analyzePurgeableRecordsForApps: Clone analysis failed: %@, using unadjusted sizes"
+ "analyzePurgeableRecordsForApps: Failed to allocate memory for purgeable records"
+ "analyzePurgeableRecordsForApps: Operation was cancelled, completed partial work"
+ "analyzePurgeableRecordsForApps: Purge complete. totalPurged: %llu, purgeLimit: %llu, apps: %lu"
+ "analyzePurgeableRecordsForApps: Purge limit reached (%llu >= %llu), stopping"
+ "bundleCloneInfo"
+ "climbDirStatHierarchy: APFSIOC_DIR_STATS_OP for %llu returned errno %u (%s)"
+ "climbDirStatHierarchy: Finished checking dirstat key %llu"
+ "climbDirStatHierarchy: Found owner %@ for dirStatID %llu via parent %llu"
+ "climbDirStatHierarchy: Too many nested folders for dirStatID %llu"
+ "climbDirStatHierarchy: chained_key is pointing to itself dirKeyItr:%llu chained_key:%llu"
+ "climbDirStatHierarchy: dirStatID %llu not in SAF hierarchy"
+ "climbDirStatHierarchy: dir_stats entry is inconsistent for dirKeyItr:%llu"
+ "code"
+ "com.apple.CacheDelete.CloneAnalysis"
+ "com.apple.deleted_helper.purge_specific_apps"
+ "com.apple.deleted_helper.purge_specific_apps_queue"
+ "customerReleaseBuild IS SEED BUILD"
+ "dictionary"
+ "error=%{public}d errno=%{public}d actual_purged=%{public}llu"
+ "errorWithDomain:code:userInfo:"
+ "firstObject"
+ "fsPurge: Added per-volume results for %lu volumes"
+ "fsPurge: Added single volume result: %@ -> %llu bytes"
+ "fsPurge: Batch mode with %lu volumes"
+ "fsPurge: Concurrent processing completed, total purged: %llu bytes from %lu volumes"
+ "fsPurge: Root volume: %@"
+ "fsPurge: Starting concurrent processing for %lu volumes"
+ "fsPurge: Total %llu at urgency %d across %lu volumes (concurrent processing)"
+ "fsPurge: Volume %@ purged %llu bytes (allocated: %llu)"
+ "fsPurge: Volume %@ result: %llu bytes"
+ "fsPurge: Volume %@ starting with %llu bytes allocation"
+ "fsPurgeable volume: %{public}@, total: %lld bytes"
+ "fsPurgeable: Batch mode with %lu volumes"
+ "fsPurgeable: total %llu across %lu volumes (concurrent)"
+ "fsPurgeable: unable to map volume: %@"
+ "groupPurgeableClonesSize"
+ "initWithOptions:"
+ "initWithOptions:dirStatIDToBundleMap:tagHashToBundleIDMap:"
+ "localizedDescription"
+ "lock"
+ "longLongValue"
+ "numberWithLongLong:"
+ "performSingleVolumePurge: Starting purge on %@ for %llu bytes"
+ "performSingleVolumePurge: Volume %@ total purged %llu bytes"
+ "performSingleVolumePurge: fsctl failed on %@ with error: %s"
+ "performSingleVolumePurge: fsctl purged %llu bytes (all services)"
+ "performSingleVolumePurge: fsctl purged %llu bytes from service %@"
+ "performSingleVolumePurge: requesting %llu bytes (all services)"
+ "performSingleVolumePurge: requesting %llu bytes from service %@"
+ "purgeSingleFile: Failed to get path for inode %llu"
+ "purgeSingleFile: Failed to stat volume %@ with error %d (%s)"
+ "purgeSingleFile: Opening file %s for purge failed: %s (%d)"
+ "purgeSingleFile: Purged file %s (inode %llu), freed %lld bytes"
+ "purgeSingleFile: Purging file %s (inode %llu) failed: %s (%d)"
+ "purgeableClonesSize"
+ "removeAllObjects"
+ "service=%{public}s volume=%{public}s urgency=%{public}d requested=%{public}llu type=%{public}u flags=0x%{public}x"
+ "service=generic volume=%{public}s urgency=%{public}d requested=%{public}llu flags=0x%{public}x"
+ "setBundleCloneInfo:"
+ "setGroupPurgeableClonesSize:"
+ "setPurgeableClonesSize:"
+ "setTotalPurgeableClones:"
+ "setTotalPurgeablePartialClones:"
+ "setWithArray:"
+ "stringValue"
+ "totalPurgeableClones"
+ "totalPurgeablePartialClones"
+ "unlock"
+ "v24@0:8Q16"
- "%d fsPurge: purged: %llu, still need: %llu tries: %d"
- "%d fsPurge: purging: %llu"
- "%d purge_orphans urgency: %d, clearing /tmp/"
- "/tmp/"
- "/var/mobile/Library/AutoBugCapture/"
- "/var/mobile/Library/Logs/AutoBugCapture/"
- "APFSIOC_DIR_STATS_OP for %llu returned errno %u"
- "APFSIOC_PURGE_FILES failed: %@ at urgency %d (0x%x) on %s : %s"
- "Customer build, clearing %@"
- "Finished checking dirstat key %llu"
- "Reguesting fsPurgeable for urgency %d with APFS_PURGEABLE urgency %0llx"
- "chained_key is pointing to itself dirKeyItr:%lld chained_key:%lld"
- "com.apple.cache_delete"
- "customerReleaseBuild IS INTERNAL BUILD"
- "customerReleaseBuild IS NOT INTERNAL BUILD"
- "customerReleaseBuild IS NOT SEED BUILD"
- "dir_stats entry is inconsistent for dirKeyItr:%lld"
- "fsPurge: %llu at urgency %d (flags: 0x%x) on %{public}s (%{public}@)"
- "fsPurge: adding service %@ (%u), amount: %@"
- "fsPurge: amountPurged %llu postPurgeFreespace %llu prePurgeFreespace %llu"
- "numberWithBool:"
- "objectForKey:"
- "setObject:forKey:"
- "unable to get address of MGGetBoolAnswer"

```
