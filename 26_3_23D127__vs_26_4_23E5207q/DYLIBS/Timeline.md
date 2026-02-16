## Timeline

> `/System/Library/PrivateFrameworks/Timeline.framework/Timeline`

```diff

 22.0.0.0.0
-  __TEXT.__text: 0x7500
-  __TEXT.__auth_stubs: 0x440
+  __TEXT.__text: 0x79f8
+  __TEXT.__auth_stubs: 0x3e0
   __TEXT.__objc_methlist: 0xc6c
   __TEXT.__const: 0x68
   __TEXT.__gcc_except_tab: 0x504
   __TEXT.__cstring: 0x41e
   __TEXT.__oslogstring: 0xce
-  __TEXT.__unwind_info: 0x488
+  __TEXT.__unwind_info: 0x490
   __TEXT.__objc_classname: 0x1ed
   __TEXT.__objc_methname: 0x1725
   __TEXT.__objc_methtype: 0x46f

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_arraydata: 0xb0
-  __AUTH_CONST.__auth_got: 0x230
+  __AUTH_CONST.__auth_got: 0x200
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x500
   __AUTH_CONST.__objc_const: 0x17d8

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 93EA43E2-3B04-3844-A2C0-D473DDCD7626
+  UUID: 940EC2E1-0225-3067-8389-31ED4D2EA2B3
   Functions: 231
-  Symbols:   1011
+  Symbols:   1005
   CStrings:  496
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x24
- _objc_retain_x26
- _objc_retain_x3
- _objc_retain_x8
Functions:
~ -[TLTimelineNode encodeWithCoder:] : 192 -> 200
~ -[TLTimelineNode initWithCoder:] : 208 -> 216
~ -[TLTimelineNode hash] : 208 -> 232
~ -[TLTimelineNode isEqualToObject:includingLeftNodes:includingRightNodes:] : 284 -> 296
~ -[TLTimelineBlobEntry initWithBlob:atDate:] : 156 -> 152
~ -[TLTimelineBlobEntry initWithCoder:] : 188 -> 196
~ -[TLTimelineBlobEntry encodeWithCoder:] : 148 -> 156
~ -[TLTimelineBlobEntry tl_validate:] : 364 -> 388
~ -[TLTimelineBlobEntry hash] : 96 -> 104
~ -[TLTimelineBlobEntry isEqual:] : 336 -> 368
~ -[TLTimelineBlobEntry copyWithZone:] : 108 -> 116
~ -[TLTimelineBlobEntry description] : 280 -> 304
~ -[TLTimelineBlobEntry tl_setEntryDate:] : 12 -> 64
~ ___19-[TLOperation init]_block_invoke : 220 -> 236
~ -[TLTimelineExtendOperation main] : 708 -> 728
~ ___33-[TLTimelineExtendOperation main]_block_invoke : 172 -> 176
~ -[TLTimelineSetupOperation main] : 1224 -> 1236
~ ___32-[TLTimelineSetupOperation main]_block_invoke : 156 -> 164
~ ___32-[TLTimelineSetupOperation main]_block_invoke_2 : 156 -> 164
~ +[TLTimelineEntryNodeRecycleBin sharedRecycleBin] : 68 -> 84
~ -[TLTimelineEntryNodeRecycleBin recycleEntryNode:] : 436 -> 488
~ -[TLTimelineEntryNodeRecycleBin retrieveRecycledEntryNode] : 212 -> 232
~ -[TLTimelineEntryNodeRecycleBin emptyRecycleBin] : 120 -> 128
~ __SharedRecycleBin : 68 -> 84
~ -[TLTimelineEntryNodeRecycleBin numberOfRecycledNodes] : 112 -> 120
~ -[TLTimelineWindow initWithCoder:] : 200 -> 204
~ -[TLTimelineWindow encodeWithCoder:] : 208 -> 212
~ -[TLTimelineWindow copyWithZone:] : 180 -> 184
~ -[TLTimelineWindow hash] : 128 -> 132
~ -[TLTimelineWindow isEqual:] : 344 -> 356
~ -[TLTimelineWindow initWithFocalNode:maxNodes:leftSegmentCount:rightSegmentCount:] : 316 -> 320
~ -[TLTimelineWindow initWithFocalNode:maxNodes:] : 228 -> 224
~ -[TLTimelineWindow initWithFocalNode:leftSegment:rightSegment:maxNodes:] : 196 -> 188
~ -[TLTimelineWindow updateFocalNodeWithDate:] : 448 -> 472
~ -[TLTimelineWindow rebalance] : 468 -> 472
~ -[TLTimelineWindow leftmostNode] : 108 -> 116
~ -[TLTimelineWindow rightmostNode] : 108 -> 116
~ -[TLTimelineWindow leftmostContiguousEntryDate] : 76 -> 84
~ -[TLTimelineWindow rightmostContiguousEntryDate] : 76 -> 84
~ -[TLTimelineWindow leftEntryCount] : 88 -> 92
~ -[TLTimelineWindow rightEntryCount] : 88 -> 92
~ _TLLoggingObjectForDomain : 132 -> 140
~ ___TLLoggingObjectForDomain_block_invoke : 220 -> 228
~ -[TLTimelineSessionOperation initWithProvider:operations:providerTimeout:operationTimeout:] : 444 -> 448
~ ___91-[TLTimelineSessionOperation initWithProvider:operations:providerTimeout:operationTimeout:]_block_invoke : 164 -> 172
~ ___91-[TLTimelineSessionOperation initWithProvider:operations:providerTimeout:operationTimeout:]_block_invoke_2 : 216 -> 232
~ -[TLTimelineSessionOperation cancel] : 324 -> 336
~ -[TLTimelineSessionOperation main] : 896 -> 908
~ ___34-[TLTimelineSessionOperation main]_block_invoke : 156 -> 164
~ ___34-[TLTimelineSessionOperation main]_block_invoke_2 : 984 -> 1028
~ +[TLTimelineUtilities object:isEqualToObject:] : 132 -> 128
~ -[TLTimelineSegment initWithCoder:] : 224 -> 228
~ -[TLTimelineSegment encodeWithCoder:] : 152 -> 156
~ -[TLTimelineSegment copyWithZone:] : 228 -> 236
~ -[TLTimelineSegment isEqual:] : 236 -> 244
~ -[TLTimelineSegment hash] : 104 -> 108
~ -[TLTimelineSegment initWithLeftmostNode:rightmostNode:count:] : 160 -> 152
~ -[TLTimelineSegment containsNode:] : 276 -> 292
~ -[TLTimelineSegment expandToRight] : 144 -> 152
~ -[TLTimelineSegment expandToLeft] : 144 -> 152
~ -[TLTimelineSegment contractFromRight] : 132 -> 140
~ -[TLTimelineSegment contractFromLeft] : 132 -> 140
~ -[TLTimelineSegment shiftRight] : 108 -> 112
~ -[TLTimelineSegment shiftLeft] : 108 -> 112
~ -[TLTimelineSegment duration] : 180 -> 196
~ -[TLPreviewTimelineSelectableRegion initWithCoder:] : 120 -> 124
~ -[TLPreviewTimelineSelectableRegion encodeWithCoder:] : 172 -> 180
~ -[TLPreviewTimelineSelectableRegion hash] : 56 -> 60
~ -[TLPreviewTimelineSelectableRegion isEqual:] : 312 -> 320
~ -[TLPreviewTimelineSelectableRegion copyWithZone:] : 132 -> 136
~ -[TLTimelineEntryNode encodeWithCoder:] : 196 -> 208
~ -[TLTimelineEntryNode initWithCoder:] : 264 -> 276
~ -[TLTimelineEntryNode setEntry:] : 132 -> 144
~ -[TLTimelineEntryNode date] : 76 -> 84
~ -[TLTimelineEntryNode hash] : 128 -> 132
~ -[TLTimelineEntryNode isEqual:] : 200 -> 208
~ -[TLTimelineEntryNode copyWithZone:] : 308 -> 336
~ -[TLTimelineEntryNode(TLTimelineEntryNodeAdditions) rightEntryNode] : 132 -> 144
~ __NodeIfEntryNode : 88 -> 100
~ -[TLTimelineEntryNode(TLTimelineEntryNodeAdditions) leftEntryNode] : 132 -> 144
~ -[TLPreviewTimelineError initWithErrorType:errorDescription:path:] : 164 -> 160
~ -[TLPreviewTimelineError initWithCoder:] : 184 -> 192
~ -[TLPreviewTimelineError encodeWithCoder:] : 188 -> 196
~ -[TLPreviewTimelineError hash] : 108 -> 116
~ -[TLPreviewTimelineError isEqual:] : 380 -> 412
~ -[TLPreviewTimelineError copyWithZone:] : 124 -> 132
~ -[TLTimeline initWithCoder:] : 144 -> 148
~ -[TLTimeline encodeWithCoder:] : 152 -> 156
~ -[TLTimeline copyWithZone:] : 112 -> 116
~ -[TLTimeline initWithWindow:paused:] : 228 -> 240
~ -[TLTimeline initWithEntry:] : 148 -> 152
~ __DequeueRecycledEntryNode : 84 -> 92
~ -[TLTimeline dealloc] : 128 -> 132
~ -[TLTimeline isEqual:] : 212 -> 220
~ -[TLTimeline hash] : 104 -> 108
~ -[TLTimeline setUpdatesNowNodeOnSignificantTimeChange:] : 308 -> 312
~ -[TLTimeline updatesNowNodeOnSignificantTimeChange] : 60 -> 64
~ -[TLTimeline setDelegate:] : 132 -> 136
~ -[TLTimeline resetWithEntry:] : 136 -> 140
~ -[TLTimeline entriesWithinDateInterval:] : 384 -> 416
~ -[TLTimeline extendRightFromDate:withEntries:] : 440 -> 472
~ __AttachNodes : 100 -> 104
~ -[TLTimeline nowEntry] : 116 -> 120
~ -[TLTimeline nowWindow] : 8 -> 56
~ -[TLTimeline endOfVisibilityForNowEntry] : 100 -> 112
~ -[TLTimeline description] : 208 -> 232
~ -[TLTimeline _updateTimer] : 680 -> 748
~ -[TLTimeline _timerFired] : 96 -> 100
~ -[TLTimeline _nowEntry] : 76 -> 84
~ -[TLTimeline _setupWithEntry:] : 184 -> 196
~ +[TLTimeline TLTimelineSegmentFromSortedEntries:withLowerBound:upperBound:] : 660 -> 676
~ ___29-[TLTimeline _sortedEntries:]_block_invoke : 112 -> 120
~ -[TLTimeline _updateNowWindow] : 288 -> 300
~ -[TLTimeline _trimTimeline] : 376 -> 388
~ __RecycleNode : 100 -> 104

```
