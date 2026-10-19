## CalendarDatabase

> `/System/Library/PrivateFrameworks/CalendarDatabase.framework/CalendarDatabase`

```diff

 1291.2.3.0.0
-  __TEXT.__text: 0xd8040
+  __TEXT.__text: 0xd7fec
   __TEXT.__objc_methlist: 0x1f24
-  __TEXT.__cstring: 0x1fa98
+  __TEXT.__cstring: 0x1fb91
   __TEXT.__const: 0xaa4
   __TEXT.__gcc_except_tab: 0x18f0
-  __TEXT.__oslogstring: 0xce69
+  __TEXT.__oslogstring: 0xcdd0
   __TEXT.__dlopen_cstrs: 0x60
   __TEXT.__unwind_info: 0x4010
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_selrefs: 0x2500
   __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_arraydata: 0x38
-  __DATA_CONST.__got: 0x9a8
+  __DATA_CONST.__got: 0x9a0
   __AUTH_CONST.__const: 0x2150
-  __AUTH_CONST.__cfstring: 0xca60
+  __AUTH_CONST.__cfstring: 0xcb00
   __AUTH_CONST.__objc_const: 0x37d0
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__auth_got: 0xfe0
+  __AUTH_CONST.__auth_got: 0xfd8
   __AUTH.__objc_data: 0x550
   __DATA.__objc_ivar: 0x1b4
   __DATA.__data: 0x1360

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   Functions: 4253
-  Symbols:   6564
-  CStrings:  3130
+  Symbols:   6562
+  CStrings:  3131
 
Symbols:
+ GCC_except_table57
+ __CalAttachmentFileResolveLocalURLReArchivingIfNeeded
- GCC_except_table53
- GCC_except_table56
- _NSURLCreationDateKey
- _UnzipArchive
Functions:
~ _CalAttachmentFileMigrateTables : 120 -> 468
~ __CalAttachmentFileCopyLocalURLForArchivedData : 476 -> 164
~ __CalAttachmentFileSetFileDataWithOpenFile : 2620 -> 2484
~ __CalAttachmentFileCopyLocalURL -> __CalAttachmentFileGetLocalRelativePath : 132 -> 212
~ __CalAttachmentFileGetLocalRelativePath -> __CalAttachmentFileGetCalendarDataContainerForAttachmentFile : 212 -> 280
~ __CalAttachmentFileGetCalendarDataContainerForAttachmentFile -> __CalAttachmentFileResolveLocalURLReArchivingIfNeeded : 280 -> 444
~ _CalDatabaseDeleteOrphanedAttachmentsInDirectory : 1760 -> 1464
CStrings:
+ "%@.zip"
+ "AutoArchivedPathMigrationCompleted"
+ "UPDATE AttachmentFile SET local_path = local_path || '.zip' WHERE (flags & %d) != 0 AND SUBSTR(local_path, -4) != '.zip';"
+ "UPDATE AttachmentFile SET local_path = local_path || '.zip' WHERE (flags & %d) != 0;"
+ "Unable to re-archive attachment data: %@"
- "Attachment cleanup: skipping removing file because it is archived and is too young: %@"
- "Error checking creation date for %@: %@"
- "Failed to unzip attachment (error: %@)."
- "Unable to archive data: %@"
```
