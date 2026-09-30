## LoggingSupport

> `/System/Library/PrivateFrameworks/LoggingSupport.framework/Versions/A/LoggingSupport`

```diff

-1612.80.7.0.0
-  __TEXT.__text: 0x5d4d0
-  __TEXT.__auth_stubs: 0x14d0
-  __TEXT.__objc_methlist: 0x2e0c
-  __TEXT.__const: 0x547
-  __TEXT.__gcc_except_tab: 0x11d4
-  __TEXT.__cstring: 0x69f2
-  __TEXT.__oslogstring: 0xc01
-  __TEXT.__unwind_info: 0x1180
-  __TEXT.__objc_classname: 0x6cd
-  __TEXT.__objc_methname: 0x6da6
-  __TEXT.__objc_methtype: 0x41bd
-  __TEXT.__objc_stubs: 0x5380
-  __DATA_CONST.__got: 0x2b0
-  __DATA_CONST.__const: 0x1058
-  __DATA_CONST.__objc_classlist: 0x218
-  __DATA_CONST.__objc_protolist: 0x38
+1643.100.44.0.0
+  __TEXT.__text: 0x647b0
+  __TEXT.__auth_stubs: 0x1510
+  __TEXT.__objc_methlist: 0x3978
+  __TEXT.__const: 0x4a3
+  __TEXT.__gcc_except_tab: 0x12d0
+  __TEXT.__cstring: 0x6e0c
+  __TEXT.__oslogstring: 0x14d8
+  __TEXT.__unwind_info: 0x1270
+  __TEXT.__objc_classname: 0x7bf
+  __TEXT.__objc_methname: 0x78bc
+  __TEXT.__objc_methtype: 0x5568
+  __TEXT.__objc_stubs: 0x5c20
+  __DATA_CONST.__got: 0x2c8
+  __DATA_CONST.__const: 0x10f8
+  __DATA_CONST.__objc_classlist: 0x260
+  __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1a78
+  __DATA_CONST.__objc_selrefs: 0x1d98
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x1a0
+  __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x440
-  __AUTH_CONST.__auth_got: 0xa78
-  __AUTH_CONST.__const: 0x1848
-  __AUTH_CONST.__cfstring: 0x30e0
-  __AUTH_CONST.__objc_const: 0x78f8
+  __AUTH_CONST.__auth_got: 0xa98
+  __AUTH_CONST.__const: 0x1a08
+  __AUTH_CONST.__cfstring: 0x31c0
+  __AUTH_CONST.__objc_const: 0x81b8
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0x360
   __AUTH_CONST.__objc_dictobj: 0xf0
-  __AUTH.__objc_data: 0x14f0
+  __AUTH.__objc_data: 0x17c0
   __AUTH.__os_assumes_log: 0x8
-  __DATA.__objc_ivar: 0x57c
-  __DATA.__data: 0x31c
+  __DATA.__objc_ivar: 0x638
+  __DATA.__data: 0x4fc
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x700
-  __DATA.__common: 0x8
+  __DATA.__common: 0x4
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 50A234EA-EC0F-3739-9693-4550EE03023B
-  Functions: 1662
-  Symbols:   3928
-  CStrings:  3196
+  UUID: 13B2E22B-4857-3E7D-B92A-CEA4871BBCB6
+  Functions: 1773
+  Symbols:   4317
+  CStrings:  3454
 
Symbols:
+ -[CacheIndex chunk_offset]
+ -[CacheIndex copyWithZone:]
+ -[CacheIndex fileIndex]
+ -[CacheIndex hash]
+ -[CacheIndex initWithCDHash:identifier:]
+ -[CacheIndex isEqual:]
+ -[CacheIndex isEqualToCacheIndex:]
+ -[CatalogsCache .cxx_destruct]
+ -[CatalogsCache cache]
+ -[CatalogsCache catalogForCDHash:identifier:generator:]
+ -[CatalogsCache flush]
+ -[CatalogsCache init:evictionHandler:]
+ -[DataCache .cxx_destruct]
+ -[DataCache cache]
+ -[DataCache dataForCDHash:identifier:size:generator:]
+ -[DataCache flush]
+ -[DataCache init:evictionHandler:]
+ -[OSLogDoublyLinkedList .cxx_destruct]
+ -[OSLogDoublyLinkedList addToTail:]
+ -[OSLogDoublyLinkedList count]
+ -[OSLogDoublyLinkedList head]
+ -[OSLogDoublyLinkedList removeAllObjects]
+ -[OSLogDoublyLinkedList removeFromHead]
+ -[OSLogDoublyLinkedList removeNodeAndAddToTail:]
+ -[OSLogDoublyLinkedList setCount:]
+ -[OSLogDoublyLinkedList setHead:]
+ -[OSLogDoublyLinkedList setTail:]
+ -[OSLogDoublyLinkedList tail]
+ -[OSLogDoublyLinkedListNode .cxx_destruct]
+ -[OSLogDoublyLinkedListNode data]
+ -[OSLogDoublyLinkedListNode initWithKey:data:]
+ -[OSLogDoublyLinkedListNode key]
+ -[OSLogDoublyLinkedListNode next]
+ -[OSLogDoublyLinkedListNode prev]
+ -[OSLogDoublyLinkedListNode setData:]
+ -[OSLogDoublyLinkedListNode setKey:]
+ -[OSLogDoublyLinkedListNode setNext:]
+ -[OSLogDoublyLinkedListNode setPrev:]
+ -[OSLogEventStream _activateStreamFromDate:toDate:useMemEffic:catalogCacheSize:dataCacheSize:]
+ -[OSLogEventStream _activateStreamInRange:useMemEffic:catalogCacheSize:dataCacheSize:]
+ -[OSLogEventStream activateStreamFromDate:catalogCacheSize:dataCacheSize:]
+ -[OSLogStatistics aggregationForLogReporterWithStartDate:endDate:predicate:withOptions:catalogCacheSize:dataCacheSize:errorOut:]
+ -[OSLogStatistics aggregationForStartDate_impl:endDate:predicate:withOptions:catalogCacheSize:dataCacheSize:useMemEffic:errorOut:]
+ -[OversizeIndex catalog_offset]
+ -[OversizeIndex chunk_offset]
+ -[OversizeIndex compareTimestamp:]
+ -[OversizeIndex fileIndex]
+ -[OversizeIndex hash64]
+ -[OversizeIndex init:msgID:pidV:timestamp:]
+ -[OversizeIndex msgID]
+ -[OversizeIndex pidversion]
+ -[OversizeIndex processID]
+ -[OversizeIndex setCatalog_offset:]
+ -[OversizeIndex setChunk_offset:]
+ -[OversizeIndex setFileIndex:]
+ -[OversizeIndex setMsgID:]
+ -[OversizeIndex setPidversion:]
+ -[OversizeIndex setProcessID:]
+ -[OversizeIndex setTimestamp:]
+ -[OversizeIndex setTp_offset:]
+ -[OversizeIndex timestamp]
+ -[OversizeIndex tp_offset]
+ -[_BaseTracepointBuffer .cxx_destruct]
+ -[_BaseTracepointBuffer _isEmpty]
+ -[_BaseTracepointBuffer advanceCursorToTime:]
+ -[_BaseTracepointBuffer allocateRow]
+ -[_BaseTracepointBuffer beginInsertingTracepointsClippingFromTime:]
+ -[_BaseTracepointBuffer bufferHasFreeSpace]
+ -[_BaseTracepointBuffer canMutate]
+ -[_BaseTracepointBuffer consolidate]
+ -[_BaseTracepointBuffer count]
+ -[_BaseTracepointBuffer cursor]
+ -[_BaseTracepointBuffer dealloc]
+ -[_BaseTracepointBuffer enumerateEventsFromTime:to:options:usingBlock:]
+ -[_BaseTracepointBuffer fileNames]
+ -[_BaseTracepointBuffer finishedInsertingTracepointsWithNextMajorTime:options:]
+ -[_BaseTracepointBuffer getFileNameAt:]
+ -[_BaseTracepointBuffer growBuffer:]
+ -[_BaseTracepointBuffer growBufferImmediatelyIfNeeded]
+ -[_BaseTracepointBuffer init]
+ -[_BaseTracepointBuffer insertChunk:chunkOffset:chunkSetStartAddr:timestamp:subchunk:]
+ -[_BaseTracepointBuffer insertNonsparsePoint:uuid:ttl:inMemory:]
+ -[_BaseTracepointBuffer insertOversizedChunk:chunkOffset:chunkSetStartAddr:subchunk:chunkList:]
+ -[_BaseTracepointBuffer insertSimpleChunk:chunkOffset:chunkSetStartAddr:subchunk:options:]
+ -[_BaseTracepointBuffer insertStatedumpChunk:chunkOffset:chunkSetStartAddr:subchunk:]
+ -[_BaseTracepointBuffer insertTimesyncPoints:forBoot:oldestContinuousTime:]
+ -[_BaseTracepointBuffer insertTracepoints:chunkOffset:chunkSetStartAddr:subchunk:options:]
+ -[_BaseTracepointBuffer setCanMutate:]
+ -[_BaseTracepointBuffer setCount:]
+ -[_BaseTracepointBuffer setCursor:]
+ -[_BaseTracepointBuffer setFileNames:]
+ -[_BaseTracepointBuffer setSize:]
+ -[_BaseTracepointBuffer size]
+ -[_MemoryEfficientEnumeratorCatalogSubchunk .cxx_destruct]
+ -[_MemoryEfficientEnumeratorCatalogSubchunk algo]
+ -[_MemoryEfficientEnumeratorCatalogSubchunk buuid]
+ -[_MemoryEfficientEnumeratorCatalogSubchunk catalog_offset]
+ -[_MemoryEfficientEnumeratorCatalogSubchunk decompressedBufferForChunk:]
+ -[_MemoryEfficientEnumeratorCatalogSubchunk endTime]
+ -[_MemoryEfficientEnumeratorCatalogSubchunk enumerateChunksUsingBlock:]
+ -[_MemoryEfficientEnumeratorCatalogSubchunk getBootUUIDIndex:]
+ -[_MemoryEfficientEnumeratorCatalogSubchunk initWithCatalog:subchunk:range:]
+ -[_MemoryEfficientEnumeratorCatalogSubchunk initWithCatalog:subchunk:range:oldestTime:endTime:]
+ -[_MemoryEfficientEnumeratorCatalogSubchunk oldestTime]
+ -[_MemoryEfficientEnumeratorCatalogSubchunk store]
+ -[_MemoryEfficientEnumeratorCatalogSubchunk usize]
+ -[_MemoryEfficientTracepointBuffer .cxx_destruct]
+ -[_MemoryEfficientTracepointBuffer addTSEntry:]
+ -[_MemoryEfficientTracepointBuffer advanceCursorToTime:]
+ -[_MemoryEfficientTracepointBuffer consolidate]
+ -[_MemoryEfficientTracepointBuffer dealloc]
+ -[_MemoryEfficientTracepointBuffer enumerateEventsFromTime:to:options:usingBlock:]
+ -[_MemoryEfficientTracepointBuffer findOversize:process:oversize_id:pidversion:timestamp:block:]
+ -[_MemoryEfficientTracepointBuffer finishedInsertingTracepointsWithNextMajorTime:options:]
+ -[_MemoryEfficientTracepointBuffer indexOfUUID:]
+ -[_MemoryEfficientTracepointBuffer init:dataCacheSize:]
+ -[_MemoryEfficientTracepointBuffer insertChunk:chunkOffset:chunkSetStartAddr:timestamp:subchunk:]
+ -[_MemoryEfficientTracepointBuffer insertNonsparsePoint:uuid:ttl:inMemory:]
+ -[_MemoryEfficientTracepointBuffer insertOversizedChunk:chunkOffset:chunkSetStartAddr:subchunk:chunkList:]
+ -[_MemoryEfficientTracepointBuffer insertTimesyncPoints:forBoot:oldestContinuousTime:]
+ -[_MemoryEfficientTracepointBuffer insertTracepoints:chunkOffset:chunkSetStartAddr:subchunk:options:]
+ -[_MemoryEfficientTracepointBuffer insertValuesIntoIndex:coffset:fileName:sortKey:type:]
+ -[_MemoryEfficientTracepointBuffer iterateChunksAndFillEvent:block:]
+ -[_MemoryEfficientTracepointBuffer retireOversize:]
+ -[_MemoryEfficientTracepointBuffer setupStoresForIndex:]
+ -[_OSLogEnumeratorCatalog chunkRange]
+ -[_OSLogEnumeratorCatalog initWithStore:index:fileHeader:range:chunk:storeCatalogsAndSubchunks:]
+ -[_OSLogEnumeratorCatalog setChunkRange:]
+ -[_OSLogEnumeratorCatalog storeCatalogsAndSubchunks]
+ -[_OSLogEnumeratorCatalogSubchunk decompressedBufferForChunk:]
+ -[_OSLogEnumeratorCatalogSubchunk getBootUUIDIndex:]
+ -[_OSLogIndex enumerateEntriesInRange:options:usingCatalogFilter:catalogCacheSize:dataCacheSize:usingBlock:]
+ -[_OSLogIndexEnumerator initWithIndex:metadata:fileBootList:catalogFilter:options:catalogCacheSize:dataCacehSize:]
+ -[_OSLogLRUCache .cxx_destruct]
+ -[_OSLogLRUCache count]
+ -[_OSLogLRUCache dealloc]
+ -[_OSLogLRUCache evictAllEntries]
+ -[_OSLogLRUCache evictionHandler]
+ -[_OSLogLRUCache initWithName:maxCount:evictionHandler:]
+ -[_OSLogLRUCache maxCount]
+ -[_OSLogLRUCache mruItems]
+ -[_OSLogLRUCache name]
+ -[_OSLogLRUCache objectForKey:]
+ -[_OSLogLRUCache removeAllObjects]
+ -[_OSLogLRUCache setEvictionHandler:]
+ -[_OSLogLRUCache setObject:forKey:]
+ -[_OSLogLRUCache storage]
+ GCC_except_table1071
+ GCC_except_table1080
+ GCC_except_table1088
+ GCC_except_table1095
+ GCC_except_table1109
+ GCC_except_table1112
+ GCC_except_table1113
+ GCC_except_table1114
+ GCC_except_table1115
+ GCC_except_table1125
+ GCC_except_table1279
+ GCC_except_table1316
+ GCC_except_table1339
+ GCC_except_table1379
+ GCC_except_table1495
+ GCC_except_table1515
+ GCC_except_table1520
+ GCC_except_table1522
+ GCC_except_table1593
+ GCC_except_table1594
+ GCC_except_table1602
+ GCC_except_table1605
+ GCC_except_table359
+ GCC_except_table364
+ GCC_except_table410
+ GCC_except_table482
+ GCC_except_table552
+ GCC_except_table662
+ GCC_except_table670
+ GCC_except_table678
+ GCC_except_table679
+ GCC_except_table731
+ GCC_except_table845
+ GCC_except_table898
+ GCC_except_table967
+ GCC_except_table970
+ GCC_except_table976
+ GCC_except_table986
+ GCC_except_table989
+ OBJC_IVAR_$_CacheIndex._chunk_offset
+ OBJC_IVAR_$_CacheIndex._fileIndex
+ OBJC_IVAR_$_CatalogsCache._cache
+ OBJC_IVAR_$_DataCache._cache
+ OBJC_IVAR_$_OSLogDoublyLinkedList._count
+ OBJC_IVAR_$_OSLogDoublyLinkedList.head
+ OBJC_IVAR_$_OSLogDoublyLinkedList.tail
+ OBJC_IVAR_$_OSLogDoublyLinkedListNode._data
+ OBJC_IVAR_$_OSLogDoublyLinkedListNode._key
+ OBJC_IVAR_$_OSLogDoublyLinkedListNode._next
+ OBJC_IVAR_$_OSLogDoublyLinkedListNode._prev
+ OBJC_IVAR_$_OversizeIndex._catalog_offset
+ OBJC_IVAR_$_OversizeIndex._chunk_offset
+ OBJC_IVAR_$_OversizeIndex._fileIndex
+ OBJC_IVAR_$_OversizeIndex._msgID
+ OBJC_IVAR_$_OversizeIndex._pidversion
+ OBJC_IVAR_$_OversizeIndex._processID
+ OBJC_IVAR_$_OversizeIndex._timestamp
+ OBJC_IVAR_$_OversizeIndex._tp_offset
+ OBJC_IVAR_$__BaseTracepointBuffer._canMutate
+ OBJC_IVAR_$__BaseTracepointBuffer._count
+ OBJC_IVAR_$__BaseTracepointBuffer._cursor
+ OBJC_IVAR_$__BaseTracepointBuffer._events
+ OBJC_IVAR_$__BaseTracepointBuffer._fileNames
+ OBJC_IVAR_$__BaseTracepointBuffer._size
+ OBJC_IVAR_$__MemoryEfficientEnumeratorCatalogSubchunk._algo
+ OBJC_IVAR_$__MemoryEfficientEnumeratorCatalogSubchunk._buuid
+ OBJC_IVAR_$__MemoryEfficientEnumeratorCatalogSubchunk._catalog_offset
+ OBJC_IVAR_$__MemoryEfficientEnumeratorCatalogSubchunk._et
+ OBJC_IVAR_$__MemoryEfficientEnumeratorCatalogSubchunk._had_subchunk
+ OBJC_IVAR_$__MemoryEfficientEnumeratorCatalogSubchunk._ot
+ OBJC_IVAR_$__MemoryEfficientEnumeratorCatalogSubchunk._range
+ OBJC_IVAR_$__MemoryEfficientEnumeratorCatalogSubchunk._store
+ OBJC_IVAR_$__MemoryEfficientEnumeratorCatalogSubchunk._usize
+ OBJC_IVAR_$__MemoryEfficientTracepointBuffer._ocount
+ OBJC_IVAR_$__MemoryEfficientTracepointBuffer._osize
+ OBJC_IVAR_$__MemoryEfficientTracepointBuffer._oversizeTable
+ OBJC_IVAR_$__MemoryEfficientTracepointBuffer._traceEvents
+ OBJC_IVAR_$__MemoryEfficientTracepointBuffer._tsEntries
+ OBJC_IVAR_$__MemoryEfficientTracepointBuffer._tscount
+ OBJC_IVAR_$__MemoryEfficientTracepointBuffer._tssize
+ OBJC_IVAR_$__MemoryEfficientTracepointBuffer._uuids
+ OBJC_IVAR_$__MemoryEfficientTracepointBuffer.catalogCache
+ OBJC_IVAR_$__MemoryEfficientTracepointBuffer.dataCache
+ OBJC_IVAR_$__MemoryEfficientTracepointBuffer.storeArray
+ OBJC_IVAR_$__OSLogEnumeratorCatalog._storeCatalogsAndSubchunks
+ OBJC_IVAR_$__OSLogIndexEnumerator._memEffic
+ OBJC_IVAR_$__OSLogLRUCache._lock
+ OBJC_IVAR_$__OSLogLRUCache._maxCount
+ OBJC_IVAR_$__OSLogLRUCache._mruItems
+ OBJC_IVAR_$__OSLogLRUCache._name
+ OBJC_IVAR_$__OSLogLRUCache._storage
+ OBJC_IVAR_$__OSLogLRUCache.evictionHandler
+ _OBJC_CLASS_$_CacheIndex
+ _OBJC_CLASS_$_CatalogsCache
+ _OBJC_CLASS_$_DataCache
+ _OBJC_CLASS_$_NSValue
+ _OBJC_CLASS_$_OSLogDoublyLinkedList
+ _OBJC_CLASS_$_OSLogDoublyLinkedListNode
+ _OBJC_CLASS_$_OversizeIndex
+ _OBJC_CLASS_$__BaseTracepointBuffer
+ _OBJC_CLASS_$__MemoryEfficientEnumeratorCatalogSubchunk
+ _OBJC_CLASS_$__MemoryEfficientTracepointBuffer
+ _OBJC_CLASS_$__OSLogLRUCache
+ _OBJC_METACLASS_$_CacheIndex
+ _OBJC_METACLASS_$_CatalogsCache
+ _OBJC_METACLASS_$_DataCache
+ _OBJC_METACLASS_$_OSLogDoublyLinkedList
+ _OBJC_METACLASS_$_OSLogDoublyLinkedListNode
+ _OBJC_METACLASS_$_OversizeIndex
+ _OBJC_METACLASS_$__BaseTracepointBuffer
+ _OBJC_METACLASS_$__MemoryEfficientEnumeratorCatalogSubchunk
+ _OBJC_METACLASS_$__MemoryEfficientTracepointBuffer
+ _OBJC_METACLASS_$__OSLogLRUCache
+ _OSLogEventUnpackChunk.3899
+ _OSLogEventUnpackChunk.4316
+ __130-[OSLogStatistics aggregationForStartDate_impl:endDate:predicate:withOptions:catalogCacheSize:dataCacheSize:useMemEffic:errorOut:]_block_invoke.171
+ __56-[_OSLogEnumeratorCatalog enumerateSubchunksUsingBlock:]_block_invoke.178
+ __Block_byref_object_copy_.2710
+ __Block_byref_object_copy_.2910
+ __Block_byref_object_copy_.3935
+ __Block_byref_object_copy_.4321
+ __Block_byref_object_copy_.919
+ __Block_byref_object_dispose_.2711
+ __Block_byref_object_dispose_.2911
+ __Block_byref_object_dispose_.3936
+ __Block_byref_object_dispose_.4322
+ __Block_byref_object_dispose_.920
+ __OBJC_$_INSTANCE_METHODS_CacheIndex
+ __OBJC_$_INSTANCE_METHODS_CatalogsCache
+ __OBJC_$_INSTANCE_METHODS_DataCache
+ __OBJC_$_INSTANCE_METHODS_OSLogDoublyLinkedList
+ __OBJC_$_INSTANCE_METHODS_OSLogDoublyLinkedListNode
+ __OBJC_$_INSTANCE_METHODS_OversizeIndex
+ __OBJC_$_INSTANCE_METHODS__BaseTracepointBuffer
+ __OBJC_$_INSTANCE_METHODS__MemoryEfficientEnumeratorCatalogSubchunk
+ __OBJC_$_INSTANCE_METHODS__MemoryEfficientTracepointBuffer
+ __OBJC_$_INSTANCE_METHODS__OSLogLRUCache
+ __OBJC_$_INSTANCE_VARIABLES_CacheIndex
+ __OBJC_$_INSTANCE_VARIABLES_CatalogsCache
+ __OBJC_$_INSTANCE_VARIABLES_DataCache
+ __OBJC_$_INSTANCE_VARIABLES_OSLogDoublyLinkedList
+ __OBJC_$_INSTANCE_VARIABLES_OSLogDoublyLinkedListNode
+ __OBJC_$_INSTANCE_VARIABLES_OversizeIndex
+ __OBJC_$_INSTANCE_VARIABLES__BaseTracepointBuffer
+ __OBJC_$_INSTANCE_VARIABLES__MemoryEfficientEnumeratorCatalogSubchunk
+ __OBJC_$_INSTANCE_VARIABLES__MemoryEfficientTracepointBuffer
+ __OBJC_$_INSTANCE_VARIABLES__OSLogLRUCache
+ __OBJC_$_PROP_LIST_CacheIndex
+ __OBJC_$_PROP_LIST_CatalogsCache
+ __OBJC_$_PROP_LIST_DataCache
+ __OBJC_$_PROP_LIST_OSLogDoublyLinkedList
+ __OBJC_$_PROP_LIST_OSLogDoublyLinkedListNode
+ __OBJC_$_PROP_LIST_OversizeIndex
+ __OBJC_$_PROP_LIST__BaseTracepointBuffer
+ __OBJC_$_PROP_LIST__MemoryEfficientEnumeratorCatalogSubchunk
+ __OBJC_$_PROP_LIST__OSLogCache
+ __OBJC_$_PROP_LIST__OSLogLRUCache
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CatalogsCache
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_DataCache
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_EnumeratorCatalogSubchunk
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__OSLogCache
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CatalogsCache
+ __OBJC_$_PROTOCOL_METHOD_TYPES_DataCache
+ __OBJC_$_PROTOCOL_METHOD_TYPES_EnumeratorCatalogSubchunk
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying
+ __OBJC_$_PROTOCOL_METHOD_TYPES__OSLogCache
+ __OBJC_$_PROTOCOL_REFS_CatalogsCache
+ __OBJC_$_PROTOCOL_REFS_DataCache
+ __OBJC_$_PROTOCOL_REFS_EnumeratorCatalogSubchunk
+ __OBJC_$_PROTOCOL_REFS__OSLogCache
+ __OBJC_CLASS_PROTOCOLS_$_CacheIndex
+ __OBJC_CLASS_PROTOCOLS_$_CatalogsCache
+ __OBJC_CLASS_PROTOCOLS_$_DataCache
+ __OBJC_CLASS_PROTOCOLS_$__MemoryEfficientEnumeratorCatalogSubchunk
+ __OBJC_CLASS_PROTOCOLS_$__OSLogLRUCache
+ __OBJC_CLASS_RO_$_CacheIndex
+ __OBJC_CLASS_RO_$_CatalogsCache
+ __OBJC_CLASS_RO_$_DataCache
+ __OBJC_CLASS_RO_$_OSLogDoublyLinkedList
+ __OBJC_CLASS_RO_$_OSLogDoublyLinkedListNode
+ __OBJC_CLASS_RO_$_OversizeIndex
+ __OBJC_CLASS_RO_$__BaseTracepointBuffer
+ __OBJC_CLASS_RO_$__MemoryEfficientEnumeratorCatalogSubchunk
+ __OBJC_CLASS_RO_$__MemoryEfficientTracepointBuffer
+ __OBJC_CLASS_RO_$__OSLogLRUCache
+ __OBJC_LABEL_PROTOCOL_$_CatalogsCache
+ __OBJC_LABEL_PROTOCOL_$_DataCache
+ __OBJC_LABEL_PROTOCOL_$_EnumeratorCatalogSubchunk
+ __OBJC_LABEL_PROTOCOL_$_NSCopying
+ __OBJC_LABEL_PROTOCOL_$__OSLogCache
+ __OBJC_METACLASS_RO_$_CacheIndex
+ __OBJC_METACLASS_RO_$_CatalogsCache
+ __OBJC_METACLASS_RO_$_DataCache
+ __OBJC_METACLASS_RO_$_OSLogDoublyLinkedList
+ __OBJC_METACLASS_RO_$_OSLogDoublyLinkedListNode
+ __OBJC_METACLASS_RO_$_OversizeIndex
+ __OBJC_METACLASS_RO_$__BaseTracepointBuffer
+ __OBJC_METACLASS_RO_$__MemoryEfficientEnumeratorCatalogSubchunk
+ __OBJC_METACLASS_RO_$__MemoryEfficientTracepointBuffer
+ __OBJC_METACLASS_RO_$__OSLogLRUCache
+ __OBJC_PROTOCOL_$_CatalogsCache
+ __OBJC_PROTOCOL_$_DataCache
+ __OBJC_PROTOCOL_$_EnumeratorCatalogSubchunk
+ __OBJC_PROTOCOL_$_NSCopying
+ __OBJC_PROTOCOL_$__OSLogCache
+ __OTRCreateActivityStreamForPID_block_invoke.69
+ __OTRStartLegacyStreaming_block_invoke.75
+ __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB8nn190102EPKvm
+ __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8nn190102ERKS6_S9_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8nn190102ILi0EEEPKc
+ __ZSt28__throw_bad_array_new_lengthB8nn190102v
+ ___101-[_MemoryEfficientTracepointBuffer insertTracepoints:chunkOffset:chunkSetStartAddr:subchunk:options:]_block_invoke
+ ___108-[_OSLogIndex enumerateEntriesInRange:options:usingCatalogFilter:catalogCacheSize:dataCacheSize:usingBlock:]_block_invoke
+ ___108-[_OSLogIndex enumerateEntriesInRange:options:usingCatalogFilter:catalogCacheSize:dataCacheSize:usingBlock:]_block_invoke_2
+ ___130-[OSLogStatistics aggregationForStartDate_impl:endDate:predicate:withOptions:catalogCacheSize:dataCacheSize:useMemEffic:errorOut:]_block_invoke
+ ___34-[DataCache init:evictionHandler:]_block_invoke
+ ___38-[CatalogsCache init:evictionHandler:]_block_invoke
+ ___55-[_MemoryEfficientTracepointBuffer init:dataCacheSize:]_block_invoke
+ ___55-[_MemoryEfficientTracepointBuffer init:dataCacheSize:]_block_invoke_2
+ ___56-[_MemoryEfficientTracepointBuffer setupStoresForIndex:]_block_invoke
+ ___68-[_MemoryEfficientTracepointBuffer iterateChunksAndFillEvent:block:]_block_invoke
+ ___68-[_MemoryEfficientTracepointBuffer iterateChunksAndFillEvent:block:]_block_invoke_2
+ ___71-[_MemoryEfficientEnumeratorCatalogSubchunk enumerateChunksUsingBlock:]_block_invoke
+ ___71-[_MemoryEfficientEnumeratorCatalogSubchunk enumerateChunksUsingBlock:]_block_invoke_2
+ ___75-[_BaseTracepointBuffer insertTimesyncPoints:forBoot:oldestContinuousTime:]_block_invoke
+ ___79-[_BaseTracepointBuffer finishedInsertingTracepointsWithNextMajorTime:options:]_block_invoke
+ ___86-[OSLogEventStream _activateStreamInRange:useMemEffic:catalogCacheSize:dataCacheSize:]_block_invoke
+ ___86-[_MemoryEfficientTracepointBuffer insertTimesyncPoints:forBoot:oldestContinuousTime:]_block_invoke
+ ___90-[_BaseTracepointBuffer insertTracepoints:chunkOffset:chunkSetStartAddr:subchunk:options:]_block_invoke
+ ___90-[_MemoryEfficientTracepointBuffer finishedInsertingTracepointsWithNextMajorTime:options:]_block_invoke
+ ___94-[OSLogEventStream _activateStreamFromDate:toDate:useMemEffic:catalogCacheSize:dataCacheSize:]_block_invoke
+ ___OversizeHelper_block_invoke
+ ___OversizeHelper_block_invoke_2
+ ___TPChunkHelper_block_invoke
+ ___TPChunkHelper_block_invoke_2
+ ___block_descriptor_120_e8_32s40s_e69_v16?0^{firehose_tracepoint_s=(?={?=CCSI}QAQ)Q(?={?=b48b16}QAQ)[0C]}8l
+ ___block_descriptor_122_e8_32s40s48s56s64s72r80r88r96r104r112r_e782_B32?0^{tracev3_chunk_s={tracev3_chunk_preamble_s=IIQ}(?={tracev3_chunk_header_s={mach_timebase_info=II}QqiiiI{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_continuous_s=Q}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_systeminfo_s=ii[16c][32c]}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_generation_s=[16C]ii}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_timezone_s=[48c]}}{tracev3_chunk_catalog_s=SSSS[0C]}{tracev3_chunk_catalog_v2_s=SSSSS[3S]Q[0C]}{tracev3_chunk_log_preamble_s=QIC[3C]}{tracev3_chunk_firehose_s=QICC[2C][0C]}{tracev3_chunk_firehose_old_s=QiCC[0C]}{tracev3_chunk_oversize_s=QIC[3C]QISS[0C]}{tracev3_chunk_oversize_old_s=QISS[0C]}{tracev3_chunk_statedump_s=QIC[3C]QQ[16C][0C]}{tracev3_chunk_simple_s=QICC[2C]QQQ[16C][16C][0C]}[0C])}8{_NSRange=QQ}16l
+ ___block_descriptor_136_e8_32s40s_e69_v16?0^{firehose_tracepoint_s=(?={?=CCSI}QAQ)Q(?={?=b48b16}QAQ)[0C]}8l
+ ___block_descriptor_32_e173_v28?0S8q12^{catalog_s={catalog_hdr_s=SQ}^{os_trace_uuid_map_s}^{os_trace_str_map_s}Q^{os_procinfo_map_s}QQ{subchunk_queue_t=^{catalog_subchunk_s}^^{catalog_subchunk_s}}Q}20l
+ ___block_descriptor_32_e17_v32?0S8q12I20*24l
+ ___block_descriptor_40_e164_^{catalog_s={catalog_hdr_s=SQ}^{os_trace_uuid_map_s}^{os_trace_str_map_s}Q^{os_procinfo_map_s}QQ{subchunk_queue_t=^{catalog_subchunk_s}^^{catalog_subchunk_s}}Q}8?0l
+ ___block_descriptor_40_e8_32bs_e11_v24?0816l
+ ___block_descriptor_40_e8_32s_e25_v16?0"_OSLogIndexFile"8l
+ ___block_descriptor_40_e8_32s_e37_B16?0"<EnumeratorCatalogSubchunk>"8l
+ ___block_descriptor_48_e13_*24?0^Q8^I16l
+ ___block_descriptor_48_e39_B16?0"_OSLogEnumeratorOversizeChunk"8lu32l8
+ ___block_descriptor_64_e8_32s40s48bs_e330_B24?0^{_range_context_s=Q{mach_timebase_info=II}}8^{?=IQSqq(?={?=^{tracev3_chunk_s}^{catalog_s}{_OSLogEventChunkContext=^{tracev3_chunk_s}^{_firehose_unaligned_chunk_s}{iovec=^vQ}^{catalog_procinfo_s}}^{_firehose_unaligned_tracepoint_s}}{?=[16C]{os_timesync_time_entry_s={os_timesync_header_s=SSI}QQ{timezone=ii}}}{?=[16C]CB})}16lu56l8
+ ___block_descriptor_65_e8_32s40s48s_e5_v8?0l
+ ___block_descriptor_72_e8_32s40s48r_e767_B16?0^{tracev3_chunk_s={tracev3_chunk_preamble_s=IIQ}(?={tracev3_chunk_header_s={mach_timebase_info=II}QqiiiI{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_continuous_s=Q}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_systeminfo_s=ii[16c][32c]}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_generation_s=[16C]ii}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_timezone_s=[48c]}}{tracev3_chunk_catalog_s=SSSS[0C]}{tracev3_chunk_catalog_v2_s=SSSSS[3S]Q[0C]}{tracev3_chunk_log_preamble_s=QIC[3C]}{tracev3_chunk_firehose_s=QICC[2C][0C]}{tracev3_chunk_firehose_old_s=QiCC[0C]}{tracev3_chunk_oversize_s=QIC[3C]QISS[0C]}{tracev3_chunk_oversize_old_s=QISS[0C]}{tracev3_chunk_statedump_s=QIC[3C]QQ[16C][0C]}{tracev3_chunk_simple_s=QICC[2C]QQQ[16C][16C][0C]}[0C])}8l
+ ___block_descriptor_88_e8_32bs40r48r_e767_B16?0^{tracev3_chunk_s={tracev3_chunk_preamble_s=IIQ}(?={tracev3_chunk_header_s={mach_timebase_info=II}QqiiiI{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_continuous_s=Q}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_systeminfo_s=ii[16c][32c]}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_generation_s=[16C]ii}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_timezone_s=[48c]}}{tracev3_chunk_catalog_s=SSSS[0C]}{tracev3_chunk_catalog_v2_s=SSSSS[3S]Q[0C]}{tracev3_chunk_log_preamble_s=QIC[3C]}{tracev3_chunk_firehose_s=QICC[2C][0C]}{tracev3_chunk_firehose_old_s=QiCC[0C]}{tracev3_chunk_oversize_s=QIC[3C]QISS[0C]}{tracev3_chunk_oversize_old_s=QISS[0C]}{tracev3_chunk_statedump_s=QIC[3C]QQ[16C][0C]}{tracev3_chunk_simple_s=QICC[2C]QQQ[16C][16C][0C]}[0C])}8l
+ ___block_descriptor_90_e8_32s40bs48r56r64r72r_e782_B32?0^{tracev3_chunk_s={tracev3_chunk_preamble_s=IIQ}(?={tracev3_chunk_header_s={mach_timebase_info=II}QqiiiI{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_continuous_s=Q}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_systeminfo_s=ii[16c][32c]}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_generation_s=[16C]ii}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_timezone_s=[48c]}}{tracev3_chunk_catalog_s=SSSS[0C]}{tracev3_chunk_catalog_v2_s=SSSSS[3S]Q[0C]}{tracev3_chunk_log_preamble_s=QIC[3C]}{tracev3_chunk_firehose_s=QICC[2C][0C]}{tracev3_chunk_firehose_old_s=QiCC[0C]}{tracev3_chunk_oversize_s=QIC[3C]QISS[0C]}{tracev3_chunk_oversize_old_s=QISS[0C]}{tracev3_chunk_statedump_s=QIC[3C]QQ[16C][0C]}{tracev3_chunk_simple_s=QICC[2C]QQQ[16C][16C][0C]}[0C])}8{_NSRange=QQ}16l
+ ___copy_helper_block_e8_32b40r48r
+ ___copy_helper_block_e8_32s40b48r56r64r72r
+ ___copy_helper_block_e8_32s40s48b
+ ___copy_helper_block_e8_32s40s48s56s64s72r80r88r96r104r112r
+ ___destroy_helper_block_e8_32s40s48r56r64r72r
+ ___destroy_helper_block_e8_32s40s48s56s64s72r80r88r96r104r112r
+ ___findOversizeAndFill_block_invoke
+ ___findOversizeAndFill_block_invoke_2
+ ___os_activity_stream_resume_with_filter_block_invoke.42
+ __block_descriptor_tmp.1179
+ __block_descriptor_tmp.20.994
+ __block_descriptor_tmp.23
+ __block_descriptor_tmp.2486
+ __block_descriptor_tmp.3025
+ __block_descriptor_tmp.3298
+ __block_descriptor_tmp.4.3305
+ __block_descriptor_tmp.44
+ __block_descriptor_tmp.49
+ __block_descriptor_tmp.66
+ __block_descriptor_tmp.68
+ __block_descriptor_tmp.72
+ __block_descriptor_tmp.74
+ __block_descriptor_tmp.78.3317
+ __block_descriptor_tmp.86.3306
+ __block_descriptor_tmp.996
+ __block_literal_global.1177
+ __block_literal_global.1554
+ __block_literal_global.2104
+ __block_literal_global.213
+ __block_literal_global.2211
+ __block_literal_global.238
+ __block_literal_global.2605
+ __block_literal_global.277
+ __block_literal_global.2798
+ __block_literal_global.3260
+ __block_literal_global.3266
+ __block_literal_global.363
+ __block_literal_global.369
+ __block_literal_global.4175
+ __block_literal_global.4350
+ __block_literal_global.564
+ __block_literal_global.63
+ __block_literal_global.734
+ __block_literal_global.9.1555
+ __block_literal_global.969
+ __block_literal_global.977
+ __compact_logarchive_block_invoke.95
+ __enumerateAndDecompressSubchunk_block_invoke.3445
+ __os_crash_msg
+ __os_log_send_and_compose_impl
+ __timesync_enumerate_boot
+ _objc_msgSend$_activateStreamFromDate:toDate:useMemEffic:catalogCacheSize:dataCacheSize:
+ _objc_msgSend$_activateStreamInRange:useMemEffic:catalogCacheSize:dataCacheSize:
+ _objc_msgSend$activateStreamFromDate:catalogCacheSize:dataCacheSize:
+ _objc_msgSend$addTSEntry:
+ _objc_msgSend$addToTail:
+ _objc_msgSend$advanceCursorToTime:
+ _objc_msgSend$aggregationForStartDate_impl:endDate:predicate:withOptions:catalogCacheSize:dataCacheSize:useMemEffic:errorOut:
+ _objc_msgSend$allocWithZone:
+ _objc_msgSend$allocateRow
+ _objc_msgSend$bufferHasFreeSpace
+ _objc_msgSend$cache
+ _objc_msgSend$canMutate
+ _objc_msgSend$catalogForCDHash:identifier:generator:
+ _objc_msgSend$catalog_offset
+ _objc_msgSend$chunkRange
+ _objc_msgSend$chunk_offset
+ _objc_msgSend$consolidate
+ _objc_msgSend$cursor
+ _objc_msgSend$dataForCDHash:identifier:size:generator:
+ _objc_msgSend$decompressedBufferForChunk:
+ _objc_msgSend$dictionaryWithCapacity:
+ _objc_msgSend$enumerateEntriesInRange:options:usingCatalogFilter:catalogCacheSize:dataCacheSize:usingBlock:
+ _objc_msgSend$evictAllEntries
+ _objc_msgSend$evictionHandler
+ _objc_msgSend$fileIndex
+ _objc_msgSend$findOversize:process:oversize_id:pidversion:timestamp:block:
+ _objc_msgSend$getBootUUIDIndex:
+ _objc_msgSend$getFileNameAt:
+ _objc_msgSend$growBuffer:
+ _objc_msgSend$growBufferImmediatelyIfNeeded
+ _objc_msgSend$hash64
+ _objc_msgSend$head
+ _objc_msgSend$indexOfUUID:
+ _objc_msgSend$init:dataCacheSize:
+ _objc_msgSend$init:evictionHandler:
+ _objc_msgSend$init:msgID:pidV:timestamp:
+ _objc_msgSend$initWithCDHash:identifier:
+ _objc_msgSend$initWithIndex:metadata:fileBootList:catalogFilter:options:catalogCacheSize:dataCacehSize:
+ _objc_msgSend$initWithKey:data:
+ _objc_msgSend$initWithName:maxCount:evictionHandler:
+ _objc_msgSend$initWithStore:index:fileHeader:range:chunk:storeCatalogsAndSubchunks:
+ _objc_msgSend$insertOversizedChunk:chunkOffset:chunkSetStartAddr:subchunk:chunkList:
+ _objc_msgSend$insertValuesIntoIndex:coffset:fileName:sortKey:type:
+ _objc_msgSend$isEqualToCacheIndex:
+ _objc_msgSend$iterateChunksAndFillEvent:block:
+ _objc_msgSend$key
+ _objc_msgSend$keysSortedByValueUsingSelector:
+ _objc_msgSend$maxCount
+ _objc_msgSend$mruItems
+ _objc_msgSend$next
+ _objc_msgSend$numberWithUnsignedShort:
+ _objc_msgSend$pointerValue
+ _objc_msgSend$prev
+ _objc_msgSend$removeFromHead
+ _objc_msgSend$removeNodeAndAddToTail:
+ _objc_msgSend$retireOversize:
+ _objc_msgSend$setCanMutate:
+ _objc_msgSend$setCatalog_offset:
+ _objc_msgSend$setChunk_offset:
+ _objc_msgSend$setCount:
+ _objc_msgSend$setCursor:
+ _objc_msgSend$setData:
+ _objc_msgSend$setFileIndex:
+ _objc_msgSend$setHead:
+ _objc_msgSend$setKey:
+ _objc_msgSend$setNext:
+ _objc_msgSend$setPrev:
+ _objc_msgSend$setSize:
+ _objc_msgSend$setTail:
+ _objc_msgSend$setTp_offset:
+ _objc_msgSend$setupStoresForIndex:
+ _objc_msgSend$storage
+ _objc_msgSend$tail
+ _objc_msgSend$tp_offset
+ _objc_msgSend$valueWithPointer:
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _size_for_stream_message
+ enumerateAndDecompressSubchunk.3444
- -[OSLogEventStream _activateStreamFromDate:toDate:]
- -[OSLogEventStream _activateStreamInRange:]
- -[_OSLogEnumeratorCatalog initWithStore:index:fileHeader:range:chunk:]
- -[_OSLogEnumeratorCatalogSubchunk _decompressedBufferForChunk:subchunk:]
- -[_OSLogEnumeratorCatalogSubchunk endTimeCompare:]
- -[_OSLogEnumeratorCatalogSubchunk oldestTimeCompare:]
- -[_OSLogIndex enumerateEntriesInRange:options:usingCatalogFilter:usingBlock:]
- -[_OSLogIndexEnumerator initWithIndex:metadata:fileBootList:catalogFilter:]
- -[_OSLogTracepointBuffer .cxx_destruct]
- -[_OSLogTracepointBuffer _isEmpty]
- -[_OSLogTracepointBuffer beginInsertingTracepointsClippingFromTime:]
- -[_OSLogTracepointBuffer dealloc]
- -[_OSLogTracepointBuffer enumerateEventsFromTime:to:options:usingBlock:]
- -[_OSLogTracepointBuffer fileNames]
- -[_OSLogTracepointBuffer finishedInsertingTracepointsWithNextMajorTime:options:]
- -[_OSLogTracepointBuffer init]
- -[_OSLogTracepointBuffer insertChunk:chunkOffset:chunkSetStartAddr:timestamp:subchunk:]
- -[_OSLogTracepointBuffer insertNonsparsePoint:uuid:ttl:inMemory:]
- -[_OSLogTracepointBuffer insertSimpleChunk:chunkOffset:chunkSetStartAddr:subchunk:options:]
- -[_OSLogTracepointBuffer insertStatedumpChunk:chunkOffset:chunkSetStartAddr:subchunk:]
- -[_OSLogTracepointBuffer insertTimesyncPoints:forBoot:oldestContinuousTime:]
- -[_OSLogTracepointBuffer insertTracepoints:chunkOffset:chunkSetStartAddr:subchunk:options:]
- GCC_except_table1002
- GCC_except_table1010
- GCC_except_table1017
- GCC_except_table1031
- GCC_except_table1034
- GCC_except_table1035
- GCC_except_table1036
- GCC_except_table1037
- GCC_except_table1047
- GCC_except_table1201
- GCC_except_table1243
- GCC_except_table1283
- GCC_except_table1399
- GCC_except_table1419
- GCC_except_table1424
- GCC_except_table1426
- GCC_except_table358
- GCC_except_table363
- GCC_except_table409
- GCC_except_table481
- GCC_except_table559
- GCC_except_table585
- GCC_except_table660
- GCC_except_table668
- GCC_except_table674
- GCC_except_table677
- GCC_except_table727
- GCC_except_table879
- GCC_except_table880
- GCC_except_table900
- GCC_except_table906
- GCC_except_table916
- GCC_except_table919
- GCC_except_table995
- OBJC_IVAR_$__OSLogTracepointBuffer._count
- OBJC_IVAR_$__OSLogTracepointBuffer._cursor
- OBJC_IVAR_$__OSLogTracepointBuffer._events
- OBJC_IVAR_$__OSLogTracepointBuffer._fileNames
- OBJC_IVAR_$__OSLogTracepointBuffer._mutable
- OBJC_IVAR_$__OSLogTracepointBuffer._size
- _OBJC_CLASS_$__OSLogTracepointBuffer
- _OBJC_METACLASS_$__OSLogTracepointBuffer
- _OSLogEventUnpackChunk.3127
- __56-[_OSLogEnumeratorCatalog enumerateSubchunksUsingBlock:]_block_invoke.223
- __82-[OSLogStatistics aggregationForStartDate:endDate:predicate:withOptions:errorOut:]_block_invoke.171
- __Block_byref_object_copy_.2094
- __Block_byref_object_copy_.2289
- __Block_byref_object_copy_.3163
- __Block_byref_object_copy_.838
- __Block_byref_object_dispose_.2095
- __Block_byref_object_dispose_.2290
- __Block_byref_object_dispose_.3164
- __Block_byref_object_dispose_.839
- __OBJC_$_INSTANCE_METHODS__OSLogTracepointBuffer
- __OBJC_$_INSTANCE_VARIABLES__OSLogTracepointBuffer
- __OBJC_$_PROP_LIST__OSLogTracepointBuffer
- __OBJC_CLASS_RO_$__OSLogTracepointBuffer
- __OBJC_METACLASS_RO_$__OSLogTracepointBuffer
- __OTRCreateActivityStreamForPID_block_invoke.66
- __OTRStartLegacyStreaming_block_invoke.72
- __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB8nn180100EPKvm
- __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8nn180100ERKS6_S9_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8nn180100ILi0EEEPKc
- __ZSt28__throw_bad_array_new_lengthB8nn180100v
- ___43-[OSLogEventStream _activateStreamInRange:]_block_invoke
- ___51-[OSLogEventStream _activateStreamFromDate:toDate:]_block_invoke
- ___76-[_OSLogTracepointBuffer insertTimesyncPoints:forBoot:oldestContinuousTime:]_block_invoke
- ___77-[_OSLogIndex enumerateEntriesInRange:options:usingCatalogFilter:usingBlock:]_block_invoke
- ___80-[_OSLogTracepointBuffer finishedInsertingTracepointsWithNextMajorTime:options:]_block_invoke
- ___82-[OSLogStatistics aggregationForStartDate:endDate:predicate:withOptions:errorOut:]_block_invoke
- ____os_activity_stream_resume_with_filter_block_invoke_2
- ___block_descriptor_40_e8_32s_e41_B16?0"_OSLogEnumeratorCatalogSubchunk"8l
- ___block_descriptor_56_e8_32s40bs_e330_B24?0^{_range_context_s=Q{mach_timebase_info=II}}8^{?=IQSqq(?={?=^{tracev3_chunk_s}^{catalog_s}{_OSLogEventChunkContext=^{tracev3_chunk_s}^{_firehose_unaligned_chunk_s}{iovec=^vQ}^{catalog_procinfo_s}}^{_firehose_unaligned_tracepoint_s}}{?=[16C]{os_timesync_time_entry_s={os_timesync_header_s=SSI}QQ{timezone=ii}}}{?=[16C]CB})}16lu48l8
- ___block_descriptor_56_e8_32s40s48s_e5_v8?0l
- __block_descriptor_tmp.1091
- __block_descriptor_tmp.1890
- __block_descriptor_tmp.21
- __block_descriptor_tmp.23.912
- __block_descriptor_tmp.2393
- __block_descriptor_tmp.2655
- __block_descriptor_tmp.4.2662
- __block_descriptor_tmp.43
- __block_descriptor_tmp.48
- __block_descriptor_tmp.64
- __block_descriptor_tmp.65
- __block_descriptor_tmp.69
- __block_descriptor_tmp.71.2673
- __block_descriptor_tmp.75
- __block_descriptor_tmp.83
- __block_descriptor_tmp.914
- __block_literal_global.1089
- __block_literal_global.1343
- __block_literal_global.1616
- __block_literal_global.1712
- __block_literal_global.2005
- __block_literal_global.214
- __block_literal_global.2184
- __block_literal_global.234
- __block_literal_global.2620
- __block_literal_global.2626
- __block_literal_global.275
- __block_literal_global.3403
- __block_literal_global.360
- __block_literal_global.445
- __block_literal_global.584
- __block_literal_global.670
- __block_literal_global.886
- __block_literal_global.895
- __block_literal_global.9.1344
- __compact_logarchive_block_invoke.92
- __oltb_allocate_row
- __oltb_consolidate
- _objc_msgSend$_activateStreamFromDate:toDate:
- _objc_msgSend$_activateStreamInRange:
- _objc_msgSend$_decompressedBufferForChunk:subchunk:
- _objc_msgSend$enumerateEntriesInRange:options:usingCatalogFilter:usingBlock:
- _objc_msgSend$initWithIndex:metadata:fileBootList:catalogFilter:
- _objc_msgSend$initWithStore:index:fileHeader:range:chunk:
CStrings:
+ "*24@?0^Q8^I16"
+ "*44@0:8S16q20^Q28@?36"
+ "*44@0:8S16q20^Q28@?<*@?^Q^I>36"
+ "2`"
+ "@"
+ "@\"<EnumeratorCatalogSubchunk>\""
+ "@\"<_OSLogCache>\""
+ "@\"CatalogsCache\""
+ "@\"DataCache\""
+ "@\"OSLogDoublyLinkedList\""
+ "@\"OSLogDoublyLinkedListNode\""
+ "@\"_BaseTracepointBuffer\""
+ "@\"_OSLogChunkBuffer\"24@0:8^{tracev3_chunk_s={tracev3_chunk_preamble_s=IIQ}(?={tracev3_chunk_header_s={mach_timebase_info=II}QqiiiI{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_continuous_s=Q}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_systeminfo_s=ii[16c][32c]}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_generation_s=[16C]ii}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_timezone_s=[48c]}}{tracev3_chunk_catalog_s=SSSS[0C]}{tracev3_chunk_catalog_v2_s=SSSSS[3S]Q[0C]}{tracev3_chunk_log_preamble_s=QIC[3C]}{tracev3_chunk_firehose_s=QICC[2C][0C]}{tracev3_chunk_firehose_old_s=QiCC[0C]}{tracev3_chunk_oversize_s=QIC[3C]QISS[0C]}{tracev3_chunk_oversize_old_s=QISS[0C]}{tracev3_chunk_statedump_s=QIC[3C]QQ[16C][0C]}{tracev3_chunk_simple_s=QICC[2C]QQQ[16C][16C][0C]}[0C])}16"
+ "@20@0:8S16"
+ "@24@0:8I16I20"
+ "@24@0:8^{_NSZone=}16"
+ "@24@0:8^{tracev3_chunk_s={tracev3_chunk_preamble_s=IIQ}(?={tracev3_chunk_header_s={mach_timebase_info=II}QqiiiI{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_continuous_s=Q}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_systeminfo_s=ii[16c][32c]}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_generation_s=[16C]ii}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_timezone_s=[48c]}}{tracev3_chunk_catalog_s=SSSS[0C]}{tracev3_chunk_catalog_v2_s=SSSSS[3S]Q[0C]}{tracev3_chunk_log_preamble_s=QIC[3C]}{tracev3_chunk_firehose_s=QICC[2C][0C]}{tracev3_chunk_firehose_old_s=QiCC[0C]}{tracev3_chunk_oversize_s=QIC[3C]QISS[0C]}{tracev3_chunk_oversize_old_s=QISS[0C]}{tracev3_chunk_statedump_s=QIC[3C]QQ[16C][0C]}{tracev3_chunk_simple_s=QICC[2C]QQQ[16C][16C][0C]}[0C])}16"
+ "@28@0:8I16@?20"
+ "@28@0:8I16@?<v@?SqI*>20"
+ "@28@0:8I16@?<v@?Sq^{catalog_s={catalog_hdr_s=SQ}^{os_trace_uuid_map_s}^{os_trace_str_map_s}Q^{os_procinfo_map_s}QQ{subchunk_queue_t=^{catalog_subchunk_s}^^{catalog_subchunk_s}}Q}>20"
+ "@28@0:8S16q20"
+ "@40@0:8@16Q24@?32"
+ "@40@0:8Q16I24I28Q32"
+ "@48@0:8@\"_OSLogEnumeratorCatalog\"16^{catalog_subchunk_s={?=^{catalog_subchunk_s}^^{catalog_subchunk_s}}QQII^{hashtable}^{hashtable}}24{_NSRange=QQ}32"
+ "@60@0:8@16^{?={_os_log_index_timeref=[16C]Q}{_os_log_index_timeref=[16C]Q}{_os_log_index_timeref=[16C]Q}{_os_log_index_timeref=[16C]Q}{_os_log_index_timeref=[16C]Q}{_os_log_index_timeref=[16C]Q}^{_os_log_index_timeref}[5{?={_os_log_index_timeref=[16C]Q}C}]}24@32@40I48I52I56"
+ "@64@0:8@\"_OSLogEnumeratorCatalog\"16^{catalog_subchunk_s={?=^{catalog_subchunk_s}^^{catalog_subchunk_s}}QQII^{hashtable}^{hashtable}}24{_NSRange=QQ}32Q48Q56"
+ "@64@0:8@16@24@32Q40I48I52^@56"
+ "@68@0:8@16@24@32Q40I48I52B56^@60"
+ "@68@0:8@16@24^{tracev3_chunk_s={tracev3_chunk_preamble_s=IIQ}(?={tracev3_chunk_header_s={mach_timebase_info=II}QqiiiI{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_continuous_s=Q}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_systeminfo_s=ii[16c][32c]}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_generation_s=[16C]ii}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_timezone_s=[48c]}}{tracev3_chunk_catalog_s=SSSS[0C]}{tracev3_chunk_catalog_v2_s=SSSSS[3S]Q[0C]}{tracev3_chunk_log_preamble_s=QIC[3C]}{tracev3_chunk_firehose_s=QICC[2C][0C]}{tracev3_chunk_firehose_old_s=QiCC[0C]}{tracev3_chunk_oversize_s=QIC[3C]QISS[0C]}{tracev3_chunk_oversize_old_s=QISS[0C]}{tracev3_chunk_statedump_s=QIC[3C]QQ[16C][0C]}{tracev3_chunk_simple_s=QICC[2C]QQQ[16C][16C][0C]}[0C])}32{_NSRange=QQ}40^{tracev3_chunk_s={tracev3_chunk_preamble_s=IIQ}(?={tracev3_chunk_header_s={mach_timebase_info=II}QqiiiI{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_continuous_s=Q}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_systeminfo_s=ii[16c][32c]}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_generation_s=[16C]ii}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_timezone_s=[48c]}}{tracev3_chunk_catalog_s=SSSS[0C]}{tracev3_chunk_catalog_v2_s=SSSSS[3S]Q[0C]}{tracev3_chunk_log_preamble_s=QIC[3C]}{tracev3_chunk_firehose_s=QICC[2C][0C]}{tracev3_chunk_firehose_old_s=QiCC[0C]}{tracev3_chunk_oversize_s=QIC[3C]QISS[0C]}{tracev3_chunk_oversize_old_s=QISS[0C]}{tracev3_chunk_statedump_s=QIC[3C]QQ[16C][0C]}{tracev3_chunk_simple_s=QICC[2C]QQQ[16C][16C][0C]}[0C])}56B64"
+ "@?<v@?@@>16@0:8"
+ "B16@?0@\"<EnumeratorCatalogSubchunk>\"8"
+ "B16@?0@\"_OSLogEnumeratorOversizeChunk\"8"
+ "B32@0:8^{tp_element=SqqQC(?={?=qQQ}{?=SCB}{?=Si})}16@?24"
+ "B56@0:8@16Q24I32I36Q40@?48"
+ "BUG IN LIBTRACE: BUG IN LOGGINGSUPPORT: Wrong type of CatalogSubchunk"
+ "BUG IN LIBTRACE: CatalogsCache EvictionHandler was given a bad key!"
+ "BUG IN LIBTRACE: CatalogsCache EvictionHandler was given a bad value!"
+ "BUG IN LIBTRACE: DataCache EvictionHandler was given a bad key!"
+ "BUG IN LIBTRACE: DataCache EvictionHandler was given a bad value!"
+ "BUG IN LIBTRACE: OVERFLOW OF UUID INDEXES"
+ "BUG IN LIBTRACE: _BaseTracepointBuffer table overflow"
+ "BUG IN LIBTRACE: oltb manipulation while immutable"
+ "BUG IN LIBTRACE: unsupported chunk found in TPChunkHelper"
+ "CacheIndex"
+ "CatalogsCache"
+ "DataCache"
+ "EnumeratorCatalogSubchunk"
+ "NSCopying"
+ "OSLogDoublyLinkedList"
+ "OSLogDoublyLinkedListNode"
+ "OversizeIndex"
+ "Q24@0:8^{os_trace_uuid_map_s=}16"
+ "Q48@0:8{os_timesync_time_entry_s={os_timesync_header_s=SSI}QQ{timezone=ii}}16"
+ "S24@0:8[16C]16"
+ "T@\"<_OSLogCache>\",R,N,V_cache"
+ "T@\"NSMutableDictionary\",R,N,V_storage"
+ "T@\"NSMutableOrderedSet\",&,N,V_fileNames"
+ "T@\"NSUUID\",R,N,V_buuid"
+ "T@\"OSLogDoublyLinkedList\",R,N,V_mruItems"
+ "T@\"OSLogDoublyLinkedListNode\",&,N,V_next"
+ "T@\"OSLogDoublyLinkedListNode\",&,N,Vhead"
+ "T@\"OSLogDoublyLinkedListNode\",&,N,Vtail"
+ "T@\"OSLogDoublyLinkedListNode\",W,N,V_prev"
+ "T@\"_BaseTracepointBuffer\",R,N,V_tracepoints"
+ "T@,&,N,V_data"
+ "T@,&,N,V_key"
+ "T@?,C,N"
+ "T@?,C,N,VevictionHandler"
+ "TB,N,V_canMutate"
+ "TB,R,N,V_storeCatalogsAndSubchunks"
+ "TI,N,V_msgID"
+ "TI,N,V_pidversion"
+ "TI,R,N,V_algo"
+ "TI,R,N,V_usize"
+ "TQ,N,V_count"
+ "TQ,N,V_cursor"
+ "TQ,N,V_processID"
+ "TQ,N,V_size"
+ "TQ,N,V_timestamp"
+ "TQ,R,N,V_maxCount"
+ "TS,N,V_fileIndex"
+ "TS,R,N,V_fileIndex"
+ "Tq,N,V_catalog_offset"
+ "Tq,N,V_chunk_offset"
+ "Tq,N,V_tp_offset"
+ "Tq,R,N,V_catalog_offset"
+ "Tq,R,N,V_chunk_offset"
+ "T{_NSRange=QQ},N,V_chunkRange"
+ "Warning: chunk with chunkset_start_addr and id: %p, %@ had a bad preamble!"
+ "^{catalog_s={catalog_hdr_s=SQ}^{os_trace_uuid_map_s}^{os_trace_str_map_s}Q^{os_procinfo_map_s}QQ{subchunk_queue_t=^{catalog_subchunk_s}^^{catalog_subchunk_s}}Q}36@0:8S16q20@?28"
+ "^{catalog_s={catalog_hdr_s=SQ}^{os_trace_uuid_map_s}^{os_trace_str_map_s}Q^{os_procinfo_map_s}QQ{subchunk_queue_t=^{catalog_subchunk_s}^^{catalog_subchunk_s}}Q}36@0:8S16q20@?<^{catalog_s={catalog_hdr_s=SQ}^{os_trace_uuid_map_s}^{os_trace_str_map_s}Q^{os_procinfo_map_s}QQ{subchunk_queue_t=^{catalog_subchunk_s}^^{catalog_subchunk_s}}Q}@?>28"
+ "^{catalog_s={catalog_hdr_s=SQ}^{os_trace_uuid_map_s}^{os_trace_str_map_s}Q^{os_procinfo_map_s}QQ{subchunk_queue_t=^{catalog_subchunk_s}^^{catalog_subchunk_s}}Q}8@?0"
+ "^{os_timesync_time_entry_s={os_timesync_header_s=SSI}QQ{timezone=ii}}"
+ "^{tp_element=SqqQC(?={?=qQQ}{?=SCB}{?=Si})}"
+ "^{tp_element=SqqQC(?={?=qQQ}{?=SCB}{?=Si})}52@0:8q16q24@32Q40C48"
+ "_BaseTracepointBuffer"
+ "_MemoryEfficientEnumeratorCatalogSubchunk"
+ "_MemoryEfficientTracepointBuffer"
+ "_OSLogCache"
+ "_OSLogLRUCache"
+ "_activateStreamFromDate:toDate:useMemEffic:catalogCacheSize:dataCacheSize:"
+ "_activateStreamInRange:useMemEffic:catalogCacheSize:dataCacheSize:"
+ "_algo"
+ "_buuid"
+ "_cache"
+ "_canMutate"
+ "_catalog_offset"
+ "_chunk_offset"
+ "_fileIndex"
+ "_had_subchunk"
+ "_key"
+ "_lock"
+ "_maxCount"
+ "_memEffic"
+ "_mruItems"
+ "_msgID"
+ "_next"
+ "_ocount"
+ "_osize"
+ "_oversizeTable"
+ "_pidversion"
+ "_prev"
+ "_storage"
+ "_storeCatalogsAndSubchunks"
+ "_tp_offset"
+ "_traceEvents"
+ "_tsEntries"
+ "_tscount"
+ "_tssize"
+ "_usize"
+ "_uuids"
+ "`"
+ "activateStreamFromDate:catalogCacheSize:dataCacheSize:"
+ "addTSEntry:"
+ "addToTail:"
+ "advanceCursorToTime:"
+ "aggregationForLogReporterWithStartDate:endDate:predicate:withOptions:catalogCacheSize:dataCacheSize:errorOut:"
+ "aggregationForStartDate_impl:endDate:predicate:withOptions:catalogCacheSize:dataCacheSize:useMemEffic:errorOut:"
+ "algo"
+ "algo_key"
+ "allocWithZone:"
+ "allocateRow"
+ "assertion failure: \"!filter\" -> %llu"
+ "assertion failure: \"!stream->all_procs\" -> %llu"
+ "assertion failure: \"((char *)field_pointer + member_size) <= ((char *)arg->data + arg->size)\" -> %llu"
+ "assertion failure: \"(domain_length + 1) < 255\" -> %llu"
+ "assertion failure: \"0 < element_size && element_size <= 65535\" -> %llu"
+ "assertion failure: \"0 < member_size && member_size <= 65535\" -> %llu"
+ "assertion failure: \"__extension__({ __typeof__(_os_trace_close(tsfd)) _e = ((__typeof__(_os_trace_close(tsfd)))__builtin_expect(((long)(_os_trace_close(tsfd))), (0l))); if (_e == (__typeof__(_os_trace_close(tsfd)))-1) { _os_assumes_log((uint64_t)(uintptr_t)(*__error())); } _e; })\" -> %{errno}d"
+ "assertion failure: \"_eint.log_message.hdr == ((void*)0)\" -> %llu"
+ "assertion failure: \"_pass == MAPPER_PASS_VALIDATE\" -> %llu"
+ "assertion failure: \"_version != -1\" -> %llu"
+ "assertion failure: \"array_info.ctr_nelems * (uint16_t)element_size <= size\" -> %llu"
+ "assertion failure: \"array_info.ctr_nelems <= size\" -> %llu"
+ "assertion failure: \"ctf_is_type(domain, domain_length)\" -> %llu"
+ "assertion failure: \"enum_size <= size\" -> %llu"
+ "assertion failure: \"error == (1ull)\" -> %llu"
+ "assertion failure: \"error == 0\" -> %llu"
+ "assertion failure: \"expression.arguments.count == 1\" -> %llu"
+ "assertion failure: \"expression.operand.expressionType == NSEvaluatedObjectExpressionType\" -> %llu"
+ "assertion failure: \"kind < 31\" -> %llu"
+ "assertion failure: \"metadata->ctf != ((void*)0)\" -> %llu"
+ "assertion failure: \"metadata->ctf == ((void*)0)\" -> %llu"
+ "assertion failure: \"mkdirat(dfd, \"timesync\", 0755)\" -> %{errno}d"
+ "assertion failure: \"nested_type != (-1L)\" -> %llu"
+ "assertion failure: \"op == LOGDEV_NEW\" -> %llu"
+ "assertion failure: \"privacy_flags\" -> %llu"
+ "assertion failure: \"result\" -> %llu"
+ "assertion failure: \"self.tier <= OSLogStatisticsAggregationTier_MAXIMUM\" -> %llu"
+ "assertion failure: \"stream->all_procs\" -> %llu"
+ "assertion failure: \"strncmp(domain, \"type\", 4) == 0\" -> %llu"
+ "assertion failure: \"type_size <= size\" -> %llu"
+ "assertion failure: \"unlinkat(dfd, \"timesync\", 0x0080)\" -> %{errno}d"
+ "assertion failure: \"unlinkat(tsfd, names[i]->d_name, 0)\" -> %{errno}d"
+ "assertion failure: \"xpc_array_get_count(pids)\" -> %llu"
+ "assertion failure: \"xpc_array_get_count(uids)\" -> %llu"
+ "bufferHasFreeSpace"
+ "bug in LRUCache implementation; %ld != %ld"
+ "buuid"
+ "cache"
+ "canMutate"
+ "catalogCache"
+ "catalogForCDHash:identifier:generator:"
+ "catalog_offset"
+ "chunkRange"
+ "chunk_offset"
+ "clientCatalogCache"
+ "clientDataCache"
+ "compareTimestamp:"
+ "consolidate"
+ "copyWithZone:"
+ "cursor"
+ "dataCache"
+ "dataForCDHash:identifier:size:generator:"
+ "data_key"
+ "decompressedBufferForChunk:"
+ "dictionaryWithCapacity:"
+ "enumerateEntriesInRange:options:usingCatalogFilter:catalogCacheSize:dataCacheSize:usingBlock:"
+ "evictAllEntries"
+ "evictionHandler"
+ "fileIndex"
+ "findOversize:process:oversize_id:pidversion:timestamp:block:"
+ "flush"
+ "getBootUUIDIndex:"
+ "getFileNameAt:"
+ "growBuffer:"
+ "growBufferImmediatelyIfNeeded"
+ "hash64"
+ "head"
+ "indexOfUUID:"
+ "init:dataCacheSize:"
+ "init:evictionHandler:"
+ "init:msgID:pidV:timestamp:"
+ "initWithCDHash:identifier:"
+ "initWithIndex:metadata:fileBootList:catalogFilter:options:catalogCacheSize:dataCacehSize:"
+ "initWithKey:data:"
+ "initWithName:maxCount:evictionHandler:"
+ "initWithStore:index:fileHeader:range:chunk:storeCatalogsAndSubchunks:"
+ "insertOversizedChunk:chunkOffset:chunkSetStartAddr:subchunk:chunkList:"
+ "insertValuesIntoIndex:coffset:fileName:sortKey:type:"
+ "isEqualToCacheIndex:"
+ "iterateChunksAndFillEvent:block:"
+ "key"
+ "keysSortedByValueUsingSelector:"
+ "maxCount"
+ "mruItems"
+ "msgID"
+ "next"
+ "numberWithUnsignedShort:"
+ "pidversion"
+ "pointerValue"
+ "prev"
+ "removeFromHead"
+ "removeNodeAndAddToTail:"
+ "retireOversize:"
+ "setCanMutate:"
+ "setCatalog_offset:"
+ "setChunkRange:"
+ "setChunk_offset:"
+ "setCount:"
+ "setCursor:"
+ "setData:"
+ "setEvictionHandler:"
+ "setFileIndex:"
+ "setFileNames:"
+ "setHead:"
+ "setKey:"
+ "setMsgID:"
+ "setNext:"
+ "setPidversion:"
+ "setPrev:"
+ "setProcessID:"
+ "setSize:"
+ "setTail:"
+ "setTimestamp:"
+ "setTp_offset:"
+ "setupStoresForIndex:"
+ "size_key"
+ "storage"
+ "storeArray"
+ "storeCatalogsAndSubchunks"
+ "tail"
+ "tp_offset"
+ "usize"
+ "v16@?0^{firehose_tracepoint_s=(?={?=CCSI}QAQ)Q(?={?=b48b16}QAQ)[0C]}8"
+ "v24@0:8@?<B@?^{tracev3_chunk_s={tracev3_chunk_preamble_s=IIQ}(?={tracev3_chunk_header_s={mach_timebase_info=II}QqiiiI{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_continuous_s=Q}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_systeminfo_s=ii[16c][32c]}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_generation_s=[16C]ii}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_timezone_s=[48c]}}{tracev3_chunk_catalog_s=SSSS[0C]}{tracev3_chunk_catalog_v2_s=SSSSS[3S]Q[0C]}{tracev3_chunk_log_preamble_s=QIC[3C]}{tracev3_chunk_firehose_s=QICC[2C][0C]}{tracev3_chunk_firehose_old_s=QiCC[0C]}{tracev3_chunk_oversize_s=QIC[3C]QISS[0C]}{tracev3_chunk_oversize_old_s=QISS[0C]}{tracev3_chunk_statedump_s=QIC[3C]QQ[16C][0C]}{tracev3_chunk_simple_s=QICC[2C]QQQ[16C][16C][0C]}[0C])}q^v>16"
+ "v24@0:8@?<v@?@@>16"
+ "v24@?0@8@16"
+ "v28@?0S8q12^{catalog_s={catalog_hdr_s=SQ}^{os_trace_uuid_map_s}^{os_trace_str_map_s}Q^{os_procinfo_map_s}QQ{subchunk_queue_t=^{catalog_subchunk_s}^^{catalog_subchunk_s}}Q}20"
+ "v32@0:8@16I24I28"
+ "v32@?0S8q12I20*24"
+ "v36@0:8^{os_timesync_range_s=^{os_trace_uuid_map_s}QQ[0[16C]]}16B24I28I32"
+ "v44@0:8@16@24B32I36I40"
+ "v52@0:8^{os_timesync_range_s=^{os_trace_uuid_map_s}QQ[0[16C]]}16I24@28I36I40@?44"
+ "v56@0:8^{tracev3_chunk_s={tracev3_chunk_preamble_s=IIQ}(?={tracev3_chunk_header_s={mach_timebase_info=II}QqiiiI{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_continuous_s=Q}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_systeminfo_s=ii[16c][32c]}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_generation_s=[16C]ii}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_timezone_s=[48c]}}{tracev3_chunk_catalog_s=SSSS[0C]}{tracev3_chunk_catalog_v2_s=SSSSS[3S]Q[0C]}{tracev3_chunk_log_preamble_s=QIC[3C]}{tracev3_chunk_firehose_s=QICC[2C][0C]}{tracev3_chunk_firehose_old_s=QiCC[0C]}{tracev3_chunk_oversize_s=QIC[3C]QISS[0C]}{tracev3_chunk_oversize_old_s=QISS[0C]}{tracev3_chunk_statedump_s=QIC[3C]QQ[16C][0C]}{tracev3_chunk_simple_s=QICC[2C]QQQ[16C][16C][0C]}[0C])}16q24^v32@40@48"
+ "valueWithPointer:"
+ "{_NSRange=QQ}16@0:8"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "%{"
- ".."
- "0"
- "1"
- "1`"
- "@\"_OSLogEnumeratorCatalogSubchunk\""
- "@\"_OSLogTracepointBuffer\""
- "@48@0:8@16^{?={_os_log_index_timeref=[16C]Q}{_os_log_index_timeref=[16C]Q}{_os_log_index_timeref=[16C]Q}{_os_log_index_timeref=[16C]Q}{_os_log_index_timeref=[16C]Q}{_os_log_index_timeref=[16C]Q}^{_os_log_index_timeref}[5{?={_os_log_index_timeref=[16C]Q}C}]}24@32@40"
- "@64@0:8@16@24^{tracev3_chunk_s={tracev3_chunk_preamble_s=IIQ}(?={tracev3_chunk_header_s={mach_timebase_info=II}QqiiiI{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_continuous_s=Q}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_systeminfo_s=ii[16c][32c]}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_generation_s=[16C]ii}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_timezone_s=[48c]}}{tracev3_chunk_catalog_s=SSSS[0C]}{tracev3_chunk_catalog_v2_s=SSSSS[3S]Q[0C]}{tracev3_chunk_log_preamble_s=QIC[3C]}{tracev3_chunk_firehose_s=QICC[2C][0C]}{tracev3_chunk_firehose_old_s=QiCC[0C]}{tracev3_chunk_oversize_s=QIC[3C]QISS[0C]}{tracev3_chunk_oversize_old_s=QISS[0C]}{tracev3_chunk_statedump_s=QIC[3C]QQ[16C][0C]}{tracev3_chunk_simple_s=QICC[2C]QQQ[16C][16C][0C]}[0C])}32{_NSRange=QQ}40^{tracev3_chunk_s={tracev3_chunk_preamble_s=IIQ}(?={tracev3_chunk_header_s={mach_timebase_info=II}QqiiiI{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_continuous_s=Q}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_systeminfo_s=ii[16c][32c]}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_generation_s=[16C]ii}{tracev3_subchunk_preamble_s=II}{tracev3_subchunk_timezone_s=[48c]}}{tracev3_chunk_catalog_s=SSSS[0C]}{tracev3_chunk_catalog_v2_s=SSSSS[3S]Q[0C]}{tracev3_chunk_log_preamble_s=QIC[3C]}{tracev3_chunk_firehose_s=QICC[2C][0C]}{tracev3_chunk_firehose_old_s=QiCC[0C]}{tracev3_chunk_oversize_s=QIC[3C]QISS[0C]}{tracev3_chunk_oversize_old_s=QISS[0C]}{tracev3_chunk_statedump_s=QIC[3C]QQ[16C][0C]}{tracev3_chunk_simple_s=QICC[2C]QQQ[16C][16C][0C]}[0C])}56"
- "B16@?0@\"_OSLogEnumeratorCatalogSubchunk\"8"
- "BUG IN LIBTRACE: _tp_class_ttl_to called with invalid tp"
- "BUG IN LIBTRACE: oltb maniplation while immutable"
- "R"
- "T@\"NSMutableOrderedSet\",R,N,V_fileNames"
- "T@\"_OSLogTracepointBuffer\",R,N,V_tracepoints"
- "_OSLogTracepointBuffer"
- "_activateStreamFromDate:toDate:"
- "_activateStreamInRange:"
- "_decompressedBufferForChunk:subchunk:"
- "_mutable"
- "endTimeCompare:"
- "enumerateEntriesInRange:options:usingCatalogFilter:usingBlock:"
- "initWithIndex:metadata:fileBootList:catalogFilter:"
- "initWithStore:index:fileHeader:range:chunk:"
- "oldestTimeCompare:"
- "v24@0:8^{os_timesync_range_s=^{os_trace_uuid_map_s}QQ[0[16C]]}16"
- "v44@0:8^{os_timesync_range_s=^{os_trace_uuid_map_s}QQ[0[16C]]}16I24@28@?36"

```
