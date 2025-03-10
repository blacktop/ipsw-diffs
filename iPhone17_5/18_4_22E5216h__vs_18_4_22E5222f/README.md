# 18.4 (22E5216h) .vs 18.4 (22E5222f)

## IPSWs

- `iPhone17,5_18.4_22E5216h_Restore.ipsw`
- `iPhone17,5_18.4_22E5222f_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 18.4 *(22E5216h)* | 24.4.0 | 11417.100.564.502.1~1 | Tue, 25Feb2025 21:30:30 PST |
| 18.4 *(22E5222f)* | 24.4.0 | 11417.100.576.502.2~1 | Tue, 04Mar2025 21:48:46 PST |

### Kexts

#### ⬆️ Updated (25)

<details>
  <summary><i>View Updated</i></summary>

>  `com.apple.AGXG17P`

```diff

-325.30.0.0.0
+325.31.2.0.0
   __TEXT.__const: 0x4e5c
   __TEXT.__os_log: 0x318
   __TEXT.__cstring: 0xf38b
-  __TEXT_EXEC.__text: 0xd0ed8
+  __TEXT_EXEC.__text: 0xd0fdc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x13c0
   __DATA.__common: 0x10

   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x398
   __DATA_CONST.__mod_term_func: 0x2e0
-  __DATA_CONST.__const: 0x10530
+  __DATA_CONST.__const: 0x10540
   __DATA_CONST.__kalloc_type: 0x25c0
   __DATA_CONST.__kalloc_var: 0x32f0
-  Functions: 3039
+  Functions: 3041
   Symbols:   0
   CStrings:  1913
 
CStrings:
+ "Mar  5 2025 21:16:56"
- "Feb 25 2025 21:08:46"

```

>  `com.apple.driver.AppleAVE2`

```diff

-803.57.0.0.0
-  __TEXT.__const: 0x2ef70
-  __TEXT.__cstring: 0x35329
-  __TEXT.__os_log: 0x3ffcf
-  __TEXT_EXEC.__text: 0x14404c
+803.63.1.0.0
+  __TEXT.__const: 0x2ef60
+  __TEXT.__cstring: 0x35335
+  __TEXT.__os_log: 0x3ffe3
+  __TEXT_EXEC.__text: 0x14437c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x290
   __DATA.__common: 0x130
CStrings:
+ "%lld %d AVE %s: %s::%s:%d SKIP %p %d %lld | %d %d | %p %d %lld 0x%x %lld"
+ "%lld %d AVE %s: %s::%s:%d SKIP %p %d %lld | %d %d | %p %d %lld 0x%x %lld\n"
+ "%lld %d AVE %s: UsedByCurrPicS0[%d] %hhu"
+ "%lld %d AVE %s: UsedByCurrPicS0[%d] %hhu\n"
+ "%lld %d AVE %s: UsedByCurrPicS1[%d] %hhu"
+ "%lld %d AVE %s: UsedByCurrPicS1[%d] %hhu\n"
+ "22:27:43"
+ "803.63.1"
+ "Mar  4 2025"
- "%lld %d AVE %s: %s::%s:%d SKIP %p %d %lld | %p %d %lld 0x%x %lld"
- "%lld %d AVE %s: %s::%s:%d SKIP %p %d %lld | %p %d %lld 0x%x %lld\n"
- "%lld %d AVE %s: UsedByCurrPicS0[%d] %d"
- "%lld %d AVE %s: UsedByCurrPicS0[%d] %d\n"
- "%lld %d AVE %s: UsedByCurrPicS1[%d] %d"
- "%lld %d AVE %s: UsedByCurrPicS1[%d] %d\n"
- "21:13:54"
- "803.57.0"
- "Feb 25 2025"

```

>  `com.apple.driver.AppleC26Charger`

```diff

-85.100.9.0.0
+85.100.13.0.0
   __TEXT.__const: 0x177
-  __TEXT.__cstring: 0x1d84
+  __TEXT.__cstring: 0x1dfc
   __TEXT.__os_log: 0x51
-  __TEXT_EXEC.__text: 0x130fc
+  __TEXT_EXEC.__text: 0x131e0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x348

   __DATA_CONST.__kalloc_type: 0x500
   Functions: 540
   Symbols:   0
-  CStrings:  217
+  CStrings:  218
 
CStrings:
+ "1211121111221112112221122"
+ "AppleWirelessPowerTelegramStream:receivePacketFromController mp(%d) el(%d) il(%d) rs(%d) pdl(%d) rel(%d) rl(%d) rml(%d)\n"
- "12111211112211121122211222"

```

>  `com.apple.driver.AppleCS42L77v2Audio`

```diff

-840.25.0.0.0
+840.26.0.0.0
   __TEXT.__cstring: 0x16a2
   __TEXT.__os_log: 0x189e
   __TEXT.__const: 0x360
-  __TEXT_EXEC.__text: 0xe28c
+  __TEXT_EXEC.__text: 0xe290
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0xe8

```

>  `com.apple.driver.AppleConvergedIPCBBControl`

```diff

 198.0.0.0.0
-  __TEXT.__cstring: 0x671a
-  __TEXT.__const: 0x17ce7
-  __TEXT_EXEC.__text: 0x912f8
+  __TEXT.__cstring: 0x5732
+  __TEXT.__const: 0xa6b7
+  __TEXT_EXEC.__text: 0x5eb50
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x2e0
-  __DATA.__common: 0x7c0
-  __DATA.__bss: 0x90f0
-  __DATA_CONST.__auth_got: 0x850
-  __DATA_CONST.__got: 0x2508
-  __DATA_CONST.__mod_init_func: 0x2748
-  __DATA_CONST.__mod_term_func: 0x1c0
-  __DATA_CONST.__const: 0x2c0e0
-  __DATA_CONST.__kalloc_type: 0x1dc0
-  __DATA_CONST.__kalloc_var: 0x9b0
-  Functions: 3750
+  __DATA.__data: 0x230
+  __DATA.__common: 0x748
+  __DATA.__bss: 0x3e28
+  __DATA_CONST.__auth_got: 0x778
+  __DATA_CONST.__got: 0x10e0
+  __DATA_CONST.__mod_init_func: 0x1178
+  __DATA_CONST.__mod_term_func: 0x158
+  __DATA_CONST.__const: 0x1bc48
+  __DATA_CONST.__kalloc_type: 0x1c80
+  __DATA_CONST.__kalloc_var: 0x870
+  Functions: 2735
   Symbols:   0
-  CStrings:  681
+  CStrings:  563
 
CStrings:
+ "121111121222121211111111121121111111111111111211211211211112111121"
+ "12111112122212121111111112112111111111111111121121121121111211112112221111112222211112"
+ "1211111212221212111111111211211111111111111112112112112111121111212"
+ "12111112122212121111121112222222111122121112"
+ "12111112122212121112211111111111122222222222222222221121111122112221111111111111111111111111111111122222222111222222222222222222222122222222222222222222"
+ "12111112122212121112212111122222222211112111"
+ "1211111212221212112111111111111111222221111111112212111112"
+ "1211111212221212112111111111111111222221111111112212111112112"
+ "121111121222121212112121111211111111111111111111111111111111111111111111111111111111111111111111222222222222222222222221"
+ "1211111212221212121121211112111111111111111111111111111111111111111111111111111111111111111111112222222222222222222222212"
- "%06ld.%06d "
- "%3u"
- "%3u to %3u"
- "%3u to inf"
- "%s::%s: %d. %u\n"
- "%s::%s: %s to enable refclk gating\n"
- "%s::%s: *%p == 0x%x\n"
- "%s::%s: HMAP VSEC regs(@0x%x)= 0x%x\n"
- "%s::%s: HMAP capability not found\n"
- "%s::%s: Invalid bar Index for MSI-X: %u! skipping HMAP config for MSI-X\n"
- "%s::%s: Invalid index %d"
- "%s::%s: Link control reg: 0x%x, Link control offset: 0x%llx\n"
- "%s::%s: MSI address 0x%llx\n"
- "%s::%s: MSI or MSI-X capability not found!\n"
- "%s::%s: MSI-X bar Index: 0x%x\n"
- "%s::%s: MSI-X capability found\n"
- "%s::%s: MSI-X vector 0 address 0x%llx\n"
- "%s::%s: PCIe getLinkSpeed failed. Supported RP speed %u, Supported EP speed %u, Desired speed %u, Enumerated speed %u\n"
- "%s::%s: PCIe link speed mismatched. Supported RP speed %u, Supported EP sped %u, Desired speed %u, Enumerated speed %u\n"
- "%s::%s: VSEC ID at offset 0x%llx matched HMAP 0x%x\n"
- "%s::%s: VSEC ID at offset 0x%llx not matched HMAP. Expected 0x0024, found 0x%x\n"
- "%s::%s: bar%u %p [+0x%x], (pa: 0x%llx)\n"
- "%s::%s: bar0 %p [+0x%x], bar1 %p [+0x%x]\n"
- "%s::%s: chip revision major (%u)\n"
- "%s::%s: configured HMAP for MSI\n"
- "%s::%s: dart window range: %p --> %p\n"
- "%s::%s: db[%u]=%u\n"
- "%s::%s: endpoint pcie capability not found\n"
- "%s::%s: endpoint port PCIe capability not found\n"
- "%s::%s: failed to create/init a reporter\n"
- "%s::%s: failed to get PCIe link speed %u\n"
- "%s::%s: failed to get provider of IOPCI2PCIBridge\n"
- "%s::%s: failed to get provider of IOPCIDevice\n"
- "%s::%s: failed to map bar0\n"
- "%s::%s: failed to map bar1\n"
- "%s::%s: failed to map msi-X bar! skipping HMAP config for MSI-X!\n"
- "%s::%s: failed to start reporting\n"
- "%s::%s: root port PCIe capability not found\n"
- "+-----------------------------------------------+----------------+"
- "/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPCBaseband/AppleConvergedIPCBBControl/AppleConvergedIPCBBLogger.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPCBaseband/AppleConvergedIPCBBControl/AppleConvergedPCIBBRASReporter.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPCBaseband/AppleConvergedIPCPDP/AppleConvergedIPCPDPReporter.cpp"
- "112111111"
- "1211111212221212111111111211211111111111111111211211211211112111121"
- "121111121222121211111111121121111111111111111121121121121111211112112221111112222211112"
- "12111112122212121111111112112111111111111111112112112112111121111212"
- "121111121222121211111211122222221111221211121"
- "121111121222121211122111111111111122222222222222222221121111122112221111111111111111111111111111111122222222111222222222222222222222122222222222222222222"
- "121111121222121211122121111122222222211112111"
- "12111112122212121121111111111111112222211111111112212111112"
- "12111112122212121121111111111111112222211111111112212111112112"
- "1211111212221212121121211112111111111111111111111111111111111111111111111111111111111111111111112222222222222222222222121"
- "12111112122212121211212111121111111111111111111111111111111111111111111111111111111111111111111122222222222222222222221212"
- "1211111212221212121122222222211111112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221222212222122221222212222122221222212222122221222212222122221222212222122221222212222122221222212222122221222212222122221222212222122221222212222122221222212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222122211212"
- "12112111"
- "1211222111111111111"
- "Aggregated Block"
- "AppleBasebandPCILogger::start: failed to allocate memory for snapshot buffer\n"
- "AppleConvergedIPCBBLogger"
- "AppleConvergedIPCBBLogger.cpp"
- "AppleConvergedIPCPDPReporter"
- "AppleConvergedIPCPDPReporter.cpp"
- "AppleConvergedPCIBBRASReporter"
- "AppleConvergedPCIBBRASReporter.cpp"
- "Counters"
- "DL"
- "DL Aggregation Histogram"
- "DL Drop Counters"
- "Downlink Bytes"
- "Downlink Pkts"
- "Dropped Downlink Bytes"
- "Dropped Downlink Packets"
- "Flow Control"
- "Global"
- "Invalid Interface"
- "Link Status Notifications"
- "PDP"
- "PDP packet dump level"
- "PDP packet dump new level: %u\n"
- "PDP packet dump size"
- "Publish Count"
- "RAS Event Capability"
- "States"
- "Terminate Count"
- "UL"
- "UL Aggregation Histogram"
- "Uplink Bytes"
- "Uplink Pkts"
- "abp-debug-buf-size"
- "abp-uart-debug"
- "acipc-pdp-reporting"
- "currentLogSnapshotBufferSize"
- "disabled"
- "doorbellAssertAndFlush"
- "down"
- "enableHostMemProtectionGated"
- "enabled"
- "failed"
- "getLinkSpeed_block_invoke"
- "isLinkSpeedChangedGated"
- "logSnapshotBufferSize"
- "mapBarGated"
- "pdp:%s: error %d\n"
- "pdp:%s: size (%u) out of range.\n"
- "pdp_dump_level"
- "pdp_dump_size"
- "publish"
- "readBar"
- "readEndpointASPM"
- "running"
- "setPowerStateGated"
- "shadowDoorbellRing"
- "site.AppleConvergedIPCBBLogger"
- "site.AppleConvergedIPCPDPReporter"
- "site.AppleConvergedPCIBBRASReporter"
- "site.IOSimpleReporter*"
- "site.IOStateReporter*"
- "site.logBuffer"
- "some logs dropped\n"
- "stopped"
- "succeeded"
- "sysctl_pdp_dump_level"
- "sysctl_pdp_dump_size"
- "terminate"
- "up"
- "v16@?0r*8"
- "writeBar"
- "|%02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x|%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c|"

```

>  `com.apple.driver.AppleDCP`

```diff

-811.100.94.0.1
-  __TEXT.__cstring: 0x1ac9
+811.100.96.0.1
+  __TEXT.__cstring: 0x1b7b
   __TEXT.__const: 0x18
-  __TEXT_EXEC.__text: 0x7564
+  __TEXT_EXEC.__text: 0x7ad8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0xb0
   __DATA.__bss: 0x10
-  __DATA_CONST.__auth_got: 0x1a8
+  __DATA_CONST.__auth_got: 0x1c8
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__mod_init_func: 0x20
   __DATA_CONST.__mod_term_func: 0x20
   __DATA_CONST.__const: 0x1458
   __DATA_CONST.__kalloc_type: 0x100
-  Functions: 195
+  Functions: 197
   Symbols:   0
-  CStrings:  150
+  CStrings:  156
 
CStrings:
+ "1211111212221212122222222222222222222222222222222222222222112121211111121122212122112211122221121222222222222222222222222222221111211111111111111222111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111"
+ "com.apple.display.HealthMonitor.DisplayFailsafeCategorization"
+ "displayDeviceID"
+ "failsafe-category-%d"
+ "failsafe-category-0"
+ "maxConsecutive%sFailures"
+ "total%sFailures"
- "1211111212221212122222222222222222222222222222222222222222112121211111121122212122112211122221121222222222222211211111111111111222111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111"

```

>  `com.apple.driver.AppleHIDTransportSPI`

```diff

 8150.1.0.0.0
   __TEXT.__const: 0x3c8
-  __TEXT.__cstring: 0x7d1f
-  __TEXT_EXEC.__text: 0x437e4
+  __TEXT.__cstring: 0x7d31
+  __TEXT_EXEC.__text: 0x43854
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x348
+  __DATA.__data: 0x3e8
   __DATA.__common: 0xd8
   __DATA_CONST.__auth_got: 0x320
   __DATA_CONST.__got: 0x180
   __DATA_CONST.__mod_init_func: 0x28
   __DATA_CONST.__mod_term_func: 0x28
-  __DATA_CONST.__const: 0x32c0
+  __DATA_CONST.__const: 0x32e0
   __DATA_CONST.__kalloc_type: 0xa80
   __DATA_CONST.__kalloc_var: 0x320
   Functions: 1041
   Symbols:   0
-  CStrings:  897
+  CStrings:  899
 
CStrings:
+ "/AppleInternal/Library/BuildRoots/a893df77-fa81-11ef-9813-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/hidspi/HSMDevice.h"
+ "/AppleInternal/Library/BuildRoots/a893df77-fa81-11ef-9813-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/hidspi/HSMDeviceInterface.h"
+ "/AppleInternal/Library/BuildRoots/a893df77-fa81-11ef-9813-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/hidspi/HSMDeviceTest.h"
+ "/AppleInternal/Library/BuildRoots/a893df77-fa81-11ef-9813-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/hidspi/HSMHIDInterface.h"
+ "/AppleInternal/Library/BuildRoots/a893df77-fa81-11ef-9813-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/hidspi/HSMParserTest.h"
+ "/AppleInternal/Library/BuildRoots/a893df77-fa81-11ef-9813-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/hidspi/HSMSPITest.h"
+ "/AppleInternal/Library/BuildRoots/a893df77-fa81-11ef-9813-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/hidspi/HSMTransferDevice.h"
+ "/AppleInternal/Library/BuildRoots/a893df77-fa81-11ef-9813-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/hidspi/HSMTransferTest.h"
+ "/AppleInternal/Library/BuildRoots/a893df77-fa81-11ef-9813-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/hidspi/HSParserDevice.h"
+ "/AppleInternal/Library/BuildRoots/a893df77-fa81-11ef-9813-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/hidspi/HSParserTest.h"
+ "/AppleInternal/Library/BuildRoots/a893df77-fa81-11ef-9813-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/hidspi/HSTransferTest.h"
+ "AlsC"
+ "VolumeButton"
- "/AppleInternal/Library/BuildRoots/e3acf947-f363-11ef-bc4c-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/hidspi/HSMDevice.h"
- "/AppleInternal/Library/BuildRoots/e3acf947-f363-11ef-bc4c-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/hidspi/HSMDeviceInterface.h"
- "/AppleInternal/Library/BuildRoots/e3acf947-f363-11ef-bc4c-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/hidspi/HSMDeviceTest.h"
- "/AppleInternal/Library/BuildRoots/e3acf947-f363-11ef-bc4c-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/hidspi/HSMHIDInterface.h"
- "/AppleInternal/Library/BuildRoots/e3acf947-f363-11ef-bc4c-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/hidspi/HSMParserTest.h"
- "/AppleInternal/Library/BuildRoots/e3acf947-f363-11ef-bc4c-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/hidspi/HSMSPITest.h"
- "/AppleInternal/Library/BuildRoots/e3acf947-f363-11ef-bc4c-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/hidspi/HSMTransferDevice.h"
- "/AppleInternal/Library/BuildRoots/e3acf947-f363-11ef-bc4c-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/hidspi/HSMTransferTest.h"
- "/AppleInternal/Library/BuildRoots/e3acf947-f363-11ef-bc4c-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/hidspi/HSParserDevice.h"
- "/AppleInternal/Library/BuildRoots/e3acf947-f363-11ef-bc4c-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/hidspi/HSParserTest.h"
- "/AppleInternal/Library/BuildRoots/e3acf947-f363-11ef-bc4c-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/hidspi/HSTransferTest.h"

```

>  `com.apple.driver.ApplePearlSEPDriver`

```diff

-754.100.53.0.0
+754.100.55.0.0
   __TEXT.__const: 0x308
   __TEXT.__cstring: 0x99ea
   __TEXT.__os_log: 0x45d6
-  __TEXT_EXEC.__text: 0x3ccf0
+  __TEXT_EXEC.__text: 0x3ccb4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xcd
   __DATA.__common: 0x1d8

   __DATA_CONST.__const: 0x1fe8
   __DATA_CONST.__kalloc_type: 0x580
   __DATA_CONST.__kalloc_var: 0x1e0
-  Functions: 624
+  Functions: 623
   Symbols:   0
   CStrings:  1545
 

```

>  `com.apple.driver.AppleProcessorTrace`

```diff

-52.100.15.0.0
+52.100.16.0.0
   __TEXT.__cstring: 0x4398
   __TEXT.__const: 0x398
   __TEXT.__os_log: 0x1586
-  __TEXT_EXEC.__text: 0x213b0
+  __TEXT_EXEC.__text: 0x213bc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x380

```

>  `com.apple.driver.AppleSEPKeyStore`

```diff

-1827.100.152.502.1
-  __TEXT.__cstring: 0x3ad3
+1827.100.154.0.2
+  __TEXT.__cstring: 0x3ad1
   __TEXT.__const: 0x874
-  __TEXT_EXEC.__text: 0x3bcc0
+  __TEXT_EXEC.__text: 0x3bdfc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x3a4
   __DATA.__common: 0xe8

   __DATA_CONST.__const: 0x3a88
   __DATA_CONST.__kalloc_type: 0xd80
   __DATA_CONST.__kalloc_var: 0xa0
-  Functions: 951
+  Functions: 952
   Symbols:   0
   CStrings:  344
 
CStrings:
+ "1827.100.154.0.2"
+ "21:53:14"
+ "Mar  4 2025"
- "1827.100.152.502.1"
- "21:19:25"
- "Feb 25 2025"

```

>  `com.apple.driver.AppleSMC`

```diff

-728.100.8.0.0
+728.100.9.0.0
   __TEXT.__cstring: 0x8892
   __TEXT.__const: 0x1e4
   __TEXT.__os_log: 0xd26
-  __TEXT_EXEC.__text: 0x2b210
+  __TEXT_EXEC.__text: 0x2b218
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xcc
   __DATA.__common: 0x4e0
CStrings:
+ "21:46:41"
+ "21:46:43"
+ "Mar  4 2025"
- "21:08:36"
- "21:08:38"
- "Feb 25 2025"

```

>  `com.apple.driver.AppleSMCWirelessCharger`

```diff

-85.100.9.0.0
+85.100.13.0.0
   __TEXT.__const: 0x70
   __TEXT.__cstring: 0x296d
-  __TEXT.__os_log: 0x4b9
-  __TEXT_EXEC.__text: 0xf744
+  __TEXT.__os_log: 0x4e2
+  __TEXT_EXEC.__text: 0xf7cc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x68

   __DATA_CONST.__kalloc_var: 0x1e0
   Functions: 176
   Symbols:   0
-  CStrings:  369
+  CStrings:  370
 
CStrings:
+ "%s: qipp stream reception error ret(%s)\n"

```

>  `com.apple.driver.AppleSPMIPMU`

```diff

 1356.100.2.0.0
-  __TEXT.__cstring: 0x2543
+  __TEXT.__cstring: 0x2584
   __TEXT.__const: 0x26
-  __TEXT_EXEC.__text: 0xc684
+  __TEXT_EXEC.__text: 0xc774
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x320
   __DATA.__common: 0xc0

   __DATA_CONST.__kalloc_type: 0x140
   Functions: 155
   Symbols:   0
-  CStrings:  347
+  CStrings:  350
 
CStrings:
+ "%s::%s%sBoot Reason LPMSU\n\n"
+ "%s::handleStart: %s _pmuNub: %p ** configuration not found ** built 21:35:44 Mar  4 2025\n"
+ "%s::handleStart: ro=%d nvram=%d helper=%d %s _pmuNub: %p 0x%04x:0x%04x-0x%04x built 21:35:44 Mar  4 2025\n"
+ "%s::start: %s _pmuNub: %p ** configuration not found ** built 21:35:45 Mar  4 2025\n"
+ "%s::start: %s _pmuNub: %p built 21:35:45 Mar  4 2025\n"
+ "IOPMUBootReasonLPMSU"
+ "seaship-su-boot"
- "%s::handleStart: %s _pmuNub: %p ** configuration not found ** built 20:52:32 Feb 25 2025\n"
- "%s::handleStart: ro=%d nvram=%d helper=%d %s _pmuNub: %p 0x%04x:0x%04x-0x%04x built 20:52:32 Feb 25 2025\n"
- "%s::start: %s _pmuNub: %p ** configuration not found ** built 20:52:32 Feb 25 2025\n"
- "%s::start: %s _pmuNub: %p built 20:52:32 Feb 25 2025\n"

```

>  `com.apple.driver.AppleSPURose`

```diff

-1014.100.10.0.0
+1014.100.12.0.0
   __TEXT.__const: 0x30
   __TEXT.__cstring: 0x1f7c
-  __TEXT.__os_log: 0x1431
-  __TEXT_EXEC.__text: 0x17da8
+  __TEXT.__os_log: 0x1d43
+  __TEXT_EXEC.__text: 0x186ec
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x248
   __DATA.__common: 0x268

   __DATA_CONST.__mod_term_func: 0x78
   __DATA_CONST.__const: 0x32c8
   __DATA_CONST.__kalloc_type: 0x3c0
-  Functions: 615
+  Functions: 655
   Symbols:   0
-  CStrings:  368
+  CStrings:  369
 
CStrings:
+ "%s: AssertMacros: %s, %s file: %s, line: %d value:%x\n"

```

>  `com.apple.driver.AppleThunderboltPCIDownAdapter`

```diff

-437.0.0.0.0
-  __TEXT.__cstring: 0x106e
-  __TEXT_EXEC.__text: 0x5190
+438.0.0.0.0
+  __TEXT.__cstring: 0x127e
+  __TEXT_EXEC.__text: 0x55ac
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60

   __DATA_CONST.__got: 0xb0
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0xf20
+  __DATA_CONST.__const: 0xf40
   __DATA_CONST.__kalloc_type: 0x80
-  Functions: 73
+  Functions: 75
   Symbols:   0
-  CStrings:  61
+  CStrings:  66
 
CStrings:
+ "%lldus AppleThunderboltPCIDownAdapter(%x:%llx:%x)::activateSetLegacyProperty - fCorrelatedPCIDevice = %p, fProviderPort = %p\n"
+ "%lldus AppleThunderboltPCIDownAdapter(%x:%llx:%x)::activateSetLegacyProperty - switch needs extended link training, add legacy property to correlated PCI\n"
+ "%lldus AppleThunderboltPCIDownAdapter(%x:%llx:%x)::activateSetLegacyProperty - the_switch = %p\n"
+ "%lldus AppleThunderboltPCIDownAdapter(%x:%llx:%x)::deactivateRemoveLegacyProperty - remove legacy property from correlated PCI\n"
+ "PCI-Thunderbolt-Legacy"

```

>  `com.apple.driver.AppleThunderboltPCIUpAdapter`

```diff

-437.0.0.0.0
+438.0.0.0.0
   __TEXT.__cstring: 0x4235
-  __TEXT_EXEC.__text: 0x1a0a8
+  __TEXT_EXEC.__text: 0x1a174
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x220
   __DATA.__common: 0x38

```

>  `com.apple.driver.FairPlayIOKit`

```diff

 72.13.0.0.0
   __TEXT.__cstring: 0x1cc7
-  __TEXT.__const: 0x49860
-  __TEXT_EXEC.__text: 0x1cccc4
+  __TEXT.__const: 0x49850
+  __TEXT_EXEC.__text: 0x1ccd10
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x13a8
-  __DATA.__common: 0x5fe1
+  __DATA.__common: 0x5fe9
   __DATA.__bss: 0x38
   __DATA_CONST.__auth_got: 0x238
   __DATA_CONST.__got: 0x68
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
-  __DATA_CONST.__const: 0x13e78
+  __DATA_CONST.__const: 0x13ef8
   __DATA_CONST.__kalloc_type: 0x1b40
   __DATA_CONST.__kalloc_var: 0x370
   Functions: 536

```

>  `com.apple.driver.IOACIPCFamily`

```diff

 133.0.0.0.0
-  __TEXT.__cstring: 0x5ff4
-  __TEXT.__const: 0x181e7
-  __TEXT.__os_log: 0x86c
-  __TEXT_EXEC.__text: 0xbf114
+  __TEXT.__cstring: 0x3dcc
+  __TEXT.__const: 0x1d0
+  __TEXT_EXEC.__text: 0x5b6ec
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x278
-  __DATA.__common: 0x590
-  __DATA.__bss: 0x9df0
-  __DATA_CONST.__auth_got: 0x510
-  __DATA_CONST.__got: 0x27c0
-  __DATA_CONST.__mod_init_func: 0x28c8
-  __DATA_CONST.__mod_term_func: 0x128
-  __DATA_CONST.__const: 0x29cc8
-  __DATA_CONST.__kalloc_type: 0x3840
+  __DATA.__common: 0x508
+  __DATA.__bss: 0x90
+  __DATA_CONST.__auth_got: 0x440
+  __DATA_CONST.__got: 0x138
+  __DATA_CONST.__mod_init_func: 0xe0
+  __DATA_CONST.__mod_term_func: 0xd0
+  __DATA_CONST.__const: 0xb600
+  __DATA_CONST.__kalloc_type: 0x34c0
   __DATA_CONST.__kalloc_var: 0x1950
-  Functions: 4210
+  Functions: 2545
   Symbols:   0
-  CStrings:  883
+  CStrings:  564
 
CStrings:
+ "1211111212221212112111111111111111222221111111112212"
- "%02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x"
- "%06ld.%06d "
- "%d. OUT --> ... "
- "%d. size %llu. OUT --> "
- "%d. size %u. IN <-- "
- "%d. size %u. OUT --> "
- "%s Close"
- "%s Open "
- "%s Read "
- "%s Write"
- "%s: %u:%u was not found\n"
- "%s: failed to allocate logger user knob instance\n"
- "%s: logger user knob %u:%u already registered\n"
- "%s::%s: \n"
- "%s::%s: %d. %u\n"
- "%s::%s: %d. external buffer %p\n"
- "%s::%s: %d. io %p, size %u, pa %p, va %p\n"
- "%s::%s: %d. io %p, td %p\n"
- "%s::%s: %d. optional footer %p\n"
- "%s::%s: %p-[0x%x]->%p\n"
- "%s::%s: %s%02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x\n"
- "%s::%s: %s%s\n"
- "%s::%s: %u\n"
- "%s::%s: *%p = 0x%x\n"
- "%s::%s: -- done %u\n"
- "%s::%s: --done\n"
- "%s::%s: 1 byte write\n"
- "%s::%s: 4 byte write\n"
- "%s::%s: AER was already registered\n"
- "%s::%s: ASPML1 disabled on endpoint\n"
- "%s::%s: ASPML1 disabled on root port\n"
- "%s::%s: Device Status/Control register: 0x%x, isPending: %u\n"
- "%s::%s: DeviceCtl 0x%08x DeviceStatus 0x%08x LinkStatus 0x%08x\n"
- "%s::%s: Enable %u\n"
- "%s::%s: Failed to get Transaction Pending bit, ret: 0x%x\n"
- "%s::%s: Failed to read AER Capability Structure\n"
- "%s::%s: Failed to read PCIe Express Capability Structure\n"
- "%s::%s: HeaderLog 0 to 3 0x%08x 0x%08x 0x%x 0x%08x\n"
- "%s::%s: IOMMU unavailable\n"
- "%s::%s: L1SS control 1 reg: 0x%x\n"
- "%s::%s: L1SS control 2 reg: 0x%x\n"
- "%s::%s: Link control reg: 0x%x, Link control offset: 0x%llx\n"
- "%s::%s: MSI notification processed\n"
- "%s::%s: PCIE capability not found\n"
- "%s::%s: Received AER, Config Reg Space Dump : UnCorErrStat 0x%08x CorrErrStat 0x%08x AERCapCtl 0x%08x\n"
- "%s::%s: Root port local clk granularity %x ns \n"
- "%s::%s: Transaction Pending bit cleared (count: %u)\n"
- "%s::%s: Transaction Pending bit poll timed out\n"
- "%s::%s: _workLoopControl was not set yet\n"
- "%s::%s: bad index %u\n"
- "%s::%s: bar0 %p [+0x%x], bar1 %p [+0x%x]\n"
- "%s::%s: cr %u, ti %u, interval %llu\n"
- "%s::%s: crID %u, trID %u, tag 0x%x, count %u\n"
- "%s::%s: dead\n"
- "%s::%s: device %p, powerStateOrdinal %lu\n"
- "%s::%s: device %p, stateNumber %lu\n"
- "%s::%s: domainState: 0x%lx\n"
- "%s::%s: enable\n"
- "%s::%s: enable %u\n"
- "%s::%s: enable interrupt %u\n"
- "%s::%s: enablePCIPowerManagement failed 0x%x\n"
- "%s::%s: enabling PTM for Endpoint\n"
- "%s::%s: endpoint L1PMSS capability not found\n"
- "%s::%s: endpoint pcie capability not found\n"
- "%s::%s: endpoint port PCIe capability not found\n"
- "%s::%s: failed to add AER event source\n"
- "%s::%s: failed to add interrupt source\n"
- "%s::%s: failed to create AER event source\n"
- "%s::%s: failed to create event source at %u\n"
- "%s::%s: failed to get provider of IOPCI2PCIBridge\n"
- "%s::%s: failed to get provider of IOPCIDevice\n"
- "%s::%s: failed to map bar0\n"
- "%s::%s: failed to map bar1\n"
- "%s::%s: forClient %p\n"
- "%s::%s: got valid interrupt source\n"
- "%s::%s: hi %u, _completionRing[index]._hi %u, _completionRing[index]._ti %u, _completionRing[index]._ring._count %u\n"
- "%s::%s: index %d, getInterruptType error 0x%08x\n"
- "%s::%s: index %d, not msi %d\n"
- "%s::%s: index %u\n"
- "%s::%s: index %u, cd %p\n"
- "%s::%s: index %u, hi %u\n"
- "%s::%s: index out of range %d\n"
- "%s::%s: interval %llu\n"
- "%s::%s: invalid device\n"
- "%s::%s: link not up\n"
- "%s::%s: link not up 0x%x\n"
- "%s::%s: no PCI device %u\n"
- "%s::%s: options 0x%08x\n"
- "%s::%s: pci device open ret %u\n"
- "%s::%s: provider %p, options 0x%08x\n"
- "%s::%s: provider is NULL\n"
- "%s::%s: root port L1PMSS capability not found\n"
- "%s::%s: root port PCIe capability not found\n"
- "%s::%s: service already open by %p\n"
- "%s::%s: set power request %d\n"
- "%s::%s: skip doorbell flush %u, hi %u\n"
- "%s::%s: tag is completed.\n"
- "%s::%s: tag still in use. completion deferred.\n"
- "%s::%s: trID %u, tag 0x%x, discard %u, footer %p, footer-size %zu\n"
- "%s::%s: trID %u, tag 0x%x, footer %p, size %u, status %u\n"
- "%s::%s: trID %u, tag 0x%x, offset %u, size %u, footer %p, footer-size %zu\n"
- "%s::%s: unmapped bar\n"
- "%s::%s: using IOMapper::gSystem\n"
- "%s::%s: vendorID = 0x%04x, deviceID = 0x%04x\n"
- "%s::%s: workloop unavailable\n"
- "%s::%s: write falls outside BAR 0x%x\n"
- "%s::%s: write falls outside BAR 0x%x, 0x%x\n"
- "***IOAppleConvergedIPC Logger: allowed %d, PE_i_can_has_debugger %d\n"
- "/Library/Caches/com.apple.xbs/Sources/IOACIPCFamily/IOACIPCFamily/IOAppleConvergedIPCControl/IOAppleConvergedIPCLogger.cpp"
- "112111111"
- "112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221222212222122221222212222122221222212222122221222212222122221222212222122221222212222122221222212222122221222212222122221222212222122221222212222122221222212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222"
- "1211"
- "1211111111221112"
- "12111112122212121121111111111111112222211111111112212"
- "1211111212221212121122222222211111112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221222212222122221222212222122221222212222122221222212222122221222212222122221222212222122221222212222122221222212222122221222212222122221222212222122221222212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222"
- "Advanced Error Reporting"
- "AppleConvergedIPCLogger"
- "Buffers Completed"
- "Buffers Queued"
- "Bytes Dropped"
- "Bytes Sent"
- "CR HIA PA"
- "CR TIA PA"
- "CR[%d].HIA"
- "CR[%d].IAVector"
- "CR[%d].TIA"
- "CR[%d].context"
- "CR[%d].size"
- "Context Info"
- "Context Info Addr PA"
- "Correctable Error"
- "Current State Index"
- "Doorbell Counter"
- "Doorbell[%d].counter"
- "Error"
- "False"
- "Fatal Error"
- "I/O"
- "IOACIPCDebug::%s: \n"
- "IOACIPCDebug::%s:     %u: %p\n"
- "IOACIPCDebug::%s: \"%s\" didn't provide any debug files\n"
- "IOACIPCDebug::%s: \"%s\" provided %u debug files\n"
- "IOACIPCDebug::%s: %s:\n"
- "IOACIPCDebug::%s: '%s' service published (%p)\n"
- "IOACIPCDebug::%s: '%s' service terminating (%p)\n"
- "IOACIPCDebug::%s: ---done\n"
- "IOACIPCDebug::%s: --done\n"
- "IOACIPCDebug::%s: Adding service '%s' to list\n"
- "IOACIPCDebug::%s: Failed to open \"%s\"\n"
- "IOACIPCDebug::%s: Found logger service \"%s\"\n"
- "IOACIPCDebug::%s: IOAppleConvergedIPCDebug: %p, register service\n"
- "IOACIPCDebug::%s: Logging disallowed by boot-arg\n"
- "IOACIPCDebug::%s: LoggingEnableChange: requested %u, current %u\n"
- "IOACIPCDebug::%s: Registering notifier for %s\n"
- "IOACIPCDebug::%s: Servicename: \"%s\" \n"
- "IOACIPCDebug::%s: Unable to allocate event queue lock\n"
- "IOACIPCDebug::%s: async event allocation failed\n"
- "IOACIPCDebug::%s: bad refCon %p, _servicePublishNotifier %p, _serviceTerminateNotifier %p\n"
- "IOACIPCDebug::%s: debug group %s \n"
- "IOACIPCDebug::%s: directory %s \n"
- "IOACIPCDebug::%s: enqueueAsyncEvent: type %d\n"
- "IOACIPCDebug::%s: failed to add \"%s\" to CC report for \"%s\": 0x%x\n"
- "IOACIPCDebug::%s: failed to convert \"%s\" to string\n"
- "IOACIPCDebug::%s: failed to iterate debug files\n"
- "IOACIPCDebug::%s: logLevel %u, consoleLevel %u\n"
- "IOACIPCDebug::%s: service %p\n"
- "IOACIPCDebug::%s: service %p is not a IOAppleConvergedIPCDebugService object\n"
- "IOACIPCDebug::%s: terminating service %p doesn't match any saved service\n"
- "IOACIPCDebug::%s: thread call failed with 0x%08x: event %u\n"
- "IOACIPCDebug::%s: unable to create _workLoop\n"
- "IOACIPCDebug::%s: unable to create commandGate\n"
- "IOACIPCDebug::%s: unable to create service notifiers\n"
- "IOACIPCDebug::%s: unknown event %u\n"
- "IOAppleConvergedIPC debug disabled by boot-arg\n"
- "IOAppleConvergedIPCControl::start: failed to create logger\n"
- "IOAppleConvergedIPCControl::start: logger attach/start failed %p\n"
- "IOAppleConvergedIPCControlReporter"
- "IOAppleConvergedIPCLogger"
- "IOAppleConvergedIPCLogger.cpp"
- "IOAppleConvergedIPCLogger::initWithReporter: no reporter\n"
- "IOAppleConvergedIPCLogger::initWithReporter: super failed\n"
- "IOAppleConvergedIPCLogger::start: super failed\n"
- "IOAppleConvergedIPCReporter"
- "IOAppleConvergedIPCReporter::%s: could not create a legend\n"
- "IOAppleConvergedIPCReporter::%s: could not create a set object\n"
- "IOAppleConvergedIPCReporter::%s: invalid argument\n"
- "IOAppleConvergedIPCReporter::%s: setProperty failed\n"
- "IOAppleConvergedIPCReporter::%s: subclass failed to add reporters\n"
- "IOReportLegend"
- "IOReportLegendPublic"
- "Interfaces"
- "Interrupt"
- "Logging"
- "Logging to User Client"
- "Logs Dropped"
- "Logs Sent"
- "MCR PA"
- "MTR PA"
- "Non-Fatal Error"
- "Pipe[%d].HIA"
- "Pipe[%d].IAVector"
- "Pipe[%d].TIA"
- "Pipe[%d].context"
- "Pipe[%d].size"
- "Power"
- "R"
- "Ring Info"
- "Secondary ISR Count"
- "Secondary Interrupt Handler"
- "State Summary"
- "String"
- "TR HIA PA"
- "TR TIA PA"
- "TimeStampNs"
- "True"
- "W"
- "[%03u] %06ld.%06d -   %s   - %p - %07u - 0x%08x\n"
- "[%03u] %06ld.%06d - %06ld.%06d   - %06ld.%06d\n"
- "[%03u] %06ld.%06d - %u -> %u\n"
- "[%03u] %06ld.%06d - ring db %u: value %u\n"
- "[%03u] %06ld.%06d - start timer: %llu us\n"
- "[%03u] %06ld.%06d - timer fired\n"
- "[idx] primary       - secondary start - secondary end\n"
- "[idx] time          - [R/W] - addr               - size    - value\n"
- "[idx] time          - event\n"
- "[idx] time          - old state -> new state\n"
- "acipc-db.log"
- "acipc-ipc-state.log"
- "acipc-mmio.log"
- "acipc-msi.log"
- "acipc-nodebug"
- "acipc-sleep-state.log"
- "addDebugServiceData"
- "aggregatedIoCompletion"
- "asyncEventHandler"
- "closeServiceGated"
- "completeACIPCIO"
- "deregisterUserKnob"
- "didTerminate"
- "disableLoggingGated"
- "disableLoggingInternal"
- "dumpLogs"
- "enableASPMGated"
- "enableEndpointASPM"
- "enableEndpointPTM"
- "enableL1SSPostROMGated"
- "enableLoggingGated"
- "enableLoggingInternal"
- "enqueueAsyncEvent"
- "failed to create _logBufferQueue\n"
- "flr"
- "free"
- "gatherEPConfigRegSpace"
- "getEPTransactionPendingBit"
- "getInLowPower"
- "initialPowerStateForDomainState"
- "ioCompletion"
- "ioTransfer"
- "isDeviceAccessibleGated"
- "mapBarGated"
- "mmioWrite"
- "mmioWriteBar0"
- "mmioWriteBar1"
- "mmioWriteMemory"
- "mmioWriteMemoryBar0"
- "mmioWriteMemoryBar1"
- "msiInterrupt"
- "not "
- "notifyTerminateAck"
- "notifyTerminateAckGated"
- "openLogger"
- "openServiceGated"
- "powerStateDidChangeTo"
- "powerStateWillChangeTo"
- "prepareACIPCIO"
- "printDbgServiceQueue"
- "processCD"
- "processCompletionRing"
- "processSubrangeCompletion"
- "processSubrangeDiscard"
- "protectDeviceAccess_block_invoke"
- "queueTransfer"
- "registerAER"
- "registerMSI"
- "registerMSIwithFilter"
- "registerRead"
- "registerUserKnob"
- "registerWorkLoop"
- "registerWrite"
- "reinitialize"
- "reinitializeCompletionRing"
- "sendMessage"
- "sendTransfer"
- "serviceDebugNotifier"
- "serviceNotifier"
- "setPowerOn"
- "setPowerState"
- "setPowerStateGated"
- "setupMessage"
- "shadowDoorbellCheck"
- "shadowDoorbellFlush"
- "site.IOACIPCiOSLogger"
- "site.IOAppleConvergedIPCControlReporter"
- "site.IOAppleConvergedIPCLogger"
- "site.IOAppleConvergedIPCReporter"
- "site.UserKnob"
- "site.logBuffer"
- "site.logBufferQueue"
- "start"
- "startReporting"
- "stop"
- "terminate"
- "triggerStateDumpForService"
- "triggerStateDumpForService_block_invoke"
- "unmapBarGated"
- "updateCompletionRingTailIndex"
- "updateDebugServiceInfo"
- "validateMSIIndex"
- "willTerminate"
- "willTerminateGated"

```

>  `com.apple.driver.IOPAudioVoiceTriggerDevice`

```diff

 440.4.0.0.0
   __TEXT.__const: 0x78
-  __TEXT.__cstring: 0x2c29
+  __TEXT.__cstring: 0x2c32
   __TEXT.__os_log: 0x16f1
   __TEXT_EXEC.__text: 0xafb0
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__kalloc_type: 0xc0
   Functions: 258
   Symbols:   0
-  CStrings:  232
+  CStrings:  233
 
CStrings:
+ "21:04:42"
+ "21:04:43"
+ "Mar  6 2025"
- "21:16:59"
- "Feb 25 2025"

```

>  `com.apple.filesystems.apfs`

```diff

-2332.100.75.502.1
+2332.100.82.0.1
   __TEXT.__const: 0x990
-  __TEXT.__cstring: 0x49c78
-  __TEXT_EXEC.__text: 0x13ffe0
+  __TEXT.__cstring: 0x49c89
+  __TEXT_EXEC.__text: 0x13ffc8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x6a0
   __DATA.__bss: 0xca8
-  __DATA_CONST.__auth_got: 0x1128
+  __DATA_CONST.__auth_got: 0x1120
   __DATA_CONST.__got: 0x1b0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x10

   __DATA_CONST.__assert: 0x14
   Functions: 2268
   Symbols:   0
-  CStrings:  6414
+  CStrings:  6415
 
CStrings:
+ "%s:%d: ubc_msync failed on ino %llu offset %llu (error %d)\n"
+ "2025/03/04"
+ "21:38:34"
+ "21:38:35"
+ "2332.100.82.0.1"
+ "Mar  4 2025"
+ "apfs-2332.100.82.0.1"
- "%s:%d: ubc_msync failed on ino %llu (error %d)\n"
- "15:08:39"
- "2025/02/28"
- "2332.100.75.502.1"
- "Feb 28 2025"
- "apfs-2332.100.75.502.1"

```

>  `com.apple.iokit.IONVMeFamily`

```diff

-775.100.14.0.0
+775.100.14.0.1
   __TEXT.__const: 0x708
   __TEXT.__cstring: 0xf8eb
-  __TEXT_EXEC.__text: 0x600cc
+  __TEXT_EXEC.__text: 0x600a0
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x544
+  __DATA.__data: 0x4e4
   __DATA.__common: 0x528
   __DATA.__bss: 0x10
   __DATA_CONST.__auth_got: 0x688

   __DATA_CONST.__const: 0xcc98
   __DATA_CONST.__kalloc_type: 0x7c0
   __DATA_CONST.__kalloc_var: 0x550
-  Functions: 3170
+  Functions: 3169
   Symbols:   0
   CStrings:  1710
 

```

>  `com.apple.iokit.IOPCIFamily`

```diff

-681.100.10.0.0
+681.100.11.0.0
   __TEXT.__const: 0x710
-  __TEXT.__cstring: 0x548c
-  __TEXT_EXEC.__text: 0x2fc50
+  __TEXT.__cstring: 0x548e
+  __TEXT_EXEC.__text: 0x2fca4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xcc
   __DATA.__common: 0x218
CStrings:
+ "111111222"
+ "21:35:37"
+ "Mar  4 2025"
- "1111112"
- "20:52:25"
- "Feb 25 2025"

```

>  `com.apple.iokit.IOThunderboltFamily`

```diff

-6781.100.3.0.0
-  __TEXT.__cstring: 0x34429
-  __TEXT.__os_log: 0x2e268
+6781.100.4.0.0
+  __TEXT.__cstring: 0x3439d
+  __TEXT.__os_log: 0x2e604
   __TEXT.__const: 0x800
-  __TEXT_EXEC.__text: 0x18e2b8
+  __TEXT_EXEC.__text: 0x18e54c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xb1a
   __DATA.__common: 0x1238

   __DATA_CONST.__kalloc_var: 0xaf0
   Functions: 4720
   Symbols:   0
-  CStrings:  4821
+  CStrings:  4828
 
CStrings:
+ "21:36:07"
+ "Mar  4 2025"
- "%lldus IOThunderboltPort(%x@%llx:%x)::configureFromDesciption - WORKAROUND: setting HW BW to %u! spec_version = 0x%x fAdapterType = 0x%08x\n"
- "20:53:22"
- "Feb 25 2025"

```

>  `com.apple.kernel`

```diff

-11417.100.564.502.1
-  __TEXT.__const: 0x34910
+11417.100.576.502.2
+  __TEXT.__const: 0x34900
   __TEXT.__copyio_vectors: 0xf0
-  __TEXT.__cstring: 0x765fa
-  __TEXT.__os_log: 0x2a5fa
+  __TEXT.__cstring: 0x7670a
+  __TEXT.__os_log: 0x2a64c
   __TEXT.__eh_frame: 0x610
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x2d8

   __DATA_CONST.__brk_desc: 0x78
   __DATA_SPTM.__const: 0x3c000
   __TEXT_EXEC.__hib_text: 0xcc8
-  __TEXT_EXEC.__text: 0x8180cc
+  __TEXT_EXEC.__text: 0x81ea5c
   __TEXT_BOOT_EXEC.__bootcode: 0x514c
   __KLD.__text: 0x1638
   __LASTDATA_CONST.__mod_init_func: 0x8
   __LAST.__pinst: 0x8
   __LAST.__last: 0x0
   __KLDDATA.__cstring: 0x6e1
-  __KLDDATA.__const: 0x2b10
+  __KLDDATA.__const: 0x2af8
   __KLDDATA.__mod_init_func: 0x8
   __KLDDATA.__mod_term_func: 0x8
   __KLDDATA.__bss: 0x1
   __DATA.__data: 0x185c1
   __DATA.__lock_grp: 0x5a10
-  __DATA.__percpu: 0x6e78
+  __DATA.__percpu: 0x6e80
   __DATA.__common: 0x5bd10
   __DATA.__bss: 0x96008
   __BOOTDATA.__data: 0x18000

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x4662c
-  Functions: 20142
+  Functions: 20156
   Symbols:   0
-  CStrings:  17873
+  CStrings:  17879
 
CStrings:
+ "Expected to have usecount or iocount on vnode @%s:%d"
+ "IS_P2ALIGNED(ccp, CHANNEL_CACHE_ALIGN_MAX)"
+ "TCP LQM heuristics flags (1:rxmtcomp 2:noackpro 4:synrxmt 8:stealth 0x10:rtomin 0x20:notlp)"
+ "memorystatus: attempt to unkill pid %s [%d] ignored\n"
+ "memorystatus: resuming %s [%d]\n"
+ "memorystatus: unthrottling %s [%d]\n"
+ "memorystatus: {\"available_pages_below_critical\": %d, \"available_pages_below_idle\": %d, \"available_pages_below_soft\": %d, \"available_pages_below_reaper\": %d, \"compressor_needs_to_swap\": %d, \"compressor_exhausted\": %d, \"compressor_is_thrashing\": %d, \"filecache_is_thrashing\": %d, \"zone_map_is_exhausted\": %d, \"phantom_cache_pressure\": %d, \"swappable_compressor_segments_over_limit\": %d, \"swapin_queue_over_limit\": %d, \"swap_low\": %d, \"swap_exhausted\": %d}\n"
+ "sha_digest_len == SHA1_RESULTLEN || sha_digest_len == SHA256_DIGEST_LENGTH"
+ "unaligned read of 0x%lu bytes from socd trace ram address 0x%lu @%s:%d"
+ "unaligned write of 0x%lu bytes to socd trace ram address 0x%lu @%s:%d"
- "811222222"
- "TCP LQM heuristics flags (1:rxmtcomp 2:noackpro 4:synrxmt 8:stealth 10:rtomin)"
- "memorystatus: {\"available_pages_below_critical\": %d, \"available_pages_below_idle\": %d, \"available_pages_below_soft\": %d, \"available_pages_below_reaper\": %d, \"compressor_needs_to_swap\": %d, \"compressor_is_low_on_space\": %d, \"compressor_is_thrashing\": %d, \"compressed_pages_nearing_limit\": %d, \"filecache_is_thrashing\": %d, \"zone_map_is_exhausted\": %d, \"phantom_cache_pressure\": %d, \"swappable_compressor_segments_over_limit\": %d, \"swapin_queue_over_limit\": %d, \"swap_low\": %d, \"swap_full\": %d}\n"
- "unaligned acccess to socd trace ram @%s:%d"

```

>  `com.apple.security.sandbox`

```diff

-2401.100.194.0.0
+2401.100.196.0.0
   __TEXT.__os_log: 0x2092
-  __TEXT.__const: 0x1b2e71
+  __TEXT.__const: 0x1b3761
   __TEXT.__cstring: 0x719d
   __TEXT_EXEC.__text: 0x31588
   __TEXT_EXEC.__auth_stubs: 0x0

```

</details>

## MachO

### 🆕 NEW (1)

- `/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices-0002.bundle/MobileDevices-0002`

### ❌ Removed (2)

- `/System/Library/ExtensionKit/Extensions/ProactiveShareSheetLighthouseBackgroundPlugin.appex/ProactiveShareSheetLighthouseBackgroundPlugin`
- `/System/Library/PrivateFrameworks/ProactiveShareSheetDataHarvestingLighthouse.framework/PlugIns/ProactiveShareSheetDataHarvestingLighthousePlugin.appex/ProactiveShareSheetDataHarvestingLighthousePlugin`

### ⬆️ Updated (482)

<details>
  <summary><i>View Updated</i></summary>

- [/Applications/AccessorySetupUI.app/AccessorySetupUI](MACHOS/AccessorySetupUI.md)
- [/Applications/ActivityMessagesApp.app/PlugIns/ActivityMessagesExtension.appex/ActivityMessagesExtension](MACHOS/ActivityMessagesExtension.md)
- [/Applications/ActivityProgressUI.app/ActivityProgressUI](MACHOS/ActivityProgressUI.md)
- [/Applications/AdaptiveMusicApp.app/AdaptiveMusicApp](MACHOS/AdaptiveMusicApp.md)
- [/Applications/AirPlayReceiver.app/AirPlayReceiver](MACHOS/AirPlayReceiver.md)
- [/Applications/AppDistributionLaunchAngel.app/AppDistributionLaunchAngel](MACHOS/AppDistributionLaunchAngel.md)
- [/Applications/AppleIDSetupUIService.app/AppleIDSetupUIService](MACHOS/AppleIDSetupUIService.md)
- [/Applications/AskToMessagesHost.app/PlugIns/AskToMessagesExtension.appex/AskToMessagesExtension](MACHOS/AskToMessagesExtension.md)
- [/Applications/BusinessExtensionsWrapper.app/PlugIns/Business.appex/Business](MACHOS/Business.md)
- [/Applications/CameraOverlayAngel.app/CameraOverlayAngel](MACHOS/CameraOverlayAngel.md)
- [/Applications/CarCamera.app/CarCamera](MACHOS/CarCamera.md)
- [/Applications/CarPlaySettings.app/CarPlaySettings](MACHOS/CarPlaySettings.md)
- [/Applications/Charge.app/Charge](MACHOS/Charge.md)
- [/Applications/ClarityCamera.app/ClarityCamera](MACHOS/ClarityCamera.md)
- [/Applications/Climate.app/Climate](MACHOS/Climate.md)
- [/Applications/ClockAngel.app/ClockAngel](MACHOS/ClockAngel.md)
- [/Applications/Closures.app/Closures](MACHOS/Closures.md)
- [/Applications/ColorPickerUIService.app/ColorPickerUIService](MACHOS/ColorPickerUIService.md)
- [/Applications/Diagnostics.app/Diagnostics](MACHOS/Diagnostics.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8185.appex/Diagnostic-8185](MACHOS/Diagnostic-8185.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9006.appex/Diagnostic-9006](MACHOS/Diagnostic-9006.md)
- [/Applications/DiagnosticsService.app/PlugIns/SystemReport.appex/SystemReport](MACHOS/SystemReport.md)
- [/Applications/EventViewService.app/EventViewService](MACHOS/EventViewService.md)
- [/Applications/FTMInternal-4.app/FTMInternal-4](MACHOS/FTMInternal-4.md)
- [/Applications/Family.app/PlugIns/InviteMessageBubbleExtension.appex/InviteMessageBubbleExtension](MACHOS/InviteMessageBubbleExtension.md)
- [/Applications/Feedback Assistant iOS.app/Feedback Assistant iOS](MACHOS/Feedback_Assistant_iOS.md)
- [/Applications/FinanceUIService.app/FinanceUIService](MACHOS/FinanceUIService.md)
- [/Applications/FindMyRemoteUIService.app/FindMyRemoteUIService](MACHOS/FindMyRemoteUIService.md)
- [/Applications/FontPickerUIService.app/FontPickerUIService](MACHOS/FontPickerUIService.md)
- [/Applications/GameCenterUIService.app/PlugIns/GameCenterMessageExtension.appex/GameCenterMessageExtension](MACHOS/GameCenterMessageExtension.md)
- [/Applications/GameCenterWidgets.app/PlugIns/GCWidgets.appex/GCWidgets](MACHOS/GCWidgets.md)
- [/Applications/GameOverlayUI.app/GameOverlayUI](MACHOS/GameOverlayUI.md)
- [/Applications/GuestUserHandoverSetup.app/GuestUserHandoverSetup](MACHOS/GuestUserHandoverSetup.md)
- [/Applications/HDSViewService.app/HDSViewService](MACHOS/HDSViewService.md)
- [/Applications/HeadphoneProxService.app/HeadphoneProxService](MACHOS/HeadphoneProxService.md)
- [/Applications/HomeCaptiveViewService.app/HomeCaptiveViewService](MACHOS/HomeCaptiveViewService.md)
- [/Applications/InCallService.app/InCallService](MACHOS/InCallService.md)
- [/Applications/InCallService.app/PlugIns/IntentsUI.appex/IntentsUI](MACHOS/IntentsUI.md)
- [/Applications/Media.app/Media](MACHOS/Media.md)
- [/Applications/MediaRemoteUI.app/MediaRemoteUI](MACHOS/MediaRemoteUI.md)
- [/Applications/MobilePhone.app/MobilePhone](MACHOS/MobilePhone.md)
- [/Applications/MobilePhone.app/PlugIns/VoicemailMessageNotificationExtension.appex/VoicemailMessageNotificationExtension](MACHOS/VoicemailMessageNotificationExtension.md)
- [/Applications/MusicRecognition.app/MusicRecognition](MACHOS/MusicRecognition.md)
- [/Applications/NewDeviceSetupUIService.app/NewDeviceSetupUIService](MACHOS/NewDeviceSetupUIService.md)
- [/Applications/PASViewService.app/PASViewService](MACHOS/PASViewService.md)
- [/Applications/PCViewService.app/PCViewService](MACHOS/PCViewService.md)
- [/Applications/PeopleMessageService.app/PlugIns/PeopleMessagesScreenTime.appex/PeopleMessagesScreenTime](MACHOS/PeopleMessagesScreenTime.md)
- [/Applications/PeopleViewService.app/PeopleViewService](MACHOS/PeopleViewService.md)
- [/Applications/Preferences.app/Preferences](MACHOS/Preferences.md)
- [/Applications/RecoverDeviceUI.app/RecoverDeviceUI](MACHOS/RecoverDeviceUI.md)
- [/Applications/SOSBuddy.app/SOSBuddy](MACHOS/SOSBuddy.md)
- [/Applications/Screen Time.app/PlugIns/ScreenTimeWidgetExtension.appex/ScreenTimeWidgetExtension](MACHOS/ScreenTimeWidgetExtension.md)
- [/Applications/Setup.app/Setup](MACHOS/Setup.md)
- [/Applications/SharingUIService.app/SharingUIService](MACHOS/SharingUIService.md)
- [/Applications/SharingViewService.app/SharingViewService](MACHOS/SharingViewService.md)
- [/Applications/ShazamEventsApp.app/ShazamEventsApp](MACHOS/ShazamEventsApp.md)
- [/Applications/Sidecar.app/PlugIns/ContinuityDisplay.appex/ContinuityDisplay](MACHOS/ContinuityDisplay.md)
- [/Applications/Siri.app/PlugIns/TypeToSiriWidgetExtension.appex/TypeToSiriWidgetExtension](MACHOS/TypeToSiriWidgetExtension.md)
- [/Applications/Siri.app/Siri](MACHOS/Siri.md)
- [/Applications/StickerPickerService.app/StickerPickerService](MACHOS/StickerPickerService.md)
- [/Applications/StickersUltra.app/PlugIns/StickersUltraExtension.appex/StickersUltraExtension](MACHOS/StickersUltraExtension.md)
- [/Applications/StoreKitUIService.app/StoreKitUIService](MACHOS/StoreKitUIService.md)
- [/Applications/TDGSharingViewService.app/TDGSharingViewService](MACHOS/TDGSharingViewService.md)
- [/Applications/Tamale.app/Tamale](MACHOS/Tamale.md)
- [/Applications/TirePressure.app/TirePressure](MACHOS/TirePressure.md)
- [/Applications/Trip.app/Trip](MACHOS/Trip.md)
- [/Applications/Vehicle.app/Vehicle](MACHOS/Vehicle.md)
- [/Applications/WritingToolsUIService.app/WritingToolsUIService](MACHOS/WritingToolsUIService.md)
- [/Library/Audio/Plug-Ins/HAL/VirtualAudio.plugin/VirtualAudio](MACHOS/VirtualAudio.md)
- [/System/Applications/Family/InviteMessageBubbleExtension.appex/InviteMessageBubbleExtension](MACHOS/InviteMessageBubbleExtension.md)
- [/System/DriverKit/usr/lib/system/libsystem_c_debug.dylib](MACHOS/libsystem_c_debug.dylib.md)
- [/System/DriverKit/usr/lib/system/libsystem_malloc_debug.dylib](MACHOS/libsystem_malloc_debug.dylib.md)
- [/System/Library/AccessibilityBundles/AXMotionCuesServer.axuiservice/AXMotionCuesServer](MACHOS/AXMotionCuesServer.md)
- [/System/Library/AccessibilityBundles/BackTapUIServer.axuiservice/BackTapUIServer](MACHOS/BackTapUIServer.md)
- [/System/Library/AccessibilityBundles/ClockAngel.axbundle/ClockAngel](MACHOS/ClockAngel.md)
- [/System/Library/AccessibilityBundles/LiveSpeechUIService.axuiservice/LiveSpeechUIService](MACHOS/LiveSpeechUIService.md)
- [/System/Library/Accounts/Authentication/AMSAccountAuthenticationPlugin.bundle/AMSAccountAuthenticationPlugin](MACHOS/AMSAccountAuthenticationPlugin.md)
- [/System/Library/Accounts/ServiceOwners/AMSMediaServiceOwner.bundle/AMSMediaServiceOwner](MACHOS/AMSMediaServiceOwner.md)
- [/System/Library/AppleMediaServices/DynamicUI/PlugIns/CoreDynamicUIPlugin.bundle/CoreDynamicUIPlugin](MACHOS/CoreDynamicUIPlugin.md)
- [/System/Library/AppleMediaServices/DynamicUI/PlugIns/StoreDynamicUIPlugin.bundle/StoreDynamicUIPlugin](MACHOS/StoreDynamicUIPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/AudioFlowDelegatePlugin](MACHOS/AudioFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/CarCommandsFlowDelegatePlugin.bundle/CarCommandsFlowDelegatePlugin](MACHOS/CarCommandsFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/DailyBriefingFlowPlugin.bundle/DailyBriefingFlowPlugin](MACHOS/DailyBriefingFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/EdutainmentFlowPlugin.bundle/EdutainmentFlowPlugin](MACHOS/EdutainmentFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/EmergencyFlowPlugin.bundle/EmergencyFlowPlugin](MACHOS/EmergencyFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/GeoFlowDelegatePlugin.bundle/GeoFlowDelegatePlugin](MACHOS/GeoFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/HealthFlowDelegatePlugin.bundle/HealthFlowDelegatePlugin](MACHOS/HealthFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/IFFlowPlugin](MACHOS/IFFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/InformationFlowPlugin](MACHOS/InformationFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/PhoneCallFlowDelegatePlugin](MACHOS/PhoneCallFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SiriLinkFlowPlugin.bundle/SiriLinkFlowPlugin](MACHOS/SiriLinkFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/SocialConversationFlowDelegatePlugin](MACHOS/SocialConversationFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/WellnessFlowPlugin](MACHOS/WellnessFlowPlugin.md)
- [/System/Library/Assistant/Plugins/Maps.assistantBundle/Maps](MACHOS/Maps.md)
- [/System/Library/Assistant/Plugins/PreferencesAssistant.assistantBundle/PreferencesAssistant](MACHOS/PreferencesAssistant.md)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriPrivateLearningInferencePlugin.bundle/SiriPrivateLearningInferencePlugin](MACHOS/SiriPrivateLearningInferencePlugin.md)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriPrivateLearningPatternExtractionPlugin.bundle/SiriPrivateLearningPatternExtractionPlugin](MACHOS/SiriPrivateLearningPatternExtractionPlugin.md)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriPrivateLearningTTSMispronunciationPlugin.bundle/SiriPrivateLearningTTSMispronunciationPlugin](MACHOS/SiriPrivateLearningTTSMispronunciationPlugin.md)
- [/System/Library/Assistant/UIPlugins/Maps.siriUIBundle/Maps](MACHOS/Maps.md)
- [/System/Library/Audio/Plug-Ins/AVC/AVCHalogen.driver/AVCHalogen](MACHOS/AVCHalogen.md)
- [/System/Library/Audio/Plug-Ins/HAL/AirPlayHalogen.driver/AirPlayHalogen](MACHOS/AirPlayHalogen.md)
- [/System/Library/Audio/Plug-Ins/HAL/BTAudioHALPlugin.driver/BTAudioHALPlugin](MACHOS/BTAudioHALPlugin.md)
- [/System/Library/Audio/Plug-Ins/HAL/CarPlayHalogen.driver/CarPlayHalogen](MACHOS/CarPlayHalogen.md)
- [/System/Library/Audio/Plug-Ins/HAL/OctaviaHalogen.driver/OctaviaHalogen](MACHOS/OctaviaHalogen.md)
- [/System/Library/Audio/Plug-Ins/usbaudio.bundle/usbaudiod](MACHOS/usbaudiod.md)
- [/System/Library/CoreServices/AccessibilityUIServer.app/Extensions/AccessibilityAppIntents.appex/AccessibilityAppIntents](MACHOS/AccessibilityAppIntents.md)
- [/System/Library/CoreServices/AccessibilityUIServer.app/PlugIns/AccessibilityControlsExtension.appex/AccessibilityControlsExtension](MACHOS/AccessibilityControlsExtension.md)
- [/System/Library/CoreServices/AegirProxyApp.app/PlugIns/AegirPoster.appex/AegirPoster](MACHOS/AegirPoster.md)
- [/System/Library/CoreServices/AssistiveTouch.app/assistivetouchd](MACHOS/assistivetouchd.md)
- [/System/Library/CoreServices/ClarityBoard.app/ClarityBoard](MACHOS/ClarityBoard.md)
- [/System/Library/CoreServices/IntelligentLight.app/IntelligentLight](MACHOS/IntelligentLight.md)
- [/System/Library/CoreServices/OTACrashCopier](MACHOS/OTACrashCopier.md)
- [/System/Library/CoreServices/VoiceOverTouch.app/vot](MACHOS/vot.md)
- [/System/Library/CoreServices/osanalyticshelper](MACHOS/osanalyticshelper.md)
- [/System/Library/DataClassMigrators/MobileAsset.migrator/MobileAsset](MACHOS/MobileAsset.md)
- [/System/Library/DataClassMigrators/RestorePostProcess.migrator/RestorePostProcess](MACHOS/RestorePostProcess.md)
- [/System/Library/DigitalSeparation/SharingSources/DSNotesPlugin.bundle/DSNotesPlugin](MACHOS/DSNotesPlugin.md)
- [/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN](MACHOS/com.apple.DriverKit-AppleBCMWLAN.md)
- [/System/Library/ExtensionKit/Extensions/ADFollowUpExtension.appex/ADFollowUpExtension](MACHOS/ADFollowUpExtension.md)
- [/System/Library/ExtensionKit/Extensions/AccessibilityControlsExtension.appex/AccessibilityControlsExtension](MACHOS/AccessibilityControlsExtension.md)
- [/System/Library/ExtensionKit/Extensions/AppleAccountIntents.appex/AppleAccountIntents](MACHOS/AppleAccountIntents.md)
- [/System/Library/ExtensionKit/Extensions/AssistantSettingsControlsExtension.appex/AssistantSettingsControlsExtension](MACHOS/AssistantSettingsControlsExtension.md)
- [/System/Library/ExtensionKit/Extensions/BatterySettingsIntentsExtension.appex/BatterySettingsIntentsExtension](MACHOS/BatterySettingsIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/DeveloperSettingsIntents.appex/DeveloperSettingsIntents](MACHOS/DeveloperSettingsIntents.md)
- [/System/Library/ExtensionKit/Extensions/DisplayAndBrightnessSettingsExtension.appex/DisplayAndBrightnessSettingsExtension](MACHOS/DisplayAndBrightnessSettingsExtension.md)
- [/System/Library/ExtensionKit/Extensions/DoNotDisturbAppIntents.appex/DoNotDisturbAppIntents](MACHOS/DoNotDisturbAppIntents.md)
- [/System/Library/ExtensionKit/Extensions/DocumentAppIntents.appex/DocumentAppIntents](MACHOS/DocumentAppIntents.md)
- [/System/Library/ExtensionKit/Extensions/EventKitUIRemoteUIExtension.appex/EventKitUIRemoteUIExtension](MACHOS/EventKitUIRemoteUIExtension.md)
- [/System/Library/ExtensionKit/Extensions/FamilyIntents.appex/FamilyIntents](MACHOS/FamilyIntents.md)
- [/System/Library/ExtensionKit/Extensions/FedStatsMLHostPluginClassA.appex/FedStatsMLHostPluginClassA](MACHOS/FedStatsMLHostPluginClassA.md)
- [/System/Library/ExtensionKit/Extensions/GenerativeAssistantExtension.appex/GenerativeAssistantExtension](MACHOS/GenerativeAssistantExtension.md)
- [/System/Library/ExtensionKit/Extensions/GenerativeAssistantSettingsExtension.appex/GenerativeAssistantSettingsExtension](MACHOS/GenerativeAssistantSettingsExtension.md)
- [/System/Library/ExtensionKit/Extensions/KeyboardSettingsExtension.appex/KeyboardSettingsExtension](MACHOS/KeyboardSettingsExtension.md)
- [/System/Library/ExtensionKit/Extensions/MADViewServiceExtension.appex/MADViewServiceExtension](MACHOS/MADViewServiceExtension.md)
- [/System/Library/ExtensionKit/Extensions/MKRemoteUI.appex/MKRemoteUI](MACHOS/MKRemoteUI.md)
- [/System/Library/ExtensionKit/Extensions/MercuryPosterExtension.appex/MercuryPosterExtension](MACHOS/MercuryPosterExtension.md)
- [/System/Library/ExtensionKit/Extensions/MessagesAnalyticsWorker.appex/MessagesAnalyticsWorker](MACHOS/MessagesAnalyticsWorker.md)
- [/System/Library/ExtensionKit/Extensions/MusicEngagementExtension.appex/MusicEngagementExtension](MACHOS/MusicEngagementExtension.md)
- [/System/Library/ExtensionKit/Extensions/ODDIPoirotMetricsExtension.appex/ODDIPoirotMetricsExtension](MACHOS/ODDIPoirotMetricsExtension.md)
- [/System/Library/ExtensionKit/Extensions/PridePosterExtension.appex/PridePosterExtension](MACHOS/PridePosterExtension.md)
- [/System/Library/ExtensionKit/Extensions/PrivateEvolutionPlugin.appex/PrivateEvolutionPlugin](MACHOS/PrivateEvolutionPlugin.md)
- [/System/Library/ExtensionKit/Extensions/ProductPageExtension.appex/ProductPageExtension](MACHOS/ProductPageExtension.md)
- [/System/Library/ExtensionKit/Extensions/ScreenTimeAppIntentsExtension.appex/ScreenTimeAppIntentsExtension](MACHOS/ScreenTimeAppIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/SearchToolExtension.appex/SearchToolExtension](MACHOS/SearchToolExtension.md)
- [/System/Library/ExtensionKit/Extensions/SubscribePageExtension.appex/SubscribePageExtension](MACHOS/SubscribePageExtension.md)
- [/System/Library/ExtensionKit/Extensions/WiFiSettingsControlsExtension.appex/WiFiSettingsControlsExtension](MACHOS/WiFiSettingsControlsExtension.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.fskit.apfs.appex/com.apple.fskit.apfs](MACHOS/com.apple.fskit.apfs.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.fskit.msdos.appex/com.apple.fskit.msdos](MACHOS/com.apple.fskit.msdos.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.mlhost.CloudWorker.appex/com.apple.mlhost.CloudWorker](MACHOS/com.apple.mlhost.CloudWorker.md)
- [/System/Library/Filesystems/apfs.fs/apfs_checkseal](MACHOS/apfs_checkseal.md)
- [/System/Library/Filesystems/apfs.fs/apfs_condenser](MACHOS/apfs_condenser.md)
- [/System/Library/Filesystems/apfs.fs/apfs_iosd](MACHOS/apfs_iosd.md)
- [/System/Library/Filesystems/apfs.fs/apfs_vol_converter](MACHOS/apfs_vol_converter.md)
- [/System/Library/Filesystems/apfs.fs/fsck_apfs](MACHOS/fsck_apfs.md)
- [/System/Library/Filesystems/apfs.fs/newfs_apfs](MACHOS/newfs_apfs.md)
- [/System/Library/Filesystems/apfs.fs/slurpAPFSMeta](MACHOS/slurpAPFSMeta.md)
- [/System/Library/Filesystems/apfs.fs/sm_stats](MACHOS/sm_stats.md)
- [/System/Library/Frameworks/AutomatedDeviceEnrollment.framework/PlugIns/AddDevicesToAutomatedDeviceEnrollmentExtension.appex/AddDevicesToAutomatedDeviceEnrollmentExtension](MACHOS/AddDevicesToAutomatedDeviceEnrollmentExtension.md)
- [/System/Library/Frameworks/CFNetwork.framework/PlugIns/DiagnosticExtension.appex/DiagnosticExtension](MACHOS/DiagnosticExtension.md)
- [/System/Library/Frameworks/CoreGraphics.framework/XPCServices/CGPDFService.xpc/CGPDFService](MACHOS/CGPDFService.md)
- [/System/Library/Frameworks/CoreLocation.framework/PlugIns/CoreLocationNumberedMapCalloutPromptPlugin.appex/CoreLocationNumberedMapCalloutPromptPlugin](MACHOS/CoreLocationNumberedMapCalloutPromptPlugin.md)
- [/System/Library/Frameworks/CoreLocation.framework/PlugIns/CoreLocationRepromptAlwaysAuthPromptPlugin.appex/CoreLocationRepromptAlwaysAuthPromptPlugin](MACHOS/CoreLocationRepromptAlwaysAuthPromptPlugin.md)
- [/System/Library/Frameworks/CoreLocationUI.framework/XPCServices/com.apple.corelocation.locationUI.xpc/com.apple.corelocation.locationUI](MACHOS/com.apple.corelocation.locationUI.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/Support/com.apple.spotlight.IndexAgent](MACHOS/com.apple.spotlight.IndexAgent.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/spotlightknowledged](MACHOS/spotlightknowledged.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenterMobileHelper](MACHOS/CommCenterMobileHelper.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenterRootHelper](MACHOS/CommCenterRootHelper.md)
- [/System/Library/Frameworks/FamilyControls.framework/FamilyControlsAgent](MACHOS/FamilyControlsAgent.md)
- [/System/Library/Frameworks/IdentityLookup.framework/XPCServices/com.apple.IdentityLookup.MessageFilter.xpc/com.apple.IdentityLookup.MessageFilter](MACHOS/com.apple.IdentityLookup.MessageFilter.md)
- [/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond](MACHOS/managedappdistributiond.md)
- [/System/Library/Frameworks/ManagedSettings.framework/ManagedSettingsAgent](MACHOS/ManagedSettingsAgent.md)
- [/System/Library/Frameworks/ShazamKit.framework/shazamd](MACHOS/shazamd.md)
- [/System/Library/Frameworks/StoreKit.framework/PlugIns/SKAskPermissionExtension.appex/SKAskPermissionExtension](MACHOS/SKAskPermissionExtension.md)
- [/System/Library/Frameworks/StoreKit.framework/Support/storekitd](MACHOS/storekitd.md)
- [/System/Library/Frameworks/SystemConfiguration.framework/get-network-info](MACHOS/get-network-info.md)
- [/System/Library/Frameworks/UIKit.framework/PlugIns/com.apple.UIKit.ColorPicker.appex/com.apple.UIKit.ColorPicker](MACHOS/com.apple.UIKit.ColorPicker.md)
- [/System/Library/Frameworks/UIKit.framework/PlugIns/com.apple.UIKit.screenpicker.appex/com.apple.UIKit.screenpicker](MACHOS/com.apple.UIKit.screenpicker.md)
- [/System/Library/Frameworks/VideoToolbox.framework/XPCServices/videodecodeservice.xpc/videodecodeservice](MACHOS/videodecodeservice.md)
- [/System/Library/HIDPlugins/ServicePlugins/HSTouchHIDService.plugin/HSTouchHIDService](MACHOS/HSTouchHIDService.md)
- [/System/Library/LocationBundles/AppGenius.bundle/AppGenius](MACHOS/AppGenius.md)
- [/System/Library/LocationBundles/CompassCalibration.bundle/CompassCalibration](MACHOS/CompassCalibration.md)
- [/System/Library/LocationBundles/IonosphereHarvest.bundle/IonosphereHarvest](MACHOS/IonosphereHarvest.md)
- [/System/Library/LocationBundles/LocationFenceSync.bundle/LocationFenceSync](MACHOS/LocationFenceSync.md)
- [/System/Library/LocationBundles/MotionCalibration.bundle/MotionCalibration](MACHOS/MotionCalibration.md)
- [/System/Library/LocationBundles/PLAMonitor.bundle/PLAMonitor](MACHOS/PLAMonitor.md)
- [/System/Library/Messages/PlugIns/RCS.imservice/RCS](MACHOS/RCS.md)
- [/System/Library/Messages/iMessageBalloons/ASMessagesProvider.bundle/ASMessagesProvider](MACHOS/ASMessagesProvider.md)
- [/System/Library/NanoPreferenceBundles/Applications/NanoPassbookBridgeSettings.bundle/NanoPassbookBridgeSettings](MACHOS/NanoPassbookBridgeSettings.md)
- [/System/Library/NanoPreferenceBundles/General/CompanionInternationalSettings.bundle/CompanionInternationalSettings](MACHOS/CompanionInternationalSettings.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKMagmaFaceBundleCompanion.bundle/NTKMagmaFaceBundleCompanion](MACHOS/NTKMagmaFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKRenegadeFaceBundleCompanion.bundle/NTKRenegadeFaceBundleCompanion](MACHOS/NTKRenegadeFaceBundleCompanion.md)
- [/System/Library/PreferenceBundles/AccessibilitySettings.bundle/AccessibilitySettings](MACHOS/AccessibilitySettings.md)
- [/System/Library/PreferenceBundles/AccountSettings/icloudMailSettings.bundle/icloudMailSettings](MACHOS/icloudMailSettings.md)
- [/System/Library/PreferenceBundles/AdAttributionKitDeveloperSettings.bundle/AdAttributionKitDeveloperSettings](MACHOS/AdAttributionKitDeveloperSettings.md)
- [/System/Library/PreferenceBundles/AirDropSettings.bundle/AirDropSettings](MACHOS/AirDropSettings.md)
- [/System/Library/PreferenceBundles/AppInstallationSettings.bundle/AppInstallationSettings](MACHOS/AppInstallationSettings.md)
- [/System/Library/PreferenceBundles/CameraSettings.bundle/CameraSettings](MACHOS/CameraSettings.md)
- [/System/Library/PreferenceBundles/CarKitSettings.bundle/CarKitSettings](MACHOS/CarKitSettings.md)
- [/System/Library/PreferenceBundles/GameControlleriOSSettings.bundle/GameControlleriOSSettings](MACHOS/GameControlleriOSSettings.md)
- [/System/Library/PreferenceBundles/JournalSettings.bundle/JournalSettings](MACHOS/JournalSettings.md)
- [/System/Library/PreferenceBundles/MapsSettings.bundle/MapsSettings](MACHOS/MapsSettings.md)
- [/System/Library/PreferenceBundles/MobileSafariSettings.bundle/MobileSafariSettings](MACHOS/MobileSafariSettings.md)
- [/System/Library/PreferenceBundles/MobileStoreSettings.bundle/MobileStoreSettings](MACHOS/MobileStoreSettings.md)
- [/System/Library/PreferenceBundles/MultitaskingAndGesturesSettings.bundle/MultitaskingAndGesturesSettings](MACHOS/MultitaskingAndGesturesSettings.md)
- [/System/Library/PreferenceBundles/NotificationsSettings.bundle/NotificationsSettings](MACHOS/NotificationsSettings.md)
- [/System/Library/PreferenceBundles/PasswordsSettings.bundle/PasswordsSettings](MACHOS/PasswordsSettings.md)
- [/System/Library/PreferenceBundles/PodcastsSettingsPlugin.bundle/PodcastsSettingsPlugin](MACHOS/PodcastsSettingsPlugin.md)
- [/System/Library/PreferenceBundles/PrivacyAndSecuritySettings.bundle/PrivacyAndSecuritySettings](MACHOS/PrivacyAndSecuritySettings.md)
- [/System/Library/PreferenceBundles/SiriMessagesSettings.bundle/SiriMessagesSettings](MACHOS/SiriMessagesSettings.md)
- [/System/Library/PreferenceBundles/StorageSettingsUI.bundle/StorageSettingsUI](MACHOS/StorageSettingsUI.md)
- [/System/Library/PreferenceBundles/TetsuoNotifications.bundle/TetsuoNotifications](MACHOS/TetsuoNotifications.md)
- [/System/Library/PreferenceBundles/WallpaperSettings.bundle/WallpaperSettings](MACHOS/WallpaperSettings.md)
- [/System/Library/PrivateFrameworks/ABMHelper.framework/Support/abm-helper](MACHOS/abm-helper.md)
- [/System/Library/PrivateFrameworks/ASOctaneSupport.framework/XPCServices/ASOctaneSupportXPCService.xpc/ASOctaneSupportXPCService](MACHOS/ASOctaneSupportXPCService.md)
- [/System/Library/PrivateFrameworks/AccessoryOOBBTPairing.framework/XPCServices/ACCBluetoothPairingService.xpc/ACCBluetoothPairingService](MACHOS/ACCBluetoothPairingService.md)
- [/System/Library/PrivateFrameworks/ActionPredictionHeuristics.framework/XPCServices/HeuristicInterpreter.xpc/HeuristicInterpreter](MACHOS/HeuristicInterpreter.md)
- [/System/Library/PrivateFrameworks/AppInstallationMetrics.framework/Support/appinstallationmetricsd](MACHOS/appinstallationmetricsd.md)
- [/System/Library/PrivateFrameworks/AppPredictionFoundation.framework/XPCServices/AppPredictionIntentsHelperService.xpc/AppPredictionIntentsHelperService](MACHOS/AppPredictionIntentsHelperService.md)
- [/System/Library/PrivateFrameworks/AppStoreComponents.framework/Support/appstorecomponentsd](MACHOS/appstorecomponentsd.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored](MACHOS/appstored.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/amsaccountsd](MACHOS/amsaccountsd.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/Extensions/UtilityExtension.appex/UtilityExtension](MACHOS/UtilityExtension.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/amsengagementd](MACHOS/amsengagementd.md)
- [/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/XPCServices/ANECompilerService.xpc/ANECompilerService](MACHOS/ANECompilerService.md)
- [/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/XPCServices/ANEStorageMaintainer.xpc/ANEStorageMaintainer](MACHOS/ANEStorageMaintainer.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd](MACHOS/assistantd.md)
- [/System/Library/PrivateFrameworks/AuthKit.framework/akd](MACHOS/akd.md)
- [/System/Library/PrivateFrameworks/BookDataStore.framework/Support/bookdatastored](MACHOS/bookdatastored.md)
- [/System/Library/PrivateFrameworks/BookLibraryCore.framework/Support/bookassetd](MACHOS/bookassetd.md)
- [/System/Library/PrivateFrameworks/BusinessChatService.framework/businessservicesd](MACHOS/businessservicesd.md)
- [/System/Library/PrivateFrameworks/CMCapture.framework/PlugIns/CMCaptureDiagnosticExtension.appex/CMCaptureDiagnosticExtension](MACHOS/CMCaptureDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/ClipServices.framework/clipserviced](MACHOS/clipserviced.md)
- [/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/Support/cloudphotod](MACHOS/cloudphotod.md)
- [/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/XPCServices/com.apple.Photos.CPLDiagnose.xpc/com.apple.Photos.CPLDiagnose](MACHOS/com.apple.Photos.CPLDiagnose.md)
- [/System/Library/PrivateFrameworks/CloudSharing.framework/XPCServices/SPIHelper-iOS.xpc/SPIHelper-iOS](MACHOS/SPIHelper-iOS.md)
- [/System/Library/PrivateFrameworks/CloudSharingUI.framework/PlugIns/com.apple.CloudSharingUI.CloudSharing.appex/com.apple.CloudSharingUI.CloudSharing](MACHOS/com.apple.CloudSharingUI.CloudSharing.md)
- [/System/Library/PrivateFrameworks/CloudTelemetry.framework/XPCServices/CloudTelemetryService.xpc/CloudTelemetryService](MACHOS/CloudTelemetryService.md)
- [/System/Library/PrivateFrameworks/CompanionCamera.framework/Support/companioncamerad](MACHOS/companioncamerad.md)
- [/System/Library/PrivateFrameworks/CoreAccessories.framework/Support/accessoryd](MACHOS/accessoryd.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/parsec-fbf](MACHOS/parsec-fbf.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/parsecd](MACHOS/parsecd.md)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd](MACHOS/corespeechd.md)
- [/System/Library/PrivateFrameworks/CoreThreadRadio.framework/threadradiod](MACHOS/threadradiod.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/XPCServices/com.apple.dt.DTMLModelRunnerService.xpc/com.apple.dt.DTMLModelRunnerService](MACHOS/com.apple.dt.DTMLModelRunnerService.md)
- [/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/DesktopServicesHelper](MACHOS/DesktopServicesHelper.md)
- [/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/XPCServices/ArchiveService.xpc/ArchiveService](MACHOS/ArchiveService.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Cellular.appex/com.apple.DiagnosticExtensions.Cellular](MACHOS/com.apple.DiagnosticExtensions.Cellular.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Telephony.appex/com.apple.DiagnosticExtensions.Telephony](MACHOS/com.apple.DiagnosticExtensions.Telephony.md)
- [/System/Library/PrivateFrameworks/DiskImages2.framework/XPCServices/diskimagescontroller.xpc/diskimagescontroller](MACHOS/diskimagescontroller.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAppPopover.appex/RecentsAppPopover](MACHOS/RecentsAppPopover.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAvocado.appex/RecentsAvocado](MACHOS/RecentsAvocado.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/SaveToFiles.appex/SaveToFiles](MACHOS/SaveToFiles.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/com.apple.DocumentManager.Service.appex/com.apple.DocumentManager.Service](MACHOS/com.apple.DocumentManager.Service.md)
- [/System/Library/PrivateFrameworks/EmailDaemon.framework/maild](MACHOS/maild.md)
- [/System/Library/PrivateFrameworks/FinHealth.framework/ClientTools/finhealthclient](MACHOS/finhealthclient.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/Resources/UITypographyPanel.bundle/UITypographyPanel](MACHOS/UITypographyPanel.md)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/PlugIns/GameCenterMatchmakerExtension.appex/GameCenterMatchmakerExtension](MACHOS/GameCenterMatchmakerExtension.md)
- [/System/Library/PrivateFrameworks/GeoServices.framework/MapsOfflineService.bundle/MapsOfflineService](MACHOS/MapsOfflineService.md)
- [/System/Library/PrivateFrameworks/HomePlatformSettingsUI.framework/PlugIns/HPSUIViewService.appex/HPSUIViewService](MACHOS/HPSUIViewService.md)
- [/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd](MACHOS/identityservicesd.md)
- [/System/Library/PrivateFrameworks/InstallCoordination.framework/Support/installcoordinationd](MACHOS/installcoordinationd.md)
- [/System/Library/PrivateFrameworks/MFAAuthentication.framework/XPCServices/MFAANetwork.xpc/MFAANetwork](MACHOS/MFAANetwork.md)
- [/System/Library/PrivateFrameworks/MLKit.framework/PlugIns/com.apple.MLKit.MLModelPreview.appex/com.apple.MLKit.MLModelPreview](MACHOS/com.apple.MLKit.MLModelPreview.md)
- [/System/Library/PrivateFrameworks/MLKit.framework/PlugIns/com.apple.MLKit.MLPackagePreview.appex/com.apple.MLKit.MLPackagePreview](MACHOS/com.apple.MLKit.MLPackagePreview.md)
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd](MACHOS/mediaanalysisd.md)
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd-service](MACHOS/mediaanalysisd-service.md)
- [/System/Library/PrivateFrameworks/MediaRemote.framework/Support/mediaremoted](MACHOS/mediaremoted.md)
- [/System/Library/PrivateFrameworks/MediaServicesBroker.framework/PlugIns/MediaSetupViewService.appex/MediaSetupViewService](MACHOS/MediaSetupViewService.md)
- [/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/XPCServices/MessagesBlastDoorService.xpc/MessagesBlastDoorService](MACHOS/MessagesBlastDoorService.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/EAUpdaterService.xpc/EAUpdaterService](MACHOS/EAUpdaterService.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceDFU.xpc/UARPUpdaterServiceDFU](MACHOS/UARPUpdaterServiceDFU.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceLegacyAudio.xpc/UARPUpdaterServiceLegacyAudio](MACHOS/UARPUpdaterServiceLegacyAudio.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/backupd](MACHOS/backupd.md)
- [/System/Library/PrivateFrameworks/MusicLibrary.framework/Support/medialibraryd](MACHOS/medialibraryd.md)
- [/System/Library/PrivateFrameworks/NanoPreferencesSync.framework/nanoprefsyncd](MACHOS/nanoprefsyncd.md)
- [/System/Library/PrivateFrameworks/NeighborhoodActivityConduit.framework/XPCServices/com.apple.NeighborhoodActivityConduitService.xpc/com.apple.NeighborhoodActivityConduitService](MACHOS/com.apple.NeighborhoodActivityConduitService.md)
- [/System/Library/PrivateFrameworks/OnDeviceStorage.framework/Support/amsondevicestoraged](MACHOS/amsondevicestoraged.md)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/passd](MACHOS/passd.md)
- [/System/Library/PrivateFrameworks/PowerLog.framework/XPCServices/PerfPowerTelemetryClientRegistrationService.xpc/PerfPowerTelemetryClientRegistrationService](MACHOS/PerfPowerTelemetryClientRegistrationService.md)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/XPCServices/PerfPowerTelemetryClientRegistrationService.xpc/PerfPowerTelemetryClientRegistrationService](MACHOS/PerfPowerTelemetryClientRegistrationService.md)
- [/System/Library/PrivateFrameworks/PreviewsOSSupport.framework/Support/previewsd](MACHOS/previewsd.md)
- [/System/Library/PrivateFrameworks/PrivateCloudCompute.framework/privatecloudcomputed.app/privatecloudcomputed](MACHOS/privatecloudcomputed.md)
- [/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeAgent](MACHOS/ScreenTimeAgent.md)
- [/System/Library/PrivateFrameworks/Search.framework/PlugIns/SpotlightDiagnostic.appex/SpotlightDiagnostic](MACHOS/SpotlightDiagnostic.md)
- [/System/Library/PrivateFrameworks/Search.framework/searchd](MACHOS/searchd.md)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningAnalytics.framework/PlugIns/SiriUserFeedbackLearningUniversalSuggestionsPlugin.appex/SiriUserFeedbackLearningUniversalSuggestionsPlugin](MACHOS/SiriUserFeedbackLearningUniversalSuggestionsPlugin.md)
- [/System/Library/PrivateFrameworks/SiriTTSService.framework/sirittsd](MACHOS/sirittsd.md)
- [/System/Library/PrivateFrameworks/SonicKit.framework/PlugIns/SonicDiagnostics.appex/SonicDiagnostics](MACHOS/SonicDiagnostics.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd](MACHOS/callservicesd.md)
- [/System/Library/PrivateFrameworks/TranslationUIServices.framework/PlugIns/TranslationUIService.appex/TranslationUIService](MACHOS/TranslationUIService.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/TextEffectsCatalog.bundle/TextEffectsCatalog](MACHOS/TextEffectsCatalog.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/XPCServices/SecureControlService.xpc/SecureControlService](MACHOS/SecureControlService.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/XPCServices/com.apple.UIKit.KeyboardManagement.xpc/com.apple.UIKit.KeyboardManagement](MACHOS/com.apple.UIKit.KeyboardManagement.md)
- [/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTrackingAgent](MACHOS/UsageTrackingAgent.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/ExtragalacticPoster.appex/ExtragalacticPoster](MACHOS/ExtragalacticPoster.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/RhizomePoster.appex/RhizomePoster](MACHOS/RhizomePoster.md)
- [/System/Library/PrivateFrameworks/WeatherDaemon.framework/weatherd](MACHOS/weatherd.md)
- [/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/BackgroundShortcutRunner.xpc/BackgroundShortcutRunner](MACHOS/BackgroundShortcutRunner.md)
- [/System/Library/PrivateFrameworks/iTunesStore.framework/Support/itunesstored](MACHOS/itunesstored.md)
- [/System/Library/Settings/InstalledApps.settings/InstalledApps](MACHOS/InstalledApps.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/AudioSuggestionsPlugin.bundle/AudioSuggestionsPlugin](MACHOS/AudioSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/HomeAutomationSiriSuggestions.bundle/HomeAutomationSiriSuggestions](MACHOS/HomeAutomationSiriSuggestions.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriLinkSuggestionsPlugin.bundle/SiriLinkSuggestionsPlugin](MACHOS/SiriLinkSuggestionsPlugin.md)
- [/System/Library/Snippets/UIPlugins/SiriLinkUIPlugin.bundle/SiriLinkUIPlugin](MACHOS/SiriLinkUIPlugin.md)
- [/System/Library/SyncBundles/AirFair.syncBundle/AirFair](MACHOS/AirFair.md)
- [/System/Library/SyncBundles/AirFair2.syncBundle/AirFair2](MACHOS/AirFair2.md)
- [/System/Library/SyncBundles/MusicLibrary.syncBundle/MusicLibrary](MACHOS/MusicLibrary.md)
- [/System/Library/SystemConfiguration/IPConfiguration.bundle/IPConfiguration](MACHOS/IPConfiguration.md)
- [/System/Library/UserEventPlugins/AHTUserEventAgent.plugin/AHTUserEventAgent](MACHOS/AHTUserEventAgent.md)
- [/System/Library/UserNotifications/Bundles/com.apple.Siri.ActionPredictionNotifications.bundle/com.apple.Siri.ActionPredictionNotifications](MACHOS/com.apple.Siri.ActionPredictionNotifications.md)
- [/System/Library/Video/Plug-Ins/AppleVideoEncoder.bundle/AppleVideoEncoder](MACHOS/AppleVideoEncoder.md)
- [/System/Library/VideoProcessors/ColourConstancyV1.bundle/ColourConstancyV1](MACHOS/ColourConstancyV1.md)
- [/System/Library/VideoProcessors/SemanticStyleV1.bundle/SemanticStyleV1](MACHOS/SemanticStyleV1.md)
- [/System/Library/VideoProcessors/SmartStyleV1.bundle/SmartStyleV1](MACHOS/SmartStyleV1.md)
- [/System/Library/VideoProcessors/SuperResolutionV2.bundle/SuperResolutionV2](MACHOS/SuperResolutionV2.md)
- [/System/Library/VideoProcessors/VideoDeghostingV1.bundle/VideoDeghostingV1](MACHOS/VideoDeghostingV1.md)
- [/System/Library/VideoProcessors/VideoDeghostingV2.bundle/VideoDeghostingV2](MACHOS/VideoDeghostingV2.md)
- [/System/Library/VideoProcessors/VideoStabilizationV2.bundle/VideoStabilizationV2](MACHOS/VideoStabilizationV2.md)
- [/private/var/staged_system_apps/AppStore.app/AppStore](MACHOS/AppStore.md)
- [/private/var/staged_system_apps/AppStore.app/PlugIns/AppStoreWidgetsExtension.appex/AppStoreWidgetsExtension](MACHOS/AppStoreWidgetsExtension.md)
- [/private/var/staged_system_apps/AppleTV.app/PlugIns/TVWidgetExtension.appex/TVWidgetExtension](MACHOS/TVWidgetExtension.md)
- [/private/var/staged_system_apps/AppleVisionProApp.app/AppleVisionProApp](MACHOS/AppleVisionProApp.md)
- [/private/var/staged_system_apps/Books.app/Books](MACHOS/Books.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/AEBookPlugins.framework/AEBookPlugins](MACHOS/AEBookPlugins.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookAnalytics.framework/BookAnalytics](MACHOS/BookAnalytics.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookEPUB.framework/BookEPUB](MACHOS/BookEPUB.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookStoreUI.framework/BookStoreUI](MACHOS/BookStoreUI.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BooksPersonalization.framework/BooksPersonalization](MACHOS/BooksPersonalization.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BooksUI.framework/BooksUI](MACHOS/BooksUI.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/JSApp.framework/JSApp](MACHOS/JSApp.md)
- [/private/var/staged_system_apps/Books.app/PlugIns/BooksWidgetExtension.appex/BooksWidgetExtension](MACHOS/BooksWidgetExtension.md)
- [/private/var/staged_system_apps/Bridge.app/Bridge](MACHOS/Bridge.md)
- [/private/var/staged_system_apps/Calculator.app/Calculator](MACHOS/Calculator.md)
- [/private/var/staged_system_apps/FaceTime.app/FaceTime](MACHOS/FaceTime.md)
- [/private/var/staged_system_apps/Files.app/Files](MACHOS/Files.md)
- [/private/var/staged_system_apps/FindMy.app/FindMy](MACHOS/FindMy.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyNotificationsService.appex/FindMyNotificationsService](MACHOS/FindMyNotificationsService.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyWidgetItems.appex/FindMyWidgetItems](MACHOS/FindMyWidgetItems.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyWidgetPeople.appex/FindMyWidgetPeople](MACHOS/FindMyWidgetPeople.md)
- [/private/var/staged_system_apps/Fitness.app/Fitness](MACHOS/Fitness.md)
- [/private/var/staged_system_apps/Freeform.app/Extensions/USDRendererExtension.appex/USDRendererExtension](MACHOS/USDRendererExtension.md)
- [/private/var/staged_system_apps/Freeform.app/Freeform](MACHOS/Freeform.md)
- [/private/var/staged_system_apps/Freeform.app/PlugIns/FreeformWidgetKitExtension.appex/FreeformWidgetKitExtension](MACHOS/FreeformWidgetKitExtension.md)
- [/private/var/staged_system_apps/Health.app/Health](MACHOS/Health.md)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeDiagnosticExtension.appex/HomeDiagnosticExtension](MACHOS/HomeDiagnosticExtension.md)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeWidget.appex/HomeWidget](MACHOS/HomeWidget.md)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeWidgetLockScreen.appex/HomeWidgetLockScreen](MACHOS/HomeWidgetLockScreen.md)
- [/private/var/staged_system_apps/Journal.app/Journal](MACHOS/Journal.md)
- [/private/var/staged_system_apps/Journal.app/PlugIns/JournalShareExtension.appex/JournalShareExtension](MACHOS/JournalShareExtension.md)
- [/private/var/staged_system_apps/Journal.app/PlugIns/JournalWidgets.appex/JournalWidgets](MACHOS/JournalWidgets.md)
- [/private/var/staged_system_apps/Journal.app/PlugIns/JournalWidgetsSecure.appex/JournalWidgetsSecure](MACHOS/JournalWidgetsSecure.md)
- [/private/var/staged_system_apps/Maps.app/Maps](MACHOS/Maps.md)
- [/private/var/staged_system_apps/Maps.app/PlugIns/GeneralMapsWidget.appex/GeneralMapsWidget](MACHOS/GeneralMapsWidget.md)
- [/private/var/staged_system_apps/Measure.app/Measure](MACHOS/Measure.md)
- [/private/var/staged_system_apps/MobileMail.app/MobileMail](MACHOS/MobileMail.md)
- [/private/var/staged_system_apps/MobileMail.app/PlugIns/MailQuickLookExtension.appex/MailQuickLookExtension](MACHOS/MailQuickLookExtension.md)
- [/private/var/staged_system_apps/MobileMail.app/PlugIns/MailWidgetExtension.appex/MailWidgetExtension](MACHOS/MailWidgetExtension.md)
- [/private/var/staged_system_apps/MobileNotes.app/MobileNotes](MACHOS/MobileNotes.md)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.SharingExtension.appex/com.apple.mobilenotes.SharingExtension](MACHOS/com.apple.mobilenotes.SharingExtension.md)
- [/private/var/staged_system_apps/MobileSafari.app/PlugIns/SafariWidgetExtension.appex/SafariWidgetExtension](MACHOS/SafariWidgetExtension.md)
- [/private/var/staged_system_apps/MobileTimer.app/PlugIns/WorldClockWidget.appex/WorldClockWidget](MACHOS/WorldClockWidget.md)
- [/private/var/staged_system_apps/Music.app/Frameworks/MusicApplication.framework/MusicApplication](MACHOS/MusicApplication.md)
- [/private/var/staged_system_apps/Music.app/Frameworks/MusicApplication.framework/XPCServices/MusicScriptUpdateService.xpc/MusicScriptUpdateService](MACHOS/MusicScriptUpdateService.md)
- [/private/var/staged_system_apps/Music.app/Music](MACHOS/Music.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/MusicMessagesApp.appex/MusicMessagesApp](MACHOS/MusicMessagesApp.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/MusicWidgets.appex/MusicWidgets](MACHOS/MusicWidgets.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsTag.appex/NewsTag](MACHOS/NewsTag.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsToday2.appex/NewsToday2](MACHOS/NewsToday2.md)
- [/private/var/staged_system_apps/Passbook.app/PlugIns/PassbookLockedWidgetsExtension.appex/PassbookLockedWidgetsExtension](MACHOS/PassbookLockedWidgetsExtension.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/PodcastsTranscripts.framework/PodcastsTranscripts](MACHOS/PodcastsTranscripts.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/ShelfKit.framework/ShelfKit](MACHOS/ShelfKit.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/ShelfKitCollectionViews.framework/ShelfKitCollectionViews](MACHOS/ShelfKitCollectionViews.md)
- [/private/var/staged_system_apps/Podcasts.app/PlugIns/com.apple.podcasts.SpotlightIndexExtension.appex/com.apple.podcasts.SpotlightIndexExtension](MACHOS/com.apple.podcasts.SpotlightIndexExtension.md)
- [/private/var/staged_system_apps/Podcasts.app/Podcasts](MACHOS/Podcasts.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersIntentsExtension.appex/RemindersIntentsExtension](MACHOS/RemindersIntentsExtension.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersIntentsUIExtension.appex/RemindersIntentsUIExtension](MACHOS/RemindersIntentsUIExtension.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersWidgetExtension.appex/RemindersWidgetExtension](MACHOS/RemindersWidgetExtension.md)
- [/private/var/staged_system_apps/Reminders.app/Reminders](MACHOS/Reminders.md)
- [/private/var/staged_system_apps/SequoiaTranslator.app/SequoiaTranslator](MACHOS/SequoiaTranslator.md)
- [/private/var/staged_system_apps/Shortcuts.app/PlugIns/ShortcutsWidgetExtension.appex/ShortcutsWidgetExtension](MACHOS/ShortcutsWidgetExtension.md)
- [/private/var/staged_system_apps/Shortcuts.app/Shortcuts](MACHOS/Shortcuts.md)
- [/private/var/staged_system_apps/Stocks.app/PlugIns/StocksWidget.appex/StocksWidget](MACHOS/StocksWidget.md)
- [/private/var/staged_system_apps/Tips.app/Tips](MACHOS/Tips.md)
- [/private/var/staged_system_apps/VoiceMemos.app/VoiceMemos](MACHOS/VoiceMemos.md)
- [/private/var/staged_system_apps/Weather.app/PlugIns/WeatherPoster.appex/WeatherPoster](MACHOS/WeatherPoster.md)
- [/private/var/staged_system_apps/Weather.app/PlugIns/WeatherWidget.appex/WeatherWidget](MACHOS/WeatherWidget.md)
- [/private/var/staged_system_apps/Weather.app/Weather](MACHOS/Weather.md)
- [/sbin/launchd](MACHOS/launchd.md)
- [/usr/bin/IOMFB_FDR_Loader](MACHOS/IOMFB_FDR_Loader.md)
- [/usr/bin/abmlite](MACHOS/abmlite.md)
- [/usr/bin/csfdiagnose](MACHOS/csfdiagnose.md)
- [/usr/bin/swift-inspect](MACHOS/swift-inspect.md)
- [/usr/lib/dyld](MACHOS/dyld.md)
- [/usr/lib/libCoreFP.dylib](MACHOS/libCoreFP.dylib.md)
- [/usr/lib/libmobileassetd.dylib](MACHOS/libmobileassetd.dylib.md)
- [/usr/lib/libramrod.dylib](MACHOS/libramrod.dylib.md)
- [/usr/libexec/BackupAgent2](MACHOS/BackupAgent2.md)
- [/usr/libexec/SidecarRelay](MACHOS/SidecarRelay.md)
- [/usr/libexec/aned](MACHOS/aned.md)
- [/usr/libexec/anomalydetectiond](MACHOS/anomalydetectiond.md)
- [/usr/libexec/appleaccountd](MACHOS/appleaccountd.md)
- [/usr/libexec/applekeystored](MACHOS/applekeystored.md)
- [/usr/libexec/asd](MACHOS/asd.md)
- [/usr/libexec/assessmentagent](MACHOS/assessmentagent.md)
- [/usr/libexec/audioaccessoryd](MACHOS/audioaccessoryd.md)
- [/usr/libexec/audioanalyticsd](MACHOS/audioanalyticsd.md)
- [/usr/libexec/backgroundassets.user](MACHOS/backgroundassets.user.md)
- [/usr/libexec/bluetoothuserd](MACHOS/bluetoothuserd.md)
- [/usr/libexec/bootpd](MACHOS/bootpd.md)
- [/usr/libexec/cameracaptured](MACHOS/cameracaptured.md)
- [/usr/libexec/caraccessoryd](MACHOS/caraccessoryd.md)
- [/usr/libexec/carkitd](MACHOS/carkitd.md)
- [/usr/libexec/checkpointd](MACHOS/checkpointd.md)
- [/usr/libexec/coreidvd](MACHOS/coreidvd.md)
- [/usr/libexec/dasd](MACHOS/dasd.md)
- [/usr/libexec/debugserver](MACHOS/debugserver.md)
- [/usr/libexec/demod](MACHOS/demod.md)
- [/usr/libexec/dhcp6d](MACHOS/dhcp6d.md)
- [/usr/libexec/diskarbitrationd](MACHOS/diskarbitrationd.md)
- [/usr/libexec/diskimagesiod](MACHOS/diskimagesiod.md)
- [/usr/libexec/dmd](MACHOS/dmd.md)
- [/usr/libexec/dockaccessoryd](MACHOS/dockaccessoryd.md)
- [/usr/libexec/driverkitd](MACHOS/driverkitd.md)
- [/usr/libexec/duetexpertd](MACHOS/duetexpertd.md)
- [/usr/libexec/eligibilityd](MACHOS/eligibilityd.md)
- [/usr/libexec/findmydeviced](MACHOS/findmydeviced.md)
- [/usr/libexec/findmylocated](MACHOS/findmylocated.md)
- [/usr/libexec/fskitd](MACHOS/fskitd.md)
- [/usr/libexec/gamed](MACHOS/gamed.md)
- [/usr/libexec/gamepolicyd](MACHOS/gamepolicyd.md)
- [/usr/libexec/icloudmailagent](MACHOS/icloudmailagent.md)
- [/usr/libexec/idcredd](MACHOS/idcredd.md)
- [/usr/libexec/linkd](MACHOS/linkd.md)
- [/usr/libexec/locationd](MACHOS/locationd.md)
- [/usr/libexec/lockdownd](MACHOS/lockdownd.md)
- [/usr/libexec/lskdd](MACHOS/lskdd.md)
- [/usr/libexec/mediaparserd](MACHOS/mediaparserd.md)
- [/usr/libexec/mediaplaybackd](MACHOS/mediaplaybackd.md)
- [/usr/libexec/merchantd](MACHOS/merchantd.md)
- [/usr/libexec/mlhostd](MACHOS/mlhostd.md)
- [/usr/libexec/mobileactivationd](MACHOS/mobileactivationd.md)
- [/usr/libexec/mobilerepaird](MACHOS/mobilerepaird.md)
- [/usr/libexec/modelmanagerd](MACHOS/modelmanagerd.md)
- [/usr/libexec/momentsd](MACHOS/momentsd.md)
- [/usr/libexec/nanoregistryd](MACHOS/nanoregistryd.md)
- [/usr/libexec/nearbyd](MACHOS/nearbyd.md)
- [/usr/libexec/nehelper](MACHOS/nehelper.md)
- [/usr/libexec/networkserviceproxy](MACHOS/networkserviceproxy.md)
- [/usr/libexec/nfcd](MACHOS/nfcd.md)
- [/usr/libexec/nsurlsessiond](MACHOS/nsurlsessiond.md)
- [/usr/libexec/online-auth-agent](MACHOS/online-auth-agent.md)
- [/usr/libexec/photosfaced](MACHOS/photosfaced.md)
- [/usr/libexec/promotedcontentd](MACHOS/promotedcontentd.md)
- [/usr/libexec/proximitycontrold](MACHOS/proximitycontrold.md)
- [/usr/libexec/ptpd](MACHOS/ptpd.md)
- [/usr/libexec/rapportd](MACHOS/rapportd.md)
- [/usr/libexec/remindd](MACHOS/remindd.md)
- [/usr/libexec/remotepairingdeviced](MACHOS/remotepairingdeviced.md)
- [/usr/libexec/rtcreportingd](MACHOS/rtcreportingd.md)
- [/usr/libexec/runningboardd](MACHOS/runningboardd.md)
- [/usr/libexec/searchpartyd](MACHOS/searchpartyd.md)
- [/usr/libexec/seserviced](MACHOS/seserviced.md)
- [/usr/libexec/sharingd](MACHOS/sharingd.md)
- [/usr/libexec/sportsd](MACHOS/sportsd.md)
- [/usr/libexec/swtransparencyd](MACHOS/swtransparencyd.md)
- [/usr/libexec/sysdiagnose_helper](MACHOS/sysdiagnose_helper.md)
- [/usr/libexec/sysdiagnosed](MACHOS/sysdiagnosed.md)
- [/usr/libexec/systemservicemonitord](MACHOS/systemservicemonitord.md)
- [/usr/libexec/terminusd](MACHOS/terminusd.md)
- [/usr/libexec/transparencyd](MACHOS/transparencyd.md)
- [/usr/libexec/trustd](MACHOS/trustd.md)
- [/usr/libexec/usermanagerd](MACHOS/usermanagerd.md)
- [/usr/libexec/videocodecd](MACHOS/videocodecd.md)
- [/usr/libexec/visioncompaniond](MACHOS/visioncompaniond.md)
- [/usr/libexec/webbookmarksd](MACHOS/webbookmarksd.md)
- [/usr/libexec/wifianalyticsd](MACHOS/wifianalyticsd.md)
- [/usr/sbin/BTLEServer](MACHOS/BTLEServer.md)
- [/usr/sbin/BlueTool](MACHOS/BlueTool.md)
- [/usr/sbin/WirelessRadioManagerd](MACHOS/WirelessRadioManagerd.md)
- [/usr/sbin/bluetoothd](MACHOS/bluetoothd.md)
- [/usr/sbin/fairplayd.H2](MACHOS/fairplayd.H2.md)
- [/usr/sbin/wifid](MACHOS/wifid.md)

</details>

### 🔑 Entitlements

- [Entitlements DIFF](Entitlements.md)

## Firmware

### ⬆️ Updated (5)

<details>
  <summary><i>View Updated</i></summary>

#### AppleAVE2FW_H17.im4p

>  `AppleAVE2FW_H17.im4p`

```diff

 
-  __TEXT.__text: 0xf3c98
+  __TEXT.__text: 0xf39b8
   __TEXT._rtk_mtab: 0x2d0
   __TEXT.__const: 0x22794
-  __TEXT.__cstring: 0x140f7
+  __TEXT.__cstring: 0x14115
   __TEXT.__constructor: 0x0
   __TEXT.__chain_starts: 0x0
   __DATA.__const: 0x2a20
CStrings:
+ "%d %d %d %d %d %d %d %hhu %d %hhu %d %hhu "
+ "%d | %d %d | %d %d | %hhu %d %hhu %d "
+ "%s::%s:%d  %d F %d Type %d POC %d | %d %d | S0 %d %hhu %d %hhu | S1 %d %hhu"
+ "%s::%s:%d %d F %d Type %d POC %d | %d %d | %d %hhu %d %hhu"
+ "%s::%s:%d i %d PicOrderCntVal %d UsedByCurrPicS0 %hhu DeltaPocS0 %d"
+ "%s::%s:%d i %d PicOrderCntVal %d UsedByCurrPicS1 %hhu DeltaPocS1 %d"
+ "%s::%s:%d ptr->UsedByCurrPicS0[%d] %hhu"
+ "8002.41.0"
+ "RPSparams.strps.rps[%d].used_by_curr_pic_s0_flag[%d]  %hhu\n"
+ "RPSparams.strps.rps[%d].used_by_curr_pic_s1_flag[%d]  %hhu\n"
- "%d %d %d %d %d %d %d %d %d %d %d %d "
- "%d | %d %d | %d %d | %d %d %d %d "
- "%s::%s:%d  %d F %d Type %d POC %d | %d %d | S0 %d %d %d %d | S1 %d %d"
- "%s::%s:%d %d F %d Type %d POC %d | %d %d | %d %d %d %d"
- "%s::%s:%d i %d PicOrderCntVal %d UsedByCurrPicS0 %d DeltaPocS0 %d"
- "%s::%s:%d i %d PicOrderCntVal %d UsedByCurrPicS1 %d DeltaPocS1 %d"
- "%s::%s:%d ptr->UsedByCurrPicS0[%d] %d"
- "8002.38.0"
- "RPSparams.strps.rps[%d].used_by_curr_pic_s0_flag[%d]  %d\n"
- "RPSparams.strps.rps[%d].used_by_curr_pic_s1_flag[%d]  %d\n"

```

#### adc-rheia-v59.im4p

>  `adc-rheia-v59.im4p`

```diff

 
-  __TEXT.__text: 0x782eb8
-  __TEXT.__const: 0x944ea0
+  __TEXT.__text: 0x782fc0
+  __TEXT.__const: 0x944e98
   __TEXT.__cstring: 0x8da75
   __TEXT.text_env: 0x4fda4
   __TEXT._rtk_mtab: 0x2b8
CStrings:
+ "20:50:35"
- "19:32:46"

```

#### ansf.t8140.release.im4p

>  `ansf.t8140.release.im4p`

```diff

 
   __TEXT.text_first: 0x4488
-  __TEXT.__text: 0x1c13cc
+  __TEXT.__text: 0x1c1400
   __TEXT.shared: 0xd914
   __TEXT.read: 0x6b14
   __TEXT.__const: 0x5398
   __TEXT.idle_hooks: 0x10
-  __TEXT.__cstring: 0x22997
+  __TEXT.__cstring: 0x229a0
   __TEXT.__chain_starts: 0x0
   __TEXT.__constructor: 0x0
   __TEXT._rtk_mtab: 0x310
CStrings:
+ "2077.100.377.0.1"
+ "7.100.377.0.1~72"
+ "AppleStorageFirmware-2077.100.377.0.1~72"
- "2077.100.377"
- "2077.100.377~58"
- "AppleStorageFirmware-2077.100.377~58"

```

#### rans.t8140.release.im4p

>  `rans.t8140.release.im4p`

```diff

 
   __TEXT.text_first: 0x4488
-  __TEXT.__text: 0x1c13cc
+  __TEXT.__text: 0x1c1400
   __TEXT.shared: 0xd914
   __TEXT.read: 0x6b14
   __TEXT.__const: 0x5398
   __TEXT.idle_hooks: 0x10
-  __TEXT.__cstring: 0x22997
+  __TEXT.__cstring: 0x229a0
   __TEXT.__chain_starts: 0x0
   __TEXT.__constructor: 0x0
   __TEXT._rtk_mtab: 0x310
CStrings:
+ "2077.100.377.0.1"
+ "7.100.377.0.1~72"
+ "AppleStorageFirmware-2077.100.377.0.1~72"
- "2077.100.377"
- "2077.100.377~58"
- "AppleStorageFirmware-2077.100.377~58"

```

#### t8140pmp.im4p

>  `t8140pmp.im4p`

```diff

 
-  __TEXT.__text: 0x37880
+  __TEXT.__text: 0x3788c
   __TEXT.__const: 0x235c
   __TEXT.__cstring: 0x1540
   __TEXT._rtk_mtab: 0x5e8

```


</details>

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 18.4 *(22E5216h)* | 621.1.13.10.4 |
| 18.4 *(22E5222f)* | 621.1.14.10.3 |

### Dylibs

#### 🆕 NEW (1)

- `/System/Library/AccessibilityBundles/PasswordsSettings.axbundle/PasswordsSettings`

#### ❌ Removed (2)

- `/System/Library/PrivateFrameworks/AppleMediaServicesKit.framework/AppleMediaServicesKit`
- `/System/Library/PrivateFrameworks/ProactiveShareSheetDataHarvestingLighthouse.framework/ProactiveShareSheetDataHarvestingLighthouse`

#### ⬆️ Updated (929)

<details>
  <summary><i>View Updated</i></summary>

- [/System/Library/AccessibilityBundles/ChatKitFramework.axbundle/ChatKitFramework](DYLIBS/ChatKitFramework.md)
- [/System/Library/AccessibilityBundles/CommunicationsUI.axbundle/CommunicationsUI](DYLIBS/CommunicationsUI.md)
- [/System/Library/AccessibilityBundles/ControlCenterUI.axbundle/ControlCenterUI](DYLIBS/ControlCenterUI.md)
- [/System/Library/AccessibilityBundles/ControlCenterUIKit.axbundle/ControlCenterUIKit](DYLIBS/ControlCenterUIKit.md)
- [/System/Library/AccessibilityBundles/CoreIDVUI.axbundle/CoreIDVUI](DYLIBS/CoreIDVUI.md)
- [/System/Library/AccessibilityBundles/MailUI.axbundle/MailUI](DYLIBS/MailUI.md)
- [/System/Library/AccessibilityBundles/Maps.axbundle/Maps](DYLIBS/Maps.md)
- [/System/Library/AccessibilityBundles/MapsUI.axbundle/MapsUI](DYLIBS/MapsUI.md)
- [/System/Library/AccessibilityBundles/MediaControls.axbundle/MediaControls](DYLIBS/MediaControls.md)
- [/System/Library/AccessibilityBundles/MobileSafariFramework.axbundle/MobileSafariFramework](DYLIBS/MobileSafariFramework.md)
- [/System/Library/AccessibilityBundles/MobileTimer.axbundle/MobileTimer](DYLIBS/MobileTimer.md)
- [/System/Library/AccessibilityBundles/PencilKit.axbundle/PencilKit](DYLIBS/PencilKit.md)
- [/System/Library/AccessibilityBundles/PhotosUIFramework.axbundle/PhotosUIFramework](DYLIBS/PhotosUIFramework.md)
- [/System/Library/AccessibilityBundles/PosterBoardFramework.axbundle/PosterBoardFramework](DYLIBS/PosterBoardFramework.md)
- [/System/Library/AccessibilityBundles/SafariServices.axbundle/SafariServices](DYLIBS/SafariServices.md)
- [/System/Library/AccessibilityBundles/SiriSharedUI.axbundle/SiriSharedUI](DYLIBS/SiriSharedUI.md)
- [/System/Library/AccessibilityBundles/SpringBoard.axbundle/SpringBoard](DYLIBS/SpringBoard.md)
- [/System/Library/AccessibilityBundles/SpringBoardHome.axbundle/SpringBoardHome](DYLIBS/SpringBoardHome.md)
- [/System/Library/AccessibilityBundles/SpringBoardUIServices.axbundle/SpringBoardUIServices](DYLIBS/SpringBoardUIServices.md)
- [/System/Library/AccessibilityBundles/TVMLKit.axbundle/TVMLKit](DYLIBS/TVMLKit.md)
- [/System/Library/AccessibilityBundles/UIKit.axbundle/UIKit](DYLIBS/UIKit.md)
- [/System/Library/AccessibilityBundles/VideosUIFramework.axbundle/VideosUIFramework](DYLIBS/VideosUIFramework.md)
- [/System/Library/AccessibilityBundles/VoiceTriggerUI.axbundle/VoiceTriggerUI](DYLIBS/VoiceTriggerUI.md)
- [/System/Library/AccessibilityBundles/WorkflowUI.axbundle/WorkflowUI](DYLIBS/WorkflowUI.md)
- [/System/Library/AccessibilityBundles/iCloudSettings.axbundle/iCloudSettings](DYLIBS/iCloudSettings.md)
- [/System/Library/Accounts/Notification/AAAccountNotificationPlugin.bundle/AAAccountNotificationPlugin](DYLIBS/AAAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/PCSAccountNotificationPlugin.bundle/PCSAccountNotificationPlugin](DYLIBS/PCSAccountNotificationPlugin.md)
- [/System/Library/Assistant/UIPlugins/SiriFindMyUIPlugin.siriUIBundle/Frameworks/SiriFindMyUI.framework/SiriFindMyUI](DYLIBS/SiriFindMyUI.md)
- [/System/Library/ControlCenter/Bundles/AccessibilityTextSizeModule.bundle/AccessibilityTextSizeModule](DYLIBS/AccessibilityTextSizeModule.md)
- [/System/Library/ControlCenter/Bundles/TVRemoteModule.bundle/TVRemoteModule](DYLIBS/TVRemoteModule.md)
- [/System/Library/CoreAccessories/PlugIns/Transports/IOAccessoryManager.transport/IOAccessoryManager](DYLIBS/IOAccessoryManager.md)
- [/System/Library/CoreAccessories/PlugIns/Transports/USBHost.transport/USBHost](DYLIBS/USBHost.md)
- [/System/Library/Extensions/AGXMetalG17P.bundle/AGXMetalG17P](DYLIBS/AGXMetalG17P.md)
- [/System/Library/Frameworks/AVFAudio.framework/AVFAudio](DYLIBS/AVFAudio.md)
- [/System/Library/Frameworks/AVKit.framework/AVKit](DYLIBS/AVKit.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libBNNS.dylib](DYLIBS/libBNNS.dylib.md)
- [/System/Library/Frameworks/ActivityKit.framework/ActivityKit](DYLIBS/ActivityKit.md)
- [/System/Library/Frameworks/AppIntents.framework/AppIntents](DYLIBS/AppIntents.md)
- [/System/Library/Frameworks/Assignables.framework/Assignables](DYLIBS/Assignables.md)
- [/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox](DYLIBS/AudioToolbox.md)
- [/System/Library/Frameworks/AudioToolbox.framework/libAudioDSP.dylib](DYLIBS/libAudioDSP.dylib.md)
- [/System/Library/Frameworks/AudioToolbox.framework/libEmbeddedSystemAUs.dylib](DYLIBS/libEmbeddedSystemAUs.dylib.md)
- [/System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices](DYLIBS/AuthenticationServices.md)
- [/System/Library/Frameworks/CFNetwork.framework/CFNetwork](DYLIBS/CFNetwork.md)
- [/System/Library/Frameworks/Charts.framework/Charts](DYLIBS/Charts.md)
- [/System/Library/Frameworks/ClockKit.framework/ClockKit](DYLIBS/ClockKit.md)
- [/System/Library/Frameworks/CloudKit.framework/CloudKit](DYLIBS/CloudKit.md)
- [/System/Library/Frameworks/Combine.framework/Combine](DYLIBS/Combine.md)
- [/System/Library/Frameworks/ContactsUI.framework/ContactsUI](DYLIBS/ContactsUI.md)
- [/System/Library/Frameworks/CoreAudio.framework/CoreAudio](DYLIBS/CoreAudio.md)
- [/System/Library/Frameworks/CoreAudioKit.framework/CoreAudioKit](DYLIBS/CoreAudioKit.md)
- [/System/Library/Frameworks/CoreData.framework/CoreData](DYLIBS/CoreData.md)
- [/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation](DYLIBS/CoreFoundation.md)
- [/System/Library/Frameworks/CoreGraphics.framework/CoreGraphics](DYLIBS/CoreGraphics.md)
- [/System/Library/Frameworks/CoreLocation.framework/CoreLocation](DYLIBS/CoreLocation.md)
- [/System/Library/Frameworks/CoreML.framework/CoreML](DYLIBS/CoreML.md)
- [/System/Library/Frameworks/CoreMedia.framework/CoreMedia](DYLIBS/CoreMedia.md)
- [/System/Library/Frameworks/CoreMediaIO.framework/CoreMediaIO](DYLIBS/CoreMediaIO.md)
- [/System/Library/Frameworks/CoreMotion.framework/CoreMotion](DYLIBS/CoreMotion.md)
- [/System/Library/Frameworks/CoreServices.framework/CoreServices](DYLIBS/CoreServices.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight](DYLIBS/CoreSpotlight.md)
- [/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony](DYLIBS/CoreTelephony.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/CTParser.framework/CTParser](DYLIBS/CTParser.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterBase.dylib](DYLIBS/libCommCenterBase.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterCommandDrivers.dylib](DYLIBS/libCommCenterCommandDrivers.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterKCommandDrivers.dylib](DYLIBS/libCommCenterKCommandDrivers.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterMCommandDrivers.dylib](DYLIBS/libCommCenterMCommandDrivers.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libSystemDetermination.dylib](DYLIBS/libSystemDetermination.dylib.md)
- [/System/Library/Frameworks/CoreText.framework/CoreText](DYLIBS/CoreText.md)
- [/System/Library/Frameworks/CreateML.framework/CreateML](DYLIBS/CreateML.md)
- [/System/Library/Frameworks/CreateMLComponents.framework/CreateMLComponents](DYLIBS/CreateMLComponents.md)
- [/System/Library/Frameworks/CryptoKit.framework/CryptoKit](DYLIBS/CryptoKit.md)
- [/System/Library/Frameworks/DeveloperToolsSupport.framework/DeveloperToolsSupport](DYLIBS/DeveloperToolsSupport.md)
- [/System/Library/Frameworks/DeviceActivity.framework/DeviceActivity](DYLIBS/DeviceActivity.md)
- [/System/Library/Frameworks/EventKitUI.framework/EventKitUI](DYLIBS/EventKitUI.md)
- [/System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation](DYLIBS/ExtensionFoundation.md)
- [/System/Library/Frameworks/FileProvider.framework/FileProvider](DYLIBS/FileProvider.md)
- [/System/Library/Frameworks/FinanceKit.framework/FinanceKit](DYLIBS/FinanceKit.md)
- [/System/Library/Frameworks/FinanceKitUI.framework/FinanceKitUI](DYLIBS/FinanceKitUI.md)
- [/System/Library/Frameworks/Foundation.framework/Foundation](DYLIBS/Foundation.md)
- [/System/Library/Frameworks/GameKit.framework/GameKit](DYLIBS/GameKit.md)
- [/System/Library/Frameworks/GroupActivities.framework/GroupActivities](DYLIBS/GroupActivities.md)
- [/System/Library/Frameworks/HealthKit.framework/HealthKit](DYLIBS/HealthKit.md)
- [/System/Library/Frameworks/HomeKit.framework/HomeKit](DYLIBS/HomeKit.md)
- [/System/Library/Frameworks/ImageIO.framework/ImageIO](DYLIBS/ImageIO.md)
- [/System/Library/Frameworks/JavaScriptCore.framework/JavaScriptCore](DYLIBS/JavaScriptCore.md)
- [/System/Library/Frameworks/LightweightCodeRequirements.framework/LightweightCodeRequirements](DYLIBS/LightweightCodeRequirements.md)
- [/System/Library/Frameworks/LiveCommunicationKit.framework/LiveCommunicationKit](DYLIBS/LiveCommunicationKit.md)
- [/System/Library/Frameworks/ManagedApp.framework/ManagedApp](DYLIBS/ManagedApp.md)
- [/System/Library/Frameworks/ManagedAppDistribution.framework/ManagedAppDistribution](DYLIBS/ManagedAppDistribution.md)
- [/System/Library/Frameworks/ManagedSettings.framework/ManagedSettings](DYLIBS/ManagedSettings.md)
- [/System/Library/Frameworks/MapKit.framework/MapKit](DYLIBS/MapKit.md)
- [/System/Library/Frameworks/MarketplaceKit.framework/MarketplaceKit](DYLIBS/MarketplaceKit.md)
- [/System/Library/Frameworks/Matter.framework/Matter](DYLIBS/Matter.md)
- [/System/Library/Frameworks/MediaPlayer.framework/MediaPlayer](DYLIBS/MediaPlayer.md)
- [/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox](DYLIBS/MediaToolbox.md)
- [/System/Library/Frameworks/Metal.framework/Metal](DYLIBS/Metal.md)
- [/System/Library/Frameworks/MetalFX.framework/MetalFX](DYLIBS/MetalFX.md)
- [/System/Library/Frameworks/MusicKit.framework/MusicKit](DYLIBS/MusicKit.md)
- [/System/Library/Frameworks/Network.framework/Network](DYLIBS/Network.md)
- [/System/Library/Frameworks/PencilKit.framework/PencilKit](DYLIBS/PencilKit.md)
- [/System/Library/Frameworks/Photos.framework/Photos](DYLIBS/Photos.md)
- [/System/Library/Frameworks/ProximityReader.framework/ProximityReader](DYLIBS/ProximityReader.md)
- [/System/Library/Frameworks/QuartzCore.framework/QuartzCore](DYLIBS/QuartzCore.md)
- [/System/Library/Frameworks/RealityFoundation.framework/RealityFoundation](DYLIBS/RealityFoundation.md)
- [/System/Library/Frameworks/RealityKit.framework/RealityKit](DYLIBS/RealityKit.md)
- [/System/Library/Frameworks/RoomPlan.framework/RoomPlan](DYLIBS/RoomPlan.md)
- [/System/Library/Frameworks/SafariServices.framework/SafariServices](DYLIBS/SafariServices.md)
- [/System/Library/Frameworks/SceneKit.framework/SceneKit](DYLIBS/SceneKit.md)
- [/System/Library/Frameworks/ScreenTime.framework/ScreenTime](DYLIBS/ScreenTime.md)
- [/System/Library/Frameworks/SoundAnalysis.framework/SoundAnalysis](DYLIBS/SoundAnalysis.md)
- [/System/Library/Frameworks/Speech.framework/Speech](DYLIBS/Speech.md)
- [/System/Library/Frameworks/StickerKit.framework/StickerKit](DYLIBS/StickerKit.md)
- [/System/Library/Frameworks/StoreKit.framework/StoreKit](DYLIBS/StoreKit.md)
- [/System/Library/Frameworks/SwiftData.framework/SwiftData](DYLIBS/SwiftData.md)
- [/System/Library/Frameworks/SwiftUI.framework/SwiftUI](DYLIBS/SwiftUI.md)
- [/System/Library/Frameworks/SwiftUICore.framework/SwiftUICore](DYLIBS/SwiftUICore.md)
- [/System/Library/Frameworks/TabularData.framework/TabularData](DYLIBS/TabularData.md)
- [/System/Library/Frameworks/TipKit.framework/TipKit](DYLIBS/TipKit.md)
- [/System/Library/Frameworks/TranslationUIProvider.framework/TranslationUIProvider](DYLIBS/TranslationUIProvider.md)
- [/System/Library/Frameworks/VideoSubscriberAccount.framework/VideoSubscriberAccount](DYLIBS/VideoSubscriberAccount.md)
- [/System/Library/Frameworks/VideoToolbox.framework/VideoToolbox](DYLIBS/VideoToolbox.md)
- [/System/Library/Frameworks/Vision.framework/Vision](DYLIBS/Vision.md)
- [/System/Library/Frameworks/WebKit.framework/WebKit](DYLIBS/WebKit.md)
- [/System/Library/Frameworks/WidgetKit.framework/WidgetKit](DYLIBS/WidgetKit.md)
- [/System/Library/Frameworks/WorkoutKit.framework/WorkoutKit](DYLIBS/WorkoutKit.md)
- [/System/Library/Frameworks/_AppIntents_SwiftUI.framework/_AppIntents_SwiftUI](DYLIBS/_AppIntents_SwiftUI.md)
- [/System/Library/Frameworks/_AppIntents_UIKit.framework/_AppIntents_UIKit](DYLIBS/_AppIntents_UIKit.md)
- [/System/Library/Frameworks/_AuthenticationServices_SwiftUI.framework/_AuthenticationServices_SwiftUI](DYLIBS/_AuthenticationServices_SwiftUI.md)
- [/System/Library/Frameworks/_ManagedAppDistribution_SwiftUI.framework/_ManagedAppDistribution_SwiftUI](DYLIBS/_ManagedAppDistribution_SwiftUI.md)
- [/System/Library/Frameworks/_MapKit_SwiftUI.framework/_MapKit_SwiftUI](DYLIBS/_MapKit_SwiftUI.md)
- [/System/Library/Frameworks/_MusicKit_SwiftUI.framework/_MusicKit_SwiftUI](DYLIBS/_MusicKit_SwiftUI.md)
- [/System/Library/Frameworks/_RealityKit_SwiftUI.framework/_RealityKit_SwiftUI](DYLIBS/_RealityKit_SwiftUI.md)
- [/System/Library/Frameworks/_StoreKit_SwiftUI.framework/_StoreKit_SwiftUI](DYLIBS/_StoreKit_SwiftUI.md)
- [/System/Library/Frameworks/_SwiftData_CoreData.framework/_SwiftData_CoreData](DYLIBS/_SwiftData_CoreData.md)
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
- [/System/Library/NanoPreferenceBundles/General/AccessibilitySettings.bundle/AccessibilitySettings](DYLIBS/AccessibilitySettings.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/WeatherComplications.bundle/WeatherComplications](DYLIBS/WeatherComplications.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKEsterbrookFaceBundleCompanion.bundle/NTKEsterbrookFaceBundleCompanion](DYLIBS/NTKEsterbrookFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKParmesanFaceBundleCompanion.bundle/NTKParmesanFaceBundleCompanion](DYLIBS/NTKParmesanFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKRhizomeFaceBundleCompanion.bundle/NTKRhizomeFaceBundleCompanion](DYLIBS/NTKRhizomeFaceBundleCompanion.md)
- [/System/Library/Previews/ShellPlugins/WidgetPreviewsShellPlugin.bundle/WidgetPreviewsShellPlugin](DYLIBS/WidgetPreviewsShellPlugin.md)
- [/System/Library/PrivateFrameworks/ABMHelper.framework/ABMHelper](DYLIBS/ABMHelper.md)
- [/System/Library/PrivateFrameworks/AGXCompilerCore.framework/AGXCompilerCore](DYLIBS/AGXCompilerCore.md)
- [/System/Library/PrivateFrameworks/ANECompiler.framework/ANECompiler](DYLIBS/ANECompiler.md)
- [/System/Library/PrivateFrameworks/APFS.framework/APFS](DYLIBS/APFS.md)
- [/System/Library/PrivateFrameworks/APFoundation.framework/APFoundation](DYLIBS/APFoundation.md)
- [/System/Library/PrivateFrameworks/ARKitCore.framework/ARKitCore](DYLIBS/ARKitCore.md)
- [/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture](DYLIBS/AVFCapture.md)
- [/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore](DYLIBS/AVFCore.md)
- [/System/Library/PrivateFrameworks/AccessibilitySettingsUI.framework/AccessibilitySettingsUI](DYLIBS/AccessibilitySettingsUI.md)
- [/System/Library/PrivateFrameworks/AccessibilitySharedUISupport.framework/AccessibilitySharedUISupport](DYLIBS/AccessibilitySharedUISupport.md)
- [/System/Library/PrivateFrameworks/AccessibilityUIService.framework/AccessibilityUIService](DYLIBS/AccessibilityUIService.md)
- [/System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities](DYLIBS/AccessibilityUtilities.md)
- [/System/Library/PrivateFrameworks/ActionButtonConfigurationUI.framework/ActionButtonConfigurationUI](DYLIBS/ActionButtonConfigurationUI.md)
- [/System/Library/PrivateFrameworks/ActionKitUI.framework/ActionKitUI](DYLIBS/ActionKitUI.md)
- [/System/Library/PrivateFrameworks/ActionPredictionHeuristics.framework/ActionPredictionHeuristics](DYLIBS/ActionPredictionHeuristics.md)
- [/System/Library/PrivateFrameworks/ActionPredictionHeuristicsInternal.framework/ActionPredictionHeuristicsInternal](DYLIBS/ActionPredictionHeuristicsInternal.md)
- [/System/Library/PrivateFrameworks/ActivitySharingServices.framework/ActivitySharingServices](DYLIBS/ActivitySharingServices.md)
- [/System/Library/PrivateFrameworks/ActivitySharingUI.framework/ActivitySharingUI](DYLIBS/ActivitySharingUI.md)
- [/System/Library/PrivateFrameworks/ActivityUIServices.framework/ActivityUIServices](DYLIBS/ActivityUIServices.md)
- [/System/Library/PrivateFrameworks/AdPlatforms.framework/AdPlatforms](DYLIBS/AdPlatforms.md)
- [/System/Library/PrivateFrameworks/AdaptiveVoiceShortcuts.framework/AdaptiveVoiceShortcuts](DYLIBS/AdaptiveVoiceShortcuts.md)
- [/System/Library/PrivateFrameworks/AirPlayKit.framework/AirPlayKit](DYLIBS/AirPlayKit.md)
- [/System/Library/PrivateFrameworks/AirPlayReceiver.framework/AirPlayReceiver](DYLIBS/AirPlayReceiver.md)
- [/System/Library/PrivateFrameworks/AirPlaySender.framework/AirPlaySender](DYLIBS/AirPlaySender.md)
- [/System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport](DYLIBS/AirPlaySupport.md)
- [/System/Library/PrivateFrameworks/AirTrafficDevice.framework/AirTrafficDevice](DYLIBS/AirTrafficDevice.md)
- [/System/Library/PrivateFrameworks/Anvil.framework/Anvil](DYLIBS/Anvil.md)
- [/System/Library/PrivateFrameworks/AppAnalytics.framework/AppAnalytics](DYLIBS/AppAnalytics.md)
- [/System/Library/PrivateFrameworks/AppAttestInternal.framework/AppAttestInternal](DYLIBS/AppAttestInternal.md)
- [/System/Library/PrivateFrameworks/AppDistribution.framework/AppDistribution](DYLIBS/AppDistribution.md)
- [/System/Library/PrivateFrameworks/AppIntentsServices.framework/AppIntentsServices](DYLIBS/AppIntentsServices.md)
- [/System/Library/PrivateFrameworks/AppMigrationKit.framework/AppMigrationKit](DYLIBS/AppMigrationKit.md)
- [/System/Library/PrivateFrameworks/AppPredictionInternal.framework/AppPredictionInternal](DYLIBS/AppPredictionInternal.md)
- [/System/Library/PrivateFrameworks/AppPredictionToolsInternal.framework/AppPredictionToolsInternal](DYLIBS/AppPredictionToolsInternal.md)
- [/System/Library/PrivateFrameworks/AppPredictionUIFoundation.framework/AppPredictionUIFoundation](DYLIBS/AppPredictionUIFoundation.md)
- [/System/Library/PrivateFrameworks/AppProtection.framework/AppProtection](DYLIBS/AppProtection.md)
- [/System/Library/PrivateFrameworks/AppState.framework/AppState](DYLIBS/AppState.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon](DYLIBS/AppStoreDaemon.md)
- [/System/Library/PrivateFrameworks/AppStoreKit.framework/AppStoreKit](DYLIBS/AppStoreKit.md)
- [/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount](DYLIBS/AppleAccount.md)
- [/System/Library/PrivateFrameworks/AppleAccountUI.framework/AppleAccountUI](DYLIBS/AppleAccountUI.md)
- [/System/Library/PrivateFrameworks/AppleBasebandManager.framework/AppleBasebandManager](DYLIBS/AppleBasebandManager.md)
- [/System/Library/PrivateFrameworks/AppleBasebandServices.framework/AppleBasebandServices](DYLIBS/AppleBasebandServices.md)
- [/System/Library/PrivateFrameworks/AppleCV3D.framework/AppleCV3D](DYLIBS/AppleCV3D.md)
- [/System/Library/PrivateFrameworks/AppleCVHWA.framework/AppleCVHWA](DYLIBS/AppleCVHWA.md)
- [/System/Library/PrivateFrameworks/AppleCareSupport.framework/AppleCareSupport](DYLIBS/AppleCareSupport.md)
- [/System/Library/PrivateFrameworks/AppleIDSetup.framework/AppleIDSetup](DYLIBS/AppleIDSetup.md)
- [/System/Library/PrivateFrameworks/AppleIDSetupDaemon.framework/AppleIDSetupDaemon](DYLIBS/AppleIDSetupDaemon.md)
- [/System/Library/PrivateFrameworks/AppleIDSetupUI.framework/AppleIDSetupUI](DYLIBS/AppleIDSetupUI.md)
- [/System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore](DYLIBS/AppleKeyStore.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices](DYLIBS/AppleMediaServices.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesKitInternal.framework/AppleMediaServicesKitInternal](DYLIBS/AppleMediaServicesKitInternal.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesKitSupport.framework/AppleMediaServicesKitSupport](DYLIBS/AppleMediaServicesKitSupport.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/AppleMediaServicesUI](DYLIBS/AppleMediaServicesUI.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUIDynamic.framework/AppleMediaServicesUIDynamic](DYLIBS/AppleMediaServicesUIDynamic.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUIPaymentSheets.framework/AppleMediaServicesUIPaymentSheets](DYLIBS/AppleMediaServicesUIPaymentSheets.md)
- [/System/Library/PrivateFrameworks/ApplePhotonDetectorServices.framework/ApplePhotonDetectorServices](DYLIBS/ApplePhotonDetectorServices.md)
- [/System/Library/PrivateFrameworks/ArgumentParserInternal.framework/ArgumentParserInternal](DYLIBS/ArgumentParserInternal.md)
- [/System/Library/PrivateFrameworks/AskToDaemon.framework/AskToDaemon](DYLIBS/AskToDaemon.md)
- [/System/Library/PrivateFrameworks/AssertionServices.framework/AssertionServices](DYLIBS/AssertionServices.md)
- [/System/Library/PrivateFrameworks/AssetViewer.framework/AssetViewer](DYLIBS/AssetViewer.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices](DYLIBS/AssistantServices.md)
- [/System/Library/PrivateFrameworks/AssistantSettingsSupport.framework/AssistantSettingsSupport](DYLIBS/AssistantSettingsSupport.md)
- [/System/Library/PrivateFrameworks/AttributeGraph.framework/AttributeGraph](DYLIBS/AttributeGraph.md)
- [/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices](DYLIBS/AudioAccessoryServices.md)
- [/System/Library/PrivateFrameworks/AudioAnalyticsBase.framework/AudioAnalyticsBase](DYLIBS/AudioAnalyticsBase.md)
- [/System/Library/PrivateFrameworks/AudioAnalyticsExternal.framework/AudioAnalyticsExternal](DYLIBS/AudioAnalyticsExternal.md)
- [/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore](DYLIBS/AudioToolboxCore.md)
- [/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit](DYLIBS/AuthKit.md)
- [/System/Library/PrivateFrameworks/AuthKitUI.framework/AuthKitUI](DYLIBS/AuthKitUI.md)
- [/System/Library/PrivateFrameworks/AuthenticationServicesCore.framework/AuthenticationServicesCore](DYLIBS/AuthenticationServicesCore.md)
- [/System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks](DYLIBS/BackgroundSystemTasks.md)
- [/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost](DYLIBS/BacklightServicesHost.md)
- [/System/Library/PrivateFrameworks/BasebandTraceHelper.framework/BasebandTraceHelper](DYLIBS/BasebandTraceHelper.md)
- [/System/Library/PrivateFrameworks/BiomeFoundation.framework/BiomeFoundation](DYLIBS/BiomeFoundation.md)
- [/System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary](DYLIBS/BiomeLibrary.md)
- [/System/Library/PrivateFrameworks/BiomePubSub.framework/BiomePubSub](DYLIBS/BiomePubSub.md)
- [/System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams](DYLIBS/BiomeStreams.md)
- [/System/Library/PrivateFrameworks/BiometricSupport.framework/BiometricSupport](DYLIBS/BiometricSupport.md)
- [/System/Library/PrivateFrameworks/Blackbeard.framework/Blackbeard](DYLIBS/Blackbeard.md)
- [/System/Library/PrivateFrameworks/BlastDoor.framework/BlastDoor](DYLIBS/BlastDoor.md)
- [/System/Library/PrivateFrameworks/BookDataStore.framework/BookDataStore](DYLIBS/BookDataStore.md)
- [/System/Library/PrivateFrameworks/BrailleSymbology.framework/BrailleSymbology](DYLIBS/BrailleSymbology.md)
- [/System/Library/PrivateFrameworks/BrailleTranslation.framework/BrailleTranslation](DYLIBS/BrailleTranslation.md)
- [/System/Library/PrivateFrameworks/CAFCombine.framework/CAFCombine](DYLIBS/CAFCombine.md)
- [/System/Library/PrivateFrameworks/CAFUI.framework/CAFUI](DYLIBS/CAFUI.md)
- [/System/Library/PrivateFrameworks/CDMFoundation.framework/CDMFoundation](DYLIBS/CDMFoundation.md)
- [/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture](DYLIBS/CMCapture.md)
- [/System/Library/PrivateFrameworks/CMCaptureCore.framework/CMCaptureCore](DYLIBS/CMCaptureCore.md)
- [/System/Library/PrivateFrameworks/CMContinuityCaptureCore.framework/CMContinuityCaptureCore](DYLIBS/CMContinuityCaptureCore.md)
- [/System/Library/PrivateFrameworks/CMImaging.framework/CMImaging](DYLIBS/CMImaging.md)
- [/System/Library/PrivateFrameworks/CMPhoto.framework/CMPhoto](DYLIBS/CMPhoto.md)
- [/System/Library/PrivateFrameworks/CPAnalytics.framework/CPAnalytics](DYLIBS/CPAnalytics.md)
- [/System/Library/PrivateFrameworks/CTCarrierSpace.framework/CTCarrierSpace](DYLIBS/CTCarrierSpace.md)
- [/System/Library/PrivateFrameworks/CTLazuliSupport.framework/CTLazuliSupport](DYLIBS/CTLazuliSupport.md)
- [/System/Library/PrivateFrameworks/Calculate.framework/Calculate](DYLIBS/Calculate.md)
- [/System/Library/PrivateFrameworks/CalculateUI.framework/CalculateUI](DYLIBS/CalculateUI.md)
- [/System/Library/PrivateFrameworks/CalendarLink.framework/CalendarLink](DYLIBS/CalendarLink.md)
- [/System/Library/PrivateFrameworks/CalendarUIKit.framework/CalendarUIKit](DYLIBS/CalendarUIKit.md)
- [/System/Library/PrivateFrameworks/CalendarWidget.framework/CalendarWidget](DYLIBS/CalendarWidget.md)
- [/System/Library/PrivateFrameworks/CallHistory.framework/CallHistory](DYLIBS/CallHistory.md)
- [/System/Library/PrivateFrameworks/CameraColorProcessing.framework/CameraColorProcessing](DYLIBS/CameraColorProcessing.md)
- [/System/Library/PrivateFrameworks/CameraEditKit.framework/CameraEditKit](DYLIBS/CameraEditKit.md)
- [/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI](DYLIBS/CameraUI.md)
- [/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework](DYLIBS/CarAccessoryFramework.md)
- [/System/Library/PrivateFrameworks/CarAssetUtils.framework/CarAssetUtils](DYLIBS/CarAssetUtils.md)
- [/System/Library/PrivateFrameworks/CarKit.framework/CarKit](DYLIBS/CarKit.md)
- [/System/Library/PrivateFrameworks/CarPlayAssetUI.framework/CarPlayAssetUI](DYLIBS/CarPlayAssetUI.md)
- [/System/Library/PrivateFrameworks/CarPlaySupport.framework/CarPlaySupport](DYLIBS/CarPlaySupport.md)
- [/System/Library/PrivateFrameworks/CarPlayUI.framework/CarPlayUI](DYLIBS/CarPlayUI.md)
- [/System/Library/PrivateFrameworks/CarPlayUIServices.framework/CarPlayUIServices](DYLIBS/CarPlayUIServices.md)
- [/System/Library/PrivateFrameworks/CascadeEngine.framework/CascadeEngine](DYLIBS/CascadeEngine.md)
- [/System/Library/PrivateFrameworks/CascadeSets.framework/CascadeSets](DYLIBS/CascadeSets.md)
- [/System/Library/PrivateFrameworks/Celestial.framework/Celestial](DYLIBS/Celestial.md)
- [/System/Library/PrivateFrameworks/CellularPlanManager.framework/CellularPlanManager](DYLIBS/CellularPlanManager.md)
- [/System/Library/PrivateFrameworks/ChatKit.framework/ChatKit](DYLIBS/ChatKit.md)
- [/System/Library/PrivateFrameworks/Chirp.framework/Chirp](DYLIBS/Chirp.md)
- [/System/Library/PrivateFrameworks/ChronoCore.framework/ChronoCore](DYLIBS/ChronoCore.md)
- [/System/Library/PrivateFrameworks/ChronoKit.framework/ChronoKit](DYLIBS/ChronoKit.md)
- [/System/Library/PrivateFrameworks/ChronoServices.framework/ChronoServices](DYLIBS/ChronoServices.md)
- [/System/Library/PrivateFrameworks/ChronoUIServices.framework/ChronoUIServices](DYLIBS/ChronoUIServices.md)
- [/System/Library/PrivateFrameworks/CinematicFraming.framework/CinematicFraming](DYLIBS/CinematicFraming.md)
- [/System/Library/PrivateFrameworks/CipherML.framework/CipherML](DYLIBS/CipherML.md)
- [/System/Library/PrivateFrameworks/ClassroomKit.framework/Frameworks/ClassroomUIKit.framework/ClassroomUIKit](DYLIBS/ClassroomUIKit.md)
- [/System/Library/PrivateFrameworks/ClipServices.framework/ClipServices](DYLIBS/ClipServices.md)
- [/System/Library/PrivateFrameworks/ClipUIServices.framework/ClipUIServices](DYLIBS/ClipUIServices.md)
- [/System/Library/PrivateFrameworks/ClockPoster.framework/ClockPoster](DYLIBS/ClockPoster.md)
- [/System/Library/PrivateFrameworks/CloudAsset.framework/CloudAsset](DYLIBS/CloudAsset.md)
- [/System/Library/PrivateFrameworks/CloudAssetDaemon.framework/CloudAssetDaemon](DYLIBS/CloudAssetDaemon.md)
- [/System/Library/PrivateFrameworks/CloudAttestation.framework/CloudAttestation](DYLIBS/CloudAttestation.md)
- [/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/CloudPhotoLibrary](DYLIBS/CloudPhotoLibrary.md)
- [/System/Library/PrivateFrameworks/CloudRecommendationUI.framework/CloudRecommendationUI](DYLIBS/CloudRecommendationUI.md)
- [/System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/CloudSubscriptionFeatures](DYLIBS/CloudSubscriptionFeatures.md)
- [/System/Library/PrivateFrameworks/CloudTelemetryTools.framework/CloudTelemetryTools](DYLIBS/CloudTelemetryTools.md)
- [/System/Library/PrivateFrameworks/Coherence.framework/Coherence](DYLIBS/Coherence.md)
- [/System/Library/PrivateFrameworks/CollectionsInternal.framework/CollectionsInternal](DYLIBS/CollectionsInternal.md)
- [/System/Library/PrivateFrameworks/CommunicationsUI.framework/CommunicationsUI](DYLIBS/CommunicationsUI.md)
- [/System/Library/PrivateFrameworks/ContactlessReaderUI.framework/ContactlessReaderUI](DYLIBS/ContactlessReaderUI.md)
- [/System/Library/PrivateFrameworks/ContactsAutocomplete.framework/ContactsAutocomplete](DYLIBS/ContactsAutocomplete.md)
- [/System/Library/PrivateFrameworks/ContactsUICore.framework/ContactsUICore](DYLIBS/ContactsUICore.md)
- [/System/Library/PrivateFrameworks/ContainerManagerCommon.framework/ContainerManagerCommon](DYLIBS/ContainerManagerCommon.md)
- [/System/Library/PrivateFrameworks/ControlCenterUI.framework/ControlCenterUI](DYLIBS/ControlCenterUI.md)
- [/System/Library/PrivateFrameworks/ControlCenterUIKit.framework/ControlCenterUIKit](DYLIBS/ControlCenterUIKit.md)
- [/System/Library/PrivateFrameworks/ConversationKit.framework/ConversationKit](DYLIBS/ConversationKit.md)
- [/System/Library/PrivateFrameworks/CookingKit.framework/CookingKit](DYLIBS/CookingKit.md)
- [/System/Library/PrivateFrameworks/CookingSupport.framework/CookingSupport](DYLIBS/CookingSupport.md)
- [/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness](DYLIBS/CoreBrightness.md)
- [/System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP](DYLIBS/CoreCDP.md)
- [/System/Library/PrivateFrameworks/CoreCDPUI.framework/CoreCDPUI](DYLIBS/CoreCDPUI.md)
- [/System/Library/PrivateFrameworks/CoreDiagnostics.framework/CoreDiagnostics](DYLIBS/CoreDiagnostics.md)
- [/System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet](DYLIBS/CoreDuet.md)
- [/System/Library/PrivateFrameworks/CoreDuetContext.framework/CoreDuetContext](DYLIBS/CoreDuetContext.md)
- [/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/CoreEmbeddedSpeechRecognition](DYLIBS/CoreEmbeddedSpeechRecognition.md)
- [/System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp](DYLIBS/CoreFollowUp.md)
- [/System/Library/PrivateFrameworks/CoreHID.framework/CoreHID](DYLIBS/CoreHID.md)
- [/System/Library/PrivateFrameworks/CoreHandwriting.framework/CoreHandwriting](DYLIBS/CoreHandwriting.md)
- [/System/Library/PrivateFrameworks/CoreIDV.framework/CoreIDV](DYLIBS/CoreIDV.md)
- [/System/Library/PrivateFrameworks/CoreIDVRGBLiveness.framework/CoreIDVRGBLiveness](DYLIBS/CoreIDVRGBLiveness.md)
- [/System/Library/PrivateFrameworks/CoreIDVShared.framework/CoreIDVShared](DYLIBS/CoreIDVShared.md)
- [/System/Library/PrivateFrameworks/CoreIDVUI.framework/CoreIDVUI](DYLIBS/CoreIDVUI.md)
- [/System/Library/PrivateFrameworks/CoreKnowledge.framework/CoreKnowledge](DYLIBS/CoreKnowledge.md)
- [/System/Library/PrivateFrameworks/CoreOC.framework/CoreOC](DYLIBS/CoreOC.md)
- [/System/Library/PrivateFrameworks/CoreODI.framework/CoreODI](DYLIBS/CoreODI.md)
- [/System/Library/PrivateFrameworks/CoreODIEssentials.framework/CoreODIEssentials](DYLIBS/CoreODIEssentials.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/CoreParsec](DYLIBS/CoreParsec.md)
- [/System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore](DYLIBS/CoreRepairCore.md)
- [/System/Library/PrivateFrameworks/CoreRepairKit.framework/CoreRepairKit](DYLIBS/CoreRepairKit.md)
- [/System/Library/PrivateFrameworks/CoreRepairLite.framework/CoreRepairLite](DYLIBS/CoreRepairLite.md)
- [/System/Library/PrivateFrameworks/CoreRepairUI.framework/CoreRepairUI](DYLIBS/CoreRepairUI.md)
- [/System/Library/PrivateFrameworks/CoreSuggestions.framework/CoreSuggestions](DYLIBS/CoreSuggestions.md)
- [/System/Library/PrivateFrameworks/CoreSuggestionsInternals.framework/CoreSuggestionsInternals](DYLIBS/CoreSuggestionsInternals.md)
- [/System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils](DYLIBS/CoreUtils.md)
- [/System/Library/PrivateFrameworks/CoverSheet.framework/CoverSheet](DYLIBS/CoverSheet.md)
- [/System/Library/PrivateFrameworks/CryptoKitPrivate.framework/CryptoKitPrivate](DYLIBS/CryptoKitPrivate.md)
- [/System/Library/PrivateFrameworks/DMCApps.framework/DMCApps](DYLIBS/DMCApps.md)
- [/System/Library/PrivateFrameworks/DSRemotePairing.framework/DSRemotePairing](DYLIBS/DSRemotePairing.md)
- [/System/Library/PrivateFrameworks/DailyBriefingCommon.framework/DailyBriefingCommon](DYLIBS/DailyBriefingCommon.md)
- [/System/Library/PrivateFrameworks/DarwinDirectoryQuery.framework/DarwinDirectoryQuery](DYLIBS/DarwinDirectoryQuery.md)
- [/System/Library/PrivateFrameworks/DashBoard.framework/DashBoard](DYLIBS/DashBoard.md)
- [/System/Library/PrivateFrameworks/DataFlow.framework/DataFlow](DYLIBS/DataFlow.md)
- [/System/Library/PrivateFrameworks/DeepThought.framework/DeepThought](DYLIBS/DeepThought.md)
- [/System/Library/PrivateFrameworks/DeepThoughtBiomeFoundation.framework/DeepThoughtBiomeFoundation](DYLIBS/DeepThoughtBiomeFoundation.md)
- [/System/Library/PrivateFrameworks/Dendrite.framework/Dendrite](DYLIBS/Dendrite.md)
- [/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/DesktopServicesPriv](DYLIBS/DesktopServicesPriv.md)
- [/System/Library/PrivateFrameworks/DeviceDiscoveryUI.framework/DeviceDiscoveryUI](DYLIBS/DeviceDiscoveryUI.md)
- [/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/DeviceExpertIntents](DYLIBS/DeviceExpertIntents.md)
- [/System/Library/PrivateFrameworks/DeviceExpertUI.framework/DeviceExpertUI](DYLIBS/DeviceExpertUI.md)
- [/System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity](DYLIBS/DeviceIdentity.md)
- [/System/Library/PrivateFrameworks/DeviceSharing.framework/DeviceSharing](DYLIBS/DeviceSharing.md)
- [/System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation](DYLIBS/DigitalSeparation.md)
- [/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI](DYLIBS/DigitalSeparationUI.md)
- [/System/Library/PrivateFrameworks/DiskImages2.framework/DiskImages2](DYLIBS/DiskImages2.md)
- [/System/Library/PrivateFrameworks/DistributedTimersDaemon.framework/DistributedTimersDaemon](DYLIBS/DistributedTimersDaemon.md)
- [/System/Library/PrivateFrameworks/DockKitCore.framework/DockKitCore](DYLIBS/DockKitCore.md)
- [/System/Library/PrivateFrameworks/DocumentUnderstanding.framework/DocumentUnderstanding](DYLIBS/DocumentUnderstanding.md)
- [/System/Library/PrivateFrameworks/DrawingBoard.framework/DrawingBoard](DYLIBS/DrawingBoard.md)
- [/System/Library/PrivateFrameworks/DropIn.framework/DropIn](DYLIBS/DropIn.md)
- [/System/Library/PrivateFrameworks/DropInCore.framework/DropInCore](DYLIBS/DropInCore.md)
- [/System/Library/PrivateFrameworks/DuetActivityScheduler.framework/DuetActivityScheduler](DYLIBS/DuetActivityScheduler.md)
- [/System/Library/PrivateFrameworks/Dyld.framework/Dyld](DYLIBS/Dyld.md)
- [/System/Library/PrivateFrameworks/EDPSecurity.framework/EDPSecurity](DYLIBS/EDPSecurity.md)
- [/System/Library/PrivateFrameworks/EcosystemAnalytics.framework/EcosystemAnalytics](DYLIBS/EcosystemAnalytics.md)
- [/System/Library/PrivateFrameworks/Email.framework/Email](DYLIBS/Email.md)
- [/System/Library/PrivateFrameworks/EmailDaemon.framework/EmailDaemon](DYLIBS/EmailDaemon.md)
- [/System/Library/PrivateFrameworks/EmailFoundation.framework/EmailFoundation](DYLIBS/EmailFoundation.md)
- [/System/Library/PrivateFrameworks/EmbeddedAcousticRecognition.framework/EmbeddedAcousticRecognition](DYLIBS/EmbeddedAcousticRecognition.md)
- [/System/Library/PrivateFrameworks/EmojiFoundation.framework/EmojiFoundation](DYLIBS/EmojiFoundation.md)
- [/System/Library/PrivateFrameworks/EmojiPoster.framework/EmojiPoster](DYLIBS/EmojiPoster.md)
- [/System/Library/PrivateFrameworks/Espresso.framework/Espresso](DYLIBS/Espresso.md)
- [/System/Library/PrivateFrameworks/FMFCore.framework/FMFCore](DYLIBS/FMFCore.md)
- [/System/Library/PrivateFrameworks/FMFindingUI.framework/FMFindingUI](DYLIBS/FMFindingUI.md)
- [/System/Library/PrivateFrameworks/FMIPCore.framework/FMIPCore](DYLIBS/FMIPCore.md)
- [/System/Library/PrivateFrameworks/FSKit.framework/FSKit](DYLIBS/FSKit.md)
- [/System/Library/PrivateFrameworks/FaceTimeMessageStore.framework/FaceTimeMessageStore](DYLIBS/FaceTimeMessageStore.md)
- [/System/Library/PrivateFrameworks/FamilyCircleUI.framework/FamilyCircleUI](DYLIBS/FamilyCircleUI.md)
- [/System/Library/PrivateFrameworks/Feedback.framework/Feedback](DYLIBS/Feedback.md)
- [/System/Library/PrivateFrameworks/FeedbackCore.framework/FeedbackCore](DYLIBS/FeedbackCore.md)
- [/System/Library/PrivateFrameworks/FeedbackLogger.framework/FeedbackLogger](DYLIBS/FeedbackLogger.md)
- [/System/Library/PrivateFrameworks/FileProviderDaemon.framework/FileProviderDaemon](DYLIBS/FileProviderDaemon.md)
- [/System/Library/PrivateFrameworks/FinanceDaemon.framework/FinanceDaemon](DYLIBS/FinanceDaemon.md)
- [/System/Library/PrivateFrameworks/FindMyBase.framework/FindMyBase](DYLIBS/FindMyBase.md)
- [/System/Library/PrivateFrameworks/FindMyCore.framework/FindMyCore](DYLIBS/FindMyCore.md)
- [/System/Library/PrivateFrameworks/FindMyLocate.framework/FindMyLocate](DYLIBS/FindMyLocate.md)
- [/System/Library/PrivateFrameworks/FindMyMessaging.framework/FindMyMessaging](DYLIBS/FindMyMessaging.md)
- [/System/Library/PrivateFrameworks/FindMyUICore.framework/FindMyUICore](DYLIBS/FindMyUICore.md)
- [/System/Library/PrivateFrameworks/FitnessAppRoot.framework/FitnessAppRoot](DYLIBS/FitnessAppRoot.md)
- [/System/Library/PrivateFrameworks/FitnessAsset.framework/FitnessAsset](DYLIBS/FitnessAsset.md)
- [/System/Library/PrivateFrameworks/FitnessCanvasUI.framework/FitnessCanvasUI](DYLIBS/FitnessCanvasUI.md)
- [/System/Library/PrivateFrameworks/FitnessCoaching.framework/FitnessCoaching](DYLIBS/FitnessCoaching.md)
- [/System/Library/PrivateFrameworks/FitnessCoachingServices.framework/FitnessCoachingServices](DYLIBS/FitnessCoachingServices.md)
- [/System/Library/PrivateFrameworks/FitnessFiltering.framework/FitnessFiltering](DYLIBS/FitnessFiltering.md)
- [/System/Library/PrivateFrameworks/FitnessUI.framework/FitnessUI](DYLIBS/FitnessUI.md)
- [/System/Library/PrivateFrameworks/FocusSettingsUI.framework/FocusSettingsUI](DYLIBS/FocusSettingsUI.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/libFontParser.dylib](DYLIBS/libFontParser.dylib.md)
- [/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/libGPUCompilerImpl.dylib](DYLIBS/libGPUCompilerImpl.dylib.md)
- [/System/Library/PrivateFrameworks/GRDBInternal.framework/GRDBInternal](DYLIBS/GRDBInternal.md)
- [/System/Library/PrivateFrameworks/GameCenterFoundation.framework/GameCenterFoundation](DYLIBS/GameCenterFoundation.md)
- [/System/Library/PrivateFrameworks/GameCenterOverlayService.framework/GameCenterOverlayService](DYLIBS/GameCenterOverlayService.md)
- [/System/Library/PrivateFrameworks/GameCenterServerClient.framework/GameCenterServerClient](DYLIBS/GameCenterServerClient.md)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/GameCenterUI](DYLIBS/GameCenterUI.md)
- [/System/Library/PrivateFrameworks/GameCenterUICore.framework/GameCenterUICore](DYLIBS/GameCenterUICore.md)
- [/System/Library/PrivateFrameworks/GameServices.framework/GameServices](DYLIBS/GameServices.md)
- [/System/Library/PrivateFrameworks/GameServicesCore.framework/GameServicesCore](DYLIBS/GameServicesCore.md)
- [/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/GenerativeAssistantActions](DYLIBS/GenerativeAssistantActions.md)
- [/System/Library/PrivateFrameworks/GenerativeAssistantSettings.framework/GenerativeAssistantSettings](DYLIBS/GenerativeAssistantSettings.md)
- [/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/GenerativeExperiencesRuntime](DYLIBS/GenerativeExperiencesRuntime.md)
- [/System/Library/PrivateFrameworks/GenerativeExperiencesUI.framework/GenerativeExperiencesUI](DYLIBS/GenerativeExperiencesUI.md)
- [/System/Library/PrivateFrameworks/GenerativeFunctionsFoundation.framework/GenerativeFunctionsFoundation](DYLIBS/GenerativeFunctionsFoundation.md)
- [/System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels](DYLIBS/GenerativeModels.md)
- [/System/Library/PrivateFrameworks/GeoServices.framework/GeoServices](DYLIBS/GeoServices.md)
- [/System/Library/PrivateFrameworks/HTTPTypesInternal.framework/HTTPTypesInternal](DYLIBS/HTTPTypesInternal.md)
- [/System/Library/PrivateFrameworks/Hands.framework/Hands](DYLIBS/Hands.md)
- [/System/Library/PrivateFrameworks/HeadGestures.framework/HeadGestures](DYLIBS/HeadGestures.md)
- [/System/Library/PrivateFrameworks/HealthArticlesUI.framework/HealthArticlesUI](DYLIBS/HealthArticlesUI.md)
- [/System/Library/PrivateFrameworks/HealthBalance.framework/HealthBalance](DYLIBS/HealthBalance.md)
- [/System/Library/PrivateFrameworks/HealthBalanceDaemon.framework/HealthBalanceDaemon](DYLIBS/HealthBalanceDaemon.md)
- [/System/Library/PrivateFrameworks/HealthBalanceUI.framework/HealthBalanceUI](DYLIBS/HealthBalanceUI.md)
- [/System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon](DYLIBS/HealthDaemon.md)
- [/System/Library/PrivateFrameworks/HealthExperience.framework/HealthExperience](DYLIBS/HealthExperience.md)
- [/System/Library/PrivateFrameworks/HealthExperienceUI.framework/HealthExperienceUI](DYLIBS/HealthExperienceUI.md)
- [/System/Library/PrivateFrameworks/HealthExposureNotificationUI.framework/HealthExposureNotificationUI](DYLIBS/HealthExposureNotificationUI.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsExperience.framework/HealthMedicationsExperience](DYLIBS/HealthMedicationsExperience.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsUI.framework/HealthMedicationsUI](DYLIBS/HealthMedicationsUI.md)
- [/System/Library/PrivateFrameworks/HealthMobilityUI.framework/HealthMobilityUI](DYLIBS/HealthMobilityUI.md)
- [/System/Library/PrivateFrameworks/HealthPlatformCore.framework/HealthPlatformCore](DYLIBS/HealthPlatformCore.md)
- [/System/Library/PrivateFrameworks/HealthPluginHost.framework/HealthPluginHost](DYLIBS/HealthPluginHost.md)
- [/System/Library/PrivateFrameworks/HealthRecordServices.framework/HealthRecordServices](DYLIBS/HealthRecordServices.md)
- [/System/Library/PrivateFrameworks/HealthRecordsDaemon.framework/HealthRecordsDaemon](DYLIBS/HealthRecordsDaemon.md)
- [/System/Library/PrivateFrameworks/HealthRecordsExtraction.framework/HealthRecordsExtraction](DYLIBS/HealthRecordsExtraction.md)
- [/System/Library/PrivateFrameworks/HealthRecordsUI.framework/HealthRecordsUI](DYLIBS/HealthRecordsUI.md)
- [/System/Library/PrivateFrameworks/HealthUI.framework/HealthUI](DYLIBS/HealthUI.md)
- [/System/Library/PrivateFrameworks/HealthVisualization.framework/HealthVisualization](DYLIBS/HealthVisualization.md)
- [/System/Library/PrivateFrameworks/HearingTest.framework/HearingTest](DYLIBS/HearingTest.md)
- [/System/Library/PrivateFrameworks/HearingTestUI.framework/HearingTestUI](DYLIBS/HearingTestUI.md)
- [/System/Library/PrivateFrameworks/HearingUI.framework/HearingUI](DYLIBS/HearingUI.md)
- [/System/Library/PrivateFrameworks/Home.framework/Home](DYLIBS/Home.md)
- [/System/Library/PrivateFrameworks/HomeAccessoryControlUI.framework/HomeAccessoryControlUI](DYLIBS/HomeAccessoryControlUI.md)
- [/System/Library/PrivateFrameworks/HomeAppIntents.framework/HomeAppIntents](DYLIBS/HomeAppIntents.md)
- [/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/HomeAutomationInternal](DYLIBS/HomeAutomationInternal.md)
- [/System/Library/PrivateFrameworks/HomeDataModel.framework/HomeDataModel](DYLIBS/HomeDataModel.md)
- [/System/Library/PrivateFrameworks/HomeEnergyDaemon.framework/HomeEnergyDaemon](DYLIBS/HomeEnergyDaemon.md)
- [/System/Library/PrivateFrameworks/HomeKitCore.framework/HomeKitCore](DYLIBS/HomeKitCore.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemon.framework/HomeKitDaemon](DYLIBS/HomeKitDaemon.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemonLegacy.framework/HomeKitDaemonLegacy](DYLIBS/HomeKitDaemonLegacy.md)
- [/System/Library/PrivateFrameworks/HomeKitEvents.framework/HomeKitEvents](DYLIBS/HomeKitEvents.md)
- [/System/Library/PrivateFrameworks/HomeKitMatter.framework/HomeKitMatter](DYLIBS/HomeKitMatter.md)
- [/System/Library/PrivateFrameworks/HomePlatformSettingsUI.framework/HomePlatformSettingsUI](DYLIBS/HomePlatformSettingsUI.md)
- [/System/Library/PrivateFrameworks/HomePodSettings.framework/HomePodSettings](DYLIBS/HomePodSettings.md)
- [/System/Library/PrivateFrameworks/HomeServices.framework/HomeServices](DYLIBS/HomeServices.md)
- [/System/Library/PrivateFrameworks/HomeSharing.framework/HomeSharing](DYLIBS/HomeSharing.md)
- [/System/Library/PrivateFrameworks/HomeUI.framework/HomeUI](DYLIBS/HomeUI.md)
- [/System/Library/PrivateFrameworks/HomeUI2.framework/HomeUI2](DYLIBS/HomeUI2.md)
- [/System/Library/PrivateFrameworks/HomeUtilityServices.framework/HomeUtilityServices](DYLIBS/HomeUtilityServices.md)
- [/System/Library/PrivateFrameworks/HoverTextUI.framework/HoverTextUI](DYLIBS/HoverTextUI.md)
- [/System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation](DYLIBS/IDSFoundation.md)
- [/System/Library/PrivateFrameworks/IMCore.framework/IMCore](DYLIBS/IMCore.md)
- [/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence](DYLIBS/IMDPersistence.md)
- [/System/Library/PrivateFrameworks/IMDaemonCore.framework/IMDaemonCore](DYLIBS/IMDaemonCore.md)
- [/System/Library/PrivateFrameworks/IMSharedUtilities.framework/IMSharedUtilities](DYLIBS/IMSharedUtilities.md)
- [/System/Library/PrivateFrameworks/IPTelephony.framework/Support/libIPTelephony.dylib](DYLIBS/libIPTelephony.dylib.md)
- [/System/Library/PrivateFrameworks/ImagePlaygroundInternal.framework/ImagePlaygroundInternal](DYLIBS/ImagePlaygroundInternal.md)
- [/System/Library/PrivateFrameworks/InputAccessoriesSettings.framework/InputAccessoriesSettings](DYLIBS/InputAccessoriesSettings.md)
- [/System/Library/PrivateFrameworks/InputAnalytics.framework/InputAnalytics](DYLIBS/InputAnalytics.md)
- [/System/Library/PrivateFrameworks/InputAnalyticsServer.framework/InputAnalyticsServer](DYLIBS/InputAnalyticsServer.md)
- [/System/Library/PrivateFrameworks/InstalledContentLibrary.framework/InstalledContentLibrary](DYLIBS/InstalledContentLibrary.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowContextRuntime.framework/IntelligenceFlowContextRuntime](DYLIBS/IntelligenceFlowContextRuntime.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/IntelligenceFlowPlannerRuntime](DYLIBS/IntelligenceFlowPlannerRuntime.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowPlannerSupport.framework/IntelligenceFlowPlannerSupport](DYLIBS/IntelligenceFlowPlannerSupport.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/IntelligenceFlowRuntime](DYLIBS/IntelligenceFlowRuntime.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatform.framework/IntelligencePlatform](DYLIBS/IntelligencePlatform.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/IntelligencePlatformCore](DYLIBS/IntelligencePlatformCore.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformLibrary.framework/IntelligencePlatformLibrary](DYLIBS/IntelligencePlatformLibrary.md)
- [/System/Library/PrivateFrameworks/IntelligentTrackingCore.framework/IntelligentTrackingCore](DYLIBS/IntelligentTrackingCore.md)
- [/System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf](DYLIBS/InternalSwiftProtobuf.md)
- [/System/Library/PrivateFrameworks/InternationalSupport.framework/InternationalSupport](DYLIBS/InternationalSupport.md)
- [/System/Library/PrivateFrameworks/JetCore.framework/JetCore](DYLIBS/JetCore.md)
- [/System/Library/PrivateFrameworks/JetEngine.framework/JetEngine](DYLIBS/JetEngine.md)
- [/System/Library/PrivateFrameworks/JetUI.framework/JetUI](DYLIBS/JetUI.md)
- [/System/Library/PrivateFrameworks/KnowledgeGraphKit.framework/KnowledgeGraphKit](DYLIBS/KnowledgeGraphKit.md)
- [/System/Library/PrivateFrameworks/KoaMapper.framework/KoaMapper](DYLIBS/KoaMapper.md)
- [/System/Library/PrivateFrameworks/LegalAndRegulatorySettingsSupport.framework/LegalAndRegulatorySettingsSupport](DYLIBS/LegalAndRegulatorySettingsSupport.md)
- [/System/Library/PrivateFrameworks/LiftUI.framework/LiftUI](DYLIBS/LiftUI.md)
- [/System/Library/PrivateFrameworks/LighthouseBackground.framework/LighthouseBackground](DYLIBS/LighthouseBackground.md)
- [/System/Library/PrivateFrameworks/LighthouseDataProcessor.framework/LighthouseDataProcessor](DYLIBS/LighthouseDataProcessor.md)
- [/System/Library/PrivateFrameworks/LinkMetadata.framework/LinkMetadata](DYLIBS/LinkMetadata.md)
- [/System/Library/PrivateFrameworks/LinkServices.framework/LinkServices](DYLIBS/LinkServices.md)
- [/System/Library/PrivateFrameworks/LiveExecutionResultsProbe.framework/LiveExecutionResultsProbe](DYLIBS/LiveExecutionResultsProbe.md)
- [/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore](DYLIBS/LocalAuthenticationCore.md)
- [/System/Library/PrivateFrameworks/MCCKitCategorization.framework/MCCKitCategorization](DYLIBS/MCCKitCategorization.md)
- [/System/Library/PrivateFrameworks/MLModelSpecification.framework/MLModelSpecification](DYLIBS/MLModelSpecification.md)
- [/System/Library/PrivateFrameworks/MMCS.framework/MMCS](DYLIBS/MMCS.md)
- [/System/Library/PrivateFrameworks/MagnifierSupport.framework/MagnifierSupport](DYLIBS/MagnifierSupport.md)
- [/System/Library/PrivateFrameworks/MailUI.framework/MailUI](DYLIBS/MailUI.md)
- [/System/Library/PrivateFrameworks/ManagedAppsCore.framework/ManagedAppsCore](DYLIBS/ManagedAppsCore.md)
- [/System/Library/PrivateFrameworks/ManagedAppsInterface.framework/ManagedAppsInterface](DYLIBS/ManagedAppsInterface.md)
- [/System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration](DYLIBS/ManagedConfiguration.md)
- [/System/Library/PrivateFrameworks/MapsSync.framework/MapsSync](DYLIBS/MapsSync.md)
- [/System/Library/PrivateFrameworks/MapsUI.framework/MapsUI](DYLIBS/MapsUI.md)
- [/System/Library/PrivateFrameworks/MatterPlugin.framework/MatterPlugin](DYLIBS/MatterPlugin.md)
- [/System/Library/PrivateFrameworks/MeasureFoundation.framework/MeasureFoundation](DYLIBS/MeasureFoundation.md)
- [/System/Library/PrivateFrameworks/MediaControls.framework/MediaControls](DYLIBS/MediaControls.md)
- [/System/Library/PrivateFrameworks/MediaCoreUI.framework/MediaCoreUI](DYLIBS/MediaCoreUI.md)
- [/System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience](DYLIBS/MediaExperience.md)
- [/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore](DYLIBS/MediaPlaybackCore.md)
- [/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote](DYLIBS/MediaRemote.md)
- [/System/Library/PrivateFrameworks/MedicalIDUI.framework/MedicalIDUI](DYLIBS/MedicalIDUI.md)
- [/System/Library/PrivateFrameworks/MentalHealthUI.framework/MentalHealthUI](DYLIBS/MentalHealthUI.md)
- [/System/Library/PrivateFrameworks/Mercury.framework/Mercury](DYLIBS/Mercury.md)
- [/System/Library/PrivateFrameworks/Message.framework/Message](DYLIBS/Message.md)
- [/System/Library/PrivateFrameworks/MessageProtection.framework/MessageProtection](DYLIBS/MessageProtection.md)
- [/System/Library/PrivateFrameworks/MetadataUtilities.framework/MetadataUtilities](DYLIBS/MetadataUtilities.md)
- [/System/Library/PrivateFrameworks/MetricsFramework.framework/MetricsFramework](DYLIBS/MetricsFramework.md)
- [/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon](DYLIBS/MicroLocationDaemon.md)
- [/System/Library/PrivateFrameworks/MicroLocationUtilities.framework/MicroLocationUtilities](DYLIBS/MicroLocationUtilities.md)
- [/System/Library/PrivateFrameworks/MigrationKit.framework/MigrationKit](DYLIBS/MigrationKit.md)
- [/System/Library/PrivateFrameworks/MobileActivation.framework/MobileActivation](DYLIBS/MobileActivation.md)
- [/System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset](DYLIBS/MobileAsset.md)
- [/System/Library/PrivateFrameworks/MobileSafari.framework/MobileSafari](DYLIBS/MobileSafari.md)
- [/System/Library/PrivateFrameworks/MobileSafariUI.framework/MobileSafariUI](DYLIBS/MobileSafariUI.md)
- [/System/Library/PrivateFrameworks/MobileSpotlightIndex.framework/MobileSpotlightIndex](DYLIBS/MobileSpotlightIndex.md)
- [/System/Library/PrivateFrameworks/MobileStoreDemoKit.framework/MobileStoreDemoKit](DYLIBS/MobileStoreDemoKit.md)
- [/System/Library/PrivateFrameworks/MobileStoreDemoSetupUI.framework/MobileStoreDemoSetupUI](DYLIBS/MobileStoreDemoSetupUI.md)
- [/System/Library/PrivateFrameworks/MobileTimerSupport.framework/MobileTimerSupport](DYLIBS/MobileTimerSupport.md)
- [/System/Library/PrivateFrameworks/ModelCatalog.framework/ModelCatalog](DYLIBS/ModelCatalog.md)
- [/System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/ModelCatalogRuntime](DYLIBS/ModelCatalogRuntime.md)
- [/System/Library/PrivateFrameworks/Morpheus.framework/Morpheus](DYLIBS/Morpheus.md)
- [/System/Library/PrivateFrameworks/MusicKitInternal.framework/MusicKitInternal](DYLIBS/MusicKitInternal.md)
- [/System/Library/PrivateFrameworks/MusicLibrary.framework/MusicLibrary](DYLIBS/MusicLibrary.md)
- [/System/Library/PrivateFrameworks/MusicUI.framework/MusicUI](DYLIBS/MusicUI.md)
- [/System/Library/PrivateFrameworks/NanoMailKitServer.framework/NanoMailKitServer](DYLIBS/NanoMailKitServer.md)
- [/System/Library/PrivateFrameworks/NanoPassKit.framework/NanoPassKit](DYLIBS/NanoPassKit.md)
- [/System/Library/PrivateFrameworks/NanoTimeKit.framework/NanoTimeKit](DYLIBS/NanoTimeKit.md)
- [/System/Library/PrivateFrameworks/NanoTimeKitCompanion.framework/NanoTimeKitCompanion](DYLIBS/NanoTimeKitCompanion.md)
- [/System/Library/PrivateFrameworks/NetworkInfo.framework/NetworkInfo](DYLIBS/NetworkInfo.md)
- [/System/Library/PrivateFrameworks/NetworkRelay.framework/NetworkRelay](DYLIBS/NetworkRelay.md)
- [/System/Library/PrivateFrameworks/NetworkServiceProxy.framework/NetworkServiceProxy](DYLIBS/NetworkServiceProxy.md)
- [/System/Library/PrivateFrameworks/NeuralNetworks.framework/NeuralNetworks](DYLIBS/NeuralNetworks.md)
- [/System/Library/PrivateFrameworks/NeutrinoCore.framework/NeutrinoCore](DYLIBS/NeutrinoCore.md)
- [/System/Library/PrivateFrameworks/NewsAds.framework/NewsAds](DYLIBS/NewsAds.md)
- [/System/Library/PrivateFrameworks/NewsAnalytics.framework/NewsAnalytics](DYLIBS/NewsAnalytics.md)
- [/System/Library/PrivateFrameworks/NewsAnalyticsUpload.framework/NewsAnalyticsUpload](DYLIBS/NewsAnalyticsUpload.md)
- [/System/Library/PrivateFrameworks/NewsArticles.framework/NewsArticles](DYLIBS/NewsArticles.md)
- [/System/Library/PrivateFrameworks/NewsCore.framework/NewsCore](DYLIBS/NewsCore.md)
- [/System/Library/PrivateFrameworks/NewsDaemon.framework/NewsDaemon](DYLIBS/NewsDaemon.md)
- [/System/Library/PrivateFrameworks/NewsFeed.framework/NewsFeed](DYLIBS/NewsFeed.md)
- [/System/Library/PrivateFrameworks/NewsLiveActivitiesCore.framework/NewsLiveActivitiesCore](DYLIBS/NewsLiveActivitiesCore.md)
- [/System/Library/PrivateFrameworks/NewsPersonalization.framework/NewsPersonalization](DYLIBS/NewsPersonalization.md)
- [/System/Library/PrivateFrameworks/NewsSubscription.framework/NewsSubscription](DYLIBS/NewsSubscription.md)
- [/System/Library/PrivateFrameworks/NewsToday.framework/NewsToday](DYLIBS/NewsToday.md)
- [/System/Library/PrivateFrameworks/NewsUI2.framework/NewsUI2](DYLIBS/NewsUI2.md)
- [/System/Library/PrivateFrameworks/NexusDaemon.framework/NexusDaemon](DYLIBS/NexusDaemon.md)
- [/System/Library/PrivateFrameworks/NightingaleTraining.framework/NightingaleTraining](DYLIBS/NightingaleTraining.md)
- [/System/Library/PrivateFrameworks/NotesEditor.framework/NotesEditor](DYLIBS/NotesEditor.md)
- [/System/Library/PrivateFrameworks/NotesShared.framework/NotesShared](DYLIBS/NotesShared.md)
- [/System/Library/PrivateFrameworks/ODCurareEvaluationAndReporting.framework/ODCurareEvaluationAndReporting](DYLIBS/ODCurareEvaluationAndReporting.md)
- [/System/Library/PrivateFrameworks/OSASubmissionClient.framework/OSASubmissionClient](DYLIBS/OSASubmissionClient.md)
- [/System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics](DYLIBS/OSAnalytics.md)
- [/System/Library/PrivateFrameworks/OSAnalyticsPrivate.framework/OSAnalyticsPrivate](DYLIBS/OSAnalyticsPrivate.md)
- [/System/Library/PrivateFrameworks/OSEligibility.framework/OSEligibility](DYLIBS/OSEligibility.md)
- [/System/Library/PrivateFrameworks/OnDeviceStorageCore.framework/OnDeviceStorageCore](DYLIBS/OnDeviceStorageCore.md)
- [/System/Library/PrivateFrameworks/OnDeviceStorageInternal.framework/OnDeviceStorageInternal](DYLIBS/OnDeviceStorageInternal.md)
- [/System/Library/PrivateFrameworks/Osprey.framework/Osprey](DYLIBS/Osprey.md)
- [/System/Library/PrivateFrameworks/PaperKit.framework/PaperKit](DYLIBS/PaperKit.md)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore](DYLIBS/PassKitCore.md)
- [/System/Library/PrivateFrameworks/PassKitUI.framework/PassKitUI](DYLIBS/PassKitUI.md)
- [/System/Library/PrivateFrameworks/PasswordManagerUI.framework/PasswordManagerUI](DYLIBS/PasswordManagerUI.md)
- [/System/Library/PrivateFrameworks/PegasusConfiguration.framework/PegasusConfiguration](DYLIBS/PegasusConfiguration.md)
- [/System/Library/PrivateFrameworks/PegasusKit.framework/PegasusKit](DYLIBS/PegasusKit.md)
- [/System/Library/PrivateFrameworks/PeopleSuggester.framework/PeopleSuggester](DYLIBS/PeopleSuggester.md)
- [/System/Library/PrivateFrameworks/PeopleSuggesterLighthouse.framework/PeopleSuggesterLighthouse](DYLIBS/PeopleSuggesterLighthouse.md)
- [/System/Library/PrivateFrameworks/PerfPowerServicesMetadata.framework/PerfPowerServicesMetadata](DYLIBS/PerfPowerServicesMetadata.md)
- [/System/Library/PrivateFrameworks/PersonalAudio.framework/PersonalAudio](DYLIBS/PersonalAudio.md)
- [/System/Library/PrivateFrameworks/PhotoAnalysis.framework/PhotoAnalysis](DYLIBS/PhotoAnalysis.md)
- [/System/Library/PrivateFrameworks/PhotoImaging.framework/PhotoImaging](DYLIBS/PhotoImaging.md)
- [/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/PhotoLibraryServices](DYLIBS/PhotoLibraryServices.md)
- [/System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/PhotoLibraryServicesCore](DYLIBS/PhotoLibraryServicesCore.md)
- [/System/Library/PrivateFrameworks/PhotosFace.framework/PhotosFace](DYLIBS/PhotosFace.md)
- [/System/Library/PrivateFrameworks/PhotosGraph.framework/PhotosGraph](DYLIBS/PhotosGraph.md)
- [/System/Library/PrivateFrameworks/PhotosIntelligence.framework/PhotosIntelligence](DYLIBS/PhotosIntelligence.md)
- [/System/Library/PrivateFrameworks/PhotosSwiftUICore.framework/PhotosSwiftUICore](DYLIBS/PhotosSwiftUICore.md)
- [/System/Library/PrivateFrameworks/PhotosUICore.framework/PhotosUICore](DYLIBS/PhotosUICore.md)
- [/System/Library/PrivateFrameworks/PhotosUIFoundation.framework/PhotosUIFoundation](DYLIBS/PhotosUIFoundation.md)
- [/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PhotosUIPrivate](DYLIBS/PhotosUIPrivate.md)
- [/System/Library/PrivateFrameworks/PlatformSSOCore.framework/PlatformSSOCore](DYLIBS/PlatformSSOCore.md)
- [/System/Library/PrivateFrameworks/PnROnDeviceFramework.framework/PnROnDeviceFramework](DYLIBS/PnROnDeviceFramework.md)
- [/System/Library/PrivateFrameworks/PodcastsFoundation.framework/PodcastsFoundation](DYLIBS/PodcastsFoundation.md)
- [/System/Library/PrivateFrameworks/PodcastsKit.framework/PodcastsKit](DYLIBS/PodcastsKit.md)
- [/System/Library/PrivateFrameworks/PodcastsUI.framework/PodcastsUI](DYLIBS/PodcastsUI.md)
- [/System/Library/PrivateFrameworks/PoirotBlocks.framework/PoirotBlocks](DYLIBS/PoirotBlocks.md)
- [/System/Library/PrivateFrameworks/PoirotSchematizer.framework/PoirotSchematizer](DYLIBS/PoirotSchematizer.md)
- [/System/Library/PrivateFrameworks/PoirotUDFs.framework/PoirotUDFs](DYLIBS/PoirotUDFs.md)
- [/System/Library/PrivateFrameworks/PosterBoard.framework/PosterBoard](DYLIBS/PosterBoard.md)
- [/System/Library/PrivateFrameworks/PosterKit.framework/PosterKit](DYLIBS/PosterKit.md)
- [/System/Library/PrivateFrameworks/PowerUI.framework/PowerUI](DYLIBS/PowerUI.md)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore](DYLIBS/PowerlogCore.md)
- [/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators](DYLIBS/PowerlogHelperdOperators.md)
- [/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators](DYLIBS/PowerlogLiteOperators.md)
- [/System/Library/PrivateFrameworks/PreferencesExtended.framework/PreferencesExtended](DYLIBS/PreferencesExtended.md)
- [/System/Library/PrivateFrameworks/PreviewShellKit.framework/PreviewShellKit](DYLIBS/PreviewShellKit.md)
- [/System/Library/PrivateFrameworks/PreviewsInjection.framework/PreviewsInjection](DYLIBS/PreviewsInjection.md)
- [/System/Library/PrivateFrameworks/PreviewsServicesUI.framework/PreviewsServicesUI](DYLIBS/PreviewsServicesUI.md)
- [/System/Library/PrivateFrameworks/PrivateCloudCompute.framework/PrivateCloudCompute](DYLIBS/PrivateCloudCompute.md)
- [/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PrivateFederatedLearning](DYLIBS/PrivateFederatedLearning.md)
- [/System/Library/PrivateFrameworks/PrivateMLClient.framework/PrivateMLClient](DYLIBS/PrivateMLClient.md)
- [/System/Library/PrivateFrameworks/ProactiveExperiments.framework/ProactiveExperiments](DYLIBS/ProactiveExperiments.md)
- [/System/Library/PrivateFrameworks/ProactiveExperimentsInternals.framework/ProactiveExperimentsInternals](DYLIBS/ProactiveExperimentsInternals.md)
- [/System/Library/PrivateFrameworks/ProactiveHarvesting.framework/ProactiveHarvesting](DYLIBS/ProactiveHarvesting.md)
- [/System/Library/PrivateFrameworks/ProactiveML.framework/ProactiveML](DYLIBS/ProactiveML.md)
- [/System/Library/PrivateFrameworks/ProactiveSummarization.framework/ProactiveSummarization](DYLIBS/ProactiveSummarization.md)
- [/System/Library/PrivateFrameworks/ProactiveSummarizationClient.framework/ProactiveSummarizationClient](DYLIBS/ProactiveSummarizationClient.md)
- [/System/Library/PrivateFrameworks/ProductKit.framework/ProductKit](DYLIBS/ProductKit.md)
- [/System/Library/PrivateFrameworks/PromotedContent.framework/PromotedContent](DYLIBS/PromotedContent.md)
- [/System/Library/PrivateFrameworks/PromotedContentJetSupport.framework/PromotedContentJetSupport](DYLIBS/PromotedContentJetSupport.md)
- [/System/Library/PrivateFrameworks/PromotedContentUI.framework/PromotedContentUI](DYLIBS/PromotedContentUI.md)
- [/System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/ProtectedCloudStorage](DYLIBS/ProtectedCloudStorage.md)
- [/System/Library/PrivateFrameworks/ProximityAppleIDSetup.framework/ProximityAppleIDSetup](DYLIBS/ProximityAppleIDSetup.md)
- [/System/Library/PrivateFrameworks/ProximityAppleIDSetupUI.framework/ProximityAppleIDSetupUI](DYLIBS/ProximityAppleIDSetupUI.md)
- [/System/Library/PrivateFrameworks/ProximityReaderCore.framework/ProximityReaderCore](DYLIBS/ProximityReaderCore.md)
- [/System/Library/PrivateFrameworks/ProximityReaderDaemon.framework/ProximityReaderDaemon](DYLIBS/ProximityReaderDaemon.md)
- [/System/Library/PrivateFrameworks/QueryParser.framework/QueryParser](DYLIBS/QueryParser.md)
- [/System/Library/PrivateFrameworks/RapidResourceDelivery.framework/RapidResourceDelivery](DYLIBS/RapidResourceDelivery.md)
- [/System/Library/PrivateFrameworks/Recount.framework/Recount](DYLIBS/Recount.md)
- [/System/Library/PrivateFrameworks/RegulatoryDomain.framework/RegulatoryDomain](DYLIBS/RegulatoryDomain.md)
- [/System/Library/PrivateFrameworks/ReminderKitInternal.framework/ReminderKitInternal](DYLIBS/ReminderKitInternal.md)
- [/System/Library/PrivateFrameworks/RemindersUICore.framework/RemindersUICore](DYLIBS/RemindersUICore.md)
- [/System/Library/PrivateFrameworks/RemotePairingDevice.framework/RemotePairingDevice](DYLIBS/RemotePairingDevice.md)
- [/System/Library/PrivateFrameworks/RemoteTextInput.framework/RemoteTextInput](DYLIBS/RemoteTextInput.md)
- [/System/Library/PrivateFrameworks/RenderBox.framework/RenderBox](DYLIBS/RenderBox.md)
- [/System/Library/PrivateFrameworks/ReplicatorCore.framework/ReplicatorCore](DYLIBS/ReplicatorCore.md)
- [/System/Library/PrivateFrameworks/ReplicatorEngine.framework/ReplicatorEngine](DYLIBS/ReplicatorEngine.md)
- [/System/Library/PrivateFrameworks/ReplicatorServices.framework/ReplicatorServices](DYLIBS/ReplicatorServices.md)
- [/System/Library/PrivateFrameworks/RequestDispatcherBridges.framework/RequestDispatcherBridges](DYLIBS/RequestDispatcherBridges.md)
- [/System/Library/PrivateFrameworks/RunningBoard.framework/RunningBoard](DYLIBS/RunningBoard.md)
- [/System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices](DYLIBS/RunningBoardServices.md)
- [/System/Library/PrivateFrameworks/SEService.framework/SEService](DYLIBS/SEService.md)
- [/System/Library/PrivateFrameworks/SPOwner.framework/SPOwner](DYLIBS/SPOwner.md)
- [/System/Library/PrivateFrameworks/SPRCore.framework/SPRCore](DYLIBS/SPRCore.md)
- [/System/Library/PrivateFrameworks/SafariCore.framework/SafariCore](DYLIBS/SafariCore.md)
- [/System/Library/PrivateFrameworks/SafariShared.framework/SafariShared](DYLIBS/SafariShared.md)
- [/System/Library/PrivateFrameworks/SafariSharedUI.framework/SafariSharedUI](DYLIBS/SafariSharedUI.md)
- [/System/Library/PrivateFrameworks/SafetyMonitorUI.framework/SafetyMonitorUI](DYLIBS/SafetyMonitorUI.md)
- [/System/Library/PrivateFrameworks/SampleAnalysis.framework/SampleAnalysis](DYLIBS/SampleAnalysis.md)
- [/System/Library/PrivateFrameworks/SavageCameraInterface.framework/SavageCameraInterface](DYLIBS/SavageCameraInterface.md)
- [/System/Library/PrivateFrameworks/ScreenReaderCore.framework/ScreenReaderCore](DYLIBS/ScreenReaderCore.md)
- [/System/Library/PrivateFrameworks/ScreenReaderOutput.framework/ScreenReaderOutput](DYLIBS/ScreenReaderOutput.md)
- [/System/Library/PrivateFrameworks/ScreenSharingKit.framework/ScreenSharingKit](DYLIBS/ScreenSharingKit.md)
- [/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore](DYLIBS/ScreenTimeCore.md)
- [/System/Library/PrivateFrameworks/ScreenTimeSettingsUI.framework/ScreenTimeSettingsUI](DYLIBS/ScreenTimeSettingsUI.md)
- [/System/Library/PrivateFrameworks/ScreenTimeUICore.framework/ScreenTimeUICore](DYLIBS/ScreenTimeUICore.md)
- [/System/Library/PrivateFrameworks/SearchAssets.framework/SearchAssets](DYLIBS/SearchAssets.md)
- [/System/Library/PrivateFrameworks/SearchOnDeviceAnalytics.framework/SearchOnDeviceAnalytics](DYLIBS/SearchOnDeviceAnalytics.md)
- [/System/Library/PrivateFrameworks/SearchUI.framework/SearchUI](DYLIBS/SearchUI.md)
- [/System/Library/PrivateFrameworks/SecureTransactionService.framework/SecureTransactionService](DYLIBS/SecureTransactionService.md)
- [/System/Library/PrivateFrameworks/SensitiveContentAnalysisML.framework/SensitiveContentAnalysisML](DYLIBS/SensitiveContentAnalysisML.md)
- [/System/Library/PrivateFrameworks/SensitiveContentAnalysisUI.framework/SensitiveContentAnalysisUI](DYLIBS/SensitiveContentAnalysisUI.md)
- [/System/Library/PrivateFrameworks/SessionCore.framework/SessionCore](DYLIBS/SessionCore.md)
- [/System/Library/PrivateFrameworks/SessionSyncEngine.framework/SessionSyncEngine](DYLIBS/SessionSyncEngine.md)
- [/System/Library/PrivateFrameworks/Settings.framework/Settings](DYLIBS/Settings.md)
- [/System/Library/PrivateFrameworks/SettingsFoundation.framework/SettingsFoundation](DYLIBS/SettingsFoundation.md)
- [/System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant](DYLIBS/SetupAssistant.md)
- [/System/Library/PrivateFrameworks/SetupAssistantUI.framework/SetupAssistantUI](DYLIBS/SetupAssistantUI.md)
- [/System/Library/PrivateFrameworks/SeymourClient.framework/SeymourClient](DYLIBS/SeymourClient.md)
- [/System/Library/PrivateFrameworks/SeymourCore.framework/SeymourCore](DYLIBS/SeymourCore.md)
- [/System/Library/PrivateFrameworks/SeymourMedia.framework/SeymourMedia](DYLIBS/SeymourMedia.md)
- [/System/Library/PrivateFrameworks/SeymourServices.framework/SeymourServices](DYLIBS/SeymourServices.md)
- [/System/Library/PrivateFrameworks/SeymourSessionServices.framework/SeymourSessionServices](DYLIBS/SeymourSessionServices.md)
- [/System/Library/PrivateFrameworks/SeymourUI.framework/SeymourUI](DYLIBS/SeymourUI.md)
- [/System/Library/PrivateFrameworks/ShaderGraph.framework/ShaderGraph](DYLIBS/ShaderGraph.md)
- [/System/Library/PrivateFrameworks/ShareSheet.framework/ShareSheet](DYLIBS/ShareSheet.md)
- [/System/Library/PrivateFrameworks/Sharing.framework/Sharing](DYLIBS/Sharing.md)
- [/System/Library/PrivateFrameworks/SharingHUD.framework/SharingHUD](DYLIBS/SharingHUD.md)
- [/System/Library/PrivateFrameworks/SharingXPCServices.framework/SharingXPCServices](DYLIBS/SharingXPCServices.md)
- [/System/Library/PrivateFrameworks/ShazamEvents.framework/ShazamEvents](DYLIBS/ShazamEvents.md)
- [/System/Library/PrivateFrameworks/ShazamKitUI.framework/ShazamKitUI](DYLIBS/ShazamKitUI.md)
- [/System/Library/PrivateFrameworks/ShellSceneKit.framework/ShellSceneKit](DYLIBS/ShellSceneKit.md)
- [/System/Library/PrivateFrameworks/ShimGameServices.framework/ShimGameServices](DYLIBS/ShimGameServices.md)
- [/System/Library/PrivateFrameworks/SignpostSupport.framework/SignpostSupport](DYLIBS/SignpostSupport.md)
- [/System/Library/PrivateFrameworks/SiriAnalytics.framework/SiriAnalytics](DYLIBS/SiriAnalytics.md)
- [/System/Library/PrivateFrameworks/SiriAppLaunchIntents.framework/SiriAppLaunchIntents](DYLIBS/SiriAppLaunchIntents.md)
- [/System/Library/PrivateFrameworks/SiriAudioInternal.framework/SiriAudioInternal](DYLIBS/SiriAudioInternal.md)
- [/System/Library/PrivateFrameworks/SiriAudioSupport.framework/SiriAudioSupport](DYLIBS/SiriAudioSupport.md)
- [/System/Library/PrivateFrameworks/SiriAutoComplete.framework/SiriAutoComplete](DYLIBS/SiriAutoComplete.md)
- [/System/Library/PrivateFrameworks/SiriAutoCompleteAPI.framework/SiriAutoCompleteAPI](DYLIBS/SiriAutoCompleteAPI.md)
- [/System/Library/PrivateFrameworks/SiriCalendarIntents.framework/SiriCalendarIntents](DYLIBS/SiriCalendarIntents.md)
- [/System/Library/PrivateFrameworks/SiriCam.framework/SiriCam](DYLIBS/SiriCam.md)
- [/System/Library/PrivateFrameworks/SiriCarCommandsIntents.framework/SiriCarCommandsIntents](DYLIBS/SiriCarCommandsIntents.md)
- [/System/Library/PrivateFrameworks/SiriContactsIntents.framework/SiriContactsIntents](DYLIBS/SiriContactsIntents.md)
- [/System/Library/PrivateFrameworks/SiriCoreMetrics.framework/SiriCoreMetrics](DYLIBS/SiriCoreMetrics.md)
- [/System/Library/PrivateFrameworks/SiriCrossDeviceArbitration.framework/SiriCrossDeviceArbitration](DYLIBS/SiriCrossDeviceArbitration.md)
- [/System/Library/PrivateFrameworks/SiriExpanseInternal.framework/SiriExpanseInternal](DYLIBS/SiriExpanseInternal.md)
- [/System/Library/PrivateFrameworks/SiriFindMy.framework/SiriFindMy](DYLIBS/SiriFindMy.md)
- [/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/SiriIdentityInternal](DYLIBS/SiriIdentityInternal.md)
- [/System/Library/PrivateFrameworks/SiriInCall.framework/SiriInCall](DYLIBS/SiriInCall.md)
- [/System/Library/PrivateFrameworks/SiriInference.framework/SiriInference](DYLIBS/SiriInference.md)
- [/System/Library/PrivateFrameworks/SiriInformationSearch.framework/SiriInformationSearch](DYLIBS/SiriInformationSearch.md)
- [/System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation](DYLIBS/SiriInstrumentation.md)
- [/System/Library/PrivateFrameworks/SiriKitFlow.framework/SiriKitFlow](DYLIBS/SiriKitFlow.md)
- [/System/Library/PrivateFrameworks/SiriKitRuntime.framework/SiriKitRuntime](DYLIBS/SiriKitRuntime.md)
- [/System/Library/PrivateFrameworks/SiriMailInternal.framework/SiriMailInternal](DYLIBS/SiriMailInternal.md)
- [/System/Library/PrivateFrameworks/SiriMessageTypes.framework/SiriMessageTypes](DYLIBS/SiriMessageTypes.md)
- [/System/Library/PrivateFrameworks/SiriMessagesFlow.framework/SiriMessagesFlow](DYLIBS/SiriMessagesFlow.md)
- [/System/Library/PrivateFrameworks/SiriMessagesUI.framework/SiriMessagesUI](DYLIBS/SiriMessagesUI.md)
- [/System/Library/PrivateFrameworks/SiriNLUTypes.framework/SiriNLUTypes](DYLIBS/SiriNLUTypes.md)
- [/System/Library/PrivateFrameworks/SiriNetwork.framework/SiriNetwork](DYLIBS/SiriNetwork.md)
- [/System/Library/PrivateFrameworks/SiriNotebook.framework/SiriNotebook](DYLIBS/SiriNotebook.md)
- [/System/Library/PrivateFrameworks/SiriNotebookUI.framework/SiriNotebookUI](DYLIBS/SiriNotebookUI.md)
- [/System/Library/PrivateFrameworks/SiriNotificationsIntents.framework/SiriNotificationsIntents](DYLIBS/SiriNotificationsIntents.md)
- [/System/Library/PrivateFrameworks/SiriOntology.framework/SiriOntology](DYLIBS/SiriOntology.md)
- [/System/Library/PrivateFrameworks/SiriOntologyProtobuf.framework/SiriOntologyProtobuf](DYLIBS/SiriOntologyProtobuf.md)
- [/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/SiriPlaybackControlIntents](DYLIBS/SiriPlaybackControlIntents.md)
- [/System/Library/PrivateFrameworks/SiriPlaybackControlSupport.framework/SiriPlaybackControlSupport](DYLIBS/SiriPlaybackControlSupport.md)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningAnalytics.framework/SiriPrivateLearningAnalytics](DYLIBS/SiriPrivateLearningAnalytics.md)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningInference.framework/SiriPrivateLearningInference](DYLIBS/SiriPrivateLearningInference.md)
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
- [/System/Library/PrivateFrameworks/SiriTTSService.framework/SiriTTSService](DYLIBS/SiriTTSService.md)
- [/System/Library/PrivateFrameworks/SiriTranslationIntents.framework/SiriTranslationIntents](DYLIBS/SiriTranslationIntents.md)
- [/System/Library/PrivateFrameworks/SiriUtilities.framework/SiriUtilities](DYLIBS/SiriUtilities.md)
- [/System/Library/PrivateFrameworks/SiriVideoIntents.framework/SiriVideoIntents](DYLIBS/SiriVideoIntents.md)
- [/System/Library/PrivateFrameworks/SleepHealthUI.framework/SleepHealthUI](DYLIBS/SleepHealthUI.md)
- [/System/Library/PrivateFrameworks/SleepWidgetUI.framework/SleepWidgetUI](DYLIBS/SleepWidgetUI.md)
- [/System/Library/PrivateFrameworks/SmartReplies.framework/SmartReplies](DYLIBS/SmartReplies.md)
- [/System/Library/PrivateFrameworks/SnippetKit.framework/SnippetKit](DYLIBS/SnippetKit.md)
- [/System/Library/PrivateFrameworks/SnippetUI.framework/SnippetUI](DYLIBS/SnippetUI.md)
- [/System/Library/PrivateFrameworks/SocialLayer.framework/SocialLayer](DYLIBS/SocialLayer.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/SoftwareUpdateCore](DYLIBS/SoftwareUpdateCore.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateSettingsUI.framework/SoftwareUpdateSettingsUI](DYLIBS/SoftwareUpdateSettingsUI.md)
- [/System/Library/PrivateFrameworks/SonicFoundation.framework/SonicFoundation](DYLIBS/SonicFoundation.md)
- [/System/Library/PrivateFrameworks/SonicKit.framework/SonicKit](DYLIBS/SonicKit.md)
- [/System/Library/PrivateFrameworks/SpeechRecognitionCommandAndControl.framework/SpeechRecognitionCommandAndControl](DYLIBS/SpeechRecognitionCommandAndControl.md)
- [/System/Library/PrivateFrameworks/SpeechRecognitionCommandServices.framework/SpeechRecognitionCommandServices](DYLIBS/SpeechRecognitionCommandServices.md)
- [/System/Library/PrivateFrameworks/SportsKit.framework/SportsKit](DYLIBS/SportsKit.md)
- [/System/Library/PrivateFrameworks/Spotlight.framework/Spotlight](DYLIBS/Spotlight.md)
- [/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon](DYLIBS/SpotlightDaemon.md)
- [/System/Library/PrivateFrameworks/SpotlightFoundation.framework/SpotlightFoundation](DYLIBS/SpotlightFoundation.md)
- [/System/Library/PrivateFrameworks/SpotlightKnowledge.framework/SpotlightKnowledge](DYLIBS/SpotlightKnowledge.md)
- [/System/Library/PrivateFrameworks/SpotlightLinguistics.framework/SpotlightLinguistics](DYLIBS/SpotlightLinguistics.md)
- [/System/Library/PrivateFrameworks/SpotlightRecommendation.framework/SpotlightRecommendation](DYLIBS/SpotlightRecommendation.md)
- [/System/Library/PrivateFrameworks/SpotlightServices.framework/SpotlightServices](DYLIBS/SpotlightServices.md)
- [/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard](DYLIBS/SpringBoard.md)
- [/System/Library/PrivateFrameworks/SpringBoardHome.framework/SpringBoardHome](DYLIBS/SpringBoardHome.md)
- [/System/Library/PrivateFrameworks/Stickers.framework/Stickers](DYLIBS/Stickers.md)
- [/System/Library/PrivateFrameworks/StocksCore.framework/StocksCore](DYLIBS/StocksCore.md)
- [/System/Library/PrivateFrameworks/StocksPersonalization.framework/StocksPersonalization](DYLIBS/StocksPersonalization.md)
- [/System/Library/PrivateFrameworks/StocksUI.framework/StocksUI](DYLIBS/StocksUI.md)
- [/System/Library/PrivateFrameworks/StoreServices.framework/StoreServices](DYLIBS/StoreServices.md)
- [/System/Library/PrivateFrameworks/SuggestionsSpotlightMetrics.framework/SuggestionsSpotlightMetrics](DYLIBS/SuggestionsSpotlightMetrics.md)
- [/System/Library/PrivateFrameworks/SummarizationKit.framework/SummarizationKit](DYLIBS/SummarizationKit.md)
- [/System/Library/PrivateFrameworks/Symbolication.framework/Symbolication](DYLIBS/Symbolication.md)
- [/System/Library/PrivateFrameworks/SymptomLinkAdvisory.framework/SymptomLinkAdvisory](DYLIBS/SymptomLinkAdvisory.md)
- [/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomAnalytics.framework/SymptomAnalytics](DYLIBS/SymptomAnalytics.md)
- [/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomEvaluator.framework/SymptomEvaluator](DYLIBS/SymptomEvaluator.md)
- [/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomPresentationFeed.framework/SymptomPresentationFeed](DYLIBS/SymptomPresentationFeed.md)
- [/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomPresentationLite.framework/SymptomPresentationLite](DYLIBS/SymptomPresentationLite.md)
- [/System/Library/PrivateFrameworks/SystemServiceMonitor.framework/SystemServiceMonitor](DYLIBS/SystemServiceMonitor.md)
- [/System/Library/PrivateFrameworks/TDGSharing.framework/TDGSharing](DYLIBS/TDGSharing.md)
- [/System/Library/PrivateFrameworks/TVAppServices.framework/TVAppServices](DYLIBS/TVAppServices.md)
- [/System/Library/PrivateFrameworks/TVLatency.framework/TVLatency](DYLIBS/TVLatency.md)
- [/System/Library/PrivateFrameworks/TVRemoteCore.framework/TVRemoteCore](DYLIBS/TVRemoteCore.md)
- [/System/Library/PrivateFrameworks/TVRemoteUI.framework/TVRemoteUI](DYLIBS/TVRemoteUI.md)
- [/System/Library/PrivateFrameworks/Tabi.framework/Tabi](DYLIBS/Tabi.md)
- [/System/Library/PrivateFrameworks/TeaBreeze.framework/TeaBreeze](DYLIBS/TeaBreeze.md)
- [/System/Library/PrivateFrameworks/TeaDB.framework/TeaDB](DYLIBS/TeaDB.md)
- [/System/Library/PrivateFrameworks/TeaFoundation.framework/TeaFoundation](DYLIBS/TeaFoundation.md)
- [/System/Library/PrivateFrameworks/TeaSettings.framework/TeaSettings](DYLIBS/TeaSettings.md)
- [/System/Library/PrivateFrameworks/TeaTemplate.framework/TeaTemplate](DYLIBS/TeaTemplate.md)
- [/System/Library/PrivateFrameworks/TeaUI.framework/TeaUI](DYLIBS/TeaUI.md)
- [/System/Library/PrivateFrameworks/TelephonyBlastDoorSupport.framework/TelephonyBlastDoorSupport](DYLIBS/TelephonyBlastDoorSupport.md)
- [/System/Library/PrivateFrameworks/TelephonyKit.framework/TelephonyKit](DYLIBS/TelephonyKit.md)
- [/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer](DYLIBS/TextComposer.md)
- [/System/Library/PrivateFrameworks/TextInputCore.framework/TextInputCore](DYLIBS/TextInputCore.md)
- [/System/Library/PrivateFrameworks/TextInputUI.framework/TextInputUI](DYLIBS/TextInputUI.md)
- [/System/Library/PrivateFrameworks/TextRecognition.framework/TextRecognition](DYLIBS/TextRecognition.md)
- [/System/Library/PrivateFrameworks/TextToSpeech.framework/TextToSpeech](DYLIBS/TextToSpeech.md)
- [/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingUI.framework/TextToSpeechVoiceBankingUI](DYLIBS/TextToSpeechVoiceBankingUI.md)
- [/System/Library/PrivateFrameworks/ThirdPartyApplicationSettings.framework/ThirdPartyApplicationSettings](DYLIBS/ThirdPartyApplicationSettings.md)
- [/System/Library/PrivateFrameworks/TipKitCore.framework/TipKitCore](DYLIBS/TipKitCore.md)
- [/System/Library/PrivateFrameworks/TipsCore.framework/TipsCore](DYLIBS/TipsCore.md)
- [/System/Library/PrivateFrameworks/TipsDaemon.framework/TipsDaemon](DYLIBS/TipsDaemon.md)
- [/System/Library/PrivateFrameworks/TipsTryIt.framework/TipsTryIt](DYLIBS/TipsTryIt.md)
- [/System/Library/PrivateFrameworks/TokenGenerationCore.framework/TokenGenerationCore](DYLIBS/TokenGenerationCore.md)
- [/System/Library/PrivateFrameworks/TokenGenerationInference.framework/TokenGenerationInference](DYLIBS/TokenGenerationInference.md)
- [/System/Library/PrivateFrameworks/ToneKit.framework/ToneKit](DYLIBS/ToneKit.md)
- [/System/Library/PrivateFrameworks/ToolKit.framework/ToolKit](DYLIBS/ToolKit.md)
- [/System/Library/PrivateFrameworks/TranslationDaemon.framework/TranslationDaemon](DYLIBS/TranslationDaemon.md)
- [/System/Library/PrivateFrameworks/TranslationUI.framework/TranslationUI](DYLIBS/TranslationUI.md)
- [/System/Library/PrivateFrameworks/TrialProto.framework/TrialProto](DYLIBS/TrialProto.md)
- [/System/Library/PrivateFrameworks/TrialServer.framework/TrialServer](DYLIBS/TrialServer.md)
- [/System/Library/PrivateFrameworks/TrustKit.framework/TrustKit](DYLIBS/TrustKit.md)
- [/System/Library/PrivateFrameworks/UIIntelligenceIntents.framework/UIIntelligenceIntents](DYLIBS/UIIntelligenceIntents.md)
- [/System/Library/PrivateFrameworks/UIIntelligenceSupport.framework/UIIntelligenceSupport](DYLIBS/UIIntelligenceSupport.md)
- [/System/Library/PrivateFrameworks/UIIntelligenceSupportAgent.framework/UIIntelligenceSupportAgent](DYLIBS/UIIntelligenceSupportAgent.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore](DYLIBS/UIKitCore.md)
- [/System/Library/PrivateFrameworks/UIUnderstanding.framework/UIUnderstanding](DYLIBS/UIUnderstanding.md)
- [/System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework](DYLIBS/UnifiedAssetFramework.md)
- [/System/Library/PrivateFrameworks/UnifiedMessagingKit.framework/UnifiedMessagingKit](DYLIBS/UnifiedMessagingKit.md)
- [/System/Library/PrivateFrameworks/UniversalDrag.framework/UniversalDrag](DYLIBS/UniversalDrag.md)
- [/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_apfs.dylib](DYLIBS/livefiles_apfs.dylib.md)
- [/System/Library/PrivateFrameworks/UserNotificationsCore.framework/UserNotificationsCore](DYLIBS/UserNotificationsCore.md)
- [/System/Library/PrivateFrameworks/UserNotificationsKit.framework/UserNotificationsKit](DYLIBS/UserNotificationsKit.md)
- [/System/Library/PrivateFrameworks/UserNotificationsUIKit.framework/UserNotificationsUIKit](DYLIBS/UserNotificationsUIKit.md)
- [/System/Library/PrivateFrameworks/VFX.framework/VFX](DYLIBS/VFX.md)
- [/System/Library/PrivateFrameworks/VectorKit.framework/VectorKit](DYLIBS/VectorKit.md)
- [/System/Library/PrivateFrameworks/VectorSearch.framework/VectorSearch](DYLIBS/VectorSearch.md)
- [/System/Library/PrivateFrameworks/VideosUI.framework/VideosUI](DYLIBS/VideosUI.md)
- [/System/Library/PrivateFrameworks/VideosUICore.framework/VideosUICore](DYLIBS/VideosUICore.md)
- [/System/Library/PrivateFrameworks/VisionCompanion.framework/VisionCompanion](DYLIBS/VisionCompanion.md)
- [/System/Library/PrivateFrameworks/VisionHWAccelerationServices.framework/VisionHWAccelerationServices](DYLIBS/VisionHWAccelerationServices.md)
- [/System/Library/PrivateFrameworks/VisualGeneration.framework/VisualGeneration](DYLIBS/VisualGeneration.md)
- [/System/Library/PrivateFrameworks/VisualIntelligence.framework/VisualIntelligence](DYLIBS/VisualIntelligence.md)
- [/System/Library/PrivateFrameworks/VisualUnderstanding.framework/VisualUnderstanding](DYLIBS/VisualUnderstanding.md)
- [/System/Library/PrivateFrameworks/VoiceActions.framework/VoiceActions](DYLIBS/VoiceActions.md)
- [/System/Library/PrivateFrameworks/VoiceControlUI.framework/VoiceControlUI](DYLIBS/VoiceControlUI.md)
- [/System/Library/PrivateFrameworks/VoiceShortcutClient.framework/VoiceShortcutClient](DYLIBS/VoiceShortcutClient.md)
- [/System/Library/PrivateFrameworks/VoiceShortcuts.framework/VoiceShortcuts](DYLIBS/VoiceShortcuts.md)
- [/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/VoiceTriggerUI](DYLIBS/VoiceTriggerUI.md)
- [/System/Library/PrivateFrameworks/WallpaperKit.framework/WallpaperKit](DYLIBS/WallpaperKit.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/WatchFacesWallpaperSupport](DYLIBS/WatchFacesWallpaperSupport.md)
- [/System/Library/PrivateFrameworks/WatchListKit.framework/WatchListKit](DYLIBS/WatchListKit.md)
- [/System/Library/PrivateFrameworks/WeatherAnalytics.framework/WeatherAnalytics](DYLIBS/WeatherAnalytics.md)
- [/System/Library/PrivateFrameworks/WeatherCore.framework/WeatherCore](DYLIBS/WeatherCore.md)
- [/System/Library/PrivateFrameworks/WeatherDaemon.framework/WeatherDaemon](DYLIBS/WeatherDaemon.md)
- [/System/Library/PrivateFrameworks/WeatherMaps.framework/WeatherMaps](DYLIBS/WeatherMaps.md)
- [/System/Library/PrivateFrameworks/WeatherUI.framework/WeatherUI](DYLIBS/WeatherUI.md)
- [/System/Library/PrivateFrameworks/WebApp.framework/WebApp](DYLIBS/WebApp.md)
- [/System/Library/PrivateFrameworks/WebBookmarksSwift.framework/WebBookmarksSwift](DYLIBS/WebBookmarksSwift.md)
- [/System/Library/PrivateFrameworks/WebCore.framework/WebCore](DYLIBS/WebCore.md)
- [/System/Library/PrivateFrameworks/WebGPU.framework/WebGPU](DYLIBS/WebGPU.md)
- [/System/Library/PrivateFrameworks/WebKitLegacy.framework/WebKitLegacy](DYLIBS/WebKitLegacy.md)
- [/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics](DYLIBS/WiFiAnalytics.md)
- [/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit](DYLIBS/WiFiKit.md)
- [/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy](DYLIBS/WiFiPolicy.md)
- [/System/Library/PrivateFrameworks/WidgetRenderer.framework/WidgetRenderer](DYLIBS/WidgetRenderer.md)
- [/System/Library/PrivateFrameworks/WorkflowEditor.framework/WorkflowEditor](DYLIBS/WorkflowEditor.md)
- [/System/Library/PrivateFrameworks/WorkflowKit.framework/WorkflowKit](DYLIBS/WorkflowKit.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/WorkflowUI](DYLIBS/WorkflowUI.md)
- [/System/Library/PrivateFrameworks/WorkflowUICore.framework/WorkflowUICore](DYLIBS/WorkflowUICore.md)
- [/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/WorkoutAnnouncements](DYLIBS/WorkoutAnnouncements.md)
- [/System/Library/PrivateFrameworks/WorkoutCore.framework/WorkoutCore](DYLIBS/WorkoutCore.md)
- [/System/Library/PrivateFrameworks/WorkoutUI.framework/WorkoutUI](DYLIBS/WorkoutUI.md)
- [/System/Library/PrivateFrameworks/WritingTools.framework/WritingTools](DYLIBS/WritingTools.md)
- [/System/Library/PrivateFrameworks/WritingToolsUI.framework/WritingToolsUI](DYLIBS/WritingToolsUI.md)
- [/System/Library/PrivateFrameworks/_JetEngine_SwiftUI.framework/_JetEngine_SwiftUI](DYLIBS/_JetEngine_SwiftUI.md)
- [/System/Library/PrivateFrameworks/_MusicKitInternal_SwiftUI.framework/_MusicKitInternal_SwiftUI](DYLIBS/_MusicKitInternal_SwiftUI.md)
- [/System/Library/PrivateFrameworks/_SonicKit_MusicKit.framework/_SonicKit_MusicKit](DYLIBS/_SonicKit_MusicKit.md)
- [/System/Library/PrivateFrameworks/iCloudMailAccountUI.framework/iCloudMailAccountUI](DYLIBS/iCloudMailAccountUI.md)
- [/System/Library/PrivateFrameworks/iCloudSettings.framework/iCloudSettings](DYLIBS/iCloudSettings.md)
- [/System/Library/PrivateFrameworks/iCloudSubscriptionOptimizerDaemon.framework/iCloudSubscriptionOptimizerDaemon](DYLIBS/iCloudSubscriptionOptimizerDaemon.md)
- [/System/Library/PrivateFrameworks/iTunesCloud.framework/iTunesCloud](DYLIBS/iTunesCloud.md)
- [/System/Library/PrivateFrameworks/iTunesStoreUI.framework/iTunesStoreUI](DYLIBS/iTunesStoreUI.md)
- [/System/Library/PrivateFrameworks/ktrace.framework/ktrace](DYLIBS/ktrace.md)
- [/System/Library/PrivateFrameworks/shared_cache_page_prewarming.framework/shared_cache_page_prewarming](DYLIBS/shared_cache_page_prewarming.md)
- [/System/Library/VideoCodecs/H264SW.videocodec](DYLIBS/H264SW.videocodec.md)
- [/System/Library/VideoDecoders/AppleProResSWDecoder.videodecoder](DYLIBS/AppleProResSWDecoder.videodecoder.md)
- [/System/Library/VideoDecoders/JPEGH1.videodecoder](DYLIBS/JPEGH1.videodecoder.md)
- [/System/Library/VideoEncoders/AppleProResSWEncoder.videoencoder](DYLIBS/AppleProResSWEncoder.videoencoder.md)
- [/System/Library/VideoEncoders/H264H9.videoencoder](DYLIBS/H264H9.videoencoder.md)
- [/System/Library/VideoEncoders/H9.videoencoder](DYLIBS/H9.videoencoder.md)
- [/System/Library/VideoEncoders/JPEGH1.videoencoder](DYLIBS/JPEGH1.videoencoder.md)
- [/System/Library/VideoProcessors/BarcodeScanner.videoprocessor](DYLIBS/BarcodeScanner.videoprocessor.md)
- [/System/Library/VideoProcessors/DepthProcessorV2.bundle/DepthProcessorV2](DYLIBS/DepthProcessorV2.md)
- [/System/Library/VideoProcessors/FPDisparityV3.bundle/FPDisparityV3](DYLIBS/FPDisparityV3.md)
- [/System/Library/VideoProcessors/IntelligentDistortionCorrectionV1.bundle/IntelligentDistortionCorrectionV1](DYLIBS/IntelligentDistortionCorrectionV1.md)
- [/System/Library/VideoProcessors/MattingV2.bundle/MattingV2](DYLIBS/MattingV2.md)
- [/System/Library/VideoProcessors/MetalFilter.bundle/MetalFilter](DYLIBS/MetalFilter.md)
- [/System/Library/VideoProcessors/NRFV4.bundle/NRFV4](DYLIBS/NRFV4.md)
- [/System/Library/VideoProcessors/SDOFRenderingV5.bundle/SDOFRenderingV5](DYLIBS/SDOFRenderingV5.md)
- [/System/Library/VideoProcessors/STF.bundle/STF](DYLIBS/STF.md)
- [/usr/lib/dyld](DYLIBS/dyld.md)
- [/usr/lib/libATCommandStudioDynamic.dylib](DYLIBS/libATCommandStudioDynamic.dylib.md)
- [/usr/lib/libAppletTranslationLibrary.dylib](DYLIBS/libAppletTranslationLibrary.dylib.md)
- [/usr/lib/libBBUpdaterDynamic.dylib](DYLIBS/libBBUpdaterDynamic.dylib.md)
- [/usr/lib/libBKDM2.dylib](DYLIBS/libBKDM2.dylib.md)
- [/usr/lib/libBasebandCommandDrivers.dylib](DYLIBS/libBasebandCommandDrivers.dylib.md)
- [/usr/lib/libBasebandCommandDriversARI.dylib](DYLIBS/libBasebandCommandDriversARI.dylib.md)
- [/usr/lib/libBasebandCommandDriversMIPC.dylib](DYLIBS/libBasebandCommandDriversMIPC.dylib.md)
- [/usr/lib/libBasebandCommandDriversQMI.dylib](DYLIBS/libBasebandCommandDriversQMI.dylib.md)
- [/usr/lib/libBasebandManager.dylib](DYLIBS/libBasebandManager.dylib.md)
- [/usr/lib/libBasebandManagerDAL.dylib](DYLIBS/libBasebandManagerDAL.dylib.md)
- [/usr/lib/libBasebandManagerICE.dylib](DYLIBS/libBasebandManagerICE.dylib.md)
- [/usr/lib/libETLDLFDynamic.dylib](DYLIBS/libETLDLFDynamic.dylib.md)
- [/usr/lib/libETLDLOADCoreDumpDynamic.dylib](DYLIBS/libETLDLOADCoreDumpDynamic.dylib.md)
- [/usr/lib/libETLDLOADDynamic.dylib](DYLIBS/libETLDLOADDynamic.dylib.md)
- [/usr/lib/libETLDMCDynamic.dylib](DYLIBS/libETLDMCDynamic.dylib.md)
- [/usr/lib/libETLDynamic.dylib](DYLIBS/libETLDynamic.dylib.md)
- [/usr/lib/libETLSAHDynamic.dylib](DYLIBS/libETLSAHDynamic.dylib.md)
- [/usr/lib/libLLVM.dylib](DYLIBS/libLLVM.dylib.md)
- [/usr/lib/libMobileGestalt.dylib](DYLIBS/libMobileGestalt.dylib.md)
- [/usr/lib/libQMIParserDynamic.dylib](DYLIBS/libQMIParserDynamic.dylib.md)
- [/usr/lib/libTelephonyBasebandDynamic.dylib](DYLIBS/libTelephonyBasebandDynamic.dylib.md)
- [/usr/lib/libTelephonyCapabilities.dylib](DYLIBS/libTelephonyCapabilities.dylib.md)
- [/usr/lib/libTelephonyDebugDynamic.dylib](DYLIBS/libTelephonyDebugDynamic.dylib.md)
- [/usr/lib/libTelephonyUtilDynamic.dylib](DYLIBS/libTelephonyUtilDynamic.dylib.md)
- [/usr/lib/libVinylNonUpdater.dylib](DYLIBS/libVinylNonUpdater.dylib.md)
- [/usr/lib/libauthinstall.dylib](DYLIBS/libauthinstall.dylib.md)
- [/usr/lib/libhwtrace.dylib](DYLIBS/libhwtrace.dylib.md)
- [/usr/lib/libllvm-lmdb.dylib](DYLIBS/libllvm-lmdb.dylib.md)
- [/usr/lib/libmecabra.dylib](DYLIBS/libmecabra.dylib.md)
- [/usr/lib/libnetwork.dylib](DYLIBS/libnetwork.dylib.md)
- [/usr/lib/libnfshared.dylib](DYLIBS/libnfshared.dylib.md)
- [/usr/lib/libquic.dylib](DYLIBS/libquic.dylib.md)
- [/usr/lib/libswiftPrespecialized.dylib](DYLIBS/libswiftPrespecialized.dylib.md)
- [/usr/lib/libtailspin.dylib](DYLIBS/libtailspin.dylib.md)
- [/usr/lib/libusrtcp.dylib](DYLIBS/libusrtcp.dylib.md)
- [/usr/lib/libxml2.2.dylib](DYLIBS/libxml2.2.dylib.md)
- [/usr/lib/log/liblog_network.dylib](DYLIBS/liblog_network.dylib.md)
- [/usr/lib/swift/libswiftAVFoundation.dylib](DYLIBS/libswiftAVFoundation.dylib.md)
- [/usr/lib/swift/libswiftAccelerate.dylib](DYLIBS/libswiftAccelerate.dylib.md)
- [/usr/lib/swift/libswiftDarwin.dylib](DYLIBS/libswiftDarwin.dylib.md)
- [/usr/lib/swift/libswiftDistributed.dylib](DYLIBS/libswiftDistributed.dylib.md)
- [/usr/lib/swift/libswiftNetwork.dylib](DYLIBS/libswiftNetwork.dylib.md)
- [/usr/lib/swift/libswiftSpatial.dylib](DYLIBS/libswiftSpatial.dylib.md)
- [/usr/lib/swift/libswiftSynchronization.dylib](DYLIBS/libswiftSynchronization.dylib.md)
- [/usr/lib/swift/libswiftXPC.dylib](DYLIBS/libswiftXPC.dylib.md)
- [/usr/lib/swift/libswift_errno.dylib](DYLIBS/libswift_errno.dylib.md)
- [/usr/lib/swift/libswift_math.dylib](DYLIBS/libswift_math.dylib.md)
- [/usr/lib/swift/libswift_stdio.dylib](DYLIBS/libswift_stdio.dylib.md)
- [/usr/lib/swift/libswift_time.dylib](DYLIBS/libswift_time.dylib.md)
- [/usr/lib/swift/libswiftunistd.dylib](DYLIBS/libswiftunistd.dylib.md)
- [/usr/lib/system/libdyld.dylib](DYLIBS/libdyld.dylib.md)
- [/usr/lib/system/libsystem_c.dylib](DYLIBS/libsystem_c.dylib.md)
- [/usr/lib/system/libsystem_darwin.dylib](DYLIBS/libsystem_darwin.dylib.md)
- [/usr/lib/system/libsystem_eligibility.dylib](DYLIBS/libsystem_eligibility.dylib.md)
- [/usr/lib/system/libsystem_malloc.dylib](DYLIBS/libsystem_malloc.dylib.md)
- [/usr/lib/system/libsystem_sandbox.dylib](DYLIBS/libsystem_sandbox.dylib.md)
- [/usr/lib/updaters/libVinylUpdater.dylib](DYLIBS/libVinylUpdater.dylib.md)

</details>

### Feature Flags

#### ⬆️ Updated (8)

<details>
  <summary><i>View Updated</i></summary>

#### AppleMediaServices.plist

>  `Domain/AppleMediaServices.plist`

```diff

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
+	<key>TSDataSyncMetrics</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>UseMobileGestaltProductType</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### ConversationKit.plist

>  `Domain/ConversationKit.plist`

```diff

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
+	<key>ShowTranscriptWithoutConfidenceFiltering</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>TouchBar</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### DigitalSeparation.plist

>  `Domain/DigitalSeparation.plist`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>SCSharingTypeWiFiSync</key>
-	<dict>
-		<key>DevelopmentPhase</key>
-		<string>FeatureComplete</string>
-	</dict>
 	<key>errorMessaging</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### Finance.plist

>  `Domain/Finance.plist`

```diff

 	</dict>
 	<key>BackgroundRefreshReminders</key>
 	<dict>
-		<key>Enabled</key>
-		<true/>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
 	</dict>
 	<key>CredentialSync</key>
 	<dict>

```

#### FindMy.plist

>  `Domain/FindMy.plist`

```diff

 		<key>Enabled</key>
 		<true/>
 	</dict>
+	<key>ArcticPlum</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>BA_AirPods</key>
 	<dict>
 		<key>Enabled</key>

```

#### IntelligenceFlow.plist

>  `Domain/IntelligenceFlow.plist`

```diff

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
-	<key>SearchSupport</key>
-	<dict>
-		<key>DevelopmentPhase</key>
-		<string>FeatureComplete</string>
-	</dict>
 </dict>
 </plist>
 

```

#### Shortcuts.plist

>  `Domain/Shortcuts.plist`

```diff

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
-	<key>zoom_transition</key>
-	<dict>
-		<key>DevelopmentPhase</key>
-		<string>FeatureComplete</string>
-	</dict>
 </dict>
 </plist>
 

```

#### Spotlight.plist

>  `Domain/Spotlight.plist`

```diff

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
-	<key>SpotlightKnowledgePreExtraction</key>
-	<dict>
-		<key>DevelopmentPhase</key>
-		<string>FeatureComplete</string>
-	</dict>
 	<key>SpotlightMatchingArrayIndexes</key>
 	<dict>
 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
-	<key>SpotlightPIRLocationLookup</key>
-	<dict>
-		<key>DevelopmentPhase</key>
-		<string>FeatureComplete</string>
-	</dict>
 	<key>SuggestionsQuality2024</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```


</details>

## EOF
