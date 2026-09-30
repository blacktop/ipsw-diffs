## HealthRecordsPlugin

> `/System/Library/PrivateFrameworks/HealthRecordsPlugin.framework/HealthRecordsPlugin`

```diff

 7027.0.72.2.7
-  __TEXT.__text: 0xb6428
+  __TEXT.__text: 0xb6420
   __TEXT.__objc_methlist: 0x780c
   __TEXT.__const: 0xa30
   __TEXT.__cstring: 0x978f

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3548
+  Functions: 3549
   Symbols:   7806
   CStrings:  1779
 
Functions:
~ -[HDClinicalDailyAnalyticsManager _fetchAccountAnalyticsCollectsClinicalOptInData:collectsImproveHealthAndActivityData:error:] : 1552 -> 1548
+ _OUTLINED_FUNCTION_0
~ -[HDHealthRecordsProfileExtension _ivarLock_updateHealthRecordsSupportedStatus].cold.1 : 60 -> 56
~ -[HDHealthRecordsProfileExtension _supportedFHIRConfiguration].cold.1 : 60 -> 56
~ ___76-[HDHealthRecordsProfileExtension didUpdateSourcesForAccountWithIdentifier:]_block_invoke.cold.1 : 76 -> 64
~ -[HDHealthRecordsProfileExtension notificationSyncClient:didReceiveInstructionWithAction:].cold.1 : 104 -> 100
~ -[HDHealthRecordsProfileExtension _deleteSignedClinicalDataRecords].cold.1 : 60 -> 56
```
