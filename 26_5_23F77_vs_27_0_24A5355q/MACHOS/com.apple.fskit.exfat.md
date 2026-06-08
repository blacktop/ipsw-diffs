## com.apple.fskit.exfat

> `/System/Library/ExtensionKit/Extensions/com.apple.fskit.exfat.appex/com.apple.fskit.exfat`

```diff

-522.100.20.0.0
-  __TEXT.__text: 0xfe28
-  __TEXT.__auth_stubs: 0x920
-  __TEXT.__objc_stubs: 0x7a0
-  __TEXT.__objc_methlist: 0x214
-  __TEXT.__const: 0x4cf3
-  __TEXT.__cstring: 0x34df
+560.0.0.0.0
+  __TEXT.__text: 0x120a4
+  __TEXT.__auth_stubs: 0x980
+  __TEXT.__objc_stubs: 0x760
+  __TEXT.__objc_methlist: 0x204
+  __TEXT.__const: 0x4d03
+  __TEXT.__cstring: 0x3e51
   __TEXT.__oslogstring: 0x581
-  __TEXT.__gcc_except_tab: 0x3c4
-  __TEXT.__objc_methname: 0x740
-  __TEXT.__objc_classname: 0x62
-  __TEXT.__objc_methtype: 0x343
-  __TEXT.__unwind_info: 0x2b0
-  __DATA_CONST.__auth_got: 0x4a0
-  __DATA_CONST.__got: 0xb0
-  __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x218
+  __TEXT.__gcc_except_tab: 0x32c
+  __TEXT.__objc_methname: 0x6fc
+  __TEXT.__objc_classname: 0x5f
+  __TEXT.__objc_methtype: 0x233
+  __TEXT.__unwind_info: 0x2e0
+  __DATA_CONST.__const: 0x370
   __DATA_CONST.__cfstring: 0x3c0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0x4d0
+  __DATA_CONST.__got: 0xb8
+  __DATA_CONST.__auth_ptr: 0x10
   __DATA.__objc_const: 0x278
-  __DATA.__objc_selrefs: 0x2c0
+  __DATA.__objc_selrefs: 0x2b0
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0x48e8
-  __DATA.__bss: 0x2018
-  __DATA.__common: 0x1e8
+  __DATA.__data: 0x4938
+  __DATA.__thread_vars: 0x60
+  __DATA.__thread_bss: 0x40
+  __DATA.__bss: 0xa4
+  __DATA.__common: 0x2b0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: B5B880DC-DDAE-344F-B9F3-5C15956A7E87
-  Functions: 264
-  Symbols:   341
-  CStrings:  586
+  UUID: 0D9459C6-E5A6-306C-AD61-89C419099565
+  Functions: 276
+  Symbols:   408
+  CStrings:  599
 
Symbols:
+ _CONV_NormalizeUnistr255ToPrecomposed
+ __dispatch_queue_attr_concurrent
+ __tlv_bootstrap
+ _buffer_data_and_length
+ _dispatch_group_async
+ _dispatch_queue_create
+ _dispatch_release
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _dispatch_sync
+ _dup
+ _fsckBitmapTooSmall_args
+ _fsckBlockSizeTooLarge_args
+ _fsckChainTooFewClusters_args
+ _fsckChainTooManyClusters_args
+ _fsckClusterInvalid_args
+ _fsckClusterOverlap_args
+ _fsckCorruptFilesDirectory_args
+ _fsckCouldNotCreateBitmapCacheFile_args
+ _fsckCouldNotReadClusterFromFAT_args
+ _fsckCouldNotReadCluster_args
+ _fsckCouldNotReleaseBuffer_args
+ _fsckCouldNotTruncateBitmapCacheFile_args
+ _fsckCouldNotUnlinkBitmapCacheFile_args
+ _fsckDeviceBlockSizeMismatch_args
+ _fsckDirectoryZeroLength_args
+ _fsckDuplicateNameInDirectory_args
+ _fsckEmptyStreamHasClusters_args
+ _fsckEntriesBeyondEndOfDir_args
+ _fsckFileFolderDamage_args
+ _fsckFileFolderNotRepaired_args
+ _fsckFileHasNoStreamEntry_args
+ _fsckFileUnexpectedSecondaryEntry_args
+ _fsckIncompleteDirEntrySet_args
+ _fsckInformation_args
+ _fsckInvalidFileNameLength_args
+ _fsckInvalidFileName_args
+ _fsckLostFoundDirectory_args
+ _fsckNameHasInvalidCharacters_args
+ _fsckPrintAndAskPrompt
+ _fsckProgress_args
+ _fsckRepairSuccessful_args
+ _fsckStartClusterInvalid_args
+ _fsckStartClusterOverlap_args
+ _fsckStreamHasNoAllocation_args
+ _fsckUnexpectedBenignPrimaryEntry_args
+ _fsckUnexpectedCritPrimaryEntry_args
+ _fsckValidLenBiggerThanDataLen_args
+ _fsckVolumeCorruptNeedsRepair_args
+ _fsckVolumeCorruptNoRepair_args
+ _fsckVolumeNameIs_args
+ _fsckVolumeNotRepairedInUse_args
+ _fsckVolumeNotRepairedTries_args
+ _fsckVolumeNotRepaired_args
+ _fsckVolumeNotVerifiedInUse_args
+ _fsckVolumeOK_args
+ _fsckVolumeVerifyIncompleteNoRepair_args
+ _fsckVolumeVerifyIncomplete_args
+ _fsck_exfat_buf_init_thread
+ _fsck_exfat_dir_cluster_cache_dispose
+ _fsck_exfat_dir_cluster_cache_dispose_thread
+ _fsck_exfat_dir_cluster_cache_init
+ _fsck_exfat_dir_cluster_cache_init_thread
+ _fsck_exfat_dir_cluster_cache_update
+ _fsck_exfat_read_to_buf
+ _fsck_exfat_write_from_buf
+ _fsck_messages_common_count
+ _fsck_messages_exfat_count
+ _objc_claimAutoreleasedReturnValue
+ _pthread_mutex_destroy
+ _pthread_mutex_init
+ _pthread_mutex_lock
+ _pthread_mutex_unlock
+ _sfm_to_mac_len
+ _snprintf
- _CFArrayRemoveAllValues
- _CFSetAddValue
- _CFSetContainsValue
- _CFSetRemoveAllValues
- _fsck_exfat_dir_get_path
- _objc_release_x1
- _objc_retain
- _objc_retainAutoreleasedReturnValue
- _sprintf
CStrings:
+ "%08X: %02X should be %02X"
+ "%llu total sectors; %u bytes per sector"
+ "%u clusters starting at sector %u; %u bytes per cluster"
+ "%u clusters were marked free, but referenced"
+ "%u clusters were marked used and CLUST_BAD"
+ "%u clusters were marked used, but not referenced"
+ "--- [%d] Evicted %d buffers (%u bytes; %u pages)"
+ "B16@?0^(exfat_direntry=C{exfat_direntry_volname=CC[11{uint16le=S}][8C]}{exfat_direntry_upcase=C[3C]{uint32le=I}[12C]{uint32le=I}{uint64le=Q}}{exfat_direntry_bitmap=CC[18C]{uint32le=I}{uint64le=Q}}{exfat_direntry_guid=CC{uint16le=S}{uint16le=S}{exfat_guid={uint32le=I}{uint16le=S}{uint16le=S}[8C]}[10C]}{exfat_direntry_file=CC{uint16le=S}{uint16le=S}{uint16le=S}{uint32le=I}{uint32le=I}{uint32le=I}CCCCC[7C]}{exfat_direntry_stream=CCCC{uint16le=S}[2C]{uint64le=Q}[4C]{uint32le=I}{uint64le=Q}}{exfat_direntry_filename=CC[15{uint16le=S}]}{exfat_direntry_vendor=CC{exfat_guid={uint32le=I}{uint16le=S}{uint16le=S}[8C]}[14C]}{exfat_direntry_vendor_alloc=CC{exfat_guid={uint32le=I}{uint16le=S}{uint16le=S}[8C]}[2C]{uint32le=I}{uint64le=Q}}{exfat_direntry_generic_primary=CC{uint16le=S}{uint16le=S}[14C]{uint32le=I}{uint64le=Q}}{exfat_direntry_generic_secondary=CC[18C]{uint32le=I}{uint64le=Q}})8"
+ "B20@?0^(exfat_direntry=C{exfat_direntry_volname=CC[11{uint16le=S}][8C]}{exfat_direntry_upcase=C[3C]{uint32le=I}[12C]{uint32le=I}{uint64le=Q}}{exfat_direntry_bitmap=CC[18C]{uint32le=I}{uint64le=Q}}{exfat_direntry_guid=CC{uint16le=S}{uint16le=S}{exfat_guid={uint32le=I}{uint16le=S}{uint16le=S}[8C]}[10C]}{exfat_direntry_file=CC{uint16le=S}{uint16le=S}{uint16le=S}{uint32le=I}{uint32le=I}{uint32le=I}CCCCC[7C]}{exfat_direntry_stream=CCCC{uint16le=S}[2C]{uint64le=Q}[4C]{uint32le=I}{uint64le=Q}}{exfat_direntry_filename=CC[15{uint16le=S}]}{exfat_direntry_vendor=CC{exfat_guid={uint32le=I}{uint16le=S}{uint16le=S}[8C]}[14C]}{exfat_direntry_vendor_alloc=CC{exfat_guid={uint32le=I}{uint16le=S}{uint16le=S}[8C]}[2C]{uint32le=I}{uint64le=Q}}{exfat_direntry_generic_primary=CC{uint16le=S}{uint16le=S}[14C]{uint32le=I}{uint64le=Q}}{exfat_direntry_generic_secondary=CC[18C]{uint32le=I}{uint64le=Q}})8I16"
+ "Cannot allocate a buffer for iterating dir entries"
+ "Cannot allocate a buffer for iterating the directory"
+ "Cannot allocate a buffer for processing directory"
+ "Cannot allocate a buffer for scanning the root directory"
+ "Cannot create a generated name for %s"
+ "Checking bitmap cluster %u"
+ "Could not allocate dir cluster cache buffer"
+ "Could not allocate dir cluster cache buffer data"
+ "Could not allocate dir cluster cache thread buffer"
+ "Could not dup() file descriptor"
+ "Could not get directory buffer"
+ "Could not initialize bitmap mutex"
+ "Could not initialize cache mutex"
+ "Could not initialize message mutex"
+ "Could not initialize progress mutex"
+ "Could not read directory data from disk"
+ "Could not read from disk"
+ "Could not write to disk"
+ "Directory %s"
+ "Directory /"
+ "FAT starts at sector %u; size %u sectors"
+ "FSOPS_ReadBootSector: Cluster size not supported: %u"
+ "File      %s"
+ "Found active bitmap; first cluster %u, length %llu"
+ "Found upcase table; starting cluster %u, length %llu"
+ "Hash bitmap collision: index: %u"
+ "Partition offset was not initialized, setting to default value (%d)\n"
+ "QUICKCHECK ONLY; CORRUPTION FOUND"
+ "QUICKCHECK ONLY; FILESYSTEM CLEAN"
+ "QUICKCHECK ONLY; FILESYSTEM DIRTY"
+ "QUICKCHECK ONLY; FILESYSTEM MARKED CORRUPT"
+ "Read      offset = 0x%012llx  length = 0x%06lx"
+ "Renaming completed in %s"
+ "Renaming failed in %s"
+ "Renaming items in %s"
+ "Root directory starts at cluster %u"
+ "The volume %s could not be verified completely and cannot be repaired."
+ "The volume %s was found corrupt and cannot be repaired."
+ "Trying to read from an invalid cluster number"
+ "Trying to write to an invalid cluster number"
+ "Write     offset = 0x%012llx  length = 0x%06x"
+ "dirsToProcess.access"
+ "fsck_exfat_process_dir"
+ "fsck_exfat_recurse.work_queue"
+ "vm.memory_pressure = %u"
+ "vm.page_free_wanted = %u"
- "%08X: %02X should be %02X\n"
- "%llu total sectors; %u bytes per sector\n"
- "%u clusters starting at sector %u; %u bytes per cluster\n"
- "%u clusters were marked free, but referenced\n"
- "%u clusters were marked used and CLUST_BAD\n"
- "%u clusters were marked used, but not referenced\n"
- "--- [%d] Evicted %d buffers (%u bytes; %u pages)\n"
- "Cannot create a generated name for %s\n"
- "Checking bitmap cluster %u\n"
- "Could not write clusters for directory %s\n"
- "Directory %s\n"
- "Directory /\n"
- "FAT starts at sector %u; size %u sectors\n"
- "FSOPS_ReadBootSector: Cluster size not supported: %u\n"
- "File      %s\n"
- "Found active bitmap; first cluster %u, length %llu\n"
- "Found upcase table; starting cluster %u, length %llu\n"
- "Hash bitmap collision: index: %u\n"
- "Partition offset was not initialized , setting to default value (%d)\n"
- "QUICKCHECK ONLY; CORRUPTION FOUND\n"
- "QUICKCHECK ONLY; FILESYSTEM CLEAN\n"
- "QUICKCHECK ONLY; FILESYSTEM DIRTY\n"
- "QUICKCHECK ONLY; FILESYSTEM MARKED CORRUPT\n"
- "Read      offset = 0x%012llx  length = 0x%06lx\n"
- "Renaming completed in %s\n"
- "Renaming failed in %s\n"
- "Renaming items in %s\n"
- "Root directory starts at cluster %u\n"
- "S24@0:8^{exfat_file_entry_set={exfat_direntry_file=CC{uint16le=S}{uint16le=S}{uint16le=S}{uint32le=I}{uint32le=I}{uint32le=I}CCCCC[7C]}{exfat_direntry_stream=CCCC{uint16le=S}[2C]{uint64le=Q}[4C]{uint32le=I}{uint64le=Q}}[254{exfat_direntry_filename=CC[15{uint16le=S}]}]}16"
- "The volume %s could not be verified completely and can not be repaired."
- "The volume %s was found corrupt and can not be repaired."
- "Write     offset = 0x%012llx  length = 0x%06x\n"
- "dir->refs != 0"
- "dir->refs > 0"
- "fsck_exfat_dir_ref"
- "fsck_exfat_dir_rele"
- "fsck_exfat_recurse"
- "getDirEntrySetChecksum:"
- "logLocalizedMessage:table:bundle:arguments:"
- "path != NULL"
- "vm.memory_pressure = %u\n"
- "vm.page_free_wanted = %u\n"

```
