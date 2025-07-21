## CoreData

> `/System/Library/Frameworks/CoreData.framework/CoreData`

```diff

-1448.0.0.0.0
-  __TEXT.__text: 0x3085e0
+1448.1.0.0.0
+  __TEXT.__text: 0x30793c
   __TEXT.__auth_stubs: 0x2470
   __TEXT.__objc_methlist: 0x10c6c
   __TEXT.__const: 0x1250
-  __TEXT.__cstring: 0x4b07a
+  __TEXT.__cstring: 0x4b07f
   __TEXT.__swift5_typeref: 0x346
   __TEXT.__swift5_capture: 0x25c
   __TEXT.__constg_swiftt: 0x14c

   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0xc
   __TEXT.__swift5_fieldmd: 0x12c
-  __TEXT.__gcc_except_tab: 0x1b784
-  __TEXT.__oslogstring: 0x31873
-  __TEXT.__unwind_info: 0x73e8
+  __TEXT.__gcc_except_tab: 0x1b420
+  __TEXT.__oslogstring: 0x317e9
+  __TEXT.__unwind_info: 0x73a0
   __TEXT.__eh_frame: 0x5e0
   __TEXT.__objc_classname: 0x3b84
   __TEXT.__objc_methname: 0x1e7ea
   __TEXT.__objc_methtype: 0x4de5
   __TEXT.__objc_stubs: 0x13f80
   __DATA_CONST.__got: 0x950
-  __DATA_CONST.__const: 0x49c8
+  __DATA_CONST.__const: 0x49a0
   __DATA_CONST.__objc_classlist: 0x1018
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x138

   __DATA_CONST.__objc_arraydata: 0x6678
   __AUTH_CONST.__auth_got: 0x1248
   __AUTH_CONST.__const: 0x16c8
-  __AUTH_CONST.__cfstring: 0x25c40
+  __AUTH_CONST.__cfstring: 0x25c20
   __AUTH_CONST.__objc_const: 0x2ac60
   __AUTH_CONST.__objc_dictobj: 0x1f18
   __AUTH_CONST.__objc_intobj: 0x558

   - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: ACD19609-C79A-396C-AE59-67AC9CF2E5B5
+  UUID: 80D683C7-B791-3F93-98F7-E53306D5F056
   Functions: 8901
-  Symbols:   28901
-  CStrings:  20182
+  Symbols:   28894
+  CStrings:  20178
 
Symbols:
+ ___85-[PFCloudKitMetadataModelMigrator checkForRecordMetadataZoneCorruptionInStore:error:]_block_invoke
+ ___85-[PFCloudKitMetadataModelMigrator checkForRecordMetadataZoneCorruptionInStore:error:]_block_invoke_2
- ___98-[PFCloudKitMetadataModelMigrator checkForRecordMetadataZoneCorruptionInStore:usingContext:error:]_block_invoke
- ___98-[PFCloudKitMetadataModelMigrator checkForRecordMetadataZoneCorruptionInStore:usingContext:error:]_block_invoke_2
- ___block_descriptor_80_e8_32o40o48o56o64r72r_e37_v40?0"NSArray"8"NSError"16^B24^B32ls32l8s40l8s48l8s56l8r64l8r72l8
Functions:
~ ___69-[PFCloudKitMetadataModelMigrator commitMigrationMetadataAndCleanup:]_block_invoke : 8384 -> 7908
~ -[PFCloudKitMetadataModelMigrator checkForOrphanedMirroredRelationshipsInStore:inManagedObjectContext:error:] : 1416 -> 1204
~ -[PFCloudKitMetadataModelMigrator checkForCorruptedRecordMetadataInStore:inManagedObjectContext:error:] : 1536 -> 1392
~ -[PFCloudKitMetadataModelMigrator cleanUpAfterClientMigrationWithStore:andContext:error:] : 1688 -> 1404
~ -[PFCloudKitMetadataModelMigrator checkAndPerformMigrationIfNecessary:] : 1848 -> 1920
~ ___98-[PFCloudKitMetadataModelMigrator checkForRecordMetadataZoneCorruptionInStore:usingContext:error:]_block_invoke -> ___85-[PFCloudKitMetadataModelMigrator checkForRecordMetadataZoneCorruptionInStore:error:]_block_invoke : 2360 -> 1576
~ ___98-[PFCloudKitMetadataModelMigrator checkForRecordMetadataZoneCorruptionInStore:usingContext:error:]_block_invoke_2 -> ___85-[PFCloudKitMetadataModelMigrator checkForRecordMetadataZoneCorruptionInStore:error:]_block_invoke_2 : 1096 -> 872
~ ___107-[PFCloudKitMetadataModelMigrator migrateMetadataForObjectsInStore:toNSCKRecordMetadataUsingContext:error:]_block_invoke : 1540 -> 964
~ ___149-[PFCloudKitMetadataModelMigrator addMigrationStatementsToDeleteDuplicateMirroredRelationshipsToContext:withManagedObjectContext:andSQLEntity:error:]_block_invoke : 1612 -> 1256
~ ___89-[PFCloudKitMetadataModelMigrator cleanUpAfterClientMigrationWithStore:andContext:error:]_block_invoke : 804 -> 552
CStrings:
+ "-[PFCloudKitMetadataModelMigrator checkForRecordMetadataZoneCorruptionInStore:error:]_block_invoke_2"
+ "ckRecordSystemFields != NULL"
+ "ckRecordSystemFields == NULL"
- "%K != NULL"
- "%K == NULL"
- "-[PFCloudKitMetadataModelMigrator checkForRecordMetadataZoneCorruptionInStore:usingContext:error:]_block_invoke_2"
- "CoreData: Unable to find a system fields attribute on entity: %@"
- "CoreData: fault: Unable to find a system fields attribute on entity: %@\n"
- "systemFieldsAsset"

```
