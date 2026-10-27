## CalendarDatabase

> `/System/Library/PrivateFrameworks/CalendarDatabase.framework/Versions/A/CalendarDatabase`

```diff

-1291.0.0.0.0
-  __TEXT.__text: 0xe1430
-  __TEXT.__objc_methlist: 0x1f0c
-  __TEXT.__cstring: 0x20570
-  __TEXT.__const: 0xab4
-  __TEXT.__gcc_except_tab: 0x1828
-  __TEXT.__oslogstring: 0xccaf
+1291.2.3.0.0
+  __TEXT.__text: 0xe1ac8
+  __TEXT.__objc_methlist: 0x1f24
+  __TEXT.__cstring: 0x20679
+  __TEXT.__const: 0xaa4
+  __TEXT.__gcc_except_tab: 0x1830
+  __TEXT.__oslogstring: 0xce98
   __TEXT.__dlopen_cstrs: 0xc0
-  __TEXT.__unwind_info: 0x2d38
+  __TEXT.__unwind_info: 0x2d48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_arraydata: 0xc8
   __DATA_CONST.__got: 0x9d0
   __AUTH_CONST.__const: 0x29e0
-  __AUTH_CONST.__cfstring: 0xcc80
+  __AUTH_CONST.__cfstring: 0xcd00
   __AUTH_CONST.__objc_const: 0x37d0
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__auth_got: 0xee0
+  __AUTH_CONST.__auth_got: 0xed8
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__objc_data: 0x780
+  __AUTH.__objc_data: 0x500
   __DATA.__objc_ivar: 0x1b4
   __DATA.__data: 0x12d0
   __DATA.__bss: 0x1e0
-  __DATA_DIRTY.__objc_data: 0x5a0
+  __DATA_DIRTY.__objc_data: 0x820
   __DATA_DIRTY.__data: 0x280
   __DATA_DIRTY.__bss: 0x218
   __DATA_DIRTY.__common: 0x48

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 4279
-  Symbols:   7673
-  CStrings:  3132
+  Functions: 4284
+  Symbols:   7678
+  CStrings:  3140
 
Symbols:
+ -[CalSingleDatabaseInMemoryChangeTimestamp hash]
+ -[CalSingleDatabaseInMemoryChangeTimestamp isEqual:]
+ GCC_except_table250
+ GCC_except_table30
+ GCC_except_table344
+ GCC_except_table347
+ GCC_except_table55
+ _CalDatabaseClearDefaultCalendarIfDefaultIsInAuxDatabaseWithID
+ _CalDatabaseCopyOrCreateDefaultCalendarForNewEventsUpdateIfNeeded
+ _CalDatabaseSaveWithOptionsAndOutSelfTimestamp
+ _CalPersonaUtilsErrorDomain
+ __CalAttachmentFileResolveLocalURLReArchivingIfNeeded
+ _objc_msgSend$containerForAccountIdentifier:error:
+ _objc_msgSend$containerInfoForAccount:error:
+ _objc_msgSend$containerInfoForAccountIdentifier:error:
+ _objc_msgSend$containerInfoForPersonaIdentifier:error:
- GCC_except_table249
- GCC_except_table342
- GCC_except_table345
- GCC_except_table54
- GCC_except_table61
- _NSURLCreationDateKey
- _UnzipArchive
- _objc_msgSend$containerForAccountIdentifier:
- _objc_msgSend$containerInfoForAccount:
- _objc_msgSend$containerInfoForAccountIdentifier:
- _objc_msgSend$containerInfoForPersonaIdentifier:
CStrings:
+ "%@.zip"
+ "AutoArchivedPathMigrationCompleted"
+ "Aux database containing the default calendar was deleted"
+ "CalCalendarRef CalDatabaseCopyDefaultOrAnyReadWriteCalendarForNewEvents(CalDatabaseRef, CalStoreRef, BOOL)"
+ "CalCalendarRef CalDatabaseCopyOrCreateDefaultCalendarForNewEventsUpdateIfNeeded(CalDatabaseRef, BOOL)"
+ "Could not get a container info for account ID %{public}@: %@"
+ "Could not get new calendar data container. store uuid = %{public}@: %@"
+ "Could not open %@: %s"
+ "Couldn't get container info for persona %{public}@. Using main database for this persona. error = %@"
+ "Couldn't look up persona %{public}@: %@"
+ "Couldn't look up persona ID %{public}@: %@"
+ "Failed to get URL for data container of account %{public}@: %@"
+ "Failed to get container info for account [%{public}@]: %@"
+ "Failed to get container info for persona %{public}@: %@"
+ "UPDATE AttachmentFile SET local_path = local_path || '.zip' WHERE (flags & %d) != 0 AND SUBSTR(local_path, -4) != '.zip';"
+ "UPDATE AttachmentFile SET local_path = local_path || '.zip' WHERE (flags & %d) != 0;"
+ "Unable to re-archive attachment data: %@"
+ "_CalAttachmentFileGetAttachmentContainerURLsForStoreProperties: Failed to get container for account %{public}@: %@"
+ "_CalAttachmentFileGetCalendarDataContainerForAttachmentFile: Failed to get container for account %{public}@: %@"
+ "_CalAttachmentFileMigrateAttachmentsInStoreFromOldPersistentIDToNewPersistentID: Failed to get container for account %{public}@: %@"
+ "commit at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CalendarDatabase/CalendarDatabase/CalCalendar.m:4352"
+ "rollback at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CalendarDatabase/CalendarDatabase/CalDatabase.m:5068"
+ "write at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CalendarDatabase/CalendarDatabase/CalCalendar.m:4329"
- "Attachment cleanup: skipping removing file because it is archived and is too young: %@"
- "CalCalendarRef CalDatabaseCopyDefaultOrAnyReadWriteCalendarForNewEvents(CalDatabaseRef, CalStoreRef)"
- "CalCalendarRef CalDatabaseCopyOrCreateDefaultCalendarForNewEvents(CalDatabaseRef)"
- "Could not get new calendar data container. store uuid = %{public}@"
- "Couldn't get container info for persona %{public}@. Using main database for this persona."
- "Couldn't look up persona %{public}@"
- "Couldn't look up persona ID %{public}@"
- "Error checking creation date for %@: %@"
- "Failed to unzip attachment (error: %@)."
- "SiriCanLearnFromAppBlacklist"
- "Unable to archive data: %@"
- "com.apple.suggestions.settingsChanged"
- "commit at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CalendarDatabase/CalendarDatabase/CalCalendar.m:4339"
- "rollback at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CalendarDatabase/CalendarDatabase/CalDatabase.m:5055"
- "write at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CalendarDatabase/CalendarDatabase/CalCalendar.m:4316"
```
