## libramrod.dylib

> `/usr/lib/libramrod.dylib`

```diff

-3476.120.8.0.2
-  __TEXT.__text: 0xdc3d0
-  __TEXT.__auth_stubs: 0x2920
-  __TEXT.__objc_methlist: 0x117c
-  __TEXT.__cstring: 0x290ab
-  __TEXT.__const: 0x94a48
-  __TEXT.__gcc_except_tab: 0xba4
+3689.0.0.0.1
+  __TEXT.__text: 0xef0e8
+  __TEXT.__objc_methlist: 0x1194
+  __TEXT.__cstring: 0x2bb76
+  __TEXT.__const: 0x94f98
+  __TEXT.__gcc_except_tab: 0xb2c
   __TEXT.__oslogstring: 0xab4
-  __TEXT.__unwind_info: 0x1d90
-  __TEXT.__eh_frame: 0x370
-  __TEXT.__objc_classname: 0x195
-  __TEXT.__objc_methname: 0x29a2
-  __TEXT.__objc_methtype: 0xb65
-  __TEXT.__objc_stubs: 0x28c0
-  __DATA_CONST.__got: 0x2d0
-  __DATA_CONST.__const: 0x1f98
+  __TEXT.__unwind_info: 0x1ea0
+  __TEXT.__eh_frame: 0x378
+  __TEXT.__objc_stubs: 0x2900
+  __TEXT.__auth_stubs: 0x2af0
+  __TEXT.__objc_classname: 0x18b
+  __TEXT.__objc_methname: 0x29d3
+  __TEXT.__objc_methtype: 0xb58
+  __DATA_CONST.__const: 0x1f78
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xcb8
-  __AUTH_CONST.__auth_got: 0x14a8
-  __AUTH_CONST.__const: 0x2020
-  __AUTH_CONST.__cfstring: 0xbae0
+  __DATA_CONST.__weak_got: 0x8
+  __DATA_CONST.__objc_selrefs: 0xcc8
+  __DATA_CONST.__got: 0x2c0
+  __AUTH_CONST.__const: 0x2068
+  __AUTH_CONST.__cfstring: 0xc360
   __AUTH_CONST.__objc_const: 0x1ad0
+  __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__auth_got: 0x1580
   __AUTH.__objc_data: 0x5a0
   __AUTH.__data: 0x318
   __DATA.__objc_classrefs: 0x128
   __DATA.__objc_superrefs: 0x80
   __DATA.__objc_ivar: 0x138
-  __DATA.__data: 0x2198
-  __DATA.__bss: 0x878
+  __DATA.__data: 0x2598
+  __DATA.__bss: 0x888
   __DATA.__common: 0x38
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libutil.dylib
   - /usr/lib/libz.1.dylib
   - /usr/lib/updaters/libAppleTypeCRetimerUpdater.dylib
-  UUID: E60B401D-CC18-376C-BA71-B83143D31871
-  Functions: 2754
-  Symbols:   1831
-  CStrings:  7477
+  - /usr/lib/updaters/libBMCMCUUpdater.dylib
+  UUID: 1D86C1AD-858F-3D33-BF4A-81A230B26F23
+  Functions: 2867
+  Symbols:   1883
+  CStrings:  7948
 
Symbols:
+ _BMCMCUUpdaterCleanupDeviceInfo
+ _BMCMCUUpdaterGetDeviceInfo
+ _BMCMCUUpdaterUpdateDevice
+ _CFArrayApplyFunction
+ _CFDataSetLength
+ _CFURLCopyAbsoluteURL
+ _CFURLCreateCopyDeletingLastPathComponent
+ _CFURLCreateFromFileSystemRepresentation
+ _CFURLHasDirectoryPath
+ _ParallelArchiveWriteDirContents
+ _ParallelArchiveWriteEntryData
+ _ParallelArchiveWriteEntryHeader
+ _ParallelArchiveWriterCreate
+ _ParallelArchiveWriterCreateLegacy
+ _ParallelArchiveWriterDestroy
+ _ParallelCompressionAFSCFixupMetadataEx
+ _RAMROD_UPDATE_OPT_BMC_MCU_RESET
+ _RAMROD_UPDATE_OPT_STOCKHOLM_DISABLE_ENFORCEMENT
+ _RAMROD_UPDATE_OPT_STOCKHOLM_HASH_OVERRIDE
+ _RAMROD_UPDATE_OPT_STOCKHOLM_LOCK_PAGE
+ _RAMROD_UPDATE_OPT_UPDATE_BMC_MCU
+ _acl_get_entry
+ _acl_get_file
+ _acl_get_flag_np
+ _acl_get_permset_mask_np
+ _acl_get_qualifier
+ _acl_get_tag_type
+ _archive_dir
+ _backtrace
+ _bsearch
+ _cleanIOServiceConnection
+ _dladdr
+ _fgets
+ _getgrgid_r
+ _getpwuid_r
+ _getxattr
+ _hardware_folder_data_files_commit
+ _hardware_folder_files_data_create
+ _initializeIOServiceConnectionWithName
+ _kImg4TagStr_bmcf
+ _kImg4TagStr_lpmc
+ _mbr_sid_to_string
+ _mbr_uuid_to_id
+ _mbr_uuid_to_sid
+ _objc_retainAutoreleaseReturnValue
+ _performCommand
+ _persistent_hardware_files_commit
+ _persistent_hardware_files_create
+ _qsort
+ _qsort_r
+ _ramrod_device_supports_precommit_iboot
+ _ramrod_device_supports_provisional_nonces
+ _ramrod_hardware_partition_supports_ecc_persistence
+ _readlink
+ _realloc
- ___NSArray0__
- _pthread_cond_broadcast
- _ramrod_splat_object_image_patch_tag
CStrings:
+ "#%-2d 0x%016lx %s + %td (%s)\n"
+ "#%-2d 0x%016lx <unknown>\n"
+ "%12llu bytes in regular files (%.2f %cB)\n"
+ "%12llu clone clusters\n"
+ "%12llu clone entries\n"
+ "%12llu hard link clusters\n"
+ "%12llu hard link entries\n"
+ "%12llu redundant bytes in clones\n"
+ "%12llu redundant bytes in hard links\n"
+ "%12llu redundant bytes in same data files\n"
+ "%12llu same data clusters\n"
+ "%12llu same data entries\n"
+ "%12u entries in archive tree\n"
+ "%12u entries in index\n"
+ "%12u entries selected\n"
+ "%12zu FIFO\n"
+ "%12zu block special entries\n"
+ "%12zu character special entries\n"
+ "%12zu directories\n"
+ "%12zu entries reported an error\n"
+ "%12zu entries selected\n"
+ "%12zu entries with ACL blob\n"
+ "%12zu entries with XAT blob\n"
+ "%12zu regular files\n"
+ "%12zu sockets\n"
+ "%12zu symbolic links\n"
+ "%@/bic"
+ "%@/dramecc"
+ "%@/history"
+ "%@/lac"
+ "%@/srvo"
+ "%@/testfile1"
+ "%@:%@"
+ "%d battery data files were unable to be preserved\n"
+ "%d files failed to write to NAND\n"
+ "%lu files found in total.\n"
+ "%s Updater: Forcing Repersonalization due to restore option.\n"
+ "%s: %lu files found in total.\n"
+ "%s: %s failed\n"
+ "%s: AMSupportCreateDataFromFileURL failed with %d on file %s\n"
+ "%s: AMSupportCreateDataFromFileURL succeeded but returned NULL Data on file %d\n"
+ "%s: Attempting to recreate directory %s\n"
+ "%s: Attempting to recreate file %s\n"
+ "%s: Attempting to save stat info and data for file to memory: %s\n"
+ "%s: Directory(%s) closed\n"
+ "%s: Directory(%s) opened\n"
+ "%s: Failed to allocate memory for fileInfo struct\n"
+ "%s: Failed to create directory %s\n"
+ "%s: Failed to get file name for %@"
+ "%s: Failed to stat %s(%s)..skipping"
+ "%s: File %s: %lu bytes read into memory.\n"
+ "%s: File %s: Size %lu is larger than max (%lu) - discarding to avoid crashing.\n"
+ "%s: Initializing Array\n"
+ "%s: Manifest does not contain %s (%s)\n"
+ "%s: No files/folders found\n"
+ "%s: Only saving stat info for directory: %s\n"
+ "%s: Payload not found for %s (%s): %d %s\n"
+ "%s: Successfully created directory %s\n"
+ "%s: bad argument - no options"
+ "%s: copy_available_fud_image_names returned NULL"
+ "%s: failed to copy fud data for: %@"
+ "%s: failed to get device name and tag from %s\n"
+ "%s: failed to open dir: %s\n"
+ "%zu failed entries reported"
+ "- %s\n"
+ ".\n"
+ "./"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/ParallelCompression/Common/BlobBuffer.c"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/ParallelCompression/Common/StringTable.c"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/ParallelCompression/ParallelArchive/ArchiveTree.c"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/ParallelCompression/ParallelArchive/Write.c"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/ParallelCompression/ParallelArchive/WriteDirContents.c"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Pearl_Kernel/PearlSupport/PearlSupportUtils.m"
+ "/usr/lib/updaters/libBMCMCUUpdater.dylib"
+ "40A0DDD2-77F8-4392-B4A3-1E7304206516"
+ "ACL blob [%zu] stored for %s\n"
+ "AMSupportCreateDataFromFileURL succeeded but returned NULL Data\n"
+ "AMSupportFileURLExists failed with %d\n"
+ "AMSupportFileURLExists failed with %d on file %d\n"
+ "ArchiveTree append"
+ "ArchiveTreeCreateFromArchive"
+ "ArchiveTreeCreateFromDirectory"
+ "ArchiveTreeCreateFromIndex"
+ "ArchiveTreeCreateWithRootEntry"
+ "ArchiveTreeInsert"
+ "ArchiveTreeMergeAndDestroy"
+ "ArchiveTreePrune"
+ "AssertMacros: %s (value = 0x%lx), %s file: %s, line: %d\n"
+ "B48@0:8*16^{__CFDictionary=}24@32^^{__CFError}40"
+ "BMC MCU Chassis Reset"
+ "BMCMCU"
+ "BMCMCUUpdaterGetDeviceInfo"
+ "BTM"
+ "Bad parameter to hardware_folder_files_data_create, outArray is NULL\n"
+ "Bad parameter, inArray is NULL\n"
+ "Bad parameter, inDict is NULL\n"
+ "Bad parameter, options is NULL\n"
+ "Bad parameter, outDict is NULL\n"
+ "BlobBufferIncreaseCapacity"
+ "BlobBufferStore"
+ "Broken pipeline"
+ "CFArrayCreateMutable failed"
+ "CFStringCreateWithCString"
+ "CFURLCreateCopyDeletingLastPathComponent failed\n"
+ "CFURLGetFileSystemRepresentation failed\n"
+ "CLC"
+ "CTM"
+ "ChunkPipelineCreate"
+ "ChunkPipelineDestroy"
+ "Could not find: %s, skipping update\n"
+ "Create chunk pipeline"
+ "DisableBootMeasurementEnforcement"
+ "ERR"
+ "EYP"
+ "Failed to allocate myURL\n"
+ "Failed to allocate outDirectories\n"
+ "Failed to allocate pathURL\n"
+ "Failed to allocate persistentFiles\n"
+ "Failed to lookup device tree property: %s\n"
+ "Failed to set persistent file data for file %@\n"
+ "File %s: %lu bytes read into memory.\n"
+ "File %s: Can't stat file.\n"
+ "File %s: Size %llu is larger than max (%llu) - discarding to avoid crashing.\n"
+ "File %s: failed to archive directory.\n"
+ "File %s: failed to read file: %d.\n"
+ "File %s: not a file or directory.\n"
+ "File %s: not found.\n"
+ "File %s: wrote out %lu bytes.\n"
+ "File comparison failed: %s vs %s"
+ "Flush chunk pipeline"
+ "HLC"
+ "IODTNVRAMVariables"
+ "IONameMatch"
+ "IORegistryEntryCreateCFProperties failed: %x\n"
+ "IS"
+ "LockFactoryPage"
+ "LynxSerialNumber"
+ "NFCBootHashOverride"
+ "NOT"
+ "Not overwriting existing file.\n"
+ "Not overwriting file in stage1.\n"
+ "Options.ForceRepersonalization"
+ "PRC"
+ "ParallelArchiveWriteDirContents"
+ "ParallelArchiveWriteEntryData"
+ "ParallelArchiveWriteEntryHeader"
+ "ParallelArchiveWriterCreate"
+ "ParallelCompressionAFSCFixupMetadataEx"
+ "Payload too large: %zu B received / %llu B expected"
+ "Pipeline failed"
+ "Pipeline failed: using in-thread compression"
+ "Running %u threads to expand %u nodes (%u per thread)\n"
+ "SLC"
+ "SharedArrayPush: pthread_cond_signal failed\n"
+ "Stockholm Disable Enforcement"
+ "Stockholm Hash Override"
+ "Stockholm Lock Page"
+ "StringTableAppend"
+ "StringTableAppendArray"
+ "StringTableAppendFile"
+ "StringTableAppendTable"
+ "StringTableClone"
+ "StringTableCreate"
+ "StringTableGetCFArray"
+ "StringTableSort"
+ "SupportsLEDAging"
+ "SystemAudioVolume"
+ "SystemAudioVolumeExtension"
+ "Thread reported an error"
+ "Unable_to_get_file_name"
+ "Warning: ACL tag type is not ALLOW/DENY (ignoring entry): %d\n"
+ "Write chunk"
+ "WriteAlignedChunkProc"
+ "XAT blob [%zu] stored for %s\n"
+ "XAT value is too long to be stored in YAA archive (%zd B): %s"
+ "YAA1xx"
+ "[%d] Entry processing thread starting\n"
+ "[%d] processing entry %s\n"
+ "[%d] terminating\n"
+ "[%s] archive dir failed 0x%llx\n"
+ "[%s] final data is %lu bytes\n"
+ "[%s] write %llu bytes\n"
+ "_connect != ((io_object_t) 0)"
+ "_hardware_folder_data_write_file"
+ "_write_archive_data"
+ "acl_get_permset_mask_np"
+ "acl_get_qualifier"
+ "acl_get_tag_type"
+ "alloc writer buffer"
+ "allocating YAF buffer"
+ "allow-sealer-hash-mismatch"
+ "allow-sealer-hash-mismatch is set. Hash mismatch may panic!\n"
+ "append expandDirRange output to main tree"
+ "archive tree creation"
+ "archiveTreeAppend"
+ "archiveTreeAppendTree"
+ "archiveTreeCreate"
+ "archiveTreeFindPath"
+ "archiveTreeFromArchiveBlobProc"
+ "archiveTreeFromArchiveEndProc"
+ "archiveTreeFromArchivePayloadProc"
+ "archiveTreeFromIndexBeginProc"
+ "archiveTreePackNodes"
+ "archiveTreeRemapNodes"
+ "archiveTreeReserve"
+ "archiveTreeSort"
+ "archiveTreeSortStringTable"
+ "archiveTreeUpdateChilds"
+ "archiveTreeUpdateDepth"
+ "archiveTreeUpdateNodeDepth"
+ "archive_dir"
+ "boot-args"
+ "boot-volume"
+ "bootdelay"
+ "building archive tree"
+ "building full path from includePaths"
+ "chassis-disable-throttle"
+ "chassis-platform-id"
+ "chassis-slot-id"
+ "collecting YAF buffer"
+ "connect"
+ "copy header extra fields"
+ "create expandDir thread"
+ "creating resolve thread"
+ "dataInfo->setCount <= (4)"
+ "debug-uarts"
+ "device has no BMC MCU, skipping update\n"
+ "ecc-db-hw-partition-size"
+ "encode ACL field"
+ "encode BTM field"
+ "encode CKS field"
+ "encode CLC field"
+ "encode CTM field"
+ "encode DAT field"
+ "encode DEV field"
+ "encode ERR field"
+ "encode EYP field"
+ "encode FLG field"
+ "encode GID field"
+ "encode HLC field"
+ "encode INO field"
+ "encode LNK field"
+ "encode MOD field"
+ "encode MTM field"
+ "encode PAT field"
+ "encode PRC field"
+ "encode SH1 field"
+ "encode SH2 field"
+ "encode SIZ field"
+ "encode SLC field"
+ "encode TYP field"
+ "encode UID field"
+ "encode XAT field"
+ "encode header field"
+ "encoding ACE"
+ "entry is missing IDX field: %s"
+ "entry path too long"
+ "expand directory"
+ "expandDir"
+ "expandDirRange"
+ "expandDirRangeThreadProc"
+ "expanding archive tree range"
+ "extra data: %s"
+ "extra header data size doesn't match expected value"
+ "extra header field is too large for processing thread buffer"
+ "file type is not supported (st_mode=0%o): %s"
+ "full entry path is too long"
+ "full path too long"
+ "generating entry header"
+ "getting node path"
+ "getting string from includePaths"
+ "getxattr"
+ "hardware_folder_files_data_create"
+ "hw.perflevel1.physicalcpu"
+ "iBICEnableTestfile"
+ "iboot-failure-reason"
+ "include path doesn't exist, or is not a directory: %s"
+ "increasing XAT buffer capacity: %s"
+ "increasing archive tree storage"
+ "increasing blob capacity failed"
+ "increasing string table capacity"
+ "init available_threads"
+ "init entry_ready"
+ "inserting XAT xname: %s"
+ "inserting XAT xsize: %s"
+ "inserting new node"
+ "inserting new root name string"
+ "inserting root entry"
+ "inserting root node"
+ "inserting string"
+ "inserting tree node"
+ "insertion failed in string table"
+ "invalid entry type: %s"
+ "invalid extra field key: %s"
+ "invalid inDir"
+ "invalid inDir length"
+ "invalid input for ArchiveTreeInsert"
+ "invalid new index"
+ "invalid new node index"
+ "invalid path"
+ "invalid prune operation: more than one node at depth %u"
+ "invalid size increase"
+ "invalid string"
+ "invalid thread_id stored in entry"
+ "join expandDir thread"
+ "joining resolve thread"
+ "libBMCMCUUpdater.dylib"
+ "looking up parent node"
+ "looking up parent path failed"
+ "lstat %s"
+ "lzraven"
+ "mem-db-hw-partition-size"
+ "merging string tables"
+ "merging trees"
+ "moving thread data to main state"
+ "node has a first child, but no last child"
+ "open failed (%d): %s"
+ "opendir %s"
+ "options-system"
+ "ota-brain-version"
+ "ota-breadcrumbs"
+ "ota-context"
+ "ota-controllerVersion"
+ "ota-failure-reason"
+ "ota-forced-reset-uptime"
+ "ota-initial-failure-reason"
+ "ota-initial-forced-reset-uptime"
+ "ota-initial-result"
+ "ota-install-tonight"
+ "ota-reboot-retry-enabled"
+ "ota-result"
+ "ota-retry-failure-reason"
+ "ota-retry-result"
+ "ota-snapshot-update"
+ "ota-updateType"
+ "outConnect"
+ "parent node was not processed first"
+ "parsing archive"
+ "parsing index"
+ "path too long"
+ "path too long: %s/%s"
+ "persistentFile is NULL\n"
+ "persistent_files_create has nothing to persist.\n"
+ "processEntryThreadProc"
+ "processing failed for entry %zd\n"
+ "ramrod_NVRAM_has_system_namespace: system namespace %s present\n"
+ "ramrod_create_directory failed: %s\n"
+ "ramrod_unarchive_dir failed: %s\n"
+ "ramrod_write_data_to_file_with_class failed with %d\n"
+ "ramrod_write_data_to_file_with_class failed with %d: %s\n"
+ "read failed (%d): %s"
+ "readdir on dataless directory: %s"
+ "readlink returned an empty string: %s"
+ "recovery-boot-mode"
+ "recovery-breadcrumbs"
+ "remapping nodes"
+ "remapping tree nodes"
+ "resolveSameThreadProc"
+ "resolving ACE qualifier: %s"
+ "restore-retry-enabled"
+ "restored-host-timeout"
+ "root-live-fs"
+ "scan_directory"
+ "sendFailureEntry"
+ "sending failure info"
+ "serviceName"
+ "skip dataless dir: %s"
+ "skip mounted dir: %s"
+ "snap-provisional-nonces"
+ "snap-supports-precommit"
+ "sock %3d: received EOF"
+ "sock %3d: recv(%lu) failed: unexpected EOF"
+ "sort string table"
+ "sorting string table"
+ "sorting tree"
+ "starting task"
+ "stat failed: %s"
+ "store AUX in depth"
+ "storing ACL"
+ "storing XAT"
+ "storing depth in AUX"
+ "storing encoded extra fields"
+ "storing extra fields data"
+ "storing link"
+ "storing node depth in AUX"
+ "string table creation"
+ "string table sorting"
+ "string too long for StringTable"
+ "stringTableReserve"
+ "supportsProvisionalNonces"
+ "supportsiBootPrecommit"
+ "target-uuid"
+ "tree has a first root, but no last root"
+ "truncated data: %s"
+ "truncated entry payload: %llu B missing"
+ "update node depth"
+ "update parent depth"
+ "update-volume"
+ "update_bmc_mcu"
+ "updating depth field"
+ "updating tree depth"
+ "upgrade-fallback-boot-command"
+ "upgrade-manifest-hash"
+ "waiting for an available worker"
+ "write DAT 0x00, w=%zu: %s"
+ "write DAT, w=%zu: %s"
+ "write entry ACL"
+ "write entry XAT"
+ "write extra fields data"
+ "writing data"
+ "writing header"
+ "writing raw header"
+ "yaa_writeRawEntryHeader"
- "%s: Payload not found (%s): %d %s\n"
- "%s: segment_data_array failed to allocate"
- "AspYltP/iGWg0qxfg7c/3w"
- "B48@0:8*16^{__CFDictionary=}24r^^{__CFArray}32^^{__CFError}40"
- "ParallelCompressionAFSCFixupMetadata"
- "SharedArrayPush: pthread_cond_broadcast failed\n"
- "cryptex-app"
- "cryptex-system-arm64e"
- "r5pA2qLgR86BQKwgMjPWzg"
- "sock %3d: recv(%lu) failed: connection closed"

```
