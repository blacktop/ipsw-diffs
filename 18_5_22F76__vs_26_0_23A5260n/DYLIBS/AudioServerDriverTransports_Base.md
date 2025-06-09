## AudioServerDriverTransports_Base

> `/System/Library/PrivateFrameworks/AudioServerDriverTransports_Base.framework/AudioServerDriverTransports_Base`

```diff

-250.3.0.0.0
-  __TEXT.__text: 0x3e918
-  __TEXT.__auth_stubs: 0xe30
-  __TEXT.__objc_methlist: 0x3314
-  __TEXT.__gcc_except_tab: 0x5fd4
+300.65.0.0.0
+  __TEXT.__text: 0x3f9cc
+  __TEXT.__auth_stubs: 0xe20
+  __TEXT.__objc_methlist: 0x33cc
+  __TEXT.__gcc_except_tab: 0x6330
   __TEXT.__const: 0x50e
-  __TEXT.__cstring: 0x12e0
-  __TEXT.__oslogstring: 0x2fa4
-  __TEXT.__unwind_info: 0x1f70
-  __TEXT.__objc_classname: 0x6c8
-  __TEXT.__objc_methname: 0x6af8
-  __TEXT.__objc_methtype: 0x1194
-  __TEXT.__objc_stubs: 0x6340
-  __DATA_CONST.__got: 0x2c0
-  __DATA_CONST.__const: 0x750
-  __DATA_CONST.__objc_classlist: 0x1a0
+  __TEXT.__cstring: 0x13f0
+  __TEXT.__oslogstring: 0x2fc4
+  __TEXT.__unwind_info: 0x1fe0
+  __TEXT.__objc_classname: 0x6a1
+  __TEXT.__objc_methname: 0x6dd1
+  __TEXT.__objc_methtype: 0x1013
+  __TEXT.__objc_stubs: 0x6500
+  __DATA_CONST.__got: 0x2b8
+  __DATA_CONST.__const: 0x758
+  __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0x40
-  __DATA_CONST.__objc_protolist: 0xb0
+  __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c78
+  __DATA_CONST.__objc_selrefs: 0x1cc8
   __DATA_CONST.__objc_protorefs: 0x50
-  __DATA_CONST.__objc_superrefs: 0x160
+  __DATA_CONST.__objc_superrefs: 0x168
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__auth_got: 0x730
-  __AUTH_CONST.__const: 0x470
-  __AUTH_CONST.__cfstring: 0x1860
-  __AUTH_CONST.__objc_const: 0x51a8
-  __AUTH_CONST.__objc_intobj: 0x288
+  __AUTH_CONST.__auth_got: 0x728
+  __AUTH_CONST.__const: 0x450
+  __AUTH_CONST.__cfstring: 0x18e0
+  __AUTH_CONST.__objc_const: 0x51d0
+  __AUTH_CONST.__objc_intobj: 0x2a0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x910
-  __DATA.__objc_ivar: 0x2f8
-  __DATA.__data: 0x8a0
-  __DATA.__bss: 0x35
-  __DATA_DIRTY.__objc_data: 0x730
+  __DATA.__objc_ivar: 0x314
+  __DATA.__data: 0x840
+  __DATA.__bss: 0x48
+  __DATA_DIRTY.__objc_data: 0x6e0
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x60
+  __DATA_DIRTY.__bss: 0x40
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B443BB38-82A0-3B93-BCFD-58644A1B3E95
-  Functions: 1656
-  Symbols:   5636
-  CStrings:  2259
+  UUID: 48BB429A-6B3D-33C1-8641-2A93612A95DC
+  Functions: 1678
+  Symbols:   5701
+  CStrings:  2291
 
Symbols:
+ +[ASDTDeviceManager concurrentQueue]
+ +[ASDTDeviceManager concurrentQueue].cold.1
+ -[ASDTAudioDevice concurrentQueue]
+ -[ASDTDeviceManager concurrentQueue]
+ -[ASDTDeviceManager factoryPublishCond]
+ -[ASDTDeviceManager getInitStatusForDeviceUID:]
+ -[ASDTDeviceManager serialQueue]
+ -[ASDTDeviceManager setConcurrentQueue:]
+ -[ASDTDeviceManager setFactoryPublishCond:]
+ -[ASDTDeviceManager setSerialQueue:]
+ -[ASDTDeviceManagerSeeU .cxx_destruct]
+ -[ASDTDeviceManagerSeeU addAudioDeviceWithCheck:]
+ -[ASDTDeviceManagerSeeU addAudioDeviceWithCheck:].cold.1
+ -[ASDTDeviceManagerSeeU initWithConfig:withDelegate:]
+ -[ASDTDeviceManagerSeeU publishDevice:]
+ -[ASDTDeviceManagerSeeU publishUnderlyingDevicesProperty]
+ -[ASDTDeviceManagerSeeU removeAudioDevice:]
+ -[ASDTDeviceManagerSeeU removeAudioDevices:]
+ -[ASDTDeviceManagerSeeU setPublishUnderlyingDevicesProperty:]
+ -[ASDTDeviceManagerSeeU setUnderlyingDevices:]
+ -[ASDTDeviceManagerSeeU setUnderlyingDevicesArePublished:]
+ -[ASDTDeviceManagerSeeU setupPublishUnderlyingDevicesProperty]
+ -[ASDTDeviceManagerSeeU underlyingDevicesArePublished]
+ -[ASDTDeviceManagerSeeU underlyingDevices]
+ -[ASDTDeviceManagerSeeU updateUnderlyingDeviceVisibility]
+ -[ASDTPMActionNumericPropertyAnalyticsEvent lock]
+ -[ASDTPMActionNumericPropertyAnalyticsEvent setLock:]
+ -[ASDTPlugin concurrentQueue]
+ -[ASDTPlugin setConcurrentQueue:]
+ -[NSDictionary(ASDTConfig) asdtOptionallyPublishedDevice]
+ GCC_except_table108
+ GCC_except_table117
+ GCC_except_table118
+ GCC_except_table119
+ GCC_except_table120
+ GCC_except_table121
+ GCC_except_table128
+ GCC_except_table129
+ GCC_except_table132
+ GCC_except_table140
+ GCC_except_table141
+ GCC_except_table153
+ GCC_except_table158
+ GCC_except_table166
+ GCC_except_table168
+ GCC_except_table176
+ GCC_except_table179
+ GCC_except_table182
+ GCC_except_table185
+ GCC_except_table188
+ GCC_except_table191
+ GCC_except_table195
+ GCC_except_table199
+ GCC_except_table201
+ GCC_except_table203
+ GCC_except_table211
+ GCC_except_table213
+ GCC_except_table218
+ GCC_except_table219
+ GCC_except_table220
+ GCC_except_table225
+ GCC_except_table231
+ GCC_except_table232
+ GCC_except_table235
+ GCC_except_table91
+ _OBJC_CLASS_$_ASDTDeviceManagerSeeU
+ _OBJC_IVAR_$_ASDTDeviceManager._concurrentQueue
+ _OBJC_IVAR_$_ASDTDeviceManager._factoryPublishCond
+ _OBJC_IVAR_$_ASDTDeviceManager._serialQueue
+ _OBJC_IVAR_$_ASDTDeviceManagerSeeU._publishUnderlyingDevicesProperty
+ _OBJC_IVAR_$_ASDTDeviceManagerSeeU._underlyingDevices
+ _OBJC_IVAR_$_ASDTDeviceManagerSeeU._underlyingDevicesArePublished
+ _OBJC_IVAR_$_ASDTPMActionNumericPropertyAnalyticsEvent._lock
+ _OBJC_IVAR_$_ASDTPlugin._concurrentQueue
+ _OBJC_METACLASS_$_ASDTDeviceManagerSeeU
+ __OBJC_$_INSTANCE_METHODS_ASDTDeviceManagerSeeU
+ __OBJC_$_INSTANCE_VARIABLES_ASDTDeviceManagerSeeU
+ __OBJC_$_PROP_LIST_ASDTDeviceManagerSeeU
+ __OBJC_CLASS_RO_$_ASDTDeviceManagerSeeU
+ __OBJC_METACLASS_RO_$_ASDTDeviceManagerSeeU
+ __ZN10applesauce2CF9ObjectRefIPK10__CFStringED2Ev
+ __ZN10applesauce2CF9ObjectRefIPK11__CFBooleanED2Ev
+ __ZN10applesauce2CF9ObjectRefIPK14__CFDictionaryED2Ev
+ __ZN10applesauce2CF9ObjectRefIPK8__CFDataED2Ev
+ __ZN10applesauce2CF9ObjectRefIPK9__CFArrayED2Ev
+ __ZN10applesauce2CF9StringRefD2Ev
+ __ZN5caulk10concurrent9messenger5drainEv
+ __ZNK10applesauce2CF7TypeRefcvNS0_10BooleanRefEEv
+ __ZNK10applesauce2CF7TypeRefcvNS0_13DictionaryRefEEv
+ __ZNK10applesauce2CF7TypeRefcvNS0_7DataRefEEv
+ __ZNK10applesauce2CF7TypeRefcvNS0_8ArrayRefEEv
+ __ZNK10applesauce2CF7TypeRefcvNS0_9NumberRefEEv
+ __ZNK10applesauce2CF7TypeRefcvNS0_9StringRefEEv
+ __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorIN10applesauce2CF11TypeRefPairEEEPS4_EclB8ne200100Ev
+ __ZNSt12length_errorC1B8ne200100EPKc
+ __ZNSt12out_of_rangeC1B8ne200100EPKc
+ __ZNSt3__111shared_lockINS_12shared_mutexEED2B8ne200100Ev
+ __ZNSt3__111unique_lockINS_12shared_mutexEED2B8ne200100Ev
+ __ZNSt3__112__destroy_atB8ne200100IN10applesauce2CF7TypeRefELi0EEEvPT_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne200100ILi0EEEPKc
+ __ZNSt3__112construct_atB8ne200100IN10applesauce2CF7TypeRefEJRKS3_EPS3_EEPT_S8_DpOT0_
+ __ZNSt3__112shared_mutexD1B8ne200100Ev
+ __ZNSt3__113__tree_removeB8ne200100IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__114__split_bufferIN10applesauce2CF11TypeRefPairERNS_9allocatorIS3_EEE17__destruct_at_endB8ne200100EPS3_
+ __ZNSt3__114__split_bufferIN10applesauce2CF7TypeRefERNS_9allocatorIS3_EEE12emplace_backIJRKS3_EEEvDpOT_
+ __ZNSt3__116allocator_traitsINS_9allocatorIN10applesauce2CF11TypeRefPairEEEE7destroyB8ne200100IS4_vLi0EEEvRS5_PT_
+ __ZNSt3__116allocator_traitsINS_9allocatorIN10applesauce2CF11TypeRefPairEEEE9constructB8ne200100IS4_JRKNS3_9StringRefERKNS3_7TypeRefEEvLi0EEEvRS5_PT_DpOT0_
+ __ZNSt3__116allocator_traitsINS_9allocatorINS_11__tree_nodeINS_12__value_typeIN10applesauce2CF9StringRefENS5_7TypeRefEEEPvEEEEE7destroyB8ne200100INS_4pairIKS6_S7_EEvLi0EEEvRSB_PT_
+ __ZNSt3__119__shared_weak_count16__release_sharedB8ne200100Ev
+ __ZNSt3__120__throw_length_errorB8ne200100EPKc
+ __ZNSt3__122__tree_node_destructorINS_9allocatorINS_11__tree_nodeINS_12__value_typeIN10applesauce2CF9StringRefENS5_7TypeRefEEEPvEEEEEclB8ne200100EPSA_
+ __ZNSt3__127__tree_balance_after_insertB8ne200100IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorIN10applesauce2CF11TypeRefPairEEEPS5_EEED2B8ne200100Ev
+ __ZNSt3__134__uninitialized_allocator_relocateB8ne200100INS_9allocatorIN10applesauce2CF11TypeRefPairEEEPS4_EEvRT_T0_S9_S9_
+ __ZNSt3__135__uninitialized_allocator_copy_implB8ne200100INS_9allocatorIN10applesauce2CF7TypeRefEEENS3_17ArrayRef_iteratorIS4_EES7_PS4_EET2_RT_T0_T1_S9_
+ __ZNSt3__13mapIN10applesauce2CF9StringRefENS2_7TypeRefENS_4lessIS3_EENS_9allocatorINS_4pairIKS3_S4_EEEEE16insert_or_assignB8ne200100IRS4_EENS8_INS_14__map_iteratorINS_15__tree_iteratorINS_12__value_typeIS3_S4_EEPNS_11__tree_nodeISI_PvEElEEEEbEERS9_OT_
+ __ZNSt3__13mapIN10applesauce2CF9StringRefENS2_7TypeRefENS_4lessIS3_EENS_9allocatorINS_4pairIKS3_S4_EEEEE6insertB8ne200100INS2_22DictionaryRef_iteratorIS4_S4_EEEEvT_SG_
+ __ZNSt3__13mapIN10applesauce2CF9StringRefENS2_7TypeRefENS_4lessIS3_EENS_9allocatorINS_4pairIKS3_S4_EEEEEC2B8ne200100INS2_22DictionaryRef_iteratorIS4_S4_EEEET_SG_RKS6_
+ __ZNSt3__14pairIN10applesauce2CF7TypeRefES3_ED2Ev
+ __ZNSt3__16__treeINS_12__value_typeIN10applesauce2CF9StringRefENS3_7TypeRefEEENS_19__map_value_compareIS4_S6_NS_4lessIS4_EELb1EEENS_9allocatorIS6_EEE16__construct_nodeIJRKS4_RKS5_EEENS_10unique_ptrINS_11__tree_nodeIS6_PvEENS_22__tree_node_destructorINSB_ISM_EEEEEEDpOT_
+ __ZNSt3__16__treeINS_12__value_typeIN10applesauce2CF9StringRefENS3_7TypeRefEEENS_19__map_value_compareIS4_S6_NS_4lessIS4_EELb1EEENS_9allocatorIS6_EEE16__construct_nodeIJRKS4_RS5_EEENS_10unique_ptrINS_11__tree_nodeIS6_PvEENS_22__tree_node_destructorINSB_ISL_EEEEEEDpOT_
+ __ZNSt3__16__treeINS_12__value_typeIN10applesauce2CF9StringRefENS3_7TypeRefEEENS_19__map_value_compareIS4_S6_NS_4lessIS4_EELb1EEENS_9allocatorIS6_EEE5eraseENS_21__tree_const_iteratorIS6_PNS_11__tree_nodeIS6_PvEElEE
+ __ZNSt3__16vectorIN10applesauce2CF11TypeRefPairENS_9allocatorIS3_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorIN10applesauce2CF11TypeRefPairENS_9allocatorIS3_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN10applesauce2CF11TypeRefPairENS_9allocatorIS3_EEE22__base_destruct_at_endB8ne200100EPS3_
+ __ZNSt3__16vectorIN10applesauce2CF7TypeRefENS_9allocatorIS3_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIN10applesauce2CF7TypeRefENS_9allocatorIS3_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorIN10applesauce2CF7TypeRefENS_9allocatorIS3_EEE16__init_with_sizeB8ne200100INS2_17ArrayRef_iteratorIS3_EES9_EEvT_T0_m
+ __ZNSt3__16vectorIN10applesauce2CF7TypeRefENS_9allocatorIS3_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN4ASDT8Exclaves13StatusTracker6UpdateENS_9allocatorIS4_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE16__init_with_sizeB8ne200100IPS2_S7_EEvT_T0_m
+ __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEEC2B8ne200100Em
+ __ZNSt3__19__advanceB8ne200100INS_20__map_const_iteratorINS_21__tree_const_iteratorINS_12__value_typeIN4ASDT8RawPointENS4_7DBPointEEEPNS_11__tree_nodeIS7_PvEElEEEEEEvRT_NS_15iterator_traitsISE_E15difference_typeENS_26bidirectional_iterator_tagE
+ __ZNSt3__19allocatorIN10applesauce2CF11TypeRefPairEE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIN10applesauce2CF7TypeRefEE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIN4ASDT8Exclaves13StatusTracker6UpdateEE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIPKvE17allocate_at_leastB8ne200100Em
+ __ZSt28__throw_bad_array_new_lengthB8ne200100v
+ __ZZ36+[ASDTDeviceManager concurrentQueue]E16sConcurrentQueue
+ __ZZ36+[ASDTDeviceManager concurrentQueue]E9onceToken
+ ___36+[ASDTDeviceManager concurrentQueue]_block_invoke
+ ___42-[ASDTAudioDeviceFactory initializeDevice]_block_invoke
+ ___62-[ASDTDeviceManagerSeeU setupPublishUnderlyingDevicesProperty]_block_invoke
+ ___62-[ASDTDeviceManagerSeeU setupPublishUnderlyingDevicesProperty]_block_invoke_2
+ ___block_descriptor_40_ea8_32w_e8_v16?08lw32l8
+ _kASDTConfigKeyOptionallyPublishedDevice
+ _objc_msgSend$asdtOptionallyPublishedDevice
+ _objc_msgSend$concurrentQueue
+ _objc_msgSend$factoryForDeviceUID:
+ _objc_msgSend$factoryPublishCond
+ _objc_msgSend$powerNotificationQueue
+ _objc_msgSend$publishUnderlyingDevicesProperty
+ _objc_msgSend$serialQueue
+ _objc_msgSend$setConcurrentQueue:
+ _objc_msgSend$setFactoryPublishCond:
+ _objc_msgSend$setPropertyChangeBlock:
+ _objc_msgSend$setPublishUnderlyingDevicesProperty:
+ _objc_msgSend$setSerialQueue:
+ _objc_msgSend$setUnderlyingDevices:
+ _objc_msgSend$setUnderlyingDevicesArePublished:
+ _objc_msgSend$setupPublishUnderlyingDevicesProperty
+ _objc_msgSend$underlyingDevices
+ _objc_msgSend$underlyingDevicesArePublished
+ _objc_msgSend$updateUnderlyingDeviceVisibility
- +[ASDTGlobalQueues concurrent]
- +[ASDTGlobalQueues concurrent].cold.1
- +[ASDTGlobalQueues systemNotification]
- +[ASDTGlobalQueues systemNotification].cold.1
- -[ASDTCustomPropertyCachePMEnabler deviceName]
- -[ASDTPMActionAnalyticsEvent deviceName]
- -[ASDTPMActionNumericPropertyAnalyticsEvent deviceName]
- -[ASDTPMDevice deviceName]
- -[MockASDTSelectorControl setTestingEnabled:]
- -[MockASDTSelectorControl testingEnable:]
- -[MockASDTSelectorControl testingEnabled]
- GCC_except_table114
- GCC_except_table123
- GCC_except_table126
- GCC_except_table134
- GCC_except_table135
- GCC_except_table136
- GCC_except_table137
- GCC_except_table143
- GCC_except_table144
- GCC_except_table149
- GCC_except_table150
- GCC_except_table157
- GCC_except_table164
- GCC_except_table167
- GCC_except_table175
- GCC_except_table178
- GCC_except_table181
- GCC_except_table184
- GCC_except_table187
- GCC_except_table190
- GCC_except_table193
- GCC_except_table196
- GCC_except_table197
- GCC_except_table200
- GCC_except_table216
- GCC_except_table217
- GCC_except_table221
- GCC_except_table227
- GCC_except_table233
- GCC_except_table67
- GCC_except_table97
- _OBJC_CLASS_$_ASDTGlobalQueues
- _OBJC_CLASS_$_MockASDTSelectorControl
- _OBJC_IVAR_$_MockASDTSelectorControl._testingEnabled
- _OBJC_METACLASS_$_ASDTGlobalQueues
- _OBJC_METACLASS_$_MockASDTSelectorControl
- __OBJC_$_CLASS_METHODS_ASDTGlobalQueues
- __OBJC_$_INSTANCE_METHODS_MockASDTSelectorControl
- __OBJC_$_INSTANCE_VARIABLES_MockASDTSelectorControl
- __OBJC_$_PROP_LIST_ASDTTestingProtocol
- __OBJC_$_PROP_LIST_MockASDTSelectorControl
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_ASDTTestingProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_ASDTTestingProtocol
- __OBJC_$_PROTOCOL_REFS_ASDTTestingProtocol
- __OBJC_CLASS_PROTOCOLS_$_MockASDTSelectorControl
- __OBJC_CLASS_RO_$_ASDTGlobalQueues
- __OBJC_CLASS_RO_$_MockASDTSelectorControl
- __OBJC_LABEL_PROTOCOL_$_ASDTTestingProtocol
- __OBJC_METACLASS_RO_$_ASDTGlobalQueues
- __OBJC_METACLASS_RO_$_MockASDTSelectorControl
- __OBJC_PROTOCOL_$_ASDTTestingProtocol
- __ZN10applesauce2CF10BooleanRef8from_getEPK11__CFBoolean
- __ZN10applesauce2CF11TypeRefPairC2IRKNS0_9StringRefERKNS0_7TypeRefEEEOT_OT0_
- __ZN10applesauce2CF13DictionaryRef8from_getEPK14__CFDictionary
- __ZN10applesauce2CF7DataRef8from_getEPK8__CFData
- __ZN10applesauce2CF8ArrayRef8from_getEPK9__CFArray
- __ZN10applesauce2CF9NumberRef8from_getEPK10__CFNumber
- __ZN10applesauce2CF9ObjectRefIPK10__CFStringED1Ev
- __ZN10applesauce2CF9ObjectRefIPK11__CFBooleanED1Ev
- __ZN10applesauce2CF9ObjectRefIPK14__CFDictionaryED1Ev
- __ZN10applesauce2CF9ObjectRefIPK8__CFDataED1Ev
- __ZN10applesauce2CF9ObjectRefIPK9__CFArrayED1Ev
- __ZN10applesauce2CF9StringRef8from_getEPK10__CFString
- __ZN10applesauce2CF9StringRefD1Ev
- __ZN4ASDT6Ramper6CreateERK27AudioStreamBasicDescriptionj
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN10applesauce2CF11TypeRefPairENS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN10applesauce2CF7TypeRefENS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN4ASDT8Exclaves13StatusTracker6UpdateENS_9allocatorIS4_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIPKvNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNSt12length_errorC1B8ne190102EPKc
- __ZNSt12out_of_rangeC1B8ne190102EPKc
- __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeIN10applesauce2CF9StringRefENS4_7TypeRefEEEPvEENS_22__tree_node_destructorINS_9allocatorIS9_EEEEE5resetB8ne190102EPS9_
- __ZNSt3__111shared_lockINS_12shared_mutexEED2B8ne190102Ev
- __ZNSt3__111unique_lockINS_12shared_mutexEED2B8ne190102Ev
- __ZNSt3__112__destroy_atB8ne190102IN10applesauce2CF11TypeRefPairELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne190102IN10applesauce2CF7TypeRefELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne190102INS_4pairIKN10applesauce2CF9StringRefENS3_7TypeRefEEELi0EEEvPT_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102Emc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ILi0EEEPKc
- __ZNSt3__112construct_atB8ne190102IN10applesauce2CF7TypeRefEJRKS3_EPS3_EEPT_S8_DpOT0_
- __ZNSt3__112shared_mutexD1B8ne190102Ev
- __ZNSt3__113__tree_removeB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN10applesauce2CF11TypeRefPairEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN10applesauce2CF7TypeRefEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN4ASDT8Exclaves13StatusTracker6UpdateEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPKvEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__shared_weak_count16__release_sharedB8ne190102Ev
- __ZNSt3__120__throw_length_errorB8ne190102EPKc
- __ZNSt3__124__optional_destruct_baseIN10applesauce2CF7TypeRefELb0EED2B8ne190102Ev
- __ZNSt3__127__tree_balance_after_insertB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__134__uninitialized_allocator_relocateB8ne190102INS_9allocatorIN10applesauce2CF11TypeRefPairEEES4_EEvRT_PT0_S9_S9_
- __ZNSt3__135__uninitialized_allocator_copy_implB8ne190102INS_9allocatorIN10applesauce2CF7TypeRefEEENS3_17ArrayRef_iteratorIS4_EES7_PS4_EET2_RT_T0_T1_S9_
- __ZNSt3__13mapIN10applesauce2CF9StringRefENS2_7TypeRefENS_4lessIS3_EENS_9allocatorINS_4pairIKS3_S4_EEEEE16insert_or_assignB8ne190102IRS4_EENS8_INS_14__map_iteratorINS_15__tree_iteratorINS_12__value_typeIS3_S4_EEPNS_11__tree_nodeISI_PvEElEEEEbEERS9_OT_
- __ZNSt3__13mapIN10applesauce2CF9StringRefENS2_7TypeRefENS_4lessIS3_EENS_9allocatorINS_4pairIKS3_S4_EEEEE6insertB8ne190102INS2_22DictionaryRef_iteratorIS4_S4_EEEEvT_SG_
- __ZNSt3__13mapIN10applesauce2CF9StringRefENS2_7TypeRefENS_4lessIS3_EENS_9allocatorINS_4pairIKS3_S4_EEEEEC2B8ne190102INS2_22DictionaryRef_iteratorIS4_S4_EEEET_SG_RKS6_
- __ZNSt3__14pairIKN10applesauce2CF9StringRefENS2_7TypeRefEEC2B8ne190102ILb1ELi0EEERS4_RKS5_
- __ZNSt3__14pairIKN10applesauce2CF9StringRefENS2_7TypeRefEEC2B8ne190102IRS4_RS5_Li0EEEOT_OT0_
- __ZNSt3__14pairIKN10applesauce2CF9StringRefENS2_7TypeRefEEC2B8ne190102IS5_S5_Li0EEEONS0_IT_T0_EE
- __ZNSt3__14pairIN10applesauce2CF7TypeRefES3_ED1Ev
- __ZNSt3__16vectorIN10applesauce2CF11TypeRefPairENS_9allocatorIS3_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorIN10applesauce2CF7TypeRefENS_9allocatorIS3_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorIN10applesauce2CF7TypeRefENS_9allocatorIS3_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorIN10applesauce2CF7TypeRefENS_9allocatorIS3_EEE16__init_with_sizeB8ne190102INS2_17ArrayRef_iteratorIS3_EES9_EEvT_T0_m
- __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE16__init_with_sizeB8ne190102IPS2_S7_EEvT_T0_m
- __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEEC2B8ne190102Em
- __ZNSt3__19__advanceB8ne190102INS_20__map_const_iteratorINS_21__tree_const_iteratorINS_12__value_typeIN4ASDT8RawPointENS4_7DBPointEEEPNS_11__tree_nodeIS7_PvEElEEEEEEvRT_NS_15iterator_traitsISE_E15difference_typeENS_26bidirectional_iterator_tagE
- __ZSt28__throw_bad_array_new_lengthB8ne190102v
- __Znwm
- ___30+[ASDTGlobalQueues concurrent]_block_invoke
- ___38+[ASDTGlobalQueues systemNotification]_block_invoke
- ___block_descriptor_56_ea8_32s40s48w_e5_v8?0ls32l8s40l8w48l8
- ___block_literal_global.3
- _concurrent.onceToken
- _concurrent.sConcurrentQueue
- _memset
- _objc_msgSend$concurrent
- _objc_msgSend$setIsActive:
- _objc_msgSend$setTestingEnabled:
- _objc_msgSend$systemNotification
- _systemNotification.onceToken
- _systemNotification.sNotificationQueue
CStrings:
+ "  Added %@ to underlyingDevices"
+ "300.65"
+ "@\"ASDTPlugin\""
+ "@\"ASDTUInt32Property\""
+ "ASDTDeviceManagerSeeU"
+ "OptionallyPublished"
+ "T@\"ASDTCondition\",&,N,V_factoryPublishCond"
+ "T@\"ASDTCondition\",&,N,V_lock"
+ "T@\"ASDTPlugin\",W,N,V_plugin"
+ "T@\"ASDTUInt32Property\",&,N,V_publishUnderlyingDevicesProperty"
+ "T@\"NSMutableSet\",&,N,V_underlyingDevices"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_concurrentQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_serialQueue"
+ "TB,N,V_underlyingDevicesArePublished"
+ "_concurrentQueue"
+ "_factoryPublishCond"
+ "_publishUnderlyingDevicesProperty"
+ "_serialQueue"
+ "_underlyingDevices"
+ "_underlyingDevicesArePublished"
+ "asdtOptionallyPublishedDevice"
+ "com.apple.AudioServerDriverTransports.ASDTDeviceManager.concurrentQueue"
+ "com.apple.AudioServerDriverTransports.ASDTDeviceManager.factoryCond"
+ "com.apple.AudioServerDriverTransports.ASDTDeviceManager.serialQueue"
+ "com.apple.AudioServerDriverTransports.ASDTPlugin.concurrentQueue"
+ "concurrentQueue"
+ "factoryPublishCond"
+ "getInitStatusForDeviceUID:"
+ "publishUnderlyingDevicesProperty"
+ "sampleTime"
+ "serialQueue"
+ "setConcurrentQueue:"
+ "setFactoryPublishCond:"
+ "setPublishUnderlyingDevicesProperty:"
+ "setSerialQueue:"
+ "setUnderlyingDevices:"
+ "setUnderlyingDevicesArePublished:"
+ "setupPublishUnderlyingDevicesProperty"
+ "underlyingDevices"
+ "underlyingDevicesArePublished"
+ "updateUnderlyingDeviceVisibility"
+ "v16@?0@8"
+ "{unique_ptr<ASDT::Exclaves::AudioBuffer, std::default_delete<ASDT::Exclaves::AudioBuffer>>=\"__ptr_\"^{AudioBuffer}}"
+ "{unique_ptr<ASDT::Exclaves::InboundBuffer, std::default_delete<ASDT::Exclaves::InboundBuffer>>=\"__ptr_\"^{InboundBuffer}}"
+ "{unique_ptr<ASDT::Exclaves::Sensor, std::default_delete<ASDT::Exclaves::Sensor>>=\"__ptr_\"^{Sensor}}"
+ "{unique_ptr<ASDT::Ramper, std::default_delete<ASDT::Ramper>>=\"__ptr_\"^{Ramper}}"
- "250.3"
- "@\"ASDPlugin\""
- "ASDTGlobalQueues"
- "ASDTTestingProtocol"
- "MockASDTSelectorControl"
- "T@\"ASDPlugin\",W,N,V_plugin"
- "TB,N,V_testingEnabled"
- "_testingEnabled"
- "com.apple.AudioServerDriverTransports.Global.concurrentQueue"
- "concurrent"
- "setIsActive:"
- "setTestingEnabled:"
- "systemNotification"
- "testingEnable:"
- "testingEnabled"
- "{unique_ptr<ASDT::Exclaves::AudioBuffer, std::default_delete<ASDT::Exclaves::AudioBuffer>>=\"__ptr_\"{__compressed_pair<ASDT::Exclaves::AudioBuffer *, std::default_delete<ASDT::Exclaves::AudioBuffer>>=\"__value_\"^{AudioBuffer}}}"
- "{unique_ptr<ASDT::Exclaves::InboundBuffer, std::default_delete<ASDT::Exclaves::InboundBuffer>>=\"__ptr_\"{__compressed_pair<ASDT::Exclaves::InboundBuffer *, std::default_delete<ASDT::Exclaves::InboundBuffer>>=\"__value_\"^{InboundBuffer}}}"
- "{unique_ptr<ASDT::Exclaves::Sensor, std::default_delete<ASDT::Exclaves::Sensor>>=\"__ptr_\"{__compressed_pair<ASDT::Exclaves::Sensor *, std::default_delete<ASDT::Exclaves::Sensor>>=\"__value_\"^{Sensor}}}"
- "{unique_ptr<ASDT::Ramper, std::default_delete<ASDT::Ramper>>=\"__ptr_\"{__compressed_pair<ASDT::Ramper *, std::default_delete<ASDT::Ramper>>=\"__value_\"^{Ramper}}}"

```
