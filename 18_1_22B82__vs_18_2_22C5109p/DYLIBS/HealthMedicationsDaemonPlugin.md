## HealthMedicationsDaemonPlugin

> `/System/Library/PrivateFrameworks/HealthMedicationsDaemonPlugin.framework/HealthMedicationsDaemonPlugin`

```diff

-5200.1.18.0.0
-  __TEXT.__text: 0x53fc0
-  __TEXT.__auth_stubs: 0xb80
-  __TEXT.__objc_methlist: 0x3964
+5200.2.4.1.5
+  __TEXT.__text: 0x55098
+  __TEXT.__auth_stubs: 0xb70
+  __TEXT.__objc_methlist: 0x3a44
   __TEXT.__const: 0x190
-  __TEXT.__cstring: 0x5fe1
+  __TEXT.__cstring: 0x624b
   __TEXT.__gcc_except_tab: 0xab8
-  __TEXT.__oslogstring: 0x6082
+  __TEXT.__oslogstring: 0x60df
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x1320
-  __TEXT.__objc_classname: 0x119f
-  __TEXT.__objc_methname: 0xebd0
-  __TEXT.__objc_methtype: 0x2667
-  __TEXT.__objc_stubs: 0x8880
-  __DATA_CONST.__got: 0x820
-  __DATA_CONST.__const: 0x1b38
-  __DATA_CONST.__objc_classlist: 0x2a8
+  __TEXT.__unwind_info: 0x1370
+  __TEXT.__objc_classname: 0x120a
+  __TEXT.__objc_methname: 0xee3e
+  __TEXT.__objc_methtype: 0x2655
+  __TEXT.__objc_stubs: 0x8940
+  __DATA_CONST.__got: 0x838
+  __DATA_CONST.__const: 0x1c38
+  __DATA_CONST.__objc_classlist: 0x2b8
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2d60
+  __DATA_CONST.__objc_selrefs: 0x2da8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x188
-  __DATA_CONST.__objc_arraydata: 0x2c8
-  __AUTH_CONST.__auth_got: 0x5d0
-  __AUTH_CONST.__const: 0x420
-  __AUTH_CONST.__cfstring: 0x33a0
-  __AUTH_CONST.__objc_const: 0x88a8
+  __DATA_CONST.__objc_superrefs: 0x190
+  __DATA_CONST.__objc_arraydata: 0x2d0
+  __AUTH_CONST.__auth_got: 0x5c8
+  __AUTH_CONST.__const: 0x460
+  __AUTH_CONST.__cfstring: 0x3460
+  __AUTH_CONST.__objc_const: 0x8a50
   __AUTH_CONST.__objc_intobj: 0x4b0
-  __AUTH_CONST.__objc_arrayobj: 0x288
+  __AUTH_CONST.__objc_arrayobj: 0x2a0
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x500
-  __DATA.__objc_ivar: 0x38c
+  __AUTH.__objc_data: 0x5a0
+  __DATA.__objc_ivar: 0x390
   __DATA.__data: 0x1140
   __DATA.__bss: 0x8
   __DATA_DIRTY.__objc_data: 0x1590

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1784
-  Symbols:   2396
-  CStrings:  3080
+  Functions: 1811
+  Symbols:   2427
+  CStrings:  3100
 
Symbols:
+ _HDDismissedRemoteScheduleUnavailableRecordEntityMedicationIdentifier
+ _HDDismissedRemoteScheduleUnavailableRecordsForMedicationSemanticIdentifiers
+ _OBJC_CLASS_$_HDDismissedRemoteScheduleUnavailableRecordEntity
+ _OBJC_CLASS_$_HKDismissedRemoteScheduleUnavailableRecord
+ _OBJC_METACLASS_$_HDDismissedRemoteScheduleUnavailableRecordEntity
+ __HKDismissedRemoteScheduleUnavailableRecordDeviceSeparator
- _objc_release_x10
CStrings:
+ "%!@(MISSING): medication.semanticIdentifier must not be nil"
+ "@16@?0@\"HKRemoteScheduleUnavailableRecord\"8"
+ "B24@?0@\"HKDismissedRemoteScheduleUnavailableRecord\"8^@16"
+ "CREATE TABLE IF NOT EXISTS medication_dismissed_remote_schedule_unavailable_records (ROWID INTEGER PRIMARY KEY AUTOINCREMENT, medication_identifier TEXT UNIQUE NOT NULL, schedule_type INTEGER NOT NULL, schedule_compatibility_version INTEGER NOT NULL, device_identifiers TEXT NOT NULL, creation_date REAL NOT NULL)"
+ "HDDismissedRemoteScheduleUnavailableRecordEntity"
+ "HDDismissedRemoteScheduleUnavailableRecordInsertOperation"
+ "[%!{(MISSING)public}@]: Timezone has changed, but setting experience disabled failed with '%!{(MISSING)public}@'"
+ "_createRemoteScheduleUnavailableRecordsTableWithTransaction:error:"
+ "_dismissedRecords"
+ "_initWithMedicationIdentifier:scheduleType:scheduleCompatibilityVersion:deviceIdentifiers:creationDate:"
+ "deviceIdentifiersDatabaseString"
+ "device_identifiers"
+ "dismissedRecord"
+ "dismissed_remote_schedule_unavailable_records"
+ "enumerateDismissedRemoteScheduleUnavailableRecordEntitiesWithPredicate:transaction:error:enumerationHandler:"
+ "initWithRemoteScheduleUnavailableRecords:"
+ "insertDismissedRemoteScheduleUnavailableRecords:profile:error:"
+ "medication_dismissed_remote_schedule_unavailable_records"
+ "remote_allDismissedRemoteScheduleUnavailableRecordsWithCompletion:"
+ "remote_deleteDismissedRemoteScheduleUnavailableForMedication:completion:"
+ "remote_markRemoteScheduleUnavailableRecordsAsDismissed:completion:"
+ "schedule_compatibility_version"
- "B40@0:8q16@24^@32"
- "decodeArrayOfObjectsOfClass:forKey:"

```
