## CoreAudioOrchestration

> `/System/Library/PrivateFrameworks/CoreAudioOrchestration.framework/CoreAudioOrchestration`

```diff

-50.202.0.0.0
-  __TEXT.__text: 0x54d8c
-  __TEXT.__auth_stubs: 0x1440
-  __TEXT.__objc_methlist: 0x76c
-  __TEXT.__const: 0xaaa4
-  __TEXT.__gcc_except_tab: 0x52c
-  __TEXT.__cstring: 0x2242
-  __TEXT.__oslogstring: 0x16aa
-  __TEXT.__swift5_typeref: 0x2274
-  __TEXT.__swift5_fieldmd: 0x2128
-  __TEXT.__constg_swiftt: 0x3198
-  __TEXT.__swift5_reflstr: 0xef7
+50.408.0.0.0
+  __TEXT.__text: 0x59e00
+  __TEXT.__auth_stubs: 0x1460
+  __TEXT.__objc_methlist: 0x95c
+  __TEXT.__const: 0xb004
+  __TEXT.__gcc_except_tab: 0x888
+  __TEXT.__cstring: 0x2472
+  __TEXT.__oslogstring: 0x1bfa
+  __TEXT.__swift5_typeref: 0x2424
+  __TEXT.__swift5_fieldmd: 0x228c
+  __TEXT.__constg_swiftt: 0x353c
+  __TEXT.__swift5_reflstr: 0xff7
   __TEXT.__swift5_builtin: 0x8c
-  __TEXT.__swift5_assocty: 0x278
-  __TEXT.__swift5_protos: 0x40
-  __TEXT.__swift5_proto: 0x9a0
-  __TEXT.__swift5_types: 0x350
+  __TEXT.__swift5_assocty: 0x298
+  __TEXT.__swift5_protos: 0x50
+  __TEXT.__swift5_proto: 0x9e8
+  __TEXT.__swift5_types: 0x368
   __TEXT.__swift5_mpenum: 0x48
-  __TEXT.__swift5_capture: 0x2bc
-  __TEXT.__swift_as_entry: 0x2c
-  __TEXT.__swift_as_ret: 0x1c
-  __TEXT.__unwind_info: 0x1e58
-  __TEXT.__eh_frame: 0x2bd4
-  __TEXT.__objc_classname: 0x194
-  __TEXT.__objc_methname: 0xb71
-  __TEXT.__objc_methtype: 0xe3a
-  __TEXT.__objc_stubs: 0x4e0
-  __DATA_CONST.__got: 0x260
-  __DATA_CONST.__const: 0x58
-  __DATA_CONST.__objc_classlist: 0x208
-  __DATA_CONST.__objc_protolist: 0x68
+  __TEXT.__swift5_capture: 0x1b8
+  __TEXT.__unwind_info: 0x2070
+  __TEXT.__eh_frame: 0x2a28
+  __TEXT.__objc_classname: 0x2c2
+  __TEXT.__objc_methname: 0xf4c
+  __TEXT.__objc_methtype: 0x11e7
+  __TEXT.__objc_stubs: 0x8e0
+  __DATA_CONST.__got: 0x288
+  __DATA_CONST.__const: 0x98
+  __DATA_CONST.__objc_classlist: 0x240
+  __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x398
-  __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0xa30
-  __AUTH_CONST.__const: 0x5838
-  __AUTH_CONST.__cfstring: 0x160
-  __AUTH_CONST.__objc_const: 0x3e30
-  __AUTH.__objc_data: 0x820
-  __AUTH.__data: 0x33b0
-  __DATA.__objc_ivar: 0x3c
-  __DATA.__data: 0x1f50
-  __DATA.__bss: 0x12a20
-  __DATA.__common: 0x70
+  __DATA_CONST.__objc_selrefs: 0x4a0
+  __DATA_CONST.__objc_protorefs: 0x50
+  __DATA_CONST.__objc_superrefs: 0x38
+  __AUTH_CONST.__auth_got: 0xa40
+  __AUTH_CONST.__const: 0x59b0
+  __AUTH_CONST.__cfstring: 0x1a0
+  __AUTH_CONST.__objc_const: 0x4948
+  __AUTH.__objc_data: 0x978
+  __AUTH.__data: 0x3780
+  __DATA.__objc_ivar: 0x58
+  __DATA.__data: 0x22e0
+  __DATA.__bss: 0x13160
+  __DATA.__common: 0x48
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/caulk.framework/caulk
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 37CC443D-F6EE-3CA6-B3CF-9B462EF8C7E8
-  Functions: 2598
-  Symbols:   1901
-  CStrings:  589
+  UUID: 717382E4-5856-357C-A61C-E21E75AD4650
+  Functions: 2738
+  Symbols:   2242
+  CStrings:  708
 
Symbols:
+ +[ExclaveAudioFormatBase createFrom:forUseCase:destination:error:]
+ +[NSXPCConnection(XPC_Connection_PID_Access) getPIDFromCurrentConnection]
+ -[ADMDSPHostCallbacks .cxx_destruct]
+ -[ADMDSPHostCallbacks initWithHostCallbacks:]
+ -[ADMDSPHostCallbacks notifyClientsOfCustomPropertyChange:]
+ -[ADMDSPProcessorPropertySet .cxx_destruct]
+ -[ADMDSPProcessorPropertySet getHostedDSPPropertyAtAddress:withQualifierData:]
+ -[ADMDSPProcessorPropertySet getHostedDSPPropertyInfoArray]
+ -[ADMDSPProcessorPropertySet hasHostedDSPPropertyAtAddress:]
+ -[ADMDSPProcessorPropertySet initWithDSPPropertySet:]
+ -[ADMDSPProcessorPropertySet setHostedDSPPropertyAtAddress:withData:withQualifier:error:]
+ -[DSPController getProcessorPropertySet]
+ -[DSPController initWithBundleID:withLogger:andADMConfigurator:andHALDSPFactory:andHostCallbacks:]
+ -[MicActivityServiceDelegate .cxx_construct]
+ -[MicActivityServiceDelegate .cxx_destruct]
+ -[MicActivityServiceDelegate disableMicrophoneActivityDetection:]
+ -[MicActivityServiceDelegate enableMicrophoneActivityDetection:]
+ -[MicActivityServiceDelegate listenForMicrophoneActivity:reply:]
+ -[MicActivityServiceDelegate propertyChanged:]
+ -[MicActivityServiceDelegate selfConfigureMAD]
+ -[MicActivityServiceDelegate setDSPProcessorPropertySet:]
+ -[MicActivityServiceDelegate setSelfConfigureHandler:]
+ -[MicActivityServiceDelegate stopListeningForMicrophoneActivity:]
+ -[MicActivityServiceDelegate submitReferenceStreamUID:withReply:]
+ -[NSXPCConnection(XPC_Connection_PID_Access) getProcessID]
+ -[SelfConfigurationDescription .cxx_destruct]
+ -[SelfConfigurationDescription referenceDeviceUID]
+ -[SelfConfigurationDescription setReferenceDeviceUID:]
+ GCC_except_table26
+ GCC_except_table7
+ GCC_except_table9
+ _OBJC_CLASS_$_ADMDSPHostCallbacks
+ _OBJC_CLASS_$_ADMDSPProcessorPropertySet
+ _OBJC_CLASS_$_MicActivityServiceDelegate
+ _OBJC_CLASS_$_NSXPCConnection
+ _OBJC_CLASS_$_SelfConfigurationDescription
+ _OBJC_IVAR_$_ADMDSPHostCallbacks.hostCallbacks
+ _OBJC_IVAR_$_ADMDSPProcessorPropertySet.dspPropertySet
+ _OBJC_IVAR_$_DSPController.admHostCallbacks
+ _OBJC_IVAR_$_DSPController.admPropertySet
+ _OBJC_IVAR_$_MicActivityServiceDelegate.mMicActivityContext
+ _OBJC_IVAR_$_MicActivityServiceDelegate.mSelfConfigureGateway
+ _OBJC_IVAR_$_SelfConfigurationDescription._referenceDeviceUID
+ _OBJC_METACLASS_$_ADMDSPHostCallbacks
+ _OBJC_METACLASS_$_ADMDSPProcessorPropertySet
+ _OBJC_METACLASS_$_MicActivityServiceDelegate
+ _OBJC_METACLASS_$_SelfConfigurationDescription
+ __DATA__TtC22CoreAudioOrchestration16MicActivityRoute
+ __DATA__TtC22CoreAudioOrchestration20HistoricalAudioRoute
+ __DATA__TtC22CoreAudioOrchestration37ExitWhenAllProcessesDisconnectHandler
+ __DATA__TtCV22CoreAudioOrchestration25HALReferenceStreamControlP33_29BB33CCC407684894C614FC375C431020StreamConfigListener
+ __IVARS__TtC22CoreAudioOrchestration16MicActivityRoute
+ __IVARS__TtCV22CoreAudioOrchestration25HALReferenceStreamControlP33_29BB33CCC407684894C614FC375C431020StreamConfigListener
+ __METACLASS_DATA__TtC22CoreAudioOrchestration16MicActivityRoute
+ __METACLASS_DATA__TtC22CoreAudioOrchestration20HistoricalAudioRoute
+ __METACLASS_DATA__TtC22CoreAudioOrchestration37ExitWhenAllProcessesDisconnectHandler
+ __METACLASS_DATA__TtCV22CoreAudioOrchestration25HALReferenceStreamControlP33_29BB33CCC407684894C614FC375C431020StreamConfigListener
+ __NSConcreteGlobalBlock
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSXPCConnection_$_XPC_Connection_PID_Access
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSXPCConnection_$_XPC_Connection_PID_Access
+ __OBJC_$_CATEGORY_NSXPCConnection_$_XPC_Connection_PID_Access
+ __OBJC_$_INSTANCE_METHODS_ADMDSPHostCallbacks
+ __OBJC_$_INSTANCE_METHODS_ADMDSPProcessorPropertySet
+ __OBJC_$_INSTANCE_METHODS_MicActivityServiceDelegate
+ __OBJC_$_INSTANCE_METHODS_SelfConfigurationDescription
+ __OBJC_$_INSTANCE_VARIABLES_ADMDSPHostCallbacks
+ __OBJC_$_INSTANCE_VARIABLES_ADMDSPProcessorPropertySet
+ __OBJC_$_INSTANCE_VARIABLES_MicActivityServiceDelegate
+ __OBJC_$_INSTANCE_VARIABLES_SelfConfigurationDescription
+ __OBJC_$_PROP_LIST_ADMDSPHostCallbacks
+ __OBJC_$_PROP_LIST_SelfConfigurationDescription
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_DSPHostCallbacks
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_DSPProcessorPropertySet
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_DSPProcessorPropertySetHandler
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HAL_DSP_HostCallbacks
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MicActivityReverseClientProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SelfConfiguringClient
+ __OBJC_$_PROTOCOL_METHOD_TYPES_DSPHostCallbacks
+ __OBJC_$_PROTOCOL_METHOD_TYPES_DSPProcessorPropertySet
+ __OBJC_$_PROTOCOL_METHOD_TYPES_DSPProcessorPropertySetHandler
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HAL_DSP_HostCallbacks
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MicActivityReverseClientProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SelfConfiguringClient
+ __OBJC_$_PROTOCOL_REFS_DSPPropertySupervisor
+ __OBJC_$_PROTOCOL_REFS_HAL_DSP_HostCallbacks
+ __OBJC_CLASS_PROTOCOLS_$_ADMDSPHostCallbacks
+ __OBJC_CLASS_PROTOCOLS_$_ADMDSPProcessorPropertySet
+ __OBJC_CLASS_PROTOCOLS_$_MicActivityServiceDelegate
+ __OBJC_CLASS_RO_$_ADMDSPHostCallbacks
+ __OBJC_CLASS_RO_$_ADMDSPProcessorPropertySet
+ __OBJC_CLASS_RO_$_MicActivityServiceDelegate
+ __OBJC_CLASS_RO_$_SelfConfigurationDescription
+ __OBJC_LABEL_PROTOCOL_$_DSPHostCallbacks
+ __OBJC_LABEL_PROTOCOL_$_DSPProcessorPropertySet
+ __OBJC_LABEL_PROTOCOL_$_DSPProcessorPropertySetHandler
+ __OBJC_LABEL_PROTOCOL_$_DSPPropertySupervisor
+ __OBJC_LABEL_PROTOCOL_$_HAL_DSP_HostCallbacks
+ __OBJC_LABEL_PROTOCOL_$_MicActivityReverseClientProtocol
+ __OBJC_LABEL_PROTOCOL_$_SelfConfiguringClient
+ __OBJC_METACLASS_RO_$_ADMDSPHostCallbacks
+ __OBJC_METACLASS_RO_$_ADMDSPProcessorPropertySet
+ __OBJC_METACLASS_RO_$_MicActivityServiceDelegate
+ __OBJC_METACLASS_RO_$_SelfConfigurationDescription
+ __OBJC_PROTOCOL_$_DSPHostCallbacks
+ __OBJC_PROTOCOL_$_DSPProcessorPropertySet
+ __OBJC_PROTOCOL_$_DSPProcessorPropertySetHandler
+ __OBJC_PROTOCOL_$_DSPPropertySupervisor
+ __OBJC_PROTOCOL_$_HAL_DSP_HostCallbacks
+ __OBJC_PROTOCOL_$_MicActivityReverseClientProtocol
+ __OBJC_PROTOCOL_$_SelfConfiguringClient
+ __OBJC_PROTOCOL_REFERENCE_$_MicActivityReverseClientProtocol
+ __Z25ExADKeyNameForDestination23ExclaveAudioDestination
+ __Z25ExADUseCaseFormatsFromEDTPU38objcproto27EmbeddedDeviceTreeAudioInfo11objc_object23ExclaveAudioDestinationPU15__autoreleasingP7NSError
+ __Z34ExADUseCaseFormatForUseCaseFromEDTPU38objcproto27EmbeddedDeviceTreeAudioInfo11objc_objectj23ExclaveAudioDestinationPU15__autoreleasingP7NSError
+ __ZN17MicActivityClient21setReferenceDeviceUIDEP8NSString
+ __ZN17MicActivityClient25voiceActivityStateChangedEb
+ __ZN17MicActivityClientC1EP21NSXPCListenerEndpoint
+ __ZN17MicActivityClientC2EP21NSXPCListenerEndpoint
+ __ZN17MicActivityClientD1Ev
+ __ZN17MicActivityClientD2Ev
+ __ZN18MicActivityContext19addClientConnectionEiP21NSXPCListenerEndpoint
+ __ZN18MicActivityContext19processPropertyDataERK26AudioObjectPropertyAddressP6NSData
+ __ZN18MicActivityContext19processPropertyDataERK26AudioObjectPropertyAddressP6NSData.cold.1
+ __ZN18MicActivityContext22removeClientConnectionEi
+ __ZN18MicActivityContext23getQualifierForPropertyERK26AudioObjectPropertyAddress
+ __ZN18MicActivityContext24submitReferenceDeviceUIDEiP8NSString
+ __ZN18MicActivityContextC1Ev
+ __ZN18MicActivityContextC2Ev
+ __ZN18MicActivityContextD1Ev
+ __ZN18MicActivityContextD2Ev
+ __ZN20SelfConfigureGateway23setSelfConfigureHandlerEU13block_pointerFiP28SelfConfigurationDescriptionE
+ __ZN20SelfConfigureGatewayC1Ev
+ __ZN20SelfConfigureGatewayC2Ev
+ __ZN20SelfConfigureGatewayD1Ev
+ __ZN20SelfConfigureGatewayD2Ev
+ __ZN27DSPProcessorPropertyHandler15propertyChangedERK26AudioObjectPropertyAddress
+ __ZN27DSPProcessorPropertyHandler26setDSPProcessorPropertySetEPU34objcproto23DSPProcessorPropertySet11objc_object
+ __ZN27DSPProcessorPropertyHandlerC2Ev
+ __ZN27DSPProcessorPropertyHandlerD1Ev
+ __ZN27DSPProcessorPropertyHandlerD2Ev
+ __ZN27MicActivityClientConnectionC1EP21NSXPCListenerEndpoint
+ __ZN27MicActivityClientConnectionC2EP21NSXPCListenerEndpoint
+ __ZN27MicActivityClientConnectionD1Ev
+ __ZN27MicActivityClientConnectionD2Ev
+ __ZN28MicActivityClientConnections19addClientConnectionEiP21NSXPCListenerEndpoint
+ __ZN28MicActivityClientConnections22determinePrimaryClientEv
+ __ZN28MicActivityClientConnections22removeClientConnectionEi
+ __ZN28MicActivityClientConnections24submitReferenceDeviceUIDEiP8NSString
+ __ZN28MicActivityClientConnections25voiceActivityStateChangedEb
+ __ZN28MicActivityClientConnectionsC1Ev
+ __ZN28MicActivityClientConnectionsC2Ev
+ __ZN28MicActivityClientConnectionsD1Ev
+ __ZN28MicActivityClientConnectionsD2Ev
+ __ZNK17MicActivityClient21getReferenceDeviceUIDEv
+ __ZNK18MicActivityContext15isPrimaryClientEi
+ __ZNK18MicActivityContext34getPrimaryClientReferenceDeviceUIDEv
+ __ZNK20SelfConfigureGateway20executeSelfConfigureEP28SelfConfigurationDescription
+ __ZNK20SelfConfigureGateway20executeSelfConfigureEP28SelfConfigurationDescription.cold.1
+ __ZNK27MicActivityClientConnection25voiceActivityStateChangedEb
+ __ZNK28MicActivityClientConnections15isPrimaryClientEi
+ __ZNK28MicActivityClientConnections34getPrimaryClientReferenceDeviceUIDEv
+ __ZNSt3__110unique_ptrI17MicActivityClientNS_14default_deleteIS1_EEE5resetB8ne200100EPS1_
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeIiNS0_I17MicActivityClientNS_14default_deleteIS3_EEEEEEPvEENS_22__tree_node_destructorINS_9allocatorIS9_EEEEED1B8ne200100Ev
+ __ZNSt3__113__tree_removeB8ne200100IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__119piecewise_constructE
+ __ZNSt3__127__tree_balance_after_insertB8ne200100IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__15mutex4lockEv
+ __ZNSt3__15mutex6unlockEv
+ __ZNSt3__15mutexD1Ev
+ __ZNSt3__16__treeINS_12__value_typeIiNS_10unique_ptrI17MicActivityClientNS_14default_deleteIS3_EEEEEENS_19__map_value_compareIiS7_NS_4lessIiEELb1EEENS_9allocatorIS7_EEE14__erase_uniqueIiEEmRKT_
+ __ZNSt3__16__treeINS_12__value_typeIiNS_10unique_ptrI17MicActivityClientNS_14default_deleteIS3_EEEEEENS_19__map_value_compareIiS7_NS_4lessIiEELb1EEENS_9allocatorIS7_EEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSJ_SJ_
+ __ZNSt3__16__treeINS_12__value_typeIiNS_10unique_ptrI17MicActivityClientNS_14default_deleteIS3_EEEEEENS_19__map_value_compareIiS7_NS_4lessIiEELb1EEENS_9allocatorIS7_EEE21__remove_node_pointerEPNS_11__tree_nodeIS7_PvEE
+ __ZNSt3__16__treeINS_12__value_typeIiNS_10unique_ptrI17MicActivityClientNS_14default_deleteIS3_EEEEEENS_19__map_value_compareIiS7_NS_4lessIiEELb1EEENS_9allocatorIS7_EEE25__emplace_unique_key_argsIiJRKNS_21piecewise_construct_tENS_5tupleIJRKiEEENSJ_IJEEEEEENS_4pairINS_15__tree_iteratorIS7_PNS_11__tree_nodeIS7_PvEElEEbEERKT_DpOT0_
+ __ZNSt3__16__treeINS_12__value_typeIiNS_10unique_ptrI17MicActivityClientNS_14default_deleteIS3_EEEEEENS_19__map_value_compareIiS7_NS_4lessIiEELb1EEENS_9allocatorIS7_EEE5eraseENS_21__tree_const_iteratorIS7_PNS_11__tree_nodeIS7_PvEElEE
+ __ZNSt3__16__treeINS_12__value_typeIiNS_10unique_ptrI17MicActivityClientNS_14default_deleteIS3_EEEEEENS_19__map_value_compareIiS7_NS_4lessIiEELb1EEENS_9allocatorIS7_EEE7destroyEPNS_11__tree_nodeIS7_PvEE
+ __ZTI18MicActivityContext
+ __ZTI27DSPProcessorPropertyHandler
+ __ZTS18MicActivityContext
+ __ZTS27DSPProcessorPropertyHandler
+ __ZTV18MicActivityContext
+ __ZTV27DSPProcessorPropertyHandler
+ ____ZN27MicActivityClientConnectionC2EP21NSXPCListenerEndpoint_block_invoke
+ ____ZNK27MicActivityClientConnection25voiceActivityStateChangedEb_block_invoke
+ ____ZZN27MicActivityClientConnectionC1EP21NSXPCListenerEndpointENK3$_0cvU13block_pointerFvvEEv_block_invoke
+ ____ZZN27MicActivityClientConnectionC1EP21NSXPCListenerEndpointENK3$_1cvU13block_pointerFvvEEv_block_invoke
+ ___block_descriptor_32_e17_v16?0"NSError"8l
+ ___block_descriptor_32_e8_v12?0i8l
+ ___block_descriptor_33_ea8_32c68_ZTSKZN27MicActivityClientConnectionC1EP21NSXPCListenerEndpointE3$_1_e5_v8?0l
+ ___block_descriptor_40_ea8_32c68_ZTSKZN27MicActivityClientConnectionC1EP21NSXPCListenerEndpointE3$_0_e5_v8?0l
+ ___block_literal_global
+ ___block_literal_global.6
+ ___copy_helper_block_ea8_32c68_ZTSKZN27MicActivityClientConnectionC1EP21NSXPCListenerEndpointE3$_0
+ ___copy_helper_block_ea8_32c68_ZTSKZN27MicActivityClientConnectionC1EP21NSXPCListenerEndpointE3$_1
+ ___cxa_pure_virtual
+ ___destroy_helper_block_ea8_32
+ ___destroy_helper_block_ea8_32c68_ZTSKZN27MicActivityClientConnectionC1EP21NSXPCListenerEndpointE3$_0
+ ___swift_memcpy48_8
+ ___swift_memcpy66_8
+ _associated conformance 22CoreAudioOrchestration0aB21OrchestratorServerXPCC19GetHiddenDeviceUIDsV10CodingKeys33_521AA05610F1767FACEC4E5A11A48B45LLOSHAASQ
+ _associated conformance 22CoreAudioOrchestration0aB21OrchestratorServerXPCC19GetHiddenDeviceUIDsV10CodingKeys33_521AA05610F1767FACEC4E5A11A48B45LLOs0K3KeyAAs23CustomStringConvertible
+ _associated conformance 22CoreAudioOrchestration0aB21OrchestratorServerXPCC19GetHiddenDeviceUIDsV10CodingKeys33_521AA05610F1767FACEC4E5A11A48B45LLOs0K3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 22CoreAudioOrchestration0aB21OrchestratorServerXPCC19GetHiddenDeviceUIDsVAA0abdF0C18XPCRequestProtocolAA7RequestAgHP_SE
+ _associated conformance 22CoreAudioOrchestration0aB21OrchestratorServerXPCC19GetHiddenDeviceUIDsVAA0abdF0C18XPCRequestProtocolAA7RequestAgHP_Se
+ _associated conformance 22CoreAudioOrchestration0aB21OrchestratorServerXPCC19GetHiddenDeviceUIDsVAA0abdF0C18XPCRequestProtocolAA8ResponseAgHP_SE
+ _associated conformance 22CoreAudioOrchestration0aB21OrchestratorServerXPCC19GetHiddenDeviceUIDsVAA0abdF0C18XPCRequestProtocolAA8ResponseAgHP_Se
+ _associated conformance 22CoreAudioOrchestration0aB21OrchestratorServerXPCC7RequestO29GetHiddenDeviceUIDSCodingKeys33_521AA05610F1767FACEC4E5A11A48B45LLOSHAASQ
+ _associated conformance 22CoreAudioOrchestration0aB21OrchestratorServerXPCC7RequestO29GetHiddenDeviceUIDSCodingKeys33_521AA05610F1767FACEC4E5A11A48B45LLOs9CodingKeyAAs23CustomStringConvertible
+ _associated conformance 22CoreAudioOrchestration0aB21OrchestratorServerXPCC7RequestO29GetHiddenDeviceUIDSCodingKeys33_521AA05610F1767FACEC4E5A11A48B45LLOs9CodingKeyAAs28CustomDebugStringConvertible
+ _audit_token_to_pid
+ _block_copy_helper.25
+ _block_descriptor.27
+ _block_destroy_helper.26
+ _flat unique So21DSPPropertySupervisor_p
+ _flat unique So21SelfConfiguringClient_p
+ _objc_msgSend$auditToken
+ _objc_msgSend$code
+ _objc_msgSend$currentConnection
+ _objc_msgSend$destroyHALIOProc
+ _objc_msgSend$destroyHALLapseEventListeners
+ _objc_msgSend$getBytes:length:
+ _objc_msgSend$getHostedDSPPropertyAtAddress:withQualifierData:
+ _objc_msgSend$getHostedDSPPropertyInfoArray
+ _objc_msgSend$getPIDFromCurrentConnection
+ _objc_msgSend$getProcessID
+ _objc_msgSend$getProcessorPropertySet
+ _objc_msgSend$hasHostedDSPPropertyAtAddress:
+ _objc_msgSend$initWithDSPPropertySet:
+ _objc_msgSend$initWithHostCallbacks:
+ _objc_msgSend$initWithListenerEndpoint:
+ _objc_msgSend$initWithString:
+ _objc_msgSend$interfaceWithProtocol:
+ _objc_msgSend$invalidate
+ _objc_msgSend$length
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$localizedFailureReason
+ _objc_msgSend$localizedRecoverySuggestion
+ _objc_msgSend$microphoneActivityStateChanged:reply:
+ _objc_msgSend$propertyChanged:
+ _objc_msgSend$resume
+ _objc_msgSend$selfConfigureMAD
+ _objc_msgSend$setHostedDSPPropertyAtAddress:withData:withQualifier:error:
+ _objc_msgSend$setInterruptionHandler:
+ _objc_msgSend$setInvalidationHandler:
+ _objc_msgSend$setReferenceDeviceUID:
+ _objc_msgSend$setRemoteObjectInterface:
+ _objc_msgSend$synchronousRemoteObjectProxyWithErrorHandler:
+ _objc_retainBlock
+ _objc_retain_x1
+ _objc_retain_x25
+ _objc_retain_x28
+ _symbolic $s22CoreAudioOrchestration0B17HALStreamProtocolP
+ _symbolic $s22CoreAudioOrchestration0B21HALHasStreamsProtocolP
+ _symbolic $s22CoreAudioOrchestration0B27HALPropertyGetSetListenableP
+ _symbolic $s22CoreAudioOrchestration24ProcessConnectionHandlerP
+ _symbolic _____ 22CoreAudioOrchestration010HistoricalB5RouteC
+ _symbolic _____ 22CoreAudioOrchestration0aB21OrchestratorServerXPCC19GetHiddenDeviceUIDsV
+ _symbolic _____ 22CoreAudioOrchestration0aB21OrchestratorServerXPCC19GetHiddenDeviceUIDsV10CodingKeys33_521AA05610F1767FACEC4E5A11A48B45LLO
+ _symbolic _____ 22CoreAudioOrchestration0aB21OrchestratorServerXPCC7RequestO29GetHiddenDeviceUIDSCodingKeys33_521AA05610F1767FACEC4E5A11A48B45LLO
+ _symbolic _____ 22CoreAudioOrchestration16MicActivityRouteC
+ _symbolic _____ 22CoreAudioOrchestration25HALReferenceStreamControlV
+ _symbolic _____ 22CoreAudioOrchestration25HALReferenceStreamControlV0E14ConfigListener33_29BB33CCC407684894C614FC375C4310LLC
+ _symbolic _____ 22CoreAudioOrchestration37ExitWhenAllProcessesDisconnectHandlerC
+ _symbolic ______p So21DSPPropertySupervisorP
+ _symbolic ______p So21SelfConfiguringClientP
+ _symbolic ______pSg 22CoreAudioOrchestration24ProcessConnectionHandlerP
+ _symbolic _____y_ShySSGG 22CoreAudioOrchestration0aB15OrchestratorXPCC8ResponseO
+ _symbolic _____y_ShySSGGSg 22CoreAudioOrchestration0aB15OrchestratorXPCC8ResponseO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 22CoreAudioOrchestration0dE21OrchestratorServerXPCC19GetHiddenDeviceUIDsV10CodingKeys33_521AA05610F1767FACEC4E5A11A48B45LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 22CoreAudioOrchestration0dE21OrchestratorServerXPCC7RequestO29GetHiddenDeviceUIDSCodingKeys33_521AA05610F1767FACEC4E5A11A48B45LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 22CoreAudioOrchestration0dE21OrchestratorServerXPCC19GetHiddenDeviceUIDsV10CodingKeys33_521AA05610F1767FACEC4E5A11A48B45LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 22CoreAudioOrchestration0dE21OrchestratorServerXPCC7RequestO29GetHiddenDeviceUIDSCodingKeys33_521AA05610F1767FACEC4E5A11A48B45LLO
+ _symbolic yycSg
+ _type_layout_string 22CoreAudioOrchestration0aB21OrchestratorServerXPCC19GetHiddenDeviceUIDsV
+ _usleep
- +[ExclaveAudioFormatBase createFrom:forUseCase:error:]
- -[DSPController initWithBundleID:withLogger:andADMConfigurator:andHALDSPFactory:]
- GCC_except_table16
- GCC_except_table20
- __DATA__TtC22CoreAudioOrchestration26MicActivityServiceDelegate
- __INSTANCE_METHODS__TtC22CoreAudioOrchestration26MicActivityServiceDelegate
- __METACLASS_DATA__TtC22CoreAudioOrchestration26MicActivityServiceDelegate
- __PROTOCOLS__TtC22CoreAudioOrchestration26MicActivityServiceDelegate
- __PROTOCOLS__TtC22CoreAudioOrchestration26MicActivityServiceDelegate.2
- __Z25ExADUseCaseFormatsFromEDTPU38objcproto27EmbeddedDeviceTreeAudioInfo11objc_objectPU15__autoreleasingP7NSError
- __Z34ExADUseCaseFormatForUseCaseFromEDTPU38objcproto27EmbeddedDeviceTreeAudioInfo11objc_objectjPU15__autoreleasingP7NSError
- ___swift_async_entry_functlets
- ___swift_async_ret_functlets
- ___swift_memcpy37_8
- ___swift_memcpy58_8
- _block_copy_helper.24
- _block_descriptor.26
- _block_destroy_helper.25
- _objc_retain_x27
- _objectdestroy.8Tm
- _swift_deletedAsyncMethodErrorTu
- _swift_task_alloc
- _swift_task_create
- _swift_task_dealloc
- _swift_task_switch
- _symbolic IeAgH_
- _symbolic IeghH_
- _symbolic ScA_pSg
- _symbolic ScPSg
- _symbolic So21NSXPCListenerEndpointCSg
- _symbolic _____ 22CoreAudioOrchestration26MicActivityServiceDelegateC
- _symbolic _____IeyBhy_Sg s5Int32V
- _symbolic ytIeAgHr_
CStrings:
+ ""
+ "%25s:%-5d  Code:\t\t\t%ld"
+ "%25s:%-5d  Description:\t%@"
+ "%25s:%-5d  Reason:\t\t%@"
+ "%25s:%-5d  Suggestion:\t%@"
+ "%25s:%-5d Attempt to connect to MAD client via XPC failed."
+ "%25s:%-5d Connecting the DSP Property Set"
+ "%25s:%-5d Connection with client was invalidated!"
+ "%25s:%-5d Disabling mic activity detection - THIS SHOULD NOT BE CALLED"
+ "%25s:%-5d Enabling mic activity detection - THIS SHOULD NOT BE CALLED"
+ "%25s:%-5d Listening for mic activity detection - %d"
+ "%25s:%-5d MicActivityContext::processPropertyData - voiceActivityChanged => %d"
+ "%25s:%-5d Received property change for: %u"
+ "%25s:%-5d Self configure handle did not become available after %u retries"
+ "%25s:%-5d Should send client an update"
+ "%25s:%-5d Stop listenting for mic activity detection - %d"
+ "%25s:%-5d Submitted reference device ID: %@"
+ "%25s:%-5d microphoneActivityStateChanged - in reply block!"
+ "%s: Invalid arguments: %p\n"
+ "1"
+ "@\"<DSPHostCallbacks>\""
+ "@\"<HAL_DSP_PropertySet>\""
+ "@\"ADMDSPHostCallbacks\""
+ "@\"ADMDSPProcessorPropertySet\""
+ "@\"NSData\"36@0:8{AudioObjectPropertyAddress=III}16@\"NSData\"28"
+ "@\"NSString\""
+ "@36@0:8{AudioObjectPropertyAddress=III}16@28"
+ "@40@0:8@16I24i28^@32"
+ "@56@0:8@16@24@32@40@48"
+ "ADMDSPHostCallbacks"
+ "ADMDSPProcessorPropertySet"
+ "B28@0:8{AudioObjectPropertyAddress=III}16"
+ "B52@0:8{AudioObjectPropertyAddress=III}16@28@36^@44"
+ "BuiltInMicrophoneDevice"
+ "Client requested hidden deviceUIDs: %s"
+ "DSPHostCallbacks"
+ "DSPProcessorPropertySet"
+ "DSPProcessorPropertySetHandler"
+ "DSPPropertySupervisor"
+ "Defaulting to no hidden device UIDS"
+ "Defaulting to no required ADM input streams"
+ "Defaulting to no required ADM reference streams"
+ "Defaulting to no required aggregate devices"
+ "Defaulting to no required device UIDS"
+ "HAL_DSP_HostCallbacks"
+ "Ignoring provided devicueUIDs!"
+ "Ignoring provided reference UID!"
+ "Incoming connection is missing required entitlement - %s!"
+ "MicActivityClientConnection.mm"
+ "MicActivityContext.mm"
+ "MicActivityReverseClientProtocol"
+ "MicActivityServiceDelegate"
+ "MicActivityServiceDelegate.mm"
+ "Reference UID: %s"
+ "Self Configuring resulted in: %d"
+ "SelfConfigurationDescription"
+ "SelfConfigureGateway.mm"
+ "SelfConfiguringClient"
+ "Starting IO resulted in: %d"
+ "Stopping IO resulted in: %d"
+ "T@\"NSString\",&,N,V_referenceDeviceUID"
+ "XPC_Connection_PID_Access"
+ "_TtC22CoreAudioOrchestration16MicActivityRoute"
+ "_TtC22CoreAudioOrchestration20HistoricalAudioRoute"
+ "_TtC22CoreAudioOrchestration37ExitWhenAllProcessesDisconnectHandler"
+ "_TtCV22CoreAudioOrchestration25HALReferenceStreamControlP33_29BB33CCC407684894C614FC375C431020StreamConfigListener"
+ "_referenceDeviceUID"
+ "admHostCallbacks"
+ "admPropertySet"
+ "auditToken"
+ "code"
+ "com.apple.audio.historicalaudio"
+ "com.apple.audio.micactivityd"
+ "createFrom:forUseCase:destination:error:"
+ "currentConnection"
+ "dspPropertySet"
+ "foundAvailableDeviceIDs"
+ "getADMConfiguration no input stream"
+ "getADMConfiguration no reference stream device: %s"
+ "getADMConfiguration reference stream device: %s"
+ "getBytes:length:"
+ "getHiddenDeviceUIDS"
+ "getHostedDSPPropertyAtAddress:withQualifierData:"
+ "getHostedDSPPropertyInfoArray"
+ "getPIDFromCurrentConnection"
+ "getProcessID"
+ "getProcessorPropertySet"
+ "hasHostedDSPPropertyAtAddress:"
+ "hostCallbacks"
+ "i16@?0@\"SelfConfigurationDescription\"8"
+ "initWithBundleID:withLogger:andADMConfigurator:andHALDSPFactory:andHostCallbacks:"
+ "initWithDSPPropertySet:"
+ "initWithHostCallbacks:"
+ "initWithListenerEndpoint:"
+ "initWithString:"
+ "integerValue"
+ "invalidate"
+ "isReference"
+ "length"
+ "localizedFailureReason"
+ "localizedRecoverySuggestion"
+ "mMicActivityContext"
+ "mSelfConfigureGateway"
+ "microphoneActivityStateChanged:reply:"
+ "notifyClientsOfCustomPropertyChange:"
+ "processConnectionHandler"
+ "propertyChanged:"
+ "referenceDeviceUID"
+ "resume"
+ "selfConfigureMAD"
+ "setDSPProcessorPropertySet:"
+ "setHostedDSPPropertyAtAddress:withData:withQualifier:error:"
+ "setReferenceDeviceUID:"
+ "setRemoteObjectInterface:"
+ "setSelfConfigureHandler:"
+ "streamConfigDidChange"
+ "submitReferenceStreamUID:withReply:"
+ "synchronousRemoteObjectProxyWithErrorHandler:"
+ "use-case-dsp-in-format"
+ "v12@?0i8"
+ "v16@?0@\"NSError\"8"
+ "v24@0:8@\"<DSPProcessorPropertySet>\"16"
+ "v24@0:8@16"
+ "v24@0:8@?<i@?@\"SelfConfigurationDescription\">16"
+ "v28@0:8B16@?20"
+ "v28@0:8B16@?<v@?i>20"
+ "v28@0:8{AudioObjectPropertyAddress=III}16"
+ "v32@0:8@\"NSString\"16@?<v@?i>24"
+ "valueForEntitlement:"
+ "{MicActivityContext=\"_vptr$DSPProcessorPropertyHandler\"^^?\"mPropertySet\"@\"<DSPProcessorPropertySet>\"\"mClientConnections\"{unique_ptr<MicActivityClientConnections, std::default_delete<MicActivityClientConnections>>=\"\"{?=\"__ptr_\"^{MicActivityClientConnections}}}}"
+ "{SelfConfigureGateway=\"mHandler\"@?\"mSelfConfigureHandleSet\"{atomic<bool>=\"__a_\"{__cxx_atomic_impl<bool, std::__cxx_atomic_base_impl<bool>>=\"__a_value\"AB}}}"
- "%s: Invalid argumnents: %p\n"
- "@36@0:8@16I24^@28"
- "@48@0:8@16@24@32@40"
- "Disabling mic activity detection"
- "Enabling mic activity detection"
- "Listening for mic activity detection"
- "Stop listenting for mic activity detection"
- "_TtC22CoreAudioOrchestration26MicActivityServiceDelegate"
- "com.apple.private.audio.orchestration.micactivityd"
- "createFrom:forUseCase:error:"
- "getADMConfigurationHAD"
- "initWithBundleID:withLogger:andADMConfigurator:andHALDSPFactory:"

```
