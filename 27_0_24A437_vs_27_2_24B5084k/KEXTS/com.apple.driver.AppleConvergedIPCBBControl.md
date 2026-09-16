## com.apple.driver.AppleConvergedIPCBBControl

> `com.apple.driver.AppleConvergedIPCBBControl`

```diff

 430.0.0.0.0
-  __TEXT.__cstring: 0x462f
-  __TEXT.__const: 0xc12e
-  __TEXT_EXEC.__text: 0x65e10
-  __TEXT_EXEC.__auth_stubs: 0xfc0
-  __DATA.__data: 0x348
-  __DATA.__common: 0x778
-  __DATA_CONST.__mod_init_func: 0x1420
-  __DATA_CONST.__mod_term_func: 0x160
-  __DATA_CONST.__const: 0x1e7b0
-  __DATA_CONST.__weak_got: 0x1130
-  __DATA_CONST.__kalloc_type: 0x1cc0
-  __DATA_CONST.__kalloc_var: 0x870
-  __DATA_CONST.__auth_got: 0x7e0
-  __DATA_CONST.__got: 0x228
-  Functions: 2976
+  __TEXT.__cstring: 0x545d
+  __TEXT.__const: 0x19eee
+  __TEXT_EXEC.__text: 0x9d450
+  __TEXT_EXEC.__auth_stubs: 0x1170
+  __DATA.__data: 0x3f8
+  __DATA.__common: 0x7f0
+  __DATA_CONST.__mod_init_func: 0x2ab0
+  __DATA_CONST.__mod_term_func: 0x1d0
+  __DATA_CONST.__const: 0x2f3c8
+  __DATA_CONST.__weak_got: 0x25e0
+  __DATA_CONST.__kalloc_type: 0x1e00
+  __DATA_CONST.__kalloc_var: 0x9b0
+  __DATA_CONST.__auth_got: 0x8b8
+  __DATA_CONST.__got: 0x250
+  Functions: 4025
   Symbols:   0
-  CStrings:  553
+  CStrings:  664
 
CStrings:
+ "%06ld.%06d "
+ "%3u"
+ "%3u to %3u"
+ "%3u to inf"
+ "%s::%s: %s to enable refclk gating\n"
+ "%s::%s: *%p == 0x%x\n"
+ "%s::%s: HMAP VSEC regs(@0x%x)= 0x%x\n"
+ "%s::%s: HMAP capability not found\n"
+ "%s::%s: Invalid bar Index for MSI-X: %u! skipping HMAP config for MSI-X\n"
+ "%s::%s: Invalid index %d"
+ "%s::%s: Link control reg: 0x%x, Link control offset: 0x%llx\n"
+ "%s::%s: MSI address 0x%llx\n"
+ "%s::%s: MSI or MSI-X capability not found!\n"
+ "%s::%s: MSI-X bar Index: 0x%x\n"
+ "%s::%s: MSI-X capability found\n"
+ "%s::%s: MSI-X vector 0 address 0x%llx\n"
+ "%s::%s: PCIe getLinkSpeed failed. Supported RP speed %u, Supported EP speed %u, Desired speed %u, Enumerated speed %u\n"
+ "%s::%s: PCIe link speed mismatched. Supported RP speed %u, Supported EP sped %u, Desired speed %u, Enumerated speed %u\n"
+ "%s::%s: VSEC ID at offset 0x%llx matched HMAP 0x%x\n"
+ "%s::%s: VSEC ID at offset 0x%llx not matched HMAP. Expected 0x0024, found 0x%x\n"
+ "%s::%s: bar%u %p [+0x%x], (pa: 0x%llx)\n"
+ "%s::%s: bar0 %p [+0x%x], bar1 %p [+0x%x]\n"
+ "%s::%s: chip revision major (%u)\n"
+ "%s::%s: configured HMAP for MSI\n"
+ "%s::%s: dart window range: %p --> %p\n"
+ "%s::%s: endpoint pcie capability not found\n"
+ "%s::%s: endpoint port PCIe capability not found\n"
+ "%s::%s: failed to create/init a reporter\n"
+ "%s::%s: failed to get PCIe link speed %u\n"
+ "%s::%s: failed to get provider of IOPCI2PCIBridge\n"
+ "%s::%s: failed to get provider of IOPCIDevice\n"
+ "%s::%s: failed to map bar0\n"
+ "%s::%s: failed to map bar1\n"
+ "%s::%s: failed to map msi-X bar! skipping HMAP config for MSI-X!\n"
+ "%s::%s: failed to start reporting\n"
+ "%s::%s: root port PCIe capability not found\n"
+ "+-----------------------------------------------+----------------+"
+ "112111111"
+ "121111121222121211111112111211211111111111111111211211211211112111121"
+ "12111112122212121111111211121121111111111111111121121121121111211112112221111112222211112"
+ "1211111212221212111111121112112111111111111111112112112112111121111212"
+ "121111121222121211111211122222221111221211121"
+ "121111121222121211122111111111111122222222222222222221121111122112221111111111111111111111111111111122222222111222222222222222222222122222222222222222222"
+ "121111121222121211122121111122222222211112111"
+ "12111112122212121121111111111111112222211111111112212111112121"
+ "121111121222121211211111111111111122222111111111122121111121212211121"
+ "1211111212221212121121211112111111111111111111111111111111111111111111111111111111111111111111112222222222222222222222121"
+ "12111112122212121211212111121111111111111111111111111111111111111111111111111111111111111111111122222222222222222222221212"
+ "1211111212221212121122222222211111112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221222212222122221222212222122221222212222122221222212222122221222212222122221222212222122221222212222122221222212222122221222212222122221222212222122221222212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222122211212"
+ "12112111"
+ "1211222111111111111"
+ "Aggregated Block"
+ "AppleBasebandPCILogger::start: failed to allocate memory for snapshot buffer\n"
+ "AppleConvergedIPCBBLogger"
+ "AppleConvergedIPCBBLogger.cpp"
+ "AppleConvergedIPCPDPReporter"
+ "AppleConvergedIPCPDPReporter.cpp"
+ "AppleConvergedPCIBBRASReporter"
+ "AppleConvergedPCIBBRASReporter.cpp"
+ "Counters"
+ "DL"
+ "DL Aggregation Histogram"
+ "DL Drop Counters"
+ "Downlink Bytes"
+ "Downlink Pkts"
+ "Dropped Downlink Bytes"
+ "Dropped Downlink Packets"
+ "Flow Control"
+ "Global"
+ "Invalid Interface"
+ "Link Status Notifications"
+ "PDP"
+ "PDP packet dump level"
+ "PDP packet dump new level: %u\n"
+ "PDP packet dump size"
+ "Publish Count"
+ "RAS Event Capability"
+ "States"
+ "Terminate Count"
+ "UL"
+ "UL Aggregation Histogram"
+ "Uplink Bytes"
+ "Uplink Pkts"
+ "abp-debug-buf-size"
+ "abp-uart-debug"
+ "acipc-pdp-reporting"
+ "currentLogSnapshotBufferSize"
+ "disabled"
+ "down"
+ "enableHostMemProtectionGated"
+ "enabled"
+ "failed"
+ "getLinkSpeed_block_invoke"
+ "isLinkSpeedChangedGated"
+ "logSnapshotBufferSize"
+ "mapBarGated"
+ "pdp:%s: error %d\n"
+ "pdp:%s: size (%u) out of range.\n"
+ "pdp_dump_level"
+ "pdp_dump_size"
+ "publish"
+ "readBar"
+ "readEndpointASPM"
+ "running"
+ "setPowerStateGated"
+ "site.AppleConvergedIPCBBLogger"
+ "site.AppleConvergedIPCPDPReporter"
+ "site.AppleConvergedPCIBBRASReporter"
+ "site.IOSimpleReporter*"
+ "site.IOStateReporter*"
+ "site.logBuffer"
+ "some logs dropped\n"
+ "stopped"
+ "succeeded"
+ "sysctl_pdp_dump_level"
+ "sysctl_pdp_dump_size"
+ "terminate"
+ "up"
+ "v16@?0r*8"
+ "writeBar"
+ "|%02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x|%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c|"
- "12111112122212121111111211121121111111111111111211211211211112111121"
- "1211111212221212111111121112112111111111111111121121121121111211112112221111112222211112"
- "121111121222121211111112111211211111111111111112112112112111121111212"
- "12111112122212121111121112222222111122121112"
- "12111112122212121112211111111111122222222222222222221121111122112221111111111111111111111111111111122222222111222222222222222222222122222222222222222222"
- "12111112122212121112212111122222222211112111"
- "1211111212221212112111111111111111222221111111112212111112121"
- "12111112122212121121111111111111112222211111111122121111121212211121"
- "121111121222121212112121111211111111111111111111111111111111111111111111111111111111111111111111222222222222222222222221"
- "1211111212221212121121211112111111111111111111111111111111111111111111111111111111111111111111112222222222222222222222212"
```
