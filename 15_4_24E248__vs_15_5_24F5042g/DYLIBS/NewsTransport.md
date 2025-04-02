## NewsTransport

> `/System/Library/PrivateFrameworks/NewsTransport.framework/Versions/A/NewsTransport`

```diff

-5676.0.3.0.0
-  __TEXT.__text: 0x25a900
+5680.0.0.0.0
+  __TEXT.__text: 0x258e18
   __TEXT.__auth_stubs: 0x390
-  __TEXT.__objc_methlist: 0x376ac
+  __TEXT.__objc_methlist: 0x3744c
   __TEXT.__const: 0x48
-  __TEXT.__cstring: 0x11d1d
-  __TEXT.__unwind_info: 0x5090
-  __TEXT.__objc_classname: 0x26b8
-  __TEXT.__objc_methname: 0x5588b
-  __TEXT.__objc_methtype: 0xcb73
-  __TEXT.__objc_stubs: 0x90c0
-  __DATA_CONST.__got: 0x960
+  __TEXT.__cstring: 0x11cbd
+  __TEXT.__unwind_info: 0x5018
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
   __AUTH_CONST.__auth_got: 0x1d0
-  __AUTH_CONST.__cfstring: 0x15fe0
-  __AUTH_CONST.__objc_const: 0x4d7a0
-  __AUTH.__objc_data: 0x6270
-  __DATA.__objc_ivar: 0x3ffc
+  __AUTH_CONST.__cfstring: 0x15f40
+  __AUTH_CONST.__objc_const: 0x4d520
+  __AUTH.__objc_data: 0x61d0
+  __DATA.__objc_ivar: 0x3fe8
   __DATA.__data: 0x60
   __DATA_DIRTY.__objc_data: 0x10e0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/Versions/A/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 18917
-  Symbols:   27276
-  CStrings:  17123
+  Functions: 18869
+  Symbols:   27200
+  CStrings:  17079
 
Symbols:
+ +[NTPBSmarterFetchRequest fetchRecordSpecsType]
+ -[NTPBSmarterFetchRequest addFetchRecordSpecs:]
+ -[NTPBSmarterFetchRequest clearFetchRecordSpecs]
+ -[NTPBSmarterFetchRequest fetchRecordSpecsAtIndex:]
+ -[NTPBSmarterFetchRequest fetchRecordSpecsCount]
+ -[NTPBSmarterFetchRequest fetchRecordSpecs]
+ -[NTPBSmarterFetchRequest fetchSource]
+ -[NTPBSmarterFetchRequest fetchStrategy]
+ -[NTPBSmarterFetchRequest fromTimestamp]
+ -[NTPBSmarterFetchRequest hasFetchSource]
+ -[NTPBSmarterFetchRequest hasFetchStrategy]
+ -[NTPBSmarterFetchRequest hasFromTimestamp]
+ -[NTPBSmarterFetchRequest hasToTimestamp]
+ -[NTPBSmarterFetchRequest setFetchRecordSpecs:]
+ -[NTPBSmarterFetchRequest setFetchSource:]
+ -[NTPBSmarterFetchRequest setFetchStrategy:]
+ -[NTPBSmarterFetchRequest setFromTimestamp:]
+ -[NTPBSmarterFetchRequest setHasFromTimestamp:]
+ -[NTPBSmarterFetchRequest setHasToTimestamp:]
+ -[NTPBSmarterFetchRequest setToTimestamp:]
+ -[NTPBSmarterFetchRequest toTimestamp]
+ -[NTPBSmarterFetchResponse hasRecordCount]
+ -[NTPBSmarterFetchResponse hasToTimestamp]
+ -[NTPBSmarterFetchResponse recordCount]
+ -[NTPBSmarterFetchResponse setHasRecordCount:]
+ -[NTPBSmarterFetchResponse setHasToTimestamp:]
+ -[NTPBSmarterFetchResponse setRecordCount:]
+ -[NTPBSmarterFetchResponse setToTimestamp:]
+ -[NTPBSmarterFetchResponse toTimestamp]
+ OBJC_IVAR_$_NTPBSmarterFetchRequest._fetchRecordSpecs
+ OBJC_IVAR_$_NTPBSmarterFetchRequest._fetchSource
+ OBJC_IVAR_$_NTPBSmarterFetchRequest._fetchStrategy
+ OBJC_IVAR_$_NTPBSmarterFetchRequest._fromTimestamp
+ OBJC_IVAR_$_NTPBSmarterFetchRequest._has
+ OBJC_IVAR_$_NTPBSmarterFetchRequest._toTimestamp
+ OBJC_IVAR_$_NTPBSmarterFetchResponse._has
+ OBJC_IVAR_$_NTPBSmarterFetchResponse._recordCount
+ OBJC_IVAR_$_NTPBSmarterFetchResponse._toTimestamp
- +[NTPBSmarterFetchRequest todayFeedPoolRequestsType]
- +[NTPBSmarterFetchResponse todayFeedPoolResponseType]
- +[NTPBTodayFeedPoolRequest fetchRecordSpecsType]
- +[NTPBTodayFeedPoolResponse recordsType]
- -[NTPBSmarterFetchRequest addTodayFeedPoolRequests:]
- -[NTPBSmarterFetchRequest clearTodayFeedPoolRequests]
- -[NTPBSmarterFetchRequest setTodayFeedPoolRequests:]
- -[NTPBSmarterFetchRequest todayFeedPoolRequestsAtIndex:]
- -[NTPBSmarterFetchRequest todayFeedPoolRequestsCount]
- -[NTPBSmarterFetchRequest todayFeedPoolRequests]
- -[NTPBSmarterFetchResponse .cxx_destruct]
- -[NTPBSmarterFetchResponse addTodayFeedPoolResponse:]
- -[NTPBSmarterFetchResponse clearTodayFeedPoolResponses]
- -[NTPBSmarterFetchResponse setTodayFeedPoolResponses:]
- -[NTPBSmarterFetchResponse todayFeedPoolResponseAtIndex:]
- -[NTPBSmarterFetchResponse todayFeedPoolResponsesCount]
- -[NTPBSmarterFetchResponse todayFeedPoolResponses]
- -[NTPBTodayFeedPoolRequest .cxx_destruct]
- -[NTPBTodayFeedPoolRequest addFetchRecordSpecs:]
- -[NTPBTodayFeedPoolRequest clearFetchRecordSpecs]
- -[NTPBTodayFeedPoolRequest copyWithZone:]
- -[NTPBTodayFeedPoolRequest description]
- -[NTPBTodayFeedPoolRequest dictionaryRepresentation]
- -[NTPBTodayFeedPoolRequest fetchRecordSpecsAtIndex:]
- -[NTPBTodayFeedPoolRequest fetchRecordSpecsCount]
- -[NTPBTodayFeedPoolRequest fetchRecordSpecs]
- -[NTPBTodayFeedPoolRequest fetchSource]
- -[NTPBTodayFeedPoolRequest fetchStrategy]
- -[NTPBTodayFeedPoolRequest fromTimestamp]
- -[NTPBTodayFeedPoolRequest hasFetchSource]
- -[NTPBTodayFeedPoolRequest hasFetchStrategy]
- -[NTPBTodayFeedPoolRequest hasFromTimestamp]
- -[NTPBTodayFeedPoolRequest hasPreviousFromTimestamp]
- -[NTPBTodayFeedPoolRequest hasRequestId]
- -[NTPBTodayFeedPoolRequest hash]
- -[NTPBTodayFeedPoolRequest isEqual:]
- -[NTPBTodayFeedPoolRequest mergeFrom:]
- -[NTPBTodayFeedPoolRequest previousFromTimestamp]
- -[NTPBTodayFeedPoolRequest readFrom:]
- -[NTPBTodayFeedPoolRequest requestId]
- -[NTPBTodayFeedPoolRequest setFetchRecordSpecs:]
- -[NTPBTodayFeedPoolRequest setFetchSource:]
- -[NTPBTodayFeedPoolRequest setFetchStrategy:]
- -[NTPBTodayFeedPoolRequest setFromTimestamp:]
- -[NTPBTodayFeedPoolRequest setHasFromTimestamp:]
- -[NTPBTodayFeedPoolRequest setHasPreviousFromTimestamp:]
- -[NTPBTodayFeedPoolRequest setPreviousFromTimestamp:]
- -[NTPBTodayFeedPoolRequest setRequestId:]
- -[NTPBTodayFeedPoolRequest writeTo:]
- -[NTPBTodayFeedPoolResponse .cxx_destruct]
- -[NTPBTodayFeedPoolResponse addRecords:]
- -[NTPBTodayFeedPoolResponse clearRecords]
- -[NTPBTodayFeedPoolResponse copyWithZone:]
- -[NTPBTodayFeedPoolResponse description]
- -[NTPBTodayFeedPoolResponse dictionaryRepresentation]
- -[NTPBTodayFeedPoolResponse hasNextFromTimestamp]
- -[NTPBTodayFeedPoolResponse hasRequestId]
- -[NTPBTodayFeedPoolResponse hasTtlSecs]
- -[NTPBTodayFeedPoolResponse hash]
- -[NTPBTodayFeedPoolResponse isEqual:]
- -[NTPBTodayFeedPoolResponse mergeFrom:]
- -[NTPBTodayFeedPoolResponse nextFromTimestamp]
- -[NTPBTodayFeedPoolResponse readFrom:]
- -[NTPBTodayFeedPoolResponse recordsAtIndex:]
- -[NTPBTodayFeedPoolResponse recordsCount]
- -[NTPBTodayFeedPoolResponse records]
- -[NTPBTodayFeedPoolResponse requestId]
- -[NTPBTodayFeedPoolResponse setHasNextFromTimestamp:]
- -[NTPBTodayFeedPoolResponse setHasTtlSecs:]
- -[NTPBTodayFeedPoolResponse setNextFromTimestamp:]
- -[NTPBTodayFeedPoolResponse setRecords:]
- -[NTPBTodayFeedPoolResponse setRequestId:]
- -[NTPBTodayFeedPoolResponse setTtlSecs:]
- -[NTPBTodayFeedPoolResponse ttlSecs]
- -[NTPBTodayFeedPoolResponse writeTo:]
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
- __OBJC_$_CLASS_METHODS_NTPBSmarterFetchResponse
- __OBJC_$_CLASS_METHODS_NTPBTodayFeedPoolRequest
- __OBJC_$_CLASS_METHODS_NTPBTodayFeedPoolResponse
- __OBJC_$_INSTANCE_METHODS_NTPBTodayFeedPoolRequest
- __OBJC_$_INSTANCE_METHODS_NTPBTodayFeedPoolResponse
- __OBJC_$_INSTANCE_VARIABLES_NTPBTodayFeedPoolRequest
- __OBJC_$_INSTANCE_VARIABLES_NTPBTodayFeedPoolResponse
- __OBJC_$_PROP_LIST_NTPBTodayFeedPoolRequest
- __OBJC_$_PROP_LIST_NTPBTodayFeedPoolResponse
- __OBJC_CLASS_PROTOCOLS_$_NTPBTodayFeedPoolRequest
- __OBJC_CLASS_PROTOCOLS_$_NTPBTodayFeedPoolResponse
- __OBJC_CLASS_RO_$_NTPBTodayFeedPoolRequest
- __OBJC_CLASS_RO_$_NTPBTodayFeedPoolResponse
- __OBJC_METACLASS_RO_$_NTPBTodayFeedPoolRequest
- __OBJC_METACLASS_RO_$_NTPBTodayFeedPoolResponse
- _objc_msgSend$addRecords:
- _objc_msgSend$addTodayFeedPoolRequests:
- _objc_msgSend$addTodayFeedPoolResponse:
- _objc_msgSend$setRequestId:
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
