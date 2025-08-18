## SystemStatusServer

> `/System/Library/PrivateFrameworks/SystemStatusServer.framework/SystemStatusServer`

```diff

-248.100.0.0.0
-  __TEXT.__text: 0x1dce8
-  __TEXT.__auth_stubs: 0x720
-  __TEXT.__objc_methlist: 0x1be0
+248.101.0.0.0
+  __TEXT.__text: 0x1d29c
+  __TEXT.__auth_stubs: 0x700
+  __TEXT.__objc_methlist: 0x1ab0
   __TEXT.__const: 0xc8
-  __TEXT.__cstring: 0x19da
-  __TEXT.__gcc_except_tab: 0x2f0
+  __TEXT.__cstring: 0x1a61
+  __TEXT.__gcc_except_tab: 0x31c
   __TEXT.__oslogstring: 0xa5e
-  __TEXT.__unwind_info: 0x7f8
-  __TEXT.__objc_classname: 0x87f
-  __TEXT.__objc_methname: 0x5361
-  __TEXT.__objc_methtype: 0x18d1
-  __TEXT.__objc_stubs: 0x3c00
-  __DATA_CONST.__got: 0x428
-  __DATA_CONST.__const: 0xd18
-  __DATA_CONST.__objc_classlist: 0x118
+  __TEXT.__unwind_info: 0x7a8
+  __TEXT.__objc_classname: 0x825
+  __TEXT.__objc_methname: 0x5209
+  __TEXT.__objc_methtype: 0x1889
+  __TEXT.__objc_stubs: 0x3be0
+  __DATA_CONST.__got: 0x430
+  __DATA_CONST.__const: 0xd20
+  __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1280
-  __DATA_CONST.__objc_superrefs: 0xf8
-  __AUTH_CONST.__auth_got: 0x3a0
-  __AUTH_CONST.__const: 0x2a0
+  __DATA_CONST.__objc_selrefs: 0x1250
+  __DATA_CONST.__objc_superrefs: 0xe8
+  __AUTH_CONST.__auth_got: 0x390
+  __AUTH_CONST.__const: 0x260
   __AUTH_CONST.__cfstring: 0x1620
-  __AUTH_CONST.__objc_const: 0x3e50
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x274
+  __AUTH_CONST.__objc_const: 0x3b78
+  __DATA.__objc_ivar: 0x258
   __DATA.__data: 0xb40
   __DATA_DIRTY.__objc_ivar: 0x8
   __DATA_DIRTY.__objc_data: 0xa50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 590BF296-FB2E-3605-8DDA-BBE0E857AC8B
-  Functions: 699
-  Symbols:   2785
-  CStrings:  1512
+  UUID: 7DC80A6D-5C1C-39E1-BA53-949C71D17ABC
+  Functions: 664
+  Symbols:   2691
+  CStrings:  1493
 
Symbols:
+ -[STDataAccessStatusDomainDataProvider _internalQueue_publishData:]
+ -[STDataAccessStatusDomainDataProvider initWithServerHandle:publisherServerHandle:]
+ GCC_except_table1
+ GCC_except_table18
+ GCC_except_table4
+ GCC_except_table50
+ _OBJC_CLASS_$_STLocationStatusDomain
+ _OBJC_CLASS_$_STMediaStatusDomain
+ _OBJC_IVAR_$_STDataAccessStatusDomainDataProvider._locationDomain
+ _OBJC_IVAR_$_STDataAccessStatusDomainDataProvider._mediaDomain
+ ___55-[STLocalStatusServer removePublisherClient:forDomain:]_block_invoke_2
+ ___77-[STLocalStatusServer replaceDataChangeRecord:forPublisherClient:completion:]_block_invoke.135
+ ___77-[STLocalStatusServer replaceDataChangeRecord:forPublisherClient:completion:]_block_invoke_2
+ ___82-[STLocalStatusServer _internalQueue_mutateDataForDomain:withChangeContext:block:]_block_invoke.151
+ ___83-[STDataAccessStatusDomainDataProvider initWithServerHandle:publisherServerHandle:]_block_invoke
+ ___83-[STDataAccessStatusDomainDataProvider initWithServerHandle:publisherServerHandle:]_block_invoke_2
+ ___83-[STDataAccessStatusDomainDataProvider initWithServerHandle:publisherServerHandle:]_block_invoke_3
+ ___83-[STDataAccessStatusDomainDataProvider initWithServerHandle:publisherServerHandle:]_block_invoke_4
+ ___83-[STDataAccessStatusDomainDataProvider initWithServerHandle:publisherServerHandle:]_block_invoke_5
+ ___85-[STLocalStatusServer replaceVolatileDataChangeRecord:forPublisherClient:completion:]_block_invoke.139
+ ___85-[STLocalStatusServer replaceVolatileDataChangeRecord:forPublisherClient:completion:]_block_invoke_2
+ ___block_descriptor_40_e8_32w_e71_v24?0"STMediaStatusDomainData"8"<STStatusDomainDataChangeContext>"16lw32l8
+ ___block_descriptor_40_e8_32w_e80_v24?0"STLocationStatusDomainData"8"STLocationStatusDomainDataChangeContext"16lw32l8
+ ___block_literal_global.138
+ ___block_literal_global.141
+ ___block_literal_global.19
+ ___block_literal_global.21
+ ___block_literal_global.23
+ _objc_msgSend$data
+ _objc_msgSend$initWithServerHandle:wantsUntransformedData:
+ _objc_msgSend$observeData:
+ _objc_msgSend$remoteObjectProxy
+ _objc_retain_x10
- -[STDataAccessStatusDomainDataProvider _internalQueue_notifyForNewData:manualUpdate:]
- -[STDataAccessStatusDomainDataProvider dataAccessData]
- -[STDataAccessStatusDomainDataProvider dataChangedHandler]
- -[STDataAccessStatusDomainDataProvider init]
- -[STDataAccessStatusDomainDataProvider locationData]
- -[STDataAccessStatusDomainDataProvider mediaData]
- -[STDataAccessStatusDomainDataProvider setDataChangedHandler:]
- -[STDataAccessStatusDomainDataProvider setLocationData:mediaData:]
- -[STDataAccessStatusDomainDataProviderTransformer .cxx_destruct]
- -[STDataAccessStatusDomainDataProviderTransformer initWithDataProvider:publisherServerHandle:]
- -[STDataAccessStatusDomainDataProviderTransformer transformedDataForData:]
- -[STLocalStatusServer _internalQueue_publishData:forPublisherClient:domain:withChangeContext:completion:]
- -[STLocalStatusServer _internalQueue_publishVolatileData:forPublisherClient:domain:withChangeContext:completion:]
- -[STLocalStatusServer _internalQueue_registerPublisherClient:forDomain:fallbackData:]
- -[STLocalStatusServer _internalQueue_removePublisherClient:forDomain:]
- -[STLocalStatusServer _internalQueue_replaceDataChangeRecord:forPublisherClient:completion:]
- -[STLocalStatusServer _internalQueue_replaceVolatileDataChangeRecord:forPublisherClient:completion:]
- -[STLocalStatusServer _internalQueue_updateDataForPublisherClient:domain:usingDiffProvider:completion:]
- -[STLocalStatusServer _internalQueue_updateVolatileDataForPublisherClient:domain:usingDiffProvider:completion:]
- -[STLocalStatusServer internalQueuePublisherServerHandle]
- -[_STInternalQueueLocalStatusServerWrapper .cxx_destruct]
- -[_STInternalQueueLocalStatusServerWrapper initWithServer:]
- -[_STInternalQueueLocalStatusServerWrapper publishData:forPublisherClient:domain:withChangeContext:completion:]
- -[_STInternalQueueLocalStatusServerWrapper publishVolatileData:forPublisherClient:domain:withChangeContext:completion:]
- -[_STInternalQueueLocalStatusServerWrapper publishedDataForDomain:]
- -[_STInternalQueueLocalStatusServerWrapper publishedVolatileDataForDomain:]
- -[_STInternalQueueLocalStatusServerWrapper registerPublisherClient:forDomain:fallbackData:]
- -[_STInternalQueueLocalStatusServerWrapper removePublisherClient:forDomain:]
- -[_STInternalQueueLocalStatusServerWrapper replaceDataChangeRecord:forPublisherClient:completion:]
- -[_STInternalQueueLocalStatusServerWrapper replaceVolatileDataChangeRecord:forPublisherClient:completion:]
- -[_STInternalQueueLocalStatusServerWrapper server]
- -[_STInternalQueueLocalStatusServerWrapper updateDataForPublisherClient:domain:usingDiffProvider:completion:]
- -[_STInternalQueueLocalStatusServerWrapper updateVolatileDataForPublisherClient:domain:usingDiffProvider:completion:]
- GCC_except_table24
- GCC_except_table52
- _BSEqualObjects
- _OBJC_CLASS_$_STDataAccessStatusDomainDataProviderTransformer
- _OBJC_CLASS_$__STInternalQueueLocalStatusServerWrapper
- _OBJC_IVAR_$_STDataAccessStatusDomainDataProvider._dataChangedHandler
- _OBJC_IVAR_$_STDataAccessStatusDomainDataProvider._locationData
- _OBJC_IVAR_$_STDataAccessStatusDomainDataProvider._mediaData
- _OBJC_IVAR_$_STDataAccessStatusDomainDataProviderTransformer._dataAccessPublisher
- _OBJC_IVAR_$_STDataAccessStatusDomainDataProviderTransformer._dataProvider
- _OBJC_IVAR_$_STDataAccessStatusDomainDataProviderTransformer._locationData
- _OBJC_IVAR_$_STDataAccessStatusDomainDataProviderTransformer._mediaData
- _OBJC_IVAR_$_STDataAccessStatusDomainDataProviderTransformer._publisherServerHandle
- _OBJC_IVAR_$__STInternalQueueLocalStatusServerWrapper._server
- _OBJC_METACLASS_$_STDataAccessStatusDomainDataProviderTransformer
- _OBJC_METACLASS_$__STInternalQueueLocalStatusServerWrapper
- __OBJC_$_INSTANCE_METHODS_STDataAccessStatusDomainDataProviderTransformer
- __OBJC_$_INSTANCE_METHODS__STInternalQueueLocalStatusServerWrapper
- __OBJC_$_INSTANCE_VARIABLES_STDataAccessStatusDomainDataProviderTransformer
- __OBJC_$_INSTANCE_VARIABLES__STInternalQueueLocalStatusServerWrapper
- __OBJC_$_PROP_LIST__STInternalQueueLocalStatusServerWrapper
- __OBJC_CLASS_PROTOCOLS_$_STDataAccessStatusDomainDataProviderTransformer
- __OBJC_CLASS_PROTOCOLS_$__STInternalQueueLocalStatusServerWrapper
- __OBJC_CLASS_RO_$_STDataAccessStatusDomainDataProviderTransformer
- __OBJC_CLASS_RO_$__STInternalQueueLocalStatusServerWrapper
- __OBJC_METACLASS_RO_$_STDataAccessStatusDomainDataProviderTransformer
- __OBJC_METACLASS_RO_$__STInternalQueueLocalStatusServerWrapper
- ___100-[STLocalStatusServer _internalQueue_replaceVolatileDataChangeRecord:forPublisherClient:completion:]_block_invoke
- ___100-[STLocalStatusServer _internalQueue_replaceVolatileDataChangeRecord:forPublisherClient:completion:]_block_invoke.146
- ___44-[STDataAccessStatusDomainDataProvider init]_block_invoke
- ___49-[STDataAccessStatusDomainDataProvider mediaData]_block_invoke
- ___52-[STDataAccessStatusDomainDataProvider locationData]_block_invoke
- ___54-[STDataAccessStatusDomainDataProvider dataAccessData]_block_invoke
- ___66-[STDataAccessStatusDomainDataProvider setLocationData:mediaData:]_block_invoke
- ___70-[STLocalStatusServer _internalQueue_removePublisherClient:forDomain:]_block_invoke
- ___73-[STStatusDomainXPCClientHandle observeData:forDomain:withChangeContext:]_block_invoke_4
- ___74-[STStatusDomainPublisherXPCClientHandle handleUserInteraction:forDomain:]_block_invoke_2
- ___82-[STLocalStatusServer _internalQueue_mutateDataForDomain:withChangeContext:block:]_block_invoke.152
- ___92-[STLocalStatusServer _internalQueue_replaceDataChangeRecord:forPublisherClient:completion:]_block_invoke
- ___92-[STLocalStatusServer _internalQueue_replaceDataChangeRecord:forPublisherClient:completion:]_block_invoke.142
- ___block_descriptor_32_e17_v16?0"NSError"8l
- ___block_descriptor_64_e8_32s40s48s56r_e5_v8?0ls32l8s40l8s48l8r56l8
- ___block_literal_global.14
- ___block_literal_global.145
- ___block_literal_global.148
- ___block_literal_global.16
- ___block_literal_global.18
- _objc_msgSend$dataChangedHandler
- _objc_msgSend$initWithServer:
- _objc_msgSend$server
- _objc_msgSend$setLocationData:mediaData:
- _objc_msgSend$synchronousRemoteObjectProxyWithErrorHandler:
- _objc_retain_x5
- _objc_retain_x6
CStrings:
+ "@\"STLocationStatusDomain\""
+ "@\"STMediaStatusDomain\""
+ "_locationDomain"
+ "_mediaDomain"
+ "initWithServerHandle:publisherServerHandle:"
+ "initWithServerHandle:wantsUntransformedData:"
+ "observeData:"
+ "remoteObjectProxy"
+ "v24@?0@\"STLocationStatusDomainData\"8@\"STLocationStatusDomainDataChangeContext\"16"
+ "v24@?0@\"STMediaStatusDomainData\"8@\"<STStatusDomainDataChangeContext>\"16"
- "@\"STDataAccessStatusDomainDataProvider\""
- "@\"STLocationStatusDomainData\""
- "@\"STMediaStatusDomainData\""
- "@?"
- "@?16@0:8"
- "STDataAccessStatusDomainDataProviderTransformer"
- "T@\"STDataAccessStatusDomainData\",R,C,N"
- "T@\"STLocalStatusServer\",R,N,V_server"
- "T@\"STLocationStatusDomainData\",R,C,N"
- "T@\"STMediaStatusDomainData\",R,C,N"
- "T@?,C,N,V_dataChangedHandler"
- "_STInternalQueueLocalStatusServerWrapper"
- "_dataChangedHandler"
- "_dataProvider"
- "_locationData"
- "_mediaData"
- "_server"
- "dataAccessData"
- "dataChangedHandler"
- "initWithDataProvider:publisherServerHandle:"
- "initWithServer:"
- "internalQueuePublisherServerHandle"
- "locationData"
- "mediaData"
- "server"
- "setDataChangedHandler:"
- "setLocationData:mediaData:"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "v16@?0@\"NSError\"8"
- "v24@0:8@?16"

```
