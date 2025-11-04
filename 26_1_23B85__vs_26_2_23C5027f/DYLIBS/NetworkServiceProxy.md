## NetworkServiceProxy

> `/System/Library/PrivateFrameworks/NetworkServiceProxy.framework/NetworkServiceProxy`

```diff

-921.40.2.0.1
-  __TEXT.__text: 0x51d54
+921.60.3.502.1
+  __TEXT.__text: 0x5207c
   __TEXT.__auth_stubs: 0xd50
-  __TEXT.__objc_methlist: 0x4c34
+  __TEXT.__objc_methlist: 0x4c64
   __TEXT.__const: 0x360
   __TEXT.__gcc_except_tab: 0x90
-  __TEXT.__cstring: 0x5619
+  __TEXT.__cstring: 0x5647
   __TEXT.__oslogstring: 0x305e
-  __TEXT.__unwind_info: 0xe58
+  __TEXT.__unwind_info: 0xe60
   __TEXT.__objc_classname: 0x607
-  __TEXT.__objc_methname: 0x9aaa
-  __TEXT.__objc_methtype: 0x1391
-  __TEXT.__objc_stubs: 0x53a0
+  __TEXT.__objc_methname: 0x9b14
+  __TEXT.__objc_methtype: 0x13eb
+  __TEXT.__objc_stubs: 0x53c0
   __DATA_CONST.__got: 0x3d8
   __DATA_CONST.__const: 0xc40
   __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x23b8
+  __DATA_CONST.__objc_selrefs: 0x23d8
   __DATA_CONST.__objc_superrefs: 0x178
   __DATA_CONST.__objc_arraydata: 0x48
   __AUTH_CONST.__auth_got: 0x6c0
   __AUTH_CONST.__const: 0x180
-  __AUTH_CONST.__cfstring: 0x4b20
-  __AUTH_CONST.__objc_const: 0x6798
+  __AUTH_CONST.__cfstring: 0x4b40
+  __AUTH_CONST.__objc_const: 0x67d8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28

   __DATA.__data: 0x268
   __DATA.__common: 0x1
   __DATA.__bss: 0x10
-  __DATA_DIRTY.__objc_ivar: 0x240
+  __DATA_DIRTY.__objc_ivar: 0x244
   __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__bss: 0xa8
   __DATA_DIRTY.__common: 0x20

   - /usr/lib/libboringssl.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8A195057-0C8A-3CB3-97D0-EB1D928D78E9
-  Functions: 1710
-  Symbols:   5074
-  CStrings:  3662
+  UUID: 7D74F341-C6AE-3AF5-9AEF-FA121D54FB12
+  Functions: 1715
+  Symbols:   5083
+  CStrings:  3672
 
Symbols:
+ -[NSPPrivacyProxyProxiedContentMap allowFailover]
+ -[NSPPrivacyProxyProxiedContentMap hasAllowFailover]
+ -[NSPPrivacyProxyProxiedContentMap setAllowFailover:]
+ -[NSPPrivacyProxyProxiedContentMap setHasAllowFailover:]
+ ___80-[NSPPrivateAccessTokenFetcher handleTokenResponse:withQueue:completionHandler:]_block_invoke.210
+ ___83-[NSPPrivateAccessTokenFetcher checkRemainingCostQuotaWithQueue:completionHandler:]_block_invoke.211
+ ___87-[NSPPrivateAccessTokenFetcher generateTokenRequestForKey:withQueue:completionHandler:]_block_invoke.193
+ ___87-[NSPPrivateAccessTokenFetcher generateTokenRequestForKey:withQueue:completionHandler:]_block_invoke.197
+ ___block_descriptor_56_e8_32s40s48bs_e31_v28?0"NSData"8I16"NSError"20ls32l8s48l8s40l8
+ _objc_msgSend$setAllowFailover:
- ___80-[NSPPrivateAccessTokenFetcher handleTokenResponse:withQueue:completionHandler:]_block_invoke.209
- ___83-[NSPPrivateAccessTokenFetcher checkRemainingCostQuotaWithQueue:completionHandler:]_block_invoke.210
- ___87-[NSPPrivateAccessTokenFetcher generateTokenRequestForKey:withQueue:completionHandler:]_block_invoke.194
- ___87-[NSPPrivateAccessTokenFetcher generateTokenRequestForKey:withQueue:completionHandler:]_block_invoke.198
- ___block_descriptor_56_e8_32s40s48bs_e28_v24?0"NSData"8"NSError"16ls32l8s48l8s40l8
CStrings:
+ "TB,N,V_allowFailover"
+ "_allowFailover"
+ "allowFailover"
+ "hasAllowFailover"
+ "setAllowFailover:"
+ "setHasAllowFailover:"
+ "v28@?0@\"NSData\"8I16@\"NSError\"20"
+ "v36@0:8@\"NSPPrivateAccessTokenFetcher\"16B24@?<v@?@\"NSData\"I@\"NSError\">28"
+ "{?=\"percentEnabled\"b1\"resolver\"b1\"allowFailover\"b1\"isPrivacyProxy\"b1\"matchExactHostnames\"b1\"supportsReverseProxying\"b1\"systemProcessOnly\"b1}"
- "{?=\"percentEnabled\"b1\"resolver\"b1\"isPrivacyProxy\"b1\"matchExactHostnames\"b1\"supportsReverseProxying\"b1\"systemProcessOnly\"b1}"

```
