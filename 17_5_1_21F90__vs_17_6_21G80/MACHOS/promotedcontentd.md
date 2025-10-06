## promotedcontentd

> `/usr/libexec/promotedcontentd`

```diff

-511.16.0.0.0
-  __TEXT.__text: 0x19bbe8
-  __TEXT.__auth_stubs: 0x21a0
-  __TEXT.__objc_stubs: 0x16ec0
-  __TEXT.__objc_methlist: 0x12a34
-  __TEXT.__const: 0x13210
-  __TEXT.__objc_methname: 0x22cd4
-  __TEXT.__oslogstring: 0xba00
-  __TEXT.__cstring: 0xded1
-  __TEXT.__objc_classname: 0x24af
-  __TEXT.__objc_methtype: 0x477c
-  __TEXT.__gcc_except_tab: 0xdc8
+512.6.0.0.0
+  __TEXT.__text: 0x19f774
+  __TEXT.__auth_stubs: 0x21d0
+  __TEXT.__objc_stubs: 0x172e0
+  __TEXT.__objc_methlist: 0x12d9c
+  __TEXT.__const: 0x13220
+  __TEXT.__objc_methname: 0x2335a
+  __TEXT.__oslogstring: 0xbb75
+  __TEXT.__cstring: 0xe261
+  __TEXT.__objc_classname: 0x2514
+  __TEXT.__objc_methtype: 0x4862
+  __TEXT.__gcc_except_tab: 0xe54
   __TEXT.__constg_swiftt: 0x1f4c
-  __TEXT.__swift5_typeref: 0x15f8
+  __TEXT.__swift5_typeref: 0x15f4
   __TEXT.__swift5_fieldmd: 0x17b8
   __TEXT.__swift5_types: 0x1d4
   __TEXT.__swift5_reflstr: 0xe03

   __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_protos: 0x64
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x4b1c
-  __TEXT.__eh_frame: 0x1fa8
-  __DATA_CONST.__auth_got: 0x10e0
-  __DATA_CONST.__got: 0x698
-  __DATA_CONST.__auth_ptr: 0x1a8
-  __DATA_CONST.__const: 0xbbc8
-  __DATA_CONST.__cfstring: 0xe400
-  __DATA_CONST.__objc_classlist: 0xbb0
+  __TEXT.__unwind_info: 0x4c5c
+  __TEXT.__eh_frame: 0x2020
+  __DATA_CONST.__auth_got: 0x10f8
+  __DATA_CONST.__got: 0x6a0
+  __DATA_CONST.__auth_ptr: 0x1b8
+  __DATA_CONST.__const: 0xbc88
+  __DATA_CONST.__cfstring: 0xe500
+  __DATA_CONST.__objc_classlist: 0xbd8
   __DATA_CONST.__objc_catlist: 0xc0
-  __DATA_CONST.__objc_protolist: 0x248
+  __DATA_CONST.__objc_protolist: 0x258
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0xe0
-  __DATA_CONST.__objc_classrefs: 0xda0
-  __DATA_CONST.__objc_superrefs: 0x6e0
+  __DATA_CONST.__objc_protorefs: 0xe8
+  __DATA_CONST.__objc_classrefs: 0xdd0
+  __DATA_CONST.__objc_superrefs: 0x6f8
   __DATA_CONST.__linkguard: 0x15
   __DATA_CONST.__objc_intobj: 0x1698
   __DATA_CONST.__objc_arraydata: 0x700
   __DATA_CONST.__objc_dictobj: 0xa28
   __DATA_CONST.__objc_arrayobj: 0x90
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0x262b0
-  __DATA.__objc_selrefs: 0x8640
-  __DATA.__objc_ivar: 0x1434
-  __DATA.__objc_data: 0x6e08
-  __DATA.__data: 0x6978
+  __DATA.__objc_const: 0x26a90
+  __DATA.__objc_selrefs: 0x8778
+  __DATA.__objc_ivar: 0x1484
+  __DATA.__objc_data: 0x6fd8
+  __DATA.__data: 0x6a68
   __DATA.__bss: 0x4cd0
   __DATA.__common: 0xf8
   - /System/Library/Frameworks/AdServices.framework/AdServices

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 29AC7AF0-D141-351B-81A2-6B35107FD3C6
-  Functions: 8479
-  Symbols:   2032
-  CStrings:  12332
+  UUID: 8FA3A480-E738-30AE-84BB-806B8B307A59
+  Functions: 8572
+  Symbols:   2042
+  CStrings:  12443
 
Symbols:
+ OBJC_IVAR_$_APPBLogMetaData._duration
+ _OBJC_CLASS_$_APSponsorshipPlacementConfig
+ _OBJC_CLASS_$_APTimeSpentEntry
+ _OBJC_CLASS_$_APTimeSpentEventRequester
+ _OBJC_CLASS_$_APTimeSpentLegacyInterface
+ _OBJC_CLASS_$_APTimeSpentStoreDatabase
+ _OBJC_METACLASS_$_APTimeSpentEntry
+ _OBJC_METACLASS_$_APTimeSpentEventRequester
+ _OBJC_METACLASS_$_APTimeSpentLegacyInterface
+ _OBJC_METACLASS_$_APTimeSpentStoreDatabase
CStrings:
+ "\x01\x15"
+ "\x0f\x01"
+ "%{public}@."
+ "2\x12\x11\x12\x12#\x12"
+ "@\"APDatabaseManager\""
+ "@\"APTimeSpentLegacyInterface\""
+ "@\"NSArray\"24@0:8@\"NSDate\"16"
+ "@\"NSURLSessionDataTask\""
+ "@24@0:8@\"APDatabaseManager\"16"
+ "@88@0:8@16@24@32@40@48@56@64d72@80"
+ "APTimeSpentEntry"
+ "APTimeSpentEventRequester"
+ "APTimeSpentLegacyInterface"
+ "APTimeSpentReportActivity"
+ "APTimeSpentStore"
+ "APTimeSpentStoreDatabase"
+ "B36@0:8@16@24B32"
+ "DELETE FROM TimeSpent WHERE contentId IN ("
+ "ExpiredAnonId"
+ "INSERT OR REPLACE INTO TimeSpent(contentId,timeStamp) VALUES (?,?)"
+ "ManagedContentNotFound"
+ "ManagedContextNotFound"
+ "No managed content data for %{public}@."
+ "Request Time Spent Report activity deferral."
+ "R\xc1"
+ "SELECT * FROM TimeSpent WHERE timestamp <= ?"
+ "Starting Time Spent Report activity."
+ "T@\"APDatabaseManager\",&,N,V_databaseManager"
+ "T@\"APDatabaseManager\",R,N,V_databaseManager"
+ "T@\"APDatabaseManager\",R,V_dbManager"
+ "T@\"APMetricsLegacyInterface\",R,N,V_legacyInterface"
+ "T@\"APTimeSpentLegacyInterface\",&,N,V_timeSpentLegacyInterface"
+ "T@\"APXPCActivity\",&,N,V_timeSpentReportActivity"
+ "T@\"NSDate\",N,R"
+ "T@\"NSString\",&,N,V_contentId"
+ "T@\"NSString\",N,R"
+ "T@\"NSURLSessionDataTask\",&,N,V_activeDataTask"
+ "TB,N,V_isCancelled"
+ "Td,V_timeSpent"
+ "Ti,N,V_duration"
+ "Time Spent Activity Terminated."
+ "Time Spent Metric Request failed for some reason, keep content with identifier %{public}@ in database to retry later."
+ "Time spent metric request failed due to %{public}@."
+ "Time spent metric request succeeded."
+ "TimeSpent"
+ "TimeSpentDailyRequester"
+ "Trying to send time spent metric for promoted content with content id: %@, but couldn't find it or user account changed."
+ "[TimeSpentDatabase] Removing entry for contentId: %{public}@"
+ "[TimeSpentDatabase] Retrieving entry for contentId: %{public}@ and timeStamp: %{public}@"
+ "[TimeSpentDatabase] Storing entry for contentId: %{public}@ and timeStamp: %{public}@"
+ "__ObjC.APTimeSpentEntry"
+ "__ObjC.APTimeSpentStoreDatabase"
+ "_activeDataTask"
+ "_contentId"
+ "_databaseManager"
+ "_dbManager"
+ "_isCancelled"
+ "_legacyInterface"
+ "_timeSpent"
+ "_timeSpentLegacyInterface"
+ "_timeSpentReportActivity"
+ "activeDataTask"
+ "addTimeSpent:"
+ "calculateDuration"
+ "cancel:"
+ "cancelActiveWork:"
+ "com.apple.ap.promotedcontentd.timespent"
+ "com.apple.ap.promotedcontentd.timespentactivity.queue"
+ "contentId"
+ "databaseManager"
+ "dateWithTimeIntervalSinceNow:"
+ "dbManager"
+ "initWithBundleID:idAccount:contentId:contextId:adDataResponseIdentifier:batchId:impressionIdentifierData:timeSpent:databaseManager:"
+ "initWithContentId:timeStamp:"
+ "initWithDatabase:"
+ "initWithDbManager:retryManager:"
+ "initWithLegacyInterface:"
+ "initWithRetryManager:databaseManager:"
+ "initWithTokens:legacyInterface:"
+ "legacyInterface"
+ "makeNetworkRequest:"
+ "makeTimeSpentRequests:activity:"
+ "removeEntriesForContentIds:"
+ "retrieveTimeSpentEntriesOlderThan:"
+ "retrieveTimeSpentTTLConfigValue"
+ "sendDiagnosticReport:context:isUserChanged:"
+ "sendTimeSpentMetric"
+ "sendTimeSpentMetricFor:contentId:contextId:adDataResponseIdentifier:batchId:impressionIdentifierData:timeSpent:completionHandler:"
+ "setActiveDataTask:"
+ "setContentId:"
+ "setDatabaseManager:"
+ "setIsCancelled:"
+ "setTimeSpent:"
+ "setTimeSpentLegacyInterface:"
+ "setTimeSpentReportActivity:"
+ "startWithLegacyInterface:"
+ "storeEntryForContentId:"
+ "storeEntryForContentId:timeStamp:"
+ "timeInterval"
+ "timeSpent"
+ "timeSpentLegacyInterface"
+ "timeSpentMetricTTL"
+ "timeSpentProcessor"
+ "timeSpentReportActivity"
+ "v20@?0B8@\"NSString\"12"
+ "v80@0:8@16@24@32@40@48@56d64@?72"
+ "{?=\"screenScale\"b1\"timeSinceAppResume\"b1\"timeStamp\"b1\"adSpace\"b1\"buttonState\"b1\"clickSource\"b1\"connectionType\"b1\"duration\"b1\"impressionSequence\"b1\"impressionSource\"b1\"messageSequence\"b1\"overclickCount\"b1\"slotPosition\"b1\"slotWasVisuallyEngaged\"b1}"
- "\x0f"
- "2\x12\x11\x14#\x12"
- "Can't construct Array with count < 0"
- "R\xb1"
- "Swift/Array.swift"
- "initWithTokens:"
- "{?=\"screenScale\"b1\"timeSinceAppResume\"b1\"timeStamp\"b1\"adSpace\"b1\"buttonState\"b1\"clickSource\"b1\"connectionType\"b1\"impressionSequence\"b1\"impressionSource\"b1\"messageSequence\"b1\"overclickCount\"b1\"slotPosition\"b1\"slotWasVisuallyEngaged\"b1}"

```
