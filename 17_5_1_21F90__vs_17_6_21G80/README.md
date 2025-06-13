# 17.5.1 (21F90) .vs 17.6 (21G80)

## IPSWs

- `iPhone16,1_17.5.1_21F90_Restore.ipsw`
- `iPhone16,1_17.6_21G80_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 17.5.1 *(21F90)* | 23.5.0 | 10063.122.3~3 | Wed, 01May2024 20:34:22 PDT |
| 17.6 *(21G80)* | 23.6.0 | 10063.142.1~1 | Fri, 05Jul2024 18:04:28 PDT |

### Kexts

#### ⬆️ Updated (79)

<details>
  <summary><i>View Updated</i></summary>

>  `com.apple.AGXFirmwareKextG16PRTBuddy`

```diff

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xd40
   __DATA_CONST.__kalloc_type: 0x80
-  UUID: BD06F236-2150-3C31-920A-B22604366074
+  UUID: 12180FEC-A36E-3914-A54B-6AD6ED60C2A5
   Functions: 35
   Symbols:   0
   CStrings:  33

```

>  `com.apple.AGXG16P`

```diff

   __DATA_CONST.__const: 0x10418
   __DATA_CONST.__kalloc_type: 0x2100
   __DATA_CONST.__kalloc_var: 0x3160
-  UUID: 79DB4AEC-F9C5-37CB-9A64-50AF032F44F3
+  UUID: 766BC1DC-628E-3F28-983D-E297F0A23712
   Functions: 1218
   Symbols:   0
   CStrings:  1671
CStrings:
+ "Jul  5 2024 18:22:05"
- "May  2 2024 07:24:53"

```

>  `com.apple.AppleFSCompression.AppleFSCompressionTypeZlib`

```diff

-163.0.0.0.0
+163.140.2.0.0
   __TEXT.__const: 0x3a40
   __TEXT.__cstring: 0x775
-  __TEXT_EXEC.__text: 0xae0c
+  __TEXT_EXEC.__text: 0xad14
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd8
   __DATA.__bss: 0x29

   __DATA_CONST.__const: 0x16e0
   __DATA_CONST.__kalloc_type: 0x40
   __DATA_CONST.__kalloc_var: 0x140
-  UUID: A6B8FF10-E281-38A8-BCB5-610BE1DF10C5
-  Functions: 49
+  UUID: 99B5FCE4-9871-32AC-A7D6-553528F33BC5
+  Functions: 48
   Symbols:   0
   CStrings:  38
 

```

>  `com.apple.driver.AppleALSColorSensor`

```diff

-1672.120.23.0.0
+1672.140.4.0.0
   __TEXT.__const: 0x104
-  __TEXT.__cstring: 0x3470
+  __TEXT.__cstring: 0x34d3
   __TEXT.__os_log: 0x96
-  __TEXT_EXEC.__text: 0x141d0
+  __TEXT_EXEC.__text: 0x141e4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x188
   __DATA.__common: 0x1d0

   __DATA_CONST.__mod_term_func: 0x58
   __DATA_CONST.__const: 0x5a38
   __DATA_CONST.__kalloc_type: 0x340
-  UUID: 1A4D34B4-CB4F-34EE-907E-23A5BFA72D4A
+  UUID: B17DD27C-57DE-3F4A-851A-8185B141E7B9
   Functions: 186
   Symbols:   0
-  CStrings:  381
+  CStrings:  382
 
CStrings:
+ "AppleALSColorSensor::setPropertiesGated: state is suspended; setting report interval is discarded\n"

```

>  `com.apple.driver.AppleAOPAudio`

```diff

   __DATA_CONST.__mod_term_func: 0xe0
   __DATA_CONST.__const: 0xb7c8
   __DATA_CONST.__kalloc_type: 0xa00
-  UUID: 9C05282E-1894-3ADB-994F-E7B288F5A828
+  UUID: DA98CF10-B606-3373-9E49-A346CE240815
   Functions: 709
   Symbols:   0
   CStrings:  1152
CStrings:
+ "19:16:14"
+ "19:16:29"
+ "Jul 14 2024"
- "07:20:57"
- "07:21:02"
- "May  2 2024"

```

>  `com.apple.driver.AppleAOPVoiceTrigger`

```diff

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xd70
   __DATA_CONST.__kalloc_type: 0x180
-  UUID: D9F57DBE-516B-3D99-A21C-6B45EA1CE2ED
+  UUID: 943368FD-3FED-3822-A9BC-1B256441C267
   Functions: 108
   Symbols:   0
   CStrings:  216
CStrings:
+ "19:16:23"
+ "Jul 14 2024"
- "07:21:41"
- "May  2 2024"

```

>  `com.apple.driver.AppleARMPMU`

```diff

-1026.120.7.0.0
+1026.140.2.0.0
   __TEXT.__const: 0x64
   __TEXT.__cstring: 0x2d45
   __TEXT_EXEC.__text: 0x16170

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0x1e50
   __DATA_CONST.__kalloc_type: 0x300
-  UUID: 2BE09A62-DD53-3F41-8E37-4F9A70996547
+  UUID: 3EE16C1B-159D-3C4F-AD16-4A9B62FE2411
   Functions: 162
   Symbols:   0
   CStrings:  399

```

>  `com.apple.driver.AppleARMPlatform`

```diff

-1026.120.7.0.0
+1026.140.2.0.0
   __TEXT.__const: 0x16f0
   __TEXT.__os_log: 0x13fe
   __TEXT.__cstring: 0xcac1
-  __TEXT_EXEC.__text: 0x52c40
+  __TEXT_EXEC.__text: 0x52dc4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x6c8
   __DATA.__common: 0xcc8

   __DATA_CONST.__const: 0x16588
   __DATA_CONST.__kalloc_var: 0x140
   __DATA_CONST.__kalloc_type: 0x1580
-  UUID: 29C961DE-8D56-391B-834A-E86E92ED9783
+  UUID: B8A19F40-3517-31AD-AE2B-CF3884E05544
   Functions: 1229
   Symbols:   0
   CStrings:  1692

```

>  `com.apple.driver.AppleAVD`

```diff

-742.5.0.0.0
-  __TEXT.__os_log: 0x1ccb0
+743.5.0.0.0
+  __TEXT.__os_log: 0x1e00b
   __TEXT.__cstring: 0x10bfe
   __TEXT.__const: 0x8a1c8
-  __TEXT_EXEC.__text: 0xf087c
+  __TEXT_EXEC.__text: 0xf1eac
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2ac
   __DATA.__common: 0x90

   __DATA_CONST.__const: 0x5678
   __DATA_CONST.__kalloc_type: 0x3a80
   __DATA_CONST.__kalloc_var: 0x1b30
-  UUID: 90498BE9-22F0-3D09-9B2A-6994916459D1
-  Functions: 1644
+  UUID: AAC3BC0C-A81B-3AF6-B621-32289ED8B017
+  Functions: 1664
   Symbols:   0
-  CStrings:  2177
+  CStrings:  2184
 
CStrings:
+ "AppleAVD: ERROR: %s(): Invalid workOffset=%u + numWorks=%u"
+ "AppleAVD: ERROR: %s(): Invalid workOffset[0]=%u + numWorks[0]=%u, workOffset[1]=%u"
+ "AppleAVD: ERROR: %s(): No numWorks specified"
+ "AppleAVD: ERROR: %s(): Unsupported numSlices = %u"
+ "AppleAVD: ERROR: %s(): Unsupported numTiles = num_tile_columns (=%u) * num_tile_rows (=%u)"
+ "AppleAVD: ERROR: %s(): Unsupported numWorks = %u"
+ "AppleAVD: ERROR: %s(): Unsupported numWorks, numWorks[0]=%u, numWorks[1]=%u"
+ "AppleAVD: ERROR: %s(): workOffset is expected to be specified from low to high"
- "AppleAVD: AVC sps[%d] width %d height %d over size in %s\n"

```

>  `com.apple.driver.AppleAVE2`

```diff

-760.30.1.0.0
+760.31.1.0.0
   __TEXT.__const: 0x22d10
-  __TEXT.__cstring: 0x29aaa
-  __TEXT.__os_log: 0x303b9
-  __TEXT_EXEC.__text: 0x102684
+  __TEXT.__cstring: 0x29bab
+  __TEXT.__os_log: 0x30443
+  __TEXT_EXEC.__text: 0x102954
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2b0
   __DATA.__common: 0xb4

   __DATA_CONST.__const: 0x46e0
   __DATA_CONST.__kalloc_type: 0x1540
   __DATA_CONST.__kalloc_var: 0x8c0
-  UUID: 7B589464-B56B-3B34-9671-AA1C23AF3DA8
-  Functions: 1270
+  UUID: FDA24939-4C26-37AC-93DA-A63A87906DBE
+  Functions: 1271
   Symbols:   0
-  CStrings:  5634
+  CStrings:  5641
 
CStrings:
+ "%lld %d AVE %s: %s:%d %s | wrong DLB configuration %d %d %p"
+ "%lld %d AVE %s: %s:%d %s | wrong DLB configuration %d %d %p\n"
+ "%lld %d AVE %s: %s:%d %s | wrong DLB configuration %p %d %d"
+ "%lld %d AVE %s: %s:%d %s | wrong DLB configuration %p %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | wrong state %p %d %p %p %p"
+ "%lld %d AVE %s: %s::%s:%d %s | wrong state %p %d %p %p %p\n"
+ "12111112122212121111111111111221111111111111"
+ "18:20:24"
+ "Jul  5 2024"
+ "m_pcIODrv != nullptr && m_psNotificationPort != 0 && m_psClient != nullptr"
- "1211111212221212111111111111121111111111111"
- "20:23:51"
- "May  1 2024"

```

>  `com.apple.driver.AppleDCP`

```diff

-590.122.1.0.0
+590.140.7.0.0
   __TEXT.__cstring: 0x12a3
   __TEXT.__const: 0x18
   __TEXT_EXEC.__text: 0x504c

   __DATA_CONST.__mod_term_func: 0x20
   __DATA_CONST.__const: 0x1400
   __DATA_CONST.__kalloc_type: 0x100
-  UUID: 8C088795-6151-3676-832B-C03020110DEE
+  UUID: 4C63920A-F3A3-39C1-8344-3CBA28E88E09
   Functions: 103
   Symbols:   0
   CStrings:  89

```

>  `com.apple.driver.AppleDiskImages2`

```diff

-276.120.5.0.2
-  __TEXT.__cstring: 0x2040
+276.120.7.0.0
+  __TEXT.__cstring: 0x205a
   __TEXT.__os_log: 0x11a2
   __TEXT.__const: 0x10
   __TEXT_EXEC.__text: 0xd32c

   __DATA_CONST.__const: 0x1cb8
   __DATA_CONST.__kalloc_type: 0x240
   __DATA_CONST.__kalloc_var: 0xa0
-  UUID: 8D1EC11E-2046-3FEF-A863-00F56C022845
+  UUID: 96929FE2-710D-30A0-B246-CA3F5D5D4983
   Functions: 209
   Symbols:   0
   CStrings:  279
CStrings:
+ "276.120.7"
+ "v32@?0^{?=II^{ipc_port}^{ipc_port}Ii}8^(?={?=(?=^{ipc_port}^{ipc_port}^{ipc_port})b16b8b8I}{?=IIb8b8b8b8}{?=IIb8b8b8b8}{?=IIb24b8}{?=IIb16b8b8})16^v24"
- "276.120.5"
- "v32@?0^{?=II^{ipc_port}^{ipc_port}Ii}8^(?={?=^{ipc_port}b16b8b8I}{?=IIb8b8b8b8}{?=IIb8b8b8b8}{?=IIb24b8}{?=IIb16b8b8})16^v24"

```

>  `com.apple.driver.AppleEmbeddedLightSensor`

```diff

-1672.120.23.0.0
+1672.140.4.0.0
   __TEXT.__const: 0x15e8
   __TEXT.__cstring: 0x4331
   __TEXT.__os_log: 0x2c

   __DATA_CONST.__mod_term_func: 0x48
   __DATA_CONST.__const: 0x4a98
   __DATA_CONST.__kalloc_type: 0x240
-  UUID: 724BD1F1-1719-3F19-89C8-097AAD4D5F60
+  UUID: FD953A45-B165-3F01-A88B-FC93A6CFA6C9
   Functions: 227
   Symbols:   0
   CStrings:  467

```

>  `com.apple.driver.AppleEventLogHandler`

```diff

-1374.120.11.0.0
+1374.140.2.0.0
   __TEXT.__cstring: 0x4cf
   __TEXT_EXEC.__text: 0x13e0
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__const: 0x5f0
   __DATA_CONST.__kalloc_type: 0x40
   __DATA_CONST.__kalloc_var: 0xf0
-  UUID: 1DCB2239-38D0-3DC2-8628-77CA26772543
+  UUID: 31280DBB-19D6-38B0-9DDB-3F09B58BEE24
   Functions: 35
   Symbols:   0
   CStrings:  38

```

>  `com.apple.driver.AppleFirmwareKit`

```diff

-454.120.7.0.1
-  __TEXT.__os_log: 0x1d3f
-  __TEXT.__cstring: 0x2b5d
+454.140.3.0.0
+  __TEXT.__os_log: 0x1dd0
+  __TEXT.__cstring: 0x2b7b
   __TEXT.__const: 0x2e0
-  __TEXT_EXEC.__text: 0x45bc8
+  __TEXT_EXEC.__text: 0x45f88
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x578
   __DATA.__common: 0x790

   __DATA_CONST.__mod_init_func: 0x100
   __DATA_CONST.__mod_term_func: 0x100
   __DATA_CONST.__const: 0xd7b8
-  __DATA_CONST.__kalloc_type: 0x1780
+  __DATA_CONST.__kalloc_type: 0x1840
   __DATA_CONST.__kalloc_var: 0xa0
-  UUID: CEFC1562-B3B0-38CA-920E-1DA5DC67C488
+  UUID: 852A5A46-93E8-3957-8981-DA1AC4916DB3
   Functions: 1095
   Symbols:   0
-  CStrings:  521
+  CStrings:  525
 
CStrings:
+ "%s(%s:%#llx): Dropping context for command not completed by AFKUser\n"
+ "%s(%s:%#llx): Unable to find message context %#lx associated with command \n"
+ "111"
+ "12111112122212121111111111111211212111"
+ "site.CommandContextNode"
- "121111121222121211111111111112112121"

```

>  `com.apple.driver.AppleFirmwareUpdateKext`

```diff

-975.120.15.0.0
+975.140.4.0.0
   __TEXT.__cstring: 0x8f8
   __TEXT_EXEC.__text: 0x25f4
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xc70
   __DATA_CONST.__kalloc_type: 0x80
-  UUID: 9CCB9753-C2B9-34F7-BDAD-F890BD551E1E
+  UUID: D0BE4D9A-5F7D-30D8-A5F1-A7F57AB51F05
   Functions: 40
   Symbols:   0
   CStrings:  62

```

>  `com.apple.driver.AppleGameControllerPersonality`

```diff

-11.5.1.0.0
+11.6.2.0.0
   __TEXT.__cstring: 0xd4
   __TEXT.__os_log: 0x53
   __TEXT_EXEC.__text: 0x7b8

   __DATA_CONST.__mod_term_func: 0x8
   __DATA_CONST.__const: 0x788
   __DATA_CONST.__kalloc_type: 0x40
-  UUID: 4ED82E5D-5B26-3AFE-9423-482B2EFA155A
+  UUID: 6FA7C469-97B6-3CAE-8477-F928B5AC6302
   Functions: 13
   Symbols:   0
   CStrings:  11

```

>  `com.apple.driver.AppleH16ANEInterface`

```diff

   __DATA_CONST.__const: 0x5870
   __DATA_CONST.__kalloc_type: 0x2680
   __DATA_CONST.__kalloc_var: 0x1ef0
-  UUID: D1D2C00B-E356-3D54-8D0F-B8084308C4B6
+  UUID: 4D1BA683-D60E-3B17-98D7-C5286FB2CD2C
   Functions: 978
   Symbols:   0
   CStrings:  2786
CStrings:
+ "/AppleInternal/Library/BuildRoots/ce4161a3-3a02-11ef-92ee-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.6.Internal.sdk/System/Library/Frameworks/Kernel.framework/PrivateHeaders/kernel_sdkroot/usr/include/c++/v1/span"
+ "/AppleInternal/Library/BuildRoots/ce4161a3-3a02-11ef-92ee-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.6.Internal.sdk/System/Library/Frameworks/Kernel.framework/PrivateHeaders/kernel_sdkroot/usr/include/c++/v1/vector"
- "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/System/Library/Frameworks/Kernel.framework/PrivateHeaders/kernel_sdkroot/usr/include/c++/v1/span"
- "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/System/Library/Frameworks/Kernel.framework/PrivateHeaders/kernel_sdkroot/usr/include/c++/v1/vector"

```

>  `com.apple.driver.AppleH16CameraInterface`

```diff

-2.602.0.0.0
+2.700.0.0.0
   __TEXT.__const: 0x9fb0
   __TEXT.__cstring: 0x18d42
   __TEXT.__os_log: 0x14f6a

   __DATA_CONST.__const: 0x8848
   __DATA_CONST.__kalloc_type: 0x1280
   __DATA_CONST.__kalloc_var: 0xd70
-  UUID: 759B73CC-5DF0-3CD8-B0FC-753615BFA5E8
+  UUID: 13E63680-3E93-36BB-8A38-F836D57453F4
   Functions: 1165
   Symbols:   0
   CStrings:  3256

```

>  `com.apple.driver.AppleH16PhotonDetector`

```diff

-2.602.0.0.0
+2.700.0.0.0
   __TEXT.__cstring: 0x1ea
   __TEXT.__os_log: 0x5af
   __TEXT_EXEC.__text: 0x2790

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xe48
   __DATA_CONST.__kalloc_type: 0x100
-  UUID: 7F16E02C-6CDD-3D89-A403-003CEE8ECBB3
+  UUID: F4EA2BAC-38CE-3A7F-80E9-45BB191DE4DF
   Functions: 45
   Symbols:   0
   CStrings:  45

```

>  `com.apple.driver.AppleHIDALSService`

```diff

-1672.120.23.0.0
+1672.140.4.0.0
   __TEXT.__cstring: 0xbf
   __TEXT.__os_log: 0xc0
   __TEXT_EXEC.__text: 0x904

   __DATA_CONST.__mod_term_func: 0x8
   __DATA_CONST.__const: 0x5f0
   __DATA_CONST.__kalloc_type: 0x40
-  UUID: 0BB88802-4CD2-3735-A6A2-6539835C1ABF
+  UUID: 0D2514B9-643D-3FB4-B01D-9D850307EF55
   Functions: 14
   Symbols:   0
   CStrings:  18

```

>  `com.apple.driver.AppleHIDTransportSPI`

```diff

   __DATA_CONST.__const: 0x31e0
   __DATA_CONST.__kalloc_type: 0xa80
   __DATA_CONST.__kalloc_var: 0x320
-  UUID: 0CD88448-781B-3BFC-8268-08B7BEAF6511
+  UUID: 292662DA-EB22-3E5E-9C80-60E435B489FA
   Functions: 354
   Symbols:   0
   CStrings:  857
CStrings:
+ "/AppleInternal/Library/BuildRoots/8bb5d799-4029-11ef-93f2-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.6.Internal.sdk/usr/local/include/hidspi/HSMDevice.h"
+ "/AppleInternal/Library/BuildRoots/8bb5d799-4029-11ef-93f2-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.6.Internal.sdk/usr/local/include/hidspi/HSMDeviceInterface.h"
+ "/AppleInternal/Library/BuildRoots/8bb5d799-4029-11ef-93f2-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.6.Internal.sdk/usr/local/include/hidspi/HSMDeviceTest.h"
+ "/AppleInternal/Library/BuildRoots/8bb5d799-4029-11ef-93f2-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.6.Internal.sdk/usr/local/include/hidspi/HSMHIDInterface.h"
+ "/AppleInternal/Library/BuildRoots/8bb5d799-4029-11ef-93f2-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.6.Internal.sdk/usr/local/include/hidspi/HSMParserTest.h"
+ "/AppleInternal/Library/BuildRoots/8bb5d799-4029-11ef-93f2-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.6.Internal.sdk/usr/local/include/hidspi/HSMSPITest.h"
+ "/AppleInternal/Library/BuildRoots/8bb5d799-4029-11ef-93f2-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.6.Internal.sdk/usr/local/include/hidspi/HSMTransferDevice.h"
+ "/AppleInternal/Library/BuildRoots/8bb5d799-4029-11ef-93f2-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.6.Internal.sdk/usr/local/include/hidspi/HSMTransferTest.h"
+ "/AppleInternal/Library/BuildRoots/8bb5d799-4029-11ef-93f2-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.6.Internal.sdk/usr/local/include/hidspi/HSParserDevice.h"
+ "/AppleInternal/Library/BuildRoots/8bb5d799-4029-11ef-93f2-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.6.Internal.sdk/usr/local/include/hidspi/HSParserTest.h"
+ "/AppleInternal/Library/BuildRoots/8bb5d799-4029-11ef-93f2-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.6.Internal.sdk/usr/local/include/hidspi/HSTransferTest.h"
- "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/local/include/hidspi/HSMDevice.h"
- "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/local/include/hidspi/HSMDeviceInterface.h"
- "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/local/include/hidspi/HSMDeviceTest.h"
- "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/local/include/hidspi/HSMHIDInterface.h"
- "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/local/include/hidspi/HSMParserTest.h"
- "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/local/include/hidspi/HSMSPITest.h"
- "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/local/include/hidspi/HSMTransferDevice.h"
- "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/local/include/hidspi/HSMTransferTest.h"
- "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/local/include/hidspi/HSParserDevice.h"
- "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/local/include/hidspi/HSParserTest.h"
- "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/local/include/hidspi/HSTransferTest.h"

```

>  `com.apple.driver.AppleHPM`

```diff

-540.120.2.0.0
-  __TEXT.__cstring: 0x18257
+540.140.2.0.0
+  __TEXT.__cstring: 0x182f2
   __TEXT.__os_log: 0x1e8
   __TEXT.__const: 0x60
-  __TEXT_EXEC.__text: 0x4d114
+  __TEXT_EXEC.__text: 0x4d4a4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x6d0
   __DATA.__common: 0x518

   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__mod_init_func: 0xf8
   __DATA_CONST.__mod_term_func: 0xf8
-  __DATA_CONST.__const: 0x11150
+  __DATA_CONST.__const: 0x11180
   __DATA_CONST.__kalloc_type: 0xb00
-  UUID: 53B06705-02C1-3CC1-8442-8C9086EE950E
+  UUID: 6FC47255-C511-3E91-85A6-00DD261FD3BB
   Functions: 843
   Symbols:   0
-  CStrings:  1452
+  CStrings:  1454
 
CStrings:
+ "AppleHPMARMSPMI::readRegs - Transaction aborted due to SPMI Driver sleeping\n"
+ "AppleHPMARMSPMI::writeRegs - Transaction aborted due to SPMI Driver sleeping\n"

```

>  `com.apple.driver.AppleIDV`

```diff

-6.504.0.0.0
+6.600.1.0.0
   __TEXT.__const: 0xf8
-  __TEXT.__cstring: 0x137c
+  __TEXT.__cstring: 0x137e
   __TEXT_EXEC.__text: 0x80e0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xde8
   __DATA_CONST.__kalloc_type: 0x80
-  UUID: ECAB619B-ADAD-36D0-BB53-4E56F80CE6EA
+  UUID: 7DB3C2DD-BBC6-3F7B-898C-B1C15ED12AE1
   Functions: 83
   Symbols:   0
   CStrings:  117
CStrings:
+ "6.600.1"
- "6.504"

```

>  `com.apple.driver.AppleJPEGDriver`

```diff

   __DATA_CONST.__mod_term_func: 0x60
   __DATA_CONST.__const: 0x1e38
   __DATA_CONST.__kalloc_type: 0x880
-  UUID: 53B1FD9D-E41D-3D80-8CC7-0E2E5AF86C84
+  UUID: 7406EA0B-D88A-38FE-B8E6-24B9486BD51B
   Functions: 356
   Symbols:   0
   CStrings:  438
CStrings:
+ "/AppleInternal/Library/BuildRoots/ce4161a3-3a02-11ef-92ee-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.6.Internal.sdk/System/Library/Frameworks/Kernel.framework/PrivateHeaders/kernel_sdkroot/usr/include/c++/v1/array"
+ "/AppleInternal/Library/BuildRoots/ce4161a3-3a02-11ef-92ee-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.6.Internal.sdk/System/Library/Frameworks/Kernel.framework/PrivateHeaders/kernel_sdkroot/usr/include/c++/v1/span"
- "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/System/Library/Frameworks/Kernel.framework/PrivateHeaders/kernel_sdkroot/usr/include/c++/v1/array"
- "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/System/Library/Frameworks/Kernel.framework/PrivateHeaders/kernel_sdkroot/usr/include/c++/v1/span"

```

>  `com.apple.driver.AppleM2ScalerCSCDriver`

```diff

-147.0.26.0.0
-  __TEXT.__const: 0x25158
-  __TEXT.__cstring: 0x10523
-  __TEXT_EXEC.__text: 0x8d0a8
+147.0.32.0.0
+  __TEXT.__const: 0x25478
+  __TEXT.__cstring: 0x10779
+  __TEXT_EXEC.__text: 0x90398
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x150e4
-  __DATA.__common: 0x1970
+  __DATA.__common: 0x1978
   __DATA.__bss: 0xd20
   __DATA_CONST.__auth_got: 0x498
   __DATA_CONST.__got: 0x90
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__mod_init_func: 0x450
   __DATA_CONST.__mod_term_func: 0x428
-  __DATA_CONST.__const: 0x1ac00
+  __DATA_CONST.__const: 0x1adf0
   __DATA_CONST.__kalloc_type: 0x2c00
-  UUID: C1F2A817-C099-3D5D-85D5-B56EF3BAE621
-  Functions: 2249
+  UUID: 5EC43A4D-948F-3E17-87E7-22CFEA537F52
+  Functions: 2257
   Symbols:   0
-  CStrings:  1699
+  CStrings:  1705
 
CStrings:
+ "/Library/Caches/com.apple.xbs/Sources/IOSurfaceAccelerator_kexts/M2ScalerCSCColorConversionControlMSR8.cpp"
+ "1211111121211111111111111"
+ "121111112121111111111111111111111111111"
+ "12111111212111111111111111111111111111111111111111111"
+ "12112221222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222112222222222222222222222222222222222222211122222222222222222222221122222222222222222222222222222222222222111222222112222222222222222222222222222222122222222222222222222221222222222112222222222222222222222222222222222212121212121212121111211221112111212122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222212222222222222222222222211"
+ "HdrInputError: Input Maximum Clip hit input clip value limits \n"
+ "HdrInputError: Input Minimum Clip hit input clip value limits\n"
+ "HdrInputError: Output Maximum Clip hit output clip value limits\n"
+ "HdrInputError: Output Minimum Clip hit output clip value limits\n"
+ "IosaColorManagerMSR15.cpp"
+ "Selecting 3x3 block %d that doesn't exist in this HW version\n"
+ "msr_disable_hdr_clips"
- "121111112121111111111111122222222222222222222222222222222222222"
- "1211222122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211222222222222222222222222222222222222221112222222222222222222222112222222222222222222222222222222222222211122222211222222222222222222222222222222212222222222222222222222122222222211222222222222222222222222222222222221212121212121212111121122111211121212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222212222222222222222222222211"
- "HdrInputError: Input Maximum Clip limit hit\n"
- "HdrInputError: Input Minimum Clip limit hit\n"
- "HdrInputError: Output Maximum Clip limit hit\n"
- "HdrInputError: Output Minimum Clip limit hit\n"

```

>  `com.apple.driver.AppleMobileDispH16P-DCP`

```diff

-337.7.12.5.0
+338.2.9.0.0
   __TEXT.__cstring: 0x54c2
   __TEXT.__const: 0x1a90
   __TEXT_EXEC.__text: 0x1fc00

   __DATA_CONST.__const: 0x3c28
   __DATA_CONST.__kalloc_type: 0x580
   __DATA_CONST.__kalloc_var: 0xf0
-  UUID: BBB72B60-3E05-3909-9177-B95DB4555CA9
+  UUID: AE67FEE9-D5A2-3DB1-9A6E-A1B0315191DE
   Functions: 495
   Symbols:   0
   CStrings:  500

```

>  `com.apple.driver.AppleMobileFileIntegrity`

```diff

-859.120.5.0.0
+859.140.4.0.0
   __TEXT.__cstring: 0x9247
   __TEXT.__const: 0x14b0
   __TEXT.__os_log: 0x233

   __DATA_CONST.__const: 0x3718
   __DATA_CONST.__kalloc_type: 0xec0
   __DATA_CONST.__kalloc_var: 0x1310
-  UUID: 8326B175-3FCD-37A5-946C-13CF844C6070
+  UUID: 53A9D2FE-A576-35E5-87F4-5F292F517D6D
   Functions: 548
   Symbols:   0
   CStrings:  933
CStrings:
+ "18:02:15"
+ "Jul  5 2024"
- "07:22:04"
- "May  2 2024"

```

>  `com.apple.driver.ApplePMGR`

```diff

-1374.120.11.0.0
+1374.140.2.0.0
   __TEXT.__const: 0x250
   __TEXT.__cstring: 0xdc05
   __TEXT_EXEC.__text: 0x5028c

   __DATA_CONST.__const: 0x63e0
   __DATA_CONST.__kalloc_type: 0x600
   __DATA_CONST.__kalloc_var: 0xdc0
-  UUID: ADB44644-73D1-3EA4-8B6F-B8F3B285437E
+  UUID: DD22E21A-003A-3D20-B237-10766B819B7B
   Functions: 1470
   Symbols:   0
   CStrings:  1495

```

>  `com.apple.driver.ApplePhotonDetector`

```diff

-8.600.0.0.0
+8.700.0.0.0
   __TEXT.__cstring: 0x1d7
   __TEXT.__os_log: 0x56e
   __TEXT_EXEC.__text: 0x2790

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xe48
   __DATA_CONST.__kalloc_type: 0x100
-  UUID: 8E1F0F95-158C-3BD4-A5BB-9B7F7F9622CE
+  UUID: 98510224-CDC4-3422-97CB-E0CE8D6E9A82
   Functions: 45
   Symbols:   0
   CStrings:  45

```

>  `com.apple.driver.AppleSARService`

```diff

-1053.0.0.0.0
+1054.0.0.0.0
   __TEXT.__const: 0x720
   __TEXT.__cstring: 0x2975
   __TEXT.__os_log: 0x74d6

   __DATA_CONST.__const: 0x4620
   __DATA_CONST.__kalloc_type: 0x1940
   __DATA_CONST.__kalloc_var: 0x140
-  UUID: 891E4F04-3D26-3F90-A72D-372F67F04842
+  UUID: FBDF242A-4516-3947-B452-EE4B77F62978
   Functions: 320
   Symbols:   0
   CStrings:  754

```

>  `com.apple.driver.AppleSEPCredentialManager`

```diff

-660.120.3.0.1
+660.120.4.0.0
   __TEXT.__cstring: 0x102b4
   __TEXT.__const: 0x318
   __TEXT_EXEC.__text: 0x47ba8

   __DATA_CONST.__const: 0x1a98
   __DATA_CONST.__kalloc_type: 0x600
   __DATA_CONST.__kalloc_var: 0x1400
-  UUID: 8F3C853C-7B9E-3CA7-A7E3-534EC512A940
+  UUID: E65716C2-7638-3001-BA6C-0326F3678E24
   Functions: 686
   Symbols:   0
   CStrings:  1783

```

>  `com.apple.driver.AppleSEPKeyStore`

```diff

-1655.120.10.0.0
-  __TEXT.__cstring: 0x3974
+1655.140.2.0.0
+  __TEXT.__cstring: 0x398d
   __TEXT.__const: 0x814
   __TEXT_EXEC.__text: 0x3b698
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__const: 0x39b0
   __DATA_CONST.__kalloc_type: 0xd40
   __DATA_CONST.__kalloc_var: 0x140
-  UUID: 100F3BC5-44AF-340D-8B97-437C0AFB0C1F
+  UUID: F4C889FB-83B2-3045-AEFA-1E4562CEC147
   Functions: 577
   Symbols:   0
   CStrings:  336
CStrings:
+ "1655.140.2"
+ "18:21:23"
+ "Jul  5 2024"
+ "v32@?0^{?=II^{ipc_port}^{ipc_port}Ii}8^(?={?=(?=^{ipc_port}^{ipc_port}^{ipc_port})b16b8b8I}{?=IIb8b8b8b8}{?=IIb8b8b8b8}{?=IIb24b8}{?=IIb16b8b8})16^v24"
- "07:28:44"
- "1655.120.10"
- "May  2 2024"
- "v32@?0^{?=II^{ipc_port}^{ipc_port}Ii}8^(?={?=^{ipc_port}b16b8b8I}{?=IIb8b8b8b8}{?=IIb8b8b8b8}{?=IIb24b8}{?=IIb16b8b8})16^v24"

```

>  `com.apple.driver.AppleSMC`

```diff

   __DATA_CONST.__const: 0x7618
   __DATA_CONST.__kalloc_type: 0x680
   __DATA_CONST.__kalloc_var: 0xa0
-  UUID: 3ADFC6DF-1B15-311B-B8B8-0E0187DA14D5
+  UUID: 6DCC38D2-2E12-3B30-9534-F432F854F656
   Functions: 478
   Symbols:   0
   CStrings:  867
CStrings:
+ "18:17:11"
+ "18:17:13"
+ "Jul  5 2024"
- "20:23:08"
- "20:23:10"
- "May  1 2024"

```

>  `com.apple.driver.AppleSPMIPMU`

```diff

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xf00
   __DATA_CONST.__kalloc_type: 0x140
-  UUID: DB798C2A-4B9C-35C8-AB2E-F77B7B9DC7B9
+  UUID: 1B30B138-7B0E-31FB-A355-8F598DD2E232
   Functions: 107
   Symbols:   0
   CStrings:  342
CStrings:
+ "%s::handleStart: %s _pmuNub: %p ** configuration not found ** built 18:02:01 Jul  5 2024\n"
+ "%s::handleStart: ro=%d nvram=%d helper=%d %s _pmuNub: %p 0x%04x:0x%04x-0x%04x built 18:02:01 Jul  5 2024\n"
+ "%s::start: %s _pmuNub: %p ** configuration not found ** built 18:02:01 Jul  5 2024\n"
+ "%s::start: %s _pmuNub: %p built 18:02:01 Jul  5 2024\n"
- "%s::handleStart: %s _pmuNub: %p ** configuration not found ** built 07:20:44 May  2 2024\n"
- "%s::handleStart: ro=%d nvram=%d helper=%d %s _pmuNub: %p 0x%04x:0x%04x-0x%04x built 07:20:44 May  2 2024\n"
- "%s::start: %s _pmuNub: %p ** configuration not found ** built 07:20:45 May  2 2024\n"
- "%s::start: %s _pmuNub: %p built 07:20:45 May  2 2024\n"

```

>  `com.apple.driver.AppleSPU`

```diff

-957.120.3.0.1
+957.120.4.0.0
   __TEXT.__cstring: 0x5957
   __TEXT.__os_log: 0x725
   __TEXT.__const: 0x368

   __DATA_CONST.__const: 0x157f0
   __DATA_CONST.__kalloc_type: 0xe80
   __DATA_CONST.__kalloc_var: 0x320
-  UUID: D9D9A738-ED25-3B28-B82C-64FB8F7CB95C
+  UUID: 9E9495F2-C89C-359D-9476-0235081DA3D3
   Functions: 1243
   Symbols:   0
   CStrings:  888

```

>  `com.apple.driver.AppleSPURose`

```diff

-957.120.3.0.1
+957.120.4.0.0
   __TEXT.__const: 0x30
   __TEXT.__cstring: 0x1f82
   __TEXT.__os_log: 0x1431

   __DATA_CONST.__mod_term_func: 0x78
   __DATA_CONST.__const: 0x32c8
   __DATA_CONST.__kalloc_type: 0x3c0
-  UUID: A5DF53B9-3163-33C7-8B48-840191E5E469
+  UUID: AF59E968-70AF-3DC2-BAF5-E24D47AD65AB
   Functions: 375
   Symbols:   0
   CStrings:  365

```

>  `com.apple.driver.AppleSPUSphere`

```diff

-957.120.3.0.1
+957.120.4.0.0
   __TEXT.__cstring: 0x220
   __TEXT_EXEC.__text: 0x190c
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__mod_term_func: 0x8
   __DATA_CONST.__const: 0x748
   __DATA_CONST.__kalloc_type: 0x80
-  UUID: E4BA36B6-8663-31E1-AE30-5A1F64386BC1
+  UUID: 5240817A-A861-39C0-85B0-CDD24947CDBB
   Functions: 35
   Symbols:   0
   CStrings:  19

```

>  `com.apple.driver.AppleSmartIO2`

```diff

   __DATA_CONST.__const: 0x21f0
   __DATA_CONST.__kalloc_type: 0x280
   __DATA_CONST.__kalloc_var: 0xa0
-  UUID: 5B9FDEC5-478D-38FE-AAEE-A511975C77F5
+  UUID: 690036A3-3189-3FC2-AF48-BF33DEDD7E63
   Functions: 366
   Symbols:   0
   CStrings:  378
CStrings:
+ "18:06:08"
+ "Jul  5 2024"
- "20:14:29"
- "May  1 2024"

```

>  `com.apple.driver.AppleStockholmControl`

```diff

-345.7.0.0.0
+346.4.0.0.0
   __TEXT.__cstring: 0x4736
   __TEXT.__const: 0x30
   __TEXT_EXEC.__text: 0x15624

   __DATA_CONST.__mod_term_func: 0x30
   __DATA_CONST.__const: 0x21c8
   __DATA_CONST.__kalloc_type: 0x1c0
-  UUID: 64A1B8EA-1239-38F8-8F30-240BB567AE3C
+  UUID: E4CC75F3-03D5-398E-A0C8-7F86D79B73E0
   Functions: 163
   Symbols:   0
   CStrings:  448

```

>  `com.apple.driver.AppleT8030SOCTuner`

```diff

-1374.120.11.0.0
+1374.140.2.0.0
   __TEXT.__cstring: 0x41e
   __TEXT.__const: 0x30
   __TEXT_EXEC.__text: 0x1654

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xc50
   __DATA_CONST.__kalloc_type: 0x80
-  UUID: 3B99CC97-13EC-3C3C-AD65-0E3CA8B161C3
+  UUID: CB429BF0-A24D-3DB7-B936-703FAC072D1A
   Functions: 29
   Symbols:   0
   CStrings:  43

```

>  `com.apple.driver.AppleT8130CLPC`

```diff

   __DATA_CONST.__const: 0x4a08
   __DATA_CONST.__kalloc_type: 0x380
   __DATA_CONST.__kalloc_var: 0x370
-  UUID: C23189C1-602D-311F-B557-C7FB87D5C8C3
+  UUID: FFD7CBF1-C0EF-3C1F-A982-59652A8929A1
   Functions: 648
   Symbols:   0
   CStrings:  449
CStrings:
+ "2024-07-05T18:17:50-07:00"
- "2024-05-02T07:22:42-07:00"

```

>  `com.apple.driver.AppleT8130PMGR`

```diff

-1374.120.11.0.0
+1374.140.2.0.0
   __TEXT.__const: 0x1250
   __TEXT.__cstring: 0x1616
   __TEXT_EXEC.__text: 0xf26c

   __DATA_CONST.__mod_term_func: 0x8
   __DATA_CONST.__const: 0x1210
   __DATA_CONST.__kalloc_type: 0x40
-  UUID: AB3C6491-DFD2-3EAB-A794-23CD3E997389
+  UUID: 83F1215A-176F-360D-AAA3-EAA6AF39B9AD
   Functions: 267
   Symbols:   0
   CStrings:  119

```

>  `com.apple.driver.AppleUSBDeviceMux`

```diff

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0x780
   __DATA_CONST.__kalloc_type: 0x440
-  UUID: 29CBF8ED-F810-34BF-B428-F2375FC2DDBF
+  UUID: 0A073209-7056-366E-BF6E-F64638A38C2D
   Functions: 69
   Symbols:   0
   CStrings:  144
CStrings:
+ "18:18:05"
+ "Jul  5 2024"
- "07:21:07"
- "May  2 2024"

```

>  `com.apple.driver.AppleUSBDeviceNCM`

```diff

-341.120.1.0.1
+341.120.2.0.0
   __TEXT.__const: 0x57
   __TEXT.__cstring: 0xaa5
   __TEXT_EXEC.__text: 0x779c

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0x1698
   __DATA_CONST.__kalloc_type: 0xc0
-  UUID: 25052075-8074-3519-9A3F-4DACCC4C0994
+  UUID: AB78AB1F-43BB-3830-9A1D-D62F5C7F5A22
   Functions: 77
   Symbols:   0
   CStrings:  105

```

>  `com.apple.driver.AppleUSBHostMergeProperties`

```diff

-1337.120.6.0.0
+1337.140.2.0.0
   __TEXT.__cstring: 0x89
   __TEXT_EXEC.__text: 0xac4
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__mod_term_func: 0x8
   __DATA_CONST.__const: 0x600
   __DATA_CONST.__kalloc_type: 0x40
-  UUID: 1F821AF7-3A37-390C-A7BA-8193E6AE9569
+  UUID: 2B97085B-4FF5-356F-88E6-AFE67112B4D8
   Functions: 12
   Symbols:   0
   CStrings:  5

```

>  `com.apple.driver.AudioDMAController-T8130`

```diff

   __DATA_CONST.__mod_term_func: 0x20
   __DATA_CONST.__const: 0x1988
   __DATA_CONST.__kalloc_type: 0x340
-  UUID: AB49F529-9B90-39AE-B331-B49B1664801D
+  UUID: C9B555B4-612F-33F0-B75C-0E10D817759B
   Functions: 226
   Symbols:   0
   CStrings:  368
CStrings:
+ "18:08:35"
+ "Jul  5 2024"
- "20:16:37"
- "May  1 2024"

```

>  `com.apple.driver.DCPAVFamilyProxy`

```diff

-283.120.9.0.1
+283.140.3.0.0
   __TEXT.__const: 0x270
   __TEXT.__cstring: 0x23fd
   __TEXT.__os_log: 0x1252
-  __TEXT_EXEC.__text: 0x16df0
+  __TEXT_EXEC.__text: 0x16e04
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x308

   __DATA_CONST.__const: 0x85b8
   __DATA_CONST.__kalloc_type: 0x4c0
   __DATA_CONST.__kalloc_var: 0x3c0
-  UUID: 311AFE7C-F38F-3435-A39B-9297C7BCD72E
+  UUID: 8FA6F5D7-9E81-3F22-BDE1-53F5E6648BD6
   Functions: 474
   Symbols:   0
   CStrings:  269

```

>  `com.apple.driver.RTBuddy`

```diff

-550.120.14.0.0
-  __TEXT.__cstring: 0x9b77
+550.140.2.0.0
+  __TEXT.__cstring: 0x9c0d
   __TEXT.__const: 0x280
-  __TEXT_EXEC.__text: 0x41b60
+  __TEXT_EXEC.__text: 0x41b6c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x128
   __DATA.__common: 0xb48

   __DATA_CONST.__const: 0xa958
   __DATA_CONST.__kalloc_type: 0x1300
   __DATA_CONST.__kalloc_var: 0xf0
-  UUID: 38565443-53C3-3F84-8722-88AE73F3257D
-  Functions: 1442
+  UUID: A73A0F76-E95C-35CA-9C43-096FA7C884A1
+  Functions: 1443
   Symbols:   0
-  CStrings:  1059
+  CStrings:  1058
 
CStrings:
+ "\"Assertion failed: \" \"0\" @%s:%d"
+ "\"Assertion failed: \" \"buffer_len >= entry.key_len + data_len\" @%s:%d"
+ "\"Assertion failed: \" \"buffer_len >= sizeof(entry)\" @%s:%d"
+ "\"Assertion failed: \" \"dict\" @%s:%d"
+ "\"Assertion failed: \" \"entry.key_len <= RTK_CAS_KEY_STR_MAX_SIZE\" @%s:%d"
+ "\"Assertion failed: \" \"item_count\" @%s:%d"
+ "18:17:22"
+ "Jul  5 2024"
- "\"Assertion failed: %s\" @%s:%d"
- "0"
- "20:23:03"
- "May  1 2024"
- "buffer_len >= entry.key_len + data_len"
- "buffer_len >= sizeof(entry)"
- "dict"
- "entry.key_len <= RTK_CAS_KEY_STR_MAX_SIZE"
- "item_count"

```

>  `com.apple.driver.usb.AppleUSBCommon`

```diff

-1337.120.6.0.0
+1337.140.2.0.0
   __TEXT.__cstring: 0x2b6
   __TEXT.__os_log: 0xc6
   __TEXT_EXEC.__text: 0x4c54

   __DATA_CONST.__mod_term_func: 0x20
   __DATA_CONST.__const: 0x818
   __DATA_CONST.__kalloc_type: 0x240
-  UUID: 8EF2B00B-8926-32EF-8F85-7BE850AE6D7E
+  UUID: F661600E-2A6C-3566-B4A7-806605BA5E91
   Functions: 84
   Symbols:   0
   CStrings:  42

```

>  `com.apple.driver.usb.AppleUSBHostBillboardDevice`

```diff

-1337.120.6.0.0
+1337.140.2.0.0
   __TEXT.__cstring: 0x29b
   __TEXT.__os_log: 0x15d
   __TEXT_EXEC.__text: 0x1ae0

   __DATA_CONST.__mod_term_func: 0x8
   __DATA_CONST.__const: 0x5f0
   __DATA_CONST.__kalloc_type: 0x40
-  UUID: 219050B0-B5CE-36F2-8699-02FBD5C23B69
+  UUID: 195E478B-B522-3B17-9072-5768F996031D
   Functions: 10
   Symbols:   0
   CStrings:  32

```

>  `com.apple.driver.usb.AppleUSBHostCompositeDevice`

```diff

-1337.120.6.0.0
+1337.140.2.0.0
   __TEXT.__cstring: 0x4de
   __TEXT.__os_log: 0x358
   __TEXT_EXEC.__text: 0x4294

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0x920
   __DATA_CONST.__kalloc_type: 0xc0
-  UUID: FB5F3946-3CD2-38A1-81BD-35F75751688C
+  UUID: 6D35D3C8-175C-36DA-877C-7E4FC690630B
   Functions: 37
   Symbols:   0
   CStrings:  44

```

>  `com.apple.driver.usb.AppleUSBHostPacketFilter`

```diff

-1337.120.6.0.0
+1337.140.2.0.0
   __TEXT.__const: 0x18
   __TEXT.__cstring: 0xa5a
   __TEXT.__os_log: 0xaf

   __DATA_CONST.__mod_term_func: 0x8
   __DATA_CONST.__const: 0x5f0
   __DATA_CONST.__kalloc_type: 0x140
-  UUID: 6C3638AA-5F6D-33E2-915A-8D03E7FDABBD
+  UUID: 29876758-219A-332A-8C12-B65C9BFF4DD1
   Functions: 22
   Symbols:   0
   CStrings:  34

```

>  `com.apple.driver.usb.AppleUSBHostiOSDevice`

```diff

-1337.120.6.0.0
+1337.140.2.0.0
   __TEXT.__cstring: 0x145
   __TEXT.__os_log: 0x1e
   __TEXT_EXEC.__text: 0x1094

   __DATA_CONST.__mod_term_func: 0x8
   __DATA_CONST.__const: 0x5f0
   __DATA_CONST.__kalloc_type: 0x40
-  UUID: 7E7DB2E4-F4BD-3841-B83D-2D5206778502
+  UUID: E66E678B-BB51-3475-8597-4C1439DDC74A
   Functions: 15
   Symbols:   0
   CStrings:  15

```

>  `com.apple.driver.usb.AppleUSBHub`

```diff

-1337.120.6.0.0
+1337.140.2.0.0
   __TEXT.__const: 0x58
   __TEXT.__cstring: 0x227f
   __TEXT.__os_log: 0x2466

   __DATA_CONST.__mod_term_func: 0x50
   __DATA_CONST.__const: 0x4848
   __DATA_CONST.__kalloc_type: 0x280
-  UUID: 97551E00-D398-393E-A0E2-D8AA366B7921
+  UUID: EA4BD922-F017-3391-9591-D55999D66B47
   Functions: 190
   Symbols:   0
   CStrings:  371

```

>  `com.apple.driver.usb.AppleUSBXHCI`

```diff

-1337.120.6.0.0
+1337.140.2.0.0
   __TEXT.__const: 0xc4
   __TEXT.__cstring: 0x5da9
   __TEXT.__os_log: 0x5d61

   __DATA_CONST.__const: 0x5d78
   __DATA_CONST.__kalloc_type: 0x8c0
   __DATA_CONST.__kalloc_var: 0xa0
-  UUID: 31AC5ECF-9BBA-3E97-9B56-1042A257A67F
+  UUID: 5887960A-2FD9-359E-985C-EA8703C3060C
   Functions: 580
   Symbols:   0
   CStrings:  907

```

>  `com.apple.driver.usb.IOUSBHostHIDDevice`

```diff

-1337.120.6.0.0
+1337.140.2.0.0
   __TEXT.__cstring: 0xac4
   __TEXT.__os_log: 0x9af
   __TEXT_EXEC.__text: 0x8aac

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xf20
   __DATA_CONST.__kalloc_type: 0x200
-  UUID: E958FBCE-1E51-3E3A-8287-1CF0D20FC435
+  UUID: 05EB247E-9C2E-3468-BEAA-5CA81E12B446
   Functions: 50
   Symbols:   0
   CStrings:  140

```

>  `com.apple.driver.usb.cdc`

```diff

-341.120.1.0.1
+341.120.2.0.0
   __TEXT.__cstring: 0x20d
   __TEXT_EXEC.__text: 0x22f0
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xc20
   __DATA_CONST.__kalloc_type: 0x80
-  UUID: 40A9050E-5AC4-396E-B3B7-A5592593BD6D
+  UUID: 4E532C2B-7BAE-3B42-868C-9857213C63BA
   Functions: 34
   Symbols:   0
   CStrings:  25

```

>  `com.apple.driver.usb.cdc.ecm`

```diff

-341.120.1.0.1
+341.120.2.0.0
   __TEXT.__const: 0x38
   __TEXT.__cstring: 0x32c
   __TEXT_EXEC.__text: 0x40dc

   __DATA_CONST.__mod_term_func: 0x18
   __DATA_CONST.__const: 0x17b8
   __DATA_CONST.__kalloc_type: 0x140
-  UUID: B2E968F2-F5C7-3D3E-ABB7-AEFAF09C799C
+  UUID: 406B76FF-9E69-30F0-A4E4-E6394DAC9DBE
   Functions: 76
   Symbols:   0
   CStrings:  21

```

>  `com.apple.driver.usb.cdc.ncm`

```diff

-341.120.1.0.1
+341.120.2.0.0
   __TEXT.__const: 0x78
   __TEXT.__cstring: 0xcba
   __TEXT_EXEC.__text: 0x8a2c

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xf48
   __DATA_CONST.__kalloc_type: 0x100
-  UUID: 2E75A747-168A-3B52-AF0F-3D5C5F36274D
+  UUID: B1629869-52F2-3B50-A322-854F9416B8B8
   Functions: 102
   Symbols:   0
   CStrings:  120

```

>  `com.apple.driver.usb.ethernet.asix`

```diff

-341.120.1.0.1
+341.120.2.0.0
   __TEXT.__cstring: 0xe36
   __TEXT.__const: 0x270
   __TEXT_EXEC.__text: 0x12574

   __DATA_CONST.__mod_term_func: 0x20
   __DATA_CONST.__const: 0x2538
   __DATA_CONST.__kalloc_type: 0x100
-  UUID: 3C42D5C7-1D8D-33B0-AB93-C8EB30337083
+  UUID: 72331F9F-A207-335C-A3F1-9D753C05418E
   Functions: 153
   Symbols:   0
   CStrings:  111

```

>  `com.apple.driver.usb.networking`

```diff

-341.120.1.0.1
+341.120.2.0.0
   __TEXT.__cstring: 0x24a
   __TEXT_EXEC.__text: 0x215c
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__mod_term_func: 0x8
   __DATA_CONST.__const: 0x438
   __DATA_CONST.__kalloc_type: 0xc0
-  UUID: E79ABA26-AD2F-36FA-BBBD-C8CC80B6CF72
+  UUID: 161593B3-6058-360C-BEBF-AE66F51D7F98
   Functions: 52
   Symbols:   0
   CStrings:  25

```

>  `com.apple.filesystems.apfs`

```diff

-2236.122.2.0.0
+2236.140.6.0.0
   __TEXT.__const: 0x6a8
-  __TEXT.__cstring: 0x45e95
-  __TEXT_EXEC.__text: 0x130f80
+  __TEXT.__cstring: 0x45f11
+  __TEXT_EXEC.__text: 0x131130
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x688
   __DATA.__bss: 0xc60

   __DATA_CONST.__const: 0x5d80
   __DATA_CONST.__kalloc_type: 0x4dc0
   __DATA_CONST.__kalloc_var: 0x2800
-  UUID: 2A9FCB3B-81F0-3531-9D63-142B470238ED
+  UUID: D5F4EB78-E4DA-3705-9126-FC0BBEA3EB7F
   Functions: 1855
   Symbols:   0
-  CStrings:  6116
+  CStrings:  6118
 
CStrings:
+ "%s:%d: Volume role 0x%x is not supported in container\n"
+ "%s:%d: cannot change role of Backup volume\n"
+ "%s:%d: cannot change role of SideCar volume\n"
+ "18:08:38"
+ "2024/07/05"
+ "2236.140.6"
+ "Jul  5 2024"
+ "apfs-2236.140.6"
+ "com.apple.private.apfs.change-special-role"
- "%s:%d: Volume role 0x%x is not supported in container"
- "2024/05/01"
- "20:15:58"
- "20:15:59"
- "2236.122.2"
- "May  1 2024"
- "apfs-2236.122.2"

```

>  `com.apple.filesystems.hfs.kext`

```diff

-650.120.1.0.0
+650.140.2.0.0
   __TEXT.__const: 0x1a80
   __TEXT.__cstring: 0xa17d
-  __TEXT_EXEC.__text: 0x51a04
+  __TEXT_EXEC.__text: 0x51a54
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x4d0
   __DATA.__common: 0x10

   __DATA_CONST.__const: 0xf50
   __DATA_CONST.__kalloc_type: 0x3340
   __DATA_CONST.__kalloc_var: 0x690
-  UUID: CE47FBB1-E826-36CC-BD09-1A538FE04EFF
+  UUID: 0C15001E-D646-3086-8135-568143F3867A
   Functions: 477
   Symbols:   0
   CStrings:  872

```

>  `com.apple.filesystems.lifs`

```diff

-208.120.7.0.3
+208.140.4.0.0
   __TEXT.__os_log: 0x11c5
   __TEXT.__cstring: 0x1d28
   __TEXT.__const: 0x290
-  __TEXT_EXEC.__text: 0x19f88
+  __TEXT_EXEC.__text: 0x1a088
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x5d0
   __DATA.__common: 0x138

   __DATA_CONST.__mod_term_func: 0x18
   __DATA_CONST.__const: 0x1688
   __DATA_CONST.__kalloc_type: 0xb40
-  UUID: 3E0CAC76-8BC6-3B37-8FC0-3DB54A05B44D
-  Functions: 304
+  UUID: F1E1A002-D9A3-3156-9B11-0E09503A2951
+  Functions: 305
   Symbols:   0
   CStrings:  355
 

```

>  `com.apple.iokit.IOMIPIFamily`

```diff

-142.100.2.0.0
+142.140.1.0.0
   __TEXT.__const: 0x20
   __TEXT.__cstring: 0x1f5
-  __TEXT_EXEC.__text: 0x111c
+  __TEXT_EXEC.__text: 0x1138
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xc70
   __DATA_CONST.__kalloc_type: 0x80
-  UUID: 2B3F2DBB-0CC4-3419-A267-15942F37ECDD
+  UUID: 98267C11-009E-3A6D-AEFB-9479685AC643
   Functions: 30
   Symbols:   0
   CStrings:  13

```

>  `com.apple.iokit.IOMobileGraphicsFamily`

```diff

-337.7.12.5.0
-  __TEXT.__cstring: 0x87b4
+338.2.9.0.0
+  __TEXT.__cstring: 0x87bf
   __TEXT.__const: 0x938
-  __TEXT_EXEC.__text: 0x420e8
+  __TEXT_EXEC.__text: 0x42164
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2908
   __DATA.__common: 0x1c9a4

   __DATA_CONST.__got: 0x120
   __DATA_CONST.__mod_init_func: 0x50
   __DATA_CONST.__mod_term_func: 0x50
-  __DATA_CONST.__const: 0x5160
+  __DATA_CONST.__const: 0x5170
   __DATA_CONST.__kalloc_type: 0xac0
-  UUID: 872ED87D-C457-33BD-AD10-34FBDEFA7478
+  UUID: 12022191-9423-30AE-8C84-F9AC65E7103D
   Functions: 898
   Symbols:   0
-  CStrings:  983
+  CStrings:  984
 
CStrings:
+ "IOMFB: attempt to use invalid PBT type %d\n"
+ "null descs_ptr\n"
- "\"IOMFB: attempt to use invalid PBT type\" @%s:%d"

```

>  `com.apple.iokit.IOMobileGraphicsFamily-DCP`

```diff

-337.7.12.5.0
-  __TEXT.__cstring: 0x4511
+338.2.9.0.0
+  __TEXT.__cstring: 0x4539
   __TEXT.__const: 0x23a1
-  __TEXT_EXEC.__text: 0x419cc
+  __TEXT_EXEC.__text: 0x41a2c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xf8
   __DATA.__common: 0x26f8

   __DATA_CONST.__mod_term_func: 0x28
   __DATA_CONST.__const: 0x1740
   __DATA_CONST.__kalloc_type: 0x880
-  UUID: 3E5FC177-11DC-3018-B0C0-5E2CB6E5FE73
+  UUID: F0F080F2-DC5D-3215-A71A-479757A6C9B6
   Functions: 826
   Symbols:   0
   CStrings:  396
CStrings:
+ "get_clamshell_state fAPClamshellState %d from_kernel %d fReceivedClamshellStateFromSkyLight %d \n"
- "get_clamshell_state fAPClamshellState %d from_kernel %d\n"

```

>  `com.apple.iokit.IONVMeFamily`

```diff

-732.120.3.0.0
-  __TEXT.__cstring: 0xf4df
+732.140.2.0.0
+  __TEXT.__cstring: 0xf51d
   __TEXT.__const: 0x688
-  __TEXT_EXEC.__text: 0x580c0
+  __TEXT_EXEC.__text: 0x58110
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x534
   __DATA.__common: 0x500

   __DATA_CONST.__const: 0xc138
   __DATA_CONST.__kalloc_type: 0x780
   __DATA_CONST.__kalloc_var: 0x5f0
-  UUID: 4158D903-748D-3B8B-A0D9-1B7E3910210A
+  UUID: 53320D46-2640-3E61-82CB-F3D4B04C88AE
   Functions: 1026
   Symbols:   0
-  CStrings:  1678
+  CStrings:  1679
 
CStrings:
+ "\"pmap_iommu_alloc_contiguous_pages failed: size=%qd\\n\" @%s:%d"

```

>  `com.apple.iokit.IOPCIFamily`

```diff

   __DATA_CONST.__const: 0x3c98
   __DATA_CONST.__kalloc_type: 0x600
   __DATA_CONST.__kalloc_var: 0x190
-  UUID: 569B40A9-AB24-3AE6-B44C-A28058A8E88E
+  UUID: 0560F9C4-6E89-3860-BAE7-E09B6EFA2CE0
   Functions: 433
   Symbols:   0
   CStrings:  635
CStrings:
+ "18:02:27"
+ "Jul  5 2024"
- "20:13:38"
- "May  1 2024"

```

>  `com.apple.iokit.IOThunderboltFamily`

```diff

   __DATA_CONST.__const: 0x1cf40
   __DATA_CONST.__kalloc_type: 0x1d00
   __DATA_CONST.__kalloc_var: 0x910
-  UUID: 12770770-9D16-3994-A637-320D9264FBD6
+  UUID: 773BCD1A-61B5-3CEE-86EB-40D24887CD9F
   Functions: 2781
   Symbols:   0
   CStrings:  2678
CStrings:
+ "18:02:28"
+ "Jul  5 2024"
- "07:23:18"
- "May  2 2024"

```

>  `com.apple.iokit.IOTimeSyncFamily`

```diff

-1250.2.0.0.0
+1240.15.0.0.0
   __TEXT.__cstring: 0x31ac
   __TEXT.__os_log: 0x6fa2
   __TEXT.__const: 0x1d8

   __DATA_CONST.__const: 0xbe08
   __DATA_CONST.__kalloc_type: 0xbc0
   __DATA_CONST.__kalloc_var: 0x280
-  UUID: 1FEF32B7-BA40-3A57-8D90-EF10F397B47E
+  UUID: 318B64A6-E8BD-3DE2-B5E5-3D8ED3C0A2C4
   Functions: 762
   Symbols:   0
   CStrings:  603

```

>  `com.apple.iokit.IOUSBHostFamily`

```diff

-1337.120.6.0.0
+1337.140.2.0.0
   __TEXT.__cstring: 0x9912
   __TEXT.__os_log: 0x814a
   __TEXT.__const: 0xa30

   __DATA_CONST.__const: 0xcb50
   __DATA_CONST.__kalloc_type: 0x1cc0
   __DATA_CONST.__kalloc_var: 0x280
-  UUID: C8E2C0F3-9EE7-3DF9-9A1E-576A0D6A2002
+  UUID: AAC55435-4A94-34A4-BC46-02439659C2FB
   Functions: 1171
   Symbols:   0
   CStrings:  1534

```

>  `com.apple.iokit.IOUserEthernet`

```diff

 74.0.0.0.0
   __TEXT.__const: 0x18
-  __TEXT.__cstring: 0x9f0
+  __TEXT.__cstring: 0xa0a
   __TEXT_EXEC.__text: 0x5438
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8

   __DATA_CONST.__mod_term_func: 0x20
   __DATA_CONST.__const: 0x1d30
   __DATA_CONST.__kalloc_type: 0x180
-  UUID: 797F2374-4555-333D-8A15-894E69023A1C
+  UUID: B97F1551-8C8E-3972-BEBF-DACD36830C27
   Functions: 95
   Symbols:   0
   CStrings:  103
CStrings:
+ "v32@?0^{?=II^{ipc_port}^{ipc_port}Ii}8^(?={?=(?=^{ipc_port}^{ipc_port}^{ipc_port})b16b8b8I}{?=IIb8b8b8b8}{?=IIb8b8b8b8}{?=IIb24b8}{?=IIb16b8b8})16^v24"
- "v32@?0^{?=II^{ipc_port}^{ipc_port}Ii}8^(?={?=^{ipc_port}b16b8b8I}{?=IIb8b8b8b8}{?=IIb8b8b8b8}{?=IIb24b8}{?=IIb16b8b8})16^v24"

```

>  `com.apple.kec.corecrypto`

```diff

-1638.100.62.0.0
+1638.140.6.0.0
   __TEXT.__cstring: 0x4693
-  __TEXT.__const: 0x14150
+  __TEXT.__const: 0x14130
   __TEXT.__fips_hmacs: 0x20
-  __TEXT_EXEC.__text: 0x511bc
+  __TEXT_EXEC.__text: 0x517bc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2df0
   __DATA.__bss: 0x2960

   __DATA_CONST.__got: 0x10
   __DATA_CONST.__auth_ptr: 0x120
   __DATA_CONST.__const: 0x28f8
-  UUID: 6F0ADEB3-6F4E-340A-A8B7-B934314CE848
-  Functions: 852
+  UUID: FB73D389-7D00-366B-8BC7-F0EBC7C2DFE7
+  Functions: 857
   Symbols:   0
   CStrings:  539
 

```

>  `com.apple.kernel`

```diff

-10063.122.3.0.0
+10063.142.1.0.0
   __TEXT.__const: 0x340c0
   __TEXT.__copyio_vectors: 0xf0
-  __TEXT.__cstring: 0x65664
+  __TEXT.__cstring: 0x65487
   __TEXT.__os_log: 0x228f2
   __TEXT.__eh_frame: 0x4c0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x2c0
-  __DATA_CONST.__const: 0xa1f98
+  __DATA_CONST.__const: 0xa1ef8
   __DATA_CONST.__hib_const: 0x140
   __DATA_CONST.__kalloc_type: 0x12d00
-  __DATA_CONST.__kalloc_var: 0x7800
+  __DATA_CONST.__kalloc_var: 0x7620
   __DATA_CONST.__brk_desc: 0x60
   __DATA_SPTM.__const: 0x3c000
   __TEXT_EXEC.__hib_text: 0xd28
-  __TEXT_EXEC.__text: 0x74cba4
+  __TEXT_EXEC.__text: 0x74eee4
   __TEXT_BOOT_EXEC.__bootcode: 0x4cf8
   __KLD.__text: 0x1644
   __LASTDATA_CONST.__mod_init_func: 0x8

   __KLDDATA.__bss: 0x1
   __DATA.__data: 0x17aa9
   __DATA.__lock_grp: 0x5800
-  __DATA.__percpu: 0x4e50
-  __DATA.__common: 0x577d0
+  __DATA.__percpu: 0x4e40
+  __DATA.__common: 0x577c0
   __DATA.__bss: 0x3d220
   __BOOTDATA.__data: 0x18000
   __BOOTDATA.__init: 0x5b0e8
-  __BOOTDATA.__init_entry_set: 0x10230
+  __BOOTDATA.__init_entry_set: 0x10200
   __PRELINK_TEXT.__text: 0x0
   __PRELINK_INFO.__info: 0x0
   __PLK_TEXT_EXEC.__text: 0x0

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x44bf2
-  UUID: 6273B14D-2BFC-3178-B28A-8721E2C2419E
-  Functions: 19223
+  UUID: 05694318-9654-392B-9425-CEBB3A03ED48
+  Functions: 19237
   Symbols:   0
-  CStrings:  15933
+  CStrings:  15920
 
CStrings:
+ "%s: mach_msg_send_from_kernel(0x%x)\n"
+ "8"
+ "IPC kmsg header signature mismatch: kmsg=%p, hdr=%p, id=%d, sig=0x%08x (expected 0x%08x) @%s:%d"
+ "Invalid descriptor type (%p: %d) @%s:%d"
+ "b2"
+ "site.mach_msg_base_t.mach_msg_kdescriptor_t"
+ "site.mach_port_ool_t"
+ "v & IKM_KEEP_ALIVE_IN_USE"
+ "v & IKM_KEEP_ALIVE_OWNED"
+ "v32@?0^{?=II^{ipc_port}^{ipc_port}Ii}8^(?={?=(?=^{ipc_port}^{ipc_port}^{ipc_port})b16b8b8I}{?=IIb8b8b8b8}{?=IIb8b8b8b8}{?=IIb24b8}{?=IIb16b8b8})16^v24"
+ "vnode_waitformount"
- "%s: mach_msg_send_from_kernel_proper(0x%x)\n"
- "32"
- "Message signature failure count"
- "WindowServer VM Debugging panic: address 0x%llx copy ptr %p size 0x%llx @%s:%d"
- "full"
- "header trailer"
- "ikm_signature_failure_id"
- "ikm_signature_failures"
- "ikm_validate_sig: %s signature mismatch: kmsg=0x%p, id=%d, sig=0x%zx (expected 0x%zx) @%s:%d"
- "invalid descriptor type %d @%s:%d"
- "invalid descriptor type @%s:%d"
- "invalid descriptor type: (%p: %d) @%s:%d"
- "ipc_kmsg_body_sig: invalid message descriptor @%s:%d"
- "ipc_kmsg_free: invalid kmsg (%p) header @%s:%d"
- "message.h"
- "mk_timer.c"
- "port %p / mktimer %p: circularity check failed @%s:%d"
- "port(%p, %p): prealloc message in an invalid state @%s:%d"
- "round msg overflow @%s:%d"
- "site.mach_msg_base_t.mach_msg_descriptor_t"
- "site.mach_port_t"
- "site.void *"
- "untyped IPC copyout body: invalid message descriptor @%s:%d"
- "v32@?0^{?=II^{ipc_port}^{ipc_port}Ii}8^(?={?=^{ipc_port}b16b8b8I}{?=IIb8b8b8b8}{?=IIb8b8b8b8}{?=IIb24b8}{?=IIb16b8b8})16^v24"

```

>  `com.apple.plugin.IOgPTPPlugin`

```diff

-1250.2.0.0.0
-  __TEXT.__cstring: 0x6101
-  __TEXT.__os_log: 0x1a273
+1240.15.0.0.0
+  __TEXT.__cstring: 0x6112
+  __TEXT.__os_log: 0x1a26b
   __TEXT.__const: 0x290
-  __TEXT_EXEC.__text: 0x75b98
+  __TEXT_EXEC.__text: 0x75ad8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xcc
   __DATA.__common: 0x5d8
-  __DATA_CONST.__auth_got: 0x708
+  __DATA_CONST.__auth_got: 0x700
   __DATA_CONST.__got: 0x1b8
   __DATA_CONST.__mod_init_func: 0x110
   __DATA_CONST.__mod_term_func: 0x110
   __DATA_CONST.__const: 0xeab8
   __DATA_CONST.__kalloc_type: 0x940
   __DATA_CONST.__kalloc_var: 0x280
-  UUID: 0807651C-6D05-3356-9DF7-E855BBF5E88B
-  Functions: 929
+  UUID: 2A0EC10A-C6AB-3106-AF45-36AF87C754FD
+  Functions: 928
   Symbols:   0
   CStrings:  1416
 
CStrings:
+ "IOTimeSyncgPTPManager::addInterfaceAdapterForInterface error %u getting address"
+ "ifnet != nullptr"
- "findMacAddress error %u getting address"
- "findMacAddress: Failed to find the %s interface"

```

>  `com.apple.security.AppleImage4`

```diff

-257.120.3.0.0
+257.140.2.0.0
   __TEXT.__const: 0x6ad8
-  __TEXT.__cstring: 0x528b
+  __TEXT.__cstring: 0x528d
   __TEXT_EXEC.__text: 0x20464
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x640

   __DATA_CONST.__const: 0xa968
   __DATA_CONST.__kalloc_type: 0x180
   __DATA_CONST.__image4_exp: 0x10
-  UUID: 3BBF2219-D889-3CCB-A3B1-0383B0426488
+  UUID: D32AAF5E-C479-3E65-99BF-16EF37AC71CE
   Functions: 674
   Symbols:   0
   CStrings:  684
CStrings:
+ "257.140.2"
+ "@(#)VERSION:Darwin Image4 Validator Version 6.3.0: Fri Jul  5 17:58:17 PDT 2024; root:AppleImage4-257.140.2~228/AppleImage4/RELEASE_ARM64E"
+ "Darwin Image4 Validator Version 6.3.0: Fri Jul  5 17:58:17 PDT 2024; root:AppleImage4-257.140.2~228/AppleImage4/RELEASE_ARM64E"
- "257.120.3"
- "@(#)VERSION:Darwin Image4 Validator Version 6.3.0: Wed May  1 20:13:19 PDT 2024; root:AppleImage4-257.120.3~72/AppleImage4/RELEASE_ARM64E"
- "Darwin Image4 Validator Version 6.3.0: Wed May  1 20:13:19 PDT 2024; root:AppleImage4-257.120.3~72/AppleImage4/RELEASE_ARM64E"

```

>  `com.apple.security.sandbox`

```diff

-2190.120.12.0.0
-  __TEXT.__const: 0x171dd9
+2190.140.13.0.0
+  __TEXT.__const: 0x16eb79
   __TEXT.__cstring: 0x6549
   __TEXT.__os_log: 0x1cbb
-  __TEXT_EXEC.__text: 0x2e4b0
+  __TEXT_EXEC.__text: 0x2e480
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x1e0
   __DATA.__bss: 0x144d0

   __DATA_CONST.__const: 0x3450
   __DATA_CONST.__kalloc_var: 0x550
   __DATA_CONST.__kalloc_type: 0xb40
-  UUID: 0DD64D5C-67F9-3A17-8702-0B0126F93DA2
-  Functions: 541
+  UUID: 96F87881-BA14-3AB9-ACC0-3EF14E696766
+  Functions: 539
   Symbols:   0
   CStrings:  1232
 

```

</details>

## MachO

### 🆕 NEW (1)

- `/System/Library/Snippets/UIPlugins/SiriKitUIPlugin.bundle/SiriKitUIPlugin`

### ❌ Removed (1)

- `/System/Library/PreferenceBundles/ContactlessAndCredentialSettings.bundle/ContactlessAndCredentialSettings`

### ⬆️ Updated (2754)

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
- [/Applications/AppDistributionLaunchAngel.app/AppDistributionLaunchAngel](MACHOS/AppDistributionLaunchAngel.md)
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
- [/Applications/AutoSettings.app/AutoSettings](MACHOS/AutoSettings.md)
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
- [/Applications/CarCamera.app/CarCamera](MACHOS/CarCamera.md)
- [/Applications/CarPlaySettings.app/CarPlaySettings](MACHOS/CarPlaySettings.md)
- [/Applications/CarPlaySetup.app/CarPlaySetup](MACHOS/CarPlaySetup.md)
- [/Applications/CarPlaySplashScreen.app/CarPlaySplashScreen](MACHOS/CarPlaySplashScreen.md)
- [/Applications/CarPlayWallpaper.app/CarPlayWallpaper](MACHOS/CarPlayWallpaper.md)
- [/Applications/Charge.app/Charge](MACHOS/Charge.md)
- [/Applications/CheckerBoard.app/CheckerBoard](MACHOS/CheckerBoard.md)
- [/Applications/CheckerBoardRemoteSetup.app/CheckerBoardRemoteSetup](MACHOS/CheckerBoardRemoteSetup.md)
- [/Applications/ClarityCamera.app/ClarityCamera](MACHOS/ClarityCamera.md)
- [/Applications/ClarityPhotos.app/ClarityPhotos](MACHOS/ClarityPhotos.md)
- [/Applications/Climate.app/Climate](MACHOS/Climate.md)
- [/Applications/ClipViewService.app/ClipViewService](MACHOS/ClipViewService.md)
- [/Applications/ClockAngel.app/ClockAngel](MACHOS/ClockAngel.md)
- [/Applications/Closures.app/Closures](MACHOS/Closures.md)
- [/Applications/ColorPickerUIService.app/ColorPickerUIService](MACHOS/ColorPickerUIService.md)
- [/Applications/CompanionServicesViewService.app/CompanionServicesViewService](MACHOS/CompanionServicesViewService.md)
- [/Applications/CompassCalibrationViewService.app/CompassCalibrationViewService](MACHOS/CompassCalibrationViewService.md)
- [/Applications/ContactPhotoCarouselRemoteAlert.app/ContactPhotoCarouselRemoteAlert](MACHOS/ContactPhotoCarouselRemoteAlert.md)
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
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6004.appex/Diagnostic-6004](MACHOS/Diagnostic-6004.md)
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
- [/Applications/Media.app/Media](MACHOS/Media.md)
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
- [/Applications/ProximityReaderSceneUI.app/ProximityReaderSceneUI](MACHOS/ProximityReaderSceneUI.md)
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
- [/Applications/TirePressure.app/TirePressure](MACHOS/TirePressure.md)
- [/Applications/Trip.app/Trip](MACHOS/Trip.md)
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
- [/System/Library/Audio/Plug-Ins/HAL/BuiltinAudioPlugin.driver/BuiltinAudioPlugin](MACHOS/BuiltinAudioPlugin.md)
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
- [/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices-0002.bundle/MobileDevices-0002](MACHOS/MobileDevices-0002.md)
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
- [/System/Library/ExtensionKit/Extensions/ADFollowUpExtension.appex/ADFollowUpExtension](MACHOS/ADFollowUpExtension.md)
- [/System/Library/ExtensionKit/Extensions/AppExtensionManagement.appex/AppExtensionManagement](MACHOS/AppExtensionManagement.md)
- [/System/Library/ExtensionKit/Extensions/AppStoreEvalLighthouseWorker.appex/AppStoreEvalLighthouseWorker](MACHOS/AppStoreEvalLighthouseWorker.md)
- [/System/Library/ExtensionKit/Extensions/BitacoraWorker.appex/BitacoraWorker](MACHOS/BitacoraWorker.md)
- [/System/Library/ExtensionKit/Extensions/ComposeReviewExtension.appex/ComposeReviewExtension](MACHOS/ComposeReviewExtension.md)
- [/System/Library/ExtensionKit/Extensions/DeepThoughtWorker.appex/DeepThoughtWorker](MACHOS/DeepThoughtWorker.md)
- [/System/Library/ExtensionKit/Extensions/DevicePropertiesExtension.appex/DevicePropertiesExtension](MACHOS/DevicePropertiesExtension.md)
- [/System/Library/ExtensionKit/Extensions/EventKitUIRemoteUIExtension.appex/EventKitUIRemoteUIExtension](MACHOS/EventKitUIRemoteUIExtension.md)
- [/System/Library/ExtensionKit/Extensions/ExperimentationExtension.appex/ExperimentationExtension](MACHOS/ExperimentationExtension.md)
- [/System/Library/ExtensionKit/Extensions/GPUExtension.appex/com.apple.WebKit.GPU](MACHOS/com.apple.WebKit.GPU.md)
- [/System/Library/ExtensionKit/Extensions/LighthouseNightingaleExtension.appex/LighthouseNightingaleExtension](MACHOS/LighthouseNightingaleExtension.md)
- [/System/Library/ExtensionKit/Extensions/MADViewServiceExtension.appex/MADViewServiceExtension](MACHOS/MADViewServiceExtension.md)
- [/System/Library/ExtensionKit/Extensions/MapsTransactionInsightsExtension.appex/MapsTransactionInsightsExtension](MACHOS/MapsTransactionInsightsExtension.md)
- [/System/Library/ExtensionKit/Extensions/MercuryPosterExtension.appex/MercuryPosterExtension](MACHOS/MercuryPosterExtension.md)
- [/System/Library/ExtensionKit/Extensions/MetricsExtension.appex/MetricsExtension](MACHOS/MetricsExtension.md)
- [/System/Library/ExtensionKit/Extensions/MusicEngagementExtension.appex/MusicEngagementExtension](MACHOS/MusicEngagementExtension.md)
- [/System/Library/ExtensionKit/Extensions/NetworkingExtension.appex/com.apple.WebKit.Networking](MACHOS/com.apple.WebKit.Networking.md)
- [/System/Library/ExtensionKit/Extensions/PFLHRPeriodPredCK.appex/PFLHRPeriodPredCK](MACHOS/PFLHRPeriodPredCK.md)
- [/System/Library/ExtensionKit/Extensions/PFLHRPeriodPredMLH.appex/PFLHRPeriodPredMLH](MACHOS/PFLHRPeriodPredMLH.md)
- [/System/Library/ExtensionKit/Extensions/PFLHRPeriodPredPush.appex/PFLHRPeriodPredPush](MACHOS/PFLHRPeriodPredPush.md)
- [/System/Library/ExtensionKit/Extensions/PridePosterExtension.appex/PridePosterExtension](MACHOS/PridePosterExtension.md)
- [/System/Library/ExtensionKit/Extensions/ProactiveShareSheetLighthouseBackgroundPlugin.appex/ProactiveShareSheetLighthouseBackgroundPlugin](MACHOS/ProactiveShareSheetLighthouseBackgroundPlugin.md)
- [/System/Library/ExtensionKit/Extensions/RepackagingWorker.appex/RepackagingWorker](MACHOS/RepackagingWorker.md)
- [/System/Library/ExtensionKit/Extensions/SiriCoreMetricsWorker.appex/SiriCoreMetricsWorker](MACHOS/SiriCoreMetricsWorker.md)
- [/System/Library/ExtensionKit/Extensions/SiriMASPFLCK.appex/SiriMASPFLCK](MACHOS/SiriMASPFLCK.md)
- [/System/Library/ExtensionKit/Extensions/SiriMASPFLPlugin.appex/SiriMASPFLPlugin](MACHOS/SiriMASPFLPlugin.md)
- [/System/Library/ExtensionKit/Extensions/SiriMASPFLPush.appex/SiriMASPFLPush](MACHOS/SiriMASPFLPush.md)
- [/System/Library/ExtensionKit/Extensions/SiriSuggestionsLightHousePlugin.appex/SiriSuggestionsLightHousePlugin](MACHOS/SiriSuggestionsLightHousePlugin.md)
- [/System/Library/ExtensionKit/Extensions/SiriUserSegmentation.appex/SiriUserSegmentation](MACHOS/SiriUserSegmentation.md)
- [/System/Library/ExtensionKit/Extensions/WebContentCaptivePortalExtension.appex/com.apple.WebKit.WebContent.CaptivePortal](MACHOS/com.apple.WebKit.WebContent.CaptivePortal.md)
- [/System/Library/ExtensionKit/Extensions/WebContentExtension.appex/com.apple.WebKit.WebContent](MACHOS/com.apple.WebKit.WebContent.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.fskit.exfat.appex/com.apple.fskit.exfat](MACHOS/com.apple.fskit.exfat.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.fskit.msdos.appex/com.apple.fskit.msdos](MACHOS/com.apple.fskit.msdos.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.mlhost.CloudWorker.appex/com.apple.mlhost.CloudWorker](MACHOS/com.apple.mlhost.CloudWorker.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.mlhost.QuartzWorker.appex/com.apple.mlhost.QuartzWorker](MACHOS/com.apple.mlhost.QuartzWorker.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.mlhost.SampleWorker.appex/com.apple.mlhost.SampleWorker](MACHOS/com.apple.mlhost.SampleWorker.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.mlhost.TelemetryWorker.appex/com.apple.mlhost.TelemetryWorker](MACHOS/com.apple.mlhost.TelemetryWorker.md)
- [/System/Library/Extensions/AppleBiometricSensor.kext/PlugIns/AppleMesaLib.plugin/AppleMesaLib](MACHOS/AppleMesaLib.md)
- [/System/Library/Extensions/AppleGameControllerPersonality.kext/AppleGameControllerPersonality](MACHOS/AppleGameControllerPersonality.md)
- [/System/Library/Extensions/AppleHIDALSService.kext/PlugIns/AppleHIDALS.plugin/AppleHIDALS](MACHOS/AppleHIDALS.md)
- [/System/Library/Extensions/AppleHPM.kext/PlugIns/AppleHPMLib.plugin/AppleHPMLib](MACHOS/AppleHPMLib.md)
- [/System/Library/Extensions/AppleSPU.kext/PlugIns/FastpathLib.plugin/FastpathLib](MACHOS/FastpathLib.md)
- [/System/Library/Extensions/AppleSPURose.kext/PlugIns/RoseControllerLib.plugin/RoseControllerLib](MACHOS/RoseControllerLib.md)
- [/System/Library/Extensions/AppleUVDM.kext/PlugIns/AppleUVDMLib.plugin/AppleUVDMLib](MACHOS/AppleUVDMLib.md)
- [/System/Library/Extensions/EAP-RSA.ppp/EAP-RSA](MACHOS/EAP-RSA.md)
- [/System/Library/Extensions/EXBrightKext.kext/EXBrightKext](MACHOS/EXBrightKext.md)
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
- [/System/Library/Frameworks/AdAttributionKit.framework/Support/attributionkitd](MACHOS/attributionkitd.md)
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
- [/System/Library/Frameworks/HealthKit.framework/PlugIns/com.apple.HealthKit.HealthResearchLogsDiagnosticExtension.appex/com.apple.HealthKit.HealthResearchLogsDiagnosticExtension](MACHOS/com.apple.HealthKit.HealthResearchLogsDiagnosticExtension.md)
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
- [/System/Library/Frameworks/ManagedAppDistribution.framework/Support/applicensedeliveryd](MACHOS/applicensedeliveryd.md)
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
- [/System/Library/Frameworks/SensorKit.framework/XPCServices/SensorKitLongTermStorageHelper.xpc/SensorKitLongTermStorageHelper](MACHOS/SensorKitLongTermStorageHelper.md)
- [/System/Library/Frameworks/SensorKit.framework/XPCServices/com.apple.SensorKit.CHSupportService.xpc/com.apple.SensorKit.CHSupportService](MACHOS/com.apple.SensorKit.CHSupportService.md)
- [/System/Library/Frameworks/SensorKit.framework/XPCServices/com.apple.SensorKitAppHelper.xpc/com.apple.SensorKitAppHelper](MACHOS/com.apple.SensorKitAppHelper.md)
- [/System/Library/Frameworks/ShazamKit.framework/PlugIns/ShazamNotificationContentExtension.appex/ShazamNotificationContentExtension](MACHOS/ShazamNotificationContentExtension.md)
- [/System/Library/Frameworks/ShazamKit.framework/shazamd](MACHOS/shazamd.md)
- [/System/Library/Frameworks/Speech.framework/XPCServices/localspeechrecognition.xpc/localspeechrecognition](MACHOS/localspeechrecognition.md)
- [/System/Library/Frameworks/StoreKit.framework/PlugIns/SKAskPermissionExtension.appex/SKAskPermissionExtension](MACHOS/SKAskPermissionExtension.md)
- [/System/Library/Frameworks/StoreKit.framework/Support/storekitd](MACHOS/storekitd.md)
- [/System/Library/Frameworks/SystemConfiguration.framework/SCHelper](MACHOS/SCHelper.md)
- [/System/Library/Frameworks/Translation.framework/translationd](MACHOS/translationd.md)
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
- [/System/Library/Frameworks/WebKit.framework/Frameworks/libWebKitSwift.dylib](MACHOS/libWebKitSwift.dylib.md)
- [/System/Library/Frameworks/_DeviceActivity_SwiftUI.framework/PlugIns/DeviceActivityReportService.appex/DeviceActivityReportService](MACHOS/DeviceActivityReportService.md)
- [/System/Library/HIDPlugins/ColourSensorFilterPlugin.plugin/ColourSensorFilterPlugin](MACHOS/ColourSensorFilterPlugin.md)
- [/System/Library/HIDPlugins/ServiceFilters/AppleDeviceManagementHIDFilter.plugin/AppleDeviceManagementHIDFilter](MACHOS/AppleDeviceManagementHIDFilter.md)
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
- [/System/Library/NanoTimeKit/FaceBundles/NTKPlumeriaFaceBundleCompanion.bundle/NTKPlumeriaFaceBundleCompanion](MACHOS/NTKPlumeriaFaceBundleCompanion.md)
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
- [/System/Library/PreferenceBundles/AppInstallationSettings.bundle/AppInstallationSettings](MACHOS/AppInstallationSettings.md)
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
- [/System/Library/PreferenceBundles/Privacy/WalletPrivacySettings.bundle/WalletPrivacySettings](MACHOS/WalletPrivacySettings.md)
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
- [/System/Library/PrivateFrameworks/CascadeSets.framework/XPCServices/SetStoreUpdateService.xpc/SetStoreUpdateService](MACHOS/SetStoreUpdateService.md)
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
- [/System/Library/PrivateFrameworks/CoreRepairCore.framework/XPCServices/CoreRepairCoreXPCService.xpc/CoreRepairCoreXPCService](MACHOS/CoreRepairCoreXPCService.md)
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
- [/System/Library/PrivateFrameworks/DendriteIngest.framework/XPCServices/IngestService.xpc/IngestService](MACHOS/IngestService.md)
- [/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/DesktopServicesHelper](MACHOS/DesktopServicesHelper.md)
- [/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/XPCServices/ArchiveService.xpc/ArchiveService](MACHOS/ArchiveService.md)
- [/System/Library/PrivateFrameworks/DeviceCheckInternal.framework/devicecheckd](MACHOS/devicecheckd.md)
- [/System/Library/PrivateFrameworks/DeviceToDeviceManager.framework/PlugIns/BTD2DPlugin.bundle/BTD2DPlugin](MACHOS/BTD2DPlugin.md)
- [/System/Library/PrivateFrameworks/DeviceToDeviceManager.framework/PlugIns/WiFiAwareD2DPlugin.bundle/WiFiAwareD2DPlugin](MACHOS/WiFiAwareD2DPlugin.md)
- [/System/Library/PrivateFrameworks/DeviceToDeviceManager.framework/PlugIns/WiFiD2DPlugin.bundle/WiFiD2DPlugin](MACHOS/WiFiD2DPlugin.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/AudioDiagnosticExtension.appex/AudioDiagnosticExtension](MACHOS/AudioDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/BluetoothHeadset.appex/BluetoothHeadset](MACHOS/BluetoothHeadset.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/ContinuousRecordingsDiagnosticExtension.appex/ContinuousRecordingsDiagnosticExtension](MACHOS/ContinuousRecordingsDiagnosticExtension.md)
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
- [/System/Library/PrivateFrameworks/FileProviderDaemon.framework/XPCServices/FPCKService.xpc/FPCKService](MACHOS/FPCKService.md)
- [/System/Library/PrivateFrameworks/FinHealth.framework/ClientTools/finhealth_client](MACHOS/finhealth_client.md)
- [/System/Library/PrivateFrameworks/FinHealth.framework/ClientTools/finhealthclient](MACHOS/finhealthclient.md)
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
- [/System/Library/PrivateFrameworks/NearFieldPrivateServices.framework/XPCServices/NFRadioPowerSwitch.xpc/NFRadioPowerSwitch](MACHOS/NFRadioPowerSwitch.md)
- [/System/Library/PrivateFrameworks/NearFieldPrivateServices.framework/XPCServices/NFRestoreService.xpc/NFRestoreService](MACHOS/NFRestoreService.md)
- [/System/Library/PrivateFrameworks/NearFieldPrivateServices.framework/XPCServices/NFUIService.xpc/NFUIService](MACHOS/NFUIService.md)
- [/System/Library/PrivateFrameworks/NearbySessions.framework/XPCServices/com.apple.SharePlay.NearbyInvitationsService.xpc/com.apple.SharePlay.NearbyInvitationsService](MACHOS/com.apple.SharePlay.NearbyInvitationsService.md)
- [/System/Library/PrivateFrameworks/NeighborhoodActivityConduit.framework/XPCServices/com.apple.NeighborhoodActivityConduitService.xpc/com.apple.NeighborhoodActivityConduitService](MACHOS/com.apple.NeighborhoodActivityConduitService.md)
- [/System/Library/PrivateFrameworks/NetworkQualityServices.framework/XPCServices/NetworkQualityXPC.xpc/NetworkQualityXPC](MACHOS/NetworkQualityXPC.md)
- [/System/Library/PrivateFrameworks/NetworkRelay.framework/PlugIns/NRDiagnosticExtension.appex/NRDiagnosticExtension](MACHOS/NRDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/PlugIns/NewDeviceOutreachExtension.appex/NewDeviceOutreachExtension](MACHOS/NewDeviceOutreachExtension.md)
- [/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/ndoagent](MACHOS/ndoagent.md)
- [/System/Library/PrivateFrameworks/NewsDaemon.framework/XPCServices/ANFDecoder.xpc/ANFDecoder](MACHOS/ANFDecoder.md)
- [/System/Library/PrivateFrameworks/NewsDaemon.framework/newsd](MACHOS/newsd.md)
- [/System/Library/PrivateFrameworks/NewsServices.framework/PlugIns/NewsArticleViewer.appex/NewsArticleViewer](MACHOS/NewsArticleViewer.md)
- [/System/Library/PrivateFrameworks/NewsServices.framework/nanonewscd](MACHOS/nanonewscd.md)
- [/System/Library/PrivateFrameworks/NewsUI2.framework/XPCServices/TodayFeedConfigDecoder.xpc/TodayFeedConfigDecoder](MACHOS/TodayFeedConfigDecoder.md)
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
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/XPCServices/PPSFeatureFlagReader.xpc/PPSFeatureFlagReader](MACHOS/PPSFeatureFlagReader.md)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/XPCServices/PerfPowerServicesSignpostReader.xpc/PerfPowerServicesSignpostReader](MACHOS/PerfPowerServicesSignpostReader.md)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/XPCServices/rbdcConverter.xpc/rbdcConverter](MACHOS/rbdcConverter.md)
- [/System/Library/PrivateFrameworks/PreviewsOSSupport.framework/Support/previewsd](MACHOS/previewsd.md)
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
- [/System/Library/PrivateFrameworks/SiriUserSegments.framework/PlugIns/SiriUserSegmentsPlugin.appex/SiriUserSegmentsPlugin](MACHOS/SiriUserSegmentsPlugin.md)
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
- [/System/Library/PrivateFrameworks/SonicKit.framework/PlugIns/SonicDiagnostics.appex/SonicDiagnostics](MACHOS/SonicDiagnostics.md)
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
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/RhizomePoster.appex/RhizomePoster](MACHOS/RhizomePoster.md)
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
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/SystemActionConfigurationExtension.appex/SystemActionConfigurationExtension](MACHOS/SystemActionConfigurationExtension.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/WidgetConfigurationExtension.appex/WidgetConfigurationExtension](MACHOS/WidgetConfigurationExtension.md)
- [/System/Library/PrivateFrameworks/WorkoutKitServices.framework/XPCServices/WorkoutKitXPCService.xpc/WorkoutKitXPCService](MACHOS/WorkoutKitXPCService.md)
- [/System/Library/PrivateFrameworks/ZhuGeSupport.framework/XPCServices/ZhuGeService.xpc/ZhuGeService](MACHOS/ZhuGeService.md)
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
- [/System/Library/Snippets/UIPlugins/GeoUIPlugin.bundle/GeoUIPlugin](MACHOS/GeoUIPlugin.md)
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
- [/private/var/staged_system_apps/Books.app/PlugIns/BooksSpotlightExtension.appex/BooksSpotlightExtension](MACHOS/BooksSpotlightExtension.md)
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
- [/usr/libexec/appleh16camerad](MACHOS/appleh16camerad.md)
- [/usr/libexec/appleidsetupd](MACHOS/appleidsetupd.md)
- [/usr/libexec/arkitd](MACHOS/arkitd.md)
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
- [/usr/libexec/caraccessoryd](MACHOS/caraccessoryd.md)
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
- [/usr/libexec/dietapplecamerad](MACHOS/dietapplecamerad.md)
- [/usr/libexec/dietappleh16camerad](MACHOS/dietappleh16camerad.md)
- [/usr/libexec/dirs_cleaner](MACHOS/dirs_cleaner.md)
- [/usr/libexec/diskarbitrationd](MACHOS/diskarbitrationd.md)
- [/usr/libexec/diskimagesiod](MACHOS/diskimagesiod.md)
- [/usr/libexec/dmd](MACHOS/dmd.md)
- [/usr/libexec/dockaccessoryd](MACHOS/dockaccessoryd.md)
- [/usr/libexec/dprivacyd](MACHOS/dprivacyd.md)
- [/usr/libexec/driverkitd](MACHOS/driverkitd.md)
- [/usr/libexec/dtfetchsymbolsd](MACHOS/dtfetchsymbolsd.md)
- [/usr/libexec/duetexpertd](MACHOS/duetexpertd.md)
- [/usr/libexec/eligibilityd](MACHOS/eligibilityd.md)
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
- [/usr/libexec/init_exclavekit](MACHOS/init_exclavekit.md)
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
- [/usr/libexec/soundanalysisd](MACHOS/soundanalysisd.md)
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

### ⬆️ Updated (15)

<details>
  <summary><i>View Updated</i></summary>

#### AppleAVE2FW_H16.im4p

>  `AppleAVE2FW_H16.im4p`

```diff

 
-  __TEXT.__text: 0xb8980
+  __TEXT.__text: 0xb8990
   __TEXT.__cstring: 0x11f2c
   __TEXT.__const: 0x1ca70
   __TEXT.__chain_starts: 0x0

   __DATA._rtk_boot: 0x8000
   __DATA._rtk_page_tables: 0x40000
   __DATA._rtk_power: 0x368
+  __DATA._rtk_data_uuid: 0x0
   __DATA._rtk_tunables: 0x5b0
   __DATA.__mod_init_func: 0x0
   __DATA.__noinit: 0x0
   __DATA._rtk_threads: 0x0
   __DATA._rtk_heap: 0x0
   __DATA.__zerofill: 0xc6880
-  UUID: 74140EE1-9B54-37BF-9706-658E4FF98F63
+  UUID: AE85DAF6-009B-338B-AA7C-1F530B505077
   Functions: 0
   Symbols:   1436
   CStrings:  2018

```

#### SmartIOFirmware_ASCv6.im4p

>  `SmartIOFirmware_ASCv6.im4p`

```diff

 
-  __TEXT.__text: 0x1a454
+  __TEXT.__text: 0x1a464
   __TEXT.__cstring: 0x102c
   __TEXT.__const: 0x338
   __TEXT._rtk_mtab: 0x278

   __DATA._rtk_patchbay: 0x1e8
   __DATA._rtk_tunables: 0x5b0
   __DATA._rtk_power: 0x358
+  __DATA._rtk_data_uuid: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__autobkp: 0x0
   __DATA._rtk_heap: 0x0
   __DATA.__zerofill: 0xcec78
-  UUID: 48F52AE7-AFC2-3D25-A022-C09CB2CA2F5E
+  UUID: 0F352834-94CF-36C5-81C1-FF417B91D343
   Functions: 0
   Symbols:   171
   CStrings:  263

```

#### adc-aceso-d8x.im4p

>  `adc-aceso-d8x.im4p`

```diff

 
-  __TEXT.__text: 0x7aff00
+  __TEXT.__text: 0x7aff10
   __TEXT.__data_copy: 0x100000
   __TEXT.__const: 0x803ff0
   __TEXT.__cstring: 0x9c1ab

   __TEXT.text_env: 0x507ac
   __TEXT.__ustring: 0xe
   __TEXT.__eh_frame: 0x200
-  __DATA.__const: 0x54958
+  __DATA.__const: 0x548a0
   __DATA._rtk_heap: 0x1000
   __DATA.__data: 0xe0210
   __DATA._rtk_power: 0x3a8

   __DATA._rtk_boot_l1: 0x80
   __DATA.__mod_init_func: 0x20
   __DATA.__zerofill: 0x221e58
-  UUID: 171AF074-70BB-3CF9-804E-44EFA64AC492
+  UUID: 99F07123-FD83-398A-9E71-CF395804DFE1
   Functions: 0
   Symbols:   0
   CStrings:  17213
CStrings:
+ "11:21:41"
+ "Jun 29 2024"
- "08:10:24"
- "May  2 2024"

```

#### agx_a000

>  `agx_a000`

```diff

 
-  __TEXT.__text: 0x58940
-  __TEXT.__gxf_code: 0x108c
+  __TEXT.__text: 0x588c8
+  __TEXT.__gxf_code: 0x1044
   __TEXT.__gxf_code_pad: 0x0
-  __TEXT.__const: 0x1540
+  __TEXT.__const: 0x1510
   __TEXT._rtk_patchbay: 0x1e8
   __TEXT._rtk_tunables: 0x5b0
   __TEXT.__gxf_shr_code: 0x558
-  __TEXT.__cstring: 0x1bce
+  __TEXT.__cstring: 0x1bcb
   __TEXT.__constructor: 0x0
   __TEXT.__chain_starts: 0x0
   __TEXT._rtk_mtab: 0x378

   __DATA.__mod_init_func: 0x0
   __DATA._rtk_heap: 0x0
   __DATA.__zerofill: 0x6b518
-  UUID: DD1D2D72-A0A2-3209-90A5-0ABDBC786E21
+  UUID: 3B2D5F0F-A4E5-347B-A2D0-8283EEAE2D9A
   Functions: 0
   Symbols:   199
   CStrings:  201
CStrings:
+ "GFX %s %s FW %s! (%s)"
+ "Jul  5 2024 18:08:05"
- "GFX %s %u %s FW %s! (%s)"
- "May  2 2024 08:16:18"

```

#### agx_b000

>  `agx_b000`

```diff

 
-  __TEXT.__text: 0x5862c
-  __TEXT.__gxf_code: 0x108c
+  __TEXT.__text: 0x585b4
+  __TEXT.__gxf_code: 0x1044
   __TEXT.__gxf_code_pad: 0x0
-  __TEXT.__const: 0x1580
+  __TEXT.__const: 0x1550
   __TEXT._rtk_patchbay: 0x1e8
   __TEXT._rtk_tunables: 0x5b0
   __TEXT.__gxf_shr_code: 0x558
-  __TEXT.__cstring: 0x1bce
+  __TEXT.__cstring: 0x1bcb
   __TEXT.__constructor: 0x0
   __TEXT.__chain_starts: 0x0
   __TEXT._rtk_mtab: 0x378

   __DATA.__mod_init_func: 0x0
   __DATA._rtk_heap: 0x0
   __DATA.__zerofill: 0x6b398
-  UUID: 56F525B8-9E3B-375B-9E39-497C1C8A693E
+  UUID: 06E47D6D-3583-3917-BC38-556D58ACD9EF
   Functions: 0
   Symbols:   199
   CStrings:  201
CStrings:
+ "GFX %s %s FW %s! (%s)"
+ "Jul  5 2024 18:08:39"
- "GFX %s %u %s FW %s! (%s)"
- "May  2 2024 08:16:49"

```

#### agx_b100

>  `agx_b100`

```diff

 
-  __TEXT.__text: 0x5862c
-  __TEXT.__gxf_code: 0x108c
+  __TEXT.__text: 0x585b4
+  __TEXT.__gxf_code: 0x1044
   __TEXT.__gxf_code_pad: 0x0
-  __TEXT.__const: 0x1580
+  __TEXT.__const: 0x1550
   __TEXT._rtk_patchbay: 0x1e8
   __TEXT._rtk_tunables: 0x5b0
   __TEXT.__gxf_shr_code: 0x558
-  __TEXT.__cstring: 0x1bce
+  __TEXT.__cstring: 0x1bcb
   __TEXT.__constructor: 0x0
   __TEXT.__chain_starts: 0x0
   __TEXT._rtk_mtab: 0x378

   __DATA.__mod_init_func: 0x0
   __DATA._rtk_heap: 0x0
   __DATA.__zerofill: 0x6b398
-  UUID: 8B2E8456-E8A9-36B2-BEEF-19745DF2001E
+  UUID: B0604AD8-2254-3F8E-A5F0-F55AAA5D47F8
   Functions: 0
   Symbols:   199
   CStrings:  201
CStrings:
+ "GFX %s %s FW %s! (%s)"
+ "Jul  5 2024 18:09:14"
- "GFX %s %u %s FW %s! (%s)"
- "May  2 2024 08:17:22"

```

#### ansf.t8130.release.im4p

>  `ansf.t8130.release.im4p`

```diff

 
-  __TEXT.text_first: 0x44a0
-  __TEXT.__text: 0x1727cc
+  __TEXT.text_first: 0x4488
+  __TEXT.__text: 0x17279c
   __TEXT.shared: 0xb7b0
   __TEXT.read: 0x59d0
   __TEXT.__const: 0x8d68
   __TEXT.idle_hooks: 0x10
-  __TEXT.__cstring: 0x1e5b9
+  __TEXT.__cstring: 0x1e5b7
   __TEXT.__chain_starts: 0x0
   __TEXT.__constructor: 0x0
   __TEXT._rtk_mtab: 0x310

   __DATA._rtk_irq_stack: 0x1000
   __DATA._rtk_exc_stack: 0x1000
   __DATA._rtk_page_tables: 0x40000
+  __DATA._rtk_data_uuid: 0x0
   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__mod_init_func: 0x0
CStrings:
+ "373.140.2"
+ "373.140.2~75"
+ "AppleStorageFirmwarePreASP3-373.140.2~75"
+ "Invalid hopIdx %u numProb %u"
+ "Invalid hopIdx:%d or numProb:%d (%llu)"
- "373.120.4"
- "373.120.4~101"
- "AppleStorageFirmwarePreASP3-373.120.4~101"
- "Invalid DM.hopIdx + DM.numProb = %u"
- "Invalid hopIdx:%d or numProb:%d"

```

#### aopfw-iphone16aop.RELEASE.im4p

>  `aopfw-iphone16aop.RELEASE.im4p`

```diff

 
-  __TEXT.__text: 0x145edc
+  __TEXT.__text: 0x145f5c
   __TEXT.__const: 0x11f28
   __TEXT.__cstring: 0x93fc
   __TEXT.__chain_starts: 0x9c

   __DATA._rtk_ext_stack: 0x1800
   __DATA.__const: 0x13dd8
   __DATA.__objc_imageinfo: 0x8
-  __DATA.__data: 0x64a0
+  __DATA.__data: 0x64a8
   __DATA._rtk_patchbay: 0x325
   __DATA._rtk_power: 0x3b8
   __DATA._spu_service: 0xb10

   __DATA._rtk_mtab: 0x788
   __DATA._rtk_tunables: 0x5b0
   __DATA.__version: 0x8
+  __DATA._rtk_data_uuid: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0xdc590
   __ETEXT.__StaticInit: 0x8490
   __ETEXT.__text: 0x1d5dc
   __ETEXT.__const: 0xd9e
-  __OS_LOG.__string: 0x26799
+  __OS_LOG.__string: 0x2679b
   __MISC.__apf_list: 0xb0
   __CMA.__cma_log_string: 0x40da
-  UUID: 4ED68705-3040-3F6E-A2E4-03EA52E4D370
-  Functions: 4232
+  UUID: B9074EF7-7A8A-32F7-92CE-9F8665F0A8F0
+  Functions: 4238
   Symbols:   0
   CStrings:  3622
 
CStrings:
+ "21G65"
+ "23:14:26"
+ "23:55:57"
+ "AppleSPUFirmware-1834.120.13~274"
+ "Jun 28 2024"
+ "RTKitAudioFramework v346.3.1 (built %s %s) ready!! {%zu nodes}"
+ "SensingAlgsProx-43~882"
- "20:44:55"
- "20:51:37"
- "21F62"
- "AppleSPUFirmware-1834.120.11~548"
- "Apr 17 2024"
- "RTKitAudioFramework v346.3 (built %s %s) ready!! {%zu nodes}"
- "SensingAlgsProx-43~870"

```

#### h16x_ane_fw_iaso_d8x.im4p

>  `h16x_ane_fw_iaso_d8x.im4p`

```diff

 
-  __TEXT.__text: 0xa53f8
+  __TEXT.__text: 0xa5408
   __TEXT.__data_copy: 0x8000
   __TEXT.__const: 0x8388
   __TEXT.__cstring: 0x19533

   __DATA.__mod_init_func: 0x0
   __DATA.__noinit: 0x0
   __DATA.__zerofill: 0x53f28
-  UUID: CD1C874A-0207-3067-A1E2-5490EADB647F
+  UUID: 4F9D8932-9EB7-3E3C-8B39-B1BF182817A7
   Functions: 0
   Symbols:   0
   CStrings:  3186
CStrings:
+ "00:59:35"
+ "Jun 29 2024"
- "08:09:53"
- "May  2 2024"

```

#### rans.t8130.release.im4p

>  `rans.t8130.release.im4p`

```diff

 
-  __TEXT.text_first: 0x44a0
-  __TEXT.__text: 0x1727cc
+  __TEXT.text_first: 0x4488
+  __TEXT.__text: 0x17279c
   __TEXT.shared: 0xb7b0
   __TEXT.read: 0x59d0
   __TEXT.__const: 0x8d68
   __TEXT.idle_hooks: 0x10
-  __TEXT.__cstring: 0x1e5b9
+  __TEXT.__cstring: 0x1e5b7
   __TEXT.__chain_starts: 0x0
   __TEXT.__constructor: 0x0
   __TEXT._rtk_mtab: 0x310

   __DATA._rtk_irq_stack: 0x1000
   __DATA._rtk_exc_stack: 0x1000
   __DATA._rtk_page_tables: 0x40000
+  __DATA._rtk_data_uuid: 0x0
   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__mod_init_func: 0x0
CStrings:
+ "373.140.2"
+ "373.140.2~75"
+ "AppleStorageFirmwarePreASP3-373.140.2~75"
+ "Invalid hopIdx %u numProb %u"
+ "Invalid hopIdx:%d or numProb:%d (%llu)"
- "373.120.4"
- "373.120.4~101"
- "AppleStorageFirmwarePreASP3-373.120.4~101"
- "Invalid DM.hopIdx + DM.numProb = %u"
- "Invalid hopIdx:%d or numProb:%d"

```

#### sptm.t8122.release.im4p

>  `sptm.t8122.release.im4p`

```diff

-194.122.2.0.0
-  __TEXT.__cstring: 0xa28d
+194.140.9.0.1
+  __TEXT.__cstring: 0xa3a9
   __TEXT.__binname: 0x40
   __TEXT.__chain_starts: 0x1c
   __TEXT.__const: 0x4b8
-  __DATA_CONST.__const: 0x4c638
-  __TEXT_EXEC.__text: 0x31c40
+  __DATA_CONST.__const: 0x4c640
+  __TEXT_EXEC.__text: 0x31fb8
   __LAST.__pinst: 0x8
   __DATA.__data: 0x16
   __DATA.__common: 0x7150
   __DATA.__bss: 0x4e70
   __BOOTDATA.__data: 0x14000
-  UUID: 2DE6E74C-560C-33DD-8FF0-D679795C3FD3
-  Functions: 235
+  UUID: D4932C0F-35CD-334B-9F92-3023E2480652
+  Functions: 236
   Symbols:   1
-  CStrings:  1293
+  CStrings:  1304
 
CStrings:
+ "&nvme_instance->func_state[5]"
+ "&nvme_instance->func_state[6]"
+ "&nvme_instance->func_state[7]"
+ "&nvme_instance->func_state[8]"
+ "FUNC_BUSY"
+ "FUNC_CALLABLE"
+ "VIOLATION_NVME_ILLEGAL_FUNC_CALL_STATE"
+ "sptm_nvme_bar_admin_queue_regs"
+ "sptm_nvme_bar_iocq_reg"
+ "sptm_nvme_bar_ioqa_reg"
+ "sptm_nvme_bar_iosq_reg"
+ "xnu ro pagetable page #%d is not SPTM owned, but %x"
- "xnu ro pagetable page #%d is not XNU owned, but %x"

```

#### t8130dcp.im4p

>  `t8130dcp.im4p`

```diff

 
-  __TEXT.__text: 0x2b3084
-  __TEXT.__const: 0x7b21c
-  __TEXT.__cstring: 0x2d989
+  __TEXT.__text: 0x2b3bb0
+  __TEXT.__const: 0x7b230
+  __TEXT.__cstring: 0x2daac
   __TEXT.__chain_starts: 0x160
   __DATA.__constructor: 0x8
-  __DATA.__const: 0x47b08
+  __DATA.__const: 0x47b48
   __DATA._rtk_patchbay: 0x710
-  __DATA.__data: 0x2bac0
+  __DATA._rtk_data_uuid: 0x40
+  __DATA.__data: 0x2bad0
   __DATA._rtk_boot: 0x6000
   __DATA._rtk_page_tables: 0xc0000
   __DATA._rtk_power: 0x3b8

   __DATA._afk_sys_objt: 0xb60
   __DATA._rtk_mtab: 0x5b0
   __DATA.__zerofill: 0x9c868
-  __OS_LOG.__string: 0x1ed47
-  UUID: A6B13FFD-1613-3C8D-A3C9-222A5E57854A
-  Functions: 6434
+  __OS_LOG.__string: 0x1ed6e
+  UUID: A1B10300-5E37-3409-A23D-B728795E466C
+  Functions: 6443
   Symbols:   0
-  CStrings:  5771
+  CStrings:  5777
 
CStrings:
+ "ASSERT!%s:%d set TCON_2DIRA_ENABLE_KEY violation"
+ "Enable_backlight_gated enable %d skip backlight dark_boot %d is_dark_boot %d aot %d\n"
+ "IOMFB: %s Enabling failed \n"
+ "IOMFB: %s Enabling! \n"
+ "IOMFB: attempt to use invalid PBT type %d\n"
+ "set_mode_shutdown_gated return HPD is %d link_status is %d that->is_AppleTV() is %d\n"
+ "tcon-2dira-enable"
- "IOMFB: attempt to use invalid PBT type"

```

#### t8130dcp_restore.im4p

>  `t8130dcp_restore.im4p`

```diff

 
-  __TEXT.__text: 0x2b3084
-  __TEXT.__const: 0x7b21c
-  __TEXT.__cstring: 0x2d989
+  __TEXT.__text: 0x2b3bb0
+  __TEXT.__const: 0x7b230
+  __TEXT.__cstring: 0x2daac
   __TEXT.__chain_starts: 0x160
   __DATA.__constructor: 0x8
-  __DATA.__const: 0x47b08
+  __DATA.__const: 0x47b48
   __DATA._rtk_patchbay: 0x710
-  __DATA.__data: 0x2bac0
+  __DATA._rtk_data_uuid: 0x40
+  __DATA.__data: 0x2bad0
   __DATA._rtk_boot: 0x6000
   __DATA._rtk_page_tables: 0xc0000
   __DATA._rtk_power: 0x3b8

   __DATA._afk_sys_objt: 0xb60
   __DATA._rtk_mtab: 0x5b0
   __DATA.__zerofill: 0x9c868
-  __OS_LOG.__string: 0x1ed47
-  UUID: 9BB1907C-38D4-30CF-991A-80F4FC44EC21
-  Functions: 6434
+  __OS_LOG.__string: 0x1ed6e
+  UUID: 0F8B3870-0627-35DE-8301-0E07D85085A0
+  Functions: 6443
   Symbols:   0
-  CStrings:  5771
+  CStrings:  5777
 
CStrings:
+ "ASSERT!%s:%d set TCON_2DIRA_ENABLE_KEY violation"
+ "Enable_backlight_gated enable %d skip backlight dark_boot %d is_dark_boot %d aot %d\n"
+ "IOMFB: %s Enabling failed \n"
+ "IOMFB: %s Enabling! \n"
+ "IOMFB: attempt to use invalid PBT type %d\n"
+ "set_mode_shutdown_gated return HPD is %d link_status is %d that->is_AppleTV() is %d\n"
+ "tcon-2dira-enable"
- "IOMFB: attempt to use invalid PBT type"

```

#### t8130pmp.im4p

>  `t8130pmp.im4p`

```diff

   __DATA._rtk_patchbay: 0x29c
   __DATA._rtk_tunables: 0x5b0
   __DATA._rtk_power: 0x358
+  __DATA._rtk_data_uuid: 0x0
   __DATA._rtk_heap: 0x0
   __DATA.__mod_init_func: 0x10
   __DATA.__zerofill: 0x4d0f0
-  UUID: 11AF5FCD-25AD-3BFD-9AAE-144A31C4153C
+  UUID: 735874E5-7E59-38B6-A88B-5CC47018687C
   Functions: 0
   Symbols:   0
   CStrings:  396

```

#### txm.iphoneos.release.im4p

>  `txm.iphoneos.release.im4p`

```diff

   __DATA.__data: 0x238
   __DATA.__common: 0xa60
   __DATA.__bss: 0x488
-  UUID: B43BB37F-51D6-3242-9FD6-C1DE32BCC4B8
+  UUID: FA924A54-3F38-3E38-9FFC-B8EB6FCC9F34
   Functions: 824
   Symbols:   1
   CStrings:  559
CStrings:
+ "257.140.2"
+ "@(#)VERSION:Darwin Image4 Validator Version 6.3.0: Fri Jun 28 22:43:37 PDT 2024; root:AppleImage4_txm-257.140.2~44/libimage4_TXM/RELEASE_ARM64E"
+ "Darwin Image4 Validator Version 6.3.0: Fri Jun 28 22:43:37 PDT 2024; root:AppleImage4_txm-257.140.2~44/libimage4_TXM/RELEASE_ARM64E"
- "257.120.3"
- "@(#)VERSION:Darwin Image4 Validator Version 6.3.0: Sat Apr 13 03:55:12 PDT 2024; root:AppleImage4_txm-257.120.3~18/libimage4_TXM/RELEASE_ARM64E"
- "Darwin Image4 Validator Version 6.3.0: Sat Apr 13 03:55:12 PDT 2024; root:AppleImage4_txm-257.120.3~18/libimage4_TXM/RELEASE_ARM64E"

```


</details>

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 17.5.1 *(21F90)* | 618.2.12.10.9 |
| 17.6 *(21G80)* | 618.3.11.10.5 |

### Dylibs

#### 🆕 NEW (1)

- `/System/Library/PrivateFrameworks/CallHistoryToolKit.framework/CallHistoryToolKit`

#### ⬆️ Updated (3429)

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
- [/System/Library/AccessibilityBundles/HomeControlService.axbundle/HomeControlService](DYLIBS/HomeControlService.md)
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
- [/System/Library/Frameworks/AdAttributionKit.framework/AdAttributionKit](DYLIBS/AdAttributionKit.md)
- [/System/Library/Frameworks/AdServices.framework/AdServices](DYLIBS/AdServices.md)
- [/System/Library/Frameworks/AdSupport.framework/AdSupport](DYLIBS/AdSupport.md)
- [/System/Library/Frameworks/AddressBook.framework/AddressBook](DYLIBS/AddressBook.md)
- [/System/Library/Frameworks/AddressBookUI.framework/AddressBookUI](DYLIBS/AddressBookUI.md)
- [/System/Library/Frameworks/AppClip.framework/AppClip](DYLIBS/AppClip.md)
- [/System/Library/Frameworks/AppIntents.framework/AppIntents](DYLIBS/AppIntents.md)
- [/System/Library/Frameworks/AppTrackingTransparency.framework/AppTrackingTransparency](DYLIBS/AppTrackingTransparency.md)
- [/System/Library/Frameworks/AssetsLibrary.framework/AssetsLibrary](DYLIBS/AssetsLibrary.md)
- [/System/Library/Frameworks/Assignables.framework/Assignables](DYLIBS/Assignables.md)
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
- [/System/Library/Frameworks/BrowserEngineCore.framework/BrowserEngineCore](DYLIBS/BrowserEngineCore.md)
- [/System/Library/Frameworks/BrowserEngineKit.framework/BrowserEngineKit](DYLIBS/BrowserEngineKit.md)
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
- [/System/Library/Frameworks/LightweightCodeRequirements.framework/LightweightCodeRequirements](DYLIBS/LightweightCodeRequirements.md)
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
- [/System/Library/Frameworks/ManagedSettingsUI.framework/ManagedSettingsUI](DYLIBS/ManagedSettingsUI.md)
- [/System/Library/Frameworks/MapKit.framework/MapKit](DYLIBS/MapKit.md)
- [/System/Library/Frameworks/MarketplaceKit.framework/MarketplaceKit](DYLIBS/MarketplaceKit.md)
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
- [/System/Library/Frameworks/Translation.framework/Translation](DYLIBS/Translation.md)
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
- [/System/Library/Frameworks/_AdAttributionKit_StoreKit.framework/_AdAttributionKit_StoreKit](DYLIBS/_AdAttributionKit_StoreKit.md)
- [/System/Library/Frameworks/_AppIntents_SwiftUI.framework/_AppIntents_SwiftUI](DYLIBS/_AppIntents_SwiftUI.md)
- [/System/Library/Frameworks/_AppIntents_UIKit.framework/_AppIntents_UIKit](DYLIBS/_AppIntents_UIKit.md)
- [/System/Library/Frameworks/_AuthenticationServices_SwiftUI.framework/_AuthenticationServices_SwiftUI](DYLIBS/_AuthenticationServices_SwiftUI.md)
- [/System/Library/Frameworks/_CoreData_CloudKit.framework/_CoreData_CloudKit](DYLIBS/_CoreData_CloudKit.md)
- [/System/Library/Frameworks/_CoreLocationUI_SwiftUI.framework/_CoreLocationUI_SwiftUI](DYLIBS/_CoreLocationUI_SwiftUI.md)
- [/System/Library/Frameworks/_CoreNFC_UIKit.framework/_CoreNFC_UIKit](DYLIBS/_CoreNFC_UIKit.md)
- [/System/Library/Frameworks/_DeviceActivity_SwiftUI.framework/_DeviceActivity_SwiftUI](DYLIBS/_DeviceActivity_SwiftUI.md)
- [/System/Library/Frameworks/_GroupActivities_UIKit.framework/_GroupActivities_UIKit](DYLIBS/_GroupActivities_UIKit.md)
- [/System/Library/Frameworks/_HomeKit_SwiftUI.framework/_HomeKit_SwiftUI](DYLIBS/_HomeKit_SwiftUI.md)
- [/System/Library/Frameworks/_ManagedAppDistribution_SwiftUI.framework/_ManagedAppDistribution_SwiftUI](DYLIBS/_ManagedAppDistribution_SwiftUI.md)
- [/System/Library/Frameworks/_MapKit_SwiftUI.framework/_MapKit_SwiftUI](DYLIBS/_MapKit_SwiftUI.md)
- [/System/Library/Frameworks/_MarketplaceKit_UIKit.framework/_MarketplaceKit_UIKit](DYLIBS/_MarketplaceKit_UIKit.md)
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
- [/System/Library/Frameworks/_Translation_SwiftUI.framework/_Translation_SwiftUI](DYLIBS/_Translation_SwiftUI.md)
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
- [/System/Library/NanoTimeKit/FaceBundles/NTKRhizomeFaceBundleCompanion.bundle/NTKRhizomeFaceBundleCompanion](DYLIBS/NTKRhizomeFaceBundleCompanion.md)
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
- [/System/Library/PrivateFrameworks/ASRBridge.framework/ASRBridge](DYLIBS/ASRBridge.md)
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
- [/System/Library/PrivateFrameworks/AppDistribution.framework/AppDistribution](DYLIBS/AppDistribution.md)
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
- [/System/Library/PrivateFrameworks/AppStoreEvalLighthouseUtils.framework/AppStoreEvalLighthouseUtils](DYLIBS/AppStoreEvalLighthouseUtils.md)
- [/System/Library/PrivateFrameworks/AppStoreFoundation.framework/AppStoreFoundation](DYLIBS/AppStoreFoundation.md)
- [/System/Library/PrivateFrameworks/AppStoreKit.framework/AppStoreKit](DYLIBS/AppStoreKit.md)
- [/System/Library/PrivateFrameworks/AppStoreKitInternal.framework/AppStoreKitInternal](DYLIBS/AppStoreKitInternal.md)
- [/System/Library/PrivateFrameworks/AppStoreOverlays.framework/AppStoreOverlays](DYLIBS/AppStoreOverlays.md)
- [/System/Library/PrivateFrameworks/AppStoreUI.framework/AppStoreUI](DYLIBS/AppStoreUI.md)
- [/System/Library/PrivateFrameworks/AppStoreUtilities.framework/AppStoreUtilities](DYLIBS/AppStoreUtilities.md)
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
- [/System/Library/PrivateFrameworks/AppleEmbeddedDisplayServices.framework/AppleEmbeddedDisplayServices](DYLIBS/AppleEmbeddedDisplayServices.md)
- [/System/Library/PrivateFrameworks/AppleFSCompression.framework/AppleFSCompression](DYLIBS/AppleFSCompression.md)
- [/System/Library/PrivateFrameworks/AppleFirmwareUpdate.framework/AppleFirmwareUpdate](DYLIBS/AppleFirmwareUpdate.md)
- [/System/Library/PrivateFrameworks/AppleFlatBuffers.framework/AppleFlatBuffers](DYLIBS/AppleFlatBuffers.md)
- [/System/Library/PrivateFrameworks/AppleHIDFeedback.framework/AppleHIDFeedback](DYLIBS/AppleHIDFeedback.md)
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
- [/System/Library/PrivateFrameworks/AppleMediaServicesKitSupport.framework/AppleMediaServicesKitSupport](DYLIBS/AppleMediaServicesKitSupport.md)
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
- [/System/Library/PrivateFrameworks/ArgumentParserInternal.framework/ArgumentParserInternal](DYLIBS/ArgumentParserInternal.md)
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
- [/System/Library/PrivateFrameworks/AudioDSPManager.framework/AudioDSPManager](DYLIBS/AudioDSPManager.md)
- [/System/Library/PrivateFrameworks/AudioDataAnalysis.framework/AudioDataAnalysis](DYLIBS/AudioDataAnalysis.md)
- [/System/Library/PrivateFrameworks/AudioPasscode.framework/AudioPasscode](DYLIBS/AudioPasscode.md)
- [/System/Library/PrivateFrameworks/AudioServerApplication.framework/AudioServerApplication](DYLIBS/AudioServerApplication.md)
- [/System/Library/PrivateFrameworks/AudioServerDriver.framework/AudioServerDriver](DYLIBS/AudioServerDriver.md)
- [/System/Library/PrivateFrameworks/AudioServerDriverTransports_Base.framework/AudioServerDriverTransports_Base](DYLIBS/AudioServerDriverTransports_Base.md)
- [/System/Library/PrivateFrameworks/AudioServerDriverTransports_IOA2.framework/AudioServerDriverTransports_IOA2](DYLIBS/AudioServerDriverTransports_IOA2.md)
- [/System/Library/PrivateFrameworks/AudioServerDriverTransports_IOP.framework/AudioServerDriverTransports_IOP](DYLIBS/AudioServerDriverTransports_IOP.md)
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
- [/System/Library/PrivateFrameworks/BusinessFoundation.framework/BusinessFoundation](DYLIBS/BusinessFoundation.md)
- [/System/Library/PrivateFrameworks/BusinessServices.framework/BusinessServices](DYLIBS/BusinessServices.md)
- [/System/Library/PrivateFrameworks/BusinessServicesUI.framework/BusinessServicesUI](DYLIBS/BusinessServicesUI.md)
- [/System/Library/PrivateFrameworks/ButtonResolver.framework/ButtonResolver](DYLIBS/ButtonResolver.md)
- [/System/Library/PrivateFrameworks/C2.framework/C2](DYLIBS/C2.md)
- [/System/Library/PrivateFrameworks/CAFCombine.framework/CAFCombine](DYLIBS/CAFCombine.md)
- [/System/Library/PrivateFrameworks/CAFUI.framework/CAFUI](DYLIBS/CAFUI.md)
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
- [/System/Library/PrivateFrameworks/CameraColorProcessing.framework/CameraColorProcessing](DYLIBS/CameraColorProcessing.md)
- [/System/Library/PrivateFrameworks/CameraEditKit.framework/CameraEditKit](DYLIBS/CameraEditKit.md)
- [/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit](DYLIBS/CameraEffectsKit.md)
- [/System/Library/PrivateFrameworks/CameraImagingFramework.framework/CameraImagingFramework](DYLIBS/CameraImagingFramework.md)
- [/System/Library/PrivateFrameworks/CameraKit.framework/CameraKit](DYLIBS/CameraKit.md)
- [/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI](DYLIBS/CameraUI.md)
- [/System/Library/PrivateFrameworks/CaptiveNetwork.framework/CaptiveNetwork](DYLIBS/CaptiveNetwork.md)
- [/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework](DYLIBS/CarAccessoryFramework.md)
- [/System/Library/PrivateFrameworks/CarAssetUtils.framework/CarAssetUtils](DYLIBS/CarAssetUtils.md)
- [/System/Library/PrivateFrameworks/CarCommandsUIFramework.framework/CarCommandsUIFramework](DYLIBS/CarCommandsUIFramework.md)
- [/System/Library/PrivateFrameworks/CarKit.framework/CarKit](DYLIBS/CarKit.md)
- [/System/Library/PrivateFrameworks/CarKitNavigation.framework/CarKitNavigation](DYLIBS/CarKitNavigation.md)
- [/System/Library/PrivateFrameworks/CarPlayAssetUI.framework/CarPlayAssetUI](DYLIBS/CarPlayAssetUI.md)
- [/System/Library/PrivateFrameworks/CarPlayServices.framework/CarPlayServices](DYLIBS/CarPlayServices.md)
- [/System/Library/PrivateFrameworks/CarPlaySetup.framework/CarPlaySetup](DYLIBS/CarPlaySetup.md)
- [/System/Library/PrivateFrameworks/CarPlaySupport.framework/CarPlaySupport](DYLIBS/CarPlaySupport.md)
- [/System/Library/PrivateFrameworks/CarPlayUI.framework/CarPlayUI](DYLIBS/CarPlayUI.md)
- [/System/Library/PrivateFrameworks/CarPlayUIServices.framework/CarPlayUIServices](DYLIBS/CarPlayUIServices.md)
- [/System/Library/PrivateFrameworks/CardKit.framework/CardKit](DYLIBS/CardKit.md)
- [/System/Library/PrivateFrameworks/CardServices.framework/CardServices](DYLIBS/CardServices.md)
- [/System/Library/PrivateFrameworks/Cards.framework/Cards](DYLIBS/Cards.md)
- [/System/Library/PrivateFrameworks/CarouselPreferenceServices.framework/CarouselPreferenceServices](DYLIBS/CarouselPreferenceServices.md)
- [/System/Library/PrivateFrameworks/CascadeEngine.framework/CascadeEngine](DYLIBS/CascadeEngine.md)
- [/System/Library/PrivateFrameworks/CascadeSets.framework/CascadeSets](DYLIBS/CascadeSets.md)
- [/System/Library/PrivateFrameworks/Catalyst.framework/Catalyst](DYLIBS/Catalyst.md)
- [/System/Library/PrivateFrameworks/Categories.framework/Categories](DYLIBS/Categories.md)
- [/System/Library/PrivateFrameworks/Celestial.framework/Celestial](DYLIBS/Celestial.md)
- [/System/Library/PrivateFrameworks/CellularBridgeUI.framework/CellularBridgeUI](DYLIBS/CellularBridgeUI.md)
- [/System/Library/PrivateFrameworks/CellularDataDiagnosticsSuite.framework/CellularDataDiagnosticsSuite](DYLIBS/CellularDataDiagnosticsSuite.md)
- [/System/Library/PrivateFrameworks/CellularPlanManager.framework/CellularPlanManager](DYLIBS/CellularPlanManager.md)
- [/System/Library/PrivateFrameworks/CertInfo.framework/CertInfo](DYLIBS/CertInfo.md)
- [/System/Library/PrivateFrameworks/CertUI.framework/CertUI](DYLIBS/CertUI.md)
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
- [/System/Library/PrivateFrameworks/ConstantClasses.framework/ConstantClasses](DYLIBS/ConstantClasses.md)
- [/System/Library/PrivateFrameworks/ContactProvider.framework/ContactProvider](DYLIBS/ContactProvider.md)
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
- [/System/Library/PrivateFrameworks/CoreSpeechExclave.framework/CoreSpeechExclave](DYLIBS/CoreSpeechExclave.md)
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
- [/System/Library/PrivateFrameworks/Cosmo.framework/Cosmo](DYLIBS/Cosmo.md)
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
- [/System/Library/PrivateFrameworks/Dendrite.framework/Dendrite](DYLIBS/Dendrite.md)
- [/System/Library/PrivateFrameworks/DendriteIngest.framework/DendriteIngest](DYLIBS/DendriteIngest.md)
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
- [/System/Library/PrivateFrameworks/EDPSecurity.framework/EDPSecurity](DYLIBS/EDPSecurity.md)
- [/System/Library/PrivateFrameworks/EXDisplayPipe.framework/EXDisplayPipe](DYLIBS/EXDisplayPipe.md)
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
- [/System/Library/PrivateFrameworks/FindMyUnsafeAsyncBridging.framework/FindMyUnsafeAsyncBridging](DYLIBS/FindMyUnsafeAsyncBridging.md)
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
- [/System/Library/PrivateFrameworks/GeoShifter.framework/GeoShifter](DYLIBS/GeoShifter.md)
- [/System/Library/PrivateFrameworks/GeoUIFramework.framework/GeoUIFramework](DYLIBS/GeoUIFramework.md)
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
- [/System/Library/PrivateFrameworks/MediaControl.framework/MediaControl](DYLIBS/MediaControl.md)
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
- [/System/Library/PrivateFrameworks/MobileIdentityServiceUI.framework/MobileIdentityServiceUI](DYLIBS/MobileIdentityServiceUI.md)
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
- [/System/Library/PrivateFrameworks/MusicKitPlaybackSupport.framework/MusicKitPlaybackSupport](DYLIBS/MusicKitPlaybackSupport.md)
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
- [/System/Library/PrivateFrameworks/NearFieldPrivateServices.framework/NearFieldPrivateServices](DYLIBS/NearFieldPrivateServices.md)
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
- [/System/Library/PrivateFrameworks/PassKitCore_SoftLinking.framework/PassKitCore_SoftLinking](DYLIBS/PassKitCore_SoftLinking.md)
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
- [/System/Library/PrivateFrameworks/PoirotBlocks.framework/PoirotBlocks](DYLIBS/PoirotBlocks.md)
- [/System/Library/PrivateFrameworks/PoirotSQLite.framework/PoirotSQLite](DYLIBS/PoirotSQLite.md)
- [/System/Library/PrivateFrameworks/PoirotSchematizer.framework/PoirotSchematizer](DYLIBS/PoirotSchematizer.md)
- [/System/Library/PrivateFrameworks/PoirotUDFs.framework/PoirotUDFs](DYLIBS/PoirotUDFs.md)
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
- [/System/Library/PrivateFrameworks/PreviewsFoundationOS.framework/PreviewsFoundationOS](DYLIBS/PreviewsFoundationOS.md)
- [/System/Library/PrivateFrameworks/PreviewsInjection.framework/PreviewsInjection](DYLIBS/PreviewsInjection.md)
- [/System/Library/PrivateFrameworks/PreviewsMessagingOS.framework/PreviewsMessagingOS](DYLIBS/PreviewsMessagingOS.md)
- [/System/Library/PrivateFrameworks/PreviewsOSSupport.framework/PreviewsOSSupport](DYLIBS/PreviewsOSSupport.md)
- [/System/Library/PrivateFrameworks/PreviewsOSSupportUI.framework/PreviewsOSSupportUI](DYLIBS/PreviewsOSSupportUI.md)
- [/System/Library/PrivateFrameworks/PreviewsServices.framework/PreviewsServices](DYLIBS/PreviewsServices.md)
- [/System/Library/PrivateFrameworks/PreviewsServicesUI.framework/PreviewsServicesUI](DYLIBS/PreviewsServicesUI.md)
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
- [/System/Library/PrivateFrameworks/Recount.framework/Recount](DYLIBS/Recount.md)
- [/System/Library/PrivateFrameworks/ReflectionInternal.framework/ReflectionInternal](DYLIBS/ReflectionInternal.md)
- [/System/Library/PrivateFrameworks/RegulatoryDomain.framework/RegulatoryDomain](DYLIBS/RegulatoryDomain.md)
- [/System/Library/PrivateFrameworks/RelativeMotion.framework/RelativeMotion](DYLIBS/RelativeMotion.md)
- [/System/Library/PrivateFrameworks/RelevanceEngine.framework/RelevanceEngine](DYLIBS/RelevanceEngine.md)
- [/System/Library/PrivateFrameworks/RelevanceEngineUI.framework/RelevanceEngineUI](DYLIBS/RelevanceEngineUI.md)
- [/System/Library/PrivateFrameworks/ReminderKit.framework/ReminderKit](DYLIBS/ReminderKit.md)
- [/System/Library/PrivateFrameworks/ReminderKitInternal.framework/ReminderKitInternal](DYLIBS/ReminderKitInternal.md)
- [/System/Library/PrivateFrameworks/ReminderKitUI.framework/ReminderKitUI](DYLIBS/ReminderKitUI.md)
- [/System/Library/PrivateFrameworks/RemindersIntentsFramework.framework/RemindersIntentsFramework](DYLIBS/RemindersIntentsFramework.md)
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
- [/System/Library/PrivateFrameworks/SILManager.framework/SILManager](DYLIBS/SILManager.md)
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
- [/System/Library/PrivateFrameworks/Scandium.framework/Scandium](DYLIBS/Scandium.md)
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
- [/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets.framework/SecureVoiceTriggerAssets](DYLIBS/SecureVoiceTriggerAssets.md)
- [/System/Library/PrivateFrameworks/SecurityFoundation.framework/SecurityFoundation](DYLIBS/SecurityFoundation.md)
- [/System/Library/PrivateFrameworks/Seeding.framework/Seeding](DYLIBS/Seeding.md)
- [/System/Library/PrivateFrameworks/SemanticPerception.framework/SemanticPerception](DYLIBS/SemanticPerception.md)
- [/System/Library/PrivateFrameworks/SensingAlgsService.framework/SensingAlgsService](DYLIBS/SensingAlgsService.md)
- [/System/Library/PrivateFrameworks/SensitiveContentAnalysisML.framework/SensitiveContentAnalysisML](DYLIBS/SensitiveContentAnalysisML.md)
- [/System/Library/PrivateFrameworks/SensitiveContentAnalysisUI.framework/SensitiveContentAnalysisUI](DYLIBS/SensitiveContentAnalysisUI.md)
- [/System/Library/PrivateFrameworks/SensorKitHelper.framework/SensorKitHelper](DYLIBS/SensorKitHelper.md)
- [/System/Library/PrivateFrameworks/SensorKitSupport.framework/SensorKitSupport](DYLIBS/SensorKitSupport.md)
- [/System/Library/PrivateFrameworks/SensorKitUI.framework/SensorKitUI](DYLIBS/SensorKitUI.md)
- [/System/Library/PrivateFrameworks/SentencePiece.framework/SentencePiece](DYLIBS/SentencePiece.md)
- [/System/Library/PrivateFrameworks/Sentry.framework/Sentry](DYLIBS/Sentry.md)
- [/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts](DYLIBS/SeparationAlerts.md)
- [/System/Library/PrivateFrameworks/ServiceExtensions.framework/ServiceExtensions](DYLIBS/ServiceExtensions.md)
- [/System/Library/PrivateFrameworks/ServiceExtensionsCore.framework/ServiceExtensionsCore](DYLIBS/ServiceExtensionsCore.md)
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
- [/System/Library/PrivateFrameworks/SiriCalendarUI.framework/SiriCalendarUI](DYLIBS/SiriCalendarUI.md)
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
- [/System/Library/PrivateFrameworks/SiriEntityMatcher.framework/SiriEntityMatcher](DYLIBS/SiriEntityMatcher.md)
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
- [/System/Library/PrivateFrameworks/SiriMASPFLTraining.framework/SiriMASPFLTraining](DYLIBS/SiriMASPFLTraining.md)
- [/System/Library/PrivateFrameworks/SiriMailInternal.framework/SiriMailInternal](DYLIBS/SiriMailInternal.md)
- [/System/Library/PrivateFrameworks/SiriMailUI.framework/SiriMailUI](DYLIBS/SiriMailUI.md)
- [/System/Library/PrivateFrameworks/SiriMessageBus.framework/SiriMessageBus](DYLIBS/SiriMessageBus.md)
- [/System/Library/PrivateFrameworks/SiriMessageTypes.framework/SiriMessageTypes](DYLIBS/SiriMessageTypes.md)
- [/System/Library/PrivateFrameworks/SiriMessagesCommon.framework/SiriMessagesCommon](DYLIBS/SiriMessagesCommon.md)
- [/System/Library/PrivateFrameworks/SiriMessagesFlow.framework/SiriMessagesFlow](DYLIBS/SiriMessagesFlow.md)
- [/System/Library/PrivateFrameworks/SiriMessagesUI.framework/SiriMessagesUI](DYLIBS/SiriMessagesUI.md)
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
- [/System/Library/PrivateFrameworks/SiriUserSegments.framework/SiriUserSegments](DYLIBS/SiriUserSegments.md)
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
- [/System/Library/PrivateFrameworks/SnippetKit_Proto.framework/SnippetKit_Proto](DYLIBS/SnippetKit_Proto.md)
- [/System/Library/PrivateFrameworks/SnippetUI.framework/SnippetUI](DYLIBS/SnippetUI.md)
- [/System/Library/PrivateFrameworks/SnippetUI_Proto.framework/SnippetUI_Proto](DYLIBS/SnippetUI_Proto.md)
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
- [/System/Library/PrivateFrameworks/SonicFoundation.framework/SonicFoundation](DYLIBS/SonicFoundation.md)
- [/System/Library/PrivateFrameworks/SonicKit.framework/SonicKit](DYLIBS/SonicKit.md)
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
- [/System/Library/PrivateFrameworks/Tabi.framework/Tabi](DYLIBS/Tabi.md)
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
- [/System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam](DYLIBS/Tightbeam.md)
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
- [/System/Library/PrivateFrameworks/VDAF.framework/VDAF](DYLIBS/VDAF.md)
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
- [/System/Library/PrivateFrameworks/_SonicKit_MusicKit.framework/_SonicKit_MusicKit](DYLIBS/_SonicKit_MusicKit.md)
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
- [/System/Library/PrivateFrameworks/libmalloc_exclaves_introspector.framework/libmalloc_exclaves_introspector](DYLIBS/libmalloc_exclaves_introspector.md)
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
- [/usr/lib/libimage4.dylib](DYLIBS/libimage4.dylib.md)
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
- [/usr/lib/system/libsystem_symptoms.dylib](DYLIBS/libsystem_symptoms.dylib.md)
- [/usr/lib/system/libsystem_trace.dylib](DYLIBS/libsystem_trace.dylib.md)
- [/usr/lib/system/libunwind.dylib](DYLIBS/libunwind.dylib.md)
- [/usr/lib/system/libxpc.dylib](DYLIBS/libxpc.dylib.md)
- [/usr/lib/updaters/libAce3Updater.dylib](DYLIBS/libAce3Updater.dylib.md)
- [/usr/lib/updaters/libAppleTCONUpdater.dylib](DYLIBS/libAppleTCONUpdater.dylib.md)
- [/usr/lib/updaters/libAppleTconUARPUpdater.dylib](DYLIBS/libAppleTconUARPUpdater.dylib.md)
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

- `Firmware/Mav23-1.70.02.Release.bbfw`
- `Firmware/Mav23-1.70.02.Release.plist`

#### filesystem (691)

<details>
  <summary><i>View Files</i></summary>

- `/Applications/FindMyRemoteUIService.app/Assets.car`
- `/Applications/FindMyRemoteUIService.app/Localizable.loctable`
- `/Applications/Print Center.app/Localizable.loctable`
- `/System/Library/Assistant/FlowDelegatePlugins/GeoFlowDelegatePlugin.bundle/Templates/dialog/LocationServices.catfamily/PreciseLocationDisabled.cat/en-in.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/Templates/dialog/PhoneCallDisplayText.catfamily/CancelButtonText.cat/de-ch.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/Templates/dialog/PhoneCallDisplayText.catfamily/CancelButtonText.cat/fr-be.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/Templates/dialog/PhoneCallDisplayText.catfamily/CancelButtonText.cat/fr-ca.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/Templates/dialog/PhoneCallDisplayText.catfamily/CancelButtonText.cat/fr-ch.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/ar/dialog/SocialConversation.catfamily/dalRollADie.cat/_params.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/ar/dialog/SocialConversation.catfamily/dalRollADie.cat/ar.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/ar/pattern/SocialConversation.patternfamily/dalCanYouSpeakHindi.patternxml`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/da/pattern/SocialConversation.patternfamily/dalCanYouSpeakHindi.patternxml`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/de/dialog/SocialConversation.catfamily/dalFeelingSoothe.cat/de-at.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/de/dialog/SocialConversation.catfamily/dalFeelingUplift.cat/de-at.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/de/dialog/SocialConversation.catfamily/dalFeelingUplift.cat/de-ch.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/de/pattern/SocialConversation.patternfamily/dalCanYouSpeakHindi.patternxml`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/en/dialog/SocialConversation.catfamily/dalFeelingUplift.cat/en-ie.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/en/dialog/SocialConversation.catfamily/dalFeelingUplift.cat/en-sg.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/en/dialog/SocialConversation.catfamily/dalRollADie.cat/en-au.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/en/dialog/SocialConversation.catfamily/dalRollADie.cat/en-ca.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/en/dialog/SocialConversation.catfamily/dalRollADie.cat/en-gb.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/en/dialog/SocialConversation.catfamily/dalRollADie.cat/en-za.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/es/dialog/SocialConversation.catfamily/dalCountingOnYou.cat/es-mx.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/es/dialog/SocialConversation.catfamily/dalKnockKnockJoke_exit.cat/_params.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/es/dialog/SocialConversation.catfamily/dalKnockKnockJoke_exit.cat/es.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/es/dialog/SocialConversation.catfamily/dalKnockKnockJoke_replayFallback.cat/_params.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/es/dialog/SocialConversation.catfamily/dalKnockKnockJoke_replayFallback.cat/es.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/es/dialog/SocialConversation.catfamily/dalKnockKnockJoke_startPrompt.cat/_params.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/es/dialog/SocialConversation.catfamily/dalKnockKnockJoke_startPrompt.cat/es.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/es/dialog/SocialConversation.catfamily/dalPrepareForEid.cat/es-mx.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/es/dialog/SocialConversation.catfamily/dalWhyDontYouEatDrinkSleepRest.cat/es-mx.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/es/pattern/SocialConversation.patternfamily/dalCanYouSpeakHindi.patternxml`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/fi/pattern/SocialConversation.patternfamily/dalCanYouSpeakHindi.patternxml`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/fr/pattern/SocialConversation.patternfamily/dalCanYouSpeakHindi.patternxml`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/he/pattern/SocialConversation.patternfamily/dalCanYouSpeakHindi.patternxml`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/hi/pattern/SocialConversation.patternfamily/dalCanYouSpeakHindi.patternxml`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/it/pattern/SocialConversation.patternfamily/dalCanYouSpeakHindi.patternxml`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/ja/dialog/SocialConversation.catfamily/dalBlondLadyUrbanLegend.cat/_params.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/ja/dialog/SocialConversation.catfamily/dalBlondLadyUrbanLegend.cat/ja.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/ja/dialog/SocialConversation.catfamily/dalKnockKnockJoke_exit.cat/_params.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/ja/dialog/SocialConversation.catfamily/dalKnockKnockJoke_exit.cat/ja.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/ja/dialog/SocialConversation.catfamily/dalKnockKnockJoke_replayFallback.cat/_params.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/ja/dialog/SocialConversation.catfamily/dalKnockKnockJoke_replayFallback.cat/ja.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/ja/dialog/SocialConversation.catfamily/dalKnockKnockJoke_startPrompt.cat/_params.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/ja/dialog/SocialConversation.catfamily/dalKnockKnockJoke_startPrompt.cat/ja.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/ja/pattern/SocialConversation.patternfamily/dalCanYouSpeakHindi.patternxml`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/ko/dialog/SocialConversation.catfamily/dalRollADie.cat/_params.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/ko/dialog/SocialConversation.catfamily/dalRollADie.cat/ko.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/ko/pattern/SocialConversation.patternfamily/dalCanYouSpeakHindi.patternxml`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/ms/dialog/SocialConversation.catfamily/dailyUplift.cat/_params.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/ms/dialog/SocialConversation.catfamily/dailyUplift.cat/ms.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/ms/pattern/SocialConversation.patternfamily/dalCanYouSpeakHindi.patternxml`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/nb/pattern/SocialConversation.patternfamily/dalCanYouSpeakHindi.patternxml`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/nl/dialog/SocialConversation.catfamily/dalBlondLadyUrbanLegend.cat/_params.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/nl/dialog/SocialConversation.catfamily/dalBlondLadyUrbanLegend.cat/nl.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/nl/dialog/SocialConversation.catfamily/dalKnockKnockJoke_exit.cat/_params.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/nl/dialog/SocialConversation.catfamily/dalKnockKnockJoke_exit.cat/nl-be.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/nl/dialog/SocialConversation.catfamily/dalKnockKnockJoke_exit.cat/nl.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/nl/dialog/SocialConversation.catfamily/dalKnockKnockJoke_replayFallback.cat/_params.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/nl/dialog/SocialConversation.catfamily/dalKnockKnockJoke_replayFallback.cat/nl-be.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/nl/dialog/SocialConversation.catfamily/dalKnockKnockJoke_replayFallback.cat/nl.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/nl/dialog/SocialConversation.catfamily/dalKnockKnockJoke_startPrompt.cat/_params.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/nl/dialog/SocialConversation.catfamily/dalKnockKnockJoke_startPrompt.cat/nl-be.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/nl/dialog/SocialConversation.catfamily/dalKnockKnockJoke_startPrompt.cat/nl.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/nl/pattern/SocialConversation.patternfamily/dalCanYouSpeakHindi.patternxml`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/pt/pattern/SocialConversation.patternfamily/dalCanYouSpeakHindi.patternxml`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/ru/dialog/SocialConversation.catfamily/dalBlondLadyUrbanLegend.cat/_params.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/ru/dialog/SocialConversation.catfamily/dalBlondLadyUrbanLegend.cat/ru.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/ru/dialog/SocialConversation.catfamily/dalKnockKnockJoke_jokes.cat/_params.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/ru/dialog/SocialConversation.catfamily/dalKnockKnockJoke_jokes.cat/ru.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/ru/pattern/SocialConversation.patternfamily/dalCanYouSpeakHindi.patternxml`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/sv/dialog/SocialConversation.catfamily/dalKnockKnockJoke_jokes.cat/_params.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/sv/dialog/SocialConversation.catfamily/dalKnockKnockJoke_jokes.cat/sv.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/sv/pattern/SocialConversation.patternfamily/dalCanYouSpeakHindi.patternxml`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/th/dialog/SocialConversation.catfamily/dalRollADie.cat/_params.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/th/dialog/SocialConversation.catfamily/dalRollADie.cat/th.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/th/dialog/SocialConversation.catfamily/shouldIVote.cat/_params.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/th/dialog/SocialConversation.catfamily/shouldIVote.cat/th.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/th/pattern/SocialConversation.patternfamily/dalCanYouSpeakHindi.patternxml`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/tr/dialog/SocialConversation.catfamily/dalRollADie.cat/_params.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/tr/dialog/SocialConversation.catfamily/dalRollADie.cat/tr.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/tr/pattern/SocialConversation.patternfamily/dalCanYouSpeakHindi.patternxml`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/yue/pattern/SocialConversation.patternfamily/dalCanYouSpeakHindi.patternxml`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/zh/pattern/SocialConversation.patternfamily/dalCanYouSpeakHindi.patternxml`
- `/System/Library/CoreServices/IOUIAngel.app/InfoPlist.loctable`
- `/System/Library/CoreServices/IOUIAngel.app/Localizable.loctable`
- `/System/Library/LifecyclePolicy/DomainAttributes/com.apple.photosretailexperience.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.appstoreutilities.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-Custom.bundle/Info.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-Custom.bundle/Personalities/8BitDo/M30/Bluetooth.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-Custom.bundle/Personalities/8BitDo/M30/USB.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-Custom.bundle/Personalities/8BitDo/Micro/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-Custom.bundle/Personalities/8BitDo/NEOGEOGP/Bluetooth.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-Custom.bundle/Personalities/8BitDo/NEOGEOGP/USB.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-Custom.bundle/Personalities/8BitDo/Pro2/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-Custom.bundle/Personalities/8BitDo/Pro2/WithBackButtons.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-Custom.bundle/Personalities/8BitDo/SN30_Pro/v11720_p8449_r256.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-Custom.bundle/Personalities/Backbone/backboneone/MFi.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-Custom.bundle/Personalities/Backbone/backboneone/MFi_Playstation_Named.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-Custom.bundle/Personalities/Backbone/backboneone/MFi_Playstation_USB.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-Custom.bundle/Personalities/Backbone/backboneone/MFi_Playstation_USB_Named.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-Custom.bundle/Personalities/Backbone/backboneone/MFi_USB.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-Custom.bundle/Personalities/Flydigi/Vader2Pro/MobileBluetooth.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-Custom.bundle/Personalities/Flydigi/Vader2Pro/MobileBluetoothWithBackButtons.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-Custom.bundle/Personalities/Flydigi/Vader2Pro/MobileUSB.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-Custom.bundle/Personalities/Flydigi/Vader2Pro/MobileUSBWithBackButtons.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-Custom.bundle/Personalities/GameSir/X3/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-Custom.bundle/Personalities/HORI/PlayStation5FightingStickAlpha/PS4Mode.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-Custom.bundle/Personalities/HORI/PlayStation5FightingStickAlpha/PS5Mode.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-Custom.bundle/Personalities/MadCatz/EGOArcadeStick/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-Custom.bundle/Personalities/Mayflash/ArcadeStick/GameConsoleMode.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-Custom.bundle/Personalities/Mayflash/ArcadeStickF101/DInputMode.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-Custom.bundle/Personalities/Mayflash/ArcadeStickF300/DInputMode.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-Custom.bundle/Personalities/Mayflash/ArcadeStickF300Elite/DInputMode.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-Custom.bundle/Personalities/Mayflash/ArcadeStickF500v2/DInputMode.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-Custom.bundle/Personalities/PowerA/moga/Bluetooth.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-Custom.bundle/Personalities/PowerA/moga/USB.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-Custom.bundle/Personalities/Razer/KishiV2/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-Custom.bundle/Personalities/Razer/WolverineV2Pro/Wired.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-Custom.bundle/Personalities/Razer/WolverineV2Pro/Wireless.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-Custom.bundle/Personalities/RotorRiot/RR1800A/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-Custom.bundle/Personalities/Tech4Home/TIMOK/BluetoothLE.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-Custom.bundle/_CodeSignature/CodeDirectory`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-Custom.bundle/_CodeSignature/CodeRequirements`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-Custom.bundle/_CodeSignature/CodeRequirements-1`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-Custom.bundle/_CodeSignature/CodeResources`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-Custom.bundle/_CodeSignature/CodeSignature`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Info.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v10007/p12612/r297/XiaoMi_Game_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v10256/p9/8Bitdo_SFC30_GamePad_Joystick/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1064/p16385/r512/Gravis_Gamepad_Pro/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1103/p45824/Thrustmaster_Firestorm_Dual_Power/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1103/p45845/Thrustmaster_Dual_Analog_3_2/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1103/p53262/r512/ThrustMaster_eSwap_PRO_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1118/p39/r257/Microsoft_SideWinder_Plug_and_Play/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1133/p49686/Logitech_F310_Gamepad_(DInput)/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1133/p49686/r1044/Logitech_Dual_Action/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1133/p49686/r512/Logitech_Dual_Action/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1133/p49686/r768/Logitech_Dual_Action/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1133/p49688/Logitech_F510_Gamepad_(DInput)/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1133/p49688/r256/Logitech_RumblePad_2_USB/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1133/p49689/Logitech_Wireless_Gamepad_(DInput)/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1133/p49689/r773/Logitech_F710_Gamepad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1133/p49695/Logitech_F710_Gamepad_(XInput)/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1149/p16389/r257/Gravis_Eliminator_GamePad_Pro/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p10272/r256/8BitDo_NES30/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p10304/r256/8Bitdo_SN30_GamePad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p10341/r256/8BitDo_N30_Pro_2/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p12306/r256/8BitDo_Ultimate_Wireless_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p12306/r512/8BitDo_Ultimate_Wireless_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p12544/r1/8BitDo_Wireless_Adapter/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p12848/r256/8BitDo_Zero_2/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p14352/r256/8BitDo_FC30_Pro/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p20753/r256/8BitDo_Lite_SE/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p20753/r512/8BitDo_Lite_SE/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p20754/r256/8BitDo_Lite_2/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p20754/r512/8BitDo_Lite_2/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p24577/r1/8BitDo_SN30_Pro/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p24578/r1/8BitDo_SN30_Pro+/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p24833/r256/8BitDo_SN30_Pro/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p24834/r256/8BitDo_SN30_Pro+/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p36864/r1/8BitDo_FC30_Pro/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p36865/r1/8Bitdo_NES30_Pro/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p36882/r1/8BitDo_SN30_Gamepad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p36885/r1/8BitDo_N30_Pro_2/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p36888/r1/8BitDo_Zero_2/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p43794/r1/8BitDo_NES30/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1204/p266/Sega_Saturn_USB_Gamepad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1204/p9233/Flydigi_Vader_2/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v12068/p115/r512/Mayflash_Magic_NS/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v12068/p45/r263/JYS_Wireless_Adapter/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v121/p17/Retro_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v121/p17/r261/Retro_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v121/p17/r262/Retrolink_SNES_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v121/p6/r263/Marvo_GT-004/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v121/p6144/Mayflash_WiiU_Pro_Game_Controller_Adapter_(DInput)/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v121/p6144/r256/Mayflash_Wii_U_Pro_Controller_Adapter/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v121/p6212/r256/Mayflash_GameCube_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v121/p6214/r256/GameCube_Controller_Adapter/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v121/p6354/r294/Mayflash_Magic_NS/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1356/p2976/Sony_DualShock_4_Wireless_Adaptor/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1356/p2976/r256/PS4_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1356/p3290/r256/Playstation_Classic_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1356/p4919/r256/PlayStation_Vita/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1356/p616/PS3_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1356/p616/r256/PS3_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1411/p45105/Cideko_AK08b/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1411/p8288/iBuffalo_Gamepad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1411/p8288/r256/Retro_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v14368/p9/r256/8Bitdo_NES30_Pro/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1440/p12850/r264/8Bitdo_Zero_GamePad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1440/p12850/r265/8Bitdo_Zero_GamePad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1519/p3/r512/AxisPad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1699/p63010/r769/Cyborg_V_3_Rumble_Pad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1848/p12880/r256/Mad_Catz_FightPad_PRO_(PS3)/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1848/p13188/r256/Mad_Catz_FightStick_TE_S+_(PS3)/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1848/p33360/r256/Mad_Catz_FightPad_PRO_(PS4)/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1848/p33668/r256/Mad_Catz_FightStick_TE_S+_(PS4)/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1907/p260/r256/Sanwa_PlayOnline_Mobile/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v2064/p1/Twin_USB_Joystick/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v2064/p3/r262/PS2_Adapter/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v2064/p58625/r262/NEXT_SNES_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v2341/p1000/Mayflash_Wii_Classic_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v2342/p34952/r648/Cyber_Gadget_GameCube_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v2389/p29204/r1317/NVIDIA_Controller_v01_04/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v273/p5145/r265/SteelSeries_Stratus_XL/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v2821/p17664/r49/ASUS_Gamepad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v30021/p4386/r256/SZMY_Power_PC_Gamepad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3090/p3600/r256/Zeroplus_P4_Gamepad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3090/p3616/r256/Brook_Mars_PS4_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3090/p3617/r256/Brook_Mars_PS4_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3090/p7696/r256/Zeroplus_P4_Wired_Gamepad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3235/p39/r771/Astro_City_Mini/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3235/p40/r771/Astro_City_Mini/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3695/p1025/Xbox_360_Wired_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3695/p265/r258/PDP_Versus_Fighting_Pad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3695/p513/GameStop_Xbox_360_Wired_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3695/p515/r1061/Victrix_Pro_Fight_Stick_for_PS4/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3695/p519/r1539/Victrix_Pro_Fight_Stick_for_PS4/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3727/p12307/r273/HuiJia_SNES_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3727/p3/Piranha_Xtreme_PS3_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3727/p3/r263/GreenAsia_USB_Joystick/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3727/p3/r265/2In1_USB_Joystick/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p102/Horipad_FPS_Plus_4/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p102/r256/Horipad_4_PS4/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p110/r256/Horipad_4_PS3/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p132/r256/Fighting_Commander/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p133/r256/Fighting_Commander/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p146/r256/Hori_Pokken_Tournament_DX_Pro_Pad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p238/r256/Horipad_Mini_4/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p45/r4096/Hori_Fighting_Commander_3_Pro/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p77/Hori_Gem_Pad_3/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p94/Hori_Fighting_Commander_4_PS4/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p94/r256/Hori_Fighting_Commander_4_PS4/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p95/Hori_Fighting_Commander_4_PS3/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p95/r256/Hori_Fighting_Commander_4_PS3/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v4544/p16385/r256/GameStop_PS4_Fun_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v4661/p43794/r1/8BitDo_NES30_Gamepad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v4661/p43809/SFC30_Joystick/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v4754/p17995/r515/NES_2-port_Adapter/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v4797/p53269/Tomee_SNES_USB_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v4797/p53269/r256/Tomee_Retro_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5227/p3329/r256/Revolution_Pro_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5227/p3347/r256/Revolution_Pro_Controller_3/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5336/p53198/Cthulhu/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5426/p1025/r256/Razer_Panthera_PS4/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5426/p1026/r256/Razer_Panthera_PS3/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5426/p1797/r257/Razer_Raiju_Mobile/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5426/p1799/r256/Razer_Raiju_Mobile/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5426/p2304/r14870/Razer_Serval/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5426/p2304/r512/Razer_Serval/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5426/p2563/Razer_Wildcat/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5426/p4096/r256/Razer_Raiju/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5426/p4103/r257/Razer_Raiju_Tournament_Edition/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5426/p4106/r1/Razer_Raiju_Tournament_Edition/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5426/p4352/r256/Razer_Raion_Fightpad_for_PS4/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5769/p64768/Razer_Onza_TE/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v6017/p1406/Sega_Saturn/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v61440/p241/SNES_RetroPort/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v6353/p37888/r256/Stadia_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v6421/p64/r1/Flydigi_Vader_2/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v6473/p1049/r257/Amazon_Luna_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v7085/p63745/Gamestop_BB070_X360_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v7545/p769/r265/Wii_Classic_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v8194/p36864/r1/8Bitdo_NES30_Pro/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v8406/p25201/r1/Moga_Pro_2_HID/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v8406/p31018/r256/BDA_PS4_Fightpad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v8406/p42768/r259/Mayflash_Magic_NS/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v8406/p42769/r1296/Nintendo_Switch_PowerA_Wired_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v8406/p42769/r512/Nintendo_Switch_Core_Plus_Wired_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v8406/p51821/r256/PowerA_Pro_Ex/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v9414/p21562/Xbox_One_PowerA_Wired_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v9414/p23812/Xbox_360_Wired_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v9414/p35098/r256/BDA_MOGA_XP5-X_Plus/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v9414/p35099/r256/BDA_MOGA_XP5-X_Plus/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v9414/p35114/r256/MOGA_XP5A_Plus/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v9414/p35115/r256/MOGA_XP5A_Plus/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v9414/p64254/Rock_Candy_Gamepad_for_PS3/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/Personalities/v9571/p1397/r512/NEOGEO_mini_PAD_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/_CodeSignature/CodeDirectory`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/_CodeSignature/CodeRequirements`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/_CodeSignature/CodeRequirements-1`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/_CodeSignature/CodeResources`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/AssetData/GameControllers-SDL.bundle/_CodeSignature/CodeSignature`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/Info.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/_CodeSignature/CodeDirectory`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/_CodeSignature/CodeRequirements`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/_CodeSignature/CodeRequirements-1`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/_CodeSignature/CodeResources`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/a83e946f4f00ce96c93ba5cd54b7a3fc0b75dfde.asset/_CodeSignature/CodeSignature`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_VoiceTriggerRePromptListiPhone15x/4265cb638fb9a148cc9c28323ab59c8e4fd1e232.asset/AssetData/devidblobiphone15`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_VoiceTriggerRePromptListiPhone15x/4265cb638fb9a148cc9c28323ab59c8e4fd1e232.asset/AssetData/repromptMetadata.json`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_VoiceTriggerRePromptListiPhone15x/4265cb638fb9a148cc9c28323ab59c8e4fd1e232.asset/Info.plist`
- `/System/Library/PrivateFrameworks/APConfigurationSystem.framework/APCS/Placements/Sponsorship/ConfigurationNode.json`
- `/System/Library/PrivateFrameworks/APFoundation.framework/DatabaseMigrationScritps/APDatabase/5.plist`
- `/System/Library/PrivateFrameworks/AppStoreUtilities.framework/com.apple.appstoreutilities.plist`
- `/System/Library/PrivateFrameworks/CallHistoryToolKit.framework/Info.plist`
- `/System/Library/PrivateFrameworks/CallHistoryToolKit.framework/_CodeSignature/CodeResources`
- `/System/Library/PrivateFrameworks/DisembarkUI.framework/Assets.car`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/TargetConditionals.h`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/metal_array`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/metal_assert`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/metal_atomic`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/metal_command_buffer`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/metal_common`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/metal_compute`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/metal_config`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/metal_curves`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/metal_extended_vector`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/metal_functional`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/metal_geometric`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/metal_graphics`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/metal_imageblocks`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/metal_initializer_list`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/metal_integer`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/metal_interpolate`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/metal_limits`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/metal_math`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/metal_matrix`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/metal_mesh`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/metal_numeric`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/metal_pack`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/metal_packed_vector`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/metal_pixel`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/metal_quadgroup`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/metal_raytracing`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/metal_relational`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/metal_simdgroup`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/metal_simdgroup_matrix`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/metal_stdlib`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/metal_tessellation`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/metal_texture`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/metal_type_traits`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/metal_types`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/metal_types.h`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/metal_uniform`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/metal_utility`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/metal_visible_function_table`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/module.modulemap`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/prebuilt_implicit_modules/1C06DJYNPWKD1/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/prebuilt_implicit_modules/1LWVRH94U711Q/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/prebuilt_implicit_modules/1P94WOU95Z7NI/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/prebuilt_implicit_modules/1X1TJHI7UL5NI/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/prebuilt_implicit_modules/26WIY3JVJVOI0/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/prebuilt_implicit_modules/2HJQ687U5F3T0/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/prebuilt_implicit_modules/2XJZPFC3R4QS4/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/prebuilt_implicit_modules/3LS7EQ48ADVK9/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/prebuilt_implicit_modules/3ULD0G6JJFC0R/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/prebuilt_implicit_modules/IITFUWGC6EPB/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/simd/matrix_types.h`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/simd/packed.h`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/simd/simd.h`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/include/metal/simd/vector_types.h`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/lib/darwin/libair_rt_ios.rtlib`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/lib/darwin/libmetal_rt_ios.a`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/lib/darwin/libpost_mesh_dump_rt_ios.rtlib`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/lib/darwin/libresource_tracking_rt_ios.rtlib`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/lib/darwin/libtracepoint_rt_ios.metallib`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/lib/darwin/libtracepoint_rt_static_ios.a`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.198/lib/darwin/libtracepoint_rt_workaround_ios.a`
- `/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/Templates/dialog/HomeAutomation.catfamily/CalibrationInProgress.cat/en-ie.cat.bin`
- `/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/Templates/dialog/HomeAutomation.catfamily/CalibrationInProgress.cat/en-sg.cat.bin`
- `/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/Templates/dialog/HomeAutomation.catfamily/CalibrationInProgress.cat/fr-ch.cat.bin`
- `/System/Library/PrivateFrameworks/Preferences.framework/ContactlessAndCredentialSettings_Localizable.loctable`
- `/System/Library/PrivateFrameworks/SEService.framework/SESSettings_Localizable.loctable`
- `/System/Library/PrivateFrameworks/SiriFindMy.framework/Templates/schema/findmy.Device.catschema.bin`
- `/System/Library/PrivateFrameworks/SiriFindMy.framework/Templates/schema/findmy.VisualPerson.catschema.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationDoNot.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationDoNot.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationDoNot.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationDoNot.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationDoNot.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationDoNot.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationDoNot.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationDoNot.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationDoNot.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationDoNot.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationDoNot.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationDoNot.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationDoNot.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationDoNot.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationDoNot.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationDoNot.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationDoNot.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationDoNot.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationDoNot.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationDoNot.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationDoNot.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationDoNot.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationDoNot.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationDoNot.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationDoNot.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationDoNot.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationDoNot.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationDoNot.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationDoNot.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationOnce.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationOnce.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationOnce.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationOnce.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationOnce.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationOnce.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationOnce.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationOnce.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationOnce.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationOnce.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationOnce.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationOnce.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationOnce.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationOnce.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationOnce.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationOnce.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationOnce.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationOnce.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationOnce.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationOnce.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationOnce.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationOnce.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationOnce.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationOnce.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationOnce.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationOnce.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationOnce.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationOnce.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationOnce.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationUsingSiri.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationUsingSiri.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationUsingSiri.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationUsingSiri.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationUsingSiri.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationUsingSiri.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationUsingSiri.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationUsingSiri.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationUsingSiri.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationUsingSiri.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationUsingSiri.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationUsingSiri.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationUsingSiri.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationUsingSiri.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationUsingSiri.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationUsingSiri.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationUsingSiri.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationUsingSiri.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationUsingSiri.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationUsingSiri.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationUsingSiri.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationUsingSiri.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationUsingSiri.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationUsingSiri.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationUsingSiri.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationUsingSiri.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationUsingSiri.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationUsingSiri.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/AccessLocationUsingSiri.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/ErrorSiriNeedsLocationAccess.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/ErrorSiriNeedsLocationAccess.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/ErrorSiriNeedsLocationAccess.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/ErrorSiriNeedsLocationAccess.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/ErrorSiriNeedsLocationAccess.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/ErrorSiriNeedsLocationAccess.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/ErrorSiriNeedsLocationAccess.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/ErrorSiriNeedsLocationAccess.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/ErrorSiriNeedsLocationAccess.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/ErrorSiriNeedsLocationAccess.cat/es-us.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/ErrorSiriNeedsLocationAccess.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/ErrorSiriNeedsLocationAccess.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/ErrorSiriNeedsLocationAccess.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/ErrorSiriNeedsLocationAccess.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/ErrorSiriNeedsLocationAccess.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/ErrorSiriNeedsLocationAccess.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/ErrorSiriNeedsLocationAccess.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/ErrorSiriNeedsLocationAccess.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/ErrorSiriNeedsLocationAccess.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/ErrorSiriNeedsLocationAccess.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/ErrorSiriNeedsLocationAccess.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/ErrorSiriNeedsLocationAccess.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/ErrorSiriNeedsLocationAccess.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/ErrorSiriNeedsLocationAccess.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/ErrorSiriNeedsLocationAccess.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/ErrorSiriNeedsLocationAccess.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/ErrorSiriNeedsLocationAccess.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/ErrorSiriNeedsLocationAccess.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/ErrorSiriNeedsLocationAccess.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/ErrorSiriNeedsLocationAccess.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/LocationServicesSettings.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/LocationServicesSettings.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/LocationServicesSettings.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/LocationServicesSettings.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/LocationServicesSettings.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/LocationServicesSettings.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/LocationServicesSettings.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/LocationServicesSettings.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/LocationServicesSettings.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/LocationServicesSettings.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/LocationServicesSettings.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/LocationServicesSettings.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/LocationServicesSettings.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/LocationServicesSettings.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/LocationServicesSettings.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/LocationServicesSettings.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/LocationServicesSettings.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/LocationServicesSettings.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/LocationServicesSettings.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/LocationServicesSettings.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/LocationServicesSettings.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/LocationServicesSettings.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/LocationServicesSettings.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/LocationServicesSettings.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/LocationServicesSettings.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/LocationServicesSettings.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/LocationServicesSettings.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/LocationServicesSettings.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/LocationServicesSettings.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessLocationBySiri.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessLocationBySiri.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessLocationBySiri.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessLocationBySiri.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessLocationBySiri.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessLocationBySiri.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessLocationBySiri.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessLocationBySiri.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessLocationBySiri.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessLocationBySiri.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessLocationBySiri.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessLocationBySiri.cat/fr-ca.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessLocationBySiri.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessLocationBySiri.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessLocationBySiri.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessLocationBySiri.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessLocationBySiri.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessLocationBySiri.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessLocationBySiri.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessLocationBySiri.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessLocationBySiri.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessLocationBySiri.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessLocationBySiri.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessLocationBySiri.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessLocationBySiri.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessLocationBySiri.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessLocationBySiri.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessLocationBySiri.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessLocationBySiri.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessLocationBySiri.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessPreciseLocationBySiriOneTime.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessPreciseLocationBySiriOneTime.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessPreciseLocationBySiriOneTime.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessPreciseLocationBySiriOneTime.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessPreciseLocationBySiriOneTime.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessPreciseLocationBySiriOneTime.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessPreciseLocationBySiriOneTime.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessPreciseLocationBySiriOneTime.cat/en-ie.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessPreciseLocationBySiriOneTime.cat/en-in.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessPreciseLocationBySiriOneTime.cat/en-za.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessPreciseLocationBySiriOneTime.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessPreciseLocationBySiriOneTime.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessPreciseLocationBySiriOneTime.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessPreciseLocationBySiriOneTime.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessPreciseLocationBySiriOneTime.cat/fr-ca.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessPreciseLocationBySiriOneTime.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessPreciseLocationBySiriOneTime.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessPreciseLocationBySiriOneTime.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessPreciseLocationBySiriOneTime.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessPreciseLocationBySiriOneTime.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessPreciseLocationBySiriOneTime.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessPreciseLocationBySiriOneTime.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessPreciseLocationBySiriOneTime.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessPreciseLocationBySiriOneTime.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessPreciseLocationBySiriOneTime.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessPreciseLocationBySiriOneTime.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessPreciseLocationBySiriOneTime.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessPreciseLocationBySiriOneTime.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessPreciseLocationBySiriOneTime.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessPreciseLocationBySiriOneTime.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessPreciseLocationBySiriOneTime.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessPreciseLocationBySiriOneTime.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/CommonTCC.catfamily/PromptToAccessPreciseLocationBySiriOneTime.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/SiriMessagesFlow.framework/Templates/dialog/Labels.catfamily/ButtonSkip.cat/es-cl.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/Resume.cat/fr-ca.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPrivateLearningAnalytics.framework/default_factors_354.pb`
- `/System/Library/PrivateFrameworks/WebContentRestrictions.framework/WCRAppleAllowList-2024-05-15.plist`
- `/System/Library/PrivateFrameworks/WebContentRestrictions.framework/WCRFilter-2024-05-15.plist`
- `/System/Library/Snippets/UIPlugins/SiriKitUIPlugin.bundle/Info.plist`
- `/System/Library/Snippets/UIPlugins/SiriKitUIPlugin.bundle/SiriKitUIPlugin`
- `/System/Library/Snippets/UIPlugins/SiriKitUIPlugin.bundle/_CodeSignature/CodeResources`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/ar_SA.453115ffc2e8350adb43085a7ea41a05.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/da_DK.552772c590f8f1cb8094ef61e1663474.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/de_DE.f96aa0752858426936e3a391113ba608.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/en_AU.a8522fa88110afd32ea4483c77d197ef.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/en_GB.4612c896347f3bb361ed32d3662ed18a.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/en_US.17cd39f47327202a31edc7ea48bd16b8.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/es_ES.f93f24d645adc24978c0443d6fea127e.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/es_MX.81210f9d6c3bed2aaf8709997efcd2f1.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/fi_FI.b2582e50eda91bc0bbfe4f29e64e9bac.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/fr_CA.5757a8e9e05fc15859f490e29d85ec7a.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/fr_FR.bca1086385359c899461586ad3a9df4f.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/he_IL.f6b7066e0a7b366660a7def7c0540f16.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/it_IT.055b434c2b50d0700b517bd193e76ad5.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/ja_JP.86af72e4075222d728a21a4c16d5f72b.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/ko_KR.351356500e6e361567ab04aa2064d13a.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/ms_MY.175d9e008ba8688714cfcc71b54160f4.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/nl_NL.299f69988aae2beb07960be79cc42ccf.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/pt_BR.9937a928db9e80cd3d662194576e9249.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/ru_RU.2fa15b79fab5b80ff3f58b43aa79d370.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/sv_SE.5348539a58c6e89724cbda91084fc986.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/th_TH.4727a3094dfb745a8fe254297edf22bd.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/tr_TR.aa33362dd4d6891c6d2eaf54a9cd2ade.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/zh_CN.fa58b803bb680fdc1745b22011dea079.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/zh_HK.797bbe8e39114e2e052e1d0ce0eebd13.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/zh_TW.a3cf060773809b02b3bd421e88f6f14f.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/ar_SA.efcc107e7ae51e0023e6c5bb0d112e29.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/da_DK.4e092e321f00aba7beb5217e9c03db8d.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/de_DE.024f3da50d0bd346a8b5130fd61fc35b.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/en_AU.eebf8d0dab931863ed16ec364630c6e8.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/en_GB.d8e550d70841377c4b707d935264a654.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/en_IN.a907940751c1febc5854596930e0133b.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/en_US.2b37dde754c2befe13e22a9b019bf451.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/es_ES.8c9152403165fc57cf8d8a315d0b14f6.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/es_MX.dcd58d92a0fa4551d7792d21b59dd328.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/fi_FI.dc5e0e7eee43a3385a002864cdcf5bdb.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/fr_CA.9e6e34def1c4d877b3c1e5a24f96a5b3.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/fr_FR.1b69865235ee98480bc9414fe49c1d1e.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/he_IL.c95669159c9f859d683fd334e815566b.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/it_IT.9bb4940d1798cab4a8e6dc8ab0f3a651.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/ja_JP.62dc0af365781312405bd6cab2ee12bd.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/ko_KR.6fd03e0a339ea2f611cb59f24a0022be.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/ms_MY.e6fa2638b9ecbcf929291a5b27992163.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/nl_NL.9fab942a715b44a16f5f27aaf1f8737d.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/pt_BR.d63021cfa6779e2283491ea0afc23712.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/ru_RU.49c8c6c37f0f2db7070de4fe37e3abd0.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/sv_SE.eae8a729139984178cac58ef2ab6d644.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/th_TH.ee1aa3e2db26c4829c6522ed1dec78e8.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/tr_TR.5e193767561d02be999180d3c8c6f954.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/zh_CN.41282166002dd94bcd73a777875d18f0.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/zh_HK.ce1cc3826c77a6ac977b6ae1bd032b87.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/zh_TW.db64d473defc734dd8620e6a29b6db42.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/ar_SA.962a5da206bc581ba13948af19bd80c3.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/da_DK.7bf35d91e8d67bc6b1363751e808cd98.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/de_DE.031a209fe15db3c5f0ef08be1b55d993.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/en_AU.152796ccaeaa7b64c7b86de6595528fd.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/en_GB.10945e11d1601950b7bd88c35f2e1745.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/en_US.fcb98a2b1e327f1a8a2dd2ace930d16c.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/es_ES.ea935cca1b930155ac84c8ad283d3187.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/es_MX.4b8e98fc90d0e23dc9a2120f840f88c1.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/fi_FI.a4becb5ca7633b5f9593417cad932daf.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/fr_CA.9d075e0b42516c6849b381f08f509d02.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/fr_FR.2f0d748a3c6e7b313b8d53a3292943bb.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/he_IL.f5f3512cbcbee9e5746d1ab21c8495c2.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/it_IT.29fa8aaf2b818794a2e643ee06ee724d.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/ja_JP.afb1b230d14e544db6025f3ce7dc0f25.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/ko_KR.793c4eb8c5a3bc824c6e219960571c79.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/ms_MY.35fbd9d48f6ee92d22416aeb81dd15af.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/nl_NL.88e425d5ebd19dde9e9aaab2c8d140d7.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/pt_BR.a7cf9a4d21822f0033fdfdfc4f27a82b.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/ru_RU.abebdb9e7fc028d7e017e96a4c9f1e87.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/sv_SE.067c831feeefc201d5f09a1aea390f35.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/th_TH.38d4c5fc4c0cc5def8ef144e420fdd1e.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/tr_TR.465e3921d3d5d6851914868e9ee8aa2d.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/zh_CN.1d06017a0d93fb33ab77036cc2c7ff1b.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/zh_HK.c92e76dde0399969f616c9f398f09ea0.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/zh_TW.45258bb45495f83e88be42a2f7a734ba.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/ar_SA.24f011f5818157cba5ac06be5f1b1296.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/da_DK.9bb11471efd0c0372dc453713d999e03.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/de_DE.160f05949c19674c369f0b26135b204c.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/en_AU.1147efd393a49d88654de8ae167affed.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/en_GB.17b34f4729b171978f6b9060211345ee.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/en_US.51f08c7d983bd9a87eba44830ac7c1bd.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/es_ES.142712f1201e85b38fb552f4467070bc.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/es_MX.6d0abfa1c72356c1166756c10a466233.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/fi_FI.f6d7325bcd8a70e4094a21798a1d7876.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/fr_CA.a7fafee0e4f81914af41a62ddd9cb43d.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/fr_FR.d3f8bc68b9b9e06779e6afafad8dd144.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/he_IL.f03eeaf9158b353321c1bb8530f05654.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/it_IT.a9065ad37d4ee6fd3b391a1d9446ab78.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/ja_JP.0225cf2038132656b9091ace9bfd08fb.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/ko_KR.05330311dcab4b54e3be93718edda92a.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/ms_MY.23c4cddc0ebb81a7a135b62806783b0a.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/nl_NL.74781d2ae13ba974a7dbc497f9038813.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/pt_BR.f7ef0f6fea35ad097d4dd7bf94794c3a.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/ru_RU.391c08ec62713c57eea5a0d16a581f65.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/sv_SE.d8428c10bfc7eb54ca75ead55ee5f7a6.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/th_TH.e8f834ec240253d9b1b8729c5ab0fac6.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/tr_TR.e00e3ca1ac6b5fb5f62548eb0dee7b16.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/zh_CN.ca5da671c81e109d94be5096c5139f23.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/zh_HK.07b338de24209d86d0a0ec94853d590a.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/zh_TW.29bebcbe8985e69c33c4fd7036091688.version`
- `/usr/standalone/firmware/nfrestore/firmware/fw/SN100V_FW_A3_01_01_9A_rev150922.bin`
- `/usr/standalone/firmware/nfrestore/firmware/fw/SN200V_FW_B1_02_01_9D_rev150916.bin`
- `/usr/standalone/firmware/nfrestore/firmware/fw/SN300V_FW_B0_02_01_45_rev150912.bin`
- `/usr/standalone/firmware/nfrestore/firmware/rf/SN100V_FW_A3_01_01_9A_rev150922.plist`
- `/usr/standalone/firmware/nfrestore/firmware/rf/SN200V_FW_B1_02_01_9D_rev150916.plist`
- `/usr/standalone/firmware/nfrestore/firmware/rf/SN300V_FW_B0_02_01_45_rev150912.plist`

</details>

### ❌ Removed

#### IPSW (2)

- `Firmware/Mav23-1.60.02.Release.bbfw`
- `Firmware/Mav23-1.60.02.Release.plist`

#### filesystem (419)

<details>
  <summary><i>View Files</i></summary>

- `/Applications/AppStore.app/EventCell.nib`
- `/Applications/AppStore.app/ImpressionTableViewCell.nib`
- `/Applications/AppStore.app/PlugIns/ProductPageExtension.appex/EventCell.nib`
- `/Applications/AppStore.app/PlugIns/ProductPageExtension.appex/ImpressionTableViewCell.nib`
- `/Applications/AppStore.app/PlugIns/ProductPageExtension.appex/Type1Cell.nib`
- `/Applications/AppStore.app/PlugIns/SubscribePageExtension.appex/EventCell.nib`
- `/Applications/AppStore.app/PlugIns/SubscribePageExtension.appex/ImpressionTableViewCell.nib`
- `/Applications/AppStore.app/PlugIns/SubscribePageExtension.appex/Type1Cell.nib`
- `/Applications/AppStore.app/Type1Cell.nib`
- `/Applications/CTKUIService.app/InfoPlist.loctable`
- `/Applications/FindMyRemoteUIService.app/Localizable.strings`
- `/System/Library/Assistant/FlowDelegatePlugins/AlarmFlowPlugin.bundle/Templates/dialog/AlarmBase.catfamily/UnsupportedWithReasonAlarmNotFound.cat/it-ch.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/GeoFlowDelegatePlugin.bundle/Templates/dialog/TrafficIncident.catfamily/AssistantPreciseLocationServicesDisabled.cat/en-in.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/HomeCommunicationFlowDelegatePlugin.bundle/Templates/dialog/SendAnnouncement.catfamily/OpenHomeApp.cat/es-cl.cat.bin`
- `/System/Library/Frameworks/Foundation.framework/Localizable.loctable`
- `/System/Library/Messages/iMessageBalloons/ASMessagesProvider.bundle/EventCell.nib`
- `/System/Library/Messages/iMessageBalloons/ASMessagesProvider.bundle/ImpressionTableViewCell.nib`
- `/System/Library/Messages/iMessageBalloons/ASMessagesProvider.bundle/Type1Cell.nib`
- `/System/Library/PreferenceBundles/AccountSettings/AppleAccountSettings.bundle/accountBeneficiary@2x.png`
- `/System/Library/PreferenceBundles/AccountSettings/AppleAccountSettings.bundle/accountBeneficiary@3x.png`
- `/System/Library/PreferenceBundles/ContactlessAndCredentialSettings.bundle/ContactlessAndCredentialSettings`
- `/System/Library/PreferenceBundles/ContactlessAndCredentialSettings.bundle/ContactlessAndCredentialSettings_Localizable.loctable`
- `/System/Library/PreferenceBundles/ContactlessAndCredentialSettings.bundle/Info.plist`
- `/System/Library/PreferenceBundles/ContactlessAndCredentialSettings.bundle/_CodeSignature/CodeResources`
- `/System/Library/PreferenceManifestsInternal/ContactlessAndCredentialSettingsManifests.bundle/Info.plist`
- `/System/Library/PreferenceManifestsInternal/ContactlessAndCredentialSettingsManifests.bundle/SettingsSearchManifest-ContactlessAndCredential.loctable`
- `/System/Library/PreferenceManifestsInternal/ContactlessAndCredentialSettingsManifests.bundle/SettingsSearchManifest-ContactlessAndCredential.plist`
- `/System/Library/PreferenceManifestsInternal/ContactlessAndCredentialSettingsManifests.bundle/_CodeSignature/CodeDirectory`
- `/System/Library/PreferenceManifestsInternal/ContactlessAndCredentialSettingsManifests.bundle/_CodeSignature/CodeRequirements`
- `/System/Library/PreferenceManifestsInternal/ContactlessAndCredentialSettingsManifests.bundle/_CodeSignature/CodeRequirements-1`
- `/System/Library/PreferenceManifestsInternal/ContactlessAndCredentialSettingsManifests.bundle/_CodeSignature/CodeResources`
- `/System/Library/PreferenceManifestsInternal/ContactlessAndCredentialSettingsManifests.bundle/_CodeSignature/CodeSignature`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-Custom.bundle/Info.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-Custom.bundle/Personalities/8BitDo/M30/Bluetooth.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-Custom.bundle/Personalities/8BitDo/M30/USB.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-Custom.bundle/Personalities/8BitDo/Micro/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-Custom.bundle/Personalities/8BitDo/NEOGEOGP/Bluetooth.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-Custom.bundle/Personalities/8BitDo/NEOGEOGP/USB.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-Custom.bundle/Personalities/8BitDo/Pro2/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-Custom.bundle/Personalities/8BitDo/Pro2/WithBackButtons.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-Custom.bundle/Personalities/8BitDo/SN30_Pro/v11720_p8449_r256.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-Custom.bundle/Personalities/Backbone/backboneone/MFi.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-Custom.bundle/Personalities/Backbone/backboneone/MFi_Playstation.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-Custom.bundle/Personalities/Backbone/backboneone/MFi_USB_Playstation.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-Custom.bundle/Personalities/Flydigi/Vader2Pro/MobileBluetooth.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-Custom.bundle/Personalities/Flydigi/Vader2Pro/MobileBluetoothWithBackButtons.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-Custom.bundle/Personalities/Flydigi/Vader2Pro/MobileUSB.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-Custom.bundle/Personalities/Flydigi/Vader2Pro/MobileUSBWithBackButtons.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-Custom.bundle/Personalities/GameSir/X3/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-Custom.bundle/Personalities/HORI/PlayStation5FightingStickAlpha/PS4Mode.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-Custom.bundle/Personalities/HORI/PlayStation5FightingStickAlpha/PS5Mode.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-Custom.bundle/Personalities/MadCatz/EGOArcadeStick/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-Custom.bundle/Personalities/Mayflash/ArcadeStick/GameConsoleMode.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-Custom.bundle/Personalities/Mayflash/ArcadeStickF101/DInputMode.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-Custom.bundle/Personalities/Mayflash/ArcadeStickF300/DInputMode.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-Custom.bundle/Personalities/Mayflash/ArcadeStickF300Elite/DInputMode.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-Custom.bundle/Personalities/Mayflash/ArcadeStickF500v2/DInputMode.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-Custom.bundle/Personalities/PowerA/moga/Bluetooth.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-Custom.bundle/Personalities/PowerA/moga/USB.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-Custom.bundle/Personalities/Razer/KishiV2/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-Custom.bundle/Personalities/Razer/WolverineV2Pro/Wired.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-Custom.bundle/Personalities/Razer/WolverineV2Pro/Wireless.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-Custom.bundle/Personalities/RotorRiot/RR1800A/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-Custom.bundle/Personalities/Tech4Home/TIMOK/BluetoothLE.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-Custom.bundle/_CodeSignature/CodeDirectory`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-Custom.bundle/_CodeSignature/CodeRequirements`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-Custom.bundle/_CodeSignature/CodeRequirements-1`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-Custom.bundle/_CodeSignature/CodeResources`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-Custom.bundle/_CodeSignature/CodeSignature`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Info.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v10007/p12612/r297/XiaoMi_Game_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v10256/p9/8Bitdo_SFC30_GamePad_Joystick/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1064/p16385/r512/Gravis_Gamepad_Pro/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1103/p45824/Thrustmaster_Firestorm_Dual_Power/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1103/p45845/Thrustmaster_Dual_Analog_3_2/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1103/p53262/r512/ThrustMaster_eSwap_PRO_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1118/p39/r257/Microsoft_SideWinder_Plug_and_Play/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1133/p49686/Logitech_F310_Gamepad_(DInput)/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1133/p49686/r1044/Logitech_Dual_Action/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1133/p49686/r512/Logitech_Dual_Action/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1133/p49686/r768/Logitech_Dual_Action/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1133/p49688/Logitech_F510_Gamepad_(DInput)/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1133/p49688/r256/Logitech_RumblePad_2_USB/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1133/p49689/Logitech_Wireless_Gamepad_(DInput)/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1133/p49689/r773/Logitech_F710_Gamepad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1133/p49695/Logitech_F710_Gamepad_(XInput)/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1149/p16389/r257/Gravis_Eliminator_GamePad_Pro/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p10272/r256/8BitDo_NES30/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p10304/r256/8Bitdo_SN30_GamePad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p10341/r256/8BitDo_N30_Pro_2/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p12306/r256/8BitDo_Ultimate_Wireless_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p12306/r512/8BitDo_Ultimate_Wireless_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p12544/r1/8BitDo_Wireless_Adapter/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p12848/r256/8BitDo_Zero_2/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p14352/r256/8BitDo_FC30_Pro/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p20753/r256/8BitDo_Lite_SE/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p20753/r512/8BitDo_Lite_SE/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p20754/r256/8BitDo_Lite_2/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p20754/r512/8BitDo_Lite_2/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p24577/r1/8BitDo_SN30_Pro/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p24578/r1/8BitDo_SN30_Pro+/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p24833/r256/8BitDo_SN30_Pro/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p24834/r256/8BitDo_SN30_Pro+/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p36864/r1/8BitDo_FC30_Pro/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p36865/r1/8Bitdo_NES30_Pro/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p36882/r1/8BitDo_SN30_Gamepad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p36885/r1/8BitDo_N30_Pro_2/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p36888/r1/8BitDo_Zero_2/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v11720/p43794/r1/8BitDo_NES30/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1204/p266/Sega_Saturn_USB_Gamepad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1204/p9233/Flydigi_Vader_2/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v12068/p115/r512/Mayflash_Magic_NS/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v12068/p45/r263/JYS_Wireless_Adapter/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v121/p17/Retro_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v121/p17/r261/Retro_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v121/p17/r262/Retrolink_SNES_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v121/p6/r263/Marvo_GT-004/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v121/p6144/Mayflash_WiiU_Pro_Game_Controller_Adapter_(DInput)/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v121/p6144/r256/Mayflash_Wii_U_Pro_Controller_Adapter/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v121/p6212/r256/Mayflash_GameCube_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v121/p6214/r256/GameCube_Controller_Adapter/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v121/p6354/r294/Mayflash_Magic_NS/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1356/p2976/Sony_DualShock_4_Wireless_Adaptor/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1356/p2976/r256/PS4_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1356/p3290/r256/Playstation_Classic_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1356/p4919/r256/PlayStation_Vita/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1356/p616/PS3_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1356/p616/r256/PS3_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1411/p45105/Cideko_AK08b/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1411/p8288/iBuffalo_Gamepad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1411/p8288/r256/Retro_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v14368/p9/r256/8Bitdo_NES30_Pro/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1440/p12850/r264/8Bitdo_Zero_GamePad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1440/p12850/r265/8Bitdo_Zero_GamePad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1519/p3/r512/AxisPad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1699/p63010/r769/Cyborg_V_3_Rumble_Pad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1848/p12880/r256/Mad_Catz_FightPad_PRO_(PS3)/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1848/p13188/r256/Mad_Catz_FightStick_TE_S+_(PS3)/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1848/p33360/r256/Mad_Catz_FightPad_PRO_(PS4)/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1848/p33668/r256/Mad_Catz_FightStick_TE_S+_(PS4)/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v1907/p260/r256/Sanwa_PlayOnline_Mobile/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v2064/p1/Twin_USB_Joystick/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v2064/p3/r262/PS2_Adapter/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v2064/p58625/r262/NEXT_SNES_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v2341/p1000/Mayflash_Wii_Classic_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v2342/p34952/r648/Cyber_Gadget_GameCube_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v2389/p29204/r1317/NVIDIA_Controller_v01_04/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v273/p5145/r265/SteelSeries_Stratus_XL/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v2821/p17664/r49/ASUS_Gamepad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v30021/p4386/r256/SZMY_Power_PC_Gamepad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3090/p3600/r256/Zeroplus_P4_Gamepad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3090/p3616/r256/Brook_Mars_PS4_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3090/p3617/r256/Brook_Mars_PS4_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3090/p7696/r256/Zeroplus_P4_Wired_Gamepad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3235/p39/r771/Astro_City_Mini/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3235/p40/r771/Astro_City_Mini/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3695/p1025/Xbox_360_Wired_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3695/p265/r258/PDP_Versus_Fighting_Pad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3695/p513/GameStop_Xbox_360_Wired_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3695/p515/r1061/Victrix_Pro_Fight_Stick_for_PS4/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3695/p519/r1539/Victrix_Pro_Fight_Stick_for_PS4/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3727/p12307/r273/HuiJia_SNES_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3727/p3/Piranha_Xtreme_PS3_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3727/p3/r263/GreenAsia_USB_Joystick/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3727/p3/r265/2In1_USB_Joystick/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p102/Horipad_FPS_Plus_4/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p102/r256/Horipad_4_PS4/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p110/r256/Horipad_4_PS3/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p132/r256/Fighting_Commander/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p133/r256/Fighting_Commander/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p146/r256/Hori_Pokken_Tournament_DX_Pro_Pad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p238/r256/Horipad_Mini_4/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p45/r4096/Hori_Fighting_Commander_3_Pro/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p77/Hori_Gem_Pad_3/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p94/Hori_Fighting_Commander_4_PS4/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p94/r256/Hori_Fighting_Commander_4_PS4/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p95/Hori_Fighting_Commander_4_PS3/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v3853/p95/r256/Hori_Fighting_Commander_4_PS3/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v4544/p16385/r256/GameStop_PS4_Fun_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v4661/p43794/r1/8BitDo_NES30_Gamepad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v4661/p43809/SFC30_Joystick/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v4754/p17995/r515/NES_2-port_Adapter/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v4797/p53269/Tomee_SNES_USB_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v4797/p53269/r256/Tomee_Retro_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5227/p3329/r256/Revolution_Pro_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5227/p3347/r256/Revolution_Pro_Controller_3/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5336/p53198/Cthulhu/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5426/p1025/r256/Razer_Panthera_PS4/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5426/p1026/r256/Razer_Panthera_PS3/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5426/p1797/r257/Razer_Raiju_Mobile/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5426/p1799/r256/Razer_Raiju_Mobile/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5426/p2304/r14870/Razer_Serval/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5426/p2304/r512/Razer_Serval/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5426/p2563/Razer_Wildcat/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5426/p4096/r256/Razer_Raiju/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5426/p4103/r257/Razer_Raiju_Tournament_Edition/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5426/p4106/r1/Razer_Raiju_Tournament_Edition/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5426/p4352/r256/Razer_Raion_Fightpad_for_PS4/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v5769/p64768/Razer_Onza_TE/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v6017/p1406/Sega_Saturn/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v61440/p241/SNES_RetroPort/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v6353/p37888/r256/Stadia_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v6421/p64/r1/Flydigi_Vader_2/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v6473/p1049/r257/Amazon_Luna_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v7085/p63745/Gamestop_BB070_X360_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v7545/p769/r265/Wii_Classic_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v8194/p36864/r1/8Bitdo_NES30_Pro/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v8406/p25201/r1/Moga_Pro_2_HID/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v8406/p31018/r256/BDA_PS4_Fightpad/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v8406/p42768/r259/Mayflash_Magic_NS/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v8406/p42769/r1296/Nintendo_Switch_PowerA_Wired_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v8406/p42769/r512/Nintendo_Switch_Core_Plus_Wired_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v8406/p51821/r256/PowerA_Pro_Ex/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v9414/p21562/Xbox_One_PowerA_Wired_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v9414/p23812/Xbox_360_Wired_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v9414/p35098/r256/BDA_MOGA_XP5-X_Plus/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v9414/p35099/r256/BDA_MOGA_XP5-X_Plus/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v9414/p35114/r256/MOGA_XP5A_Plus/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v9414/p35115/r256/MOGA_XP5A_Plus/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v9414/p64254/Rock_Candy_Gamepad_for_PS3/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/Personalities/v9571/p1397/r512/NEOGEO_mini_PAD_Controller/Default.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/_CodeSignature/CodeDirectory`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/_CodeSignature/CodeRequirements`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/_CodeSignature/CodeRequirements-1`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/_CodeSignature/CodeResources`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/AssetData/GameControllers-SDL.bundle/_CodeSignature/CodeSignature`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/Info.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/_CodeSignature/CodeDirectory`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/_CodeSignature/CodeRequirements`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/_CodeSignature/CodeRequirements-1`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/_CodeSignature/CodeResources`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_GameController_DB1/ebad5315d3bf69bf6fa10ff131a28cbf6db704fd.asset/_CodeSignature/CodeSignature`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_VoiceTriggerRePromptListiPhone15x/74152a20d9ecb8d8ff1084e1f699382320e19967.asset/AssetData/devidblobiphone15`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_VoiceTriggerRePromptListiPhone15x/74152a20d9ecb8d8ff1084e1f699382320e19967.asset/AssetData/repromptMetadata.json`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_VoiceTriggerRePromptListiPhone15x/74152a20d9ecb8d8ff1084e1f699382320e19967.asset/Info.plist`
- `/System/Library/PrivateFrameworks/AOPVoiceTriggerSecure.framework/Modules/AOPVoiceTriggerSecure.tightbeam/AOPVoiceTriggerSecure.tbmodule`
- `/System/Library/PrivateFrameworks/CoreSpeechExclave.framework/Modules/CoreSpeechExclave.tightbeam/CoreSpeechExclave.tbmodule`
- `/System/Library/PrivateFrameworks/ExclavesAudioDrivers.framework/Modules/ExclavesAudioDrivers.tightbeam/ExclavesAudioDrivers.tbmodule`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/TargetConditionals.h`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/metal_array`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/metal_assert`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/metal_atomic`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/metal_command_buffer`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/metal_common`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/metal_compute`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/metal_config`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/metal_curves`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/metal_extended_vector`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/metal_functional`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/metal_geometric`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/metal_graphics`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/metal_imageblocks`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/metal_initializer_list`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/metal_integer`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/metal_interpolate`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/metal_limits`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/metal_math`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/metal_matrix`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/metal_mesh`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/metal_numeric`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/metal_pack`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/metal_packed_vector`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/metal_pixel`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/metal_quadgroup`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/metal_raytracing`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/metal_relational`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/metal_simdgroup`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/metal_simdgroup_matrix`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/metal_stdlib`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/metal_tessellation`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/metal_texture`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/metal_type_traits`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/metal_types`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/metal_types.h`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/metal_uniform`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/metal_utility`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/metal_visible_function_table`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/module.modulemap`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/prebuilt_implicit_modules/1A1ZT1OBPGITO/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/prebuilt_implicit_modules/1AM3QLKQ47QWE/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/prebuilt_implicit_modules/1T2UVFWFA6T7G/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/prebuilt_implicit_modules/1WUMIMNT7CDH1/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/prebuilt_implicit_modules/22G7RR2FSSUNQ/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/prebuilt_implicit_modules/2I0QHFVLX0KT1/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/prebuilt_implicit_modules/34GSD8YUYTVFE/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/prebuilt_implicit_modules/351AT2YCSMGOI/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/prebuilt_implicit_modules/8IV1FTCDRTKW/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/prebuilt_implicit_modules/ASOI91UHSX8G/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/simd/matrix_types.h`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/simd/packed.h`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/simd/simd.h`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/include/metal/simd/vector_types.h`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/lib/darwin/libair_rt_ios.rtlib`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/lib/darwin/libmetal_rt_ios.a`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/lib/darwin/libpost_mesh_dump_rt_ios.rtlib`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/lib/darwin/libresource_tracking_rt_ios.rtlib`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/lib/darwin/libtracepoint_rt_ios.metallib`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/lib/darwin/libtracepoint_rt_static_ios.a`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.194/lib/darwin/libtracepoint_rt_workaround_ios.a`
- `/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/Templates/dialog/HomeAutomation.catfamily/RequestSent.cat/en-za.cat.bin`
- `/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/Templates/dialog/HomeAutomation.catfamily/RequestSent.cat/es-cl.cat.bin`
- `/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/Templates/dialog/HomeAutomation.catfamily/RequestSent.cat/nl-be.cat.bin`
- `/System/Library/PrivateFrameworks/IsolatedCoreAudioClient.framework/Modules/IsolatedCoreAudioClient.tightbeam/IsolatedCoreAudioClient.tbmodule`
- `/System/Library/PrivateFrameworks/LPMicDeviceAOP.framework/Modules/LPMicDeviceAOP.tightbeam/LPMicDeviceAOP.tbmodule`
- `/System/Library/PrivateFrameworks/SiriFindMy.framework/Templates/schema/findmy.Device.catschema`
- `/System/Library/PrivateFrameworks/SiriFindMy.framework/Templates/schema/findmy.VisualPerson.catschema`
- `/System/Library/PrivateFrameworks/SiriNotificationsIntents.framework/Templates/dialog/ReadNotifications.catfamily/ReadLongHint.cat/es-cl.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/Paused.cat/en-za.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/Resume.cat/en-za.cat.bin`
- `/System/Library/PrivateFrameworks/VoiceTriggerAOP.framework/Modules/VoiceTriggerAOP.tightbeam/VoiceTriggerAOP.tbmodule`
- `/System/Library/PrivateFrameworks/WebContentRestrictions.framework/WCRAppleAllowList-2024-02-13.plist`
- `/System/Library/PrivateFrameworks/WebContentRestrictions.framework/WCRFilter-2024-02-13.plist`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/ar_SA.b8e006d30f90319da1a0b331b6584b15.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/da_DK.b93ba30de1ff04d4badf35c6ac0996af.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/de_DE.4f85bdb32ee6070a3c9cd51e0ff89a1f.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/en_AU.2a326c475bfe8546fc680fede7a6a99c.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/en_GB.0f2d2950ba4ea5d576146da342023ce5.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/en_US.74d6622f39214a9e36a12777aaa22acb.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/es_ES.01337e108abd4ac9954ade5adc1fc827.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/es_MX.feca46a53495f9c8407fd097f2d12328.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/fi_FI.3ee5eb0bfe734a9834cf230a48e6765b.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/fr_CA.e1f693c1e1d94e2a5c098207374f855e.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/fr_FR.25ca4c1563a37375ce0df289da5dc9a6.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/he_IL.d0e4f776af87097c6116cfebd1b62859.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/it_IT.db7c926dfb2408e051d1d2b7d940aa98.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/ja_JP.39bdb6f8e94d8a4b8eb1fb7a309a150b.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/ko_KR.f7d2a38cea73096acb9615b7fb58b4f5.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/ms_MY.478766435e6a26fffd20e057ebd1fb94.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/nl_NL.04f6033076442bf7d82da79f86586146.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/pt_BR.ee90987e6b1469a914c9a79e4908aa3c.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/ru_RU.85c185f40e948228137f296aa2104cc2.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/sv_SE.9ebd56b996320984af68f6b9ad5d8715.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/th_TH.e0b85f367e58f60b8624c622b1032437.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/tr_TR.fc9f41bb32798fb8a6c4707d22858254.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/zh_CN.5fd71caa8aaef385118429015c7c45e9.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/zh_HK.a7cfc8e42ebddcee7fb458a9f42141c6.version`
- `/private/var/staged_system_apps/Files.app/Metadata.appintents/nlu/zh_TW.f8143987332b8168a01fe663a854672c.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/ar_SA.7f12b80f26859d356ec1b970c0b565b6.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/da_DK.2aa999519c719f52096ee08b72e9f585.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/de_DE.15f4a49b9b54488606d435656d2e1586.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/en_AU.bfb06e4ac61f178e1b7d72fff80b3830.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/en_GB.3e0baaabceb1befa1567f8a7f6345d7e.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/en_IN.b82a1d0aee5afa9d52a796f9fd292875.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/en_US.4162a835a5de48a35c405f94c4c95db4.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/es_ES.31682d40a77dc39e036044b2be463762.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/es_MX.0c0a12153b378698ec6c36bfda39870d.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/fi_FI.e67b8dba465c0936af22e47c62cdd231.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/fr_CA.b43e33f173bb6424db29a890888508e3.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/fr_FR.694aa61b6f8932a134e1bcdcf9839fa9.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/he_IL.c536cb2d9e96d79021035e98e124ee34.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/it_IT.104dfb1f42b8fd1d3150222960c13314.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/ja_JP.259d12d5d1dcc6f6ab97e219038531bb.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/ko_KR.298c6df5e970eaf77905ace64fe2cd87.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/ms_MY.07a612d4b5b6984f015e19ef89193c84.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/nl_NL.8f29582be8009184401994b6f990397d.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/pt_BR.b655c1354d510bbc4b89adfd9031ed8b.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/ru_RU.acdcbe2f2dbd369d3832fb036148ddda.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/sv_SE.9ab7be031b3efc915cd98bfe38441dd0.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/th_TH.40a50ab75a62d3f1944ce5919b8fa462.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/tr_TR.fd1cb0b0321cf996986b026f4c8c0f2b.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/zh_CN.92c5f85455f8f078e90ca5e8d22b4e47.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/zh_HK.7d2c02c7cd57b88e4f3c4d7fee7e5fba.version`
- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/zh_TW.3830d7912076009a7a8bdf3fb9870f4c.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/ar_SA.982111cad3a27ef08c033722d99f8290.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/da_DK.084e9a00f12c66c1fd8feedde0a34c56.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/de_DE.f2030dff760486e39bea11116e85273c.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/en_AU.993d7ee436c7a078f6fa475a363482c6.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/en_GB.39d49092b31dc84aa83387b3d6c31660.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/en_US.f985a294616c50ceb8860d3945305a7a.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/es_ES.4306df6b4a34e5eb77133518f10957b3.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/es_MX.f00cccf79520da29357cfa56d3705808.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/fi_FI.cc549265e4e64acbd8ede47f38b6be0d.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/fr_CA.40cd20c5b3ac9396b47c7f17c67eeb8c.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/fr_FR.f88268038b517a31a2e650d05a51e2e2.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/he_IL.dd196709682fd58df1c08e2e313be67d.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/it_IT.6db601e8c7150578bdf11d8f1104ed29.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/ja_JP.dbee38d80546686b114e1380eccde486.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/ko_KR.ab898a05b66b0c475e1b73f8bc2aefc0.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/ms_MY.9b9fbdb4b73bc99f07d8020209816784.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/nl_NL.1a68eb760a628a4eeb8684b7333074c5.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/pt_BR.27df5070f765fdd922c9d81909fad10a.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/ru_RU.a7187ac1f8949ce79659d3fe28cfc494.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/sv_SE.6e864871725be2b987d7cf2bdc18e498.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/th_TH.ac8c6850e7aae7ccef3453bb5ca20041.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/tr_TR.89601986cc342cdc5f9cbd7002d3fca5.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/zh_CN.d390ee1d3590028e058d05d72db8bafe.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/zh_HK.39552215ffe4155ae289ca1e6de249f8.version`
- `/private/var/staged_system_apps/Tips.app/Metadata.appintents/nlu/zh_TW.154a349fe326a375ed8a096db3e36b67.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/ar_SA.8c8a8323fefb546e5ab5f45943ca7f1e.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/da_DK.1e68525861719afd47c81e4d3f17e2b0.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/de_DE.e2dc81d32da690dd8c39a691373696f9.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/en_AU.0654d18acb86b2e1eb8bf6ba771e2f28.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/en_GB.43911db409db86a95ad51046cd9cff8e.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/en_US.1ee8bf4392900d4ec8e53d272467eb2b.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/es_ES.95277be9d23593242531a29319e6ab6a.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/es_MX.b27305dd349462bd5fb448f3461b9a08.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/fi_FI.b016bddc698b0b2bd1d75de136db607c.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/fr_CA.f8c9e709117fd2b1219c409480a85665.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/fr_FR.84cf264c3137e28288e57ead01fd067b.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/he_IL.24c825f65968a323f20990d57b3023f8.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/it_IT.08f9c8db568ffbff8a9ef2cb4c2cedee.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/ja_JP.57ca72f6b53e1c7d8b37af11c170f070.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/ko_KR.82ae564f5ba69c2f6e35bb655af7f9ef.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/ms_MY.8ef77b3805b396d383fcc93521be3a06.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/nl_NL.431758c54e1354486e8db363e7a9ba19.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/pt_BR.10d6e7ab1969e7f16647454af81d305c.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/ru_RU.388d9299f20a892e3226d73dcfe4bc07.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/sv_SE.2f1fbf37d46b13966360e96c040c51d0.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/th_TH.2932477922022d6e8d5c9d82fd0a2eae.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/tr_TR.dd75f303dbd5533eed23347b29b303d2.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/zh_CN.72bfb2876f99862fdb6b12397661168e.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/zh_HK.46dd619f62c68b8a618f68324eb427b1.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Metadata.appintents/nlu/zh_TW.c58d5fe53400a0e96ebbed72dbd527cf.version`
- `/usr/standalone/firmware/nfrestore/firmware/fw/SN100V_FW_A3_01_01_99_rev148069.bin`
- `/usr/standalone/firmware/nfrestore/firmware/fw/SN200V_FW_B1_02_01_9C_rev148061.bin`
- `/usr/standalone/firmware/nfrestore/firmware/fw/SN300V_FW_B0_02_01_44_rev148056.bin`
- `/usr/standalone/firmware/nfrestore/firmware/rf/SN100V_FW_A3_01_01_99_rev148069.plist`
- `/usr/standalone/firmware/nfrestore/firmware/rf/SN200V_FW_B1_02_01_9C_rev148061.plist`
- `/usr/standalone/firmware/nfrestore/firmware/rf/SN300V_FW_B0_02_01_44_rev148056.plist`

</details>

## Feature Flags

### ⬆️ Updated (5)

<details>
  <summary><i>View Updated</i></summary>

#### AppStore.plist

>  `Domain/AppStore.plist`

```diff

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
+	<key>game_center_shelves_crossfire_referral_2023G</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>hero_carousel</key>
 	<dict>
 		<key>Enabled</key>

```

#### AssessmentMode.plist

>  `Domain/AssessmentMode.plist`

```diff

 <?xml version="1.0" encoding="UTF-8"?>
 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
-<dict>
-	<key>iOSAgent</key>
-	<dict>
-		<key>Enabled</key>
-		<true/>
-	</dict>
-</dict>
+<dict/>
 </plist>
 

```

#### Photos.plist

>  `Domain/Photos.plist`

```diff

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
+	<key>CloudComputeStateSync</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>ComputeCache</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### Siri.plist

>  `Domain/Siri.plist`

```diff

 		<key>Enabled</key>
 		<true/>
 	</dict>
+	<key>siri_location_services_prompting</key>
+	<dict>
+		<key>Enabled</key>
+		<true/>
+	</dict>
 	<key>siri_request_dispatcher</key>
 	<dict>
 		<key>Enabled</key>

```

#### TVApp.plist

>  `Domain/TVApp.plist`

```diff

 		<key>Enabled</key>
 		<true/>
 	</dict>
-	<key>begonia</key>
+	<key>cider</key>
 	<dict>
 		<key>Enabled</key>
 		<true/>
 	</dict>
-	<key>cider</key>
+	<key>contextual_download</key>
 	<dict>
 		<key>Enabled</key>
 		<true/>
 	</dict>
-	<key>contextual_download</key>
+	<key>denali</key>
 	<dict>
 		<key>Enabled</key>
 		<true/>

```


</details>

## EOF
