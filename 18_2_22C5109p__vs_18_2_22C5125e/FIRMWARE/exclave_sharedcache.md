## exclave_sharedcache

> `exclave_sharedcache`

```diff

-460.60.233.0.1
-  __TEXT.__text: 0x4bba9c
+460.60.253.0.1
+  __TEXT.__text: 0x4be8f8
   __TEXT.__lcxx_override: 0x200
-  __TEXT.__cstring: 0x30bfe
-  __TEXT.__const: 0xe27a8
+  __TEXT.__cstring: 0x3091f
+  __TEXT.__const: 0xe2768
   __TEXT.__swift5_typeref: 0xdee5
   __TEXT.__swift5_reflstr: 0x9235
   __TEXT.__swift5_assocty: 0x6a90

   __TEXT.__term_offsets: 0x0
   __TEXT.__swift5_replace: 0x0
   __TEXT.__thread_starts: 0x3c
-  __TEXT.__eh_frame: 0x23194
+  __TEXT.__eh_frame: 0x23884
   __DATA.__got: 0x18
   __DATA.__auth_ptr: 0x270
   __DATA.__mod_init_func: 0x38
-  __DATA.__const: 0x2c520
+  __DATA.__const: 0x2c538
   __DATA.__objc_imageinfo: 0x8
   __DATA.__data: 0xe4d8
   __DATA.__shared_cache: 0x70

   __DATA.__DEVICETREE: 0x18
   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x28
-  __DATA.__common: 0x539
+  __DATA.__common: 0x531
   __DATA.__bss: 0x8ef0
-  __PDATA.__data: 0x1590
-  __PDATA.__const: 0x2180
+  __PDATA.__data: 0x15f0
+  __PDATA.__const: 0x2190
   __PDATA.__ENDPOINTS: 0x731
   __PDATA.__shared_cache: 0x38
   __PDATA.__mod_init_func: 0x18
   __PDATA.__auth_ptr: 0x20
   __PDATA.__objc_imageinfo: 0x8
-  __PDATA.__bss: 0x40f0
+  __PDATA.__bss: 0x40e0
   __PDATA.__common: 0x1fc0
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  Functions: 18359
+  Functions: 18394
   Symbols:   0
-  CStrings:  5135
+  CStrings:  5142
 
CStrings:
+ "!va_alloc->uncommitted_alloc"
+ "(tb_message_decode_capability(msg, (uint64_t *) &frame) == TB_ERROR_SUCCESS) && \"failed to decode capability\""
+ "(tb_message_encode_capability(&msg, (uint64_t) frame) == TB_ERROR_SUCCESS) && \"failed to encode capability\""
+ "/AppleInternal/Library/BuildRoots/11914d60-911b-11ef-aa10-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.2.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
+ "/AppleInternal/Library/BuildRoots/11914d60-911b-11ef-aa10-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.2.Internal.sdk/System/ExclaveCore/usr/local/standalone/RTKit/usr/include/protocols/mbi_tightbeam_protocol.h"
+ "<="
+ "CNode"
+ "Could not allocate for VAS private %!s(MISSING) range of %!l(MISSING)x bytes (%!s(MISSING))\n"
+ "DART_CNODE"
+ "EASM_CNODE"
+ "Prespecializations library: Disabling, SWIFT_DEBUG_ENABLE_LIB_PRESPECIALIZED = %!d(MISSING)\n"
+ "SHADOW_CNODE"
+ "TB_FATAL: Attempt to retrieve accumulator in environment without large message support (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from allocAMXContext (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from allocEndpoint (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from allocExecutionContext (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from frameCopy (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from freeKernelObject (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from getAddressSpaceInfo (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from getIPCStackEntry (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from handleFault (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from mapMacho (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from physicalAddress (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from registerThread (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from rootCopy (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from setupSuccessful (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from spanAlloc (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from spanAt (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from spanBump (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from spanConfig (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from spanDepopulate (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from spanDestroy (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from spanDowngrade (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from spanMapFrame (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from spanMerge (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from spanPopulate (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from spanResize (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from spanSetFaultstate (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from spanSplit (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from unregisterThread (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid value: unexpected bits, 0x%!l(MISSING)lx (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid value: unexpected case value, %!l(MISSING)lx (%!s(MISSING):%!d(MISSING))\n"
+ "[VAS abort in function %!s(MISSING) at line %!d(MISSING)] [true: %!l(MISSING)lx %!s(MISSING) %!l(MISSING)lx]Could not reserve VA for VAS private %!s(MISSING) range [%!l(MISSING)x, %!l(MISSING)x) (%!s(MISSING))\n\n"
+ "[VAS abort in function %!s(MISSING) at line %!d(MISSING)] [true: %!l(MISSING)lx %!s(MISSING) %!l(MISSING)lx]Used up entire initial [%!l(MISSING)x, %!l(MISSING)x) allocation for va_alloc %!p(MISSING)\n"
+ "[VAS abort in function %!s(MISSING) at line %!d(MISSING)] [true: %!l(MISSING)lx %!s(MISSING) %!l(MISSING)lx]addr not as expected; another alloc happened?\n"
+ "[VAS abort in function %!s(MISSING) at line %!d(MISSING)] [true: %!l(MISSING)lx %!s(MISSING) %!l(MISSING)lx]allocation point must be inside span\n"
+ "[VAS abort in function %!s(MISSING) at line %!d(MISSING)] [true: %!l(MISSING)lx %!s(MISSING) %!l(MISSING)lx]allocation point must be part of span\n"
+ "[VAS abort in function %!s(MISSING) at line %!d(MISSING)] [true: (%!s(MISSING))] Couldn't sustain VAS object watermark: _alloc_va() failed\n"
+ "[VAS abort in function %!s(MISSING) at line %!d(MISSING)] [true: (%!s(MISSING))] Couldn't sustain VAS object watermark: allocating frame failed\n"
+ "[VAS abort in function %!s(MISSING) at line %!d(MISSING)] [true: (%!s(MISSING))] Couldn't sustain VAS object watermark: allocating page table\n"
+ "[VAS abort in function %!s(MISSING) at line %!d(MISSING)] [true: (%!s(MISSING))] _alloc_va() with uncommitted allocation\n"
+ "[VAS abort in function %!s(MISSING) at line %!d(MISSING)] [true: (%!s(MISSING))] _commit_alloc_va()/_undo_alloc_va() with no uncommitted allocation\n"
+ "[VAS abort in function %!s(MISSING) at line %!d(MISSING)] [true: (%!s(MISSING))] heap reserve dropped with uncommitted allocation\n"
+ "[VAS abort in function %!s(MISSING) at line %!d(MISSING)] [true: (%!s(MISSING))] returning with uncommitted allocation\n"
+ "^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[40c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16"
+ "__span_alloc"
+ "_alloc_memory_frame"
+ "_alloc_va"
+ "_commit_alloc_va"
+ "heap->ensure_watermark_active"
+ "heap->heap_va.uncommitted_alloc || heap->cnode_va.uncommitted_alloc"
+ "invalid rawValue for ACMEnvironmentVariableTB: "
+ "invalid rawValue for ACMErrorTB: "
+ "invalid rawValue for ALSIOReturn: "
+ "invalid rawValue for ALSOperationMode: "
+ "invalid rawValue for ALSOrientation: "
+ "invalid rawValue for ALSPlacement: "
+ "invalid rawValue for ALSPowerEvent: "
+ "invalid rawValue for ALSSamplingMode: "
+ "invalid rawValue for ALSSensorType: "
+ "invalid rawValue for ArbitratedAudioBuffer: "
+ "invalid rawValue for DeviceResourceError: "
+ "invalid rawValue for DriverTimerType: "
+ "invalid rawValue for DriverUpcallError: "
+ "invalid rawValue for EXBrightALSSVerificationSCA: "
+ "invalid rawValue for EXBrightSILHealth: "
+ "invalid rawValue for EXDisplayPipeHealthFailures: unexpected bits in value, "
+ "invalid rawValue for EXDisplayPipeIndicator: "
+ "invalid rawValue for ExclaveSEPManagerResult: "
+ "invalid rawValue for FSTag: "
+ "invalid rawValue for LifeCycleError: "
+ "invalid rawValue for LogStreamType: "
+ "invalid rawValue for NotificationError: "
+ "invalid rawValue for PageKind: "
+ "invalid rawValue for PowerState: "
+ "invalid rawValue for RequestedRefreshRate: "
+ "invalid rawValue for SensorType: "
+ "invalid rawValue for StorageUpcallsError: "
+ "invalid rawValue for SuppressionCode: "
+ "invalid rawValue for SyncOp: "
+ "va_alloc->uncommitted_alloc"
+ "vas_core_heap_alloc_span"
+ "xrt_init failed with %!d(MISSING)"
- "(decode_error == TB_ERROR_SUCCESS) && \"tb_message_decode_capability failed\""
- "(easm_failure__decode(message, &result->value.failure) == TB_ERROR_SUCCESS) && \"failed to decode type: EASM.Failure\""
- "(easm_memoryfaultkind__decode(msg, &faultType) == TB_ERROR_SUCCESS) && \"failed to decode type: EASM.MemoryFaultKind\""
- "(easm_memoryfaultstate__decode(msg, &state) == TB_ERROR_SUCCESS) && \"failed to decode type: EASM.MemoryFaultState\""
- "(easm_spanconfig__decode(message, &result->value.success) == TB_ERROR_SUCCESS) && \"failed to decode type: EASM.SpanConfig\""
- "(easm_spanconfig__decode(msg, &config) == TB_ERROR_SUCCESS) && \"failed to decode type: EASM.SpanConfig\""
- "(easm_spanrefconfig__decode(message, &result->value.success) == TB_ERROR_SUCCESS) && \"failed to decode type: EASM.SpanRefConfig\""
- "(oslogexclaves_signposterror__decode(message, &result->value.failure) == TB_ERROR_SUCCESS) && \"failed to decode type: OSLogExclaves.SignpostError\""
- "(oslogexclaves_subsystemerror__decode(message, &result->value.failure) == TB_ERROR_SUCCESS) && \"failed to decode type: OSLogExclaves.SubsystemError\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from allocAMXContext\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from allocEndpoint\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from allocExecutionContext\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from frameCopy\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from freeKernelObject\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from getAddressSpaceInfo\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from getIPCStackEntry\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from handleFault\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from mapMacho\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from physicalAddress\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from registerThread\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from rootCopy\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from setupSuccessful\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from spanAlloc\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from spanAt\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from spanBump\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from spanConfig\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from spanDepopulate\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from spanDestroy\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from spanDowngrade\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from spanMapFrame\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from spanMerge\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from spanPopulate\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from spanResize\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from spanSetFaultstate\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from spanSplit\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from unregisterThread\""
- "(sharedmemorybase_accesserror__decode(message, &result->value.failure) == TB_ERROR_SUCCESS) && \"failed to decode type: SharedMemoryBase.AccessError\""
- "(sharedmemorybase_mappingresult__decode(message, &result->value.success) == TB_ERROR_SUCCESS) && \"failed to decode type: SharedMemoryBase.MappingResult\""
- "(sharedmemorybase_perms__decode(message, &opt->value) == TB_ERROR_SUCCESS) && \"failed to decode type: SharedMemoryBase.Perms\""
- "/AppleInternal/Library/BuildRoots/be5905ba-8b8c-11ef-a962-725d7f06bcf4/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.2.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
- "/AppleInternal/Library/BuildRoots/be5905ba-8b8c-11ef-a962-725d7f06bcf4/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.2.Internal.sdk/System/ExclaveCore/usr/local/standalone/RTKit/usr/include/protocols/mbi_tightbeam_protocol.h"
- "Disabling metadata, SWIFT_DEBUG_ENABLE_LIB_PRESPECIALIZED_METADATA is false."
- "Prespecializations library: %!s(MISSING)\n"
- "Prespecializations library: Data at %!p(MISSING) contains both maps. Using %!s(MISSING) keyed map.\n"
- "Prespecializations library: Data at %!p(MISSING) only contains name-keyed map.\n"
- "Prespecializations library: Data at %!p(MISSING) only contains pointer-keyed map.\n"
- "Prespecializations library: No prespecializations map available from data at %!p(MISSING), disabling.\n"
- "Prespecializations library: Returning data pointer %!p(MISSING)\n"
- "Prespecializations library: Setting descriptorMapEnabled=%!s(MISSING) from SWIFT_DEBUG_ENABLE_LIB_PRESPECIALIZED_DESCRIPTOR_LOOKUP.\n"
- "Prespecializations library: Setting descriptorMapEnabled=%!s(MISSING) from the option flags.\n"
- "VAS_CNODE"
- "[VAS abort in function %!s(MISSING) at line %!d(MISSING)] [true: %!l(MISSING)lx %!s(MISSING) %!l(MISSING)lx]Could not allocate span for VAS private heap (%!s(MISSING))\n\n"
- "^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[32c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16"
- "_span_alloc"
- "invalid rawValue for ACMEnvironmentVariableTB "
- "invalid rawValue for ACMErrorTB "
- "invalid rawValue for ALSIOReturn "
- "invalid rawValue for ALSOperationMode "
- "invalid rawValue for ALSOrientation "
- "invalid rawValue for ALSPlacement "
- "invalid rawValue for ALSPowerEvent "
- "invalid rawValue for ALSSamplingMode "
- "invalid rawValue for ALSSensorType "
- "invalid rawValue for ArbitratedAudioBuffer "
- "invalid rawValue for DeviceResourceError "
- "invalid rawValue for DriverTimerType "
- "invalid rawValue for DriverUpcallError "
- "invalid rawValue for EXBrightALSSVerificationSCA "
- "invalid rawValue for EXBrightSILHealth "
- "invalid rawValue for EXDisplayPipeIndicator "
- "invalid rawValue for ExclaveSEPManagerResult "
- "invalid rawValue for FSTag "
- "invalid rawValue for LifeCycleError "
- "invalid rawValue for LogStreamType "
- "invalid rawValue for NotificationError "
- "invalid rawValue for PageKind "
- "invalid rawValue for PowerState "
- "invalid rawValue for RequestedRefreshRate "
- "invalid rawValue for SensorType "
- "invalid rawValue for StorageUpcallsError "
- "invalid rawValue for SuppressionCode "
- "invalid rawValue for SyncOp "
- "nested"
- "pointer"
- "vas span alloc failed on region of size %!z(MISSING)u with error code %!x(MISSING), error name %!s(MISSING), and detail %!d(MISSING)\n"
- "vas_core_heap_reserve_region"

```
