## CalendarDatabase

> `/System/Library/PrivateFrameworks/CalendarDatabase.framework/Versions/A/CalendarDatabase`

```diff

-1253.3.2.0.0
-  __TEXT.__text: 0xe0354
-  __TEXT.__auth_stubs: 0x1d70
-  __TEXT.__objc_methlist: 0x19f0
-  __TEXT.__cstring: 0x1f31c
+1253.5.4.0.0
+  __TEXT.__text: 0xe2008
+  __TEXT.__auth_stubs: 0x1d60
+  __TEXT.__objc_methlist: 0x1d94
+  __TEXT.__cstring: 0x1f279
   __TEXT.__const: 0x74c
-  __TEXT.__gcc_except_tab: 0x191c
-  __TEXT.__oslogstring: 0xc7e6
+  __TEXT.__gcc_except_tab: 0x190c
+  __TEXT.__oslogstring: 0xc90e
   __TEXT.__dlopen_cstrs: 0xc0
-  __TEXT.__unwind_info: 0x2bf0
+  __TEXT.__unwind_info: 0x2be0
   __TEXT.__objc_classname: 0x567
-  __TEXT.__objc_methname: 0x8daa
+  __TEXT.__objc_methname: 0x8de3
   __TEXT.__objc_methtype: 0x4513
-  __TEXT.__objc_stubs: 0x8200
-  __DATA_CONST.__got: 0x9c8
-  __DATA_CONST.__const: 0xd938
+  __TEXT.__objc_stubs: 0x8280
+  __DATA_CONST.__got: 0x9e0
+  __DATA_CONST.__const: 0xd950
   __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x23c8
+  __DATA_CONST.__objc_selrefs: 0x2470
   __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0xb8
-  __AUTH_CONST.__auth_got: 0xec8
-  __AUTH_CONST.__const: 0x2930
+  __AUTH_CONST.__auth_got: 0xec0
+  __AUTH_CONST.__const: 0x2950
   __AUTH_CONST.__cfstring: 0xc780
-  __AUTH_CONST.__objc_const: 0x3cb0
+  __AUTH_CONST.__objc_const: 0x35f0
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0xcd0
   __DATA.__objc_ivar: 0x1a0
-  __DATA.__data: 0x940
+  __DATA.__data: 0x938
   __DATA.__bss: 0x3f0
   __DATA.__common: 0x40
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: AEE6ECF3-928A-3F71-81AE-2BE3E2AEF21F
-  Functions: 4155
-  Symbols:   7649
-  CStrings:  6253
+  UUID: F719BDD5-1197-3D58-A4AA-17C41B4F94D1
+  Functions: 4195
+  Symbols:   7709
+  CStrings:  6263
 
Symbols:
+ +[CDBPreferences sharedReadOnly].cold.1
+ +[CDBPreferences sharedReadWrite].cold.1
+ +[CalACMigrationAccountStore sharedInstance].cold.1
+ +[CalAlarmMetadata isRecognizedParameter:forProperty:inComponent:].cold.1
+ +[CalAlarmMetadata isRecognizedProperty:inComponent:].cold.1
+ +[CalAlarmMetadata shouldSkipSavingUnrecognizedParametersForProperty:inComponent:].cold.1
+ +[CalCalendarLocalAccountInfo sharedInstance].cold.1
+ +[CalExchangeCalendarExternalRepresentation logHandle].cold.1
+ +[CalExchangeCalendarItemExternalRepresentation logHandle].cold.1
+ +[CalItemMetadata _whitelistedClassesForSecureCoding].cold.1
+ +[CalItemMetadata isRecognizedParameter:forProperty:inComponent:].cold.1
+ +[CalItemMetadata isRecognizedProperty:inComponent:].cold.1
+ +[CalItemMetadata shouldSkipSavingUnrecognizedParametersForProperty:inComponent:].cold.1
+ +[CalStoreSetupAndTeardownUtils setLocalStoreEnabled:inDatabase:].cold.1
+ -[CalAlarmMetadata initWithCoder:].cold.1
+ -[CalItemMetadata initWithCoder:].cold.1
+ CDBLogInitIfNeeded.cold.1
+ CalAttendeeBasePropertiesMappingDict.cold.1
+ CalAttendeeGetPropertyIDWithPropertyName.cold.1
+ CalCalendarItemUpdateICSComponent.cold.1
+ CalColorGetPropertyIDWithPropertyName.cold.1
+ CalConferenceGetPropertyIDWithPropertyName.cold.1
+ CalDatabaseClearSuperfluousChanges.cold.1
+ CalDatabaseCreateWithConfiguration.cold.1
+ CalDatabaseCreateWithConfiguration.cold.2
+ CalDatabaseCreateWithConfiguration.cold.3
+ CalDatabaseGetSubscribedCalendarAccountPropertiesIncludedInBackup.cold.1
+ CalDatabaseIsCurrentProcessCalaccessd.cold.1
+ CalDatabasePerformMigrationIfNeeded.cold.1
+ CalDatabasePerformReminderTruthFileMigrationIfNeeded.cold.1
+ CalDatabaseRequestWidgetRefreshWithRateLimiter.cold.1
+ CalDatabaseSaveInternalWithOptions.cold.1
+ CalDatabaseSaveInternalWithOptions.cold.2
+ CalErrorGetPropertyIDWithPropertyName.cold.1
+ CalEventOccurrenceCacheGetLongAlarmIntervals.cold.1
+ CalImageGetPropertyIDWithPropertyName.cold.1
+ CalInvalidAlarmDate.cold.1
+ CalOrganizerGetPropertyIDWithPropertyName.cold.1
+ CalResourceChangeGetPropertyIDWithPropertyName.cold.1
+ GCC_except_table17
+ GCC_except_table340
+ GCC_except_table347
+ GCC_except_table40
+ GCC_except_table43
+ GCC_except_table51
+ GCC_except_table61
+ GCC_except_table64
+ GCC_except_table80
+ GCC_except_table82
+ ICSCalendarFromCalEntitiesWithTimeZoneGenerationOptions.cold.1
+ _CalAlarmCacheGenerateAlarmsInDateRange.cold.1
+ _CalDatabaseBeginTransactionOfType.cold.1
+ _CalDatabasePostDBOrSyncStatusChangeNotification.cold.1
+ _CalDatabaseShouldPostInProcessChangeNotification.cold.1
+ _CalEventOccurrenceCacheLoadInfo.cold.1
+ _CopyOpenFileURLWrapper
+ _DestroyOpenFileURLWrapper
+ _EKAttachmentProperty_URLWrapperForPendingFileCopy
+ _EKCreateMSUIDStringForEvent.cold.1
+ _EKMSUUIDStringForDetachedEvent.cold.1
+ _NSURLFileProtectionCompleteUnlessOpen
+ _NSURLFileProtectionKey
+ _OBJC_CLASS_$_CalOpenFileURLWrapper
+ __CalAttachmentFileGetURLWrapperForPendingFileCopy
+ __CalAttachmentFileSetAttributes
+ __CalAttachmentFileSetFileDataWithOpenFile
+ __CalAttachmentFileSetProtectionAndQuarantineAttributes
+ __CalAttachmentFileSetProtectionAndQuarantineAttributesWithFile
+ __CalAttachmentFileValidateLocalRelativePath
+ __CalAttendeeGetPropertyIDWithPropertyName_block_invoke.cold.1
+ __CalDatabaseCommitTransaction.cold.1
+ __CalDatabaseGetChangedEKObjectsForClient_block_invoke.cold.1
+ __CalDatabasePerformMigrationIfNeeded_block_invoke.cold.1
+ __CalDatabaseRollbackTransaction.cold.1
+ __CalEventOccurrenceCacheTrimAndExtendCore
+ __CalOrganizerGetPropertyIDWithPropertyName_block_invoke.cold.1
+ ____CalAttachmentFileSetProtectionAndQuarantineAttributes_block_invoke
+ _fcopyfile
+ _isSavedAttachmentParameter.cold.1
+ _isSavedParameter.cold.1
+ _kCalOpenFileURLWrapperMethods
+ _lseek
+ _objc_msgSend$characterAtIndex:
+ _objc_msgSend$compare:options:range:
+ _objc_msgSend$file
+ _objc_msgSend$fileDescriptor
+ _objc_msgSend$setResourceValues:error:
- CalAlertSharedEventChanges.__AlertSharedEventChangesValue
- CalAlertUnacknowledgedInvitations.__AlertUnacknowledgedInvitationsValue
- GCC_except_table21
- GCC_except_table24
- GCC_except_table35
- GCC_except_table352
- GCC_except_table353
- GCC_except_table42
- GCC_except_table57
- GCC_except_table59
- GCC_except_table62
- GCC_except_table79
- GCC_except_table81
- GCC_except_table90
- _CFURLCopyPathExtension
- _CFURLStartAccessingSecurityScopedResource
- _CalAlertSharedEventChanges
- _CalAlertUnacknowledgedInvitations
- _CalDatabaseCopyEventIDsThatMatchLocationOrSummary
- _CopySecurityScopedURLWrapper
- _DestroySecurityScopedURLWrapper
- _EKAttachmentProperty_securityScopedURLWrapperForPendingFileCopy
- __CalAttachmentFileCopyURLForPendingFileCopy
- __CalAttachmentFileSetQuarantineAttributes
- __CalAttachmentFileSetQuarantineAttributesForFile
- __CalEventAlertPrefChanged
- __CalEventAlertSharedEventChangesPrefChanged
- __CalGetPrefValue
- _kCalSecurityScopedURLWrapperMethods
- _objc_msgSend$copyItemAtPath:toPath:error:
- _pthread_cond_signal
CStrings:
+ "/.."
+ "/../"
+ "Attachment file path (%@) is invalid"
+ "Attachments/"
+ "Copy failed"
+ "Couldn't create a local file for the attachment file %d"
+ "Couldn't rewind file to be copied: %i"
+ "Encountered an error setting protection/quarantine attributes with %@: %@"
+ "Error checking if url to be protected (%@) is a directory: %@"
+ "Error setting file data: %i"
+ "Error setting resource attributes for URL %@: %@"
+ "Failed to close target file following copy: %i"
+ "URLWrapperForPendingFileCopy"
+ "characterAtIndex:"
+ "commit at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalCalendar.m:4233"
+ "commit at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabase.m:3064"
+ "commit at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1631"
+ "commit at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1673"
+ "commit at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1719"
+ "commit at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1937"
+ "commit at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:1444"
+ "commit at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:3708"
+ "commit at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:3742"
+ "commit at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:4124"
+ "commit at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalStore.m:2929"
+ "commit at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalStore.m:455"
+ "compare:options:range:"
+ "fileDescriptor"
+ "read at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalAlarmOccurrence.m:235"
+ "read at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabaseBackup.m:224"
+ "read at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1094"
+ "read at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1743"
+ "read at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:711"
+ "read at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:1559"
+ "read at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:1882"
+ "read at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:1964"
+ "read at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2029"
+ "read at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2084"
+ "read at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2200"
+ "read at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2253"
+ "read at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2671"
+ "read at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2883"
+ "read at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2970"
+ "read at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:3123"
+ "read at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:4097"
+ "read at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalRecurrence.m:1057"
+ "rollback at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalAlarmOccurrence.m:282"
+ "rollback at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabase.m:3066"
+ "rollback at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabase.m:3092"
+ "rollback at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabase.m:4800"
+ "rollback at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabaseBackup.m:241"
+ "rollback at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1224"
+ "rollback at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1812"
+ "rollback at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:840"
+ "rollback at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:1561"
+ "rollback at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:1910"
+ "rollback at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:1994"
+ "rollback at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2054"
+ "rollback at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2141"
+ "rollback at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2204"
+ "rollback at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2272"
+ "rollback at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2699"
+ "rollback at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2782"
+ "rollback at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2955"
+ "rollback at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:3010"
+ "rollback at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:3177"
+ "rollback at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:4100"
+ "rollback at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalRecurrence.m:1059"
+ "rollback at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalStore.m:2937"
+ "rollback at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalStore.m:460"
+ "setResourceValues:error:"
+ "write at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalCalendar.m:4210"
+ "write at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabase.m:2827"
+ "write at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1621"
+ "write at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1640"
+ "write at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1689"
+ "write at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1893"
+ "write at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:1401"
+ "write at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:3679"
+ "write at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:3734"
+ "write at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:4108"
+ "write at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:4114"
+ "write at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalStore.m:2865"
+ "write at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalStore.m:449"
- "CalDatabaseCopyEventIDsThatMatchLocationOrSummary"
- "Failed to copy attachment (error: %@)."
- "Failed to set quarantine properties for new attachment download: %@"
- "InvitationAlerts"
- "SELECT rowid FROM CalendarItem WHERE location LIKE '%%%@%%' or summary LIKE '%%%@%%';"
- "SharedEventAlerts"
- "commit at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalCalendar.m:4233"
- "commit at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabase.m:3064"
- "commit at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1631"
- "commit at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1673"
- "commit at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1719"
- "commit at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1937"
- "commit at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:1444"
- "commit at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:3708"
- "commit at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:3742"
- "commit at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:4124"
- "commit at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalStore.m:2929"
- "commit at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalStore.m:455"
- "copyItemAtPath:toPath:error:"
- "read at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalAlarmOccurrence.m:235"
- "read at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabaseBackup.m:224"
- "read at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1094"
- "read at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1743"
- "read at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:711"
- "read at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:1559"
- "read at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:1882"
- "read at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:1964"
- "read at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2029"
- "read at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2084"
- "read at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2200"
- "read at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2253"
- "read at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2671"
- "read at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2883"
- "read at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2970"
- "read at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:3123"
- "read at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:4097"
- "read at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalRecurrence.m:1057"
- "rollback at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalAlarmOccurrence.m:282"
- "rollback at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabase.m:3066"
- "rollback at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabase.m:3092"
- "rollback at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabase.m:4800"
- "rollback at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabaseBackup.m:241"
- "rollback at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1224"
- "rollback at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1812"
- "rollback at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:840"
- "rollback at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:1561"
- "rollback at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:1910"
- "rollback at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:1994"
- "rollback at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2054"
- "rollback at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2141"
- "rollback at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2204"
- "rollback at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2272"
- "rollback at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2699"
- "rollback at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2782"
- "rollback at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:2955"
- "rollback at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:3010"
- "rollback at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:3177"
- "rollback at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:4100"
- "rollback at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalRecurrence.m:1059"
- "rollback at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalStore.m:2937"
- "rollback at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalStore.m:460"
- "securityScopedURLWrapperForPendingFileCopy"
- "write at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalCalendar.m:4210"
- "write at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabase.m:2827"
- "write at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1621"
- "write at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1640"
- "write at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1689"
- "write at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1893"
- "write at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:1401"
- "write at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:3679"
- "write at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:3734"
- "write at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:4108"
- "write at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalEventOccurrenceCache.m:4114"
- "write at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalStore.m:2865"
- "write at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalStore.m:449"

```
