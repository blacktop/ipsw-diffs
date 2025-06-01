# 17.2.1 (21C66) .vs 17.3 (21D50)

## IPSWs

- `iPhone16,1_17.2.1_21C66_Restore.ipsw`
- `iPhone16,1_17.3_21D50_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 17.2.1 *(21C66)* | 23.2.0 | 10002.60.75.0.3~27 | Sun, 12Nov2023 06:35:58 PST |
| 17.3 *(21D50)* | 23.3.0 | 10002.82.4~3 | Wed, 20Dec2023 17:32:00 PST |

### Kexts

#### ⬆️ Updated (86)

<details>
  <summary><i>View Updated</i></summary>

>  `com.apple.AGXFirmwareKextG16PRTBuddy`

```diff

-276.11.0.0.0
+276.21.0.0.0
   __TEXT.__const: 0x117
   __TEXT.__cstring: 0x5cd
   __TEXT_EXEC.__text: 0x2828

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xd40
   __DATA_CONST.__kalloc_type: 0x80
-  UUID: BF0C3F3E-EAC6-335F-9E32-AF66B9246992
+  UUID: EDAEE135-F50A-3EE8-96A1-AC6D7D3E75F8
   Functions: 35
   Symbols:   0
   CStrings:  33

```

>  `com.apple.AGXFirmwareKextRTBuddy64`

```diff

-276.11.0.0.0
+276.21.0.0.0
   __TEXT_EXEC.__text: 0x48
   __DATA.__data: 0xc4
   __DATA.__common: 0x10
-  UUID: A436BC76-1DA4-3AA4-B2CA-8F151A217694
+  UUID: F72F3D90-AD96-39C9-8C05-D4C9FEC9971E
   Functions: 0
   Symbols:   0
   CStrings:  0

```

>  `com.apple.AGXG16P`

```diff

-276.11.0.0.0
+276.21.0.0.0
   __TEXT.__const: 0x43b4
   __TEXT.__cstring: 0xc369
   __TEXT.__os_log: 0x2d8

   __DATA_CONST.__const: 0x103a0
   __DATA_CONST.__kalloc_type: 0x20c0
   __DATA_CONST.__kalloc_var: 0x30c0
-  UUID: 390B70F7-0214-3E47-89BE-3DFD69463CE8
+  UUID: 80863D48-320A-377D-8958-D34293D6E908
   Functions: 1212
   Symbols:   0
   CStrings:  1649
CStrings:
+ "Dec 20 2023 22:40:02"
- "Nov 12 2023 07:22:03"

```

>  `com.apple.driver.ASIOKit`

```diff

-11.43.0.0.0
+11.61.0.0.0
   __TEXT.__cstring: 0x1e3
   __TEXT.__const: 0x7c50
-  __TEXT_EXEC.__text: 0x2e2fc
+  __TEXT_EXEC.__text: 0x2e2f8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd8
   __DATA.__common: 0x60

   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0x2f78
-  UUID: D72E1810-1EBE-3732-8C96-4DFC59200864
+  UUID: B4F62919-92A6-39CB-9DC8-A7B9E934EEBF
   Functions: 44
   Symbols:   0
   CStrings:  12

```

>  `com.apple.driver.AppleALSColorSensor`

```diff

-1603.60.7.0.0
+1603.80.2.0.0
   __TEXT.__const: 0x104
   __TEXT.__cstring: 0x33fe
   __TEXT.__os_log: 0x96

   __DATA_CONST.__mod_term_func: 0x58
   __DATA_CONST.__const: 0x59e0
   __DATA_CONST.__kalloc_type: 0x340
-  UUID: 88C9A3E5-8E6A-36F5-BB95-FE220F53A997
+  UUID: 48AD886C-1AB3-3292-893D-75AACC8ABDBE
   Functions: 185
   Symbols:   0
   CStrings:  377

```

>  `com.apple.driver.AppleAOPAudio`

```diff

   __DATA_CONST.__mod_term_func: 0xe0
   __DATA_CONST.__const: 0xb7d0
   __DATA_CONST.__kalloc_type: 0xa00
-  UUID: 2416635D-F3A4-3D7E-86C2-61BDB697E7B9
+  UUID: 952E0F6F-AF1C-36E4-9347-BA029D492641
   Functions: 711
   Symbols:   0
   CStrings:  1152
CStrings:
+ "22:10:41"
+ "22:11:01"
+ "Dec 20 2023"
- "06:08:38"
- "06:09:13"
- "Nov 12 2023"

```

>  `com.apple.driver.AppleAOPVoiceTrigger`

```diff

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xd70
   __DATA_CONST.__kalloc_type: 0x180
-  UUID: 4F0D7381-E3B8-3582-A677-874150E3713C
+  UUID: 72FE8517-AA72-3E68-BF6F-56D3B6B0E17B
   Functions: 104
   Symbols:   0
   CStrings:  202
CStrings:
+ "22:34:20"
+ "Dec 20 2023"
- "07:06:35"
- "Nov 12 2023"

```

>  `com.apple.driver.AppleAVE2`

```diff

   __DATA_CONST.__const: 0x46e0
   __DATA_CONST.__kalloc_type: 0x1540
   __DATA_CONST.__kalloc_var: 0x8c0
-  UUID: F57023D9-3ADB-3A7E-BD7D-A57852A1A81A
+  UUID: 63EBE0F4-EC96-37D0-8D38-703ABB35901D
   Functions: 1276
   Symbols:   0
   CStrings:  5631
CStrings:
+ "20:24:00"
+ "Dec 20 2023"
- "08:44:47"
- "Nov 12 2023"

```

>  `com.apple.driver.AppleCallbackPowerSource`

```diff

-1630.60.5.0.1
+1630.60.6.0.0
   __TEXT.__cstring: 0xf3b
   __TEXT.__os_log: 0x76
   __TEXT_EXEC.__text: 0x49f0

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xc00
   __DATA_CONST.__kalloc_type: 0x80
-  UUID: 106E3593-EE7E-3DEE-A3AF-AE5CEA12ABB6
+  UUID: 8F91B27C-2BE8-358C-A451-72A4E20AC0BD
   Functions: 34
   Symbols:   0
   CStrings:  235

```

>  `com.apple.driver.AppleDCP`

```diff

-590.60.2.0.0
+590.80.5.0.0
   __TEXT.__cstring: 0x12a1
   __TEXT.__const: 0x18
   __TEXT_EXEC.__text: 0x5084

   __DATA_CONST.__mod_term_func: 0x20
   __DATA_CONST.__const: 0x1400
   __DATA_CONST.__kalloc_type: 0x100
-  UUID: 54113E26-C39E-35D6-8F3A-53169D8A2F02
+  UUID: 33C9B278-AE95-3DAC-8915-DFD4B8B78181
   Functions: 102
   Symbols:   0
   CStrings:  89

```

>  `com.apple.driver.AppleDCPDPTXProxy`

```diff

-224.60.1.0.0
-  __TEXT.__cstring: 0x14f5
+224.80.5.0.0
+  __TEXT.__cstring: 0x1523
   __TEXT.__const: 0x58
   __TEXT.__os_log: 0xd02
-  __TEXT_EXEC.__text: 0x9724
+  __TEXT_EXEC.__text: 0x98b8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0xd8
   __DATA_CONST.__auth_got: 0x1f8
-  __DATA_CONST.__got: 0x98
+  __DATA_CONST.__got: 0xa0
   __DATA_CONST.__mod_init_func: 0x28
   __DATA_CONST.__mod_term_func: 0x28
-  __DATA_CONST.__const: 0x2bf8
+  __DATA_CONST.__const: 0x2c38
   __DATA_CONST.__kalloc_type: 0x140
-  UUID: 114D4E8F-64B6-3883-801E-46E1CB4D5DC3
-  Functions: 160
+  UUID: 69BF97CF-E4C2-321D-B0DB-7BD586A7AD9A
+  Functions: 161
   Symbols:   0
-  CStrings:  214
+  CStrings:  216
 
CStrings:
+ "ResourceAvailableDefault"
+ "SetResourceAvailable"

```

>  `com.apple.driver.AppleDisplayCrossbar`

```diff

   __TEXT.__cstring: 0x4005
   __TEXT.__os_log: 0x5a52
   __TEXT.__const: 0x160
-  __TEXT_EXEC.__text: 0x313d0
+  __TEXT_EXEC.__text: 0x31498
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x3a8

   __DATA_CONST.__got: 0xd0
   __DATA_CONST.__mod_init_func: 0xb8
   __DATA_CONST.__mod_term_func: 0xb8
-  __DATA_CONST.__const: 0xc620
+  __DATA_CONST.__const: 0xc738
   __DATA_CONST.__kalloc_type: 0x5c0
-  UUID: 5EC014FF-7043-3D63-9AF9-065D911563EE
+  UUID: 1D5ABF89-EA53-318E-A9DA-D6CC60F76FB1
   Functions: 550
   Symbols:   0
   CStrings:  683

```

>  `com.apple.driver.AppleEmbeddedLightSensor`

```diff

-1603.60.7.0.0
+1603.80.2.0.0
   __TEXT.__const: 0x15e8
   __TEXT.__cstring: 0x4331
   __TEXT.__os_log: 0x2c

   __DATA_CONST.__mod_term_func: 0x48
   __DATA_CONST.__const: 0x4a50
   __DATA_CONST.__kalloc_type: 0x240
-  UUID: 212B1AF2-8A8E-3945-8352-A81D4587DDF5
+  UUID: DD964CF7-60DB-3E9B-B9FD-BFE9E7B798EF
   Functions: 227
   Symbols:   0
   CStrings:  467

```

>  `com.apple.driver.AppleFirmwareUpdateKext`

```diff

-916.60.6.0.0
+916.80.2.0.1
   __TEXT.__cstring: 0x8f8
   __TEXT_EXEC.__text: 0x25f4
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xc70
   __DATA_CONST.__kalloc_type: 0x80
-  UUID: 30116F8F-29F6-3A7C-9ED3-FD52C0C46E75
+  UUID: E5EF37F8-C559-3B7E-B8F0-08B38D56A1AB
   Functions: 40
   Symbols:   0
   CStrings:  62

```

>  `com.apple.driver.AppleGameControllerPersonality`

```diff

-11.2.3.0.0
+11.3.1.0.0
   __TEXT.__cstring: 0xd4
   __TEXT.__os_log: 0x53
   __TEXT_EXEC.__text: 0x7b8

   __DATA_CONST.__mod_term_func: 0x8
   __DATA_CONST.__const: 0x780
   __DATA_CONST.__kalloc_type: 0x40
-  UUID: 98EF8DF0-54E5-3B46-B7F3-1960A4F340E7
+  UUID: 1A2F99C0-D96F-3D59-847B-96CD691293B8
   Functions: 13
   Symbols:   0
   CStrings:  11

```

>  `com.apple.driver.AppleH10PearlCameraInterface`

```diff

-20.200.0.0.0
+20.300.0.0.0
   __TEXT.__cstring: 0x418
   __TEXT_EXEC.__text: 0x6b98
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__mod_term_func: 0x8
   __DATA_CONST.__const: 0x1aa8
   __DATA_CONST.__kalloc_type: 0x480
-  UUID: FECB08AE-5560-3B29-94F6-4A7F5823A64F
+  UUID: A4BB186F-06CD-37A6-9B6C-D5F5C30F5E30
   Functions: 214
   Symbols:   0
   CStrings:  46

```

>  `com.apple.driver.AppleH16ANEInterface`

```diff

-7.202.0.0.0
-  __TEXT.__os_log: 0x24c60
-  __TEXT.__cstring: 0x96be
+7.300.0.0.0
+  __TEXT.__os_log: 0x250da
+  __TEXT.__cstring: 0x9726
   __TEXT.__const: 0x430
-  __TEXT_EXEC.__text: 0x81c34
+  __TEXT_EXEC.__text: 0x825a4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2b88
   __DATA.__common: 0x370

   __DATA_CONST.__const: 0x5870
   __DATA_CONST.__kalloc_type: 0x2240
   __DATA_CONST.__kalloc_var: 0x1e00
-  UUID: 9E2CC7C0-1D32-39B4-AD60-EB3F1022035B
-  Functions: 953
+  UUID: C1BD7688-152C-3D9F-ABA0-E4670A27E975
+  Functions: 957
   Symbols:   0
-  CStrings:  2738
+  CStrings:  2761
 
CStrings:
+ "/AppleInternal/Library/BuildRoots/5a481bbe-9f57-11ee-9024-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.3.Internal.sdk/System/Library/Frameworks/Kernel.framework/PrivateHeaders/kernel_sdkroot/usr/include/c++/v1/__memory/construct_at.h"
+ "/AppleInternal/Library/BuildRoots/5a481bbe-9f57-11ee-9024-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.3.Internal.sdk/System/Library/Frameworks/Kernel.framework/PrivateHeaders/kernel_sdkroot/usr/include/c++/v1/span"
+ "/AppleInternal/Library/BuildRoots/5a481bbe-9f57-11ee-9024-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.3.Internal.sdk/System/Library/Frameworks/Kernel.framework/PrivateHeaders/kernel_sdkroot/usr/include/c++/v1/vector"
+ "ANE%d: %s: Bring out of Exclave mode and set the pending flag\n"
+ "ANE%d: %s: Client requesting power off: %s"
+ "ANE%d: %s: Client requesting power on: %s"
+ "ANE%d: %s: Completing pending request for switch to Exclave mode\n"
+ "ANE%d: %s: Driver intercepting Exclave property\n"
+ "ANE%d: %s: Exclave work paused\n"
+ "ANE%d: %s: Exclave work resumed\n"
+ "ANE%d: %s: Failed to open dummy SEP client: res=0x%08X\n"
+ "ANE%d: %s: Failed to open persistent client: res=0x%08X\n"
+ "ANE%d: %s: Failed to power off dummy SEP client: res=0x%08X\n"
+ "ANE%d: %s: Failed to power off persistent client: res=0x%08X\n"
+ "ANE%d: %s: Failed to power on dummy SEP client: res=0x%08X\n"
+ "ANE%d: %s: Failed to power on persistent client: res=0x%08X\n"
+ "ANE%d: %s: Invalid state for Exclave interrupt\n"
+ "ANE%d: %s: Masking Exclave interrupt\n"
+ "ANE%d: %s: No pending requests for switching from SEP to Exclave mode \n"
+ "ANE%d: %s: PauseExclaveWork call failed\n"
+ "ANE%d: %s: Powered up already, blocking: %d\n"
+ "ANE%d: %s: ResumeExclaveWork call failed\n"
+ "ANE%d: %s: Starting power down sequences for client at 0x%p\n"
+ "ANE%d: %s: Switch into SEP mode\n"
+ "ANE%d: %s: Switch out of SEP mode\n"
+ "ANE%d: %s: Toggling Exclave Mode switch flag and returning. State after toggle = %d\n"
+ "ANE%d: %s: Unmasking Exclave interrupt\n"
+ "ANE%d: %s: Unsupported property for kext\n"
+ "ANE%d: %s: clientContext->isPowered: SEP(%u) ISP(%u) PersistentClient(%u)\n"
+ "ANE%d: %s: clientname %s isPowered %d\n"
+ "ANE_AddDummySEPClient_gated"
+ "ANE_ExclavePause"
+ "ANE_ExclaveResume"
+ "ANE_RemoveDummySEPClient_gated"
+ "bool DeCxt::FileIndexToWeight(uint32_t, uint64_t, uint64_t, const char *&)"
+ "buffer overrun in MutableProcedureInfo"
+ "pointer overflow in MutableProcedureInfo"
- "%s: Insufficient weight buffer size to fit ANECMutableOperationInfo "
- "%s: Insufficient weight buffer size to fit ANECMutableWeightInfo "
- "%s: Insufficient weight buffer size to fit weight data "
- "/AppleInternal/Library/BuildRoots/529cd1b6-810a-11ee-9ed3-8e1462286c80/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.2.Internal.sdk/System/Library/Frameworks/Kernel.framework/PrivateHeaders/kernel_sdkroot/usr/include/c++/v1/__memory/construct_at.h"
- "/AppleInternal/Library/BuildRoots/529cd1b6-810a-11ee-9ed3-8e1462286c80/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.2.Internal.sdk/System/Library/Frameworks/Kernel.framework/PrivateHeaders/kernel_sdkroot/usr/include/c++/v1/span"
- "/AppleInternal/Library/BuildRoots/529cd1b6-810a-11ee-9ed3-8e1462286c80/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.2.Internal.sdk/System/Library/Frameworks/Kernel.framework/PrivateHeaders/kernel_sdkroot/usr/include/c++/v1/vector"
- "ANE%d: %s :Failed to open persistent client: res=0x%08X\n"
- "ANE%d: %s :Failed to power off persistent client: res=0x%08X\n"
- "ANE%d: %s :Failed to power on persistent client: res=0x%08X\n"
- "ANE%d: %s: Client: %s"
- "ANE%d: %s: Power early already: %d\n"
- "ANE%d: %s: Starting power down sequences\n"
- "ANE%d: %s: clientContext->isPowered: ISP(%u) SEP(%u) PersistentClient(%u)\n"
- "bool DeCxt::FileIndexToWeight(uint32_t, uint64_t, const char *&)"

```

>  `com.apple.driver.AppleH16CameraInterface`

```diff

-1.205.0.0.0
+1.300.0.0.0
   __TEXT.__const: 0xa898
   __TEXT.__cstring: 0xa4b3
   __TEXT.__os_log: 0x1414e

   __DATA_CONST.__const: 0x110c8
   __DATA_CONST.__kalloc_type: 0x1100
   __DATA_CONST.__kalloc_var: 0xc30
-  UUID: DF670C83-F5FD-39DB-A2A6-E128A473B094
+  UUID: 31A2091F-5769-3842-A5CE-F1EFBB74C076
   Functions: 807
   Symbols:   0
   CStrings:  2303

```

>  `com.apple.driver.AppleH16PhotonDetector`

```diff

-1.205.0.0.0
+1.300.0.0.0
   __TEXT.__cstring: 0x1ea
   __TEXT.__os_log: 0x5b0
   __TEXT_EXEC.__text: 0x27a4

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xe48
   __DATA_CONST.__kalloc_type: 0x100
-  UUID: 2CC4D95A-10AA-3A34-9390-E78F7D6A81EC
+  UUID: 880E8050-1D2D-35E9-928D-C72A4AFD1699
   Functions: 45
   Symbols:   0
   CStrings:  45

```

>  `com.apple.driver.AppleHIDALSService`

```diff

-1603.60.7.0.0
+1603.80.2.0.0
   __TEXT.__cstring: 0xbf
   __TEXT.__os_log: 0xc0
   __TEXT_EXEC.__text: 0x904

   __DATA_CONST.__mod_term_func: 0x8
   __DATA_CONST.__const: 0x5f0
   __DATA_CONST.__kalloc_type: 0x40
-  UUID: 2A83D96E-B732-3D5A-8BE3-8E735DF0F72F
+  UUID: FFB447AF-CE61-37A8-A22A-4E7524132194
   Functions: 14
   Symbols:   0
   CStrings:  18

```

>  `com.apple.driver.AppleHIDTransportSPI`

```diff

   __DATA_CONST.__const: 0x31e0
   __DATA_CONST.__kalloc_type: 0xa80
   __DATA_CONST.__kalloc_var: 0x320
-  UUID: 7D4898F5-82C3-3647-B00B-BD3496CB6068
+  UUID: 6D98ADDA-81FB-3A48-9C70-90A6F8FCCC4D
   Functions: 354
   Symbols:   0
   CStrings:  857
CStrings:
+ "/AppleInternal/Library/BuildRoots/5a481bbe-9f57-11ee-9024-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.3.Internal.sdk/usr/local/include/hidspi/HSMDevice.h"
+ "/AppleInternal/Library/BuildRoots/5a481bbe-9f57-11ee-9024-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.3.Internal.sdk/usr/local/include/hidspi/HSMDeviceInterface.h"
+ "/AppleInternal/Library/BuildRoots/5a481bbe-9f57-11ee-9024-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.3.Internal.sdk/usr/local/include/hidspi/HSMDeviceTest.h"
+ "/AppleInternal/Library/BuildRoots/5a481bbe-9f57-11ee-9024-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.3.Internal.sdk/usr/local/include/hidspi/HSMHIDInterface.h"
+ "/AppleInternal/Library/BuildRoots/5a481bbe-9f57-11ee-9024-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.3.Internal.sdk/usr/local/include/hidspi/HSMParserTest.h"
+ "/AppleInternal/Library/BuildRoots/5a481bbe-9f57-11ee-9024-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.3.Internal.sdk/usr/local/include/hidspi/HSMSPITest.h"
+ "/AppleInternal/Library/BuildRoots/5a481bbe-9f57-11ee-9024-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.3.Internal.sdk/usr/local/include/hidspi/HSMTransferDevice.h"
+ "/AppleInternal/Library/BuildRoots/5a481bbe-9f57-11ee-9024-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.3.Internal.sdk/usr/local/include/hidspi/HSMTransferTest.h"
+ "/AppleInternal/Library/BuildRoots/5a481bbe-9f57-11ee-9024-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.3.Internal.sdk/usr/local/include/hidspi/HSParserDevice.h"
+ "/AppleInternal/Library/BuildRoots/5a481bbe-9f57-11ee-9024-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.3.Internal.sdk/usr/local/include/hidspi/HSParserTest.h"
+ "/AppleInternal/Library/BuildRoots/5a481bbe-9f57-11ee-9024-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.3.Internal.sdk/usr/local/include/hidspi/HSTransferTest.h"
- "/AppleInternal/Library/BuildRoots/529cd1b6-810a-11ee-9ed3-8e1462286c80/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.2.Internal.sdk/usr/local/include/hidspi/HSMDevice.h"
- "/AppleInternal/Library/BuildRoots/529cd1b6-810a-11ee-9ed3-8e1462286c80/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.2.Internal.sdk/usr/local/include/hidspi/HSMDeviceInterface.h"
- "/AppleInternal/Library/BuildRoots/529cd1b6-810a-11ee-9ed3-8e1462286c80/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.2.Internal.sdk/usr/local/include/hidspi/HSMDeviceTest.h"
- "/AppleInternal/Library/BuildRoots/529cd1b6-810a-11ee-9ed3-8e1462286c80/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.2.Internal.sdk/usr/local/include/hidspi/HSMHIDInterface.h"
- "/AppleInternal/Library/BuildRoots/529cd1b6-810a-11ee-9ed3-8e1462286c80/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.2.Internal.sdk/usr/local/include/hidspi/HSMParserTest.h"
- "/AppleInternal/Library/BuildRoots/529cd1b6-810a-11ee-9ed3-8e1462286c80/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.2.Internal.sdk/usr/local/include/hidspi/HSMSPITest.h"
- "/AppleInternal/Library/BuildRoots/529cd1b6-810a-11ee-9ed3-8e1462286c80/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.2.Internal.sdk/usr/local/include/hidspi/HSMTransferDevice.h"
- "/AppleInternal/Library/BuildRoots/529cd1b6-810a-11ee-9ed3-8e1462286c80/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.2.Internal.sdk/usr/local/include/hidspi/HSMTransferTest.h"
- "/AppleInternal/Library/BuildRoots/529cd1b6-810a-11ee-9ed3-8e1462286c80/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.2.Internal.sdk/usr/local/include/hidspi/HSParserDevice.h"
- "/AppleInternal/Library/BuildRoots/529cd1b6-810a-11ee-9ed3-8e1462286c80/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.2.Internal.sdk/usr/local/include/hidspi/HSParserTest.h"
- "/AppleInternal/Library/BuildRoots/529cd1b6-810a-11ee-9ed3-8e1462286c80/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.2.Internal.sdk/usr/local/include/hidspi/HSTransferTest.h"

```

>  `com.apple.driver.AppleHPM`

```diff

-540.60.3.0.0
+540.80.1.0.0
   __TEXT.__cstring: 0x1825b
   __TEXT.__os_log: 0x1e8
   __TEXT.__const: 0x60

   __DATA_CONST.__mod_term_func: 0xf8
   __DATA_CONST.__const: 0x11040
   __DATA_CONST.__kalloc_type: 0xb00
-  UUID: 971BD2E9-F97D-3B40-A887-0F4D3F237E34
+  UUID: B7BEB033-693F-3922-9037-BD7B2A97859F
   Functions: 843
   Symbols:   0
   CStrings:  1453

```

>  `com.apple.driver.AppleIDV`

```diff

-6.204.0.0.0
+6.300.0.0.0
   __TEXT.__const: 0xf8
   __TEXT.__cstring: 0x137c
   __TEXT_EXEC.__text: 0x80cc

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xde8
   __DATA_CONST.__kalloc_type: 0x80
-  UUID: BEA3D495-FFC9-303B-AA6B-D612F11C8095
+  UUID: F41094BC-25E9-3786-A9F4-A47C0E9DCA36
   Functions: 83
   Symbols:   0
   CStrings:  117
CStrings:
+ "6.300"
- "6.204"

```

>  `com.apple.driver.AppleLockdownMode`

```diff

 65.0.0.0.0
   __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x43a9
-  __TEXT_EXEC.__text: 0x13a24
+  __TEXT.__cstring: 0x446f
+  __TEXT_EXEC.__text: 0x13bb0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc6
   __DATA.__common: 0x40

   __DATA_CONST.__mod_term_func: 0x8
   __DATA_CONST.__const: 0x5f0
   __DATA_CONST.__kalloc_type: 0x300
-  __DATA_CONST.__kalloc_var: 0x1360
-  UUID: 32506FA1-73CD-399A-8B9E-D1C38DCAFF4A
+  __DATA_CONST.__kalloc_var: 0x1400
+  UUID: 2264196E-722D-359C-B516-C5C190E183BB
   Functions: 168
   Symbols:   0
-  CStrings:  462
+  CStrings:  466
 
CStrings:
+ "ACMRequirement - ACMRequirementDataRatchet"
+ "requirement->dataLength >= sizeof(ACMRequirementDataRatchet)"
+ "requirement->type == kACMRequirementTypeRatchet"
+ "site.ACMRequirement.ACMRequirementDataRatchet"

```

>  `com.apple.driver.AppleM68Buttons`

```diff

 123.0.0.0.0
-  __TEXT.__cstring: 0x496b
+  __TEXT.__cstring: 0x4a31
   __TEXT.__const: 0x140
   __TEXT.__os_log: 0x606
-  __TEXT_EXEC.__text: 0x1c090
+  __TEXT_EXEC.__text: 0x1c21c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xca
   __DATA.__common: 0x90

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xbd0
   __DATA_CONST.__kalloc_type: 0x400
-  __DATA_CONST.__kalloc_var: 0x1360
-  UUID: C542088A-FDD8-3508-894E-3A5644E0544A
+  __DATA_CONST.__kalloc_var: 0x1400
+  UUID: EB854280-0E2B-3266-8148-9BA8A27484D9
   Functions: 238
   Symbols:   0
-  CStrings:  593
+  CStrings:  597
 
CStrings:
+ "ACMRequirement - ACMRequirementDataRatchet"
+ "requirement->dataLength >= sizeof(ACMRequirementDataRatchet)"
+ "requirement->type == kACMRequirementTypeRatchet"
+ "site.ACMRequirement.ACMRequirementDataRatchet"

```

>  `com.apple.driver.AppleMobileDispH16P-DCP`

```diff

-336.3.5.0.0
+336.3.6.0.0
   __TEXT.__cstring: 0x4f79
   __TEXT.__const: 0x1a98
   __TEXT_EXEC.__text: 0x1f2cc

   __DATA_CONST.__const: 0x3b08
   __DATA_CONST.__kalloc_type: 0x580
   __DATA_CONST.__kalloc_var: 0xf0
-  UUID: C7E95E67-CF92-3EF3-BD33-CAE2A21B9008
+  UUID: 8B4EED38-6EFC-38CF-B601-F7807E5B621C
   Functions: 493
   Symbols:   0
   CStrings:  476

```

>  `com.apple.driver.AppleMobileFileIntegrity`

```diff

 859.60.7.0.0
-  __TEXT.__cstring: 0x8f73
+  __TEXT.__cstring: 0x8fa1
   __TEXT.__const: 0x14a0
   __TEXT.__os_log: 0x233
   __TEXT_EXEC.__text: 0x2413c

   __DATA_CONST.__mod_term_func: 0x18
   __DATA_CONST.__const: 0x36c0
   __DATA_CONST.__kalloc_type: 0xe40
-  __DATA_CONST.__kalloc_var: 0x1270
-  UUID: 2E295F9D-D495-36A8-975D-27F5CF29C2E8
+  __DATA_CONST.__kalloc_var: 0x1310
+  UUID: 0144F710-632E-39FA-B482-0C5A1CD1DDAC
   Functions: 540
   Symbols:   0
-  CStrings:  913
+  CStrings:  914
 
CStrings:
+ "22:31:32"
+ "Dec 20 2023"
+ "site.ACMRequirement.ACMRequirementDataRatchet"
- "07:26:22"
- "Nov 12 2023"

```

>  `com.apple.driver.ApplePMP`

```diff

-961.62.2.0.0
+961.80.9.0.0
   __TEXT.__const: 0x48
   __TEXT.__cstring: 0x14f8
-  __TEXT_EXEC.__text: 0xd7e4
+  __TEXT_EXEC.__text: 0xd8a0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x178

   __DATA_CONST.__const: 0x3340
   __DATA_CONST.__kalloc_type: 0x240
   __DATA_CONST.__kalloc_var: 0x140
-  UUID: DB420397-1B8D-3867-9BD1-43EFC3FD7881
+  UUID: 4A3BCC52-371A-307B-91CA-0C8B0410AE69
   Functions: 278
   Symbols:   0
   CStrings:  155

```

>  `com.apple.driver.ApplePMPFirmware`

```diff

-961.62.2.0.0
+961.80.9.0.0
   __TEXT.__cstring: 0x376
   __TEXT_EXEC.__text: 0x11bc
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__mod_term_func: 0x8
   __DATA_CONST.__const: 0x618
   __DATA_CONST.__kalloc_type: 0x40
-  UUID: 2FF063AC-D80A-34B9-B7D9-0BBF1A457F3B
+  UUID: 9CC7EDC1-7699-3396-911A-AFED6FD688EE
   Functions: 20
   Symbols:   0
   CStrings:  51

```

>  `com.apple.driver.ApplePPMCPMS`

```diff

-857.60.2.0.0
+857.80.1.0.0
   __TEXT.__const: 0xe90
   __TEXT.__cstring: 0xdb2d
   __TEXT.__os_log: 0x1f5a

   __DATA_CONST.__mod_term_func: 0xa8
   __DATA_CONST.__const: 0x4f28
   __DATA_CONST.__kalloc_type: 0x940
-  UUID: B57B4F6F-FBC0-36FA-9380-991E4D812B8F
+  UUID: BF1335F1-AD2B-3DDE-B430-8A979C7B5A8C
   Functions: 1090
   Symbols:   0
   CStrings:  1364

```

>  `com.apple.driver.ApplePearlSEPDriver`

```diff

-667.60.2.0.0
+667.80.2.0.0
   __TEXT.__const: 0x248
   __TEXT.__cstring: 0x7941
   __TEXT.__os_log: 0x3abd

   __DATA_CONST.__const: 0x1f80
   __DATA_CONST.__kalloc_type: 0x540
   __DATA_CONST.__kalloc_var: 0x1e0
-  UUID: 39CD028D-E74B-3759-BEF7-0F968568780E
+  UUID: 70FC0A39-B5E1-3AE0-AD2C-849D537F5247
   Functions: 342
   Symbols:   0
   CStrings:  1275

```

>  `com.apple.driver.ApplePhotonDetector`

```diff

-8.205.0.0.0
+8.301.0.0.0
   __TEXT.__cstring: 0x1d7
   __TEXT.__os_log: 0x56e
   __TEXT_EXEC.__text: 0x27a4

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xe48
   __DATA_CONST.__kalloc_type: 0x100
-  UUID: 2AB9A01F-1B5C-338A-85A9-C28FAB495144
+  UUID: 11CD1A68-422B-3ECF-8E94-69A6F7102CF7
   Functions: 45
   Symbols:   0
   CStrings:  45

```

>  `com.apple.driver.AppleProxDriver`

```diff

-31.3.0.0.0
-  __TEXT.__cstring: 0x7f7
+31.6.0.0.0
+  __TEXT.__cstring: 0x819
   __TEXT.__os_log: 0x5d9
   __TEXT.__const: 0x28
-  __TEXT_EXEC.__text: 0x96bc
+  __TEXT_EXEC.__text: 0x9734
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0xd8

   __DATA_CONST.__mod_term_func: 0x28
   __DATA_CONST.__const: 0x20f8
   __DATA_CONST.__kalloc_type: 0x200
-  UUID: 73AA8CDC-F447-3B50-A8E6-8EBF007685DB
+  UUID: CB9E92BD-A679-355F-92CF-B50893201E5D
   Functions: 102
   Symbols:   0
-  CStrings:  143
+  CStrings:  144
 
CStrings:
+ "SuggestedLPAScreenOffHysteresisMs"

```

>  `com.apple.driver.AppleSEPCredentialManager`

```diff

-660.60.15.0.0
-  __TEXT.__cstring: 0xfd75
+660.80.7.0.0
+  __TEXT.__cstring: 0xfe89
   __TEXT.__const: 0x318
-  __TEXT_EXEC.__text: 0x46f60
+  __TEXT_EXEC.__text: 0x47154
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x1ff1
   __DATA.__common: 0x1d8

   __DATA_CONST.__mod_term_func: 0x58
   __DATA_CONST.__const: 0x1a98
   __DATA_CONST.__kalloc_type: 0x600
-  __DATA_CONST.__kalloc_var: 0x1360
-  UUID: D62D0B8A-A243-30F2-A6B1-D114C2FF20B4
+  __DATA_CONST.__kalloc_var: 0x1400
+  UUID: 8556F7E5-7FB0-3124-9B4D-C560BF8C66B1
   Functions: 684
   Symbols:   0
-  CStrings:  1745
+  CStrings:  1750
 
CStrings:
+ "%s: %s: ignoring not persistent var[%u].\n"
+ "%s: %s: ignoring unknown var[%u], device downgraded?.\n"
+ "ACMRequirement - ACMRequirementDataRatchet"
+ "requirement->dataLength >= sizeof(ACMRequirementDataRatchet)"
+ "requirement->type == kACMRequirementTypeRatchet"
+ "site.ACMRequirement.ACMRequirementDataRatchet"
- "isPersistent(slot)"

```

>  `com.apple.driver.AppleSEPKeyStore`

```diff

-1555.62.1.0.0
+1555.80.3.0.0
   __TEXT.__cstring: 0x389e
   __TEXT.__const: 0x814
   __TEXT_EXEC.__text: 0x3ab18

   __DATA_CONST.__const: 0x38c8
   __DATA_CONST.__kalloc_type: 0xd40
   __DATA_CONST.__kalloc_var: 0x140
-  UUID: EC10DA6B-B7E6-36D8-B177-FD06DEB9343C
+  UUID: 3CF7AD9E-CA83-36D1-B336-54775B603FCD
   Functions: 579
   Symbols:   0
   CStrings:  323
CStrings:
+ "22:39:53"
+ "Dec 20 2023"
- "07:47:33"
- "Nov 12 2023"

```

>  `com.apple.driver.AppleSMC`

```diff

   __DATA_CONST.__const: 0x74e0
   __DATA_CONST.__kalloc_type: 0x600
   __DATA_CONST.__kalloc_var: 0xa0
-  UUID: 4EC3196E-C2CB-3E85-99ED-E793A32F744F
+  UUID: 5A6CC8C6-E2EE-3FEE-95B4-A64D5987671E
   Functions: 463
   Symbols:   0
   CStrings:  856
CStrings:
+ "18:09:52"
+ "18:09:53"
+ "Dec 20 2023"
- "07:24:24"
- "07:24:26"
- "Nov 12 2023"

```

>  `com.apple.driver.AppleSPMIPMU`

```diff

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xf00
   __DATA_CONST.__kalloc_type: 0x140
-  UUID: 60FEE2B8-5E65-37D7-8DD0-C9C8A179D421
+  UUID: 906C03FC-7467-309A-80FA-3077C23BE95F
   Functions: 107
   Symbols:   0
   CStrings:  342
CStrings:
+ "%s::handleStart: %s _pmuNub: %p ** configuration not found ** built 22:10:57 Dec 20 2023\n"
+ "%s::handleStart: ro=%d nvram=%d helper=%d %s _pmuNub: %p 0x%04x:0x%04x-0x%04x built 22:10:57 Dec 20 2023\n"
+ "%s::start: %s _pmuNub: %p ** configuration not found ** built 22:10:57 Dec 20 2023\n"
+ "%s::start: %s _pmuNub: %p built 22:10:57 Dec 20 2023\n"
- "%s::handleStart: %s _pmuNub: %p ** configuration not found ** built 06:06:30 Nov 12 2023\n"
- "%s::handleStart: ro=%d nvram=%d helper=%d %s _pmuNub: %p 0x%04x:0x%04x-0x%04x built 06:06:30 Nov 12 2023\n"
- "%s::start: %s _pmuNub: %p ** configuration not found ** built 06:06:30 Nov 12 2023\n"
- "%s::start: %s _pmuNub: %p built 06:06:30 Nov 12 2023\n"

```

>  `com.apple.driver.AppleSmartBatteryManagerEmbedded`

```diff

-1630.60.5.0.1
+1630.60.6.0.0
   __TEXT.__cstring: 0x40cc
   __TEXT.__const: 0xbf8
   __TEXT.__os_log: 0x268f

   __DATA_CONST.__mod_term_func: 0x40
   __DATA_CONST.__const: 0x2dc0
   __DATA_CONST.__kalloc_type: 0x340
-  UUID: 14C63CB5-5116-3162-AC13-A4CCA756F2FC
+  UUID: 9CBF4FE6-3E92-31F6-950C-06579654E7C7
   Functions: 247
   Symbols:   0
   CStrings:  868

```

>  `com.apple.driver.AppleSmartIO2`

```diff

   __DATA_CONST.__const: 0x21f0
   __DATA_CONST.__kalloc_type: 0x280
   __DATA_CONST.__kalloc_var: 0xa0
-  UUID: 80A97654-ED55-35F8-B8CA-A97BC5814375
+  UUID: D2C4540A-1229-3A10-8E43-AB88F654D66B
   Functions: 366
   Symbols:   0
   CStrings:  378
CStrings:
+ "22:09:21"
+ "Dec 20 2023"
- "06:05:25"
- "Nov 12 2023"

```

>  `com.apple.driver.AppleT8130CLPC`

```diff

-994.60.5.0.0
+994.80.3.0.0
   __TEXT.__cstring: 0x2ad9
   __TEXT.__const: 0xad0
-  __TEXT_EXEC.__text: 0x45df4
+  __TEXT_EXEC.__text: 0x45e50
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x9268
   __DATA.__common: 0x6e11

   __DATA_CONST.__const: 0x4940
   __DATA_CONST.__kalloc_type: 0x380
   __DATA_CONST.__kalloc_var: 0x370
-  UUID: 0878FB32-30C7-3FC2-A0A6-CB0D0FC31F5B
+  UUID: 75EC6487-6148-39C8-A334-896733819722
   Functions: 640
   Symbols:   0
   CStrings:  445
CStrings:
+ "2023-12-20T18:57:28-08:00"
+ "AppleCLPC-994.80.3"
- "2023-11-12T07:30:16-08:00"
- "AppleCLPC-994.60.5"

```

>  `com.apple.driver.AppleUSBDeviceMux`

```diff

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0x780
   __DATA_CONST.__kalloc_type: 0x440
-  UUID: 94290601-DA56-30B0-B3A5-163C1ADFF0D5
+  UUID: E64016AC-8159-33AD-A616-DC762C2D85D7
   Functions: 69
   Symbols:   0
   CStrings:  144
CStrings:
+ "22:35:33"
+ "Dec 20 2023"
- "06:57:43"
- "Nov 12 2023"

```

>  `com.apple.driver.AppleUSBHostMergeProperties`

```diff

-1309.60.4.0.0
+1309.80.2.0.0
   __TEXT.__cstring: 0x89
   __TEXT_EXEC.__text: 0xac4
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__mod_term_func: 0x8
   __DATA_CONST.__const: 0x600
   __DATA_CONST.__kalloc_type: 0x40
-  UUID: DB273E5F-D4E1-36F7-B397-E0F36D63DA21
+  UUID: 21C32989-10BD-395E-A8B2-893696995B11
   Functions: 12
   Symbols:   0
   CStrings:  5

```

>  `com.apple.driver.AppleUSBLightningAdapter`

```diff

-48.62.1.0.0
+50.0.0.0.0
   __TEXT.__const: 0x8
   __TEXT.__cstring: 0x1185
   __TEXT.__os_log: 0xa8b

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xe28
   __DATA_CONST.__kalloc_type: 0x80
-  UUID: 5C4C4479-6052-3E84-BEEA-3234523121C3
+  UUID: 583F7BBF-03D2-378A-B841-C76192B4BC82
   Functions: 48
   Symbols:   0
   CStrings:  161

```

>  `com.apple.driver.AppleUSBXDCI`

```diff

-783.60.2.0.0
+783.80.2.0.0
   __TEXT.__cstring: 0x5852
   __TEXT.__os_log: 0x2877
   __TEXT.__const: 0x20
-  __TEXT_EXEC.__text: 0x266fc
+  __TEXT_EXEC.__text: 0x26734
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x100

   __DATA_CONST.__const: 0x1070
   __DATA_CONST.__kalloc_type: 0x300
   __DATA_CONST.__kalloc_var: 0x140
-  UUID: F210607F-C875-39F9-B950-BF1AFA63B23E
+  UUID: 89C74053-F054-31FF-8E63-2B32AB5FF28C
   Functions: 175
   Symbols:   0
   CStrings:  670

```

>  `com.apple.driver.AppleUSBXDCIARM`

```diff

-783.60.2.0.0
+783.80.2.0.0
   __TEXT.__const: 0x40
   __TEXT.__cstring: 0x2e4d
   __TEXT.__os_log: 0x3b5a
-  __TEXT_EXEC.__text: 0x2a878
+  __TEXT_EXEC.__text: 0x2a8a4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x178

   __DATA_CONST.__mod_term_func: 0x40
   __DATA_CONST.__const: 0x49d0
   __DATA_CONST.__kalloc_type: 0x200
-  UUID: 4D238AA2-43FB-3145-948B-7B42ACC10977
+  UUID: CC985597-9628-3D4B-A48C-B45C03BF691B
   Functions: 157
   Symbols:   0
   CStrings:  256

```

>  `com.apple.driver.AudioDMAController-T8130`

```diff

   __DATA_CONST.__mod_term_func: 0x20
   __DATA_CONST.__const: 0x1988
   __DATA_CONST.__kalloc_type: 0x340
-  UUID: 8BBBE86C-9EE6-3A25-87DD-46345338F263
+  UUID: BBE475AE-4539-3313-8376-44DE4BA7B419
   Functions: 224
   Symbols:   0
   CStrings:  366
CStrings:
+ "17:01:41"
+ "Dec 20 2023"
- "06:07:21"
- "Nov 12 2023"

```

>  `com.apple.driver.DCPAVFamilyProxy`

```diff

-280.62.1.0.0
+280.80.6.0.0
   __TEXT.__const: 0x250
   __TEXT.__cstring: 0x23fc
   __TEXT.__os_log: 0x1252

   __DATA_CONST.__const: 0x8520
   __DATA_CONST.__kalloc_type: 0x4c0
   __DATA_CONST.__kalloc_var: 0x3c0
-  UUID: 709C91A8-567B-38C2-8A87-053D06A7BFB0
+  UUID: 8103C186-95C5-3656-8A3A-5408E0FC5559
   Functions: 452
   Symbols:   0
   CStrings:  269

```

>  `com.apple.driver.DiskImages`

```diff

-649.0.0.0.0
-  __TEXT.__cstring: 0xc34
+649.80.1.0.1
+  __TEXT.__cstring: 0xc3d
   __TEXT_EXEC.__text: 0x9be0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8

   __DATA_CONST.__const: 0x2320
   __DATA_CONST.__kalloc_type: 0x2c0
   __DATA_CONST.__kalloc_var: 0xa0
-  UUID: 943FFD23-8191-3DEE-8BC6-7C4C9539E6AF
+  UUID: 01A0AE1F-04DF-3AF6-A901-A67D7582D918
   Functions: 145
   Symbols:   0
   CStrings:  149
CStrings:
+ "649.80.1.0.1"
- "649"

```

>  `com.apple.driver.DiskImages.FileBackingStore`

```diff

-649.0.0.0.0
+649.80.1.0.1
   __TEXT.__const: 0x10
   __TEXT.__cstring: 0x237
   __TEXT_EXEC.__text: 0x1384

   __DATA_CONST.__mod_term_func: 0x8
   __DATA_CONST.__const: 0x678
   __DATA_CONST.__kalloc_type: 0x40
-  UUID: 0F82FA78-598E-3C92-AF8F-1ADF2989589E
+  UUID: 15180300-11FF-34D6-BBB2-C59843D5594D
   Functions: 18
   Symbols:   0
   CStrings:  20

```

>  `com.apple.driver.DiskImages.KernelBacked`

```diff

-649.0.0.0.0
+649.80.1.0.1
   __TEXT.__cstring: 0x382
   __TEXT_EXEC.__text: 0x4818
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__mod_term_func: 0x38
   __DATA_CONST.__const: 0x2d28
   __DATA_CONST.__kalloc_type: 0x1c0
-  UUID: C21900F4-36E0-39DB-9A26-47FB20F24A2C
+  UUID: 57CD4083-9571-39B0-B0FB-2D4C17FEAD91
   Functions: 82
   Symbols:   0
   CStrings:  39

```

>  `com.apple.driver.DiskImages.RAMBackingStore`

```diff

-649.0.0.0.0
+649.80.1.0.1
   __TEXT.__cstring: 0xc8
   __TEXT_EXEC.__text: 0xb38
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__mod_term_func: 0x8
   __DATA_CONST.__const: 0x678
   __DATA_CONST.__kalloc_type: 0x40
-  UUID: 8DB5F14C-5D7F-3C6E-8A9D-8E33283AA6A4
+  UUID: 005E6A1E-01AA-3069-8482-D58B0F1EFA93
   Functions: 14
   Symbols:   0
   CStrings:  13

```

>  `com.apple.driver.DiskImages.ReadWriteDiskImage`

```diff

-649.0.0.0.0
+649.80.1.0.1
   __TEXT.__cstring: 0x48
   __TEXT_EXEC.__text: 0x57c
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__mod_term_func: 0x8
   __DATA_CONST.__const: 0x678
   __DATA_CONST.__kalloc_type: 0x40
-  UUID: 71AF3DFE-BD82-35AF-92AB-FA839B23E410
+  UUID: 549C37AC-0973-3CF3-A1B5-34BEDB33FE47
   Functions: 13
   Symbols:   0
   CStrings:  3

```

>  `com.apple.driver.DiskImages.UDIFDiskImage`

```diff

-649.0.0.0.0
+649.80.1.0.1
   __TEXT.__const: 0x30b8
   __TEXT.__cstring: 0x2ac
   __TEXT_EXEC.__text: 0xab00

   __DATA_CONST.__const: 0x25f0
   __DATA_CONST.__kalloc_type: 0x140
   __DATA_CONST.__kalloc_var: 0x190
-  UUID: B251CC78-1EB3-346B-A1C2-618AB75A421B
+  UUID: DD5047E6-A5BA-3712-9C6B-7CC265F9C83F
   Functions: 98
   Symbols:   0
   CStrings:  30

```

>  `com.apple.driver.IOHIDPowerSource`

```diff

-2008.60.7.0.0
+2008.80.3.0.1
   __TEXT.__const: 0x18
   __TEXT.__cstring: 0x7e4
   __TEXT.__os_log: 0x433

   __DATA_CONST.__mod_term_func: 0x20
   __DATA_CONST.__const: 0x1a78
   __DATA_CONST.__kalloc_type: 0x340
-  UUID: 34051480-83C2-3939-9709-FB76B8B0F4E7
+  UUID: 0FEBCC57-D5A4-3890-9C3A-1AB5A0727F71
   Functions: 140
   Symbols:   0
   CStrings:  107

```

>  `com.apple.driver.RTBuddy`

```diff

   __DATA_CONST.__const: 0xa368
   __DATA_CONST.__kalloc_type: 0x1200
   __DATA_CONST.__kalloc_var: 0xf0
-  UUID: 4B2028BD-06E5-3CD6-B65F-650CC60BBBCE
+  UUID: 02574DDA-1B7F-32FF-A014-7D4BFC4F73E9
   Functions: 1351
   Symbols:   0
   CStrings:  988
CStrings:
+ "22:35:11"
+ "Dec 20 2023"
- "07:21:17"
- "Nov 12 2023"

```

>  `com.apple.driver.usb.AppleUSBCommon`

```diff

-1309.60.4.0.0
+1309.80.2.0.0
   __TEXT.__cstring: 0x2b6
   __TEXT.__os_log: 0xc6
   __TEXT_EXEC.__text: 0x4c14

   __DATA_CONST.__mod_term_func: 0x20
   __DATA_CONST.__const: 0x818
   __DATA_CONST.__kalloc_type: 0x240
-  UUID: 9B9267EF-17CC-366C-A2A0-DCE3EEC798F2
+  UUID: E9E003E4-6B28-3855-84C9-FDD54160A7C3
   Functions: 84
   Symbols:   0
   CStrings:  42

```

>  `com.apple.driver.usb.AppleUSBHostBillboardDevice`

```diff

-1309.60.4.0.0
+1309.80.2.0.0
   __TEXT.__cstring: 0x29b
   __TEXT.__os_log: 0x15d
   __TEXT_EXEC.__text: 0x1ae0

   __DATA_CONST.__mod_term_func: 0x8
   __DATA_CONST.__const: 0x5f0
   __DATA_CONST.__kalloc_type: 0x40
-  UUID: 7BBA5D11-9E33-3AD0-BA83-433566FC697E
+  UUID: ED63A756-9B5E-34E7-8A80-8416B93AC658
   Functions: 10
   Symbols:   0
   CStrings:  32

```

>  `com.apple.driver.usb.AppleUSBHostCompositeDevice`

```diff

-1309.60.4.0.0
+1309.80.2.0.0
   __TEXT.__cstring: 0x4de
   __TEXT.__os_log: 0x358
   __TEXT_EXEC.__text: 0x4294

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0x920
   __DATA_CONST.__kalloc_type: 0xc0
-  UUID: 6D7BA102-5E71-3870-85E8-F5F71407B0FF
+  UUID: 12C7CE79-E70C-3A0A-8261-4EDA8A864BAC
   Functions: 37
   Symbols:   0
   CStrings:  44

```

>  `com.apple.driver.usb.AppleUSBHostPacketFilter`

```diff

-1309.60.4.0.0
+1309.80.2.0.0
   __TEXT.__const: 0x18
   __TEXT.__cstring: 0xa5a
   __TEXT.__os_log: 0xaf

   __DATA_CONST.__mod_term_func: 0x8
   __DATA_CONST.__const: 0x5f0
   __DATA_CONST.__kalloc_type: 0x140
-  UUID: 97C15D37-5387-3673-8BE0-B90FB2A21A5A
+  UUID: 75F01A37-CCE0-31C9-B605-3327C73A60A4
   Functions: 22
   Symbols:   0
   CStrings:  34

```

>  `com.apple.driver.usb.AppleUSBHostiOSDevice`

```diff

-1309.60.4.0.0
+1309.80.2.0.0
   __TEXT.__cstring: 0x145
   __TEXT.__os_log: 0x1e
   __TEXT_EXEC.__text: 0x1094

   __DATA_CONST.__mod_term_func: 0x8
   __DATA_CONST.__const: 0x5f0
   __DATA_CONST.__kalloc_type: 0x40
-  UUID: 1AED6B23-FF82-3489-B838-201BB6D04280
+  UUID: C158F8DD-F381-36CA-B2CE-7C6913976179
   Functions: 15
   Symbols:   0
   CStrings:  15

```

>  `com.apple.driver.usb.AppleUSBHub`

```diff

-1309.60.4.0.0
+1309.80.2.0.0
   __TEXT.__const: 0x58
   __TEXT.__cstring: 0x227f
   __TEXT.__os_log: 0x2429

   __DATA_CONST.__mod_term_func: 0x50
   __DATA_CONST.__const: 0x4848
   __DATA_CONST.__kalloc_type: 0x280
-  UUID: ECB0E3AB-5368-330F-825F-6883A29DE61B
+  UUID: 3007B734-1153-332C-9940-A204C79FD8E7
   Functions: 190
   Symbols:   0
   CStrings:  371

```

>  `com.apple.driver.usb.AppleUSBXHCI`

```diff

-1309.60.4.0.0
+1309.80.2.0.0
   __TEXT.__const: 0xc4
   __TEXT.__cstring: 0x5729
   __TEXT.__os_log: 0x5973

   __DATA_CONST.__const: 0x5a60
   __DATA_CONST.__kalloc_type: 0x8c0
   __DATA_CONST.__kalloc_var: 0xa0
-  UUID: C4192D36-24FD-36F3-8D08-C890773A49E7
+  UUID: 2A6621DC-72C2-3D0E-ABAE-9B326C2DE433
   Functions: 574
   Symbols:   0
   CStrings:  855

```

>  `com.apple.driver.usb.IOUSBHostHIDDevice`

```diff

-1309.60.4.0.0
+1309.80.2.0.0
   __TEXT.__cstring: 0xac4
   __TEXT.__os_log: 0x9af
   __TEXT_EXEC.__text: 0x8aac

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xf20
   __DATA_CONST.__kalloc_type: 0x200
-  UUID: 924D6CDF-7422-34D2-A431-44C9E4A86923
+  UUID: CE6B7D7F-7F14-347D-AC0C-0D255AF897AA
   Functions: 50
   Symbols:   0
   CStrings:  140

```

>  `com.apple.filesystems.apfs`

```diff

-2235.60.6.0.0
+2235.80.4.0.1
   __TEXT.__const: 0x690
-  __TEXT.__cstring: 0x442fc
-  __TEXT_EXEC.__text: 0x12c04c
+  __TEXT.__cstring: 0x44304
+  __TEXT_EXEC.__text: 0x12c0bc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x688
   __DATA.__bss: 0xc60

   __DATA_CONST.__const: 0x5d80
   __DATA_CONST.__kalloc_type: 0x4b40
   __DATA_CONST.__kalloc_var: 0x2760
-  UUID: 89DF074D-1F93-32AE-AC17-59BDD743D20F
+  UUID: F0A03F01-E7AA-392B-B236-BC50E152BA4C
   Functions: 1820
   Symbols:   0
   CStrings:  5963
CStrings:
+ "2023/12/20"
+ "2235.80.4.0.1"
+ "22:09:32"
+ "Dec 20 2023"
+ "apfs-2235.80.4.0.1"
- "06:08:43"
- "2023/11/12"
- "2235.60.6"
- "Nov 12 2023"
- "apfs-2235.60.6"

```

>  `com.apple.filesystems.lifs`

```diff

-208.60.13.0.2
+208.80.5.0.0
   __TEXT.__os_log: 0x1190
   __TEXT.__cstring: 0x1d00
   __TEXT.__const: 0x270
-  __TEXT_EXEC.__text: 0x19b2c
+  __TEXT_EXEC.__text: 0x19b58
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x5d0
   __DATA.__common: 0x138

   __DATA_CONST.__mod_term_func: 0x18
   __DATA_CONST.__const: 0x1688
   __DATA_CONST.__kalloc_type: 0xb40
-  UUID: 26620D80-27B5-309E-86FA-905D94596194
+  UUID: C229A0F6-8610-3976-ACDD-97B3D9C8C72D
   Functions: 302
   Symbols:   0
   CStrings:  352

```

>  `com.apple.iokit.IOAVFamily`

```diff

-446.62.1.0.0
+446.80.3.0.0
   __TEXT.__cstring: 0xa99f
   __TEXT.__os_log: 0x9c42
   __TEXT.__const: 0xe7c4

   __DATA_CONST.__const: 0x14d00
   __DATA_CONST.__kalloc_type: 0xf00
   __DATA_CONST.__kalloc_var: 0x1e0
-  UUID: 803C75CB-EC80-3153-B1A5-B1DE55E6DD10
+  UUID: 888B6330-1F57-3E2D-BD82-198AEB97D886
   Functions: 1428
   Symbols:   0
   CStrings:  2143

```

>  `com.apple.iokit.IOAccessoryManager`

```diff

-958.62.2.0.0
-  __TEXT.__cstring: 0xfe37
+958.82.1.0.0
+  __TEXT.__cstring: 0xfeb6
   __TEXT.__os_log: 0xfc14
   __TEXT.__const: 0x338
-  __TEXT_EXEC.__text: 0x103a74
+  __TEXT_EXEC.__text: 0x1045dc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x7e8
   __DATA.__common: 0x1590
-  __DATA.__bss: 0x10a
-  __DATA_CONST.__auth_got: 0x590
+  __DATA.__bss: 0x15a
+  __DATA_CONST.__auth_got: 0x598
   __DATA_CONST.__got: 0x1d8
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__mod_init_func: 0x318
+  __DATA_CONST.__mod_init_func: 0x328
   __DATA_CONST.__mod_term_func: 0x318
-  __DATA_CONST.__const: 0x27d00
-  __DATA_CONST.__kalloc_type: 0x22c0
-  UUID: 17223D9C-5189-37BC-A3EB-448DA28D0D98
-  Functions: 2575
+  __DATA_CONST.__const: 0x27f50
+  __DATA_CONST.__kalloc_type: 0x23c0
+  UUID: 2E4C1A9B-96CE-3FE3-8144-A7321DD860A5
+  Functions: 2599
   Symbols:   0
-  CStrings:  2665
+  CStrings:  2671
 
CStrings:
+ "112221121"
+ "212"
+ "Failed to allocate data object!!"
+ "OSValueObject<IOAccessoryIDBusTransport::TransferData>"
+ "OSValueObject<_MessageData_t>"
+ "site.T"
+ "txDataObject->getRetainCount: %d"
- "%s::%s: %s: getTransferData() returned NULL\n"

```

>  `com.apple.iokit.IOAccessoryPortUSB`

```diff

-958.62.2.0.0
+958.82.1.0.0
   __TEXT.__cstring: 0x6a0
   __TEXT_EXEC.__text: 0x27f8
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__mod_term_func: 0x8
   __DATA_CONST.__const: 0x640
   __DATA_CONST.__kalloc_type: 0x40
-  UUID: DCD686AA-96B9-388F-B35E-72397B389741
+  UUID: D61A696E-38D2-3436-A573-464F53746623
   Functions: 23
   Symbols:   0
   CStrings:  53

```

>  `com.apple.iokit.IODisplayPortFamily`

```diff

-678.60.1.0.0
+678.80.4.0.0
   __TEXT.__const: 0x300
-  __TEXT.__cstring: 0x72e0
-  __TEXT.__os_log: 0x900a
-  __TEXT_EXEC.__text: 0x53b1c
+  __TEXT.__cstring: 0x72ab
+  __TEXT.__os_log: 0x8fc2
+  __TEXT_EXEC.__text: 0x53c84
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x438

   __DATA_CONST.__got: 0x148
   __DATA_CONST.__mod_init_func: 0xd8
   __DATA_CONST.__mod_term_func: 0xd0
-  __DATA_CONST.__const: 0xcee8
+  __DATA_CONST.__const: 0xcf20
   __DATA_CONST.__kalloc_type: 0x680
   __DATA_CONST.__kalloc_var: 0x280
-  UUID: D5C266EE-50FE-39A1-9F2A-19F0CA602565
+  UUID: 3C0B1670-38B7-3EEC-82B2-89990E60F8A2
   Functions: 776
   Symbols:   0
-  CStrings:  1389
+  CStrings:  1387
 
CStrings:
+ "refresh"
- "IOAV[%d] %s<0x%llx>::%s: warning: skipping disconnect of non-idle port\n"
- "disconnectDFP"
- "warning: skipping disconnect of non-idle port\n"

```

>  `com.apple.iokit.IOHIDFamily`

```diff

-2008.60.7.0.0
+2008.80.3.0.1
   __TEXT.__cstring: 0x2497
   __TEXT.__const: 0x6b8
   __TEXT.__os_log: 0x28d2

   __DATA_CONST.__mod_term_func: 0xd0
   __DATA_CONST.__const: 0x9fc0
   __DATA_CONST.__kalloc_type: 0x1480
-  UUID: 9B525BED-EF2D-369E-8A54-5DB583966A97
+  UUID: 5BCBA3CA-1118-39A5-BC59-DED2E1582061
   Functions: 1104
   Symbols:   0
   CStrings:  632

```

>  `com.apple.iokit.IOMobileGraphicsFamily`

```diff

-336.3.5.0.0
+336.3.6.0.0
   __TEXT.__cstring: 0x80dc
   __TEXT.__const: 0x910
   __TEXT_EXEC.__text: 0x4008c

   __DATA_CONST.__mod_term_func: 0x50
   __DATA_CONST.__const: 0x4ff0
   __DATA_CONST.__kalloc_type: 0xac0
-  UUID: 9C9C632F-D3A0-3440-90B2-E13EBF8F9D55
+  UUID: DF522C6D-EA3F-33A4-9147-F6C3A2BD0F93
   Functions: 889
   Symbols:   0
   CStrings:  931

```

>  `com.apple.iokit.IOMobileGraphicsFamily-DCP`

```diff

-336.3.5.0.0
+336.3.6.0.0
   __TEXT.__cstring: 0x42c8
   __TEXT.__const: 0x31c1
   __TEXT_EXEC.__text: 0x3f54c

   __DATA_CONST.__mod_term_func: 0x28
   __DATA_CONST.__const: 0x1710
   __DATA_CONST.__kalloc_type: 0x880
-  UUID: 854B3A0E-9A52-3C9C-AA97-3504F49E2020
+  UUID: 1299FC04-8DAB-38C5-BA9F-A880EE67AC22
   Functions: 801
   Symbols:   0
   CStrings:  375

```

>  `com.apple.iokit.IONVMeFamily`

```diff

-723.0.7.0.0
-  __TEXT.__cstring: 0xefca
+723.80.1.0.0
+  __TEXT.__cstring: 0xefe4
   __TEXT.__const: 0x5c8
-  __TEXT_EXEC.__text: 0x569b4
+  __TEXT_EXEC.__text: 0x569c0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x534
   __DATA.__common: 0x500

   __DATA_CONST.__const: 0xc038
   __DATA_CONST.__kalloc_type: 0x780
   __DATA_CONST.__kalloc_var: 0x5f0
-  UUID: A01646B4-A01E-3FE7-90B3-A1AA01289BCB
+  UUID: 507DE51A-1B66-32AE-B08A-5ED59D905BB5
   Functions: 1008
   Symbols:   0
   CStrings:  1656
CStrings:
+ "( ( ( uint64_t ) inOffset + ( uint64_t ) inSize ) <= buffer->getLength ( ) )"
- "( ( inOffset + inSize ) <= buffer->getLength ( ) )"

```

>  `com.apple.iokit.IONetworkFamily`

```diff

-464.62.2.0.0
+464.80.2.0.2
   __TEXT.__cstring: 0x63
   __TEXT_EXEC.__text: 0x394
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__mod_term_func: 0x8
   __DATA_CONST.__const: 0x7a8
   __DATA_CONST.__kalloc_type: 0x40
-  UUID: 300D3CF7-9DEF-35A1-B2FD-E8111C120541
+  UUID: F99689D9-0015-3A52-AEB2-9ED03525996C
   Functions: 9
   Symbols:   0
   CStrings:  3

```

>  `com.apple.iokit.IOPCIFamily`

```diff

   __DATA_CONST.__const: 0x3c78
   __DATA_CONST.__kalloc_type: 0x600
   __DATA_CONST.__kalloc_var: 0x190
-  UUID: E9243C58-5DC3-3C10-AFF3-029FF28822E7
+  UUID: 341D9E33-389B-31DC-9BAC-3851571CF88F
   Functions: 430
   Symbols:   0
   CStrings:  630
CStrings:
+ "17:00:37"
+ "Dec 20 2023"
- "06:08:49"
- "Nov 12 2023"

```

>  `com.apple.iokit.IOPortFamily`

```diff

-48.62.1.0.0
+50.0.0.0.0
   __TEXT_EXEC.__text: 0x84
   __DATA.__data: 0xc8
   __DATA.__common: 0x10
-  UUID: CB8D6D24-A364-353D-93ED-748DCE1BCFA5
+  UUID: 8D098028-5FF6-3A15-85F0-047140663315
   Functions: 0
   Symbols:   0
   CStrings:  0

```

>  `com.apple.iokit.IOSkywalkFamily`

```diff

-464.62.2.0.0
+464.80.2.0.2
   __TEXT.__cstring: 0x1aff
   __TEXT.__const: 0xd80
-  __TEXT_EXEC.__text: 0x387b4
+  __TEXT_EXEC.__text: 0x3884c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xe8
   __DATA.__common: 0x6b0

   __DATA_CONST.__const: 0x8d00
   __DATA_CONST.__kalloc_type: 0x1640
   __DATA_CONST.__kalloc_var: 0x6e0
-  UUID: 7F446D92-E257-31A8-816F-6F300161DFA6
+  UUID: 06E2D4BC-5EE2-373C-9E8C-C51481FEA60A
   Functions: 1184
   Symbols:   0
   CStrings:  284

```

>  `com.apple.iokit.IOThunderboltFamily`

```diff

-6728.40.3.0.0
+6728.80.2.0.0
   __TEXT.__cstring: 0x301c9
   __TEXT.__const: 0x7e0
   __TEXT_EXEC.__text: 0x13b9f0

   __DATA_CONST.__const: 0x1cf40
   __DATA_CONST.__kalloc_type: 0x1d00
   __DATA_CONST.__kalloc_var: 0x910
-  UUID: 853DC498-C90F-3547-ABDB-CC99944C6188
+  UUID: 742183C9-DE23-3A8C-88BF-05A73C5BDADB
   Functions: 2781
   Symbols:   0
   CStrings:  2677
CStrings:
+ "22:12:11"
+ "Dec 20 2023"
- "06:07:34"
- "Nov 12 2023"

```

>  `com.apple.iokit.IOTimeSyncFamily`

```diff

-1220.2.0.0.0
+1230.2.0.0.0
   __TEXT.__cstring: 0x31ac
   __TEXT.__os_log: 0x6fa2
   __TEXT.__const: 0x1e8

   __DATA_CONST.__const: 0xbe08
   __DATA_CONST.__kalloc_type: 0xbc0
   __DATA_CONST.__kalloc_var: 0x280
-  UUID: A3B2FEA0-B2A2-3ADA-A682-47ED5A46D49C
+  UUID: E1537693-4848-36EE-AEF6-C9FBD2A04AB2
   Functions: 762
   Symbols:   0
   CStrings:  603

```

>  `com.apple.iokit.IOUSBDeviceFamily`

```diff

-783.60.2.0.0
+783.80.2.0.0
   __TEXT.__cstring: 0x2840
   __TEXT.__const: 0x68
   __TEXT.__os_log: 0x1910

   __DATA_CONST.__const: 0x3508
   __DATA_CONST.__kalloc_type: 0x640
   __DATA_CONST.__kalloc_var: 0x190
-  UUID: 0EE23AFD-6A69-317C-91AC-28736237237B
+  UUID: EB30FB3D-B259-3182-A57B-4A9F42E5DD74
   Functions: 399
   Symbols:   0
   CStrings:  444

```

>  `com.apple.iokit.IOUSBHostFamily`

```diff

-1309.60.4.0.0
+1309.80.2.0.0
   __TEXT.__cstring: 0x97c3
   __TEXT.__os_log: 0x800e
   __TEXT.__const: 0xa50

   __DATA_CONST.__const: 0xca20
   __DATA_CONST.__kalloc_type: 0x1cc0
   __DATA_CONST.__kalloc_var: 0x280
-  UUID: AC51DD16-4824-3B5D-A63E-8A28C056088E
+  UUID: 0A64B173-8E4C-3502-8844-C8A79E880D60
   Functions: 1167
   Symbols:   0
   CStrings:  1516

```

>  `com.apple.kec.corecrypto`

```diff

-1608.60.11.0.0
-  __TEXT.__cstring: 0x4669
+1608.80.10.0.0
+  __TEXT.__cstring: 0x4693
   __TEXT.__const: 0x14140
   __TEXT.__fips_hmacs: 0x20
-  __TEXT_EXEC.__text: 0x5080c
+  __TEXT_EXEC.__text: 0x50d0c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2df0
   __DATA.__bss: 0x2960

   __DATA_CONST.__got: 0x10
   __DATA_CONST.__auth_ptr: 0x120
   __DATA_CONST.__const: 0x28f8
-  UUID: B4707900-DA76-3F27-8D04-DC3E48890843
-  Functions: 848
+  UUID: 1FEEE683-F182-3E1A-B803-0DE292042477
+  Functions: 850
   Symbols:   0
-  CStrings:  538
+  CStrings:  539
 
CStrings:
+ "ccrsa_eme_pkcs1v15_decode_generate_random"

```

>  `com.apple.kernel`

```diff

-10002.60.75.0.3
+10002.82.4.0.0
   __TEXT.__const: 0x34980
   __TEXT.__copyio_vectors: 0xf0
-  __TEXT.__cstring: 0x62ec5
-  __TEXT.__os_log: 0x221fd
+  __TEXT.__cstring: 0x62fe1
+  __TEXT.__os_log: 0x2224d
   __TEXT.__eh_frame: 0x4c0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x2c0

   __DATA_CONST.__brk_desc: 0x48
   __DATA_SPTM.__const: 0x3c000
   __TEXT_EXEC.__hib_text: 0xc88
-  __TEXT_EXEC.__text: 0x73fda0
+  __TEXT_EXEC.__text: 0x740078
   __TEXT_BOOT_EXEC.__bootcode: 0x4cf8
   __KLD.__text: 0x1630
   __LASTDATA_CONST.__mod_init_func: 0x8

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x4434a
-  UUID: 156B3DF7-CFC3-3F9E-B349-97A6310E6D70
+  UUID: 5301F8A1-054D-31CB-BC1E-FF61B6C3E6CA
   Functions: 18971
   Symbols:   0
-  CStrings:  15680
+  CStrings:  15686
 
CStrings:
+ "%s: inm %llx already on relq ifp %s\n"
+ "Failed to get memory error port - mcc"
+ "Object has no pager because the backing vnode was force unmounted\n"
+ "Object has no pager because the backing vnode was ungrafted\n"
+ "inm->in6m_in_nrele == true"
+ "inm->inm_in_nrele == true"
+ "kmem_realloc(map=%p, addr=%p, size=%zd, entry=%p): object %p has unexpected pager %p (%d,%d,%d) @%s:%d"
- "Failed to get memory error port"

```

>  `com.apple.plugin.IOgPTPPlugin`

```diff

-1220.2.0.0.0
+1230.2.0.0.0
   __TEXT.__cstring: 0x60f2
   __TEXT.__os_log: 0x1a236
   __TEXT.__const: 0x28a

   __DATA_CONST.__const: 0xeab8
   __DATA_CONST.__kalloc_type: 0x940
   __DATA_CONST.__kalloc_var: 0x280
-  UUID: 73D5174E-E186-3B37-A54A-E7AFF63B4D01
+  UUID: E6A0C28E-90DE-3D6D-ADD5-B27B75B16F47
   Functions: 912
   Symbols:   0
   CStrings:  1415

```

>  `com.apple.security.AppleImage4`

```diff

   __DATA_CONST.__const: 0x97f8
   __DATA_CONST.__kalloc_type: 0x1c0
   __DATA_CONST.__img4_rt: 0x20
-  UUID: 1838A809-AE3C-33C9-972E-94FFEA6550A1
+  UUID: 075E22E2-A204-3244-B413-03D715A8DE17
   Functions: 425
   Symbols:   0
   CStrings:  707
CStrings:
+ "@(#)VERSION:Darwin Image4 Validator Version 5.0.0: Wed Dec 20 22:32:10 PST 2023; root:AppleImage4-247~2516/AppleImage4/RELEASE_ARM64E"
+ "Darwin Image4 Validator Version 5.0.0: Wed Dec 20 22:32:10 PST 2023; root:AppleImage4-247~2516/AppleImage4/RELEASE_ARM64E"
- "@(#)VERSION:Darwin Image4 Validator Version 5.0.0: Sun Nov 12 06:23:50 PST 2023; root:AppleImage4-247~2284/AppleImage4/RELEASE_ARM64E"
- "Darwin Image4 Validator Version 5.0.0: Sun Nov 12 06:23:50 PST 2023; root:AppleImage4-247~2284/AppleImage4/RELEASE_ARM64E"

```

>  `com.apple.security.sandbox`

```diff

-2169.60.10.0.0
-  __TEXT.__const: 0x174461
+2169.80.2.0.0
+  __TEXT.__const: 0x175471
   __TEXT.__cstring: 0x64e2
   __TEXT.__os_log: 0x1d08
   __TEXT_EXEC.__text: 0x307e4

   __DATA_CONST.__const: 0x3478
   __DATA_CONST.__kalloc_var: 0x550
   __DATA_CONST.__kalloc_type: 0xbc0
-  UUID: 5A0A0C39-FC51-3CD2-82B2-84FF541C22B4
+  UUID: 30E8CC80-8007-3629-8CB9-293F276D9844
   Functions: 553
   Symbols:   0
   CStrings:  1227

```

</details>

## MachO

### 🆕 NEW (3)

- `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6004.appex/Diagnostic-6004`
- `/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/RhizomePoster.appex/RhizomePoster`
- `/private/var/staged_system_apps/Books.app/PlugIns/BooksSpotlightExtension.appex/BooksSpotlightExtension`

### ❌ Removed (4)

- `/System/Library/Frameworks/WebKit.framework/XPCServices/com.apple.WebKit.WebContent.Crashy.xpc/com.apple.WebKit.WebContent.Crashy`
- `/System/Library/HIDPlugins/ServicePlugins/ApplePencilDMServicePlugin.plugin/ApplePencilDMServicePlugin`
- `/System/Library/HIDPlugins/SessionFilters/ApplePencilSessionFilter.plugin/ApplePencilSessionFilter`
- `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/AirPlayDiagnosticExtension.appex/AirPlayDiagnosticExtension`

### ⬆️ Updated (2710)

<details>
  <summary><i>View Updated</i></summary>

- [/Applications/AAUIViewService.app/AAUIViewService](MACHOS/AAUIViewService.md)
- [/Applications/AMSEngagementViewService.app/AMSEngagementViewService](MACHOS/AMSEngagementViewService.md)
- [/Applications/AXRemoteViewService.app/AXRemoteViewService](MACHOS/AXRemoteViewService.md)
- [/Applications/AXUIViewService.app/AXUIViewService](MACHOS/AXUIViewService.md)
- [/Applications/AccountAuthenticationDialog.app/AccountAuthenticationDialog](MACHOS/AccountAuthenticationDialog.md)
- [/Applications/ActivityMessagesApp.app/ActivityMessagesApp](MACHOS/ActivityMessagesApp.md)
- [/Applications/ActivityMessagesApp.app/PlugIns/ActivityMessagesExtension.appex/ActivityMessagesExtension](MACHOS/ActivityMessagesExtension.md)
- [/Applications/AirDropUI.app/AirDropUI](MACHOS/AirDropUI.md)
- [/Applications/AirPlayReceiver.app/AirPlayReceiver](MACHOS/AirPlayReceiver.md)
- [/Applications/AirPlaySenderUIApp.app/AirPlaySenderUIApp](MACHOS/AirPlaySenderUIApp.md)
- [/Applications/AnimojiStickers.app/AnimojiStickers](MACHOS/AnimojiStickers.md)
- [/Applications/AnimojiStickers.app/PlugIns/AnimojiStickersExtension.appex/AnimojiStickersExtension](MACHOS/AnimojiStickersExtension.md)
- [/Applications/AppSSOUIService.app/AppSSOUIService](MACHOS/AppSSOUIService.md)
- [/Applications/AppStore.app/AppStore](MACHOS/AppStore.md)
- [/Applications/AppStore.app/PlugIns/AppStoreWidgetsExtension.appex/AppStoreWidgetsExtension](MACHOS/AppStoreWidgetsExtension.md)
- [/Applications/AppStore.app/PlugIns/ProductPageExtension.appex/ProductPageExtension](MACHOS/ProductPageExtension.md)
- [/Applications/AppStore.app/PlugIns/SubscribePageExtension.appex/SubscribePageExtension](MACHOS/SubscribePageExtension.md)
- [/Applications/AskPermissionUI.app/AskPermissionUI](MACHOS/AskPermissionUI.md)
- [/Applications/AskToMessagesHost.app/AskToMessagesHost](MACHOS/AskToMessagesHost.md)
- [/Applications/AskToMessagesHost.app/Extensions/AskToExtension.appex/AskToExtension](MACHOS/AskToExtension.md)
- [/Applications/AskToMessagesHost.app/PlugIns/AskToMessagesExtension.appex/AskToMessagesExtension](MACHOS/AskToMessagesExtension.md)
- [/Applications/AuthKitUIService.app/AuthKitUIService](MACHOS/AuthKitUIService.md)
- [/Applications/AuthenticationServicesUI.app/AuthenticationServicesUI](MACHOS/AuthenticationServicesUI.md)
- [/Applications/AuthenticationServicesUI.app/PlugIns/AccountAuthenticationModificationExtensionHelper.appex/AccountAuthenticationModificationExtensionHelper](MACHOS/AccountAuthenticationModificationExtensionHelper.md)
- [/Applications/BacklinkIndicator.app/BacklinkIndicator](MACHOS/BacklinkIndicator.md)
- [/Applications/BarcodeScanner.app/BarcodeScanner](MACHOS/BarcodeScanner.md)
- [/Applications/Batteries.app/Batteries](MACHOS/Batteries.md)
- [/Applications/Batteries.app/PlugIns/BatteriesAvocadoWidgetExtension.appex/BatteriesAvocadoWidgetExtension](MACHOS/BatteriesAvocadoWidgetExtension.md)
- [/Applications/Batteries.app/PlugIns/BatteriesWidgetExtension.appex/BatteriesWidgetExtension](MACHOS/BatteriesWidgetExtension.md)
- [/Applications/Batteries.app/PlugIns/BatteriesWidgetIntentsExtension.appex/BatteriesWidgetIntentsExtension](MACHOS/BatteriesWidgetIntentsExtension.md)
- [/Applications/BusinessChatViewService.app/BusinessChatViewService](MACHOS/BusinessChatViewService.md)
- [/Applications/BusinessExtensionsWrapper.app/BusinessExtensionsWrapper](MACHOS/BusinessExtensionsWrapper.md)
- [/Applications/BusinessExtensionsWrapper.app/PlugIns/Business.appex/Business](MACHOS/Business.md)
- [/Applications/CTCarrierSpaceAuth.app/CTCarrierSpaceAuth](MACHOS/CTCarrierSpaceAuth.md)
- [/Applications/CTKUIService.app/CTKUIService](MACHOS/CTKUIService.md)
- [/Applications/CTNotifyUIService.app/CTNotifyUIService](MACHOS/CTNotifyUIService.md)
- [/Applications/Camera.app/Camera](MACHOS/Camera.md)
- [/Applications/Camera.app/PlugIns/CameraMessagesApp.appex/CameraMessagesApp](MACHOS/CameraMessagesApp.md)
- [/Applications/CarPlaySettings.app/CarPlaySettings](MACHOS/CarPlaySettings.md)
- [/Applications/CarPlaySetup.app/CarPlaySetup](MACHOS/CarPlaySetup.md)
- [/Applications/CarPlaySplashScreen.app/CarPlaySplashScreen](MACHOS/CarPlaySplashScreen.md)
- [/Applications/CarPlayWallpaper.app/CarPlayWallpaper](MACHOS/CarPlayWallpaper.md)
- [/Applications/CheckerBoard.app/CheckerBoard](MACHOS/CheckerBoard.md)
- [/Applications/CheckerBoardRemoteSetup.app/CheckerBoardRemoteSetup](MACHOS/CheckerBoardRemoteSetup.md)
- [/Applications/ClarityCamera.app/ClarityCamera](MACHOS/ClarityCamera.md)
- [/Applications/ClarityPhotos.app/ClarityPhotos](MACHOS/ClarityPhotos.md)
- [/Applications/ClipViewService.app/ClipViewService](MACHOS/ClipViewService.md)
- [/Applications/ClockAngel.app/ClockAngel](MACHOS/ClockAngel.md)
- [/Applications/ColorPickerUIService.app/ColorPickerUIService](MACHOS/ColorPickerUIService.md)
- [/Applications/CompanionServicesViewService.app/CompanionServicesViewService](MACHOS/CompanionServicesViewService.md)
- [/Applications/CompassCalibrationViewService.app/CompassCalibrationViewService](MACHOS/CompassCalibrationViewService.md)
- [/Applications/ContactPhotoCarouselRemoteAlert.app/ContactPhotoCarouselRemoteAlert](MACHOS/ContactPhotoCarouselRemoteAlert.md)
- [/Applications/ContactlessReaderUIService.app/ContactlessReaderUIService](MACHOS/ContactlessReaderUIService.md)
- [/Applications/ContinuityCaptureShieldUI.app/ContinuityCaptureShieldUI](MACHOS/ContinuityCaptureShieldUI.md)
- [/Applications/CoreAuthUI.app/CoreAuthUI](MACHOS/CoreAuthUI.md)
- [/Applications/Coverage Details.app/Coverage Details](MACHOS/Coverage_Details.md)
- [/Applications/CredentialSharingUIViewService.app/CredentialSharingUIViewService](MACHOS/CredentialSharingUIViewService.md)
- [/Applications/CredentialSharingUIViewService.app/PlugIns/ShareableCredentialsMessagesExtension.appex/ShareableCredentialsMessagesExtension](MACHOS/ShareableCredentialsMessagesExtension.md)
- [/Applications/DDActionsService.app/DDActionsService](MACHOS/DDActionsService.md)
- [/Applications/DKPairingUIService.app/DKPairingUIService](MACHOS/DKPairingUIService.md)
- [/Applications/DemoApp.app/DemoApp](MACHOS/DemoApp.md)
- [/Applications/Diagnostics.app/Diagnostics](MACHOS/Diagnostics.md)
- [/Applications/Diagnostics.app/PlugIns/com.apple.Diagnostics.diagnosticextension.appex/com.apple.Diagnostics.diagnosticextension](MACHOS/com.apple.Diagnostics.diagnosticextension.md)
- [/Applications/DiagnosticsReporter.app/DiagnosticsReporter](MACHOS/DiagnosticsReporter.md)
- [/Applications/DiagnosticsService.app/DiagnosticsService](MACHOS/DiagnosticsService.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-0001.appex/Diagnostic-0001](MACHOS/Diagnostic-0001.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3732.appex/Diagnostic-3732](MACHOS/Diagnostic-3732.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3734.appex/Diagnostic-3734](MACHOS/Diagnostic-3734.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3738.appex/Diagnostic-3738](MACHOS/Diagnostic-3738.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3741.appex/Diagnostic-3741](MACHOS/Diagnostic-3741.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3743.appex/Diagnostic-3743](MACHOS/Diagnostic-3743.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3744.appex/Diagnostic-3744](MACHOS/Diagnostic-3744.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3745.appex/Diagnostic-3745](MACHOS/Diagnostic-3745.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3903.appex/Diagnostic-3903](MACHOS/Diagnostic-3903.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3904.appex/Diagnostic-3904](MACHOS/Diagnostic-3904.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3905.appex/Diagnostic-3905](MACHOS/Diagnostic-3905.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3906.appex/Diagnostic-3906](MACHOS/Diagnostic-3906.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3907.appex/Diagnostic-3907](MACHOS/Diagnostic-3907.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3909.appex/Diagnostic-3909](MACHOS/Diagnostic-3909.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3939.appex/Diagnostic-3939](MACHOS/Diagnostic-3939.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3942.appex/Diagnostic-3942](MACHOS/Diagnostic-3942.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3985.appex/Diagnostic-3985](MACHOS/Diagnostic-3985.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4002.appex/Diagnostic-4002](MACHOS/Diagnostic-4002.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4003.appex/Diagnostic-4003](MACHOS/Diagnostic-4003.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4004.appex/Diagnostic-4004](MACHOS/Diagnostic-4004.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4005.appex/Diagnostic-4005](MACHOS/Diagnostic-4005.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4006.appex/Diagnostic-4006](MACHOS/Diagnostic-4006.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4007.appex/Diagnostic-4007](MACHOS/Diagnostic-4007.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4008.appex/Diagnostic-4008](MACHOS/Diagnostic-4008.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4009-iOS-D83-D84.appex/Diagnostic-4009-iOS-D83-D84](MACHOS/Diagnostic-4009-iOS-D83-D84.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4153.appex/Diagnostic-4153](MACHOS/Diagnostic-4153.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4154.appex/Diagnostic-4154](MACHOS/Diagnostic-4154.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4180.appex/Diagnostic-4180](MACHOS/Diagnostic-4180.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4181.appex/Diagnostic-4181](MACHOS/Diagnostic-4181.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4182.appex/Diagnostic-4182](MACHOS/Diagnostic-4182.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4183.appex/Diagnostic-4183](MACHOS/Diagnostic-4183.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4184.appex/Diagnostic-4184](MACHOS/Diagnostic-4184.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4276.appex/Diagnostic-4276](MACHOS/Diagnostic-4276.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4351.appex/Diagnostic-4351](MACHOS/Diagnostic-4351.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4359.appex/Diagnostic-4359](MACHOS/Diagnostic-4359.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4492-sshb.appex/Diagnostic-4492-sshb](MACHOS/Diagnostic-4492-sshb.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4579.appex/Diagnostic-4579](MACHOS/Diagnostic-4579.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4615.appex/Diagnostic-4615](MACHOS/Diagnostic-4615.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6000.appex/Diagnostic-6000](MACHOS/Diagnostic-6000.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6001.appex/Diagnostic-6001](MACHOS/Diagnostic-6001.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6002.appex/Diagnostic-6002](MACHOS/Diagnostic-6002.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-7004.appex/Diagnostic-7004](MACHOS/Diagnostic-7004.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8035.appex/Diagnostic-8035](MACHOS/Diagnostic-8035.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8068.appex/Diagnostic-8068](MACHOS/Diagnostic-8068.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8079.appex/Diagnostic-8079](MACHOS/Diagnostic-8079.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8134.appex/Diagnostic-8134](MACHOS/Diagnostic-8134.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8185.appex/Diagnostic-8185](MACHOS/Diagnostic-8185.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8187.appex/Diagnostic-8187](MACHOS/Diagnostic-8187.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8201.appex/Diagnostic-8201](MACHOS/Diagnostic-8201.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8209.appex/Diagnostic-8209](MACHOS/Diagnostic-8209.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8217.appex/Diagnostic-8217](MACHOS/Diagnostic-8217.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8238.appex/Diagnostic-8238](MACHOS/Diagnostic-8238.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8246.appex/Diagnostic-8246](MACHOS/Diagnostic-8246.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8253.appex/Diagnostic-8253](MACHOS/Diagnostic-8253.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8259.appex/Diagnostic-8259](MACHOS/Diagnostic-8259.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8262.appex/Diagnostic-8262](MACHOS/Diagnostic-8262.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8264.appex/Diagnostic-8264](MACHOS/Diagnostic-8264.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8268.appex/Diagnostic-8268](MACHOS/Diagnostic-8268.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8276.appex/Diagnostic-8276](MACHOS/Diagnostic-8276.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8288.appex/Diagnostic-8288](MACHOS/Diagnostic-8288.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8290-EFD.appex/Diagnostic-8290-EFD](MACHOS/Diagnostic-8290-EFD.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8357.appex/Diagnostic-8357](MACHOS/Diagnostic-8357.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8374.appex/Diagnostic-8374](MACHOS/Diagnostic-8374.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8381.appex/Diagnostic-8381](MACHOS/Diagnostic-8381.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8389.appex/Diagnostic-8389](MACHOS/Diagnostic-8389.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8441.appex/Diagnostic-8441](MACHOS/Diagnostic-8441.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8441.appex/Frameworks/DiagnosticsSupport.framework/DiagnosticsSupport](MACHOS/DiagnosticsSupport.md)
- [/Applications/DiagnosticsService.app/PlugIns/SystemReport-AirPods.appex/SystemReport-AirPods](MACHOS/SystemReport-AirPods.md)
- [/Applications/DiagnosticsService.app/PlugIns/SystemReport-BatteryCase.appex/SystemReport-BatteryCase](MACHOS/SystemReport-BatteryCase.md)
- [/Applications/DiagnosticsService.app/PlugIns/SystemReport-iOS-D83-D84.appex/SystemReport-iOS-D83-D84](MACHOS/SystemReport-iOS-D83-D84.md)
- [/Applications/EventViewService.app/EventViewService](MACHOS/EventViewService.md)
- [/Applications/ExposureNotificationRemoteViewService.app/ExposureNotificationRemoteViewService](MACHOS/ExposureNotificationRemoteViewService.md)
- [/Applications/EyeReliefUI.app/EyeReliefUI](MACHOS/EyeReliefUI.md)
- [/Applications/FMDMagSafeSetupRemoteUI.app/FMDMagSafeSetupRemoteUI](MACHOS/FMDMagSafeSetupRemoteUI.md)
- [/Applications/FTMInternal-4.app/FTMInternal-4](MACHOS/FTMInternal-4.md)
- [/Applications/FaceTimeLinkTrampoline.app/FaceTimeLinkTrampoline](MACHOS/FaceTimeLinkTrampoline.md)
- [/Applications/Family.app/Family](MACHOS/Family.md)
- [/Applications/Family.app/PlugIns/FAFollowupExtension.appex/FAFollowupExtension](MACHOS/FAFollowupExtension.md)
- [/Applications/Family.app/PlugIns/InviteMessageBubbleExtension.appex/InviteMessageBubbleExtension](MACHOS/InviteMessageBubbleExtension.md)
- [/Applications/FamilyControlsAuthenticationUI.app/FamilyControlsAuthenticationUI](MACHOS/FamilyControlsAuthenticationUI.md)
- [/Applications/Feedback Assistant iOS.app/Feedback Assistant iOS](MACHOS/Feedback_Assistant_iOS.md)
- [/Applications/FeedbackRemoteView.app/FeedbackRemoteView](MACHOS/FeedbackRemoteView.md)
- [/Applications/FieldTest.app/FieldTest](MACHOS/FieldTest.md)
- [/Applications/FinanceStub.app/FinanceStub](MACHOS/FinanceStub.md)
- [/Applications/FinanceUIService.app/FinanceUIService](MACHOS/FinanceUIService.md)
- [/Applications/FindMyExtensionContainer.app/FindMyExtensionContainer](MACHOS/FindMyExtensionContainer.md)
- [/Applications/FindMyExtensionContainer.app/PlugIns/FMDMagSafeExtension.appex/FMDMagSafeExtension](MACHOS/FMDMagSafeExtension.md)
- [/Applications/FindMyExtensionContainer.app/PlugIns/FindMyDeviceBluetoothExtension.appex/FindMyDeviceBluetoothExtension](MACHOS/FindMyDeviceBluetoothExtension.md)
- [/Applications/FindMyRemoteUIService.app/FindMyRemoteUIService](MACHOS/FindMyRemoteUIService.md)
- [/Applications/FontInstallViewService.app/FontInstallViewService](MACHOS/FontInstallViewService.md)
- [/Applications/FontPickerUIService.app/FontPickerUIService](MACHOS/FontPickerUIService.md)
- [/Applications/FunCameraEmojiStickers.app/FunCameraEmojiStickers](MACHOS/FunCameraEmojiStickers.md)
- [/Applications/FunCameraEmojiStickers.app/PlugIns/FunCameraEmojiStickersExtension.appex/FunCameraEmojiStickersExtension](MACHOS/FunCameraEmojiStickersExtension.md)
- [/Applications/FunCameraShapes.app/FunCameraShapes](MACHOS/FunCameraShapes.md)
- [/Applications/FunCameraShapes.app/PlugIns/FunCameraShapesExtension.appex/FunCameraShapesExtension](MACHOS/FunCameraShapesExtension.md)
- [/Applications/FunCameraText.app/FunCameraText](MACHOS/FunCameraText.md)
- [/Applications/FunCameraText.app/PlugIns/FunCameraTextExtension.appex/FunCameraTextExtension](MACHOS/FunCameraTextExtension.md)
- [/Applications/GameCenterRemoteAlert.app/GameCenterRemoteAlert](MACHOS/GameCenterRemoteAlert.md)
- [/Applications/GameCenterUIService.app/GameCenterUIService](MACHOS/GameCenterUIService.md)
- [/Applications/GameCenterUIService.app/PlugIns/GameCenterMessageExtension.appex/GameCenterMessageExtension](MACHOS/GameCenterMessageExtension.md)
- [/Applications/GameCenterWidgets.app/GameCenterWidgets](MACHOS/GameCenterWidgets.md)
- [/Applications/GameCenterWidgets.app/PlugIns/GCWidgets.appex/GCWidgets](MACHOS/GCWidgets.md)
- [/Applications/HDSViewService.app/HDSViewService](MACHOS/HDSViewService.md)
- [/Applications/HashtagImages.app/HashtagImages](MACHOS/HashtagImages.md)
- [/Applications/HashtagImages.app/PlugIns/HashtagImagesExtension.appex/HashtagImagesExtension](MACHOS/HashtagImagesExtension.md)
- [/Applications/HealthENBuddy.app/HealthENBuddy](MACHOS/HealthENBuddy.md)
- [/Applications/HealthENLauncher.app/HealthENLauncher](MACHOS/HealthENLauncher.md)
- [/Applications/HealthPrivacyService.app/HealthPrivacyService](MACHOS/HealthPrivacyService.md)
- [/Applications/HearingApp.app/HearingApp](MACHOS/HearingApp.md)
- [/Applications/HomeCaptiveViewService.app/HomeCaptiveViewService](MACHOS/HomeCaptiveViewService.md)
- [/Applications/HomeControlService.app/HomeControlService](MACHOS/HomeControlService.md)
- [/Applications/HomeUIService.app/HomeUIService](MACHOS/HomeUIService.md)
- [/Applications/InCallService.app/InCallService](MACHOS/InCallService.md)
- [/Applications/InCallService.app/PlugIns/FaceTimeShareExtension.appex/FaceTimeShareExtension](MACHOS/FaceTimeShareExtension.md)
- [/Applications/InCallService.app/PlugIns/IntentsUI.appex/IntentsUI](MACHOS/IntentsUI.md)
- [/Applications/InCallService.app/PlugIns/RemotePeoplePicker.appex/RemotePeoplePicker](MACHOS/RemotePeoplePicker.md)
- [/Applications/InputUI.app/InputUI](MACHOS/InputUI.md)
- [/Applications/Jellyfish.app/Jellyfish](MACHOS/Jellyfish.md)
- [/Applications/Jellyfish.app/PlugIns/Animoji.appex/Animoji](MACHOS/Animoji.md)
- [/Applications/MBHelperApp.app/MBHelperApp](MACHOS/MBHelperApp.md)
- [/Applications/MTLReplayer.app/Frameworks/MTLReplayController.framework/MTLReplayController](MACHOS/MTLReplayController.md)
- [/Applications/MTLReplayer.app/Frameworks/libGTLLVMShaderProfilerHelper.dylib](MACHOS/libGTLLVMShaderProfilerHelper.dylib.md)
- [/Applications/MTLReplayer.app/MTLReplayer](MACHOS/MTLReplayer.md)
- [/Applications/MailCompositionService.app/MailCompositionService](MACHOS/MailCompositionService.md)
- [/Applications/MediaRemoteUI.app/MediaRemoteUI](MACHOS/MediaRemoteUI.md)
- [/Applications/MediaRemoteUIService.app/MediaRemoteUIService](MACHOS/MediaRemoteUIService.md)
- [/Applications/MessagesViewService.app/MessagesViewService](MACHOS/MessagesViewService.md)
- [/Applications/MobilePhone.app/MobilePhone](MACHOS/MobilePhone.md)
- [/Applications/MobilePhone.app/PlugIns/VoicemailMessageNotificationExtension.appex/VoicemailMessageNotificationExtension](MACHOS/VoicemailMessageNotificationExtension.md)
- [/Applications/MobileReplayer.app/MobileReplayer](MACHOS/MobileReplayer.md)
- [/Applications/MobileReplayer.app/PlugIns/EAGLReplayControllerSupport.mrplugin/EAGLReplayControllerSupport](MACHOS/EAGLReplayControllerSupport.md)
- [/Applications/MobileSMS.app/Extensions/MessagesActionExtension.appex/MessagesActionExtension](MACHOS/MessagesActionExtension.md)
- [/Applications/MobileSMS.app/MobileSMS](MACHOS/MobileSMS.md)
- [/Applications/MobileSMS.app/PlugIns/MessagesAssistantExtension.appex/MessagesAssistantExtension](MACHOS/MessagesAssistantExtension.md)
- [/Applications/MobileSMS.app/PlugIns/MessagesAssistantUIExtension.appex/MessagesAssistantUIExtension](MACHOS/MessagesAssistantUIExtension.md)
- [/Applications/MobileSMS.app/PlugIns/MessagesNotificationExtension.appex/MessagesNotificationExtension](MACHOS/MessagesNotificationExtension.md)
- [/Applications/MobileSMS.app/PlugIns/MessagesPluginNotificationExtension.appex/MessagesPluginNotificationExtension](MACHOS/MessagesPluginNotificationExtension.md)
- [/Applications/MobileSMS.app/PlugIns/MessagesTranscriptExtension.appex/MessagesTranscriptExtension](MACHOS/MessagesTranscriptExtension.md)
- [/Applications/MobileSMS.app/PlugIns/MobileSMSSpotlightImporter.appex/MobileSMSSpotlightImporter](MACHOS/MobileSMSSpotlightImporter.md)
- [/Applications/MobileSafari.app/Extensions/SafariLinkExtension.appex/SafariLinkExtension](MACHOS/SafariLinkExtension.md)
- [/Applications/MobileSafari.app/Extensions/SafariWidgetExtension.appex/SafariWidgetExtension](MACHOS/SafariWidgetExtension.md)
- [/Applications/MobileSafari.app/MobileSafari](MACHOS/MobileSafari.md)
- [/Applications/MobileSafari.app/PlugIns/SafariWidgetExtension.appex/SafariWidgetExtension](MACHOS/SafariWidgetExtension.md)
- [/Applications/MobileSafari.app/PlugIns/com.apple.mobilesafari.SafariDiagnosticExtension.appex/com.apple.mobilesafari.SafariDiagnosticExtension](MACHOS/com.apple.mobilesafari.SafariDiagnosticExtension.md)
- [/Applications/MobileSafari.app/XPCServices/com.apple.Safari.SandboxBroker.xpc/com.apple.Safari.SandboxBroker](MACHOS/com.apple.Safari.SandboxBroker.md)
- [/Applications/MobileSlideShow.app/MobileSlideShow](MACHOS/MobileSlideShow.md)
- [/Applications/MobileSlideShow.app/PlugIns/PhotoPicker.appex/PhotoPicker](MACHOS/PhotoPicker.md)
- [/Applications/MobileSlideShow.app/PlugIns/PhotosDestructiveChangeConfirmation.appex/PhotosDestructiveChangeConfirmation](MACHOS/PhotosDestructiveChangeConfirmation.md)
- [/Applications/MobileSlideShow.app/PlugIns/PhotosFileProvider.appex/PhotosFileProvider](MACHOS/PhotosFileProvider.md)
- [/Applications/MobileSlideShow.app/PlugIns/PhotosMemoriesNotificationUpdates.appex/PhotosMemoriesNotificationUpdates](MACHOS/PhotosMemoriesNotificationUpdates.md)
- [/Applications/MobileSlideShow.app/PlugIns/PhotosMessagesApp.appex/PhotosMessagesApp](MACHOS/PhotosMessagesApp.md)
- [/Applications/MobileSlideShow.app/PlugIns/PhotosNotificationsUpdates.appex/PhotosNotificationsUpdates](MACHOS/PhotosNotificationsUpdates.md)
- [/Applications/MobileSlideShow.app/PlugIns/PhotosPicker.appex/PhotosPicker](MACHOS/PhotosPicker.md)
- [/Applications/MobileSlideShow.app/PlugIns/PhotosReliveWidget.appex/PhotosReliveWidget](MACHOS/PhotosReliveWidget.md)
- [/Applications/MobileSlideShow.app/PlugIns/PhotosReliveWidgetIntents.appex/PhotosReliveWidgetIntents](MACHOS/PhotosReliveWidgetIntents.md)
- [/Applications/MobileSlideShow.app/PlugIns/PhotosTCCNotificationExtension.appex/PhotosTCCNotificationExtension](MACHOS/PhotosTCCNotificationExtension.md)
- [/Applications/MobileSlideShow.app/PlugIns/com.apple.social.StreamShareService.appex/com.apple.social.StreamShareService](MACHOS/com.apple.social.StreamShareService.md)
- [/Applications/MomentsUIService.app/Frameworks/MomentsUIServiceCore.framework/MomentsUIServiceCore](MACHOS/MomentsUIServiceCore.md)
- [/Applications/MomentsUIService.app/MomentsUIService](MACHOS/MomentsUIService.md)
- [/Applications/MusicRecognition.app/MusicRecognition](MACHOS/MusicRecognition.md)
- [/Applications/MusicUIService.app/MusicUIService](MACHOS/MusicUIService.md)
- [/Applications/NewDeviceSetupUIService.app/NewDeviceSetupUIService](MACHOS/NewDeviceSetupUIService.md)
- [/Applications/PASViewService.app/PASViewService](MACHOS/PASViewService.md)
- [/Applications/PCViewService.app/PCViewService](MACHOS/PCViewService.md)
- [/Applications/PDUIApp.app/PDUIApp](MACHOS/PDUIApp.md)
- [/Applications/PaperBoard.app/PaperBoard](MACHOS/PaperBoard.md)
- [/Applications/PaperBoard.app/PlugIns/LegacyPoster.appex/LegacyPoster](MACHOS/LegacyPoster.md)
- [/Applications/PassbookSecureUIService.app/PassbookSecureUIService](MACHOS/PassbookSecureUIService.md)
- [/Applications/PassbookUISceneService.app/PassbookUISceneService](MACHOS/PassbookUISceneService.md)
- [/Applications/PassbookUIService.app/PassbookUIService](MACHOS/PassbookUIService.md)
- [/Applications/PassbookUIService.app/PlugIns/PeerPaymentMessagesExtension.appex/PeerPaymentMessagesExtension](MACHOS/PeerPaymentMessagesExtension.md)
- [/Applications/PeopleMessageService.app/Extensions/PeopleLegacyMessageService.appex/PeopleLegacyMessageService](MACHOS/PeopleLegacyMessageService.md)
- [/Applications/PeopleMessageService.app/PeopleMessageService](MACHOS/PeopleMessageService.md)
- [/Applications/PeopleMessageService.app/PlugIns/PeopleMessagesAskToBuy.appex/PeopleMessagesAskToBuy](MACHOS/PeopleMessagesAskToBuy.md)
- [/Applications/PeopleMessageService.app/PlugIns/PeopleMessagesScreenTime.appex/PeopleMessagesScreenTime](MACHOS/PeopleMessagesScreenTime.md)
- [/Applications/PeopleViewService.app/PeopleViewService](MACHOS/PeopleViewService.md)
- [/Applications/PeopleViewService.app/PlugIns/PeopleWidget_iOSExtension.appex/PeopleWidget_iOSExtension](MACHOS/PeopleWidget_iOSExtension.md)
- [/Applications/PeopleViewService.app/PlugIns/SelectPerson_iOS.appex/SelectPerson_iOS](MACHOS/SelectPerson_iOS.md)
- [/Applications/PhotosUIService.app/PhotosUIService](MACHOS/PhotosUIService.md)
- [/Applications/PosterBoard.app/PlugIns/WallpaperDiagnosticExtension.appex/WallpaperDiagnosticExtension](MACHOS/WallpaperDiagnosticExtension.md)
- [/Applications/PosterBoard.app/PosterBoard](MACHOS/PosterBoard.md)
- [/Applications/PreBoard.app/PreBoard](MACHOS/PreBoard.md)
- [/Applications/Preferences.app/Preferences](MACHOS/Preferences.md)
- [/Applications/PreviewShell.app/PreviewShell](MACHOS/PreviewShell.md)
- [/Applications/Print Center.app/Print Center](MACHOS/Print_Center.md)
- [/Applications/ProximityReaderUIService.app/ProximityReaderUIService](MACHOS/ProximityReaderUIService.md)
- [/Applications/RecoverDeviceUI.app/RecoverDeviceUI](MACHOS/RecoverDeviceUI.md)
- [/Applications/RemotePaymentPassActionsService.app/PlugIns/RemotePaymentPassActionsMessagesExtension.appex/RemotePaymentPassActionsMessagesExtension](MACHOS/RemotePaymentPassActionsMessagesExtension.md)
- [/Applications/RemotePaymentPassActionsService.app/RemotePaymentPassActionsService](MACHOS/RemotePaymentPassActionsService.md)
- [/Applications/RemoteiCloudQuotaUI.app/RemoteiCloudQuotaUI](MACHOS/RemoteiCloudQuotaUI.md)
- [/Applications/ReplayKitAngel.app/ReplayKitAngel](MACHOS/ReplayKitAngel.md)
- [/Applications/SIMSetupUIService.app/SIMSetupUIService](MACHOS/SIMSetupUIService.md)
- [/Applications/SLYahooAuth.app/PlugIns/SLYahooAuthService.appex/SLYahooAuthService](MACHOS/SLYahooAuthService.md)
- [/Applications/SLYahooAuth.app/SLYahooAuth](MACHOS/SLYahooAuth.md)
- [/Applications/SMS Filter.app/PlugIns/extensionFilter.appex/extensionFilter](MACHOS/extensionFilter.md)
- [/Applications/SMS Filter.app/SMS Filter](MACHOS/SMS_Filter.md)
- [/Applications/SOSBuddy.app/SOSBuddy](MACHOS/SOSBuddy.md)
- [/Applications/SafariViewService.app/SafariViewService](MACHOS/SafariViewService.md)
- [/Applications/SafetyMonitorApp.app/SafetyMonitorApp](MACHOS/SafetyMonitorApp.md)
- [/Applications/Screen Time.app/PlugIns/ScreenTimeWidgetExtension.appex/ScreenTimeWidgetExtension](MACHOS/ScreenTimeWidgetExtension.md)
- [/Applications/Screen Time.app/PlugIns/ScreenTimeWidgetIntentsExtension.appex/ScreenTimeWidgetIntentsExtension](MACHOS/ScreenTimeWidgetIntentsExtension.md)
- [/Applications/Screen Time.app/Screen Time](MACHOS/Screen_Time.md)
- [/Applications/ScreenSharingViewService.app/ScreenSharingViewService](MACHOS/ScreenSharingViewService.md)
- [/Applications/ScreenTimeUnlock.app/ScreenTimeUnlock](MACHOS/ScreenTimeUnlock.md)
- [/Applications/ScreenshotServicesService.app/ScreenshotServicesService](MACHOS/ScreenshotServicesService.md)
- [/Applications/Setup.app/Setup](MACHOS/Setup.md)
- [/Applications/SharedWebCredentialViewService.app/SharedWebCredentialViewService](MACHOS/SharedWebCredentialViewService.md)
- [/Applications/SharingUIService.app/SharingUIService](MACHOS/SharingUIService.md)
- [/Applications/SharingViewService.app/SharingViewService](MACHOS/SharingViewService.md)
- [/Applications/ShazamEventsApp.app/ShazamEventsApp](MACHOS/ShazamEventsApp.md)
- [/Applications/ShortcutsUI.app/ShortcutsUI](MACHOS/ShortcutsUI.md)
- [/Applications/ShortcutsViewService.app/ShortcutsViewService](MACHOS/ShortcutsViewService.md)
- [/Applications/Sidecar.app/PlugIns/ContinuityCamera.appex/ContinuityCamera](MACHOS/ContinuityCamera.md)
- [/Applications/Sidecar.app/PlugIns/ContinuityCapture.appex/ContinuityCapture](MACHOS/ContinuityCapture.md)
- [/Applications/Sidecar.app/PlugIns/ContinuityDisplay.appex/ContinuityDisplay](MACHOS/ContinuityDisplay.md)
- [/Applications/Sidecar.app/PlugIns/ContinuityMarkup.appex/ContinuityMarkup](MACHOS/ContinuityMarkup.md)
- [/Applications/Sidecar.app/PlugIns/ContinuitySignature.appex/ContinuitySignature](MACHOS/ContinuitySignature.md)
- [/Applications/Sidecar.app/PlugIns/ContinuitySketch.appex/ContinuitySketch](MACHOS/ContinuitySketch.md)
- [/Applications/Sidecar.app/Sidecar](MACHOS/Sidecar.md)
- [/Applications/Siri.app/Siri](MACHOS/Siri.md)
- [/Applications/SleepLockScreen.app/SleepLockScreen](MACHOS/SleepLockScreen.md)
- [/Applications/SleepWidgetContainer.app/PlugIns/SleepWidgetExtension.appex/SleepWidgetExtension](MACHOS/SleepWidgetExtension.md)
- [/Applications/SleepWidgetContainer.app/SleepWidgetContainer](MACHOS/SleepWidgetContainer.md)
- [/Applications/SoftwareUpdateUIService.app/PlugIns/SUSUIVerifyingAlertCFUserNotificationUIExtension.appex/SUSUIVerifyingAlertCFUserNotificationUIExtension](MACHOS/SUSUIVerifyingAlertCFUserNotificationUIExtension.md)
- [/Applications/SoftwareUpdateUIService.app/PlugIns/SUSUInstallAlertCFUserNotificationUIExtension.appex/SUSUInstallAlertCFUserNotificationUIExtension](MACHOS/SUSUInstallAlertCFUserNotificationUIExtension.md)
- [/Applications/SoftwareUpdateUIService.app/SoftwareUpdateUIService](MACHOS/SoftwareUpdateUIService.md)
- [/Applications/Spotlight.app/Spotlight](MACHOS/Spotlight.md)
- [/Applications/SpringBoardEducation.app/SpringBoardEducation](MACHOS/SpringBoardEducation.md)
- [/Applications/StickersUltra.app/PlugIns/StickersUltraExtension.appex/StickersUltraExtension](MACHOS/StickersUltraExtension.md)
- [/Applications/StickersUltra.app/StickersUltra](MACHOS/StickersUltra.md)
- [/Applications/StoreDemoViewService.app/StoreDemoViewService](MACHOS/StoreDemoViewService.md)
- [/Applications/StoreKitUIService.app/StoreKitUIService](MACHOS/StoreKitUIService.md)
- [/Applications/SubcredentialUIService.app/PlugIns/SubcredentialInvitationMessagesExtension.appex/SubcredentialInvitationMessagesExtension](MACHOS/SubcredentialInvitationMessagesExtension.md)
- [/Applications/SubcredentialUIService.app/SubcredentialUIService](MACHOS/SubcredentialUIService.md)
- [/Applications/SystemPaperViewService.app/SystemPaperViewService](MACHOS/SystemPaperViewService.md)
- [/Applications/TDGSharingViewService.app/TDGSharingViewService](MACHOS/TDGSharingViewService.md)
- [/Applications/TVAccessViewService.app/TVAccessViewService](MACHOS/TVAccessViewService.md)
- [/Applications/TVRemoteUIService.app/PlugIns/TVRemoteIntentExtension.appex/TVRemoteIntentExtension](MACHOS/TVRemoteIntentExtension.md)
- [/Applications/TVRemoteUIService.app/TVRemoteUIService](MACHOS/TVRemoteUIService.md)
- [/Applications/TVSetupUIService.app/TVSetupUIService](MACHOS/TVSetupUIService.md)
- [/Applications/TrustMe.app/TrustMe](MACHOS/TrustMe.md)
- [/Applications/VideoSubscriberAccountViewService.app/VideoSubscriberAccountViewService](MACHOS/VideoSubscriberAccountViewService.md)
- [/Applications/Web.app/Web](MACHOS/Web.md)
- [/Applications/WebContentAnalysisUI.app/WebContentAnalysisUI](MACHOS/WebContentAnalysisUI.md)
- [/Applications/WebSheet.app/WebSheet](MACHOS/WebSheet.md)
- [/Applications/WidgetRenderer_CarPlay.app/WidgetRenderer_CarPlay](MACHOS/WidgetRenderer_CarPlay.md)
- [/Applications/WidgetRenderer_Default.app/WidgetRenderer_Default](MACHOS/WidgetRenderer_Default.md)
- [/Applications/WorkoutRemoteViewService.app/WorkoutRemoteViewService](MACHOS/WorkoutRemoteViewService.md)
- [/Applications/iCloud+.app/iCloud+](MACHOS/iCloud+.md)
- [/Applications/iCloud.app/iCloud](MACHOS/iCloud.md)
- [/Applications/iMessageAppsViewService.app/iMessageAppsViewService](MACHOS/iMessageAppsViewService.md)
- [/Library/Audio/Plug-Ins/HAL/VirtualAudio.plugin/VirtualAudio](MACHOS/VirtualAudio.md)
- [/System/Applications/Family/InviteMessageBubbleExtension.appex/InviteMessageBubbleExtension](MACHOS/InviteMessageBubbleExtension.md)
- [/System/DriverKit/System/Library/PrivateFrameworks/BroadcomWLANDriverKit.framework/BroadcomWLANDriverKit](MACHOS/BroadcomWLANDriverKit.md)
- [/System/DriverKit/usr/lib/libSystem_debug.dylib](MACHOS/libSystem_debug.dylib.md)
- [/System/DriverKit/usr/lib/system/libdispatch_debug.dylib](MACHOS/libdispatch_debug.dylib.md)
- [/System/DriverKit/usr/lib/system/libdispatch_profile.dylib](MACHOS/libdispatch_profile.dylib.md)
- [/System/DriverKit/usr/lib/system/libsystem_blocks_debug.dylib](MACHOS/libsystem_blocks_debug.dylib.md)
- [/System/DriverKit/usr/lib/system/libsystem_blocks_profile.dylib](MACHOS/libsystem_blocks_profile.dylib.md)
- [/System/DriverKit/usr/lib/system/libsystem_c_debug.dylib](MACHOS/libsystem_c_debug.dylib.md)
- [/System/DriverKit/usr/lib/system/libsystem_malloc_debug.dylib](MACHOS/libsystem_malloc_debug.dylib.md)
- [/System/DriverKit/usr/lib/system/libsystem_platform_debug.dylib](MACHOS/libsystem_platform_debug.dylib.md)
- [/System/DriverKit/usr/lib/system/libsystem_pthread_debug.dylib](MACHOS/libsystem_pthread_debug.dylib.md)
- [/System/DriverKit/usr/lib/system/libsystem_trace_debug.dylib](MACHOS/libsystem_trace_debug.dylib.md)
- [/System/Library/AccessibilityBundles/AXAggregateStatisticsServer.axuiservice/AXAggregateStatisticsServer](MACHOS/AXAggregateStatisticsServer.md)
- [/System/Library/AccessibilityBundles/AXAssetAndDataServer.axuiservice/AXAssetAndDataServer](MACHOS/AXAssetAndDataServer.md)
- [/System/Library/AccessibilityBundles/AXAuditAXUIService.axuiservice/AXAuditAXUIService](MACHOS/AXAuditAXUIService.md)
- [/System/Library/AccessibilityBundles/AXBannerUIServer.axuiservice/AXBannerUIServer](MACHOS/AXBannerUIServer.md)
- [/System/Library/AccessibilityBundles/AXBuddyBundle.bundle/AXBuddyBundle](MACHOS/AXBuddyBundle.md)
- [/System/Library/AccessibilityBundles/AXContainerManagerServer.axuiservice/AXContainerManagerServer](MACHOS/AXContainerManagerServer.md)
- [/System/Library/AccessibilityBundles/AXElementInteractionUIServer.axuiservice/AXElementInteractionUIServer](MACHOS/AXElementInteractionUIServer.md)
- [/System/Library/AccessibilityBundles/AXIDSServer.axuiservice/AXIDSServer](MACHOS/AXIDSServer.md)
- [/System/Library/AccessibilityBundles/AXLocalizationCaptionServer.axuiservice/AXLocalizationCaptionServer](MACHOS/AXLocalizationCaptionServer.md)
- [/System/Library/AccessibilityBundles/AXUltronPluginService.axuiservice/AXUltronPluginService](MACHOS/AXUltronPluginService.md)
- [/System/Library/AccessibilityBundles/AXWatchRemoteScreenUIServer.axuiservice/AXWatchRemoteScreenUIServer](MACHOS/AXWatchRemoteScreenUIServer.md)
- [/System/Library/AccessibilityBundles/ActivityAchievementsUI.axbundle/ActivityAchievementsUI](MACHOS/ActivityAchievementsUI.md)
- [/System/Library/AccessibilityBundles/ActivityBridgeSetup.axbundle/ActivityBridgeSetup](MACHOS/ActivityBridgeSetup.md)
- [/System/Library/AccessibilityBundles/ActivityRingsUI.axbundle/ActivityRingsUI](MACHOS/ActivityRingsUI.md)
- [/System/Library/AccessibilityBundles/ActivitySharing.axbundle/ActivitySharing](MACHOS/ActivitySharing.md)
- [/System/Library/AccessibilityBundles/ActivitySharingUI.axbundle/ActivitySharingUI](MACHOS/ActivitySharingUI.md)
- [/System/Library/AccessibilityBundles/AssistiveTouch.axuiservice/AssistiveTouch](MACHOS/AssistiveTouch.md)
- [/System/Library/AccessibilityBundles/BackTapUIServer.axuiservice/BackTapUIServer](MACHOS/BackTapUIServer.md)
- [/System/Library/AccessibilityBundles/ClarityUIServer.axuiservice/ClarityUIServer](MACHOS/ClarityUIServer.md)
- [/System/Library/AccessibilityBundles/ClockAngel.axbundle/ClockAngel](MACHOS/ClockAngel.md)
- [/System/Library/AccessibilityBundles/DisplayFilterUIServer.axuiservice/DisplayFilterUIServer](MACHOS/DisplayFilterUIServer.md)
- [/System/Library/AccessibilityBundles/FitnessApp.axbundle/FitnessApp](MACHOS/FitnessApp.md)
- [/System/Library/AccessibilityBundles/FitnessUI.axbundle/FitnessUI](MACHOS/FitnessUI.md)
- [/System/Library/AccessibilityBundles/GAXBackboardServer.bundle/GAXBackboardServer](MACHOS/GAXBackboardServer.md)
- [/System/Library/AccessibilityBundles/GAXClient.bundle/GAXClient](MACHOS/GAXClient.md)
- [/System/Library/AccessibilityBundles/GAXSpringboardServer.bundle/GAXSpringboardServer](MACHOS/GAXSpringboardServer.md)
- [/System/Library/AccessibilityBundles/GuidedAccess.axuiservice/GuidedAccess](MACHOS/GuidedAccess.md)
- [/System/Library/AccessibilityBundles/HoverTextUIServer.axuiservice/HoverTextUIServer](MACHOS/HoverTextUIServer.md)
- [/System/Library/AccessibilityBundles/InvertColorsManager.bundle/InvertColorsManager](MACHOS/InvertColorsManager.md)
- [/System/Library/AccessibilityBundles/LiveSpeechUIService.axuiservice/LiveSpeechUIService](MACHOS/LiveSpeechUIService.md)
- [/System/Library/AccessibilityBundles/NTKCustomization.axbundle/NTKCustomization](MACHOS/NTKCustomization.md)
- [/System/Library/AccessibilityBundles/NTKUltraCubeFaceBundleCompanion.axbundle/NTKUltraCubeFaceBundleCompanion](MACHOS/NTKUltraCubeFaceBundleCompanion.md)
- [/System/Library/AccessibilityBundles/NanoMailBridgeSettings.axbundle/NanoMailBridgeSettings](MACHOS/NanoMailBridgeSettings.md)
- [/System/Library/AccessibilityBundles/NanoMediaBridgeUI.axbundle/NanoMediaBridgeUI](MACHOS/NanoMediaBridgeUI.md)
- [/System/Library/AccessibilityBundles/NanoPeopleBridgeSettings.axbundle/NanoPeopleBridgeSettings](MACHOS/NanoPeopleBridgeSettings.md)
- [/System/Library/AccessibilityBundles/NanoTimeKitCompanion.axbundle/NanoTimeKitCompanion](MACHOS/NanoTimeKitCompanion.md)
- [/System/Library/AccessibilityBundles/PingMyWatchControlCenterUI.axbundle/PingMyWatchControlCenterUI](MACHOS/PingMyWatchControlCenterUI.md)
- [/System/Library/AccessibilityBundles/SchoolTimeSettingsUI.axbundle/SchoolTimeSettingsUI](MACHOS/SchoolTimeSettingsUI.md)
- [/System/Library/AccessibilityBundles/ScreenSharing.axuiservice/ScreenSharing](MACHOS/ScreenSharing.md)
- [/System/Library/AccessibilityBundles/SiriSetup.axbundle/SiriSetup](MACHOS/SiriSetup.md)
- [/System/Library/AccessibilityBundles/SpeakServer.axuiservice/SpeakServer](MACHOS/SpeakServer.md)
- [/System/Library/AccessibilityBundles/SpeakThis.axuiservice/SpeakThis](MACHOS/SpeakThis.md)
- [/System/Library/AccessibilityBundles/StickyKeys.axuiservice/StickyKeys](MACHOS/StickyKeys.md)
- [/System/Library/AccessibilityBundles/TouchAccommodations.axuiservice/TouchAccommodations](MACHOS/TouchAccommodations.md)
- [/System/Library/AccessibilityBundles/VisualAlerts.bundle/VisualAlerts](MACHOS/VisualAlerts.md)
- [/System/Library/AccessibilityBundles/VoiceOver.axuiservice/VoiceOver](MACHOS/VoiceOver.md)
- [/System/Library/AccessibilityBundles/WidgetRenderer.axbundle/WidgetRenderer](MACHOS/WidgetRenderer.md)
- [/System/Library/AccessibilityBundles/ZoomWindow.axuiservice/ZoomWindow](MACHOS/ZoomWindow.md)
- [/System/Library/AccessibilityBundles/activity-widget.axbundle/activity-widget](MACHOS/activity-widget.md)
- [/System/Library/AccessibilityBundles/com.apple.NanoTimeKit.CreateWatchFace.axbundle/com.apple.NanoTimeKit.CreateWatchFace](MACHOS/com.apple.NanoTimeKit.CreateWatchFace.md)
- [/System/Library/Accounts/AppleIDLoginPlugins/FMFAppleIDLoginPlugin.bundle/FMFAppleIDLoginPlugin](MACHOS/FMFAppleIDLoginPlugin.md)
- [/System/Library/Accounts/AppleIDLoginPlugins/FaceTimeAppleIDLoginPlugin.bundle/FaceTimeAppleIDLoginPlugin](MACHOS/FaceTimeAppleIDLoginPlugin.md)
- [/System/Library/Accounts/AppleIDLoginPlugins/GameCenterAppleIDLoginPlugin.bundle/GameCenterAppleIDLoginPlugin](MACHOS/GameCenterAppleIDLoginPlugin.md)
- [/System/Library/Accounts/AppleIDLoginPlugins/ISLoginPlugin.bundle/ISLoginPlugin](MACHOS/ISLoginPlugin.md)
- [/System/Library/Accounts/AppleIDLoginPlugins/MadridAppleIDLoginPlugin.bundle/MadridAppleIDLoginPlugin](MACHOS/MadridAppleIDLoginPlugin.md)
- [/System/Library/Accounts/AppleIDLoginPlugins/iCloudAppleIDLoginPlugin.bundle/iCloudAppleIDLoginPlugin](MACHOS/iCloudAppleIDLoginPlugin.md)
- [/System/Library/Accounts/Authentication/AAGKAuthenticationPlugin.bundle/AAGKAuthenticationPlugin](MACHOS/AAGKAuthenticationPlugin.md)
- [/System/Library/Accounts/Authentication/AAIDSAuthenticationPlugin.bundle/AAIDSAuthenticationPlugin](MACHOS/AAIDSAuthenticationPlugin.md)
- [/System/Library/Accounts/Authentication/AMSAccountAuthenticationPlugin.bundle/AMSAccountAuthenticationPlugin](MACHOS/AMSAccountAuthenticationPlugin.md)
- [/System/Library/Accounts/Authentication/AppleIDAuthenticationDelegates/AppleAccountAuthenticationDelegate.bundle/AppleAccountAuthenticationDelegate](MACHOS/AppleAccountAuthenticationDelegate.md)
- [/System/Library/Accounts/Authentication/AppleIDAuthenticationDelegates/GameCenterAppleIDAuthenticationDelegate.bundle/GameCenterAppleIDAuthenticationDelegate](MACHOS/GameCenterAppleIDAuthenticationDelegate.md)
- [/System/Library/Accounts/Authentication/AppleIDAuthenticationDelegates/IDSAuthenticationDelegatePlugin.bundle/IDSAuthenticationDelegatePlugin](MACHOS/IDSAuthenticationDelegatePlugin.md)
- [/System/Library/Accounts/Authentication/AppleIDAuthenticationDelegates/SOSCCAuthPlugin.bundle/SOSCCAuthPlugin](MACHOS/SOSCCAuthPlugin.md)
- [/System/Library/Accounts/DataclassOwners/Bookmarks.bundle/Bookmarks](MACHOS/Bookmarks.md)
- [/System/Library/Accounts/DataclassOwners/Calendar.bundle/Calendar](MACHOS/Calendar.md)
- [/System/Library/Accounts/DataclassOwners/CloudDocsDataclassOwnerPlugin.bundle/CloudDocsDataclassOwnerPlugin](MACHOS/CloudDocsDataclassOwnerPlugin.md)
- [/System/Library/Accounts/DataclassOwners/ContactsDataclassOwner.bundle/ContactsDataclassOwner](MACHOS/ContactsDataclassOwner.md)
- [/System/Library/Accounts/DataclassOwners/FreeformDataclassOwner.bundle/FreeformDataclassOwner](MACHOS/FreeformDataclassOwner.md)
- [/System/Library/Accounts/DataclassOwners/HealthDataclassOwnerPlugin.bundle/HealthDataclassOwnerPlugin](MACHOS/HealthDataclassOwnerPlugin.md)
- [/System/Library/Accounts/DataclassOwners/JournalDataclassOwner.bundle/JournalDataclassOwner](MACHOS/JournalDataclassOwner.md)
- [/System/Library/Accounts/DataclassOwners/KeychainDataclassOwner.bundle/KeychainDataclassOwner](MACHOS/KeychainDataclassOwner.md)
- [/System/Library/Accounts/DataclassOwners/MessagesDataclassOwner.bundle/MessagesDataclassOwner](MACHOS/MessagesDataclassOwner.md)
- [/System/Library/Accounts/DataclassOwners/News.bundle/News](MACHOS/News.md)
- [/System/Library/Accounts/DataclassOwners/Notes.bundle/Notes](MACHOS/Notes.md)
- [/System/Library/Accounts/DataclassOwners/RemindersDataclassOwnerPlugin.bundle/RemindersDataclassOwnerPlugin](MACHOS/RemindersDataclassOwnerPlugin.md)
- [/System/Library/Accounts/DataclassOwners/SiriDataclassOwner.bundle/SiriDataclassOwner](MACHOS/SiriDataclassOwner.md)
- [/System/Library/Accounts/DataclassOwners/StocksDataclassOwner.bundle/StocksDataclassOwner](MACHOS/StocksDataclassOwner.md)
- [/System/Library/Accounts/Notification/ASDAccountNotificationPlugin.bundle/ASDAccountNotificationPlugin](MACHOS/ASDAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/AccountNotificationPlugin.bundle/AccountNotificationPlugin](MACHOS/AccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/AccountSuggestionNotificationPlugin.bundle/AccountSuggestionNotificationPlugin](MACHOS/AccountSuggestionNotificationPlugin.md)
- [/System/Library/Accounts/Notification/CloudBookmarksAccountsNotifier.bundle/CloudBookmarksAccountsNotifier](MACHOS/CloudBookmarksAccountsNotifier.md)
- [/System/Library/Accounts/Notification/CloudDocsAccountNotificationPlugin.bundle/CloudDocsAccountNotificationPlugin](MACHOS/CloudDocsAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/CoreAccessoriesAccountNotificationPlugin.bundle/CoreAccessoriesAccountNotificationPlugin](MACHOS/CoreAccessoriesAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/DeviceManagementClientAccountNotificationPlugin.bundle/DeviceManagementClientAccountNotificationPlugin](MACHOS/DeviceManagementClientAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/GroupKitAccountNotification.bundle/GroupKitAccountNotification](MACHOS/GroupKitAccountNotification.md)
- [/System/Library/Accounts/Notification/MBPrebuddyAccountNotificationPlugin.bundle/MBPrebuddyAccountNotificationPlugin](MACHOS/MBPrebuddyAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/MCAccountNotificationPlugin.bundle/MCAccountNotificationPlugin](MACHOS/MCAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/NDOAccountNotificationPlugin.bundle/NDOAccountNotificationPlugin](MACHOS/NDOAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/NanoMailAccountNotificationPlugin.bundle/NanoMailAccountNotificationPlugin](MACHOS/NanoMailAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/NanoPassbookAccountNotificationPlugin.bundle/NanoPassbookAccountNotificationPlugin](MACHOS/NanoPassbookAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/RemoteManagementAccountNotificationPlugin.bundle/RemoteManagementAccountNotificationPlugin](MACHOS/RemoteManagementAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/SyncedDefaultsAccountNotificationPlugin.bundle/SyncedDefaultsAccountNotificationPlugin](MACHOS/SyncedDefaultsAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/TransparencyAccountNotification.bundle/TransparencyAccountNotification](MACHOS/TransparencyAccountNotification.md)
- [/System/Library/Accounts/Notification/iTunesAccountsNotificationPlugin.bundle/iTunesAccountsNotificationPlugin](MACHOS/iTunesAccountsNotificationPlugin.md)
- [/System/Library/Accounts/ServiceOwners/AACloudServiceOwner.bundle/AACloudServiceOwner](MACHOS/AACloudServiceOwner.md)
- [/System/Library/Accounts/ServiceOwners/AMSMediaServiceOwner.bundle/AMSMediaServiceOwner](MACHOS/AMSMediaServiceOwner.md)
- [/System/Library/Accounts/ServiceOwners/GCCloudServiceOwner.bundle/GCCloudServiceOwner](MACHOS/GCCloudServiceOwner.md)
- [/System/Library/Accounts/ServiceOwners/IDSServiceOwner.bundle/IDSServiceOwner](MACHOS/IDSServiceOwner.md)
- [/System/Library/AppRemovalServices/com.apple.Bridge.appremoval.xpc/com.apple.Bridge.appremoval](MACHOS/com.apple.Bridge.appremoval.md)
- [/System/Library/AppRemovalServices/com.apple.Home.appremoval.xpc/com.apple.Home.appremoval](MACHOS/com.apple.Home.appremoval.md)
- [/System/Library/AppRemovalServices/com.apple.Maps.appremoval.xpc/com.apple.Maps.appremoval](MACHOS/com.apple.Maps.appremoval.md)
- [/System/Library/AppRemovalServices/com.apple.MobileStore.appremoval.xpc/com.apple.MobileStore.appremoval](MACHOS/com.apple.MobileStore.appremoval.md)
- [/System/Library/AppRemovalServices/com.apple.Translate.appremoval.xpc/com.apple.Translate.appremoval](MACHOS/com.apple.Translate.appremoval.md)
- [/System/Library/AppRemovalServices/com.apple.VoiceMemos.appremoval.xpc/com.apple.VoiceMemos.appremoval](MACHOS/com.apple.VoiceMemos.appremoval.md)
- [/System/Library/AppRemovalServices/com.apple.freeform.appremoval.xpc/com.apple.freeform.appremoval](MACHOS/com.apple.freeform.appremoval.md)
- [/System/Library/AppRemovalServices/com.apple.iBooks.appremoval.xpc/com.apple.iBooks.appremoval](MACHOS/com.apple.iBooks.appremoval.md)
- [/System/Library/AppRemovalServices/com.apple.mobilecal.appremoval.xpc/com.apple.mobilecal.appremoval](MACHOS/com.apple.mobilecal.appremoval.md)
- [/System/Library/AppRemovalServices/com.apple.mobilemail.appremoval.xpc/com.apple.mobilemail.appremoval](MACHOS/com.apple.mobilemail.appremoval.md)
- [/System/Library/AppRemovalServices/com.apple.mobilenotes.appremoval.xpc/com.apple.mobilenotes.appremoval](MACHOS/com.apple.mobilenotes.appremoval.md)
- [/System/Library/AppRemovalServices/com.apple.news.appremoval.xpc/com.apple.news](MACHOS/com.apple.news.md)
- [/System/Library/AppRemovalServices/com.apple.podcasts.appremoval.xpc/com.apple.podcasts.appremoval](MACHOS/com.apple.podcasts.appremoval.md)
- [/System/Library/AppRemovalServices/com.apple.shortcuts.appremoval.xpc/com.apple.shortcuts.appremoval](MACHOS/com.apple.shortcuts.appremoval.md)
- [/System/Library/AppRemovalServices/com.apple.tv.appremoval.xpc/com.apple.tv.appremoval](MACHOS/com.apple.tv.appremoval.md)
- [/System/Library/AppRemovalServices/com.apple.weather.appremoval.xpc/com.apple.weather.appremoval](MACHOS/com.apple.weather.appremoval.md)
- [/System/Library/AppleMediaServices/DynamicUI/PlugIns/CoreDynamicUIPlugin.bundle/CoreDynamicUIPlugin](MACHOS/CoreDynamicUIPlugin.md)
- [/System/Library/AppleMediaServices/DynamicUI/PlugIns/StoreDynamicUIPlugin.bundle/StoreDynamicUIPlugin](MACHOS/StoreDynamicUIPlugin.md)
- [/System/Library/AppleMediaServices/WebUI/PlugIns/MusicAMSUIWebPlugin.bundle/MusicAMSUIWebPlugin](MACHOS/MusicAMSUIWebPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/AlarmFlowPlugin.bundle/AlarmFlowPlugin](MACHOS/AlarmFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/AppLaunchPlugin.bundle/AppLaunchPlugin](MACHOS/AppLaunchPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/AudioFlowDelegatePlugin](MACHOS/AudioFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/CAMRootFlowPlugin.bundle/CAMRootFlowPlugin](MACHOS/CAMRootFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/CalendarFlowDelegatePlugin.bundle/CalendarFlowDelegatePlugin](MACHOS/CalendarFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/CarCommandsFlowDelegatePlugin.bundle/CarCommandsFlowDelegatePlugin](MACHOS/CarCommandsFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/ClockFlowPlugin.bundle/ClockFlowPlugin](MACHOS/ClockFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/ContactsFlowDelegatePlugin.bundle/ContactsFlowDelegatePlugin](MACHOS/ContactsFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/ControlsFlowDelegatePlugin.bundle/ControlsFlowDelegatePlugin](MACHOS/ControlsFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/DailyBriefingFlowPlugin.bundle/DailyBriefingFlowPlugin](MACHOS/DailyBriefingFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/EdutainmentFlowPlugin.bundle/EdutainmentFlowPlugin](MACHOS/EdutainmentFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/EmergencyFlowPlugin.bundle/EmergencyFlowPlugin](MACHOS/EmergencyFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/FindMyFlowPlugin.bundle/FindMyFlowPlugin](MACHOS/FindMyFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/GeoFlowDelegatePlugin.bundle/GeoFlowDelegatePlugin](MACHOS/GeoFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/HealthFlowDelegatePlugin.bundle/HealthFlowDelegatePlugin](MACHOS/HealthFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/HomeAutomationFlowDelegatePlugin.bundle/HomeAutomationFlowDelegatePlugin](MACHOS/HomeAutomationFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/HomeCommunicationFlowDelegatePlugin.bundle/HomeCommunicationFlowDelegatePlugin](MACHOS/HomeCommunicationFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/IdentityFlowPlugin.bundle/IdentityFlowPlugin](MACHOS/IdentityFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/InformationFlowPlugin](MACHOS/InformationFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/MailFlowDelegatePlugin.bundle/MailFlowDelegatePlugin](MACHOS/MailFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/MessagesFlowDelegatePlugin.bundle/MessagesFlowDelegatePlugin](MACHOS/MessagesFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/NotebookFlowPlugin.bundle/NotebookFlowPlugin](MACHOS/NotebookFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/NotificationsFlowDelegatePlugin.bundle/NotificationsFlowDelegatePlugin](MACHOS/NotificationsFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/PaymentsFlowDelegatePlugin.bundle/PaymentsFlowDelegatePlugin](MACHOS/PaymentsFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/PhoneCallFlowDelegatePlugin](MACHOS/PhoneCallFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/ReaderFlowPlugin.bundle/ReaderFlowPlugin](MACHOS/ReaderFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SafetySessionFlowPlugin.bundle/SafetySessionFlowPlugin](MACHOS/SafetySessionFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SettingsFlowDelegatePlugin.bundle/SettingsFlowDelegatePlugin](MACHOS/SettingsFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SiriLinkFlowPlugin.bundle/SiriLinkFlowPlugin](MACHOS/SiriLinkFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SiriSuggestionsFlowPlugin.bundle/SiriSuggestionsFlowPlugin](MACHOS/SiriSuggestionsFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/SocialConversationFlowDelegatePlugin](MACHOS/SocialConversationFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SystemCommandsFlowDelegatePlugin.bundle/SystemCommandsFlowDelegatePlugin](MACHOS/SystemCommandsFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/TimerFlowDelegatePlugin.bundle/TimerFlowDelegatePlugin](MACHOS/TimerFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/TranslationFlowDelegatePlugin.bundle/TranslationFlowDelegatePlugin](MACHOS/TranslationFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/VideoFlowDelegatePlugin.bundle/VideoFlowDelegatePlugin](MACHOS/VideoFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/WellnessFlowPlugin](MACHOS/WellnessFlowPlugin.md)
- [/System/Library/Assistant/Plugins/Accessibility.assistantBundle/Accessibility](MACHOS/Accessibility.md)
- [/System/Library/Assistant/Plugins/Applications.assistantBundle/Applications](MACHOS/Applications.md)
- [/System/Library/Assistant/Plugins/ChatKitAssistant.assistantBundle/ChatKitAssistant](MACHOS/ChatKitAssistant.md)
- [/System/Library/Assistant/Plugins/DeviceControl.assistantBundle/DeviceControl](MACHOS/DeviceControl.md)
- [/System/Library/Assistant/Plugins/DoNotDisturbAssistant.assistantBundle/DoNotDisturbAssistant](MACHOS/DoNotDisturbAssistant.md)
- [/System/Library/Assistant/Plugins/Mail.assistantBundle/Mail](MACHOS/Mail.md)
- [/System/Library/Assistant/Plugins/Maps.assistantBundle/Maps](MACHOS/Maps.md)
- [/System/Library/Assistant/Plugins/MobileTimer.assistantBundle/MobileTimer](MACHOS/MobileTimer.md)
- [/System/Library/Assistant/Plugins/NanoAppSync.assistantBundle/NanoAppSync](MACHOS/NanoAppSync.md)
- [/System/Library/Assistant/Plugins/NotificationsSettingsAssistant.assistantBundle/NotificationsSettingsAssistant](MACHOS/NotificationsSettingsAssistant.md)
- [/System/Library/Assistant/Plugins/ParsecContextSync.assistantBundle/ParsecContextSync](MACHOS/ParsecContextSync.md)
- [/System/Library/Assistant/Plugins/ParsecSubscriptionServiceSync.assistantBundle/ParsecSubscriptionServiceSync](MACHOS/ParsecSubscriptionServiceSync.md)
- [/System/Library/Assistant/Plugins/PreferencesAssistant.assistantBundle/PreferencesAssistant](MACHOS/PreferencesAssistant.md)
- [/System/Library/Assistant/Plugins/Safari.assistantBundle/Safari](MACHOS/Safari.md)
- [/System/Library/Assistant/Plugins/SiriFindMyBundle.assistantBundle/SiriFindMyBundle](MACHOS/SiriFindMyBundle.md)
- [/System/Library/Assistant/Plugins/SiriPrivateLearningAnalytics.assistantBundle/SiriPrivateLearningAnalytics](MACHOS/SiriPrivateLearningAnalytics.md)
- [/System/Library/Assistant/Plugins/Social.assistantBundle/Social](MACHOS/Social.md)
- [/System/Library/Assistant/Plugins/Stocks.assistantBundle/Stocks](MACHOS/Stocks.md)
- [/System/Library/Assistant/Plugins/UILite.assistantBundle/UILite](MACHOS/UILite.md)
- [/System/Library/Assistant/Plugins/WatchListAssistant.assistantBundle/WatchListAssistant](MACHOS/WatchListAssistant.md)
- [/System/Library/Assistant/Plugins/WebSearch.assistantBundle/WebSearch](MACHOS/WebSearch.md)
- [/System/Library/Assistant/Plugins/activity.assistantBundle/activity](MACHOS/activity.md)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriPrivateLearningInferencePlugin.bundle/SiriPrivateLearningInferencePlugin](MACHOS/SiriPrivateLearningInferencePlugin.md)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriPrivateLearningPatternExtractionPlugin.bundle/SiriPrivateLearningPatternExtractionPlugin](MACHOS/SiriPrivateLearningPatternExtractionPlugin.md)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriPrivateLearningTTSMispronunciationPlugin.bundle/SiriPrivateLearningTTSMispronunciationPlugin](MACHOS/SiriPrivateLearningTTSMispronunciationPlugin.md)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriReferenceResolutionMetricsPlugin.bundle/SiriReferenceResolutionMetricsPlugin](MACHOS/SiriReferenceResolutionMetricsPlugin.md)
- [/System/Library/Assistant/Suggestions/InferenceBridge/SiriSuggestionsInferenceBridge.bundle/SiriSuggestionsInferenceBridge](MACHOS/SiriSuggestionsInferenceBridge.md)
- [/System/Library/Assistant/Suggestions/SKEBridge/SiriSuggestionsSKEBridge.bundle/SiriSuggestionsSKEBridge](MACHOS/SiriSuggestionsSKEBridge.md)
- [/System/Library/Assistant/UIPlugins/AcousticId.siriUIBundle/AcousticId](MACHOS/AcousticId.md)
- [/System/Library/Assistant/UIPlugins/AddressBook.siriUIBundle/AddressBook](MACHOS/AddressBook.md)
- [/System/Library/Assistant/UIPlugins/Calendar.siriUIBundle/Calendar](MACHOS/Calendar.md)
- [/System/Library/Assistant/UIPlugins/GeneralKnowledge.siriUIBundle/GeneralKnowledge](MACHOS/GeneralKnowledge.md)
- [/System/Library/Assistant/UIPlugins/Intents.siriUIBundle/Intents](MACHOS/Intents.md)
- [/System/Library/Assistant/UIPlugins/Mail.siriUIBundle/Mail](MACHOS/Mail.md)
- [/System/Library/Assistant/UIPlugins/Maps.siriUIBundle/Maps](MACHOS/Maps.md)
- [/System/Library/Assistant/UIPlugins/MobileTimer.siriUIBundle/MobileTimer](MACHOS/MobileTimer.md)
- [/System/Library/Assistant/UIPlugins/Notes.siriUIBundle/Notes](MACHOS/Notes.md)
- [/System/Library/Assistant/UIPlugins/Notifications.siriUIBundle/Notifications](MACHOS/Notifications.md)
- [/System/Library/Assistant/UIPlugins/RemindersSiriUIPlugin.siriUIBundle/RemindersSiriUIPlugin](MACHOS/RemindersSiriUIPlugin.md)
- [/System/Library/Assistant/UIPlugins/Settings.siriUIBundle/Settings](MACHOS/Settings.md)
- [/System/Library/Assistant/UIPlugins/SiriFindMyUIPlugin.siriUIBundle/SiriFindMyUIPlugin](MACHOS/SiriFindMyUIPlugin.md)
- [/System/Library/Assistant/UIPlugins/Stocks.siriUIBundle/Stocks](MACHOS/Stocks.md)
- [/System/Library/Assistant/UIPlugins/System.siriUIBundle/System](MACHOS/System.md)
- [/System/Library/Assistant/UIPlugins/UniversalSearch.siriUIBundle/UniversalSearch](MACHOS/UniversalSearch.md)
- [/System/Library/Assistant/UIPlugins/WAAnswer.siriUIBundle/WAAnswer](MACHOS/WAAnswer.md)
- [/System/Library/Audio/MIDI Drivers/AppleIDAMDriver.plugin/AppleIDAMDriver](MACHOS/AppleIDAMDriver.md)
- [/System/Library/Audio/MIDI Drivers/AppleMIDIBluetoothDriver.plugin/AppleMIDIBluetoothDriver](MACHOS/AppleMIDIBluetoothDriver.md)
- [/System/Library/Audio/MIDI Drivers/AppleMIDIRTPDriver.plugin/AppleMIDIRTPDriver](MACHOS/AppleMIDIRTPDriver.md)
- [/System/Library/Audio/MIDI Drivers/AppleMIDIUSBDriver.plugin/AppleMIDIUSBDriver](MACHOS/AppleMIDIUSBDriver.md)
- [/System/Library/Audio/MIDI Drivers/YamahaUSBMIDIDriver.plugin/YamahaUSBMIDIDriver](MACHOS/YamahaUSBMIDIDriver.md)
- [/System/Library/Audio/Plug-Ins/HAL/AirPlayHalogen.driver/AirPlayHalogen](MACHOS/AirPlayHalogen.md)
- [/System/Library/Audio/Plug-Ins/HAL/AppleAOPAudioPlugin.driver/AppleAOPAudioPlugin](MACHOS/AppleAOPAudioPlugin.md)
- [/System/Library/Audio/Plug-Ins/HAL/AppleTimeSyncAudioClock.driver/AppleTimeSyncAudioClock](MACHOS/AppleTimeSyncAudioClock.md)
- [/System/Library/Audio/Plug-Ins/HAL/AppleUSBAudio.driver/AppleUSBAudio](MACHOS/AppleUSBAudio.md)
- [/System/Library/Audio/Plug-Ins/HAL/BTAudioHALPlugin.driver/BTAudioHALPlugin](MACHOS/BTAudioHALPlugin.md)
- [/System/Library/Audio/Plug-Ins/HAL/BasebandVoice.driver/BasebandVoice](MACHOS/BasebandVoice.md)
- [/System/Library/Audio/Plug-Ins/HAL/CarPlayHalogen.driver/CarPlayHalogen](MACHOS/CarPlayHalogen.md)
- [/System/Library/Audio/Plug-Ins/HAL/NetworkUplinkClock.driver/NetworkUplinkClock](MACHOS/NetworkUplinkClock.md)
- [/System/Library/Audio/Plug-Ins/HAL/OctaviaHalogen.driver/OctaviaHalogen](MACHOS/OctaviaHalogen.md)
- [/System/Library/Audio/Plug-Ins/RemoteInput/AudioAppleSiriRemoteInput.bundle/AudioAppleSiriRemoteInput](MACHOS/AudioAppleSiriRemoteInput.md)
- [/System/Library/Audio/Plug-Ins/RemoteInput/JarvisPlugin.bundle/JarvisPlugin](MACHOS/JarvisPlugin.md)
- [/System/Library/Audio/Plug-Ins/RemoteInput/RemoteAudioInputPlugin.bundle/RemoteAudioInputPlugin](MACHOS/RemoteAudioInputPlugin.md)
- [/System/Library/BulletinDistributor/PingSubscribers/NanoBedtimePingSubscriber.bundle/NanoBedtimePingSubscriber](MACHOS/NanoBedtimePingSubscriber.md)
- [/System/Library/BulletinDistributor/PingSubscribers/NanoCalendarPingSubscriber.bundle/NanoCalendarPingSubscriber](MACHOS/NanoCalendarPingSubscriber.md)
- [/System/Library/BulletinDistributor/PingSubscribers/NanoHealthPingSubscriber.bundle/NanoHealthPingSubscriber](MACHOS/NanoHealthPingSubscriber.md)
- [/System/Library/BulletinDistributor/PingSubscribers/SearchPartyNotificationPingSubscriber.bundle/SearchPartyNotificationPingSubscriber](MACHOS/SearchPartyNotificationPingSubscriber.md)
- [/System/Library/BulletinDistributor/PingSubscribers/ShortcutsPingSubscriber.bundle/ShortcutsPingSubscriber](MACHOS/ShortcutsPingSubscriber.md)
- [/System/Library/CardKit/Plugins/IntentsUICardKitProvider.bundle/IntentsUICardKitProvider](MACHOS/IntentsUICardKitProvider.md)
- [/System/Library/CardKit/Plugins/SearchUICardKitProvider.bundle/SearchUICardKitProvider](MACHOS/SearchUICardKitProvider.md)
- [/System/Library/CardKit/Plugins/SiriUICardKitProvider.bundle/SiriUICardKitProvider](MACHOS/SiriUICardKitProvider.md)
- [/System/Library/CloudRecommendations/ClientSources/ICQReviewLargeFilesRecommendations.bundle/ICQReviewLargeFilesRecommendations](MACHOS/ICQReviewLargeFilesRecommendations.md)
- [/System/Library/CloudRecommendations/ClientSources/PhotosCloudRecommendations.bundle/PhotosCloudRecommendations](MACHOS/PhotosCloudRecommendations.md)
- [/System/Library/ControlCenter/Bundles/AskToAirDropControlCenterModule.bundle/AskToAirDropControlCenterModule](MACHOS/AskToAirDropControlCenterModule.md)
- [/System/Library/ControlCenter/Bundles/AudioConferenceControlCenterModule.bundle/AudioConferenceControlCenterModule](MACHOS/AudioConferenceControlCenterModule.md)
- [/System/Library/ControlCenter/Bundles/ContinuousExposeModule.bundle/ContinuousExposeModule](MACHOS/ContinuousExposeModule.md)
- [/System/Library/ControlCenter/Bundles/FocusUIModule.bundle/FocusUIModule](MACHOS/FocusUIModule.md)
- [/System/Library/ControlCenter/Bundles/NFCControlCenterModule.bundle/NFCControlCenterModule](MACHOS/NFCControlCenterModule.md)
- [/System/Library/ControlCenter/Bundles/PingMyWatchControlCenterUI.bundle/PingMyWatchControlCenterUI](MACHOS/PingMyWatchControlCenterUI.md)
- [/System/Library/ControlCenter/Bundles/ReplayKitModule.bundle/ReplayKitModule](MACHOS/ReplayKitModule.md)
- [/System/Library/ControlCenter/Bundles/SilenceCallsCCWidget.bundle/SilenceCallsCCWidget](MACHOS/SilenceCallsCCWidget.md)
- [/System/Library/ControlCenter/Bundles/SystemQuickNoteModule.bundle/SystemQuickNoteModule](MACHOS/SystemQuickNoteModule.md)
- [/System/Library/ControlCenter/Bundles/VideoConferenceControlCenterModule.bundle/VideoConferenceControlCenterModule](MACHOS/VideoConferenceControlCenterModule.md)
- [/System/Library/CoreImage/CIBarcode.cifilter/CIBarcode](MACHOS/CIBarcode.md)
- [/System/Library/CoreImage/CIPassThrough.cifilter/CIPassThrough](MACHOS/CIPassThrough.md)
- [/System/Library/CoreImage/PortraitFilters.cifilter/PortraitFilters](MACHOS/PortraitFilters.md)
- [/System/Library/CoreServices/AccessibilityUIServer.app/AccessibilityUIServer](MACHOS/AccessibilityUIServer.md)
- [/System/Library/CoreServices/AccessibilityUIServer.app/Extensions/AccessibilityAppIntents.appex/AccessibilityAppIntents](MACHOS/AccessibilityAppIntents.md)
- [/System/Library/CoreServices/AegirProxyApp.app/AegirProxyApp](MACHOS/AegirProxyApp.md)
- [/System/Library/CoreServices/AegirProxyApp.app/PlugIns/AegirPoster.appex/AegirPoster](MACHOS/AegirPoster.md)
- [/System/Library/CoreServices/AssistiveTouch.app/assistivetouchd](MACHOS/assistivetouchd.md)
- [/System/Library/CoreServices/BluetoothUIService.app/BluetoothUIService](MACHOS/BluetoothUIService.md)
- [/System/Library/CoreServices/CacheDeleteAppContainerCaches](MACHOS/CacheDeleteAppContainerCaches.md)
- [/System/Library/CoreServices/CacheDeleteDaily](MACHOS/CacheDeleteDaily.md)
- [/System/Library/CoreServices/CarPlay.app/CarPlay](MACHOS/CarPlay.md)
- [/System/Library/CoreServices/CarPlayTemplateUIHost.app/CarPlayTemplateUIHost](MACHOS/CarPlayTemplateUIHost.md)
- [/System/Library/CoreServices/ClarityBoard.app/ClarityBoard](MACHOS/ClarityBoard.md)
- [/System/Library/CoreServices/CloudSettingsSyncAgent](MACHOS/CloudSettingsSyncAgent.md)
- [/System/Library/CoreServices/CommandAndControl.app/CommandAndControl](MACHOS/CommandAndControl.md)
- [/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices-0001.bundle/MobileDevices-0001](MACHOS/MobileDevices-0001.md)
- [/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices-0003.bundle/MobileDevices-0003](MACHOS/MobileDevices-0003.md)
- [/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices.bundle/MobileDevices](MACHOS/MobileDevices.md)
- [/System/Library/CoreServices/DeviceOMatic.app/DeviceOMatic](MACHOS/DeviceOMatic.md)
- [/System/Library/CoreServices/EscrowSecurityAlert.app/EscrowSecurityAlert](MACHOS/EscrowSecurityAlert.md)
- [/System/Library/CoreServices/FullKeyboardAccess.app/FullKeyboardAccess](MACHOS/FullKeyboardAccess.md)
- [/System/Library/CoreServices/IOUIAngel.app/IOUIAngel](MACHOS/IOUIAngel.md)
- [/System/Library/CoreServices/LiveTranscriptionUI.app/LiveTranscriptionUI](MACHOS/LiveTranscriptionUI.md)
- [/System/Library/CoreServices/MediaMLPluginApp.app/MediaMLPluginApp](MACHOS/MediaMLPluginApp.md)
- [/System/Library/CoreServices/MediaMLPluginApp.app/PlugIns/MediaMLPlugin.appex/MediaMLPlugin](MACHOS/MediaMLPlugin.md)
- [/System/Library/CoreServices/MobileCoreTypes.bundle/MobileCoreTypes](MACHOS/MobileCoreTypes.md)
- [/System/Library/CoreServices/OTACrashCopier](MACHOS/OTACrashCopier.md)
- [/System/Library/CoreServices/OverlayUI.app/OverlayUI](MACHOS/OverlayUI.md)
- [/System/Library/CoreServices/RawCameraSupport.bundle/RawCameraSupport](MACHOS/RawCameraSupport.md)
- [/System/Library/CoreServices/ReportCrash](MACHOS/ReportCrash.md)
- [/System/Library/CoreServices/SafariSupport.bundle/SafariBookmarksSyncAgent](MACHOS/SafariBookmarksSyncAgent.md)
- [/System/Library/CoreServices/ScreenSharingServer.app/ScreenSharingServer](MACHOS/ScreenSharingServer.md)
- [/System/Library/CoreServices/ShortcutsActions.app/Extensions/ShortcutsTopHitsExtension.appex/ShortcutsTopHitsExtension](MACHOS/ShortcutsTopHitsExtension.md)
- [/System/Library/CoreServices/ShortcutsActions.app/ShortcutsActions](MACHOS/ShortcutsActions.md)
- [/System/Library/CoreServices/SpringBoard.app/PlugIns/SpringBoardDiagnosticExtension.appex/SpringBoardDiagnosticExtension](MACHOS/SpringBoardDiagnosticExtension.md)
- [/System/Library/CoreServices/SpringBoard.app/SpringBoard](MACHOS/SpringBoard.md)
- [/System/Library/CoreServices/VoiceOverTouch.app/scrod](MACHOS/scrod.md)
- [/System/Library/CoreServices/VoiceOverTouch.app/vot](MACHOS/vot.md)
- [/System/Library/CoreServices/iconservicesagent](MACHOS/iconservicesagent.md)
- [/System/Library/CoreServices/osanalyticshelper](MACHOS/osanalyticshelper.md)
- [/System/Library/CoreServices/powerd.bundle/powerd](MACHOS/powerd.md)
- [/System/Library/CryptoTokenKit/usbsmartcardreaderd.slotd/usbsmartcardreaderd](MACHOS/usbsmartcardreaderd.md)
- [/System/Library/DataClassMigrators/00LaunchServicesMigrator.migrator/00LaunchServicesMigrator](MACHOS/00LaunchServicesMigrator.md)
- [/System/Library/DataClassMigrators/AccessibilityDataMigration.migrator/AccessibilityDataMigration](MACHOS/AccessibilityDataMigration.md)
- [/System/Library/DataClassMigrators/Accounts.migrator/Accounts](MACHOS/Accounts.md)
- [/System/Library/DataClassMigrators/AccountsObsolescence.migrator/AccountsObsolescence](MACHOS/AccountsObsolescence.md)
- [/System/Library/DataClassMigrators/AddressBookLegacy.migrator/AddressBookLegacy](MACHOS/AddressBookLegacy.md)
- [/System/Library/DataClassMigrators/AirTrafficMigrator.migrator/AirTrafficMigrator](MACHOS/AirTrafficMigrator.md)
- [/System/Library/DataClassMigrators/AnisetteMigrator.migrator/AnisetteMigrator](MACHOS/AnisetteMigrator.md)
- [/System/Library/DataClassMigrators/AppUserDataMigrator.migrator/AppUserDataMigrator](MACHOS/AppUserDataMigrator.md)
- [/System/Library/DataClassMigrators/AppleAccountMigrator.migrator/AppleAccountMigrator](MACHOS/AppleAccountMigrator.md)
- [/System/Library/DataClassMigrators/BuddyMigrator.migrator/BuddyMigrator](MACHOS/BuddyMigrator.md)
- [/System/Library/DataClassMigrators/CallHistoryDataMigrator.migrator/CallHistoryDataMigrator](MACHOS/CallHistoryDataMigrator.md)
- [/System/Library/DataClassMigrators/CloudRecentsMigrator.migrator/CloudRecentsMigrator](MACHOS/CloudRecentsMigrator.md)
- [/System/Library/DataClassMigrators/CloudTabsMigrator.migrator/CloudTabsMigrator](MACHOS/CloudTabsMigrator.md)
- [/System/Library/DataClassMigrators/ContainerMigrator.migrator/ContainerMigrator](MACHOS/ContainerMigrator.md)
- [/System/Library/DataClassMigrators/CookieDataMigrator.migrator/CookieDataMigrator](MACHOS/CookieDataMigrator.md)
- [/System/Library/DataClassMigrators/CoreLocationMigrator.migrator/CoreLocationMigrator](MACHOS/CoreLocationMigrator.md)
- [/System/Library/DataClassMigrators/CoreTimeMigrator.migrator/CoreTimeMigrator](MACHOS/CoreTimeMigrator.md)
- [/System/Library/DataClassMigrators/FitnessMigrator.migrator/FitnessMigrator](MACHOS/FitnessMigrator.md)
- [/System/Library/DataClassMigrators/HAENDataMigrator.migrator/HAENDataMigrator](MACHOS/HAENDataMigrator.md)
- [/System/Library/DataClassMigrators/HealthMigrator.migrator/HealthMigrator](MACHOS/HealthMigrator.md)
- [/System/Library/DataClassMigrators/InternationalSupportMigrator.migrator/InternationalSupportMigrator](MACHOS/InternationalSupportMigrator.md)
- [/System/Library/DataClassMigrators/KeyboardMigrator.migrator/KeyboardMigrator](MACHOS/KeyboardMigrator.md)
- [/System/Library/DataClassMigrators/KeyboardUIMigrator.migrator/KeyboardUIMigrator](MACHOS/KeyboardUIMigrator.md)
- [/System/Library/DataClassMigrators/KeychainMigrator.migrator/KeychainMigrator](MACHOS/KeychainMigrator.md)
- [/System/Library/DataClassMigrators/LanguageAssetMigrator.migrator/LanguageAssetMigrator](MACHOS/LanguageAssetMigrator.md)
- [/System/Library/DataClassMigrators/LegacyMessageAccountsMigrator.migrator/LegacyMessageAccountsMigrator](MACHOS/LegacyMessageAccountsMigrator.md)
- [/System/Library/DataClassMigrators/MCCleanup.migrator/MCCleanup](MACHOS/MCCleanup.md)
- [/System/Library/DataClassMigrators/MCMDM.migrator/MCMDM](MACHOS/MCMDM.md)
- [/System/Library/DataClassMigrators/MCProfile.migrator/MCProfile](MACHOS/MCProfile.md)
- [/System/Library/DataClassMigrators/MKBMigrator.migrator/MKBMigrator](MACHOS/MKBMigrator.md)
- [/System/Library/DataClassMigrators/MSUDataMigrator.migrator/MSUDataMigrator](MACHOS/MSUDataMigrator.md)
- [/System/Library/DataClassMigrators/MediaLibrary.migrator/MediaLibrary](MACHOS/MediaLibrary.md)
- [/System/Library/DataClassMigrators/MergeBuddyProvisioningResponse.migrator/MergeBuddyProvisioningResponse](MACHOS/MergeBuddyProvisioningResponse.md)
- [/System/Library/DataClassMigrators/MessageAccountsMigrator.migrator/MessageAccountsMigrator](MACHOS/MessageAccountsMigrator.md)
- [/System/Library/DataClassMigrators/MobileActivationMigrator.migrator/MobileActivationMigrator](MACHOS/MobileActivationMigrator.md)
- [/System/Library/DataClassMigrators/MobileAsset.migrator/MobileAsset](MACHOS/MobileAsset.md)
- [/System/Library/DataClassMigrators/MobileGestaltMigrator.migrator/MobileGestaltMigrator](MACHOS/MobileGestaltMigrator.md)
- [/System/Library/DataClassMigrators/MobileMailMigrator.migrator/MobileMailMigrator](MACHOS/MobileMailMigrator.md)
- [/System/Library/DataClassMigrators/MobileSafari.migrator/MobileSafari](MACHOS/MobileSafari.md)
- [/System/Library/DataClassMigrators/MobileSlideShow.migrator/MobileSlideShow](MACHOS/MobileSlideShow.md)
- [/System/Library/DataClassMigrators/PassbookDataMigrator.migrator/PassbookDataMigrator](MACHOS/PassbookDataMigrator.md)
- [/System/Library/DataClassMigrators/PreferencesMigrator.migrator/PreferencesMigrator](MACHOS/PreferencesMigrator.md)
- [/System/Library/DataClassMigrators/RestorePostProcess.migrator/RestorePostProcess](MACHOS/RestorePostProcess.md)
- [/System/Library/DataClassMigrators/Shortcuts.migrator/Shortcuts](MACHOS/Shortcuts.md)
- [/System/Library/DataClassMigrators/Siri.migrator/Siri](MACHOS/Siri.md)
- [/System/Library/DataClassMigrators/SpringBoard.migrator/SpringBoard](MACHOS/SpringBoard.md)
- [/System/Library/DataClassMigrators/StocksMigrator.migrator/StocksMigrator](MACHOS/StocksMigrator.md)
- [/System/Library/DataClassMigrators/SystemAppMigrator.migrator/SystemAppMigrator](MACHOS/SystemAppMigrator.md)
- [/System/Library/DataClassMigrators/TVMigrator.migrator/TVMigrator](MACHOS/TVMigrator.md)
- [/System/Library/DataClassMigrators/Tones.migrator/Tones](MACHOS/Tones.md)
- [/System/Library/DataClassMigrators/Vibrations.migrator/Vibrations](MACHOS/Vibrations.md)
- [/System/Library/DataClassMigrators/WebBookmarks.migrator/WebBookmarks](MACHOS/WebBookmarks.md)
- [/System/Library/DataClassMigrators/WiFiDataMigrator.migrator/WiFiDataMigrator](MACHOS/WiFiDataMigrator.md)
- [/System/Library/DataClassMigrators/iTunesStore.migrator/iTunesStore](MACHOS/iTunesStore.md)
- [/System/Library/DigitalSeparation/SharingSources/ActivityDigitalSeparation.bundle/ActivityDigitalSeparation](MACHOS/ActivityDigitalSeparation.md)
- [/System/Library/DigitalSeparation/SharingSources/CalendarSeparation.bundle/CalendarSeparation](MACHOS/CalendarSeparation.md)
- [/System/Library/DigitalSeparation/SharingSources/DSNotesPlugin.bundle/DSNotesPlugin](MACHOS/DSNotesPlugin.md)
- [/System/Library/DigitalSeparation/SharingSources/DigitalSeparationBundle.bundle/DigitalSeparationBundle](MACHOS/DigitalSeparationBundle.md)
- [/System/Library/DigitalSeparation/SharingSources/FindMy.bundle/FindMy](MACHOS/FindMy.md)
- [/System/Library/DigitalSeparation/SharingSources/FindMyItemsDigitalSeparation.bundle/FindMyItemsDigitalSeparation](MACHOS/FindMyItemsDigitalSeparation.md)
- [/System/Library/DigitalSeparation/SharingSources/HealthSharingSeparation.bundle/HealthSharingSeparation](MACHOS/HealthSharingSeparation.md)
- [/System/Library/DigitalSeparation/SharingSources/MapsDigitalSeparation.bundle/MapsDigitalSeparation](MACHOS/MapsDigitalSeparation.md)
- [/System/Library/DigitalSeparation/SharingSources/PhotosSeparation.bundle/PhotosSeparation](MACHOS/PhotosSeparation.md)
- [/System/Library/DigitalSeparation/SharingSources/SafetyMonitorSeparation.bundle/SafetyMonitorSeparation](MACHOS/SafetyMonitorSeparation.md)
- [/System/Library/DistributedEvaluation/Plugins/APODMLDESPlugin.desPlugin/APODMLDESPlugin](MACHOS/APODMLDESPlugin.md)
- [/System/Library/DistributedEvaluation/Plugins/AutocorrectionTesterDESPlugin.desPlugin/AutocorrectionTesterDESPlugin](MACHOS/AutocorrectionTesterDESPlugin.md)
- [/System/Library/DistributedEvaluation/Plugins/DictationPersonalizationFides2Plugin.desPlugin/DictationPersonalizationFides2Plugin](MACHOS/DictationPersonalizationFides2Plugin.md)
- [/System/Library/DistributedEvaluation/Plugins/FidesPHSPlugin.desPlugin/FidesPHSPlugin](MACHOS/FidesPHSPlugin.md)
- [/System/Library/DistributedEvaluation/Plugins/GlobalNNLMFidesPlugin.desPlugin/GlobalNNLMFidesPlugin](MACHOS/GlobalNNLMFidesPlugin.md)
- [/System/Library/DistributedEvaluation/Plugins/InertiaCamDES.desPlugin/InertiaCamDES](MACHOS/InertiaCamDES.md)
- [/System/Library/DistributedEvaluation/Plugins/PMLDESPlugin.desPlugin/PMLDESPlugin](MACHOS/PMLDESPlugin.md)
- [/System/Library/DistributedEvaluation/Plugins/PeopleSuggesterDESPlugin.desPlugin/PeopleSuggesterDESPlugin](MACHOS/PeopleSuggesterDESPlugin.md)
- [/System/Library/DistributedEvaluation/Plugins/PhotosDESPlugin.desPlugin/PhotosDESPlugin](MACHOS/PhotosDESPlugin.md)
- [/System/Library/DistributedEvaluation/Plugins/QuickTypeDESPlugin.desPlugin/QuickTypeDESPlugin](MACHOS/QuickTypeDESPlugin.md)
- [/System/Library/DistributedEvaluation/Plugins/RemindersDES.desPlugin/RemindersDES](MACHOS/RemindersDES.md)
- [/System/Library/DistributedEvaluation/Plugins/TypingDESPlugin.desPlugin/TypingDESPlugin](MACHOS/TypingDESPlugin.md)
- [/System/Library/DistributedEvaluation/Plugins/siriinference-dodml-plugin.desPlugin/siriinference-dodml-plugin](MACHOS/siriinference-dodml-plugin.md)
- [/System/Library/DoNotDisturb/ClientBundles/com.apple.donotdisturb.private.app-launch.bundle/com.apple.donotdisturb.private.app-launch](MACHOS/com.apple.donotdisturb.private.app-launch.md)
- [/System/Library/DoNotDisturb/ClientBundles/com.apple.donotdisturb.private.driving-trigger.bundle/com.apple.donotdisturb.private.driving-trigger](MACHOS/com.apple.donotdisturb.private.driving-trigger.md)
- [/System/Library/DoNotDisturb/ClientBundles/com.apple.donotdisturb.private.intents.preload.bundle/com.apple.donotdisturb.private.intents.preload](MACHOS/com.apple.donotdisturb.private.intents.preload.md)
- [/System/Library/DoNotDisturb/ClientBundles/com.apple.donotdisturb.private.intents.user-interactive.preload.bundle/com.apple.donotdisturb.private.intents.user-interactive.preload](MACHOS/com.apple.donotdisturb.private.intents.user-interactive.preload.md)
- [/System/Library/DoNotDisturb/ClientBundles/com.apple.donotdisturb.private.schedule.bundle/com.apple.donotdisturb.private.schedule](MACHOS/com.apple.donotdisturb.private.schedule.md)
- [/System/Library/DoNotDisturb/ClientBundles/com.apple.donotdisturb.private.sleeping-trigger.bundle/com.apple.donotdisturb.private.sleeping-trigger](MACHOS/com.apple.donotdisturb.private.sleeping-trigger.md)
- [/System/Library/DoNotDisturb/ClientBundles/com.apple.donotdisturb.private.smart-trigger.bundle/com.apple.donotdisturb.private.smart-trigger](MACHOS/com.apple.donotdisturb.private.smart-trigger.md)
- [/System/Library/DoNotDisturb/ClientBundles/com.apple.donotdisturb.private.workout-trigger.bundle/com.apple.donotdisturb.private.workout-trigger](MACHOS/com.apple.donotdisturb.private.workout-trigger.md)
- [/System/Library/DoNotDisturb/ClientBundles/com.apple.donotdisturb.user-toggles.preload.bundle/com.apple.donotdisturb.user-toggles.preload](MACHOS/com.apple.donotdisturb.user-toggles.preload.md)
- [/System/Library/DoNotDisturb/ClientBundles/com.apple.private.SpringBoard.focus.intents.preload.bundle/com.apple.private.SpringBoard.focus.intents.preload](MACHOS/com.apple.private.SpringBoard.focus.intents.preload.md)
- [/System/Library/DriverExtensions/com.apple.AFKUserHIDDrivers.dext/com.apple.AFKUserHIDDrivers](MACHOS/com.apple.AFKUserHIDDrivers.md)
- [/System/Library/DriverExtensions/com.apple.AppleUserHIDDrivers.dext/com.apple.AppleUserHIDDrivers](MACHOS/com.apple.AppleUserHIDDrivers.md)
- [/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN](MACHOS/com.apple.DriverKit-AppleBCMWLAN.md)
- [/System/Library/DriverExtensions/com.apple.DriverKit-AppleEthernetE1000.dext/com.apple.DriverKit-AppleEthernetE1000](MACHOS/com.apple.DriverKit-AppleEthernetE1000.md)
- [/System/Library/DriverExtensions/com.apple.DriverKit-AppleEthernetIXGBE.dext/com.apple.DriverKit-AppleEthernetIXGBE](MACHOS/com.apple.DriverKit-AppleEthernetIXGBE.md)
- [/System/Library/DriverExtensions/com.apple.DriverKit-AppleEthernetIXL.dext/com.apple.DriverKit-AppleEthernetIXL](MACHOS/com.apple.DriverKit-AppleEthernetIXL.md)
- [/System/Library/DriverExtensions/com.apple.DriverKit-AppleEthernetMLX5.dext/com.apple.DriverKit-AppleEthernetMLX5](MACHOS/com.apple.DriverKit-AppleEthernetMLX5.md)
- [/System/Library/DriverExtensions/com.apple.DriverKit.AppleUserECM.dext/com.apple.DriverKit.AppleUserECM](MACHOS/com.apple.DriverKit.AppleUserECM.md)
- [/System/Library/DuetActivityScheduler/Scheduler/DuetActivitySchedulerDaemon.bundle/DuetActivitySchedulerDaemon](MACHOS/DuetActivitySchedulerDaemon.md)
- [/System/Library/ExtensionKit/Extensions/AppExtensionManagement.appex/AppExtensionManagement](MACHOS/AppExtensionManagement.md)
- [/System/Library/ExtensionKit/Extensions/BitacoraWorker.appex/BitacoraWorker](MACHOS/BitacoraWorker.md)
- [/System/Library/ExtensionKit/Extensions/DeepThoughtWorker.appex/DeepThoughtWorker](MACHOS/DeepThoughtWorker.md)
- [/System/Library/ExtensionKit/Extensions/EventKitUIRemoteUIExtension.appex/EventKitUIRemoteUIExtension](MACHOS/EventKitUIRemoteUIExtension.md)
- [/System/Library/ExtensionKit/Extensions/LighthouseNightingaleExtension.appex/LighthouseNightingaleExtension](MACHOS/LighthouseNightingaleExtension.md)
- [/System/Library/ExtensionKit/Extensions/MADViewServiceExtension.appex/MADViewServiceExtension](MACHOS/MADViewServiceExtension.md)
- [/System/Library/ExtensionKit/Extensions/MapsTransactionInsightsExtension.appex/MapsTransactionInsightsExtension](MACHOS/MapsTransactionInsightsExtension.md)
- [/System/Library/ExtensionKit/Extensions/MetricsExtension.appex/MetricsExtension](MACHOS/MetricsExtension.md)
- [/System/Library/ExtensionKit/Extensions/PFLHRPeriodPredCK.appex/PFLHRPeriodPredCK](MACHOS/PFLHRPeriodPredCK.md)
- [/System/Library/ExtensionKit/Extensions/PFLHRPeriodPredMLH.appex/PFLHRPeriodPredMLH](MACHOS/PFLHRPeriodPredMLH.md)
- [/System/Library/ExtensionKit/Extensions/ProactiveShareSheetLighthouseBackgroundPlugin.appex/ProactiveShareSheetLighthouseBackgroundPlugin](MACHOS/ProactiveShareSheetLighthouseBackgroundPlugin.md)
- [/System/Library/ExtensionKit/Extensions/RepackagingWorker.appex/RepackagingWorker](MACHOS/RepackagingWorker.md)
- [/System/Library/ExtensionKit/Extensions/SiriCoreMetricsWorker.appex/SiriCoreMetricsWorker](MACHOS/SiriCoreMetricsWorker.md)
- [/System/Library/ExtensionKit/Extensions/SiriMASPFLPlugin.appex/SiriMASPFLPlugin](MACHOS/SiriMASPFLPlugin.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.fskit.exfat.appex/com.apple.fskit.exfat](MACHOS/com.apple.fskit.exfat.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.fskit.msdos.appex/com.apple.fskit.msdos](MACHOS/com.apple.fskit.msdos.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.mlhost.CloudWorker.appex/com.apple.mlhost.CloudWorker](MACHOS/com.apple.mlhost.CloudWorker.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.mlhost.QuartzWorker.appex/com.apple.mlhost.QuartzWorker](MACHOS/com.apple.mlhost.QuartzWorker.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.mlhost.SampleWorker.appex/com.apple.mlhost.SampleWorker](MACHOS/com.apple.mlhost.SampleWorker.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.mlhost.TelemetryWorker.appex/com.apple.mlhost.TelemetryWorker](MACHOS/com.apple.mlhost.TelemetryWorker.md)
- [/System/Library/Extensions/ASIOKit.kext/ASIOKit](MACHOS/ASIOKit.md)
- [/System/Library/Extensions/AppleBiometricSensor.kext/PlugIns/AppleMesaLib.plugin/AppleMesaLib](MACHOS/AppleMesaLib.md)
- [/System/Library/Extensions/AppleGameControllerPersonality.kext/AppleGameControllerPersonality](MACHOS/AppleGameControllerPersonality.md)
- [/System/Library/Extensions/AppleHIDALSService.kext/PlugIns/AppleHIDALS.plugin/AppleHIDALS](MACHOS/AppleHIDALS.md)
- [/System/Library/Extensions/AppleHPM.kext/PlugIns/AppleHPMLib.plugin/AppleHPMLib](MACHOS/AppleHPMLib.md)
- [/System/Library/Extensions/AppleLockdownMode.kext/AppleLockdownMode](MACHOS/AppleLockdownMode.md)
- [/System/Library/Extensions/AppleSPU.kext/PlugIns/FastpathLib.plugin/FastpathLib](MACHOS/FastpathLib.md)
- [/System/Library/Extensions/AppleSPURose.kext/PlugIns/RoseControllerLib.plugin/RoseControllerLib](MACHOS/RoseControllerLib.md)
- [/System/Library/Extensions/AppleUVDM.kext/PlugIns/AppleUVDMLib.plugin/AppleUVDMLib](MACHOS/AppleUVDMLib.md)
- [/System/Library/Extensions/EAP-RSA.ppp/EAP-RSA](MACHOS/EAP-RSA.md)
- [/System/Library/Extensions/IOStreamFamily.kext/PlugIns/IOStreamLib.plugin/IOStreamLib](MACHOS/IOStreamLib.md)
- [/System/Library/Extensions/IOUSBHostFamily.kext/PlugIns/IOUSBLib.bundle/IOUSBLib](MACHOS/IOUSBLib.md)
- [/System/Library/Extensions/lifs.kext/lifs](MACHOS/lifs.md)
- [/System/Library/Filesystems/apfs.fs/apfs.util](MACHOS/apfs.util.md)
- [/System/Library/Filesystems/apfs.fs/apfs_boot_util](MACHOS/apfs_boot_util.md)
- [/System/Library/Filesystems/apfs.fs/apfs_checkdigest](MACHOS/apfs_checkdigest.md)
- [/System/Library/Filesystems/apfs.fs/apfs_checkseal](MACHOS/apfs_checkseal.md)
- [/System/Library/Filesystems/apfs.fs/apfs_condenser](MACHOS/apfs_condenser.md)
- [/System/Library/Filesystems/apfs.fs/apfs_iosd](MACHOS/apfs_iosd.md)
- [/System/Library/Filesystems/apfs.fs/apfs_stats](MACHOS/apfs_stats.md)
- [/System/Library/Filesystems/apfs.fs/apfs_vol_converter](MACHOS/apfs_vol_converter.md)
- [/System/Library/Filesystems/apfs.fs/fsck_apfs](MACHOS/fsck_apfs.md)
- [/System/Library/Filesystems/apfs.fs/mount_apfs](MACHOS/mount_apfs.md)
- [/System/Library/Filesystems/apfs.fs/newfs_apfs](MACHOS/newfs_apfs.md)
- [/System/Library/Filesystems/apfs.fs/slurpAPFSMeta](MACHOS/slurpAPFSMeta.md)
- [/System/Library/Filesystems/apfs.fs/sm_stats](MACHOS/sm_stats.md)
- [/System/Library/Filesystems/apfs_userfs.fs/apfs_userfs.util](MACHOS/apfs_userfs.util.md)
- [/System/Library/Filesystems/exfat.fs/exfat.util](MACHOS/exfat.util.md)
- [/System/Library/Filesystems/exfat.fs/fsck_exfat](MACHOS/fsck_exfat.md)
- [/System/Library/Filesystems/exfat.fs/newfs_exfat](MACHOS/newfs_exfat.md)
- [/System/Library/Filesystems/hfs.fs/CopyHFSMeta](MACHOS/CopyHFSMeta.md)
- [/System/Library/Filesystems/hfs.fs/fsck_hfs](MACHOS/fsck_hfs.md)
- [/System/Library/Filesystems/hfs.fs/hfs.util](MACHOS/hfs.util.md)
- [/System/Library/Filesystems/hfs.fs/mount_hfs](MACHOS/mount_hfs.md)
- [/System/Library/Filesystems/hfs.fs/newfs_hfs](MACHOS/newfs_hfs.md)
- [/System/Library/Filesystems/msdos.fs/fsck_msdos](MACHOS/fsck_msdos.md)
- [/System/Library/Filesystems/msdos.fs/msdos.util](MACHOS/msdos.util.md)
- [/System/Library/Filesystems/msdos.fs/newfs_msdos](MACHOS/newfs_msdos.md)
- [/System/Library/Filesystems/ntfs.fs/BootCampFormatter](MACHOS/BootCampFormatter.md)
- [/System/Library/Filesystems/ntfs.fs/ntfs.util](MACHOS/ntfs.util.md)
- [/System/Library/Filesystems/tmpfs.fs/mount_tmpfs](MACHOS/mount_tmpfs.md)
- [/System/Library/Frameworks/AVFAudio.framework/XPCServices/AVAudioDeviceTestService.xpc/AVAudioDeviceTestService](MACHOS/AVAudioDeviceTestService.md)
- [/System/Library/Frameworks/AVKit.framework/XPCServices/SharedPreferences.xpc/SharedPreferences](MACHOS/SharedPreferences.md)
- [/System/Library/Frameworks/Accounts.framework/accountsd](MACHOS/accountsd.md)
- [/System/Library/Frameworks/AddressBook.framework/Support/ABDatabaseDoctor](MACHOS/ABDatabaseDoctor.md)
- [/System/Library/Frameworks/AppTrackingTransparency.framework/XPCServices/EnforcementService.xpc/EnforcementService](MACHOS/EnforcementService.md)
- [/System/Library/Frameworks/AssetsLibrary.framework/Support/assetsd](MACHOS/assetsd.md)
- [/System/Library/Frameworks/AudioToolbox.framework/XPCServices/AudioConverterService.xpc/AudioConverterService](MACHOS/AudioConverterService.md)
- [/System/Library/Frameworks/AudioToolbox.framework/XPCServices/CAReportingService.xpc/CAReportingService](MACHOS/CAReportingService.md)
- [/System/Library/Frameworks/AutomatedDeviceEnrollment.framework/PlugIns/AddDevicesToAutomatedDeviceEnrollmentExtension.appex/AddDevicesToAutomatedDeviceEnrollmentExtension](MACHOS/AddDevicesToAutomatedDeviceEnrollmentExtension.md)
- [/System/Library/Frameworks/CFNetwork.framework/AuthBrokerAgent](MACHOS/AuthBrokerAgent.md)
- [/System/Library/Frameworks/CFNetwork.framework/CFNetworkAgent](MACHOS/CFNetworkAgent.md)
- [/System/Library/Frameworks/CFNetwork.framework/PlugIns/DiagnosticExtension.appex/DiagnosticExtension](MACHOS/DiagnosticExtension.md)
- [/System/Library/Frameworks/CallKit.framework/XPCServices/com.apple.CallKit.CallDirectory.xpc/com.apple.CallKit.CallDirectory](MACHOS/com.apple.CallKit.CallDirectory.md)
- [/System/Library/Frameworks/CallKit.framework/XPCServices/com.apple.CallKit.CallDirectoryMaintenance.xpc/com.apple.CallKit.CallDirectoryMaintenance](MACHOS/com.apple.CallKit.CallDirectoryMaintenance.md)
- [/System/Library/Frameworks/ClassKit.framework/PlugIns/ClassKitDiagnosticExtension.appex/ClassKitDiagnosticExtension](MACHOS/ClassKitDiagnosticExtension.md)
- [/System/Library/Frameworks/ClassKit.framework/progressd](MACHOS/progressd.md)
- [/System/Library/Frameworks/ClockKit.framework/XPCServices/CLKCompanionWatchFaceLibraryService.xpc/CLKCompanionWatchFaceLibraryService](MACHOS/CLKCompanionWatchFaceLibraryService.md)
- [/System/Library/Frameworks/Contacts.framework/PlugIns/ContactsCoreSpotlightExtension.appex/ContactsCoreSpotlightExtension](MACHOS/ContactsCoreSpotlightExtension.md)
- [/System/Library/Frameworks/Contacts.framework/Support/contactsd](MACHOS/contactsd.md)
- [/System/Library/Frameworks/ContactsUI.framework/PlugIns/ContactViewViewService.appex/ContactViewViewService](MACHOS/ContactViewViewService.md)
- [/System/Library/Frameworks/ContactsUI.framework/PlugIns/ContactsViewService.appex/ContactsViewService](MACHOS/ContactsViewService.md)
- [/System/Library/Frameworks/ContactsUI.framework/PlugIns/MonogramPosterExtension.appex/MonogramPosterExtension](MACHOS/MonogramPosterExtension.md)
- [/System/Library/Frameworks/CoreGraphics.framework/XPCServices/CGPDFService.xpc/CGPDFService](MACHOS/CGPDFService.md)
- [/System/Library/Frameworks/CoreImage.framework/ccportrait_builtins_archive_bin.metallib](MACHOS/ccportrait_builtins_archive_bin.metallib.md)
- [/System/Library/Frameworks/CoreImage.framework/coreui_archive_bin.metallib](MACHOS/coreui_archive_bin.metallib.md)
- [/System/Library/Frameworks/CoreImage.framework/photo_style_archive_bin.metallib](MACHOS/photo_style_archive_bin.metallib.md)
- [/System/Library/Frameworks/CoreImage.framework/portrait_filters_archive_bin.metallib](MACHOS/portrait_filters_archive_bin.metallib.md)
- [/System/Library/Frameworks/CoreImage.framework/portrait_filters_fullsize_archive_bin.metallib](MACHOS/portrait_filters_fullsize_archive_bin.metallib.md)
- [/System/Library/Frameworks/CoreImage.framework/redeye_repair_archive_bin.metallib](MACHOS/redeye_repair_archive_bin.metallib.md)
- [/System/Library/Frameworks/CoreLocation.framework/PlugIns/CoreLocationRepromptAlwaysAuthPromptPlugin.appex/CoreLocationRepromptAlwaysAuthPromptPlugin](MACHOS/CoreLocationRepromptAlwaysAuthPromptPlugin.md)
- [/System/Library/Frameworks/CoreLocation.framework/PlugIns/CoreLocationTemporaryPreciseAuthPromptPlugin.appex/CoreLocationTemporaryPreciseAuthPromptPlugin](MACHOS/CoreLocationTemporaryPreciseAuthPromptPlugin.md)
- [/System/Library/Frameworks/CoreLocation.framework/PlugIns/CoreLocationVanillaWhenInUseAuthPromptPlugin.appex/CoreLocationVanillaWhenInUseAuthPromptPlugin](MACHOS/CoreLocationVanillaWhenInUseAuthPromptPlugin.md)
- [/System/Library/Frameworks/CoreLocation.framework/XPCServices/maphelperservice.xpc/maphelperservice](MACHOS/maphelperservice.md)
- [/System/Library/Frameworks/CoreLocationUI.framework/XPCServices/com.apple.corelocation.locationUI.xpc/com.apple.corelocation.locationUI](MACHOS/com.apple.corelocation.locationUI.md)
- [/System/Library/Frameworks/CoreMIDI.framework/MIDIServer](MACHOS/MIDIServer.md)
- [/System/Library/Frameworks/CoreML.framework/XPCServices/CoreMLModelSecurityService.xpc/CoreMLModelSecurityService](MACHOS/CoreMLModelSecurityService.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlightService](MACHOS/CoreSpotlightService.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/PlugIns/CoreSpotlightImportExtension1_iOS.appex/CoreSpotlightImportExtension1_iOS](MACHOS/CoreSpotlightImportExtension1_iOS.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/PlugIns/CoreSpotlightImportExtension2_iOS.appex/CoreSpotlightImportExtension2_iOS](MACHOS/CoreSpotlightImportExtension2_iOS.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/Support/com.apple.spotlight.IndexAgent](MACHOS/com.apple.spotlight.IndexAgent.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/spotlightknowledged](MACHOS/spotlightknowledged.md)
- [/System/Library/Frameworks/CoreTelephony.framework/PlugIns/CTFollowUpExtension.appex/CTFollowUpExtension](MACHOS/CTFollowUpExtension.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/CTParser.framework/XPCServices/CTParserService.xpc/CTParserService](MACHOS/CTParserService.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenterMobileHelper](MACHOS/CommCenterMobileHelper.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenterRootHelper](MACHOS/CommCenterRootHelper.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/DMHelper](MACHOS/DMHelper.md)
- [/System/Library/Frameworks/CryptoTokenKit.framework/PlugIns/pivtoken.appex/pivtoken](MACHOS/pivtoken.md)
- [/System/Library/Frameworks/CryptoTokenKit.framework/PlugIns/secelemtoken.appex/secelemtoken](MACHOS/secelemtoken.md)
- [/System/Library/Frameworks/CryptoTokenKit.framework/ctkd](MACHOS/ctkd.md)
- [/System/Library/Frameworks/EventKit.framework/PlugIns/CalendarDiagnosticExtension.appex/CalendarDiagnosticExtension](MACHOS/CalendarDiagnosticExtension.md)
- [/System/Library/Frameworks/ExposureNotification.framework/XPCServices/ExposureNotificationService.xpc/ExposureNotificationService](MACHOS/ExposureNotificationService.md)
- [/System/Library/Frameworks/ExtensionFoundation.framework/XPCServices/extensionkitservice.xpc/extensionkitservice](MACHOS/extensionkitservice.md)
- [/System/Library/Frameworks/ExternalAccessory.framework/PlugIns/ExternalAccessoryWACUIBits.bundle/ExternalAccessoryWACUIBits](MACHOS/ExternalAccessoryWACUIBits.md)
- [/System/Library/Frameworks/ExternalAccessory.framework/PlugIns/com.apple.ExternalAccessory.WACUI.appex/com.apple.ExternalAccessory.WACUI](MACHOS/com.apple.ExternalAccessory.WACUI.md)
- [/System/Library/Frameworks/ExternalAccessory.framework/XPCServices/WACEAService.xpc/WACEAService](MACHOS/WACEAService.md)
- [/System/Library/Frameworks/FamilyControls.framework/FamilyControlsAgent](MACHOS/FamilyControlsAgent.md)
- [/System/Library/Frameworks/FamilyControls.framework/PlugIns/ActivityPickerExtension.appex/ActivityPickerExtension](MACHOS/ActivityPickerExtension.md)
- [/System/Library/Frameworks/FamilyControls.framework/PlugIns/FamilyControlsOverrideSettingsExtension.appex/FamilyControlsOverrideSettingsExtension](MACHOS/FamilyControlsOverrideSettingsExtension.md)
- [/System/Library/Frameworks/FileProvider.framework/OverrideBundles/CloudDocsFileProvider.bundle/CloudDocsFileProvider](MACHOS/CloudDocsFileProvider.md)
- [/System/Library/Frameworks/FileProvider.framework/OverrideBundles/FileProviderOverride.bundle/FileProviderOverride](MACHOS/FileProviderOverride.md)
- [/System/Library/Frameworks/FileProvider.framework/OverrideBundles/iCloudDriveFileProviderOverride.bundle/iCloudDriveFileProviderOverride](MACHOS/iCloudDriveFileProviderOverride.md)
- [/System/Library/Frameworks/FileProvider.framework/PlugIns/FPSpotlightIndexer.appex/FPSpotlightIndexer](MACHOS/FPSpotlightIndexer.md)
- [/System/Library/Frameworks/FileProvider.framework/PlugIns/LocalStorageFileProvider.appex/LocalStorageFileProvider](MACHOS/LocalStorageFileProvider.md)
- [/System/Library/Frameworks/FileProvider.framework/Support/fileproviderd](MACHOS/fileproviderd.md)
- [/System/Library/Frameworks/FileProviderUI.framework/PlugIns/ServerAuthUIExtension.appex/ServerAuthUIExtension](MACHOS/ServerAuthUIExtension.md)
- [/System/Library/Frameworks/FinanceKit.framework/financed](MACHOS/financed.md)
- [/System/Library/Frameworks/GSS.framework/Helpers/GSSCred](MACHOS/GSSCred.md)
- [/System/Library/Frameworks/GameController.framework/VirtualGameController.bundle/VirtualGameController](MACHOS/VirtualGameController.md)
- [/System/Library/Frameworks/GroupActivities.framework/XPCServices/GroupSessionService.xpc/GroupSessionService](MACHOS/GroupSessionService.md)
- [/System/Library/Frameworks/HealthKit.framework/PlugIns/com.apple.HealthKit.HealthCustomerDiagnosticExtension.appex/com.apple.HealthKit.HealthCustomerDiagnosticExtension](MACHOS/com.apple.HealthKit.HealthCustomerDiagnosticExtension.md)
- [/System/Library/Frameworks/HealthKit.framework/PlugIns/com.apple.HealthKit.HealthDiagnosticExtension.appex/com.apple.HealthKit.HealthDiagnosticExtension](MACHOS/com.apple.HealthKit.HealthDiagnosticExtension.md)
- [/System/Library/Frameworks/HealthKit.framework/healthd](MACHOS/healthd.md)
- [/System/Library/Frameworks/HomeKit.framework/PlugIns/HomeKitDiagnosticExtension.appex/HomeKitDiagnosticExtension](MACHOS/HomeKitDiagnosticExtension.md)
- [/System/Library/Frameworks/HomeKit.framework/PlugIns/HomeKitIntentExtension.appex/HomeKitIntentExtension](MACHOS/HomeKitIntentExtension.md)
- [/System/Library/Frameworks/IdentityLookup.framework/XPCServices/com.apple.IdentityLookup.MessageFilter.xpc/com.apple.IdentityLookup.MessageFilter](MACHOS/com.apple.IdentityLookup.MessageFilter.md)
- [/System/Library/Frameworks/ImageCaptureCore.framework/XPCServices/icprefd-xpc.xpc/icprefd-xpc](MACHOS/icprefd-xpc.md)
- [/System/Library/Frameworks/ImageCaptureCore.framework/XPCServices/mscamerad-xpc.xpc/mscamerad-xpc](MACHOS/mscamerad-xpc.md)
- [/System/Library/Frameworks/ImageIO.framework/PlugIns/com.apple.imageimporter.appex/com.apple.imageimporter](MACHOS/com.apple.imageimporter.md)
- [/System/Library/Frameworks/ImageIO.framework/XPCServices/ImageIOXPCService.xpc/ImageIOXPCService](MACHOS/ImageIOXPCService.md)
- [/System/Library/Frameworks/Intents.framework/XPCServices/intents_helper.xpc/intents_helper](MACHOS/intents_helper.md)
- [/System/Library/Frameworks/LinkPresentation.framework/PlugIns/YouTubePlayer.wkbundle/YouTubePlayer](MACHOS/YouTubePlayer.md)
- [/System/Library/Frameworks/LinkPresentation.framework/XPCServices/com.apple.LinkPresentation.LinkSnapshotGeneratorService.xpc/com.apple.LinkPresentation.LinkSnapshotGeneratorService](MACHOS/com.apple.LinkPresentation.LinkSnapshotGeneratorService.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismPlugins/MechPasscode.bundle/MechPasscode](MACHOS/MechPasscode.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismPlugins/MechPearl.bundle/MechPearl](MACHOS/MechPearl.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismPlugins/MechPushButton.bundle/MechPushButton](MACHOS/MechPushButton.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismPlugins/MechTouchId.bundle/MechTouchId](MACHOS/MechTouchId.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/ModulePlugins/ModuleACM.bundle/ModuleACM](MACHOS/ModuleACM.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/coreauthd](MACHOS/coreauthd.md)
- [/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond](MACHOS/managedappdistributiond.md)
- [/System/Library/Frameworks/ManagedSettings.framework/ManagedSettingsAgent](MACHOS/ManagedSettingsAgent.md)
- [/System/Library/Frameworks/MapKit.framework/XPCServices/com.apple.MapKit.SnapshotService.xpc/com.apple.MapKit.SnapshotService](MACHOS/com.apple.MapKit.SnapshotService.md)
- [/System/Library/Frameworks/MediaAccessibility.framework/XPCServices/com.apple.accessibility.mediaaccessibilityd.xpc/com.apple.accessibility.mediaaccessibilityd](MACHOS/com.apple.accessibility.mediaaccessibilityd.md)
- [/System/Library/Frameworks/MediaPlayer.framework/PlugIns/MediaPlayerDiagnosticExtension.appex/MediaPlayerDiagnosticExtension](MACHOS/MediaPlayerDiagnosticExtension.md)
- [/System/Library/Frameworks/MediaPlayer.framework/XPCServices/RemotePlayerService.xpc/RemotePlayerService](MACHOS/RemotePlayerService.md)
- [/System/Library/Frameworks/MessageUI.framework/PlugIns/MessageUI.wkbundle/MessageUI](MACHOS/MessageUI.md)
- [/System/Library/Frameworks/Metal.framework/XPCServices/MTLCompilerService.xpc/MTLCompilerService](MACHOS/MTLCompilerService.md)
- [/System/Library/Frameworks/ModelIO.framework/XPCServices/AssetLoader.xpc/AssetLoader](MACHOS/AssetLoader.md)
- [/System/Library/Frameworks/NetworkExtension.framework/PlugIns/NEIKEv2Provider.appex/NEIKEv2Provider](MACHOS/NEIKEv2Provider.md)
- [/System/Library/Frameworks/OSLog.framework/XPCServices/OSLogService.xpc/OSLogService](MACHOS/OSLogService.md)
- [/System/Library/Frameworks/PDFKit.framework/PlugIns/PDFImporter.appex/PDFImporter](MACHOS/PDFImporter.md)
- [/System/Library/Frameworks/PDFKit.framework/PlugIns/com.apple.PDFKit.OFD_Preview.appex/com.apple.PDFKit.OFD_Preview](MACHOS/com.apple.PDFKit.OFD_Preview.md)
- [/System/Library/Frameworks/PDFKit.framework/PlugIns/com.apple.PDFKit.OFD_Thumbnail.appex/com.apple.PDFKit.OFD_Thumbnail](MACHOS/com.apple.PDFKit.OFD_Thumbnail.md)
- [/System/Library/Frameworks/PDFKit.framework/PlugIns/com.apple.PDFKit.PDFExtensionView.appex/com.apple.PDFKit.PDFExtensionView](MACHOS/com.apple.PDFKit.PDFExtensionView.md)
- [/System/Library/Frameworks/PassKit.framework/PlugIns/ApplePayDiagnostics.appex/ApplePayDiagnostics](MACHOS/ApplePayDiagnostics.md)
- [/System/Library/Frameworks/PassKit.framework/PlugIns/PassKitEngagementExtension.appex/PassKitEngagementExtension](MACHOS/PassKitEngagementExtension.md)
- [/System/Library/Frameworks/PassKit.framework/PlugIns/PassKitIntentsExtension.appex/PassKitIntentsExtension](MACHOS/PassKitIntentsExtension.md)
- [/System/Library/Frameworks/PassKit.framework/PlugIns/PassKitIntentsUIExtension.appex/PassKitIntentsUIExtension](MACHOS/PassKitIntentsUIExtension.md)
- [/System/Library/Frameworks/PassKit.framework/PlugIns/PassKitSpotlightIndexExtension.appex/PassKitSpotlightIndexExtension](MACHOS/PassKitSpotlightIndexExtension.md)
- [/System/Library/Frameworks/PassKit.framework/PlugIns/PassKitThumbnailExtension.appex/PassKitThumbnailExtension](MACHOS/PassKitThumbnailExtension.md)
- [/System/Library/Frameworks/ProximityReader.framework/merchantd](MACHOS/merchantd.md)
- [/System/Library/Frameworks/QuickLook.framework/PlugIns/QLWebKitBundle.wkbundle/QLWebKitBundle](MACHOS/QLWebKitBundle.md)
- [/System/Library/Frameworks/QuickLook.framework/PlugIns/com.apple.quicklook.extension.previewUI.appex/com.apple.quicklook.extension.previewUI](MACHOS/com.apple.quicklook.extension.previewUI.md)
- [/System/Library/Frameworks/QuickLookThumbnailing.framework/PlugIns/ThumbnailExtension.appex/ThumbnailExtension](MACHOS/ThumbnailExtension.md)
- [/System/Library/Frameworks/QuickLookThumbnailing.framework/PlugIns/ThumbnailExtensionSecure.appex/ThumbnailExtensionSecure](MACHOS/ThumbnailExtensionSecure.md)
- [/System/Library/Frameworks/QuickLookThumbnailing.framework/Support/com.apple.quicklook.ThumbnailsAgent](MACHOS/com.apple.quicklook.ThumbnailsAgent.md)
- [/System/Library/Frameworks/ReplayKit.framework/PlugIns/RPBroadcastActivityViewControllerExtension.appex/RPBroadcastActivityViewControllerExtension](MACHOS/RPBroadcastActivityViewControllerExtension.md)
- [/System/Library/Frameworks/ReplayKit.framework/PlugIns/RPVideoEditorExtension.appex/RPVideoEditorExtension](MACHOS/RPVideoEditorExtension.md)
- [/System/Library/Frameworks/SafariServices.framework/PlugIns/SafariServices.wkbundle/SafariServices](MACHOS/SafariServices.md)
- [/System/Library/Frameworks/SafariServices.framework/XPCServices/com.apple.SafariServices.ContentBlockerLoader.xpc/com.apple.SafariServices.ContentBlockerLoader](MACHOS/com.apple.SafariServices.ContentBlockerLoader.md)
- [/System/Library/Frameworks/ScreenTime.framework/PlugIns/ScreenTimeWebExtension.appex/ScreenTimeWebExtension](MACHOS/ScreenTimeWebExtension.md)
- [/System/Library/Frameworks/Security.framework/CircleJoinRequested/CircleJoinRequested](MACHOS/CircleJoinRequested.md)
- [/System/Library/Frameworks/Security.framework/CloudKeychainProxy.bundle/CloudKeychainProxy](MACHOS/CloudKeychainProxy.md)
- [/System/Library/Frameworks/Security.framework/XPCServices/TrustedPeersHelper.xpc/TrustedPeersHelper](MACHOS/TrustedPeersHelper.md)
- [/System/Library/Frameworks/Security.framework/XPCServices/XPCAcmeService.xpc/XPCAcmeService](MACHOS/XPCAcmeService.md)
- [/System/Library/Frameworks/Security.framework/swcagent](MACHOS/swcagent.md)
- [/System/Library/Frameworks/SensorKit.framework/PlugIns/SensorKitViewService.appex/SensorKitViewService](MACHOS/SensorKitViewService.md)
- [/System/Library/Frameworks/SensorKit.framework/Support/srsupporttool](MACHOS/srsupporttool.md)
- [/System/Library/Frameworks/SensorKit.framework/XPCServices/SensorKitDataExport.xpc/SensorKitDataExport](MACHOS/SensorKitDataExport.md)
- [/System/Library/Frameworks/SensorKit.framework/XPCServices/com.apple.SensorKit.CHSupportService.xpc/com.apple.SensorKit.CHSupportService](MACHOS/com.apple.SensorKit.CHSupportService.md)
- [/System/Library/Frameworks/SensorKit.framework/XPCServices/com.apple.SensorKitAppHelper.xpc/com.apple.SensorKitAppHelper](MACHOS/com.apple.SensorKitAppHelper.md)
- [/System/Library/Frameworks/ShazamKit.framework/PlugIns/ShazamNotificationContentExtension.appex/ShazamNotificationContentExtension](MACHOS/ShazamNotificationContentExtension.md)
- [/System/Library/Frameworks/ShazamKit.framework/shazamd](MACHOS/shazamd.md)
- [/System/Library/Frameworks/Speech.framework/XPCServices/localspeechrecognition.xpc/localspeechrecognition](MACHOS/localspeechrecognition.md)
- [/System/Library/Frameworks/StoreKit.framework/PlugIns/SKAskPermissionExtension.appex/SKAskPermissionExtension](MACHOS/SKAskPermissionExtension.md)
- [/System/Library/Frameworks/StoreKit.framework/Support/storekitd](MACHOS/storekitd.md)
- [/System/Library/Frameworks/SystemConfiguration.framework/SCHelper](MACHOS/SCHelper.md)
- [/System/Library/Frameworks/UIKit.framework/PlugIns/com.apple.UIKit.ColorPicker.appex/com.apple.UIKit.ColorPicker](MACHOS/com.apple.UIKit.ColorPicker.md)
- [/System/Library/Frameworks/UIKit.framework/PlugIns/com.apple.UIKit.FontPicker.appex/com.apple.UIKit.FontPicker](MACHOS/com.apple.UIKit.FontPicker.md)
- [/System/Library/Frameworks/UIKit.framework/PlugIns/com.apple.UIKit.ShareUI.appex/com.apple.UIKit.ShareUI](MACHOS/com.apple.UIKit.ShareUI.md)
- [/System/Library/Frameworks/UIKit.framework/PlugIns/com.apple.UIKit.TextFormatting.appex/com.apple.UIKit.TextFormatting](MACHOS/com.apple.UIKit.TextFormatting.md)
- [/System/Library/Frameworks/UIKit.framework/PlugIns/com.apple.UIKit.screenpicker.appex/com.apple.UIKit.screenpicker](MACHOS/com.apple.UIKit.screenpicker.md)
- [/System/Library/Frameworks/VideoSubscriberAccount.framework/XPCServices/com.apple.VideoSubscriberAccount.DeveloperService.xpc/com.apple.VideoSubscriberAccount.DeveloperService](MACHOS/com.apple.VideoSubscriberAccount.DeveloperService.md)
- [/System/Library/Frameworks/VideoSubscriberAccount.framework/XPCServices/com.apple.VideoSubscriberAccount.PrivacyService.xpc/com.apple.VideoSubscriberAccount.PrivacyService](MACHOS/com.apple.VideoSubscriberAccount.PrivacyService.md)
- [/System/Library/Frameworks/VideoToolbox.framework/XPCServices/videodecodeservice.xpc/videodecodeservice](MACHOS/videodecodeservice.md)
- [/System/Library/Frameworks/VisionKit.framework/PlugIns/KeyboardCamera.appex/KeyboardCamera](MACHOS/KeyboardCamera.md)
- [/System/Library/Frameworks/WatchKit.framework/Support/companionappd](MACHOS/companionappd.md)
- [/System/Library/Frameworks/WeatherKit.framework/XPCServices/com.apple.weatherkit.authservice.xpc/com.apple.weatherkit.authservice](MACHOS/com.apple.weatherkit.authservice.md)
- [/System/Library/Frameworks/WebKit.framework/Daemons/adattributiond](MACHOS/adattributiond.md)
- [/System/Library/Frameworks/WebKit.framework/XPCServices/com.apple.WebKit.GPU.xpc/com.apple.WebKit.GPU](MACHOS/com.apple.WebKit.GPU.md)
- [/System/Library/Frameworks/WebKit.framework/XPCServices/com.apple.WebKit.Networking.xpc/com.apple.WebKit.Networking](MACHOS/com.apple.WebKit.Networking.md)
- [/System/Library/Frameworks/WebKit.framework/XPCServices/com.apple.WebKit.WebContent.CaptivePortal.xpc/com.apple.WebKit.WebContent.CaptivePortal](MACHOS/com.apple.WebKit.WebContent.CaptivePortal.md)
- [/System/Library/Frameworks/WebKit.framework/XPCServices/com.apple.WebKit.WebContent.xpc/com.apple.WebKit.WebContent](MACHOS/com.apple.WebKit.WebContent.md)
- [/System/Library/Frameworks/_DeviceActivity_SwiftUI.framework/PlugIns/DeviceActivityReportService.appex/DeviceActivityReportService](MACHOS/DeviceActivityReportService.md)
- [/System/Library/HIDPlugins/ColourSensorFilterPlugin.plugin/ColourSensorFilterPlugin](MACHOS/ColourSensorFilterPlugin.md)
- [/System/Library/HIDPlugins/ServiceFilters/AppleProxServiceFilter.plugin/AppleProxServiceFilter](MACHOS/AppleProxServiceFilter.md)
- [/System/Library/HIDPlugins/ServiceFilters/AppleWirelessChargingServiceFilter.plugin/AppleWirelessChargingServiceFilter](MACHOS/AppleWirelessChargingServiceFilter.md)
- [/System/Library/HIDPlugins/ServiceFilters/GamepadHIDServiceFilter.plugin/GamepadHIDServiceFilter](MACHOS/GamepadHIDServiceFilter.md)
- [/System/Library/HIDPlugins/ServiceFilters/SafetyServiceFilter.plugin/SafetyServiceFilter](MACHOS/SafetyServiceFilter.md)
- [/System/Library/HIDPlugins/ServicePlugins/DualSenseHIDServicePlugin.plugin/DualSenseHIDServicePlugin](MACHOS/DualSenseHIDServicePlugin.md)
- [/System/Library/HIDPlugins/ServicePlugins/DualShock4HIDServicePlugin.plugin/DualShock4HIDServicePlugin](MACHOS/DualShock4HIDServicePlugin.md)
- [/System/Library/HIDPlugins/ServicePlugins/GenericGamepadHIDServicePlugin.plugin/GenericGamepadHIDServicePlugin](MACHOS/GenericGamepadHIDServicePlugin.md)
- [/System/Library/HIDPlugins/ServicePlugins/HSTouchHIDService.plugin/HSTouchHIDService](MACHOS/HSTouchHIDService.md)
- [/System/Library/HIDPlugins/ServicePlugins/IOHIDEventServicePlugin.plugin/IOHIDEventServicePlugin](MACHOS/IOHIDEventServicePlugin.md)
- [/System/Library/HIDPlugins/ServicePlugins/JoyConHIDServicePlugin.plugin/JoyConHIDServicePlugin](MACHOS/JoyConHIDServicePlugin.md)
- [/System/Library/HIDPlugins/ServicePlugins/LunaHIDServicePlugin.plugin/LunaHIDServicePlugin](MACHOS/LunaHIDServicePlugin.md)
- [/System/Library/HIDPlugins/ServicePlugins/XboxOneHIDServicePlugin.plugin/XboxOneHIDServicePlugin](MACHOS/XboxOneHIDServicePlugin.md)
- [/System/Library/HIDPlugins/SessionFilters/IOAnalytics.plugin/IOAnalytics](MACHOS/IOAnalytics.md)
- [/System/Library/HIDPlugins/SessionFilters/IOHIDDisplaySessionFilter.plugin/IOHIDDisplaySessionFilter](MACHOS/IOHIDDisplaySessionFilter.md)
- [/System/Library/HIDPlugins/SessionFilters/IOHIDMotionEventSessionFilter.plugin/IOHIDMotionEventSessionFilter](MACHOS/IOHIDMotionEventSessionFilter.md)
- [/System/Library/HIDPlugins/SessionFilters/IOHIDRemoteSensorSessionFilter.plugin/IOHIDRemoteSensorSessionFilter](MACHOS/IOHIDRemoteSensorSessionFilter.md)
- [/System/Library/Health/Plugins/HealthMedicationsDaemonPluginBundle.bundle/HealthMedicationsDaemonPluginBundle](MACHOS/HealthMedicationsDaemonPluginBundle.md)
- [/System/Library/Health/Plugins/HealthRecordsPlugin.bundle/HealthRecordsPlugin](MACHOS/HealthRecordsPlugin.md)
- [/System/Library/Health/Plugins/HearingDaemonPlugin.bundle/HearingDaemonPlugin](MACHOS/HearingDaemonPlugin.md)
- [/System/Library/Health/Plugins/MentalHealthDaemonPlugin.bundle/MentalHealthDaemonPlugin](MACHOS/MentalHealthDaemonPlugin.md)
- [/System/Library/Health/Plugins/MobilityDaemonPlugin.bundle/MobilityDaemonPlugin](MACHOS/MobilityDaemonPlugin.md)
- [/System/Library/Health/Plugins/SummariesHealthDaemonPlugin.bundle/SummariesHealthDaemonPlugin](MACHOS/SummariesHealthDaemonPlugin.md)
- [/System/Library/Health/Plugins/WorkoutHealthPlugin.bundle/WorkoutHealthPlugin](MACHOS/WorkoutHealthPlugin.md)
- [/System/Library/KerberosPlugins/GSSAPI/AppSSOReplacePlugin_iOS.bundle/AppSSOReplacePlugin_iOS](MACHOS/AppSSOReplacePlugin_iOS.md)
- [/System/Library/KerberosPlugins/KerberosFrameworkPlugins/AppSSOConfigPlugin_iOS.bundle/AppSSOConfigPlugin_iOS](MACHOS/AppSSOConfigPlugin_iOS.md)
- [/System/Library/KerberosPlugins/KerberosFrameworkPlugins/AppSSOLocatePlugin_iOS.bundle/AppSSOLocatePlugin_iOS](MACHOS/AppSSOLocatePlugin_iOS.md)
- [/System/Library/LocationBundles/AltimeterHarvest.bundle/AltimeterHarvest](MACHOS/AltimeterHarvest.md)
- [/System/Library/LocationBundles/AppGenius.bundle/AppGenius](MACHOS/AppGenius.md)
- [/System/Library/LocationBundles/AppSuggestions.bundle/AppSuggestions](MACHOS/AppSuggestions.md)
- [/System/Library/LocationBundles/CompassCalibration.bundle/CompassCalibration](MACHOS/CompassCalibration.md)
- [/System/Library/LocationBundles/CountryTracker.bundle/CountryTracker](MACHOS/CountryTracker.md)
- [/System/Library/LocationBundles/DestinationdLocationBundleiOS.bundle/DestinationdLocationBundleiOS](MACHOS/DestinationdLocationBundleiOS.md)
- [/System/Library/LocationBundles/DoNotDisturb.bundle/DoNotDisturb](MACHOS/DoNotDisturb.md)
- [/System/Library/LocationBundles/GeocorrectionDLocationBundle.bundle/GeocorrectionDLocationBundle](MACHOS/GeocorrectionDLocationBundle.md)
- [/System/Library/LocationBundles/HandwashingLocation.bundle/HandwashingLocation](MACHOS/HandwashingLocation.md)
- [/System/Library/LocationBundles/IonosphereHarvest.bundle/IonosphereHarvest](MACHOS/IonosphereHarvest.md)
- [/System/Library/LocationBundles/LocationFenceSync.bundle/LocationFenceSync](MACHOS/LocationFenceSync.md)
- [/System/Library/LocationBundles/LocationPromptUI.bundle/LocationPromptUI](MACHOS/LocationPromptUI.md)
- [/System/Library/LocationBundles/MapsAnnouncements.bundle/MapsAnnouncements](MACHOS/MapsAnnouncements.md)
- [/System/Library/LocationBundles/MicroLocation.bundle/MicroLocation](MACHOS/MicroLocation.md)
- [/System/Library/LocationBundles/MotionCalibration.bundle/MotionCalibration](MACHOS/MotionCalibration.md)
- [/System/Library/LocationBundles/NavdLocationBundleiOS.bundle/NavdLocationBundleiOS](MACHOS/NavdLocationBundleiOS.md)
- [/System/Library/LocationBundles/PLAMonitor.bundle/PLAMonitor](MACHOS/PLAMonitor.md)
- [/System/Library/LocationBundles/RemindersAlerts.bundle/RemindersAlerts](MACHOS/RemindersAlerts.md)
- [/System/Library/LocationBundles/SafetyAlerts.bundle/SafetyAlerts](MACHOS/SafetyAlerts.md)
- [/System/Library/LocationBundles/ShortcutsLocation.bundle/ShortcutsLocation](MACHOS/ShortcutsLocation.md)
- [/System/Library/LocationBundles/SystemCustomization.bundle/SystemCustomization](MACHOS/SystemCustomization.md)
- [/System/Library/LocationBundles/TimeZone.bundle/TimeZone](MACHOS/TimeZone.md)
- [/System/Library/LocationBundles/TraceHarvest.bundle/TraceHarvest](MACHOS/TraceHarvest.md)
- [/System/Library/LocationBundles/Traffic.bundle/Traffic](MACHOS/Traffic.md)
- [/System/Library/MediaStreamPlugins/PhotoSharingPlugin.mediastream/PhotoSharingPlugin](MACHOS/PhotoSharingPlugin.md)
- [/System/Library/Messages/iMessageApps/AnimojiCameraApp.bundle/AnimojiCameraApp](MACHOS/AnimojiCameraApp.md)
- [/System/Library/Messages/iMessageApps/AudioMessagesExtension.bundle/AudioMessagesExtension](MACHOS/AudioMessagesExtension.md)
- [/System/Library/Messages/iMessageApps/FindMyMessagesApp.bundle/FindMyMessagesApp](MACHOS/FindMyMessagesApp.md)
- [/System/Library/Messages/iMessageApps/FunCameraFilters.bundle/FunCameraFilters](MACHOS/FunCameraFilters.md)
- [/System/Library/Messages/iMessageApps/SafetyMonitorMessages.bundle/SafetyMonitorMessages](MACHOS/SafetyMonitorMessages.md)
- [/System/Library/Messages/iMessageBalloons/ASMessagesProvider.bundle/ASMessagesProvider](MACHOS/ASMessagesProvider.md)
- [/System/Library/Messages/iMessageBalloons/DigitalTouchBalloonProvider.bundle/DigitalTouchBalloonProvider](MACHOS/DigitalTouchBalloonProvider.md)
- [/System/Library/Messages/iMessageBalloons/HandwritingProvider.bundle/HandwritingProvider](MACHOS/HandwritingProvider.md)
- [/System/Library/Messages/iMessageBalloons/MSMessageExtensionBalloonPlugin.bundle/MSMessageExtensionBalloonPlugin](MACHOS/MSMessageExtensionBalloonPlugin.md)
- [/System/Library/Messages/iMessageBalloons/RichLinkProvider.bundle/RichLinkProvider](MACHOS/RichLinkProvider.md)
- [/System/Library/Messages/iMessageEffects/CKConfettiEffect.bundle/CKConfettiEffect](MACHOS/CKConfettiEffect.md)
- [/System/Library/Messages/iMessageEffects/CKEchoEffect.bundle/CKEchoEffect](MACHOS/CKEchoEffect.md)
- [/System/Library/Messages/iMessageEffects/CKFireworksEffect.bundle/CKFireworksEffect](MACHOS/CKFireworksEffect.md)
- [/System/Library/Messages/iMessageEffects/CKHappyBirthdayEffect.bundle/CKHappyBirthdayEffect](MACHOS/CKHappyBirthdayEffect.md)
- [/System/Library/Messages/iMessageEffects/CKHeartEffect.bundle/CKHeartEffect](MACHOS/CKHeartEffect.md)
- [/System/Library/Messages/iMessageEffects/CKLasersEffect.bundle/CKLasersEffect](MACHOS/CKLasersEffect.md)
- [/System/Library/Messages/iMessageEffects/CKShootingStarEffect.bundle/CKShootingStarEffect](MACHOS/CKShootingStarEffect.md)
- [/System/Library/Messages/iMessageEffects/CKSparklesEffect.bundle/CKSparklesEffect](MACHOS/CKSparklesEffect.md)
- [/System/Library/Messages/iMessageEffects/CKSpotlightEffect.bundle/CKSpotlightEffect](MACHOS/CKSpotlightEffect.md)
- [/System/Library/NanoPreferenceBundles/Applications/BridgeAppStoreDaemonSettings.bundle/BridgeAppStoreDaemonSettings](MACHOS/BridgeAppStoreDaemonSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/BridgeHealthSettings.bundle/BridgeHealthSettings](MACHOS/BridgeHealthSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/BridgeRemoteAccounts.bundle/BridgeRemoteAccounts](MACHOS/BridgeRemoteAccounts.md)
- [/System/Library/NanoPreferenceBundles/Applications/BrookBridgeSettings.bundle/BrookBridgeSettings](MACHOS/BrookBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/DeepBreathingSettings.bundle/DeepBreathingSettings](MACHOS/DeepBreathingSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/DepthCompanionSettings.bundle/DepthCompanionSettings](MACHOS/DepthCompanionSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/DoseSettings.bundle/DoseSettings](MACHOS/DoseSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/FindMyNotificationsSettings.bundle/FindMyNotificationsSettings](MACHOS/FindMyNotificationsSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/HealthAppsSettings.bundle/HealthAppsSettings](MACHOS/HealthAppsSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/HeartRateSettings.bundle/HeartRateSettings](MACHOS/HeartRateSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/MessagesBridgeSettings.bundle/MessagesBridgeSettings](MACHOS/MessagesBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/MindSettings.bundle/MindSettings](MACHOS/MindSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/NanoBedtimeBridgeSettings.bundle/NanoBedtimeBridgeSettings](MACHOS/NanoBedtimeBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/NanoBooksBridgeSettings.bundle/NanoBooksBridgeSettings](MACHOS/NanoBooksBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/NanoCalendarBridgeSettings.bundle/NanoCalendarBridgeSettings](MACHOS/NanoCalendarBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/NanoClockBridgeSettings.bundle/NanoClockBridgeSettings](MACHOS/NanoClockBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/NanoContactsBridgeSettingsOther.bundle/NanoContactsBridgeSettingsOther](MACHOS/NanoContactsBridgeSettingsOther.md)
- [/System/Library/NanoPreferenceBundles/Applications/NanoContactsBridgeSettingsPaired.bundle/NanoContactsBridgeSettingsPaired](MACHOS/NanoContactsBridgeSettingsPaired.md)
- [/System/Library/NanoPreferenceBundles/Applications/NanoMailBridgeSettings.bundle/NanoMailBridgeSettings](MACHOS/NanoMailBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/NanoMapsBridgeSettings.bundle/NanoMapsBridgeSettings](MACHOS/NanoMapsBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/NanoMenstrualCyclesCompanionSettings.bundle/NanoMenstrualCyclesCompanionSettings](MACHOS/NanoMenstrualCyclesCompanionSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/NanoMusicBridgeSettings.bundle/NanoMusicBridgeSettings](MACHOS/NanoMusicBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/NanoPassbookBridgeSettings.bundle/NanoPassbookBridgeSettings](MACHOS/NanoPassbookBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/NanoPhotosBridgeSettings.bundle/NanoPhotosBridgeSettings](MACHOS/NanoPhotosBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/NanoTipsBridgeSettings.bundle/NanoTipsBridgeSettings](MACHOS/NanoTipsBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/OxygenSaturationSettings.bundle/OxygenSaturationSettings](MACHOS/OxygenSaturationSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/PhoneBridgeSettings.bundle/PhoneBridgeSettings](MACHOS/PhoneBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/PodcastsBridgeSettings.bundle/PodcastsBridgeSettings](MACHOS/PodcastsBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/SessionTrackerAppSettings.bundle/SessionTrackerAppSettings](MACHOS/SessionTrackerAppSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/StocksBridgeSettings.bundle/StocksBridgeSettings](MACHOS/StocksBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/TinCanSettings.bundle/TinCanSettings](MACHOS/TinCanSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/WeatherExtensionBridgeSettings.bundle/WeatherExtensionBridgeSettings](MACHOS/WeatherExtensionBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/Customization/CarouselAppViewSettings.bundle/CarouselAppViewSettings](MACHOS/CarouselAppViewSettings.md)
- [/System/Library/NanoPreferenceBundles/Customization/CarouselLayoutSettings.bundle/CarouselLayoutSettings](MACHOS/CarouselLayoutSettings.md)
- [/System/Library/NanoPreferenceBundles/Customization/NTKCustomization.bundle/NTKCustomization](MACHOS/NTKCustomization.md)
- [/System/Library/NanoPreferenceBundles/Discover/AppsForYourWatchPlugin.bundle/AppsForYourWatchPlugin](MACHOS/AppsForYourWatchPlugin.md)
- [/System/Library/NanoPreferenceBundles/Discover/CustomizeYourWatchPlugin.bundle/CustomizeYourWatchPlugin](MACHOS/CustomizeYourWatchPlugin.md)
- [/System/Library/NanoPreferenceBundles/Discover/GetToKnowCurrentSeriesPlugin.bundle/GetToKnowCurrentSeriesPlugin](MACHOS/GetToKnowCurrentSeriesPlugin.md)
- [/System/Library/NanoPreferenceBundles/Discover/HealthAndFitnessPlugin.bundle/HealthAndFitnessPlugin](MACHOS/HealthAndFitnessPlugin.md)
- [/System/Library/NanoPreferenceBundles/Discover/UserGuidePlugin.bundle/UserGuidePlugin](MACHOS/UserGuidePlugin.md)
- [/System/Library/NanoPreferenceBundles/Discover/WelcomeToAppleWatchPlugin.bundle/WelcomeToAppleWatchPlugin](MACHOS/WelcomeToAppleWatchPlugin.md)
- [/System/Library/NanoPreferenceBundles/Discover/WhatsNewPlugin.bundle/WhatsNewPlugin](MACHOS/WhatsNewPlugin.md)
- [/System/Library/NanoPreferenceBundles/General/AssistantBridgeSettings.bundle/AssistantBridgeSettings](MACHOS/AssistantBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/General/CellularBridgeSettings.bundle/CellularBridgeSettings](MACHOS/CellularBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/General/CompanionAppBacklightPrivacySettings.bundle/CompanionAppBacklightPrivacySettings](MACHOS/CompanionAppBacklightPrivacySettings.md)
- [/System/Library/NanoPreferenceBundles/General/CompanionAutoLaunchSettings.bundle/CompanionAutoLaunchSettings](MACHOS/CompanionAutoLaunchSettings.md)
- [/System/Library/NanoPreferenceBundles/General/CompanionBARSettings.bundle/CompanionBARSettings](MACHOS/CompanionBARSettings.md)
- [/System/Library/NanoPreferenceBundles/General/CompanionComplicationSettings.bundle/CompanionComplicationSettings](MACHOS/CompanionComplicationSettings.md)
- [/System/Library/NanoPreferenceBundles/General/CompanionDockSettings.bundle/CompanionDockSettings](MACHOS/CompanionDockSettings.md)
- [/System/Library/NanoPreferenceBundles/General/CompanionInternationalSettings.bundle/CompanionInternationalSettings](MACHOS/CompanionInternationalSettings.md)
- [/System/Library/NanoPreferenceBundles/General/CompanionNotificationSettings.bundle/CompanionNotificationSettings](MACHOS/CompanionNotificationSettings.md)
- [/System/Library/NanoPreferenceBundles/General/CompanionReturnToClockSettings.bundle/CompanionReturnToClockSettings](MACHOS/CompanionReturnToClockSettings.md)
- [/System/Library/NanoPreferenceBundles/General/CompanionStingSettings.bundle/CompanionStingSettings](MACHOS/CompanionStingSettings.md)
- [/System/Library/NanoPreferenceBundles/General/CompanionWakeSettings.bundle/CompanionWakeSettings](MACHOS/CompanionWakeSettings.md)
- [/System/Library/NanoPreferenceBundles/General/NTKCTritiumSettings.bundle/NTKCTritiumSettings](MACHOS/NTKCTritiumSettings.md)
- [/System/Library/NanoPreferenceBundles/General/PairedUnlockSettings.bundle/PairedUnlockSettings](MACHOS/PairedUnlockSettings.md)
- [/System/Library/NanoPreferenceBundles/General/SchoolTimePhoneSettings.bundle/SchoolTimePhoneSettings](MACHOS/SchoolTimePhoneSettings.md)
- [/System/Library/NanoPreferenceBundles/General/WGAEltonUsersSettingsPhone.bundle/WGAEltonUsersSettingsPhone](MACHOS/WGAEltonUsersSettingsPhone.md)
- [/System/Library/NanoPreferenceBundles/PrivacySettings/HealthBridgePrivacySettings.bundle/HealthBridgePrivacySettings](MACHOS/HealthBridgePrivacySettings.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/AccessibilityBridgeSetup.bundle/AccessibilityBridgeSetup](MACHOS/AccessibilityBridgeSetup.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/ActivityBridgeSetup.bundle/ActivityBridgeSetup](MACHOS/ActivityBridgeSetup.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/BPSStingSetup.bundle/BPSStingSetup](MACHOS/BPSStingSetup.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/CellularSetupBridgeBuddyUI.bundle/CellularSetupBridgeBuddyUI](MACHOS/CellularSetupBridgeBuddyUI.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/CompanionAppViewSetup.bundle/CompanionAppViewSetup](MACHOS/CompanionAppViewSetup.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/DepthCompanionSetup.bundle/DepthCompanionSetup](MACHOS/DepthCompanionSetup.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/HealthBridgeSetupPlugin.bundle/HealthBridgeSetupPlugin](MACHOS/HealthBridgeSetupPlugin.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/HealthFeaturesBridgeSetupPlugin.bundle/HealthFeaturesBridgeSetupPlugin](MACHOS/HealthFeaturesBridgeSetupPlugin.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/HeartRateBridgePlugin.bundle/HeartRateBridgePlugin](MACHOS/HeartRateBridgePlugin.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/MessagesPairingRegistration.bundle/MessagesPairingRegistration](MACHOS/MessagesPairingRegistration.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/NanoContactsBridgeSetup.bundle/NanoContactsBridgeSetup](MACHOS/NanoContactsBridgeSetup.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/NanoPhotosBridgeSetup.bundle/NanoPhotosBridgeSetup](MACHOS/NanoPhotosBridgeSetup.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/RespiratoryHealthSetupPlugin.bundle/RespiratoryHealthSetupPlugin](MACHOS/RespiratoryHealthSetupPlugin.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/SchoolTimeSetup.bundle/SchoolTimeSetup](MACHOS/SchoolTimeSetup.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/SiriWatchPairingSetup.bundle/SiriWatchPairingSetup](MACHOS/SiriWatchPairingSetup.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/TextSettingsBridgeSetup.bundle/TextSettingsBridgeSetup](MACHOS/TextSettingsBridgeSetup.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/WGAEltonPhoneBuddyFlowPanel.bundle/WGAEltonPhoneBuddyFlowPanel](MACHOS/WGAEltonPhoneBuddyFlowPanel.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/ActivityComplicationBundleCompanion.bundle/ActivityComplicationBundleCompanion](MACHOS/ActivityComplicationBundleCompanion.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/DepthComplicationBundleCompanion.bundle/DepthComplicationBundleCompanion](MACHOS/DepthComplicationBundleCompanion.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/DoseComplicationsCompanion.bundle/DoseComplicationsCompanion](MACHOS/DoseComplicationsCompanion.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/HearingDevicesComplicationContainerCompanion.bundle/HearingDevicesComplicationContainerCompanion](MACHOS/HearingDevicesComplicationContainerCompanion.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/MindComplicationBundleCompanion.bundle/MindComplicationBundleCompanion](MACHOS/MindComplicationBundleCompanion.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/NTKCellularConnectivityCompanionComplicationBundle.bundle/NTKCellularConnectivityCompanionComplicationBundle](MACHOS/NTKCellularConnectivityCompanionComplicationBundle.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/NTKTimelyComplications.bundle/NTKTimelyComplications](MACHOS/NTKTimelyComplications.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/NTKTimerComplicationBundle.bundle/NTKTimerComplicationBundle](MACHOS/NTKTimerComplicationBundle.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/NanoCalendarComplicationsCompanion.bundle/NanoCalendarComplicationsCompanion](MACHOS/NanoCalendarComplicationsCompanion.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/NanoCameraComplication.bundle/NanoCameraComplication](MACHOS/NanoCameraComplication.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/NanoMapsComplications.bundle/NanoMapsComplications](MACHOS/NanoMapsComplications.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/NanoRemindersComplication.bundle/NanoRemindersComplication](MACHOS/NanoRemindersComplication.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/VoiceMemosComplication.bundle/VoiceMemosComplication](MACHOS/VoiceMemosComplication.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/WorkoutComplicationBundleCompanion.bundle/WorkoutComplicationBundleCompanion](MACHOS/WorkoutComplicationBundleCompanion.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/com.apple.finddevices.complications.bundle/com.apple.finddevices.complications](MACHOS/com.apple.finddevices.complications.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/com.apple.finditems.complications.bundle/com.apple.finditems.complications](MACHOS/com.apple.finditems.complications.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/com.apple.findpeople.complications.bundle/com.apple.findpeople.complications](MACHOS/com.apple.findpeople.complications.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKActivityFaceBundleCompanion.bundle/NTKActivityFaceBundleCompanion](MACHOS/NTKActivityFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKAkitaFaceBundleCompanion.bundle/NTKAkitaFaceBundleCompanion](MACHOS/NTKAkitaFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKAlaskanFaceBundleCompanion.bundle/NTKAlaskanFaceBundleCompanion](MACHOS/NTKAlaskanFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKBigNumeralsAnalogFaceBundleCompanion.bundle/NTKBigNumeralsAnalogFaceBundleCompanion](MACHOS/NTKBigNumeralsAnalogFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKBigNumeralsDigitalFaceBundleCompanion.bundle/NTKBigNumeralsDigitalFaceBundleCompanion](MACHOS/NTKBigNumeralsDigitalFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKBreatheFaceBundle.bundle/NTKBreatheFaceBundle](MACHOS/NTKBreatheFaceBundle.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKCaliforniaFaceBundleCompanion.bundle/NTKCaliforniaFaceBundleCompanion](MACHOS/NTKCaliforniaFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKCharacterFaceBundleCompanion.bundle/NTKCharacterFaceBundleCompanion](MACHOS/NTKCharacterFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKChronographFaceBundleCompanion.bundle/NTKChronographFaceBundleCompanion](MACHOS/NTKChronographFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKCloudrakerFaceBundleCompanion.bundle/NTKCloudrakerFaceBundleCompanion](MACHOS/NTKCloudrakerFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKCollieFaceBundleCompanion.bundle/NTKCollieFaceBundleCompanion](MACHOS/NTKCollieFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKColorAnalogFaceBundleCompanion.bundle/NTKColorAnalogFaceBundleCompanion](MACHOS/NTKColorAnalogFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKColtanFaceBundleCompanion.bundle/NTKColtanFaceBundleCompanion](MACHOS/NTKColtanFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKCrosswindFaceBundleCompanion.bundle/NTKCrosswindFaceBundleCompanion](MACHOS/NTKCrosswindFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKDigitalModularFaceBundleCompanion.bundle/NTKDigitalModularFaceBundleCompanion](MACHOS/NTKDigitalModularFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKExplorerFaceBundleCompanion.bundle/NTKExplorerFaceBundleCompanion](MACHOS/NTKExplorerFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKExtraLargeFaceBundleCompanion.bundle/NTKExtraLargeFaceBundleCompanion](MACHOS/NTKExtraLargeFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKFireWaterFaceBundle.bundle/NTKFireWaterFaceBundle](MACHOS/NTKFireWaterFaceBundle.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKGladiusFaceBundleCompanion.bundle/NTKGladiusFaceBundleCompanion](MACHOS/NTKGladiusFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKGlobetrotterFaceBundleCompanion.bundle/NTKGlobetrotterFaceBundleCompanion](MACHOS/NTKGlobetrotterFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKGreyhoundFaceBundleCompanion.bundle/NTKGreyhoundFaceBundleCompanion](MACHOS/NTKGreyhoundFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKInfographFaceBundle.bundle/NTKInfographFaceBundle](MACHOS/NTKInfographFaceBundle.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKInfographModularFaceBundle.bundle/NTKInfographModularFaceBundle](MACHOS/NTKInfographModularFaceBundle.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKKuiperFaceBundleCompanion.bundle/NTKKuiperFaceBundleCompanion](MACHOS/NTKKuiperFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKLilypadFaceBundleCompanion.bundle/NTKLilypadFaceBundleCompanion](MACHOS/NTKLilypadFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKLiquidMetalFaceBundle.bundle/NTKLiquidMetalFaceBundle](MACHOS/NTKLiquidMetalFaceBundle.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKMagmaFaceBundleCompanion.bundle/NTKMagmaFaceBundleCompanion](MACHOS/NTKMagmaFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKMargaritaFaceBundleCompanion.bundle/NTKMargaritaFaceBundleCompanion](MACHOS/NTKMargaritaFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKMotionFaceBundle.bundle/NTKMotionFaceBundle](MACHOS/NTKMotionFaceBundle.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKNumeralsAnalogFaceBundleCompanion.bundle/NTKNumeralsAnalogFaceBundleCompanion](MACHOS/NTKNumeralsAnalogFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKOlympusFaceBundleCompanion.bundle/NTKOlympusFaceBundleCompanion](MACHOS/NTKOlympusFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKParameciumFaceBundleCompanion.bundle/NTKParameciumFaceBundleCompanion](MACHOS/NTKParameciumFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKPrideWeaveFaceBundleCompanion.bundle/NTKPrideWeaveFaceBundleCompanion](MACHOS/NTKPrideWeaveFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKProteusFaceBundleCompanion.bundle/NTKProteusFaceBundleCompanion](MACHOS/NTKProteusFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKRenegadeFaceBundleCompanion.bundle/NTKRenegadeFaceBundleCompanion](MACHOS/NTKRenegadeFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKSeltzerFaceBundleCompanion.bundle/NTKSeltzerFaceBundleCompanion](MACHOS/NTKSeltzerFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKShibaFaceBundleCompanion.bundle/NTKShibaFaceBundleCompanion](MACHOS/NTKShibaFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKSimpleFaceBundleCompanion.bundle/NTKSimpleFaceBundleCompanion](MACHOS/NTKSimpleFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKSolarsFaceBundleCompanion.bundle/NTKSolarsFaceBundleCompanion](MACHOS/NTKSolarsFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKSpectrumFaceBundleCompanion.bundle/NTKSpectrumFaceBundleCompanion](MACHOS/NTKSpectrumFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKTimelapseFaceBundle.bundle/NTKTimelapseFaceBundle](MACHOS/NTKTimelapseFaceBundle.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKToyStoryFaceBundle.bundle/NTKToyStoryFaceBundle](MACHOS/NTKToyStoryFaceBundle.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKUltraCubeFaceBundleCompanion.bundle/NTKUltraCubeFaceBundleCompanion](MACHOS/NTKUltraCubeFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKUtilityFaceBundleCompanion.bundle/NTKUtilityFaceBundleCompanion](MACHOS/NTKUtilityFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKVaporFaceBundle.bundle/NTKVaporFaceBundle](MACHOS/NTKVaporFaceBundle.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKVictoryAnalogFaceBundleCompanion.bundle/NTKVictoryAnalogFaceBundleCompanion](MACHOS/NTKVictoryAnalogFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKVictoryDigitalFaceBundleCompanion.bundle/NTKVictoryDigitalFaceBundleCompanion](MACHOS/NTKVictoryDigitalFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKZeusFaceBundleCompanion.bundle/NTKZeusFaceBundleCompanion](MACHOS/NTKZeusFaceBundleCompanion.md)
- [/System/Library/PreferenceBundles/AccessibilitySettings.bundle/AccessibilitySettings](MACHOS/AccessibilitySettings.md)
- [/System/Library/PreferenceBundles/AccessoryDeveloperSettings.bundle/AccessoryDeveloperSettings](MACHOS/AccessoryDeveloperSettings.md)
- [/System/Library/PreferenceBundles/AccountSettings/ActiveSyncSettings.bundle/ActiveSyncSettings](MACHOS/ActiveSyncSettings.md)
- [/System/Library/PreferenceBundles/AccountSettings/AppleAccountSettings.bundle/AppleAccountSettings](MACHOS/AppleAccountSettings.md)
- [/System/Library/PreferenceBundles/AccountSettings/CloudKitSettings.bundle/CloudKitSettings](MACHOS/CloudKitSettings.md)
- [/System/Library/PreferenceBundles/AccountSettings/DAVSettings.bundle/DAVSettings](MACHOS/DAVSettings.md)
- [/System/Library/PreferenceBundles/AccountSettings/LDAPSettings.bundle/LDAPSettings](MACHOS/LDAPSettings.md)
- [/System/Library/PreferenceBundles/AccountSettings/MailAccountSettings.bundle/MailAccountSettings](MACHOS/MailAccountSettings.md)
- [/System/Library/PreferenceBundles/AccountSettings/RemoteManagementAccountSettings.bundle/RemoteManagementAccountSettings](MACHOS/RemoteManagementAccountSettings.md)
- [/System/Library/PreferenceBundles/AccountSettings/SubscribedCalendarSettings.bundle/SubscribedCalendarSettings](MACHOS/SubscribedCalendarSettings.md)
- [/System/Library/PreferenceBundles/AccountSettings/icloudCalendarSettings.bundle/icloudCalendarSettings](MACHOS/icloudCalendarSettings.md)
- [/System/Library/PreferenceBundles/AccountSettings/icloudMailSettings.bundle/icloudMailSettings](MACHOS/icloudMailSettings.md)
- [/System/Library/PreferenceBundles/AccountSettingsUI.bundle/AccountSettingsUI](MACHOS/AccountSettingsUI.md)
- [/System/Library/PreferenceBundles/ActionButtonSettings.bundle/ActionButtonSettings](MACHOS/ActionButtonSettings.md)
- [/System/Library/PreferenceBundles/ActivitySettings.bundle/ActivitySettings](MACHOS/ActivitySettings.md)
- [/System/Library/PreferenceBundles/AmbientSettings.bundle/AmbientSettings](MACHOS/AmbientSettings.md)
- [/System/Library/PreferenceBundles/AppClipDeveloperSettings.bundle/AppClipDeveloperSettings](MACHOS/AppClipDeveloperSettings.md)
- [/System/Library/PreferenceBundles/AppleEthernetSettingsPreferences.bundle/AppleEthernetSettingsPreferences](MACHOS/AppleEthernetSettingsPreferences.md)
- [/System/Library/PreferenceBundles/ApplicationSettingsWrapper.bundle/ApplicationSettingsWrapper](MACHOS/ApplicationSettingsWrapper.md)
- [/System/Library/PreferenceBundles/AssistantSettings.bundle/AssistantSettings](MACHOS/AssistantSettings.md)
- [/System/Library/PreferenceBundles/BatteryUsageUI.bundle/BatteryUsageUI](MACHOS/BatteryUsageUI.md)
- [/System/Library/PreferenceBundles/BlocklistSettings.bundle/BlocklistSettings](MACHOS/BlocklistSettings.md)
- [/System/Library/PreferenceBundles/CallDirectorySettings.bundle/CallDirectorySettings](MACHOS/CallDirectorySettings.md)
- [/System/Library/PreferenceBundles/CallForwardingTelephonySettings.bundle/CallForwardingTelephonySettings](MACHOS/CallForwardingTelephonySettings.md)
- [/System/Library/PreferenceBundles/CallScreeningSettingsBundle.bundle/CallScreeningSettingsBundle](MACHOS/CallScreeningSettingsBundle.md)
- [/System/Library/PreferenceBundles/CallWaitingTelephonySettings.bundle/CallWaitingTelephonySettings](MACHOS/CallWaitingTelephonySettings.md)
- [/System/Library/PreferenceBundles/CallingLineIdRestrictionTelephonySettings.bundle/CallingLineIdRestrictionTelephonySettings](MACHOS/CallingLineIdRestrictionTelephonySettings.md)
- [/System/Library/PreferenceBundles/CameraSettings.bundle/CameraSettings](MACHOS/CameraSettings.md)
- [/System/Library/PreferenceBundles/CarKitSettings.bundle/CarKitSettings](MACHOS/CarKitSettings.md)
- [/System/Library/PreferenceBundles/CellularNetworkTelephonySettings.bundle/CellularNetworkTelephonySettings](MACHOS/CellularNetworkTelephonySettings.md)
- [/System/Library/PreferenceBundles/ClarityUICameraSettings.bundle/ClarityUICameraSettings](MACHOS/ClarityUICameraSettings.md)
- [/System/Library/PreferenceBundles/ClarityUIMessagesSettings.bundle/ClarityUIMessagesSettings](MACHOS/ClarityUIMessagesSettings.md)
- [/System/Library/PreferenceBundles/ClarityUIMusicSettings.bundle/ClarityUIMusicSettings](MACHOS/ClarityUIMusicSettings.md)
- [/System/Library/PreferenceBundles/ClarityUIPhoneFaceTimeSettings.bundle/ClarityUIPhoneFaceTimeSettings](MACHOS/ClarityUIPhoneFaceTimeSettings.md)
- [/System/Library/PreferenceBundles/ClarityUIPhotosSettings.bundle/ClarityUIPhotosSettings](MACHOS/ClarityUIPhotosSettings.md)
- [/System/Library/PreferenceBundles/ClassKitDeveloperSettings.bundle/ClassKitDeveloperSettings](MACHOS/ClassKitDeveloperSettings.md)
- [/System/Library/PreferenceBundles/ClassKitSettings.bundle/ClassKitSettings](MACHOS/ClassKitSettings.md)
- [/System/Library/PreferenceBundles/ClassificationAndReportingSettingsBundle.bundle/ClassificationAndReportingSettingsBundle](MACHOS/ClassificationAndReportingSettingsBundle.md)
- [/System/Library/PreferenceBundles/CommunicationSafetySettings.bundle/CommunicationSafetySettings](MACHOS/CommunicationSafetySettings.md)
- [/System/Library/PreferenceBundles/CompassSettings.bundle/CompassSettings](MACHOS/CompassSettings.md)
- [/System/Library/PreferenceBundles/ConferenceExternalSettings.bundle/ConferenceExternalSettings](MACHOS/ConferenceExternalSettings.md)
- [/System/Library/PreferenceBundles/ConferenceRegistrationSettings.bundle/ConferenceRegistrationSettings](MACHOS/ConferenceRegistrationSettings.md)
- [/System/Library/PreferenceBundles/ControlCenterSettings.bundle/ControlCenterSettings](MACHOS/ControlCenterSettings.md)
- [/System/Library/PreferenceBundles/CoreRoutineSettings.bundle/CoreRoutineSettings](MACHOS/CoreRoutineSettings.md)
- [/System/Library/PreferenceBundles/DeveloperSettings.bundle/DeveloperSettings](MACHOS/DeveloperSettings.md)
- [/System/Library/PreferenceBundles/DeviceManagementClientDeveloperSettings.bundle/DeviceManagementClientDeveloperSettings](MACHOS/DeviceManagementClientDeveloperSettings.md)
- [/System/Library/PreferenceBundles/DialAssistTelephonySettings.bundle/DialAssistTelephonySettings](MACHOS/DialAssistTelephonySettings.md)
- [/System/Library/PreferenceBundles/DictionarySettings.bundle/DictionarySettings](MACHOS/DictionarySettings.md)
- [/System/Library/PreferenceBundles/DigitalSeparationSettings.bundle/DigitalSeparationSettings](MACHOS/DigitalSeparationSettings.md)
- [/System/Library/PreferenceBundles/DriverKitSettings.bundle/DriverKitSettings](MACHOS/DriverKitSettings.md)
- [/System/Library/PreferenceBundles/ENDeveloperSettings.bundle/ENDeveloperSettings](MACHOS/ENDeveloperSettings.md)
- [/System/Library/PreferenceBundles/EmergencyAlertExtension.bundle/EmergencyAlertExtension](MACHOS/EmergencyAlertExtension.md)
- [/System/Library/PreferenceBundles/ExposureNotificationSettingsUI.bundle/ExposureNotificationSettingsUI](MACHOS/ExposureNotificationSettingsUI.md)
- [/System/Library/PreferenceBundles/FitnessSettings.bundle/FitnessSettings](MACHOS/FitnessSettings.md)
- [/System/Library/PreferenceBundles/FocusSettings.bundle/FocusSettings](MACHOS/FocusSettings.md)
- [/System/Library/PreferenceBundles/FontSettings.bundle/FontSettings](MACHOS/FontSettings.md)
- [/System/Library/PreferenceBundles/FreeformSettings.bundle/FreeformSettings](MACHOS/FreeformSettings.md)
- [/System/Library/PreferenceBundles/GameCenterSettings.bundle/GameCenterSettings](MACHOS/GameCenterSettings.md)
- [/System/Library/PreferenceBundles/GameControlleriOSSettings.bundle/GameControlleriOSSettings](MACHOS/GameControlleriOSSettings.md)
- [/System/Library/PreferenceBundles/HealthRecordsSettings.bundle/HealthRecordsSettings](MACHOS/HealthRecordsSettings.md)
- [/System/Library/PreferenceBundles/HealthSettings.bundle/HealthSettings](MACHOS/HealthSettings.md)
- [/System/Library/PreferenceBundles/HearingSettings.bundle/HearingSettings](MACHOS/HearingSettings.md)
- [/System/Library/PreferenceBundles/HomeScreenSettings.bundle/HomeScreenSettings](MACHOS/HomeScreenSettings.md)
- [/System/Library/PreferenceBundles/HomeSettings.bundle/HomeSettings](MACHOS/HomeSettings.md)
- [/System/Library/PreferenceBundles/ICBSettingsBundle.bundle/ICBSettingsBundle](MACHOS/ICBSettingsBundle.md)
- [/System/Library/PreferenceBundles/ICSSettingsBundle.bundle/ICSSettingsBundle](MACHOS/ICSSettingsBundle.md)
- [/System/Library/PreferenceBundles/IDSExternalSettings.bundle/IDSExternalSettings](MACHOS/IDSExternalSettings.md)
- [/System/Library/PreferenceBundles/InternationalSettings.bundle/InternationalSettings](MACHOS/InternationalSettings.md)
- [/System/Library/PreferenceBundles/JournalSettings.bundle/JournalSettings](MACHOS/JournalSettings.md)
- [/System/Library/PreferenceBundles/MadridExternalSettings.bundle/MadridExternalSettings](MACHOS/MadridExternalSettings.md)
- [/System/Library/PreferenceBundles/ManagedConfigurationUI.bundle/ManagedConfigurationUI](MACHOS/ManagedConfigurationUI.md)
- [/System/Library/PreferenceBundles/MapsSettings.bundle/MapsSettings](MACHOS/MapsSettings.md)
- [/System/Library/PreferenceBundles/MeasureSettings.bundle/MeasureSettings](MACHOS/MeasureSettings.md)
- [/System/Library/PreferenceBundles/MessagesNotificationFiltering.bundle/MessagesNotificationFiltering](MACHOS/MessagesNotificationFiltering.md)
- [/System/Library/PreferenceBundles/MobileMailSettings.bundle/MobileMailSettings](MACHOS/MobileMailSettings.md)
- [/System/Library/PreferenceBundles/MobileSafariSettings.bundle/MobileSafariSettings](MACHOS/MobileSafariSettings.md)
- [/System/Library/PreferenceBundles/MobileSlideShowSettings.bundle/MobileSlideShowSettings](MACHOS/MobileSlideShowSettings.md)
- [/System/Library/PreferenceBundles/MobileStoreSettings.bundle/MobileStoreSettings](MACHOS/MobileStoreSettings.md)
- [/System/Library/PreferenceBundles/MultitaskingAndGesturesSettings.bundle/MultitaskingAndGesturesSettings](MACHOS/MultitaskingAndGesturesSettings.md)
- [/System/Library/PreferenceBundles/MusicSettings.bundle/MusicSettings](MACHOS/MusicSettings.md)
- [/System/Library/PreferenceBundles/NameAndPhotoSettingsBundle.bundle/NameAndPhotoSettingsBundle](MACHOS/NameAndPhotoSettingsBundle.md)
- [/System/Library/PreferenceBundles/NewsSettings.bundle/NewsSettings](MACHOS/NewsSettings.md)
- [/System/Library/PreferenceBundles/NotesSettings.bundle/NotesSettings](MACHOS/NotesSettings.md)
- [/System/Library/PreferenceBundles/NotificationsSettings.bundle/NotificationsSettings](MACHOS/NotificationsSettings.md)
- [/System/Library/PreferenceBundles/PassbookSettings.bundle/PassbookSettings](MACHOS/PassbookSettings.md)
- [/System/Library/PreferenceBundles/PhonebookTelephonySettings.bundle/PhonebookTelephonySettings](MACHOS/PhonebookTelephonySettings.md)
- [/System/Library/PreferenceBundles/PhotosCustomNotifications.bundle/PhotosCustomNotifications](MACHOS/PhotosCustomNotifications.md)
- [/System/Library/PreferenceBundles/PictureInPictureSettings.bundle/PictureInPictureSettings](MACHOS/PictureInPictureSettings.md)
- [/System/Library/PreferenceBundles/PodcastsSettingsPlugin.bundle/PodcastsSettingsPlugin](MACHOS/PodcastsSettingsPlugin.md)
- [/System/Library/PreferenceBundles/PrimaryCloudCallingSettingsBundle.bundle/PrimaryCloudCallingSettingsBundle](MACHOS/PrimaryCloudCallingSettingsBundle.md)
- [/System/Library/PreferenceBundles/Privacy/ClipServicesSettings.bundle/ClipServicesSettings](MACHOS/ClipServicesSettings.md)
- [/System/Library/PreferenceBundles/Privacy/HealthPrivacySettings.bundle/HealthPrivacySettings](MACHOS/HealthPrivacySettings.md)
- [/System/Library/PreferenceBundles/Privacy/SensorKitPrivacySettings.bundle/SensorKitPrivacySettings](MACHOS/SensorKitPrivacySettings.md)
- [/System/Library/PreferenceBundles/RemindersSettings.bundle/RemindersSettings](MACHOS/RemindersSettings.md)
- [/System/Library/PreferenceBundles/ReplyWithMessageSettings.bundle/ReplyWithMessageSettings](MACHOS/ReplyWithMessageSettings.md)
- [/System/Library/PreferenceBundles/SIMApplicationsTelephonySettings.bundle/SIMApplicationsTelephonySettings](MACHOS/SIMApplicationsTelephonySettings.md)
- [/System/Library/PreferenceBundles/SIMPasscodeTelephonySettings.bundle/SIMPasscodeTelephonySettings](MACHOS/SIMPasscodeTelephonySettings.md)
- [/System/Library/PreferenceBundles/SIMSettings.bundle/SIMSettings](MACHOS/SIMSettings.md)
- [/System/Library/PreferenceBundles/SMSPreferences.bundle/SMSPreferences](MACHOS/SMSPreferences.md)
- [/System/Library/PreferenceBundles/SOSSettings.bundle/SOSSettings](MACHOS/SOSSettings.md)
- [/System/Library/PreferenceBundles/ScreenTimeSettings.bundle/ScreenTimeSettings](MACHOS/ScreenTimeSettings.md)
- [/System/Library/PreferenceBundles/SecondaryCloudCallingSettingsBundle.bundle/SecondaryCloudCallingSettingsBundle](MACHOS/SecondaryCloudCallingSettingsBundle.md)
- [/System/Library/PreferenceBundles/SecuritySettings.bundle/SecuritySettings](MACHOS/SecuritySettings.md)
- [/System/Library/PreferenceBundles/SettingsCellular.bundle/SettingsCellular](MACHOS/SettingsCellular.md)
- [/System/Library/PreferenceBundles/SharePlaySettings.bundle/SharePlaySettings](MACHOS/SharePlaySettings.md)
- [/System/Library/PreferenceBundles/ShortcutsSettings.bundle/ShortcutsSettings](MACHOS/ShortcutsSettings.md)
- [/System/Library/PreferenceBundles/SilenceCallsSettingBundle.bundle/SilenceCallsSettingBundle](MACHOS/SilenceCallsSettingBundle.md)
- [/System/Library/PreferenceBundles/SiriMessagesSettings.bundle/SiriMessagesSettings](MACHOS/SiriMessagesSettings.md)
- [/System/Library/PreferenceBundles/StocksSettings.bundle/StocksSettings](MACHOS/StocksSettings.md)
- [/System/Library/PreferenceBundles/StoragePlugins/CKStoragePlugin.bundle/CKStoragePlugin](MACHOS/CKStoragePlugin.md)
- [/System/Library/PreferenceBundles/StoragePlugins/HealthStoragePlugin.bundle/HealthStoragePlugin](MACHOS/HealthStoragePlugin.md)
- [/System/Library/PreferenceBundles/StoragePlugins/PhotosStorageManagementSettings.bundle/PhotosStorageManagementSettings](MACHOS/PhotosStorageManagementSettings.md)
- [/System/Library/PreferenceBundles/StoragePlugins/PodcastsUsagePlugin.bundle/PodcastsUsagePlugin](MACHOS/PodcastsUsagePlugin.md)
- [/System/Library/PreferenceBundles/StoragePlugins/UsagePlugin.bundle/UsagePlugin](MACHOS/UsagePlugin.md)
- [/System/Library/PreferenceBundles/StorageSettings.bundle/StorageSettings](MACHOS/StorageSettings.md)
- [/System/Library/PreferenceBundles/StorageSettingsUI.bundle/StorageSettingsUI](MACHOS/StorageSettingsUI.md)
- [/System/Library/PreferenceBundles/TVSettings.bundle/TVSettings](MACHOS/TVSettings.md)
- [/System/Library/PreferenceBundles/UsageSettings.bundle/UsageSettings](MACHOS/UsageSettings.md)
- [/System/Library/PreferenceBundles/VideoSubscriberAccountDeveloperSettings.bundle/VideoSubscriberAccountDeveloperSettings](MACHOS/VideoSubscriberAccountDeveloperSettings.md)
- [/System/Library/PreferenceBundles/VideoSubscriberAccountSettings.bundle/VideoSubscriberAccountSettings](MACHOS/VideoSubscriberAccountSettings.md)
- [/System/Library/PreferenceBundles/VideoSubscriberAccountTVAppDeveloperSettings.bundle/VideoSubscriberAccountTVAppDeveloperSettings](MACHOS/VideoSubscriberAccountTVAppDeveloperSettings.md)
- [/System/Library/PreferenceBundles/VoiceMemosSettings.bundle/VoiceMemosSettings](MACHOS/VoiceMemosSettings.md)
- [/System/Library/PreferenceBundles/WallpaperSettings.bundle/WallpaperSettings](MACHOS/WallpaperSettings.md)
- [/System/Library/PreferenceBundles/WeatherSettings.bundle/WeatherSettings](MACHOS/WeatherSettings.md)
- [/System/Library/PreferenceBundles/WiFiCallingTelephonySettings.bundle/WiFiCallingTelephonySettings](MACHOS/WiFiCallingTelephonySettings.md)
- [/System/Library/PreferenceBundles/WiFiSettings.bundle/WiFiSettings](MACHOS/WiFiSettings.md)
- [/System/Library/PreferenceBundles/iBooksSettings.bundle/iBooksSettings](MACHOS/iBooksSettings.md)
- [/System/Library/PreferenceManifests/ICQSettingsSearch.bundle/ICQSettingsSearch](MACHOS/ICQSettingsSearch.md)
- [/System/Library/PreferenceManifests/MapsSettingsSearchManifest.bundle/MapsSettingsSearchManifest](MACHOS/MapsSettingsSearchManifest.md)
- [/System/Library/PreferenceManifests/ScreenTimeSettingsSearch.bundle/ScreenTimeSettingsSearch](MACHOS/ScreenTimeSettingsSearch.md)
- [/System/Library/PreferenceManifests/iCloudMailSettingsSearch.bundle/iCloudMailSettingsSearch](MACHOS/iCloudMailSettingsSearch.md)
- [/System/Library/PreferenceManifestsInternal/DisplayAndBrightnessPreferencesManifests.bundle/DisplayAndBrightnessPreferencesManifests](MACHOS/DisplayAndBrightnessPreferencesManifests.md)
- [/System/Library/PreferenceManifestsInternal/PreferencesManifests.bundle/PreferencesManifests](MACHOS/PreferencesManifests.md)
- [/System/Library/PreferencesSyncBundles/AppleServiceToolkitPreferencesSync.bundle/AppleServiceToolkitPreferencesSync](MACHOS/AppleServiceToolkitPreferencesSync.md)
- [/System/Library/PreferencesSyncBundles/BrookPreferencesSync.bundle/BrookPreferencesSync](MACHOS/BrookPreferencesSync.md)
- [/System/Library/PreferencesSyncBundles/CarouselSettingsSync.bundle/CarouselSettingsSync](MACHOS/CarouselSettingsSync.md)
- [/System/Library/PreferencesSyncBundles/ContactsPreferencesSyncCompanion.bundle/ContactsPreferencesSyncCompanion](MACHOS/ContactsPreferencesSyncCompanion.md)
- [/System/Library/PreferencesSyncBundles/CoreHapticsPreferencesSync.bundle/CoreHapticsPreferencesSync](MACHOS/CoreHapticsPreferencesSync.md)
- [/System/Library/PreferencesSyncBundles/CoreLocationSync.bundle/CoreLocationSync](MACHOS/CoreLocationSync.md)
- [/System/Library/PreferencesSyncBundles/DoNotDisturbSettingsSync.bundle/DoNotDisturbSettingsSync](MACHOS/DoNotDisturbSettingsSync.md)
- [/System/Library/PreferencesSyncBundles/FindMyDevicePreferencesSync.bundle/FindMyDevicePreferencesSync](MACHOS/FindMyDevicePreferencesSync.md)
- [/System/Library/PreferencesSyncBundles/MentalHealthPreferencesSync.bundle/MentalHealthPreferencesSync](MACHOS/MentalHealthPreferencesSync.md)
- [/System/Library/PreferencesSyncBundles/NanoClockBridgeSettingsPreferencesSyncCompanion.bundle/NanoClockBridgeSettingsPreferencesSyncCompanion](MACHOS/NanoClockBridgeSettingsPreferencesSyncCompanion.md)
- [/System/Library/PreferencesSyncBundles/NanoMapsPreferencesSyncCompanion.bundle/NanoMapsPreferencesSyncCompanion](MACHOS/NanoMapsPreferencesSyncCompanion.md)
- [/System/Library/PreferencesSyncBundles/NanoPhonePreferencesSyncCompanion.bundle/NanoPhonePreferencesSyncCompanion](MACHOS/NanoPhonePreferencesSyncCompanion.md)
- [/System/Library/PreferencesSyncBundles/RelevanceEngineCompanionPrefSync.bundle/RelevanceEngineCompanionPrefSync](MACHOS/RelevanceEngineCompanionPrefSync.md)
- [/System/Library/PreferencesSyncBundles/RemindersNanoPreferencesSync.bundle/RemindersNanoPreferencesSync](MACHOS/RemindersNanoPreferencesSync.md)
- [/System/Library/PreferencesSyncBundles/ScreenTimePreferencesSyncCompanion.bundle/ScreenTimePreferencesSyncCompanion](MACHOS/ScreenTimePreferencesSyncCompanion.md)
- [/System/Library/PreferencesSyncBundles/WGAEltonPreferencesSyncPhone.bundle/WGAEltonPreferencesSyncPhone](MACHOS/WGAEltonPreferencesSyncPhone.md)
- [/System/Library/PrivateFrameworks/ABMHelper.framework/Support/abm-helper](MACHOS/abm-helper.md)
- [/System/Library/PrivateFrameworks/AGXCompilerConnection-S2A8.framework/XPCServices/AGXCompilerService-S2A8.xpc/AGXCompilerService-S2A8](MACHOS/AGXCompilerService-S2A8.md)
- [/System/Library/PrivateFrameworks/AGXCompilerCore-S2A8.framework/PlugIns/AGXCompilerCrashLogs-S2A8.appex/AGXCompilerCrashLogs-S2A8](MACHOS/AGXCompilerCrashLogs-S2A8.md)
- [/System/Library/PrivateFrameworks/ASOctaneSupport.framework/XPCServices/ASOctaneSupportXPCService.xpc/ASOctaneSupportXPCService](MACHOS/ASOctaneSupportXPCService.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/PlugIns/com.apple.AVConference.Diagnostic.appex/com.apple.AVConference.Diagnostic](MACHOS/com.apple.AVConference.Diagnostic.md)
- [/System/Library/PrivateFrameworks/AXAssetLoader.framework/Support/axassetsd](MACHOS/axassetsd.md)
- [/System/Library/PrivateFrameworks/AXMediaUtilities.framework/XPCServices/AXMediaUtilitiesService.xpc/AXMediaUtilitiesService](MACHOS/AXMediaUtilitiesService.md)
- [/System/Library/PrivateFrameworks/AccessibilityAudit.framework/AccessibilityAuditCategories.bundle/AccessibilityAuditCategories](MACHOS/AccessibilityAuditCategories.md)
- [/System/Library/PrivateFrameworks/AccessibilityAudit.framework/Support/axauditd](MACHOS/axauditd.md)
- [/System/Library/PrivateFrameworks/AccessibilityRemoteServices.framework/Support/axremoted](MACHOS/axremoted.md)
- [/System/Library/PrivateFrameworks/AccessibilitySharedSupport.framework/Support/motiontrackingd](MACHOS/motiontrackingd.md)
- [/System/Library/PrivateFrameworks/AccessibilityUtilities.framework/PlugIns/AXSettingsShortcuts.appex/AXSettingsShortcuts](MACHOS/AXSettingsShortcuts.md)
- [/System/Library/PrivateFrameworks/AccessibilityUtilities.framework/PlugIns/com.apple.accessibility.Accessibility.HearingAidsTapToRadar.appex/com.apple.accessibility.Accessibility.HearingAidsTapToRadar](MACHOS/com.apple.accessibility.Accessibility.HearingAidsTapToRadar.md)
- [/System/Library/PrivateFrameworks/AccessoryOOBBTPairing.framework/XPCServices/ACCBluetoothPairingService.xpc/ACCBluetoothPairingService](MACHOS/ACCBluetoothPairingService.md)
- [/System/Library/PrivateFrameworks/AccountNotification.framework/and](MACHOS/and.md)
- [/System/Library/PrivateFrameworks/AccountsDaemon.framework/XPCServices/com.apple.accounts.dom.xpc/com.apple.accounts.dom](MACHOS/com.apple.accounts.dom.md)
- [/System/Library/PrivateFrameworks/ActionKit.framework/PlugIns/BundledIntentHandler.appex/BundledIntentHandler](MACHOS/BundledIntentHandler.md)
- [/System/Library/PrivateFrameworks/ActionPredictionHeuristics.framework/XPCServices/HeuristicInterpreter.xpc/HeuristicInterpreter](MACHOS/HeuristicInterpreter.md)
- [/System/Library/PrivateFrameworks/ActivityAwardsServices.framework/activityawardsd](MACHOS/activityawardsd.md)
- [/System/Library/PrivateFrameworks/ActivitySharingServices.framework/activitysharingd](MACHOS/activitysharingd.md)
- [/System/Library/PrivateFrameworks/AdminLite.framework/Resources/AdminLiteTool](MACHOS/AdminLiteTool.md)
- [/System/Library/PrivateFrameworks/AfibBurden.framework/PlugIns/AfibBurdenDiagnosticExtension.appex/AfibBurdenDiagnosticExtension](MACHOS/AfibBurdenDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/AggregateDictionary.framework/Support/addaily](MACHOS/addaily.md)
- [/System/Library/PrivateFrameworks/AggregateDictionary.framework/Support/aggregated](MACHOS/aggregated.md)
- [/System/Library/PrivateFrameworks/AmbientUI.framework/PlugIns/InfographPoster.appex/InfographPoster](MACHOS/InfographPoster.md)
- [/System/Library/PrivateFrameworks/AnnounceSiriExtensions.framework/PlugIns/AnnounceIntentExtension.appex/AnnounceIntentExtension](MACHOS/AnnounceIntentExtension.md)
- [/System/Library/PrivateFrameworks/AppConduit.framework/Support/appconduitd](MACHOS/appconduitd.md)
- [/System/Library/PrivateFrameworks/AppInstallationMetrics.framework/Support/appinstallationmetricsd](MACHOS/appinstallationmetricsd.md)
- [/System/Library/PrivateFrameworks/AppPredictionFoundation.framework/XPCServices/AppPredictionIntentsHelperService.xpc/AppPredictionIntentsHelperService](MACHOS/AppPredictionIntentsHelperService.md)
- [/System/Library/PrivateFrameworks/AppSSO.framework/Support/AppSSODaemon](MACHOS/AppSSODaemon.md)
- [/System/Library/PrivateFrameworks/AppSSOKerberos.framework/PlugIns/KerberosExtension.appex/KerberosExtension](MACHOS/KerberosExtension.md)
- [/System/Library/PrivateFrameworks/AppStoreComponents.framework/Support/appstorecomponentsd](MACHOS/appstorecomponentsd.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/PlugIns/ASDAskPermissionExtension.appex/ASDAskPermissionExtension](MACHOS/ASDAskPermissionExtension.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/PlugIns/ASDFollowUpExtension.appex/ASDFollowUpExtension](MACHOS/ASDFollowUpExtension.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/PlugIns/ASDUserNotificationExtension.appex/ASDUserNotificationExtension](MACHOS/ASDUserNotificationExtension.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/PlugIns/AppStoreEventServiceExtension.appex/AppStoreEventServiceExtension](MACHOS/AppStoreEventServiceExtension.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored](MACHOS/appstored.md)
- [/System/Library/PrivateFrameworks/AppStoreOverlays.framework/PlugIns/AppStoreOverlaysService.appex/AppStoreOverlaysService](MACHOS/AppStoreOverlaysService.md)
- [/System/Library/PrivateFrameworks/AppleAccountUI.framework/PlugIns/AAUIFollowUpExtension.appex/AAUIFollowUpExtension](MACHOS/AAUIFollowUpExtension.md)
- [/System/Library/PrivateFrameworks/AppleCredentialManager.framework/AppleCredentialManagerDaemon](MACHOS/AppleCredentialManagerDaemon.md)
- [/System/Library/PrivateFrameworks/AppleMediaDiscovery.framework/PlugIns/AMDEngagementExtension.appex/AMDEngagementExtension](MACHOS/AMDEngagementExtension.md)
- [/System/Library/PrivateFrameworks/AppleMediaDiscovery.framework/PlugIns/ASLAppEmbedding.appex/ASLAppEmbedding](MACHOS/ASLAppEmbedding.md)
- [/System/Library/PrivateFrameworks/AppleMediaDiscovery.framework/PlugIns/ASLArcadeRanking.appex/ASLArcadeRanking](MACHOS/ASLArcadeRanking.md)
- [/System/Library/PrivateFrameworks/AppleMediaDiscovery.framework/PlugIns/ASLArcadeRetention.appex/ASLArcadeRetention](MACHOS/ASLArcadeRetention.md)
- [/System/Library/PrivateFrameworks/AppleMediaDiscovery.framework/PlugIns/ASLExperimental.appex/ASLExperimental](MACHOS/ASLExperimental.md)
- [/System/Library/PrivateFrameworks/AppleMediaDiscovery.framework/PlugIns/AppStoreEvalLighthousePlugin.appex/AppStoreEvalLighthousePlugin](MACHOS/AppStoreEvalLighthousePlugin.md)
- [/System/Library/PrivateFrameworks/AppleMediaDiscovery.framework/PlugIns/CSLAppStore.appex/CSLAppStore](MACHOS/CSLAppStore.md)
- [/System/Library/PrivateFrameworks/AppleMediaDiscovery.framework/PlugIns/CSLAppStore2.appex/CSLAppStore2](MACHOS/CSLAppStore2.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/PlugIns/AMSFollowUpExtension.appex/AMSFollowUpExtension](MACHOS/AMSFollowUpExtension.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/amsaccountsd](MACHOS/amsaccountsd.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/Extensions/UtilityExtension.appex/UtilityExtension](MACHOS/UtilityExtension.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/PlugIns/AMSEngagementNotificationsExtension.appex/AMSEngagementNotificationsExtension](MACHOS/AMSEngagementNotificationsExtension.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/PlugIns/AMSEngagementViewExtension.appex/AMSEngagementViewExtension](MACHOS/AMSEngagementViewExtension.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/PlugIns/AMSProductPageExtension.appex/AMSProductPageExtension](MACHOS/AMSProductPageExtension.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/amsengagementd](MACHOS/amsengagementd.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUIDynamic.framework/XPCServices/AppleMediaServicesUIDynamicService.xpc/AppleMediaServicesUIDynamicService](MACHOS/AppleMediaServicesUIDynamicService.md)
- [/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/XPCServices/ANECompilerService.xpc/ANECompilerService](MACHOS/ANECompilerService.md)
- [/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/XPCServices/ANEStorageMaintainer.xpc/ANEStorageMaintainer](MACHOS/ANEStorageMaintainer.md)
- [/System/Library/PrivateFrameworks/ApplePushService.framework/apsd](MACHOS/apsd.md)
- [/System/Library/PrivateFrameworks/AskPermission.framework/Support/askpermissiond](MACHOS/askpermissiond.md)
- [/System/Library/PrivateFrameworks/AssetCacheServices.framework/XPCServices/AssetCacheLocatorService.xpc/AssetCacheLocatorService](MACHOS/AssetCacheLocatorService.md)
- [/System/Library/PrivateFrameworks/AssetViewer.framework/PlugIns/ASVAssetThumbnail.appex/ASVAssetThumbnail](MACHOS/ASVAssetThumbnail.md)
- [/System/Library/PrivateFrameworks/AssetViewer.framework/PlugIns/ASVAssetViewer.appex/ASVAssetViewer](MACHOS/ASVAssetViewer.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/PlugIns/SiriDE.appex/SiriDE](MACHOS/SiriDE.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/XPCServices/DeepSyncVerification.xpc/DeepSyncVerification](MACHOS/DeepSyncVerification.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/XPCServices/OpportuneSpeakingModelService.xpc/OpportuneSpeakingModelService](MACHOS/OpportuneSpeakingModelService.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/XPCServices/com.apple.siri.acousticsignature.xpc/com.apple.siri.acousticsignature](MACHOS/com.apple.siri.acousticsignature.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/XPCServices/com.apple.siri.analyzer.xpc/com.apple.siri.analyzer](MACHOS/com.apple.siri.analyzer.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/assistant_service](MACHOS/assistant_service.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd](MACHOS/assistantd.md)
- [/System/Library/PrivateFrameworks/AuthKit.framework/PlugIns/AKDiagnosticExtension.appex/AKDiagnosticExtension](MACHOS/AKDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/AuthKit.framework/akd](MACHOS/akd.md)
- [/System/Library/PrivateFrameworks/AuthKitUI.framework/PlugIns/AKAppSSOExtension.appex/AKAppSSOExtension](MACHOS/AKAppSSOExtension.md)
- [/System/Library/PrivateFrameworks/AuthKitUI.framework/PlugIns/AKFollowUpExtension.appex/AKFollowUpExtension](MACHOS/AKFollowUpExtension.md)
- [/System/Library/PrivateFrameworks/AuthKitUI.framework/PlugIns/AKLocationSignInAlert.appex/AKLocationSignInAlert](MACHOS/AKLocationSignInAlert.md)
- [/System/Library/PrivateFrameworks/AuthKitUI.framework/PlugIns/AKSecondFactorAlert.appex/AKSecondFactorAlert](MACHOS/AKSecondFactorAlert.md)
- [/System/Library/PrivateFrameworks/AuthKitUI.framework/PlugIns/AKSecondFactorEntryAlert.appex/AKSecondFactorEntryAlert](MACHOS/AKSecondFactorEntryAlert.md)
- [/System/Library/PrivateFrameworks/AutomationMode.framework/AutomationModeUI.app/AutomationModeUI](MACHOS/AutomationModeUI.md)
- [/System/Library/PrivateFrameworks/AutomationMode.framework/automationmode-writer](MACHOS/automationmode-writer.md)
- [/System/Library/PrivateFrameworks/AvatarPersistence.framework/Support/avatarsd](MACHOS/avatarsd.md)
- [/System/Library/PrivateFrameworks/AvatarUI.framework/PlugIns/AvatarPosterExtension.appex/AvatarPosterExtension](MACHOS/AvatarPosterExtension.md)
- [/System/Library/PrivateFrameworks/AvatarUI.framework/XPCServices/MemojiImageRenderService.xpc/MemojiImageRenderService](MACHOS/MemojiImageRenderService.md)
- [/System/Library/PrivateFrameworks/BackBoardServices.framework/XPCServices/DisplayArchiveService.xpc/DisplayArchiveService](MACHOS/DisplayArchiveService.md)
- [/System/Library/PrivateFrameworks/BacklightServices.framework/PlugIns/BacklightDiagnostics.appex/BacklightDiagnostics](MACHOS/BacklightDiagnostics.md)
- [/System/Library/PrivateFrameworks/BarcodeSupport.framework/PlugIns/com.apple.BarcodeSupport.BarcodeNotificationExtension.appex/com.apple.BarcodeSupport.BarcodeNotificationExtension](MACHOS/com.apple.BarcodeSupport.BarcodeNotificationExtension.md)
- [/System/Library/PrivateFrameworks/BarcodeSupport.framework/PlugIns/com.apple.BarcodeSupport.BarcodeNotificationExtension2.appex/com.apple.BarcodeSupport.BarcodeNotificationExtension2](MACHOS/com.apple.BarcodeSupport.BarcodeNotificationExtension2.md)
- [/System/Library/PrivateFrameworks/BarcodeSupport.framework/XPCServices/com.apple.BarcodeSupport.Helper.xpc/com.apple.BarcodeSupport.Helper](MACHOS/com.apple.BarcodeSupport.Helper.md)
- [/System/Library/PrivateFrameworks/BarcodeSupport.framework/XPCServices/com.apple.BarcodeSupport.ParsingService.xpc/com.apple.BarcodeSupport.ParsingService](MACHOS/com.apple.BarcodeSupport.ParsingService.md)
- [/System/Library/PrivateFrameworks/BarcodeSupport.framework/com.apple.BarcodeSupport.BarcodeNotificationService](MACHOS/com.apple.BarcodeSupport.BarcodeNotificationService.md)
- [/System/Library/PrivateFrameworks/BehaviorMiner.framework/Support/mlmodelingd](MACHOS/mlmodelingd.md)
- [/System/Library/PrivateFrameworks/BiomeStorage.framework/XPCServices/BiomeWriteService.xpc/BiomeWriteService](MACHOS/BiomeWriteService.md)
- [/System/Library/PrivateFrameworks/BiomeStreams.framework/PlugIns/BiomeLighthousePlugin.appex/BiomeLighthousePlugin](MACHOS/BiomeLighthousePlugin.md)
- [/System/Library/PrivateFrameworks/BiomeStreams.framework/Support/biomed](MACHOS/biomed.md)
- [/System/Library/PrivateFrameworks/BiometricKit.framework/PlugIns/BioLogDiagnostic.appex/BioLogDiagnostic](MACHOS/BioLogDiagnostic.md)
- [/System/Library/PrivateFrameworks/BookDataStore.framework/Support/bookdatastored](MACHOS/bookdatastored.md)
- [/System/Library/PrivateFrameworks/BookLibrary.framework/PlugIns/BooksDiagnosticExtension.appex/BooksDiagnosticExtension](MACHOS/BooksDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/BookLibraryCore.framework/PlugIns/BooksAskPermissionExtension.appex/BooksAskPermissionExtension](MACHOS/BooksAskPermissionExtension.md)
- [/System/Library/PrivateFrameworks/BookLibraryCore.framework/Support/bookassetd](MACHOS/bookassetd.md)
- [/System/Library/PrivateFrameworks/BrailleTranslation.framework/XPCServices/BrailleTranslationService.xpc/BrailleTranslationService](MACHOS/BrailleTranslationService.md)
- [/System/Library/PrivateFrameworks/BusinessChatService.framework/businessservicesd](MACHOS/businessservicesd.md)
- [/System/Library/PrivateFrameworks/CDDataAccess.framework/Frameworks/DACalDAV.framework/DADaemonCalDAV.bundle/DADaemonCalDAV](MACHOS/DADaemonCalDAV.md)
- [/System/Library/PrivateFrameworks/CMCapture.framework/PlugIns/CMCaptureDiagnosticExtension.appex/CMCaptureDiagnosticExtension](MACHOS/CMCaptureDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/CSExattrCrypto.framework/XPCServices/CSExattrCryptoService.xpc/CSExattrCryptoService](MACHOS/CSExattrCryptoService.md)
- [/System/Library/PrivateFrameworks/CacheDelete.framework/deleted](MACHOS/deleted.md)
- [/System/Library/PrivateFrameworks/CacheDelete.framework/deleted_helper](MACHOS/deleted_helper.md)
- [/System/Library/PrivateFrameworks/CalendarDaemon.framework/Support/calaccessd](MACHOS/calaccessd.md)
- [/System/Library/PrivateFrameworks/CalendarNotification.framework/PlugIns/CalendarNotificationContentExtension.appex/CalendarNotificationContentExtension](MACHOS/CalendarNotificationContentExtension.md)
- [/System/Library/PrivateFrameworks/CalendarWidget.framework/PlugIns/IntentsExtension.appex/IntentsExtension](MACHOS/IntentsExtension.md)
- [/System/Library/PrivateFrameworks/CallHistory.framework/Support/CallHistorySyncHelper](MACHOS/CallHistorySyncHelper.md)
- [/System/Library/PrivateFrameworks/CameraUI.framework/Support/nebulad](MACHOS/nebulad.md)
- [/System/Library/PrivateFrameworks/CarKit.framework/PlugIns/CarPlayDiagnostics.appex/CarPlayDiagnostics](MACHOS/CarPlayDiagnostics.md)
- [/System/Library/PrivateFrameworks/Categories.framework/XPCServices/CategoriesService.xpc/CategoriesService](MACHOS/CategoriesService.md)
- [/System/Library/PrivateFrameworks/CertUI.framework/certui_relay](MACHOS/certui_relay.md)
- [/System/Library/PrivateFrameworks/ChatKit.framework/companionmessagesd](MACHOS/companionmessagesd.md)
- [/System/Library/PrivateFrameworks/ChronoCore.framework/Support/chronod](MACHOS/chronod.md)
- [/System/Library/PrivateFrameworks/CipherML.framework/XPCServices/CipherMLService.xpc/CipherMLService](MACHOS/CipherMLService.md)
- [/System/Library/PrivateFrameworks/ClassKitUI.framework/PlugIns/PrivacyDisclosure.appex/PrivacyDisclosure](MACHOS/PrivacyDisclosure.md)
- [/System/Library/PrivateFrameworks/ClassroomKit.framework/Extensions/EasyMAIDSignInPicker.appex/EasyMAIDSignInPicker](MACHOS/EasyMAIDSignInPicker.md)
- [/System/Library/PrivateFrameworks/ClassroomKit.framework/XPCServices/BooksService.xpc/BooksService](MACHOS/BooksService.md)
- [/System/Library/PrivateFrameworks/ClassroomKit.framework/XPCServices/ScreenshotService.xpc/ScreenshotService](MACHOS/ScreenshotService.md)
- [/System/Library/PrivateFrameworks/ClipServices.framework/clipserviced](MACHOS/clipserviced.md)
- [/System/Library/PrivateFrameworks/ClockPoster.framework/PlugIns/ClockPosterExtension.appex/ClockPosterExtension](MACHOS/ClockPosterExtension.md)
- [/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.MobileDocumentsFileProvider.appex/com.apple.CloudDocs.MobileDocumentsFileProvider](MACHOS/com.apple.CloudDocs.MobileDocumentsFileProvider.md)
- [/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.MobileDocumentsFileProviderManaged.appex/com.apple.CloudDocs.MobileDocumentsFileProviderManaged](MACHOS/com.apple.CloudDocs.MobileDocumentsFileProviderManaged.md)
- [/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.MobileDocumentsFileProviderUI.appex/com.apple.CloudDocs.MobileDocumentsFileProviderUI](MACHOS/com.apple.CloudDocs.MobileDocumentsFileProviderUI.md)
- [/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.iCloudDriveFileProvider.appex/com.apple.CloudDocs.iCloudDriveFileProvider](MACHOS/com.apple.CloudDocs.iCloudDriveFileProvider.md)
- [/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.iCloudDriveFileProviderManaged.appex/com.apple.CloudDocs.iCloudDriveFileProviderManaged](MACHOS/com.apple.CloudDocs.iCloudDriveFileProviderManaged.md)
- [/System/Library/PrivateFrameworks/CloudDocsDaemon.framework/PlugIns/CloudDocsDiagnostic.appex/CloudDocsDiagnostic](MACHOS/CloudDocsDiagnostic.md)
- [/System/Library/PrivateFrameworks/CloudDocsDaemon.framework/bird](MACHOS/bird.md)
- [/System/Library/PrivateFrameworks/CloudDocsUI.framework/PlugIns/com.apple.CloudDocsUI.CloudSharing.appex/com.apple.CloudDocsUI.CloudSharing](MACHOS/com.apple.CloudDocsUI.CloudSharing.md)
- [/System/Library/PrivateFrameworks/CloudDocsUI.framework/PlugIns/com.apple.CloudDocsUI.DocumentPicker.appex/com.apple.CloudDocsUI.DocumentPicker](MACHOS/com.apple.CloudDocsUI.DocumentPicker.md)
- [/System/Library/PrivateFrameworks/CloudKitDaemon.framework/Support/ckdiscretionaryd](MACHOS/ckdiscretionaryd.md)
- [/System/Library/PrivateFrameworks/CloudKitDaemon.framework/Support/cloudd](MACHOS/cloudd.md)
- [/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/Support/cloudphotod](MACHOS/cloudphotod.md)
- [/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/XPCServices/com.apple.Photos.CPLDiagnose.xpc/com.apple.Photos.CPLDiagnose](MACHOS/com.apple.Photos.CPLDiagnose.md)
- [/System/Library/PrivateFrameworks/CloudServices.framework/Helpers/com.apple.sbd](MACHOS/com.apple.sbd.md)
- [/System/Library/PrivateFrameworks/CloudSettings.framework/Versions/A/XPCServices/com.apple.cloudsettings.gamecontroller.xpc/com.apple.cloudsettings.gamecontroller](MACHOS/com.apple.cloudsettings.gamecontroller.md)
- [/System/Library/PrivateFrameworks/CloudSettings.framework/XPCServices/com.apple.cloudsettings.international.xpc/com.apple.cloudsettings.international](MACHOS/com.apple.cloudsettings.international.md)
- [/System/Library/PrivateFrameworks/CloudSettings.framework/XPCServices/com.apple.cloudsettings.keyboard.xpc/com.apple.cloudsettings.keyboard](MACHOS/com.apple.cloudsettings.keyboard.md)
- [/System/Library/PrivateFrameworks/CloudSharing.framework/XPCServices/SPIHelper-iOS.xpc/SPIHelper-iOS](MACHOS/SPIHelper-iOS.md)
- [/System/Library/PrivateFrameworks/CloudSharingUI.framework/PlugIns/com.apple.CloudSharingUI.AddParticipants.appex/com.apple.CloudSharingUI.AddParticipants](MACHOS/com.apple.CloudSharingUI.AddParticipants.md)
- [/System/Library/PrivateFrameworks/CloudSharingUI.framework/PlugIns/com.apple.CloudSharingUI.CloudSharing.appex/com.apple.CloudSharingUI.CloudSharing](MACHOS/com.apple.CloudSharingUI.CloudSharing.md)
- [/System/Library/PrivateFrameworks/CloudTelemetry.framework/XPCServices/CloudTelemetryService.xpc/CloudTelemetryService](MACHOS/CloudTelemetryService.md)
- [/System/Library/PrivateFrameworks/CommunicationsFilter.framework/CMFSyncAgent](MACHOS/CMFSyncAgent.md)
- [/System/Library/PrivateFrameworks/CompanionCamera.framework/Support/companioncamerad](MACHOS/companioncamerad.md)
- [/System/Library/PrivateFrameworks/CompassUI.framework/XPCServices/CompassCalibration.xpc/CompassCalibration](MACHOS/CompassCalibration.md)
- [/System/Library/PrivateFrameworks/ContactsDonation.framework/Versions/A/Support/contactsdonationagent](MACHOS/contactsdonationagent.md)
- [/System/Library/PrivateFrameworks/ContactsUICore.framework/XPCServices/ContactsBackgroundColorService.xpc/ContactsBackgroundColorService](MACHOS/ContactsBackgroundColorService.md)
- [/System/Library/PrivateFrameworks/ContextKit.framework/XPCServices/ContextService.xpc/ContextService](MACHOS/ContextService.md)
- [/System/Library/PrivateFrameworks/ContinuousDialogManagerService.framework/assistant_cdmd](MACHOS/assistant_cdmd.md)
- [/System/Library/PrivateFrameworks/CoreAccessories.framework/Support/accessoryd](MACHOS/accessoryd.md)
- [/System/Library/PrivateFrameworks/CoreAccessories.framework/XPCServices/ACCAppLinksIconService.xpc/ACCAppLinksIconService](MACHOS/ACCAppLinksIconService.md)
- [/System/Library/PrivateFrameworks/CoreAccessories.framework/XPCServices/ACCCarPlayService.xpc/ACCCarPlayService](MACHOS/ACCCarPlayService.md)
- [/System/Library/PrivateFrameworks/CoreAccessories.framework/XPCServices/ACCHWComponentAuthService.xpc/ACCHWComponentAuthService](MACHOS/ACCHWComponentAuthService.md)
- [/System/Library/PrivateFrameworks/CoreAccessoriesFeatures.framework/XPCServices/ACCFeatureAudioProductService.xpc/ACCFeatureAudioProductService](MACHOS/ACCFeatureAudioProductService.md)
- [/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsd](MACHOS/analyticsd.md)
- [/System/Library/PrivateFrameworks/CoreBluetoothUI.framework/PlugIns/BTDevicePickerUI.appex/BTDevicePickerUI](MACHOS/BTDevicePickerUI.md)
- [/System/Library/PrivateFrameworks/CoreCDP.framework/cdpd](MACHOS/cdpd.md)
- [/System/Library/PrivateFrameworks/CoreCDPUI.framework/PlugIns/CDPFollowUpExtension.appex/CDPFollowUpExtension](MACHOS/CDPFollowUpExtension.md)
- [/System/Library/PrivateFrameworks/CoreCDPUI.framework/PlugIns/CoreCDPUIService.appex/CoreCDPUIService](MACHOS/CoreCDPUIService.md)
- [/System/Library/PrivateFrameworks/CoreDuetContext.framework/Resources/contextstored](MACHOS/contextstored.md)
- [/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/XPCServices/com.apple.siri.embeddedspeech.xpc/com.apple.siri.embeddedspeech](MACHOS/com.apple.siri.embeddedspeech.md)
- [/System/Library/PrivateFrameworks/CoreFollowUp.framework/followupd](MACHOS/followupd.md)
- [/System/Library/PrivateFrameworks/CoreFollowUpUI.framework/PlugIns/FollowUpSampleExtension.appex/FollowUpSampleExtension](MACHOS/FollowUpSampleExtension.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/PlugIns/SearchPoirotExtension.appex/SearchPoirotExtension](MACHOS/SearchPoirotExtension.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/parsec-fbf](MACHOS/parsec-fbf.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/parsecd](MACHOS/parsecd.md)
- [/System/Library/PrivateFrameworks/CorePrescriptionLite.framework/XPCServices/AccessoryDataFetch.xpc/AccessoryDataFetch](MACHOS/AccessoryDataFetch.md)
- [/System/Library/PrivateFrameworks/CoreRecents.framework/recentsd](MACHOS/recentsd.md)
- [/System/Library/PrivateFrameworks/CoreRoutine.framework/PlugIns/RTDiagnosticExtension.appex/RTDiagnosticExtension](MACHOS/RTDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/CoreRoutine.framework/XPCServices/CoreRoutineHelperService.xpc/CoreRoutineHelperService](MACHOS/CoreRoutineHelperService.md)
- [/System/Library/PrivateFrameworks/CoreSVG.framework/PlugIns/com.apple.CoreSVG.thumbnail.appex/com.apple.CoreSVG.thumbnail](MACHOS/com.apple.CoreSVG.thumbnail.md)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/MockAVVCPlugin.bundle/MockAVVCPlugin](MACHOS/MockAVVCPlugin.md)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/PlugIns/CoreSpeechDiagnosticExtension.appex/CoreSpeechDiagnosticExtension](MACHOS/CoreSpeechDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/XPCServices/CoreSpeechXPC.xpc/CoreSpeechXPC](MACHOS/CoreSpeechXPC.md)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/XPCServices/FidesPHSXPC.xpc/FidesPHSXPC](MACHOS/FidesPHSXPC.md)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd](MACHOS/corespeechd.md)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/speechmodeltrainingd](MACHOS/speechmodeltrainingd.md)
- [/System/Library/PrivateFrameworks/CoreSuggestions.framework/Tools/suggest_tool](MACHOS/suggest_tool.md)
- [/System/Library/PrivateFrameworks/CoreSuggestions.framework/reversetemplated](MACHOS/reversetemplated.md)
- [/System/Library/PrivateFrameworks/CoreSuggestions.framework/suggestd](MACHOS/suggestd.md)
- [/System/Library/PrivateFrameworks/CoreSymbolication.framework/coresymbolicationd](MACHOS/coresymbolicationd.md)
- [/System/Library/PrivateFrameworks/CoreThreadCommissionerService.framework/CoreThreadCommissionerServiced](MACHOS/CoreThreadCommissionerServiced.md)
- [/System/Library/PrivateFrameworks/CoreThreadRadio.framework/threadradiod](MACHOS/threadradiod.md)
- [/System/Library/PrivateFrameworks/CoreTime.framework/TimeSources/AccessoryTimeSync.bundle/AccessoryTimeSync](MACHOS/AccessoryTimeSync.md)
- [/System/Library/PrivateFrameworks/CoreTime.framework/TimeSources/CellularSource.bundle/CellularSource](MACHOS/CellularSource.md)
- [/System/Library/PrivateFrameworks/CoreTime.framework/TimeSources/LinkSource.bundle/LinkSource](MACHOS/LinkSource.md)
- [/System/Library/PrivateFrameworks/CoreUI.framework/DesignLibrary-iOS.bundle/DesignLibrary-iOS](MACHOS/DesignLibrary-iOS.md)
- [/System/Library/PrivateFrameworks/DASDaemon.framework/PlugIns/DuetDiagnosticExtension.appex/DuetDiagnosticExtension](MACHOS/DuetDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/DASDelegate.framework/XPCServices/DASDelegateService.xpc/DASDelegateService](MACHOS/DASDelegateService.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/DTServiceHub](MACHOS/DTServiceHub.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/LeakAgent](MACHOS/LeakAgent.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/PlugIns/DTODRAssetStatus.bundle/DTODRAssetStatus](MACHOS/DTODRAssetStatus.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/PlugIns/IDEDebugGaugeDataProviders.bundle/IDEDebugGaugeDataProviders](MACHOS/IDEDebugGaugeDataProviders.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/RemoteInjectionAgent](MACHOS/RemoteInjectionAgent.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/XPCServices/com.apple.dt.DTConditionInducerSupportService.xpc/com.apple.dt.DTConditionInducerSupportService](MACHOS/com.apple.dt.DTConditionInducerSupportService.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/XPCServices/com.apple.dt.DTMLModelRunnerService.xpc/com.apple.dt.DTMLModelRunnerService](MACHOS/com.apple.dt.DTMLModelRunnerService.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/XPCServices/com.apple.dt.DTScreenshotService.xpc/com.apple.dt.DTScreenshotService](MACHOS/com.apple.dt.DTScreenshotService.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/XPCServices/com.apple.dt.instruments.dtsecurity.xpc/com.apple.dt.instruments.dtsecurity](MACHOS/com.apple.dt.instruments.dtsecurity.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/libRemoteInjectionPayload.dylib](MACHOS/libRemoteInjectionPayload.dylib.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/liboainject.dylib](MACHOS/liboainject.dylib.md)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DACalDAV.framework/DADaemonCalDAV.bundle/DADaemonCalDAV](MACHOS/DADaemonCalDAV.md)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DACardDAV.framework/DADaemonCardDAV.bundle/DADaemonCardDAV](MACHOS/DADaemonCardDAV.md)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DAIMAPNotes.framework/DADaemonIMAPNotes.bundle/DADaemonIMAPNotes](MACHOS/DADaemonIMAPNotes.md)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DALDAP.framework/DADaemonLDAP.bundle/DADaemonLDAP](MACHOS/DADaemonLDAP.md)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DASubCal.framework/DADaemonSubCal.bundle/DADaemonSubCal](MACHOS/DADaemonSubCal.md)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Support/dataaccessd](MACHOS/dataaccessd.md)
- [/System/Library/PrivateFrameworks/DataDetectorsCore.framework/XPCServices/DataDetectorsRemoteScanner.xpc/DataDetectorsRemoteScanner](MACHOS/DataDetectorsRemoteScanner.md)
- [/System/Library/PrivateFrameworks/DataDetectorsUI.framework/PlugIns/com.apple.DataDetectorsUI.ActionsExtension.appex/com.apple.DataDetectorsUI.ActionsExtension](MACHOS/com.apple.DataDetectorsUI.ActionsExtension.md)
- [/System/Library/PrivateFrameworks/DataDetectorsUI.framework/XPCServices/com.apple.datadetectors.AddToRecentsService.xpc/com.apple.datadetectors.AddToRecentsService](MACHOS/com.apple.datadetectors.AddToRecentsService.md)
- [/System/Library/PrivateFrameworks/DataMigration.framework/XPCServices/com.apple.datamigrator.xpc/com.apple.datamigrator](MACHOS/com.apple.datamigrator.md)
- [/System/Library/PrivateFrameworks/DataMigration.framework/XPCServices/com.apple.migrationpluginwrapper.xpc/com.apple.migrationpluginwrapper](MACHOS/com.apple.migrationpluginwrapper.md)
- [/System/Library/PrivateFrameworks/DataMigration.framework/XPCServices/datamigratorhelper.xpc/datamigratorhelper](MACHOS/datamigratorhelper.md)
- [/System/Library/PrivateFrameworks/DebugHierarchyFoundation.framework/DebugHierarchyFoundation](MACHOS/DebugHierarchyFoundation.md)
- [/System/Library/PrivateFrameworks/DebugHierarchyKit.framework/DebugHierarchyKit](MACHOS/DebugHierarchyKit.md)
- [/System/Library/PrivateFrameworks/DeepThought.framework/PlugIns/DeepThoughtPlugin.appex/DeepThoughtPlugin](MACHOS/DeepThoughtPlugin.md)
- [/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/DesktopServicesHelper](MACHOS/DesktopServicesHelper.md)
- [/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/XPCServices/ArchiveService.xpc/ArchiveService](MACHOS/ArchiveService.md)
- [/System/Library/PrivateFrameworks/DeviceCheckInternal.framework/devicecheckd](MACHOS/devicecheckd.md)
- [/System/Library/PrivateFrameworks/DeviceToDeviceManager.framework/PlugIns/BTD2DPlugin.bundle/BTD2DPlugin](MACHOS/BTD2DPlugin.md)
- [/System/Library/PrivateFrameworks/DeviceToDeviceManager.framework/PlugIns/WiFiAwareD2DPlugin.bundle/WiFiAwareD2DPlugin](MACHOS/WiFiAwareD2DPlugin.md)
- [/System/Library/PrivateFrameworks/DeviceToDeviceManager.framework/PlugIns/WiFiD2DPlugin.bundle/WiFiD2DPlugin](MACHOS/WiFiD2DPlugin.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/AudioDiagnosticExtension.appex/AudioDiagnosticExtension](MACHOS/AudioDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/BluetoothHeadset.appex/BluetoothHeadset](MACHOS/BluetoothHeadset.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/HomeEnergyDiagnosticExtension.appex/HomeEnergyDiagnosticExtension](MACHOS/HomeEnergyDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/IntelligentRoutingDiagnostic.appex/IntelligentRoutingDiagnostic](MACHOS/IntelligentRoutingDiagnostic.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/LocationDiagnosticExtension.appex/LocationDiagnosticExtension](MACHOS/LocationDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/NearbydDiagnosticExtension.appex/NearbydDiagnosticExtension](MACHOS/NearbydDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/PICSDiagnosticExtension.appex/PICSDiagnosticExtension](MACHOS/PICSDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/PedestrianFenceDiagnostic.appex/PedestrianFenceDiagnostic](MACHOS/PedestrianFenceDiagnostic.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/PrecisionFindingDiagnostic.appex/PrecisionFindingDiagnostic](MACHOS/PrecisionFindingDiagnostic.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/ShortcutsDiagnosticExtension.appex/ShortcutsDiagnosticExtension](MACHOS/ShortcutsDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/TypologyDiagnosticExtension.appex/TypologyDiagnosticExtension](MACHOS/TypologyDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.B389.appex/com.apple.DiagnosticExtensions.B389](MACHOS/com.apple.DiagnosticExtensions.B389.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.BackgroundAppRefresh.appex/com.apple.DiagnosticExtensions.BackgroundAppRefresh](MACHOS/com.apple.DiagnosticExtensions.BackgroundAppRefresh.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.BluetoothABCDE.appex/com.apple.DiagnosticExtensions.BluetoothABCDE](MACHOS/com.apple.DiagnosticExtensions.BluetoothABCDE.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Cellular.appex/com.apple.DiagnosticExtensions.Cellular](MACHOS/com.apple.DiagnosticExtensions.Cellular.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Contacts.appex/com.apple.DiagnosticExtensions.Contacts](MACHOS/com.apple.DiagnosticExtensions.Contacts.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.CrashLogs.appex/com.apple.DiagnosticExtensions.CrashLogs](MACHOS/com.apple.DiagnosticExtensions.CrashLogs.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.DataAccess.appex/com.apple.DiagnosticExtensions.DataAccess](MACHOS/com.apple.DiagnosticExtensions.DataAccess.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.FaceTime.appex/com.apple.DiagnosticExtensions.FaceTime](MACHOS/com.apple.DiagnosticExtensions.FaceTime.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.HangTracer.appex/com.apple.DiagnosticExtensions.HangTracer](MACHOS/com.apple.DiagnosticExtensions.HangTracer.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Keyboard.appex/com.apple.DiagnosticExtensions.Keyboard](MACHOS/com.apple.DiagnosticExtensions.Keyboard.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.LowMemory.appex/com.apple.DiagnosticExtensions.LowMemory](MACHOS/com.apple.DiagnosticExtensions.LowMemory.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Messages.appex/com.apple.DiagnosticExtensions.Messages](MACHOS/com.apple.DiagnosticExtensions.Messages.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Microstackshot.appex/com.apple.DiagnosticExtensions.Microstackshot](MACHOS/com.apple.DiagnosticExtensions.Microstackshot.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Panic.appex/com.apple.DiagnosticExtensions.Panic](MACHOS/com.apple.DiagnosticExtensions.Panic.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Phone.appex/com.apple.DiagnosticExtensions.Phone](MACHOS/com.apple.DiagnosticExtensions.Phone.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Sandbox.appex/com.apple.DiagnosticExtensions.Sandbox](MACHOS/com.apple.DiagnosticExtensions.Sandbox.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.StackShot.appex/com.apple.DiagnosticExtensions.StackShot](MACHOS/com.apple.DiagnosticExtensions.StackShot.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Telephony.appex/com.apple.DiagnosticExtensions.Telephony](MACHOS/com.apple.DiagnosticExtensions.Telephony.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.VPN.appex/com.apple.DiagnosticExtensions.VPN](MACHOS/com.apple.DiagnosticExtensions.VPN.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.VisualVoiceMail.appex/com.apple.DiagnosticExtensions.VisualVoiceMail](MACHOS/com.apple.DiagnosticExtensions.VisualVoiceMail.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.VoiceMemos.appex/com.apple.DiagnosticExtensions.VoiceMemos](MACHOS/com.apple.DiagnosticExtensions.VoiceMemos.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.WiFi.appex/com.apple.DiagnosticExtensions.WiFi](MACHOS/com.apple.DiagnosticExtensions.WiFi.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.sysdiagnose.appex/com.apple.DiagnosticExtensions.sysdiagnose](MACHOS/com.apple.DiagnosticExtensions.sysdiagnose.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.tailspin.appex/com.apple.DiagnosticExtensions.tailspin](MACHOS/com.apple.DiagnosticExtensions.tailspin.md)
- [/System/Library/PrivateFrameworks/DialogEngine.framework/catutil](MACHOS/catutil.md)
- [/System/Library/PrivateFrameworks/DictionaryServices.framework/XPCServices/com.apple.DictionaryServiceHelper.xpc/com.apple.DictionaryServiceHelper](MACHOS/com.apple.DictionaryServiceHelper.md)
- [/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/XPCServices/DPSubmissionService.xpc/DPSubmissionService](MACHOS/DPSubmissionService.md)
- [/System/Library/PrivateFrameworks/DisembarkUI.framework/PlugIns/DKFollowUpExtension.appex/DKFollowUpExtension](MACHOS/DKFollowUpExtension.md)
- [/System/Library/PrivateFrameworks/DiskImages2.framework/XPCServices/diskimagescontroller.xpc/diskimagescontroller](MACHOS/diskimagescontroller.md)
- [/System/Library/PrivateFrameworks/DiskSpaceDiagnostics.framework/PlugIns/DiskSpaceDiagnosticsExtension.appex/DiskSpaceDiagnosticsExtension](MACHOS/DiskSpaceDiagnosticsExtension.md)
- [/System/Library/PrivateFrameworks/DiskSpaceDiagnostics.framework/XPCServices/FilesystemMetadataSnapshotService.xpc/FilesystemMetadataSnapshotService](MACHOS/FilesystemMetadataSnapshotService.md)
- [/System/Library/PrivateFrameworks/DistributedEvaluation.framework/XPCServices/com.apple.siri-distributed-evaluation.xpc/com.apple.siri-distributed-evaluation](MACHOS/com.apple.siri-distributed-evaluation.md)
- [/System/Library/PrivateFrameworks/DoNotDisturb.framework/PlugIns/DoNotDisturbIntents.appex/DoNotDisturbIntents](MACHOS/DoNotDisturbIntents.md)
- [/System/Library/PrivateFrameworks/DoNotDisturbServer.framework/Support/donotdisturbd](MACHOS/donotdisturbd.md)
- [/System/Library/PrivateFrameworks/DockKitCore.framework/PlugIns/DockKitExtension.appex/DockKitExtension](MACHOS/DockKitExtension.md)
- [/System/Library/PrivateFrameworks/DocumentCamera.framework/PlugIns/com.apple.DocumentCamera.ViewService.appex/com.apple.DocumentCamera.ViewService](MACHOS/com.apple.DocumentCamera.ViewService.md)
- [/System/Library/PrivateFrameworks/DocumentManagerCore.framework/XPCServices/com.apple.DocumentManagerCore.Downloads.xpc/com.apple.DocumentManagerCore.Downloads](MACHOS/com.apple.DocumentManagerCore.Downloads.md)
- [/System/Library/PrivateFrameworks/DocumentManagerCore.framework/XPCServices/com.apple.DocumentManagerCore.Rename.xpc/com.apple.DocumentManagerCore.Rename](MACHOS/com.apple.DocumentManagerCore.Rename.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/AddTagsActionExtension.appex/AddTagsActionExtension](MACHOS/AddTagsActionExtension.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAppPopover.appex/RecentsAppPopover](MACHOS/RecentsAppPopover.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAvocado.appex/RecentsAvocado](MACHOS/RecentsAvocado.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAvocadoIntentHandler.appex/RecentsAvocadoIntentHandler](MACHOS/RecentsAvocadoIntentHandler.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/SaveToFiles.appex/SaveToFiles](MACHOS/SaveToFiles.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/com.apple.DocumentManager.Service.appex/com.apple.DocumentManager.Service](MACHOS/com.apple.DocumentManager.Service.md)
- [/System/Library/PrivateFrameworks/DocumentUnderstanding.framework/Support/textunderstandingd](MACHOS/textunderstandingd.md)
- [/System/Library/PrivateFrameworks/DocumentUnderstanding.framework/textunderstandingd](MACHOS/textunderstandingd.md)
- [/System/Library/PrivateFrameworks/DragUI.framework/Support/druid](MACHOS/druid.md)
- [/System/Library/PrivateFrameworks/EmailCore.framework/PlugIns/EmailCore.wkbundle/EmailCore](MACHOS/EmailCore.md)
- [/System/Library/PrivateFrameworks/EmailDaemon.framework/maild](MACHOS/maild.md)
- [/System/Library/PrivateFrameworks/EmbeddedDataReset.framework/Support/devicedataresetd](MACHOS/devicedataresetd.md)
- [/System/Library/PrivateFrameworks/EmbeddedDataReset.framework/XPCServices/DeviceDataResetXPCServiceWorker.xpc/DeviceDataResetXPCServiceWorker](MACHOS/DeviceDataResetXPCServiceWorker.md)
- [/System/Library/PrivateFrameworks/EmergencyAlerts.framework/PlugIns/EmergencyAlertsUIExtension.appex/EmergencyAlertsUIExtension](MACHOS/EmergencyAlertsUIExtension.md)
- [/System/Library/PrivateFrameworks/EmojiPoster.framework/PlugIns/EmojiPosterExtension.appex/EmojiPosterExtension](MACHOS/EmojiPosterExtension.md)
- [/System/Library/PrivateFrameworks/EventKitTCCUI.framework/PlugIns/EventKitTCCFullAccessNotificationUIExtension.appex/EventKitTCCFullAccessNotificationUIExtension](MACHOS/EventKitTCCFullAccessNotificationUIExtension.md)
- [/System/Library/PrivateFrameworks/EventMetaDataExtractor.framework/PlugIns/EventMetaDataExtractorPlugin.appex/EventMetaDataExtractorPlugin](MACHOS/EventMetaDataExtractorPlugin.md)
- [/System/Library/PrivateFrameworks/ExchangeSync.framework/Frameworks/DAEAS.framework/DADaemonEAS.bundle/DADaemonEAS](MACHOS/DADaemonEAS.md)
- [/System/Library/PrivateFrameworks/ExchangeSync.framework/Support/exchangesyncd](MACHOS/exchangesyncd.md)
- [/System/Library/PrivateFrameworks/ExchangeSyncExpress.framework/PlugIns/ActiveSyncOAuthService.appex/ActiveSyncOAuthService](MACHOS/ActiveSyncOAuthService.md)
- [/System/Library/PrivateFrameworks/EyeRelief.framework/Resources/eyereliefd](MACHOS/eyereliefd.md)
- [/System/Library/PrivateFrameworks/Eyedropper.framework/Support/eyedropperd](MACHOS/eyedropperd.md)
- [/System/Library/PrivateFrameworks/FMF.framework/XPCServices/FMFMapXPCService.xpc/FMFMapXPCService](MACHOS/FMFMapXPCService.md)
- [/System/Library/PrivateFrameworks/FSKit.framework/fskit_helper](MACHOS/fskit_helper.md)
- [/System/Library/PrivateFrameworks/FSKit.framework/fskitd](MACHOS/fskitd.md)
- [/System/Library/PrivateFrameworks/FaceTimeMessageStore.framework/facetimemessagestored](MACHOS/facetimemessagestored.md)
- [/System/Library/PrivateFrameworks/FamilyCircle.framework/familycircled](MACHOS/familycircled.md)
- [/System/Library/PrivateFrameworks/FamilyCircleUI.framework/PlugIns/FAFollowupExtension.appex/FAFollowupExtension](MACHOS/FAFollowupExtension.md)
- [/System/Library/PrivateFrameworks/FamilyNotification.framework/familynotificationd](MACHOS/familynotificationd.md)
- [/System/Library/PrivateFrameworks/Feedback.framework/PlugIns/DraftingExtension-iOS.appex/DraftingExtension-iOS](MACHOS/DraftingExtension-iOS.md)
- [/System/Library/PrivateFrameworks/FileProviderDaemon.framework/XPCServices/AppStoreService.xpc/AppStoreService](MACHOS/AppStoreService.md)
- [/System/Library/PrivateFrameworks/FinHealth.framework/ClientTools/finhealth_client](MACHOS/finhealth_client.md)
- [/System/Library/PrivateFrameworks/FinHealth.framework/XPCServices/FinHealthXPCServices.xpc/FinHealthXPCServices](MACHOS/FinHealthXPCServices.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceBTDiscoveryXPCService.xpc/FindMyDeviceBTDiscoveryXPCService](MACHOS/FindMyDeviceBTDiscoveryXPCService.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceEmergencyCallInfoPublisherXPCService.xpc/FindMyDeviceEmergencyCallInfoPublisherXPCService](MACHOS/FindMyDeviceEmergencyCallInfoPublisherXPCService.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceEraseXPCService.xpc/FindMyDeviceEraseXPCService](MACHOS/FindMyDeviceEraseXPCService.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceHelperXPCService.xpc/FindMyDeviceHelperXPCService](MACHOS/FindMyDeviceHelperXPCService.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceIdentityXPCService.xpc/FindMyDeviceIdentityXPCService](MACHOS/FindMyDeviceIdentityXPCService.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceUserNotificationsXPCService.xpc/FindMyDeviceUserNotificationsXPCService](MACHOS/FindMyDeviceUserNotificationsXPCService.md)
- [/System/Library/PrivateFrameworks/FitnessCoachingServices.framework/fitnesscoachingd](MACHOS/fitnesscoachingd.md)
- [/System/Library/PrivateFrameworks/FocusSettingsUI.framework/PlugIns/UserNotificationExtension.appex/UserNotificationExtension](MACHOS/UserNotificationExtension.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/Resources/UITypographyPanel.bundle/UITypographyPanel](MACHOS/UITypographyPanel.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/Support/fontservicesd](MACHOS/fontservicesd.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/XPCServices/UserFontManager.xpc/UserFontManager](MACHOS/UserFontManager.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/XPCServices/UserFontServices.xpc/UserFontServices](MACHOS/UserFontServices.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/XPCServices/com.apple.FontServices.FontProviderLoader.xpc/com.apple.FontServices.FontProviderLoader](MACHOS/com.apple.FontServices.FontProviderLoader.md)
- [/System/Library/PrivateFrameworks/GPUToolsCapture.framework/GPUToolsCapture](MACHOS/GPUToolsCapture.md)
- [/System/Library/PrivateFrameworks/GPUToolsDiagnostics.framework/GPUToolsDiagnostics](MACHOS/GPUToolsDiagnostics.md)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/PlugIns/GameCenterAuthenticateExtension.appex/GameCenterAuthenticateExtension](MACHOS/GameCenterAuthenticateExtension.md)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/PlugIns/GameCenterChallengeIssueExtension.appex/GameCenterChallengeIssueExtension](MACHOS/GameCenterChallengeIssueExtension.md)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/PlugIns/GameCenterDashboardExtension.appex/GameCenterDashboardExtension](MACHOS/GameCenterDashboardExtension.md)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/PlugIns/GameCenterMatchmakerExtension.appex/GameCenterMatchmakerExtension](MACHOS/GameCenterMatchmakerExtension.md)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/PlugIns/GameCenterTurnBasedMatchmakerExtension.appex/GameCenterTurnBasedMatchmakerExtension](MACHOS/GameCenterTurnBasedMatchmakerExtension.md)
- [/System/Library/PrivateFrameworks/GameControllerFoundation.framework/XPCServices/GameControllerConfigService.xpc/GameControllerConfigService](MACHOS/GameControllerConfigService.md)
- [/System/Library/PrivateFrameworks/GenerationalStorage.framework/revisiond](MACHOS/revisiond.md)
- [/System/Library/PrivateFrameworks/GeoAnalytics.framework/geoanalyticsd](MACHOS/geoanalyticsd.md)
- [/System/Library/PrivateFrameworks/GeoServices.framework/MapsOfflineService.bundle/MapsOfflineService](MACHOS/MapsOfflineService.md)
- [/System/Library/PrivateFrameworks/GeoServices.framework/XPCServices/com.apple.GeoServices.MapsOfflineServices.xpc/com.apple.GeoServices.MapsOfflineServices](MACHOS/com.apple.GeoServices.MapsOfflineServices.md)
- [/System/Library/PrivateFrameworks/GeoServices.framework/geod](MACHOS/geod.md)
- [/System/Library/PrivateFrameworks/GradientPoster.framework/PlugIns/GradientPosterExtension.appex/GradientPosterExtension](MACHOS/GradientPosterExtension.md)
- [/System/Library/PrivateFrameworks/GroupKit.framework/groupkitd](MACHOS/groupkitd.md)
- [/System/Library/PrivateFrameworks/HAENotifications.framework/PlugIns/HAENotificationContentExtension.appex/HAENotificationContentExtension](MACHOS/HAENotificationContentExtension.md)
- [/System/Library/PrivateFrameworks/HRTFEnrollment.framework/XPCServices/HRTFEnrollmentService.xpc/HRTFEnrollmentService](MACHOS/HRTFEnrollmentService.md)
- [/System/Library/PrivateFrameworks/HangTracer.framework/PlugIns/HangLogsDiagnosticExtension.appex/HangLogsDiagnosticExtension](MACHOS/HangLogsDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/HangTracer.framework/PlugIns/PerformanceLoggingDiagnosticExtension.appex/PerformanceLoggingDiagnosticExtension](MACHOS/PerformanceLoggingDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/HealthAlgorithms.framework/PlugIns/CycleTrackingDiagnosticExtension.appex/CycleTrackingDiagnosticExtension](MACHOS/CycleTrackingDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/HealthAlgorithms.framework/XPCServices/DayStreamProcessorService.xpc/DayStreamProcessorService](MACHOS/DayStreamProcessorService.md)
- [/System/Library/PrivateFrameworks/HealthAlgorithms.framework/XPCServices/HistoricalAnalyzerService.xpc/HistoricalAnalyzerService](MACHOS/HistoricalAnalyzerService.md)
- [/System/Library/PrivateFrameworks/HealthAppSupport.framework/PlugIns/HealthFollowUpExtension.appex/HealthFollowUpExtension](MACHOS/HealthFollowUpExtension.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsUI.framework/PlugIns/HealthMedicationsNotificationContentExtension.appex/HealthMedicationsNotificationContentExtension](MACHOS/HealthMedicationsNotificationContentExtension.md)
- [/System/Library/PrivateFrameworks/HealthMenstrualCyclesUI.framework/PlugIns/HealthMenstrualCyclesNotificationContentExtension.appex/HealthMenstrualCyclesNotificationContentExtension](MACHOS/HealthMenstrualCyclesNotificationContentExtension.md)
- [/System/Library/PrivateFrameworks/HealthPluginHost.framework/healthappd](MACHOS/healthappd.md)
- [/System/Library/PrivateFrameworks/HealthRecordServices.framework/XPCServices/com.apple.health.records.legacy-ingestion.xpc/com.apple.health.records.legacy-ingestion](MACHOS/com.apple.health.records.legacy-ingestion.md)
- [/System/Library/PrivateFrameworks/HealthRecordServices.framework/XPCServices/com.apple.health.records.xpc/com.apple.health.records](MACHOS/com.apple.health.records.md)
- [/System/Library/PrivateFrameworks/HealthRecordServices.framework/healthrecordsd](MACHOS/healthrecordsd.md)
- [/System/Library/PrivateFrameworks/HearingCore.framework/heard](MACHOS/heard.md)
- [/System/Library/PrivateFrameworks/HearingMLHelper.framework/XPCServices/HearingMLHelperService.xpc/HearingMLHelperService](MACHOS/HearingMLHelperService.md)
- [/System/Library/PrivateFrameworks/HeartRhythmAlgorithms.framework/PlugIns/IRNDiagnosticExtension.appex/IRNDiagnosticExtension](MACHOS/IRNDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/HomeAI.framework/PlugIns/HomeAIDESExtension.appex/HomeAIDESExtension](MACHOS/HomeAIDESExtension.md)
- [/System/Library/PrivateFrameworks/HomeEnergyDaemon.framework/Support/homeenergyd](MACHOS/homeenergyd.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemon.framework/Support/homed](MACHOS/homed.md)
- [/System/Library/PrivateFrameworks/HomePlatformSettingsUI.framework/PlugIns/HPSUIViewService.appex/HPSUIViewService](MACHOS/HPSUIViewService.md)
- [/System/Library/PrivateFrameworks/IAP.framework/Support/iap2d](MACHOS/iap2d.md)
- [/System/Library/PrivateFrameworks/IAP.framework/Support/iapd](MACHOS/iapd.md)
- [/System/Library/PrivateFrameworks/IAP.framework/Support/iaptransportd](MACHOS/iaptransportd.md)
- [/System/Library/PrivateFrameworks/IAPAuthentication.framework/Support/iapauthd](MACHOS/iapauthd.md)
- [/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd](MACHOS/identityservicesd.md)
- [/System/Library/PrivateFrameworks/IDSBlastDoorSupport.framework/XPCServices/IDSBlastDoorService.xpc/IDSBlastDoorService](MACHOS/IDSBlastDoorService.md)
- [/System/Library/PrivateFrameworks/IDSFoundation.framework/IDSCredentialsAgent.app/IDSCredentialsAgent](MACHOS/IDSCredentialsAgent.md)
- [/System/Library/PrivateFrameworks/IDSFoundation.framework/IDSRemoteURLConnectionAgent.app/IDSRemoteURLConnectionAgent](MACHOS/IDSRemoteURLConnectionAgent.md)
- [/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/imagent](MACHOS/imagent.md)
- [/System/Library/PrivateFrameworks/IMDMessageServices.framework/XPCServices/IMDMessageServicesAgent.xpc/IMDMessageServicesAgent](MACHOS/IMDMessageServicesAgent.md)
- [/System/Library/PrivateFrameworks/IMDPersistence.framework/IMAutomaticHistoryDeletionAgent.app/IMAutomaticHistoryDeletionAgent](MACHOS/IMAutomaticHistoryDeletionAgent.md)
- [/System/Library/PrivateFrameworks/IMDPersistence.framework/XPCServices/IMDPersistenceAgent.xpc/IMDPersistenceAgent](MACHOS/IMDPersistenceAgent.md)
- [/System/Library/PrivateFrameworks/IMTranscoding.framework/XPCServices/IMTranscoderAgent.xpc/IMTranscoderAgent](MACHOS/IMTranscoderAgent.md)
- [/System/Library/PrivateFrameworks/IMTransferServices.framework/IMTransferAgent.app/IMTransferAgent](MACHOS/IMTransferAgent.md)
- [/System/Library/PrivateFrameworks/IOAccessoryManager.framework/PlugIns/WetNotification.appex/WetNotification](MACHOS/WetNotification.md)
- [/System/Library/PrivateFrameworks/IOSurfaceAccelerator.framework/Resources/IOSADiagnose](MACHOS/IOSADiagnose.md)
- [/System/Library/PrivateFrameworks/InAppMessages.framework/PlugIns/InAppMessagesWebProcessBundle.bundle/InAppMessagesWebProcessBundle](MACHOS/InAppMessagesWebProcessBundle.md)
- [/System/Library/PrivateFrameworks/InstallCoordination.framework/Support/installcoordination_proxy](MACHOS/installcoordination_proxy.md)
- [/System/Library/PrivateFrameworks/InstallCoordination.framework/Support/installcoordinationd](MACHOS/installcoordinationd.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatform.framework/PlugIns/DiagnosticExtension.appex/DiagnosticExtension](MACHOS/DiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCompute.framework/XPCServices/IntelligencePlatformComputeService.xpc/IntelligencePlatformComputeService](MACHOS/IntelligencePlatformComputeService.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/PlugIns/ERMLRuntimePlugin.appex/ERMLRuntimePlugin](MACHOS/ERMLRuntimePlugin.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/PlugIns/IntelligencePlatformLighthousePlugin.appex/IntelligencePlatformLighthousePlugin](MACHOS/IntelligencePlatformLighthousePlugin.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/intelligenceplatformd](MACHOS/intelligenceplatformd.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/knowledgeconstructiond](MACHOS/knowledgeconstructiond.md)
- [/System/Library/PrivateFrameworks/IntlPreferences.framework/Support/localizationswitcherd](MACHOS/localizationswitcherd.md)
- [/System/Library/PrivateFrameworks/LighthouseAV.framework/PlugIns/LighthouseAVPlugin.appex/LighthouseAVPlugin](MACHOS/LighthouseAVPlugin.md)
- [/System/Library/PrivateFrameworks/LighthouseBitacoraFramework.framework/PlugIns/LighthouseBitacoraPlugin.appex/LighthouseBitacoraPlugin](MACHOS/LighthouseBitacoraPlugin.md)
- [/System/Library/PrivateFrameworks/LighthouseDictation.framework/PlugIns/LighthouseDictationPlugin.appex/LighthouseDictationPlugin](MACHOS/LighthouseDictationPlugin.md)
- [/System/Library/PrivateFrameworks/LighthouseNightingale.framework/PlugIns/LighthouseNightingalePluginBattery.appex/LighthouseNightingalePluginBattery](MACHOS/LighthouseNightingalePluginBattery.md)
- [/System/Library/PrivateFrameworks/LighthouseNightingale.framework/PlugIns/LighthouseNightingalePluginCharger.appex/LighthouseNightingalePluginCharger](MACHOS/LighthouseNightingalePluginCharger.md)
- [/System/Library/PrivateFrameworks/LighthousePAN.framework/PlugIns/LighthousePAN.appex/LighthousePAN](MACHOS/LighthousePAN.md)
- [/System/Library/PrivateFrameworks/LockdownMode.framework/lockdownmoded](MACHOS/lockdownmoded.md)
- [/System/Library/PrivateFrameworks/MFAAuthentication.framework/XPCServices/MFAANetwork.xpc/MFAANetwork](MACHOS/MFAANetwork.md)
- [/System/Library/PrivateFrameworks/MLCompilerServices.framework/XPCServices/MLCompilerOSXPC.xpc/MLCompilerOSXPC](MACHOS/MLCompilerOSXPC.md)
- [/System/Library/PrivateFrameworks/MLKit.framework/PlugIns/com.apple.MLKit.MLModelPreview.appex/com.apple.MLKit.MLModelPreview](MACHOS/com.apple.MLKit.MLModelPreview.md)
- [/System/Library/PrivateFrameworks/MLKit.framework/PlugIns/com.apple.MLKit.MLPackagePreview.appex/com.apple.MLKit.MLPackagePreview](MACHOS/com.apple.MLKit.MLPackagePreview.md)
- [/System/Library/PrivateFrameworks/MacinTalk.framework/PlugIns/MacinTalkAUSP.appex/MacinTalkAUSP](MACHOS/MacinTalkAUSP.md)
- [/System/Library/PrivateFrameworks/ManagedConfiguration.framework/PlugIns/ManagedSettingsExtension.appex/ManagedSettingsExtension](MACHOS/ManagedSettingsExtension.md)
- [/System/Library/PrivateFrameworks/MapsSuggestions.framework/destinationd](MACHOS/destinationd.md)
- [/System/Library/PrivateFrameworks/MapsSupport.framework/geocorrectiond](MACHOS/geocorrectiond.md)
- [/System/Library/PrivateFrameworks/MapsSupport.framework/mapspushd](MACHOS/mapspushd.md)
- [/System/Library/PrivateFrameworks/MapsSupport.framework/nanomapscd](MACHOS/nanomapscd.md)
- [/System/Library/PrivateFrameworks/MapsSupport.framework/navd](MACHOS/navd.md)
- [/System/Library/PrivateFrameworks/MapsSync.framework/mapssyncd](MACHOS/mapssyncd.md)
- [/System/Library/PrivateFrameworks/MarkupUI.framework/PlugIns/MarkupPhotoExtension.appex/MarkupPhotoExtension](MACHOS/MarkupPhotoExtension.md)
- [/System/Library/PrivateFrameworks/MarkupUI.framework/PlugIns/MarkupPrivateExtension.appex/MarkupPrivateExtension](MACHOS/MarkupPrivateExtension.md)
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd](MACHOS/mediaanalysisd.md)
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd-service](MACHOS/mediaanalysisd-service.md)
- [/System/Library/PrivateFrameworks/MediaConversionService.framework/XPCServices/com.apple.photos.ImageConversionService.xpc/com.apple.photos.ImageConversionService](MACHOS/com.apple.photos.ImageConversionService.md)
- [/System/Library/PrivateFrameworks/MediaConversionService.framework/XPCServices/com.apple.photos.VideoConversionService.xpc/com.apple.photos.VideoConversionService](MACHOS/com.apple.photos.VideoConversionService.md)
- [/System/Library/PrivateFrameworks/MediaMLServices.framework/XPCServices/mediamlxpc.xpc/mediamlxpc](MACHOS/mediamlxpc.md)
- [/System/Library/PrivateFrameworks/MediaRemote.framework/Support/mediaremoted](MACHOS/mediaremoted.md)
- [/System/Library/PrivateFrameworks/MediaServices.framework/Support/mediaartworkd](MACHOS/mediaartworkd.md)
- [/System/Library/PrivateFrameworks/MediaServicesBroker.framework/PlugIns/MediaSetupViewService.appex/MediaSetupViewService](MACHOS/MediaSetupViewService.md)
- [/System/Library/PrivateFrameworks/MediaStream.framework/Support/mstreamd](MACHOS/mstreamd.md)
- [/System/Library/PrivateFrameworks/MentalHealthUI.framework/archive.metallib](MACHOS/archive.metallib.md)
- [/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/XPCServices/MessagesAirlockService.xpc/MessagesAirlockService](MACHOS/MessagesAirlockService.md)
- [/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/XPCServices/MessagesBlastDoorService.xpc/MessagesBlastDoorService](MACHOS/MessagesBlastDoorService.md)
- [/System/Library/PrivateFrameworks/MetricMeasurement.framework/XPCServices/MetricMeasurementHelper.xpc/MetricMeasurementHelper](MACHOS/MetricMeasurementHelper.md)
- [/System/Library/PrivateFrameworks/MetricsKit.framework/XPCServices/AMPIDService.xpc/AMPIDService](MACHOS/AMPIDService.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/Support/accessoryupdaterd](MACHOS/accessoryupdaterd.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/Support/auearlyboot](MACHOS/auearlyboot.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/AppleEmbeddedAccessoryUpdaterService.xpc/AppleEmbeddedAccessoryUpdaterService](MACHOS/AppleEmbeddedAccessoryUpdaterService.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/AppleSTDP2700BootstrapService.xpc/AppleSTDP2700BootstrapService](MACHOS/AppleSTDP2700BootstrapService.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/DurianUpdaterService.xpc/DurianUpdaterService](MACHOS/DurianUpdaterService.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/EAUpdaterService.xpc/EAUpdaterService](MACHOS/EAUpdaterService.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/GenericKextUpdaterService.xpc/GenericKextUpdaterService](MACHOS/GenericKextUpdaterService.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/StandaloneHIDAudService.xpc/StandaloneHIDAudService](MACHOS/StandaloneHIDAudService.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceAFU.xpc/UARPUpdaterServiceAFU](MACHOS/UARPUpdaterServiceAFU.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceHID.xpc/UARPUpdaterServiceHID](MACHOS/UARPUpdaterServiceHID.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceLegacyAudio.xpc/UARPUpdaterServiceLegacyAudio](MACHOS/UARPUpdaterServiceLegacyAudio.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceUSBPD.xpc/UARPUpdaterServiceUSBPD](MACHOS/UARPUpdaterServiceUSBPD.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/USBCAccessoryUpdaterService.xpc/USBCAccessoryUpdaterService](MACHOS/USBCAccessoryUpdaterService.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackupCacheDeleteService](MACHOS/MobileBackupCacheDeleteService.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/PlugIns/MBDiagnosticExtension.appex/MBDiagnosticExtension](MACHOS/MBDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/PlugIns/MBFollowUpExtension.appex/MBFollowUpExtension](MACHOS/MBFollowUpExtension.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/PlugIns/MBPrebuddyFollowUpExtension.appex/MBPrebuddyFollowUpExtension](MACHOS/MBPrebuddyFollowUpExtension.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/XPCServices/MBHelperService.xpc/MBHelperService](MACHOS/MBHelperService.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/backupd](MACHOS/backupd.md)
- [/System/Library/PrivateFrameworks/MobileInstallation.framework/XPCServices/com.apple.MobileInstallationHelperService.xpc/com.apple.MobileInstallationHelperService](MACHOS/com.apple.MobileInstallationHelperService.md)
- [/System/Library/PrivateFrameworks/MobileMailUI.framework/PlugIns/MailWebProcessBundle.bundle/MailWebProcessBundle](MACHOS/MailWebProcessBundle.md)
- [/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/Support/softwareupdated](MACHOS/softwareupdated.md)
- [/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/XPCServices/com.apple.MobileSoftwareUpdate.CleanupPreparePathService.xpc/com.apple.MobileSoftwareUpdate.CleanupPreparePathService](MACHOS/com.apple.MobileSoftwareUpdate.CleanupPreparePathService.md)
- [/System/Library/PrivateFrameworks/MobileTimer.framework/Executables/mobiletimerd](MACHOS/mobiletimerd.md)
- [/System/Library/PrivateFrameworks/MobileTimer.framework/PlugIns/MobileTimerIntents.appex/MobileTimerIntents](MACHOS/MobileTimerIntents.md)
- [/System/Library/PrivateFrameworks/MobileTimer.framework/PlugIns/MobileTimerNotificationExtension.appex/MobileTimerNotificationExtension](MACHOS/MobileTimerNotificationExtension.md)
- [/System/Library/PrivateFrameworks/MultitouchSessionFilterSupport.framework/XPCServices/SessionFilterPreferenceProvider.xpc/SessionFilterPreferenceProvider](MACHOS/SessionFilterPreferenceProvider.md)
- [/System/Library/PrivateFrameworks/MultitouchSessionFilterSupport.framework/XPCServices/SessionFilterRecordingUpdater.xpc/SessionFilterRecordingUpdater](MACHOS/SessionFilterRecordingUpdater.md)
- [/System/Library/PrivateFrameworks/MusicLibrary.framework/Support/medialibraryd](MACHOS/medialibraryd.md)
- [/System/Library/PrivateFrameworks/NLPLearner.framework/PlugIns/NLPLearnerQuickTypeLighthousePlugin.appex/NLPLearnerQuickTypeLighthousePlugin](MACHOS/NLPLearnerQuickTypeLighthousePlugin.md)
- [/System/Library/PrivateFrameworks/NLPLearner.framework/PlugIns/QuickTypePFLExtension.appex/QuickTypePFLExtension](MACHOS/QuickTypePFLExtension.md)
- [/System/Library/PrivateFrameworks/NPTKit.framework/PlugIns/NPTCellularDiagnosticsExtension.appex/NPTCellularDiagnosticsExtension](MACHOS/NPTCellularDiagnosticsExtension.md)
- [/System/Library/PrivateFrameworks/NPTKit.framework/PlugIns/NPTWiFiDiagnosticsExtension.appex/NPTWiFiDiagnosticsExtension](MACHOS/NPTWiFiDiagnosticsExtension.md)
- [/System/Library/PrivateFrameworks/NanoAppRegistry.framework/Support/nanoappregistryd](MACHOS/nanoappregistryd.md)
- [/System/Library/PrivateFrameworks/NanoBackup.framework/nanobackupd](MACHOS/nanobackupd.md)
- [/System/Library/PrivateFrameworks/NanoLeash.framework/companionfindlocallyd](MACHOS/companionfindlocallyd.md)
- [/System/Library/PrivateFrameworks/NanoLeash.framework/findme](MACHOS/findme.md)
- [/System/Library/PrivateFrameworks/NanoMusicSync.framework/PlugIns/NanoMediaDiagnosticExtension.appex/NanoMediaDiagnosticExtension](MACHOS/NanoMediaDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/NanoPassKit.framework/NPKCompanionAgent](MACHOS/NPKCompanionAgent.md)
- [/System/Library/PrivateFrameworks/NanoPreferencesSync.framework/nanoprefsyncd](MACHOS/nanoprefsyncd.md)
- [/System/Library/PrivateFrameworks/NanoSystemSettings.framework/nanosystemsettingsd](MACHOS/nanosystemsettingsd.md)
- [/System/Library/PrivateFrameworks/NanoTimeKit.framework/PlugIns/NTKDiagnosticExtensionCompanion.appex/NTKDiagnosticExtensionCompanion](MACHOS/NTKDiagnosticExtensionCompanion.md)
- [/System/Library/PrivateFrameworks/NanoTimeKit.framework/PlugIns/com.apple.NanoTimeKit.CreateWatchFace.appex/com.apple.NanoTimeKit.CreateWatchFace](MACHOS/com.apple.NanoTimeKit.CreateWatchFace.md)
- [/System/Library/PrivateFrameworks/NanoTimeKit.framework/XPCServices/BundleComplicationMigrationService.xpc/BundleComplicationMigrationService](MACHOS/BundleComplicationMigrationService.md)
- [/System/Library/PrivateFrameworks/NanoTimeKit.framework/XPCServices/GreenfieldService-Companion.xpc/GreenfieldService-Companion](MACHOS/GreenfieldService-Companion.md)
- [/System/Library/PrivateFrameworks/NanoTimeKit.framework/XPCServices/NTKFaceSnapshotService.xpc/NTKFaceSnapshotService](MACHOS/NTKFaceSnapshotService.md)
- [/System/Library/PrivateFrameworks/NanoTimeKit.framework/nanotimekitcompaniond](MACHOS/nanotimekitcompaniond.md)
- [/System/Library/PrivateFrameworks/NearbySessions.framework/XPCServices/com.apple.SharePlay.NearbyInvitationsService.xpc/com.apple.SharePlay.NearbyInvitationsService](MACHOS/com.apple.SharePlay.NearbyInvitationsService.md)
- [/System/Library/PrivateFrameworks/NeighborhoodActivityConduit.framework/XPCServices/com.apple.NeighborhoodActivityConduitService.xpc/com.apple.NeighborhoodActivityConduitService](MACHOS/com.apple.NeighborhoodActivityConduitService.md)
- [/System/Library/PrivateFrameworks/NetworkQualityServices.framework/XPCServices/NetworkQualityXPC.xpc/NetworkQualityXPC](MACHOS/NetworkQualityXPC.md)
- [/System/Library/PrivateFrameworks/NetworkRelay.framework/PlugIns/NRDiagnosticExtension.appex/NRDiagnosticExtension](MACHOS/NRDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/PlugIns/NewDeviceOutreachExtension.appex/NewDeviceOutreachExtension](MACHOS/NewDeviceOutreachExtension.md)
- [/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/ndoagent](MACHOS/ndoagent.md)
- [/System/Library/PrivateFrameworks/NewsDaemon.framework/newsd](MACHOS/newsd.md)
- [/System/Library/PrivateFrameworks/NewsServices.framework/PlugIns/NewsArticleViewer.appex/NewsArticleViewer](MACHOS/NewsArticleViewer.md)
- [/System/Library/PrivateFrameworks/NewsServices.framework/nanonewscd](MACHOS/nanonewscd.md)
- [/System/Library/PrivateFrameworks/NotesShared.framework/XPCServices/com.apple.mobilenotes.datastore.xpc/com.apple.mobilenotes.datastore](MACHOS/com.apple.mobilenotes.datastore.md)
- [/System/Library/PrivateFrameworks/NotesUI.framework/XPCServices/com.apple.mobilenotes.HTMLConverter.xpc/com.apple.mobilenotes.HTMLConverter](MACHOS/com.apple.mobilenotes.HTMLConverter.md)
- [/System/Library/PrivateFrameworks/NotesUI.framework/XPCServices/com.apple.mobilenotes.LPPreviewGenerator.xpc/com.apple.mobilenotes.LPPreviewGenerator](MACHOS/com.apple.mobilenotes.LPPreviewGenerator.md)
- [/System/Library/PrivateFrameworks/NotesUI.framework/XPCServices/com.apple.mobilenotes.NotesImporter.xpc/com.apple.mobilenotes.NotesImporter](MACHOS/com.apple.mobilenotes.NotesImporter.md)
- [/System/Library/PrivateFrameworks/OSAnalytics.framework/PlugIns/IPSExtension.appex/IPSExtension](MACHOS/IPSExtension.md)
- [/System/Library/PrivateFrameworks/OfficeImport.framework/PlugIns/OfficeSpotlightImporter.appex/OfficeSpotlightImporter](MACHOS/OfficeSpotlightImporter.md)
- [/System/Library/PrivateFrameworks/PBBridgeSupport.framework/PlugIns/BridgeIntents.appex/BridgeIntents](MACHOS/BridgeIntents.md)
- [/System/Library/PrivateFrameworks/PairedSync.framework/Support/pairedsyncd](MACHOS/pairedsyncd.md)
- [/System/Library/PrivateFrameworks/PairedUnlock.framework/pairedunlockd](MACHOS/pairedunlockd.md)
- [/System/Library/PrivateFrameworks/PairingProximity.framework/XPCServices/com.apple.Bridge.ppNotifierService.xpc/com.apple.Bridge.ppNotifierService](MACHOS/com.apple.Bridge.ppNotifierService.md)
- [/System/Library/PrivateFrameworks/PaperBoardUI.framework/XPCServices/SBRendererService.xpc/SBRendererService](MACHOS/SBRendererService.md)
- [/System/Library/PrivateFrameworks/PaperKit.framework/PlugIns/MarkupPhotoEditingExtension.appex/MarkupPhotoEditingExtension](MACHOS/MarkupPhotoEditingExtension.md)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/XPCServices/PassKitCoreXPCService.xpc/PassKitCoreXPCService](MACHOS/PassKitCoreXPCService.md)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/passd](MACHOS/passd.md)
- [/System/Library/PrivateFrameworks/PassKitServices.framework/XPCServices/PassKitServicesXPCService.xpc/PassKitServicesXPCService](MACHOS/PassKitServicesXPCService.md)
- [/System/Library/PrivateFrameworks/Pasteboard.framework/Support/pasted](MACHOS/pasted.md)
- [/System/Library/PrivateFrameworks/People.framework/peopled](MACHOS/peopled.md)
- [/System/Library/PrivateFrameworks/PerfPowerServicesReader.framework/XPCServices/PerfPowerTelemetryReaderService.xpc/PerfPowerTelemetryReaderService](MACHOS/PerfPowerTelemetryReaderService.md)
- [/System/Library/PrivateFrameworks/PerformanceTrace.framework/XPCServices/com.apple.PerformanceTrace.PerformanceTraceService.xpc/com.apple.PerformanceTrace.PerformanceTraceService](MACHOS/com.apple.PerformanceTrace.PerformanceTraceService.md)
- [/System/Library/PrivateFrameworks/PhotoAnalysis.framework/PlugIns/PhotoAnalysisLighthousePlugin.appex/PhotoAnalysisLighthousePlugin](MACHOS/PhotoAnalysisLighthousePlugin.md)
- [/System/Library/PrivateFrameworks/PhotoAnalysis.framework/Support/photoanalysisd](MACHOS/photoanalysisd.md)
- [/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/PlugIns/PhotosDiagnostics.appex/PhotosDiagnostics](MACHOS/PhotosDiagnostics.md)
- [/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PlugIns/AmbientPhotoFramePosterProvider.appex/AmbientPhotoFramePosterProvider](MACHOS/AmbientPhotoFramePosterProvider.md)
- [/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PlugIns/PhotosPosterProvider.appex/PhotosPosterProvider](MACHOS/PhotosPosterProvider.md)
- [/System/Library/PrivateFrameworks/PlugInKitDaemon.framework/PlugInKitDaemon](MACHOS/PlugInKitDaemon.md)
- [/System/Library/PrivateFrameworks/PointerUIServices.framework/Support/pointeruid](MACHOS/pointeruid.md)
- [/System/Library/PrivateFrameworks/PowerLog.framework/XPCServices/PerfPowerTelemetryClientRegistrationService.xpc/PerfPowerTelemetryClientRegistrationService](MACHOS/PerfPowerTelemetryClientRegistrationService.md)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/PlugIns/DEPowerlogEPL.appex/DEPowerlogEPL](MACHOS/DEPowerlogEPL.md)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/PlugIns/com.apple.PowerlogCore.diagnosticextension.appex/com.apple.PowerlogCore.diagnosticextension](MACHOS/com.apple.PowerlogCore.diagnosticextension.md)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/XPCServices/PerfPowerServicesSignpostReader.xpc/PerfPowerServicesSignpostReader](MACHOS/PerfPowerServicesSignpostReader.md)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/XPCServices/rbdcConverter.xpc/rbdcConverter](MACHOS/rbdcConverter.md)
- [/System/Library/PrivateFrameworks/PreviewsOSSupport.framework/Support/previewsd](MACHOS/previewsd.md)
- [/System/Library/PrivateFrameworks/PridePoster.framework/PlugIns/PridePosterExtension.appex/PridePosterExtension](MACHOS/PridePosterExtension.md)
- [/System/Library/PrivateFrameworks/PrintKit.framework/XPCServices/com.apple.PrintKit.PrinterTool.xpc/com.apple.PrintKit.PrinterTool](MACHOS/com.apple.PrintKit.PrinterTool.md)
- [/System/Library/PrivateFrameworks/PrintKit.framework/XPCServices/printbandservice.xpc/printbandservice](MACHOS/printbandservice.md)
- [/System/Library/PrivateFrameworks/PrivacyAccounting.framework/Versions/A/Resources/privacyaccountingd](MACHOS/privacyaccountingd.md)
- [/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePlugin.appex/DPMLRuntimePlugin](MACHOS/DPMLRuntimePlugin.md)
- [/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePluginClassB.appex/DPMLRuntimePluginClassB](MACHOS/DPMLRuntimePluginClassB.md)
- [/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePluginNonDnU.appex/DPMLRuntimePluginNonDnU](MACHOS/DPMLRuntimePluginNonDnU.md)
- [/System/Library/PrivateFrameworks/ProactiveShareSheetDataHarvestingLighthouse.framework/PlugIns/ProactiveShareSheetDataHarvestingLighthousePlugin.appex/ProactiveShareSheetDataHarvestingLighthousePlugin](MACHOS/ProactiveShareSheetDataHarvestingLighthousePlugin.md)
- [/System/Library/PrivateFrameworks/ProfileValidatedAppIdentity.framework/XPCServices/ProfileValidatedAppIdentityService.xpc/ProfileValidatedAppIdentityService](MACHOS/ProfileValidatedAppIdentityService.md)
- [/System/Library/PrivateFrameworks/PromotedContentPrediction.framework/PlugIns/SearchResultsExtension.appex/SearchResultsExtension](MACHOS/SearchResultsExtension.md)
- [/System/Library/PrivateFrameworks/PromotedContentProxy.framework/PlugIns/PromotedContentWebProcessBundle.bundle/PromotedContentWebProcessBundle](MACHOS/PromotedContentWebProcessBundle.md)
- [/System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/Helpers/ProtectedCloudKeySyncing](MACHOS/ProtectedCloudKeySyncing.md)
- [/System/Library/PrivateFrameworks/PrototypeToolsUI.framework/prototyped](MACHOS/prototyped.md)
- [/System/Library/PrivateFrameworks/Quagga.framework/QuaggaNeuralNetworks.bundle/QuaggaNeuralNetworks](MACHOS/QuaggaNeuralNetworks.md)
- [/System/Library/PrivateFrameworks/Quagga.framework/XPCServices/com.apple.Quagga.Decode.xpc/com.apple.Quagga.Decode](MACHOS/com.apple.Quagga.Decode.md)
- [/System/Library/PrivateFrameworks/RTTUI.framework/PlugIns/RTTNotificationContentExtension.appex/RTTNotificationContentExtension](MACHOS/RTTNotificationContentExtension.md)
- [/System/Library/PrivateFrameworks/RelevanceEngine.framework/relevanced](MACHOS/relevanced.md)
- [/System/Library/PrivateFrameworks/ReminderKit.framework/PlugIns/RemindersNotificationContentExtension.appex/RemindersNotificationContentExtension](MACHOS/RemindersNotificationContentExtension.md)
- [/System/Library/PrivateFrameworks/ReminderKitUI.framework/PlugIns/com.apple.ReminderKitUI.ReminderCreationViewService.appex/com.apple.ReminderKitUI.ReminderCreationViewService](MACHOS/com.apple.ReminderKitUI.ReminderCreationViewService.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/RemoteManagementAgent](MACHOS/RemoteManagementAgent.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/ASConfigurationSubscriber.xpc/ASConfigurationSubscriber](MACHOS/ASConfigurationSubscriber.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/AccountSubscriber.xpc/AccountSubscriber](MACHOS/AccountSubscriber.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/InteractiveLegacyProfilesSubscriber.xpc/InteractiveLegacyProfilesSubscriber](MACHOS/InteractiveLegacyProfilesSubscriber.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/LegacyProfilesSubscriber.xpc/LegacyProfilesSubscriber](MACHOS/LegacyProfilesSubscriber.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/MDMAppSubscriber.xpc/MDMAppSubscriber](MACHOS/MDMAppSubscriber.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/ManagedAppsSubscriber.xpc/ManagedAppsSubscriber](MACHOS/ManagedAppsSubscriber.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/ManagementTestSubscriber.xpc/ManagementTestSubscriber](MACHOS/ManagementTestSubscriber.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/PasscodeSettingsSubscriber.xpc/PasscodeSettingsSubscriber](MACHOS/PasscodeSettingsSubscriber.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/PowerSubscriber.xpc/PowerSubscriber](MACHOS/PowerSubscriber.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/SecuritySubscriber.xpc/SecuritySubscriber](MACHOS/SecuritySubscriber.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/SoftwareUpdateSubscriber.xpc/SoftwareUpdateSubscriber](MACHOS/SoftwareUpdateSubscriber.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/WatchEnrollmentSubscriber.xpc/WatchEnrollmentSubscriber](MACHOS/WatchEnrollmentSubscriber.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/remotemanagementd](MACHOS/remotemanagementd.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/rmdinspect](MACHOS/rmdinspect.md)
- [/System/Library/PrivateFrameworks/RemoteMediaServices.framework/remotemediaservicesd](MACHOS/remotemediaservicesd.md)
- [/System/Library/PrivateFrameworks/SFSymbols.framework/CoreGlyphsPrivate.bundle/CoreGlyphsPrivate](MACHOS/CoreGlyphsPrivate.md)
- [/System/Library/PrivateFrameworks/SMBClientProvider.framework/PlugIns/com.apple.SMBClientProvider.FileProvider.appex/com.apple.SMBClientProvider.FileProvider](MACHOS/com.apple.SMBClientProvider.FileProvider.md)
- [/System/Library/PrivateFrameworks/SMBClientProvider.framework/smbclientTool](MACHOS/smbclientTool.md)
- [/System/Library/PrivateFrameworks/SMBClientProvider.framework/smbclientd](MACHOS/smbclientd.md)
- [/System/Library/PrivateFrameworks/SOS.framework/sosd](MACHOS/sosd.md)
- [/System/Library/PrivateFrameworks/STSXPCHelperClient.framework/XPCServices/STSXPCHelper.xpc/STSXPCHelper](MACHOS/STSXPCHelper.md)
- [/System/Library/PrivateFrameworks/SafariFoundation.framework/XPCServices/AutoFillHelper.xpc/AutoFillHelper](MACHOS/AutoFillHelper.md)
- [/System/Library/PrivateFrameworks/SafariFoundation.framework/XPCServices/CredentialProviderExtensionHelper.xpc/CredentialProviderExtensionHelper](MACHOS/CredentialProviderExtensionHelper.md)
- [/System/Library/PrivateFrameworks/SafariSafeBrowsing.framework/com.apple.Safari.SafeBrowsing.Service](MACHOS/com.apple.Safari.SafeBrowsing.Service.md)
- [/System/Library/PrivateFrameworks/SafariShared.framework/XPCServices/com.apple.Safari.SearchHelper.xpc/com.apple.Safari.SearchHelper](MACHOS/com.apple.Safari.SearchHelper.md)
- [/System/Library/PrivateFrameworks/SchoolTime.framework/Support/schooltimed](MACHOS/schooltimed.md)
- [/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeAgent](MACHOS/ScreenTimeAgent.md)
- [/System/Library/PrivateFrameworks/ScreenTimeUI.framework/Extensions/ScreenTimeReportExtension.appex/ScreenTimeReportExtension](MACHOS/ScreenTimeReportExtension.md)
- [/System/Library/PrivateFrameworks/ScreenTimeUI.framework/PlugIns/ScreenTimeNotificationContentExtension.appex/ScreenTimeNotificationContentExtension](MACHOS/ScreenTimeNotificationContentExtension.md)
- [/System/Library/PrivateFrameworks/Search.framework/PlugIns/SpotlightDiagnostic.appex/SpotlightDiagnostic](MACHOS/SpotlightDiagnostic.md)
- [/System/Library/PrivateFrameworks/Search.framework/searchd](MACHOS/searchd.md)
- [/System/Library/PrivateFrameworks/SensorKitHelper.framework/XPCServices/com.apple.SensorKit.SKMediaEventsHelper.xpc/com.apple.SensorKit.SKMediaEventsHelper](MACHOS/com.apple.SensorKit.SKMediaEventsHelper.md)
- [/System/Library/PrivateFrameworks/SessionCore.framework/Support/liveactivitiesd](MACHOS/liveactivitiesd.md)
- [/System/Library/PrivateFrameworks/SetupAssistant.framework/budd](MACHOS/budd.md)
- [/System/Library/PrivateFrameworks/SeymourServices.framework/PlugIns/SeymourEngagementExtension.appex/SeymourEngagementExtension](MACHOS/SeymourEngagementExtension.md)
- [/System/Library/PrivateFrameworks/SeymourServices.framework/PlugIns/SeymourNotifications.appex/SeymourNotifications](MACHOS/SeymourNotifications.md)
- [/System/Library/PrivateFrameworks/SeymourServices.framework/PlugIns/diagnosticextension.appex/diagnosticextension](MACHOS/diagnosticextension.md)
- [/System/Library/PrivateFrameworks/SeymourServices.framework/fitcored](MACHOS/fitcored.md)
- [/System/Library/PrivateFrameworks/SeymourServices.framework/fitcoresessiond](MACHOS/fitcoresessiond.md)
- [/System/Library/PrivateFrameworks/SharedWebCredentials.framework/Support/swcutil](MACHOS/swcutil.md)
- [/System/Library/PrivateFrameworks/Sharing.framework/PlugIns/AirDrop.appex/AirDrop](MACHOS/AirDrop.md)
- [/System/Library/PrivateFrameworks/Sharing.framework/PlugIns/AirDropAlertUI.appex/AirDropAlertUI](MACHOS/AirDropAlertUI.md)
- [/System/Library/PrivateFrameworks/Sharing.framework/PlugIns/AirDropNotice.appex/AirDropNotice](MACHOS/AirDropNotice.md)
- [/System/Library/PrivateFrameworks/Sharing.framework/PlugIns/ContinuityRemote.appex/ContinuityRemote](MACHOS/ContinuityRemote.md)
- [/System/Library/PrivateFrameworks/SharingHUD.framework/XPCServices/SharingHUDService.xpc/SharingHUDService](MACHOS/SharingHUDService.md)
- [/System/Library/PrivateFrameworks/SharingXPCServices.framework/XPCServices/SharingXPCHelper.xpc/SharingXPCHelper](MACHOS/SharingXPCHelper.md)
- [/System/Library/PrivateFrameworks/SiriAppLaunchIntents.framework/PlugIns/AppLaunchIntentExtension.appex/AppLaunchIntentExtension](MACHOS/AppLaunchIntentExtension.md)
- [/System/Library/PrivateFrameworks/SiriContactsIntents.framework/PlugIns/ContactsIntentExtension.appex/ContactsIntentExtension](MACHOS/ContactsIntentExtension.md)
- [/System/Library/PrivateFrameworks/SiriCoreMetrics.framework/PlugIns/SiriCoreMetricsPlugin.appex/SiriCoreMetricsPlugin](MACHOS/SiriCoreMetricsPlugin.md)
- [/System/Library/PrivateFrameworks/SiriGeo.framework/PlugIns/SiriGeoIntentExtension.appex/SiriGeoIntentExtension](MACHOS/SiriGeoIntentExtension.md)
- [/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/PlugIns/IdentityIntentExtension.appex/IdentityIntentExtension](MACHOS/IdentityIntentExtension.md)
- [/System/Library/PrivateFrameworks/SiriInference.framework/Support/siriinferenced](MACHOS/siriinferenced.md)
- [/System/Library/PrivateFrameworks/SiriInferredHelpfulness.framework/PlugIns/SiriInferredHelpfulnessPlugin.appex/SiriInferredHelpfulnessPlugin](MACHOS/SiriInferredHelpfulnessPlugin.md)
- [/System/Library/PrivateFrameworks/SiriInvocationAnalytics.framework/PlugIns/SiriInvocationAnalyticsPlugin.appex/SiriInvocationAnalyticsPlugin](MACHOS/SiriInvocationAnalyticsPlugin.md)
- [/System/Library/PrivateFrameworks/SiriInvocationAnalytics.framework/PlugIns/THKOnDemandPlugin.appex/THKOnDemandPlugin](MACHOS/THKOnDemandPlugin.md)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningAnalytics.framework/PlugIns/SiriUserFeedbackLearningPlatformPlugin.appex/SiriUserFeedbackLearningPlatformPlugin](MACHOS/SiriUserFeedbackLearningPlatformPlugin.md)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningAnalytics.framework/PlugIns/SiriUserFeedbackLearningUniversalSuggestionsPlugin.appex/SiriUserFeedbackLearningUniversalSuggestionsPlugin](MACHOS/SiriUserFeedbackLearningUniversalSuggestionsPlugin.md)
- [/System/Library/PrivateFrameworks/SiriSettingsIntents.framework/PlugIns/SettingsIntentExtension.appex/SettingsIntentExtension](MACHOS/SettingsIntentExtension.md)
- [/System/Library/PrivateFrameworks/SiriSignals.framework/PlugIns/MusicAppSelectionPFLPlugin.appex/MusicAppSelectionPFLPlugin](MACHOS/MusicAppSelectionPFLPlugin.md)
- [/System/Library/PrivateFrameworks/SiriTTSService.framework/XPCServices/com.apple.SiriTTSService.TrialProxy.xpc/com.apple.SiriTTSService.TrialProxy](MACHOS/com.apple.SiriTTSService.TrialProxy.md)
- [/System/Library/PrivateFrameworks/SiriTTSService.framework/sirittsd](MACHOS/sirittsd.md)
- [/System/Library/PrivateFrameworks/SiriTTSTraining.framework/SiriTTSTraining](MACHOS/SiriTTSTraining.md)
- [/System/Library/PrivateFrameworks/SiriTTSTraining.framework/SiriTTSTrainingAgent](MACHOS/SiriTTSTrainingAgent.md)
- [/System/Library/PrivateFrameworks/SiriTasksEvaluation.framework/PlugIns/SiriTasksEvaluationPlugin.appex/SiriTasksEvaluationPlugin](MACHOS/SiriTasksEvaluationPlugin.md)
- [/System/Library/PrivateFrameworks/SiriTimeInternal.framework/PlugIns/AlarmIntentsExtension.appex/AlarmIntentsExtension](MACHOS/AlarmIntentsExtension.md)
- [/System/Library/PrivateFrameworks/SiriTimeInternal.framework/PlugIns/TimerIntentsExtension.appex/TimerIntentsExtension](MACHOS/TimerIntentsExtension.md)
- [/System/Library/PrivateFrameworks/SiriVOX.framework/SiriHeadlessService](MACHOS/SiriHeadlessService.md)
- [/System/Library/PrivateFrameworks/SiriVideoIntents.framework/PlugIns/VideoIntentExtension.appex/VideoIntentExtension](MACHOS/VideoIntentExtension.md)
- [/System/Library/PrivateFrameworks/SleepDaemon.framework/sleepd](MACHOS/sleepd.md)
- [/System/Library/PrivateFrameworks/SleepHealthUI.framework/PlugIns/SleepNotificationContentExtension.appex/SleepNotificationContentExtension](MACHOS/SleepNotificationContentExtension.md)
- [/System/Library/PrivateFrameworks/SlideshowKit.framework/PlugIns/OpusMagazineProducer.opplugin/OpusMagazineProducer](MACHOS/OpusMagazineProducer.md)
- [/System/Library/PrivateFrameworks/SlideshowKit.framework/PlugIns/OpusNewClassicProducer.opplugin/OpusNewClassicProducer](MACHOS/OpusNewClassicProducer.md)
- [/System/Library/PrivateFrameworks/SlideshowKit.framework/PlugIns/OpusOrigamiProducer.opplugin/OpusOrigamiProducer](MACHOS/OpusOrigamiProducer.md)
- [/System/Library/PrivateFrameworks/SmartReplies.framework/PlugIns/SmartRepliesMLRuntimePlugin.appex/SmartRepliesMLRuntimePlugin](MACHOS/SmartRepliesMLRuntimePlugin.md)
- [/System/Library/PrivateFrameworks/SocialLayer.framework/sociallayerd.app/sociallayerd](MACHOS/sociallayerd.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateBridge.framework/Support/subridged](MACHOS/subridged.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/PlugIns/SUFollowUpRollbackDetectedExtension.appex/SUFollowUpRollbackDetectedExtension](MACHOS/SUFollowUpRollbackDetectedExtension.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/PlugIns/SUSFollowUpExtension.appex/SUSFollowUpExtension](MACHOS/SUSFollowUpExtension.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/Support/softwareupdateservicesd](MACHOS/softwareupdateservicesd.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateServicesUI.framework/Plugins/SoftwareUpdateServicesUIPlugin.servicebundle/SoftwareUpdateServicesUIPlugin](MACHOS/SoftwareUpdateServicesUIPlugin.md)
- [/System/Library/PrivateFrameworks/SoundDetectionNotificationExtension.appex/SoundDetectionNotificationExtension](MACHOS/SoundDetectionNotificationExtension.md)
- [/System/Library/PrivateFrameworks/SoundScapesUtility.framework/PlugIns/SoundScapesViewServices.appex/SoundScapesViewServices](MACHOS/SoundScapesViewServices.md)
- [/System/Library/PrivateFrameworks/SpaceAttribution.framework/spaceattributiond](MACHOS/spaceattributiond.md)
- [/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/XPCServices/com.apple.SpeechRecognitionCore.brokerd.xpc/XPCServices/com.apple.SpeechRecognitionCore.speechrecognitiond.xpc/com.apple.SpeechRecognitionCore.speechrecognitiond](MACHOS/com.apple.SpeechRecognitionCore.speechrecognitiond.md)
- [/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/XPCServices/com.apple.SpeechRecognitionCore.brokerd.xpc/com.apple.SpeechRecognitionCore.brokerd](MACHOS/com.apple.SpeechRecognitionCore.brokerd.md)
- [/System/Library/PrivateFrameworks/StatusKit.framework/StatusKitAgent](MACHOS/StatusKitAgent.md)
- [/System/Library/PrivateFrameworks/Stickers.framework/Support/stickersd](MACHOS/stickersd.md)
- [/System/Library/PrivateFrameworks/StorageKit.framework/XPCServices/storagekitfsrunner.xpc/storagekitfsrunner](MACHOS/storagekitfsrunner.md)
- [/System/Library/PrivateFrameworks/StoreBookkeeperClient.framework/Support/storebookkeeperd](MACHOS/storebookkeeperd.md)
- [/System/Library/PrivateFrameworks/StreamingExtractor.framework/XPCServices/STExtractionService.privileged.xpc/STExtractionService.privileged](MACHOS/STExtractionService.privileged.md)
- [/System/Library/PrivateFrameworks/StreamingExtractor.framework/XPCServices/STExtractionService.xpc/STExtractionService](MACHOS/STExtractionService.md)
- [/System/Library/PrivateFrameworks/StreamingZip.framework/XPCServices/com.apple.StreamingUnzipService.privileged.xpc/com.apple.StreamingUnzipService.privileged](MACHOS/com.apple.StreamingUnzipService.privileged.md)
- [/System/Library/PrivateFrameworks/StreamingZip.framework/XPCServices/com.apple.StreamingUnzipService.xpc/com.apple.StreamingUnzipService](MACHOS/com.apple.StreamingUnzipService.md)
- [/System/Library/PrivateFrameworks/Synapse.framework/Support/contentlinkingd](MACHOS/contentlinkingd.md)
- [/System/Library/PrivateFrameworks/SyncedDefaults.framework/Support/syncdefaultsd](MACHOS/syncdefaultsd.md)
- [/System/Library/PrivateFrameworks/SystemStatusServer.framework/Support/systemstatusd](MACHOS/systemstatusd.md)
- [/System/Library/PrivateFrameworks/TCC.framework/Support/tccd](MACHOS/tccd.md)
- [/System/Library/PrivateFrameworks/TailspinSymbolication.framework/XPCServices/TailspinSymbolicationServer.xpc/TailspinSymbolicationServer](MACHOS/TailspinSymbolicationServer.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/PlugIns/PhoneIntentHandler.appex/PhoneIntentHandler](MACHOS/PhoneIntentHandler.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/XPCServices/com.apple.FTLivePhotoService.xpc/com.apple.FTLivePhotoService](MACHOS/com.apple.FTLivePhotoService.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/XPCServices/com.apple.FaceTime.FTConversationService.xpc/com.apple.FaceTime.FTConversationService](MACHOS/com.apple.FaceTime.FTConversationService.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd](MACHOS/callservicesd.md)
- [/System/Library/PrivateFrameworks/TextInputTestingKit.framework/XPCServices/TextInputTestService.xpc/TextInputTestService](MACHOS/TextInputTestService.md)
- [/System/Library/PrivateFrameworks/TextToSpeech.framework/PlugIns/SiriAUSP.appex/SiriAUSP](MACHOS/SiriAUSP.md)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/PlugIns/KonaSynthesizer.appex/KonaSynthesizer](MACHOS/KonaSynthesizer.md)
- [/System/Library/PrivateFrameworks/TextToSpeechMauiSupport.framework/PlugIns/MauiAUSP.appex/MauiAUSP](MACHOS/MauiAUSP.md)
- [/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingSupport.framework/PlugIns/VoiceBankingDiagnostics.appex/VoiceBankingDiagnostics](MACHOS/VoiceBankingDiagnostics.md)
- [/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingSupport.framework/Support/voicebankingd](MACHOS/voicebankingd.md)
- [/System/Library/PrivateFrameworks/ToneLibrary.framework/XPCServices/com.apple.tonelibraryd.xpc/com.apple.tonelibraryd](MACHOS/com.apple.tonelibraryd.md)
- [/System/Library/PrivateFrameworks/TouchRemote.framework/Support/touchsetupd](MACHOS/touchsetupd.md)
- [/System/Library/PrivateFrameworks/Translation.framework/translationd](MACHOS/translationd.md)
- [/System/Library/PrivateFrameworks/TranslationUIServices.framework/PlugIns/TranslationUIService.appex/TranslationUIService](MACHOS/TranslationUIService.md)
- [/System/Library/PrivateFrameworks/TransparencyUI.framework/PlugIns/TransparencyFollowUpExtension.appex/TransparencyFollowUpExtension](MACHOS/TransparencyFollowUpExtension.md)
- [/System/Library/PrivateFrameworks/TrialServer.framework/XPCServices/TrialArchivingService.xpc/TrialArchivingService](MACHOS/TrialArchivingService.md)
- [/System/Library/PrivateFrameworks/UIFoundation.framework/XPCServices/com.apple.uifoundation-bundle-helper.xpc/com.apple.uifoundation-bundle-helper](MACHOS/com.apple.uifoundation-bundle-helper.md)
- [/System/Library/PrivateFrameworks/UIFoundation.framework/XPCServices/nsattributedstringagent.xpc/nsattributedstringagent](MACHOS/nsattributedstringagent.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/Artwork.bundle/Artwork](MACHOS/Artwork.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/BoundingPathData.bundle/BoundingPathData](MACHOS/BoundingPathData.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/CarPlayArtwork.bundle/CarPlayArtwork](MACHOS/CarPlayArtwork.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/TextEffectsCatalog.bundle/TextEffectsCatalog](MACHOS/TextEffectsCatalog.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/XPCServices/SecureControlService.xpc/SecureControlService](MACHOS/SecureControlService.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/XPCServices/com.apple.UIKit.KeyboardManagement.xpc/com.apple.UIKit.KeyboardManagement](MACHOS/com.apple.UIKit.KeyboardManagement.md)
- [/System/Library/PrivateFrameworks/UIUnderstanding.framework/PlugIns/UIUnderstanding.diagnosticextension.appex/UIUnderstanding.diagnosticextension](MACHOS/UIUnderstanding.diagnosticextension.md)
- [/System/Library/PrivateFrameworks/USDLib_FormatLoaderProxy.framework/XPCServices/USDLib_FormatLoader.xpc/USDLib_FormatLoader](MACHOS/USDLib_FormatLoader.md)
- [/System/Library/PrivateFrameworks/UVFSXPCService.framework/XPCServices/UVFSService.xpc/UVFSService](MACHOS/UVFSService.md)
- [/System/Library/PrivateFrameworks/UnityPoster.framework/PlugIns/UnityPosterExtension.appex/UnityPosterExtension](MACHOS/UnityPosterExtension.md)
- [/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTrackingAgent](MACHOS/UsageTrackingAgent.md)
- [/System/Library/PrivateFrameworks/UserActivity.framework/Agents/useractivityd](MACHOS/useractivityd.md)
- [/System/Library/PrivateFrameworks/UserActivity.framework/PlugIns/UASharedPasteboardiOSUI.appex/UASharedPasteboardiOSUI](MACHOS/UASharedPasteboardiOSUI.md)
- [/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/userfs_provider.appex/userfs_provider](MACHOS/userfs_provider.md)
- [/System/Library/PrivateFrameworks/UserFS.framework/userfs_helper](MACHOS/userfs_helper.md)
- [/System/Library/PrivateFrameworks/UserFS.framework/userfsd](MACHOS/userfsd.md)
- [/System/Library/PrivateFrameworks/UserNotificationsCore.framework/Support/usernotificationsd](MACHOS/usernotificationsd.md)
- [/System/Library/PrivateFrameworks/UserNotificationsUIKit.framework/PlugIns/UserNotificationsUIDefaultExtension.appex/UserNotificationsUIDefaultExtension](MACHOS/UserNotificationsUIDefaultExtension.md)
- [/System/Library/PrivateFrameworks/UserNotificationsUIKit.framework/PlugIns/UserNotificationsUIThumbnailProvider.appex/UserNotificationsUIThumbnailProvider](MACHOS/UserNotificationsUIThumbnailProvider.md)
- [/System/Library/PrivateFrameworks/VectorKit.framework/mapinspectord](MACHOS/mapinspectord.md)
- [/System/Library/PrivateFrameworks/VideoSubscriberAccountUI.framework/PlugIns/VideoSubscriberAccountAuthenticationExtension.appex/VideoSubscriberAccountAuthenticationExtension](MACHOS/VideoSubscriberAccountAuthenticationExtension.md)
- [/System/Library/PrivateFrameworks/VisualTestKit.framework/VisualTestKit](MACHOS/VisualTestKit.md)
- [/System/Library/PrivateFrameworks/VisualVoicemail.framework/vmd](MACHOS/vmd.md)
- [/System/Library/PrivateFrameworks/VoiceMemos.framework/Support/voicememod](MACHOS/voicememod.md)
- [/System/Library/PrivateFrameworks/VoiceServices.framework/PlugIns/VoiceServicesDiagnosticextension.appex/VoiceServicesDiagnosticextension](MACHOS/VoiceServicesDiagnosticextension.md)
- [/System/Library/PrivateFrameworks/VoiceServices.framework/Support/voiced](MACHOS/voiced.md)
- [/System/Library/PrivateFrameworks/VoiceShortcuts.framework/Support/siriactionsd](MACHOS/siriactionsd.md)
- [/System/Library/PrivateFrameworks/WallpaperKit.framework/PlugIns/CollectionsPoster.appex/CollectionsPoster](MACHOS/CollectionsPoster.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/ExtragalacticPoster.appex/ExtragalacticPoster](MACHOS/ExtragalacticPoster.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/KaleidoscopePoster.appex/KaleidoscopePoster](MACHOS/KaleidoscopePoster.md)
- [/System/Library/PrivateFrameworks/WatchListKit.framework/Support/watchlistd](MACHOS/watchlistd.md)
- [/System/Library/PrivateFrameworks/Weather.framework/Support/nanoweatherprefsd](MACHOS/nanoweatherprefsd.md)
- [/System/Library/PrivateFrameworks/WeatherDaemon.framework/weatherd](MACHOS/weatherd.md)
- [/System/Library/PrivateFrameworks/WebPrivacy.framework/webprivacyd](MACHOS/webprivacyd.md)
- [/System/Library/PrivateFrameworks/WelcomeKit.framework/matd](MACHOS/matd.md)
- [/System/Library/PrivateFrameworks/WiFiKit.framework/PlugIns/WiFiPickerExtension.appex/WiFiPickerExtension](MACHOS/WiFiPickerExtension.md)
- [/System/Library/PrivateFrameworks/WiFiPolicy.framework/XPCServices/ThreeBarsXPCService.xpc/ThreeBarsXPCService](MACHOS/ThreeBarsXPCService.md)
- [/System/Library/PrivateFrameworks/WiFiPolicy.framework/XPCServices/WiFiCloudAssetsXPCService.xpc/WiFiCloudAssetsXPCService](MACHOS/WiFiCloudAssetsXPCService.md)
- [/System/Library/PrivateFrameworks/WirelessDiagnostics.framework/PlugIns/AWDDiagnosticExtension.appex/AWDDiagnosticExtension](MACHOS/AWDDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/WirelessInsights.framework/Support/wirelessinsightsd](MACHOS/wirelessinsightsd.md)
- [/System/Library/PrivateFrameworks/WorkflowKit.framework/PlugIns/ShortcutsIntents.appex/ShortcutsIntents](MACHOS/ShortcutsIntents.md)
- [/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/BackgroundShortcutRunner.xpc/BackgroundShortcutRunner](MACHOS/BackgroundShortcutRunner.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/AddShortcutExtension.appex/AddShortcutExtension](MACHOS/AddShortcutExtension.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/CatalystContentExtension.appex/CatalystContentExtension](MACHOS/CatalystContentExtension.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/FocusConfigurationExtension.appex/FocusConfigurationExtension](MACHOS/FocusConfigurationExtension.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/StaccatoConfigurationExtension.appex/StaccatoConfigurationExtension](MACHOS/StaccatoConfigurationExtension.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/WidgetConfigurationExtension.appex/WidgetConfigurationExtension](MACHOS/WidgetConfigurationExtension.md)
- [/System/Library/PrivateFrameworks/WorkoutKitServices.framework/XPCServices/WorkoutKitXPCService.xpc/WorkoutKitXPCService](MACHOS/WorkoutKitXPCService.md)
- [/System/Library/PrivateFrameworks/ZhuGeSupport.framework/XPCServices/ZhuGeService.xpc/ZhuGeService](MACHOS/ZhuGeService.md)
- [/System/Library/PrivateFrameworks/iCloudDriveService.framework/XPCServices/Ciconia.xpc/Ciconia](MACHOS/Ciconia.md)
- [/System/Library/PrivateFrameworks/iCloudDriveService.framework/XPCServices/ContainerMetadataExtractor.xpc/ContainerMetadataExtractor](MACHOS/ContainerMetadataExtractor.md)
- [/System/Library/PrivateFrameworks/iCloudDriveService.framework/XPCServices/TelemetryDiskChecker.xpc/TelemetryDiskChecker](MACHOS/TelemetryDiskChecker.md)
- [/System/Library/PrivateFrameworks/iCloudNotification.framework/ind](MACHOS/ind.md)
- [/System/Library/PrivateFrameworks/iCloudQuota.framework/PlugIns/ICQFollowup.appex/ICQFollowup](MACHOS/ICQFollowup.md)
- [/System/Library/PrivateFrameworks/iCloudQuotaUI.framework/Extensions/RemoteiCloudQuotaUI.appex/RemoteiCloudQuotaUI](MACHOS/RemoteiCloudQuotaUI.md)
- [/System/Library/PrivateFrameworks/iCloudQuotaUI.framework/PlugIns/ICQEngagementExtension.appex/ICQEngagementExtension](MACHOS/ICQEngagementExtension.md)
- [/System/Library/PrivateFrameworks/iCloudSubscriptionOptimizerCore.framework/PlugIns/PFLPlugin.appex/PFLPlugin](MACHOS/PFLPlugin.md)
- [/System/Library/PrivateFrameworks/iCloudSubscriptionOptimizerDaemon.framework/icloudsubscriptionoptimizerd/icloudsubscriptionoptimizerd](MACHOS/icloudsubscriptionoptimizerd.md)
- [/System/Library/PrivateFrameworks/iCloudSubscriptionOptimizerLighthouse.framework/PlugIns/LighthousePlugin.appex/LighthousePlugin](MACHOS/LighthousePlugin.md)
- [/System/Library/PrivateFrameworks/iOSDiagnostics.framework/XPCServices/com.apple.DiagnosticsSessionAvailibility.xpc/com.apple.DiagnosticsSessionAvailibility](MACHOS/com.apple.DiagnosticsSessionAvailibility.md)
- [/System/Library/PrivateFrameworks/iOSDiagnostics.framework/iosdiagnosticsd](MACHOS/iosdiagnosticsd.md)
- [/System/Library/PrivateFrameworks/iTunesCloud.framework/Support/itunescloudd](MACHOS/itunescloudd.md)
- [/System/Library/PrivateFrameworks/iTunesCloud.framework/XPCServices/SharedListeningConnectionService.xpc/SharedListeningConnectionService](MACHOS/SharedListeningConnectionService.md)
- [/System/Library/PrivateFrameworks/iTunesStore.framework/Support/itunesstored](MACHOS/itunesstored.md)
- [/System/Library/PrivateFrameworks/iTunesStoreUI.framework/PlugIns/SUAskPermissionExtension.appex/SUAskPermissionExtension](MACHOS/SUAskPermissionExtension.md)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/iWorkImport](MACHOS/iWorkImport.md)
- [/System/Library/PrivateFrameworks/iWorkXPC.framework/XPCServices/iWorkFileFormat.xpc/iWorkFileFormat](MACHOS/iWorkFileFormat.md)
- [/System/Library/Recents/Plugins/GenericAddressHandler.addresshandler/GenericAddressHandler](MACHOS/GenericAddressHandler.md)
- [/System/Library/Recents/Plugins/MapsRecents.addresshandler/MapsRecents](MACHOS/MapsRecents.md)
- [/System/Library/RelevanceEngine/NanoDataSources/BreatheRelevanceEngineDataSource.bundle/BreatheRelevanceEngineDataSource](MACHOS/BreatheRelevanceEngineDataSource.md)
- [/System/Library/RelevanceEngine/NanoDataSources/MindRelevanceEngineDataSource.bundle/MindRelevanceEngineDataSource](MACHOS/MindRelevanceEngineDataSource.md)
- [/System/Library/RelevanceEngine/NanoDataSources/NanoAlarmCompanionDataSource.bundle/NanoAlarmCompanionDataSource](MACHOS/NanoAlarmCompanionDataSource.md)
- [/System/Library/RelevanceEngine/NanoDataSources/NanoBedtimeCompanionDataSource.bundle/NanoBedtimeCompanionDataSource](MACHOS/NanoBedtimeCompanionDataSource.md)
- [/System/Library/RelevanceEngine/NanoDataSources/NanoMenstrualCyclesRelevanceEngineDataSource.bundle/NanoMenstrualCyclesRelevanceEngineDataSource](MACHOS/NanoMenstrualCyclesRelevanceEngineDataSource.md)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineActivityRings.bundle/RelevanceEngineActivityRings](MACHOS/RelevanceEngineActivityRings.md)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineActivityUpNext.bundle/RelevanceEngineActivityUpNext](MACHOS/RelevanceEngineActivityUpNext.md)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineAudiobooks.bundle/RelevanceEngineAudiobooks](MACHOS/RelevanceEngineAudiobooks.md)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineCalendar.bundle/RelevanceEngineCalendar](MACHOS/RelevanceEngineCalendar.md)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineHeart.bundle/RelevanceEngineHeart](MACHOS/RelevanceEngineHeart.md)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineMusic.bundle/RelevanceEngineMusic](MACHOS/RelevanceEngineMusic.md)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineNowPlaying.bundle/RelevanceEngineNowPlaying](MACHOS/RelevanceEngineNowPlaying.md)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEnginePodcasts.bundle/RelevanceEnginePodcasts](MACHOS/RelevanceEnginePodcasts.md)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineReminders.bundle/RelevanceEngineReminders](MACHOS/RelevanceEngineReminders.md)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineSiriSnippets.bundle/RelevanceEngineSiriSnippets](MACHOS/RelevanceEngineSiriSnippets.md)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineSports.bundle/RelevanceEngineSports](MACHOS/RelevanceEngineSports.md)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineStopwatch.bundle/RelevanceEngineStopwatch](MACHOS/RelevanceEngineStopwatch.md)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineTimer.bundle/RelevanceEngineTimer](MACHOS/RelevanceEngineTimer.md)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineWallet.bundle/RelevanceEngineWallet](MACHOS/RelevanceEngineWallet.md)
- [/System/Library/RelevanceEngine/NanoDataSources/ShortcutsRelevanceEngineDataSource.bundle/ShortcutsRelevanceEngineDataSource](MACHOS/ShortcutsRelevanceEngineDataSource.md)
- [/System/Library/ScreenReader/BrailleDrivers/Alva6Series.brailledriver/Alva6Series](MACHOS/Alva6Series.md)
- [/System/Library/ScreenReader/BrailleDrivers/Baum.brailledriver/Baum](MACHOS/Baum.md)
- [/System/Library/ScreenReader/BrailleDrivers/BrailleNoteApex.brailledriver/BrailleNoteApex](MACHOS/BrailleNoteApex.md)
- [/System/Library/ScreenReader/BrailleDrivers/BrailleSense.brailledriver/BrailleSense](MACHOS/BrailleSense.md)
- [/System/Library/ScreenReader/BrailleDrivers/Brailliant 2 Driver.brailledriver/Brailliant 2 Driver](MACHOS/Brailliant_2_Driver.md)
- [/System/Library/ScreenReader/BrailleDrivers/DOT Driver.brailledriver/DOT Driver](MACHOS/DOT_Driver.md)
- [/System/Library/ScreenReader/BrailleDrivers/EasyLink.brailledriver/EasyLink](MACHOS/EasyLink.md)
- [/System/Library/ScreenReader/BrailleDrivers/Eurobraille.brailledriver/Eurobraille](MACHOS/Eurobraille.md)
- [/System/Library/ScreenReader/BrailleDrivers/FreedomScientific.brailledriver/FreedomScientific](MACHOS/FreedomScientific.md)
- [/System/Library/ScreenReader/BrailleDrivers/GenericHID.brailledriver/GenericHID](MACHOS/GenericHID.md)
- [/System/Library/ScreenReader/BrailleDrivers/HIMS Driver.brailledriver/HIMS Driver](MACHOS/HIMS_Driver.md)
- [/System/Library/ScreenReader/BrailleDrivers/HandyTech.brailledriver/HandyTech](MACHOS/HandyTech.md)
- [/System/Library/ScreenReader/BrailleDrivers/KGS Driver.brailledriver/KGS Driver](MACHOS/KGS_Driver.md)
- [/System/Library/ScreenReader/BrailleDrivers/MDV.brailledriver/MDV](MACHOS/MDV.md)
- [/System/Library/ScreenReader/BrailleDrivers/Ninepoint Systems Driver.brailledriver/Ninepoint Systems Driver](MACHOS/Ninepoint_Systems_Driver.md)
- [/System/Library/ScreenReader/BrailleDrivers/Papenmeier.brailledriver/Papenmeier](MACHOS/Papenmeier.md)
- [/System/Library/ScreenReader/BrailleDrivers/Seika.brailledriver/Seika](MACHOS/Seika.md)
- [/System/Library/ScreenReader/BrailleTables/AppleBrailleTranslator.brailletable/AppleBrailleTranslator](MACHOS/AppleBrailleTranslator.md)
- [/System/Library/ScreenReader/BrailleTables/BrailleNBSC.brailletable/BrailleNBSC](MACHOS/BrailleNBSC.md)
- [/System/Library/ScreenReader/BrailleTables/Duxbury.brailletable/Duxbury](MACHOS/Duxbury.md)
- [/System/Library/ScreenReader/BrailleTables/LiblouisBrailleTranslator.brailletable/LiblouisBrailleTranslator](MACHOS/LiblouisBrailleTranslator.md)
- [/System/Library/ScreenReader/BrailleTables/Rhine.brailletable/Rhine](MACHOS/Rhine.md)
- [/System/Library/SetupAssistantBundles/FaceTimeSetupAssistantBundle.bundle/FaceTimeSetupAssistantBundle](MACHOS/FaceTimeSetupAssistantBundle.md)
- [/System/Library/SetupAssistantBundles/GameCenterSetupAssistant.bundle/GameCenterSetupAssistant](MACHOS/GameCenterSetupAssistant.md)
- [/System/Library/SetupAssistantBundles/MadridSetupAssistantBundle.bundle/MadridSetupAssistantBundle](MACHOS/MadridSetupAssistantBundle.md)
- [/System/Library/SetupAssistantBundles/SBSyncServiceSetupAssistantBundle.bundle/SBSyncServiceSetupAssistantBundle](MACHOS/SBSyncServiceSetupAssistantBundle.md)
- [/System/Library/SetupAssistantBundles/iTunesStoreSetupAssistant.bundle/iTunesStoreSetupAssistant](MACHOS/iTunesStoreSetupAssistant.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/AppLaunchSuggestionsPlugin.bundle/AppLaunchSuggestionsPlugin](MACHOS/AppLaunchSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/AudioSuggestionsPlugin.bundle/AudioSuggestionsPlugin](MACHOS/AudioSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/CalendarSuggestions.bundle/CalendarSuggestions](MACHOS/CalendarSuggestions.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/HomeAutomationSiriSuggestions.bundle/HomeAutomationSiriSuggestions](MACHOS/HomeAutomationSiriSuggestions.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/PhoneSuggestions.bundle/PhoneSuggestions](MACHOS/PhoneSuggestions.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/PlaybackControlsSuggestionsPlugin.bundle/PlaybackControlsSuggestionsPlugin](MACHOS/PlaybackControlsSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriGeoSuggestions.bundle/SiriGeoSuggestions](MACHOS/SiriGeoSuggestions.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriInformationSuggestionsPlugin.bundle/SiriInformationSuggestionsPlugin](MACHOS/SiriInformationSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriLinkSuggestionsPlugin.bundle/SiriLinkSuggestionsPlugin](MACHOS/SiriLinkSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriMessagesSuggestions.bundle/SiriMessagesSuggestions](MACHOS/SiriMessagesSuggestions.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriNotebookSuggestionsPlugin.bundle/SiriNotebookSuggestionsPlugin](MACHOS/SiriNotebookSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriSettingsSuggestionsPlugin.bundle/SiriSettingsSuggestionsPlugin](MACHOS/SiriSettingsSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriSocialConversationSuggestionsPlugin.bundle/SiriSocialConversationSuggestionsPlugin](MACHOS/SiriSocialConversationSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriTimeSuggestionsPlugin.bundle/SiriTimeSuggestionsPlugin](MACHOS/SiriTimeSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SystemCommandsSuggestionsPlugin.bundle/SystemCommandsSuggestionsPlugin](MACHOS/SystemCommandsSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/VideoSuggestionsPlugin.bundle/VideoSuggestionsPlugin](MACHOS/VideoSuggestionsPlugin.md)
- [/System/Library/Snippets/UIPlugins/AudioUIPlugin.bundle/AudioUIPlugin](MACHOS/AudioUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/CalendarUIPlugin.bundle/CalendarUIPlugin](MACHOS/CalendarUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/CarCommandsUIPlugin.bundle/CarCommandsUIPlugin](MACHOS/CarCommandsUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/FindMyUIPlugin.bundle/FindMyUIPlugin](MACHOS/FindMyUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/HomeCommunicationUIPlugin.bundle/HomeCommunicationUIPlugin](MACHOS/HomeCommunicationUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/MessagesUIPlugin.bundle/MessagesUIPlugin](MACHOS/MessagesUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/PhoneUIPlugin.bundle/PhoneUIPlugin](MACHOS/PhoneUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SettingsCustomPlugin.bundle/SettingsCustomPlugin](MACHOS/SettingsCustomPlugin.md)
- [/System/Library/Snippets/UIPlugins/ShazamUIPlugin.bundle/ShazamUIPlugin](MACHOS/ShazamUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SiriExpanseInternalUIPlugin.bundle/SiriExpanseInternalUIPlugin](MACHOS/SiriExpanseInternalUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SiriInferenceFlowsUIPlugin.bundle/SiriInferenceFlowsUIPlugin](MACHOS/SiriInferenceFlowsUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SiriLinkUIPlugin.bundle/SiriLinkUIPlugin](MACHOS/SiriLinkUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SiriMailUIPlugin.bundle/SiriMailUIPlugin](MACHOS/SiriMailUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SiriSocialConversationUIPlugin.bundle/SiriSocialConversationUIPlugin](MACHOS/SiriSocialConversationUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SiriSuggestionsUIPlugin.bundle/SiriSuggestionsUIPlugin](MACHOS/SiriSuggestionsUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SiriVideoUIPlugin.bundle/SiriVideoUIPlugin](MACHOS/SiriVideoUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SystemPlugin.bundle/SystemPlugin](MACHOS/SystemPlugin.md)
- [/System/Library/Snippets/UIPlugins/TimerUIPlugin.bundle/TimerUIPlugin](MACHOS/TimerUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/WellnessUIPlugin.bundle/WellnessUIPlugin](MACHOS/WellnessUIPlugin.md)
- [/System/Library/SpringBoardPlugins/FindMyiPhoneLockScreen.lockbundle/FindMyiPhoneLockScreen](MACHOS/FindMyiPhoneLockScreen.md)
- [/System/Library/SpringBoardPlugins/PassesLockScreenPlugin.lockbundle/PassesLockScreenPlugin](MACHOS/PassesLockScreenPlugin.md)
- [/System/Library/SpringBoardPlugins/StoreDemoPlugin.servicebundle/StoreDemoPlugin](MACHOS/StoreDemoPlugin.md)
- [/System/Library/SpringBoardPlugins/ZoomTouch.bundle/ZoomTouch](MACHOS/ZoomTouch.md)
- [/System/Library/StreamingExtractorPlugins/STAEAExtractionPlugin.bundle/STAEAExtractionPlugin](MACHOS/STAEAExtractionPlugin.md)
- [/System/Library/SyncBundles/AirFair.syncBundle/AirFair](MACHOS/AirFair.md)
- [/System/Library/SyncBundles/AirFair2.syncBundle/AirFair2](MACHOS/AirFair2.md)
- [/System/Library/SyncBundles/Apps.syncBundle/Apps](MACHOS/Apps.md)
- [/System/Library/SyncBundles/Books.syncBundle/Books](MACHOS/Books.md)
- [/System/Library/SyncBundles/LogsPlugin.syncBundle/LogsPlugin](MACHOS/LogsPlugin.md)
- [/System/Library/SyncBundles/MBATCPlugin.syncBundle/MBATCPlugin](MACHOS/MBATCPlugin.md)
- [/System/Library/SyncBundles/MobileSlideShow.syncBundle/MobileSlideShow](MACHOS/MobileSlideShow.md)
- [/System/Library/SyncBundles/MusicLibrary.syncBundle/MusicLibrary](MACHOS/MusicLibrary.md)
- [/System/Library/SyncBundles/Podcasts.syncBundle/Podcasts](MACHOS/Podcasts.md)
- [/System/Library/SyncBundles/ProofingPlugin.syncBundle/ProofingPlugin](MACHOS/ProofingPlugin.md)
- [/System/Library/SyncBundles/SMS.syncBundle/SMS](MACHOS/SMS.md)
- [/System/Library/SyncBundles/Tones.syncBundle/Tones](MACHOS/Tones.md)
- [/System/Library/SyncBundles/UserDataPlugin.syncBundle/UserDataPlugin](MACHOS/UserDataPlugin.md)
- [/System/Library/SystemConfiguration/EAPOLController.bundle/EAPOLController](MACHOS/EAPOLController.md)
- [/System/Library/SystemConfiguration/EAPOLController.bundle/eapolclient](MACHOS/eapolclient.md)
- [/System/Library/SystemConfiguration/IPConfiguration.bundle/IPConfiguration](MACHOS/IPConfiguration.md)
- [/System/Library/SystemConfiguration/PPPController.bundle/PPPController](MACHOS/PPPController.md)
- [/System/Library/SystemConfiguration/PPPController.bundle/PlugIns/L2TP.ppp/L2TP](MACHOS/L2TP.md)
- [/System/Library/SystemConfiguration/PPPController.bundle/PlugIns/PPPDialogs.ppp/PPPDialogs](MACHOS/PPPDialogs.md)
- [/System/Library/SystemConfiguration/USBDeviceConfiguration.bundle/USBDeviceConfiguration](MACHOS/USBDeviceConfiguration.md)
- [/System/Library/TextInput/Plugins/MessagesDataKeyboardPlugin.bundle/MessagesDataKeyboardPlugin](MACHOS/MessagesDataKeyboardPlugin.md)
- [/System/Library/TextInput/kbd](MACHOS/kbd.md)
- [/System/Library/Trace/Providers/Logging.bundle/Logging](MACHOS/Logging.md)
- [/System/Library/Trace/Providers/Required.bundle/Required](MACHOS/Required.md)
- [/System/Library/Trace/Providers/Symbolication.bundle/Symbolication](MACHOS/Symbolication.md)
- [/System/Library/Trace/Providers/TrialProvider.bundle/TrialProvider](MACHOS/TrialProvider.md)
- [/System/Library/UsageBundles/CalendarUsage.bundle/CalendarUsage](MACHOS/CalendarUsage.md)
- [/System/Library/UsageBundles/ContactsUsage.bundle/ContactsUsage](MACHOS/ContactsUsage.md)
- [/System/Library/UsageBundles/MailUsage.bundle/MailUsage](MACHOS/MailUsage.md)
- [/System/Library/UsageBundles/MessagesUsagePreferencesPlugin.bundle/MessagesUsagePreferencesPlugin](MACHOS/MessagesUsagePreferencesPlugin.md)
- [/System/Library/UsageBundles/MusicUsage.bundle/MusicUsage](MACHOS/MusicUsage.md)
- [/System/Library/UsageBundles/NanoBackupUsage.bundle/NanoBackupUsage](MACHOS/NanoBackupUsage.md)
- [/System/Library/UsageBundles/PassbookUsageBundle.bundle/PassbookUsageBundle](MACHOS/PassbookUsageBundle.md)
- [/System/Library/UsageBundles/SafariUsageBundle.bundle/SafariUsageBundle](MACHOS/SafariUsageBundle.md)
- [/System/Library/UsageBundles/SoftwareUpdateUsage.bundle/SoftwareUpdateUsage](MACHOS/SoftwareUpdateUsage.md)
- [/System/Library/UsageBundles/ToneSettingsUsage.bundle/ToneSettingsUsage](MACHOS/ToneSettingsUsage.md)
- [/System/Library/UsageBundles/VideosUsage.bundle/VideosUsage](MACHOS/VideosUsage.md)
- [/System/Library/UsageBundles/VisualVoicemailUsage.bundle/VisualVoicemailUsage](MACHOS/VisualVoicemailUsage.md)
- [/System/Library/UserEventPlugins/ADEventListenerPlugin.plugin/ADEventListenerPlugin](MACHOS/ADEventListenerPlugin.md)
- [/System/Library/UserEventPlugins/AHTUserEventAgent.plugin/AHTUserEventAgent](MACHOS/AHTUserEventAgent.md)
- [/System/Library/UserEventPlugins/BonjourEvents.plugin/BonjourEvents](MACHOS/BonjourEvents.md)
- [/System/Library/UserEventPlugins/GreenTeaUserEventAgent.plugin/GreenTeaUserEventAgent](MACHOS/GreenTeaUserEventAgent.md)
- [/System/Library/UserEventPlugins/ManagedConfigurationUEA.plugin/ManagedConfigurationUEA](MACHOS/ManagedConfigurationUEA.md)
- [/System/Library/UserEventPlugins/MemoryMonitor.plugin/MemoryMonitor](MACHOS/MemoryMonitor.md)
- [/System/Library/UserEventPlugins/MobileBackupUEA.plugin/MobileBackupUEA](MACHOS/MobileBackupUEA.md)
- [/System/Library/UserEventPlugins/MobileGestaltEvents.plugin/MobileGestaltEvents](MACHOS/MobileGestaltEvents.md)
- [/System/Library/UserEventPlugins/MobileKeyBagLockState.plugin/MobileKeyBagLockState](MACHOS/MobileKeyBagLockState.md)
- [/System/Library/UserEventPlugins/PerfPowerServicesEventListenerPlugin.plugin/PerfPowerServicesEventListenerPlugin](MACHOS/PerfPowerServicesEventListenerPlugin.md)
- [/System/Library/UserEventPlugins/USBEthernetSharing.plugin/USBEthernetSharing](MACHOS/USBEthernetSharing.md)
- [/System/Library/UserEventPlugins/com.apple.AppleKeyStoreEvents.plugin/com.apple.AppleKeyStoreEvents](MACHOS/com.apple.AppleKeyStoreEvents.md)
- [/System/Library/UserEventPlugins/com.apple.BackgroundTaskAgentPlugin.plugin/com.apple.BackgroundTaskAgentPlugin](MACHOS/com.apple.BackgroundTaskAgentPlugin.md)
- [/System/Library/UserEventPlugins/com.apple.ExternalAccessory.matching.plugin/com.apple.ExternalAccessory.matching](MACHOS/com.apple.ExternalAccessory.matching.md)
- [/System/Library/UserEventPlugins/com.apple.accessoryd.matching.plugin/com.apple.accessoryd.matching](MACHOS/com.apple.accessoryd.matching.md)
- [/System/Library/UserEventPlugins/com.apple.alarm.plugin/com.apple.alarm](MACHOS/com.apple.alarm.md)
- [/System/Library/UserEventPlugins/com.apple.bonjour.plugin/com.apple.bonjour](MACHOS/com.apple.bonjour.md)
- [/System/Library/UserEventPlugins/com.apple.cfnotification.plugin/com.apple.cfnotification](MACHOS/com.apple.cfnotification.md)
- [/System/Library/UserEventPlugins/com.apple.cts.plugin/com.apple.cts](MACHOS/com.apple.cts.md)
- [/System/Library/UserEventPlugins/com.apple.dispatch.vfs.plugin/com.apple.dispatch.vfs](MACHOS/com.apple.dispatch.vfs.md)
- [/System/Library/UserEventPlugins/com.apple.fsevents.matching.plugin/com.apple.fsevents.matching](MACHOS/com.apple.fsevents.matching.md)
- [/System/Library/UserEventPlugins/com.apple.iokit.matching.plugin/com.apple.iokit.matching](MACHOS/com.apple.iokit.matching.md)
- [/System/Library/UserEventPlugins/com.apple.launchd.helper.plugin/com.apple.launchd.helper](MACHOS/com.apple.launchd.helper.md)
- [/System/Library/UserEventPlugins/com.apple.netsvcproxy.plugin/com.apple.netsvcproxy](MACHOS/com.apple.netsvcproxy.md)
- [/System/Library/UserEventPlugins/com.apple.networkextension.plugin/com.apple.networkextension](MACHOS/com.apple.networkextension.md)
- [/System/Library/UserEventPlugins/com.apple.nsurlsessiond.plugin/com.apple.nsurlsessiond](MACHOS/com.apple.nsurlsessiond.md)
- [/System/Library/UserEventPlugins/com.apple.rapport.events.plugin/com.apple.rapport.events](MACHOS/com.apple.rapport.events.md)
- [/System/Library/UserEventPlugins/com.apple.spd.plugin/com.apple.spd](MACHOS/com.apple.spd.md)
- [/System/Library/UserEventPlugins/com.apple.systemconfiguration.plugin/com.apple.systemconfiguration](MACHOS/com.apple.systemconfiguration.md)
- [/System/Library/UserEventPlugins/com.apple.tailspin.plugin/com.apple.tailspin](MACHOS/com.apple.tailspin.md)
- [/System/Library/UserEventPlugins/com.apple.telemetry.plugin/com.apple.telemetry](MACHOS/com.apple.telemetry.md)
- [/System/Library/UserEventPlugins/locationd.events.plugin/locationd.events](MACHOS/locationd.events.md)
- [/System/Library/UserEventPlugins/routined.events.plugin/routined.events](MACHOS/routined.events.md)
- [/System/Library/UserNotifications/Bundles/com.apple.ARQLNotifications.bundle/com.apple.ARQLNotifications](MACHOS/com.apple.ARQLNotifications.md)
- [/System/Library/UserNotifications/Bundles/com.apple.AppleMediaServicesUI.engagement.notifications.bundle/com.apple.AppleMediaServicesUI.engagement.notifications](MACHOS/com.apple.AppleMediaServicesUI.engagement.notifications.md)
- [/System/Library/UserNotifications/Bundles/com.apple.ClassKitProgressNotifications.bundle/com.apple.ClassKitProgressNotifications](MACHOS/com.apple.ClassKitProgressNotifications.md)
- [/System/Library/UserNotifications/Bundles/com.apple.NDO.FollowUp.bundle/com.apple.NDO.FollowUp](MACHOS/com.apple.NDO.FollowUp.md)
- [/System/Library/UserNotifications/Bundles/com.apple.PerformanceTrace.notifications.bundle/com.apple.PerformanceTrace.notifications](MACHOS/com.apple.PerformanceTrace.notifications.md)
- [/System/Library/UserNotifications/Bundles/com.apple.RTTNotifications.bundle/com.apple.RTTNotifications](MACHOS/com.apple.RTTNotifications.md)
- [/System/Library/UserNotifications/Bundles/com.apple.ReplayKitNotifications.bundle/com.apple.ReplayKitNotifications](MACHOS/com.apple.ReplayKitNotifications.md)
- [/System/Library/UserNotifications/Bundles/com.apple.ScreenTimeDowntimeNotifications.bundle/com.apple.ScreenTimeDowntimeNotifications](MACHOS/com.apple.ScreenTimeDowntimeNotifications.md)
- [/System/Library/UserNotifications/Bundles/com.apple.ScreenTimeEnabledNotifications.bundle/com.apple.ScreenTimeEnabledNotifications](MACHOS/com.apple.ScreenTimeEnabledNotifications.md)
- [/System/Library/UserNotifications/Bundles/com.apple.ScreenTimeNotifications.bundle/com.apple.ScreenTimeNotifications](MACHOS/com.apple.ScreenTimeNotifications.md)
- [/System/Library/UserNotifications/Bundles/com.apple.ShazamNotifications.bundle/com.apple.ShazamNotifications](MACHOS/com.apple.ShazamNotifications.md)
- [/System/Library/UserNotifications/Bundles/com.apple.Siri.ActionPredictionNotifications.bundle/com.apple.Siri.ActionPredictionNotifications](MACHOS/com.apple.Siri.ActionPredictionNotifications.md)
- [/System/Library/UserNotifications/Bundles/com.apple.SoundDetectionNotifications.bundle/com.apple.SoundDetectionNotifications](MACHOS/com.apple.SoundDetectionNotifications.md)
- [/System/Library/UserNotifications/Bundles/com.apple.UserNotifications.DeviceDiscoveryUIAgent.bundle/com.apple.UserNotifications.DeviceDiscoveryUIAgent](MACHOS/com.apple.UserNotifications.DeviceDiscoveryUIAgent.md)
- [/System/Library/UserNotifications/Bundles/com.apple.accountnotifications.bundle/com.apple.accountnotifications](MACHOS/com.apple.accountnotifications.md)
- [/System/Library/UserNotifications/Bundles/com.apple.commandandcontrol.bundle/com.apple.commandandcontrol](MACHOS/com.apple.commandandcontrol.md)
- [/System/Library/UserNotifications/Bundles/com.apple.donotdisturb.bundle/com.apple.donotdisturb](MACHOS/com.apple.donotdisturb.md)
- [/System/Library/UserNotifications/Bundles/com.apple.hangtracerd.usernotifications.bundle/com.apple.hangtracerd.usernotifications](MACHOS/com.apple.hangtracerd.usernotifications.md)
- [/System/Library/UserNotifications/Bundles/com.apple.iCloud.FollowUp.bundle/com.apple.iCloud.FollowUp](MACHOS/com.apple.iCloud.FollowUp.md)
- [/System/Library/UserNotifications/Bundles/com.apple.identityservicesd.firewall.bundle/com.apple.identityservicesd.firewall](MACHOS/com.apple.identityservicesd.firewall.md)
- [/System/Library/UserNotifications/Bundles/com.apple.powerlog.proactivenotifications.bundle/com.apple.powerlog.proactivenotifications](MACHOS/com.apple.powerlog.proactivenotifications.md)
- [/System/Library/UserNotifications/Bundles/com.apple.reminders.bundle/com.apple.reminders](MACHOS/com.apple.reminders.md)
- [/System/Library/UserNotifications/Bundles/com.apple.studentd.notifications.bundle/com.apple.studentd.notifications](MACHOS/com.apple.studentd.notifications.md)
- [/System/Library/UserNotifications/Bundles/com.apple.tailspin.notifications.bundle/com.apple.tailspin.notifications](MACHOS/com.apple.tailspin.notifications.md)
- [/System/Library/Video/Plug-Ins/AppleMCTF.bundle/AppleMCTF](MACHOS/AppleMCTF.md)
- [/System/Library/Video/Plug-Ins/AppleVideoEncoder.bundle/AppleVideoEncoder](MACHOS/AppleVideoEncoder.md)
- [/System/Library/VideoProcessors/CCPortrait.bundle/ccportrait_archive_bin.metallib](MACHOS/ccportrait_archive_bin.metallib.md)
- [/System/Library/VideoProcessors/SemanticStyleV1.bundle/SemanticStyleV1](MACHOS/SemanticStyleV1.md)
- [/System/Library/VideoProcessors/SuperResolutionV2.bundle/SuperResolutionV2](MACHOS/SuperResolutionV2.md)
- [/System/Library/VideoProcessors/VideoDeghostingV1.bundle/VideoDeghostingV1](MACHOS/VideoDeghostingV1.md)
- [/System/Library/VideoProcessors/VideoDeghostingV2.bundle/VideoDeghostingV2](MACHOS/VideoDeghostingV2.md)
- [/System/Library/VideoProcessors/VideoStabilizationV2.bundle/VideoStabilizationV2](MACHOS/VideoStabilizationV2.md)
- [/System/Library/VoiceServices/PlugIns/Base.vsplugin/Base](MACHOS/Base.md)
- [/bin/df](MACHOS/df.md)
- [/bin/ps](MACHOS/ps.md)
- [/private/var/staged_system_apps/AppleTV.app/AppleTV](MACHOS/AppleTV.md)
- [/private/var/staged_system_apps/AppleTV.app/PlugIns/TVCoreSpotlightExtension.appex/TVCoreSpotlightExtension](MACHOS/TVCoreSpotlightExtension.md)
- [/private/var/staged_system_apps/AppleTV.app/PlugIns/TVIntentsExtension.appex/TVIntentsExtension](MACHOS/TVIntentsExtension.md)
- [/private/var/staged_system_apps/AppleTV.app/PlugIns/TVNotificationContentExtension.appex/TVNotificationContentExtension](MACHOS/TVNotificationContentExtension.md)
- [/private/var/staged_system_apps/AppleTV.app/PlugIns/TVWidgetExtension.appex/TVWidgetExtension](MACHOS/TVWidgetExtension.md)
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
- [/private/var/staged_system_apps/Books.app/Frameworks/EngagementCollector.framework/EngagementCollector](MACHOS/EngagementCollector.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/JSApp.framework/JSApp](MACHOS/JSApp.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/TemplateUI.framework/TemplateUI](MACHOS/TemplateUI.md)
- [/private/var/staged_system_apps/Books.app/PlugIns/BookEPUBWebProcessPlugin.bundle/BookEPUBWebProcessPlugin](MACHOS/BookEPUBWebProcessPlugin.md)
- [/private/var/staged_system_apps/Books.app/PlugIns/BooksEngagementExtension.appex/BooksEngagementExtension](MACHOS/BooksEngagementExtension.md)
- [/private/var/staged_system_apps/Books.app/PlugIns/BooksIntentHandler.appex/BooksIntentHandler](MACHOS/BooksIntentHandler.md)
- [/private/var/staged_system_apps/Books.app/PlugIns/BooksNotificationContentExtension.appex/BooksNotificationContentExtension](MACHOS/BooksNotificationContentExtension.md)
- [/private/var/staged_system_apps/Books.app/PlugIns/BooksProductPageExtension.appex/BooksProductPageExtension](MACHOS/BooksProductPageExtension.md)
- [/private/var/staged_system_apps/Books.app/PlugIns/BooksThumbnail.appex/BooksThumbnail](MACHOS/BooksThumbnail.md)
- [/private/var/staged_system_apps/Books.app/PlugIns/BooksWidgetExtension.appex/BooksWidgetExtension](MACHOS/BooksWidgetExtension.md)
- [/private/var/staged_system_apps/Books.app/XPCServices/XPCUbiquityDisableService.xpc/XPCUbiquityDisableService](MACHOS/XPCUbiquityDisableService.md)
- [/private/var/staged_system_apps/Bridge.app/Bridge](MACHOS/Bridge.md)
- [/private/var/staged_system_apps/Bridge.app/PlugIns/GreenfieldThumbnailExtension.appex/GreenfieldThumbnailExtension](MACHOS/GreenfieldThumbnailExtension.md)
- [/private/var/staged_system_apps/Calculator.app/Calculator](MACHOS/Calculator.md)
- [/private/var/staged_system_apps/Compass.app/Compass](MACHOS/Compass.md)
- [/private/var/staged_system_apps/Contacts.app/Contacts](MACHOS/Contacts.md)
- [/private/var/staged_system_apps/FaceTime.app/FaceTime](MACHOS/FaceTime.md)
- [/private/var/staged_system_apps/Files.app/Files](MACHOS/Files.md)
- [/private/var/staged_system_apps/FindMy.app/FindMy](MACHOS/FindMy.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyNotificationsContent.appex/FindMyNotificationsContent](MACHOS/FindMyNotificationsContent.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyNotificationsService.appex/FindMyNotificationsService](MACHOS/FindMyNotificationsService.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyWidgetIntentsItems.appex/FindMyWidgetIntentsItems](MACHOS/FindMyWidgetIntentsItems.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyWidgetIntentsPeople.appex/FindMyWidgetIntentsPeople](MACHOS/FindMyWidgetIntentsPeople.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyWidgetItems.appex/FindMyWidgetItems](MACHOS/FindMyWidgetItems.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyWidgetPeople.appex/FindMyWidgetPeople](MACHOS/FindMyWidgetPeople.md)
- [/private/var/staged_system_apps/Fitness.app/Fitness](MACHOS/Fitness.md)
- [/private/var/staged_system_apps/Fitness.app/PlugIns/FitnessIntents.appex/FitnessIntents](MACHOS/FitnessIntents.md)
- [/private/var/staged_system_apps/Fitness.app/PlugIns/FitnessWidget.appex/FitnessWidget](MACHOS/FitnessWidget.md)
- [/private/var/staged_system_apps/Fitness.app/PlugIns/MirroredWidgetExtension.appex/MirroredWidgetExtension](MACHOS/MirroredWidgetExtension.md)
- [/private/var/staged_system_apps/Freeform.app/Extensions/USDRendererExtension.appex/USDRendererExtension](MACHOS/USDRendererExtension.md)
- [/private/var/staged_system_apps/Freeform.app/Freeform](MACHOS/Freeform.md)
- [/private/var/staged_system_apps/Freeform.app/PlugIns/FreeformSharingExtension.appex/FreeformSharingExtension](MACHOS/FreeformSharingExtension.md)
- [/private/var/staged_system_apps/Health.app/Frameworks/HealthAppSupport.framework/HealthAppSupport](MACHOS/HealthAppSupport.md)
- [/private/var/staged_system_apps/Health.app/Frameworks/HealthAppSupport.framework/PlugIns/HealthFollowUpExtension.appex/HealthFollowUpExtension](MACHOS/HealthFollowUpExtension.md)
- [/private/var/staged_system_apps/Health.app/Health](MACHOS/Health.md)
- [/private/var/staged_system_apps/Health.app/PlugIns/HealthMedicationsWidgetExtension.appex/HealthMedicationsWidgetExtension](MACHOS/HealthMedicationsWidgetExtension.md)
- [/private/var/staged_system_apps/Health.app/PlugIns/HealthMentalHealthWidgetExtension.appex/HealthMentalHealthWidgetExtension](MACHOS/HealthMentalHealthWidgetExtension.md)
- [/private/var/staged_system_apps/Health.app/PlugIns/ShareExtension.appex/ShareExtension](MACHOS/ShareExtension.md)
- [/private/var/staged_system_apps/Home.app/Home](MACHOS/Home.md)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeDiagnosticExtension.appex/HomeDiagnosticExtension](MACHOS/HomeDiagnosticExtension.md)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeEnergyWidgetsExtension.appex/HomeEnergyWidgetsExtension](MACHOS/HomeEnergyWidgetsExtension.md)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeIntentExtension.appex/HomeIntentExtension](MACHOS/HomeIntentExtension.md)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeNotification.appex/HomeNotification](MACHOS/HomeNotification.md)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomePersonalRequestNotification.appex/HomePersonalRequestNotification](MACHOS/HomePersonalRequestNotification.md)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeUtilNotification.appex/HomeUtilNotification](MACHOS/HomeUtilNotification.md)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeWidget.appex/HomeWidget](MACHOS/HomeWidget.md)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeWidgetLockScreen.appex/HomeWidgetLockScreen](MACHOS/HomeWidgetLockScreen.md)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeWidgetSingleAccessoryIntent.appex/HomeWidgetSingleAccessoryIntent](MACHOS/HomeWidgetSingleAccessoryIntent.md)
- [/private/var/staged_system_apps/Journal.app/Journal](MACHOS/Journal.md)
- [/private/var/staged_system_apps/Journal.app/PlugIns/JournalShareExtension.appex/JournalShareExtension](MACHOS/JournalShareExtension.md)
- [/private/var/staged_system_apps/Magnifier.app/Magnifier](MACHOS/Magnifier.md)
- [/private/var/staged_system_apps/Maps.app/Maps](MACHOS/Maps.md)
- [/private/var/staged_system_apps/Maps.app/PlugIns/GeneralMapsWidget.appex/GeneralMapsWidget](MACHOS/GeneralMapsWidget.md)
- [/private/var/staged_system_apps/Maps.app/PlugIns/MapsSpotlightIndexExtension.appex/MapsSpotlightIndexExtension](MACHOS/MapsSpotlightIndexExtension.md)
- [/private/var/staged_system_apps/Maps.app/PlugIns/SiriTrafficIncidents.appex/SiriTrafficIncidents](MACHOS/SiriTrafficIncidents.md)
- [/private/var/staged_system_apps/Measure.app/Measure](MACHOS/Measure.md)
- [/private/var/staged_system_apps/MobileCal.app/Extensions/CalendarFocusConfigurationExtension.appex/CalendarFocusConfigurationExtension](MACHOS/CalendarFocusConfigurationExtension.md)
- [/private/var/staged_system_apps/MobileCal.app/MobileCal](MACHOS/MobileCal.md)
- [/private/var/staged_system_apps/MobileCal.app/PlugIns/CalendarWidgetExtension.appex/CalendarWidgetExtension](MACHOS/CalendarWidgetExtension.md)
- [/private/var/staged_system_apps/MobileCal.app/PlugIns/FacetimeExtension.appex/FacetimeExtension](MACHOS/FacetimeExtension.md)
- [/private/var/staged_system_apps/MobileMail.app/Extensions/MailShortcutsExtension.appex/MailShortcutsExtension](MACHOS/MailShortcutsExtension.md)
- [/private/var/staged_system_apps/MobileMail.app/MobileMail](MACHOS/MobileMail.md)
- [/private/var/staged_system_apps/MobileMail.app/PlugIns/DiagnosticExtension.appex/DiagnosticExtension](MACHOS/DiagnosticExtension.md)
- [/private/var/staged_system_apps/MobileMail.app/PlugIns/MailIntentsExtension.appex/MailIntentsExtension](MACHOS/MailIntentsExtension.md)
- [/private/var/staged_system_apps/MobileMail.app/PlugIns/MailNotificationContentExtension.appex/MailNotificationContentExtension](MACHOS/MailNotificationContentExtension.md)
- [/private/var/staged_system_apps/MobileMail.app/PlugIns/MailQuickLookExtension.appex/MailQuickLookExtension](MACHOS/MailQuickLookExtension.md)
- [/private/var/staged_system_apps/MobileMail.app/PlugIns/MailSpotlightIndexExtension.appex/MailSpotlightIndexExtension](MACHOS/MailSpotlightIndexExtension.md)
- [/private/var/staged_system_apps/MobileMail.app/PlugIns/MailWidgetExtension.appex/MailWidgetExtension](MACHOS/MailWidgetExtension.md)
- [/private/var/staged_system_apps/MobileNotes.app/MobileNotes](MACHOS/MobileNotes.md)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.EditorExtension.appex/com.apple.mobilenotes.EditorExtension](MACHOS/com.apple.mobilenotes.EditorExtension.md)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.IntentsExtension.appex/com.apple.mobilenotes.IntentsExtension](MACHOS/com.apple.mobilenotes.IntentsExtension.md)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.QuickLookExtension.appex/com.apple.mobilenotes.QuickLookExtension](MACHOS/com.apple.mobilenotes.QuickLookExtension.md)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.SharingExtension.appex/com.apple.mobilenotes.SharingExtension](MACHOS/com.apple.mobilenotes.SharingExtension.md)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.SpotlightIndexExtension.appex/com.apple.mobilenotes.SpotlightIndexExtension](MACHOS/com.apple.mobilenotes.SpotlightIndexExtension.md)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.WidgetExtension.appex/com.apple.mobilenotes.WidgetExtension](MACHOS/com.apple.mobilenotes.WidgetExtension.md)
- [/private/var/staged_system_apps/MobileStore.app/MobileStore](MACHOS/MobileStore.md)
- [/private/var/staged_system_apps/MobileStore.app/PlugIns/MusicStoreNotificationContentPlugin.appex/MusicStoreNotificationContentPlugin](MACHOS/MusicStoreNotificationContentPlugin.md)
- [/private/var/staged_system_apps/MobileStore.app/XPCServices/com.apple.MobileStore.appremoval.xpc/com.apple.MobileStore.appremoval](MACHOS/com.apple.MobileStore.appremoval.md)
- [/private/var/staged_system_apps/MobileTimer.app/MobileTimer](MACHOS/MobileTimer.md)
- [/private/var/staged_system_apps/MobileTimer.app/PlugIns/WorldClockWidget.appex/WorldClockWidget](MACHOS/WorldClockWidget.md)
- [/private/var/staged_system_apps/Music.app/Extensions/MusicFocusFilters.appex/MusicFocusFilters](MACHOS/MusicFocusFilters.md)
- [/private/var/staged_system_apps/Music.app/Frameworks/MusicApplication.framework/MusicApplication](MACHOS/MusicApplication.md)
- [/private/var/staged_system_apps/Music.app/Frameworks/MusicApplication.framework/XPCServices/MusicScriptUpdateService.xpc/MusicScriptUpdateService](MACHOS/MusicScriptUpdateService.md)
- [/private/var/staged_system_apps/Music.app/Music](MACHOS/Music.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/MediaPicker.appex/MediaPicker](MACHOS/MediaPicker.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/MusicCoreSpotlightExtension.appex/MusicCoreSpotlightExtension](MACHOS/MusicCoreSpotlightExtension.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/MusicMessagesApp.appex/MusicMessagesApp](MACHOS/MusicMessagesApp.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/MusicNotificationContentExtension.appex/MusicNotificationContentExtension](MACHOS/MusicNotificationContentExtension.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/MusicWidgets.appex/MusicWidgets](MACHOS/MusicWidgets.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/StoreFlowExtension.appex/StoreFlowExtension](MACHOS/StoreFlowExtension.md)
- [/private/var/staged_system_apps/News.app/News](MACHOS/News.md)
- [/private/var/staged_system_apps/News.app/PlugIns/ArticleNotificationExtension.appex/ArticleNotificationExtension](MACHOS/ArticleNotificationExtension.md)
- [/private/var/staged_system_apps/News.app/PlugIns/MarketingNotificationExtension.appex/MarketingNotificationExtension](MACHOS/MarketingNotificationExtension.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsArticleQuickLook.appex/NewsArticleQuickLook](MACHOS/NewsArticleQuickLook.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsAudioExtension.appex/NewsAudioExtension](MACHOS/NewsAudioExtension.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsDiagnosticExtension.appex/NewsDiagnosticExtension](MACHOS/NewsDiagnosticExtension.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsEngagementExtension.appex/NewsEngagementExtension](MACHOS/NewsEngagementExtension.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsNotificationServiceExtension.appex/NewsNotificationServiceExtension](MACHOS/NewsNotificationServiceExtension.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsTag.appex/NewsTag](MACHOS/NewsTag.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsToday2.appex/NewsToday2](MACHOS/NewsToday2.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsTodayIntents.appex/NewsTodayIntents](MACHOS/NewsTodayIntents.md)
- [/private/var/staged_system_apps/News.app/PlugIns/OpenInNews.appex/OpenInNews](MACHOS/OpenInNews.md)
- [/private/var/staged_system_apps/Passbook.app/Passbook](MACHOS/Passbook.md)
- [/private/var/staged_system_apps/Passbook.app/PlugIns/PassbookQuicklookPreviewExtension.appex/PassbookQuicklookPreviewExtension](MACHOS/PassbookQuicklookPreviewExtension.md)
- [/private/var/staged_system_apps/Passbook.app/PlugIns/PassbookTransactionNotificationContentExtension.appex/PassbookTransactionNotificationContentExtension](MACHOS/PassbookTransactionNotificationContentExtension.md)
- [/private/var/staged_system_apps/Passbook.app/PlugIns/PassbookWidgetsExtension-iPhone.appex/PassbookWidgetsExtension-iPhone](MACHOS/PassbookWidgetsExtension-iPhone.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/AppStoreKit.framework/AppStoreKit](MACHOS/AppStoreKit.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/IMDebug.framework/IMDebug](MACHOS/IMDebug.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/NowPlayingUI.framework/NowPlayingUI](MACHOS/NowPlayingUI.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/PodcastsStoreUI.framework/PodcastsStoreUI](MACHOS/PodcastsStoreUI.md)
- [/private/var/staged_system_apps/Podcasts.app/PlugIns/PodcastsAnnouncementsNotificationExtension.appex/PodcastsAnnouncementsNotificationExtension](MACHOS/PodcastsAnnouncementsNotificationExtension.md)
- [/private/var/staged_system_apps/Podcasts.app/PlugIns/PodcastsClassKitExtension.appex/PodcastsClassKitExtension](MACHOS/PodcastsClassKitExtension.md)
- [/private/var/staged_system_apps/Podcasts.app/PlugIns/PodcastsNotificationExtension.appex/PodcastsNotificationExtension](MACHOS/PodcastsNotificationExtension.md)
- [/private/var/staged_system_apps/Podcasts.app/PlugIns/PodcastsWidget.appex/PodcastsWidget](MACHOS/PodcastsWidget.md)
- [/private/var/staged_system_apps/Podcasts.app/PlugIns/com.apple.podcasts.DiagnosticExtension.appex/com.apple.podcasts.DiagnosticExtension](MACHOS/com.apple.podcasts.DiagnosticExtension.md)
- [/private/var/staged_system_apps/Podcasts.app/PlugIns/com.apple.podcasts.PodcastsProductPageExtension.appex/com.apple.podcasts.PodcastsProductPageExtension](MACHOS/com.apple.podcasts.PodcastsProductPageExtension.md)
- [/private/var/staged_system_apps/Podcasts.app/PlugIns/com.apple.podcasts.SpotlightIndexExtension.appex/com.apple.podcasts.SpotlightIndexExtension](MACHOS/com.apple.podcasts.SpotlightIndexExtension.md)
- [/private/var/staged_system_apps/Podcasts.app/Podcasts](MACHOS/Podcasts.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersIntentsExtension.appex/RemindersIntentsExtension](MACHOS/RemindersIntentsExtension.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersIntentsUIExtension.appex/RemindersIntentsUIExtension](MACHOS/RemindersIntentsUIExtension.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersSharingExtension.appex/RemindersSharingExtension](MACHOS/RemindersSharingExtension.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersSpotlightIndexExtension.appex/RemindersSpotlightIndexExtension](MACHOS/RemindersSpotlightIndexExtension.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersWidgetExtension.appex/RemindersWidgetExtension](MACHOS/RemindersWidgetExtension.md)
- [/private/var/staged_system_apps/Reminders.app/Reminders](MACHOS/Reminders.md)
- [/private/var/staged_system_apps/SequoiaTranslator.app/PlugIns/CacheDeleteExtension.appex/CacheDeleteExtension](MACHOS/CacheDeleteExtension.md)
- [/private/var/staged_system_apps/SequoiaTranslator.app/SequoiaTranslator](MACHOS/SequoiaTranslator.md)
- [/private/var/staged_system_apps/Shortcuts.app/PlugIns/AutomationNotificationContent.appex/AutomationNotificationContent](MACHOS/AutomationNotificationContent.md)
- [/private/var/staged_system_apps/Shortcuts.app/PlugIns/QuickLookExtension.appex/QuickLookExtension](MACHOS/QuickLookExtension.md)
- [/private/var/staged_system_apps/Shortcuts.app/PlugIns/ShortcutsActionExtension.appex/ShortcutsActionExtension](MACHOS/ShortcutsActionExtension.md)
- [/private/var/staged_system_apps/Shortcuts.app/PlugIns/ShortcutsWidgetExtension.appex/ShortcutsWidgetExtension](MACHOS/ShortcutsWidgetExtension.md)
- [/private/var/staged_system_apps/Shortcuts.app/PlugIns/ThumbnailExtension.appex/ThumbnailExtension](MACHOS/ThumbnailExtension.md)
- [/private/var/staged_system_apps/Shortcuts.app/Shortcuts](MACHOS/Shortcuts.md)
- [/private/var/staged_system_apps/Stocks.app/PlugIns/StocksDetailIntents.appex/StocksDetailIntents](MACHOS/StocksDetailIntents.md)
- [/private/var/staged_system_apps/Stocks.app/PlugIns/StocksDiagnosticExtension.appex/StocksDiagnosticExtension](MACHOS/StocksDiagnosticExtension.md)
- [/private/var/staged_system_apps/Stocks.app/PlugIns/StocksWidget.appex/StocksWidget](MACHOS/StocksWidget.md)
- [/private/var/staged_system_apps/Stocks.app/Stocks](MACHOS/Stocks.md)
- [/private/var/staged_system_apps/Tips.app/PlugIns/TipsNotification.appex/TipsNotification](MACHOS/TipsNotification.md)
- [/private/var/staged_system_apps/Tips.app/PlugIns/TipsQuicklook.appex/TipsQuicklook](MACHOS/TipsQuicklook.md)
- [/private/var/staged_system_apps/Tips.app/PlugIns/TipsSpotlightIndex.appex/TipsSpotlightIndex](MACHOS/TipsSpotlightIndex.md)
- [/private/var/staged_system_apps/Tips.app/PlugIns/TipsWidget.appex/TipsWidget](MACHOS/TipsWidget.md)
- [/private/var/staged_system_apps/Tips.app/Tips](MACHOS/Tips.md)
- [/private/var/staged_system_apps/VoiceMemos.app/PlugIns/VoiceMemosIntentsExtension.appex/VoiceMemosIntentsExtension](MACHOS/VoiceMemosIntentsExtension.md)
- [/private/var/staged_system_apps/VoiceMemos.app/PlugIns/VoiceMemosShareExtension.appex/VoiceMemosShareExtension](MACHOS/VoiceMemosShareExtension.md)
- [/private/var/staged_system_apps/VoiceMemos.app/PlugIns/com.apple.VoiceMemos.SpotlightIndexExtension.appex/com.apple.VoiceMemos.SpotlightIndexExtension](MACHOS/com.apple.VoiceMemos.SpotlightIndexExtension.md)
- [/private/var/staged_system_apps/VoiceMemos.app/VoiceMemos](MACHOS/VoiceMemos.md)
- [/private/var/staged_system_apps/Weather.app/PlugIns/WeatherDiagnosticExtension.appex/WeatherDiagnosticExtension](MACHOS/WeatherDiagnosticExtension.md)
- [/private/var/staged_system_apps/Weather.app/PlugIns/WeatherIntents.appex/WeatherIntents](MACHOS/WeatherIntents.md)
- [/private/var/staged_system_apps/Weather.app/PlugIns/WeatherPoster.appex/WeatherPoster](MACHOS/WeatherPoster.md)
- [/private/var/staged_system_apps/Weather.app/PlugIns/WeatherWidget.appex/WeatherWidget](MACHOS/WeatherWidget.md)
- [/private/var/staged_system_apps/Weather.app/Weather](MACHOS/Weather.md)
- [/sbin/fsck](MACHOS/fsck.md)
- [/sbin/launchd](MACHOS/launchd.md)
- [/sbin/mount](MACHOS/mount.md)
- [/sbin/mount_lifs](MACHOS/mount_lifs.md)
- [/sbin/mount_nfs](MACHOS/mount_nfs.md)
- [/sbin/umount](MACHOS/umount.md)
- [/usr/bin/DumpBasebandCrash](MACHOS/DumpBasebandCrash.md)
- [/usr/bin/IOMFB_FDR_Loader](MACHOS/IOMFB_FDR_Loader.md)
- [/usr/bin/abmlite](MACHOS/abmlite.md)
- [/usr/bin/afktool](MACHOS/afktool.md)
- [/usr/bin/brctl](MACHOS/brctl.md)
- [/usr/bin/codecctl](MACHOS/codecctl.md)
- [/usr/bin/fileproviderctl](MACHOS/fileproviderctl.md)
- [/usr/bin/footprint](MACHOS/footprint.md)
- [/usr/bin/hidutil](MACHOS/hidutil.md)
- [/usr/bin/hpmdiagnose](MACHOS/hpmdiagnose.md)
- [/usr/bin/kbdebug](MACHOS/kbdebug.md)
- [/usr/bin/lsdiagnose](MACHOS/lsdiagnose.md)
- [/usr/bin/ltop](MACHOS/ltop.md)
- [/usr/bin/nfsstat](MACHOS/nfsstat.md)
- [/usr/bin/powerlogHelperd](MACHOS/powerlogHelperd.md)
- [/usr/bin/swift-inspect](MACHOS/swift-inspect.md)
- [/usr/bin/sysdiagnose](MACHOS/sysdiagnose.md)
- [/usr/bin/tailspin](MACHOS/tailspin.md)
- [/usr/bin/taskinfo](MACHOS/taskinfo.md)
- [/usr/bin/umtool](MACHOS/umtool.md)
- [/usr/bin/vm_stat](MACHOS/vm_stat.md)
- [/usr/bin/zprint](MACHOS/zprint.md)
- [/usr/lib/dyld](MACHOS/dyld.md)
- [/usr/lib/libBacktraceRecording.dylib](MACHOS/libBacktraceRecording.dylib.md)
- [/usr/lib/libLogRedirect.dylib](MACHOS/libLogRedirect.dylib.md)
- [/usr/lib/libMainThreadChecker.dylib](MACHOS/libMainThreadChecker.dylib.md)
- [/usr/lib/libRPAC.dylib](MACHOS/libRPAC.dylib.md)
- [/usr/lib/libSystem.B_asan.dylib](MACHOS/libSystem.B_asan.dylib.md)
- [/usr/lib/libViewDebuggerSupport.dylib](MACHOS/libViewDebuggerSupport.dylib.md)
- [/usr/lib/libffi-trampolines.dylib](MACHOS/libffi-trampolines.dylib.md)
- [/usr/lib/libglInterpose.dylib](MACHOS/libglInterpose.dylib.md)
- [/usr/lib/libobjc-trampolines.dylib](MACHOS/libobjc-trampolines.dylib.md)
- [/usr/lib/libstdc++.6.0.9.dylib](MACHOS/libstdc++.6.0.9.dylib.md)
- [/usr/lib/swift/libswiftRemoteMirror.dylib](MACHOS/libswiftRemoteMirror.dylib.md)
- [/usr/lib/system/introspection/libdispatch.dylib](MACHOS/libdispatch.dylib.md)
- [/usr/lib/xpc/support.bundle/support](MACHOS/support.md)
- [/usr/libexec/ASPCarryLog](MACHOS/ASPCarryLog.md)
- [/usr/libexec/AuthenticationServicesAgent](MACHOS/AuthenticationServicesAgent.md)
- [/usr/libexec/BackupAgent2](MACHOS/BackupAgent2.md)
- [/usr/libexec/ChassisAttestationd](MACHOS/ChassisAttestationd.md)
- [/usr/libexec/DataDetectorsSourceAccess](MACHOS/DataDetectorsSourceAccess.md)
- [/usr/libexec/DumpPanic](MACHOS/DumpPanic.md)
- [/usr/libexec/FSTaskScheduler](MACHOS/FSTaskScheduler.md)
- [/usr/libexec/FinishRestoreFromBackup](MACHOS/FinishRestoreFromBackup.md)
- [/usr/libexec/IOAccelMemoryInfoCollector](MACHOS/IOAccelMemoryInfoCollector.md)
- [/usr/libexec/IOMFB_bics_daemon](MACHOS/IOMFB_bics_daemon.md)
- [/usr/libexec/MSUEarlyBootTask](MACHOS/MSUEarlyBootTask.md)
- [/usr/libexec/MTLAssetUpgraderD](MACHOS/MTLAssetUpgraderD.md)
- [/usr/libexec/MobileGestaltHelper](MACHOS/MobileGestaltHelper.md)
- [/usr/libexec/MobileStorageMounter](MACHOS/MobileStorageMounter.md)
- [/usr/libexec/NANDTaskScheduler](MACHOS/NANDTaskScheduler.md)
- [/usr/libexec/OTATaskingAgent](MACHOS/OTATaskingAgent.md)
- [/usr/libexec/PerfPowerServices](MACHOS/PerfPowerServices.md)
- [/usr/libexec/PerfPowerServicesExtended](MACHOS/PerfPowerServicesExtended.md)
- [/usr/libexec/PowerUIAgent](MACHOS/PowerUIAgent.md)
- [/usr/libexec/PreboardService](MACHOS/PreboardService.md)
- [/usr/libexec/ProxiedCrashCopier](MACHOS/ProxiedCrashCopier.md)
- [/usr/libexec/PurpleReverseProxy](MACHOS/PurpleReverseProxy.md)
- [/usr/libexec/ReportMemoryException](MACHOS/ReportMemoryException.md)
- [/usr/libexec/SavageUtil](MACHOS/SavageUtil.md)
- [/usr/libexec/SensorKitALSHelper](MACHOS/SensorKitALSHelper.md)
- [/usr/libexec/SidecarRelay](MACHOS/SidecarRelay.md)
- [/usr/libexec/SyncAgent](MACHOS/SyncAgent.md)
- [/usr/libexec/UserEventAgent](MACHOS/UserEventAgent.md)
- [/usr/libexec/ViewHierarchyAgent](MACHOS/ViewHierarchyAgent.md)
- [/usr/libexec/YonkersUtil](MACHOS/YonkersUtil.md)
- [/usr/libexec/addressbooksyncd](MACHOS/addressbooksyncd.md)
- [/usr/libexec/adprivacyd](MACHOS/adprivacyd.md)
- [/usr/libexec/afcd](MACHOS/afcd.md)
- [/usr/libexec/amfid](MACHOS/amfid.md)
- [/usr/libexec/aned](MACHOS/aned.md)
- [/usr/libexec/announced](MACHOS/announced.md)
- [/usr/libexec/anomalydetectiond](MACHOS/anomalydetectiond.md)
- [/usr/libexec/appleaccountd](MACHOS/appleaccountd.md)
- [/usr/libexec/appleidsetupd](MACHOS/appleidsetupd.md)
- [/usr/libexec/arkitd](MACHOS/arkitd.md)
- [/usr/libexec/asd](MACHOS/asd.md)
- [/usr/libexec/asktod](MACHOS/asktod.md)
- [/usr/libexec/assessmentagent](MACHOS/assessmentagent.md)
- [/usr/libexec/atc](MACHOS/atc.md)
- [/usr/libexec/audioaccessoryd](MACHOS/audioaccessoryd.md)
- [/usr/libexec/audioanalyticsd](MACHOS/audioanalyticsd.md)
- [/usr/libexec/audioclocksyncd](MACHOS/audioclocksyncd.md)
- [/usr/libexec/audiomxd](MACHOS/audiomxd.md)
- [/usr/libexec/avconferenced](MACHOS/avconferenced.md)
- [/usr/libexec/backboardd](MACHOS/backboardd.md)
- [/usr/libexec/backgroundassets.user](MACHOS/backgroundassets.user.md)
- [/usr/libexec/batteryalgorithmsd](MACHOS/batteryalgorithmsd.md)
- [/usr/libexec/batteryintelligenced](MACHOS/batteryintelligenced.md)
- [/usr/libexec/betaenrollmentd](MACHOS/betaenrollmentd.md)
- [/usr/libexec/biomesyncd](MACHOS/biomesyncd.md)
- [/usr/libexec/biometrickitd](MACHOS/biometrickitd.md)
- [/usr/libexec/bluetoothuserd](MACHOS/bluetoothuserd.md)
- [/usr/libexec/bootpd](MACHOS/bootpd.md)
- [/usr/libexec/brookcompaniond](MACHOS/brookcompaniond.md)
- [/usr/libexec/bulletindistributord](MACHOS/bulletindistributord.md)
- [/usr/libexec/captiveagent](MACHOS/captiveagent.md)
- [/usr/libexec/carkitd](MACHOS/carkitd.md)
- [/usr/libexec/cc_fips_test](MACHOS/cc_fips_test.md)
- [/usr/libexec/checkerboardd](MACHOS/checkerboardd.md)
- [/usr/libexec/checkpointd](MACHOS/checkpointd.md)
- [/usr/libexec/ciphermld](MACHOS/ciphermld.md)
- [/usr/libexec/com.apple.Safari.History](MACHOS/com.apple.Safari.History.md)
- [/usr/libexec/companion_proxy](MACHOS/companion_proxy.md)
- [/usr/libexec/companiond](MACHOS/companiond.md)
- [/usr/libexec/configd](MACHOS/configd.md)
- [/usr/libexec/containermanagerd](MACHOS/containermanagerd.md)
- [/usr/libexec/containermanagerd_system](MACHOS/containermanagerd_system.md)
- [/usr/libexec/continuitycaptured](MACHOS/continuitycaptured.md)
- [/usr/libexec/coordinated](MACHOS/coordinated.md)
- [/usr/libexec/corebrightnessdiag](MACHOS/corebrightnessdiag.md)
- [/usr/libexec/corecaptured](MACHOS/corecaptured.md)
- [/usr/libexec/coredatad](MACHOS/coredatad.md)
- [/usr/libexec/coreduetd](MACHOS/coreduetd.md)
- [/usr/libexec/coreidvd](MACHOS/coreidvd.md)
- [/usr/libexec/corerepaird](MACHOS/corerepaird.md)
- [/usr/libexec/countryd](MACHOS/countryd.md)
- [/usr/libexec/crash_mover](MACHOS/crash_mover.md)
- [/usr/libexec/cryptexd](MACHOS/cryptexd.md)
- [/usr/libexec/dasd](MACHOS/dasd.md)
- [/usr/libexec/datastored](MACHOS/datastored.md)
- [/usr/libexec/debugserver](MACHOS/debugserver.md)
- [/usr/libexec/deferredmediad](MACHOS/deferredmediad.md)
- [/usr/libexec/demod](MACHOS/demod.md)
- [/usr/libexec/demod_helper](MACHOS/demod_helper.md)
- [/usr/libexec/deviceaccessd](MACHOS/deviceaccessd.md)
- [/usr/libexec/dhcp6d](MACHOS/dhcp6d.md)
- [/usr/libexec/diagnosticd](MACHOS/diagnosticd.md)
- [/usr/libexec/diagnosticextensionsd](MACHOS/diagnosticextensionsd.md)
- [/usr/libexec/dirs_cleaner](MACHOS/dirs_cleaner.md)
- [/usr/libexec/diskarbitrationd](MACHOS/diskarbitrationd.md)
- [/usr/libexec/diskimagesiod](MACHOS/diskimagesiod.md)
- [/usr/libexec/dmd](MACHOS/dmd.md)
- [/usr/libexec/dockaccessoryd](MACHOS/dockaccessoryd.md)
- [/usr/libexec/dprivacyd](MACHOS/dprivacyd.md)
- [/usr/libexec/driverkitd](MACHOS/driverkitd.md)
- [/usr/libexec/dtfetchsymbolsd](MACHOS/dtfetchsymbolsd.md)
- [/usr/libexec/duetexpertd](MACHOS/duetexpertd.md)
- [/usr/libexec/eventkitsyncd](MACHOS/eventkitsyncd.md)
- [/usr/libexec/facemetricsd](MACHOS/facemetricsd.md)
- [/usr/libexec/fairplaydeviceidentityd](MACHOS/fairplaydeviceidentityd.md)
- [/usr/libexec/fdrhelper](MACHOS/fdrhelper.md)
- [/usr/libexec/feedbackd](MACHOS/feedbackd.md)
- [/usr/libexec/findmybeaconingd](MACHOS/findmybeaconingd.md)
- [/usr/libexec/findmydeviced](MACHOS/findmydeviced.md)
- [/usr/libexec/findmylocated](MACHOS/findmylocated.md)
- [/usr/libexec/finish_demo_restore](MACHOS/finish_demo_restore.md)
- [/usr/libexec/fmfd](MACHOS/fmfd.md)
- [/usr/libexec/fmflocatord](MACHOS/fmflocatord.md)
- [/usr/libexec/fseventsd](MACHOS/fseventsd.md)
- [/usr/libexec/ftp-proxy](MACHOS/ftp-proxy.md)
- [/usr/libexec/fusiond](MACHOS/fusiond.md)
- [/usr/libexec/gamecontrollerd](MACHOS/gamecontrollerd.md)
- [/usr/libexec/gamed](MACHOS/gamed.md)
- [/usr/libexec/gamepolicyd](MACHOS/gamepolicyd.md)
- [/usr/libexec/gpsd](MACHOS/gpsd.md)
- [/usr/libexec/gputoolsd](MACHOS/gputoolsd.md)
- [/usr/libexec/gputoolsserviced](MACHOS/gputoolsserviced.md)
- [/usr/libexec/griddatad](MACHOS/griddatad.md)
- [/usr/libexec/handwritingd](MACHOS/handwritingd.md)
- [/usr/libexec/hangreporter](MACHOS/hangreporter.md)
- [/usr/libexec/hangtracerd](MACHOS/hangtracerd.md)
- [/usr/libexec/heartbeatd](MACHOS/heartbeatd.md)
- [/usr/libexec/hidd](MACHOS/hidd.md)
- [/usr/libexec/hostapd](MACHOS/hostapd.md)
- [/usr/libexec/icloudmailagent](MACHOS/icloudmailagent.md)
- [/usr/libexec/idamd](MACHOS/idamd.md)
- [/usr/libexec/idcredd](MACHOS/idcredd.md)
- [/usr/libexec/inboxupdaterd](MACHOS/inboxupdaterd.md)
- [/usr/libexec/init_featureflags](MACHOS/init_featureflags.md)
- [/usr/libexec/installd](MACHOS/installd.md)
- [/usr/libexec/intelligentroutingd](MACHOS/intelligentroutingd.md)
- [/usr/libexec/ioupsd](MACHOS/ioupsd.md)
- [/usr/libexec/keybagd](MACHOS/keybagd.md)
- [/usr/libexec/keychainsharingmessagingd](MACHOS/keychainsharingmessagingd.md)
- [/usr/libexec/languageassetd](MACHOS/languageassetd.md)
- [/usr/libexec/launchd_cache_loader](MACHOS/launchd_cache_loader.md)
- [/usr/libexec/linkd](MACHOS/linkd.md)
- [/usr/libexec/locationd](MACHOS/locationd.md)
- [/usr/libexec/locationpushd](MACHOS/locationpushd.md)
- [/usr/libexec/lockdownd](MACHOS/lockdownd.md)
- [/usr/libexec/logd](MACHOS/logd.md)
- [/usr/libexec/logd_helper](MACHOS/logd_helper.md)
- [/usr/libexec/logd_reporter](MACHOS/logd_reporter.md)
- [/usr/libexec/lsd](MACHOS/lsd.md)
- [/usr/libexec/magicswitchd](MACHOS/magicswitchd.md)
- [/usr/libexec/mc_mobile_tunnel](MACHOS/mc_mobile_tunnel.md)
- [/usr/libexec/mdmd](MACHOS/mdmd.md)
- [/usr/libexec/mdmuserd](MACHOS/mdmuserd.md)
- [/usr/libexec/mediaparserd](MACHOS/mediaparserd.md)
- [/usr/libexec/mediaplaybackd](MACHOS/mediaplaybackd.md)
- [/usr/libexec/mediasetupd](MACHOS/mediasetupd.md)
- [/usr/libexec/metrickitd](MACHOS/metrickitd.md)
- [/usr/libexec/microstackshot](MACHOS/microstackshot.md)
- [/usr/libexec/misagent](MACHOS/misagent.md)
- [/usr/libexec/misd](MACHOS/misd.md)
- [/usr/libexec/mlhostd](MACHOS/mlhostd.md)
- [/usr/libexec/mlruntimed](MACHOS/mlruntimed.md)
- [/usr/libexec/mmaintenanced](MACHOS/mmaintenanced.md)
- [/usr/libexec/mobile_assertion_agent](MACHOS/mobile_assertion_agent.md)
- [/usr/libexec/mobile_diagnostics_relay](MACHOS/mobile_diagnostics_relay.md)
- [/usr/libexec/mobile_house_arrest](MACHOS/mobile_house_arrest.md)
- [/usr/libexec/mobile_installation_proxy](MACHOS/mobile_installation_proxy.md)
- [/usr/libexec/mobile_obliterator](MACHOS/mobile_obliterator.md)
- [/usr/libexec/mobile_storage_proxy](MACHOS/mobile_storage_proxy.md)
- [/usr/libexec/mobileactivationd](MACHOS/mobileactivationd.md)
- [/usr/libexec/mobileassetd](MACHOS/mobileassetd.md)
- [/usr/libexec/mobilerepaird](MACHOS/mobilerepaird.md)
- [/usr/libexec/momentsd](MACHOS/momentsd.md)
- [/usr/libexec/mtmergeprops](MACHOS/mtmergeprops.md)
- [/usr/libexec/nanomediaremotelinkagent](MACHOS/nanomediaremotelinkagent.md)
- [/usr/libexec/nanoregistryd](MACHOS/nanoregistryd.md)
- [/usr/libexec/nanoregistrylaunchd](MACHOS/nanoregistrylaunchd.md)
- [/usr/libexec/naturallanguaged](MACHOS/naturallanguaged.md)
- [/usr/libexec/neagent](MACHOS/neagent.md)
- [/usr/libexec/nearbyd](MACHOS/nearbyd.md)
- [/usr/libexec/nehelper](MACHOS/nehelper.md)
- [/usr/libexec/nesessionmanager](MACHOS/nesessionmanager.md)
- [/usr/libexec/networkserviceproxy](MACHOS/networkserviceproxy.md)
- [/usr/libexec/nexusd](MACHOS/nexusd.md)
- [/usr/libexec/nfcd](MACHOS/nfcd.md)
- [/usr/libexec/nfrestore_service](MACHOS/nfrestore_service.md)
- [/usr/libexec/nlcd](MACHOS/nlcd.md)
- [/usr/libexec/notification_proxy](MACHOS/notification_proxy.md)
- [/usr/libexec/nptocompaniond](MACHOS/nptocompaniond.md)
- [/usr/libexec/nsurlsessiond](MACHOS/nsurlsessiond.md)
- [/usr/libexec/online-auth-agent](MACHOS/online-auth-agent.md)
- [/usr/libexec/ospredictiond](MACHOS/ospredictiond.md)
- [/usr/libexec/otpaird](MACHOS/otpaird.md)
- [/usr/libexec/passcodenagd](MACHOS/passcodenagd.md)
- [/usr/libexec/passwordbreachd](MACHOS/passwordbreachd.md)
- [/usr/libexec/pcapd](MACHOS/pcapd.md)
- [/usr/libexec/pcsstatus](MACHOS/pcsstatus.md)
- [/usr/libexec/peakpowermanagerd](MACHOS/peakpowermanagerd.md)
- [/usr/libexec/perfdiagsselfenabled](MACHOS/perfdiagsselfenabled.md)
- [/usr/libexec/pfd](MACHOS/pfd.md)
- [/usr/libexec/pipelined](MACHOS/pipelined.md)
- [/usr/libexec/pkd](MACHOS/pkd.md)
- [/usr/libexec/pkreporter](MACHOS/pkreporter.md)
- [/usr/libexec/pmudiagnose/pmudiagnose](MACHOS/pmudiagnose.md)
- [/usr/libexec/powerdatad](MACHOS/powerdatad.md)
- [/usr/libexec/prng_seedctl](MACHOS/prng_seedctl.md)
- [/usr/libexec/proactiveeventtrackerd](MACHOS/proactiveeventtrackerd.md)
- [/usr/libexec/profiled](MACHOS/profiled.md)
- [/usr/libexec/promotedcontentd](MACHOS/promotedcontentd.md)
- [/usr/libexec/proximitycontrold](MACHOS/proximitycontrold.md)
- [/usr/libexec/ptpcamerad](MACHOS/ptpcamerad.md)
- [/usr/libexec/ptpd](MACHOS/ptpd.md)
- [/usr/libexec/rapportd](MACHOS/rapportd.md)
- [/usr/libexec/relatived](MACHOS/relatived.md)
- [/usr/libexec/remindd](MACHOS/remindd.md)
- [/usr/libexec/remotectl](MACHOS/remotectl.md)
- [/usr/libexec/remoted](MACHOS/remoted.md)
- [/usr/libexec/remotepairingdeviced](MACHOS/remotepairingdeviced.md)
- [/usr/libexec/replayd](MACHOS/replayd.md)
- [/usr/libexec/resourcegrabberd](MACHOS/resourcegrabberd.md)
- [/usr/libexec/restoreserviced](MACHOS/restoreserviced.md)
- [/usr/libexec/routined](MACHOS/routined.md)
- [/usr/libexec/rsync/rsync.samba](MACHOS/rsync.samba.md)
- [/usr/libexec/rtcreportingd](MACHOS/rtcreportingd.md)
- [/usr/libexec/runningboardd](MACHOS/runningboardd.md)
- [/usr/libexec/safarifetcherd](MACHOS/safarifetcherd.md)
- [/usr/libexec/safetyalertsd](MACHOS/safetyalertsd.md)
- [/usr/libexec/screenshotsyncd](MACHOS/screenshotsyncd.md)
- [/usr/libexec/searchpartyd](MACHOS/searchpartyd.md)
- [/usr/libexec/security-sysdiagnose](MACHOS/security-sysdiagnose.md)
- [/usr/libexec/securityd](MACHOS/securityd.md)
- [/usr/libexec/securityuploadd](MACHOS/securityuploadd.md)
- [/usr/libexec/seld](MACHOS/seld.md)
- [/usr/libexec/sensorkitd](MACHOS/sensorkitd.md)
- [/usr/libexec/seputil](MACHOS/seputil.md)
- [/usr/libexec/seserviced](MACHOS/seserviced.md)
- [/usr/libexec/sharingd](MACHOS/sharingd.md)
- [/usr/libexec/signpost_reporter](MACHOS/signpost_reporter.md)
- [/usr/libexec/silhouette](MACHOS/silhouette.md)
- [/usr/libexec/siriknowledged](MACHOS/siriknowledged.md)
- [/usr/libexec/sirireaderd](MACHOS/sirireaderd.md)
- [/usr/libexec/smcDiagnose](MACHOS/smcDiagnose.md)
- [/usr/libexec/softposreaderd](MACHOS/softposreaderd.md)
- [/usr/libexec/spindump_fileparser](MACHOS/spindump_fileparser.md)
- [/usr/libexec/splashboardd](MACHOS/splashboardd.md)
- [/usr/libexec/sportsd](MACHOS/sportsd.md)
- [/usr/libexec/springboardservicesrelay](MACHOS/springboardservicesrelay.md)
- [/usr/libexec/srp-mdns-proxy](MACHOS/srp-mdns-proxy.md)
- [/usr/libexec/storagedatad](MACHOS/storagedatad.md)
- [/usr/libexec/storagekitd](MACHOS/storagekitd.md)
- [/usr/libexec/streaming_zip_conduit](MACHOS/streaming_zip_conduit.md)
- [/usr/libexec/swcd](MACHOS/swcd.md)
- [/usr/libexec/symptomsd](MACHOS/symptomsd.md)
- [/usr/libexec/symptomsd-diag](MACHOS/symptomsd-diag.md)
- [/usr/libexec/symptomsd-helper](MACHOS/symptomsd-helper.md)
- [/usr/libexec/sysdiagnose_helper](MACHOS/sysdiagnose_helper.md)
- [/usr/libexec/sysdiagnosed](MACHOS/sysdiagnosed.md)
- [/usr/libexec/sysmond](MACHOS/sysmond.md)
- [/usr/libexec/sysstatuscheck](MACHOS/sysstatuscheck.md)
- [/usr/libexec/tailspind](MACHOS/tailspind.md)
- [/usr/libexec/terminusd](MACHOS/terminusd.md)
- [/usr/libexec/teslad](MACHOS/teslad.md)
- [/usr/libexec/thermalmonitord](MACHOS/thermalmonitord.md)
- [/usr/libexec/timed](MACHOS/timed.md)
- [/usr/libexec/tipsd](MACHOS/tipsd.md)
- [/usr/libexec/transitd](MACHOS/transitd.md)
- [/usr/libexec/transparency-sysdiagnose](MACHOS/transparency-sysdiagnose.md)
- [/usr/libexec/transparencyStaticKey](MACHOS/transparencyStaticKey.md)
- [/usr/libexec/transparencyd](MACHOS/transparencyd.md)
- [/usr/libexec/triald](MACHOS/triald.md)
- [/usr/libexec/triald_system](MACHOS/triald_system.md)
- [/usr/libexec/trustd](MACHOS/trustd.md)
- [/usr/libexec/tursd](MACHOS/tursd.md)
- [/usr/libexec/tvremoted](MACHOS/tvremoted.md)
- [/usr/libexec/tzd](MACHOS/tzd.md)
- [/usr/libexec/tzinit](MACHOS/tzinit.md)
- [/usr/libexec/tzlinkd](MACHOS/tzlinkd.md)
- [/usr/libexec/usermanagerd](MACHOS/usermanagerd.md)
- [/usr/libexec/usermanagerhelper](MACHOS/usermanagerhelper.md)
- [/usr/libexec/videocodecd](MACHOS/videocodecd.md)
- [/usr/libexec/videosubscriptionsd](MACHOS/videosubscriptionsd.md)
- [/usr/libexec/wapic](MACHOS/wapic.md)
- [/usr/libexec/watchdogd](MACHOS/watchdogd.md)
- [/usr/libexec/watchpresenced](MACHOS/watchpresenced.md)
- [/usr/libexec/wcd](MACHOS/wcd.md)
- [/usr/libexec/webbookmarksd](MACHOS/webbookmarksd.md)
- [/usr/libexec/webinspectord](MACHOS/webinspectord.md)
- [/usr/libexec/webpushd](MACHOS/webpushd.md)
- [/usr/libexec/wifiFirmwareLoader](MACHOS/wifiFirmwareLoader.md)
- [/usr/libexec/wifianalyticsd](MACHOS/wifianalyticsd.md)
- [/usr/libexec/wifip2pd](MACHOS/wifip2pd.md)
- [/usr/libexec/wifivelocityd](MACHOS/wifivelocityd.md)
- [/usr/libexec/xpcproxy](MACHOS/xpcproxy.md)
- [/usr/libexec/xpcroleaccountd](MACHOS/xpcroleaccountd.md)
- [/usr/sbin/BTAvrcp](MACHOS/BTAvrcp.md)
- [/usr/sbin/BTLEServer](MACHOS/BTLEServer.md)
- [/usr/sbin/BTMap](MACHOS/BTMap.md)
- [/usr/sbin/BTPbap](MACHOS/BTPbap.md)
- [/usr/sbin/BlueTool](MACHOS/BlueTool.md)
- [/usr/sbin/WirelessRadioManagerd](MACHOS/WirelessRadioManagerd.md)
- [/usr/sbin/addNetworkInterface](MACHOS/addNetworkInterface.md)
- [/usr/sbin/appleh16camerad](MACHOS/appleh16camerad.md)
- [/usr/sbin/aslmanager](MACHOS/aslmanager.md)
- [/usr/sbin/bluetoothd](MACHOS/bluetoothd.md)
- [/usr/sbin/cfprefsd](MACHOS/cfprefsd.md)
- [/usr/sbin/ckksctl](MACHOS/ckksctl.md)
- [/usr/sbin/dietappleh16camerad](MACHOS/dietappleh16camerad.md)
- [/usr/sbin/distnoted](MACHOS/distnoted.md)
- [/usr/sbin/filecoordinationd](MACHOS/filecoordinationd.md)
- [/usr/sbin/hdik](MACHOS/hdik.md)
- [/usr/sbin/ioreg](MACHOS/ioreg.md)
- [/usr/sbin/mDNSResponder](MACHOS/mDNSResponder.md)
- [/usr/sbin/mDNSResponderHelper](MACHOS/mDNSResponderHelper.md)
- [/usr/sbin/mediaserverd](MACHOS/mediaserverd.md)
- [/usr/sbin/notifyd](MACHOS/notifyd.md)
- [/usr/sbin/nvram](MACHOS/nvram.md)
- [/usr/sbin/otctl](MACHOS/otctl.md)
- [/usr/sbin/pppd](MACHOS/pppd.md)
- [/usr/sbin/racoon](MACHOS/racoon.md)
- [/usr/sbin/rtadvd](MACHOS/rtadvd.md)
- [/usr/sbin/spindump](MACHOS/spindump.md)
- [/usr/sbin/syslogd](MACHOS/syslogd.md)
- [/usr/sbin/wifid](MACHOS/wifid.md)

</details>

### 🔑 Entitlements

- [Entitlements DIFF](Entitlements.md)

## Firmware

### ⬆️ Updated (13)

<details>
  <summary><i>View Updated</i></summary>

#### AppleAVE2FW_H16.im4p

>  `AppleAVE2FW_H16.im4p`

```diff

 
-  __TEXT.__text: 0xb6188
+  __TEXT.__text: 0xb61ac
   __TEXT.__cstring: 0x11ebc
   __TEXT.__const: 0x1ca68
   __TEXT.__chain_starts: 0x0

   __DATA._rtk_threads: 0x0
   __DATA._rtk_heap: 0x0
   __DATA.__zerofill: 0xc6878
-  UUID: 9D5A2D01-D52B-3F3C-B3B7-0BB08162D147
+  UUID: 2D4C3C15-799A-362C-8FA9-A2AAFDA045BF
   Functions: 0
   Symbols:   1429
   CStrings:  2013

```

#### SmartIOFirmware_ASCv6.im4p

>  `SmartIOFirmware_ASCv6.im4p`

```diff

 
-  __TEXT.__text: 0x1a228
+  __TEXT.__text: 0x1a244
   __TEXT.__cstring: 0x1034
   __TEXT.__const: 0x338
   __TEXT._rtk_mtab: 0x278

   __DATA.__autobkp: 0x0
   __DATA._rtk_heap: 0x0
   __DATA.__zerofill: 0xcec78
-  UUID: F3D55F5A-475D-3A8E-8E06-119BACBADF9D
+  UUID: F2B1CB93-9D1A-3F70-9E44-C03E363F12FC
   Functions: 0
   Symbols:   170
   CStrings:  264

```

#### adc-aceso-d8x.im4p

>  `adc-aceso-d8x.im4p`

```diff

 
-  __TEXT.__text: 0x78cb3c
+  __TEXT.__text: 0x78cb58
   __TEXT.__data_copy: 0x100000
   __TEXT.__const: 0x7ddee0
   __TEXT.__cstring: 0x9589c

   __DATA.__mod_init_func: 0x20
   __DATA.__noinit: 0x0
   __DATA.__zerofill: 0xb75f8
-  UUID: B6F6A0D7-6F9C-3020-B83F-599C471B2D9B
+  UUID: B0BF078F-1A35-3292-861A-EF6302FFFEA8
   Functions: 0
   Symbols:   0
   CStrings:  16620
CStrings:
+ "22:35:26"
+ "Dec 20 2023"
- "08:08:59"
- "Nov 12 2023"

```

#### agx_a000

>  `agx_a000`

```diff

 
-  __TEXT.__text: 0x58720
-  __TEXT.__gxf_code: 0x1098
+  __TEXT.__text: 0x58734
+  __TEXT.__gxf_code: 0x10ac
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__const: 0x14f0
   __TEXT._rtk_patchbay: 0x1d8
-  __TEXT.__gxf_shr_code: 0x54c
+  __TEXT.__gxf_shr_code: 0x558
   __TEXT.__cstring: 0x1ba5
   __TEXT.__constructor: 0x0
   __TEXT.__chain_starts: 0x0

   __DATA.__mod_init_func: 0x0
   __DATA._rtk_heap: 0x0
   __DATA.__zerofill: 0x666a0
-  UUID: 884B20EA-F58F-3639-B48F-C76A531860D4
+  UUID: 9AC4F9DD-CB9F-3004-9BA8-5E62322EFA50
   Functions: 0
   Symbols:   197
   CStrings:  200
CStrings:
+ "Dec 21 2023 00:12:46"
- "Nov 12 2023 06:36:09"

```

#### agx_b000

>  `agx_b000`

```diff

 
-  __TEXT.__text: 0x583f0
-  __TEXT.__gxf_code: 0x1098
+  __TEXT.__text: 0x58404
+  __TEXT.__gxf_code: 0x10ac
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__const: 0x1530
   __TEXT._rtk_patchbay: 0x1d8
-  __TEXT.__gxf_shr_code: 0x54c
+  __TEXT.__gxf_shr_code: 0x558
   __TEXT.__cstring: 0x1ba5
   __TEXT.__constructor: 0x0
   __TEXT.__chain_starts: 0x0

   __DATA.__mod_init_func: 0x0
   __DATA._rtk_heap: 0x0
   __DATA.__zerofill: 0x66520
-  UUID: C7C3A927-D5DE-36BB-AF33-9247BDFB97FE
+  UUID: AF086848-9935-388B-A7BA-0C33C8419E4D
   Functions: 0
   Symbols:   197
   CStrings:  200
CStrings:
+ "Dec 21 2023 00:13:17"
- "Nov 12 2023 06:36:40"

```

#### agx_b100

>  `agx_b100`

```diff

 
-  __TEXT.__text: 0x583f0
-  __TEXT.__gxf_code: 0x1098
+  __TEXT.__text: 0x58404
+  __TEXT.__gxf_code: 0x10ac
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__const: 0x1530
   __TEXT._rtk_patchbay: 0x1d8
-  __TEXT.__gxf_shr_code: 0x54c
+  __TEXT.__gxf_shr_code: 0x558
   __TEXT.__cstring: 0x1ba5
   __TEXT.__constructor: 0x0
   __TEXT.__chain_starts: 0x0

   __DATA.__mod_init_func: 0x0
   __DATA._rtk_heap: 0x0
   __DATA.__zerofill: 0x66520
-  UUID: 6EB8EF5C-384A-33A9-90D2-391E2D7CC553
+  UUID: 1154EFF1-245B-3D05-AE6B-112BBBA7BEF7
   Functions: 0
   Symbols:   197
   CStrings:  200
CStrings:
+ "Dec 21 2023 00:14:02"
- "Nov 12 2023 06:37:11"

```

#### ansf.t8130.release.im4p

>  `ansf.t8130.release.im4p`

```diff

 
   __TEXT.text_first: 0x44a0
-  __TEXT.__text: 0x16bf24
+  __TEXT.__text: 0x16bf48
   __TEXT.shared: 0xb7c8
   __TEXT.read: 0x5820
   __TEXT.__const: 0x8c48
CStrings:
+ "359.60.3~203"
+ "AppleStorageFirmwarePreASP3-359.60.3~203"
- "359.60.3~108"
- "AppleStorageFirmwarePreASP3-359.60.3~108"

```

#### aopfw-iphone16aop.im4p

>  `aopfw-iphone16aop.im4p`

```diff

 
-  __TEXT.__text: 0x14f5f4
-  __TEXT.__const: 0x11cb8
-  __TEXT.__cstring: 0x9e67
+  __TEXT.__text: 0x14fce8
+  __TEXT.__const: 0x11d08
+  __TEXT.__cstring: 0x9e68
   __TEXT.__chain_starts: 0x94
   __TEXT.__eh_frame: 0x7b8
   __DATA._rtk_boot: 0x2000

   __DATA.__version: 0x8
   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0xdd3b0
-  __ETEXT.__StaticInit: 0x8cd8
+  __DATA.__zerofill: 0xdd450
+  __ETEXT.__StaticInit: 0x8ce0
   __ETEXT.__text: 0x18428
   __ETEXT.__const: 0x726
   __OS_LOG.__string: 0x22e7a
   __MISC.__apf_list: 0xb0
-  __CMA.__cma_log_string: 0x3be2
-  UUID: F6C85399-C2FE-3F2B-B595-6B8CB22D8295
-  Functions: 4260
+  __CMA.__cma_log_string: 0x3e0c
+  UUID: F04F2303-EB65-3ACB-9053-EA9CF392B440
+  Functions: 4259
   Symbols:   0
   CStrings:  3496
 
CStrings:
+ "16:56:36"
+ "17:00:57"
+ "21D38"
+ "22:36:17"
+ "AppleSPUFirmware-1812.60.8~104"
+ "Dec 20 2023"
+ "SensingAlgsProx-43~531"
- "05:53:24"
- "06:05:38"
- "07:12:05"
- "21C51"
- "AppleSPUFirmware-1812.60.8~13"
- "Nov 12 2023"
- "SensingAlgsProx-43~356"

```

#### h16x_ane_fw_iaso_d8x.im4p

>  `h16x_ane_fw_iaso_d8x.im4p`

```diff

 
-  __TEXT.__text: 0xa41ac
+  __TEXT.__text: 0xa49c8
   __TEXT.__data_copy: 0x8000
   __TEXT.__const: 0x8388
-  __TEXT.__cstring: 0x1940a
+  __TEXT.__cstring: 0x19498
   __TEXT._rtk_mtab: 0x288
   __TEXT.__constructor: 0x0
   __TEXT.__chain_starts: 0x0

   __DATA.__mod_init_func: 0x0
   __DATA.__noinit: 0x0
   __DATA.__zerofill: 0x53f28
-  UUID: 7669AB7B-7B04-397B-8C01-30CACBA0FE47
+  UUID: 29D398D4-10B9-3F8E-BBB1-12DCEF1A0148
   Functions: 0
   Symbols:   0
-  CStrings:  3178
+  CStrings:  3182
 
CStrings:
+ "(allocSize + 1024) > allocSize"
+ "(tdSize + 1023) > tdSize"
+ "17:54:57"
+ "Dec 20 2023"
+ "pProg->builtinProgramId < ANE_NET_TOT"
+ "progList[index].builtinProgramId == ANE_NET_TOT"
- "06:52:52"
- "Nov 12 2023"

```

#### rans.t8130.release.im4p

>  `rans.t8130.release.im4p`

```diff

 
   __TEXT.text_first: 0x44a0
-  __TEXT.__text: 0x16bf24
+  __TEXT.__text: 0x16bf48
   __TEXT.shared: 0xb7c8
   __TEXT.read: 0x5820
   __TEXT.__const: 0x8c48
CStrings:
+ "359.60.3~203"
+ "AppleStorageFirmwarePreASP3-359.60.3~203"
- "359.60.3~108"
- "AppleStorageFirmwarePreASP3-359.60.3~108"

```

#### sptm.t8122.release.im4p

>  `sptm.t8122.release.im4p`

```diff

-184.62.5.0.0
-  __TEXT.__cstring: 0x9b69
+184.80.6.0.0
+  __TEXT.__cstring: 0x9b8d
   __TEXT.__binname: 0x40
   __TEXT.__chain_starts: 0x1c
   __TEXT.__const: 0x4a8
-  __DATA_CONST.__const: 0x4c548
-  __TEXT_EXEC.__text: 0x2f7cc
+  __DATA_CONST.__const: 0x4c550
+  __TEXT_EXEC.__text: 0x2f814
   __LAST.__pinst: 0x8
   __DATA.__data: 0x1a
   __DATA.__common: 0x6011
   __DATA.__bss: 0x4d08
   __BOOTDATA.__data: 0x14000
-  UUID: 95F64359-61B6-3691-8628-D270BB395746
+  UUID: 78626C2F-026E-3E92-9EA3-FD5348C20882
   Functions: 222
   Symbols:   1
-  CStrings:  1235
+  CStrings:  1236
 
CStrings:
+ "VIOLATION_UAT_ILLEGAL_ACTIVE_CTX_ID"

```

#### t8130dcp.im4p

>  `t8130dcp.im4p`

```diff

 
-  __TEXT.__text: 0x2a5900
-  __TEXT.__const: 0x7a620
-  __TEXT.__cstring: 0x2cf48
+  __TEXT.__text: 0x2a5dc0
+  __TEXT.__const: 0x7a7a8
+  __TEXT.__cstring: 0x2cf77
   __TEXT.__chain_starts: 0x15c
   __DATA.__constructor: 0x8
-  __DATA.__const: 0x46b48
+  __DATA.__const: 0x46bc8
   __DATA._rtk_patchbay: 0x6f4
   __DATA.__data: 0x2b8b8
   __DATA._rtk_boot: 0x5000

   __DATA.__mod_init_func: 0x90
   __DATA._afk_sys_objt: 0xb50
   __DATA._rtk_mtab: 0x5b0
-  __DATA.__zerofill: 0x9c800
-  __OS_LOG.__string: 0x1e6d4
-  UUID: E0D149D1-2D9D-3D4D-8A33-832B9913CB35
-  Functions: 6343
+  __DATA.__zerofill: 0x9c860
+  __OS_LOG.__string: 0x1e700
+  UUID: 3F3A9A18-70AF-366E-A16A-AAF59064A796
+  Functions: 6348
   Symbols:   0
-  CStrings:  5610
+  CStrings:  5611
 
CStrings:
+ "%s%c:%s:%u"
+ "ASSERT!%s:%d supports-alternative-target has wrong type"
+ "ASSERT!%s:%d table allocate fail"
+ "ASSERT!%s:%d tableSize 0"
+ "Failed to allocate targets pool"
+ "registerInterrupts"
- "%s%u:%s:%u"
- "ASSERT!%s:%d _table allocate fail"
- "ASSERT!%s:%d _tableSize 0"
- "IOMFB: PIODMA error, logging and quitting!!\n"
- "PIODMA error"

```

#### t8130pmp.im4p

>  `t8130pmp.im4p`

```diff

 
-  __TEXT.__text: 0x30774
+  __TEXT.__text: 0x3071c
   __TEXT.__const: 0x1b50
   __TEXT.__chain_starts: 0x0
   __TEXT.__cstring: 0x11c3
   __TEXT.__constructor: 0x0
   __TEXT._rtk_mtab: 0x5d0
   __DATA.__const: 0x1d28
-  __DATA.__data: 0x6c60
+  __DATA.__data: 0x6bc0
   __DATA._rtk_page_tables: 0x8000
   __DATA._rtk_boot: 0x1000
   __DATA._rtk_init_stack: 0x1800

   __DATA._rtk_power: 0x358
   __DATA.__mod_init_func: 0x18
   __DATA._rtk_heap: 0x0
-  __DATA.__zerofill: 0x47568
-  UUID: 9D27BFD6-0018-399B-B5B2-856DE469894E
+  __DATA.__zerofill: 0x47608
+  UUID: 457D2129-7089-3167-899A-BF4849518CBA
   Functions: 0
   Symbols:   0
   CStrings:  337

```


</details>

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 17.2.1 *(21C66)* | 617.1.17.10.9 |
| 17.3 *(21D50)* | 617.2.4.10.7 |

### Dylibs

#### 🆕 NEW (1)

- `/System/Library/NanoTimeKit/FaceBundles/NTKRhizomeFaceBundleCompanion.bundle/NTKRhizomeFaceBundleCompanion`

#### ❌ Removed (1)

- `/System/Library/PrivateFrameworks/HearingTest.framework/HearingTest`

#### ⬆️ Updated (3359)

<details>
  <summary><i>View Updated</i></summary>

- [/System/Library/AccessibilityBundles/ARKit.axbundle/ARKit](DYLIBS/ARKit.md)
- [/System/Library/AccessibilityBundles/ARTraceModule.axbundle/ARTraceModule](DYLIBS/ARTraceModule.md)
- [/System/Library/AccessibilityBundles/ASMessagesProvider.axbundle/ASMessagesProvider](DYLIBS/ASMessagesProvider.md)
- [/System/Library/AccessibilityBundles/AVFoundation.axbundle/AVFoundation](DYLIBS/AVFoundation.md)
- [/System/Library/AccessibilityBundles/AVKit.axbundle/AVKit](DYLIBS/AVKit.md)
- [/System/Library/AccessibilityBundles/AXActionSheetUIServer.axuiservice/AXActionSheetUIServer](DYLIBS/AXActionSheetUIServer.md)
- [/System/Library/AccessibilityBundles/AXSpeechImplementation.bundle/AXSpeechImplementation](DYLIBS/AXSpeechImplementation.md)
- [/System/Library/AccessibilityBundles/AccessibilitySettings.axbundle/AccessibilitySettings](DYLIBS/AccessibilitySettings.md)
- [/System/Library/AccessibilityBundles/AccessibilitySettingsLoader.bundle/AccessibilitySettingsLoader](DYLIBS/AccessibilitySettingsLoader.md)
- [/System/Library/AccessibilityBundles/AccountsUI.axbundle/AccountsUI](DYLIBS/AccountsUI.md)
- [/System/Library/AccessibilityBundles/AcousticId-Assistant.axbundle/AcousticId-Assistant](DYLIBS/AcousticId-Assistant.md)
- [/System/Library/AccessibilityBundles/ActionButtonSelector.axbundle/ActionButtonSelector](DYLIBS/ActionButtonSelector.md)
- [/System/Library/AccessibilityBundles/ActiveSyncSettings.axbundle/ActiveSyncSettings](DYLIBS/ActiveSyncSettings.md)
- [/System/Library/AccessibilityBundles/ActivityUIServices.axbundle/ActivityUIServices](DYLIBS/ActivityUIServices.md)
- [/System/Library/AccessibilityBundles/AddressBook-Assistant.axbundle/AddressBook-Assistant](DYLIBS/AddressBook-Assistant.md)
- [/System/Library/AccessibilityBundles/AddressBookUIFramework.axbundle/AddressBookUIFramework](DYLIBS/AddressBookUIFramework.md)
- [/System/Library/AccessibilityBundles/AirDrop.axbundle/AirDrop](DYLIBS/AirDrop.md)
- [/System/Library/AccessibilityBundles/AirDropUI.axbundle/AirDropUI](DYLIBS/AirDropUI.md)
- [/System/Library/AccessibilityBundles/AirPlayMirroringModule.axbundle/AirPlayMirroringModule](DYLIBS/AirPlayMirroringModule.md)
- [/System/Library/AccessibilityBundles/AirPortSettings.axbundle/AirPortSettings](DYLIBS/AirPortSettings.md)
- [/System/Library/AccessibilityBundles/AirTrafficSettings.axbundle/AirTrafficSettings](DYLIBS/AirTrafficSettings.md)
- [/System/Library/AccessibilityBundles/AmbientUI.axbundle/AmbientUI](DYLIBS/AmbientUI.md)
- [/System/Library/AccessibilityBundles/Animoji.axbundle/Animoji](DYLIBS/Animoji.md)
- [/System/Library/AccessibilityBundles/AnnotationKit.axbundle/AnnotationKit](DYLIBS/AnnotationKit.md)
- [/System/Library/AccessibilityBundles/AppInstallExtension.axbundle/AppInstallExtension](DYLIBS/AppInstallExtension.md)
- [/System/Library/AccessibilityBundles/AppPredictionUI.axbundle/AppPredictionUI](DYLIBS/AppPredictionUI.md)
- [/System/Library/AccessibilityBundles/AppPredictionUIWidget.axbundle/AppPredictionUIWidget](DYLIBS/AppPredictionUIWidget.md)
- [/System/Library/AccessibilityBundles/AppStore.axbundle/AppStore](DYLIBS/AppStore.md)
- [/System/Library/AccessibilityBundles/AppearanceModule.axbundle/AppearanceModule](DYLIBS/AppearanceModule.md)
- [/System/Library/AccessibilityBundles/AppleAccountSettings.axbundle/AppleAccountSettings](DYLIBS/AppleAccountSettings.md)
- [/System/Library/AccessibilityBundles/AppleAccountUI.axbundle/AppleAccountUI](DYLIBS/AppleAccountUI.md)
- [/System/Library/AccessibilityBundles/AppleMediaServicesUI.axbundle/AppleMediaServicesUI](DYLIBS/AppleMediaServicesUI.md)
- [/System/Library/AccessibilityBundles/AppleTV.axbundle/AppleTV](DYLIBS/AppleTV.md)
- [/System/Library/AccessibilityBundles/Arcade.axbundle/Arcade](DYLIBS/Arcade.md)
- [/System/Library/AccessibilityBundles/AssetExplorer.axbundle/AssetExplorer](DYLIBS/AssetExplorer.md)
- [/System/Library/AccessibilityBundles/AssetViewer.axbundle/AssetViewer](DYLIBS/AssetViewer.md)
- [/System/Library/AccessibilityBundles/AssistantServices.axbundle/AssistantServices](DYLIBS/AssistantServices.md)
- [/System/Library/AccessibilityBundles/AssistantUI.axbundle/AssistantUI](DYLIBS/AssistantUI.md)
- [/System/Library/AccessibilityBundles/AttributionWeeApp.axbundle/AttributionWeeApp](DYLIBS/AttributionWeeApp.md)
- [/System/Library/AccessibilityBundles/Audio-QuickLook.axbundle/Audio-QuickLook](DYLIBS/Audio-QuickLook.md)
- [/System/Library/AccessibilityBundles/AuthKitUI.axbundle/AuthKitUI](DYLIBS/AuthKitUI.md)
- [/System/Library/AccessibilityBundles/AuthenticationServices.axbundle/AuthenticationServices](DYLIBS/AuthenticationServices.md)
- [/System/Library/AccessibilityBundles/AvatarKit.axbundle/AvatarKit](DYLIBS/AvatarKit.md)
- [/System/Library/AccessibilityBundles/AvatarPickerMemojiPicker.axbundle/AvatarPickerMemojiPicker](DYLIBS/AvatarPickerMemojiPicker.md)
- [/System/Library/AccessibilityBundles/AvatarUI.axbundle/AvatarUI](DYLIBS/AvatarUI.md)
- [/System/Library/AccessibilityBundles/BPSStingSetup.axbundle/BPSStingSetup](DYLIBS/BPSStingSetup.md)
- [/System/Library/AccessibilityBundles/BackBoard.axbundle/BackBoard](DYLIBS/BackBoard.md)
- [/System/Library/AccessibilityBundles/BannerKit.axbundle/BannerKit](DYLIBS/BannerKit.md)
- [/System/Library/AccessibilityBundles/BarcodeScanner.axbundle/BarcodeScanner](DYLIBS/BarcodeScanner.md)
- [/System/Library/AccessibilityBundles/BaseBoardUI.axbundle/BaseBoardUI](DYLIBS/BaseBoardUI.md)
- [/System/Library/AccessibilityBundles/BatteryCenterUI.axbundle/BatteryCenterUI](DYLIBS/BatteryCenterUI.md)
- [/System/Library/AccessibilityBundles/BatteryUsageUI.axbundle/BatteryUsageUI](DYLIBS/BatteryUsageUI.md)
- [/System/Library/AccessibilityBundles/BatteryWidget.axbundle/BatteryWidget](DYLIBS/BatteryWidget.md)
- [/System/Library/AccessibilityBundles/BiometricKitUI.axbundle/BiometricKitUI](DYLIBS/BiometricKitUI.md)
- [/System/Library/AccessibilityBundles/BluetoothSettings.axbundle/BluetoothSettings](DYLIBS/BluetoothSettings.md)
- [/System/Library/AccessibilityBundles/Bridge.axbundle/Bridge](DYLIBS/Bridge.md)
- [/System/Library/AccessibilityBundles/BridgePreferences.axbundle/BridgePreferences](DYLIBS/BridgePreferences.md)
- [/System/Library/AccessibilityBundles/BridgeStoreExtension.axbundle/BridgeStoreExtension](DYLIBS/BridgeStoreExtension.md)
- [/System/Library/AccessibilityBundles/Business.axbundle/Business](DYLIBS/Business.md)
- [/System/Library/AccessibilityBundles/BusinessChatFramework.axbundle/BusinessChatFramework](DYLIBS/BusinessChatFramework.md)
- [/System/Library/AccessibilityBundles/CARDNDUI.axbundle/CARDNDUI](DYLIBS/CARDNDUI.md)
- [/System/Library/AccessibilityBundles/Calculator.axbundle/Calculator](DYLIBS/Calculator.md)
- [/System/Library/AccessibilityBundles/Calendar-Assistant.axbundle/Calendar-Assistant](DYLIBS/Calendar-Assistant.md)
- [/System/Library/AccessibilityBundles/Camera.axbundle/Camera](DYLIBS/Camera.md)
- [/System/Library/AccessibilityBundles/CameraEditKitFramework.axbundle/CameraEditKitFramework](DYLIBS/CameraEditKitFramework.md)
- [/System/Library/AccessibilityBundles/CameraEffectsKit.axbundle/CameraEffectsKit](DYLIBS/CameraEffectsKit.md)
- [/System/Library/AccessibilityBundles/CameraKit.axbundle/CameraKit](DYLIBS/CameraKit.md)
- [/System/Library/AccessibilityBundles/CameraUI.axbundle/CameraUI](DYLIBS/CameraUI.md)
- [/System/Library/AccessibilityBundles/CarModeModule.axbundle/CarModeModule](DYLIBS/CarModeModule.md)
- [/System/Library/AccessibilityBundles/CarPlay.axbundle/CarPlay](DYLIBS/CarPlay.md)
- [/System/Library/AccessibilityBundles/CardKit.axbundle/CardKit](DYLIBS/CardKit.md)
- [/System/Library/AccessibilityBundles/CarouselAppViewSettings.axbundle/CarouselAppViewSettings](DYLIBS/CarouselAppViewSettings.md)
- [/System/Library/AccessibilityBundles/CertInfo.axbundle/CertInfo](DYLIBS/CertInfo.md)
- [/System/Library/AccessibilityBundles/ChargingViewService.axbundle/ChargingViewService](DYLIBS/ChargingViewService.md)
- [/System/Library/AccessibilityBundles/ChatKitAssistantUI-Assistant.axbundle/ChatKitAssistantUI-Assistant](DYLIBS/ChatKitAssistantUI-Assistant.md)
- [/System/Library/AccessibilityBundles/ChatKitFramework.axbundle/ChatKitFramework](DYLIBS/ChatKitFramework.md)
- [/System/Library/AccessibilityBundles/CheckerBoard.axbundle/CheckerBoard](DYLIBS/CheckerBoard.md)
- [/System/Library/AccessibilityBundles/ChronoCore.axbundle/ChronoCore](DYLIBS/ChronoCore.md)
- [/System/Library/AccessibilityBundles/ClipUIServices.axbundle/ClipUIServices](DYLIBS/ClipUIServices.md)
- [/System/Library/AccessibilityBundles/ClockPoster.axbundle/ClockPoster](DYLIBS/ClockPoster.md)
- [/System/Library/AccessibilityBundles/CommunicationsSetupUI.axbundle/CommunicationsSetupUI](DYLIBS/CommunicationsSetupUI.md)
- [/System/Library/AccessibilityBundles/CompanionAppViewSetup.axbundle/CompanionAppViewSetup](DYLIBS/CompanionAppViewSetup.md)
- [/System/Library/AccessibilityBundles/CompanionStingSettings.axbundle/CompanionStingSettings](DYLIBS/CompanionStingSettings.md)
- [/System/Library/AccessibilityBundles/Compass.axbundle/Compass](DYLIBS/Compass.md)
- [/System/Library/AccessibilityBundles/CompassViewCalibrationService.axbundle/CompassViewCalibrationService](DYLIBS/CompassViewCalibrationService.md)
- [/System/Library/AccessibilityBundles/ConnectivityModule.axbundle/ConnectivityModule](DYLIBS/ConnectivityModule.md)
- [/System/Library/AccessibilityBundles/ContactsAutocompleteUI.axbundle/ContactsAutocompleteUI](DYLIBS/ContactsAutocompleteUI.md)
- [/System/Library/AccessibilityBundles/ContactsUI.axbundle/ContactsUI](DYLIBS/ContactsUI.md)
- [/System/Library/AccessibilityBundles/ContinuityDisplay.axbundle/ContinuityDisplay](DYLIBS/ContinuityDisplay.md)
- [/System/Library/AccessibilityBundles/ControlCenterUI.axbundle/ControlCenterUI](DYLIBS/ControlCenterUI.md)
- [/System/Library/AccessibilityBundles/ControlCenterUIKit.axbundle/ControlCenterUIKit](DYLIBS/ControlCenterUIKit.md)
- [/System/Library/AccessibilityBundles/ConversationKit.axbundle/ConversationKit](DYLIBS/ConversationKit.md)
- [/System/Library/AccessibilityBundles/CoreAuthUI.axbundle/CoreAuthUI](DYLIBS/CoreAuthUI.md)
- [/System/Library/AccessibilityBundles/CoreCDPUI.axbundle/CoreCDPUI](DYLIBS/CoreCDPUI.md)
- [/System/Library/AccessibilityBundles/CoreDynamicUIPlugin.axbundle/CoreDynamicUIPlugin](DYLIBS/CoreDynamicUIPlugin.md)
- [/System/Library/AccessibilityBundles/CoreIDVRGBLiveness.axbundle/CoreIDVRGBLiveness](DYLIBS/CoreIDVRGBLiveness.md)
- [/System/Library/AccessibilityBundles/CoreIDVUI.axbundle/CoreIDVUI](DYLIBS/CoreIDVUI.md)
- [/System/Library/AccessibilityBundles/CoreRecognition.axbundle/CoreRecognition](DYLIBS/CoreRecognition.md)
- [/System/Library/AccessibilityBundles/CoreSuggestionsUI.axbundle/CoreSuggestionsUI](DYLIBS/CoreSuggestionsUI.md)
- [/System/Library/AccessibilityBundles/CoverSheet.axbundle/CoverSheet](DYLIBS/CoverSheet.md)
- [/System/Library/AccessibilityBundles/CoverSheetKit.axbundle/CoverSheetKit](DYLIBS/CoverSheetKit.md)
- [/System/Library/AccessibilityBundles/DDActionsService.axbundle/DDActionsService](DYLIBS/DDActionsService.md)
- [/System/Library/AccessibilityBundles/DataActivation.axbundle/DataActivation](DYLIBS/DataActivation.md)
- [/System/Library/AccessibilityBundles/DefaultMediaPlayer-QuickLook.axbundle/DefaultMediaPlayer-QuickLook](DYLIBS/DefaultMediaPlayer-QuickLook.md)
- [/System/Library/AccessibilityBundles/Diagnostics.axbundle/Diagnostics](DYLIBS/Diagnostics.md)
- [/System/Library/AccessibilityBundles/DictionarySettings.axbundle/DictionarySettings](DYLIBS/DictionarySettings.md)
- [/System/Library/AccessibilityBundles/DigitalSeparationSettings.axbundle/DigitalSeparationSettings](DYLIBS/DigitalSeparationSettings.md)
- [/System/Library/AccessibilityBundles/DigitalTouchBalloonProvider.axbundle/DigitalTouchBalloonProvider](DYLIBS/DigitalTouchBalloonProvider.md)
- [/System/Library/AccessibilityBundles/DigitalTouchShared.axbundle/DigitalTouchShared](DYLIBS/DigitalTouchShared.md)
- [/System/Library/AccessibilityBundles/DisplayAndBrightnessSettings.axbundle/DisplayAndBrightnessSettings](DYLIBS/DisplayAndBrightnessSettings.md)
- [/System/Library/AccessibilityBundles/DisplayModule.axbundle/DisplayModule](DYLIBS/DisplayModule.md)
- [/System/Library/AccessibilityBundles/DoNotDisturbModule.axbundle/DoNotDisturbModule](DYLIBS/DoNotDisturbModule.md)
- [/System/Library/AccessibilityBundles/DoNotDisturbSettings.axbundle/DoNotDisturbSettings](DYLIBS/DoNotDisturbSettings.md)
- [/System/Library/AccessibilityBundles/DocumentManager.axbundle/DocumentManager](DYLIBS/DocumentManager.md)
- [/System/Library/AccessibilityBundles/DocumentManagerExecutables.axbundle/DocumentManagerExecutables](DYLIBS/DocumentManagerExecutables.md)
- [/System/Library/AccessibilityBundles/DocumentManagerUICore.axbundle/DocumentManagerUICore](DYLIBS/DocumentManagerUICore.md)
- [/System/Library/AccessibilityBundles/DrawingKit.axbundle/DrawingKit](DYLIBS/DrawingKit.md)
- [/System/Library/AccessibilityBundles/EmojiKit.axbundle/EmojiKit](DYLIBS/EmojiKit.md)
- [/System/Library/AccessibilityBundles/EventKitUIFramework.axbundle/EventKitUIFramework](DYLIBS/EventKitUIFramework.md)
- [/System/Library/AccessibilityBundles/ExposureNotificationSettingsUI.axbundle/ExposureNotificationSettingsUI](DYLIBS/ExposureNotificationSettingsUI.md)
- [/System/Library/AccessibilityBundles/FMFindingUI.axbundle/FMFindingUI](DYLIBS/FMFindingUI.md)
- [/System/Library/AccessibilityBundles/FaceTime.axbundle/FaceTime](DYLIBS/FaceTime.md)
- [/System/Library/AccessibilityBundles/FacebookSettings.axbundle/FacebookSettings](DYLIBS/FacebookSettings.md)
- [/System/Library/AccessibilityBundles/Files.axbundle/Files](DYLIBS/Files.md)
- [/System/Library/AccessibilityBundles/FindMy.axbundle/FindMy](DYLIBS/FindMy.md)
- [/System/Library/AccessibilityBundles/FlashlightModule.axbundle/FlashlightModule](DYLIBS/FlashlightModule.md)
- [/System/Library/AccessibilityBundles/FlightUtilities.axbundle/FlightUtilities](DYLIBS/FlightUtilities.md)
- [/System/Library/AccessibilityBundles/FocusUI.axbundle/FocusUI](DYLIBS/FocusUI.md)
- [/System/Library/AccessibilityBundles/FocusUIModule.axbundle/FocusUIModule](DYLIBS/FocusUIModule.md)
- [/System/Library/AccessibilityBundles/FontPicker.axbundle/FontPicker](DYLIBS/FontPicker.md)
- [/System/Library/AccessibilityBundles/FrontBoard.axbundle/FrontBoard](DYLIBS/FrontBoard.md)
- [/System/Library/AccessibilityBundles/Game Center.axbundle/Game Center](DYLIBS/Game_Center.md)
- [/System/Library/AccessibilityBundles/GameCenterDashboardExtension.axbundle/GameCenterDashboardExtension](DYLIBS/GameCenterDashboardExtension.md)
- [/System/Library/AccessibilityBundles/GameCenterPrivateUIFramework.axbundle/GameCenterPrivateUIFramework](DYLIBS/GameCenterPrivateUIFramework.md)
- [/System/Library/AccessibilityBundles/GameCenterUIFramework.axbundle/GameCenterUIFramework](DYLIBS/GameCenterUIFramework.md)
- [/System/Library/AccessibilityBundles/GameCenterUIService.axbundle/GameCenterUIService](DYLIBS/GameCenterUIService.md)
- [/System/Library/AccessibilityBundles/GameKitFramework.axbundle/GameKitFramework](DYLIBS/GameKitFramework.md)
- [/System/Library/AccessibilityBundles/GeneralKnowledge-Assistant.axbundle/GeneralKnowledge-Assistant](DYLIBS/GeneralKnowledge-Assistant.md)
- [/System/Library/AccessibilityBundles/GeneralSettingsUI.axbundle/GeneralSettingsUI](DYLIBS/GeneralSettingsUI.md)
- [/System/Library/AccessibilityBundles/GeoServices.axbundle/GeoServices](DYLIBS/GeoServices.md)
- [/System/Library/AccessibilityBundles/Gif-QuickLook.axbundle/Gif-QuickLook](DYLIBS/Gif-QuickLook.md)
- [/System/Library/AccessibilityBundles/HDSViewService.axbundle/HDSViewService](DYLIBS/HDSViewService.md)
- [/System/Library/AccessibilityBundles/HandwritingProvider.axbundle/HandwritingProvider](DYLIBS/HandwritingProvider.md)
- [/System/Library/AccessibilityBundles/HashtagImagesExtension.axbundle/HashtagImagesExtension](DYLIBS/HashtagImagesExtension.md)
- [/System/Library/AccessibilityBundles/HeadphoneConfigs.axbundle/HeadphoneConfigs](DYLIBS/HeadphoneConfigs.md)
- [/System/Library/AccessibilityBundles/HealthArticlesUI.axbundle/HealthArticlesUI](DYLIBS/HealthArticlesUI.md)
- [/System/Library/AccessibilityBundles/HealthExperienceUI.axbundle/HealthExperienceUI](DYLIBS/HealthExperienceUI.md)
- [/System/Library/AccessibilityBundles/HealthExposureNotificationUI.axbundle/HealthExposureNotificationUI](DYLIBS/HealthExposureNotificationUI.md)
- [/System/Library/AccessibilityBundles/HealthKit.axbundle/HealthKit](DYLIBS/HealthKit.md)
- [/System/Library/AccessibilityBundles/HealthKitUI.axbundle/HealthKitUI](DYLIBS/HealthKitUI.md)
- [/System/Library/AccessibilityBundles/HealthMedicationsUI.axbundle/HealthMedicationsUI](DYLIBS/HealthMedicationsUI.md)
- [/System/Library/AccessibilityBundles/HealthRecordsUI.axbundle/HealthRecordsUI](DYLIBS/HealthRecordsUI.md)
- [/System/Library/AccessibilityBundles/HealthSafety.axbundle/HealthSafety](DYLIBS/HealthSafety.md)
- [/System/Library/AccessibilityBundles/HealthToolbox.axbundle/HealthToolbox](DYLIBS/HealthToolbox.md)
- [/System/Library/AccessibilityBundles/HealthUI.axbundle/HealthUI](DYLIBS/HealthUI.md)
- [/System/Library/AccessibilityBundles/HealthVisualization.axbundle/HealthVisualization](DYLIBS/HealthVisualization.md)
- [/System/Library/AccessibilityBundles/HearingAidUIServer.axuiservice/HearingAidUIServer](DYLIBS/HearingAidUIServer.md)
- [/System/Library/AccessibilityBundles/HeartRhythmUI.axbundle/HeartRhythmUI](DYLIBS/HeartRhythmUI.md)
- [/System/Library/AccessibilityBundles/HelpKit.axbundle/HelpKit](DYLIBS/HelpKit.md)
- [/System/Library/AccessibilityBundles/Home.axbundle/Home](DYLIBS/Home.md)
- [/System/Library/AccessibilityBundles/HomeControlCenterCompactModule.axbundle/HomeControlCenterCompactModule](DYLIBS/HomeControlCenterCompactModule.md)
- [/System/Library/AccessibilityBundles/HomeControlCenterModule.axbundle/HomeControlCenterModule](DYLIBS/HomeControlCenterModule.md)
- [/System/Library/AccessibilityBundles/HomeUI.axbundle/HomeUI](DYLIBS/HomeUI.md)
- [/System/Library/AccessibilityBundles/HomeUIService.axbundle/HomeUIService](DYLIBS/HomeUIService.md)
- [/System/Library/AccessibilityBundles/Image-QuickLook.axbundle/Image-QuickLook](DYLIBS/Image-QuickLook.md)
- [/System/Library/AccessibilityBundles/InCallLockScreen.axbundle/InCallLockScreen](DYLIBS/InCallLockScreen.md)
- [/System/Library/AccessibilityBundles/InCallService.axbundle/InCallService](DYLIBS/InCallService.md)
- [/System/Library/AccessibilityBundles/IncomingCall.axbundle/IncomingCall](DYLIBS/IncomingCall.md)
- [/System/Library/AccessibilityBundles/InputUI.axbundle/InputUI](DYLIBS/InputUI.md)
- [/System/Library/AccessibilityBundles/IntentsUI.axbundle/IntentsUI](DYLIBS/IntentsUI.md)
- [/System/Library/AccessibilityBundles/InternationalSettings.axbundle/InternationalSettings](DYLIBS/InternationalSettings.md)
- [/System/Library/AccessibilityBundles/KeyboardSettings.axbundle/KeyboardSettings](DYLIBS/KeyboardSettings.md)
- [/System/Library/AccessibilityBundles/LinkPresentation.axbundle/LinkPresentation](DYLIBS/LinkPresentation.md)
- [/System/Library/AccessibilityBundles/LiveTranscriptionUI.axbundle/LiveTranscriptionUI](DYLIBS/LiveTranscriptionUI.md)
- [/System/Library/AccessibilityBundles/LocalAuthenticationRGBCapture.axbundle/LocalAuthenticationRGBCapture](DYLIBS/LocalAuthenticationRGBCapture.md)
- [/System/Library/AccessibilityBundles/LocalAuthenticationUI.axbundle/LocalAuthenticationUI](DYLIBS/LocalAuthenticationUI.md)
- [/System/Library/AccessibilityBundles/LoginUI.axbundle/LoginUI](DYLIBS/LoginUI.md)
- [/System/Library/AccessibilityBundles/Mail-Assistant.axbundle/Mail-Assistant](DYLIBS/Mail-Assistant.md)
- [/System/Library/AccessibilityBundles/MailAttachmentPlugin.axbundle/MailAttachmentPlugin](DYLIBS/MailAttachmentPlugin.md)
- [/System/Library/AccessibilityBundles/MailVIPWidget.axbundle/MailVIPWidget](DYLIBS/MailVIPWidget.md)
- [/System/Library/AccessibilityBundles/ManagedConfigurationUI.axbundle/ManagedConfigurationUI](DYLIBS/ManagedConfigurationUI.md)
- [/System/Library/AccessibilityBundles/MapKitFramework.axbundle/MapKitFramework](DYLIBS/MapKitFramework.md)
- [/System/Library/AccessibilityBundles/MapKitSwiftUI.axbundle/MapKitSwiftUI](DYLIBS/MapKitSwiftUI.md)
- [/System/Library/AccessibilityBundles/Maps-Assistant.axbundle/Maps-Assistant](DYLIBS/Maps-Assistant.md)
- [/System/Library/AccessibilityBundles/Maps.axbundle/Maps](DYLIBS/Maps.md)
- [/System/Library/AccessibilityBundles/MapsUI.axbundle/MapsUI](DYLIBS/MapsUI.md)
- [/System/Library/AccessibilityBundles/MarkupUI.axbundle/MarkupUI](DYLIBS/MarkupUI.md)
- [/System/Library/AccessibilityBundles/Measure.axbundle/Measure](DYLIBS/Measure.md)
- [/System/Library/AccessibilityBundles/MediaControls.axbundle/MediaControls](DYLIBS/MediaControls.md)
- [/System/Library/AccessibilityBundles/MediaPlayerFramework.axbundle/MediaPlayerFramework](DYLIBS/MediaPlayerFramework.md)
- [/System/Library/AccessibilityBundles/MediaPlayerUIFramework.axbundle/MediaPlayerUIFramework](DYLIBS/MediaPlayerUIFramework.md)
- [/System/Library/AccessibilityBundles/MedicationsHealthAppPlugin.axbundle/MedicationsHealthAppPlugin](DYLIBS/MedicationsHealthAppPlugin.md)
- [/System/Library/AccessibilityBundles/Memories.axbundle/Memories](DYLIBS/Memories.md)
- [/System/Library/AccessibilityBundles/MenstrualCyclesAppPlugin.axbundle/MenstrualCyclesAppPlugin](DYLIBS/MenstrualCyclesAppPlugin.md)
- [/System/Library/AccessibilityBundles/MessageUIFramework.axbundle/MessageUIFramework](DYLIBS/MessageUIFramework.md)
- [/System/Library/AccessibilityBundles/Messages.axbundle/Messages](DYLIBS/Messages.md)
- [/System/Library/AccessibilityBundles/MessagesFlowDelegatePlugin.axbundle/MessagesFlowDelegatePlugin](DYLIBS/MessagesFlowDelegatePlugin.md)
- [/System/Library/AccessibilityBundles/MobileCal.axbundle/MobileCal](DYLIBS/MobileCal.md)
- [/System/Library/AccessibilityBundles/MobileMail.axbundle/MobileMail](DYLIBS/MobileMail.md)
- [/System/Library/AccessibilityBundles/MobileMailSettings.axbundle/MobileMailSettings](DYLIBS/MobileMailSettings.md)
- [/System/Library/AccessibilityBundles/MobilePhone.axbundle/MobilePhone](DYLIBS/MobilePhone.md)
- [/System/Library/AccessibilityBundles/MobileSMS.axbundle/MobileSMS](DYLIBS/MobileSMS.md)
- [/System/Library/AccessibilityBundles/MobileSafari.axbundle/MobileSafari](DYLIBS/MobileSafari.md)
- [/System/Library/AccessibilityBundles/MobileSafariFramework.axbundle/MobileSafariFramework](DYLIBS/MobileSafariFramework.md)
- [/System/Library/AccessibilityBundles/MobileSafariSettings.axbundle/MobileSafariSettings](DYLIBS/MobileSafariSettings.md)
- [/System/Library/AccessibilityBundles/MobileSafariUI.axbundle/MobileSafariUI](DYLIBS/MobileSafariUI.md)
- [/System/Library/AccessibilityBundles/MobileSlideShow.axbundle/MobileSlideShow](DYLIBS/MobileSlideShow.md)
- [/System/Library/AccessibilityBundles/MobileStore.axbundle/MobileStore](DYLIBS/MobileStore.md)
- [/System/Library/AccessibilityBundles/MobileStoreUI.axbundle/MobileStoreUI](DYLIBS/MobileStoreUI.md)
- [/System/Library/AccessibilityBundles/MobileTimer-Assistant.axbundle/MobileTimer-Assistant](DYLIBS/MobileTimer-Assistant.md)
- [/System/Library/AccessibilityBundles/MobileTimer.axbundle/MobileTimer](DYLIBS/MobileTimer.md)
- [/System/Library/AccessibilityBundles/MobileTimerFramework.axbundle/MobileTimerFramework](DYLIBS/MobileTimerFramework.md)
- [/System/Library/AccessibilityBundles/MobileTimerUIFramework.axbundle/MobileTimerUIFramework](DYLIBS/MobileTimerUIFramework.md)
- [/System/Library/AccessibilityBundles/Moments.axbundle/Moments](DYLIBS/Moments.md)
- [/System/Library/AccessibilityBundles/MonogramPosterExtension.axbundle/MonogramPosterExtension](DYLIBS/MonogramPosterExtension.md)
- [/System/Library/AccessibilityBundles/Movie-QuickLook.axbundle/Movie-QuickLook](DYLIBS/Movie-QuickLook.md)
- [/System/Library/AccessibilityBundles/Movies-Assistant.axbundle/Movies-Assistant](DYLIBS/Movies-Assistant.md)
- [/System/Library/AccessibilityBundles/MusicApplication.axbundle/MusicApplication](DYLIBS/MusicApplication.md)
- [/System/Library/AccessibilityBundles/MusicMessagesApp.axbundle/MusicMessagesApp](DYLIBS/MusicMessagesApp.md)
- [/System/Library/AccessibilityBundles/MusicRecognition.axbundle/MusicRecognition](DYLIBS/MusicRecognition.md)
- [/System/Library/AccessibilityBundles/MusicSettings.axbundle/MusicSettings](DYLIBS/MusicSettings.md)
- [/System/Library/AccessibilityBundles/MusicUI.axbundle/MusicUI](DYLIBS/MusicUI.md)
- [/System/Library/AccessibilityBundles/MusicUsage.axbundle/MusicUsage](DYLIBS/MusicUsage.md)
- [/System/Library/AccessibilityBundles/MuteModule.axbundle/MuteModule](DYLIBS/MuteModule.md)
- [/System/Library/AccessibilityBundles/NFCControlCenterModule.axbundle/NFCControlCenterModule](DYLIBS/NFCControlCenterModule.md)
- [/System/Library/AccessibilityBundles/Nearby.axbundle/Nearby](DYLIBS/Nearby.md)
- [/System/Library/AccessibilityBundles/NotificationCenter.axbundle/NotificationCenter](DYLIBS/NotificationCenter.md)
- [/System/Library/AccessibilityBundles/NotificationsSettings.axbundle/NotificationsSettings](DYLIBS/NotificationsSettings.md)
- [/System/Library/AccessibilityBundles/OnBoardingKit.axbundle/OnBoardingKit](DYLIBS/OnBoardingKit.md)
- [/System/Library/AccessibilityBundles/OpusKit.axbundle/OpusKit](DYLIBS/OpusKit.md)
- [/System/Library/AccessibilityBundles/OrientationLockModule.axbundle/OrientationLockModule](DYLIBS/OrientationLockModule.md)
- [/System/Library/AccessibilityBundles/PDFKit.axbundle/PDFKit](DYLIBS/PDFKit.md)
- [/System/Library/AccessibilityBundles/PaperKit.axbundle/PaperKit](DYLIBS/PaperKit.md)
- [/System/Library/AccessibilityBundles/PassKitFramework.axbundle/PassKitFramework](DYLIBS/PassKitFramework.md)
- [/System/Library/AccessibilityBundles/PassKitUI.axbundle/PassKitUI](DYLIBS/PassKitUI.md)
- [/System/Library/AccessibilityBundles/PassesLockScreenPlugin.axbundle/PassesLockScreenPlugin](DYLIBS/PassesLockScreenPlugin.md)
- [/System/Library/AccessibilityBundles/PeerPaymentMessagesExtension.axbundle/PeerPaymentMessagesExtension](DYLIBS/PeerPaymentMessagesExtension.md)
- [/System/Library/AccessibilityBundles/Pegasus.axbundle/Pegasus](DYLIBS/Pegasus.md)
- [/System/Library/AccessibilityBundles/PencilKit.axbundle/PencilKit](DYLIBS/PencilKit.md)
- [/System/Library/AccessibilityBundles/PerformanceTraceModule.axbundle/PerformanceTraceModule](DYLIBS/PerformanceTraceModule.md)
- [/System/Library/AccessibilityBundles/PhoneCallFlowDelegatePlugin.axbundle/PhoneCallFlowDelegatePlugin](DYLIBS/PhoneCallFlowDelegatePlugin.md)
- [/System/Library/AccessibilityBundles/Photo Booth.axbundle/Photo Booth](DYLIBS/Photo_Booth.md)
- [/System/Library/AccessibilityBundles/PhotoLibraryFramework.axbundle/PhotoLibraryFramework](DYLIBS/PhotoLibraryFramework.md)
- [/System/Library/AccessibilityBundles/PhotoLibraryServices.axbundle/PhotoLibraryServices](DYLIBS/PhotoLibraryServices.md)
- [/System/Library/AccessibilityBundles/PhotosEditUI.axbundle/PhotosEditUI](DYLIBS/PhotosEditUI.md)
- [/System/Library/AccessibilityBundles/PhotosFramework.axbundle/PhotosFramework](DYLIBS/PhotosFramework.md)
- [/System/Library/AccessibilityBundles/PhotosUICore.axbundle/PhotosUICore](DYLIBS/PhotosUICore.md)
- [/System/Library/AccessibilityBundles/PhotosUIFramework.axbundle/PhotosUIFramework](DYLIBS/PhotosUIFramework.md)
- [/System/Library/AccessibilityBundles/PlatterKit.axbundle/PlatterKit](DYLIBS/PlatterKit.md)
- [/System/Library/AccessibilityBundles/Podcasts.axbundle/Podcasts](DYLIBS/Podcasts.md)
- [/System/Library/AccessibilityBundles/PodcastsPodcastsTodayExtension.axbundle/PodcastsPodcastsTodayExtension](DYLIBS/PodcastsPodcastsTodayExtension.md)
- [/System/Library/AccessibilityBundles/PosterBoard.axbundle/PosterBoard](DYLIBS/PosterBoard.md)
- [/System/Library/AccessibilityBundles/PosterBoardFramework.axbundle/PosterBoardFramework](DYLIBS/PosterBoardFramework.md)
- [/System/Library/AccessibilityBundles/PosterKit.axbundle/PosterKit](DYLIBS/PosterKit.md)
- [/System/Library/AccessibilityBundles/PreBoard.axbundle/PreBoard](DYLIBS/PreBoard.md)
- [/System/Library/AccessibilityBundles/Preferences.axbundle/Preferences](DYLIBS/Preferences.md)
- [/System/Library/AccessibilityBundles/PreferencesFramework.axbundle/PreferencesFramework](DYLIBS/PreferencesFramework.md)
- [/System/Library/AccessibilityBundles/PreferencesUI.axbundle/PreferencesUI](DYLIBS/PreferencesUI.md)
- [/System/Library/AccessibilityBundles/PreviewUI.axbundle/PreviewUI](DYLIBS/PreviewUI.md)
- [/System/Library/AccessibilityBundles/PrintKitUI.axbundle/PrintKitUI](DYLIBS/PrintKitUI.md)
- [/System/Library/AccessibilityBundles/PrivacySettingsUI.axbundle/PrivacySettingsUI](DYLIBS/PrivacySettingsUI.md)
- [/System/Library/AccessibilityBundles/ProductPageExtension.axbundle/ProductPageExtension](DYLIBS/ProductPageExtension.md)
- [/System/Library/AccessibilityBundles/ProxCardKit.axbundle/ProxCardKit](DYLIBS/ProxCardKit.md)
- [/System/Library/AccessibilityBundles/QuickLook.axbundle/QuickLook](DYLIBS/QuickLook.md)
- [/System/Library/AccessibilityBundles/QuickSpeak.bundle/QuickSpeak](DYLIBS/QuickSpeak.md)
- [/System/Library/AccessibilityBundles/QuickTime Plugin.axbundle/QuickTime Plugin](DYLIBS/QuickTime_Plugin.md)
- [/System/Library/AccessibilityBundles/RealityFoundation.axbundle/RealityFoundation](DYLIBS/RealityFoundation.md)
- [/System/Library/AccessibilityBundles/RealityKit.axbundle/RealityKit](DYLIBS/RealityKit.md)
- [/System/Library/AccessibilityBundles/RecentlyPlayedTodayExtension.axbundle/RecentlyPlayedTodayExtension](DYLIBS/RecentlyPlayedTodayExtension.md)
- [/System/Library/AccessibilityBundles/RecentsAvocado.axbundle/RecentsAvocado](DYLIBS/RecentsAvocado.md)
- [/System/Library/AccessibilityBundles/RemoteUIFramework.axbundle/RemoteUIFramework](DYLIBS/RemoteUIFramework.md)
- [/System/Library/AccessibilityBundles/ReplayKitModule.axbundle/ReplayKitModule](DYLIBS/ReplayKitModule.md)
- [/System/Library/AccessibilityBundles/Restaurants-Assistant.axbundle/Restaurants-Assistant](DYLIBS/Restaurants-Assistant.md)
- [/System/Library/AccessibilityBundles/SIMSetupSupport.axbundle/SIMSetupSupport](DYLIBS/SIMSetupSupport.md)
- [/System/Library/AccessibilityBundles/SIMSetupUIService.axbundle/SIMSetupUIService](DYLIBS/SIMSetupUIService.md)
- [/System/Library/AccessibilityBundles/SOSSettings.axbundle/SOSSettings](DYLIBS/SOSSettings.md)
- [/System/Library/AccessibilityBundles/SafariServices.axbundle/SafariServices](DYLIBS/SafariServices.md)
- [/System/Library/AccessibilityBundles/SafariSharedUI.axbundle/SafariSharedUI](DYLIBS/SafariSharedUI.md)
- [/System/Library/AccessibilityBundles/SaveToFiles.axbundle/SaveToFiles](DYLIBS/SaveToFiles.md)
- [/System/Library/AccessibilityBundles/SceneKit.axbundle/SceneKit](DYLIBS/SceneKit.md)
- [/System/Library/AccessibilityBundles/ScreenTimeSettingsUI.axbundle/ScreenTimeSettingsUI](DYLIBS/ScreenTimeSettingsUI.md)
- [/System/Library/AccessibilityBundles/ScreenTimeUI.axbundle/ScreenTimeUI](DYLIBS/ScreenTimeUI.md)
- [/System/Library/AccessibilityBundles/ScreenshotServicesFramework.axbundle/ScreenshotServicesFramework](DYLIBS/ScreenshotServicesFramework.md)
- [/System/Library/AccessibilityBundles/ScreenshotServicesService.axbundle/ScreenshotServicesService](DYLIBS/ScreenshotServicesService.md)
- [/System/Library/AccessibilityBundles/SearchFoundation.axbundle/SearchFoundation](DYLIBS/SearchFoundation.md)
- [/System/Library/AccessibilityBundles/SearchSettings.axbundle/SearchSettings](DYLIBS/SearchSettings.md)
- [/System/Library/AccessibilityBundles/SearchUI.axbundle/SearchUI](DYLIBS/SearchUI.md)
- [/System/Library/AccessibilityBundles/Settings-Assistant.axbundle/Settings-Assistant](DYLIBS/Settings-Assistant.md)
- [/System/Library/AccessibilityBundles/Setup.axbundle/Setup](DYLIBS/Setup.md)
- [/System/Library/AccessibilityBundles/SetupAssistantUI.axbundle/SetupAssistantUI](DYLIBS/SetupAssistantUI.md)
- [/System/Library/AccessibilityBundles/SeymourUI.axbundle/SeymourUI](DYLIBS/SeymourUI.md)
- [/System/Library/AccessibilityBundles/ShareSheet.axbundle/ShareSheet](DYLIBS/ShareSheet.md)
- [/System/Library/AccessibilityBundles/SharedWithYouFramework.axbundle/SharedWithYouFramework](DYLIBS/SharedWithYouFramework.md)
- [/System/Library/AccessibilityBundles/SharingUI.axbundle/SharingUI](DYLIBS/SharingUI.md)
- [/System/Library/AccessibilityBundles/SharingViewService.axbundle/SharingViewService](DYLIBS/SharingViewService.md)
- [/System/Library/AccessibilityBundles/Shortcuts.axbundle/Shortcuts](DYLIBS/Shortcuts.md)
- [/System/Library/AccessibilityBundles/ShortcutsUI.axbundle/ShortcutsUI](DYLIBS/ShortcutsUI.md)
- [/System/Library/AccessibilityBundles/Sidecar.axbundle/Sidecar](DYLIBS/Sidecar.md)
- [/System/Library/AccessibilityBundles/Siri.axbundle/Siri](DYLIBS/Siri.md)
- [/System/Library/AccessibilityBundles/SiriActivation.axbundle/SiriActivation](DYLIBS/SiriActivation.md)
- [/System/Library/AccessibilityBundles/SiriKitRuntime.axbundle/SiriKitRuntime](DYLIBS/SiriKitRuntime.md)
- [/System/Library/AccessibilityBundles/SiriSharedUI.axbundle/SiriSharedUI](DYLIBS/SiriSharedUI.md)
- [/System/Library/AccessibilityBundles/SiriUI.axbundle/SiriUI](DYLIBS/SiriUI.md)
- [/System/Library/AccessibilityBundles/SiriUICore.axbundle/SiriUICore](DYLIBS/SiriUICore.md)
- [/System/Library/AccessibilityBundles/Siriland.axbundle/Siriland](DYLIBS/Siriland.md)
- [/System/Library/AccessibilityBundles/SleepHealthAppPlugin.axbundle/SleepHealthAppPlugin](DYLIBS/SleepHealthAppPlugin.md)
- [/System/Library/AccessibilityBundles/SleepHealthUI.axbundle/SleepHealthUI](DYLIBS/SleepHealthUI.md)
- [/System/Library/AccessibilityBundles/SocialFramework.axbundle/SocialFramework](DYLIBS/SocialFramework.md)
- [/System/Library/AccessibilityBundles/SocialLayer.axbundle/SocialLayer](DYLIBS/SocialLayer.md)
- [/System/Library/AccessibilityBundles/SocialWeeApp.axbundle/SocialWeeApp](DYLIBS/SocialWeeApp.md)
- [/System/Library/AccessibilityBundles/SoftwareUpdateSettingsUI.axbundle/SoftwareUpdateSettingsUI](DYLIBS/SoftwareUpdateSettingsUI.md)
- [/System/Library/AccessibilityBundles/SoundsAndHapticsSettings.axbundle/SoundsAndHapticsSettings](DYLIBS/SoundsAndHapticsSettings.md)
- [/System/Library/AccessibilityBundles/Sports-Assistant.axbundle/Sports-Assistant](DYLIBS/Sports-Assistant.md)
- [/System/Library/AccessibilityBundles/Spotlight.axbundle/Spotlight](DYLIBS/Spotlight.md)
- [/System/Library/AccessibilityBundles/SpotlightUIInternalFramework.axbundle/SpotlightUIInternalFramework](DYLIBS/SpotlightUIInternalFramework.md)
- [/System/Library/AccessibilityBundles/SpringBoard.axbundle/SpringBoard](DYLIBS/SpringBoard.md)
- [/System/Library/AccessibilityBundles/SpringBoardFoundation.axbundle/SpringBoardFoundation](DYLIBS/SpringBoardFoundation.md)
- [/System/Library/AccessibilityBundles/SpringBoardHome.axbundle/SpringBoardHome](DYLIBS/SpringBoardHome.md)
- [/System/Library/AccessibilityBundles/SpringBoardUI.axbundle/SpringBoardUI](DYLIBS/SpringBoardUI.md)
- [/System/Library/AccessibilityBundles/SpringBoardUIServices.axbundle/SpringBoardUIServices](DYLIBS/SpringBoardUIServices.md)
- [/System/Library/AccessibilityBundles/SpriteKit.axbundle/SpriteKit](DYLIBS/SpriteKit.md)
- [/System/Library/AccessibilityBundles/StickersUI.axbundle/StickersUI](DYLIBS/StickersUI.md)
- [/System/Library/AccessibilityBundles/Stocks-Assistant.axbundle/Stocks-Assistant](DYLIBS/Stocks-Assistant.md)
- [/System/Library/AccessibilityBundles/StocksFramework.axbundle/StocksFramework](DYLIBS/StocksFramework.md)
- [/System/Library/AccessibilityBundles/StocksWidget.axbundle/StocksWidget](DYLIBS/StocksWidget.md)
- [/System/Library/AccessibilityBundles/StorageSettings.axbundle/StorageSettings](DYLIBS/StorageSettings.md)
- [/System/Library/AccessibilityBundles/StorageSettingsFramework.axbundle/StorageSettingsFramework](DYLIBS/StorageSettingsFramework.md)
- [/System/Library/AccessibilityBundles/StoreDynamicUIPlugin.axbundle/StoreDynamicUIPlugin](DYLIBS/StoreDynamicUIPlugin.md)
- [/System/Library/AccessibilityBundles/StoreKitFramework.axbundle/StoreKitFramework](DYLIBS/StoreKitFramework.md)
- [/System/Library/AccessibilityBundles/StoreKitUI.axbundle/StoreKitUI](DYLIBS/StoreKitUI.md)
- [/System/Library/AccessibilityBundles/SwiftUI.axbundle/SwiftUI](DYLIBS/SwiftUI.md)
- [/System/Library/AccessibilityBundles/System-Assistant.axbundle/System-Assistant](DYLIBS/System-Assistant.md)
- [/System/Library/AccessibilityBundles/SystemApertureUI.axbundle/SystemApertureUI](DYLIBS/SystemApertureUI.md)
- [/System/Library/AccessibilityBundles/SystemStatusUI.axbundle/SystemStatusUI](DYLIBS/SystemStatusUI.md)
- [/System/Library/AccessibilityBundles/TV.axbundle/TV](DYLIBS/TV.md)
- [/System/Library/AccessibilityBundles/TVMLKit.axbundle/TVMLKit](DYLIBS/TVMLKit.md)
- [/System/Library/AccessibilityBundles/TVRemoteModule.axbundle/TVRemoteModule](DYLIBS/TVRemoteModule.md)
- [/System/Library/AccessibilityBundles/TVRemoteUI.axbundle/TVRemoteUI](DYLIBS/TVRemoteUI.md)
- [/System/Library/AccessibilityBundles/TVRemoteUIService.axbundle/TVRemoteUIService](DYLIBS/TVRemoteUIService.md)
- [/System/Library/AccessibilityBundles/TelephonyUIFramework.axbundle/TelephonyUIFramework](DYLIBS/TelephonyUIFramework.md)
- [/System/Library/AccessibilityBundles/TemplateKit.axbundle/TemplateKit](DYLIBS/TemplateKit.md)
- [/System/Library/AccessibilityBundles/TextInputUI.axbundle/TextInputUI](DYLIBS/TextInputUI.md)
- [/System/Library/AccessibilityBundles/TimerModule.axbundle/TimerModule](DYLIBS/TimerModule.md)
- [/System/Library/AccessibilityBundles/TipsApp.axbundle/TipsApp](DYLIBS/TipsApp.md)
- [/System/Library/AccessibilityBundles/TipsNotificationExtension.axbundle/TipsNotificationExtension](DYLIBS/TipsNotificationExtension.md)
- [/System/Library/AccessibilityBundles/TipsWidgetExtension.axbundle/TipsWidgetExtension](DYLIBS/TipsWidgetExtension.md)
- [/System/Library/AccessibilityBundles/ToneKit.axbundle/ToneKit](DYLIBS/ToneKit.md)
- [/System/Library/AccessibilityBundles/Translate.axbundle/Translate](DYLIBS/Translate.md)
- [/System/Library/AccessibilityBundles/TwitterFramework.axbundle/TwitterFramework](DYLIBS/TwitterFramework.md)
- [/System/Library/AccessibilityBundles/UIKit.axbundle/UIKit](DYLIBS/UIKit.md)
- [/System/Library/AccessibilityBundles/UpNext.axbundle/UpNext](DYLIBS/UpNext.md)
- [/System/Library/AccessibilityBundles/UsageSettings.axbundle/UsageSettings](DYLIBS/UsageSettings.md)
- [/System/Library/AccessibilityBundles/UserNotificationsUI.axbundle/UserNotificationsUI](DYLIBS/UserNotificationsUI.md)
- [/System/Library/AccessibilityBundles/UserNotificationsUIKit.axbundle/UserNotificationsUIKit](DYLIBS/UserNotificationsUIKit.md)
- [/System/Library/AccessibilityBundles/VectorKit.axbundle/VectorKit](DYLIBS/VectorKit.md)
- [/System/Library/AccessibilityBundles/VictoriaSettings.axbundle/VictoriaSettings](DYLIBS/VictoriaSettings.md)
- [/System/Library/AccessibilityBundles/VideoConferenceControlCenterModule.axbundle/VideoConferenceControlCenterModule](DYLIBS/VideoConferenceControlCenterModule.md)
- [/System/Library/AccessibilityBundles/Videos.axbundle/Videos](DYLIBS/Videos.md)
- [/System/Library/AccessibilityBundles/VideosExtrasFramework.axbundle/VideosExtrasFramework](DYLIBS/VideosExtrasFramework.md)
- [/System/Library/AccessibilityBundles/VideosUIFramework.axbundle/VideosUIFramework](DYLIBS/VideosUIFramework.md)
- [/System/Library/AccessibilityBundles/VisionKitCore.axbundle/VisionKitCore](DYLIBS/VisionKitCore.md)
- [/System/Library/AccessibilityBundles/VoiceShortcutsUI.axbundle/VoiceShortcutsUI](DYLIBS/VoiceShortcutsUI.md)
- [/System/Library/AccessibilityBundles/VoiceTriggerUI.axbundle/VoiceTriggerUI](DYLIBS/VoiceTriggerUI.md)
- [/System/Library/AccessibilityBundles/WAAnswer-Assistant.axbundle/WAAnswer-Assistant](DYLIBS/WAAnswer-Assistant.md)
- [/System/Library/AccessibilityBundles/Wallpaper.axbundle/Wallpaper](DYLIBS/Wallpaper.md)
- [/System/Library/AccessibilityBundles/WallpaperSettings.axbundle/WallpaperSettings](DYLIBS/WallpaperSettings.md)
- [/System/Library/AccessibilityBundles/Weather.axbundle/Weather](DYLIBS/Weather.md)
- [/System/Library/AccessibilityBundles/WebCore.axbundle/WebCore](DYLIBS/WebCore.md)
- [/System/Library/AccessibilityBundles/WebKit.axbundle/WebKit](DYLIBS/WebKit.md)
- [/System/Library/AccessibilityBundles/WebKitLegacy.axbundle/WebKitLegacy](DYLIBS/WebKitLegacy.md)
- [/System/Library/AccessibilityBundles/WebProcess.axbundle/WebProcess](DYLIBS/WebProcess.md)
- [/System/Library/AccessibilityBundles/WebProcessLoader.axbundle/WebProcessLoader](DYLIBS/WebProcessLoader.md)
- [/System/Library/AccessibilityBundles/WebUI.axbundle/WebUI](DYLIBS/WebUI.md)
- [/System/Library/AccessibilityBundles/WiFiKitUI.axbundle/WiFiKitUI](DYLIBS/WiFiKitUI.md)
- [/System/Library/AccessibilityBundles/WidgetConfigurationExtension.axbundle/WidgetConfigurationExtension](DYLIBS/WidgetConfigurationExtension.md)
- [/System/Library/AccessibilityBundles/Widgets.axbundle/Widgets](DYLIBS/Widgets.md)
- [/System/Library/AccessibilityBundles/WirelessModemSettings.axbundle/WirelessModemSettings](DYLIBS/WirelessModemSettings.md)
- [/System/Library/AccessibilityBundles/WorkflowUI.axbundle/WorkflowUI](DYLIBS/WorkflowUI.md)
- [/System/Library/AccessibilityBundles/WorkflowUIServices.axbundle/WorkflowUIServices](DYLIBS/WorkflowUIServices.md)
- [/System/Library/AccessibilityBundles/com.apple.CloudDocsUI.CloudSharing-AppExtension.axbundle/com.apple.CloudDocsUI.CloudSharing-AppExtension](DYLIBS/com.apple.CloudDocsUI.CloudSharing-AppExtension.md)
- [/System/Library/AccessibilityBundles/com.apple.DocumentManager.Service-AppExtension.axbundle/com.apple.DocumentManager.Service-AppExtension](DYLIBS/com.apple.DocumentManager.Service-AppExtension.md)
- [/System/Library/AccessibilityBundles/iAdFramework.axbundle/iAdFramework](DYLIBS/iAdFramework.md)
- [/System/Library/AccessibilityBundles/iCloudDriveApp.axbundle/iCloudDriveApp](DYLIBS/iCloudDriveApp.md)
- [/System/Library/AccessibilityBundles/iTunesStoreFramework.axbundle/iTunesStoreFramework](DYLIBS/iTunesStoreFramework.md)
- [/System/Library/AccessibilityBundles/iTunesStoreUIFramework.axbundle/iTunesStoreUIFramework](DYLIBS/iTunesStoreUIFramework.md)
- [/System/Library/Accounts/Access/CloudKitAccessPlugin.bundle/CloudKitAccessPlugin](DYLIBS/CloudKitAccessPlugin.md)
- [/System/Library/Accounts/Access/DefaultAccessPlugin.bundle/DefaultAccessPlugin](DYLIBS/DefaultAccessPlugin.md)
- [/System/Library/Accounts/Access/YelpAccessPlugin.bundle/YelpAccessPlugin](DYLIBS/YelpAccessPlugin.md)
- [/System/Library/Accounts/Authentication/AppleIDAuthentication.bundle/AppleIDAuthentication](DYLIBS/AppleIDAuthentication.md)
- [/System/Library/Accounts/Authentication/AppleIDSSOAuthenticationPlugin.bundle/AppleIDSSOAuthenticationPlugin](DYLIBS/AppleIDSSOAuthenticationPlugin.md)
- [/System/Library/Accounts/Authentication/CloudKitAuthenticationPlugin.bundle/CloudKitAuthenticationPlugin](DYLIBS/CloudKitAuthenticationPlugin.md)
- [/System/Library/Accounts/Authentication/DAAccountAuthenticator.bundle/DAAccountAuthenticator](DYLIBS/DAAccountAuthenticator.md)
- [/System/Library/Accounts/Authentication/ESAccountAuthenticator.bundle/ESAccountAuthenticator](DYLIBS/ESAccountAuthenticator.md)
- [/System/Library/Accounts/Authentication/GoogleAuthenticationPlugin.bundle/GoogleAuthenticationPlugin](DYLIBS/GoogleAuthenticationPlugin.md)
- [/System/Library/Accounts/Authentication/KerberosAuthenticationPlugin.bundle/KerberosAuthenticationPlugin](DYLIBS/KerberosAuthenticationPlugin.md)
- [/System/Library/Accounts/Authentication/MessageAccountAuthenticationPlugin.bundle/MessageAccountAuthenticationPlugin](DYLIBS/MessageAccountAuthenticationPlugin.md)
- [/System/Library/Accounts/Authentication/YahooAuthenticationPlugin.bundle/YahooAuthenticationPlugin](DYLIBS/YahooAuthenticationPlugin.md)
- [/System/Library/Accounts/Notification/AAAccountNotificationPlugin.bundle/AAAccountNotificationPlugin](DYLIBS/AAAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/AADataclassEnableNotificationPlugin.bundle/AADataclassEnableNotificationPlugin](DYLIBS/AADataclassEnableNotificationPlugin.md)
- [/System/Library/Accounts/Notification/AAIDMSAccountNotificationPlugin.bundle/AAIDMSAccountNotificationPlugin](DYLIBS/AAIDMSAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/ACDatabaseBackupNotificationPlugin.bundle/ACDatabaseBackupNotificationPlugin](DYLIBS/ACDatabaseBackupNotificationPlugin.md)
- [/System/Library/Accounts/Notification/ADAccountsNotificationPlugin.bundle/ADAccountsNotificationPlugin](DYLIBS/ADAccountsNotificationPlugin.md)
- [/System/Library/Accounts/Notification/AISAccountNotificationPlugin.bundle/AISAccountNotificationPlugin](DYLIBS/AISAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/AKAccountNotificationPlugin.bundle/AKAccountNotificationPlugin](DYLIBS/AKAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/AMSAccountNotificationPlugin.bundle/AMSAccountNotificationPlugin](DYLIBS/AMSAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/AMSAccountSyncNotificationPlugin.bundle/AMSAccountSyncNotificationPlugin](DYLIBS/AMSAccountSyncNotificationPlugin.md)
- [/System/Library/Accounts/Notification/ASDAccountNotficationPlugin.bundle/ASDAccountNotficationPlugin](DYLIBS/ASDAccountNotficationPlugin.md)
- [/System/Library/Accounts/Notification/AppleIDSSONotificationPlugin.bundle/AppleIDSSONotificationPlugin](DYLIBS/AppleIDSSONotificationPlugin.md)
- [/System/Library/Accounts/Notification/BTCloudPairingAccountNotificationPlugin.bundle/BTCloudPairingAccountNotificationPlugin](DYLIBS/BTCloudPairingAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/CDPAccountNotificationPlugin_IOS.bundle/CDPAccountNotificationPlugin_IOS](DYLIBS/CDPAccountNotificationPlugin_IOS.md)
- [/System/Library/Accounts/Notification/ClassKitAccountNotificationPlugin.bundle/ClassKitAccountNotificationPlugin](DYLIBS/ClassKitAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/CloudKitNotificationPlugin.bundle/CloudKitNotificationPlugin](DYLIBS/CloudKitNotificationPlugin.md)
- [/System/Library/Accounts/Notification/CoreIDVAccountNotificationPlugin.bundle/CoreIDVAccountNotificationPlugin](DYLIBS/CoreIDVAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/CoreLocationAccountNotificationPlugin.bundle/CoreLocationAccountNotificationPlugin](DYLIBS/CoreLocationAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/CoreRecentsAccountNotificationPlugin.bundle/CoreRecentsAccountNotificationPlugin](DYLIBS/CoreRecentsAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/CoreRoutineAccountNotificationPlugin.bundle/CoreRoutineAccountNotificationPlugin](DYLIBS/CoreRoutineAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/DAAccountNotifier.bundle/DAAccountNotifier](DYLIBS/DAAccountNotifier.md)
- [/System/Library/Accounts/Notification/DMDAccountNotificationPlugin.bundle/DMDAccountNotificationPlugin](DYLIBS/DMDAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/DonationAccountWatcher.bundle/DonationAccountWatcher](DYLIBS/DonationAccountWatcher.md)
- [/System/Library/Accounts/Notification/ESAccountNotifier.bundle/ESAccountNotifier](DYLIBS/ESAccountNotifier.md)
- [/System/Library/Accounts/Notification/FMFLocatorAccountNotificationPlugin.bundle/FMFLocatorAccountNotificationPlugin](DYLIBS/FMFLocatorAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/FindMyDeviceAccountNotificationPlugin.bundle/FindMyDeviceAccountNotificationPlugin](DYLIBS/FindMyDeviceAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/GameCenterAccountNotificationPlugin.bundle/GameCenterAccountNotificationPlugin](DYLIBS/GameCenterAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/HealthKitAccountNotificationPlugin.bundle/HealthKitAccountNotificationPlugin](DYLIBS/HealthKitAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/HomeKitAccountNotificationPlugin.bundle/HomeKitAccountNotificationPlugin](DYLIBS/HomeKitAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/IDSAccountNotificationPlugin.bundle/IDSAccountNotificationPlugin](DYLIBS/IDSAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/IMAccountNotificationPlugin.bundle/IMAccountNotificationPlugin](DYLIBS/IMAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/INDAccountNotificationPlugin.bundle/INDAccountNotificationPlugin](DYLIBS/INDAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/KeychainSyncAccountNotification.bundle/KeychainSyncAccountNotification](DYLIBS/KeychainSyncAccountNotification.md)
- [/System/Library/Accounts/Notification/LockdownModeAccountNotificationPlugin.bundle/LockdownModeAccountNotificationPlugin](DYLIBS/LockdownModeAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/MessageAccountNotificationPlugin.bundle/MessageAccountNotificationPlugin](DYLIBS/MessageAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/MobileSyncAccountNotificationPlugin.bundle/MobileSyncAccountNotificationPlugin](DYLIBS/MobileSyncAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/NewsNotificationPlugin.bundle/NewsNotificationPlugin](DYLIBS/NewsNotificationPlugin.md)
- [/System/Library/Accounts/Notification/NotesAccountNotificationPlugin.bundle/NotesAccountNotificationPlugin](DYLIBS/NotesAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/PCSAccountNotificationPlugin.bundle/PCSAccountNotificationPlugin](DYLIBS/PCSAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/PassbookAccountNotificationPlugin.bundle/PassbookAccountNotificationPlugin](DYLIBS/PassbookAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/PhotosAccountNotificationPlugin.bundle/PhotosAccountNotificationPlugin](DYLIBS/PhotosAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/RPAccountNotificationPlugin.bundle/RPAccountNotificationPlugin](DYLIBS/RPAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/RemindersAccountNotificationPlugin.bundle/RemindersAccountNotificationPlugin](DYLIBS/RemindersAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/SearchPartyAccountNotificationPlugin.bundle/SearchPartyAccountNotificationPlugin](DYLIBS/SearchPartyAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/SecureBackupNotification.bundle/SecureBackupNotification](DYLIBS/SecureBackupNotification.md)
- [/System/Library/Accounts/Notification/SharingAccountNotificationPlugin.bundle/SharingAccountNotificationPlugin](DYLIBS/SharingAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/ShortcutsCloudKitAccountNotificationPlugin.bundle/ShortcutsCloudKitAccountNotificationPlugin](DYLIBS/ShortcutsCloudKitAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/SiriCloudKitAccountsNotifier.bundle/SiriCloudKitAccountsNotifier](DYLIBS/SiriCloudKitAccountsNotifier.md)
- [/System/Library/Accounts/Notification/SocialAccountNotificationPlugin.bundle/SocialAccountNotificationPlugin](DYLIBS/SocialAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/WebBookmarksNotificationPlugin.bundle/WebBookmarksNotificationPlugin](DYLIBS/WebBookmarksNotificationPlugin.md)
- [/System/Library/Accounts/Notification/com.apple.askpermission.AccountNotificationPlugin.bundle/com.apple.askpermission.AccountNotificationPlugin](DYLIBS/com.apple.askpermission.AccountNotificationPlugin.md)
- [/System/Library/Assistant/Plugins/AssistantTTSPlugin.assistantBundle/AssistantTTSPlugin](DYLIBS/AssistantTTSPlugin.md)
- [/System/Library/Assistant/Plugins/Calendar.assistantBundle/Calendar](DYLIBS/Calendar.md)
- [/System/Library/Assistant/Plugins/Contacts.assistantBundle/Contacts](DYLIBS/Contacts.md)
- [/System/Library/Assistant/Plugins/CorrectionsProfilesSync.assistantBundle/CorrectionsProfilesSync](DYLIBS/CorrectionsProfilesSync.md)
- [/System/Library/Assistant/Plugins/GEO.assistantBundle/GEO](DYLIBS/GEO.md)
- [/System/Library/Assistant/Plugins/HMAssistant.assistantBundle/HMAssistant](DYLIBS/HMAssistant.md)
- [/System/Library/Assistant/Plugins/LocaleSettings.assistantBundle/LocaleSettings](DYLIBS/LocaleSettings.md)
- [/System/Library/Assistant/Plugins/Media.assistantBundle/Media](DYLIBS/Media.md)
- [/System/Library/Assistant/Plugins/Phone.assistantBundle/Phone](DYLIBS/Phone.md)
- [/System/Library/Assistant/Plugins/Podcasts.assistantBundle/Podcasts](DYLIBS/Podcasts.md)
- [/System/Library/Assistant/Plugins/Routine.assistantBundle/Routine](DYLIBS/Routine.md)
- [/System/Library/Assistant/Plugins/SurfStatusSync.assistantBundle/SurfStatusSync](DYLIBS/SurfStatusSync.md)
- [/System/Library/Assistant/Plugins/SynapseSyncPlugin.assistantBundle/SynapseSyncPlugin](DYLIBS/SynapseSyncPlugin.md)
- [/System/Library/Assistant/UIPlugins/SiriFindMyUIPlugin.siriUIBundle/Frameworks/SiriFindMyUI.framework/SiriFindMyUI](DYLIBS/SiriFindMyUI.md)
- [/System/Library/ControlCenter/Bundles/AccessibilityGuidedAccessControlCenterModule.bundle/AccessibilityGuidedAccessControlCenterModule](DYLIBS/AccessibilityGuidedAccessControlCenterModule.md)
- [/System/Library/ControlCenter/Bundles/AccessibilityShorcutsModule.bundle/AccessibilityShorcutsModule](DYLIBS/AccessibilityShorcutsModule.md)
- [/System/Library/ControlCenter/Bundles/AccessibilitySoundDetectionControlCenterModule.bundle/AccessibilitySoundDetectionControlCenterModule](DYLIBS/AccessibilitySoundDetectionControlCenterModule.md)
- [/System/Library/ControlCenter/Bundles/AccessibilityTextSizeModule.bundle/AccessibilityTextSizeModule](DYLIBS/AccessibilityTextSizeModule.md)
- [/System/Library/ControlCenter/Bundles/AirPlayMirroringModule.bundle/AirPlayMirroringModule](DYLIBS/AirPlayMirroringModule.md)
- [/System/Library/ControlCenter/Bundles/AlarmModule.bundle/AlarmModule](DYLIBS/AlarmModule.md)
- [/System/Library/ControlCenter/Bundles/AppearanceModule.bundle/AppearanceModule](DYLIBS/AppearanceModule.md)
- [/System/Library/ControlCenter/Bundles/CalculatorModule.bundle/CalculatorModule](DYLIBS/CalculatorModule.md)
- [/System/Library/ControlCenter/Bundles/CameraModule.bundle/CameraModule](DYLIBS/CameraModule.md)
- [/System/Library/ControlCenter/Bundles/ConnectivityModule.bundle/ConnectivityModule](DYLIBS/ConnectivityModule.md)
- [/System/Library/ControlCenter/Bundles/DisplayModule.bundle/DisplayModule](DYLIBS/DisplayModule.md)
- [/System/Library/ControlCenter/Bundles/FeedbackAssistantModule.bundle/FeedbackAssistantModule](DYLIBS/FeedbackAssistantModule.md)
- [/System/Library/ControlCenter/Bundles/FlashlightModule.bundle/FlashlightModule](DYLIBS/FlashlightModule.md)
- [/System/Library/ControlCenter/Bundles/HearingAidsModule.bundle/HearingAidsModule](DYLIBS/HearingAidsModule.md)
- [/System/Library/ControlCenter/Bundles/HomeControlCenterCompactModule.bundle/HomeControlCenterCompactModule](DYLIBS/HomeControlCenterCompactModule.md)
- [/System/Library/ControlCenter/Bundles/HomeControlCenterModule.bundle/HomeControlCenterModule](DYLIBS/HomeControlCenterModule.md)
- [/System/Library/ControlCenter/Bundles/KeyboardBrightnessModule.bundle/KeyboardBrightnessModule](DYLIBS/KeyboardBrightnessModule.md)
- [/System/Library/ControlCenter/Bundles/LowPowerModule.bundle/LowPowerModule](DYLIBS/LowPowerModule.md)
- [/System/Library/ControlCenter/Bundles/MagnifierModule.bundle/MagnifierModule](DYLIBS/MagnifierModule.md)
- [/System/Library/ControlCenter/Bundles/MediaControlsAudioModule.bundle/MediaControlsAudioModule](DYLIBS/MediaControlsAudioModule.md)
- [/System/Library/ControlCenter/Bundles/MediaControlsModule.bundle/MediaControlsModule](DYLIBS/MediaControlsModule.md)
- [/System/Library/ControlCenter/Bundles/MuteModule.bundle/MuteModule](DYLIBS/MuteModule.md)
- [/System/Library/ControlCenter/Bundles/OrientationLockModule.bundle/OrientationLockModule](DYLIBS/OrientationLockModule.md)
- [/System/Library/ControlCenter/Bundles/PerformanceTraceModule.bundle/PerformanceTraceModule](DYLIBS/PerformanceTraceModule.md)
- [/System/Library/ControlCenter/Bundles/QRCodeModule.bundle/QRCodeModule](DYLIBS/QRCodeModule.md)
- [/System/Library/ControlCenter/Bundles/QuickNoteModule.bundle/QuickNoteModule](DYLIBS/QuickNoteModule.md)
- [/System/Library/ControlCenter/Bundles/ShazamModule.bundle/ShazamModule](DYLIBS/ShazamModule.md)
- [/System/Library/ControlCenter/Bundles/SpokenNotificationsModule.bundle/SpokenNotificationsModule](DYLIBS/SpokenNotificationsModule.md)
- [/System/Library/ControlCenter/Bundles/StopwatchModule.bundle/StopwatchModule](DYLIBS/StopwatchModule.md)
- [/System/Library/ControlCenter/Bundles/TVRemoteModule.bundle/TVRemoteModule](DYLIBS/TVRemoteModule.md)
- [/System/Library/ControlCenter/Bundles/TimerModule.bundle/TimerModule](DYLIBS/TimerModule.md)
- [/System/Library/ControlCenter/Bundles/VoiceMemosModule.bundle/VoiceMemosModule](DYLIBS/VoiceMemosModule.md)
- [/System/Library/ControlCenter/Bundles/WalletModule.bundle/WalletModule](DYLIBS/WalletModule.md)
- [/System/Library/CoreAccessories/PlugIns/Features/AssistiveTouch-iOS.feature/AssistiveTouch-iOS](DYLIBS/AssistiveTouch-iOS.md)
- [/System/Library/CoreAccessories/PlugIns/Features/BLEPairing-iOS.feature/BLEPairing-iOS](DYLIBS/BLEPairing-iOS.md)
- [/System/Library/CoreAccessories/PlugIns/Features/Communications-iOS.feature/Communications-iOS](DYLIBS/Communications-iOS.md)
- [/System/Library/CoreAccessories/PlugIns/Features/HID.feature/HID](DYLIBS/HID.md)
- [/System/Library/CoreAccessories/PlugIns/Features/MediaLibrary-iOS.feature/MediaLibrary-iOS](DYLIBS/MediaLibrary-iOS.md)
- [/System/Library/CoreAccessories/PlugIns/Features/Navigation-iOS.feature/Navigation-iOS](DYLIBS/Navigation-iOS.md)
- [/System/Library/CoreAccessories/PlugIns/Features/NowPlaying-iOS.feature/NowPlaying-iOS](DYLIBS/NowPlaying-iOS.md)
- [/System/Library/CoreAccessories/PlugIns/Features/OOBBTPairing-iOS.feature/OOBBTPairing-iOS](DYLIBS/OOBBTPairing-iOS.md)
- [/System/Library/CoreAccessories/PlugIns/Platform/IOKit.platform/IOKit](DYLIBS/IOKit.md)
- [/System/Library/CoreAccessories/PlugIns/Platform/Platform-Bluetooth.platform/Platform-Bluetooth](DYLIBS/Platform-Bluetooth.md)
- [/System/Library/CoreAccessories/PlugIns/Platform/System.platform/System](DYLIBS/System.md)
- [/System/Library/CoreAccessories/PlugIns/Platform/WiFiSharing.platform/WiFiSharing](DYLIBS/WiFiSharing.md)
- [/System/Library/CoreAccessories/PlugIns/Transports/IOAccessoryManager.transport/IOAccessoryManager](DYLIBS/IOAccessoryManager.md)
- [/System/Library/CoreAccessories/PlugIns/Transports/NFC.transport/NFC](DYLIBS/NFC.md)
- [/System/Library/CoreAccessories/PlugIns/Transports/USBHost.transport/USBHost](DYLIBS/USBHost.md)
- [/System/Library/CoreServices/RawCamera.bundle/RawCamera](DYLIBS/RawCamera.md)
- [/System/Library/DataClassMigrators/DAAccount.migrator/DAAccount](DYLIBS/DAAccount.md)
- [/System/Library/DataClassMigrators/FaceTimeMigrator.migrator/FaceTimeMigrator](DYLIBS/FaceTimeMigrator.md)
- [/System/Library/DataClassMigrators/MessagesDataMigrator.migrator/MessagesDataMigrator](DYLIBS/MessagesDataMigrator.md)
- [/System/Library/DigitalSeparation/SharingSources/PasswordsDigitalSeparation.bundle/PasswordsDigitalSeparation](DYLIBS/PasswordsDigitalSeparation.md)
- [/System/Library/Extensions/AGXGPURawCounterBundle.bundle/AGXGPURawCounterBundle](DYLIBS/AGXGPURawCounterBundle.md)
- [/System/Library/Extensions/AGXMetalG16P_A0.bundle/AGXMetalG16P_A0](DYLIBS/AGXMetalG16P_A0.md)
- [/System/Library/Extensions/AGXMetalG16P_B0.bundle/AGXMetalG16P_B0](DYLIBS/AGXMetalG16P_B0.md)
- [/System/Library/Extensions/AppleHDQGasGaugeControl.kext/PlugIns/AppleHDQGasGaugeHID.plugin/AppleHDQGasGaugeHID](DYLIBS/AppleHDQGasGaugeHID.md)
- [/System/Library/Extensions/AppleMetalGLRenderer.bundle/AppleMetalGLRenderer](DYLIBS/AppleMetalGLRenderer.md)
- [/System/Library/Extensions/AppleMultitouchSPI.kext/PlugIns/MultitouchHID.plugin/MultitouchHID](DYLIBS/MultitouchHID.md)
- [/System/Library/Extensions/AppleSPU.kext/PlugIns/AppleSPULib.plugin/AppleSPULib](DYLIBS/AppleSPULib.md)
- [/System/Library/Extensions/AppleSPU.kext/PlugIns/GNSSPassthroughLib.plugin/GNSSPassthroughLib](DYLIBS/GNSSPassthroughLib.md)
- [/System/Library/Extensions/IOHIDFamily.kext/PlugIns/IOHIDLib.plugin/IOHIDLib](DYLIBS/IOHIDLib.md)
- [/System/Library/Extensions/IOUSBDeviceFamily.kext/PlugIns/IOUSBDeviceLib.plugin/IOUSBDeviceLib](DYLIBS/IOUSBDeviceLib.md)
- [/System/Library/Fitness/Plugins/ActivitySharingAwardsPlugin.bundle/ActivitySharingAwardsPlugin](DYLIBS/ActivitySharingAwardsPlugin.md)
- [/System/Library/Fitness/Plugins/SeymourAwardsPlugin.bundle/SeymourAwardsPlugin](DYLIBS/SeymourAwardsPlugin.md)
- [/System/Library/Frameworks/ARKit.framework/ARKit](DYLIBS/ARKit.md)
- [/System/Library/Frameworks/AVFAudio.framework/AVFAudio](DYLIBS/AVFAudio.md)
- [/System/Library/Frameworks/AVFoundation.framework/AVFoundation](DYLIBS/AVFoundation.md)
- [/System/Library/Frameworks/AVKit.framework/AVKit](DYLIBS/AVKit.md)
- [/System/Library/Frameworks/AVRouting.framework/AVRouting](DYLIBS/AVRouting.md)
- [/System/Library/Frameworks/Accelerate.framework/Accelerate](DYLIBS/Accelerate.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vImage.framework/Libraries/libCGInterfaces.dylib](DYLIBS/libCGInterfaces.dylib.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vImage.framework/vImage](DYLIBS/vImage.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libBLAS.dylib](DYLIBS/libBLAS.dylib.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libBNNS.dylib](DYLIBS/libBNNS.dylib.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libLAPACK.dylib](DYLIBS/libLAPACK.dylib.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libLinearAlgebra.dylib](DYLIBS/libLinearAlgebra.dylib.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libQuadrature.dylib](DYLIBS/libQuadrature.dylib.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libSparse.dylib](DYLIBS/libSparse.dylib.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libSparseBLAS.dylib](DYLIBS/libSparseBLAS.dylib.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libvDSP.dylib](DYLIBS/libvDSP.dylib.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libvMisc.dylib](DYLIBS/libvMisc.dylib.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/vecLib](DYLIBS/vecLib.md)
- [/System/Library/Frameworks/Accessibility.framework/Accessibility](DYLIBS/Accessibility.md)
- [/System/Library/Frameworks/Accounts.framework/Accounts](DYLIBS/Accounts.md)
- [/System/Library/Frameworks/ActivityKit.framework/ActivityKit](DYLIBS/ActivityKit.md)
- [/System/Library/Frameworks/AdServices.framework/AdServices](DYLIBS/AdServices.md)
- [/System/Library/Frameworks/AdSupport.framework/AdSupport](DYLIBS/AdSupport.md)
- [/System/Library/Frameworks/AddressBook.framework/AddressBook](DYLIBS/AddressBook.md)
- [/System/Library/Frameworks/AddressBookUI.framework/AddressBookUI](DYLIBS/AddressBookUI.md)
- [/System/Library/Frameworks/AppClip.framework/AppClip](DYLIBS/AppClip.md)
- [/System/Library/Frameworks/AppIntents.framework/AppIntents](DYLIBS/AppIntents.md)
- [/System/Library/Frameworks/AppTrackingTransparency.framework/AppTrackingTransparency](DYLIBS/AppTrackingTransparency.md)
- [/System/Library/Frameworks/AssetsLibrary.framework/AssetsLibrary](DYLIBS/AssetsLibrary.md)
- [/System/Library/Frameworks/AudioToolbox.framework/AudioCodecs](DYLIBS/AudioCodecs.md)
- [/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox](DYLIBS/AudioToolbox.md)
- [/System/Library/Frameworks/AudioToolbox.framework/libAudioDSP.dylib](DYLIBS/libAudioDSP.dylib.md)
- [/System/Library/Frameworks/AudioToolbox.framework/libEmbeddedSystemAUs.dylib](DYLIBS/libEmbeddedSystemAUs.dylib.md)
- [/System/Library/Frameworks/AudioToolbox.framework/libValidationCapsule.dylib](DYLIBS/libValidationCapsule.dylib.md)
- [/System/Library/Frameworks/AudioToolbox.framework/libVibeSynthEngine.dylib](DYLIBS/libVibeSynthEngine.dylib.md)
- [/System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices](DYLIBS/AuthenticationServices.md)
- [/System/Library/Frameworks/AutomatedDeviceEnrollment.framework/AutomatedDeviceEnrollment](DYLIBS/AutomatedDeviceEnrollment.md)
- [/System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/AutomaticAssessmentConfiguration](DYLIBS/AutomaticAssessmentConfiguration.md)
- [/System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/Frameworks/AACClient.framework/AACClient](DYLIBS/AACClient.md)
- [/System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/Frameworks/AACDependencies.framework/AACDependencies](DYLIBS/AACDependencies.md)
- [/System/Library/Frameworks/BackgroundAssets.framework/BackgroundAssets](DYLIBS/BackgroundAssets.md)
- [/System/Library/Frameworks/BackgroundTasks.framework/BackgroundTasks](DYLIBS/BackgroundTasks.md)
- [/System/Library/Frameworks/BusinessChat.framework/BusinessChat](DYLIBS/BusinessChat.md)
- [/System/Library/Frameworks/CFNetwork.framework/CFNetwork](DYLIBS/CFNetwork.md)
- [/System/Library/Frameworks/CallKit.framework/CallKit](DYLIBS/CallKit.md)
- [/System/Library/Frameworks/CarKey.framework/CarKey](DYLIBS/CarKey.md)
- [/System/Library/Frameworks/CarPlay.framework/CarPlay](DYLIBS/CarPlay.md)
- [/System/Library/Frameworks/Charts.framework/Charts](DYLIBS/Charts.md)
- [/System/Library/Frameworks/Cinematic.framework/Cinematic](DYLIBS/Cinematic.md)
- [/System/Library/Frameworks/ClassKit.framework/ClassKit](DYLIBS/ClassKit.md)
- [/System/Library/Frameworks/ClockKit.framework/ClockKit](DYLIBS/ClockKit.md)
- [/System/Library/Frameworks/CloudKit.framework/CloudKit](DYLIBS/CloudKit.md)
- [/System/Library/Frameworks/ColorSync.framework/ColorSync](DYLIBS/ColorSync.md)
- [/System/Library/Frameworks/Combine.framework/Combine](DYLIBS/Combine.md)
- [/System/Library/Frameworks/Contacts.framework/Contacts](DYLIBS/Contacts.md)
- [/System/Library/Frameworks/ContactsUI.framework/ContactsUI](DYLIBS/ContactsUI.md)
- [/System/Library/Frameworks/CoreAudio.framework/CoreAudio](DYLIBS/CoreAudio.md)
- [/System/Library/Frameworks/CoreAudioKit.framework/CoreAudioKit](DYLIBS/CoreAudioKit.md)
- [/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth](DYLIBS/CoreBluetooth.md)
- [/System/Library/Frameworks/CoreData.framework/CoreData](DYLIBS/CoreData.md)
- [/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation](DYLIBS/CoreFoundation.md)
- [/System/Library/Frameworks/CoreGraphics.framework/CoreGraphics](DYLIBS/CoreGraphics.md)
- [/System/Library/Frameworks/CoreHaptics.framework/CoreHaptics](DYLIBS/CoreHaptics.md)
- [/System/Library/Frameworks/CoreImage.framework/CoreImage](DYLIBS/CoreImage.md)
- [/System/Library/Frameworks/CoreLocation.framework/CoreLocation](DYLIBS/CoreLocation.md)
- [/System/Library/Frameworks/CoreLocationUI.framework/CoreLocationUI](DYLIBS/CoreLocationUI.md)
- [/System/Library/Frameworks/CoreMIDI.framework/CoreMIDI](DYLIBS/CoreMIDI.md)
- [/System/Library/Frameworks/CoreML.framework/CoreML](DYLIBS/CoreML.md)
- [/System/Library/Frameworks/CoreMedia.framework/CoreMedia](DYLIBS/CoreMedia.md)
- [/System/Library/Frameworks/CoreMediaIO.framework/CoreMediaIO](DYLIBS/CoreMediaIO.md)
- [/System/Library/Frameworks/CoreMotion.framework/CoreMotion](DYLIBS/CoreMotion.md)
- [/System/Library/Frameworks/CoreNFC.framework/CoreNFC](DYLIBS/CoreNFC.md)
- [/System/Library/Frameworks/CoreServices.framework/CoreServices](DYLIBS/CoreServices.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight](DYLIBS/CoreSpotlight.md)
- [/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony](DYLIBS/CoreTelephony.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/CTParser.framework/CTParser](DYLIBS/CTParser.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCellularDecoders.dylib](DYLIBS/libCellularDecoders.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterAWDMetrics.dylib](DYLIBS/libCommCenterAWDMetrics.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterBase.dylib](DYLIBS/libCommCenterBase.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterCNTargetData.dylib](DYLIBS/libCommCenterCNTargetData.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterCommandDrivers.dylib](DYLIBS/libCommCenterCommandDrivers.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterKCommandDrivers.dylib](DYLIBS/libCommCenterKCommandDrivers.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterMCommandDrivers.dylib](DYLIBS/libCommCenterMCommandDrivers.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libSystemDetermination.dylib](DYLIBS/libSystemDetermination.dylib.md)
- [/System/Library/Frameworks/CoreText.framework/CoreText](DYLIBS/CoreText.md)
- [/System/Library/Frameworks/CoreTransferable.framework/CoreTransferable](DYLIBS/CoreTransferable.md)
- [/System/Library/Frameworks/CoreVideo.framework/CoreVideo](DYLIBS/CoreVideo.md)
- [/System/Library/Frameworks/CreateML.framework/CreateML](DYLIBS/CreateML.md)
- [/System/Library/Frameworks/CreateMLComponents.framework/CreateMLComponents](DYLIBS/CreateMLComponents.md)
- [/System/Library/Frameworks/CryptoKit.framework/CryptoKit](DYLIBS/CryptoKit.md)
- [/System/Library/Frameworks/CryptoTokenKit.framework/CryptoTokenKit](DYLIBS/CryptoTokenKit.md)
- [/System/Library/Frameworks/DataDetection.framework/DataDetection](DYLIBS/DataDetection.md)
- [/System/Library/Frameworks/DeveloperToolsSupport.framework/DeveloperToolsSupport](DYLIBS/DeveloperToolsSupport.md)
- [/System/Library/Frameworks/DeviceActivity.framework/DeviceActivity](DYLIBS/DeviceActivity.md)
- [/System/Library/Frameworks/DeviceCheck.framework/DeviceCheck](DYLIBS/DeviceCheck.md)
- [/System/Library/Frameworks/DeviceDiscoveryExtension.framework/DeviceDiscoveryExtension](DYLIBS/DeviceDiscoveryExtension.md)
- [/System/Library/Frameworks/DockKit.framework/DockKit](DYLIBS/DockKit.md)
- [/System/Library/Frameworks/DriverKit.framework/DriverKit](DYLIBS/DriverKit.md)
- [/System/Library/Frameworks/EventKit.framework/EventKit](DYLIBS/EventKit.md)
- [/System/Library/Frameworks/EventKitUI.framework/EventKitUI](DYLIBS/EventKitUI.md)
- [/System/Library/Frameworks/ExposureNotification.framework/ExposureNotification](DYLIBS/ExposureNotification.md)
- [/System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation](DYLIBS/ExtensionFoundation.md)
- [/System/Library/Frameworks/ExtensionKit.framework/ExtensionKit](DYLIBS/ExtensionKit.md)
- [/System/Library/Frameworks/ExternalAccessory.framework/ExternalAccessory](DYLIBS/ExternalAccessory.md)
- [/System/Library/Frameworks/FamilyControls.framework/FamilyControls](DYLIBS/FamilyControls.md)
- [/System/Library/Frameworks/FileProvider.framework/FileProvider](DYLIBS/FileProvider.md)
- [/System/Library/Frameworks/FileProviderUI.framework/FileProviderUI](DYLIBS/FileProviderUI.md)
- [/System/Library/Frameworks/FinanceKit.framework/FinanceKit](DYLIBS/FinanceKit.md)
- [/System/Library/Frameworks/FinanceKitUI.framework/FinanceKitUI](DYLIBS/FinanceKitUI.md)
- [/System/Library/Frameworks/Foundation.framework/Foundation](DYLIBS/Foundation.md)
- [/System/Library/Frameworks/GLKit.framework/GLKit](DYLIBS/GLKit.md)
- [/System/Library/Frameworks/GSS.framework/GSS](DYLIBS/GSS.md)
- [/System/Library/Frameworks/GameController.framework/GameController](DYLIBS/GameController.md)
- [/System/Library/Frameworks/GameKit.framework/GameKit](DYLIBS/GameKit.md)
- [/System/Library/Frameworks/GameplayKit.framework/GameplayKit](DYLIBS/GameplayKit.md)
- [/System/Library/Frameworks/GroupActivities.framework/GroupActivities](DYLIBS/GroupActivities.md)
- [/System/Library/Frameworks/HealthKit.framework/HealthKit](DYLIBS/HealthKit.md)
- [/System/Library/Frameworks/HealthKitUI.framework/HealthKitUI](DYLIBS/HealthKitUI.md)
- [/System/Library/Frameworks/HomeKit.framework/HomeKit](DYLIBS/HomeKit.md)
- [/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit](DYLIBS/IOKit.md)
- [/System/Library/Frameworks/IOSurface.framework/IOSurface](DYLIBS/IOSurface.md)
- [/System/Library/Frameworks/IdentityLookup.framework/IdentityLookup](DYLIBS/IdentityLookup.md)
- [/System/Library/Frameworks/IdentityLookupUI.framework/IdentityLookupUI](DYLIBS/IdentityLookupUI.md)
- [/System/Library/Frameworks/ImageCaptureCore.framework/ImageCaptureCore](DYLIBS/ImageCaptureCore.md)
- [/System/Library/Frameworks/ImageIO.framework/ImageIO](DYLIBS/ImageIO.md)
- [/System/Library/Frameworks/Intents.framework/Intents](DYLIBS/Intents.md)
- [/System/Library/Frameworks/IntentsUI.framework/IntentsUI](DYLIBS/IntentsUI.md)
- [/System/Library/Frameworks/JavaScriptCore.framework/JavaScriptCore](DYLIBS/JavaScriptCore.md)
- [/System/Library/Frameworks/JournalingSuggestions.framework/JournalingSuggestions](DYLIBS/JournalingSuggestions.md)
- [/System/Library/Frameworks/LinkPresentation.framework/LinkPresentation](DYLIBS/LinkPresentation.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication](DYLIBS/LocalAuthentication.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/DaemonUtils.framework/DaemonUtils](DYLIBS/DaemonUtils.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismBase.framework/MechanismBase](DYLIBS/MechanismBase.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/ModuleBase.framework/ModuleBase](DYLIBS/ModuleBase.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/SharedUtils.framework/SharedUtils](DYLIBS/SharedUtils.md)
- [/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI](DYLIBS/LocalAuthenticationEmbeddedUI.md)
- [/System/Library/Frameworks/MLCompute.framework/MLCompute](DYLIBS/MLCompute.md)
- [/System/Library/Frameworks/ManagedAppDistribution.framework/ManagedAppDistribution](DYLIBS/ManagedAppDistribution.md)
- [/System/Library/Frameworks/ManagedSettings.framework/ManagedSettings](DYLIBS/ManagedSettings.md)
- [/System/Library/Frameworks/ManagedSettingsUI.framework/ManagedSettingsUI](DYLIBS/ManagedSettingsUI.md)
- [/System/Library/Frameworks/MapKit.framework/MapKit](DYLIBS/MapKit.md)
- [/System/Library/Frameworks/Matter.framework/Matter](DYLIBS/Matter.md)
- [/System/Library/Frameworks/MatterSupport.framework/MatterSupport](DYLIBS/MatterSupport.md)
- [/System/Library/Frameworks/MediaAccessibility.framework/MediaAccessibility](DYLIBS/MediaAccessibility.md)
- [/System/Library/Frameworks/MediaPlayer.framework/MediaPlayer](DYLIBS/MediaPlayer.md)
- [/System/Library/Frameworks/MediaSetup.framework/MediaSetup](DYLIBS/MediaSetup.md)
- [/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox](DYLIBS/MediaToolbox.md)
- [/System/Library/Frameworks/MediaToolbox.framework/Support/libSTS-N.dylib](DYLIBS/libSTS-N.dylib.md)
- [/System/Library/Frameworks/MessageUI.framework/MessageUI](DYLIBS/MessageUI.md)
- [/System/Library/Frameworks/Messages.framework/Messages](DYLIBS/Messages.md)
- [/System/Library/Frameworks/Metal.framework/Metal](DYLIBS/Metal.md)
- [/System/Library/Frameworks/MetalFX.framework/MetalFX](DYLIBS/MetalFX.md)
- [/System/Library/Frameworks/MetalKit.framework/MetalKit](DYLIBS/MetalKit.md)
- [/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSBenchmarkLoop.framework/MPSBenchmarkLoop](DYLIBS/MPSBenchmarkLoop.md)
- [/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSCore.framework/MPSCore](DYLIBS/MPSCore.md)
- [/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSFunctions.framework/MPSFunctions](DYLIBS/MPSFunctions.md)
- [/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSImage.framework/MPSImage](DYLIBS/MPSImage.md)
- [/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSMatrix.framework/MPSMatrix](DYLIBS/MPSMatrix.md)
- [/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNDArray.framework/MPSNDArray](DYLIBS/MPSNDArray.md)
- [/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork](DYLIBS/MPSNeuralNetwork.md)
- [/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSRayIntersector.framework/MPSRayIntersector](DYLIBS/MPSRayIntersector.md)
- [/System/Library/Frameworks/MetalPerformanceShaders.framework/MetalPerformanceShaders](DYLIBS/MetalPerformanceShaders.md)
- [/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph](DYLIBS/MetalPerformanceShadersGraph.md)
- [/System/Library/Frameworks/MetricKit.framework/MetricKit](DYLIBS/MetricKit.md)
- [/System/Library/Frameworks/MobileCoreServices.framework/MobileCoreServices](DYLIBS/MobileCoreServices.md)
- [/System/Library/Frameworks/ModelIO.framework/ModelIO](DYLIBS/ModelIO.md)
- [/System/Library/Frameworks/MultipeerConnectivity.framework/MultipeerConnectivity](DYLIBS/MultipeerConnectivity.md)
- [/System/Library/Frameworks/MusicKit.framework/MusicKit](DYLIBS/MusicKit.md)
- [/System/Library/Frameworks/NaturalLanguage.framework/NaturalLanguage](DYLIBS/NaturalLanguage.md)
- [/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction](DYLIBS/NearbyInteraction.md)
- [/System/Library/Frameworks/Network.framework/Network](DYLIBS/Network.md)
- [/System/Library/Frameworks/NetworkExtension.framework/NetworkExtension](DYLIBS/NetworkExtension.md)
- [/System/Library/Frameworks/NotificationCenter.framework/NotificationCenter](DYLIBS/NotificationCenter.md)
- [/System/Library/Frameworks/OSLog.framework/OSLog](DYLIBS/OSLog.md)
- [/System/Library/Frameworks/OpenAL.framework/OpenAL](DYLIBS/OpenAL.md)
- [/System/Library/Frameworks/OpenGLES.framework/GLEngine.bundle/GLEngine](DYLIBS/GLEngine.md)
- [/System/Library/Frameworks/OpenGLES.framework/OpenGLES](DYLIBS/OpenGLES.md)
- [/System/Library/Frameworks/OpenGLES.framework/libCVMSPluginSupport.dylib](DYLIBS/libCVMSPluginSupport.dylib.md)
- [/System/Library/Frameworks/OpenGLES.framework/libCoreFSCache.dylib](DYLIBS/libCoreFSCache.dylib.md)
- [/System/Library/Frameworks/OpenGLES.framework/libCoreVMClient.dylib](DYLIBS/libCoreVMClient.dylib.md)
- [/System/Library/Frameworks/OpenGLES.framework/libGFXShared.dylib](DYLIBS/libGFXShared.dylib.md)
- [/System/Library/Frameworks/OpenGLES.framework/libGLImage.dylib](DYLIBS/libGLImage.dylib.md)
- [/System/Library/Frameworks/OpenGLES.framework/libGLProgrammability.dylib](DYLIBS/libGLProgrammability.dylib.md)
- [/System/Library/Frameworks/OpenGLES.framework/libGLVMPlugin.dylib](DYLIBS/libGLVMPlugin.dylib.md)
- [/System/Library/Frameworks/PDFKit.framework/PDFKit](DYLIBS/PDFKit.md)
- [/System/Library/Frameworks/PHASE.framework/PHASE](DYLIBS/PHASE.md)
- [/System/Library/Frameworks/PassKit.framework/PassKit](DYLIBS/PassKit.md)
- [/System/Library/Frameworks/PencilKit.framework/PencilKit](DYLIBS/PencilKit.md)
- [/System/Library/Frameworks/Photos.framework/Photos](DYLIBS/Photos.md)
- [/System/Library/Frameworks/PhotosUI.framework/PhotosUI](DYLIBS/PhotosUI.md)
- [/System/Library/Frameworks/ProximityReader.framework/ProximityReader](DYLIBS/ProximityReader.md)
- [/System/Library/Frameworks/PushKit.framework/PushKit](DYLIBS/PushKit.md)
- [/System/Library/Frameworks/PushToTalk.framework/PushToTalk](DYLIBS/PushToTalk.md)
- [/System/Library/Frameworks/QuartzCore.framework/QuartzCore](DYLIBS/QuartzCore.md)
- [/System/Library/Frameworks/QuickLook.framework/QuickLook](DYLIBS/QuickLook.md)
- [/System/Library/Frameworks/QuickLookThumbnailing.framework/QuickLookThumbnailing](DYLIBS/QuickLookThumbnailing.md)
- [/System/Library/Frameworks/RealityFoundation.framework/RealityFoundation](DYLIBS/RealityFoundation.md)
- [/System/Library/Frameworks/RealityKit.framework/RealityKit](DYLIBS/RealityKit.md)
- [/System/Library/Frameworks/ReplayKit.framework/ReplayKit](DYLIBS/ReplayKit.md)
- [/System/Library/Frameworks/RoomPlan.framework/RoomPlan](DYLIBS/RoomPlan.md)
- [/System/Library/Frameworks/SafariServices.framework/SafariServices](DYLIBS/SafariServices.md)
- [/System/Library/Frameworks/SafetyKit.framework/SafetyKit](DYLIBS/SafetyKit.md)
- [/System/Library/Frameworks/SceneKit.framework/SceneKit](DYLIBS/SceneKit.md)
- [/System/Library/Frameworks/ScreenTime.framework/ScreenTime](DYLIBS/ScreenTime.md)
- [/System/Library/Frameworks/Security.framework/Security](DYLIBS/Security.md)
- [/System/Library/Frameworks/SensitiveContentAnalysis.framework/SensitiveContentAnalysis](DYLIBS/SensitiveContentAnalysis.md)
- [/System/Library/Frameworks/SensorKit.framework/SensorKit](DYLIBS/SensorKit.md)
- [/System/Library/Frameworks/SharedWithYou.framework/SharedWithYou](DYLIBS/SharedWithYou.md)
- [/System/Library/Frameworks/SharedWithYouCore.framework/SharedWithYouCore](DYLIBS/SharedWithYouCore.md)
- [/System/Library/Frameworks/ShazamKit.framework/ShazamKit](DYLIBS/ShazamKit.md)
- [/System/Library/Frameworks/Social.framework/Social](DYLIBS/Social.md)
- [/System/Library/Frameworks/SoundAnalysis.framework/SoundAnalysis](DYLIBS/SoundAnalysis.md)
- [/System/Library/Frameworks/Speech.framework/Speech](DYLIBS/Speech.md)
- [/System/Library/Frameworks/SpriteKit.framework/SpriteKit](DYLIBS/SpriteKit.md)
- [/System/Library/Frameworks/StoreKit.framework/StoreKit](DYLIBS/StoreKit.md)
- [/System/Library/Frameworks/SwiftData.framework/SwiftData](DYLIBS/SwiftData.md)
- [/System/Library/Frameworks/SwiftUI.framework/SwiftUI](DYLIBS/SwiftUI.md)
- [/System/Library/Frameworks/Symbols.framework/Symbols](DYLIBS/Symbols.md)
- [/System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration](DYLIBS/SystemConfiguration.md)
- [/System/Library/Frameworks/TabularData.framework/TabularData](DYLIBS/TabularData.md)
- [/System/Library/Frameworks/ThreadNetwork.framework/ThreadNetwork](DYLIBS/ThreadNetwork.md)
- [/System/Library/Frameworks/TipKit.framework/TipKit](DYLIBS/TipKit.md)
- [/System/Library/Frameworks/TipsNext.framework/TipsNext](DYLIBS/TipsNext.md)
- [/System/Library/Frameworks/Twitter.framework/Twitter](DYLIBS/Twitter.md)
- [/System/Library/Frameworks/UIKit.framework/UIKit](DYLIBS/UIKit.md)
- [/System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers](DYLIBS/UniformTypeIdentifiers.md)
- [/System/Library/Frameworks/UserNotifications.framework/UserNotifications](DYLIBS/UserNotifications.md)
- [/System/Library/Frameworks/UserNotificationsUI.framework/UserNotificationsUI](DYLIBS/UserNotificationsUI.md)
- [/System/Library/Frameworks/VideoSubscriberAccount.framework/VideoSubscriberAccount](DYLIBS/VideoSubscriberAccount.md)
- [/System/Library/Frameworks/VideoToolbox.framework/VideoToolbox](DYLIBS/VideoToolbox.md)
- [/System/Library/Frameworks/Vision.framework/Vision](DYLIBS/Vision.md)
- [/System/Library/Frameworks/Vision.framework/libfaceCore.dylib](DYLIBS/libfaceCore.dylib.md)
- [/System/Library/Frameworks/VisionKit.framework/VisionKit](DYLIBS/VisionKit.md)
- [/System/Library/Frameworks/WatchConnectivity.framework/WatchConnectivity](DYLIBS/WatchConnectivity.md)
- [/System/Library/Frameworks/WatchKit.framework/WatchKit](DYLIBS/WatchKit.md)
- [/System/Library/Frameworks/WeatherKit.framework/WeatherKit](DYLIBS/WeatherKit.md)
- [/System/Library/Frameworks/WebKit.framework/WebKit](DYLIBS/WebKit.md)
- [/System/Library/Frameworks/WidgetKit.framework/WidgetKit](DYLIBS/WidgetKit.md)
- [/System/Library/Frameworks/WorkoutKit.framework/WorkoutKit](DYLIBS/WorkoutKit.md)
- [/System/Library/Frameworks/_AVKit_SwiftUI.framework/_AVKit_SwiftUI](DYLIBS/_AVKit_SwiftUI.md)
- [/System/Library/Frameworks/_AppIntents_SwiftUI.framework/_AppIntents_SwiftUI](DYLIBS/_AppIntents_SwiftUI.md)
- [/System/Library/Frameworks/_AppIntents_UIKit.framework/_AppIntents_UIKit](DYLIBS/_AppIntents_UIKit.md)
- [/System/Library/Frameworks/_AuthenticationServices_SwiftUI.framework/_AuthenticationServices_SwiftUI](DYLIBS/_AuthenticationServices_SwiftUI.md)
- [/System/Library/Frameworks/_CoreData_CloudKit.framework/_CoreData_CloudKit](DYLIBS/_CoreData_CloudKit.md)
- [/System/Library/Frameworks/_CoreLocationUI_SwiftUI.framework/_CoreLocationUI_SwiftUI](DYLIBS/_CoreLocationUI_SwiftUI.md)
- [/System/Library/Frameworks/_DeviceActivity_SwiftUI.framework/_DeviceActivity_SwiftUI](DYLIBS/_DeviceActivity_SwiftUI.md)
- [/System/Library/Frameworks/_GroupActivities_UIKit.framework/_GroupActivities_UIKit](DYLIBS/_GroupActivities_UIKit.md)
- [/System/Library/Frameworks/_HomeKit_SwiftUI.framework/_HomeKit_SwiftUI](DYLIBS/_HomeKit_SwiftUI.md)
- [/System/Library/Frameworks/_ManagedAppDistribution_SwiftUI.framework/_ManagedAppDistribution_SwiftUI](DYLIBS/_ManagedAppDistribution_SwiftUI.md)
- [/System/Library/Frameworks/_MapKit_SwiftUI.framework/_MapKit_SwiftUI](DYLIBS/_MapKit_SwiftUI.md)
- [/System/Library/Frameworks/_MusicKit_SwiftUI.framework/_MusicKit_SwiftUI](DYLIBS/_MusicKit_SwiftUI.md)
- [/System/Library/Frameworks/_PassKit_SwiftUI.framework/_PassKit_SwiftUI](DYLIBS/_PassKit_SwiftUI.md)
- [/System/Library/Frameworks/_PhotosUI_SwiftUI.framework/_PhotosUI_SwiftUI](DYLIBS/_PhotosUI_SwiftUI.md)
- [/System/Library/Frameworks/_QuickLook_SwiftUI.framework/_QuickLook_SwiftUI](DYLIBS/_QuickLook_SwiftUI.md)
- [/System/Library/Frameworks/_RealityKit_SwiftUI.framework/_RealityKit_SwiftUI](DYLIBS/_RealityKit_SwiftUI.md)
- [/System/Library/Frameworks/_SceneKit_SwiftUI.framework/_SceneKit_SwiftUI](DYLIBS/_SceneKit_SwiftUI.md)
- [/System/Library/Frameworks/_SpriteKit_SwiftUI.framework/_SpriteKit_SwiftUI](DYLIBS/_SpriteKit_SwiftUI.md)
- [/System/Library/Frameworks/_StoreKit_SwiftUI.framework/_StoreKit_SwiftUI](DYLIBS/_StoreKit_SwiftUI.md)
- [/System/Library/Frameworks/_SwiftData_CoreData.framework/_SwiftData_CoreData](DYLIBS/_SwiftData_CoreData.md)
- [/System/Library/Frameworks/_SwiftData_SwiftUI.framework/_SwiftData_SwiftUI](DYLIBS/_SwiftData_SwiftUI.md)
- [/System/Library/Frameworks/_WorkoutKit_SwiftUI.framework/_WorkoutKit_SwiftUI](DYLIBS/_WorkoutKit_SwiftUI.md)
- [/System/Library/Frameworks/iAd.framework/iAd](DYLIBS/iAd.md)
- [/System/Library/HIDPlugins/AppleSPUAccCompassPlugin.plugin/AppleSPUAccCompassPlugin](DYLIBS/AppleSPUAccCompassPlugin.md)
- [/System/Library/HIDPlugins/AppleSPUDispCompassPlugin.plugin/AppleSPUDispCompassPlugin](DYLIBS/AppleSPUDispCompassPlugin.md)
- [/System/Library/HIDPlugins/AppleSPUHIDStatistics.plugin/AppleSPUHIDStatistics](DYLIBS/AppleSPUHIDStatistics.md)
- [/System/Library/HIDPlugins/AttentionAwarenessFilter.plugin/AttentionAwarenessFilter](DYLIBS/AttentionAwarenessFilter.md)
- [/System/Library/HIDPlugins/IOHIDEventProcessorFilter.plugin/IOHIDEventProcessorFilter](DYLIBS/IOHIDEventProcessorFilter.md)
- [/System/Library/HIDPlugins/IOHIDEventSystemStatistics.plugin/IOHIDEventSystemStatistics](DYLIBS/IOHIDEventSystemStatistics.md)
- [/System/Library/HIDPlugins/IOHIDKeyboardFilter.plugin/IOHIDKeyboardFilter](DYLIBS/IOHIDKeyboardFilter.md)
- [/System/Library/HIDPlugins/IOHIDPointerScrollFilter.plugin/IOHIDPointerScrollFilter](DYLIBS/IOHIDPointerScrollFilter.md)
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
- [/System/Library/Health/Plugins/ActivityAchievementsPlugin.bundle/ActivityAchievementsPlugin](DYLIBS/ActivityAchievementsPlugin.md)
- [/System/Library/Health/Plugins/ActivityAwardsPlugin.bundle/ActivityAwardsPlugin](DYLIBS/ActivityAwardsPlugin.md)
- [/System/Library/Health/Plugins/ActivitySharingPlugin.bundle/ActivitySharingPlugin](DYLIBS/ActivitySharingPlugin.md)
- [/System/Library/Health/Plugins/CompanionHealthPlugin.bundle/CompanionHealthPlugin](DYLIBS/CompanionHealthPlugin.md)
- [/System/Library/Health/Plugins/HealthAppPlugin.bundle/HealthAppPlugin](DYLIBS/HealthAppPlugin.md)
- [/System/Library/Health/Plugins/HeartDaemonPlugin.bundle/HeartDaemonPlugin](DYLIBS/HeartDaemonPlugin.md)
- [/System/Library/Health/Plugins/MenstrualCyclesDaemonPlugin.bundle/MenstrualCyclesDaemonPlugin](DYLIBS/MenstrualCyclesDaemonPlugin.md)
- [/System/Library/Health/Plugins/RespiratoryHealthDaemonPlugin.bundle/RespiratoryHealthDaemonPlugin](DYLIBS/RespiratoryHealthDaemonPlugin.md)
- [/System/Library/Health/Plugins/SleepHealthDaemonPlugin.bundle/SleepHealthDaemonPlugin](DYLIBS/SleepHealthDaemonPlugin.md)
- [/System/Library/MediaCapture/H16ISP.mediacapture](DYLIBS/H16ISP.mediacapture.md)
- [/System/Library/Messages/PlugIns/FaceTime.imservice/FaceTime](DYLIBS/FaceTime.md)
- [/System/Library/Messages/PlugIns/SMS.imservice/SMS](DYLIBS/SMS.md)
- [/System/Library/Messages/PlugIns/iMessage.imservice/iMessage](DYLIBS/iMessage.md)
- [/System/Library/NanoPreferenceBundles/General/AccessibilitySettings.bundle/AccessibilitySettings](DYLIBS/AccessibilitySettings.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/MessagesComplication.bundle/MessagesComplication](DYLIBS/MessagesComplication.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/NanoCompassComplications.bundle/NanoCompassComplications](DYLIBS/NanoCompassComplications.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/NanoMenstrualCyclesComplication.bundle/NanoMenstrualCyclesComplication](DYLIBS/NanoMenstrualCyclesComplication.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/NanoSleepComplication.bundle/NanoSleepComplication](DYLIBS/NanoSleepComplication.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/WeatherComplications.bundle/WeatherComplications](DYLIBS/WeatherComplications.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/WorldClockComplications.bundle/WorldClockComplications](DYLIBS/WorldClockComplications.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKAegirFaceBundleCompanion.bundle/NTKAegirFaceBundleCompanion](DYLIBS/NTKAegirFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKEsterbrookFaceBundleCompanion.bundle/NTKEsterbrookFaceBundleCompanion](DYLIBS/NTKEsterbrookFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKExtragalacticFaceBundleCompanion.bundle/NTKExtragalacticFaceBundleCompanion](DYLIBS/NTKExtragalacticFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKFoghornFaceBundleCompanion.bundle/NTKFoghornFaceBundleCompanion](DYLIBS/NTKFoghornFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKGalleonFaceBundleCompanion.bundle/NTKGalleonFaceBundleCompanion](DYLIBS/NTKGalleonFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKSnowglobeFaceBundleCompanion.bundle/NTKSnowglobeFaceBundleCompanion](DYLIBS/NTKSnowglobeFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKVivaldiFaceBundleCompanion.bundle/NTKVivaldiFaceBundleCompanion](DYLIBS/NTKVivaldiFaceBundleCompanion.md)
- [/System/Library/PreferenceBundles/AirPortSettings.bundle/AirPortSettings](DYLIBS/AirPortSettings.md)
- [/System/Library/PreferenceBundles/BluetoothSettings.bundle/BluetoothSettings](DYLIBS/BluetoothSettings.md)
- [/System/Library/PreferenceBundles/CarrierSettings.bundle/CarrierSettings](DYLIBS/CarrierSettings.md)
- [/System/Library/PreferenceBundles/ContactsSettings.bundle/ContactsSettings](DYLIBS/ContactsSettings.md)
- [/System/Library/PreferenceBundles/EDGESettings.bundle/EDGESettings](DYLIBS/EDGESettings.md)
- [/System/Library/PreferenceBundles/KeyboardSettings.bundle/KeyboardSettings](DYLIBS/KeyboardSettings.md)
- [/System/Library/PreferenceBundles/MobileCalSettings.bundle/MobileCalSettings](DYLIBS/MobileCalSettings.md)
- [/System/Library/PreferenceBundles/MobilePhoneSettings.bundle/MobilePhoneSettings](DYLIBS/MobilePhoneSettings.md)
- [/System/Library/PreferenceBundles/ScheduleSettings.bundle/ScheduleSettings](DYLIBS/ScheduleSettings.md)
- [/System/Library/PreferenceBundles/VPNPreferences.bundle/VPNPreferences](DYLIBS/VPNPreferences.md)
- [/System/Library/PreferenceBundles/WirelessModemSettings.bundle/WirelessModemSettings](DYLIBS/WirelessModemSettings.md)
- [/System/Library/Previews/ShellPlugins/WidgetPreviewsShellPlugin.bundle/WidgetPreviewsShellPlugin](DYLIBS/WidgetPreviewsShellPlugin.md)
- [/System/Library/PrivateFrameworks/AAAFoundation.framework/AAAFoundation](DYLIBS/AAAFoundation.md)
- [/System/Library/PrivateFrameworks/AAAFoundationSwift.framework/AAAFoundationSwift](DYLIBS/AAAFoundationSwift.md)
- [/System/Library/PrivateFrameworks/AACCore.framework/AACCore](DYLIBS/AACCore.md)
- [/System/Library/PrivateFrameworks/ABMHelper.framework/ABMHelper](DYLIBS/ABMHelper.md)
- [/System/Library/PrivateFrameworks/ACCBaker.framework/ACCBaker](DYLIBS/ACCBaker.md)
- [/System/Library/PrivateFrameworks/ACSEFoundation.framework/ACSEFoundation](DYLIBS/ACSEFoundation.md)
- [/System/Library/PrivateFrameworks/ACTFramework.framework/ACTFramework](DYLIBS/ACTFramework.md)
- [/System/Library/PrivateFrameworks/AFKUser.framework/AFKUser](DYLIBS/AFKUser.md)
- [/System/Library/PrivateFrameworks/AGXCompilerConnection-S2A8.framework/AGXCompilerConnection-S2A8](DYLIBS/AGXCompilerConnection-S2A8.md)
- [/System/Library/PrivateFrameworks/AGXCompilerCore-S2A8.framework/AGXCompilerCore-S2A8](DYLIBS/AGXCompilerCore-S2A8.md)
- [/System/Library/PrivateFrameworks/AGXCompilerCore.framework/AGXCompilerCore](DYLIBS/AGXCompilerCore.md)
- [/System/Library/PrivateFrameworks/AGXGPURawCounter.framework/AGXGPURawCounter](DYLIBS/AGXGPURawCounter.md)
- [/System/Library/PrivateFrameworks/AIMLExperimentationAnalytics.framework/AIMLExperimentationAnalytics](DYLIBS/AIMLExperimentationAnalytics.md)
- [/System/Library/PrivateFrameworks/AIMLInstrumentationStreams.framework/AIMLInstrumentationStreams](DYLIBS/AIMLInstrumentationStreams.md)
- [/System/Library/PrivateFrameworks/AMPCoreUI.framework/AMPCoreUI](DYLIBS/AMPCoreUI.md)
- [/System/Library/PrivateFrameworks/ANECompiler.framework/ANECompiler](DYLIBS/ANECompiler.md)
- [/System/Library/PrivateFrameworks/ANECompiler.framework/libORTools.dylib](DYLIBS/libORTools.dylib.md)
- [/System/Library/PrivateFrameworks/ANEServices.framework/ANEServices](DYLIBS/ANEServices.md)
- [/System/Library/PrivateFrameworks/ANSTKit.framework/ANSTKit](DYLIBS/ANSTKit.md)
- [/System/Library/PrivateFrameworks/AOPHaptics.framework/AOPHaptics](DYLIBS/AOPHaptics.md)
- [/System/Library/PrivateFrameworks/AOSKit.framework/AOSKit](DYLIBS/AOSKit.md)
- [/System/Library/PrivateFrameworks/APConfigurationSystem.framework/APConfigurationSystem](DYLIBS/APConfigurationSystem.md)
- [/System/Library/PrivateFrameworks/APFS.framework/APFS](DYLIBS/APFS.md)
- [/System/Library/PrivateFrameworks/APFoundation.framework/APFoundation](DYLIBS/APFoundation.md)
- [/System/Library/PrivateFrameworks/APTransport.framework/APTransport](DYLIBS/APTransport.md)
- [/System/Library/PrivateFrameworks/ARKitCore.framework/ARKitCore](DYLIBS/ARKitCore.md)
- [/System/Library/PrivateFrameworks/ARKitDaemon.framework/ARKitDaemon](DYLIBS/ARKitDaemon.md)
- [/System/Library/PrivateFrameworks/ARKitFoundation.framework/ARKitFoundation](DYLIBS/ARKitFoundation.md)
- [/System/Library/PrivateFrameworks/ARKitUI.framework/ARKitUI](DYLIBS/ARKitUI.md)
- [/System/Library/PrivateFrameworks/ASEProcessing.framework/ASEProcessing](DYLIBS/ASEProcessing.md)
- [/System/Library/PrivateFrameworks/ASOctaneSupport.framework/ASOctaneSupport](DYLIBS/ASOctaneSupport.md)
- [/System/Library/PrivateFrameworks/ATFoundation.framework/ATFoundation](DYLIBS/ATFoundation.md)
- [/System/Library/PrivateFrameworks/AUDeveloperSettings.framework/AUDeveloperSettings](DYLIBS/AUDeveloperSettings.md)
- [/System/Library/PrivateFrameworks/AUSettings.framework/AUSettings](DYLIBS/AUSettings.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/AVConference](DYLIBS/AVConference.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/GKSPerformance.framework/GKSPerformance](DYLIBS/GKSPerformance.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ICE.framework/ICE](DYLIBS/ICE.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/LegacyHandle.framework/LegacyHandle](DYLIBS/LegacyHandle.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/SimpleKeyExchange.framework/SimpleKeyExchange](DYLIBS/SimpleKeyExchange.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ViceroyTrace.framework/ViceroyTrace](DYLIBS/ViceroyTrace.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/snatmap.framework/snatmap](DYLIBS/snatmap.md)
- [/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture](DYLIBS/AVFCapture.md)
- [/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore](DYLIBS/AVFCore.md)
- [/System/Library/PrivateFrameworks/AXAggregateStatisticsServices.framework/AXAggregateStatisticsServices](DYLIBS/AXAggregateStatisticsServices.md)
- [/System/Library/PrivateFrameworks/AXAssetLoader.framework/AXAssetLoader](DYLIBS/AXAssetLoader.md)
- [/System/Library/PrivateFrameworks/AXContainerServices.framework/AXContainerServices](DYLIBS/AXContainerServices.md)
- [/System/Library/PrivateFrameworks/AXCoreUtilities.framework/AXCoreUtilities](DYLIBS/AXCoreUtilities.md)
- [/System/Library/PrivateFrameworks/AXElementInteraction.framework/AXElementInteraction](DYLIBS/AXElementInteraction.md)
- [/System/Library/PrivateFrameworks/AXFrontBoardUtils.framework/AXFrontBoardUtils](DYLIBS/AXFrontBoardUtils.md)
- [/System/Library/PrivateFrameworks/AXIDSServices.framework/AXIDSServices](DYLIBS/AXIDSServices.md)
- [/System/Library/PrivateFrameworks/AXLocalizationCaptionService.framework/AXLocalizationCaptionService](DYLIBS/AXLocalizationCaptionService.md)
- [/System/Library/PrivateFrameworks/AXMediaUtilities.framework/AXMediaUtilities](DYLIBS/AXMediaUtilities.md)
- [/System/Library/PrivateFrameworks/AXNTKUtilities.framework/AXNTKUtilities](DYLIBS/AXNTKUtilities.md)
- [/System/Library/PrivateFrameworks/AXRuntime.framework/AXRuntime](DYLIBS/AXRuntime.md)
- [/System/Library/PrivateFrameworks/AXSoundDetection.framework/AXSoundDetection](DYLIBS/AXSoundDetection.md)
- [/System/Library/PrivateFrameworks/AXSoundDetectionUI.framework/AXSoundDetectionUI](DYLIBS/AXSoundDetectionUI.md)
- [/System/Library/PrivateFrameworks/AXSpeakFingerManager.framework/AXSpeakFingerManager](DYLIBS/AXSpeakFingerManager.md)
- [/System/Library/PrivateFrameworks/AXSpeechAssetServices.framework/AXSpeechAssetServices](DYLIBS/AXSpeechAssetServices.md)
- [/System/Library/PrivateFrameworks/AXSpringBoardServerInstance.framework/AXSpringBoardServerInstance](DYLIBS/AXSpringBoardServerInstance.md)
- [/System/Library/PrivateFrameworks/AXTapToSpeakTime.framework/AXTapToSpeakTime](DYLIBS/AXTapToSpeakTime.md)
- [/System/Library/PrivateFrameworks/AXWatchRemoteScreenServices.framework/AXWatchRemoteScreenServices](DYLIBS/AXWatchRemoteScreenServices.md)
- [/System/Library/PrivateFrameworks/AXWatchRemoteScreenUI.framework/AXWatchRemoteScreenUI](DYLIBS/AXWatchRemoteScreenUI.md)
- [/System/Library/PrivateFrameworks/AccelerateGPU.framework/AccelerateGPU](DYLIBS/AccelerateGPU.md)
- [/System/Library/PrivateFrameworks/AccessibilityAudit.framework/AccessibilityAudit](DYLIBS/AccessibilityAudit.md)
- [/System/Library/PrivateFrameworks/AccessibilityFocusEngine.framework/AccessibilityFocusEngine](DYLIBS/AccessibilityFocusEngine.md)
- [/System/Library/PrivateFrameworks/AccessibilityPhysicalInteraction.framework/AccessibilityPhysicalInteraction](DYLIBS/AccessibilityPhysicalInteraction.md)
- [/System/Library/PrivateFrameworks/AccessibilityPlatformTranslation.framework/AccessibilityPlatformTranslation](DYLIBS/AccessibilityPlatformTranslation.md)
- [/System/Library/PrivateFrameworks/AccessibilityRemoteServices.framework/AccessibilityRemoteServices](DYLIBS/AccessibilityRemoteServices.md)
- [/System/Library/PrivateFrameworks/AccessibilityRemoteUIServices.framework/AccessibilityRemoteUIServices](DYLIBS/AccessibilityRemoteUIServices.md)
- [/System/Library/PrivateFrameworks/AccessibilitySharedSupport.framework/AccessibilitySharedSupport](DYLIBS/AccessibilitySharedSupport.md)
- [/System/Library/PrivateFrameworks/AccessibilitySharedUISupport.framework/AccessibilitySharedUISupport](DYLIBS/AccessibilitySharedUISupport.md)
- [/System/Library/PrivateFrameworks/AccessibilityUI.framework/AccessibilityUI](DYLIBS/AccessibilityUI.md)
- [/System/Library/PrivateFrameworks/AccessibilityUIService.framework/AccessibilityUIService](DYLIBS/AccessibilityUIService.md)
- [/System/Library/PrivateFrameworks/AccessibilityUIShared.framework/AccessibilityUIShared](DYLIBS/AccessibilityUIShared.md)
- [/System/Library/PrivateFrameworks/AccessibilityUIUtilities.framework/AccessibilityUIUtilities](DYLIBS/AccessibilityUIUtilities.md)
- [/System/Library/PrivateFrameworks/AccessibilityUIViewServices.framework/AccessibilityUIViewServices](DYLIBS/AccessibilityUIViewServices.md)
- [/System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities](DYLIBS/AccessibilityUtilities.md)
- [/System/Library/PrivateFrameworks/AccessoryAssistiveTouch.framework/AccessoryAssistiveTouch](DYLIBS/AccessoryAssistiveTouch.md)
- [/System/Library/PrivateFrameworks/AccessoryAudio.framework/AccessoryAudio](DYLIBS/AccessoryAudio.md)
- [/System/Library/PrivateFrameworks/AccessoryBLEPairing.framework/AccessoryBLEPairing](DYLIBS/AccessoryBLEPairing.md)
- [/System/Library/PrivateFrameworks/AccessoryCommunications.framework/AccessoryCommunications](DYLIBS/AccessoryCommunications.md)
- [/System/Library/PrivateFrameworks/AccessoryComponentAuth.framework/AccessoryComponentAuth](DYLIBS/AccessoryComponentAuth.md)
- [/System/Library/PrivateFrameworks/AccessoryHID.framework/AccessoryHID](DYLIBS/AccessoryHID.md)
- [/System/Library/PrivateFrameworks/AccessoryMediaLibrary.framework/AccessoryMediaLibrary](DYLIBS/AccessoryMediaLibrary.md)
- [/System/Library/PrivateFrameworks/AccessoryNavigation.framework/AccessoryNavigation](DYLIBS/AccessoryNavigation.md)
- [/System/Library/PrivateFrameworks/AccessoryNowPlaying.framework/AccessoryNowPlaying](DYLIBS/AccessoryNowPlaying.md)
- [/System/Library/PrivateFrameworks/AccessoryOOBBTPairing.framework/AccessoryOOBBTPairing](DYLIBS/AccessoryOOBBTPairing.md)
- [/System/Library/PrivateFrameworks/AccessoryVoiceOver.framework/AccessoryVoiceOver](DYLIBS/AccessoryVoiceOver.md)
- [/System/Library/PrivateFrameworks/AccessoryiAP2Shim.framework/AccessoryiAP2Shim](DYLIBS/AccessoryiAP2Shim.md)
- [/System/Library/PrivateFrameworks/AccountNotification.framework/AccountNotification](DYLIBS/AccountNotification.md)
- [/System/Library/PrivateFrameworks/AccountsDaemon.framework/AccountsDaemon](DYLIBS/AccountsDaemon.md)
- [/System/Library/PrivateFrameworks/AccountsUI.framework/AccountsUI](DYLIBS/AccountsUI.md)
- [/System/Library/PrivateFrameworks/AcousticMaterials.framework/AcousticMaterials](DYLIBS/AcousticMaterials.md)
- [/System/Library/PrivateFrameworks/ActionButtonConfigurationUI.framework/ActionButtonConfigurationUI](DYLIBS/ActionButtonConfigurationUI.md)
- [/System/Library/PrivateFrameworks/ActionButtonSelector.framework/ActionButtonSelector](DYLIBS/ActionButtonSelector.md)
- [/System/Library/PrivateFrameworks/ActionKit.framework/ActionKit](DYLIBS/ActionKit.md)
- [/System/Library/PrivateFrameworks/ActionKitUI.framework/ActionKitUI](DYLIBS/ActionKitUI.md)
- [/System/Library/PrivateFrameworks/ActionPredictionHeuristics.framework/ActionPredictionHeuristics](DYLIBS/ActionPredictionHeuristics.md)
- [/System/Library/PrivateFrameworks/ActionPredictionHeuristicsInternal.framework/ActionPredictionHeuristicsInternal](DYLIBS/ActionPredictionHeuristicsInternal.md)
- [/System/Library/PrivateFrameworks/ActivityAchievements.framework/ActivityAchievements](DYLIBS/ActivityAchievements.md)
- [/System/Library/PrivateFrameworks/ActivityAchievementsDaemon.framework/ActivityAchievementsDaemon](DYLIBS/ActivityAchievementsDaemon.md)
- [/System/Library/PrivateFrameworks/ActivityAchievementsUI.framework/ActivityAchievementsUI](DYLIBS/ActivityAchievementsUI.md)
- [/System/Library/PrivateFrameworks/ActivityAwardsClient.framework/ActivityAwardsClient](DYLIBS/ActivityAwardsClient.md)
- [/System/Library/PrivateFrameworks/ActivityAwardsCore.framework/ActivityAwardsCore](DYLIBS/ActivityAwardsCore.md)
- [/System/Library/PrivateFrameworks/ActivityAwardsServices.framework/ActivityAwardsServices](DYLIBS/ActivityAwardsServices.md)
- [/System/Library/PrivateFrameworks/ActivityRingsUI.framework/ActivityRingsUI](DYLIBS/ActivityRingsUI.md)
- [/System/Library/PrivateFrameworks/ActivitySharing.framework/ActivitySharing](DYLIBS/ActivitySharing.md)
- [/System/Library/PrivateFrameworks/ActivitySharingClient.framework/ActivitySharingClient](DYLIBS/ActivitySharingClient.md)
- [/System/Library/PrivateFrameworks/ActivitySharingDaemonCore.framework/ActivitySharingDaemonCore](DYLIBS/ActivitySharingDaemonCore.md)
- [/System/Library/PrivateFrameworks/ActivitySharingServices.framework/ActivitySharingServices](DYLIBS/ActivitySharingServices.md)
- [/System/Library/PrivateFrameworks/ActivitySharingUI.framework/ActivitySharingUI](DYLIBS/ActivitySharingUI.md)
- [/System/Library/PrivateFrameworks/ActivityUI.framework/ActivityUI](DYLIBS/ActivityUI.md)
- [/System/Library/PrivateFrameworks/ActivityUIServices.framework/ActivityUIServices](DYLIBS/ActivityUIServices.md)
- [/System/Library/PrivateFrameworks/AdCore.framework/AdCore](DYLIBS/AdCore.md)
- [/System/Library/PrivateFrameworks/AdID.framework/AdID](DYLIBS/AdID.md)
- [/System/Library/PrivateFrameworks/AdPlatforms.framework/AdPlatforms](DYLIBS/AdPlatforms.md)
- [/System/Library/PrivateFrameworks/AdPlatformsCommon.framework/AdPlatformsCommon](DYLIBS/AdPlatformsCommon.md)
- [/System/Library/PrivateFrameworks/AdPlatformsCommonUI.framework/AdPlatformsCommonUI](DYLIBS/AdPlatformsCommonUI.md)
- [/System/Library/PrivateFrameworks/AdPlatformsInternal.framework/AdPlatformsInternal](DYLIBS/AdPlatformsInternal.md)
- [/System/Library/PrivateFrameworks/AddressBookLegacy.framework/AddressBookLegacy](DYLIBS/AddressBookLegacy.md)
- [/System/Library/PrivateFrameworks/AdminLite.framework/AdminLite](DYLIBS/AdminLite.md)
- [/System/Library/PrivateFrameworks/AfibBurden.framework/AfibBurden](DYLIBS/AfibBurden.md)
- [/System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary](DYLIBS/AggregateDictionary.md)
- [/System/Library/PrivateFrameworks/AggregateDictionaryHistory.framework/AggregateDictionaryHistory](DYLIBS/AggregateDictionaryHistory.md)
- [/System/Library/PrivateFrameworks/AirPlayKit.framework/AirPlayKit](DYLIBS/AirPlayKit.md)
- [/System/Library/PrivateFrameworks/AirPlayReceiver.framework/AirPlayReceiver](DYLIBS/AirPlayReceiver.md)
- [/System/Library/PrivateFrameworks/AirPlayReceiverKit.framework/AirPlayReceiverKit](DYLIBS/AirPlayReceiverKit.md)
- [/System/Library/PrivateFrameworks/AirPlayRoutePrediction.framework/AirPlayRoutePrediction](DYLIBS/AirPlayRoutePrediction.md)
- [/System/Library/PrivateFrameworks/AirPlaySender.framework/AirPlaySender](DYLIBS/AirPlaySender.md)
- [/System/Library/PrivateFrameworks/AirPlaySenderUI.framework/AirPlaySenderUI](DYLIBS/AirPlaySenderUI.md)
- [/System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport](DYLIBS/AirPlaySupport.md)
- [/System/Library/PrivateFrameworks/AirPortAssistant.framework/AirPortAssistant](DYLIBS/AirPortAssistant.md)
- [/System/Library/PrivateFrameworks/AirTraffic.framework/AirTraffic](DYLIBS/AirTraffic.md)
- [/System/Library/PrivateFrameworks/AirTrafficDevice.framework/AirTrafficDevice](DYLIBS/AirTrafficDevice.md)
- [/System/Library/PrivateFrameworks/AlgosScoreFramework.framework/AlgosScoreFramework](DYLIBS/AlgosScoreFramework.md)
- [/System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit](DYLIBS/AltruisticBodyPoseKit.md)
- [/System/Library/PrivateFrameworks/Ambient.framework/Ambient](DYLIBS/Ambient.md)
- [/System/Library/PrivateFrameworks/AmbientUI.framework/AmbientUI](DYLIBS/AmbientUI.md)
- [/System/Library/PrivateFrameworks/AmbientUIKit.framework/AmbientUIKit](DYLIBS/AmbientUIKit.md)
- [/System/Library/PrivateFrameworks/AmbientUIServices.framework/AmbientUIServices](DYLIBS/AmbientUIServices.md)
- [/System/Library/PrivateFrameworks/AnnotationKit.framework/AnnotationKit](DYLIBS/AnnotationKit.md)
- [/System/Library/PrivateFrameworks/Announce.framework/Announce](DYLIBS/Announce.md)
- [/System/Library/PrivateFrameworks/AnnounceDaemon.framework/AnnounceDaemon](DYLIBS/AnnounceDaemon.md)
- [/System/Library/PrivateFrameworks/AnnounceSiriExtensions.framework/AnnounceSiriExtensions](DYLIBS/AnnounceSiriExtensions.md)
- [/System/Library/PrivateFrameworks/AppAnalytics.framework/AppAnalytics](DYLIBS/AppAnalytics.md)
- [/System/Library/PrivateFrameworks/AppAttestInternal.framework/AppAttestInternal](DYLIBS/AppAttestInternal.md)
- [/System/Library/PrivateFrameworks/AppC3D.framework/AppC3D](DYLIBS/AppC3D.md)
- [/System/Library/PrivateFrameworks/AppConduit.framework/AppConduit](DYLIBS/AppConduit.md)
- [/System/Library/PrivateFrameworks/AppInstallationMetrics.framework/AppInstallationMetrics](DYLIBS/AppInstallationMetrics.md)
- [/System/Library/PrivateFrameworks/AppNotificationsLoggingClient.framework/AppNotificationsLoggingClient](DYLIBS/AppNotificationsLoggingClient.md)
- [/System/Library/PrivateFrameworks/AppPredictionClient.framework/AppPredictionClient](DYLIBS/AppPredictionClient.md)
- [/System/Library/PrivateFrameworks/AppPredictionFoundation.framework/AppPredictionFoundation](DYLIBS/AppPredictionFoundation.md)
- [/System/Library/PrivateFrameworks/AppPredictionInternal.framework/AppPredictionInternal](DYLIBS/AppPredictionInternal.md)
- [/System/Library/PrivateFrameworks/AppPredictionUI.framework/AppPredictionUI](DYLIBS/AppPredictionUI.md)
- [/System/Library/PrivateFrameworks/AppPredictionUIFoundation.framework/AppPredictionUIFoundation](DYLIBS/AppPredictionUIFoundation.md)
- [/System/Library/PrivateFrameworks/AppPredictionUIWidget.framework/AppPredictionUIWidget](DYLIBS/AppPredictionUIWidget.md)
- [/System/Library/PrivateFrameworks/AppSSO.framework/AppSSO](DYLIBS/AppSSO.md)
- [/System/Library/PrivateFrameworks/AppSSOCore.framework/AppSSOCore](DYLIBS/AppSSOCore.md)
- [/System/Library/PrivateFrameworks/AppSSOKerberos.framework/AppSSOKerberos](DYLIBS/AppSSOKerberos.md)
- [/System/Library/PrivateFrameworks/AppSSOUI.framework/AppSSOUI](DYLIBS/AppSSOUI.md)
- [/System/Library/PrivateFrameworks/AppServerSupport.framework/AppServerSupport](DYLIBS/AppServerSupport.md)
- [/System/Library/PrivateFrameworks/AppState.framework/AppState](DYLIBS/AppState.md)
- [/System/Library/PrivateFrameworks/AppStoreComponents.framework/AppStoreComponents](DYLIBS/AppStoreComponents.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon](DYLIBS/AppStoreDaemon.md)
- [/System/Library/PrivateFrameworks/AppStoreFoundation.framework/AppStoreFoundation](DYLIBS/AppStoreFoundation.md)
- [/System/Library/PrivateFrameworks/AppStoreKit.framework/AppStoreKit](DYLIBS/AppStoreKit.md)
- [/System/Library/PrivateFrameworks/AppStoreKitInternal.framework/AppStoreKitInternal](DYLIBS/AppStoreKitInternal.md)
- [/System/Library/PrivateFrameworks/AppStoreOverlays.framework/AppStoreOverlays](DYLIBS/AppStoreOverlays.md)
- [/System/Library/PrivateFrameworks/AppStoreUI.framework/AppStoreUI](DYLIBS/AppStoreUI.md)
- [/System/Library/PrivateFrameworks/AppSupport.framework/AppSupport](DYLIBS/AppSupport.md)
- [/System/Library/PrivateFrameworks/AppSupportUI.framework/AppSupportUI](DYLIBS/AppSupportUI.md)
- [/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount](DYLIBS/AppleAccount.md)
- [/System/Library/PrivateFrameworks/AppleAccountUI.framework/AppleAccountUI](DYLIBS/AppleAccountUI.md)
- [/System/Library/PrivateFrameworks/AppleBasebandManager.framework/AppleBasebandManager](DYLIBS/AppleBasebandManager.md)
- [/System/Library/PrivateFrameworks/AppleBasebandServices.framework/AppleBasebandServices](DYLIBS/AppleBasebandServices.md)
- [/System/Library/PrivateFrameworks/AppleCV3D.framework/AppleCV3D](DYLIBS/AppleCV3D.md)
- [/System/Library/PrivateFrameworks/AppleCV3DHA.framework/AppleCV3DHA](DYLIBS/AppleCV3DHA.md)
- [/System/Library/PrivateFrameworks/AppleCV3DMOVKit.framework/AppleCV3DMOVKit](DYLIBS/AppleCV3DMOVKit.md)
- [/System/Library/PrivateFrameworks/AppleCV3DModels.framework/AppleCV3DModels](DYLIBS/AppleCV3DModels.md)
- [/System/Library/PrivateFrameworks/AppleCVA.framework/AppleCVA](DYLIBS/AppleCVA.md)
- [/System/Library/PrivateFrameworks/AppleCVAPhoto.framework/AppleCVAPhoto](DYLIBS/AppleCVAPhoto.md)
- [/System/Library/PrivateFrameworks/AppleCVHWA.framework/AppleCVHWA](DYLIBS/AppleCVHWA.md)
- [/System/Library/PrivateFrameworks/AppleCareSupport.framework/AppleCareSupport](DYLIBS/AppleCareSupport.md)
- [/System/Library/PrivateFrameworks/AppleConvergedFirmwareUpdater.framework/AppleConvergedFirmwareUpdater](DYLIBS/AppleConvergedFirmwareUpdater.md)
- [/System/Library/PrivateFrameworks/AppleDepth.framework/AppleDepth](DYLIBS/AppleDepth.md)
- [/System/Library/PrivateFrameworks/AppleDepthCore.framework/AppleDepthCore](DYLIBS/AppleDepthCore.md)
- [/System/Library/PrivateFrameworks/AppleFSCompression.framework/AppleFSCompression](DYLIBS/AppleFSCompression.md)
- [/System/Library/PrivateFrameworks/AppleFirmwareUpdate.framework/AppleFirmwareUpdate](DYLIBS/AppleFirmwareUpdate.md)
- [/System/Library/PrivateFrameworks/AppleFlatBuffers.framework/AppleFlatBuffers](DYLIBS/AppleFlatBuffers.md)
- [/System/Library/PrivateFrameworks/AppleHIDTransportSupport.framework/AppleHIDTransportSupport](DYLIBS/AppleHIDTransportSupport.md)
- [/System/Library/PrivateFrameworks/AppleIDAuthSupport.framework/AppleIDAuthSupport](DYLIBS/AppleIDAuthSupport.md)
- [/System/Library/PrivateFrameworks/AppleIDSSOAuthentication.framework/AppleIDSSOAuthentication](DYLIBS/AppleIDSSOAuthentication.md)
- [/System/Library/PrivateFrameworks/AppleIDSetup.framework/AppleIDSetup](DYLIBS/AppleIDSetup.md)
- [/System/Library/PrivateFrameworks/AppleIDSetupUI.framework/AppleIDSetupUI](DYLIBS/AppleIDSetupUI.md)
- [/System/Library/PrivateFrameworks/AppleJPEG.framework/AppleJPEG](DYLIBS/AppleJPEG.md)
- [/System/Library/PrivateFrameworks/AppleJPEGXL.framework/AppleJPEGXL](DYLIBS/AppleJPEGXL.md)
- [/System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore](DYLIBS/AppleKeyStore.md)
- [/System/Library/PrivateFrameworks/AppleLDAP.framework/AppleLDAP](DYLIBS/AppleLDAP.md)
- [/System/Library/PrivateFrameworks/AppleMediaDiscovery.framework/AppleMediaDiscovery](DYLIBS/AppleMediaDiscovery.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices](DYLIBS/AppleMediaServices.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/AppleMediaServicesUI](DYLIBS/AppleMediaServicesUI.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUIDynamic.framework/AppleMediaServicesUIDynamic](DYLIBS/AppleMediaServicesUIDynamic.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUIPaymentSheets.framework/AppleMediaServicesUIPaymentSheets](DYLIBS/AppleMediaServicesUIPaymentSheets.md)
- [/System/Library/PrivateFrameworks/AppleMobileFileIntegrity.framework/AppleMobileFileIntegrity](DYLIBS/AppleMobileFileIntegrity.md)
- [/System/Library/PrivateFrameworks/AppleNVMe.framework/AppleNVMe](DYLIBS/AppleNVMe.md)
- [/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine](DYLIBS/AppleNeuralEngine.md)
- [/System/Library/PrivateFrameworks/ApplePDPHelper.framework/ApplePDPHelper](DYLIBS/ApplePDPHelper.md)
- [/System/Library/PrivateFrameworks/ApplePhotonDetectorServices.framework/ApplePhotonDetectorServices](DYLIBS/ApplePhotonDetectorServices.md)
- [/System/Library/PrivateFrameworks/ApplePushService.framework/ApplePushService](DYLIBS/ApplePushService.md)
- [/System/Library/PrivateFrameworks/AppleSARHelper.framework/AppleSARHelper](DYLIBS/AppleSARHelper.md)
- [/System/Library/PrivateFrameworks/AppleSRP.framework/AppleSRP](DYLIBS/AppleSRP.md)
- [/System/Library/PrivateFrameworks/AppleSauce.framework/AppleSauce](DYLIBS/AppleSauce.md)
- [/System/Library/PrivateFrameworks/AppleServiceToolkit.framework/AppleServiceToolkit](DYLIBS/AppleServiceToolkit.md)
- [/System/Library/PrivateFrameworks/AppleTracingSupportSymbolication.framework/AppleTracingSupportSymbolication](DYLIBS/AppleTracingSupportSymbolication.md)
- [/System/Library/PrivateFrameworks/AskPermission.framework/AskPermission](DYLIBS/AskPermission.md)
- [/System/Library/PrivateFrameworks/AskTo.framework/AskTo](DYLIBS/AskTo.md)
- [/System/Library/PrivateFrameworks/AskToCore.framework/AskToCore](DYLIBS/AskToCore.md)
- [/System/Library/PrivateFrameworks/AssertionServices.framework/AssertionServices](DYLIBS/AssertionServices.md)
- [/System/Library/PrivateFrameworks/AssetCacheServices.framework/AssetCacheServices](DYLIBS/AssetCacheServices.md)
- [/System/Library/PrivateFrameworks/AssetCacheServicesExtensions.framework/AssetCacheServicesExtensions](DYLIBS/AssetCacheServicesExtensions.md)
- [/System/Library/PrivateFrameworks/AssetExplorer.framework/AssetExplorer](DYLIBS/AssetExplorer.md)
- [/System/Library/PrivateFrameworks/AssetViewer.framework/AssetViewer](DYLIBS/AssetViewer.md)
- [/System/Library/PrivateFrameworks/AssistantCardServiceSupport.framework/AssistantCardServiceSupport](DYLIBS/AssistantCardServiceSupport.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices](DYLIBS/AssistantServices.md)
- [/System/Library/PrivateFrameworks/AssistantSettingsSupport.framework/AssistantSettingsSupport](DYLIBS/AssistantSettingsSupport.md)
- [/System/Library/PrivateFrameworks/AssistantUI.framework/AssistantUI](DYLIBS/AssistantUI.md)
- [/System/Library/PrivateFrameworks/AtomicsInternal.framework/AtomicsInternal](DYLIBS/AtomicsInternal.md)
- [/System/Library/PrivateFrameworks/AttentionAwareness.framework/AttentionAwareness](DYLIBS/AttentionAwareness.md)
- [/System/Library/PrivateFrameworks/AttributeGraph.framework/AttributeGraph](DYLIBS/AttributeGraph.md)
- [/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices](DYLIBS/AudioAccessoryServices.md)
- [/System/Library/PrivateFrameworks/AudioAnalytics.framework/AudioAnalytics](DYLIBS/AudioAnalytics.md)
- [/System/Library/PrivateFrameworks/AudioAnalyticsBase.framework/AudioAnalyticsBase](DYLIBS/AudioAnalyticsBase.md)
- [/System/Library/PrivateFrameworks/AudioAnalyticsExternal.framework/AudioAnalyticsExternal](DYLIBS/AudioAnalyticsExternal.md)
- [/System/Library/PrivateFrameworks/AudioDataAnalysis.framework/AudioDataAnalysis](DYLIBS/AudioDataAnalysis.md)
- [/System/Library/PrivateFrameworks/AudioPasscode.framework/AudioPasscode](DYLIBS/AudioPasscode.md)
- [/System/Library/PrivateFrameworks/AudioServerApplication.framework/AudioServerApplication](DYLIBS/AudioServerApplication.md)
- [/System/Library/PrivateFrameworks/AudioServerDriver.framework/AudioServerDriver](DYLIBS/AudioServerDriver.md)
- [/System/Library/PrivateFrameworks/AudioSession.framework/AudioSession](DYLIBS/AudioSession.md)
- [/System/Library/PrivateFrameworks/AudioSession.framework/libSessionUtility.dylib](DYLIBS/libSessionUtility.dylib.md)
- [/System/Library/PrivateFrameworks/AudioSessionServer.framework/AudioSessionServer](DYLIBS/AudioSessionServer.md)
- [/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore](DYLIBS/AudioToolboxCore.md)
- [/System/Library/PrivateFrameworks/AudioTransportCommon.framework/AudioTransportCommon](DYLIBS/AudioTransportCommon.md)
- [/System/Library/PrivateFrameworks/AudiogramIngestion.framework/AudiogramIngestion](DYLIBS/AudiogramIngestion.md)
- [/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit](DYLIBS/AuthKit.md)
- [/System/Library/PrivateFrameworks/AuthKitUI.framework/AuthKitUI](DYLIBS/AuthKitUI.md)
- [/System/Library/PrivateFrameworks/AuthenticationServicesCore.framework/AuthenticationServicesCore](DYLIBS/AuthenticationServicesCore.md)
- [/System/Library/PrivateFrameworks/AutoBugCaptureCore.framework/AutoBugCaptureCore](DYLIBS/AutoBugCaptureCore.md)
- [/System/Library/PrivateFrameworks/AutoFillCore.framework/AutoFillCore](DYLIBS/AutoFillCore.md)
- [/System/Library/PrivateFrameworks/AutoFillUI.framework/AutoFillUI](DYLIBS/AutoFillUI.md)
- [/System/Library/PrivateFrameworks/AutoLoop.framework/AutoLoop](DYLIBS/AutoLoop.md)
- [/System/Library/PrivateFrameworks/AutomationMode.framework/AutomationMode](DYLIBS/AutomationMode.md)
- [/System/Library/PrivateFrameworks/AvailabilityKit.framework/AvailabilityKit](DYLIBS/AvailabilityKit.md)
- [/System/Library/PrivateFrameworks/AvatarKit.framework/AvatarKit](DYLIBS/AvatarKit.md)
- [/System/Library/PrivateFrameworks/AvatarPersistence.framework/AvatarPersistence](DYLIBS/AvatarPersistence.md)
- [/System/Library/PrivateFrameworks/AvatarPoster.framework/AvatarPoster](DYLIBS/AvatarPoster.md)
- [/System/Library/PrivateFrameworks/AvatarUI.framework/AvatarUI](DYLIBS/AvatarUI.md)
- [/System/Library/PrivateFrameworks/BWCrucible.framework/BWCrucible](DYLIBS/BWCrucible.md)
- [/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation](DYLIBS/BackBoardHIDEventFoundation.md)
- [/System/Library/PrivateFrameworks/BackBoardHIDEventProcessors.framework/BackBoardHIDEventProcessors](DYLIBS/BackBoardHIDEventProcessors.md)
- [/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices](DYLIBS/BackBoardServices.md)
- [/System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks](DYLIBS/BackgroundSystemTasks.md)
- [/System/Library/PrivateFrameworks/BackgroundTaskAgent.framework/BackgroundTaskAgent](DYLIBS/BackgroundTaskAgent.md)
- [/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices](DYLIBS/BacklightServices.md)
- [/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost](DYLIBS/BacklightServicesHost.md)
- [/System/Library/PrivateFrameworks/BagKit.framework/BagKit](DYLIBS/BagKit.md)
- [/System/Library/PrivateFrameworks/BannerKit.framework/BannerKit](DYLIBS/BannerKit.md)
- [/System/Library/PrivateFrameworks/BarcodeSupport.framework/BarcodeSupport](DYLIBS/BarcodeSupport.md)
- [/System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard](DYLIBS/BaseBoard.md)
- [/System/Library/PrivateFrameworks/BaseBoardUI.framework/BaseBoardUI](DYLIBS/BaseBoardUI.md)
- [/System/Library/PrivateFrameworks/BasebandTraceHelper.framework/BasebandTraceHelper](DYLIBS/BasebandTraceHelper.md)
- [/System/Library/PrivateFrameworks/BatteryAlgorithms.framework/BatteryAlgorithms](DYLIBS/BatteryAlgorithms.md)
- [/System/Library/PrivateFrameworks/BatteryCenter.framework/BatteryCenter](DYLIBS/BatteryCenter.md)
- [/System/Library/PrivateFrameworks/BatteryCenterUI.framework/BatteryCenterUI](DYLIBS/BatteryCenterUI.md)
- [/System/Library/PrivateFrameworks/BehaviorMiner.framework/BehaviorMiner](DYLIBS/BehaviorMiner.md)
- [/System/Library/PrivateFrameworks/BiomeDSL.framework/BiomeDSL](DYLIBS/BiomeDSL.md)
- [/System/Library/PrivateFrameworks/BiomeFlexibleStorage.framework/BiomeFlexibleStorage](DYLIBS/BiomeFlexibleStorage.md)
- [/System/Library/PrivateFrameworks/BiomeFoundation.framework/BiomeFoundation](DYLIBS/BiomeFoundation.md)
- [/System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary](DYLIBS/BiomeLibrary.md)
- [/System/Library/PrivateFrameworks/BiomePubSub.framework/BiomePubSub](DYLIBS/BiomePubSub.md)
- [/System/Library/PrivateFrameworks/BiomeSequence.framework/BiomeSequence](DYLIBS/BiomeSequence.md)
- [/System/Library/PrivateFrameworks/BiomeStorage.framework/BiomeStorage](DYLIBS/BiomeStorage.md)
- [/System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams](DYLIBS/BiomeStreams.md)
- [/System/Library/PrivateFrameworks/BiomeSync.framework/BiomeSync](DYLIBS/BiomeSync.md)
- [/System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit](DYLIBS/BiometricKit.md)
- [/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI](DYLIBS/BiometricKitUI.md)
- [/System/Library/PrivateFrameworks/BiometricKitUI.framework/Frameworks/Fluid.framework/Fluid](DYLIBS/Fluid.md)
- [/System/Library/PrivateFrameworks/BiometricKitUI.framework/Frameworks/MTLSpline.framework/MTLSpline](DYLIBS/MTLSpline.md)
- [/System/Library/PrivateFrameworks/BiometricSupport.framework/BiometricSupport](DYLIBS/BiometricSupport.md)
- [/System/Library/PrivateFrameworks/BlastDoor.framework/BlastDoor](DYLIBS/BlastDoor.md)
- [/System/Library/PrivateFrameworks/BluetoothAudio.framework/BluetoothAudio](DYLIBS/BluetoothAudio.md)
- [/System/Library/PrivateFrameworks/BluetoothManager.framework/BluetoothManager](DYLIBS/BluetoothManager.md)
- [/System/Library/PrivateFrameworks/BluetoothServices.framework/BluetoothServices](DYLIBS/BluetoothServices.md)
- [/System/Library/PrivateFrameworks/BluetoothServicesUI.framework/BluetoothServicesUI](DYLIBS/BluetoothServicesUI.md)
- [/System/Library/PrivateFrameworks/BoardServices.framework/BoardServices](DYLIBS/BoardServices.md)
- [/System/Library/PrivateFrameworks/Bom.framework/Bom](DYLIBS/Bom.md)
- [/System/Library/PrivateFrameworks/BookCoverUtility.framework/BookCoverUtility](DYLIBS/BookCoverUtility.md)
- [/System/Library/PrivateFrameworks/BookDataStore.framework/BookDataStore](DYLIBS/BookDataStore.md)
- [/System/Library/PrivateFrameworks/BookFoundation.framework/BookFoundation](DYLIBS/BookFoundation.md)
- [/System/Library/PrivateFrameworks/BookLibrary.framework/BookLibrary](DYLIBS/BookLibrary.md)
- [/System/Library/PrivateFrameworks/BookLibraryCore.framework/BookLibraryCore](DYLIBS/BookLibraryCore.md)
- [/System/Library/PrivateFrameworks/BookUtility.framework/BookUtility](DYLIBS/BookUtility.md)
- [/System/Library/PrivateFrameworks/BrailleSymbology.framework/BrailleSymbology](DYLIBS/BrailleSymbology.md)
- [/System/Library/PrivateFrameworks/BrailleTranslation.framework/BrailleTranslation](DYLIBS/BrailleTranslation.md)
- [/System/Library/PrivateFrameworks/BridgeCommons.framework/BridgeCommons](DYLIBS/BridgeCommons.md)
- [/System/Library/PrivateFrameworks/BridgePreferences.framework/BridgePreferences](DYLIBS/BridgePreferences.md)
- [/System/Library/PrivateFrameworks/BridgeReporting.framework/BridgeReporting](DYLIBS/BridgeReporting.md)
- [/System/Library/PrivateFrameworks/BrightnessControl.framework/BrightnessControl](DYLIBS/BrightnessControl.md)
- [/System/Library/PrivateFrameworks/BrookDataCollection.framework/BrookDataCollection](DYLIBS/BrookDataCollection.md)
- [/System/Library/PrivateFrameworks/BrookServices.framework/BrookServices](DYLIBS/BrookServices.md)
- [/System/Library/PrivateFrameworks/BulletinBoard.framework/BulletinBoard](DYLIBS/BulletinBoard.md)
- [/System/Library/PrivateFrameworks/BulletinDistributorCompanion.framework/BulletinDistributorCompanion](DYLIBS/BulletinDistributorCompanion.md)
- [/System/Library/PrivateFrameworks/BusinessChatService.framework/BusinessChatService](DYLIBS/BusinessChatService.md)
- [/System/Library/PrivateFrameworks/BusinessServices.framework/BusinessServices](DYLIBS/BusinessServices.md)
- [/System/Library/PrivateFrameworks/BusinessServicesUI.framework/BusinessServicesUI](DYLIBS/BusinessServicesUI.md)
- [/System/Library/PrivateFrameworks/ButtonResolver.framework/ButtonResolver](DYLIBS/ButtonResolver.md)
- [/System/Library/PrivateFrameworks/C2.framework/C2](DYLIBS/C2.md)
- [/System/Library/PrivateFrameworks/CARP.framework/CARP](DYLIBS/CARP.md)
- [/System/Library/PrivateFrameworks/CBORLibrary.framework/CBORLibrary](DYLIBS/CBORLibrary.md)
- [/System/Library/PrivateFrameworks/CDDataAccess.framework/CDDataAccess](DYLIBS/CDDataAccess.md)
- [/System/Library/PrivateFrameworks/CDDataAccess.framework/Frameworks/DACalDAV.framework/DACalDAV](DYLIBS/DACalDAV.md)
- [/System/Library/PrivateFrameworks/CDDataAccess.framework/Frameworks/DACoreDAVGlue.framework/DACoreDAVGlue](DYLIBS/DACoreDAVGlue.md)
- [/System/Library/PrivateFrameworks/CDDataAccess.framework/Frameworks/DADaemonSupport.framework/DADaemonSupport](DYLIBS/DADaemonSupport.md)
- [/System/Library/PrivateFrameworks/CDDataAccessExpress.framework/CDDataAccessExpress](DYLIBS/CDDataAccessExpress.md)
- [/System/Library/PrivateFrameworks/CDMFoundation.framework/CDMFoundation](DYLIBS/CDMFoundation.md)
- [/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture](DYLIBS/CMCapture.md)
- [/System/Library/PrivateFrameworks/CMCaptureCore.framework/CMCaptureCore](DYLIBS/CMCaptureCore.md)
- [/System/Library/PrivateFrameworks/CMContinuityCaptureCore.framework/CMContinuityCaptureCore](DYLIBS/CMContinuityCaptureCore.md)
- [/System/Library/PrivateFrameworks/CMImaging.framework/CMImaging](DYLIBS/CMImaging.md)
- [/System/Library/PrivateFrameworks/CMPhoto.framework/CMPhoto](DYLIBS/CMPhoto.md)
- [/System/Library/PrivateFrameworks/CPAnalytics.framework/CPAnalytics](DYLIBS/CPAnalytics.md)
- [/System/Library/PrivateFrameworks/CPMLBestShim.framework/CPMLBestShim](DYLIBS/CPMLBestShim.md)
- [/System/Library/PrivateFrameworks/CPMS.framework/CPMS](DYLIBS/CPMS.md)
- [/System/Library/PrivateFrameworks/CSExattrCrypto.framework/CSExattrCrypto](DYLIBS/CSExattrCrypto.md)
- [/System/Library/PrivateFrameworks/CTCarrierSpace.framework/CTCarrierSpace](DYLIBS/CTCarrierSpace.md)
- [/System/Library/PrivateFrameworks/CVNLP.framework/CVNLP](DYLIBS/CVNLP.md)
- [/System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete](DYLIBS/CacheDelete.md)
- [/System/Library/PrivateFrameworks/CalDAV.framework/CalDAV](DYLIBS/CalDAV.md)
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
- [/System/Library/PrivateFrameworks/CallScreeningActivity_Shared.framework/CallScreeningActivity_Shared](DYLIBS/CallScreeningActivity_Shared.md)
- [/System/Library/PrivateFrameworks/CameraColorProcessing.framework/CameraColorProcessing](DYLIBS/CameraColorProcessing.md)
- [/System/Library/PrivateFrameworks/CameraEditKit.framework/CameraEditKit](DYLIBS/CameraEditKit.md)
- [/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit](DYLIBS/CameraEffectsKit.md)
- [/System/Library/PrivateFrameworks/CameraImagingFramework.framework/CameraImagingFramework](DYLIBS/CameraImagingFramework.md)
- [/System/Library/PrivateFrameworks/CameraKit.framework/CameraKit](DYLIBS/CameraKit.md)
- [/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI](DYLIBS/CameraUI.md)
- [/System/Library/PrivateFrameworks/CaptiveNetwork.framework/CaptiveNetwork](DYLIBS/CaptiveNetwork.md)
- [/System/Library/PrivateFrameworks/CarAssetUtils.framework/CarAssetUtils](DYLIBS/CarAssetUtils.md)
- [/System/Library/PrivateFrameworks/CarCommandsUIFramework.framework/CarCommandsUIFramework](DYLIBS/CarCommandsUIFramework.md)
- [/System/Library/PrivateFrameworks/CarKit.framework/CarKit](DYLIBS/CarKit.md)
- [/System/Library/PrivateFrameworks/CarKitNavigation.framework/CarKitNavigation](DYLIBS/CarKitNavigation.md)
- [/System/Library/PrivateFrameworks/CarPlayServices.framework/CarPlayServices](DYLIBS/CarPlayServices.md)
- [/System/Library/PrivateFrameworks/CarPlaySetup.framework/CarPlaySetup](DYLIBS/CarPlaySetup.md)
- [/System/Library/PrivateFrameworks/CarPlaySupport.framework/CarPlaySupport](DYLIBS/CarPlaySupport.md)
- [/System/Library/PrivateFrameworks/CarPlayUI.framework/CarPlayUI](DYLIBS/CarPlayUI.md)
- [/System/Library/PrivateFrameworks/CarPlayUIServices.framework/CarPlayUIServices](DYLIBS/CarPlayUIServices.md)
- [/System/Library/PrivateFrameworks/CardKit.framework/CardKit](DYLIBS/CardKit.md)
- [/System/Library/PrivateFrameworks/CardServices.framework/CardServices](DYLIBS/CardServices.md)
- [/System/Library/PrivateFrameworks/Cards.framework/Cards](DYLIBS/Cards.md)
- [/System/Library/PrivateFrameworks/CarouselPreferenceServices.framework/CarouselPreferenceServices](DYLIBS/CarouselPreferenceServices.md)
- [/System/Library/PrivateFrameworks/Catalyst.framework/Catalyst](DYLIBS/Catalyst.md)
- [/System/Library/PrivateFrameworks/Categories.framework/Categories](DYLIBS/Categories.md)
- [/System/Library/PrivateFrameworks/Celestial.framework/Celestial](DYLIBS/Celestial.md)
- [/System/Library/PrivateFrameworks/CellularBridgeUI.framework/CellularBridgeUI](DYLIBS/CellularBridgeUI.md)
- [/System/Library/PrivateFrameworks/CellularDataDiagnosticsSuite.framework/CellularDataDiagnosticsSuite](DYLIBS/CellularDataDiagnosticsSuite.md)
- [/System/Library/PrivateFrameworks/CellularPlanManager.framework/CellularPlanManager](DYLIBS/CellularPlanManager.md)
- [/System/Library/PrivateFrameworks/CertInfo.framework/CertInfo](DYLIBS/CertInfo.md)
- [/System/Library/PrivateFrameworks/CertUI.framework/CertUI](DYLIBS/CertUI.md)
- [/System/Library/PrivateFrameworks/ChassisAttestation.framework/ChassisAttestation](DYLIBS/ChassisAttestation.md)
- [/System/Library/PrivateFrameworks/ChatKit.framework/ChatKit](DYLIBS/ChatKit.md)
- [/System/Library/PrivateFrameworks/CheckerBoardServices.framework/CheckerBoardServices](DYLIBS/CheckerBoardServices.md)
- [/System/Library/PrivateFrameworks/Chirp.framework/Chirp](DYLIBS/Chirp.md)
- [/System/Library/PrivateFrameworks/ChronoCore.framework/ChronoCore](DYLIBS/ChronoCore.md)
- [/System/Library/PrivateFrameworks/ChronoCore.framework/Support/WidgetPreviewsExtensionAgent.bundle/WidgetPreviewsExtensionAgent](DYLIBS/WidgetPreviewsExtensionAgent.md)
- [/System/Library/PrivateFrameworks/ChronoCore.framework/Support/WidgetPreviewsSupport.framework/WidgetPreviewsSupport](DYLIBS/WidgetPreviewsSupport.md)
- [/System/Library/PrivateFrameworks/ChronoKit.framework/ChronoKit](DYLIBS/ChronoKit.md)
- [/System/Library/PrivateFrameworks/ChronoServices.framework/ChronoServices](DYLIBS/ChronoServices.md)
- [/System/Library/PrivateFrameworks/ChronoUIServices.framework/ChronoUIServices](DYLIBS/ChronoUIServices.md)
- [/System/Library/PrivateFrameworks/ChunkingLibrary.framework/ChunkingLibrary](DYLIBS/ChunkingLibrary.md)
- [/System/Library/PrivateFrameworks/CinematicFraming.framework/CinematicFraming](DYLIBS/CinematicFraming.md)
- [/System/Library/PrivateFrameworks/CipherML.framework/CipherML](DYLIBS/CipherML.md)
- [/System/Library/PrivateFrameworks/ClarityBoardFoundation.framework/ClarityBoardFoundation](DYLIBS/ClarityBoardFoundation.md)
- [/System/Library/PrivateFrameworks/ClarityFoundation.framework/ClarityFoundation](DYLIBS/ClarityFoundation.md)
- [/System/Library/PrivateFrameworks/ClassKitUI.framework/ClassKitUI](DYLIBS/ClassKitUI.md)
- [/System/Library/PrivateFrameworks/ClassroomKit.framework/ClassroomKit](DYLIBS/ClassroomKit.md)
- [/System/Library/PrivateFrameworks/ClassroomKit.framework/Frameworks/ClassroomUIKit.framework/ClassroomUIKit](DYLIBS/ClassroomUIKit.md)
- [/System/Library/PrivateFrameworks/ClipServices.framework/ClipServices](DYLIBS/ClipServices.md)
- [/System/Library/PrivateFrameworks/ClipUIServices.framework/ClipUIServices](DYLIBS/ClipUIServices.md)
- [/System/Library/PrivateFrameworks/ClockComplications.framework/ClockComplications](DYLIBS/ClockComplications.md)
- [/System/Library/PrivateFrameworks/ClockKitUI.framework/ClockKitUI](DYLIBS/ClockKitUI.md)
- [/System/Library/PrivateFrameworks/ClockPoster.framework/ClockPoster](DYLIBS/ClockPoster.md)
- [/System/Library/PrivateFrameworks/CloudAsset.framework/CloudAsset](DYLIBS/CloudAsset.md)
- [/System/Library/PrivateFrameworks/CloudAssetDaemon.framework/CloudAssetDaemon](DYLIBS/CloudAssetDaemon.md)
- [/System/Library/PrivateFrameworks/CloudDocs.framework/CloudDocs](DYLIBS/CloudDocs.md)
- [/System/Library/PrivateFrameworks/CloudDocsDaemon.framework/CloudDocsDaemon](DYLIBS/CloudDocsDaemon.md)
- [/System/Library/PrivateFrameworks/CloudDocsUI.framework/CloudDocsUI](DYLIBS/CloudDocsUI.md)
- [/System/Library/PrivateFrameworks/CloudKitCode.framework/CloudKitCode](DYLIBS/CloudKitCode.md)
- [/System/Library/PrivateFrameworks/CloudKitCodeProtobuf.framework/CloudKitCodeProtobuf](DYLIBS/CloudKitCodeProtobuf.md)
- [/System/Library/PrivateFrameworks/CloudKitDaemon.framework/CloudKitDaemon](DYLIBS/CloudKitDaemon.md)
- [/System/Library/PrivateFrameworks/CloudKitDistributedSync.framework/CloudKitDistributedSync](DYLIBS/CloudKitDistributedSync.md)
- [/System/Library/PrivateFrameworks/CloudMediaServicesInterfaceKit.framework/CloudMediaServicesInterfaceKit](DYLIBS/CloudMediaServicesInterfaceKit.md)
- [/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/CloudPhotoLibrary](DYLIBS/CloudPhotoLibrary.md)
- [/System/Library/PrivateFrameworks/CloudPhotoServices.framework/CloudPhotoServices](DYLIBS/CloudPhotoServices.md)
- [/System/Library/PrivateFrameworks/CloudRecommendation.framework/CloudRecommendation](DYLIBS/CloudRecommendation.md)
- [/System/Library/PrivateFrameworks/CloudServices.framework/CloudServices](DYLIBS/CloudServices.md)
- [/System/Library/PrivateFrameworks/CloudSettings.framework/CloudSettings](DYLIBS/CloudSettings.md)
- [/System/Library/PrivateFrameworks/CloudSharing.framework/CloudSharing](DYLIBS/CloudSharing.md)
- [/System/Library/PrivateFrameworks/CloudSharingUI.framework/CloudSharingUI](DYLIBS/CloudSharingUI.md)
- [/System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/CloudSubscriptionFeatures](DYLIBS/CloudSubscriptionFeatures.md)
- [/System/Library/PrivateFrameworks/CloudTelemetry.framework/CloudTelemetry](DYLIBS/CloudTelemetry.md)
- [/System/Library/PrivateFrameworks/CloudTelemetryTools.framework/CloudTelemetryTools](DYLIBS/CloudTelemetryTools.md)
- [/System/Library/PrivateFrameworks/CognitiveHealth.framework/CognitiveHealth](DYLIBS/CognitiveHealth.md)
- [/System/Library/PrivateFrameworks/Coherence.framework/Coherence](DYLIBS/Coherence.md)
- [/System/Library/PrivateFrameworks/CollectionViewCore.framework/CollectionViewCore](DYLIBS/CollectionViewCore.md)
- [/System/Library/PrivateFrameworks/CollectionsInternal.framework/CollectionsInternal](DYLIBS/CollectionsInternal.md)
- [/System/Library/PrivateFrameworks/CombineCocoa.framework/CombineCocoa](DYLIBS/CombineCocoa.md)
- [/System/Library/PrivateFrameworks/CommandAndControlUI.framework/CommandAndControlUI](DYLIBS/CommandAndControlUI.md)
- [/System/Library/PrivateFrameworks/CommonAuth.framework/CommonAuth](DYLIBS/CommonAuth.md)
- [/System/Library/PrivateFrameworks/CommonUtilities.framework/CommonUtilities](DYLIBS/CommonUtilities.md)
- [/System/Library/PrivateFrameworks/CommunicationSafetySettingsUI.framework/CommunicationSafetySettingsUI](DYLIBS/CommunicationSafetySettingsUI.md)
- [/System/Library/PrivateFrameworks/CommunicationsFilter.framework/CommunicationsFilter](DYLIBS/CommunicationsFilter.md)
- [/System/Library/PrivateFrameworks/CommunicationsSetupUI.framework/CommunicationsSetupUI](DYLIBS/CommunicationsSetupUI.md)
- [/System/Library/PrivateFrameworks/CompanionCamera.framework/CompanionCamera](DYLIBS/CompanionCamera.md)
- [/System/Library/PrivateFrameworks/CompanionHealthDaemon.framework/CompanionHealthDaemon](DYLIBS/CompanionHealthDaemon.md)
- [/System/Library/PrivateFrameworks/CompanionServices.framework/CompanionServices](DYLIBS/CompanionServices.md)
- [/System/Library/PrivateFrameworks/CompanionSync.framework/CompanionSync](DYLIBS/CompanionSync.md)
- [/System/Library/PrivateFrameworks/CompassUI.framework/CompassUI](DYLIBS/CompassUI.md)
- [/System/Library/PrivateFrameworks/ComplicationDisplay.framework/ComplicationDisplay](DYLIBS/ComplicationDisplay.md)
- [/System/Library/PrivateFrameworks/ConditionInducer.framework/ConditionInducer](DYLIBS/ConditionInducer.md)
- [/System/Library/PrivateFrameworks/ConfigurationEngineModel.framework/ConfigurationEngineModel](DYLIBS/ConfigurationEngineModel.md)
- [/System/Library/PrivateFrameworks/ConnectedAudioTest.framework/ConnectedAudioTest](DYLIBS/ConnectedAudioTest.md)
- [/System/Library/PrivateFrameworks/ConstantClasses.framework/ConstantClasses](DYLIBS/ConstantClasses.md)
- [/System/Library/PrivateFrameworks/ContactlessReaderUI.framework/ContactlessReaderUI](DYLIBS/ContactlessReaderUI.md)
- [/System/Library/PrivateFrameworks/ContactsAssistantServices.framework/ContactsAssistantServices](DYLIBS/ContactsAssistantServices.md)
- [/System/Library/PrivateFrameworks/ContactsAutocomplete.framework/ContactsAutocomplete](DYLIBS/ContactsAutocomplete.md)
- [/System/Library/PrivateFrameworks/ContactsAutocompleteUI.framework/ContactsAutocompleteUI](DYLIBS/ContactsAutocompleteUI.md)
- [/System/Library/PrivateFrameworks/ContactsDonation.framework/ContactsDonation](DYLIBS/ContactsDonation.md)
- [/System/Library/PrivateFrameworks/ContactsDonationFeedback.framework/ContactsDonationFeedback](DYLIBS/ContactsDonationFeedback.md)
- [/System/Library/PrivateFrameworks/ContactsFoundation.framework/ContactsFoundation](DYLIBS/ContactsFoundation.md)
- [/System/Library/PrivateFrameworks/ContactsMetrics.framework/ContactsMetrics](DYLIBS/ContactsMetrics.md)
- [/System/Library/PrivateFrameworks/ContactsUICore.framework/ContactsUICore](DYLIBS/ContactsUICore.md)
- [/System/Library/PrivateFrameworks/ContactsWidgetUI.framework/ContactsWidgetUI](DYLIBS/ContactsWidgetUI.md)
- [/System/Library/PrivateFrameworks/ContainerManagerCommon.framework/ContainerManagerCommon](DYLIBS/ContainerManagerCommon.md)
- [/System/Library/PrivateFrameworks/ContainerManagerSystem.framework/ContainerManagerSystem](DYLIBS/ContainerManagerSystem.md)
- [/System/Library/PrivateFrameworks/ContainerManagerUser.framework/ContainerManagerUser](DYLIBS/ContainerManagerUser.md)
- [/System/Library/PrivateFrameworks/ContentKit.framework/ContentKit](DYLIBS/ContentKit.md)
- [/System/Library/PrivateFrameworks/ContextKit.framework/ContextKit](DYLIBS/ContextKit.md)
- [/System/Library/PrivateFrameworks/ContextKitCore.framework/ContextKitCore](DYLIBS/ContextKitCore.md)
- [/System/Library/PrivateFrameworks/ContextKitExtraction.framework/ContextKitExtraction](DYLIBS/ContextKitExtraction.md)
- [/System/Library/PrivateFrameworks/ContextKitPrediction.framework/ContextKitPrediction](DYLIBS/ContextKitPrediction.md)
- [/System/Library/PrivateFrameworks/ContextSync.framework/ContextSync](DYLIBS/ContextSync.md)
- [/System/Library/PrivateFrameworks/ContextualActionsClient.framework/ContextualActionsClient](DYLIBS/ContextualActionsClient.md)
- [/System/Library/PrivateFrameworks/ContextualSuggestionClient.framework/ContextualSuggestionClient](DYLIBS/ContextualSuggestionClient.md)
- [/System/Library/PrivateFrameworks/ContextualUnderstanding.framework/ContextualUnderstanding](DYLIBS/ContextualUnderstanding.md)
- [/System/Library/PrivateFrameworks/ContinuousDialogManagerService.framework/ContinuousDialogManagerService](DYLIBS/ContinuousDialogManagerService.md)
- [/System/Library/PrivateFrameworks/ControlCenterServices.framework/ControlCenterServices](DYLIBS/ControlCenterServices.md)
- [/System/Library/PrivateFrameworks/ControlCenterUI.framework/ControlCenterUI](DYLIBS/ControlCenterUI.md)
- [/System/Library/PrivateFrameworks/ControlCenterUIKit.framework/ControlCenterUIKit](DYLIBS/ControlCenterUIKit.md)
- [/System/Library/PrivateFrameworks/ConversationKit.framework/ConversationKit](DYLIBS/ConversationKit.md)
- [/System/Library/PrivateFrameworks/Coordination.framework/Coordination](DYLIBS/Coordination.md)
- [/System/Library/PrivateFrameworks/CoordinationCore.framework/CoordinationCore](DYLIBS/CoordinationCore.md)
- [/System/Library/PrivateFrameworks/CopresenceCore.framework/CopresenceCore](DYLIBS/CopresenceCore.md)
- [/System/Library/PrivateFrameworks/CoreAUC.framework/CoreAUC](DYLIBS/CoreAUC.md)
- [/System/Library/PrivateFrameworks/CoreAccessories.framework/CoreAccessories](DYLIBS/CoreAccessories.md)
- [/System/Library/PrivateFrameworks/CoreAccessoriesFeatures.framework/CoreAccessoriesFeatures](DYLIBS/CoreAccessoriesFeatures.md)
- [/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics](DYLIBS/CoreAnalytics.md)
- [/System/Library/PrivateFrameworks/CoreAppleCVA.framework/CoreAppleCVA](DYLIBS/CoreAppleCVA.md)
- [/System/Library/PrivateFrameworks/CoreAutoLayout.framework/CoreAutoLayout](DYLIBS/CoreAutoLayout.md)
- [/System/Library/PrivateFrameworks/CoreBluetoothUI.framework/CoreBluetoothUI](DYLIBS/CoreBluetoothUI.md)
- [/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness](DYLIBS/CoreBrightness.md)
- [/System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP](DYLIBS/CoreCDP.md)
- [/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal](DYLIBS/CoreCDPInternal.md)
- [/System/Library/PrivateFrameworks/CoreCDPUI.framework/CoreCDPUI](DYLIBS/CoreCDPUI.md)
- [/System/Library/PrivateFrameworks/CoreCDPUIInternal.framework/CoreCDPUIInternal](DYLIBS/CoreCDPUIInternal.md)
- [/System/Library/PrivateFrameworks/CoreCapture.framework/CoreCapture](DYLIBS/CoreCapture.md)
- [/System/Library/PrivateFrameworks/CoreCaptureControl.framework/CoreCaptureControl](DYLIBS/CoreCaptureControl.md)
- [/System/Library/PrivateFrameworks/CoreCaptureDaemon.framework/CoreCaptureDaemon](DYLIBS/CoreCaptureDaemon.md)
- [/System/Library/PrivateFrameworks/CoreChartSwift.framework/CoreChartSwift](DYLIBS/CoreChartSwift.md)
- [/System/Library/PrivateFrameworks/CoreDAV.framework/CoreDAV](DYLIBS/CoreDAV.md)
- [/System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet](DYLIBS/CoreDuet.md)
- [/System/Library/PrivateFrameworks/CoreDuetContext.framework/CoreDuetContext](DYLIBS/CoreDuetContext.md)
- [/System/Library/PrivateFrameworks/CoreDuetDaemonProtocol.framework/CoreDuetDaemonProtocol](DYLIBS/CoreDuetDaemonProtocol.md)
- [/System/Library/PrivateFrameworks/CoreDuetSync.framework/CoreDuetSync](DYLIBS/CoreDuetSync.md)
- [/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/CoreEmbeddedSpeechRecognition](DYLIBS/CoreEmbeddedSpeechRecognition.md)
- [/System/Library/PrivateFrameworks/CoreEmoji.framework/CoreEmoji](DYLIBS/CoreEmoji.md)
- [/System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp](DYLIBS/CoreFollowUp.md)
- [/System/Library/PrivateFrameworks/CoreFollowUpUI.framework/CoreFollowUpUI](DYLIBS/CoreFollowUpUI.md)
- [/System/Library/PrivateFrameworks/CoreGPS.framework/CoreGPS](DYLIBS/CoreGPS.md)
- [/System/Library/PrivateFrameworks/CoreGPSTest.framework/CoreGPSTest](DYLIBS/CoreGPSTest.md)
- [/System/Library/PrivateFrameworks/CoreHAP.framework/CoreHAP](DYLIBS/CoreHAP.md)
- [/System/Library/PrivateFrameworks/CoreHandwriting.framework/CoreHandwriting](DYLIBS/CoreHandwriting.md)
- [/System/Library/PrivateFrameworks/CoreIDCred.framework/CoreIDCred](DYLIBS/CoreIDCred.md)
- [/System/Library/PrivateFrameworks/CoreIDCredBuilder.framework/CoreIDCredBuilder](DYLIBS/CoreIDCredBuilder.md)
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
- [/System/Library/PrivateFrameworks/CoreMotionModels.framework/CoreMotionModels](DYLIBS/CoreMotionModels.md)
- [/System/Library/PrivateFrameworks/CoreNLP.framework/CoreNLP](DYLIBS/CoreNLP.md)
- [/System/Library/PrivateFrameworks/CoreNameParser.framework/CoreNameParser](DYLIBS/CoreNameParser.md)
- [/System/Library/PrivateFrameworks/CoreNavigation.framework/CoreNavigation](DYLIBS/CoreNavigation.md)
- [/System/Library/PrivateFrameworks/CoreOC.framework/CoreOC](DYLIBS/CoreOC.md)
- [/System/Library/PrivateFrameworks/CoreOCModules.framework/CoreOCModules](DYLIBS/CoreOCModules.md)
- [/System/Library/PrivateFrameworks/CoreODI.framework/CoreODI](DYLIBS/CoreODI.md)
- [/System/Library/PrivateFrameworks/CoreODIEssentials.framework/CoreODIEssentials](DYLIBS/CoreODIEssentials.md)
- [/System/Library/PrivateFrameworks/CoreOptimization.framework/CoreOptimization](DYLIBS/CoreOptimization.md)
- [/System/Library/PrivateFrameworks/CorePDF.framework/CorePDF](DYLIBS/CorePDF.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/CoreParsec](DYLIBS/CoreParsec.md)
- [/System/Library/PrivateFrameworks/CorePhoneNumbers.framework/CorePhoneNumbers](DYLIBS/CorePhoneNumbers.md)
- [/System/Library/PrivateFrameworks/CorePhotogrammetry.framework/CorePhotogrammetry](DYLIBS/CorePhotogrammetry.md)
- [/System/Library/PrivateFrameworks/CorePrediction.framework/CorePrediction](DYLIBS/CorePrediction.md)
- [/System/Library/PrivateFrameworks/CorePrescriptionLite.framework/CorePrescriptionLite](DYLIBS/CorePrescriptionLite.md)
- [/System/Library/PrivateFrameworks/CoreRE.framework/CoreRE](DYLIBS/CoreRE.md)
- [/System/Library/PrivateFrameworks/CoreRealityIO.framework/CoreRealityIO](DYLIBS/CoreRealityIO.md)
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
- [/System/Library/PrivateFrameworks/CoreSpeechFoundation.framework/CoreSpeechFoundation](DYLIBS/CoreSpeechFoundation.md)
- [/System/Library/PrivateFrameworks/CoreSpeechGazeTracking.framework/CoreSpeechGazeTracking](DYLIBS/CoreSpeechGazeTracking.md)
- [/System/Library/PrivateFrameworks/CoreSuggestions.framework/CoreSuggestions](DYLIBS/CoreSuggestions.md)
- [/System/Library/PrivateFrameworks/CoreSuggestionsInternals.framework/CoreSuggestionsInternals](DYLIBS/CoreSuggestionsInternals.md)
- [/System/Library/PrivateFrameworks/CoreSuggestionsML.framework/CoreSuggestionsML](DYLIBS/CoreSuggestionsML.md)
- [/System/Library/PrivateFrameworks/CoreSuggestionsUI.framework/CoreSuggestionsUI](DYLIBS/CoreSuggestionsUI.md)
- [/System/Library/PrivateFrameworks/CoreSymbolication.framework/CoreSymbolication](DYLIBS/CoreSymbolication.md)
- [/System/Library/PrivateFrameworks/CoreThemeDefinition.framework/CoreThemeDefinition](DYLIBS/CoreThemeDefinition.md)
- [/System/Library/PrivateFrameworks/CoreThread.framework/CoreThread](DYLIBS/CoreThread.md)
- [/System/Library/PrivateFrameworks/CoreThreadRadio.framework/CoreThreadRadio](DYLIBS/CoreThreadRadio.md)
- [/System/Library/PrivateFrameworks/CoreTime.framework/CoreTime](DYLIBS/CoreTime.md)
- [/System/Library/PrivateFrameworks/CoreUARP.framework/CoreUARP](DYLIBS/CoreUARP.md)
- [/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI](DYLIBS/CoreUI.md)
- [/System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils](DYLIBS/CoreUtils.md)
- [/System/Library/PrivateFrameworks/CoreUtilsExtras.framework/CoreUtilsExtras](DYLIBS/CoreUtilsExtras.md)
- [/System/Library/PrivateFrameworks/CoreUtilsSwift.framework/CoreUtilsSwift](DYLIBS/CoreUtilsSwift.md)
- [/System/Library/PrivateFrameworks/CoreUtilsUI.framework/CoreUtilsUI](DYLIBS/CoreUtilsUI.md)
- [/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi](DYLIBS/CoreWiFi.md)
- [/System/Library/PrivateFrameworks/Cornobble.framework/Cornobble](DYLIBS/Cornobble.md)
- [/System/Library/PrivateFrameworks/CoverSheet.framework/CoverSheet](DYLIBS/CoverSheet.md)
- [/System/Library/PrivateFrameworks/CoverSheetKit.framework/CoverSheetKit](DYLIBS/CoverSheetKit.md)
- [/System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport](DYLIBS/CrashReporterSupport.md)
- [/System/Library/PrivateFrameworks/CrisisResources.framework/CrisisResources](DYLIBS/CrisisResources.md)
- [/System/Library/PrivateFrameworks/CryptoKitCBridging.framework/CryptoKitCBridging](DYLIBS/CryptoKitCBridging.md)
- [/System/Library/PrivateFrameworks/CryptoKitPrivate.framework/CryptoKitPrivate](DYLIBS/CryptoKitPrivate.md)
- [/System/Library/PrivateFrameworks/DAAPKit.framework/DAAPKit](DYLIBS/DAAPKit.md)
- [/System/Library/PrivateFrameworks/DAEASOAuthFramework.framework/DAEASOAuthFramework](DYLIBS/DAEASOAuthFramework.md)
- [/System/Library/PrivateFrameworks/DASDaemon.framework/DASDaemon](DYLIBS/DASDaemon.md)
- [/System/Library/PrivateFrameworks/DASDelegate.framework/DASDelegate](DYLIBS/DASDelegate.md)
- [/System/Library/PrivateFrameworks/DEPClientLibrary.framework/DEPClientLibrary](DYLIBS/DEPClientLibrary.md)
- [/System/Library/PrivateFrameworks/DMCApps.framework/DMCApps](DYLIBS/DMCApps.md)
- [/System/Library/PrivateFrameworks/DMCEnrollmentLibrary.framework/DMCEnrollmentLibrary](DYLIBS/DMCEnrollmentLibrary.md)
- [/System/Library/PrivateFrameworks/DMCEnrollmentProvider.framework/DMCEnrollmentProvider](DYLIBS/DMCEnrollmentProvider.md)
- [/System/Library/PrivateFrameworks/DMCToolsUIUtilities.framework/DMCToolsUIUtilities](DYLIBS/DMCToolsUIUtilities.md)
- [/System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities](DYLIBS/DMCUtilities.md)
- [/System/Library/PrivateFrameworks/DRMFoundation.framework/DRMFoundation](DYLIBS/DRMFoundation.md)
- [/System/Library/PrivateFrameworks/DSRemotePairing.framework/DSRemotePairing](DYLIBS/DSRemotePairing.md)
- [/System/Library/PrivateFrameworks/DTXConnectionServices.framework/DTXConnectionServices](DYLIBS/DTXConnectionServices.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/DVTInstrumentsFoundation](DYLIBS/DVTInstrumentsFoundation.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsUtilities.framework/DVTInstrumentsUtilities](DYLIBS/DVTInstrumentsUtilities.md)
- [/System/Library/PrivateFrameworks/DarwinDirectory.framework/DarwinDirectory](DYLIBS/DarwinDirectory.md)
- [/System/Library/PrivateFrameworks/DashBoard.framework/DashBoard](DYLIBS/DashBoard.md)
- [/System/Library/PrivateFrameworks/DataAccess.framework/DataAccess](DYLIBS/DataAccess.md)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DACalDAV.framework/DACalDAV](DYLIBS/DACalDAV.md)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DACardDAV.framework/DACardDAV](DYLIBS/DACardDAV.md)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DACoreDAVGlue.framework/DACoreDAVGlue](DYLIBS/DACoreDAVGlue.md)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DADaemonSupport.framework/DADaemonSupport](DYLIBS/DADaemonSupport.md)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DAIMAPNotes.framework/DAIMAPNotes](DYLIBS/DAIMAPNotes.md)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DALDAP.framework/DALDAP](DYLIBS/DALDAP.md)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DASubCal.framework/DASubCal](DYLIBS/DASubCal.md)
- [/System/Library/PrivateFrameworks/DataAccessExpress.framework/DataAccessExpress](DYLIBS/DataAccessExpress.md)
- [/System/Library/PrivateFrameworks/DataAccessUI.framework/DataAccessUI](DYLIBS/DataAccessUI.md)
- [/System/Library/PrivateFrameworks/DataDeliveryServices.framework/DataDeliveryServices](DYLIBS/DataDeliveryServices.md)
- [/System/Library/PrivateFrameworks/DataDetectorsCore.framework/DataDetectorsCore](DYLIBS/DataDetectorsCore.md)
- [/System/Library/PrivateFrameworks/DataDetectorsCore.framework/PlugIns/PhoneNumbers.plugin/PhoneNumbers](DYLIBS/PhoneNumbers.md)
- [/System/Library/PrivateFrameworks/DataDetectorsNaturalLanguage.framework/DataDetectorsNaturalLanguage](DYLIBS/DataDetectorsNaturalLanguage.md)
- [/System/Library/PrivateFrameworks/DataDetectorsUI.framework/DataDetectorsUI](DYLIBS/DataDetectorsUI.md)
- [/System/Library/PrivateFrameworks/DataMigration.framework/DataMigration](DYLIBS/DataMigration.md)
- [/System/Library/PrivateFrameworks/DeepThought.framework/DeepThought](DYLIBS/DeepThought.md)
- [/System/Library/PrivateFrameworks/DeepThoughtBiomeFoundation.framework/DeepThoughtBiomeFoundation](DYLIBS/DeepThoughtBiomeFoundation.md)
- [/System/Library/PrivateFrameworks/DepthCore.framework/DepthCore](DYLIBS/DepthCore.md)
- [/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/DesktopServicesPriv](DYLIBS/DesktopServicesPriv.md)
- [/System/Library/PrivateFrameworks/DeviceAccess.framework/DeviceAccess](DYLIBS/DeviceAccess.md)
- [/System/Library/PrivateFrameworks/DeviceActivityConductor.framework/DeviceActivityConductor](DYLIBS/DeviceActivityConductor.md)
- [/System/Library/PrivateFrameworks/DeviceCheckInternal.framework/DeviceCheckInternal](DYLIBS/DeviceCheckInternal.md)
- [/System/Library/PrivateFrameworks/DeviceDiscoveryUI.framework/DeviceDiscoveryUI](DYLIBS/DeviceDiscoveryUI.md)
- [/System/Library/PrivateFrameworks/DeviceDiscoveryUICore.framework/DeviceDiscoveryUICore](DYLIBS/DeviceDiscoveryUICore.md)
- [/System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity](DYLIBS/DeviceIdentity.md)
- [/System/Library/PrivateFrameworks/DeviceManagement.framework/DeviceManagement](DYLIBS/DeviceManagement.md)
- [/System/Library/PrivateFrameworks/DeviceManagementTools.framework/DeviceManagementTools](DYLIBS/DeviceManagementTools.md)
- [/System/Library/PrivateFrameworks/DeviceOMatic.framework/DeviceOMatic](DYLIBS/DeviceOMatic.md)
- [/System/Library/PrivateFrameworks/DevicePresence.framework/DevicePresence](DYLIBS/DevicePresence.md)
- [/System/Library/PrivateFrameworks/DeviceToDeviceManager.framework/DeviceToDeviceManager](DYLIBS/DeviceToDeviceManager.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/DiagnosticExtensions](DYLIBS/DiagnosticExtensions.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensionsDaemon.framework/DiagnosticExtensionsDaemon](DYLIBS/DiagnosticExtensionsDaemon.md)
- [/System/Library/PrivateFrameworks/DiagnosticLogCollection.framework/DiagnosticLogCollection](DYLIBS/DiagnosticLogCollection.md)
- [/System/Library/PrivateFrameworks/DiagnosticRequest.framework/DiagnosticRequest](DYLIBS/DiagnosticRequest.md)
- [/System/Library/PrivateFrameworks/DiagnosticRequestService.framework/DiagnosticRequestService](DYLIBS/DiagnosticRequestService.md)
- [/System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit](DYLIBS/DiagnosticsKit.md)
- [/System/Library/PrivateFrameworks/DiagnosticsReporterServices.framework/DiagnosticsReporterServices](DYLIBS/DiagnosticsReporterServices.md)
- [/System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport](DYLIBS/DiagnosticsSupport.md)
- [/System/Library/PrivateFrameworks/DialogEngine.framework/DialogEngine](DYLIBS/DialogEngine.md)
- [/System/Library/PrivateFrameworks/DictionaryServices.framework/DictionaryServices](DYLIBS/DictionaryServices.md)
- [/System/Library/PrivateFrameworks/DictionaryUI.framework/DictionaryUI](DYLIBS/DictionaryUI.md)
- [/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/DifferentialPrivacy](DYLIBS/DifferentialPrivacy.md)
- [/System/Library/PrivateFrameworks/DigitalAccess.framework/DigitalAccess](DYLIBS/DigitalAccess.md)
- [/System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation](DYLIBS/DigitalSeparation.md)
- [/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI](DYLIBS/DigitalSeparationUI.md)
- [/System/Library/PrivateFrameworks/DigitalTouchShared.framework/DigitalTouchShared](DYLIBS/DigitalTouchShared.md)
- [/System/Library/PrivateFrameworks/Disembark.framework/Disembark](DYLIBS/Disembark.md)
- [/System/Library/PrivateFrameworks/DisembarkUI.framework/DisembarkUI](DYLIBS/DisembarkUI.md)
- [/System/Library/PrivateFrameworks/DiskArbitration.framework/DiskArbitration](DYLIBS/DiskArbitration.md)
- [/System/Library/PrivateFrameworks/DiskImages.framework/DiskImages](DYLIBS/DiskImages.md)
- [/System/Library/PrivateFrameworks/DiskImages2.framework/DiskImages2](DYLIBS/DiskImages2.md)
- [/System/Library/PrivateFrameworks/DiskSpaceDiagnostics.framework/DiskSpaceDiagnostics](DYLIBS/DiskSpaceDiagnostics.md)
- [/System/Library/PrivateFrameworks/DistributedEvaluation.framework/DistributedEvaluation](DYLIBS/DistributedEvaluation.md)
- [/System/Library/PrivateFrameworks/DistributedSensing.framework/DistributedSensing](DYLIBS/DistributedSensing.md)
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
- [/System/Library/PrivateFrameworks/DragUI.framework/DragUI](DYLIBS/DragUI.md)
- [/System/Library/PrivateFrameworks/DrawingBoard.framework/DrawingBoard](DYLIBS/DrawingBoard.md)
- [/System/Library/PrivateFrameworks/DrawingKit.framework/DrawingKit](DYLIBS/DrawingKit.md)
- [/System/Library/PrivateFrameworks/DriverManagement.framework/DriverManagement](DYLIBS/DriverManagement.md)
- [/System/Library/PrivateFrameworks/DropIn.framework/DropIn](DYLIBS/DropIn.md)
- [/System/Library/PrivateFrameworks/DropInCore.framework/DropInCore](DYLIBS/DropInCore.md)
- [/System/Library/PrivateFrameworks/DuetActivityScheduler.framework/DuetActivityScheduler](DYLIBS/DuetActivityScheduler.md)
- [/System/Library/PrivateFrameworks/EAFirmwareUpdater.framework/EAFirmwareUpdater](DYLIBS/EAFirmwareUpdater.md)
- [/System/Library/PrivateFrameworks/EAP8021X.framework/EAP8021X](DYLIBS/EAP8021X.md)
- [/System/Library/PrivateFrameworks/EasyConfig.framework/EasyConfig](DYLIBS/EasyConfig.md)
- [/System/Library/PrivateFrameworks/EditScript.framework/EditScript](DYLIBS/EditScript.md)
- [/System/Library/PrivateFrameworks/Email.framework/Email](DYLIBS/Email.md)
- [/System/Library/PrivateFrameworks/EmailAddressing.framework/EmailAddressing](DYLIBS/EmailAddressing.md)
- [/System/Library/PrivateFrameworks/EmailCore.framework/EmailCore](DYLIBS/EmailCore.md)
- [/System/Library/PrivateFrameworks/EmailDaemon.framework/EmailDaemon](DYLIBS/EmailDaemon.md)
- [/System/Library/PrivateFrameworks/EmailFoundation.framework/EmailFoundation](DYLIBS/EmailFoundation.md)
- [/System/Library/PrivateFrameworks/EmbeddedAcousticRecognition.framework/EmbeddedAcousticRecognition](DYLIBS/EmbeddedAcousticRecognition.md)
- [/System/Library/PrivateFrameworks/EmbeddedDataReset.framework/EmbeddedDataReset](DYLIBS/EmbeddedDataReset.md)
- [/System/Library/PrivateFrameworks/EmbeddingService.framework/EmbeddingService](DYLIBS/EmbeddingService.md)
- [/System/Library/PrivateFrameworks/EmergencyAlerts.framework/EmergencyAlerts](DYLIBS/EmergencyAlerts.md)
- [/System/Library/PrivateFrameworks/EmojiFoundation.framework/EmojiFoundation](DYLIBS/EmojiFoundation.md)
- [/System/Library/PrivateFrameworks/EmojiKit.framework/EmojiKit](DYLIBS/EmojiKit.md)
- [/System/Library/PrivateFrameworks/EmojiPoster.framework/EmojiPoster](DYLIBS/EmojiPoster.md)
- [/System/Library/PrivateFrameworks/EncoreXPCService.framework/EncoreXPCService](DYLIBS/EncoreXPCService.md)
- [/System/Library/PrivateFrameworks/Engram.framework/Engram](DYLIBS/Engram.md)
- [/System/Library/PrivateFrameworks/EnhancedLoggingState.framework/EnhancedLoggingState](DYLIBS/EnhancedLoggingState.md)
- [/System/Library/PrivateFrameworks/Espresso.framework/Espresso](DYLIBS/Espresso.md)
- [/System/Library/PrivateFrameworks/Espresso.framework/Frameworks/LoopKitGeneratedKernels.framework/LoopKitGeneratedKernels](DYLIBS/LoopKitGeneratedKernels.md)
- [/System/Library/PrivateFrameworks/EventKitTCCUI.framework/EventKitTCCUI](DYLIBS/EventKitTCCUI.md)
- [/System/Library/PrivateFrameworks/EventKitUICore.framework/EventKitUICore](DYLIBS/EventKitUICore.md)
- [/System/Library/PrivateFrameworks/EventMetaDataExtractor.framework/EventMetaDataExtractor](DYLIBS/EventMetaDataExtractor.md)
- [/System/Library/PrivateFrameworks/ExchangeSync.framework/ExchangeSync](DYLIBS/ExchangeSync.md)
- [/System/Library/PrivateFrameworks/ExchangeSync.framework/Frameworks/DAEAS.framework/DAEAS](DYLIBS/DAEAS.md)
- [/System/Library/PrivateFrameworks/ExchangeSync.framework/Frameworks/ESDaemonSupport.framework/ESDaemonSupport](DYLIBS/ESDaemonSupport.md)
- [/System/Library/PrivateFrameworks/ExchangeSyncExpress.framework/ExchangeSyncExpress](DYLIBS/ExchangeSyncExpress.md)
- [/System/Library/PrivateFrameworks/ExpansionBoard.framework/ExpansionBoard](DYLIBS/ExpansionBoard.md)
- [/System/Library/PrivateFrameworks/ExposureNotificationDaemon.framework/ExposureNotificationDaemon](DYLIBS/ExposureNotificationDaemon.md)
- [/System/Library/PrivateFrameworks/EyeRelief.framework/EyeRelief](DYLIBS/EyeRelief.md)
- [/System/Library/PrivateFrameworks/Eyedropper.framework/Eyedropper](DYLIBS/Eyedropper.md)
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
- [/System/Library/PrivateFrameworks/FSKit.framework/FSKit](DYLIBS/FSKit.md)
- [/System/Library/PrivateFrameworks/FTAWD.framework/FTAWD](DYLIBS/FTAWD.md)
- [/System/Library/PrivateFrameworks/FTClientServices.framework/FTClientServices](DYLIBS/FTClientServices.md)
- [/System/Library/PrivateFrameworks/FTServices.framework/FTServices](DYLIBS/FTServices.md)
- [/System/Library/PrivateFrameworks/FaceTimeMessageStore.framework/FaceTimeMessageStore](DYLIBS/FaceTimeMessageStore.md)
- [/System/Library/PrivateFrameworks/FamilyCircle.framework/FamilyCircle](DYLIBS/FamilyCircle.md)
- [/System/Library/PrivateFrameworks/FamilyCircleUI.framework/FamilyCircleUI](DYLIBS/FamilyCircleUI.md)
- [/System/Library/PrivateFrameworks/FamilyControlsObjC.framework/FamilyControlsObjC](DYLIBS/FamilyControlsObjC.md)
- [/System/Library/PrivateFrameworks/FamilyNotification.framework/FamilyNotification](DYLIBS/FamilyNotification.md)
- [/System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags](DYLIBS/FeatureFlags.md)
- [/System/Library/PrivateFrameworks/FeatureFlagsSupport.framework/FeatureFlagsSupport](DYLIBS/FeatureFlagsSupport.md)
- [/System/Library/PrivateFrameworks/FeatureStore.framework/FeatureStore](DYLIBS/FeatureStore.md)
- [/System/Library/PrivateFrameworks/Feedback.framework/Feedback](DYLIBS/Feedback.md)
- [/System/Library/PrivateFrameworks/FeedbackCore.framework/FeedbackCore](DYLIBS/FeedbackCore.md)
- [/System/Library/PrivateFrameworks/FeedbackLogger.framework/FeedbackLogger](DYLIBS/FeedbackLogger.md)
- [/System/Library/PrivateFrameworks/FeedbackService.framework/FeedbackService](DYLIBS/FeedbackService.md)
- [/System/Library/PrivateFrameworks/FileProviderDaemon.framework/FileProviderDaemon](DYLIBS/FileProviderDaemon.md)
- [/System/Library/PrivateFrameworks/FileProviderTelemetry.framework/FileProviderTelemetry](DYLIBS/FileProviderTelemetry.md)
- [/System/Library/PrivateFrameworks/FilesActionsUI.framework/FilesActionsUI](DYLIBS/FilesActionsUI.md)
- [/System/Library/PrivateFrameworks/FinHealth.framework/FinHealth](DYLIBS/FinHealth.md)
- [/System/Library/PrivateFrameworks/FinHealthCore.framework/FinHealthCore](DYLIBS/FinHealthCore.md)
- [/System/Library/PrivateFrameworks/FinHealthInsights.framework/FinHealthInsights](DYLIBS/FinHealthInsights.md)
- [/System/Library/PrivateFrameworks/FinanceDaemon.framework/FinanceDaemon](DYLIBS/FinanceDaemon.md)
- [/System/Library/PrivateFrameworks/FindMyBase.framework/FindMyBase](DYLIBS/FindMyBase.md)
- [/System/Library/PrivateFrameworks/FindMyBluetooth.framework/FindMyBluetooth](DYLIBS/FindMyBluetooth.md)
- [/System/Library/PrivateFrameworks/FindMyCloudKit.framework/FindMyCloudKit](DYLIBS/FindMyCloudKit.md)
- [/System/Library/PrivateFrameworks/FindMyCommon.framework/FindMyCommon](DYLIBS/FindMyCommon.md)
- [/System/Library/PrivateFrameworks/FindMyCrypto.framework/FindMyCrypto](DYLIBS/FindMyCrypto.md)
- [/System/Library/PrivateFrameworks/FindMyDaemonSupport.framework/FindMyDaemonSupport](DYLIBS/FindMyDaemonSupport.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/FindMyDevice](DYLIBS/FindMyDevice.md)
- [/System/Library/PrivateFrameworks/FindMyDeviceUI.framework/FindMyDeviceUI](DYLIBS/FindMyDeviceUI.md)
- [/System/Library/PrivateFrameworks/FindMyLocate.framework/FindMyLocate](DYLIBS/FindMyLocate.md)
- [/System/Library/PrivateFrameworks/FindMyLocateObjCWrapper.framework/FindMyLocateObjCWrapper](DYLIBS/FindMyLocateObjCWrapper.md)
- [/System/Library/PrivateFrameworks/FindMyMessaging.framework/FindMyMessaging](DYLIBS/FindMyMessaging.md)
- [/System/Library/PrivateFrameworks/FindMyServerInteraction.framework/FindMyServerInteraction](DYLIBS/FindMyServerInteraction.md)
- [/System/Library/PrivateFrameworks/FindMyStorage.framework/FindMyStorage](DYLIBS/FindMyStorage.md)
- [/System/Library/PrivateFrameworks/FindMyUICore.framework/FindMyUICore](DYLIBS/FindMyUICore.md)
- [/System/Library/PrivateFrameworks/Fitness.framework/Fitness](DYLIBS/Fitness.md)
- [/System/Library/PrivateFrameworks/FitnessCoaching.framework/FitnessCoaching](DYLIBS/FitnessCoaching.md)
- [/System/Library/PrivateFrameworks/FitnessCoachingCore.framework/FitnessCoachingCore](DYLIBS/FitnessCoachingCore.md)
- [/System/Library/PrivateFrameworks/FitnessCoachingHealthServices.framework/FitnessCoachingHealthServices](DYLIBS/FitnessCoachingHealthServices.md)
- [/System/Library/PrivateFrameworks/FitnessCoachingServices.framework/FitnessCoachingServices](DYLIBS/FitnessCoachingServices.md)
- [/System/Library/PrivateFrameworks/FitnessUI.framework/FitnessUI](DYLIBS/FitnessUI.md)
- [/System/Library/PrivateFrameworks/FlexMusicKit.framework/FlexMusicKit](DYLIBS/FlexMusicKit.md)
- [/System/Library/PrivateFrameworks/FlightUtilities.framework/FlightUtilities](DYLIBS/FlightUtilities.md)
- [/System/Library/PrivateFrameworks/FlightUtilitiesCore.framework/FlightUtilitiesCore](DYLIBS/FlightUtilitiesCore.md)
- [/System/Library/PrivateFrameworks/FlowFrameKit.framework/FlowFrameKit](DYLIBS/FlowFrameKit.md)
- [/System/Library/PrivateFrameworks/Fluid.framework/Fluid](DYLIBS/Fluid.md)
- [/System/Library/PrivateFrameworks/Focus.framework/Focus](DYLIBS/Focus.md)
- [/System/Library/PrivateFrameworks/FocusSettingsUI.framework/FocusSettingsUI](DYLIBS/FocusSettingsUI.md)
- [/System/Library/PrivateFrameworks/FocusUI.framework/FocusUI](DYLIBS/FocusUI.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/FontServices](DYLIBS/FontServices.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/libFontParser.dylib](DYLIBS/libFontParser.dylib.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/libGSFont.dylib](DYLIBS/libGSFont.dylib.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/libGSFontCache.dylib](DYLIBS/libGSFontCache.dylib.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/libType1Scaler.dylib](DYLIBS/libType1Scaler.dylib.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/libhvf.dylib](DYLIBS/libhvf.dylib.md)
- [/System/Library/PrivateFrameworks/FoundInAppsPlugins.framework/FoundInAppsPlugins](DYLIBS/FoundInAppsPlugins.md)
- [/System/Library/PrivateFrameworks/FoundationODR.framework/FoundationODR](DYLIBS/FoundationODR.md)
- [/System/Library/PrivateFrameworks/FriendKit.framework/FriendKit](DYLIBS/FriendKit.md)
- [/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard](DYLIBS/FrontBoard.md)
- [/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices](DYLIBS/FrontBoardServices.md)
- [/System/Library/PrivateFrameworks/FusionTracker.framework/FusionTracker](DYLIBS/FusionTracker.md)
- [/System/Library/PrivateFrameworks/Futhark.framework/Futhark](DYLIBS/Futhark.md)
- [/System/Library/PrivateFrameworks/GLTools.framework/GLTools](DYLIBS/GLTools.md)
- [/System/Library/PrivateFrameworks/GLToolsCore.framework/GLToolsCore](DYLIBS/GLToolsCore.md)
- [/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/libComposeFilters.dylib](DYLIBS/libComposeFilters.dylib.md)
- [/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/libGPUCompiler.dylib](DYLIBS/libGPUCompiler.dylib.md)
- [/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/libGPUCompilerImpl.dylib](DYLIBS/libGPUCompilerImpl.dylib.md)
- [/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/libGPUCompilerImplLazy.dylib](DYLIBS/libGPUCompilerImplLazy.dylib.md)
- [/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/libGPUCompilerUtils.dylib](DYLIBS/libGPUCompilerUtils.dylib.md)
- [/System/Library/PrivateFrameworks/GPURawCounter.framework/GPURawCounter](DYLIBS/GPURawCounter.md)
- [/System/Library/PrivateFrameworks/GPUSupport.framework/libGPUSupportMercury.dylib](DYLIBS/libGPUSupportMercury.dylib.md)
- [/System/Library/PrivateFrameworks/GPUTools.framework/GPUTools](DYLIBS/GPUTools.md)
- [/System/Library/PrivateFrameworks/GPUToolsCore.framework/GPUToolsCore](DYLIBS/GPUToolsCore.md)
- [/System/Library/PrivateFrameworks/GPUToolsPlayback.framework/GPUToolsPlayback](DYLIBS/GPUToolsPlayback.md)
- [/System/Library/PrivateFrameworks/GPUToolsTransport.framework/GPUToolsTransport](DYLIBS/GPUToolsTransport.md)
- [/System/Library/PrivateFrameworks/GPUToolsiOS.framework/GPUToolsiOS](DYLIBS/GPUToolsiOS.md)
- [/System/Library/PrivateFrameworks/GRDBInternal.framework/GRDBInternal](DYLIBS/GRDBInternal.md)
- [/System/Library/PrivateFrameworks/Gambit.framework/Gambit](DYLIBS/Gambit.md)
- [/System/Library/PrivateFrameworks/GameCenterFoundation.framework/GameCenterFoundation](DYLIBS/GameCenterFoundation.md)
- [/System/Library/PrivateFrameworks/GameCenterOverlayService.framework/GameCenterOverlayService](DYLIBS/GameCenterOverlayService.md)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/GameCenterUI](DYLIBS/GameCenterUI.md)
- [/System/Library/PrivateFrameworks/GameCenterUICore.framework/GameCenterUICore](DYLIBS/GameCenterUICore.md)
- [/System/Library/PrivateFrameworks/GameControllerFoundation.framework/GameControllerFoundation](DYLIBS/GameControllerFoundation.md)
- [/System/Library/PrivateFrameworks/GameControllerSettings.framework/GameControllerSettings](DYLIBS/GameControllerSettings.md)
- [/System/Library/PrivateFrameworks/GameKitServices.framework/GameKitServices](DYLIBS/GameKitServices.md)
- [/System/Library/PrivateFrameworks/GamePolicy.framework/GamePolicy](DYLIBS/GamePolicy.md)
- [/System/Library/PrivateFrameworks/GamePolicyServices.framework/GamePolicyServices](DYLIBS/GamePolicyServices.md)
- [/System/Library/PrivateFrameworks/GenerationalStorage.framework/GenerationalStorage](DYLIBS/GenerationalStorage.md)
- [/System/Library/PrivateFrameworks/GeoAnalytics.framework/GeoAnalytics](DYLIBS/GeoAnalytics.md)
- [/System/Library/PrivateFrameworks/GeoServices.framework/GeoServices](DYLIBS/GeoServices.md)
- [/System/Library/PrivateFrameworks/GeoServicesCore.framework/GeoServicesCore](DYLIBS/GeoServicesCore.md)
- [/System/Library/PrivateFrameworks/Geometry.framework/Geometry](DYLIBS/Geometry.md)
- [/System/Library/PrivateFrameworks/GradientPoster.framework/GradientPoster](DYLIBS/GradientPoster.md)
- [/System/Library/PrivateFrameworks/GraphVisualizer.framework/GraphVisualizer](DYLIBS/GraphVisualizer.md)
- [/System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices](DYLIBS/GraphicsServices.md)
- [/System/Library/PrivateFrameworks/GridDataServices.framework/GridDataServices](DYLIBS/GridDataServices.md)
- [/System/Library/PrivateFrameworks/GroupKit.framework/GroupKit](DYLIBS/GroupKit.md)
- [/System/Library/PrivateFrameworks/GroupKitCore.framework/GroupKitCore](DYLIBS/GroupKitCore.md)
- [/System/Library/PrivateFrameworks/GroupKitCrypto.framework/GroupKitCrypto](DYLIBS/GroupKitCrypto.md)
- [/System/Library/PrivateFrameworks/H10ISPServices.framework/H10ISPServices](DYLIBS/H10ISPServices.md)
- [/System/Library/PrivateFrameworks/H16ISPServices.framework/H16ISPServices](DYLIBS/H16ISPServices.md)
- [/System/Library/PrivateFrameworks/HAENotifications.framework/HAENotifications](DYLIBS/HAENotifications.md)
- [/System/Library/PrivateFrameworks/HDRProcessing.framework/HDRProcessing](DYLIBS/HDRProcessing.md)
- [/System/Library/PrivateFrameworks/HID.framework/HID](DYLIBS/HID.md)
- [/System/Library/PrivateFrameworks/HIDAnalytics.framework/HIDAnalytics](DYLIBS/HIDAnalytics.md)
- [/System/Library/PrivateFrameworks/HIDDisplay.framework/HIDDisplay](DYLIBS/HIDDisplay.md)
- [/System/Library/PrivateFrameworks/HIDPreferences.framework/HIDPreferences](DYLIBS/HIDPreferences.md)
- [/System/Library/PrivateFrameworks/HMFoundation.framework/HMFoundation](DYLIBS/HMFoundation.md)
- [/System/Library/PrivateFrameworks/HRTFEnrollment.framework/HRTFEnrollment](DYLIBS/HRTFEnrollment.md)
- [/System/Library/PrivateFrameworks/HSAAuthentication.framework/HSAAuthentication](DYLIBS/HSAAuthentication.md)
- [/System/Library/PrivateFrameworks/HangTracer.framework/HangTracer](DYLIBS/HangTracer.md)
- [/System/Library/PrivateFrameworks/HangTracerSettingsClient.framework/HangTracerSettingsClient](DYLIBS/HangTracerSettingsClient.md)
- [/System/Library/PrivateFrameworks/Haptics.framework/Haptics](DYLIBS/Haptics.md)
- [/System/Library/PrivateFrameworks/HardwareDiagnostics.framework/HardwareDiagnostics](DYLIBS/HardwareDiagnostics.md)
- [/System/Library/PrivateFrameworks/HardwareSupport.framework/HardwareSupport](DYLIBS/HardwareSupport.md)
- [/System/Library/PrivateFrameworks/HeadphoneConfigs.framework/HeadphoneConfigs](DYLIBS/HeadphoneConfigs.md)
- [/System/Library/PrivateFrameworks/HeadphoneSettings.framework/HeadphoneSettings](DYLIBS/HeadphoneSettings.md)
- [/System/Library/PrivateFrameworks/HealthAlgorithms.framework/HealthAlgorithms](DYLIBS/HealthAlgorithms.md)
- [/System/Library/PrivateFrameworks/HealthAppHealthDaemon.framework/HealthAppHealthDaemon](DYLIBS/HealthAppHealthDaemon.md)
- [/System/Library/PrivateFrameworks/HealthAppHealthDaemonSupport.framework/HealthAppHealthDaemonSupport](DYLIBS/HealthAppHealthDaemonSupport.md)
- [/System/Library/PrivateFrameworks/HealthAppServices.framework/HealthAppServices](DYLIBS/HealthAppServices.md)
- [/System/Library/PrivateFrameworks/HealthAppSupport.framework/HealthAppSupport](DYLIBS/HealthAppSupport.md)
- [/System/Library/PrivateFrameworks/HealthArticlesGeneration.framework/HealthArticlesGeneration](DYLIBS/HealthArticlesGeneration.md)
- [/System/Library/PrivateFrameworks/HealthArticlesUI.framework/HealthArticlesUI](DYLIBS/HealthArticlesUI.md)
- [/System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon](DYLIBS/HealthDaemon.md)
- [/System/Library/PrivateFrameworks/HealthDaemonFoundation.framework/HealthDaemonFoundation](DYLIBS/HealthDaemonFoundation.md)
- [/System/Library/PrivateFrameworks/HealthDiagnosticExtensionCore.framework/HealthDiagnosticExtensionCore](DYLIBS/HealthDiagnosticExtensionCore.md)
- [/System/Library/PrivateFrameworks/HealthDomainsTools.framework/HealthDomainsTools](DYLIBS/HealthDomainsTools.md)
- [/System/Library/PrivateFrameworks/HealthExperience.framework/HealthExperience](DYLIBS/HealthExperience.md)
- [/System/Library/PrivateFrameworks/HealthExperienceUI.framework/HealthExperienceUI](DYLIBS/HealthExperienceUI.md)
- [/System/Library/PrivateFrameworks/HealthExposureNotificationUI.framework/HealthExposureNotificationUI](DYLIBS/HealthExposureNotificationUI.md)
- [/System/Library/PrivateFrameworks/HealthHearing.framework/HealthHearing](DYLIBS/HealthHearing.md)
- [/System/Library/PrivateFrameworks/HealthHearingDaemon.framework/HealthHearingDaemon](DYLIBS/HealthHearingDaemon.md)
- [/System/Library/PrivateFrameworks/HealthKitAdditions.framework/HealthKitAdditions](DYLIBS/HealthKitAdditions.md)
- [/System/Library/PrivateFrameworks/HealthMedications.framework/HealthMedications](DYLIBS/HealthMedications.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsDaemonPlugin.framework/HealthMedicationsDaemonPlugin](DYLIBS/HealthMedicationsDaemonPlugin.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsExperience.framework/HealthMedicationsExperience](DYLIBS/HealthMedicationsExperience.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsUI.framework/HealthMedicationsUI](DYLIBS/HealthMedicationsUI.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsVision.framework/HealthMedicationsVision](DYLIBS/HealthMedicationsVision.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsVisionUI.framework/HealthMedicationsVisionUI](DYLIBS/HealthMedicationsVisionUI.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsWidgetUI.framework/HealthMedicationsWidgetUI](DYLIBS/HealthMedicationsWidgetUI.md)
- [/System/Library/PrivateFrameworks/HealthMenstrualCycles.framework/HealthMenstrualCycles](DYLIBS/HealthMenstrualCycles.md)
- [/System/Library/PrivateFrameworks/HealthMenstrualCyclesDaemon.framework/HealthMenstrualCyclesDaemon](DYLIBS/HealthMenstrualCyclesDaemon.md)
- [/System/Library/PrivateFrameworks/HealthMenstrualCyclesUI.framework/HealthMenstrualCyclesUI](DYLIBS/HealthMenstrualCyclesUI.md)
- [/System/Library/PrivateFrameworks/HealthMobility.framework/HealthMobility](DYLIBS/HealthMobility.md)
- [/System/Library/PrivateFrameworks/HealthMobilityDaemon.framework/HealthMobilityDaemon](DYLIBS/HealthMobilityDaemon.md)
- [/System/Library/PrivateFrameworks/HealthMobilityUI.framework/HealthMobilityUI](DYLIBS/HealthMobilityUI.md)
- [/System/Library/PrivateFrameworks/HealthPlatform.framework/HealthPlatform](DYLIBS/HealthPlatform.md)
- [/System/Library/PrivateFrameworks/HealthPlatformCore.framework/HealthPlatformCore](DYLIBS/HealthPlatformCore.md)
- [/System/Library/PrivateFrameworks/HealthPluginHost.framework/HealthPluginHost](DYLIBS/HealthPluginHost.md)
- [/System/Library/PrivateFrameworks/HealthRecordServices.framework/HealthRecordServices](DYLIBS/HealthRecordServices.md)
- [/System/Library/PrivateFrameworks/HealthRecordsConceptsSupport.framework/HealthRecordsConceptsSupport](DYLIBS/HealthRecordsConceptsSupport.md)
- [/System/Library/PrivateFrameworks/HealthRecordsDaemon.framework/HealthRecordsDaemon](DYLIBS/HealthRecordsDaemon.md)
- [/System/Library/PrivateFrameworks/HealthRecordsExtraction.framework/HealthRecordsExtraction](DYLIBS/HealthRecordsExtraction.md)
- [/System/Library/PrivateFrameworks/HealthRecordsUI.framework/HealthRecordsUI](DYLIBS/HealthRecordsUI.md)
- [/System/Library/PrivateFrameworks/HealthRecordsWalletSupport.framework/HealthRecordsWalletSupport](DYLIBS/HealthRecordsWalletSupport.md)
- [/System/Library/PrivateFrameworks/HealthToolbox.framework/HealthToolbox](DYLIBS/HealthToolbox.md)
- [/System/Library/PrivateFrameworks/HealthUI.framework/HealthUI](DYLIBS/HealthUI.md)
- [/System/Library/PrivateFrameworks/HealthVisualization.framework/HealthVisualization](DYLIBS/HealthVisualization.md)
- [/System/Library/PrivateFrameworks/HearingCore.framework/HearingCore](DYLIBS/HearingCore.md)
- [/System/Library/PrivateFrameworks/HearingMLHelper.framework/HearingMLHelper](DYLIBS/HearingMLHelper.md)
- [/System/Library/PrivateFrameworks/HearingUI.framework/HearingUI](DYLIBS/HearingUI.md)
- [/System/Library/PrivateFrameworks/HearingUtilities.framework/HearingUtilities](DYLIBS/HearingUtilities.md)
- [/System/Library/PrivateFrameworks/HeartHealth.framework/HeartHealth](DYLIBS/HeartHealth.md)
- [/System/Library/PrivateFrameworks/HeartHealthDaemon.framework/HeartHealthDaemon](DYLIBS/HeartHealthDaemon.md)
- [/System/Library/PrivateFrameworks/HeartRhythmUI.framework/HeartRhythmUI](DYLIBS/HeartRhythmUI.md)
- [/System/Library/PrivateFrameworks/Heimdal.framework/Heimdal](DYLIBS/Heimdal.md)
- [/System/Library/PrivateFrameworks/HelpKit.framework/HelpKit](DYLIBS/HelpKit.md)
- [/System/Library/PrivateFrameworks/HeroDataClient.framework/HeroDataClient](DYLIBS/HeroDataClient.md)
- [/System/Library/PrivateFrameworks/Home.framework/Home](DYLIBS/Home.md)
- [/System/Library/PrivateFrameworks/HomeAI.framework/HomeAI](DYLIBS/HomeAI.md)
- [/System/Library/PrivateFrameworks/HomeAccessoryControlUI.framework/HomeAccessoryControlUI](DYLIBS/HomeAccessoryControlUI.md)
- [/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/HomeAutomationInternal](DYLIBS/HomeAutomationInternal.md)
- [/System/Library/PrivateFrameworks/HomeCommunicationUIFramework.framework/HomeCommunicationUIFramework](DYLIBS/HomeCommunicationUIFramework.md)
- [/System/Library/PrivateFrameworks/HomeDataModel.framework/HomeDataModel](DYLIBS/HomeDataModel.md)
- [/System/Library/PrivateFrameworks/HomeDeviceSetup.framework/HomeDeviceSetup](DYLIBS/HomeDeviceSetup.md)
- [/System/Library/PrivateFrameworks/HomeEnergy.framework/HomeEnergy](DYLIBS/HomeEnergy.md)
- [/System/Library/PrivateFrameworks/HomeEnergyDaemon.framework/HomeEnergyDaemon](DYLIBS/HomeEnergyDaemon.md)
- [/System/Library/PrivateFrameworks/HomeEnergyUI.framework/HomeEnergyUI](DYLIBS/HomeEnergyUI.md)
- [/System/Library/PrivateFrameworks/HomeKitBackingStore.framework/HomeKitBackingStore](DYLIBS/HomeKitBackingStore.md)
- [/System/Library/PrivateFrameworks/HomeKitCore.framework/HomeKitCore](DYLIBS/HomeKitCore.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemon.framework/HomeKitDaemon](DYLIBS/HomeKitDaemon.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemonLegacy.framework/HomeKitDaemonLegacy](DYLIBS/HomeKitDaemonLegacy.md)
- [/System/Library/PrivateFrameworks/HomeKitEventRouter.framework/HomeKitEventRouter](DYLIBS/HomeKitEventRouter.md)
- [/System/Library/PrivateFrameworks/HomeKitEvents.framework/HomeKitEvents](DYLIBS/HomeKitEvents.md)
- [/System/Library/PrivateFrameworks/HomeKitFeatures.framework/HomeKitFeatures](DYLIBS/HomeKitFeatures.md)
- [/System/Library/PrivateFrameworks/HomeKitMatter.framework/HomeKitMatter](DYLIBS/HomeKitMatter.md)
- [/System/Library/PrivateFrameworks/HomeKitMetrics.framework/HomeKitMetrics](DYLIBS/HomeKitMetrics.md)
- [/System/Library/PrivateFrameworks/HomeMessagingUtils.framework/HomeMessagingUtils](DYLIBS/HomeMessagingUtils.md)
- [/System/Library/PrivateFrameworks/HomePlatformSettingsUI.framework/HomePlatformSettingsUI](DYLIBS/HomePlatformSettingsUI.md)
- [/System/Library/PrivateFrameworks/HomePodSettings.framework/HomePodSettings](DYLIBS/HomePodSettings.md)
- [/System/Library/PrivateFrameworks/HomeRecommendationEngine.framework/HomeRecommendationEngine](DYLIBS/HomeRecommendationEngine.md)
- [/System/Library/PrivateFrameworks/HomeServices.framework/HomeServices](DYLIBS/HomeServices.md)
- [/System/Library/PrivateFrameworks/HomeSharing.framework/HomeSharing](DYLIBS/HomeSharing.md)
- [/System/Library/PrivateFrameworks/HomeUI.framework/HomeUI](DYLIBS/HomeUI.md)
- [/System/Library/PrivateFrameworks/HomeUICommon.framework/HomeUICommon](DYLIBS/HomeUICommon.md)
- [/System/Library/PrivateFrameworks/HomeUtilityServices.framework/HomeUtilityServices](DYLIBS/HomeUtilityServices.md)
- [/System/Library/PrivateFrameworks/HoverTextServices.framework/HoverTextServices](DYLIBS/HoverTextServices.md)
- [/System/Library/PrivateFrameworks/HoverTextUI.framework/HoverTextUI](DYLIBS/HoverTextUI.md)
- [/System/Library/PrivateFrameworks/HumanUnderstandingEvidence.framework/HumanUnderstandingEvidence](DYLIBS/HumanUnderstandingEvidence.md)
- [/System/Library/PrivateFrameworks/HumanUnderstandingFoundation.framework/HumanUnderstandingFoundation](DYLIBS/HumanUnderstandingFoundation.md)
- [/System/Library/PrivateFrameworks/IAP.framework/IAP](DYLIBS/IAP.md)
- [/System/Library/PrivateFrameworks/IAPAuthentication.framework/IAPAuthentication](DYLIBS/IAPAuthentication.md)
- [/System/Library/PrivateFrameworks/IDS.framework/IDS](DYLIBS/IDS.md)
- [/System/Library/PrivateFrameworks/IDSBlastDoorSupport.framework/IDSBlastDoorSupport](DYLIBS/IDSBlastDoorSupport.md)
- [/System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation](DYLIBS/IDSFoundation.md)
- [/System/Library/PrivateFrameworks/IDSHashPersistence.framework/IDSHashPersistence](DYLIBS/IDSHashPersistence.md)
- [/System/Library/PrivateFrameworks/IDSKVStore.framework/IDSKVStore](DYLIBS/IDSKVStore.md)
- [/System/Library/PrivateFrameworks/IMAVCore.framework/IMAVCore](DYLIBS/IMAVCore.md)
- [/System/Library/PrivateFrameworks/IMAssistantCore.framework/IMAssistantCore](DYLIBS/IMAssistantCore.md)
- [/System/Library/PrivateFrameworks/IMCore.framework/IMCore](DYLIBS/IMCore.md)
- [/System/Library/PrivateFrameworks/IMCorePipeline.framework/IMCorePipeline](DYLIBS/IMCorePipeline.md)
- [/System/Library/PrivateFrameworks/IMDMessageServices.framework/IMDMessageServices](DYLIBS/IMDMessageServices.md)
- [/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence](DYLIBS/IMDPersistence.md)
- [/System/Library/PrivateFrameworks/IMDaemonCore.framework/IMDaemonCore](DYLIBS/IMDaemonCore.md)
- [/System/Library/PrivateFrameworks/IMFoundation.framework/IMFoundation](DYLIBS/IMFoundation.md)
- [/System/Library/PrivateFrameworks/IMSharedUI.framework/IMSharedUI](DYLIBS/IMSharedUI.md)
- [/System/Library/PrivateFrameworks/IMSharedUtilities.framework/IMSharedUtilities](DYLIBS/IMSharedUtilities.md)
- [/System/Library/PrivateFrameworks/IMTranscoderAgent.framework/IMTranscoderAgent](DYLIBS/IMTranscoderAgent.md)
- [/System/Library/PrivateFrameworks/IMTranscoding.framework/IMTranscoding](DYLIBS/IMTranscoding.md)
- [/System/Library/PrivateFrameworks/IMTransferAgent.framework/IMTransferAgent](DYLIBS/IMTransferAgent.md)
- [/System/Library/PrivateFrameworks/IMTransferServices.framework/IMTransferServices](DYLIBS/IMTransferServices.md)
- [/System/Library/PrivateFrameworks/IO80211.framework/IO80211](DYLIBS/IO80211.md)
- [/System/Library/PrivateFrameworks/IOAccelMemoryInfo.framework/IOAccelMemoryInfo](DYLIBS/IOAccelMemoryInfo.md)
- [/System/Library/PrivateFrameworks/IOAccelerator.framework/IOAccelerator](DYLIBS/IOAccelerator.md)
- [/System/Library/PrivateFrameworks/IOAccessoryManager.framework/IOAccessoryManager](DYLIBS/IOAccessoryManager.md)
- [/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU](DYLIBS/IOGPU.md)
- [/System/Library/PrivateFrameworks/IOImageLoader.framework/IOImageLoader](DYLIBS/IOImageLoader.md)
- [/System/Library/PrivateFrameworks/IOKitten.framework/IOKitten](DYLIBS/IOKitten.md)
- [/System/Library/PrivateFrameworks/IOMobileFramebuffer.framework/IOMobileFramebuffer](DYLIBS/IOMobileFramebuffer.md)
- [/System/Library/PrivateFrameworks/IOSurfaceAccelerator.framework/IOSurfaceAccelerator](DYLIBS/IOSurfaceAccelerator.md)
- [/System/Library/PrivateFrameworks/IOUSBHost.framework/IOUSBHost](DYLIBS/IOUSBHost.md)
- [/System/Library/PrivateFrameworks/IPTelephony.framework/Support/libIPTelephony.dylib](DYLIBS/libIPTelephony.dylib.md)
- [/System/Library/PrivateFrameworks/ITMLKit.framework/ITMLKit](DYLIBS/ITMLKit.md)
- [/System/Library/PrivateFrameworks/IXATestAppRelay.framework/IXATestAppRelay](DYLIBS/IXATestAppRelay.md)
- [/System/Library/PrivateFrameworks/IconFoundation.framework/IconFoundation](DYLIBS/IconFoundation.md)
- [/System/Library/PrivateFrameworks/IconServices.framework/IconServices](DYLIBS/IconServices.md)
- [/System/Library/PrivateFrameworks/IdleTimerHosting.framework/IdleTimerHosting](DYLIBS/IdleTimerHosting.md)
- [/System/Library/PrivateFrameworks/IdleTimerServices.framework/IdleTimerServices](DYLIBS/IdleTimerServices.md)
- [/System/Library/PrivateFrameworks/ImageHarmonizationKit.framework/ImageHarmonizationKit](DYLIBS/ImageHarmonizationKit.md)
- [/System/Library/PrivateFrameworks/InAppMessages.framework/InAppMessages](DYLIBS/InAppMessages.md)
- [/System/Library/PrivateFrameworks/InAppMessagesCore.framework/InAppMessagesCore](DYLIBS/InAppMessagesCore.md)
- [/System/Library/PrivateFrameworks/IncomingCallFilter.framework/IncomingCallFilter](DYLIBS/IncomingCallFilter.md)
- [/System/Library/PrivateFrameworks/InertiaCam.framework/InertiaCam](DYLIBS/InertiaCam.md)
- [/System/Library/PrivateFrameworks/InfoQueryPersonalizationFeatures.framework/InfoQueryPersonalizationFeatures](DYLIBS/InfoQueryPersonalizationFeatures.md)
- [/System/Library/PrivateFrameworks/InputAnalytics.framework/InputAnalytics](DYLIBS/InputAnalytics.md)
- [/System/Library/PrivateFrameworks/InputContext.framework/InputContext](DYLIBS/InputContext.md)
- [/System/Library/PrivateFrameworks/InputTranscoder.framework/InputTranscoder](DYLIBS/InputTranscoder.md)
- [/System/Library/PrivateFrameworks/InstallCoordination.framework/InstallCoordination](DYLIBS/InstallCoordination.md)
- [/System/Library/PrivateFrameworks/InstallProgress.framework/InstallProgress](DYLIBS/InstallProgress.md)
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
- [/System/Library/PrivateFrameworks/IntentsUICardKitProviderSupport.framework/IntentsUICardKitProviderSupport](DYLIBS/IntentsUICardKitProviderSupport.md)
- [/System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf](DYLIBS/InternalSwiftProtobuf.md)
- [/System/Library/PrivateFrameworks/InternationalSupport.framework/InternationalSupport](DYLIBS/InternationalSupport.md)
- [/System/Library/PrivateFrameworks/InternationalTextSearch.framework/InternationalTextSearch](DYLIBS/InternationalTextSearch.md)
- [/System/Library/PrivateFrameworks/IntlPreferences.framework/IntlPreferences](DYLIBS/IntlPreferences.md)
- [/System/Library/PrivateFrameworks/IntlPreferencesUI.framework/IntlPreferencesUI](DYLIBS/IntlPreferencesUI.md)
- [/System/Library/PrivateFrameworks/IsolatedCoreAudioClient.framework/IsolatedCoreAudioClient](DYLIBS/IsolatedCoreAudioClient.md)
- [/System/Library/PrivateFrameworks/JITAppKit.framework/JITAppKit](DYLIBS/JITAppKit.md)
- [/System/Library/PrivateFrameworks/JasperDepth.framework/JasperDepth](DYLIBS/JasperDepth.md)
- [/System/Library/PrivateFrameworks/Jet.framework/Jet](DYLIBS/Jet.md)
- [/System/Library/PrivateFrameworks/JetEngine.framework/JetEngine](DYLIBS/JetEngine.md)
- [/System/Library/PrivateFrameworks/JetPack.framework/JetPack](DYLIBS/JetPack.md)
- [/System/Library/PrivateFrameworks/JetUI.framework/JetUI](DYLIBS/JetUI.md)
- [/System/Library/PrivateFrameworks/JoinRequests.framework/JoinRequests](DYLIBS/JoinRequests.md)
- [/System/Library/PrivateFrameworks/KRExperiments.framework/KRExperiments](DYLIBS/KRExperiments.md)
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
- [/System/Library/PrivateFrameworks/LegacyGameKit.framework/LegacyGameKit](DYLIBS/LegacyGameKit.md)
- [/System/Library/PrivateFrameworks/Lexicon.framework/Lexicon](DYLIBS/Lexicon.md)
- [/System/Library/PrivateFrameworks/LiftUI.framework/LiftUI](DYLIBS/LiftUI.md)
- [/System/Library/PrivateFrameworks/LighthouseAV.framework/LighthouseAV](DYLIBS/LighthouseAV.md)
- [/System/Library/PrivateFrameworks/LighthouseBackground.framework/LighthouseBackground](DYLIBS/LighthouseBackground.md)
- [/System/Library/PrivateFrameworks/LighthouseBitacoraFramework.framework/LighthouseBitacoraFramework](DYLIBS/LighthouseBitacoraFramework.md)
- [/System/Library/PrivateFrameworks/LighthouseCoreMLFeatureStore.framework/LighthouseCoreMLFeatureStore](DYLIBS/LighthouseCoreMLFeatureStore.md)
- [/System/Library/PrivateFrameworks/LighthouseCoreMLModelAnalysis.framework/LighthouseCoreMLModelAnalysis](DYLIBS/LighthouseCoreMLModelAnalysis.md)
- [/System/Library/PrivateFrameworks/LighthouseCoreMLModelStore.framework/LighthouseCoreMLModelStore](DYLIBS/LighthouseCoreMLModelStore.md)
- [/System/Library/PrivateFrameworks/LighthouseDictation.framework/LighthouseDictation](DYLIBS/LighthouseDictation.md)
- [/System/Library/PrivateFrameworks/LighthouseModelMonitoring.framework/LighthouseModelMonitoring](DYLIBS/LighthouseModelMonitoring.md)
- [/System/Library/PrivateFrameworks/LighthouseNightingale.framework/LighthouseNightingale](DYLIBS/LighthouseNightingale.md)
- [/System/Library/PrivateFrameworks/LighthousePAN.framework/LighthousePAN](DYLIBS/LighthousePAN.md)
- [/System/Library/PrivateFrameworks/LighthouseQuartz.framework/LighthouseQuartz](DYLIBS/LighthouseQuartz.md)
- [/System/Library/PrivateFrameworks/LimitAdTracking.framework/LimitAdTracking](DYLIBS/LimitAdTracking.md)
- [/System/Library/PrivateFrameworks/LinguisticData.framework/LinguisticData](DYLIBS/LinguisticData.md)
- [/System/Library/PrivateFrameworks/LinkMetadata.framework/LinkMetadata](DYLIBS/LinkMetadata.md)
- [/System/Library/PrivateFrameworks/LinkServices.framework/LinkServices](DYLIBS/LinkServices.md)
- [/System/Library/PrivateFrameworks/LiveExecutionResultsFoundation.framework/LiveExecutionResultsFoundation](DYLIBS/LiveExecutionResultsFoundation.md)
- [/System/Library/PrivateFrameworks/LiveExecutionResultsProbe.framework/LiveExecutionResultsProbe](DYLIBS/LiveExecutionResultsProbe.md)
- [/System/Library/PrivateFrameworks/LiveExecutionResultsRuntime.framework/LiveExecutionResultsRuntime](DYLIBS/LiveExecutionResultsRuntime.md)
- [/System/Library/PrivateFrameworks/LiveFS.framework/LiveFS](DYLIBS/LiveFS.md)
- [/System/Library/PrivateFrameworks/LiveFSFPHelper.framework/LiveFSFPHelper](DYLIBS/LiveFSFPHelper.md)
- [/System/Library/PrivateFrameworks/LiveSpeechServices.framework/LiveSpeechServices](DYLIBS/LiveSpeechServices.md)
- [/System/Library/PrivateFrameworks/LiveSpeechUI.framework/LiveSpeechUI](DYLIBS/LiveSpeechUI.md)
- [/System/Library/PrivateFrameworks/LiveTranscription.framework/LiveTranscription](DYLIBS/LiveTranscription.md)
- [/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore](DYLIBS/LocalAuthenticationCore.md)
- [/System/Library/PrivateFrameworks/LocalAuthenticationCoreUI.framework/LocalAuthenticationCoreUI](DYLIBS/LocalAuthenticationCoreUI.md)
- [/System/Library/PrivateFrameworks/LocalAuthenticationPrivateUI.framework/LocalAuthenticationPrivateUI](DYLIBS/LocalAuthenticationPrivateUI.md)
- [/System/Library/PrivateFrameworks/LocalSpeechRecognitionBridge.framework/LocalSpeechRecognitionBridge](DYLIBS/LocalSpeechRecognitionBridge.md)
- [/System/Library/PrivateFrameworks/LocalStatusKit.framework/LocalStatusKit](DYLIBS/LocalStatusKit.md)
- [/System/Library/PrivateFrameworks/LocationSupport.framework/LocationSupport](DYLIBS/LocationSupport.md)
- [/System/Library/PrivateFrameworks/LockdownMode.framework/LockdownMode](DYLIBS/LockdownMode.md)
- [/System/Library/PrivateFrameworks/LockoutUI.framework/LockoutUI](DYLIBS/LockoutUI.md)
- [/System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport](DYLIBS/LoggingSupport.md)
- [/System/Library/PrivateFrameworks/LoginKit.framework/LoginKit](DYLIBS/LoginKit.md)
- [/System/Library/PrivateFrameworks/LoginPerformanceKit.framework/LoginPerformanceKit](DYLIBS/LoginPerformanceKit.md)
- [/System/Library/PrivateFrameworks/LoginUILogViewer.framework/LoginUILogViewer](DYLIBS/LoginUILogViewer.md)
- [/System/Library/PrivateFrameworks/LowPowerMode.framework/LowPowerMode](DYLIBS/LowPowerMode.md)
- [/System/Library/PrivateFrameworks/MDM.framework/MDM](DYLIBS/MDM.md)
- [/System/Library/PrivateFrameworks/MDMClientLibrary.framework/MDMClientLibrary](DYLIBS/MDMClientLibrary.md)
- [/System/Library/PrivateFrameworks/MFAAuthentication.framework/MFAAuthentication](DYLIBS/MFAAuthentication.md)
- [/System/Library/PrivateFrameworks/MIL.framework/MIL](DYLIBS/MIL.md)
- [/System/Library/PrivateFrameworks/MIME.framework/MIME](DYLIBS/MIME.md)
- [/System/Library/PrivateFrameworks/MLAssetIO.framework/MLAssetIO](DYLIBS/MLAssetIO.md)
- [/System/Library/PrivateFrameworks/MLCompilerRuntime.framework/MLCompilerRuntime](DYLIBS/MLCompilerRuntime.md)
- [/System/Library/PrivateFrameworks/MLCompilerServices.framework/MLCompilerServices](DYLIBS/MLCompilerServices.md)
- [/System/Library/PrivateFrameworks/MLKit.framework/MLKit](DYLIBS/MLKit.md)
- [/System/Library/PrivateFrameworks/MLModelSpecification.framework/MLModelSpecification](DYLIBS/MLModelSpecification.md)
- [/System/Library/PrivateFrameworks/MLRuntime.framework/MLRuntime](DYLIBS/MLRuntime.md)
- [/System/Library/PrivateFrameworks/MMCS.framework/MMCS](DYLIBS/MMCS.md)
- [/System/Library/PrivateFrameworks/MMCSServices.framework/MMCSServices](DYLIBS/MMCSServices.md)
- [/System/Library/PrivateFrameworks/MOVStreamIO.framework/MOVStreamIO](DYLIBS/MOVStreamIO.md)
- [/System/Library/PrivateFrameworks/MPUFoundation.framework/MPUFoundation](DYLIBS/MPUFoundation.md)
- [/System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor](DYLIBS/MSUDataAccessor.md)
- [/System/Library/PrivateFrameworks/MTLCompiler.framework/MTLCompiler](DYLIBS/MTLCompiler.md)
- [/System/Library/PrivateFrameworks/MTLCompiler.framework/libMTLCompilerHelper.dylib](DYLIBS/libMTLCompilerHelper.dylib.md)
- [/System/Library/PrivateFrameworks/MTLToolsDeviceSupport.framework/MTLToolsDeviceSupport](DYLIBS/MTLToolsDeviceSupport.md)
- [/System/Library/PrivateFrameworks/MacinTalk.framework/MacinTalk](DYLIBS/MacinTalk.md)
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
- [/System/Library/PrivateFrameworks/ManagedSettingsSupport.framework/ManagedSettingsSupport](DYLIBS/ManagedSettingsSupport.md)
- [/System/Library/PrivateFrameworks/MapsSuggestions.framework/MapsSuggestions](DYLIBS/MapsSuggestions.md)
- [/System/Library/PrivateFrameworks/MapsSupport.framework/MapsSupport](DYLIBS/MapsSupport.md)
- [/System/Library/PrivateFrameworks/MapsSync.framework/MapsSync](DYLIBS/MapsSync.md)
- [/System/Library/PrivateFrameworks/MapsUI.framework/MapsUI](DYLIBS/MapsUI.md)
- [/System/Library/PrivateFrameworks/Marco.framework/Marco](DYLIBS/Marco.md)
- [/System/Library/PrivateFrameworks/MarkupUI.framework/MarkupUI](DYLIBS/MarkupUI.md)
- [/System/Library/PrivateFrameworks/Marrs.framework/Marrs](DYLIBS/Marrs.md)
- [/System/Library/PrivateFrameworks/MaterialKit.framework/MaterialKit](DYLIBS/MaterialKit.md)
- [/System/Library/PrivateFrameworks/MeasureFoundation.framework/MeasureFoundation](DYLIBS/MeasureFoundation.md)
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/MediaAnalysis](DYLIBS/MediaAnalysis.md)
- [/System/Library/PrivateFrameworks/MediaAnalysisServices.framework/MediaAnalysisServices](DYLIBS/MediaAnalysisServices.md)
- [/System/Library/PrivateFrameworks/MediaControlSender.framework/MediaControlSender](DYLIBS/MediaControlSender.md)
- [/System/Library/PrivateFrameworks/MediaControls.framework/MediaControls](DYLIBS/MediaControls.md)
- [/System/Library/PrivateFrameworks/MediaConversionService.framework/MediaConversionService](DYLIBS/MediaConversionService.md)
- [/System/Library/PrivateFrameworks/MediaCoreUI.framework/MediaCoreUI](DYLIBS/MediaCoreUI.md)
- [/System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience](DYLIBS/MediaExperience.md)
- [/System/Library/PrivateFrameworks/MediaFoundation.framework/MediaFoundation](DYLIBS/MediaFoundation.md)
- [/System/Library/PrivateFrameworks/MediaGroups.framework/MediaGroups](DYLIBS/MediaGroups.md)
- [/System/Library/PrivateFrameworks/MediaGroupsDaemon.framework/MediaGroupsDaemon](DYLIBS/MediaGroupsDaemon.md)
- [/System/Library/PrivateFrameworks/MediaKit.framework/MediaKit](DYLIBS/MediaKit.md)
- [/System/Library/PrivateFrameworks/MediaLibraryCore.framework/MediaLibraryCore](DYLIBS/MediaLibraryCore.md)
- [/System/Library/PrivateFrameworks/MediaML.framework/MediaML](DYLIBS/MediaML.md)
- [/System/Library/PrivateFrameworks/MediaMLServices.framework/MediaMLServices](DYLIBS/MediaMLServices.md)
- [/System/Library/PrivateFrameworks/MediaMiningKit.framework/MediaMiningKit](DYLIBS/MediaMiningKit.md)
- [/System/Library/PrivateFrameworks/MediaPlatform.framework/MediaPlatform](DYLIBS/MediaPlatform.md)
- [/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore](DYLIBS/MediaPlaybackCore.md)
- [/System/Library/PrivateFrameworks/MediaPlayerUI.framework/MediaPlayerUI](DYLIBS/MediaPlayerUI.md)
- [/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote](DYLIBS/MediaRemote.md)
- [/System/Library/PrivateFrameworks/MediaRemoteDaemonServices.framework/MediaRemoteDaemonServices](DYLIBS/MediaRemoteDaemonServices.md)
- [/System/Library/PrivateFrameworks/MediaSafetyNet.framework/MediaSafetyNet](DYLIBS/MediaSafetyNet.md)
- [/System/Library/PrivateFrameworks/MediaServices.framework/MediaServices](DYLIBS/MediaServices.md)
- [/System/Library/PrivateFrameworks/MediaServicesBroker.framework/MediaServicesBroker](DYLIBS/MediaServicesBroker.md)
- [/System/Library/PrivateFrameworks/MediaStream.framework/MediaStream](DYLIBS/MediaStream.md)
- [/System/Library/PrivateFrameworks/MemoryDiagnostics.framework/MemoryDiagnostics](DYLIBS/MemoryDiagnostics.md)
- [/System/Library/PrivateFrameworks/MenstrualAlgorithmsInternal.framework/MenstrualAlgorithmsInternal](DYLIBS/MenstrualAlgorithmsInternal.md)
- [/System/Library/PrivateFrameworks/MentalHealth.framework/MentalHealth](DYLIBS/MentalHealth.md)
- [/System/Library/PrivateFrameworks/MentalHealthDaemon.framework/MentalHealthDaemon](DYLIBS/MentalHealthDaemon.md)
- [/System/Library/PrivateFrameworks/MentalHealthUI.framework/MentalHealthUI](DYLIBS/MentalHealthUI.md)
- [/System/Library/PrivateFrameworks/MentalHealthWidgetUI.framework/MentalHealthWidgetUI](DYLIBS/MentalHealthWidgetUI.md)
- [/System/Library/PrivateFrameworks/Mercury.framework/Mercury](DYLIBS/Mercury.md)
- [/System/Library/PrivateFrameworks/Message.framework/MailServices/IMAP.framework/IMAP](DYLIBS/IMAP.md)
- [/System/Library/PrivateFrameworks/Message.framework/MailServices/POP.framework/POP](DYLIBS/POP.md)
- [/System/Library/PrivateFrameworks/Message.framework/Message](DYLIBS/Message.md)
- [/System/Library/PrivateFrameworks/MessageLegacy.framework/MailServices/IMAP.framework/IMAP](DYLIBS/IMAP.md)
- [/System/Library/PrivateFrameworks/MessageLegacy.framework/MessageLegacy](DYLIBS/MessageLegacy.md)
- [/System/Library/PrivateFrameworks/MessageProtection.framework/MessageProtection](DYLIBS/MessageProtection.md)
- [/System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity](DYLIBS/MessageSecurity.md)
- [/System/Library/PrivateFrameworks/MessageSupport.framework/MessageSupport](DYLIBS/MessageSupport.md)
- [/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/MessagesBlastDoorSupport](DYLIBS/MessagesBlastDoorSupport.md)
- [/System/Library/PrivateFrameworks/MessagesCloudSync.framework/MessagesCloudSync](DYLIBS/MessagesCloudSync.md)
- [/System/Library/PrivateFrameworks/MessagesSettingsUI.framework/MessagesSettingsUI](DYLIBS/MessagesSettingsUI.md)
- [/System/Library/PrivateFrameworks/MessagesSupport.framework/MessagesSupport](DYLIBS/MessagesSupport.md)
- [/System/Library/PrivateFrameworks/MetadataUtilities.framework/MetadataUtilities](DYLIBS/MetadataUtilities.md)
- [/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools](DYLIBS/MetalTools.md)
- [/System/Library/PrivateFrameworks/MetricKitCore.framework/MetricKitCore](DYLIBS/MetricKitCore.md)
- [/System/Library/PrivateFrameworks/MetricKitServices.framework/MetricKitServices](DYLIBS/MetricKitServices.md)
- [/System/Library/PrivateFrameworks/MetricKitSource.framework/MetricKitSource](DYLIBS/MetricKitSource.md)
- [/System/Library/PrivateFrameworks/MetricMeasurement.framework/MetricMeasurement](DYLIBS/MetricMeasurement.md)
- [/System/Library/PrivateFrameworks/MetricsFramework.framework/MetricsFramework](DYLIBS/MetricsFramework.md)
- [/System/Library/PrivateFrameworks/MetricsKit.framework/MetricsKit](DYLIBS/MetricsKit.md)
- [/System/Library/PrivateFrameworks/MigrationKit.framework/MigrationKit](DYLIBS/MigrationKit.md)
- [/System/Library/PrivateFrameworks/MilAneflow.framework/MilAneflow](DYLIBS/MilAneflow.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/MobileAccessoryUpdater](DYLIBS/MobileAccessoryUpdater.md)
- [/System/Library/PrivateFrameworks/MobileActivation.framework/MobileActivation](DYLIBS/MobileActivation.md)
- [/System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset](DYLIBS/MobileAsset.md)
- [/System/Library/PrivateFrameworks/MobileAssetUpdater.framework/MobileAssetUpdater](DYLIBS/MobileAssetUpdater.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup](DYLIBS/MobileBackup.md)
- [/System/Library/PrivateFrameworks/MobileBluetooth.framework/MobileBluetooth](DYLIBS/MobileBluetooth.md)
- [/System/Library/PrivateFrameworks/MobileContainerManager.framework/MobileContainerManager](DYLIBS/MobileContainerManager.md)
- [/System/Library/PrivateFrameworks/MobileDeviceLink.framework/MobileDeviceLink](DYLIBS/MobileDeviceLink.md)
- [/System/Library/PrivateFrameworks/MobileIcons.framework/MobileIcons](DYLIBS/MobileIcons.md)
- [/System/Library/PrivateFrameworks/MobileInBoxUpdate.framework/MobileInBoxUpdate](DYLIBS/MobileInBoxUpdate.md)
- [/System/Library/PrivateFrameworks/MobileInstallation.framework/MobileInstallation](DYLIBS/MobileInstallation.md)
- [/System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag](DYLIBS/MobileKeyBag.md)
- [/System/Library/PrivateFrameworks/MobileLookup.framework/MobileLookup](DYLIBS/MobileLookup.md)
- [/System/Library/PrivateFrameworks/MobileMailUI.framework/MobileMailUI](DYLIBS/MobileMailUI.md)
- [/System/Library/PrivateFrameworks/MobileObliteration.framework/MobileObliteration](DYLIBS/MobileObliteration.md)
- [/System/Library/PrivateFrameworks/MobileSafari.framework/MobileSafari](DYLIBS/MobileSafari.md)
- [/System/Library/PrivateFrameworks/MobileSafari.framework/PlugIns/Safari.wkbundle/Safari](DYLIBS/Safari.md)
- [/System/Library/PrivateFrameworks/MobileSafariSwift.framework/MobileSafariSwift](DYLIBS/MobileSafariSwift.md)
- [/System/Library/PrivateFrameworks/MobileSafariUI.framework/MobileSafariUI](DYLIBS/MobileSafariUI.md)
- [/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/MobileSoftwareUpdate](DYLIBS/MobileSoftwareUpdate.md)
- [/System/Library/PrivateFrameworks/MobileSpotlightIndex.framework/MobileSpotlightIndex](DYLIBS/MobileSpotlightIndex.md)
- [/System/Library/PrivateFrameworks/MobileStorage.framework/MobileStorage](DYLIBS/MobileStorage.md)
- [/System/Library/PrivateFrameworks/MobileStoreDemoKit.framework/MobileStoreDemoKit](DYLIBS/MobileStoreDemoKit.md)
- [/System/Library/PrivateFrameworks/MobileStoreDemoSetupUI.framework/MobileStoreDemoSetupUI](DYLIBS/MobileStoreDemoSetupUI.md)
- [/System/Library/PrivateFrameworks/MobileStoreUI.framework/MobileStoreUI](DYLIBS/MobileStoreUI.md)
- [/System/Library/PrivateFrameworks/MobileSync.framework/MobileSync](DYLIBS/MobileSync.md)
- [/System/Library/PrivateFrameworks/MobileSystemServices.framework/MobileSystemServices](DYLIBS/MobileSystemServices.md)
- [/System/Library/PrivateFrameworks/MobileTimer.framework/MobileTimer](DYLIBS/MobileTimer.md)
- [/System/Library/PrivateFrameworks/MobileTimerSupport.framework/MobileTimerSupport](DYLIBS/MobileTimerSupport.md)
- [/System/Library/PrivateFrameworks/MobileTimerUI.framework/MobileTimerUI](DYLIBS/MobileTimerUI.md)
- [/System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi](DYLIBS/MobileWiFi.md)
- [/System/Library/PrivateFrameworks/ModalityXObjects.framework/ModalityXObjects](DYLIBS/ModalityXObjects.md)
- [/System/Library/PrivateFrameworks/Moments.framework/Moments](DYLIBS/Moments.md)
- [/System/Library/PrivateFrameworks/MomentsData.framework/MomentsData](DYLIBS/MomentsData.md)
- [/System/Library/PrivateFrameworks/MomentsOnboardingAndSettings.framework/MomentsOnboardingAndSettings](DYLIBS/MomentsOnboardingAndSettings.md)
- [/System/Library/PrivateFrameworks/MonogramPoster.framework/MonogramPoster](DYLIBS/MonogramPoster.md)
- [/System/Library/PrivateFrameworks/Montreal.framework/Montreal](DYLIBS/Montreal.md)
- [/System/Library/PrivateFrameworks/MorphunAssets.framework/MorphunAssets](DYLIBS/MorphunAssets.md)
- [/System/Library/PrivateFrameworks/MorphunSwift.framework/MorphunSwift](DYLIBS/MorphunSwift.md)
- [/System/Library/PrivateFrameworks/MotionSensorLogging.framework/MotionSensorLogging](DYLIBS/MotionSensorLogging.md)
- [/System/Library/PrivateFrameworks/MultitouchSessionFilterSupport.framework/MultitouchSessionFilterSupport](DYLIBS/MultitouchSessionFilterSupport.md)
- [/System/Library/PrivateFrameworks/MultitouchSupport.framework/MultitouchSupport](DYLIBS/MultitouchSupport.md)
- [/System/Library/PrivateFrameworks/MusicCarDisplayUI.framework/MusicCarDisplayUI](DYLIBS/MusicCarDisplayUI.md)
- [/System/Library/PrivateFrameworks/MusicKitInternal.framework/MusicKitInternal](DYLIBS/MusicKitInternal.md)
- [/System/Library/PrivateFrameworks/MusicLibrary.framework/MusicLibrary](DYLIBS/MusicLibrary.md)
- [/System/Library/PrivateFrameworks/MusicSettingsSupport.framework/MusicSettingsSupport](DYLIBS/MusicSettingsSupport.md)
- [/System/Library/PrivateFrameworks/MusicStoreUI.framework/MusicStoreUI](DYLIBS/MusicStoreUI.md)
- [/System/Library/PrivateFrameworks/MusicUI.framework/MusicUI](DYLIBS/MusicUI.md)
- [/System/Library/PrivateFrameworks/NCLaunchStats.framework/NCLaunchStats](DYLIBS/NCLaunchStats.md)
- [/System/Library/PrivateFrameworks/NLP.framework/NLP](DYLIBS/NLP.md)
- [/System/Library/PrivateFrameworks/NLPLearner.framework/NLPLearner](DYLIBS/NLPLearner.md)
- [/System/Library/PrivateFrameworks/NPTKit.framework/NPTKit](DYLIBS/NPTKit.md)
- [/System/Library/PrivateFrameworks/NanoAppRegistry.framework/NanoAppRegistry](DYLIBS/NanoAppRegistry.md)
- [/System/Library/PrivateFrameworks/NanoAudioControl.framework/NanoAudioControl](DYLIBS/NanoAudioControl.md)
- [/System/Library/PrivateFrameworks/NanoBackup.framework/NanoBackup](DYLIBS/NanoBackup.md)
- [/System/Library/PrivateFrameworks/NanoComplicationSettings.framework/NanoComplicationSettings](DYLIBS/NanoComplicationSettings.md)
- [/System/Library/PrivateFrameworks/NanoLeash.framework/NanoLeash](DYLIBS/NanoLeash.md)
- [/System/Library/PrivateFrameworks/NanoMailCompanionUI.framework/NanoMailCompanionUI](DYLIBS/NanoMailCompanionUI.md)
- [/System/Library/PrivateFrameworks/NanoMailKitServer.framework/NanoMailKitServer](DYLIBS/NanoMailKitServer.md)
- [/System/Library/PrivateFrameworks/NanoMediaAPI.framework/NanoMediaAPI](DYLIBS/NanoMediaAPI.md)
- [/System/Library/PrivateFrameworks/NanoMediaBridgeUI.framework/NanoMediaBridgeUI](DYLIBS/NanoMediaBridgeUI.md)
- [/System/Library/PrivateFrameworks/NanoMediaRemote.framework/NanoMediaRemote](DYLIBS/NanoMediaRemote.md)
- [/System/Library/PrivateFrameworks/NanoMusicSync.framework/NanoMusicSync](DYLIBS/NanoMusicSync.md)
- [/System/Library/PrivateFrameworks/NanoPassKit.framework/NanoPassKit](DYLIBS/NanoPassKit.md)
- [/System/Library/PrivateFrameworks/NanoPhotosCore.framework/NanoPhotosCore](DYLIBS/NanoPhotosCore.md)
- [/System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync](DYLIBS/NanoPreferencesSync.md)
- [/System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry](DYLIBS/NanoRegistry.md)
- [/System/Library/PrivateFrameworks/NanoResourceGrabber.framework/NanoResourceGrabber](DYLIBS/NanoResourceGrabber.md)
- [/System/Library/PrivateFrameworks/NanoSystemSettings.framework/NanoSystemSettings](DYLIBS/NanoSystemSettings.md)
- [/System/Library/PrivateFrameworks/NanoTimeKit.framework/NanoTimeKit](DYLIBS/NanoTimeKit.md)
- [/System/Library/PrivateFrameworks/NanoTimeKitCompanion.framework/NanoTimeKitCompanion](DYLIBS/NanoTimeKitCompanion.md)
- [/System/Library/PrivateFrameworks/NanoUniverse.framework/NanoUniverse](DYLIBS/NanoUniverse.md)
- [/System/Library/PrivateFrameworks/NanoWeatherComplicationsCompanion.framework/NanoWeatherComplicationsCompanion](DYLIBS/NanoWeatherComplicationsCompanion.md)
- [/System/Library/PrivateFrameworks/NanoWeatherKitUICompanion.framework/NanoWeatherKitUICompanion](DYLIBS/NanoWeatherKitUICompanion.md)
- [/System/Library/PrivateFrameworks/Navigation.framework/Navigation](DYLIBS/Navigation.md)
- [/System/Library/PrivateFrameworks/NearField.framework/NearField](DYLIBS/NearField.md)
- [/System/Library/PrivateFrameworks/NearFieldAccessory.framework/NearFieldAccessory](DYLIBS/NearFieldAccessory.md)
- [/System/Library/PrivateFrameworks/NearbySessions.framework/NearbySessions](DYLIBS/NearbySessions.md)
- [/System/Library/PrivateFrameworks/NeighborhoodActivityConduit.framework/NeighborhoodActivityConduit](DYLIBS/NeighborhoodActivityConduit.md)
- [/System/Library/PrivateFrameworks/NetAppsUtilities.framework/NetAppsUtilities](DYLIBS/NetAppsUtilities.md)
- [/System/Library/PrivateFrameworks/NetAppsUtilitiesUI.framework/NetAppsUtilitiesUI](DYLIBS/NetAppsUtilitiesUI.md)
- [/System/Library/PrivateFrameworks/Netrb.framework/Netrb](DYLIBS/Netrb.md)
- [/System/Library/PrivateFrameworks/NetworkQualityServices.framework/NetworkQualityServices](DYLIBS/NetworkQualityServices.md)
- [/System/Library/PrivateFrameworks/NetworkRelay.framework/NetworkRelay](DYLIBS/NetworkRelay.md)
- [/System/Library/PrivateFrameworks/NetworkServiceProxy.framework/NetworkServiceProxy](DYLIBS/NetworkServiceProxy.md)
- [/System/Library/PrivateFrameworks/NetworkStatistics.framework/NetworkStatistics](DYLIBS/NetworkStatistics.md)
- [/System/Library/PrivateFrameworks/NeuralNetworks.framework/NeuralNetworks](DYLIBS/NeuralNetworks.md)
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
- [/System/Library/PrivateFrameworks/NewsURLResolution.framework/NewsURLResolution](DYLIBS/NewsURLResolution.md)
- [/System/Library/PrivateFrameworks/Nexus.framework/Nexus](DYLIBS/Nexus.md)
- [/System/Library/PrivateFrameworks/NexusDaemon.framework/NexusDaemon](DYLIBS/NexusDaemon.md)
- [/System/Library/PrivateFrameworks/NightingaleTraining.framework/NightingaleTraining](DYLIBS/NightingaleTraining.md)
- [/System/Library/PrivateFrameworks/NonverbalCues.framework/NonverbalCues](DYLIBS/NonverbalCues.md)
- [/System/Library/PrivateFrameworks/NotTheStoreKitUIFrameworkYouAreLookingFor.framework/NotTheStoreKitUIFrameworkYouAreLookingFor](DYLIBS/NotTheStoreKitUIFrameworkYouAreLookingFor.md)
- [/System/Library/PrivateFrameworks/Notes.framework/Notes](DYLIBS/Notes.md)
- [/System/Library/PrivateFrameworks/NotesAnalytics.framework/NotesAnalytics](DYLIBS/NotesAnalytics.md)
- [/System/Library/PrivateFrameworks/NotesEditor.framework/NotesEditor](DYLIBS/NotesEditor.md)
- [/System/Library/PrivateFrameworks/NotesPreviewKit.framework/NotesPreviewKit](DYLIBS/NotesPreviewKit.md)
- [/System/Library/PrivateFrameworks/NotesShared.framework/NotesShared](DYLIBS/NotesShared.md)
- [/System/Library/PrivateFrameworks/NotesSupport.framework/NotesSupport](DYLIBS/NotesSupport.md)
- [/System/Library/PrivateFrameworks/NotesUI.framework/NotesUI](DYLIBS/NotesUI.md)
- [/System/Library/PrivateFrameworks/NotesUIServices.framework/NotesUIServices](DYLIBS/NotesUIServices.md)
- [/System/Library/PrivateFrameworks/OAuth.framework/OAuth](DYLIBS/OAuth.md)
- [/System/Library/PrivateFrameworks/ODCurareAnalysis.framework/ODCurareAnalysis](DYLIBS/ODCurareAnalysis.md)
- [/System/Library/PrivateFrameworks/ODCurareEvaluationAndReporting.framework/ODCurareEvaluationAndReporting](DYLIBS/ODCurareEvaluationAndReporting.md)
- [/System/Library/PrivateFrameworks/OSAServicesClient.framework/OSAServicesClient](DYLIBS/OSAServicesClient.md)
- [/System/Library/PrivateFrameworks/OSASubmissionClient.framework/OSASubmissionClient](DYLIBS/OSASubmissionClient.md)
- [/System/Library/PrivateFrameworks/OSASyncProxyClient.framework/OSASyncProxyClient](DYLIBS/OSASyncProxyClient.md)
- [/System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics](DYLIBS/OSAnalytics.md)
- [/System/Library/PrivateFrameworks/OSAnalyticsPrivate.framework/OSAnalyticsPrivate](DYLIBS/OSAnalyticsPrivate.md)
- [/System/Library/PrivateFrameworks/OSIntelligence.framework/OSIntelligence](DYLIBS/OSIntelligence.md)
- [/System/Library/PrivateFrameworks/OTSVG.framework/OTSVG](DYLIBS/OTSVG.md)
- [/System/Library/PrivateFrameworks/ObjectUnderstanding.framework/ObjectUnderstanding](DYLIBS/ObjectUnderstanding.md)
- [/System/Library/PrivateFrameworks/OctagonTrust.framework/OctagonTrust](DYLIBS/OctagonTrust.md)
- [/System/Library/PrivateFrameworks/OfficeImport.framework/OfficeImport](DYLIBS/OfficeImport.md)
- [/System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit](DYLIBS/OnBoardingKit.md)
- [/System/Library/PrivateFrameworks/OpticalFlowFramework.framework/OpticalFlowFramework](DYLIBS/OpticalFlowFramework.md)
- [/System/Library/PrivateFrameworks/Osprey.framework/Osprey](DYLIBS/Osprey.md)
- [/System/Library/PrivateFrameworks/PBBridgeSupport.framework/PBBridgeSupport](DYLIBS/PBBridgeSupport.md)
- [/System/Library/PrivateFrameworks/PDS.framework/PDS](DYLIBS/PDS.md)
- [/System/Library/PrivateFrameworks/PDSAgent.framework/PDSAgent](DYLIBS/PDSAgent.md)
- [/System/Library/PrivateFrameworks/PLSnapshot.framework/PLSnapshot](DYLIBS/PLSnapshot.md)
- [/System/Library/PrivateFrameworks/PacketFilter.framework/PacketFilter](DYLIBS/PacketFilter.md)
- [/System/Library/PrivateFrameworks/PairedSync.framework/PairedSync](DYLIBS/PairedSync.md)
- [/System/Library/PrivateFrameworks/PairedUnlock.framework/PairedUnlock](DYLIBS/PairedUnlock.md)
- [/System/Library/PrivateFrameworks/PairingProximity.framework/PairingProximity](DYLIBS/PairingProximity.md)
- [/System/Library/PrivateFrameworks/PaperBoardUI.framework/PaperBoardUI](DYLIBS/PaperBoardUI.md)
- [/System/Library/PrivateFrameworks/PaperKit.framework/PaperKit](DYLIBS/PaperKit.md)
- [/System/Library/PrivateFrameworks/ParavirtualizedANE.framework/ParavirtualizedANE](DYLIBS/ParavirtualizedANE.md)
- [/System/Library/PrivateFrameworks/ParsecModel.framework/ParsecModel](DYLIBS/ParsecModel.md)
- [/System/Library/PrivateFrameworks/ParsecSubscriptionServiceSupport.framework/ParsecSubscriptionServiceSupport](DYLIBS/ParsecSubscriptionServiceSupport.md)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore](DYLIBS/PassKitCore.md)
- [/System/Library/PrivateFrameworks/PassKitServices.framework/PassKitServices](DYLIBS/PassKitServices.md)
- [/System/Library/PrivateFrameworks/PassKitUI.framework/PassKitUI](DYLIBS/PassKitUI.md)
- [/System/Library/PrivateFrameworks/PassKitUIFoundation.framework/PassKitUIFoundation](DYLIBS/PassKitUIFoundation.md)
- [/System/Library/PrivateFrameworks/PasswordManagerUI.framework/PasswordManagerUI](DYLIBS/PasswordManagerUI.md)
- [/System/Library/PrivateFrameworks/Pasteboard.framework/Pasteboard](DYLIBS/Pasteboard.md)
- [/System/Library/PrivateFrameworks/PaymentUI.framework/PaymentUI](DYLIBS/PaymentUI.md)
- [/System/Library/PrivateFrameworks/PaymentUIBase.framework/PaymentUIBase](DYLIBS/PaymentUIBase.md)
- [/System/Library/PrivateFrameworks/Pegasus.framework/Pegasus](DYLIBS/Pegasus.md)
- [/System/Library/PrivateFrameworks/PegasusAPI.framework/PegasusAPI](DYLIBS/PegasusAPI.md)
- [/System/Library/PrivateFrameworks/PegasusConfiguration.framework/PegasusConfiguration](DYLIBS/PegasusConfiguration.md)
- [/System/Library/PrivateFrameworks/PegasusKit.framework/PegasusKit](DYLIBS/PegasusKit.md)
- [/System/Library/PrivateFrameworks/PegasusPersistence.framework/PegasusPersistence](DYLIBS/PegasusPersistence.md)
- [/System/Library/PrivateFrameworks/PencilPairingUI.framework/PencilPairingUI](DYLIBS/PencilPairingUI.md)
- [/System/Library/PrivateFrameworks/People.framework/People](DYLIBS/People.md)
- [/System/Library/PrivateFrameworks/PeopleSuggester.framework/PeopleSuggester](DYLIBS/PeopleSuggester.md)
- [/System/Library/PrivateFrameworks/PeopleUI.framework/PeopleUI](DYLIBS/PeopleUI.md)
- [/System/Library/PrivateFrameworks/PeopleUIInternal.framework/PeopleUIInternal](DYLIBS/PeopleUIInternal.md)
- [/System/Library/PrivateFrameworks/PerfPowerMetricMonitor.framework/PerfPowerMetricMonitor](DYLIBS/PerfPowerMetricMonitor.md)
- [/System/Library/PrivateFrameworks/PerfPowerServicesMetadata.framework/PerfPowerServicesMetadata](DYLIBS/PerfPowerServicesMetadata.md)
- [/System/Library/PrivateFrameworks/PerfPowerServicesReader.framework/PerfPowerServicesReader](DYLIBS/PerfPowerServicesReader.md)
- [/System/Library/PrivateFrameworks/PerformanceControlKit.framework/PerformanceControlKit](DYLIBS/PerformanceControlKit.md)
- [/System/Library/PrivateFrameworks/PerformanceTrace.framework/PerformanceTrace](DYLIBS/PerformanceTrace.md)
- [/System/Library/PrivateFrameworks/PeridotDepth.framework/PeridotDepth](DYLIBS/PeridotDepth.md)
- [/System/Library/PrivateFrameworks/PersistentConnection.framework/PersistentConnection](DYLIBS/PersistentConnection.md)
- [/System/Library/PrivateFrameworks/PersonaKit.framework/PersonaKit](DYLIBS/PersonaKit.md)
- [/System/Library/PrivateFrameworks/PersonaUI.framework/PersonaUI](DYLIBS/PersonaUI.md)
- [/System/Library/PrivateFrameworks/PersonalAudio.framework/PersonalAudio](DYLIBS/PersonalAudio.md)
- [/System/Library/PrivateFrameworks/PersonalIntelligenceCore.framework/PersonalIntelligenceCore](DYLIBS/PersonalIntelligenceCore.md)
- [/System/Library/PrivateFrameworks/PersonalizationPortrait.framework/PersonalizationPortrait](DYLIBS/PersonalizationPortrait.md)
- [/System/Library/PrivateFrameworks/PersonalizationPortraitInternals.framework/PersonalizationPortraitInternals](DYLIBS/PersonalizationPortraitInternals.md)
- [/System/Library/PrivateFrameworks/Phoenix.framework/Phoenix](DYLIBS/Phoenix.md)
- [/System/Library/PrivateFrameworks/PhoneNumberResolver.framework/PhoneNumberResolver](DYLIBS/PhoneNumberResolver.md)
- [/System/Library/PrivateFrameworks/PhoneNumbers.framework/PhoneNumbers](DYLIBS/PhoneNumbers.md)
- [/System/Library/PrivateFrameworks/PhoneSnippetUI.framework/PhoneSnippetUI](DYLIBS/PhoneSnippetUI.md)
- [/System/Library/PrivateFrameworks/PhotoAnalysis.framework/PhotoAnalysis](DYLIBS/PhotoAnalysis.md)
- [/System/Library/PrivateFrameworks/PhotoBoothEffects.framework/PhotoBoothEffects](DYLIBS/PhotoBoothEffects.md)
- [/System/Library/PrivateFrameworks/PhotoFoundation.framework/PhotoFoundation](DYLIBS/PhotoFoundation.md)
- [/System/Library/PrivateFrameworks/PhotoImaging.framework/PhotoImaging](DYLIBS/PhotoImaging.md)
- [/System/Library/PrivateFrameworks/PhotoLibrary.framework/PhotoLibrary](DYLIBS/PhotoLibrary.md)
- [/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/PhotoLibraryServices](DYLIBS/PhotoLibraryServices.md)
- [/System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/PhotoLibraryServicesCore](DYLIBS/PhotoLibraryServicesCore.md)
- [/System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats](DYLIBS/PhotosFormats.md)
- [/System/Library/PrivateFrameworks/PhotosGraph.framework/PhotosGraph](DYLIBS/PhotosGraph.md)
- [/System/Library/PrivateFrameworks/PhotosImagingFoundation.framework/PhotosImagingFoundation](DYLIBS/PhotosImagingFoundation.md)
- [/System/Library/PrivateFrameworks/PhotosIntelligence.framework/PhotosIntelligence](DYLIBS/PhotosIntelligence.md)
- [/System/Library/PrivateFrameworks/PhotosKnowledgeGraph.framework/PhotosKnowledgeGraph](DYLIBS/PhotosKnowledgeGraph.md)
- [/System/Library/PrivateFrameworks/PhotosPlayer.framework/PhotosPlayer](DYLIBS/PhotosPlayer.md)
- [/System/Library/PrivateFrameworks/PhotosUICore.framework/PhotosUICore](DYLIBS/PhotosUICore.md)
- [/System/Library/PrivateFrameworks/PhotosUIEdit.framework/PhotosUIEdit](DYLIBS/PhotosUIEdit.md)
- [/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PhotosUIPrivate](DYLIBS/PhotosUIPrivate.md)
- [/System/Library/PrivateFrameworks/PhotosensitivityProcessing.framework/PhotosensitivityProcessing](DYLIBS/PhotosensitivityProcessing.md)
- [/System/Library/PrivateFrameworks/PhysicsKit.framework/PhysicsKit](DYLIBS/PhysicsKit.md)
- [/System/Library/PrivateFrameworks/PlacesKit.framework/PlacesKit](DYLIBS/PlacesKit.md)
- [/System/Library/PrivateFrameworks/PlatformSSO.framework/PlatformSSO](DYLIBS/PlatformSSO.md)
- [/System/Library/PrivateFrameworks/PlatterKit.framework/PlatterKit](DYLIBS/PlatterKit.md)
- [/System/Library/PrivateFrameworks/PlugInKit.framework/PlugInKit](DYLIBS/PlugInKit.md)
- [/System/Library/PrivateFrameworks/PodcastsFoundation.framework/PodcastsFoundation](DYLIBS/PodcastsFoundation.md)
- [/System/Library/PrivateFrameworks/PodcastsKit.framework/PodcastsKit](DYLIBS/PodcastsKit.md)
- [/System/Library/PrivateFrameworks/PodcastsUI.framework/PodcastsUI](DYLIBS/PodcastsUI.md)
- [/System/Library/PrivateFrameworks/PointerUIServices.framework/PointerUIServices](DYLIBS/PointerUIServices.md)
- [/System/Library/PrivateFrameworks/PointerUISystemServices.framework/PointerUISystemServices](DYLIBS/PointerUISystemServices.md)
- [/System/Library/PrivateFrameworks/Portrait.framework/Portrait](DYLIBS/Portrait.md)
- [/System/Library/PrivateFrameworks/PortraitCore.framework/PortraitCore](DYLIBS/PortraitCore.md)
- [/System/Library/PrivateFrameworks/PostSiriEngagement.framework/PostSiriEngagement](DYLIBS/PostSiriEngagement.md)
- [/System/Library/PrivateFrameworks/PosterBoard.framework/PosterBoard](DYLIBS/PosterBoard.md)
- [/System/Library/PrivateFrameworks/PosterBoardServices.framework/PosterBoardServices](DYLIBS/PosterBoardServices.md)
- [/System/Library/PrivateFrameworks/PosterBoardUI.framework/PosterBoardUI](DYLIBS/PosterBoardUI.md)
- [/System/Library/PrivateFrameworks/PosterBoardUIServices.framework/PosterBoardUIServices](DYLIBS/PosterBoardUIServices.md)
- [/System/Library/PrivateFrameworks/PosterKit.framework/PosterKit](DYLIBS/PosterKit.md)
- [/System/Library/PrivateFrameworks/PowerLog.framework/PowerLog](DYLIBS/PowerLog.md)
- [/System/Library/PrivateFrameworks/PowerUI.framework/PowerUI](DYLIBS/PowerUI.md)
- [/System/Library/PrivateFrameworks/PowerlogAccounting.framework/PowerlogAccounting](DYLIBS/PowerlogAccounting.md)
- [/System/Library/PrivateFrameworks/PowerlogControl.framework/PowerlogControl](DYLIBS/PowerlogControl.md)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore](DYLIBS/PowerlogCore.md)
- [/System/Library/PrivateFrameworks/PowerlogDatabaseReader.framework/PowerlogDatabaseReader](DYLIBS/PowerlogDatabaseReader.md)
- [/System/Library/PrivateFrameworks/PowerlogFullOperators.framework/PowerlogFullOperators](DYLIBS/PowerlogFullOperators.md)
- [/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators](DYLIBS/PowerlogHelperdOperators.md)
- [/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators](DYLIBS/PowerlogLiteOperators.md)
- [/System/Library/PrivateFrameworks/Preferences.framework/Preferences](DYLIBS/Preferences.md)
- [/System/Library/PrivateFrameworks/PreferencesUI.framework/PreferencesUI](DYLIBS/PreferencesUI.md)
- [/System/Library/PrivateFrameworks/PreviewShellKit.framework/PreviewShellKit](DYLIBS/PreviewShellKit.md)
- [/System/Library/PrivateFrameworks/PreviewsFoundation.framework/PreviewsFoundation](DYLIBS/PreviewsFoundation.md)
- [/System/Library/PrivateFrameworks/PreviewsInjection.framework/PreviewsInjection](DYLIBS/PreviewsInjection.md)
- [/System/Library/PrivateFrameworks/PreviewsMessaging.framework/PreviewsMessaging](DYLIBS/PreviewsMessaging.md)
- [/System/Library/PrivateFrameworks/PreviewsOSSupport.framework/PreviewsOSSupport](DYLIBS/PreviewsOSSupport.md)
- [/System/Library/PrivateFrameworks/PreviewsOSSupportUI.framework/PreviewsOSSupportUI](DYLIBS/PreviewsOSSupportUI.md)
- [/System/Library/PrivateFrameworks/PreviewsServices.framework/PreviewsServices](DYLIBS/PreviewsServices.md)
- [/System/Library/PrivateFrameworks/PreviewsServicesUI.framework/PreviewsServicesUI](DYLIBS/PreviewsServicesUI.md)
- [/System/Library/PrivateFrameworks/PridePoster.framework/PridePoster](DYLIBS/PridePoster.md)
- [/System/Library/PrivateFrameworks/PrintKit.framework/PrintKit](DYLIBS/PrintKit.md)
- [/System/Library/PrivateFrameworks/PrintKitUI.framework/PrintKitUI](DYLIBS/PrintKitUI.md)
- [/System/Library/PrivateFrameworks/PrivacyAccounting.framework/PrivacyAccounting](DYLIBS/PrivacyAccounting.md)
- [/System/Library/PrivateFrameworks/PrivacyDisclosureCore.framework/PrivacyDisclosureCore](DYLIBS/PrivacyDisclosureCore.md)
- [/System/Library/PrivateFrameworks/PrivacyDisclosureUI.framework/PrivacyDisclosureUI](DYLIBS/PrivacyDisclosureUI.md)
- [/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PrivateFederatedLearning](DYLIBS/PrivateFederatedLearning.md)
- [/System/Library/PrivateFrameworks/PrivateSearchClient.framework/PrivateSearchClient](DYLIBS/PrivateSearchClient.md)
- [/System/Library/PrivateFrameworks/PrivateSearchCore.framework/PrivateSearchCore](DYLIBS/PrivateSearchCore.md)
- [/System/Library/PrivateFrameworks/PrivateSearchProtocols.framework/PrivateSearchProtocols](DYLIBS/PrivateSearchProtocols.md)
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
- [/System/Library/PrivateFrameworks/ProactiveShareSheetDataHarvestingLighthouse.framework/ProactiveShareSheetDataHarvestingLighthouse](DYLIBS/ProactiveShareSheetDataHarvestingLighthouse.md)
- [/System/Library/PrivateFrameworks/ProactiveSuggestionClientModel.framework/ProactiveSuggestionClientModel](DYLIBS/ProactiveSuggestionClientModel.md)
- [/System/Library/PrivateFrameworks/ProactiveSupport.framework/ProactiveSupport](DYLIBS/ProactiveSupport.md)
- [/System/Library/PrivateFrameworks/ProactiveSupportStubs.framework/ProactiveSupportStubs](DYLIBS/ProactiveSupportStubs.md)
- [/System/Library/PrivateFrameworks/ProductKit.framework/ProductKit](DYLIBS/ProductKit.md)
- [/System/Library/PrivateFrameworks/ProfileValidatedAppIdentity.framework/ProfileValidatedAppIdentity](DYLIBS/ProfileValidatedAppIdentity.md)
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
- [/System/Library/PrivateFrameworks/ProxCardKit.framework/ProxCardKit](DYLIBS/ProxCardKit.md)
- [/System/Library/PrivateFrameworks/Proximity.framework/Proximity](DYLIBS/Proximity.md)
- [/System/Library/PrivateFrameworks/ProximityAppleIDSetup.framework/ProximityAppleIDSetup](DYLIBS/ProximityAppleIDSetup.md)
- [/System/Library/PrivateFrameworks/ProximityAppleIDSetupUI.framework/ProximityAppleIDSetupUI](DYLIBS/ProximityAppleIDSetupUI.md)
- [/System/Library/PrivateFrameworks/ProximityControl.framework/ProximityControl](DYLIBS/ProximityControl.md)
- [/System/Library/PrivateFrameworks/ProximityUI.framework/ProximityUI](DYLIBS/ProximityUI.md)
- [/System/Library/PrivateFrameworks/QLCharts.framework/QLCharts](DYLIBS/QLCharts.md)
- [/System/Library/PrivateFrameworks/QOSToolkit.framework/QOSToolkit](DYLIBS/QOSToolkit.md)
- [/System/Library/PrivateFrameworks/Quagga.framework/Quagga](DYLIBS/Quagga.md)
- [/System/Library/PrivateFrameworks/QueryParser.framework/QueryParser](DYLIBS/QueryParser.md)
- [/System/Library/PrivateFrameworks/QueryUnderstanding.framework/QueryUnderstanding](DYLIBS/QueryUnderstanding.md)
- [/System/Library/PrivateFrameworks/QuickLookSupport.framework/QuickLookSupport](DYLIBS/QuickLookSupport.md)
- [/System/Library/PrivateFrameworks/QuickLookThumbnailGeneration.framework/QuickLookThumbnailGeneration](DYLIBS/QuickLookThumbnailGeneration.md)
- [/System/Library/PrivateFrameworks/QuickLookThumbnailingDaemon.framework/QuickLookThumbnailingDaemon](DYLIBS/QuickLookThumbnailingDaemon.md)
- [/System/Library/PrivateFrameworks/QuickLookUICore.framework/QuickLookUICore](DYLIBS/QuickLookUICore.md)
- [/System/Library/PrivateFrameworks/RESync.framework/RESync](DYLIBS/RESync.md)
- [/System/Library/PrivateFrameworks/RTBuddyCrashlogDecoder.framework/RTBuddyCrashlogDecoder](DYLIBS/RTBuddyCrashlogDecoder.md)
- [/System/Library/PrivateFrameworks/RTCReporting.framework/RTCReporting](DYLIBS/RTCReporting.md)
- [/System/Library/PrivateFrameworks/RTTUI.framework/RTTUI](DYLIBS/RTTUI.md)
- [/System/Library/PrivateFrameworks/RTTUtilities.framework/RTTUtilities](DYLIBS/RTTUtilities.md)
- [/System/Library/PrivateFrameworks/Radio.framework/Radio](DYLIBS/Radio.md)
- [/System/Library/PrivateFrameworks/Rapport.framework/Rapport](DYLIBS/Rapport.md)
- [/System/Library/PrivateFrameworks/RapportUI.framework/RapportUI](DYLIBS/RapportUI.md)
- [/System/Library/PrivateFrameworks/RealityCamera.framework/AirPlayPlugin.rcplugin](DYLIBS/AirPlayPlugin.rcplugin.md)
- [/System/Library/PrivateFrameworks/RealityFusion.framework/RealityFusion](DYLIBS/RealityFusion.md)
- [/System/Library/PrivateFrameworks/RealityIO.framework/RealityIO](DYLIBS/RealityIO.md)
- [/System/Library/PrivateFrameworks/Recap.framework/Recap](DYLIBS/Recap.md)
- [/System/Library/PrivateFrameworks/RecapPerformanceTesting.framework/RecapPerformanceTesting](DYLIBS/RecapPerformanceTesting.md)
- [/System/Library/PrivateFrameworks/Recon3D.framework/Recon3D](DYLIBS/Recon3D.md)
- [/System/Library/PrivateFrameworks/ReflectionInternal.framework/ReflectionInternal](DYLIBS/ReflectionInternal.md)
- [/System/Library/PrivateFrameworks/RegulatoryDomain.framework/RegulatoryDomain](DYLIBS/RegulatoryDomain.md)
- [/System/Library/PrivateFrameworks/RelativeMotion.framework/RelativeMotion](DYLIBS/RelativeMotion.md)
- [/System/Library/PrivateFrameworks/RelevanceEngine.framework/RelevanceEngine](DYLIBS/RelevanceEngine.md)
- [/System/Library/PrivateFrameworks/RelevanceEngineUI.framework/RelevanceEngineUI](DYLIBS/RelevanceEngineUI.md)
- [/System/Library/PrivateFrameworks/ReminderKit.framework/ReminderKit](DYLIBS/ReminderKit.md)
- [/System/Library/PrivateFrameworks/ReminderKitInternal.framework/ReminderKitInternal](DYLIBS/ReminderKitInternal.md)
- [/System/Library/PrivateFrameworks/ReminderKitUI.framework/ReminderKitUI](DYLIBS/ReminderKitUI.md)
- [/System/Library/PrivateFrameworks/RemindersUICore.framework/RemindersUICore](DYLIBS/RemindersUICore.md)
- [/System/Library/PrivateFrameworks/RemoteConfiguration.framework/RemoteConfiguration](DYLIBS/RemoteConfiguration.md)
- [/System/Library/PrivateFrameworks/RemoteCoreML.framework/RemoteCoreML](DYLIBS/RemoteCoreML.md)
- [/System/Library/PrivateFrameworks/RemoteHID.framework/RemoteHID](DYLIBS/RemoteHID.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/RemoteManagement](DYLIBS/RemoteManagement.md)
- [/System/Library/PrivateFrameworks/RemoteManagementModel.framework/RemoteManagementModel](DYLIBS/RemoteManagementModel.md)
- [/System/Library/PrivateFrameworks/RemoteManagementProtocol.framework/RemoteManagementProtocol](DYLIBS/RemoteManagementProtocol.md)
- [/System/Library/PrivateFrameworks/RemoteManagementStore.framework/RemoteManagementStore](DYLIBS/RemoteManagementStore.md)
- [/System/Library/PrivateFrameworks/RemoteManagementUI.framework/RemoteManagementUI](DYLIBS/RemoteManagementUI.md)
- [/System/Library/PrivateFrameworks/RemoteMediaServices.framework/RemoteMediaServices](DYLIBS/RemoteMediaServices.md)
- [/System/Library/PrivateFrameworks/RemotePairingDevice.framework/RemotePairingDevice](DYLIBS/RemotePairingDevice.md)
- [/System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/RemoteServiceDiscovery](DYLIBS/RemoteServiceDiscovery.md)
- [/System/Library/PrivateFrameworks/RemoteStateDumpKit.framework/RemoteStateDumpKit](DYLIBS/RemoteStateDumpKit.md)
- [/System/Library/PrivateFrameworks/RemoteTextInput.framework/RemoteTextInput](DYLIBS/RemoteTextInput.md)
- [/System/Library/PrivateFrameworks/RemoteUI.framework/RemoteUI](DYLIBS/RemoteUI.md)
- [/System/Library/PrivateFrameworks/RemoteXPC.framework/RemoteXPC](DYLIBS/RemoteXPC.md)
- [/System/Library/PrivateFrameworks/RenderBox.framework/RenderBox](DYLIBS/RenderBox.md)
- [/System/Library/PrivateFrameworks/ReportingPlugin.framework/ReportingPlugin](DYLIBS/ReportingPlugin.md)
- [/System/Library/PrivateFrameworks/RequestDispatcherBridges.framework/RequestDispatcherBridges](DYLIBS/RequestDispatcherBridges.md)
- [/System/Library/PrivateFrameworks/RespiratoryHealth.framework/RespiratoryHealth](DYLIBS/RespiratoryHealth.md)
- [/System/Library/PrivateFrameworks/RespiratoryHealthDaemon.framework/RespiratoryHealthDaemon](DYLIBS/RespiratoryHealthDaemon.md)
- [/System/Library/PrivateFrameworks/RespiratoryHealthUI.framework/RespiratoryHealthUI](DYLIBS/RespiratoryHealthUI.md)
- [/System/Library/PrivateFrameworks/ResponseKit.framework/ResponseKit](DYLIBS/ResponseKit.md)
- [/System/Library/PrivateFrameworks/RevealCore.framework/RevealCore](DYLIBS/RevealCore.md)
- [/System/Library/PrivateFrameworks/RoomScanCore.framework/RoomScanCore](DYLIBS/RoomScanCore.md)
- [/System/Library/PrivateFrameworks/RunningBoard.framework/RunningBoard](DYLIBS/RunningBoard.md)
- [/System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices](DYLIBS/RunningBoardServices.md)
- [/System/Library/PrivateFrameworks/RuntimeInternal.framework/RuntimeInternal](DYLIBS/RuntimeInternal.md)
- [/System/Library/PrivateFrameworks/SAML.framework/SAML](DYLIBS/SAML.md)
- [/System/Library/PrivateFrameworks/SAObjects.framework/SAObjects](DYLIBS/SAObjects.md)
- [/System/Library/PrivateFrameworks/SDAPI.framework/SDAPI](DYLIBS/SDAPI.md)
- [/System/Library/PrivateFrameworks/SEService.framework/SEService](DYLIBS/SEService.md)
- [/System/Library/PrivateFrameworks/SFSymbols.framework/SFSymbols](DYLIBS/SFSymbols.md)
- [/System/Library/PrivateFrameworks/SIMSetupSupport.framework/SIMSetupSupport](DYLIBS/SIMSetupSupport.md)
- [/System/Library/PrivateFrameworks/SIMToolkitUI.framework/SIMToolkitUI](DYLIBS/SIMToolkitUI.md)
- [/System/Library/PrivateFrameworks/SMBClientEngine.framework/SMBClientEngine](DYLIBS/SMBClientEngine.md)
- [/System/Library/PrivateFrameworks/SMBClientProvider.framework/SMBClientProvider](DYLIBS/SMBClientProvider.md)
- [/System/Library/PrivateFrameworks/SMBSearch.framework/SMBSearch](DYLIBS/SMBSearch.md)
- [/System/Library/PrivateFrameworks/SOS.framework/SOS](DYLIBS/SOS.md)
- [/System/Library/PrivateFrameworks/SOSUI.framework/SOSUI](DYLIBS/SOSUI.md)
- [/System/Library/PrivateFrameworks/SPFinder.framework/SPFinder](DYLIBS/SPFinder.md)
- [/System/Library/PrivateFrameworks/SPOwner.framework/SPOwner](DYLIBS/SPOwner.md)
- [/System/Library/PrivateFrameworks/SPShared.framework/SPShared](DYLIBS/SPShared.md)
- [/System/Library/PrivateFrameworks/STSXPCHelperClient.framework/STSXPCHelperClient](DYLIBS/STSXPCHelperClient.md)
- [/System/Library/PrivateFrameworks/SafariCore.framework/SafariCore](DYLIBS/SafariCore.md)
- [/System/Library/PrivateFrameworks/SafariFoundation.framework/SafariFoundation](DYLIBS/SafariFoundation.md)
- [/System/Library/PrivateFrameworks/SafariSafeBrowsing.framework/SafariSafeBrowsing](DYLIBS/SafariSafeBrowsing.md)
- [/System/Library/PrivateFrameworks/SafariShared.framework/SafariShared](DYLIBS/SafariShared.md)
- [/System/Library/PrivateFrameworks/SafariSharedUI.framework/SafariSharedUI](DYLIBS/SafariSharedUI.md)
- [/System/Library/PrivateFrameworks/SafetyAlerts.framework/SafetyAlerts](DYLIBS/SafetyAlerts.md)
- [/System/Library/PrivateFrameworks/SafetyMonitor.framework/SafetyMonitor](DYLIBS/SafetyMonitor.md)
- [/System/Library/PrivateFrameworks/SafetyMonitorUI.framework/SafetyMonitorUI](DYLIBS/SafetyMonitorUI.md)
- [/System/Library/PrivateFrameworks/SampleAnalysis.framework/SampleAnalysis](DYLIBS/SampleAnalysis.md)
- [/System/Library/PrivateFrameworks/SavageCameraInterface.framework/SavageCameraInterface](DYLIBS/SavageCameraInterface.md)
- [/System/Library/PrivateFrameworks/SceneIntelligence.framework/SceneIntelligence](DYLIBS/SceneIntelligence.md)
- [/System/Library/PrivateFrameworks/SchoolTime.framework/SchoolTime](DYLIBS/SchoolTime.md)
- [/System/Library/PrivateFrameworks/SchoolTimeSettingsUI.framework/SchoolTimeSettingsUI](DYLIBS/SchoolTimeSettingsUI.md)
- [/System/Library/PrivateFrameworks/ScreenReaderBrailleDriver.framework/ScreenReaderBrailleDriver](DYLIBS/ScreenReaderBrailleDriver.md)
- [/System/Library/PrivateFrameworks/ScreenReaderCore.framework/ScreenReaderCore](DYLIBS/ScreenReaderCore.md)
- [/System/Library/PrivateFrameworks/ScreenReaderOutput.framework/ScreenReaderOutput](DYLIBS/ScreenReaderOutput.md)
- [/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore](DYLIBS/ScreenTimeCore.md)
- [/System/Library/PrivateFrameworks/ScreenTimeSettingsUI.framework/ScreenTimeSettingsUI](DYLIBS/ScreenTimeSettingsUI.md)
- [/System/Library/PrivateFrameworks/ScreenTimeSwift.framework/ScreenTimeSwift](DYLIBS/ScreenTimeSwift.md)
- [/System/Library/PrivateFrameworks/ScreenTimeUI.framework/ScreenTimeUI](DYLIBS/ScreenTimeUI.md)
- [/System/Library/PrivateFrameworks/ScreenTimeUICore.framework/ScreenTimeUICore](DYLIBS/ScreenTimeUICore.md)
- [/System/Library/PrivateFrameworks/ScreenshotServices.framework/ScreenshotServices](DYLIBS/ScreenshotServices.md)
- [/System/Library/PrivateFrameworks/Search.framework/Search](DYLIBS/Search.md)
- [/System/Library/PrivateFrameworks/SearchAds.framework/SearchAds](DYLIBS/SearchAds.md)
- [/System/Library/PrivateFrameworks/SearchFoundation.framework/SearchFoundation](DYLIBS/SearchFoundation.md)
- [/System/Library/PrivateFrameworks/SearchToShareCore.framework/SearchToShareCore](DYLIBS/SearchToShareCore.md)
- [/System/Library/PrivateFrameworks/SearchUI.framework/SearchUI](DYLIBS/SearchUI.md)
- [/System/Library/PrivateFrameworks/SearchUICardKitProviderSupport.framework/SearchUICardKitProviderSupport](DYLIBS/SearchUICardKitProviderSupport.md)
- [/System/Library/PrivateFrameworks/SecureChannel.framework/SecureChannel](DYLIBS/SecureChannel.md)
- [/System/Library/PrivateFrameworks/SecureTransactionService.framework/SecureTransactionService](DYLIBS/SecureTransactionService.md)
- [/System/Library/PrivateFrameworks/SecurityFoundation.framework/SecurityFoundation](DYLIBS/SecurityFoundation.md)
- [/System/Library/PrivateFrameworks/Seeding.framework/Seeding](DYLIBS/Seeding.md)
- [/System/Library/PrivateFrameworks/SensingAlgsService.framework/SensingAlgsService](DYLIBS/SensingAlgsService.md)
- [/System/Library/PrivateFrameworks/SensitiveContentAnalysisML.framework/SensitiveContentAnalysisML](DYLIBS/SensitiveContentAnalysisML.md)
- [/System/Library/PrivateFrameworks/SensitiveContentAnalysisUI.framework/SensitiveContentAnalysisUI](DYLIBS/SensitiveContentAnalysisUI.md)
- [/System/Library/PrivateFrameworks/SensorKitHelper.framework/SensorKitHelper](DYLIBS/SensorKitHelper.md)
- [/System/Library/PrivateFrameworks/SensorKitSupport.framework/SensorKitSupport](DYLIBS/SensorKitSupport.md)
- [/System/Library/PrivateFrameworks/SensorKitUI.framework/SensorKitUI](DYLIBS/SensorKitUI.md)
- [/System/Library/PrivateFrameworks/SentencePiece.framework/SentencePiece](DYLIBS/SentencePiece.md)
- [/System/Library/PrivateFrameworks/Sentry.framework/Sentry](DYLIBS/Sentry.md)
- [/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts](DYLIBS/SeparationAlerts.md)
- [/System/Library/PrivateFrameworks/ServiceManagement.framework/ServiceManagement](DYLIBS/ServiceManagement.md)
- [/System/Library/PrivateFrameworks/SessionAlert.framework/SessionAlert](DYLIBS/SessionAlert.md)
- [/System/Library/PrivateFrameworks/SessionAssertion.framework/SessionAssertion](DYLIBS/SessionAssertion.md)
- [/System/Library/PrivateFrameworks/SessionCore.framework/SessionCore](DYLIBS/SessionCore.md)
- [/System/Library/PrivateFrameworks/SessionFoundation.framework/SessionFoundation](DYLIBS/SessionFoundation.md)
- [/System/Library/PrivateFrameworks/SessionPushNotifications.framework/SessionPushNotifications](DYLIBS/SessionPushNotifications.md)
- [/System/Library/PrivateFrameworks/SessionSQL.framework/SessionSQL](DYLIBS/SessionSQL.md)
- [/System/Library/PrivateFrameworks/SessionSyncEngine.framework/SessionSyncEngine](DYLIBS/SessionSyncEngine.md)
- [/System/Library/PrivateFrameworks/Settings.framework/Settings](DYLIBS/Settings.md)
- [/System/Library/PrivateFrameworks/Settings/DisplayAndBrightnessSettings.framework/DisplayAndBrightnessSettings](DYLIBS/DisplayAndBrightnessSettings.md)
- [/System/Library/PrivateFrameworks/Settings/GeneralSettingsUI.framework/GeneralSettingsUI](DYLIBS/GeneralSettingsUI.md)
- [/System/Library/PrivateFrameworks/Settings/LegalAndRegulatorySettingsPrivate.framework/LegalAndRegulatorySettingsPrivate](DYLIBS/LegalAndRegulatorySettingsPrivate.md)
- [/System/Library/PrivateFrameworks/Settings/PrivacySettingsUI.framework/PrivacySettingsUI](DYLIBS/PrivacySettingsUI.md)
- [/System/Library/PrivateFrameworks/Settings/SettingsUIKitPrivate.framework/SettingsUIKitPrivate](DYLIBS/SettingsUIKitPrivate.md)
- [/System/Library/PrivateFrameworks/Settings/SoundsAndHapticsSettings.framework/SoundsAndHapticsSettings](DYLIBS/SoundsAndHapticsSettings.md)
- [/System/Library/PrivateFrameworks/SettingsCellular.framework/SettingsCellular](DYLIBS/SettingsCellular.md)
- [/System/Library/PrivateFrameworks/SettingsCellularUI.framework/SettingsCellularUI](DYLIBS/SettingsCellularUI.md)
- [/System/Library/PrivateFrameworks/SettingsFoundation.framework/SettingsFoundation](DYLIBS/SettingsFoundation.md)
- [/System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant](DYLIBS/SetupAssistant.md)
- [/System/Library/PrivateFrameworks/SetupAssistantSupport.framework/SetupAssistantSupport](DYLIBS/SetupAssistantSupport.md)
- [/System/Library/PrivateFrameworks/SetupAssistantSupportUI.framework/SetupAssistantSupportUI](DYLIBS/SetupAssistantSupportUI.md)
- [/System/Library/PrivateFrameworks/SetupAssistantUI.framework/SetupAssistantUI](DYLIBS/SetupAssistantUI.md)
- [/System/Library/PrivateFrameworks/SetupKit.framework/SetupKit](DYLIBS/SetupKit.md)
- [/System/Library/PrivateFrameworks/SeymourClient.framework/SeymourClient](DYLIBS/SeymourClient.md)
- [/System/Library/PrivateFrameworks/SeymourCore.framework/SeymourCore](DYLIBS/SeymourCore.md)
- [/System/Library/PrivateFrameworks/SeymourMedia.framework/SeymourMedia](DYLIBS/SeymourMedia.md)
- [/System/Library/PrivateFrameworks/SeymourServerProtocol.framework/SeymourServerProtocol](DYLIBS/SeymourServerProtocol.md)
- [/System/Library/PrivateFrameworks/SeymourServices.framework/SeymourServices](DYLIBS/SeymourServices.md)
- [/System/Library/PrivateFrameworks/SeymourUI.framework/SeymourUI](DYLIBS/SeymourUI.md)
- [/System/Library/PrivateFrameworks/ShareSheet.framework/ShareSheet](DYLIBS/ShareSheet.md)
- [/System/Library/PrivateFrameworks/SharedWebCredentials.framework/SharedWebCredentials](DYLIBS/SharedWebCredentials.md)
- [/System/Library/PrivateFrameworks/Sharing.framework/Sharing](DYLIBS/Sharing.md)
- [/System/Library/PrivateFrameworks/SharingHUD.framework/SharingHUD](DYLIBS/SharingHUD.md)
- [/System/Library/PrivateFrameworks/SharingUI.framework/SharingUI](DYLIBS/SharingUI.md)
- [/System/Library/PrivateFrameworks/SharingXPCServices.framework/SharingXPCServices](DYLIBS/SharingXPCServices.md)
- [/System/Library/PrivateFrameworks/ShazamCore.framework/ShazamCore](DYLIBS/ShazamCore.md)
- [/System/Library/PrivateFrameworks/ShazamEvents.framework/ShazamEvents](DYLIBS/ShazamEvents.md)
- [/System/Library/PrivateFrameworks/ShazamInsights.framework/ShazamInsights](DYLIBS/ShazamInsights.md)
- [/System/Library/PrivateFrameworks/ShazamKitUI.framework/ShazamKitUI](DYLIBS/ShazamKitUI.md)
- [/System/Library/PrivateFrameworks/ShortcutUIKit.framework/ShortcutUIKit](DYLIBS/ShortcutUIKit.md)
- [/System/Library/PrivateFrameworks/SidecarCore.framework/SidecarCore](DYLIBS/SidecarCore.md)
- [/System/Library/PrivateFrameworks/SidecarUI.framework/SidecarUI](DYLIBS/SidecarUI.md)
- [/System/Library/PrivateFrameworks/SignalCompression.framework/SignalCompression](DYLIBS/SignalCompression.md)
- [/System/Library/PrivateFrameworks/SignpostCollection.framework/SignpostCollection](DYLIBS/SignpostCollection.md)
- [/System/Library/PrivateFrameworks/SignpostMetrics.framework/SignpostMetrics](DYLIBS/SignpostMetrics.md)
- [/System/Library/PrivateFrameworks/SignpostNotification.framework/SignpostNotification](DYLIBS/SignpostNotification.md)
- [/System/Library/PrivateFrameworks/SignpostSupport.framework/SignpostSupport](DYLIBS/SignpostSupport.md)
- [/System/Library/PrivateFrameworks/Silex.framework/Silex](DYLIBS/Silex.md)
- [/System/Library/PrivateFrameworks/SilexVideo.framework/SilexVideo](DYLIBS/SilexVideo.md)
- [/System/Library/PrivateFrameworks/SilexWeb.framework/SilexWeb](DYLIBS/SilexWeb.md)
- [/System/Library/PrivateFrameworks/SiriActivation.framework/SiriActivation](DYLIBS/SiriActivation.md)
- [/System/Library/PrivateFrameworks/SiriActivationFoundation.framework/SiriActivationFoundation](DYLIBS/SiriActivationFoundation.md)
- [/System/Library/PrivateFrameworks/SiriAnalytics.framework/SiriAnalytics](DYLIBS/SiriAnalytics.md)
- [/System/Library/PrivateFrameworks/SiriAppLaunchIntents.framework/SiriAppLaunchIntents](DYLIBS/SiriAppLaunchIntents.md)
- [/System/Library/PrivateFrameworks/SiriAppResolution.framework/SiriAppResolution](DYLIBS/SiriAppResolution.md)
- [/System/Library/PrivateFrameworks/SiriAudioIntentUtils.framework/SiriAudioIntentUtils](DYLIBS/SiriAudioIntentUtils.md)
- [/System/Library/PrivateFrameworks/SiriAudioInternal.framework/SiriAudioInternal](DYLIBS/SiriAudioInternal.md)
- [/System/Library/PrivateFrameworks/SiriAudioSnippetKit.framework/SiriAudioSnippetKit](DYLIBS/SiriAudioSnippetKit.md)
- [/System/Library/PrivateFrameworks/SiriAudioSnippetUI.framework/SiriAudioSnippetUI](DYLIBS/SiriAudioSnippetUI.md)
- [/System/Library/PrivateFrameworks/SiriAudioSupport.framework/SiriAudioSupport](DYLIBS/SiriAudioSupport.md)
- [/System/Library/PrivateFrameworks/SiriBaseTypes.framework/SiriBaseTypes](DYLIBS/SiriBaseTypes.md)
- [/System/Library/PrivateFrameworks/SiriCalendarIntents.framework/SiriCalendarIntents](DYLIBS/SiriCalendarIntents.md)
- [/System/Library/PrivateFrameworks/SiriCam.framework/SiriCam](DYLIBS/SiriCam.md)
- [/System/Library/PrivateFrameworks/SiriCarCommandsIntents.framework/SiriCarCommandsIntents](DYLIBS/SiriCarCommandsIntents.md)
- [/System/Library/PrivateFrameworks/SiriContactsIntents.framework/SiriContactsIntents](DYLIBS/SiriContactsIntents.md)
- [/System/Library/PrivateFrameworks/SiriCore.framework/SiriCore](DYLIBS/SiriCore.md)
- [/System/Library/PrivateFrameworks/SiriCoreMetrics.framework/SiriCoreMetrics](DYLIBS/SiriCoreMetrics.md)
- [/System/Library/PrivateFrameworks/SiriCorrections.framework/SiriCorrections](DYLIBS/SiriCorrections.md)
- [/System/Library/PrivateFrameworks/SiriCrossDeviceArbitration.framework/SiriCrossDeviceArbitration](DYLIBS/SiriCrossDeviceArbitration.md)
- [/System/Library/PrivateFrameworks/SiriCrossDeviceArbitrationFeedback.framework/SiriCrossDeviceArbitrationFeedback](DYLIBS/SiriCrossDeviceArbitrationFeedback.md)
- [/System/Library/PrivateFrameworks/SiriDailyBriefingInternal.framework/SiriDailyBriefingInternal](DYLIBS/SiriDailyBriefingInternal.md)
- [/System/Library/PrivateFrameworks/SiriDialogEngine.framework/SiriDialogEngine](DYLIBS/SiriDialogEngine.md)
- [/System/Library/PrivateFrameworks/SiriEmergencyIntents.framework/SiriEmergencyIntents](DYLIBS/SiriEmergencyIntents.md)
- [/System/Library/PrivateFrameworks/SiriExpanseInternal.framework/SiriExpanseInternal](DYLIBS/SiriExpanseInternal.md)
- [/System/Library/PrivateFrameworks/SiriExpanseInternalUI.framework/SiriExpanseInternalUI](DYLIBS/SiriExpanseInternalUI.md)
- [/System/Library/PrivateFrameworks/SiriFindMy.framework/SiriFindMy](DYLIBS/SiriFindMy.md)
- [/System/Library/PrivateFrameworks/SiriFlowEnvironment.framework/SiriFlowEnvironment](DYLIBS/SiriFlowEnvironment.md)
- [/System/Library/PrivateFrameworks/SiriGeo.framework/SiriGeo](DYLIBS/SiriGeo.md)
- [/System/Library/PrivateFrameworks/SiriHomeAccessoryFramework.framework/SiriHomeAccessoryFramework](DYLIBS/SiriHomeAccessoryFramework.md)
- [/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/SiriIdentityInternal](DYLIBS/SiriIdentityInternal.md)
- [/System/Library/PrivateFrameworks/SiriInCall.framework/SiriInCall](DYLIBS/SiriInCall.md)
- [/System/Library/PrivateFrameworks/SiriInference.framework/SiriInference](DYLIBS/SiriInference.md)
- [/System/Library/PrivateFrameworks/SiriInferenceFlow.framework/SiriInferenceFlow](DYLIBS/SiriInferenceFlow.md)
- [/System/Library/PrivateFrameworks/SiriInferenceIntents.framework/SiriInferenceIntents](DYLIBS/SiriInferenceIntents.md)
- [/System/Library/PrivateFrameworks/SiriInferredHelpfulness.framework/SiriInferredHelpfulness](DYLIBS/SiriInferredHelpfulness.md)
- [/System/Library/PrivateFrameworks/SiriInformationSearch.framework/SiriInformationSearch](DYLIBS/SiriInformationSearch.md)
- [/System/Library/PrivateFrameworks/SiriInformationTypes.framework/SiriInformationTypes](DYLIBS/SiriInformationTypes.md)
- [/System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation](DYLIBS/SiriInstrumentation.md)
- [/System/Library/PrivateFrameworks/SiriIntentEvents.framework/SiriIntentEvents](DYLIBS/SiriIntentEvents.md)
- [/System/Library/PrivateFrameworks/SiriInteractive.framework/SiriInteractive](DYLIBS/SiriInteractive.md)
- [/System/Library/PrivateFrameworks/SiriInvocationAnalytics.framework/SiriInvocationAnalytics](DYLIBS/SiriInvocationAnalytics.md)
- [/System/Library/PrivateFrameworks/SiriKitFlow.framework/SiriKitFlow](DYLIBS/SiriKitFlow.md)
- [/System/Library/PrivateFrameworks/SiriKitInvocation.framework/SiriKitInvocation](DYLIBS/SiriKitInvocation.md)
- [/System/Library/PrivateFrameworks/SiriKitRuntime.framework/SiriKitRuntime](DYLIBS/SiriKitRuntime.md)
- [/System/Library/PrivateFrameworks/SiriLiminal.framework/SiriLiminal](DYLIBS/SiriLiminal.md)
- [/System/Library/PrivateFrameworks/SiriMailInternal.framework/SiriMailInternal](DYLIBS/SiriMailInternal.md)
- [/System/Library/PrivateFrameworks/SiriMailUI.framework/SiriMailUI](DYLIBS/SiriMailUI.md)
- [/System/Library/PrivateFrameworks/SiriMessageBus.framework/SiriMessageBus](DYLIBS/SiriMessageBus.md)
- [/System/Library/PrivateFrameworks/SiriMessageTypes.framework/SiriMessageTypes](DYLIBS/SiriMessageTypes.md)
- [/System/Library/PrivateFrameworks/SiriModes.framework/SiriModes](DYLIBS/SiriModes.md)
- [/System/Library/PrivateFrameworks/SiriNLUOverrides.framework/SiriNLUOverrides](DYLIBS/SiriNLUOverrides.md)
- [/System/Library/PrivateFrameworks/SiriNLUTypes.framework/SiriNLUTypes](DYLIBS/SiriNLUTypes.md)
- [/System/Library/PrivateFrameworks/SiriNaturalLanguageGeneration.framework/SiriNaturalLanguageGeneration](DYLIBS/SiriNaturalLanguageGeneration.md)
- [/System/Library/PrivateFrameworks/SiriNaturalLanguageParsing.framework/SiriNaturalLanguageParsing](DYLIBS/SiriNaturalLanguageParsing.md)
- [/System/Library/PrivateFrameworks/SiriNetwork.framework/SiriNetwork](DYLIBS/SiriNetwork.md)
- [/System/Library/PrivateFrameworks/SiriNotebook.framework/SiriNotebook](DYLIBS/SiriNotebook.md)
- [/System/Library/PrivateFrameworks/SiriNotificationsIntents.framework/SiriNotificationsIntents](DYLIBS/SiriNotificationsIntents.md)
- [/System/Library/PrivateFrameworks/SiriObservation.framework/SiriObservation](DYLIBS/SiriObservation.md)
- [/System/Library/PrivateFrameworks/SiriOntology.framework/SiriOntology](DYLIBS/SiriOntology.md)
- [/System/Library/PrivateFrameworks/SiriOntologyProtobuf.framework/SiriOntologyProtobuf](DYLIBS/SiriOntologyProtobuf.md)
- [/System/Library/PrivateFrameworks/SiriPaymentsIntents.framework/SiriPaymentsIntents](DYLIBS/SiriPaymentsIntents.md)
- [/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/SiriPlaybackControlIntents](DYLIBS/SiriPlaybackControlIntents.md)
- [/System/Library/PrivateFrameworks/SiriPlaybackControlSupport.framework/SiriPlaybackControlSupport](DYLIBS/SiriPlaybackControlSupport.md)
- [/System/Library/PrivateFrameworks/SiriPowerInstrumentation.framework/SiriPowerInstrumentation](DYLIBS/SiriPowerInstrumentation.md)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningAnalytics.framework/SiriPrivateLearningAnalytics](DYLIBS/SiriPrivateLearningAnalytics.md)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningInference.framework/SiriPrivateLearningInference](DYLIBS/SiriPrivateLearningInference.md)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningLogging.framework/SiriPrivateLearningLogging](DYLIBS/SiriPrivateLearningLogging.md)
- [/System/Library/PrivateFrameworks/SiriReaderIntents.framework/SiriReaderIntents](DYLIBS/SiriReaderIntents.md)
- [/System/Library/PrivateFrameworks/SiriReaderServices.framework/SiriReaderServices](DYLIBS/SiriReaderServices.md)
- [/System/Library/PrivateFrameworks/SiriReferenceResolution.framework/SiriReferenceResolution](DYLIBS/SiriReferenceResolution.md)
- [/System/Library/PrivateFrameworks/SiriReferenceResolutionDataModel.framework/SiriReferenceResolutionDataModel](DYLIBS/SiriReferenceResolutionDataModel.md)
- [/System/Library/PrivateFrameworks/SiriReferenceResolver.framework/SiriReferenceResolver](DYLIBS/SiriReferenceResolver.md)
- [/System/Library/PrivateFrameworks/SiriRemembers.framework/SiriRemembers](DYLIBS/SiriRemembers.md)
- [/System/Library/PrivateFrameworks/SiriRequestDispatcher.framework/SiriRequestDispatcher](DYLIBS/SiriRequestDispatcher.md)
- [/System/Library/PrivateFrameworks/SiriSettingsIntents.framework/SiriSettingsIntents](DYLIBS/SiriSettingsIntents.md)
- [/System/Library/PrivateFrameworks/SiriSetup.framework/SiriSetup](DYLIBS/SiriSetup.md)
- [/System/Library/PrivateFrameworks/SiriSharedUI.framework/SiriSharedUI](DYLIBS/SiriSharedUI.md)
- [/System/Library/PrivateFrameworks/SiriSignals.framework/SiriSignals](DYLIBS/SiriSignals.md)
- [/System/Library/PrivateFrameworks/SiriSocialConversation.framework/SiriSocialConversation](DYLIBS/SiriSocialConversation.md)
- [/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis](DYLIBS/SiriSpeechSynthesis.md)
- [/System/Library/PrivateFrameworks/SiriStates.framework/SiriStates](DYLIBS/SiriStates.md)
- [/System/Library/PrivateFrameworks/SiriSuggestions.framework/SiriSuggestions](DYLIBS/SiriSuggestions.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsAPI.framework/SiriSuggestionsAPI](DYLIBS/SiriSuggestionsAPI.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsIntelligence.framework/SiriSuggestionsIntelligence](DYLIBS/SiriSuggestionsIntelligence.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsKit.framework/SiriSuggestionsKit](DYLIBS/SiriSuggestionsKit.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsSupport.framework/SiriSuggestionsSupport](DYLIBS/SiriSuggestionsSupport.md)
- [/System/Library/PrivateFrameworks/SiriSystemCommandsIntents.framework/SiriSystemCommandsIntents](DYLIBS/SiriSystemCommandsIntents.md)
- [/System/Library/PrivateFrameworks/SiriTTS.framework/SiriTTS](DYLIBS/SiriTTS.md)
- [/System/Library/PrivateFrameworks/SiriTTSService.framework/SiriTTSService](DYLIBS/SiriTTSService.md)
- [/System/Library/PrivateFrameworks/SiriTaskEngagement.framework/SiriTaskEngagement](DYLIBS/SiriTaskEngagement.md)
- [/System/Library/PrivateFrameworks/SiriTasks.framework/SiriTasks](DYLIBS/SiriTasks.md)
- [/System/Library/PrivateFrameworks/SiriTasksEvaluation.framework/SiriTasksEvaluation](DYLIBS/SiriTasksEvaluation.md)
- [/System/Library/PrivateFrameworks/SiriTimeAlarmInternal.framework/SiriTimeAlarmInternal](DYLIBS/SiriTimeAlarmInternal.md)
- [/System/Library/PrivateFrameworks/SiriTimeInternal.framework/SiriTimeInternal](DYLIBS/SiriTimeInternal.md)
- [/System/Library/PrivateFrameworks/SiriTimeTimerInternal.framework/SiriTimeTimerInternal](DYLIBS/SiriTimeTimerInternal.md)
- [/System/Library/PrivateFrameworks/SiriTranslationIntents.framework/SiriTranslationIntents](DYLIBS/SiriTranslationIntents.md)
- [/System/Library/PrivateFrameworks/SiriTurnTakingManager.framework/SiriTurnTakingManager](DYLIBS/SiriTurnTakingManager.md)
- [/System/Library/PrivateFrameworks/SiriUI.framework/SiriUI](DYLIBS/SiriUI.md)
- [/System/Library/PrivateFrameworks/SiriUIActivation.framework/SiriUIActivation](DYLIBS/SiriUIActivation.md)
- [/System/Library/PrivateFrameworks/SiriUIBridge.framework/SiriUIBridge](DYLIBS/SiriUIBridge.md)
- [/System/Library/PrivateFrameworks/SiriUICardKitProviderSupport.framework/SiriUICardKitProviderSupport](DYLIBS/SiriUICardKitProviderSupport.md)
- [/System/Library/PrivateFrameworks/SiriUICore.framework/SiriUICore](DYLIBS/SiriUICore.md)
- [/System/Library/PrivateFrameworks/SiriUIFoundation.framework/SiriUIFoundation](DYLIBS/SiriUIFoundation.md)
- [/System/Library/PrivateFrameworks/SiriUtilities.framework/SiriUtilities](DYLIBS/SiriUtilities.md)
- [/System/Library/PrivateFrameworks/SiriVOX.framework/SiriVOX](DYLIBS/SiriVOX.md)
- [/System/Library/PrivateFrameworks/SiriVideoIntents.framework/SiriVideoIntents](DYLIBS/SiriVideoIntents.md)
- [/System/Library/PrivateFrameworks/SiriVirtualDeviceResolution.framework/SiriVirtualDeviceResolution](DYLIBS/SiriVirtualDeviceResolution.md)
- [/System/Library/PrivateFrameworks/SiriWellnessIntents.framework/SiriWellnessIntents](DYLIBS/SiriWellnessIntents.md)
- [/System/Library/PrivateFrameworks/Sleep.framework/Sleep](DYLIBS/Sleep.md)
- [/System/Library/PrivateFrameworks/SleepDaemon.framework/SleepDaemon](DYLIBS/SleepDaemon.md)
- [/System/Library/PrivateFrameworks/SleepHealth.framework/SleepHealth](DYLIBS/SleepHealth.md)
- [/System/Library/PrivateFrameworks/SleepHealthDaemon.framework/SleepHealthDaemon](DYLIBS/SleepHealthDaemon.md)
- [/System/Library/PrivateFrameworks/SleepHealthUI.framework/SleepHealthUI](DYLIBS/SleepHealthUI.md)
- [/System/Library/PrivateFrameworks/SleepWidgetUI.framework/SleepWidgetUI](DYLIBS/SleepWidgetUI.md)
- [/System/Library/PrivateFrameworks/SlideshowKit.framework/Frameworks/OpusFoundation.framework/OpusFoundation](DYLIBS/OpusFoundation.md)
- [/System/Library/PrivateFrameworks/SlideshowKit.framework/Frameworks/OpusKit.framework/OpusKit](DYLIBS/OpusKit.md)
- [/System/Library/PrivateFrameworks/SlideshowKit.framework/SlideshowKit](DYLIBS/SlideshowKit.md)
- [/System/Library/PrivateFrameworks/SmartReplies.framework/SmartReplies](DYLIBS/SmartReplies.md)
- [/System/Library/PrivateFrameworks/SmartRepliesServer.framework/SmartRepliesServer](DYLIBS/SmartRepliesServer.md)
- [/System/Library/PrivateFrameworks/SmartRepliesUI.framework/SmartRepliesUI](DYLIBS/SmartRepliesUI.md)
- [/System/Library/PrivateFrameworks/SnippetCommands.framework/SnippetCommands](DYLIBS/SnippetCommands.md)
- [/System/Library/PrivateFrameworks/SnippetKit.framework/SnippetKit](DYLIBS/SnippetKit.md)
- [/System/Library/PrivateFrameworks/SnippetUI.framework/SnippetUI](DYLIBS/SnippetUI.md)
- [/System/Library/PrivateFrameworks/SocialLayer.framework/SocialLayer](DYLIBS/SocialLayer.md)
- [/System/Library/PrivateFrameworks/SocialServices.framework/SocialServices](DYLIBS/SocialServices.md)
- [/System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking](DYLIBS/SoftLinking.md)
- [/System/Library/PrivateFrameworks/SoftPosReader.framework/SoftPosReader](DYLIBS/SoftPosReader.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateBridge.framework/SoftwareUpdateBridge](DYLIBS/SoftwareUpdateBridge.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateController.framework/SoftwareUpdateController](DYLIBS/SoftwareUpdateController.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/SoftwareUpdateCore](DYLIBS/SoftwareUpdateCore.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateCoreConnect.framework/SoftwareUpdateCoreConnect](DYLIBS/SoftwareUpdateCoreConnect.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport](DYLIBS/SoftwareUpdateCoreSupport.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices](DYLIBS/SoftwareUpdateServices.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateServicesUI.framework/SoftwareUpdateServicesUI](DYLIBS/SoftwareUpdateServicesUI.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateSettings.framework/SoftwareUpdateSettings](DYLIBS/SoftwareUpdateSettings.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateSettingsUI.framework/SoftwareUpdateSettingsUI](DYLIBS/SoftwareUpdateSettingsUI.md)
- [/System/Library/PrivateFrameworks/SoundAutoConfig.framework/SoundAutoConfig](DYLIBS/SoundAutoConfig.md)
- [/System/Library/PrivateFrameworks/SoundBoardServices.framework/SoundBoardServices](DYLIBS/SoundBoardServices.md)
- [/System/Library/PrivateFrameworks/SoundScapesUtility.framework/SoundScapesUtility](DYLIBS/SoundScapesUtility.md)
- [/System/Library/PrivateFrameworks/SpaceAttribution.framework/SpaceAttribution](DYLIBS/SpaceAttribution.md)
- [/System/Library/PrivateFrameworks/SpeakThisServices.framework/SpeakThisServices](DYLIBS/SpeakThisServices.md)
- [/System/Library/PrivateFrameworks/SpeakTypingServices.framework/SpeakTypingServices](DYLIBS/SpeakTypingServices.md)
- [/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition](DYLIBS/SpeakerRecognition.md)
- [/System/Library/PrivateFrameworks/SpeechDetector.framework/SpeechDetector](DYLIBS/SpeechDetector.md)
- [/System/Library/PrivateFrameworks/SpeechDictionary.framework/SpeechDictionary](DYLIBS/SpeechDictionary.md)
- [/System/Library/PrivateFrameworks/SpeechRecognitionCommandAndControl.framework/SpeechRecognitionCommandAndControl](DYLIBS/SpeechRecognitionCommandAndControl.md)
- [/System/Library/PrivateFrameworks/SpeechRecognitionCommandServices.framework/SpeechRecognitionCommandServices](DYLIBS/SpeechRecognitionCommandServices.md)
- [/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/SpeechRecognitionCore](DYLIBS/SpeechRecognitionCore.md)
- [/System/Library/PrivateFrameworks/SpeechRecognitionSharedSupport.framework/SpeechRecognitionSharedSupport](DYLIBS/SpeechRecognitionSharedSupport.md)
- [/System/Library/PrivateFrameworks/SplashBoard.framework/SplashBoard](DYLIBS/SplashBoard.md)
- [/System/Library/PrivateFrameworks/SportsKit.framework/SportsKit](DYLIBS/SportsKit.md)
- [/System/Library/PrivateFrameworks/Spotlight.framework/Spotlight](DYLIBS/Spotlight.md)
- [/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon](DYLIBS/SpotlightDaemon.md)
- [/System/Library/PrivateFrameworks/SpotlightFoundation.framework/SpotlightFoundation](DYLIBS/SpotlightFoundation.md)
- [/System/Library/PrivateFrameworks/SpotlightLinguistics.framework/SpotlightLinguistics](DYLIBS/SpotlightLinguistics.md)
- [/System/Library/PrivateFrameworks/SpotlightReceiver.framework/SpotlightReceiver](DYLIBS/SpotlightReceiver.md)
- [/System/Library/PrivateFrameworks/SpotlightRecommendation.framework/SpotlightRecommendation](DYLIBS/SpotlightRecommendation.md)
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
- [/System/Library/PrivateFrameworks/StateReplicator.framework/StateReplicator](DYLIBS/StateReplicator.md)
- [/System/Library/PrivateFrameworks/Stateful.framework/Stateful](DYLIBS/Stateful.md)
- [/System/Library/PrivateFrameworks/StatusKit.framework/StatusKit](DYLIBS/StatusKit.md)
- [/System/Library/PrivateFrameworks/StatusKitAgentCore.framework/StatusKitAgentCore](DYLIBS/StatusKitAgentCore.md)
- [/System/Library/PrivateFrameworks/Stickers.framework/Stickers](DYLIBS/Stickers.md)
- [/System/Library/PrivateFrameworks/StickersUI.framework/StickersUI](DYLIBS/StickersUI.md)
- [/System/Library/PrivateFrameworks/Stocks.framework/Stocks](DYLIBS/Stocks.md)
- [/System/Library/PrivateFrameworks/StocksAnalytics.framework/StocksAnalytics](DYLIBS/StocksAnalytics.md)
- [/System/Library/PrivateFrameworks/StocksCore.framework/StocksCore](DYLIBS/StocksCore.md)
- [/System/Library/PrivateFrameworks/StocksKit.framework/StocksKit](DYLIBS/StocksKit.md)
- [/System/Library/PrivateFrameworks/StocksUI.framework/StocksUI](DYLIBS/StocksUI.md)
- [/System/Library/PrivateFrameworks/StorageData.framework/StorageData](DYLIBS/StorageData.md)
- [/System/Library/PrivateFrameworks/StorageKit.framework/StorageKit](DYLIBS/StorageKit.md)
- [/System/Library/PrivateFrameworks/StorageSettings.framework/StorageSettings](DYLIBS/StorageSettings.md)
- [/System/Library/PrivateFrameworks/StorageUI.framework/StorageUI](DYLIBS/StorageUI.md)
- [/System/Library/PrivateFrameworks/StoreBookkeeper.framework/StoreBookkeeper](DYLIBS/StoreBookkeeper.md)
- [/System/Library/PrivateFrameworks/StoreBookkeeperClient.framework/StoreBookkeeperClient](DYLIBS/StoreBookkeeperClient.md)
- [/System/Library/PrivateFrameworks/StoreKitUI.framework/StoreKitUI](DYLIBS/StoreKitUI.md)
- [/System/Library/PrivateFrameworks/StoreServices.framework/StoreServices](DYLIBS/StoreServices.md)
- [/System/Library/PrivateFrameworks/StreamingExtractor.framework/StreamingExtractor](DYLIBS/StreamingExtractor.md)
- [/System/Library/PrivateFrameworks/StreamingZip.framework/StreamingZip](DYLIBS/StreamingZip.md)
- [/System/Library/PrivateFrameworks/StrokeAnimation.framework/StrokeAnimation](DYLIBS/StrokeAnimation.md)
- [/System/Library/PrivateFrameworks/StudyLog.framework/StudyLog](DYLIBS/StudyLog.md)
- [/System/Library/PrivateFrameworks/SuggestionsSpotlightMetrics.framework/SuggestionsSpotlightMetrics](DYLIBS/SuggestionsSpotlightMetrics.md)
- [/System/Library/PrivateFrameworks/SummariesHealthDaemon.framework/SummariesHealthDaemon](DYLIBS/SummariesHealthDaemon.md)
- [/System/Library/PrivateFrameworks/SwiftCertificate.framework/SwiftCertificate](DYLIBS/SwiftCertificate.md)
- [/System/Library/PrivateFrameworks/SwiftNN.framework/SwiftNN](DYLIBS/SwiftNN.md)
- [/System/Library/PrivateFrameworks/SwiftSQLite.framework/SwiftSQLite](DYLIBS/SwiftSQLite.md)
- [/System/Library/PrivateFrameworks/SwiftUIAccessibility.framework/SwiftUIAccessibility](DYLIBS/SwiftUIAccessibility.md)
- [/System/Library/PrivateFrameworks/Symbolication.framework/Symbolication](DYLIBS/Symbolication.md)
- [/System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter](DYLIBS/SymptomDiagnosticReporter.md)
- [/System/Library/PrivateFrameworks/SymptomReporter.framework/SymptomReporter](DYLIBS/SymptomReporter.md)
- [/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/ManagedEvent.framework/ManagedEvent](DYLIBS/ManagedEvent.md)
- [/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomAnalytics.framework/SymptomAnalytics](DYLIBS/SymptomAnalytics.md)
- [/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomEvaluator.framework/SymptomEvaluator](DYLIBS/SymptomEvaluator.md)
- [/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomNetworkUsage.framework/SymptomNetworkUsage](DYLIBS/SymptomNetworkUsage.md)
- [/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomPresentationFeed.framework/SymptomPresentationFeed](DYLIBS/SymptomPresentationFeed.md)
- [/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomPresentationLite.framework/SymptomPresentationLite](DYLIBS/SymptomPresentationLite.md)
- [/System/Library/PrivateFrameworks/Synapse.framework/Synapse](DYLIBS/Synapse.md)
- [/System/Library/PrivateFrameworks/SyncedDefaults.framework/SyncedDefaults](DYLIBS/SyncedDefaults.md)
- [/System/Library/PrivateFrameworks/SyncedModels.framework/SyncedModels](DYLIBS/SyncedModels.md)
- [/System/Library/PrivateFrameworks/SystemAperture.framework/SystemAperture](DYLIBS/SystemAperture.md)
- [/System/Library/PrivateFrameworks/SystemApertureUI.framework/SystemApertureUI](DYLIBS/SystemApertureUI.md)
- [/System/Library/PrivateFrameworks/SystemPaperPresentation.framework/SystemPaperPresentation](DYLIBS/SystemPaperPresentation.md)
- [/System/Library/PrivateFrameworks/SystemStatus.framework/SystemStatus](DYLIBS/SystemStatus.md)
- [/System/Library/PrivateFrameworks/SystemStatusServer.framework/SystemStatusServer](DYLIBS/SystemStatusServer.md)
- [/System/Library/PrivateFrameworks/SystemStatusUI.framework/SystemStatusUI](DYLIBS/SystemStatusUI.md)
- [/System/Library/PrivateFrameworks/SystemWake.framework/SystemWake](DYLIBS/SystemWake.md)
- [/System/Library/PrivateFrameworks/TCC.framework/TCC](DYLIBS/TCC.md)
- [/System/Library/PrivateFrameworks/TDGSharing.framework/TDGSharing](DYLIBS/TDGSharing.md)
- [/System/Library/PrivateFrameworks/TSReading.framework/TSReading](DYLIBS/TSReading.md)
- [/System/Library/PrivateFrameworks/TSUtility.framework/TSUtility](DYLIBS/TSUtility.md)
- [/System/Library/PrivateFrameworks/TVAppServices.framework/TVAppServices](DYLIBS/TVAppServices.md)
- [/System/Library/PrivateFrameworks/TVLatency.framework/TVLatency](DYLIBS/TVLatency.md)
- [/System/Library/PrivateFrameworks/TVMLKit.framework/TVMLKit](DYLIBS/TVMLKit.md)
- [/System/Library/PrivateFrameworks/TVPlayback.framework/TVPlayback](DYLIBS/TVPlayback.md)
- [/System/Library/PrivateFrameworks/TVRemoteCore.framework/TVRemoteCore](DYLIBS/TVRemoteCore.md)
- [/System/Library/PrivateFrameworks/TVRemoteUI.framework/TVRemoteUI](DYLIBS/TVRemoteUI.md)
- [/System/Library/PrivateFrameworks/TVUIKit.framework/TVUIKit](DYLIBS/TVUIKit.md)
- [/System/Library/PrivateFrameworks/TailspinSymbolication.framework/TailspinSymbolication](DYLIBS/TailspinSymbolication.md)
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
- [/System/Library/PrivateFrameworks/TelephonyXPCServer.framework/TelephonyXPCServer](DYLIBS/TelephonyXPCServer.md)
- [/System/Library/PrivateFrameworks/TemplateKit.framework/TemplateKit](DYLIBS/TemplateKit.md)
- [/System/Library/PrivateFrameworks/TestFlightCore.framework/TestFlightCore](DYLIBS/TestFlightCore.md)
- [/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer](DYLIBS/TextComposer.md)
- [/System/Library/PrivateFrameworks/TextInput.framework/TextInput](DYLIBS/TextInput.md)
- [/System/Library/PrivateFrameworks/TextInputCJK.framework/TextInputCJK](DYLIBS/TextInputCJK.md)
- [/System/Library/PrivateFrameworks/TextInputCore.framework/TextInputCore](DYLIBS/TextInputCore.md)
- [/System/Library/PrivateFrameworks/TextInputTestingKit.framework/TextInputTestingKit](DYLIBS/TextInputTestingKit.md)
- [/System/Library/PrivateFrameworks/TextInputUI.framework/TextInputUI](DYLIBS/TextInputUI.md)
- [/System/Library/PrivateFrameworks/TextRecognition.framework/TextRecognition](DYLIBS/TextRecognition.md)
- [/System/Library/PrivateFrameworks/TextToSpeech.framework/TextToSpeech](DYLIBS/TextToSpeech.md)
- [/System/Library/PrivateFrameworks/TextToSpeechBundleSupport.framework/TextToSpeechBundleSupport](DYLIBS/TextToSpeechBundleSupport.md)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/deu.dylib](DYLIBS/deu.dylib.md)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/eci.dylib](DYLIBS/eci.dylib.md)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/eng.dylib](DYLIBS/eng.dylib.md)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/enu.dylib](DYLIBS/enu.dylib.md)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/esm.dylib](DYLIBS/esm.dylib.md)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/esp.dylib](DYLIBS/esp.dylib.md)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/fin.dylib](DYLIBS/fin.dylib.md)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/fra.dylib](DYLIBS/fra.dylib.md)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/frc.dylib](DYLIBS/frc.dylib.md)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/ita.dylib](DYLIBS/ita.dylib.md)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/ptb.dylib](DYLIBS/ptb.dylib.md)
- [/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/TextToSpeechKonaSupport](DYLIBS/TextToSpeechKonaSupport.md)
- [/System/Library/PrivateFrameworks/TextToSpeechMauiSupport.framework/TextToSpeechMauiSupport](DYLIBS/TextToSpeechMauiSupport.md)
- [/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingSupport.framework/TextToSpeechVoiceBankingSupport](DYLIBS/TextToSpeechVoiceBankingSupport.md)
- [/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingUI.framework/TextToSpeechVoiceBankingUI](DYLIBS/TextToSpeechVoiceBankingUI.md)
- [/System/Library/PrivateFrameworks/TextUnderstandingShared.framework/TextUnderstandingShared](DYLIBS/TextUnderstandingShared.md)
- [/System/Library/PrivateFrameworks/TextureIO.framework/TextureIO](DYLIBS/TextureIO.md)
- [/System/Library/PrivateFrameworks/ThirdPartyApplicationSettings.framework/ThirdPartyApplicationSettings](DYLIBS/ThirdPartyApplicationSettings.md)
- [/System/Library/PrivateFrameworks/TimeAppServices.framework/TimeAppServices](DYLIBS/TimeAppServices.md)
- [/System/Library/PrivateFrameworks/TimeSync.framework/TimeSync](DYLIBS/TimeSync.md)
- [/System/Library/PrivateFrameworks/Timeline.framework/Timeline](DYLIBS/Timeline.md)
- [/System/Library/PrivateFrameworks/TinCanShared.framework/TinCanShared](DYLIBS/TinCanShared.md)
- [/System/Library/PrivateFrameworks/TipKitCore.framework/TipKitCore](DYLIBS/TipKitCore.md)
- [/System/Library/PrivateFrameworks/TipKitLegacy.framework/TipKitLegacy](DYLIBS/TipKitLegacy.md)
- [/System/Library/PrivateFrameworks/TipKitServices.framework/TipKitServices](DYLIBS/TipKitServices.md)
- [/System/Library/PrivateFrameworks/TipsCore.framework/TipsCore](DYLIBS/TipsCore.md)
- [/System/Library/PrivateFrameworks/TipsDaemon.framework/TipsDaemon](DYLIBS/TipsDaemon.md)
- [/System/Library/PrivateFrameworks/TipsNextServices.framework/TipsNextServices](DYLIBS/TipsNextServices.md)
- [/System/Library/PrivateFrameworks/TipsTryIt.framework/TipsTryIt](DYLIBS/TipsTryIt.md)
- [/System/Library/PrivateFrameworks/TipsUI.framework/TipsUI](DYLIBS/TipsUI.md)
- [/System/Library/PrivateFrameworks/ToneKit.framework/ToneKit](DYLIBS/ToneKit.md)
- [/System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary](DYLIBS/ToneLibrary.md)
- [/System/Library/PrivateFrameworks/TouchML.framework/TouchML](DYLIBS/TouchML.md)
- [/System/Library/PrivateFrameworks/TouchRemote.framework/TouchRemote](DYLIBS/TouchRemote.md)
- [/System/Library/PrivateFrameworks/TrackingAvoidance.framework/TrackingAvoidance](DYLIBS/TrackingAvoidance.md)
- [/System/Library/PrivateFrameworks/TraitsArbiter.framework/TraitsArbiter](DYLIBS/TraitsArbiter.md)
- [/System/Library/PrivateFrameworks/Translation.framework/Translation](DYLIBS/Translation.md)
- [/System/Library/PrivateFrameworks/TranslationDaemon.framework/TranslationDaemon](DYLIBS/TranslationDaemon.md)
- [/System/Library/PrivateFrameworks/TranslationUI.framework/TranslationUI](DYLIBS/TranslationUI.md)
- [/System/Library/PrivateFrameworks/TranslationUIServices.framework/TranslationUIServices](DYLIBS/TranslationUIServices.md)
- [/System/Library/PrivateFrameworks/Transliteration.framework/Transliteration](DYLIBS/Transliteration.md)
- [/System/Library/PrivateFrameworks/Transparency.framework/Transparency](DYLIBS/Transparency.md)
- [/System/Library/PrivateFrameworks/TransparencyDetailsView.framework/TransparencyDetailsView](DYLIBS/TransparencyDetailsView.md)
- [/System/Library/PrivateFrameworks/TransparencyUI.framework/TransparencyUI](DYLIBS/TransparencyUI.md)
- [/System/Library/PrivateFrameworks/Trial.framework/Trial](DYLIBS/Trial.md)
- [/System/Library/PrivateFrameworks/TrialProto.framework/TrialProto](DYLIBS/TrialProto.md)
- [/System/Library/PrivateFrameworks/TrialServer.framework/TrialServer](DYLIBS/TrialServer.md)
- [/System/Library/PrivateFrameworks/TrustedPeers.framework/TrustedPeers](DYLIBS/TrustedPeers.md)
- [/System/Library/PrivateFrameworks/TuriCore.framework/TuriCore](DYLIBS/TuriCore.md)
- [/System/Library/PrivateFrameworks/TypistFramework.framework/TypistFramework](DYLIBS/TypistFramework.md)
- [/System/Library/PrivateFrameworks/TypologyAccess.framework/TypologyAccess](DYLIBS/TypologyAccess.md)
- [/System/Library/PrivateFrameworks/UARPUpdaterService.framework/UARPUpdaterService](DYLIBS/UARPUpdaterService.md)
- [/System/Library/PrivateFrameworks/UARPiCloud.framework/UARPiCloud](DYLIBS/UARPiCloud.md)
- [/System/Library/PrivateFrameworks/UIAccessibility.framework/UIAccessibility](DYLIBS/UIAccessibility.md)
- [/System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation](DYLIBS/UIFoundation.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore](DYLIBS/UIKitCore.md)
- [/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices](DYLIBS/UIKitServices.md)
- [/System/Library/PrivateFrameworks/UITriggerVC.framework/UITriggerVC](DYLIBS/UITriggerVC.md)
- [/System/Library/PrivateFrameworks/UIUnderstanding.framework/UIUnderstanding](DYLIBS/UIUnderstanding.md)
- [/System/Library/PrivateFrameworks/URLCompression.framework/URLCompression](DYLIBS/URLCompression.md)
- [/System/Library/PrivateFrameworks/URLFormatting.framework/URLFormatting](DYLIBS/URLFormatting.md)
- [/System/Library/PrivateFrameworks/USDKit.framework/USDKit](DYLIBS/USDKit.md)
- [/System/Library/PrivateFrameworks/USDLib_FormatLoaderProxy.framework/USDLib_FormatLoaderProxy](DYLIBS/USDLib_FormatLoaderProxy.md)
- [/System/Library/PrivateFrameworks/UVFSXPCService.framework/UVFSXPCService](DYLIBS/UVFSXPCService.md)
- [/System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework](DYLIBS/UnifiedAssetFramework.md)
- [/System/Library/PrivateFrameworks/UnityPoster.framework/UnityPoster](DYLIBS/UnityPoster.md)
- [/System/Library/PrivateFrameworks/UniversalHID.framework/UniversalHID](DYLIBS/UniversalHID.md)
- [/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTracking](DYLIBS/UsageTracking.md)
- [/System/Library/PrivateFrameworks/UserActivity.framework/UserActivity](DYLIBS/UserActivity.md)
- [/System/Library/PrivateFrameworks/UserAlerts.framework/UserAlerts](DYLIBS/UserAlerts.md)
- [/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/liblivefiles.plugin.dummy.dylib](DYLIBS/liblivefiles.plugin.dummy.dylib.md)
- [/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_apfs.dylib](DYLIBS/livefiles_apfs.dylib.md)
- [/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_cs.dylib](DYLIBS/livefiles_cs.dylib.md)
- [/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_exfat.dylib](DYLIBS/livefiles_exfat.dylib.md)
- [/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_hfs.dylib](DYLIBS/livefiles_hfs.dylib.md)
- [/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_msdos.dylib](DYLIBS/livefiles_msdos.dylib.md)
- [/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_ntfs.dylib](DYLIBS/livefiles_ntfs.dylib.md)
- [/System/Library/PrivateFrameworks/UserFS.framework/UserFS](DYLIBS/UserFS.md)
- [/System/Library/PrivateFrameworks/UserManagement.framework/UserManagement](DYLIBS/UserManagement.md)
- [/System/Library/PrivateFrameworks/UserManagementLayout.framework/UserManagementLayout](DYLIBS/UserManagementLayout.md)
- [/System/Library/PrivateFrameworks/UserManagementUI.framework/UserManagementUI](DYLIBS/UserManagementUI.md)
- [/System/Library/PrivateFrameworks/UserNotificationsCore.framework/UserNotificationsCore](DYLIBS/UserNotificationsCore.md)
- [/System/Library/PrivateFrameworks/UserNotificationsKit.framework/UserNotificationsKit](DYLIBS/UserNotificationsKit.md)
- [/System/Library/PrivateFrameworks/UserNotificationsServer.framework/UserNotificationsServer](DYLIBS/UserNotificationsServer.md)
- [/System/Library/PrivateFrameworks/UserNotificationsSettings.framework/UserNotificationsSettings](DYLIBS/UserNotificationsSettings.md)
- [/System/Library/PrivateFrameworks/UserNotificationsTranslation.framework/UserNotificationsTranslation](DYLIBS/UserNotificationsTranslation.md)
- [/System/Library/PrivateFrameworks/UserNotificationsUIKit.framework/UserNotificationsUIKit](DYLIBS/UserNotificationsUIKit.md)
- [/System/Library/PrivateFrameworks/UserSafety.framework/UserSafety](DYLIBS/UserSafety.md)
- [/System/Library/PrivateFrameworks/UserSafetyUI.framework/UserSafetyUI](DYLIBS/UserSafetyUI.md)
- [/System/Library/PrivateFrameworks/VFX.framework/Frameworks/libVFXCore.dylib](DYLIBS/libVFXCore.dylib.md)
- [/System/Library/PrivateFrameworks/VFX.framework/VFX](DYLIBS/VFX.md)
- [/System/Library/PrivateFrameworks/VectorKit.framework/VectorKit](DYLIBS/VectorKit.md)
- [/System/Library/PrivateFrameworks/VideoProcessing.framework/VideoProcessing](DYLIBS/VideoProcessing.md)
- [/System/Library/PrivateFrameworks/VideoSubscriberAccountUI.framework/VideoSubscriberAccountUI](DYLIBS/VideoSubscriberAccountUI.md)
- [/System/Library/PrivateFrameworks/VideoToolboxParavirtualizationSupport.framework/VideoToolboxParavirtualizationSupport](DYLIBS/VideoToolboxParavirtualizationSupport.md)
- [/System/Library/PrivateFrameworks/VideosUI.framework/VideosUI](DYLIBS/VideosUI.md)
- [/System/Library/PrivateFrameworks/VideosUICore.framework/VideosUICore](DYLIBS/VideosUICore.md)
- [/System/Library/PrivateFrameworks/VirtualGarage.framework/VirtualGarage](DYLIBS/VirtualGarage.md)
- [/System/Library/PrivateFrameworks/VisageHRTF.framework/VisageHRTF](DYLIBS/VisageHRTF.md)
- [/System/Library/PrivateFrameworks/VisionCore.framework/VisionCore](DYLIBS/VisionCore.md)
- [/System/Library/PrivateFrameworks/VisionHWAccelerationServices.framework/VisionHWAccelerationServices](DYLIBS/VisionHWAccelerationServices.md)
- [/System/Library/PrivateFrameworks/VisionKitCore.framework/VisionKitCore](DYLIBS/VisionKitCore.md)
- [/System/Library/PrivateFrameworks/VisionKitInternal.framework/VisionKitInternal](DYLIBS/VisionKitInternal.md)
- [/System/Library/PrivateFrameworks/VisualAlert.framework/VisualAlert](DYLIBS/VisualAlert.md)
- [/System/Library/PrivateFrameworks/VisualIntelligence.framework/VisualIntelligence](DYLIBS/VisualIntelligence.md)
- [/System/Library/PrivateFrameworks/VisualLocalization.framework/VisualLocalization](DYLIBS/VisualLocalization.md)
- [/System/Library/PrivateFrameworks/VisualLogger.framework/VisualLogger](DYLIBS/VisualLogger.md)
- [/System/Library/PrivateFrameworks/VisualPairing.framework/VisualPairing](DYLIBS/VisualPairing.md)
- [/System/Library/PrivateFrameworks/VisualUnderstanding.framework/VisualUnderstanding](DYLIBS/VisualUnderstanding.md)
- [/System/Library/PrivateFrameworks/VisualVoicemail.framework/IMAP.framework/IMAP](DYLIBS/IMAP.md)
- [/System/Library/PrivateFrameworks/VisualVoicemail.framework/VisualVoicemail](DYLIBS/VisualVoicemail.md)
- [/System/Library/PrivateFrameworks/VoiceActions.framework/VoiceActions](DYLIBS/VoiceActions.md)
- [/System/Library/PrivateFrameworks/VoiceMemos.framework/VoiceMemos](DYLIBS/VoiceMemos.md)
- [/System/Library/PrivateFrameworks/VoiceOverServices.framework/VoiceOverServices](DYLIBS/VoiceOverServices.md)
- [/System/Library/PrivateFrameworks/VoiceServices.framework/Support/libvoiced_tts.dylib](DYLIBS/libvoiced_tts.dylib.md)
- [/System/Library/PrivateFrameworks/VoiceServices.framework/VoiceServices](DYLIBS/VoiceServices.md)
- [/System/Library/PrivateFrameworks/VoiceShortcutClient.framework/VoiceShortcutClient](DYLIBS/VoiceShortcutClient.md)
- [/System/Library/PrivateFrameworks/VoiceShortcuts.framework/VoiceShortcuts](DYLIBS/VoiceShortcuts.md)
- [/System/Library/PrivateFrameworks/VoiceShortcutsUICardKitProviderSupport.framework/VoiceShortcutsUICardKitProviderSupport](DYLIBS/VoiceShortcutsUICardKitProviderSupport.md)
- [/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger](DYLIBS/VoiceTrigger.md)
- [/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/VoiceTriggerUI](DYLIBS/VoiceTriggerUI.md)
- [/System/Library/PrivateFrameworks/VoicemailStore.framework/VoicemailStore](DYLIBS/VoicemailStore.md)
- [/System/Library/PrivateFrameworks/WPDaemon.framework/WPDaemon](DYLIBS/WPDaemon.md)
- [/System/Library/PrivateFrameworks/WallpaperKit.framework/WallpaperKit](DYLIBS/WallpaperKit.md)
- [/System/Library/PrivateFrameworks/WatchControlAssets.framework/WatchControlAssets](DYLIBS/WatchControlAssets.md)
- [/System/Library/PrivateFrameworks/WatchControlSettings.framework/WatchControlSettings](DYLIBS/WatchControlSettings.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/WatchFacesWallpaperSupport](DYLIBS/WatchFacesWallpaperSupport.md)
- [/System/Library/PrivateFrameworks/WatchListKit.framework/WatchListKit](DYLIBS/WatchListKit.md)
- [/System/Library/PrivateFrameworks/WatchQuickActionsServices.framework/WatchQuickActionsServices](DYLIBS/WatchQuickActionsServices.md)
- [/System/Library/PrivateFrameworks/WatchReplies.framework/WatchReplies](DYLIBS/WatchReplies.md)
- [/System/Library/PrivateFrameworks/WatchdogClient.framework/WatchdogClient](DYLIBS/WatchdogClient.md)
- [/System/Library/PrivateFrameworks/Weather.framework/Weather](DYLIBS/Weather.md)
- [/System/Library/PrivateFrameworks/WeatherAnalytics.framework/WeatherAnalytics](DYLIBS/WeatherAnalytics.md)
- [/System/Library/PrivateFrameworks/WeatherCore.framework/WeatherCore](DYLIBS/WeatherCore.md)
- [/System/Library/PrivateFrameworks/WeatherDaemon.framework/WeatherDaemon](DYLIBS/WeatherDaemon.md)
- [/System/Library/PrivateFrameworks/WeatherFoundation.framework/WeatherFoundation](DYLIBS/WeatherFoundation.md)
- [/System/Library/PrivateFrameworks/WeatherMaps.framework/WeatherMaps](DYLIBS/WeatherMaps.md)
- [/System/Library/PrivateFrameworks/WeatherUI.framework/WeatherUI](DYLIBS/WeatherUI.md)
- [/System/Library/PrivateFrameworks/WebApp.framework/WebApp](DYLIBS/WebApp.md)
- [/System/Library/PrivateFrameworks/WebBookmarks.framework/WebBookmarks](DYLIBS/WebBookmarks.md)
- [/System/Library/PrivateFrameworks/WebBookmarksSwift.framework/WebBookmarksSwift](DYLIBS/WebBookmarksSwift.md)
- [/System/Library/PrivateFrameworks/WebContentAnalysis.framework/WebContentAnalysis](DYLIBS/WebContentAnalysis.md)
- [/System/Library/PrivateFrameworks/WebContentRestrictions.framework/WebContentRestrictions](DYLIBS/WebContentRestrictions.md)
- [/System/Library/PrivateFrameworks/WebCore.framework/Frameworks/libANGLE-shared.dylib](DYLIBS/libANGLE-shared.dylib.md)
- [/System/Library/PrivateFrameworks/WebCore.framework/Frameworks/libwebrtc.dylib](DYLIBS/libwebrtc.dylib.md)
- [/System/Library/PrivateFrameworks/WebCore.framework/WebCore](DYLIBS/WebCore.md)
- [/System/Library/PrivateFrameworks/WebGPU.framework/WebGPU](DYLIBS/WebGPU.md)
- [/System/Library/PrivateFrameworks/WebInspector.framework/WebInspector](DYLIBS/WebInspector.md)
- [/System/Library/PrivateFrameworks/WebKitLegacy.framework/WebKitLegacy](DYLIBS/WebKitLegacy.md)
- [/System/Library/PrivateFrameworks/WebPrivacy.framework/WebPrivacy](DYLIBS/WebPrivacy.md)
- [/System/Library/PrivateFrameworks/WebSheet.framework/WebSheet](DYLIBS/WebSheet.md)
- [/System/Library/PrivateFrameworks/WebUI.framework/WebUI](DYLIBS/WebUI.md)
- [/System/Library/PrivateFrameworks/WelcomeKit.framework/WelcomeKit](DYLIBS/WelcomeKit.md)
- [/System/Library/PrivateFrameworks/WelcomeKitCore.framework/WelcomeKitCore](DYLIBS/WelcomeKitCore.md)
- [/System/Library/PrivateFrameworks/WelcomeKitUI.framework/WelcomeKitUI](DYLIBS/WelcomeKitUI.md)
- [/System/Library/PrivateFrameworks/WellnessUI.framework/WellnessUI](DYLIBS/WellnessUI.md)
- [/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics](DYLIBS/WiFiAnalytics.md)
- [/System/Library/PrivateFrameworks/WiFiCloudSyncEngine.framework/WiFiCloudSyncEngine](DYLIBS/WiFiCloudSyncEngine.md)
- [/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit](DYLIBS/WiFiKit.md)
- [/System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI](DYLIBS/WiFiKitUI.md)
- [/System/Library/PrivateFrameworks/WiFiLogCapture.framework/WiFiLogCapture](DYLIBS/WiFiLogCapture.md)
- [/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer](DYLIBS/WiFiPeerToPeer.md)
- [/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy](DYLIBS/WiFiPolicy.md)
- [/System/Library/PrivateFrameworks/WiFiVelocity.framework/WiFiVelocity](DYLIBS/WiFiVelocity.md)
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
- [/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/WorkoutAnnouncements](DYLIBS/WorkoutAnnouncements.md)
- [/System/Library/PrivateFrameworks/WorkoutCore.framework/WorkoutCore](DYLIBS/WorkoutCore.md)
- [/System/Library/PrivateFrameworks/WorkoutHealthBridge.framework/WorkoutHealthBridge](DYLIBS/WorkoutHealthBridge.md)
- [/System/Library/PrivateFrameworks/WorkoutKitServices.framework/WorkoutKitServices](DYLIBS/WorkoutKitServices.md)
- [/System/Library/PrivateFrameworks/WorkoutKitUI.framework/WorkoutKitUI](DYLIBS/WorkoutKitUI.md)
- [/System/Library/PrivateFrameworks/WorkoutUI.framework/WorkoutUI](DYLIBS/WorkoutUI.md)
- [/System/Library/PrivateFrameworks/XCTTargetBootstrap.framework/XCTTargetBootstrap](DYLIBS/XCTTargetBootstrap.md)
- [/System/Library/PrivateFrameworks/XGBoostFramework.framework/XGBoostFramework](DYLIBS/XGBoostFramework.md)
- [/System/Library/PrivateFrameworks/XOJIT.framework/XOJIT](DYLIBS/XOJIT.md)
- [/System/Library/PrivateFrameworks/XOJITExecutor.framework/XOJITExecutor](DYLIBS/XOJITExecutor.md)
- [/System/Library/PrivateFrameworks/XavierCore.framework/XavierCore](DYLIBS/XavierCore.md)
- [/System/Library/PrivateFrameworks/XavierNews.framework/XavierNews](DYLIBS/XavierNews.md)
- [/System/Library/PrivateFrameworks/ZhuGeSupport.framework/ZhuGeSupport](DYLIBS/ZhuGeSupport.md)
- [/System/Library/PrivateFrameworks/ZhuGeSupport.framework/libZhuGeArmory.dylib](DYLIBS/libZhuGeArmory.dylib.md)
- [/System/Library/PrivateFrameworks/ZoomServices.framework/ZoomServices](DYLIBS/ZoomServices.md)
- [/System/Library/PrivateFrameworks/_Coherence_CloudKit_Private.framework/_Coherence_CloudKit_Private](DYLIBS/_Coherence_CloudKit_Private.md)
- [/System/Library/PrivateFrameworks/_IconServices_SwiftUI.framework/_IconServices_SwiftUI](DYLIBS/_IconServices_SwiftUI.md)
- [/System/Library/PrivateFrameworks/_JetEngine_SwiftUI.framework/_JetEngine_SwiftUI](DYLIBS/_JetEngine_SwiftUI.md)
- [/System/Library/PrivateFrameworks/_JetUI_SwiftUI.framework/_JetUI_SwiftUI](DYLIBS/_JetUI_SwiftUI.md)
- [/System/Library/PrivateFrameworks/_MusicKitInternal_MediaPlaybackCore.framework/_MusicKitInternal_MediaPlaybackCore](DYLIBS/_MusicKitInternal_MediaPlaybackCore.md)
- [/System/Library/PrivateFrameworks/_MusicKitInternal_MediaPlayer.framework/_MusicKitInternal_MediaPlayer](DYLIBS/_MusicKitInternal_MediaPlayer.md)
- [/System/Library/PrivateFrameworks/_MusicKitInternal_SwiftUI.framework/_MusicKitInternal_SwiftUI](DYLIBS/_MusicKitInternal_SwiftUI.md)
- [/System/Library/PrivateFrameworks/apfs_boot_mount.framework/apfs_boot_mount](DYLIBS/apfs_boot_mount.md)
- [/System/Library/PrivateFrameworks/caulk.framework/caulk](DYLIBS/caulk.md)
- [/System/Library/PrivateFrameworks/iCalendar.framework/iCalendar](DYLIBS/iCalendar.md)
- [/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore](DYLIBS/iCloudDriveCore.md)
- [/System/Library/PrivateFrameworks/iCloudDriveService.framework/iCloudDriveService](DYLIBS/iCloudDriveService.md)
- [/System/Library/PrivateFrameworks/iCloudMailAccountUI.framework/iCloudMailAccountUI](DYLIBS/iCloudMailAccountUI.md)
- [/System/Library/PrivateFrameworks/iCloudNotification.framework/iCloudNotification](DYLIBS/iCloudNotification.md)
- [/System/Library/PrivateFrameworks/iCloudQuota.framework/iCloudQuota](DYLIBS/iCloudQuota.md)
- [/System/Library/PrivateFrameworks/iCloudQuotaUI.framework/iCloudQuotaUI](DYLIBS/iCloudQuotaUI.md)
- [/System/Library/PrivateFrameworks/iCloudSubscriptionOptimizerClient.framework/iCloudSubscriptionOptimizerClient](DYLIBS/iCloudSubscriptionOptimizerClient.md)
- [/System/Library/PrivateFrameworks/iCloudSubscriptionOptimizerCore.framework/iCloudSubscriptionOptimizerCore](DYLIBS/iCloudSubscriptionOptimizerCore.md)
- [/System/Library/PrivateFrameworks/iCloudSubscriptionOptimizerDaemon.framework/iCloudSubscriptionOptimizerDaemon](DYLIBS/iCloudSubscriptionOptimizerDaemon.md)
- [/System/Library/PrivateFrameworks/iCloudSubscriptionOptimizerLighthouse.framework/iCloudSubscriptionOptimizerLighthouse](DYLIBS/iCloudSubscriptionOptimizerLighthouse.md)
- [/System/Library/PrivateFrameworks/iCloudSubscriptionOptimizerPFLTraining.framework/iCloudSubscriptionOptimizerPFLTraining](DYLIBS/iCloudSubscriptionOptimizerPFLTraining.md)
- [/System/Library/PrivateFrameworks/iMessageApps.framework/iMessageApps](DYLIBS/iMessageApps.md)
- [/System/Library/PrivateFrameworks/iOSDiagnostics.framework/iOSDiagnostics](DYLIBS/iOSDiagnostics.md)
- [/System/Library/PrivateFrameworks/iOSScreenSharing.framework/iOSScreenSharing](DYLIBS/iOSScreenSharing.md)
- [/System/Library/PrivateFrameworks/iTunesCloud.framework/iTunesCloud](DYLIBS/iTunesCloud.md)
- [/System/Library/PrivateFrameworks/iTunesStore.framework/iTunesStore](DYLIBS/iTunesStore.md)
- [/System/Library/PrivateFrameworks/iTunesStoreUI.framework/iTunesStoreUI](DYLIBS/iTunesStoreUI.md)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/EquationKit.framework/EquationKit](DYLIBS/EquationKit.md)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/KeynoteQuicklook.framework/KeynoteQuicklook](DYLIBS/KeynoteQuicklook.md)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/NumbersQuicklook.framework/NumbersQuicklook](DYLIBS/NumbersQuicklook.md)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/PagesQuicklook.framework/PagesQuicklook](DYLIBS/PagesQuicklook.md)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TQQuicklook.framework/TQQuicklook](DYLIBS/TQQuicklook.md)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSApplication.framework/TSApplication](DYLIBS/TSApplication.md)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSCalculationEngine.framework/TSCalculationEngine](DYLIBS/TSCalculationEngine.md)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSCharts.framework/TSCharts](DYLIBS/TSCharts.md)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSDrawables.framework/TSDrawables](DYLIBS/TSDrawables.md)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSKit.framework/TSKit](DYLIBS/TSKit.md)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSPersistence.framework/TSPersistence](DYLIBS/TSPersistence.md)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSStyles.framework/TSStyles](DYLIBS/TSStyles.md)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSTables.framework/TSTables](DYLIBS/TSTables.md)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSText.framework/TSText](DYLIBS/TSText.md)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSUtility.framework/TSUtility](DYLIBS/TSUtility.md)
- [/System/Library/PrivateFrameworks/iWorkXPC.framework/iWorkXPC](DYLIBS/iWorkXPC.md)
- [/System/Library/PrivateFrameworks/icloudMCCKit.framework/icloudMCCKit](DYLIBS/icloudMCCKit.md)
- [/System/Library/PrivateFrameworks/kperf.framework/kperf](DYLIBS/kperf.md)
- [/System/Library/PrivateFrameworks/kperfdata.framework/kperfdata](DYLIBS/kperfdata.md)
- [/System/Library/PrivateFrameworks/ktrace.framework/ktrace](DYLIBS/ktrace.md)
- [/System/Library/PrivateFrameworks/libEDR.framework/libEDR](DYLIBS/libEDR.md)
- [/System/Library/PrivateFrameworks/lighthouse_runtime.framework/lighthouse_runtime](DYLIBS/lighthouse_runtime.md)
- [/System/Library/PrivateFrameworks/oncrpc.framework/oncrpc](DYLIBS/oncrpc.md)
- [/System/Library/PrivateFrameworks/perfdata.framework/perfdata](DYLIBS/perfdata.md)
- [/System/Library/PrivateFrameworks/vCard.framework/vCard](DYLIBS/vCard.md)
- [/System/Library/ProceduralWallpaper/ProceduralWallpapers.bundle/ProceduralWallpapers](DYLIBS/ProceduralWallpapers.md)
- [/System/Library/RelevanceEngine/NanoDataSources/NanoMapsNavigationCompanionDataSource.bundle/NanoMapsNavigationCompanionDataSource](DYLIBS/NanoMapsNavigationCompanionDataSource.md)
- [/System/Library/RelevanceEngine/NanoDataSources/NanoMapsSampleDataSource.bundle/NanoMapsSampleDataSource](DYLIBS/NanoMapsSampleDataSource.md)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineHome.bundle/RelevanceEngineHome](DYLIBS/RelevanceEngineHome.md)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineSolar.bundle/RelevanceEngineSolar](DYLIBS/RelevanceEngineSolar.md)
- [/System/Library/RelevanceEngine/NanoDataSources/RelevanceEngineWeather.bundle/RelevanceEngineWeather](DYLIBS/RelevanceEngineWeather.md)
- [/System/Library/SystemConfiguration/CaptiveNetworkSupport.bundle/CaptiveNetworkSupport](DYLIBS/CaptiveNetworkSupport.md)
- [/System/Library/TextInput/TextInput_bo.bundle/TextInput_bo](DYLIBS/TextInput_bo.md)
- [/System/Library/TextInput/TextInput_ca.bundle/TextInput_ca](DYLIBS/TextInput_ca.md)
- [/System/Library/TextInput/TextInput_chr.bundle/TextInput_chr](DYLIBS/TextInput_chr.md)
- [/System/Library/TextInput/TextInput_cs.bundle/TextInput_cs](DYLIBS/TextInput_cs.md)
- [/System/Library/TextInput/TextInput_de.bundle/TextInput_de](DYLIBS/TextInput_de.md)
- [/System/Library/TextInput/TextInput_el.bundle/TextInput_el](DYLIBS/TextInput_el.md)
- [/System/Library/TextInput/TextInput_emoji.bundle/TextInput_emoji](DYLIBS/TextInput_emoji.md)
- [/System/Library/TextInput/TextInput_en.bundle/TextInput_en](DYLIBS/TextInput_en.md)
- [/System/Library/TextInput/TextInput_es.bundle/TextInput_es](DYLIBS/TextInput_es.md)
- [/System/Library/TextInput/TextInput_fr.bundle/TextInput_fr](DYLIBS/TextInput_fr.md)
- [/System/Library/TextInput/TextInput_haw.bundle/TextInput_haw](DYLIBS/TextInput_haw.md)
- [/System/Library/TextInput/TextInput_he.bundle/TextInput_he](DYLIBS/TextInput_he.md)
- [/System/Library/TextInput/TextInput_hi.bundle/TextInput_hi](DYLIBS/TextInput_hi.md)
- [/System/Library/TextInput/TextInput_intl.bundle/TextInput_intl](DYLIBS/TextInput_intl.md)
- [/System/Library/TextInput/TextInput_ja.bundle/TextInput_ja](DYLIBS/TextInput_ja.md)
- [/System/Library/TextInput/TextInput_ko.bundle/TextInput_ko](DYLIBS/TextInput_ko.md)
- [/System/Library/TextInput/TextInput_mr.bundle/TextInput_mr](DYLIBS/TextInput_mr.md)
- [/System/Library/TextInput/TextInput_mul.bundle/TextInput_mul](DYLIBS/TextInput_mul.md)
- [/System/Library/TextInput/TextInput_my.bundle/TextInput_my](DYLIBS/TextInput_my.md)
- [/System/Library/TextInput/TextInput_nl.bundle/TextInput_nl](DYLIBS/TextInput_nl.md)
- [/System/Library/TextInput/TextInput_pa.bundle/TextInput_pa](DYLIBS/TextInput_pa.md)
- [/System/Library/TextInput/TextInput_pt.bundle/TextInput_pt](DYLIBS/TextInput_pt.md)
- [/System/Library/TextInput/TextInput_si.bundle/TextInput_si](DYLIBS/TextInput_si.md)
- [/System/Library/TextInput/TextInput_sk.bundle/TextInput_sk](DYLIBS/TextInput_sk.md)
- [/System/Library/TextInput/TextInput_ta.bundle/TextInput_ta](DYLIBS/TextInput_ta.md)
- [/System/Library/TextInput/TextInput_th.bundle/TextInput_th](DYLIBS/TextInput_th.md)
- [/System/Library/TextInput/TextInput_tr.bundle/TextInput_tr](DYLIBS/TextInput_tr.md)
- [/System/Library/TextInput/TextInput_ug.bundle/TextInput_ug](DYLIBS/TextInput_ug.md)
- [/System/Library/TextInput/TextInput_vi.bundle/TextInput_vi](DYLIBS/TextInput_vi.md)
- [/System/Library/TextInput/TextInput_yue.bundle/TextInput_yue](DYLIBS/TextInput_yue.md)
- [/System/Library/TextInput/TextInput_zh.bundle/TextInput_zh](DYLIBS/TextInput_zh.md)
- [/System/Library/UserEventPlugins/AppleHDQGasGauge.plugin/AppleHDQGasGauge](DYLIBS/AppleHDQGasGauge.md)
- [/System/Library/VideoCodecs/H264SW.videocodec](DYLIBS/H264SW.videocodec.md)
- [/System/Library/VideoCodecs/VCPHEVC.videocodec](DYLIBS/VCPHEVC.videocodec.md)
- [/System/Library/VideoDecoders/AV1SW.videodecoder](DYLIBS/AV1SW.videodecoder.md)
- [/System/Library/VideoDecoders/AVD.videodecoder](DYLIBS/AVD.videodecoder.md)
- [/System/Library/VideoDecoders/AppleProResHWDecoder.videodecoder](DYLIBS/AppleProResHWDecoder.videodecoder.md)
- [/System/Library/VideoDecoders/AppleProResSWDecoder.videodecoder](DYLIBS/AppleProResSWDecoder.videodecoder.md)
- [/System/Library/VideoDecoders/H264H8.videodecoder](DYLIBS/H264H8.videodecoder.md)
- [/System/Library/VideoDecoders/JPEGH1.videodecoder](DYLIBS/JPEGH1.videodecoder.md)
- [/System/Library/VideoDecoders/MP4VH8.videodecoder](DYLIBS/MP4VH8.videodecoder.md)
- [/System/Library/VideoDecoders/VCH263.videodecoder](DYLIBS/VCH263.videodecoder.md)
- [/System/Library/VideoDecoders/VCPMP4V.videodecoder](DYLIBS/VCPMP4V.videodecoder.md)
- [/System/Library/VideoEncoders/AppleProResHWEncoder.videoencoder](DYLIBS/AppleProResHWEncoder.videoencoder.md)
- [/System/Library/VideoEncoders/AppleProResSWEncoder.videoencoder](DYLIBS/AppleProResSWEncoder.videoencoder.md)
- [/System/Library/VideoEncoders/H264H9.videoencoder](DYLIBS/H264H9.videoencoder.md)
- [/System/Library/VideoEncoders/H9.videoencoder](DYLIBS/H9.videoencoder.md)
- [/System/Library/VideoEncoders/JPEGH1.videoencoder](DYLIBS/JPEGH1.videoencoder.md)
- [/System/Library/VideoEncoders/VCH263.videoencoder](DYLIBS/VCH263.videoencoder.md)
- [/System/Library/VideoProcessors/BarcodeScanner.videoprocessor](DYLIBS/BarcodeScanner.videoprocessor.md)
- [/System/Library/VideoProcessors/CCPortrait.bundle/CCPortrait](DYLIBS/CCPortrait.md)
- [/System/Library/VideoProcessors/CalibrationV1.bundle/CalibrationV1](DYLIBS/CalibrationV1.md)
- [/System/Library/VideoProcessors/DepthProcessorV2.bundle/DepthProcessorV2](DYLIBS/DepthProcessorV2.md)
- [/System/Library/VideoProcessors/DisparityV5.bundle/DisparityV5](DYLIBS/DisparityV5.md)
- [/System/Library/VideoProcessors/IntelligentDistortionCorrectionV1.bundle/IntelligentDistortionCorrectionV1](DYLIBS/IntelligentDistortionCorrectionV1.md)
- [/System/Library/VideoProcessors/MattingV2.bundle/MattingV2](DYLIBS/MattingV2.md)
- [/System/Library/VideoProcessors/MetalFilter.bundle/MetalFilter](DYLIBS/MetalFilter.md)
- [/System/Library/VideoProcessors/NRFV2.bundle/NRFV2](DYLIBS/NRFV2.md)
- [/System/Library/VideoProcessors/NRFV4.bundle/NRFV4](DYLIBS/NRFV4.md)
- [/System/Library/VideoProcessors/SDOFRenderingV5.bundle/SDOFRenderingV5](DYLIBS/SDOFRenderingV5.md)
- [/System/Library/VideoProcessors/STF.bundle/STF](DYLIBS/STF.md)
- [/System/Library/VoiceServices/PlugIns/VoiceDial.vsplugin/VoiceDial](DYLIBS/VoiceDial.md)
- [/usr/lib/ACIPCBTLib.dylib](DYLIBS/ACIPCBTLib.dylib.md)
- [/usr/lib/AppleConvergedTransport.dylib](DYLIBS/AppleConvergedTransport.dylib.md)
- [/usr/lib/CarrierBundleUtilities.dylib](DYLIBS/CarrierBundleUtilities.dylib.md)
- [/usr/lib/dyld](DYLIBS/dyld.md)
- [/usr/lib/i18n/libBIG5.dylib](DYLIBS/libBIG5.dylib.md)
- [/usr/lib/i18n/libDECHanyu.dylib](DYLIBS/libDECHanyu.dylib.md)
- [/usr/lib/i18n/libDECKanji.dylib](DYLIBS/libDECKanji.dylib.md)
- [/usr/lib/i18n/libEUC.dylib](DYLIBS/libEUC.dylib.md)
- [/usr/lib/i18n/libEUCTW.dylib](DYLIBS/libEUCTW.dylib.md)
- [/usr/lib/i18n/libGBK2K.dylib](DYLIBS/libGBK2K.dylib.md)
- [/usr/lib/i18n/libHZ.dylib](DYLIBS/libHZ.dylib.md)
- [/usr/lib/i18n/libISO2022.dylib](DYLIBS/libISO2022.dylib.md)
- [/usr/lib/i18n/libJOHAB.dylib](DYLIBS/libJOHAB.dylib.md)
- [/usr/lib/i18n/libMSKanji.dylib](DYLIBS/libMSKanji.dylib.md)
- [/usr/lib/i18n/libUES.dylib](DYLIBS/libUES.dylib.md)
- [/usr/lib/i18n/libUTF1632.dylib](DYLIBS/libUTF1632.dylib.md)
- [/usr/lib/i18n/libUTF7.dylib](DYLIBS/libUTF7.dylib.md)
- [/usr/lib/i18n/libUTF8.dylib](DYLIBS/libUTF8.dylib.md)
- [/usr/lib/i18n/libUTF8MAC.dylib](DYLIBS/libUTF8MAC.dylib.md)
- [/usr/lib/i18n/libVIQR.dylib](DYLIBS/libVIQR.dylib.md)
- [/usr/lib/i18n/libZW.dylib](DYLIBS/libZW.dylib.md)
- [/usr/lib/i18n/libiconv_none.dylib](DYLIBS/libiconv_none.dylib.md)
- [/usr/lib/i18n/libiconv_std.dylib](DYLIBS/libiconv_std.dylib.md)
- [/usr/lib/i18n/libmapper_646.dylib](DYLIBS/libmapper_646.dylib.md)
- [/usr/lib/i18n/libmapper_none.dylib](DYLIBS/libmapper_none.dylib.md)
- [/usr/lib/i18n/libmapper_parallel.dylib](DYLIBS/libmapper_parallel.dylib.md)
- [/usr/lib/i18n/libmapper_serial.dylib](DYLIBS/libmapper_serial.dylib.md)
- [/usr/lib/i18n/libmapper_std.dylib](DYLIBS/libmapper_std.dylib.md)
- [/usr/lib/i18n/libmapper_zone.dylib](DYLIBS/libmapper_zone.dylib.md)
- [/usr/lib/libAHTRestore.dylib](DYLIBS/libAHTRestore.dylib.md)
- [/usr/lib/libARI.dylib](DYLIBS/libARI.dylib.md)
- [/usr/lib/libARIServer.dylib](DYLIBS/libARIServer.dylib.md)
- [/usr/lib/libATCommandStudioDynamic.dylib](DYLIBS/libATCommandStudioDynamic.dylib.md)
- [/usr/lib/libAWDProtobufBluetooth.dylib](DYLIBS/libAWDProtobufBluetooth.dylib.md)
- [/usr/lib/libAWDProtobufFacetime.dylib](DYLIBS/libAWDProtobufFacetime.dylib.md)
- [/usr/lib/libAWDProtobufFacetimeiMessage.dylib](DYLIBS/libAWDProtobufFacetimeiMessage.dylib.md)
- [/usr/lib/libAWDProtobufGCK.dylib](DYLIBS/libAWDProtobufGCK.dylib.md)
- [/usr/lib/libAWDProtobufLocation.dylib](DYLIBS/libAWDProtobufLocation.dylib.md)
- [/usr/lib/libAWDSupport.dylib](DYLIBS/libAWDSupport.dylib.md)
- [/usr/lib/libAWDSupportFramework.dylib](DYLIBS/libAWDSupportFramework.dylib.md)
- [/usr/lib/libAXSafeCategoryBundle.dylib](DYLIBS/libAXSafeCategoryBundle.dylib.md)
- [/usr/lib/libAXSpeechManager.dylib](DYLIBS/libAXSpeechManager.dylib.md)
- [/usr/lib/libAccessibility.dylib](DYLIBS/libAccessibility.dylib.md)
- [/usr/lib/libAppPatch.dylib](DYLIBS/libAppPatch.dylib.md)
- [/usr/lib/libAppleArchive.dylib](DYLIBS/libAppleArchive.dylib.md)
- [/usr/lib/libAppleEXR.dylib](DYLIBS/libAppleEXR.dylib.md)
- [/usr/lib/libAppleSSEExt.dylib](DYLIBS/libAppleSSEExt.dylib.md)
- [/usr/lib/libAppletTranslationLibrary.dylib](DYLIBS/libAppletTranslationLibrary.dylib.md)
- [/usr/lib/libAudioDSPCore.dylib](DYLIBS/libAudioDSPCore.dylib.md)
- [/usr/lib/libAudioIssueDetector.dylib](DYLIBS/libAudioIssueDetector.dylib.md)
- [/usr/lib/libAudioStatistics.dylib](DYLIBS/libAudioStatistics.dylib.md)
- [/usr/lib/libAudioToolboxUtility.dylib](DYLIBS/libAudioToolboxUtility.dylib.md)
- [/usr/lib/libBASupport.dylib](DYLIBS/libBASupport.dylib.md)
- [/usr/lib/libBBUpdaterDynamic.dylib](DYLIBS/libBBUpdaterDynamic.dylib.md)
- [/usr/lib/libBBUpdaterDynamic_stubs.dylib](DYLIBS/libBBUpdaterDynamic_stubs.dylib.md)
- [/usr/lib/libBKDM2.dylib](DYLIBS/libBKDM2.dylib.md)
- [/usr/lib/libBasebandCommandDrivers.dylib](DYLIBS/libBasebandCommandDrivers.dylib.md)
- [/usr/lib/libBasebandCommandDriversARI.dylib](DYLIBS/libBasebandCommandDriversARI.dylib.md)
- [/usr/lib/libBasebandCommandDriversQMI.dylib](DYLIBS/libBasebandCommandDriversQMI.dylib.md)
- [/usr/lib/libBasebandDiagnostic.dylib](DYLIBS/libBasebandDiagnostic.dylib.md)
- [/usr/lib/libBasebandManager.dylib](DYLIBS/libBasebandManager.dylib.md)
- [/usr/lib/libBasebandManagerICE.dylib](DYLIBS/libBasebandManagerICE.dylib.md)
- [/usr/lib/libCRFSuite.dylib](DYLIBS/libCRFSuite.dylib.md)
- [/usr/lib/libCTGreenTeaLogger.dylib](DYLIBS/libCTGreenTeaLogger.dylib.md)
- [/usr/lib/libChineseTokenizer.dylib](DYLIBS/libChineseTokenizer.dylib.md)
- [/usr/lib/libCoreEntitlements.dylib](DYLIBS/libCoreEntitlements.dylib.md)
- [/usr/lib/libDHCPServer.A.dylib](DYLIBS/libDHCPServer.A.dylib.md)
- [/usr/lib/libETLDIAGLoggingDynamic.dylib](DYLIBS/libETLDIAGLoggingDynamic.dylib.md)
- [/usr/lib/libETLDLFDynamic.dylib](DYLIBS/libETLDLFDynamic.dylib.md)
- [/usr/lib/libETLDLOADCoreDumpDynamic.dylib](DYLIBS/libETLDLOADCoreDumpDynamic.dylib.md)
- [/usr/lib/libETLDLOADDynamic.dylib](DYLIBS/libETLDLOADDynamic.dylib.md)
- [/usr/lib/libETLDMCDynamic.dylib](DYLIBS/libETLDMCDynamic.dylib.md)
- [/usr/lib/libETLDynamic.dylib](DYLIBS/libETLDynamic.dylib.md)
- [/usr/lib/libETLEFSDumpDynamic.dylib](DYLIBS/libETLEFSDumpDynamic.dylib.md)
- [/usr/lib/libETLSAHDynamic.dylib](DYLIBS/libETLSAHDynamic.dylib.md)
- [/usr/lib/libFDR.dylib](DYLIBS/libFDR.dylib.md)
- [/usr/lib/libFDRDecode.dylib](DYLIBS/libFDRDecode.dylib.md)
- [/usr/lib/libFosl_dynamic.dylib](DYLIBS/libFosl_dynamic.dylib.md)
- [/usr/lib/libHDLCDynamic.dylib](DYLIBS/libHDLCDynamic.dylib.md)
- [/usr/lib/libHSFilerDynamic.dylib](DYLIBS/libHSFilerDynamic.dylib.md)
- [/usr/lib/libICEClient.dylib](DYLIBS/libICEClient.dylib.md)
- [/usr/lib/libIOABP.dylib](DYLIBS/libIOABP.dylib.md)
- [/usr/lib/libIOACIPC.dylib](DYLIBS/libIOACIPC.dylib.md)
- [/usr/lib/libIOACIPCBB.dylib](DYLIBS/libIOACIPCBB.dylib.md)
- [/usr/lib/libIOAccessoryManager.dylib](DYLIBS/libIOAccessoryManager.dylib.md)
- [/usr/lib/libIOReport.dylib](DYLIBS/libIOReport.dylib.md)
- [/usr/lib/libKTLDynamic.dylib](DYLIBS/libKTLDynamic.dylib.md)
- [/usr/lib/libLLVM.dylib](DYLIBS/libLLVM.dylib.md)
- [/usr/lib/libMTLHud.dylib](DYLIBS/libMTLHud.dylib.md)
- [/usr/lib/libMatch.1.dylib](DYLIBS/libMatch.1.dylib.md)
- [/usr/lib/libMemoryResourceException.dylib](DYLIBS/libMemoryResourceException.dylib.md)
- [/usr/lib/libMobileCheckpoint.dylib](DYLIBS/libMobileCheckpoint.dylib.md)
- [/usr/lib/libMobileGestalt.dylib](DYLIBS/libMobileGestalt.dylib.md)
- [/usr/lib/libMobileGestaltExtensions.dylib](DYLIBS/libMobileGestaltExtensions.dylib.md)
- [/usr/lib/libNFC_Comet.dylib](DYLIBS/libNFC_Comet.dylib.md)
- [/usr/lib/libNFC_HAL.dylib](DYLIBS/libNFC_HAL.dylib.md)
- [/usr/lib/libPCITransport.dylib](DYLIBS/libPCITransport.dylib.md)
- [/usr/lib/libPN548_API.dylib](DYLIBS/libPN548_API.dylib.md)
- [/usr/lib/libPPM.dylib](DYLIBS/libPPM.dylib.md)
- [/usr/lib/libPPMDataModel.dylib](DYLIBS/libPPMDataModel.dylib.md)
- [/usr/lib/libParallelCompression.dylib](DYLIBS/libParallelCompression.dylib.md)
- [/usr/lib/libQMIParserDynamic.dylib](DYLIBS/libQMIParserDynamic.dylib.md)
- [/usr/lib/libRemoteTelephonyTransport.dylib](DYLIBS/libRemoteTelephonyTransport.dylib.md)
- [/usr/lib/libReverseProxyDevice.dylib](DYLIBS/libReverseProxyDevice.dylib.md)
- [/usr/lib/libRoseBooter.dylib](DYLIBS/libRoseBooter.dylib.md)
- [/usr/lib/libSCLM.dylib](DYLIBS/libSCLM.dylib.md)
- [/usr/lib/libSESShared.dylib](DYLIBS/libSESShared.dylib.md)
- [/usr/lib/libSLAMDynamic.dylib](DYLIBS/libSLAMDynamic.dylib.md)
- [/usr/lib/libSMC.dylib](DYLIBS/libSMC.dylib.md)
- [/usr/lib/libSoftwareUpdateSSO.dylib](DYLIBS/libSoftwareUpdateSSO.dylib.md)
- [/usr/lib/libSpatial.dylib](DYLIBS/libSpatial.dylib.md)
- [/usr/lib/libSystem.B.dylib](DYLIBS/libSystem.B.dylib.md)
- [/usr/lib/libSystemHealth.dylib](DYLIBS/libSystemHealth.dylib.md)
- [/usr/lib/libTLE.dylib](DYLIBS/libTLE.dylib.md)
- [/usr/lib/libTelephonyBasebandDynamic.dylib](DYLIBS/libTelephonyBasebandDynamic.dylib.md)
- [/usr/lib/libTelephonyCapabilities.dylib](DYLIBS/libTelephonyCapabilities.dylib.md)
- [/usr/lib/libTelephonyDebugDynamic.dylib](DYLIBS/libTelephonyDebugDynamic.dylib.md)
- [/usr/lib/libTelephonyIOKitDynamic.dylib](DYLIBS/libTelephonyIOKitDynamic.dylib.md)
- [/usr/lib/libTelephonyUSBDynamic.dylib](DYLIBS/libTelephonyUSBDynamic.dylib.md)
- [/usr/lib/libTelephonyUtilDynamic.dylib](DYLIBS/libTelephonyUtilDynamic.dylib.md)
- [/usr/lib/libThaiTokenizer.dylib](DYLIBS/libThaiTokenizer.dylib.md)
- [/usr/lib/libThreadExternalCommissioner.dylib](DYLIBS/libThreadExternalCommissioner.dylib.md)
- [/usr/lib/libWAPI.dylib](DYLIBS/libWAPI.dylib.md)
- [/usr/lib/libWISSupport.dylib](DYLIBS/libWISSupport.dylib.md)
- [/usr/lib/libWirelessAudioIPC.dylib](DYLIBS/libWirelessAudioIPC.dylib.md)
- [/usr/lib/libacmobileshim.dylib](DYLIBS/libacmobileshim.dylib.md)
- [/usr/lib/libafc.dylib](DYLIBS/libafc.dylib.md)
- [/usr/lib/libamsupport.dylib](DYLIBS/libamsupport.dylib.md)
- [/usr/lib/libapp_launch_measurement.dylib](DYLIBS/libapp_launch_measurement.dylib.md)
- [/usr/lib/libapple_nghttp2.dylib](DYLIBS/libapple_nghttp2.dylib.md)
- [/usr/lib/libarchive.2.dylib](DYLIBS/libarchive.2.dylib.md)
- [/usr/lib/libate.dylib](DYLIBS/libate.dylib.md)
- [/usr/lib/libauthinstall.dylib](DYLIBS/libauthinstall.dylib.md)
- [/usr/lib/libboringssl.dylib](DYLIBS/libboringssl.dylib.md)
- [/usr/lib/libbsm.0.dylib](DYLIBS/libbsm.0.dylib.md)
- [/usr/lib/libbz2.1.0.dylib](DYLIBS/libbz2.1.0.dylib.md)
- [/usr/lib/libc++.1.dylib](DYLIBS/libc++.1.dylib.md)
- [/usr/lib/libc++abi.dylib](DYLIBS/libc++abi.dylib.md)
- [/usr/lib/libchannel.dylib](DYLIBS/libchannel.dylib.md)
- [/usr/lib/libcharset.1.dylib](DYLIBS/libcharset.1.dylib.md)
- [/usr/lib/libcmark-gfm.dylib](DYLIBS/libcmark-gfm.dylib.md)
- [/usr/lib/libcmph.dylib](DYLIBS/libcmph.dylib.md)
- [/usr/lib/libcompression.dylib](DYLIBS/libcompression.dylib.md)
- [/usr/lib/libcoreroutine.dylib](DYLIBS/libcoreroutine.dylib.md)
- [/usr/lib/libcoretls.dylib](DYLIBS/libcoretls.dylib.md)
- [/usr/lib/libcoretls_cfhelpers.dylib](DYLIBS/libcoretls_cfhelpers.dylib.md)
- [/usr/lib/libcryptex.dylib](DYLIBS/libcryptex.dylib.md)
- [/usr/lib/libcryptex_core.dylib](DYLIBS/libcryptex_core.dylib.md)
- [/usr/lib/libcryptex_interface.dylib](DYLIBS/libcryptex_interface.dylib.md)
- [/usr/lib/libcryptex_trampoline.dylib](DYLIBS/libcryptex_trampoline.dylib.md)
- [/usr/lib/libcupolicy.dylib](DYLIBS/libcupolicy.dylib.md)
- [/usr/lib/libdns_services.dylib](DYLIBS/libdns_services.dylib.md)
- [/usr/lib/libdscsym.dylib](DYLIBS/libdscsym.dylib.md)
- [/usr/lib/libedit.3.dylib](DYLIBS/libedit.3.dylib.md)
- [/usr/lib/libenergytrace.dylib](DYLIBS/libenergytrace.dylib.md)
- [/usr/lib/libexpat.1.dylib](DYLIBS/libexpat.1.dylib.md)
- [/usr/lib/libexslt.0.dylib](DYLIBS/libexslt.0.dylib.md)
- [/usr/lib/libffi.dylib](DYLIBS/libffi.dylib.md)
- [/usr/lib/libfire7.dylib](DYLIBS/libfire7.dylib.md)
- [/usr/lib/libform.5.4.dylib](DYLIBS/libform.5.4.dylib.md)
- [/usr/lib/libgermantok.dylib](DYLIBS/libgermantok.dylib.md)
- [/usr/lib/libgraphcompute-rt.dylib](DYLIBS/libgraphcompute-rt.dylib.md)
- [/usr/lib/libheimdal-asn1.dylib](DYLIBS/libheimdal-asn1.dylib.md)
- [/usr/lib/libheimdalasn1.dylib](DYLIBS/libheimdalasn1.dylib.md)
- [/usr/lib/libiconv.2.dylib](DYLIBS/libiconv.2.dylib.md)
- [/usr/lib/libicucore.A.dylib](DYLIBS/libicucore.A.dylib.md)
- [/usr/lib/libimg4.dylib](DYLIBS/libimg4.dylib.md)
- [/usr/lib/libipconfig.dylib](DYLIBS/libipconfig.dylib.md)
- [/usr/lib/libipsec.A.dylib](DYLIBS/libipsec.A.dylib.md)
- [/usr/lib/libktrace.dylib](DYLIBS/libktrace.dylib.md)
- [/usr/lib/liblangid.dylib](DYLIBS/liblangid.dylib.md)
- [/usr/lib/libllvm-flatbuffers.dylib](DYLIBS/libllvm-flatbuffers.dylib.md)
- [/usr/lib/libllvm-lmdb.dylib](DYLIBS/libllvm-lmdb.dylib.md)
- [/usr/lib/liblockdown.dylib](DYLIBS/liblockdown.dylib.md)
- [/usr/lib/liblzma.5.dylib](DYLIBS/liblzma.5.dylib.md)
- [/usr/lib/libmarisa.dylib](DYLIBS/libmarisa.dylib.md)
- [/usr/lib/libmav_ipc_router_dynamic.dylib](DYLIBS/libmav_ipc_router_dynamic.dylib.md)
- [/usr/lib/libmd.dylib](DYLIBS/libmd.dylib.md)
- [/usr/lib/libmdns.dylib](DYLIBS/libmdns.dylib.md)
- [/usr/lib/libmecab.dylib](DYLIBS/libmecab.dylib.md)
- [/usr/lib/libmecabra.dylib](DYLIBS/libmecabra.dylib.md)
- [/usr/lib/libmis.dylib](DYLIBS/libmis.dylib.md)
- [/usr/lib/libmobileassetd.dylib](DYLIBS/libmobileassetd.dylib.md)
- [/usr/lib/libmorphun.dylib](DYLIBS/libmorphun.dylib.md)
- [/usr/lib/libmrc.dylib](DYLIBS/libmrc.dylib.md)
- [/usr/lib/libncurses.5.4.dylib](DYLIBS/libncurses.5.4.dylib.md)
- [/usr/lib/libnetquality.dylib](DYLIBS/libnetquality.dylib.md)
- [/usr/lib/libnetwork.dylib](DYLIBS/libnetwork.dylib.md)
- [/usr/lib/libnetworkextension.dylib](DYLIBS/libnetworkextension.dylib.md)
- [/usr/lib/libnfrestore.dylib](DYLIBS/libnfrestore.dylib.md)
- [/usr/lib/libnfshared.dylib](DYLIBS/libnfshared.dylib.md)
- [/usr/lib/libnfstorage.dylib](DYLIBS/libnfstorage.dylib.md)
- [/usr/lib/libnwswifttls.dylib](DYLIBS/libnwswifttls.dylib.md)
- [/usr/lib/libobjc.A.dylib](DYLIBS/libobjc.A.dylib.md)
- [/usr/lib/libolaf.dylib](DYLIBS/libolaf.dylib.md)
- [/usr/lib/libomadm.dylib](DYLIBS/libomadm.dylib.md)
- [/usr/lib/libpartition2_dynamic.dylib](DYLIBS/libpartition2_dynamic.dylib.md)
- [/usr/lib/libpcap.A.dylib](DYLIBS/libpcap.A.dylib.md)
- [/usr/lib/libperfcheck.dylib](DYLIBS/libperfcheck.dylib.md)
- [/usr/lib/libpmenergy.dylib](DYLIBS/libpmenergy.dylib.md)
- [/usr/lib/libpmsample.dylib](DYLIBS/libpmsample.dylib.md)
- [/usr/lib/libprequelite.dylib](DYLIBS/libprequelite.dylib.md)
- [/usr/lib/libprotobuf-lite.dylib](DYLIBS/libprotobuf-lite.dylib.md)
- [/usr/lib/libprotobuf.dylib](DYLIBS/libprotobuf.dylib.md)
- [/usr/lib/libquic.dylib](DYLIBS/libquic.dylib.md)
- [/usr/lib/librealtime_safety.dylib](DYLIBS/librealtime_safety.dylib.md)
- [/usr/lib/libresolv.9.dylib](DYLIBS/libresolv.9.dylib.md)
- [/usr/lib/libsandbox.1.dylib](DYLIBS/libsandbox.1.dylib.md)
- [/usr/lib/libsbuf.dylib](DYLIBS/libsbuf.dylib.md)
- [/usr/lib/libskit.dylib](DYLIBS/libskit.dylib.md)
- [/usr/lib/libsp.dylib](DYLIBS/libsp.dylib.md)
- [/usr/lib/libspindump.dylib](DYLIBS/libspindump.dylib.md)
- [/usr/lib/libsqlite3.dylib](DYLIBS/libsqlite3.dylib.md)
- [/usr/lib/libsysdiagnose.dylib](DYLIBS/libsysdiagnose.dylib.md)
- [/usr/lib/libsysmon.dylib](DYLIBS/libsysmon.dylib.md)
- [/usr/lib/libsystemstats.dylib](DYLIBS/libsystemstats.dylib.md)
- [/usr/lib/libtailspin.dylib](DYLIBS/libtailspin.dylib.md)
- [/usr/lib/libtidy.A.dylib](DYLIBS/libtidy.A.dylib.md)
- [/usr/lib/libtzupdate.dylib](DYLIBS/libtzupdate.dylib.md)
- [/usr/lib/libusrtcp.dylib](DYLIBS/libusrtcp.dylib.md)
- [/usr/lib/libutil.dylib](DYLIBS/libutil.dylib.md)
- [/usr/lib/libxml2.2.dylib](DYLIBS/libxml2.2.dylib.md)
- [/usr/lib/libxo.dylib](DYLIBS/libxo.dylib.md)
- [/usr/lib/libxpc_datastores.dylib](DYLIBS/libxpc_datastores.dylib.md)
- [/usr/lib/libxslt.1.dylib](DYLIBS/libxslt.1.dylib.md)
- [/usr/lib/libz.1.dylib](DYLIBS/libz.1.dylib.md)
- [/usr/lib/log/liblog_IOHIDFamily.dylib](DYLIBS/liblog_IOHIDFamily.dylib.md)
- [/usr/lib/log/liblog_SystemConfiguration.dylib](DYLIBS/liblog_SystemConfiguration.dylib.md)
- [/usr/lib/log/liblog_coreacc.dylib](DYLIBS/liblog_coreacc.dylib.md)
- [/usr/lib/log/liblog_geo.dylib](DYLIBS/liblog_geo.dylib.md)
- [/usr/lib/log/liblog_location.dylib](DYLIBS/liblog_location.dylib.md)
- [/usr/lib/log/liblog_mdns.dylib](DYLIBS/liblog_mdns.dylib.md)
- [/usr/lib/log/liblog_mdnsresponder.dylib](DYLIBS/liblog_mdnsresponder.dylib.md)
- [/usr/lib/log/liblog_network.dylib](DYLIBS/liblog_network.dylib.md)
- [/usr/lib/log/liblog_signpost.description.dylib](DYLIBS/liblog_signpost.description.dylib.md)
- [/usr/lib/log/liblog_signpost.dylib](DYLIBS/liblog_signpost.dylib.md)
- [/usr/lib/log/liblog_signpost.telemetry.dylib](DYLIBS/liblog_signpost.telemetry.dylib.md)
- [/usr/lib/log/liblog_srp.dylib](DYLIBS/liblog_srp.dylib.md)
- [/usr/lib/swift/libswiftARKit.dylib](DYLIBS/libswiftARKit.dylib.md)
- [/usr/lib/swift/libswiftAVFoundation.dylib](DYLIBS/libswiftAVFoundation.dylib.md)
- [/usr/lib/swift/libswiftAccelerate.dylib](DYLIBS/libswiftAccelerate.dylib.md)
- [/usr/lib/swift/libswiftAppleArchive.dylib](DYLIBS/libswiftAppleArchive.dylib.md)
- [/usr/lib/swift/libswiftAssetsLibrary.dylib](DYLIBS/libswiftAssetsLibrary.dylib.md)
- [/usr/lib/swift/libswiftCallKit.dylib](DYLIBS/libswiftCallKit.dylib.md)
- [/usr/lib/swift/libswiftCarPlay.dylib](DYLIBS/libswiftCarPlay.dylib.md)
- [/usr/lib/swift/libswiftCompression.dylib](DYLIBS/libswiftCompression.dylib.md)
- [/usr/lib/swift/libswiftContacts.dylib](DYLIBS/libswiftContacts.dylib.md)
- [/usr/lib/swift/libswiftCore.dylib](DYLIBS/libswiftCore.dylib.md)
- [/usr/lib/swift/libswiftCoreAudio.dylib](DYLIBS/libswiftCoreAudio.dylib.md)
- [/usr/lib/swift/libswiftCoreData.dylib](DYLIBS/libswiftCoreData.dylib.md)
- [/usr/lib/swift/libswiftCoreFoundation.dylib](DYLIBS/libswiftCoreFoundation.dylib.md)
- [/usr/lib/swift/libswiftCoreGraphics.dylib](DYLIBS/libswiftCoreGraphics.dylib.md)
- [/usr/lib/swift/libswiftCoreImage.dylib](DYLIBS/libswiftCoreImage.dylib.md)
- [/usr/lib/swift/libswiftCoreLocation.dylib](DYLIBS/libswiftCoreLocation.dylib.md)
- [/usr/lib/swift/libswiftCoreMIDI.dylib](DYLIBS/libswiftCoreMIDI.dylib.md)
- [/usr/lib/swift/libswiftCoreML.dylib](DYLIBS/libswiftCoreML.dylib.md)
- [/usr/lib/swift/libswiftCoreMedia.dylib](DYLIBS/libswiftCoreMedia.dylib.md)
- [/usr/lib/swift/libswiftCoreNFC.dylib](DYLIBS/libswiftCoreNFC.dylib.md)
- [/usr/lib/swift/libswiftCryptoTokenKit.dylib](DYLIBS/libswiftCryptoTokenKit.dylib.md)
- [/usr/lib/swift/libswiftDarwin.dylib](DYLIBS/libswiftDarwin.dylib.md)
- [/usr/lib/swift/libswiftDataDetection.dylib](DYLIBS/libswiftDataDetection.dylib.md)
- [/usr/lib/swift/libswiftDemangle.dylib](DYLIBS/libswiftDemangle.dylib.md)
- [/usr/lib/swift/libswiftDispatch.dylib](DYLIBS/libswiftDispatch.dylib.md)
- [/usr/lib/swift/libswiftDistributed.dylib](DYLIBS/libswiftDistributed.dylib.md)
- [/usr/lib/swift/libswiftExtensionFoundation.dylib](DYLIBS/libswiftExtensionFoundation.dylib.md)
- [/usr/lib/swift/libswiftExtensionKit.dylib](DYLIBS/libswiftExtensionKit.dylib.md)
- [/usr/lib/swift/libswiftFileProvider.dylib](DYLIBS/libswiftFileProvider.dylib.md)
- [/usr/lib/swift/libswiftFoundation.dylib](DYLIBS/libswiftFoundation.dylib.md)
- [/usr/lib/swift/libswiftGLKit.dylib](DYLIBS/libswiftGLKit.dylib.md)
- [/usr/lib/swift/libswiftGameplayKit.dylib](DYLIBS/libswiftGameplayKit.dylib.md)
- [/usr/lib/swift/libswiftHealthKit.dylib](DYLIBS/libswiftHealthKit.dylib.md)
- [/usr/lib/swift/libswiftHomeKit.dylib](DYLIBS/libswiftHomeKit.dylib.md)
- [/usr/lib/swift/libswiftIdentityLookup.dylib](DYLIBS/libswiftIdentityLookup.dylib.md)
- [/usr/lib/swift/libswiftIntents.dylib](DYLIBS/libswiftIntents.dylib.md)
- [/usr/lib/swift/libswiftMLCompute.dylib](DYLIBS/libswiftMLCompute.dylib.md)
- [/usr/lib/swift/libswiftMapKit.dylib](DYLIBS/libswiftMapKit.dylib.md)
- [/usr/lib/swift/libswiftMediaPlayer.dylib](DYLIBS/libswiftMediaPlayer.dylib.md)
- [/usr/lib/swift/libswiftMetal.dylib](DYLIBS/libswiftMetal.dylib.md)
- [/usr/lib/swift/libswiftMetalKit.dylib](DYLIBS/libswiftMetalKit.dylib.md)
- [/usr/lib/swift/libswiftMetricKit.dylib](DYLIBS/libswiftMetricKit.dylib.md)
- [/usr/lib/swift/libswiftModelIO.dylib](DYLIBS/libswiftModelIO.dylib.md)
- [/usr/lib/swift/libswiftNaturalLanguage.dylib](DYLIBS/libswiftNaturalLanguage.dylib.md)
- [/usr/lib/swift/libswiftNearbyInteraction.dylib](DYLIBS/libswiftNearbyInteraction.dylib.md)
- [/usr/lib/swift/libswiftNetwork.dylib](DYLIBS/libswiftNetwork.dylib.md)
- [/usr/lib/swift/libswiftOSLog.dylib](DYLIBS/libswiftOSLog.dylib.md)
- [/usr/lib/swift/libswiftObjectiveC.dylib](DYLIBS/libswiftObjectiveC.dylib.md)
- [/usr/lib/swift/libswiftObservation.dylib](DYLIBS/libswiftObservation.dylib.md)
- [/usr/lib/swift/libswiftPassKit.dylib](DYLIBS/libswiftPassKit.dylib.md)
- [/usr/lib/swift/libswiftPhotos.dylib](DYLIBS/libswiftPhotos.dylib.md)
- [/usr/lib/swift/libswiftPhotosUI.dylib](DYLIBS/libswiftPhotosUI.dylib.md)
- [/usr/lib/swift/libswiftQuartzCore.dylib](DYLIBS/libswiftQuartzCore.dylib.md)
- [/usr/lib/swift/libswiftRegexBuilder.dylib](DYLIBS/libswiftRegexBuilder.dylib.md)
- [/usr/lib/swift/libswiftSceneKit.dylib](DYLIBS/libswiftSceneKit.dylib.md)
- [/usr/lib/swift/libswiftShazamKit.dylib](DYLIBS/libswiftShazamKit.dylib.md)
- [/usr/lib/swift/libswiftSpatial.dylib](DYLIBS/libswiftSpatial.dylib.md)
- [/usr/lib/swift/libswiftSpeech.dylib](DYLIBS/libswiftSpeech.dylib.md)
- [/usr/lib/swift/libswiftSpriteKit.dylib](DYLIBS/libswiftSpriteKit.dylib.md)
- [/usr/lib/swift/libswiftSwiftOnoneSupport.dylib](DYLIBS/libswiftSwiftOnoneSupport.dylib.md)
- [/usr/lib/swift/libswiftSystem.dylib](DYLIBS/libswiftSystem.dylib.md)
- [/usr/lib/swift/libswiftSystem_Foundation.dylib](DYLIBS/libswiftSystem_Foundation.dylib.md)
- [/usr/lib/swift/libswiftUIKit.dylib](DYLIBS/libswiftUIKit.dylib.md)
- [/usr/lib/swift/libswiftUniformTypeIdentifiers.dylib](DYLIBS/libswiftUniformTypeIdentifiers.dylib.md)
- [/usr/lib/swift/libswiftVideoToolbox.dylib](DYLIBS/libswiftVideoToolbox.dylib.md)
- [/usr/lib/swift/libswiftVision.dylib](DYLIBS/libswiftVision.dylib.md)
- [/usr/lib/swift/libswiftWatchKit.dylib](DYLIBS/libswiftWatchKit.dylib.md)
- [/usr/lib/swift/libswiftWebKit.dylib](DYLIBS/libswiftWebKit.dylib.md)
- [/usr/lib/swift/libswiftXPC.dylib](DYLIBS/libswiftXPC.dylib.md)
- [/usr/lib/swift/libswift_Concurrency.dylib](DYLIBS/libswift_Concurrency.dylib.md)
- [/usr/lib/swift/libswift_Differentiation.dylib](DYLIBS/libswift_Differentiation.dylib.md)
- [/usr/lib/swift/libswift_RegexParser.dylib](DYLIBS/libswift_RegexParser.dylib.md)
- [/usr/lib/swift/libswift_StringProcessing.dylib](DYLIBS/libswift_StringProcessing.dylib.md)
- [/usr/lib/swift/libswiftos.dylib](DYLIBS/libswiftos.dylib.md)
- [/usr/lib/swift/libswiftsimd.dylib](DYLIBS/libswiftsimd.dylib.md)
- [/usr/lib/swift/~libswiftPencilKit.dylib](DYLIBS/~libswiftPencilKit.dylib.md)
- [/usr/lib/system/libcache.dylib](DYLIBS/libcache.dylib.md)
- [/usr/lib/system/libcommonCrypto.dylib](DYLIBS/libcommonCrypto.dylib.md)
- [/usr/lib/system/libcompiler_rt.dylib](DYLIBS/libcompiler_rt.dylib.md)
- [/usr/lib/system/libcopyfile.dylib](DYLIBS/libcopyfile.dylib.md)
- [/usr/lib/system/libcorecrypto.dylib](DYLIBS/libcorecrypto.dylib.md)
- [/usr/lib/system/libcorecrypto_noasm.dylib](DYLIBS/libcorecrypto_noasm.dylib.md)
- [/usr/lib/system/libcorecrypto_trace.dylib](DYLIBS/libcorecrypto_trace.dylib.md)
- [/usr/lib/system/libdispatch.dylib](DYLIBS/libdispatch.dylib.md)
- [/usr/lib/system/libdyld.dylib](DYLIBS/libdyld.dylib.md)
- [/usr/lib/system/liblaunch.dylib](DYLIBS/liblaunch.dylib.md)
- [/usr/lib/system/libmacho.dylib](DYLIBS/libmacho.dylib.md)
- [/usr/lib/system/libremovefile.dylib](DYLIBS/libremovefile.dylib.md)
- [/usr/lib/system/libsystem_asl.dylib](DYLIBS/libsystem_asl.dylib.md)
- [/usr/lib/system/libsystem_blocks.dylib](DYLIBS/libsystem_blocks.dylib.md)
- [/usr/lib/system/libsystem_c.dylib](DYLIBS/libsystem_c.dylib.md)
- [/usr/lib/system/libsystem_collections.dylib](DYLIBS/libsystem_collections.dylib.md)
- [/usr/lib/system/libsystem_configuration.dylib](DYLIBS/libsystem_configuration.dylib.md)
- [/usr/lib/system/libsystem_containermanager.dylib](DYLIBS/libsystem_containermanager.dylib.md)
- [/usr/lib/system/libsystem_coreservices.dylib](DYLIBS/libsystem_coreservices.dylib.md)
- [/usr/lib/system/libsystem_darwin.dylib](DYLIBS/libsystem_darwin.dylib.md)
- [/usr/lib/system/libsystem_darwindirectory.dylib](DYLIBS/libsystem_darwindirectory.dylib.md)
- [/usr/lib/system/libsystem_dnssd.dylib](DYLIBS/libsystem_dnssd.dylib.md)
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
- [/usr/lib/system/libsystem_symptoms.dylib](DYLIBS/libsystem_symptoms.dylib.md)
- [/usr/lib/system/libsystem_trace.dylib](DYLIBS/libsystem_trace.dylib.md)
- [/usr/lib/system/libunwind.dylib](DYLIBS/libunwind.dylib.md)
- [/usr/lib/system/libxpc.dylib](DYLIBS/libxpc.dylib.md)
- [/usr/lib/updaters/libAce3Updater.dylib](DYLIBS/libAce3Updater.dylib.md)
- [/usr/lib/updaters/libAppleTCONUpdater.dylib](DYLIBS/libAppleTCONUpdater.dylib.md)
- [/usr/lib/updaters/libRoseUpdater.dylib](DYLIBS/libRoseUpdater.dylib.md)
- [/usr/lib/updaters/libSEUpdater.dylib](DYLIBS/libSEUpdater.dylib.md)
- [/usr/lib/updaters/libSavageRestoreInfo_iOS.dylib](DYLIBS/libSavageRestoreInfo_iOS.dylib.md)
- [/usr/lib/updaters/libSavageUpdater_iOS.dylib](DYLIBS/libSavageUpdater_iOS.dylib.md)
- [/usr/lib/updaters/libT200Updater.dylib](DYLIBS/libT200Updater.dylib.md)
- [/usr/lib/updaters/libVinylUpdater.dylib](DYLIBS/libVinylUpdater.dylib.md)
- [/usr/lib/usd/libusd_ms.dylib](DYLIBS/libusd_ms.dylib.md)

</details>

## Files

### 🆕 New

#### IPSW (2)

- `Firmware/Mav23-1.40.01.Release.bbfw`
- `Firmware/Mav23-1.40.01.Release.plist`

#### filesystem (485)

<details>
  <summary><i>View Files</i></summary>

- `/Applications/CoreAuthUI.app/MobileUI-Ratchet.loctable`
- `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6004.appex/Diagnostic-6004`
- `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6004.appex/Info.plist`
- `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6004.appex/Localizable.loctable`
- `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6004.appex/_CodeSignature/CodeResources`
- `/Applications/Setup.app/ar.lproj/DimpleKey.strings`
- `/Applications/Setup.app/bg.lproj/DimpleKey.strings`
- `/Applications/Setup.app/ca.lproj/DimpleKey.strings`
- `/Applications/Setup.app/cs.lproj/DimpleKey.strings`
- `/Applications/Setup.app/da.lproj/DimpleKey.strings`
- `/Applications/Setup.app/de.lproj/DimpleKey.strings`
- `/Applications/Setup.app/el.lproj/DimpleKey.strings`
- `/Applications/Setup.app/en.lproj/DimpleKey.strings`
- `/Applications/Setup.app/en_AU.lproj/DimpleKey.strings`
- `/Applications/Setup.app/en_GB.lproj/DimpleKey.strings`
- `/Applications/Setup.app/en_IN.lproj/DimpleKey.strings`
- `/Applications/Setup.app/es.lproj/DimpleKey.strings`
- `/Applications/Setup.app/es_419.lproj/DimpleKey.strings`
- `/Applications/Setup.app/fi.lproj/DimpleKey.strings`
- `/Applications/Setup.app/fr.lproj/DimpleKey.strings`
- `/Applications/Setup.app/fr_CA.lproj/DimpleKey.strings`
- `/Applications/Setup.app/he.lproj/DimpleKey.strings`
- `/Applications/Setup.app/hi.lproj/DimpleKey.strings`
- `/Applications/Setup.app/hr.lproj/DimpleKey.strings`
- `/Applications/Setup.app/hu.lproj/DimpleKey.strings`
- `/Applications/Setup.app/id.lproj/DimpleKey.strings`
- `/Applications/Setup.app/it.lproj/DimpleKey.strings`
- `/Applications/Setup.app/ja.lproj/DimpleKey.strings`
- `/Applications/Setup.app/kk.lproj/DimpleKey.strings`
- `/Applications/Setup.app/ko.lproj/DimpleKey.strings`
- `/Applications/Setup.app/ms.lproj/DimpleKey.strings`
- `/Applications/Setup.app/nl.lproj/DimpleKey.strings`
- `/Applications/Setup.app/no.lproj/DimpleKey.strings`
- `/Applications/Setup.app/pl.lproj/DimpleKey.strings`
- `/Applications/Setup.app/pt_BR.lproj/DimpleKey.strings`
- `/Applications/Setup.app/pt_PT.lproj/DimpleKey.strings`
- `/Applications/Setup.app/ro.lproj/DimpleKey.strings`
- `/Applications/Setup.app/ru.lproj/DimpleKey.strings`
- `/Applications/Setup.app/sk.lproj/DimpleKey.strings`
- `/Applications/Setup.app/sv.lproj/DimpleKey.strings`
- `/Applications/Setup.app/th.lproj/DimpleKey.strings`
- `/Applications/Setup.app/tr.lproj/DimpleKey.strings`
- `/Applications/Setup.app/uk.lproj/DimpleKey.strings`
- `/Applications/Setup.app/vi.lproj/DimpleKey.strings`
- `/Applications/Setup.app/yue_CN.lproj/DimpleKey.strings`
- `/Applications/Setup.app/zh_CN.lproj/DimpleKey.strings`
- `/Applications/Setup.app/zh_HK.lproj/DimpleKey.strings`
- `/Applications/Setup.app/zh_TW.lproj/DimpleKey.strings`
- `/System/Library/AppPlaceholders/Books.app/PlugIns/BooksSpotlightExtension.appex/Info.plist`
- `/System/Library/AppPlaceholders/Books.app/PlugIns/BooksSpotlightExtension.appex/PlaceholderEntitlements.plist`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Templates/dialog/CommonMediaIntent.catfamily/AmpError.cat/_params.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Templates/dialog/CommonMediaIntent.catfamily/AmpError.cat/en.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Templates/dialog/CommonMediaIntent.catfamily/SomethingHasToBePlaying.cat/_params.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Templates/dialog/CommonMediaIntent.catfamily/SomethingHasToBePlaying.cat/en.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/en/dialog/SocialConversation.catfamily/dalKnockKnockJoke_jokes.cat/en-au.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/fr/dialog/SocialConversation.catfamily/dalWhatAreYouDoing.cat/fr-be.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/Templates/dialog/wellness.catfamily/regionNotSupportedForMeds.cat/nl-be.cat.bin`
- `/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/Localizable-Ratchet.loctable`
- `/System/Library/NanoTimeKit/FaceBundles/NTKRhizomeFaceBundleCompanion.bundle/Info.plist`
- `/System/Library/NanoTimeKit/FaceBundles/NTKRhizomeFaceBundleCompanion.bundle/LocalizableCompanion.loctable`
- `/System/Library/NanoTimeKit/FaceBundles/NTKRhizomeFaceBundleCompanion.bundle/Rhizome.otf`
- `/System/Library/NanoTimeKit/FaceBundles/NTKRhizomeFaceBundleCompanion.bundle/_CodeSignature/CodeResources`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-Custom.bundle/Info.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-Custom.bundle/Personalities/8BitDo/M30/Bluetooth.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-Custom.bundle/Personalities/8BitDo/M30/USB.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-Custom.bundle/Personalities/8BitDo/Micro/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-Custom.bundle/Personalities/8BitDo/NEOGEOGP/Bluetooth.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-Custom.bundle/Personalities/8BitDo/NEOGEOGP/USB.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-Custom.bundle/Personalities/8BitDo/SN30_Pro/v11720_p8449_r256.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-Custom.bundle/Personalities/Backbone/backboneone/MFi.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-Custom.bundle/Personalities/Backbone/backboneone/MFi_Playstation.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-Custom.bundle/Personalities/GameSir/X3/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-Custom.bundle/Personalities/HORI/PlayStation5FightingStickAlpha/PS4Mode.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-Custom.bundle/Personalities/HORI/PlayStation5FightingStickAlpha/PS5Mode.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-Custom.bundle/Personalities/MadCatz/EGOArcadeStick/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-Custom.bundle/Personalities/Mayflash/ArcadeStick/GameConsoleMode.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-Custom.bundle/Personalities/Mayflash/ArcadeStickF101/DInputMode.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-Custom.bundle/Personalities/Mayflash/ArcadeStickF300/DInputMode.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-Custom.bundle/Personalities/Mayflash/ArcadeStickF300Elite/DInputMode.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-Custom.bundle/Personalities/Mayflash/ArcadeStickF500v2/DInputMode.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-Custom.bundle/Personalities/PowerA/moga/Bluetooth.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-Custom.bundle/Personalities/PowerA/moga/USB.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-Custom.bundle/Personalities/Razer/KishiV2/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-Custom.bundle/Personalities/Razer/WolverineV2Pro/Wired.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-Custom.bundle/Personalities/Razer/WolverineV2Pro/Wireless.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-Custom.bundle/Personalities/RotorRiot/RR1800A/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Info.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v10007/p12612/r297/XiaoMi_Game_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v10256/p9/8Bitdo_SFC30_GamePad_Joystick/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1064/p16385/r512/Gravis_Gamepad_Pro/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1103/p45824/Thrustmaster_Firestorm_Dual_Power/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1103/p45845/Thrustmaster_Dual_Analog_3_2/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1103/p53262/r512/ThrustMaster_eSwap_PRO_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1118/p39/r257/Microsoft_SideWinder_Plug_and_Play/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1133/p49686/Logitech_F310_Gamepad_(DInput)/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1133/p49686/r1044/Logitech_Dual_Action/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1133/p49686/r512/Logitech_Dual_Action/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1133/p49686/r768/Logitech_Dual_Action/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1133/p49688/Logitech_F510_Gamepad_(DInput)/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1133/p49688/r256/Logitech_RumblePad_2_USB/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1133/p49689/Logitech_Wireless_Gamepad_(DInput)/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1133/p49689/r773/Logitech_F710_Gamepad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1133/p49695/Logitech_F710_Gamepad_(XInput)/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1149/p16389/r257/Gravis_Eliminator_GamePad_Pro/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p10272/r256/8BitDo_NES30/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p10304/r256/8Bitdo_SN30_GamePad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p10341/r256/8BitDo_N30_Pro_2/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p12306/r256/8BitDo_Ultimate_Wireless_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p12306/r512/8BitDo_Ultimate_Wireless_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p12544/r1/8BitDo_Wireless_Adapter/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p12848/r256/8BitDo_Zero_2/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p14352/r256/8BitDo_FC30_Pro/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p20753/r256/8BitDo_Lite_SE/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p20753/r512/8BitDo_Lite_SE/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p20754/r256/8BitDo_Lite_2/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p20754/r512/8BitDo_Lite_2/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p24577/r1/8BitDo_SN30_Pro/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p24578/r1/8BitDo_SN30_Pro+/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p24582/r256/8BitDo_Pro_2/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p24582/r512/8BitDo_Pro_2/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p24833/r256/8BitDo_SN30_Pro/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p24834/r256/8BitDo_SN30_Pro+/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p36864/r1/8BitDo_FC30_Pro/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p36865/r1/8Bitdo_NES30_Pro/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p36882/r1/8BitDo_SN30_Gamepad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p36885/r1/8BitDo_N30_Pro_2/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p36888/r1/8BitDo_Zero_2/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p43794/r1/8BitDo_NES30/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1204/p266/Sega_Saturn_USB_Gamepad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1204/p9233/Flydigi_Vader_2/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1204/p9234/r1280/Flydigi_Vader_2_Pro/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v12068/p115/r512/Mayflash_Magic_NS/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v12068/p45/r263/JYS_Wireless_Adapter/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v121/p17/Retro_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v121/p17/r261/Retro_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v121/p17/r262/Retrolink_SNES_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v121/p6/r263/Marvo_GT-004/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v121/p6144/Mayflash_WiiU_Pro_Game_Controller_Adapter_(DInput)/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v121/p6144/r256/Mayflash_Wii_U_Pro_Controller_Adapter/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v121/p6212/r256/Mayflash_GameCube_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v121/p6214/r256/GameCube_Controller_Adapter/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v121/p6354/r294/Mayflash_Magic_NS/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1356/p2976/Sony_DualShock_4_Wireless_Adaptor/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1356/p2976/r256/PS4_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1356/p3290/r256/Playstation_Classic_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1356/p4919/r256/PlayStation_Vita/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1356/p616/PS3_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1356/p616/r256/PS3_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1411/p45105/Cideko_AK08b/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1411/p8288/iBuffalo_Gamepad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1411/p8288/r256/Retro_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v14368/p9/r256/8Bitdo_NES30_Pro/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1440/p12850/r264/8Bitdo_Zero_GamePad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1440/p12850/r265/8Bitdo_Zero_GamePad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1519/p3/r512/AxisPad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1699/p63010/r769/Cyborg_V_3_Rumble_Pad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1848/p12880/r256/Mad_Catz_FightPad_PRO_(PS3)/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1848/p13188/r256/Mad_Catz_FightStick_TE_S+_(PS3)/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1848/p33360/r256/Mad_Catz_FightPad_PRO_(PS4)/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1848/p33668/r256/Mad_Catz_FightStick_TE_S+_(PS4)/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1907/p260/r256/Sanwa_PlayOnline_Mobile/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v2007/p64/r257/Flydigi_Vader_2_Pro/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v2064/p1/Twin_USB_Joystick/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v2064/p3/r262/PS2_Adapter/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v2064/p58625/r262/NEXT_SNES_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v2341/p1000/Mayflash_Wii_Classic_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v2342/p34952/r648/Cyber_Gadget_GameCube_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v2389/p29204/r1317/NVIDIA_Controller_v01_04/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v273/p5145/r265/SteelSeries_Stratus_XL/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v2821/p17664/r49/ASUS_Gamepad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v30021/p4386/r256/SZMY_Power_PC_Gamepad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3090/p3600/r256/Zeroplus_P4_Gamepad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3090/p3616/r256/Brook_Mars_PS4_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3090/p3617/r256/Brook_Mars_PS4_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3090/p7696/r256/Zeroplus_P4_Wired_Gamepad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3235/p39/r771/Astro_City_Mini/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3235/p40/r771/Astro_City_Mini/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3695/p1025/Xbox_360_Wired_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3695/p265/r258/PDP_Versus_Fighting_Pad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3695/p513/GameStop_Xbox_360_Wired_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3695/p515/r1061/Victrix_Pro_Fight_Stick_for_PS4/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3695/p519/r1539/Victrix_Pro_Fight_Stick_for_PS4/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3727/p12307/r273/HuiJia_SNES_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3727/p3/Piranha_Xtreme_PS3_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3727/p3/r263/GreenAsia_USB_Joystick/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3727/p3/r265/2In1_USB_Joystick/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p102/Horipad_FPS_Plus_4/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p102/r256/Horipad_4_PS4/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p110/r256/Horipad_4_PS3/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p132/r256/Fighting_Commander/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p133/r256/Fighting_Commander/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p146/r256/Hori_Pokken_Tournament_DX_Pro_Pad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p238/r256/Horipad_Mini_4/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p45/r4096/Hori_Fighting_Commander_3_Pro/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p77/Hori_Gem_Pad_3/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p94/Hori_Fighting_Commander_4_PS4/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p94/r256/Hori_Fighting_Commander_4_PS4/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p95/Hori_Fighting_Commander_4_PS3/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p95/r256/Hori_Fighting_Commander_4_PS3/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v4544/p16385/r256/GameStop_PS4_Fun_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v4661/p43794/r1/8BitDo_NES30_Gamepad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v4661/p43809/SFC30_Joystick/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v4754/p17995/r515/NES_2-port_Adapter/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v4797/p53269/Tomee_SNES_USB_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v4797/p53269/r256/Tomee_Retro_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5227/p3329/r256/Revolution_Pro_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5227/p3347/r256/Revolution_Pro_Controller_3/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5336/p53198/Cthulhu/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5426/p1025/r256/Razer_Panthera_PS4/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5426/p1026/r256/Razer_Panthera_PS3/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5426/p1797/r257/Razer_Raiju_Mobile/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5426/p1799/r256/Razer_Raiju_Mobile/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5426/p2304/r14870/Razer_Serval/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5426/p2304/r512/Razer_Serval/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5426/p2563/Razer_Wildcat/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5426/p4096/r256/Razer_Raiju/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5426/p4103/r257/Razer_Raiju_Tournament_Edition/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5426/p4106/r1/Razer_Raiju_Tournament_Edition/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5426/p4352/r256/Razer_Raion_Fightpad_for_PS4/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5769/p64768/Razer_Onza_TE/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v6017/p1406/Sega_Saturn/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v61440/p241/SNES_RetroPort/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v6353/p37888/r256/Stadia_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v6421/p64/r1/Flydigi_Vader_2/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v6473/p1049/r257/Amazon_Luna_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v7085/p63745/Gamestop_BB070_X360_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v7545/p769/r265/Wii_Classic_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v8194/p36864/r1/8Bitdo_NES30_Pro/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v8406/p25201/r1/Moga_Pro_2_HID/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v8406/p31018/r256/BDA_PS4_Fightpad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v8406/p42768/r259/Mayflash_Magic_NS/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v8406/p42769/r1296/Nintendo_Switch_PowerA_Wired_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v8406/p42769/r512/Nintendo_Switch_Core_Plus_Wired_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v8406/p51821/r256/PowerA_Pro_Ex/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v9414/p21562/Xbox_One_PowerA_Wired_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v9414/p23812/Xbox_360_Wired_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v9414/p35098/r256/BDA_MOGA_XP5-X_Plus/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v9414/p35099/r256/BDA_MOGA_XP5-X_Plus/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v9414/p35114/r256/MOGA_XP5A_Plus/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v9414/p35115/r256/MOGA_XP5A_Plus/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v9414/p64254/Rock_Candy_Gamepad_for_PS3/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/AssetData/GameControllers-SDL.bundle/Personalities/v9571/p1397/r512/NEOGEO_mini_PAD_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/b1b5e6b4e02b5e15a79be4612e2ff0d5d4bebcf5.asset/Info.plist`
- `/System/Library/PrivateFrameworks/AppleAccountUI.framework/Localizable-DTO.loctable`
- `/System/Library/PrivateFrameworks/AuthKit.framework/Localizable-DTO.loctable`
- `/System/Library/PrivateFrameworks/AuthKitUI.framework/Localizable-DTO.loctable`
- `/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI_DTO.loctable`
- `/System/Library/PrivateFrameworks/FindMyDevice.framework/ar.lproj/Localizable-DIMPLEKEY.strings`
- `/System/Library/PrivateFrameworks/FindMyDevice.framework/bg.lproj/Localizable-DIMPLEKEY.strings`
- `/System/Library/PrivateFrameworks/FindMyDevice.framework/ca.lproj/Localizable-DIMPLEKEY.strings`
- `/System/Library/PrivateFrameworks/FindMyDevice.framework/cs.lproj/Localizable-DIMPLEKEY.strings`
- `/System/Library/PrivateFrameworks/FindMyDevice.framework/da.lproj/Localizable-DIMPLEKEY.strings`
- `/System/Library/PrivateFrameworks/FindMyDevice.framework/de.lproj/Localizable-DIMPLEKEY.strings`
- `/System/Library/PrivateFrameworks/FindMyDevice.framework/el.lproj/Localizable-DIMPLEKEY.strings`
- `/System/Library/PrivateFrameworks/FindMyDevice.framework/en.lproj/Localizable-DIMPLEKEY.strings`
- `/System/Library/PrivateFrameworks/FindMyDevice.framework/en_AU.lproj/Localizable-DIMPLEKEY.strings`
- `/System/Library/PrivateFrameworks/FindMyDevice.framework/en_GB.lproj/Localizable-DIMPLEKEY.strings`
- `/System/Library/PrivateFrameworks/FindMyDevice.framework/es.lproj/Localizable-DIMPLEKEY.strings`
- `/System/Library/PrivateFrameworks/FindMyDevice.framework/es_419.lproj/Localizable-DIMPLEKEY.strings`
- `/System/Library/PrivateFrameworks/FindMyDevice.framework/fi.lproj/Localizable-DIMPLEKEY.strings`
- `/System/Library/PrivateFrameworks/FindMyDevice.framework/fr.lproj/Localizable-DIMPLEKEY.strings`
- `/System/Library/PrivateFrameworks/FindMyDevice.framework/fr_CA.lproj/Localizable-DIMPLEKEY.strings`
- `/System/Library/PrivateFrameworks/FindMyDevice.framework/he.lproj/Localizable-DIMPLEKEY.strings`
- `/System/Library/PrivateFrameworks/FindMyDevice.framework/hi.lproj/Localizable-DIMPLEKEY.strings`
- `/System/Library/PrivateFrameworks/FindMyDevice.framework/hr.lproj/Localizable-DIMPLEKEY.strings`
- `/System/Library/PrivateFrameworks/FindMyDevice.framework/hu.lproj/Localizable-DIMPLEKEY.strings`
- `/System/Library/PrivateFrameworks/FindMyDevice.framework/id.lproj/Localizable-DIMPLEKEY.strings`
- `/System/Library/PrivateFrameworks/FindMyDevice.framework/it.lproj/Localizable-DIMPLEKEY.strings`
- `/System/Library/PrivateFrameworks/FindMyDevice.framework/ja.lproj/Localizable-DIMPLEKEY.strings`
- `/System/Library/PrivateFrameworks/FindMyDevice.framework/kk.lproj/Localizable-DIMPLEKEY.strings`
- `/System/Library/PrivateFrameworks/FindMyDevice.framework/ko.lproj/Localizable-DIMPLEKEY.strings`
- `/System/Library/PrivateFrameworks/FindMyDevice.framework/ms.lproj/Localizable-DIMPLEKEY.strings`
- `/System/Library/PrivateFrameworks/FindMyDevice.framework/nl.lproj/Localizable-DIMPLEKEY.strings`
- `/System/Library/PrivateFrameworks/FindMyDevice.framework/no.lproj/Localizable-DIMPLEKEY.strings`
- `/System/Library/PrivateFrameworks/FindMyDevice.framework/pl.lproj/Localizable-DIMPLEKEY.strings`
- `/System/Library/PrivateFrameworks/FindMyDevice.framework/pt_BR.lproj/Localizable-DIMPLEKEY.strings`
- `/System/Library/PrivateFrameworks/FindMyDevice.framework/pt_PT.lproj/Localizable-DIMPLEKEY.strings`
- `/System/Library/PrivateFrameworks/FindMyDevice.framework/ro.lproj/Localizable-DIMPLEKEY.strings`
- `/System/Library/PrivateFrameworks/FindMyDevice.framework/ru.lproj/Localizable-DIMPLEKEY.strings`
- `/System/Library/PrivateFrameworks/FindMyDevice.framework/sk.lproj/Localizable-DIMPLEKEY.strings`
- `/System/Library/PrivateFrameworks/FindMyDevice.framework/sv.lproj/Localizable-DIMPLEKEY.strings`
- `/System/Library/PrivateFrameworks/FindMyDevice.framework/th.lproj/Localizable-DIMPLEKEY.strings`
- `/System/Library/PrivateFrameworks/FindMyDevice.framework/tr.lproj/Localizable-DIMPLEKEY.strings`
- `/System/Library/PrivateFrameworks/FindMyDevice.framework/uk.lproj/Localizable-DIMPLEKEY.strings`
- `/System/Library/PrivateFrameworks/FindMyDevice.framework/vi.lproj/Localizable-DIMPLEKEY.strings`
- `/System/Library/PrivateFrameworks/FindMyDevice.framework/zh_CN.lproj/Localizable-DIMPLEKEY.strings`
- `/System/Library/PrivateFrameworks/FindMyDevice.framework/zh_HK.lproj/Localizable-DIMPLEKEY.strings`
- `/System/Library/PrivateFrameworks/FindMyDevice.framework/zh_TW.lproj/Localizable-DIMPLEKEY.strings`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/TargetConditionals.h`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/metal_array`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/metal_assert`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/metal_atomic`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/metal_command_buffer`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/metal_common`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/metal_compute`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/metal_config`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/metal_curves`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/metal_extended_vector`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/metal_functional`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/metal_geometric`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/metal_graphics`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/metal_imageblocks`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/metal_initializer_list`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/metal_integer`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/metal_interpolate`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/metal_limits`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/metal_math`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/metal_matrix`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/metal_mesh`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/metal_numeric`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/metal_pack`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/metal_packed_vector`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/metal_pixel`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/metal_quadgroup`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/metal_raytracing`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/metal_relational`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/metal_simdgroup`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/metal_simdgroup_matrix`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/metal_stdlib`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/metal_tessellation`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/metal_texture`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/metal_type_traits`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/metal_types`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/metal_types.h`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/metal_uniform`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/metal_utility`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/metal_visible_function_table`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/module.modulemap`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/prebuilt_implicit_modules/27I9H4BEZ5K0Q/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/prebuilt_implicit_modules/2EF8F7LCOETF/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/prebuilt_implicit_modules/2G1VKP7JVP3IH/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/prebuilt_implicit_modules/2HIDJ7ZQLA9TM/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/prebuilt_implicit_modules/2N8MGGUIGF6C5/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/simd/matrix_types.h`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/simd/packed.h`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/simd/simd.h`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/include/metal/simd/vector_types.h`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/lib/darwin/libair_rt_ios.rtlib`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/lib/darwin/libmetal_rt_ios.a`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/lib/darwin/libpost_mesh_dump_rt_ios.rtlib`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/lib/darwin/libresource_tracking_rt_ios.rtlib`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/lib/darwin/libtracepoint_rt_ios.metallib`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/lib/darwin/libtracepoint_rt_static_ios.a`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.116/lib/darwin/libtracepoint_rt_workaround_ios.a`
- `/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/Localizable-Ratchet.loctable`
- `/System/Library/PrivateFrameworks/LocalAuthenticationCoreUI.framework/Localizable-Ratchet.loctable`
- `/System/Library/PrivateFrameworks/PodcastsFoundation.framework/MTLibrary.momd/MTLibrary 134.mom`
- `/System/Library/PrivateFrameworks/PodcastsFoundation.framework/MTLibrary.momd/MTLibrary 135.mom`
- `/System/Library/PrivateFrameworks/PodcastsFoundation.framework/MTLibrary.momd/MTLibrary 135.omo`
- `/System/Library/PrivateFrameworks/PreferencesUI.framework/PasscodeLock-DimpleKey.loctable`
- `/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePluginClassB.appex/assets_1544/recipe.json`
- `/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePluginClassB.appex/assets_841/recipe.json`
- `/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePluginClassB.appex/com.apple.Trial.NamespaceDescriptor.1544.plist`
- `/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePluginClassB.appex/com.apple.Trial.NamespaceDescriptor.841.plist`
- `/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePluginClassB.appex/default_factors_1544.pb`
- `/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePluginClassB.appex/default_factors_841.pb`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonResponses.catfamily/UnlockDeviceSegue.cat/en-za.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonResponses.catfamily/UnlockDeviceSegue.cat/nl-be.cat.bin`
- `/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/RhizomePoster.appex/Entitlements.plist`
- `/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/RhizomePoster.appex/Info.plist`
- `/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/RhizomePoster.appex/InfoPlist.loctable`
- `/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/RhizomePoster.appex/Localizable.loctable`
- `/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/RhizomePoster.appex/Rhizome.otf`
- `/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/RhizomePoster.appex/RhizomePoster`
- `/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/RhizomePoster.appex/_CodeSignature/CodeResources`
- `/private/var/staged_system_apps/Books.app/PlugIns/BooksSpotlightExtension.appex`
- `/private/var/staged_system_apps/Books.app/PlugIns/BooksSpotlightExtension.appex/BooksSpotlightExtension`
- `/private/var/staged_system_apps/Books.app/PlugIns/BooksSpotlightExtension.appex/Info.plist`
- `/private/var/staged_system_apps/Books.app/PlugIns/BooksSpotlightExtension.appex/_CodeSignature`
- `/private/var/staged_system_apps/Books.app/PlugIns/BooksSpotlightExtension.appex/_CodeSignature/CodeResources`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/ar_SA.c04f26495e2f3a0457808c2f06899e81.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/da_DK.49ba3775ede0a7ef6d8502400b7a0a23.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/de_DE.f9dcb87cfdeea5892257cb5dbddec1a8.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/en_AU.944bc92c0a7d60a58758b5afa1c87334.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/en_GB.29c3d0ea3c65c6ad6cb7934e18b2c7d2.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/en_US.cef424c41da00a9023f54c69cdd9fc47.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/es_ES.2d96183e8d208981f8d97d41f80b083d.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/es_MX.fa60cb2c0698b4a8d7e891cef23babf0.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/fi_FI.e5d655476c003403eb3adbbd05019044.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/fr_CA.750c603a6ecc4af5df3eddcceeca8972.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/fr_FR.6524e8d19bb9cb75e0a58ca36c07c2e2.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/he_IL.1e3e9312b7037b7ebb4ba84bf9dfd47e.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/it_IT.1c3f2ff0035c805a8b8fab2dfee8fb05.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/ja_JP.945296e8e43716da6f52aee884b2fdc2.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/ko_KR.27167adba4e0792613a071b345accde1.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/ms_MY.4e9b4ac26e93df25ae678afd29586c56.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/nl_NL.fdba1f04971d8377949be55fb2f9838c.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/pt_BR.2a74e4f6b3c1573b5b07813bd7406521.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/ru_RU.e1848967d56872f81e249da0b5ff7810.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/sv_SE.50a1b4b815bd60b8e16674156e4cb3c0.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/th_TH.7dca4c942c5670cf625de48d31fb5d2b.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/tr_TR.a5e68b8e06861445a1d4ca0d764c1f85.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/zh_CN.0a2ed5b4cb442a1fbe8eb95c219ae52d.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/zh_HK.028b49229b8d76464e737932dc94207c.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/zh_TW.f00c429f9cd55ed5e26e81ab565ec3f8.version`
- `/private/var/staged_system_apps/FindMy.app/Localizable-DIMPLEKEY.loctable`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/ar_SA.a643ac2542c2aed2188d160f58d118e4.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/da_DK.48d1c46c33fe09fac5f477aa3fafde30.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/de_DE.465111a61e04d131059fdb08813ac7cd.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/en_AU.434a6042b29d9bfdad8ecbbc1f91ee16.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/en_GB.ab67296097480d29375f097fe5e32036.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/en_IN.d128c3b010cc0b7fcc0d2be27a2f33db.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/en_US.ee63e8379779f6f7c9f7b9ea4fc3d364.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/es_ES.f14b08c34a68877b5a5f9759f23ceda1.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/es_MX.3e84768caab4da62469de8ce607779b8.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/fi_FI.1bb87a940a2cee300cd2d3d2d31a461d.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/fr_CA.b3406b66e1eb68bca85b7ff71be60b66.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/fr_FR.d6669952e92ed7ce7c5e4f906c7a5b7f.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/he_IL.63162e9b3692b66de460dc256b997247.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/it_IT.95ad2a6c9e123ecf5322c09c034024b1.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/ja_JP.d810e7ad82c4ca29f59f548b4b8f7168.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/ko_KR.01dafc0cc7fdc8736ef537680ebb6e9e.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/ms_MY.699993b374f4c9291ae2e06ab2b7e56f.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/nl_NL.31629d7f7708e8c553ddccdf25d04840.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/pt_BR.8599118ccd9cd0c8ae5edd5cb786cff7.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/ru_RU.e357232be79f129c705d7d92576ff5ee.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/sv_SE.9b4b0c4520260fffa0cb1f55f9613586.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/th_TH.8e15b8d669b07193cc25adf0682b05e1.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/tr_TR.3a526014ebf425ba234ec514653a70a7.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/zh_CN.d67f46cc3477a8dc26e52e7c277b5bcf.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/zh_HK.9c37b5b2f49ee984c2bb4b151dd57496.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/zh_TW.12266e94d637cb90b2d5e4263592040d.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/ar_SA.ab550ec6eeaec91b0da3cc4c4e21744a.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/da_DK.6a99f0684fac00ac04a47b591dbfc84d.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/de_DE.623b105c786ba43cec130f4085d39f18.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/en_AU.c2e349a18cafe657a38b634f81a9896d.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/en_GB.baa972c4143ca2423293a833673de9de.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/en_US.0345f739ed3eced82e8bd4715ac62444.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/es_ES.4c355ecc590cb07077a0c53283ac073e.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/es_MX.b596af2b4a17090c039a234e212b6168.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/fi_FI.8618b86ca0180ec75247c16e515449db.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/fr_CA.56bcece1bcbd602163dc5782b4c4294d.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/fr_FR.09342a8b460128cd3995298aa84c8aa8.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/he_IL.8db356c4169a93439e794734c6155a0c.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/it_IT.c8de24e7eb89cb10e553cc9c9a10007b.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/ja_JP.d377f13eac59a357fa29a050f0a0b52d.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/ko_KR.d7f1ecf16dde18441c6bfda94c5acb5d.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/ms_MY.949b703c5a64d451b47cebec6ece3452.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/nl_NL.9fb17d52e7f06f0211c63d986f82952f.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/pt_BR.3b3c17dc7f3c63b724e91738849b03b4.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/ru_RU.53a71decf88e0da262af38801599a784.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/sv_SE.b894f0da00ec8d5ed49cf37db01ff9da.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/th_TH.da05d590ddfe56a3c9361a0205372900.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/tr_TR.d1cdd98aa4a029778cb03c41ac08fc65.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/zh_CN.78a63b49e53766405c9323f9b910fe26.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/zh_HK.7ed2c7374f79ac9a017b553b0f21c3a9.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/zh_TW.e35ad372d3ad0f70f81fab8b28158719.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/ar_SA.458c1f4cc6b38ea34ec675c0b3b1bfee.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/da_DK.ad27e89846e38093069382c717a45362.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/de_DE.9a2ea24c7bd8ede9d690f12b5e6b8200.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/en_AU.035cff48c3bbfd9e13014867f050998d.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/en_GB.0236192b228b639af2645fbce522c565.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/en_US.eae56d787cdc448425b83835658e3563.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/es_ES.9f154ff29cec1f36f269ae493c00e47c.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/es_MX.0bcbb7529a19646a8a86780e580d4ac9.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/fi_FI.7ec2a36e24d2f2832dece03865845deb.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/fr_CA.b559b595d8ee41c93a506423a3970006.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/fr_FR.c36e5835f937d99c6bfca7e4de04055e.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/he_IL.65bc02ddf69bd104d8ae3ae2eabb050a.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/it_IT.d29cf7396442a8c3717212ecb01045c1.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/ja_JP.933957da676db8247d587e395b6eb58e.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/ko_KR.0bd36485a0391b1887588c77c3236cd0.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/ms_MY.d0dc46ed77b38cc36a29f644119b5373.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/nl_NL.e7e5035288830e341dba19023e41c149.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/pt_BR.56c5a1c64f91091c98c953c765f1d8c4.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/ru_RU.cf8b0beaee49ac39c30958ac4494a257.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/sv_SE.b818f50577c4cc0e826219b26b719fed.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/th_TH.5e0ab53910a64957c0f0ac7a1c0dea4a.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/tr_TR.cb6fb41981247dad8e66dcb10325557c.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/zh_CN.2c14fee6c684de4f3c0f3d1672b11668.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/zh_HK.8a9fa32d76052c8c94621d50415cd32c.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/zh_TW.9ddd24c22523a34297741a206a0b25fa.version`
- `/usr/share/kpep/a10.plist`
- `/usr/share/kpep/a11.plist`
- `/usr/share/kpep/a12.plist`
- `/usr/share/kpep/a13.plist`
- `/usr/share/kpep/a14.plist`
- `/usr/share/kpep/a15.plist`
- `/usr/share/kpep/a16.plist`
- `/usr/share/kpep/a7.plist`
- `/usr/share/kpep/a8.plist`
- `/usr/share/kpep/a9.plist`
- `/usr/share/kpep/as1.plist`
- `/usr/share/kpep/as2.plist`
- `/usr/share/kpep/as3.plist`

</details>

#### SystemOS (8)

- `/System/Library/Caches/com.apple.dyld/dyld_shared_cache_arm64e.27`
- `/System/Library/Caches/com.apple.dyld/dyld_shared_cache_arm64e.28`
- `/System/Library/Caches/com.apple.dyld/dyld_shared_cache_arm64e.29.dylddata`
- `/System/Library/Caches/com.apple.dyld/dyld_shared_cache_arm64e.30.dyldlinkedit`
- `/System/Library/Caches/com.apple.dyld/dyld_shared_cache_arm64e.51`
- `/System/Library/Caches/com.apple.dyld/dyld_shared_cache_arm64e.52`
- `/System/Library/Caches/com.apple.dyld/dyld_shared_cache_arm64e.53.dylddata`
- `/System/Library/Caches/com.apple.dyld/dyld_shared_cache_arm64e.54.dyldlinkedit`

### ❌ Removed

#### IPSW (2)

- `Firmware/Mav23-1.22.05.Release.bbfw`
- `Firmware/Mav23-1.22.05.Release.plist`

#### filesystem (385)

<details>
  <summary><i>View Files</i></summary>

- `/Applications/GameCenterWidgets.app/Base.lproj/LaunchScreen.storyboardc/01J-lp-oVM-view-Ze5-6b-2t3.nib`
- `/Applications/GameCenterWidgets.app/Base.lproj/LaunchScreen.storyboardc/Info.plist`
- `/Applications/GameCenterWidgets.app/Base.lproj/LaunchScreen.storyboardc/UIViewController-01J-lp-oVM.nib`
- `/Applications/GameCenterWidgets.app/Base.lproj/Main.storyboardc/BYZ-38-t0r-view-8bC-Xf-vdC.nib`
- `/Applications/GameCenterWidgets.app/Base.lproj/Main.storyboardc/Info.plist`
- `/Applications/GameCenterWidgets.app/Base.lproj/Main.storyboardc/UIViewController-BYZ-38-t0r.nib`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Templates/dialog/AddMediaIntent.catfamily/UnsupportedMediaItemsAlreadyInLibrary.cat/de-ch.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Templates/dialog/PlayMediaIntent.catfamily/PlayEditorialPlaylist.cat/de-ch.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Templates/dialog/PlayMediaIntent.catfamily/SwitchNewsSourcePreferenceMediaAPICallError.cat/fr-ca.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/ClockFlowPlugin.bundle/Templates/dialog/TimeSuggestions.catfamily/whatIsTodaysDate.cat/nl-be.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/HomeCommunicationFlowDelegatePlugin.bundle/Templates/manifest.pb`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/es/dialog/SocialConversation.catfamily/dalChineseNewYearGreetings.cat/es-cl.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/es/dialog/SocialConversation.catfamily/dalChineseNewYearGreetings.cat/es-us.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/es/dialog/SocialConversation.catfamily/dalLunarNewYearGreetings.cat/es-cl.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/es/dialog/SocialConversation.catfamily/dalLunarNewYearGreetings.cat/es-us.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/tr/manifest.pb`
- `/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/Templates/dialog/wellness.catfamily/regionNotSupported.cat/nl-be.cat.bin`
- `/System/Library/CacheDelete/com.apple.assetsd.special.CacheDelete.plist`
- `/System/Library/HIDPlugins/ServicePlugins/ApplePencilDMServicePlugin.plugin/ApplePencilDMServicePlugin`
- `/System/Library/HIDPlugins/ServicePlugins/ApplePencilDMServicePlugin.plugin/Info.plist`
- `/System/Library/HIDPlugins/ServicePlugins/ApplePencilDMServicePlugin.plugin/_CodeSignature/CodeResources`
- `/System/Library/HIDPlugins/SessionFilters/ApplePencilSessionFilter.plugin/ApplePencilSessionFilter`
- `/System/Library/HIDPlugins/SessionFilters/ApplePencilSessionFilter.plugin/Info.plist`
- `/System/Library/HIDPlugins/SessionFilters/ApplePencilSessionFilter.plugin/_CodeSignature/CodeResources`
- `/System/Library/OnBoardingBundles/com.apple.onboarding.bifrost.bundle/Bifrost.loctable`
- `/System/Library/OnBoardingBundles/com.apple.onboarding.bifrost.bundle/Bifrost.plist`
- `/System/Library/OnBoardingBundles/com.apple.onboarding.bifrost.bundle/Info.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-Custom.bundle/Info.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-Custom.bundle/Personalities/8BitDo/M30/Bluetooth.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-Custom.bundle/Personalities/8BitDo/M30/USB.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-Custom.bundle/Personalities/8BitDo/NEOGEOGP/Bluetooth.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-Custom.bundle/Personalities/8BitDo/NEOGEOGP/USB.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-Custom.bundle/Personalities/8BitDo/SN30_Pro/v11720_p8449_r256.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-Custom.bundle/Personalities/Backbone/backboneone/MFi.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-Custom.bundle/Personalities/Backbone/backboneone/MFi_Playstation.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-Custom.bundle/Personalities/GameSir/X3/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-Custom.bundle/Personalities/HORI/PlayStation5FightingStickAlpha/PS4Mode.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-Custom.bundle/Personalities/HORI/PlayStation5FightingStickAlpha/PS5Mode.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-Custom.bundle/Personalities/MadCatz/EGOArcadeStick/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-Custom.bundle/Personalities/Mayflash/ArcadeStick/GameConsoleMode.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-Custom.bundle/Personalities/Mayflash/ArcadeStickF101/DInputMode.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-Custom.bundle/Personalities/Mayflash/ArcadeStickF300/DInputMode.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-Custom.bundle/Personalities/Mayflash/ArcadeStickF300Elite/DInputMode.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-Custom.bundle/Personalities/Mayflash/ArcadeStickF500v2/DInputMode.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-Custom.bundle/Personalities/PowerA/moga/Bluetooth.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-Custom.bundle/Personalities/PowerA/moga/USB.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-Custom.bundle/Personalities/Razer/KishiV2/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-Custom.bundle/Personalities/Razer/WolverineV2Pro/Wired.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-Custom.bundle/Personalities/Razer/WolverineV2Pro/Wireless.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-Custom.bundle/Personalities/RotorRiot/RR1800A/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Info.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v10007/p12612/r297/XiaoMi_Game_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v10256/p9/8Bitdo_SFC30_GamePad_Joystick/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1064/p16385/r512/Gravis_Gamepad_Pro/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1103/p45824/Thrustmaster_Firestorm_Dual_Power/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1103/p45845/Thrustmaster_Dual_Analog_3_2/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1103/p53262/r512/ThrustMaster_eSwap_PRO_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1118/p39/r257/Microsoft_SideWinder_Plug_and_Play/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1133/p49686/Logitech_F310_Gamepad_(DInput)/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1133/p49686/r1044/Logitech_Dual_Action/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1133/p49686/r512/Logitech_Dual_Action/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1133/p49686/r768/Logitech_Dual_Action/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1133/p49688/Logitech_F510_Gamepad_(DInput)/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1133/p49688/r256/Logitech_RumblePad_2_USB/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1133/p49689/Logitech_Wireless_Gamepad_(DInput)/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1133/p49689/r773/Logitech_F710_Gamepad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1133/p49695/Logitech_F710_Gamepad_(XInput)/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1149/p16389/r257/Gravis_Eliminator_GamePad_Pro/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p10272/r256/8BitDo_NES30/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p10304/r256/8Bitdo_SN30_GamePad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p10341/r256/8BitDo_N30_Pro_2/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p12306/r256/8BitDo_Ultimate_Wireless_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p12306/r512/8BitDo_Ultimate_Wireless_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p12544/r1/8BitDo_Wireless_Adapter/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p12848/r256/8BitDo_Zero_2/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p14352/r256/8BitDo_FC30_Pro/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p20753/r256/8BitDo_Lite_SE/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p20753/r512/8BitDo_Lite_SE/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p20754/r256/8BitDo_Lite_2/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p20754/r512/8BitDo_Lite_2/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p24577/r1/8BitDo_SN30_Pro/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p24578/r1/8BitDo_SN30_Pro+/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p24582/r256/8BitDo_Pro_2/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p24582/r512/8BitDo_Pro_2/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p24833/r256/8BitDo_SN30_Pro/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p24834/r256/8BitDo_SN30_Pro+/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p36864/r1/8BitDo_FC30_Pro/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p36865/r1/8Bitdo_NES30_Pro/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p36882/r1/8BitDo_SN30_Gamepad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p36885/r1/8BitDo_N30_Pro_2/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p36888/r1/8BitDo_Zero_2/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p43794/r1/8BitDo_NES30/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1204/p266/Sega_Saturn_USB_Gamepad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1204/p9233/Flydigi_Vader_2/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1204/p9234/r1280/Flydigi_Vader_2_Pro/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v12068/p115/r512/Mayflash_Magic_NS/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v12068/p45/r263/JYS_Wireless_Adapter/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v121/p17/Retro_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v121/p17/r261/Retro_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v121/p17/r262/Retrolink_SNES_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v121/p6/r263/Marvo_GT-004/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v121/p6144/Mayflash_WiiU_Pro_Game_Controller_Adapter_(DInput)/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v121/p6144/r256/Mayflash_Wii_U_Pro_Controller_Adapter/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v121/p6212/r256/Mayflash_GameCube_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v121/p6214/r256/GameCube_Controller_Adapter/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v121/p6354/r294/Mayflash_Magic_NS/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1356/p2976/Sony_DualShock_4_Wireless_Adaptor/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1356/p2976/r256/PS4_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1356/p3290/r256/Playstation_Classic_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1356/p4919/r256/PlayStation_Vita/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1356/p616/PS3_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1356/p616/r256/PS3_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1411/p45105/Cideko_AK08b/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1411/p8288/iBuffalo_Gamepad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1411/p8288/r256/Retro_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v14368/p9/r256/8Bitdo_NES30_Pro/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1440/p12850/r264/8Bitdo_Zero_GamePad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1440/p12850/r265/8Bitdo_Zero_GamePad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1519/p3/r512/AxisPad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1699/p63010/r769/Cyborg_V_3_Rumble_Pad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1848/p12880/r256/Mad_Catz_FightPad_PRO_(PS3)/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1848/p13188/r256/Mad_Catz_FightStick_TE_S+_(PS3)/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1848/p33360/r256/Mad_Catz_FightPad_PRO_(PS4)/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1848/p33668/r256/Mad_Catz_FightStick_TE_S+_(PS4)/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1907/p260/r256/Sanwa_PlayOnline_Mobile/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v2007/p64/r257/Flydigi_Vader_2_Pro/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v2064/p1/Twin_USB_Joystick/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v2064/p3/r262/PS2_Adapter/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v2064/p58625/r262/NEXT_SNES_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v2341/p1000/Mayflash_Wii_Classic_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v2342/p34952/r648/Cyber_Gadget_GameCube_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v2389/p29204/r1317/NVIDIA_Controller_v01_04/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v273/p5145/r265/SteelSeries_Stratus_XL/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v2821/p17664/r49/ASUS_Gamepad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v30021/p4386/r256/SZMY_Power_PC_Gamepad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3090/p3600/r256/Zeroplus_P4_Gamepad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3090/p3616/r256/Brook_Mars_PS4_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3090/p3617/r256/Brook_Mars_PS4_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3090/p7696/r256/Zeroplus_P4_Wired_Gamepad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3235/p39/r771/Astro_City_Mini/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3235/p40/r771/Astro_City_Mini/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3695/p1025/Xbox_360_Wired_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3695/p265/r258/PDP_Versus_Fighting_Pad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3695/p513/GameStop_Xbox_360_Wired_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3695/p515/r1061/Victrix_Pro_Fight_Stick_for_PS4/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3695/p519/r1539/Victrix_Pro_Fight_Stick_for_PS4/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3727/p12307/r273/HuiJia_SNES_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3727/p3/Piranha_Xtreme_PS3_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3727/p3/r263/GreenAsia_USB_Joystick/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3727/p3/r265/2In1_USB_Joystick/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p102/Horipad_FPS_Plus_4/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p102/r256/Horipad_4_PS4/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p110/r256/Horipad_4_PS3/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p132/r256/Fighting_Commander/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p133/r256/Fighting_Commander/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p146/r256/Hori_Pokken_Tournament_DX_Pro_Pad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p238/r256/Horipad_Mini_4/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p45/r4096/Hori_Fighting_Commander_3_Pro/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p77/Hori_Gem_Pad_3/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p94/Hori_Fighting_Commander_4_PS4/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p94/r256/Hori_Fighting_Commander_4_PS4/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p95/Hori_Fighting_Commander_4_PS3/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p95/r256/Hori_Fighting_Commander_4_PS3/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v4544/p16385/r256/GameStop_PS4_Fun_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v4661/p43794/r1/8BitDo_NES30_Gamepad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v4661/p43809/SFC30_Joystick/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v4754/p17995/r515/NES_2-port_Adapter/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v4797/p53269/Tomee_SNES_USB_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v4797/p53269/r256/Tomee_Retro_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5227/p3329/r256/Revolution_Pro_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5227/p3347/r256/Revolution_Pro_Controller_3/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5336/p53198/Cthulhu/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5426/p1025/r256/Razer_Panthera_PS4/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5426/p1026/r256/Razer_Panthera_PS3/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5426/p1797/r257/Razer_Raiju_Mobile/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5426/p1799/r256/Razer_Raiju_Mobile/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5426/p2304/r14870/Razer_Serval/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5426/p2304/r512/Razer_Serval/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5426/p2563/Razer_Wildcat/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5426/p4096/r256/Razer_Raiju/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5426/p4103/r257/Razer_Raiju_Tournament_Edition/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5426/p4106/r1/Razer_Raiju_Tournament_Edition/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5426/p4352/r256/Razer_Raion_Fightpad_for_PS4/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5769/p64768/Razer_Onza_TE/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v6017/p1406/Sega_Saturn/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v61440/p241/SNES_RetroPort/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v6353/p37888/r256/Stadia_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v6421/p64/r1/Flydigi_Vader_2/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v6473/p1049/r257/Amazon_Luna_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v7085/p63745/Gamestop_BB070_X360_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v7545/p769/r265/Wii_Classic_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v8194/p36864/r1/8Bitdo_NES30_Pro/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v8406/p25201/r1/Moga_Pro_2_HID/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v8406/p31018/r256/BDA_PS4_Fightpad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v8406/p42768/r259/Mayflash_Magic_NS/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v8406/p42769/r1296/Nintendo_Switch_PowerA_Wired_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v8406/p42769/r512/Nintendo_Switch_Core_Plus_Wired_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v8406/p51821/r256/PowerA_Pro_Ex/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v9414/p21562/Xbox_One_PowerA_Wired_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v9414/p23812/Xbox_360_Wired_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v9414/p35098/r256/BDA_MOGA_XP5-X_Plus/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v9414/p35099/r256/BDA_MOGA_XP5-X_Plus/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v9414/p35114/r256/MOGA_XP5A_Plus/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v9414/p35115/r256/MOGA_XP5A_Plus/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v9414/p64254/Rock_Candy_Gamepad_for_PS3/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/AssetData/GameControllers-SDL.bundle/Personalities/v9571/p1397/r512/NEOGEO_mini_PAD_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/f6f9d98c130344fed5034ae32d778a14d3ad03c3.asset/Info.plist`
- `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/AirPlayDiagnosticExtension.appex/AirPlayDiagnosticExtension`
- `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/AirPlayDiagnosticExtension.appex/Info.plist`
- `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/AirPlayDiagnosticExtension.appex/_CodeSignature/CodeResources`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/TargetConditionals.h`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/metal_array`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/metal_assert`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/metal_atomic`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/metal_command_buffer`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/metal_common`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/metal_compute`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/metal_config`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/metal_curves`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/metal_extended_vector`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/metal_functional`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/metal_geometric`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/metal_graphics`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/metal_imageblocks`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/metal_initializer_list`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/metal_integer`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/metal_interpolate`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/metal_limits`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/metal_math`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/metal_matrix`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/metal_mesh`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/metal_numeric`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/metal_pack`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/metal_packed_vector`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/metal_pixel`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/metal_quadgroup`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/metal_raytracing`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/metal_relational`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/metal_simdgroup`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/metal_simdgroup_matrix`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/metal_stdlib`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/metal_tessellation`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/metal_texture`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/metal_type_traits`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/metal_types`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/metal_types.h`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/metal_uniform`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/metal_utility`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/metal_visible_function_table`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/module.modulemap`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/prebuilt_implicit_modules/1I7OTA7ODIPX0/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/prebuilt_implicit_modules/2GTEXXAD1KU31/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/prebuilt_implicit_modules/2JEEXSWHU8FR6/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/prebuilt_implicit_modules/3E471V3ECZV34/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/prebuilt_implicit_modules/3KAHUPKD930XA/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/simd/matrix_types.h`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/simd/packed.h`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/simd/simd.h`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/include/metal/simd/vector_types.h`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/lib/darwin/libair_rt_ios.rtlib`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/lib/darwin/libmetal_rt_ios.a`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/lib/darwin/libpost_mesh_dump_rt_ios.rtlib`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/lib/darwin/libresource_tracking_rt_ios.rtlib`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/lib/darwin/libtracepoint_rt_ios.metallib`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/lib/darwin/libtracepoint_rt_static_ios.a`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.98/lib/darwin/libtracepoint_rt_workaround_ios.a`
- `/System/Library/PrivateFrameworks/HearingTest.framework/Info.plist`
- `/System/Library/PrivateFrameworks/HearingTest.framework/_CodeSignature/CodeResources`
- `/System/Library/PrivateFrameworks/PodcastsFoundation.framework/MTLibrary.momd/MTLibrary 133.omo`
- `/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePlugin.appex/assets_1544/recipe.json`
- `/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePlugin.appex/assets_841/recipe.json`
- `/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePlugin.appex/com.apple.Trial.NamespaceDescriptor.1544.plist`
- `/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePlugin.appex/com.apple.Trial.NamespaceDescriptor.841.plist`
- `/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePlugin.appex/default_factors_1544.pb`
- `/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePlugin.appex/default_factors_841.pb`
- `/System/Library/PrivateFrameworks/RequestDispatcherBridges.framework/Templates/manifest.pb`
- `/System/Library/PrivateFrameworks/SiriAppLaunchIntents.framework/Templates/dialog/LaunchApp.catfamily/LaunchedApp.cat/fr-be.cat.bin`
- `/System/Library/PrivateFrameworks/SiriAppLaunchIntents.framework/Templates/dialog/LaunchApp.catfamily/LaunchedApp.cat/fr-ch.cat.bin`
- `/System/Library/PrivateFrameworks/SiriCalendarIntents.framework/Templates/dialog/FindEvents.catfamily/ResultSetSingle.cat/de-at.cat.bin`
- `/System/Library/PrivateFrameworks/SiriInferenceFlow.framework/Templates/dialog/ContactsCommon.catfamily/UnsupportedInvalidUserLocation.cat/en-nz.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonResponses.catfamily/UnlockDeviceSegue.cat/en-nz.cat.bin`
- `/System/Library/PrivateFrameworks/SiriMailInternal.framework/Templates/manifest.pb`
- `/System/Library/PrivateFrameworks/SiriNaturalLanguageGeneration.framework/Templates/manifest.pb`
- `/System/Library/PrivateFrameworks/SiriTranslationIntents.framework/Templates/manifest.pb`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/ar_SA.04cb63715921bb4562770b89c3b0943b.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/da_DK.6fa6e3eff956b96ddadf9352a484ff2f.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/de_DE.884831b13bf7e5f64ed23afeb283ff55.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/en_AU.ef4ffa73c44f5e55ec85cbe22ec2fe69.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/en_GB.c31cd4d6f7dc02a3e8df1bd01288c146.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/en_US.ad4fd06f42dcc58fc6eb510d6cef8882.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/es_ES.10561c61b2bcc91390116bf7033c48f2.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/es_MX.8018ea772262566744da7b188ef7c017.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/fi_FI.66459b3220e2c591bbca00e0fd579b50.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/fr_CA.9f2166e477ee74f29b1ecae555cd4751.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/fr_FR.1cfe868ad9758dc8f672f76909138e66.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/he_IL.3c94f236a61e0703f5e07eceb2d06b38.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/it_IT.8cd5cd2ca055a59fe45d63a595afe992.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/ja_JP.0995042986c7b725b2b5b290c2a21332.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/ko_KR.2374fea3b26b62b09a6881483eed7f64.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/ms_MY.697c21b4a4fc8cc98553f5f2c9fd8ad1.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/nl_NL.a8392eb85d14558c32c6eddcc43e1b1b.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/pt_BR.6d58d660d81dc070a7b958fe9c4c3a95.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/ru_RU.08979b19b9bf726bb10cc7158ce15f3c.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/sv_SE.d95cf4bad8b9459aa8660c0c55c7e7c5.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/th_TH.36441d55a587fa4f4161ab9252345573.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/tr_TR.b9c8717b5009cd8fa17be8e381bab45d.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/zh_CN.1353bd1db29cd4d9d27d38189e77ec8c.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/zh_HK.13537d134623a09d12b942a395d6ed14.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/zh_TW.75862da3b1436d98af565b457fbdd262.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/ar_SA.3be6eea4febe18b91c66f300fe34568a.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/da_DK.9805b59eb282ffcc37e0b04a87dc9709.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/de_DE.c98766ccda73238aaa53e833a05b95f4.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/en_AU.af716db7210950bcd65838e060617e91.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/en_GB.5c6df897972e0fee7cdc8af513ccade3.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/en_IN.a1bca3670a26e317f346e491b01363f5.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/en_US.0fe8d2b92e7647c9f92190db5ffb1703.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/es_ES.3d86238780c3088e390854cda53591bc.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/es_MX.c7e0654df47a8c85f1fdfaac0f63f94b.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/fi_FI.52ebee9adb6b5e668888cbd34f0f03a3.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/fr_CA.70fc2eb1c96fe2ae90597de6871b1846.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/fr_FR.dbe4dd3b1b2801543a26a8d8795ae96e.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/he_IL.4570ab88a24fafba68600cef524de7e7.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/it_IT.81ed959943eb7f18225358012a0fbff4.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/ja_JP.6ecb84248b9b412163a0724459d6ca94.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/ko_KR.6ca8b4e2160b4ddac1df65b11af88b0e.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/ms_MY.adbb32943c100cc4b109bd48be81cbac.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/nl_NL.0cec6c1042605d8ecd078afe55e0eba4.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/pt_BR.5cc31d55b3742730365c78f6da0304a9.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/ru_RU.8aeb8b6c8b8da36a45885c50b8e1cb84.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/sv_SE.530b7d4e738360b86aaca5bcd19ec8f8.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/th_TH.efdb50fd9e50e2e553e6d501f3c28008.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/tr_TR.4fb2faaad3675ab75b27f247efd19030.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/zh_CN.0bd6d29f55378d623ad61850addaf125.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/zh_HK.a0a3dfdecd90e7fde04aa036b1e77aa8.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/zh_TW.ce398edd522cc0fc6441a77c97b45e6b.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/ar_SA.3a599c7d12a829ebb4eb3f2184a00afd.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/da_DK.a35baadf4e6aef44bb689f8924b50762.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/de_DE.0f34d9eb9c03033277e4d0a2c3a3db7a.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/en_AU.11f0febd1f4f42e1709f3a4be5cc2e9d.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/en_GB.9a420d1edaa359b126fc993c39a59c09.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/en_US.f7337fbda76356c4b762c54df878c3da.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/es_ES.104d7a9d1e964ed0945b62570997d677.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/es_MX.93bf50b7263f07b1ce3578897711a325.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/fi_FI.a4498a8f22106c9c7ba883a6c8786568.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/fr_CA.0f725c429c155b084a047dd473b03bfa.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/fr_FR.bb7d8655f02249734d3020c2fdec4ff9.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/he_IL.11b191ec83383796d4354b7c84e1e86f.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/it_IT.8bede2c3b25c3a7653c0ab204b331d1d.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/ja_JP.e8db6f8a8d124d827f210a71663e0c97.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/ko_KR.eca756b2b7e4d0b9f2e29089fdd8166f.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/ms_MY.2f331416944f49f9b684f75a82f034f3.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/nl_NL.c7695376910757d14095ad312252102e.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/pt_BR.e3802573f3252965dd66abbbc5d4c6e6.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/ru_RU.de65aaaf5a917bad2202b16d79a07c7b.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/sv_SE.36e36177858e0f16ffb044064b7bb27d.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/th_TH.ab30c64864ca7611a5d3018517b37f91.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/tr_TR.79f987bf63e048a739066800d9319ab1.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/zh_CN.6ce448584b2872bbc1577e10bbfe68e3.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/zh_HK.43da4146b88ef2f7fecbcdff06f51c31.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/zh_TW.a6332d24b6223eaab0b658f29f0a18fe.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/ar_SA.e83a28202302a9bef48fe72400e158bf.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/da_DK.a2e6ea8ad762b641d3d78a76891febcf.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/de_DE.08b6ab821a62e6be004ad5719f92ee29.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/en_AU.bf5e503adf29ca698ca0d532064b6847.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/en_GB.8209d237dd9f68d3c7b69150b1602ce7.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/en_US.1461bf38e32151c2c366926c5b868ad9.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/es_ES.4b8d6f6d8b389d8d62cf2620fb6b0eb5.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/es_MX.979f7f4d3b26f39956f2a40fa0898bfa.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/fi_FI.f9e8702c9977e1706253e505fda2a23c.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/fr_CA.9b873378abd5ee45fd92b6063cd63ac8.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/fr_FR.be1f0bb94811bfadb3f0cf7914c87466.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/he_IL.61eba2fbd76b219b7e55f92a7ed72f5d.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/it_IT.3dfabacac293de7bbd45039bbdd7842f.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/ja_JP.b0fe31f7929476e67905fb1a9634b8df.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/ko_KR.7f50d565e5ce4fc967bcc52424badd6c.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/ms_MY.135bd6ec7a6f407c5a032cfa73850048.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/nl_NL.96166c9cf7f1e6c9caf62bd8219f6811.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/pt_BR.5cc44ffbfe233c23ceb63f3c8ea9173d.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/ru_RU.02615a1a0756b3210733e1c91ab2ec01.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/sv_SE.cd410267074844ecb863ee4e3f9bf431.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/th_TH.49cdcc8b022f8d483a5337c5549362f5.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/tr_TR.797e28bdf4348909bcb8020cc36c6801.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/zh_CN.56ee37628f8b15060f693fcb8f7d633e.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/zh_HK.93ab34d7649740763d08d12136411bf4.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/zh_TW.fc72ee39c67cdaaf31c464a5250e33f9.version`

</details>

#### SystemOS (9)

- `/System/Library/Caches/com.apple.dyld/dyld_shared_cache_arm64e.27.dylddata`
- `/System/Library/Caches/com.apple.dyld/dyld_shared_cache_arm64e.28.dyldlinkedit`
- `/System/Library/Caches/com.apple.dyld/dyld_shared_cache_arm64e.29`
- `/System/Library/Caches/com.apple.dyld/dyld_shared_cache_arm64e.30`
- `/System/Library/Caches/com.apple.dyld/dyld_shared_cache_arm64e.51.dylddata`
- `/System/Library/Caches/com.apple.dyld/dyld_shared_cache_arm64e.52.dyldlinkedit`
- `/System/Library/Frameworks/WebKit.framework/XPCServices/com.apple.WebKit.WebContent.Crashy.xpc/Info.plist`
- `/System/Library/Frameworks/WebKit.framework/XPCServices/com.apple.WebKit.WebContent.Crashy.xpc/_CodeSignature/CodeResources`
- `/System/Library/Frameworks/WebKit.framework/XPCServices/com.apple.WebKit.WebContent.Crashy.xpc/com.apple.WebKit.WebContent.Crashy`

## Feature Flags

### ⬆️ Updated (6)

<details>
  <summary><i>View Updated</i></summary>

#### AuthKit.plist

>  `Domain/AuthKit.plist`

```diff

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
+	<key>DTO</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>EasyDependentSignIn</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### Bridge.plist

>  `Domain/Bridge.plist`

```diff

 		<key>Enabled</key>
 		<true/>
 	</dict>
+	<key>DimpleKey</key>
+	<dict>
+		<key>Enabled</key>
+		<true/>
+	</dict>
 	<key>HealthChecklistOnboarding</key>
 	<dict>
 		<key>Enabled</key>

```

#### LocalAuthentication.plist

>  `Domain/LocalAuthentication.plist`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>DimpleKey</key>
+	<dict>
+		<key>Enabled</key>
+		<true/>
+	</dict>
+	<key>DimpleKey_PassChange</key>
+	<dict>
+		<key>Enabled</key>
+		<true/>
+	</dict>
 	<key>PasscodeChangeService</key>
 	<dict>
 		<key>Enabled</key>

```

#### Music.plist

>  `Domain/Music.plist`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>el_camino_collaboration</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
+	<key>moonface</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>psp</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### NanoTimeKit.plist

>  `Domain/NanoTimeKit.plist`

```diff

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
+	<key>disable_blinking_separator_on_m9</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>disable_face_swiping</key>
 	<dict>
 		<key>DevelopmentPhase</key>

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
+	<key>m9_optimized_tritium_animations</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>paramecium_face_bundle</key>
 	<dict>
 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
+	<key>rhizome</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>starbear_picker</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### SiriKitFlow.plist

>  `Domain/SiriKitFlow.plist`

```diff

 		<key>Enabled</key>
 		<true/>
 	</dict>
+	<key>hide_unlock_prompt</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>ua_cancel_default_behavior</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```


</details>

## EOF
