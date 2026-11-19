## exclave_sharedcache

> `Firmware/image4/exclavecore_bundle.t8142.RELEASE.im4p/exclave_sharedcache`

### Sections with Same Size but Changed Content

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
-  __TEXT.__text: 0xd4637c
+1777.40.37.0.0
+  __TEXT.__text: 0xd6b970
   __TEXT.__lcxx_override: 0xe4
-  __TEXT.__cstring: 0xa37d1
-  __TEXT.__const: 0x19aa34
-  __TEXT.__swift5_typeref: 0x2a036
-  __TEXT.__swift5_reflstr: 0x3bbc8
-  __TEXT.__swift5_assocty: 0xe648
-  __TEXT.__swift5_fieldmd: 0x5c530
-  __TEXT.__constg_swiftt: 0x61a04
-  __TEXT.__swift5_protos: 0x1208
-  __TEXT.__swift5_proto: 0x9a2c
-  __TEXT.__swift5_types: 0x5ec4
-  __TEXT.__swift5_types2: 0xbc
-  __TEXT.__swift5_builtin: 0x2738
-  __TEXT.__swift5_capture: 0x34d4
-  __TEXT.__objc_methtype: 0x2b6
-  __TEXT.__swift5_mpenum: 0xc38
-  __TEXT.__swift_as_entry: 0x160c
-  __TEXT.__swift_as_ret: 0x1808
-  __TEXT.__swift_as_cont: 0x2e58
-  __TEXT.__oslogstring: 0x6c67
+  __TEXT.__cstring: 0xa5941
+  __TEXT.__const: 0x19d104
+  __TEXT.__swift5_typeref: 0x2a466
+  __TEXT.__swift5_reflstr: 0x3d4f8
+  __TEXT.__swift5_assocty: 0xea68
+  __TEXT.__swift5_fieldmd: 0x5d8e0
+  __TEXT.__constg_swiftt: 0x62a2c
+  __TEXT.__swift5_protos: 0x1220
+  __TEXT.__swift5_proto: 0x9c2c
+  __TEXT.__swift5_types: 0x5fc8
+  __TEXT.__swift5_types2: 0xc0
+  __TEXT.__swift5_builtin: 0x2760
+  __TEXT.__swift5_capture: 0x3558
+  __TEXT.__objc_methtype: 0x2f6
+  __TEXT.__swift5_mpenum: 0xc34
+  __TEXT.__swift_as_entry: 0x168c
+  __TEXT.__swift_as_ret: 0x18ac
+  __TEXT.__swift_as_cont: 0x2f94
+  __TEXT.__oslogstring: 0x6ee7
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__info_plist: 0x4f6
+  __TEXT.__info_plist: 0x4fc
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0
   __TEXT.__swift5_replace: 0x0
   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x0
   __TEXT.__chain_fixups: 0x128
-  __TEXT.__eh_frame: 0x74fdc
+  __TEXT.__eh_frame: 0x77318
   __DATA.__TIGHTBEAM_VT: 0x1200
   __DATA.__TIGHTBEAM: 0x4a8
-  __DATA.__const: 0xe1a28
-  __DATA.__data: 0x4ed68
+  __DATA.__const: 0xe3a38
+  __DATA.__data: 0x4fa28
   __DATA.__mod_init_func: 0x40
-  __DATA.__ENDPOINTS: 0x1b7b4
-  __DATA.__auth_ptr: 0x7488
+  __DATA.__ENDPOINTS: 0x1bcd7
+  __DATA.__auth_ptr: 0x75a0
   __DATA.__DEVICETREE: 0x30
   __DATA.__shared_cache: 0x3b8
   __DATA.__DARTS: 0x93f

   __DATA.__mod_term_func: 0x0
   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x30
-  __DATA.__bss: 0x24aa0
-  __DATA.__common: 0x28a1
+  __DATA.__bss: 0x24ad0
+  __DATA.__common: 0x2971
   __PDATA.__auth_ptr: 0x280
-  __PDATA.__const: 0x67b0
+  __PDATA.__const: 0x6810
   __PDATA.__objc_imageinfo: 0x8
   __PDATA.__mod_init_func: 0x18
   __PDATA.__data: 0x2af0
   __PDATA.__ENDPOINTS: 0x838
   __PDATA.__shared_cache: 0x70
-  __PDATA.__bss: 0xba48
+  __PDATA.__bss: 0xbae8
   __PDATA.__common: 0x2578
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  Functions: 47342
+  Functions: 47768
   Symbols:   1
-  CStrings:  15063
+  CStrings:  15221
 
CStrings:
+ "  Quick start = "
+ " - Secure M3's cursor init has never run this power cycle, so "
+ " DisplayManager is not configured!"
+ " but a session is already active!"
+ " but startTimestampUS is nil!"
+ " bytes) — DART panics will occur if hardware accesses beyond "
+ " bytes, expected "
+ " could not be committed, holding the mapping"
+ " deferrals(hwBusy)="
+ " deferrals(pipelineBusy)="
+ " did not ask for an ack"
+ " exceeds the highest instance SEP can track ("
+ " for Storage exclave"
+ " gateEarlyRejects="
+ " gateExemptedBuffers="
+ " is not 'SCLD' 0x"
+ " is not a valid integer: "
+ " is still parked, keeping "
+ " lastVerdictAge="
+ " message to SEP. ane_id: "
+ " not acked after "
+ " opted into prefers-waiting-through-sleep, blocking: "
+ " parked request(s) with mappers disabled; they will submit against unmapped DART state"
+ " parking until sleep cycle completes, parked: "
+ " rejected before IO prep. SleepCycle: "
+ " requested, not waiting for the ack"
+ " sclCursorSupported "
+ " skipped, Secure M3 DMEM is not accessible"
+ " still published, "
+ " succeeded for ane_id "
+ " to ungated flush"
+ " will start once sensor sessions are resumed"
+ "$JgANEExclaveComponent.ANEExclave.init(_:driverUpcalls:aneUpcalls:_:oslog:ANEStorageService:ANEStorageSegAccess:ANEXNUContentReader:SEPControlEndpoint:ANEId:ANEDevelopmentModeEnabled:ANEFWTrustedCompartmentExists:ANEIsoIDSegAccess:ANEClientEXRegionSegAccess:ANEEXSurfaceRootSegAccess:ANEEXSurfaceRootService:)"
+ "$JgExclaveSEPManager.ExclaveSEPANEControlEndpoint"
+ "%s(%zu): failed to delete delta scratch RO span slot"
+ "%s(%zu): failed to delete delta scratch RO temp cap"
+ "%s(%zu): failed to map frame into delta scratch RO span"
+ ") < rampUp startTs ("
+ "), default health back to good"
+ "), deferring DART unmap"
+ "), the SCL cursor is inert "
+ "), this should never happen!"
+ ", Secure M3 cannot ack"
+ ", nextSubCheck @ "
+ ", parking mapping dva "
+ ", priorFiltered="
+ ", the region cannot fetch"
+ ".failureNoFilteredIB"
+ ".failureRampUpNoProgress(checkType="
+ ".failureTimestampUnderflow"
+ ".failureTimestampUnderflow(lhs="
+ ".rampUp(start @ "
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.MacOSX.platform/Developer/SDKs/ExclaveCore.MacOSX27.2.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.MacOSX.platform/Developer/SDKs/ExclaveCore.MacOSX27.2.Internal.sdk/System/ExclaveCore/usr/local/standalone/RTKit/usr/include/protocols/mbi_tightbeam_protocol.h"
+ "430.40.6"
+ ": initiating upcall (notification ID: "
+ ": notification done"
+ ": panicking to prevent MTE tag brute-forcing"
+ "; not submitting request "
+ "; nothing to release"
+ "; using no-op control"
+ "; will retry on the next 1->0 edge"
+ "@(#)VERSION:ExclaveOS Image4 Framework Version 7.0.0: Wed Oct  7 23:02:23 PDT 2026; root:AppleImage4_exclavecore-374~19426/ExclaveImage4/RELEASE_ARM64E"
+ "ANE power op returned unknown status byte: "
+ "ANEExclave version: ANEExclave_exclavecore-13.102.1"
+ "ANEExclaveComponent/ANEExclave.swift"
+ "Active pause requests: "
+ "Adding pause request: "
+ "Applying MTE backoff of "
+ "B16@?0^{vas_core_span={?=CQQCCCCC^vQ}iC[3C]{?=^?^?^?}^vQQ^{vas_core_vas}^{vas_core_span}^{vas_core_span}Q^{vas_segment}{spanmap_struct=b2b4b22b36}{_liblibc_mtx=[16C]}B{?=^{vas_core_span}^^{vas_core_span}}{spanmap_struct=b2b4b22b36}}8"
+ "BUG IN LIBTRACE: log payload "
+ "Build Date: Wed Oct  7 22:26:45 PDT 2026"
+ "Builtin.Borrow is not supported in runtime type lookup"
+ "Bundle metadata for "
+ "CompanionHandler: "
+ "CompanionHandler: %s: failed: %s"
+ "CompanionHandler: %s: initiating upcall (notification ID: %u)"
+ "CompanionHandler: %s: notification done"
+ "CompanionHandler: setupPowerDownAsyncSignal: setup done for ID: "
+ "CompanionHandler: setupPowerDownAsyncSignal: setup done for ID: %u"
+ "CompanionHandler: setupPowerUpAsyncSignal: setup done for ID: "
+ "CompanionHandler: setupPowerUpAsyncSignal: setup done for ID: %u"
+ "Conclave MTE tag check fault: esr="
+ "Deferred XnuContent unwire failed for skFileRefId: 0x"
+ "Deferred power on for ANEEngine from "
+ "Deferring XnuContent unwire for skFileRefId: 0x"
+ "ENABLED via driver opt-in"
+ "ERROR DMEM write refused ("
+ "ERROR a mapping is already parked, dropping the request to park "
+ "ERROR base lo 0x"
+ "ERROR mapping returned dva 0, Region 3 will stay off"
+ "ERROR nil ImageBuffer, nothing published, keeping seq "
+ "ERROR no Secure M3 HAL, keeping the base already published"
+ "ERROR refusing to publish, mapping dva "
+ "Empty value of bundle metadata "
+ "ExclaveOS Image4 Framework Version 7.0.0: Wed Oct  7 23:02:23 PDT 2026; root:AppleImage4_exclavecore-374~19426/ExclaveImage4/RELEASE_ARM64E"
+ "ExclaveSISP-6.105"
+ "FaceLivelinessFull"
+ "Failed to get frames from region "
+ "Failed to request full wake: "
+ "I14@?0{easm_space_unmapxnucontentregionwithflags__result_s=C(?={easm_failure_s=CS})}8"
+ "I28@?0Q8I16@?<I@?{easm_space_unmapxnucontentregionwithflags__result_s=C(?={easm_failure_s=CS})}>20"
+ "Ignoring duplicate pause request: "
+ "Ignoring pause request due to non-enforcing mode: "
+ "Ignoring pause request since ISP watchdog is disabled: "
+ "Ignoring pause request since health checks are disabled: "
+ "In-flight HW or pipeline requests present (pipeline: "
+ "Initialized count must be in 0 ... unsafeUninitializedCapacity."
+ "Invalid key value while decoding result type for createAssertion"
+ "Invalid key value while decoding result type for getDeviceLockInfo"
+ "Invalid key value while decoding result type for hold_ane_power_assertion"
+ "Invalid key value while decoding result type for releaseAssertion"
+ "Invalid key value while decoding result type for release_ane_power_assertion"
+ "Invalid key value while decoding result type for unloadMemoryWithFlags"
+ "Invalid key value while decoding result type for unloadWithFlags"
+ "Invalid key value while decoding result type for updateXnuContentWithFlags"
+ "Invalid log level "
+ "Log payload exceeds "
+ "MTE tag check fault #"
+ "No SEP power assertion held for aneId "
+ "One initializer to rule them all, with SEP power control for ANE"
+ "Park-through-sleep "
+ "ParkThroughSleep enabled: "
+ "PatchKeypointTracker"
+ "Quick start policy resolved @ GLTB "
+ "Quick start policy violated @ GLTB "
+ "Removed pause request: "
+ "Resuming ANEEngine to service existing clients from "
+ "SCA: skipping algo (Jindo Animation: indicator not yet at steady size, currSize < steadySize)"
+ "SCA: skipping algo (Jindo Animation: indicator not yet drawn, currSize == 0)"
+ "SCL: Cursor surface re-map after power on"
+ "SCL: cursor DMEM write refused"
+ "SCL: cursor ack timeout"
+ "SCL: nil buffer for cursor surface"
+ "SEP assertion refused, async request "
+ "SEP assertion refused, cached procedure "
+ "SEP assertion refused, leaving request "
+ "SEP assertion refused, sync request "
+ "SEP power assertion refused for ANE"
+ "SEP power assertions disabled for this instance"
+ "SEP power control wired but SoC type is unknown; disabling SEP reset lockout"
+ "SEP power-assertion enforcement "
+ "SEP power-assertion hold status "
+ "SEP power-assertion release non-ok status "
+ "SEP reset lockout not supported on "
+ "SEP reset protection "
+ "SEP reset protection enabled: "
+ "SEP reset protection requested but no SEP control is wired on this part"
+ "SM3 debug block absent: layout 0x"
+ "SM3 debug layout 0x"
+ "SetLogLevelFromBundle()"
+ "SleepCycle parked requests: "
+ "SleepCycle pipeline count: "
+ "SleepCycle totals: parks="
+ "Start not allowed: camera disabled by EDT policy"
+ "Starting quick start policy @ GLTB "
+ "Status not allowed: camera disabled by EDT policy"
+ "Storage service using v1 sharedmem"
+ "StorageExclaveComponent/XRTBundleResources.swift"
+ "System/ExclaveKit/System/Library/Frameworks/Vision.framework/faceliveliness_ek_fp16.bundle/*.bundle/main/main_ane"
+ "System/ExclaveKit/System/Library/Frameworks/Vision.framework/facelivelinessfull_ek_fp16.bundle/*.bundle/main/main_ane"
+ "System/ExclaveKit/System/Library/PrivateFrameworks/ODTL.framework/PhoneTracking/odtl/0/0/PatchKeypointTracker.bundle/*.bundle/main/main_ane"
+ "System/ExclaveKit/System/Library/PrivateFrameworks/ODTL.framework/PhoneTracking/odtl/ObjectDetector.bundle/*.bundle/main/main_ane"
+ "System/ExclaveKit/System/Library/PrivateFrameworks/Visage.framework/VGUnifiedLightingH5Models.bundle/img_to_sg_exclave_model.bundle/*.bundle/main/main_ane"
+ "TB_FATAL: invalid result returned from unmapXnuContentRegionWithFlags (%s:%d)\n"
+ "Unexpected L4_Error: %s(%zu) err='L4_Cap_Delete(scratch->ro_span_slot)'"
+ "Unexpected L4_Error: %s(%zu) err='L4_Cap_Delete(scratch->ro_temp_slot)'"
+ "Unexpected L4_Error: %s(%zu) err='_map_this_frame_readonly(scratch->ro_span, (uintptr_t)ro_words, scratch->ro_temp_slot)'"
+ "Unwiring XnuContent (deferred, ungated) for skFileRefId: 0x"
+ "VIOLATION: CIL never came on during quick start policy"
+ "Wed Oct  7 23:49:18 PDT 2026"
+ "[AppleKeyStoreManager] getDeviceLockInfo: unexpected nil derOut"
+ "[BrightnessCheck] NOT EVALUATED ("
+ "[BrightnessCheck][PowerOnDefaultHealth] Display power on, default health is bad until EXBright reports (max "
+ "[BrightnessCheck][PowerOnDefaultHealth] EXBright report received (health="
+ "[LogServer] error: "
+ "[SecureM3Handler] ERROR firmware load failed"
+ "[SecureM3Handler] MCPU power "
+ "[SecureM3Handler] MCPU power %ld -> %ld"
+ "[StrictMode] .rampUp -> .steady"
+ "[StrictMode] Can't use pre-wake MIB. Reporting failure."
+ "[StrictMode] Disabling (enabledTs="
+ "[StrictMode] Enabling (ts="
+ "[StrictMode] Healthy. Disabling. MIB="
+ "[VAS abort in function %s at line %d] [%s] could not allocate fixup span for fault handler\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] Could not depopulate temp span (drop): %s (0x%04hx)\n\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] _delta_page_against_original returned unexpected result(%p)\n"
+ "]\n  defaultDisplayChanged: triggered="
+ "] .rampUp -> .steady. Ctx: filteredNits="
+ "] .rampUp restart: start "
+ "] Failed to get filtered IB for rampUp, this should never happen! (items: "
+ "] In .rampUp, but currentMIB is nil. This should never happen!"
+ "])\n  deviceStateDisplayWake: allowance="
+ "])\n  quickStart: allowance="
+ "_delta_page_against_original"
+ "_insecure_random_buf"
+ "_os_log_payload_size(olp), OS_LOG_EXCLAVES_PAYLOAD_MAX"
+ "_wireXnuContentAndReadCaps called while holding the workLoop gate!!!"
+ "aligned, refusing to publish, keeping seq "
+ "applyFixups: rebase failed for %#lx (region %zd)"
+ "applyFixups: region %zd has NULL fixup_metadata_pointer"
+ "base not live (magic absent or never published), re-publishing at power-on"
+ "base_lo_valid clear at didPowerOff"
+ "base_lo_valid clear at power-on"
+ "base_lo_valid clear at teardown"
+ "base_lo_valid commit"
+ "clearRequestOffHardware not called with workLoop Gate held!"
+ "clearing base_lo_valid"
+ "clientSessionHint(client:model:args:) Cycles: "
+ "clientSetPowerHint(client:model:keepPowered:) Cycles: "
+ "control block cleared, valid 0 seq 0, ack cleared "
+ "delta_output != fault->write_buffer"
+ "didPowerOff with Secure M3 DMEM inaccessible, leaving the control block alone"
+ "didPowerOff with seq "
+ "disabled (default)"
+ "display power-off"
+ "doPowerDownAsyncSignal"
+ "doPowerUpAsyncSignal"
+ "failed to set storage window: "
+ "flushPendingXnuUnwires called while holding the workLoop gate!!!"
+ "for this session, nothing was published"
+ "fpwm-frequency-hz"
+ "getBundleMetadata(_:)"
+ "getDeviceLockInfo threw an unexpected error type "
+ "getRegionCap(idx:regionId:capId:)"
+ "hold_ane_power_assertion threw an unexpected error type"
+ "i24@?0^{?=^{thread}}8^{thread={allocation=^{allocation_map}{?=s}{?=AC}^{allocation}}QCQQQ^{?}(?={?=^{thread}^^{thread}}{heap_element=^{?}{?=^{thread}}{?=^{thread}}Q})^{turnstile}{?={?=CQ}Q}QQQ{inherit_set=^{turnstile}}{?={?=s}Q}QQQCS}16"
+ "invalid rawValue for ExclaveSEPANEControlEndpoint.Selector "
+ "invalid rawValue for SensorPauseReason: "
+ "invalid rawValue for XnuContentANEFlags: unexpected bits in value, "
+ "invalid rawValue for XnuContentUnloadFlags: unexpected bits in value, "
+ "load-failure XnuContent unwire attempted while holding the workLoop gate!!!"
+ "magic / base_hi / len"
+ "magic absent, forcing the full header rewrite so the block is gated again"
+ "malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:982)"
+ "malloc assertion \"!memtag_config.tag_data\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8903)"
+ "malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8331)"
+ "malloc assertion \"allocation_front_count == 2\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7872)"
+ "malloc assertion \"old_size\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:6854)"
+ "malloc assertion \"success\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:2216)"
+ "malloc assertion \"success\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:5356)"
+ "mapping(s) still held at didPowerOff, waiting for display power-off before handing them back"
+ "markRequestOnHardware not called with workLoop Gate held!"
+ "missing firmware engine"
+ "ms\n  displayPower: triggered="
+ "ms, lastFiltered="
+ "nits preserved (MIB="
+ "nits, currentFiltered="
+ "nits, expectedGrowth="
+ "notifyPowerStateToCompanion: no notification handler registered"
+ "notifyPowerStateToCompanion: powerUp:"
+ "notifyPowerStateToCompanion: powerUp:%{bool}d upcall took %fus"
+ "ns before launch"
+ "ns before next launch"
+ "octopus_no_quick_start"
+ "octopus_quick_start"
+ "olp->olp_tpb.tp_size, OS_LOG_EXCLAVES_TRACEPOINT_HDR_SIZE"
+ "pipe has stopped"
+ "policy-sil-disable"
+ "publishing WITHOUT waiting for an ack: Secure M3 has no descriptor (init has not run, or it gave up on SpareConfig), so no ack can arrive and a wait would only burn the timeout and park the mapping"
+ "quick-start-allowance"
+ "readback ctrl 0x"
+ "releaseFrameToXnu(_:using:)"
+ "releasePipelineReservation not called with workLoop Gate held!"
+ "release_ane_power_assertion threw an unexpected error type"
+ "releasing cursor mapping(s) at "
+ "releasing parked mapping dva "
+ "s[0] || s[1]"
+ "setSurfaceForCursor id "
+ "sharedmem_framemap_getPhysicalAddress"
+ "sharedmem_framemap_setMapped_delta"
+ "sil-disable-config"
+ "sil-disable-offset"
+ "sllt"
+ "slma"
+ "slmu"
+ "slpa"
+ "slpu"
+ "sls"
+ "takePipelineReservation called twice for request "
+ "takePipelineReservation not called with workLoop Gate held!"
+ "teardown requested with the display up, Region 3 may still composite over the black frame for a frame"
+ "there are no counters to read. Nothing below would be data."
+ "total_memory_usage_bytes"
+ "unexpected error retyping page "
+ "unload(refId:startFrame:n:flags:)"
+ "unloadWithFlags threw an unexpected error type"
+ "unmapXnuContentRegionWithFlags"
+ "updateXnuContent(refId:ranges:flags:)"
+ "us, unmapping old surface"
+ "v14@?0{easm_space_unmapxnucontentregionwithflags__result_s=C(?={easm_failure_s=CS})}8"
+ "v24@?0{sharedmem_pagerange=QQ}8"
+ "valid clear before base_hi / len"
+ "vas__easm_unmap_xnu_content_region_with_flags"
+ "vas_return_code(drop_depop) != VAS_SUCCESS"
+ "waitForSleepCycleCompletion not called with workLoop Gate held!"
+ "writeFileInternal(client:catInfo:name:offset:length:encrypted:inputBuffer:)"
+ "x, actualGrowth="
+ "{?=[2Q]}20@?0Q8I16"
- "\nANEEngineBufferDescriptor Summary\n===\nValid    : "
- "\nAneEngineBarInfo Summary\n===\nBARID : "
- "\nAneEngineSegmentProperty Summary\n===\nIndex     : "
- " (never registered)"
- " already configured"
- " already registered"
- " and is a State IO "
- " bytes from SecureStorage"
- " bytes mapped (expected "
- " for liveInParam["
- " from input buffer for liveInParam["
- " invoking memory manager for tracking EXSurface"
- " not referenced by BAR table, skipping"
- " proceeding with submission"
- " request completed, total: "
- " split kernel section(s)"
- " split kernel section(s): "
- " with bufferIndex="
- " → bufferIndex="
- "$JgStorageExclaveComponent.StorageExclaveComponent.init(newStorageUpcalls:xnuStorage:keyStorage:seg1:seg2:seg3:seg4:seg5:seg6:seg7:seg8:seg9:seg10:seg11:seg12:seg13:seg14:seg15:seg16:seg17:seg18:seg19:seg20:seg21:seg22:seg23:seg24:seg25:seg26:seg27:seg28:seg29:seg30:seg31:seg32:seg33:seg34:seg35:seg36:seg37:seg38:seg39:seg40:seg41:seg42:seg43:seg44:seg45:seg46:seg47:seg48:seg49:seg50:seg51:seg52:seg53:seg54:seg55:seg56:seg57:seg58:seg59:seg60:seg61:seg62:seg63:seg64:seg65:seg66:seg67:seg68:seg69:seg70:seg71:seg72:seg73:seg74:seg75:seg76:seg77:seg78:seg79:seg80:)"
- ", DebugLogEvents: "
- ", Last increase: "
- ", lastIncreasedIB="
- ", offset in MachO: "
- ".failureRampUpBrightnessBelowStartIB(startIB="
- ".failureRampUpBrightnessDecreased(startIB="
- ".failureRampUpNoProgress(lastIncreasedIB="
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.MacOSX.platform/Developer/SDKs/ExclaveCore.MacOSX27.0.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.MacOSX.platform/Developer/SDKs/ExclaveCore.MacOSX27.0.Internal.sdk/System/ExclaveCore/usr/local/standalone/RTKit/usr/include/protocols/mbi_tightbeam_protocol.h"
- "430.0.5"
- "@(#)VERSION:ExclaveOS Image4 Framework Version 7.0.0: Sat Aug  8 15:53:53 PDT 2026; root:AppleImage4_exclavecore-374~17266/ExclaveImage4/RELEASE_ARM64E"
- "ANEExclave version: ANEExclave_exclavecore-13.18.1"
- "Allocating context "
- "B16@?0^{vas_core_span={?=CQQCCCCC^vQ}iC[3C]{?=^?^?}^vQQ^{vas_core_vas}^{vas_core_span}^{vas_core_span}Q^{vas_segment}{spanmap_struct=b2b4b22b36}{_liblibc_mtx=[16C]}B{?=^{vas_core_span}^^{vas_core_span}}{spanmap_struct=b2b4b22b36}}8"
- "BAR entry usage:"
- "BAR entry: type="
- "BUG IN LIBTRACE: Received a BATCH_ERROR while creating a LogBatch"
- "Build Date: Sat Aug  8 14:40:58 PDT 2026"
- "CONST section at offset "
- "CacheRequestID: "
- "Clearing pending trigger for cached procedure "
- "Created DMA mapping at offset: "
- "Creating BufMemoryObject (heap-backed) uuid="
- "Creating XnuContentMemoryObject (XNU-backed) uuid="
- "DART panics will occur if hardware accesses beyond "
- "DMA mapping validated: "
- "Deferred power on for ANEEngine"
- "Deinit for ANEModel with identifier "
- "Destroying EXSurfaceObject "
- "Destroying MemoryObject "
- "Destroying SharedMemoryObject "
- "Destroying XnuContentMemoryObject "
- "Directory not present (probe): "
- "Done: Unloaded XnuContent for skFileRefId: "
- "ExclaveOS Image4 Framework Version 7.0.0: Sat Aug  8 15:53:53 PDT 2026; root:AppleImage4_exclavecore-374~17266/ExclaveImage4/RELEASE_ARM64E"
- "ExclaveSISP-6.20"
- "FW allocated cacheRequestHandle "
- "Firmware handle for the model: "
- "Firmware returned cacheRequestID "
- "Firmware returned program ID "
- "Firwmare buffer "
- "Freeing request "
- "Going to look for "
- "IO index for liveInParam "
- "In-flight HW requests present, deferring DART unmap"
- "Initialized count set to greater than specified capacity."
- "Kext Query token: "
- "LiveInParam operation["
- "Load Program Section: "
- "Logging section info agains ADDR: "
- "Mapping L2 spill buffer for the firmware EC for priority: "
- "Name: __bss, Size "
- "Offset in file: "
- "Overall output size to send to firmware "
- "Overall size to send to firmware "
- "Parsing section "
- "Part of IO fragment with startOffset "
- "Program MCache size: "
- "RTGraph procedure "
- "Resuming ANEEngine to service existing clients"
- "SCL: Buffer mapping failed for cursor surface"
- "SCL: Cursor address programmed "
- "Sat Aug  8 16:48:36 PDT 2026"
- "Section addr field "
- "Set resizable mapped range of size "
- "Signaling completion for "
- "Signaling completion with failure for "
- "Split kernel barSetup: barId="
- "Split kernel buffer: bufferIndex="
- "Split kernel entry "
- "Type: LiveInParam "
- "Type: Single Plane Linear "
- "Unexpected error type in allocate: "
- "Unloading XnuContent failed for skFileRefId: "
- "Unloading XnuContent for skFileRefId: "
- "Unloading program "
- "Unmapping L2 spill buffer for ANEEngine for priority "
- "Unsupported IO type!"
- "Unsupported type for input"
- "Unsupported type for output"
- "Updating BAR info for "
- "Updating request "
- "[B] Start Siri dark wake policy"
- "[B] Stop Siri dark wake policy"
- "] Cannot estimate ramp duration, invalid target brightness value: "
- "] Switched to MIB ramp up mode during brightness ramp down, ignoring this frame."
- "][healthCheckMode] .rampUp -> .steady. Ctx: adjustedIBNitsFiltered="
- "_os_log_payload_size(olp), OS_LOG_PAYLOAD_HARD_MAX_SIZE"
- "allocate(page:from:using:)"
- "allocateSectionBuffer kernel: uuid="
- "allocateSectionBuffer text: uuid="
- "and is of type FVMLIB"
- "bufferSymbolName: "
- "could not retype "
- "delete(frame:using:)"
- "has a vaid ANE thread binding "
- "i24@?0^{?=^{thread}}8^{thread={allocation=^{allocation_map}{?=s}{?=AC}^{allocation}}QCQQQ^{?}(?={?=^{thread}^^{thread}}{heap_element=^{?}{?=^{thread}}{?=^{thread}}Q})^{turnstile}{?={?=CQ}Q}QQQ{inherit_set=^{turnstile}}{?={?=s}{?=s}}QQQCS}16"
- "intermediateSection"
- "localmap_map(%zx): localmap() remap with changed PA (%llx != %llx)\n"
- "malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:981)"
- "malloc assertion \"!memtag_config.tag_data\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8865)"
- "malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8293)"
- "malloc assertion \"allocation_front_count == 2\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7834)"
- "malloc assertion \"old_size\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:6830)"
- "malloc assertion \"success\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:2197)"
- "malloc assertion \"success\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:5336)"
- "nits, elapsedWithoutIBIncrease="
- "olp->olp_tpb.tp_size, OS_LOG_PAYLOAD_HDR_SIZE"
- "paramSymbolName: "
- "populateProgramSectionDVAs: kernel DVA=0x"
- "populateProgramSectionDVAs: splitKernel["
- "populateProgramSectionDVAs: text DVA=0x"
- "sendRequestToFirmware priority: "
- "sharedmem_framemap_getPhysicalAddresses"
- "sharedmem_framemap_setMapped"
- "splitKernelSections count="
- "total_memory_kib"
- "unload(refId:startFrame:n:)"
- "v14@?0{easm_space_unmapxnucontentregion__result_s=C(?={easm_failure_s=CS})}8"
- "vas__easm_unmap_xnu_content_region"
- "writeFileInternal(client:catInfo:name:offset:length:encrypted:)"
```
