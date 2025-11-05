## HomeKitEventRouter

> `/System/Library/PrivateFrameworks/HomeKitEventRouter.framework/Versions/A/HomeKitEventRouter`

```diff

-1241.4.11.0.0
-  __TEXT.__text: 0x19b48
-  __TEXT.__auth_stubs: 0x4c0
-  __TEXT.__objc_methlist: 0x12d0
+1278.5.13.4.2
+  __TEXT.__text: 0x19aa0
+  __TEXT.__auth_stubs: 0x4b0
+  __TEXT.__objc_methlist: 0x157c
   __TEXT.__const: 0x40
   __TEXT.__gcc_except_tab: 0x598
   __TEXT.__cstring: 0xb2f
   __TEXT.__oslogstring: 0x1d6b
-  __TEXT.__unwind_info: 0x690
+  __TEXT.__unwind_info: 0x660
   __TEXT.__objc_classname: 0x2d1
   __TEXT.__objc_methname: 0x3474
   __TEXT.__objc_methtype: 0xa99

   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xaf0
+  __DATA_CONST.__objc_selrefs: 0xb70
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x270
+  __AUTH_CONST.__auth_got: 0x268
   __AUTH_CONST.__const: 0x510
   __AUTH_CONST.__cfstring: 0x740
-  __AUTH_CONST.__objc_const: 0x2988
+  __AUTH_CONST.__objc_const: 0x24f0
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x640

   __DATA.__data: 0x4e0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
+  - /System/Library/PrivateFrameworks/MobileStoreDemoCore.framework/Versions/A/MobileStoreDemoCore
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/Versions/A/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 35AA616B-EDE6-33EB-A69D-BD2BA8A14A6D
-  Functions: 505
-  Symbols:   1276
+  UUID: AB5BF8E0-DFC2-38FE-8D2C-07882FE4A6B0
+  Functions: 504
+  Symbols:   1275
   CStrings:  973
 
Symbols:
- _fmod
Functions:
~ -[HMETopicRouter dumpStateDescription] : 1460 -> 1480
~ -[HMELastEventStore writer:saveEventIfDifferent:topic:] : 856 -> 848
~ -[HMELastEventStore _doesCachePolicyAllowSaveForEvent:] : 348 -> 344
~ -[HMELastEventStore _executeInsertWithStatement:query:key:value:eventSource:eventTimestamp:eventCachePolicy:eventCombineType:eventQOS:outDidChangeRow:error:] : 664 -> 648
~ -[HMELastEventStore resetWildcardTopics:] : 684 -> 672
~ -[HMELastEventStore resetTopic:] : 684 -> 672
~ -[HMELastEventStore _executeSelectEventByKeyStatementWithKey:outResult:error:] : 928 -> 924
~ -[HMELastEventStore resetEventStore] : 296 -> 292
~ -[HMELastEventStore startup] : 160 -> 156
~ -[HMELastEventStore _startupWithRepair:] : 3056 -> 3036
~ -[HMERouterClient forwardingTopicsForTopics:] : 44 -> 8
~ -[HMERouterClient handleChangeRegistrationsWithTopicFilterAdditions:removals:] : 756 -> 752
~ -[HMERouterClient processReceivedEvents:] : 1104 -> 1136
~ -[HMERouterClient didChangeRegistrationsWithTopicFilterAdditions:removals:] : 332 -> 328
~ -[HMEProtoEventMetadata hash] : 300 -> 308
~ _HMEProtoEventMetadataReadFrom : 1012 -> 1024
- sub_238165174
~ -[HMEThreadSafePendingEventsCollection resetItems] : 96 -> 92
~ -[HMEThreadSafePendingEventsCollection popEventItemsUpWithFragments:toSizeInBytes:usedBytes:] : 168 -> 164
~ -[HMEThreadSafePendingEventsCollection hasEventItem] : 104 -> 108
~ -[HMEThreadSafePendingEventsCollection addEventInfoItems:] : 164 -> 160
~ -[HMEThreadSafePendingEventsCollection addEventInfo:] : 164 -> 160
~ -[HMEThreadSafePendingEventsCollection combinePreviousEvents:] : 164 -> 160
~ -[HMEThreadSafePendingEventsCollection isFinishedAddingItems] : 84 -> 88
~ -[HMEThreadSafePendingEventsCollection didFinishAddingAdditionalEvents] : 156 -> 152
~ -[HMEThreadSafePendingEventsCollection willAddAdditionalEvents] : 92 -> 88
~ -[HMEThreadSafePendingEventsCollection eventItems] : 128 -> 132
~ -[HMEMessageDatagramClient dumpStateDescription] : 296 -> 288
~ -[HMEMessageDatagramClient _performNextOperation] : 1664 -> 1660
~ -[HMEMessageDatagramClient _enableKeepAliveIfNeeded] : 568 -> 564
~ ___60-[HMEMessageDatagramClient _performSubscriptionFetchRequest]_block_invoke : 544 -> 540
~ ___52-[HMEMessageDatagramClient _performKeepAliveRequest]_block_invoke : 444 -> 440
~ -[HMEMessageDatagramClient _enableReconnectTimer] : 708 -> 704
~ ___62-[HMEMessageDatagramClient _performChangeRegistrationsRequest]_block_invoke : 884 -> 880
~ ___53-[HMEMessageDatagramClient _performDisconnectRequest]_block_invoke : 464 -> 460
~ ___50-[HMEMessageDatagramClient _performConnectRequest]_block_invoke : 684 -> 680
~ __50-[HMEMessageDatagramClient _performConnectRequest]_block_invoke.17 : 900 -> 896
~ -[HMERouterServer expandedTopicsForTopics:] : 44 -> 8
~ -[HMEPendingTopicsCombiner combineWithAdditions:removals:] : 640 -> 636
~ -[HMEMessageDatagramServer _addCachedEvents:connections:] : 908 -> 912
~ -[HMEMessageDatagramServer _startDebounceTimerIfNeeded] : 1020 -> 1016
~ ___44-[HMEMessageDatagramServer _performRequest:]_block_invoke : 472 -> 456
~ ___44-[HMEMessageDatagramServer _performRequest:]_block_invoke_2 : 924 -> 964
~ ___destroy_helper_block_e8_32s40s48w56w : 80 -> 76
~ _HMEEventComponentsFromTopic : 1248 -> 1244
~ -[HMEMessageDatagramServer _setupAndStartExpiryTimer] : 968 -> 964
~ -[HMEPersistentConnectionClient didReconnect] : 476 -> 472

```
