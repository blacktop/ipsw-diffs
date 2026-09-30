## IOKit

> `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`

```diff

-100140.81.1.0.0
-  __TEXT.__text: 0xb7158
+100150.100.19.0.0
+  __TEXT.__text: 0xb6b08
   __TEXT.__auth_stubs: 0x22b0
   __TEXT.__objc_methlist: 0x150
-  __TEXT.__cstring: 0xec75
-  __TEXT.__const: 0xeba0
+  __TEXT.__cstring: 0xec3d
+  __TEXT.__const: 0x10608
   __TEXT.__dlopen_cstrs: 0x57
-  __TEXT.__oslogstring: 0x4b13
-  __TEXT.__gcc_except_tab: 0x574
-  __TEXT.__unwind_info: 0x2348
+  __TEXT.__oslogstring: 0x4b83
+  __TEXT.__gcc_except_tab: 0x5e0
+  __TEXT.__unwind_info: 0x23c8
   __TEXT.__objc_classname: 0x58
   __TEXT.__objc_methname: 0xa3
-  __TEXT.__objc_methtype: 0x1972
+  __TEXT.__objc_methtype: 0x19b4
   __TEXT.__objc_stubs: 0x60
-  __DATA_CONST.__got: 0x228
-  __DATA_CONST.__const: 0x2278
+  __DATA_CONST.__got: 0x218
+  __DATA_CONST.__const: 0x22a0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x38
   __AUTH_CONST.__auth_got: 0x1168
   __AUTH_CONST.__const: 0x2388
-  __AUTH_CONST.__cfstring: 0x7f00
+  __AUTH_CONST.__cfstring: 0x7f20
   __AUTH_CONST.__objc_const: 0x508
-  __AUTH.__data: 0x10
+  __AUTH.__data: 0x20
   __DATA.__objc_ivar: 0x1c
   __DATA.__data: 0x5e8
   __DATA.__bss: 0x798
-  __DATA.__common: 0xc0
+  __DATA.__common: 0x100
   __DATA_DIRTY.__objc_data: 0x230
-  __DATA_DIRTY.__data: 0x138
+  __DATA_DIRTY.__data: 0x128
   __DATA_DIRTY.__bss: 0xa8
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
   - /usr/lib/system/libkxld.dylib
-  UUID: FFD74642-9D8E-31DB-AD51-41EB5F08837B
-  Functions: 3742
-  Symbols:   5162
-  CStrings:  3912
+  UUID: AD7EC8BC-9612-3A26-9967-5B81F1EEA596
+  Functions: 3611
+  Symbols:   5252
+  CStrings:  3910
 
Symbols:
+ GCC_except_table108
+ GCC_except_table109
+ GCC_except_table113
+ GCC_except_table117
+ GCC_except_table121
+ GCC_except_table124
+ GCC_except_table128
+ GCC_except_table133
+ GCC_except_table134
+ GCC_except_table71
+ GCC_except_table79
+ GCC_except_table83
+ GCC_except_table84
+ GCC_except_table87
+ GCC_except_table92
+ GCC_except_table95
+ IOHIDAccessCheckAuditToken.cold.1
+ IOHIDAnalyticsEventCreate.cold.1
+ IOHIDAnalyticsHistogramEventCreate.cold.1
+ IOHIDDeviceCreate.cold.4
+ IOHIDDeviceCreate.cold.5
+ IOHIDDeviceSetProperty.cold.1
+ IOHIDEventGetPolicy.cold.2
+ IOHIDEventGetPolicy.cold.3
+ IOHIDEventGetPolicy.cold.4
+ IOHIDEventGetPolicy.cold.5
+ IOHIDEventGetPolicy.cold.6
+ IOHIDEventGetVendorDefinedData.cold.1
+ IOHIDEventGetVendorDefinedData.cold.2
+ IOHIDEventQueueGetTypeID.cold.1
+ IOHIDManagerActivate.cold.1
+ IOHIDManagerUnscheduleFromRunLoop.cold.1
+ IOHIDPostEvent.cold.1
+ IOHIDPostEvent.cold.2
+ IOHIDPreferencesCopy.cold.1
+ IOHIDPreferencesCopyDomain.cold.1
+ IOHIDPreferencesCopyDomainForInstance.cold.1
+ IOHIDPreferencesCopyForInstance.cold.1
+ IOHIDPreferencesCopyMultiple.cold.1
+ IOHIDPreferencesCopyMultipleForInstance.cold.1
+ IOHIDPreferencesCreateInstance.cold.1
+ IOHIDPreferencesSet.cold.1
+ IOHIDPreferencesSetDomain.cold.1
+ IOHIDPreferencesSetDomainForInstance.cold.1
+ IOHIDPreferencesSetForInstance.cold.1
+ IOHIDPreferencesSetMultiple.cold.1
+ IOHIDPreferencesSetMultipleForInstance.cold.1
+ IOHIDPreferencesSynchronize.cold.1
+ IOHIDPreferencesSynchronizeForInstance.cold.1
+ IOHIDQueueSetDispatchQueue.cold.2
+ IOHIDServiceConformsTo.cold.2
+ IOHIDServiceConnectionCacheGetTypeID.cold.1
+ IOHIDServiceRegister.cold.1
+ IOHIDUserDeviceSetDispatchQueue.cold.2
+ OSKextCreatePrelinkedKernel.cold.10
+ OSKextCreatePrelinkedKernel.cold.11
+ OSKextCreatePrelinkedKernel.cold.12
+ OSKextCreatePrelinkedKernel.cold.13
+ OSKextCreatePrelinkedKernel.cold.14
+ OSKextCreatePrelinkedKernel.cold.7
+ OSKextCreatePrelinkedKernel.cold.8
+ OSKextCreatePrelinkedKernel.cold.9
+ _IOHIDDebugTrace.cold.1
+ _IOHIDEventSystemConnectionSetProperty.cold.3
+ _IOHIDEventSystemConnectionSetProperty.cold.4
+ _IOHIDEventSystemConnectionSetProperty.cold.5
+ _IOHIDEventSystemConnectionSetProperty.cold.6
+ _IOHIDEventSystemRematchServices
+ _IOHIDLoadBundles.cold.1
+ _IOHIDLoadConnectionPluginBundles.cold.1
+ _IOHIDLoadServiceFilterBundles.cold.1
+ _IOHIDLoadServicePluginBundles.cold.1
+ _IOHIDLoadSessionFilterBundles.cold.1
+ _IOHIDLog.cold.1
+ _IOHIDLogCategory.cold.2
+ _IOHIDServiceAddConnection.cold.3
+ _IOHIDServiceAddConnection.cold.4
+ _IOHIDServiceAddConnection.cold.5
+ _IOHIDServiceClientCreate.cold.1
+ _IOHIDServiceClientRefresh.cold.1
+ _IOHIDServiceCreate.cold.5
+ _IOHIDServiceRegister
+ _IOHIDServiceRemoveConnection.cold.3
+ _IOHIDServiceScheduleAsync.cold.3
+ _IOHIDSessionGetEventSystem
+ _IOHIDSessionSetPropertyForClient.cold.7
+ _MergedGlobals.65
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_30
+ __IOHIDManagerCreate_block_invoke.cold.1
+ __IOHIDQueueSetupAsyncSupport.cold.2
+ __IOHIDServiceEventCallback.cold.5
+ __IOHIDServiceInit.cold.5
+ __IOHIDServiceInit.cold.6
+ __IOHIDSessionCreate_block_invoke.cold.5
+ __IOHIDSessionDispatchEvent.cold.7
+ __IOMIGMachPortChannelCallback.cold.1
+ __IOMIGMachPortRelease.cold.2
+ __MergedGlobals
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorIN4TrieI10ExportInfoE15EntryWithOffsetEEEPS5_EclB8ne190102Ev
+ __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorIN4TrieI10ExportInfoE5EntryEEEPS5_EclB8ne190102Ev
+ __ZNKSt3__14lessINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8ne190102ERKS6_S9_
+ __ZNKSt3__16vectorIN4TrieI10ExportInfoE15EntryWithOffsetENS_9allocatorIS4_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN4TrieI10ExportInfoE5EntryENS_9allocatorIS4_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIP21macho_segment_commandI9Pointer32I12LittleEndianEENS_9allocatorIS6_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIP21macho_segment_commandI9Pointer64I12LittleEndianEENS_9allocatorIS6_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIPN4TrieI10ExportInfoE4NodeENS_9allocatorIS5_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIPhNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIPvNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIyNS_9allocatorIyEEE20__throw_length_errorB8ne190102Ev
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt3__110__pop_heapB8ne190102INS_17_ClassicAlgPolicyENS_6__lessIvvEEPN4TrieI10ExportInfoE15EntryWithOffsetEEEvT1_S9_RT0_NS_15iterator_traitsIS9_E15difference_typeE
+ __ZNSt3__110unique_ptrIN4TrieI10ExportInfoE4NodeENS_14default_deleteIS4_EEE5resetB8ne190102EPS4_
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS0_IN4TrieI10ExportInfoE4NodeENS_14default_deleteISC_EEEEEEPvEENS_22__tree_node_destructorINS6_ISI_EEEEE5resetB8ne190102EPSI_
+ __ZNSt3__111__sift_downB8ne190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN4TrieI10ExportInfoE15EntryWithOffsetEEEvT1_OT0_NS_15iterator_traitsISA_E15difference_typeESA_
+ __ZNSt3__112__destroy_atB8ne190102INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN4TrieI10ExportInfoE4NodeENS_14default_deleteISD_EEEEEELi0EEEvPT_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE16__init_with_sizeB8ne190102INS_11__wrap_iterIPKcEESA_EEvT_T0_m
+ __ZNSt3__113__tree_removeB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__114__split_bufferIN4TrieI10ExportInfoE15EntryWithOffsetERNS_9allocatorIS4_EEE5clearB8ne190102Ev
+ __ZNSt3__114__split_bufferIN4TrieI10ExportInfoE5EntryERNS_9allocatorIS4_EEE5clearB8ne190102Ev
+ __ZNSt3__116__insertion_sortB8ne190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN4TrieI10ExportInfoE15EntryWithOffsetEEEvT1_SA_T0_
+ __ZNSt3__117__floyd_sift_downB8ne190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN4TrieI10ExportInfoE15EntryWithOffsetEEET1_SA_OT0_NS_15iterator_traitsISA_E15difference_typeE
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN4TrieI10ExportInfoE15EntryWithOffsetEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN4TrieI10ExportInfoE5EntryEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP21macho_segment_commandI9Pointer32I12LittleEndianEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP21macho_segment_commandI9Pointer64I12LittleEndianEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPN4TrieI10ExportInfoE4NodeEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPhEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPvEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIyEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__partial_sort_implB8ne190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN4TrieI10ExportInfoE15EntryWithOffsetES9_EET1_SA_SA_T2_OT0_
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZNSt3__126__insertion_sort_unguardedB8ne190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN4TrieI10ExportInfoE15EntryWithOffsetEEEvT1_SA_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN4TrieI10ExportInfoE15EntryWithOffsetEEEbT1_SA_T0_
+ __ZNSt3__127__tree_balance_after_insertB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorIN4TrieI10ExportInfoE15EntryWithOffsetEEEPS6_EEED2B8ne190102Ev
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorIN4TrieI10ExportInfoE5EntryEEEPS6_EEED2B8ne190102Ev
+ __ZNSt3__131__partition_with_equals_on_leftB8ne190102INS_17_ClassicAlgPolicyEPN4TrieI10ExportInfoE15EntryWithOffsetERNS_6__lessIvvEEEET0_SA_SA_T1_
+ __ZNSt3__132__partition_with_equals_on_rightB8ne190102INS_17_ClassicAlgPolicyEPN4TrieI10ExportInfoE15EntryWithOffsetERNS_6__lessIvvEEEENS_4pairIT0_bEESB_SB_T1_
+ __ZNSt3__134__uninitialized_allocator_relocateB8ne190102INS_9allocatorIN4TrieI10ExportInfoE15EntryWithOffsetEEES5_EEvRT_PT0_SA_SA_
+ __ZNSt3__134__uninitialized_allocator_relocateB8ne190102INS_9allocatorIN4TrieI10ExportInfoE5EntryEEES5_EEvRT_PT0_SA_SA_
+ __ZNSt3__16vectorIN4TrieI10ExportInfoE15EntryWithOffsetENS_9allocatorIS4_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorIN4TrieI10ExportInfoE5EntryENS_9allocatorIS4_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorIyNS_9allocatorIyEEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorIyNS_9allocatorIyEEE16__init_with_sizeB8ne190102IPKyS6_EEvT_T0_m
+ __ZNSt3__16vectorIyNS_9allocatorIyEEE16__init_with_sizeB8ne190102IPyS5_EEvT_T0_m
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN4TrieI10ExportInfoE15EntryWithOffsetEEEjT1_SA_SA_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN4TrieI10ExportInfoE15EntryWithOffsetEEEvT1_SA_SA_SA_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN4TrieI10ExportInfoE15EntryWithOffsetEEEvT1_SA_SA_SA_SA_T0_
+ __ZNSt3__18_IterOpsINS_17_ClassicAlgPolicyEE9iter_swapB8ne190102IRPN4TrieI10ExportInfoE15EntryWithOffsetES8_EEvOT_OT0_
+ __ZNSt3__18_IterOpsINS_17_ClassicAlgPolicyEE9iter_swapB8ne190102IRPN4TrieI10ExportInfoE15EntryWithOffsetES9_EEvOT_OT0_
+ __ZNSt3__19__sift_upB8ne190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN4TrieI10ExportInfoE15EntryWithOffsetEEEvT1_SA_OT0_NS_15iterator_traitsISA_E15difference_typeE
+ __ZNSt3__19allocatorIN4TrieI10ExportInfoE15EntryWithOffsetEE7destroyB8ne190102EPS4_
+ __ZNSt3__19allocatorIN4TrieI10ExportInfoE15EntryWithOffsetEE9constructB8ne190102IS4_JRKS4_EEEvPT_DpOT0_
+ __ZNSt3__19allocatorIN4TrieI10ExportInfoE5EntryEE7destroyB8ne190102EPS4_
+ __ZNSt3__19allocatorIN4TrieI10ExportInfoE5EntryEE9constructB8ne190102IS4_JRKS4_EEEvPT_DpOT0_
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
+ ___IOHIDManagerCancel_block_invoke
+ ___vers_digit_for_char
+ _iohideventsystem_client_dispatch_notification_results.cold.1
+ _kIOHIDServiceUnregisteredKey
+ _segIdxToName
+ getPMQueue.cold.2
+ getUserActiveValidDict.cold.2
+ initialSetup.cold.9
+ setupLogging.cold.1
- GCC_except_table110
- GCC_except_table111
- GCC_except_table115
- GCC_except_table119
- GCC_except_table123
- GCC_except_table126
- GCC_except_table130
- GCC_except_table135
- GCC_except_table136
- GCC_except_table72
- GCC_except_table80
- GCC_except_table85
- GCC_except_table88
- GCC_except_table89
- GCC_except_table94
- GCC_except_table97
- IOAVPropertyListCreateWithCFProperties.arrayTypeID
- IOAVPropertyListCreateWithCFProperties.booleanTypeID
- IOAVPropertyListCreateWithCFProperties.dataTypeID
- IOAVPropertyListCreateWithCFProperties.dateTypeID
- IOAVPropertyListCreateWithCFProperties.dictionaryTypeID
- IOAVPropertyListCreateWithCFProperties.numberTypeID
- IOAVPropertyListCreateWithCFProperties.onceToken
- IOAVPropertyListCreateWithCFProperties.setTypeID
- IOAVPropertyListCreateWithCFProperties.stringTypeID
- IOHIDConnectionFilterCreate.cold.1
- IOHIDConnectionFilterCreate.cold.2
- IOHIDConnectionFilterCreate.cold.3
- IOHIDConnectionFilterCreate.cold.4
- IOHIDEventQueueCreate.cold.1
- IOHIDEventQueueCreate.cold.2
- IOHIDEventQueueCreate.cold.3
- IOHIDEventQueueCreate.cold.4
- IOHIDEventQueueCreate.cold.5
- IOHIDEventQueueCreateWithVM.cold.1
- IOHIDEventQueueCreateWithVM.cold.2
- IOHIDEventQueueDequeueCopy.cold.1
- IOHIDEventSystemConnectionDispatchEvent.cold.1
- IOHIDEventSystemCreate.cold.1
- IOHIDEventSystemOpen.cold.1
- IOHIDEventSystemOpen.cold.2
- IOHIDServiceClientCopyDescription.cold.1
- IOHIDServiceClientCopyDescription.cold.2
- IOHIDServiceClientCopyDescription.cold.3
- IOHIDServiceClientCopyDescription.cold.4
- IOHIDServiceClientCopyDescription.cold.5
- IOHIDServiceFilterCreateWithClass.cold.1
- IOHIDServiceFilterCreateWithClass.cold.2
- IOHIDServiceFilterCreateWithClass.cold.3
- IOHIDSessionFilterCreateWithClass.cold.1
- IOHIDSessionFilterCreateWithClass.cold.2
- IOHIDSessionFilterCreateWithClass.cold.3
- IOHIDUserDeviceCreateWithOptions.cold.1
- IOHIDUserDeviceCreateWithOptions.cold.2
- IOHIDUserDeviceCreateWithOptions.cold.3
- IOHIDUserDeviceCreateWithOptions.cold.4
- IOHIDVirtualServiceClientRemove.cold.1
- _IOHIDEventSystemConnectionAddServices.cold.1
- _IOHIDEventSystemConnectionFilterEvent.cold.1
- __IOHIDEventCreateWithBytesHelper.cold.1
- __IOHIDEventDataAppendEventData.cold.1
- __IOHIDEventDataAppendEventData.cold.2
- __IOHIDEventSystemClientSetupAsyncSupport.cold.1
- __IOHIDEventSystemClientSetupAsyncSupport.cold.2
- __IOHIDServiceVirtualCopyPropertyCallback.cold.1
- __IOHIDUserDeviceSetupAnalytics.keys
- __OSKextPrelinkSplitKexts.cold.1
- __OSKextPrelinkSplitKexts.cold.10
- __OSKextPrelinkSplitKexts.cold.11
- __OSKextPrelinkSplitKexts.cold.12
- __OSKextPrelinkSplitKexts.cold.13
- __OSKextPrelinkSplitKexts.cold.14
- __OSKextPrelinkSplitKexts.cold.2
- __OSKextPrelinkSplitKexts.cold.3
- __OSKextPrelinkSplitKexts.cold.4
- __OSKextPrelinkSplitKexts.cold.5
- __OSKextPrelinkSplitKexts.cold.6
- __OSKextPrelinkSplitKexts.cold.7
- __OSKextPrelinkSplitKexts.cold.8
- __OSKextPrelinkSplitKexts.cold.9
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorIN4TrieI10ExportInfoE15EntryWithOffsetEEENS_16reverse_iteratorIPS5_EEEclB8ne180100Ev
- __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorIN4TrieI10ExportInfoE5EntryEEENS_16reverse_iteratorIPS5_EEEclB8ne180100Ev
- __ZNKSt3__14lessINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8ne180100ERKS6_S9_
- __ZNKSt3__16vectorIN4TrieI10ExportInfoE15EntryWithOffsetENS_9allocatorIS4_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN4TrieI10ExportInfoE5EntryENS_9allocatorIS4_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIP21macho_segment_commandI9Pointer32I12LittleEndianEENS_9allocatorIS6_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIP21macho_segment_commandI9Pointer64I12LittleEndianEENS_9allocatorIS6_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIPN4TrieI10ExportInfoE4NodeENS_9allocatorIS5_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIPhNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIPvNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIyNS_9allocatorIyEEE20__throw_length_errorB8ne180100Ev
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt3__110__pop_heapB8ne180100INS_17_ClassicAlgPolicyENS_6__lessIvvEEPN4TrieI10ExportInfoE15EntryWithOffsetEEEvT1_S9_RT0_NS_15iterator_traitsIS9_E15difference_typeE
- __ZNSt3__110unique_ptrIN4TrieI10ExportInfoE4NodeENS_14default_deleteIS4_EEE5resetB8ne180100EPS4_
- __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS0_IN4TrieI10ExportInfoE4NodeENS_14default_deleteISC_EEEEEEPvEENS_22__tree_node_destructorINS6_ISI_EEEEE5resetB8ne180100EPSI_
- __ZNSt3__111__sift_downB8ne180100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN4TrieI10ExportInfoE15EntryWithOffsetEEEvT1_OT0_NS_15iterator_traitsISA_E15difference_typeESA_
- __ZNSt3__112__destroy_atB8ne180100INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN4TrieI10ExportInfoE4NodeENS_14default_deleteISD_EEEEEELi0EEEvPT_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE16__init_with_sizeB8ne180100INS_11__wrap_iterIPKcEESA_EEvT_T0_m
- __ZNSt3__113__tree_removeB8ne180100IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__114__split_bufferIN4TrieI10ExportInfoE15EntryWithOffsetERNS_9allocatorIS4_EEE5clearB8ne180100Ev
- __ZNSt3__114__split_bufferIN4TrieI10ExportInfoE5EntryERNS_9allocatorIS4_EEE5clearB8ne180100Ev
- __ZNSt3__116__insertion_sortB8ne180100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN4TrieI10ExportInfoE15EntryWithOffsetEEEvT1_SA_T0_
- __ZNSt3__117__floyd_sift_downB8ne180100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN4TrieI10ExportInfoE15EntryWithOffsetEEET1_SA_OT0_NS_15iterator_traitsISA_E15difference_typeE
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN4TrieI10ExportInfoE15EntryWithOffsetEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN4TrieI10ExportInfoE5EntryEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIP21macho_segment_commandI9Pointer32I12LittleEndianEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIP21macho_segment_commandI9Pointer64I12LittleEndianEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIPN4TrieI10ExportInfoE4NodeEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIPhEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIPvEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIyEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__partial_sort_implB8ne180100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN4TrieI10ExportInfoE15EntryWithOffsetES9_EET1_SA_SA_T2_OT0_
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZNSt3__126__insertion_sort_unguardedB8ne180100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN4TrieI10ExportInfoE15EntryWithOffsetEEEvT1_SA_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN4TrieI10ExportInfoE15EntryWithOffsetEEEbT1_SA_T0_
- __ZNSt3__127__tree_balance_after_insertB8ne180100IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorIN4TrieI10ExportInfoE15EntryWithOffsetEEENS_16reverse_iteratorIPS6_EEEEED2B8ne180100Ev
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorIN4TrieI10ExportInfoE5EntryEEENS_16reverse_iteratorIPS6_EEEEED2B8ne180100Ev
- __ZNSt3__131__partition_with_equals_on_leftB8ne180100INS_17_ClassicAlgPolicyEPN4TrieI10ExportInfoE15EntryWithOffsetERNS_6__lessIvvEEEET0_SA_SA_T1_
- __ZNSt3__132__partition_with_equals_on_rightB8ne180100INS_17_ClassicAlgPolicyEPN4TrieI10ExportInfoE15EntryWithOffsetERNS_6__lessIvvEEEENS_4pairIT0_bEESB_SB_T1_
- __ZNSt3__142__uninitialized_allocator_move_if_noexceptB8ne180100INS_9allocatorIN4TrieI10ExportInfoE15EntryWithOffsetEEENS_16reverse_iteratorIPS5_EES9_S9_EET2_RT_T0_T1_SA_
- __ZNSt3__142__uninitialized_allocator_move_if_noexceptB8ne180100INS_9allocatorIN4TrieI10ExportInfoE5EntryEEENS_16reverse_iteratorIPS5_EES9_S9_EET2_RT_T0_T1_SA_
- __ZNSt3__16vectorIN4TrieI10ExportInfoE15EntryWithOffsetENS_9allocatorIS4_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorIN4TrieI10ExportInfoE15EntryWithOffsetENS_9allocatorIS4_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS4_RS6_EE
- __ZNSt3__16vectorIN4TrieI10ExportInfoE5EntryENS_9allocatorIS4_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorIN4TrieI10ExportInfoE5EntryENS_9allocatorIS4_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS4_RS6_EE
- __ZNSt3__16vectorIyNS_9allocatorIyEEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorIyNS_9allocatorIyEEE16__init_with_sizeB8ne180100IPKyS6_EEvT_T0_m
- __ZNSt3__16vectorIyNS_9allocatorIyEEE16__init_with_sizeB8ne180100IPyS5_EEvT_T0_m
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN4TrieI10ExportInfoE15EntryWithOffsetEEEjT1_SA_SA_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN4TrieI10ExportInfoE15EntryWithOffsetEEEvT1_SA_SA_SA_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN4TrieI10ExportInfoE15EntryWithOffsetEEEvT1_SA_SA_SA_SA_T0_
- __ZNSt3__18_IterOpsINS_17_ClassicAlgPolicyEE9iter_swapB8ne180100IRPN4TrieI10ExportInfoE15EntryWithOffsetES8_EEvOT_OT0_
- __ZNSt3__18_IterOpsINS_17_ClassicAlgPolicyEE9iter_swapB8ne180100IRPN4TrieI10ExportInfoE15EntryWithOffsetES9_EEvOT_OT0_
- __ZNSt3__19__sift_upB8ne180100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN4TrieI10ExportInfoE15EntryWithOffsetEEEvT1_SA_OT0_NS_15iterator_traitsISA_E15difference_typeE
- __ZNSt3__19allocatorIN4TrieI10ExportInfoE15EntryWithOffsetEE7destroyB8ne180100EPS4_
- __ZNSt3__19allocatorIN4TrieI10ExportInfoE15EntryWithOffsetEE9constructB8ne180100IS4_JRKS4_EEEvPT_DpOT0_
- __ZNSt3__19allocatorIN4TrieI10ExportInfoE5EntryEE7destroyB8ne180100EPS4_
- __ZNSt3__19allocatorIN4TrieI10ExportInfoE5EntryEE9constructB8ne180100IS4_JRKS4_EEEvPT_DpOT0_
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
- ___OSKextPrelinkSplitKexts
- ___eventSytemAnalyticsEvent
- ___kIOHIDEventSystemTypeID
- ___kIOHIDUserDeviceTypeID
- __loadTCCFramework.onceToken
- __loadTCCFramework.tccFramework
- __preflightFunc
- __requestFunc
- _io_hideventsystem_create_virtual_service.cold.1
- _io_hideventsystem_dispatch_event.cold.1
- _io_hideventsystem_register_event_filter.cold.1
- _io_hideventsystem_register_record_client_changed_notification.cold.1
- _io_hideventsystem_register_record_service_changed_notification.cold.1
- _kIOHIDServiceEnumerationWorkloop
- _setKCPlkSegVMSize
- getKCPlkSegFileOff.cold.2
- getKCPlkSegNextVMAddr.cold.2
- getKCPlkSegVMAddr.cold.2
- getKCPlkSegVMSize.cold.2
- getKextVMAddr.cold.2
- setKCPlkSegVMSize.cold.1
- setKCPlkSegVMSize.cold.2
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IOAVFamily_user/IOAV.cpp"
+ "OSKEXT_BUILD_DATE 19:45:36 Mar  7 2025"
+ "Service: %@ trigger matching failed: service is already registered"
+ "Service:0x%llx  is unregistered, not matching"
+ "Unregistered"
+ "assertion failure: \"!device->cancelHandler && handler\" -> %llu"
+ "assertion failure: \"!manager->cancelHandler && handler\" -> %llu"
+ "assertion failure: \"!manager->runLoop && !manager->dispatchQueue\" -> %llu"
+ "assertion failure: \"!queue->cancelHandler && handler\" -> %llu"
+ "assertion failure: \"__IOHIDQueueSetupAsyncSupport(queue)\" -> %llu"
+ "assertion failure: \"__IOHIDUserDeviceSetupAsyncSupport(device)\" -> %llu"
+ "assertion failure: \"completionElement\" -> %llu"
+ "assertion failure: \"pthread_cond_init(&session->stateCondition, ((void*)0))\" -> %llu"
+ "assertion failure: \"pthread_mutex_init(&service->queueContext->lock, &mutexattr)\" -> %llu"
+ "assertion failure: \"pthread_mutex_init(&session->queueContext->lock, &mutexattr)\" -> %llu"
+ "assertion failure: \"pthread_mutex_lock(&(queueContext)->lock)\" -> %llu"
+ "assertion failure: \"pthread_mutex_lock(&(service->queueContext)->lock)\" -> %llu"
+ "assertion failure: \"pthread_mutex_lock(&(session->queueContext)->lock)\" -> %llu"
+ "assertion failure: \"pthread_mutex_unlock(&(queueContext)->lock)\" -> %llu"
+ "assertion failure: \"pthread_mutex_unlock(&(service->queueContext)->lock)\" -> %llu"
+ "assertion failure: \"pthread_mutex_unlock(&(session->queueContext)->lock)\" -> %llu"
+ "assertion failure: \"pthread_mutexattr_destroy(&mutexattr)\" -> %llu"
+ "assertion failure: \"pthread_mutexattr_init(&mutexattr)\" -> %llu"
+ "assertion failure: \"retainCount < (2147483647 *2U +1U)\" -> %llu"
+ "assertion failure: \"retainCount\" -> %llu"
+ "assertion failure: \"semaphore\" -> %llu"
+ "{?=\"session\"^{__IOHIDSession}\"service\"I\"serviceInterface\"^^{IOHIDServiceInterface}\"serviceInterface2\"^^{IOHIDServiceInterface2}\"plugInInterface\"^^{IOCFPlugInInterfaceStruct}\"registryID\"^{__CFNumber}\"locationID\"^v\"entitlements\"^{__CFArray}\"queueContext\"^{__IOHIDServiceQueueContext}\"dispatchQueue\"@\"NSObject<OS_dispatch_queue>\"\"notificationPort\"^{IONotificationPort}\"notification\"I\"removalNotificationSet\"^{__CFSet}\"propertyNotificationSet\"^{__CFSet}\"requestTerminationNotificationSet\"^{__CFSet}\"eventTarget\"^v\"eventRefcon\"^v\"eventCallback\"^?\"lastLEDMask\"I\"lastButtonMask\"I\"currentReportInterval\"I\"currentBatchInterval\"I\"defaultReportInterval\"I\"defaultBatchInterval\"I\"primaryUsagePage\"I\"primaryUsage\"I\"transport\"[32c]\"queueSize\"I\"containsReportInterval\"i\"state\"I\"eventCount\"I\"eventMask\"Q\"clientCacheDict\"^{__CFDictionary}\"simpleFilters\"^{__CFArray}\"filters\"^{__CFArray}\"keyboardEventInProgress\"^{__CFSet}\"nullEventMask\"Q\"displayIntegratedDigitizer\"i\"builtIn\"i\"inMomentumPhase\"i\"inDigitizerPhase\"i\"supportReportLatency\"i\"hidden\"i\"registered\"i\"protectedAccess\"i\"propertyCache\"^{__CFDictionary}\"propertyCacheHit\"I\"propertyCacheMiss\"I\"activityLastTimestamp\"Q\"virtualService\"{?=\"connection\"^v\"target\"^v\"refcon\"^v\"callbacks\"^{IOHIDServiceVirtualCallbacksV2}}\"connections\"^^v\"propertySetTime\"Q\"propertyGetTime\"Q\"elementSetTime\"Q\"regID\"Q\"eventLog\"^{__CFData}\"eventTypeCnt\"^Q\"pluginCancelHandler\"@?\"filterCancelHandler\"@?\"pendingPluginCancel\"B\"pendingFilterCancels\"I\"cancelTimer\"@\"NSObject<OS_dispatch_source>\"\"dataLock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"hidAnalyticsEvent\"^v\"hidAnalyticsDispatchEvent\"^v\"objc\"{?=\"interface\"^v\"name\"^{__CFString}\"getProperty\":\"setProperty\":\"eventMatching\":\"setEventDispatcher\":\"setCancelHandler\":\"activate\":\"cancel\":\"setDispatchQueue\":\"clientNotification\":\"copyEvent\":\"setOutputEvent\":}}"
+ "{?=\"system\"^{__IOHIDEventSystem}\"notifications\"^{__CFDictionary}\"queue\"^{__IOHIDEventQueue}\"port\"^{__IOMIGMachPort}\"reply_port\"I\"demuxCallback\"^?\"demuxRefcon\"^v\"terminationCallback\"^?\"terminationRefcon\"^v\"services\"^{__CFSet}\"pid\"i\"dispatchQueue\"@\"NSObject<OS_dispatch_queue>\"\"sendPossiblePort\"I\"sendPossibleSource\"@\"NSObject<OS_dispatch_source>\"\"replySendPossibleSource\"@\"NSObject<OS_dispatch_source>\"\"sendPossible\"i\"propertySet\"^{__CFSet}\"caller\"^{__CFString}\"procName\"^{__CFString}\"uuid\"^{__CFString}\"uuidStr\"*\"type\"i\"attributes\"^{__CFDictionary}\"task_name_port\"I\"audit_token\"{?=\"val\"[8I]}\"lock\"{os_unfair_recursive_lock_s=\"ourl_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"ourl_count\"I}\"entitlements\"^(IOHIDEventSystemConnectionEntitlements)\"connectionEntitlements\"@\"NSObject<OS_xpc_object>\"\"disableProtectedServices\"i\"filterPriority\"i\"state\"I\"notificationsLock\"{os_unfair_recursive_lock_s=\"ourl_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"ourl_count\"I}\"virtualServices\"^{__CFDictionary}\"eventFilterMask\"Q\"eventFilteredCount\"I\"eventFilterTimeoutCount\"I\"droppedEventCount\"I\"currentDroppedEventCount\"I\"droppedEventTypeMask\"Q\"eventCount\"I\"eventMask\"Q\"lastDroppedEventTime\"{timeval=\"tv_sec\"q\"tv_usec\"i}\"firstDroppedEventTime\"{timeval=\"tv_sec\"q\"tv_usec\"i}\"maxEventLatency\"Q\"droppedEventStatus\"i\"propertyChangeNotificationHandlingTime\"Q\"eventLog\"^{__CFData}\"eventTypeCnt\"^I\"activityState\"I\"activityStateChangeCount\"I\"idleNotificationTime\"Q\"activityDispatchSource\"@\"NSObject<OS_dispatch_source>\"\"activityNotification\"^{__IOHIDNotification}\"activityLog\"^{__CFData}\"filter\"^{__IOHIDConnectionFilter}\"serverDied\"i}"
- ".."
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/IOAVFamily_user/IOAV.cpp"
- "Mac"
- "OSKEXT_BUILD_DATE 20:23:13 Jan  7 2025"
- "assertion failure: \"!device->cancelHandler && handler\" -> %lld"
- "assertion failure: \"!manager->cancelHandler && handler\" -> %lld"
- "assertion failure: \"!manager->runLoop && !manager->dispatchQueue\" -> %lld"
- "assertion failure: \"!queue->cancelHandler && handler\" -> %lld"
- "assertion failure: \"__IOHIDQueueSetupAsyncSupport(queue)\" -> %lld"
- "assertion failure: \"__IOHIDUserDeviceSetupAsyncSupport(device)\" -> %lld"
- "assertion failure: \"completionElement\" -> %lld"
- "assertion failure: \"pthread_cond_init(&session->stateCondition, ((void *)0))\" -> %lld"
- "assertion failure: \"pthread_mutex_init(&service->queueContext->lock, &mutexattr)\" -> %lld"
- "assertion failure: \"pthread_mutex_init(&session->queueContext->lock, &mutexattr)\" -> %lld"
- "assertion failure: \"pthread_mutex_lock(&(queueContext)->lock)\" -> %lld"
- "assertion failure: \"pthread_mutex_lock(&(service->queueContext)->lock)\" -> %lld"
- "assertion failure: \"pthread_mutex_lock(&(session->queueContext)->lock)\" -> %lld"
- "assertion failure: \"pthread_mutex_unlock(&(queueContext)->lock)\" -> %lld"
- "assertion failure: \"pthread_mutex_unlock(&(service->queueContext)->lock)\" -> %lld"
- "assertion failure: \"pthread_mutex_unlock(&(session->queueContext)->lock)\" -> %lld"
- "assertion failure: \"pthread_mutexattr_destroy(&mutexattr)\" -> %lld"
- "assertion failure: \"pthread_mutexattr_init(&mutexattr)\" -> %lld"
- "assertion failure: \"retainCount < (2147483647 *2U +1U)\" -> %lld"
- "assertion failure: \"retainCount\" -> %lld"
- "assertion failure: \"semaphore\" -> %lld"
- "segName"
- "setKCPlkSegNextVMAddr"
- "setKCPlkSegVMSize"
- "setKextVMAddr"
- "{?=\"session\"^{__IOHIDSession}\"service\"I\"serviceInterface\"^^{IOHIDServiceInterface}\"serviceInterface2\"^^{IOHIDServiceInterface2}\"plugInInterface\"^^{IOCFPlugInInterfaceStruct}\"registryID\"^{__CFNumber}\"locationID\"^v\"entitlements\"^{__CFArray}\"queueContext\"^{__IOHIDServiceQueueContext}\"dispatchQueue\"@\"NSObject<OS_dispatch_queue>\"\"notificationPort\"^{IONotificationPort}\"notification\"I\"removalNotificationSet\"^{__CFSet}\"propertyNotificationSet\"^{__CFSet}\"requestTerminationNotificationSet\"^{__CFSet}\"eventTarget\"^v\"eventRefcon\"^v\"eventCallback\"^?\"lastLEDMask\"I\"lastButtonMask\"I\"currentReportInterval\"I\"currentBatchInterval\"I\"defaultReportInterval\"I\"defaultBatchInterval\"I\"primaryUsagePage\"I\"primaryUsage\"I\"transport\"[32c]\"queueSize\"I\"containsReportInterval\"i\"state\"I\"eventCount\"I\"eventMask\"Q\"clientCacheDict\"^{__CFDictionary}\"simpleFilters\"^{__CFArray}\"filters\"^{__CFArray}\"keyboardEventInProgress\"^{__CFSet}\"nullEventMask\"Q\"displayIntegratedDigitizer\"i\"builtIn\"i\"inMomentumPhase\"i\"inDigitizerPhase\"i\"supportReportLatency\"i\"hidden\"i\"protectedAccess\"i\"propertyCache\"^{__CFDictionary}\"propertyCacheHit\"I\"propertyCacheMiss\"I\"activityLastTimestamp\"Q\"virtualService\"{?=\"connection\"^v\"target\"^v\"refcon\"^v\"callbacks\"^{IOHIDServiceVirtualCallbacksV2}}\"connections\"^^v\"propertySetTime\"Q\"propertyGetTime\"Q\"elementSetTime\"Q\"regID\"Q\"eventLog\"^{__CFData}\"eventTypeCnt\"^Q\"pluginCancelHandler\"@?\"filterCancelHandler\"@?\"pendingPluginCancel\"B\"pendingFilterCancels\"I\"cancelTimer\"@\"NSObject<OS_dispatch_source>\"\"dataLock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"hidAnalyticsEvent\"^v\"hidAnalyticsDispatchEvent\"^v\"objc\"{?=\"interface\"^v\"name\"^{__CFString}\"getProperty\":\"setProperty\":\"eventMatching\":\"setEventDispatcher\":\"setCancelHandler\":\"activate\":\"cancel\":\"setDispatchQueue\":\"clientNotification\":\"copyEvent\":\"setOutputEvent\":}}"
- "{?=\"system\"^{__IOHIDEventSystem}\"notifications\"^{__CFDictionary}\"queue\"^{__IOHIDEventQueue}\"port\"^{__IOMIGMachPort}\"reply_port\"I\"demuxCallback\"^?\"demuxRefcon\"^v\"terminationCallback\"^?\"terminationRefcon\"^v\"services\"^{__CFSet}\"pid\"i\"dispatchQueue\"@\"NSObject<OS_dispatch_queue>\"\"sendPossiblePort\"I\"sendPossibleSource\"@\"NSObject<OS_dispatch_source>\"\"replySendPossibleSource\"@\"NSObject<OS_dispatch_source>\"\"sendPossible\"i\"propertySet\"^{__CFSet}\"caller\"^{__CFString}\"procName\"^{__CFString}\"uuid\"^{__CFString}\"uuidStr\"*\"type\"i\"attributes\"^{__CFDictionary}\"task_name_port\"I\"audit_token\"{?=\"val\"[8I]}\"lock\"{os_unfair_recursive_lock_s=\"ourl_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"ourl_count\"I}\"entitlements\"^(IOHIDEventSystemConnectionEntitlements)\"connectionEntitlements\"@\"NSObject<OS_xpc_object>\"\"disableProtectedServices\"i\"filterPriority\"i\"state\"I\"notificationsLock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"virtualServices\"^{__CFDictionary}\"eventFilterMask\"Q\"eventFilteredCount\"I\"eventFilterTimeoutCount\"I\"droppedEventCount\"I\"currentDroppedEventCount\"I\"droppedEventTypeMask\"Q\"eventCount\"I\"eventMask\"Q\"lastDroppedEventTime\"{timeval=\"tv_sec\"q\"tv_usec\"i}\"firstDroppedEventTime\"{timeval=\"tv_sec\"q\"tv_usec\"i}\"maxEventLatency\"Q\"droppedEventStatus\"i\"propertyChangeNotificationHandlingTime\"Q\"eventLog\"^{__CFData}\"eventTypeCnt\"^I\"activityState\"I\"activityStateChangeCount\"I\"idleNotificationTime\"Q\"activityDispatchSource\"@\"NSObject<OS_dispatch_source>\"\"activityNotification\"^{__IOHIDNotification}\"activityLog\"^{__CFData}\"filter\"^{__IOHIDConnectionFilter}\"serverDied\"i}"

```
