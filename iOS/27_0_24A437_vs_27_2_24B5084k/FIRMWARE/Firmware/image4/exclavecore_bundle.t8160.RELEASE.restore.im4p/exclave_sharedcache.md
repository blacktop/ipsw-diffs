## exclave_sharedcache

> `Firmware/image4/exclavecore_bundle.t8160.RELEASE.restore.im4p/exclave_sharedcache`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_types2`
- `__TEXT.__swift5_entry`
- `__TEXT.__chain_fixups`
- `__DATA.__TIGHTBEAM_VT`
- `__DATA.__TIGHTBEAM`
- `__DATA.__mod_init_func`
- `__DATA.__shared_cache`
- `__DATA.__got`
- `__DATA.__thread_vars`
- `__PDATA.__auth_ptr`
- `__PDATA.__mod_init_func`
- `__PDATA.__data`
- `__PDATA.__shared_cache`

```diff

-1777.0.27.0.0
-  __TEXT.__text: 0x5efd18
+1777.40.23.502.2
+  __TEXT.__text: 0x5fa338
   __TEXT.__lcxx_override: 0xd0
-  __TEXT.__cstring: 0x4ffc1
-  __TEXT.__const: 0x122d14
-  __TEXT.__swift5_typeref: 0x1439a
-  __TEXT.__swift5_reflstr: 0x12398
-  __TEXT.__swift5_assocty: 0x7b78
-  __TEXT.__swift5_fieldmd: 0x1c4d4
-  __TEXT.__constg_swiftt: 0x28564
-  __TEXT.__swift5_protos: 0x988
-  __TEXT.__swift5_proto: 0x3ddc
-  __TEXT.__swift5_types: 0x24cc
+  __TEXT.__cstring: 0x50a21
+  __TEXT.__const: 0x123d84
+  __TEXT.__swift5_typeref: 0x144ee
+  __TEXT.__swift5_reflstr: 0x13508
+  __TEXT.__swift5_assocty: 0x7d10
+  __TEXT.__swift5_fieldmd: 0x1cdb0
+  __TEXT.__constg_swiftt: 0x28a48
+  __TEXT.__swift5_protos: 0x998
+  __TEXT.__swift5_proto: 0x3e94
+  __TEXT.__swift5_types: 0x251c
   __TEXT.__swift5_types2: 0x60
-  __TEXT.__swift5_builtin: 0x15cc
-  __TEXT.__swift5_capture: 0x1018
+  __TEXT.__swift5_builtin: 0x15b8
+  __TEXT.__swift5_capture: 0x1048
   __TEXT.__objc_methtype: 0xe1
-  __TEXT.__swift5_mpenum: 0x3d4
-  __TEXT.__swift_as_entry: 0x998
-  __TEXT.__swift_as_ret: 0xb08
-  __TEXT.__swift_as_cont: 0x11f8
+  __TEXT.__swift5_mpenum: 0x3b8
+  __TEXT.__swift_as_entry: 0x9b4
+  __TEXT.__swift_as_ret: 0xb2c
+  __TEXT.__swift_as_cont: 0x1224
   __TEXT.__oslogstring: 0xf3
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constructor: 0x0

   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x0
   __TEXT.__chain_fixups: 0xb8
-  __TEXT.__eh_frame: 0x354c0
+  __TEXT.__eh_frame: 0x35db0
   __DATA.__TIGHTBEAM_VT: 0x8a0
   __DATA.__TIGHTBEAM: 0x238
-  __DATA.__const: 0x3dac8
-  __DATA.__data: 0x18de0
+  __DATA.__const: 0x3e5d0
+  __DATA.__data: 0x19110
   __DATA.__mod_init_func: 0x40
-  __DATA.__ENDPOINTS: 0x1a328
-  __DATA.__auth_ptr: 0x2420
+  __DATA.__ENDPOINTS: 0x1a536
+  __DATA.__auth_ptr: 0x2490
   __DATA.__DEVICETREE: 0x18
   __DATA.__shared_cache: 0x380
   __DATA.__MMIOREGS: 0x795

   __DATA.__thread_bss: 0x30
   __DATA.__common: 0x72a
   __PDATA.__auth_ptr: 0x280
-  __PDATA.__const: 0x67b0
+  __PDATA.__const: 0x6800
   __PDATA.__objc_imageinfo: 0x8
   __PDATA.__mod_init_func: 0x18
   __PDATA.__data: 0x2af0

   __DATA_CONST.__mod_term_func: 0x0
   Functions: 657
   Symbols:   1
-  CStrings:  7363
+  CStrings:  7418
 
Functions:
~ sub_7ffe468 : 141616 -> 141032
~ sub_80246a0 -> sub_8024458 : 423936 -> 425680
~ sub_808bea0 -> sub_808c328 : 173496 -> 173736
~ sub_80b65d0 -> sub_80b6b48 : 240 -> 184
~ sub_80ba520 -> sub_80baa60 : 141340 -> 141072
~ sub_80e86b4 -> sub_80e8ae8 : 62228 -> 61580
~ sub_80f79c8 -> sub_80f7b74 : 26176 -> 26224
~ sub_80fe60c -> sub_80fe7e8 : 8584 -> 8724
~ sub_810a934 -> sub_810ab9c : 7848 -> 7860
~ sub_8110900 -> sub_8110b74 : 47660 -> 48104
~ sub_8127834 -> sub_8127c64 : 1076 -> 1104
~ sub_8127c68 -> sub_81280b4 : 15488 -> 15504
~ sub_812cba0 -> sub_812cffc : 305420 -> 305432
~ sub_818b71c -> sub_818bb84 : 955868 -> 970800
~ sub_82764b8 -> sub_827a374 : 15032 -> 15180
~ sub_827a0c0 -> sub_827e010 : 273200 -> 288992
~ sub_82bebf4 -> sub_82c68f4 : 408880 -> 409180
~ sub_832a1f4 -> sub_8332020 : 31976 -> 31980
~ sub_833d6a8 -> sub_83454d8 : 208 -> 188
~ sub_833d8d4 -> sub_83456f0 : 1128 -> 1188
~ sub_833ddc8 -> sub_8345c20 : 392 -> 408
~ sub_833df50 -> sub_8345db8 : 192 -> 216
~ sub_833e010 -> sub_8345e90 : 580 -> 596
~ sub_833e2e8 -> sub_8346178 : 36 -> 48
~ sub_833e328 -> sub_83461c4 : 964 -> 976
~ sub_833e6ec -> sub_8346594 : 1224 -> 1320
~ sub_833ebb4 -> sub_8346abc : 604 -> 588
~ sub_833ee10 -> sub_8346d08 : 3108 -> 3052
~ sub_833fa34 -> sub_83478f4 : 32684 -> 32748
~ sub_848e768 -> sub_8496668 : 12944 -> 12936
~ sub_84f7cf0 -> sub_84ffbe8 : 1432 -> 1444
~ sub_84f8550 -> sub_8500454 : 356 -> 368
~ sub_84fae0c -> sub_8502d1c : 948 -> 936
~ sub_858b2d4 -> sub_85931d8 : 397408 -> 407420
CStrings:
+ "  Quick start = "
+ " message to SEP. ane_id: "
+ " succeeded for ane_id "
+ " will start once sensor sessions are resumed"
+ "$JgExclaveSEPManager.ExclaveSEPANEControlEndpoint"
+ ") < rampUp startTs ("
+ "), this should never happen!"
+ ", nextSubCheck @ "
+ ", priorFiltered="
+ ".failureNoFilteredIB"
+ ".failureRampUpNoProgress(checkType="
+ ".failureTimestampUnderflow"
+ ".failureTimestampUnderflow(lhs="
+ ".rampUp(start @ "
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS27.2.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS27.2.Internal.sdk/System/ExclaveCore/usr/local/standalone/RTKit/usr/include/protocols/mbi_tightbeam_protocol.h"
+ "ANE power op returned unknown status byte: "
+ "Active pause requests: "
+ "Adding pause request: "
+ "BUG IN LIBTRACE: log payload "
+ "Failed to get frames from region "
+ "I14@?0{easm_space_unmapxnucontentregionwithflags__result_s=C(?={easm_failure_s=CS})}8"
+ "I28@?0Q8I16@?<I@?{easm_space_unmapxnucontentregionwithflags__result_s=C(?={easm_failure_s=CS})}>20"
+ "Ignoring duplicate pause request: "
+ "Ignoring pause request due to non-enforcing mode: "
+ "Ignoring pause request since ISP watchdog is disabled: "
+ "Ignoring pause request since health checks are disabled: "
+ "Invalid key value while decoding result type for hold_ane_power_assertion"
+ "Invalid key value while decoding result type for release_ane_power_assertion"
+ "Invalid key value while decoding result type for unloadMemoryWithFlags"
+ "Invalid key value while decoding result type for updateXnuContentWithFlags"
+ "Log payload exceeds "
+ "Quick start policy canceled ("
+ "Quick start policy resolved @ GLTB "
+ "Quick start policy violated @ GLTB "
+ "Removed pause request: "
+ "Starting quick start policy @ GLTB "
+ "TB_FATAL: invalid result returned from unmapXnuContentRegionWithFlags (%s:%d)\n"
+ "VIOLATION: CIL never came on during quick start policy"
+ "[LogServer] error: "
+ "]\n  defaultDisplayChanged: triggered="
+ "] .rampUp -> .steady. Ctx: filteredNits="
+ "] .rampUp restart: start "
+ "] Failed to get filtered IB for rampUp, this should never happen! (items: "
+ "] In .rampUp, but currentMIB is nil. This should never happen!"
+ "])\n  medinaStateDisplayWake: allowance="
+ "])\n  quickStart: allowance="
+ "_insecure_random_buf"
+ "_os_log_payload_size(olp), OS_LOG_EXCLAVES_PAYLOAD_MAX"
+ "hold_ane_power_assertion threw an unexpected error type"
+ "i24@?0^{?=^{thread}}8^{thread={allocation=^{allocation_map}{?=s}{?=AC}^{allocation}}QCQQQ^{?}(?={?=^{thread}^^{thread}}{heap_element=^{?}{?=^{thread}}{?=^{thread}}Q})^{turnstile}{?={?=CQ}Q}QQQ{inherit_set=^{turnstile}}{?={?=s}Q}QQQCS}16"
+ "invalid rawValue for ExclaveSEPANEControlEndpoint.Selector "
+ "invalid rawValue for SensorPauseReason: "
+ "invalid rawValue for XnuContentANEFlags: unexpected bits in value, "
+ "invalid rawValue for XnuContentUnloadFlags: unexpected bits in value, "
+ "malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:982)"
+ "malloc assertion \"!memtag_config.tag_data\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8903)"
+ "malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8331)"
+ "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7872)"
+ "malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:6854)"
+ "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:2216)"
+ "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:5356)"
+ "ms\n  displayPower: triggered="
+ "ms, lastFiltered="
+ "nits preserved (MIB="
+ "nits, currentFiltered="
+ "nits, expectedGrowth="
+ "octopus_medina_state_display_wake_allowance"
+ "octopus_no_quick_start"
+ "octopus_quick_start"
+ "olp->olp_tpb.tp_size, OS_LOG_EXCLAVES_TRACEPOINT_HDR_SIZE"
+ "quick-start-allowance"
+ "release_ane_power_assertion threw an unexpected error type"
+ "s[0] || s[1]"
+ "total_memory_usage_bytes"
+ "unmapXnuContentRegionWithFlags"
+ "updateXnuContent(refId:ranges:flags:)"
+ "v14@?0{easm_space_unmapxnucontentregionwithflags__result_s=C(?={easm_failure_s=CS})}8"
+ "vas__easm_unmap_xnu_content_region_with_flags"
+ "x, actualGrowth="
- ", Last increase: "
- ", lastIncreasedIB="
- ".failureRampUpBrightnessBelowStartIB(startIB="
- ".failureRampUpBrightnessDecreased(startIB="
- ".failureRampUpNoProgress(lastIncreasedIB="
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS27.0.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS27.0.Internal.sdk/System/ExclaveCore/usr/local/standalone/RTKit/usr/include/protocols/mbi_tightbeam_protocol.h"
- "BUG IN LIBTRACE: Received a BATCH_ERROR while creating a LogBatch"
- "] Cannot estimate ramp duration, invalid target brightness value: "
- "] Switched to MIB ramp up mode during brightness ramp down, ignoring this frame."
- "][healthCheckMode] .rampUp -> .steady. Ctx: adjustedIBNitsFiltered="
- "_os_log_payload_size(olp), OS_LOG_PAYLOAD_HARD_MAX_SIZE"
- "i24@?0^{?=^{thread}}8^{thread={allocation=^{allocation_map}{?=s}{?=AC}^{allocation}}QCQQQ^{?}(?={?=^{thread}^^{thread}}{heap_element=^{?}{?=^{thread}}{?=^{thread}}Q})^{turnstile}{?={?=CQ}Q}QQQ{inherit_set=^{turnstile}}{?={?=s}{?=s}}QQQCS}16"
- "malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:981)"
- "malloc assertion \"!memtag_config.tag_data\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8865)"
- "malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8293)"
- "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7834)"
- "malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:6830)"
- "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:2197)"
- "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:5336)"
- "nits, elapsedWithoutIBIncrease="
- "olp->olp_tpb.tp_size, OS_LOG_PAYLOAD_HDR_SIZE"
- "total_memory_kib"
- "v14@?0{easm_space_unmapxnucontentregion__result_s=C(?={easm_failure_s=CS})}8"
- "vas__easm_unmap_xnu_content_region"
```
