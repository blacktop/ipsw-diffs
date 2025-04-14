# 18.5 (22F5042g) .vs 18.5 (22F5053f)

## IPSWs

- `iPhone17,1_18.5_22F5042g_Restore.ipsw`
- `iPhone17,1_18.5_22F5053f_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 18.5 *(22F5042g)* | 24.5.0 | 11417.120.80.0.3~45 | Mon, 24Mar2025 20:10:57 PDT |
| 18.5 *(22F5053f)* | 24.5.0 | 11417.120.96.502.1~1 | Thu, 10Apr2025 21:44:12 PDT |

### Kexts

#### ⬆️ Updated (23)

<details>
  <summary><i>View Updated</i></summary>

>  `com.apple.EXBrightKext`

```diff

-1902.120.16.0.0
+1902.120.20.0.0
   __TEXT.__const: 0xb0
-  __TEXT.__cstring: 0x20ce
-  __TEXT_EXEC.__text: 0xd468
+  __TEXT.__cstring: 0x2118
+  __TEXT_EXEC.__text: 0xd5b0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd8
   __DATA.__common: 0x68

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0x17e8
   __DATA_CONST.__kalloc_type: 0x80
-  Functions: 334
+  Functions: 333
   Symbols:   0
   CStrings:  141
 
CStrings:
+ "[%s] [ERR] Could not add _upcallNotificationES to workloop!\n"
+ "[%s] [ERR] Could not configure upcall notifications!\n"
+ "[%s] [ERR] Failed to setup upcall notifications!\n"
+ "[%s] [ERR] Unknown type of xtalk estimate\n"
- "\"%s\" @%s:%d"
- "Could not add _upcallNotificationES to workloop!"
- "Could not configure upcall notifications!"
- "Unknown type of xtalk estimate"

```

>  `com.apple.driver.AppleAVE2`

```diff

-803.63.3.0.0
+803.71.1.0.0
   __TEXT.__const: 0x2ef60
-  __TEXT.__cstring: 0x35335
-  __TEXT.__os_log: 0x3ffe3
-  __TEXT_EXEC.__text: 0x14437c
+  __TEXT.__cstring: 0x3567a
+  __TEXT.__os_log: 0x40bb0
+  __TEXT_EXEC.__text: 0x14789c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x290
   __DATA.__common: 0x130

   __DATA_CONST.__const: 0x6318
   __DATA_CONST.__kalloc_type: 0x3f80
   __DATA_CONST.__kalloc_var: 0x1b80
-  Functions: 2440
+  Functions: 2450
   Symbols:   0
-  CStrings:  6961
+  CStrings:  6981
 
CStrings:
+ "%lld %d AVE %s: %s:%d %p %d %p %d | %d %d %d %d %d %d | %d %d %d %d"
+ "%lld %d AVE %s: %s:%d %p %d %p %d | %d %d %d %d %d %d | %d %d %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | Client Type is invalid %p %d %d"
+ "%lld %d AVE %s: %s:%d %s | Client Type is invalid %p %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | Priority value is OOB %p %d %d"
+ "%lld %d AVE %s: %s:%d %s | Priority value is OOB %p %d %d\n"
+ "%lld %d AVE %s: %s::%s %p %p %d | %p %d %d"
+ "%lld %d AVE %s: %s::%s %p %p %d | %p %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d %p %d %p %d | %d %d %d %d %d %d | %d %d %d %d"
+ "%lld %d AVE %s: %s::%s:%d %p %d %p %d | %d %d %d %d %d %d | %d %d %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | wrong WP command sequence %p %d | %p %d %p %d | %p 0x%x 0x%x"
+ "%lld %d AVE %s: %s::%s:%d %s | wrong WP command sequence %p %d | %p %d %p %d | %p 0x%x 0x%x\n"
+ "%lld %d AVE %s: %s::%s:%d failed to send Work Pool command priority %p %d | %p %d %p %d | %p %d"
+ "%lld %d AVE %s: %s::%s:%d failed to send Work Pool command priority %p %d | %p %d %p %d | %p %d\n"
+ "%lld %d AVE %s: %s::%s:%d failed to send firmware command priority %p %d | %p %d %p %d | %p %d"
+ "%lld %d AVE %s: %s::%s:%d failed to send firmware command priority %p %d | %p %d %p %d | %p %d\n"
+ "%lld %d AVE %s: %s::%s:%d total number of commands %p %d | %p %d %lld %p %d | %d %d %d %d | %d %d  %d %d %d %d %d | %d"
+ "%lld %d AVE %s: %s::%s:%d total number of commands %p %d | %p %d %lld %p %d | %d %d %d %d | %d %d  %d %d %d %d %d | %d\n"
+ "%lld %d AVE %s: %s::%s:%d total number of commands %p %d | %p %d %lld %p %d | %d %d %d %d | %d %d %d %d %d %d %d | %d"
+ "%lld %d AVE %s: %s::%s:%d total number of commands %p %d | %p %d %lld %p %d | %d %d %d %d | %d %d %d %d %d %d %d | %d\n"
+ "%lld %d AVE %s: %s::%s:%d total number of commands %p %d | %p %d %p %d | %d %d %d %d | %d %d %d %d %d %d %d"
+ "%lld %d AVE %s: %s::%s:%d total number of commands %p %d | %p %d %p %d | %d %d %d %d | %d %d %d %d %d %d %d\n"
+ "%lld %d AVE %s: Firmware Command Max: %d %d %d Flag: 0x%x Count: %d %d %d"
+ "%lld %d AVE %s: Firmware Command Max: %d %d %d Flag: 0x%x Count: %d %d %d\n"
+ "(psCmd != nullptr) && (iSize >= sizeof(S_AVE_WPOutParam_Priority))"
+ "21:48:33"
+ "803.71.1"
+ "AVE_CHM_MakeFwCmd_Priority"
+ "Apr 10 2025"
+ "Assign      14 "
+ "Firmware Command Max: %d %d %d Flag: 0x%x Count: %d %d %d"
+ "Firmware Command Max: %d %d %d Flag: 0x%x Count: %d %d %d\n"
+ "Flush       11 "
+ "Priority    10 "
+ "ProcessNewCmd_Priority"
+ "ProcessReadyCmd_Priority"
+ "ProcessRunCmd_Priority"
+ "Reset       12 "
+ "SendFwCmd_Priority"
+ "SendWPCmd_Priority"
+ "Sync        13 "
+ "Verify      15 "
+ "pClient->eType > AVE_ClientType_None && pClient->eType < AVE_ClientType_Max"
- "%lld %d AVE %s: %s:%d %p %d %p %d | %d %d %d %d | %d %d %d %d"
- "%lld %d AVE %s: %s:%d %p %d %p %d | %d %d %d %d | %d %d %d %d\n"
- "%lld %d AVE %s: %s::%s %p %p %d | %p %d %d %d"
- "%lld %d AVE %s: %s::%s %p %p %d | %p %d %d %d\n"
- "%lld %d AVE %s: %s::%s:%d %p %d %p %d | %d %d %d %d | %d %d %d %d"
- "%lld %d AVE %s: %s::%s:%d %p %d %p %d | %d %d %d %d | %d %d %d %d\n"
- "%lld %d AVE %s: %s::%s:%d total number of commands %p %d | %p %d %lld %p %d | %d %d %d %d | %d %d %d %d %d | %d"
- "%lld %d AVE %s: %s::%s:%d total number of commands %p %d | %p %d %lld %p %d | %d %d %d %d | %d %d %d %d %d | %d\n"
- "%lld %d AVE %s: %s::%s:%d total number of commands %p %d | %p %d %p %d | %d %d %d %d | %d %d %d %d %d"
- "%lld %d AVE %s: %s::%s:%d total number of commands %p %d | %p %d %p %d | %d %d %d %d | %d %d %d %d %d\n"
- "%lld %d AVE %s: Firmware Command Max: %d %d Flag: 0x%x Count: %d %d"
- "%lld %d AVE %s: Firmware Command Max: %d %d Flag: 0x%x Count: %d %d\n"
- "21:22:28"
- "803.63.3"
- "Assign      13 "
- "Firmware Command Max: %d %d Flag: 0x%x Count: %d %d"
- "Firmware Command Max: %d %d Flag: 0x%x Count: %d %d\n"
- "Flush       10 "
- "Mar 24 2025"
- "Priority    15 "
- "Reset       11 "
- "Sync        12 "
- "Verify      14 "

```

>  `com.apple.driver.AppleConvergedIPCOLYBTControl`

```diff

-150.0.0.0.0
+153.0.0.0.0
   __TEXT.__cstring: 0x7cc1
   __TEXT.__const: 0x90
-  __TEXT_EXEC.__text: 0x490d4
+  __TEXT_EXEC.__text: 0x49188
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x1f0

```

>  `com.apple.driver.AppleConvergedPCI`

```diff

-150.0.0.0.0
+153.0.0.0.0
   __TEXT.__const: 0x1e0
   __TEXT.__cstring: 0x6c99
-  __TEXT_EXEC.__text: 0x3fa24
+  __TEXT_EXEC.__text: 0x3f98c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x248
   __DATA.__common: 0x2d0

```

>  `com.apple.driver.AppleH16CameraInterface`

```diff

-3.512.0.0.0
-  __TEXT.__const: 0xa1d0
-  __TEXT.__cstring: 0x17d4b
-  __TEXT.__os_log: 0x1489e
-  __TEXT_EXEC.__text: 0x9ba80
+3.605.0.0.0
+  __TEXT.__const: 0xa110
+  __TEXT.__cstring: 0x17b2f
+  __TEXT.__os_log: 0x140d8
+  __TEXT_EXEC.__text: 0x98e80
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2a0
   __DATA.__common: 0x4c8
   __DATA.__bss: 0x200
-  __DATA_CONST.__auth_got: 0x830
+  __DATA_CONST.__auth_got: 0x828
   __DATA_CONST.__got: 0x1c8
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__mod_init_func: 0x90
   __DATA_CONST.__mod_term_func: 0x50
-  __DATA_CONST.__const: 0xddf0
-  __DATA_CONST.__kalloc_type: 0x1240
+  __DATA_CONST.__const: 0xdbd0
+  __DATA_CONST.__kalloc_type: 0x11c0
   __DATA_CONST.__kalloc_var: 0xa50
-  Functions: 1770
+  Functions: 1737
   Symbols:   0
-  CStrings:  3093
+  CStrings:  3079
 
CStrings:
+ "121111121222121211111"
+ "AppleH16CamIn:%s - EC NVM Read - mask: 0x%06X, ret: 0x%08X\n"
+ "AppleH16CamIn:%s - EC failed to read sensor NVM\n"
+ "AppleH16CamIn:%s - completed - res=%#x epoch=%u\n\n"
+ "AppleH16CamIn:%s - completed - res=%#x numPowerUps=%llu fIsPowered=%u\n\n"
+ "ECNotifyFirmwareTearDown_block_invoke"
+ "ISP_ECReadNVMSequence"
+ "ISP_PowerOnCamera"
+ "checkForWork_block_invoke_3"
- "12111112122212121111111"
- "AppleH16CamIn:%s - Could not allocate memory for SEAR approved exclave client\n"
- "AppleH16CamIn:%s - EC HWIRQ IDL returned an error: req passed = %d ipcRet = %d, tberr = 0x%x\n\n"
- "AppleH16CamIn:%s - Sent Exclave HWIRQ: TBErr=%U\n"
- "AppleH16CamIn:%s - [Exclaves] ISP Engine failed HWIRQ\n"
- "AppleH16CamIn:%s - init SEAR approved IDL call failed\n"
- "AppleH16CamIn:%s - tb_endpointSearApproved is null\n"
- "ECDirtyShutdownSearApproved"
- "ECForceCleanupSearApproved"
- "ECForceResetSearApproved"
- "ECNotifyFirmwareTearDownSearApproved"
- "ECNotifyFirmwareTearDownSearApproved_block_invoke"
- "ECSendCommandHWIRQSearApproved"
- "ECSendCommandMboxIRQSearApproved"
- "ECSendCommandOffSearApproved"
- "ECSendCommandOnSearApproved"
- "checkForWork_block_invoke_5"
- "site.exclavecoreispeng_ispengexclavecore_s"
- "v12@?0B8"
- "v32@?0{exclavecoreispeng_ispengexclavecoreexclaveisphwirqret_s=IIIIIB}8"

```

>  `com.apple.driver.AppleM2ScalerCSCDriver`

```diff

-149.28.4.0.0
+149.50.1.0.0
   __TEXT.__const: 0x64e28
-  __TEXT.__cstring: 0x19ce4
-  __TEXT_EXEC.__text: 0x10d9c8
+  __TEXT.__cstring: 0x1a118
+  __TEXT_EXEC.__text: 0x10e540
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x1ff00
-  __DATA.__common: 0x22f0
+  __DATA.__common: 0x22f8
   __DATA.__bss: 0x1170
   __DATA_CONST.__auth_got: 0x570
   __DATA_CONST.__got: 0xa0
   __DATA_CONST.__auth_ptr: 0x88
   __DATA_CONST.__mod_init_func: 0x5c8
   __DATA_CONST.__mod_term_func: 0x5a0
-  __DATA_CONST.__const: 0x23c68
+  __DATA_CONST.__const: 0x23c98
   __DATA_CONST.__kalloc_type: 0x4580
   __DATA_CONST.__kalloc_var: 0x780
-  Functions: 7848
+  Functions: 7869
   Symbols:   0
-  CStrings:  2773
+  CStrings:  2790
 
CStrings:
+ "%d %s %s got null for pcoeffs\n"
+ "122222121221212212122121221212212122121221212212122121221212212122121221212212122121221212212122121221212212122121221212212122121221212212122121221212212122121221212212122121221212212122121221212212122121221212212122121221212212122121221212212122121221212212122121221212212122121221212212122121221212212121112222222222"
+ "Custom Filter Shift has been detected.\n"
+ "Custom Filter does not follow odd symmetry in phase 0\n"
+ "Falling back to default filters, skipping custom filters\n"
+ "Found phase %d that has taps around middle tap with closer values\n"
+ "IOSurfaceAcceleratorCapabilitiesVariableRateDirectionalScaling"
+ "Skipping coefficients are shifted checks\n"
+ "Skipping complete even symmetry check. Custom Filter is not shifted.\n"
+ "Using custom threshold for filter checks 0x%x\n"
+ "[%s][%s]Detected coefficient shift in custom filters bin %d\n"
+ "[SYM] Skipping CHDDAInit subsample adjustment\n"
+ "cannot get bootargs for checking shifted coefficients\n"
+ "checkCoefficientsValid"
+ "computeChromaDDAinit"
+ "msr_coefficient_checks"
+ "tap %d and tap %d are not close in value as expected\n"

```

>  `com.apple.driver.AppleMobileDispH17P-DCP`

```diff

-399.26.8.0.0
+399.27.3.0.0
   __TEXT.__cstring: 0x5f51
   __TEXT.__const: 0x1a60
-  __TEXT_EXEC.__text: 0x225f8
+  __TEXT_EXEC.__text: 0x225e0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2c0
   __DATA.__common: 0xf0

```

>  `com.apple.driver.AppleOLYHAL`

```diff

-450.19.0.0.0
-  __TEXT.__const: 0x798
+450.20.0.0.0
+  __TEXT.__const: 0x7b8
   __TEXT.__cstring: 0x45f5
-  __TEXT_EXEC.__text: 0x1d260
+  __TEXT_EXEC.__text: 0x1d4f4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x18c
   __DATA.__common: 0x170

   __DATA_CONST.__got: 0xe8
   __DATA_CONST.__mod_init_func: 0x38
   __DATA_CONST.__mod_term_func: 0x38
-  __DATA_CONST.__const: 0x13d8
+  __DATA_CONST.__const: 0x13e8
   __DATA_CONST.__kalloc_type: 0x600
-  Functions: 554
+  Functions: 559
   Symbols:   0
   CStrings:  497
 

```

>  `com.apple.driver.ApplePTD`

```diff

-22.0.0.0.0
+22.120.2.0.0
   __TEXT.__cstring: 0x1a77
   __TEXT.__const: 0x20
-  __TEXT_EXEC.__text: 0x9580
+  __TEXT_EXEC.__text: 0x9560
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0xf0
-  __DATA_CONST.__auth_got: 0x150
+  __DATA_CONST.__auth_got: 0x158
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18

```

>  `com.apple.driver.AppleSEPCredentialManager`

```diff

-758.120.1.0.0
-  __TEXT.__cstring: 0x10a64
-  __TEXT.__const: 0x390
-  __TEXT_EXEC.__text: 0x4a2e0
+758.120.3.0.0
+  __TEXT.__cstring: 0x10b3a
+  __TEXT.__const: 0x370
+  __TEXT_EXEC.__text: 0x4a860
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2d01
   __DATA.__common: 0x1d8

   __DATA_CONST.__const: 0x1a98
   __DATA_CONST.__kalloc_type: 0x600
   __DATA_CONST.__kalloc_var: 0x1400
-  Functions: 925
+  Functions: 928
   Symbols:   0
-  CStrings:  1843
+  CStrings:  1848
 
CStrings:
+ "_isDeviceUnlocked() || entitledToConfigureWhileLocked"
+ "_onEnvGetPolicyModePresentation"
+ "allowedToChange_BY_STATE"
+ "com.apple.private.applecredentialmanager.transportrestrictedmode.configurewhilelocked.allow"
+ "isEntitled"

```

>  `com.apple.driver.AppleSPU`

```diff

-1014.120.2.0.0
+1014.120.3.0.0
   __TEXT.__cstring: 0x5a9b
   __TEXT.__os_log: 0x94d
   __TEXT.__const: 0x380
-  __TEXT_EXEC.__text: 0x49140
+  __TEXT_EXEC.__text: 0x4917c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x878
   __DATA.__common: 0x970

```

>  `com.apple.driver.AudioDMAController-T8140`

```diff

-450.3.0.0.0
+450.4.0.0.0
   __TEXT.__const: 0x1e0
-  __TEXT.__cstring: 0x7cac
-  __TEXT.__os_log: 0x24d
-  __TEXT_EXEC.__text: 0x2d9b0
+  __TEXT.__cstring: 0x7b20
+  __TEXT.__os_log: 0x417
+  __TEXT_EXEC.__text: 0x2c4b8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x248
   __DATA.__common: 0x150

   __DATA_CONST.__kalloc_type: 0x400
   Functions: 411
   Symbols:   0
-  CStrings:  802
+  CStrings:  800
 
CStrings:
+ "%s invoked."
+ "21:55:57"
+ "Apr 10 2025"
+ "channel_handle        = 0x%08x"
+ "dev_xfer              = 0x%08x"
+ "dma_fifo_size         = 0x%08x"
+ "dma_timeout           = 0x%08x"
+ "fifo_start_trigger    = 0x%08x"
+ "fifo_stop_trigger     = 0x%08x"
+ "flags                 = 0x%08x"
- "%s: %s::%s::%d: %s invoked.\n"
- "%s: %s::%s::%d: channel_handle        = 0x%08x\n"
- "%s: %s::%s::%d: dev_xfer              = 0x%08x\n"
- "%s: %s::%s::%d: dma_fifo_size         = 0x%08x\n"
- "%s: %s::%s::%d: dma_timeout           = 0x%08x\n"
- "%s: %s::%s::%d: fifo_start_trigger    = 0x%08x\n"
- "%s: %s::%s::%d: fifo_stop_trigger     = 0x%08x\n"
- "%s: %s::%s::%d: flags                 = 0x%08x\n"
- "20:30:45"
- "Mar 24 2025"
- "initialize"
- "updateConfiguration"

```

>  `com.apple.driver.AudioDMAFamily`

```diff

-450.3.0.0.0
+450.4.0.0.0
   __TEXT.__const: 0x30
-  __TEXT.__cstring: 0x1016
-  __TEXT_EXEC.__text: 0x55fc
+  __TEXT.__cstring: 0xeb2
+  __TEXT.__os_log: 0x428
+  __TEXT_EXEC.__text: 0x5bbc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60
-  __DATA_CONST.__auth_got: 0xf0
-  __DATA_CONST.__got: 0x38
+  __DATA_CONST.__auth_got: 0xf8
+  __DATA_CONST.__got: 0x40
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xe40

   __DATA_CONST.__kalloc_var: 0xa0
   Functions: 78
   Symbols:   0
-  CStrings:  114
+  CStrings:  123
 
CStrings:
+ "%s: [%c%c%c%c] Direction                          = %s"
+ "%s: [%c%c%c%c] isM2M                              = %s"
+ "%s: [%c%c%c%c] programmedAXIBurstSize             = %hhu"
+ "%s: [%c%c%c%c] programmedByteSize                 = %hhu"
+ "%s: [%c%c%c%c] programmedFIFODepthBytes           = %hu"
+ "%s: [%c%c%c%c] programmedTransferEndLimitsBytes   = %hu"
+ "%s: [%c%c%c%c] programmedTransferThresholdBytes   = %hu"
+ "21:57:31"
+ "22222221211112211112"
+ "Apr 10 2025"
+ "Rx"
+ "Tx"
+ "[%c%c%c%c Rx] Requested threshold bytes(%u) <= Requested transfer-end bytes(%u)."
+ "[%c%c%c%c Tx] Requested threshold bytes(%u) >= Requested transfer-end bytes(%u)."
+ "[%c%c%c%c] Requested threshold bytes is 0."
+ "[%c%c%c%c] Requested threshold bytes(%u) >= Requested FIFO size bytes(%u)."
+ "set"
+ "updateStreamConfig"
- "%s: %s::%d: dmaConfiguration.isM2M                              = %s\n"
- "%s: %s::%d: dmaConfiguration.programmedAXIBurstSize             = %hhu\n"
- "%s: %s::%d: dmaConfiguration.programmedByteSize                 = %hhu\n"
- "%s: %s::%d: dmaConfiguration.programmedFIFODepthBytes           = %hu\n"
- "%s: %s::%d: dmaConfiguration.programmedTransferThresholdBytes   = %hu\n"
- "%s: Configuration is invalid."
- "20:32:04"
- "2222221211112211112"
- "Mar 24 2025"

```

>  `com.apple.driver.usb.cdc.ncm`

```diff

-362.100.1.0.0
+362.120.4.0.0
   __TEXT.__const: 0x128
-  __TEXT.__cstring: 0xcf2
-  __TEXT_EXEC.__text: 0x8388
+  __TEXT.__cstring: 0xcf3
+  __TEXT_EXEC.__text: 0x8494
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60
   __DATA.__bss: 0x4
-  __DATA_CONST.__auth_got: 0x288
+  __DATA_CONST.__auth_got: 0x2a8
   __DATA_CONST.__got: 0x78
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xf48
   __DATA_CONST.__kalloc_type: 0x100
-  Functions: 191
+  Functions: 190
   Symbols:   0
   CStrings:  129
 
CStrings:
+ "12111112122212121111111221211111111111211221121112211112111121111211112111121111211112111121111211112111121111211112111121111211112111121111121111121111121111121111121111121111121111121111121111121111121111121111121111121111121121122111112222222222221121112"
- "1211111212221212111111122121111111111121122112112211112111121111211112111121111211112111121111211112111121111211112111121111211112111121111121111121111121111121111121111121111121111121111121111121111121111121111121111121111121121122111112222222222221121112"

```

>  `com.apple.filesystems.apfs`

```diff

-2332.120.27.0.0
+2332.120.29.0.0
   __TEXT.__const: 0x990
-  __TEXT.__cstring: 0x49f8b
-  __TEXT_EXEC.__text: 0x14035c
+  __TEXT.__cstring: 0x49f82
+  __TEXT_EXEC.__text: 0x14033c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x6a0
   __DATA.__bss: 0xca8

   __DATA_CONST.__assert: 0x14
   Functions: 2268
   Symbols:   0
-  CStrings:  6429
+  CStrings:  6428
 
CStrings:
+ "2025/04/10"
+ "21:38:45"
+ "2332.120.29"
+ "Apr 10 2025"
+ "apfs-2332.120.29"
- "19:57:23"
- "19:57:24"
- "2025/03/24"
- "2332.120.27"
- "Mar 24 2025"
- "apfs-2332.120.27"

```

>  `com.apple.filesystems.lifs`

```diff

-531.120.13.0.0
+531.120.18.0.0
   __TEXT.__os_log: 0x12f9
   __TEXT.__cstring: 0x217f
   __TEXT.__const: 0x2c0
-  __TEXT_EXEC.__text: 0x1ac48
+  __TEXT_EXEC.__text: 0x1b138
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x5d0
   __DATA.__common: 0x138
   __DATA.__bss: 0x90
-  __DATA_CONST.__auth_got: 0x7c0
+  __DATA_CONST.__auth_got: 0x7d0
   __DATA_CONST.__got: 0x80
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
   __DATA_CONST.__const: 0x16a0
   __DATA_CONST.__kalloc_type: 0xbc0
-  Functions: 400
+  Functions: 401
   Symbols:   0
   CStrings:  393
 

```

>  `com.apple.iokit.IOAccessoryManager`

```diff

-1016.120.2.0.0
+1016.120.3.0.0
   __TEXT.__const: 0x328
-  __TEXT.__cstring: 0x1080d
-  __TEXT.__os_log: 0x10799
-  __TEXT_EXEC.__text: 0xeff9c
+  __TEXT.__cstring: 0x10803
+  __TEXT.__os_log: 0x1077b
+  __TEXT_EXEC.__text: 0xefcf8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x7e8
   __DATA.__common: 0x1630

   __DATA_DIRTY.__bss: 0x20
   Functions: 4821
   Symbols:   0
-  CStrings:  2786
+  CStrings:  2788
 
CStrings:
+ "%s::%s(): [Boot Arg] %s=%u\n"
+ "%s::%s(): [Boot Arg] %s=0x%08x\n"
+ "%s::%s(): [EDT] /defaults/%s=%u\n"
+ "[ERROR] %s::%s(): [EDT] Invalid value for /defaults/%s!\n"
- "%s::%s(): [%s%s%s] [EDT] /defaults/%s=%u\n\n"
- "[ERROR] %s::%s(): [%s%s%s] [EDT] Invalid value for /defaults/%s!\n\n"

```

>  `com.apple.iokit.IOSCSIArchitectureModelFamily`

```diff

-500.120.1.0.0
+500.120.2.0.0
   __TEXT.__const: 0x18
   __TEXT.__cstring: 0x1451
-  __TEXT_EXEC.__text: 0x1845c
+  __TEXT_EXEC.__text: 0x184ec
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x418
   __DATA.__common: 0x1c8

```

>  `com.apple.iokit.IOSCSIBlockCommandsDevice`

```diff

-500.120.1.0.0
+500.120.2.0.0
   __TEXT.__cstring: 0x69e
-  __TEXT_EXEC.__text: 0xba5c
+  __TEXT_EXEC.__text: 0xbaa8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2a8
   __DATA.__common: 0x98
   __DATA.__bss: 0x4
-  __DATA_CONST.__auth_got: 0x2c0
+  __DATA_CONST.__auth_got: 0x2c8
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18

```

>  `com.apple.iokit.IOSkywalkFamily`

```diff

-521.120.3.0.0
+521.120.4.0.0
   __TEXT.__cstring: 0x1b0e
-  __TEXT.__const: 0xe10
-  __TEXT_EXEC.__text: 0x37e78
+  __TEXT.__const: 0xe30
+  __TEXT_EXEC.__text: 0x37f0c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xe8
   __DATA.__common: 0x6b0

```

>  `com.apple.kernel`

```diff

-11417.120.80.0.3
+11417.120.96.502.1
   __TEXT.__const: 0x34500
   __TEXT.__copyio_vectors: 0xf0
-  __TEXT.__cstring: 0x7686c
-  __TEXT.__os_log: 0x2a698
+  __TEXT.__cstring: 0x768fe
+  __TEXT.__os_log: 0x2a6b0
   __TEXT.__eh_frame: 0x610
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x2d8
-  __DATA_CONST.__const: 0xabbb8
+  __DATA_CONST.__const: 0xabba8
   __DATA_CONST.__hib_const: 0x120
   __DATA_CONST.__kalloc_type: 0x13980
   __DATA_CONST.__kalloc_var: 0x7ee0

   __DATA_CONST.__brk_desc: 0x78
   __DATA_SPTM.__const: 0x3c000
   __TEXT_EXEC.__hib_text: 0xcc8
-  __TEXT_EXEC.__text: 0x81e4fc
+  __TEXT_EXEC.__text: 0x828280
   __TEXT_BOOT_EXEC.__bootcode: 0x514c
   __KLD.__text: 0x1638
   __LASTDATA_CONST.__mod_init_func: 0x8

   __KLDDATA.__mod_term_func: 0x8
   __KLDDATA.__bss: 0x1
   __DATA.__data: 0x185c1
-  __DATA.__lock_grp: 0x5a10
+  __DATA.__lock_grp: 0x5a68
   __DATA.__percpu: 0x6e80
   __DATA.__common: 0x5bd30
-  __DATA.__bss: 0x96208
+  __DATA.__bss: 0x96258
   __BOOTDATA.__data: 0x18000
-  __BOOTDATA.__init_entry_set: 0x11190
+  __BOOTDATA.__init_entry_set: 0x111c0
   __BOOTDATA.__init: 0x5b188
   __BOOTDATA.__static_ifinit: 0x8
   __BOOTDATA.__static_if: 0x0

   __PLK_DATA_CONST.__data: 0x0
   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
-  __LINKINFO.__symbolsets: 0x46658
-  Functions: 20175
+  __LINKINFO.__symbolsets: 0x4667d
+  Functions: 20189
   Symbols:   0
-  CStrings:  17886
+  CStrings:  17890
 
CStrings:
+ " (recycled)"
+ "%s: attached%s\n"
+ "%s: inpcb socket so_usecount underflow  when removing timer entry\n"
+ "SO_VALID_TC(optval)"
+ "necp_get_tlv_at_offset buffer is NULL"
+ "site.u_int8_t * __attribute__((__indexable__))"
+ "tcp_remove_timer"
- "81112"
- "site.u_int8_t *"
- "u32__v_assign_copy err %u @%s:%d"

```

>  `com.apple.kext.CoreTrust`

```diff

-148.120.5.0.0
-  __TEXT.__const: 0x10d2
-  __TEXT_EXEC.__text: 0x870c
+148.120.6.0.0
+  __TEXT.__const: 0x165e
+  __TEXT_EXEC.__text: 0x875c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd8
   __DATA.__common: 0x10
   __DATA_CONST.__auth_got: 0xe8
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x1558
+  __DATA_CONST.__const: 0x1a78
   Functions: 124
   Symbols:   0
   CStrings:  0

```

>  `com.apple.security.sandbox`

```diff

-2401.120.9.0.0
+2401.120.20.0.1
   __TEXT.__os_log: 0x2092
-  __TEXT.__const: 0x1b65f1
+  __TEXT.__const: 0x1b82f9
   __TEXT.__cstring: 0x719d
   __TEXT_EXEC.__text: 0x315a4
   __TEXT_EXEC.__auth_stubs: 0x0

```

</details>

## MachO

### 🆕 NEW (2)

- `/Applications/AMSUIAuthenticationViewService.app/AMSUIAuthenticationViewService`
- `/System/Library/PrivateFrameworks/MobileInBoxUpdate.framework/XPCServices/MIBULoopbackServerHelper.xpc/MIBULoopbackServerHelper`

### ❌ Removed (1)

- `/System/ExclaveKit/System/Library/Frameworks/XnuNotifications.framework/XnuNotifications`

### ⬆️ Updated (370)

<details>
  <summary><i>View Updated</i></summary>

- [/Applications/AMSEngagementViewService.app/AMSEngagementViewService](MACHOS/AMSEngagementViewService.md)
- [/Applications/AdaptiveMusicApp.app/AdaptiveMusicApp](MACHOS/AdaptiveMusicApp.md)
- [/Applications/AdaptiveMusicApp.app/PlugIns/AdaptiveMusicControl.appex/AdaptiveMusicControl](MACHOS/AdaptiveMusicControl.md)
- [/Applications/AirDropUI.app/AirDropUI](MACHOS/AirDropUI.md)
- [/Applications/AppDistributionLaunchAngel.app/AppDistributionLaunchAngel](MACHOS/AppDistributionLaunchAngel.md)
- [/Applications/AppSSOUIService.app/AppSSOUIService](MACHOS/AppSSOUIService.md)
- [/Applications/BusinessExtensionsWrapper.app/PlugIns/Business.appex/Business](MACHOS/Business.md)
- [/Applications/CarCamera.app/CarCamera](MACHOS/CarCamera.md)
- [/Applications/Charge.app/Charge](MACHOS/Charge.md)
- [/Applications/CheckerBoard.app/CheckerBoard](MACHOS/CheckerBoard.md)
- [/Applications/ClarityCamera.app/ClarityCamera](MACHOS/ClarityCamera.md)
- [/Applications/Climate.app/Climate](MACHOS/Climate.md)
- [/Applications/ClockAngel.app/ClockAngel](MACHOS/ClockAngel.md)
- [/Applications/ColorPickerUIService.app/ColorPickerUIService](MACHOS/ColorPickerUIService.md)
- [/Applications/CoreAuthUI.app/CoreAuthUI](MACHOS/CoreAuthUI.md)
- [/Applications/Diagnostics.app/Diagnostics](MACHOS/Diagnostics.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6004.appex/Diagnostic-6004](MACHOS/Diagnostic-6004.md)
- [/Applications/DiagnosticsService.app/PlugIns/SystemReport.appex/SystemReport](MACHOS/SystemReport.md)
- [/Applications/EventViewService.app/EventViewService](MACHOS/EventViewService.md)
- [/Applications/FMDMagSafeSetupRemoteUI.app/FMDMagSafeSetupRemoteUI](MACHOS/FMDMagSafeSetupRemoteUI.md)
- [/Applications/Feedback Assistant iOS.app/Feedback Assistant iOS](MACHOS/Feedback_Assistant_iOS.md)
- [/Applications/FinanceUIService.app/FinanceUIService](MACHOS/FinanceUIService.md)
- [/Applications/FindMyExtensionContainer.app/PlugIns/FMDMagSafeExtension.appex/FMDMagSafeExtension](MACHOS/FMDMagSafeExtension.md)
- [/Applications/FindMyExtensionContainer.app/PlugIns/FindMyDeviceBluetoothExtension.appex/FindMyDeviceBluetoothExtension](MACHOS/FindMyDeviceBluetoothExtension.md)
- [/Applications/FindMyRemoteUIService.app/FindMyRemoteUIService](MACHOS/FindMyRemoteUIService.md)
- [/Applications/FontPickerUIService.app/FontPickerUIService](MACHOS/FontPickerUIService.md)
- [/Applications/HDSViewService.app/HDSViewService](MACHOS/HDSViewService.md)
- [/Applications/HeadphoneProxService.app/HeadphoneProxService](MACHOS/HeadphoneProxService.md)
- [/Applications/HomeUIService.app/HomeUIService](MACHOS/HomeUIService.md)
- [/Applications/InCallService.app/InCallService](MACHOS/InCallService.md)
- [/Applications/Media.app/Media](MACHOS/Media.md)
- [/Applications/MediaRemoteUI.app/MediaRemoteUI](MACHOS/MediaRemoteUI.md)
- [/Applications/MobilePhone.app/MobilePhone](MACHOS/MobilePhone.md)
- [/Applications/MusicRecognition.app/MusicRecognition](MACHOS/MusicRecognition.md)
- [/Applications/NewDeviceSetupUIService.app/NewDeviceSetupUIService](MACHOS/NewDeviceSetupUIService.md)
- [/Applications/PCViewService.app/PCViewService](MACHOS/PCViewService.md)
- [/Applications/Preferences.app/Preferences](MACHOS/Preferences.md)
- [/Applications/Screen Time.app/PlugIns/ScreenTimeWidgetExtension.appex/ScreenTimeWidgetExtension](MACHOS/ScreenTimeWidgetExtension.md)
- [/Applications/Setup.app/Setup](MACHOS/Setup.md)
- [/Applications/SharingUIService.app/SharingUIService](MACHOS/SharingUIService.md)
- [/Applications/SharingViewService.app/SharingViewService](MACHOS/SharingViewService.md)
- [/Applications/ShazamEventsApp.app/ShazamEventsApp](MACHOS/ShazamEventsApp.md)
- [/Applications/Siri.app/Siri](MACHOS/Siri.md)
- [/Applications/TDGSharingViewService.app/TDGSharingViewService](MACHOS/TDGSharingViewService.md)
- [/Applications/Tamale.app/Tamale](MACHOS/Tamale.md)
- [/Applications/TirePressure.app/TirePressure](MACHOS/TirePressure.md)
- [/Applications/Trip.app/Trip](MACHOS/Trip.md)
- [/Applications/WritingToolsUIService.app/WritingToolsUIService](MACHOS/WritingToolsUIService.md)
- [/Library/Audio/Plug-Ins/HAL/VirtualAudio.plugin/VirtualAudio](MACHOS/VirtualAudio.md)
- [/System/ExclaveKit/usr/lib/dyld](MACHOS/dyld.md)
- [/System/ExclaveKit/usr/lib/system/libsystem_malloc_debug.dylib](MACHOS/libsystem_malloc_debug.dylib.md)
- [/System/Library/AccessibilityBundles/AXMotionCuesServer.axuiservice/AXMotionCuesServer](MACHOS/AXMotionCuesServer.md)
- [/System/Library/AccessibilityBundles/VoiceOver.axuiservice/VoiceOver](MACHOS/VoiceOver.md)
- [/System/Library/Accounts/DataclassOwners/FreeformDataclassOwner.bundle/FreeformDataclassOwner](MACHOS/FreeformDataclassOwner.md)
- [/System/Library/Accounts/Notification/CloudDocsAccountNotificationPlugin.bundle/CloudDocsAccountNotificationPlugin](MACHOS/CloudDocsAccountNotificationPlugin.md)
- [/System/Library/Accounts/ServiceOwners/AMSMediaServiceOwner.bundle/AMSMediaServiceOwner](MACHOS/AMSMediaServiceOwner.md)
- [/System/Library/AppleMediaServices/DynamicUI/PlugIns/StoreDynamicUIPlugin.bundle/StoreDynamicUIPlugin](MACHOS/StoreDynamicUIPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/AlarmFlowPlugin.bundle/AlarmFlowPlugin](MACHOS/AlarmFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/AudioFlowDelegatePlugin](MACHOS/AudioFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/CAMRootFlowPlugin.bundle/CAMRootFlowPlugin](MACHOS/CAMRootFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/CalendarFlowDelegatePlugin.bundle/CalendarFlowDelegatePlugin](MACHOS/CalendarFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/CarCommandsFlowDelegatePlugin.bundle/CarCommandsFlowDelegatePlugin](MACHOS/CarCommandsFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/ClockFlowPlugin.bundle/ClockFlowPlugin](MACHOS/ClockFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/DailyBriefingFlowPlugin.bundle/DailyBriefingFlowPlugin](MACHOS/DailyBriefingFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/EmergencyFlowPlugin.bundle/EmergencyFlowPlugin](MACHOS/EmergencyFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/HealthFlowDelegatePlugin.bundle/HealthFlowDelegatePlugin](MACHOS/HealthFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/HomeCommunicationFlowDelegatePlugin.bundle/HomeCommunicationFlowDelegatePlugin](MACHOS/HomeCommunicationFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/IFFlowPlugin](MACHOS/IFFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/InformationFlowPlugin](MACHOS/InformationFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/PhoneCallFlowDelegatePlugin](MACHOS/PhoneCallFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SiriLinkFlowPlugin.bundle/SiriLinkFlowPlugin](MACHOS/SiriLinkFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/TimerFlowDelegatePlugin.bundle/TimerFlowDelegatePlugin](MACHOS/TimerFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/WellnessFlowPlugin](MACHOS/WellnessFlowPlugin.md)
- [/System/Library/Assistant/Plugins/PreferencesAssistant.assistantBundle/PreferencesAssistant](MACHOS/PreferencesAssistant.md)
- [/System/Library/Audio/Plug-Ins/AVC/AVCHalogen.driver/AVCHalogen](MACHOS/AVCHalogen.md)
- [/System/Library/Audio/Plug-Ins/HAL/AirPlayHalogen.driver/AirPlayHalogen](MACHOS/AirPlayHalogen.md)
- [/System/Library/Audio/Plug-Ins/HAL/BTAudioHALPlugin.driver/BTAudioHALPlugin](MACHOS/BTAudioHALPlugin.md)
- [/System/Library/Audio/Plug-Ins/HAL/CarPlayHalogen.driver/CarPlayHalogen](MACHOS/CarPlayHalogen.md)
- [/System/Library/Audio/Plug-Ins/HAL/OctaviaHalogen.driver/OctaviaHalogen](MACHOS/OctaviaHalogen.md)
- [/System/Library/Audio/Plug-Ins/usbaudio.bundle/usbaudiod](MACHOS/usbaudiod.md)
- [/System/Library/CoreServices/AccessibilityUIServer.app/PlugIns/AccessibilityControlsExtension.appex/AccessibilityControlsExtension](MACHOS/AccessibilityControlsExtension.md)
- [/System/Library/CoreServices/AegirProxyApp.app/PlugIns/AegirPoster.appex/AegirPoster](MACHOS/AegirPoster.md)
- [/System/Library/CoreServices/AssistiveTouch.app/assistivetouchd](MACHOS/assistivetouchd.md)
- [/System/Library/CoreServices/CarPlayTemplateUIHost.app/CarPlayTemplateUIHost](MACHOS/CarPlayTemplateUIHost.md)
- [/System/Library/CoreServices/ClarityBoard.app/ClarityBoard](MACHOS/ClarityBoard.md)
- [/System/Library/CoreServices/IntelligentLight.app/IntelligentLight](MACHOS/IntelligentLight.md)
- [/System/Library/CoreServices/LiveTranscriptionUI.app/LiveTranscriptionUI](MACHOS/LiveTranscriptionUI.md)
- [/System/Library/CoreServices/VoiceOverTouch.app/vot](MACHOS/vot.md)
- [/System/Library/CoreServices/powerd.bundle/powerd](MACHOS/powerd.md)
- [/System/Library/DataClassMigrators/BuddyMigrator.migrator/BuddyMigrator](MACHOS/BuddyMigrator.md)
- [/System/Library/DataClassMigrators/PreferencesMigrator.migrator/PreferencesMigrator](MACHOS/PreferencesMigrator.md)
- [/System/Library/DigitalSeparation/SharingSources/FindMyItemsDigitalSeparation.bundle/FindMyItemsDigitalSeparation](MACHOS/FindMyItemsDigitalSeparation.md)
- [/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN](MACHOS/com.apple.DriverKit-AppleBCMWLAN.md)
- [/System/Library/DriverExtensions/com.apple.DriverKit-AppleEthernetMLX5.dext/com.apple.DriverKit-AppleEthernetMLX5](MACHOS/com.apple.DriverKit-AppleEthernetMLX5.md)
- [/System/Library/ExtensionKit/Extensions/AccessibilityControlsExtension.appex/AccessibilityControlsExtension](MACHOS/AccessibilityControlsExtension.md)
- [/System/Library/ExtensionKit/Extensions/AssetMetricsExtension.appex/AssetMetricsExtension](MACHOS/AssetMetricsExtension.md)
- [/System/Library/ExtensionKit/Extensions/AssistantSettingsControlsExtension.appex/AssistantSettingsControlsExtension](MACHOS/AssistantSettingsControlsExtension.md)
- [/System/Library/ExtensionKit/Extensions/BatterySettingsIntentsExtension.appex/BatterySettingsIntentsExtension](MACHOS/BatterySettingsIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/DevicePropertiesExtension.appex/DevicePropertiesExtension](MACHOS/DevicePropertiesExtension.md)
- [/System/Library/ExtensionKit/Extensions/DocumentAppIntents.appex/DocumentAppIntents](MACHOS/DocumentAppIntents.md)
- [/System/Library/ExtensionKit/Extensions/ExperimentationExtension.appex/ExperimentationExtension](MACHOS/ExperimentationExtension.md)
- [/System/Library/ExtensionKit/Extensions/FindMyIntentsExtension.appex/FindMyIntentsExtension](MACHOS/FindMyIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/GenerativeAssistantExtension.appex/GenerativeAssistantExtension](MACHOS/GenerativeAssistantExtension.md)
- [/System/Library/ExtensionKit/Extensions/LighthouseServicesAnalyticsExtension.appex/LighthouseServicesAnalyticsExtension](MACHOS/LighthouseServicesAnalyticsExtension.md)
- [/System/Library/ExtensionKit/Extensions/MessageCenterApplicationServiceDiscoveryExtension.appex/MessageCenterApplicationServiceDiscoveryExtension](MACHOS/MessageCenterApplicationServiceDiscoveryExtension.md)
- [/System/Library/ExtensionKit/Extensions/MetricsExtension.appex/MetricsExtension](MACHOS/MetricsExtension.md)
- [/System/Library/ExtensionKit/Extensions/ODDIMetricsExtension.appex/ODDIMetricsExtension](MACHOS/ODDIMetricsExtension.md)
- [/System/Library/ExtensionKit/Extensions/ODDIPoirotMetricsExtension.appex/ODDIPoirotMetricsExtension](MACHOS/ODDIPoirotMetricsExtension.md)
- [/System/Library/ExtensionKit/Extensions/PridePosterExtension.appex/PridePosterExtension](MACHOS/PridePosterExtension.md)
- [/System/Library/ExtensionKit/Extensions/PrivateEvolutionPlugin.appex/PrivateEvolutionPlugin](MACHOS/PrivateEvolutionPlugin.md)
- [/System/Library/ExtensionKit/Extensions/ProductPageExtension.appex/ProductPageExtension](MACHOS/ProductPageExtension.md)
- [/System/Library/ExtensionKit/Extensions/SearchToolExtension.appex/SearchToolExtension](MACHOS/SearchToolExtension.md)
- [/System/Library/ExtensionKit/Extensions/SubscribePageExtension.appex/SubscribePageExtension](MACHOS/SubscribePageExtension.md)
- [/System/Library/ExtensionKit/Extensions/TelemetryAggregator.appex/TelemetryAggregator](MACHOS/TelemetryAggregator.md)
- [/System/Library/ExtensionKit/Extensions/Unity2025Poster.appex/Unity2025Poster](MACHOS/Unity2025Poster.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.fskit.msdos.appex/com.apple.fskit.msdos](MACHOS/com.apple.fskit.msdos.md)
- [/System/Library/Extensions/lifs.kext/lifs](MACHOS/lifs.md)
- [/System/Library/Filesystems/msdos.fs/fsck_msdos](MACHOS/fsck_msdos.md)
- [/System/Library/Frameworks/AssetsLibrary.framework/Support/assetsd](MACHOS/assetsd.md)
- [/System/Library/Frameworks/CallKit.framework/XPCServices/com.apple.CallKit.CallDirectory.xpc/com.apple.CallKit.CallDirectory](MACHOS/com.apple.CallKit.CallDirectory.md)
- [/System/Library/Frameworks/CallKit.framework/XPCServices/com.apple.CallKit.CallDirectoryMaintenance.xpc/com.apple.CallKit.CallDirectoryMaintenance](MACHOS/com.apple.CallKit.CallDirectoryMaintenance.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/PlugIns/CoreSpotlightTestImporter.appex/CoreSpotlightTestImporter](MACHOS/CoreSpotlightTestImporter.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/PlugIns/CoreSpotlightTextImporter.appex/CoreSpotlightTextImporter](MACHOS/CoreSpotlightTextImporter.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/Support/com.apple.spotlight.IndexAgent](MACHOS/com.apple.spotlight.IndexAgent.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/spotlightknowledged](MACHOS/spotlightknowledged.md)
- [/System/Library/Frameworks/HomeKit.framework/PlugIns/HomeKitDiagnosticExtension.appex/HomeKitDiagnosticExtension](MACHOS/HomeKitDiagnosticExtension.md)
- [/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond](MACHOS/managedappdistributiond.md)
- [/System/Library/Frameworks/Security.framework/XPCServices/TrustedPeersHelper.xpc/TrustedPeersHelper](MACHOS/TrustedPeersHelper.md)
- [/System/Library/Frameworks/SensorKit.framework/XPCServices/SensorKitLongTermStorageHelper.xpc/SensorKitLongTermStorageHelper](MACHOS/SensorKitLongTermStorageHelper.md)
- [/System/Library/Frameworks/StoreKit.framework/Support/storekitd](MACHOS/storekitd.md)
- [/System/Library/Frameworks/UIKit.framework/PlugIns/com.apple.UIKit.ColorPicker.appex/com.apple.UIKit.ColorPicker](MACHOS/com.apple.UIKit.ColorPicker.md)
- [/System/Library/LocationBundles/SystemCustomization.bundle/SystemCustomization](MACHOS/SystemCustomization.md)
- [/System/Library/Messages/PlugIns/RCS.imservice/RCS](MACHOS/RCS.md)
- [/System/Library/Messages/PlugIns/iMessage.imservice/iMessage](MACHOS/iMessage.md)
- [/System/Library/Messages/iMessageBalloons/ASMessagesProvider.bundle/ASMessagesProvider](MACHOS/ASMessagesProvider.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/ActivityBridgeSetup.bundle/ActivityBridgeSetup](MACHOS/ActivityBridgeSetup.md)
- [/System/Library/PreferenceBundles/AccountSettings/CloudKitSettings.bundle/CloudKitSettings](MACHOS/CloudKitSettings.md)
- [/System/Library/PreferenceBundles/AccountSettings/MailAccountSettings.bundle/MailAccountSettings](MACHOS/MailAccountSettings.md)
- [/System/Library/PreferenceBundles/AirDropSettings.bundle/AirDropSettings](MACHOS/AirDropSettings.md)
- [/System/Library/PreferenceBundles/AirPlayAndHandoffSettings.bundle/AirPlayAndHandoffSettings](MACHOS/AirPlayAndHandoffSettings.md)
- [/System/Library/PreferenceBundles/BatteryUsageUI.bundle/BatteryUsageUI](MACHOS/BatteryUsageUI.md)
- [/System/Library/PreferenceBundles/HomeSettings.bundle/HomeSettings](MACHOS/HomeSettings.md)
- [/System/Library/PreferenceBundles/MobileStoreSettings.bundle/MobileStoreSettings](MACHOS/MobileStoreSettings.md)
- [/System/Library/PreferenceBundles/MultitaskingAndGesturesSettings.bundle/MultitaskingAndGesturesSettings](MACHOS/MultitaskingAndGesturesSettings.md)
- [/System/Library/PreferenceBundles/PodcastsSettingsPlugin.bundle/PodcastsSettingsPlugin](MACHOS/PodcastsSettingsPlugin.md)
- [/System/Library/PreferenceBundles/PrivacyAndSecuritySettings.bundle/PrivacyAndSecuritySettings](MACHOS/PrivacyAndSecuritySettings.md)
- [/System/Library/PreferenceBundles/ScreenTimeSettings.bundle/ScreenTimeSettings](MACHOS/ScreenTimeSettings.md)
- [/System/Library/PreferenceBundles/WallpaperSettings.bundle/WallpaperSettings](MACHOS/WallpaperSettings.md)
- [/System/Library/PreferenceManifestsInternal/PreferencesManifests.bundle/PreferencesManifests](MACHOS/PreferencesManifests.md)
- [/System/Library/PrivateFrameworks/ASOctaneSupport.framework/XPCServices/ASOctaneSupportXPCService.xpc/ASOctaneSupportXPCService](MACHOS/ASOctaneSupportXPCService.md)
- [/System/Library/PrivateFrameworks/ActionPredictionHeuristics.framework/XPCServices/HeuristicInterpreter.xpc/HeuristicInterpreter](MACHOS/HeuristicInterpreter.md)
- [/System/Library/PrivateFrameworks/AppSSO.framework/Support/AppSSODaemon](MACHOS/AppSSODaemon.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored](MACHOS/appstored.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/amsaccountsd](MACHOS/amsaccountsd.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/Extensions/UtilityExtension.appex/UtilityExtension](MACHOS/UtilityExtension.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/amsengagementd](MACHOS/amsengagementd.md)
- [/System/Library/PrivateFrameworks/ApplePushService.framework/apsd](MACHOS/apsd.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd](MACHOS/assistantd.md)
- [/System/Library/PrivateFrameworks/AuthKit.framework/akd](MACHOS/akd.md)
- [/System/Library/PrivateFrameworks/BiomeStorage.framework/XPCServices/BiomeWriteService.xpc/BiomeWriteService](MACHOS/BiomeWriteService.md)
- [/System/Library/PrivateFrameworks/CSExattrCrypto.framework/XPCServices/CSExattrCryptoService.xpc/CSExattrCryptoService](MACHOS/CSExattrCryptoService.md)
- [/System/Library/PrivateFrameworks/CascadeSets.framework/XPCServices/SetStoreUpdateService.xpc/SetStoreUpdateService](MACHOS/SetStoreUpdateService.md)
- [/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.MobileDocumentsFileProviderUI.appex/com.apple.CloudDocs.MobileDocumentsFileProviderUI](MACHOS/com.apple.CloudDocs.MobileDocumentsFileProviderUI.md)
- [/System/Library/PrivateFrameworks/CloudKitDaemon.framework/Support/ckdiscretionaryd](MACHOS/ckdiscretionaryd.md)
- [/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/Support/cloudphotod](MACHOS/cloudphotod.md)
- [/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/XPCServices/com.apple.Photos.CPLDiagnose.xpc/com.apple.Photos.CPLDiagnose](MACHOS/com.apple.Photos.CPLDiagnose.md)
- [/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsagent](MACHOS/analyticsagent.md)
- [/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsd](MACHOS/analyticsd.md)
- [/System/Library/PrivateFrameworks/CoreLocationTiles.framework/XPCServices/TilesService.xpc/TilesService](MACHOS/TilesService.md)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd](MACHOS/corespeechd.md)
- [/System/Library/PrivateFrameworks/DeviceCheckInternal.framework/devicecheckd](MACHOS/devicecheckd.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/LocationDiagnosticExtension.appex/LocationDiagnosticExtension](MACHOS/LocationDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/NearbydDiagnosticExtension.appex/NearbydDiagnosticExtension](MACHOS/NearbydDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.B389.appex/com.apple.DiagnosticExtensions.B389](MACHOS/com.apple.DiagnosticExtensions.B389.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Microstackshot.appex/com.apple.DiagnosticExtensions.Microstackshot](MACHOS/com.apple.DiagnosticExtensions.Microstackshot.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.sysdiagnose.appex/com.apple.DiagnosticExtensions.sysdiagnose](MACHOS/com.apple.DiagnosticExtensions.sysdiagnose.md)
- [/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/XPCServices/DPSubmissionService.xpc/DPSubmissionService](MACHOS/DPSubmissionService.md)
- [/System/Library/PrivateFrameworks/DiskImages2.framework/XPCServices/diskimagescontroller.xpc/diskimagescontroller](MACHOS/diskimagescontroller.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAppPopover.appex/RecentsAppPopover](MACHOS/RecentsAppPopover.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAvocado.appex/RecentsAvocado](MACHOS/RecentsAvocado.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/SaveToFiles.appex/SaveToFiles](MACHOS/SaveToFiles.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/com.apple.DocumentManager.Service.appex/com.apple.DocumentManager.Service](MACHOS/com.apple.DocumentManager.Service.md)
- [/System/Library/PrivateFrameworks/EmailDaemon.framework/maild](MACHOS/maild.md)
- [/System/Library/PrivateFrameworks/FileProviderDaemon.framework/PlugIns/FileProviderDiagnosticExtension.appex/FileProviderDiagnosticExtension](MACHOS/FileProviderDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceBTDiscoveryXPCService.xpc/FindMyDeviceBTDiscoveryXPCService](MACHOS/FindMyDeviceBTDiscoveryXPCService.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceEmergencyCallInfoPublisherXPCService.xpc/FindMyDeviceEmergencyCallInfoPublisherXPCService](MACHOS/FindMyDeviceEmergencyCallInfoPublisherXPCService.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceEraseXPCService.xpc/FindMyDeviceEraseXPCService](MACHOS/FindMyDeviceEraseXPCService.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceHelperXPCService.xpc/FindMyDeviceHelperXPCService](MACHOS/FindMyDeviceHelperXPCService.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceIdentityXPCService.xpc/FindMyDeviceIdentityXPCService](MACHOS/FindMyDeviceIdentityXPCService.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceUserNotificationsXPCService.xpc/FindMyDeviceUserNotificationsXPCService](MACHOS/FindMyDeviceUserNotificationsXPCService.md)
- [/System/Library/PrivateFrameworks/GPUToolsCapture.framework/GPUToolsCapture](MACHOS/GPUToolsCapture.md)
- [/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd](MACHOS/identityservicesd.md)
- [/System/Library/PrivateFrameworks/IDSBlastDoorSupport.framework/XPCServices/IDSBlastDoorService.xpc/IDSBlastDoorService](MACHOS/IDSBlastDoorService.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCompute.framework/XPCServices/IntelligencePlatformComputeService.xpc/IntelligencePlatformComputeService](MACHOS/IntelligencePlatformComputeService.md)
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd](MACHOS/mediaanalysisd.md)
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd-service](MACHOS/mediaanalysisd-service.md)
- [/System/Library/PrivateFrameworks/Message.framework/XPCServices/SearchIndexer.xpc/SearchIndexer](MACHOS/SearchIndexer.md)
- [/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/XPCServices/MessagesBlastDoorService.xpc/MessagesBlastDoorService](MACHOS/MessagesBlastDoorService.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/EAUpdaterService.xpc/EAUpdaterService](MACHOS/EAUpdaterService.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackupCacheDeleteService](MACHOS/MobileBackupCacheDeleteService.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/XPCServices/MBHelperService.xpc/MBHelperService](MACHOS/MBHelperService.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/backupd](MACHOS/backupd.md)
- [/System/Library/PrivateFrameworks/NanoPassKit.framework/NPKCompanionAgent](MACHOS/NPKCompanionAgent.md)
- [/System/Library/PrivateFrameworks/NeighborhoodActivityConduit.framework/XPCServices/com.apple.NeighborhoodActivityConduitService.xpc/com.apple.NeighborhoodActivityConduitService](MACHOS/com.apple.NeighborhoodActivityConduitService.md)
- [/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/ndoagent](MACHOS/ndoagent.md)
- [/System/Library/PrivateFrameworks/OnDeviceStorage.framework/Support/amsondevicestoraged](MACHOS/amsondevicestoraged.md)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/passd](MACHOS/passd.md)
- [/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/PlugIns/PhotosSearchDiagnostics.appex/PhotosSearchDiagnostics](MACHOS/PhotosSearchDiagnostics.md)
- [/System/Library/PrivateFrameworks/PhotosIntelligence.framework/PlugIns/PhotosStoryDiagnostics.appex/PhotosStoryDiagnostics](MACHOS/PhotosStoryDiagnostics.md)
- [/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PlugIns/AmbientPhotoFramePosterProvider.appex/AmbientPhotoFramePosterProvider](MACHOS/AmbientPhotoFramePosterProvider.md)
- [/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PlugIns/PhotosPosterProvider.appex/PhotosPosterProvider](MACHOS/PhotosPosterProvider.md)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/PlugIns/DEPowerlogEPL.appex/DEPowerlogEPL](MACHOS/DEPowerlogEPL.md)
- [/System/Library/PrivateFrameworks/PrivateCloudCompute.framework/privatecloudcomputed.app/privatecloudcomputed](MACHOS/privatecloudcomputed.md)
- [/System/Library/PrivateFrameworks/PromotedContentProxy.framework/PlugIns/PromotedContentWebProcessBundle.bundle/PromotedContentWebProcessBundle](MACHOS/PromotedContentWebProcessBundle.md)
- [/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeAgent](MACHOS/ScreenTimeAgent.md)
- [/System/Library/PrivateFrameworks/Search.framework/searchd](MACHOS/searchd.md)
- [/System/Library/PrivateFrameworks/SiriTTSService.framework/PlugIns/STSDiagnostic.appex/STSDiagnostic](MACHOS/STSDiagnostic.md)
- [/System/Library/PrivateFrameworks/SiriTTSService.framework/sirittsd](MACHOS/sirittsd.md)
- [/System/Library/PrivateFrameworks/SonicKit.framework/PlugIns/SonicDiagnostics.appex/SonicDiagnostics](MACHOS/SonicDiagnostics.md)
- [/System/Library/PrivateFrameworks/Stickers.framework/Support/stickersd](MACHOS/stickersd.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd](MACHOS/callservicesd.md)
- [/System/Library/PrivateFrameworks/UVFSXPCService.framework/XPCServices/UVFSService.xpc/UVFSService](MACHOS/UVFSService.md)
- [/System/Library/PrivateFrameworks/VisualVoicemail.framework/vmd](MACHOS/vmd.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/RhizomePoster.appex/RhizomePoster](MACHOS/RhizomePoster.md)
- [/System/Library/PrivateFrameworks/WirelessInsights.framework/Support/wirelessinsightsd](MACHOS/wirelessinsightsd.md)
- [/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/BackgroundShortcutRunner.xpc/BackgroundShortcutRunner](MACHOS/BackgroundShortcutRunner.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/FocusConfigurationExtension.appex/FocusConfigurationExtension](MACHOS/FocusConfigurationExtension.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/WidgetConfigurationExtension.appex/WidgetConfigurationExtension](MACHOS/WidgetConfigurationExtension.md)
- [/System/Library/PrivateFrameworks/iCloudDriveCore.framework/PlugIns/CloudDocsDiagnostic.appex/CloudDocsDiagnostic](MACHOS/CloudDocsDiagnostic.md)
- [/System/Library/PrivateFrameworks/iCloudDriveCore.framework/bird](MACHOS/bird.md)
- [/System/Library/PrivateFrameworks/iCloudDriveService.framework/XPCServices/ContainerMetadataExtractor.xpc/ContainerMetadataExtractor](MACHOS/ContainerMetadataExtractor.md)
- [/System/Library/PrivateFrameworks/iCloudNotification.framework/ind](MACHOS/ind.md)
- [/System/Library/PrivateFrameworks/iOSDiagnostics.framework/iosdiagnosticsd](MACHOS/iosdiagnosticsd.md)
- [/System/Library/ScreenReader/BrailleTables/LiblouisBrailleTranslator.brailletable/LiblouisBrailleTranslator](MACHOS/LiblouisBrailleTranslator.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/AudioSuggestionsPlugin.bundle/AudioSuggestionsPlugin](MACHOS/AudioSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/HomeAutomationSiriSuggestions.bundle/HomeAutomationSiriSuggestions](MACHOS/HomeAutomationSiriSuggestions.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriTimeSuggestionsPlugin.bundle/SiriTimeSuggestionsPlugin](MACHOS/SiriTimeSuggestionsPlugin.md)
- [/System/Library/Snippets/UIPlugins/SiriSuggestionsUIPlugin.bundle/SiriSuggestionsUIPlugin](MACHOS/SiriSuggestionsUIPlugin.md)
- [/System/Library/SyncBundles/Books.syncBundle/Books](MACHOS/Books.md)
- [/System/Library/SystemConfiguration/IPConfiguration.bundle/IPConfiguration](MACHOS/IPConfiguration.md)
- [/System/Library/UsageBundles/SoftwareUpdateUsage.bundle/SoftwareUpdateUsage](MACHOS/SoftwareUpdateUsage.md)
- [/System/Library/UserEventPlugins/MobileBackupUEA.plugin/MobileBackupUEA](MACHOS/MobileBackupUEA.md)
- [/System/Library/UserEventPlugins/com.apple.cts.plugin/com.apple.cts](MACHOS/com.apple.cts.md)
- [/System/Library/UserNotifications/Bundles/com.apple.Siri.ActionPredictionNotifications.bundle/com.apple.Siri.ActionPredictionNotifications](MACHOS/com.apple.Siri.ActionPredictionNotifications.md)
- [/System/Library/Video/Plug-Ins/AppleMCTF.bundle/AppleMCTF](MACHOS/AppleMCTF.md)
- [/System/Library/Video/Plug-Ins/AppleVideoEncoder.bundle/AppleVideoEncoder](MACHOS/AppleVideoEncoder.md)
- [/private/var/staged_system_apps/AppStore.app/AppStore](MACHOS/AppStore.md)
- [/private/var/staged_system_apps/AppStore.app/PlugIns/AppStoreWidgetsExtension.appex/AppStoreWidgetsExtension](MACHOS/AppStoreWidgetsExtension.md)
- [/private/var/staged_system_apps/AppleTV.app/PlugIns/TVWidgetExtension.appex/TVWidgetExtension](MACHOS/TVWidgetExtension.md)
- [/private/var/staged_system_apps/AppleVisionProApp.app/AppleVisionProApp](MACHOS/AppleVisionProApp.md)
- [/private/var/staged_system_apps/Books.app/Books](MACHOS/Books.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/AEBookPlugins.framework/AEBookPlugins](MACHOS/AEBookPlugins.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BlissReader.framework/BlissReader](MACHOS/BlissReader.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookAnalytics.framework/BookAnalytics](MACHOS/BookAnalytics.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookCore.framework/BookCore](MACHOS/BookCore.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookEPUB.framework/BookEPUB](MACHOS/BookEPUB.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookStoreUI.framework/BookStoreUI](MACHOS/BookStoreUI.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BooksPersonalization.framework/BooksPersonalization](MACHOS/BooksPersonalization.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/JSApp.framework/JSApp](MACHOS/JSApp.md)
- [/private/var/staged_system_apps/Books.app/PlugIns/BooksWidgetExtension.appex/BooksWidgetExtension](MACHOS/BooksWidgetExtension.md)
- [/private/var/staged_system_apps/Bridge.app/Bridge](MACHOS/Bridge.md)
- [/private/var/staged_system_apps/Calculator.app/Calculator](MACHOS/Calculator.md)
- [/private/var/staged_system_apps/Files.app/Files](MACHOS/Files.md)
- [/private/var/staged_system_apps/FindMy.app/FindMy](MACHOS/FindMy.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyNotificationsService.appex/FindMyNotificationsService](MACHOS/FindMyNotificationsService.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyWidgetItems.appex/FindMyWidgetItems](MACHOS/FindMyWidgetItems.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyWidgetPeople.appex/FindMyWidgetPeople](MACHOS/FindMyWidgetPeople.md)
- [/private/var/staged_system_apps/Fitness.app/Fitness](MACHOS/Fitness.md)
- [/private/var/staged_system_apps/Freeform.app/Extensions/USDRendererExtension.appex/USDRendererExtension](MACHOS/USDRendererExtension.md)
- [/private/var/staged_system_apps/Freeform.app/Freeform](MACHOS/Freeform.md)
- [/private/var/staged_system_apps/Health.app/Health](MACHOS/Health.md)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeEnergyWidgetsExtension.appex/HomeEnergyWidgetsExtension](MACHOS/HomeEnergyWidgetsExtension.md)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeWidget.appex/HomeWidget](MACHOS/HomeWidget.md)
- [/private/var/staged_system_apps/Maps.app/Maps](MACHOS/Maps.md)
- [/private/var/staged_system_apps/Maps.app/PlugIns/GeneralMapsWidget.appex/GeneralMapsWidget](MACHOS/GeneralMapsWidget.md)
- [/private/var/staged_system_apps/MobileMail.app/MobileMail](MACHOS/MobileMail.md)
- [/private/var/staged_system_apps/MobileMail.app/PlugIns/MailNotificationContentExtension.appex/MailNotificationContentExtension](MACHOS/MailNotificationContentExtension.md)
- [/private/var/staged_system_apps/MobileMail.app/PlugIns/MailQuickLookExtension.appex/MailQuickLookExtension](MACHOS/MailQuickLookExtension.md)
- [/private/var/staged_system_apps/MobileMail.app/PlugIns/MailWidgetExtension.appex/MailWidgetExtension](MACHOS/MailWidgetExtension.md)
- [/private/var/staged_system_apps/MobileNotes.app/MobileNotes](MACHOS/MobileNotes.md)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.WidgetExtension.appex/com.apple.mobilenotes.WidgetExtension](MACHOS/com.apple.mobilenotes.WidgetExtension.md)
- [/private/var/staged_system_apps/MobileSafari.app/PlugIns/SafariWidgetExtension.appex/SafariWidgetExtension](MACHOS/SafariWidgetExtension.md)
- [/private/var/staged_system_apps/MobileTimer.app/PlugIns/WorldClockWidget.appex/WorldClockWidget](MACHOS/WorldClockWidget.md)
- [/private/var/staged_system_apps/Music.app/Frameworks/MusicApplication.framework/MusicApplication](MACHOS/MusicApplication.md)
- [/private/var/staged_system_apps/Music.app/Music](MACHOS/Music.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/MusicWidgets.appex/MusicWidgets](MACHOS/MusicWidgets.md)
- [/private/var/staged_system_apps/Passbook.app/PlugIns/PassbookLockedWidgetsExtension.appex/PassbookLockedWidgetsExtension](MACHOS/PassbookLockedWidgetsExtension.md)
- [/private/var/staged_system_apps/Passbook.app/PlugIns/PassbookWidgetsExtension-iPhone.appex/PassbookWidgetsExtension-iPhone](MACHOS/PassbookWidgetsExtension-iPhone.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/NowPlayingUI.framework/NowPlayingUI](MACHOS/NowPlayingUI.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/PodcastsTranscripts.framework/PodcastsTranscripts](MACHOS/PodcastsTranscripts.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/ShelfKit.framework/ShelfKit](MACHOS/ShelfKit.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/ShelfKitCollectionViews.framework/ShelfKitCollectionViews](MACHOS/ShelfKitCollectionViews.md)
- [/private/var/staged_system_apps/Podcasts.app/PlugIns/PodcastsNotificationExtension.appex/PodcastsNotificationExtension](MACHOS/PodcastsNotificationExtension.md)
- [/private/var/staged_system_apps/Podcasts.app/Podcasts](MACHOS/Podcasts.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersIntentsExtension.appex/RemindersIntentsExtension](MACHOS/RemindersIntentsExtension.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersIntentsUIExtension.appex/RemindersIntentsUIExtension](MACHOS/RemindersIntentsUIExtension.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersWidgetExtension.appex/RemindersWidgetExtension](MACHOS/RemindersWidgetExtension.md)
- [/private/var/staged_system_apps/Reminders.app/Reminders](MACHOS/Reminders.md)
- [/private/var/staged_system_apps/Shortcuts.app/PlugIns/ShortcutsWidgetExtension.appex/ShortcutsWidgetExtension](MACHOS/ShortcutsWidgetExtension.md)
- [/private/var/staged_system_apps/VoiceMemos.app/VoiceMemos](MACHOS/VoiceMemos.md)
- [/sbin/launchd](MACHOS/launchd.md)
- [/usr/bin/csfdiagnose](MACHOS/csfdiagnose.md)
- [/usr/bin/sysdiagnose](MACHOS/sysdiagnose.md)
- [/usr/lib/dyld](MACHOS/dyld.md)
- [/usr/lib/libRPAC.dylib](MACHOS/libRPAC.dylib.md)
- [/usr/lib/libmobileassetd.dylib](MACHOS/libmobileassetd.dylib.md)
- [/usr/libexec/BackupAgent2](MACHOS/BackupAgent2.md)
- [/usr/libexec/SensorKitALSHelper](MACHOS/SensorKitALSHelper.md)
- [/usr/libexec/anomalydetectiond](MACHOS/anomalydetectiond.md)
- [/usr/libexec/audioaccessoryd](MACHOS/audioaccessoryd.md)
- [/usr/libexec/bluetoothuserd](MACHOS/bluetoothuserd.md)
- [/usr/libexec/caraccessoryd](MACHOS/caraccessoryd.md)
- [/usr/libexec/carkitd](MACHOS/carkitd.md)
- [/usr/libexec/companiond](MACHOS/companiond.md)
- [/usr/libexec/coreidvd](MACHOS/coreidvd.md)
- [/usr/libexec/cryptexd](MACHOS/cryptexd.md)
- [/usr/libexec/dasd](MACHOS/dasd.md)
- [/usr/libexec/dhcp6d](MACHOS/dhcp6d.md)
- [/usr/libexec/diskarbitrationd](MACHOS/diskarbitrationd.md)
- [/usr/libexec/diskimagesiod](MACHOS/diskimagesiod.md)
- [/usr/libexec/dmd](MACHOS/dmd.md)
- [/usr/libexec/driverkitd](MACHOS/driverkitd.md)
- [/usr/libexec/duetexpertd](MACHOS/duetexpertd.md)
- [/usr/libexec/eligibilityd](MACHOS/eligibilityd.md)
- [/usr/libexec/findmydeviced](MACHOS/findmydeviced.md)
- [/usr/libexec/findmylocated](MACHOS/findmylocated.md)
- [/usr/libexec/fmflocatord](MACHOS/fmflocatord.md)
- [/usr/libexec/fskitd](MACHOS/fskitd.md)
- [/usr/libexec/idcredd](MACHOS/idcredd.md)
- [/usr/libexec/inboxupdaterd](MACHOS/inboxupdaterd.md)
- [/usr/libexec/launchd_cache_loader](MACHOS/launchd_cache_loader.md)
- [/usr/libexec/linkd](MACHOS/linkd.md)
- [/usr/libexec/locationd](MACHOS/locationd.md)
- [/usr/libexec/lockdownd](MACHOS/lockdownd.md)
- [/usr/libexec/logd](MACHOS/logd.md)
- [/usr/libexec/mediaparserd](MACHOS/mediaparserd.md)
- [/usr/libexec/mediaplaybackd](MACHOS/mediaplaybackd.md)
- [/usr/libexec/mobile_obliterator](MACHOS/mobile_obliterator.md)
- [/usr/libexec/mobileactivationd](MACHOS/mobileactivationd.md)
- [/usr/libexec/mobilerepaird](MACHOS/mobilerepaird.md)
- [/usr/libexec/modelmanagerd](MACHOS/modelmanagerd.md)
- [/usr/libexec/nearbyd](MACHOS/nearbyd.md)
- [/usr/libexec/nesessionmanager](MACHOS/nesessionmanager.md)
- [/usr/libexec/networkserviceproxy](MACHOS/networkserviceproxy.md)
- [/usr/libexec/nfcd](MACHOS/nfcd.md)
- [/usr/libexec/profiled](MACHOS/profiled.md)
- [/usr/libexec/promotedcontentd](MACHOS/promotedcontentd.md)
- [/usr/libexec/proximitycontrold](MACHOS/proximitycontrold.md)
- [/usr/libexec/rapportd](MACHOS/rapportd.md)
- [/usr/libexec/remindd](MACHOS/remindd.md)
- [/usr/libexec/safetyalertsd](MACHOS/safetyalertsd.md)
- [/usr/libexec/searchpartyd](MACHOS/searchpartyd.md)
- [/usr/libexec/securityd](MACHOS/securityd.md)
- [/usr/libexec/sensorkitd](MACHOS/sensorkitd.md)
- [/usr/libexec/seserviced](MACHOS/seserviced.md)
- [/usr/libexec/sharingd](MACHOS/sharingd.md)
- [/usr/libexec/srp-mdns-proxy](MACHOS/srp-mdns-proxy.md)
- [/usr/libexec/swtransparencyd](MACHOS/swtransparencyd.md)
- [/usr/libexec/sysdiagnosed](MACHOS/sysdiagnosed.md)
- [/usr/libexec/thermalmonitord](MACHOS/thermalmonitord.md)
- [/usr/libexec/transparencyd](MACHOS/transparencyd.md)
- [/usr/libexec/trustd](MACHOS/trustd.md)
- [/usr/libexec/tursd](MACHOS/tursd.md)
- [/usr/libexec/uarppersonalizationd](MACHOS/uarppersonalizationd.md)
- [/usr/libexec/videocodecd](MACHOS/videocodecd.md)
- [/usr/libexec/wifip2pd](MACHOS/wifip2pd.md)
- [/usr/libexec/xpcproxy](MACHOS/xpcproxy.md)
- [/usr/libexec/xpcroleaccountd](MACHOS/xpcroleaccountd.md)
- [/usr/sbin/absd](MACHOS/absd.md)
- [/usr/sbin/bluetoothd](MACHOS/bluetoothd.md)

</details>

### 🔑 Entitlements

- [Entitlements DIFF](Entitlements.md)

## Firmware

### ⬆️ Updated (21)

<details>
  <summary><i>View Updated</i></summary>

- [AppleAVE2FW_H17.im4p](FIRMWARE/AppleAVE2FW_H17.im4p.md)
- [SmartIOFirmware_ASCv7.im4p](FIRMWARE/SmartIOFirmware_ASCv7.im4p.md)
- [adc-rheia-d9x.im4p](FIRMWARE/adc-rheia-d9x.im4p.md)
- [agx_a000](FIRMWARE/agx_a000.md)
- [agx_a010](FIRMWARE/agx_a010.md)
- [agx_b000](FIRMWARE/agx_b000.md)
- [agx_b010](FIRMWARE/agx_b010.md)
- [agx_b100](FIRMWARE/agx_b100.md)
- [ansf.t8140.release.im4p](FIRMWARE/ansf.t8140.release.im4p.md)
- [exclave_ExclaveStackshotServer](FIRMWARE/exclave_ExclaveStackshotServer.md)
- [exclave_kernel](FIRMWARE/exclave_kernel.md)
- [exclave_pmm_exclave](FIRMWARE/exclave_pmm_exclave.md)
- [exclave_roottask](FIRMWARE/exclave_roottask.md)
- [exclave_scheduler](FIRMWARE/exclave_scheduler.md)
- [exclave_sharedcache](FIRMWARE/exclave_sharedcache.md)
- [h17_ane_fw_theia_d9x.im4p](FIRMWARE/h17_ane_fw_theia_d9x.im4p.md)
- [rans.t8140.release.im4p](FIRMWARE/rans.t8140.release.im4p.md)
- [securem3fw-d9x.im4p](FIRMWARE/securem3fw-d9x.im4p.md)
- [sptm.t8140.release.im4p](FIRMWARE/sptm.t8140.release.im4p.md)
- [t8140pmp.im4p](FIRMWARE/t8140pmp.im4p.md)
- [txm.iphoneos.release.im4p](FIRMWARE/txm.iphoneos.release.im4p.md)

</details>

### iBoot

| iOS | Version |
| :-- | :------ |
| 18.5 *(22F5042g)* | iBoot-11881.120.91.0.1 |
| 18.5 *(22F5053f)* | iBoot-11881.120.111.0.1 |

#### 🆕 NEW (2)

<details>
  <summary><i>View NEW</i></summary>

##### `iboot`
  - `iBoot-11881.120.111.0.1`
  - `~v)|L|p ri`
  - `bQʅmrjA˛=`
  - `b10c19e591df8f0a343a644bf6dcbe19`
  - `^$kA#NQw89Y`
  - `root@jmqcv.p1l.plx.sd...2025/04/07@02:43:35`
  - ` ApplePMUFirmware-503.120.3~192.release`
##### `AppleSMCFirmware.bin`
  - `AppleSMCFirmware_H17-5204.120.48.d93.REL`

</details>

#### ❌ Removed (2)

<details>
  <summary><i>View Removed</i></summary>

##### `iboot`
  - ` ApplePMUFirmware-503.120.2~328.release`
  - `iBoot-11881.120.91.0.1`
  - `":xLU+bHn@B`
  - `root@g5wnr.p1l.plx.sd...2025/03/21@21:24:02`
  - `(3-;9Gæ_J`
  - `w^-ƿev$£9`
  - `48d11dabb471e66eede5813dfc056de3`
##### `AppleSMCFirmware.bin`
  - `AppleSMCFirmware_H17-5204.120.45.d93.REL`

</details>

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 18.5 *(22F5042g)* | 621.2.1.10.3 |
| 18.5 *(22F5053f)* | 621.2.3.10.3 |

### Dylibs

#### ⬆️ Updated (665)

<details>
  <summary><i>View Updated</i></summary>

- [/System/Library/AccessibilityBundles/BackBoard.axbundle/BackBoard](DYLIBS/BackBoard.md)
- [/System/Library/AccessibilityBundles/ChatKitFramework.axbundle/ChatKitFramework](DYLIBS/ChatKitFramework.md)
- [/System/Library/AccessibilityBundles/CoreIDVUI.axbundle/CoreIDVUI](DYLIBS/CoreIDVUI.md)
- [/System/Library/AccessibilityBundles/PosterBoardFramework.axbundle/PosterBoardFramework](DYLIBS/PosterBoardFramework.md)
- [/System/Library/AccessibilityBundles/SystemApertureUI.axbundle/SystemApertureUI](DYLIBS/SystemApertureUI.md)
- [/System/Library/AccessibilityBundles/ToneKit.axbundle/ToneKit](DYLIBS/ToneKit.md)
- [/System/Library/AccessibilityBundles/UIKit.axbundle/UIKit](DYLIBS/UIKit.md)
- [/System/Library/AccessibilityBundles/UserNotificationsUIKit.axbundle/UserNotificationsUIKit](DYLIBS/UserNotificationsUIKit.md)
- [/System/Library/AccessibilityBundles/VideosUIFramework.axbundle/VideosUIFramework](DYLIBS/VideosUIFramework.md)
- [/System/Library/Accounts/Notification/ADAccountsNotificationPlugin.bundle/ADAccountsNotificationPlugin](DYLIBS/ADAccountsNotificationPlugin.md)
- [/System/Library/Accounts/Notification/CloudKitNotificationPlugin.bundle/CloudKitNotificationPlugin](DYLIBS/CloudKitNotificationPlugin.md)
- [/System/Library/Accounts/Notification/FindMyDeviceAccountNotificationPlugin.bundle/FindMyDeviceAccountNotificationPlugin](DYLIBS/FindMyDeviceAccountNotificationPlugin.md)
- [/System/Library/ControlCenter/Bundles/ConnectivityModule.bundle/ConnectivityModule](DYLIBS/ConnectivityModule.md)
- [/System/Library/DataClassMigrators/MessagesDataMigrator.migrator/MessagesDataMigrator](DYLIBS/MessagesDataMigrator.md)
- [/System/Library/Extensions/AGXMetalG17P.bundle/AGXMetalG17P](DYLIBS/AGXMetalG17P.md)
- [/System/Library/Fitness/Plugins/SeymourAwardsPlugin.bundle/SeymourAwardsPlugin](DYLIBS/SeymourAwardsPlugin.md)
- [/System/Library/Frameworks/AVFAudio.framework/AVFAudio](DYLIBS/AVFAudio.md)
- [/System/Library/Frameworks/AVKit.framework/AVKit](DYLIBS/AVKit.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libBLAS.dylib](DYLIBS/libBLAS.dylib.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libLAPACK.dylib](DYLIBS/libLAPACK.dylib.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libSparse.dylib](DYLIBS/libSparse.dylib.md)
- [/System/Library/Frameworks/AppIntents.framework/AppIntents](DYLIBS/AppIntents.md)
- [/System/Library/Frameworks/AudioToolbox.framework/AudioCodecs](DYLIBS/AudioCodecs.md)
- [/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox](DYLIBS/AudioToolbox.md)
- [/System/Library/Frameworks/AudioToolbox.framework/libAudioDSP.dylib](DYLIBS/libAudioDSP.dylib.md)
- [/System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices](DYLIBS/AuthenticationServices.md)
- [/System/Library/Frameworks/CFNetwork.framework/CFNetwork](DYLIBS/CFNetwork.md)
- [/System/Library/Frameworks/CarPlay.framework/CarPlay](DYLIBS/CarPlay.md)
- [/System/Library/Frameworks/CloudKit.framework/CloudKit](DYLIBS/CloudKit.md)
- [/System/Library/Frameworks/CoreAudio.framework/CoreAudio](DYLIBS/CoreAudio.md)
- [/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth](DYLIBS/CoreBluetooth.md)
- [/System/Library/Frameworks/CoreData.framework/CoreData](DYLIBS/CoreData.md)
- [/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation](DYLIBS/CoreFoundation.md)
- [/System/Library/Frameworks/CoreGraphics.framework/CoreGraphics](DYLIBS/CoreGraphics.md)
- [/System/Library/Frameworks/CoreML.framework/CoreML](DYLIBS/CoreML.md)
- [/System/Library/Frameworks/CoreMedia.framework/CoreMedia](DYLIBS/CoreMedia.md)
- [/System/Library/Frameworks/CoreMotion.framework/CoreMotion](DYLIBS/CoreMotion.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight](DYLIBS/CoreSpotlight.md)
- [/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony](DYLIBS/CoreTelephony.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterBase.dylib](DYLIBS/libCommCenterBase.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterKCommandDrivers.dylib](DYLIBS/libCommCenterKCommandDrivers.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterMCommandDrivers.dylib](DYLIBS/libCommCenterMCommandDrivers.dylib.md)
- [/System/Library/Frameworks/CoreText.framework/CoreText](DYLIBS/CoreText.md)
- [/System/Library/Frameworks/DeviceCheck.framework/DeviceCheck](DYLIBS/DeviceCheck.md)
- [/System/Library/Frameworks/ExternalAccessory.framework/ExternalAccessory](DYLIBS/ExternalAccessory.md)
- [/System/Library/Frameworks/FinanceKit.framework/FinanceKit](DYLIBS/FinanceKit.md)
- [/System/Library/Frameworks/FinanceKitUI.framework/FinanceKitUI](DYLIBS/FinanceKitUI.md)
- [/System/Library/Frameworks/Foundation.framework/Foundation](DYLIBS/Foundation.md)
- [/System/Library/Frameworks/GameController.framework/GameController](DYLIBS/GameController.md)
- [/System/Library/Frameworks/HomeKit.framework/HomeKit](DYLIBS/HomeKit.md)
- [/System/Library/Frameworks/ImageIO.framework/ImageIO](DYLIBS/ImageIO.md)
- [/System/Library/Frameworks/Intents.framework/Intents](DYLIBS/Intents.md)
- [/System/Library/Frameworks/JavaScriptCore.framework/JavaScriptCore](DYLIBS/JavaScriptCore.md)
- [/System/Library/Frameworks/LinkPresentation.framework/LinkPresentation](DYLIBS/LinkPresentation.md)
- [/System/Library/Frameworks/LiveCommunicationKit.framework/LiveCommunicationKit](DYLIBS/LiveCommunicationKit.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/DaemonUtils.framework/DaemonUtils](DYLIBS/DaemonUtils.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/ModuleBase.framework/ModuleBase](DYLIBS/ModuleBase.md)
- [/System/Library/Frameworks/ManagedApp.framework/ManagedApp](DYLIBS/ManagedApp.md)
- [/System/Library/Frameworks/MapKit.framework/MapKit](DYLIBS/MapKit.md)
- [/System/Library/Frameworks/Matter.framework/Matter](DYLIBS/Matter.md)
- [/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox](DYLIBS/MediaToolbox.md)
- [/System/Library/Frameworks/MessageUI.framework/MessageUI](DYLIBS/MessageUI.md)
- [/System/Library/Frameworks/Metal.framework/Metal](DYLIBS/Metal.md)
- [/System/Library/Frameworks/MetalFX.framework/MetalFX](DYLIBS/MetalFX.md)
- [/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSBenchmarkLoop.framework/MPSBenchmarkLoop](DYLIBS/MPSBenchmarkLoop.md)
- [/System/Library/Frameworks/MusicKit.framework/MusicKit](DYLIBS/MusicKit.md)
- [/System/Library/Frameworks/Network.framework/Network](DYLIBS/Network.md)
- [/System/Library/Frameworks/PDFKit.framework/PDFKit](DYLIBS/PDFKit.md)
- [/System/Library/Frameworks/Photos.framework/Photos](DYLIBS/Photos.md)
- [/System/Library/Frameworks/QuartzCore.framework/QuartzCore](DYLIBS/QuartzCore.md)
- [/System/Library/Frameworks/QuickLook.framework/QuickLook](DYLIBS/QuickLook.md)
- [/System/Library/Frameworks/RealityFoundation.framework/RealityFoundation](DYLIBS/RealityFoundation.md)
- [/System/Library/Frameworks/SafariServices.framework/SafariServices](DYLIBS/SafariServices.md)
- [/System/Library/Frameworks/SecureElementCredential.framework/SecureElementCredential](DYLIBS/SecureElementCredential.md)
- [/System/Library/Frameworks/Security.framework/Security](DYLIBS/Security.md)
- [/System/Library/Frameworks/SensorKit.framework/SensorKit](DYLIBS/SensorKit.md)
- [/System/Library/Frameworks/ShazamKit.framework/ShazamKit](DYLIBS/ShazamKit.md)
- [/System/Library/Frameworks/SoundAnalysis.framework/SoundAnalysis](DYLIBS/SoundAnalysis.md)
- [/System/Library/Frameworks/StickerKit.framework/StickerKit](DYLIBS/StickerKit.md)
- [/System/Library/Frameworks/StoreKit.framework/StoreKit](DYLIBS/StoreKit.md)
- [/System/Library/Frameworks/SwiftUI.framework/SwiftUI](DYLIBS/SwiftUI.md)
- [/System/Library/Frameworks/SwiftUICore.framework/SwiftUICore](DYLIBS/SwiftUICore.md)
- [/System/Library/Frameworks/VideoToolbox.framework/VideoToolbox](DYLIBS/VideoToolbox.md)
- [/System/Library/Frameworks/WebKit.framework/WebKit](DYLIBS/WebKit.md)
- [/System/Library/Frameworks/WidgetKit.framework/WidgetKit](DYLIBS/WidgetKit.md)
- [/System/Library/Frameworks/WorkoutKit.framework/WorkoutKit](DYLIBS/WorkoutKit.md)
- [/System/Library/Frameworks/_AuthenticationServices_SwiftUI.framework/_AuthenticationServices_SwiftUI](DYLIBS/_AuthenticationServices_SwiftUI.md)
- [/System/Library/Frameworks/_MapKit_SwiftUI.framework/_MapKit_SwiftUI](DYLIBS/_MapKit_SwiftUI.md)
- [/System/Library/Frameworks/_RealityKit_SwiftUI.framework/_RealityKit_SwiftUI](DYLIBS/_RealityKit_SwiftUI.md)
- [/System/Library/Frameworks/_StoreKit_SwiftUI.framework/_StoreKit_SwiftUI](DYLIBS/_StoreKit_SwiftUI.md)
- [/System/Library/Health/FeedItemPlugins/HealthArticles.healthplugin/HealthArticles](DYLIBS/HealthArticles.md)
- [/System/Library/Health/FeedItemPlugins/HearingAppPlugin.healthplugin/HearingAppPlugin](DYLIBS/HearingAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/Heart.healthplugin/Heart](DYLIBS/Heart.md)
- [/System/Library/Health/FeedItemPlugins/Highlights.healthplugin/Highlights](DYLIBS/Highlights.md)
- [/System/Library/Health/FeedItemPlugins/MedicationsHealthAppPlugin.healthplugin/MedicationsHealthAppPlugin](DYLIBS/MedicationsHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/MenstrualCyclesAppPlugin.healthplugin/MenstrualCyclesAppPlugin](DYLIBS/MenstrualCyclesAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/MentalHealthAppPlugin.healthplugin/MentalHealthAppPlugin](DYLIBS/MentalHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/Profiles.healthplugin/Profiles](DYLIBS/Profiles.md)
- [/System/Library/Health/FeedItemPlugins/RespiratoryHealthAppPlugin.healthplugin/RespiratoryHealthAppPlugin](DYLIBS/RespiratoryHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/Safety.healthplugin/Safety](DYLIBS/Safety.md)
- [/System/Library/Health/FeedItemPlugins/SleepHealthAppPlugin.healthplugin/SleepHealthAppPlugin](DYLIBS/SleepHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/Summaries.healthplugin/Summaries](DYLIBS/Summaries.md)
- [/System/Library/Health/FeedItemPlugins/VisionHealthAppPlugin.healthplugin/VisionHealthAppPlugin](DYLIBS/VisionHealthAppPlugin.md)
- [/System/Library/MediaCapture/H16ISP.mediacapture](DYLIBS/H16ISP.mediacapture.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKEsterbrookFaceBundleCompanion.bundle/NTKEsterbrookFaceBundleCompanion](DYLIBS/NTKEsterbrookFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKParmesanFaceBundleCompanion.bundle/NTKParmesanFaceBundleCompanion](DYLIBS/NTKParmesanFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKRhizomeFaceBundleCompanion.bundle/NTKRhizomeFaceBundleCompanion](DYLIBS/NTKRhizomeFaceBundleCompanion.md)
- [/System/Library/Previews/ShellPlugins/WidgetPreviewsShellPlugin.bundle/WidgetPreviewsShellPlugin](DYLIBS/WidgetPreviewsShellPlugin.md)
- [/System/Library/PrivateFrameworks/AGXCompilerCore.framework/AGXCompilerCore](DYLIBS/AGXCompilerCore.md)
- [/System/Library/PrivateFrameworks/APFoundation.framework/APFoundation](DYLIBS/APFoundation.md)
- [/System/Library/PrivateFrameworks/ASRBridge.framework/ASRBridge](DYLIBS/ASRBridge.md)
- [/System/Library/PrivateFrameworks/AUSettings.framework/AUSettings](DYLIBS/AUSettings.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/AVConference](DYLIBS/AVConference.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ViceroyTrace.framework/ViceroyTrace](DYLIBS/ViceroyTrace.md)
- [/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture](DYLIBS/AVFCapture.md)
- [/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore](DYLIBS/AVFCore.md)
- [/System/Library/PrivateFrameworks/AccessibilitySettingsUI.framework/AccessibilitySettingsUI](DYLIBS/AccessibilitySettingsUI.md)
- [/System/Library/PrivateFrameworks/AccessibilitySharedUISupport.framework/AccessibilitySharedUISupport](DYLIBS/AccessibilitySharedUISupport.md)
- [/System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities](DYLIBS/AccessibilityUtilities.md)
- [/System/Library/PrivateFrameworks/ActionKit.framework/ActionKit](DYLIBS/ActionKit.md)
- [/System/Library/PrivateFrameworks/AdCore.framework/AdCore](DYLIBS/AdCore.md)
- [/System/Library/PrivateFrameworks/AdID.framework/AdID](DYLIBS/AdID.md)
- [/System/Library/PrivateFrameworks/AdPlatformsCommon.framework/AdPlatformsCommon](DYLIBS/AdPlatformsCommon.md)
- [/System/Library/PrivateFrameworks/AdaptiveMusic.framework/AdaptiveMusic](DYLIBS/AdaptiveMusic.md)
- [/System/Library/PrivateFrameworks/AirPlayReceiverKit.framework/AirPlayReceiverKit](DYLIBS/AirPlayReceiverKit.md)
- [/System/Library/PrivateFrameworks/AirPlaySender.framework/AirPlaySender](DYLIBS/AirPlaySender.md)
- [/System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport](DYLIBS/AirPlaySupport.md)
- [/System/Library/PrivateFrameworks/AlarmUIFramework.framework/AlarmUIFramework](DYLIBS/AlarmUIFramework.md)
- [/System/Library/PrivateFrameworks/Announce.framework/Announce](DYLIBS/Announce.md)
- [/System/Library/PrivateFrameworks/AnnounceDaemon.framework/AnnounceDaemon](DYLIBS/AnnounceDaemon.md)
- [/System/Library/PrivateFrameworks/Anvil.framework/Anvil](DYLIBS/Anvil.md)
- [/System/Library/PrivateFrameworks/AppAttestInternal.framework/AppAttestInternal](DYLIBS/AppAttestInternal.md)
- [/System/Library/PrivateFrameworks/AppProtection.framework/AppProtection](DYLIBS/AppProtection.md)
- [/System/Library/PrivateFrameworks/AppProtectionUI.framework/AppProtectionUI](DYLIBS/AppProtectionUI.md)
- [/System/Library/PrivateFrameworks/AppSSO.framework/AppSSO](DYLIBS/AppSSO.md)
- [/System/Library/PrivateFrameworks/AppStoreKit.framework/AppStoreKit](DYLIBS/AppStoreKit.md)
- [/System/Library/PrivateFrameworks/AppleAccountUI.framework/AppleAccountUI](DYLIBS/AppleAccountUI.md)
- [/System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore](DYLIBS/AppleKeyStore.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices](DYLIBS/AppleMediaServices.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesKitInternal.framework/AppleMediaServicesKitInternal](DYLIBS/AppleMediaServicesKitInternal.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/AppleMediaServicesUI](DYLIBS/AppleMediaServicesUI.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUIPaymentSheets.framework/AppleMediaServicesUIPaymentSheets](DYLIBS/AppleMediaServicesUIPaymentSheets.md)
- [/System/Library/PrivateFrameworks/ApplePushService.framework/ApplePushService](DYLIBS/ApplePushService.md)
- [/System/Library/PrivateFrameworks/AppleServiceToolkit.framework/AppleServiceToolkit](DYLIBS/AppleServiceToolkit.md)
- [/System/Library/PrivateFrameworks/AskPermission.framework/AskPermission](DYLIBS/AskPermission.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices](DYLIBS/AssistantServices.md)
- [/System/Library/PrivateFrameworks/AssistantSettingsSupport.framework/AssistantSettingsSupport](DYLIBS/AssistantSettingsSupport.md)
- [/System/Library/PrivateFrameworks/AssistantUI.framework/AssistantUI](DYLIBS/AssistantUI.md)
- [/System/Library/PrivateFrameworks/AudioDSPManager.framework/AudioDSPManager](DYLIBS/AudioDSPManager.md)
- [/System/Library/PrivateFrameworks/AudioServerDriverTransports_Base.framework/AudioServerDriverTransports_Base](DYLIBS/AudioServerDriverTransports_Base.md)
- [/System/Library/PrivateFrameworks/AudioServerDriverTransports_IOA2.framework/AudioServerDriverTransports_IOA2](DYLIBS/AudioServerDriverTransports_IOA2.md)
- [/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit](DYLIBS/AuthKit.md)
- [/System/Library/PrivateFrameworks/AuthenticationServicesCore.framework/AuthenticationServicesCore](DYLIBS/AuthenticationServicesCore.md)
- [/System/Library/PrivateFrameworks/BiomeFoundation.framework/BiomeFoundation](DYLIBS/BiomeFoundation.md)
- [/System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary](DYLIBS/BiomeLibrary.md)
- [/System/Library/PrivateFrameworks/BiomePubSub.framework/BiomePubSub](DYLIBS/BiomePubSub.md)
- [/System/Library/PrivateFrameworks/BiomeStorage.framework/BiomeStorage](DYLIBS/BiomeStorage.md)
- [/System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams](DYLIBS/BiomeStreams.md)
- [/System/Library/PrivateFrameworks/Blackbeard.framework/Blackbeard](DYLIBS/Blackbeard.md)
- [/System/Library/PrivateFrameworks/BlastDoor.framework/BlastDoor](DYLIBS/BlastDoor.md)
- [/System/Library/PrivateFrameworks/BrailleSymbology.framework/BrailleSymbology](DYLIBS/BrailleSymbology.md)
- [/System/Library/PrivateFrameworks/BusinessChatService.framework/BusinessChatService](DYLIBS/BusinessChatService.md)
- [/System/Library/PrivateFrameworks/CAFCombine.framework/CAFCombine](DYLIBS/CAFCombine.md)
- [/System/Library/PrivateFrameworks/CDMFoundation.framework/CDMFoundation](DYLIBS/CDMFoundation.md)
- [/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture](DYLIBS/CMCapture.md)
- [/System/Library/PrivateFrameworks/CMCaptureCore.framework/CMCaptureCore](DYLIBS/CMCaptureCore.md)
- [/System/Library/PrivateFrameworks/CMImaging.framework/CMImaging](DYLIBS/CMImaging.md)
- [/System/Library/PrivateFrameworks/CMPhoto.framework/CMPhoto](DYLIBS/CMPhoto.md)
- [/System/Library/PrivateFrameworks/CSExattrCrypto.framework/CSExattrCrypto](DYLIBS/CSExattrCrypto.md)
- [/System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete](DYLIBS/CacheDelete.md)
- [/System/Library/PrivateFrameworks/CalendarUIKit.framework/CalendarUIKit](DYLIBS/CalendarUIKit.md)
- [/System/Library/PrivateFrameworks/CallHistory.framework/CallHistory](DYLIBS/CallHistory.md)
- [/System/Library/PrivateFrameworks/CarKit.framework/CarKit](DYLIBS/CarKit.md)
- [/System/Library/PrivateFrameworks/CarKitNavigation.framework/CarKitNavigation](DYLIBS/CarKitNavigation.md)
- [/System/Library/PrivateFrameworks/CarPlayAssetUI.framework/CarPlayAssetUI](DYLIBS/CarPlayAssetUI.md)
- [/System/Library/PrivateFrameworks/CarPlaySupport.framework/CarPlaySupport](DYLIBS/CarPlaySupport.md)
- [/System/Library/PrivateFrameworks/CarPlayUI.framework/CarPlayUI](DYLIBS/CarPlayUI.md)
- [/System/Library/PrivateFrameworks/CascadeEngine.framework/CascadeEngine](DYLIBS/CascadeEngine.md)
- [/System/Library/PrivateFrameworks/CascadeSets.framework/CascadeSets](DYLIBS/CascadeSets.md)
- [/System/Library/PrivateFrameworks/Celestial.framework/Celestial](DYLIBS/Celestial.md)
- [/System/Library/PrivateFrameworks/ChatKit.framework/ChatKit](DYLIBS/ChatKit.md)
- [/System/Library/PrivateFrameworks/ChronoCore.framework/ChronoCore](DYLIBS/ChronoCore.md)
- [/System/Library/PrivateFrameworks/ChronoKit.framework/ChronoKit](DYLIBS/ChronoKit.md)
- [/System/Library/PrivateFrameworks/ChronoServices.framework/ChronoServices](DYLIBS/ChronoServices.md)
- [/System/Library/PrivateFrameworks/ChronoUIServices.framework/ChronoUIServices](DYLIBS/ChronoUIServices.md)
- [/System/Library/PrivateFrameworks/CipherML.framework/CipherML](DYLIBS/CipherML.md)
- [/System/Library/PrivateFrameworks/ClassroomKit.framework/Frameworks/ClassroomUIKit.framework/ClassroomUIKit](DYLIBS/ClassroomUIKit.md)
- [/System/Library/PrivateFrameworks/CloudAsset.framework/CloudAsset](DYLIBS/CloudAsset.md)
- [/System/Library/PrivateFrameworks/CloudAssetDaemon.framework/CloudAssetDaemon](DYLIBS/CloudAssetDaemon.md)
- [/System/Library/PrivateFrameworks/CloudAssets.framework/CloudAssets](DYLIBS/CloudAssets.md)
- [/System/Library/PrivateFrameworks/CloudAttestation.framework/CloudAttestation](DYLIBS/CloudAttestation.md)
- [/System/Library/PrivateFrameworks/CloudDocs.framework/CloudDocs](DYLIBS/CloudDocs.md)
- [/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/CloudPhotoLibrary](DYLIBS/CloudPhotoLibrary.md)
- [/System/Library/PrivateFrameworks/CloudRecommendationUI.framework/CloudRecommendationUI](DYLIBS/CloudRecommendationUI.md)
- [/System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/CloudSubscriptionFeatures](DYLIBS/CloudSubscriptionFeatures.md)
- [/System/Library/PrivateFrameworks/CommandAndControlUI.framework/CommandAndControlUI](DYLIBS/CommandAndControlUI.md)
- [/System/Library/PrivateFrameworks/CommunicationsSetupUI.framework/CommunicationsSetupUI](DYLIBS/CommunicationsSetupUI.md)
- [/System/Library/PrivateFrameworks/CommunicationsUI.framework/CommunicationsUI](DYLIBS/CommunicationsUI.md)
- [/System/Library/PrivateFrameworks/ComplicationDisplay.framework/ComplicationDisplay](DYLIBS/ComplicationDisplay.md)
- [/System/Library/PrivateFrameworks/ContainerManagerCommon.framework/ContainerManagerCommon](DYLIBS/ContainerManagerCommon.md)
- [/System/Library/PrivateFrameworks/ContentKit.framework/ContentKit](DYLIBS/ContentKit.md)
- [/System/Library/PrivateFrameworks/ContextSync.framework/ContextSync](DYLIBS/ContextSync.md)
- [/System/Library/PrivateFrameworks/ControlCenterUI.framework/ControlCenterUI](DYLIBS/ControlCenterUI.md)
- [/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics](DYLIBS/CoreAnalytics.md)
- [/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness](DYLIBS/CoreBrightness.md)
- [/System/Library/PrivateFrameworks/CoreCDPUI.framework/CoreCDPUI](DYLIBS/CoreCDPUI.md)
- [/System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet](DYLIBS/CoreDuet.md)
- [/System/Library/PrivateFrameworks/CoreIDVRGBLiveness.framework/CoreIDVRGBLiveness](DYLIBS/CoreIDVRGBLiveness.md)
- [/System/Library/PrivateFrameworks/CoreIDVShared.framework/CoreIDVShared](DYLIBS/CoreIDVShared.md)
- [/System/Library/PrivateFrameworks/CoreIDVUI.framework/CoreIDVUI](DYLIBS/CoreIDVUI.md)
- [/System/Library/PrivateFrameworks/CoreKnowledge.framework/CoreKnowledge](DYLIBS/CoreKnowledge.md)
- [/System/Library/PrivateFrameworks/CoreLocationTiles.framework/CoreLocationTiles](DYLIBS/CoreLocationTiles.md)
- [/System/Library/PrivateFrameworks/CoreMotionAlgorithms.framework/CoreMotionAlgorithms](DYLIBS/CoreMotionAlgorithms.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/CoreParsec](DYLIBS/CoreParsec.md)
- [/System/Library/PrivateFrameworks/CoreRepairUI.framework/CoreRepairUI](DYLIBS/CoreRepairUI.md)
- [/System/Library/PrivateFrameworks/CoreServicesInternal.framework/CoreServicesInternal](DYLIBS/CoreServicesInternal.md)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/CoreSpeech](DYLIBS/CoreSpeech.md)
- [/System/Library/PrivateFrameworks/CoreSpeechExclave.framework/CoreSpeechExclave](DYLIBS/CoreSpeechExclave.md)
- [/System/Library/PrivateFrameworks/CoreSpeechFoundation.framework/CoreSpeechFoundation](DYLIBS/CoreSpeechFoundation.md)
- [/System/Library/PrivateFrameworks/CoreSpeechUtils.framework/CoreSpeechUtils](DYLIBS/CoreSpeechUtils.md)
- [/System/Library/PrivateFrameworks/CoreThreadRadio.framework/CoreThreadRadio](DYLIBS/CoreThreadRadio.md)
- [/System/Library/PrivateFrameworks/CoreUARP.framework/CoreUARP](DYLIBS/CoreUARP.md)
- [/System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils](DYLIBS/CoreUtils.md)
- [/System/Library/PrivateFrameworks/CoreUtilsExtras.framework/CoreUtilsExtras](DYLIBS/CoreUtilsExtras.md)
- [/System/Library/PrivateFrameworks/CosmeticAssessment.framework/CosmeticAssessment](DYLIBS/CosmeticAssessment.md)
- [/System/Library/PrivateFrameworks/CoverSheet.framework/CoverSheet](DYLIBS/CoverSheet.md)
- [/System/Library/PrivateFrameworks/CryptexServer.framework/CryptexServer](DYLIBS/CryptexServer.md)
- [/System/Library/PrivateFrameworks/DMCApps.framework/DMCApps](DYLIBS/DMCApps.md)
- [/System/Library/PrivateFrameworks/DailyBriefingCommon.framework/DailyBriefingCommon](DYLIBS/DailyBriefingCommon.md)
- [/System/Library/PrivateFrameworks/DashBoard.framework/DashBoard](DYLIBS/DashBoard.md)
- [/System/Library/PrivateFrameworks/DataFlow.framework/DataFlow](DYLIBS/DataFlow.md)
- [/System/Library/PrivateFrameworks/Dendrite.framework/Dendrite](DYLIBS/Dendrite.md)
- [/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/DesktopServicesPriv](DYLIBS/DesktopServicesPriv.md)
- [/System/Library/PrivateFrameworks/DeviceCheckInternal.framework/DeviceCheckInternal](DYLIBS/DeviceCheckInternal.md)
- [/System/Library/PrivateFrameworks/DeviceDiscoveryUI.framework/DeviceDiscoveryUI](DYLIBS/DeviceDiscoveryUI.md)
- [/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/DeviceExpertIntents](DYLIBS/DeviceExpertIntents.md)
- [/System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity](DYLIBS/DeviceIdentity.md)
- [/System/Library/PrivateFrameworks/DeviceManagement.framework/DeviceManagement](DYLIBS/DeviceManagement.md)
- [/System/Library/PrivateFrameworks/DeviceSharing.framework/DeviceSharing](DYLIBS/DeviceSharing.md)
- [/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/DifferentialPrivacy](DYLIBS/DifferentialPrivacy.md)
- [/System/Library/PrivateFrameworks/DisembarkUI.framework/DisembarkUI](DYLIBS/DisembarkUI.md)
- [/System/Library/PrivateFrameworks/DiskImages2.framework/DiskImages2](DYLIBS/DiskImages2.md)
- [/System/Library/PrivateFrameworks/DistributedTimers.framework/DistributedTimers](DYLIBS/DistributedTimers.md)
- [/System/Library/PrivateFrameworks/DistributedTimersDaemon.framework/DistributedTimersDaemon](DYLIBS/DistributedTimersDaemon.md)
- [/System/Library/PrivateFrameworks/DocumentManagerCore.framework/DocumentManagerCore](DYLIBS/DocumentManagerCore.md)
- [/System/Library/PrivateFrameworks/DocumentManagerExecutables.framework/DocumentManagerExecutables](DYLIBS/DocumentManagerExecutables.md)
- [/System/Library/PrivateFrameworks/DropletUI.framework/DropletUI](DYLIBS/DropletUI.md)
- [/System/Library/PrivateFrameworks/Dyld.framework/Dyld](DYLIBS/Dyld.md)
- [/System/Library/PrivateFrameworks/Email.framework/Email](DYLIBS/Email.md)
- [/System/Library/PrivateFrameworks/EmailDaemon.framework/EmailDaemon](DYLIBS/EmailDaemon.md)
- [/System/Library/PrivateFrameworks/EmailFoundation.framework/EmailFoundation](DYLIBS/EmailFoundation.md)
- [/System/Library/PrivateFrameworks/Espresso.framework/Espresso](DYLIBS/Espresso.md)
- [/System/Library/PrivateFrameworks/FMFCore.framework/FMFCore](DYLIBS/FMFCore.md)
- [/System/Library/PrivateFrameworks/FMIPCore.framework/FMIPCore](DYLIBS/FMIPCore.md)
- [/System/Library/PrivateFrameworks/FSKit.framework/FSKit](DYLIBS/FSKit.md)
- [/System/Library/PrivateFrameworks/FaceTimeMessageStore.framework/FaceTimeMessageStore](DYLIBS/FaceTimeMessageStore.md)
- [/System/Library/PrivateFrameworks/FedStats.framework/FedStats](DYLIBS/FedStats.md)
- [/System/Library/PrivateFrameworks/FedStatsPluginCore.framework/FedStatsPluginCore](DYLIBS/FedStatsPluginCore.md)
- [/System/Library/PrivateFrameworks/Feedback.framework/Feedback](DYLIBS/Feedback.md)
- [/System/Library/PrivateFrameworks/FeedbackCore.framework/FeedbackCore](DYLIBS/FeedbackCore.md)
- [/System/Library/PrivateFrameworks/FeedbackLogger.framework/FeedbackLogger](DYLIBS/FeedbackLogger.md)
- [/System/Library/PrivateFrameworks/FileProviderDaemon.framework/FileProviderDaemon](DYLIBS/FileProviderDaemon.md)
- [/System/Library/PrivateFrameworks/FinanceDaemon.framework/FinanceDaemon](DYLIBS/FinanceDaemon.md)
- [/System/Library/PrivateFrameworks/FindMyBase.framework/FindMyBase](DYLIBS/FindMyBase.md)
- [/System/Library/PrivateFrameworks/FindMyBluetooth.framework/FindMyBluetooth](DYLIBS/FindMyBluetooth.md)
- [/System/Library/PrivateFrameworks/FindMyCore.framework/FindMyCore](DYLIBS/FindMyCore.md)
- [/System/Library/PrivateFrameworks/FindMyDaemonSupport.framework/FindMyDaemonSupport](DYLIBS/FindMyDaemonSupport.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/FindMyDevice](DYLIBS/FindMyDevice.md)
- [/System/Library/PrivateFrameworks/FindMyLocate.framework/FindMyLocate](DYLIBS/FindMyLocate.md)
- [/System/Library/PrivateFrameworks/FindMyMessaging.framework/FindMyMessaging](DYLIBS/FindMyMessaging.md)
- [/System/Library/PrivateFrameworks/FindMyUICore.framework/FindMyUICore](DYLIBS/FindMyUICore.md)
- [/System/Library/PrivateFrameworks/FitnessAppRoot.framework/FitnessAppRoot](DYLIBS/FitnessAppRoot.md)
- [/System/Library/PrivateFrameworks/FitnessAsset.framework/FitnessAsset](DYLIBS/FitnessAsset.md)
- [/System/Library/PrivateFrameworks/FitnessAwards.framework/FitnessAwards](DYLIBS/FitnessAwards.md)
- [/System/Library/PrivateFrameworks/FitnessCanvasUI.framework/FitnessCanvasUI](DYLIBS/FitnessCanvasUI.md)
- [/System/Library/PrivateFrameworks/FitnessCoaching.framework/FitnessCoaching](DYLIBS/FitnessCoaching.md)
- [/System/Library/PrivateFrameworks/FitnessCoachingServices.framework/FitnessCoachingServices](DYLIBS/FitnessCoachingServices.md)
- [/System/Library/PrivateFrameworks/FitnessFiltering.framework/FitnessFiltering](DYLIBS/FitnessFiltering.md)
- [/System/Library/PrivateFrameworks/FitnessProductDetail.framework/FitnessProductDetail](DYLIBS/FitnessProductDetail.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/libFontParser.dylib](DYLIBS/libFontParser.dylib.md)
- [/System/Library/PrivateFrameworks/FoundInAppsPlugins.framework/FoundInAppsPlugins](DYLIBS/FoundInAppsPlugins.md)
- [/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/libGPUCompilerImpl.dylib](DYLIBS/libGPUCompilerImpl.dylib.md)
- [/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/libGPUCompilerImplLazy.dylib](DYLIBS/libGPUCompilerImplLazy.dylib.md)
- [/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/GenerativeAssistantActions](DYLIBS/GenerativeAssistantActions.md)
- [/System/Library/PrivateFrameworks/GenerativeAssistantSettings.framework/GenerativeAssistantSettings](DYLIBS/GenerativeAssistantSettings.md)
- [/System/Library/PrivateFrameworks/GenerativeExperiences.framework/GenerativeExperiences](DYLIBS/GenerativeExperiences.md)
- [/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/GenerativeExperiencesRuntime](DYLIBS/GenerativeExperiencesRuntime.md)
- [/System/Library/PrivateFrameworks/GenerativeExperiencesUI.framework/GenerativeExperiencesUI](DYLIBS/GenerativeExperiencesUI.md)
- [/System/Library/PrivateFrameworks/GenerativeFunctionsFoundation.framework/GenerativeFunctionsFoundation](DYLIBS/GenerativeFunctionsFoundation.md)
- [/System/Library/PrivateFrameworks/GenerativeFunctionsInstrumentation.framework/GenerativeFunctionsInstrumentation](DYLIBS/GenerativeFunctionsInstrumentation.md)
- [/System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels](DYLIBS/GenerativeModels.md)
- [/System/Library/PrivateFrameworks/GenerativeModelsFoundation.framework/GenerativeModelsFoundation](DYLIBS/GenerativeModelsFoundation.md)
- [/System/Library/PrivateFrameworks/GeoServices.framework/GeoServices](DYLIBS/GeoServices.md)
- [/System/Library/PrivateFrameworks/HMFoundation.framework/HMFoundation](DYLIBS/HMFoundation.md)
- [/System/Library/PrivateFrameworks/Hands.framework/Hands](DYLIBS/Hands.md)
- [/System/Library/PrivateFrameworks/HealthBalanceDaemon.framework/HealthBalanceDaemon](DYLIBS/HealthBalanceDaemon.md)
- [/System/Library/PrivateFrameworks/HealthBalanceUI.framework/HealthBalanceUI](DYLIBS/HealthBalanceUI.md)
- [/System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon](DYLIBS/HealthDaemon.md)
- [/System/Library/PrivateFrameworks/HealthExperienceUI.framework/HealthExperienceUI](DYLIBS/HealthExperienceUI.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsUI.framework/HealthMedicationsUI](DYLIBS/HealthMedicationsUI.md)
- [/System/Library/PrivateFrameworks/HealthMenstrualCyclesDaemon.framework/HealthMenstrualCyclesDaemon](DYLIBS/HealthMenstrualCyclesDaemon.md)
- [/System/Library/PrivateFrameworks/HealthPlatformCore.framework/HealthPlatformCore](DYLIBS/HealthPlatformCore.md)
- [/System/Library/PrivateFrameworks/HealthPluginHost.framework/HealthPluginHost](DYLIBS/HealthPluginHost.md)
- [/System/Library/PrivateFrameworks/HealthRecordsDaemon.framework/HealthRecordsDaemon](DYLIBS/HealthRecordsDaemon.md)
- [/System/Library/PrivateFrameworks/HealthRecordsExtraction.framework/HealthRecordsExtraction](DYLIBS/HealthRecordsExtraction.md)
- [/System/Library/PrivateFrameworks/HealthRecordsUI.framework/HealthRecordsUI](DYLIBS/HealthRecordsUI.md)
- [/System/Library/PrivateFrameworks/HealthVisualization.framework/HealthVisualization](DYLIBS/HealthVisualization.md)
- [/System/Library/PrivateFrameworks/HearingTestUI.framework/HearingTestUI](DYLIBS/HearingTestUI.md)
- [/System/Library/PrivateFrameworks/Home.framework/Home](DYLIBS/Home.md)
- [/System/Library/PrivateFrameworks/HomeAccessoryControlUI.framework/HomeAccessoryControlUI](DYLIBS/HomeAccessoryControlUI.md)
- [/System/Library/PrivateFrameworks/HomeAppIntents.framework/HomeAppIntents](DYLIBS/HomeAppIntents.md)
- [/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/HomeAutomationInternal](DYLIBS/HomeAutomationInternal.md)
- [/System/Library/PrivateFrameworks/HomeAutomationUIFramework.framework/HomeAutomationUIFramework](DYLIBS/HomeAutomationUIFramework.md)
- [/System/Library/PrivateFrameworks/HomeDataModel.framework/HomeDataModel](DYLIBS/HomeDataModel.md)
- [/System/Library/PrivateFrameworks/HomeEnergyDaemon.framework/HomeEnergyDaemon](DYLIBS/HomeEnergyDaemon.md)
- [/System/Library/PrivateFrameworks/HomeEnergyUI.framework/HomeEnergyUI](DYLIBS/HomeEnergyUI.md)
- [/System/Library/PrivateFrameworks/HomeKitCore.framework/HomeKitCore](DYLIBS/HomeKitCore.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemon.framework/HomeKitDaemon](DYLIBS/HomeKitDaemon.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemonLegacy.framework/HomeKitDaemonLegacy](DYLIBS/HomeKitDaemonLegacy.md)
- [/System/Library/PrivateFrameworks/HomeKitEvents.framework/HomeKitEvents](DYLIBS/HomeKitEvents.md)
- [/System/Library/PrivateFrameworks/HomeKitMatter.framework/HomeKitMatter](DYLIBS/HomeKitMatter.md)
- [/System/Library/PrivateFrameworks/HomeKitMetrics.framework/HomeKitMetrics](DYLIBS/HomeKitMetrics.md)
- [/System/Library/PrivateFrameworks/HomePodSettings.framework/HomePodSettings](DYLIBS/HomePodSettings.md)
- [/System/Library/PrivateFrameworks/HomeUI.framework/HomeUI](DYLIBS/HomeUI.md)
- [/System/Library/PrivateFrameworks/HomeUI2.framework/HomeUI2](DYLIBS/HomeUI2.md)
- [/System/Library/PrivateFrameworks/HomeUtilityServices.framework/HomeUtilityServices](DYLIBS/HomeUtilityServices.md)
- [/System/Library/PrivateFrameworks/HoverTextUI.framework/HoverTextUI](DYLIBS/HoverTextUI.md)
- [/System/Library/PrivateFrameworks/IDS.framework/IDS](DYLIBS/IDS.md)
- [/System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation](DYLIBS/IDSFoundation.md)
- [/System/Library/PrivateFrameworks/IMCore.framework/IMCore](DYLIBS/IMCore.md)
- [/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence](DYLIBS/IMDPersistence.md)
- [/System/Library/PrivateFrameworks/IMDaemonCore.framework/IMDaemonCore](DYLIBS/IMDaemonCore.md)
- [/System/Library/PrivateFrameworks/IMSharedUtilities.framework/IMSharedUtilities](DYLIBS/IMSharedUtilities.md)
- [/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU](DYLIBS/IOGPU.md)
- [/System/Library/PrivateFrameworks/IPTelephony.framework/Support/libIPTelephony.dylib](DYLIBS/libIPTelephony.dylib.md)
- [/System/Library/PrivateFrameworks/ISPExclaveKitServices.framework/ISPExclaveKitServices](DYLIBS/ISPExclaveKitServices.md)
- [/System/Library/PrivateFrameworks/ITMLKit.framework/ITMLKit](DYLIBS/ITMLKit.md)
- [/System/Library/PrivateFrameworks/InputAccessoriesSettings.framework/InputAccessoriesSettings](DYLIBS/InputAccessoriesSettings.md)
- [/System/Library/PrivateFrameworks/InputAnalytics.framework/InputAnalytics](DYLIBS/InputAnalytics.md)
- [/System/Library/PrivateFrameworks/InputAnalyticsServer.framework/InputAnalyticsServer](DYLIBS/InputAnalyticsServer.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlow.framework/IntelligenceFlow](DYLIBS/IntelligenceFlow.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowContext.framework/IntelligenceFlowContext](DYLIBS/IntelligenceFlowContext.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowContextRuntime.framework/IntelligenceFlowContextRuntime](DYLIBS/IntelligenceFlowContextRuntime.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/IntelligenceFlowPlannerRuntime](DYLIBS/IntelligenceFlowPlannerRuntime.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/IntelligenceFlowRuntime](DYLIBS/IntelligenceFlowRuntime.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatform.framework/IntelligencePlatform](DYLIBS/IntelligencePlatform.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/IntelligencePlatformCore](DYLIBS/IntelligencePlatformCore.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformLibrary.framework/IntelligencePlatformLibrary](DYLIBS/IntelligencePlatformLibrary.md)
- [/System/Library/PrivateFrameworks/IsolatedCoreAudioClient.framework/IsolatedCoreAudioClient](DYLIBS/IsolatedCoreAudioClient.md)
- [/System/Library/PrivateFrameworks/KnowledgeGraphKit.framework/KnowledgeGraphKit](DYLIBS/KnowledgeGraphKit.md)
- [/System/Library/PrivateFrameworks/KnowledgeMonitor.framework/KnowledgeMonitor](DYLIBS/KnowledgeMonitor.md)
- [/System/Library/PrivateFrameworks/LighthouseServicesAnalyticsFramework.framework/LighthouseServicesAnalyticsFramework](DYLIBS/LighthouseServicesAnalyticsFramework.md)
- [/System/Library/PrivateFrameworks/LimitAdTracking.framework/LimitAdTracking](DYLIBS/LimitAdTracking.md)
- [/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore](DYLIBS/LocalAuthenticationCore.md)
- [/System/Library/PrivateFrameworks/LocationAccessStore.framework/LocationAccessStore](DYLIBS/LocationAccessStore.md)
- [/System/Library/PrivateFrameworks/LocationSupport.framework/LocationSupport](DYLIBS/LocationSupport.md)
- [/System/Library/PrivateFrameworks/MFAAuthentication.framework/MFAAuthentication](DYLIBS/MFAAuthentication.md)
- [/System/Library/PrivateFrameworks/MIME.framework/MIME](DYLIBS/MIME.md)
- [/System/Library/PrivateFrameworks/MailUI.framework/MailUI](DYLIBS/MailUI.md)
- [/System/Library/PrivateFrameworks/ManagedAppsCore.framework/ManagedAppsCore](DYLIBS/ManagedAppsCore.md)
- [/System/Library/PrivateFrameworks/MatterPlugin.framework/MatterPlugin](DYLIBS/MatterPlugin.md)
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/MediaAnalysis](DYLIBS/MediaAnalysis.md)
- [/System/Library/PrivateFrameworks/MediaControls.framework/MediaControls](DYLIBS/MediaControls.md)
- [/System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience](DYLIBS/MediaExperience.md)
- [/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore](DYLIBS/MediaPlaybackCore.md)
- [/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote](DYLIBS/MediaRemote.md)
- [/System/Library/PrivateFrameworks/MentalHealthUI.framework/MentalHealthUI](DYLIBS/MentalHealthUI.md)
- [/System/Library/PrivateFrameworks/Message.framework/Message](DYLIBS/Message.md)
- [/System/Library/PrivateFrameworks/MessagesCloudSync.framework/MessagesCloudSync](DYLIBS/MessagesCloudSync.md)
- [/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools](DYLIBS/MetalTools.md)
- [/System/Library/PrivateFrameworks/MetricsFramework.framework/MetricsFramework](DYLIBS/MetricsFramework.md)
- [/System/Library/PrivateFrameworks/MigrationKit.framework/MigrationKit](DYLIBS/MigrationKit.md)
- [/System/Library/PrivateFrameworks/MobileInBoxUpdate.framework/MobileInBoxUpdate](DYLIBS/MobileInBoxUpdate.md)
- [/System/Library/PrivateFrameworks/MobileMailUI.framework/MobileMailUI](DYLIBS/MobileMailUI.md)
- [/System/Library/PrivateFrameworks/MobileMulticastTransfer.framework/MobileMulticastTransfer](DYLIBS/MobileMulticastTransfer.md)
- [/System/Library/PrivateFrameworks/MobileSafari.framework/MobileSafari](DYLIBS/MobileSafari.md)
- [/System/Library/PrivateFrameworks/MobileSafariUI.framework/MobileSafariUI](DYLIBS/MobileSafariUI.md)
- [/System/Library/PrivateFrameworks/MobileSpotlightIndex.framework/MobileSpotlightIndex](DYLIBS/MobileSpotlightIndex.md)
- [/System/Library/PrivateFrameworks/MobileStoreDemoSetupUI.framework/MobileStoreDemoSetupUI](DYLIBS/MobileStoreDemoSetupUI.md)
- [/System/Library/PrivateFrameworks/ModelCatalog.framework/ModelCatalog](DYLIBS/ModelCatalog.md)
- [/System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/ModelCatalogRuntime](DYLIBS/ModelCatalogRuntime.md)
- [/System/Library/PrivateFrameworks/ModelManagerServices.framework/ModelManagerServices](DYLIBS/ModelManagerServices.md)
- [/System/Library/PrivateFrameworks/Morpheus.framework/Morpheus](DYLIBS/Morpheus.md)
- [/System/Library/PrivateFrameworks/MotionSensorLogging.framework/MotionSensorLogging](DYLIBS/MotionSensorLogging.md)
- [/System/Library/PrivateFrameworks/MusicKitInternal.framework/MusicKitInternal](DYLIBS/MusicKitInternal.md)
- [/System/Library/PrivateFrameworks/MusicLibrary.framework/MusicLibrary](DYLIBS/MusicLibrary.md)
- [/System/Library/PrivateFrameworks/MusicUI.framework/MusicUI](DYLIBS/MusicUI.md)
- [/System/Library/PrivateFrameworks/NDOAPI.framework/NDOAPI](DYLIBS/NDOAPI.md)
- [/System/Library/PrivateFrameworks/NDOUI.framework/NDOUI](DYLIBS/NDOUI.md)
- [/System/Library/PrivateFrameworks/NanoPassKit.framework/NanoPassKit](DYLIBS/NanoPassKit.md)
- [/System/Library/PrivateFrameworks/NanoTimeKitCompanion.framework/NanoTimeKitCompanion](DYLIBS/NanoTimeKitCompanion.md)
- [/System/Library/PrivateFrameworks/NearField.framework/NearField](DYLIBS/NearField.md)
- [/System/Library/PrivateFrameworks/NetworkInfo.framework/NetworkInfo](DYLIBS/NetworkInfo.md)
- [/System/Library/PrivateFrameworks/NeutrinoCore.framework/NeutrinoCore](DYLIBS/NeutrinoCore.md)
- [/System/Library/PrivateFrameworks/NewDeviceOutreachUI.framework/NewDeviceOutreachUI](DYLIBS/NewDeviceOutreachUI.md)
- [/System/Library/PrivateFrameworks/NexusDaemon.framework/NexusDaemon](DYLIBS/NexusDaemon.md)
- [/System/Library/PrivateFrameworks/NightingaleTraining.framework/NightingaleTraining](DYLIBS/NightingaleTraining.md)
- [/System/Library/PrivateFrameworks/NotesEditor.framework/NotesEditor](DYLIBS/NotesEditor.md)
- [/System/Library/PrivateFrameworks/NotesShared.framework/NotesShared](DYLIBS/NotesShared.md)
- [/System/Library/PrivateFrameworks/NotesSupport.framework/NotesSupport](DYLIBS/NotesSupport.md)
- [/System/Library/PrivateFrameworks/NotesUI.framework/NotesUI](DYLIBS/NotesUI.md)
- [/System/Library/PrivateFrameworks/ODDIFramework.framework/ODDIFramework](DYLIBS/ODDIFramework.md)
- [/System/Library/PrivateFrameworks/OSEligibility.framework/OSEligibility](DYLIBS/OSEligibility.md)
- [/System/Library/PrivateFrameworks/OfficeImport.framework/OfficeImport](DYLIBS/OfficeImport.md)
- [/System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit](DYLIBS/OnBoardingKit.md)
- [/System/Library/PrivateFrameworks/OnDeviceStorage.framework/OnDeviceStorage](DYLIBS/OnDeviceStorage.md)
- [/System/Library/PrivateFrameworks/OnDeviceStorageCore.framework/OnDeviceStorageCore](DYLIBS/OnDeviceStorageCore.md)
- [/System/Library/PrivateFrameworks/OnDeviceStorageInternal.framework/OnDeviceStorageInternal](DYLIBS/OnDeviceStorageInternal.md)
- [/System/Library/PrivateFrameworks/PaperBoardUI.framework/PaperBoardUI](DYLIBS/PaperBoardUI.md)
- [/System/Library/PrivateFrameworks/PaperKit.framework/PaperKit](DYLIBS/PaperKit.md)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore](DYLIBS/PassKitCore.md)
- [/System/Library/PrivateFrameworks/PassKitUI.framework/PassKitUI](DYLIBS/PassKitUI.md)
- [/System/Library/PrivateFrameworks/PasswordManagerUI.framework/PasswordManagerUI](DYLIBS/PasswordManagerUI.md)
- [/System/Library/PrivateFrameworks/PegasusConfiguration.framework/PegasusConfiguration](DYLIBS/PegasusConfiguration.md)
- [/System/Library/PrivateFrameworks/PeopleSuggester.framework/PeopleSuggester](DYLIBS/PeopleSuggester.md)
- [/System/Library/PrivateFrameworks/PerfPowerServicesMetadata.framework/PerfPowerServicesMetadata](DYLIBS/PerfPowerServicesMetadata.md)
- [/System/Library/PrivateFrameworks/PhotoAnalysis.framework/PhotoAnalysis](DYLIBS/PhotoAnalysis.md)
- [/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/PhotoLibraryServices](DYLIBS/PhotoLibraryServices.md)
- [/System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/PhotoLibraryServicesCore](DYLIBS/PhotoLibraryServicesCore.md)
- [/System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats](DYLIBS/PhotosFormats.md)
- [/System/Library/PrivateFrameworks/PhotosGraph.framework/PhotosGraph](DYLIBS/PhotosGraph.md)
- [/System/Library/PrivateFrameworks/PhotosIntelligence.framework/PhotosIntelligence](DYLIBS/PhotosIntelligence.md)
- [/System/Library/PrivateFrameworks/PhotosSwiftUICore.framework/PhotosSwiftUICore](DYLIBS/PhotosSwiftUICore.md)
- [/System/Library/PrivateFrameworks/PhotosUICore.framework/PhotosUICore](DYLIBS/PhotosUICore.md)
- [/System/Library/PrivateFrameworks/PhotosUIEdit.framework/PhotosUIEdit](DYLIBS/PhotosUIEdit.md)
- [/System/Library/PrivateFrameworks/PhotosUIFoundation.framework/PhotosUIFoundation](DYLIBS/PhotosUIFoundation.md)
- [/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PhotosUIPrivate](DYLIBS/PhotosUIPrivate.md)
- [/System/Library/PrivateFrameworks/PlatformSSO.framework/PlatformSSO](DYLIBS/PlatformSSO.md)
- [/System/Library/PrivateFrameworks/PodcastsFoundation.framework/PodcastsFoundation](DYLIBS/PodcastsFoundation.md)
- [/System/Library/PrivateFrameworks/PodcastsKit.framework/PodcastsKit](DYLIBS/PodcastsKit.md)
- [/System/Library/PrivateFrameworks/PodcastsUI.framework/PodcastsUI](DYLIBS/PodcastsUI.md)
- [/System/Library/PrivateFrameworks/Portrait.framework/Portrait](DYLIBS/Portrait.md)
- [/System/Library/PrivateFrameworks/PosterBoard.framework/PosterBoard](DYLIBS/PosterBoard.md)
- [/System/Library/PrivateFrameworks/PosterBoardServices.framework/PosterBoardServices](DYLIBS/PosterBoardServices.md)
- [/System/Library/PrivateFrameworks/PosterBoardUIServices.framework/PosterBoardUIServices](DYLIBS/PosterBoardUIServices.md)
- [/System/Library/PrivateFrameworks/PosterFoundation.framework/PosterFoundation](DYLIBS/PosterFoundation.md)
- [/System/Library/PrivateFrameworks/PosterKit.framework/PosterKit](DYLIBS/PosterKit.md)
- [/System/Library/PrivateFrameworks/PosterPlatformSupport.framework/PosterPlatformSupport](DYLIBS/PosterPlatformSupport.md)
- [/System/Library/PrivateFrameworks/PosterUIFoundation.framework/PosterUIFoundation](DYLIBS/PosterUIFoundation.md)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore](DYLIBS/PowerlogCore.md)
- [/System/Library/PrivateFrameworks/PowerlogFullOperators.framework/PowerlogFullOperators](DYLIBS/PowerlogFullOperators.md)
- [/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators](DYLIBS/PowerlogHelperdOperators.md)
- [/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators](DYLIBS/PowerlogLiteOperators.md)
- [/System/Library/PrivateFrameworks/PrintKit.framework/PrintKit](DYLIBS/PrintKit.md)
- [/System/Library/PrivateFrameworks/PrivateCloudCompute.framework/PrivateCloudCompute](DYLIBS/PrivateCloudCompute.md)
- [/System/Library/PrivateFrameworks/ProactiveDaemonSupport.framework/ProactiveDaemonSupport](DYLIBS/ProactiveDaemonSupport.md)
- [/System/Library/PrivateFrameworks/ProactiveExperiments.framework/ProactiveExperiments](DYLIBS/ProactiveExperiments.md)
- [/System/Library/PrivateFrameworks/ProactiveExperimentsInternals.framework/ProactiveExperimentsInternals](DYLIBS/ProactiveExperimentsInternals.md)
- [/System/Library/PrivateFrameworks/ProactiveHarvesting.framework/ProactiveHarvesting](DYLIBS/ProactiveHarvesting.md)
- [/System/Library/PrivateFrameworks/ProactiveInputPredictionsInternals.framework/ProactiveInputPredictionsInternals](DYLIBS/ProactiveInputPredictionsInternals.md)
- [/System/Library/PrivateFrameworks/ProactiveML.framework/ProactiveML](DYLIBS/ProactiveML.md)
- [/System/Library/PrivateFrameworks/ProactiveSummarization.framework/ProactiveSummarization](DYLIBS/ProactiveSummarization.md)
- [/System/Library/PrivateFrameworks/ProactiveSummarizationClient.framework/ProactiveSummarizationClient](DYLIBS/ProactiveSummarizationClient.md)
- [/System/Library/PrivateFrameworks/PromotedContent.framework/PromotedContent](DYLIBS/PromotedContent.md)
- [/System/Library/PrivateFrameworks/PromotedContentUI.framework/PromotedContentUI](DYLIBS/PromotedContentUI.md)
- [/System/Library/PrivateFrameworks/ProximityControl.framework/ProximityControl](DYLIBS/ProximityControl.md)
- [/System/Library/PrivateFrameworks/RTTUtilities.framework/RTTUtilities](DYLIBS/RTTUtilities.md)
- [/System/Library/PrivateFrameworks/RapidResourceDelivery.framework/RapidResourceDelivery](DYLIBS/RapidResourceDelivery.md)
- [/System/Library/PrivateFrameworks/Rapport.framework/Rapport](DYLIBS/Rapport.md)
- [/System/Library/PrivateFrameworks/ReminderKitInternal.framework/ReminderKitInternal](DYLIBS/ReminderKitInternal.md)
- [/System/Library/PrivateFrameworks/RemindersUICore.framework/RemindersUICore](DYLIBS/RemindersUICore.md)
- [/System/Library/PrivateFrameworks/RequestDispatcherBridges.framework/RequestDispatcherBridges](DYLIBS/RequestDispatcherBridges.md)
- [/System/Library/PrivateFrameworks/SFSymbols.framework/SFSymbols](DYLIBS/SFSymbols.md)
- [/System/Library/PrivateFrameworks/SILManager.framework/SILManager](DYLIBS/SILManager.md)
- [/System/Library/PrivateFrameworks/SPOwner.framework/SPOwner](DYLIBS/SPOwner.md)
- [/System/Library/PrivateFrameworks/SafariShared.framework/SafariShared](DYLIBS/SafariShared.md)
- [/System/Library/PrivateFrameworks/SafariSharedUI.framework/SafariSharedUI](DYLIBS/SafariSharedUI.md)
- [/System/Library/PrivateFrameworks/Sage.framework/Sage](DYLIBS/Sage.md)
- [/System/Library/PrivateFrameworks/ScreenSharingKit.framework/ScreenSharingKit](DYLIBS/ScreenSharingKit.md)
- [/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore](DYLIBS/ScreenTimeCore.md)
- [/System/Library/PrivateFrameworks/ScreenTimeSettingsUI.framework/ScreenTimeSettingsUI](DYLIBS/ScreenTimeSettingsUI.md)
- [/System/Library/PrivateFrameworks/ScreenTimeUICore.framework/ScreenTimeUICore](DYLIBS/ScreenTimeUICore.md)
- [/System/Library/PrivateFrameworks/ScreenshotServices.framework/ScreenshotServices](DYLIBS/ScreenshotServices.md)
- [/System/Library/PrivateFrameworks/Search.framework/Search](DYLIBS/Search.md)
- [/System/Library/PrivateFrameworks/SearchAds.framework/SearchAds](DYLIBS/SearchAds.md)
- [/System/Library/PrivateFrameworks/SearchOnDeviceAnalytics.framework/SearchOnDeviceAnalytics](DYLIBS/SearchOnDeviceAnalytics.md)
- [/System/Library/PrivateFrameworks/SensitiveContentAnalysisML.framework/SensitiveContentAnalysisML](DYLIBS/SensitiveContentAnalysisML.md)
- [/System/Library/PrivateFrameworks/SensitiveContentAnalysisUI.framework/SensitiveContentAnalysisUI](DYLIBS/SensitiveContentAnalysisUI.md)
- [/System/Library/PrivateFrameworks/SensorKitWriting.framework/SensorKitWriting](DYLIBS/SensorKitWriting.md)
- [/System/Library/PrivateFrameworks/SeymourClient.framework/SeymourClient](DYLIBS/SeymourClient.md)
- [/System/Library/PrivateFrameworks/SeymourClientServices.framework/SeymourClientServices](DYLIBS/SeymourClientServices.md)
- [/System/Library/PrivateFrameworks/SeymourCore.framework/SeymourCore](DYLIBS/SeymourCore.md)
- [/System/Library/PrivateFrameworks/SeymourMedia.framework/SeymourMedia](DYLIBS/SeymourMedia.md)
- [/System/Library/PrivateFrameworks/SeymourServices.framework/SeymourServices](DYLIBS/SeymourServices.md)
- [/System/Library/PrivateFrameworks/SeymourServicesCore.framework/SeymourServicesCore](DYLIBS/SeymourServicesCore.md)
- [/System/Library/PrivateFrameworks/SeymourUI.framework/SeymourUI](DYLIBS/SeymourUI.md)
- [/System/Library/PrivateFrameworks/ShareSheet.framework/ShareSheet](DYLIBS/ShareSheet.md)
- [/System/Library/PrivateFrameworks/Sharing.framework/Sharing](DYLIBS/Sharing.md)
- [/System/Library/PrivateFrameworks/ShazamCore.framework/ShazamCore](DYLIBS/ShazamCore.md)
- [/System/Library/PrivateFrameworks/ShazamEvents.framework/ShazamEvents](DYLIBS/ShazamEvents.md)
- [/System/Library/PrivateFrameworks/ShazamKitUI.framework/ShazamKitUI](DYLIBS/ShazamKitUI.md)
- [/System/Library/PrivateFrameworks/ShellSceneKit.framework/ShellSceneKit](DYLIBS/ShellSceneKit.md)
- [/System/Library/PrivateFrameworks/SiriActivation.framework/SiriActivation](DYLIBS/SiriActivation.md)
- [/System/Library/PrivateFrameworks/SiriAnalytics.framework/SiriAnalytics](DYLIBS/SiriAnalytics.md)
- [/System/Library/PrivateFrameworks/SiriAppLaunchIntents.framework/SiriAppLaunchIntents](DYLIBS/SiriAppLaunchIntents.md)
- [/System/Library/PrivateFrameworks/SiriAppLaunchUIFramework.framework/SiriAppLaunchUIFramework](DYLIBS/SiriAppLaunchUIFramework.md)
- [/System/Library/PrivateFrameworks/SiriAudioInternal.framework/SiriAudioInternal](DYLIBS/SiriAudioInternal.md)
- [/System/Library/PrivateFrameworks/SiriAudioSupport.framework/SiriAudioSupport](DYLIBS/SiriAudioSupport.md)
- [/System/Library/PrivateFrameworks/SiriAutoComplete.framework/SiriAutoComplete](DYLIBS/SiriAutoComplete.md)
- [/System/Library/PrivateFrameworks/SiriCalendarIntents.framework/SiriCalendarIntents](DYLIBS/SiriCalendarIntents.md)
- [/System/Library/PrivateFrameworks/SiriCalendarUI.framework/SiriCalendarUI](DYLIBS/SiriCalendarUI.md)
- [/System/Library/PrivateFrameworks/SiriCam.framework/SiriCam](DYLIBS/SiriCam.md)
- [/System/Library/PrivateFrameworks/SiriContactsIntents.framework/SiriContactsIntents](DYLIBS/SiriContactsIntents.md)
- [/System/Library/PrivateFrameworks/SiriContactsUI.framework/SiriContactsUI](DYLIBS/SiriContactsUI.md)
- [/System/Library/PrivateFrameworks/SiriCrossDeviceArbitration.framework/SiriCrossDeviceArbitration](DYLIBS/SiriCrossDeviceArbitration.md)
- [/System/Library/PrivateFrameworks/SiriFlowEnvironment.framework/SiriFlowEnvironment](DYLIBS/SiriFlowEnvironment.md)
- [/System/Library/PrivateFrameworks/SiriGestureBridge.framework/SiriGestureBridge](DYLIBS/SiriGestureBridge.md)
- [/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/SiriIdentityInternal](DYLIBS/SiriIdentityInternal.md)
- [/System/Library/PrivateFrameworks/SiriInference.framework/SiriInference](DYLIBS/SiriInference.md)
- [/System/Library/PrivateFrameworks/SiriInformationSearch.framework/SiriInformationSearch](DYLIBS/SiriInformationSearch.md)
- [/System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation](DYLIBS/SiriInstrumentation.md)
- [/System/Library/PrivateFrameworks/SiriKitFlow.framework/SiriKitFlow](DYLIBS/SiriKitFlow.md)
- [/System/Library/PrivateFrameworks/SiriKitRuntime.framework/SiriKitRuntime](DYLIBS/SiriKitRuntime.md)
- [/System/Library/PrivateFrameworks/SiriMailInternal.framework/SiriMailInternal](DYLIBS/SiriMailInternal.md)
- [/System/Library/PrivateFrameworks/SiriMessageBus.framework/SiriMessageBus](DYLIBS/SiriMessageBus.md)
- [/System/Library/PrivateFrameworks/SiriMessageTypes.framework/SiriMessageTypes](DYLIBS/SiriMessageTypes.md)
- [/System/Library/PrivateFrameworks/SiriMessagesFlow.framework/SiriMessagesFlow](DYLIBS/SiriMessagesFlow.md)
- [/System/Library/PrivateFrameworks/SiriMessagesUI.framework/SiriMessagesUI](DYLIBS/SiriMessagesUI.md)
- [/System/Library/PrivateFrameworks/SiriNetwork.framework/SiriNetwork](DYLIBS/SiriNetwork.md)
- [/System/Library/PrivateFrameworks/SiriNotebook.framework/SiriNotebook](DYLIBS/SiriNotebook.md)
- [/System/Library/PrivateFrameworks/SiriNotebookUI.framework/SiriNotebookUI](DYLIBS/SiriNotebookUI.md)
- [/System/Library/PrivateFrameworks/SiriNotificationsIntents.framework/SiriNotificationsIntents](DYLIBS/SiriNotificationsIntents.md)
- [/System/Library/PrivateFrameworks/SiriOntology.framework/SiriOntology](DYLIBS/SiriOntology.md)
- [/System/Library/PrivateFrameworks/SiriOntologyProtobuf.framework/SiriOntologyProtobuf](DYLIBS/SiriOntologyProtobuf.md)
- [/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/SiriPlaybackControlIntents](DYLIBS/SiriPlaybackControlIntents.md)
- [/System/Library/PrivateFrameworks/SiriPlaybackControlSupport.framework/SiriPlaybackControlSupport](DYLIBS/SiriPlaybackControlSupport.md)
- [/System/Library/PrivateFrameworks/SiriRemembers.framework/SiriRemembers](DYLIBS/SiriRemembers.md)
- [/System/Library/PrivateFrameworks/SiriRequestDispatcher.framework/SiriRequestDispatcher](DYLIBS/SiriRequestDispatcher.md)
- [/System/Library/PrivateFrameworks/SiriSettingsIntents.framework/SiriSettingsIntents](DYLIBS/SiriSettingsIntents.md)
- [/System/Library/PrivateFrameworks/SiriSetup.framework/SiriSetup](DYLIBS/SiriSetup.md)
- [/System/Library/PrivateFrameworks/SiriSharedUI.framework/SiriSharedUI](DYLIBS/SiriSharedUI.md)
- [/System/Library/PrivateFrameworks/SiriSignals.framework/SiriSignals](DYLIBS/SiriSignals.md)
- [/System/Library/PrivateFrameworks/SiriSuggestions.framework/SiriSuggestions](DYLIBS/SiriSuggestions.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsAPI.framework/SiriSuggestionsAPI](DYLIBS/SiriSuggestionsAPI.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/SiriSuggestionsBaseModel](DYLIBS/SiriSuggestionsBaseModel.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsIntelligence.framework/SiriSuggestionsIntelligence](DYLIBS/SiriSuggestionsIntelligence.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsKit.framework/SiriSuggestionsKit](DYLIBS/SiriSuggestionsKit.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsSupport.framework/SiriSuggestionsSupport](DYLIBS/SiriSuggestionsSupport.md)
- [/System/Library/PrivateFrameworks/SiriTTS.framework/SiriTTS](DYLIBS/SiriTTS.md)
- [/System/Library/PrivateFrameworks/SiriTTSService.framework/SiriTTSService](DYLIBS/SiriTTSService.md)
- [/System/Library/PrivateFrameworks/SiriTimeInternal.framework/SiriTimeInternal](DYLIBS/SiriTimeInternal.md)
- [/System/Library/PrivateFrameworks/SiriTimeTimerInternal.framework/SiriTimeTimerInternal](DYLIBS/SiriTimeTimerInternal.md)
- [/System/Library/PrivateFrameworks/SiriTranslationIntents.framework/SiriTranslationIntents](DYLIBS/SiriTranslationIntents.md)
- [/System/Library/PrivateFrameworks/SiriUIActivation.framework/SiriUIActivation](DYLIBS/SiriUIActivation.md)
- [/System/Library/PrivateFrameworks/SiriUIFoundation.framework/SiriUIFoundation](DYLIBS/SiriUIFoundation.md)
- [/System/Library/PrivateFrameworks/SleepHealthUI.framework/SleepHealthUI](DYLIBS/SleepHealthUI.md)
- [/System/Library/PrivateFrameworks/SleepWidgetUI.framework/SleepWidgetUI](DYLIBS/SleepWidgetUI.md)
- [/System/Library/PrivateFrameworks/SnippetKit.framework/SnippetKit](DYLIBS/SnippetKit.md)
- [/System/Library/PrivateFrameworks/SnippetUI.framework/SnippetUI](DYLIBS/SnippetUI.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateController.framework/SoftwareUpdateController](DYLIBS/SoftwareUpdateController.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/SoftwareUpdateCore](DYLIBS/SoftwareUpdateCore.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices](DYLIBS/SoftwareUpdateServices.md)
- [/System/Library/PrivateFrameworks/SonicFoundation.framework/SonicFoundation](DYLIBS/SonicFoundation.md)
- [/System/Library/PrivateFrameworks/SonicKit.framework/SonicKit](DYLIBS/SonicKit.md)
- [/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition](DYLIBS/SpeakerRecognition.md)
- [/System/Library/PrivateFrameworks/SpeechRecognitionCommandAndControl.framework/SpeechRecognitionCommandAndControl](DYLIBS/SpeechRecognitionCommandAndControl.md)
- [/System/Library/PrivateFrameworks/Spotlight.framework/Spotlight](DYLIBS/Spotlight.md)
- [/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon](DYLIBS/SpotlightDaemon.md)
- [/System/Library/PrivateFrameworks/SpotlightEmbedding.framework/SpotlightEmbedding](DYLIBS/SpotlightEmbedding.md)
- [/System/Library/PrivateFrameworks/SpotlightKnowledge.framework/SpotlightKnowledge](DYLIBS/SpotlightKnowledge.md)
- [/System/Library/PrivateFrameworks/SpotlightLinguistics.framework/SpotlightLinguistics](DYLIBS/SpotlightLinguistics.md)
- [/System/Library/PrivateFrameworks/SpotlightReceiver.framework/SpotlightReceiver](DYLIBS/SpotlightReceiver.md)
- [/System/Library/PrivateFrameworks/SpotlightResources.framework/SpotlightResources](DYLIBS/SpotlightResources.md)
- [/System/Library/PrivateFrameworks/SpotlightServices.framework/SpotlightServices](DYLIBS/SpotlightServices.md)
- [/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard](DYLIBS/SpringBoard.md)
- [/System/Library/PrivateFrameworks/StatusKitAgentCore.framework/StatusKitAgentCore](DYLIBS/StatusKitAgentCore.md)
- [/System/Library/PrivateFrameworks/Stickers.framework/Stickers](DYLIBS/Stickers.md)
- [/System/Library/PrivateFrameworks/StorageKit.framework/StorageKit](DYLIBS/StorageKit.md)
- [/System/Library/PrivateFrameworks/SuggestionsSpotlightMetrics.framework/SuggestionsSpotlightMetrics](DYLIBS/SuggestionsSpotlightMetrics.md)
- [/System/Library/PrivateFrameworks/SummarizationKit.framework/SummarizationKit](DYLIBS/SummarizationKit.md)
- [/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomEvaluator.framework/SymptomEvaluator](DYLIBS/SymptomEvaluator.md)
- [/System/Library/PrivateFrameworks/SyncedDefaultsDaemon.framework/SyncedDefaultsDaemon](DYLIBS/SyncedDefaultsDaemon.md)
- [/System/Library/PrivateFrameworks/SystemServiceMonitor.framework/SystemServiceMonitor](DYLIBS/SystemServiceMonitor.md)
- [/System/Library/PrivateFrameworks/SystemStatus.framework/SystemStatus](DYLIBS/SystemStatus.md)
- [/System/Library/PrivateFrameworks/SystemStatusServer.framework/SystemStatusServer](DYLIBS/SystemStatusServer.md)
- [/System/Library/PrivateFrameworks/SystemStatusUI.framework/SystemStatusUI](DYLIBS/SystemStatusUI.md)
- [/System/Library/PrivateFrameworks/SystemUIAnimationKit.framework/SystemUIAnimationKit](DYLIBS/SystemUIAnimationKit.md)
- [/System/Library/PrivateFrameworks/TCC.framework/TCC](DYLIBS/TCC.md)
- [/System/Library/PrivateFrameworks/TVPlayback.framework/TVPlayback](DYLIBS/TVPlayback.md)
- [/System/Library/PrivateFrameworks/TVRemoteUI.framework/TVRemoteUI](DYLIBS/TVRemoteUI.md)
- [/System/Library/PrivateFrameworks/TelephonyBlastDoorSupport.framework/TelephonyBlastDoorSupport](DYLIBS/TelephonyBlastDoorSupport.md)
- [/System/Library/PrivateFrameworks/TelephonyKit.framework/TelephonyKit](DYLIBS/TelephonyKit.md)
- [/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer](DYLIBS/TextComposer.md)
- [/System/Library/PrivateFrameworks/TextInput.framework/TextInput](DYLIBS/TextInput.md)
- [/System/Library/PrivateFrameworks/TextInputUI.framework/TextInputUI](DYLIBS/TextInputUI.md)
- [/System/Library/PrivateFrameworks/TextToSpeech.framework/TextToSpeech](DYLIBS/TextToSpeech.md)
- [/System/Library/PrivateFrameworks/TokenGenerationInference.framework/TokenGenerationInference](DYLIBS/TokenGenerationInference.md)
- [/System/Library/PrivateFrameworks/ToolKit.framework/ToolKit](DYLIBS/ToolKit.md)
- [/System/Library/PrivateFrameworks/TypistFramework.framework/TypistFramework](DYLIBS/TypistFramework.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore](DYLIBS/UIKitCore.md)
- [/System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework](DYLIBS/UnifiedAssetFramework.md)
- [/System/Library/PrivateFrameworks/UserNotificationsCore.framework/UserNotificationsCore](DYLIBS/UserNotificationsCore.md)
- [/System/Library/PrivateFrameworks/UserNotificationsKit.framework/UserNotificationsKit](DYLIBS/UserNotificationsKit.md)
- [/System/Library/PrivateFrameworks/UserNotificationsUIKit.framework/UserNotificationsUIKit](DYLIBS/UserNotificationsUIKit.md)
- [/System/Library/PrivateFrameworks/VectorKit.framework/VectorKit](DYLIBS/VectorKit.md)
- [/System/Library/PrivateFrameworks/VideosUI.framework/VideosUI](DYLIBS/VideosUI.md)
- [/System/Library/PrivateFrameworks/VisionCompanion.framework/VisionCompanion](DYLIBS/VisionCompanion.md)
- [/System/Library/PrivateFrameworks/VisualGeneration.framework/VisualGeneration](DYLIBS/VisualGeneration.md)
- [/System/Library/PrivateFrameworks/VisualPairing.framework/VisualPairing](DYLIBS/VisualPairing.md)
- [/System/Library/PrivateFrameworks/VoiceControl.framework/VoiceControl](DYLIBS/VoiceControl.md)
- [/System/Library/PrivateFrameworks/VoiceControlUI.framework/VoiceControlUI](DYLIBS/VoiceControlUI.md)
- [/System/Library/PrivateFrameworks/VoiceShortcutClient.framework/VoiceShortcutClient](DYLIBS/VoiceShortcutClient.md)
- [/System/Library/PrivateFrameworks/VoiceShortcuts.framework/VoiceShortcuts](DYLIBS/VoiceShortcuts.md)
- [/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger](DYLIBS/VoiceTrigger.md)
- [/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/VoiceTriggerUI](DYLIBS/VoiceTriggerUI.md)
- [/System/Library/PrivateFrameworks/WPDaemon.framework/WPDaemon](DYLIBS/WPDaemon.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/WatchFacesWallpaperSupport](DYLIBS/WatchFacesWallpaperSupport.md)
- [/System/Library/PrivateFrameworks/WatchListKit.framework/WatchListKit](DYLIBS/WatchListKit.md)
- [/System/Library/PrivateFrameworks/WebBookmarks.framework/WebBookmarks](DYLIBS/WebBookmarks.md)
- [/System/Library/PrivateFrameworks/WebBookmarksSwift.framework/WebBookmarksSwift](DYLIBS/WebBookmarksSwift.md)
- [/System/Library/PrivateFrameworks/WebCore.framework/Frameworks/libANGLE-shared.dylib](DYLIBS/libANGLE-shared.dylib.md)
- [/System/Library/PrivateFrameworks/WebCore.framework/Frameworks/libwebrtc.dylib](DYLIBS/libwebrtc.dylib.md)
- [/System/Library/PrivateFrameworks/WebCore.framework/WebCore](DYLIBS/WebCore.md)
- [/System/Library/PrivateFrameworks/WebGPU.framework/WebGPU](DYLIBS/WebGPU.md)
- [/System/Library/PrivateFrameworks/WebKitLegacy.framework/WebKitLegacy](DYLIBS/WebKitLegacy.md)
- [/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics](DYLIBS/WiFiAnalytics.md)
- [/System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI](DYLIBS/WiFiKitUI.md)
- [/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy](DYLIBS/WiFiPolicy.md)
- [/System/Library/PrivateFrameworks/WidgetRenderer.framework/WidgetRenderer](DYLIBS/WidgetRenderer.md)
- [/System/Library/PrivateFrameworks/WorkflowEditor.framework/WorkflowEditor](DYLIBS/WorkflowEditor.md)
- [/System/Library/PrivateFrameworks/WorkflowKit.framework/WorkflowKit](DYLIBS/WorkflowKit.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/WorkflowUI](DYLIBS/WorkflowUI.md)
- [/System/Library/PrivateFrameworks/WorkflowUICore.framework/WorkflowUICore](DYLIBS/WorkflowUICore.md)
- [/System/Library/PrivateFrameworks/WorkflowUIServices.framework/WorkflowUIServices](DYLIBS/WorkflowUIServices.md)
- [/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/WorkoutAnnouncements](DYLIBS/WorkoutAnnouncements.md)
- [/System/Library/PrivateFrameworks/WorkoutCore.framework/WorkoutCore](DYLIBS/WorkoutCore.md)
- [/System/Library/PrivateFrameworks/WorkoutUI.framework/WorkoutUI](DYLIBS/WorkoutUI.md)
- [/System/Library/PrivateFrameworks/XCTTargetBootstrap.framework/XCTTargetBootstrap](DYLIBS/XCTTargetBootstrap.md)
- [/System/Library/PrivateFrameworks/_MusicKitInternal_SwiftUI.framework/_MusicKitInternal_SwiftUI](DYLIBS/_MusicKitInternal_SwiftUI.md)
- [/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore](DYLIBS/iCloudDriveCore.md)
- [/System/Library/PrivateFrameworks/iCloudDriveService.framework/iCloudDriveService](DYLIBS/iCloudDriveService.md)
- [/System/Library/PrivateFrameworks/iCloudQuota.framework/iCloudQuota](DYLIBS/iCloudQuota.md)
- [/System/Library/PrivateFrameworks/iCloudQuotaUI.framework/iCloudQuotaUI](DYLIBS/iCloudQuotaUI.md)
- [/System/Library/PrivateFrameworks/iTunesCloud.framework/iTunesCloud](DYLIBS/iTunesCloud.md)
- [/System/Library/PrivateFrameworks/shared_cache_page_prewarming.framework/shared_cache_page_prewarming](DYLIBS/shared_cache_page_prewarming.md)
- [/System/Library/VideoDecoders/JPEGH1.videodecoder](DYLIBS/JPEGH1.videodecoder.md)
- [/System/Library/VideoEncoders/H264H9.videoencoder](DYLIBS/H264H9.videoencoder.md)
- [/System/Library/VideoEncoders/H9.videoencoder](DYLIBS/H9.videoencoder.md)
- [/System/Library/VideoEncoders/JPEGH1.videoencoder](DYLIBS/JPEGH1.videoencoder.md)
- [/System/Library/VideoProcessors/NRFV4.bundle/NRFV4](DYLIBS/NRFV4.md)
- [/usr/lib/dyld](DYLIBS/dyld.md)
- [/usr/lib/libARI.dylib](DYLIBS/libARI.dylib.md)
- [/usr/lib/libAppletTranslationLibrary.dylib](DYLIBS/libAppletTranslationLibrary.dylib.md)
- [/usr/lib/libLLVM.dylib](DYLIBS/libLLVM.dylib.md)
- [/usr/lib/libPN548_API.dylib](DYLIBS/libPN548_API.dylib.md)
- [/usr/lib/libSESShared.dylib](DYLIBS/libSESShared.dylib.md)
- [/usr/lib/libboringssl.dylib](DYLIBS/libboringssl.dylib.md)
- [/usr/lib/libcryptex.dylib](DYLIBS/libcryptex.dylib.md)
- [/usr/lib/libcryptex_core.dylib](DYLIBS/libcryptex_core.dylib.md)
- [/usr/lib/libcryptex_interface.dylib](DYLIBS/libcryptex_interface.dylib.md)
- [/usr/lib/libcryptex_trampoline.dylib](DYLIBS/libcryptex_trampoline.dylib.md)
- [/usr/lib/libimage4.dylib](DYLIBS/libimage4.dylib.md)
- [/usr/lib/libmis.dylib](DYLIBS/libmis.dylib.md)
- [/usr/lib/libnetquality.dylib](DYLIBS/libnetquality.dylib.md)
- [/usr/lib/libnetworkextension.dylib](DYLIBS/libnetworkextension.dylib.md)
- [/usr/lib/libswiftPrespecialized.dylib](DYLIBS/libswiftPrespecialized.dylib.md)
- [/usr/lib/libsysdiagnose.dylib](DYLIBS/libsysdiagnose.dylib.md)
- [/usr/lib/log/liblog_location.dylib](DYLIBS/liblog_location.dylib.md)
- [/usr/lib/system/liblaunch.dylib](DYLIBS/liblaunch.dylib.md)
- [/usr/lib/system/libsystem_dnssd.dylib](DYLIBS/libsystem_dnssd.dylib.md)
- [/usr/lib/system/libsystem_eligibility.dylib](DYLIBS/libsystem_eligibility.dylib.md)
- [/usr/lib/system/libsystem_info.dylib](DYLIBS/libsystem_info.dylib.md)
- [/usr/lib/system/libsystem_malloc.dylib](DYLIBS/libsystem_malloc.dylib.md)
- [/usr/lib/system/libsystem_pthread.dylib](DYLIBS/libsystem_pthread.dylib.md)
- [/usr/lib/updaters/libSEUpdater.dylib](DYLIBS/libSEUpdater.dylib.md)

</details>

## Feature Flags

### ❌ Removed (1)

- `Domain/Diagnostics.plist`

### ⬆️ Updated (6)

<details>
  <summary><i>View Updated</i></summary>

#### APS.plist

>  `Domain/APS.plist`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>BAAPhysicalDevicesInternal</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>BAASupport</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### AVConference.plist

>  `Domain/AVConference.plist`

```diff

 		<key>Enabled</key>
 		<true/>
 	</dict>
-	<key>EnableEnhancedJBAdaptations</key>
-	<dict>
-		<key>DevelopmentPhase</key>
-		<string>FeatureComplete</string>
-	</dict>
 	<key>EnableEyeContactOniPad</key>
 	<dict>
 		<key>Enabled</key>

```

#### AppleMediaServices.plist

>  `Domain/AppleMediaServices.plist`

```diff

 		<key>Enabled</key>
 		<true/>
 	</dict>
+	<key>EngagementDaemonAppData</key>
+	<dict>
+		<key>Enabled</key>
+		<true/>
+	</dict>
 	<key>EngagementFamilyCircleDatasource</key>
 	<dict>
 		<key>Enabled</key>

```

#### MediaRemote.plist

>  `Domain/MediaRemote.plist`

```diff

 		<key>Enabled</key>
 		<true/>
 	</dict>
+	<key>unify_siri_local_volume</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>watch_intentional_routing</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### Oneness.plist

>  `Domain/Oneness.plist`

```diff

 		<key>DisclosureRequired</key>
 		<string>8f6f8e85-8d9d-8330-8c15-a603765b90f3</string>
 	</dict>
-	<key>RemoteTextInput</key>
-	<dict>
-		<key>DevelopmentPhase</key>
-		<string>FeatureComplete</string>
-	</dict>
 	<key>Shell</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### WiFiManager.plist

>  `Domain/WiFiManager.plist`

```diff

 		<key>Enabled</key>
 		<true/>
 	</dict>
-	<key>EnableCarPlayJoinAfterInCar</key>
-	<dict>
-		<key>Enabled</key>
-		<true/>
-	</dict>
 	<key>EnableNANPHS</key>
 	<dict>
 		<key>Enabled</key>

```


</details>

## EOF
