## DataDeliveryServices

> `/System/Library/PrivateFrameworks/DataDeliveryServices.framework/DataDeliveryServices`

```diff

-90.0.0.0.0
-  __TEXT.__text: 0x240e8
+93.0.0.0.0
+  __TEXT.__text: 0x23d90
   __TEXT.__auth_stubs: 0x620
-  __TEXT.__objc_methlist: 0x2584
+  __TEXT.__objc_methlist: 0x2564
   __TEXT.__const: 0x168
-  __TEXT.__gcc_except_tab: 0x6c4
-  __TEXT.__cstring: 0x11a6
-  __TEXT.__oslogstring: 0x2dad
-  __TEXT.__unwind_info: 0xac8
-  __TEXT.__objc_classname: 0x4ce
-  __TEXT.__objc_methname: 0x4ff5
-  __TEXT.__objc_methtype: 0x136c
-  __TEXT.__objc_stubs: 0x44a0
+  __TEXT.__gcc_except_tab: 0x6f0
+  __TEXT.__cstring: 0x1230
+  __TEXT.__oslogstring: 0x2dfb
+  __TEXT.__unwind_info: 0xa80
+  __TEXT.__objc_classname: 0x4ba
+  __TEXT.__objc_methname: 0x4f29
+  __TEXT.__objc_methtype: 0x133c
+  __TEXT.__objc_stubs: 0x43e0
   __DATA_CONST.__got: 0x2b8
-  __DATA_CONST.__const: 0xd50
+  __DATA_CONST.__const: 0xdd0
   __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1368
+  __DATA_CONST.__objc_selrefs: 0x1338
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x108
   __DATA_CONST.__objc_arraydata: 0x70
   __AUTH_CONST.__auth_got: 0x320
   __AUTH_CONST.__const: 0x2a0
-  __AUTH_CONST.__cfstring: 0x1440
-  __AUTH_CONST.__objc_const: 0x7a70
+  __AUTH_CONST.__cfstring: 0x1540
+  __AUTH_CONST.__objc_const: 0x79e8
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x208
+  __DATA.__objc_ivar: 0x1fc
   __DATA.__data: 0xab0
   __DATA.__bss: 0x38
   __DATA_DIRTY.__objc_data: 0xc30

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A8D88E22-8326-30BE-A2F4-0FB4384D3FBE
-  Functions: 888
-  Symbols:   3471
-  CStrings:  1702
+  UUID: 11F808EB-D117-3CE3-B51E-DE510EFA5345
+  Functions: 878
+  Symbols:   3438
+  CStrings:  1705
 
Symbols:
+ -[DDSAssetCenter triggerDumpWithReply:]
+ -[DDSCache init]
+ -[DDSInterface triggerDumpWithReply:]
+ -[DDSManager triggerDumpWithReply:]
+ -[DDSManager triggerDumpWithReply:].cold.1
+ -[DDSManager triggerDumpWithReply:].cold.2
+ GCC_except_table17
+ GCC_except_table32
+ _AssetUpdatePostCacheClearNotificationPrefix
+ _OBJC_CLASS_$_NSNotificationCenter
+ _OBJC_IVAR_$_DDSCache._lock
+ __OBJC_$_PROP_LIST_DDSMobileAssetv2ProviderDataSource.339
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_DDSCache
+ __OBJC_$_PROTOCOL_METHOD_TYPES_DDSCache
+ __OBJC_$_PROTOCOL_REFS_DDSCache
+ __OBJC_CLASS_PROTOCOLS_$_DDSCache
+ __OBJC_LABEL_PROTOCOL_$_DDSCache
+ __OBJC_PROTOCOL_$_DDSCache
+ ___37-[DDSInterface triggerDumpWithReply:]_block_invoke
+ ___37-[DDSInterface triggerDumpWithReply:]_block_invoke_2
+ ___39-[DDSAssetCenter triggerDumpWithReply:]_block_invoke
+ ___43-[DDSInterface createConnectionIfNecessary]_block_invoke.6
+ ___43-[DDSManager updateAssetForQuery:callback:]_block_invoke.314
+ ___48-[DDSAssetCenter serverDidUpdateAssetsWithType:]_block_invoke.307
+ ___48-[DDSServer listener:shouldAcceptNewConnection:]_block_invoke.306
+ ___48-[DDSServer listener:shouldAcceptNewConnection:]_block_invoke.306.cold.1
+ ___51-[DDSManager didEndUpdateCycleWithAssetType:error:]_block_invoke.301
+ ___54-[DDSManager fetchAssetUpdateStatusForQuery:callback:]_block_invoke.310
+ ___54-[DDSManager fetchAssetUpdateStatusForQuery:callback:]_block_invoke.312
+ ___59-[DDSManager updateCatalogBasedAssetForAssertion:callback:]_block_invoke.313
+ ___59-[DDSManager updateCatalogBasedAssetForAssertion:callback:]_block_invoke.313.cold.1
+ ___59-[DDSManager updateCatalogBasedAssetForAssertion:callback:]_block_invoke.313.cold.2
+ ___72-[DDSManager beginUpdateCycleForAssetType:forced:discretionaryDownload:]_block_invoke.290
+ ___84-[DDSMobileAssetv2Provider beginDownloadForAssertion:discretionaryDownload:handler:]_block_invoke.309
+ ___84-[DDSMobileAssetv2Provider beginDownloadForAssertion:discretionaryDownload:handler:]_block_invoke.309.cold.1
+ ___84-[DDSMobileAssetv2Provider beginDownloadForAssertion:discretionaryDownload:handler:]_block_invoke.309.cold.2
+ ___block_descriptor_40_e8_32bs_e18_v16?0"NSString"8ls32l8
+ ___block_descriptor_40_e8_32r_e18_v16?0"NSString"8lr32l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_literal_global.11
+ ___block_literal_global.13
+ ___block_literal_global.285
+ ___block_literal_global.298
+ ___block_literal_global.87
+ ___block_literal_global.9
+ ___block_literal_global.99
+ _objc_msgSend$defaultCenter
+ _objc_msgSend$postNotificationName:object:
+ _objc_msgSend$triggerDumpWithReply:
- -[DDSAssetCenter triggerDump]
- -[DDSAssetQueryResultCache cache:willEvictObjects:]
- -[DDSCache delegate]
- -[DDSCache initWithMaxCount:]
- -[DDSCache maxCount]
- -[DDSCache order]
- -[DDSCache queue]
- -[DDSCache setDelegate:]
- -[DDSInterface triggerDump]
- -[DDSManager triggerDump]
- -[DDSManager triggerDump].cold.1
- -[DDSManager triggerDump].cold.2
- _OBJC_CLASS_$_NSMutableOrderedSet
- _OBJC_IVAR_$_DDSCache._delegate
- _OBJC_IVAR_$_DDSCache._maxCount
- _OBJC_IVAR_$_DDSCache._order
- _OBJC_IVAR_$_DDSCache._queue
- __OBJC_$_PROP_LIST_DDSMobileAssetv2ProviderDataSource.336
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_DDSCacheDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_DDSCacheDelegate
- __OBJC_$_PROTOCOL_REFS_DDSCacheDelegate
- __OBJC_CLASS_PROTOCOLS_$_DDSAssetQueryResultCache
- __OBJC_LABEL_PROTOCOL_$_DDSCacheDelegate
- __OBJC_PROTOCOL_$_DDSCacheDelegate
- ___22-[DDSCache clearCache]_block_invoke
- ___25-[DDSCache objectForKey:]_block_invoke
- ___27-[DDSInterface triggerDump]_block_invoke
- ___31-[DDSCache cacheObject:forKey:]_block_invoke
- ___39-[DDSCache removeEntriesWithPrefixKey:]_block_invoke
- ___43-[DDSInterface createConnectionIfNecessary]_block_invoke.5
- ___43-[DDSManager updateAssetForQuery:callback:]_block_invoke.308
- ___48-[DDSAssetCenter serverDidUpdateAssetsWithType:]_block_invoke.301
- ___48-[DDSServer listener:shouldAcceptNewConnection:]_block_invoke.303
- ___48-[DDSServer listener:shouldAcceptNewConnection:]_block_invoke.303.cold.1
- ___51-[DDSManager didEndUpdateCycleWithAssetType:error:]_block_invoke.295
- ___54-[DDSManager fetchAssetUpdateStatusForQuery:callback:]_block_invoke.304
- ___54-[DDSManager fetchAssetUpdateStatusForQuery:callback:]_block_invoke.306
- ___59-[DDSManager updateCatalogBasedAssetForAssertion:callback:]_block_invoke.307
- ___59-[DDSManager updateCatalogBasedAssetForAssertion:callback:]_block_invoke.307.cold.1
- ___59-[DDSManager updateCatalogBasedAssetForAssertion:callback:]_block_invoke.307.cold.2
- ___72-[DDSManager beginUpdateCycleForAssetType:forced:discretionaryDownload:]_block_invoke.287
- ___84-[DDSMobileAssetv2Provider beginDownloadForAssertion:discretionaryDownload:handler:]_block_invoke.306
- ___84-[DDSMobileAssetv2Provider beginDownloadForAssertion:discretionaryDownload:handler:]_block_invoke.306.cold.1
- ___84-[DDSMobileAssetv2Provider beginDownloadForAssertion:discretionaryDownload:handler:]_block_invoke.306.cold.2
- ___block_literal_global.12
- ___block_literal_global.282
- ___block_literal_global.292
- ___block_literal_global.73
- ___block_literal_global.8
- ___block_literal_global.85
- _objc_msgSend$cache:willEvictObjects:
- _objc_msgSend$initWithCapacity:
- _objc_msgSend$initWithMaxCount:
- _objc_msgSend$maxCount
- _objc_msgSend$objectAtIndex:
- _objc_msgSend$order
- _objc_msgSend$removeObjectAtIndex:
- _objc_msgSend$triggerDump
- _objc_msgSend$writeToFile:atomically:encoding:error:
CStrings:
+ "\n"
+ "\n\n"
+ "***********\n"
+ "************\n"
+ "*******************\n"
+ "***********************************"
+ "***********************************\n"
+ "@\"<DDSCache>\""
+ "Cache evicted %lu objects with prefixKey: %{public}@, Evicted objects: %{public}@"
+ "Clearing cache"
+ "Error occurred!!!"
+ "Fired notification: %{public}@"
+ "In Progress:\n"
+ "Installed Assets:\n"
+ "T@\"<DDSCache>\",R,N,V_cache"
+ "com.apple.DataDeliveryServices.AssetUpdatedAndCacheCleared"
+ "defaultCenter"
+ "postNotificationName:object:"
+ "triggerDumpWithReply:"
+ "v16@?0@\"NSString\"8"
+ "v24@0:8@?<v@?@\"NSString\">16"
- "\n\nIn Progress:\n"
- "\nInstalled Assets:\n"
- "/var/tmp/dds_dump_%@.log"
- "@\"<DDSCacheDelegate>\""
- "@\"DDSCache\""
- "@\"NSMutableOrderedSet\""
- "Cache will evict: %{public}@"
- "DDSCacheDelegate"
- "Dumping: \n%{public}@"
- "T@\"<DDSCacheDelegate>\",W,N,V_delegate"
- "T@\"DDSCache\",R,N,V_cache"
- "T@\"NSMutableOrderedSet\",R,N,V_order"
- "TQ,R,N,V_maxCount"
- "_maxCount"
- "_order"
- "cache:willEvictObjects:"
- "com.apple.DataDeliveryServices.DDSAssetQueryResultCache"
- "initWithCapacity:"
- "initWithMaxCount:"
- "maxCount"
- "objectAtIndex:"
- "order"
- "removeObjectAtIndex:"
- "triggerDump"
- "v32@0:8@\"DDSCache\"16@\"NSArray\"24"
- "writeToFile:atomically:encoding:error:"

```
