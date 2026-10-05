## CalendarDatabase

> `/System/Library/PrivateFrameworks/CalendarDatabase.framework/CalendarDatabase`

```diff

-1291.1.3.0.0
-  __TEXT.__text: 0xd79d0
+1291.2.3.0.0
+  __TEXT.__text: 0xd8040
   __TEXT.__objc_methlist: 0x1f24
-  __TEXT.__cstring: 0x1fa45
+  __TEXT.__cstring: 0x1fa98
   __TEXT.__const: 0xaa4
-  __TEXT.__gcc_except_tab: 0x18e4
-  __TEXT.__oslogstring: 0xcbe7
+  __TEXT.__gcc_except_tab: 0x18f0
+  __TEXT.__oslogstring: 0xce69
   __TEXT.__dlopen_cstrs: 0x60
   __TEXT.__unwind_info: 0x4010
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_selrefs: 0x2500
   __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_arraydata: 0x38
-  __DATA_CONST.__got: 0x9a0
+  __DATA_CONST.__got: 0x9a8
   __AUTH_CONST.__const: 0x2150
-  __AUTH_CONST.__cfstring: 0xca40
+  __AUTH_CONST.__cfstring: 0xca60
   __AUTH_CONST.__objc_const: 0x37d0
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__auth_got: 0xfe0
-  __AUTH.__objc_data: 0xa00
+  __AUTH.__objc_data: 0x550
   __DATA.__objc_ivar: 0x1b4
   __DATA.__data: 0x1360
   __DATA.__common: 0x20
-  __DATA_DIRTY.__objc_data: 0x320
+  __DATA_DIRTY.__objc_data: 0x7d0
   __DATA_DIRTY.__data: 0x1f8
   __DATA_DIRTY.__bss: 0xf0
   __DATA_DIRTY.__common: 0x28

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 4251
-  Symbols:   6560
-  CStrings:  3121
+  Functions: 4253
+  Symbols:   6564
+  CStrings:  3130
 
Symbols:
+ GCC_except_table342
+ GCC_except_table345
+ _CalDatabaseClearDefaultCalendarIfDefaultIsInAuxDatabaseWithID
+ _CalDatabaseCopyOrCreateDefaultCalendarForNewEventsUpdateIfNeeded
+ _CalPersonaUtilsErrorDomain
- GCC_except_table340
CStrings:
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
+ "_CalAttachmentFileGetAttachmentContainerURLsForStoreProperties: Failed to get container for account %{public}@: %@"
+ "_CalAttachmentFileGetCalendarDataContainerForAttachmentFile: Failed to get container for account %{public}@: %@"
+ "_CalAttachmentFileMigrateAttachmentsInStoreFromOldPersistentIDToNewPersistentID: Failed to get container for account %{public}@: %@"
+ "commit at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CalendarDatabase/CalendarDatabase/CalCalendar.m:4352"
+ "write at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CalendarDatabase/CalendarDatabase/CalCalendar.m:4329"
- "CalCalendarRef CalDatabaseCopyDefaultOrAnyReadWriteCalendarForNewEvents(CalDatabaseRef, CalStoreRef)"
- "CalCalendarRef CalDatabaseCopyOrCreateDefaultCalendarForNewEvents(CalDatabaseRef)"
- "Could not get new calendar data container. store uuid = %{public}@"
- "Couldn't get container info for persona %{public}@. Using main database for this persona."
- "Couldn't look up persona %{public}@"
- "Couldn't look up persona ID %{public}@"
- "commit at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CalendarDatabase/CalendarDatabase/CalCalendar.m:4338"
- "write at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CalendarDatabase/CalendarDatabase/CalCalendar.m:4315"
```
