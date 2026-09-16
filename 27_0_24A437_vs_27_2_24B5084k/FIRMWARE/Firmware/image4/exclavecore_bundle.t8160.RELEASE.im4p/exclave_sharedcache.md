## exclave_sharedcache

> `Firmware/image4/exclavecore_bundle.t8160.RELEASE.im4p/exclave_sharedcache`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_entry`
- `__TEXT.__chain_fixups`
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
-  __TEXT.__text: 0xf11a04
+1777.40.23.502.2
+  __TEXT.__text: 0xf35478
   __TEXT.__lcxx_override: 0xd0
-  __TEXT.__cstring: 0xb3971
-  __TEXT.__const: 0x204164
-  __TEXT.__swift5_typeref: 0x32542
-  __TEXT.__swift5_reflstr: 0x53698
-  __TEXT.__swift5_assocty: 0xfe50
-  __TEXT.__swift5_fieldmd: 0x8d96c
-  __TEXT.__constg_swiftt: 0x77b88
-  __TEXT.__swift5_protos: 0x14a4
-  __TEXT.__swift5_proto: 0xcad4
-  __TEXT.__swift5_types: 0x8390
-  __TEXT.__swift5_types2: 0xc0
-  __TEXT.__swift5_builtin: 0x2b98
-  __TEXT.__swift5_capture: 0x3b98
-  __TEXT.__objc_methtype: 0x536
-  __TEXT.__swift5_mpenum: 0xdc8
-  __TEXT.__swift_as_entry: 0x1634
-  __TEXT.__swift_as_ret: 0x1828
-  __TEXT.__swift_as_cont: 0x2e9c
-  __TEXT.__oslogstring: 0x7005
+  __TEXT.__cstring: 0xb52a1
+  __TEXT.__const: 0x207fe4
+  __TEXT.__swift5_typeref: 0x32b54
+  __TEXT.__swift5_reflstr: 0x551c8
+  __TEXT.__swift5_assocty: 0x102b8
+  __TEXT.__swift5_fieldmd: 0x8eea4
+  __TEXT.__constg_swiftt: 0x78dc0
+  __TEXT.__swift5_protos: 0x14c8
+  __TEXT.__swift5_proto: 0xccf0
+  __TEXT.__swift5_types: 0x84a8
+  __TEXT.__swift5_types2: 0xc4
+  __TEXT.__swift5_builtin: 0x2bc0
+  __TEXT.__swift5_capture: 0x3c0c
+  __TEXT.__objc_methtype: 0x556
+  __TEXT.__swift5_mpenum: 0xdc4
+  __TEXT.__swift_as_entry: 0x1668
+  __TEXT.__swift_as_ret: 0x1870
+  __TEXT.__swift_as_cont: 0x2f28
+  __TEXT.__oslogstring: 0x72f5
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0

   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x0
   __TEXT.__chain_fixups: 0x170
-  __TEXT.__eh_frame: 0x81600
-  __DATA.__TIGHTBEAM_VT: 0x1500
-  __DATA.__TIGHTBEAM: 0x588
-  __DATA.__const: 0x166540
-  __DATA.__data: 0x5f3a0
+  __TEXT.__eh_frame: 0x83494
+  __DATA.__TIGHTBEAM_VT: 0x1530
+  __DATA.__TIGHTBEAM: 0x590
+  __DATA.__const: 0x168588
+  __DATA.__data: 0x60320
   __DATA.__mod_init_func: 0x40
-  __DATA.__ENDPOINTS: 0x1b7b4
-  __DATA.__auth_ptr: 0xb740
+  __DATA.__ENDPOINTS: 0x1b9c2
+  __DATA.__auth_ptr: 0xb888
   __DATA.__DEVICETREE: 0x30
   __DATA.__shared_cache: 0x3b8
   __DATA.__DARTS: 0x93f

   __DATA.__mod_term_func: 0x0
   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x30
-  __DATA.__common: 0x5cf2
+  __DATA.__common: 0x5e02
   __PDATA.__auth_ptr: 0x280
-  __PDATA.__const: 0x67b0
+  __PDATA.__const: 0x6800
   __PDATA.__objc_imageinfo: 0x8
   __PDATA.__mod_init_func: 0x18
   __PDATA.__data: 0x2af0

   __PDATA.__common: 0x2578
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  Functions: 1451
+  Functions: 1452
   Symbols:   1
-  CStrings:  16706
+  CStrings:  16846
 
CStrings:
+ "  Quick start = "
+ " - Secure M3's cursor init has never run this power cycle, so "
+ " authenticAppleDisplay="
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
+ "$JgConclaveWakerComponent.ConclaveWakerComponent.init(upcall:powerManagement:)"
+ "$JgExclaveSEPManager.ExclaveSEPANEControlEndpoint"
+ "$JgIOPProximityValidation.IOPPeerProximity"
+ ") < rampUp startTs ("
+ "), the SCL cursor is inert "
+ "), this should never happen!"
+ ", Secure M3 cannot ack"
+ ", iopsOverride: "
+ ", nextSubCheck @ "
+ ", outbox msg_count="
+ ", parking mapping dva "
+ ", preferedEncoding: "
+ ", priorFiltered="
+ ", system DAK len = "
+ ", the region cannot fetch"
+ ".failureNoFilteredIB"
+ ".failureRampUpNoProgress(checkType="
+ ".failureTimestampUnderflow"
+ ".failureTimestampUnderflow(lhs="
+ ".rampUp(start @ "
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS27.2.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS27.2.Internal.sdk/System/ExclaveCore/usr/local/standalone/RTKit/usr/include/protocols/mbi_tightbeam_protocol.h"
+ "/device-tree/arm-io/smc/iop-smc-nub/smc-mogul"
+ "430.40.5"
+ "; not submitting request "
+ "; nothing to release"
+ "; will retry on the next 1->0 edge"
+ "@(#)VERSION:ExclaveOS Image4 Framework Version 7.0.0: Fri Sep  4 01:28:14 PDT 2026; root:AppleImage4_exclavecore-374~18270/ExclaveImage4/RELEASE_ARM64E"
+ "ANE power op returned unknown status byte: "
+ "ANEExclave version: ANEExclave_exclavecore-13.100.8"
+ "ANEExclaveComponent/ANEExclave.swift"
+ "Accessory timeout"
+ "Active pause requests: "
+ "Adding pause request: "
+ "All domain keys are up to date"
+ "Attempt to serialize IOPDomainKey without peerPubKey"
+ "Attempt to serialize IOPDomainKey without serializedRefKey"
+ "BUG IN LIBTRACE: log payload "
+ "Build Date: Wed Sep  9 20:44:59 PDT 2026"
+ "Can't read iop type from stream"
+ "Can't read peerPubKey"
+ "Can't serialize AKSRefKey: "
+ "Could not update a public key for domain: %u"
+ "Deferred XnuContent unwire failed for skFileRefId: 0x"
+ "Deferring XnuContent unwire for skFileRefId: 0x"
+ "DeviceInfoH19P: target "
+ "DeviceInfoH19P: target %s authenticAppleDisplay=%{bool}d (edtPath: %s)"
+ "Dropping unsoported public key type: %u"
+ "ERROR DMEM write refused ("
+ "ERROR a mapping is already parked, dropping the request to park "
+ "ERROR base lo 0x"
+ "ERROR mapping returned dva 0, Region 3 will stay off"
+ "ERROR nil ImageBuffer, nothing published, keeping seq "
+ "ERROR no Secure M3 HAL, keeping the base already published"
+ "ERROR refusing to publish, mapping dva "
+ "ExclaveCameraSISP-20.104.4"
+ "ExclaveOS Image4 Framework Version 7.0.0: Fri Sep  4 01:28:14 PDT 2026; root:AppleImage4_exclavecore-374~18270/ExclaveImage4/RELEASE_ARM64E"
+ "Failed to get frames from region "
+ "Failed to read domain key"
+ "Failed to read domain key count"
+ "Failed to read iop domain keys"
+ "Failed to request full wake: "
+ "I14@?0{easm_space_unmapxnucontentregionwithflags__result_s=C(?={easm_failure_s=CS})}8"
+ "I28@?0Q8I16@?<I@?{easm_space_unmapxnucontentregionwithflags__result_s=C(?={easm_failure_s=CS})}>20"
+ "Ignoring duplicate pause request: "
+ "Ignoring pause request due to non-enforcing mode: "
+ "Ignoring pause request since ISP watchdog is disabled: "
+ "Ignoring pause request since health checks are disabled: "
+ "Invalid PeerClass value "
+ "Invalid key value while decoding result type for createAssertion"
+ "Invalid key value while decoding result type for getDeviceLockInfo"
+ "Invalid key value while decoding result type for hold_ane_power_assertion"
+ "Invalid key value while decoding result type for releaseAssertion"
+ "Invalid key value while decoding result type for release_ane_power_assertion"
+ "Invalid key value while decoding result type for unloadMemoryWithFlags"
+ "Invalid key value while decoding result type for unloadWithFlags"
+ "Invalid key value while decoding result type for updateXnuContentWithFlags"
+ "Log payload exceeds "
+ "No SEP power assertion held for aneId "
+ "One initializer to rule them all, with SEP power control for ANE"
+ "Quick start policy canceled ("
+ "Quick start policy resolved @ GLTB "
+ "Quick start policy violated @ GLTB "
+ "Record does not contain domain keys"
+ "Removed pause request: "
+ "Requested iop keys: "
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
+ "SPR not found for peerId "
+ "Saving the client repository failed"
+ "SecurePairingCoreComponent/SecurePairingCore+Domain.swift"
+ "Skipping unsupported IOP key type: %u"
+ "Skipping unsupported IOP type: %u"
+ "Starting quick start policy @ GLTB "
+ "Storage service using v1 sharedmem"
+ "Stored domain keys contain unknow IOP type: %u"
+ "TB_FATAL: invalid result returned from unmapXnuContentRegionWithFlags (%s:%d)\n"
+ "TransferDataStream attempt to receive data in finished state"
+ "TransferDataStream attempt to send data in finished state"
+ "Unexpected iop type code "
+ "Unwiring XnuContent (deferred, ungated) for skFileRefId: 0x"
+ "Update domain keys, missing keys: "
+ "Updating provided keys based on peer response"
+ "VIOLATION: CIL never came on during quick start policy"
+ "Will provide keys for IOPs: "
+ "[AppleKeyStoreManager] getDeviceLockInfo: unexpected nil derOut"
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
+ "_wireXnuContentAndReadCaps called while holding the workLoop gate!!!"
+ "aligned, refusing to publish, keeping seq "
+ "base not live (magic absent or never published), re-publishing at power-on"
+ "base_lo_valid clear at didPowerOff"
+ "base_lo_valid clear at power-on"
+ "base_lo_valid clear at teardown"
+ "base_lo_valid commit"
+ "cancelDomainPairing threw an unexpected error type"
+ "clearRequestOffHardware not called with workLoop Gate held!"
+ "clearing base_lo_valid"
+ "control block cleared, valid 0 seq 0, ack cleared "
+ "didPowerOff with Secure M3 DMEM inaccessible, leaving the control block alone"
+ "didPowerOff with seq "
+ "display power-off"
+ "extractPublicKeys(from: "
+ "extractPublicKeys(from:)"
+ "extracted public keys for domains: "
+ "failed to set storage window: "
+ "flushPendingXnuUnwires called while holding the workLoop gate!!!"
+ "for this session, nothing was published"
+ "generateDomainKeys()"
+ "generateKey(for: "
+ "generateKey(for:)"
+ "getDeviceLockInfo threw an unexpected error type "
+ "getRegionCap(idx:regionId:capId:)"
+ "got key material: "
+ "handleDomainKeys -> "
+ "handleDomainKeys threw an unexpected error type"
+ "handleDomainKeys(pairingId: "
+ "handleDomainKeys(pairingId:bytes:)"
+ "handleDomainKeysAck -> "
+ "handleDomainKeysAck threw an unexpected error type"
+ "handleDomainKeysAck(pairingId: "
+ "handleDomainKeysAck(pairingId:bytes:)"
+ "handleMissingKeyTypes(peerIds: "
+ "handleMissingKeyTypesAck -> "
+ "handleMissingKeyTypesAck(pairingId: "
+ "handleMissingKeyTypesAck(pairingId:bytes:)"
+ "handleMissingKeyTypesCont -> "
+ "handleMissingKeyTypesCont(pairingId: "
+ "handleMissingKeyTypesCont(pairingId:bytes:)"
+ "handleMissingKeys -> "
+ "handleMissingKeys(bytes: "
+ "handleMissingKeys(context:bytes:)"
+ "handleStartKeyTransfer - no iops set to context before key transfer"
+ "handleStartKeyTransfer -> "
+ "handleStartKeyTransfer threw an unexpected error type"
+ "handleStartKeyTransfer(pairingId: "
+ "handleStartKeyTransfer(pairingId:)"
+ "hold_ane_power_assertion threw an unexpected error type"
+ "i24@?0^{?=^{thread}}8^{thread={allocation=^{allocation_map}{?=s}{?=AC}^{allocation}}QCQQQ^{?}(?={?=^{thread}^^{thread}}{heap_element=^{?}{?=^{thread}}{?=^{thread}}Q})^{turnstile}{?={?=CQ}Q}QQQ{inherit_set=^{turnstile}}{?={?=s}Q}QQQCS}16"
+ "inbox msg_count="
+ "invalid rawValue for ExclaveSEPANEControlEndpoint.Selector "
+ "invalid rawValue for SensorPauseReason: "
+ "invalid rawValue for TightbeamComponents.iopProximityValidationSelector "
+ "invalid rawValue for TransferEncoding: "
+ "invalid rawValue for XnuContentANEFlags: unexpected bits in value, "
+ "invalid rawValue for XnuContentUnloadFlags: unexpected bits in value, "
+ "iopProximityValidation"
+ "load-failure XnuContent unwire attempted while holding the workLoop gate!!!"
+ "magic / base_hi / len"
+ "magic absent, forcing the full header rewrite so the block is gated again"
+ "malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:982)"
+ "malloc assertion \"!memtag_config.tag_data\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8903)"
+ "malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8331)"
+ "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7872)"
+ "malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:6854)"
+ "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:2216)"
+ "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:5356)"
+ "mapping(s) still held at didPowerOff, waiting for display power-off before handing them back"
+ "markRequestOnHardware not called with workLoop Gate held!"
+ "missing firmware engine"
+ "ms\n  displayPower: triggered="
+ "ms, lastFiltered="
+ "nits preserved (MIB="
+ "nits, currentFiltered="
+ "nits, expectedGrowth="
+ "no payload should be here"
+ "octopus_medina_state_display_wake_allowance"
+ "octopus_no_quick_start"
+ "octopus_quick_start"
+ "olp->olp_tpb.tp_size, OS_LOG_EXCLAVES_TRACEPOINT_HDR_SIZE"
+ "pipe has stopped"
+ "publishing WITHOUT waiting for an ack: Secure M3 has no descriptor (init has not run, or it gave up on SpareConfig), so no ack can arrive and a wait would only burn the timeout and park the mapping"
+ "quick-start-allowance"
+ "readback ctrl 0x"
+ "received NACK, ackStatus: "
+ "releaseFrameToXnu(_:using:)"
+ "release_ane_power_assertion threw an unexpected error type"
+ "releasing cursor mapping(s) at "
+ "releasing parked mapping dva "
+ "s[0] || s[1]"
+ "setProvidedKeys(_:merge:)"
+ "setSurfaceForCursor id "
+ "sllt"
+ "slma"
+ "slmu"
+ "slpa"
+ "slpu"
+ "sls"
+ "startDomainPairing -> "
+ "startDomainPairing(clientClass:peerId:tag:encoding:iopsOverride:bytes:)"
+ "startDomainPairing(clientClass:peerId:tag:preferedEncoding:iopsOverride:)"
+ "startDomainPairing(peerIds: "
+ "storeDomainKeys()"
+ "storing new keys for domains: "
+ "storing original keys for domains: "
+ "teardown requested with the display up, Region 3 may still composite over the black frame for a frame"
+ "there are no counters to read. Nothing below would be data."
+ "total_memory_usage_bytes"
+ "unexpected error retyping page "
+ "unexpected payload size: %ld"
+ "unload(refId:startFrame:n:flags:)"
+ "unloadWithFlags threw an unexpected error type"
+ "unmapXnuContentRegionWithFlags"
+ "updateDomainKeys(iopsOverride: "
+ "updateDomainKeys(iopsOverride:)"
+ "updatePublicKeys(_:)"
+ "updatePublicKeys(from:) count = "
+ "updateXnuContent(refId:ranges:flags:)"
+ "us, unmapping old surface"
+ "v14@?0{easm_space_unmapxnucontentregionwithflags__result_s=C(?={easm_failure_s=CS})}8"
+ "valid clear before base_hi / len"
+ "vas__easm_unmap_xnu_content_region_with_flags"
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
- " bytes long nonce)"
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
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS27.0.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS27.0.Internal.sdk/System/ExclaveCore/usr/local/standalone/RTKit/usr/include/protocols/mbi_tightbeam_protocol.h"
- "430.0.5"
- "@(#)VERSION:ExclaveOS Image4 Framework Version 7.0.0: Sun Aug  9 21:40:10 PDT 2026; root:AppleImage4_exclavecore-374~17299/ExclaveImage4/RELEASE_ARM64E"
- "ANEExclave version: ANEExclave_exclavecore-13.18.1"
- "Allocating context "
- "BAR entry usage:"
- "BAR entry: type="
- "BUG IN LIBTRACE: Received a BATCH_ERROR while creating a LogBatch"
- "Build Date: Sun Aug  9 21:08:46 PDT 2026"
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
- "ExclaveCameraSISP-20.77.1"
- "ExclaveOS Image4 Framework Version 7.0.0: Sun Aug  9 21:40:10 PDT 2026; root:AppleImage4_exclavecore-374~17299/ExclaveImage4/RELEASE_ARM64E"
- "FW allocated cacheRequestHandle "
- "Firmware handle for the model: "
- "Firmware returned cacheRequestID "
- "Firmware returned program ID "
- "Firwmare buffer "
- "Freeing request "
- "Generated attestation in "
- "Going to look for "
- "IO index for liveInParam "
- "Invalid PeerType value "
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
- "malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:981)"
- "malloc assertion \"!memtag_config.tag_data\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8865)"
- "malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8293)"
- "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7834)"
- "malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:6830)"
- "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:2197)"
- "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:5336)"
- "nits, elapsedWithoutIBIncrease="
- "nonce length is "
- "olp->olp_tpb.tp_size, OS_LOG_PAYLOAD_HDR_SIZE"
- "paramSymbolName: "
- "populateProgramSectionDVAs: kernel DVA=0x"
- "populateProgramSectionDVAs: splitKernel["
- "populateProgramSectionDVAs: text DVA=0x"
- "sendRequestToFirmware priority: "
- "serializedRefKey["
- "splitKernelSections count="
- "system DAK len = "
- "systemKeyAttest -> "
- "systemKeyAttest("
- "total_memory_kib"
- "unload(refId:startFrame:n:)"
- "v14@?0{easm_space_unmapxnucontentregion__result_s=C(?={easm_failure_s=CS})}8"
- "vas__easm_unmap_xnu_content_region"
```
