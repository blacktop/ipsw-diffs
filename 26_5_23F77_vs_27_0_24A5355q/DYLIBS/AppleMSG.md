## AppleMSG

> `/System/Library/PrivateFrameworks/AppleMSG.framework/AppleMSG`

```diff

-101.0.24.0.0
-  __TEXT.__text: 0x10620
-  __TEXT.__auth_stubs: 0x360
-  __TEXT.__const: 0xd8
-  __TEXT.__oslogstring: 0xb7c
-  __TEXT.__cstring: 0x1f18
-  __TEXT.__gcc_except_tab: 0x104
-  __TEXT.__unwind_info: 0x3e8
-  __DATA_CONST.__got: 0x50
-  __DATA_CONST.__const: 0x70
-  __AUTH_CONST.__auth_got: 0x1b8
+418.0.0.0.1
+  __TEXT.__text: 0x142e0
+  __TEXT.__const: 0x158
+  __TEXT.__oslogstring: 0x1eda
+  __TEXT.__cstring: 0x2049
+  __TEXT.__gcc_except_tab: 0x158
+  __TEXT.__unwind_info: 0x488
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__const: 0x80
+  __DATA_CONST.__weak_got: 0x10
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x1c0
-  __AUTH_CONST.__cfstring: 0x40
-  __DATA.__common: 0x18
+  __AUTH_CONST.__cfstring: 0x80
+  __AUTH_CONST.__weak_auth_got: 0x30
+  __AUTH_CONST.__auth_got: 0x1f0
+  __DATA.__common: 0x10
+  __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: E08A8A1D-0CDA-3C55-8F9B-C7C554D4E0EC
-  Functions: 483
-  Symbols:   923
-  CStrings:  242
+  UUID: 3425AA68-6A2A-3490-A0A4-0EBD656F3BE3
+  Functions: 574
+  Symbols:   1109
+  CStrings:  357
 
Symbols:
+ GCC_except_table14
+ GCC_except_table3
+ _CFDataGetBytePtr
+ _CFDataGetLength
+ _IOConnectMapMemory
+ _IORegistryEntrySearchCFProperty
+ _IOServiceGetMatchingServices
+ _MSGClearEventTriggerInterruptStatus.cold.2
+ _MSGCreate.cold.5
+ _MSGDeinitializeDeviceHandle
+ _MSGDeinitializeDeviceHandle.cold.1
+ _MSGDeinitializeHubHandle
+ _MSGDeinitializeHubHandle.cold.1
+ _MSGDeviceInfoGetName
+ _MSGDeviceInfoIsDefault
+ _MSGEnableEventTriggerInterrupt.cold.2
+ _MSGEventTriggerLookupResultGetDeviceName
+ _MSGEventTriggerLookupResultGetEventTriggerID
+ _MSGFreeDeviceList
+ _MSGFreeEventTriggerLookupResults
+ _MSGFreeSyncLookupResults
+ _MSGGetCurrentSyncTiming.cold.4
+ _MSGGetDevices
+ _MSGGetDevices.cold.1
+ _MSGGetDevices.cold.2
+ _MSGGetDevices.cold.3
+ _MSGGetDevices.cold.4
+ _MSGGetEventTriggerConfig.cold.2
+ _MSGGetEventTriggerCount.cold.2
+ _MSGGetEventTriggerInterruptEnable.cold.2
+ _MSGGetEventTriggerInterruptStatus.cold.2
+ _MSGGetFutureSyncTiming.cold.4
+ _MSGGetSystemState.cold.1
+ _MSGGetSystemState.cold.2
+ _MSGHubConfigure
+ _MSGHubConfigure.cold.1
+ _MSGHubConfigure.cold.2
+ _MSGHubGetConfiguration
+ _MSGHubGetConfiguration.cold.1
+ _MSGHubGetConfiguration.cold.2
+ _MSGHubGetConfiguration.cold.3
+ _MSGHubGetConfiguration.cold.4
+ _MSGHubReset
+ _MSGHubReset.cold.1
+ _MSGHubReset.cold.2
+ _MSGInitializeDeviceHandle
+ _MSGInitializeDeviceHandle.cold.1
+ _MSGInitializeDeviceHandle.cold.2
+ _MSGInitializeDeviceHandle.cold.3
+ _MSGInitializeEventTriggerHandle
+ _MSGInitializeEventTriggerHandle.cold.1
+ _MSGInitializeHubHandle
+ _MSGInitializeHubHandle.cold.1
+ _MSGInitializeSyncHandle
+ _MSGInitializeSyncHandle.cold.1
+ _MSGLookupEventTriggerNamesBatch
+ _MSGLookupEventTriggerNamesBatch.cold.1
+ _MSGLookupEventTriggerNamesBatch.cold.2
+ _MSGLookupEventTriggerNamesBatch.cold.3
+ _MSGLookupEventTriggerNamesBatch.cold.4
+ _MSGLookupEventTriggerNamesBatch.cold.5
+ _MSGLookupEventTriggerNamesBatch.cold.6
+ _MSGLookupEventTriggerNamesBatch.cold.7
+ _MSGLookupSyncNamesBatch
+ _MSGLookupSyncNamesBatch.cold.1
+ _MSGLookupSyncNamesBatch.cold.2
+ _MSGLookupSyncNamesBatch.cold.3
+ _MSGLookupSyncNamesBatch.cold.4
+ _MSGLookupSyncNamesBatch.cold.5
+ _MSGLookupSyncNamesBatch.cold.6
+ _MSGLookupSyncNamesBatch.cold.7
+ _MSGRegisterForEventTriggerTiming.cold.2
+ _MSGRegisterForSyncTiming.cold.3
+ _MSGSetEventTriggerConfig.cold.2
+ _MSGSyncLookupResultGetDeviceName
+ _MSGSyncLookupResultGetSyncID
+ _MSGUnregisterFromEventTriggerTiming.cold.2
+ _MSGUnregisterFromSyncTiming.cold.3
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ __Z27SyncComputeNextMSGPulseTimeN8AppleMSG16frame_duration_tENS_15msg_timer_sel_tEyyyPyS2_b
+ __ZL13allocateMutexv
+ __ZN13MSGController13getMSGDevicesEP20applemsg_device_infojPj
+ __ZN13MSGController13getMSGDevicesEP20applemsg_device_infojPj.cold.1
+ __ZN13MSGController14SetEnqueueModeEb.cold.1
+ __ZN13MSGController15lookupSyncNamesER22msg_lookup_names_inputR28msg_lookup_sync_names_output
+ __ZN13MSGController15lookupSyncNamesER22msg_lookup_names_inputR28msg_lookup_sync_names_output.cold.1
+ __ZN13MSGController17ExecuteTransitionEN8AppleMSG15transition_id_tE
+ __ZN13MSGController17ExecuteTransitionEN8AppleMSG15transition_id_tE.cold.1
+ __ZN13MSGController17ExecuteTransitionEN8AppleMSG15transition_id_tE.cold.2
+ __ZN13MSGController17extractDeviceInfoEjR20applemsg_device_info
+ __ZN13MSGController19EnumerateMSGDevicesEP20applemsg_device_infojPj
+ __ZN13MSGController19EnumerateMSGDevicesEP20applemsg_device_infojPj.cold.1
+ __ZN13MSGController19EnumerateMSGDevicesEP20applemsg_device_infojPj.cold.2
+ __ZN13MSGController19EnumerateMSGDevicesEP20applemsg_device_infojPj.cold.3
+ __ZN13MSGController19openMatchingServiceEjRjS0_
+ __ZN13MSGController19openMatchingServiceEjRjS0_.cold.1
+ __ZN13MSGController20_openServiceInternalEPKcP16dispatch_queue_syRjS4_.cold.7
+ __ZN13MSGController20_openServiceInternalEPKcP16dispatch_queue_syRjS4_.cold.8
+ __ZN13MSGController23getTransitionIdFromNameERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
+ __ZN13MSGController23lookupEventTriggerNamesER22msg_lookup_names_inputR37msg_lookup_event_trigger_names_output
+ __ZN13MSGController23lookupEventTriggerNamesER22msg_lookup_names_inputR37msg_lookup_event_trigger_names_output.cold.1
+ __ZN13MSGController25mapTimingInfoSharedMemoryEjPPvPj
+ __ZN13MSGController26mapMSGRegistersToUserspaceEPPvPm
+ __ZN13MSGController30unmapMSGRegistersFromUserspaceEPvm
+ __ZN13MSGControllerC1EPKcb
+ __ZN13MSGControllerC2EPKcb
+ __ZN13MSGControllerC2EPKcb.cold.1
+ __ZN16MSGHubController11openServiceEv
+ __ZN16MSGHubController11openServiceEv.cold.1
+ __ZN16MSGHubController11openServiceEv.cold.2
+ __ZN16MSGHubController12closeServiceEv
+ __ZN16MSGHubController16GetConfigurationERhS0_
+ __ZN16MSGHubController16GetConfigurationERhS0_.cold.1
+ __ZN16MSGHubController5ResetEv
+ __ZN16MSGHubController5ResetEv.cold.1
+ __ZN16MSGHubController9ConfigureEaa
+ __ZN16MSGHubController9ConfigureEaa.cold.1
+ __ZN16MSGHubControllerC1Ev
+ __ZN16MSGHubControllerC2Ev
+ __ZN16MSGHubControllerC2Ev.cold.1
+ __ZN16MSGHubControllerD1Ev
+ __ZN16MSGHubControllerD2Ev
+ __ZNKSt3__114default_deleteI34msg_local_timing_info_subscriptionEclB9fqe220100EPS1_
+ __ZNSt12length_errorC1B9fqe220100EPKc
+ __ZNSt16invalid_argumentC1B9fqe220100EPKc
+ __ZNSt3__111__call_onceERVmPvPFvS2_E
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9fqe220100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE22__init_internal_bufferB9fqe220100Em
+ __ZNSt3__117__call_once_proxyB9fqe220100INS_5tupleIJRFvvEEEEEEvPv
+ __ZNSt3__120__throw_length_errorB9fqe220100EPKc
+ __ZSt7nothrow
+ __ZTISt9bad_alloc
+ __ZnamRKSt9nothrow_t
+ ___cxa_end_catch
+ ___error
+ _kCFAllocatorDefault
+ _munmap
+ _mutexFlag
+ _printf
+ _strlcpy
+ _strncmp
+ _strncpy
- GCC_except_table11
- GCC_except_table12
- GCC_except_table13
- GCC_except_table8
- _MSGAllocateEventTriggerHandle.cold.1
- _MSGAllocateSyncHandle.cold.1
- __Z23SyncComputeMSGPulseTimeN8AppleMSG16frame_duration_tENS_15msg_timer_sel_tENS_20sync_tracking_info_tEtPy.cold.1
- __Z23SyncComputeMSGPulseTimeN8AppleMSG16frame_duration_tENS_15msg_timer_sel_tENS_20sync_tracking_info_tEtPy.cold.2
- __Z23SyncComputeMSGPulseTimeN8AppleMSG16frame_duration_tENS_15msg_timer_sel_tENS_20sync_tracking_info_tEtPy.cold.3
- __Z27SyncComputeNextMSGPulseTimeN8AppleMSG16frame_duration_tENS_15msg_timer_sel_tEyyyPyS2_
- __Z27SyncComputeNextMSGPulseTimeN8AppleMSG16frame_duration_tENS_15msg_timer_sel_tEyyyPyS2_.cold.1
- __Z27SyncComputeNextMSGPulseTimeN8AppleMSG16frame_duration_tENS_15msg_timer_sel_tEyyyPyS2_.cold.2
- __Z27SyncComputeNextMSGPulseTimeN8AppleMSG16frame_duration_tENS_15msg_timer_sel_tEyyyPyS2_.cold.3
- __Z27SyncComputeNextMSGPulseTimeN8AppleMSG16frame_duration_tENS_15msg_timer_sel_tEyyyPyS2_.cold.4
- __ZN13MSGController22serviceMatchedCallbackEPvj.cold.1
- __ZN18RingBufferW1Reader12jumpToLatestEb.cold.1
- __ZN18RingBufferW1Reader4initEPhj.cold.1
- __ZN18RingBufferW1Reader4initEPhj.cold.2
- __ZN18RingBufferW1Reader8readNextEPhPt.cold.1
- __ZN18RingBufferW1Reader8readNextEPhPt.cold.10
- __ZN18RingBufferW1Reader8readNextEPhPt.cold.11
- __ZN18RingBufferW1Reader8readNextEPhPt.cold.2
- __ZN18RingBufferW1Reader8readNextEPhPt.cold.3
- __ZN18RingBufferW1Reader8readNextEPhPt.cold.4
- __ZN18RingBufferW1Reader8readNextEPhPt.cold.5
- __ZN18RingBufferW1Reader8readNextEPhPt.cold.6
- __ZN18RingBufferW1Reader8readNextEPhPt.cold.7
- __ZN18RingBufferW1Reader8readNextEPhPt.cold.8
- __ZN18RingBufferW1Reader8readNextEPhPt.cold.9
- __ZN18RingBufferW1Writer4initEPhjt.cold.1
- __ZN18RingBufferW1Writer4initEPhjt.cold.2
- __ZN18RingBufferW1Writer4initEPhjt.cold.3
- __ZN18RingBufferW1Writer5writeEPht.cold.1
- __ZN18RingBufferW1Writer5writeEPht.cold.2
- __ZN8AppleMSG16MSGTriggerToCStrENS_13msg_trigger_tE
- __ZNKSt3__114default_deleteI36msg_local_timing_info_subscription_tEclB9nqe210106EPS1_
- __ZNSt12length_errorC1B9nqe210106EPKc
- __ZNSt16invalid_argumentC1B9nqe210106EPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9nqe210106ILi0EEEPKc
- __ZNSt3__120__throw_length_errorB9nqe210106EPKc
- _memmove
CStrings:
+ "!internalSyncHandle->remote"
+ "((maxDeviceCount > 0) && (maxDeviceCount <= MSG_MAX_DEVICE_COUNT))"
+ "(internalSyncHandle->id == 0)"
+ "(isRequestingDefault || isRequestingRemote)"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleMSG/MSGClientAPI/MSGHubClientAPI.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleMSG/MSGHub/MSGHubController.cpp"
+ "Bad device name '%s' passed in\n"
+ "Configure"
+ "EnumerateMSGDevices"
+ "Failed to Instantiate MSGHubController\n"
+ "GetConfiguration"
+ "IOService"
+ "Invalid event trigger handle passed in"
+ "MSGClientAPI::%s: Could not allocate the MSG Hub Controller\n"
+ "MSGClientAPI::%s: EnumerateMSGDevices failed with error : 0x%x\n\n"
+ "MSGClientAPI::%s: Failed to allocate device array\n"
+ "MSGClientAPI::%s: Failed to allocate opaque array\n"
+ "MSGClientAPI::%s: Failed to allocate the controller mutex\n"
+ "MSGClientAPI::%s: Invalid deviceName argument passed in\n"
+ "MSGClientAPI::%s: Invalid handle argument passed in\n"
+ "MSGClientAPI::%s: Invalid handle passed in to MSGDeinitializeDeviceHandle\n"
+ "MSGClientAPI::%s: Local MSG Controller not supported on this platform\n"
+ "MSGClientAPI::%s: MSG Hub Controller not supported on this platform\n"
+ "MSGClientAPI::%s: No valid controller found\n"
+ "MSGClientAPI::%s: Releasing the internal device controller\n"
+ "MSGClientAPI::%s: Releasing the internal device handle\n"
+ "MSGClientAPI::%s: Remote MSG Controller not supported on this platform\n"
+ "MSGClientAPI::%s: Unknown exception caught\n"
+ "MSGClientAPI::%s: controllerMutex can not be NULL\n"
+ "MSGClientAPI::%s: deviceCount parameter cannot be NULL\n"
+ "MSGClientAPI::%s: devices parameter cannot be NULL\n"
+ "MSGClientAPI_EventTriggers::%s: Failed to allocate external result array\n"
+ "MSGClientAPI_EventTriggers::%s: Failed to allocate internal result array\n"
+ "MSGClientAPI_EventTriggers::%s: Failed to enumerate MSG devices\n"
+ "MSGClientAPI_EventTriggers::%s: Failed to initialize device handle for %s\n"
+ "MSGClientAPI_EventTriggers::%s: Invalid device handle passed in\n"
+ "MSGClientAPI_EventTriggers::%s: Invalid nameCount: %u (max %u)\n"
+ "MSGClientAPI_EventTriggers::%s: No MSG devices found on platform\n"
+ "MSGClientAPI_EventTriggers::%s: eventTriggerNames is NULL\n"
+ "MSGClientAPI_EventTriggers::%s: results is NULL\n"
+ "MSGClientAPI_Syncs::%s: Failed to allocate external result array\n"
+ "MSGClientAPI_Syncs::%s: Failed to allocate internal result array\n"
+ "MSGClientAPI_Syncs::%s: Failed to enumerate MSG devices\n"
+ "MSGClientAPI_Syncs::%s: Failed to initialize device handle for %s\n"
+ "MSGClientAPI_Syncs::%s: Invalid device handle passed in\n"
+ "MSGClientAPI_Syncs::%s: Invalid nameCount: %u (max %u)\n"
+ "MSGClientAPI_Syncs::%s: No MSG devices found on platform\n"
+ "MSGClientAPI_Syncs::%s: results parameter cannot be NULL\n"
+ "MSGClientAPI_Syncs::%s: syncNames parameter cannot be NULL\n"
+ "MSGController::%s: Attempting to map MSG registers using existing connection...\n"
+ "MSGController::%s: Attempting to map timing info shared memory for sync %u...\n"
+ "MSGController::%s: Did not find any matching services for %s\n"
+ "MSGController::%s: EDT Device Name = %s\n\n"
+ "MSGController::%s: Failed to map MSG registers: 0x%x\n"
+ "MSGController::%s: Failed to map timing info shared memory for sync %u: 0x%x\n"
+ "MSGController::%s: Failed to unmap MSG registers: errno=%d\n"
+ "MSGController::%s: Found service %s\n\n"
+ "MSGController::%s: IOServiceGetMatchingServices failed with error 0x%x\n"
+ "MSGController::%s: IOServiceOpen failed with error : 0x%x\n\n"
+ "MSGController::%s: Insufficient memory for mapping.\n"
+ "MSGController::%s: Invalid memory type or arguments.\n"
+ "MSGController::%s: Maximum device count (%u) exceeded, ignoring additional devices\n"
+ "MSGController::%s: No active connection to MSG Kext. Call openService() first.\n"
+ "MSGController::%s: Permission denied. Check entitlements: com.apple.private.msg.register-access\n"
+ "MSGController::%s: Remote MSG is not supported for timing info shared memory mapping\n"
+ "MSGController::%s: Requested Device Name = %s\n\n"
+ "MSGController::%s: Successfully mapped MSG registers: address=0x%llx, size=0x%llx\n"
+ "MSGController::%s: Successfully mapped timing info shared memory: address=0x%llx, size=0x%x\n"
+ "MSGController::%s: Successfully unmapped MSG registers\n"
+ "MSGController::%s: Unknown error during memory mapping.\n"
+ "MSGController::%s: Virtual memory error during mapping.\n"
+ "MSGController::%s: _openServiceInternal failed with error 0x%x\n\n"
+ "MSGController::%s: actualDeviceCount parameter cannot be NULL\n"
+ "MSGController::%s: devices parameter cannot be NULL\n"
+ "MSGController::%s: isDefaultMsg = %d\n\n"
+ "MSGController::%s: isRequestingDefault = %d, isRequestingRemote = %d\n\n"
+ "MSGController::%s: maxDeviceCount must be greater than 0 and less than %d\n"
+ "MSGCreate"
+ "MSGDeinitializeDeviceHandle"
+ "MSGDeinitializeHubHandle"
+ "MSGGetDevices"
+ "MSGGetSystemState"
+ "MSGHub"
+ "MSGHubClientAPI: AssertMacros: %s, %s file: %s, line: %d, value: %ld\n\n"
+ "MSGHubClientAPI::%s: Could not allocate the MSG Hub Controller\n"
+ "MSGHubClientAPI::%s: Hub configuration failed with error : 0x%x\n"
+ "MSGHubClientAPI::%s: Hub register read failed with error : 0x%x\n"
+ "MSGHubClientAPI::%s: Hub reset failed with error : 0x%x\n"
+ "MSGHubClientAPI::%s: Invalid configReg1 pointer passed in\n"
+ "MSGHubClientAPI::%s: Invalid configReg2 pointer passed in\n"
+ "MSGHubClientAPI::%s: Invalid handle argument passed in\n"
+ "MSGHubClientAPI::%s: Invalid handle passed in to MSGDeinitializeHubHandle\n"
+ "MSGHubClientAPI::%s: MSG Hub Controller not supported on this platform\n"
+ "MSGHubClientAPI::%s: Passed in Hub Controller is NULL\n"
+ "MSGHubClientAPI::%s: Releasing the internal device controller\n"
+ "MSGHubClientAPI::%s: Releasing the internal device handle\n"
+ "MSGHubClientAPI::%s: Unknown exception caught\n"
+ "MSGHubConfigure"
+ "MSGHubController: AssertMacros: %s, %s file: %s, line: %d, value: %ld\n\n"
+ "MSGHubController::%s: Connecting to MSGHub\n"
+ "MSGHubController::%s: IOConnectCallScalarMethod failed for Configure with error : 0x%x\n\n"
+ "MSGHubController::%s: IOConnectCallScalarMethod failed for GetConfiguration with error : 0x%x\n\n"
+ "MSGHubController::%s: IOServiceOpen failed with error : 0x%x\n\n"
+ "MSGHubGetConfiguration"
+ "MSGHubReset"
+ "MSGInitializeDeviceHandle"
+ "MSGInitializeEventTriggerHandle"
+ "MSGInitializeHubHandle"
+ "MSGInitializeSyncHandle"
+ "MSGLookupEventTriggerNamesBatch"
+ "MSGLookupSyncNamesBatch"
+ "No valid MSG controller found"
+ "_connect != IO_OBJECT_NULL"
+ "_ioconnect != IO_OBJECT_NULL"
+ "_num_config_requests == 0"
+ "_service != IO_OBJECT_NULL"
+ "actualDeviceCount"
+ "controllerMutex"
+ "default"
+ "default-device"
+ "device-name"
+ "deviceCount"
+ "deviceCount > 0"
+ "deviceHandle"
+ "deviceName"
+ "devices"
+ "eventTriggerHandle"
+ "eventTriggerNames != nullptr"
+ "externalDeviceArray"
+ "externalResultArray"
+ "getMSGDevices"
+ "handle"
+ "inputConfigReg"
+ "internalDeviceArray"
+ "internalHandle"
+ "internalHubHandle"
+ "internalHubHandle->controller"
+ "internalResultArray"
+ "mapMSGRegistersToUserspace"
+ "mapTimingInfoSharedMemory"
+ "nameCount > 0 && nameCount <= MSG_NAME_LOOKUP_MAX_BATCH_SIZE"
+ "openMatchingService"
+ "openService"
+ "outputConfigReg"
+ "remote"
+ "result == 0 "
+ "result == KERN_SUCCESS"
+ "results"
+ "results != nullptr"
+ "syncNames"
+ "unmapMSGRegistersFromUserspace"
- "!syncHandle->remote"
- "(syncHandle->id == 0)"
- "*size >= PAYLOAD_SIZE(current_read_desc.getEntrySize())"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleMSG/AppleMSG/AppleMSGTypeUtils.cpp"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleMSG/MSGSupport/RingBuffer/RingBufferW1.cpp"
- "ACTUAL_ENTRY_SIZE(max_payload_size) <= MAX_ENTRY_SIZE && ACTUAL_ENTRY_SIZE(max_payload_size) <= data_sz"
- "ACTUAL_ENTRY_SIZE(size) <= header->max_entry_sz"
- "AppleMSGRingBuffer: AssertMacros: %s, %s file: %s, line: %d, value: %ld\n\n"
- "AppleMSGRingBuffer::%s: 0x%llx\n"
- "AppleMSGRingBuffer::%s: Initial Header: 0x%llx, Final Header: 0x%llx\n"
- "AppleMSGRingBuffer::%s: Ring Buffer data:\n"
- "AppleMSGTypeUtils: AssertMacros: %s, %s file: %s, line: %d, value: %ld\n\n"
- "Failed to allocate event trigger handle"
- "Failed to allocate internalTimingArray"
- "Failed to allocate sync handle"
- "IS_MSG_TRANSITION_SCHEDULED_FRAME_IN_FUTURE(tracking.frame_index, targetFrameID)"
- "MSG was not initialized"
- "MSGController::%s: Found service %s\n"
- "allow_reread == true"
- "bad tracking info/targetFrameID"
- "buffer_addr != nullptr && IS_ALIGN64(reinterpret_cast<uint64_t>(buffer_addr))"
- "buffer_len >= header_sz"
- "bytes_written_since >= 0"
- "currentTime >= referencePulseTime"
- "current_read_desc.isValid()"
- "data_sz >= bytes_written_since + bytes_read"
- "data_sz >= bytes_written_since + bytes_read - sizeof(prev_read_desc)"
- "dumpStateToLogs"
- "finishedReading == false"
- "futureFrameID != nullptr"
- "futurePulseTime != nullptr"
- "header->max_entry_sz <= data_sz"
- "internalTimingArray"
- "prev_read_desc.getRaw() == 0"
- "retHandle"
- "serviceMatchedCallback"
- "size > 0"
- "timer_sel == AppleMSG::msg_timer_sel_t::GTB"
- "write_desc.getRaw() != 0"

```
