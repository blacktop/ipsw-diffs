## CalendarDaemon

> `/System/Library/PrivateFrameworks/CalendarDaemon.framework/CalendarDaemon`

```diff

-1224.2.3.0.0
-  __TEXT.__text: 0x72664
+1224.3.1.0.0
+  __TEXT.__text: 0x73290
   __TEXT.__auth_stubs: 0x3830
-  __TEXT.__objc_methlist: 0x625c
+  __TEXT.__objc_methlist: 0x62ac
   __TEXT.__cstring: 0x70f4
   __TEXT.__const: 0x150
-  __TEXT.__oslogstring: 0x8360
-  __TEXT.__gcc_except_tab: 0x1c50
+  __TEXT.__oslogstring: 0x845a
+  __TEXT.__gcc_except_tab: 0x1c7c
   __TEXT.__dlopen_cstrs: 0xc0
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x1b38
-  __TEXT.__objc_classname: 0x149c
-  __TEXT.__objc_methname: 0xecbc
-  __TEXT.__objc_methtype: 0x67d6
-  __TEXT.__objc_stubs: 0x9d00
+  __TEXT.__unwind_info: 0x1b68
+  __TEXT.__objc_classname: 0x14b1
+  __TEXT.__objc_methname: 0xed47
+  __TEXT.__objc_methtype: 0x6972
+  __TEXT.__objc_stubs: 0x9d60
   __DATA_CONST.__got: 0x9f0
-  __DATA_CONST.__const: 0x2058
-  __DATA_CONST.__objc_classlist: 0x3f8
+  __DATA_CONST.__const: 0x2080
+  __DATA_CONST.__objc_classlist: 0x400
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x1c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3198
+  __DATA_CONST.__objc_selrefs: 0x31b0
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x2a8
+  __DATA_CONST.__objc_superrefs: 0x2b0
   __DATA_CONST.__objc_arraydata: 0x350
   __AUTH_CONST.__auth_got: 0x1c28
   __AUTH_CONST.__const: 0x880
   __AUTH_CONST.__cfstring: 0x7ac0
-  __AUTH_CONST.__objc_const: 0xc278
+  __AUTH_CONST.__objc_const: 0xc478
   __AUTH_CONST.__objc_intobj: 0x468
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x1400
+  __AUTH.__objc_data: 0x1450
   __AUTH.__data: 0xa50
-  __DATA.__objc_ivar: 0x7a8
+  __DATA.__objc_ivar: 0x7c8
   __DATA.__data: 0x1728
   __DATA.__bss: 0x198
   __DATA.__common: 0x8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: C981CF2E-6224-37CF-8052-67FE424EC240
-  Functions: 2174
-  Symbols:   9025
-  CStrings:  5599
+  UUID: 23D13490-7D09-3ED9-AB47-32786372767B
+  Functions: 2181
+  Symbols:   9060
+  CStrings:  5617
 
Symbols:
+ +[CADFetchCalendarItemsWithPredicateOperation queryDatabase:withID:batchSize:batchToken:predicate:connection:serializer:cancellationToken:completed:]
+ -[CADBatchedFetchAgent .cxx_destruct]
+ -[CADBatchedFetchAgent fetchBatch:complete:]
+ -[CADBatchedFetchAgent initWithPredicate:connection:token:]
+ -[CADBatchedFetchAgent loadDatabaseIDs]
+ -[CADBatchedFetchAgent token]
+ -[CADFetchedObjectSerializer count]
+ -[CADPredicate copyNextBatchFromDatabase:batchSize:complete:]
+ -[CADPropertySearchPredicate copyNextBatchFromDatabase:batchSize:complete:]
+ -[CADXPCImplementation(CADCalendarItemOperationGroup) CADDatabaseFetchEventsWithPredicate:fetchIdentifier:batchSize:reply:]
+ _OBJC_CLASS_$_CADBatchedFetchAgent
+ _OBJC_IVAR_$_CADBatchedFetchAgent._conn
+ _OBJC_IVAR_$_CADBatchedFetchAgent._databaseIDs
+ _OBJC_IVAR_$_CADBatchedFetchAgent._databaseIndex
+ _OBJC_IVAR_$_CADBatchedFetchAgent._predicate
+ _OBJC_IVAR_$_CADBatchedFetchAgent._token
+ _OBJC_IVAR_$_CADPropertySearchPredicate._batchOffset
+ _OBJC_IVAR_$_CADPropertySearchPredicate._databaseID
+ _OBJC_IVAR_$_CADPropertySearchPredicate._types
+ _OBJC_IVAR_$_CADPropertySearchPredicate._values
+ _OBJC_IVAR_$_CADPropertySearchPredicate._whereClause
+ _OBJC_METACLASS_$_CADBatchedFetchAgent
+ __OBJC_$_INSTANCE_METHODS_CADBatchedFetchAgent
+ __OBJC_$_INSTANCE_VARIABLES_CADBatchedFetchAgent
+ __OBJC_$_PROP_LIST_CADBatchedFetchAgent
+ __OBJC_CLASS_PROTOCOLS_$_CADBatchedFetchAgent
+ __OBJC_CLASS_RO_$_CADBatchedFetchAgent
+ __OBJC_METACLASS_RO_$_CADBatchedFetchAgent
+ ___39-[CADBatchedFetchAgent loadDatabaseIDs]_block_invoke
+ ___44-[CADBatchedFetchAgent fetchBatch:complete:]_block_invoke
+ ___block_descriptor_68_e8_32s40s48r56r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12lr48l8r56l8s32l8s40l8
+ ___block_literal_global.372
+ _objc_msgSend$copyNextBatchFromDatabase:batchSize:complete:
+ _objc_msgSend$fetchBatch:complete:
+ _objc_msgSend$initWithPredicate:connection:token:
+ _objc_msgSend$loadDatabaseIDs
+ _objc_msgSend$queryDatabase:withID:batchSize:batchToken:predicate:connection:serializer:cancellationToken:completed:
- +[CADFetchCalendarItemsWithPredicateOperation queryDatabase:withID:predicate:connection:serializer:cancellationToken:]
- -[CADPropertySearchPredicate initWithEntityType:filters:calendars:limit:randomize:]
- -[CADPropertySearchPredicate initWithEntityType:filters:calendars:source:limit:randomize:]
- -[CADPropertySearchPredicate limit]
- -[CADPropertySearchPredicate randomize]
- _OBJC_IVAR_$_CADPropertySearchPredicate._limit
- _OBJC_IVAR_$_CADPropertySearchPredicate._randomize
- ___block_literal_global.368
- _objc_msgSend$initWithEntityType:filters:calendars:source:limit:randomize:
- _objc_msgSend$queryDatabase:withID:predicate:connection:serializer:cancellationToken:
CStrings:
+ "@28@0:8i16^B20"
+ "@36@0:8@16@24I32"
+ "@36@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16i24^B28"
+ "@52@0:8@16Q24Q32I40@44"
+ "Agent already exists %u"
+ "CADBatchedFetchAgent"
+ "CADDatabaseFetchEventsWithPredicate:fetchIdentifier:batchSize:reply:"
+ "FetchBatch"
+ "Invalid batch token"
+ "Requested continuation of non-existant batched predicate search %u"
+ "Switched database IDs (%i to %i) while at batch offset %lli"
+ "_batchOffset"
+ "_databaseIDs"
+ "_databaseIndex"
+ "_types"
+ "_values"
+ "_whereClause"
+ "class=%@, dbid=%i, agent=%i"
+ "copyNextBatchFromDatabase:batchSize:complete:"
+ "fetchBatch:complete:"
+ "initWithPredicate:connection:token:"
+ "loadDatabaseIDs"
+ "queryDatabase:withID:batchSize:batchToken:predicate:connection:serializer:cancellationToken:completed:"
+ "results.count = %lu complete = %{BOOL}i"
+ "v40@0:8@\"NSPredicate\"16I24i28@?<v@?i@\"NSArray\"B>32"
+ "v40@0:8@16I24i28@?32"
+ "v52@0:8@\"NSPredicate\"16Q24Q32I40@?<v@?i>44"
+ "v52@0:8@16Q24Q32I40@?44"
+ "v76@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16i24i28i32@36@44@52@60^B68"
- "@48@0:8i16@20@28q36B44"
- "@52@0:8@16Q24Q32i40@44"
- "@56@0:8i16@20@28@36q44B52"
- "TB,R,N,V_randomize"
- "Tq,R,N,V_limit"
- "initWithEntityType:filters:calendars:limit:randomize:"
- "initWithEntityType:filters:calendars:source:limit:randomize:"
- "queryDatabase:withID:predicate:connection:serializer:cancellationToken:"
- "v52@0:8@\"NSPredicate\"16Q24Q32i40@?<v@?i>44"
- "v52@0:8@16Q24Q32i40@?44"
- "v60@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16i24@28@36@44@52"

```
