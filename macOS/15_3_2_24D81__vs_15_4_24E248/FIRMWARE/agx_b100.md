## agx_b100

> `agx_b100`

```diff

 
-  __TEXT.__text: 0x3cd04
-  __TEXT.__gxf_shr_code: 0x560
-  __TEXT.__gxf_code: 0x12c0
+  __TEXT.__text: 0x3db58
+  __TEXT.__gxf_shr_code: 0x55c
+  __TEXT.__gxf_code: 0x12b8
   __TEXT.__gxf_code_pad: 0x0
-  __TEXT.__const: 0x1704
-  __TEXT._rtk_patchbay: 0x208
+  __TEXT.__const: 0x1d88
+  __TEXT._rtk_patchbay: 0x228
   __TEXT._rtk_tunables: 0x1e8
   __TEXT.__chain_starts: 0x20
-  __TEXT.__cstring: 0x158a
+  __TEXT.__cstring: 0x1c49
   __DATA.__gxf_data: 0x4200
   __DATA.__data: 0xc30
-  __DATA.__const: 0x4f8
+  __DATA.__const: 0x7e8
   __DATA._rtk_init_stack: 0x4000
   __DATA._rtk_irq_stack: 0x4000
   __DATA._rtk_exc_stack: 0x4000

   __DATA.__constructor: 0x0
   __DATA.__xnu_shared: 0x3c000
   __DATA._rtk_mtab: 0x260
-  __DATA.__zerofill: 0x51b78
-  UUID: 9EDCD09B-348F-39FC-AF15-0BFE28E9E282
-  Functions: 396
-  Symbols:   211
-  CStrings:  155
+  __DATA.__zerofill: 0x51f98
+  UUID: A4D4B3EA-D5E5-3A9C-9813-69447613C73D
+  Functions: 407
+  Symbols:   213
+  CStrings:  203
 
Symbols:
+ __rtk_patch_RTK_platform_flags
+ __rtk_patch__pac_entropy
CStrings:
+ "AGFHALPBDescTableFlush"
+ "AGFHALWaitForMGPUReqCleared"
+ "AGFHALWaitForPerfState"
+ "GFX %s %u %s FW %s! (%s)"
+ "Mar 19 2025 21:18:27"
+ "_agfGL2DependentPollReg32"
+ "agfDCPMSTraceStop"
+ "agfGCPMSDisable"
+ "agfGCPMSEnable"
+ "agfGCPMSUpdateDashboard"
+ "kAGFIPIORegionTypeAFRClkGenRegisters"
+ "kAGFIPIORegionTypeAFRClkGenRegisters1"
+ "kAGFIPIORegionTypeAFRRegisters"
+ "kAGFIPIORegionTypeAICBankedRegisters"
+ "kAGFIPIORegionTypeANE0Registers"
+ "kAGFIPIORegionTypeANE1Registers"
+ "kAGFIPIORegionTypeAONPTDSpace"
+ "kAGFIPIORegionTypeAVMRControllerFastRegisters"
+ "kAGFIPIORegionTypeCRERegisters"
+ "kAGFIPIORegionTypeDVFMAFRRegisters"
+ "kAGFIPIORegionTypeDVFMMgpuRegisters"
+ "kAGFIPIORegionTypeDisplayURMagic"
+ "kAGFIPIORegionTypeDpwrMXURegisters"
+ "kAGFIPIORegionTypeFenderRegsAFRNIA"
+ "kAGFIPIORegionTypeFenderRegsBumper"
+ "kAGFIPIORegionTypeFenderRegsDFenderCSCfg"
+ "kAGFIPIORegionTypeFenderRegsDFenderMGPUCfg"
+ "kAGFIPIORegionTypeFenderRegsDFenderPowerTransG16G"
+ "kAGFIPIORegionTypeFenderRegsGCPMS"
+ "kAGFIPIORegionTypeFenderRegsGFenderCfg"
+ "kAGFIPIORegionTypeFenderRegsIVDM"
+ "kAGFIPIORegionTypeFenderRegsLegacyDPECfg"
+ "kAGFIPIORegionTypeFenderRegsLegacyFenderCfg"
+ "kAGFIPIORegionTypeFenderRegsLegacyGFXCfg"
+ "kAGFIPIORegionTypeFenderRegsMCW"
+ "kAGFIPIORegionTypeFenderRegsPRC"
+ "kAGFIPIORegionTypeFenderRegsScratchRam"
+ "kAGFIPIORegionTypeGFXCAXI2AFRegisters"
+ "kAGFIPIORegionTypeGFXCLKGENMGPU"
+ "kAGFIPIORegionTypeGMGIFAFRegisters"
+ "kAGFIPIORegionTypeGPCAICSWInt"
+ "kAGFIPIORegionTypeMCacheG11Plane0Registers"
+ "kAGFIPIORegionTypeMCacheG11Plane1Registers"
+ "kAGFIPIORegionTypeMCacheG11Plane2Registers"
+ "kAGFIPIORegionTypeMCacheG11Plane3Registers"
+ "kAGFIPIORegionTypeMCacheRegisters"
+ "kAGFIPIORegionTypeMTRRegisters"
+ "kAGFIPIORegionTypePMGRScratch"
+ "kAGFIPIORegionTypePMPDoorbell"
+ "kAGFIPIORegionTypePushTelemetryDashboard"
+ "kAGFIPIORegionTypePushTelemetryDashboardConfigSpace"
+ "kAGFIPIORegionTypePushTelemetryDashboardReadSpace"
+ "kAGFIPIORegionTypeSpecialAgentIdleDie0"
+ "kAGFIPIORegionTypeSpecialAgentIdleDie1"
+ "kAGFIPIORegionTypeTempSensorRegister"
+ "kAGFIPIORegionTypeThrtlStatCntrsRegisters"
+ "kAGFIPIORegionTypeUTRegisters"
- "\tAONPTD@0x%llX->0x%llX/0x%X"
- "AGFASchedulerContextSwitchRequired"
- "ERROR: Unknown DM (%d) in AGFCheckProgressGPU"
- "GFX %s %s FW %s! (%s)"
- "Invalid DM %d in %s\n"
- "Jan  2 2025 20:17:36"
- "agfGL2DependentPollReg32"
- "agfPollFenderReg"
- "agfPollFenderRegIgnoreRecovery"

```
