## IDSFoundation

> `/System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation`

```diff

-1814.200.71.2.7
-  __TEXT.__text: 0x1a9bc0
-  __TEXT.__auth_stubs: 0x2480
-  __TEXT.__objc_methlist: 0x14414
+1814.300.81.2.2
+  __TEXT.__text: 0x1aa84c
+  __TEXT.__auth_stubs: 0x24a0
+  __TEXT.__objc_methlist: 0x14574
   __TEXT.__const: 0x4f8
-  __TEXT.__oslogstring: 0x1fff4
-  __TEXT.__cstring: 0x292aa
-  __TEXT.__gcc_except_tab: 0x7864
+  __TEXT.__oslogstring: 0x2000d
+  __TEXT.__cstring: 0x29474
+  __TEXT.__gcc_except_tab: 0x7930
   __TEXT.__ustring: 0xc
   __TEXT.__dlopen_cstrs: 0xac
-  __TEXT.__unwind_info: 0x50e4
-  __TEXT.__objc_classname: 0x31bd
-  __TEXT.__objc_methname: 0x2d91b
-  __TEXT.__objc_methtype: 0x6a90
-  __TEXT.__objc_stubs: 0x172c0
+  __TEXT.__unwind_info: 0x512c
+  __TEXT.__objc_classname: 0x31ee
+  __TEXT.__objc_methname: 0x2db45
+  __TEXT.__objc_methtype: 0x6a9b
+  __TEXT.__objc_stubs: 0x17440
   __DATA_CONST.__got: 0x320
-  __DATA_CONST.__const: 0x51f0
-  __DATA_CONST.__objc_classlist: 0xcb8
+  __DATA_CONST.__const: 0x5268
+  __DATA_CONST.__objc_classlist: 0xcc8
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x256e0
-  __DATA_CONST.__objc_selrefs: 0x8ad8
+  __DATA_CONST.__objc_const: 0x258a0
+  __DATA_CONST.__objc_selrefs: 0x8b60
   __DATA_CONST.__objc_arraydata: 0x1460
-  __AUTH_CONST.__objc_const: 0x9948
-  __AUTH_CONST.__const: 0x1700
-  __AUTH_CONST.__cfstring: 0x25280
+  __AUTH_CONST.__objc_const: 0x9a68
+  __AUTH_CONST.__const: 0x1720
+  __AUTH_CONST.__cfstring: 0x25440
   __AUTH_CONST.__auth_ptr: 0x38
   __AUTH_CONST.__objc_intobj: 0xa98
   __AUTH_CONST.__objc_arrayobj: 0x1e18
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0x1250
-  __AUTH.__objc_data: 0x6cc0
+  __AUTH_CONST.__auth_got: 0x1260
+  __AUTH.__objc_data: 0x6d60
   __DATA.__objc_protorefs: 0x30
-  __DATA.__objc_classrefs: 0xa20
-  __DATA.__objc_superrefs: 0x940
-  __DATA.__objc_ivar: 0x209c
+  __DATA.__objc_classrefs: 0xa28
+  __DATA.__objc_superrefs: 0x950
+  __DATA.__objc_ivar: 0x20b4
   __DATA.__data: 0x1620
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x6b8
+  __DATA.__bss: 0x6c8
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x1270
   __DATA_DIRTY.__bss: 0x180

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 8349
-  Symbols:   4161
-  CStrings:  16335
+  Functions: 8376
+  Symbols:   4173
+  CStrings:  16384
 
Symbols:
+ OBJC_IVAR_$_IDSInterfaceAddress._clat46
+ _IDSDSessionReportLocalIPVersionKey
+ _IDSDeliveryForceQueryKey
+ _IDSQuickRelayUserTypeKey
+ _OBJC_CLASS_$_IDSCacheClearRequest
+ _OBJC_CLASS_$_IDSCacheClearRequestContext
+ _OBJC_METACLASS_$_IDSCacheClearRequest
+ _OBJC_METACLASS_$_IDSCacheClearRequestContext
+ _kIDSForceQuerySendParameterEntitlement
+ _kIDSKeyTransparencyCacheClearRequestEntitlement
+ _nw_connection_copy_connected_local_endpoint
+ _objc_retain_x11
CStrings:
+ "<%@: %p verifierResult: %@, ticket: %@, accountKey: %@, queryResponseTime: %@>, ktOptInStatus: %@"
+ "B\x11\x13!\x12\x12"
+ "IDSCacheClearRequest"
+ "IDSCacheClearRequestContext"
+ "IDSSendParametersForceQueryKey"
+ "IDSSendParametersQuickRelayUserTypeKey"
+ "LIPV"
+ "Null context"
+ "OptInStatus"
+ "RequestContextKey"
+ "S24@0:8@16"
+ "T@\"NSArray\",&,N,V_requestContexts"
+ "T@\"NSArray\",&,N,V_uris"
+ "T@\"NSObject<OS_nw_endpoint>\",&,N,V_localEndpoint"
+ "T@\"NSObject<OS_nw_endpoint>\",R,N,V_cachedH2LocalEndpoint"
+ "T@\"NSString\",&,N,V_service"
+ "TB,R,N,V_clat46"
+ "TQ,R,N,V_ktOptIn"
+ "_cachedH2LocalEndpoint"
+ "_clat46"
+ "_generateTransportScoreCard: skipping %@ which is a simualted IPv4 interface!"
+ "_getConnectedLocalPortAndSetLocalEndpointForConnection:"
+ "_ktOptIn"
+ "_requestContexts"
+ "_uris"
+ "abtout"
+ "allocBindRequestTimeOut"
+ "cachedH2LocalEndpoint"
+ "clat46"
+ "com.apple.private.ids.force-query-send-option-allowed"
+ "com.apple.private.ids.key-transparency.cache-clear-request"
+ "connectTCP: got local endpoint: %u"
+ "connectTCP: unable to get local endpoint from the connected connection!"
+ "force-query"
+ "forceQuery"
+ "h2fdv2"
+ "has_quickRelayUserType"
+ "initWithVerifierResult:ticket:accountKey:queryResponseTime:ktOptIn:"
+ "ktOptIn"
+ "pkt"
+ "qtu"
+ "quickRelayUserType"
+ "receivedFirstPacketTime:"
+ "receivedFromGFT2"
+ "recvGFT2"
+ "requestContexts"
+ "serviceKey"
+ "setForceQuery:"
+ "setLocalEndpoint:"
+ "setQuickRelayUserType:"
+ "setRequestContexts:"
+ "setUris:"
+ "und2"
+ "uris"
+ "urisKey"
+ "v24@?0B8B12B16S20"
- "<%@: %p verifierResult: %@, ticket: %@, accountKey: %@, queryResponseTime: %@>"
- "B\x11\x12!\x12\x12"
- "T@\"NSObject<OS_nw_endpoint>\",R,N,V_localEndpoint"
- "filter out simulated IPv4 interface [if:%s type:%d]."
- "h2fd"
- "initWithVerifierResult:ticket:accountKey:queryResponseTime:"
- "und"

```
