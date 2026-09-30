## AudioServerDriverTransports_Base

> `/System/Library/PrivateFrameworks/AudioServerDriverTransports_Base.framework/Versions/A/AudioServerDriverTransports_Base`

```diff

-230.2.0.0.0
-  __TEXT.__text: 0x44560
-  __TEXT.__auth_stubs: 0xe20
-  __TEXT.__objc_methlist: 0x2c98
-  __TEXT.__gcc_except_tab: 0x59f8
-  __TEXT.__const: 0x3e6
-  __TEXT.__cstring: 0x17ee
-  __TEXT.__oslogstring: 0x2df2
-  __TEXT.__unwind_info: 0x1f48
-  __TEXT.__objc_classname: 0x601
-  __TEXT.__objc_methname: 0x6829
-  __TEXT.__objc_methtype: 0x1143
-  __TEXT.__objc_stubs: 0x60c0
-  __DATA_CONST.__got: 0x2c8
-  __DATA_CONST.__const: 0x4f8
-  __DATA_CONST.__objc_classlist: 0x188
+240.42.0.0.0
+  __TEXT.__text: 0x49568
+  __TEXT.__auth_stubs: 0xe60
+  __TEXT.__objc_methlist: 0x338c
+  __TEXT.__gcc_except_tab: 0x6358
+  __TEXT.__const: 0x55e
+  __TEXT.__cstring: 0x17a3
+  __TEXT.__oslogstring: 0x302e
+  __TEXT.__unwind_info: 0x2228
+  __TEXT.__objc_classname: 0x6dd
+  __TEXT.__objc_methname: 0x6b90
+  __TEXT.__objc_methtype: 0x11be
+  __TEXT.__objc_stubs: 0x6400
+  __DATA_CONST.__got: 0x2d8
+  __DATA_CONST.__const: 0x520
+  __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x90
+  __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b00
-  __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_superrefs: 0x150
-  __AUTH_CONST.__auth_got: 0x728
-  __AUTH_CONST.__const: 0x590
-  __AUTH_CONST.__cfstring: 0x1860
-  __AUTH_CONST.__objc_const: 0x5460
-  __AUTH_CONST.__objc_intobj: 0x120
-  __AUTH.__objc_data: 0xf50
-  __DATA.__objc_ivar: 0x2e4
-  __DATA.__data: 0x738
-  __DATA.__bss: 0x78
+  __DATA_CONST.__objc_selrefs: 0x1cb0
+  __DATA_CONST.__objc_protorefs: 0x50
+  __DATA_CONST.__objc_superrefs: 0x160
+  __DATA_CONST.__objc_arraydata: 0x60
+  __AUTH_CONST.__auth_got: 0x748
+  __AUTH_CONST.__const: 0x770
+  __AUTH_CONST.__cfstring: 0x1880
+  __AUTH_CONST.__objc_const: 0x5268
+  __AUTH_CONST.__objc_intobj: 0x288
+  __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH.__objc_data: 0x1090
+  __DATA.__objc_ivar: 0x2f8
+  __DATA.__data: 0x8b8
+  __DATA.__bss: 0x98
+  - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C4D710C3-5059-3D6D-988D-528901EA4B7D
-  Functions: 1722
-  Symbols:   4178
-  CStrings:  2264
+  UUID: 5914A29F-23A7-3631-A10F-5BDFA1CE8C86
+  Functions: 1836
+  Symbols:   4457
+  CStrings:  2343
 
Symbols:
+ +[ASDTExclavesSensorManager forSensorName:].cold.1
+ +[ASDTGlobalQueues concurrent]
+ +[ASDTGlobalQueues concurrent].cold.1
+ +[ASDTGlobalQueues systemNotification]
+ +[ASDTGlobalQueues systemNotification].cold.1
+ +[ASDTIOServiceManager forIOServiceWithClassName:withIDProperty:managerClass:].cold.1
+ +[ASDTNonSecurePathEnableProperty createForInput]
+ +[ASDTNonSecurePathEnableProperty setNonSecureInputEnabled:onDevice:]
+ +[ASDTSystemPowerNotifier notifierForBundleName:delegate:queue:earlyWake:]
+ +[ASDTSystemStatus systemStatus].cold.1
+ -[ASDTAudioDevice .cxx_construct]
+ -[ASDTAudioDevice addControl:]
+ -[ASDTAudioDevice addCustomProperty:]
+ -[ASDTAudioDevice addInputStream:]
+ -[ASDTAudioDevice addOutputStream:]
+ -[ASDTAudioDevice completeInitialization]
+ -[ASDTAudioDevice initWithConfig:withDeviceManager:andPlugin:].cold.2
+ -[ASDTAudioDevice objectsConformingAddObjects:]
+ -[ASDTAudioDevice objectsConformingRemoveObjects:]
+ -[ASDTAudioDevice objectsConformingToProtocol:]
+ -[ASDTAudioDevice performPowerStateInactive:]
+ -[ASDTAudioDevice performStartIO].cold.1
+ -[ASDTAudioDevice performStartIO].cold.2
+ -[ASDTAudioDevice protocolMap]
+ -[ASDTAudioDevice removeControl:]
+ -[ASDTAudioDevice removeCustomProperty:]
+ -[ASDTAudioDevice removeInputStream:]
+ -[ASDTAudioDevice removeOutputStream:]
+ -[ASDTAudioDevice setProtocolMap:]
+ -[ASDTAudioDevice setupSamplingRates:]
+ -[ASDTAudioDevice subclassInitWithConfig:]
+ -[ASDTAudioDevice userActiveChanged:]
+ -[ASDTAudioDevice userIsActive]
+ -[ASDTChangeRequestManager configurationChangeRunningForObject:]
+ -[ASDTCustomProperty addedToDevice:]
+ -[ASDTCustomProperty checkAndSetPropertyValue:].cold.2
+ -[ASDTCustomProperty getPropertyWithQualifierSize:qualifierData:dataSize:andData:forClient:].cold.4
+ -[ASDTCustomProperty propertyChangeBlock]
+ -[ASDTCustomProperty setPropertyChangeBlock:]
+ -[ASDTDeviceManager setUserIsActive:]
+ -[ASDTDeviceManager stopThread]
+ -[ASDTDeviceManager userIsActive]
+ -[ASDTExclavesSensorManager ioThreadStartStop:withStatusTracker:]
+ -[ASDTExclavesStatusProperty addedToDevice:]
+ -[ASDTExclavesStatusProperty addedToDevice:].cold.1
+ -[ASDTExclavesStatusProperty setStatusTrackerHost:]
+ -[ASDTExclavesStatusProperty statusTrackerHost]
+ -[ASDTExclavesStream exclavesStatusTracker]
+ -[ASDTExclavesStream ramper]
+ -[ASDTIOServiceManager addDelegate:forIDValues:].cold.5
+ -[ASDTIOServiceManager initForIOServiceWithClassName:andIDProperty:].cold.4
+ -[ASDTNonSecurePathEnableProperty enabled]
+ -[ASDTNonSecurePathEnableProperty initWithConfig:]
+ -[ASDTNonSecurePathEnableProperty setEnabled:]
+ -[ASDTPMDevice performPowerStateInactive:]
+ -[ASDTPMDeviceProxy performPowerStateInactive:]
+ -[ASDTPMSequencer doUpdateQuiescentState:]
+ -[ASDTPMSequencer executeSequenceToState:fromState:]
+ -[ASDTPMSequencer powerState]
+ -[ASDTPMSequencer quiescentState]
+ -[ASDTPMSequencer setQuiescentState:]
+ -[ASDTPMSequencer updateQuiescentState:]
+ -[ASDTPlugin .cxx_construct]
+ -[ASDTPlugin configurationChangeRunningForObject:]
+ -[ASDTPlugin dealloc]
+ -[ASDTStream ioBufferFramesSizeMax]
+ -[ASDTStream ioBufferFramesUnexpectedSizeCount]
+ -[ASDTStream ioBufferPtr]
+ -[ASDTStream ioBufferRef]
+ -[ASDTStream pmInactiveStream:]
+ -[ASDTStream setIoBufferPtr:]
+ -[ASDTStream setupPhysicalFormats:]
+ -[ASDTSystemPowerNotifier initForBundleName:delegate:queue:earlyWake:]
+ -[ASDTSystemPowerNotifier initForBundleName:delegate:queue:earlyWake:].cold.1
+ -[ASDTUInt32Property checkPropertyValue:]
+ -[ASDTUInt32Property initWithConfig:]
+ -[ASDTUInt32Property setUint32Value:]
+ -[ASDTUInt32Property uint32Value]
+ -[MockASDTSelectorControl setTestingEnabled:]
+ -[MockASDTSelectorControl testingEnable:]
+ -[MockASDTSelectorControl testingEnabled]
+ -[NSDictionary(ASDTConfig) asdtAddNonSecurePathEnable]
+ ASDTBaseLogType.cold.1
+ GCC_except_table100
+ GCC_except_table113
+ GCC_except_table134
+ GCC_except_table135
+ GCC_except_table137
+ GCC_except_table138
+ GCC_except_table139
+ GCC_except_table142
+ GCC_except_table146
+ GCC_except_table147
+ GCC_except_table155
+ GCC_except_table157
+ GCC_except_table171
+ GCC_except_table174
+ GCC_except_table177
+ GCC_except_table180
+ GCC_except_table183
+ GCC_except_table187
+ GCC_except_table190
+ GCC_except_table192
+ GCC_except_table194
+ GCC_except_table200
+ GCC_except_table202
+ GCC_except_table214
+ GCC_except_table216
+ GCC_except_table217
+ GCC_except_table224
+ GCC_except_table227
+ GCC_except_table229
+ GCC_except_table233
+ GCC_except_table69
+ GCC_except_table74
+ OBJC_IVAR_$_ASDTAudioDevice._protocolMap
+ OBJC_IVAR_$_ASDTAudioDevice._protocolMutex
+ OBJC_IVAR_$_ASDTCustomProperty._propertyChangeBlock
+ OBJC_IVAR_$_ASDTDeviceManager._userIsActive
+ OBJC_IVAR_$_ASDTExclavesStatusProperty._statusTrackerHost
+ OBJC_IVAR_$_ASDTExclavesStream._ramper
+ OBJC_IVAR_$_ASDTPMSequencer._quiescentState
+ OBJC_IVAR_$_ASDTStream._ioBufferFramesSizeMax
+ OBJC_IVAR_$_ASDTStream._ioBufferFramesUnexpectedSizeCount
+ OBJC_IVAR_$_ASDTStream._ioBufferPtr
+ OBJC_IVAR_$_MockASDTSelectorControl._testingEnabled
+ _NSProtocolFromString
+ _NSStringFromProtocol
+ _OBJC_CLASS_$_ASDTGlobalQueues
+ _OBJC_CLASS_$_ASDTNonSecurePathEnableProperty
+ _OBJC_CLASS_$_ASDTUInt32Property
+ _OBJC_CLASS_$_MockASDTSelectorControl
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_METACLASS_$_ASDTGlobalQueues
+ _OBJC_METACLASS_$_ASDTNonSecurePathEnableProperty
+ _OBJC_METACLASS_$_ASDTUInt32Property
+ _OBJC_METACLASS_$_MockASDTSelectorControl
+ _ZN12_GLOBAL__N_110NsecToHostExRxRt.cold.1
+ _ZN12_GLOBAL__N_117NsecFromLargeHostEn.cold.1
+ _ZN4ASDT11IOMemoryMap7ReleaseEv.cold.1
+ _ZN4ASDT6RamperC2ERK27AudioStreamBasicDescriptionj.cold.1
+ _ZN4ASDT6RamperC2ERK27AudioStreamBasicDescriptionj.cold.2
+ _ZN4ASDT6RamperC2ERK27AudioStreamBasicDescriptionj.cold.3
+ _ZN4ASDT6RamperC2ERK27AudioStreamBasicDescriptionj.cold.4
+ _ZN4ASDT9IOConnect6Object6RetainEv.cold.1
+ _ZN4ASDT9IOConnect6Object7ReleaseEv.cold.1
+ __41-[ASDTPlugin requestConfigurationChange:]_block_invoke.26
+ __OBJC_$_CLASS_METHODS_ASDTGlobalQueues
+ __OBJC_$_CLASS_METHODS_ASDTNonSecurePathEnableProperty
+ __OBJC_$_INSTANCE_METHODS_ASDTNonSecurePathEnableProperty
+ __OBJC_$_INSTANCE_METHODS_ASDTUInt32Property
+ __OBJC_$_INSTANCE_METHODS_MockASDTSelectorControl
+ __OBJC_$_INSTANCE_VARIABLES_MockASDTSelectorControl
+ __OBJC_$_PROP_LIST_ASDTExclavesStatusTrackerHostProtocol
+ __OBJC_$_PROP_LIST_ASDTNonSecurePathEnableProperty
+ __OBJC_$_PROP_LIST_ASDTTestingProtocol
+ __OBJC_$_PROP_LIST_ASDTUInt32Property
+ __OBJC_$_PROP_LIST_ASDTUserActivityManagerProtocol
+ __OBJC_$_PROP_LIST_MockASDTSelectorControl
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ASDTExclavesStatusTrackerHostProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ASDTTestingProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ASDTUserActivityClientProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ASDTUserActivityManagerProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ASDTExclavesStatusTrackerHostProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ASDTTestingProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ASDTUserActivityClientProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ASDTUserActivityManagerProtocol
+ __OBJC_$_PROTOCOL_REFS_ASDTExclavesStatusTrackerHostProtocol
+ __OBJC_$_PROTOCOL_REFS_ASDTTestingProtocol
+ __OBJC_$_PROTOCOL_REFS_ASDTUserActivityClientProtocol
+ __OBJC_$_PROTOCOL_REFS_ASDTUserActivityManagerProtocol
+ __OBJC_CLASS_PROTOCOLS_$_ASDTUInt32Property
+ __OBJC_CLASS_PROTOCOLS_$_ASDTUserActivityNotifier
+ __OBJC_CLASS_PROTOCOLS_$_MockASDTSelectorControl
+ __OBJC_CLASS_RO_$_ASDTGlobalQueues
+ __OBJC_CLASS_RO_$_ASDTNonSecurePathEnableProperty
+ __OBJC_CLASS_RO_$_ASDTUInt32Property
+ __OBJC_CLASS_RO_$_MockASDTSelectorControl
+ __OBJC_LABEL_PROTOCOL_$_ASDTExclavesStatusTrackerHostProtocol
+ __OBJC_LABEL_PROTOCOL_$_ASDTTestingProtocol
+ __OBJC_LABEL_PROTOCOL_$_ASDTUserActivityClientProtocol
+ __OBJC_LABEL_PROTOCOL_$_ASDTUserActivityManagerProtocol
+ __OBJC_METACLASS_RO_$_ASDTGlobalQueues
+ __OBJC_METACLASS_RO_$_ASDTNonSecurePathEnableProperty
+ __OBJC_METACLASS_RO_$_ASDTUInt32Property
+ __OBJC_METACLASS_RO_$_MockASDTSelectorControl
+ __OBJC_PROTOCOL_$_ASDTExclavesStatusTrackerHostProtocol
+ __OBJC_PROTOCOL_$_ASDTTestingProtocol
+ __OBJC_PROTOCOL_$_ASDTUserActivityClientProtocol
+ __OBJC_PROTOCOL_$_ASDTUserActivityManagerProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_ASDTExclavesStatusTrackerHostProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_ASDTUserActivityClientProtocol
+ __ZN10applesauce2CF10BooleanRef8from_getEPK11__CFBoolean
+ __ZN10applesauce2CF13DictionaryRef8from_getEPK14__CFDictionary
+ __ZN10applesauce2CF7DataRef8from_getEPK8__CFData
+ __ZN10applesauce2CF7details20make_CFDictionaryRefINS0_9StringRefENS0_7TypeRefEEEDaRKNSt3__13mapIT_T0_NS6_4lessIS8_EENS6_9allocatorINS6_4pairIKS8_S9_EEEEEE
+ __ZN10applesauce2CF8ArrayRef8from_getEPK9__CFArray
+ __ZN10applesauce2CF9NumberRef8from_getEPK10__CFNumber
+ __ZN10applesauce2CF9ObjectRefIPK10__CFNumberED1Ev
+ __ZN10applesauce2CF9ObjectRefIPK10__CFStringED1Ev
+ __ZN10applesauce2CF9ObjectRefIPK11__CFBooleanED1Ev
+ __ZN10applesauce2CF9ObjectRefIPK14__CFDictionaryED1Ev
+ __ZN10applesauce2CF9ObjectRefIPK8__CFDataED1Ev
+ __ZN10applesauce2CF9ObjectRefIPK9__CFArrayED1Ev
+ __ZN10applesauce2CF9StringRef8from_getEPK10__CFString
+ __ZN12_GLOBAL__N_117NsecFromLargeHostEn
+ __ZN4ASDT11IOMemoryMap7ReleaseEv
+ __ZN4ASDT11IOMemoryMapC1EOS0_
+ __ZN4ASDT11IOMemoryMapC1ERNS_9IOConnectEjj
+ __ZN4ASDT11IOMemoryMapC2EOS0_
+ __ZN4ASDT11IOMemoryMapC2ERNS_9IOConnectEjj
+ __ZN4ASDT11IOMemoryMapD0Ev
+ __ZN4ASDT11IOMemoryMapD1Ev
+ __ZN4ASDT11IOMemoryMapD2Ev
+ __ZN4ASDT11IOMemoryMapaSEOS0_
+ __ZN4ASDT12IOUserClient11SetPropertyERKN10applesauce2CF9StringRefERKNS2_13DictionaryRefEb
+ __ZN4ASDT12IOUserClient11SetPropertyERKN10applesauce2CF9StringRefERKNS2_7DataRefEb
+ __ZN4ASDT12IOUserClient11SetPropertyERKN10applesauce2CF9StringRefERKNS2_7TypeRefEb
+ __ZN4ASDT12IOUserClient11SetPropertyERKN10applesauce2CF9StringRefERKNS2_8ArrayRefEb
+ __ZN4ASDT12IOUserClient11SetPropertyERKN10applesauce2CF9StringRefES5_b
+ __ZN4ASDT12IOUserClient11SetPropertyERKN10applesauce2CF9StringRefEbb
+ __ZN4ASDT12IOUserClient11SetPropertyERKN10applesauce2CF9StringRefEdb
+ __ZN4ASDT12IOUserClient11SetPropertyERKN10applesauce2CF9StringRefEfb
+ __ZN4ASDT12IOUserClient11SetPropertyERKN10applesauce2CF9StringRefEib
+ __ZN4ASDT12IOUserClient11SetPropertyERKN10applesauce2CF9StringRefEjb
+ __ZN4ASDT12IOUserClient11SetPropertyERKN10applesauce2CF9StringRefExb
+ __ZN4ASDT12IOUserClient11SetPropertyERKN10applesauce2CF9StringRefEyb
+ __ZN4ASDT12IOUserClient14OpenConnectionEv
+ __ZN4ASDT12IOUserClient17EnableConnectionsEb
+ __ZN4ASDT12IOUserClient9MapMemoryEjj
+ __ZN4ASDT12IOUserClientC1Ejj
+ __ZN4ASDT12IOUserClientC1Ev
+ __ZN4ASDT12IOUserClientC2Ejj
+ __ZN4ASDT12IOUserClientC2Ev
+ __ZN4ASDT6Ramper14CreateRampDataEv
+ __ZN4ASDT6Ramper19MuteForSensorStatusENS_8Exclaves6Sensor6StatusEb
+ __ZN4ASDT6Ramper6CreateERK27AudioStreamBasicDescriptionj
+ __ZN4ASDT6Ramper7ProcessEjPKvPvNS_8Exclaves6Sensor6StatusE
+ __ZN4ASDT6Ramper8SetMutedEbb
+ __ZN4ASDT6RamperC1ERK27AudioStreamBasicDescriptionj
+ __ZN4ASDT6RamperC2ERK27AudioStreamBasicDescriptionj
+ __ZN4ASDT6RamperD0Ev
+ __ZN4ASDT6RamperD1Ev
+ __ZN4ASDT6RamperD2Ev
+ __ZN4ASDT9IOConnect3GetEv
+ __ZN4ASDT9IOConnect4OpenEv
+ __ZN4ASDT9IOConnect5CloseEv
+ __ZN4ASDT9IOConnect6EnableEb
+ __ZN4ASDT9IOConnect6IsOpenEv
+ __ZN4ASDT9IOConnect6Object5CloseEv
+ __ZN4ASDT9IOConnect6Object6EnableEb
+ __ZN4ASDT9IOConnect6Object6RetainEv
+ __ZN4ASDT9IOConnect6Object7ReleaseEv
+ __ZN4ASDT9IOConnect6Object9TerminateEv
+ __ZN4ASDT9IOConnect6ObjectC1Ejj
+ __ZN4ASDT9IOConnect6ObjectC2Ejj
+ __ZN4ASDT9IOConnect6ObjectD0Ev
+ __ZN4ASDT9IOConnect6ObjectD1Ev
+ __ZN4ASDT9IOConnect6ObjectD2Ev
+ __ZN4ASDT9IOConnect7DoCloseEv
+ __ZN4ASDT9IOConnect7IsValidEv
+ __ZN4ASDT9IOConnect9TerminateEv
+ __ZN4ASDT9IOConnectC1EOS0_
+ __ZN4ASDT9IOConnectC1ERS0_b
+ __ZN4ASDT9IOConnectC1Ejj
+ __ZN4ASDT9IOConnectC1Ev
+ __ZN4ASDT9IOConnectC2EOS0_
+ __ZN4ASDT9IOConnectC2ERS0_b
+ __ZN4ASDT9IOConnectC2Ejj
+ __ZN4ASDT9IOConnectC2Ev
+ __ZN4ASDT9IOConnectD0Ev
+ __ZN4ASDT9IOConnectD1Ev
+ __ZN4ASDT9IOConnectD2Ev
+ __ZN4ASDT9IOConnectaSEOS0_
+ __ZN4ASDT9IOConnectaSERS0_
+ __ZN8ASDTTime8addTicksERKS_
+ __ZN8ASDTTime8divTicksEy
+ __ZN8ASDTTime8mulTicksEy
+ __ZN8ASDTTime8subTicksERKS_
+ __ZNK4ASDT12IOUserClient10CallMethodEjPKyjPKvmPyPjPvPmb
+ __ZNK4ASDT9IOConnect6Object3GetEv
+ __ZNK4ASDT9IOConnect6Object7IsValidEv
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__119__shared_weak_count13__get_deleterERKSt9type_info
+ __ZNKSt3__16vectorI17CAAudioValueRangeNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN10applesauce2CF11TypeRefPairENS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN10applesauce2CF7TypeRefENS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN4ASDT8Exclaves13StatusTracker6UpdateENS_9allocatorIS4_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIPKvNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt12out_of_rangeC1B8ne190102EPKc
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeIN10applesauce2CF9StringRefENS4_7TypeRefEEEPvEENS_22__tree_node_destructorINS_9allocatorIS9_EEEEE5resetB8ne190102EPS9_
+ __ZNSt3__111shared_lockINS_12shared_mutexEED2B8ne190102Ev
+ __ZNSt3__111unique_lockINS_12shared_mutexEED2B8ne190102Ev
+ __ZNSt3__112__destroy_atB8ne190102IN10applesauce2CF11TypeRefPairELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne190102IN10applesauce2CF7TypeRefELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne190102INS_4pairIKN10applesauce2CF9StringRefENS3_7TypeRefEEELi0EEEvPT_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102Emc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ILi0EEEPKc
+ __ZNSt3__112construct_atB8ne190102IN10applesauce2CF7TypeRefEJRKS3_EPS3_EEPT_S8_DpOT0_
+ __ZNSt3__112shared_mutexD1B8ne190102Ev
+ __ZNSt3__113__tree_removeB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI17CAAudioValueRangeEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN10applesauce2CF11TypeRefPairEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN10applesauce2CF7TypeRefEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN4ASDT8Exclaves13StatusTracker6UpdateEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPKvEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__shared_weak_count14__release_weakEv
+ __ZNSt3__119__shared_weak_count16__release_sharedB8ne190102Ev
+ __ZNSt3__119__shared_weak_countD2Ev
+ __ZNSt3__120__shared_ptr_emplaceIN4ASDT9IOConnect6ObjectENS_9allocatorIS3_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_emplaceIN4ASDT9IOConnect6ObjectENS_9allocatorIS3_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_emplaceIN4ASDT9IOConnect6ObjectENS_9allocatorIS3_EEED0Ev
+ __ZNSt3__120__shared_ptr_emplaceIN4ASDT9IOConnect6ObjectENS_9allocatorIS3_EEED1Ev
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZNSt3__124__optional_destruct_baseIN10applesauce2CF7TypeRefELb0EED2B8ne190102Ev
+ __ZNSt3__127__tree_balance_after_insertB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__134__uninitialized_allocator_relocateB8ne190102INS_9allocatorIN10applesauce2CF11TypeRefPairEEES4_EEvRT_PT0_S9_S9_
+ __ZNSt3__135__uninitialized_allocator_copy_implB8ne190102INS_9allocatorIN10applesauce2CF7TypeRefEEENS3_17ArrayRef_iteratorIS4_EES7_PS4_EET2_RT_T0_T1_S9_
+ __ZNSt3__13mapIN10applesauce2CF9StringRefENS2_7TypeRefENS_4lessIS3_EENS_9allocatorINS_4pairIKS3_S4_EEEEE16insert_or_assignB8ne190102IRS4_EENS8_INS_14__map_iteratorINS_15__tree_iteratorINS_12__value_typeIS3_S4_EEPNS_11__tree_nodeISI_PvEElEEEEbEERS9_OT_
+ __ZNSt3__13mapIN10applesauce2CF9StringRefENS2_7TypeRefENS_4lessIS3_EENS_9allocatorINS_4pairIKS3_S4_EEEEE6insertB8ne190102INS2_22DictionaryRef_iteratorIS4_S4_EEEEvT_SG_
+ __ZNSt3__13mapIN10applesauce2CF9StringRefENS2_7TypeRefENS_4lessIS3_EENS_9allocatorINS_4pairIKS3_S4_EEEEEC2B8ne190102INS2_22DictionaryRef_iteratorIS4_S4_EEEET_SG_RKS6_
+ __ZNSt3__14pairIKN10applesauce2CF9StringRefENS2_7TypeRefEEC2B8ne190102ILb1ELi0EEERS4_RKS5_
+ __ZNSt3__14pairIKN10applesauce2CF9StringRefENS2_7TypeRefEEC2B8ne190102IRS4_RS5_Li0EEEOT_OT0_
+ __ZNSt3__14pairIKN10applesauce2CF9StringRefENS2_7TypeRefEEC2B8ne190102IS5_S5_Li0EEEONS0_IT_T0_EE
+ __ZNSt3__16vectorIN10applesauce2CF11TypeRefPairENS_9allocatorIS3_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorIN10applesauce2CF11TypeRefPairENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRKNS2_9StringRefERKNS2_7TypeRefEEEEPS3_DpOT_
+ __ZNSt3__16vectorIN10applesauce2CF7TypeRefENS_9allocatorIS3_EEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorIN10applesauce2CF7TypeRefENS_9allocatorIS3_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorIN10applesauce2CF7TypeRefENS_9allocatorIS3_EEE16__init_with_sizeB8ne190102INS2_17ArrayRef_iteratorIS3_EES9_EEvT_T0_m
+ __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE16__init_with_sizeB8ne190102IPS2_S7_EEvT_T0_m
+ __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEEC2B8ne190102Em
+ __ZNSt3__19__advanceB8ne190102INS_20__map_const_iteratorINS_21__tree_const_iteratorINS_12__value_typeIN4ASDT8RawPointENS4_7DBPointEEEPNS_11__tree_nodeIS7_PvEElEEEEEEvRT_NS_15iterator_traitsISE_E15difference_typeENS_26bidirectional_iterator_tagE
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
+ __ZTIN4ASDT11IOMemoryMapE
+ __ZTIN4ASDT6RamperE
+ __ZTIN4ASDT9IOConnect6ObjectE
+ __ZTIN4ASDT9IOConnectE
+ __ZTINSt3__119__shared_weak_countE
+ __ZTINSt3__120__shared_ptr_emplaceIN4ASDT9IOConnect6ObjectENS_9allocatorIS3_EEEE
+ __ZTSN4ASDT11IOMemoryMapE
+ __ZTSN4ASDT6RamperE
+ __ZTSN4ASDT9IOConnect6ObjectE
+ __ZTSN4ASDT9IOConnectE
+ __ZTSNSt3__120__shared_ptr_emplaceIN4ASDT9IOConnect6ObjectENS_9allocatorIS3_EEEE
+ __ZTVN4ASDT11IOMemoryMapE
+ __ZTVN4ASDT6RamperE
+ __ZTVN4ASDT9IOConnect6ObjectE
+ __ZTVN4ASDT9IOConnectE
+ __ZTVNSt3__120__shared_ptr_emplaceIN4ASDT9IOConnect6ObjectENS_9allocatorIS3_EEEE
+ __ZdaPvSt19__type_descriptor_t
+ __ZnamSt19__type_descriptor_t
+ ___29-[ASDTPMSequencer powerState]_block_invoke
+ ___30+[ASDTGlobalQueues concurrent]_block_invoke
+ ___38+[ASDTGlobalQueues systemNotification]_block_invoke
+ ___40-[ASDTPMSequencer updateQuiescentState:]_block_invoke
+ ___44-[ASDTExclavesStatusProperty addedToDevice:]_block_invoke
+ ___52-[ASDTPMSequencer executeSequenceToState:fromState:]_block_invoke
+ ___block_descriptor_44_ea8_32s_e5_v8?0l
+ ___block_descriptor_48_ea8_32s40r_e5_v8?0l
+ ___block_descriptor_56_ea8_32s40r_e5_v8?0l
+ ___block_descriptor_72_e195_i40?0I8r^{AudioServerPlugInIOCycleInfo=QI{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}(?=dd)d}12^v20^v28I36l
+ ___block_descriptor_92_e195_i40?0I8r^{AudioServerPlugInIOCycleInfo=QI{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}(?=dd)d}12^v20^v28I36l
+ __block_literal_global.3
+ __block_literal_global.9
+ _asdtPowerStateFromTransition
+ _asdtPowerTransitionFromUInt32
+ _asdtPowerTransitionList
+ _cosf
+ _kASDTConfigKeyAddNonSecurePathEnableProperty
+ _kASDTNonSecurePathEnableInputAddress
+ _objc_msgSend$_updateSafetyOffsets:
+ _objc_msgSend$_updateTimestampPeriod:
+ _objc_msgSend$addedToDevice:
+ _objc_msgSend$asdtAddMissingEntriesFromDictionary:
+ _objc_msgSend$cancel
+ _objc_msgSend$completeInitialization
+ _objc_msgSend$concurrent
+ _objc_msgSend$configurationChangeRunningForObject:
+ _objc_msgSend$doUpdateQuiescentState:
+ _objc_msgSend$exclavesStatusTracker
+ _objc_msgSend$executeSequenceToState:fromState:
+ _objc_msgSend$includeValueInDescription
+ _objc_msgSend$initForBundleName:delegate:queue:earlyWake:
+ _objc_msgSend$ioBufferFramesSizeMax
+ _objc_msgSend$ioBufferFramesUnexpectedSizeCount
+ _objc_msgSend$ioBufferRef
+ _objc_msgSend$ioThreadStartStop:withStatusTracker:
+ _objc_msgSend$isFinished
+ _objc_msgSend$notifierForBundleName:delegate:queue:earlyWake:
+ _objc_msgSend$objectsConformingAddObjects:
+ _objc_msgSend$objectsConformingRemoveObjects:
+ _objc_msgSend$objectsConformingToProtocol:
+ _objc_msgSend$performPowerStateInactive:
+ _objc_msgSend$pmInactiveStream:
+ _objc_msgSend$propertyChangeBlock
+ _objc_msgSend$protocolMap
+ _objc_msgSend$quiescentState
+ _objc_msgSend$setIoBufferPtr:
+ _objc_msgSend$setProtocolMap:
+ _objc_msgSend$setQuiescentState:
+ _objc_msgSend$setStatusTrackerHost:
+ _objc_msgSend$setTestingEnabled:
+ _objc_msgSend$setUint32Value:
+ _objc_msgSend$setupPhysicalFormats:
+ _objc_msgSend$setupSamplingRates:
+ _objc_msgSend$statusTrackerHost
+ _objc_msgSend$stopThread
+ _objc_msgSend$subclassInitWithConfig:
+ _objc_msgSend$systemNotification
+ _objc_msgSend$timestampPeriod
+ _objc_msgSend$uint32Value
+ _objc_msgSend$updateQuiescentState:
+ _objc_msgSend$userIsActive
+ _vDSP_vmul
+ asdt_exclaves_available.cold.1
+ concurrent.onceToken
+ concurrent.sConcurrentQueue
+ systemNotification.onceToken
+ systemNotification.sNotificationQueue
- -[ASDTAudioDevice addStatusProtocolObject:toArray:]
- -[ASDTAudioDevice setStatusProtocolObjects:]
- -[ASDTAudioDevice setupStatusProtocol]
- -[ASDTAudioDevice statusProtocolObjects]
- -[ASDTCustomProperty checkPropertyValue:].cold.1
- -[ASDTDeviceManager initializingQueue]
- -[ASDTDeviceManager setInitializingQueue:]
- -[ASDTExclavesSensorManager initWithSensorName:].cold.2
- -[ASDTExclavesSensorManager ioThreadStartStop:]
- -[ASDTExclavesSensorManager statusTracker]
- -[ASDTExclavesStatusProperty initWithConfig:].cold.2
- -[ASDTExclavesStatusProperty sensorManager]
- -[ASDTExclavesStatusProperty setSensorManager:]
- -[ASDTNullStream ioBuffer]
- -[ASDTPMSequencer pmConcurrentQueue]
- -[ASDTPMSequencer setPmConcurrentQueue:]
- -[ASDTPlugin concurrentQueue]
- -[ASDTPlugin setConcurrentQueue:]
- -[ASDTStream initWithConfig:withDevice:].cold.1
- -[ASDTStream ioBuffer]
- -[ASDTSystemPowerNotifier initForBundleName:delegate:earlyWake:]
- -[ASDTSystemPowerNotifier initForBundleName:delegate:earlyWake:].cold.1
- GCC_except_table108
- GCC_except_table119
- GCC_except_table121
- GCC_except_table124
- GCC_except_table125
- GCC_except_table127
- GCC_except_table132
- GCC_except_table133
- GCC_except_table151
- GCC_except_table152
- GCC_except_table153
- GCC_except_table163
- GCC_except_table165
- GCC_except_table166
- GCC_except_table176
- GCC_except_table179
- GCC_except_table182
- GCC_except_table185
- GCC_except_table188
- GCC_except_table199
- GCC_except_table207
- GCC_except_table213
- GCC_except_table218
- GCC_except_table226
- GCC_except_table232
- GCC_except_table235
- GCC_except_table238
- GCC_except_table242
- GCC_except_table243
- GCC_except_table244
- GCC_except_table245
- GCC_except_table248
- GCC_except_table91
- OBJC_IVAR_$_ASDTAudioDevice._statusProtocolObjects
- OBJC_IVAR_$_ASDTDeviceManager._initializingQueue
- OBJC_IVAR_$_ASDTExclavesSensorManager._statusTracker
- OBJC_IVAR_$_ASDTExclavesStatusProperty._sensorManager
- OBJC_IVAR_$_ASDTPMSequencer._pmConcurrentQueue
- OBJC_IVAR_$_ASDTPlugin._concurrentQueue
- _ZN4ASDT12IOUserClient20GuardedReleaseMemoryEPv.cold.1
- _ZN4ASDT12IOUserClient20GuardedReleaseMemoryEPv.cold.2
- _ZN4ASDT12IOUserClientC2EOS0_.cold.1
- __41-[ASDTPlugin requestConfigurationChange:]_block_invoke.24
- __OBJC_$_PROP_LIST_ASDPlugin_$_ASDTDeviceManager
- __OBJC_CATEGORY_PROTOCOLS_$_ASDPlugin_$_ASDTDeviceManager
- __OBJC_CLASS_PROTOCOLS_$_ASDTDeviceList
- __ZN10applesauce2CF10BooleanRefC1EPK11__CFBoolean
- __ZN10applesauce2CF13DictionaryRefC1EPK14__CFDictionary
- __ZN10applesauce2CF18make_DictionaryRefINS0_9StringRefENS0_7TypeRefEEENS0_13DictionaryRefERKNSt3__13mapIT_T0_NS5_4lessIS7_EENS5_9allocatorINS5_4pairIKS7_S8_EEEEEE
- __ZN10applesauce2CF7DataRefC1EPK8__CFData
- __ZN10applesauce2CF8ArrayRefC1EPK9__CFArray
- __ZN10applesauce2CF9NumberRefC1EPK10__CFNumber
- __ZN10applesauce2CF9StringRefC1EPK10__CFString
- __ZN10applesauce5iokit7details20io_services_iteratorC1ENS0_16io_object_holderE
- __ZN4ASDT12IOUserClient11SetPropertyERKN10applesauce2CF9StringRefERKNS2_13DictionaryRefE
- __ZN4ASDT12IOUserClient11SetPropertyERKN10applesauce2CF9StringRefERKNS2_7DataRefE
- __ZN4ASDT12IOUserClient11SetPropertyERKN10applesauce2CF9StringRefERKNS2_7TypeRefE
- __ZN4ASDT12IOUserClient11SetPropertyERKN10applesauce2CF9StringRefERKNS2_8ArrayRefE
- __ZN4ASDT12IOUserClient11SetPropertyERKN10applesauce2CF9StringRefES5_
- __ZN4ASDT12IOUserClient11SetPropertyERKN10applesauce2CF9StringRefEb
- __ZN4ASDT12IOUserClient11SetPropertyERKN10applesauce2CF9StringRefEd
- __ZN4ASDT12IOUserClient11SetPropertyERKN10applesauce2CF9StringRefEf
- __ZN4ASDT12IOUserClient11SetPropertyERKN10applesauce2CF9StringRefEi
- __ZN4ASDT12IOUserClient11SetPropertyERKN10applesauce2CF9StringRefEj
- __ZN4ASDT12IOUserClient11SetPropertyERKN10applesauce2CF9StringRefEx
- __ZN4ASDT12IOUserClient11SetPropertyERKN10applesauce2CF9StringRefEy
- __ZN4ASDT12IOUserClient13ReleaseMemoryEPv
- __ZN4ASDT12IOUserClient14OpenConnectionEj
- __ZN4ASDT12IOUserClient20GuardedReleaseMemoryEPv
- __ZN4ASDT12IOUserClient9MapMemoryEjjRj
- __ZN4ASDT12IOUserClientC1Ej
- __ZN4ASDT12IOUserClientC2Ej
- __ZN4ASDT12IOUserClientaSEj
- __ZNK10applesauce2CF7TypeRefcvNS0_10BooleanRefEEv
- __ZNK10applesauce2CF7TypeRefcvNS0_13DictionaryRefEEv
- __ZNK10applesauce2CF7TypeRefcvNS0_7DataRefEEv
- __ZNK10applesauce2CF7TypeRefcvNS0_8ArrayRefEEv
- __ZNK10applesauce2CF7TypeRefcvNS0_9NumberRefEEv
- __ZNK10applesauce2CF7TypeRefcvNS0_9StringRefEEv
- __ZNK4ASDT12IOUserClient10CallMethodEjPKyjPKvmPyPjPvPm
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE5rfindEcm
- __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorIN10applesauce2CF11TypeRefPairEEENS_16reverse_iteratorIPS4_EEEclB8ne180100Ev
- __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorIN10applesauce2CF7TypeRefEEENS_16reverse_iteratorIPS4_EEEclB8ne180100Ev
- __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorIN10applesauce2CF7TypeRefEEEPS4_EclB8ne180100Ev
- __ZNKSt3__16vectorI17CAAudioValueRangeNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN10applesauce2CF11TypeRefPairENS_9allocatorIS3_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN10applesauce2CF7TypeRefENS_9allocatorIS3_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN4ASDT8Exclaves13StatusTracker6UpdateENS_9allocatorIS4_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIPKvNS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt12out_of_rangeC1B8ne180100EPKc
- __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeIN10applesauce2CF9StringRefENS4_7TypeRefEEEPvEENS_22__tree_node_destructorINS_9allocatorIS9_EEEEE5resetB8ne180100EPS9_
- __ZNSt3__111shared_lockINS_12shared_mutexEE6unlockEv
- __ZNSt3__111shared_lockINS_12shared_mutexEED2B8ne180100Ev
- __ZNSt3__111unique_lockINS_12shared_mutexEE6unlockEv
- __ZNSt3__111unique_lockINS_12shared_mutexEED2B8ne180100Ev
- __ZNSt3__111unique_lockINS_5mutexEE6unlockEv
- __ZNSt3__112__destroy_atB8ne180100INS_4pairIKN10applesauce2CF9StringRefENS3_7TypeRefEEELi0EEEvPT_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne180100Emc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne180100ILi0EEEPKc
- __ZNSt3__112shared_mutexD1B8ne180100Ev
- __ZNSt3__113__tree_removeB8ne180100IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__114__split_bufferIN10applesauce2CF11TypeRefPairERNS_9allocatorIS3_EEE5clearB8ne180100Ev
- __ZNSt3__114__split_bufferIN10applesauce2CF7TypeRefERNS_9allocatorIS3_EEE5clearB8ne180100Ev
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorI17CAAudioValueRangeEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN10applesauce2CF11TypeRefPairEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN10applesauce2CF7TypeRefEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN4ASDT8Exclaves13StatusTracker6UpdateEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIPKvEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZNSt3__120__throw_system_errorEiPKc
- __ZNSt3__124__optional_destruct_baseIN10applesauce2CF7TypeRefELb0EED2B8ne180100Ev
- __ZNSt3__127__tree_balance_after_insertB8ne180100IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorIN10applesauce2CF11TypeRefPairEEENS_16reverse_iteratorIPS5_EEEEED2B8ne180100Ev
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorIN10applesauce2CF7TypeRefEEENS_16reverse_iteratorIPS5_EEEEED2B8ne180100Ev
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorIN10applesauce2CF7TypeRefEEEPS5_EEED2B8ne180100Ev
- __ZNSt3__135__uninitialized_allocator_copy_implB8ne180100INS_9allocatorIN10applesauce2CF7TypeRefEEENS3_17ArrayRef_iteratorIS4_EES7_PS4_EET2_RT_T0_T1_S9_
- __ZNSt3__13mapIN10applesauce2CF9StringRefENS2_7TypeRefENS_4lessIS3_EENS_9allocatorINS_4pairIKS3_S4_EEEEE16insert_or_assignB8ne180100IRS4_EENS8_INS_14__map_iteratorINS_15__tree_iteratorINS_12__value_typeIS3_S4_EEPNS_11__tree_nodeISI_PvEElEEEEbEERS9_OT_
- __ZNSt3__13mapIN10applesauce2CF9StringRefENS2_7TypeRefENS_4lessIS3_EENS_9allocatorINS_4pairIKS3_S4_EEEEE6insertB8ne180100INS2_22DictionaryRef_iteratorIS4_S4_EEEEvT_SG_
- __ZNSt3__13mapIN10applesauce2CF9StringRefENS2_7TypeRefENS_4lessIS3_EENS_9allocatorINS_4pairIKS3_S4_EEEEEC2B8ne180100INS2_22DictionaryRef_iteratorIS4_S4_EEEET_SG_RKS6_
- __ZNSt3__142__uninitialized_allocator_move_if_noexceptB8ne180100INS_9allocatorIN10applesauce2CF11TypeRefPairEEENS_16reverse_iteratorIPS4_EES8_S8_EET2_RT_T0_T1_S9_
- __ZNSt3__142__uninitialized_allocator_move_if_noexceptB8ne180100INS_9allocatorIN10applesauce2CF7TypeRefEEENS_16reverse_iteratorIPS4_EES8_S8_EET2_RT_T0_T1_S9_
- __ZNSt3__142__uninitialized_allocator_move_if_noexceptB8ne180100INS_9allocatorIN10applesauce2CF7TypeRefEEEPS4_S6_S6_EET2_RT_T0_T1_S7_
- __ZNSt3__14pairIKN10applesauce2CF9StringRefENS2_7TypeRefEEC2B8ne180100ILb1ELi0EEERS4_RKS5_
- __ZNSt3__14pairIKN10applesauce2CF9StringRefENS2_7TypeRefEEC2B8ne180100IRS4_RS5_Li0EEEOT_OT0_
- __ZNSt3__16__treeINS_12__value_typeIPvjEENS_19__map_value_compareIS2_S3_NS_4lessIS2_EELb1EEENS_9allocatorIS3_EEE13__move_assignERSA_NS_17integral_constantIbLb1EEE
- __ZNSt3__16__treeINS_12__value_typeIPvjEENS_19__map_value_compareIS2_S3_NS_4lessIS2_EELb1EEENS_9allocatorIS3_EEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIS2_EEEERSE_SE_
- __ZNSt3__16__treeINS_12__value_typeIPvjEENS_19__map_value_compareIS2_S3_NS_4lessIS2_EELb1EEENS_9allocatorIS3_EEE21__remove_node_pointerEPNS_11__tree_nodeIS3_S2_EE
- __ZNSt3__16__treeINS_12__value_typeIPvjEENS_19__map_value_compareIS2_S3_NS_4lessIS2_EELb1EEENS_9allocatorIS3_EEE25__emplace_unique_key_argsIS2_JRS2_RjEEENS_4pairINS_15__tree_iteratorIS3_PNS_11__tree_nodeIS3_S2_EElEEbEERKT_DpOT0_
- __ZNSt3__16__treeINS_12__value_typeIPvjEENS_19__map_value_compareIS2_S3_NS_4lessIS2_EELb1EEENS_9allocatorIS3_EEE7destroyEPNS_11__tree_nodeIS3_S2_EE
- __ZNSt3__16vectorIN10applesauce2CF11TypeRefPairENS_9allocatorIS3_EEE12emplace_backIJRKNS2_9StringRefERKNS2_7TypeRefEEEERS3_DpOT_
- __ZNSt3__16vectorIN10applesauce2CF11TypeRefPairENS_9allocatorIS3_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorIN10applesauce2CF11TypeRefPairENS_9allocatorIS3_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS3_RS5_EE
- __ZNSt3__16vectorIN10applesauce2CF7TypeRefENS_9allocatorIS3_EEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorIN10applesauce2CF7TypeRefENS_9allocatorIS3_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorIN10applesauce2CF7TypeRefENS_9allocatorIS3_EEE16__init_with_sizeB8ne180100INS2_17ArrayRef_iteratorIS3_EES9_EEvT_T0_m
- __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE16__init_with_sizeB8ne180100IPS2_S7_EEvT_T0_m
- __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEEC2Em
- __ZNSt3__19__advanceB8ne180100INS_20__map_const_iteratorINS_21__tree_const_iteratorINS_12__value_typeIN4ASDT8RawPointENS4_7DBPointEEEPNS_11__tree_nodeIS7_PvEElEEEEEEvRT_NS_15iterator_traitsISE_E15difference_typeENS_26bidirectional_iterator_tagE
- __ZNSt3__19allocatorIN10applesauce2CF11TypeRefPairEE7destroyB8ne180100EPS3_
- __ZNSt3__19allocatorIN10applesauce2CF7TypeRefEE7destroyB8ne180100EPS3_
- __ZNSt3__19allocatorIN10applesauce2CF7TypeRefEE9constructB8ne180100IS3_JRKS3_EEEvPT_DpOT0_
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
- ___45-[ASDTExclavesStatusProperty initWithConfig:]_block_invoke
- ___block_descriptor_56_e195_i40?0I8r^{AudioServerPlugInIOCycleInfo=QI{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}(?=dd)d}12^v20^v28I36l
- __block_literal_global.12
- _objc_msgSend$addStatusProtocolObject:toArray:
- _objc_msgSend$concurrentQueue
- _objc_msgSend$initForBundleName:delegate:earlyWake:
- _objc_msgSend$initializingQueue
- _objc_msgSend$ioBuffer
- _objc_msgSend$ioThreadStartStop:
- _objc_msgSend$notifierForBundleName:delegate:earlyWake:
- _objc_msgSend$pmConcurrentQueue
- _objc_msgSend$sensorManager
- _objc_msgSend$setConcurrentQueue:
- _objc_msgSend$setInitializingQueue:
- _objc_msgSend$setPmConcurrentQueue:
- _objc_msgSend$setSensorManager:
- _objc_msgSend$setStatusProtocolObjects:
- _objc_msgSend$setupStatusProtocol
- _objc_msgSend$statusProtocolObjects
- _objc_msgSend$statusTracker
- _objc_opt_self
CStrings:
+ "#"
+ "%@: Cannot StartIO: device %s."
+ "%@: Cannot StartIO: running a configuration change."
+ "%@: Failed creating PM sequencer with config: %@"
+ "%@: Failed subclass init with config: %@"
+ "%@: Finished background thread."
+ "%@: Unexpected starting state '%c%c%c%c' for transition to '%c%c%c%c' expected '%c%c%c%c'."
+ "%@: Waiting for thread to finish..."
+ "%@: retry from state: '%c%c%c%c'"
+ "%@:%@: Bad physical format; ramper is nil."
+ "%@:%@: Bad stream format: Bbf: %u, streamBufferSize: %u, period: %u"
+ "%@:%@: Failed to allocate ramper object."
+ "%@:%@: Maximum frames per IO: %u, unexpected size cycles: %u"
+ "*"
+ "240.42"
+ "@\"<ASDTExclavesStatusTrackerHostProtocol>\""
+ "@44@0:8@16@24@32B40"
+ "ASDTExclavesStatusTrackerHostProtocol"
+ "ASDTGlobalQueues"
+ "ASDTNonSecurePathEnableProperty"
+ "ASDTRamper: Bad format flags: %x"
+ "ASDTRamper: Format must be 32-bit: %u"
+ "ASDTRamper: Missing format flags: %x"
+ "ASDTTestingProtocol"
+ "ASDTUInt32Property"
+ "ASDTUserActivityClientProtocol"
+ "ASDTUserActivityManagerProtocol"
+ "AddNonSecurePathEnable"
+ "B28@0:8B16@20"
+ "IOConnect::Object::Release: called with refCount of %u"
+ "IOConnect::Retain: IOServiceOpen(%u) failed: %x (%c%c%c%c)"
+ "IOConnect::Retain: IOServiceOpen(%u) failed: %x (%c%c%c%c): Retrying..."
+ "IOMemoryMap: MapMemory(%u, %u, ...) failed: %x (%c%c%c%c)"
+ "IOMemoryMap: UnmapMemory() failed: %x (%c%c%c%c)"
+ "MockASDTSelectorControl"
+ "T*,N,V_ioBufferPtr"
+ "T@\"<ASDTExclavesStatusTrackerHostProtocol>\",&,N,V_statusTrackerHost"
+ "T@\"ASDTDeviceManager\",W,N,V_deviceManager"
+ "T@\"NSMutableDictionary\",&,N,V_protocolMap"
+ "T@?,C,N,V_propertyChangeBlock"
+ "TB,D,N"
+ "TB,N,V_testingEnabled"
+ "TB,N,V_userIsActive"
+ "TI,D,N"
+ "Ti,N,V_quiescentState"
+ "^*16@0:8"
+ "^I16@0:8"
+ "_ioBufferFramesSizeMax"
+ "_ioBufferFramesUnexpectedSizeCount"
+ "_ioBufferPtr"
+ "_propertyChangeBlock"
+ "_protocolMap"
+ "_protocolMutex"
+ "_quiescentState"
+ "_ramper"
+ "_statusTrackerHost"
+ "_testingEnabled"
+ "_updateTimestampPeriod:"
+ "_userIsActive"
+ "addedToDevice:"
+ "asdtAddNonSecurePathEnable"
+ "cancel"
+ "com.apple.AudioServerDriverTransports.ASDTDeviceManager.initCond"
+ "com.apple.AudioServerDriverTransports.Global.concurrentQueue"
+ "completeInitialization"
+ "concurrent"
+ "configurationChangeRunningForObject:"
+ "createForInput"
+ "doUpdateQuiescentState:"
+ "exclavesStatusTracker"
+ "executeSequenceToState:fromState:"
+ "i24@0:8@16"
+ "initForBundleName:delegate:queue:earlyWake:"
+ "ioBufferFramesSizeMax"
+ "ioBufferFramesUnexpectedSizeCount"
+ "ioBufferPtr"
+ "ioBufferRef"
+ "ioThreadStartStop:withStatusTracker:"
+ "isFinished"
+ "notifierForBundleName:delegate:queue:earlyWake:"
+ "objectsConformingAddObjects:"
+ "objectsConformingRemoveObjects:"
+ "objectsConformingToProtocol:"
+ "performPowerStateInactive:"
+ "pmInactiveStream:"
+ "propertyChangeBlock"
+ "protocolMap"
+ "quiescentState"
+ "ramper"
+ "removeControl:"
+ "removeInputStream:"
+ "removeOutputStream:"
+ "setEnabled:"
+ "setIoBufferPtr:"
+ "setNonSecureInputEnabled:onDevice:"
+ "setPropertyChangeBlock:"
+ "setProtocolMap:"
+ "setQuiescentState:"
+ "setStatusTrackerHost:"
+ "setTestingEnabled:"
+ "setUint32Value:"
+ "setUserIsActive:"
+ "setupPhysicalFormats:"
+ "setupSamplingRates:"
+ "sleeping"
+ "statusTrackerHost"
+ "stopThread"
+ "subclassInitWithConfig:"
+ "systemNotification"
+ "testingEnable:"
+ "testingEnabled"
+ "timestampPeriod"
+ "uint32Value"
+ "updateQuiescentState:"
+ "v24@0:8*16"
+ "v28@0:8B16^v20"
+ "{mutex=\"__m_\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}}"
+ "{unique_ptr<ASDT::Ramper, std::default_delete<ASDT::Ramper>>=\"__ptr_\"{__compressed_pair<ASDT::Ramper *, std::default_delete<ASDT::Ramper>>=\"__value_\"^{Ramper}}}"
+ "\xd1"
- "\""
- "%@: Failed creating PM seqeucner with config: %@"
- "%@: Memory allocation error on initializingQueue/Devices/Cond."
- "%s.%@.concurrent"
- "%s: MapMemory(%u, %u, ...) failed: %x (%c%c%c%c)"
- "%s: OpenConnection(%u) failed: %x (%c%c%c%c)"
- "%s: OpenConnection(%u) failed: %x (%c%c%c%c): Retrying..."
- "%s: ReleaseMemory() failed: %x (%c%c%c%c)"
- "%s: ReleaseMemory() not tracking map at %p"
- "'"
- "230.2"
- "ASDTExclavesSensorManager(%@): Failed to allocate memory."
- "T@\"ASDTExclavesSensorManager\",&,N,V_sensorManager"
- "T@\"NSArray\",&,N,V_statusProtocolObjects"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_concurrentQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_initializingQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_pmConcurrentQueue"
- "_concurrentQueue"
- "_initializingQueue"
- "_pmConcurrentQueue"
- "_sensorManager"
- "_statusProtocolObjects"
- "_statusTracker"
- "addStatusProtocolObject:toArray:"
- "com.apple.AudioServerDriverTransports.ASDTDeviceManager.initcond"
- "com.apple.AudioServerDriverTransports.ASDTDeviceManager.initqueue"
- "com.apple.AudioServerDriverTransports.ASDTPlugin.concurrentQueue"
- "concurrentQueue"
- "initForBundleName:delegate:earlyWake:"
- "initializingQueue"
- "ioBuffer"
- "ioThreadStartStop:"
- "pmConcurrentQueue"
- "sensorManager"
- "setConcurrentQueue:"
- "setInitializingQueue:"
- "setPmConcurrentQueue:"
- "setSensorManager:"
- "setStatusProtocolObjects:"
- "setupStatusProtocol"
- "shared_lock::unlock: not locked"
- "statusProtocolObjects"
- "statusTracker"
- "unique_lock::unlock: not locked"
- "{unique_ptr<ASDT::Exclaves::StatusTracker, std::default_delete<ASDT::Exclaves::StatusTracker>>=\"__ptr_\"{__compressed_pair<ASDT::Exclaves::StatusTracker *, std::default_delete<ASDT::Exclaves::StatusTracker>>=\"__value_\"^{StatusTracker}}}"

```
