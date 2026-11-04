## NetworkServiceProxy

> `/System/Library/PrivateFrameworks/NetworkServiceProxy.framework/NetworkServiceProxy`

```diff

-990.40.2.0.0
-  __TEXT.__text: 0x65d9c
-  __TEXT.__objc_methlist: 0x654c
-  __TEXT.__const: 0x370
+990.60.10.0.1
+  __TEXT.__text: 0x68cb4
+  __TEXT.__objc_methlist: 0x6844
+  __TEXT.__const: 0x378
   __TEXT.__gcc_except_tab: 0x64
-  __TEXT.__cstring: 0x5b9c
-  __TEXT.__oslogstring: 0x32c4
-  __TEXT.__unwind_info: 0x15c8
+  __TEXT.__cstring: 0x5d42
+  __TEXT.__oslogstring: 0x33d5
+  __TEXT.__unwind_info: 0x1680
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xcd0
-  __DATA_CONST.__objc_classlist: 0x240
+  __DATA_CONST.__const: 0xd70
+  __DATA_CONST.__objc_classlist: 0x258
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2b20
-  __DATA_CONST.__objc_superrefs: 0x228
+  __DATA_CONST.__objc_selrefs: 0x2be0
+  __DATA_CONST.__objc_superrefs: 0x240
   __DATA_CONST.__objc_arraydata: 0x48
-  __DATA_CONST.__got: 0x478
+  __DATA_CONST.__got: 0x488
   __AUTH_CONST.__const: 0x160
-  __AUTH_CONST.__cfstring: 0x5340
-  __AUTH_CONST.__objc_const: 0x8660
+  __AUTH_CONST.__cfstring: 0x53c0
+  __AUTH_CONST.__objc_const: 0x8a00
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x6d0
-  __AUTH.__objc_data: 0x1540
-  __DATA.__objc_ivar: 0x334
+  __AUTH.__objc_data: 0x1630
+  __DATA.__objc_ivar: 0x340
   __DATA.__data: 0x260
   __DATA.__common: 0x1
-  __DATA_DIRTY.__objc_ivar: 0x310
+  __DATA_DIRTY.__objc_ivar: 0x31c
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__bss: 0x98
   __DATA_DIRTY.__common: 0x20

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2236
-  Symbols:   3447
-  CStrings:  1235
+  Functions: 2303
+  Symbols:   3543
+  CStrings:  1253
 
Symbols:
+ +[NPUtilities copyAllItemsFromKeychainWithIdentifier:]
+ +[NPUtilities totalDataInKeychainWithIdentifier:accountName:]
+ +[NSPPrivacyProxyCostTokenKeyConfig entriesType]
+ -[NSPPrivacyProxyAggregatorService costTokenKeyConfig]
+ -[NSPPrivacyProxyAggregatorService hasCostTokenKeyConfig]
+ -[NSPPrivacyProxyAggregatorService setCostTokenKeyConfig:]
+ -[NSPPrivacyProxyCostTokenKeyConfig .cxx_destruct]
+ -[NSPPrivacyProxyCostTokenKeyConfig addEntries:]
+ -[NSPPrivacyProxyCostTokenKeyConfig clearEntries]
+ -[NSPPrivacyProxyCostTokenKeyConfig copyTo:]
+ -[NSPPrivacyProxyCostTokenKeyConfig copyWithZone:]
+ -[NSPPrivacyProxyCostTokenKeyConfig description]
+ -[NSPPrivacyProxyCostTokenKeyConfig dictionaryRepresentation]
+ -[NSPPrivacyProxyCostTokenKeyConfig entriesAtIndex:]
+ -[NSPPrivacyProxyCostTokenKeyConfig entriesCount]
+ -[NSPPrivacyProxyCostTokenKeyConfig entries]
+ -[NSPPrivacyProxyCostTokenKeyConfig hash]
+ -[NSPPrivacyProxyCostTokenKeyConfig isEqual:]
+ -[NSPPrivacyProxyCostTokenKeyConfig mergeFrom:]
+ -[NSPPrivacyProxyCostTokenKeyConfig readFrom:]
+ -[NSPPrivacyProxyCostTokenKeyConfig setEntries:]
+ -[NSPPrivacyProxyCostTokenKeyConfig writeTo:]
+ -[NSPPrivacyProxyCostTokenKeyEntry .cxx_destruct]
+ -[NSPPrivacyProxyCostTokenKeyEntry copyTo:]
+ -[NSPPrivacyProxyCostTokenKeyEntry copyWithZone:]
+ -[NSPPrivacyProxyCostTokenKeyEntry description]
+ -[NSPPrivacyProxyCostTokenKeyEntry dictionaryRepresentation]
+ -[NSPPrivacyProxyCostTokenKeyEntry hasTransparencyEntry]
+ -[NSPPrivacyProxyCostTokenKeyEntry hasTransparencyProof]
+ -[NSPPrivacyProxyCostTokenKeyEntry hash]
+ -[NSPPrivacyProxyCostTokenKeyEntry isEqual:]
+ -[NSPPrivacyProxyCostTokenKeyEntry mergeFrom:]
+ -[NSPPrivacyProxyCostTokenKeyEntry readFrom:]
+ -[NSPPrivacyProxyCostTokenKeyEntry setTransparencyEntry:]
+ -[NSPPrivacyProxyCostTokenKeyEntry setTransparencyProof:]
+ -[NSPPrivacyProxyCostTokenKeyEntry transparencyEntry]
+ -[NSPPrivacyProxyCostTokenKeyEntry transparencyProof]
+ -[NSPPrivacyProxyCostTokenKeyEntry writeTo:]
+ -[NSPPrivacyProxyTransparencyCostTokenEntry .cxx_destruct]
+ -[NSPPrivacyProxyTransparencyCostTokenEntry copyTo:]
+ -[NSPPrivacyProxyTransparencyCostTokenEntry copyWithZone:]
+ -[NSPPrivacyProxyTransparencyCostTokenEntry description]
+ -[NSPPrivacyProxyTransparencyCostTokenEntry dictionaryRepresentation]
+ -[NSPPrivacyProxyTransparencyCostTokenEntry hasPublicKey]
+ -[NSPPrivacyProxyTransparencyCostTokenEntry hash]
+ -[NSPPrivacyProxyTransparencyCostTokenEntry isEqual:]
+ -[NSPPrivacyProxyTransparencyCostTokenEntry mergeFrom:]
+ -[NSPPrivacyProxyTransparencyCostTokenEntry publicKey]
+ -[NSPPrivacyProxyTransparencyCostTokenEntry readFrom:]
+ -[NSPPrivacyProxyTransparencyCostTokenEntry setPublicKey:]
+ -[NSPPrivacyProxyTransparencyCostTokenEntry writeTo:]
+ -[NSPPrivateAccessTokenFetcher fetchFromServerOnlyOncePerDay]
+ -[NSPPrivateAccessTokenFetcher getCachedTokenCountWithQueue:completionHandler:]
+ -[NSPPrivateAccessTokenFetcher prewarmTokenCacheToSize:withQueue:completionHandler:]
+ -[NSPPrivateAccessTokenFetcher setFetchFromServerOnlyOncePerDay:]
+ -[NSPServerClient getCachedTokenCountForFetcher:allowRetry:completionHandler:]
+ -[NSPServerClient handleCacheSizeReply:completionHandler:]
+ -[NSPServerClient prewarmTokenCacheForFetcher:]
+ -[NSPServerClient prewarmTokenCacheForFetcher:desiredCacheSize:allowRetry:completionHandler:]
+ GCC_except_table23
+ GCC_except_table52
+ _NSPPrivacyProxyCostTokenKeyConfigReadFrom
+ _NSPPrivacyProxyCostTokenKeyEntryReadFrom
+ _NSPPrivacyProxyTransparencyCostTokenEntryReadFrom
+ _NSPServerClientSetCacheRequestFields
+ _OBJC_CLASS_$_NSPPrivacyProxyCostTokenKeyConfig
+ _OBJC_CLASS_$_NSPPrivacyProxyCostTokenKeyEntry
+ _OBJC_CLASS_$_NSPPrivacyProxyTransparencyCostTokenEntry
+ _OBJC_IVAR_$_NSPPrivacyProxyCostTokenKeyConfig._entries
+ _OBJC_IVAR_$_NSPPrivacyProxyCostTokenKeyEntry._transparencyEntry
+ _OBJC_IVAR_$_NSPPrivacyProxyCostTokenKeyEntry._transparencyProof
+ _OBJC_IVAR_$_NSPPrivacyProxyTransparencyCostTokenEntry._publicKey
+ _OBJC_IVAR_$_NSPPrivateAccessTokenFetcher._fetchFromServerOnlyOncePerDay
+ _OBJC_METACLASS_$_NSPPrivacyProxyCostTokenKeyConfig
+ _OBJC_METACLASS_$_NSPPrivacyProxyCostTokenKeyEntry
+ _OBJC_METACLASS_$_NSPPrivacyProxyTransparencyCostTokenEntry
+ __OBJC_$_CLASS_METHODS_NSPPrivacyProxyCostTokenKeyConfig
+ __OBJC_$_INSTANCE_METHODS_NSPPrivacyProxyCostTokenKeyConfig
+ __OBJC_$_INSTANCE_METHODS_NSPPrivacyProxyCostTokenKeyEntry
+ __OBJC_$_INSTANCE_METHODS_NSPPrivacyProxyTransparencyCostTokenEntry
+ __OBJC_$_INSTANCE_VARIABLES_NSPPrivacyProxyCostTokenKeyConfig
+ __OBJC_$_INSTANCE_VARIABLES_NSPPrivacyProxyCostTokenKeyEntry
+ __OBJC_$_INSTANCE_VARIABLES_NSPPrivacyProxyTransparencyCostTokenEntry
+ __OBJC_$_PROP_LIST_NSPPrivacyProxyCostTokenKeyConfig
+ __OBJC_$_PROP_LIST_NSPPrivacyProxyCostTokenKeyEntry
+ __OBJC_$_PROP_LIST_NSPPrivacyProxyTransparencyCostTokenEntry
+ __OBJC_CLASS_PROTOCOLS_$_NSPPrivacyProxyCostTokenKeyConfig
+ __OBJC_CLASS_PROTOCOLS_$_NSPPrivacyProxyCostTokenKeyEntry
+ __OBJC_CLASS_PROTOCOLS_$_NSPPrivacyProxyTransparencyCostTokenEntry
+ __OBJC_CLASS_RO_$_NSPPrivacyProxyCostTokenKeyConfig
+ __OBJC_CLASS_RO_$_NSPPrivacyProxyCostTokenKeyEntry
+ __OBJC_CLASS_RO_$_NSPPrivacyProxyTransparencyCostTokenEntry
+ __OBJC_METACLASS_RO_$_NSPPrivacyProxyCostTokenKeyConfig
+ __OBJC_METACLASS_RO_$_NSPPrivacyProxyCostTokenKeyEntry
+ __OBJC_METACLASS_RO_$_NSPPrivacyProxyTransparencyCostTokenEntry
+ ___78-[NSPServerClient getCachedTokenCountForFetcher:allowRetry:completionHandler:]_block_invoke
+ ___79-[NSPPrivateAccessTokenFetcher getCachedTokenCountWithQueue:completionHandler:]_block_invoke
+ ___84-[NSPPrivateAccessTokenFetcher prewarmTokenCacheToSize:withQueue:completionHandler:]_block_invoke
+ ___93-[NSPServerClient prewarmTokenCacheForFetcher:desiredCacheSize:allowRetry:completionHandler:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e23_v24?0I8I12"NSError"16ls32l8
+ ___block_descriptor_48_e8_32s40bs_e20_v20?0I8"NSError"12ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e23_v24?0I8I12"NSError"16ls32l8s40l8
+ ___block_descriptor_52_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_61_e8_32s40s48bs_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8s40l8s48l8
+ _dispatch_queue_attr_make_with_autorelease_frequency
- +[NPUtilities totalDataInKeychainWithIdentifier:]
- GCC_except_table24
- GCC_except_table51
- _OBJC_IVAR_$_NSPPrivacyProxyAggregatorService._serviceURL
- _OBJC_IVAR_$_NSPPrivacyProxyAggregatorService._supportedUseCaseIdentifiers
- ___49-[NSPPrivateAccessTokenFetcher prewarmTokenCache]_block_invoke
- ___block_descriptor_40_e8_32s_e28_v24?0"NSData"8"NSError"16ls32l8
- _deviceClassIsHomepod
- _os_variant_has_internal_content
CStrings:
+ "-[NSPPrivateAccessTokenFetcher getCachedTokenCountWithQueue:completionHandler:]"
+ "-[NSPPrivateAccessTokenFetcher prewarmTokenCacheToSize:withQueue:completionHandler:]"
+ "Failed to get cached token count: %@"
+ "Failed to prewarm token cache: %@"
+ "Get cached token count got invalid connection, retrying"
+ "Getting cached Private Access Token count"
+ "NSPServerPrivateAccessTokenCacheCount"
+ "NSPServerPrivateAccessTokenDesiredCacheCount"
+ "NSPServerPrivateAccessTokenFetchedCount"
+ "NSPServerTokenFetchOnlyOncePerDay"
+ "Prewarm token cache got invalid connection, retrying"
+ "Prewarming Private Access Token cache to %u tokens"
+ "costTokenKeyConfig"
+ "entries"
+ "publicKey"
+ "transparencyEntry"
+ "v20@?0I8@\"NSError\"12"
+ "v24@?0I8I12@\"NSError\"16"
```
