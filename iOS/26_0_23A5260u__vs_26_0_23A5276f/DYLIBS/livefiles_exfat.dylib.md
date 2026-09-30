## livefiles_exfat.dylib

> `/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_exfat.dylib`

```diff

-522.0.0.0.0
-  __TEXT.__text: 0x1c598
-  __TEXT.__auth_stubs: 0x420
+522.0.1.0.0
+  __TEXT.__text: 0x1c9f0
+  __TEXT.__auth_stubs: 0x430
   __TEXT.__const: 0x4b50
-  __TEXT.__oslogstring: 0x4862
-  __TEXT.__cstring: 0x6c8
-  __TEXT.__unwind_info: 0x240
+  __TEXT.__oslogstring: 0x46d8
+  __TEXT.__cstring: 0x71b
+  __TEXT.__unwind_info: 0x248
   __TEXT.__objc_methname: 0xe2
   __TEXT.__objc_stubs: 0xe0
-  __DATA_CONST.__got: 0x18
+  __DATA_CONST.__got: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x218
+  __AUTH_CONST.__auth_got: 0x220
   __AUTH.__data: 0x140
   __DATA.__data: 0x27
   __DATA.__common: 0x18

   - /System/Library/PrivateFrameworks/LiveFS.framework/LiveFS
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E04D2A66-7CB1-3370-90AE-3CB0E053821C
-  Functions: 176
-  Symbols:   336
-  CStrings:  443
+  UUID: AD9F1F3F-6B28-31F1-B05C-F233C16EB6B3
+  Functions: 179
+  Symbols:   344
+  CStrings:  447
 
Symbols:
+ _MultiReadSingleWrite_LockRead.cold.1
+ _MultiReadSingleWrite_LockWrite.cold.1
+ _OUTLINED_FUNCTION_0
+ __os_log_default
+ __os_log_fault_impl
Functions:
~ _MultiReadSingleWrite_LockRead : 4 -> 72
~ _MultiReadSingleWrite_LockWrite : 4 -> 72
+ _FILEOPS_GetFileAllocatedSize
~ _FileOPS_SetAttrToDirEntry : 1996 -> 2044
~ _EXFAT_Write : 2560 -> 2572
~ _EXFAT_BeginBlockmap : 2640 -> 2648
~ _EXFAT_EndBlockmap : 1864 -> 1872
~ _EXFAT_Create : 1416 -> 1420
~ _EXFAT_SetAttr : 512 -> 516
~ _EXFAT_SymLink : 1388 -> 1392
~ _EXFAT_Rename : 4276 -> 4636
~ _DIROPS_CreateNewEntry : 2084 -> 2244
~ _DIROPS_UpdateDirLastModifiedTime : 360 -> 368
~ _DIROPS_MarkNodeDirEntriesAsDeleted : 1316 -> 1372
~ _EXFAT_MkDir : 1428 -> 1432
~ _EXFAT_RmDir : 1360 -> 1364
~ _EXFAT_Remove : 1124 -> 1128
CStrings:
+ "%s failed to allocate record.\n"
+ "%s:  fail to convert utf8 -> utf16.\n"
+ "%s: 'From' lookup ended with error [%d].\n"
+ "%s: 'To' and 'From' are the same\n"
+ "%s: 'To' is a directory [eFromRecId %d].\n"
+ "%s: 'To' is not a directory [eToRecId %d].\n"
+ "%s: DIROPS_LookForDirEntry of 'to' returned an error [%d].\n"
+ "%s: DIROPS_PopulateHT failed with err = [%d]\n"
+ "%s: DIROPS_isDirEmpty returned error %d.\n"
+ "%s: Fail to write errno = [%d]\n"
+ "%s: Failed to allocate FileSet.\n"
+ "%s: Failed to allocate psName.\n"
+ "%s: FolderNode is not a directory.\n"
+ "%s: Got illegal fromName/toName [%s] [%s]\n"
+ "%s: Got invalid new entry type [%d].\n"
+ "%s: Invalid mode or type[%#llx, %d]"
+ "%s: Invalid objects ('From' is %d 'To' is %d).\n"
+ "%s: Lookup for free directory entries failed with error [%d].\n"
+ "%s: Save new entries to device failed with error [%d].\n"
+ "%s: Setting readonly fields, %#llx 0x%llx]"
+ "%s: expected the volume to be dirty"
+ "%s: fail to lookup for new dir record [%d].\n"
+ "%s: failed to create HT with error %s"
+ "%s: failed to evict clusters [%d]"
+ "%s: got invalid first cluster for: %s %u.\n"
+ "%s: ht_insert failed with [%d].\n"
+ "%s: pthread_rwlock_rdlock returned %d\n"
+ "%s: pthread_rwlock_wrlock returned %d\n"
+ "%s: unable to create new file / directory entry in destination dir (%d).\n"
+ "%s: unable to remove 'to' file / record (iError %d).\n"
+ "%s: unable to remove old file / directory entry (DIROPS_MarkNodeDirEntriesAsDeleted returned %d).\n"
+ "DIROPS_CreateNewEntry"
+ "MultiReadSingleWrite_LockRead"
+ "MultiReadSingleWrite_LockWrite"
- "DIROPS_CreateNewEntry:  fail to convert utf8 -> utf16.\n"
- "DIROPS_CreateNewEntry: Failed to allocate FileSet.\n"
- "DIROPS_CreateNewEntry: Failed to allocate psName.\n"
- "DIROPS_CreateNewEntry: FolderNode is not a directory.\n"
- "DIROPS_CreateNewEntry: Got invalid new entry type [%d].\n"
- "DIROPS_CreateNewEntry: Invalid mode or type[%#llx, %d]"
- "DIROPS_CreateNewEntry: Lookup for free directory entries failed with error [%d].\n"
- "DIROPS_CreateNewEntry: Save new entries to device failed with error [%d].\n"
- "DIROPS_CreateNewEntry: Setting readonly fields, %#llx 0x%llx]"
- "DIROPS_CreateNewEntry: got invalid first cluster for: %s %u.\n"
- "DIROPS_CreateNewEntry: ht_insert failed with [%d].\n"
- "DIROPS_MarkNodeDirEntriesAsDeleted fail to write errno = [%d]\n"
- "DIROPS_MarkNodeDirEntriesAsDeleted: DIROPS_PopulateHT failed with err = [%d]\n"
- "EXFAT_Rename\n"
- "EXFAT_Rename failed to allocate record.\n"
- "EXFAT_Rename: 'From' lookup ended with error [%d].\n"
- "EXFAT_Rename: 'To' and 'From' are the same\n"
- "EXFAT_Rename: 'To' is a directory [eFromRecId %d].\n"
- "EXFAT_Rename: 'To' is not a directory [eToRecId %d].\n"
- "EXFAT_Rename: DIROPS_LookForDirEntry of 'to' returned an error [%d].\n"
- "EXFAT_Rename: DIROPS_isDirEmpty returned error %d.\n"
- "EXFAT_Rename: Got illegal fromName/toName [%s] [%s]\n"
- "EXFAT_Rename: Invalid objects ('From' is %d 'To' is %d).\n"
- "EXFAT_Rename: fail to lookup for new dir record [%d].\n"
- "EXFAT_Rename: failed to create HT with error %s"
- "EXFAT_Rename: unable to create new file / directory entry in destination dir (%d).\n"
- "EXFAT_Rename: unable to remove 'to' file / record (iError %d).\n"
- "EXFAT_Rename: unable to remove old file / directory entry (DIROPS_MarkNodeDirEntriesAsDeleted returned %d).\n"
- "FileOPS_SetAttrToDirEntry: expected the volume to be dirty"
- "FileOPS_SetAttrToDirEntry: failed to evict clusters [%d]"

```
