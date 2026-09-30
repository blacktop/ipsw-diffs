## BusinessChatService

> `/System/Library/PrivateFrameworks/BusinessChatService.framework/BusinessChatService`

```diff

-30123.31.8.11.3
-  __TEXT.__text: 0x6be8c
-  __TEXT.__objc_methlist: 0x797c
+30123.31.8.11.4
+  __TEXT.__text: 0x6c154
+  __TEXT.__objc_methlist: 0x79a4
   __TEXT.__const: 0x248
-  __TEXT.__cstring: 0x8bd2
-  __TEXT.__oslogstring: 0x4fe7
+  __TEXT.__cstring: 0x8c39
+  __TEXT.__oslogstring: 0x5025
   __TEXT.__gcc_except_tab: 0x728
-  __TEXT.__unwind_info: 0x1a70
+  __TEXT.__unwind_info: 0x1a78
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x308
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2788
+  __DATA_CONST.__objc_selrefs: 0x2798
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x388
   __DATA_CONST.__got: 0x480
   __AUTH_CONST.__const: 0x220
   __AUTH_CONST.__cfstring: 0x4a20
-  __AUTH_CONST.__objc_const: 0xfdd8
+  __AUTH_CONST.__objc_const: 0xfde0
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x4f0
   __DATA.__objc_ivar: 0x510

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2388
-  Symbols:   5885
-  CStrings:  1321
+  Functions: 2392
+  Symbols:   5890
+  CStrings:  1323
 
Symbols:
+ -[BCSBusinessQueryController fetchBusinessItemWithPhoneNumber:forClientBundleID:cacheOnly:completion:]
+ -[BCSBusinessQueryController fetchItemWithQuery:cacheOnly:completion:]
+ -[BCSBusinessQueryService cachedBusinessItemWithPhoneNumber:completion:]
+ GCC_except_table102
+ GCC_except_table57
+ GCC_except_table62
+ GCC_except_table73
+ GCC_except_table77
+ GCC_except_table84
+ ___102-[BCSBusinessQueryController fetchBusinessItemWithPhoneNumber:forClientBundleID:cacheOnly:completion:]_block_invoke
+ ___70-[BCSBusinessQueryController fetchItemWithQuery:cacheOnly:completion:]_block_invoke
+ ___72-[BCSBusinessQueryService cachedBusinessItemWithPhoneNumber:completion:]_block_invoke
+ _objc_msgSend$fetchBusinessItemWithPhoneNumber:forClientBundleID:cacheOnly:completion:
- GCC_except_table100
- GCC_except_table55
- GCC_except_table60
- GCC_except_table71
- GCC_except_table75
- GCC_except_table82
- ___60-[BCSBusinessQueryController fetchItemWithQuery:completion:]_block_invoke
- ___92-[BCSBusinessQueryController fetchBusinessItemWithPhoneNumber:forClientBundleID:completion:]_block_invoke
CStrings:
+ "%s - Cache only lookup. Did not find item in cache - type: %@"
+ "-[BCSBusinessQueryController fetchBusinessItemWithPhoneNumber:forClientBundleID:cacheOnly:completion:]"
+ "-[BCSBusinessQueryController fetchItemWithQuery:cacheOnly:completion:]"
+ "-[BCSBusinessQueryController fetchItemWithQuery:cacheOnly:completion:]_block_invoke"
+ "-[BCSBusinessQueryService cachedBusinessItemWithPhoneNumber:completion:]"
- "-[BCSBusinessQueryController fetchBusinessItemWithPhoneNumber:forClientBundleID:completion:]"
- "-[BCSBusinessQueryController fetchItemWithQuery:completion:]"
- "-[BCSBusinessQueryController fetchItemWithQuery:completion:]_block_invoke"
```
