## HomeKitBackingStore

> `/System/Library/PrivateFrameworks/HomeKitBackingStore.framework/HomeKitBackingStore`

```diff

-1520.2.7.1.3
-  __TEXT.__text: 0x9c0c4
+1535.0.0.0.2
+  __TEXT.__text: 0x9c63c
   __TEXT.__objc_methlist: 0x54b4
   __TEXT.__const: 0x140
-  __TEXT.__gcc_except_tab: 0x521c
-  __TEXT.__cstring: 0x74d0
-  __TEXT.__oslogstring: 0x1902e
+  __TEXT.__gcc_except_tab: 0x5310
+  __TEXT.__cstring: 0x7505
+  __TEXT.__oslogstring: 0x191c7
   __TEXT.__unwind_info: 0x2210
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x2d0
   __DATA_CONST.__objc_arraydata: 0x98
-  __DATA_CONST.__got: 0x590
+  __DATA_CONST.__got: 0x598
   __AUTH_CONST.__const: 0x8a0
-  __AUTH_CONST.__cfstring: 0x45c0
+  __AUTH_CONST.__cfstring: 0x45e0
   __AUTH_CONST.__objc_const: 0xae10
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_arrayobj: 0x60

   __DATA.__objc_ivar: 0x5c0
   __DATA.__data: 0x910
   __DATA_DIRTY.__objc_data: 0x1d10
-  __DATA_DIRTY.__bss: 0x1b0
+  __DATA_DIRTY.__bss: 0x1a0
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /usr/lib/libz.1.dylib
   Functions: 2136
   Symbols:   4316
-  CStrings:  2410
+  CStrings:  2417
 
Functions:
~ -[HMBLocalZone(Process) _processItemsForBlockRow:error:] : 25468 -> 26440
~ -[HMBLocalSQLQueryTable prepareWithError:] : 5740 -> 6176
~ ___59-[HMBLocalZone(Record_Internal) removeAllRecordsWithError:]_block_invoke : 488 -> 480
CStrings:
+ "CREATE INDEX IF NOT EXISTS rid_%@ ON %@ (_record_id)"
+ "Failed to update schema version to current version %lu: %@"
+ "Unable to create record index %@: %@"
+ "[%{public}@] Dropped output block %lu since no records were staged for it"
+ "[%{public}@] Failed to drop output block %lu: domain=%{public}@ code=%ld"
+ "[%{public}@] Failed to update schema version to current version %lu: %@"
+ "[%{public}@] Unable to clean up rollback block: %@"
+ "[%{public}@] Unable to create record index %@: %@"
+ "[%{public}@] [%{public}@] Dropped output block %lu since no records were staged for it"
+ "[%{public}@] [%{public}@] Failed to drop output block %lu: domain=%{public}@ code=%ld"
+ "[%{public}@] [%{public}@] Unable to clean up rollback block: %@"
+ "[%{public}@] [%{public}@] unable to clean up corrupt block: %@"
+ "[%{public}@] unable to clean up corrupt block: %@"
- "Failed to updated schema version to current version %lu: %@"
- "[%{public}@] Failed to updated schema version to current version %lu: %@"
- "[%{public}@] Unable to cleanup rollback block: %@"
- "[%{public}@] [%{public}@] Unable to cleanup rollback block: %@"
- "[%{public}@] [%{public}@] unable to cleanup corrupt block: %@"
- "[%{public}@] unable to cleanup corrupt block: %@"
```
