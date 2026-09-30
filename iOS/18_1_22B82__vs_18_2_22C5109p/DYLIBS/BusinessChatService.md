## BusinessChatService

> `/System/Library/PrivateFrameworks/BusinessChatService.framework/BusinessChatService`

```diff

-30095.31.8.12.6
-  __TEXT.__text: 0x6b6f8
-  __TEXT.__auth_stubs: 0x9f0
-  __TEXT.__objc_methlist: 0x6dcc
-  __TEXT.__const: 0x1c8
-  __TEXT.__cstring: 0x781f
-  __TEXT.__oslogstring: 0x40e3
-  __TEXT.__gcc_except_tab: 0x8d4
+30095.32.9.7.3
+  __TEXT.__text: 0x71d18
+  __TEXT.__auth_stubs: 0xa00
+  __TEXT.__objc_methlist: 0x6fec
+  __TEXT.__const: 0x1f0
+  __TEXT.__cstring: 0x80ca
+  __TEXT.__oslogstring: 0x4524
+  __TEXT.__gcc_except_tab: 0xad4
   __TEXT.__ustring: 0x5b0
-  __TEXT.__unwind_info: 0x16f0
-  __TEXT.__objc_classname: 0x1654
-  __TEXT.__objc_methname: 0xd790
-  __TEXT.__objc_methtype: 0x2c8f
-  __TEXT.__objc_stubs: 0x9260
-  __DATA_CONST.__got: 0x400
-  __DATA_CONST.__const: 0x1828
-  __DATA_CONST.__objc_classlist: 0x4a0
+  __TEXT.__unwind_info: 0x17e8
+  __TEXT.__objc_classname: 0x1709
+  __TEXT.__objc_methname: 0xde16
+  __TEXT.__objc_methtype: 0x30c9
+  __TEXT.__objc_stubs: 0x9740
+  __DATA_CONST.__got: 0x408
+  __DATA_CONST.__const: 0x1b18
+  __DATA_CONST.__objc_classlist: 0x4b0
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x2d8
+  __DATA_CONST.__objc_protolist: 0x2f8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2f40
-  __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x388
+  __DATA_CONST.__objc_selrefs: 0x3080
+  __DATA_CONST.__objc_protorefs: 0x40
+  __DATA_CONST.__objc_superrefs: 0x390
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x508
+  __AUTH_CONST.__auth_got: 0x510
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x2c0
-  __AUTH_CONST.__cfstring: 0x5a40
-  __AUTH_CONST.__objc_const: 0x119b8
+  __AUTH_CONST.__const: 0x2e0
+  __AUTH_CONST.__cfstring: 0x5cc0
+  __AUTH_CONST.__objc_const: 0x11fa8
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_ivar: 0x5b8
-  __DATA.__data: 0xda10
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0x5d4
+  __DATA.__data: 0xdb90
   __DATA.__bss: 0x10
-  __DATA_DIRTY.__objc_ivar: 0x2b0
+  __DATA_DIRTY.__objc_ivar: 0x2b8
   __DATA_DIRTY.__objc_data: 0x2e40
   __DATA_DIRTY.__bss: 0x190
   __DATA_DIRTY.__common: 0x10

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2539
-  Symbols:   2934
-  CStrings:  4139
+  Functions: 2611
+  Symbols:   3009
+  CStrings:  4278
 
Symbols:
+ _BCSErrorCancelled
+ _BCSErrorNotFoundCode
+ _BCSErrorUnknownCode
+ _objc_storeWeak
- _BCSErrorUnkownCode
CStrings:
+ "\""
+ "%!s(MISSING) - %!l(MISSING)d items not found in cache for - type: %!@(MISSING)"
+ "%!s(MISSING) - All items found in cache for type: %!@(MISSING)"
+ "%!s(MISSING) - Failed to fetch requested data (received NSNull for %!{(MISSING)private}@)"
+ "%!s(MISSING) - Found cached item - type: %!@(MISSING)"
+ "%!s(MISSING) - Invalid request ID!"
+ "%!s(MISSING) - No more items to fetch - type: %!@(MISSING)"
+ "%!s(MISSING) - Unexpected response data (received %!@(MISSING), expected NSData)"
+ "%!s(MISSING) - Unexpectedly invalid index (%!l(MISSING)u) in query item identifiers (%!@(MISSING){private})"
+ "%!s(MISSING) - fetching data from PIR for key '%!{(MISSING)private}@'"
+ "%!s(MISSING) - fetching data from PIR for keys '%!{(MISSING)private}@'"
+ "%!s(MISSING) - issuing request with requestId: %!@(MISSING)"
+ "%!s(MISSING) Shard Identifiers: %!l(MISSING)d ConfigItem %!@(MISSING) type %!l(MISSING)d Shard Count %!l(MISSING)ld"
+ "-[BCSBusinessEmailResolver _metadataMatching:metric:perItemBlock:completion:]_block_invoke"
+ "-[BCSBusinessEmailResolver itemsMatching:metric:perItemBlock:completion:]"
+ "-[BCSBusinessQueryController fetchAreBusinessesRegisteredWithQuery:completion:]"
+ "-[BCSBusinessQueryController fetchAreBusinessesRegisteredWithQuery:completion:]_block_invoke"
+ "-[BCSBusinessQueryController fetchBusinessMetadataForEmails:forClientBundleID:requestId:completion:]"
+ "-[BCSBusinessQueryController fetchItemsWithQuery:perItemCompletion:completion:]"
+ "-[BCSBusinessQueryController fetchItemsWithQuery:perItemCompletion:completion:]_block_invoke"
+ "-[BCSBusinessQueryController fetchShardsWithQuery:completion:]"
+ "-[BCSBusinessQueryController fetchShardsWithQuery:completion:]_block_invoke"
+ "-[BCSBusinessQueryService didFetchBusinessMetadata:forEmailIdentifier:requestId:error:reply:]"
+ "-[BCSBusinessQueryService didFetchBusinessMetadataForEmailsForRequestId:error:reply:]"
+ "-[BCSBusinessQueryService fetchBusinessMetadataForEmails:perItemCallback:completion:]"
+ "-[BCSRemoteFetchPIR fetchDataMatchingBatch:timeout:perItemBlock:completion:]"
+ "-[BCSRemoteFetchPIR fetchDataMatchingBatch:timeout:perItemBlock:completion:]_block_invoke"
+ "-[BCSRemoteFetchPIR fetchDataMatchingBatch:timeout:perItemBlock:completion:]_block_invoke_2"
+ "-[BCSShardResolver shardItemsMatching:metric:completion:]"
+ "-[BCSShardResolver shardItemsMatching:metric:completion:]_block_invoke"
+ "-[BCSShardResolver triggerMegashardFetchForShardType:reason:completion:]_block_invoke_2"
+ "<%!@(MISSING) { email: %!@(MISSING), fullDomain: %!@(MISSING), topLevelDomain: %!@(MISSING) }>"
+ "<%!@(MISSING) { email: %!@(MISSING), name: %!@(MISSING), displayName: %!@(MISSING), businessId: %!@(MISSING), companyId: %!@(MISSING)>"
+ "@\"<BCSItemResolving><BCSItemBatchResolving>\""
+ "@\"<BCSXPCDaemonBusinessEmailClientInterface>\""
+ "@\"NSUUID\""
+ "@52@0:8@16@24@32q40B48"
+ "B32@?0@\"<BCSItemIdentifying>\"8@\"BCSItem\"16@\"NSError\"24"
+ "B32@?0@\"<BCSItemIdentifying>\"8@\"NSData\"16@\"NSError\"24"
+ "BCSBatchQuery"
+ "BCSBusinessBatchProvider"
+ "BCSBusinessBatchQuery"
+ "BCSBusinessQueryRequest"
+ "BCSItemBatchResolving"
+ "BCSProtoLocalizedStringsHelper"
+ "BCSXPCDaemonBusinessEmailClientInterface"
+ "Batch exceeds maximum size (%!l(MISSING)d > %!l(MISSING)ld)"
+ "BusinessEmail (Client): Received response to didFetchBusinessMetadata:forEmailIdentifier:withError:reply:"
+ "Client cancelled request"
+ "Failed to decompress data"
+ "Failed to decompress data (%!@(MISSING))!"
+ "Failed to fetch some items"
+ "Fetched shards: %!@(MISSING)"
+ "Invalid response from server"
+ "Missing business metadata entitlement"
+ "Must request at least one identifier"
+ "Nil results & nil fetchShardError"
+ "No data received"
+ "No identifiers requested"
+ "No matching data found"
+ "Request cancelled by caller (perItem block return NO)"
+ "T@\"NSArray\",&,N,V_itemIdentifiers"
+ "T@\"NSArray\",&,N,V_shardIdentifiers"
+ "T@\"NSUUID\",&,N,V_requestId"
+ "T@?,C,N,V_fetchEmailsCompletion"
+ "T@?,C,N,V_fetchEmailsPerItemBlock"
+ "Unexpected item"
+ "Unexpected item identifier (should be BCSBusinessEmailItemIdentifier, got %!{(MISSING)private}@)"
+ "Unexpected item identifier (wrong class)"
+ "Unsupported type (batch requests for logos are unimplemented)"
+ "_exportedClient"
+ "_fetchEmailsCompletion"
+ "_fetchEmailsPerItemBlock"
+ "_itemIdentifiers"
+ "_metadataMatching:metric:perItemBlock:completion:"
+ "_requestId"
+ "_requestLock"
+ "_requestsById"
+ "_shardIdentifiers"
+ "allObjects"
+ "arrayWithArray:"
+ "dataByStringKeywords:error:"
+ "defaultLocalizedStringsValue"
+ "dictionaryWithCapacity:"
+ "didFetchBusinessMetadata:forEmailIdentifier:requestId:error:reply:"
+ "didFetchBusinessMetadata:forEmailIdentifier:withError:reply: - requestId: %!@(MISSING), metadata: %!@(MISSING), identifier: %!@(MISSING), error: %!@(MISSING)"
+ "didFetchBusinessMetadataForEmailsForRequestId:error:reply:"
+ "didFetchBusinessMetadataForEmailsWithError:reply: - requestId: %!@(MISSING), error: %!@(MISSING)"
+ "displayName"
+ "fetchAreBusinessesRegisteredWithQuery:completion:"
+ "fetchBusinessMetadataForEmails:forClientBundleID:requestId:completion:"
+ "fetchBusinessMetadataForEmails:forClientBundleId:requestId:completion: did error: %!@(MISSING)"
+ "fetchBusinessMetadataForEmails:perItemCallback:completion:"
+ "fetchDataMatchingBatch:timeout:perItemBlock:completion:"
+ "fetchEmailsCompletion"
+ "fetchEmailsPerItemBlock"
+ "fetchItemsWithQuery:perItemCompletion:completion:"
+ "fetchShardsWithQuery:completion:"
+ "initWithArray:"
+ "initWithDefaultsDictionary:"
+ "initWithFilterMatchResult:config:"
+ "initWithIdentifier:defaultsDictionary:"
+ "initWithItemIdentifier:config:clientBundleId:shardType:skipRegistrationCheck:"
+ "initWithItemIdentifiers:config:clientBundleId:shardType:skipRegistrationCheck:"
+ "itemIdentifiers"
+ "itemsMatching:metric:perItemBlock:completion:"
+ "localizedStringsToDictionary"
+ "matchesIdentifier:"
+ "requestDataByStringKeywords:completionHandler:"
+ "requestId"
+ "setClasses:forSelector:argumentIndex:ofReply:"
+ "setExportedClient:"
+ "setExportedInterface:"
+ "setExportedObject:"
+ "setFetchEmailsCompletion:"
+ "setFetchEmailsPerItemBlock:"
+ "setItemIdentifiers:"
+ "setRequestId:"
+ "setShardIdentifiers:"
+ "shardIdentifiers"
+ "shardItemsMatching:metric:completion:"
+ "subErrors"
+ "v12@?0B8"
+ "v24@0:8@\"<BCSXPCDaemonBusinessEmailClientInterface>\"16"
+ "v24@0:8@\"NSArray\"16"
+ "v24@?0@\"NSDictionary\"8@\"NSError\"16"
+ "v32@0:8@\"<BCSBusinessBatchQuery>\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "v32@0:8@\"<BCSBusinessBatchQuery>\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
+ "v40@0:8@\"<BCSBusinessBatchQuery>\"16@\"<BCSResolutionMetricProtocol>\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
+ "v40@0:8@\"<BCSBusinessBatchQuery>\"16@?<B@?@\"<BCSItemIdentifying>\"@\"BCSItem\"@\"NSError\">24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSUUID\"16@\"NSError\"24@?<v@?>32"
+ "v40@0:8@16@?24@?32"
+ "v48@0:8@\"<BCSBusinessBatchQuery>\"16@\"<BCSResolutionMetricProtocol>\"24@?<B@?@\"<BCSItemIdentifying>\"@\"BCSItem\"@\"NSError\">32@?<v@?@\"NSError\">40"
+ "v48@0:8@\"<BCSBusinessBatchQuery>\"16q24@?<B@?@\"<BCSItemIdentifying>\"@\"NSData\"@\"NSError\">32@?<v@?@\"NSError\">40"
+ "v48@0:8@\"NSArray\"16@\"NSString\"24@\"NSUUID\"32@?<v@?@\"NSError\">40"
+ "v48@0:8@16@24@?32@?40"
+ "v48@0:8@16q24@?32@?40"
+ "v56@0:8@\"BCSBusinessEmailItem\"16@\"BCSBusinessEmailIdentifier\"24@\"NSUUID\"32@\"NSError\"40@?<v@?B>48"
+ "v56@0:8@16@24@32@40@?48"
- "%!s(MISSING) - fetching data from PIR for key '%!@(MISSING)'"
- "-[BCSShardResolver shardItemMatching:clientBundleID:metric:completion:]_block_invoke_2"

```
