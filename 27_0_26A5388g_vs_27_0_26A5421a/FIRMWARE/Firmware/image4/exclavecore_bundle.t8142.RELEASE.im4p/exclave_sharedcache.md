## exclave_sharedcache

> `Firmware/image4/exclavecore_bundle.t8142.RELEASE.im4p/exclave_sharedcache`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_types2`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_entry`
- `__TEXT.__chain_fixups`
- `__DATA.__TIGHTBEAM_VT`
- `__DATA.__TIGHTBEAM`
- `__DATA.__mod_init_func`
- `__DATA.__shared_cache`
- `__DATA.__got`
- `__PDATA.__auth_ptr`
- `__PDATA.__const`
- `__PDATA.__data`
- `__PDATA.__shared_cache`

```diff

-1777.0.20.0.0
-  __TEXT.__text: 0xd3638c
+1777.0.27.0.0
+  __TEXT.__text: 0xd3fe7c
   __TEXT.__lcxx_override: 0xe4
-  __TEXT.__cstring: 0xa17e1
-  __TEXT.__const: 0x199a64
-  __TEXT.__swift5_typeref: 0x29c5a
-  __TEXT.__swift5_reflstr: 0x3b678
-  __TEXT.__swift5_assocty: 0xe460
-  __TEXT.__swift5_fieldmd: 0x5bf84
-  __TEXT.__constg_swiftt: 0x61410
-  __TEXT.__swift5_protos: 0x11f4
-  __TEXT.__swift5_proto: 0x98bc
-  __TEXT.__swift5_types: 0x5e44
+  __TEXT.__cstring: 0xa1dd1
+  __TEXT.__const: 0x19a894
+  __TEXT.__swift5_typeref: 0x29f06
+  __TEXT.__swift5_reflstr: 0x3b908
+  __TEXT.__swift5_assocty: 0xe648
+  __TEXT.__swift5_fieldmd: 0x5c38c
+  __TEXT.__constg_swiftt: 0x616b8
+  __TEXT.__swift5_protos: 0x1204
+  __TEXT.__swift5_proto: 0x9a24
+  __TEXT.__swift5_types: 0x5eb0
   __TEXT.__swift5_types2: 0xbc
-  __TEXT.__swift5_builtin: 0x26fc
+  __TEXT.__swift5_builtin: 0x2724
   __TEXT.__swift5_capture: 0x34d4
   __TEXT.__objc_methtype: 0x2b6
-  __TEXT.__swift5_mpenum: 0xc00
-  __TEXT.__swift_as_entry: 0x1608
+  __TEXT.__swift5_mpenum: 0xc18
+  __TEXT.__swift_as_entry: 0x160c
   __TEXT.__swift_as_ret: 0x1808
   __TEXT.__swift_as_cont: 0x2e58
-  __TEXT.__oslogstring: 0x6ba7
+  __TEXT.__oslogstring: 0x6c67
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0

   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x0
   __TEXT.__chain_fixups: 0x128
-  __TEXT.__eh_frame: 0x74ac0
+  __TEXT.__eh_frame: 0x74fd4
   __DATA.__TIGHTBEAM_VT: 0x1200
   __DATA.__TIGHTBEAM: 0x4a8
-  __DATA.__const: 0xe08e0
-  __DATA.__data: 0x4e8a8
+  __DATA.__const: 0xe1858
+  __DATA.__data: 0x4ea18
   __DATA.__mod_init_func: 0x40
-  __DATA.__ENDPOINTS: 0x1b6ad
-  __DATA.__auth_ptr: 0x73d8
+  __DATA.__ENDPOINTS: 0x1b7b4
+  __DATA.__auth_ptr: 0x7480
   __DATA.__DEVICETREE: 0x30
   __DATA.__shared_cache: 0x3b8
   __DATA.__DARTS: 0x93f

   __DATA.__mod_term_func: 0x0
   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x30
-  __DATA.__bss: 0x244a0
-  __DATA.__common: 0x2891
+  __DATA.__bss: 0x24aa0
+  __DATA.__common: 0x28a1
   __PDATA.__auth_ptr: 0x280
   __PDATA.__const: 0x67b0
   __PDATA.__objc_imageinfo: 0x8

   __PDATA.__data: 0x2af0
   __PDATA.__ENDPOINTS: 0x838
   __PDATA.__shared_cache: 0x70
-  __PDATA.__bss: 0xc4b8
+  __PDATA.__bss: 0xba48
   __PDATA.__common: 0x2578
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  Functions: 47182
+  Functions: 47298
   Symbols:   1
-  CStrings:  14933
+  CStrings:  14969
 
CStrings:
+ "\n    Background factors: last="
+ " (expected 0); proceeding"
+ " -> calculated XYZ:"
+ " ALS sensor(s) present but no als-types configured; treating as no-ALS static platform"
+ " [nits]\n    Indicator factors: last="
+ " sample is invalid, using max sample (lux="
+ " vs alsTypes.count="
+ "%llx %llx %llx"
+ ", BackgroundColor="
+ ", IndicatorColor="
+ "@(#)VERSION:ExclaveOS Image4 Framework Version 7.0.0: Mon Aug 10 00:39:23 PDT 2026; root:AppleImage4_exclavecore-374~17304/ExclaveImage4/RELEASE_ARM64E"
+ "ANEExclave version: ANEExclave_exclavecore-13.18.1"
+ "Build Date: Sat Aug  8 17:06:14 PDT 2026"
+ "Calculated XYZ and supplied XYZ for background color are too far from each other, original RGB:"
+ "Calculated XYZ and supplied XYZ for indicator color are too far from each other, original RGB:"
+ "Can't skip by a negative offset"
+ "Chill pill usage is "
+ "CryptoKit/Ed448Keys_cc.swift"
+ "CryptoKit/X25519Keys_cc.swift"
+ "CryptoKit/X448Keys_cc.swift"
+ "Directory not present (probe): "
+ "EXBrightComponent/EXBrightComponent_swift.swift"
+ "EXBrightComponent/Extensions.swift"
+ "EXBrightDefines/EXBrightDefines_swift.swift"
+ "EXBrightDisplayPipeClient/EXBrightDisplayPipeClient_swift.swift"
+ "EXBrightPILComponent/EXBrightPILComponent_swift.swift"
+ "EXBrightPILComponent/Extensions.swift"
+ "EXBrightPILEICClient/EXBrightPILEICClient_swift.swift"
+ "Escaping Closure Propagated"
+ "ExclaveOS Image4 Framework Version 7.0.0: Mon Aug 10 00:39:23 PDT 2026; root:AppleImage4_exclavecore-374~17304/ExclaveImage4/RELEASE_ARM64E"
+ "ExclaveSISP-6.20"
+ "Failed to calibrate sensor(s), setting dispatchUpcallOnSILEnabled=true"
+ "Failed to create ALSManager: alses.count="
+ "MMIO read: addr=%p value=0x%llx"
+ "MMIO read: addr=%p value=0x%x"
+ "MMIO write: addr=%p value=0x%x"
+ "MNISTPersistentPower"
+ "Mon Aug 10 01:20:43 PDT 2026"
+ "No ALS manager; secure static PIL controller initialized"
+ "No ALS sensors available; no-ALS platform"
+ "No Resource Available"
+ "PIL Calibration (v1) loaded - checksum: "
+ "PIL Calibration (v2) bad magic: expected 'PiCA', got "
+ "PIL Calibration (v2) checksum mismatch: sum & 0xFFFF = 0x"
+ "PIL Calibration (v2) loaded - version: "
+ "PIL Calibration (v2) unexpected version "
+ "Queue size must > 0"
+ "SCA: applying lower thresholds"
+ "SCA: restoring normal thresholds (lower thresholds window ended)"
+ "Swift/BorrowingSequence.swift"
+ "[EIC] MMIO read: addr=%p value=0x%llx\n"
+ "[EIC] MMIO read: addr=%p value=0x%x\n"
+ "[EIC] MMIO write: addr=%p value=0x%x\n"
+ "] Brightness health nil when expecting a value - setting to false"
+ "] Cannot estimate ramp duration, invalid target brightness value: "
+ "] Contrast Health "
+ "] Contrast failure session began"
+ "] Contrast failure session continuing, passing since "
+ "] Contrast failure session ending"
+ "] Contrast failure session longer than grace period for applying soft boundary, reporting failure"
+ "] Contrast failure session still in grace period ("
+ "] Contrast health for frame #"
+ "] ContrastCheckResult="
+ "] Failed to create BrightnessUtil, health checks will not be available!"
+ "] Hibernation count has changed, reporting bad health"
+ "] Indicator Brightness Health "
+ "] Indicator brightness health for frame #"
+ "] No MIB before first sample, ignoring .failureNoMIB"
+ "] Overflow when substracting timestamps, frame ts: "
+ "] Received MIB with SIL off"
+ "] SCA factor is 0, requesting soft boundary"
+ "] SIL not enabled when requesting soft boundary"
+ "] Setting UI Brightness "
+ "] Soft boundary minimum ontime not met"
+ "] Switched to MIB ramp up mode during brightness ramp down, ignoring this frame."
+ "] Underflow in contrast failure session recovery check, "
+ "] Underflow in soft boundary SIL session start grace period evaluation - "
+ "] Underflow when checking minimum ontime for soft boundary"
+ "] Waking up from hibernation with soft boundary state as enabled!"
+ "] We have received empty array of frames for health check!"
+ "][EXDisplayPipe Utilization] Health Check took "
+ "][evaluateContrastHealth] Contrast is progressing, returning success"
+ "][healthCheckMode] .rampUp -> .steady. Ctx: adjustedIBNitsFiltered="
+ "minItems must be >= 1"
+ "octopus_chill_pill_stability"
- "\n    Background RGB: last="
- " [nits]\n    Indicator RGB: last="
- ", BackgroundRGB="
- "@(#)VERSION:ExclaveOS Image4 Framework Version 7.0.0: Fri Jul 10 22:26:57 PDT 2026; root:AppleImage4_exclavecore-374~10965/ExclaveImage4/RELEASE_ARM64E"
- "ANEExclave version: ANEExclave_exclavecore-13.17.1"
- "Brightness health nil when expecting a value - setting to false"
- "Build Date: Fri Jul 10 22:05:30 PDT 2026"
- "Cannot estimate ramp duration, invalid target brightness value: "
- "Contrast Health "
- "Contrast failure session began"
- "Contrast failure session continuing, passing since "
- "Contrast failure session ending"
- "Contrast failure session longer than grace period for applying soft boundary, reporting failure"
- "Contrast failure session still in grace period ("
- "Contrast health for frame #"
- "ContrastCheckResult="
- "EXBrightComponent/EXBrightComponent_Swift.swift"
- "EXBrightDisplayPipeClient/EXBrightDisplayPipeClient_Swift.swift"
- "EXBrightPILComponent/EXBrightPILComponent_Swift.swift"
- "EXBrightPILEICClient/EXBrightPILEICClient_Swift.swift"
- "ExclaveOS Image4 Framework Version 7.0.0: Fri Jul 10 22:26:57 PDT 2026; root:AppleImage4_exclavecore-374~10965/ExclaveImage4/RELEASE_ARM64E"
- "ExclaveSISP-6.14.1"
- "Failed to create ALSManager despite having ALS sensors!"
- "Failed to create BrightnessUtil, health checks will not be available!"
- "Hibernation count has changed, reporting bad health"
- "Indicator Brightness Health "
- "Indicator brightness health for frame #"
- "MMIO Write: addr=%p value=0x%x"
- "No ALS sensors available, skipping ALSManager initialization"
- "No MIB before first sample, ignoring .failureNoMIB"
- "Overflow when substracting timestamps, frame ts: "
- "PIL Calibration loaded - checksum: "
- "Received MIB with SIL off"
- "SCA factor is 0, requesting soft boundary"
- "SIL not enabled when requesting soft boundary"
- "Setting UI Brightness "
- "Soft boundary minimum ontime not met"
- "Switched to MIB ramp up mode during brightness ramp down, ignoring this frame."
- "Tue Jul 14 21:24:01 PDT 2026"
- "Underflow in contrast failure session recovery check, "
- "Underflow in soft boundary SIL session start grace period evaluation - "
- "Underflow when checking minimum ontime for soft boundary"
- "Unexpected size!"
- "Waking up from hibernation with soft boundary state as enabled!"
- "We have received empty array of frames for health check!"
- "[EIC] MMIO Write: addr=%p value=0x%x\n"
- "[EXDisplayPipe Utilization] Health Check took "
- "[evaluateContrastHealth] Contrast is progressing, returning success"
- "[healthCheckMode] .rampUp -> .steady. Ctx: adjustedIBNitsFiltered="
```
