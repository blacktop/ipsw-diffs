## exclave_sharedcache

> `Firmware/image4/exclavecore_bundle.t8160.RELEASE.im4p/exclave_sharedcache`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_types2`
- `__TEXT.__swift5_entry`
- `__DATA.__mod_init_func`
- `__DATA.__shared_cache`
- `__DATA.__got`
- `__PDATA.__auth_ptr`
- `__PDATA.__const`
- `__PDATA.__data`
- `__PDATA.__shared_cache`

```diff

-1777.60.14.0.1
-  __TEXT.__text: 0xf7ca28
+1777.60.18.0.1
+  __TEXT.__text: 0xfa8224
   __TEXT.__lcxx_override: 0xd0
-  __TEXT.__cstring: 0xb8e51
-  __TEXT.__const: 0x225db4
-  __TEXT.__swift5_typeref: 0x32f42
-  __TEXT.__swift5_reflstr: 0x55de8
-  __TEXT.__swift5_assocty: 0x103f0
-  __TEXT.__swift5_fieldmd: 0x8fad0
-  __TEXT.__constg_swiftt: 0x89054
-  __TEXT.__swift5_protos: 0x14e0
-  __TEXT.__swift5_proto: 0xce00
-  __TEXT.__swift5_types: 0x8534
+  __TEXT.__cstring: 0xba171
+  __TEXT.__const: 0x2271a4
+  __TEXT.__swift5_typeref: 0x33426
+  __TEXT.__swift5_reflstr: 0x56898
+  __TEXT.__swift5_assocty: 0x10498
+  __TEXT.__swift5_fieldmd: 0x906ec
+  __TEXT.__constg_swiftt: 0x89e64
+  __TEXT.__swift5_protos: 0x14f0
+  __TEXT.__swift5_proto: 0xcea4
+  __TEXT.__swift5_types: 0x85dc
   __TEXT.__swift5_types2: 0xc4
-  __TEXT.__swift5_builtin: 0x2bac
-  __TEXT.__swift5_capture: 0x3404
+  __TEXT.__swift5_builtin: 0x2c74
+  __TEXT.__swift5_capture: 0x33f4
   __TEXT.__objc_methtype: 0x576
-  __TEXT.__swift5_mpenum: 0xdd8
-  __TEXT.__swift_as_entry: 0x1798
-  __TEXT.__swift_as_ret: 0x1ae0
-  __TEXT.__swift_as_cont: 0x3444
-  __TEXT.__oslogstring: 0x7285
+  __TEXT.__swift5_mpenum: 0x103c
+  __TEXT.__swift_as_entry: 0x17f8
+  __TEXT.__swift_as_ret: 0x1b30
+  __TEXT.__swift_as_cont: 0x34d0
+  __TEXT.__oslogstring: 0x7575
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0
   __TEXT.__swift5_replace: 0x0
   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x0
-  __TEXT.__chain_fixups: 0x170
-  __TEXT.__eh_frame: 0x86308
-  __DATA.__TIGHTBEAM_VT: 0x1530
-  __DATA.__TIGHTBEAM: 0x590
-  __DATA.__const: 0x120020
-  __DATA.__data: 0xa75d0
+  __TEXT.__chain_fixups: 0x178
+  __TEXT.__eh_frame: 0x86cb0
+  __DATA.__TIGHTBEAM_VT: 0x1560
+  __DATA.__TIGHTBEAM: 0x598
+  __DATA.__const: 0x121400
+  __DATA.__data: 0xa8248
   __DATA.__mod_init_func: 0x40
-  __DATA.__ENDPOINTS: 0x1c71d
-  __DATA.__auth_ptr: 0xb938
+  __DATA.__ENDPOINTS: 0x1cb39
+  __DATA.__auth_ptr: 0xb9e8
   __DATA.__DEVICETREE: 0x30
   __DATA.__shared_cache: 0x3b8
   __DATA.__DARTS: 0x93f

   __DATA.__mod_term_func: 0x0
   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x30
-  __DATA.__common: 0x5dc2
+  __DATA.__common: 0x5de2
   __PDATA.__auth_ptr: 0x280
   __PDATA.__const: 0x6910
   __PDATA.__objc_imageinfo: 0x8

   __PDATA.__common: 0x2578
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  Functions: 1082
+  Functions: 1080
   Symbols:   1
-  CStrings:  17134
+  CStrings:  17227
 
CStrings:
+ "  matrix: nil (sRGB target, no color conversion)"
+ " has a session hint transition in flight -- leaving for later"
+ " ignored: perf control upcalls not wired"
+ " minModeledLatencyUs "
+ " no sample from this sensor, still within first integration period, skipping..."
+ " shapeSimilarity: "
+ "$JgDeviceMemoryKeyStoreComponent.DeviceMemoryKeyStoreController.init(sksdClient:sharedOOLBufferIn:sharedOOLBufferOut:sharedKeyBufferSegments:convenienceBioSegments:)"
+ "); kext has no handler, disabling perf control upcalls"
+ "@(#)VERSION:ExclaveOS Image4 Framework Version 7.0.0: Tue Nov 10 02:06:38 PST 2026; root:AppleImage4_exclavecore-374~20321/ExclaveImage4/RELEASE_ARM64E"
+ "ANEExclave version: ANEExclave_exclavecore-13.205"
+ "BUG IN XNU: concurrent calls to LogServer.getLogs()"
+ "BUG IN XNU: concurrent calls to RedactedLogServer.getLogs()"
+ "Build Date: Tue Nov 10 01:46:21 PST 2026"
+ "Builtin.FixedArray of %zd elements with stride %zu is too large to be representable\n"
+ "Cached procedure refused: shutdown in progress"
+ "ExclaveCameraSISP-20.206"
+ "ExclaveIndicatorControllerComponent/ExclavesPlatform.swift"
+ "ExclaveOS Image4 Framework Version 7.0.0: Tue Nov 10 02:06:38 PST 2026; root:AppleImage4_exclavecore-374~20321/ExclaveImage4/RELEASE_ARM64E"
+ "Failed to read GLTB"
+ "Invalid key value while decoding result type for disableConvenienceBio"
+ "Invalid key value while decoding result type for dropConvenienceBioSecret"
+ "Invalid key value while decoding result type for enableConvenienceBio"
+ "Invalid key value while decoding result type for getConvenienceBioState"
+ "Invalid key value while decoding result type for isConvenienceBioEnabled"
+ "Invalid key value while decoding result type for performConvenienceBioUnlock"
+ "Invalid key value while decoding result type for retrieveConvenienceBioSecret"
+ "MNISTDynamicPower"
+ "Model load refused: shutdown in progress"
+ "Non-finite XYZ color factors detected, sending RGB only"
+ "OSLogServerComponent/RedactedLogServer.swift"
+ "Perf control policy 0x"
+ "Perf control policy: report "
+ "Request refused: shutdown in progress"
+ "SCLCursorDriver: verification-only mode, skipping cursor DMA mapping"
+ "SCLDriver: verification-only mode, skipping DMA mapping"
+ "SILManager: enabled region with no indicator resolved"
+ "SM3: DMEM load failed"
+ "Shutdown reset: accepting new work again"
+ "Siri activated mic: microphone allowed for longer than "
+ "Siri activated mic: no voice trigger service, microphone not allowed"
+ "Siri activated mic: recent voice trigger event detected"
+ "SiriActivatedMic = "
+ "Tried to build a Builtin.FixedArray without metadata for the element type"
+ "VerificationAlgorithmContext.cleanup: destroying preparedIndicator="
+ "VerificationAlgorithmContext.deinit: destroying preparedIndicator="
+ "VerificationAlgorithmContext.detectIndicator: SCA buffer is nil"
+ "VerificationAlgorithmContext.detectIndicator: preparedIndicator is nil"
+ "VerificationAlgorithmContext.init: vlibVersion="
+ "VerificationAlgorithmContext.updateSCLBuffer: PrepareIndicatorFromTemplateBuffer failed"
+ "VerificationAlgorithmContext.updateSCLBuffer: PrepareIndicatorFromTemplateBuffer succeeded preparedIndicator="
+ "VerificationAlgorithmContext.updateSCLBuffer: destroying preparedIndicator="
+ "[ERROR] %s: %s: No valid procedure variant info for procId %llu (single and bonded both absent)\n"
+ "[EXDisplayPipeDriver] setSILHealth(region:indicator:status:healthValidForDuration:) not supported"
+ "[EXDisplayPipe] supports-verification-only: taking verification-only path, SCL mapper disabled"
+ "[EXDisplayPipe] verification-only mode: using SCLStubDriver"
+ "[StrictMode] .rampUp -> .steady"
+ "[StrictMode] Can't use pre-wake MIB. Reporting failure."
+ "[StrictMode] Disabling (enabledTs="
+ "[StrictMode] Enabling (ts="
+ "[StrictMode] Healthy. Disabling. MIB="
+ "_decNumAllocated()"
+ "allocateNode(_:_:_:)"
+ "backgroundChroma: ("
+ "backgroundChroma: (%f, %f, %f)"
+ "chromaticPixelRatio: "
+ "chromaticPixelRatio: %f outscaleX: %f outscaleY: %f"
+ "detectIndicatorWorkspaceSize: size="
+ "disableConvenienceBio threw an unexpected error type "
+ "dropConvenienceBioSecret threw an unexpected error type "
+ "enableConvenienceBio threw an unexpected error type "
+ "exdisp_sca_vlib_enable"
+ "failed to shrink max mapped to minimum = "
+ "getConvenienceBioState threw an unexpected error type "
+ "getProcedureLatencyStats"
+ "indicatorChroma: ("
+ "indicatorChroma: (%f, %f, %f)"
+ "invalid rawValue for AKSConvenienceBioState: "
+ "invalid rawValue for EXDisplayPipeSwapAnimationKind: "
+ "isConvenienceBioEnabled threw an unexpected error type "
+ "octopus_siri_activated_mic"
+ "performConvenienceBioUnlock threw an unexpected error type"
+ "policy-siri-activated-mic"
+ "positionalOffset: ("
+ "positionalOffset: (%f, %f)"
+ "querySupportsVerificationOnly: no root node"
+ "reset max mapped to minimum = "
+ "retrieveConvenienceBioSecret threw an unexpected error type"
+ "scalarInvariantColorScore: "
+ "scalarInvariantColorScore: %f shapeSimilarity: %f"
+ "scl.setRegionEnable( 0, true) failed"
+ "scl.setRegionEnable( 1, true) failed"
+ "scl.setRegionEnable( 2, true) failed"
+ "scl.setRegionEnable( 3, true) failed"
+ "sessionHint Start: releasing the re-registration EC assertion failed: "
+ "sessionHint: refused, shutdown in progress"
+ "startShutdown: shutdown downcall completed"
+ "supports-verification-only"
+ "template changed"
+ "type bound to a value generic parameter"
+ "type where a Builtin.FixedArray count is required"
+ "unresolved Builtin.FixedArray element type"
- "@(#)VERSION:ExclaveOS Image4 Framework Version 7.0.0: Sat Oct 24 02:00:08 PDT 2026; root:AppleImage4_exclavecore-374~19937/ExclaveImage4/RELEASE_ARM64E"
- "ANEExclave version: ANEExclave_exclavecore-13.203.1"
- "Build Date: Sat Oct 24 01:40:55 PDT 2026"
- "ExclaveCameraSISP-20.203.1"
- "ExclaveOS Image4 Framework Version 7.0.0: Sat Oct 24 02:00:08 PDT 2026; root:AppleImage4_exclavecore-374~19937/ExclaveImage4/RELEASE_ARM64E"
- "MMIO read: addr=%p value=0x%llx"
- "[EIC] MMIO read: addr=%p value=0x%llx\n"
- "[EXDisplayPipeDriver] setSILHealth(region:status:healthValidForDuration:) not supported"
```
