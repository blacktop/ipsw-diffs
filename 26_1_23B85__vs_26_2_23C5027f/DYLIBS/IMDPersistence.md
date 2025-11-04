## IMDPersistence

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence`

```diff

-1450.200.89.2.31
-  __TEXT.__text: 0x226218
+1450.300.16.2.4
+  __TEXT.__text: 0x226b78
   __TEXT.__auth_stubs: 0x4560
-  __TEXT.__objc_methlist: 0x71fc
+  __TEXT.__objc_methlist: 0x7264
   __TEXT.__const: 0xad28
-  __TEXT.__cstring: 0x47e8b
-  __TEXT.__oslogstring: 0x1d886
-  __TEXT.__gcc_except_tab: 0xd0d0
+  __TEXT.__cstring: 0x480bb
+  __TEXT.__oslogstring: 0x1d8d6
+  __TEXT.__gcc_except_tab: 0xd0d4
   __TEXT.__ustring: 0x434
   __TEXT.__dlopen_cstrs: 0x360
   __TEXT.__constg_swiftt: 0x4cf8
-  __TEXT.__swift5_typeref: 0x3282
+  __TEXT.__swift5_typeref: 0x32e6
   __TEXT.__swift5_builtin: 0x244
-  __TEXT.__swift5_reflstr: 0x2ad1
-  __TEXT.__swift5_fieldmd: 0x2d60
+  __TEXT.__swift5_reflstr: 0x2ae1
+  __TEXT.__swift5_fieldmd: 0x2d6c
   __TEXT.__swift5_assocty: 0x530
   __TEXT.__swift5_proto: 0x664
   __TEXT.__swift5_types: 0x320

   __TEXT.__swift_as_entry: 0x60
   __TEXT.__swift_as_ret: 0x58
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x8820
+  __TEXT.__unwind_info: 0x8850
   __TEXT.__eh_frame: 0x6df0
-  __TEXT.__objc_classname: 0x11c3
-  __TEXT.__objc_methname: 0x17a35
-  __TEXT.__objc_methtype: 0x37aa
-  __TEXT.__objc_stubs: 0x11b40
-  __DATA_CONST.__got: 0x1708
-  __DATA_CONST.__const: 0x8390
+  __TEXT.__objc_classname: 0x11ce
+  __TEXT.__objc_methname: 0x17b25
+  __TEXT.__objc_methtype: 0x377d
+  __TEXT.__objc_stubs: 0x11c60
+  __DATA_CONST.__got: 0x1718
+  __DATA_CONST.__const: 0x8448
   __DATA_CONST.__objc_classlist: 0x600
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x228
+  __DATA_CONST.__objc_protolist: 0x230
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5260
+  __DATA_CONST.__objc_selrefs: 0x5298
   __DATA_CONST.__objc_protorefs: 0xe8
   __DATA_CONST.__objc_superrefs: 0x1d8
-  __DATA_CONST.__objc_arraydata: 0x220
+  __DATA_CONST.__objc_arraydata: 0x2f0
   __AUTH_CONST.__auth_got: 0x22c0
-  __AUTH_CONST.__const: 0x9920
-  __AUTH_CONST.__cfstring: 0x11f40
-  __AUTH_CONST.__objc_const: 0xf420
+  __AUTH_CONST.__const: 0x9a50
+  __AUTH_CONST.__cfstring: 0x12200
+  __AUTH_CONST.__objc_const: 0xf458
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH_CONST.__objc_dictobj: 0x28
+  __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x1c30
   __AUTH.__data: 0x3ed0
   __DATA.__objc_ivar: 0x488
-  __DATA.__data: 0x2da8
+  __DATA.__data: 0x2e08
   __DATA.__bss: 0x9fe0
   __DATA.__common: 0x168
   __DATA_DIRTY.__objc_data: 0x1620

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1079CD55-A617-3129-8F8B-B52B6C1FC48A
-  Functions: 10556
-  Symbols:   2569
-  CStrings:  12282
+  UUID: CAC2D103-3EED-32A2-8476-68B0C6044534
+  Functions: 10569
+  Symbols:   2571
+  CStrings:  12336
 
Symbols:
+ _IMDDScanAttributedStringWithTranslationsFromSummaryInfo
+ _IMMessagePropertyAssociatedMessageGUID
+ _IMMessagePropertyThreadOriginatorGUID
- _IMDDScanAttributedStringWithExtendedContext
CStrings:
+ " AND message_date <= ?"
+ "%s%s set to %ld (max(%ld, %ld) due to overflow)"
+ "%s%s set to %ld (max(%ld, %ld))"
+ "1. QueryHighestMessageDate"
+ "BGSTLane"
+ "ForceDeferral"
+ "FullReindex"
+ "FullReindexChatCount"
+ "FullReindexMessageCount"
+ "FullReindexOldestMessageGUID"
+ "IMDIndexingThrottleHistory"
+ "IMDebugCoding"
+ "IgnoreRejections"
+ "IgnoreThrottle"
+ "LIKE"
+ "LaneOverride"
+ "NeedsPriorityCheck"
+ "Preflight"
+ "Reason"
+ "SELECT\n    flag, flag_group, lane, reason, COUNT(*) AS count\nFROM persistent_tasks\nWHERE retry_count < 5\nGROUP BY flag, flag_group, lane, reason"
+ "SELECT 1\nFROM persistent_tasks\nWHERE flag =  ?  AND flag_group =  ?  AND lane =  ?  AND reason =  ?  AND retry_count < 5\nLIMIT 1"
+ "T@\"NSMutableDictionary\",R,N,V_historicalThrottles"
+ "_IMDMessageRecordCopyAndMarkAsReadMessagesReceivedPriorToDateMatchingChatGUIDs"
+ "_beginThrottlingForIdentifier:error:untilDate:"
+ "_cleanupHistoricalThrottles"
+ "_cleanupThrottles"
+ "_historicalThrottles"
+ "_recordHistoricalThrottleForIdentifier:error:untilDate:"
+ "_shouldGenerateVisibleRootItem"
+ "beginThrottlingForIdentifier:error:untilDate:"
+ "chat(is_filtered)"
+ "chat_idx_is_filtered"
+ "chat_message_join(message_date)"
+ "chat_message_join_idx_message_date_only"
+ "debugEncodeWithCoder:"
+ "debuggingDictionaryFromDictionaryRepresentation:"
+ "expiresAt"
+ "historicalThrottles"
+ "persistent_tasks(flag, flag_group, lane, reason, retry_count) WHERE retry_count < 5"
+ "q24@?0@\"NSDictionary\"8@\"NSDictionary\"16"
+ "removeObjectsInRange:"
+ "setHistoricalThrottles:"
+ "startedAt"
+ "v32@?0@\"NSString\"8@\"NSMutableArray\"16^B24"
- " AND rowid <= ?"
- "1. QueryHighestRowID"
- "@\"IMDContactStoreChangeHistoryEventsHandler\""
- "SELECT\n    flag, flag_group, lane, reason, COUNT(*) AS count\nFROM persistent_tasks\nGROUP BY flag, flag_group, lane, reason"
- "SELECT 1\nFROM persistent_tasks\nWHERE flag =  ?  AND flag_group =  ?  AND lane =  ?  AND reason =  ? \nLIMIT 1"
- "T@\"IMDContactStoreChangeHistoryEventsHandler\",&,N,V_contactsEventhandler"
- "_IMDMessageRecordCopyAndMarkAsReadMessagesReceivedPriorToGuidMatchingChatGUIDs"
- "_beginThrottlingForIdentifier:untilDate:"
- "_contactsEventhandler"
- "contactsEventhandler"
- "isMultiPart"
- "persistent_tasks(flag, flag_group, lane, reason)"
- "setContactsEventhandler:"

```
