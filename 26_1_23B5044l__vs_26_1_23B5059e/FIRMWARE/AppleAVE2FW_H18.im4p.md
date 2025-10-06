## AppleAVE2FW_H18.im4p

> `AppleAVE2FW_H18.im4p`

```diff

 
-  __TEXT.__text: 0x105c40
-  __TEXT.__const: 0x20614
-  __TEXT.__cstring: 0x16a72
+  __TEXT.__text: 0x108520
+  __TEXT.__const: 0x20634
+  __TEXT.__cstring: 0x1708a
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x20
-  __DATA.__const: 0x3978
+  __DATA.__const: 0x39b0
   __DATA._rtk_patchbay: 0x211
   __DATA.__data: 0x1700
   __DATA._rtk_mtab: 0x320

   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0xc67f8
-  UUID: 8F3324E4-78AC-371D-B165-3C5EC6A56ACA
-  Functions: 1195
-  Symbols:   1678
-  CStrings:  2566
+  __DATA.__zerofill: 0xc6838
+  UUID: 80FDB373-89F3-30B4-9093-B5FF902572CD
+  Functions: 1212
+  Symbols:   1701
+  CStrings:  2638
 
Symbols:
+ __Z11AVE_Cfg_Getv
+ __Z12AVE_DPM_InitP11AVE_DevInfoPK10_S_AVE_Cfg
+ __Z12AVE_PSD_Initv
+ __Z13AVE_PMGR_InitP11AVE_DevInfo
+ __Z13AVE_PSD_SetPS14_E_AVE_PSDSlot14_E_AVE_PMGR_PS
+ __Z14AVE_DPM_Uninitv
+ __Z14AVE_PMGR_SetPS14_E_AVE_PMGR_PD14_E_AVE_PMGR_PSb
+ __Z14AVE_PSD_Uninitv
+ __Z15AVE_PMGR_Uninitv
+ __Z16AVE_DPM_TuneUpHwj
+ __Z17AVE_Cfg_UpdateDPMj
+ __Z18AVE_CSC_IRQ_Enableii
+ __Z18AVE_DPM_TuneDownHwj
+ __Z18AVE_PMGR_EnableDPMv
+ __Z19AVE_PMGR_DisableDPMv
+ __Z19AVE_PMGR_Get_erebus14_E_AVE_PMGR_PDP14_E_AVE_PMGR_PS
+ __Z19AVE_PMGR_Set_erebus14_E_AVE_PMGR_PD14_E_AVE_PMGR_PS
+ __Z20AVE_DevCap_FindPDMap12_E_AVE_DevID
+ __Z22AVE_DPM_CalcDPMHwStatsjjjjjjjjjjjjj
+ __Z24AVE_PMGR_CheckDMA_erebus14_E_AVE_PMGR_PS
+ __Z25AVE_PMGR_EnableDPM_erebusv
+ __Z26AVE_PMGR_DisableDPM_erebusv
+ __Z26AVE_PMGR_EnableIdle_erebusv
CStrings:
+ "%s Enter"
+ "%s Enter %d %d"
+ "%s Enter %d %d %d"
+ "%s Enter %p"
+ "%s Enter %p %d"
+ "%s Enter %p %d %d %d"
+ "%s Enter %p %p"
+ "%s Enter 0x%x"
+ "%s Enter 0x%x %d"
+ "%s Enter 0x%x %d %d"
+ "%s Exit %d"
+ "%s Exit %d %d %d"
+ "%s Exit %d %d %d %d"
+ "%s Exit %p %d"
+ "%s Exit %p %d %d"
+ "%s Exit %p %d %d %d %d"
+ "%s Exit %p %p %d"
+ "%s Exit 0x%x %d"
+ "%s Exit 0x%x %d %d"
+ "%s Exit 0x%x %d %d %d"
+ "%s:%d %s | fail to enable DPM %p %p"
+ "%s:%d %s | fail to init PMGR %p %p"
+ "%s:%d %s | fail to init PSD %d"
+ "%s:%d %s | fail to power on PSD %d"
+ "%s:%d %s | fail to set power domain %d off"
+ "%s:%d %s | fail to set power domain %d on"
+ "%s:%d %s | failed to set power state %s %s %d"
+ "%s:%d %s | power domain %s is not supported/enabled %d %d %d"
+ "%s:%d %s | power management is not supported"
+ "%s:%d %s | wrong parameters %d %d"
+ "%s:%d %s | wrong parameters %p"
+ "%s:%d failed to destroy PSD %d"
+ "%s:%d failed to disable PMGR %d"
+ "%s:%d failed to power off %d"
+ "%s:%d failed to uninit PMGR %d"
+ "%s:%d keep power state %d %d"
+ "%s:%d set power state %s (%s <- %s)"
+ "%s:%d set power time out %d 0x%x"
+ "./AppleAVE2FW/Firmware/PMGR/AVE_PMGR_erebus.cpp"
+ "9003.68.0"
+ "AVE_DPM_Init"
+ "AVE_DPM_TuneDownHw"
+ "AVE_DPM_TuneUpHw"
+ "AVE_DPM_Uninit"
+ "AVE_PMGR_DisableDPM"
+ "AVE_PMGR_EnableDPM"
+ "AVE_PMGR_Init"
+ "AVE_PMGR_SetPS"
+ "AVE_PMGR_Set_erebus"
+ "AVE_PMGR_Uninit"
+ "CheckPDDepDown"
+ "CheckPDDepUp"
+ "CheckPSFlagDown"
+ "CheckPSFlagUp"
+ "CheckPeerDown"
+ "FE"
+ "HME"
+ "MDINTER"
+ "MDINTRA"
+ "ME"
+ "Off"
+ "On"
+ "SetPSDependencyDown"
+ "SetPSDependencyUp"
+ "SetPSDown"
+ "SetPSUp"
+ "SetPowerState"
+ "gs_sAVE_PMGR.piPDMap[pd] >= 0"
+ "gs_sAVE_PMGR.psPDMap != NULL"
+ "pDevInfo != __null"
+ "pDevInfo != __null && pCfg != __null"
+ "pPDMap != __null"
+ "pd < AVE_PMGR_PD_Max && ps < AVE_PMGR_PS_Max"
- "9003.60.0"

```
