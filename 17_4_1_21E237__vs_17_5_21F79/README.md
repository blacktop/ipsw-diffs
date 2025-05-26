# 17.4.1 (21E237) .vs 17.5 (21F79)

## IPSWs

- `iPhone16,1_17.4.1_21E237_Restore.ipsw`
- `iPhone16,1_17.5_21F79_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 17.4.1 *(21E237)* | 23.4.0 | 10063.102.14~67 | Fri, 08Mar2024 23:31:42 PST |
| 17.5 *(21F79)* | 23.5.0 | 10063.122.3~3 | Wed, 01May2024 20:34:22 PDT |

### Kexts

#### ⬆️ Updated (60)

<details>
  <summary><i>View Updated</i></summary>

>  `com.apple.AGXFirmwareKextG16PRTBuddy`

```diff

-280.3.9.0.0
-  __TEXT.__const: 0x117
+282.14.0.0.0
+  __TEXT.__const: 0x127
   __TEXT.__cstring: 0x5ce
   __TEXT_EXEC.__text: 0x282c
   __TEXT_EXEC.__auth_stubs: 0x0

```

>  `com.apple.AGXG16P`

```diff

-280.3.9.0.0
-  __TEXT.__const: 0x43ec
-  __TEXT.__cstring: 0xc5bf
+282.14.0.0.0
+  __TEXT.__const: 0x4414
+  __TEXT.__cstring: 0xc5d9
   __TEXT.__os_log: 0x2d8
-  __TEXT_EXEC.__text: 0xa801c
+  __TEXT_EXEC.__text: 0xa89a8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x13b8
   __DATA.__common: 0x10

   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x308
   __DATA_CONST.__mod_term_func: 0x270
-  __DATA_CONST.__const: 0x103c8
+  __DATA_CONST.__const: 0x10418
   __DATA_CONST.__kalloc_type: 0x2100
   __DATA_CONST.__kalloc_var: 0x3160
-  Functions: 1213
+  Functions: 1218
   Symbols:   0
-  CStrings:  1664
+  CStrings:  1671
 
CStrings:
+ "1221111111122222222211112122222222222222222222222222221112111111"
+ "AGXk: %s:%d:%s: !!! Unexpectedly handled SAPT interrupt!\n"
+ "Enable"
+ "Fi_hit"
+ "Fi_miss"
+ "Fn_hit"
+ "Fn_miss"
+ "G16G"
+ "High_Confidence"
+ "May  2 2024 07:24:53"
+ "Min_Confidence"
+ "Nei_hit"
+ "Probablity_Init_Val"
+ "Reset_Iterations"
+ "SEEngageTolerance"
+ "SEResetDelayCounter"
+ "SEResetTolerance"
+ "Standby_Timer"
+ "engage-tolerance"
+ "gpu-se-engagement-tolerance"
+ "gpu-se-reset-tolerance"
+ "reset-tolerance"
+ "virtual void AGXAccelerator::handleSAPTInterrupt()"
- "122111111122222222211112122222222222222222222222222221112111111"
- "Mar  8 2024 23:58:58"
- "ce_override"
- "downsample_count_override"
- "dual_filter_overridden"
- "dual_filter_override"
- "filter_tc_override0"
- "filter_tc_override1"
- "inactive_engagement_threshold_override"
- "integral_gain_override0"
- "integral_gain_override1"
- "proportional_gain_override0"
- "proportional_gain_override1"
- "reset_criteria_override"
- "sustained_efficiency_engagement_criteria_override"
- "target_override"

```

>  `com.apple.AUC`

```diff

-485.13.0.0.0
+516.2.0.0.0
   __TEXT.__cstring: 0x947
   __TEXT.__const: 0x20
-  __TEXT_EXEC.__text: 0x55a0
+  __TEXT_EXEC.__text: 0x56e4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc5
   __DATA.__common: 0xb0

   __DATA_CONST.__got: 0x60
   __DATA_CONST.__mod_init_func: 0x20
   __DATA_CONST.__mod_term_func: 0x20
-  __DATA_CONST.__const: 0xfb0
+  __DATA_CONST.__const: 0xfc8
   __DATA_CONST.__kalloc_type: 0x240
   __DATA_CONST.__kalloc_var: 0xa0
-  Functions: 129
+  Functions: 132
   Symbols:   0
   CStrings:  42
 

```

>  `com.apple.driver.AppleA7IOP`

```diff

-225.100.13.0.0
+225.120.5.0.0
   __TEXT.__cstring: 0xe1e
-  __TEXT_EXEC.__text: 0x5ebc
+  __TEXT_EXEC.__text: 0x5ec0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0xb0

```

>  `com.apple.driver.AppleA7IOP-ASCWrap-v6`

```diff

-225.100.13.0.0
-  __TEXT.__cstring: 0x3f8
-  __TEXT_EXEC.__text: 0x1894
+225.120.5.0.0
+  __TEXT.__cstring: 0x40d
+  __TEXT_EXEC.__text: 0x1920
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60
   __DATA_CONST.__auth_got: 0xd8
-  __DATA_CONST.__got: 0x20
+  __DATA_CONST.__got: 0x18
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xf20
CStrings:
+ "offset + sizeof(uint32_t) <= device_memory->getLength()"
+ "virtual void AppleASCWrapV6::_mapFirmware(uint64_t, IOMemoryDescriptor *, IOOptionBits)"
- "offset + PAGE_SIZE <= device_memory->getLength()"
- "virtual void AppleASCWrapV6::_mapFirmware(uint64_t, IOMemoryDescriptor *)"

```

>  `com.apple.driver.AppleARMPlatform`

```diff

-1026.100.19.0.3
+1026.120.7.0.0
   __TEXT.__const: 0x16f0
   __TEXT.__os_log: 0x13fe
-  __TEXT.__cstring: 0xc8c0
-  __TEXT_EXEC.__text: 0x52244
+  __TEXT.__cstring: 0xcac1
+  __TEXT_EXEC.__text: 0x52c40
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x6c8
-  __DATA.__common: 0xca0
+  __DATA.__common: 0xcc8
   __DATA.__bss: 0x69
   __DATA_CONST.__auth_got: 0x668
   __DATA_CONST.__got: 0x1f0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x128
   __DATA_CONST.__mod_term_func: 0x128
-  __DATA_CONST.__const: 0x15e68
+  __DATA_CONST.__const: 0x16588
   __DATA_CONST.__kalloc_var: 0x140
-  __DATA_CONST.__kalloc_type: 0x1540
-  Functions: 1217
+  __DATA_CONST.__kalloc_type: 0x1580
+  Functions: 1229
   Symbols:   0
-  CStrings:  1663
+  CStrings:  1692
 
CStrings:
+ "%s.livelog"
+ "%s: CmdEnd, %X - %s %02x - #%02x %uus\n"
+ "%s: CmdEnd, %X - %s %02x - #%02x %uus, 0x%08x\n"
+ "%s: CmdStart, %X - %s %02x - #%02x\n"
+ "*size >= count * sizeof(spmiLogEnt)"
+ ".livelog"
+ "12111112122212121111122212111112"
+ "AppleARMSPMIControllerUserClient"
+ "AppleARMSPMIDeviceUserClient"
+ "Authenticate"
+ "BusOwnership"
+ "Copied %d entries\n"
+ "DDBFollowerRead"
+ "DDBLeaderRead"
+ "ExtRegRead"
+ "ExtRegReadLong"
+ "ExtRegWriteLong"
+ "ExtrRegWrite"
+ "LeaderRead"
+ "LeaderWrite"
+ "Not enough space %0x < %0lx\n"
+ "Reg0Write"
+ "RegRead"
+ "RegWrite"
+ "Reset"
+ "Shutdown"
+ "Sleep"
+ "Unknown"
+ "Unsupported"
+ "Wakeup"
+ "all-spmi.livelog"
+ "com.apple.driver.SPMI.user-access"
+ "dcpexpert-service-cb"
+ "site.AppleARMSPMIControllerUserClient"
+ "site.AppleARMSPMIDeviceUserClient"
- "12111112122212121111121222111112"
- "AppleARMSPMIUserClient"
- "com.apple.driver.SPMI.device.user-access"
- "dcpexpert-service"
- "losesPowerInSleep"
- "site.AppleARMSPMIUserClient"

```

>  `com.apple.driver.AppleARMWatchdogTimer`

```diff

-254.100.5.0.0
-  __TEXT.__cstring: 0xff3
-  __TEXT_EXEC.__text: 0x4a64
+254.120.4.0.0
+  __TEXT.__cstring: 0x113f
+  __TEXT_EXEC.__text: 0x4d4c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x118
   __DATA.__common: 0xc0

   __DATA_CONST.__const: 0x1380
   __DATA_CONST.__kalloc_type: 0xc0
   __DATA_CONST.__kalloc_var: 0x190
-  Functions: 96
+  Functions: 102
   Symbols:   0
-  CStrings:  107
+  CStrings:  113
 
CStrings:
+ "\"Simplified Reconfig watchdog cannot be supported without SMC AP watchdog support\" @%s:%d"
+ "\"simple-reconfig-wdog-support and reconfig-wdog-support can't be enabled at the same time. They are mutually exclusive\" @%s:%d"
+ "Disabling AON Watchdog...\n"
+ "Reconfig Watchdog: ICC = %d\n"
+ "simple-reconfig-wdog-icc-time"
+ "simple-reconfig-wdog-support"

```

>  `com.apple.driver.AppleAVD`

```diff

-740.5.0.0.0
-  __TEXT.__os_log: 0x1cc35
-  __TEXT.__cstring: 0x10be3
+742.5.0.0.0
+  __TEXT.__os_log: 0x1ccb0
+  __TEXT.__cstring: 0x10bfe
   __TEXT.__const: 0x8a1c8
-  __TEXT_EXEC.__text: 0xf0678
+  __TEXT_EXEC.__text: 0xf087c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2ac
   __DATA.__common: 0x90
   __DATA.__bss: 0x14
-  __DATA_CONST.__auth_got: 0x3c0
+  __DATA_CONST.__auth_got: 0x3c8
   __DATA_CONST.__got: 0xd8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x10

   __DATA_CONST.__const: 0x5678
   __DATA_CONST.__kalloc_type: 0x3a80
   __DATA_CONST.__kalloc_var: 0x1b30
-  Functions: 1642
+  Functions: 1644
   Symbols:   0
-  CStrings:  2174
+  CStrings:  2177
 
CStrings:
+ "AppleAVD: ERROR: %s(): buffer has device memory cache mode!\n"
+ "AppleAVD: WARNING: %s(): Couldn't find surface with index %d\n"
+ "isDeviceExclusiveCacheMode"

```

>  `com.apple.driver.AppleAVE2`

```diff

-760.23.1.0.0
-  __TEXT.__const: 0x22db0
-  __TEXT.__cstring: 0x29a58
-  __TEXT.__os_log: 0x3036f
-  __TEXT_EXEC.__text: 0x10251c
+760.30.1.0.0
+  __TEXT.__const: 0x22d10
+  __TEXT.__cstring: 0x29aaa
+  __TEXT.__os_log: 0x303b9
+  __TEXT_EXEC.__text: 0x102684
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2b0
   __DATA.__common: 0xb4

   __DATA_CONST.__kalloc_var: 0x8c0
   Functions: 1270
   Symbols:   0
-  CStrings:  5633
+  CStrings:  5634
 
CStrings:
+ "%lld %d AVE %s: %s:%d %s | failed to create surface input YUV %p %d %d %p"
+ "%lld %d AVE %s: %s:%d %s | failed to create surface input YUV %p %d %d %p\n"
+ "20:23:51"
+ "AVE_CodecType_AVC <= pIn->codecType && pIn->codecType < AVE_CodecType_Max"
+ "May  1 2024"
- "00:50:57"
- "Mar  9 2024"
- "pIn->codecType < AVE_CodecType_Max"
- "ret == 0 && pSurface != nullptr"

```

>  `com.apple.driver.AppleActuatorDriver`

```diff

-7140.17.0.0.0
+7150.1.0.0.0
   __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x1243
+  __TEXT.__cstring: 0x1283
   __TEXT.__os_log: 0x2f1
-  __TEXT_EXEC.__text: 0xa4e8
+  __TEXT_EXEC.__text: 0xa8f0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0xf0
-  __DATA_CONST.__auth_got: 0x238
+  __DATA_CONST.__auth_got: 0x248
   __DATA_CONST.__got: 0xa8
   __DATA_CONST.__mod_init_func: 0x28
   __DATA_CONST.__mod_term_func: 0x28

   __DATA_CONST.__kalloc_var: 0x190
   Functions: 145
   Symbols:   0
-  CStrings:  159
+  CStrings:  164
 
CStrings:
+ "ActuatorLimits"
+ "AmplitudeMax"
+ "AmplitudeMin"
+ "DurationMax"
+ "DurationMin"
+ "changeHostClickControl"
- "reclaimHostClickControl"

```

>  `com.apple.driver.AppleAuthCP`

```diff

-144.100.3.0.0
+144.120.2.0.0
   __TEXT.__const: 0x4c
   __TEXT.__cstring: 0x26c1
   __TEXT.__os_log: 0x1025
-  __TEXT_EXEC.__text: 0x17bdc
+  __TEXT_EXEC.__text: 0x17bc4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x188
   __DATA.__common: 0x1f0

```

>  `com.apple.driver.AppleC26Charger`

```diff

-50.100.3.0.0
+50.120.2.0.0
   __TEXT.__const: 0x188
   __TEXT.__cstring: 0x2121
   __TEXT.__os_log: 0x51
-  __TEXT_EXEC.__text: 0x15108
+  __TEXT_EXEC.__text: 0x15124
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x370

```

>  `com.apple.driver.AppleDiskImages2`

```diff

-276.100.16.0.0
-  __TEXT.__cstring: 0x2041
+276.120.5.0.2
+  __TEXT.__cstring: 0x2040
   __TEXT.__os_log: 0x11a2
   __TEXT.__const: 0x10
   __TEXT_EXEC.__text: 0xd32c
CStrings:
+ "276.120.5"
- "276.100.16"

```

>  `com.apple.driver.AppleDisplayCrossbar`

```diff

-314.100.14.0.0
+314.120.5.0.0
   __TEXT.__cstring: 0x41bd
-  __TEXT.__os_log: 0x5c0c
+  __TEXT.__os_log: 0x5bf1
   __TEXT.__const: 0x160
-  __TEXT_EXEC.__text: 0x31f54
+  __TEXT_EXEC.__text: 0x320e0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x3a8
-  __DATA_CONST.__auth_got: 0x1e8
+  __DATA_CONST.__auth_got: 0x1f0
   __DATA_CONST.__got: 0xd0
   __DATA_CONST.__mod_init_func: 0xb8
   __DATA_CONST.__mod_term_func: 0xb8
-  __DATA_CONST.__const: 0xc7b8
+  __DATA_CONST.__const: 0xc7e0
   __DATA_CONST.__kalloc_type: 0x5c0
-  Functions: 554
+  Functions: 553
   Symbols:   0
-  CStrings:  698
+  CStrings:  700
 
CStrings:
+ "12111112122212121122222112211111111112111222222"
+ "IOAV[%d] %s<0x%llx>::%s: reset _hpdAsserted due to tunnel state change\n"
+ "Route String"
+ "pipe-sharing"
+ "reset _hpdAsserted due to tunnel state change\n"
- "1211111212221212112222211221111111111211122222"
- "IOAV[%d] %s<0x%llx>::%s: reset _hpdAsserted and _dpinAdapterPortActive due to tunnel state change\n"
- "reset _hpdAsserted and _dpinAdapterPortActive due to tunnel state change\n"

```

>  `com.apple.driver.AppleEmbeddedMikeyBus`

```diff

 217.0.0.0.0
-  __TEXT.__cstring: 0x1edc
+  __TEXT.__cstring: 0x1ede
   __TEXT.__const: 0x78
   __TEXT_EXEC.__text: 0x187e4
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__mod_init_func: 0x48
   __DATA_CONST.__mod_term_func: 0x48
-  __DATA_CONST.__const: 0x56c0
+  __DATA_CONST.__const: 0x56d0
   __DATA_CONST.__kalloc_type: 0x380
   __DATA_CONST.__kalloc_var: 0x1e0
   Functions: 293
CStrings:
+ "12111112122212121111112111112122222222112211111112122111122222212222121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122222221222222222222222212222222221122212222212222222122222122222222122222112211121211111211212"
- "121111121222121211111121111121222222221122111111121221111222222122221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211222222212222222222222222122222222211222122222122222221222221222222122222112211121211111211212"

```

>  `com.apple.driver.AppleEmbeddedUSBHost`

```diff

-615.100.5.0.0
-  __TEXT.__cstring: 0x5a0
+615.120.5.0.0
+  __TEXT.__cstring: 0x5a2
   __TEXT.__const: 0x40
   __TEXT_EXEC.__text: 0x2590
   __TEXT_EXEC.__auth_stubs: 0x0
CStrings:
+ "121111121222121211222222212222222222222222222222222222222222222222222222222221221111122221111111112112222222222111221221"
+ "12111112122212121122222221222222222222222222222222222222222222222222222222222122111112222111111111211222222222211122122122"
- "12111112122212121122222212222222222222222222222222222222222222222222222222221221111122221111111112112222222222111221221"
- "1211111212221212112222221222222222222222222222222222222222222222222222222222122111112222111111111211222222222211122122122"

```

>  `com.apple.driver.AppleH10PearlCameraInterface`

```diff

-20.402.0.0.0
+20.500.1.0.0
   __TEXT.__cstring: 0x67b
   __TEXT.__os_log: 0x130
-  __TEXT_EXEC.__text: 0x7910
+  __TEXT_EXEC.__text: 0x79e8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x2e0

   __DATA_CONST.__mod_term_func: 0x8
   __DATA_CONST.__const: 0x1b48
   __DATA_CONST.__kalloc_type: 0x480
-  Functions: 231
+  Functions: 232
   Symbols:   0
   CStrings:  94
 

```

>  `com.apple.driver.AppleH16ANEInterface`

```diff

-7.400.0.0.0
-  __TEXT.__os_log: 0x2515c
-  __TEXT.__cstring: 0x9cc1
-  __TEXT.__const: 0x430
-  __TEXT_EXEC.__text: 0x8372c
+7.500.0.0.0
+  __TEXT.__os_log: 0x24c6a
+  __TEXT.__cstring: 0x9d40
+  __TEXT.__const: 0x4e0
+  __TEXT_EXEC.__text: 0x83158
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x2b88
+  __DATA.__data: 0x2f90
   __DATA.__common: 0x370
   __DATA.__bss: 0x210
   __DATA_CONST.__auth_got: 0x7e8

   __DATA_CONST.__mod_term_func: 0x20
   __DATA_CONST.__const: 0x5870
   __DATA_CONST.__kalloc_type: 0x2680
-  __DATA_CONST.__kalloc_var: 0x1ea0
-  Functions: 979
+  __DATA_CONST.__kalloc_var: 0x1ef0
+  Functions: 978
   Symbols:   0
-  CStrings:  2777
+  CStrings:  2786
 
CStrings:
+ "\"Exclave mode switch didn't succeed on retry\\n\" @%s:%d"
+ "\"Firmware timeout recovery for Exclaves failed!!!\\n\" @%s:%d"
+ "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/System/Library/Frameworks/Kernel.framework/PrivateHeaders/kernel_sdkroot/usr/include/c++/v1/span"
+ "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/System/Library/Frameworks/Kernel.framework/PrivateHeaders/kernel_sdkroot/usr/include/c++/v1/vector"
+ "ANE%d: %s - No capability parameters\n"
+ "ANE%d: %s Ignoring unsuppported notification\n"
+ "ANE%d: %s Warning: no target\n"
+ "ANE%d: %s messageType=0x%x changeFlags=0x%x capabilities=(0x%x -> 0x%x)\n"
+ "ANE%d: %s: ANE Sleep in progress...Block here waiting for ANE to come back from sleep\n"
+ "ANE%d: %s: ANE driverInitiatedSleep completed\n"
+ "ANE%d: %s: ANE power on in progress...Block here waiting for ANE to be up\n"
+ "ANE%d: %s: ANE power status: isPowered: %d, fDeInitInProgress: %d, fFirmwareTimeout: %d\n"
+ "ANE%d: %s: ANE sleep failed! Marking firmware as being in timed out for clean reboot\n"
+ "ANE%d: %s: ANE sleep initiated\n"
+ "ANE%d: %s: ANE systemInitiatedSleep completed\n"
+ "ANE%d: %s: About to sleep\n"
+ "ANE%d: %s: Added a persistent client for ANEExclave during retry attempt...\n"
+ "ANE%d: %s: Added persistent client for ANEExclave\n"
+ "ANE%d: %s: All pending requests completed. Proceeding with regular sleep\n"
+ "ANE%d: %s: Attempting driver initiated sleep in kIOMessageSystemWillSleep call\n"
+ "ANE%d: %s: Cleanup finished\n"
+ "ANE%d: %s: Cleanup started\n"
+ "ANE%d: %s: Client passed -1 for driver initiated sleep timer period, ignoring\n"
+ "ANE%d: %s: Client passed 0 for driver initiated sleep timer period, disabling sleep timer\n"
+ "ANE%d: %s: Client requesting power on: %s\n"
+ "ANE%d: %s: Client: %s, powerAssertion: %d, isClosed: %d\n"
+ "ANE%d: %s: Couldn't DART map consolidated memory descriptor\n"
+ "ANE%d: %s: Dark Wake ANE_IsPowered=%d\n"
+ "ANE%d: %s: Did not match due to size\n"
+ "ANE%d: %s: Did not match program\n"
+ "ANE%d: %s: Done waiting for commands to complete on the ANE\n"
+ "ANE%d: %s: Done waiting for pending commands to complete retries=%d"
+ "ANE%d: %s: Done waiting for pending requests to complete\n"
+ "ANE%d: %s: Done waiting for requests to complete on the ANE retries=%d\n"
+ "ANE%d: %s: Driver initiated sleep failed. result = 0x%x\n"
+ "ANE%d: %s: ERROR commandArgs is NULL in fOutstandingCommands osset\n"
+ "ANE%d: %s: ERROR data %p not present in fOutstandingCommands osset\n"
+ "ANE%d: %s: ERROR: Invalid number of i/o buffers, programHandle: 0x%llx, totInputBuffers: %u, totOutputBuffers: %u\n"
+ "ANE%d: %s: ERROR: total i/o buffers calculation overflowed\n"
+ "ANE%d: %s: EXCLAVE mode -> SECURE mode\n"
+ "ANE%d: %s: Enabled driver initiated sleep timer! fANEDriverInitiatedSleepTimerPeriodMs=%d\n"
+ "ANE%d: %s: Error: ReleaseSharedMemorySurface called on surface with no references\n"
+ "ANE%d: %s: Exclave interrupt was disabled during firmware recovery\n"
+ "ANE%d: %s: Exclave mode not active\n"
+ "ANE%d: %s: FD networks surface PA(%p) not found in fPersistentSharedMemorySurfaces list\n"
+ "ANE%d: %s: Failed to allocate memory descriptor\n"
+ "ANE%d: %s: Failed to map non-persistent surface shared memory descriptor\n"
+ "ANE%d: %s: Failed to map persistent surface shared memory descriptor\n"
+ "ANE%d: %s: Failed to transition into Exclave mode, (fFirmwareTimeout=%d) will retry\n"
+ "ANE%d: %s: Failed to transition out of Exclave mode, (fFirmwareTimeout=%d) will not retry\n"
+ "ANE%d: %s: Finished saving ANE state\n"
+ "ANE%d: %s: Firmware time state cleared... retrying Exclave mode switch sequence\n"
+ "ANE%d: %s: Forcing firmware timeout path for clean reboot\n"
+ "ANE%d: %s: Freed mapped FD networks ISP surface. surface-id=0x%08X, size=0x%016llx dartMapBase=0x%08X\n"
+ "ANE%d: %s: Freed mapped ISP surface. surface-id=0x%08X, size=0x%016llx, dartMapBase=0x%016llx\n"
+ "ANE%d: %s: Freed mapped ISP surface. surface-id=0x%08X, size=0x%016llx, dartMapBase=0x%08X\n"
+ "ANE%d: %s: Freed mutable kernel surface. programId: %d, size: 0x%016llx, dartMapBase: 0x%016llx\n"
+ "ANE%d: %s: Freed non-persistent shared surface. surface-id=0x%08X, size=0x%016llx, dartMapBase=0x%016llx usage='%c%c%c%c'\n"
+ "ANE%d: %s: Freed persistent shared surface. surface-id=0x%08X, size=0x%016llx, dartMapBase=0x%016llx usage='%c%c%c%c'\n"
+ "ANE%d: %s: Freeing program memory surface. programId: %d, size: %-8d, dartMapBase: 0x%08X refCount: %d\n"
+ "ANE%d: %s: Going to sleep before retrying persistent client re-registration...\n"
+ "ANE%d: %s: IPC peer ISP will power down\n"
+ "ANE%d: %s: ISP client still present.. waiting for it to go away. retries=%d\n"
+ "ANE%d: %s: ITQ result: #TsInfo: %d, #Pending queries: %lld\n"
+ "ANE%d: %s: Ignoring message type %u as fFirmwareTimeout=%d fDeInitInProgress=%d\n"
+ "ANE%d: %s: Masking off ANE Exclave interrupt before informing the EC\n"
+ "ANE%d: %s: Moved non-persistent shared surface into pending list, surface-id=0x%08X, size=%016llx dartMapBase=%016llx usage='%c%c%c%c'\n"
+ "ANE%d: %s: Moved peer shared surface into pending list. surface-id=0x%08X, size=0x%016llx, dartMapBase=0x%016llx usage='%c%c%c%c'\n"
+ "ANE%d: %s: Moved persistent shared surface into pending list. surface-id=0x%08X, size=0x%016llx dartMapBase=0x%016llx usage='%c%c%c%c'\n"
+ "ANE%d: %s: Moving intermediate buffer into pending list, intermediateBufferId=0x%llx, size=%lld, dartMapBase=0x%016llx usage='%c%c%c%c'\n"
+ "ANE%d: %s: Moving program memory surface into pending list. programId: %d, size: %-8d, dartMapBase: 0x%08X refCount: %d\n"
+ "ANE%d: %s: No pending request for SECURE mode -> EXCLAVE mode \n"
+ "ANE%d: %s: None of the programs matched\n"
+ "ANE%d: %s: Not re-enabling driver initiated sleep timer, IsLatencySensitiveClientPresent=%d pendingRequests=%d\n"
+ "ANE%d: %s: Not re-enabling driver initiated sleep timer, fSystemInitiatedSleep=%d fSleepInProgress=%d\n"
+ "ANE%d: %s: Not starting driver initiated sleep timer, fDriverInitiatedSleepAssertions=%u\n"
+ "ANE%d: %s: PearlSEP Client going away..powering OFF the ANE, retries=%d\n"
+ "ANE%d: %s: PearlSEP client still present.. waiting for it to go away. retries=%d camDisableTimeouts=%d\n"
+ "ANE%d: %s: PersistentClient upcall ack delivery failed!\n"
+ "ANE%d: %s: Querying status for: %llu\n"
+ "ANE%d: %s: Release aned daemon\n"
+ "ANE%d: %s: Removed persistent client for ANEExclave\n"
+ "ANE%d: %s: Removed persistent client for ANEExclave before retrying...\n"
+ "ANE%d: %s: Removing mappings for programId: %d\n"
+ "ANE%d: %s: RequestUUID: %lld startTS: %lld endTS: %lld\n"
+ "ANE%d: %s: Requested power state: %d\n"
+ "ANE%d: %s: Restoring Exclave state\n"
+ "ANE%d: %s: Retry Exclave mode switch\n"
+ "ANE%d: %s: SECURE mode -> EXCLAVE mode\n"
+ "ANE%d: %s: Skip cleanup - nothing in the pending queue\n"
+ "ANE%d: %s: Start aned daemon\n"
+ "ANE%d: %s: Starting SECURE mode\n"
+ "ANE%d: %s: Starting deinit\n"
+ "ANE%d: %s: Stopping SECURE mode\n"
+ "ANE%d: %s: Surface with PA(%p) not found in the ISP mapped surface list\n"
+ "ANE%d: %s: Suspend in progress, returning\n"
+ "ANE%d: %s: Switched out of Exclave mode\n"
+ "ANE%d: %s: Switched to Exclave mode after retrying\n"
+ "ANE%d: %s: Switching out of Exclave mode\n"
+ "ANE%d: %s: Switching to Exclave mode\n"
+ "ANE%d: %s: Timed out\n"
+ "ANE%d: %s: Timed out waiting for ANE to be up. Retrying...retries=%d\n"
+ "ANE%d: %s: Timed out waiting for ANE to wake up. Retrying...retries=%d\n"
+ "ANE%d: %s: Timed out waiting for ISP to go away sleepResult=0x%x aneISPClientContext->isPowered=%d\n"
+ "ANE%d: %s: Timed out waiting for PearlSEP to go away sleepResult=0x%x\n"
+ "ANE%d: %s: Timed out waiting for commands to complete on the ANE\n"
+ "ANE%d: %s: Timed out waiting for fFirmwareTimeout state to be cleared during Exclave mode switch, sleepResult=0x%x\n, retry count %d\n"
+ "ANE%d: %s: Timed out waiting for requests to complete on the ANE\n"
+ "ANE%d: %s: Try to remove some mappings\n"
+ "ANE%d: %s: WARN: ANE Sleep without fSleepInProgress set to true!! Forcing fSleepInProgress to true \n"
+ "ANE%d: %s: Wait for ISP client going away before powering OFF the ANE... retries=%d\n"
+ "ANE%d: %s: Waiting for ISP to go away with camDisableTimeouts=1\n"
+ "ANE%d: %s: Waiting for commands to complete on the ANE...retries=%d\n"
+ "ANE%d: %s: Waiting for pending requests to complete on the ANE...retries=%d\n"
+ "ANE%d: %s: Work Stats:  WorkSubmit: %u WorkSubmitFailed: %u WorkBegin: %u WorkEnd: %u PendingRequests: %u\n"
+ "ANE%d: %s: Work around for PushTelemetry\n"
+ "ANE%d: %s: checkFwCpuThrottled: %d\n"
+ "ANE%d: %s: fDriverInitiatedSleepAssertions=0, checking other conditions now\n"
+ "ANE%d: %s: fEnableFwReload is off, don't do anything\n"
+ "ANE%d: %s: fEnableFwReload is on from forget\n"
+ "ANE%d: %s: fNonPersistentSharedMemorySurfaces: %d\n"
+ "ANE%d: %s: kIOMessageSystemHasPoweredOn ANE_IsPowered=%d\n"
+ "ANE%d: %s: kIOMessageSystemWillNotSleep ANE_IsPowered=%d\n"
+ "ANE%d: %s: kIOMessageSystemWillPowerOn\n"
+ "ANE%d: %s: kIOMessageSystemWillSleep ANE_IsPowered=%d\n"
+ "ANE%d: %s: messageANEAddress: 0x%llx\n"
+ "ANETLimitHandlingDuringPowerDown"
+ "ANE_QuiesceFirmwareWorkProcessor"
+ "AppleT8132ANEHAL"
+ "aneExclaveCycleRetry"
+ "pmp-virt-notify"
+ "setPowerState"
- "/AppleInternal/Library/BuildRoots/2d3303f9-dd50-11ee-ac91-22c3409c8aad/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/System/Library/Frameworks/Kernel.framework/PrivateHeaders/kernel_sdkroot/usr/include/c++/v1/span"
- "/AppleInternal/Library/BuildRoots/2d3303f9-dd50-11ee-ac91-22c3409c8aad/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/System/Library/Frameworks/Kernel.framework/PrivateHeaders/kernel_sdkroot/usr/include/c++/v1/vector"
- "ANE%d: %s :\n"
- "ANE%d: %s : H11ANEIn::ANE_PowerOnByKernelClient - about to sleep\n"
- "ANE%d: %s : WARN: ANE Sleep without fSleepInProgress set to true!! Forcing fSleepInProgress to true \n"
- "ANE%d: %s :ANE Sleep in progress...Block here waiting for ANE to come back from sleep\n"
- "ANE%d: %s :ANE driverInitiatedSleep completed\n"
- "ANE%d: %s :ANE power on in progress...Block here waiting for ANE to be up\n"
- "ANE%d: %s :ANE sleep failed!\n"
- "ANE%d: %s :ANE systemInitiatedSleep completed\n"
- "ANE%d: %s :ANE_SaveState completed\n"
- "ANE%d: %s :Couldn't DART map consolidated memory descriptor\n"
- "ANE%d: %s :Did not match due to size\n"
- "ANE%d: %s :Did not match program\n"
- "ANE%d: %s :Done waiting for commands to complete on the ANE\n"
- "ANE%d: %s :Done waiting for pending commands to complete retries=%d"
- "ANE%d: %s :Done waiting for pending requests to complete"
- "ANE%d: %s :Done waiting for requests to complete on the ANE retries=%d\n"
- "ANE%d: %s :H11ANE::setPowerStateGated - ANE sleep initiated\n"
- "ANE%d: %s :H11ANEIn: FD networks surface physicalAddress(%p) is not found in the  fPersistentSharedMemorySurfaces list\n"
- "ANE%d: %s :H11ANEIn: The surface physicalAddress(%p) is not found in the ISP mapped surface list\n"
- "ANE%d: %s :H11ANEIn:: IPC peer ISP will power down\n"
- "ANE%d: %s :H11ANEIn::ANE_processISPSurfaceUnMapRequest - freed mapped  FD networks ISP surface. surface-id=0x%08X, size=0x%016llx, dartMapBase=0x%08X\n"
- "ANE%d: %s :H11ANEIn::ANE_processISPSurfaceUnMapRequest - freed mapped ISP surface. surface-id=0x%08X, size=0x%016llx, dartMapBase=0x%016llx\n"
- "ANE%d: %s :H11ANEIn::ANE_processISPSurfaceUnMapRequest - freed mapped ISP surface. surface-id=0x%08X, size=0x%016llx, dartMapBase=0x%08X\n"
- "ANE%d: %s :H11ANEIn::ANE_releaseDaemon_gated, release aned daemon\n"
- "ANE%d: %s :H11ANEIn::ANE_startDaemon_gated, start aned daemon\n"
- "ANE%d: %s :H11ANEIn::AllocateHeapMemorySurface failed to allocate memory descriptor\n"
- "ANE%d: %s :H11ANEIn::ReleaseFwHeapMemorySurface\n"
- "ANE%d: %s :H11ANEIn::processCommandResponse, messageANEAddress: 0x%llx\n"
- "ANE%d: %s :H11ANEIn::setPowerStateGated, suspend in progress\n"
- "ANE%d: %s :H11ANEIn::setPowerStateGated: %d\n"
- "ANE%d: %s :INFO: H11ANEIn: ANE power status: isPowered: %d, fDeInitInProgress: %d, fFirmwareTimeout: %d\n"
- "ANE%d: %s :ISP Client present when we are asked to sleep by PMGR.. Waiting for ISP client to go away. retries=%d\n"
- "ANE%d: %s :None of the programs matched\n"
- "ANE%d: %s :PearlSEP Client going away..powering OFF the ANE.... retries=%d\n"
- "ANE%d: %s :PearlSEP Client present when we are asked to sleep by PMGR.. Waiting for PearlSEP client to go away. retries=%d camDisableTimeouts=%d\n"
- "ANE%d: %s :Removing mappings for programId: %d\n"
- "ANE%d: %s :Timed out waiting for ANE  to be up.Retrying...retries=%d\n"
- "ANE%d: %s :Timed out waiting for ANE  to wake up.Retrying...retries=%d\n"
- "ANE%d: %s :Timed out waiting for ISP to go away sleepResult=0x%x aneISPClientContext->isPowered=%d\n"
- "ANE%d: %s :Timed out waiting for PearlSEP to go away sleepResult=0x%x\n"
- "ANE%d: %s :Timed out waiting for commands to complete on the ANE\n"
- "ANE%d: %s :Timed out waiting for requests to complete on the ANE\n"
- "ANE%d: %s :Try to remove some mappings\n"
- "ANE%d: %s :Wait for ISP Client going away..powering OFF the ANE.... retries=%d\n"
- "ANE%d: %s :Waiting for commands to complete on the ANE...retries=%d\n"
- "ANE%d: %s :Waiting for pending requests to complete on the ANE...retries=%d\n"
- "ANE%d: %s :fEnableFwReload is off, don't do anything \n"
- "ANE%d: %s :fEnableFwReload is on from forget\n"
- "ANE%d: %s :line: %d\n"
- "ANE%d: %s Driver initiated sleep failed. result = 0x%x\n"
- "ANE%d: %s: ANE_deInit - 0x%08X\n"
- "ANE%d: %s: Added a persistent client for ANEExclave...\n"
- "ANE%d: %s: Bring out of Exclave mode and set the pending flag\n"
- "ANE%d: %s: CSNE_CMD_SECURE_MODE_STOP \n"
- "ANE%d: %s: Client requesting power on: %s"
- "ANE%d: %s: Completing pending request for switch to Exclave mode\n"
- "ANE%d: %s: ERROR: Invalid number of i/o buffers, programHandle: 0x%llx, totInputBuffers: %d, totOutputBuffers: %d\n"
- "ANE%d: %s: Enabled driver initiated sleep timer! fANEDriverInitiatedSleepTimerPeriodMs= %d\n"
- "ANE%d: %s: Entering ANE_CleanupForColdReboot_gated ++"
- "ANE%d: %s: EvaluateWithModel returned token %llu\n"
- "ANE%d: %s: Exclave evaluate: %llu queued\n"
- "ANE%d: %s: Exclave load for %d queued\n"
- "ANE%d: %s: Exclave unload: %llu queued\n"
- "ANE%d: %s: Exiting ANE_CleanupForColdReboot_gated --"
- "ANE%d: %s: ITQ result: Num of TsInfo %d requestUUID: %lld startTS: %lld endTS: %lld\n"
- "ANE%d: %s: LoadModel returned programHandle %llu\n"
- "ANE%d: %s: Masking off ANE Exclave interrupt before informing the EC"
- "ANE%d: %s: Moving intermediate buffer into pending list due to fSleepInProgress = true. intermediateBufferId=0x%llx, size=%lld, dartMapBase=0x%016llx usage='%c%c%c%c'\n"
- "ANE%d: %s: No pending requests for switching from SEP to Exclave mode \n"
- "ANE%d: %s: Not re-enabling driver initiated sleep timer as latency sensitive client is present or pending requests queue is non empty IsLatencySensitiveClientPresent=%d pendingRequests = %d\n"
- "ANE%d: %s: Not re-enabling driver initiated sleep timer as sleep is in progress fSystemInitiatedSleep=%d fSleepInProgress = %d\n"
- "ANE%d: %s: Not start driver initiated sleep timer, fDriverInitiatedSleepAssertions = %u\n"
- "ANE%d: %s: Not toggling Exclave state for user client\n"
- "ANE%d: %s: Pending queries %lld\n"
- "ANE%d: %s: Querying status of request from driver: %llu\n"
- "ANE%d: %s: Removed a persistent client for ANEExclave...\n"
- "ANE%d: %s: Switched to regular mode\n"
- "ANE%d: %s: Switching out of Exclave mode now\n"
- "ANE%d: %s: Unload call returned %llu\n"
- "ANE%d: %s: Work around for Telmetry\n"
- "ANE%d: %s: fDriverInitiatedSleepAssertions = 0 , setting off timer to initiate sleep\n"
- "ANE%d: %s: freed mutable kernel surface. programId: %d, size: 0x%016llx, dartMapBase: 0x%016llx\n"
- "ANE%d: %s: freeing program memory surface. programId: %d, size: %-8d, dartMapBase: 0x%08X refCount: %d\n"
- "ANE%d: %s: moving program memory surface into pending list due to fSleepInProgress=true. programId: %d, size: %-8d, dartMapBase: 0x%08X refCount: %d\n"
- "ANE%d: %s: releasing buffer 0x%08X that was never passed back to the user-space client\n"
- "ANE%d: %s: skip cleanup - nothing in the pending queue\n"
- "ANE%d:%s - ANEPowerChangeHandler_gated: Dark Wake ANE_IsPowered=%d\n"
- "ANE%d:%s - ANEPowerChangeHandler_gated: Ignoring message type %u as fFirmwareTimeout=%d fDeInitInProgress=%d\n"
- "ANE%d:%s - ANEPowerChangeHandler_gated: kIOMessageSystemHasPoweredOn ANE_IsPowered=%d\n"
- "ANE%d:%s - ANEPowerChangeHandler_gated: kIOMessageSystemWillNotSleep ANE_IsPowered=%d\n"
- "ANE%d:%s - ANEPowerChangeHandler_gated: kIOMessageSystemWillPowerOn\n"
- "ANE%d:%s - ANEPowerChangeHandler_gated: kIOMessageSystemWillSleep ANE_IsPowered=%d\n"
- "ANE%d:%s - ANEPowerChangeHandler_gated: warning: no target\n"
- "ANE%d:%s - H11ANEIn::Error ReleaseSharedMemorySurface called on surface with no references\n"
- "ANE%d:%s - H11ANEIn::FreeSharedMemorySurface - freed non-persistent shared surface. surface-id=0x%08X, size=0x%016llx, dartMapBase=0x%016llx usage='%c%c%c%c'\n"
- "ANE%d:%s - H11ANEIn::FreeSharedMemorySurface - freed persistent shared surface. surface-id=0x%08X, size=0x%016llx, dartMapBase=0x%016llx usage='%c%c%c%c'\n"
- "ANE%d:%s - H11ANEIn::FreeSharedMemorySurface: # fNonPersistentSharedMemorySurfaces: %d\n"
- "ANE%d:%s - H11ANEIn::SharedMemorySurfaceTargetPhysicalAddressToHostVirtualAddress - Failed to map shared memory descriptor\n"
- "ANE%d:%s - Ignoring unsuppported notification, and not scheduling on work-loop, messageType=0x%x\n"
- "ANE%d:%s - Ignoring unsuppported notification, and not scheduling on work-loop, messageType=0x%x p->changeFlags=0x%x p->fromCapabilities=0x%x p->toCapabilities=0x%x\n"
- "ANE%d:%s - Moved non-persistent shared surface into pending list due to fSleepInProgress = true. surface-id=0x%08X, size=%016llx, dartMapBase=%016llx usage='%c%c%c%c'\n"
- "ANE%d:%s - No capability parameters\n"
- "ANE%d:%s - moved peer shared surface into pending list due to fSleepInProgress = true. surface-id=0x%08X, size=0x%016llx, dartMapBase=0x%016llx usage='%c%c%c%c'\n"
- "ANE%d:%s - moved persistent shared surface into pending list due to fSleepInProgress = true. surface-id=0x%08X, size=0x%016llx, dartMapBase=0x%016llx usage='%c%c%c%c'\n"
- "ANE%d:%s : Forcing driver initiated sleep in kIOMessageSystemWillSleep call\n"
- "ANE%d:%s: H11ANEIn::ERROR commandArgs is NULL in fOutstandingCommands osset\n"
- "ANE%d:%s: H11ANEIn::ERROR data %p not present in fOutstandingCommands osset\n"
- "ANE%d:%s: Wait for ISP Client going away.. and ISP has camDisableTimeouts=1 \n"
- "ANE%d:%s: client: %s, powerAssertion: %d, isClosed: %d\n"
- "ANE%d:%s:SendRequestToFirmware %d, checkFwCpuThrottled: %d\n"
- "ANE_ExclaveCycle"
- "ANE_ExclaveEvaluate"
- "ANE_ExclaveLoad"
- "ANE_ExclaveUnload"
- "H11ANEIn:: AppleH11ANEDrv::DriverInitiatedSleepTimerTimeOut\n"
- "H11ANEIn:: Passing a -1 value for driver initiated sleep timer period, ignoring\n"
- "H11ANEIn:: Passing a 0 value for driver initiated sleep timer period, disabling sleep timer\n"
- "H11ANEIn::Function:%s, line: %d, ANE_PowerOnByKernelClient timeout\n"
- "aneExclaveEvaluate"
- "aneExclaveLoad"
- "aneExclaveUnload"

```

>  `com.apple.driver.AppleH16CameraInterface`

```diff

-2.403.0.0.0
-  __TEXT.__const: 0x9ef0
-  __TEXT.__cstring: 0x165f5
-  __TEXT.__os_log: 0x132ea
-  __TEXT_EXEC.__text: 0x7fb5c
+2.602.0.0.0
+  __TEXT.__const: 0x9fb0
+  __TEXT.__cstring: 0x18d42
+  __TEXT.__os_log: 0x14f6a
+  __TEXT_EXEC.__text: 0x85a18
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x248
-  __DATA.__common: 0x318
-  __DATA.__bss: 0x220
-  __DATA_CONST.__auth_got: 0x838
-  __DATA_CONST.__got: 0x1b8
+  __DATA.__common: 0x470
+  __DATA.__bss: 0x1f8
+  __DATA_CONST.__auth_got: 0x888
+  __DATA_CONST.__got: 0x1c8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__mod_init_func: 0x90
+  __DATA_CONST.__mod_init_func: 0x88
   __DATA_CONST.__mod_term_func: 0x48
-  __DATA_CONST.__const: 0x7a08
-  __DATA_CONST.__kalloc_type: 0x1140
-  __DATA_CONST.__kalloc_var: 0xcd0
-  Functions: 1036
+  __DATA_CONST.__const: 0x8848
+  __DATA_CONST.__kalloc_type: 0x1280
+  __DATA_CONST.__kalloc_var: 0xd70
+  Functions: 1165
   Symbols:   0
-  CStrings:  2956
+  CStrings:  3256
 
CStrings:
+ "  %4d: surface-id=%#08X, task: %p, refCount=%u\n"
+ "  %4u:  channel:%u, type:%u, filesize:%u surfacesize:%llu surface-id:%#08X, dartMapBase=%#llX\n"
+ "  %4u:  channel:%u, type:%u, filesize:%u surfacesize:%llu surface-id:%#08X, dartMapBase=%#llX (EarlyBoot)\n"
+ "\"AppleH16CamIn::%s: Failed to allocate IOBMD for extra heap, size = 0x%llX\\n\" @%s:%d"
+ "\"AppleH16CamIn::%s: timed out waiting for the EC to power off\\n\" @%s:%d"
+ "\"AppleH16CamIn::%s: timed out waiting for the EC to power on\\n\" @%s:%d"
+ "\"AppleH16CamIn::H16ISPSharedMemorySurfaces::%s - Failed to map shared memory descriptor (IOSurface size: %llu, DART address: %#08X)\\n\" @%s:%d"
+ "\"AppleH16CamIn::H16ISPSharedMemorySurfaces::%s - allocation failure: %#08X\" @%s:%d"
+ "\"ISP didnt power-up cleanly\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->getcmdexclavependingoncrashhandling != NULL) && \\\"implementation for getCmdExclavePendingOnCrashHandling is not present\\\"\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->getcmdexclavepowerstate != NULL) && \\\"implementation for getCmdExclavePowerState is not present\\\"\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->getdeviceid != NULL) && \\\"implementation for getDeviceID is not present\\\"\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->sendcmdforcereset != NULL) && \\\"implementation for sendCmdForceReset is not present\\\"\" @%s:%d"
+ "111111112211211112112221122222221121"
+ "1211111111211122222121221"
+ "121111121222121211211111111111222122222222212122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222"
+ "121112111"
+ "1212112112121112121112121112121112121112121111222222222222222222221211212222111222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221111111111111222"
+ "121212"
+ "12211112"
+ "122121111211"
+ "122211"
+ "12228"
+ "1222822"
+ "12228221"
+ "2222222222221"
+ "AppleH16CamIn:%s - %s: EC did not cleanup after a conclave crash\n\n"
+ "AppleH16CamIn:%s - - CISP_CMD_CIL_BREAKER_ACTIVATED , cilStatus = %d, fidStatus = %d\n"
+ "AppleH16CamIn:%s - - Could not allocate a message queue\n"
+ "AppleH16CamIn:%s - AE Resume IDL failed\n"
+ "AppleH16CamIn:%s - AE Suspend IDL failed\n"
+ "AppleH16CamIn:%s - Could not allocate a message queue lock\n"
+ "AppleH16CamIn:%s - Could not allocate an IOBMD for [%s] of size 0x%llX\n"
+ "AppleH16CamIn:%s - Could not allocate memory for exclave client\n"
+ "AppleH16CamIn:%s - Could not create Exclave IOWorkLoop\n"
+ "AppleH16CamIn:%s - Could not force power off the EC, proceeding to disable mappers, tberr = 0x%x\n\n"
+ "AppleH16CamIn:%s - Could not get a Exclave EPIPE0 mapper\n"
+ "AppleH16CamIn:%s - Could not get a Exclave EPIPE1 mapper\n"
+ "AppleH16CamIn:%s - Could not get a Exclave PIODMA0 mapper\n"
+ "AppleH16CamIn:%s - Could not get a Exclave PIODMA1 mapper\n"
+ "AppleH16CamIn:%s - Could not look up IOSurface with ID %#08x\n"
+ "AppleH16CamIn:%s - Could not make memory visible to ISP\n"
+ "AppleH16CamIn:%s - Could not map the [%s] IOBMD memory descriptor, size 0x%llX\n"
+ "AppleH16CamIn:%s - Could not power off Exclave core, proceeding to disable mappers, tberr = 0x%x result = %d\n"
+ "AppleH16CamIn:%s - Could not power off the EC, result = 0x%x\n"
+ "AppleH16CamIn:%s - Could not power on the EC, result = 0x%x\n"
+ "AppleH16CamIn:%s - Couldn't add H16ISPExclaveEventSource to Exclave IOWorkLoop\n"
+ "AppleH16CamIn:%s - Couldn't add command gate to exclave work loop.\n"
+ "AppleH16CamIn:%s - Couldn't add isp interrupt event source to exclave work loop\n"
+ "AppleH16CamIn:%s - Couldn't create H16ISPExclaveEventSource\n"
+ "AppleH16CamIn:%s - Couldn't create command gate for exclaves\n"
+ "AppleH16CamIn:%s - DVA = 0x%llx, pVisibleMemory = %p\n"
+ "AppleH16CamIn:%s - Default triplets loaded in clocking table\n"
+ "AppleH16CamIn:%s - EC HWIRQ IDL returned an error: req passed = %d ipcRet = %d, tberr = 0x%x\n\n"
+ "AppleH16CamIn:%s - EC did not complete force reset\n\n"
+ "AppleH16CamIn:%s - Exclave Algo not defined/supported\n"
+ "AppleH16CamIn:%s - Exclaves not supported in the kernel\n"
+ "AppleH16CamIn:%s - ISP Engine sendcmdon IDL call failed\n"
+ "AppleH16CamIn:%s - ISP_CILRequestPerChannel got a wrong CH ID (%u/%u)\n"
+ "AppleH16CamIn:%s - Invalid Exclave AE Runkit, channel %d\n"
+ "AppleH16CamIn:%s - Invalid arguments\n"
+ "AppleH16CamIn:%s - Invalid buffer\n"
+ "AppleH16CamIn:%s - Less than %d triplets were found\n"
+ "AppleH16CamIn:%s - Loading default triplet bank\n"
+ "AppleH16CamIn:%s - Memory map failed: 0x%08X\n"
+ "AppleH16CamIn:%s - Memory map failed: 0x%08x\n"
+ "AppleH16CamIn:%s - No valid new data from RGB Face detection(ANST), ipcRet %d isValid %d\n"
+ "AppleH16CamIn:%s - Not enough memory for exclaveData\n"
+ "AppleH16CamIn:%s - Primary selection failed due to a zero count\n"
+ "AppleH16CamIn:%s - Sending Peridot clock banks to FW - res: 0x%08X\n"
+ "AppleH16CamIn:%s - Sent Exclave AE gain: channel=%u, exposure time=%u, agc=%u, ispgain=%u, sensorgain=%u, tag=%u, framerate=%u, TBErr=%U\n"
+ "AppleH16CamIn:%s - Sent Exclave AE max framerate: channel=%u, max framerate=%u TBErr=%U\n"
+ "AppleH16CamIn:%s - Sent Exclave AE max integration time: channel=%u, max time=%u(us) TBErr=%U\n"
+ "AppleH16CamIn:%s - Sent Exclave AE min framerate: channel=%u, min framerate=%u TBErr=%U\n"
+ "AppleH16CamIn:%s - Sent Exclave AE resume: channel=%u, TBErr=%U\n"
+ "AppleH16CamIn:%s - Sent Exclave AE set gain cap: channel=%u, gaincap=%u TBErr=%U\n"
+ "AppleH16CamIn:%s - Sent Exclave AE suspend: channel=%u, TBErr=%U\n"
+ "AppleH16CamIn:%s - Sent Exclave HWIRQ: TBErr=%U\n"
+ "AppleH16CamIn:%s - Sent Exclave Property Read: channel=%u, property=%u TBErr=%U\n"
+ "AppleH16CamIn:%s - Sent Exclave Property Write: channel=%u, property=%u, value=%u, TBErr=%U\n"
+ "AppleH16CamIn:%s - Sent Exclave off: TBErr=%U\n"
+ "AppleH16CamIn:%s - Sent Exclave on: TBErr=%U\n"
+ "AppleH16CamIn:%s - Sent exclave flicker freqset command: freq = %u, confidence = %hu, luxlvl = %.3f, luxvalid = %u, TBErr=%U\n"
+ "AppleH16CamIn:%s - Setting up isp interrupt event source for exclaves failed\n"
+ "AppleH16CamIn:%s - Statistics: NonPersistentMemory:%llu, PersistentMemory:%llu, DeletionPendingMemory:%llu, NonPersistentMemoryMax:%llu, PersistentMemoryMax:%llu\n"
+ "AppleH16CamIn:%s - Statistics: NonPersistentMemory:%llu, PersistentMemory:%llu, DeletionPendingMemory:%llu, NonPersistentMemoryMax:%llu, PersistentMemoryMax:%llu, NumJetsamTriggeredISPDeInits:%llu\n"
+ "AppleH16CamIn:%s - This platform doesn't support Exclave (fPlatformType:%x)\n"
+ "AppleH16CamIn:%s - Timed out waiting for Final EC clean up to complete\n\n"
+ "AppleH16CamIn:%s - Timed out waiting for Initial EC clean up to complete\n\n"
+ "AppleH16CamIn:%s - Unable to get memory descriptor\n"
+ "AppleH16CamIn:%s - Unable to map exclave buffer memory desc\n"
+ "AppleH16CamIn:%s - Unable to run ISP Manager, channel %d\n"
+ "AppleH16CamIn:%s - Unable to set AE Gain Cap\n"
+ "AppleH16CamIn:%s - Unable to set AE Max Integration Time\n"
+ "AppleH16CamIn:%s - Unable to set Exclave AE Min FPS\n"
+ "AppleH16CamIn:%s - Unable to set Exclave AE manual settings\n"
+ "AppleH16CamIn:%s - Uninitialized message queue lock\n"
+ "AppleH16CamIn:%s - [%s:%d] [CIL] Force to turn off CIL (fCILRequestStatus:0x%x)\n"
+ "AppleH16CamIn:%s - [Exclaves] Core power on status: %d exclaves enabled: %d fKextEKSupportEnabled: %d fIsExclaveCoreChannelActive: %d\n"
+ "AppleH16CamIn:%s - [Exclaves] Exclave is already initialized\n"
+ "AppleH16CamIn:%s - [Exclaves] ISP Engine failed HWIRQ\n"
+ "AppleH16CamIn:%s - [Exclaves] ISP_InitializeExclave took %lld usec\n\n"
+ "AppleH16CamIn:%s - [Exclaves] Return fExclaveEnabled=%d\n\n"
+ "AppleH16CamIn:%s - [Exclaves] RunKit FD IDL call failed\n"
+ "AppleH16CamIn:%s - [Exclaves] Set fExclaveEnabled to false\n\n"
+ "AppleH16CamIn:%s - [Exclaves] Set fExclaveEnabled to true\n\n"
+ "AppleH16CamIn:%s - [Exclaves] fExclaveEnabledPlatform = %s / fExclaveInitializationStatus = %u / fKextEKSupportEnabled = %s\n"
+ "AppleH16CamIn:%s - [Exclaves] fExclaveInitializationStatus: COMPLETE\n"
+ "AppleH16CamIn:%s - [Exclaves] fExclaveInitializationStatus: FAIL\n"
+ "AppleH16CamIn:%s - bypassing panic, disabled by boot-args\n"
+ "AppleH16CamIn:%s - driver CIL shutdown enable: %d\n"
+ "AppleH16CamIn:%s - enableExclave = %d\n"
+ "AppleH16CamIn:%s - exclaveStart failed\n"
+ "AppleH16CamIn:%s - exclaves_sensor_start(CAM) returned error (ret:0x%x / status:%u)\n"
+ "AppleH16CamIn:%s - exclaves_sensor_start(FACEID) returned error (ret:0x%x / status:%u)\n"
+ "AppleH16CamIn:%s - exclaves_sensor_stop(CAM) returned error (ret:0x%x / status:%u)\n"
+ "AppleH16CamIn:%s - exclaves_sensor_stop(FACEID) returned error (ret:0x%x / status:%u)\n"
+ "AppleH16CamIn:%s - fNonPersistentSharedMemoryIOBMDs count: %d\n"
+ "AppleH16CamIn:%s - fSharedMemorySurfaces.deletionPendingList count: %u\n"
+ "AppleH16CamIn:%s - fSharedMemorySurfaces.nonPersistentList count: %u\n"
+ "AppleH16CamIn:%s - fSharedMemorySurfaces.pFirmwareSurfaceParams->virtualAddress is NULL.\n"
+ "AppleH16CamIn:%s - fSharedMemorySurfaces.persistentList count: %u\n"
+ "AppleH16CamIn:%s - failed to call ISP_CILRequestPerChannel error: 0x%08X (%u/false)\n"
+ "AppleH16CamIn:%s - init IDL call failed\n"
+ "AppleH16CamIn:%s - memory allocation fail on pChannels[%d].fExclaveConfigs, allocation size=%d\n"
+ "AppleH16CamIn:%s - result=0x%08X\n"
+ "AppleH16CamIn:%s - ret=%#x, surfaceID=%u, size=%llu, dartMapBase=%#llx\n"
+ "AppleH16CamIn:%s - rtb_recoverable_ap_panics is %s\n"
+ "AppleH16CamIn:%s - sendcmdexclavechpropertyread IDL call failed\n"
+ "AppleH16CamIn:%s - sendcmdexclavechpropertywrite IDL call failed\n"
+ "AppleH16CamIn:%s - tb_endpoint is null\n"
+ "AppleH16CamIn:%s - timed out waiting for the EC to power off\n\n"
+ "AppleH16CamIn:%s - timed out waiting for the EC to power on\n\n"
+ "AppleH16CamIn:%s - total non-persistent IOBMD allocation size: %u\n"
+ "AppleH16CamIn:%s - unable to get virtual mapped address\n"
+ "AppleH16CamIn::H16ISPSharedMemorySurfaces:%s - %sfreeing %s shared surface. surface-id=%#08X, size=%llu, dartMapBase=%#llX, fSystemSleepInProgress=%d, fIsDartActive=%d\n"
+ "AppleH16CamIn::H16ISPSharedMemorySurfaces:%s - Failed to get shared memory buffer memory descriptor\n"
+ "AppleH16CamIn::H16ISPSharedMemorySurfaces:%s - Failed to map shared memory descriptor\n"
+ "AppleH16CamIn::H16ISPSharedMemorySurfaces:%s - Memory map failed: %#08X\n"
+ "AppleH16CamIn::H16ISPSharedMemorySurfaces:%s - Shared memory region mapped at DART translated address: %#llX, visible memory: %p\n"
+ "AppleH16CamIn::H16ISPSharedMemorySurfaces:%s - Successfully allocated surface. surface-id=%#08X, surface address: 0x%p, size=%llu, dartMapBase=%#llX\n"
+ "AppleH16CamIn::H16ISPSharedMemorySurfaces:%s - called with NULL pointer, nothing to free\n"
+ "AppleH16CamIn::H16ISPSharedMemorySurfaces:%s - creating kernel mapping for surface %d, usage='%c%c%c%c'\n"
+ "AppleH16CamIn::H16ISPSharedMemorySurfaces:%s - failed to allocate shared memory surface\n"
+ "AppleH16CamIn::H16ISPSharedMemorySurfaces:%s - freed deletionPending shared surface. surface-id=%#08X, size=%llu, dartMapBase=%#llX\n"
+ "AppleH16CamIn::H16ISPSharedMemorySurfaces:%s - in CTRR region: physicalAddress: %llu, fFWCTRRMemSurface.physicalAddress: %llu, size: %#llxn\n"
+ "AppleH16CamIn::H16ISPSharedMemorySurfaces:%s - usable mapped memory exceeds surface boundary!\n"
+ "AppleH16CamIn::client_log_buffer_t:%s - Could not map memory for logging database\n\n"
+ "AppleH16CamIn::client_log_buffer_t:%s - Could not obtain IOMemoryDescriptor for IOSurface with ID %#x\n\n"
+ "AppleH16CamIn::client_log_buffer_t:%s - Could not obtain physical memory address for IOSurface with ID %#x\n\n"
+ "AppleH16CamIn::client_log_buffer_t:%s - IOSurface ID %#x has insufficient size: %#zx bytes\n\n"
+ "AppleH16CamIn::client_log_buffer_t:%s - Unable to lock surface - %#x\n\n"
+ "AppleH16CamIn::releaseSurface:%s - Error: called on surface %#x with no references\n"
+ "AppleH16CamInFrameReceiver:%s - failed to call ISP_CILManager error: 0x%08X (true/false)\n"
+ "AppleH16CamInFrameReceiver:%s - failed to call ISP_CILManager error: 0x%08X (true/true)\n"
+ "AppleH16Camin:%s - Exclave Core Channel is stopped, skipping sending metadata!\n"
+ "AppleH16PearlCam:%s - Error: Failed to create PearlSUR Unwrap output dict: %#x\n"
+ "AppleH16PearlCam:%s - Error: Failed to create PowerOn response dict: %#x\n"
+ "AppleH16PearlCam:%s - Error: Invalid unwrap input!\n"
+ "CreatePearlSURUnwrapOutputDictionary"
+ "CreatePowerOnResponseDictionary"
+ "Deferred "
+ "H16ISPClientMappedSurface"
+ "H16ISPClientMappedSurfaceArray"
+ "H16ISPExclaveEventSource"
+ "H16ISPExclaveEventSource:%s - Could not get a message queue lock, exiting\n"
+ "H16ISPExclaveEventSource:%s - Could not get a pointer to the exclave client, exiting\n"
+ "H16ISPExclaveEventSource:%s - Could not get the exclave message queue, exiting\n"
+ "H16ISPExclaveEventSource:%s - Not enabled, exiting\n"
+ "H16ISPExclaveEventSource:%s - [Exclaves] Unable to send sensor metadata to EC\n"
+ "H16ISPExclaveEventSource:%s - thread=%p\n"
+ "H16ISPMPMMemoryParamArray"
+ "H16ISPMPMMemoryParams"
+ "H16ISPSharedMemorySurfaceParamArray"
+ "H16ISPSharedMemorySurfaceParams"
+ "ISP_CILManager_gated"
+ "ISP_ExclaveAEResume_gated"
+ "ISP_ExclaveAESetAEGain_gated"
+ "ISP_ExclaveAESetGainCap_gated"
+ "ISP_ExclaveAESetMaxFrameRate_gated"
+ "ISP_ExclaveAESetMaxIntegrationTime_gated"
+ "ISP_ExclaveAESetMinFrameRate_gated"
+ "ISP_ExclaveAESuspend_gated"
+ "ISP_ExclaveSetFlickerFrequency_gated"
+ "ISP_GetExclaveEnablementStatus_gated"
+ "ISP_InitializeExclave"
+ "ISP_PowerOffExclaveCore_gated"
+ "ISP_PowerOnExclaveCore_gated"
+ "ISP_ReadPropertyValueExclave_gated"
+ "ISP_RunAlgorithm_gated"
+ "ISP_SecureStreamConfig_gated"
+ "ISP_WritePropertyValueExclave_gated"
+ "J717"
+ "J718"
+ "J720"
+ "J721"
+ "OSValueObject<H16CamInChannelDataFileParams>"
+ "OSValueObject<H16ISPExclaveMessage>"
+ "OSValueObject<H16ISPOverrideNVMParams>"
+ "PearlCamPearlSURDataString_SensorNonce"
+ "PearlCamPearlSURDataString_SensorTag"
+ "PearlCamPearlSURDataString_UnwrapOutputData"
+ "PearlCamPearlSURDataString_UnwrapOutputIV"
+ "PearlCamPearlSURDataString_UnwrapOutputMac"
+ "PearlCamPowerOnDataString_SensorNonce"
+ "PearlCamPowerOnOptionsString_GetSensorNonce"
+ "PearlCamPowerOnOptionsString_SkipFDRCheck"
+ "PearlCamStartOptionsString_HostSignature"
+ "PearlCamStartOptionsString_HostTag"
+ "PearlCamStartOptionsString_UnwrapInputData"
+ "PearlCamStartOptionsString_UnwrapInputIV"
+ "PearlCamStartOptionsString_UnwrapInputMac"
+ "T2030"
+ "[%s:%d] [CIL] CH:%u / faceId:%d / enabled:%d / prevStatus0x%08x\n"
+ "[%s:%d] [CIL] Call ISP_CILManager (%u/false/false)\n"
+ "[%s:%d] [CIL] Call ISP_CILManager (true/false)\n\n"
+ "[%s:%d] [CIL] Call ISP_CILManager (true/true)\n\n"
+ "[%s:%d] [CIL] Finished exclaves_sensor_start(CAM) (ret:0x%x / status:%u)\n"
+ "[%s:%d] [CIL] Finished exclaves_sensor_start(FACEID) (ret:0x%x / status:%u)\n"
+ "[%s:%d] [CIL] Finished exclaves_sensor_stop(CAM) (ret:0x%x / status:%u)\n"
+ "[%s:%d] [CIL] Finished exclaves_sensor_stop(FACEID) (ret:0x%x / status:%u)\n"
+ "[%s:%d] [CIL] prevStatus:0x%08x / Updated fCILRequestStatus:0x%08x\n"
+ "allocateIOBMD"
+ "allocateSurface"
+ "camEnableCILShutdown"
+ "camEnableExclave"
+ "client_log_buffer_t"
+ "com.apple.driver.AppleH16CameraInterface.NonPersistentIOBMD"
+ "exclave-assigned"
+ "exclaveIspInterruptHandler"
+ "exp"
+ "fDeletionPendingSharedMemoryTotalSize = %llu (%u allocations)\n"
+ "fNonPersistentSharedMemoryIOBMDTotalSize = %llu (%u allocations)\n"
+ "freeDeletionPendingAllocations"
+ "freeSurface"
+ "isp:44,24"
+ "makeMemoryVisible"
+ "non-persistent"
+ "persistent"
+ "releaseSurface"
+ "resetCILRequest"
+ "rtb_recoverable_ap_panics"
+ "sendMessageToExclaveWorkLoop"
+ "signalDoorbell"
+ "site.H16ISPClientMappedSurface"
+ "site.H16ISPClientMappedSurfaceArray"
+ "site.H16ISPExclaveEventSource"
+ "site.H16ISPMPMMemoryParamArray"
+ "site.H16ISPMPMMemoryParams"
+ "site.H16ISPSharedMemorySurfaceParamArray"
+ "site.H16ISPSharedMemorySurfaceParams"
+ "site.client_log_buffer_t"
+ "site.exclavecoreispeng_ispengexclavecore"
+ "site.sCIspExclaveCameraConfig"
+ "targetPhysicalAddressToHostVirtualAddress"
- "  %4d: surface-id=0x%08X, task: %p, refCount=%u\n"
- "  %4u:  channel:%u, type:%u, filesize:%u surfacesize:%llu surface-id:0x%08X, dartMapBase=0x%llX\n"
- "  %4u:  channel:%u, type:%u, filesize:%u surfacesize:%llu surface-id:0x%08X, dartMapBase=0x%llX (EarlyBoot)\n"
- "\"AppleH16CamIn::%s - Failed to map shared memory descriptor (IOSurface size: %llu, DART address: 0x%08X)\\n\" @%s:%d"
- "\"AppleH16CamIn::AllocateSharedMemorySurface() - allocation failure: 0x%08X\" @%s:%d"
- "\"ISP didnt power-up cleanly, PS regs: \\n ISP_SYS_PS = 0x%x \\n\" \"ISP_CPU_PS = 0x%x \\n \" \"ISP_CORE0_PS = 0x%x \\n\" \"ISP_CORE1_PS = 0x%x \\n\" \"ISP_FE_PS = 0x%x \\n\" \"ISP_DPRX_PS = 0x%x \\n\" \"ISP_SECURE_PS = 0x%x \\n\" \"ISP_STS0_PS = 0x%x\\n\" \"ISP_STS1_PS = 0x%x \\n\" \"ISP_PEARL_PS = 0x%x \\n\" \"ISP_BE_PS = 0x%x \\n\" \"ISP_CLR_PS = 0x%x \\n\" \"ISP_CVD_PS = 0x%x \\n\" \"ISP_CVM_PS = 0x%x \\n\" @%s:%d"
- "1111111122112111212221122222221121"
- "12111111112211222212122"
- "12111112122212121121111111111122212222222221212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222"
- "1211121111"
- "1212"
- "121211211212111212111212111212111212111212111122222222222222222222121121222211222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221111122"
- "211112"
- "21211112"
- "2211"
- "AllocateSharedMemorySurface"
- "AppleH16CamIn:%s -  failed to allocate shared memory surface, kIOReturnNoMemory\n"
- "AppleH16CamIn:%s - Could not look up IOSurface with ID 0x%08x\n"
- "AppleH16CamIn:%s - Could not map memory for logging database\n"
- "AppleH16CamIn:%s - Could not obtain IOMemoryDescriptor for IOSurface with ID 0x%08x\n"
- "AppleH16CamIn:%s - Could not obtain physical memory address for IOSurface with ID 0x%08x\n"
- "AppleH16CamIn:%s - Deferred freeing of non-persistent shared surface. surface-id=0x%08X, size=%llu, dartMapBase=0x%llX, fSystemSleepInProgress=%d, fIsDartActive=%d\n"
- "AppleH16CamIn:%s - Error: called on surface with no references\n"
- "AppleH16CamIn:%s - Error: outputBuffer retain count is zero\n"
- "AppleH16CamIn:%s - Failed to get shared memory buffer memory descriptor\n"
- "AppleH16CamIn:%s - Failed to map shared memory descriptor\n"
- "AppleH16CamIn:%s - FreeSharedMemorySurfaceWithParams with NULL pointer, nothing to free\n"
- "AppleH16CamIn:%s - IOSurface ID 0x%08x has insufficient size: 0x%08lx bytes\n"
- "AppleH16CamIn:%s - Primary SAC PRI/PLL index selection returned kIOReturnNotFound -- recalling with default indices\n"
- "AppleH16CamIn:%s - Shared memory  region mapped at DART translated address: %#0llX\n"
- "AppleH16CamIn:%s - Statistics: NonPersistentMemory:%llu, PersistentMemory:%llu, DeletionPendingMemory:%d, NonPersistentMemoryMax:%llu, PersistentMemoryMax:%llu\n"
- "AppleH16CamIn:%s - Statistics: NonPersistentMemory:%llu, PersistentMemory:%llu, DeletionPendingMemory:%d, NonPersistentMemoryMax:%llu, PersistentMemoryMax:%llu, NumJetsamTriggeredISPDeInits:%llu\n"
- "AppleH16CamIn:%s - Successfully allocated surface. surface-id=0x%08X, surface address: 0x%p, size=%llu, dartMapBase=0x%llX\n"
- "AppleH16CamIn:%s - creating kernel mapping for surface %d, usage='%c%c%c%c'\n"
- "AppleH16CamIn:%s - dartMapMemoryDescriptor failed\n"
- "AppleH16CamIn:%s - dartMapMemoryDescriptor status=0x%08x\n"
- "AppleH16CamIn:%s - fDeletionPendingMemorySurfaces count: %u\n"
- "AppleH16CamIn:%s - fNonPersistentSharedMemorySurfaces count: %u\n"
- "AppleH16CamIn:%s - fPersistentSharedMemorySurfaces count: %u\n"
- "AppleH16CamIn:%s - failed to allocate shared memory surface\n"
- "AppleH16CamIn:%s - freed deletionPending shared surface. surface-id=0x%08X, size=%llu, dartMapBase=0x%llX\n"
- "AppleH16CamIn:%s - freed non-persistent shared surface. surface-id=0x%08X, size=%llu, dartMapBase=0x%llX\n"
- "AppleH16CamIn:%s - freed persistent shared surface failed, 0x%x\n"
- "AppleH16CamIn:%s - freed persistent shared surface. surface-id=0x%08X, size=%llu, dartMapBase=0x%llX\n"
- "AppleH16CamIn:%s - in CTRR region: physicalAddress: %llu, fFWCTRRMemSurface.physicalAddress: %llu, size: 0x%llxn\n"
- "AppleH16CamIn:%s - pFirmwareSharedMemorySurfaceParams->virtualAddress is NULL.\n"
- "AppleH16CamIn:%s - ret=%#x, surfaceID=%u, size=%llu, dart-Address=%#llx\n"
- "AppleH16CamIn:%s - usable mapped memory exceeds surface boundary!\n"
- "FreeDeletionPendingAllocations"
- "FreeSharedMemorySurface"
- "FreeSharedMemorySurfaceWithParams"
- "OSValueObject<H16ISP::client_log_buffer_t>"
- "OSValueObject<H16ISPClientMappedSurface>"
- "OSValueObject<H16ISPMPMMemoryParams>"
- "OSValueObject<H16ISPSharedMemorySurfaceParams>"
- "PearlCamEventSource:%s - disable\n"
- "PearlCamEventSource:%s - enable\n"
- "PearlCamEventSource:%s - free\n"
- "PearlCamEventSource:%s - initWithOptions\n"
- "PearlCamEventSource:%s - initWithOptions - Error: could not init base object\n"
- "PearlCamEventSource:%s - initWithOptions - Error: provider is not AppleH16PearlCam\n"
- "ReleaseSharedMemorySurface"
- "SharedMemorySurfaceTargetPhysicalAddressToHostVirtualAddress"
- "fDeletionPendingSharedMemoryTotalSize = %u (%u allocations)\n"
- "site.H16ISPOverrideNVMParams"

```

>  `com.apple.driver.AppleHIDTransportFIFO`

```diff

-7140.3.0.0.0
+7141.1.0.0.0
   __TEXT.__cstring: 0x2c86
   __TEXT.__const: 0x8
-  __TEXT_EXEC.__text: 0x16754
+  __TEXT_EXEC.__text: 0x16848
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0xd8

```

>  `com.apple.driver.AppleHPM`

```diff

-540.100.5.0.0
+540.120.2.0.0
   __TEXT.__cstring: 0x18257
   __TEXT.__os_log: 0x1e8
   __TEXT.__const: 0x60
-  __TEXT_EXEC.__text: 0x4d11c
+  __TEXT_EXEC.__text: 0x4d114
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x6d0
   __DATA.__common: 0x518

```

>  `com.apple.driver.AppleInputDeviceSupport`

```diff

-7140.3.0.0.0
-  __TEXT.__cstring: 0x153f
+7141.1.0.0.0
+  __TEXT.__cstring: 0x1540
   __TEXT.__const: 0x48
   __TEXT.__os_log: 0x63a
-  __TEXT_EXEC.__text: 0x1335c
+  __TEXT_EXEC.__text: 0x13238
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x2e0

   __DATA_CONST.__const: 0x30f8
   __DATA_CONST.__kalloc_type: 0x580
   __DATA_CONST.__kalloc_var: 0x2d0
-  Functions: 287
+  Functions: 284
   Symbols:   0
   CStrings:  279
 
CStrings:
+ "1212112"
- "122112"

```

>  `com.apple.driver.AppleMobileDispH16P-DCP`

```diff

-337.5.36.0.0
-  __TEXT.__cstring: 0x5455
+337.7.12.5.0
+  __TEXT.__cstring: 0x54c2
   __TEXT.__const: 0x1a90
-  __TEXT_EXEC.__text: 0x1fb50
+  __TEXT_EXEC.__text: 0x1fc00
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x298
+  __DATA.__data: 0x2b0
   __DATA.__common: 0xf8
   __DATA.__bss: 0x1
   __DATA_CONST.__auth_got: 0x700
   __DATA_CONST.__got: 0xe0
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
-  __DATA_CONST.__const: 0x3bf8
+  __DATA_CONST.__const: 0x3c28
   __DATA_CONST.__kalloc_type: 0x580
   __DATA_CONST.__kalloc_var: 0xf0
   Functions: 495
   Symbols:   0
-  CStrings:  496
+  CStrings:  500
 
CStrings:
+ "121111121222121212121222222222222111111111111121111111111111222211111122222222222222211222211222222222222221111122221222222122222222222112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211222112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222111111111111111111111111111111111111122222222222221222222222222122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222111111111111111111111111111111111111122222222222221222222222222121111111111112111222111122222222222222222222222222222222222221121122222222222222222222222222222111111111121211111122111122112222222222222222222222222222222222222222222222222222222222222222222222222222222221"
+ "1211111212221212121212222222222221111111111111211111111111112222111111222222222222222112222112222222222222211111222212222221222222222221122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222112221122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221111111111111111111111111111111111111222222222222212222222222221222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221111111111111111111111111111111111111222222222222212222222222221211111111111121112221111222222222222222222222222222222222222211211222222222222222222222222222221111111111212111111221111221122222222222222222222222222222222222222222222222222222222222222222222222222222222211111112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222111112222222221"
+ "IOMFBIndicatorBrightnessNits"
+ "IOMFBSecureContentFactor"
+ "IOMFBSecureIndicatorFactor"
+ "iomfb_pending_poweron_sched"
- "121111121222121212121222222222222111111111111211111111111112222111111222222222222222112222112222222222222212111122221222222122222222222112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211222112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222111111111111111111111111111111111111122222222222221222222222222122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222111111111111111111111111111111111111122222222222221222222222222121111111111112111222111122222222222222222222222222222222222221121122222222222222222222222222222111111111121211111122111122112222222222222222222222222222222222222222222222222222222222222222222222222222222221"
- "1211111212221212121212222222222221111111111112111111111111122221111112222222222222221122221122222222222222121111222212222221222222222221122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222112221122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221111111111111111111111111111111111111222222222222212222222222221222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221111111111111111111111111111111111111222222222222212222222222221211111111111121112221111222222222222222222222222222222222222211211222222222222222222222222222221111111111212111111221111221122222222222222222222222222222222222222222222222222222222222222222222222222222222211111112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222111112222222221"

```

>  `com.apple.driver.AppleMultitouchDriver`

```diff

-7140.17.0.0.0
+7150.1.0.0.0
   __TEXT.__const: 0x1b8
-  __TEXT.__cstring: 0x21f5
-  __TEXT.__os_log: 0x303a
-  __TEXT_EXEC.__text: 0x1d268
+  __TEXT.__cstring: 0x2133
+  __TEXT.__os_log: 0x2f65
+  __TEXT_EXEC.__text: 0x1ce04
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xca
   __DATA.__common: 0x270

   __DATA_CONST.__const: 0x4308
   __DATA_CONST.__kalloc_var: 0x280
   __DATA_CONST.__kalloc_type: 0x780
-  Functions: 339
+  Functions: 337
   Symbols:   0
-  CStrings:  517
+  CStrings:  510
 
CStrings:
+ "12111222"
- "121111222"
- "[AMDTimestampSyncMgr::%s]: Prepopulated timestamp sync %u received with timestamp %ums"
- "[AMDTimestampSyncMgr::%s]: Timestamp sync disabled. Informing downstream users"
- "[HID] [%s] %s Prepopulated timestamp sync %u received with timestamp %ums\n"
- "[HID] [%s] %s Timestamp sync disabled. Informing downstream users\n"
- "[HID] [%s] [Error] %s runAction for syncDisabledGated returned 0x%08X\n"
- "interest"
- "syncDisabledGated"

```

>  `com.apple.driver.ApplePMGR`

```diff

-1374.100.73.0.0
+1374.120.11.0.0
   __TEXT.__const: 0x250
-  __TEXT.__cstring: 0xdb6c
-  __TEXT_EXEC.__text: 0x4fcf4
+  __TEXT.__cstring: 0xdc05
+  __TEXT_EXEC.__text: 0x5028c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x100
-  __DATA.__common: 0x3a8
+  __DATA.__common: 0x3d0
   __DATA.__bss: 0x40
   __DATA_CONST.__auth_got: 0x378
   __DATA_CONST.__got: 0xd0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
-  __DATA_CONST.__const: 0x62a8
-  __DATA_CONST.__kalloc_type: 0x5c0
+  __DATA_CONST.__const: 0x63e0
+  __DATA_CONST.__kalloc_type: 0x600
   __DATA_CONST.__kalloc_var: 0xdc0
-  Functions: 1458
+  Functions: 1470
   Symbols:   0
-  CStrings:  1490
+  CStrings:  1495
 
CStrings:
+ "ApplePMGRFunctionReconfigTrigger"
+ "UInt32 ApplePMGR::_getCIOClusterIndex(DeviceID)"
+ "_cioClusterData"
+ "cio-cluster"
+ "site.ApplePMGRFunctionReconfigTrigger"
+ "void ApplePMGR::_waitForCioClusterCompleteGated(UInt64, UInt32, UInt32, bool)"
- "void ApplePMGR::_waitForCioClusterCompleteGated(UInt64, UInt32, UInt32)"

```

>  `com.apple.driver.ApplePearlSEPDriver`

```diff

-673.100.17.0.0
+673.120.3.0.0
   __TEXT.__const: 0x268
-  __TEXT.__cstring: 0x839b
-  __TEXT.__os_log: 0x3ca3
-  __TEXT_EXEC.__text: 0x355c4
+  __TEXT.__cstring: 0x83ca
+  __TEXT.__os_log: 0x3cd9
+  __TEXT_EXEC.__text: 0x35788
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc6
   __DATA.__common: 0x1d8

   __DATA_CONST.__kalloc_var: 0x1e0
   Functions: 350
   Symbols:   0
-  CStrings:  1354
+  CStrings:  1356
 
CStrings:
+ "%s: Enabling/disabling device clock failed, err:0x%x\n"
+ "deviceIDObj && (deviceIDObj->getLength() == 2)"

```

>  `com.apple.driver.AppleSARService`

```diff

-1006.0.0.0.0
+1053.0.0.0.0
   __TEXT.__const: 0x720
   __TEXT.__cstring: 0x2975
   __TEXT.__os_log: 0x74d6
   __TEXT.__ustring: 0x8
-  __TEXT_EXEC.__text: 0x3208c
+  __TEXT_EXEC.__text: 0x3207c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd0
   __DATA.__common: 0x5e8

```

>  `com.apple.driver.AppleSEPKeyStore`

```diff

-1655.102.1.0.0
-  __TEXT.__cstring: 0x3973
+1655.120.10.0.0
+  __TEXT.__cstring: 0x3974
   __TEXT.__const: 0x814
-  __TEXT_EXEC.__text: 0x3b65c
+  __TEXT_EXEC.__text: 0x3b698
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x378
   __DATA.__common: 0xe8
CStrings:
+ "07:28:44"
+ "1655.120.10"
+ "May  2 2024"
- "00:00:55"
- "1655.102.1"
- "Mar  9 2024"

```

>  `com.apple.driver.AppleSEPManager`

```diff

-774.100.29.0.0
-  __TEXT.__cstring: 0xf0ec
+774.120.7.0.0
+  __TEXT.__cstring: 0xf132
   __TEXT.__const: 0x63e0
-  __TEXT_EXEC.__text: 0x442e4
+  __TEXT_EXEC.__text: 0x4432c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x168
   __DATA.__common: 0xc48

   __DATA_CONST.__kalloc_var: 0x50
   Functions: 1783
   Symbols:   0
-  CStrings:  1325
+  CStrings:  1327
 
CStrings:
+ "%s: SEP info: 0x%x\n"
+ "void AppleSEPControl::_cmsgAction(void *, void *)"

```

>  `com.apple.driver.AppleSMC`

```diff

-689.100.12.0.0
-  __TEXT.__cstring: 0x75ff
+689.120.3.0.0
+  __TEXT.__cstring: 0x75bd
   __TEXT.__const: 0x1a4
   __TEXT.__os_log: 0x20f
-  __TEXT_EXEC.__text: 0x240a8
+  __TEXT_EXEC.__text: 0x23ff0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x3f8

   __DATA_CONST.__kalloc_var: 0xa0
   Functions: 478
   Symbols:   0
-  CStrings:  869
+  CStrings:  867
 
CStrings:
+ "20:23:08"
+ "20:23:10"
+ "May  1 2024"
- "23:50:59"
- "23:51:01"
- "AppleSMC detected kPanicEnd\n"
- "AppleSMC kPanicEnd MBSE failed (%s)\n"
- "Mar  8 2024"

```

>  `com.apple.driver.AppleSPMI`

```diff

-87.100.7.0.0
+87.120.2.0.0
   __TEXT.__const: 0x98
-  __TEXT.__cstring: 0x2889
-  __TEXT_EXEC.__text: 0x8fbc
+  __TEXT.__cstring: 0x214a
+  __TEXT_EXEC.__text: 0x90dc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0xd8

   __DATA_CONST.__got: 0x40
   __DATA_CONST.__mod_init_func: 0x28
   __DATA_CONST.__mod_term_func: 0x28
-  __DATA_CONST.__const: 0x31a8
+  __DATA_CONST.__const: 0x31f8
   __DATA_CONST.__kalloc_type: 0x140
   __DATA_CONST.__kalloc_var: 0x230
-  Functions: 97
+  Functions: 98
   Symbols:   0
-  CStrings:  232
+  CStrings:  235
 
CStrings:
+ "0x%08X,0x%08X,0x%08X\n"
+ "12111112122212121111122212111112122212222211121222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211211222222211212"
+ "1211111212221212111112221211111212221222221112122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221121122222221121222222222222222212222122"
+ "12111112122212121111122212111112122212222211121222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211211222222211212222222222222222122222122"
+ "121111121222121211111222121111121222122222111212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222112112222222112122222222222222221222221222222"
+ "12111112122212121111122212111112122212222211121222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211211222222211212222222222222222122222222"
+ "Copied %d entries\n"
+ "Not enough space %0x < %0lx\n"
+ "losesPowerInSleep"
- "0x%08X,0x%08lX,0x%08X\n"
- "12111112122212121111121222111112122212222211121222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211211222222211212"
- "1211111212221212111112122211111212221222221112122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221121122222221121222222222222222212222122"
- "12111112122212121111121222111112122212222211121222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211211222222211212222222222222222122222122"
- "121111121222121211111212221111121222122222111212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222112112222222112122222222222222221222221222222"
- "12111112122212121111121222111112122212222211121222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211211222222211212222222222222222122222222"

```

>  `com.apple.driver.AppleSPMIPMU`

```diff

-1345.0.0.0.0
+1345.120.2.0.0
   __TEXT.__cstring: 0x24d1
   __TEXT.__const: 0x26
-  __TEXT_EXEC.__text: 0xbd6c
+  __TEXT_EXEC.__text: 0xbd54
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x320
   __DATA.__common: 0xc0
CStrings:
+ "%s::handleStart: %s _pmuNub: %p ** configuration not found ** built 07:20:44 May  2 2024\n"
+ "%s::handleStart: ro=%d nvram=%d helper=%d %s _pmuNub: %p 0x%04x:0x%04x-0x%04x built 07:20:44 May  2 2024\n"
+ "%s::start: %s _pmuNub: %p ** configuration not found ** built 07:20:45 May  2 2024\n"
+ "%s::start: %s _pmuNub: %p built 07:20:45 May  2 2024\n"
- "%s::handleStart: %s _pmuNub: %p ** configuration not found ** built 23:03:35 Mar  8 2024\n"
- "%s::handleStart: ro=%d nvram=%d helper=%d %s _pmuNub: %p 0x%04x:0x%04x-0x%04x built 23:03:35 Mar  8 2024\n"
- "%s::start: %s _pmuNub: %p ** configuration not found ** built 23:03:35 Mar  8 2024\n"
- "%s::start: %s _pmuNub: %p built 23:03:35 Mar  8 2024\n"

```

>  `com.apple.driver.AppleT8110DART`

```diff

-417.100.13.0.0
+417.120.2.0.0
   __TEXT.__const: 0x60
   __TEXT.__cstring: 0x2758
-  __TEXT_EXEC.__text: 0xcf04
+  __TEXT_EXEC.__text: 0xcf18
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x38

```

>  `com.apple.driver.AppleT8130CLPC`

```diff

-994.100.46.0.0
-  __TEXT.__cstring: 0x2b21
-  __TEXT.__const: 0xad0
-  __TEXT_EXEC.__text: 0x46a84
+994.120.9.0.0
+  __TEXT.__cstring: 0x2b20
+  __TEXT.__const: 0xaf0
+  __TEXT_EXEC.__text: 0x46c54
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x92e8
-  __DATA.__common: 0x6e11
+  __DATA.__data: 0x9428
+  __DATA.__common: 0x7291
   __DATA.__bss: 0x268
   __DATA_CONST.__auth_got: 0x4a8
   __DATA_CONST.__got: 0xd8
   __DATA_CONST.__mod_init_func: 0x110
   __DATA_CONST.__mod_term_func: 0x18
-  __DATA_CONST.__const: 0x4990
+  __DATA_CONST.__const: 0x4a08
   __DATA_CONST.__kalloc_type: 0x380
   __DATA_CONST.__kalloc_var: 0x370
-  Functions: 646
+  Functions: 648
   Symbols:   0
   CStrings:  449
 
CStrings:
+ "2024-05-02T07:22:42-07:00"
+ "AppleCLPC-994.120.9"
- "2024-03-08T23:58:14-08:00"
- "AppleCLPC-994.100.46"

```

>  `com.apple.driver.AppleTriStar`

```diff

-208.0.0.0.0
+209.0.0.0.0
   __TEXT.__const: 0x8f4
-  __TEXT.__cstring: 0x2afb
+  __TEXT.__cstring: 0x2ff4
   __TEXT.__os_log: 0x25d
-  __TEXT_EXEC.__text: 0x1c8f0
+  __TEXT_EXEC.__text: 0x1da4c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x248
   __DATA.__common: 0x270
-  __DATA_CONST.__auth_got: 0x278
+  __DATA_CONST.__auth_got: 0x280
   __DATA_CONST.__got: 0xd0
   __DATA_CONST.__auth_ptr: 0x20
   __DATA_CONST.__mod_init_func: 0x48
   __DATA_CONST.__mod_term_func: 0x48
-  __DATA_CONST.__const: 0x5c40
+  __DATA_CONST.__const: 0x5cd0
   __DATA_CONST.__kalloc_type: 0x340
-  Functions: 284
+  Functions: 289
   Symbols:   0
-  CStrings:  344
+  CStrings:  380
 
CStrings:
+ "%s::%s: %s: AppleCBTL1614::assertPowerGateEnable error code: 0x%x description: %s\n"
+ "%s::%s: %s: AppleCBTL1614::disableOscillator error code: 0x%x description: %s\n"
+ "%s::%s: %s: AppleCBTL1614::enterTestMode error code: 0x%x description: %s\n"
+ "%s::%s: %s: AppleCBTL1614::forcePowerGateEnable %d error code: 0x%x retries: %d %d %d\n"
+ "%s::%s: %s: AppleCBTL1614::forcePowerGateEnable %d error description: %s\n"
+ "%s::%s: %s: AppleCBTL1614::forcePowerGateEnable %d start idBusTimeout: %d\n"
+ "%s::%s: %s: AppleCBTL1614::forcePowerGateEnable %d success retries: %d %d %d\n"
+ "121111121222121211111121111121222222221122111111121221111222222122221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211222222212222222222222222122222222211222122222122222221222221222222221222221122"
+ "121111121222121211111121111121222222221122111111121221111222222122221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211222222212222222222222222122222222211222122222122222221222221222222221222221122111111111111111111111122211121222"
+ "AssertPowerGateEnableError"
+ "DisableOscillatorError"
+ "EnterTestModeError"
+ "Failed all overall retries"
+ "Failed all power gate enable retries"
+ "Failed all test mode entry retries"
+ "Failed assert power gate enable"
+ "Failed check oscillator disable"
+ "Failed check power gate enable"
+ "Failed check status"
+ "Failed check tm"
+ "Failed enable tm"
+ "Failed oscillator disable"
+ "Failed read revision"
+ "Failed read tm"
+ "Failed revision not set"
+ "Failed setup oscillator disable"
+ "Failed setup power gate enable"
+ "Failed tm entry"
+ "Failed verify power gate enable"
+ "Failed verify tm"
+ "ForcePowerGateEnableError"
+ "ID Bus should not be connected"
+ "Oscillator not disabled"
+ "Power gate enable should be set"
+ "assertPowerGateEnable"
+ "disableOscillator"
+ "enterTestMode"
+ "forcePowerGateEnable"
- "1211111212221212111111211111212222222211221111111212211112222221222212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112222222122222222222222221222222222112221222221222222212222212222221222221122"
- "1211111212221212111111211111212222222211221111111212211112222221222212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112222222122222222222222221222222222112221222221222222212222212222221222221122111111111111111111111122211121222"

```

>  `com.apple.driver.AppleUSBDeviceNCM`

```diff

-341.0.0.0.0
+341.120.1.0.1
   __TEXT.__const: 0x57
   __TEXT.__cstring: 0xaa5
-  __TEXT_EXEC.__text: 0x7794
+  __TEXT_EXEC.__text: 0x779c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x88

```

>  `com.apple.driver.AppleUSBXDCI`

```diff

-785.100.9.0.0
-  __TEXT.__cstring: 0x5929
+785.120.4.0.0
+  __TEXT.__cstring: 0x5949
   __TEXT.__os_log: 0x28b5
   __TEXT.__const: 0x20
-  __TEXT_EXEC.__text: 0x26af8
+  __TEXT_EXEC.__text: 0x26c60
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x100

   __DATA_CONST.__kalloc_var: 0x140
   Functions: 176
   Symbols:   0
-  CStrings:  676
+  CStrings:  678
 
CStrings:
+ "u1-init-disable"
+ "u2-init-disable"

```

>  `com.apple.driver.AppleUSBXDCIARM`

```diff

-785.100.9.0.0
+785.120.4.0.0
   __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x2e49
-  __TEXT.__os_log: 0x3b5a
-  __TEXT_EXEC.__text: 0x2a9b4
+  __TEXT.__cstring: 0x3348
+  __TEXT.__os_log: 0x4424
+  __TEXT_EXEC.__text: 0x30870
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
-  __DATA.__common: 0x178
+  __DATA.__common: 0x1a0
   __DATA_CONST.__auth_got: 0x2d8
   __DATA_CONST.__got: 0xc0
-  __DATA_CONST.__mod_init_func: 0x40
-  __DATA_CONST.__mod_term_func: 0x40
-  __DATA_CONST.__const: 0x4a50
-  __DATA_CONST.__kalloc_type: 0x200
-  Functions: 157
+  __DATA_CONST.__mod_init_func: 0x48
+  __DATA_CONST.__mod_term_func: 0x48
+  __DATA_CONST.__const: 0x5390
+  __DATA_CONST.__kalloc_type: 0x240
+  Functions: 176
   Symbols:   0
-  CStrings:  256
+  CStrings:  261
 
CStrings:
+ "12111112122212121112122222212212222112121111111212222212221122222222211111121111111111111111111111111111111122211111111121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121221122222221222112122112111111111111212111111"
+ "AppleT8132USBXDCI"
+ "AppleT8132USBXDCI.cpp"
+ "site.AppleT8132USBXDCI"
+ "tunable_AUSBC_DEBUG_DEFAULT"

```

>  `com.apple.driver.DCPAVFamilyProxy`

```diff

-283.100.41.0.0
+283.120.9.0.1
   __TEXT.__const: 0x270
   __TEXT.__cstring: 0x23fd
   __TEXT.__os_log: 0x1252
-  __TEXT_EXEC.__text: 0x16dc4
+  __TEXT_EXEC.__text: 0x16df0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x308

```

>  `com.apple.driver.ExclavesAudioKext`

```diff

-140.36.0.0.0
+146.11.0.0.0
   __TEXT.__const: 0x78
   __TEXT.__cstring: 0x2b35
   __TEXT.__os_log: 0x438
-  __TEXT_EXEC.__text: 0x5de4
+  __TEXT_EXEC.__text: 0x5f1c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60

```

>  `com.apple.driver.RTBuddy`

```diff

-550.100.35.0.1
-  __TEXT.__cstring: 0x95a9
-  __TEXT.__const: 0x238
-  __TEXT_EXEC.__text: 0x40074
+550.120.14.0.0
+  __TEXT.__cstring: 0x9b77
+  __TEXT.__const: 0x280
+  __TEXT_EXEC.__text: 0x41b60
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x128
-  __DATA.__common: 0xb20
+  __DATA.__common: 0xb48
   __DATA_CONST.__auth_got: 0x4c8
   __DATA_CONST.__got: 0x148
-  __DATA_CONST.__mod_init_func: 0x140
-  __DATA_CONST.__mod_term_func: 0x140
-  __DATA_CONST.__const: 0xa798
-  __DATA_CONST.__kalloc_type: 0x12c0
+  __DATA_CONST.__mod_init_func: 0x148
+  __DATA_CONST.__mod_term_func: 0x148
+  __DATA_CONST.__const: 0xa958
+  __DATA_CONST.__kalloc_type: 0x1300
   __DATA_CONST.__kalloc_var: 0xf0
-  Functions: 1407
+  Functions: 1442
   Symbols:   0
-  CStrings:  1023
+  CStrings:  1059
 
CStrings:
+ "\n!!!! Unsupported Crashlog info section version %u.%u !!!!\n"
+ "!os_mul_and_add_overflow(sizeof(CrashLogAgentInfo_t), i, sizeof(CrashLogMultiAgentHeader_t), &agent_hdr_offset)"
+ "!os_sub_overflow(_crashlogBufferSize, crashlogOffset, &crashLogBufferSize)"
+ "%s coredump: error = %s\n"
+ "%s coredump: failed to count pages. error = %s\n"
+ "%s coredump: failed to read firmware metadata. error = %s\n"
+ "%s coredump: failed to save data. error = %s\n"
+ "%s coredump: failed to save segment description. error = %s\n"
+ "%s coredump: invalid coredump server version: %llu\n"
+ "%s coredump: server does not support coredump. flags: 0x%llx\n"
+ "0x%016llx"
+ "1211111212221212111211112221111122212222212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211111211111111111111121212222221111"
+ "121111222222222211"
+ "20:23:03"
+ "ASLR slide: %s\n"
+ "Invalid architecture"
+ "Invalid data"
+ "Invalid version"
+ "May  1 2024"
+ "Metadata not cached"
+ "Multilog crash with invalid (short) log length. %u bytes. Minimum valid length is %lu \n"
+ "Multilog crash with invalid header signature: 0x%x, should be 0x%x\n"
+ "Multilog crash with unsupported log (major version: %u, should be %u)\n"
+ "No crashlog entry found in multi-crashlog header\n"
+ "Not ready"
+ "Not supported"
+ "OK"
+ "OSBoundedPtr<const uint8_t> RTBuddyCrashlogDecoder::_multiCrashlogFindFirstCrash(OSBoundedPtr<const uint8_t>, size_t *)"
+ "RTBuddy(%s): cL4 coredump region identified\n"
+ "RTBuddy(%s)::%s: 'crashlog-region' data invalid: %p:%p\n"
+ "RTBuddyCL4Coredump"
+ "Timeout"
+ "_multiCrashlogFindFirstCrash"
+ "coredump-region"
+ "crashlog-region"
+ "crashlogBuffer != nullptr"
+ "setCrashlogBufferAddress"
+ "site.RTBuddyCL4Coredump"
+ "void RTBuddyCrashlogEndpoint::setCrashlogBufferAddress(IOPhysicalAddress, size_t)"
- "00:16:19"
- "121111121222121211121111222111122212222212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211111211111111111111121212222221111"
- "Mar  9 2024"

```

>  `com.apple.driver.mDNSOffloadUserClient-Embedded`

```diff

-119.0.0.0.0
+119.120.1.0.0
   __TEXT.__const: 0x10
   __TEXT.__cstring: 0xd61
-  __TEXT_EXEC.__text: 0x38cc
+  __TEXT_EXEC.__text: 0x37f8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60
   __DATA.__bss: 0x4
-  __DATA_CONST.__auth_got: 0x148
+  __DATA_CONST.__auth_got: 0x150
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__mod_init_func: 0x8
   __DATA_CONST.__mod_term_func: 0x8
   __DATA_CONST.__const: 0x7d8
   __DATA_CONST.__kalloc_type: 0x80
   __DATA_CONST.__kalloc_var: 0xf0
-  Functions: 49
+  Functions: 48
   Symbols:   0
   CStrings:  70
 

```

>  `com.apple.driver.usb.AppleSynopsysUSBXHCI`

```diff

-615.100.5.0.0
-  __TEXT.__cstring: 0x3c3b
-  __TEXT.__os_log: 0x2e8a
+615.120.5.0.0
+  __TEXT.__cstring: 0x3bd4
+  __TEXT.__os_log: 0x2e57
   __TEXT.__const: 0x20
-  __TEXT_EXEC.__text: 0x29e78
+  __TEXT_EXEC.__text: 0x293e4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
-  __DATA.__common: 0x290
+  __DATA.__common: 0x268
   __DATA.__bss: 0x8
   __DATA_CONST.__auth_got: 0x298
   __DATA_CONST.__got: 0x108
-  __DATA_CONST.__mod_init_func: 0x80
-  __DATA_CONST.__mod_term_func: 0x80
-  __DATA_CONST.__const: 0x7378
-  __DATA_CONST.__kalloc_type: 0x480
-  Functions: 287
+  __DATA_CONST.__mod_init_func: 0x78
+  __DATA_CONST.__mod_term_func: 0x78
+  __DATA_CONST.__const: 0x6ad8
+  __DATA_CONST.__kalloc_type: 0x440
+  Functions: 273
   Symbols:   0
-  CStrings:  353
+  CStrings:  348
 
CStrings:
+ "1211111212221212112222222122222222222222222222222222222222222222222222222222212211111222211111111121122222222221112211112221111112"
+ "12111112122212121122222221222222222222222222222222222222222222222222222222222122111112222111111111211222222222211122111122211111121"
+ "1211111212221212112222222122222222222222222222222222222222222222222222222222212211111222211111111121122222222221112211112221111112112"
- "%s@%s: %s::%s: Toggling USB2 phy\n"
- "121111121222121211222222122222222222222222222222222222222222222222222222222212211111222211111111121122222222221112211112221111112"
- "1211111212221212112222221222222222222222222222222222222222222222222222222222122111112222111111111211222222222211122111122211111121"
- "121111121222121211222222122222222222222222222222222222222222222222222222222212211111222211111111121122222222221112211112221111112112"
- "AppleUSB20XHCIARMTypeCPort"
- "resetUSB2Phy"
- "site.AppleUSB20XHCIARMTypeCPort"

```

>  `com.apple.driver.usb.AppleUSBHub`

```diff

-1337.100.4.0.1
+1337.120.6.0.0
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x227c
+  __TEXT.__cstring: 0x227f
   __TEXT.__os_log: 0x2466
   __TEXT_EXEC.__text: 0x28594
   __TEXT_EXEC.__auth_stubs: 0x0
CStrings:
+ "12111112122212121122222221222222222222222222222222222222222222222222222222222122111112222111111111211222222222211122122"
+ "121111121222121211222222212222222222222222222222222222222222222222222222222221221111122221111111112112222222222111221221"
+ "12111112122212121122222221222222222222222222222222222222222222222222222222222122111112222111111111211222222222211122122122"
- "1211111212221212112222221222222222222222222222222222222222222222222222222222122111112222111111111211222222222211122122"
- "12111112122212121122222212222222222222222222222222222222222222222222222222221221111122221111111112112222222222111221221"
- "1211111212221212112222221222222222222222222222222222222222222222222222222222122111112222111111111211222222222211122122122"

```

>  `com.apple.driver.usb.AppleUSBXHCI`

```diff

-1337.100.4.0.1
+1337.120.6.0.0
   __TEXT.__const: 0xc4
-  __TEXT.__cstring: 0x5cfc
-  __TEXT.__os_log: 0x5cb7
-  __TEXT_EXEC.__text: 0x64960
+  __TEXT.__cstring: 0x5da9
+  __TEXT.__os_log: 0x5d61
+  __TEXT_EXEC.__text: 0x64f14
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x428

   __DATA_CONST.__kalloc_var: 0xa0
   Functions: 580
   Symbols:   0
-  CStrings:  903
+  CStrings:  907
 
CStrings:
+ "%s@%s: %s::%s: link change to compliance (PORTSC 0x%08x)\n"
+ "%s@%s: %s::%s: link change to inactive (PORTSC 0x%08x)\n"
+ "%s@%s: %s::%s: the link is still inactive after %d ms. Do a warm reset to transtion the port to RX.Detect (PORTSC 0x%08x)\n"
+ "1211111212221212112222222122222222222222222222222222222222222222222222222222212211111222211111111121122222222221112211112"
+ "12111112122212121122222221222222222222222222222222222222222222222222222222222122111112222111111111211222222222211122111122"
+ "1211111212221212112222222122222222222222222222222222222222222222222222222222212211111222211111111121122222222221112211112221111112"
- "%s@%s: %s::%s: link change to inactive/compliance (PORTSC 0x%08x)\n"
- "121111121222121211222222122222222222222222222222222222222222222222222222222212211111222211111111121122222222221112211112"
- "1211111212221212112222221222222222222222222222222222222222222222222222222222122111112222111111111211222222222211122111122"
- "121111121222121211222222122222222222222222222222222222222222222222222222222212211111222211111111121122222222221112211112221111112"

```

>  `com.apple.filesystems.apfs`

```diff

-2236.102.1.0.0
+2236.122.2.0.0
   __TEXT.__const: 0x6a8
-  __TEXT.__cstring: 0x45892
-  __TEXT_EXEC.__text: 0x12f3c8
+  __TEXT.__cstring: 0x45e95
+  __TEXT_EXEC.__text: 0x130f80
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x688
-  __DATA.__bss: 0xc68
-  __DATA_CONST.__auth_got: 0x1010
+  __DATA.__bss: 0xc60
+  __DATA_CONST.__auth_got: 0x1018
   __DATA_CONST.__got: 0x198
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x10

   __DATA_CONST.__const: 0x5d80
   __DATA_CONST.__kalloc_type: 0x4dc0
   __DATA_CONST.__kalloc_var: 0x2800
-  Functions: 1844
+  Functions: 1855
   Symbols:   0
-  CStrings:  6080
+  CStrings:  6116
 
CStrings:
+ "%s:%d: %s Cannot set speculative download hierarchy for non SAF origin ino %llu\n"
+ "%s:%d: %s Cannot set speculative download hierarchy ino %llu\n"
+ "%s:%d: %s Failed to extract dir stat by key error %s (%d)\n"
+ "%s:%d: %s Failed to extract dir stat chain key error %s (%d)\n"
+ "%s:%d: %s Failed to perform speculative download telemetry ino %llu\n"
+ "%s:%d: %s Failed to perform speculative download telemetry ino %llu error=%s (%d)\n"
+ "%s:%d: %s Failed to set XF INO_EXT_TYPE_SPEC_TELEM_FLAGS ino %llu error %d (%s)"
+ "%s:%d: %s Failed to update inode %llu with speculative download XF error %d (%s)\n"
+ "%s:%d: %s Invalid use_state %d ino %llu\n"
+ "%s:%d: %s Unable to delete XATTR_SPEC_TELEMETRY ino %llu error=%d (%s)\n"
+ "%s:%d: %s Unable to delete XATTR_SPEC_TELEMETRY ino %llu error=%s (%d)\n"
+ "%s:%d: %s Unable to send telemetry event ino %llu error=%s (%d)\n"
+ "%s:%d: %s deny User volume Library chmod to 0%o, ino %llu, pid %d, proc_name [%s], parent_pid %d, parent_proc_name [%s]\n"
+ "%s:%d: %s invalid purge_reason %d\n"
+ "%s:%d: %s pristine age calculation failed with overflow ino %llu\n"
+ "%s:%d: Failed to extract purgeable flags ino %llu error %d (%s)\n"
+ "%s:%d: Failed to extract purgeable size ino %llu error %d (%s)\n"
+ "%s:%d: Unrecognized speculative telemetry request action %d\n"
+ "%s:%d: apfs: speculative telemetry feature ENABLED by boot-arg\n"
+ "2024/05/01"
+ "20:15:58"
+ "20:15:59"
+ "2236.122.2"
+ "Library"
+ "May  1 2024"
+ "apfs-2236.122.2"
+ "apfs_spec_telemetry"
+ "apfs_vnop_allocate"
+ "com.apple.apfs.spec_telemetry"
+ "com.apple.apfs.user_volume_library_chmod"
+ "create_spec_telemetry_xattr"
+ "get_dir_stat_origin_id"
+ "handle_get_spec_telem"
+ "handle_set_unset_spec_telemetry_hierarchy"
+ "handle_spec_telemetry_op"
+ "lookup_purgeable_info"
+ "mode"
+ "parent_pid"
+ "parent_proc_name"
+ "perform_spec_telemetry_locked"
+ "pid"
+ "proc_name"
+ "remove_spec_telemetry_xattr"
+ "send_spec_telemetry_event"
+ "spec_telem_xattr_data_update"
- "%s:%d: %s failed to update spec telemetry xattr for ino %lld with error: %d\n"
- "2024/03/08"
- "2236.102.1"
- "23:03:07"
- "Mar  8 2024"
- "apfs-2236.102.1"
- "apfs: speculative telemetry feature ENABLED by boot-arg\n"
- "lookup_purgeable_flags_and_start_time"
- "update_spec_telem_xattr_with_purge_reason"

```

>  `com.apple.filesystems.lifs`

```diff

-208.100.36.0.3
+208.120.7.0.3
   __TEXT.__os_log: 0x11c5
   __TEXT.__cstring: 0x1d28
   __TEXT.__const: 0x290
-  __TEXT_EXEC.__text: 0x19f38
+  __TEXT_EXEC.__text: 0x19f88
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x5d0
   __DATA.__common: 0x138

```

>  `com.apple.iokit.IOAccessoryManager`

```diff

-971.102.1.0.0
-  __TEXT.__const: 0x318
-  __TEXT.__cstring: 0x1000b
+971.120.5.0.0
+  __TEXT.__const: 0x330
+  __TEXT.__cstring: 0x10212
   __TEXT.__os_log: 0xfd4c
-  __TEXT_EXEC.__text: 0x105288
+  __TEXT_EXEC.__text: 0x1064f0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x7e8
   __DATA.__common: 0x1590

   __DATA_CONST.__auth_ptr: 0x20
   __DATA_CONST.__mod_init_func: 0x328
   __DATA_CONST.__mod_term_func: 0x318
-  __DATA_CONST.__const: 0x28150
+  __DATA_CONST.__const: 0x28190
   __DATA_CONST.__kalloc_type: 0x23c0
-  Functions: 2612
+  Functions: 2618
   Symbols:   0
-  CStrings:  2683
+  CStrings:  2697
 
CStrings:
+ "%s::%s: %s: Requesting accessory name status: 0x%x\n\n"
+ "%s::%s: %s: Sending zone 2 read\n"
+ "%s::%s: %s: Sending zone 2 write\n"
+ "%s::%s: %s: Sent zone 2 read (error code: 0x%x)\n"
+ "%s::%s: %s: Sent zone 2 write (error code: 0x%x)\n"
+ "%s::%s: %s: forcePowerGateEnable: UNSUPPORTED!\n\n"
+ "%s::%s: %s: handleIDBusResponse:%d: RspMGIDWAReadMemory 0x%llx\n\n"
+ "%s::%s: %s: handleIDBusResponse:%d: RspMGIDWAWriteMemory status: 0x%x\n\n"
+ "12111112122212121111112111112122222222112211111112122111122222212222121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122121122222221222222222222222212222222221122212222212222222122222122222222"
+ "12111112122212121111112122222222222222222211222"
+ "MGIDWARetryCount"
+ "MGIDWAState"
+ "acc-pd-wait-retry"
+ "flushFIFO"
+ "forcePowerGateEnable"
+ "handleIDBusCommandForWorkarounds"
- "121111121222121211111121111121222222221122111111121221111222222122221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211222222212222222222222222122222222211222122222122222221222221222222"
- "1211111212221212111111212222222222222222211222"

```

>  `com.apple.iokit.IOHIDFamily`

```diff

-2031.100.16.0.0
-  __TEXT.__cstring: 0x2498
+2031.120.4.0.0
+  __TEXT.__cstring: 0x24b3
   __TEXT.__const: 0x6b8
-  __TEXT.__os_log: 0x28d2
-  __TEXT_EXEC.__text: 0x64f84
+  __TEXT.__os_log: 0x29a0
+  __TEXT_EXEC.__text: 0x65474
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xbcc
   __DATA.__common: 0x748

   __DATA_CONST.__kalloc_type: 0x1480
   Functions: 1105
   Symbols:   0
-  CStrings:  632
+  CStrings:  636
 
CStrings:
+ "%s:0x%llx Client does not have entitlement: %s\n\n"
+ "%s:0x%llx Insufficient permissions to access device for PID: %d\n\n"
+ "%s:0x%llx Insufficient permissions to access device for PID: %d, missing entitlement: %s\n\n"
+ "HIDDeviceAccessEntitlement"

```

>  `com.apple.iokit.IOMobileGraphicsFamily`

```diff

-337.5.36.0.0
-  __TEXT.__cstring: 0x8562
-  __TEXT.__const: 0x928
-  __TEXT_EXEC.__text: 0x41c54
+337.7.12.5.0
+  __TEXT.__cstring: 0x87b4
+  __TEXT.__const: 0x938
+  __TEXT_EXEC.__text: 0x420e8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2908
   __DATA.__common: 0x1c9a4
   __DATA.__bss: 0x18
-  __DATA_CONST.__auth_got: 0x5c8
+  __DATA_CONST.__auth_got: 0x5d0
   __DATA_CONST.__got: 0x120
   __DATA_CONST.__mod_init_func: 0x50
   __DATA_CONST.__mod_term_func: 0x50
-  __DATA_CONST.__const: 0x5148
+  __DATA_CONST.__const: 0x5160
   __DATA_CONST.__kalloc_type: 0xac0
-  Functions: 895
+  Functions: 898
   Symbols:   0
-  CStrings:  966
+  CStrings:  983
 
CStrings:
+ "\"IOMFB: swap_wait_gated blocked for more than 5 seconds. Should not happen. Panicking\\n\" @%s:%d"
+ "%s System error: Failure to allocate memory descriptor\n"
+ "%s System error: Failure to prepare memory descriptor\n"
+ "%s System error: Mismatched data size\n"
+ "12111112122212121212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221111111111111111111111111111111111111222222222222212222222222221222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221111111111111111111111111111111111111222222222222212222222222221211111111111111111221111111111111112222222222222222222222222222222222222222221211112111111111111121122222"
+ "122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211111111111111111111111111111111111112111122222222222222221211"
+ "ForceSecureAnimation"
+ "IOMFB %s: swapId = %d, options = 0x%x, noBlock = 0x%x, HPD = %d, DPLink = %d,                    TimingEnable = %d, PowerStates-Cntr = %d, Display =%d\n"
+ "IOMFB: %s:  CommandWake didn't happen even after 5 seconds.                       Seems system in bad state, cancelling swaps\n"
+ "IOMFBIndicatorBrightnessNits"
+ "IOMFBSecureContentFactor"
+ "IOMFBSecureIndicatorFactor"
+ "IRDCFrameMaxResetCount"
+ "IRDCFrameMinResetCount"
+ "IRDCFrameReset"
+ "iomfb_RuntimeProperty_IRDCFrameMaxResetCount"
+ "iomfb_RuntimeProperty_IRDCFrameMinResetCount"
+ "iomfb_RuntimeProperty_IRDCFrameReset"
+ "iomfb_RuntimeProperty_forceSecureAnimationUpdate"
+ "iomfb_RuntimeProperty_indicatorBrightnessNits"
+ "iomfb_RuntimeProperty_secureContentFactor"
+ "iomfb_RuntimeProperty_secureIndicatorFactor"
+ "iomfb_RuntimeProperty_usePodBoostAtRTPLCFDLUT"
+ "usePodBoostAtRTPLCFDLUT"
- "\"%s System error: Failure to prepare memory descriptor\\n\" @%s:%d"
- "\"%s System error: Mismatched data size\\n\" @%s:%d"
- "\"IOMFB: swap_wait_gated blocked for more than timeout. Should not happen. Panicking\\n\" @%s:%d"
- "12111112122212121212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221111111111111111111111111111111111111222222222222212222222222221222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221111111111111111111111111111111111111222222222222212222222222221211111111111111111221111111111111112222222222222222222222222222222222222222221211112111111111111121122222"
- "1222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211111111111111111111111111111111111112111122222222222222221211"
- "IOMFB %s: swapId = %d, options = 0x%x, noBlock = 0x%x, HPD = %d, DPLink = %d,                TimingEnable = %d, PowerStates-Cntr = %d, Display =%d\n"
- "IOMFB: %s:  CommandWake didn't happen even after %d seconds.                Seems system in bad state, cancelling swaps\n"

```

>  `com.apple.iokit.IOMobileGraphicsFamily-DCP`

```diff

-337.5.36.0.0
-  __TEXT.__cstring: 0x443f
-  __TEXT.__const: 0x2389
-  __TEXT_EXEC.__text: 0x41734
+337.7.12.5.0
+  __TEXT.__cstring: 0x4511
+  __TEXT.__const: 0x23a1
+  __TEXT_EXEC.__text: 0x419cc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xf8
   __DATA.__common: 0x26f8
   __DATA.__bss: 0x4e
-  __DATA_CONST.__auth_got: 0x6b8
+  __DATA_CONST.__auth_got: 0x6d0
   __DATA_CONST.__got: 0x138
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x28
   __DATA_CONST.__mod_term_func: 0x28
   __DATA_CONST.__const: 0x1740
   __DATA_CONST.__kalloc_type: 0x880
-  Functions: 818
+  Functions: 826
   Symbols:   0
-  CStrings:  390
+  CStrings:  396
 
CStrings:
+ "%s: Powering off external and powering on Internal from hpd notification\n"
+ "121111121222121212121222222222222111111111111121111111111111222211111122222222222222211222211222222222222221111122221222222122222222222112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211222112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222111111111111111111111111111111111111122222222222221222222222222122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222111111111111111111111111111111111111122222222222221222222222222121111111111112111222111122222222222222222222222222222222222221121122222222222222222222222222222111"
+ "D589_callback__"
+ "get_clamshell_state fAPClamshellState %d from_kernel %d\n"
+ "property doesnt Exists \n"
+ "propertyExists \n"
+ "propertyHas default Value \n"
+ "propertyHas false Value \n"
+ "propertyHas true Value \n"
- "121111121222121212121222222222222111111111111211111111111112222111111222222222222222112222112222222222222212111122221222222122222222222112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211222112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222111111111111111111111111111111111111122222222222221222222222222122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222111111111111111111111111111111111111122222222222221222222222222121111111111112111222111122222222222222222222222222222222222221121122222222222222222222222222222111"
- "D591_callback__"
- "get_clamshell_state fAPClamshellState %d\n"

```

>  `com.apple.iokit.IONVMeFamily`

```diff

-732.100.10.0.0
-  __TEXT.__cstring: 0xf1d0
+732.120.3.0.0
+  __TEXT.__cstring: 0xf4df
   __TEXT.__const: 0x688
-  __TEXT_EXEC.__text: 0x56f68
+  __TEXT_EXEC.__text: 0x580c0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x534
   __DATA.__common: 0x500

   __DATA_CONST.__got: 0x180
   __DATA_CONST.__mod_init_func: 0xf8
   __DATA_CONST.__mod_term_func: 0xf8
-  __DATA_CONST.__const: 0xc040
+  __DATA_CONST.__const: 0xc138
   __DATA_CONST.__kalloc_type: 0x780
   __DATA_CONST.__kalloc_var: 0x5f0
-  Functions: 1008
+  Functions: 1026
   Symbols:   0
-  CStrings:  1663
+  CStrings:  1678
 
CStrings:
+ "\"ANS DevTreeRoot not found !\\n\" @%s:%d"
+ "\"defaultsEntry not found in EDT!\\n\" @%s:%d"
+ "\"pmap_iommu_ioctl - Setting Admin Queue Regs - failed\\n\" @%s:%d"
+ "\"pmap_iommu_ioctl - Setting IOCQ base addr - failed\\n\" @%s:%d"
+ "\"pmap_iommu_ioctl - Setting IOQA base addr - failed\\n\" @%s:%d"
+ "\"pmap_iommu_ioctl - Setting IOSQ base addr - failed\\n\" @%s:%d"
+ "%s::%d:NVMe BAR Workaround required\n"
+ "12111112122212121121111111122122211111111112222112122222222222121111211112222211212221221111111111111111111111111111111122211222122111111111122111211111111111111111111111111111111111111111111111111111111111111112222222222222222222222222222222222211212211211111111111111111211111211112112112122"
+ "1211111212221212112111111112212221111111111222211212222222222212111121111222221121222122111111111111111111111111111111112221122212211111111112211121111111111111111111111111111111111111111111111111111111111111111222222222222222222222222222222222221121221121111111111111111121111121111211211212212"
+ "fSecureBaseAddress"
+ "fSecureBaseRegisterMap"
+ "nvme-iboot-sptm-security"
+ "nvme-secure-bar"
+ "virtual IOReturn AppleANS2CGNVMeController::EnableCompletionQueue(uint16_t)"
+ "virtual IOReturn AppleANS2CGNVMeController::EnableSubmissionQueue(uint16_t)"
+ "virtual IOReturn AppleANS2CGv2Controller::EnableCompletionQueue(uint16_t)"
+ "virtual IOReturn AppleANS2CGv2Controller::EnableSubmissionQueue(uint16_t)"
+ "virtual void AppleANS2NVMeController::CheckEDTProperties()"
- "%s::%d:ANS DevTreeRoot not found !\n"
- "1211111212221212112111111112212221111111111222211212222222222212111121111222221121222122111111111111111111111111111111112221122212211111111112211121111111111111111111111111111111111111111111111111111111111111111222222222222222222222222222222222221121221121111111111111111121111121111211122"
- "121111121222121211211111111221222111111111122221121222222222221211112111122222112122212211111111111111111111111111111111222112221221111111111221112111111111111111111111111111111111111111111111111111111111111111122222222222222222222222222222222222112122112111111111111111112111112111121112212"

```

>  `com.apple.iokit.IOUSBDeviceFamily`

```diff

-785.100.9.0.0
-  __TEXT.__cstring: 0x2835
+785.120.4.0.0
+  __TEXT.__cstring: 0x284e
   __TEXT.__const: 0x88
   __TEXT.__os_log: 0x18bd
-  __TEXT_EXEC.__text: 0x2b23c
+  __TEXT_EXEC.__text: 0x2b2b4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x1f0

   __DATA_CONST.__kalloc_var: 0x190
   Functions: 415
   Symbols:   0
-  CStrings:  446
+  CStrings:  447
 
CStrings:
+ "soft-disconnect-interval"

```

>  `com.apple.iokit.IOUSBHostFamily`

```diff

-1337.100.4.0.1
-  __TEXT.__cstring: 0x98be
-  __TEXT.__os_log: 0x8108
+1337.120.6.0.0
+  __TEXT.__cstring: 0x9912
+  __TEXT.__os_log: 0x814a
   __TEXT.__const: 0xa30
-  __TEXT_EXEC.__text: 0xaaacc
+  __TEXT_EXEC.__text: 0xaad70
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x310
   __DATA.__common: 0x928

   __DATA_CONST.__kalloc_var: 0x280
   Functions: 1171
   Symbols:   0
-  CStrings:  1531
+  CStrings:  1534
 
CStrings:
+ "%s@%s: %s::%s: usb2 port timings are resume: %ums, resumeRecovery: %ums, suspend: %ums, powerOnStabilize: %ums, reset: %ums, resetRecovery: %ums, setAddressRecovery: %ums\n"
+ "%s@%s: %s::%s: usb3 port timings are disconnectDetect: %ums\n"
+ "1211111212221212112222222122222222222222222222222222222222222222222222222222212211111222211111111121122222222221112"
+ "usb3-port-timing"
- "%s@%s: %s::%s: port timings are resume: %ums, resumeRecovery: %ums, suspend: %ums, powerOnStabilize: %ums, reset: %ums, resetRecovery: %ums, setAddressRecovery: %ums\n"
- "121111121222121211222222122222222222222222222222222222222222222222222222222212211111222211111111121122222222221112"

```

>  `com.apple.kec.Compression`

```diff

-169.100.2.0.0
+171.0.0.0.0
   __TEXT.__const: 0x8
-  __TEXT_EXEC.__text: 0x3804
+  __TEXT_EXEC.__text: 0x37dc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xdc
   __DATA_CONST.__auth_got: 0x30

```

>  `com.apple.kernel`

```diff

-10063.102.14.0.0
-  __TEXT.__const: 0x34080
+10063.122.3.0.0
+  __TEXT.__const: 0x340c0
   __TEXT.__copyio_vectors: 0xf0
-  __TEXT.__cstring: 0x652c2
-  __TEXT.__os_log: 0x2289c
+  __TEXT.__cstring: 0x65664
+  __TEXT.__os_log: 0x228f2
   __TEXT.__eh_frame: 0x4c0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x2c0
-  __DATA_CONST.__const: 0xa1bc0
+  __DATA_CONST.__const: 0xa1f98
   __DATA_CONST.__hib_const: 0x140
-  __DATA_CONST.__kalloc_type: 0x12c80
-  __DATA_CONST.__kalloc_var: 0x77b0
+  __DATA_CONST.__kalloc_type: 0x12d00
+  __DATA_CONST.__kalloc_var: 0x7800
   __DATA_CONST.__brk_desc: 0x60
   __DATA_SPTM.__const: 0x3c000
   __TEXT_EXEC.__hib_text: 0xd28
-  __TEXT_EXEC.__text: 0x74cd18
+  __TEXT_EXEC.__text: 0x74cba4
   __TEXT_BOOT_EXEC.__bootcode: 0x4cf8
   __KLD.__text: 0x1644
   __LASTDATA_CONST.__mod_init_func: 0x8

   __KLDDATA.__mod_init_func: 0x8
   __KLDDATA.__mod_term_func: 0x8
   __KLDDATA.__bss: 0x1
-  __DATA.__data: 0x17b29
+  __DATA.__data: 0x17aa9
   __DATA.__lock_grp: 0x5800
   __DATA.__percpu: 0x4e50
   __DATA.__common: 0x577d0
   __DATA.__bss: 0x3d220
   __BOOTDATA.__data: 0x18000
   __BOOTDATA.__init: 0x5b0e8
-  __BOOTDATA.__init_entry_set: 0x100f8
+  __BOOTDATA.__init_entry_set: 0x10230
   __PRELINK_TEXT.__text: 0x0
   __PRELINK_INFO.__info: 0x0
   __PLK_TEXT_EXEC.__text: 0x0

   __PLK_DATA_CONST.__data: 0x0
   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
-  __LINKINFO.__symbolsets: 0x44b08
-  Functions: 19210
+  __LINKINFO.__symbolsets: 0x44bf2
+  Functions: 19223
   Symbols:   0
-  CStrings:  15898
+  CStrings:  15933
 
CStrings:
+ "%s: map %p pmap %p entry %p 0x%llx:0x%llx prot 0x%x @%s:%d"
+ "%s: map %p va 0x%llx obj %p,%u saved %p,%u: unexpected CoW @%s:%d"
+ "%s: pmap %p vaddr 0x%llx prot 0x%x options 0x%x !cs_bypass @%s:%d"
+ "%s: pmap %p vaddr 0x%llx prot 0x%x options 0x%x @%s:%d"
+ "%s: pmap %p vaddr 0x%llx prot 0x%x options 0x%x m%p obj %p copyobj %p @%s:%d"
+ "%s: so %llu [%d,%d] epid %d euuid %s%s %s->%s\n"
+ "%s:%d CLAT46: NEXT ia %s address on ifp1 %s skipped as it is not reserved for CLAT46\n"
+ "%s[%d]: so %llu [%d,%d] epid %llu euuid %s%s event posted\n"
+ "%s[%d]: so %llu [%d,%d] epid %llu euuid %s%s has %d redundant events supressed\n"
+ "/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ip6_id.c"
+ "22222222222222221111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111122221221111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111222222222222222222222222222222"
+ "FEAT_AFP"
+ "FEAT_RPRES"
+ "FEAT_SME"
+ "FEAT_SME2"
+ "FEAT_SME_F64F64"
+ "FEAT_SME_I16I64"
+ "FEAT_WFxT"
+ "IOMemoryDescriptor::makeMapping !64bit @%s:%d"
+ "PAC failure from kernel with %s key while branching to %s"
+ "PAC failure from kernel with %s key while returning"
+ "SME_B16F32"
+ "SME_BI32I32"
+ "SME_F16F32"
+ "SME_F32F32"
+ "SME_I16I32"
+ "SME_I8I32"
+ "audiomxd"
+ "com.apple.developer.cs.jit-write-allowlist"
+ "com.apple.developer.cs.jit-write-allowlist-freeze-late"
+ "com.apple.private.route.iflist.include-clat46"
+ "com.apple.security.fatal-exceptions"
+ "conclave_mem"
+ "invalid jrange value @%s:%d"
+ "jit"
+ "mediaplaybackd"
+ "salt_tmp != 0"
+ "vm_fault_enter_prepare"
+ "vm_map_fork"
+ "vm_map_fork_share"
+ "vm_map_lookup_and_lock_object"
+ "vm_map_remap_extract"
- "%s: so 0x%llx [%d,%d] epid %d euuid %s%s %s->%s\n"
- "%s[%d]: so 0x%llx [%d,%d] epid %llu euuid %s%s event posted\n"
- "%s[%d]: so 0x%llx [%d,%d] epid %llu euuid %s%s has %d redundant events supressed\n"
- "21211"
- "2222222222222222111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111112221221111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111222222222222222222222222222222"
- "map %p va 0x%llx obj %p,%u saved %p,%u: unexpected CoW @%s:%d"
- "v24@?0^{tb_list_node_s=AB^{tb_list_node_s}Q^v@?}8^B16"

```

>  `com.apple.kext.CoreTrust`

```diff

-140.100.1.0.0
-  __TEXT.__const: 0xfc1
+140.120.3.0.0
+  __TEXT.__const: 0xfc9
   __TEXT.__cstring: 0x52
-  __TEXT_EXEC.__text: 0x81e8
+  __TEXT_EXEC.__text: 0x83f4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd8
   __DATA.__common: 0x10

   __DATA_CONST.__got: 0x8
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x14a0
-  Functions: 91
+  Functions: 94
   Symbols:   0
   CStrings:  4
 

```

>  `com.apple.plugin.IOgPTPPlugin`

```diff

-1240.15.0.0.0
-  __TEXT.__cstring: 0x6112
-  __TEXT.__os_log: 0x1a26b
+1250.2.0.0.0
+  __TEXT.__cstring: 0x6101
+  __TEXT.__os_log: 0x1a273
   __TEXT.__const: 0x290
-  __TEXT_EXEC.__text: 0x75ad8
+  __TEXT_EXEC.__text: 0x75b98
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xcc
   __DATA.__common: 0x5d8
-  __DATA_CONST.__auth_got: 0x700
+  __DATA_CONST.__auth_got: 0x708
   __DATA_CONST.__got: 0x1b8
   __DATA_CONST.__mod_init_func: 0x110
   __DATA_CONST.__mod_term_func: 0x110
   __DATA_CONST.__const: 0xeab8
   __DATA_CONST.__kalloc_type: 0x940
   __DATA_CONST.__kalloc_var: 0x280
-  Functions: 928
+  Functions: 929
   Symbols:   0
   CStrings:  1416
 
CStrings:
+ "findMacAddress error %u getting address"
+ "findMacAddress: Failed to find the %s interface"
- "IOTimeSyncgPTPManager::addInterfaceAdapterForInterface error %u getting address"
- "ifnet != nullptr"

```

>  `com.apple.security.AppleImage4`

```diff

-257.100.26.0.0
+257.120.3.0.0
   __TEXT.__const: 0x6ad8
-  __TEXT.__cstring: 0x5180
-  __TEXT_EXEC.__text: 0x20244
+  __TEXT.__cstring: 0x528b
+  __TEXT_EXEC.__text: 0x20464
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x640
   __DATA.__bss: 0x215

   __DATA_CONST.__auth_ptr: 0x20
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0xa960
+  __DATA_CONST.__const: 0xa968
   __DATA_CONST.__kalloc_type: 0x180
   __DATA_CONST.__image4_exp: 0x10
-  Functions: 673
+  Functions: 674
   Symbols:   0
-  CStrings:  679
+  CStrings:  684
 
CStrings:
+ "2211122222222221221222222222222"
+ "257.120.3"
+ "@(#)VERSION:Darwin Image4 Validator Version 6.3.0: Wed May  1 20:13:19 PDT 2024; root:AppleImage4-257.120.3~72/AppleImage4/RELEASE_ARM64E"
+ "Darwin Image4 Validator Version 6.3.0: Wed May  1 20:13:19 PDT 2024; root:AppleImage4-257.120.3~72/AppleImage4/RELEASE_ARM64E"
+ "legacy nonce blob has no Cryptex1 boot nonce: v = %hx, length = %lu"
+ "legacy nonce blob length insufficient: actual = %lu, expected >= %lu"
+ "magazine[%s]: failed retry write of magazine: %d"
+ "magazine[%s]: failed retry write of slot: %d"
+ "magazine[%s]: failed to nuke legacy blob: %d"
+ "magazine[%s]: failed to write priority slot: %d"
+ "magazine[%s]: magazine write failed; may be expected: %d"
- "221122222222221221222222222222"
- "257.100.26"
- "@(#)VERSION:Darwin Image4 Validator Version 6.3.0: Fri Mar  8 23:24:14 PST 2024; root:AppleImage4-257.100.26~253/AppleImage4/RELEASE_ARM64E"
- "Darwin Image4 Validator Version 6.3.0: Fri Mar  8 23:24:14 PST 2024; root:AppleImage4-257.100.26~253/AppleImage4/RELEASE_ARM64E"
- "legacy nonce blob is ancient: length = %u"
- "legacy nonce blob length insufficient: actual = %lu, expected = %lu"

```

>  `com.apple.security.sandbox`

```diff

-2190.100.100.0.0
-  __TEXT.__const: 0x16fcc1
+2190.120.12.0.0
+  __TEXT.__const: 0x171dd9
   __TEXT.__cstring: 0x6549
   __TEXT.__os_log: 0x1cbb
-  __TEXT_EXEC.__text: 0x2e488
+  __TEXT_EXEC.__text: 0x2e4b0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x1e0
   __DATA.__bss: 0x144d0

```

</details>

## MachO

### 🆕 NEW (9)

- `/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices-0002.bundle/MobileDevices-0002`
- `/System/Library/ExtensionKit/Extensions/DevicePropertiesExtension.appex/DevicePropertiesExtension`
- `/System/Library/ExtensionKit/Extensions/PridePosterExtension.appex/PridePosterExtension`
- `/System/Library/Frameworks/HealthKit.framework/PlugIns/com.apple.HealthKit.HealthResearchLogsDiagnosticExtension.appex/com.apple.HealthKit.HealthResearchLogsDiagnosticExtension`
- `/System/Library/NanoTimeKit/FaceBundles/NTKPlumeriaFaceBundleCompanion.bundle/NTKPlumeriaFaceBundleCompanion`
- `/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceEraseXPCService.xpc/Contents/MacOS/FindMyDeviceEraseXPCService`
- `/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceIdentityXPCService.xpc/Contents/MacOS/FindMyDeviceIdentityXPCService`
- `/System/Library/PrivateFrameworks/NewsDaemon.framework/XPCServices/ANFDecoder.xpc/ANFDecoder`
- `/System/Library/PrivateFrameworks/NewsUI2.framework/XPCServices/TodayFeedConfigDecoder.xpc/TodayFeedConfigDecoder`

### ❌ Removed (2)

- `/System/Library/ControlCenter/Bundles/AskToAirDropControlCenterModule.bundle/AskToAirDropControlCenterModule`
- `/System/Library/PrivateFrameworks/PridePoster.framework/PlugIns/PridePosterExtension.appex/PridePosterExtension`

### ⬆️ Updated (652)

<details>
  <summary><i>View Updated</i></summary>

- [/Applications/AirDropUI.app/AirDropUI](MACHOS/AirDropUI.md)
- [/Applications/AirPlaySenderUIApp.app/AirPlaySenderUIApp](MACHOS/AirPlaySenderUIApp.md)
- [/Applications/AppDistributionLaunchAngel.app/AppDistributionLaunchAngel](MACHOS/AppDistributionLaunchAngel.md)
- [/Applications/AppStore.app/AppStore](MACHOS/AppStore.md)
- [/Applications/AppStore.app/PlugIns/AppStoreWidgetsExtension.appex/AppStoreWidgetsExtension](MACHOS/AppStoreWidgetsExtension.md)
- [/Applications/AppStore.app/PlugIns/ProductPageExtension.appex/ProductPageExtension](MACHOS/ProductPageExtension.md)
- [/Applications/AppStore.app/PlugIns/SubscribePageExtension.appex/SubscribePageExtension](MACHOS/SubscribePageExtension.md)
- [/Applications/AskPermissionUI.app/AskPermissionUI](MACHOS/AskPermissionUI.md)
- [/Applications/AskToMessagesHost.app/PlugIns/AskToMessagesExtension.appex/AskToMessagesExtension](MACHOS/AskToMessagesExtension.md)
- [/Applications/AuthenticationServicesUI.app/AuthenticationServicesUI](MACHOS/AuthenticationServicesUI.md)
- [/Applications/CheckerBoardRemoteSetup.app/CheckerBoardRemoteSetup](MACHOS/CheckerBoardRemoteSetup.md)
- [/Applications/CoreAuthUI.app/CoreAuthUI](MACHOS/CoreAuthUI.md)
- [/Applications/Coverage Details.app/Coverage Details](MACHOS/Coverage_Details.md)
- [/Applications/Diagnostics.app/Diagnostics](MACHOS/Diagnostics.md)
- [/Applications/DiagnosticsReporter.app/DiagnosticsReporter](MACHOS/DiagnosticsReporter.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4009-iOS-D83-D84.appex/Diagnostic-4009-iOS-D83-D84](MACHOS/Diagnostic-4009-iOS-D83-D84.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4615.appex/Diagnostic-4615](MACHOS/Diagnostic-4615.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6002.appex/Diagnostic-6002](MACHOS/Diagnostic-6002.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6004.appex/Diagnostic-6004](MACHOS/Diagnostic-6004.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8185.appex/Diagnostic-8185](MACHOS/Diagnostic-8185.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8201.appex/Diagnostic-8201](MACHOS/Diagnostic-8201.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8253.appex/Diagnostic-8253](MACHOS/Diagnostic-8253.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8276.appex/Diagnostic-8276](MACHOS/Diagnostic-8276.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8288.appex/Diagnostic-8288](MACHOS/Diagnostic-8288.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8441.appex/Frameworks/DiagnosticsSupport.framework/DiagnosticsSupport](MACHOS/DiagnosticsSupport.md)
- [/Applications/DiagnosticsService.app/PlugIns/SystemReport-iOS-D83-D84.appex/SystemReport-iOS-D83-D84](MACHOS/SystemReport-iOS-D83-D84.md)
- [/Applications/EventViewService.app/EventViewService](MACHOS/EventViewService.md)
- [/Applications/FMDMagSafeSetupRemoteUI.app/FMDMagSafeSetupRemoteUI](MACHOS/FMDMagSafeSetupRemoteUI.md)
- [/Applications/FTMInternal-4.app/FTMInternal-4](MACHOS/FTMInternal-4.md)
- [/Applications/FindMyExtensionContainer.app/PlugIns/FindMyDeviceBluetoothExtension.appex/FindMyDeviceBluetoothExtension](MACHOS/FindMyDeviceBluetoothExtension.md)
- [/Applications/HDSViewService.app/HDSViewService](MACHOS/HDSViewService.md)
- [/Applications/InCallService.app/InCallService](MACHOS/InCallService.md)
- [/Applications/InCallService.app/PlugIns/IntentsUI.appex/IntentsUI](MACHOS/IntentsUI.md)
- [/Applications/InputUI.app/InputUI](MACHOS/InputUI.md)
- [/Applications/MTLReplayer.app/MTLReplayer](MACHOS/MTLReplayer.md)
- [/Applications/MediaRemoteUI.app/MediaRemoteUI](MACHOS/MediaRemoteUI.md)
- [/Applications/MobilePhone.app/MobilePhone](MACHOS/MobilePhone.md)
- [/Applications/MobilePhone.app/PlugIns/VoicemailMessageNotificationExtension.appex/VoicemailMessageNotificationExtension](MACHOS/VoicemailMessageNotificationExtension.md)
- [/Applications/MobileSMS.app/MobileSMS](MACHOS/MobileSMS.md)
- [/Applications/MobileSMS.app/PlugIns/MobileSMSSpotlightImporter.appex/MobileSMSSpotlightImporter](MACHOS/MobileSMSSpotlightImporter.md)
- [/Applications/MobileSlideShow.app/MobileSlideShow](MACHOS/MobileSlideShow.md)
- [/Applications/MomentsUIService.app/MomentsUIService](MACHOS/MomentsUIService.md)
- [/Applications/PassbookUIService.app/PassbookUIService](MACHOS/PassbookUIService.md)
- [/Applications/PeopleMessageService.app/Extensions/PeopleLegacyMessageService.appex/PeopleLegacyMessageService](MACHOS/PeopleLegacyMessageService.md)
- [/Applications/PeopleMessageService.app/PeopleMessageService](MACHOS/PeopleMessageService.md)
- [/Applications/PeopleMessageService.app/PlugIns/PeopleMessagesAskToBuy.appex/PeopleMessagesAskToBuy](MACHOS/PeopleMessagesAskToBuy.md)
- [/Applications/PeopleMessageService.app/PlugIns/PeopleMessagesScreenTime.appex/PeopleMessagesScreenTime](MACHOS/PeopleMessagesScreenTime.md)
- [/Applications/Preferences.app/Preferences](MACHOS/Preferences.md)
- [/Applications/ProximityReaderSceneUI.app/ProximityReaderSceneUI](MACHOS/ProximityReaderSceneUI.md)
- [/Applications/ReplayKitAngel.app/ReplayKitAngel](MACHOS/ReplayKitAngel.md)
- [/Applications/SIMSetupUIService.app/SIMSetupUIService](MACHOS/SIMSetupUIService.md)
- [/Applications/SOSBuddy.app/SOSBuddy](MACHOS/SOSBuddy.md)
- [/Applications/Screen Time.app/PlugIns/ScreenTimeWidgetExtension.appex/ScreenTimeWidgetExtension](MACHOS/ScreenTimeWidgetExtension.md)
- [/Applications/Screen Time.app/PlugIns/ScreenTimeWidgetIntentsExtension.appex/ScreenTimeWidgetIntentsExtension](MACHOS/ScreenTimeWidgetIntentsExtension.md)
- [/Applications/ScreenshotServicesService.app/ScreenshotServicesService](MACHOS/ScreenshotServicesService.md)
- [/Applications/Setup.app/Setup](MACHOS/Setup.md)
- [/Applications/SharingViewService.app/SharingViewService](MACHOS/SharingViewService.md)
- [/Applications/ShazamEventsApp.app/ShazamEventsApp](MACHOS/ShazamEventsApp.md)
- [/Applications/ShortcutsUI.app/ShortcutsUI](MACHOS/ShortcutsUI.md)
- [/Applications/ShortcutsViewService.app/ShortcutsViewService](MACHOS/ShortcutsViewService.md)
- [/Applications/Sidecar.app/PlugIns/ContinuityDisplay.appex/ContinuityDisplay](MACHOS/ContinuityDisplay.md)
- [/Applications/Siri.app/Siri](MACHOS/Siri.md)
- [/Applications/StickersUltra.app/PlugIns/StickersUltraExtension.appex/StickersUltraExtension](MACHOS/StickersUltraExtension.md)
- [/Applications/StoreKitUIService.app/StoreKitUIService](MACHOS/StoreKitUIService.md)
- [/Applications/TDGSharingViewService.app/TDGSharingViewService](MACHOS/TDGSharingViewService.md)
- [/Applications/iCloud+.app/iCloud+](MACHOS/iCloud+.md)
- [/Library/Audio/Plug-Ins/HAL/VirtualAudio.plugin/VirtualAudio](MACHOS/VirtualAudio.md)
- [/System/DriverKit/usr/lib/system/libsystem_malloc_debug.dylib](MACHOS/libsystem_malloc_debug.dylib.md)
- [/System/DriverKit/usr/lib/system/libsystem_trace_debug.dylib](MACHOS/libsystem_trace_debug.dylib.md)
- [/System/Library/AccessibilityBundles/AXAggregateStatisticsServer.axuiservice/AXAggregateStatisticsServer](MACHOS/AXAggregateStatisticsServer.md)
- [/System/Library/AccessibilityBundles/AssistiveTouch.axuiservice/AssistiveTouch](MACHOS/AssistiveTouch.md)
- [/System/Library/AccessibilityBundles/ClarityUIServer.axuiservice/ClarityUIServer](MACHOS/ClarityUIServer.md)
- [/System/Library/AccessibilityBundles/GAXBackboardServer.bundle/GAXBackboardServer](MACHOS/GAXBackboardServer.md)
- [/System/Library/AccessibilityBundles/GAXClient.bundle/GAXClient](MACHOS/GAXClient.md)
- [/System/Library/AccessibilityBundles/GAXSpringboardServer.bundle/GAXSpringboardServer](MACHOS/GAXSpringboardServer.md)
- [/System/Library/AccessibilityBundles/InvertColorsManager.bundle/InvertColorsManager](MACHOS/InvertColorsManager.md)
- [/System/Library/AccessibilityBundles/SpeakServer.axuiservice/SpeakServer](MACHOS/SpeakServer.md)
- [/System/Library/Accounts/Authentication/AMSAccountAuthenticationPlugin.bundle/AMSAccountAuthenticationPlugin](MACHOS/AMSAccountAuthenticationPlugin.md)
- [/System/Library/AppleMediaServices/DynamicUI/PlugIns/CoreDynamicUIPlugin.bundle/CoreDynamicUIPlugin](MACHOS/CoreDynamicUIPlugin.md)
- [/System/Library/AppleMediaServices/DynamicUI/PlugIns/StoreDynamicUIPlugin.bundle/StoreDynamicUIPlugin](MACHOS/StoreDynamicUIPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/AlarmFlowPlugin.bundle/AlarmFlowPlugin](MACHOS/AlarmFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/AudioFlowDelegatePlugin](MACHOS/AudioFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/DailyBriefingFlowPlugin.bundle/DailyBriefingFlowPlugin](MACHOS/DailyBriefingFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/GeoFlowDelegatePlugin.bundle/GeoFlowDelegatePlugin](MACHOS/GeoFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/HomeCommunicationFlowDelegatePlugin.bundle/HomeCommunicationFlowDelegatePlugin](MACHOS/HomeCommunicationFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/InformationFlowPlugin](MACHOS/InformationFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/PhoneCallFlowDelegatePlugin](MACHOS/PhoneCallFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SiriLinkFlowPlugin.bundle/SiriLinkFlowPlugin](MACHOS/SiriLinkFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/SocialConversationFlowDelegatePlugin](MACHOS/SocialConversationFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/TimerFlowDelegatePlugin.bundle/TimerFlowDelegatePlugin](MACHOS/TimerFlowDelegatePlugin.md)
- [/System/Library/Assistant/Plugins/Applications.assistantBundle/Applications](MACHOS/Applications.md)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriPrivateLearningInferencePlugin.bundle/SiriPrivateLearningInferencePlugin](MACHOS/SiriPrivateLearningInferencePlugin.md)
- [/System/Library/Audio/MIDI Drivers/AppleMIDIUSBDriver.plugin/AppleMIDIUSBDriver](MACHOS/AppleMIDIUSBDriver.md)
- [/System/Library/Audio/MIDI Drivers/YamahaUSBMIDIDriver.plugin/YamahaUSBMIDIDriver](MACHOS/YamahaUSBMIDIDriver.md)
- [/System/Library/Audio/Plug-Ins/HAL/AirPlayHalogen.driver/AirPlayHalogen](MACHOS/AirPlayHalogen.md)
- [/System/Library/Audio/Plug-Ins/HAL/BTAudioHALPlugin.driver/BTAudioHALPlugin](MACHOS/BTAudioHALPlugin.md)
- [/System/Library/Audio/Plug-Ins/HAL/BasebandVoice.driver/BasebandVoice](MACHOS/BasebandVoice.md)
- [/System/Library/Audio/Plug-Ins/HAL/OctaviaHalogen.driver/OctaviaHalogen](MACHOS/OctaviaHalogen.md)
- [/System/Library/ControlCenter/Bundles/AudioConferenceControlCenterModule.bundle/AudioConferenceControlCenterModule](MACHOS/AudioConferenceControlCenterModule.md)
- [/System/Library/ControlCenter/Bundles/ReplayKitModule.bundle/ReplayKitModule](MACHOS/ReplayKitModule.md)
- [/System/Library/CoreServices/AegirProxyApp.app/PlugIns/AegirPoster.appex/AegirPoster](MACHOS/AegirPoster.md)
- [/System/Library/CoreServices/AssistiveTouch.app/assistivetouchd](MACHOS/assistivetouchd.md)
- [/System/Library/CoreServices/BluetoothUIService.app/BluetoothUIService](MACHOS/BluetoothUIService.md)
- [/System/Library/CoreServices/ClarityBoard.app/ClarityBoard](MACHOS/ClarityBoard.md)
- [/System/Library/CoreServices/EscrowSecurityAlert.app/EscrowSecurityAlert](MACHOS/EscrowSecurityAlert.md)
- [/System/Library/CoreServices/OverlayUI.app/OverlayUI](MACHOS/OverlayUI.md)
- [/System/Library/CoreServices/ReportCrash](MACHOS/ReportCrash.md)
- [/System/Library/CoreServices/SafariSupport.bundle/SafariBookmarksSyncAgent](MACHOS/SafariBookmarksSyncAgent.md)
- [/System/Library/CoreServices/VoiceOverTouch.app/vot](MACHOS/vot.md)
- [/System/Library/CoreServices/iconservicesagent](MACHOS/iconservicesagent.md)
- [/System/Library/CoreServices/osanalyticshelper](MACHOS/osanalyticshelper.md)
- [/System/Library/CoreServices/powerd.bundle/powerd](MACHOS/powerd.md)
- [/System/Library/CryptoTokenKit/usbsmartcardreaderd.slotd/usbsmartcardreaderd](MACHOS/usbsmartcardreaderd.md)
- [/System/Library/DataClassMigrators/RestorePostProcess.migrator/RestorePostProcess](MACHOS/RestorePostProcess.md)
- [/System/Library/DataClassMigrators/SpringBoard.migrator/SpringBoard](MACHOS/SpringBoard.md)
- [/System/Library/DigitalSeparation/SharingSources/FindMyItemsDigitalSeparation.bundle/FindMyItemsDigitalSeparation](MACHOS/FindMyItemsDigitalSeparation.md)
- [/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN](MACHOS/com.apple.DriverKit-AppleBCMWLAN.md)
- [/System/Library/ExtensionKit/Extensions/ADFollowUpExtension.appex/ADFollowUpExtension](MACHOS/ADFollowUpExtension.md)
- [/System/Library/ExtensionKit/Extensions/AppStoreEvalLighthouseWorker.appex/AppStoreEvalLighthouseWorker](MACHOS/AppStoreEvalLighthouseWorker.md)
- [/System/Library/ExtensionKit/Extensions/ExperimentationExtension.appex/ExperimentationExtension](MACHOS/ExperimentationExtension.md)
- [/System/Library/ExtensionKit/Extensions/GPUExtension.appex/com.apple.WebKit.GPU](MACHOS/com.apple.WebKit.GPU.md)
- [/System/Library/ExtensionKit/Extensions/MercuryPosterExtension.appex/MercuryPosterExtension](MACHOS/MercuryPosterExtension.md)
- [/System/Library/ExtensionKit/Extensions/MusicEngagementExtension.appex/MusicEngagementExtension](MACHOS/MusicEngagementExtension.md)
- [/System/Library/ExtensionKit/Extensions/NetworkingExtension.appex/com.apple.WebKit.Networking](MACHOS/com.apple.WebKit.Networking.md)
- [/System/Library/ExtensionKit/Extensions/PFLHRPeriodPredCK.appex/PFLHRPeriodPredCK](MACHOS/PFLHRPeriodPredCK.md)
- [/System/Library/ExtensionKit/Extensions/PFLHRPeriodPredPush.appex/PFLHRPeriodPredPush](MACHOS/PFLHRPeriodPredPush.md)
- [/System/Library/ExtensionKit/Extensions/RepackagingWorker.appex/RepackagingWorker](MACHOS/RepackagingWorker.md)
- [/System/Library/ExtensionKit/Extensions/SiriMASPFLPush.appex/SiriMASPFLPush](MACHOS/SiriMASPFLPush.md)
- [/System/Library/ExtensionKit/Extensions/WebContentCaptivePortalExtension.appex/com.apple.WebKit.WebContent.CaptivePortal](MACHOS/com.apple.WebKit.WebContent.CaptivePortal.md)
- [/System/Library/ExtensionKit/Extensions/WebContentExtension.appex/com.apple.WebKit.WebContent](MACHOS/com.apple.WebKit.WebContent.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.mlhost.CloudWorker.appex/com.apple.mlhost.CloudWorker](MACHOS/com.apple.mlhost.CloudWorker.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.mlhost.TelemetryWorker.appex/com.apple.mlhost.TelemetryWorker](MACHOS/com.apple.mlhost.TelemetryWorker.md)
- [/System/Library/Extensions/AppleHPM.kext/PlugIns/AppleHPMLib.plugin/AppleHPMLib](MACHOS/AppleHPMLib.md)
- [/System/Library/Extensions/EXBrightKext.kext/EXBrightKext](MACHOS/EXBrightKext.md)
- [/System/Library/Extensions/lifs.kext/lifs](MACHOS/lifs.md)
- [/System/Library/Filesystems/apfs.fs/apfs.util](MACHOS/apfs.util.md)
- [/System/Library/Filesystems/apfs.fs/apfs_boot_util](MACHOS/apfs_boot_util.md)
- [/System/Library/Filesystems/apfs.fs/apfs_checkseal](MACHOS/apfs_checkseal.md)
- [/System/Library/Filesystems/apfs.fs/apfs_condenser](MACHOS/apfs_condenser.md)
- [/System/Library/Filesystems/apfs.fs/apfs_vol_converter](MACHOS/apfs_vol_converter.md)
- [/System/Library/Filesystems/apfs.fs/fsck_apfs](MACHOS/fsck_apfs.md)
- [/System/Library/Filesystems/apfs.fs/newfs_apfs](MACHOS/newfs_apfs.md)
- [/System/Library/Frameworks/AdAttributionKit.framework/Support/attributionkitd](MACHOS/attributionkitd.md)
- [/System/Library/Frameworks/AssetsLibrary.framework/Support/assetsd](MACHOS/assetsd.md)
- [/System/Library/Frameworks/CallKit.framework/XPCServices/com.apple.CallKit.CallDirectory.xpc/com.apple.CallKit.CallDirectory](MACHOS/com.apple.CallKit.CallDirectory.md)
- [/System/Library/Frameworks/ClassKit.framework/progressd](MACHOS/progressd.md)
- [/System/Library/Frameworks/Contacts.framework/Support/contactsd](MACHOS/contactsd.md)
- [/System/Library/Frameworks/CoreLocationUI.framework/XPCServices/com.apple.corelocation.locationUI.xpc/com.apple.corelocation.locationUI](MACHOS/com.apple.corelocation.locationUI.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlightService](MACHOS/CoreSpotlightService.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/PlugIns/CoreSpotlightImportExtension1_iOS.appex/CoreSpotlightImportExtension1_iOS](MACHOS/CoreSpotlightImportExtension1_iOS.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/PlugIns/CoreSpotlightImportExtension2_iOS.appex/CoreSpotlightImportExtension2_iOS](MACHOS/CoreSpotlightImportExtension2_iOS.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/Support/com.apple.spotlight.IndexAgent](MACHOS/com.apple.spotlight.IndexAgent.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/spotlightknowledged](MACHOS/spotlightknowledged.md)
- [/System/Library/Frameworks/CoreTelephony.framework/PlugIns/CTFollowUpExtension.appex/CTFollowUpExtension](MACHOS/CTFollowUpExtension.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/CTParser.framework/XPCServices/CTParserService.xpc/CTParserService](MACHOS/CTParserService.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenterMobileHelper](MACHOS/CommCenterMobileHelper.md)
- [/System/Library/Frameworks/FileProvider.framework/OverrideBundles/FileProviderOverride.bundle/FileProviderOverride](MACHOS/FileProviderOverride.md)
- [/System/Library/Frameworks/FileProvider.framework/OverrideBundles/iCloudDriveFileProviderOverride.bundle/iCloudDriveFileProviderOverride](MACHOS/iCloudDriveFileProviderOverride.md)
- [/System/Library/Frameworks/FileProvider.framework/PlugIns/LocalStorageFileProvider.appex/LocalStorageFileProvider](MACHOS/LocalStorageFileProvider.md)
- [/System/Library/Frameworks/HealthKit.framework/healthd](MACHOS/healthd.md)
- [/System/Library/Frameworks/HomeKit.framework/PlugIns/HomeKitDiagnosticExtension.appex/HomeKitDiagnosticExtension](MACHOS/HomeKitDiagnosticExtension.md)
- [/System/Library/Frameworks/ImageCaptureCore.framework/XPCServices/mscamerad-xpc.xpc/mscamerad-xpc](MACHOS/mscamerad-xpc.md)
- [/System/Library/Frameworks/ImageIO.framework/XPCServices/ImageIOXPCService.xpc/ImageIOXPCService](MACHOS/ImageIOXPCService.md)
- [/System/Library/Frameworks/Intents.framework/XPCServices/intents_helper.xpc/intents_helper](MACHOS/intents_helper.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismPlugins/MechPushButton.bundle/MechPushButton](MACHOS/MechPushButton.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/ModulePlugins/ModuleACM.bundle/ModuleACM](MACHOS/ModuleACM.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/coreauthd](MACHOS/coreauthd.md)
- [/System/Library/Frameworks/ManagedAppDistribution.framework/Support/applicensedeliveryd](MACHOS/applicensedeliveryd.md)
- [/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond](MACHOS/managedappdistributiond.md)
- [/System/Library/Frameworks/ManagedSettings.framework/ManagedSettingsAgent](MACHOS/ManagedSettingsAgent.md)
- [/System/Library/Frameworks/OSLog.framework/XPCServices/OSLogService.xpc/OSLogService](MACHOS/OSLogService.md)
- [/System/Library/Frameworks/ProximityReader.framework/merchantd](MACHOS/merchantd.md)
- [/System/Library/Frameworks/QuickLookThumbnailing.framework/Support/com.apple.quicklook.ThumbnailsAgent](MACHOS/com.apple.quicklook.ThumbnailsAgent.md)
- [/System/Library/Frameworks/Security.framework/CircleJoinRequested/CircleJoinRequested](MACHOS/CircleJoinRequested.md)
- [/System/Library/Frameworks/Security.framework/XPCServices/TrustedPeersHelper.xpc/TrustedPeersHelper](MACHOS/TrustedPeersHelper.md)
- [/System/Library/Frameworks/SensorKit.framework/XPCServices/SensorKitDataExport.xpc/SensorKitDataExport](MACHOS/SensorKitDataExport.md)
- [/System/Library/Frameworks/SensorKit.framework/XPCServices/SensorKitLongTermStorageHelper.xpc/SensorKitLongTermStorageHelper](MACHOS/SensorKitLongTermStorageHelper.md)
- [/System/Library/Frameworks/Speech.framework/XPCServices/localspeechrecognition.xpc/localspeechrecognition](MACHOS/localspeechrecognition.md)
- [/System/Library/Frameworks/StoreKit.framework/PlugIns/SKAskPermissionExtension.appex/SKAskPermissionExtension](MACHOS/SKAskPermissionExtension.md)
- [/System/Library/Frameworks/StoreKit.framework/Support/storekitd](MACHOS/storekitd.md)
- [/System/Library/Frameworks/SystemConfiguration.framework/SCHelper](MACHOS/SCHelper.md)
- [/System/Library/Frameworks/WebKit.framework/Frameworks/libWebKitSwift.dylib](MACHOS/libWebKitSwift.dylib.md)
- [/System/Library/HIDPlugins/ColourSensorFilterPlugin.plugin/ColourSensorFilterPlugin](MACHOS/ColourSensorFilterPlugin.md)
- [/System/Library/HIDPlugins/ServiceFilters/AppleDeviceManagementHIDFilter.plugin/AppleDeviceManagementHIDFilter](MACHOS/AppleDeviceManagementHIDFilter.md)
- [/System/Library/HIDPlugins/ServiceFilters/AppleProxServiceFilter.plugin/AppleProxServiceFilter](MACHOS/AppleProxServiceFilter.md)
- [/System/Library/HIDPlugins/ServiceFilters/AppleWirelessChargingServiceFilter.plugin/AppleWirelessChargingServiceFilter](MACHOS/AppleWirelessChargingServiceFilter.md)
- [/System/Library/HIDPlugins/ServicePlugins/HSTouchHIDService.plugin/HSTouchHIDService](MACHOS/HSTouchHIDService.md)
- [/System/Library/HIDPlugins/ServicePlugins/IOHIDEventServicePlugin.plugin/IOHIDEventServicePlugin](MACHOS/IOHIDEventServicePlugin.md)
- [/System/Library/HIDPlugins/ServicePlugins/XboxOneHIDServicePlugin.plugin/XboxOneHIDServicePlugin](MACHOS/XboxOneHIDServicePlugin.md)
- [/System/Library/HIDPlugins/SessionFilters/IOAnalytics.plugin/IOAnalytics](MACHOS/IOAnalytics.md)
- [/System/Library/HIDPlugins/SessionFilters/IOHIDMotionEventSessionFilter.plugin/IOHIDMotionEventSessionFilter](MACHOS/IOHIDMotionEventSessionFilter.md)
- [/System/Library/Health/Plugins/HealthRecordsPlugin.bundle/HealthRecordsPlugin](MACHOS/HealthRecordsPlugin.md)
- [/System/Library/Health/Plugins/WorkoutHealthPlugin.bundle/WorkoutHealthPlugin](MACHOS/WorkoutHealthPlugin.md)
- [/System/Library/LocationBundles/AltimeterHarvest.bundle/AltimeterHarvest](MACHOS/AltimeterHarvest.md)
- [/System/Library/LocationBundles/AppGenius.bundle/AppGenius](MACHOS/AppGenius.md)
- [/System/Library/LocationBundles/AppSuggestions.bundle/AppSuggestions](MACHOS/AppSuggestions.md)
- [/System/Library/LocationBundles/CountryTracker.bundle/CountryTracker](MACHOS/CountryTracker.md)
- [/System/Library/LocationBundles/IonosphereHarvest.bundle/IonosphereHarvest](MACHOS/IonosphereHarvest.md)
- [/System/Library/LocationBundles/LocationFenceSync.bundle/LocationFenceSync](MACHOS/LocationFenceSync.md)
- [/System/Library/LocationBundles/LocationPromptUI.bundle/LocationPromptUI](MACHOS/LocationPromptUI.md)
- [/System/Library/LocationBundles/MotionCalibration.bundle/MotionCalibration](MACHOS/MotionCalibration.md)
- [/System/Library/LocationBundles/TimeZone.bundle/TimeZone](MACHOS/TimeZone.md)
- [/System/Library/LocationBundles/Traffic.bundle/Traffic](MACHOS/Traffic.md)
- [/System/Library/Messages/iMessageApps/FindMyMessagesApp.bundle/FindMyMessagesApp](MACHOS/FindMyMessagesApp.md)
- [/System/Library/Messages/iMessageApps/SafetyMonitorMessages.bundle/SafetyMonitorMessages](MACHOS/SafetyMonitorMessages.md)
- [/System/Library/Messages/iMessageBalloons/ASMessagesProvider.bundle/ASMessagesProvider](MACHOS/ASMessagesProvider.md)
- [/System/Library/Messages/iMessageBalloons/MSMessageExtensionBalloonPlugin.bundle/MSMessageExtensionBalloonPlugin](MACHOS/MSMessageExtensionBalloonPlugin.md)
- [/System/Library/NanoPreferenceBundles/Applications/NanoPassbookBridgeSettings.bundle/NanoPassbookBridgeSettings](MACHOS/NanoPassbookBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/OxygenSaturationSettings.bundle/OxygenSaturationSettings](MACHOS/OxygenSaturationSettings.md)
- [/System/Library/NanoPreferenceBundles/Customization/NTKCustomization.bundle/NTKCustomization](MACHOS/NTKCustomization.md)
- [/System/Library/NanoPreferenceBundles/PrivacySettings/HealthBridgePrivacySettings.bundle/HealthBridgePrivacySettings](MACHOS/HealthBridgePrivacySettings.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKActivityFaceBundleCompanion.bundle/NTKActivityFaceBundleCompanion](MACHOS/NTKActivityFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKAlaskanFaceBundleCompanion.bundle/NTKAlaskanFaceBundleCompanion](MACHOS/NTKAlaskanFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKBigNumeralsDigitalFaceBundleCompanion.bundle/NTKBigNumeralsDigitalFaceBundleCompanion](MACHOS/NTKBigNumeralsDigitalFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKChronographFaceBundleCompanion.bundle/NTKChronographFaceBundleCompanion](MACHOS/NTKChronographFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKCollieFaceBundleCompanion.bundle/NTKCollieFaceBundleCompanion](MACHOS/NTKCollieFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKColorAnalogFaceBundleCompanion.bundle/NTKColorAnalogFaceBundleCompanion](MACHOS/NTKColorAnalogFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKColtanFaceBundleCompanion.bundle/NTKColtanFaceBundleCompanion](MACHOS/NTKColtanFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKCrosswindFaceBundleCompanion.bundle/NTKCrosswindFaceBundleCompanion](MACHOS/NTKCrosswindFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKDigitalModularFaceBundleCompanion.bundle/NTKDigitalModularFaceBundleCompanion](MACHOS/NTKDigitalModularFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKExplorerFaceBundleCompanion.bundle/NTKExplorerFaceBundleCompanion](MACHOS/NTKExplorerFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKGladiusFaceBundleCompanion.bundle/NTKGladiusFaceBundleCompanion](MACHOS/NTKGladiusFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKGreyhoundFaceBundleCompanion.bundle/NTKGreyhoundFaceBundleCompanion](MACHOS/NTKGreyhoundFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKInfographFaceBundle.bundle/NTKInfographFaceBundle](MACHOS/NTKInfographFaceBundle.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKKuiperFaceBundleCompanion.bundle/NTKKuiperFaceBundleCompanion](MACHOS/NTKKuiperFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKMargaritaFaceBundleCompanion.bundle/NTKMargaritaFaceBundleCompanion](MACHOS/NTKMargaritaFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKNumeralsAnalogFaceBundleCompanion.bundle/NTKNumeralsAnalogFaceBundleCompanion](MACHOS/NTKNumeralsAnalogFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKOlympusFaceBundleCompanion.bundle/NTKOlympusFaceBundleCompanion](MACHOS/NTKOlympusFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKParameciumFaceBundleCompanion.bundle/NTKParameciumFaceBundleCompanion](MACHOS/NTKParameciumFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKPrideWeaveFaceBundleCompanion.bundle/NTKPrideWeaveFaceBundleCompanion](MACHOS/NTKPrideWeaveFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKSeltzerFaceBundleCompanion.bundle/NTKSeltzerFaceBundleCompanion](MACHOS/NTKSeltzerFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKShibaFaceBundleCompanion.bundle/NTKShibaFaceBundleCompanion](MACHOS/NTKShibaFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKSimpleFaceBundleCompanion.bundle/NTKSimpleFaceBundleCompanion](MACHOS/NTKSimpleFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKSolarsFaceBundleCompanion.bundle/NTKSolarsFaceBundleCompanion](MACHOS/NTKSolarsFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKSpectrumFaceBundleCompanion.bundle/NTKSpectrumFaceBundleCompanion](MACHOS/NTKSpectrumFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKTimelapseFaceBundle.bundle/NTKTimelapseFaceBundle](MACHOS/NTKTimelapseFaceBundle.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKToyStoryFaceBundle.bundle/NTKToyStoryFaceBundle](MACHOS/NTKToyStoryFaceBundle.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKUltraCubeFaceBundleCompanion.bundle/NTKUltraCubeFaceBundleCompanion](MACHOS/NTKUltraCubeFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKUtilityFaceBundleCompanion.bundle/NTKUtilityFaceBundleCompanion](MACHOS/NTKUtilityFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKVictoryDigitalFaceBundleCompanion.bundle/NTKVictoryDigitalFaceBundleCompanion](MACHOS/NTKVictoryDigitalFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKZeusFaceBundleCompanion.bundle/NTKZeusFaceBundleCompanion](MACHOS/NTKZeusFaceBundleCompanion.md)
- [/System/Library/PreferenceBundles/AccessibilitySettings.bundle/AccessibilitySettings](MACHOS/AccessibilitySettings.md)
- [/System/Library/PreferenceBundles/AccessoryDeveloperSettings.bundle/AccessoryDeveloperSettings](MACHOS/AccessoryDeveloperSettings.md)
- [/System/Library/PreferenceBundles/AccountSettings/ActiveSyncSettings.bundle/ActiveSyncSettings](MACHOS/ActiveSyncSettings.md)
- [/System/Library/PreferenceBundles/AccountSettings/AppleAccountSettings.bundle/AppleAccountSettings](MACHOS/AppleAccountSettings.md)
- [/System/Library/PreferenceBundles/AccountSettings/MailAccountSettings.bundle/MailAccountSettings](MACHOS/MailAccountSettings.md)
- [/System/Library/PreferenceBundles/AccountSettings/icloudMailSettings.bundle/icloudMailSettings](MACHOS/icloudMailSettings.md)
- [/System/Library/PreferenceBundles/AppInstallationSettings.bundle/AppInstallationSettings](MACHOS/AppInstallationSettings.md)
- [/System/Library/PreferenceBundles/BatteryUsageUI.bundle/BatteryUsageUI](MACHOS/BatteryUsageUI.md)
- [/System/Library/PreferenceBundles/CallScreeningSettingsBundle.bundle/CallScreeningSettingsBundle](MACHOS/CallScreeningSettingsBundle.md)
- [/System/Library/PreferenceBundles/ContactlessAndCredentialSettings.bundle/ContactlessAndCredentialSettings](MACHOS/ContactlessAndCredentialSettings.md)
- [/System/Library/PreferenceBundles/MobileSafariSettings.bundle/MobileSafariSettings](MACHOS/MobileSafariSettings.md)
- [/System/Library/PreferenceBundles/MobileStoreSettings.bundle/MobileStoreSettings](MACHOS/MobileStoreSettings.md)
- [/System/Library/PreferenceBundles/MusicSettings.bundle/MusicSettings](MACHOS/MusicSettings.md)
- [/System/Library/PreferenceBundles/NewsSettings.bundle/NewsSettings](MACHOS/NewsSettings.md)
- [/System/Library/PreferenceBundles/PictureInPictureSettings.bundle/PictureInPictureSettings](MACHOS/PictureInPictureSettings.md)
- [/System/Library/PreferenceBundles/PodcastsSettingsPlugin.bundle/PodcastsSettingsPlugin](MACHOS/PodcastsSettingsPlugin.md)
- [/System/Library/PreferenceBundles/Privacy/WalletPrivacySettings.bundle/WalletPrivacySettings](MACHOS/WalletPrivacySettings.md)
- [/System/Library/PreferenceBundles/StoragePlugins/PodcastsUsagePlugin.bundle/PodcastsUsagePlugin](MACHOS/PodcastsUsagePlugin.md)
- [/System/Library/PreferenceBundles/StorageSettingsUI.bundle/StorageSettingsUI](MACHOS/StorageSettingsUI.md)
- [/System/Library/PreferenceBundles/TVSettings.bundle/TVSettings](MACHOS/TVSettings.md)
- [/System/Library/PreferenceBundles/VideoSubscriberAccountSettings.bundle/VideoSubscriberAccountSettings](MACHOS/VideoSubscriberAccountSettings.md)
- [/System/Library/PreferenceManifestsInternal/DisplayAndBrightnessPreferencesManifests.bundle/DisplayAndBrightnessPreferencesManifests](MACHOS/DisplayAndBrightnessPreferencesManifests.md)
- [/System/Library/PreferencesSyncBundles/CoreLocationSync.bundle/CoreLocationSync](MACHOS/CoreLocationSync.md)
- [/System/Library/PrivateFrameworks/AnnounceSiriExtensions.framework/PlugIns/AnnounceIntentExtension.appex/AnnounceIntentExtension](MACHOS/AnnounceIntentExtension.md)
- [/System/Library/PrivateFrameworks/AppInstallationMetrics.framework/Support/appinstallationmetricsd](MACHOS/appinstallationmetricsd.md)
- [/System/Library/PrivateFrameworks/AppSSO.framework/Support/AppSSODaemon](MACHOS/AppSSODaemon.md)
- [/System/Library/PrivateFrameworks/AppStoreComponents.framework/Support/appstorecomponentsd](MACHOS/appstorecomponentsd.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored](MACHOS/appstored.md)
- [/System/Library/PrivateFrameworks/AppleAccountUI.framework/PlugIns/AAUIFollowUpExtension.appex/AAUIFollowUpExtension](MACHOS/AAUIFollowUpExtension.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/amsaccountsd](MACHOS/amsaccountsd.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/Extensions/UtilityExtension.appex/UtilityExtension](MACHOS/UtilityExtension.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/amsengagementd](MACHOS/amsengagementd.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUIDynamic.framework/XPCServices/AppleMediaServicesUIDynamicService.xpc/AppleMediaServicesUIDynamicService](MACHOS/AppleMediaServicesUIDynamicService.md)
- [/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/XPCServices/ANECompilerService.xpc/ANECompilerService](MACHOS/ANECompilerService.md)
- [/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/XPCServices/ANEStorageMaintainer.xpc/ANEStorageMaintainer](MACHOS/ANEStorageMaintainer.md)
- [/System/Library/PrivateFrameworks/ApplePushService.framework/apsd](MACHOS/apsd.md)
- [/System/Library/PrivateFrameworks/AskPermission.framework/Support/askpermissiond](MACHOS/askpermissiond.md)
- [/System/Library/PrivateFrameworks/AssetCacheServices.framework/XPCServices/AssetCacheLocatorService.xpc/AssetCacheLocatorService](MACHOS/AssetCacheLocatorService.md)
- [/System/Library/PrivateFrameworks/AssetViewer.framework/PlugIns/ASVAssetViewer.appex/ASVAssetViewer](MACHOS/ASVAssetViewer.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd](MACHOS/assistantd.md)
- [/System/Library/PrivateFrameworks/AuthKit.framework/akd](MACHOS/akd.md)
- [/System/Library/PrivateFrameworks/AuthKitUI.framework/PlugIns/AKAppSSOExtension.appex/AKAppSSOExtension](MACHOS/AKAppSSOExtension.md)
- [/System/Library/PrivateFrameworks/AuthKitUI.framework/PlugIns/AKFollowUpExtension.appex/AKFollowUpExtension](MACHOS/AKFollowUpExtension.md)
- [/System/Library/PrivateFrameworks/BookDataStore.framework/Support/bookdatastored](MACHOS/bookdatastored.md)
- [/System/Library/PrivateFrameworks/BookLibraryCore.framework/Support/bookassetd](MACHOS/bookassetd.md)
- [/System/Library/PrivateFrameworks/CSExattrCrypto.framework/XPCServices/CSExattrCryptoService.xpc/CSExattrCryptoService](MACHOS/CSExattrCryptoService.md)
- [/System/Library/PrivateFrameworks/CacheDelete.framework/deleted](MACHOS/deleted.md)
- [/System/Library/PrivateFrameworks/CacheDelete.framework/deleted_helper](MACHOS/deleted_helper.md)
- [/System/Library/PrivateFrameworks/CallHistory.framework/Support/CallHistorySyncHelper](MACHOS/CallHistorySyncHelper.md)
- [/System/Library/PrivateFrameworks/Categories.framework/XPCServices/CategoriesService.xpc/CategoriesService](MACHOS/CategoriesService.md)
- [/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.MobileDocumentsFileProvider.appex/com.apple.CloudDocs.MobileDocumentsFileProvider](MACHOS/com.apple.CloudDocs.MobileDocumentsFileProvider.md)
- [/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.MobileDocumentsFileProviderManaged.appex/com.apple.CloudDocs.MobileDocumentsFileProviderManaged](MACHOS/com.apple.CloudDocs.MobileDocumentsFileProviderManaged.md)
- [/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.iCloudDriveFileProvider.appex/com.apple.CloudDocs.iCloudDriveFileProvider](MACHOS/com.apple.CloudDocs.iCloudDriveFileProvider.md)
- [/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.iCloudDriveFileProviderManaged.appex/com.apple.CloudDocs.iCloudDriveFileProviderManaged](MACHOS/com.apple.CloudDocs.iCloudDriveFileProviderManaged.md)
- [/System/Library/PrivateFrameworks/CloudDocsDaemon.framework/PlugIns/CloudDocsDiagnostic.appex/CloudDocsDiagnostic](MACHOS/CloudDocsDiagnostic.md)
- [/System/Library/PrivateFrameworks/CloudKitDaemon.framework/Support/ckdiscretionaryd](MACHOS/ckdiscretionaryd.md)
- [/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/Support/cloudphotod](MACHOS/cloudphotod.md)
- [/System/Library/PrivateFrameworks/CommunicationsFilter.framework/CMFSyncAgent](MACHOS/CMFSyncAgent.md)
- [/System/Library/PrivateFrameworks/ContinuousDialogManagerService.framework/assistant_cdmd](MACHOS/assistant_cdmd.md)
- [/System/Library/PrivateFrameworks/CoreAccessories.framework/Support/accessoryd](MACHOS/accessoryd.md)
- [/System/Library/PrivateFrameworks/CoreAccessories.framework/XPCServices/ACCHWComponentAuthService.xpc/ACCHWComponentAuthService](MACHOS/ACCHWComponentAuthService.md)
- [/System/Library/PrivateFrameworks/CoreAccessoriesFeatures.framework/XPCServices/ACCFeatureAudioProductService.xpc/ACCFeatureAudioProductService](MACHOS/ACCFeatureAudioProductService.md)
- [/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsd](MACHOS/analyticsd.md)
- [/System/Library/PrivateFrameworks/CoreCDPUI.framework/PlugIns/CDPFollowUpExtension.appex/CDPFollowUpExtension](MACHOS/CDPFollowUpExtension.md)
- [/System/Library/PrivateFrameworks/CoreFollowUp.framework/followupd](MACHOS/followupd.md)
- [/System/Library/PrivateFrameworks/CoreFollowUpUI.framework/PlugIns/FollowUpSampleExtension.appex/FollowUpSampleExtension](MACHOS/FollowUpSampleExtension.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/PlugIns/SearchPoirotExtension.appex/SearchPoirotExtension](MACHOS/SearchPoirotExtension.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/parsec-fbf](MACHOS/parsec-fbf.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/parsecd](MACHOS/parsecd.md)
- [/System/Library/PrivateFrameworks/CoreRecents.framework/recentsd](MACHOS/recentsd.md)
- [/System/Library/PrivateFrameworks/CoreRoutine.framework/XPCServices/CoreRoutineHelperService.xpc/CoreRoutineHelperService](MACHOS/CoreRoutineHelperService.md)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/XPCServices/CoreSpeechXPC.xpc/CoreSpeechXPC](MACHOS/CoreSpeechXPC.md)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd](MACHOS/corespeechd.md)
- [/System/Library/PrivateFrameworks/DataMigration.framework/XPCServices/com.apple.datamigrator.xpc/com.apple.datamigrator](MACHOS/com.apple.datamigrator.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/ContinuousRecordingsDiagnosticExtension.appex/ContinuousRecordingsDiagnosticExtension](MACHOS/ContinuousRecordingsDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.B389.appex/com.apple.DiagnosticExtensions.B389](MACHOS/com.apple.DiagnosticExtensions.B389.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Microstackshot.appex/com.apple.DiagnosticExtensions.Microstackshot](MACHOS/com.apple.DiagnosticExtensions.Microstackshot.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.sysdiagnose.appex/com.apple.DiagnosticExtensions.sysdiagnose](MACHOS/com.apple.DiagnosticExtensions.sysdiagnose.md)
- [/System/Library/PrivateFrameworks/DialogEngine.framework/catutil](MACHOS/catutil.md)
- [/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/XPCServices/DPSubmissionService.xpc/DPSubmissionService](MACHOS/DPSubmissionService.md)
- [/System/Library/PrivateFrameworks/DiskImages2.framework/XPCServices/diskimagescontroller.xpc/diskimagescontroller](MACHOS/diskimagescontroller.md)
- [/System/Library/PrivateFrameworks/DragUI.framework/Support/druid](MACHOS/druid.md)
- [/System/Library/PrivateFrameworks/EmailDaemon.framework/maild](MACHOS/maild.md)
- [/System/Library/PrivateFrameworks/EmergencyAlerts.framework/PlugIns/EmergencyAlertsUIExtension.appex/EmergencyAlertsUIExtension](MACHOS/EmergencyAlertsUIExtension.md)
- [/System/Library/PrivateFrameworks/FSKit.framework/fskitd](MACHOS/fskitd.md)
- [/System/Library/PrivateFrameworks/FamilyCircle.framework/familycircled](MACHOS/familycircled.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceHelperXPCService.xpc/FindMyDeviceHelperXPCService](MACHOS/FindMyDeviceHelperXPCService.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/Support/fontservicesd](MACHOS/fontservicesd.md)
- [/System/Library/PrivateFrameworks/GPUToolsCapture.framework/GPUToolsCapture](MACHOS/GPUToolsCapture.md)
- [/System/Library/PrivateFrameworks/GPUToolsDiagnostics.framework/GPUToolsDiagnostics](MACHOS/GPUToolsDiagnostics.md)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/PlugIns/GameCenterMatchmakerExtension.appex/GameCenterMatchmakerExtension](MACHOS/GameCenterMatchmakerExtension.md)
- [/System/Library/PrivateFrameworks/GenerationalStorage.framework/revisiond](MACHOS/revisiond.md)
- [/System/Library/PrivateFrameworks/GeoAnalytics.framework/geoanalyticsd](MACHOS/geoanalyticsd.md)
- [/System/Library/PrivateFrameworks/GeoServices.framework/geod](MACHOS/geod.md)
- [/System/Library/PrivateFrameworks/HealthPluginHost.framework/healthappd](MACHOS/healthappd.md)
- [/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd](MACHOS/identityservicesd.md)
- [/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/imagent](MACHOS/imagent.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatform.framework/PlugIns/DiagnosticExtension.appex/DiagnosticExtension](MACHOS/DiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCompute.framework/XPCServices/IntelligencePlatformComputeService.xpc/IntelligencePlatformComputeService](MACHOS/IntelligencePlatformComputeService.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/PlugIns/IntelligencePlatformLighthousePlugin.appex/IntelligencePlatformLighthousePlugin](MACHOS/IntelligencePlatformLighthousePlugin.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/intelligenceplatformd](MACHOS/intelligenceplatformd.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/knowledgeconstructiond](MACHOS/knowledgeconstructiond.md)
- [/System/Library/PrivateFrameworks/MapsSuggestions.framework/destinationd](MACHOS/destinationd.md)
- [/System/Library/PrivateFrameworks/MapsSupport.framework/mapspushd](MACHOS/mapspushd.md)
- [/System/Library/PrivateFrameworks/MapsSupport.framework/navd](MACHOS/navd.md)
- [/System/Library/PrivateFrameworks/MapsSync.framework/mapssyncd](MACHOS/mapssyncd.md)
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd](MACHOS/mediaanalysisd.md)
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd-service](MACHOS/mediaanalysisd-service.md)
- [/System/Library/PrivateFrameworks/MediaRemote.framework/Support/mediaremoted](MACHOS/mediaremoted.md)
- [/System/Library/PrivateFrameworks/MentalHealthUI.framework/archive.metallib](MACHOS/archive.metallib.md)
- [/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/XPCServices/MessagesAirlockService.xpc/MessagesAirlockService](MACHOS/MessagesAirlockService.md)
- [/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/XPCServices/MessagesBlastDoorService.xpc/MessagesBlastDoorService](MACHOS/MessagesBlastDoorService.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/Support/accessoryupdaterd](MACHOS/accessoryupdaterd.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/EAUpdaterService.xpc/EAUpdaterService](MACHOS/EAUpdaterService.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceHID.xpc/UARPUpdaterServiceHID](MACHOS/UARPUpdaterServiceHID.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceLegacyAudio.xpc/UARPUpdaterServiceLegacyAudio](MACHOS/UARPUpdaterServiceLegacyAudio.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceUSBPD.xpc/UARPUpdaterServiceUSBPD](MACHOS/UARPUpdaterServiceUSBPD.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackupCacheDeleteService](MACHOS/MobileBackupCacheDeleteService.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/PlugIns/MBDiagnosticExtension.appex/MBDiagnosticExtension](MACHOS/MBDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/PlugIns/MBPrebuddyFollowUpExtension.appex/MBPrebuddyFollowUpExtension](MACHOS/MBPrebuddyFollowUpExtension.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/XPCServices/MBHelperService.xpc/MBHelperService](MACHOS/MBHelperService.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/backupd](MACHOS/backupd.md)
- [/System/Library/PrivateFrameworks/MobileInstallation.framework/XPCServices/com.apple.MobileInstallationHelperService.xpc/com.apple.MobileInstallationHelperService](MACHOS/com.apple.MobileInstallationHelperService.md)
- [/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/XPCServices/com.apple.MobileSoftwareUpdate.CleanupPreparePathService.xpc/com.apple.MobileSoftwareUpdate.CleanupPreparePathService](MACHOS/com.apple.MobileSoftwareUpdate.CleanupPreparePathService.md)
- [/System/Library/PrivateFrameworks/MultitouchSessionFilterSupport.framework/XPCServices/SessionFilterPreferenceProvider.xpc/SessionFilterPreferenceProvider](MACHOS/SessionFilterPreferenceProvider.md)
- [/System/Library/PrivateFrameworks/MusicLibrary.framework/Support/medialibraryd](MACHOS/medialibraryd.md)
- [/System/Library/PrivateFrameworks/NanoBackup.framework/nanobackupd](MACHOS/nanobackupd.md)
- [/System/Library/PrivateFrameworks/NanoTimeKit.framework/nanotimekitcompaniond](MACHOS/nanotimekitcompaniond.md)
- [/System/Library/PrivateFrameworks/NeighborhoodActivityConduit.framework/XPCServices/com.apple.NeighborhoodActivityConduitService.xpc/com.apple.NeighborhoodActivityConduitService](MACHOS/com.apple.NeighborhoodActivityConduitService.md)
- [/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/PlugIns/NewDeviceOutreachExtension.appex/NewDeviceOutreachExtension](MACHOS/NewDeviceOutreachExtension.md)
- [/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/ndoagent](MACHOS/ndoagent.md)
- [/System/Library/PrivateFrameworks/NewsDaemon.framework/newsd](MACHOS/newsd.md)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/passd](MACHOS/passd.md)
- [/System/Library/PrivateFrameworks/Pasteboard.framework/Support/pasted](MACHOS/pasted.md)
- [/System/Library/PrivateFrameworks/People.framework/peopled](MACHOS/peopled.md)
- [/System/Library/PrivateFrameworks/PlugInKitDaemon.framework/PlugInKitDaemon](MACHOS/PlugInKitDaemon.md)
- [/System/Library/PrivateFrameworks/PointerUIServices.framework/Support/pointeruid](MACHOS/pointeruid.md)
- [/System/Library/PrivateFrameworks/PowerLog.framework/XPCServices/PerfPowerTelemetryClientRegistrationService.xpc/PerfPowerTelemetryClientRegistrationService](MACHOS/PerfPowerTelemetryClientRegistrationService.md)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/PlugIns/DEPowerlogEPL.appex/DEPowerlogEPL](MACHOS/DEPowerlogEPL.md)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/XPCServices/PerfPowerServicesSignpostReader.xpc/PerfPowerServicesSignpostReader](MACHOS/PerfPowerServicesSignpostReader.md)
- [/System/Library/PrivateFrameworks/PrintKit.framework/XPCServices/com.apple.PrintKit.PrinterTool.xpc/com.apple.PrintKit.PrinterTool](MACHOS/com.apple.PrintKit.PrinterTool.md)
- [/System/Library/PrivateFrameworks/PrintKit.framework/XPCServices/printbandservice.xpc/printbandservice](MACHOS/printbandservice.md)
- [/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePlugin.appex/DPMLRuntimePlugin](MACHOS/DPMLRuntimePlugin.md)
- [/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePluginClassB.appex/DPMLRuntimePluginClassB](MACHOS/DPMLRuntimePluginClassB.md)
- [/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePluginNonDnU.appex/DPMLRuntimePluginNonDnU](MACHOS/DPMLRuntimePluginNonDnU.md)
- [/System/Library/PrivateFrameworks/STSXPCHelperClient.framework/XPCServices/STSXPCHelper.xpc/STSXPCHelper](MACHOS/STSXPCHelper.md)
- [/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeAgent](MACHOS/ScreenTimeAgent.md)
- [/System/Library/PrivateFrameworks/Search.framework/searchd](MACHOS/searchd.md)
- [/System/Library/PrivateFrameworks/Sharing.framework/PlugIns/AirDrop.appex/AirDrop](MACHOS/AirDrop.md)
- [/System/Library/PrivateFrameworks/SharingHUD.framework/XPCServices/SharingHUDService.xpc/SharingHUDService](MACHOS/SharingHUDService.md)
- [/System/Library/PrivateFrameworks/SiriGeo.framework/PlugIns/SiriGeoIntentExtension.appex/SiriGeoIntentExtension](MACHOS/SiriGeoIntentExtension.md)
- [/System/Library/PrivateFrameworks/SiriInference.framework/Support/siriinferenced](MACHOS/siriinferenced.md)
- [/System/Library/PrivateFrameworks/SiriTTSService.framework/sirittsd](MACHOS/sirittsd.md)
- [/System/Library/PrivateFrameworks/SiriVOX.framework/SiriHeadlessService](MACHOS/SiriHeadlessService.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/Support/softwareupdateservicesd](MACHOS/softwareupdateservicesd.md)
- [/System/Library/PrivateFrameworks/SpaceAttribution.framework/spaceattributiond](MACHOS/spaceattributiond.md)
- [/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/XPCServices/com.apple.SpeechRecognitionCore.brokerd.xpc/com.apple.SpeechRecognitionCore.brokerd](MACHOS/com.apple.SpeechRecognitionCore.brokerd.md)
- [/System/Library/PrivateFrameworks/StreamingZip.framework/XPCServices/com.apple.StreamingUnzipService.privileged.xpc/com.apple.StreamingUnzipService.privileged](MACHOS/com.apple.StreamingUnzipService.privileged.md)
- [/System/Library/PrivateFrameworks/StreamingZip.framework/XPCServices/com.apple.StreamingUnzipService.xpc/com.apple.StreamingUnzipService](MACHOS/com.apple.StreamingUnzipService.md)
- [/System/Library/PrivateFrameworks/SyncedDefaults.framework/Support/syncdefaultsd](MACHOS/syncdefaultsd.md)
- [/System/Library/PrivateFrameworks/TCC.framework/Support/tccd](MACHOS/tccd.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd](MACHOS/callservicesd.md)
- [/System/Library/PrivateFrameworks/TrialServer.framework/XPCServices/TrialArchivingService.xpc/TrialArchivingService](MACHOS/TrialArchivingService.md)
- [/System/Library/PrivateFrameworks/UVFSXPCService.framework/XPCServices/UVFSService.xpc/UVFSService](MACHOS/UVFSService.md)
- [/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTrackingAgent](MACHOS/UsageTrackingAgent.md)
- [/System/Library/PrivateFrameworks/UserActivity.framework/Agents/useractivityd](MACHOS/useractivityd.md)
- [/System/Library/PrivateFrameworks/VisualVoicemail.framework/vmd](MACHOS/vmd.md)
- [/System/Library/PrivateFrameworks/VoiceMemos.framework/Support/voicememod](MACHOS/voicememod.md)
- [/System/Library/PrivateFrameworks/WatchListKit.framework/Support/watchlistd](MACHOS/watchlistd.md)
- [/System/Library/PrivateFrameworks/WeatherDaemon.framework/weatherd](MACHOS/weatherd.md)
- [/System/Library/PrivateFrameworks/WebPrivacy.framework/webprivacyd](MACHOS/webprivacyd.md)
- [/System/Library/PrivateFrameworks/WelcomeKit.framework/matd](MACHOS/matd.md)
- [/System/Library/PrivateFrameworks/WiFiPolicy.framework/XPCServices/ThreeBarsXPCService.xpc/ThreeBarsXPCService](MACHOS/ThreeBarsXPCService.md)
- [/System/Library/PrivateFrameworks/WiFiPolicy.framework/XPCServices/WiFiCloudAssetsXPCService.xpc/WiFiCloudAssetsXPCService](MACHOS/WiFiCloudAssetsXPCService.md)
- [/System/Library/PrivateFrameworks/WirelessInsights.framework/Support/wirelessinsightsd](MACHOS/wirelessinsightsd.md)
- [/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/BackgroundShortcutRunner.xpc/BackgroundShortcutRunner](MACHOS/BackgroundShortcutRunner.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/SystemActionConfigurationExtension.appex/SystemActionConfigurationExtension](MACHOS/SystemActionConfigurationExtension.md)
- [/System/Library/PrivateFrameworks/iCloudNotification.framework/ind](MACHOS/ind.md)
- [/System/Library/PrivateFrameworks/iTunesCloud.framework/Support/itunescloudd](MACHOS/itunescloudd.md)
- [/System/Library/PrivateFrameworks/iTunesStore.framework/Support/itunesstored](MACHOS/itunesstored.md)
- [/System/Library/ScreenReader/BrailleDrivers/DOT Driver.brailledriver/DOT Driver](MACHOS/DOT_Driver.md)
- [/System/Library/ScreenReader/BrailleDrivers/GenericHID.brailledriver/GenericHID](MACHOS/GenericHID.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/AudioSuggestionsPlugin.bundle/AudioSuggestionsPlugin](MACHOS/AudioSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriGeoSuggestions.bundle/SiriGeoSuggestions](MACHOS/SiriGeoSuggestions.md)
- [/System/Library/Snippets/UIPlugins/HomeCommunicationUIPlugin.bundle/HomeCommunicationUIPlugin](MACHOS/HomeCommunicationUIPlugin.md)
- [/System/Library/SpringBoardPlugins/StoreDemoPlugin.servicebundle/StoreDemoPlugin](MACHOS/StoreDemoPlugin.md)
- [/System/Library/SyncBundles/MusicLibrary.syncBundle/MusicLibrary](MACHOS/MusicLibrary.md)
- [/System/Library/SystemConfiguration/IPConfiguration.bundle/IPConfiguration](MACHOS/IPConfiguration.md)
- [/System/Library/TextInput/kbd](MACHOS/kbd.md)
- [/System/Library/Trace/Providers/Symbolication.bundle/Symbolication](MACHOS/Symbolication.md)
- [/System/Library/UserEventPlugins/ADEventListenerPlugin.plugin/ADEventListenerPlugin](MACHOS/ADEventListenerPlugin.md)
- [/System/Library/UserEventPlugins/BonjourEvents.plugin/BonjourEvents](MACHOS/BonjourEvents.md)
- [/System/Library/UserEventPlugins/MobileBackupUEA.plugin/MobileBackupUEA](MACHOS/MobileBackupUEA.md)
- [/System/Library/UserEventPlugins/MobileKeyBagLockState.plugin/MobileKeyBagLockState](MACHOS/MobileKeyBagLockState.md)
- [/System/Library/UserEventPlugins/PerfPowerServicesEventListenerPlugin.plugin/PerfPowerServicesEventListenerPlugin](MACHOS/PerfPowerServicesEventListenerPlugin.md)
- [/System/Library/UserEventPlugins/com.apple.BackgroundTaskAgentPlugin.plugin/com.apple.BackgroundTaskAgentPlugin](MACHOS/com.apple.BackgroundTaskAgentPlugin.md)
- [/System/Library/UserEventPlugins/com.apple.accessoryd.matching.plugin/com.apple.accessoryd.matching](MACHOS/com.apple.accessoryd.matching.md)
- [/System/Library/UserEventPlugins/com.apple.cts.plugin/com.apple.cts](MACHOS/com.apple.cts.md)
- [/System/Library/UserEventPlugins/com.apple.fsevents.matching.plugin/com.apple.fsevents.matching](MACHOS/com.apple.fsevents.matching.md)
- [/System/Library/UserEventPlugins/com.apple.telemetry.plugin/com.apple.telemetry](MACHOS/com.apple.telemetry.md)
- [/System/Library/UserEventPlugins/locationd.events.plugin/locationd.events](MACHOS/locationd.events.md)
- [/System/Library/UserNotifications/Bundles/com.apple.ARQLNotifications.bundle/com.apple.ARQLNotifications](MACHOS/com.apple.ARQLNotifications.md)
- [/System/Library/Video/Plug-Ins/AppleMCTF.bundle/AppleMCTF](MACHOS/AppleMCTF.md)
- [/System/Library/Video/Plug-Ins/AppleVideoEncoder.bundle/AppleVideoEncoder](MACHOS/AppleVideoEncoder.md)
- [/System/Library/VideoProcessors/VideoDeghostingV2.bundle/VideoDeghostingV2](MACHOS/VideoDeghostingV2.md)
- [/private/var/staged_system_apps/AppleTV.app/AppleTV](MACHOS/AppleTV.md)
- [/private/var/staged_system_apps/Books.app/Books](MACHOS/Books.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/AEBookPlugins.framework/AEBookPlugins](MACHOS/AEBookPlugins.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BKAudiobooks.framework/BKAudiobooks](MACHOS/BKAudiobooks.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BKLibrary.framework/BKLibrary](MACHOS/BKLibrary.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BlissReader.framework/BlissReader](MACHOS/BlissReader.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookAnalytics.framework/BookAnalytics](MACHOS/BookAnalytics.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookCore.framework/BookCore](MACHOS/BookCore.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookEPUB.framework/BookEPUB](MACHOS/BookEPUB.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookStoreUI.framework/BookStoreUI](MACHOS/BookStoreUI.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BooksAll.framework/BooksAll](MACHOS/BooksAll.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BooksPersonalization.framework/BooksPersonalization](MACHOS/BooksPersonalization.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BooksUI.framework/BooksUI](MACHOS/BooksUI.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/JSApp.framework/JSApp](MACHOS/JSApp.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/TemplateUI.framework/TemplateUI](MACHOS/TemplateUI.md)
- [/private/var/staged_system_apps/Books.app/PlugIns/BooksNotificationContentExtension.appex/BooksNotificationContentExtension](MACHOS/BooksNotificationContentExtension.md)
- [/private/var/staged_system_apps/Books.app/PlugIns/BooksProductPageExtension.appex/BooksProductPageExtension](MACHOS/BooksProductPageExtension.md)
- [/private/var/staged_system_apps/Books.app/PlugIns/BooksThumbnail.appex/BooksThumbnail](MACHOS/BooksThumbnail.md)
- [/private/var/staged_system_apps/Books.app/PlugIns/BooksWidgetExtension.appex/BooksWidgetExtension](MACHOS/BooksWidgetExtension.md)
- [/private/var/staged_system_apps/Bridge.app/Bridge](MACHOS/Bridge.md)
- [/private/var/staged_system_apps/Calculator.app/Calculator](MACHOS/Calculator.md)
- [/private/var/staged_system_apps/Compass.app/Compass](MACHOS/Compass.md)
- [/private/var/staged_system_apps/Contacts.app/Contacts](MACHOS/Contacts.md)
- [/private/var/staged_system_apps/FaceTime.app/FaceTime](MACHOS/FaceTime.md)
- [/private/var/staged_system_apps/Files.app/Files](MACHOS/Files.md)
- [/private/var/staged_system_apps/FindMy.app/FindMy](MACHOS/FindMy.md)
- [/private/var/staged_system_apps/Fitness.app/Fitness](MACHOS/Fitness.md)
- [/private/var/staged_system_apps/Freeform.app/Freeform](MACHOS/Freeform.md)
- [/private/var/staged_system_apps/Health.app/Health](MACHOS/Health.md)
- [/private/var/staged_system_apps/Home.app/Home](MACHOS/Home.md)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeNotification.appex/HomeNotification](MACHOS/HomeNotification.md)
- [/private/var/staged_system_apps/Journal.app/Journal](MACHOS/Journal.md)
- [/private/var/staged_system_apps/Journal.app/PlugIns/JournalShareExtension.appex/JournalShareExtension](MACHOS/JournalShareExtension.md)
- [/private/var/staged_system_apps/Maps.app/Maps](MACHOS/Maps.md)
- [/private/var/staged_system_apps/MobileCal.app/MobileCal](MACHOS/MobileCal.md)
- [/private/var/staged_system_apps/MobileMail.app/MobileMail](MACHOS/MobileMail.md)
- [/private/var/staged_system_apps/MobileMail.app/PlugIns/MailNotificationContentExtension.appex/MailNotificationContentExtension](MACHOS/MailNotificationContentExtension.md)
- [/private/var/staged_system_apps/MobileMail.app/PlugIns/MailQuickLookExtension.appex/MailQuickLookExtension](MACHOS/MailQuickLookExtension.md)
- [/private/var/staged_system_apps/MobileNotes.app/MobileNotes](MACHOS/MobileNotes.md)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.IntentsExtension.appex/com.apple.mobilenotes.IntentsExtension](MACHOS/com.apple.mobilenotes.IntentsExtension.md)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.SharingExtension.appex/com.apple.mobilenotes.SharingExtension](MACHOS/com.apple.mobilenotes.SharingExtension.md)
- [/private/var/staged_system_apps/MobileStore.app/MobileStore](MACHOS/MobileStore.md)
- [/private/var/staged_system_apps/MobileTimer.app/MobileTimer](MACHOS/MobileTimer.md)
- [/private/var/staged_system_apps/Music.app/Frameworks/MusicApplication.framework/MusicApplication](MACHOS/MusicApplication.md)
- [/private/var/staged_system_apps/Music.app/Frameworks/MusicApplication.framework/XPCServices/MusicScriptUpdateService.xpc/MusicScriptUpdateService](MACHOS/MusicScriptUpdateService.md)
- [/private/var/staged_system_apps/Music.app/Music](MACHOS/Music.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/MusicMessagesApp.appex/MusicMessagesApp](MACHOS/MusicMessagesApp.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/MusicWidgets.appex/MusicWidgets](MACHOS/MusicWidgets.md)
- [/private/var/staged_system_apps/News.app/News](MACHOS/News.md)
- [/private/var/staged_system_apps/News.app/PlugIns/ArticleNotificationExtension.appex/ArticleNotificationExtension](MACHOS/ArticleNotificationExtension.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsDiagnosticExtension.appex/NewsDiagnosticExtension](MACHOS/NewsDiagnosticExtension.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsNotificationServiceExtension.appex/NewsNotificationServiceExtension](MACHOS/NewsNotificationServiceExtension.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsTag.appex/NewsTag](MACHOS/NewsTag.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsToday2.appex/NewsToday2](MACHOS/NewsToday2.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsTodayIntents.appex/NewsTodayIntents](MACHOS/NewsTodayIntents.md)
- [/private/var/staged_system_apps/News.app/PlugIns/OpenInNews.appex/OpenInNews](MACHOS/OpenInNews.md)
- [/private/var/staged_system_apps/Passbook.app/Passbook](MACHOS/Passbook.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/AppStoreKit.framework/AppStoreKit](MACHOS/AppStoreKit.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/NowPlayingUI.framework/NowPlayingUI](MACHOS/NowPlayingUI.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/PodcastsStoreUI.framework/PodcastsStoreUI](MACHOS/PodcastsStoreUI.md)
- [/private/var/staged_system_apps/Podcasts.app/Podcasts](MACHOS/Podcasts.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersIntentsExtension.appex/RemindersIntentsExtension](MACHOS/RemindersIntentsExtension.md)
- [/private/var/staged_system_apps/Reminders.app/Reminders](MACHOS/Reminders.md)
- [/private/var/staged_system_apps/Shortcuts.app/PlugIns/ShortcutsWidgetExtension.appex/ShortcutsWidgetExtension](MACHOS/ShortcutsWidgetExtension.md)
- [/private/var/staged_system_apps/Shortcuts.app/Shortcuts](MACHOS/Shortcuts.md)
- [/private/var/staged_system_apps/Stocks.app/PlugIns/StocksDetailIntents.appex/StocksDetailIntents](MACHOS/StocksDetailIntents.md)
- [/private/var/staged_system_apps/Stocks.app/PlugIns/StocksDiagnosticExtension.appex/StocksDiagnosticExtension](MACHOS/StocksDiagnosticExtension.md)
- [/private/var/staged_system_apps/Stocks.app/PlugIns/StocksWidget.appex/StocksWidget](MACHOS/StocksWidget.md)
- [/private/var/staged_system_apps/Stocks.app/Stocks](MACHOS/Stocks.md)
- [/private/var/staged_system_apps/Tips.app/Tips](MACHOS/Tips.md)
- [/private/var/staged_system_apps/VoiceMemos.app/VoiceMemos](MACHOS/VoiceMemos.md)
- [/private/var/staged_system_apps/Weather.app/PlugIns/WeatherWidget.appex/WeatherWidget](MACHOS/WeatherWidget.md)
- [/private/var/staged_system_apps/Weather.app/Weather](MACHOS/Weather.md)
- [/sbin/launchd](MACHOS/launchd.md)
- [/sbin/mount](MACHOS/mount.md)
- [/usr/bin/IOMFB_FDR_Loader](MACHOS/IOMFB_FDR_Loader.md)
- [/usr/bin/afktool](MACHOS/afktool.md)
- [/usr/bin/zprint](MACHOS/zprint.md)
- [/usr/lib/dyld](MACHOS/dyld.md)
- [/usr/lib/libRPAC.dylib](MACHOS/libRPAC.dylib.md)
- [/usr/libexec/ASPCarryLog](MACHOS/ASPCarryLog.md)
- [/usr/libexec/BackupAgent2](MACHOS/BackupAgent2.md)
- [/usr/libexec/DumpPanic](MACHOS/DumpPanic.md)
- [/usr/libexec/FinishRestoreFromBackup](MACHOS/FinishRestoreFromBackup.md)
- [/usr/libexec/IOMFB_bics_daemon](MACHOS/IOMFB_bics_daemon.md)
- [/usr/libexec/MSUEarlyBootTask](MACHOS/MSUEarlyBootTask.md)
- [/usr/libexec/MobileGestaltHelper](MACHOS/MobileGestaltHelper.md)
- [/usr/libexec/UserEventAgent](MACHOS/UserEventAgent.md)
- [/usr/libexec/aned](MACHOS/aned.md)
- [/usr/libexec/anomalydetectiond](MACHOS/anomalydetectiond.md)
- [/usr/libexec/appleaccountd](MACHOS/appleaccountd.md)
- [/usr/libexec/appleh16camerad](MACHOS/appleh16camerad.md)
- [/usr/libexec/asktod](MACHOS/asktod.md)
- [/usr/libexec/assessmentagent](MACHOS/assessmentagent.md)
- [/usr/libexec/audioaccessoryd](MACHOS/audioaccessoryd.md)
- [/usr/libexec/audioanalyticsd](MACHOS/audioanalyticsd.md)
- [/usr/libexec/audioclocksyncd](MACHOS/audioclocksyncd.md)
- [/usr/libexec/backboardd](MACHOS/backboardd.md)
- [/usr/libexec/biomesyncd](MACHOS/biomesyncd.md)
- [/usr/libexec/bluetoothuserd](MACHOS/bluetoothuserd.md)
- [/usr/libexec/carkitd](MACHOS/carkitd.md)
- [/usr/libexec/configd](MACHOS/configd.md)
- [/usr/libexec/containermanagerd_system](MACHOS/containermanagerd_system.md)
- [/usr/libexec/coreduetd](MACHOS/coreduetd.md)
- [/usr/libexec/coreidvd](MACHOS/coreidvd.md)
- [/usr/libexec/countryd](MACHOS/countryd.md)
- [/usr/libexec/dasd](MACHOS/dasd.md)
- [/usr/libexec/demod](MACHOS/demod.md)
- [/usr/libexec/diagnosticd](MACHOS/diagnosticd.md)
- [/usr/libexec/dietapplecamerad](MACHOS/dietapplecamerad.md)
- [/usr/libexec/dietappleh16camerad](MACHOS/dietappleh16camerad.md)
- [/usr/libexec/diskarbitrationd](MACHOS/diskarbitrationd.md)
- [/usr/libexec/diskimagesiod](MACHOS/diskimagesiod.md)
- [/usr/libexec/dmd](MACHOS/dmd.md)
- [/usr/libexec/dockaccessoryd](MACHOS/dockaccessoryd.md)
- [/usr/libexec/eligibilityd](MACHOS/eligibilityd.md)
- [/usr/libexec/fairplaydeviceidentityd](MACHOS/fairplaydeviceidentityd.md)
- [/usr/libexec/findmydeviced](MACHOS/findmydeviced.md)
- [/usr/libexec/findmylocated](MACHOS/findmylocated.md)
- [/usr/libexec/fmfd](MACHOS/fmfd.md)
- [/usr/libexec/fseventsd](MACHOS/fseventsd.md)
- [/usr/libexec/gamed](MACHOS/gamed.md)
- [/usr/libexec/gamepolicyd](MACHOS/gamepolicyd.md)
- [/usr/libexec/gpsd](MACHOS/gpsd.md)
- [/usr/libexec/idcredd](MACHOS/idcredd.md)
- [/usr/libexec/inboxupdaterd](MACHOS/inboxupdaterd.md)
- [/usr/libexec/init_exclavekit](MACHOS/init_exclavekit.md)
- [/usr/libexec/keybagd](MACHOS/keybagd.md)
- [/usr/libexec/linkd](MACHOS/linkd.md)
- [/usr/libexec/locationd](MACHOS/locationd.md)
- [/usr/libexec/lockdownd](MACHOS/lockdownd.md)
- [/usr/libexec/logd](MACHOS/logd.md)
- [/usr/libexec/logd_helper](MACHOS/logd_helper.md)
- [/usr/libexec/logd_reporter](MACHOS/logd_reporter.md)
- [/usr/libexec/mediaparserd](MACHOS/mediaparserd.md)
- [/usr/libexec/mediaplaybackd](MACHOS/mediaplaybackd.md)
- [/usr/libexec/mediasetupd](MACHOS/mediasetupd.md)
- [/usr/libexec/mlhostd](MACHOS/mlhostd.md)
- [/usr/libexec/mmaintenanced](MACHOS/mmaintenanced.md)
- [/usr/libexec/mobileactivationd](MACHOS/mobileactivationd.md)
- [/usr/libexec/mobilerepaird](MACHOS/mobilerepaird.md)
- [/usr/libexec/momentsd](MACHOS/momentsd.md)
- [/usr/libexec/nanoregistryd](MACHOS/nanoregistryd.md)
- [/usr/libexec/neagent](MACHOS/neagent.md)
- [/usr/libexec/nearbyd](MACHOS/nearbyd.md)
- [/usr/libexec/nehelper](MACHOS/nehelper.md)
- [/usr/libexec/nesessionmanager](MACHOS/nesessionmanager.md)
- [/usr/libexec/networkserviceproxy](MACHOS/networkserviceproxy.md)
- [/usr/libexec/nfcd](MACHOS/nfcd.md)
- [/usr/libexec/nsurlsessiond](MACHOS/nsurlsessiond.md)
- [/usr/libexec/online-auth-agent](MACHOS/online-auth-agent.md)
- [/usr/libexec/pcsstatus](MACHOS/pcsstatus.md)
- [/usr/libexec/pipelined](MACHOS/pipelined.md)
- [/usr/libexec/profiled](MACHOS/profiled.md)
- [/usr/libexec/promotedcontentd](MACHOS/promotedcontentd.md)
- [/usr/libexec/proximitycontrold](MACHOS/proximitycontrold.md)
- [/usr/libexec/ptpcamerad](MACHOS/ptpcamerad.md)
- [/usr/libexec/rapportd](MACHOS/rapportd.md)
- [/usr/libexec/remindd](MACHOS/remindd.md)
- [/usr/libexec/remotepairingdeviced](MACHOS/remotepairingdeviced.md)
- [/usr/libexec/replayd](MACHOS/replayd.md)
- [/usr/libexec/rtcreportingd](MACHOS/rtcreportingd.md)
- [/usr/libexec/safetyalertsd](MACHOS/safetyalertsd.md)
- [/usr/libexec/searchpartyd](MACHOS/searchpartyd.md)
- [/usr/libexec/securityd](MACHOS/securityd.md)
- [/usr/libexec/securityuploadd](MACHOS/securityuploadd.md)
- [/usr/libexec/seserviced](MACHOS/seserviced.md)
- [/usr/libexec/sharingd](MACHOS/sharingd.md)
- [/usr/libexec/sirireaderd](MACHOS/sirireaderd.md)
- [/usr/libexec/smcDiagnose](MACHOS/smcDiagnose.md)
- [/usr/libexec/softposreaderd](MACHOS/softposreaderd.md)
- [/usr/libexec/spindump_fileparser](MACHOS/spindump_fileparser.md)
- [/usr/libexec/splashboardd](MACHOS/splashboardd.md)
- [/usr/libexec/srp-mdns-proxy](MACHOS/srp-mdns-proxy.md)
- [/usr/libexec/storagekitd](MACHOS/storagekitd.md)
- [/usr/libexec/sysdiagnose_helper](MACHOS/sysdiagnose_helper.md)
- [/usr/libexec/sysdiagnosed](MACHOS/sysdiagnosed.md)
- [/usr/libexec/terminusd](MACHOS/terminusd.md)
- [/usr/libexec/thermalmonitord](MACHOS/thermalmonitord.md)
- [/usr/libexec/timed](MACHOS/timed.md)
- [/usr/libexec/tipsd](MACHOS/tipsd.md)
- [/usr/libexec/transparencyd](MACHOS/transparencyd.md)
- [/usr/libexec/triald_system](MACHOS/triald_system.md)
- [/usr/libexec/trustd](MACHOS/trustd.md)
- [/usr/libexec/tzd](MACHOS/tzd.md)
- [/usr/libexec/usermanagerd](MACHOS/usermanagerd.md)
- [/usr/libexec/videosubscriptionsd](MACHOS/videosubscriptionsd.md)
- [/usr/libexec/watchdogd](MACHOS/watchdogd.md)
- [/usr/libexec/wcd](MACHOS/wcd.md)
- [/usr/libexec/webbookmarksd](MACHOS/webbookmarksd.md)
- [/usr/libexec/wifip2pd](MACHOS/wifip2pd.md)
- [/usr/libexec/xpcproxy](MACHOS/xpcproxy.md)
- [/usr/libexec/xpcroleaccountd](MACHOS/xpcroleaccountd.md)
- [/usr/sbin/BTLEServer](MACHOS/BTLEServer.md)
- [/usr/sbin/BlueTool](MACHOS/BlueTool.md)
- [/usr/sbin/WirelessRadioManagerd](MACHOS/WirelessRadioManagerd.md)
- [/usr/sbin/appleh16camerad](MACHOS/appleh16camerad.md)
- [/usr/sbin/bluetoothd](MACHOS/bluetoothd.md)
- [/usr/sbin/dietappleh16camerad](MACHOS/dietappleh16camerad.md)
- [/usr/sbin/distnoted](MACHOS/distnoted.md)
- [/usr/sbin/filecoordinationd](MACHOS/filecoordinationd.md)
- [/usr/sbin/mDNSResponder](MACHOS/mDNSResponder.md)
- [/usr/sbin/mediaserverd](MACHOS/mediaserverd.md)
- [/usr/sbin/racoon](MACHOS/racoon.md)
- [/usr/sbin/spindump](MACHOS/spindump.md)
- [/usr/sbin/wifid](MACHOS/wifid.md)

</details>

### 🔑 Entitlements

- [Entitlements DIFF](Entitlements.md)

## Firmware

### 🆕 NEW (1)

- `aopfw-iphone16aop.RELEASE.im4p`

### ❌ Removed (1)

- `aopfw-iphone16aop.im4p`

### ⬆️ Updated (14)

<details>
  <summary><i>View Updated</i></summary>

#### AppleAVE2FW_H16.im4p

>  `AppleAVE2FW_H16.im4p`

```diff

 
-  __TEXT.__text: 0xb8840
+  __TEXT.__text: 0xb8980
   __TEXT.__cstring: 0x11f2c
   __TEXT.__const: 0x1ca70
   __TEXT.__chain_starts: 0x0

```

#### SmartIOFirmware_ASCv6.im4p

>  `SmartIOFirmware_ASCv6.im4p`

```diff

 
-  __TEXT.__text: 0x1a3f8
+  __TEXT.__text: 0x1a454
   __TEXT.__cstring: 0x102c
   __TEXT.__const: 0x338
   __TEXT._rtk_mtab: 0x278

```

#### adc-aceso-d8x.im4p

>  `adc-aceso-d8x.im4p`

```diff

 
-  __TEXT.__text: 0x7a37fc
+  __TEXT.__text: 0x7aff00
   __TEXT.__data_copy: 0x100000
-  __TEXT.__const: 0x803300
-  __TEXT.__cstring: 0x9b10d
+  __TEXT.__const: 0x803ff0
+  __TEXT.__cstring: 0x9c1ab
   __TEXT._rtk_mtab: 0x288
   __TEXT.__constructor: 0x0
   __TEXT.__chain_starts: 0x0
   __TEXT.text_env: 0x507ac
   __TEXT.__ustring: 0xe
   __TEXT.__eh_frame: 0x200
-  __DATA.__const: 0x545f0
+  __DATA.__const: 0x54958
   __DATA._rtk_heap: 0x1000
-  __DATA.__data: 0xe02b0
+  __DATA.__data: 0xe0210
   __DATA._rtk_power: 0x3a8
   __DATA._rtk_patchbay: 0x218
   __DATA._rtk_init_stack: 0x2000

   __DATA._fwinfo: 0x100
   __DATA.__sysvars: 0x4
   __DATA._rtk_smp_main: 0x8
+  __DATA._rtk_boot_l1: 0x80
   __DATA.__mod_init_func: 0x20
-  __DATA.__zerofill: 0x221ed8
+  __DATA.__zerofill: 0x221e58
   Functions: 0
   Symbols:   0
-  CStrings:  17132
+  CStrings:  17213
 
CStrings:
+ "  %s: %u s frames:%u %s"
+ "  => next: {%4d%csx%3d%%x%3d%%} SIFR{%4d%csx%3d%%x%3d%%} stb=%d req=0x%x"
+ "  preLSC_amplitude_fft_ROI_1     %.9f\n"
+ "  preLSC_amplitude_fft_ROI_2     %.9f\n"
+ "  preLSC_amplitude_fft_ROI_26    %.9f\n"
+ "  preLSC_amplitude_fft_ROI_27    %.9f\n"
+ "  preLSC_amplitude_fft_ROI_28    %.9f\n"
+ "  preLSC_amplitude_fft_ROI_29    %.9f\n"
+ "  preLSC_amplitude_fft_ROI_3     %.9f\n"
+ "  preLSC_amplitude_fft_ROI_4     %.9f\n"
+ "  preLSC_amplitude_fft_ROI_5     %.9f\n"
+ "  preLSC_phase_deg_ROI_1         %.9f\n"
+ "  preLSC_phase_deg_ROI_2         %.9f\n"
+ "  preLSC_phase_deg_ROI_26        %.9f\n"
+ "  preLSC_phase_deg_ROI_27        %.9f\n"
+ "  preLSC_phase_deg_ROI_28        %.9f\n"
+ "  preLSC_phase_deg_ROI_29        %.9f\n"
+ "  preLSC_phase_deg_ROI_3         %.9f\n"
+ "  preLSC_phase_deg_ROI_4         %.9f\n"
+ "  preLSC_phase_deg_ROI_5         %.9f\n"
+ "  preLSC_pitch_mm_ROI_1          %.9f\n"
+ "  preLSC_pitch_mm_ROI_2          %.9f\n"
+ "  preLSC_pitch_mm_ROI_26         %.9f\n"
+ "  preLSC_pitch_mm_ROI_27         %.9f\n"
+ "  preLSC_pitch_mm_ROI_28         %.9f\n"
+ "  preLSC_pitch_mm_ROI_29         %.9f\n"
+ "  preLSC_pitch_mm_ROI_3          %.9f\n"
+ "  preLSC_pitch_mm_ROI_4          %.9f\n"
+ "  preLSC_pitch_mm_ROI_5          %.9f\n"
+ "%hx"
+ "%s read debug register 0x%x result %d\n"
+ "%s,lut,file=ispLutDump.bin\n"
+ "%s,reg,file=%s,bmsk=%d\n"
+ "%s,reg,file=%s_b%d.bin\n"
+ "%s: %s: No matching FCAMImageOCCorrection parser"
+ "%s: FRM_LENGTH_CALC : 0x%x%x - 0x%x%x - 0x%x%x\n"
+ "%s: chID=%d, fdAFWinID=%d, fdAFWinIDscaleFactor=%d, afFloatingWindowMask=%d\n"
+ "%s: chId=%d, enable=%d, window.x=%d, window.y=%d, window.width=%d, window.height=%d\n"
+ "%s: chId=%d, winID=%d, window.x=%d, window.y=%d, window.width=%d, window.height=%d\n"
+ "%s:%u:AE-IR:AE# currupt output gA 0x%x, dg 0x%x\n"
+ "./h10isp/drivers/SENSOR/VD56G0Balan/CImageSensorVD56G0BalanBoot.cpp"
+ "./h10isp/filters/Algorithm/PDAF/channel.cpp"
+ "08:10:24"
+ "274fc6f"
+ ":pdaf:{\"origin\":\"%s\",\"type\":\"%s\",\"ch\":%zu,\"enable\":%s,\"roi0\":[%d,%d,%d,%d],..\n"
+ ":pdaf:{\"origin\":\"%s\",\"type\":\"%s\",\"ch\":%zu,\"enable\":%s,\"roi1\":[%d,%d,%d,%d],..\n"
+ ":pdaf:{\"origin\":\"%s\",\"type\":\"%s\",\"ch\":%zu,\"enable\":%s,\"roi2\":[%d,%d,%d,%d],..\n"
+ "AEIR-PE:# %u, fps %f (%u, %u) fid %s, expT %d (%llu), pat %d(%d), prb %d, skip %d, tgt %u\n"
+ "AE[%u]: change faceTarget to %u\n"
+ "AE[%zu]:avg=%3u/tgt=%3u {%4d %csx%3d%%x%3d%%} SIFR{%4d %csx%3d%%x%3d%%} %9d lux"
+ "AFC Controller Output"
+ "AF_METHOD_MLAF"
+ "APS Com Single Cal \n"
+ "APS ComCal \n"
+ "ApplyCachedZoomParametersOnContextSwitch"
+ "Attn: Debug set to %d\n"
+ "BES Preview [%d %d %d %d] -> %d x %d OutDMA [%d %d %d %d]\n"
+ "BuildInfo  \n"
+ "CISP_CMD_APPLE_CH_AWB_AMBIENT_LIGHT_SENSOR_SET"
+ "CISP_CMD_APPLE_CH_MLVNR_MODE_CONFIG_SET"
+ "CISP_CMD_CH_CAPTURE_FES_CROP_SIZE_SET ColorBE Capture width/height are updated from [%d %d] to [%d %d]\n"
+ "CISP_CMD_CH_LC_DYNAMIC_VOLTAGE_PVDD_SET"
+ "CISP_CMD_CH_LPDP_RC_PARAMS_GET"
+ "CISP_CMD_CH_MULTICAM_AE_WINDOW_PARAM_SET"
+ "CISP_CMD_CH_MULTICAM_BHIST_ROI_SET"
+ "CISP_CMD_CH_MULTICAM_CAMERA_CONTROL_ROI_SET"
+ "CISP_CMD_CH_MULTICAM_COMBINED_AF_WINDOW_PARAM_SET"
+ "CISP_CMD_CH_TIMEWARP_FORCE_FPS"
+ "CISP_CMD_CH_TIMEWARP_PARAMS_SET"
+ "CISP_CMD_CH_TIMEWARP_RECORDING_SET"
+ "CNVMParserAPSSingleCal_H4_Format2.cpp"
+ "CfgTask_ProjectorReadTemperature"
+ "Color AF Cal  \n"
+ "Color Recal  \n"
+ "Color shading  \n"
+ "DbgOverlay::%s:%d:Set overlay flags for all channels => 0x%llx\n"
+ "DistCal \n"
+ "DistOverlayCal \n"
+ "Driver Command Write Timestamp [0:31]"
+ "Driver Command Write Timestamp [32:63]"
+ "Dual Build Info \n"
+ "ER-%llu/fd-postout-%03d.bin"
+ "Ext Cal \n"
+ "FD-%llu/depth-%03d.raw"
+ "FES [%d %d %d %d] -> %d x %d\n"
+ "FPDC \n"
+ "FPS[%zu]: Fr:%d.%03d ms = %3d.%03d fps"
+ "Field Curvature \n"
+ "GetMetaData"
+ "GetSecureInfo"
+ "HPR verification failure, status (0x7F4) 0x%x\n"
+ "IMU: accel:%3d,%3d,%3d = %3d"
+ "IMU: gyr:%3d,%3d,%3d=%3d quat=%3d,%3d,%3d,%3d dOrient=%3d,%3d,%3d"
+ "IMX614RegSetting.cpp"
+ "IMX913_ES2_v0202_mode021_n1a4_nonsifr60_pri_2112x1192_sec_skip"
+ "IMX913_ES2_v025_mode001_m0a1_ff60_pri_4224x3024_sec_4224x3024"
+ "IMX913_ES2_v025_mode004_c0a1_fb60_pri_4224x3024_sec_2112x1512"
+ "IMX913_ES2_v025_mode008_n1a3_nonsifr60_pri_2112x1512_sec_skip"
+ "IMX913_ES2_v025_mode009_m0a3_nonsifr120_pri_4224x3024_sec_skip"
+ "IMX913_ES2_v025_mode017_c0a2_fb60_pri_4224x2384_sec_2112x1192"
+ "IMX913_ES2_v025_mode021_n1a4_nonsifr60_pri_2112x1192_sec_skip"
+ "IMX913_ES2_v025_mode022_m0a4_nonsifr120_pri_4224x2384_sec_skip"
+ "IMX913_ES2_v025_mode024_n0a4_nonsifr240_pri_2112x1192_sec_skip"
+ "IMX913_ES2_v025_mode037_c0a2_fb60_pri_4224x2640_sec_2112x1320"
+ "IMX913_ES2_v025_mode040_duall_fb60_pri_4224x2640_sec_2112x1320"
+ "IMX913_ES2_v105_mode001_m0a1_ff60_pri_4224x3024_sec_4224x3024"
+ "IMX913_ES2_v105_mode004_c0a1_fb60_pri_4224x3024_sec_2112x1512"
+ "IMX913_ES2_v105_mode008_n1a3_nonsifr60_pri_2112x1512_sec_skip"
+ "IMX913_ES2_v105_mode009_m0a3_nonsifr120_pri_4224x3024_sec_skip"
+ "IMX913_ES2_v105_mode017_c0a2_fb60_pri_4224x2384_sec_2112x1192"
+ "IMX913_ES2_v105_mode021_n1a4_nonsifr60_pri_2112x1192_sec_skip"
+ "IMX913_ES2_v105_mode022_m0a4_nonsifr120_pri_4224x2384_sec_skip"
+ "IMX913_ES2_v105_mode024_n0a4_nonsifr240_pri_2112x1192_sec_skip"
+ "IMX913_ES2_v105_mode037_c0a2_fb60_pri_4224x2640_sec_2112x1320"
+ "IMX913_ES2_v105_mode040_duall_fb60_pri_4224x2640_sec_2112x1320"
+ "Image Rotation Correction \n"
+ "IspLutsMultiDump.bin"
+ "IspRegMultiDump.bin"
+ "LTC grid: ch=%zu cnt=%u %i(%i %i %i %i) -> %i(%i %i %i %i) (%i %i)"
+ "LTM: ch=%zu cnt=%u statsFrCnt=%u"
+ "LUT cache empty, No dump"
+ "Last DMA Start:Stop Ts:%llu:%llu Delta=%d\n"
+ "Lutdump: %.2fms lapsed\n"
+ "MLAF is selected, but MLTiles are invalid! ch%zu t(%d %d)(%d %d %d)\n"
+ "MLAF: A ch%zu regionId=%d nRow=%d ts=%d,%d tc=%d,%d ssr=%d,%d,%d,%d str=%d,%d,%d,%d\n"
+ "MLAF: Conf =[%6.3f,%6.3f,%6.3f,%6.3f,%6.3f,%6.3f,%6.3f,%6.3f,%6.3f,%6.3f]\n"
+ "MLAF: PXdp =[%6.3f,%6.3f,%6.3f,%6.3f,%6.3f,%6.3f,%6.3f,%6.3f,%6.3f,%6.3f]\n"
+ "MLAF: meanG=[%6.3f,%6.3f,%6.3f,%6.3f,%6.3f,%6.3f,%6.3f,%6.3f,%6.3f,%6.3f]\n"
+ "MLAF: model offset=%f slope=%f confTh=%f focusPos=%d MLSelected=%d luxLevel=%d\n"
+ "MLAF: ssR[%d %d %d %d] nRow=%d regionId=%d tileCnt[%d %d] stR[%d %d %d %d] lastMLts=%lld fp=%d\n"
+ "MLAF: updateMlaf ch%zu[%lld] mlSelect()=%d hasMLTiles=%d hasUpdatedMLTiles=%d time=%lld L=%lld\n"
+ "MLAF:CH%zu [PDAF => AC] ROI0      : %4d x %4d @ (%+5d, %+5d)\n"
+ "MLAF:CH%zu [PDAF => AC] ROI0.patch: %4d x %4d @ (%+5d, %+5d) (= %d x %d patches, %d px x %d px)\n"
+ "MLAF:CH%zu [PDAF => AC] ROI1 Enable(%s)  : %4d x %4d @ (%+5d, %+5d)\n"
+ "MLAF:CH%zu [PDAF => AC] ROI1.patch: %4d x %4d @ (%+5d, %+5d) (= %d x %d patches, %d px x %d px)\n"
+ "MLAF:CH%zu [PDAF => AC] ROI2 Enable(%s)  : %4d x %4d @ (%+5d, %+5d)\n"
+ "MLAF:CH%zu [PDAF => AC] ROI2.patch: %4d x %4d @ (%+5d, %+5d) (= %d x %d patches, %d px x %d px)\n"
+ "Map from bes preview output [%d %d %d %d] -> pyr output [%d %d %d %d]\n"
+ "Map from bes preview output [%d %d %d %d] -> sensor config raw [%d %d %d %d]\n"
+ "Map from fes output [%d %d %d %d] -> pyr output [%d %d %d %d]\n"
+ "Map from fes output [%d %d %d %d] -> sensor config raw [%d %d %d %d]\n"
+ "Map from pyr output [%d %d %d %d] -> bes preview output [%d %d %d %d]\n"
+ "Map from pyr preview output [%d %d %d %d] -> fes output [%d %d %d %d]\n"
+ "Map from sensor config raw [%d %d %d %d] -> bes preview output [%d %d %d %d]\n"
+ "Map from sensor config raw [%d %d %d %d] -> fes output [%d %d %d %d]\n"
+ "May  2 2024"
+ "Multi Build Info ComCal \n"
+ "Multi DPC Tagging \n"
+ "NVM header and syscfg header V5 miss match\n"
+ "OIS Z Cal \n"
+ "Override Cal \n"
+ "PDAF Disparity Cal \n"
+ "PDAF: setMlPDAFModelProperty(ch=%zu, value=%d, offset = %d, slope = %d)\n"
+ "PYR [%d %d %d %d] -> %d x %d\n"
+ "PYR: [%d %d %d %d] -> %dx%d, DBG - PYR_1x [%d %d %d %d]\n"
+ "Power not on: %s\n"
+ "ProcWindowService - fhsEn=%d fsclEn=%d pyrEn=%d sbsEn=%d sbsSupportWithFSCL=%d\n"
+ "ProcWindowService - log ch %d frame id %d\n"
+ "QCH Imabalance Shading \n"
+ "REC"
+ "REC "
+ "RegCache empty, No dump"
+ "RegDump: %.2fms lapsed\n"
+ "Regist: status=%u {%3d,%3d,%3d, %3d,%3d,%3d, %3d,%3d,%3d} %%."
+ "STBY"
+ "Sen: [%d %d] -> [%d %d %d %d]\n"
+ "Sensor state 0x%x\n"
+ "Set"
+ "Should have booted to try unwrap\n"
+ "Sphere Cal \n"
+ "Sphere ReCal \n"
+ "SyncTag:0x%x reached max, reset to 1"
+ "Sysmode: 0x%x unexpected for this operation\n"
+ "TIMEWARP: mode=0x%x gyr=%d luma={%3d %3d %3d %3d}%%. fps:%2d.%03d smth=%2d.%.03d"
+ "TM: raw only request not in range i %u idx %d frameType %u qSize %zu"
+ "TM: request not in range i %u idx %d frameType %u qSize %zu depthMax %d"
+ "Tile[%d]: confTh[%d][%d]=%f defocus=%f conf=%d extra=%d valid=%d\n"
+ "Tripod:%u shaking:=%u sameDir:%u (%d deg)"
+ "Unwrap waited %d ms, regval 0x%x\n"
+ "[%s]  %s Dynamic Voltage PVDD to  [%f] V\n"
+ "[%s] CH = 0x%x HFF LACC content is missing!, numDescriptors=%d\n"
+ "[%s] CH = 0x%x STF LACC content is missing!, numDescriptors=%d\n"
+ "[%s] CH = 0x%zu  PYR CROP -> [%d, %d][%d, %d] PYR output [%d, %d]\n"
+ "[%s] CH = 0x%zu MSSync %d Primary Frame Skipping Ratio [%u] %s\n"
+ "[%s] CH = 0x%zx   High Res raw internal buffer %p num %lu size %zu stride %zu %ux%u\n"
+ "[%s] CH = 0x%zx High Res raw internal buffer already setup\n"
+ "[%s] CH = 0x%zx PropertyWrite for SPMI traffic creation, device addr: 0x%02x, I2C bus %zu, # of iterations: %d\n"
+ "[%s] LACC Image File Loading STF PC 0x%x size %d\n"
+ "[DSI] %s: ProcessProjectorCommand() failed"
+ "[DSI] %s: Quark isn't powered on"
+ "[DSI] GetChipState failed (%u)"
+ "[DSI] Transition back to IDLE/ACTIVE failed, state=%u"
+ "_bufferUncached"
+ "ch %d fr %d SBS %d config %d, bFESAllowed=%d, bMsBEPYRScalerAllowed=%d\n"
+ "ch %u ROI %u %u %u %u"
+ "ch%d, Set default purple window size"
+ "imgOCCorrection"
+ "ispRegDump"
+ "pNVMParserFCAMImageOCCorrection class already created\n"
+ "received CISP_CMD_CH_MULTICAM_CAMERA_CONTROL_ROI_SET numCh %u\n"
+ "sensor unexpected state\n"
+ "setOverlayUpperFlags"
+ "sifrSkipInterval %d does not match current decimation table %d period %u"
+ "vc %zu fc %d %s: [%u] e=%u et=%u ag=%u dg=%u scp=%.4f spw=%.4f vfs=%u vft=%u aec=%llu \n"
+ "vc %zu fc %d %s: ts %llu\n"
+ "vc %zu fc %d AE_CONFIG_SET %llu (ag: %u dg: %u ex: %u et: %u vs: %u vst: %u spw: %.0f spc: %.0f) \n"
+ "vc %zu fc %d CIC_CMD_CAPTURE_PREPARE_TO_STOP received\n"
+ "vc %zu fc %d CIC_CMD_CAPTURE_START received\n"
+ "vc %zu fc %d CIC_CMD_CAPTURE_STOP received\n"
+ "vc %zu fc %d CIC_CMD_CONFIGURATION_SET received\n"
+ "vc %zu fc %d CIC_CMD_EXCLAVE_OUTPUT_ENABLE_SET: enable: %u\n"
+ "vc %zu fc %d CIC_CMD_EXCLAVE_STREAMING_START: arming projector for first frame \n"
+ "vc %zu fc %d CIC_CMD_EXCLAVE_STREAMING_START: frameRate %d done\n"
+ "vc %zu fc %d CIC_CMD_LED_TORCH_SET received\n"
+ "vc %zu fc %d CIC_CMD_PROJECTOR_ALLOW_ON received\n"
+ "vc %zu fc %d CIC_CMD_PROJECTOR_LUT_SET received\n"
+ "vc %zu fc %d CIC_CMD_WAIT_FOR_FULL_STOP received\n"
+ "vc %zu fc %d CIL watchdog timer expired\n"
+ "vc %zu fc %d Not dequeueing PIODMA as IC state is %u\n"
+ "vc %zu fc %d capture start task already %s!\n"
+ "vc %zu fc %d ctrlPearl exclave projectorSema %p\n"
+ "vc %zu fc %d enqueue %llu %llu 0x%0x %u %u %u %u %.4f %.4f\n"
+ "vc %zu fc %d exclave fvSyncSema\n"
+ "vc %zu fc %d exclave popAckIrqSema\n"
+ "vc %zu fc %d exclave projectorSema\n"
+ "vc %zu fc %d exclave rvSyncSema\n"
- "  => next: {1/%4dx%3d%%x%3d%%} SIFR{1/%4dx%3d%%x%3d%%} stb=%d req=0x%x"
- "  => next: {1/%4dx%3d%%x%3d%%} stb=%d req=0x%x"
- "  APS Com Single Cal \n"
- "  APS ComCal \n"
- "  BuildInfo  \n"
- "  Color AF Cal  \n"
- "  Color Recal  \n"
- "  Color shading  \n"
- "  DistCal \n"
- "  DistOverlayCal \n"
- "  Dual Build Info \n"
- "  Ext Cal \n"
- "  FPDC \n"
- "  Field Curveture \n"
- "  Multi Build Info ComCal \n"
- "  Multi DPC Tagging \n"
- "  OIS Z Cal \n"
- "  Override Cal \n"
- "  QCH Imabalance Shading \n"
- "  Sphere Cal \n"
- "  Sphere ReCal \n"
- "  preLSC_amplitude_fft_ROI_1            %.9f\n"
- "  preLSC_amplitude_fft_ROI_2            %.9f\n"
- "  preLSC_amplitude_fft_ROI_26            %.9f\n"
- "  preLSC_amplitude_fft_ROI_27            %.9f\n"
- "  preLSC_amplitude_fft_ROI_28            %.9f\n"
- "  preLSC_amplitude_fft_ROI_29            %.9f\n"
- "  preLSC_amplitude_fft_ROI_3            %.9f\n"
- "  preLSC_amplitude_fft_ROI_4            %.9f\n"
- "  preLSC_amplitude_fft_ROI_5            %.9f\n"
- "  preLSC_phase_deg_ROI_1                %.9f\n"
- "  preLSC_phase_deg_ROI_2                %.9f\n"
- "  preLSC_phase_deg_ROI_26                %.9f\n"
- "  preLSC_phase_deg_ROI_27                %.9f\n"
- "  preLSC_phase_deg_ROI_28                %.9f\n"
- "  preLSC_phase_deg_ROI_29                %.9f\n"
- "  preLSC_phase_deg_ROI_3                %.9f\n"
- "  preLSC_phase_deg_ROI_4                %.9f\n"
- "  preLSC_phase_deg_ROI_5                %.9f\n"
- "  preLSC_pitch_mm_ROI_1                %.9f\n"
- "  preLSC_pitch_mm_ROI_2                %.9f\n"
- "  preLSC_pitch_mm_ROI_26                %.9f\n"
- "  preLSC_pitch_mm_ROI_27                %.9f\n"
- "  preLSC_pitch_mm_ROI_28                %.9f\n"
- "  preLSC_pitch_mm_ROI_29                %.9f\n"
- "  preLSC_pitch_mm_ROI_3                %.9f\n"
- "  preLSC_pitch_mm_ROI_4                %.9f\n"
- "  preLSC_pitch_mm_ROI_5                %.9f\n"
- "%.2fms lapsed"
- "%hu+"
- "%lu,%s,%llu,%d,%d\n"
- "%s stream paused @ %llu fl %d\n"
- "%s: [%u] e=%u et=%u ag=%u dg=%u scp=%.4f spw=%.4f vfs=%u vft=%u aec=%llu \n"
- "%s: ch %zu"
- "%s: frameCount=%d %llu\n"
- "./taskHistory%d.txt"
- "./tracefile_%d_%d.bin"
- "00:49:33"
- "2b6cf84"
- ":pdaf:{\"origin\":\"%s\",\"type\":\"%s\",\"ch\":%zu,\"enable\":%s,\"roi\":[%d,%d,%d,%d],..\n"
- "AE:avg=%3u/tgt=%3u {1/%4dx%3d%%x%3d%%}  %9d lux"
- "AE:avg=%3u/tgt=%3u {1/%4dx%3d%%x%3d%%} SIFR{1/%4dx%3d%%x%3d%%} %9d lux"
- "AEIR-PE:# %u, fps %f (%u, %u) fid %s, expT %d (%llu), pat %d(%d), prb %d, skip %d\n"
- "BES Preview [%d %d %d %d] -> %d x %d OutDMA [%d %d %d %d]"
- "CIC_CMD_CAPTURE_PREPARE_TO_STOP received\n"
- "CIC_CMD_CAPTURE_STOP received\n"
- "CIC_CMD_CONFIGURATION_SET received\n"
- "CIC_CMD_EXCLAVE_OUTPUT_ENABLE_SET: enable: %u\n"
- "CIC_CMD_EXCLAVE_SENSOR_AE_CONFIG_SET %llu (ag: %u dg: %u ex: %u et: %u vs: %u vst: %u spw: %.0f spc: %.0f) \n"
- "CIC_CMD_EXCLAVE_STREAMING_START: ch %zu arming projector for first frame \n"
- "CIC_CMD_EXCLAVE_STREAMING_START: ch %zu frameRate %d done\n"
- "CIC_CMD_LED_TORCH_SET received\n"
- "CIC_CMD_PROJECTOR_ALLOW_ON received\n"
- "CIC_CMD_WAIT_FOR_FULL_STOP received\n"
- "CIL watchdog timer expired\n"
- "CMD=CIC_CMD_CAPTURE_START received\n"
- "CTraceEventBuffer.cpp"
- "Create,%lu,%s"
- "DMA: [%d %d %d %d]"
- "DbgOverlay::%s:%d:Set overlay flags 0x%x -> 0x%x\n"
- "Delete,%lu,%s"
- "FDTO-%d: ch %zu,fc %d cfg %d RV %llu.%llu spd %d sifr %d rdOf %u mCh %d syTg 0x%llx\n"
- "FDTO: ch %zu,lnTm %.5f frmTm %f skp %d eM %lld eS %lld vSz %u CIT %lld max %f\n"
- "FES [%d %d %d %d] -> %d x %d"
- "FPS: Fr:%d ms = %6d fps"
- "FileTask"
- "HPR verification failure, status 0x%x\n"
- "IMX913_ES2_v023_mode001_m0a1_ff60_pri_4224x3024_sec_4224x3024"
- "IMX913_ES2_v023_mode004_c0a1_fb60_pri_4224x3024_sec_2112x1512"
- "IMX913_ES2_v023_mode008_n1a3_nonsifr60_pri_2112x1512_sec_skip"
- "IMX913_ES2_v023_mode009_m0a3_nonsifr120_pri_4224x3024_sec_skip"
- "IMX913_ES2_v023_mode017_c0a2_fb60_pri_4224x2384_sec_2112x1192"
- "IMX913_ES2_v023_mode022_m0a4_nonsifr120_pri_4224x2384_sec_skip"
- "IMX913_ES2_v023_mode024_n0a4_nonsifr240_pri_2112x1192_sec_skip"
- "IMX913_ES2_v023_mode037_c0a2_fb60_pri_4224x2640_sec_2112x1320"
- "IMX913_ES2_v023_mode040_duall_fb60_pri_4224x2640_sec_2112x1320"
- "IMX913_ES2_v103_mode001_m0a1_ff60_pri_4224x3024_sec_4224x3024"
- "IMX913_ES2_v103_mode004_c0a1_fb60_pri_4224x3024_sec_2112x1512"
- "IMX913_ES2_v103_mode008_n1a3_nonsifr60_pri_2112x1512_sec_skip"
- "IMX913_ES2_v103_mode009_m0a3_nonsifr120_pri_4224x3024_sec_skip"
- "IMX913_ES2_v103_mode017_c0a2_fb60_pri_4224x2384_sec_2112x1192"
- "IMX913_ES2_v103_mode022_m0a4_nonsifr120_pri_4224x2384_sec_skip"
- "IMX913_ES2_v103_mode024_n0a4_nonsifr240_pri_2112x1192_sec_skip"
- "IMX913_ES2_v103_mode037_c0a2_fb60_pri_4224x2640_sec_2112x1320"
- "IMX913_ES2_v103_mode040_duall_fb60_pri_4224x2640_sec_2112x1320"
- "IRQ disabled time"
- "LTC grid: ch=%zu cnt=%u %i(%u %u %u %u) -> %i(%u %u %u %u) (%u %u)"
- "LTM: statsFrCnt=%u"
- "MLAF: A ch%zu id=%d nRow=%d ts=%d,%d tc=%d,%d ssr=%d,%d,%d,%d str=%d,%d,%d,%d fp=%d SE=%d confTh=%4.3f\n"
- "MLAF: Conf=[%6.2f,%6.2f,%6.2f,%6.2f,%6.2f,%6.2f,%6.2f,%6.2f,%6.2f,%6.2f]\n"
- "MLAF: PXdp=[%6.2f,%6.2f,%6.2f,%6.2f,%6.2f,%6.2f,%6.2f,%6.2f,%6.2f,%6.2f]\n"
- "MLAF: ssR[%d %d %d %d], nRow=%d, tileCount[%d %d], stR[%d %d %d %d], fp=%d\n"
- "MLAF:CH%zu [PDAF => AC] ROI      : %4d x %4d @ (%+5d, %+5d)\n"
- "MLAF:CH%zu [PDAF => AC] ROI.patch: %4d x %4d @ (%+5d, %+5d) (= %d x %d patches, %d px x %d px)\n"
- "MLAFRaw"
- "Map from bes preview output [%d %d %d %d] -> fes output [%d %d %d %d]"
- "Map from bes preview output [%d %d %d %d] -> sensor config raw [%d %d %d %d]"
- "Map from fes output [%d %d %d %d] -> bes preview output [%d %d %d %d]"
- "Map from fes output [%d %d %d %d] -> sensor config raw [%d %d %d %d]"
- "Map from sensor config raw [%d %d %d %d] -> bes preview output [%d %d %d %d]"
- "Map from sensor config raw [%d %d %d %d] -> fes output [%d %d %d %d]"
- "Mar  9 2024"
- "No RPC available or no fileName!"
- "Not dequeueing PIODMA as IC state is %u\n"
- "Performance"
- "SVC"
- "Sen: [%d %d] -> [%d %d %d %d]"
- "TM: request not in range i %u idx %d frameType %u qSize %zu"
- "Thread time"
- "Trace data loss\n"
- "Tripod: %d"
- "Wait for sensor HMAC ok time out\n"
- "Window service log ch %d frame id %d"
- "[%s] CH = 0x%zu Primary Frame Skipping Ratio [%u] %s\n"
- "[%s] CH = 0x%zx   Context Switch still raw internal buffer %p num %lu size %zu stride %zu %ux%u\n"
- "[%s] CH = 0x%zx   Context Switch still raw internal buffer already setup\n"
- "__debug__ bad (row, col) (%d %d) \n"
- "ch %d fr %d SBS %d config %d\n"
- "ctrlPearl exclave projectorSema %p\n"
- "current fes [%d %d %d %d] -> [%d %d]\n"
- "enqueue %llu %llu 0x%0x %u %u %u %u %.4f %.4f\n"
- "exclave fvSyncSema\n"
- "exclave popAckIrqSema\n"
- "exclave projectorSema\n"
- "exclave rvSyncSema\n"

```

#### agx_a000

>  `agx_a000`

```diff

 
-  __TEXT.__text: 0x58834
-  __TEXT.__gxf_code: 0x10ac
+  __TEXT.__text: 0x58940
+  __TEXT.__gxf_code: 0x108c
   __TEXT.__gxf_code_pad: 0x0
-  __TEXT.__const: 0x1510
+  __TEXT.__const: 0x1540
   __TEXT._rtk_patchbay: 0x1e8
+  __TEXT._rtk_tunables: 0x5b0
   __TEXT.__gxf_shr_code: 0x558
-  __TEXT.__cstring: 0x1bb9
+  __TEXT.__cstring: 0x1bce
   __TEXT.__constructor: 0x0
   __TEXT.__chain_starts: 0x0
   __TEXT._rtk_mtab: 0x378
+  __DATA.__gxf_data: 0x41f0
+  __DATA.__data: 0xd78
   __DATA.__const: 0x4c0
   __DATA._rtk_init_stack: 0x4000
   __DATA._rtk_irq_stack: 0x4000
   __DATA._rtk_exc_stack: 0x4000
-  __DATA.__data: 0xd78
-  __DATA.__gxf_data: 0x41f0
+  __DATA._rtk_boot_l1: 0x200
   __DATA._rtk_boot: 0x8000
-  __DATA._rtk_tunables: 0x5b0
   __DATA._rtk_power: 0x358
   __DATA._rtk_page_tables: 0x20000
   __DATA._rtk_threads: 0x0

   __DATA._rtk_heap: 0x0
   __DATA.__zerofill: 0x6b518
   Functions: 0
-  Symbols:   198
-  CStrings:  200
+  Symbols:   199
+  CStrings:  201
 
Symbols:
+ __rtk_armv8_l1_bootstrap
+ __rtk_astris_island
- __rtk_arch_gxf_vector_el0_sync_exception
CStrings:
+ "GFX %s %u %s FW %s! (%s)"
+ "May  2 2024 08:16:18"
+ "range_param_check"
- "GFX %s %s FW %s! (%s)"
- "Mar  8 2024 23:59:04"

```

#### agx_b000

>  `agx_b000`

```diff

 
-  __TEXT.__text: 0x5850c
-  __TEXT.__gxf_code: 0x10ac
+  __TEXT.__text: 0x5862c
+  __TEXT.__gxf_code: 0x108c
   __TEXT.__gxf_code_pad: 0x0
-  __TEXT.__const: 0x1550
+  __TEXT.__const: 0x1580
   __TEXT._rtk_patchbay: 0x1e8
+  __TEXT._rtk_tunables: 0x5b0
   __TEXT.__gxf_shr_code: 0x558
-  __TEXT.__cstring: 0x1bb9
+  __TEXT.__cstring: 0x1bce
   __TEXT.__constructor: 0x0
   __TEXT.__chain_starts: 0x0
   __TEXT._rtk_mtab: 0x378
+  __DATA.__gxf_data: 0x41f0
+  __DATA.__data: 0xd78
   __DATA.__const: 0x4c0
   __DATA._rtk_init_stack: 0x4000
   __DATA._rtk_irq_stack: 0x4000
   __DATA._rtk_exc_stack: 0x4000
-  __DATA.__data: 0xd78
-  __DATA.__gxf_data: 0x41f0
+  __DATA._rtk_boot_l1: 0x200
   __DATA._rtk_boot: 0x8000
-  __DATA._rtk_tunables: 0x5b0
   __DATA._rtk_power: 0x358
   __DATA._rtk_page_tables: 0x20000
   __DATA._rtk_threads: 0x0

   __DATA._rtk_heap: 0x0
   __DATA.__zerofill: 0x6b398
   Functions: 0
-  Symbols:   198
-  CStrings:  200
+  Symbols:   199
+  CStrings:  201
 
Symbols:
+ __rtk_armv8_l1_bootstrap
+ __rtk_astris_island
- __rtk_arch_gxf_vector_el0_sync_exception
CStrings:
+ "GFX %s %u %s FW %s! (%s)"
+ "May  2 2024 08:16:49"
+ "range_param_check"
- "GFX %s %s FW %s! (%s)"
- "Mar  8 2024 23:59:40"

```

#### agx_b100

>  `agx_b100`

```diff

 
-  __TEXT.__text: 0x5850c
-  __TEXT.__gxf_code: 0x10ac
+  __TEXT.__text: 0x5862c
+  __TEXT.__gxf_code: 0x108c
   __TEXT.__gxf_code_pad: 0x0
-  __TEXT.__const: 0x1550
+  __TEXT.__const: 0x1580
   __TEXT._rtk_patchbay: 0x1e8
+  __TEXT._rtk_tunables: 0x5b0
   __TEXT.__gxf_shr_code: 0x558
-  __TEXT.__cstring: 0x1bb9
+  __TEXT.__cstring: 0x1bce
   __TEXT.__constructor: 0x0
   __TEXT.__chain_starts: 0x0
   __TEXT._rtk_mtab: 0x378
+  __DATA.__gxf_data: 0x41f0
+  __DATA.__data: 0xd78
   __DATA.__const: 0x4c0
   __DATA._rtk_init_stack: 0x4000
   __DATA._rtk_irq_stack: 0x4000
   __DATA._rtk_exc_stack: 0x4000
-  __DATA.__data: 0xd78
-  __DATA.__gxf_data: 0x41f0
+  __DATA._rtk_boot_l1: 0x200
   __DATA._rtk_boot: 0x8000
-  __DATA._rtk_tunables: 0x5b0
   __DATA._rtk_power: 0x358
   __DATA._rtk_page_tables: 0x20000
   __DATA._rtk_threads: 0x0

   __DATA._rtk_heap: 0x0
   __DATA.__zerofill: 0x6b398
   Functions: 0
-  Symbols:   198
-  CStrings:  200
+  Symbols:   199
+  CStrings:  201
 
Symbols:
+ __rtk_armv8_l1_bootstrap
+ __rtk_astris_island
- __rtk_arch_gxf_vector_el0_sync_exception
CStrings:
+ "GFX %s %u %s FW %s! (%s)"
+ "May  2 2024 08:17:22"
+ "range_param_check"
- "GFX %s %s FW %s! (%s)"
- "Mar  9 2024 00:00:20"

```

#### ansf.t8130.release.im4p

>  `ansf.t8130.release.im4p`

```diff

 
   __TEXT.text_first: 0x44a0
-  __TEXT.__text: 0x172704
+  __TEXT.__text: 0x1727cc
   __TEXT.shared: 0xb7b0
   __TEXT.read: 0x59d0
   __TEXT.__const: 0x8d68
   __TEXT.idle_hooks: 0x10
-  __TEXT.__cstring: 0x1e5bc
+  __TEXT.__cstring: 0x1e5b9
   __TEXT.__chain_starts: 0x0
   __TEXT.__constructor: 0x0
   __TEXT._rtk_mtab: 0x310
CStrings:
+ "373.120.4"
+ "373.120.4~101"
+ "AppleStorageFirmwarePreASP3-373.120.4~101"
- "373.100.78"
- "373.100.78~159"
- "AppleStorageFirmwarePreASP3-373.100.78~159"

```

#### h16x_ane_fw_iaso_d8x.im4p

>  `h16x_ane_fw_iaso_d8x.im4p`

```diff

 
-  __TEXT.__text: 0xa4ba0
+  __TEXT.__text: 0xa53f8
   __TEXT.__data_copy: 0x8000
   __TEXT.__const: 0x8388
-  __TEXT.__cstring: 0x19490
+  __TEXT.__cstring: 0x19533
   __TEXT._rtk_mtab: 0x288
   __TEXT.__constructor: 0x0
   __TEXT.__chain_starts: 0x0
   __TEXT.text_env: 0x28
-  __DATA.__const: 0x4ab0
+  __DATA.__const: 0x4a90
   __DATA._rtk_heap: 0x1000
   __DATA.__data: 0xf58
   __DATA._rtk_patchbay: 0x1e8

   __DATA._rtk_page_tables: 0x3c0000
   __DATA._rtk_threads: 0x0
   __DATA._fwinfo: 0x100
+  __DATA._rtk_boot_l1: 0x80
   __DATA.__mod_init_func: 0x0
   __DATA.__noinit: 0x0
   __DATA.__zerofill: 0x53f28
   Functions: 0
   Symbols:   0
-  CStrings:  3181
+  CStrings:  3186
 
CStrings:
+ "08:09:53"
+ "Cannot find nid %d"
+ "Cannot find nid %d with tid %d event %d"
+ "May  2 2024"
+ "local copy of pAneProgramDesc2 was not allocated"
+ "pAneProgramDesc2 != __null"
+ "pMsg->bufNbr == 1 + pAneProgramDesc2->procedures[pProgCallSubPacket->procedureId].numIoBuffers"
+ "setEnableDynamicPowerGate"
+ "setStartTimestamp"
- "23:51:17"
- "Mar  8 2024"
- "SwitchDynamicPowerGate"
- "pMsg->bufNbr == 1 + pProgDesc->procedures[pProgCallSubPacket->procedureId].numIoBuffers"

```

#### rans.t8130.release.im4p

>  `rans.t8130.release.im4p`

```diff

 
   __TEXT.text_first: 0x44a0
-  __TEXT.__text: 0x172704
+  __TEXT.__text: 0x1727cc
   __TEXT.shared: 0xb7b0
   __TEXT.read: 0x59d0
   __TEXT.__const: 0x8d68
   __TEXT.idle_hooks: 0x10
-  __TEXT.__cstring: 0x1e5bc
+  __TEXT.__cstring: 0x1e5b9
   __TEXT.__chain_starts: 0x0
   __TEXT.__constructor: 0x0
   __TEXT._rtk_mtab: 0x310
CStrings:
+ "373.120.4"
+ "373.120.4~101"
+ "AppleStorageFirmwarePreASP3-373.120.4~101"
- "373.100.78"
- "373.100.78~159"
- "AppleStorageFirmwarePreASP3-373.100.78~159"

```

#### sptm.t8122.release.im4p

>  `sptm.t8122.release.im4p`

```diff

-194.102.1.0.0
-  __TEXT.__cstring: 0x9fee
+194.122.2.0.0
+  __TEXT.__cstring: 0xa28d
   __TEXT.__binname: 0x40
   __TEXT.__chain_starts: 0x1c
-  __TEXT.__const: 0x4a0
-  __DATA_CONST.__const: 0x4c5a8
-  __TEXT_EXEC.__text: 0x30fe0
+  __TEXT.__const: 0x4b8
+  __DATA_CONST.__const: 0x4c638
+  __TEXT_EXEC.__text: 0x31c40
   __LAST.__pinst: 0x8
   __DATA.__data: 0x16
-  __DATA.__common: 0x7121
-  __DATA.__bss: 0x4d08
+  __DATA.__common: 0x7150
+  __DATA.__bss: 0x4e70
   __BOOTDATA.__data: 0x14000
-  Functions: 230
+  Functions: 235
   Symbols:   1
-  CStrings:  1274
+  CStrings:  1293
 
CStrings:
+ "%s: Could not find /defaults"
+ "%s: Error looking up /chosen/%s"
+ "ACQ doesnt match the previously cached value !"
+ "AQA doesnt match the previously cached value !"
+ "ASQ doesnt match the previously cached value !"
+ "IOCQ doesnt match the previously cached value !"
+ "IOQA doesnt match the previously cached value !"
+ "IOSQ doesnt match the previously cached value !"
+ "Not enough SK entropy"
+ "asq_length/acq_length out of range. asq_length: %u, acq_length: %u\n"
+ "cl4-entropy"
+ "nvme-iboot-sptm-security"
+ "nvme-secure-bar"
+ "shared_tte"
+ "sptm_t8110dart_sk_power_assert"
+ "sptm_t8110dart_sk_power_release"
+ "t8110dart %p (%s:%u): power down not permitted as SK still using the DART"
+ "t8110dart_enable_translation"
+ "t8110dart_invalidate_tlb"
+ "t8110dart_tlbi_start"
- "%s: Error looking up /chosen/random-seed"

```

#### t8130dcp.im4p

>  `t8130dcp.im4p`

```diff

 
-  __TEXT.__text: 0x2b1408
-  __TEXT.__const: 0x7b074
-  __TEXT.__cstring: 0x2dd61
+  __TEXT.__text: 0x2b3074
+  __TEXT.__const: 0x7b21c
+  __TEXT.__cstring: 0x2d989
   __TEXT.__chain_starts: 0x160
   __DATA.__constructor: 0x8
-  __DATA.__const: 0x47828
+  __DATA.__const: 0x47b08
   __DATA._rtk_patchbay: 0x710
-  __DATA.__data: 0x2ba70
+  __DATA.__data: 0x2bac0
   __DATA._rtk_boot: 0x6000
   __DATA._rtk_page_tables: 0xc0000
   __DATA._rtk_power: 0x3b8

   __DATA.__mod_init_func: 0x90
   __DATA._afk_sys_objt: 0xb60
   __DATA._rtk_mtab: 0x5b0
-  __DATA.__zerofill: 0x9c870
-  __OS_LOG.__string: 0x1ed28
-  Functions: 6411
+  __DATA.__zerofill: 0x9c868
+  __OS_LOG.__string: 0x1ed47
+  Functions: 6434
   Symbols:   0
-  CStrings:  5741
+  CStrings:  5771
 
CStrings:
+ " IOMFB: BIC RD Decompress Error detected "
+ "%s::%s(): ALPM not disabled from VFTG! COMMON_INT_STA_1=0x%0x"
+ "%s::%s(): Failed to clear DPTX_VIDEO_STATUS_VIDEO_SENDING_EN_S within %dms"
+ "Child must override"
+ "DCPExpert failed to wait for management route"
+ "Dealloacte dummy_pdc\n"
+ "ForceSecureAnimation"
+ "IOMFBIndicatorBrightnessNits"
+ "IOMFBSecureContentFactor"
+ "IOMFBSecureIndicatorFactor"
+ "IRDCFrameMaxResetCount"
+ "IRDCFrameMinResetCount"
+ "IRDCFrameReset"
+ "LTH median not converging chan=%u min=%u max=%u\n"
+ "SWAP_WAIT_DEBUG: start_record_dmem_info called\n"
+ "SwitchToInternalALPMOverride"
+ "[AFK]%s: Invalid command (%i < %zu)"
+ "[AFK]%s: Invalid command (%zu < %zu)"
+ "dcp_kdebug_capacity"
+ "dcp_kdebug_threshold"
+ "disableVideoStream"
+ "e: ACSS EMMP exceeding max brightness count: %u > %u\n"
+ "e: ACSS EMMP exceeding max temperature count: %u > %u\n"
+ "e: ACSS: set_block_cb failed\n"
+ "e: ALSS EMMP exceeding max brightness count: %u > %u\n"
+ "e: ALSS EMMP exceeding max temperature count: %u > %u\n"
+ "e: ALSS: set_block_cb_failed\n"
+ "e: Bad size/version for HGOD\n"
+ "e: Bad size/version for aftg\n"
+ "e: Could not find PRC tables [%d:%d:%d] [%d:%d:%d]\n"
+ "e: Could not find PRC tables [%d:%d:%d] for bins [%d:%d]\n"
+ "e: Counted vectors [%d][%d] mismatch expected [%d][%d]\n"
+ "e: DC or PM LUT size too big\n"
+ "e: DCLUT[%d, %d, %d, %d, %d, %d] is all zeros\n"
+ "e: DPCl: Data size insufficient for the taps \n"
+ "e: DPCl: More brightness taps( %d ) then expected (%d) \n"
+ "e: DPCl: More temperature taps( %d ) then expected (%d) \n"
+ "e: Duplicate PDC table (bin=%d temp=%d bright=%d sf=%d param=%d chan=%X) found in input.\n"
+ "e: Duplicate PTUC table vers=%d (bright=%d, temp=%d) found in input.\n"
+ "e: Duplicate elvs table temperature=%d found in input.\n"
+ "e: EMMK exceeding max brightness count: %u > %u\n"
+ "e: EMMK exceeding max temperature count: %u > %u\n"
+ "e: EMMP table for ACSS is NULL\n"
+ "e: EMMP table for ALSS is NULL\n"
+ "e: Failed to sort EMMP tables\n"
+ "e: Failed to sort async PCS tables\n"
+ "e: Failed to sort sync PCS tables\n"
+ "e: GSC exceeding max brightness count: %u > %u\n"
+ "e: GSC exceeding max temperature count: %u > %u\n"
+ "e: GSC table is NULL\n"
+ "e: IRDC Block data and header size mismatch by %d too many bytes\n"
+ "e: Illegal channel code %c\n"
+ "e: LLMT APL Thresholds not in descending order\n"
+ "e: LLMT DBV Thresholds not in ascending order\n"
+ "e: LLMT Max DBV Threshold doesn't correspond to 0%% APL\n"
+ "e: PCS exceeding max brightness count: %u > %u\n"
+ "e: PCS exceeding max temperature count: %u > %u\n"
+ "e: PCS table is NULL\n"
+ "e: PCS tables are NULL\n"
+ "e: PDC missing at least 1 channel\n"
+ "e: PDC missing bin\n"
+ "e: PMLUT[%d, %d, %d, %d, %d, %d] is all zeros\n"
+ "e: PP LUT missing color channel\n"
+ "e: PRC table not well formed\n"
+ "e: Prox PD bin tables do no correlate\n"
+ "e: Prox PP bin tables do no correlate\n"
+ "e: Step values should be nonzero\n"
+ "e: The data size ( %d )is actually lesser than remaining bytes ( %d )\n"
+ "e: Too many index values for LUT tables\n"
+ "e: UPCL set DPCL data failed\n"
+ "e: Undefined EEPROM version 0x%x, expected 0x%x\n"
+ "e: Unexpected BLAH block version 0x%x\n"
+ "e: Unexpected BLTS block version 0x%x\n"
+ "e: Unexpected DPCL block version 0x%x\n"
+ "e: Unexpected RXTK block version 0x%x\n"
+ "e: Vector exceeding max i count: %u > %u\n"
+ "e: Vector exceeding max j count: %u > %u\n"
+ "e: actual number of Prox LUTs differ from specified\n"
+ "e: bin mix factor must be between 0 and 1\n"
+ "e: bin tables do not correlate.\n"
+ "e: block %s not well formed size %d remaining %d\n"
+ "e: channel not specified\n"
+ "e: data size %d mismatch header %d\n"
+ "e: duplicate PRC table found in input\n"
+ "e: duplicate tables\n"
+ "e: expected 3 color channels\n"
+ "e: failed to process block %s\n"
+ "e: failed to set ELVS LUT temperature %d\n"
+ "e: failed to set ELVS table config\n"
+ "e: failed to set LLMT table config\n"
+ "e: failed to set LUS LUT [%d %d %d]\n"
+ "e: failed to set LUS table config\n"
+ "e: failed to set PDC LUT [%d %d %d %d] \n"
+ "e: failed to set PDC table config\n"
+ "e: failed to set PRC LUT [t%d s%d b%d p%d]\n"
+ "e: failed to set PRC table config\n"
+ "e: failed to set PTUC TLS LUT brightness %d\n"
+ "e: failed to set PTUC table config\n"
+ "e: failed to set Prox PD LUT [t %d]\n"
+ "e: failed to set Prox PP LUT [t %d b %d p %d]\n"
+ "e: failed to set prox table config\n"
+ "e: frame repeat LUT incomplete, only %d/%d provided\n"
+ "e: illegal frame count %d\n"
+ "e: incoming data not well formed\n"
+ "e: inconsistent DC index\n"
+ "e: inconsistent PM index\n"
+ "e: inconsistent nframes value\n"
+ "e: input data not well-formed\n"
+ "e: invalid acss_config version %u\n"
+ "e: invalid block length for block %s\n"
+ "e: invalid header\n"
+ "e: lerped DCLUT[%d, %d, %d, %d, %d] is all zeros"
+ "e: lerped DCLUT[%d, %d, %d, %d] is all zeros"
+ "e: lerped PMLUT[%d, %d, %d, %d, %d] is all zeros"
+ "e: lerped PMLUT[%d, %d, %d, %d] is all zeros"
+ "e: lut size too big\n"
+ "e: lut sizes should be the same\n"
+ "e: missing LUS LUTs\n"
+ "e: missing PDC LUTs\n"
+ "e: missing PRC LUTs\n"
+ "e: missing PTUC LUTs\n"
+ "e: missing prox PD table bin %d\n"
+ "e: missing prox PP table bin %d\n"
+ "e: no data\n"
+ "e: no valid set block callback\n"
+ "e: not enough durations provided for LUS LUTs\n"
+ "e: processed ALSS EMMP dimensions (temp %u, bright %u)mismatch specified values (temp %u, bright %u)\n"
+ "e: provided min or max durations (%d, %d) invalid\n"
+ "e: prox LUTs should come after config parameters\n"
+ "e: ramp down configurations should be nonzero\n"
+ "e: reported PDC tap points (temp/DBV/RR/HGOD status) mismatch actual counts\n"
+ "e: set BCAL data failed\n"
+ "e: set BLAH data failed\n"
+ "e: set BLTS data failed\n"
+ "e: set CA data failed\n"
+ "e: set DBMA data failed\n"
+ "e: set DPCl data failed\n"
+ "e: set HGOD data failed\n"
+ "e: set HSPC data failed\n"
+ "e: set IRDC data failed\n"
+ "e: set PSFA data failed\n"
+ "e: set PSFM data failed\n"
+ "e: set QETC data failed\n"
+ "e: set QETC data failed. Too many brightness levels. \n"
+ "e: set RXTK data failed\n"
+ "e: set TLSC data failed\n"
+ "e: set TLSC data failed. Too many frequency levels. \n"
+ "e: set USPC data failed\n"
+ "e: set user_cal_aft_gain failed\n"
+ "e: unexpected LLMT block size %d\n"
+ "e: unexpected LLMT block version %d\n"
+ "e: unexpected PBDD block size 0x%x != 0x%x\n"
+ "e: unexpected PBDD version %d\n"
+ "e: unexpected PBDS block size 0x%x != 0x%x\n"
+ "e: unexpected PBDS version %d\n"
+ "e: unexpected PBDp block size %d\n"
+ "e: unexpected PBDp block version %d\n"
+ "e: unexpected PDC table version %d\n"
+ "e: unexpected PRCW block size %d\n"
+ "e: unexpected block size %d\n"
+ "e: unexpected block version %d\n"
+ "e: unexpected number of backlight sections %d\n"
+ "e: unexpected number of bins %d\n"
+ "e: unexpected value for polarity %d\n"
+ "e: unexpected version %d for PDCc block\n"
+ "e: unexpected version %d for PDCp block\n"
+ "e: unknown backlight section %d\n"
+ "e: unknown block name %s\n"
+ "e: unknown header block name %s\n"
+ "e: unspecified PD LUT temperature value %d C\n"
+ "e: unspecified PP LUT brightness %d\n"
+ "e: unspecified PP LUT scan plan 0x%x\n"
+ "e: unspecified PP LUT temperature %d C\n"
+ "e: unsupported number of color channels\n"
+ "e: useless PDC table\n"
+ "hard_power_state %d fTimingsUpdatePowerState %d fControllerPowerState %d fSoftPowerState %d  newCtrlrState %d \n"
+ "i:  UPCL set DPCL data succeeded\n"
+ "i: PDC bin interpolation, bin = 0x%x\n"
+ "i: PDC mix bin %g and bin %g with %g --> %g\n"
+ "i: PDC params version %d\n"
+ "i: Processing BLAH format version %d data version %d\n"
+ "i: Processing BLTS format version %d data version %d\n"
+ "i: Processing RXTK format version %d data version %d\n"
+ "i: Prox PD LUT bin interpolation, bin = 0x%x\n"
+ "i: Prox PP LUT bin interpolation, bin = 0x%x\n"
+ "i: Set ALSS EM config success\n"
+ "i: all done\n"
+ "i: processing prox data version %d\n"
+ "i: set BCAL data succeeded\n"
+ "i: set BLAH data succeeded\n"
+ "i: set BLTS data succeeded\n"
+ "i: set CA data succeeded\n"
+ "i: set DBMA data succeeded\n"
+ "i: set DPCl data succeeded\n"
+ "i: set ELVS table config succeeded\n"
+ "i: set EVLS LUTs succeeded\n"
+ "i: set HGOD data succeeded\n"
+ "i: set HSPC data succeeded\n"
+ "i: set IRDC data succeeded\n"
+ "i: set LLMT table config succeeded\n"
+ "i: set LUS LUTs succeeded\n"
+ "i: set LUS table config succeeded\n"
+ "i: set PDC LUTs succeeded\n"
+ "i: set PDC table config succeeded\n"
+ "i: set PRC LUTs succeeded\n"
+ "i: set PRC table config succeeded\n"
+ "i: set PSFA data succeeded\n"
+ "i: set PSFM data succeeded\n"
+ "i: set PTUC TLS LUTs succeeded\n"
+ "i: set PTUC table config succeeded\n"
+ "i: set Prox LUTs succeeded\n"
+ "i: set QETC data succeeded\n"
+ "i: set RXTK data succeeded"
+ "i: set TLSC data succeeded\n"
+ "i: set USPC data succeeded\n"
+ "i: set prox table config succeeded\n"
+ "i: set user_cal_aft_gain succeeded\n"
+ "iomfb_RuntimeProperty_IRDCFrameMaxResetCount"
+ "iomfb_RuntimeProperty_IRDCFrameMinResetCount"
+ "iomfb_RuntimeProperty_IRDCFrameReset"
+ "iomfb_RuntimeProperty_forceSecureAnimationUpdate"
+ "iomfb_RuntimeProperty_indicatorBrightnessNits"
+ "iomfb_RuntimeProperty_secureContentFactor"
+ "iomfb_RuntimeProperty_secureIndicatorFactor"
+ "iomfb_RuntimeProperty_usePodBoostAtRTPLCFDLUT"
+ "refresh-rate"
+ "usePodBoostAtRTPLCFDLUT"
+ "virtual bool IOMobileFramebuffer::getDebugInfoBufferJob(uint32_t *, uint32_t *)"
- "%s: Async Swap request landing on unsupported platform. Force panic\n"
- "average-refresh-rate"
- "parser_error: ACSS EMMP exceeding max brightness count: %u > %u\n"
- "parser_error: ACSS EMMP exceeding max temperature count: %u > %u\n"
- "parser_error: ACSS: set_block_cb failed\n"
- "parser_error: ALSS EMMP exceeding max brightness count: %u > %u\n"
- "parser_error: ALSS EMMP exceeding max temperature count: %u > %u\n"
- "parser_error: ALSS: set_block_cb_failed\n"
- "parser_error: Bad size/version for HGOD\n"
- "parser_error: Bad size/version for aftg\n"
- "parser_error: Could not find PRC tables [%d:%d:%d] [%d:%d:%d]\n"
- "parser_error: Could not find PRC tables [%d:%d:%d] for bins [%d:%d]\n"
- "parser_error: Counted vectors [%d][%d] mismatch expected [%d][%d]\n"
- "parser_error: DC or PM LUT size too big\n"
- "parser_error: DCLUT[%d, %d, %d, %d, %d, %d] is all zeros\n"
- "parser_error: DPCl: Data size insufficient for the taps \n"
- "parser_error: DPCl: More brightness taps( %d ) then expected (%d) \n"
- "parser_error: DPCl: More temperature taps( %d ) then expected (%d) \n"
- "parser_error: Duplicate PDC table (bin=%d temp=%d bright=%d sf=%d param=%d chan=%X) found in input.\n"
- "parser_error: Duplicate PTUC table vers=%d (bright=%d, temp=%d) found in input.\n"
- "parser_error: Duplicate elvs table temperature=%d found in input.\n"
- "parser_error: EMMK exceeding max brightness count: %u > %u\n"
- "parser_error: EMMK exceeding max temperature count: %u > %u\n"
- "parser_error: EMMP table for ACSS is NULL\n"
- "parser_error: EMMP table for ALSS is NULL\n"
- "parser_error: Failed to sort EMMP tables\n"
- "parser_error: Failed to sort async PCS tables\n"
- "parser_error: Failed to sort sync PCS tables\n"
- "parser_error: GSC exceeding max brightness count: %u > %u\n"
- "parser_error: GSC exceeding max temperature count: %u > %u\n"
- "parser_error: GSC table is NULL\n"
- "parser_error: IRDC Block data and header size mismatch by %d too many bytes\n"
- "parser_error: Illegal channel code %c\n"
- "parser_error: LLMT APL Thresholds not in descending order\n"
- "parser_error: LLMT DBV Thresholds not in ascending order\n"
- "parser_error: LLMT Max DBV Threshold doesn't correspond to 0%% APL\n"
- "parser_error: PCS exceeding max brightness count: %u > %u\n"
- "parser_error: PCS exceeding max temperature count: %u > %u\n"
- "parser_error: PCS table is NULL\n"
- "parser_error: PCS tables are NULL\n"
- "parser_error: PDC missing at least 1 channel\n"
- "parser_error: PDC missing bin\n"
- "parser_error: PMLUT[%d, %d, %d, %d, %d, %d] is all zeros\n"
- "parser_error: PP LUT missing color channel\n"
- "parser_error: PRC table not well formed\n"
- "parser_error: Prox PD bin tables do no correlate\n"
- "parser_error: Prox PP bin tables do no correlate\n"
- "parser_error: Step values should be nonzero\n"
- "parser_error: The data size ( %d )is actually lesser than remaining bytes ( %d )\n"
- "parser_error: Too many index values for LUT tables\n"
- "parser_error: UPCL set DPCL data failed\n"
- "parser_error: Undefined EEPROM version 0x%x, expected 0x%x\n"
- "parser_error: Unexpected BLAH block version 0x%x\n"
- "parser_error: Unexpected BLTS block version 0x%x\n"
- "parser_error: Unexpected DPCL block version 0x%x\n"
- "parser_error: Unexpected RXTK block version 0x%x\n"
- "parser_error: Vector exceeding max i count: %u > %u\n"
- "parser_error: Vector exceeding max j count: %u > %u\n"
- "parser_error: actual number of Prox LUTs differ from specified\n"
- "parser_error: bin mix factor must be between 0 and 1\n"
- "parser_error: bin tables do not correlate.\n"
- "parser_error: block %s not well formed size %d remaining %d\n"
- "parser_error: channel not specified\n"
- "parser_error: data size %d mismatch header %d\n"
- "parser_error: duplicate PRC table found in input\n"
- "parser_error: duplicate tables\n"
- "parser_error: expected 3 color channels\n"
- "parser_error: failed to process block %s\n"
- "parser_error: failed to set ELVS LUT temperatue %d\n"
- "parser_error: failed to set ELVS table config\n"
- "parser_error: failed to set LLMT table config\n"
- "parser_error: failed to set LUS LUT [%d %d %d]\n"
- "parser_error: failed to set LUS table config\n"
- "parser_error: failed to set PDC LUT [%d %d %d %d] \n"
- "parser_error: failed to set PDC table config\n"
- "parser_error: failed to set PRC LUT [t%d s%d b%d p%d]\n"
- "parser_error: failed to set PRC table config\n"
- "parser_error: failed to set PTUC TLS LUT brightness %d\n"
- "parser_error: failed to set PTUC table config\n"
- "parser_error: failed to set Prox PD LUT [t %d]\n"
- "parser_error: failed to set Prox PP LUT [t %d b %d p %d]\n"
- "parser_error: failed to set prox table config\n"
- "parser_error: frame repeat LUT incomplete, only %d/%d provided\n"
- "parser_error: illegal frame count %d\n"
- "parser_error: incoming data not well formed\n"
- "parser_error: inconsistent DC index\n"
- "parser_error: inconsistent PM index\n"
- "parser_error: inconsistent nframes value\n"
- "parser_error: input data not well-formed\n"
- "parser_error: invalid acss_config version %u\n"
- "parser_error: invalid block length for block %s\n"
- "parser_error: invalid header\n"
- "parser_error: lerped DCLUT[%d, %d, %d, %d, %d] is all zeros"
- "parser_error: lerped DCLUT[%d, %d, %d, %d] is all zeros"
- "parser_error: lerped PMLUT[%d, %d, %d, %d, %d] is all zeros"
- "parser_error: lerped PMLUT[%d, %d, %d, %d] is all zeros"
- "parser_error: lut size too big\n"
- "parser_error: lut sizes should be the same\n"
- "parser_error: missing LUS LUTs\n"
- "parser_error: missing PDC LUTs\n"
- "parser_error: missing PRC LUTs\n"
- "parser_error: missing PTUC LUTs\n"
- "parser_error: missing prox PD table bin %d\n"
- "parser_error: missing prox PP table bin %d\n"
- "parser_error: no data\n"
- "parser_error: no valid set block callback\n"
- "parser_error: not enough durations provided for LUS LUTs\n"
- "parser_error: processed ALSS EMMP dimensions (temp %u, bright %u)mismatch specified values (temp %u, bright %u)\n"
- "parser_error: provided min or max durations (%d, %d) invalid\n"
- "parser_error: prox LUTs should come after config parameters\n"
- "parser_error: ramp down configurations should be nonzero\n"
- "parser_error: reported PDC tap points (temp/DBV/RR/HGOD status) mismatch actual counts\n"
- "parser_error: set BCAL data failed\n"
- "parser_error: set BLAH data failed\n"
- "parser_error: set BLTS data failed\n"
- "parser_error: set CA data failed\n"
- "parser_error: set DBMA data failed\n"
- "parser_error: set DPCl data failed\n"
- "parser_error: set HGOD data failed\n"
- "parser_error: set HSPC data failed\n"
- "parser_error: set IRDC data failed\n"
- "parser_error: set PSFA data failed\n"
- "parser_error: set PSFM data failed\n"
- "parser_error: set QETC data failed\n"
- "parser_error: set QETC data failed. Too many brightness levels. \n"
- "parser_error: set RXTK data failed\n"
- "parser_error: set TLSC data failed\n"
- "parser_error: set TLSC data failed. Too many frequency levels. \n"
- "parser_error: set USPC data failed\n"
- "parser_error: set user_cal_aft_gain failed\n"
- "parser_error: unexpected LLMT block size %d\n"
- "parser_error: unexpected LLMT block version %d\n"
- "parser_error: unexpected PBDD block size 0x%x != 0x%x\n"
- "parser_error: unexpected PBDD version %d\n"
- "parser_error: unexpected PBDS block size 0x%x != 0x%x\n"
- "parser_error: unexpected PBDS version %d\n"
- "parser_error: unexpected PBDp block size %d\n"
- "parser_error: unexpected PBDp block version %d\n"
- "parser_error: unexpected PDC table version %d\n"
- "parser_error: unexpected PRCW block size %d\n"
- "parser_error: unexpected block size %d\n"
- "parser_error: unexpected block version %d\n"
- "parser_error: unexpected number of backlight sections %d\n"
- "parser_error: unexpected number of bins %d\n"
- "parser_error: unexpected value for polarity %d\n"
- "parser_error: unexpected version %d for PDCc block\n"
- "parser_error: unexpected version %d for PDCp block\n"
- "parser_error: unknown backlight section %d\n"
- "parser_error: unknown block name %s\n"
- "parser_error: unknown header block name %s\n"
- "parser_error: unspecified PD LUT temperature value %d C\n"
- "parser_error: unspecified PP LUT brightness %d\n"
- "parser_error: unspecified PP LUT scan plan 0x%x\n"
- "parser_error: unspecified PP LUT temperature %d C\n"
- "parser_error: unsupported number of color channels\n"
- "parser_error: useless PDC table\n"
- "parser_info:  UPCL set DPCL data succeeded\n"
- "parser_info: PDC bin interpolation, bin = 0x%x\n"
- "parser_info: PDC mix bin %g and bin %g with %g --> %g\n"
- "parser_info: PDC params version %d\n"
- "parser_info: Processing BLAH format version %d data version %d\n"
- "parser_info: Processing BLTS format version %d data version %d\n"
- "parser_info: Processing RXTK format version %d data version %d\n"
- "parser_info: Prox PD LUT bin interpolation, bin = 0x%x\n"
- "parser_info: Prox PP LUT bin interpolation, bin = 0x%x\n"
- "parser_info: Set ALSS EM config success\n"
- "parser_info: all done\n"
- "parser_info: processing prox data version %d\n"
- "parser_info: set BCAL data succeeded\n"
- "parser_info: set BLAH data succeeded\n"
- "parser_info: set BLTS data succeeded\n"
- "parser_info: set CA data succeeded\n"
- "parser_info: set DBMA data succeeded\n"
- "parser_info: set DPCl data succeeded\n"
- "parser_info: set ELVS table config succeeded\n"
- "parser_info: set EVLS LUTs succeeded\n"
- "parser_info: set HGOD data succeeded\n"
- "parser_info: set HSPC data succeeded\n"
- "parser_info: set IRDC data succeeded\n"
- "parser_info: set LLMT table config succeeded\n"
- "parser_info: set LUS LUTs succeeded\n"
- "parser_info: set LUS table config succeeded\n"
- "parser_info: set PDC LUTs succeeded\n"
- "parser_info: set PDC table config succeeded\n"
- "parser_info: set PRC LUTs succeeded\n"
- "parser_info: set PRC table config succeeded\n"
- "parser_info: set PSFA data succeeded\n"
- "parser_info: set PSFM data succeeded\n"
- "parser_info: set PTUC TLS LUTs succeeded\n"
- "parser_info: set PTUC table config succeeded\n"
- "parser_info: set Prox LUTs succeeded\n"
- "parser_info: set QETC data succeeded\n"
- "parser_info: set RXTK data succeeded"
- "parser_info: set TLSC data succeeded\n"
- "parser_info: set USPC data succeeded\n"
- "parser_info: set prox table config succeeded\n"
- "parser_info: set user_cal_aft_gain succeeded\n"
- "virtual bool IOMobileFramebuffer::writeDebugInfoJob(uintptr_t)"

```

#### t8130dcp_restore.im4p

>  `t8130dcp_restore.im4p`

```diff

 
-  __TEXT.__text: 0x2b1408
-  __TEXT.__const: 0x7b074
-  __TEXT.__cstring: 0x2dd61
+  __TEXT.__text: 0x2b3074
+  __TEXT.__const: 0x7b21c
+  __TEXT.__cstring: 0x2d989
   __TEXT.__chain_starts: 0x160
   __DATA.__constructor: 0x8
-  __DATA.__const: 0x47828
+  __DATA.__const: 0x47b08
   __DATA._rtk_patchbay: 0x710
-  __DATA.__data: 0x2ba70
+  __DATA.__data: 0x2bac0
   __DATA._rtk_boot: 0x6000
   __DATA._rtk_page_tables: 0xc0000
   __DATA._rtk_power: 0x3b8

   __DATA.__mod_init_func: 0x90
   __DATA._afk_sys_objt: 0xb60
   __DATA._rtk_mtab: 0x5b0
-  __DATA.__zerofill: 0x9c870
-  __OS_LOG.__string: 0x1ed28
-  Functions: 6411
+  __DATA.__zerofill: 0x9c868
+  __OS_LOG.__string: 0x1ed47
+  Functions: 6434
   Symbols:   0
-  CStrings:  5741
+  CStrings:  5771
 
CStrings:
+ " IOMFB: BIC RD Decompress Error detected "
+ "%s::%s(): ALPM not disabled from VFTG! COMMON_INT_STA_1=0x%0x"
+ "%s::%s(): Failed to clear DPTX_VIDEO_STATUS_VIDEO_SENDING_EN_S within %dms"
+ "Child must override"
+ "DCPExpert failed to wait for management route"
+ "Dealloacte dummy_pdc\n"
+ "ForceSecureAnimation"
+ "IOMFBIndicatorBrightnessNits"
+ "IOMFBSecureContentFactor"
+ "IOMFBSecureIndicatorFactor"
+ "IRDCFrameMaxResetCount"
+ "IRDCFrameMinResetCount"
+ "IRDCFrameReset"
+ "LTH median not converging chan=%u min=%u max=%u\n"
+ "SWAP_WAIT_DEBUG: start_record_dmem_info called\n"
+ "SwitchToInternalALPMOverride"
+ "[AFK]%s: Invalid command (%i < %zu)"
+ "[AFK]%s: Invalid command (%zu < %zu)"
+ "dcp_kdebug_capacity"
+ "dcp_kdebug_threshold"
+ "disableVideoStream"
+ "e: ACSS EMMP exceeding max brightness count: %u > %u\n"
+ "e: ACSS EMMP exceeding max temperature count: %u > %u\n"
+ "e: ACSS: set_block_cb failed\n"
+ "e: ALSS EMMP exceeding max brightness count: %u > %u\n"
+ "e: ALSS EMMP exceeding max temperature count: %u > %u\n"
+ "e: ALSS: set_block_cb_failed\n"
+ "e: Bad size/version for HGOD\n"
+ "e: Bad size/version for aftg\n"
+ "e: Could not find PRC tables [%d:%d:%d] [%d:%d:%d]\n"
+ "e: Could not find PRC tables [%d:%d:%d] for bins [%d:%d]\n"
+ "e: Counted vectors [%d][%d] mismatch expected [%d][%d]\n"
+ "e: DC or PM LUT size too big\n"
+ "e: DCLUT[%d, %d, %d, %d, %d, %d] is all zeros\n"
+ "e: DPCl: Data size insufficient for the taps \n"
+ "e: DPCl: More brightness taps( %d ) then expected (%d) \n"
+ "e: DPCl: More temperature taps( %d ) then expected (%d) \n"
+ "e: Duplicate PDC table (bin=%d temp=%d bright=%d sf=%d param=%d chan=%X) found in input.\n"
+ "e: Duplicate PTUC table vers=%d (bright=%d, temp=%d) found in input.\n"
+ "e: Duplicate elvs table temperature=%d found in input.\n"
+ "e: EMMK exceeding max brightness count: %u > %u\n"
+ "e: EMMK exceeding max temperature count: %u > %u\n"
+ "e: EMMP table for ACSS is NULL\n"
+ "e: EMMP table for ALSS is NULL\n"
+ "e: Failed to sort EMMP tables\n"
+ "e: Failed to sort async PCS tables\n"
+ "e: Failed to sort sync PCS tables\n"
+ "e: GSC exceeding max brightness count: %u > %u\n"
+ "e: GSC exceeding max temperature count: %u > %u\n"
+ "e: GSC table is NULL\n"
+ "e: IRDC Block data and header size mismatch by %d too many bytes\n"
+ "e: Illegal channel code %c\n"
+ "e: LLMT APL Thresholds not in descending order\n"
+ "e: LLMT DBV Thresholds not in ascending order\n"
+ "e: LLMT Max DBV Threshold doesn't correspond to 0%% APL\n"
+ "e: PCS exceeding max brightness count: %u > %u\n"
+ "e: PCS exceeding max temperature count: %u > %u\n"
+ "e: PCS table is NULL\n"
+ "e: PCS tables are NULL\n"
+ "e: PDC missing at least 1 channel\n"
+ "e: PDC missing bin\n"
+ "e: PMLUT[%d, %d, %d, %d, %d, %d] is all zeros\n"
+ "e: PP LUT missing color channel\n"
+ "e: PRC table not well formed\n"
+ "e: Prox PD bin tables do no correlate\n"
+ "e: Prox PP bin tables do no correlate\n"
+ "e: Step values should be nonzero\n"
+ "e: The data size ( %d )is actually lesser than remaining bytes ( %d )\n"
+ "e: Too many index values for LUT tables\n"
+ "e: UPCL set DPCL data failed\n"
+ "e: Undefined EEPROM version 0x%x, expected 0x%x\n"
+ "e: Unexpected BLAH block version 0x%x\n"
+ "e: Unexpected BLTS block version 0x%x\n"
+ "e: Unexpected DPCL block version 0x%x\n"
+ "e: Unexpected RXTK block version 0x%x\n"
+ "e: Vector exceeding max i count: %u > %u\n"
+ "e: Vector exceeding max j count: %u > %u\n"
+ "e: actual number of Prox LUTs differ from specified\n"
+ "e: bin mix factor must be between 0 and 1\n"
+ "e: bin tables do not correlate.\n"
+ "e: block %s not well formed size %d remaining %d\n"
+ "e: channel not specified\n"
+ "e: data size %d mismatch header %d\n"
+ "e: duplicate PRC table found in input\n"
+ "e: duplicate tables\n"
+ "e: expected 3 color channels\n"
+ "e: failed to process block %s\n"
+ "e: failed to set ELVS LUT temperature %d\n"
+ "e: failed to set ELVS table config\n"
+ "e: failed to set LLMT table config\n"
+ "e: failed to set LUS LUT [%d %d %d]\n"
+ "e: failed to set LUS table config\n"
+ "e: failed to set PDC LUT [%d %d %d %d] \n"
+ "e: failed to set PDC table config\n"
+ "e: failed to set PRC LUT [t%d s%d b%d p%d]\n"
+ "e: failed to set PRC table config\n"
+ "e: failed to set PTUC TLS LUT brightness %d\n"
+ "e: failed to set PTUC table config\n"
+ "e: failed to set Prox PD LUT [t %d]\n"
+ "e: failed to set Prox PP LUT [t %d b %d p %d]\n"
+ "e: failed to set prox table config\n"
+ "e: frame repeat LUT incomplete, only %d/%d provided\n"
+ "e: illegal frame count %d\n"
+ "e: incoming data not well formed\n"
+ "e: inconsistent DC index\n"
+ "e: inconsistent PM index\n"
+ "e: inconsistent nframes value\n"
+ "e: input data not well-formed\n"
+ "e: invalid acss_config version %u\n"
+ "e: invalid block length for block %s\n"
+ "e: invalid header\n"
+ "e: lerped DCLUT[%d, %d, %d, %d, %d] is all zeros"
+ "e: lerped DCLUT[%d, %d, %d, %d] is all zeros"
+ "e: lerped PMLUT[%d, %d, %d, %d, %d] is all zeros"
+ "e: lerped PMLUT[%d, %d, %d, %d] is all zeros"
+ "e: lut size too big\n"
+ "e: lut sizes should be the same\n"
+ "e: missing LUS LUTs\n"
+ "e: missing PDC LUTs\n"
+ "e: missing PRC LUTs\n"
+ "e: missing PTUC LUTs\n"
+ "e: missing prox PD table bin %d\n"
+ "e: missing prox PP table bin %d\n"
+ "e: no data\n"
+ "e: no valid set block callback\n"
+ "e: not enough durations provided for LUS LUTs\n"
+ "e: processed ALSS EMMP dimensions (temp %u, bright %u)mismatch specified values (temp %u, bright %u)\n"
+ "e: provided min or max durations (%d, %d) invalid\n"
+ "e: prox LUTs should come after config parameters\n"
+ "e: ramp down configurations should be nonzero\n"
+ "e: reported PDC tap points (temp/DBV/RR/HGOD status) mismatch actual counts\n"
+ "e: set BCAL data failed\n"
+ "e: set BLAH data failed\n"
+ "e: set BLTS data failed\n"
+ "e: set CA data failed\n"
+ "e: set DBMA data failed\n"
+ "e: set DPCl data failed\n"
+ "e: set HGOD data failed\n"
+ "e: set HSPC data failed\n"
+ "e: set IRDC data failed\n"
+ "e: set PSFA data failed\n"
+ "e: set PSFM data failed\n"
+ "e: set QETC data failed\n"
+ "e: set QETC data failed. Too many brightness levels. \n"
+ "e: set RXTK data failed\n"
+ "e: set TLSC data failed\n"
+ "e: set TLSC data failed. Too many frequency levels. \n"
+ "e: set USPC data failed\n"
+ "e: set user_cal_aft_gain failed\n"
+ "e: unexpected LLMT block size %d\n"
+ "e: unexpected LLMT block version %d\n"
+ "e: unexpected PBDD block size 0x%x != 0x%x\n"
+ "e: unexpected PBDD version %d\n"
+ "e: unexpected PBDS block size 0x%x != 0x%x\n"
+ "e: unexpected PBDS version %d\n"
+ "e: unexpected PBDp block size %d\n"
+ "e: unexpected PBDp block version %d\n"
+ "e: unexpected PDC table version %d\n"
+ "e: unexpected PRCW block size %d\n"
+ "e: unexpected block size %d\n"
+ "e: unexpected block version %d\n"
+ "e: unexpected number of backlight sections %d\n"
+ "e: unexpected number of bins %d\n"
+ "e: unexpected value for polarity %d\n"
+ "e: unexpected version %d for PDCc block\n"
+ "e: unexpected version %d for PDCp block\n"
+ "e: unknown backlight section %d\n"
+ "e: unknown block name %s\n"
+ "e: unknown header block name %s\n"
+ "e: unspecified PD LUT temperature value %d C\n"
+ "e: unspecified PP LUT brightness %d\n"
+ "e: unspecified PP LUT scan plan 0x%x\n"
+ "e: unspecified PP LUT temperature %d C\n"
+ "e: unsupported number of color channels\n"
+ "e: useless PDC table\n"
+ "hard_power_state %d fTimingsUpdatePowerState %d fControllerPowerState %d fSoftPowerState %d  newCtrlrState %d \n"
+ "i:  UPCL set DPCL data succeeded\n"
+ "i: PDC bin interpolation, bin = 0x%x\n"
+ "i: PDC mix bin %g and bin %g with %g --> %g\n"
+ "i: PDC params version %d\n"
+ "i: Processing BLAH format version %d data version %d\n"
+ "i: Processing BLTS format version %d data version %d\n"
+ "i: Processing RXTK format version %d data version %d\n"
+ "i: Prox PD LUT bin interpolation, bin = 0x%x\n"
+ "i: Prox PP LUT bin interpolation, bin = 0x%x\n"
+ "i: Set ALSS EM config success\n"
+ "i: all done\n"
+ "i: processing prox data version %d\n"
+ "i: set BCAL data succeeded\n"
+ "i: set BLAH data succeeded\n"
+ "i: set BLTS data succeeded\n"
+ "i: set CA data succeeded\n"
+ "i: set DBMA data succeeded\n"
+ "i: set DPCl data succeeded\n"
+ "i: set ELVS table config succeeded\n"
+ "i: set EVLS LUTs succeeded\n"
+ "i: set HGOD data succeeded\n"
+ "i: set HSPC data succeeded\n"
+ "i: set IRDC data succeeded\n"
+ "i: set LLMT table config succeeded\n"
+ "i: set LUS LUTs succeeded\n"
+ "i: set LUS table config succeeded\n"
+ "i: set PDC LUTs succeeded\n"
+ "i: set PDC table config succeeded\n"
+ "i: set PRC LUTs succeeded\n"
+ "i: set PRC table config succeeded\n"
+ "i: set PSFA data succeeded\n"
+ "i: set PSFM data succeeded\n"
+ "i: set PTUC TLS LUTs succeeded\n"
+ "i: set PTUC table config succeeded\n"
+ "i: set Prox LUTs succeeded\n"
+ "i: set QETC data succeeded\n"
+ "i: set RXTK data succeeded"
+ "i: set TLSC data succeeded\n"
+ "i: set USPC data succeeded\n"
+ "i: set prox table config succeeded\n"
+ "i: set user_cal_aft_gain succeeded\n"
+ "iomfb_RuntimeProperty_IRDCFrameMaxResetCount"
+ "iomfb_RuntimeProperty_IRDCFrameMinResetCount"
+ "iomfb_RuntimeProperty_IRDCFrameReset"
+ "iomfb_RuntimeProperty_forceSecureAnimationUpdate"
+ "iomfb_RuntimeProperty_indicatorBrightnessNits"
+ "iomfb_RuntimeProperty_secureContentFactor"
+ "iomfb_RuntimeProperty_secureIndicatorFactor"
+ "iomfb_RuntimeProperty_usePodBoostAtRTPLCFDLUT"
+ "refresh-rate"
+ "usePodBoostAtRTPLCFDLUT"
+ "virtual bool IOMobileFramebuffer::getDebugInfoBufferJob(uint32_t *, uint32_t *)"
- "%s: Async Swap request landing on unsupported platform. Force panic\n"
- "average-refresh-rate"
- "parser_error: ACSS EMMP exceeding max brightness count: %u > %u\n"
- "parser_error: ACSS EMMP exceeding max temperature count: %u > %u\n"
- "parser_error: ACSS: set_block_cb failed\n"
- "parser_error: ALSS EMMP exceeding max brightness count: %u > %u\n"
- "parser_error: ALSS EMMP exceeding max temperature count: %u > %u\n"
- "parser_error: ALSS: set_block_cb_failed\n"
- "parser_error: Bad size/version for HGOD\n"
- "parser_error: Bad size/version for aftg\n"
- "parser_error: Could not find PRC tables [%d:%d:%d] [%d:%d:%d]\n"
- "parser_error: Could not find PRC tables [%d:%d:%d] for bins [%d:%d]\n"
- "parser_error: Counted vectors [%d][%d] mismatch expected [%d][%d]\n"
- "parser_error: DC or PM LUT size too big\n"
- "parser_error: DCLUT[%d, %d, %d, %d, %d, %d] is all zeros\n"
- "parser_error: DPCl: Data size insufficient for the taps \n"
- "parser_error: DPCl: More brightness taps( %d ) then expected (%d) \n"
- "parser_error: DPCl: More temperature taps( %d ) then expected (%d) \n"
- "parser_error: Duplicate PDC table (bin=%d temp=%d bright=%d sf=%d param=%d chan=%X) found in input.\n"
- "parser_error: Duplicate PTUC table vers=%d (bright=%d, temp=%d) found in input.\n"
- "parser_error: Duplicate elvs table temperature=%d found in input.\n"
- "parser_error: EMMK exceeding max brightness count: %u > %u\n"
- "parser_error: EMMK exceeding max temperature count: %u > %u\n"
- "parser_error: EMMP table for ACSS is NULL\n"
- "parser_error: EMMP table for ALSS is NULL\n"
- "parser_error: Failed to sort EMMP tables\n"
- "parser_error: Failed to sort async PCS tables\n"
- "parser_error: Failed to sort sync PCS tables\n"
- "parser_error: GSC exceeding max brightness count: %u > %u\n"
- "parser_error: GSC exceeding max temperature count: %u > %u\n"
- "parser_error: GSC table is NULL\n"
- "parser_error: IRDC Block data and header size mismatch by %d too many bytes\n"
- "parser_error: Illegal channel code %c\n"
- "parser_error: LLMT APL Thresholds not in descending order\n"
- "parser_error: LLMT DBV Thresholds not in ascending order\n"
- "parser_error: LLMT Max DBV Threshold doesn't correspond to 0%% APL\n"
- "parser_error: PCS exceeding max brightness count: %u > %u\n"
- "parser_error: PCS exceeding max temperature count: %u > %u\n"
- "parser_error: PCS table is NULL\n"
- "parser_error: PCS tables are NULL\n"
- "parser_error: PDC missing at least 1 channel\n"
- "parser_error: PDC missing bin\n"
- "parser_error: PMLUT[%d, %d, %d, %d, %d, %d] is all zeros\n"
- "parser_error: PP LUT missing color channel\n"
- "parser_error: PRC table not well formed\n"
- "parser_error: Prox PD bin tables do no correlate\n"
- "parser_error: Prox PP bin tables do no correlate\n"
- "parser_error: Step values should be nonzero\n"
- "parser_error: The data size ( %d )is actually lesser than remaining bytes ( %d )\n"
- "parser_error: Too many index values for LUT tables\n"
- "parser_error: UPCL set DPCL data failed\n"
- "parser_error: Undefined EEPROM version 0x%x, expected 0x%x\n"
- "parser_error: Unexpected BLAH block version 0x%x\n"
- "parser_error: Unexpected BLTS block version 0x%x\n"
- "parser_error: Unexpected DPCL block version 0x%x\n"
- "parser_error: Unexpected RXTK block version 0x%x\n"
- "parser_error: Vector exceeding max i count: %u > %u\n"
- "parser_error: Vector exceeding max j count: %u > %u\n"
- "parser_error: actual number of Prox LUTs differ from specified\n"
- "parser_error: bin mix factor must be between 0 and 1\n"
- "parser_error: bin tables do not correlate.\n"
- "parser_error: block %s not well formed size %d remaining %d\n"
- "parser_error: channel not specified\n"
- "parser_error: data size %d mismatch header %d\n"
- "parser_error: duplicate PRC table found in input\n"
- "parser_error: duplicate tables\n"
- "parser_error: expected 3 color channels\n"
- "parser_error: failed to process block %s\n"
- "parser_error: failed to set ELVS LUT temperatue %d\n"
- "parser_error: failed to set ELVS table config\n"
- "parser_error: failed to set LLMT table config\n"
- "parser_error: failed to set LUS LUT [%d %d %d]\n"
- "parser_error: failed to set LUS table config\n"
- "parser_error: failed to set PDC LUT [%d %d %d %d] \n"
- "parser_error: failed to set PDC table config\n"
- "parser_error: failed to set PRC LUT [t%d s%d b%d p%d]\n"
- "parser_error: failed to set PRC table config\n"
- "parser_error: failed to set PTUC TLS LUT brightness %d\n"
- "parser_error: failed to set PTUC table config\n"
- "parser_error: failed to set Prox PD LUT [t %d]\n"
- "parser_error: failed to set Prox PP LUT [t %d b %d p %d]\n"
- "parser_error: failed to set prox table config\n"
- "parser_error: frame repeat LUT incomplete, only %d/%d provided\n"
- "parser_error: illegal frame count %d\n"
- "parser_error: incoming data not well formed\n"
- "parser_error: inconsistent DC index\n"
- "parser_error: inconsistent PM index\n"
- "parser_error: inconsistent nframes value\n"
- "parser_error: input data not well-formed\n"
- "parser_error: invalid acss_config version %u\n"
- "parser_error: invalid block length for block %s\n"
- "parser_error: invalid header\n"
- "parser_error: lerped DCLUT[%d, %d, %d, %d, %d] is all zeros"
- "parser_error: lerped DCLUT[%d, %d, %d, %d] is all zeros"
- "parser_error: lerped PMLUT[%d, %d, %d, %d, %d] is all zeros"
- "parser_error: lerped PMLUT[%d, %d, %d, %d] is all zeros"
- "parser_error: lut size too big\n"
- "parser_error: lut sizes should be the same\n"
- "parser_error: missing LUS LUTs\n"
- "parser_error: missing PDC LUTs\n"
- "parser_error: missing PRC LUTs\n"
- "parser_error: missing PTUC LUTs\n"
- "parser_error: missing prox PD table bin %d\n"
- "parser_error: missing prox PP table bin %d\n"
- "parser_error: no data\n"
- "parser_error: no valid set block callback\n"
- "parser_error: not enough durations provided for LUS LUTs\n"
- "parser_error: processed ALSS EMMP dimensions (temp %u, bright %u)mismatch specified values (temp %u, bright %u)\n"
- "parser_error: provided min or max durations (%d, %d) invalid\n"
- "parser_error: prox LUTs should come after config parameters\n"
- "parser_error: ramp down configurations should be nonzero\n"
- "parser_error: reported PDC tap points (temp/DBV/RR/HGOD status) mismatch actual counts\n"
- "parser_error: set BCAL data failed\n"
- "parser_error: set BLAH data failed\n"
- "parser_error: set BLTS data failed\n"
- "parser_error: set CA data failed\n"
- "parser_error: set DBMA data failed\n"
- "parser_error: set DPCl data failed\n"
- "parser_error: set HGOD data failed\n"
- "parser_error: set HSPC data failed\n"
- "parser_error: set IRDC data failed\n"
- "parser_error: set PSFA data failed\n"
- "parser_error: set PSFM data failed\n"
- "parser_error: set QETC data failed\n"
- "parser_error: set QETC data failed. Too many brightness levels. \n"
- "parser_error: set RXTK data failed\n"
- "parser_error: set TLSC data failed\n"
- "parser_error: set TLSC data failed. Too many frequency levels. \n"
- "parser_error: set USPC data failed\n"
- "parser_error: set user_cal_aft_gain failed\n"
- "parser_error: unexpected LLMT block size %d\n"
- "parser_error: unexpected LLMT block version %d\n"
- "parser_error: unexpected PBDD block size 0x%x != 0x%x\n"
- "parser_error: unexpected PBDD version %d\n"
- "parser_error: unexpected PBDS block size 0x%x != 0x%x\n"
- "parser_error: unexpected PBDS version %d\n"
- "parser_error: unexpected PBDp block size %d\n"
- "parser_error: unexpected PBDp block version %d\n"
- "parser_error: unexpected PDC table version %d\n"
- "parser_error: unexpected PRCW block size %d\n"
- "parser_error: unexpected block size %d\n"
- "parser_error: unexpected block version %d\n"
- "parser_error: unexpected number of backlight sections %d\n"
- "parser_error: unexpected number of bins %d\n"
- "parser_error: unexpected value for polarity %d\n"
- "parser_error: unexpected version %d for PDCc block\n"
- "parser_error: unexpected version %d for PDCp block\n"
- "parser_error: unknown backlight section %d\n"
- "parser_error: unknown block name %s\n"
- "parser_error: unknown header block name %s\n"
- "parser_error: unspecified PD LUT temperature value %d C\n"
- "parser_error: unspecified PP LUT brightness %d\n"
- "parser_error: unspecified PP LUT scan plan 0x%x\n"
- "parser_error: unspecified PP LUT temperature %d C\n"
- "parser_error: unsupported number of color channels\n"
- "parser_error: useless PDC table\n"
- "parser_info:  UPCL set DPCL data succeeded\n"
- "parser_info: PDC bin interpolation, bin = 0x%x\n"
- "parser_info: PDC mix bin %g and bin %g with %g --> %g\n"
- "parser_info: PDC params version %d\n"
- "parser_info: Processing BLAH format version %d data version %d\n"
- "parser_info: Processing BLTS format version %d data version %d\n"
- "parser_info: Processing RXTK format version %d data version %d\n"
- "parser_info: Prox PD LUT bin interpolation, bin = 0x%x\n"
- "parser_info: Prox PP LUT bin interpolation, bin = 0x%x\n"
- "parser_info: Set ALSS EM config success\n"
- "parser_info: all done\n"
- "parser_info: processing prox data version %d\n"
- "parser_info: set BCAL data succeeded\n"
- "parser_info: set BLAH data succeeded\n"
- "parser_info: set BLTS data succeeded\n"
- "parser_info: set CA data succeeded\n"
- "parser_info: set DBMA data succeeded\n"
- "parser_info: set DPCl data succeeded\n"
- "parser_info: set ELVS table config succeeded\n"
- "parser_info: set EVLS LUTs succeeded\n"
- "parser_info: set HGOD data succeeded\n"
- "parser_info: set HSPC data succeeded\n"
- "parser_info: set IRDC data succeeded\n"
- "parser_info: set LLMT table config succeeded\n"
- "parser_info: set LUS LUTs succeeded\n"
- "parser_info: set LUS table config succeeded\n"
- "parser_info: set PDC LUTs succeeded\n"
- "parser_info: set PDC table config succeeded\n"
- "parser_info: set PRC LUTs succeeded\n"
- "parser_info: set PRC table config succeeded\n"
- "parser_info: set PSFA data succeeded\n"
- "parser_info: set PSFM data succeeded\n"
- "parser_info: set PTUC TLS LUTs succeeded\n"
- "parser_info: set PTUC table config succeeded\n"
- "parser_info: set Prox LUTs succeeded\n"
- "parser_info: set QETC data succeeded\n"
- "parser_info: set RXTK data succeeded"
- "parser_info: set TLSC data succeeded\n"
- "parser_info: set USPC data succeeded\n"
- "parser_info: set prox table config succeeded\n"
- "parser_info: set user_cal_aft_gain succeeded\n"
- "virtual bool IOMobileFramebuffer::writeDebugInfoJob(uintptr_t)"

```

#### t8130pmp.im4p

>  `t8130pmp.im4p`

```diff

 
-  __TEXT.__text: 0x34b94
+  __TEXT.__text: 0x34b40
   __TEXT.__const: 0x1e90
   __TEXT.__cstring: 0x15c4
   __TEXT.__chain_starts: 0x0
   __TEXT.__constructor: 0x0
   __TEXT._rtk_mtab: 0x5d0
-  __DATA.__const: 0x1e68
-  __DATA.__data: 0x6cf8
+  __DATA.__const: 0x1e90
+  __DATA.__data: 0x6c78
   __DATA._rtk_page_tables: 0x8000
   __DATA._rtk_boot: 0x1000
   __DATA._rtk_init_stack: 0x1800

   __DATA._rtk_power: 0x358
   __DATA._rtk_heap: 0x0
   __DATA.__mod_init_func: 0x10
-  __DATA.__zerofill: 0x4d0e8
+  __DATA.__zerofill: 0x4d0f0
   Functions: 0
   Symbols:   0
   CStrings:  396

```

#### txm.iphoneos.release.im4p

>  `txm.iphoneos.release.im4p`

```diff

-89.100.16.0.0
-  __TEXT.__cstring: 0x46a7
+89.120.2.0.0
+  __TEXT.__cstring: 0x46a2
   __TEXT.__const: 0x33d0
   __TEXT.__binname: 0x40
   __TEXT.__chain_starts: 0x44
   __DATA_CONST.__auth_ptr: 0x40
   __DATA_CONST.__const: 0x6c58
-  __TEXT_EXEC.__text: 0x3a91c
+  __TEXT_EXEC.__text: 0x3aafc
   __TEXT_BOOT_EXEC.__text: 0x4058
   __TEXT_BOOT_EXEC.__bootcode: 0x20
   __DATA.__data: 0x238
   __DATA.__common: 0xa60
-  __DATA.__bss: 0x480
-  Functions: 821
+  __DATA.__bss: 0x488
+  Functions: 824
   Symbols:   1
   CStrings:  559
 
CStrings:
+ "257.120.3"
+ "@(#)VERSION:Darwin Image4 Validator Version 6.3.0: Sat Apr 13 03:55:12 PDT 2024; root:AppleImage4_txm-257.120.3~18/libimage4_TXM/RELEASE_ARM64E"
+ "Darwin Image4 Validator Version 6.3.0: Sat Apr 13 03:55:12 PDT 2024; root:AppleImage4_txm-257.120.3~18/libimage4_TXM/RELEASE_ARM64E"
+ "txm.iphoneos.release.TrustedExecutionMonitor_Guarded-89.120.2"
- "257.100.26"
- "@(#)VERSION:Darwin Image4 Validator Version 6.3.0: Fri Mar  8 22:58:36 PST 2024; root:AppleImage4_txm-257.100.26~94/libimage4_TXM/RELEASE_ARM64E"
- "Darwin Image4 Validator Version 6.3.0: Fri Mar  8 22:58:36 PST 2024; root:AppleImage4_txm-257.100.26~94/libimage4_TXM/RELEASE_ARM64E"
- "txm.iphoneos.release.TrustedExecutionMonitor_Guarded-89.100.16"

```


</details>

### Launchd

```diff

 		</dict>
 		<key>exclaves-boot</key>
 		<dict>
+			<key>PerformInRestore</key>
+			<true/>
 			<key>Block</key>
 			<string>exclaves-boot</string>
 		</dict>

```
## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 17.4.1 *(21E237)* | 618.1.15.10.15 |
| 17.5 *(21F79)* | 618.2.12.10.9 |

### Dylibs

#### 🆕 NEW (6)

- `/System/Library/PrivateFrameworks/AudioDSPManager.framework/AudioDSPManager`
- `/System/Library/PrivateFrameworks/Cosmo.framework/Cosmo`
- `/System/Library/PrivateFrameworks/EXDisplayPipe.framework/EXDisplayPipe`
- `/System/Library/PrivateFrameworks/Scandium.framework/Scandium`
- `/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets.framework/SecureVoiceTriggerAssets`
- `/System/Library/PrivateFrameworks/SemanticPerception.framework/SemanticPerception`

#### ❌ Removed (2)

- `/System/Library/PrivateFrameworks/BWCrucible.framework/BWCrucible`
- `/System/Library/PrivateFrameworks/PridePoster.framework/PridePoster`

#### ⬆️ Updated (1783)

<details>
  <summary><i>View Updated</i></summary>

- [/System/Library/AccessibilityBundles/ASMessagesProvider.axbundle/ASMessagesProvider](DYLIBS/ASMessagesProvider.md)
- [/System/Library/AccessibilityBundles/AVKit.axbundle/AVKit](DYLIBS/AVKit.md)
- [/System/Library/AccessibilityBundles/AccessibilitySettingsLoader.bundle/AccessibilitySettingsLoader](DYLIBS/AccessibilitySettingsLoader.md)
- [/System/Library/AccessibilityBundles/AnnotationKit.axbundle/AnnotationKit](DYLIBS/AnnotationKit.md)
- [/System/Library/AccessibilityBundles/AppInstallExtension.axbundle/AppInstallExtension](DYLIBS/AppInstallExtension.md)
- [/System/Library/AccessibilityBundles/AppStore.axbundle/AppStore](DYLIBS/AppStore.md)
- [/System/Library/AccessibilityBundles/Arcade.axbundle/Arcade](DYLIBS/Arcade.md)
- [/System/Library/AccessibilityBundles/BackBoard.axbundle/BackBoard](DYLIBS/BackBoard.md)
- [/System/Library/AccessibilityBundles/BridgeStoreExtension.axbundle/BridgeStoreExtension](DYLIBS/BridgeStoreExtension.md)
- [/System/Library/AccessibilityBundles/CameraUI.axbundle/CameraUI](DYLIBS/CameraUI.md)
- [/System/Library/AccessibilityBundles/CarPlay.axbundle/CarPlay](DYLIBS/CarPlay.md)
- [/System/Library/AccessibilityBundles/ChatKitFramework.axbundle/ChatKitFramework](DYLIBS/ChatKitFramework.md)
- [/System/Library/AccessibilityBundles/ConversationKit.axbundle/ConversationKit](DYLIBS/ConversationKit.md)
- [/System/Library/AccessibilityBundles/CoverSheet.axbundle/CoverSheet](DYLIBS/CoverSheet.md)
- [/System/Library/AccessibilityBundles/FlightUtilities.axbundle/FlightUtilities](DYLIBS/FlightUtilities.md)
- [/System/Library/AccessibilityBundles/FrontBoard.axbundle/FrontBoard](DYLIBS/FrontBoard.md)
- [/System/Library/AccessibilityBundles/GameCenterUIFramework.axbundle/GameCenterUIFramework](DYLIBS/GameCenterUIFramework.md)
- [/System/Library/AccessibilityBundles/HealthExperienceUI.axbundle/HealthExperienceUI](DYLIBS/HealthExperienceUI.md)
- [/System/Library/AccessibilityBundles/HealthRecordsUI.axbundle/HealthRecordsUI](DYLIBS/HealthRecordsUI.md)
- [/System/Library/AccessibilityBundles/HealthUI.axbundle/HealthUI](DYLIBS/HealthUI.md)
- [/System/Library/AccessibilityBundles/LinkPresentation.axbundle/LinkPresentation](DYLIBS/LinkPresentation.md)
- [/System/Library/AccessibilityBundles/MapKitFramework.axbundle/MapKitFramework](DYLIBS/MapKitFramework.md)
- [/System/Library/AccessibilityBundles/MobileMail.axbundle/MobileMail](DYLIBS/MobileMail.md)
- [/System/Library/AccessibilityBundles/MobilePhone.axbundle/MobilePhone](DYLIBS/MobilePhone.md)
- [/System/Library/AccessibilityBundles/MobileSafari.axbundle/MobileSafari](DYLIBS/MobileSafari.md)
- [/System/Library/AccessibilityBundles/MobileSafariUI.axbundle/MobileSafariUI](DYLIBS/MobileSafariUI.md)
- [/System/Library/AccessibilityBundles/MusicApplication.axbundle/MusicApplication](DYLIBS/MusicApplication.md)
- [/System/Library/AccessibilityBundles/MusicUI.axbundle/MusicUI](DYLIBS/MusicUI.md)
- [/System/Library/AccessibilityBundles/PaperKit.axbundle/PaperKit](DYLIBS/PaperKit.md)
- [/System/Library/AccessibilityBundles/Pegasus.axbundle/Pegasus](DYLIBS/Pegasus.md)
- [/System/Library/AccessibilityBundles/PencilKit.axbundle/PencilKit](DYLIBS/PencilKit.md)
- [/System/Library/AccessibilityBundles/PhotosUIFramework.axbundle/PhotosUIFramework](DYLIBS/PhotosUIFramework.md)
- [/System/Library/AccessibilityBundles/PosterBoardFramework.axbundle/PosterBoardFramework](DYLIBS/PosterBoardFramework.md)
- [/System/Library/AccessibilityBundles/PreBoard.axbundle/PreBoard](DYLIBS/PreBoard.md)
- [/System/Library/AccessibilityBundles/PreferencesFramework.axbundle/PreferencesFramework](DYLIBS/PreferencesFramework.md)
- [/System/Library/AccessibilityBundles/ProductPageExtension.axbundle/ProductPageExtension](DYLIBS/ProductPageExtension.md)
- [/System/Library/AccessibilityBundles/QuickLook.axbundle/QuickLook](DYLIBS/QuickLook.md)
- [/System/Library/AccessibilityBundles/SafariServices.axbundle/SafariServices](DYLIBS/SafariServices.md)
- [/System/Library/AccessibilityBundles/SearchUI.axbundle/SearchUI](DYLIBS/SearchUI.md)
- [/System/Library/AccessibilityBundles/SharingUI.axbundle/SharingUI](DYLIBS/SharingUI.md)
- [/System/Library/AccessibilityBundles/SiriKitRuntime.axbundle/SiriKitRuntime](DYLIBS/SiriKitRuntime.md)
- [/System/Library/AccessibilityBundles/SpringBoard.axbundle/SpringBoard](DYLIBS/SpringBoard.md)
- [/System/Library/AccessibilityBundles/SpringBoardFoundation.axbundle/SpringBoardFoundation](DYLIBS/SpringBoardFoundation.md)
- [/System/Library/AccessibilityBundles/SpringBoardHome.axbundle/SpringBoardHome](DYLIBS/SpringBoardHome.md)
- [/System/Library/AccessibilityBundles/StoreDynamicUIPlugin.axbundle/StoreDynamicUIPlugin](DYLIBS/StoreDynamicUIPlugin.md)
- [/System/Library/AccessibilityBundles/SystemApertureUI.axbundle/SystemApertureUI](DYLIBS/SystemApertureUI.md)
- [/System/Library/AccessibilityBundles/SystemStatusUI.axbundle/SystemStatusUI](DYLIBS/SystemStatusUI.md)
- [/System/Library/AccessibilityBundles/Translate.axbundle/Translate](DYLIBS/Translate.md)
- [/System/Library/AccessibilityBundles/UIKit.axbundle/UIKit](DYLIBS/UIKit.md)
- [/System/Library/AccessibilityBundles/VectorKit.axbundle/VectorKit](DYLIBS/VectorKit.md)
- [/System/Library/AccessibilityBundles/VideosUIFramework.axbundle/VideosUIFramework](DYLIBS/VideosUIFramework.md)
- [/System/Library/AccessibilityBundles/Weather.axbundle/Weather](DYLIBS/Weather.md)
- [/System/Library/AccessibilityBundles/WebCore.axbundle/WebCore](DYLIBS/WebCore.md)
- [/System/Library/AccessibilityBundles/WebKit.axbundle/WebKit](DYLIBS/WebKit.md)
- [/System/Library/AccessibilityBundles/iAdFramework.axbundle/iAdFramework](DYLIBS/iAdFramework.md)
- [/System/Library/Accounts/Authentication/AppleIDAuthentication.bundle/AppleIDAuthentication](DYLIBS/AppleIDAuthentication.md)
- [/System/Library/Accounts/Notification/AADataclassEnableNotificationPlugin.bundle/AADataclassEnableNotificationPlugin](DYLIBS/AADataclassEnableNotificationPlugin.md)
- [/System/Library/Accounts/Notification/AKAccountNotificationPlugin.bundle/AKAccountNotificationPlugin](DYLIBS/AKAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/KeychainSyncAccountNotification.bundle/KeychainSyncAccountNotification](DYLIBS/KeychainSyncAccountNotification.md)
- [/System/Library/Accounts/Notification/SearchPartyAccountNotificationPlugin.bundle/SearchPartyAccountNotificationPlugin](DYLIBS/SearchPartyAccountNotificationPlugin.md)
- [/System/Library/ControlCenter/Bundles/AirPlayMirroringModule.bundle/AirPlayMirroringModule](DYLIBS/AirPlayMirroringModule.md)
- [/System/Library/ControlCenter/Bundles/ConnectivityModule.bundle/ConnectivityModule](DYLIBS/ConnectivityModule.md)
- [/System/Library/ControlCenter/Bundles/SpokenNotificationsModule.bundle/SpokenNotificationsModule](DYLIBS/SpokenNotificationsModule.md)
- [/System/Library/CoreAccessories/PlugIns/Features/BLEPairing-iOS.feature/BLEPairing-iOS](DYLIBS/BLEPairing-iOS.md)
- [/System/Library/CoreAccessories/PlugIns/Features/Communications-iOS.feature/Communications-iOS](DYLIBS/Communications-iOS.md)
- [/System/Library/CoreAccessories/PlugIns/Platform/IOKit.platform/IOKit](DYLIBS/IOKit.md)
- [/System/Library/CoreAccessories/PlugIns/Transports/IOAccessoryManager.transport/IOAccessoryManager](DYLIBS/IOAccessoryManager.md)
- [/System/Library/CoreAccessories/PlugIns/Transports/NFC.transport/NFC](DYLIBS/NFC.md)
- [/System/Library/CoreAccessories/PlugIns/Transports/USBHost.transport/USBHost](DYLIBS/USBHost.md)
- [/System/Library/CoreServices/RawCamera.bundle/RawCamera](DYLIBS/RawCamera.md)
- [/System/Library/Extensions/AGXMetalG16P_A0.bundle/AGXMetalG16P_A0](DYLIBS/AGXMetalG16P_A0.md)
- [/System/Library/Extensions/AGXMetalG16P_B0.bundle/AGXMetalG16P_B0](DYLIBS/AGXMetalG16P_B0.md)
- [/System/Library/Extensions/AppleMultitouchSPI.kext/PlugIns/MultitouchHID.plugin/MultitouchHID](DYLIBS/MultitouchHID.md)
- [/System/Library/Extensions/AppleSPU.kext/PlugIns/AppleSPULib.plugin/AppleSPULib](DYLIBS/AppleSPULib.md)
- [/System/Library/Extensions/AppleSPU.kext/PlugIns/GNSSPassthroughLib.plugin/GNSSPassthroughLib](DYLIBS/GNSSPassthroughLib.md)
- [/System/Library/Fitness/Plugins/SeymourAwardsPlugin.bundle/SeymourAwardsPlugin](DYLIBS/SeymourAwardsPlugin.md)
- [/System/Library/Frameworks/AVFAudio.framework/AVFAudio](DYLIBS/AVFAudio.md)
- [/System/Library/Frameworks/AVFoundation.framework/AVFoundation](DYLIBS/AVFoundation.md)
- [/System/Library/Frameworks/AVKit.framework/AVKit](DYLIBS/AVKit.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vImage.framework/Libraries/libCGInterfaces.dylib](DYLIBS/libCGInterfaces.dylib.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vImage.framework/vImage](DYLIBS/vImage.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libBLAS.dylib](DYLIBS/libBLAS.dylib.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libBNNS.dylib](DYLIBS/libBNNS.dylib.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libLAPACK.dylib](DYLIBS/libLAPACK.dylib.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libSparseBLAS.dylib](DYLIBS/libSparseBLAS.dylib.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libvDSP.dylib](DYLIBS/libvDSP.dylib.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libvMisc.dylib](DYLIBS/libvMisc.dylib.md)
- [/System/Library/Frameworks/Accessibility.framework/Accessibility](DYLIBS/Accessibility.md)
- [/System/Library/Frameworks/Accounts.framework/Accounts](DYLIBS/Accounts.md)
- [/System/Library/Frameworks/ActivityKit.framework/ActivityKit](DYLIBS/ActivityKit.md)
- [/System/Library/Frameworks/AdAttributionKit.framework/AdAttributionKit](DYLIBS/AdAttributionKit.md)
- [/System/Library/Frameworks/AppIntents.framework/AppIntents](DYLIBS/AppIntents.md)
- [/System/Library/Frameworks/AppTrackingTransparency.framework/AppTrackingTransparency](DYLIBS/AppTrackingTransparency.md)
- [/System/Library/Frameworks/AssetsLibrary.framework/AssetsLibrary](DYLIBS/AssetsLibrary.md)
- [/System/Library/Frameworks/Assignables.framework/Assignables](DYLIBS/Assignables.md)
- [/System/Library/Frameworks/AudioToolbox.framework/AudioCodecs](DYLIBS/AudioCodecs.md)
- [/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox](DYLIBS/AudioToolbox.md)
- [/System/Library/Frameworks/AudioToolbox.framework/libAudioDSP.dylib](DYLIBS/libAudioDSP.dylib.md)
- [/System/Library/Frameworks/AudioToolbox.framework/libEmbeddedSystemAUs.dylib](DYLIBS/libEmbeddedSystemAUs.dylib.md)
- [/System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices](DYLIBS/AuthenticationServices.md)
- [/System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/AutomaticAssessmentConfiguration](DYLIBS/AutomaticAssessmentConfiguration.md)
- [/System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/Frameworks/AACClient.framework/AACClient](DYLIBS/AACClient.md)
- [/System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/Frameworks/AACDependencies.framework/AACDependencies](DYLIBS/AACDependencies.md)
- [/System/Library/Frameworks/BackgroundTasks.framework/BackgroundTasks](DYLIBS/BackgroundTasks.md)
- [/System/Library/Frameworks/BrowserEngineKit.framework/BrowserEngineKit](DYLIBS/BrowserEngineKit.md)
- [/System/Library/Frameworks/CFNetwork.framework/CFNetwork](DYLIBS/CFNetwork.md)
- [/System/Library/Frameworks/CallKit.framework/CallKit](DYLIBS/CallKit.md)
- [/System/Library/Frameworks/CarPlay.framework/CarPlay](DYLIBS/CarPlay.md)
- [/System/Library/Frameworks/Charts.framework/Charts](DYLIBS/Charts.md)
- [/System/Library/Frameworks/ClassKit.framework/ClassKit](DYLIBS/ClassKit.md)
- [/System/Library/Frameworks/ClockKit.framework/ClockKit](DYLIBS/ClockKit.md)
- [/System/Library/Frameworks/CloudKit.framework/CloudKit](DYLIBS/CloudKit.md)
- [/System/Library/Frameworks/ColorSync.framework/ColorSync](DYLIBS/ColorSync.md)
- [/System/Library/Frameworks/Combine.framework/Combine](DYLIBS/Combine.md)
- [/System/Library/Frameworks/Contacts.framework/Contacts](DYLIBS/Contacts.md)
- [/System/Library/Frameworks/ContactsUI.framework/ContactsUI](DYLIBS/ContactsUI.md)
- [/System/Library/Frameworks/CoreAudio.framework/CoreAudio](DYLIBS/CoreAudio.md)
- [/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth](DYLIBS/CoreBluetooth.md)
- [/System/Library/Frameworks/CoreData.framework/CoreData](DYLIBS/CoreData.md)
- [/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation](DYLIBS/CoreFoundation.md)
- [/System/Library/Frameworks/CoreGraphics.framework/CoreGraphics](DYLIBS/CoreGraphics.md)
- [/System/Library/Frameworks/CoreHaptics.framework/CoreHaptics](DYLIBS/CoreHaptics.md)
- [/System/Library/Frameworks/CoreImage.framework/CoreImage](DYLIBS/CoreImage.md)
- [/System/Library/Frameworks/CoreLocation.framework/CoreLocation](DYLIBS/CoreLocation.md)
- [/System/Library/Frameworks/CoreMIDI.framework/CoreMIDI](DYLIBS/CoreMIDI.md)
- [/System/Library/Frameworks/CoreML.framework/CoreML](DYLIBS/CoreML.md)
- [/System/Library/Frameworks/CoreMedia.framework/CoreMedia](DYLIBS/CoreMedia.md)
- [/System/Library/Frameworks/CoreMediaIO.framework/CoreMediaIO](DYLIBS/CoreMediaIO.md)
- [/System/Library/Frameworks/CoreMotion.framework/CoreMotion](DYLIBS/CoreMotion.md)
- [/System/Library/Frameworks/CoreServices.framework/CoreServices](DYLIBS/CoreServices.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight](DYLIBS/CoreSpotlight.md)
- [/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony](DYLIBS/CoreTelephony.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/CTParser.framework/CTParser](DYLIBS/CTParser.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCellularDecoders.dylib](DYLIBS/libCellularDecoders.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterAWDMetrics.dylib](DYLIBS/libCommCenterAWDMetrics.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterBase.dylib](DYLIBS/libCommCenterBase.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterCommandDrivers.dylib](DYLIBS/libCommCenterCommandDrivers.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterKCommandDrivers.dylib](DYLIBS/libCommCenterKCommandDrivers.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterMCommandDrivers.dylib](DYLIBS/libCommCenterMCommandDrivers.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libSystemDetermination.dylib](DYLIBS/libSystemDetermination.dylib.md)
- [/System/Library/Frameworks/CoreText.framework/CoreText](DYLIBS/CoreText.md)
- [/System/Library/Frameworks/CoreVideo.framework/CoreVideo](DYLIBS/CoreVideo.md)
- [/System/Library/Frameworks/CreateMLComponents.framework/CreateMLComponents](DYLIBS/CreateMLComponents.md)
- [/System/Library/Frameworks/CryptoKit.framework/CryptoKit](DYLIBS/CryptoKit.md)
- [/System/Library/Frameworks/CryptoTokenKit.framework/CryptoTokenKit](DYLIBS/CryptoTokenKit.md)
- [/System/Library/Frameworks/DeviceActivity.framework/DeviceActivity](DYLIBS/DeviceActivity.md)
- [/System/Library/Frameworks/DeviceCheck.framework/DeviceCheck](DYLIBS/DeviceCheck.md)
- [/System/Library/Frameworks/DriverKit.framework/DriverKit](DYLIBS/DriverKit.md)
- [/System/Library/Frameworks/EventKit.framework/EventKit](DYLIBS/EventKit.md)
- [/System/Library/Frameworks/EventKitUI.framework/EventKitUI](DYLIBS/EventKitUI.md)
- [/System/Library/Frameworks/ExposureNotification.framework/ExposureNotification](DYLIBS/ExposureNotification.md)
- [/System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation](DYLIBS/ExtensionFoundation.md)
- [/System/Library/Frameworks/ExternalAccessory.framework/ExternalAccessory](DYLIBS/ExternalAccessory.md)
- [/System/Library/Frameworks/FileProvider.framework/FileProvider](DYLIBS/FileProvider.md)
- [/System/Library/Frameworks/FinanceKit.framework/FinanceKit](DYLIBS/FinanceKit.md)
- [/System/Library/Frameworks/FinanceKitUI.framework/FinanceKitUI](DYLIBS/FinanceKitUI.md)
- [/System/Library/Frameworks/Foundation.framework/Foundation](DYLIBS/Foundation.md)
- [/System/Library/Frameworks/GLKit.framework/GLKit](DYLIBS/GLKit.md)
- [/System/Library/Frameworks/GameController.framework/GameController](DYLIBS/GameController.md)
- [/System/Library/Frameworks/GroupActivities.framework/GroupActivities](DYLIBS/GroupActivities.md)
- [/System/Library/Frameworks/HealthKit.framework/HealthKit](DYLIBS/HealthKit.md)
- [/System/Library/Frameworks/HomeKit.framework/HomeKit](DYLIBS/HomeKit.md)
- [/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit](DYLIBS/IOKit.md)
- [/System/Library/Frameworks/IOSurface.framework/IOSurface](DYLIBS/IOSurface.md)
- [/System/Library/Frameworks/IdentityLookup.framework/IdentityLookup](DYLIBS/IdentityLookup.md)
- [/System/Library/Frameworks/ImageCaptureCore.framework/ImageCaptureCore](DYLIBS/ImageCaptureCore.md)
- [/System/Library/Frameworks/ImageIO.framework/ImageIO](DYLIBS/ImageIO.md)
- [/System/Library/Frameworks/Intents.framework/Intents](DYLIBS/Intents.md)
- [/System/Library/Frameworks/IntentsUI.framework/IntentsUI](DYLIBS/IntentsUI.md)
- [/System/Library/Frameworks/JavaScriptCore.framework/JavaScriptCore](DYLIBS/JavaScriptCore.md)
- [/System/Library/Frameworks/LinkPresentation.framework/LinkPresentation](DYLIBS/LinkPresentation.md)
- [/System/Library/Frameworks/LiveCommunicationKit.framework/LiveCommunicationKit](DYLIBS/LiveCommunicationKit.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication](DYLIBS/LocalAuthentication.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/DaemonUtils.framework/DaemonUtils](DYLIBS/DaemonUtils.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismBase.framework/MechanismBase](DYLIBS/MechanismBase.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/ModuleBase.framework/ModuleBase](DYLIBS/ModuleBase.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/SharedUtils.framework/SharedUtils](DYLIBS/SharedUtils.md)
- [/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI](DYLIBS/LocalAuthenticationEmbeddedUI.md)
- [/System/Library/Frameworks/MLCompute.framework/MLCompute](DYLIBS/MLCompute.md)
- [/System/Library/Frameworks/ManagedAppDistribution.framework/ManagedAppDistribution](DYLIBS/ManagedAppDistribution.md)
- [/System/Library/Frameworks/ManagedSettings.framework/ManagedSettings](DYLIBS/ManagedSettings.md)
- [/System/Library/Frameworks/MapKit.framework/MapKit](DYLIBS/MapKit.md)
- [/System/Library/Frameworks/MarketplaceKit.framework/MarketplaceKit](DYLIBS/MarketplaceKit.md)
- [/System/Library/Frameworks/Matter.framework/Matter](DYLIBS/Matter.md)
- [/System/Library/Frameworks/MatterSupport.framework/MatterSupport](DYLIBS/MatterSupport.md)
- [/System/Library/Frameworks/MediaAccessibility.framework/MediaAccessibility](DYLIBS/MediaAccessibility.md)
- [/System/Library/Frameworks/MediaPlayer.framework/MediaPlayer](DYLIBS/MediaPlayer.md)
- [/System/Library/Frameworks/MediaSetup.framework/MediaSetup](DYLIBS/MediaSetup.md)
- [/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox](DYLIBS/MediaToolbox.md)
- [/System/Library/Frameworks/MessageUI.framework/MessageUI](DYLIBS/MessageUI.md)
- [/System/Library/Frameworks/Messages.framework/Messages](DYLIBS/Messages.md)
- [/System/Library/Frameworks/Metal.framework/Metal](DYLIBS/Metal.md)
- [/System/Library/Frameworks/MetalKit.framework/MetalKit](DYLIBS/MetalKit.md)
- [/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSBenchmarkLoop.framework/MPSBenchmarkLoop](DYLIBS/MPSBenchmarkLoop.md)
- [/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSCore.framework/MPSCore](DYLIBS/MPSCore.md)
- [/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSImage.framework/MPSImage](DYLIBS/MPSImage.md)
- [/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSMatrix.framework/MPSMatrix](DYLIBS/MPSMatrix.md)
- [/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNDArray.framework/MPSNDArray](DYLIBS/MPSNDArray.md)
- [/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork](DYLIBS/MPSNeuralNetwork.md)
- [/System/Library/Frameworks/MetricKit.framework/MetricKit](DYLIBS/MetricKit.md)
- [/System/Library/Frameworks/ModelIO.framework/ModelIO](DYLIBS/ModelIO.md)
- [/System/Library/Frameworks/MusicKit.framework/MusicKit](DYLIBS/MusicKit.md)
- [/System/Library/Frameworks/NaturalLanguage.framework/NaturalLanguage](DYLIBS/NaturalLanguage.md)
- [/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction](DYLIBS/NearbyInteraction.md)
- [/System/Library/Frameworks/Network.framework/Network](DYLIBS/Network.md)
- [/System/Library/Frameworks/NetworkExtension.framework/NetworkExtension](DYLIBS/NetworkExtension.md)
- [/System/Library/Frameworks/NotificationCenter.framework/NotificationCenter](DYLIBS/NotificationCenter.md)
- [/System/Library/Frameworks/OSLog.framework/OSLog](DYLIBS/OSLog.md)
- [/System/Library/Frameworks/PHASE.framework/PHASE](DYLIBS/PHASE.md)
- [/System/Library/Frameworks/PencilKit.framework/PencilKit](DYLIBS/PencilKit.md)
- [/System/Library/Frameworks/Photos.framework/Photos](DYLIBS/Photos.md)
- [/System/Library/Frameworks/PhotosUI.framework/PhotosUI](DYLIBS/PhotosUI.md)
- [/System/Library/Frameworks/ProximityReader.framework/ProximityReader](DYLIBS/ProximityReader.md)
- [/System/Library/Frameworks/PushKit.framework/PushKit](DYLIBS/PushKit.md)
- [/System/Library/Frameworks/QuartzCore.framework/QuartzCore](DYLIBS/QuartzCore.md)
- [/System/Library/Frameworks/QuickLook.framework/QuickLook](DYLIBS/QuickLook.md)
- [/System/Library/Frameworks/QuickLookThumbnailing.framework/QuickLookThumbnailing](DYLIBS/QuickLookThumbnailing.md)
- [/System/Library/Frameworks/RealityFoundation.framework/RealityFoundation](DYLIBS/RealityFoundation.md)
- [/System/Library/Frameworks/RealityKit.framework/RealityKit](DYLIBS/RealityKit.md)
- [/System/Library/Frameworks/ReplayKit.framework/ReplayKit](DYLIBS/ReplayKit.md)
- [/System/Library/Frameworks/SafariServices.framework/SafariServices](DYLIBS/SafariServices.md)
- [/System/Library/Frameworks/SafetyKit.framework/SafetyKit](DYLIBS/SafetyKit.md)
- [/System/Library/Frameworks/SceneKit.framework/SceneKit](DYLIBS/SceneKit.md)
- [/System/Library/Frameworks/Security.framework/Security](DYLIBS/Security.md)
- [/System/Library/Frameworks/SensitiveContentAnalysis.framework/SensitiveContentAnalysis](DYLIBS/SensitiveContentAnalysis.md)
- [/System/Library/Frameworks/SensorKit.framework/SensorKit](DYLIBS/SensorKit.md)
- [/System/Library/Frameworks/SharedWithYou.framework/SharedWithYou](DYLIBS/SharedWithYou.md)
- [/System/Library/Frameworks/SharedWithYouCore.framework/SharedWithYouCore](DYLIBS/SharedWithYouCore.md)
- [/System/Library/Frameworks/ShazamKit.framework/ShazamKit](DYLIBS/ShazamKit.md)
- [/System/Library/Frameworks/SoundAnalysis.framework/SoundAnalysis](DYLIBS/SoundAnalysis.md)
- [/System/Library/Frameworks/Speech.framework/Speech](DYLIBS/Speech.md)
- [/System/Library/Frameworks/SpriteKit.framework/SpriteKit](DYLIBS/SpriteKit.md)
- [/System/Library/Frameworks/StoreKit.framework/StoreKit](DYLIBS/StoreKit.md)
- [/System/Library/Frameworks/SwiftData.framework/SwiftData](DYLIBS/SwiftData.md)
- [/System/Library/Frameworks/SwiftUI.framework/SwiftUI](DYLIBS/SwiftUI.md)
- [/System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration](DYLIBS/SystemConfiguration.md)
- [/System/Library/Frameworks/ThreadNetwork.framework/ThreadNetwork](DYLIBS/ThreadNetwork.md)
- [/System/Library/Frameworks/TipKit.framework/TipKit](DYLIBS/TipKit.md)
- [/System/Library/Frameworks/TipsNext.framework/TipsNext](DYLIBS/TipsNext.md)
- [/System/Library/Frameworks/Translation.framework/Translation](DYLIBS/Translation.md)
- [/System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers](DYLIBS/UniformTypeIdentifiers.md)
- [/System/Library/Frameworks/UserNotifications.framework/UserNotifications](DYLIBS/UserNotifications.md)
- [/System/Library/Frameworks/UserNotificationsUI.framework/UserNotificationsUI](DYLIBS/UserNotificationsUI.md)
- [/System/Library/Frameworks/VideoSubscriberAccount.framework/VideoSubscriberAccount](DYLIBS/VideoSubscriberAccount.md)
- [/System/Library/Frameworks/VideoToolbox.framework/VideoToolbox](DYLIBS/VideoToolbox.md)
- [/System/Library/Frameworks/Vision.framework/Vision](DYLIBS/Vision.md)
- [/System/Library/Frameworks/WatchConnectivity.framework/WatchConnectivity](DYLIBS/WatchConnectivity.md)
- [/System/Library/Frameworks/WeatherKit.framework/WeatherKit](DYLIBS/WeatherKit.md)
- [/System/Library/Frameworks/WebKit.framework/WebKit](DYLIBS/WebKit.md)
- [/System/Library/Frameworks/WidgetKit.framework/WidgetKit](DYLIBS/WidgetKit.md)
- [/System/Library/Frameworks/_AppIntents_SwiftUI.framework/_AppIntents_SwiftUI](DYLIBS/_AppIntents_SwiftUI.md)
- [/System/Library/Frameworks/_AppIntents_UIKit.framework/_AppIntents_UIKit](DYLIBS/_AppIntents_UIKit.md)
- [/System/Library/Frameworks/_GroupActivities_UIKit.framework/_GroupActivities_UIKit](DYLIBS/_GroupActivities_UIKit.md)
- [/System/Library/Frameworks/_MapKit_SwiftUI.framework/_MapKit_SwiftUI](DYLIBS/_MapKit_SwiftUI.md)
- [/System/Library/Frameworks/_MarketplaceKit_UIKit.framework/_MarketplaceKit_UIKit](DYLIBS/_MarketplaceKit_UIKit.md)
- [/System/Library/Frameworks/_MusicKit_SwiftUI.framework/_MusicKit_SwiftUI](DYLIBS/_MusicKit_SwiftUI.md)
- [/System/Library/Frameworks/_PhotosUI_SwiftUI.framework/_PhotosUI_SwiftUI](DYLIBS/_PhotosUI_SwiftUI.md)
- [/System/Library/Frameworks/_StoreKit_SwiftUI.framework/_StoreKit_SwiftUI](DYLIBS/_StoreKit_SwiftUI.md)
- [/System/Library/HIDPlugins/IOHIDEventProcessorFilter.plugin/IOHIDEventProcessorFilter](DYLIBS/IOHIDEventProcessorFilter.md)
- [/System/Library/HIDPlugins/IOHIDKeyboardFilter.plugin/IOHIDKeyboardFilter](DYLIBS/IOHIDKeyboardFilter.md)
- [/System/Library/HIDPlugins/IOHIDT8027USBSessionFilter.plugin/IOHIDT8027USBSessionFilter](DYLIBS/IOHIDT8027USBSessionFilter.md)
- [/System/Library/HIDPlugins/PearlEventFilter.plugin/PearlEventFilter](DYLIBS/PearlEventFilter.md)
- [/System/Library/Health/FeedItemPlugins/AppRecommendations.healthplugin/AppRecommendations](DYLIBS/AppRecommendations.md)
- [/System/Library/Health/FeedItemPlugins/Categories.healthplugin/Categories](DYLIBS/Categories.md)
- [/System/Library/Health/FeedItemPlugins/HealthArticles.healthplugin/HealthArticles](DYLIBS/HealthArticles.md)
- [/System/Library/Health/FeedItemPlugins/HealthRecords.healthplugin/HealthRecords](DYLIBS/HealthRecords.md)
- [/System/Library/Health/FeedItemPlugins/HearingAppPlugin.healthplugin/HearingAppPlugin](DYLIBS/HearingAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/Heart.healthplugin/Heart](DYLIBS/Heart.md)
- [/System/Library/Health/FeedItemPlugins/HighlightAlerts.healthplugin/HighlightAlerts](DYLIBS/HighlightAlerts.md)
- [/System/Library/Health/FeedItemPlugins/Highlights.healthplugin/Highlights](DYLIBS/Highlights.md)
- [/System/Library/Health/FeedItemPlugins/MedicationsHealthAppPlugin.healthplugin/MedicationsHealthAppPlugin](DYLIBS/MedicationsHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/MenstrualCyclesAppPlugin.healthplugin/MenstrualCyclesAppPlugin](DYLIBS/MenstrualCyclesAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/MentalHealthAppPlugin.healthplugin/MentalHealthAppPlugin](DYLIBS/MentalHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/MobilityAppPlugin.healthplugin/MobilityAppPlugin](DYLIBS/MobilityAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/Profiles.healthplugin/Profiles](DYLIBS/Profiles.md)
- [/System/Library/Health/FeedItemPlugins/ResearchApp.healthplugin/ResearchApp](DYLIBS/ResearchApp.md)
- [/System/Library/Health/FeedItemPlugins/RespiratoryHealthAppPlugin.healthplugin/RespiratoryHealthAppPlugin](DYLIBS/RespiratoryHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/Safety.healthplugin/Safety](DYLIBS/Safety.md)
- [/System/Library/Health/FeedItemPlugins/SleepHealthAppPlugin.healthplugin/SleepHealthAppPlugin](DYLIBS/SleepHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/Summaries.healthplugin/Summaries](DYLIBS/Summaries.md)
- [/System/Library/Health/FeedItemPlugins/VisionHealthAppPlugin.healthplugin/VisionHealthAppPlugin](DYLIBS/VisionHealthAppPlugin.md)
- [/System/Library/Health/Plugins/ActivitySharingPlugin.bundle/ActivitySharingPlugin](DYLIBS/ActivitySharingPlugin.md)
- [/System/Library/MediaCapture/H16ISP.mediacapture](DYLIBS/H16ISP.mediacapture.md)
- [/System/Library/Messages/PlugIns/FaceTime.imservice/FaceTime](DYLIBS/FaceTime.md)
- [/System/Library/Messages/PlugIns/SMS.imservice/SMS](DYLIBS/SMS.md)
- [/System/Library/Messages/PlugIns/iMessage.imservice/iMessage](DYLIBS/iMessage.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKAegirFaceBundleCompanion.bundle/NTKAegirFaceBundleCompanion](DYLIBS/NTKAegirFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKEsterbrookFaceBundleCompanion.bundle/NTKEsterbrookFaceBundleCompanion](DYLIBS/NTKEsterbrookFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKFoghornFaceBundleCompanion.bundle/NTKFoghornFaceBundleCompanion](DYLIBS/NTKFoghornFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKGalleonFaceBundleCompanion.bundle/NTKGalleonFaceBundleCompanion](DYLIBS/NTKGalleonFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKRhizomeFaceBundleCompanion.bundle/NTKRhizomeFaceBundleCompanion](DYLIBS/NTKRhizomeFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKSnowglobeFaceBundleCompanion.bundle/NTKSnowglobeFaceBundleCompanion](DYLIBS/NTKSnowglobeFaceBundleCompanion.md)
- [/System/Library/PreferenceBundles/BluetoothSettings.bundle/BluetoothSettings](DYLIBS/BluetoothSettings.md)
- [/System/Library/PreferenceBundles/KeyboardSettings.bundle/KeyboardSettings](DYLIBS/KeyboardSettings.md)
- [/System/Library/PrivateFrameworks/AAAFoundation.framework/AAAFoundation](DYLIBS/AAAFoundation.md)
- [/System/Library/PrivateFrameworks/AAAFoundationSwift.framework/AAAFoundationSwift](DYLIBS/AAAFoundationSwift.md)
- [/System/Library/PrivateFrameworks/AACCore.framework/AACCore](DYLIBS/AACCore.md)
- [/System/Library/PrivateFrameworks/ABMHelper.framework/ABMHelper](DYLIBS/ABMHelper.md)
- [/System/Library/PrivateFrameworks/AGXCompilerCore.framework/AGXCompilerCore](DYLIBS/AGXCompilerCore.md)
- [/System/Library/PrivateFrameworks/AGXGPURawCounter.framework/AGXGPURawCounter](DYLIBS/AGXGPURawCounter.md)
- [/System/Library/PrivateFrameworks/AIMLExperimentationAnalytics.framework/AIMLExperimentationAnalytics](DYLIBS/AIMLExperimentationAnalytics.md)
- [/System/Library/PrivateFrameworks/AIMLInstrumentationStreams.framework/AIMLInstrumentationStreams](DYLIBS/AIMLInstrumentationStreams.md)
- [/System/Library/PrivateFrameworks/ANECompiler.framework/ANECompiler](DYLIBS/ANECompiler.md)
- [/System/Library/PrivateFrameworks/ANECompiler.framework/libORTools.dylib](DYLIBS/libORTools.dylib.md)
- [/System/Library/PrivateFrameworks/ANEServices.framework/ANEServices](DYLIBS/ANEServices.md)
- [/System/Library/PrivateFrameworks/ANSTKit.framework/ANSTKit](DYLIBS/ANSTKit.md)
- [/System/Library/PrivateFrameworks/APConfigurationSystem.framework/APConfigurationSystem](DYLIBS/APConfigurationSystem.md)
- [/System/Library/PrivateFrameworks/APFS.framework/APFS](DYLIBS/APFS.md)
- [/System/Library/PrivateFrameworks/APFoundation.framework/APFoundation](DYLIBS/APFoundation.md)
- [/System/Library/PrivateFrameworks/APTransport.framework/APTransport](DYLIBS/APTransport.md)
- [/System/Library/PrivateFrameworks/ARKitCore.framework/ARKitCore](DYLIBS/ARKitCore.md)
- [/System/Library/PrivateFrameworks/ARKitFoundation.framework/ARKitFoundation](DYLIBS/ARKitFoundation.md)
- [/System/Library/PrivateFrameworks/ARKitUI.framework/ARKitUI](DYLIBS/ARKitUI.md)
- [/System/Library/PrivateFrameworks/ASOctaneSupport.framework/ASOctaneSupport](DYLIBS/ASOctaneSupport.md)
- [/System/Library/PrivateFrameworks/ASRBridge.framework/ASRBridge](DYLIBS/ASRBridge.md)
- [/System/Library/PrivateFrameworks/ATFoundation.framework/ATFoundation](DYLIBS/ATFoundation.md)
- [/System/Library/PrivateFrameworks/AUDeveloperSettings.framework/AUDeveloperSettings](DYLIBS/AUDeveloperSettings.md)
- [/System/Library/PrivateFrameworks/AUSettings.framework/AUSettings](DYLIBS/AUSettings.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/AVConference](DYLIBS/AVConference.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/GKSPerformance.framework/GKSPerformance](DYLIBS/GKSPerformance.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ICE.framework/ICE](DYLIBS/ICE.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ViceroyTrace.framework/ViceroyTrace](DYLIBS/ViceroyTrace.md)
- [/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture](DYLIBS/AVFCapture.md)
- [/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore](DYLIBS/AVFCore.md)
- [/System/Library/PrivateFrameworks/AXAssetLoader.framework/AXAssetLoader](DYLIBS/AXAssetLoader.md)
- [/System/Library/PrivateFrameworks/AXCoreUtilities.framework/AXCoreUtilities](DYLIBS/AXCoreUtilities.md)
- [/System/Library/PrivateFrameworks/AXMediaUtilities.framework/AXMediaUtilities](DYLIBS/AXMediaUtilities.md)
- [/System/Library/PrivateFrameworks/AXRuntime.framework/AXRuntime](DYLIBS/AXRuntime.md)
- [/System/Library/PrivateFrameworks/AXSoundDetection.framework/AXSoundDetection](DYLIBS/AXSoundDetection.md)
- [/System/Library/PrivateFrameworks/AXSoundDetectionUI.framework/AXSoundDetectionUI](DYLIBS/AXSoundDetectionUI.md)
- [/System/Library/PrivateFrameworks/AXSpringBoardServerInstance.framework/AXSpringBoardServerInstance](DYLIBS/AXSpringBoardServerInstance.md)
- [/System/Library/PrivateFrameworks/AXWatchRemoteScreenServices.framework/AXWatchRemoteScreenServices](DYLIBS/AXWatchRemoteScreenServices.md)
- [/System/Library/PrivateFrameworks/AccessibilityAudit.framework/AccessibilityAudit](DYLIBS/AccessibilityAudit.md)
- [/System/Library/PrivateFrameworks/AccessibilitySharedSupport.framework/AccessibilitySharedSupport](DYLIBS/AccessibilitySharedSupport.md)
- [/System/Library/PrivateFrameworks/AccessibilityUI.framework/AccessibilityUI](DYLIBS/AccessibilityUI.md)
- [/System/Library/PrivateFrameworks/AccessibilityUIService.framework/AccessibilityUIService](DYLIBS/AccessibilityUIService.md)
- [/System/Library/PrivateFrameworks/AccessibilityUIUtilities.framework/AccessibilityUIUtilities](DYLIBS/AccessibilityUIUtilities.md)
- [/System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities](DYLIBS/AccessibilityUtilities.md)
- [/System/Library/PrivateFrameworks/AccessoryBLEPairing.framework/AccessoryBLEPairing](DYLIBS/AccessoryBLEPairing.md)
- [/System/Library/PrivateFrameworks/AccessoryComponentAuth.framework/AccessoryComponentAuth](DYLIBS/AccessoryComponentAuth.md)
- [/System/Library/PrivateFrameworks/AccessoryNavigation.framework/AccessoryNavigation](DYLIBS/AccessoryNavigation.md)
- [/System/Library/PrivateFrameworks/AccessoryiAP2Shim.framework/AccessoryiAP2Shim](DYLIBS/AccessoryiAP2Shim.md)
- [/System/Library/PrivateFrameworks/AccountNotification.framework/AccountNotification](DYLIBS/AccountNotification.md)
- [/System/Library/PrivateFrameworks/AccountsDaemon.framework/AccountsDaemon](DYLIBS/AccountsDaemon.md)
- [/System/Library/PrivateFrameworks/AccountsUI.framework/AccountsUI](DYLIBS/AccountsUI.md)
- [/System/Library/PrivateFrameworks/ActionButtonSelector.framework/ActionButtonSelector](DYLIBS/ActionButtonSelector.md)
- [/System/Library/PrivateFrameworks/ActionKit.framework/ActionKit](DYLIBS/ActionKit.md)
- [/System/Library/PrivateFrameworks/ActionPredictionHeuristics.framework/ActionPredictionHeuristics](DYLIBS/ActionPredictionHeuristics.md)
- [/System/Library/PrivateFrameworks/ActionPredictionHeuristicsInternal.framework/ActionPredictionHeuristicsInternal](DYLIBS/ActionPredictionHeuristicsInternal.md)
- [/System/Library/PrivateFrameworks/ActivityAchievements.framework/ActivityAchievements](DYLIBS/ActivityAchievements.md)
- [/System/Library/PrivateFrameworks/ActivityAchievementsDaemon.framework/ActivityAchievementsDaemon](DYLIBS/ActivityAchievementsDaemon.md)
- [/System/Library/PrivateFrameworks/ActivityAchievementsUI.framework/ActivityAchievementsUI](DYLIBS/ActivityAchievementsUI.md)
- [/System/Library/PrivateFrameworks/ActivityAwardsServices.framework/ActivityAwardsServices](DYLIBS/ActivityAwardsServices.md)
- [/System/Library/PrivateFrameworks/ActivityRingsUI.framework/ActivityRingsUI](DYLIBS/ActivityRingsUI.md)
- [/System/Library/PrivateFrameworks/ActivitySharing.framework/ActivitySharing](DYLIBS/ActivitySharing.md)
- [/System/Library/PrivateFrameworks/ActivitySharingClient.framework/ActivitySharingClient](DYLIBS/ActivitySharingClient.md)
- [/System/Library/PrivateFrameworks/ActivitySharingDaemonCore.framework/ActivitySharingDaemonCore](DYLIBS/ActivitySharingDaemonCore.md)
- [/System/Library/PrivateFrameworks/ActivitySharingServices.framework/ActivitySharingServices](DYLIBS/ActivitySharingServices.md)
- [/System/Library/PrivateFrameworks/ActivitySharingUI.framework/ActivitySharingUI](DYLIBS/ActivitySharingUI.md)
- [/System/Library/PrivateFrameworks/ActivityUIServices.framework/ActivityUIServices](DYLIBS/ActivityUIServices.md)
- [/System/Library/PrivateFrameworks/AdCore.framework/AdCore](DYLIBS/AdCore.md)
- [/System/Library/PrivateFrameworks/AdID.framework/AdID](DYLIBS/AdID.md)
- [/System/Library/PrivateFrameworks/AdPlatforms.framework/AdPlatforms](DYLIBS/AdPlatforms.md)
- [/System/Library/PrivateFrameworks/AdPlatformsCommon.framework/AdPlatformsCommon](DYLIBS/AdPlatformsCommon.md)
- [/System/Library/PrivateFrameworks/AddressBookLegacy.framework/AddressBookLegacy](DYLIBS/AddressBookLegacy.md)
- [/System/Library/PrivateFrameworks/AirPlayReceiver.framework/AirPlayReceiver](DYLIBS/AirPlayReceiver.md)
- [/System/Library/PrivateFrameworks/AirPlayReceiverKit.framework/AirPlayReceiverKit](DYLIBS/AirPlayReceiverKit.md)
- [/System/Library/PrivateFrameworks/AirPlayRoutePrediction.framework/AirPlayRoutePrediction](DYLIBS/AirPlayRoutePrediction.md)
- [/System/Library/PrivateFrameworks/AirPlaySender.framework/AirPlaySender](DYLIBS/AirPlaySender.md)
- [/System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport](DYLIBS/AirPlaySupport.md)
- [/System/Library/PrivateFrameworks/AirTraffic.framework/AirTraffic](DYLIBS/AirTraffic.md)
- [/System/Library/PrivateFrameworks/AirTrafficDevice.framework/AirTrafficDevice](DYLIBS/AirTrafficDevice.md)
- [/System/Library/PrivateFrameworks/AlgosScoreFramework.framework/AlgosScoreFramework](DYLIBS/AlgosScoreFramework.md)
- [/System/Library/PrivateFrameworks/AnnotationKit.framework/AnnotationKit](DYLIBS/AnnotationKit.md)
- [/System/Library/PrivateFrameworks/AnnounceDaemon.framework/AnnounceDaemon](DYLIBS/AnnounceDaemon.md)
- [/System/Library/PrivateFrameworks/AppAnalytics.framework/AppAnalytics](DYLIBS/AppAnalytics.md)
- [/System/Library/PrivateFrameworks/AppAttestInternal.framework/AppAttestInternal](DYLIBS/AppAttestInternal.md)
- [/System/Library/PrivateFrameworks/AppC3D.framework/AppC3D](DYLIBS/AppC3D.md)
- [/System/Library/PrivateFrameworks/AppConduit.framework/AppConduit](DYLIBS/AppConduit.md)
- [/System/Library/PrivateFrameworks/AppDistribution.framework/AppDistribution](DYLIBS/AppDistribution.md)
- [/System/Library/PrivateFrameworks/AppNotificationsLoggingClient.framework/AppNotificationsLoggingClient](DYLIBS/AppNotificationsLoggingClient.md)
- [/System/Library/PrivateFrameworks/AppPredictionClient.framework/AppPredictionClient](DYLIBS/AppPredictionClient.md)
- [/System/Library/PrivateFrameworks/AppPredictionFoundation.framework/AppPredictionFoundation](DYLIBS/AppPredictionFoundation.md)
- [/System/Library/PrivateFrameworks/AppPredictionInternal.framework/AppPredictionInternal](DYLIBS/AppPredictionInternal.md)
- [/System/Library/PrivateFrameworks/AppPredictionUIFoundation.framework/AppPredictionUIFoundation](DYLIBS/AppPredictionUIFoundation.md)
- [/System/Library/PrivateFrameworks/AppSSO.framework/AppSSO](DYLIBS/AppSSO.md)
- [/System/Library/PrivateFrameworks/AppSSOCore.framework/AppSSOCore](DYLIBS/AppSSOCore.md)
- [/System/Library/PrivateFrameworks/AppSSOKerberos.framework/AppSSOKerberos](DYLIBS/AppSSOKerberos.md)
- [/System/Library/PrivateFrameworks/AppServerSupport.framework/AppServerSupport](DYLIBS/AppServerSupport.md)
- [/System/Library/PrivateFrameworks/AppState.framework/AppState](DYLIBS/AppState.md)
- [/System/Library/PrivateFrameworks/AppStoreComponents.framework/AppStoreComponents](DYLIBS/AppStoreComponents.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon](DYLIBS/AppStoreDaemon.md)
- [/System/Library/PrivateFrameworks/AppStoreEvalLighthouseUtils.framework/AppStoreEvalLighthouseUtils](DYLIBS/AppStoreEvalLighthouseUtils.md)
- [/System/Library/PrivateFrameworks/AppStoreKit.framework/AppStoreKit](DYLIBS/AppStoreKit.md)
- [/System/Library/PrivateFrameworks/AppStoreKitInternal.framework/AppStoreKitInternal](DYLIBS/AppStoreKitInternal.md)
- [/System/Library/PrivateFrameworks/AppStoreOverlays.framework/AppStoreOverlays](DYLIBS/AppStoreOverlays.md)
- [/System/Library/PrivateFrameworks/AppSupport.framework/AppSupport](DYLIBS/AppSupport.md)
- [/System/Library/PrivateFrameworks/AppSupportUI.framework/AppSupportUI](DYLIBS/AppSupportUI.md)
- [/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount](DYLIBS/AppleAccount.md)
- [/System/Library/PrivateFrameworks/AppleAccountUI.framework/AppleAccountUI](DYLIBS/AppleAccountUI.md)
- [/System/Library/PrivateFrameworks/AppleBasebandManager.framework/AppleBasebandManager](DYLIBS/AppleBasebandManager.md)
- [/System/Library/PrivateFrameworks/AppleCV3D.framework/AppleCV3D](DYLIBS/AppleCV3D.md)
- [/System/Library/PrivateFrameworks/AppleCV3DMOVKit.framework/AppleCV3DMOVKit](DYLIBS/AppleCV3DMOVKit.md)
- [/System/Library/PrivateFrameworks/AppleCVA.framework/AppleCVA](DYLIBS/AppleCVA.md)
- [/System/Library/PrivateFrameworks/AppleCVAPhoto.framework/AppleCVAPhoto](DYLIBS/AppleCVAPhoto.md)
- [/System/Library/PrivateFrameworks/AppleCVHWA.framework/AppleCVHWA](DYLIBS/AppleCVHWA.md)
- [/System/Library/PrivateFrameworks/AppleDepth.framework/AppleDepth](DYLIBS/AppleDepth.md)
- [/System/Library/PrivateFrameworks/AppleDepthCore.framework/AppleDepthCore](DYLIBS/AppleDepthCore.md)
- [/System/Library/PrivateFrameworks/AppleEmbeddedDisplayServices.framework/AppleEmbeddedDisplayServices](DYLIBS/AppleEmbeddedDisplayServices.md)
- [/System/Library/PrivateFrameworks/AppleFSCompression.framework/AppleFSCompression](DYLIBS/AppleFSCompression.md)
- [/System/Library/PrivateFrameworks/AppleHIDFeedback.framework/AppleHIDFeedback](DYLIBS/AppleHIDFeedback.md)
- [/System/Library/PrivateFrameworks/AppleIDSSOAuthentication.framework/AppleIDSSOAuthentication](DYLIBS/AppleIDSSOAuthentication.md)
- [/System/Library/PrivateFrameworks/AppleIDSetup.framework/AppleIDSetup](DYLIBS/AppleIDSetup.md)
- [/System/Library/PrivateFrameworks/AppleIDSetupUI.framework/AppleIDSetupUI](DYLIBS/AppleIDSetupUI.md)
- [/System/Library/PrivateFrameworks/AppleJPEG.framework/AppleJPEG](DYLIBS/AppleJPEG.md)
- [/System/Library/PrivateFrameworks/AppleJPEGXL.framework/AppleJPEGXL](DYLIBS/AppleJPEGXL.md)
- [/System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore](DYLIBS/AppleKeyStore.md)
- [/System/Library/PrivateFrameworks/AppleMediaDiscovery.framework/AppleMediaDiscovery](DYLIBS/AppleMediaDiscovery.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices](DYLIBS/AppleMediaServices.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/AppleMediaServicesUI](DYLIBS/AppleMediaServicesUI.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUIDynamic.framework/AppleMediaServicesUIDynamic](DYLIBS/AppleMediaServicesUIDynamic.md)
- [/System/Library/PrivateFrameworks/AppleMobileFileIntegrity.framework/AppleMobileFileIntegrity](DYLIBS/AppleMobileFileIntegrity.md)
- [/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine](DYLIBS/AppleNeuralEngine.md)
- [/System/Library/PrivateFrameworks/ApplePhotonDetectorServices.framework/ApplePhotonDetectorServices](DYLIBS/ApplePhotonDetectorServices.md)
- [/System/Library/PrivateFrameworks/ApplePushService.framework/ApplePushService](DYLIBS/ApplePushService.md)
- [/System/Library/PrivateFrameworks/AppleSauce.framework/AppleSauce](DYLIBS/AppleSauce.md)
- [/System/Library/PrivateFrameworks/AppleServiceToolkit.framework/AppleServiceToolkit](DYLIBS/AppleServiceToolkit.md)
- [/System/Library/PrivateFrameworks/AppleTracingSupportSymbolication.framework/AppleTracingSupportSymbolication](DYLIBS/AppleTracingSupportSymbolication.md)
- [/System/Library/PrivateFrameworks/ArgumentParserInternal.framework/ArgumentParserInternal](DYLIBS/ArgumentParserInternal.md)
- [/System/Library/PrivateFrameworks/AskPermission.framework/AskPermission](DYLIBS/AskPermission.md)
- [/System/Library/PrivateFrameworks/AskTo.framework/AskTo](DYLIBS/AskTo.md)
- [/System/Library/PrivateFrameworks/AskToCore.framework/AskToCore](DYLIBS/AskToCore.md)
- [/System/Library/PrivateFrameworks/AssertionServices.framework/AssertionServices](DYLIBS/AssertionServices.md)
- [/System/Library/PrivateFrameworks/AssetCacheServices.framework/AssetCacheServices](DYLIBS/AssetCacheServices.md)
- [/System/Library/PrivateFrameworks/AssetViewer.framework/AssetViewer](DYLIBS/AssetViewer.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices](DYLIBS/AssistantServices.md)
- [/System/Library/PrivateFrameworks/AssistantUI.framework/AssistantUI](DYLIBS/AssistantUI.md)
- [/System/Library/PrivateFrameworks/AtomicsInternal.framework/AtomicsInternal](DYLIBS/AtomicsInternal.md)
- [/System/Library/PrivateFrameworks/AttentionAwareness.framework/AttentionAwareness](DYLIBS/AttentionAwareness.md)
- [/System/Library/PrivateFrameworks/AttributeGraph.framework/AttributeGraph](DYLIBS/AttributeGraph.md)
- [/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices](DYLIBS/AudioAccessoryServices.md)
- [/System/Library/PrivateFrameworks/AudioAnalytics.framework/AudioAnalytics](DYLIBS/AudioAnalytics.md)
- [/System/Library/PrivateFrameworks/AudioAnalyticsBase.framework/AudioAnalyticsBase](DYLIBS/AudioAnalyticsBase.md)
- [/System/Library/PrivateFrameworks/AudioAnalyticsExternal.framework/AudioAnalyticsExternal](DYLIBS/AudioAnalyticsExternal.md)
- [/System/Library/PrivateFrameworks/AudioDataAnalysis.framework/AudioDataAnalysis](DYLIBS/AudioDataAnalysis.md)
- [/System/Library/PrivateFrameworks/AudioServerDriver.framework/AudioServerDriver](DYLIBS/AudioServerDriver.md)
- [/System/Library/PrivateFrameworks/AudioServerDriverTransports_Base.framework/AudioServerDriverTransports_Base](DYLIBS/AudioServerDriverTransports_Base.md)
- [/System/Library/PrivateFrameworks/AudioServerDriverTransports_IOA2.framework/AudioServerDriverTransports_IOA2](DYLIBS/AudioServerDriverTransports_IOA2.md)
- [/System/Library/PrivateFrameworks/AudioServerDriverTransports_IOP.framework/AudioServerDriverTransports_IOP](DYLIBS/AudioServerDriverTransports_IOP.md)
- [/System/Library/PrivateFrameworks/AudioSession.framework/AudioSession](DYLIBS/AudioSession.md)
- [/System/Library/PrivateFrameworks/AudioSession.framework/libSessionUtility.dylib](DYLIBS/libSessionUtility.dylib.md)
- [/System/Library/PrivateFrameworks/AudioSessionServer.framework/AudioSessionServer](DYLIBS/AudioSessionServer.md)
- [/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore](DYLIBS/AudioToolboxCore.md)
- [/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit](DYLIBS/AuthKit.md)
- [/System/Library/PrivateFrameworks/AuthKitUI.framework/AuthKitUI](DYLIBS/AuthKitUI.md)
- [/System/Library/PrivateFrameworks/AuthenticationServicesCore.framework/AuthenticationServicesCore](DYLIBS/AuthenticationServicesCore.md)
- [/System/Library/PrivateFrameworks/AutoBugCaptureCore.framework/AutoBugCaptureCore](DYLIBS/AutoBugCaptureCore.md)
- [/System/Library/PrivateFrameworks/AutoFillCore.framework/AutoFillCore](DYLIBS/AutoFillCore.md)
- [/System/Library/PrivateFrameworks/AutoFillUI.framework/AutoFillUI](DYLIBS/AutoFillUI.md)
- [/System/Library/PrivateFrameworks/AvailabilityKit.framework/AvailabilityKit](DYLIBS/AvailabilityKit.md)
- [/System/Library/PrivateFrameworks/AvatarKit.framework/AvatarKit](DYLIBS/AvatarKit.md)
- [/System/Library/PrivateFrameworks/AvatarUI.framework/AvatarUI](DYLIBS/AvatarUI.md)
- [/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation](DYLIBS/BackBoardHIDEventFoundation.md)
- [/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices](DYLIBS/BackBoardServices.md)
- [/System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks](DYLIBS/BackgroundSystemTasks.md)
- [/System/Library/PrivateFrameworks/BackgroundTaskAgent.framework/BackgroundTaskAgent](DYLIBS/BackgroundTaskAgent.md)
- [/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices](DYLIBS/BacklightServices.md)
- [/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost](DYLIBS/BacklightServicesHost.md)
- [/System/Library/PrivateFrameworks/BannerKit.framework/BannerKit](DYLIBS/BannerKit.md)
- [/System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard](DYLIBS/BaseBoard.md)
- [/System/Library/PrivateFrameworks/BatteryCenterUI.framework/BatteryCenterUI](DYLIBS/BatteryCenterUI.md)
- [/System/Library/PrivateFrameworks/BehaviorMiner.framework/BehaviorMiner](DYLIBS/BehaviorMiner.md)
- [/System/Library/PrivateFrameworks/BiomeDSL.framework/BiomeDSL](DYLIBS/BiomeDSL.md)
- [/System/Library/PrivateFrameworks/BiomeFoundation.framework/BiomeFoundation](DYLIBS/BiomeFoundation.md)
- [/System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary](DYLIBS/BiomeLibrary.md)
- [/System/Library/PrivateFrameworks/BiomePubSub.framework/BiomePubSub](DYLIBS/BiomePubSub.md)
- [/System/Library/PrivateFrameworks/BiomeStorage.framework/BiomeStorage](DYLIBS/BiomeStorage.md)
- [/System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams](DYLIBS/BiomeStreams.md)
- [/System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit](DYLIBS/BiometricKit.md)
- [/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI](DYLIBS/BiometricKitUI.md)
- [/System/Library/PrivateFrameworks/BiometricSupport.framework/BiometricSupport](DYLIBS/BiometricSupport.md)
- [/System/Library/PrivateFrameworks/BlastDoor.framework/BlastDoor](DYLIBS/BlastDoor.md)
- [/System/Library/PrivateFrameworks/BluetoothAudio.framework/BluetoothAudio](DYLIBS/BluetoothAudio.md)
- [/System/Library/PrivateFrameworks/BluetoothManager.framework/BluetoothManager](DYLIBS/BluetoothManager.md)
- [/System/Library/PrivateFrameworks/BluetoothServicesUI.framework/BluetoothServicesUI](DYLIBS/BluetoothServicesUI.md)
- [/System/Library/PrivateFrameworks/BoardServices.framework/BoardServices](DYLIBS/BoardServices.md)
- [/System/Library/PrivateFrameworks/BookCoverUtility.framework/BookCoverUtility](DYLIBS/BookCoverUtility.md)
- [/System/Library/PrivateFrameworks/BookDataStore.framework/BookDataStore](DYLIBS/BookDataStore.md)
- [/System/Library/PrivateFrameworks/BookFoundation.framework/BookFoundation](DYLIBS/BookFoundation.md)
- [/System/Library/PrivateFrameworks/BookLibrary.framework/BookLibrary](DYLIBS/BookLibrary.md)
- [/System/Library/PrivateFrameworks/BookLibraryCore.framework/BookLibraryCore](DYLIBS/BookLibraryCore.md)
- [/System/Library/PrivateFrameworks/BookUtility.framework/BookUtility](DYLIBS/BookUtility.md)
- [/System/Library/PrivateFrameworks/BrailleTranslation.framework/BrailleTranslation](DYLIBS/BrailleTranslation.md)
- [/System/Library/PrivateFrameworks/BridgePreferences.framework/BridgePreferences](DYLIBS/BridgePreferences.md)
- [/System/Library/PrivateFrameworks/BridgeReporting.framework/BridgeReporting](DYLIBS/BridgeReporting.md)
- [/System/Library/PrivateFrameworks/BrightnessControl.framework/BrightnessControl](DYLIBS/BrightnessControl.md)
- [/System/Library/PrivateFrameworks/BulletinBoard.framework/BulletinBoard](DYLIBS/BulletinBoard.md)
- [/System/Library/PrivateFrameworks/BusinessChatService.framework/BusinessChatService](DYLIBS/BusinessChatService.md)
- [/System/Library/PrivateFrameworks/C2.framework/C2](DYLIBS/C2.md)
- [/System/Library/PrivateFrameworks/CAFCombine.framework/CAFCombine](DYLIBS/CAFCombine.md)
- [/System/Library/PrivateFrameworks/CDDataAccess.framework/Frameworks/DADaemonSupport.framework/DADaemonSupport](DYLIBS/DADaemonSupport.md)
- [/System/Library/PrivateFrameworks/CDMFoundation.framework/CDMFoundation](DYLIBS/CDMFoundation.md)
- [/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture](DYLIBS/CMCapture.md)
- [/System/Library/PrivateFrameworks/CMCaptureCore.framework/CMCaptureCore](DYLIBS/CMCaptureCore.md)
- [/System/Library/PrivateFrameworks/CMContinuityCaptureCore.framework/CMContinuityCaptureCore](DYLIBS/CMContinuityCaptureCore.md)
- [/System/Library/PrivateFrameworks/CMImaging.framework/CMImaging](DYLIBS/CMImaging.md)
- [/System/Library/PrivateFrameworks/CMPhoto.framework/CMPhoto](DYLIBS/CMPhoto.md)
- [/System/Library/PrivateFrameworks/CPAnalytics.framework/CPAnalytics](DYLIBS/CPAnalytics.md)
- [/System/Library/PrivateFrameworks/CPMS.framework/CPMS](DYLIBS/CPMS.md)
- [/System/Library/PrivateFrameworks/CSExattrCrypto.framework/CSExattrCrypto](DYLIBS/CSExattrCrypto.md)
- [/System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete](DYLIBS/CacheDelete.md)
- [/System/Library/PrivateFrameworks/Calculate.framework/Calculate](DYLIBS/Calculate.md)
- [/System/Library/PrivateFrameworks/CalendarDaemon.framework/CalendarDaemon](DYLIBS/CalendarDaemon.md)
- [/System/Library/PrivateFrameworks/CalendarDatabase.framework/CalendarDatabase](DYLIBS/CalendarDatabase.md)
- [/System/Library/PrivateFrameworks/CalendarFoundation.framework/CalendarFoundation](DYLIBS/CalendarFoundation.md)
- [/System/Library/PrivateFrameworks/CalendarLink.framework/CalendarLink](DYLIBS/CalendarLink.md)
- [/System/Library/PrivateFrameworks/CalendarMigration.framework/CalendarMigration](DYLIBS/CalendarMigration.md)
- [/System/Library/PrivateFrameworks/CalendarNotification.framework/CalendarNotification](DYLIBS/CalendarNotification.md)
- [/System/Library/PrivateFrameworks/CalendarUIKit.framework/CalendarUIKit](DYLIBS/CalendarUIKit.md)
- [/System/Library/PrivateFrameworks/CalendarWidget.framework/CalendarWidget](DYLIBS/CalendarWidget.md)
- [/System/Library/PrivateFrameworks/CallHistory.framework/CallHistory](DYLIBS/CallHistory.md)
- [/System/Library/PrivateFrameworks/CameraColorProcessing.framework/CameraColorProcessing](DYLIBS/CameraColorProcessing.md)
- [/System/Library/PrivateFrameworks/CameraEditKit.framework/CameraEditKit](DYLIBS/CameraEditKit.md)
- [/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI](DYLIBS/CameraUI.md)
- [/System/Library/PrivateFrameworks/CaptiveNetwork.framework/CaptiveNetwork](DYLIBS/CaptiveNetwork.md)
- [/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework](DYLIBS/CarAccessoryFramework.md)
- [/System/Library/PrivateFrameworks/CarKit.framework/CarKit](DYLIBS/CarKit.md)
- [/System/Library/PrivateFrameworks/CarKitNavigation.framework/CarKitNavigation](DYLIBS/CarKitNavigation.md)
- [/System/Library/PrivateFrameworks/CarPlayServices.framework/CarPlayServices](DYLIBS/CarPlayServices.md)
- [/System/Library/PrivateFrameworks/CarPlaySupport.framework/CarPlaySupport](DYLIBS/CarPlaySupport.md)
- [/System/Library/PrivateFrameworks/CarPlayUIServices.framework/CarPlayUIServices](DYLIBS/CarPlayUIServices.md)
- [/System/Library/PrivateFrameworks/CardKit.framework/CardKit](DYLIBS/CardKit.md)
- [/System/Library/PrivateFrameworks/CascadeEngine.framework/CascadeEngine](DYLIBS/CascadeEngine.md)
- [/System/Library/PrivateFrameworks/CascadeSets.framework/CascadeSets](DYLIBS/CascadeSets.md)
- [/System/Library/PrivateFrameworks/Catalyst.framework/Catalyst](DYLIBS/Catalyst.md)
- [/System/Library/PrivateFrameworks/Categories.framework/Categories](DYLIBS/Categories.md)
- [/System/Library/PrivateFrameworks/CellularBridgeUI.framework/CellularBridgeUI](DYLIBS/CellularBridgeUI.md)
- [/System/Library/PrivateFrameworks/CellularPlanManager.framework/CellularPlanManager](DYLIBS/CellularPlanManager.md)
- [/System/Library/PrivateFrameworks/ChatKit.framework/ChatKit](DYLIBS/ChatKit.md)
- [/System/Library/PrivateFrameworks/ChronoCore.framework/ChronoCore](DYLIBS/ChronoCore.md)
- [/System/Library/PrivateFrameworks/ChronoKit.framework/ChronoKit](DYLIBS/ChronoKit.md)
- [/System/Library/PrivateFrameworks/ChronoServices.framework/ChronoServices](DYLIBS/ChronoServices.md)
- [/System/Library/PrivateFrameworks/ChunkingLibrary.framework/ChunkingLibrary](DYLIBS/ChunkingLibrary.md)
- [/System/Library/PrivateFrameworks/CinematicFraming.framework/CinematicFraming](DYLIBS/CinematicFraming.md)
- [/System/Library/PrivateFrameworks/CipherML.framework/CipherML](DYLIBS/CipherML.md)
- [/System/Library/PrivateFrameworks/ClarityFoundation.framework/ClarityFoundation](DYLIBS/ClarityFoundation.md)
- [/System/Library/PrivateFrameworks/ClipServices.framework/ClipServices](DYLIBS/ClipServices.md)
- [/System/Library/PrivateFrameworks/ClockKitUI.framework/ClockKitUI](DYLIBS/ClockKitUI.md)
- [/System/Library/PrivateFrameworks/ClockPoster.framework/ClockPoster](DYLIBS/ClockPoster.md)
- [/System/Library/PrivateFrameworks/CloudAsset.framework/CloudAsset](DYLIBS/CloudAsset.md)
- [/System/Library/PrivateFrameworks/CloudDocs.framework/CloudDocs](DYLIBS/CloudDocs.md)
- [/System/Library/PrivateFrameworks/CloudDocsDaemon.framework/CloudDocsDaemon](DYLIBS/CloudDocsDaemon.md)
- [/System/Library/PrivateFrameworks/CloudKitCode.framework/CloudKitCode](DYLIBS/CloudKitCode.md)
- [/System/Library/PrivateFrameworks/CloudKitDaemon.framework/CloudKitDaemon](DYLIBS/CloudKitDaemon.md)
- [/System/Library/PrivateFrameworks/CloudKitDistributedSync.framework/CloudKitDistributedSync](DYLIBS/CloudKitDistributedSync.md)
- [/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/CloudPhotoLibrary](DYLIBS/CloudPhotoLibrary.md)
- [/System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/CloudSubscriptionFeatures](DYLIBS/CloudSubscriptionFeatures.md)
- [/System/Library/PrivateFrameworks/CloudTelemetry.framework/CloudTelemetry](DYLIBS/CloudTelemetry.md)
- [/System/Library/PrivateFrameworks/Coherence.framework/Coherence](DYLIBS/Coherence.md)
- [/System/Library/PrivateFrameworks/CollectionViewCore.framework/CollectionViewCore](DYLIBS/CollectionViewCore.md)
- [/System/Library/PrivateFrameworks/CollectionsInternal.framework/CollectionsInternal](DYLIBS/CollectionsInternal.md)
- [/System/Library/PrivateFrameworks/CommonUtilities.framework/CommonUtilities](DYLIBS/CommonUtilities.md)
- [/System/Library/PrivateFrameworks/CommunicationSafetySettingsUI.framework/CommunicationSafetySettingsUI](DYLIBS/CommunicationSafetySettingsUI.md)
- [/System/Library/PrivateFrameworks/CommunicationsFilter.framework/CommunicationsFilter](DYLIBS/CommunicationsFilter.md)
- [/System/Library/PrivateFrameworks/CommunicationsSetupUI.framework/CommunicationsSetupUI](DYLIBS/CommunicationsSetupUI.md)
- [/System/Library/PrivateFrameworks/CompanionServices.framework/CompanionServices](DYLIBS/CompanionServices.md)
- [/System/Library/PrivateFrameworks/CompanionSync.framework/CompanionSync](DYLIBS/CompanionSync.md)
- [/System/Library/PrivateFrameworks/CompassUI.framework/CompassUI](DYLIBS/CompassUI.md)
- [/System/Library/PrivateFrameworks/ConfigurationEngineModel.framework/ConfigurationEngineModel](DYLIBS/ConfigurationEngineModel.md)
- [/System/Library/PrivateFrameworks/ContactlessReaderUI.framework/ContactlessReaderUI](DYLIBS/ContactlessReaderUI.md)
- [/System/Library/PrivateFrameworks/ContactsAutocomplete.framework/ContactsAutocomplete](DYLIBS/ContactsAutocomplete.md)
- [/System/Library/PrivateFrameworks/ContactsAutocompleteUI.framework/ContactsAutocompleteUI](DYLIBS/ContactsAutocompleteUI.md)
- [/System/Library/PrivateFrameworks/ContactsDonation.framework/ContactsDonation](DYLIBS/ContactsDonation.md)
- [/System/Library/PrivateFrameworks/ContactsFoundation.framework/ContactsFoundation](DYLIBS/ContactsFoundation.md)
- [/System/Library/PrivateFrameworks/ContactsMetrics.framework/ContactsMetrics](DYLIBS/ContactsMetrics.md)
- [/System/Library/PrivateFrameworks/ContactsUICore.framework/ContactsUICore](DYLIBS/ContactsUICore.md)
- [/System/Library/PrivateFrameworks/ContainerManagerCommon.framework/ContainerManagerCommon](DYLIBS/ContainerManagerCommon.md)
- [/System/Library/PrivateFrameworks/ContentKit.framework/ContentKit](DYLIBS/ContentKit.md)
- [/System/Library/PrivateFrameworks/ContextKit.framework/ContextKit](DYLIBS/ContextKit.md)
- [/System/Library/PrivateFrameworks/ContextKitCore.framework/ContextKitCore](DYLIBS/ContextKitCore.md)
- [/System/Library/PrivateFrameworks/ContextKitExtraction.framework/ContextKitExtraction](DYLIBS/ContextKitExtraction.md)
- [/System/Library/PrivateFrameworks/ContextKitPrediction.framework/ContextKitPrediction](DYLIBS/ContextKitPrediction.md)
- [/System/Library/PrivateFrameworks/ContextSync.framework/ContextSync](DYLIBS/ContextSync.md)
- [/System/Library/PrivateFrameworks/ContextualActionsClient.framework/ContextualActionsClient](DYLIBS/ContextualActionsClient.md)
- [/System/Library/PrivateFrameworks/ContextualSuggestionClient.framework/ContextualSuggestionClient](DYLIBS/ContextualSuggestionClient.md)
- [/System/Library/PrivateFrameworks/ContextualUnderstanding.framework/ContextualUnderstanding](DYLIBS/ContextualUnderstanding.md)
- [/System/Library/PrivateFrameworks/ControlCenterServices.framework/ControlCenterServices](DYLIBS/ControlCenterServices.md)
- [/System/Library/PrivateFrameworks/ControlCenterUI.framework/ControlCenterUI](DYLIBS/ControlCenterUI.md)
- [/System/Library/PrivateFrameworks/ControlCenterUIKit.framework/ControlCenterUIKit](DYLIBS/ControlCenterUIKit.md)
- [/System/Library/PrivateFrameworks/ConversationKit.framework/ConversationKit](DYLIBS/ConversationKit.md)
- [/System/Library/PrivateFrameworks/Coordination.framework/Coordination](DYLIBS/Coordination.md)
- [/System/Library/PrivateFrameworks/CoordinationCore.framework/CoordinationCore](DYLIBS/CoordinationCore.md)
- [/System/Library/PrivateFrameworks/CopresenceCore.framework/CopresenceCore](DYLIBS/CopresenceCore.md)
- [/System/Library/PrivateFrameworks/CoreALD.framework/CoreALD](DYLIBS/CoreALD.md)
- [/System/Library/PrivateFrameworks/CoreAccessories.framework/CoreAccessories](DYLIBS/CoreAccessories.md)
- [/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics](DYLIBS/CoreAnalytics.md)
- [/System/Library/PrivateFrameworks/CoreAppleCVA.framework/CoreAppleCVA](DYLIBS/CoreAppleCVA.md)
- [/System/Library/PrivateFrameworks/CoreAutoLayout.framework/CoreAutoLayout](DYLIBS/CoreAutoLayout.md)
- [/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness](DYLIBS/CoreBrightness.md)
- [/System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP](DYLIBS/CoreCDP.md)
- [/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal](DYLIBS/CoreCDPInternal.md)
- [/System/Library/PrivateFrameworks/CoreCDPUI.framework/CoreCDPUI](DYLIBS/CoreCDPUI.md)
- [/System/Library/PrivateFrameworks/CoreCDPUIInternal.framework/CoreCDPUIInternal](DYLIBS/CoreCDPUIInternal.md)
- [/System/Library/PrivateFrameworks/CoreChartSwift.framework/CoreChartSwift](DYLIBS/CoreChartSwift.md)
- [/System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet](DYLIBS/CoreDuet.md)
- [/System/Library/PrivateFrameworks/CoreDuetContext.framework/CoreDuetContext](DYLIBS/CoreDuetContext.md)
- [/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/CoreEmbeddedSpeechRecognition](DYLIBS/CoreEmbeddedSpeechRecognition.md)
- [/System/Library/PrivateFrameworks/CoreEmoji.framework/CoreEmoji](DYLIBS/CoreEmoji.md)
- [/System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp](DYLIBS/CoreFollowUp.md)
- [/System/Library/PrivateFrameworks/CoreFollowUpUI.framework/CoreFollowUpUI](DYLIBS/CoreFollowUpUI.md)
- [/System/Library/PrivateFrameworks/CoreHAP.framework/CoreHAP](DYLIBS/CoreHAP.md)
- [/System/Library/PrivateFrameworks/CoreHandwriting.framework/CoreHandwriting](DYLIBS/CoreHandwriting.md)
- [/System/Library/PrivateFrameworks/CoreIDCred.framework/CoreIDCred](DYLIBS/CoreIDCred.md)
- [/System/Library/PrivateFrameworks/CoreIDV.framework/CoreIDV](DYLIBS/CoreIDV.md)
- [/System/Library/PrivateFrameworks/CoreIDVPAD.framework/CoreIDVPAD](DYLIBS/CoreIDVPAD.md)
- [/System/Library/PrivateFrameworks/CoreIDVRGBLiveness.framework/CoreIDVRGBLiveness](DYLIBS/CoreIDVRGBLiveness.md)
- [/System/Library/PrivateFrameworks/CoreIDVShared.framework/CoreIDVShared](DYLIBS/CoreIDVShared.md)
- [/System/Library/PrivateFrameworks/CoreIDVUI.framework/CoreIDVUI](DYLIBS/CoreIDVUI.md)
- [/System/Library/PrivateFrameworks/CoreIK.framework/CoreIK](DYLIBS/CoreIK.md)
- [/System/Library/PrivateFrameworks/CoreIndoor.framework/CoreIndoor](DYLIBS/CoreIndoor.md)
- [/System/Library/PrivateFrameworks/CoreKnowledge.framework/CoreKnowledge](DYLIBS/CoreKnowledge.md)
- [/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf](DYLIBS/CoreLocationProtobuf.md)
- [/System/Library/PrivateFrameworks/CoreLocationReplay.framework/CoreLocationReplay](DYLIBS/CoreLocationReplay.md)
- [/System/Library/PrivateFrameworks/CoreMaterial.framework/CoreMaterial](DYLIBS/CoreMaterial.md)
- [/System/Library/PrivateFrameworks/CoreMediaStream.framework/CoreMediaStream](DYLIBS/CoreMediaStream.md)
- [/System/Library/PrivateFrameworks/CoreMotionAlgorithms.framework/CoreMotionAlgorithms](DYLIBS/CoreMotionAlgorithms.md)
- [/System/Library/PrivateFrameworks/CoreNLP.framework/CoreNLP](DYLIBS/CoreNLP.md)
- [/System/Library/PrivateFrameworks/CoreNavigation.framework/CoreNavigation](DYLIBS/CoreNavigation.md)
- [/System/Library/PrivateFrameworks/CoreOC.framework/CoreOC](DYLIBS/CoreOC.md)
- [/System/Library/PrivateFrameworks/CoreOCModules.framework/CoreOCModules](DYLIBS/CoreOCModules.md)
- [/System/Library/PrivateFrameworks/CoreODIEssentials.framework/CoreODIEssentials](DYLIBS/CoreODIEssentials.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/CoreParsec](DYLIBS/CoreParsec.md)
- [/System/Library/PrivateFrameworks/CorePhoneNumbers.framework/CorePhoneNumbers](DYLIBS/CorePhoneNumbers.md)
- [/System/Library/PrivateFrameworks/CorePhotogrammetry.framework/CorePhotogrammetry](DYLIBS/CorePhotogrammetry.md)
- [/System/Library/PrivateFrameworks/CorePrescriptionLite.framework/CorePrescriptionLite](DYLIBS/CorePrescriptionLite.md)
- [/System/Library/PrivateFrameworks/CoreRecents.framework/CoreRecents](DYLIBS/CoreRecents.md)
- [/System/Library/PrivateFrameworks/CoreRecognition.framework/CoreRecognition](DYLIBS/CoreRecognition.md)
- [/System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore](DYLIBS/CoreRepairCore.md)
- [/System/Library/PrivateFrameworks/CoreRepairKit.framework/CoreRepairKit](DYLIBS/CoreRepairKit.md)
- [/System/Library/PrivateFrameworks/CoreRepairLite.framework/CoreRepairLite](DYLIBS/CoreRepairLite.md)
- [/System/Library/PrivateFrameworks/CoreRepairUI.framework/CoreRepairUI](DYLIBS/CoreRepairUI.md)
- [/System/Library/PrivateFrameworks/CoreRoutine.framework/CoreRoutine](DYLIBS/CoreRoutine.md)
- [/System/Library/PrivateFrameworks/CoreSDB.framework/CoreSDB](DYLIBS/CoreSDB.md)
- [/System/Library/PrivateFrameworks/CoreSVG.framework/CoreSVG](DYLIBS/CoreSVG.md)
- [/System/Library/PrivateFrameworks/CoreSceneUnderstanding.framework/CoreSceneUnderstanding](DYLIBS/CoreSceneUnderstanding.md)
- [/System/Library/PrivateFrameworks/CoreServicesInternal.framework/CoreServicesInternal](DYLIBS/CoreServicesInternal.md)
- [/System/Library/PrivateFrameworks/CoreServicesStore.framework/CoreServicesStore](DYLIBS/CoreServicesStore.md)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/CoreSpeech](DYLIBS/CoreSpeech.md)
- [/System/Library/PrivateFrameworks/CoreSpeechExclave.framework/CoreSpeechExclave](DYLIBS/CoreSpeechExclave.md)
- [/System/Library/PrivateFrameworks/CoreSpeechFoundation.framework/CoreSpeechFoundation](DYLIBS/CoreSpeechFoundation.md)
- [/System/Library/PrivateFrameworks/CoreSuggestions.framework/CoreSuggestions](DYLIBS/CoreSuggestions.md)
- [/System/Library/PrivateFrameworks/CoreSuggestionsInternals.framework/CoreSuggestionsInternals](DYLIBS/CoreSuggestionsInternals.md)
- [/System/Library/PrivateFrameworks/CoreSuggestionsML.framework/CoreSuggestionsML](DYLIBS/CoreSuggestionsML.md)
- [/System/Library/PrivateFrameworks/CoreSuggestionsUI.framework/CoreSuggestionsUI](DYLIBS/CoreSuggestionsUI.md)
- [/System/Library/PrivateFrameworks/CoreSymbolication.framework/CoreSymbolication](DYLIBS/CoreSymbolication.md)
- [/System/Library/PrivateFrameworks/CoreTime.framework/CoreTime](DYLIBS/CoreTime.md)
- [/System/Library/PrivateFrameworks/CoreUARP.framework/CoreUARP](DYLIBS/CoreUARP.md)
- [/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI](DYLIBS/CoreUI.md)
- [/System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils](DYLIBS/CoreUtils.md)
- [/System/Library/PrivateFrameworks/CoreUtilsExtras.framework/CoreUtilsExtras](DYLIBS/CoreUtilsExtras.md)
- [/System/Library/PrivateFrameworks/CoreUtilsSwift.framework/CoreUtilsSwift](DYLIBS/CoreUtilsSwift.md)
- [/System/Library/PrivateFrameworks/CoreUtilsUI.framework/CoreUtilsUI](DYLIBS/CoreUtilsUI.md)
- [/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi](DYLIBS/CoreWiFi.md)
- [/System/Library/PrivateFrameworks/CoverSheet.framework/CoverSheet](DYLIBS/CoverSheet.md)
- [/System/Library/PrivateFrameworks/CoverSheetKit.framework/CoverSheetKit](DYLIBS/CoverSheetKit.md)
- [/System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport](DYLIBS/CrashReporterSupport.md)
- [/System/Library/PrivateFrameworks/CryptoKitCBridging.framework/CryptoKitCBridging](DYLIBS/CryptoKitCBridging.md)
- [/System/Library/PrivateFrameworks/CryptoKitPrivate.framework/CryptoKitPrivate](DYLIBS/CryptoKitPrivate.md)
- [/System/Library/PrivateFrameworks/DAAPKit.framework/DAAPKit](DYLIBS/DAAPKit.md)
- [/System/Library/PrivateFrameworks/DMCEnrollmentLibrary.framework/DMCEnrollmentLibrary](DYLIBS/DMCEnrollmentLibrary.md)
- [/System/Library/PrivateFrameworks/DMCEnrollmentProvider.framework/DMCEnrollmentProvider](DYLIBS/DMCEnrollmentProvider.md)
- [/System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities](DYLIBS/DMCUtilities.md)
- [/System/Library/PrivateFrameworks/DTXConnectionServices.framework/DTXConnectionServices](DYLIBS/DTXConnectionServices.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/DVTInstrumentsFoundation](DYLIBS/DVTInstrumentsFoundation.md)
- [/System/Library/PrivateFrameworks/DashBoard.framework/DashBoard](DYLIBS/DashBoard.md)
- [/System/Library/PrivateFrameworks/DataAccess.framework/DataAccess](DYLIBS/DataAccess.md)
- [/System/Library/PrivateFrameworks/DataDeliveryServices.framework/DataDeliveryServices](DYLIBS/DataDeliveryServices.md)
- [/System/Library/PrivateFrameworks/DataDetectorsCore.framework/DataDetectorsCore](DYLIBS/DataDetectorsCore.md)
- [/System/Library/PrivateFrameworks/DataDetectorsCore.framework/PlugIns/PhoneNumbers.plugin/PhoneNumbers](DYLIBS/PhoneNumbers.md)
- [/System/Library/PrivateFrameworks/DataDetectorsNaturalLanguage.framework/DataDetectorsNaturalLanguage](DYLIBS/DataDetectorsNaturalLanguage.md)
- [/System/Library/PrivateFrameworks/DataDetectorsUI.framework/DataDetectorsUI](DYLIBS/DataDetectorsUI.md)
- [/System/Library/PrivateFrameworks/DataMigration.framework/DataMigration](DYLIBS/DataMigration.md)
- [/System/Library/PrivateFrameworks/Dendrite.framework/Dendrite](DYLIBS/Dendrite.md)
- [/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/DesktopServicesPriv](DYLIBS/DesktopServicesPriv.md)
- [/System/Library/PrivateFrameworks/DeviceAccess.framework/DeviceAccess](DYLIBS/DeviceAccess.md)
- [/System/Library/PrivateFrameworks/DeviceCheckInternal.framework/DeviceCheckInternal](DYLIBS/DeviceCheckInternal.md)
- [/System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity](DYLIBS/DeviceIdentity.md)
- [/System/Library/PrivateFrameworks/DeviceManagement.framework/DeviceManagement](DYLIBS/DeviceManagement.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/DiagnosticExtensions](DYLIBS/DiagnosticExtensions.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensionsDaemon.framework/DiagnosticExtensionsDaemon](DYLIBS/DiagnosticExtensionsDaemon.md)
- [/System/Library/PrivateFrameworks/DiagnosticRequest.framework/DiagnosticRequest](DYLIBS/DiagnosticRequest.md)
- [/System/Library/PrivateFrameworks/DiagnosticRequestService.framework/DiagnosticRequestService](DYLIBS/DiagnosticRequestService.md)
- [/System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport](DYLIBS/DiagnosticsSupport.md)
- [/System/Library/PrivateFrameworks/DialogEngine.framework/DialogEngine](DYLIBS/DialogEngine.md)
- [/System/Library/PrivateFrameworks/DictionaryServices.framework/DictionaryServices](DYLIBS/DictionaryServices.md)
- [/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/DifferentialPrivacy](DYLIBS/DifferentialPrivacy.md)
- [/System/Library/PrivateFrameworks/DigitalAccess.framework/DigitalAccess](DYLIBS/DigitalAccess.md)
- [/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI](DYLIBS/DigitalSeparationUI.md)
- [/System/Library/PrivateFrameworks/DisembarkUI.framework/DisembarkUI](DYLIBS/DisembarkUI.md)
- [/System/Library/PrivateFrameworks/DiskImages.framework/DiskImages](DYLIBS/DiskImages.md)
- [/System/Library/PrivateFrameworks/DiskImages2.framework/DiskImages2](DYLIBS/DiskImages2.md)
- [/System/Library/PrivateFrameworks/DistributedEvaluation.framework/DistributedEvaluation](DYLIBS/DistributedEvaluation.md)
- [/System/Library/PrivateFrameworks/DoNotDisturb.framework/DoNotDisturb](DYLIBS/DoNotDisturb.md)
- [/System/Library/PrivateFrameworks/DoNotDisturbKit.framework/DoNotDisturbKit](DYLIBS/DoNotDisturbKit.md)
- [/System/Library/PrivateFrameworks/DoNotDisturbServer.framework/DoNotDisturbServer](DYLIBS/DoNotDisturbServer.md)
- [/System/Library/PrivateFrameworks/DockKitCore.framework/DockKitCore](DYLIBS/DockKitCore.md)
- [/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera](DYLIBS/DocumentCamera.md)
- [/System/Library/PrivateFrameworks/DocumentManager.framework/DocumentManager](DYLIBS/DocumentManager.md)
- [/System/Library/PrivateFrameworks/DocumentManagerCore.framework/DocumentManagerCore](DYLIBS/DocumentManagerCore.md)
- [/System/Library/PrivateFrameworks/DocumentManagerExecutables.framework/DocumentManagerExecutables](DYLIBS/DocumentManagerExecutables.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/DocumentManagerUICore](DYLIBS/DocumentManagerUICore.md)
- [/System/Library/PrivateFrameworks/DocumentUnderstanding.framework/DocumentUnderstanding](DYLIBS/DocumentUnderstanding.md)
- [/System/Library/PrivateFrameworks/DocumentUnderstandingClient.framework/DocumentUnderstandingClient](DYLIBS/DocumentUnderstandingClient.md)
- [/System/Library/PrivateFrameworks/DriverManagement.framework/DriverManagement](DYLIBS/DriverManagement.md)
- [/System/Library/PrivateFrameworks/DropIn.framework/DropIn](DYLIBS/DropIn.md)
- [/System/Library/PrivateFrameworks/DropInCore.framework/DropInCore](DYLIBS/DropInCore.md)
- [/System/Library/PrivateFrameworks/DuetActivityScheduler.framework/DuetActivityScheduler](DYLIBS/DuetActivityScheduler.md)
- [/System/Library/PrivateFrameworks/EAP8021X.framework/EAP8021X](DYLIBS/EAP8021X.md)
- [/System/Library/PrivateFrameworks/Email.framework/Email](DYLIBS/Email.md)
- [/System/Library/PrivateFrameworks/EmailAddressing.framework/EmailAddressing](DYLIBS/EmailAddressing.md)
- [/System/Library/PrivateFrameworks/EmailCore.framework/EmailCore](DYLIBS/EmailCore.md)
- [/System/Library/PrivateFrameworks/EmailDaemon.framework/EmailDaemon](DYLIBS/EmailDaemon.md)
- [/System/Library/PrivateFrameworks/EmailFoundation.framework/EmailFoundation](DYLIBS/EmailFoundation.md)
- [/System/Library/PrivateFrameworks/EmbeddedAcousticRecognition.framework/EmbeddedAcousticRecognition](DYLIBS/EmbeddedAcousticRecognition.md)
- [/System/Library/PrivateFrameworks/EmbeddingService.framework/EmbeddingService](DYLIBS/EmbeddingService.md)
- [/System/Library/PrivateFrameworks/EmergencyAlerts.framework/EmergencyAlerts](DYLIBS/EmergencyAlerts.md)
- [/System/Library/PrivateFrameworks/EmojiFoundation.framework/EmojiFoundation](DYLIBS/EmojiFoundation.md)
- [/System/Library/PrivateFrameworks/EmojiKit.framework/EmojiKit](DYLIBS/EmojiKit.md)
- [/System/Library/PrivateFrameworks/Engram.framework/Engram](DYLIBS/Engram.md)
- [/System/Library/PrivateFrameworks/EnhancedLoggingState.framework/EnhancedLoggingState](DYLIBS/EnhancedLoggingState.md)
- [/System/Library/PrivateFrameworks/Espresso.framework/Espresso](DYLIBS/Espresso.md)
- [/System/Library/PrivateFrameworks/ExposureNotificationDaemon.framework/ExposureNotificationDaemon](DYLIBS/ExposureNotificationDaemon.md)
- [/System/Library/PrivateFrameworks/FMCore.framework/FMCore](DYLIBS/FMCore.md)
- [/System/Library/PrivateFrameworks/FMCoreLite.framework/FMCoreLite](DYLIBS/FMCoreLite.md)
- [/System/Library/PrivateFrameworks/FMCoreUI.framework/FMCoreUI](DYLIBS/FMCoreUI.md)
- [/System/Library/PrivateFrameworks/FMF.framework/FMF](DYLIBS/FMF.md)
- [/System/Library/PrivateFrameworks/FMFCore.framework/FMFCore](DYLIBS/FMFCore.md)
- [/System/Library/PrivateFrameworks/FMFUI.framework/FMFUI](DYLIBS/FMFUI.md)
- [/System/Library/PrivateFrameworks/FMFindingUI.framework/FMFindingUI](DYLIBS/FMFindingUI.md)
- [/System/Library/PrivateFrameworks/FMIPCore.framework/FMIPCore](DYLIBS/FMIPCore.md)
- [/System/Library/PrivateFrameworks/FMNetworking.framework/FMNetworking](DYLIBS/FMNetworking.md)
- [/System/Library/PrivateFrameworks/FRC.framework/FRC](DYLIBS/FRC.md)
- [/System/Library/PrivateFrameworks/FSEvents.framework/FSEvents](DYLIBS/FSEvents.md)
- [/System/Library/PrivateFrameworks/FTServices.framework/FTServices](DYLIBS/FTServices.md)
- [/System/Library/PrivateFrameworks/FaceTimeMessageStore.framework/FaceTimeMessageStore](DYLIBS/FaceTimeMessageStore.md)
- [/System/Library/PrivateFrameworks/FamilyCircle.framework/FamilyCircle](DYLIBS/FamilyCircle.md)
- [/System/Library/PrivateFrameworks/FamilyCircleUI.framework/FamilyCircleUI](DYLIBS/FamilyCircleUI.md)
- [/System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags](DYLIBS/FeatureFlags.md)
- [/System/Library/PrivateFrameworks/FeatureFlagsSupport.framework/FeatureFlagsSupport](DYLIBS/FeatureFlagsSupport.md)
- [/System/Library/PrivateFrameworks/FeatureStore.framework/FeatureStore](DYLIBS/FeatureStore.md)
- [/System/Library/PrivateFrameworks/FeedbackLogger.framework/FeedbackLogger](DYLIBS/FeedbackLogger.md)
- [/System/Library/PrivateFrameworks/FileProviderDaemon.framework/FileProviderDaemon](DYLIBS/FileProviderDaemon.md)
- [/System/Library/PrivateFrameworks/FileProviderTelemetry.framework/FileProviderTelemetry](DYLIBS/FileProviderTelemetry.md)
- [/System/Library/PrivateFrameworks/FinHealthCore.framework/FinHealthCore](DYLIBS/FinHealthCore.md)
- [/System/Library/PrivateFrameworks/FinanceDaemon.framework/FinanceDaemon](DYLIBS/FinanceDaemon.md)
- [/System/Library/PrivateFrameworks/FindMyBase.framework/FindMyBase](DYLIBS/FindMyBase.md)
- [/System/Library/PrivateFrameworks/FindMyBluetooth.framework/FindMyBluetooth](DYLIBS/FindMyBluetooth.md)
- [/System/Library/PrivateFrameworks/FindMyCloudKit.framework/FindMyCloudKit](DYLIBS/FindMyCloudKit.md)
- [/System/Library/PrivateFrameworks/FindMyCommon.framework/FindMyCommon](DYLIBS/FindMyCommon.md)
- [/System/Library/PrivateFrameworks/FindMyCrypto.framework/FindMyCrypto](DYLIBS/FindMyCrypto.md)
- [/System/Library/PrivateFrameworks/FindMyDaemonSupport.framework/FindMyDaemonSupport](DYLIBS/FindMyDaemonSupport.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/FindMyDevice](DYLIBS/FindMyDevice.md)
- [/System/Library/PrivateFrameworks/FindMyLocate.framework/FindMyLocate](DYLIBS/FindMyLocate.md)
- [/System/Library/PrivateFrameworks/FindMyMessaging.framework/FindMyMessaging](DYLIBS/FindMyMessaging.md)
- [/System/Library/PrivateFrameworks/FindMyServerInteraction.framework/FindMyServerInteraction](DYLIBS/FindMyServerInteraction.md)
- [/System/Library/PrivateFrameworks/FindMyUICore.framework/FindMyUICore](DYLIBS/FindMyUICore.md)
- [/System/Library/PrivateFrameworks/FindMyUnsafeAsyncBridging.framework/FindMyUnsafeAsyncBridging](DYLIBS/FindMyUnsafeAsyncBridging.md)
- [/System/Library/PrivateFrameworks/FitnessCoachingCore.framework/FitnessCoachingCore](DYLIBS/FitnessCoachingCore.md)
- [/System/Library/PrivateFrameworks/FitnessCoachingServices.framework/FitnessCoachingServices](DYLIBS/FitnessCoachingServices.md)
- [/System/Library/PrivateFrameworks/FitnessUI.framework/FitnessUI](DYLIBS/FitnessUI.md)
- [/System/Library/PrivateFrameworks/FlexMusicKit.framework/FlexMusicKit](DYLIBS/FlexMusicKit.md)
- [/System/Library/PrivateFrameworks/FlightUtilities.framework/FlightUtilities](DYLIBS/FlightUtilities.md)
- [/System/Library/PrivateFrameworks/FlightUtilitiesCore.framework/FlightUtilitiesCore](DYLIBS/FlightUtilitiesCore.md)
- [/System/Library/PrivateFrameworks/Focus.framework/Focus](DYLIBS/Focus.md)
- [/System/Library/PrivateFrameworks/FocusUI.framework/FocusUI](DYLIBS/FocusUI.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/FontServices](DYLIBS/FontServices.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/libFontParser.dylib](DYLIBS/libFontParser.dylib.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/libGSFont.dylib](DYLIBS/libGSFont.dylib.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/libhvf.dylib](DYLIBS/libhvf.dylib.md)
- [/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard](DYLIBS/FrontBoard.md)
- [/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices](DYLIBS/FrontBoardServices.md)
- [/System/Library/PrivateFrameworks/FusionTracker.framework/FusionTracker](DYLIBS/FusionTracker.md)
- [/System/Library/PrivateFrameworks/Futhark.framework/Futhark](DYLIBS/Futhark.md)
- [/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/libComposeFilters.dylib](DYLIBS/libComposeFilters.dylib.md)
- [/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/libGPUCompiler.dylib](DYLIBS/libGPUCompiler.dylib.md)
- [/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/libGPUCompilerImpl.dylib](DYLIBS/libGPUCompilerImpl.dylib.md)
- [/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/libGPUCompilerImplLazy.dylib](DYLIBS/libGPUCompilerImplLazy.dylib.md)
- [/System/Library/PrivateFrameworks/GPURawCounter.framework/GPURawCounter](DYLIBS/GPURawCounter.md)
- [/System/Library/PrivateFrameworks/GPUToolsTransport.framework/GPUToolsTransport](DYLIBS/GPUToolsTransport.md)
- [/System/Library/PrivateFrameworks/GRDBInternal.framework/GRDBInternal](DYLIBS/GRDBInternal.md)
- [/System/Library/PrivateFrameworks/GameCenterFoundation.framework/GameCenterFoundation](DYLIBS/GameCenterFoundation.md)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/GameCenterUI](DYLIBS/GameCenterUI.md)
- [/System/Library/PrivateFrameworks/GameCenterUICore.framework/GameCenterUICore](DYLIBS/GameCenterUICore.md)
- [/System/Library/PrivateFrameworks/GameKitServices.framework/GameKitServices](DYLIBS/GameKitServices.md)
- [/System/Library/PrivateFrameworks/GamePolicy.framework/GamePolicy](DYLIBS/GamePolicy.md)
- [/System/Library/PrivateFrameworks/GenerationalStorage.framework/GenerationalStorage](DYLIBS/GenerationalStorage.md)
- [/System/Library/PrivateFrameworks/GeoAnalytics.framework/GeoAnalytics](DYLIBS/GeoAnalytics.md)
- [/System/Library/PrivateFrameworks/GeoServices.framework/GeoServices](DYLIBS/GeoServices.md)
- [/System/Library/PrivateFrameworks/GeoServicesCore.framework/GeoServicesCore](DYLIBS/GeoServicesCore.md)
- [/System/Library/PrivateFrameworks/GridDataServices.framework/GridDataServices](DYLIBS/GridDataServices.md)
- [/System/Library/PrivateFrameworks/GroupKitCrypto.framework/GroupKitCrypto](DYLIBS/GroupKitCrypto.md)
- [/System/Library/PrivateFrameworks/H16ISPServices.framework/H16ISPServices](DYLIBS/H16ISPServices.md)
- [/System/Library/PrivateFrameworks/HAENotifications.framework/HAENotifications](DYLIBS/HAENotifications.md)
- [/System/Library/PrivateFrameworks/HDRProcessing.framework/HDRProcessing](DYLIBS/HDRProcessing.md)
- [/System/Library/PrivateFrameworks/HID.framework/HID](DYLIBS/HID.md)
- [/System/Library/PrivateFrameworks/HIDAnalytics.framework/HIDAnalytics](DYLIBS/HIDAnalytics.md)
- [/System/Library/PrivateFrameworks/HMFoundation.framework/HMFoundation](DYLIBS/HMFoundation.md)
- [/System/Library/PrivateFrameworks/HRTFEnrollment.framework/HRTFEnrollment](DYLIBS/HRTFEnrollment.md)
- [/System/Library/PrivateFrameworks/HangTracer.framework/HangTracer](DYLIBS/HangTracer.md)
- [/System/Library/PrivateFrameworks/HeadphoneConfigs.framework/HeadphoneConfigs](DYLIBS/HeadphoneConfigs.md)
- [/System/Library/PrivateFrameworks/HeadphoneSettings.framework/HeadphoneSettings](DYLIBS/HeadphoneSettings.md)
- [/System/Library/PrivateFrameworks/HealthAppHealthDaemon.framework/HealthAppHealthDaemon](DYLIBS/HealthAppHealthDaemon.md)
- [/System/Library/PrivateFrameworks/HealthAppHealthDaemonSupport.framework/HealthAppHealthDaemonSupport](DYLIBS/HealthAppHealthDaemonSupport.md)
- [/System/Library/PrivateFrameworks/HealthArticlesGeneration.framework/HealthArticlesGeneration](DYLIBS/HealthArticlesGeneration.md)
- [/System/Library/PrivateFrameworks/HealthArticlesUI.framework/HealthArticlesUI](DYLIBS/HealthArticlesUI.md)
- [/System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon](DYLIBS/HealthDaemon.md)
- [/System/Library/PrivateFrameworks/HealthDaemonFoundation.framework/HealthDaemonFoundation](DYLIBS/HealthDaemonFoundation.md)
- [/System/Library/PrivateFrameworks/HealthExperience.framework/HealthExperience](DYLIBS/HealthExperience.md)
- [/System/Library/PrivateFrameworks/HealthExperienceUI.framework/HealthExperienceUI](DYLIBS/HealthExperienceUI.md)
- [/System/Library/PrivateFrameworks/HealthHearing.framework/HealthHearing](DYLIBS/HealthHearing.md)
- [/System/Library/PrivateFrameworks/HealthHearingDaemon.framework/HealthHearingDaemon](DYLIBS/HealthHearingDaemon.md)
- [/System/Library/PrivateFrameworks/HealthKitAdditions.framework/HealthKitAdditions](DYLIBS/HealthKitAdditions.md)
- [/System/Library/PrivateFrameworks/HealthMedications.framework/HealthMedications](DYLIBS/HealthMedications.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsDaemonPlugin.framework/HealthMedicationsDaemonPlugin](DYLIBS/HealthMedicationsDaemonPlugin.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsExperience.framework/HealthMedicationsExperience](DYLIBS/HealthMedicationsExperience.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsUI.framework/HealthMedicationsUI](DYLIBS/HealthMedicationsUI.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsVisionUI.framework/HealthMedicationsVisionUI](DYLIBS/HealthMedicationsVisionUI.md)
- [/System/Library/PrivateFrameworks/HealthMenstrualCycles.framework/HealthMenstrualCycles](DYLIBS/HealthMenstrualCycles.md)
- [/System/Library/PrivateFrameworks/HealthMenstrualCyclesDaemon.framework/HealthMenstrualCyclesDaemon](DYLIBS/HealthMenstrualCyclesDaemon.md)
- [/System/Library/PrivateFrameworks/HealthMobility.framework/HealthMobility](DYLIBS/HealthMobility.md)
- [/System/Library/PrivateFrameworks/HealthMobilityDaemon.framework/HealthMobilityDaemon](DYLIBS/HealthMobilityDaemon.md)
- [/System/Library/PrivateFrameworks/HealthPlatform.framework/HealthPlatform](DYLIBS/HealthPlatform.md)
- [/System/Library/PrivateFrameworks/HealthPlatformCore.framework/HealthPlatformCore](DYLIBS/HealthPlatformCore.md)
- [/System/Library/PrivateFrameworks/HealthPluginHost.framework/HealthPluginHost](DYLIBS/HealthPluginHost.md)
- [/System/Library/PrivateFrameworks/HealthRecordServices.framework/HealthRecordServices](DYLIBS/HealthRecordServices.md)
- [/System/Library/PrivateFrameworks/HealthRecordsConceptsSupport.framework/HealthRecordsConceptsSupport](DYLIBS/HealthRecordsConceptsSupport.md)
- [/System/Library/PrivateFrameworks/HealthRecordsDaemon.framework/HealthRecordsDaemon](DYLIBS/HealthRecordsDaemon.md)
- [/System/Library/PrivateFrameworks/HealthRecordsUI.framework/HealthRecordsUI](DYLIBS/HealthRecordsUI.md)
- [/System/Library/PrivateFrameworks/HealthToolbox.framework/HealthToolbox](DYLIBS/HealthToolbox.md)
- [/System/Library/PrivateFrameworks/HealthUI.framework/HealthUI](DYLIBS/HealthUI.md)
- [/System/Library/PrivateFrameworks/HealthVisualization.framework/HealthVisualization](DYLIBS/HealthVisualization.md)
- [/System/Library/PrivateFrameworks/HearingCore.framework/HearingCore](DYLIBS/HearingCore.md)
- [/System/Library/PrivateFrameworks/HearingUI.framework/HearingUI](DYLIBS/HearingUI.md)
- [/System/Library/PrivateFrameworks/HearingUtilities.framework/HearingUtilities](DYLIBS/HearingUtilities.md)
- [/System/Library/PrivateFrameworks/HeartHealth.framework/HeartHealth](DYLIBS/HeartHealth.md)
- [/System/Library/PrivateFrameworks/HeartHealthDaemon.framework/HeartHealthDaemon](DYLIBS/HeartHealthDaemon.md)
- [/System/Library/PrivateFrameworks/HeroDataClient.framework/HeroDataClient](DYLIBS/HeroDataClient.md)
- [/System/Library/PrivateFrameworks/Home.framework/Home](DYLIBS/Home.md)
- [/System/Library/PrivateFrameworks/HomeAccessoryControlUI.framework/HomeAccessoryControlUI](DYLIBS/HomeAccessoryControlUI.md)
- [/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/HomeAutomationInternal](DYLIBS/HomeAutomationInternal.md)
- [/System/Library/PrivateFrameworks/HomeCommunicationUIFramework.framework/HomeCommunicationUIFramework](DYLIBS/HomeCommunicationUIFramework.md)
- [/System/Library/PrivateFrameworks/HomeDataModel.framework/HomeDataModel](DYLIBS/HomeDataModel.md)
- [/System/Library/PrivateFrameworks/HomeDeviceSetup.framework/HomeDeviceSetup](DYLIBS/HomeDeviceSetup.md)
- [/System/Library/PrivateFrameworks/HomeEnergyDaemon.framework/HomeEnergyDaemon](DYLIBS/HomeEnergyDaemon.md)
- [/System/Library/PrivateFrameworks/HomeEnergyUI.framework/HomeEnergyUI](DYLIBS/HomeEnergyUI.md)
- [/System/Library/PrivateFrameworks/HomeKitBackingStore.framework/HomeKitBackingStore](DYLIBS/HomeKitBackingStore.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemon.framework/HomeKitDaemon](DYLIBS/HomeKitDaemon.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemonLegacy.framework/HomeKitDaemonLegacy](DYLIBS/HomeKitDaemonLegacy.md)
- [/System/Library/PrivateFrameworks/HomeKitEventRouter.framework/HomeKitEventRouter](DYLIBS/HomeKitEventRouter.md)
- [/System/Library/PrivateFrameworks/HomeKitEvents.framework/HomeKitEvents](DYLIBS/HomeKitEvents.md)
- [/System/Library/PrivateFrameworks/HomeKitMatter.framework/HomeKitMatter](DYLIBS/HomeKitMatter.md)
- [/System/Library/PrivateFrameworks/HomeKitMetrics.framework/HomeKitMetrics](DYLIBS/HomeKitMetrics.md)
- [/System/Library/PrivateFrameworks/HomePodSettings.framework/HomePodSettings](DYLIBS/HomePodSettings.md)
- [/System/Library/PrivateFrameworks/HomeServices.framework/HomeServices](DYLIBS/HomeServices.md)
- [/System/Library/PrivateFrameworks/HomeSharing.framework/HomeSharing](DYLIBS/HomeSharing.md)
- [/System/Library/PrivateFrameworks/HomeUI.framework/HomeUI](DYLIBS/HomeUI.md)
- [/System/Library/PrivateFrameworks/HomeUICommon.framework/HomeUICommon](DYLIBS/HomeUICommon.md)
- [/System/Library/PrivateFrameworks/HoverTextUI.framework/HoverTextUI](DYLIBS/HoverTextUI.md)
- [/System/Library/PrivateFrameworks/HumanUnderstandingFoundation.framework/HumanUnderstandingFoundation](DYLIBS/HumanUnderstandingFoundation.md)
- [/System/Library/PrivateFrameworks/IAP.framework/IAP](DYLIBS/IAP.md)
- [/System/Library/PrivateFrameworks/IDS.framework/IDS](DYLIBS/IDS.md)
- [/System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation](DYLIBS/IDSFoundation.md)
- [/System/Library/PrivateFrameworks/IDSHashPersistence.framework/IDSHashPersistence](DYLIBS/IDSHashPersistence.md)
- [/System/Library/PrivateFrameworks/IDSKVStore.framework/IDSKVStore](DYLIBS/IDSKVStore.md)
- [/System/Library/PrivateFrameworks/IMCore.framework/IMCore](DYLIBS/IMCore.md)
- [/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence](DYLIBS/IMDPersistence.md)
- [/System/Library/PrivateFrameworks/IMDaemonCore.framework/IMDaemonCore](DYLIBS/IMDaemonCore.md)
- [/System/Library/PrivateFrameworks/IMFoundation.framework/IMFoundation](DYLIBS/IMFoundation.md)
- [/System/Library/PrivateFrameworks/IMSharedUI.framework/IMSharedUI](DYLIBS/IMSharedUI.md)
- [/System/Library/PrivateFrameworks/IMSharedUtilities.framework/IMSharedUtilities](DYLIBS/IMSharedUtilities.md)
- [/System/Library/PrivateFrameworks/IMTransferAgent.framework/IMTransferAgent](DYLIBS/IMTransferAgent.md)
- [/System/Library/PrivateFrameworks/IMTransferServices.framework/IMTransferServices](DYLIBS/IMTransferServices.md)
- [/System/Library/PrivateFrameworks/IO80211.framework/IO80211](DYLIBS/IO80211.md)
- [/System/Library/PrivateFrameworks/IOAccessoryManager.framework/IOAccessoryManager](DYLIBS/IOAccessoryManager.md)
- [/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU](DYLIBS/IOGPU.md)
- [/System/Library/PrivateFrameworks/IOMobileFramebuffer.framework/IOMobileFramebuffer](DYLIBS/IOMobileFramebuffer.md)
- [/System/Library/PrivateFrameworks/IPTelephony.framework/Support/libIPTelephony.dylib](DYLIBS/libIPTelephony.dylib.md)
- [/System/Library/PrivateFrameworks/ITMLKit.framework/ITMLKit](DYLIBS/ITMLKit.md)
- [/System/Library/PrivateFrameworks/IconFoundation.framework/IconFoundation](DYLIBS/IconFoundation.md)
- [/System/Library/PrivateFrameworks/IconServices.framework/IconServices](DYLIBS/IconServices.md)
- [/System/Library/PrivateFrameworks/InAppMessages.framework/InAppMessages](DYLIBS/InAppMessages.md)
- [/System/Library/PrivateFrameworks/InAppMessagesCore.framework/InAppMessagesCore](DYLIBS/InAppMessagesCore.md)
- [/System/Library/PrivateFrameworks/InertiaCam.framework/InertiaCam](DYLIBS/InertiaCam.md)
- [/System/Library/PrivateFrameworks/InputAnalytics.framework/InputAnalytics](DYLIBS/InputAnalytics.md)
- [/System/Library/PrivateFrameworks/InputContext.framework/InputContext](DYLIBS/InputContext.md)
- [/System/Library/PrivateFrameworks/InstallCoordination.framework/InstallCoordination](DYLIBS/InstallCoordination.md)
- [/System/Library/PrivateFrameworks/InstalledContentLibrary.framework/InstalledContentLibrary](DYLIBS/InstalledContentLibrary.md)
- [/System/Library/PrivateFrameworks/IntelligenceEngine.framework/IntelligenceEngine](DYLIBS/IntelligenceEngine.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatform.framework/IntelligencePlatform](DYLIBS/IntelligencePlatform.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCompute.framework/IntelligencePlatformCompute](DYLIBS/IntelligencePlatformCompute.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/IntelligencePlatformCore](DYLIBS/IntelligencePlatformCore.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformLibrary.framework/IntelligencePlatformLibrary](DYLIBS/IntelligencePlatformLibrary.md)
- [/System/Library/PrivateFrameworks/IntelligentRouting.framework/IntelligentRouting](DYLIBS/IntelligentRouting.md)
- [/System/Library/PrivateFrameworks/IntelligentRoutingDaemon.framework/IntelligentRoutingDaemon](DYLIBS/IntelligentRoutingDaemon.md)
- [/System/Library/PrivateFrameworks/IntentsCore.framework/IntentsCore](DYLIBS/IntentsCore.md)
- [/System/Library/PrivateFrameworks/IntentsFoundation.framework/IntentsFoundation](DYLIBS/IntentsFoundation.md)
- [/System/Library/PrivateFrameworks/IntentsServices.framework/IntentsServices](DYLIBS/IntentsServices.md)
- [/System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf](DYLIBS/InternalSwiftProtobuf.md)
- [/System/Library/PrivateFrameworks/InternationalSupport.framework/InternationalSupport](DYLIBS/InternationalSupport.md)
- [/System/Library/PrivateFrameworks/IsolatedCoreAudioClient.framework/IsolatedCoreAudioClient](DYLIBS/IsolatedCoreAudioClient.md)
- [/System/Library/PrivateFrameworks/JasperDepth.framework/JasperDepth](DYLIBS/JasperDepth.md)
- [/System/Library/PrivateFrameworks/Jet.framework/Jet](DYLIBS/Jet.md)
- [/System/Library/PrivateFrameworks/JetEngine.framework/JetEngine](DYLIBS/JetEngine.md)
- [/System/Library/PrivateFrameworks/JetPack.framework/JetPack](DYLIBS/JetPack.md)
- [/System/Library/PrivateFrameworks/JetUI.framework/JetUI](DYLIBS/JetUI.md)
- [/System/Library/PrivateFrameworks/KeyboardArbiter.framework/KeyboardArbiter](DYLIBS/KeyboardArbiter.md)
- [/System/Library/PrivateFrameworks/KeyboardServices.framework/KeyboardServices](DYLIBS/KeyboardServices.md)
- [/System/Library/PrivateFrameworks/KeyboardSettingsFeedback.framework/KeyboardSettingsFeedback](DYLIBS/KeyboardSettingsFeedback.md)
- [/System/Library/PrivateFrameworks/KeychainCircle.framework/KeychainCircle](DYLIBS/KeychainCircle.md)
- [/System/Library/PrivateFrameworks/KnowledgeGraphKit.framework/KnowledgeGraphKit](DYLIBS/KnowledgeGraphKit.md)
- [/System/Library/PrivateFrameworks/KnowledgeMonitor.framework/KnowledgeMonitor](DYLIBS/KnowledgeMonitor.md)
- [/System/Library/PrivateFrameworks/Koa.framework/Koa](DYLIBS/Koa.md)
- [/System/Library/PrivateFrameworks/KoaMapper.framework/KoaMapper](DYLIBS/KoaMapper.md)
- [/System/Library/PrivateFrameworks/LACC.framework/LACC](DYLIBS/LACC.md)
- [/System/Library/PrivateFrameworks/LanguageModeling.framework/LanguageModeling](DYLIBS/LanguageModeling.md)
- [/System/Library/PrivateFrameworks/LatentSemanticMapping.framework/LatentSemanticMapping](DYLIBS/LatentSemanticMapping.md)
- [/System/Library/PrivateFrameworks/LearnedFeatures.framework/LearnedFeatures](DYLIBS/LearnedFeatures.md)
- [/System/Library/PrivateFrameworks/Lexicon.framework/Lexicon](DYLIBS/Lexicon.md)
- [/System/Library/PrivateFrameworks/LighthouseBackground.framework/LighthouseBackground](DYLIBS/LighthouseBackground.md)
- [/System/Library/PrivateFrameworks/LimitAdTracking.framework/LimitAdTracking](DYLIBS/LimitAdTracking.md)
- [/System/Library/PrivateFrameworks/LinguisticData.framework/LinguisticData](DYLIBS/LinguisticData.md)
- [/System/Library/PrivateFrameworks/LinkMetadata.framework/LinkMetadata](DYLIBS/LinkMetadata.md)
- [/System/Library/PrivateFrameworks/LinkServices.framework/LinkServices](DYLIBS/LinkServices.md)
- [/System/Library/PrivateFrameworks/LiveFS.framework/LiveFS](DYLIBS/LiveFS.md)
- [/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore](DYLIBS/LocalAuthenticationCore.md)
- [/System/Library/PrivateFrameworks/LocalAuthenticationCoreUI.framework/LocalAuthenticationCoreUI](DYLIBS/LocalAuthenticationCoreUI.md)
- [/System/Library/PrivateFrameworks/LocalAuthenticationPrivateUI.framework/LocalAuthenticationPrivateUI](DYLIBS/LocalAuthenticationPrivateUI.md)
- [/System/Library/PrivateFrameworks/LocalStatusKit.framework/LocalStatusKit](DYLIBS/LocalStatusKit.md)
- [/System/Library/PrivateFrameworks/LocationSupport.framework/LocationSupport](DYLIBS/LocationSupport.md)
- [/System/Library/PrivateFrameworks/LockdownMode.framework/LockdownMode](DYLIBS/LockdownMode.md)
- [/System/Library/PrivateFrameworks/LockoutUI.framework/LockoutUI](DYLIBS/LockoutUI.md)
- [/System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport](DYLIBS/LoggingSupport.md)
- [/System/Library/PrivateFrameworks/LowPowerMode.framework/LowPowerMode](DYLIBS/LowPowerMode.md)
- [/System/Library/PrivateFrameworks/MDMClientLibrary.framework/MDMClientLibrary](DYLIBS/MDMClientLibrary.md)
- [/System/Library/PrivateFrameworks/MFAAuthentication.framework/MFAAuthentication](DYLIBS/MFAAuthentication.md)
- [/System/Library/PrivateFrameworks/MIME.framework/MIME](DYLIBS/MIME.md)
- [/System/Library/PrivateFrameworks/MLAssetIO.framework/MLAssetIO](DYLIBS/MLAssetIO.md)
- [/System/Library/PrivateFrameworks/MMCS.framework/MMCS](DYLIBS/MMCS.md)
- [/System/Library/PrivateFrameworks/MOVStreamIO.framework/MOVStreamIO](DYLIBS/MOVStreamIO.md)
- [/System/Library/PrivateFrameworks/MPUFoundation.framework/MPUFoundation](DYLIBS/MPUFoundation.md)
- [/System/Library/PrivateFrameworks/MTLCompiler.framework/MTLCompiler](DYLIBS/MTLCompiler.md)
- [/System/Library/PrivateFrameworks/MTLCompiler.framework/libMTLCompilerHelper.dylib](DYLIBS/libMTLCompilerHelper.dylib.md)
- [/System/Library/PrivateFrameworks/MagnifierSupport.framework/MagnifierSupport](DYLIBS/MagnifierSupport.md)
- [/System/Library/PrivateFrameworks/MailKit.framework/MailKit](DYLIBS/MailKit.md)
- [/System/Library/PrivateFrameworks/MailServices.framework/MailServices](DYLIBS/MailServices.md)
- [/System/Library/PrivateFrameworks/MailSupport.framework/MailSupport](DYLIBS/MailSupport.md)
- [/System/Library/PrivateFrameworks/MailUI.framework/MailUI](DYLIBS/MailUI.md)
- [/System/Library/PrivateFrameworks/MailWebProcessSupport.framework/MailWebProcessSupport](DYLIBS/MailWebProcessSupport.md)
- [/System/Library/PrivateFrameworks/MallocStackLogging.framework/MallocStackLogging](DYLIBS/MallocStackLogging.md)
- [/System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration](DYLIBS/ManagedConfiguration.md)
- [/System/Library/PrivateFrameworks/ManagedConfigurationUI.framework/ManagedConfigurationUI](DYLIBS/ManagedConfigurationUI.md)
- [/System/Library/PrivateFrameworks/ManagedSettingsObjC.framework/ManagedSettingsObjC](DYLIBS/ManagedSettingsObjC.md)
- [/System/Library/PrivateFrameworks/MapsSuggestions.framework/MapsSuggestions](DYLIBS/MapsSuggestions.md)
- [/System/Library/PrivateFrameworks/MapsSupport.framework/MapsSupport](DYLIBS/MapsSupport.md)
- [/System/Library/PrivateFrameworks/MapsSync.framework/MapsSync](DYLIBS/MapsSync.md)
- [/System/Library/PrivateFrameworks/MapsUI.framework/MapsUI](DYLIBS/MapsUI.md)
- [/System/Library/PrivateFrameworks/Marrs.framework/Marrs](DYLIBS/Marrs.md)
- [/System/Library/PrivateFrameworks/MaterialKit.framework/MaterialKit](DYLIBS/MaterialKit.md)
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/MediaAnalysis](DYLIBS/MediaAnalysis.md)
- [/System/Library/PrivateFrameworks/MediaAnalysisServices.framework/MediaAnalysisServices](DYLIBS/MediaAnalysisServices.md)
- [/System/Library/PrivateFrameworks/MediaControlSender.framework/MediaControlSender](DYLIBS/MediaControlSender.md)
- [/System/Library/PrivateFrameworks/MediaControls.framework/MediaControls](DYLIBS/MediaControls.md)
- [/System/Library/PrivateFrameworks/MediaCoreUI.framework/MediaCoreUI](DYLIBS/MediaCoreUI.md)
- [/System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience](DYLIBS/MediaExperience.md)
- [/System/Library/PrivateFrameworks/MediaFoundation.framework/MediaFoundation](DYLIBS/MediaFoundation.md)
- [/System/Library/PrivateFrameworks/MediaKit.framework/MediaKit](DYLIBS/MediaKit.md)
- [/System/Library/PrivateFrameworks/MediaLibraryCore.framework/MediaLibraryCore](DYLIBS/MediaLibraryCore.md)
- [/System/Library/PrivateFrameworks/MediaMLServices.framework/MediaMLServices](DYLIBS/MediaMLServices.md)
- [/System/Library/PrivateFrameworks/MediaMiningKit.framework/MediaMiningKit](DYLIBS/MediaMiningKit.md)
- [/System/Library/PrivateFrameworks/MediaPlatform.framework/MediaPlatform](DYLIBS/MediaPlatform.md)
- [/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore](DYLIBS/MediaPlaybackCore.md)
- [/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote](DYLIBS/MediaRemote.md)
- [/System/Library/PrivateFrameworks/MediaSafetyNet.framework/MediaSafetyNet](DYLIBS/MediaSafetyNet.md)
- [/System/Library/PrivateFrameworks/MediaServices.framework/MediaServices](DYLIBS/MediaServices.md)
- [/System/Library/PrivateFrameworks/MediaStream.framework/MediaStream](DYLIBS/MediaStream.md)
- [/System/Library/PrivateFrameworks/MenstrualAlgorithmsInternal.framework/MenstrualAlgorithmsInternal](DYLIBS/MenstrualAlgorithmsInternal.md)
- [/System/Library/PrivateFrameworks/MentalHealth.framework/MentalHealth](DYLIBS/MentalHealth.md)
- [/System/Library/PrivateFrameworks/MentalHealthDaemon.framework/MentalHealthDaemon](DYLIBS/MentalHealthDaemon.md)
- [/System/Library/PrivateFrameworks/MentalHealthUI.framework/MentalHealthUI](DYLIBS/MentalHealthUI.md)
- [/System/Library/PrivateFrameworks/Mercury.framework/Mercury](DYLIBS/Mercury.md)
- [/System/Library/PrivateFrameworks/Message.framework/Message](DYLIBS/Message.md)
- [/System/Library/PrivateFrameworks/MessageLegacy.framework/MailServices/IMAP.framework/IMAP](DYLIBS/IMAP.md)
- [/System/Library/PrivateFrameworks/MessageProtection.framework/MessageProtection](DYLIBS/MessageProtection.md)
- [/System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity](DYLIBS/MessageSecurity.md)
- [/System/Library/PrivateFrameworks/MessageSupport.framework/MessageSupport](DYLIBS/MessageSupport.md)
- [/System/Library/PrivateFrameworks/MessagesCloudSync.framework/MessagesCloudSync](DYLIBS/MessagesCloudSync.md)
- [/System/Library/PrivateFrameworks/MessagesSupport.framework/MessagesSupport](DYLIBS/MessagesSupport.md)
- [/System/Library/PrivateFrameworks/MetadataUtilities.framework/MetadataUtilities](DYLIBS/MetadataUtilities.md)
- [/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools](DYLIBS/MetalTools.md)
- [/System/Library/PrivateFrameworks/MetricKitCore.framework/MetricKitCore](DYLIBS/MetricKitCore.md)
- [/System/Library/PrivateFrameworks/MetricKitServices.framework/MetricKitServices](DYLIBS/MetricKitServices.md)
- [/System/Library/PrivateFrameworks/MetricKitSource.framework/MetricKitSource](DYLIBS/MetricKitSource.md)
- [/System/Library/PrivateFrameworks/MetricsFramework.framework/MetricsFramework](DYLIBS/MetricsFramework.md)
- [/System/Library/PrivateFrameworks/MetricsKit.framework/MetricsKit](DYLIBS/MetricsKit.md)
- [/System/Library/PrivateFrameworks/MigrationKit.framework/MigrationKit](DYLIBS/MigrationKit.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/MobileAccessoryUpdater](DYLIBS/MobileAccessoryUpdater.md)
- [/System/Library/PrivateFrameworks/MobileActivation.framework/MobileActivation](DYLIBS/MobileActivation.md)
- [/System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset](DYLIBS/MobileAsset.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup](DYLIBS/MobileBackup.md)
- [/System/Library/PrivateFrameworks/MobileBluetooth.framework/MobileBluetooth](DYLIBS/MobileBluetooth.md)
- [/System/Library/PrivateFrameworks/MobileIcons.framework/MobileIcons](DYLIBS/MobileIcons.md)
- [/System/Library/PrivateFrameworks/MobileIdentityServiceUI.framework/MobileIdentityServiceUI](DYLIBS/MobileIdentityServiceUI.md)
- [/System/Library/PrivateFrameworks/MobileInBoxUpdate.framework/MobileInBoxUpdate](DYLIBS/MobileInBoxUpdate.md)
- [/System/Library/PrivateFrameworks/MobileInstallation.framework/MobileInstallation](DYLIBS/MobileInstallation.md)
- [/System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag](DYLIBS/MobileKeyBag.md)
- [/System/Library/PrivateFrameworks/MobileMailUI.framework/MobileMailUI](DYLIBS/MobileMailUI.md)
- [/System/Library/PrivateFrameworks/MobileObliteration.framework/MobileObliteration](DYLIBS/MobileObliteration.md)
- [/System/Library/PrivateFrameworks/MobileSafari.framework/MobileSafari](DYLIBS/MobileSafari.md)
- [/System/Library/PrivateFrameworks/MobileSafari.framework/PlugIns/Safari.wkbundle/Safari](DYLIBS/Safari.md)
- [/System/Library/PrivateFrameworks/MobileSafariSwift.framework/MobileSafariSwift](DYLIBS/MobileSafariSwift.md)
- [/System/Library/PrivateFrameworks/MobileSafariUI.framework/MobileSafariUI](DYLIBS/MobileSafariUI.md)
- [/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/MobileSoftwareUpdate](DYLIBS/MobileSoftwareUpdate.md)
- [/System/Library/PrivateFrameworks/MobileSpotlightIndex.framework/MobileSpotlightIndex](DYLIBS/MobileSpotlightIndex.md)
- [/System/Library/PrivateFrameworks/MobileStoreDemoKit.framework/MobileStoreDemoKit](DYLIBS/MobileStoreDemoKit.md)
- [/System/Library/PrivateFrameworks/MobileStoreUI.framework/MobileStoreUI](DYLIBS/MobileStoreUI.md)
- [/System/Library/PrivateFrameworks/MobileTimer.framework/MobileTimer](DYLIBS/MobileTimer.md)
- [/System/Library/PrivateFrameworks/MobileTimerSupport.framework/MobileTimerSupport](DYLIBS/MobileTimerSupport.md)
- [/System/Library/PrivateFrameworks/MobileTimerUI.framework/MobileTimerUI](DYLIBS/MobileTimerUI.md)
- [/System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi](DYLIBS/MobileWiFi.md)
- [/System/Library/PrivateFrameworks/MomentsOnboardingAndSettings.framework/MomentsOnboardingAndSettings](DYLIBS/MomentsOnboardingAndSettings.md)
- [/System/Library/PrivateFrameworks/Montreal.framework/Montreal](DYLIBS/Montreal.md)
- [/System/Library/PrivateFrameworks/MotionSensorLogging.framework/MotionSensorLogging](DYLIBS/MotionSensorLogging.md)
- [/System/Library/PrivateFrameworks/MultitouchSupport.framework/MultitouchSupport](DYLIBS/MultitouchSupport.md)
- [/System/Library/PrivateFrameworks/MusicKitInternal.framework/MusicKitInternal](DYLIBS/MusicKitInternal.md)
- [/System/Library/PrivateFrameworks/MusicLibrary.framework/MusicLibrary](DYLIBS/MusicLibrary.md)
- [/System/Library/PrivateFrameworks/MusicUI.framework/MusicUI](DYLIBS/MusicUI.md)
- [/System/Library/PrivateFrameworks/NCLaunchStats.framework/NCLaunchStats](DYLIBS/NCLaunchStats.md)
- [/System/Library/PrivateFrameworks/NLP.framework/NLP](DYLIBS/NLP.md)
- [/System/Library/PrivateFrameworks/NPTKit.framework/NPTKit](DYLIBS/NPTKit.md)
- [/System/Library/PrivateFrameworks/NanoBackup.framework/NanoBackup](DYLIBS/NanoBackup.md)
- [/System/Library/PrivateFrameworks/NanoMailKitServer.framework/NanoMailKitServer](DYLIBS/NanoMailKitServer.md)
- [/System/Library/PrivateFrameworks/NanoMediaAPI.framework/NanoMediaAPI](DYLIBS/NanoMediaAPI.md)
- [/System/Library/PrivateFrameworks/NanoPassKit.framework/NanoPassKit](DYLIBS/NanoPassKit.md)
- [/System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync](DYLIBS/NanoPreferencesSync.md)
- [/System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry](DYLIBS/NanoRegistry.md)
- [/System/Library/PrivateFrameworks/NanoResourceGrabber.framework/NanoResourceGrabber](DYLIBS/NanoResourceGrabber.md)
- [/System/Library/PrivateFrameworks/NanoSystemSettings.framework/NanoSystemSettings](DYLIBS/NanoSystemSettings.md)
- [/System/Library/PrivateFrameworks/NanoTimeKit.framework/NanoTimeKit](DYLIBS/NanoTimeKit.md)
- [/System/Library/PrivateFrameworks/NanoTimeKitCompanion.framework/NanoTimeKitCompanion](DYLIBS/NanoTimeKitCompanion.md)
- [/System/Library/PrivateFrameworks/NanoUniverse.framework/NanoUniverse](DYLIBS/NanoUniverse.md)
- [/System/Library/PrivateFrameworks/Navigation.framework/Navigation](DYLIBS/Navigation.md)
- [/System/Library/PrivateFrameworks/NearField.framework/NearField](DYLIBS/NearField.md)
- [/System/Library/PrivateFrameworks/NearbySessions.framework/NearbySessions](DYLIBS/NearbySessions.md)
- [/System/Library/PrivateFrameworks/NetAppsUtilities.framework/NetAppsUtilities](DYLIBS/NetAppsUtilities.md)
- [/System/Library/PrivateFrameworks/NetAppsUtilitiesUI.framework/NetAppsUtilitiesUI](DYLIBS/NetAppsUtilitiesUI.md)
- [/System/Library/PrivateFrameworks/Netrb.framework/Netrb](DYLIBS/Netrb.md)
- [/System/Library/PrivateFrameworks/NetworkServiceProxy.framework/NetworkServiceProxy](DYLIBS/NetworkServiceProxy.md)
- [/System/Library/PrivateFrameworks/NetworkStatistics.framework/NetworkStatistics](DYLIBS/NetworkStatistics.md)
- [/System/Library/PrivateFrameworks/NeutrinoCore.framework/NeutrinoCore](DYLIBS/NeutrinoCore.md)
- [/System/Library/PrivateFrameworks/NeutrinoKit.framework/NeutrinoKit](DYLIBS/NeutrinoKit.md)
- [/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/NewDeviceOutreach](DYLIBS/NewDeviceOutreach.md)
- [/System/Library/PrivateFrameworks/NewDeviceOutreachUI.framework/NewDeviceOutreachUI](DYLIBS/NewDeviceOutreachUI.md)
- [/System/Library/PrivateFrameworks/NewsAds.framework/NewsAds](DYLIBS/NewsAds.md)
- [/System/Library/PrivateFrameworks/NewsAnalytics.framework/NewsAnalytics](DYLIBS/NewsAnalytics.md)
- [/System/Library/PrivateFrameworks/NewsAnalyticsUpload.framework/NewsAnalyticsUpload](DYLIBS/NewsAnalyticsUpload.md)
- [/System/Library/PrivateFrameworks/NewsArticles.framework/NewsArticles](DYLIBS/NewsArticles.md)
- [/System/Library/PrivateFrameworks/NewsCore.framework/NewsCore](DYLIBS/NewsCore.md)
- [/System/Library/PrivateFrameworks/NewsDaemon.framework/NewsDaemon](DYLIBS/NewsDaemon.md)
- [/System/Library/PrivateFrameworks/NewsEngagement.framework/NewsEngagement](DYLIBS/NewsEngagement.md)
- [/System/Library/PrivateFrameworks/NewsEngagementCollector.framework/NewsEngagementCollector](DYLIBS/NewsEngagementCollector.md)
- [/System/Library/PrivateFrameworks/NewsFeed.framework/NewsFeed](DYLIBS/NewsFeed.md)
- [/System/Library/PrivateFrameworks/NewsFoundation.framework/NewsFoundation](DYLIBS/NewsFoundation.md)
- [/System/Library/PrivateFrameworks/NewsKit.framework/NewsKit](DYLIBS/NewsKit.md)
- [/System/Library/PrivateFrameworks/NewsLiveActivitiesCore.framework/NewsLiveActivitiesCore](DYLIBS/NewsLiveActivitiesCore.md)
- [/System/Library/PrivateFrameworks/NewsPersonalization.framework/NewsPersonalization](DYLIBS/NewsPersonalization.md)
- [/System/Library/PrivateFrameworks/NewsServices.framework/NewsServices](DYLIBS/NewsServices.md)
- [/System/Library/PrivateFrameworks/NewsServicesInternal.framework/NewsServicesInternal](DYLIBS/NewsServicesInternal.md)
- [/System/Library/PrivateFrameworks/NewsSubscription.framework/NewsSubscription](DYLIBS/NewsSubscription.md)
- [/System/Library/PrivateFrameworks/NewsToday.framework/NewsToday](DYLIBS/NewsToday.md)
- [/System/Library/PrivateFrameworks/NewsTransport.framework/NewsTransport](DYLIBS/NewsTransport.md)
- [/System/Library/PrivateFrameworks/NewsUI.framework/NewsUI](DYLIBS/NewsUI.md)
- [/System/Library/PrivateFrameworks/NewsUI2.framework/NewsUI2](DYLIBS/NewsUI2.md)
- [/System/Library/PrivateFrameworks/NewsURLBucket.framework/NewsURLBucket](DYLIBS/NewsURLBucket.md)
- [/System/Library/PrivateFrameworks/NightingaleTraining.framework/NightingaleTraining](DYLIBS/NightingaleTraining.md)
- [/System/Library/PrivateFrameworks/Notes.framework/Notes](DYLIBS/Notes.md)
- [/System/Library/PrivateFrameworks/NotesAnalytics.framework/NotesAnalytics](DYLIBS/NotesAnalytics.md)
- [/System/Library/PrivateFrameworks/NotesEditor.framework/NotesEditor](DYLIBS/NotesEditor.md)
- [/System/Library/PrivateFrameworks/NotesShared.framework/NotesShared](DYLIBS/NotesShared.md)
- [/System/Library/PrivateFrameworks/NotesSupport.framework/NotesSupport](DYLIBS/NotesSupport.md)
- [/System/Library/PrivateFrameworks/NotesUI.framework/NotesUI](DYLIBS/NotesUI.md)
- [/System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics](DYLIBS/OSAnalytics.md)
- [/System/Library/PrivateFrameworks/OSAnalyticsPrivate.framework/OSAnalyticsPrivate](DYLIBS/OSAnalyticsPrivate.md)
- [/System/Library/PrivateFrameworks/OSIntelligence.framework/OSIntelligence](DYLIBS/OSIntelligence.md)
- [/System/Library/PrivateFrameworks/OTSVG.framework/OTSVG](DYLIBS/OTSVG.md)
- [/System/Library/PrivateFrameworks/ObjectUnderstanding.framework/ObjectUnderstanding](DYLIBS/ObjectUnderstanding.md)
- [/System/Library/PrivateFrameworks/OfficeImport.framework/OfficeImport](DYLIBS/OfficeImport.md)
- [/System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit](DYLIBS/OnBoardingKit.md)
- [/System/Library/PrivateFrameworks/PBBridgeSupport.framework/PBBridgeSupport](DYLIBS/PBBridgeSupport.md)
- [/System/Library/PrivateFrameworks/PairedSync.framework/PairedSync](DYLIBS/PairedSync.md)
- [/System/Library/PrivateFrameworks/PairingProximity.framework/PairingProximity](DYLIBS/PairingProximity.md)
- [/System/Library/PrivateFrameworks/PaperBoardUI.framework/PaperBoardUI](DYLIBS/PaperBoardUI.md)
- [/System/Library/PrivateFrameworks/PaperKit.framework/PaperKit](DYLIBS/PaperKit.md)
- [/System/Library/PrivateFrameworks/ParsecModel.framework/ParsecModel](DYLIBS/ParsecModel.md)
- [/System/Library/PrivateFrameworks/ParsecSubscriptionServiceSupport.framework/ParsecSubscriptionServiceSupport](DYLIBS/ParsecSubscriptionServiceSupport.md)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore](DYLIBS/PassKitCore.md)
- [/System/Library/PrivateFrameworks/PassKitCore_SoftLinking.framework/PassKitCore_SoftLinking](DYLIBS/PassKitCore_SoftLinking.md)
- [/System/Library/PrivateFrameworks/PassKitUI.framework/PassKitUI](DYLIBS/PassKitUI.md)
- [/System/Library/PrivateFrameworks/PassKitUIFoundation.framework/PassKitUIFoundation](DYLIBS/PassKitUIFoundation.md)
- [/System/Library/PrivateFrameworks/PasswordManagerUI.framework/PasswordManagerUI](DYLIBS/PasswordManagerUI.md)
- [/System/Library/PrivateFrameworks/Pasteboard.framework/Pasteboard](DYLIBS/Pasteboard.md)
- [/System/Library/PrivateFrameworks/PaymentUIBase.framework/PaymentUIBase](DYLIBS/PaymentUIBase.md)
- [/System/Library/PrivateFrameworks/Pegasus.framework/Pegasus](DYLIBS/Pegasus.md)
- [/System/Library/PrivateFrameworks/PegasusAPI.framework/PegasusAPI](DYLIBS/PegasusAPI.md)
- [/System/Library/PrivateFrameworks/PegasusConfiguration.framework/PegasusConfiguration](DYLIBS/PegasusConfiguration.md)
- [/System/Library/PrivateFrameworks/PegasusKit.framework/PegasusKit](DYLIBS/PegasusKit.md)
- [/System/Library/PrivateFrameworks/PegasusPersistence.framework/PegasusPersistence](DYLIBS/PegasusPersistence.md)
- [/System/Library/PrivateFrameworks/PencilPairingUI.framework/PencilPairingUI](DYLIBS/PencilPairingUI.md)
- [/System/Library/PrivateFrameworks/People.framework/People](DYLIBS/People.md)
- [/System/Library/PrivateFrameworks/PeopleSuggester.framework/PeopleSuggester](DYLIBS/PeopleSuggester.md)
- [/System/Library/PrivateFrameworks/PeopleUIInternal.framework/PeopleUIInternal](DYLIBS/PeopleUIInternal.md)
- [/System/Library/PrivateFrameworks/PerfPowerMetricMonitor.framework/PerfPowerMetricMonitor](DYLIBS/PerfPowerMetricMonitor.md)
- [/System/Library/PrivateFrameworks/PerfPowerServicesMetadata.framework/PerfPowerServicesMetadata](DYLIBS/PerfPowerServicesMetadata.md)
- [/System/Library/PrivateFrameworks/PerfPowerServicesReader.framework/PerfPowerServicesReader](DYLIBS/PerfPowerServicesReader.md)
- [/System/Library/PrivateFrameworks/PerformanceControlKit.framework/PerformanceControlKit](DYLIBS/PerformanceControlKit.md)
- [/System/Library/PrivateFrameworks/PeridotDepth.framework/PeridotDepth](DYLIBS/PeridotDepth.md)
- [/System/Library/PrivateFrameworks/PersistentConnection.framework/PersistentConnection](DYLIBS/PersistentConnection.md)
- [/System/Library/PrivateFrameworks/PersonaUI.framework/PersonaUI](DYLIBS/PersonaUI.md)
- [/System/Library/PrivateFrameworks/PersonalAudio.framework/PersonalAudio](DYLIBS/PersonalAudio.md)
- [/System/Library/PrivateFrameworks/PersonalIntelligenceCore.framework/PersonalIntelligenceCore](DYLIBS/PersonalIntelligenceCore.md)
- [/System/Library/PrivateFrameworks/PersonalizationPortrait.framework/PersonalizationPortrait](DYLIBS/PersonalizationPortrait.md)
- [/System/Library/PrivateFrameworks/PersonalizationPortraitInternals.framework/PersonalizationPortraitInternals](DYLIBS/PersonalizationPortraitInternals.md)
- [/System/Library/PrivateFrameworks/PhoneSnippetUI.framework/PhoneSnippetUI](DYLIBS/PhoneSnippetUI.md)
- [/System/Library/PrivateFrameworks/PhotoAnalysis.framework/PhotoAnalysis](DYLIBS/PhotoAnalysis.md)
- [/System/Library/PrivateFrameworks/PhotoFoundation.framework/PhotoFoundation](DYLIBS/PhotoFoundation.md)
- [/System/Library/PrivateFrameworks/PhotoImaging.framework/PhotoImaging](DYLIBS/PhotoImaging.md)
- [/System/Library/PrivateFrameworks/PhotoLibrary.framework/PhotoLibrary](DYLIBS/PhotoLibrary.md)
- [/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/PhotoLibraryServices](DYLIBS/PhotoLibraryServices.md)
- [/System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/PhotoLibraryServicesCore](DYLIBS/PhotoLibraryServicesCore.md)
- [/System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats](DYLIBS/PhotosFormats.md)
- [/System/Library/PrivateFrameworks/PhotosGraph.framework/PhotosGraph](DYLIBS/PhotosGraph.md)
- [/System/Library/PrivateFrameworks/PhotosImagingFoundation.framework/PhotosImagingFoundation](DYLIBS/PhotosImagingFoundation.md)
- [/System/Library/PrivateFrameworks/PhotosIntelligence.framework/PhotosIntelligence](DYLIBS/PhotosIntelligence.md)
- [/System/Library/PrivateFrameworks/PhotosPlayer.framework/PhotosPlayer](DYLIBS/PhotosPlayer.md)
- [/System/Library/PrivateFrameworks/PhotosUICore.framework/PhotosUICore](DYLIBS/PhotosUICore.md)
- [/System/Library/PrivateFrameworks/PhotosUIEdit.framework/PhotosUIEdit](DYLIBS/PhotosUIEdit.md)
- [/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PhotosUIPrivate](DYLIBS/PhotosUIPrivate.md)
- [/System/Library/PrivateFrameworks/PlacesKit.framework/PlacesKit](DYLIBS/PlacesKit.md)
- [/System/Library/PrivateFrameworks/PlatformSSO.framework/PlatformSSO](DYLIBS/PlatformSSO.md)
- [/System/Library/PrivateFrameworks/PlatterKit.framework/PlatterKit](DYLIBS/PlatterKit.md)
- [/System/Library/PrivateFrameworks/PlugInKit.framework/PlugInKit](DYLIBS/PlugInKit.md)
- [/System/Library/PrivateFrameworks/PodcastsFoundation.framework/PodcastsFoundation](DYLIBS/PodcastsFoundation.md)
- [/System/Library/PrivateFrameworks/PodcastsKit.framework/PodcastsKit](DYLIBS/PodcastsKit.md)
- [/System/Library/PrivateFrameworks/PodcastsUI.framework/PodcastsUI](DYLIBS/PodcastsUI.md)
- [/System/Library/PrivateFrameworks/PointerUIServices.framework/PointerUIServices](DYLIBS/PointerUIServices.md)
- [/System/Library/PrivateFrameworks/PoirotSQLite.framework/PoirotSQLite](DYLIBS/PoirotSQLite.md)
- [/System/Library/PrivateFrameworks/PoirotSchematizer.framework/PoirotSchematizer](DYLIBS/PoirotSchematizer.md)
- [/System/Library/PrivateFrameworks/Portrait.framework/Portrait](DYLIBS/Portrait.md)
- [/System/Library/PrivateFrameworks/PosterBoard.framework/PosterBoard](DYLIBS/PosterBoard.md)
- [/System/Library/PrivateFrameworks/PosterBoardServices.framework/PosterBoardServices](DYLIBS/PosterBoardServices.md)
- [/System/Library/PrivateFrameworks/PosterKit.framework/PosterKit](DYLIBS/PosterKit.md)
- [/System/Library/PrivateFrameworks/PowerLog.framework/PowerLog](DYLIBS/PowerLog.md)
- [/System/Library/PrivateFrameworks/PowerUI.framework/PowerUI](DYLIBS/PowerUI.md)
- [/System/Library/PrivateFrameworks/PowerlogAccounting.framework/PowerlogAccounting](DYLIBS/PowerlogAccounting.md)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore](DYLIBS/PowerlogCore.md)
- [/System/Library/PrivateFrameworks/PowerlogFullOperators.framework/PowerlogFullOperators](DYLIBS/PowerlogFullOperators.md)
- [/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators](DYLIBS/PowerlogHelperdOperators.md)
- [/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators](DYLIBS/PowerlogLiteOperators.md)
- [/System/Library/PrivateFrameworks/Preferences.framework/Preferences](DYLIBS/Preferences.md)
- [/System/Library/PrivateFrameworks/PreferencesUI.framework/PreferencesUI](DYLIBS/PreferencesUI.md)
- [/System/Library/PrivateFrameworks/PreviewShellKit.framework/PreviewShellKit](DYLIBS/PreviewShellKit.md)
- [/System/Library/PrivateFrameworks/PrintKit.framework/PrintKit](DYLIBS/PrintKit.md)
- [/System/Library/PrivateFrameworks/PrintKitUI.framework/PrintKitUI](DYLIBS/PrintKitUI.md)
- [/System/Library/PrivateFrameworks/PrivacyAccounting.framework/PrivacyAccounting](DYLIBS/PrivacyAccounting.md)
- [/System/Library/PrivateFrameworks/PrivacyDisclosureCore.framework/PrivacyDisclosureCore](DYLIBS/PrivacyDisclosureCore.md)
- [/System/Library/PrivateFrameworks/PrivacyDisclosureUI.framework/PrivacyDisclosureUI](DYLIBS/PrivacyDisclosureUI.md)
- [/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PrivateFederatedLearning](DYLIBS/PrivateFederatedLearning.md)
- [/System/Library/PrivateFrameworks/ProVideo.framework/ProVideo](DYLIBS/ProVideo.md)
- [/System/Library/PrivateFrameworks/ProactiveBlendingLayer_iOS.framework/ProactiveBlendingLayer_iOS](DYLIBS/ProactiveBlendingLayer_iOS.md)
- [/System/Library/PrivateFrameworks/ProactiveCDNDownloader.framework/ProactiveCDNDownloader](DYLIBS/ProactiveCDNDownloader.md)
- [/System/Library/PrivateFrameworks/ProactiveContextClient.framework/ProactiveContextClient](DYLIBS/ProactiveContextClient.md)
- [/System/Library/PrivateFrameworks/ProactiveEventTracker.framework/ProactiveEventTracker](DYLIBS/ProactiveEventTracker.md)
- [/System/Library/PrivateFrameworks/ProactiveExperiments.framework/ProactiveExperiments](DYLIBS/ProactiveExperiments.md)
- [/System/Library/PrivateFrameworks/ProactiveExperimentsInternals.framework/ProactiveExperimentsInternals](DYLIBS/ProactiveExperimentsInternals.md)
- [/System/Library/PrivateFrameworks/ProactiveHarvesting.framework/ProactiveHarvesting](DYLIBS/ProactiveHarvesting.md)
- [/System/Library/PrivateFrameworks/ProactiveInputPredictions.framework/ProactiveInputPredictions](DYLIBS/ProactiveInputPredictions.md)
- [/System/Library/PrivateFrameworks/ProactiveInputPredictionsInternals.framework/ProactiveInputPredictionsInternals](DYLIBS/ProactiveInputPredictionsInternals.md)
- [/System/Library/PrivateFrameworks/ProactiveML.framework/ProactiveML](DYLIBS/ProactiveML.md)
- [/System/Library/PrivateFrameworks/ProactiveMagicalMoments.framework/ProactiveMagicalMoments](DYLIBS/ProactiveMagicalMoments.md)
- [/System/Library/PrivateFrameworks/ProactiveSuggestionClientModel.framework/ProactiveSuggestionClientModel](DYLIBS/ProactiveSuggestionClientModel.md)
- [/System/Library/PrivateFrameworks/ProactiveSupport.framework/ProactiveSupport](DYLIBS/ProactiveSupport.md)
- [/System/Library/PrivateFrameworks/ProductKit.framework/ProductKit](DYLIBS/ProductKit.md)
- [/System/Library/PrivateFrameworks/ProgressUI.framework/ProgressUI](DYLIBS/ProgressUI.md)
- [/System/Library/PrivateFrameworks/PromotedContent.framework/PromotedContent](DYLIBS/PromotedContent.md)
- [/System/Library/PrivateFrameworks/PromotedContentPrediction.framework/PromotedContentPrediction](DYLIBS/PromotedContentPrediction.md)
- [/System/Library/PrivateFrameworks/PromotedContentProxy.framework/PromotedContentProxy](DYLIBS/PromotedContentProxy.md)
- [/System/Library/PrivateFrameworks/PromotedContentSupport.framework/PromotedContentSupport](DYLIBS/PromotedContentSupport.md)
- [/System/Library/PrivateFrameworks/PromotedContentUI.framework/PromotedContentUI](DYLIBS/PromotedContentUI.md)
- [/System/Library/PrivateFrameworks/ProofReader.framework/ProofReader](DYLIBS/ProofReader.md)
- [/System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/ProtectedCloudStorage](DYLIBS/ProtectedCloudStorage.md)
- [/System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer](DYLIBS/ProtocolBuffer.md)
- [/System/Library/PrivateFrameworks/PrototypeTools.framework/PrototypeTools](DYLIBS/PrototypeTools.md)
- [/System/Library/PrivateFrameworks/PrototypeToolsUI.framework/PrototypeToolsUI](DYLIBS/PrototypeToolsUI.md)
- [/System/Library/PrivateFrameworks/Proximity.framework/Proximity](DYLIBS/Proximity.md)
- [/System/Library/PrivateFrameworks/ProximityAppleIDSetup.framework/ProximityAppleIDSetup](DYLIBS/ProximityAppleIDSetup.md)
- [/System/Library/PrivateFrameworks/ProximityAppleIDSetupUI.framework/ProximityAppleIDSetupUI](DYLIBS/ProximityAppleIDSetupUI.md)
- [/System/Library/PrivateFrameworks/Quagga.framework/Quagga](DYLIBS/Quagga.md)
- [/System/Library/PrivateFrameworks/QueryParser.framework/QueryParser](DYLIBS/QueryParser.md)
- [/System/Library/PrivateFrameworks/QueryUnderstanding.framework/QueryUnderstanding](DYLIBS/QueryUnderstanding.md)
- [/System/Library/PrivateFrameworks/QuickLookSupport.framework/QuickLookSupport](DYLIBS/QuickLookSupport.md)
- [/System/Library/PrivateFrameworks/QuickLookThumbnailingDaemon.framework/QuickLookThumbnailingDaemon](DYLIBS/QuickLookThumbnailingDaemon.md)
- [/System/Library/PrivateFrameworks/RTCReporting.framework/RTCReporting](DYLIBS/RTCReporting.md)
- [/System/Library/PrivateFrameworks/RTTUtilities.framework/RTTUtilities](DYLIBS/RTTUtilities.md)
- [/System/Library/PrivateFrameworks/Radio.framework/Radio](DYLIBS/Radio.md)
- [/System/Library/PrivateFrameworks/Rapport.framework/Rapport](DYLIBS/Rapport.md)
- [/System/Library/PrivateFrameworks/RealityFusion.framework/RealityFusion](DYLIBS/RealityFusion.md)
- [/System/Library/PrivateFrameworks/Recap.framework/Recap](DYLIBS/Recap.md)
- [/System/Library/PrivateFrameworks/RecapPerformanceTesting.framework/RecapPerformanceTesting](DYLIBS/RecapPerformanceTesting.md)
- [/System/Library/PrivateFrameworks/Recon3D.framework/Recon3D](DYLIBS/Recon3D.md)
- [/System/Library/PrivateFrameworks/ReflectionInternal.framework/ReflectionInternal](DYLIBS/ReflectionInternal.md)
- [/System/Library/PrivateFrameworks/RegulatoryDomain.framework/RegulatoryDomain](DYLIBS/RegulatoryDomain.md)
- [/System/Library/PrivateFrameworks/RelevanceEngine.framework/RelevanceEngine](DYLIBS/RelevanceEngine.md)
- [/System/Library/PrivateFrameworks/ReminderKit.framework/ReminderKit](DYLIBS/ReminderKit.md)
- [/System/Library/PrivateFrameworks/ReminderKitInternal.framework/ReminderKitInternal](DYLIBS/ReminderKitInternal.md)
- [/System/Library/PrivateFrameworks/ReminderKitUI.framework/ReminderKitUI](DYLIBS/ReminderKitUI.md)
- [/System/Library/PrivateFrameworks/RemindersIntentsFramework.framework/RemindersIntentsFramework](DYLIBS/RemindersIntentsFramework.md)
- [/System/Library/PrivateFrameworks/RemindersUICore.framework/RemindersUICore](DYLIBS/RemindersUICore.md)
- [/System/Library/PrivateFrameworks/RemoteConfiguration.framework/RemoteConfiguration](DYLIBS/RemoteConfiguration.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/RemoteManagement](DYLIBS/RemoteManagement.md)
- [/System/Library/PrivateFrameworks/RemoteManagementModel.framework/RemoteManagementModel](DYLIBS/RemoteManagementModel.md)
- [/System/Library/PrivateFrameworks/RemotePairingDevice.framework/RemotePairingDevice](DYLIBS/RemotePairingDevice.md)
- [/System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/RemoteServiceDiscovery](DYLIBS/RemoteServiceDiscovery.md)
- [/System/Library/PrivateFrameworks/RemoteUI.framework/RemoteUI](DYLIBS/RemoteUI.md)
- [/System/Library/PrivateFrameworks/RemoteXPC.framework/RemoteXPC](DYLIBS/RemoteXPC.md)
- [/System/Library/PrivateFrameworks/RenderBox.framework/RenderBox](DYLIBS/RenderBox.md)
- [/System/Library/PrivateFrameworks/ReportingPlugin.framework/ReportingPlugin](DYLIBS/ReportingPlugin.md)
- [/System/Library/PrivateFrameworks/RequestDispatcherBridges.framework/RequestDispatcherBridges](DYLIBS/RequestDispatcherBridges.md)
- [/System/Library/PrivateFrameworks/RespiratoryHealth.framework/RespiratoryHealth](DYLIBS/RespiratoryHealth.md)
- [/System/Library/PrivateFrameworks/RespiratoryHealthDaemon.framework/RespiratoryHealthDaemon](DYLIBS/RespiratoryHealthDaemon.md)
- [/System/Library/PrivateFrameworks/RespiratoryHealthUI.framework/RespiratoryHealthUI](DYLIBS/RespiratoryHealthUI.md)
- [/System/Library/PrivateFrameworks/ResponseKit.framework/ResponseKit](DYLIBS/ResponseKit.md)
- [/System/Library/PrivateFrameworks/RoomScanCore.framework/RoomScanCore](DYLIBS/RoomScanCore.md)
- [/System/Library/PrivateFrameworks/RunningBoard.framework/RunningBoard](DYLIBS/RunningBoard.md)
- [/System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices](DYLIBS/RunningBoardServices.md)
- [/System/Library/PrivateFrameworks/RuntimeInternal.framework/RuntimeInternal](DYLIBS/RuntimeInternal.md)
- [/System/Library/PrivateFrameworks/SAML.framework/SAML](DYLIBS/SAML.md)
- [/System/Library/PrivateFrameworks/SEService.framework/SEService](DYLIBS/SEService.md)
- [/System/Library/PrivateFrameworks/SFSymbols.framework/SFSymbols](DYLIBS/SFSymbols.md)
- [/System/Library/PrivateFrameworks/SILManager.framework/SILManager](DYLIBS/SILManager.md)
- [/System/Library/PrivateFrameworks/SIMSetupSupport.framework/SIMSetupSupport](DYLIBS/SIMSetupSupport.md)
- [/System/Library/PrivateFrameworks/SIMToolkitUI.framework/SIMToolkitUI](DYLIBS/SIMToolkitUI.md)
- [/System/Library/PrivateFrameworks/SPFinder.framework/SPFinder](DYLIBS/SPFinder.md)
- [/System/Library/PrivateFrameworks/SPOwner.framework/SPOwner](DYLIBS/SPOwner.md)
- [/System/Library/PrivateFrameworks/SPShared.framework/SPShared](DYLIBS/SPShared.md)
- [/System/Library/PrivateFrameworks/SafariCore.framework/SafariCore](DYLIBS/SafariCore.md)
- [/System/Library/PrivateFrameworks/SafariFoundation.framework/SafariFoundation](DYLIBS/SafariFoundation.md)
- [/System/Library/PrivateFrameworks/SafariSafeBrowsing.framework/SafariSafeBrowsing](DYLIBS/SafariSafeBrowsing.md)
- [/System/Library/PrivateFrameworks/SafariShared.framework/SafariShared](DYLIBS/SafariShared.md)
- [/System/Library/PrivateFrameworks/SafariSharedUI.framework/SafariSharedUI](DYLIBS/SafariSharedUI.md)
- [/System/Library/PrivateFrameworks/SafetyAlerts.framework/SafetyAlerts](DYLIBS/SafetyAlerts.md)
- [/System/Library/PrivateFrameworks/SafetyMonitor.framework/SafetyMonitor](DYLIBS/SafetyMonitor.md)
- [/System/Library/PrivateFrameworks/SampleAnalysis.framework/SampleAnalysis](DYLIBS/SampleAnalysis.md)
- [/System/Library/PrivateFrameworks/SceneIntelligence.framework/SceneIntelligence](DYLIBS/SceneIntelligence.md)
- [/System/Library/PrivateFrameworks/ScreenReaderOutput.framework/ScreenReaderOutput](DYLIBS/ScreenReaderOutput.md)
- [/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore](DYLIBS/ScreenTimeCore.md)
- [/System/Library/PrivateFrameworks/ScreenTimeSettingsUI.framework/ScreenTimeSettingsUI](DYLIBS/ScreenTimeSettingsUI.md)
- [/System/Library/PrivateFrameworks/ScreenTimeUI.framework/ScreenTimeUI](DYLIBS/ScreenTimeUI.md)
- [/System/Library/PrivateFrameworks/ScreenTimeUICore.framework/ScreenTimeUICore](DYLIBS/ScreenTimeUICore.md)
- [/System/Library/PrivateFrameworks/ScreenshotServices.framework/ScreenshotServices](DYLIBS/ScreenshotServices.md)
- [/System/Library/PrivateFrameworks/Search.framework/Search](DYLIBS/Search.md)
- [/System/Library/PrivateFrameworks/SearchAds.framework/SearchAds](DYLIBS/SearchAds.md)
- [/System/Library/PrivateFrameworks/SearchFoundation.framework/SearchFoundation](DYLIBS/SearchFoundation.md)
- [/System/Library/PrivateFrameworks/SearchUI.framework/SearchUI](DYLIBS/SearchUI.md)
- [/System/Library/PrivateFrameworks/SecurityFoundation.framework/SecurityFoundation](DYLIBS/SecurityFoundation.md)
- [/System/Library/PrivateFrameworks/Seeding.framework/Seeding](DYLIBS/Seeding.md)
- [/System/Library/PrivateFrameworks/SensingAlgsService.framework/SensingAlgsService](DYLIBS/SensingAlgsService.md)
- [/System/Library/PrivateFrameworks/SensitiveContentAnalysisML.framework/SensitiveContentAnalysisML](DYLIBS/SensitiveContentAnalysisML.md)
- [/System/Library/PrivateFrameworks/SensorKitHelper.framework/SensorKitHelper](DYLIBS/SensorKitHelper.md)
- [/System/Library/PrivateFrameworks/SentencePiece.framework/SentencePiece](DYLIBS/SentencePiece.md)
- [/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts](DYLIBS/SeparationAlerts.md)
- [/System/Library/PrivateFrameworks/ServiceExtensions.framework/ServiceExtensions](DYLIBS/ServiceExtensions.md)
- [/System/Library/PrivateFrameworks/ServiceExtensionsCore.framework/ServiceExtensionsCore](DYLIBS/ServiceExtensionsCore.md)
- [/System/Library/PrivateFrameworks/ServiceManagement.framework/ServiceManagement](DYLIBS/ServiceManagement.md)
- [/System/Library/PrivateFrameworks/SessionCore.framework/SessionCore](DYLIBS/SessionCore.md)
- [/System/Library/PrivateFrameworks/SessionFoundation.framework/SessionFoundation](DYLIBS/SessionFoundation.md)
- [/System/Library/PrivateFrameworks/SessionPushNotifications.framework/SessionPushNotifications](DYLIBS/SessionPushNotifications.md)
- [/System/Library/PrivateFrameworks/SessionSyncEngine.framework/SessionSyncEngine](DYLIBS/SessionSyncEngine.md)
- [/System/Library/PrivateFrameworks/Settings.framework/Settings](DYLIBS/Settings.md)
- [/System/Library/PrivateFrameworks/Settings/DisplayAndBrightnessSettings.framework/DisplayAndBrightnessSettings](DYLIBS/DisplayAndBrightnessSettings.md)
- [/System/Library/PrivateFrameworks/Settings/GeneralSettingsUI.framework/GeneralSettingsUI](DYLIBS/GeneralSettingsUI.md)
- [/System/Library/PrivateFrameworks/Settings/PrivacySettingsUI.framework/PrivacySettingsUI](DYLIBS/PrivacySettingsUI.md)
- [/System/Library/PrivateFrameworks/Settings/SettingsUIKitPrivate.framework/SettingsUIKitPrivate](DYLIBS/SettingsUIKitPrivate.md)
- [/System/Library/PrivateFrameworks/Settings/SoundsAndHapticsSettings.framework/SoundsAndHapticsSettings](DYLIBS/SoundsAndHapticsSettings.md)
- [/System/Library/PrivateFrameworks/SettingsCellular.framework/SettingsCellular](DYLIBS/SettingsCellular.md)
- [/System/Library/PrivateFrameworks/SettingsCellularUI.framework/SettingsCellularUI](DYLIBS/SettingsCellularUI.md)
- [/System/Library/PrivateFrameworks/SettingsFoundation.framework/SettingsFoundation](DYLIBS/SettingsFoundation.md)
- [/System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant](DYLIBS/SetupAssistant.md)
- [/System/Library/PrivateFrameworks/SetupAssistantUI.framework/SetupAssistantUI](DYLIBS/SetupAssistantUI.md)
- [/System/Library/PrivateFrameworks/SeymourClient.framework/SeymourClient](DYLIBS/SeymourClient.md)
- [/System/Library/PrivateFrameworks/SeymourCore.framework/SeymourCore](DYLIBS/SeymourCore.md)
- [/System/Library/PrivateFrameworks/SeymourMedia.framework/SeymourMedia](DYLIBS/SeymourMedia.md)
- [/System/Library/PrivateFrameworks/SeymourServices.framework/SeymourServices](DYLIBS/SeymourServices.md)
- [/System/Library/PrivateFrameworks/SeymourUI.framework/SeymourUI](DYLIBS/SeymourUI.md)
- [/System/Library/PrivateFrameworks/ShareSheet.framework/ShareSheet](DYLIBS/ShareSheet.md)
- [/System/Library/PrivateFrameworks/SharedWebCredentials.framework/SharedWebCredentials](DYLIBS/SharedWebCredentials.md)
- [/System/Library/PrivateFrameworks/Sharing.framework/Sharing](DYLIBS/Sharing.md)
- [/System/Library/PrivateFrameworks/SharingUI.framework/SharingUI](DYLIBS/SharingUI.md)
- [/System/Library/PrivateFrameworks/SignpostCollection.framework/SignpostCollection](DYLIBS/SignpostCollection.md)
- [/System/Library/PrivateFrameworks/SignpostMetrics.framework/SignpostMetrics](DYLIBS/SignpostMetrics.md)
- [/System/Library/PrivateFrameworks/SignpostNotification.framework/SignpostNotification](DYLIBS/SignpostNotification.md)
- [/System/Library/PrivateFrameworks/SignpostSupport.framework/SignpostSupport](DYLIBS/SignpostSupport.md)
- [/System/Library/PrivateFrameworks/Silex.framework/Silex](DYLIBS/Silex.md)
- [/System/Library/PrivateFrameworks/SilexWeb.framework/SilexWeb](DYLIBS/SilexWeb.md)
- [/System/Library/PrivateFrameworks/SiriActivation.framework/SiriActivation](DYLIBS/SiriActivation.md)
- [/System/Library/PrivateFrameworks/SiriAnalytics.framework/SiriAnalytics](DYLIBS/SiriAnalytics.md)
- [/System/Library/PrivateFrameworks/SiriAppLaunchIntents.framework/SiriAppLaunchIntents](DYLIBS/SiriAppLaunchIntents.md)
- [/System/Library/PrivateFrameworks/SiriAudioInternal.framework/SiriAudioInternal](DYLIBS/SiriAudioInternal.md)
- [/System/Library/PrivateFrameworks/SiriAudioSupport.framework/SiriAudioSupport](DYLIBS/SiriAudioSupport.md)
- [/System/Library/PrivateFrameworks/SiriCam.framework/SiriCam](DYLIBS/SiriCam.md)
- [/System/Library/PrivateFrameworks/SiriCore.framework/SiriCore](DYLIBS/SiriCore.md)
- [/System/Library/PrivateFrameworks/SiriCorrections.framework/SiriCorrections](DYLIBS/SiriCorrections.md)
- [/System/Library/PrivateFrameworks/SiriCrossDeviceArbitration.framework/SiriCrossDeviceArbitration](DYLIBS/SiriCrossDeviceArbitration.md)
- [/System/Library/PrivateFrameworks/SiriDialogEngine.framework/SiriDialogEngine](DYLIBS/SiriDialogEngine.md)
- [/System/Library/PrivateFrameworks/SiriEntityMatcher.framework/SiriEntityMatcher](DYLIBS/SiriEntityMatcher.md)
- [/System/Library/PrivateFrameworks/SiriFindMy.framework/SiriFindMy](DYLIBS/SiriFindMy.md)
- [/System/Library/PrivateFrameworks/SiriFlowEnvironment.framework/SiriFlowEnvironment](DYLIBS/SiriFlowEnvironment.md)
- [/System/Library/PrivateFrameworks/SiriGeo.framework/SiriGeo](DYLIBS/SiriGeo.md)
- [/System/Library/PrivateFrameworks/SiriInCall.framework/SiriInCall](DYLIBS/SiriInCall.md)
- [/System/Library/PrivateFrameworks/SiriInference.framework/SiriInference](DYLIBS/SiriInference.md)
- [/System/Library/PrivateFrameworks/SiriInferenceIntents.framework/SiriInferenceIntents](DYLIBS/SiriInferenceIntents.md)
- [/System/Library/PrivateFrameworks/SiriInformationSearch.framework/SiriInformationSearch](DYLIBS/SiriInformationSearch.md)
- [/System/Library/PrivateFrameworks/SiriInformationTypes.framework/SiriInformationTypes](DYLIBS/SiriInformationTypes.md)
- [/System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation](DYLIBS/SiriInstrumentation.md)
- [/System/Library/PrivateFrameworks/SiriKitFlow.framework/SiriKitFlow](DYLIBS/SiriKitFlow.md)
- [/System/Library/PrivateFrameworks/SiriKitInvocation.framework/SiriKitInvocation](DYLIBS/SiriKitInvocation.md)
- [/System/Library/PrivateFrameworks/SiriKitRuntime.framework/SiriKitRuntime](DYLIBS/SiriKitRuntime.md)
- [/System/Library/PrivateFrameworks/SiriLiminal.framework/SiriLiminal](DYLIBS/SiriLiminal.md)
- [/System/Library/PrivateFrameworks/SiriMASPFLTraining.framework/SiriMASPFLTraining](DYLIBS/SiriMASPFLTraining.md)
- [/System/Library/PrivateFrameworks/SiriMailInternal.framework/SiriMailInternal](DYLIBS/SiriMailInternal.md)
- [/System/Library/PrivateFrameworks/SiriMessageBus.framework/SiriMessageBus](DYLIBS/SiriMessageBus.md)
- [/System/Library/PrivateFrameworks/SiriMessageTypes.framework/SiriMessageTypes](DYLIBS/SiriMessageTypes.md)
- [/System/Library/PrivateFrameworks/SiriMessagesFlow.framework/SiriMessagesFlow](DYLIBS/SiriMessagesFlow.md)
- [/System/Library/PrivateFrameworks/SiriNLUOverrides.framework/SiriNLUOverrides](DYLIBS/SiriNLUOverrides.md)
- [/System/Library/PrivateFrameworks/SiriNLUTypes.framework/SiriNLUTypes](DYLIBS/SiriNLUTypes.md)
- [/System/Library/PrivateFrameworks/SiriNaturalLanguageParsing.framework/SiriNaturalLanguageParsing](DYLIBS/SiriNaturalLanguageParsing.md)
- [/System/Library/PrivateFrameworks/SiriObservation.framework/SiriObservation](DYLIBS/SiriObservation.md)
- [/System/Library/PrivateFrameworks/SiriOntology.framework/SiriOntology](DYLIBS/SiriOntology.md)
- [/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/SiriPlaybackControlIntents](DYLIBS/SiriPlaybackControlIntents.md)
- [/System/Library/PrivateFrameworks/SiriPlaybackControlSupport.framework/SiriPlaybackControlSupport](DYLIBS/SiriPlaybackControlSupport.md)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningAnalytics.framework/SiriPrivateLearningAnalytics](DYLIBS/SiriPrivateLearningAnalytics.md)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningInference.framework/SiriPrivateLearningInference](DYLIBS/SiriPrivateLearningInference.md)
- [/System/Library/PrivateFrameworks/SiriReaderIntents.framework/SiriReaderIntents](DYLIBS/SiriReaderIntents.md)
- [/System/Library/PrivateFrameworks/SiriReferenceResolution.framework/SiriReferenceResolution](DYLIBS/SiriReferenceResolution.md)
- [/System/Library/PrivateFrameworks/SiriReferenceResolutionDataModel.framework/SiriReferenceResolutionDataModel](DYLIBS/SiriReferenceResolutionDataModel.md)
- [/System/Library/PrivateFrameworks/SiriReferenceResolver.framework/SiriReferenceResolver](DYLIBS/SiriReferenceResolver.md)
- [/System/Library/PrivateFrameworks/SiriRemembers.framework/SiriRemembers](DYLIBS/SiriRemembers.md)
- [/System/Library/PrivateFrameworks/SiriRequestDispatcher.framework/SiriRequestDispatcher](DYLIBS/SiriRequestDispatcher.md)
- [/System/Library/PrivateFrameworks/SiriSettingsIntents.framework/SiriSettingsIntents](DYLIBS/SiriSettingsIntents.md)
- [/System/Library/PrivateFrameworks/SiriSignals.framework/SiriSignals](DYLIBS/SiriSignals.md)
- [/System/Library/PrivateFrameworks/SiriSuggestions.framework/SiriSuggestions](DYLIBS/SiriSuggestions.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsAPI.framework/SiriSuggestionsAPI](DYLIBS/SiriSuggestionsAPI.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsIntelligence.framework/SiriSuggestionsIntelligence](DYLIBS/SiriSuggestionsIntelligence.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsKit.framework/SiriSuggestionsKit](DYLIBS/SiriSuggestionsKit.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsSupport.framework/SiriSuggestionsSupport](DYLIBS/SiriSuggestionsSupport.md)
- [/System/Library/PrivateFrameworks/SiriSystemCommandsIntents.framework/SiriSystemCommandsIntents](DYLIBS/SiriSystemCommandsIntents.md)
- [/System/Library/PrivateFrameworks/SiriTTS.framework/SiriTTS](DYLIBS/SiriTTS.md)
- [/System/Library/PrivateFrameworks/SiriTTSService.framework/SiriTTSService](DYLIBS/SiriTTSService.md)
- [/System/Library/PrivateFrameworks/SiriTimeAlarmInternal.framework/SiriTimeAlarmInternal](DYLIBS/SiriTimeAlarmInternal.md)
- [/System/Library/PrivateFrameworks/SiriTimeInternal.framework/SiriTimeInternal](DYLIBS/SiriTimeInternal.md)
- [/System/Library/PrivateFrameworks/SiriTimeTimerInternal.framework/SiriTimeTimerInternal](DYLIBS/SiriTimeTimerInternal.md)
- [/System/Library/PrivateFrameworks/SiriTurnTakingManager.framework/SiriTurnTakingManager](DYLIBS/SiriTurnTakingManager.md)
- [/System/Library/PrivateFrameworks/SiriUIActivation.framework/SiriUIActivation](DYLIBS/SiriUIActivation.md)
- [/System/Library/PrivateFrameworks/SiriUIBridge.framework/SiriUIBridge](DYLIBS/SiriUIBridge.md)
- [/System/Library/PrivateFrameworks/SiriUICore.framework/SiriUICore](DYLIBS/SiriUICore.md)
- [/System/Library/PrivateFrameworks/SiriUserSegments.framework/SiriUserSegments](DYLIBS/SiriUserSegments.md)
- [/System/Library/PrivateFrameworks/SiriUtilities.framework/SiriUtilities](DYLIBS/SiriUtilities.md)
- [/System/Library/PrivateFrameworks/SiriVOX.framework/SiriVOX](DYLIBS/SiriVOX.md)
- [/System/Library/PrivateFrameworks/SiriVideoIntents.framework/SiriVideoIntents](DYLIBS/SiriVideoIntents.md)
- [/System/Library/PrivateFrameworks/Sleep.framework/Sleep](DYLIBS/Sleep.md)
- [/System/Library/PrivateFrameworks/SleepHealth.framework/SleepHealth](DYLIBS/SleepHealth.md)
- [/System/Library/PrivateFrameworks/SleepHealthDaemon.framework/SleepHealthDaemon](DYLIBS/SleepHealthDaemon.md)
- [/System/Library/PrivateFrameworks/SleepHealthUI.framework/SleepHealthUI](DYLIBS/SleepHealthUI.md)
- [/System/Library/PrivateFrameworks/SleepWidgetUI.framework/SleepWidgetUI](DYLIBS/SleepWidgetUI.md)
- [/System/Library/PrivateFrameworks/SmartRepliesServer.framework/SmartRepliesServer](DYLIBS/SmartRepliesServer.md)
- [/System/Library/PrivateFrameworks/SnippetUI.framework/SnippetUI](DYLIBS/SnippetUI.md)
- [/System/Library/PrivateFrameworks/SocialLayer.framework/SocialLayer](DYLIBS/SocialLayer.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateBridge.framework/SoftwareUpdateBridge](DYLIBS/SoftwareUpdateBridge.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateController.framework/SoftwareUpdateController](DYLIBS/SoftwareUpdateController.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/SoftwareUpdateCore](DYLIBS/SoftwareUpdateCore.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport](DYLIBS/SoftwareUpdateCoreSupport.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices](DYLIBS/SoftwareUpdateServices.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateSettings.framework/SoftwareUpdateSettings](DYLIBS/SoftwareUpdateSettings.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateSettingsUI.framework/SoftwareUpdateSettingsUI](DYLIBS/SoftwareUpdateSettingsUI.md)
- [/System/Library/PrivateFrameworks/SonicFoundation.framework/SonicFoundation](DYLIBS/SonicFoundation.md)
- [/System/Library/PrivateFrameworks/SonicKit.framework/SonicKit](DYLIBS/SonicKit.md)
- [/System/Library/PrivateFrameworks/SpaceAttribution.framework/SpaceAttribution](DYLIBS/SpaceAttribution.md)
- [/System/Library/PrivateFrameworks/SpeakTypingServices.framework/SpeakTypingServices](DYLIBS/SpeakTypingServices.md)
- [/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition](DYLIBS/SpeakerRecognition.md)
- [/System/Library/PrivateFrameworks/SpeechRecognitionCommandAndControl.framework/SpeechRecognitionCommandAndControl](DYLIBS/SpeechRecognitionCommandAndControl.md)
- [/System/Library/PrivateFrameworks/SplashBoard.framework/SplashBoard](DYLIBS/SplashBoard.md)
- [/System/Library/PrivateFrameworks/SportsKit.framework/SportsKit](DYLIBS/SportsKit.md)
- [/System/Library/PrivateFrameworks/Spotlight.framework/Spotlight](DYLIBS/Spotlight.md)
- [/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon](DYLIBS/SpotlightDaemon.md)
- [/System/Library/PrivateFrameworks/SpotlightFoundation.framework/SpotlightFoundation](DYLIBS/SpotlightFoundation.md)
- [/System/Library/PrivateFrameworks/SpotlightLinguistics.framework/SpotlightLinguistics](DYLIBS/SpotlightLinguistics.md)
- [/System/Library/PrivateFrameworks/SpotlightReceiver.framework/SpotlightReceiver](DYLIBS/SpotlightReceiver.md)
- [/System/Library/PrivateFrameworks/SpotlightResources.framework/SpotlightResources](DYLIBS/SpotlightResources.md)
- [/System/Library/PrivateFrameworks/SpotlightServices.framework/SpotlightServices](DYLIBS/SpotlightServices.md)
- [/System/Library/PrivateFrameworks/SpotlightUI.framework/SpotlightUI](DYLIBS/SpotlightUI.md)
- [/System/Library/PrivateFrameworks/SpotlightUIInternal.framework/SpotlightUIInternal](DYLIBS/SpotlightUIInternal.md)
- [/System/Library/PrivateFrameworks/SpotlightUIShared.framework/SpotlightUIShared](DYLIBS/SpotlightUIShared.md)
- [/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard](DYLIBS/SpringBoard.md)
- [/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation](DYLIBS/SpringBoardFoundation.md)
- [/System/Library/PrivateFrameworks/SpringBoardHome.framework/SpringBoardHome](DYLIBS/SpringBoardHome.md)
- [/System/Library/PrivateFrameworks/SpringBoardIntents.framework/SpringBoardIntents](DYLIBS/SpringBoardIntents.md)
- [/System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices](DYLIBS/SpringBoardServices.md)
- [/System/Library/PrivateFrameworks/SpringBoardUI.framework/SpringBoardUI](DYLIBS/SpringBoardUI.md)
- [/System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices](DYLIBS/SpringBoardUIServices.md)
- [/System/Library/PrivateFrameworks/StatusKit.framework/StatusKit](DYLIBS/StatusKit.md)
- [/System/Library/PrivateFrameworks/StatusKitAgentCore.framework/StatusKitAgentCore](DYLIBS/StatusKitAgentCore.md)
- [/System/Library/PrivateFrameworks/Stocks.framework/Stocks](DYLIBS/Stocks.md)
- [/System/Library/PrivateFrameworks/StocksAnalytics.framework/StocksAnalytics](DYLIBS/StocksAnalytics.md)
- [/System/Library/PrivateFrameworks/StocksCore.framework/StocksCore](DYLIBS/StocksCore.md)
- [/System/Library/PrivateFrameworks/StocksKit.framework/StocksKit](DYLIBS/StocksKit.md)
- [/System/Library/PrivateFrameworks/StocksUI.framework/StocksUI](DYLIBS/StocksUI.md)
- [/System/Library/PrivateFrameworks/StorageData.framework/StorageData](DYLIBS/StorageData.md)
- [/System/Library/PrivateFrameworks/StorageKit.framework/StorageKit](DYLIBS/StorageKit.md)
- [/System/Library/PrivateFrameworks/StoreKitUI.framework/StoreKitUI](DYLIBS/StoreKitUI.md)
- [/System/Library/PrivateFrameworks/StoreServices.framework/StoreServices](DYLIBS/StoreServices.md)
- [/System/Library/PrivateFrameworks/StreamingZip.framework/StreamingZip](DYLIBS/StreamingZip.md)
- [/System/Library/PrivateFrameworks/SwiftNN.framework/SwiftNN](DYLIBS/SwiftNN.md)
- [/System/Library/PrivateFrameworks/SwiftSQLite.framework/SwiftSQLite](DYLIBS/SwiftSQLite.md)
- [/System/Library/PrivateFrameworks/Symbolication.framework/Symbolication](DYLIBS/Symbolication.md)
- [/System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter](DYLIBS/SymptomDiagnosticReporter.md)
- [/System/Library/PrivateFrameworks/SymptomReporter.framework/SymptomReporter](DYLIBS/SymptomReporter.md)
- [/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomAnalytics.framework/SymptomAnalytics](DYLIBS/SymptomAnalytics.md)
- [/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomEvaluator.framework/SymptomEvaluator](DYLIBS/SymptomEvaluator.md)
- [/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomPresentationFeed.framework/SymptomPresentationFeed](DYLIBS/SymptomPresentationFeed.md)
- [/System/Library/PrivateFrameworks/Synapse.framework/Synapse](DYLIBS/Synapse.md)
- [/System/Library/PrivateFrameworks/SyncedDefaults.framework/SyncedDefaults](DYLIBS/SyncedDefaults.md)
- [/System/Library/PrivateFrameworks/SystemAperture.framework/SystemAperture](DYLIBS/SystemAperture.md)
- [/System/Library/PrivateFrameworks/SystemApertureUI.framework/SystemApertureUI](DYLIBS/SystemApertureUI.md)
- [/System/Library/PrivateFrameworks/SystemStatus.framework/SystemStatus](DYLIBS/SystemStatus.md)
- [/System/Library/PrivateFrameworks/SystemStatusServer.framework/SystemStatusServer](DYLIBS/SystemStatusServer.md)
- [/System/Library/PrivateFrameworks/SystemStatusUI.framework/SystemStatusUI](DYLIBS/SystemStatusUI.md)
- [/System/Library/PrivateFrameworks/TCC.framework/TCC](DYLIBS/TCC.md)
- [/System/Library/PrivateFrameworks/TSReading.framework/TSReading](DYLIBS/TSReading.md)
- [/System/Library/PrivateFrameworks/TSUtility.framework/TSUtility](DYLIBS/TSUtility.md)
- [/System/Library/PrivateFrameworks/TVAppServices.framework/TVAppServices](DYLIBS/TVAppServices.md)
- [/System/Library/PrivateFrameworks/TVMLKit.framework/TVMLKit](DYLIBS/TVMLKit.md)
- [/System/Library/PrivateFrameworks/TVPlayback.framework/TVPlayback](DYLIBS/TVPlayback.md)
- [/System/Library/PrivateFrameworks/TVRemoteCore.framework/TVRemoteCore](DYLIBS/TVRemoteCore.md)
- [/System/Library/PrivateFrameworks/TVRemoteUI.framework/TVRemoteUI](DYLIBS/TVRemoteUI.md)
- [/System/Library/PrivateFrameworks/Tabi.framework/Tabi](DYLIBS/Tabi.md)
- [/System/Library/PrivateFrameworks/TeaCharts.framework/TeaCharts](DYLIBS/TeaCharts.md)
- [/System/Library/PrivateFrameworks/TeaDB.framework/TeaDB](DYLIBS/TeaDB.md)
- [/System/Library/PrivateFrameworks/TeaFoundation.framework/TeaFoundation](DYLIBS/TeaFoundation.md)
- [/System/Library/PrivateFrameworks/TeaSettings.framework/TeaSettings](DYLIBS/TeaSettings.md)
- [/System/Library/PrivateFrameworks/TeaSnappy.framework/TeaSnappy](DYLIBS/TeaSnappy.md)
- [/System/Library/PrivateFrameworks/TeaTemplate.framework/TeaTemplate](DYLIBS/TeaTemplate.md)
- [/System/Library/PrivateFrameworks/TeaUI.framework/TeaUI](DYLIBS/TeaUI.md)
- [/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences](DYLIBS/TelephonyPreferences.md)
- [/System/Library/PrivateFrameworks/TelephonyRPC.framework/TelephonyRPC](DYLIBS/TelephonyRPC.md)
- [/System/Library/PrivateFrameworks/TelephonyUI.framework/TelephonyUI](DYLIBS/TelephonyUI.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities](DYLIBS/TelephonyUtilities.md)
- [/System/Library/PrivateFrameworks/TelephonyXPCClient.framework/TelephonyXPCClient](DYLIBS/TelephonyXPCClient.md)
- [/System/Library/PrivateFrameworks/TemplateKit.framework/TemplateKit](DYLIBS/TemplateKit.md)
- [/System/Library/PrivateFrameworks/TextInput.framework/TextInput](DYLIBS/TextInput.md)
- [/System/Library/PrivateFrameworks/TextInputCore.framework/TextInputCore](DYLIBS/TextInputCore.md)
- [/System/Library/PrivateFrameworks/TextInputTestingKit.framework/TextInputTestingKit](DYLIBS/TextInputTestingKit.md)
- [/System/Library/PrivateFrameworks/TextInputUI.framework/TextInputUI](DYLIBS/TextInputUI.md)
- [/System/Library/PrivateFrameworks/TextRecognition.framework/TextRecognition](DYLIBS/TextRecognition.md)
- [/System/Library/PrivateFrameworks/TextToSpeech.framework/TextToSpeech](DYLIBS/TextToSpeech.md)
- [/System/Library/PrivateFrameworks/TextToSpeechMauiSupport.framework/TextToSpeechMauiSupport](DYLIBS/TextToSpeechMauiSupport.md)
- [/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingSupport.framework/TextToSpeechVoiceBankingSupport](DYLIBS/TextToSpeechVoiceBankingSupport.md)
- [/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingUI.framework/TextToSpeechVoiceBankingUI](DYLIBS/TextToSpeechVoiceBankingUI.md)
- [/System/Library/PrivateFrameworks/ThirdPartyApplicationSettings.framework/ThirdPartyApplicationSettings](DYLIBS/ThirdPartyApplicationSettings.md)
- [/System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam](DYLIBS/Tightbeam.md)
- [/System/Library/PrivateFrameworks/TimeSync.framework/TimeSync](DYLIBS/TimeSync.md)
- [/System/Library/PrivateFrameworks/TinCanShared.framework/TinCanShared](DYLIBS/TinCanShared.md)
- [/System/Library/PrivateFrameworks/TipKitCore.framework/TipKitCore](DYLIBS/TipKitCore.md)
- [/System/Library/PrivateFrameworks/TipKitLegacy.framework/TipKitLegacy](DYLIBS/TipKitLegacy.md)
- [/System/Library/PrivateFrameworks/TipsCore.framework/TipsCore](DYLIBS/TipsCore.md)
- [/System/Library/PrivateFrameworks/TipsDaemon.framework/TipsDaemon](DYLIBS/TipsDaemon.md)
- [/System/Library/PrivateFrameworks/TipsUI.framework/TipsUI](DYLIBS/TipsUI.md)
- [/System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary](DYLIBS/ToneLibrary.md)
- [/System/Library/PrivateFrameworks/TouchRemote.framework/TouchRemote](DYLIBS/TouchRemote.md)
- [/System/Library/PrivateFrameworks/TrackingAvoidance.framework/TrackingAvoidance](DYLIBS/TrackingAvoidance.md)
- [/System/Library/PrivateFrameworks/TraitsArbiter.framework/TraitsArbiter](DYLIBS/TraitsArbiter.md)
- [/System/Library/PrivateFrameworks/TranslationDaemon.framework/TranslationDaemon](DYLIBS/TranslationDaemon.md)
- [/System/Library/PrivateFrameworks/TranslationUIServices.framework/TranslationUIServices](DYLIBS/TranslationUIServices.md)
- [/System/Library/PrivateFrameworks/Transparency.framework/Transparency](DYLIBS/Transparency.md)
- [/System/Library/PrivateFrameworks/TransparencyUI.framework/TransparencyUI](DYLIBS/TransparencyUI.md)
- [/System/Library/PrivateFrameworks/Trial.framework/Trial](DYLIBS/Trial.md)
- [/System/Library/PrivateFrameworks/TrialProto.framework/TrialProto](DYLIBS/TrialProto.md)
- [/System/Library/PrivateFrameworks/TrialServer.framework/TrialServer](DYLIBS/TrialServer.md)
- [/System/Library/PrivateFrameworks/TrustedPeers.framework/TrustedPeers](DYLIBS/TrustedPeers.md)
- [/System/Library/PrivateFrameworks/UARPiCloud.framework/UARPiCloud](DYLIBS/UARPiCloud.md)
- [/System/Library/PrivateFrameworks/UIAccessibility.framework/UIAccessibility](DYLIBS/UIAccessibility.md)
- [/System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation](DYLIBS/UIFoundation.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore](DYLIBS/UIKitCore.md)
- [/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices](DYLIBS/UIKitServices.md)
- [/System/Library/PrivateFrameworks/URLFormatting.framework/URLFormatting](DYLIBS/URLFormatting.md)
- [/System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework](DYLIBS/UnifiedAssetFramework.md)
- [/System/Library/PrivateFrameworks/UnityPoster.framework/UnityPoster](DYLIBS/UnityPoster.md)
- [/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTracking](DYLIBS/UsageTracking.md)
- [/System/Library/PrivateFrameworks/UserActivity.framework/UserActivity](DYLIBS/UserActivity.md)
- [/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_apfs.dylib](DYLIBS/livefiles_apfs.dylib.md)
- [/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_exfat.dylib](DYLIBS/livefiles_exfat.dylib.md)
- [/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_hfs.dylib](DYLIBS/livefiles_hfs.dylib.md)
- [/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_msdos.dylib](DYLIBS/livefiles_msdos.dylib.md)
- [/System/Library/PrivateFrameworks/UserManagement.framework/UserManagement](DYLIBS/UserManagement.md)
- [/System/Library/PrivateFrameworks/UserManagementLayout.framework/UserManagementLayout](DYLIBS/UserManagementLayout.md)
- [/System/Library/PrivateFrameworks/UserNotificationsCore.framework/UserNotificationsCore](DYLIBS/UserNotificationsCore.md)
- [/System/Library/PrivateFrameworks/UserNotificationsKit.framework/UserNotificationsKit](DYLIBS/UserNotificationsKit.md)
- [/System/Library/PrivateFrameworks/UserNotificationsServer.framework/UserNotificationsServer](DYLIBS/UserNotificationsServer.md)
- [/System/Library/PrivateFrameworks/UserNotificationsSettings.framework/UserNotificationsSettings](DYLIBS/UserNotificationsSettings.md)
- [/System/Library/PrivateFrameworks/UserNotificationsUIKit.framework/UserNotificationsUIKit](DYLIBS/UserNotificationsUIKit.md)
- [/System/Library/PrivateFrameworks/UserSafety.framework/UserSafety](DYLIBS/UserSafety.md)
- [/System/Library/PrivateFrameworks/VDAF.framework/VDAF](DYLIBS/VDAF.md)
- [/System/Library/PrivateFrameworks/VFX.framework/Frameworks/libVFXCore.dylib](DYLIBS/libVFXCore.dylib.md)
- [/System/Library/PrivateFrameworks/VFX.framework/VFX](DYLIBS/VFX.md)
- [/System/Library/PrivateFrameworks/VectorKit.framework/VectorKit](DYLIBS/VectorKit.md)
- [/System/Library/PrivateFrameworks/VideoProcessing.framework/VideoProcessing](DYLIBS/VideoProcessing.md)
- [/System/Library/PrivateFrameworks/VideoSubscriberAccountUI.framework/VideoSubscriberAccountUI](DYLIBS/VideoSubscriberAccountUI.md)
- [/System/Library/PrivateFrameworks/VideosUI.framework/VideosUI](DYLIBS/VideosUI.md)
- [/System/Library/PrivateFrameworks/VideosUICore.framework/VideosUICore](DYLIBS/VideosUICore.md)
- [/System/Library/PrivateFrameworks/VirtualGarage.framework/VirtualGarage](DYLIBS/VirtualGarage.md)
- [/System/Library/PrivateFrameworks/VisionCore.framework/VisionCore](DYLIBS/VisionCore.md)
- [/System/Library/PrivateFrameworks/VisionHWAccelerationServices.framework/VisionHWAccelerationServices](DYLIBS/VisionHWAccelerationServices.md)
- [/System/Library/PrivateFrameworks/VisionKitCore.framework/VisionKitCore](DYLIBS/VisionKitCore.md)
- [/System/Library/PrivateFrameworks/VisionKitInternal.framework/VisionKitInternal](DYLIBS/VisionKitInternal.md)
- [/System/Library/PrivateFrameworks/VisualIntelligence.framework/VisualIntelligence](DYLIBS/VisualIntelligence.md)
- [/System/Library/PrivateFrameworks/VisualLocalization.framework/VisualLocalization](DYLIBS/VisualLocalization.md)
- [/System/Library/PrivateFrameworks/VisualLogger.framework/VisualLogger](DYLIBS/VisualLogger.md)
- [/System/Library/PrivateFrameworks/VisualUnderstanding.framework/VisualUnderstanding](DYLIBS/VisualUnderstanding.md)
- [/System/Library/PrivateFrameworks/VisualVoicemail.framework/IMAP.framework/IMAP](DYLIBS/IMAP.md)
- [/System/Library/PrivateFrameworks/VisualVoicemail.framework/VisualVoicemail](DYLIBS/VisualVoicemail.md)
- [/System/Library/PrivateFrameworks/VoiceMemos.framework/VoiceMemos](DYLIBS/VoiceMemos.md)
- [/System/Library/PrivateFrameworks/VoiceOverServices.framework/VoiceOverServices](DYLIBS/VoiceOverServices.md)
- [/System/Library/PrivateFrameworks/VoiceServices.framework/Support/libvoiced_tts.dylib](DYLIBS/libvoiced_tts.dylib.md)
- [/System/Library/PrivateFrameworks/VoiceServices.framework/VoiceServices](DYLIBS/VoiceServices.md)
- [/System/Library/PrivateFrameworks/VoiceShortcutClient.framework/VoiceShortcutClient](DYLIBS/VoiceShortcutClient.md)
- [/System/Library/PrivateFrameworks/VoiceShortcuts.framework/VoiceShortcuts](DYLIBS/VoiceShortcuts.md)
- [/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger](DYLIBS/VoiceTrigger.md)
- [/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/VoiceTriggerUI](DYLIBS/VoiceTriggerUI.md)
- [/System/Library/PrivateFrameworks/WPDaemon.framework/WPDaemon](DYLIBS/WPDaemon.md)
- [/System/Library/PrivateFrameworks/WallpaperKit.framework/WallpaperKit](DYLIBS/WallpaperKit.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/WatchFacesWallpaperSupport](DYLIBS/WatchFacesWallpaperSupport.md)
- [/System/Library/PrivateFrameworks/WatchListKit.framework/WatchListKit](DYLIBS/WatchListKit.md)
- [/System/Library/PrivateFrameworks/WatchdogClient.framework/WatchdogClient](DYLIBS/WatchdogClient.md)
- [/System/Library/PrivateFrameworks/Weather.framework/Weather](DYLIBS/Weather.md)
- [/System/Library/PrivateFrameworks/WeatherAnalytics.framework/WeatherAnalytics](DYLIBS/WeatherAnalytics.md)
- [/System/Library/PrivateFrameworks/WeatherCore.framework/WeatherCore](DYLIBS/WeatherCore.md)
- [/System/Library/PrivateFrameworks/WeatherDaemon.framework/WeatherDaemon](DYLIBS/WeatherDaemon.md)
- [/System/Library/PrivateFrameworks/WeatherFoundation.framework/WeatherFoundation](DYLIBS/WeatherFoundation.md)
- [/System/Library/PrivateFrameworks/WeatherMaps.framework/WeatherMaps](DYLIBS/WeatherMaps.md)
- [/System/Library/PrivateFrameworks/WeatherUI.framework/WeatherUI](DYLIBS/WeatherUI.md)
- [/System/Library/PrivateFrameworks/WebBookmarks.framework/WebBookmarks](DYLIBS/WebBookmarks.md)
- [/System/Library/PrivateFrameworks/WebBookmarksSwift.framework/WebBookmarksSwift](DYLIBS/WebBookmarksSwift.md)
- [/System/Library/PrivateFrameworks/WebCore.framework/Frameworks/libANGLE-shared.dylib](DYLIBS/libANGLE-shared.dylib.md)
- [/System/Library/PrivateFrameworks/WebCore.framework/Frameworks/libwebrtc.dylib](DYLIBS/libwebrtc.dylib.md)
- [/System/Library/PrivateFrameworks/WebCore.framework/WebCore](DYLIBS/WebCore.md)
- [/System/Library/PrivateFrameworks/WebGPU.framework/WebGPU](DYLIBS/WebGPU.md)
- [/System/Library/PrivateFrameworks/WebInspector.framework/WebInspector](DYLIBS/WebInspector.md)
- [/System/Library/PrivateFrameworks/WebKitLegacy.framework/WebKitLegacy](DYLIBS/WebKitLegacy.md)
- [/System/Library/PrivateFrameworks/WebPrivacy.framework/WebPrivacy](DYLIBS/WebPrivacy.md)
- [/System/Library/PrivateFrameworks/WebUI.framework/WebUI](DYLIBS/WebUI.md)
- [/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics](DYLIBS/WiFiAnalytics.md)
- [/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit](DYLIBS/WiFiKit.md)
- [/System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI](DYLIBS/WiFiKitUI.md)
- [/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer](DYLIBS/WiFiPeerToPeer.md)
- [/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy](DYLIBS/WiFiPolicy.md)
- [/System/Library/PrivateFrameworks/WidgetRenderer.framework/WidgetRenderer](DYLIBS/WidgetRenderer.md)
- [/System/Library/PrivateFrameworks/Widgets.framework/Widgets](DYLIBS/Widgets.md)
- [/System/Library/PrivateFrameworks/WirelessCoexManager.framework/WirelessCoexManager](DYLIBS/WirelessCoexManager.md)
- [/System/Library/PrivateFrameworks/WirelessDiagnostics.framework/WirelessDiagnostics](DYLIBS/WirelessDiagnostics.md)
- [/System/Library/PrivateFrameworks/WirelessInsights.framework/WirelessInsights](DYLIBS/WirelessInsights.md)
- [/System/Library/PrivateFrameworks/WirelessProximity.framework/WirelessProximity](DYLIBS/WirelessProximity.md)
- [/System/Library/PrivateFrameworks/WorkflowEditor.framework/WorkflowEditor](DYLIBS/WorkflowEditor.md)
- [/System/Library/PrivateFrameworks/WorkflowKit.framework/WorkflowKit](DYLIBS/WorkflowKit.md)
- [/System/Library/PrivateFrameworks/WorkflowResponsiveness.framework/WorkflowResponsiveness](DYLIBS/WorkflowResponsiveness.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/WorkflowUI](DYLIBS/WorkflowUI.md)
- [/System/Library/PrivateFrameworks/WorkflowUICore.framework/WorkflowUICore](DYLIBS/WorkflowUICore.md)
- [/System/Library/PrivateFrameworks/WorkflowUIServices.framework/WorkflowUIServices](DYLIBS/WorkflowUIServices.md)
- [/System/Library/PrivateFrameworks/WorkoutCore.framework/WorkoutCore](DYLIBS/WorkoutCore.md)
- [/System/Library/PrivateFrameworks/XCTTargetBootstrap.framework/XCTTargetBootstrap](DYLIBS/XCTTargetBootstrap.md)
- [/System/Library/PrivateFrameworks/XGBoostFramework.framework/XGBoostFramework](DYLIBS/XGBoostFramework.md)
- [/System/Library/PrivateFrameworks/XavierNews.framework/XavierNews](DYLIBS/XavierNews.md)
- [/System/Library/PrivateFrameworks/ZhuGeSupport.framework/ZhuGeSupport](DYLIBS/ZhuGeSupport.md)
- [/System/Library/PrivateFrameworks/ZhuGeSupport.framework/libZhuGeArmory.dylib](DYLIBS/libZhuGeArmory.dylib.md)
- [/System/Library/PrivateFrameworks/_IconServices_SwiftUI.framework/_IconServices_SwiftUI](DYLIBS/_IconServices_SwiftUI.md)
- [/System/Library/PrivateFrameworks/_JetEngine_SwiftUI.framework/_JetEngine_SwiftUI](DYLIBS/_JetEngine_SwiftUI.md)
- [/System/Library/PrivateFrameworks/_MusicKitInternal_MediaPlayer.framework/_MusicKitInternal_MediaPlayer](DYLIBS/_MusicKitInternal_MediaPlayer.md)
- [/System/Library/PrivateFrameworks/_SonicKit_MusicKit.framework/_SonicKit_MusicKit](DYLIBS/_SonicKit_MusicKit.md)
- [/System/Library/PrivateFrameworks/caulk.framework/caulk](DYLIBS/caulk.md)
- [/System/Library/PrivateFrameworks/iCalendar.framework/iCalendar](DYLIBS/iCalendar.md)
- [/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore](DYLIBS/iCloudDriveCore.md)
- [/System/Library/PrivateFrameworks/iCloudNotification.framework/iCloudNotification](DYLIBS/iCloudNotification.md)
- [/System/Library/PrivateFrameworks/iCloudQuota.framework/iCloudQuota](DYLIBS/iCloudQuota.md)
- [/System/Library/PrivateFrameworks/iCloudQuotaUI.framework/iCloudQuotaUI](DYLIBS/iCloudQuotaUI.md)
- [/System/Library/PrivateFrameworks/iTunesCloud.framework/iTunesCloud](DYLIBS/iTunesCloud.md)
- [/System/Library/PrivateFrameworks/iTunesStore.framework/iTunesStore](DYLIBS/iTunesStore.md)
- [/System/Library/PrivateFrameworks/iTunesStoreUI.framework/iTunesStoreUI](DYLIBS/iTunesStoreUI.md)
- [/System/Library/PrivateFrameworks/kperfdata.framework/kperfdata](DYLIBS/kperfdata.md)
- [/System/Library/PrivateFrameworks/ktrace.framework/ktrace](DYLIBS/ktrace.md)
- [/System/Library/PrivateFrameworks/libEDR.framework/libEDR](DYLIBS/libEDR.md)
- [/System/Library/PrivateFrameworks/vCard.framework/vCard](DYLIBS/vCard.md)
- [/System/Library/SystemConfiguration/CaptiveNetworkSupport.bundle/CaptiveNetworkSupport](DYLIBS/CaptiveNetworkSupport.md)
- [/System/Library/VideoCodecs/H264SW.videocodec](DYLIBS/H264SW.videocodec.md)
- [/System/Library/VideoCodecs/VCPHEVC.videocodec](DYLIBS/VCPHEVC.videocodec.md)
- [/System/Library/VideoDecoders/AVD.videodecoder](DYLIBS/AVD.videodecoder.md)
- [/System/Library/VideoDecoders/AppleProResHWDecoder.videodecoder](DYLIBS/AppleProResHWDecoder.videodecoder.md)
- [/System/Library/VideoDecoders/AppleProResSWDecoder.videodecoder](DYLIBS/AppleProResSWDecoder.videodecoder.md)
- [/System/Library/VideoDecoders/H264H8.videodecoder](DYLIBS/H264H8.videodecoder.md)
- [/System/Library/VideoDecoders/MP4VH8.videodecoder](DYLIBS/MP4VH8.videodecoder.md)
- [/System/Library/VideoDecoders/VCPMP4V.videodecoder](DYLIBS/VCPMP4V.videodecoder.md)
- [/System/Library/VideoEncoders/H264H9.videoencoder](DYLIBS/H264H9.videoencoder.md)
- [/System/Library/VideoEncoders/H9.videoencoder](DYLIBS/H9.videoencoder.md)
- [/System/Library/VideoEncoders/JPEGH1.videoencoder](DYLIBS/JPEGH1.videoencoder.md)
- [/System/Library/VideoProcessors/CCPortrait.bundle/CCPortrait](DYLIBS/CCPortrait.md)
- [/System/Library/VideoProcessors/DepthProcessorV2.bundle/DepthProcessorV2](DYLIBS/DepthProcessorV2.md)
- [/System/Library/VideoProcessors/IntelligentDistortionCorrectionV1.bundle/IntelligentDistortionCorrectionV1](DYLIBS/IntelligentDistortionCorrectionV1.md)
- [/System/Library/VideoProcessors/MattingV2.bundle/MattingV2](DYLIBS/MattingV2.md)
- [/System/Library/VideoProcessors/MetalFilter.bundle/MetalFilter](DYLIBS/MetalFilter.md)
- [/System/Library/VideoProcessors/NRFV2.bundle/NRFV2](DYLIBS/NRFV2.md)
- [/System/Library/VideoProcessors/NRFV4.bundle/NRFV4](DYLIBS/NRFV4.md)
- [/System/Library/VideoProcessors/SDOFRenderingV5.bundle/SDOFRenderingV5](DYLIBS/SDOFRenderingV5.md)
- [/System/Library/VideoProcessors/STF.bundle/STF](DYLIBS/STF.md)
- [/usr/lib/AppleConvergedTransport.dylib](DYLIBS/AppleConvergedTransport.dylib.md)
- [/usr/lib/dyld](DYLIBS/dyld.md)
- [/usr/lib/i18n/libUTF1632.dylib](DYLIBS/libUTF1632.dylib.md)
- [/usr/lib/i18n/libUTF7.dylib](DYLIBS/libUTF7.dylib.md)
- [/usr/lib/i18n/libUTF8.dylib](DYLIBS/libUTF8.dylib.md)
- [/usr/lib/i18n/libUTF8MAC.dylib](DYLIBS/libUTF8MAC.dylib.md)
- [/usr/lib/i18n/libiconv_std.dylib](DYLIBS/libiconv_std.dylib.md)
- [/usr/lib/libATCommandStudioDynamic.dylib](DYLIBS/libATCommandStudioDynamic.dylib.md)
- [/usr/lib/libAWDSupport.dylib](DYLIBS/libAWDSupport.dylib.md)
- [/usr/lib/libAXSafeCategoryBundle.dylib](DYLIBS/libAXSafeCategoryBundle.dylib.md)
- [/usr/lib/libAccessibility.dylib](DYLIBS/libAccessibility.dylib.md)
- [/usr/lib/libAppPatch.dylib](DYLIBS/libAppPatch.dylib.md)
- [/usr/lib/libAppleEXR.dylib](DYLIBS/libAppleEXR.dylib.md)
- [/usr/lib/libAppletTranslationLibrary.dylib](DYLIBS/libAppletTranslationLibrary.dylib.md)
- [/usr/lib/libAudioDSPCore.dylib](DYLIBS/libAudioDSPCore.dylib.md)
- [/usr/lib/libAudioIssueDetector.dylib](DYLIBS/libAudioIssueDetector.dylib.md)
- [/usr/lib/libAudioStatistics.dylib](DYLIBS/libAudioStatistics.dylib.md)
- [/usr/lib/libAudioToolboxUtility.dylib](DYLIBS/libAudioToolboxUtility.dylib.md)
- [/usr/lib/libBBUpdaterDynamic.dylib](DYLIBS/libBBUpdaterDynamic.dylib.md)
- [/usr/lib/libBKDM2.dylib](DYLIBS/libBKDM2.dylib.md)
- [/usr/lib/libBasebandCommandDriversARI.dylib](DYLIBS/libBasebandCommandDriversARI.dylib.md)
- [/usr/lib/libBasebandCommandDriversQMI.dylib](DYLIBS/libBasebandCommandDriversQMI.dylib.md)
- [/usr/lib/libBasebandManager.dylib](DYLIBS/libBasebandManager.dylib.md)
- [/usr/lib/libBasebandManagerICE.dylib](DYLIBS/libBasebandManagerICE.dylib.md)
- [/usr/lib/libCTGreenTeaLogger.dylib](DYLIBS/libCTGreenTeaLogger.dylib.md)
- [/usr/lib/libCoreEntitlements.dylib](DYLIBS/libCoreEntitlements.dylib.md)
- [/usr/lib/libFDR.dylib](DYLIBS/libFDR.dylib.md)
- [/usr/lib/libIOABP.dylib](DYLIBS/libIOABP.dylib.md)
- [/usr/lib/libIOAccessoryManager.dylib](DYLIBS/libIOAccessoryManager.dylib.md)
- [/usr/lib/libLLVM.dylib](DYLIBS/libLLVM.dylib.md)
- [/usr/lib/libMobileGestalt.dylib](DYLIBS/libMobileGestalt.dylib.md)
- [/usr/lib/libMobileGestaltExtensions.dylib](DYLIBS/libMobileGestaltExtensions.dylib.md)
- [/usr/lib/libNFC_Comet.dylib](DYLIBS/libNFC_Comet.dylib.md)
- [/usr/lib/libNFC_HAL.dylib](DYLIBS/libNFC_HAL.dylib.md)
- [/usr/lib/libPCITransport.dylib](DYLIBS/libPCITransport.dylib.md)
- [/usr/lib/libPN548_API.dylib](DYLIBS/libPN548_API.dylib.md)
- [/usr/lib/libQMIParserDynamic.dylib](DYLIBS/libQMIParserDynamic.dylib.md)
- [/usr/lib/libRoseBooter.dylib](DYLIBS/libRoseBooter.dylib.md)
- [/usr/lib/libSMC.dylib](DYLIBS/libSMC.dylib.md)
- [/usr/lib/libSoftwareUpdateSSO.dylib](DYLIBS/libSoftwareUpdateSSO.dylib.md)
- [/usr/lib/libSystem.B.dylib](DYLIBS/libSystem.B.dylib.md)
- [/usr/lib/libSystemHealth.dylib](DYLIBS/libSystemHealth.dylib.md)
- [/usr/lib/libTLE.dylib](DYLIBS/libTLE.dylib.md)
- [/usr/lib/libTelephonyCapabilities.dylib](DYLIBS/libTelephonyCapabilities.dylib.md)
- [/usr/lib/libTelephonyIOKitDynamic.dylib](DYLIBS/libTelephonyIOKitDynamic.dylib.md)
- [/usr/lib/libTelephonyUtilDynamic.dylib](DYLIBS/libTelephonyUtilDynamic.dylib.md)
- [/usr/lib/libWISSupport.dylib](DYLIBS/libWISSupport.dylib.md)
- [/usr/lib/libapp_launch_measurement.dylib](DYLIBS/libapp_launch_measurement.dylib.md)
- [/usr/lib/libapple_nghttp2.dylib](DYLIBS/libapple_nghttp2.dylib.md)
- [/usr/lib/libarchive.2.dylib](DYLIBS/libarchive.2.dylib.md)
- [/usr/lib/libate.dylib](DYLIBS/libate.dylib.md)
- [/usr/lib/libauthinstall.dylib](DYLIBS/libauthinstall.dylib.md)
- [/usr/lib/libboringssl.dylib](DYLIBS/libboringssl.dylib.md)
- [/usr/lib/libbsm.0.dylib](DYLIBS/libbsm.0.dylib.md)
- [/usr/lib/libc++.1.dylib](DYLIBS/libc++.1.dylib.md)
- [/usr/lib/libc++abi.dylib](DYLIBS/libc++abi.dylib.md)
- [/usr/lib/libcmark-gfm.dylib](DYLIBS/libcmark-gfm.dylib.md)
- [/usr/lib/libcompression.dylib](DYLIBS/libcompression.dylib.md)
- [/usr/lib/libcoreroutine.dylib](DYLIBS/libcoreroutine.dylib.md)
- [/usr/lib/libcoretls.dylib](DYLIBS/libcoretls.dylib.md)
- [/usr/lib/libcupolicy.dylib](DYLIBS/libcupolicy.dylib.md)
- [/usr/lib/libdns_services.dylib](DYLIBS/libdns_services.dylib.md)
- [/usr/lib/libdscsym.dylib](DYLIBS/libdscsym.dylib.md)
- [/usr/lib/libenergytrace.dylib](DYLIBS/libenergytrace.dylib.md)
- [/usr/lib/libexpat.1.dylib](DYLIBS/libexpat.1.dylib.md)
- [/usr/lib/libfire7.dylib](DYLIBS/libfire7.dylib.md)
- [/usr/lib/libiconv.2.dylib](DYLIBS/libiconv.2.dylib.md)
- [/usr/lib/libimage4.dylib](DYLIBS/libimage4.dylib.md)
- [/usr/lib/liblangid.dylib](DYLIBS/liblangid.dylib.md)
- [/usr/lib/libllvm-flatbuffers.dylib](DYLIBS/libllvm-flatbuffers.dylib.md)
- [/usr/lib/libllvm-lmdb.dylib](DYLIBS/libllvm-lmdb.dylib.md)
- [/usr/lib/liblockdown.dylib](DYLIBS/liblockdown.dylib.md)
- [/usr/lib/liblzma.5.dylib](DYLIBS/liblzma.5.dylib.md)
- [/usr/lib/libmav_ipc_router_dynamic.dylib](DYLIBS/libmav_ipc_router_dynamic.dylib.md)
- [/usr/lib/libmdns.dylib](DYLIBS/libmdns.dylib.md)
- [/usr/lib/libmis.dylib](DYLIBS/libmis.dylib.md)
- [/usr/lib/libmobileassetd.dylib](DYLIBS/libmobileassetd.dylib.md)
- [/usr/lib/libmorphun.dylib](DYLIBS/libmorphun.dylib.md)
- [/usr/lib/libnetworkextension.dylib](DYLIBS/libnetworkextension.dylib.md)
- [/usr/lib/libnfshared.dylib](DYLIBS/libnfshared.dylib.md)
- [/usr/lib/libnwswifttls.dylib](DYLIBS/libnwswifttls.dylib.md)
- [/usr/lib/libobjc.A.dylib](DYLIBS/libobjc.A.dylib.md)
- [/usr/lib/libolaf.dylib](DYLIBS/libolaf.dylib.md)
- [/usr/lib/libpartition2_dynamic.dylib](DYLIBS/libpartition2_dynamic.dylib.md)
- [/usr/lib/libperfcheck.dylib](DYLIBS/libperfcheck.dylib.md)
- [/usr/lib/libprotobuf-lite.dylib](DYLIBS/libprotobuf-lite.dylib.md)
- [/usr/lib/libprotobuf.dylib](DYLIBS/libprotobuf.dylib.md)
- [/usr/lib/libquic.dylib](DYLIBS/libquic.dylib.md)
- [/usr/lib/librealtime_safety.dylib](DYLIBS/librealtime_safety.dylib.md)
- [/usr/lib/libspindump.dylib](DYLIBS/libspindump.dylib.md)
- [/usr/lib/libsqlite3.dylib](DYLIBS/libsqlite3.dylib.md)
- [/usr/lib/libsystemstats.dylib](DYLIBS/libsystemstats.dylib.md)
- [/usr/lib/libtzupdate.dylib](DYLIBS/libtzupdate.dylib.md)
- [/usr/lib/libusrtcp.dylib](DYLIBS/libusrtcp.dylib.md)
- [/usr/lib/libxml2.2.dylib](DYLIBS/libxml2.2.dylib.md)
- [/usr/lib/libz.1.dylib](DYLIBS/libz.1.dylib.md)
- [/usr/lib/log/liblog_location.dylib](DYLIBS/liblog_location.dylib.md)
- [/usr/lib/log/liblog_network.dylib](DYLIBS/liblog_network.dylib.md)
- [/usr/lib/swift/libswiftAVFoundation.dylib](DYLIBS/libswiftAVFoundation.dylib.md)
- [/usr/lib/swift/libswiftAppleArchive.dylib](DYLIBS/libswiftAppleArchive.dylib.md)
- [/usr/lib/swift/libswiftCompression.dylib](DYLIBS/libswiftCompression.dylib.md)
- [/usr/lib/swift/libswiftCore.dylib](DYLIBS/libswiftCore.dylib.md)
- [/usr/lib/swift/libswiftCoreFoundation.dylib](DYLIBS/libswiftCoreFoundation.dylib.md)
- [/usr/lib/swift/libswiftCoreGraphics.dylib](DYLIBS/libswiftCoreGraphics.dylib.md)
- [/usr/lib/swift/libswiftCoreML.dylib](DYLIBS/libswiftCoreML.dylib.md)
- [/usr/lib/swift/libswiftCoreMedia.dylib](DYLIBS/libswiftCoreMedia.dylib.md)
- [/usr/lib/swift/libswiftDispatch.dylib](DYLIBS/libswiftDispatch.dylib.md)
- [/usr/lib/swift/libswiftDistributed.dylib](DYLIBS/libswiftDistributed.dylib.md)
- [/usr/lib/swift/libswiftIntents.dylib](DYLIBS/libswiftIntents.dylib.md)
- [/usr/lib/swift/libswiftMLCompute.dylib](DYLIBS/libswiftMLCompute.dylib.md)
- [/usr/lib/swift/libswiftMetal.dylib](DYLIBS/libswiftMetal.dylib.md)
- [/usr/lib/swift/libswiftObjectiveC.dylib](DYLIBS/libswiftObjectiveC.dylib.md)
- [/usr/lib/swift/libswiftObservation.dylib](DYLIBS/libswiftObservation.dylib.md)
- [/usr/lib/swift/libswiftQuartzCore.dylib](DYLIBS/libswiftQuartzCore.dylib.md)
- [/usr/lib/swift/libswiftRegexBuilder.dylib](DYLIBS/libswiftRegexBuilder.dylib.md)
- [/usr/lib/swift/libswiftShazamKit.dylib](DYLIBS/libswiftShazamKit.dylib.md)
- [/usr/lib/swift/libswiftSwiftOnoneSupport.dylib](DYLIBS/libswiftSwiftOnoneSupport.dylib.md)
- [/usr/lib/swift/libswiftUniformTypeIdentifiers.dylib](DYLIBS/libswiftUniformTypeIdentifiers.dylib.md)
- [/usr/lib/swift/libswiftXPC.dylib](DYLIBS/libswiftXPC.dylib.md)
- [/usr/lib/swift/libswift_RegexParser.dylib](DYLIBS/libswift_RegexParser.dylib.md)
- [/usr/lib/swift/libswift_StringProcessing.dylib](DYLIBS/libswift_StringProcessing.dylib.md)
- [/usr/lib/swift/libswiftos.dylib](DYLIBS/libswiftos.dylib.md)
- [/usr/lib/system/libcache.dylib](DYLIBS/libcache.dylib.md)
- [/usr/lib/system/libcommonCrypto.dylib](DYLIBS/libcommonCrypto.dylib.md)
- [/usr/lib/system/libcompiler_rt.dylib](DYLIBS/libcompiler_rt.dylib.md)
- [/usr/lib/system/libcopyfile.dylib](DYLIBS/libcopyfile.dylib.md)
- [/usr/lib/system/libcorecrypto.dylib](DYLIBS/libcorecrypto.dylib.md)
- [/usr/lib/system/libdyld.dylib](DYLIBS/libdyld.dylib.md)
- [/usr/lib/system/libmacho.dylib](DYLIBS/libmacho.dylib.md)
- [/usr/lib/system/libremovefile.dylib](DYLIBS/libremovefile.dylib.md)
- [/usr/lib/system/libsystem_asl.dylib](DYLIBS/libsystem_asl.dylib.md)
- [/usr/lib/system/libsystem_c.dylib](DYLIBS/libsystem_c.dylib.md)
- [/usr/lib/system/libsystem_collections.dylib](DYLIBS/libsystem_collections.dylib.md)
- [/usr/lib/system/libsystem_configuration.dylib](DYLIBS/libsystem_configuration.dylib.md)
- [/usr/lib/system/libsystem_containermanager.dylib](DYLIBS/libsystem_containermanager.dylib.md)
- [/usr/lib/system/libsystem_darwin.dylib](DYLIBS/libsystem_darwin.dylib.md)
- [/usr/lib/system/libsystem_darwindirectory.dylib](DYLIBS/libsystem_darwindirectory.dylib.md)
- [/usr/lib/system/libsystem_dnssd.dylib](DYLIBS/libsystem_dnssd.dylib.md)
- [/usr/lib/system/libsystem_eligibility.dylib](DYLIBS/libsystem_eligibility.dylib.md)
- [/usr/lib/system/libsystem_featureflags.dylib](DYLIBS/libsystem_featureflags.dylib.md)
- [/usr/lib/system/libsystem_info.dylib](DYLIBS/libsystem_info.dylib.md)
- [/usr/lib/system/libsystem_kernel.dylib](DYLIBS/libsystem_kernel.dylib.md)
- [/usr/lib/system/libsystem_m.dylib](DYLIBS/libsystem_m.dylib.md)
- [/usr/lib/system/libsystem_malloc.dylib](DYLIBS/libsystem_malloc.dylib.md)
- [/usr/lib/system/libsystem_networkextension.dylib](DYLIBS/libsystem_networkextension.dylib.md)
- [/usr/lib/system/libsystem_notify.dylib](DYLIBS/libsystem_notify.dylib.md)
- [/usr/lib/system/libsystem_platform.dylib](DYLIBS/libsystem_platform.dylib.md)
- [/usr/lib/system/libsystem_pthread.dylib](DYLIBS/libsystem_pthread.dylib.md)
- [/usr/lib/system/libsystem_sandbox.dylib](DYLIBS/libsystem_sandbox.dylib.md)
- [/usr/lib/system/libsystem_sanitizers.dylib](DYLIBS/libsystem_sanitizers.dylib.md)
- [/usr/lib/system/libsystem_trace.dylib](DYLIBS/libsystem_trace.dylib.md)
- [/usr/lib/system/libxpc.dylib](DYLIBS/libxpc.dylib.md)
- [/usr/lib/updaters/libAce3Updater.dylib](DYLIBS/libAce3Updater.dylib.md)
- [/usr/lib/updaters/libSEUpdater.dylib](DYLIBS/libSEUpdater.dylib.md)
- [/usr/lib/usd/libusd_ms.dylib](DYLIBS/libusd_ms.dylib.md)

</details>

## Feature Flags

### 🆕 NEW (5)

<details>
  <summary><i>View New</i></summary>

#### Conclaves.plist

>  `Domain/Conclaves.plist`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com_apple_audiomxd_conclave</key>
	<dict>
		<key>DevelopmentPhase</key>
		<string>FeatureComplete</string>
	</dict>
	<key>com_apple_backboardd_conclave</key>
	<dict>
		<key>DevelopmentPhase</key>
		<string>FeatureComplete</string>
	</dict>
	<key>com_apple_conclave_mediaserverd</key>
	<dict>
		<key>DevelopmentPhase</key>
		<string>FeatureComplete</string>
	</dict>
	<key>com_apple_corespeechd_conclave</key>
	<dict>
		<key>DevelopmentPhase</key>
		<string>FeatureComplete</string>
	</dict>
	<key>com_apple_exclavetestrunnerd_conclave</key>
	<dict>
		<key>DevelopmentPhase</key>
		<string>FeatureComplete</string>
	</dict>
	<key>com_apple_securdled_conclave</key>
	<dict>
		<key>DevelopmentPhase</key>
		<string>FeatureComplete</string>
	</dict>
	<key>com_apple_soundanalysisd_conclave</key>
	<dict>
		<key>DevelopmentPhase</key>
		<string>FeatureComplete</string>
	</dict>
</dict>
</plist>

```
#### Essonite.plist

>  `Domain/Essonite.plist`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict/>
</plist>

```
#### ISPExclaves.plist

>  `Domain/ISPExclaves.plist`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>ISPExclaveExclaveKitPath</key>
	<dict>
		<key>DevelopmentPhase</key>
		<string>FeatureComplete</string>
	</dict>
	<key>ISPExclavesEnablement</key>
	<dict>
		<key>DevelopmentPhase</key>
		<string>FeatureComplete</string>
	</dict>
</dict>
</plist>

```
#### MarketplaceKit.plist

>  `Domain/MarketplaceKit.plist`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>WebDistribution</key>
	<dict>
		<key>DevelopmentPhase</key>
		<string>FeatureComplete</string>
	</dict>
	<key>WebInstallation</key>
	<dict>
		<key>DevelopmentPhase</key>
		<string>FeatureComplete</string>
	</dict>
</dict>
</plist>

```
#### AudioHAL.plist

>  `Domain/AudioHAL.plist`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>Load_ADM_DSP_Lib</key>
	<dict>
		<key>Enabled</key>
		<true/>
	</dict>
</dict>
</plist>

```

</details>

### ❌ Removed (3)

- `Domain/SpaceAttributionFramework.plist`
- `Domain/EasyScreenSharing.plist`
- `Domain/AppDistribution.plist`

### ⬆️ Updated (25)

<details>
  <summary><i>View Updated</i></summary>

- [Domain/Accessibility.plist](FEATURES/Accessibility.plist.md)
- [Domain/AppStore.plist](FEATURES/AppStore.plist.md)
- [Domain/AssessmentMode.plist](FEATURES/AssessmentMode.plist.md)
- [Domain/BluetoothFeatures.plist](FEATURES/BluetoothFeatures.plist.md)
- [Domain/Books.plist](FEATURES/Books.plist.md)
- [Domain/CoreLocation.plist](FEATURES/CoreLocation.plist.md)
- [Domain/CoreSpeech.plist](FEATURES/CoreSpeech.plist.md)
- [Domain/CoreTelephony.plist](FEATURES/CoreTelephony.plist.md)
- [Domain/Family.plist](FEATURES/Family.plist.md)
- [Domain/FindMy.plist](FEATURES/FindMy.plist.md)
- [Domain/Home.plist](FEATURES/Home.plist.md)
- [Domain/HomeDeviceSetup.plist](FEATURES/HomeDeviceSetup.plist.md)
- [Domain/HomePod.plist](FEATURES/HomePod.plist.md)
- [Domain/Internationalization.plist](FEATURES/Internationalization.plist.md)
- [Domain/MediaPlayer.plist](FEATURES/MediaPlayer.plist.md)
- [Domain/NanoTimeKit.plist](FEATURES/NanoTimeKit.plist.md)
- [Domain/PencilAndPaper.plist](FEATURES/PencilAndPaper.plist.md)
- [Domain/Podcasts.plist](FEATURES/Podcasts.plist.md)
- [Domain/ScreenTime.plist](FEATURES/ScreenTime.plist.md)
- [Domain/SecureElementService.plist](FEATURES/SecureElementService.plist.md)
- [Domain/Spotlight.plist](FEATURES/Spotlight.plist.md)
- [Domain/TVApp.plist](FEATURES/TVApp.plist.md)
- [Domain/TelephonyUtilities.plist](FEATURES/TelephonyUtilities.plist.md)
- [Domain/UIKit.plist](FEATURES/UIKit.plist.md)
- [Domain/Wallet.plist](FEATURES/Wallet.plist.md)

</details>

## EOF
