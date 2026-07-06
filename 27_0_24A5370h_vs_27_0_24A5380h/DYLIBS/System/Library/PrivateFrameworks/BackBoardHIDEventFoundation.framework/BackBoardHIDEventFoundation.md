## BackBoardHIDEventFoundation

> `/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation`

```diff

-  __TEXT.__text: 0x3c54c
-  __TEXT.__objc_methlist: 0x2160
+  __TEXT.__text: 0x3cdc4
+  __TEXT.__objc_methlist: 0x22c8
   __TEXT.__const: 0x68c
   __TEXT.__constg_swiftt: 0x1b0
   __TEXT.__swift5_typeref: 0x225
   __TEXT.__swift5_reflstr: 0x12c
   __TEXT.__swift5_fieldmd: 0x1b0
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__cstring: 0x2fc9
+  __TEXT.__cstring: 0x3392
   __TEXT.__swift5_types: 0x24
   __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__gcc_except_tab: 0x39c
-  __TEXT.__oslogstring: 0x326d
-  __TEXT.__unwind_info: 0xbd8
+  __TEXT.__gcc_except_tab: 0x3bc
+  __TEXT.__oslogstring: 0x32e0
+  __TEXT.__unwind_info: 0xc28
   __TEXT.__eh_frame: 0x158
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1350
-  __DATA_CONST.__objc_classlist: 0x1a8
+  __DATA_CONST.__const: 0x15f8
+  __DATA_CONST.__objc_classlist: 0x1b8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x13e8
+  __DATA_CONST.__objc_selrefs: 0x1480
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x118
   __DATA_CONST.__objc_arraydata: 0x290
-  __DATA_CONST.__got: 0x3f0
-  __AUTH_CONST.__const: 0xa18
-  __AUTH_CONST.__cfstring: 0x2a80
-  __AUTH_CONST.__objc_const: 0x5e88
+  __DATA_CONST.__got: 0x400
+  __AUTH_CONST.__const: 0xb58
+  __AUTH_CONST.__cfstring: 0x2b40
+  __AUTH_CONST.__objc_const: 0x6098
   __AUTH_CONST.__objc_intobj: 0x3d8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x8e8
-  __AUTH.__objc_data: 0x450
+  __AUTH.__objc_data: 0x4f0
   __AUTH.__data: 0x148
-  __DATA.__objc_ivar: 0x44c
+  __DATA.__objc_ivar: 0x45c
   __DATA.__data: 0xca0
   __DATA.__bss: 0x460
   __DATA_DIRTY.__objc_data: 0xc80

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1045
-  Symbols:   3687
-  CStrings:  1003
+  Functions: 1086
+  Symbols:   3840
+  CStrings:  1031
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ +[BKHIDDomainClientCalloutContextualizer(ClientEnvironment) _contextualizerWrappingClientProvidedContextualizer:connection:getCurrent:setCurrent:]
+ +[BKHIDDomainServiceServer(ClientEnvironment) _currentClientEnvironmentObjectForKey:]
+ +[BKHIDDomainServiceServer(ClientEnvironment) _currentDirectTouchEventProcessor]
+ +[BKHIDDomainServiceServer(ClientEnvironment) _currentDisplayRenderSpace]
+ +[BKHIDDomainServiceServer(ClientEnvironment) _currentHIDEventDeliveryManager]
+ +[BKHIDDomainServiceServer(ClientEnvironment) _currentHIDEventDeliveryObserverService]
+ +[BKHIDDomainServiceServer(ClientEnvironment) _currentTouchDeliveryObservationManager]
+ +[BKHIDDomainServiceServer(ClientEnvironment) _setCurrentClientEnvironmentObject:forKey:]
+ +[BKHIDDomainServiceServer(ClientEnvironment) _setCurrentDirectTouchEventProcessor:]
+ +[BKHIDDomainServiceServer(ClientEnvironment) _setCurrentDisplayRenderSpace:]
+ +[BKHIDDomainServiceServer(ClientEnvironment) _setCurrentHIDEventDeliveryManager:]
+ +[BKHIDDomainServiceServer(ClientEnvironment) _setCurrentHIDEventDeliveryObserverService:]
+ +[BKHIDDomainServiceServer(ClientEnvironment) _setCurrentTouchDeliveryObservationManager:]
+ -[BKHIDClientCalloutContextualizer .cxx_destruct]
+ -[BKHIDClientCalloutContextualizer contextualizedMappedObjectFetcher]
+ -[BKHIDClientCalloutContextualizer setContextualizedMappedObjectFetcher:]
+ -[BKHIDClientCalloutContextualizer setSetupBlock:]
+ -[BKHIDClientCalloutContextualizer setTeardownBlock:]
+ -[BKHIDClientCalloutContextualizer setupBlock]
+ -[BKHIDClientCalloutContextualizer teardownBlock]
+ -[BKHIDDomainClientCalloutContextualizer .cxx_destruct]
+ -[BKHIDDomainClientCalloutContextualizer setSetupBlock:]
+ -[BKHIDDomainClientCalloutContextualizer setTeardownBlock:]
+ -[BKHIDDomainClientCalloutContextualizer setupBlock]
+ -[BKHIDDomainClientCalloutContextualizer teardownBlock]
+ -[BKHIDDomainIncomingServiceConnection acceptConnectionUsingServiceQueue:clientCalloutContextualizer:]
+ -[BKHIDDomainServiceServer acceptIncomingServiceConnection:serviceQueue:clientCalloutContextualizer:]
+ -[BKHIDEventDeliveryManagerServer acceptIncomingServiceConnection:serviceQueue:clientCalloutContextualizer:]
+ -[BKHIDEventDeliveryObserverServer acceptIncomingServiceConnection:serviceQueue:clientCalloutContextualizer:]
+ -[BKHIDIncomingServiceConnection acceptConnectionWithServiceQueue:clientCalloutContextualizer:]
+ GCC_except_table241
+ GCC_except_table281
+ GCC_except_table334
+ GCC_except_table392
+ GCC_except_table405
+ GCC_except_table408
+ GCC_except_table414
+ GCC_except_table417
+ GCC_except_table43
+ GCC_except_table662
+ GCC_except_table665
+ GCC_except_table69
+ GCC_except_table699
+ GCC_except_table748
+ GCC_except_table809
+ GCC_except_table821
+ GCC_except_table853
+ _BKGetCurrentDirectTouchEventProcessor
+ _BKGetCurrentDirectTouchEventProcessor_block_invoke
+ _BKGetCurrentDisplayRenderSpace
+ _BKGetCurrentDisplayRenderSpace_block_invoke_3
+ _BKGetCurrentHIDEventDeliveryManager
+ _BKGetCurrentHIDEventDeliveryManager_block_invoke_5
+ _BKGetCurrentHIDEventDeliveryObserverService
+ _BKGetCurrentHIDEventDeliveryObserverService_block_invoke_7
+ _BKGetCurrentTouchDeliveryObservationManager
+ _BKGetCurrentTouchDeliveryObservationManager_block_invoke_9
+ _BKSetCurrentDirectTouchEventProcessor
+ _BKSetCurrentDirectTouchEventProcessor_block_invoke_2
+ _BKSetCurrentDisplayRenderSpace
+ _BKSetCurrentDisplayRenderSpace_block_invoke_4
+ _BKSetCurrentHIDEventDeliveryManager
+ _BKSetCurrentHIDEventDeliveryManager_block_invoke_6
+ _BKSetCurrentHIDEventDeliveryObserverService
+ _BKSetCurrentHIDEventDeliveryObserverService_block_invoke_8
+ _BKSetCurrentTouchDeliveryObservationManager
+ _BKSetCurrentTouchDeliveryObservationManager_block_invoke_10
+ _OBJC_CLASS_$_BKHIDClientCalloutContextualizer
+ _OBJC_CLASS_$_BKHIDDomainClientCalloutContextualizer
+ _OBJC_CLASS_$_BSServiceConnectionCalloutContextualizer
+ _OBJC_CLASS_$_NSThread
+ _OBJC_IVAR_$_BKHIDClientCalloutContextualizer._contextualizedMappedObjectFetcher
+ _OBJC_IVAR_$_BKHIDClientCalloutContextualizer._setupBlock
+ _OBJC_IVAR_$_BKHIDClientCalloutContextualizer._teardownBlock
+ _OBJC_IVAR_$_BKHIDDomainClientCalloutContextualizer._setupBlock
+ _OBJC_IVAR_$_BKHIDDomainClientCalloutContextualizer._teardownBlock
+ _OBJC_METACLASS_$_BKHIDClientCalloutContextualizer
+ _OBJC_METACLASS_$_BKHIDDomainClientCalloutContextualizer
+ __OBJC_$_CLASS_METHODS_BKHIDDomainClientCalloutContextualizer(ClientEnvironment)
+ __OBJC_$_CLASS_METHODS_BKHIDDomainServiceServer(ClientEnvironment)
+ __OBJC_$_INSTANCE_METHODS_BKHIDClientCalloutContextualizer
+ __OBJC_$_INSTANCE_METHODS_BKHIDDomainClientCalloutContextualizer
+ __OBJC_$_INSTANCE_VARIABLES_BKHIDClientCalloutContextualizer
+ __OBJC_$_INSTANCE_VARIABLES_BKHIDDomainClientCalloutContextualizer
+ __OBJC_$_PROP_LIST_BKHIDClientCalloutContextualizer
+ __OBJC_$_PROP_LIST_BKHIDDomainClientCalloutContextualizer
+ __OBJC_CLASS_RO_$_BKHIDClientCalloutContextualizer
+ __OBJC_CLASS_RO_$_BKHIDDomainClientCalloutContextualizer
+ __OBJC_METACLASS_RO_$_BKHIDClientCalloutContextualizer
+ __OBJC_METACLASS_RO_$_BKHIDDomainClientCalloutContextualizer
+ ___101-[BKHIDDomainServiceServer acceptIncomingServiceConnection:serviceQueue:clientCalloutContextualizer:]_block_invoke
+ ___101-[BKHIDDomainServiceServer acceptIncomingServiceConnection:serviceQueue:clientCalloutContextualizer:]_block_invoke_2
+ ___101-[BKHIDDomainServiceServer acceptIncomingServiceConnection:serviceQueue:clientCalloutContextualizer:]_block_invoke_3
+ ___101-[BKHIDDomainServiceServer acceptIncomingServiceConnection:serviceQueue:clientCalloutContextualizer:]_block_invoke_4
+ ___101-[BKHIDDomainServiceServer acceptIncomingServiceConnection:serviceQueue:clientCalloutContextualizer:]_block_invoke_5
+ ___146+[BKHIDDomainClientCalloutContextualizer(ClientEnvironment) _contextualizerWrappingClientProvidedContextualizer:connection:getCurrent:setCurrent:]_block_invoke
+ ___146+[BKHIDDomainClientCalloutContextualizer(ClientEnvironment) _contextualizerWrappingClientProvidedContextualizer:connection:getCurrent:setCurrent:]_block_invoke_2
+ ___67-[BKHIDIncomingServiceConnection acceptConnectionWithMappedObject:]_block_invoke
+ ___block_descriptor_32_e29_"<BKDisplayRenderSpace>"8?0l
+ ___block_descriptor_32_e32_"BKHIDEventDeliveryManager"8?0l
+ ___block_descriptor_32_e32_v16?0"<BKDisplayRenderSpace>"8l
+ ___block_descriptor_32_e35_v16?0"BKHIDEventDeliveryManager"8l
+ ___block_descriptor_32_e37_"BKHIDDirectTouchEventProcessor"8?0l
+ ___block_descriptor_32_e40_"BKHIDEventDeliveryObserverService"8?0l
+ ___block_descriptor_32_e40_"BKTouchDeliveryObservationManager"8?0l
+ ___block_descriptor_32_e40_v16?0"BKHIDDirectTouchEventProcessor"8l
+ ___block_descriptor_32_e43_v16?0"BKHIDEventDeliveryObserverService"8l
+ ___block_descriptor_32_e43_v16?0"BKTouchDeliveryObservationManager"8l
+ ___block_descriptor_40_e8_32bs_e42_16?0"<BSServiceConnectionCalloutType>"8ls32l8
+ ___block_descriptor_40_e8_32bs_e45_v24?0"<BSServiceConnectionCalloutType>"816ls32l8
+ ___block_descriptor_40_e8_32s_e50_v16?0"<BSServiceListenerConnectionConfiguring>"8ls32l8
+ ___block_descriptor_40_e8_32s_e5_8?0ls32l8
+ ___block_descriptor_64_e8_32s40bs48bs56r_e8_v16?08ls40l8s48l8r56l8s32l8
+ ___block_descriptor_64_e8_32s40s48bs56bs_e5_v8?0ls48l8s32l8s40l8s56l8
+ ___block_descriptor_72_e8_32bs40bs48bs56bs64r_e5_8?0ls32l8r64l8s40l8s48l8s56l8
+ _objc_msgSend$_contextualizerWrappingClientProvidedContextualizer:connection:getCurrent:setCurrent:
+ _objc_msgSend$_currentClientEnvironmentObjectForKey:
+ _objc_msgSend$_setCurrentClientEnvironmentObject:forKey:
+ _objc_msgSend$acceptConnectionUsingServiceQueue:clientCalloutContextualizer:
+ _objc_msgSend$acceptConnectionWithServiceQueue:clientCalloutContextualizer:
+ _objc_msgSend$acceptIncomingServiceConnection:serviceQueue:clientCalloutContextualizer:
+ _objc_msgSend$contextualizedMappedObjectFetcher
+ _objc_msgSend$currentThread
+ _objc_msgSend$performAsync:
+ _objc_msgSend$setCalloutContextualizer:
+ _objc_msgSend$setContextualizedMappedObjectFetcher:
+ _objc_msgSend$setSetupBlock:
+ _objc_msgSend$setTeardownBlock:
+ _objc_msgSend$setupBlock
+ _objc_msgSend$teardownBlock
+ _objc_msgSend$threadDictionary
- -[BKHIDDomainIncomingServiceConnection acceptConnection]
- -[BKHIDDomainServiceServer acceptIncomingServiceConnection:]
- -[BKHIDEventDeliveryManagerServer _deliveryManagerForEstablishedConnection:]
- -[BKHIDEventDeliveryManagerServer acceptIncomingServiceConnection:mappedObject:]
- -[BKHIDEventDeliveryObserverServer _deliveryObserverServiceForEstablishedConnection:]
- -[BKHIDEventDeliveryObserverServer acceptIncomingServiceConnection:mappedObject:]
- GCC_except_table213
- GCC_except_table248
- GCC_except_table301
- GCC_except_table359
- GCC_except_table372
- GCC_except_table375
- GCC_except_table381
- GCC_except_table384
- GCC_except_table39
- GCC_except_table621
- GCC_except_table624
- GCC_except_table658
- GCC_except_table707
- GCC_except_table768
- GCC_except_table780
- GCC_except_table812
- _OBJC_IVAR_$__BKEventObserverConnectionRecord._observerService
- ___60-[BKHIDDomainServiceServer acceptIncomingServiceConnection:]_block_invoke
- _objc_msgSend$acceptConnection
- _objc_msgSend$acceptIncomingServiceConnection:
- _objc_msgSend$acceptIncomingServiceConnection:mappedObject:
- _objc_msgSend$performAsyncAndWait:
- _objc_msgSend$queue
CStrings:
+ "+[BKHIDDomainClientCalloutContextualizer(ClientEnvironment) _contextualizerWrappingClientProvidedContextualizer:connection:getCurrent:setCurrent:]_block_invoke_2"
+ "+[BKHIDDomainServiceServer(ClientEnvironment) _setCurrentClientEnvironmentObject:forKey:]"
+ "@\"<BKDisplayRenderSpace>\"8@?0"
+ "@\"BKHIDDirectTouchEventProcessor\"8@?0"
+ "@\"BKHIDEventDeliveryManager\"8@?0"
+ "@\"BKHIDEventDeliveryObserverService\"8@?0"
+ "@\"BKTouchDeliveryObservationManager\"8@?0"
+ "@16@?0@\"<BSServiceConnectionCalloutType>\"8"
+ "BKHIDClientCalloutContextualizerSetupBlock for %@ stashed info with no teardownBlock to clean it up!"
+ "BKHIDDomainServiceServer_CurrentDeliveryManager"
+ "BKHIDDomainServiceServer_CurrentDisplayRenderSpace"
+ "BKHIDDomainServiceServer_CurrentHIDEventDeliveryObserverService"
+ "BKHIDDomainServiceServer_CurrentTouchDeliveryObservationManager"
+ "BKHIDDomainServiceServer_CurrentTouchProcessor"
+ "Delivery manager isn't configured"
+ "HID Event delivery observer service isn't configured"
+ "clientContextualizer"
+ "configuring connection (%{public}@) - %{public}@ with queue: %@"
+ "failed to provide a clientCalloutContextualizer for %@ while activating incoming connection: %@"
+ "failure in %{public}@ (%{public}@:%i) : %{public}@"
+ "getter"
+ "key"
+ "missing thread-local storage on %@"
+ "setter"
+ "v16@?0@\"<BKDisplayRenderSpace>\"8"
+ "v16@?0@\"BKHIDDirectTouchEventProcessor\"8"
+ "v16@?0@\"BKHIDEventDeliveryManager\"8"
+ "v16@?0@\"BKHIDEventDeliveryObserverService\"8"
+ "v16@?0@\"BKTouchDeliveryObservationManager\"8"
+ "v24@?0@\"<BSServiceConnectionCalloutType>\"8@16"
- "deliveryManager"
- "failed to find delivery manager for established connection: %@"
- "failed to find delivery observer service for established connection: %@"
- "failed to provide %@ while activating incoming connection: %@"
- "failed to provide delivery manager for incoming connection: %@"
- "failed to provide delivery observer service for incoming connection: %@"
- "no delivery observer service"
- "service"

```
