## bookdatastored

> `/System/Library/PrivateFrameworks/BookDataStore.framework/Support/bookdatastored`

```diff

-969.0.0.0.0
-  __TEXT.__text: 0x18de80
-  __TEXT.__auth_stubs: 0x3140
-  __TEXT.__objc_stubs: 0xbc00
-  __TEXT.__objc_methlist: 0x7d24
-  __TEXT.__oslogstring: 0xca09
-  __TEXT.__const: 0x4700
-  __TEXT.__cstring: 0xe816
-  __TEXT.__objc_methname: 0x1265a
+1019.0.0.0.0
+  __TEXT.__text: 0x190008
+  __TEXT.__auth_stubs: 0x3130
+  __TEXT.__objc_stubs: 0xbc20
+  __TEXT.__objc_methlist: 0x7d3c
+  __TEXT.__oslogstring: 0xc9af
+  __TEXT.__const: 0x4760
+  __TEXT.__cstring: 0xe9a6
+  __TEXT.__objc_methname: 0x1271c
   __TEXT.__objc_classname: 0x1341
-  __TEXT.__objc_methtype: 0x2d80
+  __TEXT.__objc_methtype: 0x2dd8
   __TEXT.__gcc_except_tab: 0x1244
-  __TEXT.__swift5_typeref: 0x3192
-  __TEXT.__constg_swiftt: 0x20a4
-  __TEXT.__swift5_fieldmd: 0x1828
+  __TEXT.__swift5_typeref: 0x31ce
+  __TEXT.__constg_swiftt: 0x20e0
+  __TEXT.__swift5_fieldmd: 0x1884
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_reflstr: 0x1788
+  __TEXT.__swift5_reflstr: 0x1828
   __TEXT.__swift5_assocty: 0x280
   __TEXT.__swift5_proto: 0x3a4
-  __TEXT.__swift5_types: 0x1a0
-  __TEXT.__swift5_capture: 0x20ac
+  __TEXT.__swift5_types: 0x1a4
+  __TEXT.__swift5_capture: 0x20e0
   __TEXT.__swift5_protos: 0x68
-  __TEXT.__unwind_info: 0x577c
+  __TEXT.__unwind_info: 0x57b8
   __TEXT.__eh_frame: 0x44d0
-  __DATA_CONST.__auth_got: 0x18b0
+  __DATA_CONST.__auth_got: 0x18a8
   __DATA_CONST.__got: 0x7a8
-  __DATA_CONST.__auth_ptr: 0x118
-  __DATA_CONST.__const: 0xb908
-  __DATA_CONST.__cfstring: 0x3b00
-  __DATA_CONST.__objc_classlist: 0x470
+  __DATA_CONST.__auth_ptr: 0x120
+  __DATA_CONST.__const: 0xb980
+  __DATA_CONST.__cfstring: 0x3b20
+  __DATA_CONST.__objc_classlist: 0x478
   __DATA_CONST.__objc_catlist: 0x98
-  __DATA_CONST.__objc_protolist: 0x370
+  __DATA_CONST.__objc_protolist: 0x378
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x12ca8
-  __DATA.__objc_selrefs: 0x3ca0
-  __DATA.__objc_protorefs: 0x148
+  __DATA.__objc_const: 0x12ee8
+  __DATA.__objc_selrefs: 0x3ca8
+  __DATA.__objc_protorefs: 0x150
   __DATA.__objc_classrefs: 0x6f0
   __DATA.__objc_superrefs: 0x2f8
-  __DATA.__objc_ivar: 0x738
-  __DATA.__objc_data: 0x3800
-  __DATA.__data: 0x5f20
+  __DATA.__objc_ivar: 0x740
+  __DATA.__objc_data: 0x37f0
+  __DATA.__data: 0x5fd0
   __DATA.__bss: 0x6848
   __DATA.__common: 0x1c0
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8579
-  Symbols:   538
-  CStrings:  5562
+  Functions: 8604
+  Symbols:   537
+  CStrings:  5580
 
Symbols:
- _BUIsGDPRAcknowledgementNeededForBooks
CStrings:
+ "2\x1b"
+ "@\"NSObject<BDSReadingHistoryCommandLineServiceSupport>\""
+ "@80@0:8@16@24@32@40@48@56@64@72"
+ "BCCloudSecureUserData"
+ "BDSMediaAPIService.m"
+ "BDSReadingHistoryCommandLineServiceSupport"
+ "T@\"NSObject<BDSReadingHistoryCommandLineServiceSupport>\",&,N,V_readingHistoryCommandLineService"
+ "[%@ '%@' %@ %@ %@ (%.0f%%) %@%@]"
+ "_TtC14bookdatastored27CloudSecureUserDataMigrator"
+ "_readingHistoryCommandLineService"
+ "fetchMixedAssetsWithBookIds:audiobookIds:relationships:views:additionalParameters:batchSize:fileID:line:completionHandler:"
+ "fetchResourcesWithAdamIDs:relationships:views:additionalParameters:batchSize:fileID:line:completionHandler:"
+ "genreName"
+ "genres"
+ "initWithAssetID:title:pageProgressionDirection:coverURL:readingProgress:cloudAssetType:libraryAssetType:"
+ "initWithAssetID:title:pageProgressionDirection:coverURL:readingProgress:totalDuration:cloudAssetType:libraryAssetType:"
+ "migrateIfNecessary()"
+ "migrateIfNecessary() No data to write to new data source"
+ "migrateIfNecessary() error %s"
+ "migrateIfNecessary() error reading %s %s"
+ "migrateIfNecessary() migrating data to new data source"
+ "migrateIfNecessary() needsMigration=true"
+ "migrateIfNecessary() unable to insert key/value pair %s=%s"
+ "migrateOldUserDataGenerationKey"
+ "migratedSecureUserDataGeneration"
+ "oldSecureUserDataModelName"
+ "oldUserDataMigrationGeneration"
+ "persistentStoreOptions"
+ "readingHistoryCommandLineService"
+ "rootDirectoryName"
+ "setReadingHistoryCommandLineService:"
- "2\x1a"
- "ReadingHistoryService DONE readingHistoryModelSnapshotInfo (currentTime: %@), stateInfo: %@"
- "ReadingHistoryService readingHistoryModelSnapshotInfo ( currentTime: %@)"
- "ReadingHistoryServiceManager readingHistoryModelSnapshotInfo ( currentTime: %@)"
- "Startup: Tried to launch bookdatastored before user has accepted books GDPR. Kill process"
- "[%@ '%@' %@ %@ (%.0f%%) %@%@]"
- "fetchMixedAssetsWithBookIds:audiobookIds:relationships:views:additionalParameters:batchSize:completionHandler:"
- "fetchResourcesWithAdamIDs:relationships:views:additionalParameters:batchSize:completionHandler:"
- "genre"
- "initWithAssetID:title:pageProgressionDirection:coverURL:readingProgress:libraryAssetType:"
- "initWithAssetID:title:pageProgressionDirection:coverURL:readingProgress:totalDuration:libraryAssetType:"
- "readingHistoryModelSnapshotInfoWithCurrentTime:completionHandler:"
- "v32@0:8@\"NSDate\"16@?<v@?@\"BDSReadingHistoryModelSnapshotInfo\"B>24"

```
