## IOGameControllerFamily

> `/System/Library/Extensions/IOGameControllerFamily.kext/IOGameControllerFamily`

```diff

-12.5.2.0.0
-  __TEXT.__cstring: 0x7e9
-  __TEXT.__const: 0x38
-  __TEXT.__os_log: 0x1085
-  __TEXT_EXEC.__text: 0x89f8
-  __TEXT_EXEC.__auth_stubs: 0x290
+13.0.28.0.0
+  __TEXT.__const: 0x460
+  __TEXT.__cstring: 0xe84
+  __TEXT.__os_log: 0x1aa8
+  __TEXT_EXEC.__text: 0x1a874
+  __TEXT_EXEC.__auth_stubs: 0x520
   __DATA.__data: 0xc8
-  __DATA.__common: 0x128
-  __DATA.__bss: 0x8
-  __DATA_CONST.__auth_got: 0x148
-  __DATA_CONST.__got: 0x78
-  __DATA_CONST.__mod_init_func: 0x30
-  __DATA_CONST.__mod_term_func: 0x30
-  __DATA_CONST.__const: 0x15f8
-  __DATA_CONST.__kalloc_type: 0x480
-  UUID: 4EA08217-55B0-38F5-97DB-AE2886B5B9EC
-  Functions: 294
-  Symbols:   705
-  CStrings:  83
+  __DATA.__common: 0x240
+  __DATA.__bss: 0x10
+  __DATA_CONST.__auth_got: 0x290
+  __DATA_CONST.__got: 0xd8
+  __DATA_CONST.__mod_init_func: 0x50
+  __DATA_CONST.__mod_term_func: 0x50
+  __DATA_CONST.__const: 0x4d30
+  __DATA_CONST.__kalloc_type: 0x7c0
+  UUID: 3C9CE710-C3DA-3AA2-AB8B-14DE9C189EDD
+  Functions: 615
+  Symbols:   830
+  CStrings:  275
 
Symbols:
+ _IOFreeData
+ _IOMallocData
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ _ZN21IOGCCircularDataQueue15initWithEntriesEjj.cold.3
+ __IOGCCircularControlQueueReadBackwardsFromLatestEnqueued_block_invoke.1
+ __IOGCCircularControlQueueReadForwardFromNextApply_block_invoke.12
+ __Z16OSUnserializeXMLPKcmPP8OSString
+ __ZL17fetchFirmwareInfoP28FirmwareInfoDataFetchContext
+ __ZL23inputDataAvailableApplyP15IORegistryEntryPv
+ __ZN11OSSerialize18binaryWithCapacityEjPvS0_
+ __ZN11OSSharedPtrI6OSDataEaSERKS1_
+ __ZN12IOHIDElement9metaClassE
+ __ZN12IOUserClient10clientDiedEv
+ __ZN12IOUserClient10getServiceEv
+ __ZN12IOUserClient12initWithTaskEP4taskPvjP12OSDictionary
+ __ZN12IOUserClient13connectClientEPS_
+ __ZN12IOUserClient20exportObjectToClientEP4taskP8OSObjectPS3_
+ __ZN12IOUserClient21copyClientEntitlementEP4taskPKc
+ __ZN12IOUserClient23getExternalTrapForIndexEj
+ __ZN12IOUserClient24getNotificationSemaphoreEjPP9semaphore
+ __ZN12IOUserClient24getTargetAndTrapForIndexEPP9IOServicej
+ __ZN12IOUserClient24registerNotificationPortEP8ipc_portjj
+ __ZN12IOUserClient24registerNotificationPortEP8ipc_portjy
+ __ZN12IOUserClient25getExternalMethodForIndexEj
+ __ZN12IOUserClient26getTargetAndMethodForIndexEPP9IOServicej
+ __ZN12IOUserClient27copyObjectForPortNameInTaskEP4taskjR11OSSharedPtrI8OSObjectE
+ __ZN12IOUserClient27copyPortNameForObjectInTaskEP4taskP8OSObjectPj
+ __ZN12IOUserClient30getExternalAsyncMethodForIndexEj
+ __ZN12IOUserClient31getAsyncTargetAndMethodForIndexEPP9IOServicej
+ __ZN12IOUserClient4initEP12OSDictionary
+ __ZN12IOUserClient4initEv
+ __ZN12IOUserClient8DispatchE5IORPC
+ __ZN12OSCollection14iterateObjectsEPvPFbS0_P8OSObjectE
+ __ZN12OSDictionary12withCapacityEj
+ __ZN12OSDictionary9metaClassE
+ __ZN12OSDictionary9setObjectEPKcRK11OSSharedPtrIK15OSMetaClassBaseE
+ __ZN13IOCommandGate14runActionBlockEU13block_pointerFivE
+ __ZN13IOHIDGCDevice25getPhysicalDeviceUniqueIDEv
+ __ZN15OSMetaClassBase16requiredMetaCastEPKS_PK11OSMetaClass
+ __ZN16IOUserClient202210gMetaClassE
+ __ZN16IOUserClient202214externalMethodEjP25IOExternalMethodArgumentsP24IOExternalMethodDispatchP8OSObjectPv
+ __ZN16IOUserClient202222dispatchExternalMethodEjP31IOExternalMethodArgumentsOpaquePK28IOExternalMethodDispatch2022mP8OSObjectPv
+ __ZN16IOUserClient2022C2EPK11OSMetaClass
+ __ZN16IOUserClient2022D2Ev
+ __ZN18IOTimerEventSource16timerEventSourceEjP8OSObjectPFvS1_PS_E
+ __ZN20OSCollectionIterator14withCollectionEPK12OSCollection
+ __ZN24IOBufferMemoryDescriptor12withCapacityEmjb
+ __ZN24IOBufferMemoryDescriptor9withBytesEPKvmjb
+ __ZN5OSSet12withCapacityEj
+ __ZN6OSData9metaClassE
+ __ZN6OSData9withBytesEPKvj
+ __ZN7OSArray12withCapacityEj
+ __ZN7OSArray13replaceObjectEjRK11OSSharedPtrIK15OSMetaClassBaseE
+ __ZN7OSArray9metaClassE
+ __ZN7OSArray9setObjectERK11OSSharedPtrIK15OSMetaClassBaseE
+ __ZN7OSArray9setObjectEjRK11OSSharedPtrIK15OSMetaClassBaseE
+ __ZN8OSNumber10withDoubleEd
+ __ZN8OSNumber10withNumberEyj
+ __ZN8OSString11withCStringEPKc
+ __ZN8OSString11withCStringEPKcm
+ __ZN8OSString17withCStringNoCopyEPKc
+ __ZN9OSBoolean9metaClassE
+ __ZNK8OSNumber11doubleValueEv
+ __ZNK9IOService10isInactiveEv
+ __ZTV16IOUserClient2022
+ __ZZL39_IOHIDDevice_getReport_completion_thunkPvS_ijE20kalloc_type_view_524
+ __ZZL39_IOHIDDevice_setReport_completion_thunkPvS_ijE20kalloc_type_view_666
+ __ZZN13IOHIDGCDevice9getReportE15IOHIDReportTypehP18IOMemoryDescriptorjP8OSObjectPvPFvS4_S5_S2_iEE20kalloc_type_view_549
+ __ZZN13IOHIDGCDevice9getReportE15IOHIDReportTypehP18IOMemoryDescriptorjP8OSObjectPvPFvS4_S5_S2_iEE20kalloc_type_view_584
+ __ZZN13IOHIDGCDevice9setReportE15IOHIDReportTypehP18IOMemoryDescriptorjP8OSObjectPvPFvS4_S5_S2_iEE20kalloc_type_view_691
+ __ZZN13IOHIDGCDevice9setReportE15IOHIDReportTypehP18IOMemoryDescriptorjP8OSObjectPvPFvS4_S5_S2_iEE20kalloc_type_view_725
+ __ZZN16IOGCCommandQueue11asyncActionEPFiP8OSObjectPvES2_NS_12AsyncOptionsEPPNS_12ContinuationEE20kalloc_type_view_213
+ __ZZN16IOGCCommandQueue12checkForWorkEvE20kalloc_type_view_137
+ __ZZN16IOGCCommandQueue16freeContinuationEPNS_12ContinuationEE20kalloc_type_view_192
+ __ZZN16IOGCCommandQueue20allocateContinuationEvE20kalloc_type_view_185
+ __ZZZL17fetchFirmwareInfoP28FirmwareInfoDataFetchContextEUb18_E11_os_log_fmt
+ __ZZZL17fetchFirmwareInfoP28FirmwareInfoDataFetchContextEUb18_E11_os_log_fmt_0
+ __ZZZL17fetchFirmwareInfoP28FirmwareInfoDataFetchContextEUb18_E11_os_log_fmt_1
+ __ZZZL33fetchNextMotionCorrectionDataPageP32MotionCorrectionDataFetchContextEUb19_E11_os_log_fmt
+ __ZZZL33fetchNextMotionCorrectionDataPageP32MotionCorrectionDataFetchContextEUb19_E11_os_log_fmt_0
+ __ZZZL33fetchNextMotionCorrectionDataPageP32MotionCorrectionDataFetchContextEUb19_E11_os_log_fmt_1
+ ___ZL17fetchFirmwareInfoP28FirmwareInfoDataFetchContext_block_invoke.cold.1
+ ___ZL33fetchNextMotionCorrectionDataPageP32MotionCorrectionDataFetchContext_block_invoke.cold.1
+ ___ZL33fetchNextMotionCorrectionDataPageP32MotionCorrectionDataFetchContext_block_invoke.cold.2
+ ____ZL17fetchFirmwareInfoP28FirmwareInfoDataFetchContext_block_invoke
+ ____ZL33fetchNextMotionCorrectionDataPageP32MotionCorrectionDataFetchContext_block_invoke
+ ___copy_helper_block_8_32b40b
+ ___copy_helper_block_8_32r
+ ___copy_helper_block_8_32r40r48r56r64r72r
+ ___copy_helper_block_8_32r40r48r56r64r72r80r
+ ___copy_helper_block_8_48c27_ZTS11OSSharedPtrI7OSArrayE
+ ___cxa_pure_virtual
+ ___destroy_helper_block_8_32b40b
+ ___destroy_helper_block_8_32r
+ ___destroy_helper_block_8_32r40r48r56r64r72r
+ ___destroy_helper_block_8_32r40r48r56r64r72r80r
+ ___destroy_helper_block_8_48c27_ZTS11OSSharedPtrI7OSArrayE
+ ___stack_chk_fail
+ ___stack_chk_guard
+ ___strncpy_chk
+ __block_descriptor_tmp.100
+ __block_descriptor_tmp.104
+ __block_descriptor_tmp.108
+ __block_descriptor_tmp.114
+ __block_descriptor_tmp.117
+ __block_descriptor_tmp.118
+ __block_descriptor_tmp.13
+ __block_descriptor_tmp.14
+ __block_descriptor_tmp.15
+ __block_descriptor_tmp.163
+ __block_descriptor_tmp.166
+ __block_descriptor_tmp.170
+ __block_descriptor_tmp.172
+ __block_descriptor_tmp.173
+ __block_descriptor_tmp.174
+ __block_descriptor_tmp.175
+ __block_descriptor_tmp.176
+ __block_descriptor_tmp.177
+ __block_descriptor_tmp.178
+ __block_descriptor_tmp.18
+ __block_descriptor_tmp.182
+ __block_descriptor_tmp.186
+ __block_descriptor_tmp.189
+ __block_descriptor_tmp.194
+ __block_descriptor_tmp.198
+ __block_descriptor_tmp.199
+ __block_descriptor_tmp.20
+ __block_descriptor_tmp.200
+ __block_descriptor_tmp.201
+ __block_descriptor_tmp.202
+ __block_descriptor_tmp.203
+ __block_descriptor_tmp.204
+ __block_descriptor_tmp.205
+ __block_descriptor_tmp.211
+ __block_descriptor_tmp.213
+ __block_descriptor_tmp.22
+ __block_descriptor_tmp.29
+ __block_descriptor_tmp.33
+ __block_descriptor_tmp.36
+ __block_descriptor_tmp.39
+ __block_descriptor_tmp.4
+ __block_descriptor_tmp.40
+ __block_descriptor_tmp.41
+ __block_descriptor_tmp.42
+ __block_descriptor_tmp.46
+ __block_descriptor_tmp.47
+ __block_descriptor_tmp.48
+ __block_descriptor_tmp.50
+ __block_descriptor_tmp.54
+ __block_descriptor_tmp.58
+ __block_descriptor_tmp.64
+ __block_descriptor_tmp.67
+ __block_descriptor_tmp.69
+ __block_descriptor_tmp.8
+ __block_descriptor_tmp.81
+ __block_descriptor_tmp.85
+ __block_descriptor_tmp.89
+ __block_descriptor_tmp.92
+ __block_descriptor_tmp.96
+ __gc_log_psvr2
+ _clock_get_uptime
+ _clock_timebase_info
+ _gIOGeneralInterest
+ _gIOServicePlane
+ _gc_log_psvr2.Log
+ _get_bsdtask_info
+ _kOSBooleanFalse
+ _kOSBooleanTrue
+ _proc_name
+ _proc_pid
+ _snprintf
+ _strnlen
- IOGCCircularControlQueueEntryCommitModifications._os_log_fmt
- IOGCCircularControlQueueEntryCommitModifications._os_log_fmt.39
- IOGCCircularControlQueueEntryCommitModifications._os_log_fmt.40
- IOGCCircularControlQueueEntryCommitModifications._os_log_fmt.41
- IOGCCircularControlQueueEntryCommitModifications._os_log_fmt.42
- IOGCCircularControlQueueEntryModify._os_log_fmt
- IOGCCircularControlQueueEntryModify._os_log_fmt.35
- IOGCCircularControlQueueEntryModify._os_log_fmt.36
- IOGCCircularControlQueueEntryModify._os_log_fmt.37
- IOGCCircularControlQueueEntryModify._os_log_fmt.38
- IOGCCircularControlQueueEntryResetModifications._os_log_fmt
- IOGCCircularControlQueueEntryResetModifications._os_log_fmt.43
- IOGCCircularControlQueueEntryResetModifications._os_log_fmt.44
- IOGCCircularControlQueueEntryResetModifications._os_log_fmt.45
- IOGCCircularControlQueueEntryResetModifications._os_log_fmt.46
- IOGCCircularControlQueueGetLastAppliedPosition._os_log_fmt
- IOGCCircularControlQueueGetLastAppliedPosition.cold.1
- IOGCCircularControlQueueGetNextApplyPosition._os_log_fmt
- IOGCCircularControlQueueGetNextApplyPosition.cold.1
- IOGCCircularControlQueueInit._os_log_fmt
- IOGCCircularControlQueueInit._os_log_fmt.3
- IOGCCircularControlQueueInit._os_log_fmt.5
- IOGCCircularControlQueueInit.cold.1
- IOGCCircularControlQueueInit.cold.2
- IOGCCircularControlQueueInit.cold.3
- IOGCCircularControlQueueReadNext._os_log_fmt
- IOGCCircularControlQueueReadNext._os_log_fmt.27
- IOGCCircularControlQueueReadNext._os_log_fmt.29
- IOGCCircularControlQueueReadNext._os_log_fmt.31
- IOGCCircularControlQueueReadNext._os_log_fmt.33
- IOGCCircularControlQueueReset._os_log_fmt
- IOGCCircularControlQueueReset.cold.1
- _IOGCCircularControlQueueValidateAndAccess._os_log_fmt
- _IOGCCircularControlQueueValidateAndAccess._os_log_fmt.47
- _IOGCCircularControlQueueValidateAndAccess._os_log_fmt.48
- _ZN12IOGCResource5startEP9IOService.cold.1
- _ZN12IOGCResource5startEP9IOService.cold.2
- _ZN13IOHIDGCDevice12openProviderEj.cold.1
- _ZN13IOHIDGCDevice16_tryOpenProviderEjy.cold.1
- _ZN13IOHIDGCDevice17handleInputReportEyjP18IOMemoryDescriptor.cold.1
- _ZN13IOHIDGCDevice24openProviderInBackgroundEv.cold.1
- _ZN13IOHIDGCDevice24openProviderInBackgroundEv.cold.2
- _ZN13IOHIDGCDevice5startEP9IOService.cold.1
- _ZN13IOHIDGCDevice5startEP9IOService.cold.2
- _ZN13IOHIDGCDevice5startEP9IOService.cold.3
- _ZN13IOHIDGCDevice5startEP9IOService.cold.4
- _ZN13IOHIDGCDevice5startEP9IOService.cold.5
- _ZN13IOHIDGCDevice5startEP9IOService.cold.6
- _ZN13IOHIDGCDevice5startEP9IOService.cold.7
- _ZN13IOHIDGCDevice9getReportE15IOHIDReportTypehP18IOMemoryDescriptorjP8OSObjectPvPFvS4_S5_S2_iE.cold.1
- _ZN13IOHIDGCDevice9getReportE15IOHIDReportTypehP18IOMemoryDescriptorjU13block_pointerFvS2_iE.cold.1
- _ZN13IOHIDGCDevice9getReportE15IOHIDReportTypehP18IOMemoryDescriptorjU13block_pointerFvS2_iE.cold.2
- _ZN13IOHIDGCDevice9setReportE15IOHIDReportTypehP18IOMemoryDescriptorjP8OSObjectPvPFvS4_S5_S2_iE.cold.1
- _ZN13IOHIDGCDevice9setReportE15IOHIDReportTypehP18IOMemoryDescriptorjU13block_pointerFvS2_iE.cold.1
- _ZN13IOHIDGCDevice9setReportE15IOHIDReportTypehP18IOMemoryDescriptorjU13block_pointerFvS2_iE.cold.2
- _ZN16IOGCCommandQueue10syncActionEPFiP8OSObjectPvES2_.cold.1
- _ZN16IOGCCommandQueue10syncActionEPFiP8OSObjectPvES2_.cold.2
- _ZN16IOGCCommandQueue11asyncActionEPFiP8OSObjectPvES2_NS_12AsyncOptionsEPPNS_12ContinuationE.cold.1
- _ZN16IOGCCommandQueue11asyncActionEPFiP8OSObjectPvES2_NS_12AsyncOptionsEPPNS_12ContinuationE.cold.2
- _ZN21IOGCCircularDataQueue7enqueueEPvj.cold.1
- _ZN27IOGCCircularDataQueueCursor4readEPvPj.cold.1
- _ZN27IOGCCircularDataQueueCursor6accessEPvS0_PFiS0_S0_S0_jE.cold.1
- __IOGCCircularControlQueueReadBackwardsFromLatestEnqueued_block_invoke.9
- __IOGCCircularControlQueueReadForwardFromNextApply_block_invoke.20
- __IOGCCircularControlQueueValidateAndAccess
- __ZZL39_IOHIDDevice_getReport_completion_thunkPvS_ijE20kalloc_type_view_506
- __ZZL39_IOHIDDevice_setReport_completion_thunkPvS_ijE20kalloc_type_view_639
- __ZZN12IOGCResource5startEP9IOServiceE11_os_log_fmt
- __ZZN12IOGCResource5startEP9IOServiceE11_os_log_fmt_0
- __ZZN13IOHIDGCDevice10getProductEvE11_os_log_fmt
- __ZZN13IOHIDGCDevice12getTransportEvE11_os_log_fmt
- __ZZN13IOHIDGCDevice12openProviderEjE11_os_log_fmt
- __ZZN13IOHIDGCDevice13closeProviderEvE11_os_log_fmt
- __ZZN13IOHIDGCDevice15getManufacturerEvE11_os_log_fmt
- __ZZN13IOHIDGCDevice15getSerialNumberEvE11_os_log_fmt
- __ZZN13IOHIDGCDevice16_tryOpenProviderEjyE11_os_log_fmt
- __ZZN13IOHIDGCDevice16_tryOpenProviderEjyE11_os_log_fmt_0
- __ZZN13IOHIDGCDevice17handleInputReportEyjP18IOMemoryDescriptorE11_os_log_fmt
- __ZZN13IOHIDGCDevice20copyProviderPropertyEPKcE11_os_log_fmt
- __ZZN13IOHIDGCDevice20copyProviderPropertyEPKcE11_os_log_fmt_0
- __ZZN13IOHIDGCDevice24openProviderInBackgroundEvE11_os_log_fmt
- __ZZN13IOHIDGCDevice24openProviderInBackgroundEvE11_os_log_fmt_0
- __ZZN13IOHIDGCDevice5startEP9IOServiceE11_os_log_fmt
- __ZZN13IOHIDGCDevice5startEP9IOServiceE11_os_log_fmt_0
- __ZZN13IOHIDGCDevice5startEP9IOServiceE11_os_log_fmt_1
- __ZZN13IOHIDGCDevice5startEP9IOServiceE11_os_log_fmt_2
- __ZZN13IOHIDGCDevice5startEP9IOServiceE11_os_log_fmt_3
- __ZZN13IOHIDGCDevice5startEP9IOServiceE11_os_log_fmt_4
- __ZZN13IOHIDGCDevice5startEP9IOServiceE11_os_log_fmt_5
- __ZZN13IOHIDGCDevice9getReportE15IOHIDReportTypehP18IOMemoryDescriptorE11_os_log_fmt
- __ZZN13IOHIDGCDevice9getReportE15IOHIDReportTypehP18IOMemoryDescriptorjP8OSObjectPvPFvS4_S5_S2_iEE11_os_log_fmt
- __ZZN13IOHIDGCDevice9getReportE15IOHIDReportTypehP18IOMemoryDescriptorjP8OSObjectPvPFvS4_S5_S2_iEE11_os_log_fmt_0
- __ZZN13IOHIDGCDevice9getReportE15IOHIDReportTypehP18IOMemoryDescriptorjP8OSObjectPvPFvS4_S5_S2_iEE11_os_log_fmt_1
- __ZZN13IOHIDGCDevice9getReportE15IOHIDReportTypehP18IOMemoryDescriptorjP8OSObjectPvPFvS4_S5_S2_iEE20kalloc_type_view_525
- __ZZN13IOHIDGCDevice9getReportE15IOHIDReportTypehP18IOMemoryDescriptorjP8OSObjectPvPFvS4_S5_S2_iEE20kalloc_type_view_560
- __ZZN13IOHIDGCDevice9getReportE15IOHIDReportTypehP18IOMemoryDescriptorjU13block_pointerFvS2_iEE11_os_log_fmt
- __ZZN13IOHIDGCDevice9getReportE15IOHIDReportTypehP18IOMemoryDescriptorjU13block_pointerFvS2_iEE11_os_log_fmt_0
- __ZZN13IOHIDGCDevice9setReportE15IOHIDReportTypehP18IOMemoryDescriptorE11_os_log_fmt
- __ZZN13IOHIDGCDevice9setReportE15IOHIDReportTypehP18IOMemoryDescriptorjP8OSObjectPvPFvS4_S5_S2_iEE11_os_log_fmt
- __ZZN13IOHIDGCDevice9setReportE15IOHIDReportTypehP18IOMemoryDescriptorjP8OSObjectPvPFvS4_S5_S2_iEE11_os_log_fmt_0
- __ZZN13IOHIDGCDevice9setReportE15IOHIDReportTypehP18IOMemoryDescriptorjP8OSObjectPvPFvS4_S5_S2_iEE11_os_log_fmt_1
- __ZZN13IOHIDGCDevice9setReportE15IOHIDReportTypehP18IOMemoryDescriptorjP8OSObjectPvPFvS4_S5_S2_iEE20kalloc_type_view_658
- __ZZN13IOHIDGCDevice9setReportE15IOHIDReportTypehP18IOMemoryDescriptorjP8OSObjectPvPFvS4_S5_S2_iEE20kalloc_type_view_692
- __ZZN13IOHIDGCDevice9setReportE15IOHIDReportTypehP18IOMemoryDescriptorjU13block_pointerFvS2_iEE11_os_log_fmt
- __ZZN13IOHIDGCDevice9setReportE15IOHIDReportTypehP18IOMemoryDescriptorjU13block_pointerFvS2_iEE11_os_log_fmt_0
- __ZZN16IOGCCommandQueue10syncActionEPFiP8OSObjectPvES2_E11_os_log_fmt
- __ZZN16IOGCCommandQueue10syncActionEPFiP8OSObjectPvES2_E11_os_log_fmt_0
- __ZZN16IOGCCommandQueue11asyncActionEPFiP8OSObjectPvES2_NS_12AsyncOptionsEPPNS_12ContinuationEE11_os_log_fmt
- __ZZN16IOGCCommandQueue11asyncActionEPFiP8OSObjectPvES2_NS_12AsyncOptionsEPPNS_12ContinuationEE11_os_log_fmt_0
- __ZZN16IOGCCommandQueue11asyncActionEPFiP8OSObjectPvES2_NS_12AsyncOptionsEPPNS_12ContinuationEE11_os_log_fmt_1
- __ZZN16IOGCCommandQueue11asyncActionEPFiP8OSObjectPvES2_NS_12AsyncOptionsEPPNS_12ContinuationEE20kalloc_type_view_199
- __ZZN16IOGCCommandQueue12checkForWorkEvE11_os_log_fmt
- __ZZN16IOGCCommandQueue12checkForWorkEvE20kalloc_type_view_130
- __ZZN16IOGCCommandQueue16freeContinuationEPNS_12ContinuationEE20kalloc_type_view_185
- __ZZN16IOGCCommandQueue20allocateContinuationEvE20kalloc_type_view_178
- __ZZN21IOGCCircularDataQueue15initWithEntriesEjjE11_os_log_fmt_2
- __ZZN21IOGCCircularDataQueue7enqueueEPvjE11_os_log_fmt
- __ZZN24IOGCCircularControlQueue15initWithEntriesEjjE11_os_log_fmt_0
- __ZZN27IOGCCircularDataQueueCursor4readEPvPjE11_os_log_fmt
- __ZZN27IOGCCircularDataQueueCursor6accessEPvS0_PFiS0_S0_S0_jEE11_os_log_fmt
- __block_descriptor_tmp.12
- __block_descriptor_tmp.16
- __block_descriptor_tmp.19
- __block_descriptor_tmp.51
- _block_invoke._os_log_fmt.49
CStrings:
+ " (bad CRC)"
+ " (skipped CRC)"
+ "%#0.2x"
+ "%#0.4x"
+ "%#0.8x"
+ "12111112122212121111"
+ "121111121222121211111"
+ "12111112122212121111111111111"
+ "121111121222121211111111111112"
+ "121111121222121211111122111112221112111211111211212"
+ "12112222212111"
+ "12222222222222212111"
+ "B36@?0Q8B16^v20Q28"
+ "B8@?0"
+ "BT"
+ "Bluetooth"
+ "Built-In"
+ "Could not unserialize input arguments!"
+ "DeviceUsage"
+ "DeviceUsagePage"
+ "DeviceUsagePairs"
+ "HI"
+ "HIDVirtualDevice"
+ "HasDeviceSequenceIdentifiers"
+ "IOUserClientDefaultLocking"
+ "IOUserClientDefaultLockingSetProperties"
+ "IOUserClientDefaultLockingSingleThreadExternalMethod"
+ "IOUserClientEntitlements"
+ "Input.NormalizedThumbstickAxisSnapRadius"
+ "Input.NormalizedThumbstickDeadzoneRadius"
+ "Input.NormalizedTriggerDeadzone"
+ "InputReportElements"
+ "LED"
+ "LED~Override"
+ "MV"
+ "PSVR2"
+ "PSVR2Connection"
+ "PSVR2DeviceType"
+ "PSVR2HeldInHand"
+ "PSVR2SenseDevice"
+ "PSVR2SenseDeviceFastPathUserClient"
+ "PSVR2SenseDeviceFastPathUserClientHapticsQueue"
+ "PSVR2SenseDeviceFastPathUserClientInputQueue"
+ "PSVR2SenseDeviceFastPathUserClientQueue"
+ "PSVR2SenseDeviceFastPathUserClientTrackingQueue"
+ "PSVR2SenseDeviceHIDEventServerUserClient"
+ "PhysicalDeviceUniqueID"
+ "Power.Disconnect.OnBattery.AtLevel"
+ "Power.Disconnect.OnBattery.AtLowVoltage"
+ "Power.Disconnect.OnBattery.NotHeldAfterTime"
+ "PrimaryUsage"
+ "PrimaryUsagePage"
+ "QueueCapacity"
+ "QueueChannel"
+ "QueueEntrySize"
+ "QueueGuard"
+ "QueueID"
+ "QueueMemorySize"
+ "ReportInterval"
+ "ReportInterval~Latest"
+ "ReportInterval~Override"
+ "SS"
+ "Sense Left"
+ "Sense Right"
+ "TimeSyncEnabled"
+ "Transport.ReportInterval"
+ "Transport.ReportInterval~Latest"
+ "Transport.ReportInterval~Override"
+ "Transport.TimeSynchronization"
+ "Transport.TimeSynchronization~Latest"
+ "Transport.TimeSynchronization~Override"
+ "UC"
+ "USB"
+ "UV"
+ "UniformTypeIdentifiers"
+ "Unknown"
+ "[%#010llx] #DENY openHapticsControl(<IOService %#010llx>).  Currently open by other client %#010llx."
+ "[%#010llx] #DENY openTrackingControl(<IOService %#010llx>).  Currently open by other client %#010llx."
+ "[%#010llx] #INPUT Queue Enqueue failed"
+ "[%#010llx] #INPUT Queue Reset -> %llu"
+ "[%#010llx] #INPUT Queue Reset failed: %x"
+ "[%#010llx] #POWER 'Controller not held' time meets BATTERY disconnect criteria {\n\t now = %llums\n\t last held in hand update = %llums\n\t should disconnect after = %ums\n}"
+ "[%#010llx] #POWER Battery level %d meets BATTERY disconnect criteria."
+ "[%#010llx] #POWER Battery low voltage meets BATTERY disconnect criteria."
+ "[%#010llx] #POWER Notifying clients that 'should disconnect' state changed %#x -> %#x"
+ "[%#010llx] Apply 'Input' configuration {\n\tInput.NormalizedThumbstickAxisSnapRadius = %f\n}"
+ "[%#010llx] Apply 'Input' configuration {\n\tInput.NormalizedThumbstickAxisSnapRadius = ERROR, expected number value!\n}"
+ "[%#010llx] Apply 'Input' configuration {\n\tInput.NormalizedThumbstickDeadzoneRadius = %f\n}"
+ "[%#010llx] Apply 'Input' configuration {\n\tInput.NormalizedThumbstickDeadzoneRadius = ERROR, expected number value!\n}"
+ "[%#010llx] Apply 'Input' configuration {\n\tInput.NormalizedTriggerDeadzone = %f\n}"
+ "[%#010llx] Apply 'Input' configuration {\n\tInput.NormalizedTriggerDeadzone = ERROR, expected number value!\n}"
+ "[%#010llx] Apply 'Power' configuration {\n\tPower.Disconnect.OnBattery.AtLevel = %hhu\n}"
+ "[%#010llx] Apply 'Power' configuration {\n\tPower.Disconnect.OnBattery.AtLowVoltage = %d\n}"
+ "[%#010llx] Apply 'Power' configuration {\n\tPower.Disconnect.OnBattery.NotHeldAfterTime = %u\n}"
+ "[%#010llx] Clear 'PSVR2HeldInHand'"
+ "[%#010llx] Could not determine connection type!"
+ "[%#010llx] Could not determine device type!"
+ "[%#010llx] Create control queue (%llx): Not permitted"
+ "[%#010llx] ERROR: Refresh accessory firmware info failed (Attempt 2/2): %#x"
+ "[%#010llx] ERROR: Refresh accessory motion correction data failed (Attempt 2/2): %#x"
+ "[%#010llx] Fetch accessory firmware info  (g: %llu a:%u) failed: invalid checksum"
+ "[%#010llx] Fetch accessory firmware info (g: %llu a:%u) failed: %#x"
+ "[%#010llx] Fetch accessory firmware info (g: %llu a:%u) failed: %#x (will retry)"
+ "[%#010llx] Fetch motion correction data (g: %llu a:%u p:%u) failed: %#x"
+ "[%#010llx] Fetch motion correction data (g: %llu a:%u p:%u) failed: %#x (will retry)"
+ "[%#010llx] Fetch motion correction data (g: %llu a:%u p:%u) failed: invalid checksum."
+ "[%#010llx] Get feature report %#0.2x #NOTE: Response [%#0.2x] (%zu bytes) has invalid checksum '%#0.8x'; expected '%#0.8x'."
+ "[%#010llx] Get feature report %#0.2x error: Could not map response."
+ "[%#010llx] Get feature report %#0.2x error: Response [%#0.2x] has length %{bytes}zu.  Expected at least %zu bytes."
+ "[%#010llx] Get feature report %#0.2x error: Response [%#0.2x] is too short. Expected at least %zu bytes."
+ "[%#010llx] Get feature report %#0.2x error: Response has length %{bytes}zu, which is abnormally large."
+ "[%#010llx] Get feature report %#0.2x error: Response is empty. Expected at least %zu bytes."
+ "[%#010llx] Get feature report %#0.2x failed: %#x"
+ "[%#010llx] Get feature report %#0.2x: [%#0.2x] | %#0.8x%{public}s (%zu bytes)"
+ "[%#010llx] Get feature report %#0.2x: [%#0.2x] | (%zu bytes)"
+ "[%#010llx] Missing motion correction data page %u."
+ "[%#010llx] Missing motion correction data pages."
+ "[%#010llx] Missing one or more motion correction data pages after %u."
+ "[%#010llx] Missing some motion correction data pages."
+ "[%#010llx] Motion correction data page out of order."
+ "[%#010llx] PSVR2SenseDevice::closeHapticsControl(<IOService %#010llx>)"
+ "[%#010llx] PSVR2SenseDevice::closeTrackingControl(<IOService %#010llx>)"
+ "[%#010llx] PSVR2SenseDevice::didTerminate(<IOHIDInterface %#010llx>)"
+ "[%#010llx] PSVR2SenseDevice::handleProviderClosed(%llu)"
+ "[%#010llx] PSVR2SenseDevice::handleProviderOpened(%llu)"
+ "[%#010llx] PSVR2SenseDevice::handleStart(<IOHIDInterface %#010llx>)"
+ "[%#010llx] PSVR2SenseDevice::handleStop(<IOHIDInterface %#010llx>)"
+ "[%#010llx] PSVR2SenseDevice::openHapticsControl(<IOService %#010llx>)"
+ "[%#010llx] PSVR2SenseDevice::openTrackingControl(<IOService %#010llx>)"
+ "[%#010llx] PSVR2SenseDeviceFastPathUserClient::start(<PSVR2SenseDevice %#010llx>) for pid %i, %s"
+ "[%#010llx] PSVR2SenseDeviceFastPathUserClientHapticsQueue::start(<IOService %#010llx>)"
+ "[%#010llx] PSVR2SenseDeviceFastPathUserClientHapticsQueue::stop(<IOService %#010llx>)"
+ "[%#010llx] PSVR2SenseDeviceFastPathUserClientInputQueue::start(<IOService %#010llx>)"
+ "[%#010llx] PSVR2SenseDeviceFastPathUserClientInputQueue::stop(<IOService %#010llx>)"
+ "[%#010llx] PSVR2SenseDeviceFastPathUserClientTrackingQueue::start(<IOService %#010llx>)"
+ "[%#010llx] PSVR2SenseDeviceFastPathUserClientTrackingQueue::stop(<IOService %#010llx>)"
+ "[%#010llx] Payload for input report [%#x] has length [%{bytes}zu], which is less than the minimum expected length [%{bytes}zu]. Ignoring."
+ "[%#010llx] Received unknown input report: reportID = %#lx"
+ "[%#010llx] Refresh accessory firmware info completed with status (Attempt 1/2): %#x"
+ "[%#010llx] Refresh accessory firmware info completed with status (Attempt 2/2): %#x"
+ "[%#010llx] Refresh accessory motion correction data completed with status (Attempt 1/2): %#x"
+ "[%#010llx] Refresh accessory motion correction data completed with status (Attempt 2/2): %#x"
+ "[%#010llx] Registering service with IOKit..."
+ "[%#010llx] Request Firmware Info failed: %#x"
+ "[%#010llx] Request Motion Correction Data failed: %#x"
+ "[%#010llx] Set 'PSVR2HeldInHand': Not permitted"
+ "[%#010llx] Set feature report %#0.2x failed: %#x"
+ "[%#010llx] Set feature report %#0.2x | %{private}.*P"
+ "[%#010llx] Set feature report %#0.2x | %{private}.*P | %{public}.*P%{public}s"
+ "[%#010llx] Set output report %#0.2x failed: %#x"
+ "[%#010llx] Started PSVR2 %s {\n    isVirtual = %d\n    isProxied = %d\n    transport = %d\n    connection = %d\n    reportInterval = %uus\n}"
+ "[%#010llx] WARNING: Refresh accessory firmware info failed (Attempt 1/2): %#x"
+ "[%#010llx] WARNING: Refresh accessory motion correction data failed (Attempt 1/2): %#x"
+ "[%#010llx] [!] Refresh accessory info failed: %#x. The service will not be registered.  Disconnect and reconnect the accessory."
+ "[%#010llx] openHapticsControl(<PSVR2SenseDevice %#010llx>) denied: %x."
+ "[%#010llx] openTrackingControl(<PSVR2SenseDevice %#010llx>) denied: %x."
+ "_1"
+ "_10"
+ "_11"
+ "_12"
+ "_13"
+ "_14"
+ "_15"
+ "_16"
+ "_17"
+ "_18"
+ "_19"
+ "_2"
+ "_20"
+ "_21"
+ "_22"
+ "_23"
+ "_24"
+ "_25"
+ "_26"
+ "_27"
+ "_28"
+ "_29"
+ "_3"
+ "_30"
+ "_31"
+ "_32"
+ "_33"
+ "_34"
+ "_35"
+ "_36"
+ "_37"
+ "_38"
+ "_39"
+ "_4"
+ "_40"
+ "_41"
+ "_42"
+ "_43"
+ "_5"
+ "_6"
+ "_7"
+ "_8"
+ "_9"
+ "_PSVR2FirmwareInfo"
+ "_PSVR2MotionCalibrationInfo"
+ "application-identifier"
+ "com.apple.arkitd"
+ "com.apple.arkitd-objecttracking"
+ "com.apple.gamecontroller.driver"
+ "com.apple.iohideventsystem.server"
+ "com.sony.playstation.vr2-sense"
+ "com.sony.playstation.vr2-sense.left"
+ "com.sony.playstation.vr2-sense.right"
+ "i16@?0@?<v@?i^{?=[11c][8c]SSII[12C]SC[1C]b1b7[11C]}{CRCResult=BII}>8"
+ "i16@?0@?<v@?i^{?=b7b1(?=[58C][29C]{?=sssssssssssssssssssssssssssss}{?=sssssssssssss})}{CRCResult=BII}>8"
+ "i8@?0"
+ "site.FirmwareInfoDataFetchContext"
+ "site.MotionCorrectionDataFetchContext"
+ "site.PSVR2SenseDevice"
+ "site.PSVR2SenseDeviceFastPathUserClient"
+ "site.PSVR2SenseDeviceFastPathUserClientHapticsQueue"
+ "site.PSVR2SenseDeviceFastPathUserClientInputQueue"
+ "site.PSVR2SenseDeviceFastPathUserClientQueue"
+ "site.PSVR2SenseDeviceFastPathUserClientTrackingQueue"
+ "site.PSVR2SenseDeviceHIDEventServerUserClient"
+ "v12@?0B8"
+ "v12@?0i8"
+ "v20@?0^v8i16"
+ "v32@?0i8r^{?=[11c][8c]SSII[12C]SC[1C]b1b7[11C]}12{CRCResult=BII}20"
+ "v32@?0i8r^{?=b7b1(?=[58C][29C]{?=sssssssssssssssssssssssssssss}{?=sssssssssssss})}12{CRCResult=BII}20"
+ "v40@?0i8r^v12Q20{CRCResult=BII}28"
+ "v8@?0"
- "/Library/Caches/com.apple.xbs/Sources/CoreController_kext/IOGameControllerFamily/IOGCResource.cpp"
- "/Library/Caches/com.apple.xbs/Sources/CoreController_kext/IOGameControllerFamily/Service/IOHIDGCDevice.cpp"
- "/Library/Caches/com.apple.xbs/Sources/CoreController_kext/IOGameControllerFamily/Utility/ControlQueue/IOGCCircularControlQueueMemory.c"
- "/Library/Caches/com.apple.xbs/Sources/CoreController_kext/IOGameControllerFamily/Utility/DataQueue/IOGCCircularDataQueue.cpp"
- "/Library/Caches/com.apple.xbs/Sources/CoreController_kext/IOGameControllerFamily/Utility/IOGCCommandQueue.cpp"
- "::asyncAction() Signal Work Available"
- "::checkForWork() -> %{bool}d"
- "::initWithEntries failed: invalid entry data size [%u]."
- "AssertMacros: %s, %s file: %s, line: %d, value: %ld\n"
- "IOGCCircularDataQueue::initWithEntries -> queueSize:%#x entryDataSize:%u"
- "IOService::start(provider)"
- "_commandGate"
- "_device"
- "_interface"
- "_pendingOpenProviderThread"
- "_workLoop"
- "_workLoop->addEventSource(_commandGate.get()) == 0 "
- "action"
- "asyncContinuation"
- "continuation"
- "device"
- "entry"
- "entry->sentinel == queueGuard"
- "entryDataSize == queue->shadow.entryDataSize"
- "handleStart(_interface.get())"
- "heapCompletion"
- "interface"
- "lockForArbitration(false)"
- "queueGuard == queue->shadow.sentinel"
- "queueMemory->entryDataSize == entryDataSize"
- "queueMemory->memorySize == memorySize"
- "queueMemory->sentinel == sentinel"
- "queueMemorySize == queue->shadow.memorySize"
- "reportMap"
- "ret == 0 "
- "workLoop"

```
