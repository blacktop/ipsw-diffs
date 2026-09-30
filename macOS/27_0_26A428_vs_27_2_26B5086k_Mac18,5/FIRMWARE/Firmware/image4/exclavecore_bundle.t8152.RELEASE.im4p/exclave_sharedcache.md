## exclave_sharedcache

> `Firmware/image4/exclavecore_bundle.t8152.RELEASE.im4p/exclave_sharedcache`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_entry`
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
-  __TEXT.__text: 0xcec338
+1777.40.24.501.1
+  __TEXT.__text: 0xd00bc0
   __TEXT.__lcxx_override: 0xd0
-  __TEXT.__cstring: 0xa0c31
-  __TEXT.__const: 0x1986f4
-  __TEXT.__swift5_typeref: 0x287a0
-  __TEXT.__swift5_reflstr: 0x394e8
-  __TEXT.__swift5_assocty: 0xe1a0
-  __TEXT.__swift5_fieldmd: 0x5a944
-  __TEXT.__constg_swiftt: 0x5eaac
-  __TEXT.__swift5_protos: 0x113c
-  __TEXT.__swift5_proto: 0x95c4
-  __TEXT.__swift5_types: 0x5c98
-  __TEXT.__swift5_types2: 0xb8
-  __TEXT.__swift5_builtin: 0x265c
-  __TEXT.__swift5_capture: 0x3474
-  __TEXT.__objc_methtype: 0x2b6
-  __TEXT.__swift5_mpenum: 0xb54
-  __TEXT.__swift_as_entry: 0x1600
-  __TEXT.__swift_as_ret: 0x1804
-  __TEXT.__swift_as_cont: 0x2e44
-  __TEXT.__oslogstring: 0x6c57
+  __TEXT.__cstring: 0xa1961
+  __TEXT.__const: 0x19a5e4
+  __TEXT.__swift5_typeref: 0x28ac0
+  __TEXT.__swift5_reflstr: 0x3aaf8
+  __TEXT.__swift5_assocty: 0xe5a8
+  __TEXT.__swift5_fieldmd: 0x5b980
+  __TEXT.__constg_swiftt: 0x5f6c8
+  __TEXT.__swift5_protos: 0x1150
+  __TEXT.__swift5_proto: 0x9770
+  __TEXT.__swift5_types: 0x5d68
+  __TEXT.__swift5_types2: 0xbc
+  __TEXT.__swift5_builtin: 0x2698
+  __TEXT.__swift5_capture: 0x34d8
+  __TEXT.__objc_methtype: 0x2d6
+  __TEXT.__swift5_mpenum: 0xb6c
+  __TEXT.__swift_as_entry: 0x1634
+  __TEXT.__swift_as_ret: 0x184c
+  __TEXT.__swift_as_cont: 0x2ed0
+  __TEXT.__oslogstring: 0x6cb7
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0
   __TEXT.__swift5_replace: 0x0
   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x0
-  __TEXT.__chain_fixups: 0x120
-  __TEXT.__eh_frame: 0x72bcc
+  __TEXT.__chain_fixups: 0x128
+  __TEXT.__eh_frame: 0x743ec
   __DATA.__TIGHTBEAM_VT: 0x11a0
   __DATA.__TIGHTBEAM: 0x490
-  __DATA.__const: 0xe3748
-  __DATA.__data: 0x4bed0
+  __DATA.__const: 0xe4ff0
+  __DATA.__data: 0x4c840
   __DATA.__mod_init_func: 0x40
-  __DATA.__ENDPOINTS: 0x1b7b4
-  __DATA.__auth_ptr: 0x5ec8
+  __DATA.__ENDPOINTS: 0x1bbd0
+  __DATA.__auth_ptr: 0x5fa8
   __DATA.__DEVICETREE: 0x30
   __DATA.__shared_cache: 0x3b8
   __DATA.__DARTS: 0x93f

   __DATA.__mod_term_func: 0x0
   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x30
-  __DATA.__common: 0x24e1
+  __DATA.__common: 0x25a1
   __PDATA.__auth_ptr: 0x280
-  __PDATA.__const: 0x67b0
+  __PDATA.__const: 0x6800
   __PDATA.__objc_imageinfo: 0x8
   __PDATA.__mod_init_func: 0x18
   __PDATA.__data: 0x2af0

   __PDATA.__common: 0x2578
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  Functions: 1360
+  Functions: 1361
   Symbols:   1
-  CStrings:  14837
+  CStrings:  14885
 
CStrings:
+ "  Quick start = "
+ " - Secure M3's cursor init has never run this power cycle, so "
+ " bytes) — DART panics will occur if hardware accesses beyond "
+ " bytes, expected "
+ " could not be committed, holding the mapping"
+ " did not ask for an ack"
+ " exceeds the highest instance SEP can track ("
+ " is not 'SCLD' 0x"
+ " is still parked, keeping "
+ " message to SEP. ane_id: "
+ " not acked after "
+ " requested, not waiting for the ack"
+ " sclCursorSupported "
+ " skipped, Secure M3 DMEM is not accessible"
+ " still published, "
+ " succeeded for ane_id "
+ " to ungated flush"
+ " will start once sensor sessions are resumed"
+ "$JgANEExclaveComponent.ANEExclave.init(_:driverUpcalls:aneUpcalls:_:oslog:ANEStorageService:ANEStorageSegAccess:ANEXNUContentReader:SEPControlEndpoint:ANEId:ANEDevelopmentModeEnabled:ANEFWTrustedCompartmentExists:ANEIsoIDSegAccess:ANEClientEXRegionSegAccess:ANEEXSurfaceRootSegAccess:ANEEXSurfaceRootService:)"
+ "$JgExclaveSEPManager.ExclaveSEPANEControlEndpoint"
+ "), the SCL cursor is inert "
+ ", Secure M3 cannot ack"
+ ", parking mapping dva "
+ ", the region cannot fetch"
+ ".failureNoFilteredIB"
+ ".failureTimestampUnderflow"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.MacOSX.platform/Developer/SDKs/ExclaveCore.MacOSX27.2.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.MacOSX.platform/Developer/SDKs/ExclaveCore.MacOSX27.2.Internal.sdk/System/ExclaveCore/usr/local/standalone/RTKit/usr/include/protocols/mbi_tightbeam_protocol.h"
+ "430.40.5"
+ "; not submitting request "
+ "; nothing to release"
+ "; will retry on the next 1->0 edge"
+ "@(#)VERSION:ExclaveOS Image4 Framework Version 7.0.0: Thu Sep  3 23:08:07 PDT 2026; root:AppleImage4_exclavecore-374~18265/ExclaveImage4/RELEASE_ARM64E"
+ "ANE power op returned unknown status byte: "
+ "ANEExclave version: ANEExclave_exclavecore-13.100.8"
+ "ANEExclaveComponent/ANEExclave.swift"
+ "Active pause requests: "
+ "Adding pause request: "
+ "Build Date: Thu Sep  3 22:41:50 PDT 2026"
+ "Deferred XnuContent unwire failed for skFileRefId: 0x"
+ "Deferring XnuContent unwire for skFileRefId: 0x"
+ "ERROR DMEM write refused ("
+ "ERROR a mapping is already parked, dropping the request to park "
+ "ERROR base lo 0x"
+ "ERROR mapping returned dva 0, Region 3 will stay off"
+ "ERROR nil ImageBuffer, nothing published, keeping seq "
+ "ERROR no Secure M3 HAL, keeping the base already published"
+ "ERROR refusing to publish, mapping dva "
+ "ExclaveOS Image4 Framework Version 7.0.0: Thu Sep  3 23:08:07 PDT 2026; root:AppleImage4_exclavecore-374~18265/ExclaveImage4/RELEASE_ARM64E"
+ "ExclaveSISP-6.103"
+ "Failed to get frames from region "
+ "Failed to request full wake: "
+ "I14@?0{easm_space_unmapxnucontentregionwithflags__result_s=C(?={easm_failure_s=CS})}8"
+ "I28@?0Q8I16@?<I@?{easm_space_unmapxnucontentregionwithflags__result_s=C(?={easm_failure_s=CS})}>20"
+ "Ignoring duplicate pause request: "
+ "Ignoring pause request due to non-enforcing mode: "
+ "Ignoring pause request since ISP watchdog is disabled: "
+ "Ignoring pause request since health checks are disabled: "
+ "Invalid key value while decoding result type for createAssertion"
+ "Invalid key value while decoding result type for getDeviceLockInfo"
+ "Invalid key value while decoding result type for hold_ane_power_assertion"
+ "Invalid key value while decoding result type for releaseAssertion"
+ "Invalid key value while decoding result type for release_ane_power_assertion"
+ "Invalid key value while decoding result type for unloadMemoryWithFlags"
+ "Invalid key value while decoding result type for unloadWithFlags"
+ "Invalid key value while decoding result type for updateXnuContentWithFlags"
+ "No SEP power assertion held for aneId "
+ "One initializer to rule them all, with SEP power control for ANE"
+ "Quick start policy resolved @ GLTB "
+ "Quick start policy violated @ GLTB "
+ "Removed pause request: "
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
+ "SEP power-assertion enforcement "
+ "SEP power-assertion hold status "
+ "SEP power-assertion release non-ok status "
+ "SM3 debug block absent: layout 0x"
+ "SM3 debug layout 0x"
+ "Starting quick start policy @ GLTB "
+ "Storage service using v1 sharedmem"
+ "TB_FATAL: invalid result returned from unmapXnuContentRegionWithFlags (%s:%d)\n"
+ "Unwiring XnuContent (deferred, ungated) for skFileRefId: 0x"
+ "VIOLATION: CIL never came on during quick start policy"
+ "[AppleKeyStoreManager] getDeviceLockInfo: unexpected nil derOut"
+ "]\n  defaultDisplayChanged: triggered="
+ "])\n  medinaStateDisplayWake: allowance="
+ "])\n  quickStart: allowance="
+ "_insecure_random_buf"
+ "_wireXnuContentAndReadCaps called while holding the workLoop gate!!!"
+ "aligned, refusing to publish, keeping seq "
+ "base not live (magic absent or never published), re-publishing at power-on"
+ "base_lo_valid clear at didPowerOff"
+ "base_lo_valid clear at power-on"
+ "base_lo_valid clear at teardown"
+ "base_lo_valid commit"
+ "clearRequestOffHardware not called with workLoop Gate held!"
+ "clearing base_lo_valid"
+ "control block cleared, valid 0 seq 0, ack cleared "
+ "didPowerOff with Secure M3 DMEM inaccessible, leaving the control block alone"
+ "didPowerOff with seq "
+ "display power-off"
+ "failed to set storage window: "
+ "flushPendingXnuUnwires called while holding the workLoop gate!!!"
+ "for this session, nothing was published"
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
+ "octopus_no_quick_start"
+ "octopus_quick_start"
+ "pipe has stopped"
+ "publishing WITHOUT waiting for an ack: Secure M3 has no descriptor (init has not run, or it gave up on SpareConfig), so no ack can arrive and a wait would only burn the timeout and park the mapping"
+ "quick-start-allowance"
+ "readback ctrl 0x"
+ "releaseFrameToXnu(_:using:)"
+ "release_ane_power_assertion threw an unexpected error type"
+ "releasing cursor mapping(s) at "
+ "releasing parked mapping dva "
+ "s[0] || s[1]"
+ "setSurfaceForCursor id "
+ "sllt"
+ "slma"
+ "slmu"
+ "slpa"
+ "slpu"
+ "sls"
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
+ "valid clear before base_hi / len"
+ "vas__easm_unmap_xnu_content_region_with_flags"
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
- ", offset in MachO: "
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.MacOSX.platform/Developer/SDKs/ExclaveCore.MacOSX27.0.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.MacOSX.platform/Developer/SDKs/ExclaveCore.MacOSX27.0.Internal.sdk/System/ExclaveCore/usr/local/standalone/RTKit/usr/include/protocols/mbi_tightbeam_protocol.h"
- "430.0.5"
- "@(#)VERSION:ExclaveOS Image4 Framework Version 7.0.0: Sat Aug  8 15:53:53 PDT 2026; root:AppleImage4_exclavecore-374~17266/ExclaveImage4/RELEASE_ARM64E"
- "ANEExclave version: ANEExclave_exclavecore-13.18.1"
- "Allocating context "
- "BAR entry usage:"
- "BAR entry: type="
- "Build Date: Sat Aug  8 14:40:58 PDT 2026"
- "CONST section at offset "
- "CacheRequestID: "
- "Clearing pending trigger for cached procedure "
- "Created DMA mapping at offset: "
- "Creating BufMemoryObject (heap-backed) uuid="
- "Creating XnuContentMemoryObject (XNU-backed) uuid="
- "DART panics will occur if hardware accesses beyond "
- "DMA mapping validated: "
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
- "SCL: Buffer mapping failed for cursor surface"
- "SCL: Cursor address programmed "
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
- "malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:981)"
- "malloc assertion \"!memtag_config.tag_data\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8865)"
- "malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8293)"
- "malloc assertion \"allocation_front_count == 2\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7834)"
- "malloc assertion \"old_size\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:6830)"
- "malloc assertion \"success\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:2197)"
- "malloc assertion \"success\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:5336)"
- "paramSymbolName: "
- "populateProgramSectionDVAs: kernel DVA=0x"
- "populateProgramSectionDVAs: splitKernel["
- "populateProgramSectionDVAs: text DVA=0x"
- "sendRequestToFirmware priority: "
- "splitKernelSections count="
- "total_memory_kib"
- "unload(refId:startFrame:n:)"
- "v14@?0{easm_space_unmapxnucontentregion__result_s=C(?={easm_failure_s=CS})}8"
- "vas__easm_unmap_xnu_content_region"
```
