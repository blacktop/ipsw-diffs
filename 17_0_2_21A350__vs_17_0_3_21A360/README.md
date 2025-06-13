# 17.0.2 (21A350) .vs 17.0.3 (21A360)

## IPSWs

- `iPhone16,1_17.0.2_21A350_Restore.ipsw`
- `iPhone16,1_17.0.3_21A360_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 17.0.2 *(21A350)* | 23.0.0 | 10002.2.12~1 | Fri, 15Sep2023 13:42:21 PDT |
| 17.0.3 *(21A360)* | 23.0.0 | 10002.2.13~1 | Sat, 30Sep2023 17:17:51 PDT |

### Kexts

#### ⬆️ Updated (22)

<details>
  <summary><i>View Updated</i></summary>

>  `com.apple.AGXG16P`

```diff

   __DATA_CONST.__const: 0x10350
   __DATA_CONST.__kalloc_type: 0x20c0
   __DATA_CONST.__kalloc_var: 0x30c0
-  UUID: 4D131C2D-E0E8-355B-8B85-241DC5B4E064
+  UUID: 57CAFC38-926C-3408-B375-9E57E48A8C57
   Functions: 1203
   Symbols:   0
   CStrings:  1651
CStrings:
+ "Sep 30 2023 17:19:31"
- "Sep 15 2023 13:44:01"

```

>  `com.apple.driver.AppleAOPAudio`

```diff

   __DATA_CONST.__mod_term_func: 0xe0
   __DATA_CONST.__const: 0xb7d0
   __DATA_CONST.__kalloc_type: 0xa00
-  UUID: CA9E1A8A-1D46-3A59-8898-B4D729149D5C
+  UUID: 95F8A812-0331-3BDD-8EA9-7D6168BD4D78
   Functions: 711
   Symbols:   0
   CStrings:  1152
CStrings:
+ "17:09:04"
+ "17:09:13"
+ "Sep 30 2023"
- "13:33:19"
- "13:33:33"
- "Sep 15 2023"

```

>  `com.apple.driver.AppleAOPVoiceTrigger`

```diff

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xd70
   __DATA_CONST.__kalloc_type: 0x180
-  UUID: E1DA7DFE-F6F0-3068-A72A-527AFBB5DF0C
+  UUID: 906745A1-7012-3DAA-917E-7AF1BD19EBA8
   Functions: 104
   Symbols:   0
   CStrings:  202
CStrings:
+ "17:17:58"
+ "Sep 30 2023"
- "13:43:38"
- "Sep 15 2023"

```

>  `com.apple.driver.AppleAVE2`

```diff

   __DATA_CONST.__const: 0x4648
   __DATA_CONST.__kalloc_type: 0x1540
   __DATA_CONST.__kalloc_var: 0x8c0
-  UUID: 23C2901D-D8EB-3FEB-9514-38DC1584AF62
+  UUID: D0FABA27-88AB-3A82-8E2B-30C509672957
   Functions: 1259
   Symbols:   0
   CStrings:  5470
CStrings:
+ "17:21:58"
+ "Sep 30 2023"
- "13:45:41"
- "Sep 15 2023"

```

>  `com.apple.driver.AppleH16ANEInterface`

```diff

   __DATA_CONST.__const: 0x57a0
   __DATA_CONST.__kalloc_type: 0x2240
   __DATA_CONST.__kalloc_var: 0x1cc0
-  UUID: 6B4AF867-6A51-374C-BB44-73A024BF2B36
+  UUID: 788B289B-1550-3034-8E7D-255D8845D3B6
   Functions: 918
   Symbols:   0
   CStrings:  2643
CStrings:
+ "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/System/Library/Frameworks/Kernel.framework/PrivateHeaders/kernel_sdkroot/usr/include/c++/v1/span"
- "/AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/System/Library/Frameworks/Kernel.framework/PrivateHeaders/kernel_sdkroot/usr/include/c++/v1/span"

```

>  `com.apple.driver.AppleHIDTransportSPI`

```diff

   __DATA_CONST.__const: 0x31e0
   __DATA_CONST.__kalloc_type: 0xa80
   __DATA_CONST.__kalloc_var: 0x320
-  UUID: BD28D4D9-013A-3C5D-AA76-FF7C2F981EF9
+  UUID: B2EFCA8D-C25A-30B5-9F55-148B87FBFFED
   Functions: 353
   Symbols:   0
   CStrings:  855
CStrings:
+ "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/hidspi/HSMDevice.h"
+ "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/hidspi/HSMDeviceInterface.h"
+ "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/hidspi/HSMDeviceTest.h"
+ "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/hidspi/HSMHIDInterface.h"
+ "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/hidspi/HSMParserTest.h"
+ "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/hidspi/HSMSPITest.h"
+ "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/hidspi/HSMTransferDevice.h"
+ "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/hidspi/HSMTransferTest.h"
+ "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/hidspi/HSParserDevice.h"
+ "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/hidspi/HSParserTest.h"
+ "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/hidspi/HSTransferTest.h"
- "/AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/hidspi/HSMDevice.h"
- "/AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/hidspi/HSMDeviceInterface.h"
- "/AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/hidspi/HSMDeviceTest.h"
- "/AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/hidspi/HSMHIDInterface.h"
- "/AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/hidspi/HSMParserTest.h"
- "/AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/hidspi/HSMSPITest.h"
- "/AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/hidspi/HSMTransferDevice.h"
- "/AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/hidspi/HSMTransferTest.h"
- "/AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/hidspi/HSParserDevice.h"
- "/AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/hidspi/HSParserTest.h"
- "/AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/hidspi/HSTransferTest.h"

```

>  `com.apple.driver.AppleMobileFileIntegrity`

```diff

   __DATA_CONST.__const: 0x36c0
   __DATA_CONST.__kalloc_type: 0xe40
   __DATA_CONST.__kalloc_var: 0x1270
-  UUID: CA9E79FA-AB68-3FB7-B9E9-FFB7623A0EF8
+  UUID: 572BC0B9-A44D-37F1-9768-BB2C15D18D00
   Functions: 539
   Symbols:   0
   CStrings:  912
CStrings:
+ "17:09:25"
+ "Sep 30 2023"
- "13:33:44"
- "Sep 15 2023"

```

>  `com.apple.driver.AppleSEPKeyStore`

```diff

   __DATA_CONST.__const: 0x3890
   __DATA_CONST.__kalloc_type: 0xd40
   __DATA_CONST.__kalloc_var: 0x140
-  UUID: 0EFCD129-C8C5-300F-A5DC-DEB967D29E49
+  UUID: 0AC0EED0-4598-3F7D-9C5A-8EDA3DE9D4CC
   Functions: 573
   Symbols:   0
   CStrings:  318
CStrings:
+ "17:20:21"
+ "Sep 30 2023"
- "13:48:48"
- "Sep 15 2023"

```

>  `com.apple.driver.AppleSMC`

```diff

   __DATA_CONST.__const: 0x74e0
   __DATA_CONST.__kalloc_type: 0x600
   __DATA_CONST.__kalloc_var: 0xa0
-  UUID: C4D9D988-A3F4-3AC8-B400-FE549B7862E5
+  UUID: D18D2B73-5F72-3576-AE06-190DFEB11ED7
   Functions: 463
   Symbols:   0
   CStrings:  856
CStrings:
+ "17:19:50"
+ "17:19:52"
+ "Sep 30 2023"
- "13:44:35"
- "13:44:37"
- "Sep 15 2023"

```

>  `com.apple.driver.AppleSPMIPMU`

```diff

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xf00
   __DATA_CONST.__kalloc_type: 0x140
-  UUID: 88873EEC-6596-37D5-A670-7DFD8FCF7E48
+  UUID: BAFD0019-616A-313D-B248-77145F5586E4
   Functions: 107
   Symbols:   0
   CStrings:  342
CStrings:
+ "%s::handleStart: %s _pmuNub: %p ** configuration not found ** built 17:09:13 Sep 30 2023\n"
+ "%s::handleStart: ro=%d nvram=%d helper=%d %s _pmuNub: %p 0x%04x:0x%04x-0x%04x built 17:09:13 Sep 30 2023\n"
+ "%s::start: %s _pmuNub: %p ** configuration not found ** built 17:09:13 Sep 30 2023\n"
+ "%s::start: %s _pmuNub: %p built 17:09:13 Sep 30 2023\n"
- "%s::handleStart: %s _pmuNub: %p ** configuration not found ** built 13:33:23 Sep 15 2023\n"
- "%s::handleStart: ro=%d nvram=%d helper=%d %s _pmuNub: %p 0x%04x:0x%04x-0x%04x built 13:33:23 Sep 15 2023\n"
- "%s::start: %s _pmuNub: %p ** configuration not found ** built 13:33:23 Sep 15 2023\n"
- "%s::start: %s _pmuNub: %p built 13:33:23 Sep 15 2023\n"

```

>  `com.apple.driver.AppleSmartIO2`

```diff

   __DATA_CONST.__const: 0x21f0
   __DATA_CONST.__kalloc_type: 0x280
   __DATA_CONST.__kalloc_var: 0xa0
-  UUID: 045F2CC3-16D7-3226-AC85-99AA6D6987B3
+  UUID: 10799323-5CD5-32A2-8432-03A11056DBC3
   Functions: 366
   Symbols:   0
   CStrings:  378
CStrings:
+ "17:10:46"
+ "Sep 30 2023"
- "13:35:13"
- "Sep 15 2023"

```

>  `com.apple.driver.AppleT8130CLPC`

```diff

   __DATA_CONST.__const: 0x4898
   __DATA_CONST.__kalloc_type: 0x380
   __DATA_CONST.__kalloc_var: 0x370
-  UUID: C09339B9-8756-3A50-84B6-A02BF2D69CDE
+  UUID: 110B4898-FF9A-3EB8-AEA7-9F6606876B18
   Functions: 640
   Symbols:   0
   CStrings:  445
CStrings:
+ "2023-09-30T17:17:23-07:00"
- "2023-09-15T13:41:38-07:00"

```

>  `com.apple.driver.AppleUSBDeviceMux`

```diff

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0x780
   __DATA_CONST.__kalloc_type: 0x440
-  UUID: BB259055-6F8F-326C-A748-FF2125E7A144
+  UUID: 571D1AA4-8A15-3EB6-92F7-501DD686CDC0
   Functions: 69
   Symbols:   0
   CStrings:  144
CStrings:
+ "17:19:21"
+ "Sep 30 2023"
- "13:43:22"
- "Sep 15 2023"

```

>  `com.apple.driver.AppleUVDM`

```diff

-14.2.2.0.0
+14.2.3.0.0
   __TEXT.__cstring: 0x452
   __TEXT_EXEC.__text: 0x1f40
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xdc8
   __DATA_CONST.__kalloc_type: 0x80
-  UUID: E46CAE6F-F68D-3446-9A54-13CE3C43E7B1
+  UUID: C2EABF85-DAD3-36D8-A7EB-F9B6A2F4025B
   Functions: 30
   Symbols:   0
   CStrings:  40

```

>  `com.apple.driver.AppleUVDMDriver`

```diff

-14.2.2.0.0
-  __TEXT.__cstring: 0x1183
-  __TEXT_EXEC.__text: 0x6440
+14.2.3.0.0
+  __TEXT.__cstring: 0x12ce
+  __TEXT_EXEC.__text: 0x657c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x188
   __DATA.__common: 0xb0

   __DATA_CONST.__mod_term_func: 0x20
   __DATA_CONST.__const: 0x1078
   __DATA_CONST.__kalloc_type: 0x100
-  UUID: 67DC6612-E79D-3A40-BF50-3785A580F9D3
+  UUID: CB745706-F2F2-3423-9313-BBD6F58D0BD4
   Functions: 78
   Symbols:   0
-  CStrings:  150
+  CStrings:  153
 
CStrings:
+ "%s::%s - [%s] ERROR: bytesLeft2Read [0x%X] < returnLen (already read here) [0x%X]; more bytes read than left to be read\n\n"
+ "%s::%s - [%s] ERROR: loopIter=0x%X >= MAX_ACCESS_TIMES=0x%X OR bytesRead=0x%X >= MAX_APPLEVDO_LEN=0x%X\n\n"
+ "%s::%s - [%s] ERROR: reading more than the outBufLen [0x%X], bytesRead [0x%X], returnLen [0x%X]\n\n"
+ "%s::%s - [%s] ERROR: returnLen [0x%X] != length2read [0x%X]\n\n"
- "%s::%s - [%s] Try to read 4 bytes at a time instead...\n"

```

>  `com.apple.driver.AudioDMAController-T8130`

```diff

   __DATA_CONST.__mod_term_func: 0x20
   __DATA_CONST.__const: 0x1988
   __DATA_CONST.__kalloc_type: 0x340
-  UUID: 34D56E83-1ED5-39DE-9FAA-D8F7C8C1D85D
+  UUID: 4C49687A-EFC5-3690-9D35-53F147A5A684
   Functions: 224
   Symbols:   0
   CStrings:  366
CStrings:
+ "17:11:15"
+ "Sep 30 2023"
- "13:36:12"
- "Sep 15 2023"

```

>  `com.apple.driver.RTBuddy`

```diff

   __DATA_CONST.__const: 0xa368
   __DATA_CONST.__kalloc_type: 0x1200
   __DATA_CONST.__kalloc_var: 0xf0
-  UUID: D9F76BD6-0A60-3E22-96E0-C998D7048A9D
+  UUID: F661C59D-99A4-3550-A152-E7F0BF13D182
   Functions: 1352
   Symbols:   0
   CStrings:  987
CStrings:
+ "17:19:03"
+ "Sep 30 2023"
- "13:42:58"
- "Sep 15 2023"

```

>  `com.apple.filesystems.apfs`

```diff

   __DATA_CONST.__const: 0x5d80
   __DATA_CONST.__kalloc_type: 0x4b40
   __DATA_CONST.__kalloc_var: 0x2760
-  UUID: 9C070308-6067-3B26-B2CF-C3E25145FEE4
+  UUID: A2E492B7-D637-31D3-B78F-7FF29724FB9A
   Functions: 1813
   Symbols:   0
   CStrings:  5944
CStrings:
+ "17:10:43"
+ "2023/09/30"
+ "Sep 30 2023"
- "13:36:01"
- "2023/09/15"
- "Sep 15 2023"

```

>  `com.apple.iokit.IOPCIFamily`

```diff

   __DATA_CONST.__const: 0x3c78
   __DATA_CONST.__kalloc_type: 0x600
   __DATA_CONST.__kalloc_var: 0x190
-  UUID: 3D7979C5-2479-366E-93C4-18E78D36E948
+  UUID: 6C72128A-0231-3CE6-B7C8-831F9E30A9FF
   Functions: 430
   Symbols:   0
   CStrings:  627
CStrings:
+ "17:09:33"
+ "Sep 30 2023"
- "13:35:12"
- "Sep 15 2023"

```

>  `com.apple.iokit.IOThunderboltFamily`

```diff

   __DATA_CONST.__const: 0x1cf40
   __DATA_CONST.__kalloc_type: 0x1d00
   __DATA_CONST.__kalloc_var: 0x910
-  UUID: EAE580ED-9655-33E1-858F-E555F53869B1
+  UUID: D0E63963-E592-399E-98E7-295EE6C6B0B5
   Functions: 2780
   Symbols:   0
   CStrings:  2677
CStrings:
+ "17:09:10"
+ "Sep 30 2023"
- "13:35:33"
- "Sep 15 2023"

```

>  `com.apple.kernel`

```diff

-10002.2.12.0.0
+10002.2.13.0.0
   __TEXT.__const: 0x34980
   __TEXT.__copyio_vectors: 0xf0
-  __TEXT.__cstring: 0x61fe4
+  __TEXT.__cstring: 0x6203d
   __TEXT.__os_log: 0x20f83
   __TEXT.__eh_frame: 0x3e0
   __DATA_CONST.__auth_ptr: 0x8

   __DATA_CONST.__brk_desc: 0x60
   __DATA_SPTM.__const: 0x3c000
   __TEXT_EXEC.__hib_text: 0xc88
-  __TEXT_EXEC.__text: 0x73b2e0
+  __TEXT_EXEC.__text: 0x73b430
   __TEXT_BOOT_EXEC.__bootcode: 0x4cf8
   __KLD.__text: 0x1630
   __LASTDATA_CONST.__mod_init_func: 0x8

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x442b3
-  UUID: CCBEAC40-5507-3609-98B4-19ABEE384680
+  UUID: 96BF2B4B-1AFB-3D40-9C07-18FCD26637EE
   Functions: 18935
   Symbols:   0
-  CStrings:  15502
+  CStrings:  15504
 
CStrings:
+ "map %p va 0x%llx obj %p,%u saved %p,%u: unexpected CoW @%s:%d"
+ "object_is_contended @%s:%d"

```

>  `com.apple.security.AppleImage4`

```diff

   __DATA_CONST.__const: 0x97f8
   __DATA_CONST.__kalloc_type: 0x1c0
   __DATA_CONST.__img4_rt: 0x20
-  UUID: 8C43978F-4D94-3A12-904D-0343960E9B7B
+  UUID: DF732C36-D68A-320C-B2AC-66AE620DDAEB
   Functions: 425
   Symbols:   0
   CStrings:  707
CStrings:
+ "@(#)VERSION:Darwin Image4 Validator Version 5.0.0: Sat Sep 30 17:08:53 PDT 2023; root:AppleImage4-245~3335/AppleImage4/RELEASE_ARM64E"
+ "Darwin Image4 Validator Version 5.0.0: Sat Sep 30 17:08:53 PDT 2023; root:AppleImage4-245~3335/AppleImage4/RELEASE_ARM64E"
- "@(#)VERSION:Darwin Image4 Validator Version 5.0.0: Fri Sep 15 13:33:36 PDT 2023; root:AppleImage4-245~3313/AppleImage4/RELEASE_ARM64E"
- "Darwin Image4 Validator Version 5.0.0: Fri Sep 15 13:33:36 PDT 2023; root:AppleImage4-245~3313/AppleImage4/RELEASE_ARM64E"

```

</details>

## MachO

### ⬆️ Updated (293)

<details>
  <summary><i>View Updated</i></summary>

- [/Applications/AppStore.app/AppStore](MACHOS/AppStore.md)
- [/Applications/AppStore.app/PlugIns/AppStoreWidgetsExtension.appex/AppStoreWidgetsExtension](MACHOS/AppStoreWidgetsExtension.md)
- [/Applications/AppStore.app/PlugIns/ProductPageExtension.appex/ProductPageExtension](MACHOS/ProductPageExtension.md)
- [/Applications/AppStore.app/PlugIns/SubscribePageExtension.appex/SubscribePageExtension](MACHOS/SubscribePageExtension.md)
- [/Applications/AskToMessagesHost.app/AskToMessagesHost](MACHOS/AskToMessagesHost.md)
- [/Applications/AskToMessagesHost.app/Extensions/AskToExtension.appex/AskToExtension](MACHOS/AskToExtension.md)
- [/Applications/AskToMessagesHost.app/PlugIns/AskToMessagesExtension.appex/AskToMessagesExtension](MACHOS/AskToMessagesExtension.md)
- [/Applications/AuthenticationServicesUI.app/AuthenticationServicesUI](MACHOS/AuthenticationServicesUI.md)
- [/Applications/AuthenticationServicesUI.app/PlugIns/AccountAuthenticationModificationExtensionHelper.appex/AccountAuthenticationModificationExtensionHelper](MACHOS/AccountAuthenticationModificationExtensionHelper.md)
- [/Applications/CTCarrierSpaceAuth.app/CTCarrierSpaceAuth](MACHOS/CTCarrierSpaceAuth.md)
- [/Applications/ColorPickerUIService.app/ColorPickerUIService](MACHOS/ColorPickerUIService.md)
- [/Applications/ContactPhotoCarouselRemoteAlert.app/ContactPhotoCarouselRemoteAlert](MACHOS/ContactPhotoCarouselRemoteAlert.md)
- [/Applications/ContactlessReaderUIService.app/ContactlessReaderUIService](MACHOS/ContactlessReaderUIService.md)
- [/Applications/ContinuityCaptureShieldUI.app/ContinuityCaptureShieldUI](MACHOS/ContinuityCaptureShieldUI.md)
- [/Applications/Coverage Details.app/Coverage Details](MACHOS/Coverage_Details.md)
- [/Applications/DiagnosticsService.app/DiagnosticsService](MACHOS/DiagnosticsService.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3903.appex/Diagnostic-3903](MACHOS/Diagnostic-3903.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3904.appex/Diagnostic-3904](MACHOS/Diagnostic-3904.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3905.appex/Diagnostic-3905](MACHOS/Diagnostic-3905.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3906.appex/Diagnostic-3906](MACHOS/Diagnostic-3906.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3909.appex/Diagnostic-3909](MACHOS/Diagnostic-3909.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3939.appex/Diagnostic-3939](MACHOS/Diagnostic-3939.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3942.appex/Diagnostic-3942](MACHOS/Diagnostic-3942.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4006.appex/Diagnostic-4006](MACHOS/Diagnostic-4006.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4153.appex/Diagnostic-4153](MACHOS/Diagnostic-4153.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4154.appex/Diagnostic-4154](MACHOS/Diagnostic-4154.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4276.appex/Diagnostic-4276](MACHOS/Diagnostic-4276.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4579.appex/Diagnostic-4579](MACHOS/Diagnostic-4579.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8187.appex/Diagnostic-8187](MACHOS/Diagnostic-8187.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8246.appex/Diagnostic-8246](MACHOS/Diagnostic-8246.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8381.appex/Diagnostic-8381](MACHOS/Diagnostic-8381.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8441.appex/Frameworks/DiagnosticsSupport.framework/DiagnosticsSupport](MACHOS/DiagnosticsSupport.md)
- [/Applications/DiagnosticsService.app/PlugIns/SystemReport-AirPods.appex/SystemReport-AirPods](MACHOS/SystemReport-AirPods.md)
- [/Applications/DiagnosticsService.app/PlugIns/SystemReport-BatteryCase.appex/SystemReport-BatteryCase](MACHOS/SystemReport-BatteryCase.md)
- [/Applications/DiagnosticsService.app/PlugIns/SystemReport-iOS-D83-D84.appex/SystemReport-iOS-D83-D84](MACHOS/SystemReport-iOS-D83-D84.md)
- [/Applications/FaceTimeLinkTrampoline.app/FaceTimeLinkTrampoline](MACHOS/FaceTimeLinkTrampoline.md)
- [/Applications/Family.app/Family](MACHOS/Family.md)
- [/Applications/Family.app/PlugIns/FAFollowupExtension.appex/FAFollowupExtension](MACHOS/FAFollowupExtension.md)
- [/Applications/Family.app/PlugIns/InviteMessageBubbleExtension.appex/InviteMessageBubbleExtension](MACHOS/InviteMessageBubbleExtension.md)
- [/Applications/FieldTest.app/FieldTest](MACHOS/FieldTest.md)
- [/Applications/FontPickerUIService.app/FontPickerUIService](MACHOS/FontPickerUIService.md)
- [/Applications/InCallService.app/InCallService](MACHOS/InCallService.md)
- [/Applications/InCallService.app/PlugIns/FaceTimeShareExtension.appex/FaceTimeShareExtension](MACHOS/FaceTimeShareExtension.md)
- [/Applications/InCallService.app/PlugIns/IntentsUI.appex/IntentsUI](MACHOS/IntentsUI.md)
- [/Applications/InCallService.app/PlugIns/RemotePeoplePicker.appex/RemotePeoplePicker](MACHOS/RemotePeoplePicker.md)
- [/Applications/MessagesViewService.app/MessagesViewService](MACHOS/MessagesViewService.md)
- [/Applications/MobilePhone.app/MobilePhone](MACHOS/MobilePhone.md)
- [/Applications/MobilePhone.app/PlugIns/VoicemailMessageNotificationExtension.appex/VoicemailMessageNotificationExtension](MACHOS/VoicemailMessageNotificationExtension.md)
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
- [/Applications/MusicUIService.app/MusicUIService](MACHOS/MusicUIService.md)
- [/Applications/PASViewService.app/PASViewService](MACHOS/PASViewService.md)
- [/Applications/PeopleMessageService.app/Extensions/PeopleLegacyMessageService.appex/PeopleLegacyMessageService](MACHOS/PeopleLegacyMessageService.md)
- [/Applications/PeopleMessageService.app/PeopleMessageService](MACHOS/PeopleMessageService.md)
- [/Applications/PeopleMessageService.app/PlugIns/PeopleMessagesAskToBuy.appex/PeopleMessagesAskToBuy](MACHOS/PeopleMessagesAskToBuy.md)
- [/Applications/PeopleMessageService.app/PlugIns/PeopleMessagesScreenTime.appex/PeopleMessagesScreenTime](MACHOS/PeopleMessagesScreenTime.md)
- [/Applications/PeopleViewService.app/PeopleViewService](MACHOS/PeopleViewService.md)
- [/Applications/PeopleViewService.app/PlugIns/PeopleWidget_iOSExtension.appex/PeopleWidget_iOSExtension](MACHOS/PeopleWidget_iOSExtension.md)
- [/Applications/PeopleViewService.app/PlugIns/SelectPerson_iOS.appex/SelectPerson_iOS](MACHOS/SelectPerson_iOS.md)
- [/Applications/ProximityReaderUIService.app/ProximityReaderUIService](MACHOS/ProximityReaderUIService.md)
- [/Applications/RemoteiCloudQuotaUI.app/RemoteiCloudQuotaUI](MACHOS/RemoteiCloudQuotaUI.md)
- [/Applications/SOSBuddy.app/SOSBuddy](MACHOS/SOSBuddy.md)
- [/Applications/SafariViewService.app/SafariViewService](MACHOS/SafariViewService.md)
- [/Applications/SafetyMonitorApp.app/SafetyMonitorApp](MACHOS/SafetyMonitorApp.md)
- [/Applications/Screen Time.app/PlugIns/ScreenTimeWidgetExtension.appex/ScreenTimeWidgetExtension](MACHOS/ScreenTimeWidgetExtension.md)
- [/Applications/Screen Time.app/PlugIns/ScreenTimeWidgetIntentsExtension.appex/ScreenTimeWidgetIntentsExtension](MACHOS/ScreenTimeWidgetIntentsExtension.md)
- [/Applications/Screen Time.app/Screen Time](MACHOS/Screen_Time.md)
- [/Applications/ScreenTimeUnlock.app/ScreenTimeUnlock](MACHOS/ScreenTimeUnlock.md)
- [/Applications/Setup.app/Setup](MACHOS/Setup.md)
- [/Applications/Sidecar.app/PlugIns/ContinuityCapture.appex/ContinuityCapture](MACHOS/ContinuityCapture.md)
- [/Applications/StickersUltra.app/PlugIns/StickersUltraExtension.appex/StickersUltraExtension](MACHOS/StickersUltraExtension.md)
- [/Applications/StickersUltra.app/StickersUltra](MACHOS/StickersUltra.md)
- [/Applications/Web.app/Web](MACHOS/Web.md)
- [/Applications/iCloud+.app/iCloud+](MACHOS/iCloud+.md)
- [/Applications/iMessageAppsViewService.app/iMessageAppsViewService](MACHOS/iMessageAppsViewService.md)
- [/System/Applications/Family/InviteMessageBubbleExtension.appex/InviteMessageBubbleExtension](MACHOS/InviteMessageBubbleExtension.md)
- [/System/DriverKit/usr/lib/libSystem_debug.dylib](MACHOS/libSystem_debug.dylib.md)
- [/System/Library/Accounts/DataclassOwners/Bookmarks.bundle/Bookmarks](MACHOS/Bookmarks.md)
- [/System/Library/Accounts/DataclassOwners/FreeformDataclassOwner.bundle/FreeformDataclassOwner](MACHOS/FreeformDataclassOwner.md)
- [/System/Library/Accounts/DataclassOwners/MessagesDataclassOwner.bundle/MessagesDataclassOwner](MACHOS/MessagesDataclassOwner.md)
- [/System/Library/Accounts/Notification/CloudBookmarksAccountsNotifier.bundle/CloudBookmarksAccountsNotifier](MACHOS/CloudBookmarksAccountsNotifier.md)
- [/System/Library/Accounts/Notification/NDOAccountNotificationPlugin.bundle/NDOAccountNotificationPlugin](MACHOS/NDOAccountNotificationPlugin.md)
- [/System/Library/AppRemovalServices/com.apple.Bridge.appremoval.xpc/com.apple.Bridge.appremoval](MACHOS/com.apple.Bridge.appremoval.md)
- [/System/Library/AppleMediaServices/WebUI/PlugIns/MusicAMSUIWebPlugin.bundle/MusicAMSUIWebPlugin](MACHOS/MusicAMSUIWebPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/MessagesFlowDelegatePlugin.bundle/MessagesFlowDelegatePlugin](MACHOS/MessagesFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SafetySessionFlowPlugin.bundle/SafetySessionFlowPlugin](MACHOS/SafetySessionFlowPlugin.md)
- [/System/Library/Assistant/Plugins/ChatKitAssistant.assistantBundle/ChatKitAssistant](MACHOS/ChatKitAssistant.md)
- [/System/Library/Assistant/Plugins/Safari.assistantBundle/Safari](MACHOS/Safari.md)
- [/System/Library/Assistant/Plugins/WebSearch.assistantBundle/WebSearch](MACHOS/WebSearch.md)
- [/System/Library/Assistant/UIPlugins/AddressBook.siriUIBundle/AddressBook](MACHOS/AddressBook.md)
- [/System/Library/CloudRecommendations/ClientSources/ICQReviewLargeFilesRecommendations.bundle/ICQReviewLargeFilesRecommendations](MACHOS/ICQReviewLargeFilesRecommendations.md)
- [/System/Library/ControlCenter/Bundles/PingMyWatchControlCenterUI.bundle/PingMyWatchControlCenterUI](MACHOS/PingMyWatchControlCenterUI.md)
- [/System/Library/ControlCenter/Bundles/SilenceCallsCCWidget.bundle/SilenceCallsCCWidget](MACHOS/SilenceCallsCCWidget.md)
- [/System/Library/CoreServices/OverlayUI.app/OverlayUI](MACHOS/OverlayUI.md)
- [/System/Library/CoreServices/SafariSupport.bundle/SafariBookmarksSyncAgent](MACHOS/SafariBookmarksSyncAgent.md)
- [/System/Library/DataClassMigrators/BuddyMigrator.migrator/BuddyMigrator](MACHOS/BuddyMigrator.md)
- [/System/Library/DataClassMigrators/CloudTabsMigrator.migrator/CloudTabsMigrator](MACHOS/CloudTabsMigrator.md)
- [/System/Library/DataClassMigrators/MobileSafari.migrator/MobileSafari](MACHOS/MobileSafari.md)
- [/System/Library/DataClassMigrators/WebBookmarks.migrator/WebBookmarks](MACHOS/WebBookmarks.md)
- [/System/Library/DataClassMigrators/WiFiDataMigrator.migrator/WiFiDataMigrator](MACHOS/WiFiDataMigrator.md)
- [/System/Library/Extensions/AppleUVDM.kext/PlugIns/AppleUVDMLib.plugin/AppleUVDMLib](MACHOS/AppleUVDMLib.md)
- [/System/Library/Frameworks/ContactsUI.framework/PlugIns/ContactViewViewService.appex/ContactViewViewService](MACHOS/ContactViewViewService.md)
- [/System/Library/Frameworks/ContactsUI.framework/PlugIns/ContactsViewService.appex/ContactsViewService](MACHOS/ContactsViewService.md)
- [/System/Library/Frameworks/ContactsUI.framework/PlugIns/MonogramPosterExtension.appex/MonogramPosterExtension](MACHOS/MonogramPosterExtension.md)
- [/System/Library/Frameworks/CoreLocation.framework/PlugIns/CoreLocationRepromptAlwaysAuthPromptPlugin.appex/CoreLocationRepromptAlwaysAuthPromptPlugin](MACHOS/CoreLocationRepromptAlwaysAuthPromptPlugin.md)
- [/System/Library/Frameworks/CoreLocation.framework/PlugIns/CoreLocationTemporaryPreciseAuthPromptPlugin.appex/CoreLocationTemporaryPreciseAuthPromptPlugin](MACHOS/CoreLocationTemporaryPreciseAuthPromptPlugin.md)
- [/System/Library/Frameworks/CoreLocation.framework/PlugIns/CoreLocationVanillaWhenInUseAuthPromptPlugin.appex/CoreLocationVanillaWhenInUseAuthPromptPlugin](MACHOS/CoreLocationVanillaWhenInUseAuthPromptPlugin.md)
- [/System/Library/Frameworks/CoreLocationUI.framework/XPCServices/com.apple.corelocation.locationUI.xpc/com.apple.corelocation.locationUI](MACHOS/com.apple.corelocation.locationUI.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenterMobileHelper](MACHOS/CommCenterMobileHelper.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenterRootHelper](MACHOS/CommCenterRootHelper.md)
- [/System/Library/Frameworks/ProximityReader.framework/merchantd](MACHOS/merchantd.md)
- [/System/Library/Frameworks/SafariServices.framework/PlugIns/SafariServices.wkbundle/SafariServices](MACHOS/SafariServices.md)
- [/System/Library/Frameworks/SafariServices.framework/XPCServices/com.apple.SafariServices.ContentBlockerLoader.xpc/com.apple.SafariServices.ContentBlockerLoader](MACHOS/com.apple.SafariServices.ContentBlockerLoader.md)
- [/System/Library/Frameworks/ScreenTime.framework/PlugIns/ScreenTimeWebExtension.appex/ScreenTimeWebExtension](MACHOS/ScreenTimeWebExtension.md)
- [/System/Library/Frameworks/UIKit.framework/PlugIns/com.apple.UIKit.ColorPicker.appex/com.apple.UIKit.ColorPicker](MACHOS/com.apple.UIKit.ColorPicker.md)
- [/System/Library/Frameworks/UIKit.framework/PlugIns/com.apple.UIKit.FontPicker.appex/com.apple.UIKit.FontPicker](MACHOS/com.apple.UIKit.FontPicker.md)
- [/System/Library/Frameworks/UIKit.framework/PlugIns/com.apple.UIKit.ShareUI.appex/com.apple.UIKit.ShareUI](MACHOS/com.apple.UIKit.ShareUI.md)
- [/System/Library/Frameworks/UIKit.framework/PlugIns/com.apple.UIKit.TextFormatting.appex/com.apple.UIKit.TextFormatting](MACHOS/com.apple.UIKit.TextFormatting.md)
- [/System/Library/Frameworks/UIKit.framework/PlugIns/com.apple.UIKit.screenpicker.appex/com.apple.UIKit.screenpicker](MACHOS/com.apple.UIKit.screenpicker.md)
- [/System/Library/Frameworks/WebKit.framework/Daemons/adattributiond](MACHOS/adattributiond.md)
- [/System/Library/Frameworks/WebKit.framework/XPCServices/com.apple.WebKit.GPU.xpc/com.apple.WebKit.GPU](MACHOS/com.apple.WebKit.GPU.md)
- [/System/Library/Frameworks/WebKit.framework/XPCServices/com.apple.WebKit.Networking.xpc/com.apple.WebKit.Networking](MACHOS/com.apple.WebKit.Networking.md)
- [/System/Library/Frameworks/WebKit.framework/XPCServices/com.apple.WebKit.WebContent.CaptivePortal.xpc/com.apple.WebKit.WebContent.CaptivePortal](MACHOS/com.apple.WebKit.WebContent.CaptivePortal.md)
- [/System/Library/Frameworks/WebKit.framework/XPCServices/com.apple.WebKit.WebContent.Crashy.xpc/com.apple.WebKit.WebContent.Crashy](MACHOS/com.apple.WebKit.WebContent.Crashy.md)
- [/System/Library/Frameworks/WebKit.framework/XPCServices/com.apple.WebKit.WebContent.xpc/com.apple.WebKit.WebContent](MACHOS/com.apple.WebKit.WebContent.md)
- [/System/Library/HIDPlugins/ServicePlugins/HSTouchHIDService.plugin/HSTouchHIDService](MACHOS/HSTouchHIDService.md)
- [/System/Library/Messages/iMessageApps/SafetyMonitorMessages.bundle/SafetyMonitorMessages](MACHOS/SafetyMonitorMessages.md)
- [/System/Library/Messages/iMessageBalloons/ASMessagesProvider.bundle/ASMessagesProvider](MACHOS/ASMessagesProvider.md)
- [/System/Library/Messages/iMessageBalloons/MSMessageExtensionBalloonPlugin.bundle/MSMessageExtensionBalloonPlugin](MACHOS/MSMessageExtensionBalloonPlugin.md)
- [/System/Library/Messages/iMessageEffects/CKConfettiEffect.bundle/CKConfettiEffect](MACHOS/CKConfettiEffect.md)
- [/System/Library/Messages/iMessageEffects/CKEchoEffect.bundle/CKEchoEffect](MACHOS/CKEchoEffect.md)
- [/System/Library/Messages/iMessageEffects/CKFireworksEffect.bundle/CKFireworksEffect](MACHOS/CKFireworksEffect.md)
- [/System/Library/Messages/iMessageEffects/CKHappyBirthdayEffect.bundle/CKHappyBirthdayEffect](MACHOS/CKHappyBirthdayEffect.md)
- [/System/Library/Messages/iMessageEffects/CKHeartEffect.bundle/CKHeartEffect](MACHOS/CKHeartEffect.md)
- [/System/Library/Messages/iMessageEffects/CKLasersEffect.bundle/CKLasersEffect](MACHOS/CKLasersEffect.md)
- [/System/Library/Messages/iMessageEffects/CKShootingStarEffect.bundle/CKShootingStarEffect](MACHOS/CKShootingStarEffect.md)
- [/System/Library/Messages/iMessageEffects/CKSparklesEffect.bundle/CKSparklesEffect](MACHOS/CKSparklesEffect.md)
- [/System/Library/Messages/iMessageEffects/CKSpotlightEffect.bundle/CKSpotlightEffect](MACHOS/CKSpotlightEffect.md)
- [/System/Library/NanoPreferenceBundles/Applications/MessagesBridgeSettings.bundle/MessagesBridgeSettings](MACHOS/MessagesBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/Discover/AppsForYourWatchPlugin.bundle/AppsForYourWatchPlugin](MACHOS/AppsForYourWatchPlugin.md)
- [/System/Library/NanoPreferenceBundles/Discover/CustomizeYourWatchPlugin.bundle/CustomizeYourWatchPlugin](MACHOS/CustomizeYourWatchPlugin.md)
- [/System/Library/NanoPreferenceBundles/Discover/GetToKnowCurrentSeriesPlugin.bundle/GetToKnowCurrentSeriesPlugin](MACHOS/GetToKnowCurrentSeriesPlugin.md)
- [/System/Library/NanoPreferenceBundles/Discover/HealthAndFitnessPlugin.bundle/HealthAndFitnessPlugin](MACHOS/HealthAndFitnessPlugin.md)
- [/System/Library/NanoPreferenceBundles/Discover/UserGuidePlugin.bundle/UserGuidePlugin](MACHOS/UserGuidePlugin.md)
- [/System/Library/NanoPreferenceBundles/Discover/WelcomeToAppleWatchPlugin.bundle/WelcomeToAppleWatchPlugin](MACHOS/WelcomeToAppleWatchPlugin.md)
- [/System/Library/NanoPreferenceBundles/Discover/WhatsNewPlugin.bundle/WhatsNewPlugin](MACHOS/WhatsNewPlugin.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/BPSStingSetup.bundle/BPSStingSetup](MACHOS/BPSStingSetup.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/MessagesPairingRegistration.bundle/MessagesPairingRegistration](MACHOS/MessagesPairingRegistration.md)
- [/System/Library/PreferenceBundles/AccountSettings/ActiveSyncSettings.bundle/ActiveSyncSettings](MACHOS/ActiveSyncSettings.md)
- [/System/Library/PreferenceBundles/AppleEthernetSettingsPreferences.bundle/AppleEthernetSettingsPreferences](MACHOS/AppleEthernetSettingsPreferences.md)
- [/System/Library/PreferenceBundles/BlocklistSettings.bundle/BlocklistSettings](MACHOS/BlocklistSettings.md)
- [/System/Library/PreferenceBundles/CallDirectorySettings.bundle/CallDirectorySettings](MACHOS/CallDirectorySettings.md)
- [/System/Library/PreferenceBundles/CallScreeningSettingsBundle.bundle/CallScreeningSettingsBundle](MACHOS/CallScreeningSettingsBundle.md)
- [/System/Library/PreferenceBundles/CoreRoutineSettings.bundle/CoreRoutineSettings](MACHOS/CoreRoutineSettings.md)
- [/System/Library/PreferenceBundles/ENDeveloperSettings.bundle/ENDeveloperSettings](MACHOS/ENDeveloperSettings.md)
- [/System/Library/PreferenceBundles/ICBSettingsBundle.bundle/ICBSettingsBundle](MACHOS/ICBSettingsBundle.md)
- [/System/Library/PreferenceBundles/ICSSettingsBundle.bundle/ICSSettingsBundle](MACHOS/ICSSettingsBundle.md)
- [/System/Library/PreferenceBundles/MessagesNotificationFiltering.bundle/MessagesNotificationFiltering](MACHOS/MessagesNotificationFiltering.md)
- [/System/Library/PreferenceBundles/MobileSafariSettings.bundle/MobileSafariSettings](MACHOS/MobileSafariSettings.md)
- [/System/Library/PreferenceBundles/MusicSettings.bundle/MusicSettings](MACHOS/MusicSettings.md)
- [/System/Library/PreferenceBundles/PrimaryCloudCallingSettingsBundle.bundle/PrimaryCloudCallingSettingsBundle](MACHOS/PrimaryCloudCallingSettingsBundle.md)
- [/System/Library/PreferenceBundles/ReplyWithMessageSettings.bundle/ReplyWithMessageSettings](MACHOS/ReplyWithMessageSettings.md)
- [/System/Library/PreferenceBundles/SIMSettings.bundle/SIMSettings](MACHOS/SIMSettings.md)
- [/System/Library/PreferenceBundles/ScreenTimeSettings.bundle/ScreenTimeSettings](MACHOS/ScreenTimeSettings.md)
- [/System/Library/PreferenceBundles/SecondaryCloudCallingSettingsBundle.bundle/SecondaryCloudCallingSettingsBundle](MACHOS/SecondaryCloudCallingSettingsBundle.md)
- [/System/Library/PreferenceBundles/SharePlaySettings.bundle/SharePlaySettings](MACHOS/SharePlaySettings.md)
- [/System/Library/PreferenceBundles/SilenceCallsSettingBundle.bundle/SilenceCallsSettingBundle](MACHOS/SilenceCallsSettingBundle.md)
- [/System/Library/PreferenceBundles/SiriMessagesSettings.bundle/SiriMessagesSettings](MACHOS/SiriMessagesSettings.md)
- [/System/Library/PreferenceBundles/StoragePlugins/CKStoragePlugin.bundle/CKStoragePlugin](MACHOS/CKStoragePlugin.md)
- [/System/Library/PreferenceManifests/ScreenTimeSettingsSearch.bundle/ScreenTimeSettingsSearch](MACHOS/ScreenTimeSettingsSearch.md)
- [/System/Library/PreferencesSyncBundles/ScreenTimePreferencesSyncCompanion.bundle/ScreenTimePreferencesSyncCompanion](MACHOS/ScreenTimePreferencesSyncCompanion.md)
- [/System/Library/PrivateFrameworks/AppleCredentialManager.framework/AppleCredentialManagerDaemon](MACHOS/AppleCredentialManagerDaemon.md)
- [/System/Library/PrivateFrameworks/AvatarUI.framework/PlugIns/AvatarPosterExtension.appex/AvatarPosterExtension](MACHOS/AvatarPosterExtension.md)
- [/System/Library/PrivateFrameworks/CMCapture.framework/PlugIns/CMCaptureDiagnosticExtension.appex/CMCaptureDiagnosticExtension](MACHOS/CMCaptureDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/CallHistory.framework/Support/CallHistorySyncHelper](MACHOS/CallHistorySyncHelper.md)
- [/System/Library/PrivateFrameworks/ChatKit.framework/companionmessagesd](MACHOS/companionmessagesd.md)
- [/System/Library/PrivateFrameworks/CoreAccessories.framework/Support/accessoryd](MACHOS/accessoryd.md)
- [/System/Library/PrivateFrameworks/CoreAccessories.framework/XPCServices/ACCAppLinksIconService.xpc/ACCAppLinksIconService](MACHOS/ACCAppLinksIconService.md)
- [/System/Library/PrivateFrameworks/CoreBluetoothUI.framework/PlugIns/BTDevicePickerUI.appex/BTDevicePickerUI](MACHOS/BTDevicePickerUI.md)
- [/System/Library/PrivateFrameworks/DiskImages2.framework/XPCServices/diskimagescontroller.xpc/diskimagescontroller](MACHOS/diskimagescontroller.md)
- [/System/Library/PrivateFrameworks/ExchangeSync.framework/Frameworks/DAEAS.framework/DADaemonEAS.bundle/DADaemonEAS](MACHOS/DADaemonEAS.md)
- [/System/Library/PrivateFrameworks/ExchangeSync.framework/Support/exchangesyncd](MACHOS/exchangesyncd.md)
- [/System/Library/PrivateFrameworks/ExchangeSyncExpress.framework/PlugIns/ActiveSyncOAuthService.appex/ActiveSyncOAuthService](MACHOS/ActiveSyncOAuthService.md)
- [/System/Library/PrivateFrameworks/FaceTimeMessageStore.framework/facetimemessagestored](MACHOS/facetimemessagestored.md)
- [/System/Library/PrivateFrameworks/FamilyCircleUI.framework/PlugIns/FAFollowupExtension.appex/FAFollowupExtension](MACHOS/FAFollowupExtension.md)
- [/System/Library/PrivateFrameworks/IAP.framework/Support/iap2d](MACHOS/iap2d.md)
- [/System/Library/PrivateFrameworks/IAP.framework/Support/iapd](MACHOS/iapd.md)
- [/System/Library/PrivateFrameworks/IAP.framework/Support/iaptransportd](MACHOS/iaptransportd.md)
- [/System/Library/PrivateFrameworks/IAPAuthentication.framework/Support/iapauthd](MACHOS/iapauthd.md)
- [/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/imagent](MACHOS/imagent.md)
- [/System/Library/PrivateFrameworks/IMDMessageServices.framework/XPCServices/IMDMessageServicesAgent.xpc/IMDMessageServicesAgent](MACHOS/IMDMessageServicesAgent.md)
- [/System/Library/PrivateFrameworks/IMDPersistence.framework/IMAutomaticHistoryDeletionAgent.app/IMAutomaticHistoryDeletionAgent](MACHOS/IMAutomaticHistoryDeletionAgent.md)
- [/System/Library/PrivateFrameworks/IMDPersistence.framework/XPCServices/IMDPersistenceAgent.xpc/IMDPersistenceAgent](MACHOS/IMDPersistenceAgent.md)
- [/System/Library/PrivateFrameworks/IMTranscoding.framework/XPCServices/IMTranscoderAgent.xpc/IMTranscoderAgent](MACHOS/IMTranscoderAgent.md)
- [/System/Library/PrivateFrameworks/IMTransferServices.framework/IMTransferAgent.app/IMTransferAgent](MACHOS/IMTransferAgent.md)
- [/System/Library/PrivateFrameworks/LockdownMode.framework/lockdownmoded](MACHOS/lockdownmoded.md)
- [/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/Support/softwareupdated](MACHOS/softwareupdated.md)
- [/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/PlugIns/NewDeviceOutreachExtension.appex/NewDeviceOutreachExtension](MACHOS/NewDeviceOutreachExtension.md)
- [/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/ndoagent](MACHOS/ndoagent.md)
- [/System/Library/PrivateFrameworks/PBBridgeSupport.framework/PlugIns/BridgeIntents.appex/BridgeIntents](MACHOS/BridgeIntents.md)
- [/System/Library/PrivateFrameworks/PairingProximity.framework/XPCServices/com.apple.Bridge.ppNotifierService.xpc/com.apple.Bridge.ppNotifierService](MACHOS/com.apple.Bridge.ppNotifierService.md)
- [/System/Library/PrivateFrameworks/People.framework/peopled](MACHOS/peopled.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/ASConfigurationSubscriber.xpc/ASConfigurationSubscriber](MACHOS/ASConfigurationSubscriber.md)
- [/System/Library/PrivateFrameworks/SafariFoundation.framework/XPCServices/AutoFillHelper.xpc/AutoFillHelper](MACHOS/AutoFillHelper.md)
- [/System/Library/PrivateFrameworks/SafariFoundation.framework/XPCServices/CredentialProviderExtensionHelper.xpc/CredentialProviderExtensionHelper](MACHOS/CredentialProviderExtensionHelper.md)
- [/System/Library/PrivateFrameworks/SafariSafeBrowsing.framework/com.apple.Safari.SafeBrowsing.Service](MACHOS/com.apple.Safari.SafeBrowsing.Service.md)
- [/System/Library/PrivateFrameworks/SafariShared.framework/XPCServices/com.apple.Safari.SearchHelper.xpc/com.apple.Safari.SearchHelper](MACHOS/com.apple.Safari.SearchHelper.md)
- [/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeAgent](MACHOS/ScreenTimeAgent.md)
- [/System/Library/PrivateFrameworks/ScreenTimeUI.framework/Extensions/ScreenTimeReportExtension.appex/ScreenTimeReportExtension](MACHOS/ScreenTimeReportExtension.md)
- [/System/Library/PrivateFrameworks/ScreenTimeUI.framework/PlugIns/ScreenTimeNotificationContentExtension.appex/ScreenTimeNotificationContentExtension](MACHOS/ScreenTimeNotificationContentExtension.md)
- [/System/Library/PrivateFrameworks/SetupAssistant.framework/budd](MACHOS/budd.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/PlugIns/PhoneIntentHandler.appex/PhoneIntentHandler](MACHOS/PhoneIntentHandler.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/XPCServices/com.apple.FTLivePhotoService.xpc/com.apple.FTLivePhotoService](MACHOS/com.apple.FTLivePhotoService.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd](MACHOS/callservicesd.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/Artwork.bundle/Artwork](MACHOS/Artwork.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/BoundingPathData.bundle/BoundingPathData](MACHOS/BoundingPathData.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/CarPlayArtwork.bundle/CarPlayArtwork](MACHOS/CarPlayArtwork.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/TextEffectsCatalog.bundle/TextEffectsCatalog](MACHOS/TextEffectsCatalog.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/XPCServices/SecureControlService.xpc/SecureControlService](MACHOS/SecureControlService.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/XPCServices/com.apple.UIKit.KeyboardManagement.xpc/com.apple.UIKit.KeyboardManagement](MACHOS/com.apple.UIKit.KeyboardManagement.md)
- [/System/Library/PrivateFrameworks/iCloudQuota.framework/PlugIns/ICQFollowup.appex/ICQFollowup](MACHOS/ICQFollowup.md)
- [/System/Library/PrivateFrameworks/iCloudQuotaUI.framework/Extensions/RemoteiCloudQuotaUI.appex/RemoteiCloudQuotaUI](MACHOS/RemoteiCloudQuotaUI.md)
- [/System/Library/PrivateFrameworks/iOSDiagnostics.framework/iosdiagnosticsd](MACHOS/iosdiagnosticsd.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriMessagesSuggestions.bundle/SiriMessagesSuggestions](MACHOS/SiriMessagesSuggestions.md)
- [/System/Library/Snippets/UIPlugins/MessagesUIPlugin.bundle/MessagesUIPlugin](MACHOS/MessagesUIPlugin.md)
- [/System/Library/SyncBundles/SMS.syncBundle/SMS](MACHOS/SMS.md)
- [/System/Library/TextInput/Plugins/MessagesDataKeyboardPlugin.bundle/MessagesDataKeyboardPlugin](MACHOS/MessagesDataKeyboardPlugin.md)
- [/System/Library/UsageBundles/ContactsUsage.bundle/ContactsUsage](MACHOS/ContactsUsage.md)
- [/System/Library/UsageBundles/MessagesUsagePreferencesPlugin.bundle/MessagesUsagePreferencesPlugin](MACHOS/MessagesUsagePreferencesPlugin.md)
- [/System/Library/UsageBundles/MusicUsage.bundle/MusicUsage](MACHOS/MusicUsage.md)
- [/System/Library/UsageBundles/SafariUsageBundle.bundle/SafariUsageBundle](MACHOS/SafariUsageBundle.md)
- [/System/Library/UserNotifications/Bundles/com.apple.ScreenTimeDowntimeNotifications.bundle/com.apple.ScreenTimeDowntimeNotifications](MACHOS/com.apple.ScreenTimeDowntimeNotifications.md)
- [/System/Library/UserNotifications/Bundles/com.apple.ScreenTimeEnabledNotifications.bundle/com.apple.ScreenTimeEnabledNotifications](MACHOS/com.apple.ScreenTimeEnabledNotifications.md)
- [/System/Library/UserNotifications/Bundles/com.apple.ScreenTimeNotifications.bundle/com.apple.ScreenTimeNotifications](MACHOS/com.apple.ScreenTimeNotifications.md)
- [/System/Library/VideoProcessors/SemanticStyleV1.bundle/SemanticStyleV1](MACHOS/SemanticStyleV1.md)
- [/System/Library/VideoProcessors/SuperResolutionV2.bundle/SuperResolutionV2](MACHOS/SuperResolutionV2.md)
- [/System/Library/VideoProcessors/VideoDeghostingV1.bundle/VideoDeghostingV1](MACHOS/VideoDeghostingV1.md)
- [/System/Library/VideoProcessors/VideoDeghostingV2.bundle/VideoDeghostingV2](MACHOS/VideoDeghostingV2.md)
- [/System/Library/VideoProcessors/VideoStabilizationV2.bundle/VideoStabilizationV2](MACHOS/VideoStabilizationV2.md)
- [/private/var/staged_system_apps/Bridge.app/Bridge](MACHOS/Bridge.md)
- [/private/var/staged_system_apps/Bridge.app/PlugIns/GreenfieldThumbnailExtension.appex/GreenfieldThumbnailExtension](MACHOS/GreenfieldThumbnailExtension.md)
- [/private/var/staged_system_apps/Contacts.app/Contacts](MACHOS/Contacts.md)
- [/private/var/staged_system_apps/FaceTime.app/FaceTime](MACHOS/FaceTime.md)
- [/private/var/staged_system_apps/Freeform.app/Extensions/USDRendererExtension.appex/USDRendererExtension](MACHOS/USDRendererExtension.md)
- [/private/var/staged_system_apps/Freeform.app/Freeform](MACHOS/Freeform.md)
- [/private/var/staged_system_apps/Freeform.app/PlugIns/FreeformSharingExtension.appex/FreeformSharingExtension](MACHOS/FreeformSharingExtension.md)
- [/private/var/staged_system_apps/Music.app/Frameworks/MusicApplication.framework/MusicApplication](MACHOS/MusicApplication.md)
- [/private/var/staged_system_apps/Music.app/Frameworks/MusicApplication.framework/XPCServices/MusicScriptUpdateService.xpc/MusicScriptUpdateService](MACHOS/MusicScriptUpdateService.md)
- [/private/var/staged_system_apps/Music.app/Music](MACHOS/Music.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/MediaPicker.appex/MediaPicker](MACHOS/MediaPicker.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/MusicCoreSpotlightExtension.appex/MusicCoreSpotlightExtension](MACHOS/MusicCoreSpotlightExtension.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/MusicMessagesApp.appex/MusicMessagesApp](MACHOS/MusicMessagesApp.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/MusicNotificationContentExtension.appex/MusicNotificationContentExtension](MACHOS/MusicNotificationContentExtension.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/MusicWidgets.appex/MusicWidgets](MACHOS/MusicWidgets.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/StoreFlowExtension.appex/StoreFlowExtension](MACHOS/StoreFlowExtension.md)
- [/sbin/mount_nfs](MACHOS/mount_nfs.md)
- [/usr/lib/dyld](MACHOS/dyld.md)
- [/usr/lib/libSystem.B_asan.dylib](MACHOS/libSystem.B_asan.dylib.md)
- [/usr/libexec/AuthenticationServicesAgent](MACHOS/AuthenticationServicesAgent.md)
- [/usr/libexec/anomalydetectiond](MACHOS/anomalydetectiond.md)
- [/usr/libexec/asktod](MACHOS/asktod.md)
- [/usr/libexec/bluetoothuserd](MACHOS/bluetoothuserd.md)
- [/usr/libexec/com.apple.Safari.History](MACHOS/com.apple.Safari.History.md)
- [/usr/libexec/continuitycaptured](MACHOS/continuitycaptured.md)
- [/usr/libexec/deferredmediad](MACHOS/deferredmediad.md)
- [/usr/libexec/diskimagesiod](MACHOS/diskimagesiod.md)
- [/usr/libexec/locationd](MACHOS/locationd.md)
- [/usr/libexec/locationpushd](MACHOS/locationpushd.md)
- [/usr/libexec/mobilerepaird](MACHOS/mobilerepaird.md)
- [/usr/libexec/nearbyd](MACHOS/nearbyd.md)
- [/usr/libexec/passwordbreachd](MACHOS/passwordbreachd.md)
- [/usr/libexec/powerdatad](MACHOS/powerdatad.md)
- [/usr/libexec/routined](MACHOS/routined.md)
- [/usr/libexec/safarifetcherd](MACHOS/safarifetcherd.md)
- [/usr/libexec/softposreaderd](MACHOS/softposreaderd.md)
- [/usr/libexec/webbookmarksd](MACHOS/webbookmarksd.md)
- [/usr/libexec/webinspectord](MACHOS/webinspectord.md)
- [/usr/libexec/webpushd](MACHOS/webpushd.md)
- [/usr/sbin/BlueTool](MACHOS/BlueTool.md)
- [/usr/sbin/bluetoothd](MACHOS/bluetoothd.md)
- [/usr/sbin/wifid](MACHOS/wifid.md)

</details>

## Firmware

### ⬆️ Updated (4)

<details>
  <summary><i>View Updated</i></summary>

#### agx_a000

>  `agx_a000`

```diff

   __DATA.__mod_init_func: 0x0
   __DATA._rtk_heap: 0x0
   __DATA.__zerofill: 0x666a0
-  UUID: 18FEC634-5F06-38CB-B930-C6E9D61CD65B
+  UUID: 8A6E86EC-0775-3028-BB81-A10534C8C24E
   Functions: 0
   Symbols:   197
   CStrings:  200
CStrings:
+ "Sep 30 2023 17:18:59"
- "Sep 15 2023 13:43:22"

```

#### agx_b000

>  `agx_b000`

```diff

   __DATA.__mod_init_func: 0x0
   __DATA._rtk_heap: 0x0
   __DATA.__zerofill: 0x66520
-  UUID: F5AD066F-19F9-3F93-A424-CFF074C0D844
+  UUID: 0BECB0CD-8957-36B9-89BA-6D33091A05AA
   Functions: 0
   Symbols:   197
   CStrings:  200
CStrings:
+ "Sep 30 2023 17:19:30"
- "Sep 15 2023 13:43:52"

```

#### agx_b100

>  `agx_b100`

```diff

   __DATA.__mod_init_func: 0x0
   __DATA._rtk_heap: 0x0
   __DATA.__zerofill: 0x66520
-  UUID: 1046FAE9-A814-3752-950D-62CD3B8DF17E
+  UUID: 4AC118B6-F89C-3170-BDF1-98F05B938CAA
   Functions: 0
   Symbols:   197
   CStrings:  200
CStrings:
+ "Sep 30 2023 17:20:02"
- "Sep 15 2023 13:44:23"

```

#### aopfw-iphone16aop.im4p

>  `aopfw-iphone16aop.im4p`

```diff

   __OS_LOG.__string: 0x22cd9
   __MISC.__apf_list: 0xb0
   __CMA.__cma_log_string: 0x3a50
-  UUID: 5AA37A1D-9962-33E4-B2A0-5CC79BD9E14F
+  UUID: 855F1163-D63C-3588-AB24-10E88AE2734C
   Functions: 0
   Symbols:   0
   CStrings:  3490

```


</details>

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 17.0.2 *(21A350)* | 616.1.27.10.15 |
| 17.0.3 *(21A360)* | 616.1.27.10.16 |

### Dylibs

#### ⬆️ Updated (167)

<details>
  <summary><i>View Updated</i></summary>

- [/System/Library/Accounts/Authentication/ESAccountAuthenticator.bundle/ESAccountAuthenticator](DYLIBS/ESAccountAuthenticator.md)
- [/System/Library/Accounts/Notification/ESAccountNotifier.bundle/ESAccountNotifier](DYLIBS/ESAccountNotifier.md)
- [/System/Library/Accounts/Notification/IMAccountNotificationPlugin.bundle/IMAccountNotificationPlugin](DYLIBS/IMAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/WebBookmarksNotificationPlugin.bundle/WebBookmarksNotificationPlugin](DYLIBS/WebBookmarksNotificationPlugin.md)
- [/System/Library/Assistant/Plugins/Phone.assistantBundle/Phone](DYLIBS/Phone.md)
- [/System/Library/CoreAccessories/PlugIns/Features/Communications-iOS.feature/Communications-iOS](DYLIBS/Communications-iOS.md)
- [/System/Library/DataClassMigrators/MessagesDataMigrator.migrator/MessagesDataMigrator](DYLIBS/MessagesDataMigrator.md)
- [/System/Library/DigitalSeparation/SharingSources/PasswordsDigitalSeparation.bundle/PasswordsDigitalSeparation](DYLIBS/PasswordsDigitalSeparation.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libvDSP.dylib](DYLIBS/libvDSP.dylib.md)
- [/System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices](DYLIBS/AuthenticationServices.md)
- [/System/Library/Frameworks/ContactsUI.framework/ContactsUI](DYLIBS/ContactsUI.md)
- [/System/Library/Frameworks/CoreLocation.framework/CoreLocation](DYLIBS/CoreLocation.md)
- [/System/Library/Frameworks/CoreLocationUI.framework/CoreLocationUI](DYLIBS/CoreLocationUI.md)
- [/System/Library/Frameworks/CoreMotion.framework/CoreMotion](DYLIBS/CoreMotion.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterAWDMetrics.dylib](DYLIBS/libCommCenterAWDMetrics.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterKCommandDrivers.dylib](DYLIBS/libCommCenterKCommandDrivers.dylib.md)
- [/System/Library/Frameworks/JavaScriptCore.framework/JavaScriptCore](DYLIBS/JavaScriptCore.md)
- [/System/Library/Frameworks/MapKit.framework/MapKit](DYLIBS/MapKit.md)
- [/System/Library/Frameworks/Messages.framework/Messages](DYLIBS/Messages.md)
- [/System/Library/Frameworks/PassKit.framework/PassKit](DYLIBS/PassKit.md)
- [/System/Library/Frameworks/ProximityReader.framework/ProximityReader](DYLIBS/ProximityReader.md)
- [/System/Library/Frameworks/SafariServices.framework/SafariServices](DYLIBS/SafariServices.md)
- [/System/Library/Frameworks/ScreenTime.framework/ScreenTime](DYLIBS/ScreenTime.md)
- [/System/Library/Frameworks/UIKit.framework/UIKit](DYLIBS/UIKit.md)
- [/System/Library/Frameworks/WebKit.framework/WebKit](DYLIBS/WebKit.md)
- [/System/Library/Frameworks/_AuthenticationServices_SwiftUI.framework/_AuthenticationServices_SwiftUI](DYLIBS/_AuthenticationServices_SwiftUI.md)
- [/System/Library/Frameworks/_CoreLocationUI_SwiftUI.framework/_CoreLocationUI_SwiftUI](DYLIBS/_CoreLocationUI_SwiftUI.md)
- [/System/Library/Frameworks/_MapKit_SwiftUI.framework/_MapKit_SwiftUI](DYLIBS/_MapKit_SwiftUI.md)
- [/System/Library/Messages/PlugIns/FaceTime.imservice/FaceTime](DYLIBS/FaceTime.md)
- [/System/Library/Messages/PlugIns/SMS.imservice/SMS](DYLIBS/SMS.md)
- [/System/Library/Messages/PlugIns/iMessage.imservice/iMessage](DYLIBS/iMessage.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/MessagesComplication.bundle/MessagesComplication](DYLIBS/MessagesComplication.md)
- [/System/Library/PreferenceBundles/CarrierSettings.bundle/CarrierSettings](DYLIBS/CarrierSettings.md)
- [/System/Library/PreferenceBundles/ContactsSettings.bundle/ContactsSettings](DYLIBS/ContactsSettings.md)
- [/System/Library/PreferenceBundles/MobilePhoneSettings.bundle/MobilePhoneSettings](DYLIBS/MobilePhoneSettings.md)
- [/System/Library/PrivateFrameworks/AGXCompilerConnection-S2A8.framework/AGXCompilerConnection-S2A8](DYLIBS/AGXCompilerConnection-S2A8.md)
- [/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture](DYLIBS/AVFCapture.md)
- [/System/Library/PrivateFrameworks/AppStoreKit.framework/AppStoreKit](DYLIBS/AppStoreKit.md)
- [/System/Library/PrivateFrameworks/AppStoreKitInternal.framework/AppStoreKitInternal](DYLIBS/AppStoreKitInternal.md)
- [/System/Library/PrivateFrameworks/AppleConvergedFirmwareUpdater.framework/AppleConvergedFirmwareUpdater](DYLIBS/AppleConvergedFirmwareUpdater.md)
- [/System/Library/PrivateFrameworks/AppleIDSetup.framework/AppleIDSetup](DYLIBS/AppleIDSetup.md)
- [/System/Library/PrivateFrameworks/AppleIDSetupUI.framework/AppleIDSetupUI](DYLIBS/AppleIDSetupUI.md)
- [/System/Library/PrivateFrameworks/AuthenticationServicesCore.framework/AuthenticationServicesCore](DYLIBS/AuthenticationServicesCore.md)
- [/System/Library/PrivateFrameworks/AvatarPoster.framework/AvatarPoster](DYLIBS/AvatarPoster.md)
- [/System/Library/PrivateFrameworks/AvatarUI.framework/AvatarUI](DYLIBS/AvatarUI.md)
- [/System/Library/PrivateFrameworks/BridgeCommons.framework/BridgeCommons](DYLIBS/BridgeCommons.md)
- [/System/Library/PrivateFrameworks/BridgePreferences.framework/BridgePreferences](DYLIBS/BridgePreferences.md)
- [/System/Library/PrivateFrameworks/BridgeReporting.framework/BridgeReporting](DYLIBS/BridgeReporting.md)
- [/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture](DYLIBS/CMCapture.md)
- [/System/Library/PrivateFrameworks/CMCaptureCore.framework/CMCaptureCore](DYLIBS/CMCaptureCore.md)
- [/System/Library/PrivateFrameworks/CMContinuityCaptureCore.framework/CMContinuityCaptureCore](DYLIBS/CMContinuityCaptureCore.md)
- [/System/Library/PrivateFrameworks/CMImaging.framework/CMImaging](DYLIBS/CMImaging.md)
- [/System/Library/PrivateFrameworks/CallHistory.framework/CallHistory](DYLIBS/CallHistory.md)
- [/System/Library/PrivateFrameworks/ChatKit.framework/ChatKit](DYLIBS/ChatKit.md)
- [/System/Library/PrivateFrameworks/CinematicFraming.framework/CinematicFraming](DYLIBS/CinematicFraming.md)
- [/System/Library/PrivateFrameworks/CollectionViewCore.framework/CollectionViewCore](DYLIBS/CollectionViewCore.md)
- [/System/Library/PrivateFrameworks/CommunicationsSetupUI.framework/CommunicationsSetupUI](DYLIBS/CommunicationsSetupUI.md)
- [/System/Library/PrivateFrameworks/ContactlessReaderUI.framework/ContactlessReaderUI](DYLIBS/ContactlessReaderUI.md)
- [/System/Library/PrivateFrameworks/ContactsWidgetUI.framework/ContactsWidgetUI](DYLIBS/ContactsWidgetUI.md)
- [/System/Library/PrivateFrameworks/ContainerManagerCommon.framework/ContainerManagerCommon](DYLIBS/ContainerManagerCommon.md)
- [/System/Library/PrivateFrameworks/CoreBluetoothUI.framework/CoreBluetoothUI](DYLIBS/CoreBluetoothUI.md)
- [/System/Library/PrivateFrameworks/CoreRepairUI.framework/CoreRepairUI](DYLIBS/CoreRepairUI.md)
- [/System/Library/PrivateFrameworks/DAEASOAuthFramework.framework/DAEASOAuthFramework](DYLIBS/DAEASOAuthFramework.md)
- [/System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport](DYLIBS/DiagnosticsSupport.md)
- [/System/Library/PrivateFrameworks/DiskImages2.framework/DiskImages2](DYLIBS/DiskImages2.md)
- [/System/Library/PrivateFrameworks/ExchangeSync.framework/ExchangeSync](DYLIBS/ExchangeSync.md)
- [/System/Library/PrivateFrameworks/ExchangeSync.framework/Frameworks/DAEAS.framework/DAEAS](DYLIBS/DAEAS.md)
- [/System/Library/PrivateFrameworks/ExchangeSync.framework/Frameworks/ESDaemonSupport.framework/ESDaemonSupport](DYLIBS/ESDaemonSupport.md)
- [/System/Library/PrivateFrameworks/ExchangeSyncExpress.framework/ExchangeSyncExpress](DYLIBS/ExchangeSyncExpress.md)
- [/System/Library/PrivateFrameworks/FamilyCircleUI.framework/FamilyCircleUI](DYLIBS/FamilyCircleUI.md)
- [/System/Library/PrivateFrameworks/IMAssistantCore.framework/IMAssistantCore](DYLIBS/IMAssistantCore.md)
- [/System/Library/PrivateFrameworks/IMCore.framework/IMCore](DYLIBS/IMCore.md)
- [/System/Library/PrivateFrameworks/IMCorePipeline.framework/IMCorePipeline](DYLIBS/IMCorePipeline.md)
- [/System/Library/PrivateFrameworks/IMDMessageServices.framework/IMDMessageServices](DYLIBS/IMDMessageServices.md)
- [/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence](DYLIBS/IMDPersistence.md)
- [/System/Library/PrivateFrameworks/IMDaemonCore.framework/IMDaemonCore](DYLIBS/IMDaemonCore.md)
- [/System/Library/PrivateFrameworks/IMSharedUI.framework/IMSharedUI](DYLIBS/IMSharedUI.md)
- [/System/Library/PrivateFrameworks/IMSharedUtilities.framework/IMSharedUtilities](DYLIBS/IMSharedUtilities.md)
- [/System/Library/PrivateFrameworks/IMTranscoderAgent.framework/IMTranscoderAgent](DYLIBS/IMTranscoderAgent.md)
- [/System/Library/PrivateFrameworks/IMTranscoding.framework/IMTranscoding](DYLIBS/IMTranscoding.md)
- [/System/Library/PrivateFrameworks/IMTransferAgent.framework/IMTransferAgent](DYLIBS/IMTransferAgent.md)
- [/System/Library/PrivateFrameworks/IPTelephony.framework/Support/libIPTelephony.dylib](DYLIBS/libIPTelephony.dylib.md)
- [/System/Library/PrivateFrameworks/KeyboardArbiter.framework/KeyboardArbiter](DYLIBS/KeyboardArbiter.md)
- [/System/Library/PrivateFrameworks/MMCSServices.framework/MMCSServices](DYLIBS/MMCSServices.md)
- [/System/Library/PrivateFrameworks/MessagesCloudSync.framework/MessagesCloudSync](DYLIBS/MessagesCloudSync.md)
- [/System/Library/PrivateFrameworks/MessagesSupport.framework/MessagesSupport](DYLIBS/MessagesSupport.md)
- [/System/Library/PrivateFrameworks/MobileSafari.framework/MobileSafari](DYLIBS/MobileSafari.md)
- [/System/Library/PrivateFrameworks/MobileSafari.framework/PlugIns/Safari.wkbundle/Safari](DYLIBS/Safari.md)
- [/System/Library/PrivateFrameworks/MobileSafariSwift.framework/MobileSafariSwift](DYLIBS/MobileSafariSwift.md)
- [/System/Library/PrivateFrameworks/MobileSafariUI.framework/MobileSafariUI](DYLIBS/MobileSafariUI.md)
- [/System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi](DYLIBS/MobileWiFi.md)
- [/System/Library/PrivateFrameworks/MonogramPoster.framework/MonogramPoster](DYLIBS/MonogramPoster.md)
- [/System/Library/PrivateFrameworks/MusicCarDisplayUI.framework/MusicCarDisplayUI](DYLIBS/MusicCarDisplayUI.md)
- [/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/NewDeviceOutreach](DYLIBS/NewDeviceOutreach.md)
- [/System/Library/PrivateFrameworks/NewDeviceOutreachUI.framework/NewDeviceOutreachUI](DYLIBS/NewDeviceOutreachUI.md)
- [/System/Library/PrivateFrameworks/PBBridgeSupport.framework/PBBridgeSupport](DYLIBS/PBBridgeSupport.md)
- [/System/Library/PrivateFrameworks/PairingProximity.framework/PairingProximity](DYLIBS/PairingProximity.md)
- [/System/Library/PrivateFrameworks/PasswordManagerUI.framework/PasswordManagerUI](DYLIBS/PasswordManagerUI.md)
- [/System/Library/PrivateFrameworks/People.framework/People](DYLIBS/People.md)
- [/System/Library/PrivateFrameworks/PeopleUI.framework/PeopleUI](DYLIBS/PeopleUI.md)
- [/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators](DYLIBS/PowerlogLiteOperators.md)
- [/System/Library/PrivateFrameworks/ProximityAppleIDSetup.framework/ProximityAppleIDSetup](DYLIBS/ProximityAppleIDSetup.md)
- [/System/Library/PrivateFrameworks/ProximityAppleIDSetupUI.framework/ProximityAppleIDSetupUI](DYLIBS/ProximityAppleIDSetupUI.md)
- [/System/Library/PrivateFrameworks/SafariCore.framework/SafariCore](DYLIBS/SafariCore.md)
- [/System/Library/PrivateFrameworks/SafariFoundation.framework/SafariFoundation](DYLIBS/SafariFoundation.md)
- [/System/Library/PrivateFrameworks/SafariSafeBrowsing.framework/SafariSafeBrowsing](DYLIBS/SafariSafeBrowsing.md)
- [/System/Library/PrivateFrameworks/SafariShared.framework/SafariShared](DYLIBS/SafariShared.md)
- [/System/Library/PrivateFrameworks/SafariSharedUI.framework/SafariSharedUI](DYLIBS/SafariSharedUI.md)
- [/System/Library/PrivateFrameworks/SafetyMonitor.framework/SafetyMonitor](DYLIBS/SafetyMonitor.md)
- [/System/Library/PrivateFrameworks/SafetyMonitorUI.framework/SafetyMonitorUI](DYLIBS/SafetyMonitorUI.md)
- [/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore](DYLIBS/ScreenTimeCore.md)
- [/System/Library/PrivateFrameworks/ScreenTimeSettingsUI.framework/ScreenTimeSettingsUI](DYLIBS/ScreenTimeSettingsUI.md)
- [/System/Library/PrivateFrameworks/ScreenTimeSwift.framework/ScreenTimeSwift](DYLIBS/ScreenTimeSwift.md)
- [/System/Library/PrivateFrameworks/ScreenTimeUI.framework/ScreenTimeUI](DYLIBS/ScreenTimeUI.md)
- [/System/Library/PrivateFrameworks/ScreenTimeUICore.framework/ScreenTimeUICore](DYLIBS/ScreenTimeUICore.md)
- [/System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant](DYLIBS/SetupAssistant.md)
- [/System/Library/PrivateFrameworks/SetupAssistantUI.framework/SetupAssistantUI](DYLIBS/SetupAssistantUI.md)
- [/System/Library/PrivateFrameworks/StickersUI.framework/StickersUI](DYLIBS/StickersUI.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore](DYLIBS/UIKitCore.md)
- [/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices](DYLIBS/UIKitServices.md)
- [/System/Library/PrivateFrameworks/WPDaemon.framework/WPDaemon](DYLIBS/WPDaemon.md)
- [/System/Library/PrivateFrameworks/WebApp.framework/WebApp](DYLIBS/WebApp.md)
- [/System/Library/PrivateFrameworks/WebBookmarks.framework/WebBookmarks](DYLIBS/WebBookmarks.md)
- [/System/Library/PrivateFrameworks/WebBookmarksSwift.framework/WebBookmarksSwift](DYLIBS/WebBookmarksSwift.md)
- [/System/Library/PrivateFrameworks/WebCore.framework/Frameworks/libANGLE-shared.dylib](DYLIBS/libANGLE-shared.dylib.md)
- [/System/Library/PrivateFrameworks/WebCore.framework/Frameworks/libwebrtc.dylib](DYLIBS/libwebrtc.dylib.md)
- [/System/Library/PrivateFrameworks/WebCore.framework/WebCore](DYLIBS/WebCore.md)
- [/System/Library/PrivateFrameworks/WebGPU.framework/WebGPU](DYLIBS/WebGPU.md)
- [/System/Library/PrivateFrameworks/WebInspector.framework/WebInspector](DYLIBS/WebInspector.md)
- [/System/Library/PrivateFrameworks/WebKitLegacy.framework/WebKitLegacy](DYLIBS/WebKitLegacy.md)
- [/System/Library/PrivateFrameworks/WebUI.framework/WebUI](DYLIBS/WebUI.md)
- [/System/Library/PrivateFrameworks/iCloudQuota.framework/iCloudQuota](DYLIBS/iCloudQuota.md)
- [/System/Library/PrivateFrameworks/iCloudQuotaUI.framework/iCloudQuotaUI](DYLIBS/iCloudQuotaUI.md)
- [/System/Library/PrivateFrameworks/iMessageApps.framework/iMessageApps](DYLIBS/iMessageApps.md)
- [/System/Library/PrivateFrameworks/iOSDiagnostics.framework/iOSDiagnostics](DYLIBS/iOSDiagnostics.md)
- [/System/Library/VideoDecoders/AVD.videodecoder](DYLIBS/AVD.videodecoder.md)
- [/System/Library/VideoDecoders/H264H8.videodecoder](DYLIBS/H264H8.videodecoder.md)
- [/System/Library/VideoDecoders/MP4VH8.videodecoder](DYLIBS/MP4VH8.videodecoder.md)
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
- [/usr/lib/dyld](DYLIBS/dyld.md)
- [/usr/lib/libBBUpdaterDynamic.dylib](DYLIBS/libBBUpdaterDynamic.dylib.md)
- [/usr/lib/libHSFilerDynamic.dylib](DYLIBS/libHSFilerDynamic.dylib.md)
- [/usr/lib/libKTLDynamic.dylib](DYLIBS/libKTLDynamic.dylib.md)
- [/usr/lib/libRoseBooter.dylib](DYLIBS/libRoseBooter.dylib.md)
- [/usr/lib/libSystem.B.dylib](DYLIBS/libSystem.B.dylib.md)
- [/usr/lib/libauthinstall.dylib](DYLIBS/libauthinstall.dylib.md)
- [/usr/lib/libcoreroutine.dylib](DYLIBS/libcoreroutine.dylib.md)
- [/usr/lib/libsandbox.1.dylib](DYLIBS/libsandbox.1.dylib.md)
- [/usr/lib/swift/libswiftUIKit.dylib](DYLIBS/libswiftUIKit.dylib.md)
- [/usr/lib/swift/libswiftWebKit.dylib](DYLIBS/libswiftWebKit.dylib.md)
- [/usr/lib/system/libsystem_kernel.dylib](DYLIBS/libsystem_kernel.dylib.md)
- [/usr/lib/system/libsystem_pthread.dylib](DYLIBS/libsystem_pthread.dylib.md)
- [/usr/lib/system/libsystem_sandbox.dylib](DYLIBS/libsystem_sandbox.dylib.md)
- [/usr/lib/updaters/libRoseUpdater.dylib](DYLIBS/libRoseUpdater.dylib.md)
- [/usr/lib/updaters/libVinylUpdater.dylib](DYLIBS/libVinylUpdater.dylib.md)

</details>

## Files

### 🆕 New

#### filesystem (1)

- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/en_US.7b18de982fa7faef761688d505eed072.version`

### ❌ Removed

#### filesystem (1)

- `/private/var/staged_system_apps/Freeform.app/Metadata.appintents/nlu/en_US.f04a5e45e2bdf03a05f90e3980f13d9f.version`

## EOF
