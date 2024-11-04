## BusinessChatService

> `/System/Library/PrivateFrameworks/BusinessChatService.framework/BusinessChatService`

```diff

-30095.32.9.7.3
-  __TEXT.__text: 0x71d18
+30095.32.9.7.8
+  __TEXT.__text: 0x72dac
   __TEXT.__auth_stubs: 0xa00
-  __TEXT.__objc_methlist: 0x6fec
-  __TEXT.__const: 0x1f0
-  __TEXT.__cstring: 0x80ca
-  __TEXT.__oslogstring: 0x4524
-  __TEXT.__gcc_except_tab: 0xad4
+  __TEXT.__objc_methlist: 0x7064
+  __TEXT.__const: 0x1f8
+  __TEXT.__cstring: 0x8268
+  __TEXT.__oslogstring: 0x4602
+  __TEXT.__gcc_except_tab: 0xb28
   __TEXT.__ustring: 0x5b0
-  __TEXT.__unwind_info: 0x17e8
-  __TEXT.__objc_classname: 0x1709
-  __TEXT.__objc_methname: 0xde16
-  __TEXT.__objc_methtype: 0x30c9
-  __TEXT.__objc_stubs: 0x9740
+  __TEXT.__unwind_info: 0x1830
+  __TEXT.__objc_classname: 0x170b
+  __TEXT.__objc_methname: 0xdfb4
+  __TEXT.__objc_methtype: 0x3244
+  __TEXT.__objc_stubs: 0x97e0
   __DATA_CONST.__got: 0x408
-  __DATA_CONST.__const: 0x1b18
+  __DATA_CONST.__const: 0x1b90
   __DATA_CONST.__objc_classlist: 0x4b0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x2f8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3080
+  __DATA_CONST.__objc_selrefs: 0x30c8
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x390
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x510
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x2e0
-  __AUTH_CONST.__cfstring: 0x5cc0
-  __AUTH_CONST.__objc_const: 0x11fa8
+  __AUTH_CONST.__const: 0x300
+  __AUTH_CONST.__cfstring: 0x5d40
+  __AUTH_CONST.__objc_const: 0x120d8
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x5d4
+  __DATA.__objc_ivar: 0x5dc
   __DATA.__data: 0xdb90
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_ivar: 0x2b8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2611
-  Symbols:   3009
-  CStrings:  4278
+  Functions: 2626
+  Symbols:   3025
+  CStrings:  4308
 
Symbols:
+ _BCSErrorNotCachedCode
CStrings:
+ "\x06"
+ "%!s(MISSING) - Query is cache-only, skipping fetch for item of type: %!@(MISSING)"
+ "%!s(MISSING) shard item missing!!! - type: %!@(MISSING) --> triggering BACKGROUND download of megashard from server"
+ "-[BCSBusinessQueryController cachedBusinessMetadataForEmail:forClientBundleID:completion:]"
+ "-[BCSBusinessQueryService cachedBusinessMetadataForEmail:error:]"
+ "-[BCSConfigResolver configItemWithType:clientBundleID:cacheOnly:metric:completion:]"
+ "-[BCSConfigResolver configItemWithType:clientBundleID:cacheOnly:metric:completion:]_block_invoke"
+ "-[BCSConfigResolver configItemWithType:clientBundleID:cacheOnly:metric:completion:]_block_invoke_2"
+ "-[BCSShardResolver shardItemMatching:clientBundleID:cacheOnly:metric:completion:]"
+ "-[BCSShardResolver shardItemMatching:clientBundleID:cacheOnly:metric:completion:]_block_invoke"
+ "@\"<BCSXPCDaemonProtocol>\"24@0:8@?<v@?@\"NSError\">16"
+ "@24@0:8@?16"
+ "B24@0:8@\"<BCSCoalesceObjectProtocol>\"16"
+ "Batch exceeds maximum size (%!l(MISSING)d > %!l(MISSING)u)"
+ "Item not found in cache"
+ "New request is a scheduled duplicate and already in progress:%!s(MISSING)"
+ "Query is cache-only, skipping config fetch"
+ "Query is cache-only, skipping shard fetch"
+ "Request is a scheduled duplicate and already in progress"
+ "TB,N,V_cacheOnly"
+ "_cacheOnly"
+ "_serialQueue"
+ "cacheOnly"
+ "cachedBusinessMetadataForEmail:error:"
+ "cachedBusinessMetadataForEmail:forClientBundleID:completion:"
+ "com.apple.BusinessQueryService.serialqueue"
+ "configItemWithType:clientBundleID:cacheOnly:metric:completion:"
+ "initWithItemIdentifier:clientBundleId:shardType:cacheOnly:"
+ "isDuplicateRequest:"
+ "setCacheOnly:"
+ "shardItemMatching:clientBundleID:cacheOnly:metric:completion:"
+ "synchronousRemoteObjectProxyWithErrorHandler:"
+ "v52@0:8@\"<BCSShardItemIdentifying>\"16@\"NSString\"24B32@\"<BCSResolutionMetricProtocol>\"36@?<v@?@\"<BCSShardItemProtocol>\"@\"NSError\">44"
+ "v52@0:8@16@24B32@36@?44"
+ "v52@0:8q16@\"NSString\"24B32@\"<BCSResolutionMetricProtocol>\"36@?<v@?@\"BCSConfigItem\"@\"NSError\">44"
+ "v52@0:8q16@24B32@36@?44"
- "-[BCSConfigResolver configItemWithType:clientBundleID:metric:completion:]"
- "-[BCSConfigResolver configItemWithType:clientBundleID:metric:completion:]_block_invoke"
- "-[BCSConfigResolver configItemWithType:clientBundleID:metric:completion:]_block_invoke_2"
- "-[BCSShardResolver shardItemMatching:clientBundleID:metric:completion:]"
- "-[BCSShardResolver shardItemMatching:clientBundleID:metric:completion:]_block_invoke"
- "Batch exceeds maximum size (%!l(MISSING)d > %!l(MISSING)ld)"

```
