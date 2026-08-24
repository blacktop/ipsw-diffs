## exclave_sharedcache

> `Firmware/image4/exclavecore_bundle.t8142.RELEASE.restore.im4p/exclave_sharedcache`

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
-  __TEXT.__text: 0x5c7fb8
+1777.0.27.0.0
+  __TEXT.__text: 0x5ca87c
   __TEXT.__lcxx_override: 0xe4
-  __TEXT.__cstring: 0x4e081
-  __TEXT.__const: 0x11f244
-  __TEXT.__swift5_typeref: 0x12eb8
-  __TEXT.__swift5_reflstr: 0x11228
-  __TEXT.__swift5_assocty: 0x78e8
-  __TEXT.__swift5_fieldmd: 0x1a614
-  __TEXT.__constg_swiftt: 0x25984
-  __TEXT.__swift5_protos: 0x8a4
-  __TEXT.__swift5_proto: 0x394c
-  __TEXT.__swift5_types: 0x2204
+  __TEXT.__cstring: 0x4e371
+  __TEXT.__const: 0x11f984
+  __TEXT.__swift5_typeref: 0x1302e
+  __TEXT.__swift5_reflstr: 0x11358
+  __TEXT.__swift5_assocty: 0x7a10
+  __TEXT.__swift5_fieldmd: 0x1a790
+  __TEXT.__constg_swiftt: 0x25a10
+  __TEXT.__swift5_protos: 0x8ac
+  __TEXT.__swift5_proto: 0x3a14
+  __TEXT.__swift5_types: 0x2220
   __TEXT.__swift5_types2: 0x60
-  __TEXT.__swift5_builtin: 0x1568
+  __TEXT.__swift5_builtin: 0x1590
   __TEXT.__swift5_capture: 0xf9c
   __TEXT.__objc_methtype: 0xe1
-  __TEXT.__swift5_mpenum: 0x39c
-  __TEXT.__swift_as_entry: 0x994
+  __TEXT.__swift5_mpenum: 0x3b4
+  __TEXT.__swift_as_entry: 0x998
   __TEXT.__swift_as_ret: 0xb08
   __TEXT.__swift_as_cont: 0x11f8
-  __TEXT.__oslogstring: 0xb2
+  __TEXT.__oslogstring: 0xf0
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0

   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x0
   __TEXT.__chain_fixups: 0xb0
-  __TEXT.__eh_frame: 0x32dc4
+  __TEXT.__eh_frame: 0x32fa4
   __DATA.__TIGHTBEAM_VT: 0x720
   __DATA.__TIGHTBEAM: 0x1d8
-  __DATA.__const: 0x3abb8
-  __DATA.__data: 0x16650
+  __DATA.__const: 0x3ac98
+  __DATA.__data: 0x166e0
   __DATA.__mod_init_func: 0x40
-  __DATA.__ENDPOINTS: 0x1a221
-  __DATA.__auth_ptr: 0x1fd8
+  __DATA.__ENDPOINTS: 0x1a328
+  __DATA.__auth_ptr: 0x2008
   __DATA.__DEVICETREE: 0x18
   __DATA.__shared_cache: 0x380
   __DATA.__DARTS: 0x93f

   __DATA.__mod_term_func: 0x0
   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x30
-  __DATA.__bss: 0xe260
-  __DATA.__common: 0x6ba
+  __DATA.__bss: 0xe540
+  __DATA.__common: 0x6ca
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
-  Functions: 22442
+  Functions: 22491
   Symbols:   1
-  CStrings:  7123
+  CStrings:  7141
 
CStrings:
+ "\n    Background factors: last="
+ " -> calculated XYZ:"
+ " [nits]\n    Indicator factors: last="
+ " sample is invalid, using max sample (lux="
+ ", BackgroundColor="
+ ", IndicatorColor="
+ "Calculated XYZ and supplied XYZ for background color are too far from each other, original RGB:"
+ "Calculated XYZ and supplied XYZ for indicator color are too far from each other, original RGB:"
+ "Can't skip by a negative offset"
+ "Chill pill usage is "
+ "EXBrightComponent/EXBrightComponent_swift.swift"
+ "EXBrightComponent/Extensions.swift"
+ "EXBrightDefines/EXBrightDefines_swift.swift"
+ "EXBrightDisplayPipeClient/EXBrightDisplayPipeClient_swift.swift"
+ "EXBrightPILEICClient/EXBrightPILEICClient_swift.swift"
+ "Escaping Closure Propagated"
+ "Failed to calibrate sensor(s), setting dispatchUpcallOnSILEnabled=true"
+ "MMIO read: addr=%p value=0x%llx"
+ "MMIO read: addr=%p value=0x%x"
+ "MMIO write: addr=%p value=0x%x"
+ "Queue size must > 0"
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
- "Brightness health nil when expecting a value - setting to false"
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
- "EXBrightPILEICClient/EXBrightPILEICClient_Swift.swift"
- "Failed to create BrightnessUtil, health checks will not be available!"
- "Hibernation count has changed, reporting bad health"
- "Indicator Brightness Health "
- "Indicator brightness health for frame #"
- "MMIO Write: addr=%p value=0x%x"
- "No MIB before first sample, ignoring .failureNoMIB"
- "Overflow when substracting timestamps, frame ts: "
- "Received MIB with SIL off"
- "SCA factor is 0, requesting soft boundary"
- "SIL not enabled when requesting soft boundary"
- "Setting UI Brightness "
- "Soft boundary minimum ontime not met"
- "Switched to MIB ramp up mode during brightness ramp down, ignoring this frame."
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
