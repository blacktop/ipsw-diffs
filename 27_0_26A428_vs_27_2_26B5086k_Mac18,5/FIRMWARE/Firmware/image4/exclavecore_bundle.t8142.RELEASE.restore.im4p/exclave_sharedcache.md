## exclave_sharedcache

> `Firmware/image4/exclavecore_bundle.t8142.RELEASE.restore.im4p/exclave_sharedcache`

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
-  __TEXT.__text: 0x5cce94
+1777.40.24.501.1
+  __TEXT.__text: 0x5d7030
   __TEXT.__lcxx_override: 0xe4
-  __TEXT.__cstring: 0x4e9f1
-  __TEXT.__const: 0x11fb14
-  __TEXT.__swift5_typeref: 0x13162
-  __TEXT.__swift5_reflstr: 0x114a8
-  __TEXT.__swift5_assocty: 0x7a10
-  __TEXT.__swift5_fieldmd: 0x1a910
-  __TEXT.__constg_swiftt: 0x25d5c
-  __TEXT.__swift5_protos: 0x8b0
-  __TEXT.__swift5_proto: 0x3a1c
-  __TEXT.__swift5_types: 0x2234
+  __TEXT.__cstring: 0x4f3a1
+  __TEXT.__const: 0x120d14
+  __TEXT.__swift5_typeref: 0x132aa
+  __TEXT.__swift5_reflstr: 0x12308
+  __TEXT.__swift5_assocty: 0x7ba8
+  __TEXT.__swift5_fieldmd: 0x1b0a0
+  __TEXT.__constg_swiftt: 0x261d0
+  __TEXT.__swift5_protos: 0x8c0
+  __TEXT.__swift5_proto: 0x3ad4
+  __TEXT.__swift5_types: 0x227c
   __TEXT.__swift5_types2: 0x60
-  __TEXT.__swift5_builtin: 0x15a4
-  __TEXT.__swift5_capture: 0xf9c
+  __TEXT.__swift5_builtin: 0x1590
+  __TEXT.__swift5_capture: 0xfcc
   __TEXT.__objc_methtype: 0xe1
-  __TEXT.__swift5_mpenum: 0x3d4
-  __TEXT.__swift_as_entry: 0x998
-  __TEXT.__swift_as_ret: 0xb08
-  __TEXT.__swift_as_cont: 0x11f8
+  __TEXT.__swift5_mpenum: 0x3b8
+  __TEXT.__swift_as_entry: 0x9b4
+  __TEXT.__swift_as_ret: 0xb2c
+  __TEXT.__swift_as_cont: 0x1224
   __TEXT.__oslogstring: 0xf0
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constructor: 0x0

   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x0
   __TEXT.__chain_fixups: 0xb0
-  __TEXT.__eh_frame: 0x32fa4
+  __TEXT.__eh_frame: 0x3391c
   __DATA.__TIGHTBEAM_VT: 0x720
   __DATA.__TIGHTBEAM: 0x1d8
-  __DATA.__const: 0x3ae60
-  __DATA.__data: 0x16a30
+  __DATA.__const: 0x3b818
+  __DATA.__data: 0x16d20
   __DATA.__mod_init_func: 0x40
-  __DATA.__ENDPOINTS: 0x1a328
-  __DATA.__auth_ptr: 0x2010
+  __DATA.__ENDPOINTS: 0x1a744
+  __DATA.__auth_ptr: 0x2078
   __DATA.__DEVICETREE: 0x18
   __DATA.__shared_cache: 0x380
   __DATA.__DARTS: 0x93f

   __DATA.__thread_bss: 0x30
   __DATA.__common: 0x6ca
   __PDATA.__auth_ptr: 0x280
-  __PDATA.__const: 0x67b0
+  __PDATA.__const: 0x6800
   __PDATA.__objc_imageinfo: 0x8
   __PDATA.__mod_init_func: 0x18
   __PDATA.__data: 0x2af0

   __PDATA.__common: 0x2578
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  Functions: 22510
+  Functions: 22622
   Symbols:   1
-  CStrings:  7177
+  CStrings:  7226
 
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
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.MacOSX.platform/Developer/SDKs/ExclaveCore.MacOSX27.2.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.MacOSX.platform/Developer/SDKs/ExclaveCore.MacOSX27.2.Internal.sdk/System/ExclaveCore/usr/local/standalone/RTKit/usr/include/protocols/mbi_tightbeam_protocol.h"
+ "ANE power op returned unknown status byte: "
+ "Active pause requests: "
+ "Adding pause request: "
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
+ "Quick start policy resolved @ GLTB "
+ "Quick start policy violated @ GLTB "
+ "Removed pause request: "
+ "Starting quick start policy @ GLTB "
+ "TB_FATAL: invalid result returned from unmapXnuContentRegionWithFlags (%s:%d)\n"
+ "VIOLATION: CIL never came on during quick start policy"
+ "]\n  defaultDisplayChanged: triggered="
+ "] .rampUp -> .steady. Ctx: filteredNits="
+ "] .rampUp restart: start "
+ "] Failed to get filtered IB for rampUp, this should never happen! (items: "
+ "] In .rampUp, but currentMIB is nil. This should never happen!"
+ "])\n  medinaStateDisplayWake: allowance="
+ "])\n  quickStart: allowance="
+ "_insecure_random_buf"
+ "hold_ane_power_assertion threw an unexpected error type"
+ "i24@?0^{?=^{thread}}8^{thread={allocation=^{allocation_map}{?=s}{?=AC}^{allocation}}QCQQQ^{?}(?={?=^{thread}^^{thread}}{heap_element=^{?}{?=^{thread}}{?=^{thread}}Q})^{turnstile}{?={?=CQ}Q}QQQ{inherit_set=^{turnstile}}{?={?=s}Q}QQQCS}16"
+ "invalid rawValue for ExclaveSEPANEControlEndpoint.Selector "
+ "invalid rawValue for SensorPauseReason: "
+ "invalid rawValue for XnuContentANEFlags: unexpected bits in value, "
+ "invalid rawValue for XnuContentUnloadFlags: unexpected bits in value, "
+ "malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:982)"
+ "malloc assertion \"!memtag_config.tag_data\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8903)"
+ "malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8331)"
+ "malloc assertion \"allocation_front_count == 2\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7872)"
+ "malloc assertion \"old_size\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:6854)"
+ "malloc assertion \"success\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:2216)"
+ "malloc assertion \"success\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:5356)"
+ "ms\n  displayPower: triggered="
+ "ms, lastFiltered="
+ "nits preserved (MIB="
+ "nits, currentFiltered="
+ "nits, expectedGrowth="
+ "octopus_no_quick_start"
+ "octopus_quick_start"
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
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.MacOSX.platform/Developer/SDKs/ExclaveCore.MacOSX27.0.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.MacOSX.platform/Developer/SDKs/ExclaveCore.MacOSX27.0.Internal.sdk/System/ExclaveCore/usr/local/standalone/RTKit/usr/include/protocols/mbi_tightbeam_protocol.h"
- "[B] Start Siri dark wake policy"
- "[B] Stop Siri dark wake policy"
- "] Cannot estimate ramp duration, invalid target brightness value: "
- "] Switched to MIB ramp up mode during brightness ramp down, ignoring this frame."
- "][healthCheckMode] .rampUp -> .steady. Ctx: adjustedIBNitsFiltered="
- "i24@?0^{?=^{thread}}8^{thread={allocation=^{allocation_map}{?=s}{?=AC}^{allocation}}QCQQQ^{?}(?={?=^{thread}^^{thread}}{heap_element=^{?}{?=^{thread}}{?=^{thread}}Q})^{turnstile}{?={?=CQ}Q}QQQ{inherit_set=^{turnstile}}{?={?=s}{?=s}}QQQCS}16"
- "malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:981)"
- "malloc assertion \"!memtag_config.tag_data\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8865)"
- "malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8293)"
- "malloc assertion \"allocation_front_count == 2\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7834)"
- "malloc assertion \"old_size\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:6830)"
- "malloc assertion \"success\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:2197)"
- "malloc assertion \"success\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:5336)"
- "nits, elapsedWithoutIBIncrease="
- "total_memory_kib"
- "v14@?0{easm_space_unmapxnucontentregion__result_s=C(?={easm_failure_s=CS})}8"
- "vas__easm_unmap_xnu_content_region"
```
