## identityservicesd

> `/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd`

```diff

-1814.500.141.0.0
-  __TEXT.__text: 0x5fecb8
+1814.600.72.0.0
+  __TEXT.__text: 0x5fff10
   __TEXT.__auth_stubs: 0x4940
-  __TEXT.__objc_stubs: 0x40160
-  __TEXT.__objc_methlist: 0x20a5c
+  __TEXT.__objc_stubs: 0x40260
+  __TEXT.__objc_methlist: 0x20b54
   __TEXT.__const: 0x3f860
-  __TEXT.__gcc_except_tab: 0x1b398
-  __TEXT.__objc_methname: 0x68b07
-  __TEXT.__cstring: 0x52369
-  __TEXT.__oslogstring: 0x7170d
-  __TEXT.__objc_classname: 0x3c62
+  __TEXT.__gcc_except_tab: 0x1b408
+  __TEXT.__objc_methname: 0x68c6d
+  __TEXT.__cstring: 0x52539
+  __TEXT.__oslogstring: 0x719f6
+  __TEXT.__objc_classname: 0x3c87
   __TEXT.__objc_methtype: 0xfddd
   __TEXT.__ustring: 0x52a
   __TEXT.__dlopen_cstrs: 0xa1

   __TEXT.__swift5_proto: 0x10c
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0xd81c
+  __TEXT.__unwind_info: 0xd8c8
   __TEXT.__eh_frame: 0x1ad0
   __DATA_CONST.__auth_got: 0x24b0
-  __DATA_CONST.__got: 0x20f0
+  __DATA_CONST.__got: 0x2110
   __DATA_CONST.__auth_ptr: 0xd8
-  __DATA_CONST.__const: 0x199e8
-  __DATA_CONST.__cfstring: 0x31c20
-  __DATA_CONST.__objc_classlist: 0xd10
+  __DATA_CONST.__const: 0x19a08
+  __DATA_CONST.__cfstring: 0x31d20
+  __DATA_CONST.__objc_classlist: 0xd18
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x5f8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xa8
-  __DATA_CONST.__objc_classrefs: 0x17d0
-  __DATA_CONST.__objc_superrefs: 0xaa0
-  __DATA_CONST.__objc_intobj: 0x17d0
+  __DATA_CONST.__objc_classrefs: 0x17e8
+  __DATA_CONST.__objc_superrefs: 0xaa8
+  __DATA_CONST.__objc_intobj: 0x17e8
   __DATA_CONST.__objc_arraydata: 0x548
   __DATA_CONST.__objc_arrayobj: 0x330
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x40d80
-  __DATA.__objc_selrefs: 0x12ff8
-  __DATA.__objc_ivar: 0x2e4c
-  __DATA.__objc_data: 0x9ac8
+  __DATA.__objc_const: 0x40ec0
+  __DATA.__objc_selrefs: 0x13038
+  __DATA.__objc_ivar: 0x2e5c
+  __DATA.__objc_data: 0x9b18
   __DATA.__data: 0x6f68
   __DATA.__bss: 0x42b0
   __DATA.__common: 0x384

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 17154
-  Symbols:   2487
-  CStrings:  31634
+  Functions: 17177
+  Symbols:   2493
+  CStrings:  31665
 
Symbols:
+ _IDSDailyAccountAddedNotificationMetricDuplicateKey
+ _IDSDailyAccountAddedNotificationMetricTotalKey
+ _IDSGlobalLinkOptionCallTypeKey
+ _OBJC_CLASS_$_IDSDailyAccountAddedNotificationsMetric
+ _OBJC_CLASS_$_IDSHandleListUpdatedMetric
+ _kIDSGeneralReportingTypeKey
CStrings:
+ "\x14\x11\x12!\x11\x12!!!\xf0\xf3\x11\x11\x11\x118\x14C,"
+ "23:09:13"
+ "?8A"
+ "?;A"
+ "Apr 18 2024"
+ "General unkonwn sender response: %@"
+ "IDSReportGeneralUnknownSenderMessage"
+ "Invalid reporting type provided, we shouldn't be here... { reportingType: %lu }"
+ "No sim present in slot, not reporting anything. { simSlot: %lu }"
+ "Posting new device notification. Number of notifications posted today: %@"
+ "Reporting daily PNR status and daily account added notifications."
+ "Sending report unknown sender"
+ "Sent report unknown sender message (responseMessage: %@) (error: %@) (resultCode: %d) (resultDictionary: %@)"
+ "Server has disabled unknown sender reporting."
+ "T@\"NSDictionary\",C,V_unknownSenderInfo"
+ "We processed last message from storage from the server for topic %@"
+ "We received a last from storage from the server for topic %@, not terminating storage state machine until messages finish processing. Cancelling timeout."
+ "_IDSSessionClientID failed to get pid from %@"
+ "_IDSSessionClientID unknown class type for %@"
+ "_callType"
+ "_dailyMetricsData"
+ "_unknownSenderInfo"
+ "com.apple.identityservices.dailyDeviceAddedNotificationData"
+ "ft-should-report-unknown-sender"
+ "initWithNotificationsPostedToday:duplicateNotificationPostedToday:"
+ "initWithService:"
+ "joinWithOptions for %@: URI: %@, participantData: %@, participantInfo: %@, handshakeBlob: %@, callType: %@"
+ "kt-clear-cache-opt-in-enabled"
+ "ktShouldClearCacheOnOptInOut"
+ "processedLastMessageFromStorageForTopic:"
+ "reportDailyNotificationMetrics"
+ "reportMessage:toURI:"
+ "reportMessage:toURI:registration:"
+ "reportUnknownSenderMessage:selfURI:registration:"
+ "setUnknownSenderInfo:"
+ "unknown-sender-info"
+ "unknownSenderInfo"
- "\x14\x11\x12!\x11\x12!!!\xf0\xf3\x11\x11\x11\x117\x14C,"
- "00:27:50"
- "?9A"
- "?<A"
- "Mar  9 2024"
- "Reporting daily PNR status."
- "We received a last from storage from the server for topic %@"
- "joinWithOptions for %@: URI: %@, participantData: %@, participantInfo: %@, handshakeBlob: %@"
- "reportSpamMessage:toURI:"
- "reportSpamMessage:toURI:registration:"

```
