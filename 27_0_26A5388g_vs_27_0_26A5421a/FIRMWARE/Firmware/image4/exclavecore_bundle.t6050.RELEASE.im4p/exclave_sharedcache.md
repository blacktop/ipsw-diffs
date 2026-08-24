## exclave_sharedcache

> `Firmware/image4/exclavecore_bundle.t6050.RELEASE.im4p/exclave_sharedcache`

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
-  __TEXT.__text: 0xd348ac
+1777.0.27.0.0
+  __TEXT.__text: 0xd3e3cc
   __TEXT.__lcxx_override: 0xe4
-  __TEXT.__cstring: 0xa1791
-  __TEXT.__const: 0x199104
-  __TEXT.__swift5_typeref: 0x29bca
-  __TEXT.__swift5_reflstr: 0x3ad18
-  __TEXT.__swift5_assocty: 0xe460
-  __TEXT.__swift5_fieldmd: 0x5b370
-  __TEXT.__constg_swiftt: 0x610fc
-  __TEXT.__swift5_protos: 0x11f4
-  __TEXT.__swift5_proto: 0x9870
-  __TEXT.__swift5_types: 0x5dd0
+  __TEXT.__cstring: 0xa1d81
+  __TEXT.__const: 0x199f34
+  __TEXT.__swift5_typeref: 0x29e76
+  __TEXT.__swift5_reflstr: 0x3afa8
+  __TEXT.__swift5_assocty: 0xe648
+  __TEXT.__swift5_fieldmd: 0x5b778
+  __TEXT.__constg_swiftt: 0x613a4
+  __TEXT.__swift5_protos: 0x1204
+  __TEXT.__swift5_proto: 0x99d8
+  __TEXT.__swift5_types: 0x5e3c
   __TEXT.__swift5_types2: 0xbc
-  __TEXT.__swift5_builtin: 0x26fc
+  __TEXT.__swift5_builtin: 0x2724
   __TEXT.__swift5_capture: 0x34f4
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
   __TEXT.__chain_fixups: 0x120
-  __TEXT.__eh_frame: 0x74ac0
+  __TEXT.__eh_frame: 0x74fd4
   __DATA.__TIGHTBEAM_VT: 0x1200
   __DATA.__TIGHTBEAM: 0x4a8
-  __DATA.__const: 0xdd5b0
-  __DATA.__data: 0x4e728
+  __DATA.__const: 0xde528
+  __DATA.__data: 0x4e898
   __DATA.__mod_init_func: 0x40
-  __DATA.__ENDPOINTS: 0x1b6ad
-  __DATA.__auth_ptr: 0x72f8
+  __DATA.__ENDPOINTS: 0x1b7b4
+  __DATA.__auth_ptr: 0x73a0
   __DATA.__DEVICETREE: 0x30
   __DATA.__shared_cache: 0x3b8
   __DATA.__DARTS: 0x93f

   __DATA.__mod_term_func: 0x0
   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x30
-  __DATA.__bss: 0x244b0
-  __DATA.__common: 0x2789
+  __DATA.__bss: 0x24aa0
+  __DATA.__common: 0x2799
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
-  Functions: 47172
+  Functions: 47288
   Symbols:   1
-  CStrings:  14932
+  CStrings:  14968
 
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
+ "Mon Aug 10 01:20:22 PDT 2026"
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
- "Tue Jul 14 21:23:40 PDT 2026"
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
