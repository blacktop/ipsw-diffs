## NewsTransport

> `/System/Library/PrivateFrameworks/NewsTransport.framework/NewsTransport`

```diff

-5676.2.0.0.0
-  __TEXT.__text: 0x24fe60
+5680.0.0.0.0
+  __TEXT.__text: 0x24e46c
   __TEXT.__auth_stubs: 0x460
-  __TEXT.__objc_methlist: 0x376ac
+  __TEXT.__objc_methlist: 0x3744c
   __TEXT.__const: 0x48
-  __TEXT.__cstring: 0x11d1d
-  __TEXT.__unwind_info: 0x4f58
-  __TEXT.__objc_classname: 0x26b8
-  __TEXT.__objc_methname: 0x5588b
-  __TEXT.__objc_methtype: 0xcb73
-  __TEXT.__objc_stubs: 0x90c0
-  __DATA_CONST.__got: 0x960
+  __TEXT.__cstring: 0x11cbd
+  __TEXT.__unwind_info: 0x4ea0
+  __TEXT.__objc_classname: 0x2687
+  __TEXT.__objc_methname: 0x55516
+  __TEXT.__objc_methtype: 0xcb67
+  __TEXT.__objc_stubs: 0x9040
+  __DATA_CONST.__got: 0x950
   __DATA_CONST.__const: 0x72c8
-  __DATA_CONST.__objc_classlist: 0xb88
+  __DATA_CONST.__objc_classlist: 0xb78
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11520
-  __DATA_CONST.__objc_superrefs: 0xb88
+  __DATA_CONST.__objc_selrefs: 0x11440
+  __DATA_CONST.__objc_superrefs: 0xb78
   __AUTH_CONST.__auth_got: 0x238
-  __AUTH_CONST.__cfstring: 0x15fe0
-  __AUTH_CONST.__objc_const: 0x4d7a0
-  __AUTH.__objc_data: 0xa00
-  __DATA.__objc_ivar: 0x3ffc
+  __AUTH_CONST.__cfstring: 0x15f40
+  __AUTH_CONST.__objc_const: 0x4d520
+  __AUTH.__objc_data: 0x960
+  __DATA.__objc_ivar: 0x3fe8
   __DATA.__data: 0x60
   __DATA_DIRTY.__objc_data: 0x6950
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 18917
-  Symbols:   23774
-  CStrings:  17123
+  Functions: 18869
+  Symbols:   23717
+  CStrings:  17079
 
Symbols:
+ OBJC_IVAR_$_NTPBSmarterFetchRequest._fetchRecordSpecs
+ OBJC_IVAR_$_NTPBSmarterFetchRequest._fetchSource
+ OBJC_IVAR_$_NTPBSmarterFetchRequest._fetchStrategy
+ OBJC_IVAR_$_NTPBSmarterFetchRequest._fromTimestamp
+ OBJC_IVAR_$_NTPBSmarterFetchRequest._has
+ OBJC_IVAR_$_NTPBSmarterFetchRequest._toTimestamp
+ OBJC_IVAR_$_NTPBSmarterFetchResponse._has
+ OBJC_IVAR_$_NTPBSmarterFetchResponse._recordCount
+ OBJC_IVAR_$_NTPBSmarterFetchResponse._toTimestamp
- OBJC_IVAR_$_NTPBSmarterFetchRequest._todayFeedPoolRequests
- OBJC_IVAR_$_NTPBSmarterFetchResponse._todayFeedPoolResponses
- OBJC_IVAR_$_NTPBTodayFeedPoolRequest._fetchRecordSpecs
- OBJC_IVAR_$_NTPBTodayFeedPoolRequest._fetchSource
- OBJC_IVAR_$_NTPBTodayFeedPoolRequest._fetchStrategy
- OBJC_IVAR_$_NTPBTodayFeedPoolRequest._fromTimestamp
- OBJC_IVAR_$_NTPBTodayFeedPoolRequest._has
- OBJC_IVAR_$_NTPBTodayFeedPoolRequest._previousFromTimestamp
- OBJC_IVAR_$_NTPBTodayFeedPoolRequest._requestId
- OBJC_IVAR_$_NTPBTodayFeedPoolResponse._has
- OBJC_IVAR_$_NTPBTodayFeedPoolResponse._nextFromTimestamp
- OBJC_IVAR_$_NTPBTodayFeedPoolResponse._records
- OBJC_IVAR_$_NTPBTodayFeedPoolResponse._requestId
- OBJC_IVAR_$_NTPBTodayFeedPoolResponse._ttlSecs
- _NTPBTodayFeedPoolRequestReadFrom
- _NTPBTodayFeedPoolResponseReadFrom
- _OBJC_CLASS_$_NTPBTodayFeedPoolRequest
- _OBJC_CLASS_$_NTPBTodayFeedPoolResponse
- _OBJC_METACLASS_$_NTPBTodayFeedPoolRequest
- _OBJC_METACLASS_$_NTPBTodayFeedPoolResponse
CStrings:
+ "&"
+ "Ti,N,V_recordCount"
+ "Tq,N,V_toTimestamp"
+ "_recordCount"
+ "_toTimestamp"
+ "hasRecordCount"
+ "hasToTimestamp"
+ "recordCount"
+ "record_count"
+ "setHasRecordCount:"
+ "setHasToTimestamp:"
+ "setRecordCount:"
+ "setToTimestamp:"
+ "toTimestamp"
+ "to_timestamp"
+ "{?=\"fromTimestamp\"b1\"toTimestamp\"b1}"
+ "{?=\"toTimestamp\"b1\"recordCount\"b1}"
- "NTPBTodayFeedPoolRequest"
- "NTPBTodayFeedPoolResponse"
- "T@\"NSMutableArray\",&,N,V_records"
- "T@\"NSMutableArray\",&,N,V_todayFeedPoolRequests"
- "T@\"NSMutableArray\",&,N,V_todayFeedPoolResponses"
- "T@\"NSString\",&,N,V_requestId"
- "Ti,N,V_ttlSecs"
- "Tq,N,V_nextFromTimestamp"
- "Tq,N,V_previousFromTimestamp"
- "_nextFromTimestamp"
- "_previousFromTimestamp"
- "_records"
- "_requestId"
- "_todayFeedPoolRequests"
- "_todayFeedPoolResponses"
- "_ttlSecs"
- "addRecords:"
- "addTodayFeedPoolRequests:"
- "addTodayFeedPoolResponse:"
- "clearRecords"
- "clearTodayFeedPoolRequests"
- "clearTodayFeedPoolResponses"
- "hasNextFromTimestamp"
- "hasPreviousFromTimestamp"
- "hasRequestId"
- "hasTtlSecs"
- "nextFromTimestamp"
- "next_from_timestamp"
- "previousFromTimestamp"
- "previous_from_timestamp"
- "records"
- "recordsAtIndex:"
- "recordsCount"
- "recordsType"
- "requestId"
- "request_id"
- "setHasNextFromTimestamp:"
- "setHasPreviousFromTimestamp:"
- "setHasTtlSecs:"
- "setNextFromTimestamp:"
- "setPreviousFromTimestamp:"
- "setRecords:"
- "setRequestId:"
- "setTodayFeedPoolRequests:"
- "setTodayFeedPoolResponses:"
- "setTtlSecs:"
- "todayFeedPoolRequests"
- "todayFeedPoolRequestsAtIndex:"
- "todayFeedPoolRequestsCount"
- "todayFeedPoolRequestsType"
- "todayFeedPoolResponseAtIndex:"
- "todayFeedPoolResponseType"
- "todayFeedPoolResponses"
- "todayFeedPoolResponsesCount"
- "today_feed_pool_requests"
- "today_feed_pool_response"
- "ttlSecs"
- "ttl_secs"
- "{?=\"fromTimestamp\"b1\"previousFromTimestamp\"b1}"
- "{?=\"nextFromTimestamp\"b1\"ttlSecs\"b1}"

```
