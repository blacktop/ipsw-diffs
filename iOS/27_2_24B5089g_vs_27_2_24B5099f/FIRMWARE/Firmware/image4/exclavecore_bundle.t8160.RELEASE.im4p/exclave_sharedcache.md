## exclave_sharedcache

> `Firmware/image4/exclavecore_bundle.t8160.RELEASE.im4p/exclave_sharedcache`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_types2`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_entry`
- `__TEXT.__chain_fixups`
- `__DATA.__TIGHTBEAM_VT`
- `__DATA.__TIGHTBEAM`
- `__DATA.__mod_init_func`
- `__DATA.__shared_cache`
- `__DATA.__got`
- `__PDATA.__auth_ptr`
- `__PDATA.__const`
- `__PDATA.__mod_init_func`
- `__PDATA.__data`
- `__PDATA.__shared_cache`

```diff

-1777.40.28.0.2
-  __TEXT.__text: 0xf2c9a4
+1777.40.34.0.0
+  __TEXT.__text: 0xf33e40
   __TEXT.__lcxx_override: 0xd0
-  __TEXT.__cstring: 0xb5041
-  __TEXT.__const: 0x207fc4
-  __TEXT.__swift5_typeref: 0x3292a
-  __TEXT.__swift5_reflstr: 0x55178
-  __TEXT.__swift5_assocty: 0x10270
-  __TEXT.__swift5_fieldmd: 0x8eda8
-  __TEXT.__constg_swiftt: 0x78b08
+  __TEXT.__cstring: 0xb5851
+  __TEXT.__const: 0x208314
+  __TEXT.__swift5_typeref: 0x329ba
+  __TEXT.__swift5_reflstr: 0x55368
+  __TEXT.__swift5_assocty: 0x10288
+  __TEXT.__swift5_fieldmd: 0x8ef54
+  __TEXT.__constg_swiftt: 0x78c8c
   __TEXT.__swift5_protos: 0x14c0
-  __TEXT.__swift5_proto: 0xccd4
-  __TEXT.__swift5_types: 0x8498
+  __TEXT.__swift5_proto: 0xccec
+  __TEXT.__swift5_types: 0x84ac
   __TEXT.__swift5_types2: 0xc4
   __TEXT.__swift5_builtin: 0x2bc0
-  __TEXT.__swift5_capture: 0x3c0c
-  __TEXT.__objc_methtype: 0x556
+  __TEXT.__swift5_capture: 0x3c1c
+  __TEXT.__objc_methtype: 0x576
   __TEXT.__swift5_mpenum: 0xdc4
-  __TEXT.__swift_as_entry: 0x1688
-  __TEXT.__swift_as_ret: 0x1898
-  __TEXT.__swift_as_cont: 0x2f94
-  __TEXT.__oslogstring: 0x70b5
+  __TEXT.__swift_as_entry: 0x169c
+  __TEXT.__swift_as_ret: 0x18bc
+  __TEXT.__swift_as_cont: 0x2fd0
+  __TEXT.__oslogstring: 0x70c5
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0

   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x0
   __TEXT.__chain_fixups: 0x170
-  __TEXT.__eh_frame: 0x83304
+  __TEXT.__eh_frame: 0x83718
   __DATA.__TIGHTBEAM_VT: 0x1530
   __DATA.__TIGHTBEAM: 0x590
-  __DATA.__const: 0x168568
-  __DATA.__data: 0x5ff40
+  __DATA.__const: 0x1688a8
+  __DATA.__data: 0x600c8
   __DATA.__mod_init_func: 0x40
-  __DATA.__ENDPOINTS: 0x1bbd0
-  __DATA.__auth_ptr: 0xb868
+  __DATA.__ENDPOINTS: 0x1bcd7
+  __DATA.__auth_ptr: 0xb878
   __DATA.__DEVICETREE: 0x30
   __DATA.__shared_cache: 0x3b8
   __DATA.__DARTS: 0x93f

   __DATA_CONST.__mod_term_func: 0x0
   Functions: 1451
   Symbols:   1
-  CStrings:  16807
+  CStrings:  16856
 
CStrings:
+ " DisplayManager is not configured!"
+ " but a session is already active!"
+ " but startTimestampUS is nil!"
+ " deferrals(hwBusy)="
+ " deferrals(pipelineBusy)="
+ " for Storage exclave"
+ " gateEarlyRejects="
+ " gateExemptedBuffers="
+ " is not a valid integer: "
+ " opted into prefers-waiting-through-sleep, blocking: "
+ " parked request(s) with mappers disabled; they will submit against unmapped DART state"
+ " parking until sleep cycle completes, parked: "
+ " rejected before IO prep. SleepCycle: "
+ "), deferring DART unmap"
+ "430.40.6"
+ ": panicking to prevent MTE tag brute-forcing"
+ "; using no-op control"
+ "@(#)VERSION:ExclaveOS Image4 Framework Version 7.0.0: Mon Sep 28 22:45:47 PDT 2026; root:AppleImage4_exclavecore-374~19125/ExclaveImage4/RELEASE_ARM64E"
+ "ANEExclave version: ANEExclave_exclavecore-13.102.1"
+ "Applying MTE backoff of "
+ "Build Date: Mon Sep 28 22:24:15 PDT 2026"
+ "Builtin.Borrow is not supported in runtime type lookup"
+ "Bundle metadata for "
+ "Conclave MTE tag check fault: esr="
+ "Could not start storage: "
+ "ENABLED via driver opt-in"
+ "Empty value of bundle metadata "
+ "ExclaveCameraSISP-20.106.4"
+ "ExclaveOS Image4 Framework Version 7.0.0: Mon Sep 28 22:45:47 PDT 2026; root:AppleImage4_exclavecore-374~19125/ExclaveImage4/RELEASE_ARM64E"
+ "In-flight HW or pipeline requests present (pipeline: "
+ "Initialized count must be in 0 ... unsafeUninitializedCapacity."
+ "Invalid log level "
+ "MTE tag check fault #"
+ "Park-through-sleep "
+ "ParkThroughSleep enabled: "
+ "SEP power control wired but SoC type is unknown; disabling SEP reset lockout"
+ "SEP reset lockout not supported on "
+ "SEP reset protection "
+ "SEP reset protection enabled: "
+ "SEP reset protection requested but no SEP control is wired on this part"
+ "SM3: CTRR did not open, protected "
+ "SM3: CTRR not armed, code region unprotected"
+ "SM3: IMEM is CTRR-protected, image retained, copy skipped"
+ "SM3: copy failed, leaving CTRR disarmed to allow a retry"
+ "SetLogLevelFromBundle()"
+ "SleepCycle parked requests: "
+ "SleepCycle pipeline count: "
+ "SleepCycle totals: parks="
+ "Storage not ready"
+ "StorageExclaveComponent/XRTBundleResources.swift"
+ "[EXDisplayPipe] DeviceInfoH19P: target="
+ "[EXDisplayPipe] DeviceInfoH19P: unsupported tunable target: "
+ "[SecureM3Handler] ERROR firmware load failed"
+ "[SecureM3Handler] MCPU power "
+ "[SecureM3Handler] MCPU power %ld -> %ld"
+ "disabled (default)"
+ "getBundleMetadata(_:)"
+ "ns before launch"
+ "ns before next launch"
+ "releasePipelineReservation not called with workLoop Gate held!"
+ "sharedmem_framemap_getPhysicalAddress"
+ "sharedmem_framemap_setMapped_delta"
+ "takePipelineReservation called twice for request "
+ "takePipelineReservation not called with workLoop Gate held!"
+ "v24@?0{sharedmem_pagerange=QQ}8"
+ "waitForSleepCycleCompletion not called with workLoop Gate held!"
+ "writeFileInternal(client:catInfo:name:offset:length:encrypted:inputBuffer:)"
- " opted into prefers-waiting-through-sleep; option accepted but not yet implemented"
- "430.40.5"
- "@(#)VERSION:ExclaveOS Image4 Framework Version 7.0.0: Sat Sep 12 05:10:17 PDT 2026; root:AppleImage4_exclavecore-374~18509/ExclaveImage4/RELEASE_ARM64E"
- "ANEExclave version: ANEExclave_exclavecore-13.101.1"
- "Build Date: Sat Sep 12 04:43:50 PDT 2026"
- "DeviceInfoH19P: target "
- "DeviceInfoH19P: target %s authenticAppleDisplay=%{bool}d (edtPath: %s)"
- "ExclaveCameraSISP-20.105.6"
- "ExclaveOS Image4 Framework Version 7.0.0: Sat Sep 12 05:10:17 PDT 2026; root:AppleImage4_exclavecore-374~18509/ExclaveImage4/RELEASE_ARM64E"
- "In-flight HW requests present, deferring DART unmap"
- "Initialized count set to greater than specified capacity."
- "Unsupported tunable target: "
- "[SecurePairingCoreComponent]: Could not start storage: "
- "localmap_map(%zx): localmap() remap with changed PA (%llx != %llx)\n"
- "sharedmem_framemap_getPhysicalAddresses"
- "sharedmem_framemap_setMapped"
- "storage not ready"
- "writeFileInternal(client:catInfo:name:offset:length:encrypted:)"
```
