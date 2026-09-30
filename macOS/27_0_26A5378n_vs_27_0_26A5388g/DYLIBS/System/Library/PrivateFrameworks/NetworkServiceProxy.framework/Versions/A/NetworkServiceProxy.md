## NetworkServiceProxy

> `/System/Library/PrivateFrameworks/NetworkServiceProxy.framework/Versions/A/NetworkServiceProxy`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-976.0.0.0.0
-  __TEXT.__text: 0x65790
-  __TEXT.__objc_methlist: 0x5dcc
-  __TEXT.__const: 0x370
+980.0.0.0.0
+  __TEXT.__text: 0x67d40
+  __TEXT.__objc_methlist: 0x5fec
+  __TEXT.__const: 0x378
   __TEXT.__gcc_except_tab: 0xb4
-  __TEXT.__cstring: 0x59fe
-  __TEXT.__oslogstring: 0x31b9
-  __TEXT.__unwind_info: 0x1188
+  __TEXT.__cstring: 0x5ac9
+  __TEXT.__oslogstring: 0x336e
+  __TEXT.__unwind_info: 0x11e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x628
-  __DATA_CONST.__objc_classlist: 0x210
+  __DATA_CONST.__objc_classlist: 0x220
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x28a0
-  __DATA_CONST.__objc_superrefs: 0x1f8
+  __DATA_CONST.__objc_selrefs: 0x29e0
+  __DATA_CONST.__objc_superrefs: 0x208
   __DATA_CONST.__objc_arraydata: 0x48
-  __DATA_CONST.__got: 0x460
+  __DATA_CONST.__got: 0x480
   __AUTH_CONST.__const: 0x8e0
-  __AUTH_CONST.__cfstring: 0x4fa0
-  __AUTH_CONST.__objc_const: 0x7ce8
+  __AUTH_CONST.__cfstring: 0x5140
+  __AUTH_CONST.__objc_const: 0x80a0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x618
-  __AUTH.__objc_data: 0x1360
-  __DATA.__objc_ivar: 0x31c
+  __AUTH_CONST.__auth_got: 0x620
+  __AUTH.__objc_data: 0x1400
+  __DATA.__objc_ivar: 0x334
   __DATA.__data: 0x268
   __DATA.__common: 0x1
   __DATA.__bss: 0x10
-  __DATA_DIRTY.__objc_ivar: 0x2c0
+  __DATA_DIRTY.__objc_ivar: 0x2d8
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__bss: 0x98
   __DATA_DIRTY.__common: 0x20

   - /usr/lib/libboringssl.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2094
-  Symbols:   3977
-  CStrings:  1200
+  Functions: 2139
+  Symbols:   4065
+  CStrings:  1223
 
Symbols:
+ +[NSPJSONWebToken base64URLStringFromData:]
+ +[NSPJSONWebToken dataFromBase64URLString:]
+ +[NSPJSONWebToken jsonDictionaryFromBase64URLString:]
+ +[NSPPrivateAccessTokenFetcher selectDenominationTokensToRequestForCostTokenTotal:denominationValues:]
+ -[NSPJSONWebToken .cxx_destruct]
+ -[NSPJSONWebToken derEncodedSignatureFromRaw:]
+ -[NSPJSONWebToken derIntegerFromUnsigned:]
+ -[NSPJSONWebToken descriptionWithIndent:options:]
+ -[NSPJSONWebToken description]
+ -[NSPJSONWebToken encodedString]
+ -[NSPJSONWebToken headerSegment]
+ -[NSPJSONWebToken header]
+ -[NSPJSONWebToken initWithHeader:payload:]
+ -[NSPJSONWebToken initWithString:requireSignature:]
+ -[NSPJSONWebToken payloadSegment]
+ -[NSPJSONWebToken payload]
+ -[NSPJSONWebToken signatureData]
+ -[NSPJSONWebToken signatureVerified]
+ -[NSPJSONWebToken verifyWithKey:]
+ -[NSPPrivacyProxyAuxiliaryAuthInfo aggregatedCount]
+ -[NSPPrivacyProxyAuxiliaryAuthInfo hasAggregatedCount]
+ -[NSPPrivacyProxyAuxiliaryAuthInfo setAggregatedCount:]
+ -[NSPPrivacyProxyAuxiliaryAuthInfo setHasAggregatedCount:]
+ -[NSPPrivacyProxyCacheConfig batchSize]
+ -[NSPPrivacyProxyCacheConfig copyTo:]
+ -[NSPPrivacyProxyCacheConfig copyWithZone:]
+ -[NSPPrivacyProxyCacheConfig description]
+ -[NSPPrivacyProxyCacheConfig dictionaryRepresentation]
+ -[NSPPrivacyProxyCacheConfig hasBatchSize]
+ -[NSPPrivacyProxyCacheConfig hasLowWatermark]
+ -[NSPPrivacyProxyCacheConfig hash]
+ -[NSPPrivacyProxyCacheConfig isEqual:]
+ -[NSPPrivacyProxyCacheConfig lowWatermark]
+ -[NSPPrivacyProxyCacheConfig mergeFrom:]
+ -[NSPPrivacyProxyCacheConfig readFrom:]
+ -[NSPPrivacyProxyCacheConfig setBatchSize:]
+ -[NSPPrivacyProxyCacheConfig setHasBatchSize:]
+ -[NSPPrivacyProxyCacheConfig setHasLowWatermark:]
+ -[NSPPrivacyProxyCacheConfig setLowWatermark:]
+ -[NSPPrivacyProxyCacheConfig writeTo:]
+ -[NSPPrivacyProxyTokenIssuer hasTokenCacheConfig]
+ -[NSPPrivacyProxyTokenIssuer setTokenCacheConfig:]
+ -[NSPPrivacyProxyTokenIssuer tokenCacheConfig]
+ OBJC_IVAR_$_NSPJSONWebToken._header
+ OBJC_IVAR_$_NSPJSONWebToken._headerSegment
+ OBJC_IVAR_$_NSPJSONWebToken._payload
+ OBJC_IVAR_$_NSPJSONWebToken._payloadSegment
+ OBJC_IVAR_$_NSPJSONWebToken._signatureData
+ OBJC_IVAR_$_NSPJSONWebToken._signatureVerified
+ _NSPPrivacyProxyCacheConfigReadFrom
+ _OBJC_CLASS_$_NSPJSONWebToken
+ _OBJC_CLASS_$_NSPPrivacyProxyCacheConfig
+ _OBJC_CLASS_$_NSSortDescriptor
+ _OBJC_METACLASS_$_NSPJSONWebToken
+ _OBJC_METACLASS_$_NSPPrivacyProxyCacheConfig
+ __OBJC_$_CLASS_METHODS_NSPJSONWebToken
+ __OBJC_$_INSTANCE_METHODS_NSPJSONWebToken
+ __OBJC_$_INSTANCE_METHODS_NSPPrivacyProxyCacheConfig
+ __OBJC_$_INSTANCE_VARIABLES_NSPJSONWebToken
+ __OBJC_$_INSTANCE_VARIABLES_NSPPrivacyProxyCacheConfig
+ __OBJC_$_PROP_LIST_NSPJSONWebToken
+ __OBJC_$_PROP_LIST_NSPPrivacyProxyCacheConfig
+ __OBJC_CLASS_PROTOCOLS_$_NSPPrivacyProxyCacheConfig
+ __OBJC_CLASS_RO_$_NSPJSONWebToken
+ __OBJC_CLASS_RO_$_NSPPrivacyProxyCacheConfig
+ __OBJC_METACLASS_RO_$_NSPJSONWebToken
+ __OBJC_METACLASS_RO_$_NSPPrivacyProxyCacheConfig
+ ___NSArray0__struct
+ _arc4random_uniform
+ _objc_msgSend$JSONObjectWithData:options:error:
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$array
+ _objc_msgSend$base64URLStringFromData:
+ _objc_msgSend$dataFromBase64URLString:
+ _objc_msgSend$dataUsingEncoding:
+ _objc_msgSend$derEncodedSignatureFromRaw:
+ _objc_msgSend$derIntegerFromUnsigned:
+ _objc_msgSend$header
+ _objc_msgSend$initWithBase64EncodedString:options:
+ _objc_msgSend$jsonDictionaryFromBase64URLString:
+ _objc_msgSend$payload
+ _objc_msgSend$replaceOccurrencesOfString:withString:options:range:
+ _objc_msgSend$setBatchSize:
+ _objc_msgSend$setLowWatermark:
+ _objc_msgSend$setTokenCacheConfig:
+ _objc_msgSend$sortDescriptorWithKey:ascending:
+ _objc_msgSend$sortUsingDescriptors:
+ _objc_msgSend$sortedArrayUsingDescriptors:
CStrings:
+ "\t"
+ "%@.%@"
+ "%@.%@.%@"
+ "%s called with null (!requireSignature || segments.count >= 3)"
+ "%s called with null (jwtString.length > 0)"
+ "%s called with null (localWaitingTokens.count > 0)"
+ "%s called with null (segments.count >= 2 && segments.count <= 3)"
+ "%s called with null [NSJSONSerialization isValidJSONObject:header]"
+ "%s called with null [NSJSONSerialization isValidJSONObject:payload]"
+ "%s called with null [header isKindOfClass:[NSDictionary class]]"
+ "%s called with null [payload isKindOfClass:[NSDictionary class]]"
+ "+"
+ "-"
+ "-[NSPJSONWebToken initWithHeader:payload:]"
+ "-[NSPJSONWebToken initWithString:requireSignature:]"
+ "/"
+ "Header"
+ "Payload"
+ "_"
+ "aggregatedCount"
+ "batchSize"
+ "doubleValue"
+ "lowWatermark"
+ "tokenCacheConfig"
- "%s called with null (waitingTokenList.count > 0)"
```
