## BusinessChatService

> `/System/Library/PrivateFrameworks/BusinessChatService.framework/Versions/A/BusinessChatService`

```diff

-30123.20.6.2.1
-  __TEXT.__text: 0x765f8
-  __TEXT.__objc_methlist: 0x8ddc
+30123.21.8.11.4
+  __TEXT.__text: 0x773dc
+  __TEXT.__objc_methlist: 0x8e14
   __TEXT.__const: 0x298
-  __TEXT.__cstring: 0x867e
-  __TEXT.__oslogstring: 0x5009
-  __TEXT.__gcc_except_tab: 0x5cc
-  __TEXT.__unwind_info: 0x16c0
+  __TEXT.__cstring: 0x869c
+  __TEXT.__oslogstring: 0x50e2
+  __TEXT.__gcc_except_tab: 0x6a8
+  __TEXT.__unwind_info: 0x16e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x2f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3260
+  __DATA_CONST.__objc_selrefs: 0x3288
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x390
   __DATA_CONST.__got: 0x498
-  __AUTH_CONST.__const: 0x1980
+  __AUTH_CONST.__const: 0x19e0
   __AUTH_CONST.__cfstring: 0x4aa0
-  __AUTH_CONST.__objc_const: 0x10738
+  __AUTH_CONST.__objc_const: 0x10760
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x470
   __AUTH_CONST.__auth_ptr: 0x0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2769
-  Symbols:   6567
-  CStrings:  1310
+  Functions: 2776
+  Symbols:   6581
+  CStrings:  1313
 
Symbols:
+ -[BCSBusinessEmailItemIdentifier itemIdentifiers]
+ -[BCSBusinessLookupResult initWithHasBusiness:matchingTruncatedHash:itemIdentifier:config:]
+ -[BCSBusinessQueryController fetchBusinessItemWithPhoneNumber:forClientBundleID:cacheOnly:completion:]
+ -[BCSBusinessQueryController fetchItemWithQuery:cacheOnly:completion:]
+ -[BCSBusinessQueryService cachedBusinessItemWithPhoneNumber:completion:]
+ GCC_except_table114
+ GCC_except_table44
+ GCC_except_table64
+ GCC_except_table78
+ GCC_except_table84
+ GCC_except_table91
+ __70-[BCSBusinessQueryController fetchItemWithQuery:cacheOnly:completion:]_block_invoke
+ __99-[BCSBusinessQueryController fetchBusinessMetadataForEmailIdentifier:forClientBundleID:completion:]_block_invoke
+ ___102-[BCSBusinessQueryController fetchBusinessItemWithPhoneNumber:forClientBundleID:cacheOnly:completion:]_block_invoke
+ ___70-[BCSBusinessQueryController fetchItemWithQuery:cacheOnly:completion:]_block_invoke
+ ___block_descriptor_48_e8_32r40r_e54_B32?0"<BCSItemIdentifying>"8"BCSItem"16"NSError"24l
+ ___block_descriptor_56_e8_32bs40r48r_e17_v16?0"NSError"8l
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e34_v24?0"NSDictionary"8"NSError"16l
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$fetchBusinessItemWithPhoneNumber:forClientBundleID:cacheOnly:completion:
+ _objc_msgSend$fetchItemWithQuery:cacheOnly:completion:
+ _objc_msgSend$initWithHasBusiness:matchingTruncatedHash:itemIdentifier:config:
- GCC_except_table108
- GCC_except_table43
- GCC_except_table61
- GCC_except_table85
- __60-[BCSBusinessQueryController fetchItemWithQuery:completion:]_block_invoke
- ___60-[BCSBusinessQueryController fetchItemWithQuery:completion:]_block_invoke
- ___92-[BCSBusinessQueryController fetchBusinessItemWithPhoneNumber:forClientBundleID:completion:]_block_invoke
- ___block_descriptor_64_e8_32s40s48s56bs_e34_v24?0"NSDictionary"8"NSError"16l
CStrings:
+ "%s - Cache only lookup. Did not find item in cache - type: %@"
+ "%s Expected shardItem that conforms to BCSFilterShardItemProtocol protocol but got %@"
+ "-[BCSBusinessQueryController fetchBusinessItemWithPhoneNumber:forClientBundleID:cacheOnly:completion:]"
+ "-[BCSBusinessQueryController fetchItemWithQuery:cacheOnly:completion:]"
+ "-[BCSBusinessQueryController fetchItemWithQuery:cacheOnly:completion:]_block_invoke"
+ "Extracting all matching shards for %lu keys for multi-key identifier"
- "-[BCSBusinessQueryController fetchBusinessItemWithPhoneNumber:forClientBundleID:completion:]"
- "-[BCSBusinessQueryController fetchItemWithQuery:completion:]"
- "-[BCSBusinessQueryController fetchItemWithQuery:completion:]_block_invoke"
```
