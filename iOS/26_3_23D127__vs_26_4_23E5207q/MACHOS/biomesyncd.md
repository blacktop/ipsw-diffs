## biomesyncd

> `/usr/libexec/biomesyncd`

```diff

-200.6.0.0.0
-  __TEXT.__text: 0x4be00
-  __TEXT.__auth_stubs: 0xcf0
-  __TEXT.__objc_stubs: 0x86e0
-  __TEXT.__objc_methlist: 0x3ba4
+209.12.1.0.0
+  __TEXT.__text: 0x4e4dc
+  __TEXT.__auth_stubs: 0xca0
+  __TEXT.__objc_stubs: 0x8800
+  __TEXT.__objc_methlist: 0x3bf4
   __TEXT.__const: 0x1348
-  __TEXT.__gcc_except_tab: 0x9f8
-  __TEXT.__objc_methname: 0xa0f1
-  __TEXT.__cstring: 0x57fb
+  __TEXT.__gcc_except_tab: 0x9fc
+  __TEXT.__objc_methname: 0xa23f
+  __TEXT.__cstring: 0x58e8
   __TEXT.__objc_classname: 0x83d
-  __TEXT.__objc_methtype: 0x16f1
-  __TEXT.__oslogstring: 0x604e
-  __TEXT.__unwind_info: 0x1040
-  __DATA_CONST.__auth_got: 0x688
-  __DATA_CONST.__got: 0x3d0
+  __TEXT.__objc_methtype: 0x16fe
+  __TEXT.__oslogstring: 0x63bf
+  __TEXT.__unwind_info: 0x1170
+  __DATA_CONST.__auth_got: 0x660
+  __DATA_CONST.__got: 0x3d8
   __DATA_CONST.__const: 0x10d8
-  __DATA_CONST.__cfstring: 0x45e0
+  __DATA_CONST.__cfstring: 0x46e0
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x1a0
-  __DATA_CONST.__objc_arraydata: 0x568
-  __DATA_CONST.__objc_arrayobj: 0x870
-  __DATA_CONST.__objc_intobj: 0x2d0
+  __DATA_CONST.__objc_arraydata: 0x5a0
+  __DATA_CONST.__objc_arrayobj: 0x8a0
+  __DATA_CONST.__objc_intobj: 0x2e8
   __DATA_CONST.__linkguard: 0xe
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x76d8
-  __DATA.__objc_selrefs: 0x2848
-  __DATA.__objc_ivar: 0x3e8
+  __DATA.__objc_const: 0x76f8
+  __DATA.__objc_selrefs: 0x2890
+  __DATA.__objc_ivar: 0x3ec
   __DATA.__objc_data: 0x1180
   __DATA.__data: 0x840
   __DATA.__bss: 0xf0

   - /System/Library/PrivateFrameworks/ProactiveSupport.framework/ProactiveSupport
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
+  - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /usr/appleinternal/lib/liblinkguard.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 980C951E-62FE-3C3A-95E9-E8A2E9856DD0
-  Functions: 1598
-  Symbols:   347
-  CStrings:  3629
+  UUID: 0BBFCA94-E691-3312-8484-7AE370E2D088
+  Functions: 1627
+  Symbols:   343
+  CStrings:  3668
 
Symbols:
+ _OBJC_CLASS_$_TRIClient
- _objc_claimAutoreleasedReturnValue
- _objc_release_x2
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x5
- _objc_retain_x6
CStrings:
+ "\f"
+ " AND id NOT IN (SELECT location_id FROM CKRecord WHERE record_type = ?"
+ " AND state != ?"
+ " AND stream_identifier = ?)"
+ "@\"TRIClient\""
+ "Backfilled %lu CKRecord entries for stream: %@ (success: %d)"
+ "Backfilling missing CKRecords for stream: %@"
+ "CKRecord backfill already completed for stream: %@"
+ "CKRecordBackfillCompleted_"
+ "Error adding deltas to save for (recordName: %{public}@) (zoneName: %{public}@) (error: %{public}@)"
+ "Failed to backfill CKRecord for location: %@ (site: %@, day: %@) - %@"
+ "Failed to backfill CKRecords for stream: %@. Will retry on next sync."
+ "Found %lu CRDTLocation rows without CKRecord entries for stream: %@"
+ "INTELLIGENCE_PLATFORM_BIOME_SYNC_CONFIG"
+ "No CKRecord entries needed backfilling for stream: %@"
+ "Starting backfill of CKRecords for CloudKit sync on stream: %@"
+ "Successfully backfilled %lu CKRecord entries for CloudKit sync on stream: %@"
+ "Sync to iCloud for stream %{public}@ disabled [syncEnabledOnAccount: %d] [syncDisabledOnTrial: %d]"
+ "Sync to iCloud for stream %{public}@ is enabled"
+ "Syncing recordValue %{public}@ for stream %{public}@ with default maxInlineDeltaSize"
+ "Syncing recordValue %{public}@ for stream %{public}@ with maxInlineDeltaSize %{public}@"
+ "_trialClient"
+ "addDeltasToSaveFromMergeable:maxInlineDeltaSize:error:"
+ "asset_threshold_override_"
+ "backfillCKRecordsForCloudKitSync"
+ "backfillMissingCKRecordsForStream:backfilledCount:"
+ "booleanValue"
+ "cloudSyncDisabledOnTrial:"
+ "day ASC"
+ "getMaxInlineDeltaSizeOverride:"
+ "hasCompletedCKRecordBackfillForStream:"
+ "icloud_sync_enabled_"
+ "levelForFactor:withNamespaceName:"
+ "setCompletedCKRecordBackfillForStream:"
- "\v"
- "Error adding deltas to save for %{public}@ %{public}@ %{public}@"
- "Sync to iCloud for Siri disabled"

```
