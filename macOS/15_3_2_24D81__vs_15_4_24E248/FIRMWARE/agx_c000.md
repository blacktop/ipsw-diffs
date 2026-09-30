## agx_c000

> `agx_c000`

```diff

 
-  __TEXT.__text: 0x4fd24
-  __TEXT.__gxf_shr_code: 0x560
-  __TEXT.__gxf_code: 0x1238
+  __TEXT.__text: 0x4f66c
+  __TEXT.__gxf_shr_code: 0x55c
+  __TEXT.__gxf_code: 0x1230
   __TEXT.__gxf_code_pad: 0x0
-  __TEXT.__const: 0x1cbc
-  __TEXT._rtk_patchbay: 0x208
+  __TEXT.__const: 0x2300
+  __TEXT._rtk_patchbay: 0x228
   __TEXT._rtk_tunables: 0x5b0
   __TEXT.__chain_starts: 0x28
-  __TEXT.__cstring: 0x1d74
+  __TEXT.__cstring: 0x2587
   __DATA.__gxf_data: 0x4200
   __DATA.__data: 0xda8
-  __DATA.__const: 0x5c0
+  __DATA.__const: 0x8c0
   __DATA._rtk_init_stack: 0x4000
   __DATA._rtk_irq_stack: 0x4000
   __DATA._rtk_exc_stack: 0x4000

   __DATA.__constructor: 0x0
   __DATA.__xnu_shared: 0x3c000
   __DATA._rtk_mtab: 0x390
-  __DATA.__zerofill: 0x67178
-  UUID: 4DD59941-9AE1-36E5-8256-A82591876ECF
-  Functions: 482
-  Symbols:   225
-  CStrings:  206
+  __DATA.__zerofill: 0x67598
+  UUID: E022A8FA-D8CB-313C-AB2C-9ED7AADB0CEF
+  Functions: 492
+  Symbols:   227
+  CStrings:  261
 
Symbols:
+ __rtk_patch_RTK_platform_flags
+ __rtk_patch__pac_entropy
CStrings:
+ "AGFHALGetVDSIDQuotaLinesUsed"
+ "AGFHALMCWWaitForIdle"
+ "AGFHALPBDescTableFlush"
+ "AGFHALWaitForMGPUReqCleared"
+ "AGFHALWaitForPerfState"
+ "ERROR: PIO poll%s%s timeout after %uus [type:%d reg:0x%x expected:0x%llx got:0x%llx max:%uus], continue wait"
+ "GFX %s %u %s FW %s! (%s)"
+ "Mar 19 2025 21:19:09"
+ "PIO poll%s%s timeout after %uus [type:%d reg:0x%x expected:0x%llx got:0x%llx max:%uus]"
+ "_agfGL2DependentPollReg32"
+ "agfGCPMSDisable"
+ "agfGCPMSEnable"
+ "agfGCPMSUpdateDashboard"
+ "agfPollUSCProfileIdle"
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
+ "kAGFIPIORegionTypeMTRPMSRegisters"
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
- "ERROR: Unknown DM (%d) in AGFCheckProgressGPU"
- "GFX %s %s FW %s! (%s)"
- "Jan  2 2025 20:18:18"
- "agfGL2DependentPollReg32"
- "agfPollFenderReg"
- "agfPollFenderRegIgnoreRecovery"

```
