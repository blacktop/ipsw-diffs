## NetworkServiceProxy

> `/System/Library/PrivateFrameworks/NetworkServiceProxy.framework/NetworkServiceProxy`

```diff

-921.60.5.0.0
-  __TEXT.__text: 0x520c4
-  __TEXT.__auth_stubs: 0xd50
-  __TEXT.__objc_methlist: 0x4c64
+921.100.18.0.0
+  __TEXT.__text: 0x5675c
+  __TEXT.__auth_stubs: 0xd20
+  __TEXT.__objc_methlist: 0x4dac
   __TEXT.__const: 0x360
-  __TEXT.__gcc_except_tab: 0x90
-  __TEXT.__cstring: 0x5647
-  __TEXT.__oslogstring: 0x305e
-  __TEXT.__unwind_info: 0xe60
-  __TEXT.__objc_classname: 0x607
-  __TEXT.__objc_methname: 0x9b14
-  __TEXT.__objc_methtype: 0x13eb
-  __TEXT.__objc_stubs: 0x53c0
-  __DATA_CONST.__got: 0x3e0
+  __TEXT.__gcc_except_tab: 0x8c
+  __TEXT.__cstring: 0x566c
+  __TEXT.__oslogstring: 0x3082
+  __TEXT.__unwind_info: 0x11d8
+  __TEXT.__objc_classname: 0x626
+  __TEXT.__objc_methname: 0x9c60
+  __TEXT.__objc_methtype: 0x145a
+  __TEXT.__objc_stubs: 0x5420
+  __DATA_CONST.__got: 0x3e8
   __DATA_CONST.__const: 0xc40
-  __DATA_CONST.__objc_classlist: 0x198
+  __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x23d8
-  __DATA_CONST.__objc_superrefs: 0x178
+  __DATA_CONST.__objc_selrefs: 0x2430
+  __DATA_CONST.__objc_superrefs: 0x180
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x6c0
+  __AUTH_CONST.__auth_got: 0x6a8
   __AUTH_CONST.__const: 0x180
-  __AUTH_CONST.__cfstring: 0x4b40
-  __AUTH_CONST.__objc_const: 0x67d8
+  __AUTH_CONST.__cfstring: 0x4ba0
+  __AUTH_CONST.__objc_const: 0x69b8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0xe60
+  __AUTH.__objc_data: 0xeb0
   __DATA.__objc_ivar: 0x2e0
   __DATA.__data: 0x268
   __DATA.__common: 0x1
   __DATA.__bss: 0x10
-  __DATA_DIRTY.__objc_ivar: 0x244
+  __DATA_DIRTY.__objc_ivar: 0x258
   __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__bss: 0xa8
   __DATA_DIRTY.__common: 0x20

   - /usr/lib/libboringssl.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 63CA4E1B-28F6-337D-BD83-B3D2E17C4270
-  Functions: 1715
-  Symbols:   5084
-  CStrings:  3672
+  UUID: 76AD13FF-CD85-3C5D-B95F-8B837A945BF5
+  Functions: 1741
+  Symbols:   5144
+  CStrings:  3700
 
Symbols:
+ -[NSPPrivacyProxyConfiguration edgeProbeConfig]
+ -[NSPPrivacyProxyConfiguration hasEdgeProbeConfig]
+ -[NSPPrivacyProxyConfiguration setEdgeProbeConfig:]
+ -[NSPPrivacyProxyEdgeProbeConfig .cxx_destruct]
+ -[NSPPrivacyProxyEdgeProbeConfig copyTo:]
+ -[NSPPrivacyProxyEdgeProbeConfig copyWithZone:]
+ -[NSPPrivacyProxyEdgeProbeConfig description]
+ -[NSPPrivacyProxyEdgeProbeConfig dictionaryRepresentation]
+ -[NSPPrivacyProxyEdgeProbeConfig enabled]
+ -[NSPPrivacyProxyEdgeProbeConfig hasEnabled]
+ -[NSPPrivacyProxyEdgeProbeConfig hasProbeDenominator]
+ -[NSPPrivacyProxyEdgeProbeConfig hasUrl]
+ -[NSPPrivacyProxyEdgeProbeConfig hash]
+ -[NSPPrivacyProxyEdgeProbeConfig isEqual:]
+ -[NSPPrivacyProxyEdgeProbeConfig mergeFrom:]
+ -[NSPPrivacyProxyEdgeProbeConfig probeDenominator]
+ -[NSPPrivacyProxyEdgeProbeConfig readFrom:]
+ -[NSPPrivacyProxyEdgeProbeConfig setEnabled:]
+ -[NSPPrivacyProxyEdgeProbeConfig setHasEnabled:]
+ -[NSPPrivacyProxyEdgeProbeConfig setHasProbeDenominator:]
+ -[NSPPrivacyProxyEdgeProbeConfig setProbeDenominator:]
+ -[NSPPrivacyProxyEdgeProbeConfig setUrl:]
+ -[NSPPrivacyProxyEdgeProbeConfig url]
+ -[NSPPrivacyProxyEdgeProbeConfig writeTo:]
+ -[NSPServerClient flushTokensFromCacheForFetcher:]
+ _NSPPrivacyProxyEdgeProbeConfigReadFrom
+ _OBJC_CLASS_$_NSPPrivacyProxyEdgeProbeConfig
+ _OBJC_METACLASS_$_NSPPrivacyProxyEdgeProbeConfig
+ __OBJC_$_INSTANCE_METHODS_NSPPrivacyProxyEdgeProbeConfig
+ __OBJC_$_INSTANCE_VARIABLES_NSPPrivacyProxyEdgeProbeConfig
+ __OBJC_$_PROP_LIST_NSPPrivacyProxyEdgeProbeConfig
+ __OBJC_CLASS_PROTOCOLS_$_NSPPrivacyProxyEdgeProbeConfig
+ __OBJC_CLASS_RO_$_NSPPrivacyProxyEdgeProbeConfig
+ __OBJC_METACLASS_RO_$_NSPPrivacyProxyEdgeProbeConfig
+ _memcmp
+ _objc_msgSend$setEdgeProbeConfig:
+ _objc_msgSend$setProbeDenominator:
+ _objc_msgSend$setUrl:
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
CStrings:
+ "@\"NSPPrivacyProxyEdgeProbeConfig\""
+ "Flushing One Time Tokens from cache"
+ "NSPPrivacyProxyEdgeProbeConfig"
+ "T@\"NSPPrivacyProxyEdgeProbeConfig\",&,N,V_edgeProbeConfig"
+ "T@\"NSString\",&,N,V_url"
+ "TI,N,V_probeDenominator"
+ "_edgeProbeConfig"
+ "_probeDenominator"
+ "_url"
+ "edgeProbeConfig"
+ "flushTokensFromCacheForFetcher:"
+ "hasEdgeProbeConfig"
+ "hasProbeDenominator"
+ "hasUrl"
+ "probeDenominator"
+ "setEdgeProbeConfig:"
+ "setHasProbeDenominator:"
+ "setProbeDenominator:"
+ "setUrl:"
+ "url"
+ "v24@0:8@\"NSPPrivateAccessTokenFetcher\"16"
+ "{?=\"probeDenominator\"b1\"enabled\"b1}"

```
