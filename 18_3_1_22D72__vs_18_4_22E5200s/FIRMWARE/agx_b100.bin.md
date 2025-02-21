## agx_b100.bin

> `agx_b100.bin`

```diff

 
-  __TEXT.__text: 0x345c4
-  __TEXT.__gxf_shr_code: 0x560
-  __TEXT.__gxf_code: 0x1238
+  __TEXT.__text: 0x34af4
+  __TEXT.__gxf_shr_code: 0x55c
+  __TEXT.__gxf_code: 0x1230
   __TEXT.__gxf_code_pad: 0x0
-  __TEXT.__const: 0x1868
-  __TEXT._rtk_patchbay: 0x208
+  __TEXT.__const: 0x20fc
+  __TEXT._rtk_patchbay: 0x228
   __TEXT._rtk_tunables: 0x6a0
   __TEXT.__chain_starts: 0x2c
-  __TEXT.__cstring: 0x1b11
+  __TEXT.__cstring: 0x22af
   __DATA.__gxf_data: 0x4200
   __DATA.__data: 0x14a18
-  __DATA.__const: 0x2d0
+  __DATA.__const: 0x5c0
   __DATA._rtk_init_stack: 0x4000
   __DATA._rtk_irq_stack: 0x4000
   __DATA._rtk_exc_stack: 0x4000

   __DATA.__constructor: 0x0
   __DATA.__xnu_shared: 0x3c000
   __DATA._rtk_mtab: 0x390
-  __DATA.__zerofill: 0x57bd8
-  Functions: 409
-  Symbols:   228
-  CStrings:  185
+  __DATA.__zerofill: 0x58018
+  Functions: 416
+  Symbols:   230
+  CStrings:  235
 
Symbols:
+ __rtk_patch_RTK_platform_flags
+ __rtk_patch__pac_entropy
CStrings:
+ "AGFHALGetVDSIDQuotaLinesUsed"
+ "AGFHALKSMKickQueuesSchedulingPause"
+ "AGFHALMCWWaitForIdle"
+ "AGFHALPBDescTableFlush"
+ "ERROR: PIO poll%s%s timeout after %uus [type:%d reg:0x%x expected:0x%llx got:0x%llx max:%uus], continue wait"
+ "Feb 16 2025 05:31:46"
+ "GFX %s %u %s FW %s! (%s)"
+ "PIO poll%s%s timeout after %uus [type:%d reg:0x%x expected:0x%llx got:0x%llx max:%uus]"
+ "_agfGL2DependentPollReg32"
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
- "Invalid recovery phase = %d"
- "Jan 16 2025 05:29:21"
- "agfGL2DependentPollReg32"
- "agfPollFenderReg"

```
