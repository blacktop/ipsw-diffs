## Timeline

> `/System/Library/PrivateFrameworks/Timeline.framework/Timeline`

```diff

 22.0.0.0.0
-  __TEXT.__text: 0x79f8
-  __TEXT.__auth_stubs: 0x3e0
+  __TEXT.__text: 0x74dc
   __TEXT.__objc_methlist: 0xc6c
   __TEXT.__const: 0x68
   __TEXT.__gcc_except_tab: 0x504
-  __TEXT.__cstring: 0x41e
+  __TEXT.__cstring: 0x432
   __TEXT.__oslogstring: 0xce
-  __TEXT.__unwind_info: 0x490
-  __TEXT.__objc_classname: 0x1ed
-  __TEXT.__objc_methname: 0x1725
-  __TEXT.__objc_methtype: 0x46f
-  __TEXT.__objc_stubs: 0x13a0
-  __DATA_CONST.__got: 0x100
+  __TEXT.__unwind_info: 0x488
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1a0
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_arraydata: 0xb0
-  __AUTH_CONST.__auth_got: 0x200
+  __DATA_CONST.__got: 0x100
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x500
   __AUTH_CONST.__objc_const: 0x17d8
   __AUTH_CONST.__objc_dictobj: 0x1b8
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x4b0
   __DATA.__objc_ivar: 0xb8
   __DATA.__data: 0x360

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6B318FF7-1578-3BBC-A992-B41CE5B1803E
+  UUID: D59FCFB0-93EE-389B-832B-2A14A6627755
   Functions: 231
-  Symbols:   1005
-  CStrings:  496
+  Symbols:   1011
+  CStrings:  98
 
Symbols:
+ __OBJC_$_PROP_LIST_TLTimelineWindow.112
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x24
+ _objc_retain_x26
+ _objc_retain_x3
+ _objc_retain_x8
- __OBJC_$_PROP_LIST_TLTimelineWindow.113
- _objc_retainAutoreleasedReturnValue
Functions:
~ -[TLTimelineNode encodeWithCoder:] : 200 -> 192
~ -[TLTimelineNode initWithCoder:] : 216 -> 208
~ -[TLTimelineNode hash] : 232 -> 208
~ -[TLTimelineNode isEqualToObject:includingLeftNodes:includingRightNodes:] : 296 -> 280
~ -[TLTimelineBlobEntry initWithBlob:atDate:] : 152 -> 156
~ -[TLTimelineBlobEntry initWithCoder:] : 196 -> 188
~ -[TLTimelineBlobEntry encodeWithCoder:] : 156 -> 148
~ -[TLTimelineBlobEntry tl_validate:] : 388 -> 364
~ -[TLTimelineBlobEntry hash] : 104 -> 96
~ -[TLTimelineBlobEntry isEqual:] : 368 -> 336
~ -[TLTimelineBlobEntry copyWithZone:] : 116 -> 108
~ -[TLTimelineBlobEntry description] : 304 -> 280
~ -[TLTimelineBlobEntry tl_setEntryDate:] : 64 -> 12
~ ___19-[TLOperation init]_block_invoke : 236 -> 220
~ -[TLTimelineExtendOperation initWithIdentifiable:afterDate:timeout:entryLimit:] : 188 -> 200
~ -[TLTimelineExtendOperation main] : 728 -> 708
~ ___33-[TLTimelineExtendOperation main]_block_invoke : 176 -> 172
~ -[TLTimelineExtendOperation afterDate] : 16 -> 20
~ -[TLTimelineExtendOperation timeout] : 16 -> 20
~ -[TLTimelineExtendOperation limit] : 16 -> 20
~ -[TLTimelineSetupOperation initWithIdentifiable:timeout:entryLimit:] : 124 -> 132
~ -[TLTimelineSetupOperation main] : 1236 -> 1224
~ ___32-[TLTimelineSetupOperation main]_block_invoke : 164 -> 156
~ ___32-[TLTimelineSetupOperation main]_block_invoke_2 : 164 -> 156
~ -[TLTimelineSetupOperation timeout] : 16 -> 20
~ -[TLTimelineSetupOperation entryLimit] : 16 -> 20
~ +[TLTimelineEntryNodeRecycleBin sharedRecycleBin] : 84 -> 68
~ -[TLTimelineEntryNodeRecycleBin recycleEntryNode:] : 488 -> 436
~ -[TLTimelineEntryNodeRecycleBin retrieveRecycledEntryNode] : 232 -> 212
~ -[TLTimelineEntryNodeRecycleBin emptyRecycleBin] : 128 -> 120
~ __SharedRecycleBin : 84 -> 68
~ -[TLTimelineEntryNodeRecycleBin numberOfRecycledNodes] : 120 -> 112
~ -[TLTimelineOperation initWithIdentifiable:] : 124 -> 128
~ -[TLTimelineOperation identifiable] : 16 -> 20
~ -[TLTimelineWindow initWithCoder:] : 204 -> 200
~ -[TLTimelineWindow encodeWithCoder:] : 212 -> 208
~ -[TLTimelineWindow copyWithZone:] : 184 -> 180
~ -[TLTimelineWindow hash] : 132 -> 128
~ -[TLTimelineWindow isEqual:] : 356 -> 344
~ -[TLTimelineWindow initWithFocalNode:maxNodes:leftSegmentCount:rightSegmentCount:] : 320 -> 316
~ -[TLTimelineWindow initWithFocalNode:maxNodes:] : 224 -> 228
~ -[TLTimelineWindow initWithFocalNode:leftSegment:rightSegment:maxNodes:] : 188 -> 196
~ -[TLTimelineWindow updateFocalNodeWithDate:] : 472 -> 448
~ -[TLTimelineWindow rebalance] : 472 -> 468
~ -[TLTimelineWindow leftmostNode] : 116 -> 108
~ -[TLTimelineWindow rightmostNode] : 116 -> 108
~ -[TLTimelineWindow leftmostContiguousEntryDate] : 84 -> 76
~ -[TLTimelineWindow rightmostContiguousEntryDate] : 84 -> 76
~ -[TLTimelineWindow leftEntryCount] : 92 -> 88
~ -[TLTimelineWindow rightEntryCount] : 92 -> 88
~ _TLLoggingObjectForDomain : 140 -> 132
~ ___TLLoggingObjectForDomain_block_invoke : 228 -> 220
~ -[TLTimelineSessionOperation initWithProvider:operations:providerTimeout:operationTimeout:] : 448 -> 456
~ ___91-[TLTimelineSessionOperation initWithProvider:operations:providerTimeout:operationTimeout:]_block_invoke : 172 -> 164
~ ___91-[TLTimelineSessionOperation initWithProvider:operations:providerTimeout:operationTimeout:]_block_invoke_2 : 232 -> 216
~ -[TLTimelineSessionOperation cancel] : 336 -> 328
~ -[TLTimelineSessionOperation main] : 908 -> 896
~ ___34-[TLTimelineSessionOperation main]_block_invoke : 164 -> 156
~ ___34-[TLTimelineSessionOperation main]_block_invoke_2 : 1028 -> 984
~ -[TLTimelineSessionOperation provider] : 16 -> 20
~ -[TLTimelineSessionOperation operations] : 16 -> 20
~ -[TLTimelineSessionOperation providerTimeout] : 16 -> 20
~ -[TLTimelineSessionOperation operationTimeout] : 16 -> 20
~ -[TLTimelineSessionOperation operationQueue] : 16 -> 20
~ +[TLTimelineUtilities object:isEqualToObject:] : 128 -> 132
~ -[TLTimelineSegment initWithCoder:] : 228 -> 224
~ -[TLTimelineSegment encodeWithCoder:] : 156 -> 152
~ -[TLTimelineSegment copyWithZone:] : 236 -> 228
~ -[TLTimelineSegment isEqual:] : 244 -> 236
~ -[TLTimelineSegment hash] : 108 -> 104
~ -[TLTimelineSegment initWithLeftmostNode:rightmostNode:count:] : 152 -> 160
~ -[TLTimelineSegment containsNode:] : 292 -> 276
~ -[TLTimelineSegment expandToRight] : 152 -> 144
~ -[TLTimelineSegment expandToLeft] : 152 -> 144
~ -[TLTimelineSegment contractFromRight] : 140 -> 132
~ -[TLTimelineSegment contractFromLeft] : 140 -> 132
~ -[TLTimelineSegment shiftRight] : 112 -> 108
~ -[TLTimelineSegment shiftLeft] : 112 -> 108
~ -[TLTimelineSegment duration] : 196 -> 180
~ -[TLPreviewTimelineSelectableRegion initWithCoder:] : 124 -> 120
~ -[TLPreviewTimelineSelectableRegion encodeWithCoder:] : 180 -> 172
~ -[TLPreviewTimelineSelectableRegion hash] : 60 -> 56
~ -[TLPreviewTimelineSelectableRegion isEqual:] : 320 -> 312
~ -[TLPreviewTimelineSelectableRegion copyWithZone:] : 136 -> 132
~ -[TLTimelineEntryNode encodeWithCoder:] : 208 -> 196
~ -[TLTimelineEntryNode initWithCoder:] : 276 -> 268
~ -[TLTimelineEntryNode entry] : 92 -> 96
~ -[TLTimelineEntryNode setEntry:] : 144 -> 132
~ -[TLTimelineEntryNode date] : 84 -> 76
~ -[TLTimelineEntryNode hash] : 132 -> 128
~ -[TLTimelineEntryNode isEqual:] : 208 -> 200
~ -[TLTimelineEntryNode copyWithZone:] : 336 -> 308
~ -[TLTimelineEntryNode(TLTimelineEntryNodeAdditions) rightEntryNode] : 144 -> 132
~ __NodeIfEntryNode : 100 -> 88
~ -[TLTimelineEntryNode(TLTimelineEntryNodeAdditions) leftEntryNode] : 144 -> 132
~ -[TLPreviewTimelineError initWithErrorType:errorDescription:path:] : 160 -> 164
~ -[TLPreviewTimelineError initWithCoder:] : 192 -> 184
~ -[TLPreviewTimelineError encodeWithCoder:] : 196 -> 188
~ -[TLPreviewTimelineError hash] : 116 -> 108
~ -[TLPreviewTimelineError isEqual:] : 412 -> 380
~ -[TLPreviewTimelineError copyWithZone:] : 132 -> 124
~ -[TLTimeline initWithCoder:] : 148 -> 144
~ -[TLTimeline encodeWithCoder:] : 156 -> 152
~ -[TLTimeline copyWithZone:] : 116 -> 112
~ -[TLTimeline initWithWindow:paused:] : 240 -> 228
~ -[TLTimeline initWithEntry:] : 152 -> 148
~ __DequeueRecycledEntryNode : 92 -> 84
~ -[TLTimeline dealloc] : 132 -> 128
~ -[TLTimeline isEqual:] : 220 -> 212
~ -[TLTimeline hash] : 108 -> 104
~ -[TLTimeline setUpdatesNowNodeOnSignificantTimeChange:] : 312 -> 308
~ -[TLTimeline updatesNowNodeOnSignificantTimeChange] : 64 -> 60
~ -[TLTimeline setDelegate:] : 136 -> 132
~ -[TLTimeline resetWithEntry:] : 140 -> 136
~ -[TLTimeline entriesWithinDateInterval:] : 416 -> 384
~ -[TLTimeline extendRightFromDate:withEntries:] : 472 -> 396
~ __AttachNodes : 104 -> 100
~ -[TLTimeline nowEntry] : 120 -> 116
~ -[TLTimeline nowWindow] : 56 -> 8
~ -[TLTimeline endOfVisibilityForNowEntry] : 112 -> 100
~ -[TLTimeline description] : 232 -> 208
~ -[TLTimeline _updateTimer] : 748 -> 636
~ -[TLTimeline _timerFired] : 100 -> 96
~ -[TLTimeline _nowEntry] : 84 -> 76
~ -[TLTimeline _setupWithEntry:] : 196 -> 184
~ +[TLTimeline TLTimelineSegmentFromSortedEntries:withLowerBound:upperBound:] : 676 -> 664
~ ___29-[TLTimeline _sortedEntries:]_block_invoke : 120 -> 112
~ -[TLTimeline _updateNowWindow] : 300 -> 288
~ -[TLTimeline _trimTimeline] : 388 -> 380
~ __RecycleNode : 104 -> 100
~ -[TLTimelineEntryNode initWithCoder:].cold.1 : 120 -> 76
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<TLIdentifiable>\""
- "@\"<TLTimelineDataSource>\""
- "@\"<TLTimelineDataSourceProvider>\""
- "@\"<TLTimelineDelegate>\""
- "@\"<TLTimelineEntry>\""
- "@\"NSArray\""
- "@\"NSData\""
- "@\"NSDate\""
- "@\"NSDate\"16@0:8"
- "@\"NSError\""
- "@\"NSOperationQueue\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSTimer\""
- "@\"TLTimeline\""
- "@\"TLTimelineEntryNode\""
- "@\"TLTimelineNode\""
- "@\"TLTimelineSegment\""
- "@\"TLTimelineWindow\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8^{_NSZone=}16"
- "@28@0:8@16B24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16Q24"
- "@32@0:8^{_NSZone=}16B24B28"
- "@32@0:8q16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24Q32"
- "@40@0:8@16d24Q32"
- "@40@0:8q16@24@32"
- "@48@0:8@16@24@32Q40"
- "@48@0:8@16@24d32Q40"
- "@48@0:8@16@24d32d40"
- "@48@0:8@16Q24Q32Q40"
- "@56@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"<TLIdentifiable>\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8^@16"
- "B32@0:8@16@24"
- "B32@0:8@16B24B28"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"<TLIdentifiable>\",R,N,V_identifiable"
- "T@\"<TLTimelineDataSource>\",&,V_dataSource"
- "T@\"<TLTimelineDataSourceProvider>\",R,N,V_provider"
- "T@\"<TLTimelineDelegate>\",W,N,V_delegate"
- "T@\"<TLTimelineEntry>\",&,N,V_entry"
- "T@\"<TLTimelineEntry>\",R,N"
- "T@\"NSArray\",&,V_timelineEntries"
- "T@\"NSArray\",R,C,N,V_operations"
- "T@\"NSData\",R,N,V_blob"
- "T@\"NSDate\",&,N,Stl_setEntryDate:"
- "T@\"NSDate\",&,N,Stl_setEntryDate:,V_tl_entryDate"
- "T@\"NSDate\",R,C,N"
- "T@\"NSDate\",R,N"
- "T@\"NSDate\",R,N,V_afterDate"
- "T@\"NSError\",&,V_extendError"
- "T@\"NSError\",&,V_setupError"
- "T@\"NSError\",C,V_sessionError"
- "T@\"NSError\",R,V_error"
- "T@\"NSOperationQueue\",R,C,N,V_operationQueue"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N,V_errorDescription"
- "T@\"NSString\",R,N,V_path"
- "T@\"TLTimeline\",&,V_timeline"
- "T@\"TLTimelineEntryNode\",R,N,V_focalNode"
- "T@\"TLTimelineEntryNode\",R,N,V_leftmostNode"
- "T@\"TLTimelineEntryNode\",R,N,V_rightmostNode"
- "T@\"TLTimelineNode\",&,N,V_leftNode"
- "T@\"TLTimelineNode\",&,N,V_rightNode"
- "T@\"TLTimelineSegment\",R,N,V_leftSegment"
- "T@\"TLTimelineSegment\",R,N,V_rightSegment"
- "T@?,C"
- "T@?,C,D"
- "T@?,C,V_operationCompletionBlock"
- "T@?,C,V_sessionCompletionBlock"
- "TB,N"
- "TB,N,V_paused"
- "TB,R"
- "TLFinalizable"
- "TLIdentifiable"
- "TLIdentifiableAdditions"
- "TLOperation"
- "TLPreviewTimelineError"
- "TLPreviewTimelineSelectableRegion"
- "TLTimeline"
- "TLTimelineBlobEntry"
- "TLTimelineEntry"
- "TLTimelineEntryNode"
- "TLTimelineEntryNodeAdditions"
- "TLTimelineEntryNodeRecycleBin"
- "TLTimelineExtendOperation"
- "TLTimelineNode"
- "TLTimelineOperation"
- "TLTimelineSegment"
- "TLTimelineSegmentFromSortedEntries:withLowerBound:upperBound:"
- "TLTimelineSessionOperation"
- "TLTimelineSetupOperation"
- "TLTimelineUtilities"
- "TLTimelineWindow"
- "TLValidatable"
- "TQ,R"
- "TQ,R,N"
- "TQ,R,N,V_count"
- "TQ,R,N,V_entryLimit"
- "TQ,R,N,V_limit"
- "TQ,R,N,V_maxNodes"
- "Td,R,N"
- "Td,R,N,V_operationTimeout"
- "Td,R,N,V_providerTimeout"
- "Td,R,N,V_timeout"
- "Tq,R,N,V_errorType"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_rect"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_afterDate"
- "_blob"
- "_count"
- "_dataSource"
- "_delegate"
- "_delegateRespondsToTimerFired"
- "_entry"
- "_entryLimit"
- "_error"
- "_errorDescription"
- "_errorType"
- "_extendError"
- "_focalNode"
- "_identifiable"
- "_init"
- "_leftNode"
- "_leftSegment"
- "_leftmostNode"
- "_limit"
- "_maxNodes"
- "_notifyToken"
- "_nowEntry"
- "_nowNode"
- "_nowWindow"
- "_operationCompletionBlock"
- "_operationQueue"
- "_operationTimeout"
- "_operations"
- "_path"
- "_paused"
- "_provider"
- "_providerTimeout"
- "_rect"
- "_recycleAllNodes"
- "_rightNode"
- "_rightSegment"
- "_rightmostDate"
- "_rightmostNode"
- "_sessionCompletionBlock"
- "_sessionError"
- "_setupError"
- "_setupWithEntry:"
- "_sortedEntries:"
- "_timeline"
- "_timelineEntries"
- "_timeout"
- "_timer"
- "_timerFired"
- "_tl_entryDate"
- "_trimTimeline"
- "_updateNowWindow"
- "_updateTimer"
- "_updatesNowNodeOnSignificantTimeChange"
- "addObject:"
- "addObserver:selector:name:object:"
- "addOperation:"
- "addOperations:waitUntilFinished:"
- "addTimer:forMode:"
- "afterDate"
- "allocWithZone:"
- "anyObject"
- "array"
- "autorelease"
- "cancel"
- "class"
- "compare:"
- "completionBlock"
- "conformsToProtocol:"
- "containsDate:"
- "containsNode:"
- "contractFromLeft"
- "contractFromRight"
- "copy"
- "copyWithZone:"
- "copyWithZone:copyLeftNodes:copyRightNodes:"
- "countByEnumeratingWithState:objects:count:"
- "d"
- "d16@0:8"
- "dataSource"
- "date:isOrderedAscendingToDate:"
- "dateOfLastEntryInTimeline"
- "dealloc"
- "debugDescription"
- "decodeBoolForKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "defaultCenter"
- "delegate"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "duration"
- "emptyRecycleBin"
- "encodeBool:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "endOfVisibilityForNowEntry"
- "entriesDidChangeInTimeline:"
- "entriesWithinDateInterval:"
- "entryLimit"
- "enumerateObjectsUsingBlock:"
- "error"
- "errorWithDomain:code:userInfo:"
- "expandToLeft"
- "expandToRight"
- "extendError"
- "extendRightFromDate:withEntries:"
- "extendTimelineFromDate:withEntries:"
- "hash"
- "i"
- "identifiable"
- "init"
- "initWithBlob:atDate:"
- "initWithCoder:"
- "initWithEntry:"
- "initWithErrorType:errorDescription:"
- "initWithErrorType:errorDescription:path:"
- "initWithFocalNode:leftSegment:rightSegment:maxNodes:"
- "initWithFocalNode:maxNodes:"
- "initWithFocalNode:maxNodes:leftSegmentCount:rightSegmentCount:"
- "initWithIdentifiable:"
- "initWithIdentifiable:afterDate:timeout:entryLimit:"
- "initWithIdentifiable:timeout:entryLimit:"
- "initWithLeftmostNode:rightmostNode:count:"
- "initWithOptions:capacity:"
- "initWithPath:rect:"
- "initWithProvider:operations:providerTimeout:operationTimeout:"
- "initWithWindow:paused:"
- "invalidate"
- "isCancelled"
- "isEqual:"
- "isEqualToDate:"
- "isEqualToObject:includingLeftNodes:includingRightNodes:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "lastEntry"
- "leftEntryCount"
- "leftEntryNode"
- "leftSegment"
- "leftmostContiguousEntryDate"
- "length"
- "limit"
- "localizedStringFromDate:dateStyle:timeStyle:"
- "main"
- "mainRunLoop"
- "maximumNumberOfRecycledNodes"
- "nodeCapacity"
- "nowEntry"
- "nowEntryDidChangeFrom:to:"
- "numberOfRecycledNodes"
- "numberWithDouble:"
- "numberWithInteger:"
- "numberWithUnsignedInteger:"
- "object:isEqualToObject:"
- "objectAtIndex:"
- "objectForKey:"
- "operationCompletionBlock"
- "operationQueue"
- "operationTimeout"
- "operations"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "provider"
- "providerTimeout"
- "q"
- "q16@0:8"
- "rebalance"
- "recycleEntryNode:"
- "relativePriority"
- "release"
- "removeAllObjects"
- "removeObject:"
- "removeObserver:"
- "resetWithEntry:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "retrieveRecycledEntryNode"
- "rightEntryCount"
- "rightEntryNode"
- "rightSegment"
- "rightmostContiguousEntryDate"
- "rightmostNode"
- "self"
- "sessionCompletionBlock"
- "sessionError"
- "setCompletionBlock:"
- "setDataSource:"
- "setDelegate:"
- "setEntry:"
- "setExtendError:"
- "setLeftNode:"
- "setMaxConcurrentOperationCount:"
- "setObject:forKey:"
- "setOperationCompletionBlock:"
- "setPaused:"
- "setRightNode:"
- "setSessionCompletionBlock:"
- "setSessionError:"
- "setSetupError:"
- "setTimeline:"
- "setTimelineEntries:"
- "setTimelineOperationCompletionBlock:"
- "setTolerance:"
- "setUpdatesNowNodeOnSignificantTimeChange:"
- "setupError"
- "sharedRecycleBin"
- "shiftLeft"
- "shiftRight"
- "sortedArrayUsingComparator:"
- "startDate"
- "stringByAppendingString:"
- "stringFromByteCount:countStyle:"
- "stringWithFormat:"
- "superclass"
- "supportsSecureCoding"
- "timeIntervalSinceDate:"
- "timeIntervalSinceNow"
- "timeline:didChangeNowEntryFrom:to:"
- "timelineEntries"
- "timelineOperationCompletionBlock"
- "timelineTimerDidFire:"
- "timeout"
- "timerWithTimeInterval:target:selector:userInfo:repeats:"
- "tl_entryDate"
- "tl_getCurrentTimelineEntryForIdentifiable:withHandler:"
- "tl_getDataSourceWithCompletion:"
- "tl_getTimelineEntriesForIdentifiable:afterDate:limit:withHandler:"
- "tl_isEqualToIdentifiable:"
- "tl_setEntryDate:"
- "tl_validate:"
- "updateFocalNodeWithDate:"
- "updatesNowNodeOnSignificantTimeChange"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSDate\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v32@0:8@16@24"
- "valueWithBytes:objCType:"
- "zone"
- "{CGRect=\"origin\"{CGPoint=\"x\"d\"y\"d}\"size\"{CGSize=\"width\"d\"height\"d}}"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"

```
