## SystemStatusServer

> `/System/Library/PrivateFrameworks/SystemStatusServer.framework/Versions/A/SystemStatusServer`

```diff

-210.4.13.0.0
-  __TEXT.__text: 0xe820
-  __TEXT.__auth_stubs: 0x400
-  __TEXT.__objc_methlist: 0xa78
-  __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x532
-  __TEXT.__gcc_except_tab: 0x98
-  __TEXT.__oslogstring: 0x357
-  __TEXT.__unwind_info: 0x3c8
-  __TEXT.__objc_classname: 0x434
-  __TEXT.__objc_methname: 0x1e19
-  __TEXT.__objc_methtype: 0xba4
-  __TEXT.__objc_stubs: 0x1ba0
-  __DATA_CONST.__got: 0x278
-  __DATA_CONST.__const: 0x100
-  __DATA_CONST.__objc_classlist: 0x88
-  __DATA_CONST.__objc_protolist: 0x78
+210.5.2.0.0
+  __TEXT.__text: 0x11560
+  __TEXT.__auth_stubs: 0x450
+  __TEXT.__objc_methlist: 0xbb0
+  __TEXT.__const: 0x80
+  __TEXT.__cstring: 0x6e7
+  __TEXT.__gcc_except_tab: 0x1b0
+  __TEXT.__oslogstring: 0x3b1
+  __TEXT.__unwind_info: 0x470
+  __TEXT.__objc_classname: 0x519
+  __TEXT.__objc_methname: 0x22bf
+  __TEXT.__objc_methtype: 0xcb1
+  __TEXT.__objc_stubs: 0x1f20
+  __DATA_CONST.__got: 0x2d8
+  __DATA_CONST.__const: 0x160
+  __DATA_CONST.__objc_classlist: 0xa8
+  __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7f8
-  __DATA_CONST.__objc_superrefs: 0x88
-  __AUTH_CONST.__auth_got: 0x210
-  __AUTH_CONST.__const: 0x850
-  __AUTH_CONST.__cfstring: 0x300
-  __AUTH_CONST.__objc_const: 0x1968
-  __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH.__objc_data: 0x550
-  __DATA.__objc_ivar: 0xf8
-  __DATA.__data: 0x5a0
+  __DATA_CONST.__objc_selrefs: 0x8e0
+  __DATA_CONST.__objc_superrefs: 0xa8
+  __AUTH_CONST.__auth_got: 0x238
+  __AUTH_CONST.__const: 0x9f0
+  __AUTH_CONST.__cfstring: 0x340
+  __AUTH_CONST.__objc_const: 0x1e98
+  __AUTH.__objc_data: 0x690
+  __DATA.__objc_ivar: 0x134
+  __DATA.__data: 0x660
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 275
-  Symbols:   962
-  CStrings:  493
+  Functions: 314
+  Symbols:   1111
+  CStrings:  555
 
Symbols:
+ -[STAttributedEntityResolver initWithPreferredLocalizations:identityResolver:]
+ -[STAttributedEntityResolverProvider .cxx_destruct]
+ -[STAttributedEntityResolverProvider dynamicAttributions]
+ -[STAttributedEntityResolverProvider initWithIdentityResolver:]
+ -[STAttributedEntityResolverProvider init]
+ -[STAttributedEntityResolverProvider resolverForPreferredLocalizations:]
+ -[STAttributedEntityResolverProvider setDynamicAttributions:]
+ -[STDataAccessStatusDomainDataProvider .cxx_destruct]
+ -[STDataAccessStatusDomainDataProvider _dataAccessAttributionsForAttributions:dataAccessType:dataAccessAttributionProvider:]
+ -[STDataAccessStatusDomainDataProvider _internalQueue_generatedData]
+ -[STDataAccessStatusDomainDataProvider _internalQueue_handleLocationData:mediaData:]
+ -[STDataAccessStatusDomainDataProvider _internalQueue_makeAttributionRecent:]
+ -[STDataAccessStatusDomainDataProvider _internalQueue_publishData:]
+ -[STDataAccessStatusDomainDataProvider dealloc]
+ -[STDataAccessStatusDomainDataProvider initWithServerHandle:publisherServerHandle:]
+ -[STDataAccessStatusDomainDataProvider invalidate]
+ -[STDataAccessStatusDomainDisplayNameTransformer .cxx_destruct]
+ -[STDataAccessStatusDomainDisplayNameTransformer initWithEntityResolver:]
+ -[STDataAccessStatusDomainDisplayNameTransformer transformedDataForData:]
+ -[STDataAccessStatusDomainDisplayNameTransformerProvider .cxx_destruct]
+ -[STDataAccessStatusDomainDisplayNameTransformerProvider dataTransformerForClient:]
+ -[STDataAccessStatusDomainDisplayNameTransformerProvider initWithEntityResolverProvider:]
+ -[STDataAccessStatusDomainDisplayNameTransformerProvider init]
+ -[STLocalStatusServer dataForDomain:client:]
+ -[STLocationStatusDomainDisplayNameTransformerProvider initWithEntityResolverProvider:]
+ -[STMediaStatusDomainDisplayNameTransformerProvider initWithEntityResolverProvider:]
+ -[STStatusDomainClientHandleWrapper wantsUntransformedData]
+ -[STStatusDomainXPCClientHandle serverDataForDomains:preferredLocalizations:reply:]
+ -[STStatusDomainXPCClientHandle wantsUntransformedData]
+ -[STStatusServer dataForDomain:client:]
+ GCC_except_table1
+ GCC_except_table21
+ GCC_except_table4
+ OBJC_IVAR_$_STAttributedEntityResolverProvider._dynamicAttributions
+ OBJC_IVAR_$_STAttributedEntityResolverProvider._entityResolversByLocalization
+ OBJC_IVAR_$_STAttributedEntityResolverProvider._identityResolver
+ OBJC_IVAR_$_STDataAccessStatusDomainDataProvider._activeAttributionMinimumDisplayTimers
+ OBJC_IVAR_$_STDataAccessStatusDomainDataProvider._activeAttributions
+ OBJC_IVAR_$_STDataAccessStatusDomainDataProvider._attributionsWaitingForMinimumDisplayTime
+ OBJC_IVAR_$_STDataAccessStatusDomainDataProvider._currentData
+ OBJC_IVAR_$_STDataAccessStatusDomainDataProvider._dataAccessPublisher
+ OBJC_IVAR_$_STDataAccessStatusDomainDataProvider._internalQueue
+ OBJC_IVAR_$_STDataAccessStatusDomainDataProvider._invalidated
+ OBJC_IVAR_$_STDataAccessStatusDomainDataProvider._locationDomain
+ OBJC_IVAR_$_STDataAccessStatusDomainDataProvider._mediaDomain
+ OBJC_IVAR_$_STDataAccessStatusDomainDataProvider._recentAttributionExpirationTimers
+ OBJC_IVAR_$_STDataAccessStatusDomainDataProvider._recentAttributions
+ OBJC_IVAR_$_STDataAccessStatusDomainDisplayNameTransformer._entityResolver
+ OBJC_IVAR_$_STDataAccessStatusDomainDisplayNameTransformerProvider._entityResolverProvider
+ OBJC_IVAR_$_STDataAccessStatusDomainDisplayNameTransformerProvider._transformersByLocalization
+ OBJC_IVAR_$_STLocationStatusDomainDisplayNameTransformerProvider._entityResolverProvider
+ OBJC_IVAR_$_STMediaStatusDomainDisplayNameTransformerProvider._entityResolverProvider
+ _BSFloatGreaterThanFloat
+ _OBJC_CLASS_$_BSContinuousMachTimer
+ _OBJC_CLASS_$_NSSet
+ _OBJC_CLASS_$_STAttributedEntityResolverProvider
+ _OBJC_CLASS_$_STDataAccessAttribution
+ _OBJC_CLASS_$_STDataAccessStatusDomainData
+ _OBJC_CLASS_$_STDataAccessStatusDomainDataProvider
+ _OBJC_CLASS_$_STDataAccessStatusDomainDisplayNameTransformer
+ _OBJC_CLASS_$_STDataAccessStatusDomainDisplayNameTransformerProvider
+ _OBJC_CLASS_$_STDataAccessStatusDomainPublisher
+ _OBJC_CLASS_$_STLocationStatusDomain
+ _OBJC_CLASS_$_STMediaStatusDomain
+ _OBJC_CLASS_$_STMutableDataAccessStatusDomainData
+ _OBJC_METACLASS_$_STAttributedEntityResolverProvider
+ _OBJC_METACLASS_$_STDataAccessStatusDomainDataProvider
+ _OBJC_METACLASS_$_STDataAccessStatusDomainDisplayNameTransformer
+ _OBJC_METACLASS_$_STDataAccessStatusDomainDisplayNameTransformerProvider
+ _STDataAccessStatusDomainMinumumOnTime
+ _STDescriptionForDataAccessType
+ _STStatusDomainEntitlementValueDataAccess
+ _STSystemStatusLogDataIntegrity
+ _STTimestampNow
+ __61-[STLocalStatusServer descriptionBuilderWithMultilinePrefix:]_block_invoke.155
+ __73-[STStatusDomainXPCClientHandle observeData:forDomain:withChangeContext:]_block_invoke.14
+ __77-[STLocalStatusServer replaceDataChangeRecord:forPublisherClient:completion:]_block_invoke.139
+ __82-[STLocalStatusServer _internalQueue_mutateDataForDomain:withChangeContext:block:]_block_invoke.170
+ __82-[STLocalStatusServer _internalQueue_mutateDataForDomain:withChangeContext:block:]_block_invoke.174
+ __82-[STLocalStatusServer _internalQueue_mutateDataForDomain:withChangeContext:block:]_block_invoke.175
+ __83-[STDataAccessStatusDomainDataProvider initWithServerHandle:publisherServerHandle:]_block_invoke.8
+ __83-[STDataAccessStatusDomainDataProvider initWithServerHandle:publisherServerHandle:]_block_invoke_2.9
+ __85-[STLocalStatusServer replaceVolatileDataChangeRecord:forPublisherClient:completion:]_block_invoke.143
+ __OBJC_$_INSTANCE_METHODS_STAttributedEntityResolverProvider
+ __OBJC_$_INSTANCE_METHODS_STDataAccessStatusDomainDataProvider
+ __OBJC_$_INSTANCE_METHODS_STDataAccessStatusDomainDisplayNameTransformer
+ __OBJC_$_INSTANCE_METHODS_STDataAccessStatusDomainDisplayNameTransformerProvider
+ __OBJC_$_INSTANCE_VARIABLES_STAttributedEntityResolverProvider
+ __OBJC_$_INSTANCE_VARIABLES_STDataAccessStatusDomainDataProvider
+ __OBJC_$_INSTANCE_VARIABLES_STDataAccessStatusDomainDisplayNameTransformer
+ __OBJC_$_INSTANCE_VARIABLES_STDataAccessStatusDomainDisplayNameTransformerProvider
+ __OBJC_$_PROP_LIST_STAttributedEntityResolverProvider
+ __OBJC_$_PROP_LIST_STDataAccessStatusDomainDataProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BSInvalidatable
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_STAttributedEntityResolverProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BSInvalidatable
+ __OBJC_$_PROTOCOL_METHOD_TYPES_STAttributedEntityResolverProviding
+ __OBJC_$_PROTOCOL_REFS_BSInvalidatable
+ __OBJC_CLASS_PROTOCOLS_$_STAttributedEntityResolverProvider
+ __OBJC_CLASS_PROTOCOLS_$_STDataAccessStatusDomainDataProvider
+ __OBJC_CLASS_PROTOCOLS_$_STDataAccessStatusDomainDisplayNameTransformer
+ __OBJC_CLASS_PROTOCOLS_$_STDataAccessStatusDomainDisplayNameTransformerProvider
+ __OBJC_CLASS_RO_$_STAttributedEntityResolverProvider
+ __OBJC_CLASS_RO_$_STDataAccessStatusDomainDataProvider
+ __OBJC_CLASS_RO_$_STDataAccessStatusDomainDisplayNameTransformer
+ __OBJC_CLASS_RO_$_STDataAccessStatusDomainDisplayNameTransformerProvider
+ __OBJC_LABEL_PROTOCOL_$_BSInvalidatable
+ __OBJC_LABEL_PROTOCOL_$_STAttributedEntityResolverProviding
+ __OBJC_METACLASS_RO_$_STAttributedEntityResolverProvider
+ __OBJC_METACLASS_RO_$_STDataAccessStatusDomainDataProvider
+ __OBJC_METACLASS_RO_$_STDataAccessStatusDomainDisplayNameTransformer
+ __OBJC_METACLASS_RO_$_STDataAccessStatusDomainDisplayNameTransformerProvider
+ __OBJC_PROTOCOL_$_BSInvalidatable
+ __OBJC_PROTOCOL_$_STAttributedEntityResolverProviding
+ ___104-[STDataAccessStatusDomainDataProvider _internalQueue_beginWaitingForMinimumDisplayTime:forAttribution:]_block_invoke
+ ___44-[STLocalStatusServer dataForDomain:client:]_block_invoke
+ ___50-[STDataAccessStatusDomainDataProvider invalidate]_block_invoke
+ ___61-[STAttributedEntityResolverProvider setDynamicAttributions:]_block_invoke
+ ___73-[STDataAccessStatusDomainDisplayNameTransformer transformedDataForData:]_block_invoke
+ ___73-[STDataAccessStatusDomainDisplayNameTransformer transformedDataForData:]_block_invoke_2
+ ___77-[STDataAccessStatusDomainDataProvider _internalQueue_makeAttributionRecent:]_block_invoke
+ ___83-[STDataAccessStatusDomainDataProvider initWithServerHandle:publisherServerHandle:]_block_invoke
+ ___83-[STDataAccessStatusDomainDataProvider initWithServerHandle:publisherServerHandle:]_block_invoke_2
+ ___83-[STDataAccessStatusDomainDataProvider initWithServerHandle:publisherServerHandle:]_block_invoke_3
+ ___83-[STStatusDomainXPCClientHandle serverDataForDomains:preferredLocalizations:reply:]_block_invoke
+ ___85-[STDataAccessStatusDomainDataProvider _filteredLocationAttributionsForLocationData:]_block_invoke
+ ___85-[STDataAccessStatusDomainDataProvider _filteredLocationAttributionsForLocationData:]_block_invoke_2
+ ___87-[STDataAccessStatusDomainDataProvider _dataAccessAttributionsForLocationAttributions:]_block_invoke
+ ___92-[STDataAccessStatusDomainDataProvider _dataAccessAttributionsForCameraCaptureAttributions:]_block_invoke
+ ___98-[STDataAccessStatusDomainDataProvider _dataAccessAttributionsForMicrophoneRecordingAttributions:]_block_invoke
+ ___block_descriptor_32_e33_"STDataAccessAttribution"16?08l
+ ___block_descriptor_32_e33_16?0"STDataAccessAttribution"8l
+ ___block_descriptor_40_e51_B16?0"STLocationStatusDomainLocationAttribution"8l
+ ___block_descriptor_40_e8_32s_e33_16?0"STDataAccessAttribution"8l
+ ___block_descriptor_40_e8_32w_e71_v24?0"STMediaStatusDomainData"8"<STStatusDomainDataChangeContext>"16l
+ ___block_descriptor_40_e8_32w_e80_v24?0"STLocationStatusDomainData"8"STLocationStatusDomainDataChangeContext"16l
+ ___block_descriptor_41_e8_32s_e51_16?0"STLocationStatusDomainLocationAttribution"8l
+ ___block_descriptor_48_e8_32s40w_e31_v16?0"BSContinuousMachTimer"8l
+ ___block_descriptor_48_e8_32s40w_e5_v8?0l
+ ___block_descriptor_64_e8_32s40s48r_e5_v8?0l
+ ___copy_helper_block_e8_32s40w
+ ___destroy_helper_block_e8_32s40w
+ __block_literal_global.142
+ __block_literal_global.145
+ __block_literal_global.25
+ __block_literal_global.27
+ __os_log_error_impl
+ _objc_msgSend$accessDuration
+ _objc_msgSend$accessEndTimestamp
+ _objc_msgSend$accessStartTimestamp
+ _objc_msgSend$allValues
+ _objc_msgSend$audioRecordingActivityAttribution
+ _objc_msgSend$bs_filter:
+ _objc_msgSend$cameraCaptureAttribution
+ _objc_msgSend$data
+ _objc_msgSend$dataAccessAttributions
+ _objc_msgSend$dataAccessType
+ _objc_msgSend$dataForDomain:client:
+ _objc_msgSend$initWithAudioRecordingActivityAttribution:recent:startTimestamp:endTimestamp:
+ _objc_msgSend$initWithCameraCaptureAttribution:recent:startTimestamp:endTimestamp:
+ _objc_msgSend$initWithEntityResolverProvider:
+ _objc_msgSend$initWithIdentifier:
+ _objc_msgSend$initWithIdentityResolver:
+ _objc_msgSend$initWithLocationAttribution:recent:startTimestamp:endTimestamp:
+ _objc_msgSend$initWithMicrophoneRecordingAttribution:recent:startTimestamp:endTimestamp:
+ _objc_msgSend$initWithPreferredLocalizations:identityResolver:
+ _objc_msgSend$initWithServerHandle:wantsUntransformedData:
+ _objc_msgSend$isRecent
+ _objc_msgSend$locationAttribution
+ _objc_msgSend$microphoneRecordingAttribution
+ _objc_msgSend$observeData:
+ _objc_msgSend$resolverForPreferredLocalizations:
+ _objc_msgSend$scheduleWithFireInterval:leewayInterval:queue:handler:
+ _objc_msgSend$setDataAccessAttributions:
+ _objc_msgSend$setVolatileData:
+ _objc_msgSend$wantsUntransformedData
- -[STLocalStatusServer dataForDomain:]
- -[STLocationStatusDomainDisplayNameTransformerProvider dynamicAttributions]
- -[STLocationStatusDomainDisplayNameTransformerProvider setDynamicAttributions:]
- -[STMediaStatusDomainDisplayNameTransformerProvider dynamicAttributions]
- -[STMediaStatusDomainDisplayNameTransformerProvider setDynamicAttributions:]
- -[STStatusDomainXPCClientHandle serverDataForDomains:reply:]
- -[STStatusServer dataForDomain:]
- OBJC_IVAR_$_STLocationStatusDomainDisplayNameTransformerProvider._dynamicAttributions
- OBJC_IVAR_$_STLocationStatusDomainDisplayNameTransformerProvider._entityResolversByLocalization
- OBJC_IVAR_$_STMediaStatusDomainDisplayNameTransformerProvider._dynamicAttributions
- OBJC_IVAR_$_STMediaStatusDomainDisplayNameTransformerProvider._entityResolversByLocalization
- _OBJC_CLASS_$_NSConstantIntegerNumber
- __61-[STLocalStatusServer descriptionBuilderWithMultilinePrefix:]_block_invoke.152
- __73-[STStatusDomainXPCClientHandle observeData:forDomain:withChangeContext:]_block_invoke.15
- __77-[STLocalStatusServer replaceDataChangeRecord:forPublisherClient:completion:]_block_invoke.138
- __82-[STLocalStatusServer _internalQueue_mutateDataForDomain:withChangeContext:block:]_block_invoke.167
- __82-[STLocalStatusServer _internalQueue_mutateDataForDomain:withChangeContext:block:]_block_invoke.171
- __82-[STLocalStatusServer _internalQueue_mutateDataForDomain:withChangeContext:block:]_block_invoke.172
- __85-[STLocalStatusServer replaceVolatileDataChangeRecord:forPublisherClient:completion:]_block_invoke.142
- __OBJC_$_PROP_LIST_STLocationStatusDomainDisplayNameTransformerProvider
- __OBJC_$_PROP_LIST_STMediaStatusDomainDisplayNameTransformerProvider
- ___37-[STLocalStatusServer dataForDomain:]_block_invoke
- ___60-[STStatusDomainXPCClientHandle serverDataForDomains:reply:]_block_invoke
- ___76-[STMediaStatusDomainDisplayNameTransformerProvider setDynamicAttributions:]_block_invoke
- ___79-[STLocationStatusDomainDisplayNameTransformerProvider setDynamicAttributions:]_block_invoke
- ___block_descriptor_56_e8_32s40s48bs_e5_v8?0l
- __block_literal_global.141
- __block_literal_global.144
- _objc_msgSend$dataForDomain:
CStrings:
+ "\x1a"
+ "@\"<STAttributedEntityResolverProviding>\""
+ "@\"<STStatusDomainData>\"32@0:8Q16@\"<STStatusDomainClientHandle>\"24"
+ "@\"NSMutableArray\""
+ "@\"STAttributedEntityResolver\"24@0:8@\"NSArray\"16"
+ "@\"STDataAccessAttribution\"16@?0@8"
+ "@\"STDataAccessStatusDomainData\""
+ "@\"STDataAccessStatusDomainPublisher\""
+ "@\"STLocationStatusDomain\""
+ "@\"STMediaStatusDomain\""
+ "@16@?0@\"STDataAccessAttribution\"8"
+ "@32@0:8Q16@24"
+ "B16@?0@\"STLocationStatusDomainLocationAttribution\"8"
+ "BSInvalidatable"
+ "STAttributedEntityResolverProvider"
+ "STAttributedEntityResolverProviding"
+ "STDataAccessStatusDomain-MinimumDisplayTime"
+ "STDataAccessStatusDomain-RecentAttributionExpiration"
+ "STDataAccessStatusDomainDataProvider"
+ "STDataAccessStatusDomainDisplayNameTransformer"
+ "STDataAccessStatusDomainDisplayNameTransformerProvider"
+ "TB,R,N"
+ "_activeAttributionMinimumDisplayTimers"
+ "_activeAttributions"
+ "_attributionsWaitingForMinimumDisplayTime"
+ "_currentData"
+ "_dataAccessPublisher"
+ "_entityResolverProvider"
+ "_locationDomain"
+ "_mediaDomain"
+ "_recentAttributionExpirationTimers"
+ "_recentAttributions"
+ "accessDuration"
+ "accessEndTimestamp"
+ "accessStartTimestamp"
+ "allValues"
+ "audioRecordingActivityAttribution"
+ "bs_filter:"
+ "cameraCaptureAttribution"
+ "com.apple.systemstatus.data-access.internalqueue"
+ "dataAccessAttributions"
+ "dataAccessType"
+ "dataForDomain:client:"
+ "initWithAudioRecordingActivityAttribution:recent:startTimestamp:endTimestamp:"
+ "initWithCameraCaptureAttribution:recent:startTimestamp:endTimestamp:"
+ "initWithEntityResolverProvider:"
+ "initWithIdentifier:"
+ "initWithIdentityResolver:"
+ "initWithLocationAttribution:recent:startTimestamp:endTimestamp:"
+ "initWithMicrophoneRecordingAttribution:recent:startTimestamp:endTimestamp:"
+ "initWithPreferredLocalizations:identityResolver:"
+ "initWithServerHandle:publisherServerHandle:"
+ "initWithServerHandle:wantsUntransformedData:"
+ "isRecent"
+ "locationAttribution"
+ "microphoneRecordingAttribution"
+ "observeData:"
+ "resolverForPreferredLocalizations:"
+ "scheduleWithFireInterval:leewayInterval:queue:handler:"
+ "serverDataForDomains:preferredLocalizations:reply:"
+ "setDataAccessAttributions:"
+ "setVolatileData:"
+ "transformer encountered data access attribution of invalid type: %{public}lu (%{public}@)"
+ "v16@?0@\"BSContinuousMachTimer\"8"
+ "v24@?0@\"STLocationStatusDomainData\"8@\"STLocationStatusDomainDataChangeContext\"16"
+ "v24@?0@\"STMediaStatusDomainData\"8@\"<STStatusDomainDataChangeContext>\"16"
+ "v40@0:8@\"NSSet\"16@\"NSArray\"24@?<v@?@\"NSDictionary\">32"
+ "wantsUntransformedData"
- "@\"<STStatusDomainData>\"24@0:8Q16"
- "Q"
- "data-access"
- "dataForDomain:"
- "serverDataForDomains:reply:"
- "v32@0:8@\"NSSet\"16@?<v@?@\"NSDictionary\">24"
- "v32@0:8@16@?24"

```
