## apfs_vol_converter

> `/System/Library/Filesystems/apfs.fs/apfs_vol_converter`

```diff

-2235.0.13.0.0
-  __TEXT.__text: 0x52430
-  __TEXT.__auth_stubs: 0x920
+2235.40.9.0.1
+  __TEXT.__text: 0x534e8
+  __TEXT.__auth_stubs: 0x960
   __TEXT.__init_offsets: 0x4
-  __TEXT.__cstring: 0x109d8
+  __TEXT.__cstring: 0x113ac
   __TEXT.__const: 0x168
-  __TEXT.__gcc_except_tab: 0x368
-  __TEXT.__unwind_info: 0xb04
+  __TEXT.__gcc_except_tab: 0x4ec
+  __TEXT.__unwind_info: 0xb64
   __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__auth_got: 0x498
+  __DATA_CONST.__auth_got: 0x4b8
   __DATA_CONST.__got: 0x70
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x7a0
-  __DATA_CONST.__cfstring: 0xa20
-  __DATA.__data: 0x360
-  __DATA.__bss: 0x5c
-  __DATA.__common: 0x744
+  __DATA_CONST.__const: 0x800
+  __DATA_CONST.__cfstring: 0xb00
+  __DATA.__data: 0x368
+  __DATA.__bss: 0x64
+  __DATA.__common: 0xf84
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libutil.dylib
-  Functions: 818
-  Symbols:   170
-  CStrings:  1454
+  Functions: 828
+  Symbols:   174
+  CStrings:  1550
 
Symbols:
+ _CFNumberGetTypeID
+ _CFNumberGetValue
+ _IOServiceGetMatchingServices
+ _mach_absolute_time
CStrings:
+ "%s:%d: Cannot find entries matching %s : %u\n"
+ "%s:%u: Setting timeout to extra %u seconds starting from this point (+%u:%02u)\n"
+ "2235.40.9.0.1"
+ "Bytes (Read)"
+ "Bytes (Write)"
+ "GetDstreamSize_compressed_ino_phys_size"
+ "GetDstreamSize_ino_phys_size"
+ "GetIOKitDeviceIOStats"
+ "IOBlockStorageDriver"
+ "Iterator_ProcessDrec"
+ "Iterator_iterate_jobj"
+ "MoverBase_Insert"
+ "MoverBase_InsertPurgeRec"
+ "MoverBase_MoveTo2ndTree"
+ "MoverBase_OnPostMoveObj_TYPE_INO"
+ "MoverBase_OnPostMoveObj_clone_mapping_add_ino"
+ "MoverBase_OnPurgeDrec"
+ "MoverBase_PostMove"
+ "MoverBase_PostMove_Purge_iterate_jobjs"
+ "MoverBase_PostMove_iterate_jobjs"
+ "MoverBase_Remove"
+ "MoverBase_ReplaceDirStats"
+ "MoverBase_SetDirNlink"
+ "Mover_MoveDrec_Rehashing"
+ "Mover_OnCryptoId"
+ "Mover_OnDrec"
+ "Mover_OnFext"
+ "Mover_OnFext_apfs_update_phys_range"
+ "Mover_OnInode"
+ "Mover_OnInode_DocId"
+ "Mover_OnInode_clone_mapping_add_ino"
+ "Mover_OnInode_iterate_jobjs"
+ "Mover_OnInode_walk_file_extents"
+ "Mover_OnSibling"
+ "Mover_OnXattr"
+ "Mover_OnXattr_walk_file_extents"
+ "Mover_PostMove_FolderExtractor"
+ "Operations (Read)"
+ "Operations (Write)"
+ "PathFlags_Evaluate"
+ "Preprocessor_AnalyzeFext"
+ "Preprocessor_AnalyzePurgeable"
+ "Preprocessor_AnalyzeXattr_walk_file_extents"
+ "Preprocessor_CloneFext"
+ "Preprocessor_CloneHardlink"
+ "Preprocessor_CloneXattr"
+ "Preprocessor_CryptoDecRef"
+ "Preprocessor_CryptoIncRef"
+ "Preprocessor_FinalizeCryptoState"
+ "Preprocessor_FinalizeCryptoState_iterate_jobjs"
+ "Preprocessor_FinalizeCryptoState_walk_file_extents"
+ "Preprocessor_OnDrec"
+ "Preprocessor_ProcessDstreams"
+ "Preprocessor_ProcessDstreams_walk_file_extents"
+ "Preprocessor_ProcessFexts"
+ "Preprocessor_ProcessFexts_dev_read_data"
+ "Preprocessor_ProcessFexts_dev_write_data"
+ "Preprocessor_ProcessFexts_spaceman_alloc"
+ "Preprocessor_ProcessInodes"
+ "Preprocessor_ProcessSharedMetrics"
+ "Preprocessor_RecordSharedJobjs"
+ "Preprocessor_RecordSharedJobjs_walk_file_extents"
+ "Preprocessor_ReplaceFext"
+ "Preprocessor_ScanDstreams"
+ "Preprocessor_ScanDstreams_iterate_jobjs"
+ "Preprocessor_ScanDstreams_walk_file_extents"
+ "Preprocessor_ScanFext"
+ "Preprocessor_ScanPurgeables"
+ "Preprocessor_ScanXattr"
+ "Preprocessor_ScanXattr_walk_file_extents"
+ "Preprocessor_UpdateCryptoMap"
+ "Preprocessor_UpdateDsMap"
+ "Preprocessor_UpdateInoMap"
+ "Preprocessor_UpdateRangeMap"
+ "Statistics"
+ "Total Time (Read)"
+ "Total Time (Write)"
+ "WARNING: Verification was turned off to save time"
+ "WARNING: Verification was turned off to save time\n"
+ "dereference_phys_range"
+ "extend_timeout"
+ "fs_get_inode"
+ "reference_phys_range"
+ "reserved_71"
+ "reserved_72"
+ "reserved_73"
+ "reserved_74"
+ "reserved_75"
+ "reserved_76"
+ "reserved_77"
+ "reserved_78"
+ "reserved_79"
+ "reserved_80"
+ "reserved_81"
+ "reserved_82"
+ "reserved_83"
+ "spp_extentref_get_range"
- "2235.0.13"

```
