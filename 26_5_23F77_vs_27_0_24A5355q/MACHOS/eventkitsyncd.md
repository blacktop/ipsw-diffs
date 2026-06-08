## eventkitsyncd

> `/usr/libexec/eventkitsyncd`

```diff

-420.1.0.0.0
-  __TEXT.__text: 0x78fbc
-  __TEXT.__auth_stubs: 0xd10
-  __TEXT.__objc_stubs: 0xc860
-  __TEXT.__objc_methlist: 0x73a0
-  __TEXT.__cstring: 0x5b13
-  __TEXT.__objc_methname: 0xf888
-  __TEXT.__objc_classname: 0x918
-  __TEXT.__objc_methtype: 0x2562
-  __TEXT.__const: 0x290
-  __TEXT.__oslogstring: 0xb9a8
-  __TEXT.__gcc_except_tab: 0xb04
-  __TEXT.__unwind_info: 0x1b70
-  __DATA_CONST.__auth_got: 0x698
-  __DATA_CONST.__got: 0x410
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x17c0
-  __DATA_CONST.__cfstring: 0x4f00
-  __DATA_CONST.__objc_classlist: 0x300
+428.0.0.0.0
+  __TEXT.__text: 0x76000
+  __TEXT.__auth_stubs: 0xd90
+  __TEXT.__objc_stubs: 0xcbc0
+  __TEXT.__objc_methlist: 0x7510
+  __TEXT.__cstring: 0x5b50
+  __TEXT.__objc_methname: 0xfc6c
+  __TEXT.__objc_classname: 0x8ae
+  __TEXT.__objc_methtype: 0x2576
+  __TEXT.__const: 0x278
+  __TEXT.__oslogstring: 0xbc30
+  __TEXT.__gcc_except_tab: 0x844
+  __TEXT.__unwind_info: 0x1660
+  __DATA_CONST.__const: 0x1870
+  __DATA_CONST.__cfstring: 0x5080
+  __DATA_CONST.__objc_classlist: 0x308
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x288
-  __DATA_CONST.__objc_intobj: 0x1b0
+  __DATA_CONST.__objc_intobj: 0x198
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_doubleobj: 0x50
-  __DATA.__objc_const: 0xed78
-  __DATA.__objc_selrefs: 0x3e78
-  __DATA.__objc_ivar: 0x97c
-  __DATA.__objc_data: 0x1e00
+  __DATA_CONST.__auth_got: 0x6d8
+  __DATA_CONST.__got: 0x438
+  __DATA_CONST.__auth_ptr: 0x8
+  __DATA.__objc_const: 0xefb0
+  __DATA.__objc_selrefs: 0x3f60
+  __DATA.__objc_ivar: 0x998
+  __DATA.__objc_data: 0x1e50
   __DATA.__data: 0x800
   __DATA.__bss: 0x178
   __DATA.__common: 0x1c

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 125A78FC-4C94-32B2-9F96-DE7ACB77A9F8
-  Functions: 2838
-  Symbols:   357
-  CStrings:  5391
+  UUID: FBA05E50-1327-30EB-9062-4673420083A9
+  Functions: 2865
+  Symbols:   369
+  CStrings:  5454
 
Symbols:
+ _ICSDateFromCFDate
+ _ICSFloatingDateOnlyFromCFDate
+ _IDSSendErrorDomain
+ _NSLocalizedDescriptionKey
+ _NSTemporaryDirectory
+ _NSUnderlyingErrorKey
+ _OBJC_CLASS_$_EKSSyncRange
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x4
+ _objc_retain_x6
CStrings:
+ "$5"
+ "%@ attempted without an active transaction (autocommit mode is on) for [%@]"
+ "%@ failed during an active transaction (autocommit mode is off) with errCode [%d] for [%@]"
+ "%@ succeeded during an active transaction (autocommit mode is off) for [%@]"
+ "%@(1)"
+ "%@/%@"
+ "<!ExceptionDate!>"
+ "== Started EventKitSync-428"
+ "@\"SYSession\""
+ "@40@0:8d16d24d32"
+ "A"
+ "B56@0:8@16@24@32@40^@48"
+ "Creating temporary directory (%@) for new EKEventStore failed with error: %@"
+ "Failed to create/update event source"
+ "Failed to create/update reminder source"
+ "Migration sync check dropped (not cleared to perform delta sync), current [%ld], target [%ld]"
+ "Migration sync not needed, current [%ld], target [%ld]"
+ "Migration sync requested from [%ld] to [%ld]"
+ "NEKSyncCompletionAnalytics"
+ "Received old daily analytics version [%lu] (current version [%lu]) - ignoring incoming data for drift or duplication with IDS identifier: %@"
+ "T@\"NSDictionary\",R,N"
+ "T@\"NSString\",&,N,V_icsOccurrenceID"
+ "T@\"NSString\",&,N,V_uniqueIdentifier"
+ "T@\"NSString\",C,N,V_icsOccurrenceID"
+ "T@\"NSString\",C,N,V_uniqueIdentifier"
+ "TQ,N,V_version"
+ "TQ,R,N,V_sessionCount"
+ "Td,N,V_spanNow"
+ "[%{public}@] fetchChangesInto: fetchDuration [%.2f]"
+ "[%{public}@] processArrayOfArrayOfICSWrappers failed to commit changes with error: %{public}@"
+ "[%{public}@] uniqueIdentifier [%{public}@] included for [%{public}@] uniqueId [%{public}@] start [%{public}@]"
+ "[%{public}@] uniqueIdentifier match [%{public}@] uniqueId [%{public}@] start [%{public}@]"
+ "[%{public}@] uniqueIdentifier mismatch, phone [%{public}@] watch [%{public}@] uniqueId [%{public}@] start [%{public}@]"
+ "[%{public}@] uniqueIdentifier missing (expected) for event with uniqueId [%{public}@] start [%{public}@]"
+ "[%{public}@] uniqueIdentifier missing for event with uniqueId [%{public}@] start [%{public}@]"
+ "[Session: %{public}@] Migration sync complete, updated from [%ld] to [%ld]"
+ "[Session: %{public}@] Migration sync count unchanged at [%ld]"
+ "_createPhoneSackForWatchCache:"
+ "_deferPollingSourceLock"
+ "_fetchChangesInto:inside:"
+ "_getWindowNow"
+ "_icsOccurrenceID"
+ "_icsOccurrenceIDForEvent:"
+ "_isNotConnectedError:"
+ "_performIfInTransaction:"
+ "_processArrayOfArrayOfICSWrappers:batchWrappers:session:store:"
+ "_resetSendCompletionMetrics"
+ "_sessionCount"
+ "_spanNow"
+ "_uniqueIdentifier"
+ "_uniqueIdentifierMap"
+ "_updateMigrationCountForSession:"
+ "_updateSendCompletionMetrics:"
+ "_useOldWindow"
+ "_validateUniqueIdentifierForEvent:withWrapper:"
+ "_version"
+ "cStringUsingEncoding:"
+ "cancelWithUnderlyingReason:"
+ "com.apple.eventkitsync.restoreafterresets"
+ "com.apple.eventkitsync.synccompletions"
+ "com.apple.eventkitsyncd.error"
+ "consumeAllChangesUpToToken:"
+ "createOrUpdateSYObject:eventStore:reminderStore:session:error:"
+ "driftResultsForCache:withDiagnosticTimestamp:"
+ "eks_eventOnlyStoreIgnoringExternalChangesFor:withClientId:syncSession:"
+ "errorCode"
+ "errorDomain"
+ "errorWithDomain:code:userInfo:"
+ "fetchChangedObjectIDsMergingAttendeeChanges:"
+ "freshEventStoreFor:syncSession:"
+ "g"
+ "getHeardFromPhone"
+ "getMigrationCount"
+ "hasIcsOccurrenceID"
+ "hasUniqueIdentifier"
+ "hasUniqueIdentifierForIdentifier:"
+ "icsOccurrenceID"
+ "icsOccurrenceID extracted for uniqueId [%{public}@] icsOccurrenceID [%{public}@]"
+ "icsOccurrenceID failed to extract from uniqueId [%{public}@]"
+ "icsOccurrenceIDForIdentifier:"
+ "icsString"
+ "importEventsWithUUIDs:fromICSData:intoCalendars:options:batchSize:"
+ "initForTestingWithSpanNow:spanStart:spanEnd:"
+ "initWithEventStore:cause:syncSession:"
+ "isAllDay"
+ "isEqualToIgnoringCase:"
+ "lowercaseString"
+ "readUint32"
+ "resetSyncRange"
+ "saveReminder:commit:error:"
+ "sendAnalyticsForRestoreAfterReset:error:"
+ "sendAnalyticsForSyncCompletion:"
+ "sessionCount"
+ "setError:onSession:andCallCompletion:"
+ "setHeardFromPhone:"
+ "setIcsOccurrenceID:"
+ "setIcsOccurrenceID:forIdentifier:"
+ "setMigrationCount:"
+ "setSpanNow:"
+ "setUniqueIdentifier:"
+ "setUniqueIdentifier:forIdentifier:"
+ "setVersion:"
+ "spanNow"
+ "syncCompletionSessionCount"
+ "syncCompletionStartTime"
+ "uniqueIdentifierForIdentifier:"
+ "uniqueIdentifierMap"
+ "v28@0:8I16@20"
+ "v44@?0B8@\"EKSequenceToken\"12@\"NSArray\"20@\"NSArray\"28@\"NSArray\"36"
+ "version"
+ "windowNow"
+ "writeUint32:forTag:"
- "$3"
- "%@;%@;%f"
- "== Started EventKitSync-420.1"
- "@32@0:8d16d24"
- "@40@0:8@16d24@32"
- "Changing event id from %{public}@ to %{public}@"
- "Deleteing suppression cache entry for %@"
- "Migration check dropped."
- "Migration number is fine, no migration sync needed."
- "ROLLBACK attempted without an active transaction (autocommit mode is on) for [%@]"
- "ROLLBACK failed during an active transaction (autocommit mode is off) with errCode [%d] for [%@]"
- "ROLLBACK succeeded during an active transaction (autocommit mode is off) for [%@]"
- "Requested migration sync"
- "Suppressing alert due to cache hit on %@"
- "Surreptitiously adding event to changeset: %{public}@ due to attendee change"
- "T@\"NSDictionary\",&,N,V_startDateMap"
- "Tq,N,V_changeNumber"
- "[%{public}@] fetchChangesInto: sequenceNumbers [prev: %d curr:%d delta:%d] fetchDuration [%.2f]"
- "[%{public}@] fetchEventChangeSet: pulled -1 from lastSequenceNumber, requesting one (and only one) full sync? [%{BOOL}d]"
- "[%{public}@] fetchEventChangeSet: saw sequence number failure already, still waiting for corrective full sync to complete"
- "[%{public}@] setLastSequenceNumber: %d"
- "_alertSupressionCache"
- "_changeNumber"
- "_createPhoneSackForWatchCache:andDatabase:"
- "_dbFile"
- "_fetchChangesInto:from:inside:"
- "_fwdDaysToSync"
- "_getTestWindowEnd"
- "_getTestWindowStart"
- "_lastSequenceNumber"
- "_processArrayOfArrayOfICSWrappers:batchWrappers:session:"
- "_revDaysToSync"
- "_spanNowTime"
- "_startDateMap"
- "addAttendeeEvents:"
- "backup_restore_reset"
- "cancel"
- "changeNumber"
- "changedObjectIDsSinceToken:resultHandler:"
- "commit(1)"
- "createOrUpdateSYObject:eventStore:reminderStore:session:"
- "driftResultsForCache:withDiagnosticTimestamp:andDatabase:"
- "e"
- "eks_cacheKey"
- "eks_eventOnlyStoreIgnoringExternalChangesFor:withClientId:"
- "importICSData:intoCalendars:options:"
- "initForTestingWithRevDays:fwdDays:"
- "initWithDatabaseFile:"
- "lastSequenceNumber"
- "markChangedObjectIDsConsumedUpToToken:"
- "owner"
- "rollback(1)"
- "select I.unique_identifier, C.external_id calendar, O.occurrence_date occurrence_date from occurrencecache O left join calendar C on C.rowid = O.calendar_id left join calendaritem I on I.rowid = O.event_id where I.entity_type = 2 and O.occurrence_date >= ?  and O.occurrence_date <= ? and C.flags & 786432 == 0 order by occurrence_date, I.unique_identifier"
- "setChangeNumber:"
- "setLastSequenceNumber:"
- "setStartDateMap:"
- "setUniqueId:"
- "startDateMap"
- "testWindowEnd"
- "testWindowStart"
- "v36@0:8@16i24@28"
- "v44@?0B8q12@\"NSArray\"20@\"NSArray\"28@\"NSArray\"36"

```
