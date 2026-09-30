## CalendarDaemon

> `/System/Library/PrivateFrameworks/CalendarDaemon.framework/CalendarDaemon`

```diff

-1224.1.4.0.0
-  __TEXT.__text: 0x7165c
-  __TEXT.__auth_stubs: 0x3840
-  __TEXT.__objc_methlist: 0x6184
-  __TEXT.__cstring: 0x6f7d
+1224.1.5.0.0
+  __TEXT.__text: 0x72664
+  __TEXT.__auth_stubs: 0x3830
+  __TEXT.__objc_methlist: 0x625c
+  __TEXT.__cstring: 0x70f4
   __TEXT.__const: 0x150
-  __TEXT.__oslogstring: 0x81fe
-  __TEXT.__gcc_except_tab: 0x1ba4
+  __TEXT.__oslogstring: 0x8360
+  __TEXT.__gcc_except_tab: 0x1c50
   __TEXT.__dlopen_cstrs: 0xc0
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x1ad8
-  __TEXT.__objc_classname: 0x1499
-  __TEXT.__objc_methname: 0xead1
-  __TEXT.__objc_methtype: 0x6639
-  __TEXT.__objc_stubs: 0x9bc0
-  __DATA_CONST.__got: 0x9e8
-  __DATA_CONST.__const: 0x1fe0
+  __TEXT.__unwind_info: 0x1b38
+  __TEXT.__objc_classname: 0x149c
+  __TEXT.__objc_methname: 0xecbc
+  __TEXT.__objc_methtype: 0x67d6
+  __TEXT.__objc_stubs: 0x9d00
+  __DATA_CONST.__got: 0x9f0
+  __DATA_CONST.__const: 0x2058
   __DATA_CONST.__objc_classlist: 0x3f8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x1c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3140
+  __DATA_CONST.__objc_selrefs: 0x3198
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x2a8
   __DATA_CONST.__objc_arraydata: 0x350
-  __AUTH_CONST.__auth_got: 0x1c30
+  __AUTH_CONST.__auth_got: 0x1c28
   __AUTH_CONST.__const: 0x880
-  __AUTH_CONST.__cfstring: 0x79e0
-  __AUTH_CONST.__objc_const: 0xc130
+  __AUTH_CONST.__cfstring: 0x7ac0
+  __AUTH_CONST.__objc_const: 0xc278
   __AUTH_CONST.__objc_intobj: 0x468
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x1400
   __AUTH.__data: 0xa50
-  __DATA.__objc_ivar: 0x790
+  __DATA.__objc_ivar: 0x7a8
   __DATA.__data: 0x1728
   __DATA.__bss: 0x198
   __DATA.__common: 0x8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 188073BC-48E0-3ABA-B58A-32DCB79C8B4B
-  Functions: 2149
-  Symbols:   8949
-  CStrings:  5557
+  UUID: 138FC4D9-2A6A-3928-B479-B088AD9F82A8
+  Functions: 2174
+  Symbols:   9025
+  CStrings:  5599
 
Symbols:
+ -[CADCoreSpotlightIndex beginIndexBatch]
+ -[CADCoreSpotlightIndex endIndexBatchWithExpectedClientState:newClientState:completionHandler:]
+ -[CADCoreSpotlightIndex needsReindex]
+ -[CADEventOccurrenceSet hasInvalidDates]
+ -[CADFullLoggingSpotlightIndex beginIndexBatch]
+ -[CADFullLoggingSpotlightIndex endIndexBatchWithExpectedClientState:newClientState:completionHandler:]
+ -[CADFullLoggingSpotlightIndex needsReindex]
+ -[CADMockSpotlightIndex _batchFailureError]
+ -[CADMockSpotlightIndex beginIndexBatch]
+ -[CADMockSpotlightIndex endIndexBatchWithExpectedClientState:newClientState:completionHandler:]
+ -[CADMockSpotlightIndex needsReindex]
+ -[CADMockSpotlightIndexProvider failureCallback]
+ -[CADMockSpotlightIndexProvider setFailureCallback:]
+ -[CADSpotlightIndexer _deleteAllSearchableItemsAndSetClientStateForBundleID:eventIndex:]
+ -[CADSpotlightIndexer _deleteFromIndex:eventsIndex:]
+ -[CADSpotlightIndexer _expectedClientState]
+ -[CADSpotlightIndexer _upsertToIndex:inDatabase:personaID:deleteBeforeInserting:eventsIndex:]
+ -[CADSpotlightIndexer _upsertToIndex:inDatabase:personaID:deleteBeforeInserting:eventsIndex:].cold.1
+ -[CADSpotlightIndexer _upsertToIndex:inDatabase:personaID:deleteBeforeInserting:eventsIndex:].cold.2
+ _CSIndexErrorDomain
+ _OBJC_IVAR_$_CADCoreSpotlightIndex.needsReindex
+ _OBJC_IVAR_$_CADEventOccurrenceSet._hasInvalidDates
+ _OBJC_IVAR_$_CADMockSpotlightIndex._batchJobs
+ _OBJC_IVAR_$_CADMockSpotlightIndex._batchOpen
+ _OBJC_IVAR_$_CADMockSpotlightIndex.needsReindex
+ _OBJC_IVAR_$_CADMockSpotlightIndexProvider._failureCallback
+ __OBJC_$_PROP_LIST_CADEventOccurrenceSet
+ __OBJC_$_PROP_LIST_CADSpotlightIndex
+ ___52-[CADSpotlightIndexer _deleteFromIndex:eventsIndex:]_block_invoke
+ ___52-[CADSpotlightIndexer _deleteFromIndex:eventsIndex:]_block_invoke.134
+ ___52-[CADSpotlightIndexer _deleteFromIndex:eventsIndex:]_block_invoke.134.cold.1
+ ___52-[CADSpotlightIndexer _deleteFromIndex:eventsIndex:]_block_invoke.cold.1
+ ___61-[CADSpotlightIndexer _sendSpotlightUpdates:deletes:toIndex:]_block_invoke.157
+ ___61-[CADSpotlightIndexer _sendSpotlightUpdates:deletes:toIndex:]_block_invoke.157.cold.1
+ ___61-[CADSpotlightIndexer _sendSpotlightUpdates:deletes:toIndex:]_block_invoke.161
+ ___61-[CADSpotlightIndexer _sendSpotlightUpdates:deletes:toIndex:]_block_invoke.161.cold.1
+ ___61-[CADSpotlightIndexer _sendSpotlightUpdates:deletes:toIndex:]_block_invoke.cold.1
+ ___88-[CADSpotlightIndexer _deleteAllSearchableItemsAndSetClientStateForBundleID:eventIndex:]_block_invoke
+ ___88-[CADSpotlightIndexer _deleteAllSearchableItemsAndSetClientStateForBundleID:eventIndex:]_block_invoke.59
+ ___88-[CADSpotlightIndexer _deleteAllSearchableItemsAndSetClientStateForBundleID:eventIndex:]_block_invoke.59.cold.1
+ ___88-[CADSpotlightIndexer _deleteAllSearchableItemsAndSetClientStateForBundleID:eventIndex:]_block_invoke_2
+ ___88-[CADSpotlightIndexer _deleteAllSearchableItemsAndSetClientStateForBundleID:eventIndex:]_block_invoke_2.cold.1
+ ___88-[CADSpotlightIndexer _deleteAllSearchableItemsAndSetClientStateForBundleID:eventIndex:]_block_invoke_2.cold.2
+ ___95-[CADCoreSpotlightIndex endIndexBatchWithExpectedClientState:newClientState:completionHandler:]_block_invoke
+ ___95-[CADMockSpotlightIndex endIndexBatchWithExpectedClientState:newClientState:completionHandler:]_block_invoke
+ ___99-[CADSpotlightIndexer reindexItemsWithIdentifiers:bundleID:protectionClass:acknowledgementHandler:]_block_invoke.211
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40r_e17_v16?0"NSError"8lr40l8s32l8
+ ___block_descriptor_49_e8_32s40r_e17_v16?0"NSError"8lr40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48r_e5_v8?0ls32l8r48l8s40l8
+ ___block_descriptor_56_e8_32s40r_e17_v16?0"NSError"8lr40l8s32l8
+ ___block_descriptor_56_e8_32s40s48r_e17_v16?0"NSError"8ls32l8r48l8s40l8
+ ___block_descriptor_56_e8_32s40s48w_e5_B8?0lw48l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56bs64r_e5_v8?0ls32l8r64l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e8_B12?0B8ls32l8s40l8s48l8r64l8s56l8
+ _objc_msgSend$_batchFailureError
+ _objc_msgSend$_deleteAllSearchableItemsAndSetClientStateForBundleID:eventIndex:
+ _objc_msgSend$_deleteFromIndex:eventsIndex:
+ _objc_msgSend$_expectedClientState
+ _objc_msgSend$_upsertToIndex:inDatabase:personaID:deleteBeforeInserting:eventsIndex:
+ _objc_msgSend$beginIndexBatch
+ _objc_msgSend$dataWithBytes:length:
+ _objc_msgSend$endIndexBatchWithExpectedClientState:newClientState:completionHandler:
+ _objc_msgSend$failureCallback
+ _objc_msgSend$hasInvalidDates
+ _objc_msgSend$needsReindex
- -[CADSpotlightIndexer _deleteFromIndex:]
- -[CADSpotlightIndexer _upsertToIndex:inDatabase:personaID:deleteBeforeInserting:].cold.1
- -[CADSpotlightIndexer _upsertToIndex:inDatabase:personaID:deleteBeforeInserting:].cold.2
- ___40-[CADSpotlightIndexer _deleteFromIndex:]_block_invoke
- ___40-[CADSpotlightIndexer _deleteFromIndex:]_block_invoke.cold.1
- ___46-[CADSpotlightIndexer _fullReindexWithReason:]_block_invoke.63
- ___46-[CADSpotlightIndexer _fullReindexWithReason:]_block_invoke_2.64
- ___46-[CADSpotlightIndexer _fullReindexWithReason:]_block_invoke_2.64.cold.1
- ___46-[CADSpotlightIndexer _fullReindexWithReason:]_block_invoke_2.64.cold.2
- ___61-[CADSpotlightIndexer _sendSpotlightUpdates:deletes:toIndex:]_block_invoke.147
- ___61-[CADSpotlightIndexer _sendSpotlightUpdates:deletes:toIndex:]_block_invoke.147.cold.1
- ___61-[CADSpotlightIndexer _sendSpotlightUpdates:deletes:toIndex:]_block_invoke.151
- ___61-[CADSpotlightIndexer _sendSpotlightUpdates:deletes:toIndex:]_block_invoke.151.cold.1
- ___99-[CADSpotlightIndexer reindexItemsWithIdentifiers:bundleID:protectionClass:acknowledgementHandler:]_block_invoke.201
- ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
- ___block_descriptor_57_e8_32s40s48r_e17_v16?0"NSError"8lr48l8s32l8s40l8
- ___block_descriptor_64_e8_32s40s48bs56r_e17_v16?0"NSError"8ls32l8r56l8s48l8s40l8
- ___block_descriptor_64_e8_32s40s48s56r_e17_v16?0"NSError"8ls32l8r56l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56r_e8_B12?0B8ls32l8s40l8r56l8s48l8
- ___block_descriptor_72_e8_32s40s48s56r_e5_v8?0ls32l8s40l8s48l8r56l8
- _objc_msgSend$_deleteFromIndex:
- _objc_retain_x9
CStrings:
+ "B52@0:8^{__CFArray=}16^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}24@32B40@44"
+ "B8@?0"
+ "Batch failed due to mismatch client state. Flagging for reindex %@"
+ "Error reseting client state, error = %@"
+ "Failed to execute batch request %@"
+ "Failed to execute deletes for domain ids: %{public}@, %@"
+ "Failed to execute spotlight deletes for domain ids: %@"
+ "Finished executing delete of %lu events and updates of %lu events into batch"
+ "Finished pushing %lu events into batch"
+ "Finished pushing delete of %lu events into batch"
+ "Q32@0:8i16i20@24"
+ "T@?,C,N,V_failureCallback"
+ "TB,R,N,V_hasInvalidDates"
+ "TB,R,N,VneedsReindex"
+ "_batchFailureError"
+ "_batchJobs"
+ "_batchOpen"
+ "_deleteAllSearchableItemsAndSetClientStateForBundleID:eventIndex:"
+ "_deleteFromIndex:eventsIndex:"
+ "_expectedClientState"
+ "_failureCallback"
+ "_hasInvalidDates"
+ "_upsertToIndex:inDatabase:personaID:deleteBeforeInserting:eventsIndex:"
+ "beginIndexBatch"
+ "beginIndexBatch called"
+ "beginIndexBatch called in middle of batch"
+ "dataWithBytes:length:"
+ "deleteSearchableItemsWithDomainIdentifiers called outside batch"
+ "endIndexBatchWithExpectedClientState called"
+ "endIndexBatchWithExpectedClientState called outside batch request"
+ "endIndexBatchWithExpectedClientState called with expectedClientState %@"
+ "endIndexBatchWithExpectedClientState:newClientState:completionHandler:"
+ "failureCallback"
+ "hasInvalidDates"
+ "needsReindex"
+ "setFailureCallback:"
+ "v40@0:8@\"NSData\"16@\"NSData\"24@?<v@?@\"NSError\">32"
- "B32@0:8i16i20@24"
- "Finished delete of %lu events, beginning indexing"
- "Finished indexing of %lu events"
- "_deleteFromIndex:"

```
