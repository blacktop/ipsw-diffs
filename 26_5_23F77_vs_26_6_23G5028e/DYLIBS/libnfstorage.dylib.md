## libnfstorage.dylib

> `/usr/lib/libnfstorage.dylib`

```diff

-365.3.1.0.0
-  __TEXT.__text: 0x448c
-  __TEXT.__auth_stubs: 0x290
-  __TEXT.__objc_methlist: 0x168
+366.4.0.0.0
+  __TEXT.__text: 0x84a0
+  __TEXT.__auth_stubs: 0x2a0
+  __TEXT.__objc_methlist: 0x268
   __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x6af
-  __TEXT.__oslogstring: 0x416
-  __TEXT.__unwind_info: 0xd8
-  __TEXT.__objc_classname: 0xee
-  __TEXT.__objc_methname: 0x894
-  __TEXT.__objc_methtype: 0x96
-  __TEXT.__objc_stubs: 0xb40
-  __DATA_CONST.__got: 0xe0
-  __DATA_CONST.__const: 0x118
-  __DATA_CONST.__objc_classlist: 0x48
+  __TEXT.__cstring: 0xe48
+  __TEXT.__oslogstring: 0x546
+  __TEXT.__unwind_info: 0x118
+  __TEXT.__objc_classname: 0x185
+  __TEXT.__objc_methname: 0xcec
+  __TEXT.__objc_methtype: 0xeb
+  __TEXT.__objc_stubs: 0x10e0
+  __DATA_CONST.__got: 0xf0
+  __DATA_CONST.__const: 0x208
+  __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x308
-  __AUTH_CONST.__auth_got: 0x150
-  __AUTH_CONST.__cfstring: 0x480
-  __AUTH_CONST.__objc_const: 0x830
-  __AUTH_CONST.__objc_intobj: 0xd8
-  __AUTH.__objc_data: 0xf0
+  __DATA_CONST.__objc_selrefs: 0x4b0
+  __AUTH_CONST.__auth_got: 0x158
+  __AUTH_CONST.__cfstring: 0x760
+  __AUTH_CONST.__objc_const: 0xbc8
+  __AUTH_CONST.__objc_intobj: 0x198
+  __AUTH.__objc_data: 0x230
   __DATA.__objc_ivar: 0xc
   __DATA.__data: 0x60
   __DATA_DIRTY.__objc_data: 0x1e0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0FEAB285-2A7D-3A9A-AB1D-C54166115F4F
-  Functions: 34
-  Symbols:   83
-  CStrings:  253
+  UUID: 8335911B-0FE2-34B9-97BC-2CC853F19986
+  Functions: 60
+  Symbols:   88
+  CStrings:  385
 
Symbols:
+ _OBJC_CLASS_$_NFStorageControllerDeveloperPresentment
+ _OBJC_CLASS_$_NSPredicate
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_METACLASS_$_NFStorageControllerDeveloperPresentment
+ _objc_retain_x25
CStrings:
+ ""
+ "%{public}s:%i Failed to delete presentment entities: %{public}@"
+ "%{public}s:%i Failed to delete receipt entities: %{public}@"
+ "%{public}s:%i Failed to delete report entities: %{public}@"
+ "%{public}s:%i No receipt found for bundleID=%{public}@ teamID=%{public}@"
+ "%{public}s:%i No report found for id %{public}@"
+ "-[NFStorageControllerDeveloperPresentment deleteAllReportReceipts]"
+ "-[NFStorageControllerDeveloperPresentment deleteAllReportReceipts]_block_invoke"
+ "-[NFStorageControllerDeveloperPresentment deleteAllReports]"
+ "-[NFStorageControllerDeveloperPresentment deleteAllReports]_block_invoke"
+ "-[NFStorageControllerDeveloperPresentment deleteReportWithId:]"
+ "-[NFStorageControllerDeveloperPresentment deleteReportWithId:]_block_invoke"
+ "-[NFStorageControllerDeveloperPresentment fetchReportWithId:error:]"
+ "-[NFStorageControllerDeveloperPresentment fetchReportWithId:error:]_block_invoke"
+ "-[NFStorageControllerDeveloperPresentment fetchReportsWithError:]"
+ "-[NFStorageControllerDeveloperPresentment fetchReportsWithError:]_block_invoke"
+ "-[NFStorageControllerDeveloperPresentment getLastReportReceiptForBundleID:teamID:outSentTimestamp:outIsOnDenyList:]"
+ "-[NFStorageControllerDeveloperPresentment getLastReportReceiptForBundleID:teamID:outSentTimestamp:outIsOnDenyList:]_block_invoke"
+ "-[NFStorageControllerDeveloperPresentment savePresentmentWithBundleID:teamID:timestampDay:presentmentData:savedToReport:reportReadyToSend:]"
+ "-[NFStorageControllerDeveloperPresentment savePresentmentWithBundleID:teamID:timestampDay:presentmentData:savedToReport:reportReadyToSend:]_block_invoke"
+ "-[NFStorageControllerDeveloperPresentment updatePresentmentReportReceiptWithBundleID:teamID:sentTimestamp:isOnDenyList:]"
+ "-[NFStorageControllerDeveloperPresentment updatePresentmentReportReceiptWithBundleID:teamID:sentTimestamp:isOnDenyList:]_block_invoke"
+ "@32@0:8@16^@24"
+ "@44@0:8@16@24d32B40"
+ "@48@0:8@16@24^d32^B40"
+ "@64@0:8@16@24Q32@40^@48^B56"
+ "DeveloperPresentment"
+ "DeveloperPresentmentEntity"
+ "DeveloperPresentmentReportEntity"
+ "DeveloperPresentmentReportReceiptEntity"
+ "Dictionary"
+ "NFStorageControllerDeveloperPresentment"
+ "T@\"DeveloperPresentmentReportEntity\",&,D,N"
+ "T@\"NSOrderedSet\",&,D,N"
+ "T@\"NSUUID\",C,D,N"
+ "Td,D,N"
+ "UUID"
+ "UUIDString"
+ "addDeveloperPresentmentsObject:"
+ "altitude"
+ "arrayWithCapacity:"
+ "bundleID"
+ "bundleId"
+ "bundleId == %@ AND teamId == %@"
+ "bundleId == %@ AND teamId == %@ AND timestampDay == %llu AND developerPresentments.@count < %d"
+ "city"
+ "country"
+ "deleteAllReportReceipts"
+ "deleteAllReports"
+ "deleteObject:"
+ "deleteReportWithId:"
+ "developerPresentments"
+ "developmentPresentments"
+ "doubleValue"
+ "endTimestamp"
+ "fetchReportWithId:error:"
+ "fetchReportsWithError:"
+ "getLastReportReceiptForBundleID:teamID:outSentTimestamp:outIsOnDenyList:"
+ "horizontalAccuracy"
+ "isOnDenyList"
+ "lastReportSentTimestamp"
+ "latitude"
+ "longitude"
+ "numberWithDouble:"
+ "numberWithLongLong:"
+ "populateFromDictionary:"
+ "predicateWithFormat:"
+ "reportId"
+ "reportId == %@"
+ "savePresentmentWithBundleID:teamID:timestampDay:presentmentData:savedToReport:reportReadyToSend:"
+ "setAltitude:"
+ "setBundleId:"
+ "setCity:"
+ "setCountry:"
+ "setEndTimestamp:"
+ "setHorizontalAccuracy:"
+ "setIsOnDenyList:"
+ "setLastReportSentTimestamp:"
+ "setLatitude:"
+ "setLongitude:"
+ "setPredicate:"
+ "setReportId:"
+ "setStartTimestamp:"
+ "setState:"
+ "setSuccessfulTapCount:"
+ "setTeamId:"
+ "setTimestampDay:"
+ "startTimestamp"
+ "state"
+ "successfulTapCount"
+ "teamID"
+ "teamId"
+ "timestampDay"
+ "toDictionary"
+ "updatePresentmentReportReceiptWithBundleID:teamID:sentTimestamp:isOnDenyList:"

```
