## CoreAudioOrchestration

> `/System/Library/PrivateFrameworks/CoreAudioOrchestration.framework/Versions/A/CoreAudioOrchestration`

```diff

-23.0.0.0.0
-  __TEXT.__text: 0x3f798
-  __TEXT.__auth_stubs: 0x1070
-  __TEXT.__objc_methlist: 0x3a4
-  __TEXT.__const: 0x6868
-  __TEXT.__gcc_except_tab: 0x238
-  __TEXT.__cstring: 0x1b40
-  __TEXT.__oslogstring: 0xaad
-  __TEXT.__constg_swiftt: 0x2440
-  __TEXT.__swift5_typeref: 0x1635
-  __TEXT.__swift5_reflstr: 0x9f5
-  __TEXT.__swift5_fieldmd: 0x1730
+31.0.0.0.0
+  __TEXT.__text: 0x4544c
+  __TEXT.__auth_stubs: 0x1140
+  __TEXT.__init_offsets: 0x4
+  __TEXT.__objc_methlist: 0x4b4
+  __TEXT.__const: 0x6f38
+  __TEXT.__gcc_except_tab: 0x2d4
+  __TEXT.__cstring: 0x1c10
+  __TEXT.__oslogstring: 0xd9d
+  __TEXT.__constg_swiftt: 0x25b4
+  __TEXT.__swift5_typeref: 0x17c9
+  __TEXT.__swift5_reflstr: 0xa30
+  __TEXT.__swift5_fieldmd: 0x184c
   __TEXT.__swift5_builtin: 0x50
-  __TEXT.__swift5_assocty: 0x130
-  __TEXT.__swift5_proto: 0x680
-  __TEXT.__swift5_types: 0x268
+  __TEXT.__swift5_assocty: 0x118
+  __TEXT.__swift5_proto: 0x700
+  __TEXT.__swift5_types: 0x288
   __TEXT.__swift5_protos: 0x18
   __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__swift5_capture: 0x90
-  __TEXT.__unwind_info: 0x1630
-  __TEXT.__eh_frame: 0x1e60
-  __TEXT.__objc_classname: 0x98
-  __TEXT.__objc_methname: 0x593
-  __TEXT.__objc_methtype: 0xe00
-  __TEXT.__objc_stubs: 0x240
-  __DATA_CONST.__got: 0x1d8
+  __TEXT.__swift5_capture: 0xa0
+  __TEXT.__unwind_info: 0x1768
+  __TEXT.__eh_frame: 0x2070
+  __TEXT.__objc_classname: 0xdd
+  __TEXT.__objc_methname: 0x6d4
+  __TEXT.__objc_methtype: 0xefc
+  __TEXT.__objc_stubs: 0x260
+  __DATA_CONST.__got: 0x1e0
   __DATA_CONST.__const: 0x90
   __DATA_CONST.__objc_classlist: 0x188
-  __DATA_CONST.__objc_protolist: 0x28
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f8
-  __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x848
-  __AUTH_CONST.__auth_ptr: 0x6d0
-  __AUTH_CONST.__const: 0x3620
+  __DATA_CONST.__objc_selrefs: 0x250
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_superrefs: 0x20
+  __AUTH_CONST.__auth_got: 0x8b0
+  __AUTH_CONST.__auth_ptr: 0x730
+  __AUTH_CONST.__const: 0x3bf0
   __AUTH_CONST.__cfstring: 0x60
-  __AUTH_CONST.__objc_const: 0x2a60
-  __AUTH.__objc_data: 0x250
-  __AUTH.__data: 0x2b88
-  __DATA.__objc_ivar: 0x28
-  __DATA.__data: 0x15a0
-  __DATA.__bss: 0xce00
+  __AUTH_CONST.__objc_const: 0x2b40
+  __AUTH.__objc_data: 0x2a0
+  __AUTH.__data: 0x2ba0
+  __DATA.__objc_ivar: 0x30
+  __DATA.__data: 0x1750
+  __DATA.__bss: 0xde40
   __DATA.__common: 0x30
   - /System/Library/Frameworks/CoreAudio.framework/Versions/A/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/Versions/A/FeatureFlags
+  - /System/Library/PrivateFrameworks/caulk.framework/Versions/A/caulk
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1845
-  Symbols:   1101
-  CStrings:  387
+  Functions: 1961
+  Symbols:   1210
+  CStrings:  426
 
Symbols:
+ -[OrchestratorClientIOLapseHandler .cxx_construct]
+ -[OrchestratorClientIOLapseHandler .cxx_destruct]
+ -[OrchestratorClientIOLapseHandler createHALLapseEventListeners:]
+ -[OrchestratorClientIOLapseHandler destroyHALLapseEventListeners]
+ -[OrchestratorClientIOLapseHandler init]
+ -[OrchestratorClientIOLapseHandler installClientLapseHandler:data:]
+ -[OrchestratorClientIOLapseHandler ioHasStartedOnDevice:]
+ -[OrchestratorClientIOProc init]
+ GCC_except_table14
+ GCC_except_table4
+ OBJC_IVAR_$_OrchestratorClientIOLapseHandler.mDeviceID
+ OBJC_IVAR_$_OrchestratorClientIOLapseHandler.mLapseHandler
+ _AudioObjectAddPropertyListener
+ _AudioObjectGetPropertyData
+ _AudioObjectRemovePropertyListener
+ _GLOBAL__sub_I_HALEventListener.cpp
+ _InstallCallbackForOrchestratorLapseHandling
+ _OBJC_CLASS_$_OrchestratorClientIOLapseHandler
+ _OBJC_METACLASS_$_OrchestratorClientIOLapseHandler
+ _ZL34sIsolatedCoreAudioOrchestrationLogv.cold.1
+ __MergedGlobals
+ __OBJC_$_INSTANCE_METHODS_OrchestratorClientIOLapseHandler
+ __OBJC_$_INSTANCE_VARIABLES_OrchestratorClientIOLapseHandler
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CoreAudioOrchestrationEventCallback
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CoreAudioOrchestrationEventCallback
+ __OBJC_CLASS_RO_$_OrchestratorClientIOLapseHandler
+ __OBJC_LABEL_PROTOCOL_$_CoreAudioOrchestrationEventCallback
+ __OBJC_METACLASS_RO_$_OrchestratorClientIOLapseHandler
+ __OBJC_PROTOCOL_$_CoreAudioOrchestrationEventCallback
+ __Z33CreateLapseHandlingEventListenersjP20LapseHandlerCallable
+ __Z34DestroyLapseHandlingEventListenersj
+ __ZL12kLapseEvents
+ __ZL15kIsAliveAddress
+ __ZL16callLapseHandlerPv
+ __ZL17kIsRunningAddress
+ __ZL25kStoppedAbnormallyAddress
+ __ZL34IsolatedDeviceIsAliveEventListenerjjPK26AudioObjectPropertyAddressPv
+ __ZL34sIsolatedCoreAudioOrchestrationLogv
+ __ZL36IsolatedDeviceIsRunningEventListenerjjPK26AudioObjectPropertyAddressPv
+ __ZL42IsolatedDeviceStoppedAbruptlyEventListenerjjPK26AudioObjectPropertyAddressPv
+ __ZN14IOLapseHandler15setIOHasStartedEb
+ __ZN14IOLapseHandlerC1EPFviPvES0_
+ __ZN14IOLapseHandlerC2EPFviPvES0_
+ __ZN14IOLapseHandlerD1Ev
+ __ZN14IOLapseHandlerD2Ev
+ __ZN5ADMIOaSERKS_
+ __ZNK14IOLapseHandler11handleLapseEi
+ __ZNSt3__110unique_ptrI14IOLapseHandlerNS_14default_deleteIS1_EEE5resetB8ne190102EPS1_
+ __ZNSt3__16vectorI15AudioBufferListNS_9allocatorIS1_EEE18__assign_with_sizeB8ne190102IPS1_S6_EEvT_T0_l
+ __ZNSt3__16vectorIN4AMCP11Proc_StreamENS_9allocatorIS2_EEE18__assign_with_sizeB8ne190102IPS2_S7_EEvT_T0_l
+ __ZNSt3__16vectorINS_4pairI26AudioObjectPropertyAddressPFijjPKS2_PvEEENS_9allocatorIS8_EEED1B8ne190102Ev
+ __ZTI14IOLapseHandler
+ __ZTI20LapseHandlerCallable
+ __ZTS14IOLapseHandler
+ __ZTS20LapseHandlerCallable
+ __ZTV14IOLapseHandler
+ __ZTVN10__cxxabiv120__si_class_type_infoE
+ __ZdlPvSt19__type_descriptor_t
+ __ZnwmSt19__type_descriptor_t
+ ___cxa_atexit
+ ___cxa_guard_acquire
+ ___cxa_guard_release
+ ___swift_memcpy17_8
+ _associated conformance 22CoreAudioOrchestration11BoolPayloadV10CodingKeys33_6F4531C893BD5814AC9E03CE6767CBEELLOSHAASQ
+ _associated conformance 22CoreAudioOrchestration11BoolPayloadV10CodingKeys33_6F4531C893BD5814AC9E03CE6767CBEELLOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 22CoreAudioOrchestration11BoolPayloadV10CodingKeys33_6F4531C893BD5814AC9E03CE6767CBEELLOs0F3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 22CoreAudioOrchestration25GetPropertyResponseHeaderV10CodingKeys33_6F4531C893BD5814AC9E03CE6767CBEELLOSHAASQ
+ _associated conformance 22CoreAudioOrchestration25GetPropertyResponseHeaderV10CodingKeys33_6F4531C893BD5814AC9E03CE6767CBEELLOs0H3KeyAAs23CustomStringConvertible
+ _associated conformance 22CoreAudioOrchestration25GetPropertyResponseHeaderV10CodingKeys33_6F4531C893BD5814AC9E03CE6767CBEELLOs0H3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 22CoreAudioOrchestration27ActivateConfigurationHeaderV10CodingKeys33_48A86D0391A9583A57CF362431FE5C75LLOSHAASQ
+ _associated conformance 22CoreAudioOrchestration27ActivateConfigurationHeaderV10CodingKeys33_48A86D0391A9583A57CF362431FE5C75LLOs0G3KeyAAs23CustomStringConvertible
+ _associated conformance 22CoreAudioOrchestration27ActivateConfigurationHeaderV10CodingKeys33_48A86D0391A9583A57CF362431FE5C75LLOs0G3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 22CoreAudioOrchestration29DeactivateConfigurationHeaderV10CodingKeys33_48A86D0391A9583A57CF362431FE5C75LLOSHAASQ
+ _associated conformance 22CoreAudioOrchestration29DeactivateConfigurationHeaderV10CodingKeys33_48A86D0391A9583A57CF362431FE5C75LLOs0G3KeyAAs23CustomStringConvertible
+ _associated conformance 22CoreAudioOrchestration29DeactivateConfigurationHeaderV10CodingKeys33_48A86D0391A9583A57CF362431FE5C75LLOs0G3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 22CoreAudioOrchestration31IsolatedUseCaseDevicesAvailableV10CodingKeys33_6F4531C893BD5814AC9E03CE6767CBEELLOSHAASQ
+ _associated conformance 22CoreAudioOrchestration31IsolatedUseCaseDevicesAvailableV10CodingKeys33_6F4531C893BD5814AC9E03CE6767CBEELLOs0I3KeyAAs23CustomStringConvertible
+ _associated conformance 22CoreAudioOrchestration31IsolatedUseCaseDevicesAvailableV10CodingKeys33_6F4531C893BD5814AC9E03CE6767CBEELLOs0I3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 22CoreAudioOrchestration41IsolatedUseCaseDevicesAvailabilityChangedV10CodingKeys33_7F44CEDF6732FB2CDE4A26681F34ABDELLOSHAASQ
+ _associated conformance 22CoreAudioOrchestration41IsolatedUseCaseDevicesAvailabilityChangedV10CodingKeys33_7F44CEDF6732FB2CDE4A26681F34ABDELLOs0J3KeyAAs23CustomStringConvertible
+ _associated conformance 22CoreAudioOrchestration41IsolatedUseCaseDevicesAvailabilityChangedV10CodingKeys33_7F44CEDF6732FB2CDE4A26681F34ABDELLOs0J3KeyAAs28CustomDebugStringConvertible
+ _exit
+ _flat unique So35CoreAudioOrchestrationEventCallback_p
+ _objc_msgSend$InstallLapseHandlerWithLapseHandler:clientData:
+ _os_log_create
+ _swift_getDynamicType
+ _swift_unknownObjectRetain_n
+ _symbolic SDySi______pG 22CoreAudioOrchestration12MessageFieldP
+ _symbolic Si_______pt 22CoreAudioOrchestration12MessageFieldP
+ _symbolic So32OrchestratorClientIOLapseHandlerC
+ _symbolic _____ 22CoreAudioOrchestration11BoolPayloadV
+ _symbolic _____ 22CoreAudioOrchestration11BoolPayloadV10CodingKeys33_6F4531C893BD5814AC9E03CE6767CBEELLO
+ _symbolic _____ 22CoreAudioOrchestration17SubscriptionErrorO
+ _symbolic _____ 22CoreAudioOrchestration25GetPropertyResponseHeaderV
+ _symbolic _____ 22CoreAudioOrchestration25GetPropertyResponseHeaderV10CodingKeys33_6F4531C893BD5814AC9E03CE6767CBEELLO
+ _symbolic _____ 22CoreAudioOrchestration27ActivateConfigurationHeaderV
+ _symbolic _____ 22CoreAudioOrchestration27ActivateConfigurationHeaderV10CodingKeys33_48A86D0391A9583A57CF362431FE5C75LLO
+ _symbolic _____ 22CoreAudioOrchestration29DeactivateConfigurationHeaderV
+ _symbolic _____ 22CoreAudioOrchestration29DeactivateConfigurationHeaderV10CodingKeys33_48A86D0391A9583A57CF362431FE5C75LLO
+ _symbolic _____ 22CoreAudioOrchestration31IsolatedUseCaseDevicesAvailableV
+ _symbolic _____ 22CoreAudioOrchestration31IsolatedUseCaseDevicesAvailableV10CodingKeys33_6F4531C893BD5814AC9E03CE6767CBEELLO
+ _symbolic _____ 22CoreAudioOrchestration41IsolatedUseCaseDevicesAvailabilityChangedV
+ _symbolic _____ 22CoreAudioOrchestration41IsolatedUseCaseDevicesAvailabilityChangedV10CodingKeys33_7F44CEDF6732FB2CDE4A26681F34ABDELLO
+ _symbolic ______pSg 22CoreAudioOrchestration12MessageFieldP
+ _symbolic ______pSg So35CoreAudioOrchestrationEventCallbackP
+ _symbolic _____m 22CoreAudioOrchestration11BoolPayloadV
+ _symbolic _____m 22CoreAudioOrchestration25GetPropertyResponseHeaderV
+ _symbolic _____m 22CoreAudioOrchestration27ActivateConfigurationHeaderV
+ _symbolic _____m 22CoreAudioOrchestration29DeactivateConfigurationHeaderV
+ _symbolic _____m 22CoreAudioOrchestration31IsolatedUseCaseDevicesAvailableV
+ _symbolic _____m 22CoreAudioOrchestration41IsolatedUseCaseDevicesAvailabilityChangedV
+ _symbolic _____ySi______pG s18_DictionaryStorageC 22CoreAudioOrchestration12MessageFieldP
+ _symbolic _____y_____G s22KeyedDecodingContainerV 22CoreAudioOrchestration11BoolPayloadV10CodingKeys33_6F4531C893BD5814AC9E03CE6767CBEELLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 22CoreAudioOrchestration25GetPropertyResponseHeaderV10CodingKeys33_6F4531C893BD5814AC9E03CE6767CBEELLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 22CoreAudioOrchestration27ActivateConfigurationHeaderV10CodingKeys33_48A86D0391A9583A57CF362431FE5C75LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 22CoreAudioOrchestration29DeactivateConfigurationHeaderV10CodingKeys33_48A86D0391A9583A57CF362431FE5C75LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 22CoreAudioOrchestration31IsolatedUseCaseDevicesAvailableV10CodingKeys33_6F4531C893BD5814AC9E03CE6767CBEELLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 22CoreAudioOrchestration41IsolatedUseCaseDevicesAvailabilityChangedV10CodingKeys33_7F44CEDF6732FB2CDE4A26681F34ABDELLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 22CoreAudioOrchestration11BoolPayloadV10CodingKeys33_6F4531C893BD5814AC9E03CE6767CBEELLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 22CoreAudioOrchestration25GetPropertyResponseHeaderV10CodingKeys33_6F4531C893BD5814AC9E03CE6767CBEELLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 22CoreAudioOrchestration27ActivateConfigurationHeaderV10CodingKeys33_48A86D0391A9583A57CF362431FE5C75LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 22CoreAudioOrchestration29DeactivateConfigurationHeaderV10CodingKeys33_48A86D0391A9583A57CF362431FE5C75LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 22CoreAudioOrchestration31IsolatedUseCaseDevicesAvailableV10CodingKeys33_6F4531C893BD5814AC9E03CE6767CBEELLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 22CoreAudioOrchestration41IsolatedUseCaseDevicesAvailabilityChangedV10CodingKeys33_7F44CEDF6732FB2CDE4A26681F34ABDELLO
- __DATA__TtC22CoreAudioOrchestrationP33_CB8C96822D899A15700183BFB413273740CoreAudioOrchestratorPingableMachService
- __METACLASS_DATA__TtC22CoreAudioOrchestrationP33_CB8C96822D899A15700183BFB413273740CoreAudioOrchestratorPingableMachService
- ___swift_memcpy32_8
- ___swift_memcpy48_8
- _associated conformance 22CoreAudioOrchestration12SubscriptionV10CodingKeys33_825BD687C5489A35C2C497C81D5259BCLLOSHAASQ
- _associated conformance 22CoreAudioOrchestration12SubscriptionV10CodingKeys33_825BD687C5489A35C2C497C81D5259BCLLOs0E3KeyAAs23CustomStringConvertible
- _associated conformance 22CoreAudioOrchestration12SubscriptionV10CodingKeys33_825BD687C5489A35C2C497C81D5259BCLLOs0E3KeyAAs28CustomDebugStringConvertible
- _associated conformance 22CoreAudioOrchestration34IsolatedUseCaseAvailabilityChangedV10CodingKeys33_7F44CEDF6732FB2CDE4A26681F34ABDELLOSHAASQ
- _associated conformance 22CoreAudioOrchestration34IsolatedUseCaseAvailabilityChangedV10CodingKeys33_7F44CEDF6732FB2CDE4A26681F34ABDELLOs0I3KeyAAs23CustomStringConvertible
- _associated conformance 22CoreAudioOrchestration34IsolatedUseCaseAvailabilityChangedV10CodingKeys33_7F44CEDF6732FB2CDE4A26681F34ABDELLOs0I3KeyAAs28CustomDebugStringConvertible
- _symbolic SDySi_____G 22CoreAudioOrchestration12SubscriptionV
- _symbolic _____ 22CoreAudioOrchestration0aB31OrchestratorPingableMachService33_CB8C96822D899A15700183BFB4132737LLC
- _symbolic _____ 22CoreAudioOrchestration12SubscriptionV
- _symbolic _____ 22CoreAudioOrchestration12SubscriptionV10CodingKeys33_825BD687C5489A35C2C497C81D5259BCLLO
- _symbolic _____ 22CoreAudioOrchestration34IsolatedUseCaseAvailabilityChangedV
- _symbolic _____ 22CoreAudioOrchestration34IsolatedUseCaseAvailabilityChangedV10CodingKeys33_7F44CEDF6732FB2CDE4A26681F34ABDELLO
- _symbolic _____m 22CoreAudioOrchestration12SubscriptionV
- _symbolic _____m 22CoreAudioOrchestration34IsolatedUseCaseAvailabilityChangedV
- _symbolic _____ySi_____G s18_DictionaryStorageC 22CoreAudioOrchestration12SubscriptionV
- _symbolic _____y_____G s22KeyedDecodingContainerV 22CoreAudioOrchestration12SubscriptionV10CodingKeys33_825BD687C5489A35C2C497C81D5259BCLLO
- _symbolic _____y_____G s22KeyedDecodingContainerV 22CoreAudioOrchestration34IsolatedUseCaseAvailabilityChangedV10CodingKeys33_7F44CEDF6732FB2CDE4A26681F34ABDELLO
- _symbolic _____y_____G s22KeyedEncodingContainerV 22CoreAudioOrchestration12SubscriptionV10CodingKeys33_825BD687C5489A35C2C497C81D5259BCLLO
- _symbolic _____y_____G s22KeyedEncodingContainerV 22CoreAudioOrchestration34IsolatedUseCaseAvailabilityChangedV10CodingKeys33_7F44CEDF6732FB2CDE4A26681F34ABDELLO
CStrings:
+ "%25s:%-5d Calling Lapse Handler"
+ "%25s:%-5d Creating Lapse Handler Event: %s - status: %u"
+ "%25s:%-5d Handle Lapse - %u and has Started: %d"
+ "%25s:%-5d Recevied Abnormally Stopped notification: %u"
+ "%25s:%-5d Recevied Device is Alive notification: %u"
+ "%25s:%-5d Recevied isRunning notification: %u"
+ "%25s:%-5d Set IO Has Started: %d -> %d"
+ "@\"NSDictionary\"24@0:8@\"<CoreAudioOrchestrationEventCallback>\"16"
+ "Client cancelled connection. %s"
+ "Connnection to Registrar died! %s - Exiting."
+ "CoreAudioOrchestrationEventCallback"
+ "CoreAudioOrchestration_UseSharedDSPUseCaseID"
+ "Could not create Lapse Event Listeners for provided deviceID!"
+ "Could not destory Lapse Event Listeners for provided deviceID!"
+ "Create Received: %d"
+ "Creating Lapse Handler"
+ "Destroy Received: %d"
+ "Destroying Lapse Handler"
+ "Failed to activate the configuration with the given token"
+ "Failed to deactivate the configuration with the given token"
+ "Failed to parse message to Activate Configuration"
+ "Failed to parse message to Deactivate Configuration"
+ "Failed to subscribe to event type: "
+ "HALEventListener.cpp"
+ "IOLapseHandler.cpp"
+ "Implementation stubbed"
+ "InstallLapseHandlerWithLapseHandler:clientData:"
+ "Installed client lapse handler with: %d"
+ "Installing Lapse Handler"
+ "Launch Received: %d"
+ "OrchestratorClientIOLapseHandler"
+ "Setting kAudioHardwarePropertyClientPrefersSuppressingRecordingIndicator failed"
+ "activateConfiguration:"
+ "createHALLapseEventListeners:"
+ "deactivateConfiguration:"
+ "defaultInputDevice - ok"
+ "destroyHALLapseEventListeners"
+ "eventCallback"
+ "handleIncomingConfigurationEvent:"
+ "installClientLapseHandler:data:"
+ "ioHasStartedOnDevice:"
+ "mLapseHandler"
+ "orchestratorLapseHandler"
+ "registerEventCallback:"
+ "subscribeToEvent:"
+ "unsubscribeFromEvent:"
+ "v20@0:8B16"
+ "{unique_ptr<IOLapseHandler, std::default_delete<IOLapseHandler>>=\"__ptr_\"{__compressed_pair<IOLapseHandler *, std::default_delete<IOLapseHandler>>=\"__value_\"^{IOLapseHandler}}}"
- "ADM feature flag is disabled"
- "CoreAudioOrchestration_ADMEnabled"
- "Create Received: "
- "Destroy Received: "
- "Launch Received: "
- "Received CreateOrchestratorClientPortal"
- "Received CreatePingableMachService request for %s"
- "_TtC22CoreAudioOrchestrationP33_CB8C96822D899A15700183BFB413273740CoreAudioOrchestratorPingableMachService"
- "eventDescriptionType"

```
