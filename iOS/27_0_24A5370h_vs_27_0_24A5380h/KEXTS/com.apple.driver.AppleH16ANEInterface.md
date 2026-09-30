## com.apple.driver.AppleH16ANEInterface

> `com.apple.driver.AppleH16ANEInterface`

```diff

-  __TEXT.__const: 0x1050
-  __TEXT.__cstring: 0x11346
-  __TEXT.__os_log: 0x39e6a
-  __TEXT_EXEC.__text: 0x143c04
-  __TEXT_EXEC.__auth_stubs: 0x1220
+  __TEXT.__const: 0x1030
+  __TEXT.__cstring: 0x11588
+  __TEXT.__os_log: 0x3ac29
+  __TEXT_EXEC.__text: 0x1476a8
+  __TEXT_EXEC.__auth_stubs: 0x1250
   __DATA.__data: 0x482c
   __DATA.__common: 0x7b0
-  __DATA.__bss: 0x810
-  __DATA_CONST.__mod_init_func: 0x2e8
+  __DATA.__bss: 0x818
+  __DATA_CONST.__mod_init_func: 0x2f0
   __DATA_CONST.__mod_term_func: 0x128
-  __DATA_CONST.__const: 0xf8b0
-  __DATA_CONST.__kalloc_type: 0x6b00
-  __DATA_CONST.__kalloc_var: 0x8610
-  __DATA_CONST.__auth_got: 0x910
+  __DATA_CONST.__const: 0xf950
+  __DATA_CONST.__kalloc_type: 0x6c80
+  __DATA_CONST.__kalloc_var: 0x8890
+  __DATA_CONST.__auth_got: 0x928
   __DATA_CONST.__got: 0x140
   __DATA_CONST.__auth_ptr: 0x8
-  Functions: 4869
+  Functions: 4916
   Symbols:   0
-  CStrings:  5132
+  CStrings:  5204
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
CStrings:
+ "%s: %s: ANE %u power readiness: %u\n"
+ "%s: %s: ANE_SYS power on after FSD:%u\n"
+ "%s: %s: Client %s has set an entitlement opt out of bonded mode. This request will be honored if there is no explicit user hint in the inference request to allow bonded mode\n"
+ "%s: %s: Core %u, powerReadiness %u, preference %d\n"
+ "%s: %s: Created the thermal slew rate timer event source.\n"
+ "%s: %s: Disabling Thermal Slew Rate monitoring for cluster %d"
+ "%s: %s: Enabling Thermal Slew Rate monitoring for cluster %d"
+ "%s: %s: Initializing thermal slew rate management with 1 cluster\n"
+ "%s: %s: Setup register block for MTR cluster and all sensors\n"
+ "%s: %s: Shared iPad - checking further filePath: %s\n"
+ "%s: %s: Shared iPad DataVault verification succeeded\n"
+ "%s: %s: Successfully configured MTR slew rate interrupt for cluster at EDT index %u\n"
+ "%s: %s: Thermal Slew Rate Interrupt Is Valid for cluster ID %d Sensor ID %d"
+ "%s: %s: Thermal Slew Rate interval EDT entry has incorrect length: %u (expected 4)\n"
+ "%s: %s: Thermal Slew Rate interval for timeout EDT entry not found\n"
+ "%s: %s: Thermal Slew Rate interval for timeout from EDT: %u\n"
+ "%s: %s: ane-arg-support is required, set fANERailGatingMode\n"
+ "%s: %s: enterShutdown: kicking maintenance timer to drain %u inactive resource(s) (retry %u/%u)\n"
+ "%s: %s: enterShutdown: waiting for resources to drain (inactive: %s, unwire queue: %u)\n"
+ "%s: %s: waitForUnwireThreadToDrain: timed out, retrying\n"
+ "/.resolve/2%s"
+ "/Library/Caches/com.apple.aned/"
+ "/private/var/MobileAsset/AssetsV2/"
+ "/private/var/Users/"
+ "/private/var/mobile/Library/AppleIntelligencePlatform/AppModelAssets/"
+ "/private/var/mobile/Library/Caches/com.apple.aned/"
+ "1112211112"
+ "11122222111111111221122222111111011112222211112111211222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211222012212021111111"
+ "22221"
+ "AneEngine_C.c"
+ "MTRCluster"
+ "[ERROR] %s: %s: ANEUnionResource: failed to restore dartMap state result=0x%x\n"
+ "[ERROR] %s: %s: ANEUnionResource: failed to restore wire state result=0x%x\n"
+ "[ERROR] %s: %s: ANE_AddClientForProgram: rejected — shutdown in progress\n"
+ "[ERROR] %s: %s: ANE_DoProgramCreate: rejected — shutdown in progress\n"
+ "[ERROR] %s: %s: ANE_DoProgramCreateInstance: rejected — shutdown in progress\n"
+ "[ERROR] %s: %s: Cannot wire intermediateBuffer at load time programHandle: 0x%llx\n"
+ "[ERROR] %s: %s: Couldn't add timer event source to work loop.\n"
+ "[ERROR] %s: %s: Couldn't create MTRSensor instance %d for cluster %d.\n"
+ "[ERROR] %s: %s: ERROR: Failed to lookup file at %s err=%d\n"
+ "[ERROR] %s: %s: Failed prepareKernelSplitSections for base instance - 0x%llx: 0x%x\n"
+ "[ERROR] %s: %s: Failed to add MTR slew rate interrupt event source for cluster\n"
+ "[ERROR] %s: %s: Failed to allocate anecMutableWeightFileData for %u entries\n"
+ "[ERROR] %s: %s: Failed to allocate instanceKernelSplitSections for programHandle: 0x%llx\n"
+ "[ERROR] %s: %s: Failed to allocate prepare request for base-instance kernel splits - 0x%llx\n"
+ "[ERROR] %s: %s: Failed to allocate symbol storage for %u entries\n"
+ "[ERROR] %s: %s: Failed to allocate wireRequest for intermediateBuffer programHandle: 0x%llx\n"
+ "[ERROR] %s: %s: Failed to copy kernel split section for programHandle: 0x%llx procId: %u\n"
+ "[ERROR] %s: %s: Failed to create MTR slew rate interrupt event source for cluster\n"
+ "[ERROR] %s: %s: Failed to create MTR slew rate timer event source for cluster\n"
+ "[ERROR] %s: %s: Failed to prepare base-instance kernel splits - 0x%llx: 0x%x\n"
+ "[ERROR] %s: %s: Failed to size process procedureKernelSplitSections for programHandle: 0x%llx\n"
+ "[ERROR] %s: %s: Failed to wait for DPG-disable on persistent client: res=0x%08X\n"
+ "[ERROR] %s: %s: Inference not permitted: client attempted inference while in background. machoFileSize=0x%llx ProgramHandle: 0x%llx isClientApplication: %d isEntitledToRunBackgroundInference: %d\n"
+ "[ERROR] %s: %s: MTR cluster is null\n"
+ "[ERROR] %s: %s: MTR slew rate interrupt/timer setup failed: 0x%x\n"
+ "[ERROR] %s: %s: MTRCluster: invalid arguments to setupInterruptAndTimer\n"
+ "[ERROR] %s: %s: MTRCluster: workloop unavailable for slew rate setup\n"
+ "[ERROR] %s: %s: Post-schedule takePowerAssertion failed: 0x%x (continuing; dispatch path will retry)\n"
+ "[ERROR] %s: %s: Process kernel split count exceeds kANEMaxBars for programHandle: 0x%llx procId: %u\n"
+ "[ERROR] %s: %s: Shared iPad - clientInDataVault: %d clientFilePath: %s\n"
+ "[ERROR] %s: %s: createCopy: memoryDescriptor is null\n"
+ "[ERROR] %s: %s: numWeightsBuffer %u exceeds max %u\n"
+ "[ERROR] %s: %s: waitForUnwireThreadToDrain: timed out (inactive: %s, unwire queue: %u)\n"
+ "[INFO] %s: %s: Enabling Thermal Slew Rate cluster\n"
+ "[INFO] %s: %s: Starting timer for disabled cluster\n"
+ "[INFO] %s: %s: Thermal Sensor ID %d - RDBK : 0x%x, Direction: %u, Temperature: %u, MaxDeltaTemp: %u"
+ "[INFO] %s: %s: Thermal Slew Rate Interrupt Occurred for cluster ID %d\n"
+ "[INFO] %s: %s: Thermal Slew Rate interrupt occured for cluster\n"
+ "[INFO] %s: %s: Thermal Slew Rate timer timeout occured\n"
+ "aneSlewRateInterruptHandler_gated"
+ "aneVnodeSecureLookup"
+ "com.apple.ane.singleCopyIntermediateBuffer.allow"
+ "com.apple.ane.wireIntermediateBufferAtLoadTime.allow"
+ "com.apple.developer.background-tasks.continued-processing.inference"
+ "com.apple.private.ane.bonded.allow"
+ "createCopy"
+ "disableSlewRateMonitoring"
+ "enableSlewRateMonitoring"
+ "handleSlewRateInterrupt_gated"
+ "handleSlewRateTimer_gated"
+ "no"
+ "prepareKernelSplitSections"
+ "readRDBK"
+ "setupInterruptAndTimer"
+ "site.MTRCluster"
+ "site.MTRSensor"
+ "thermal-slew-rate-interval"
+ "thermalSlewInterruptOccured"
+ "yes"
- "%s: %s: ERROR: Failed to lookup macho file at %s\n"
- "%s: %s: Rotating to next ANE %u with same preference %u\n"
- "%s: %s: System shutdown in progress, nothing to do \n"
- "%s: %s: Wrapping around to ANE %u with same preference %u\n"
- "%s: %s: ane-arg-support is required, set fANEDriverARGSupport\n"
- "%s: %s: enterShutdown: draining %zu inactive resource(s)\n"
- "%s: %s: enterShutdown: no inactive resources to drain\n"
- "%s: %s: enterShutdown: resource 0x%llx no longer inactive, skipping unwire\n"
- "%s: %s: enterShutdown: waiting for unwire thread to drain %u resource(s)\n"
- "%s: %s: waitForUnwireThreadToDrain: timed out, retrying (queue size: %u)\n"
- "/private/var/MobileAsset/AssetsV2"
- "/private/var/mobile/Library/AppleIntelligencePlatform/AppModelAssets"
- "/private/var/mobile/Library/Caches/com.apple.aned"
- "1112222211111111122112222211111101111222221111211121122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221122201221202"
- "AneEngine_tightbeam.c"
- "[ERROR] %s: %s: Inference not permitted: client application with large model (machoFileSize=0x%llx) attempted inference while in background. ProgramHandle: 0x%llx\n"
- "aneVnodeLookup"
- "drainInactiveResourcesOnShutdown"

```
