## deleted_helper

> `/System/Library/PrivateFrameworks/CacheDelete.framework/deleted_helper`

```diff

-747.120.2.0.0
-  __TEXT.__text: 0x349c
-  __TEXT.__auth_stubs: 0x520
-  __TEXT.__objc_stubs: 0x360
-  __TEXT.__const: 0xfc
-  __TEXT.__gcc_except_tab: 0x94
-  __TEXT.__cstring: 0x5a7
-  __TEXT.__oslogstring: 0x8a8
-  __TEXT.__objc_classname: 0x1
-  __TEXT.__objc_methname: 0x1d5
-  __TEXT.__unwind_info: 0xd0
-  __DATA_CONST.__auth_got: 0x2a0
-  __DATA_CONST.__got: 0x50
-  __DATA_CONST.__const: 0x300
-  __DATA_CONST.__cfstring: 0x300
+795.0.0.502.1
+  __TEXT.__text: 0x56a8
+  __TEXT.__auth_stubs: 0x650
+  __TEXT.__objc_stubs: 0x5a0
+  __TEXT.__objc_methlist: 0xd4
+  __TEXT.__const: 0x14c
+  __TEXT.__gcc_except_tab: 0xf8
+  __TEXT.__objc_methname: 0x401
+  __TEXT.__cstring: 0x6eb
+  __TEXT.__oslogstring: 0xee9
+  __TEXT.__objc_classname: 0x15
+  __TEXT.__objc_methtype: 0x7a
+  __TEXT.__unwind_info: 0x110
+  __DATA_CONST.__auth_got: 0x338
+  __DATA_CONST.__got: 0x60
+  __DATA_CONST.__const: 0x3a0
+  __DATA_CONST.__cfstring: 0x440
+  __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x78
   __DATA_CONST.__objc_arraydata: 0xd0
-  __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_selrefs: 0xd8
+  __DATA_CONST.__objc_dictobj: 0x50
+  __DATA.__objc_const: 0x160
+  __DATA.__objc_selrefs: 0x1b8
+  __DATA.__objc_ivar: 0x10
+  __DATA.__objc_data: 0x50
   __DATA.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/MobileCoreServices.framework/MobileCoreServices
+  - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B7360EFF-E889-305D-BFBD-DE3C88D15949
-  Functions: 24
-  Symbols:   180
-  CStrings:  141
+  UUID: 3982B6E3-F70C-3276-9968-6C5DA0E2A239
+  Functions: 46
+  Symbols:   260
+  CStrings:  244
 
Symbols:
+ +[CacheDeletePruner prunerWithFileAge:dirAge:]
+ -[CacheDeletePruner .cxx_destruct]
+ -[CacheDeletePruner cancel]
+ -[CacheDeletePruner dir_age]
+ -[CacheDeletePruner file_age]
+ -[CacheDeletePruner initWithFileAge:dirAge:]
+ -[CacheDeletePruner pruneContainerTmps]
+ -[CacheDeletePruner pruneDir:bundleID:]
+ -[CacheDeletePruner pruneSystemTmp]
+ -[CacheDeletePruner pruneUserTmp]
+ -[CacheDeletePruner setCancel:]
+ -[CacheDeletePruner setDir_age:]
+ -[CacheDeletePruner setFile_age:]
+ -[CacheDeletePruner setTestObject:]
+ -[CacheDeletePruner stop]
+ -[CacheDeletePruner testObject]
+ GCC_except_table16
+ GCC_except_table7
+ OBJC_IVAR_$_CacheDeletePruner._cancel
+ OBJC_IVAR_$_CacheDeletePruner._dir_age
+ OBJC_IVAR_$_CacheDeletePruner._file_age
+ OBJC_IVAR_$_CacheDeletePruner._testObject
+ _APFSVolumeUpdateBounds
+ _OBJC_CLASS_$_AppCache
+ _OBJC_CLASS_$_CacheDeletePruner
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSObject
+ _OBJC_METACLASS_$_CacheDeletePruner
+ _OBJC_METACLASS_$_NSObject
+ __39-[CacheDeletePruner pruneDir:bundleID:]_block_invoke.16
+ __39-[CacheDeletePruner pruneDir:bundleID:]_block_invoke_2.17
+ __OBJC_$_CLASS_METHODS_CacheDeletePruner
+ __OBJC_$_INSTANCE_METHODS_CacheDeletePruner
+ __OBJC_$_INSTANCE_VARIABLES_CacheDeletePruner
+ __OBJC_$_PROP_LIST_CacheDeletePruner
+ __OBJC_CLASS_RO_$_CacheDeletePruner
+ __OBJC_METACLASS_RO_$_CacheDeletePruner
+ __RegisterCacheDeleteOrphanDirHandlerService_block_invoke.106
+ ___39-[CacheDeletePruner pruneContainerTmps]_block_invoke
+ ___39-[CacheDeletePruner pruneDir:bundleID:]_block_invoke
+ ___39-[CacheDeletePruner pruneDir:bundleID:]_block_invoke_2
+ ___block_descriptor_32_e30_v24?0"NSError"8"NSString"16l
+ ___block_descriptor_40_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_40_e8_32s_e18_B16?0"AppCache"8ls32l8
+ ___block_descriptor_72_e8_32s40s48r_e51_B24?0r*8^{?=BBqiIQQQ{timespec=qq}{timespec=qq}B}16ls32l8s40l8r48l8
+ ___block_descriptor_80_e8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
+ __block_literal_global.103
+ __block_literal_global.108
+ __block_literal_global.120
+ __block_literal_global.80
+ __block_literal_global.89
+ __block_literal_global.92
+ __block_literal_global.95
+ __block_literal_global.97
+ __main_block_invoke.78
+ __main_block_invoke.87
+ __main_block_invoke.90
+ __main_block_invoke_2.93
+ __objc_empty_cache
+ _amountStillNeeded
+ _assert_group_cache_deletion
+ _dispatch_block_create_with_qos_class
+ _evaluateBoolProperty
+ _getDevBSDForUpdateVolume
+ _getPurgeableInfoByDirKey
+ _getReservedSizeFromUpdateVolume
+ _gettimeofday
+ _hasUserVolume
+ _notify_post
+ _objc_alloc
+ _objc_getProperty
+ _objc_msgSend$arrayWithObjects:count:
+ _objc_msgSend$cancel
+ _objc_msgSend$dataContainerURL
+ _objc_msgSend$dir_age
+ _objc_msgSend$enumerateAppCachesOnVolume:options:telemetry:block:
+ _objc_msgSend$fileSystemRepresentation
+ _objc_msgSend$file_age
+ _objc_msgSend$identifier
+ _objc_msgSend$initWithFileAge:dirAge:
+ _objc_msgSend$path
+ _objc_msgSend$pruneDir:bundleID:
+ _objc_msgSend$set
+ _objc_msgSend$setCancel:
+ _objc_msgSend$size
+ _objc_msgSend$stringByAppendingPathComponent:
+ _objc_msgSend$stringWithUTF8String:
+ _objc_msgSend$testObject
+ _objc_msgSend$unsignedLongValue
+ _objc_msgSendSuper2
+ _objc_retain_x20
+ _objc_retain_x23
+ _objc_retain_x24
+ _objc_retain_x9
+ _objc_setProperty_atomic
+ _objc_storeStrong
+ _releaseReservedSpaceFromUpdateVolume
+ _rmdir
+ _setiopolicy_np
+ _stat
- GCC_except_table15
- _OBJC_CLASS_$_NSConstantArray
- __RegisterCacheDeleteOrphanDirHandlerService_block_invoke.99
- ___block_descriptor_32_e50_B24?0r*8^{?=BBqiIQQQ{timespec=qq}{timespec=qq}}16l
- ___main_block_invoke_3
- ___periodic_block_invoke
- __block_literal_global.101
- __block_literal_global.113
- __block_literal_global.136
- __block_literal_global.73
- __block_literal_global.75
- __block_literal_global.85
- __block_literal_global.88
- __block_literal_global.90
- __block_literal_global.96
- __main_block_invoke.80
- __main_block_invoke.83
- __main_block_invoke_2.86
- _objc_retain_x28
- _os_variant_has_internal_diagnostics
- _shouldRetryPurge
CStrings:
+ " Decreasing reserved size to %lld cur_reserve_size: %lld amountToReserveOnUpdateVolume: %lld "
+ " Increasing reserved size to %lld cur_reserve_size: %lld amountToReserveOnUpdateVolume: %lld "
+ " Released %lld from update volume"
+ " failed to set reserve space %s: %d\n"
+ " not enough space to reserve.current freespace:%lld, need to reserve:%lld"
+ " releaseReservedSpaceFromUpdateVolume %lld"
+ " tenPercentOfDiskCapacity: %lld amountToReserve: %lld"
+ " tenPercentOfDiskCapacity: %lld maxReserveAmount: %lld"
+ "%@ /tmp/ size: %llu"
+ "%d ENTRY amountStillNeeded: %llu, urgency: %d, tries: %d, %@ freespace: %llu "
+ "%d EXIT amountStillNeeded: %llu (returning: %llu), urgency: %d, type: %@, tries: %d, %@ freespace: %llu"
+ "%d amountStillNeeded  freespaceGoal: %llu, tries: %d"
+ "%d amountStillNeeded: %llu, urgency: %d, type: %@, tries: %d, %@ freespace: %llu"
+ "%d fsPurge: purged: %llu, still need: %llu tries: %d"
+ "%d fsPurge: purging: %llu"
+ "%d pruneDir rmdir'ing %s"
+ "%d pruneDir unlink'ing %s"
+ ".cxx_destruct"
+ "/private/var"
+ "/private/var/mobile/tmp"
+ "/private/var/tmp"
+ "1"
+ "@\"TestTelemetry\""
+ "@16@0:8"
+ "@32@0:8d16d24"
+ "APFSIOC_CLONEGROUP_ITERATE failed with error %d (%s)"
+ "B"
+ "B16@0:8"
+ "B16@?0@\"AppCache\"8"
+ "B24@?0r*8^{?=BBqiIQQQ{timespec=qq}{timespec=qq}B}16"
+ "CACHE_DELETE_FACTOR_FOR_CENTRALIZED_PURGEABLE"
+ "CACHE_DELETE_FACTOR_FOR_PLUGIN_PURGEABLE"
+ "CACHE_DELETE_FREESPACE_GOAL"
+ "CACHE_DELETE_MAX_RESERVE_SPACE_AMOUNT"
+ "CACHE_DELETE_NOT_ENOUGH_SPACE_TO_RESERVE"
+ "CACHE_DELETE_RELEASE_SPACE"
+ "CACHE_DELETE_RESERVE_SPACE_AMOUNT"
+ "CACHE_DELETE_TOTAL_AVAILABLE"
+ "CACHE_DELETE_TOTAL_FSPURGEABLE"
+ "CacheDeletePruner"
+ "Checking filesystem purgeable amount for reserving %lld"
+ "Clone groups are not supported (error %d: %s). Falling back to clone mapping."
+ "Could not rmdir %s: %s\n"
+ "Failed to acquire termination assertion for '%@': %@"
+ "Failed to get total purgeable clones from clone groups (error %d: %s)"
+ "Failed to get total purgeable clones from clone mapping (error %d: %s)."
+ "Failed to malloc %llu bytes with error %d (%s)"
+ "Q16@0:8"
+ "Q32@0:8@16@24"
+ "T@\"TestTelemetry\",&,V_testObject"
+ "TB,V_cancel"
+ "Total FS Purgeable (%llu) < Total Purgeable Partial Clones (%llu)"
+ "Total Purgeable Partial Clones Size: (%llu)"
+ "Tq,N,V_dir_age"
+ "Tq,N,V_file_age"
+ "Unable to create /tmp/ path for %@"
+ "Unable to get root volume "
+ "Unknown attribute %u"
+ "_cancel"
+ "_dir_age"
+ "_file_age"
+ "_testObject"
+ "arrayWithObjects:count:"
+ "cancel"
+ "customerReleaseBuild IS SEED BUILD"
+ "dataContainerURL"
+ "dir_age"
+ "enumerateAppCachesOnVolume:options:telemetry:block:"
+ "failed to reduce the update volume size%s: %d\n"
+ "fileSystemRepresentation"
+ "file_age"
+ "gettimeofday failed: %s"
+ "got %@"
+ "identifier"
+ "init"
+ "initWithFileAge:dirAge:"
+ "path"
+ "pruneContainerTmps"
+ "pruneDir:bundleID:"
+ "pruneSystemTmp"
+ "pruneUserTmp"
+ "prunerWithFileAge:dirAge:"
+ "q"
+ "q16@0:8"
+ "set"
+ "setCancel:"
+ "setDir_age:"
+ "setFile_age:"
+ "setTestObject:"
+ "size"
+ "statfs returned %d. error: %d"
+ "stop"
+ "stringByAppendingPathComponent:"
+ "stringWithUTF8String:"
+ "testObject"
+ "tmp"
+ "totalfsPurgeable: %lld plugin purgeable: %lld centralizedPurgeFactor: %d pluginPurgeFactor: %d actualPurgeable %lld requestedReserve:%lld current reserved:%lld"
+ "unlink failed on %s : %s"
+ "unsignedLongValue"
+ "v16@0:8"
+ "v20@0:8B16"
+ "v24@0:8@16"
+ "v24@0:8q16"
+ "v24@?0@\"NSError\"8@\"NSString\"16"
- "/var/mobile/Library/AutoBugCapture/"
- "/var/mobile/Library/Logs/AutoBugCapture/"
- "APFS freed much less than reported - suggesting a retry. Actually Freed (%llu), Requested (%llu), Reported (%llu)."
- "B24@?0r*8^{?=BBqiIQQQ{timespec=qq}{timespec=qq}}16"
- "Customer build, clearing %@"
- "com.apple.cache_delete"
- "customerReleaseBuild IS INTERNAL BUILD"
- "customerReleaseBuild IS NOT INTERNAL BUILD"
- "customerReleaseBuild IS NOT SEED BUILD"
- "statfs returned %d"
- "unable to get address of MGGetBoolAnswer"

```
