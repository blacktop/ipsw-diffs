## agx_a000

> `agx_a000`

```diff

 
-  __TEXT.__text: 0x49f3c
-  __TEXT.__gxf_shr_code: 0x560
-  __TEXT.__gxf_code: 0x1238
+  __TEXT.__text: 0x4a450
+  __TEXT.__gxf_shr_code: 0x55c
+  __TEXT.__gxf_code: 0x1230
   __TEXT.__gxf_code_pad: 0x0
-  __TEXT.__const: 0xe28
-  __TEXT._rtk_patchbay: 0x208
+  __TEXT.__const: 0x11cc
+  __TEXT._rtk_patchbay: 0x228
   __TEXT._rtk_tunables: 0x6a0
   __TEXT.__chain_starts: 0x28
-  __TEXT.__cstring: 0x28a0
+  __TEXT.__cstring: 0x30dc
   __DATA.__gxf_data: 0x4200
-  __DATA.__data: 0x14788
-  __DATA.__const: 0x650
+  __DATA.__data: 0x14798
+  __DATA.__const: 0x950
   __DATA._rtk_init_stack: 0x4000
   __DATA._rtk_irq_stack: 0x4000
   __DATA._rtk_exc_stack: 0x4000

   __DATA.__constructor: 0x0
   __DATA.__xnu_shared: 0x3c000
   __DATA._rtk_mtab: 0x400
-  __DATA.__zerofill: 0x5b4b8
-  UUID: 49C9C8B9-E1E0-37BA-A811-F9C371BEE472
-  Functions: 495
-  Symbols:   231
-  CStrings:  259
+  __DATA.__zerofill: 0x5b978
+  UUID: 0A56FBF0-7F48-31AA-9AB0-D8CF9FD048ED
+  Functions: 502
+  Symbols:   233
+  CStrings:  316
 
Symbols:
+ __rtk_patch_RTK_platform_flags
+ __rtk_patch__pac_entropy
CStrings:
+ "AGFHALGetVDSIDQuotaLinesUsed"
+ "AGFHALKSMKickQueuesSchedulingPause"
+ "AGFHALMCWWaitForIdle"
+ "AGFHALPBDescTableFlush"
+ "AGFHALPreInactivePowerStateChange"
+ "AGFHALWaitForAfrPerfStateCompletion"
+ "AGFHALWaitForMGPUReqCleared"
+ "AGFHALWaitForPerfState"
+ "AGFHALWaitForPerfStateAFR"
+ "Buffer size is too small to hold all counter values"
+ "ERROR: PIO poll%s%s timeout after %uus [type:%d reg:0x%x expected:0x%llx got:0x%llx max:%uus], continue wait"
+ "GFX %s %u %s FW %s! (%s)"
+ "Mar 19 2025 21:14:46"
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
- "%s: !!! Fatal Error: Parameter buffer pages leaked for PBID %d, rebuild [%d]!"
- "ERROR: Unknown DM (%d) in AGFCheckProgressGPU"
- "GFX %s %s FW %s! (%s)"
- "Invalid recovery phase = %d"
- "Jan  2 2025 20:14:20"
- "agfGL2DependentPollReg32"
- "agfPollFenderReg"
- "agfPollFenderRegIgnoreRecovery"
- "agfaParamBufferManagerUnbindPBState"

```
