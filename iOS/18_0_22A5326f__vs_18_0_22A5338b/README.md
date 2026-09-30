# 18.0 (22A5326f) .vs 18.0 (22A5338b)

## IPSWs

- `iPhone16,2_18.0_22A5326f_Restore.ipsw`
- `iPhone16,2_18.0_22A5338b_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 18.0 *(22A5326f)* | 24.0.0 | 11215.0.199.502.1~1 | Tue, 30Jul2024 20:45:41 PDT |
| 18.0 *(22A5338b)* | 24.0.0 | 11215.2.5~59 | Thu, 08Aug2024 01:20:03 PDT |

### Kexts

#### ⬆️ Updated (16)

<details>
  <summary><i>View Updated</i></summary>

>  `com.apple.driver.AppleDisplayCrossbar`

```diff

-355.0.2.0.0
+355.0.3.0.0
   __TEXT.__cstring: 0x4413
   __TEXT.__const: 0x160
   __TEXT.__os_log: 0x5d14
-  __TEXT_EXEC.__text: 0x3214c
+  __TEXT_EXEC.__text: 0x32128
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x3d0

   __DATA_CONST.__got: 0xd0
   __DATA_CONST.__mod_init_func: 0xc0
   __DATA_CONST.__mod_term_func: 0xc0
-  __DATA_CONST.__const: 0xd1f8
+  __DATA_CONST.__const: 0xd1e0
   __DATA_CONST.__kalloc_type: 0x600
-  Functions: 1477
+  Functions: 1474
   Symbols:   0
   CStrings:  707
 

```

>  `com.apple.driver.AppleMobileDispH16P-DCP`

```diff

-395.30.0.0.0
-  __TEXT.__cstring: 0x5658
+395.33.3.0.0
+  __TEXT.__cstring: 0x56a0
   __TEXT.__const: 0x1a78
-  __TEXT_EXEC.__text: 0x20970
+  __TEXT_EXEC.__text: 0x20b6c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2b8
   __DATA.__common: 0xf0
   __DATA.__bss: 0x170
   __DATA_CONST.__auth_got: 0x708
-  __DATA_CONST.__got: 0xe0
+  __DATA_CONST.__got: 0xe8
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
-  __DATA_CONST.__const: 0x3e40
+  __DATA_CONST.__const: 0x3e88
   __DATA_CONST.__kalloc_type: 0x640
   __DATA_CONST.__kalloc_var: 0xf0
-  Functions: 1109
+  Functions: 1111
   Symbols:   0
-  CStrings:  510
+  CStrings:  512
 
CStrings:
+ "IOMFBWindowedVsyncOffDisableDetachingKey"
+ "iomfb_swap_submit_split_enable"

```

>  `com.apple.driver.AppleMobileFileIntegrity`

```diff

-938.0.27.0.1
+938.0.31.0.0
   __TEXT.__cstring: 0x9aae
   __TEXT.__const: 0x14b0
   __TEXT.__os_log: 0x233
-  __TEXT_EXEC.__text: 0x25fec
+  __TEXT_EXEC.__text: 0x25fd4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x412
   __DATA.__common: 0xb0
CStrings:
+ "01:10:33"
+ "Aug  8 2024"
- "20:35:18"
- "Jul 30 2024"

```

>  `com.apple.iokit.IOMobileGraphicsFamily-DCP`

```diff

-395.30.0.0.0
+395.33.3.0.0
   __TEXT.__cstring: 0x3ef5
-  __TEXT.__const: 0x2148
-  __TEXT_EXEC.__text: 0x1f8fc
+  __TEXT.__const: 0x2f68
+  __TEXT_EXEC.__text: 0x1fe34
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xe0
   __DATA.__common: 0x26d0

   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x20
   __DATA_CONST.__mod_term_func: 0x20
-  __DATA_CONST.__const: 0x1628
+  __DATA_CONST.__const: 0x1638
   __DATA_CONST.__kalloc_type: 0x7c0
-  Functions: 690
+  Functions: 692
   Symbols:   0
   CStrings:  364
 
CStrings:
+ "site.A439_out_args__"
+ "site.A440_in_args__"
- "site.A436_in_args__"
- "site.A437_out_args__"

```

>  `com.apple.driver.AppleBasebandPCI`

```diff

 810.0.0.0.0
-  __TEXT.__cstring: 0xc286
-  __TEXT.__const: 0x5009
-  __TEXT_EXEC.__text: 0x88dd0
+  __TEXT.__cstring: 0x3809
+  __TEXT.__const: 0x4f69
+  __TEXT_EXEC.__text: 0x48aec
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x3f8
-  __DATA.__common: 0x648
-  __DATA.__bss: 0x3048
-  __DATA_CONST.__auth_got: 0x620
-  __DATA_CONST.__got: 0x180
+  __DATA.__data: 0x33c
+  __DATA.__common: 0x5a0
+  __DATA.__bss: 0x2e50
+  __DATA_CONST.__auth_got: 0x560
+  __DATA_CONST.__got: 0x178
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__mod_init_func: 0x1350
-  __DATA_CONST.__mod_term_func: 0xf0
-  __DATA_CONST.__const: 0xfeb8
-  __DATA_CONST.__kalloc_type: 0x1d80
-  __DATA_CONST.__kalloc_var: 0x690
-  Functions: 2403
+  __DATA_CONST.__mod_init_func: 0x12f0
+  __DATA_CONST.__mod_term_func: 0xd0
+  __DATA_CONST.__const: 0xf108
+  __DATA_CONST.__kalloc_type: 0x1980
+  __DATA_CONST.__kalloc_var: 0x550
+  Functions: 2229
   Symbols:   0
-  CStrings:  1371
+  CStrings:  446
 
CStrings:
+ "121111121222121211111111211111211111111111112112112112111121121111121"
+ "1211111212221212111111112111112111111111111121121121121111211211111212"
+ "12111112122212121111211122222221211111222221212"
+ "12111112122212121211111111111111111111112212212222111111111222"
+ "1211111212221212121211111111111111111111122222222222222222222222222222222222111111111111111111111111111111111111111111111111111111111111111111111122222222222222222111112112222222"
- "\t%06ld.%06d %s %llx\n"
- "%02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x"
- "%06ld.%06d %s::%s: \n"
- "%06ld.%06d %s::%s:  --done\n"
- "%06ld.%06d %s::%s:  MSI owner cannot be NULL\n"
- "%06ld.%06d %s::%s:  MSI owner or handler cannot be NULL\n"
- "%06ld.%06d %s::%s:  PDP manager registration with IP Appender failed\n"
- "%06ld.%06d %s::%s:  Type= %s\n HwClass= %s\n HwError= %s\n IsWrite= %s\n HwStatus= %#llX\n SID= %#llx\n Address= %#llx\n"
- "%06ld.%06d %s::%s:  qctun interface tx slot count: %u\n"
- "%06ld.%06d %s::%s: \"%s\" not found in plist\n"
- "%06ld.%06d %s::%s: %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x\n"
- "%06ld.%06d %s::%s: %d\n"
- "%06ld.%06d %s::%s: %s\n"
- "%06ld.%06d %s::%s: %s -> %s\n"
- "%06ld.%06d %s::%s: %s TCP packet: len %u, seq %u, ack %u\n"
- "%06ld.%06d %s::%s: %s override\n"
- "%06ld.%06d %s::%s: %s rx slot count %u\n"
- "%06ld.%06d %s::%s: %s tx slot count %u\n"
- "%06ld.%06d %s::%s: %s%02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x\n"
- "%06ld.%06d %s::%s: %s%s\n"
- "%06ld.%06d %s::%s: %s: --> \n"
- "%06ld.%06d %s::%s: %u\n"
- "%06ld.%06d %s::%s: (async) failed client is not attached\n"
- "%06ld.%06d %s::%s: (async) failed to create memory decriptor\n"
- "%06ld.%06d %s::%s: (async) failed to prepare image command\n"
- "%06ld.%06d %s::%s: (async) failed to prepare memory command\n"
- "%06ld.%06d %s::%s: (async) returned 0x%x\n"
- "%06ld.%06d %s::%s: (sync < 4K) failed client is not attached\n"
- "%06ld.%06d %s::%s: (sync < 4K) failed to create memory decriptor\n"
- "%06ld.%06d %s::%s: (sync < 4K) failed to prepare image command\n"
- "%06ld.%06d %s::%s: (sync < 4K) failed to prepare memory command\n"
- "%06ld.%06d %s::%s: (sync < 4K) returned 0x%x\n"
- "%06ld.%06d %s::%s: (sync > 4K) failed client is not attached\n"
- "%06ld.%06d %s::%s: (sync > 4K) failed to prepare image command\n"
- "%06ld.%06d %s::%s: (sync > 4K) failed to prepare memory command\n"
- "%06ld.%06d %s::%s: (sync > 4K) no memory decriptor\n"
- "%06ld.%06d %s::%s: (sync > 4K) returned 0x%x\n"
- "%06ld.%06d %s::%s: +\n"
- "%06ld.%06d %s::%s: -\n"
- "%06ld.%06d %s::%s: -- done\n"
- "%06ld.%06d %s::%s: -- done %u\n"
- "%06ld.%06d %s::%s: --done\n"
- "%06ld.%06d %s::%s: AER was already registered\n"
- "%06ld.%06d %s::%s: ASPML1 disabled on endpoint\n"
- "%06ld.%06d %s::%s: ASPML1 disabled on root port\n"
- "%06ld.%06d %s::%s: AppleBasebandPCI workloop onThread %u, inGate %u\n"
- "%06ld.%06d %s::%s: AppleBasebandPCIControl workloop onThread %u, inGate %u\n"
- "%06ld.%06d %s::%s: Base Rx slot count not found in plist\n"
- "%06ld.%06d %s::%s: Base Tx slot count not found in plist\n"
- "%06ld.%06d %s::%s: Bearer switch trigger failed, ret: 0x%08x\n"
- "%06ld.%06d %s::%s: Bearer switch unsupported for this serviceID: %u\n"
- "%06ld.%06d %s::%s: Client lacks entitlement\n"
- "%06ld.%06d %s::%s: Closing pci service: %p\n"
- "%06ld.%06d %s::%s: Could not open PCI service\n"
- "%06ld.%06d %s::%s: Created qctun interface, pService: %p\n"
- "%06ld.%06d %s::%s: Creating QueueSet failed, index: %u\n"
- "%06ld.%06d %s::%s: Creating logical link failed\n"
- "%06ld.%06d %s::%s: Creating qctun interface\n"
- "%06ld.%06d %s::%s: Creating queue sets for logical link failed\n"
- "%06ld.%06d %s::%s: DART error handler registeration failed!, ret: 0x%08x\n"
- "%06ld.%06d %s::%s: DART window: 0x%llx --> 0x%llx\n"
- "%06ld.%06d %s::%s: DL limit set to %u\n"
- "%06ld.%06d %s::%s: De-Allocate pkts directly to pool, dir: %lu\n"
- "%06ld.%06d %s::%s: Default pci service not published! enabled: %u, shouldEnable: %u\n"
- "%06ld.%06d %s::%s: Default soft flow control thresholds: on %u, off %u\n"
- "%06ld.%06d %s::%s: Device Status/Control register: 0x%lx, isPending: %u\n"
- "%06ld.%06d %s::%s: DeviceCtl 0x%08x DeviceStatus 0x%08x LinkStatus 0x%08x\n"
- "%06ld.%06d %s::%s: Enqueue failed, dir: %u, ret: 0x%08x\n"
- "%06ld.%06d %s::%s: Failed to allocate memory for interface advisory report\n"
- "%06ld.%06d %s::%s: Failed to calculate qctun buffer pool capacity!\n"
- "%06ld.%06d %s::%s: Failed to create Create Dedicated Queue Set\n"
- "%06ld.%06d %s::%s: Failed to create Create Default Queue Set\n"
- "%06ld.%06d %s::%s: Failed to create logical link!\n"
- "%06ld.%06d %s::%s: Failed to create/attach interface, 0x%x\n"
- "%06ld.%06d %s::%s: Failed to get Transaction Pending bit, ret: 0x%llx\n"
- "%06ld.%06d %s::%s: Failed to get device reset state!\n"
- "%06ld.%06d %s::%s: Failed to read AER Capability Structure\n"
- "%06ld.%06d %s::%s: Failed to read PCIe Express Capability Structure\n"
- "%06ld.%06d %s::%s: Flow control service not active\n"
- "%06ld.%06d %s::%s: Getting BB reset state failed\n"
- "%06ld.%06d %s::%s: HMAP VSEC regs(@0x%x)= 0x%x\n"
- "%06ld.%06d %s::%s: HMAP capability not found\n"
- "%06ld.%06d %s::%s: HeaderLog 0 to 3 0x%08x 0x%08x 0x%x 0x%08x\n"
- "%06ld.%06d %s::%s: IOMemoryDescriptor %p\n"
- "%06ld.%06d %s::%s: IOMemoryDescriptor %p, info 0x%llx\n"
- "%06ld.%06d %s::%s: IOSkywalkFamily querying free space, interface: %u, returning: %u\n"
- "%06ld.%06d %s::%s: IPAppender message, message: 0x%u\n"
- "%06ld.%06d %s::%s: Init failed, intf: %p, manager: %p\n"
- "%06ld.%06d %s::%s: Interface non-existent interface ID: %u\n"
- "%06ld.%06d %s::%s: Interface: %u, Rx pkt compl cnt: %lu\n"
- "%06ld.%06d %s::%s: Interface: %u, Tx pkt compl cnt: %lu\n"
- "%06ld.%06d %s::%s: Invalid POSTROM link speed setting, will use defaults\n"
- "%06ld.%06d %s::%s: Invalid ROM link speed setting, will use defaults\n"
- "%06ld.%06d %s::%s: Invalid bearer ID\n"
- "%06ld.%06d %s::%s: Invalid data service: %u\n"
- "%06ld.%06d %s::%s: Invalid direction, dir: %u\n"
- "%06ld.%06d %s::%s: Invalid direction, direction: %u\n"
- "%06ld.%06d %s::%s: Invalid filter rule, descriptor type: \n"
- "%06ld.%06d %s::%s: Invalid interface ID: %u\n"
- "%06ld.%06d %s::%s: Invalid payload length, expected: %u, received: %u\n"
- "%06ld.%06d %s::%s: Invalid service ID: %u\n"
- "%06ld.%06d %s::%s: L1SS control 1 reg: 0x%x\n"
- "%06ld.%06d %s::%s: L1SS control 2 reg: 0x%x\n"
- "%06ld.%06d %s::%s: Logical link NOT supported!\n"
- "%06ld.%06d %s::%s: Low Latency data NOT supported!\n"
- "%06ld.%06d %s::%s: MSI address 0x%x\n"
- "%06ld.%06d %s::%s: MSI capability not found\n"
- "%06ld.%06d %s::%s: MSI registration failed with pci service, ret: 0x%08x\n"
- "%06ld.%06d %s::%s: MSI registration for index %u already exists!\n"
- "%06ld.%06d %s::%s: Mapped bearer ID: %u, queueSetID: 0x%llx\n"
- "%06ld.%06d %s::%s: NOT EOT, bail! status 0x%x, size %u, eot %d\n"
- "%06ld.%06d %s::%s: NULL input argument(s)\n"
- "%06ld.%06d %s::%s: NULL logical link\n"
- "%06ld.%06d %s::%s: NULL message argument\n"
- "%06ld.%06d %s::%s: NULL output arguments\n"
- "%06ld.%06d %s::%s: NULL payload\n"
- "%06ld.%06d %s::%s: NULL traffic descriptor\n"
- "%06ld.%06d %s::%s: Network stack rejected link status report: 0x%x\n"
- "%06ld.%06d %s::%s: Not a valid PCI service\n"
- "%06ld.%06d %s::%s: Not in low power, bailing!\n"
- "%06ld.%06d %s::%s: Not supported for non logical link interfaces\n"
- "%06ld.%06d %s::%s: Opened successfully! _pciService: %p\n"
- "%06ld.%06d %s::%s: Opening PCI data service failed, ret: 0x%08x\n"
- "%06ld.%06d %s::%s: Opening _pciService: %p\n"
- "%06ld.%06d %s::%s: Opening pci service: %p\n"
- "%06ld.%06d %s::%s: PCI notification\n"
- "%06ld.%06d %s::%s: PCI service to switch not active, service ID: %u\n"
- "%06ld.%06d %s::%s: PCIE capability not found\n"
- "%06ld.%06d %s::%s: PCIe link is down or is going down\n"
- "%06ld.%06d %s::%s: PDP event oob allocation, check for potential flaw\n"
- "%06ld.%06d %s::%s: PDP manager service not active\n"
- "%06ld.%06d %s::%s: PDP manager stopped\n"
- "%06ld.%06d %s::%s: POSTROM link speed overridden to: %u\n"
- "%06ld.%06d %s::%s: Packet dump\n"
- "%06ld.%06d %s::%s: Queue Set ID: %u\n"
- "%06ld.%06d %s::%s: ROM link speed overridden to: %u\n"
- "%06ld.%06d %s::%s: Read config space link speed: %u\n"
- "%06ld.%06d %s::%s: Received AER, Config Reg Space Dump : UnCorErrStat 0x%08x CorrErrStat 0x%08x AERCapCtl 0x%08x\n"
- "%06ld.%06d %s::%s: Removed region ID: %u from list\n"
- "%06ld.%06d %s::%s: Reporting interface advisory failed, ret: 0x%08x %u\n"
- "%06ld.%06d %s::%s: Returning packet: %p\n"
- "%06ld.%06d %s::%s: Rx SubQ finalize failed, ret: 0x%llx\n"
- "%06ld.%06d %s::%s: Rx dequeue request\n"
- "%06ld.%06d %s::%s: Rx pkt -  Sub cnt: %u, Compl cnt: %lu\n"
- "%06ld.%06d %s::%s: Rx pkt compl cnt: %lu\n"
- "%06ld.%06d %s::%s: Rx subQ not enabled\n"
- "%06ld.%06d %s::%s: Rx, default queueset: %u\n"
- "%06ld.%06d %s::%s: Setting link control2 to: 0x%08x, new target link speed: %u\n"
- "%06ld.%06d %s::%s: Skip creating qctun intf, qctun_enabled: %u\n"
- "%06ld.%06d %s::%s: Skip dedicated bearer switch for IMS\n"
- "%06ld.%06d %s::%s: Skip queue set disable for IMS\n"
- "%06ld.%06d %s::%s: Skip service id: %u, not a data pci service\n"
- "%06ld.%06d %s::%s: Soft flow control off: %u\n"
- "%06ld.%06d %s::%s: Soft flow control on: %u\n"
- "%06ld.%06d %s::%s: TBD: HMAP MSI-X support\n"
- "%06ld.%06d %s::%s: Timout waiting for bridge to power off! Continuing with potentially unsafe port disable.\n"
- "%06ld.%06d %s::%s: Transaction Pending bit cleared (count: %u)\n"
- "%06ld.%06d %s::%s: Transaction Pending bit poll timed out\n"
- "%06ld.%06d %s::%s: Trigger MSI failed - No event source\n"
- "%06ld.%06d %s::%s: Tx pkt -  Sub cnt: %u, Compl cnt: %lu\n"
- "%06ld.%06d %s::%s: Tx pkt compl cnt: %lu\n"
- "%06ld.%06d %s::%s: Tx subQ not enabled\n"
- "%06ld.%06d %s::%s: Tx, default queueset: %u\n"
- "%06ld.%06d %s::%s: Unable to find the mapped queue set, bearer ID: %u, isDefaultBearer: %u !\n"
- "%06ld.%06d %s::%s: Unable to map to queue set! bearer ID: %u, isDefaultBearer: %u\n"
- "%06ld.%06d %s::%s: Unmapping bearer ID: %u from queue set failed\n"
- "%06ld.%06d %s::%s: Unsupported direction: %u"
- "%06ld.%06d %s::%s: Unsupported direction: %u\n"
- "%06ld.%06d %s::%s: Unsupported notification type: %u\n"
- "%06ld.%06d %s::%s: VSEC ID at offset 0x%x matched HMAP 0x%x\n"
- "%06ld.%06d %s::%s: VSEC ID at offset 0x%x not matched HMAP. Expected 0x0024, found 0x%x\n"
- "%06ld.%06d %s::%s: _asyncMode 0x%08x, asyncMode 0x%08x, arg1 %p\n"
- "%06ld.%06d %s::%s: _enabled: %u\n"
- "%06ld.%06d %s::%s: _inLowPower %u\n"
- "%06ld.%06d %s::%s: _mapper %p\n"
- "%06ld.%06d %s::%s: _mediaInterfaceCount = %u\n"
- "%06ld.%06d %s::%s: _mediaInterfaceMaxPendingWriteBytes = %u\n"
- "%06ld.%06d %s::%s: _mediaInterfaceStart = %u\n"
- "%06ld.%06d %s::%s: _memoryAlloc %u\n"
- "%06ld.%06d %s::%s: _pciService: %p\n"
- "%06ld.%06d %s::%s: _pendLockPort %u\n"
- "%06ld.%06d %s::%s: _pendPortEnable %u\n"
- "%06ld.%06d %s::%s: _vmForce: 0x%llx\n"
- "%06ld.%06d %s::%s: _wiredCount: %u\n"
- "%06ld.%06d %s::%s: _workLoopControl was not set yet\n"
- "%06ld.%06d %s::%s: action %s\n"
- "%06ld.%06d %s::%s: async call failed with 0x%08x\n"
- "%06ld.%06d %s::%s: asyncMode 0x%08x\n"
- "%06ld.%06d %s::%s: attempts %d\n"
- "%06ld.%06d %s::%s: bad refCon %p, _pciPublishNotifier %p, _pciTerminateNotifier %p\n"
- "%06ld.%06d %s::%s: bar0 %p\n"
- "%06ld.%06d %s::%s: baseband chipset unknown, using default\n"
- "%06ld.%06d %s::%s: baseband service is %s\n"
- "%06ld.%06d %s::%s: bearer ID : %u, switched to default data service!\n"
- "%06ld.%06d %s::%s: bearer ID : %u, switched to low latency data service!\n"
- "%06ld.%06d %s::%s: bearer ID: %u, enable: %u, serviceID: %u\n"
- "%06ld.%06d %s::%s: bearerID: %u, interfaceID: %u, enable: %u, ipAppenderSvc: %u\n"
- "%06ld.%06d %s::%s: blockForCommand %u\n"
- "%06ld.%06d %s::%s: bootStage %u\n"
- "%06ld.%06d %s::%s: buff %p, size %u\n"
- "%06ld.%06d %s::%s: buff %p, size %u, info 0x%llx\n"
- "%06ld.%06d %s::%s: buff 0x%llx, size %llu, completion %p\n"
- "%06ld.%06d %s::%s: buff 0x%llx, size %llu, flush %d, completion %p\n"
- "%06ld.%06d %s::%s: buff 0x%llx, size %u, completion %p\n"
- "%06ld.%06d %s::%s: buffer allocation of %uB failed\n"
- "%06ld.%06d %s::%s: calling _provider->close()\n"
- "%06ld.%06d %s::%s: can't allocate map\n"
- "%06ld.%06d %s::%s: cf %p, arg0 %p, arg1 %p\n"
- "%06ld.%06d %s::%s: cf %p, intervalUs %llu, arg0 %p, arg1 %p\n"
- "%06ld.%06d %s::%s: checking link speed, expect %u\n"
- "%06ld.%06d %s::%s: cmdSize %llu\n"
- "%06ld.%06d %s::%s: cmdSize %llu, policyInfo %p\n"
- "%06ld.%06d %s::%s: command %p\n"
- "%06ld.%06d %s::%s: command packets exhausted\n"
- "%06ld.%06d %s::%s: command: %p\n"
- "%06ld.%06d %s::%s: count (%u) > gaurantee (%u) + speculative (%u) counts\n "
- "%06ld.%06d %s::%s: count: %u\n"
- "%06ld.%06d %s::%s: count: %u, dequeued: %u\n"
- "%06ld.%06d %s::%s: creating dedicated queue set, index: %u\n"
- "%06ld.%06d %s::%s: creating default queue set, index: %u\n"
- "%06ld.%06d %s::%s: current asyncMode 0x%08x\n"
- "%06ld.%06d %s::%s: current state: %s\n"
- "%06ld.%06d %s::%s: dealloc packet %p directly\n"
- "%06ld.%06d %s::%s: dedicated queue set [ %u ]: %u\n"
- "%06ld.%06d %s::%s: default queue set [ %u ]: %u\n"
- "%06ld.%06d %s::%s: default queue set config is NULL!\n"
- "%06ld.%06d %s::%s: device %p, powerStateOrdinal %lu\n"
- "%06ld.%06d %s::%s: device %p, stateNumber %lu\n"
- "%06ld.%06d %s::%s: device descriptor name: %s\n"
- "%06ld.%06d %s::%s: device name: %s, pcie reset sep workaround needed: %d\n"
- "%06ld.%06d %s::%s: dir: %u\n"
- "%06ld.%06d %s::%s: direction %s, completion %p\n"
- "%06ld.%06d %s::%s: domain %u\n"
- "%06ld.%06d %s::%s: domain: %u, buff 0x%llx, size %llu, completion %p\n"
- "%06ld.%06d %s::%s: domainState: 0x%lx\n"
- "%06ld.%06d %s::%s: enable %u\n"
- "%06ld.%06d %s::%s: enable %u, failureFatal %u, enabled state: %u\n"
- "%06ld.%06d %s::%s: enable AER notification\n"
- "%06ld.%06d %s::%s: enable interrupt %u\n"
- "%06ld.%06d %s::%s: enable sleep %u\n"
- "%06ld.%06d %s::%s: enable: %u\n"
- "%06ld.%06d %s::%s: enablePCIPowerManagement failed 0x%x\n"
- "%06ld.%06d %s::%s: enabled %u, status 0x%08x\n"
- "%06ld.%06d %s::%s: enabled %u, status 0x%x\n"
- "%06ld.%06d %s::%s: enabled: %u, shouldEnable: %u\n"
- "%06ld.%06d %s::%s: enabling L1SS\n"
- "%06ld.%06d %s::%s: endpoint L1PMSS capability not found\n"
- "%06ld.%06d %s::%s: endpoint port PCIe capability not found\n"
- "%06ld.%06d %s::%s: error type %u, arg0 %p, arg1 %p\n"
- "%06ld.%06d %s::%s: failed bytes %llu, size %llu\n"
- "%06ld.%06d %s::%s: failed client is not attached\n"
- "%06ld.%06d %s::%s: failed err %d\n"
- "%06ld.%06d %s::%s: failed to add AER event source\n"
- "%06ld.%06d %s::%s: failed to add Rx submission queue event source workLoop: 0x%x\n"
- "%06ld.%06d %s::%s: failed to add interrupt source\n"
- "%06ld.%06d %s::%s: failed to add matching notification - Default\n"
- "%06ld.%06d %s::%s: failed to add node\n"
- "%06ld.%06d %s::%s: failed to allocate MessageQueue\n"
- "%06ld.%06d %s::%s: failed to allocate Queues\n"
- "%06ld.%06d %s::%s: failed to allocate _lock\n"
- "%06ld.%06d %s::%s: failed to allocate _pciServiceLock\n"
- "%06ld.%06d %s::%s: failed to allocate _rdQueueLock\n"
- "%06ld.%06d %s::%s: failed to allocate commandGate\n"
- "%06ld.%06d %s::%s: failed to allocate io command\n"
- "%06ld.%06d %s::%s: failed to allocate link speed timer\n"
- "%06ld.%06d %s::%s: failed to allocate memory\n"
- "%06ld.%06d %s::%s: failed to allocate timer\n"
- "%06ld.%06d %s::%s: failed to allocate workloop\n"
- "%06ld.%06d %s::%s: failed to allocatePrepareMemory 0x%x\n"
- "%06ld.%06d %s::%s: failed to calculate pool capacity\n"
- "%06ld.%06d %s::%s: failed to create AER event source\n"
- "%06ld.%06d %s::%s: failed to create AppleBasebandPCIIOCommand node\n"
- "%06ld.%06d %s::%s: failed to create AppleBasebandPCIMemoryCommand node\n"
- "%06ld.%06d %s::%s: failed to create AppleBasebandPCIMemoryPolicy node\n"
- "%06ld.%06d %s::%s: failed to create AppleBasebandPCIRequest node\n"
- "%06ld.%06d %s::%s: failed to create DMA command\n"
- "%06ld.%06d %s::%s: failed to create MessageQueue\n"
- "%06ld.%06d %s::%s: failed to create Rx Completion queue!\n"
- "%06ld.%06d %s::%s: failed to create Rx Submission queue!\n"
- "%06ld.%06d %s::%s: failed to create Rx pool\n"
- "%06ld.%06d %s::%s: failed to create Rx queue\n"
- "%06ld.%06d %s::%s: failed to create Rx submission queue\n"
- "%06ld.%06d %s::%s: failed to create Tx Completion queue!\n"
- "%06ld.%06d %s::%s: failed to create Tx Submission queue!\n"
- "%06ld.%06d %s::%s: failed to create Tx completion queue\n"
- "%06ld.%06d %s::%s: failed to create Tx pool\n"
- "%06ld.%06d %s::%s: failed to create Tx queue\n"
- "%06ld.%06d %s::%s: failed to create command gate\n"
- "%06ld.%06d %s::%s: failed to create event source at %u\n"
- "%06ld.%06d %s::%s: failed to create interrupt event source\n"
- "%06ld.%06d %s::%s: failed to create lock\n"
- "%06ld.%06d %s::%s: failed to create memory descriptor\n"
- "%06ld.%06d %s::%s: failed to create memory policy info\n"
- "%06ld.%06d %s::%s: failed to create pci service notifiers\n"
- "%06ld.%06d %s::%s: failed to create pool\n"
- "%06ld.%06d %s::%s: failed to create registration entry\n"
- "%06ld.%06d %s::%s: failed to get link speed: 0x%08x\n"
- "%06ld.%06d %s::%s: failed to get mapper\n"
- "%06ld.%06d %s::%s: failed to get provider of IOPCI2PCIBridge\n"
- "%06ld.%06d %s::%s: failed to get provider of IOPCIDevice\n"
- "%06ld.%06d %s::%s: failed to get work loop\n"
- "%06ld.%06d %s::%s: failed to initialize Rx submission queue: 0x%x\n"
- "%06ld.%06d %s::%s: failed to map bar0\n"
- "%06ld.%06d %s::%s: failed to map bar1\n"
- "%06ld.%06d %s::%s: failed to map bar2\n"
- "%06ld.%06d %s::%s: failed to map memory for %p\n"
- "%06ld.%06d %s::%s: failed to open service\n"
- "%06ld.%06d %s::%s: failed to prepare 0x%x\n"
- "%06ld.%06d %s::%s: failed to prepare Rx pool, 0x%x\n"
- "%06ld.%06d %s::%s: failed to prepare Tx pool, 0x%x\n"
- "%06ld.%06d %s::%s: failed to prepare dma memory for %p\n"
- "%06ld.%06d %s::%s: failed to prepare io command\n"
- "%06ld.%06d %s::%s: failed to prepare log buffer\n"
- "%06ld.%06d %s::%s: failed to prepare qctun Rx buffer pool, 0x%x\n"
- "%06ld.%06d %s::%s: failed to prepare qctun Tx buffer pool, 0x%x\n"
- "%06ld.%06d %s::%s: failed to queue log buffer\n"
- "%06ld.%06d %s::%s: failed to read back bytes %llu, expected size %u\n"
- "%06ld.%06d %s::%s: failed to register network interface: 0x%x\n"
- "%06ld.%06d %s::%s: failed to retrieve DMA segment: 0x%x\n"
- "%06ld.%06d %s::%s: failed to retrieve any of the constants from plist\n"
- "%06ld.%06d %s::%s: failed to retrieve baseband chipset information\n"
- "%06ld.%06d %s::%s: failed to retrieve chipset device map\n"
- "%06ld.%06d %s::%s: failed to retrieve chipset name\n"
- "%06ld.%06d %s::%s: failed to retrieve dart window: 0x%x\n"
- "%06ld.%06d %s::%s: failed to retrieve device descriptor\n"
- "%06ld.%06d %s::%s: failed to retrieve device descriptor map\n"
- "%06ld.%06d %s::%s: failed to retrieve device descriptor name\n"
- "%06ld.%06d %s::%s: failed to retrieve pcie reset seperation workaround dict\n"
- "%06ld.%06d %s::%s: failed to retrieve workaround value\n"
- "%06ld.%06d %s::%s: failed to save registration entry\n"
- "%06ld.%06d %s::%s: failed to set link speed: 0x%08x\n"
- "%06ld.%06d %s::%s: failed to setup baseband service\n"
- "%06ld.%06d %s::%s: failed to setup control %p\n"
- "%06ld.%06d %s::%s: failed to setup port control %p\n"
- "%06ld.%06d %s::%s: failed to start reporting\n"
- "%06ld.%06d %s::%s: failed: 0x%x\n"
- "%06ld.%06d %s::%s: faled to copy data out of mbuf\n"
- "%06ld.%06d %s::%s: flags 0x%x, current state: %s\n"
- "%06ld.%06d %s::%s: flush %u\n"
- "%06ld.%06d %s::%s: forClient %p\n"
- "%06ld.%06d %s::%s: forClient %p, options 0x%08x, inGate %u\n"
- "%06ld.%06d %s::%s: forClient is not AppleBasebandPCIPDPSkywalkInterface\n"
- "%06ld.%06d %s::%s: force: %u, inReset = %u\n"
- "%06ld.%06d %s::%s: free count: %u\n"
- "%06ld.%06d %s::%s: got kOffPowerState\n"
- "%06ld.%06d %s::%s: got kOnPowerState\n"
- "%06ld.%06d %s::%s: got pci publish notifier\n"
- "%06ld.%06d %s::%s: got pci termination notifier\n"
- "%06ld.%06d %s::%s: got publish notifier\n"
- "%06ld.%06d %s::%s: got termination notifier\n"
- "%06ld.%06d %s::%s: ifnet_eflags not in plist\n"
- "%06ld.%06d %s::%s: ifp 0x%p, cmd 0x%x, data 0x%p\n"
- "%06ld.%06d %s::%s: ignore event %d\n"
- "%06ld.%06d %s::%s: ignoring transition\n"
- "%06ld.%06d %s::%s: in-band assert %u\n"
- "%06ld.%06d %s::%s: inReset %u\n"
- "%06ld.%06d %s::%s: index %d\n"
- "%06ld.%06d %s::%s: index %d, getInterruptType error 0x%08x\n"
- "%06ld.%06d %s::%s: index %d, not msi %d\n"
- "%06ld.%06d %s::%s: index %u\n"
- "%06ld.%06d %s::%s: index out of range %d\n"
- "%06ld.%06d %s::%s: interface %u %s\n"
- "%06ld.%06d %s::%s: interface down\n"
- "%06ld.%06d %s::%s: interface was not able to deallocate packet, force deallocating\n"
- "%06ld.%06d %s::%s: interfaces not available\n"
- "%06ld.%06d %s::%s: interval in us %llu, time mode %u\n"
- "%06ld.%06d %s::%s: intfPropMatches %u\n"
- "%06ld.%06d %s::%s: invalid descriptor\n"
- "%06ld.%06d %s::%s: invalid device\n"
- "%06ld.%06d %s::%s: invalid max_rsc_pkts config\n"
- "%06ld.%06d %s::%s: invalid max_rx_aggregation config\n"
- "%06ld.%06d %s::%s: invalid memory %p+%llu\n"
- "%06ld.%06d %s::%s: invalid message %u\n"
- "%06ld.%06d %s::%s: invalid param\n"
- "%06ld.%06d %s::%s: invalid plist, constants not dictionary\n"
- "%06ld.%06d %s::%s: invalid range: 0x%llx (+ 0x%llx)\n"
- "%06ld.%06d %s::%s: io: %p, iocmd: %p, status 0x%x, size %u, eot %d\n"
- "%06ld.%06d %s::%s: iocmd: %p, prev: %p, io: %p, pa: 0x%llx, OOO IO: %u, Intf Idx: %u, Chan Idx: %u, id: %u\n"
- "%06ld.%06d %s::%s: isDefaultQueueSet: %u\n"
- "%06ld.%06d %s::%s: link control2: 0x%08x, current target link speed: %u\n"
- "%06ld.%06d %s::%s: link control2: 0x%08x, target link speed: %u\n"
- "%06ld.%06d %s::%s: link speed mismatch: expected %u, actual %u\n"
- "%06ld.%06d %s::%s: linkState %u\n"
- "%06ld.%06d %s::%s: logical link / interface down\n"
- "%06ld.%06d %s::%s: logical link property is NULL!\n"
- "%06ld.%06d %s::%s: map %u\n"
- "%06ld.%06d %s::%s: mapped bar0 address 0x%llx (pa: 0x%llx) (+0x%x)\n"
- "%06ld.%06d %s::%s: mapped bar1 address 0x%llx (pa: 0x%llx) (+0x%x)\n"
- "%06ld.%06d %s::%s: mapped bar2 address 0x%llx (pa: 0x%llx) (+0x%x)\n"
- "%06ld.%06d %s::%s: mapper %p\n"
- "%06ld.%06d %s::%s: mapper 0x%p\n"
- "%06ld.%06d %s::%s: mapper cleared\n"
- "%06ld.%06d %s::%s: mapping bearer ID: %u, to queueset failed!\n"
- "%06ld.%06d %s::%s: mapping pending segments\n"
- "%06ld.%06d %s::%s: mbuf allocate failed err %d\n"
- "%06ld.%06d %s::%s: mem: %p\n"
- "%06ld.%06d %s::%s: memory limit reached\n"
- "%06ld.%06d %s::%s: memory not dart page aligned 0x%llx\n"
- "%06ld.%06d %s::%s: memory size not multiple of dart page size %llu\n"
- "%06ld.%06d %s::%s: memoryAllocLimit %llu, mapper %p\n"
- "%06ld.%06d %s::%s: messaging clients: message %s (0x%x), arg %p\n"
- "%06ld.%06d %s::%s: mmio read fail at %p\n"
- "%06ld.%06d %s::%s: muxed rx slot count not found in plist\n"
- "%06ld.%06d %s::%s: name: %s"
- "%06ld.%06d %s::%s: no manager\n"
- "%06ld.%06d %s::%s: no mapper\n"
- "%06ld.%06d %s::%s: no memory\n"
- "%06ld.%06d %s::%s: no pci service\n"
- "%06ld.%06d %s::%s: no provider\n"
- "%06ld.%06d %s::%s: no registration for time domain %u\n"
- "%06ld.%06d %s::%s: no slot available\n"
- "%06ld.%06d %s::%s: nomem\n"
- "%06ld.%06d %s::%s: nonmem for interface array\n"
- "%06ld.%06d %s::%s: not an AppleBasebandPCIPDPSkywalkInterface\n"
- "%06ld.%06d %s::%s: not disabling a device in reset\n"
- "%06ld.%06d %s::%s: not in sleep, bail\n"
- "%06ld.%06d %s::%s: nothing to process\n"
- "%06ld.%06d %s::%s: notifying AppleBaseband that PCI driver is registered for notifications\n"
- "%06ld.%06d %s::%s: oob Tx info allocation\n"
- "%06ld.%06d %s::%s: open failed, _pciService: %p\n"
- "%06ld.%06d %s::%s: options 0x%08x\n"
- "%06ld.%06d %s::%s: owner %u\n"
- "%06ld.%06d %s::%s: owner: %p, bearer ID: %u, status: %u\n"
- "%06ld.%06d %s::%s: packet %p\n"
- "%06ld.%06d %s::%s: packet allocation failed: 0x%x\n"
- "%06ld.%06d %s::%s: packet return %p\n"
- "%06ld.%06d %s::%s: pci bridge - device %p, stateNumber %lu\n"
- "%06ld.%06d %s::%s: pci bridge -- power on\n"
- "%06ld.%06d %s::%s: pci control, stateNumber %lu\n"
- "%06ld.%06d %s::%s: pci device open ret %u\n"
- "%06ld.%06d %s::%s: pci low power entry ack timeout\n"
- "%06ld.%06d %s::%s: pci low power entry acknowledged\n"
- "%06ld.%06d %s::%s: pci low power entry deferred\n"
- "%06ld.%06d %s::%s: pci service - device %p, stateNumber %lu\n"
- "%06ld.%06d %s::%s: pci service ID: %u\n"
- "%06ld.%06d %s::%s: pci service entered low power\n"
- "%06ld.%06d %s::%s: pci service exited low power\n"
- "%06ld.%06d %s::%s: pci service missing or in low power\n"
- "%06ld.%06d %s::%s: pci service not available\n"
- "%06ld.%06d %s::%s: pci service not available for MSI registration\n"
- "%06ld.%06d %s::%s: pci service open failed, service ID: %p\n"
- "%06ld.%06d %s::%s: pci service open failed, service: %p\n"
- "%06ld.%06d %s::%s: pci service: %p, isPublished: %u\n"
- "%06ld.%06d %s::%s: pciService not available\n"
- "%06ld.%06d %s::%s: pending\n"
- "%06ld.%06d %s::%s: plist does not contain constants for fallback (\"%s\")\n"
- "%06ld.%06d %s::%s: plist doesn't have Rx throughput specification\n"
- "%06ld.%06d %s::%s: plist doesn't have rx slot size\n"
- "%06ld.%06d %s::%s: plist doesn't have tx slot size\n"
- "%06ld.%06d %s::%s: plist error, constants property is not dictionary\n"
- "%06ld.%06d %s::%s: pool capacity: tx=%u, rx=%u\n"
- "%06ld.%06d %s::%s: pool not available\n"
- "%06ld.%06d %s::%s: pool: %p, Intf idx: %u\n"
- "%06ld.%06d %s::%s: port %p\n"
- "%06ld.%06d %s::%s: port already disabled\n"
- "%06ld.%06d %s::%s: port enable failed\n"
- "%06ld.%06d %s::%s: port enable failed!, ret: 0x%08x\n"
- "%06ld.%06d %s::%s: port enable panic setting: %u\n"
- "%06ld.%06d %s::%s: port is locked\n"
- "%06ld.%06d %s::%s: provider %p, options 0x%08x\n"
- "%06ld.%06d %s::%s: provider %p, options 0x%08x, defer %p\n"
- "%06ld.%06d %s::%s: provider is NULL\n"
- "%06ld.%06d %s::%s: provider is not AppleBasebandPCIPDPManagerBase\n"
- "%06ld.%06d %s::%s: provider is not an instance of AppleBasebandPCIInterface\n"
- "%06ld.%06d %s::%s: publishing %u PDP interfaces\n"
- "%06ld.%06d %s::%s: qctun interface enabled\n"
- "%06ld.%06d %s::%s: qctun interface number: %u\n"
- "%06ld.%06d %s::%s: qctun interface rx slot count not specified in plist!\n "
- "%06ld.%06d %s::%s: qctun interface rx slot count: %u\n"
- "%06ld.%06d %s::%s: qctun interface slot size not specified in plist!\n "
- "%06ld.%06d %s::%s: qctun interface slot size: %u\n"
- "%06ld.%06d %s::%s: qctun interface tx slot count not specified in plist!\n "
- "%06ld.%06d %s::%s: queue set config is NULL!\n"
- "%06ld.%06d %s::%s: queueSetID: 0x%llx, _isDefault: %u, index: %u\n"
- "%06ld.%06d %s::%s: raw Tx cached pkts: %u\n"
- "%06ld.%06d %s::%s: raw Tx freed pkts: %u\n"
- "%06ld.%06d %s::%s: refCon %p, _pciPublishNotifier %p, _pciTerminateNotifier %p\n"
- "%06ld.%06d %s::%s: refcon: %p, pci service: %p\n"
- "%06ld.%06d %s::%s: reg %d, size %d\n"
- "%06ld.%06d %s::%s: reg %u, buff %p, size %u\n"
- "%06ld.%06d %s::%s: region %u already mapped\n"
- "%06ld.%06d %s::%s: region %u not mapped\n"
- "%06ld.%06d %s::%s: region ID: %u, memory: %p, memorySize: %llu\n"
- "%06ld.%06d %s::%s: region Id: %u\n"
- "%06ld.%06d %s::%s: registered %p and set level to %u\n"
- "%06ld.%06d %s::%s: requested: %u, queued: %u\n"
- "%06ld.%06d %s::%s: requesting power state to be OFF\n"
- "%06ld.%06d %s::%s: requesting power state to be ON\n"
- "%06ld.%06d %s::%s: ret 0x%x, info 0x%llx\n"
- "%06ld.%06d %s::%s: retry %d\n"
- "%06ld.%06d %s::%s: root port L1PMSS capability not found\n"
- "%06ld.%06d %s::%s: root port PCIe capability not found\n"
- "%06ld.%06d %s::%s: rsc_service not present in plist or unsupported\n"
- "%06ld.%06d %s::%s: runAction failed with 0x%08x\n"
- "%06ld.%06d %s::%s: runAsync failed: %s\n"
- "%06ld.%06d %s::%s: rx pool capacity count not found in plist\n"
- "%06ld.%06d %s::%s: rx pool unavailable\n"
- "%06ld.%06d %s::%s: same mapper, skip remapping\n"
- "%06ld.%06d %s::%s: segment %p\n"
- "%06ld.%06d %s::%s: served %u raw Tx, %u remain\n"
- "%06ld.%06d %s::%s: service %p is not AppleBasebandPCI object\n"
- "%06ld.%06d %s::%s: service ID: %u\n"
- "%06ld.%06d %s::%s: service already open by %p\n"
- "%06ld.%06d %s::%s: service is terminating\n"
- "%06ld.%06d %s::%s: serviceID: %u, not present\n"
- "%06ld.%06d %s::%s: serviceID: %u, serviceObj: %p published\n"
- "%06ld.%06d %s::%s: set link speed to %u\n"
- "%06ld.%06d %s::%s: set power request %d\n"
- "%06ld.%06d %s::%s: shared mem unmapping failed: 0x%x\n"
- "%06ld.%06d %s::%s: shared memory mapping for region: %u, failed\n"
- "%06ld.%06d %s::%s: signal output request\n"
- "%06ld.%06d %s::%s: size %llu\n"
- "%06ld.%06d %s::%s: skipping port enable due to system power (sleep %d, shutdown %d)\n"
- "%06ld.%06d %s::%s: staged: %u\n"
- "%06ld.%06d %s::%s: success\n"
- "%06ld.%06d %s::%s: super class failed to initialize\n"
- "%06ld.%06d %s::%s: super failed\n"
- "%06ld.%06d %s::%s: super match failed\n"
- "%06ld.%06d %s::%s: super returned false\n"
- "%06ld.%06d %s::%s: super::init failed\n"
- "%06ld.%06d %s::%s: super::start failed\n"
- "%06ld.%06d %s::%s: t %u, arg0 %p, arg1 %p\n"
- "%06ld.%06d %s::%s: this %p\n"
- "%06ld.%06d %s::%s: this %p, pool %p, memPolicy %p\n"
- "%06ld.%06d %s::%s: this %p, status 0x%x, size %llu, cookie %p\n"
- "%06ld.%06d %s::%s: this: %p\n"
- "%06ld.%06d %s::%s: thread call failed with 0x%08x\n"
- "%06ld.%06d %s::%s: time event for domain %u is already registered\n"
- "%06ld.%06d %s::%s: timerMode %u, arg1 %p\n"
- "%06ld.%06d %s::%s: trigger power state change\n"
- "%06ld.%06d %s::%s: tx pool unavailable\n"
- "%06ld.%06d %s::%s: type %d status 0x%x header 0x%x 0x%x 0x%x 0x%x\n"
- "%06ld.%06d %s::%s: unRegistering MSI for index %u\n"
- "%06ld.%06d %s::%s: unable to allocate link status report staging buffer\n"
- "%06ld.%06d %s::%s: unable to configure the IPAppender for ifnet\n"
- "%06ld.%06d %s::%s: unable to create PCIfoundAB dictionary\n"
- "%06ld.%06d %s::%s: unable to create link speed dictionary\n"
- "%06ld.%06d %s::%s: unable to create matching dictionary\n"
- "%06ld.%06d %s::%s: unable to create port enable dictionaries\n"
- "%06ld.%06d %s::%s: unable to create port sleep enable/disable dictionaries\n"
- "%06ld.%06d %s::%s: unable to find AppleBasebandPCIPDPManagerBase service\n"
- "%06ld.%06d %s::%s: unable to find AppleIPAppender service\n"
- "%06ld.%06d %s::%s: unable to initialize pending segment list\n"
- "%06ld.%06d %s::%s: unable to unmap memory segment.\n"
- "%06ld.%06d %s::%s: unit number %u already has a session open\n"
- "%06ld.%06d %s::%s: unit number %u invalid or nonexistent\n"
- "%06ld.%06d %s::%s: unknown baseband chipset %s, no fallback option\n"
- "%06ld.%06d %s::%s: unknown client\n"
- "%06ld.%06d %s::%s: unknown message 0x%x\n"
- "%06ld.%06d %s::%s: unmapped bar\n"
- "%06ld.%06d %s::%s: unmapping leftover region %u\n"
- "%06ld.%06d %s::%s: va 0x%llx, pa 0x%llx, offset %llu\n"
- "%06ld.%06d %s::%s: vendorID = 0x%04x, deviceID = 0x%04x\n"
- "%06ld.%06d %s::%s: wait %u, event %p\n"
- "%06ld.%06d %s::%s: workloop: %p\n"
- "%3u"
- "%3u to %3u"
- "%3u to inf"
- "%d. size %llu, %p "
- "%s Close"
- "%s Open "
- "%s Read "
- "%s TimeSync"
- "%s Write"
- "%s: %u:%u was not found\n"
- "%s: logger user knob %u:%u already registered\n"
- "+-----------------------------------------------+----------------+"
- "/Library/Caches/com.apple.xbs/Sources/AppleBasebandPCI/AppleBasebandPCIControl/AppleBasebandPCILogger.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleBasebandPCI/AppleBasebandPCIPDP/AppleBasebandPCIPDPReporter.cpp"
- "11211"
- "112111111"
- "1211"
- "1211111212221212111111112111112111111111111112112112112111121121111121"
- "12111112122212121111111121111121111111111111121121121121111211211111212"
- "121111121222121211112111222222212111112222212121"
- "121111121222121212111111111111111111111122122122221111111111222"
- "12111112122212121212111111111111111111111122222222222222222222222222222222222111111111111111111111111111111111111111111111111111111111111111111111122222222222222222111112112222222"
- "12111112122212121222222222111222112111112"
- "12112221111111111111"
- "12212"
- "Advanced Error Reporting"
- "Aggregated Block"
- "AppleBasebandPCI state dump:\n"
- "AppleBasebandPCI::start: failed to get logger\n"
- "AppleBasebandPCIControlReporter"
- "AppleBasebandPCILogger"
- "AppleBasebandPCILogger.cpp"
- "AppleBasebandPCILogger::initWithInfo: AppleBasebandPCILogger instance already exists\n"
- "AppleBasebandPCILogger::initWithInfo: pDictionary creation failed\n"
- "AppleBasebandPCILogger::initWithInfo: super::init failed\n"
- "AppleBasebandPCILogger::start: failed to allocate memory for snapshot buffer\n"
- "AppleBasebandPCIPDPManagerBase::start: failed to get logger\n"
- "AppleBasebandPCIPDPReporter"
- "AppleBasebandPCIPDPReporter.cpp"
- "AppleBasebandPCIReporter"
- "AppleBasebandPCIReporter::%s: could not create a legend\n"
- "AppleBasebandPCIReporter::%s: could not create a set object\n"
- "AppleBasebandPCIReporter::%s: invalid argument\n"
- "AppleBasebandPCIReporter::%s: setProperty failed\n"
- "AppleBasebandPCIReporter::%s: subclass failed to add reporters\n"
- "Binary"
- "Correctable Error"
- "Counters"
- "Current State Index"
- "DL"
- "DL Aggregation Histogram"
- "DL Drop Counters"
- "DL Limit"
- "DL Limiter State"
- "Downlink Bytes"
- "Downlink Pkts"
- "Dropped Downlink Bytes"
- "Dropped Downlink Packets"
- "Error"
- "False"
- "Fatal Error"
- "Flow Control"
- "Global"
- "I"
- "I/O"
- "IOReportLegend"
- "IOReportLegendPublic"
- "Interfaces"
- "Interrupt"
- "Invalid Interface"
- "Link Status Notifications"
- "Non-Fatal Error"
- "PDP"
- "PDP packet dump level"
- "PDP packet dump new level: %u\n"
- "PDP packet dump size"
- "Power"
- "Publish Count"
- "Secondary ISR Count"
- "Secondary Interrupt Handler"
- "State Summary"
- "States"
- "Terminate Count"
- "True"
- "UL"
- "UL Aggregation Histogram"
- "Uplink Bytes"
- "Uplink Pkts"
- "abortChannel"
- "abp-debug"
- "abp-debug-buf-size"
- "abp-flags"
- "abp-kdbg-trace"
- "abp-reporting"
- "addNode"
- "allocQueues"
- "allocatePrepareMemory"
- "allocateRawTxCache"
- "allocateReturnCommand"
- "asyncFunction"
- "asyncThreadCallGated"
- "bounceIn"
- "bounceOut"
- "calculateBufferPoolCapacity"
- "callAsync"
- "cancel"
- "cancelAsync"
- "cancelCompletion"
- "cancelTimer"
- "changeState"
- "checkPortAction"
- "checkPortOffCycleGated"
- "cleanCommandParamters"
- "cleanRequestParamters"
- "clearDMATransfer"
- "clientClose"
- "clientCloseGated"
- "close"
- "closeGated"
- "closePublishedPCIDataServicesGated"
- "closeServiceGated"
- "complete"
- "completeGatedFunction"
- "completeMemory"
- "configureReport"
- "createDedicatedQueueSet"
- "createDefaultQueueSet"
- "createInitRxSubmissionQueue"
- "createLogicalLinkGated_block_invoke"
- "createQueueSets"
- "createQueues"
- "createRxSubmissionQueue"
- "createSetupPort"
- "currentLogSnapshotBufferSize"
- "dartErrorHandler"
- "deRegisterPort"
- "deregisterTimeEvent"
- "deregisterUserKnob"
- "deviceAwakeCheck"
- "deviceWakeAsync"
- "deviceWakeFunction"
- "didTerminate"
- "disableLockPort"
- "disableLockPortGated"
- "discardRxPacket"
- "down"
- "enableASPMGated"
- "enableDefaultQueueSet"
- "enableHostMemProtectionGated"
- "enableL1SSGated"
- "enableUnlockPort"
- "enableUnlockPortGated"
- "enqueuePDPEvent"
- "enqueuePackets"
- "enterLowPower"
- "errorFunction"
- "exitLowPower"
- "failed to create logger\n"
- "flushQueueSets"
- "flushStageQueue"
- "free"
- "freeRawTxCache"
- "gatedReturnCommand"
- "gatherEPConfigRegSpace"
- "getChipsetConstants"
- "getCommand"
- "getCurrentLinkSpeedGated"
- "getDeviceDescriptorDict"
- "getDeviceResetState"
- "getEPTransactionPendingBit"
- "getInLowPower"
- "getInReset"
- "getQCTunBufferPool"
- "handleAER"
- "handleClose"
- "handleIsOpen"
- "handleOpen"
- "handlePCIMessage"
- "handlePCIServiceSwitch"
- "initBSDInterfaceParameters"
- "initUserDefaults"
- "initWithInfo"
- "initWithName"
- "initWithOptions"
- "initWithPool"
- "initWithWorkLoop"
- "initialPowerStateForDomainState"
- "initialize"
- "invokeAsync"
- "ioCompletionFunction"
- "ipAppenderMessage"
- "isPCIServicePublished"
- "linkDown"
- "linkDownCheck"
- "linkSpeedCheck"
- "linkStateUpFunction"
- "linkUp"
- "linkUpCheck"
- "lockPort"
- "logPacket"
- "logSnapshotBufferSize"
- "logger attach/start failed %p\n"
- "manualDisablePort"
- "manualEnablePort"
- "map"
- "mapBarGated"
- "mapBearerToQueueSet"
- "mapSharedMemory"
- "mapSharedMemory_block_invoke"
- "matchPropertyTable"
- "mmioRead"
- "mmioReadMemory"
- "msiInterrupt"
- "newMemorySegment"
- "newPacket"
- "notify"
- "notifyDedicatedBearer"
- "notifyPCIServiceDidTerminateGated"
- "notifyPCIServiceGated"
- "notifyPortStateChange"
- "notifyTerminateAck"
- "notifyTerminateAckGated"
- "open"
- "openGated"
- "openPublishedPCIDataServicesGated"
- "openServiceGated"
- "packetDump"
- "pciMessageGated"
- "pciNotifier"
- "pciRegisterGated"
- "pciServiceNotifyDidTerminate"
- "pciServiceNotifyDidTerminateGated"
- "pciServiceNotifyPublishGated"
- "pciServiceNotifyTerminateGated"
- "pcieResetSeperationROMWA"
- "pdp:%s: error %d\n"
- "pdp:%s: size (%u) out of range.\n"
- "pdpEventHandler"
- "pdp_dump_level"
- "pdp_dump_size"
- "pdp_ip%u"
- "portAction"
- "portActionDone"
- "portChangeFunction"
- "portDeepSleep"
- "portEnable"
- "portEnabled"
- "portManualEnableFunction"
- "portQuiesceWaitFunction"
- "portSleep"
- "portWake"
- "powerStateDidChangeTo"
- "powerStateDidChangeToGated"
- "powerStateWillChangeTo"
- "powerStateWillChangeToGated"
- "prepare"
- "prepareBSDInterface"
- "prepareDMATransfer"
- "prepareIn"
- "prepareMemory"
- "prepareOut"
- "preparePoolsWithMapper"
- "processBSDCommand"
- "processCurrentPortAction"
- "publish"
- "qctunBufferPoolCapacity"
- "queryFreeSpace"
- "queueLogBuffer"
- "queueRxBuffersGated"
- "rawTxPrepare"
- "read"
- "readLogs"
- "registerAER"
- "registerDARTErrorHandler"
- "registerDebugObject"
- "registerMSI"
- "registerMSI_block_invoke"
- "registerPort"
- "registerRead"
- "registerTimeEvent"
- "registerUserKnob"
- "registerWorkLoop"
- "releaseBasebandService"
- "reportError"
- "reportInterfaceAdvisory"
- "reportLinkStatus"
- "reportMessage"
- "requestDequeue"
- "requestPortOffCycleGated"
- "requestTxGated"
- "resetStageQueue"
- "returnPacket"
- "running"
- "rxQueueCallbackGated"
- "scan"
- "sendImage"
- "serveRawTxQueue"
- "serviceNotifier"
- "serviceRegisterGated"
- "setBootStage"
- "setIO"
- "setInReset"
- "setLinkSpeedGated"
- "setMapper"
- "setName"
- "setPowerOn"
- "setPowerState"
- "setPowerStateGated"
- "setQueueSetId"
- "setRunningState"
- "setTargetLinkSpeedGated"
- "setupBasebandService"
- "setupDARTWindowGated"
- "setupPort"
- "shared memory"
- "site.AppleBasebandPCIControlReporter"
- "site.AppleBasebandPCILogger"
- "site.AppleBasebandPCIPDPReporter"
- "site.AppleBasebandPCIReporter"
- "site.IOSimpleReporter*"
- "site.IOStateReporter*"
- "site.StateEntry"
- "site.UserKnob"
- "site.logBuffer"
- "site.logBufferQueue"
- "site.struct StateEntry"
- "sleepAckFunction"
- "sleepCheck"
- "some logs dropped\n"
- "stagePkts"
- "stageQueueGetRxPkts"
- "stageQueueGetTxPkts"
- "startChannel"
- "startReporting"
- "startSleepTimer"
- "startTimer"
- "stop"
- "stopped"
- "switchBearerTrafficToService"
- "syncSIOCSIFFLAGS"
- "sysctl_pdp_dump_level"
- "sysctl_pdp_dump_size"
- "teardownPort"
- "telescoperRecordCompletedPackets"
- "terminate"
- "timeSync"
- "timer"
- "timerCompletion"
- "timerFunction"
- "transferDone"
- "triggerMSI"
- "triggerTxDequeue"
- "txCompletionCallbackGated"
- "txQueueCallbackGated"
- "unRegisterMSI"
- "unRegisterMSI_block_invoke"
- "unlockPort"
- "unmap"
- "unmapBarGated"
- "unmapBearerFromQueueSet"
- "unmapSharedMemory"
- "unmapSharedMemory_block_invoke"
- "up"
- "updateEnabled"
- "updateReport"
- "usesLowLatencyService"
- "usesRSCService"
- "validateMSIIndex"
- "willTerminate"
- "willTerminateGated"
- "write"
- "|%02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x|%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c|"
- "~ABPControl"
- "~ABPNullDevice"
- "~ABPPort"

```

>  `com.apple.driver.AppleBasebandPCIMAVControl`

```diff

 810.0.0.0.0
   __TEXT.__const: 0x262a
-  __TEXT.__cstring: 0x67ee
-  __TEXT_EXEC.__text: 0x511fc
+  __TEXT.__cstring: 0x11c5
+  __TEXT_EXEC.__text: 0x283ac
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x140
-  __DATA.__common: 0x100
+  __DATA.__common: 0xd8
   __DATA.__bss: 0x1760
-  __DATA_CONST.__auth_got: 0x298
-  __DATA_CONST.__got: 0xd8
-  __DATA_CONST.__mod_init_func: 0xaf8
-  __DATA_CONST.__mod_term_func: 0x38
-  __DATA_CONST.__const: 0x7dc0
-  __DATA_CONST.__kalloc_type: 0xc80
+  __DATA_CONST.__auth_got: 0x258
+  __DATA_CONST.__got: 0xc8
+  __DATA_CONST.__mod_init_func: 0xaf0
+  __DATA_CONST.__mod_term_func: 0x30
+  __DATA_CONST.__const: 0x7c38
+  __DATA_CONST.__kalloc_type: 0xc40
   __DATA_CONST.__kalloc_var: 0x5a0
-  Functions: 1079
+  Functions: 1053
   Symbols:   0
-  CStrings:  720
+  CStrings:  177
 
CStrings:
+ "121111121222121212111111111111111111111122122122221111111112222"
- "%06ld.%06d %s::%s: \n"
- "%06ld.%06d %s::%s:  --done\n"
- "%06ld.%06d %s::%s: %d. \n"
- "%06ld.%06d %s::%s: %d.  --done\n"
- "%06ld.%06d %s::%s: %d. %p [0x%llx]\n"
- "%06ld.%06d %s::%s: %d. %p [0x%llx], queued IOs: %lu\n"
- "%06ld.%06d %s::%s: %d. %s -> %s\n"
- "%06ld.%06d %s::%s: %d. (async) failed to prepare memory command\n"
- "%06ld.%06d %s::%s: %d. (async) returned 0x%x\n"
- "%06ld.%06d %s::%s: %d. -- done\n"
- "%06ld.%06d %s::%s: %d. -- done %u\n"
- "%06ld.%06d %s::%s: %d. --done\n"
- "%06ld.%06d %s::%s: %d. Copy memory command\n"
- "%06ld.%06d %s::%s: %d. Device is IN RESET state, bailing\n"
- "%06ld.%06d %s::%s: %d. Exclusive workloop interface, failed to create a control commandGate!\n"
- "%06ld.%06d %s::%s: %d. Getting BB reset state failed\n"
- "%06ld.%06d %s::%s: %d. Unmap shared memory failed\n"
- "%06ld.%06d %s::%s: %d. Virtual timesync interface\n"
- "%06ld.%06d %s::%s: %d. _asyncMode 0x%08x, asyncMode 0x%08x, arg1 %p\n"
- "%06ld.%06d %s::%s: %d. asyncMode 0x%08x\n"
- "%06ld.%06d %s::%s: %d. buffer: 0x%llx, size: %llu, seqNum: %u\n"
- "%06ld.%06d %s::%s: %d. calling completion, ret: 0x%llx\n"
- "%06ld.%06d %s::%s: %d. cf %p, arg0 %p, arg1 %p\n"
- "%06ld.%06d %s::%s: %d. chunk too large\n"
- "%06ld.%06d %s::%s: %d. commandSleep (THREAD_INTERRUPTIBLE) woke with reason 0x%x\n"
- "%06ld.%06d %s::%s: %d. current asyncMode 0x%08x\n"
- "%06ld.%06d %s::%s: %d. direction %s\n"
- "%06ld.%06d %s::%s: %d. direction %u\n"
- "%06ld.%06d %s::%s: %d. direction: %u, workloop: %p\n"
- "%06ld.%06d %s::%s: %d. do not support no copy for mbuf\n"
- "%06ld.%06d %s::%s: %d. error %u\n"
- "%06ld.%06d %s::%s: %d. error type %u, arg0 %p, arg1 %p\n"
- "%06ld.%06d %s::%s: %d. eventIndex %u\n"
- "%06ld.%06d %s::%s: %d. exclusive workloop: %p, msi index: %u\n"
- "%06ld.%06d %s::%s: %d. failed to allocate async interrupt source\n"
- "%06ld.%06d %s::%s: %d. failed to allocate commandGate\n"
- "%06ld.%06d %s::%s: %d. failed to allocate io pool\n"
- "%06ld.%06d %s::%s: %d. failed to allocate memory\n"
- "%06ld.%06d %s::%s: %d. failed to allocate memory command\n"
- "%06ld.%06d %s::%s: %d. failed to create async call lock\n"
- "%06ld.%06d %s::%s: %d. failed to create pools\n"
- "%06ld.%06d %s::%s: %d. failed to prepare memory 0x%x\n"
- "%06ld.%06d %s::%s: %d. failed to prepare memory command\n"
- "%06ld.%06d %s::%s: %d. failed to register channel\n"
- "%06ld.%06d %s::%s: %d. failed to retrieve channel direction\n"
- "%06ld.%06d %s::%s: %d. failed to setup channel\n"
- "%06ld.%06d %s::%s: %d. failed to setup interface _outChannel %p, _inChannel %p\n"
- "%06ld.%06d %s::%s: %d. failed to setup transfer ring\n"
- "%06ld.%06d %s::%s: %d. forClient %p, options 0x%08x\n"
- "%06ld.%06d %s::%s: %d. forClient %p, options 0x%08x, arg %p\n"
- "%06ld.%06d %s::%s: %d. forClient %p, options 0x%08x, arg %p, inGate %u\n"
- "%06ld.%06d %s::%s: %d. forClient %p, options 0x%08x, inGate %u\n"
- "%06ld.%06d %s::%s: %d. incomplete io\n"
- "%06ld.%06d %s::%s: %d. index %u\n"
- "%06ld.%06d %s::%s: %d. interface is inactive\n"
- "%06ld.%06d %s::%s: %d. invalid channel direction\n"
- "%06ld.%06d %s::%s: %d. invalid channel protocol\n"
- "%06ld.%06d %s::%s: %d. invalid direction: %u for the interface\n"
- "%06ld.%06d %s::%s: %d. io %p, pa: 0x%llx, tre %p\n"
- "%06ld.%06d %s::%s: %d. io %p, size %u, pa 0x%llx\n"
- "%06ld.%06d %s::%s: %d. io %p, tre %p, io->_pa %p, cookie 0x%lx\n"
- "%06ld.%06d %s::%s: %d. io: %p, pa 0x%llx\n"
- "%06ld.%06d %s::%s: %d. io: %p, status 0x%x\n"
- "%06ld.%06d %s::%s: %d. io: %p, type: %u, status 0x%x, last: %u\n"
- "%06ld.%06d %s::%s: %d. malformed count, count: %u\n"
- "%06ld.%06d %s::%s: %d. map buffer ack failed: 0x%llx\n"
- "%06ld.%06d %s::%s: %d. map buffer ack timed out: 0x%llx\n"
- "%06ld.%06d %s::%s: %d. map completion failed\n"
- "%06ld.%06d %s::%s: %d. map completion failed, mem is NULL\n"
- "%06ld.%06d %s::%s: %d. map completion success\n"
- "%06ld.%06d %s::%s: %d. memCmd %p, size %llu\n"
- "%06ld.%06d %s::%s: %d. mem[%llu] %p, direction %u\n"
- "%06ld.%06d %s::%s: %d. mhiDevice %p\n"
- "%06ld.%06d %s::%s: %d. no in channel\n"
- "%06ld.%06d %s::%s: %d. no out channel\n"
- "%06ld.%06d %s::%s: %d. num of chunks in io too large\n"
- "%06ld.%06d %s::%s: %d. openGated failed, result: 0x%08x\n"
- "%06ld.%06d %s::%s: %d. options 0x%08x\n"
- "%06ld.%06d %s::%s: %d. pa 0x%llx, size %u, code %u\n"
- "%06ld.%06d %s::%s: %d. pa 0x%llx, size %u, code %u, ccid %u, queued IOs: %lu\n"
- "%06ld.%06d %s::%s: %d. packetChain %p\n"
- "%06ld.%06d %s::%s: %d. part1 subDescSize %llu, offset %llu\n"
- "%06ld.%06d %s::%s: %d. part1 subDesc[%llu] physical address 0x%llx\n"
- "%06ld.%06d %s::%s: %d. part2 subDescSize %llu, offset %llu\n"
- "%06ld.%06d %s::%s: %d. part2 subDesc[%llu] physical address 0x%llx\n"
- "%06ld.%06d %s::%s: %d. part3 subDescSize %llu, offset %llu\n"
- "%06ld.%06d %s::%s: %d. part3 subDesc[%llu] physical address 0x%llx\n"
- "%06ld.%06d %s::%s: %d. prop %p\n"
- "%06ld.%06d %s::%s: %d. provider %p, options 0x%08x\n"
- "%06ld.%06d %s::%s: %d. provider %p, options 0x%08x, defer %p\n"
- "%06ld.%06d %s::%s: %d. queued IOs: %u\n"
- "%06ld.%06d %s::%s: %d. reap elements\n"
- "%06ld.%06d %s::%s: %d. reliable %u\n"
- "%06ld.%06d %s::%s: %d. res = 0x%x, size = %llu, cookie %p\n"
- "%06ld.%06d %s::%s: %d. reset the channels\n"
- "%06ld.%06d %s::%s: %d. result: %u, seqNum: %u, bytes read: %u\n"
- "%06ld.%06d %s::%s: %d. ring - va: 0x%llx, pa: 0x%llx\\n"
- "%06ld.%06d %s::%s: %d. ring not aligned to %u\n"
- "%06ld.%06d %s::%s: %d. ring not large enough %u\n"
- "%06ld.%06d %s::%s: %d. ring va 0x%llx, pa 0x%llx, size %u\n"
- "%06ld.%06d %s::%s: %d. sending map message failed: 0x%llx\n"
- "%06ld.%06d %s::%s: %d. sending unmap message failed: 0x%llx\n"
- "%06ld.%06d %s::%s: %d. service is terminating\n"
- "%06ld.%06d %s::%s: %d. setting defaultInt %d, defaultIEOT %d, defaultIEOB %d\n"
- "%06ld.%06d %s::%s: %d. setting doorbellSetting time %llu, threshold %u\n"
- "%06ld.%06d %s::%s: %d. setting threshold intThreshold %d, ieotThreshold %d, ieobThreshold %d\n"
- "%06ld.%06d %s::%s: %d. setting up map message completion failed: 0x%llx\n"
- "%06ld.%06d %s::%s: %d. setting up unmap message completion failed: 0x%llx\n"
- "%06ld.%06d %s::%s: %d. sharedER %u\n"
- "%06ld.%06d %s::%s: %d. skipping channel setup for channel protocol: %s\n"
- "%06ld.%06d %s::%s: %d. status 0x%x\n"
- "%06ld.%06d %s::%s: %d. status: %u, size: %u\n"
- "%06ld.%06d %s::%s: %d. status: 0x%llx, size: %llu\n"
- "%06ld.%06d %s::%s: %d. super::start failed\n"
- "%06ld.%06d %s::%s: %d. sync %u\n"
- "%06ld.%06d %s::%s: %d. tre %p, size %u, code %u, last %u, io %p\n"
- "%06ld.%06d %s::%s: %d. trigger %u, index %u\n"
- "%06ld.%06d %s::%s: %d. type %u\n"
- "%06ld.%06d %s::%s: %d. type %u, completion code %u, asyncMode %u\n"
- "%06ld.%06d %s::%s: %d. unmap buffer ack timed out: 0x%llx\n"
- "%06ld.%06d %s::%s: %d. unmap completion failed\n"
- "%06ld.%06d %s::%s: %d. unmap completion failed, mem is NULL\n"
- "%06ld.%06d %s::%s: %d. unmap completion success\n"
- "%06ld.%06d %s::%s: %d. waiting for map completion\n"
- "%06ld.%06d %s::%s: %d. waiting for unmap completion\n"
- "%06ld.%06d %s::%s: %s -> %s\n"
- "%06ld.%06d %s::%s: %u\n"
- "%06ld.%06d %s::%s: (async) failed to create memory decriptor for shared memory region\n"
- "%06ld.%06d %s::%s: -- done\n"
- "%06ld.%06d %s::%s: -- done %u\n"
- "%06ld.%06d %s::%s: --done\n"
- "%06ld.%06d %s::%s: ABPDevice %p, type %u\n"
- "%06ld.%06d %s::%s: Bailing, device not alive\n!"
- "%06ld.%06d %s::%s: Both channels should have same msi_index values, (%u, %u)\n"
- "%06ld.%06d %s::%s: CHDBOFF (0x%x) invalid\n"
- "%06ld.%06d %s::%s: Could not find %s dictionary for time_sync!\n"
- "%06ld.%06d %s::%s: Could not find time_sync dictionary!\n"
- "%06ld.%06d %s::%s: Cur expiry: %llu\n"
- "%06ld.%06d %s::%s: Cur expiry: %llu < timeout: %llu\n"
- "%06ld.%06d %s::%s: Desired link speed: %u, boot stage: %u\n"
- "%06ld.%06d %s::%s: Device in Reset state! Skip sending unmap message!\n"
- "%06ld.%06d %s::%s: Device in low power, cannot immediately initiate time sync\n"
- "%06ld.%06d %s::%s: Device in low power, cannot initiate time sync\n"
- "%06ld.%06d %s::%s: ERDBOFF (0x%x) invalid\n"
- "%06ld.%06d %s::%s: ERE: res: 0x%lx, cookie: 0x%lx, code %u, ccid: %u, len: %u, allFields: 0x%lx\n"
- "%06ld.%06d %s::%s: Error 0x%x\n"
- "%06ld.%06d %s::%s: Error getting channel doorbell number for time_sync property!\n"
- "%06ld.%06d %s::%s: Event Ring Index %u: shared channel: %u\n"
- "%06ld.%06d %s::%s: Failed to allocate pending event queue for shared ER index: %u\n"
- "%06ld.%06d %s::%s: Failed to find time sync capability register\n"
- "%06ld.%06d %s::%s: Failed to get device properties dictionary\n"
- "%06ld.%06d %s::%s: Found time sync capability register\n"
- "%06ld.%06d %s::%s: Host sleep Deferred\n"
- "%06ld.%06d %s::%s: Inserting shared mem region with ID: %u\n"
- "%06ld.%06d %s::%s: Invalid domain: %u\n"
- "%06ld.%06d %s::%s: MHI Status: 0x%x\n"
- "%06ld.%06d %s::%s: MHI in error state! MHI Status: 0x%x\n"
- "%06ld.%06d %s::%s: MHI reset complete, MHICTRL: 0x%x\n"
- "%06ld.%06d %s::%s: MHI reset procedure failed!\n"
- "%06ld.%06d %s::%s: MSI registration failed, index: %u\n"
- "%06ld.%06d %s::%s: Map / Prepare shared memory failed: 0x%llx\n"
- "%06ld.%06d %s::%s: No MHI capability regiter found!\n"
- "%06ld.%06d %s::%s: No MHIChannel\n"
- "%06ld.%06d %s::%s: Registration for domain %u already exists\n"
- "%06ld.%06d %s::%s: Shared mem pa: 0x%llx, mem desc pa: %p\n"
- "%06ld.%06d %s::%s: Starting timer: New expiry: %llu, timeout: %llu\n"
- "%06ld.%06d %s::%s: Time capability addr: %p\n"
- "%06ld.%06d %s::%s: Time capability not present\n"
- "%06ld.%06d %s::%s: Time event call back registration is NULL\n"
- "%06ld.%06d %s::%s: Time sync completion unit: %u, time: %llu, domain: %u, seq: %u\n"
- "%06ld.%06d %s::%s: Time sync is not supported\n"
- "%06ld.%06d %s::%s: Time sync not supported\n"
- "%06ld.%06d %s::%s: Total shared ER count: %u\n"
- "%06ld.%06d %s::%s: Triggering MSI index: %u, failed ret: 0x%llx\n"
- "%06ld.%06d %s::%s: Unexpected Time sync completion unit, unit: %u\n"
- "%06ld.%06d %s::%s: Unmapping region Id: %u, buffer addr: %p\n"
- "%06ld.%06d %s::%s: Unsupported time domain for device wake assertion\n"
- "%06ld.%06d %s::%s: Using exclusive timer workloop\n"
- "%06ld.%06d %s::%s: _commandContext %p, _commandContextPa 0x%llx\n"
- "%06ld.%06d %s::%s: _commandRing va 0x%llx, pa 0x%llx, size %u\n"
- "%06ld.%06d %s::%s: _commandSetting._doorbellSetting time %llu, threshold %u\n"
- "%06ld.%06d %s::%s: _eventRing[%d] va 0x%llx, pa 0x%llx, size %u\n"
- "%06ld.%06d %s::%s: _eventSetting[%d] _intmod %d, _doorbellSetting time %llu, threshold %u, sync %u\n"
- "%06ld.%06d %s::%s: _mapBase 0x%llx, _mapLimit 0x%llx\n"
- "%06ld.%06d %s::%s: _msiRange[%d]: low %d, high %d\n"
- "%06ld.%06d %s::%s: _numChannelContext %u, _channelContext %p, _channelContextPa 0x%llx\n"
- "%06ld.%06d %s::%s: _numEventContext %u, _eventContext %p, _eventContextPa 0x%llx\n"
- "%06ld.%06d %s::%s: _numEvents %d\n"
- "%06ld.%06d %s::%s: _numHWEvents: %u, NUMHWER (from device): %d\n"
- "%06ld.%06d %s::%s: _numMSI %d\n"
- "%06ld.%06d %s::%s: _shadowChannelDoorbell[%u] 0x%llx\n"
- "%06ld.%06d %s::%s: _shadowCommandDoorbell 0x%llx\n"
- "%06ld.%06d %s::%s: _shadowEventDoorbell[%u] 0x%llx\n"
- "%06ld.%06d %s::%s: abort client io completion\n"
- "%06ld.%06d %s::%s: adjusted memSize %llu\n"
- "%06ld.%06d %s::%s: alignment %u\n"
- "%06ld.%06d %s::%s: allocate memory pool for %u\n"
- "%06ld.%06d %s::%s: applying device wake 0x%x\n"
- "%06ld.%06d %s::%s: assert %d, vote 0x%x, deviceWakeCurrent 0x%x _deviceWake 0x%x\n"
- "%06ld.%06d %s::%s: assert: %u, vote: 0x%08x\n"
- "%06ld.%06d %s::%s: bar0 0x%llx (+0x%x)\n"
- "%06ld.%06d %s::%s: bar1 0x%llx (+0x%x)\n"
- "%06ld.%06d %s::%s: bhi attach/start device failed %p\n"
- "%06ld.%06d %s::%s: bhi attach/start interface failed %p\n"
- "%06ld.%06d %s::%s: can't access device wake -- the doorbell is unavailable\n"
- "%06ld.%06d %s::%s: can't access device wake -- the link is not up\n"
- "%06ld.%06d %s::%s: capability count: %u, next cap: 0x%p\n"
- "%06ld.%06d %s::%s: cf %p, intervalUs %llu, arg0 %p, arg1 %p\n"
- "%06ld.%06d %s::%s: chID: %u, type: 0x%x, res2: 0x%x, allFlags: 0x%lx\n"
- "%06ld.%06d %s::%s: change M-state %d -> %d\n"
- "%06ld.%06d %s::%s: channel %u, instance %p, ring physical address 0x%llx\n"
- "%06ld.%06d %s::%s: channel count %d\n"
- "%06ld.%06d %s::%s: channelMemoryAllocInfo._pa 0x%llx\n"
- "%06ld.%06d %s::%s: channelMemoryAllocInfo._size %llu\n"
- "%06ld.%06d %s::%s: channelMemoryAllocInfo._va 0x%llx\n"
- "%06ld.%06d %s::%s: chipset_name: %s\n"
- "%06ld.%06d %s::%s: commandSleep (THREAD_INTERRUPTIBLE) woke with reason 0x%x\n"
- "%06ld.%06d %s::%s: control %p\n"
- "%06ld.%06d %s::%s: could not allocate _memoryPoolArray\n"
- "%06ld.%06d %s::%s: cre %p\n"
- "%06ld.%06d %s::%s: create %u, type %u\n"
- "%06ld.%06d %s::%s: direction invalid\n"
- "%06ld.%06d %s::%s: dmaCmd %p\n"
- "%06ld.%06d %s::%s: domain: %u, seq: %u, fullSeq: 0x%lx, mach continuous_begin: %llu\n"
- "%06ld.%06d %s::%s: done processing event rings\n"
- "%06ld.%06d %s::%s: duplicate send image\n"
- "%06ld.%06d %s::%s: error type %u, arg0 %p, arg1 %p\n"
- "%06ld.%06d %s::%s: event index out of range\n"
- "%06ld.%06d %s::%s: execution environment for current interfaces is %d. BB is changing to %d\n"
- "%06ld.%06d %s::%s: failed readBytes %llu, size %llu\n"
- "%06ld.%06d %s::%s: failed to alloc dma command\n"
- "%06ld.%06d %s::%s: failed to allocate _interface\n"
- "%06ld.%06d %s::%s: failed to allocate async call lock\n"
- "%06ld.%06d %s::%s: failed to allocate commandGate\n"
- "%06ld.%06d %s::%s: failed to allocate io pool\n"
- "%06ld.%06d %s::%s: failed to allocate lock\n"
- "%06ld.%06d %s::%s: failed to allocate memory\n"
- "%06ld.%06d %s::%s: failed to allocate memory for channels\n"
- "%06ld.%06d %s::%s: failed to allocate memory pool of size %d\n"
- "%06ld.%06d %s::%s: failed to allocate request pool\n"
- "%06ld.%06d %s::%s: failed to allocate resources for async completion\n"
- "%06ld.%06d %s::%s: failed to allocate timer\n"
- "%06ld.%06d %s::%s: failed to allocate timer commandGate\n"
- "%06ld.%06d %s::%s: failed to allocate timer workloop\n"
- "%06ld.%06d %s::%s: failed to allocate timesync event source\n"
- "%06ld.%06d %s::%s: failed to create bhi device\n"
- "%06ld.%06d %s::%s: failed to create bhi interface\n"
- "%06ld.%06d %s::%s: failed to create mhi device\n"
- "%06ld.%06d %s::%s: failed to create mhi interface\n"
- "%06ld.%06d %s::%s: failed to create pools\n"
- "%06ld.%06d %s::%s: failed to gen DMA address: 0x%x, numSeg %u, len %llu\n"
- "%06ld.%06d %s::%s: failed to get bhi offset\n"
- "%06ld.%06d %s::%s: failed to map memory in dart\n"
- "%06ld.%06d %s::%s: failed to map result buffer\n"
- "%06ld.%06d %s::%s: failed to prepare for DMA: 0x%x\n"
- "%06ld.%06d %s::%s: failed to prepare image 0x%x\n"
- "%06ld.%06d %s::%s: failed to prepare memory: 0x%x\n"
- "%06ld.%06d %s::%s: failed to read CHDBOFF\n"
- "%06ld.%06d %s::%s: failed to read ERDBOFF\n"
- "%06ld.%06d %s::%s: failed to read MHICFG\n"
- "%06ld.%06d %s::%s: failed to read MHISTATUS\n"
- "%06ld.%06d %s::%s: failed to read MHIVER\n"
- "%06ld.%06d %s::%s: failed to read capability register\n"
- "%06ld.%06d %s::%s: failed to read capability register offset\n"
- "%06ld.%06d %s::%s: failed to read execution environment\n"
- "%06ld.%06d %s::%s: failed to read getMHICTRL\n"
- "%06ld.%06d %s::%s: failed to read memory pool array object\n"
- "%06ld.%06d %s::%s: failed to setup channel %p\n"
- "%06ld.%06d %s::%s: failed to setup command ring\n"
- "%06ld.%06d %s::%s: failed to setup context\n"
- "%06ld.%06d %s::%s: failed to setup device\n"
- "%06ld.%06d %s::%s: failed to setup device %p\n"
- "%06ld.%06d %s::%s: failed to setup event ring\n"
- "%06ld.%06d %s::%s: forClient %p, options 0x%08x, inGate %u\n"
- "%06ld.%06d %s::%s: force: %u\n"
- "%06ld.%06d %s::%s: from %s -> %s\n"
- "%06ld.%06d %s::%s: fullSeq: 0x%lx\n"
- "%06ld.%06d %s::%s: got completion for deregistered channel %u\n"
- "%06ld.%06d %s::%s: hit %u, doorbell: %u\n"
- "%06ld.%06d %s::%s: ignore m1 entry\n"
- "%06ld.%06d %s::%s: imageSize = %llu\n"
- "%06ld.%06d %s::%s: image[%u] pa 0x%llx\n"
- "%06ld.%06d %s::%s: img %p\n"
- "%06ld.%06d %s::%s: in sleep, ignore\n"
- "%06ld.%06d %s::%s: incorrect alignment\n"
- "%06ld.%06d %s::%s: index %u\n"
- "%06ld.%06d %s::%s: index %u, ccid %u, cookie: 0x%lx, size %u, code %u, last %u\n"
- "%06ld.%06d %s::%s: index %u, command %u, seq %u, reliable %u\n"
- "%06ld.%06d %s::%s: index %u, ere %p, type %u\n"
- "%06ld.%06d %s::%s: index %u, pa 0x%llx, size %u, code %u\n"
- "%06ld.%06d %s::%s: index %u, write physical address 0x%llx\n"
- "%06ld.%06d %s::%s: index out of range\n"
- "%06ld.%06d %s::%s: initializing device wake to %s\n"
- "%06ld.%06d %s::%s: interface is inactive\n"
- "%06ld.%06d %s::%s: interval %llu\n"
- "%06ld.%06d %s::%s: interval in us %llu, time mode %u\n"
- "%06ld.%06d %s::%s: intfIdx %lu\n"
- "%06ld.%06d %s::%s: link state already up\n"
- "%06ld.%06d %s::%s: link state: %u, bailing!\n"
- "%06ld.%06d %s::%s: linkState %u\n"
- "%06ld.%06d %s::%s: looking for next cap at: 0x%p, offset (from bar0): %u\n"
- "%06ld.%06d %s::%s: memSize %llu\n"
- "%06ld.%06d %s::%s: memSize = %llu\n"
- "%06ld.%06d %s::%s: memory is not page aligned\n"
- "%06ld.%06d %s::%s: memory size is not page aligned\n"
- "%06ld.%06d %s::%s: mhi attach/start device failed %p\n"
- "%06ld.%06d %s::%s: mhi attach/start interface failed %p\n"
- "%06ld.%06d %s::%s: mhi state: %u\n"
- "%06ld.%06d %s::%s: msi in unexpected state %u\n"
- "%06ld.%06d %s::%s: msi index out of range\n"
- "%06ld.%06d %s::%s: msi index range overrun\n"
- "%06ld.%06d %s::%s: msi index: %u\n"
- "%06ld.%06d %s::%s: msi range malformed\n"
- "%06ld.%06d %s::%s: nothing to do here... bailing.\n"
- "%06ld.%06d %s::%s: numChannelContext (%u) greater than supported by device %d\n"
- "%06ld.%06d %s::%s: numEvents (%u) greater than supported by device %d\n"
- "%06ld.%06d %s::%s: numHWChannelContext (%u) greater than supported by device %d\n"
- "%06ld.%06d %s::%s: numHWEvents (%u) greater than supported by device %d\n"
- "%06ld.%06d %s::%s: options 0x%08x\n"
- "%06ld.%06d %s::%s: pa 0x%llx\n"
- "%06ld.%06d %s::%s: pa 0x%llx, completion code %u\n"
- "%06ld.%06d %s::%s: pcie reset seperation workaround needed in ROM!\n"
- "%06ld.%06d %s::%s: polling for MHICTRL.RESET to be 0, MHICTRL: 0x%x\n"
- "%06ld.%06d %s::%s: pool needs to be atleast of dart page size %u\n"
- "%06ld.%06d %s::%s: provider %p, options 0x%08x\n"
- "%06ld.%06d %s::%s: provider %p, options 0x%08x, defer %p\n"
- "%06ld.%06d %s::%s: read %u, buffer %p, size %u\n"
- "%06ld.%06d %s::%s: region %u does not exist\n"
- "%06ld.%06d %s::%s: region Id: %u\n"
- "%06ld.%06d %s::%s: register %u, buff %p, size %u\n"
- "%06ld.%06d %s::%s: register time event callback failed, ret: 0x%08x\n"
- "%06ld.%06d %s::%s: res = 0x%x, code %u, size = %u\n"
- "%06ld.%06d %s::%s: res = 0x%x, size = %llu, cookie %p\n"
- "%06ld.%06d %s::%s: ring %d, 0x%llx\n"
- "%06ld.%06d %s::%s: ring %d, not aligned to %u\n"
- "%06ld.%06d %s::%s: ring %d, not large enough %u\n"
- "%06ld.%06d %s::%s: ring 0x%llx\n"
- "%06ld.%06d %s::%s: ring not aligned to %u\n"
- "%06ld.%06d %s::%s: ring not large enough %u\n"
- "%06ld.%06d %s::%s: shared mem region Id: %u, already present, client needs to it unmap first!\n"
- "%06ld.%06d %s::%s: size %u\n"
- "%06ld.%06d %s::%s: skip doorbell flush %u, pa 0x%llx\n"
- "%06ld.%06d %s::%s: status %u, dbg1 0x%x, dbg2 0x%x, dbg3 0x%x, errCode %u\n"
- "%06ld.%06d %s::%s: stopping memory pool for %llu\n"
- "%06ld.%06d %s::%s: super::start failed\n"
- "%06ld.%06d %s::%s: t %u, arg0 %p, arg1 %p\n"
- "%06ld.%06d %s::%s: there are more event rings than context array can hold\n"
- "%06ld.%06d %s::%s: time config: addr: 0x%p, 0x%lx\n"
- "%06ld.%06d %s::%s: time sync -> doorbell num: %u, event num: %u\n"
- "%06ld.%06d %s::%s: timerMode %u, arg1 %p\n"
- "%06ld.%06d %s::%s: to %s\n"
- "%06ld.%06d %s::%s: unable to allocate _cacheChannelRP array\n"
- "%06ld.%06d %s::%s: unable to allocate _channel instance array\n"
- "%06ld.%06d %s::%s: unable to allocate _msiRange\n"
- "%06ld.%06d %s::%s: unable to allocate _shadowChannelDoorbell array\n"
- "%06ld.%06d %s::%s: unable to allocate _shadowEventDoorbell array\n"
- "%06ld.%06d %s::%s: unexpected memory pool array object entry %u\n"
- "%06ld.%06d %s::%s: unexpected msi %d\n"
- "%06ld.%06d %s::%s: unexpected register read request\n"
- "%06ld.%06d %s::%s: unexpected size\n"
- "%06ld.%06d %s::%s: va 0x%llx\n"
- "%06ld.%06d %s::%s: version 0x%08x, expected 0x%08x\n"
- "%06ld.%06d %s::%s: will process event rings %d to %d\n"
- "1211111212221212121111111111111111111111221221222211111111112222"
- "12111122111"
- "AppleBasebandPCIMAVControl::%s: failed to create/init a reporter\n"
- "AppleBasebandPCIMAVControl::%s: failed to start reporting\n"
- "AppleBasebandPCIMAVControlReporter"
- "AppleBasebandPCIMAVControlReporter::%s: Failed to retrieve Device Descriptor\n"
- "abortChannel"
- "abortChannelGated"
- "abortChannels"
- "allocateChannelMemory"
- "allocateDeviceMemory"
- "asserted"
- "assignChannelMemory"
- "asyncCallCountUpdate"
- "asyncCompletion"
- "asyncFunction"
- "attach"
- "callAsync"
- "cancelAsync"
- "cancelImage"
- "cancelTimer"
- "changeState"
- "changeToM1"
- "checkCompletedIO"
- "checkIndexMSIRange"
- "checkPendingCommand"
- "checkPendingIO"
- "close"
- "closeGated"
- "coalescedTransferCompletion"
- "commandCompletion"
- "completeIO"
- "completeSharedEventIO"
- "computeChannelMemory"
- "computeDeviceMemory"
- "createDeviceFunction"
- "createPools"
- "createSetupChannel"
- "createSetupControl"
- "createSetupDevice"
- "createSetupInterface"
- "createSetupInterfaces"
- "deRegisterChannel"
- "deasserted"
- "deregisterTimeEventCallback"
- "detach"
- "deviceAlive"
- "deviceWake"
- "deviceWakeAsync"
- "device_wake assert vote"
- "device_wake deassert vote"
- "device_wake off"
- "device_wake on"
- "didTerminate"
- "engage"
- "enterError"
- "enterErrorCompletion"
- "enterLowPower"
- "errorFunction"
- "execEnvChangeFunction"
- "execEnvironmentChange"
- "exitLowPower"
- "findTimeCapability"
- "finishImageCommand"
- "finishMemoryCommand"
- "free"
- "getChannelMSIConfig"
- "getChannelProperties"
- "getDesiredLinkSpeed"
- "getReporterInterfaceNames"
- "initWithInfo"
- "initialize"
- "initializeDeviceWakeDoorbell"
- "invokeAsync"
- "ioCompletion"
- "ioTransfer"
- "linkDown"
- "linkRecovery"
- "linkUp"
- "mStateChangeFunction"
- "mapAckComplete_block_invoke"
- "mapSharedMemory"
- "mapSharedMemory_block_invoke"
- "mapUnmapMessageComplete"
- "mhiReset"
- "mhiResetDone"
- "msiInterrupt"
- "notifyError"
- "open"
- "openGated"
- "performTimeSync"
- "prepareImageCommand"
- "prepareMemoryCommand"
- "prepareTimeSync"
- "printChannelParams"
- "printDeviceParams"
- "processCurrentCommand"
- "processERE"
- "processTRE"
- "queueCommand"
- "queueTransfer"
- "read"
- "readExecutionEnvironment"
- "readGated"
- "readRegister"
- "readRegisterGated"
- "recoveryCheck"
- "registerChannel"
- "registerTimeEventCallback"
- "resetChannel"
- "resetChannelComplete"
- "rscIOCompletion"
- "scanCheck"
- "sendCommand"
- "sendImage"
- "sendImageCompletion"
- "sendImageCompletionGated"
- "sendImageGated"
- "sendMapUnmapMessage"
- "sendTransfer"
- "setDevice"
- "setUpTimeConfig"
- "setupChannel"
- "setupCommandRing"
- "setupContext"
- "setupController"
- "setupDevice"
- "setupDeviceParams"
- "setupEventRing"
- "setupMapUnmapCompletion"
- "setupTransferRing"
- "shadowDBCheckFunction_block_invoke"
- "shadowDBFunction_block_invoke"
- "shadowDoorbell"
- "shadowDoorbellCheck"
- "shadowDoorbellFlush"
- "shadowDoorbellProcess"
- "site.AppleBasebandPCIMAVControlReporter"
- "start"
- "startChannel"
- "startChannelComplete"
- "startChannelGated"
- "startChannels"
- "startCheck"
- "startTimer"
- "stateTransition"
- "stop"
- "stopChannel"
- "stopChannelComplete"
- "synchronousFunction"
- "teardownChannel"
- "teardownController"
- "teardownDevice"
- "teardownPools"
- "terminate"
- "terminateDevice"
- "terminateInterface"
- "terminateInterfaces"
- "terminate_block_invoke"
- "timeDomainToDeviceWakeVote"
- "timeSync"
- "timeSyncCompletion"
- "timeSyncEventCallback"
- "timeSync_block_invoke"
- "timer"
- "timerCompletion"
- "timerFunction_block_invoke"
- "transferCompletion"
- "triggerAsync"
- "triggerMSIFunction"
- "triggerRecovery"
- "unmapAckComplete_block_invoke"
- "unmapSharedMemory"
- "unmapSharedMemory_block_invoke"
- "willTerminate"
- "write"
- "writeGated"
- "~ABPBHIChannel"
- "~ABPBHIDevice"
- "~ABPMHIChannel"
- "~ABPMHIDevice"

```

>  `com.apple.driver.AppleSPU`

```diff

-1014.0.4.0.0
+1014.0.5.0.0
   __TEXT.__cstring: 0x5aae
   __TEXT.__os_log: 0x955
   __TEXT.__const: 0x358
-  __TEXT_EXEC.__text: 0x498e8
+  __TEXT_EXEC.__text: 0x498dc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x878
   __DATA.__common: 0x970

```

>  `com.apple.iokit.IODisplayPortFamily`

```diff

-730.0.4.0.0
+730.0.5.0.0
   __TEXT.__cstring: 0x7c47
   __TEXT.__os_log: 0x9571
   __TEXT.__const: 0x310
-  __TEXT_EXEC.__text: 0x5d094
+  __TEXT_EXEC.__text: 0x5d118
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x550

   __DATA_CONST.__got: 0x170
   __DATA_CONST.__mod_init_func: 0x110
   __DATA_CONST.__mod_term_func: 0x108
-  __DATA_CONST.__const: 0xf880
+  __DATA_CONST.__const: 0xf888
   __DATA_CONST.__kalloc_type: 0x840
   __DATA_CONST.__kalloc_var: 0x280
   Functions: 1961

```

>  `com.apple.kernel`

```diff

-11215.0.199.502.1
-  __TEXT.__const: 0x33b60
+11215.2.5.0.0
+  __TEXT.__const: 0x33ba0
   __TEXT.__copyio_vectors: 0xf0
-  __TEXT.__cstring: 0x6bbc8
-  __TEXT.__os_log: 0x26d59
+  __TEXT.__cstring: 0x6bab4
+  __TEXT.__os_log: 0x26c98
   __TEXT.__eh_frame: 0x610
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x2c0
-  __DATA_CONST.__const: 0xa2328
+  __DATA_CONST.__const: 0xa2378
   __DATA_CONST.__hib_const: 0x120
   __DATA_CONST.__kalloc_type: 0x13340
   __DATA_CONST.__kalloc_var: 0x78f0
   __DATA_CONST.__brk_desc: 0x78
   __DATA_SPTM.__const: 0x3c000
   __TEXT_EXEC.__hib_text: 0xc68
-  __TEXT_EXEC.__text: 0x7fdf60
+  __TEXT_EXEC.__text: 0x7bccfc
   __TEXT_BOOT_EXEC.__bootcode: 0x4cd8
   __KLD.__text: 0x1644
   __LASTDATA_CONST.__mod_init_func: 0x8

   __DATA.__lock_grp: 0x57a8
   __DATA.__percpu: 0x6e48
   __DATA.__common: 0x58508
-  __DATA.__bss: 0x3f7c0
+  __DATA.__bss: 0x3f778
   __BOOTDATA.__data: 0x18000
-  __BOOTDATA.__init_entry_set: 0x10788
+  __BOOTDATA.__init_entry_set: 0x107b8
   __BOOTDATA.__init: 0x5b058
   __PRELINK_TEXT.__text: 0x0
   __PRELINK_INFO.__info: 0x0

   __PLK_DATA_CONST.__data: 0x0
   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
-  __LINKINFO.__symbolsets: 0x4537a
+  __LINKINFO.__symbolsets: 0x45532
   __LATE_CONST.__late_const: 0xa8
-  Functions: 19841
+  Functions: 19804
   Symbols:   0
-  CStrings:  16812
+  CStrings:  16803
 
CStrings:
+ "B16@?0^{task={lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}{os_refcnt=AI}BBBBIIQ^{_vm_map}{queue_entry=^{queue_entry}^{queue_entry}}^{task_watchports}^v{queue_entry=^{queue_entry}^{queue_entry}}^{restartable_ranges}^{processor_set}^{affinity_space}iIiiissiQ{recount_task=^{recount_track}^{recount_usage}}{lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}[4^{ipc_port}]^{ipc_port}[14{exception_action=^{ipc_port}iiii^{label}}]{hardened_exception_action={exception_action=^{ipc_port}iiii^{label}}II}^{ipc_port}^{ipc_port}^{ipc_port}^{ipc_port}^{ipc_port}[3^{ipc_port}]^^{ipc_port}^{ipc_space}^{ledger}{queue_entry=^{queue_entry}^{queue_entry}}iI^vQQCACQQiBBB^Q^Q^Q^Q^QIIIIII^{proc_ro}^{kcdata_descriptor}Q{queue_entry=^{queue_entry}^{queue_entry}}^{label}IIQQIBBBBb4b4b4b4CCCCB*^{vm_shared_region}QQQ^{thread_call}{queue_entry=^{queue_entry}^{queue_entry}}ii^{bank_task}^{ipc_importance_task}{vm_extmod_statistics=qqqqqq}{task_requested_policy=b1b1b2b2b1b1b2b1b3b3b3b1b5b3b3b1b3b1b1b3b1b3b1b1b17}{task_effective_policy=b1b1b2b1b1b1b2b1b1b3b3b1b1b1b4b1b1b1b3b3b1b1b29}{task_pend_token=(?={?=b1b1b1b1b1b1b1b1b1b1b1b1b1}I)}b1b1b1b1b1b27b1b1b1b1b28^{io_stat_info}{task_writes_counters=QQQQ}{task_writes_counters=QQQQ}{_cpu_time_qos_stats=QQQQQQQ}{_cpu_time_qos_stats=QQQQQQQ}IIQCCCiii{queue_entry=^{queue_entry}^{queue_entry}}{lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}b16b1b1b1b1b1b1b1[2^{coalition}][2{queue_entry=^{queue_entry}^{queue_entry}}]QCCCCIQ{queue_entry=^{queue_entry}^{queue_entry}}{queue_entry=^{queue_entry}^{queue_entry}}iIQ[16C]Q^{_vmobject_list_output_}Q^{vm_deferred_reclamation_metadata_s}}8"
+ "com.apple.developer.media-device-discovery-extension"
+ "drop_loopback_count"
+ "site.u_int8_t *"
+ "task_apt_token"
- "!IN6_IS_ADDR_MULTICAST(&ip6->ip6_dst)"
- "%s: %s (process %s:%u) priority %u entry_count 0\n"
- "%s:%d esp kpipe input, ipversion %u, SPI=%x"
- "%s:%d esp kpipe input, output buffer is short(%u), compared to input buffer(%u) SPI=%x\n"
- "(sb->sb_flags & SB_LOCK) == 0"
- "B16@?0^{task={lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}{os_refcnt=AI}BBBBIIQ^{_vm_map}{queue_entry=^{queue_entry}^{queue_entry}}^{task_watchports}^v{queue_entry=^{queue_entry}^{queue_entry}}^{restartable_ranges}^{processor_set}^{affinity_space}iIiiissiQ{recount_task=^{recount_track}^{recount_usage}}{lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}[4^{ipc_port}]^{ipc_port}[14{exception_action=^{ipc_port}iiii^{label}}]{hardened_exception_action={exception_action=^{ipc_port}iiii^{label}}II}^{ipc_port}^{ipc_port}^{ipc_port}^{ipc_port}^{ipc_port}[3^{ipc_port}]^^{ipc_port}^{ipc_space}^{ledger}{queue_entry=^{queue_entry}^{queue_entry}}iI^vQQCACQQiBB^Q^Q^Q^Q^QIIIIII^{proc_ro}^{kcdata_descriptor}Q{queue_entry=^{queue_entry}^{queue_entry}}^{label}IIQQIBBBBb4b4b4b4CCCCB*^{vm_shared_region}QQQ^{thread_call}{queue_entry=^{queue_entry}^{queue_entry}}ii^{bank_task}^{ipc_importance_task}{vm_extmod_statistics=qqqqqq}{task_requested_policy=b1b1b2b2b1b1b2b1b3b3b3b1b5b3b3b1b3b1b1b3b1b3b1b1b17}{task_effective_policy=b1b1b2b1b1b1b2b1b1b3b3b1b1b1b4b1b1b1b3b3b1b1b29}{task_pend_token=(?={?=b1b1b1b1b1b1b1b1b1b1b1b1b1}I)}b1b1b1b1b1b27b1b1b1b1b28^{io_stat_info}{task_writes_counters=QQQQ}{task_writes_counters=QQQQ}{_cpu_time_qos_stats=QQQQQQQ}{_cpu_time_qos_stats=QQQQQQQ}IIQCCCiii{queue_entry=^{queue_entry}^{queue_entry}}{lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}b16b1b1b1b1b1b1b1[2^{coalition}][2{queue_entry=^{queue_entry}^{queue_entry}}]QCCCCIQ{queue_entry=^{queue_entry}^{queue_entry}}{queue_entry=^{queue_entry}^{queue_entry}}iIQ[16C]Q^{_vmobject_list_output_}Q^{vm_deferred_reclamation_metadata_s}}8"
- "IS_P2ALIGNED(ccp, CHANNEL_CACHE_ALIGN_MAX)"
- "authentication failed in IPv6 AH input: %s %s\n"
- "ndopts == NULL in nd6_option @%s:%d"
- "ndopts->nd_opts_last >= ndopts->nd_opts_search"
- "necp_get_tlv_at_offset buffer is NULL"
- "rt_key(rt)->sa_family == AF_INET"
- "site.u_int8_t * __attribute__((__indexable__))"
- "src.s_addr != INADDR_ANY"

```

>  `com.apple.security.sandbox`

```diff

-2401.0.60.0.0
-  __TEXT.__const: 0x1893f9
-  __TEXT.__cstring: 0x6edf
+2401.0.65.0.0
+  __TEXT.__const: 0x1890d9
+  __TEXT.__cstring: 0x6efc
   __TEXT.__os_log: 0x2029
   __TEXT_EXEC.__text: 0x30494
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA.__bss: 0x144c8
   __DATA_CONST.__auth_got: 0x838
   __DATA_CONST.__got: 0xc8
-  __DATA_CONST.__const: 0x3640
+  __DATA_CONST.__const: 0x3650
   __DATA_CONST.__kalloc_var: 0x550
   __DATA_CONST.__kalloc_type: 0xa80
   Functions: 648
   Symbols:   0
-  CStrings:  1295
+  CStrings:  1296
 
CStrings:
+ "/private/var/db/darwindaemon"

```

>  `com.apple.driver.AppleDCPDPTXProxy`

```diff

-311.0.16.0.0
+311.0.17.0.0
   __TEXT.__const: 0x48
   __TEXT.__cstring: 0x1007
   __TEXT.__os_log: 0xa0c
-  __TEXT_EXEC.__text: 0x84c0
+  __TEXT_EXEC.__text: 0x8518
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0xd8
-  __DATA_CONST.__auth_got: 0x1b0
+  __DATA_CONST.__auth_got: 0x1b8
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__mod_init_func: 0x28
   __DATA_CONST.__mod_term_func: 0x28
-  __DATA_CONST.__const: 0x2b38
+  __DATA_CONST.__const: 0x2b50
   __DATA_CONST.__kalloc_type: 0x140
-  Functions: 281
+  Functions: 282
   Symbols:   0
   CStrings:  198
 

```

>  `com.apple.driver.AppleM2ScalerCSCDriver`

```diff

-148.0.50.0.0
-  __TEXT.__cstring: 0x165e9
-  __TEXT.__const: 0x4ecb8
-  __TEXT_EXEC.__text: 0xd6130
+148.0.53.0.0
+  __TEXT.__cstring: 0x1673a
+  __TEXT.__const: 0x4ecc8
+  __TEXT_EXEC.__text: 0xd5ff8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x1fe40
   __DATA.__common: 0x20a8

   __DATA_CONST.__const: 0x210b8
   __DATA_CONST.__kalloc_type: 0x3c40
   __DATA_CONST.__kalloc_var: 0x500
-  Functions: 6008
+  Functions: 6012
   Symbols:   0
-  CStrings:  2384
+  CStrings:  2392
 
CStrings:
+ "1222222222212111111112111111111111111111122122112212"
+ "1222222222212111111112111111111111111111122122112212112222222"
+ "12222222222121111111121111111111111111111221221122121122222221111111221111111111111111111122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222000020000000"
+ "Awake"
+ "SleepAcked"
+ "SleepRequested"
+ "[IOSA][Boot ] Req 0x%x Resumption on MSR%d\n"
+ "[IOSA][Boot ] Req 0x%x Waiting for MSR%d wake\n"
+ "[IOSA][Boot ] [MSR%u] SleepState transition from %s to %s\n"
+ "[IOSA][Boot ] kConfigKeyIsShippedDevice=%d\n"
+ "activateForMapping_gated"
+ "commandSleep failed with %d\n"
+ "powerRefCount cannot be zero with kSPSSleepAcked. [MSR%d] partition %d newState %d oldState %d refCount %d"
- "     req %d prio %d ctx_sw_cnt %d\n"
- "122222222221211111111211111111111111111112212211221"
- "122222222221211111111211111111111111111112212211221112222222"
- "12222222222121111111121111111111111111111221221122111222222211111112211111111111111111111222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222220000020000000"
- "canContextSwitch"

```

>  `com.apple.driver.RTBuddy`

```diff

-618.0.5.0.0
+618.0.7.0.0
   __TEXT.__cstring: 0x947e
   __TEXT.__const: 0x278
-  __TEXT_EXEC.__text: 0x3f918
+  __TEXT_EXEC.__text: 0x3f970
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x128
   __DATA.__common: 0xb20
CStrings:
+ "03:08:48"
+ "Aug  8 2024"
- "20:48:46"
- "Jul 30 2024"

```

>  `com.apple.filesystems.apfs`

```diff

-2313.0.4.0.7
+2313.2.1.0.0
   __TEXT.__const: 0x790
-  __TEXT.__cstring: 0x4854d
-  __TEXT_EXEC.__text: 0x139de0
+  __TEXT.__cstring: 0x48545
+  __TEXT_EXEC.__text: 0x139de4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x690
   __DATA.__bss: 0xc60
CStrings:
+ "00:56:37"
+ "2024/08/08"
+ "2313.2.1"
+ "Aug  8 2024"
+ "apfs-2313.2.1"
- "2024/07/30"
- "20:38:21"
- "2313.0.4.0.7"
- "Jul 30 2024"
- "apfs-2313.0.4.0.7"

```

>  `com.apple.driver.AppleAVE2`

```diff

-802.97.1.0.0
+803.16.2.0.0
   __TEXT.__const: 0x2e8e0
-  __TEXT.__cstring: 0x350f8
-  __TEXT.__os_log: 0x40038
-  __TEXT_EXEC.__text: 0x142720
+  __TEXT.__cstring: 0x35356
+  __TEXT.__os_log: 0x4029b
+  __TEXT_EXEC.__text: 0x143a50
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x290
   __DATA.__common: 0x130

   __DATA_CONST.__mod_term_func: 0x38
   __DATA_CONST.__const: 0x62c8
   __DATA_CONST.__kalloc_type: 0x1fc0
-  __DATA_CONST.__kalloc_var: 0x1040
-  Functions: 2472
+  __DATA_CONST.__kalloc_var: 0xfa0
+  Functions: 2481
   Symbols:   0
-  CStrings:  6936
+  CStrings:  6958
 
CStrings:
+ "%lld %d AVE %s: %s total commands in client stages %p | %d %d | %d | %d"
+ "%lld %d AVE %s: %s total commands in client stages %p | %d %d | %d | %d\n"
+ "%lld %d AVE %s: %s:%d SKIP %p %d %lld | %p %d %lld 0x%x %lld | %p %d %lld 0x%x %lld"
+ "%lld %d AVE %s: %s:%d SKIP %p %d %lld | %p %d %lld 0x%x %lld | %p %d %lld 0x%x %lld\n"
+ "%lld %d AVE %s: %s::%s:%d %p %d | <Info> %p %d"
+ "%lld %d AVE %s: %s::%s:%d %p %d | <Info> %p %d\n"
+ "%lld %d AVE %s: %s::%s:%d %p %lld %p %d | %p %d %lld 0x%x %lld"
+ "%lld %d AVE %s: %s::%s:%d %p %lld %p %d | %p %d %lld 0x%x %lld\n"
+ "%lld %d AVE %s: %s::%s:%d %p %lld | %p %d %lld %d %lld | RefCnt %d pNewCmd %p"
+ "%lld %d AVE %s: %s::%s:%d %p %lld | %p %d %lld %d %lld | RefCnt %d pNewCmd %p\n"
+ "%lld %d AVE %s: %s::%s:%d %s | fail to initialize FPS %p %d %d %d.%03d %d.%03d %d %d %d %d"
+ "%lld %d AVE %s: %s::%s:%d %s | fail to initialize FPS %p %d %d %d.%03d %d.%03d %d %d %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | fail to update FPS %p %d %d %d.%03d %d.%03d %d %d %d %d"
+ "%lld %d AVE %s: %s::%s:%d %s | fail to update FPS %p %d %d %d.%03d %d.%03d %d %d %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to create external timer %p %p"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to create external timer %p %p\n"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to create mutex for external timer %p"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to create mutex for external timer %p\n"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to get External Timer %p %p"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to get External Timer %p %p\n"
+ "%lld %d AVE %s: %s::%s:%d SKIP %p %d %lld | %p %d %lld 0x%x %lld"
+ "%lld %d AVE %s: %s::%s:%d SKIP %p %d %lld | %p %d %lld 0x%x %lld\n"
+ "%lld %d AVE %s: %s::%s:%d WP buffer pool abnormal %p %d %d"
+ "%lld %d AVE %s: %s::%s:%d WP buffer pool abnormal %p %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d frame drop %p %d %p %d"
+ "%lld %d AVE %s: %s::%s:%d frame drop %p %d %p %d\n"
+ "%lld %d AVE %s: %s::%s:%d invalid command %p %d | %p %d %p %d | %d"
+ "%lld %d AVE %s: %s::%s:%d invalid command %p %d | %p %d %p %d | %d\n"
+ "%lld %d AVE %s: %s::%s:%d unpaired frame %p %d | %p %d %p %d | %p %lld | %p %d %d"
+ "%lld %d AVE %s: %s::%s:%d unpaired frame %p %d | %p %d %p %d | %p %lld | %p %d %d\n"
+ "%lld %d AVE %s: HierMode: %d"
+ "%lld %d AVE %s: HierMode: %d\n"
+ "%s total commands in client stages %p | %d %d | %d | %d"
+ "%s total commands in client stages %p | %d %d | %d | %d\n"
+ "03:55:38"
+ "1211111111111222212112222211111111111111111111111121222221"
+ "1211111212221212112111211122"
+ "803.16.2"
+ "AVE_LookAhead_GOPDecision_Flush"
+ "Aug  8 2024"
+ "HandleCmd"
+ "HierMode: %d"
+ "HierMode: %d\n"
+ "HwC DrainAll"
+ "HwC DrainData"
+ "ProcExtTimerHandler"
+ "ProcessReadyCmd"
+ "SwC DrainAll"
+ "SwC DrainData"
+ "m_pExtTimerMutex != nullptr"
+ "m_pcExtTimer != nullptr"
+ "m_psExtTimer != nullptr"
+ "pClientList != nullptr && piaThreshold != nullptr && iNum == 2"
+ "schedMode == 0 && euNum == 1 && piPrevEUID != nullptr"
- "%lld %d AVE %s: %s total commands in client stages %p | %d %d | %d"
- "%lld %d AVE %s: %s total commands in client stages %p | %d %d | %d\n"
- "%lld %d AVE %s: %s:%d frame drop"
- "%lld %d AVE %s: %s:%d frame drop\n"
- "%lld %d AVE %s: %s::%s:%d %p %d | <WPParam> %p | <Info> %p %d"
- "%lld %d AVE %s: %s::%s:%d %p %d | <WPParam> %p | <Info> %p %d\n"
- "%lld %d AVE %s: %s::%s:%d %p %lld | %p %d %lld %d %lld| RefCnt %d pNewCmd %p"
- "%lld %d AVE %s: %s::%s:%d %p %lld | %p %d %lld %d %lld| RefCnt %d pNewCmd %p\n"
- "%lld %d AVE %s: %s::%s:%d %s | fail to initialize FPS %p %d %d %d.%03d %d.%03d %d %d %d"
- "%lld %d AVE %s: %s::%s:%d %s | fail to initialize FPS %p %d %d %d.%03d %d.%03d %d %d %d\n"
- "%lld %d AVE %s: %s::%s:%d %s | fail to update FPS %p %d %d %d.%03d %d.%03d %d %d %d"
- "%lld %d AVE %s: %s::%s:%d %s | fail to update FPS %p %d %d %d.%03d %d.%03d %d %d %d\n"
- "%lld %d AVE %s: %s::%s:%d %s | failed to get buffer from buffer pool %p %d %p %d %d %d"
- "%lld %d AVE %s: %s::%s:%d %s | failed to get buffer from buffer pool %p %d %p %d %d %d\n"
- "%lld %d AVE %s: %s::%s:%d %s | failed to handle commands %p %lld %p %d 0x%x 0x%x %d %d"
- "%lld %d AVE %s: %s::%s:%d %s | failed to handle commands %p %lld %p %d 0x%x 0x%x %d %d\n"
- "%lld %d AVE %s: %s::%s:%d receive command done %p %d"
- "%lld %d AVE %s: %s::%s:%d receive command done %p %d\n"
- "%s total commands in client stages %p | %d %d | %d"
- "%s total commands in client stages %p | %d %d | %d\n"
- "%s::%s"
- "12111111111112222112222211111111111111111111111121222221"
- "12111112122212121121211122"
- "20:53:07"
- "802.97.1"
- "Jul 30 2024"
- "ProcesOutputCmd_Done"
- "ProcesOutputCmd_Drop"
- "ProcesOutputCmd_Skip"
- "pClientList != nullptr && iThreshold != nullptr && iNum == 2"
- "ret >= 0"
- "schedMode == 0 && euNum == 1 && iPrevCoreID != nullptr"

```

>  `com.apple.driver.AppleBasebandPCIMAVPDP`

```diff

 810.0.0.0.0
   __TEXT.__const: 0x128
-  __TEXT.__cstring: 0x4bd1
-  __TEXT_EXEC.__text: 0x2456c
+  __TEXT.__cstring: 0xcf4
+  __TEXT_EXEC.__text: 0xbf90
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x128
   __DATA.__bss: 0xb0
-  __DATA_CONST.__auth_got: 0x2d8
-  __DATA_CONST.__got: 0x80
+  __DATA_CONST.__auth_got: 0x2b8
+  __DATA_CONST.__got: 0x70
   __DATA_CONST.__mod_init_func: 0x70
   __DATA_CONST.__mod_term_func: 0x38
-  __DATA_CONST.__const: 0x3818
+  __DATA_CONST.__const: 0x3810
   __DATA_CONST.__kalloc_type: 0x400
-  Functions: 363
+  Functions: 364
   Symbols:   0
-  CStrings:  362
+  CStrings:  52
 
CStrings:
+ "1211111212221212111111112111112111111111111121121121121111211211111212222"
+ "12111112122212121111211122222221211111222221212"
+ "12111112122212121212111111111111111111111222222222222222222222222222222222221111111111111111111111111111111111111111111111111111111111111111111111222222222222222221111121122222222221111111111111111222122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222111111111111111111111111111111112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211111111111111112222"
+ "12111112122212121212111111111111111111111222222222222222222222222222222222221111111111111111111111111111111111111111111111111111111111111111111111222222222222222221111121122222222222222222222222212212112"
+ "121111121222121212121111111111111111111112222222222222222222222222222222222211111111111111111111111111111111111111111111111111111111111111111111112222222222222222211111211222222222222222222222222122121121"
- "%06ld.%06d %s::%s: \n"
- "%06ld.%06d %s::%s: %s: --> \n"
- "%06ld.%06d %s::%s: %u commands, pdp:packets: 0:%u 1:%u 2:%u 3:%u 4:%u 5:%u 6:%u 7:%u\n"
- "%06ld.%06d %s::%s: -- Done.\n"
- "%06ld.%06d %s::%s: -- done!\n"
- "%06ld.%06d %s::%s: --done\n"
- "%06ld.%06d %s::%s: Adding Tx pkt meta data failed with 0x%08x\n"
- "%06ld.%06d %s::%s: Avail data indication -- qmap hdr 0x%08x\n"
- "%06ld.%06d %s::%s: Avail data indication raw data 0x%08x %08x %08x %08x\n"
- "%06ld.%06d %s::%s: Avail data timer expired, but interface was closed\n"
- "%06ld.%06d %s::%s: Available data is non-zero, bytes: %u\n"
- "%06ld.%06d %s::%s: Bad DL dump (offset=%llu, remain=%llu)\n"
- "%06ld.%06d %s::%s: Bad RSC header\n"
- "%06ld.%06d %s::%s: Bearer already mapped to Default Service\n"
- "%06ld.%06d %s::%s: Bearer already mapped to Low Latency Service\n"
- "%06ld.%06d %s::%s: Bearer switch already pending, ownerID: %u, bearerID: %u\n"
- "%06ld.%06d %s::%s: Bearer switch complete !\n"
- "%06ld.%06d %s::%s: Bearer switch in progress\n"
- "%06ld.%06d %s::%s: Bearer switch notify!\n"
- "%06ld.%06d %s::%s: Bearer switch request for ownerID: %u, bearer ID: %u, req type: %u\n"
- "%06ld.%06d %s::%s: BearerID: %u not present for OwnerID: %u"
- "%06ld.%06d %s::%s: Blocking outgoing traffic due to IP appender (unit number %u)\n"
- "%06ld.%06d %s::%s: Cmd header: name 0x%02x: type 0x%02x: reserved 0x%04x: trans_id 0x%08x\n"
- "%06ld.%06d %s::%s: Command response raw data 0x%08x %08x %08x %08x %08x\n"
- "%06ld.%06d %s::%s: Creating interface: pdp_qctun\n"
- "%06ld.%06d %s::%s: DFC End Marker Ack already pending for ownerID: %u\n"
- "%06ld.%06d %s::%s: DFC End Marker command invalid length %u\n"
- "%06ld.%06d %s::%s: DFC End Marker command raw data 0x%08x %08x %08x\n"
- "%06ld.%06d %s::%s: DFC Info Query response raw data 0x%08x %08x\n"
- "%06ld.%06d %s::%s: DFC Info query -- qmap hdr 0x%08x\n"
- "%06ld.%06d %s::%s: DFC Info query -- qmap hdr 0x%08x %08x\n"
- "%06ld.%06d %s::%s: DFC Info query for bearer ID: %u, ownerID: %u\n"
- "%06ld.%06d %s::%s: DFC Info query raw data 0x%08x\n"
- "%06ld.%06d %s::%s: DFC Query info response invalid length %u\n"
- "%06ld.%06d %s::%s: DFC notify command invalid length %u\n"
- "%06ld.%06d %s::%s: DFC notify command raw data 0x%08x %08x %08x\n"
- "%06ld.%06d %s::%s: DFC power save mode ack not received!\n"
- "%06ld.%06d %s::%s: DFC_INFO_QUERY response, ignore query response for inactive bearer ownerID: %u, bearer ID: %u, credits: %u\n"
- "%06ld.%06d %s::%s: DFC_INFO_QUERY response, ignore query response for unmapped bearer ownerID: %u, bearer ID: %u, credits: %u\n"
- "%06ld.%06d %s::%s: DL packet dump\n"
- "%06ld.%06d %s::%s: DL packet dump (offset=%llu, length=%u, remain=%llu)\n"
- "%06ld.%06d %s::%s: Data powersave mode command -- qmap hdr 0x%08x\n"
- "%06ld.%06d %s::%s: Data powersave mode command raw data 0x%08x %08x %08x %08x %08x\n"
- "%06ld.%06d %s::%s: Deferring Ack for DFC End Marker\n"
- "%06ld.%06d %s::%s: Delete _CreditsQueue entries for intf: %u\n"
- "%06ld.%06d %s::%s: Duplicate / redundant bearer removed notification for bearerID: %u, ownerID: %u, seq num: %u\n"
- "%06ld.%06d %s::%s: Duplicate DFC_NOTIFY command for bearerID: %u, ownerID: %u, seq num: %u\n"
- "%06ld.%06d %s::%s: Error detected on Modem - removing bearerID: %u\n"
- "%06ld.%06d %s::%s: Failed to create matching dictionary\n"
- "%06ld.%06d %s::%s: Flushing pci service's stage queue pkts to queue set, packetCnt: %u\n"
- "%06ld.%06d %s::%s: Got reset bearers marker: %u for this interface\n"
- "%06ld.%06d %s::%s: Hdr Size:%u interface %u, pkt size %u, padding %u\n"
- "%06ld.%06d %s::%s: IP Appender failed with 0x%08x\n"
- "%06ld.%06d %s::%s: Incorrect bearer mapping state, ownerID: %u, bearerID: %u, current mapped owner: %u\n"
- "%06ld.%06d %s::%s: Inserting at HEAD\n"
- "%06ld.%06d %s::%s: Inserting at Tail\n"
- "%06ld.%06d %s::%s: Inserting before ownerID: %u, bearer ID: %u, credits: %u,\n"
- "%06ld.%06d %s::%s: Interface advisory report: owner %u: payload bytes %u\n"
- "%06ld.%06d %s::%s: Invalid NL pair data length, expected: %u, actual: %u\n"
- "%06ld.%06d %s::%s: Invalid bearer status : %u\n"
- "%06ld.%06d %s::%s: Invalid bearer status: %u, for bearer ID: %u\n"
- "%06ld.%06d %s::%s: Invalid bearer switch request type, req type: %u\n"
- "%06ld.%06d %s::%s: Invalid chksm\n"
- "%06ld.%06d %s::%s: Invalid intf number: %u!\n"
- "%06ld.%06d %s::%s: Invalid number of NLs, received: %u, max: %u\n"
- "%06ld.%06d %s::%s: Invalid number of bearers: %u\n"
- "%06ld.%06d %s::%s: Invalid ownerID : %u\n"
- "%06ld.%06d %s::%s: Invalid ownerID: %u\n"
- "%06ld.%06d %s::%s: Invalid ownerID: %u, bearerID: %u already mapped to ownerID: %u\n"
- "%06ld.%06d %s::%s: Invalid request type: %u\n"
- "%06ld.%06d %s::%s: LL Bearer Switch Ack raw data 0x%08x %08x\n"
- "%06ld.%06d %s::%s: LL Bearer Switch Request Ack invalid length %u != (Header + Payload) size: %u\n"
- "%06ld.%06d %s::%s: LL Bearer Switch Request Ack invalid length %u < Header Size: %u\n"
- "%06ld.%06d %s::%s: LL Bearer Switch Status command, invalid length %u != (Header + Payload) size: %u\n"
- "%06ld.%06d %s::%s: LL Bearer Switch Status raw data 0x%08x %08x\n"
- "%06ld.%06d %s::%s: LQM report: owner %u: payload bytes %u\n"
- "%06ld.%06d %s::%s: NL pair data len (%u), exceeded max len\n"
- "%06ld.%06d %s::%s: NL[%u](Length: %u, chksum map: 0x%x, NumPkts: %u)\n"
- "%06ld.%06d %s::%s: NULL owner!\n"
- "%06ld.%06d %s::%s: No UL pkts queued for ownerID: %u\n"
- "%06ld.%06d %s::%s: No bearer present for this OwnerID: %u\n"
- "%06ld.%06d %s::%s: No bearer present for this ownerID: %u\n"
- "%06ld.%06d %s::%s: No credit update for owner: %u\n"
- "%06ld.%06d %s::%s: PCIe link is down or is going down\n"
- "%06ld.%06d %s::%s: Packet txid: %u, Expected txid: %u\n"
- "%06ld.%06d %s::%s: Packet type is not QMAP control! \n"
- "%06ld.%06d %s::%s: Packet: %p, Txid: %u\n"
- "%06ld.%06d %s::%s: Preparing response: %s\n"
- "%06ld.%06d %s::%s: Previous tail entry - ownerID: %u, bearer ID: %u, credits: %u,\n"
- "%06ld.%06d %s::%s: RSC service: %u\n"
- "%06ld.%06d %s::%s: Received DFC_END_MARKER for ownerID: %u, bearer ID: %u, seqNum: %u\n"
- "%06ld.%06d %s::%s: Received DFC_INFO_QUERY response for ownerID: %u, bearer ID: %u, credits: %u\n"
- "%06ld.%06d %s::%s: Received DFC_NOTIFY for ownerID: %u, bearer ID: %u, credits: %u, seq num: %u, bearer status: %u\n"
- "%06ld.%06d %s::%s: Redundant bearer removed notificaiton, bearer ID: %u already removed\n"
- "%06ld.%06d %s::%s: Removing bearer failed!\n"
- "%06ld.%06d %s::%s: Request Bearer Switch -- qmap cmd hdr 0x%08x %08x\n"
- "%06ld.%06d %s::%s: Request Bearer Switch -- qmap hdr 0x%08x\n"
- "%06ld.%06d %s::%s: Request Bearer Switch raw data 0x%08x %08x\n"
- "%06ld.%06d %s::%s: Sending DFC End Marker Ack for ownerID: %u\n"
- "%06ld.%06d %s::%s: Setting packet buffer base / limit failed: 0x%llx\n"
- "%06ld.%06d %s::%s: Start --\n"
- "%06ld.%06d %s::%s: Start, options 0x%08x --\n"
- "%06ld.%06d %s::%s: Stop queueing pkts - DFC end marker / UL flow switched!\n"
- "%06ld.%06d %s::%s: Tcp Ack Allowed: %u\n"
- "%06ld.%06d %s::%s: Temp failure in switching bearer ID: %u\n"
- "%06ld.%06d %s::%s: Trigger DFC End Marker Ack\n"
- "%06ld.%06d %s::%s: UL packet dump\n"
- "%06ld.%06d %s::%s: Unexpected - bearer info entry is NULL!\n"
- "%06ld.%06d %s::%s: Unexpected Tx\n"
- "%06ld.%06d %s::%s: Unexpected command in RSC channel\n"
- "%06ld.%06d %s::%s: Unexpected control packet for out of band Qmap control service\n"
- "%06ld.%06d %s::%s: Unexpected next header for RSC\n"
- "%06ld.%06d %s::%s: Unexpected pci service ID: %u\n"
- "%06ld.%06d %s::%s: Unknown or unhandled command, name: %u\n"
- "%06ld.%06d %s::%s: Unmapping bearerID: %u from OwnerID: %u\n"
- "%06ld.%06d %s::%s: Unsupported status\n"
- "%06ld.%06d %s::%s: Updated credits for ownerID: %u, credits remaining: %u\n"
- "%06ld.%06d %s::%s: [%u] bearerID: %u, credits: %u\n"
- "%06ld.%06d %s::%s: _rxHEAD: %p, _rxTail: %p\n"
- "%06ld.%06d %s::%s: allowed Tx bytes: %u\n"
- "%06ld.%06d %s::%s: bad command packet size: %u\n"
- "%06ld.%06d %s::%s: bad length %u for link status report payload\n"
- "%06ld.%06d %s::%s: bearer switch ack, bearer ID: %u, status: %u\n"
- "%06ld.%06d %s::%s: bearer switch status, bearer ID: %u, status: %u\n"
- "%06ld.%06d %s::%s: bearer switch was not pending! bearer ID: %u, \n"
- "%06ld.%06d %s::%s: bearer switch was not successful! bearer ID: %u, \n"
- "%06ld.%06d %s::%s: bearer switch was not successful! bearer ID: %u, status: %u \n"
- "%06ld.%06d %s::%s: bytesRead (%llu) != header (%lu) + body (%u)\n"
- "%06ld.%06d %s::%s: cache max reached, dropping packet\n"
- "%06ld.%06d %s::%s: cannot receive interface advisory report for nonexisting owner %u\n"
- "%06ld.%06d %s::%s: cannot receive link status report for nonexisting owner %u\n"
- "%06ld.%06d %s::%s: chain length = %u\n"
- "%06ld.%06d %s::%s: chain length = %u, txid 0x%u --> 0x%u, total DL data %u bytes\n"
- "%06ld.%06d %s::%s: cksmValid: %u, numNLs: %u, incIPID: %u\n"
- "%06ld.%06d %s::%s: close called on an unopened client %p\n"
- "%06ld.%06d %s::%s: closeVal: %u, closeType: %u, contextID: %u\n"
- "%06ld.%06d %s::%s: cmd header: name 0x%02x: type 0x%02x: reserved 0x%04x: trans_id 0x%08x\n"
- "%06ld.%06d %s::%s: cmd version: %u\n"
- "%06ld.%06d %s::%s: command header raw data: 0x%08x 0x%08x\n"
- "%06ld.%06d %s::%s: command name: %u\n"
- "%06ld.%06d %s::%s: consumed:%u\n"
- "%06ld.%06d %s::%s: count %u\n"
- "%06ld.%06d %s::%s: count %u, telescoping limit %u\n"
- "%06ld.%06d %s::%s: count: %u\n"
- "%06ld.%06d %s::%s: dealloc packet %p directly\n"
- "%06ld.%06d %s::%s: device: %p, stateNumber: %lu\n"
- "%06ld.%06d %s::%s: disable soft flow control for pdp_ip%u due to %u pending write bytes\n"
- "%06ld.%06d %s::%s: disabling flow control due to QMAP command\n"
- "%06ld.%06d %s::%s: draining pci service's stage queue pkts to queue set, packetCnt: %u\n"
- "%06ld.%06d %s::%s: duplicate QMAP extension header type (%u)\n"
- "%06ld.%06d %s::%s: enabling flow control due to QMAP command\n"
- "%06ld.%06d %s::%s: enabling flow control for pdp_ip%u due to %u pending Tx bytes\n"
- "%06ld.%06d %s::%s: error 0x%08x\n"
- "%06ld.%06d %s::%s: failed to clone packet\n"
- "%06ld.%06d %s::%s: failed to create Available data zero indication timer\n"
- "%06ld.%06d %s::%s: failed to create Rx queue\n"
- "%06ld.%06d %s::%s: failed to create Tx completion queue\n"
- "%06ld.%06d %s::%s: failed to create Tx queue\n"
- "%06ld.%06d %s::%s: failed to create power save mode timer\n"
- "%06ld.%06d %s::%s: failed to open provider\n"
- "%06ld.%06d %s::%s: failed to set packet limits: 0x%08x\n"
- "%06ld.%06d %s::%s: flow control %s: owner %u: ipFamily %u: sequence 0x%04x: QoS 0x%08x\n"
- "%06ld.%06d %s::%s: flow control command invalid IP family %u\n"
- "%06ld.%06d %s::%s: flow control command invalid length %u\n"
- "%06ld.%06d %s::%s: flow control command raw data 0x%08x %08x\n"
- "%06ld.%06d %s::%s: flow control disable sequence number mismatch (got %u, expected %u)\n"
- "%06ld.%06d %s::%s: flow controlling bearerID: %u, ownerID: %u\n"
- "%06ld.%06d %s::%s: found client, unit %u\n"
- "%06ld.%06d %s::%s: free count: %u\n"
- "%06ld.%06d %s::%s: interface %u not opened yet, packet will be queued\n"
- "%06ld.%06d %s::%s: interface %u, size %u, padding %u, command %u\n"
- "%06ld.%06d %s::%s: interface 0x%p not found\n"
- "%06ld.%06d %s::%s: interface down\n"
- "%06ld.%06d %s::%s: intf %p, count %u\n"
- "%06ld.%06d %s::%s: intf number: %u, open: %u, owner = %p\n"
- "%06ld.%06d %s::%s: invalid interface %d\n"
- "%06ld.%06d %s::%s: invalid length for LQM command, length: %u\n"
- "%06ld.%06d %s::%s: invalid null header\n"
- "%06ld.%06d %s::%s: invoked with packetCount = 0\n"
- "%06ld.%06d %s::%s: kOffPowerState\n"
- "%06ld.%06d %s::%s: kOffPowerState, enable data powersave mode, allow notification: %u\n"
- "%06ld.%06d %s::%s: kOnPowerState, disable data powersave mode\n"
- "%06ld.%06d %s::%s: konPowerState\n"
- "%06ld.%06d %s::%s: last queued pkt completed, trigger DFC end marker Ack for %u\n"
- "%06ld.%06d %s::%s: link status report: owner %u: payload bytes %u\n"
- "%06ld.%06d %s::%s: low latency service: %u\n"
- "%06ld.%06d %s::%s: null header\n"
- "%06ld.%06d %s::%s: out of band QMAP control: %u\n"
- "%06ld.%06d %s::%s: oversize header (%u < %u)\n"
- "%06ld.%06d %s::%s: oversize header (%u < %zu)\n"
- "%06ld.%06d %s::%s: owner %u does not exist, processing command anyway\n"
- "%06ld.%06d %s::%s: owner: %u is inactive\n"
- "%06ld.%06d %s::%s: owner: %u is not active\n"
- "%06ld.%06d %s::%s: owner: %u is not opened yet\n"
- "%06ld.%06d %s::%s: ownerID: %u\n"
- "%06ld.%06d %s::%s: ownerID: %u has no bearer info entry for bearerID: %u\n"
- "%06ld.%06d %s::%s: ownerID: %u was previously flow controlled, updated credits: %u\n"
- "%06ld.%06d %s::%s: ownerID: %u, avail data bytes: %u\n"
- "%06ld.%06d %s::%s: ownerID: %u, bearerID: %u, Active -> Removed\n"
- "%06ld.%06d %s::%s: ownerID: %u, bearerID: %u, Inactive -> Active\n"
- "%06ld.%06d %s::%s: ownerID: %u, bearerID: %u, curr bearer state: %u, new status: %u\n"
- "%06ld.%06d %s::%s: ownerID: %u, bearerID: %u, switchStatus: %u\n"
- "%06ld.%06d %s::%s: ownerID: %u, credits queue...\n"
- "%06ld.%06d %s::%s: packet 0x%p, count: %u\n"
- "%06ld.%06d %s::%s: packet: %p, TxID: %u\n"
- "%06ld.%06d %s::%s: packet: %p, TxID: %u, next TxID: %u, count: %u\n"
- "%06ld.%06d %s::%s: pad bytes (%u) is >= total length (%u)\n"
- "%06ld.%06d %s::%s: pci service not available\n"
- "%06ld.%06d %s::%s: pciService not available\n"
- "%06ld.%06d %s::%s: pdp:packets: 0:%u 1:%u 2:%u 3:%u 4:%u 5:%u 6:%u 7:%u\n"
- "%06ld.%06d %s::%s: pdp_ip%u flow controlled, but continue until soft flow control is enabled\n"
- "%06ld.%06d %s::%s: qmap_control_service not present in plist\n"
- "%06ld.%06d %s::%s: read size too small: %llu\n"
- "%06ld.%06d %s::%s: received ack for Data Powersave Mode Control command\n"
- "%06ld.%06d %s::%s: redundant flow control disable command for owner %u\n"
- "%06ld.%06d %s::%s: redundant flow control enable command for owner %u\n"
- "%06ld.%06d %s::%s: refCon 0x%p, status 0x%x\n"
- "%06ld.%06d %s::%s: refcon: %p, status 0x%x\n"
- "%06ld.%06d %s::%s: refcon: %p, status 0x%x, enqueue: %u\n"
- "%06ld.%06d %s::%s: registering callback for ownerID: %u\n"
- "%06ld.%06d %s::%s: requesting upto: %llu usecs to PM\n"
- "%06ld.%06d %s::%s: residue (%llu) < header (%lu) + body (%u)\n"
- "%06ld.%06d %s::%s: returning free space: %u, service id: %u\n"
- "%06ld.%06d %s::%s: sending data powersave mode, ownerID: %u, enable: %u\n"
- "%06ld.%06d %s::%s: sending response...\n"
- "%06ld.%06d %s::%s: sending response: %s\n"
- "%06ld.%06d %s::%s: sent bytes: %u\n"
- "%06ld.%06d %s::%s: sent bytes: %u, pkt cnt: %u\n"
- "%06ld.%06d %s::%s: setting %u msecs timer\n"
- "%06ld.%06d %s::%s: skipping disable powersave mode, first power on\n"
- "%06ld.%06d %s::%s: soft flow control active on pdp_ip%u\n"
- "%06ld.%06d %s::%s: staged: %u\n"
- "%06ld.%06d %s::%s: super::handleOpen() failed\n!"
- "%06ld.%06d %s::%s: super::open failed\n"
- "%06ld.%06d %s::%s: too many packets in transfer (limit %u), dropping packet\n"
- "%06ld.%06d %s::%s: transfer size %u, interface %u, txid %u\n"
- "%06ld.%06d %s::%s: txid 0x%08x: status 0x%x, packet 0x%p\n"
- "%06ld.%06d %s::%s: txid 0x%x\n"
- "%06ld.%06d %s::%s: unable to get unsent bytes: 0x%x\n"
- "%06ld.%06d %s::%s: unexpected command type %u\n"
- "%06ld.%06d %s::%s: unexpected command type: %u\n"
- "%06ld.%06d %s::%s: unit number %u invalid or nonexistent\n"
- "%06ld.%06d %s::%s: unrecognized QMAP extension header type (%u)\n"
- "%06ld.%06d %s::%s: unsupported command: name 0x%02x: type %u: transactionID 0x%08x\n"
- "%06ld.%06d %s::%s: unsupported flow control QoS 0x%08x\n"
- "%06ld.%06d %s::%s: updating bearer credits failed!\n"
- "%06ld.%06d %s::%s: updating owners in QMAP control intf failed\n"
- "%06ld.%06d %s::%s: waiting for Low Latency service\n"
- "%06ld.%06d %s::%s: waiting for QMAP control service\n"
- "%06ld.%06d %s::%s: waiting for RSC service\n"
- "12111112122212121111111121111121111111111111121121121121111211211111212222"
- "121111121222121211112111222222212111112222212121"
- "121111121222121212121111111111111111111111222222222222222222222222222222222221111111111111111111111111111111111111111111111111111111111111111111111222222222222222221111121122222222221111111111111111222122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222111111111111111111111111111111112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211111111111111112222"
- "121111121222121212121111111111111111111111222222222222222222222222222222222221111111111111111111111111111111111111111111111111111111111111111111111222222222222222221111121122222222222222222222222212212112"
- "1211111212221212121211111111111111111111112222222222222222222222222222222222211111111111111111111111111111111111111111111111111111111111111111111112222222222222222211111211222222222222222222222222122121121"
- "addTxPktMetaData"
- "allocQueues"
- "availDataZeroTimerCompletion"
- "bearerSwitchComplete_block_invoke"
- "closeGated"
- "commandResponse"
- "commandResponse_block_invoke"
- "createRxSubmissionQueue"
- "decodeQMAPHeader"
- "decodeQMAPRSCHeader"
- "disable"
- "discardRxPacket"
- "dumpOwnerCreditsQueue"
- "enable"
- "flowControlAllBearers"
- "free"
- "getAvailData"
- "getOwnerCredits_block_invoke"
- "handleOpen"
- "initWithOptions"
- "openGated"
- "outputComplete"
- "powerSaveModeTimerCompletion"
- "powerStateWillChangeTo"
- "powerStateWillChangeTo_block_invoke"
- "processBearerCreditsGated"
- "processCtrlPacket"
- "processDFCEndMarker"
- "processDFCInfoQuery"
- "processDFCLLSwitchRequest"
- "processDFCLLSwitchStatus"
- "processDFCNotify"
- "processDFCPowerSaveMode"
- "processMavExtCmdAdvisoryReport"
- "processMavExtCmdLQM"
- "queryFlowControlCredits_block_invoke"
- "queryFreeULSpace"
- "queueRxBuffersGated"
- "readComplete"
- "registerBearerSwitchCallback"
- "requestBearerSwitchGated"
- "requestTxGated"
- "resetOwnerCreditsQueue"
- "rxQueueCallbackGated"
- "sendAvailDataIndication_block_invoke"
- "sendDFCEndMarkerAck_block_invoke"
- "sendDataPowerSaveMode_block_invoke"
- "setBearerSwitchPending_block_invoke"
- "setInterfaceOwnerGated"
- "setPowerStateGated"
- "start"
- "terminate"
- "triggerBearerSwitch_block_invoke"
- "triggerRxDequeue_block_invoke"
- "txCompletionCallbackGated"
- "txQueueCallbackGated"
- "updateOwnerCreditsGated_block_invoke"
- "usesQmapControlService"
- "willTerminate"
- "willTerminate_block_invoke"

```

</details>

### KDKs

- [KDK DIFF](KDK.md)

## MachO

### 🆕 NEW (18)

- `/System/Library/Accounts/DataclassOwners/Bookmarks.bundle/Bookmarks`
- `/System/Library/ControlCenter/Bundles/BluetoothModule.bundle/BluetoothModule`
- `/System/Library/ExtensionKit/Extensions/GPUExtension.appex/com.apple.WebKit.GPU`
- `/System/Library/ExtensionKit/Extensions/NetworkingExtension.appex/com.apple.WebKit.Networking`
- `/System/Library/ExtensionKit/Extensions/WebContentCaptivePortalExtension.appex/com.apple.WebKit.WebContent.CaptivePortal`
- `/System/Library/ExtensionKit/Extensions/WebContentExtension.appex/com.apple.WebKit.WebContent`
- `/System/Library/Frameworks/CoreSpotlight.framework/PlugIns/CoreSpotlightTestImporter.appex/CoreSpotlightTestImporter`
- `/System/Library/Frameworks/CoreSpotlight.framework/PlugIns/CoreSpotlightTextImporter.appex/CoreSpotlightTextImporter`
- `/System/Library/Frameworks/FinanceKit.framework/XPCServices/FinanceImageProcessingService.xpc/FinanceImageProcessingService`
- `/System/Library/Frameworks/SafariServices.framework/PlugIns/SafariServices.wkbundle/SafariServices`
- `/System/Library/Frameworks/SafariServices.framework/XPCServices/com.apple.SafariServices.ContentBlockerLoader.xpc/com.apple.SafariServices.ContentBlockerLoader`
- `/System/Library/Frameworks/WebKit.framework/Daemons/adattributiond`
- `/System/Library/PrivateFrameworks/PlugInKitDaemon.framework/PlugInKitDaemon`
- `/System/Library/PrivateFrameworks/SafariFoundation.framework/XPCServices/AutoFillHelper.xpc/AutoFillHelper`
- `/System/Library/PrivateFrameworks/SafariFoundation.framework/XPCServices/CredentialProviderExtensionHelper.xpc/CredentialProviderExtensionHelper`
- `/System/Library/PrivateFrameworks/SafariFoundation.framework/XPCServices/SafariConfigurationSubscriber.xpc/SafariConfigurationSubscriber`
- `/System/Library/PrivateFrameworks/SafariShared.framework/XPCServices/com.apple.Safari.SearchHelper.xpc/com.apple.Safari.SearchHelper`
- `/System/Library/PrivateFrameworks/VisualTestKit.framework/VisualTestKit`

### ❌ Removed (3)

- `/System/Library/ExtensionKit/Extensions/FinanceImageProcessingExtension.appex/FinanceImageProcessingExtension`
- `/System/Library/Frameworks/CoreSpotlight.framework/PlugIns/CoreSpotlightImportExtension1_iOS.appex/CoreSpotlightImportExtension1_iOS`
- `/System/Library/Frameworks/CoreSpotlight.framework/PlugIns/CoreSpotlightImportExtension2_iOS.appex/CoreSpotlightImportExtension2_iOS`

### ⬆️ Updated (499)

<details>
  <summary><i>View Updated</i></summary>

- [/Applications/AccessorySetupUI.app/AccessorySetupUI](MACHOS/AccessorySetupUI.md)
- [/Applications/ActivityMessagesApp.app/PlugIns/ActivityMessagesExtension.appex/ActivityMessagesExtension](MACHOS/ActivityMessagesExtension.md)
- [/Applications/ActivityProgressUI.app/ActivityProgressUI](MACHOS/ActivityProgressUI.md)
- [/Applications/AirDropUI.app/AirDropUI](MACHOS/AirDropUI.md)
- [/Applications/AirPlayReceiver.app/AirPlayReceiver](MACHOS/AirPlayReceiver.md)
- [/Applications/AnimojiStickers.app/PlugIns/AnimojiStickersExtension.appex/AnimojiStickersExtension](MACHOS/AnimojiStickersExtension.md)
- [/Applications/AppDistributionLaunchAngel.app/AppDistributionLaunchAngel](MACHOS/AppDistributionLaunchAngel.md)
- [/Applications/AppStore.app/AppStore](MACHOS/AppStore.md)
- [/Applications/AppStore.app/PlugIns/AppStoreWidgetsExtension.appex/AppStoreWidgetsExtension](MACHOS/AppStoreWidgetsExtension.md)
- [/Applications/AppStore.app/PlugIns/ProductPageExtension.appex/ProductPageExtension](MACHOS/ProductPageExtension.md)
- [/Applications/AppStore.app/PlugIns/SubscribePageExtension.appex/SubscribePageExtension](MACHOS/SubscribePageExtension.md)
- [/Applications/AskPermissionUI.app/AskPermissionUI](MACHOS/AskPermissionUI.md)
- [/Applications/AutoSettings.app/AutoSettings](MACHOS/AutoSettings.md)
- [/Applications/Batteries.app/PlugIns/BatteriesAvocadoWidgetExtension.appex/BatteriesAvocadoWidgetExtension](MACHOS/BatteriesAvocadoWidgetExtension.md)
- [/Applications/Batteries.app/PlugIns/BatteriesWidgetExtension.appex/BatteriesWidgetExtension](MACHOS/BatteriesWidgetExtension.md)
- [/Applications/BusinessExtensionsWrapper.app/PlugIns/Business.appex/Business](MACHOS/Business.md)
- [/Applications/Camera.app/Camera](MACHOS/Camera.md)
- [/Applications/Camera.app/Extensions/LockScreenCamera.appex/LockScreenCamera](MACHOS/LockScreenCamera.md)
- [/Applications/Camera.app/PlugIns/LauncherControlExtension.appex/LauncherControlExtension](MACHOS/LauncherControlExtension.md)
- [/Applications/CarCamera.app/CarCamera](MACHOS/CarCamera.md)
- [/Applications/CarPlaySettings.app/CarPlaySettings](MACHOS/CarPlaySettings.md)
- [/Applications/Charge.app/Charge](MACHOS/Charge.md)
- [/Applications/ClarityCamera.app/ClarityCamera](MACHOS/ClarityCamera.md)
- [/Applications/Climate.app/Climate](MACHOS/Climate.md)
- [/Applications/ClockAngel.app/ClockAngel](MACHOS/ClockAngel.md)
- [/Applications/ColorPickerUIService.app/ColorPickerUIService](MACHOS/ColorPickerUIService.md)
- [/Applications/CoreAuthUI.app/CoreAuthUI](MACHOS/CoreAuthUI.md)
- [/Applications/Diagnostics.app/Diagnostics](MACHOS/Diagnostics.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6004.appex/Diagnostic-6004](MACHOS/Diagnostic-6004.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6007.appex/Diagnostic-6007](MACHOS/Diagnostic-6007.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6008.appex/Diagnostic-6008](MACHOS/Diagnostic-6008.md)
- [/Applications/EventViewService.app/EventViewService](MACHOS/EventViewService.md)
- [/Applications/FTMInternal-4.app/FTMInternal-4](MACHOS/FTMInternal-4.md)
- [/Applications/Family.app/PlugIns/InviteMessageBubbleExtension.appex/InviteMessageBubbleExtension](MACHOS/InviteMessageBubbleExtension.md)
- [/Applications/Feedback Assistant iOS.app/Feedback Assistant iOS](MACHOS/Feedback_Assistant_iOS.md)
- [/Applications/FinanceUIService.app/FinanceUIService](MACHOS/FinanceUIService.md)
- [/Applications/FontPickerUIService.app/FontPickerUIService](MACHOS/FontPickerUIService.md)
- [/Applications/GameOverlayUI.app/GameOverlayUI](MACHOS/GameOverlayUI.md)
- [/Applications/HDSViewService.app/HDSViewService](MACHOS/HDSViewService.md)
- [/Applications/HeadphoneProxService.app/HeadphoneProxService](MACHOS/HeadphoneProxService.md)
- [/Applications/HomeCaptiveViewService.app/HomeCaptiveViewService](MACHOS/HomeCaptiveViewService.md)
- [/Applications/HomeUIService.app/HomeUIService](MACHOS/HomeUIService.md)
- [/Applications/InCallService.app/InCallService](MACHOS/InCallService.md)
- [/Applications/InCallService.app/PlugIns/IntentsUI.appex/IntentsUI](MACHOS/IntentsUI.md)
- [/Applications/InCallService.app/PlugIns/RemotePeoplePicker.appex/RemotePeoplePicker](MACHOS/RemotePeoplePicker.md)
- [/Applications/InputUI.app/InputUI](MACHOS/InputUI.md)
- [/Applications/Jellyfish.app/PlugIns/Animoji.appex/Animoji](MACHOS/Animoji.md)
- [/Applications/LimitedAccessPromptView.app/LimitedAccessPromptView](MACHOS/LimitedAccessPromptView.md)
- [/Applications/MagnifierAngel.app/MagnifierAngel](MACHOS/MagnifierAngel.md)
- [/Applications/Media.app/Media](MACHOS/Media.md)
- [/Applications/MediaRemoteUI.app/MediaRemoteUI](MACHOS/MediaRemoteUI.md)
- [/Applications/MobilePhone.app/MobilePhone](MACHOS/MobilePhone.md)
- [/Applications/MobileSlideShow.app/MobileSlideShow](MACHOS/MobileSlideShow.md)
- [/Applications/MobileSlideShow.app/PlugIns/PhotosReliveWidget.appex/PhotosReliveWidget](MACHOS/PhotosReliveWidget.md)
- [/Applications/MomentsUIService.app/MomentsUIService](MACHOS/MomentsUIService.md)
- [/Applications/MusicRecognition.app/MusicRecognition](MACHOS/MusicRecognition.md)
- [/Applications/PCViewService.app/PCViewService](MACHOS/PCViewService.md)
- [/Applications/PassbookUIService.app/PassbookUIService](MACHOS/PassbookUIService.md)
- [/Applications/PeopleMessageService.app/PlugIns/PeopleMessagesScreenTime.appex/PeopleMessagesScreenTime](MACHOS/PeopleMessagesScreenTime.md)
- [/Applications/PeopleViewService.app/PlugIns/PeopleWidget_iOSExtension.appex/PeopleWidget_iOSExtension](MACHOS/PeopleWidget_iOSExtension.md)
- [/Applications/Preferences.app/Preferences](MACHOS/Preferences.md)
- [/Applications/PreviewShell.app/PreviewShell](MACHOS/PreviewShell.md)
- [/Applications/SOSBuddy.app/SOSBuddy](MACHOS/SOSBuddy.md)
- [/Applications/SafetyMonitorApp.app/SafetyMonitorApp](MACHOS/SafetyMonitorApp.md)
- [/Applications/Screen Time.app/PlugIns/ScreenTimeWidgetExtension.appex/ScreenTimeWidgetExtension](MACHOS/ScreenTimeWidgetExtension.md)
- [/Applications/Screen Time.app/PlugIns/ScreenTimeWidgetIntentsExtension.appex/ScreenTimeWidgetIntentsExtension](MACHOS/ScreenTimeWidgetIntentsExtension.md)
- [/Applications/ScreenContinuityShell.app/ScreenContinuityShell](MACHOS/ScreenContinuityShell.md)
- [/Applications/Setup.app/Setup](MACHOS/Setup.md)
- [/Applications/SharingViewService.app/SharingViewService](MACHOS/SharingViewService.md)
- [/Applications/ShazamEventsApp.app/ShazamEventsApp](MACHOS/ShazamEventsApp.md)
- [/Applications/ShortcutsUI.app/ShortcutsUI](MACHOS/ShortcutsUI.md)
- [/Applications/Sidecar.app/PlugIns/ContinuityDisplay.appex/ContinuityDisplay](MACHOS/ContinuityDisplay.md)
- [/Applications/Siri.app/Siri](MACHOS/Siri.md)
- [/Applications/SoftwareUpdateUIService.app/SoftwareUpdateUIService](MACHOS/SoftwareUpdateUIService.md)
- [/Applications/StickersUltra.app/PlugIns/StickersUltraExtension.appex/StickersUltraExtension](MACHOS/StickersUltraExtension.md)
- [/Applications/TDGSharingViewService.app/TDGSharingViewService](MACHOS/TDGSharingViewService.md)
- [/Applications/Trip.app/Trip](MACHOS/Trip.md)
- [/Applications/WritingToolsUIService.app/WritingToolsUIService](MACHOS/WritingToolsUIService.md)
- [/Library/Audio/Plug-Ins/HAL/VirtualAudio.plugin/VirtualAudio](MACHOS/VirtualAudio.md)
- [/System/Applications/Family/InviteMessageBubbleExtension.appex/InviteMessageBubbleExtension](MACHOS/InviteMessageBubbleExtension.md)
- [/System/Library/AccessibilityBundles/AXHapticMusicServer.axuiservice/AXHapticMusicServer](MACHOS/AXHapticMusicServer.md)
- [/System/Library/AccessibilityBundles/AXMotionCuesServer.axuiservice/AXMotionCuesServer](MACHOS/AXMotionCuesServer.md)
- [/System/Library/AccessibilityBundles/AXWatchRemoteScreenUIServer.axuiservice/AXWatchRemoteScreenUIServer](MACHOS/AXWatchRemoteScreenUIServer.md)
- [/System/Library/AccessibilityBundles/DisplayFilterUIServer.axuiservice/DisplayFilterUIServer](MACHOS/DisplayFilterUIServer.md)
- [/System/Library/AccessibilityBundles/GAXSpringboardServer.bundle/GAXSpringboardServer](MACHOS/GAXSpringboardServer.md)
- [/System/Library/AccessibilityBundles/LiveSpeechUIService.axuiservice/LiveSpeechUIService](MACHOS/LiveSpeechUIService.md)
- [/System/Library/AccessibilityBundles/VoiceOver.axuiservice/VoiceOver](MACHOS/VoiceOver.md)
- [/System/Library/Accounts/Authentication/AAGKAuthenticationPlugin.bundle/AAGKAuthenticationPlugin](MACHOS/AAGKAuthenticationPlugin.md)
- [/System/Library/Accounts/Authentication/AAIDSAuthenticationPlugin.bundle/AAIDSAuthenticationPlugin](MACHOS/AAIDSAuthenticationPlugin.md)
- [/System/Library/Accounts/DataclassOwners/CloudDocsDataclassOwnerPlugin.bundle/CloudDocsDataclassOwnerPlugin](MACHOS/CloudDocsDataclassOwnerPlugin.md)
- [/System/Library/Accounts/Notification/DeviceManagementClientAccountNotificationPlugin.bundle/DeviceManagementClientAccountNotificationPlugin](MACHOS/DeviceManagementClientAccountNotificationPlugin.md)
- [/System/Library/AppleMediaServices/DynamicUI/PlugIns/CoreDynamicUIPlugin.bundle/CoreDynamicUIPlugin](MACHOS/CoreDynamicUIPlugin.md)
- [/System/Library/AppleMediaServices/DynamicUI/PlugIns/StoreDynamicUIPlugin.bundle/StoreDynamicUIPlugin](MACHOS/StoreDynamicUIPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/AlarmFlowPlugin.bundle/AlarmFlowPlugin](MACHOS/AlarmFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/AudioFlowDelegatePlugin](MACHOS/AudioFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/CarCommandsFlowDelegatePlugin.bundle/CarCommandsFlowDelegatePlugin](MACHOS/CarCommandsFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/DailyBriefingFlowPlugin.bundle/DailyBriefingFlowPlugin](MACHOS/DailyBriefingFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/EdutainmentFlowPlugin.bundle/EdutainmentFlowPlugin](MACHOS/EdutainmentFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/EmergencyFlowPlugin.bundle/EmergencyFlowPlugin](MACHOS/EmergencyFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/SocialConversationFlowDelegatePlugin](MACHOS/SocialConversationFlowDelegatePlugin.md)
- [/System/Library/Assistant/Plugins/Maps.assistantBundle/Maps](MACHOS/Maps.md)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriPrivateLearningPatternExtractionPlugin.bundle/SiriPrivateLearningPatternExtractionPlugin](MACHOS/SiriPrivateLearningPatternExtractionPlugin.md)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriPrivateLearningTTSMispronunciationPlugin.bundle/SiriPrivateLearningTTSMispronunciationPlugin](MACHOS/SiriPrivateLearningTTSMispronunciationPlugin.md)
- [/System/Library/Assistant/UIPlugins/Maps.siriUIBundle/Maps](MACHOS/Maps.md)
- [/System/Library/Assistant/UIPlugins/RemindersSiriUIPlugin.siriUIBundle/RemindersSiriUIPlugin](MACHOS/RemindersSiriUIPlugin.md)
- [/System/Library/Audio/Plug-Ins/HAL/BTAudioHALPlugin.driver/BTAudioHALPlugin](MACHOS/BTAudioHALPlugin.md)
- [/System/Library/ControlCenter/Bundles/AudioConferenceControlCenterModule.bundle/AudioConferenceControlCenterModule](MACHOS/AudioConferenceControlCenterModule.md)
- [/System/Library/ControlCenter/Bundles/VideoConferenceControlCenterModule.bundle/VideoConferenceControlCenterModule](MACHOS/VideoConferenceControlCenterModule.md)
- [/System/Library/CoreImage/PortraitFilters.cifilter/PortraitFilters](MACHOS/PortraitFilters.md)
- [/System/Library/CoreImage/PortraitFilters.cifilter/portrait_filters_archive_bin.metallib](MACHOS/portrait_filters_archive_bin.metallib.md)
- [/System/Library/CoreImage/PortraitFilters.cifilter/portrait_filters_fullsize_archive_bin.metallib](MACHOS/portrait_filters_fullsize_archive_bin.metallib.md)
- [/System/Library/CoreServices/AccessibilityUIServer.app/AccessibilityUIServer](MACHOS/AccessibilityUIServer.md)
- [/System/Library/CoreServices/AccessibilityUIServer.app/PlugIns/AccessibilityControlsExtension.appex/AccessibilityControlsExtension](MACHOS/AccessibilityControlsExtension.md)
- [/System/Library/CoreServices/AegirProxyApp.app/PlugIns/AegirPoster.appex/AegirPoster](MACHOS/AegirPoster.md)
- [/System/Library/CoreServices/AssistiveTouch.app/assistivetouchd](MACHOS/assistivetouchd.md)
- [/System/Library/CoreServices/CarPlayTemplateUIHost.app/CarPlayTemplateUIHost](MACHOS/CarPlayTemplateUIHost.md)
- [/System/Library/CoreServices/ClarityBoard.app/ClarityBoard](MACHOS/ClarityBoard.md)
- [/System/Library/CoreServices/CommandAndControl.app/CommandAndControl](MACHOS/CommandAndControl.md)
- [/System/Library/CoreServices/IntelligentLight.app/IntelligentLight](MACHOS/IntelligentLight.md)
- [/System/Library/CoreServices/LiveTranscriptionUI.app/LiveTranscriptionUI](MACHOS/LiveTranscriptionUI.md)
- [/System/Library/CoreServices/SafariSupport.bundle/SafariBookmarksSyncAgent](MACHOS/SafariBookmarksSyncAgent.md)
- [/System/Library/CoreServices/VoiceOverTouch.app/vot](MACHOS/vot.md)
- [/System/Library/DataClassMigrators/KeyboardMigrator.migrator/KeyboardMigrator](MACHOS/KeyboardMigrator.md)
- [/System/Library/DataClassMigrators/MobileAsset.migrator/MobileAsset](MACHOS/MobileAsset.md)
- [/System/Library/DataClassMigrators/SpringBoard.migrator/SpringBoard](MACHOS/SpringBoard.md)
- [/System/Library/DistributedEvaluation/Plugins/RemindersDES.desPlugin/RemindersDES](MACHOS/RemindersDES.md)
- [/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN](MACHOS/com.apple.DriverKit-AppleBCMWLAN.md)
- [/System/Library/ExtensionKit/Extensions/ADFollowUpExtension.appex/ADFollowUpExtension](MACHOS/ADFollowUpExtension.md)
- [/System/Library/ExtensionKit/Extensions/AccessibilityControlsExtension.appex/AccessibilityControlsExtension](MACHOS/AccessibilityControlsExtension.md)
- [/System/Library/ExtensionKit/Extensions/BatterySettingsIntentsExtension.appex/BatterySettingsIntentsExtension](MACHOS/BatterySettingsIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/DeveloperSettingsIntents.appex/DeveloperSettingsIntents](MACHOS/DeveloperSettingsIntents.md)
- [/System/Library/ExtensionKit/Extensions/DisplayAndBrightnessSettingsExtension.appex/DisplayAndBrightnessSettingsExtension](MACHOS/DisplayAndBrightnessSettingsExtension.md)
- [/System/Library/ExtensionKit/Extensions/DocumentAppIntents.appex/DocumentAppIntents](MACHOS/DocumentAppIntents.md)
- [/System/Library/ExtensionKit/Extensions/EventKitUIRemoteUIExtension.appex/EventKitUIRemoteUIExtension](MACHOS/EventKitUIRemoteUIExtension.md)
- [/System/Library/ExtensionKit/Extensions/GeneralSettingsIntents.appex/GeneralSettingsIntents](MACHOS/GeneralSettingsIntents.md)
- [/System/Library/ExtensionKit/Extensions/IFTelemetrySELFIngestor.appex/IFTelemetrySELFIngestor](MACHOS/IFTelemetrySELFIngestor.md)
- [/System/Library/ExtensionKit/Extensions/IntelligenceIntentsExtension.appex/IntelligenceIntentsExtension](MACHOS/IntelligenceIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/MKRemoteUI.appex/MKRemoteUI](MACHOS/MKRemoteUI.md)
- [/System/Library/ExtensionKit/Extensions/MercuryPosterExtension.appex/MercuryPosterExtension](MACHOS/MercuryPosterExtension.md)
- [/System/Library/ExtensionKit/Extensions/MusicEngagementExtension.appex/MusicEngagementExtension](MACHOS/MusicEngagementExtension.md)
- [/System/Library/ExtensionKit/Extensions/PersonalHotspotControlExtension.appex/PersonalHotspotControlExtension](MACHOS/PersonalHotspotControlExtension.md)
- [/System/Library/ExtensionKit/Extensions/PodcastsSettingsAppIntentsExtension.appex/PodcastsSettingsAppIntentsExtension](MACHOS/PodcastsSettingsAppIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/PrivacyAppIntents.appex/PrivacyAppIntents](MACHOS/PrivacyAppIntents.md)
- [/System/Library/ExtensionKit/Extensions/SafetyCheckAppIntents.appex/SafetyCheckAppIntents](MACHOS/SafetyCheckAppIntents.md)
- [/System/Library/ExtensionKit/Extensions/SettingsSOSAppIntentsExtension.appex/SettingsSOSAppIntentsExtension](MACHOS/SettingsSOSAppIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/SoundAndHapticsControls.appex/SoundAndHapticsControls](MACHOS/SoundAndHapticsControls.md)
- [/System/Library/ExtensionKit/Extensions/TextInputAppIntentsExtension.appex/TextInputAppIntentsExtension](MACHOS/TextInputAppIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/WiFiSettingsControlsExtension.appex/WiFiSettingsControlsExtension](MACHOS/WiFiSettingsControlsExtension.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.fskit.apfs.appex/com.apple.fskit.apfs](MACHOS/com.apple.fskit.apfs.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.fskit.hfs.appex/com.apple.fskit.hfs](MACHOS/com.apple.fskit.hfs.md)
- [/System/Library/Filesystems/apfs.fs/apfs_condenser](MACHOS/apfs_condenser.md)
- [/System/Library/Filesystems/apfs.fs/apfs_vol_converter](MACHOS/apfs_vol_converter.md)
- [/System/Library/Filesystems/apfs.fs/fsck_apfs](MACHOS/fsck_apfs.md)
- [/System/Library/Filesystems/apfs.fs/newfs_apfs](MACHOS/newfs_apfs.md)
- [/System/Library/Frameworks/AssetsLibrary.framework/Support/assetsd](MACHOS/assetsd.md)
- [/System/Library/Frameworks/AutomatedDeviceEnrollment.framework/PlugIns/AddDevicesToAutomatedDeviceEnrollmentExtension.appex/AddDevicesToAutomatedDeviceEnrollmentExtension](MACHOS/AddDevicesToAutomatedDeviceEnrollmentExtension.md)
- [/System/Library/Frameworks/Contacts.framework/Support/contactsd](MACHOS/contactsd.md)
- [/System/Library/Frameworks/CoreImage.framework/photo_style_archive_bin.metallib](MACHOS/photo_style_archive_bin.metallib.md)
- [/System/Library/Frameworks/CoreImage.framework/redeye_repair_archive_bin.metallib](MACHOS/redeye_repair_archive_bin.metallib.md)
- [/System/Library/Frameworks/CoreLocation.framework/PlugIns/CoreLocationMapLNPromptPlugin.appex/CoreLocationMapLNPromptPlugin](MACHOS/CoreLocationMapLNPromptPlugin.md)
- [/System/Library/Frameworks/CoreLocation.framework/XPCServices/eedmediaservice.xpc/eedmediaservice](MACHOS/eedmediaservice.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/Support/com.apple.spotlight.IndexAgent](MACHOS/com.apple.spotlight.IndexAgent.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/spotlightknowledged](MACHOS/spotlightknowledged.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenterMobileHelper](MACHOS/CommCenterMobileHelper.md)
- [/System/Library/Frameworks/FamilyControls.framework/PlugIns/ActivityPickerExtension.appex/ActivityPickerExtension](MACHOS/ActivityPickerExtension.md)
- [/System/Library/Frameworks/FileProvider.framework/OverrideBundles/CloudDocsFileProvider.bundle/CloudDocsFileProvider](MACHOS/CloudDocsFileProvider.md)
- [/System/Library/Frameworks/FileProvider.framework/PlugIns/LocalStorageFileProvider.appex/LocalStorageFileProvider](MACHOS/LocalStorageFileProvider.md)
- [/System/Library/Frameworks/HealthKit.framework/PlugIns/com.apple.HealthKit.HealthResearchLogsDiagnosticExtension.appex/com.apple.HealthKit.HealthResearchLogsDiagnosticExtension](MACHOS/com.apple.HealthKit.HealthResearchLogsDiagnosticExtension.md)
- [/System/Library/Frameworks/IdentityLookup.framework/XPCServices/com.apple.IdentityLookup.MessageFilter.xpc/com.apple.IdentityLookup.MessageFilter](MACHOS/com.apple.IdentityLookup.MessageFilter.md)
- [/System/Library/Frameworks/ImageIO.framework/archive.metallib](MACHOS/archive.metallib.md)
- [/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond](MACHOS/managedappdistributiond.md)
- [/System/Library/Frameworks/ManagedSettings.framework/ManagedSettingsAgent](MACHOS/ManagedSettingsAgent.md)
- [/System/Library/Frameworks/Security.framework/CloudKeychainProxy.bundle/CloudKeychainProxy](MACHOS/CloudKeychainProxy.md)
- [/System/Library/Frameworks/Security.framework/XPCServices/TrustedPeersHelper.xpc/TrustedPeersHelper](MACHOS/TrustedPeersHelper.md)
- [/System/Library/Frameworks/Security.framework/XPCServices/XPCAcmeService.xpc/XPCAcmeService](MACHOS/XPCAcmeService.md)
- [/System/Library/Frameworks/Security.framework/swcagent](MACHOS/swcagent.md)
- [/System/Library/Frameworks/Speech.framework/XPCServices/localspeechrecognition.xpc/localspeechrecognition](MACHOS/localspeechrecognition.md)
- [/System/Library/Frameworks/StoreKit.framework/Support/storekitd](MACHOS/storekitd.md)
- [/System/Library/Frameworks/UIKit.framework/PlugIns/com.apple.UIKit.ColorPicker.appex/com.apple.UIKit.ColorPicker](MACHOS/com.apple.UIKit.ColorPicker.md)
- [/System/Library/Messages/PlugIns/RCS.imservice/RCS](MACHOS/RCS.md)
- [/System/Library/Messages/PlugIns/SMS.imservice/SMS](MACHOS/SMS.md)
- [/System/Library/Messages/PlugIns/SatelliteSMS.imservice/SatelliteSMS](MACHOS/SatelliteSMS.md)
- [/System/Library/Messages/PlugIns/iMessage.imservice/iMessage](MACHOS/iMessage.md)
- [/System/Library/Messages/PlugIns/iMessageLite.imservice/iMessageLite](MACHOS/iMessageLite.md)
- [/System/Library/Messages/iMessageApps/AnimojiCameraApp.bundle/AnimojiCameraApp](MACHOS/AnimojiCameraApp.md)
- [/System/Library/Messages/iMessageBalloons/ASMessagesProvider.bundle/ASMessagesProvider](MACHOS/ASMessagesProvider.md)
- [/System/Library/Messages/iMessageBalloons/HandwritingProvider.bundle/HandwritingProvider](MACHOS/HandwritingProvider.md)
- [/System/Library/Messages/iMessageBalloons/MSMessageExtensionBalloonPlugin.bundle/MSMessageExtensionBalloonPlugin](MACHOS/MSMessageExtensionBalloonPlugin.md)
- [/System/Library/NanoPreferenceBundles/Applications/DepthCompanionSettings.bundle/DepthCompanionSettings](MACHOS/DepthCompanionSettings.md)
- [/System/Library/NanoPreferenceBundles/General/CSLCompanionLiveActivitiesSettings.bundle/CSLCompanionLiveActivitiesSettings](MACHOS/CSLCompanionLiveActivitiesSettings.md)
- [/System/Library/NanoPreferenceBundles/General/CompanionAutoLaunchSettings.bundle/CompanionAutoLaunchSettings](MACHOS/CompanionAutoLaunchSettings.md)
- [/System/Library/NanoPreferenceBundles/General/CompanionInternationalSettings.bundle/CompanionInternationalSettings](MACHOS/CompanionInternationalSettings.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/ActivityBridgeSetup.bundle/ActivityBridgeSetup](MACHOS/ActivityBridgeSetup.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/NanoRemindersComplication.bundle/NanoRemindersComplication](MACHOS/NanoRemindersComplication.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKCaliforniaFaceBundleCompanion.bundle/NTKCaliforniaFaceBundleCompanion](MACHOS/NTKCaliforniaFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKCloudrakerFaceBundleCompanion.bundle/NTKCloudrakerFaceBundleCompanion](MACHOS/NTKCloudrakerFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKInfographModularFaceBundle.bundle/NTKInfographModularFaceBundle](MACHOS/NTKInfographModularFaceBundle.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKZeusFaceBundleCompanion.bundle/NTKZeusFaceBundleCompanion](MACHOS/NTKZeusFaceBundleCompanion.md)
- [/System/Library/PreferenceBundles/AccessibilitySettings.bundle/AccessibilitySettings](MACHOS/AccessibilitySettings.md)
- [/System/Library/PreferenceBundles/AccountSettings/icloudMailSettings.bundle/icloudMailSettings](MACHOS/icloudMailSettings.md)
- [/System/Library/PreferenceBundles/AirDropSettings.bundle/AirDropSettings](MACHOS/AirDropSettings.md)
- [/System/Library/PreferenceBundles/AirPlayAndHandoffSettings.bundle/AirPlayAndHandoffSettings](MACHOS/AirPlayAndHandoffSettings.md)
- [/System/Library/PreferenceBundles/AppInstallationSettings.bundle/AppInstallationSettings](MACHOS/AppInstallationSettings.md)
- [/System/Library/PreferenceBundles/BatteryUsageUI.bundle/BatteryUsageUI](MACHOS/BatteryUsageUI.md)
- [/System/Library/PreferenceBundles/CameraSettings.bundle/CameraSettings](MACHOS/CameraSettings.md)
- [/System/Library/PreferenceBundles/CarKitSettings.bundle/CarKitSettings](MACHOS/CarKitSettings.md)
- [/System/Library/PreferenceBundles/ContactsSettings.bundle/ContactsSettings](MACHOS/ContactsSettings.md)
- [/System/Library/PreferenceBundles/DriverKitSettings.bundle/DriverKitSettings](MACHOS/DriverKitSettings.md)
- [/System/Library/PreferenceBundles/FocusSettings.bundle/FocusSettings](MACHOS/FocusSettings.md)
- [/System/Library/PreferenceBundles/GameControlleriOSSettings.bundle/GameControlleriOSSettings](MACHOS/GameControlleriOSSettings.md)
- [/System/Library/PreferenceBundles/HearingSettings.bundle/HearingSettings](MACHOS/HearingSettings.md)
- [/System/Library/PreferenceBundles/JournalSettings.bundle/JournalSettings](MACHOS/JournalSettings.md)
- [/System/Library/PreferenceBundles/MapsSettings.bundle/MapsSettings](MACHOS/MapsSettings.md)
- [/System/Library/PreferenceBundles/MobileCalSettings.bundle/MobileCalSettings](MACHOS/MobileCalSettings.md)
- [/System/Library/PreferenceBundles/MultitaskingAndGesturesSettings.bundle/MultitaskingAndGesturesSettings](MACHOS/MultitaskingAndGesturesSettings.md)
- [/System/Library/PreferenceBundles/PassbookSettings.bundle/PassbookSettings](MACHOS/PassbookSettings.md)
- [/System/Library/PreferenceBundles/PodcastsSettingsPlugin.bundle/PodcastsSettingsPlugin](MACHOS/PodcastsSettingsPlugin.md)
- [/System/Library/PreferenceBundles/Privacy/WalletPrivacySettings.bundle/WalletPrivacySettings](MACHOS/WalletPrivacySettings.md)
- [/System/Library/PreferenceBundles/PrivacyAndSecuritySettings.bundle/PrivacyAndSecuritySettings](MACHOS/PrivacyAndSecuritySettings.md)
- [/System/Library/PreferenceBundles/RemindersSettings.bundle/RemindersSettings](MACHOS/RemindersSettings.md)
- [/System/Library/PreferenceBundles/StorageSettingsUI.bundle/StorageSettingsUI](MACHOS/StorageSettingsUI.md)
- [/System/Library/PreferenceBundles/UsageSettings.bundle/UsageSettings](MACHOS/UsageSettings.md)
- [/System/Library/PreferenceBundles/VoiceControlSettings.bundle/VoiceControlSettings](MACHOS/VoiceControlSettings.md)
- [/System/Library/PreferenceBundles/WiFiSettings.bundle/WiFiSettings](MACHOS/WiFiSettings.md)
- [/System/Library/PrivateFrameworks/ABMHelper.framework/Support/abm-helper](MACHOS/abm-helper.md)
- [/System/Library/PrivateFrameworks/ASOctaneSupport.framework/XPCServices/ASOctaneSupportXPCService.xpc/ASOctaneSupportXPCService](MACHOS/ASOctaneSupportXPCService.md)
- [/System/Library/PrivateFrameworks/AccessibilityUtilities.framework/PlugIns/AXSettingsShortcuts.appex/AXSettingsShortcuts](MACHOS/AXSettingsShortcuts.md)
- [/System/Library/PrivateFrameworks/AppPredictionFoundation.framework/XPCServices/AppPredictionIntentsHelperService.xpc/AppPredictionIntentsHelperService](MACHOS/AppPredictionIntentsHelperService.md)
- [/System/Library/PrivateFrameworks/AppStoreComponents.framework/Support/appstorecomponentsd](MACHOS/appstorecomponentsd.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored](MACHOS/appstored.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/amsaccountsd](MACHOS/amsaccountsd.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/amsengagementd](MACHOS/amsengagementd.md)
- [/System/Library/PrivateFrameworks/ApplePushService.framework/apsd](MACHOS/apsd.md)
- [/System/Library/PrivateFrameworks/AskPermission.framework/Support/askpermissiond](MACHOS/askpermissiond.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd](MACHOS/assistantd.md)
- [/System/Library/PrivateFrameworks/AuthKitUI.framework/PlugIns/AKAppSSOExtension.appex/AKAppSSOExtension](MACHOS/AKAppSSOExtension.md)
- [/System/Library/PrivateFrameworks/AuthKitUI.framework/PlugIns/AKSecondFactorEntryAlert.appex/AKSecondFactorEntryAlert](MACHOS/AKSecondFactorEntryAlert.md)
- [/System/Library/PrivateFrameworks/BookDataStore.framework/Support/bookdatastored](MACHOS/bookdatastored.md)
- [/System/Library/PrivateFrameworks/CMCapture.framework/PlugIns/CMCaptureDiagnosticExtension.appex/CMCaptureDiagnosticExtension](MACHOS/CMCaptureDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/CSExattrCrypto.framework/XPCServices/CSExattrCryptoService.xpc/CSExattrCryptoService](MACHOS/CSExattrCryptoService.md)
- [/System/Library/PrivateFrameworks/CallHistory.framework/Support/CallHistorySyncHelper](MACHOS/CallHistorySyncHelper.md)
- [/System/Library/PrivateFrameworks/CameraUI.framework/ShutterLiquid.metallib](MACHOS/ShutterLiquid.metallib.md)
- [/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/Support/cloudphotod](MACHOS/cloudphotod.md)
- [/System/Library/PrivateFrameworks/CloudSharing.framework/XPCServices/SPIHelper-iOS.xpc/SPIHelper-iOS](MACHOS/SPIHelper-iOS.md)
- [/System/Library/PrivateFrameworks/CloudSharingUI.framework/PlugIns/com.apple.CloudSharingUI.AddParticipants.appex/com.apple.CloudSharingUI.AddParticipants](MACHOS/com.apple.CloudSharingUI.AddParticipants.md)
- [/System/Library/PrivateFrameworks/CloudSharingUI.framework/PlugIns/com.apple.CloudSharingUI.CloudSharing.appex/com.apple.CloudSharingUI.CloudSharing](MACHOS/com.apple.CloudSharingUI.CloudSharing.md)
- [/System/Library/PrivateFrameworks/CloudTelemetry.framework/XPCServices/CloudTelemetryService.xpc/CloudTelemetryService](MACHOS/CloudTelemetryService.md)
- [/System/Library/PrivateFrameworks/CoreAccessories.framework/Support/accessoryd](MACHOS/accessoryd.md)
- [/System/Library/PrivateFrameworks/CoreAccessories.framework/XPCServices/ACCHWComponentAuthService.xpc/ACCHWComponentAuthService](MACHOS/ACCHWComponentAuthService.md)
- [/System/Library/PrivateFrameworks/CoreAccessoriesFeatures.framework/XPCServices/ACCFeatureAudioProductService.xpc/ACCFeatureAudioProductService](MACHOS/ACCFeatureAudioProductService.md)
- [/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsd](MACHOS/analyticsd.md)
- [/System/Library/PrivateFrameworks/CoreCDPUI.framework/PlugIns/CDPFollowUpExtension.appex/CDPFollowUpExtension](MACHOS/CDPFollowUpExtension.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/parsec-fbf](MACHOS/parsec-fbf.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/parsecd](MACHOS/parsecd.md)
- [/System/Library/PrivateFrameworks/CoreRoutine.framework/XPCServices/CoreRoutineHelperService.xpc/CoreRoutineHelperService](MACHOS/CoreRoutineHelperService.md)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd](MACHOS/corespeechd.md)
- [/System/Library/PrivateFrameworks/CoreSuggestions.framework/Tools/suggest_tool](MACHOS/suggest_tool.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/XPCServices/com.apple.dt.DTMLModelRunnerService.xpc/com.apple.dt.DTMLModelRunnerService](MACHOS/com.apple.dt.DTMLModelRunnerService.md)
- [/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/DesktopServicesHelper](MACHOS/DesktopServicesHelper.md)
- [/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/XPCServices/ArchiveService.xpc/ArchiveService](MACHOS/ArchiveService.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Cellular.appex/com.apple.DiagnosticExtensions.Cellular](MACHOS/com.apple.DiagnosticExtensions.Cellular.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Telephony.appex/com.apple.DiagnosticExtensions.Telephony](MACHOS/com.apple.DiagnosticExtensions.Telephony.md)
- [/System/Library/PrivateFrameworks/DocumentManagerCore.framework/XPCServices/com.apple.DocumentManagerCore.Rename.xpc/com.apple.DocumentManagerCore.Rename](MACHOS/com.apple.DocumentManagerCore.Rename.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAppPopover.appex/RecentsAppPopover](MACHOS/RecentsAppPopover.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAvocado.appex/RecentsAvocado](MACHOS/RecentsAvocado.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/SaveToFiles.appex/SaveToFiles](MACHOS/SaveToFiles.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/com.apple.DocumentManager.Service.appex/com.apple.DocumentManager.Service](MACHOS/com.apple.DocumentManager.Service.md)
- [/System/Library/PrivateFrameworks/EmailDaemon.framework/maild](MACHOS/maild.md)
- [/System/Library/PrivateFrameworks/FamilyCircle.framework/familycircled](MACHOS/familycircled.md)
- [/System/Library/PrivateFrameworks/FinHealth.framework/ClientTools/finhealthclient](MACHOS/finhealthclient.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/Resources/UITypographyPanel.bundle/UITypographyPanel](MACHOS/UITypographyPanel.md)
- [/System/Library/PrivateFrameworks/GPUToolsCapture.framework/GPUToolsCapture](MACHOS/GPUToolsCapture.md)
- [/System/Library/PrivateFrameworks/GenerationalStorage.framework/revisiond](MACHOS/revisiond.md)
- [/System/Library/PrivateFrameworks/HealthPluginHost.framework/healthappd](MACHOS/healthappd.md)
- [/System/Library/PrivateFrameworks/HomePlatformSettingsUI.framework/PlugIns/HPSUIViewService.appex/HPSUIViewService](MACHOS/HPSUIViewService.md)
- [/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd](MACHOS/identityservicesd.md)
- [/System/Library/PrivateFrameworks/IDSBlastDoorSupport.framework/XPCServices/IDSBlastDoorService.xpc/IDSBlastDoorService](MACHOS/IDSBlastDoorService.md)
- [/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/imagent](MACHOS/imagent.md)
- [/System/Library/PrivateFrameworks/IMDMessageServices.framework/XPCServices/IMDMessageServicesAgent.xpc/IMDMessageServicesAgent](MACHOS/IMDMessageServicesAgent.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/intelligenceflowd](MACHOS/intelligenceflowd.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatform.framework/PlugIns/DiagnosticExtension.appex/DiagnosticExtension](MACHOS/DiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCompute.framework/XPCServices/IntelligencePlatformComputeService.xpc/IntelligencePlatformComputeService](MACHOS/IntelligencePlatformComputeService.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/PlugIns/IntelligencePlatformLighthousePlugin.appex/IntelligencePlatformLighthousePlugin](MACHOS/IntelligencePlatformLighthousePlugin.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/intelligenceplatformd](MACHOS/intelligenceplatformd.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/knowledgeconstructiond](MACHOS/knowledgeconstructiond.md)
- [/System/Library/PrivateFrameworks/LockdownMode.framework/lockdownmoded](MACHOS/lockdownmoded.md)
- [/System/Library/PrivateFrameworks/MLKit.framework/PlugIns/com.apple.MLKit.MLPackagePreview.appex/com.apple.MLKit.MLPackagePreview](MACHOS/com.apple.MLKit.MLPackagePreview.md)
- [/System/Library/PrivateFrameworks/MapsSync.framework/mapssyncd](MACHOS/mapssyncd.md)
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd](MACHOS/mediaanalysisd.md)
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd-service](MACHOS/mediaanalysisd-service.md)
- [/System/Library/PrivateFrameworks/MediaAnalysisBlastDoorSupport.framework/XPCServices/MediaAnalysisBlastDoorService.xpc/MediaAnalysisBlastDoorService](MACHOS/MediaAnalysisBlastDoorService.md)
- [/System/Library/PrivateFrameworks/MediaRemote.framework/Support/mediaremoted](MACHOS/mediaremoted.md)
- [/System/Library/PrivateFrameworks/MentalHealthUI.framework/archive.metallib](MACHOS/archive.metallib.md)
- [/System/Library/PrivateFrameworks/Message.framework/XPCServices/SearchIndexer.xpc/SearchIndexer](MACHOS/SearchIndexer.md)
- [/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/XPCServices/MessagesBlastDoorService.xpc/MessagesBlastDoorService](MACHOS/MessagesBlastDoorService.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/Support/accessoryupdaterd](MACHOS/accessoryupdaterd.md)
- [/System/Library/PrivateFrameworks/MobileAsset.framework/XPCServices/ManifestStorageService.xpc/ManifestStorageService](MACHOS/ManifestStorageService.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/backupd](MACHOS/backupd.md)
- [/System/Library/PrivateFrameworks/NanoPreferencesSync.framework/nanoprefsyncd](MACHOS/nanoprefsyncd.md)
- [/System/Library/PrivateFrameworks/NanoSystemSettings.framework/nanosystemsettingsd](MACHOS/nanosystemsettingsd.md)
- [/System/Library/PrivateFrameworks/NearbySessions.framework/XPCServices/com.apple.SharePlay.NearbyInvitationsService.xpc/com.apple.SharePlay.NearbyInvitationsService](MACHOS/com.apple.SharePlay.NearbyInvitationsService.md)
- [/System/Library/PrivateFrameworks/NeighborhoodActivityConduit.framework/XPCServices/com.apple.NeighborhoodActivityConduitService.xpc/com.apple.NeighborhoodActivityConduitService](MACHOS/com.apple.NeighborhoodActivityConduitService.md)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/passd](MACHOS/passd.md)
- [/System/Library/PrivateFrameworks/Pasteboard.framework/Support/pasted](MACHOS/pasted.md)
- [/System/Library/PrivateFrameworks/People.framework/peopled](MACHOS/peopled.md)
- [/System/Library/PrivateFrameworks/PerfPowerServicesReader.framework/XPCServices/PerfPowerTelemetryReaderService.xpc/PerfPowerTelemetryReaderService](MACHOS/PerfPowerTelemetryReaderService.md)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/XPCServices/PerfPowerServicesSignpostReader.xpc/PerfPowerServicesSignpostReader](MACHOS/PerfPowerServicesSignpostReader.md)
- [/System/Library/PrivateFrameworks/PreviewsOSSupport.framework/Support/previewsd](MACHOS/previewsd.md)
- [/System/Library/PrivateFrameworks/PrivateCloudCompute.framework/privatecloudcomputed.app/privatecloudcomputed](MACHOS/privatecloudcomputed.md)
- [/System/Library/PrivateFrameworks/ReminderKit.framework/PlugIns/RemindersNotificationContentExtension.appex/RemindersNotificationContentExtension](MACHOS/RemindersNotificationContentExtension.md)
- [/System/Library/PrivateFrameworks/ReminderKitUI.framework/PlugIns/com.apple.ReminderKitUI.ReminderCreationViewService.appex/com.apple.ReminderKitUI.ReminderCreationViewService](MACHOS/com.apple.ReminderKitUI.ReminderCreationViewService.md)
- [/System/Library/PrivateFrameworks/RenderBox.framework/archive.metallib](MACHOS/archive.metallib.md)
- [/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeAgent](MACHOS/ScreenTimeAgent.md)
- [/System/Library/PrivateFrameworks/Search.framework/PlugIns/SpotlightDiagnostic.appex/SpotlightDiagnostic](MACHOS/SpotlightDiagnostic.md)
- [/System/Library/PrivateFrameworks/Search.framework/searchd](MACHOS/searchd.md)
- [/System/Library/PrivateFrameworks/SharingHUD.framework/XPCServices/SharingHUDService.xpc/SharingHUDService](MACHOS/SharingHUDService.md)
- [/System/Library/PrivateFrameworks/SiriUICore.framework/archive.metallib](MACHOS/archive.metallib.md)
- [/System/Library/PrivateFrameworks/SiriVOX.framework/SiriHeadlessService](MACHOS/SiriHeadlessService.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateServicesUI.framework/Plugins/SoftwareUpdateServicesUIPlugin.servicebundle/SoftwareUpdateServicesUIPlugin](MACHOS/SoftwareUpdateServicesUIPlugin.md)
- [/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/XPCServices/com.apple.SpeechRecognitionCore.brokerd.xpc/XPCServices/com.apple.SpeechRecognitionCore.speechrecognitiond.xpc/com.apple.SpeechRecognitionCore.speechrecognitiond](MACHOS/com.apple.SpeechRecognitionCore.speechrecognitiond.md)
- [/System/Library/PrivateFrameworks/TCC.framework/Support/tccd](MACHOS/tccd.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/PlugIns/PhoneIntentHandler.appex/PhoneIntentHandler](MACHOS/PhoneIntentHandler.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/XPCServices/com.apple.FTLivePhotoService.xpc/com.apple.FTLivePhotoService](MACHOS/com.apple.FTLivePhotoService.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd](MACHOS/callservicesd.md)
- [/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingSupport.framework/Support/voicebankingd](MACHOS/voicebankingd.md)
- [/System/Library/PrivateFrameworks/TranslationUIServices.framework/PlugIns/TranslationUIService.appex/TranslationUIService](MACHOS/TranslationUIService.md)
- [/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTrackingAgent](MACHOS/UsageTrackingAgent.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/ExtragalacticPoster.appex/ExtragalacticPoster](MACHOS/ExtragalacticPoster.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/RhizomePoster.appex/RhizomePoster](MACHOS/RhizomePoster.md)
- [/System/Library/PrivateFrameworks/WiFiPolicy.framework/XPCServices/WiFiCloudAssetsXPCService.xpc/WiFiCloudAssetsXPCService](MACHOS/WiFiCloudAssetsXPCService.md)
- [/System/Library/PrivateFrameworks/WirelessInsights.framework/Support/wirelessinsightsd](MACHOS/wirelessinsightsd.md)
- [/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/BackgroundShortcutRunner.xpc/BackgroundShortcutRunner](MACHOS/BackgroundShortcutRunner.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/FocusConfigurationExtension.appex/FocusConfigurationExtension](MACHOS/FocusConfigurationExtension.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/SystemActionConfigurationExtension.appex/SystemActionConfigurationExtension](MACHOS/SystemActionConfigurationExtension.md)
- [/System/Library/ScreenReader/BrailleTables/Rhine.brailletable/Rhine](MACHOS/Rhine.md)
- [/System/Library/Settings/InstalledApps.settings/InstalledApps](MACHOS/InstalledApps.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/AudioSuggestionsPlugin.bundle/AudioSuggestionsPlugin](MACHOS/AudioSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/HomeAutomationSiriSuggestions.bundle/HomeAutomationSiriSuggestions](MACHOS/HomeAutomationSiriSuggestions.md)
- [/System/Library/Snippets/UIPlugins/ResponseGenerationUIPlugin.bundle/ResponseGenerationUIPlugin](MACHOS/ResponseGenerationUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SystemPlugin.bundle/SystemPlugin](MACHOS/SystemPlugin.md)
- [/System/Library/SpringBoardPlugins/PassesLockScreenPlugin.lockbundle/PassesLockScreenPlugin](MACHOS/PassesLockScreenPlugin.md)
- [/System/Library/SyncBundles/MobileSlideShow.syncBundle/MobileSlideShow](MACHOS/MobileSlideShow.md)
- [/System/Library/UserEventPlugins/com.apple.accessoryd.matching.plugin/com.apple.accessoryd.matching](MACHOS/com.apple.accessoryd.matching.md)
- [/System/Library/UserEventPlugins/com.apple.cts.plugin/com.apple.cts](MACHOS/com.apple.cts.md)
- [/System/Library/Video/Plug-Ins/AppleMCTF.bundle/AppleMCTF](MACHOS/AppleMCTF.md)
- [/System/Library/Video/Plug-Ins/AppleVideoEncoder.bundle/AppleVideoEncoder](MACHOS/AppleVideoEncoder.md)
- [/System/Library/VideoProcessors/CCPortrait.bundle/ccportrait_archive_bin.metallib](MACHOS/ccportrait_archive_bin.metallib.md)
- [/System/Library/VideoProcessors/ColourConstancyV1.bundle/ColourConstancyV1](MACHOS/ColourConstancyV1.md)
- [/System/Library/VideoProcessors/SemanticStyleV1.bundle/SemanticStyleV1](MACHOS/SemanticStyleV1.md)
- [/System/Library/VideoProcessors/SuperResolutionV2.bundle/SuperResolutionV2](MACHOS/SuperResolutionV2.md)
- [/System/Library/VideoProcessors/VideoDeghostingV1.bundle/VideoDeghostingV1](MACHOS/VideoDeghostingV1.md)
- [/System/Library/VideoProcessors/VideoDeghostingV2.bundle/VideoDeghostingV2](MACHOS/VideoDeghostingV2.md)
- [/System/Library/VideoProcessors/VideoStabilizationV2.bundle/VideoStabilizationV2](MACHOS/VideoStabilizationV2.md)
- [/private/var/staged_system_apps/AppleTV.app/PlugIns/TVWidgetExtension.appex/TVWidgetExtension](MACHOS/TVWidgetExtension.md)
- [/private/var/staged_system_apps/Books.app/Books](MACHOS/Books.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BlissReader.framework/BlissReader](MACHOS/BlissReader.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookAnalytics.framework/BookAnalytics](MACHOS/BookAnalytics.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookEPUB.framework/BookEPUB](MACHOS/BookEPUB.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookStoreUI.framework/BookStoreUI](MACHOS/BookStoreUI.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BooksPersonalization.framework/BooksPersonalization](MACHOS/BooksPersonalization.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BooksUI.framework/BooksUI](MACHOS/BooksUI.md)
- [/private/var/staged_system_apps/Books.app/PlugIns/BooksWidgetExtension.appex/BooksWidgetExtension](MACHOS/BooksWidgetExtension.md)
- [/private/var/staged_system_apps/Bridge.app/Bridge](MACHOS/Bridge.md)
- [/private/var/staged_system_apps/Calculator.app/Calculator](MACHOS/Calculator.md)
- [/private/var/staged_system_apps/FaceTime.app/FaceTime](MACHOS/FaceTime.md)
- [/private/var/staged_system_apps/Files.app/Files](MACHOS/Files.md)
- [/private/var/staged_system_apps/FindMy.app/FindMy](MACHOS/FindMy.md)
- [/private/var/staged_system_apps/FindMy.app/Frameworks/FindMyAppCore.framework/FindMyAppCore](MACHOS/FindMyAppCore.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyNotificationsService.appex/FindMyNotificationsService](MACHOS/FindMyNotificationsService.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyWidgetItems.appex/FindMyWidgetItems](MACHOS/FindMyWidgetItems.md)
- [/private/var/staged_system_apps/Fitness.app/Fitness](MACHOS/Fitness.md)
- [/private/var/staged_system_apps/Freeform.app/Extensions/USDRendererExtension.appex/USDRendererExtension](MACHOS/USDRendererExtension.md)
- [/private/var/staged_system_apps/Freeform.app/Freeform](MACHOS/Freeform.md)
- [/private/var/staged_system_apps/Freeform.app/PlugIns/FreeformSharingExtension.appex/FreeformSharingExtension](MACHOS/FreeformSharingExtension.md)
- [/private/var/staged_system_apps/Health.app/Health](MACHOS/Health.md)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeWidget.appex/HomeWidget](MACHOS/HomeWidget.md)
- [/private/var/staged_system_apps/Journal.app/Journal](MACHOS/Journal.md)
- [/private/var/staged_system_apps/Journal.app/PlugIns/JournalShareExtension.appex/JournalShareExtension](MACHOS/JournalShareExtension.md)
- [/private/var/staged_system_apps/Journal.app/PlugIns/JournalWidgets.appex/JournalWidgets](MACHOS/JournalWidgets.md)
- [/private/var/staged_system_apps/Journal.app/PlugIns/JournalWidgetsSecure.appex/JournalWidgetsSecure](MACHOS/JournalWidgetsSecure.md)
- [/private/var/staged_system_apps/Maps.app/Maps](MACHOS/Maps.md)
- [/private/var/staged_system_apps/Measure.app/Measure](MACHOS/Measure.md)
- [/private/var/staged_system_apps/MobileCal.app/MobileCal](MACHOS/MobileCal.md)
- [/private/var/staged_system_apps/MobileCal.app/PlugIns/CalendarWidgetExtension.appex/CalendarWidgetExtension](MACHOS/CalendarWidgetExtension.md)
- [/private/var/staged_system_apps/MobileMail.app/MobileMail](MACHOS/MobileMail.md)
- [/private/var/staged_system_apps/MobileMail.app/PlugIns/MailWidgetExtension.appex/MailWidgetExtension](MACHOS/MailWidgetExtension.md)
- [/private/var/staged_system_apps/MobileNotes.app/MobileNotes](MACHOS/MobileNotes.md)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.SharingExtension.appex/com.apple.mobilenotes.SharingExtension](MACHOS/com.apple.mobilenotes.SharingExtension.md)
- [/private/var/staged_system_apps/MobileTimer.app/PlugIns/WorldClockWidget.appex/WorldClockWidget](MACHOS/WorldClockWidget.md)
- [/private/var/staged_system_apps/Music.app/Frameworks/MusicApplication.framework/MusicApplication](MACHOS/MusicApplication.md)
- [/private/var/staged_system_apps/Music.app/Frameworks/MusicApplication.framework/XPCServices/MusicScriptUpdateService.xpc/MusicScriptUpdateService](MACHOS/MusicScriptUpdateService.md)
- [/private/var/staged_system_apps/Music.app/Music](MACHOS/Music.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/MusicMessagesApp.appex/MusicMessagesApp](MACHOS/MusicMessagesApp.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/MusicWidgets.appex/MusicWidgets](MACHOS/MusicWidgets.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsNotificationServiceExtension.appex/NewsNotificationServiceExtension](MACHOS/NewsNotificationServiceExtension.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsToday2.appex/NewsToday2](MACHOS/NewsToday2.md)
- [/private/var/staged_system_apps/Passbook.app/Passbook](MACHOS/Passbook.md)
- [/private/var/staged_system_apps/Passbook.app/PlugIns/PassbookLockedWidgetsExtension.appex/PassbookLockedWidgetsExtension](MACHOS/PassbookLockedWidgetsExtension.md)
- [/private/var/staged_system_apps/Passbook.app/PlugIns/PassbookTransactionNotificationContentExtension.appex/PassbookTransactionNotificationContentExtension](MACHOS/PassbookTransactionNotificationContentExtension.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/NowPlayingUI.framework/NowPlayingUI](MACHOS/NowPlayingUI.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/ShelfKit.framework/ShelfKit](MACHOS/ShelfKit.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/ShelfKitCollectionViews.framework/ShelfKitCollectionViews](MACHOS/ShelfKitCollectionViews.md)
- [/private/var/staged_system_apps/Podcasts.app/PlugIns/PodcastsWidget.appex/PodcastsWidget](MACHOS/PodcastsWidget.md)
- [/private/var/staged_system_apps/Podcasts.app/Podcasts](MACHOS/Podcasts.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersIntentsExtension.appex/RemindersIntentsExtension](MACHOS/RemindersIntentsExtension.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersIntentsUIExtension.appex/RemindersIntentsUIExtension](MACHOS/RemindersIntentsUIExtension.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersSharingExtension.appex/RemindersSharingExtension](MACHOS/RemindersSharingExtension.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersSpotlightIndexExtension.appex/RemindersSpotlightIndexExtension](MACHOS/RemindersSpotlightIndexExtension.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersWidgetExtension.appex/RemindersWidgetExtension](MACHOS/RemindersWidgetExtension.md)
- [/private/var/staged_system_apps/Reminders.app/Reminders](MACHOS/Reminders.md)
- [/private/var/staged_system_apps/SequoiaTranslator.app/PlugIns/TranslationWidgetsExtension.appex/TranslationWidgetsExtension](MACHOS/TranslationWidgetsExtension.md)
- [/private/var/staged_system_apps/SequoiaTranslator.app/SequoiaTranslator](MACHOS/SequoiaTranslator.md)
- [/private/var/staged_system_apps/Shortcuts.app/Shortcuts](MACHOS/Shortcuts.md)
- [/private/var/staged_system_apps/Stocks.app/PlugIns/StocksWidget.appex/StocksWidget](MACHOS/StocksWidget.md)
- [/private/var/staged_system_apps/Stocks.app/Stocks](MACHOS/Stocks.md)
- [/private/var/staged_system_apps/Tips.app/PlugIns/TipsNotification.appex/TipsNotification](MACHOS/TipsNotification.md)
- [/private/var/staged_system_apps/Tips.app/Tips](MACHOS/Tips.md)
- [/private/var/staged_system_apps/VoiceMemos.app/VoiceMemos](MACHOS/VoiceMemos.md)
- [/private/var/staged_system_apps/Weather.app/PlugIns/WeatherPoster.appex/WeatherPoster](MACHOS/WeatherPoster.md)
- [/private/var/staged_system_apps/Weather.app/PlugIns/WeatherWidget.appex/WeatherWidget](MACHOS/WeatherWidget.md)
- [/private/var/staged_system_apps/Weather.app/Weather](MACHOS/Weather.md)
- [/sbin/launchd](MACHOS/launchd.md)
- [/usr/bin/abmlite](MACHOS/abmlite.md)
- [/usr/bin/brctl](MACHOS/brctl.md)
- [/usr/bin/powerlogHelperd](MACHOS/powerlogHelperd.md)
- [/usr/lib/dyld](MACHOS/dyld.md)
- [/usr/libexec/SidecarRelay](MACHOS/SidecarRelay.md)
- [/usr/libexec/amfid](MACHOS/amfid.md)
- [/usr/libexec/appleaccountd](MACHOS/appleaccountd.md)
- [/usr/libexec/applekeystored](MACHOS/applekeystored.md)
- [/usr/libexec/asd](MACHOS/asd.md)
- [/usr/libexec/asktod](MACHOS/asktod.md)
- [/usr/libexec/assessmentagent](MACHOS/assessmentagent.md)
- [/usr/libexec/audioaccessoryd](MACHOS/audioaccessoryd.md)
- [/usr/libexec/audioanalyticsd](MACHOS/audioanalyticsd.md)
- [/usr/libexec/backboardd](MACHOS/backboardd.md)
- [/usr/libexec/biomesyncd](MACHOS/biomesyncd.md)
- [/usr/libexec/bluetoothuserd](MACHOS/bluetoothuserd.md)
- [/usr/libexec/cameracaptured](MACHOS/cameracaptured.md)
- [/usr/libexec/caraccessoryd](MACHOS/caraccessoryd.md)
- [/usr/libexec/carkitd](MACHOS/carkitd.md)
- [/usr/libexec/coreidvd](MACHOS/coreidvd.md)
- [/usr/libexec/demod](MACHOS/demod.md)
- [/usr/libexec/deviceaccessd](MACHOS/deviceaccessd.md)
- [/usr/libexec/dockaccessoryd](MACHOS/dockaccessoryd.md)
- [/usr/libexec/driverkitd](MACHOS/driverkitd.md)
- [/usr/libexec/feedbackd](MACHOS/feedbackd.md)
- [/usr/libexec/findmylocated](MACHOS/findmylocated.md)
- [/usr/libexec/gamed](MACHOS/gamed.md)
- [/usr/libexec/gamepolicyd](MACHOS/gamepolicyd.md)
- [/usr/libexec/idcredd](MACHOS/idcredd.md)
- [/usr/libexec/launchd_cache_loader](MACHOS/launchd_cache_loader.md)
- [/usr/libexec/linkd](MACHOS/linkd.md)
- [/usr/libexec/locationd](MACHOS/locationd.md)
- [/usr/libexec/lockdownd](MACHOS/lockdownd.md)
- [/usr/libexec/modelmanagerd](MACHOS/modelmanagerd.md)
- [/usr/libexec/nanoregistryd](MACHOS/nanoregistryd.md)
- [/usr/libexec/nearbyd](MACHOS/nearbyd.md)
- [/usr/libexec/networkserviceproxy](MACHOS/networkserviceproxy.md)
- [/usr/libexec/nptocompaniond](MACHOS/nptocompaniond.md)
- [/usr/libexec/online-auth-agent](MACHOS/online-auth-agent.md)
- [/usr/libexec/otpaird](MACHOS/otpaird.md)
- [/usr/libexec/photosfaced](MACHOS/photosfaced.md)
- [/usr/libexec/profiled](MACHOS/profiled.md)
- [/usr/libexec/promotedcontentd](MACHOS/promotedcontentd.md)
- [/usr/libexec/proximitycontrold](MACHOS/proximitycontrold.md)
- [/usr/libexec/rapportd](MACHOS/rapportd.md)
- [/usr/libexec/remindd](MACHOS/remindd.md)
- [/usr/libexec/remotepairingdeviced](MACHOS/remotepairingdeviced.md)
- [/usr/libexec/replayd](MACHOS/replayd.md)
- [/usr/libexec/rtcreportingd](MACHOS/rtcreportingd.md)
- [/usr/libexec/safarifetcherd](MACHOS/safarifetcherd.md)
- [/usr/libexec/searchpartyd](MACHOS/searchpartyd.md)
- [/usr/libexec/securityd](MACHOS/securityd.md)
- [/usr/libexec/securityuploadd](MACHOS/securityuploadd.md)
- [/usr/libexec/seserviced](MACHOS/seserviced.md)
- [/usr/libexec/sharingd](MACHOS/sharingd.md)
- [/usr/libexec/sportsd](MACHOS/sportsd.md)
- [/usr/libexec/srp-mdns-proxy](MACHOS/srp-mdns-proxy.md)
- [/usr/libexec/swtransparencyd](MACHOS/swtransparencyd.md)
- [/usr/libexec/transparencyd](MACHOS/transparencyd.md)
- [/usr/libexec/trustd](MACHOS/trustd.md)
- [/usr/libexec/watchpresenced](MACHOS/watchpresenced.md)
- [/usr/libexec/webbookmarksd](MACHOS/webbookmarksd.md)
- [/usr/libexec/wifianalyticsd](MACHOS/wifianalyticsd.md)
- [/usr/libexec/wifip2pd](MACHOS/wifip2pd.md)
- [/usr/libexec/xpcproxy](MACHOS/xpcproxy.md)
- [/usr/libexec/xpcroleaccountd](MACHOS/xpcroleaccountd.md)
- [/usr/sbin/BTLEServer](MACHOS/BTLEServer.md)
- [/usr/sbin/WirelessRadioManagerd](MACHOS/WirelessRadioManagerd.md)
- [/usr/sbin/appleh16camerad](MACHOS/appleh16camerad.md)
- [/usr/sbin/bluetoothd](MACHOS/bluetoothd.md)
- [/usr/sbin/cfprefsd](MACHOS/cfprefsd.md)
- [/usr/sbin/ckksctl](MACHOS/ckksctl.md)
- [/usr/sbin/dietappleh16camerad](MACHOS/dietappleh16camerad.md)
- [/usr/sbin/distnoted](MACHOS/distnoted.md)
- [/usr/sbin/filecoordinationd](MACHOS/filecoordinationd.md)
- [/usr/sbin/mDNSResponder](MACHOS/mDNSResponder.md)
- [/usr/sbin/wifid](MACHOS/wifid.md)

</details>

### 🔑 Entitlements

- [Entitlements DIFF](Entitlements.md)

## Firmware

### ⬆️ Updated (12)

<details>
  <summary><i>View Updated</i></summary>

#### AppleAVE2FW_H16.im4p

>  `AppleAVE2FW_H16.im4p`

```diff

 
-  __TEXT.__text: 0xcac1c
-  __TEXT.__cstring: 0x12944
-  __TEXT.__const: 0x20858
+  __TEXT.__text: 0xcae2c
+  __TEXT.__cstring: 0x1294a
+  __TEXT.__const: 0x208a8
   __TEXT.__chain_starts: 0x0
   __TEXT._rtk_mtab: 0x320
   __TEXT.__constructor: 0x0
Symbols:
+ __ZN12AVE_KeyFrame4InitEiiddiii
- __ZN12AVE_KeyFrame4InitEiiddii
CStrings:
+ "%s::%s:%d %s | fail to initialize FPS %p %d %d %d.%03d %d.%03d %d %d %d %d"
+ "%s::%s:%d %s | fail to update FPS %p %d %d %d.%03d %d.%03d %d %d %d %d"
+ "8002.21.0"
- "%s::%s:%d %s | fail to initialize FPS %p %d %d %d.%03d %d.%03d %d %d %d"
- "%s::%s:%d %s | fail to update FPS %p %d %d %d.%03d %d.%03d %d %d %d"
- "8002.15.1"

```

#### adc-aceso-d8x.im4p

>  `adc-aceso-d8x.im4p`

```diff

 
-  __TEXT.__text: 0x7a80d4
+  __TEXT.__text: 0x7a88d4
   __TEXT.__data_copy: 0x100000
-  __TEXT.__const: 0x7fd940
-  __TEXT.__cstring: 0x9bc81
+  __TEXT.__const: 0x7fd9b0
+  __TEXT.__cstring: 0x9bf11
   __TEXT._rtk_mtab: 0x2a0
   __TEXT.__constructor: 0x0
   __TEXT.__chain_starts: 0x0
   __TEXT.text_env: 0x507ac
   __TEXT.__eh_frame: 0x308
-  __DATA.__const: 0x52ab8
+  __DATA.__const: 0x52a88
   __DATA._rtk_heap: 0x1000
   __DATA.__data: 0xdeeb8
   __DATA._rtk_power: 0x3a8

   __DATA.__zerofill: 0x20de60
   Functions: 0
   Symbols:   0
-  CStrings:  17189
+  CStrings:  17202
 
CStrings:
+ "%llu < chFrmCnt[%u][%u] %llu\n"
+ "%s %d: [IMAGE_BE_OUTPUT_CAPTURE].x=%d, width=%d, y=%d, height=%d\n"
+ "%s %d: mapped crop x=%d, y=%d, width=%d, height=%d\n"
+ "%s %d: newFESOutWidth=%d, newFESOutHeight=%d\n"
+ "%s %d: sensor native crop x=%d y=%d, width=%d height=%d\n"
+ "%s %d: targetDS=%f\n"
+ "%s %d: totalCropInFES.x=%d, y=%d, width=%d, height=%d\n"
+ "%s %d: validInWidth=%d, validInHeight=%d\n"
+ "%s: M:Deferring context switch request (config %d -> config %d) for current update.\n"
+ "%s: S:Deferring context switch request (config %d -> config %d) for current update.\n"
+ "10:52:12"
+ "Aug  7 2024"
+ "HueMap buffer is not available, use preview frame's hueMapBuffer !!!!"
+ "ImageSizeSetup"
+ "[DSI] Pinhole focal length is 0!, ST=0x%x using static value"
+ "[DSI] Replacing efl with Static Value=%f"
+ "pinhole focus length is invalid, use cal data"
- "%s: Deferring context switch request (-> config %d) for current update.\n"
- "00:12:59"
- "Jul 27 2024"
- "[DSI] Pinhole focal length is 0!, ST=0x%x"

```

#### agx_a000.bin

>  `agx_a000.bin`

```diff

 
-  __TEXT.__text: 0x5b334
+  __TEXT.__text: 0x5b360
   __TEXT.__gxf_shr_code: 0x554
-  __TEXT.__gxf_code: 0x10a0
+  __TEXT.__gxf_code: 0x10a4
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__const: 0x1e20
   __TEXT._rtk_patchbay: 0x1e8
CStrings:
+ "Aug  8 2024 22:45:08"
- "Jul 30 2024 20:37:23"

```

#### agx_b000.bin

>  `agx_b000.bin`

```diff

 
-  __TEXT.__text: 0x5b03c
+  __TEXT.__text: 0x5b068
   __TEXT.__gxf_shr_code: 0x554
-  __TEXT.__gxf_code: 0x10a0
+  __TEXT.__gxf_code: 0x10a4
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__const: 0x1e60
   __TEXT._rtk_patchbay: 0x1e8
CStrings:
+ "Aug  8 2024 22:47:49"
- "Jul 30 2024 20:39:49"

```

#### agx_b100.bin

>  `agx_b100.bin`

```diff

 
-  __TEXT.__text: 0x5b03c
+  __TEXT.__text: 0x5b068
   __TEXT.__gxf_shr_code: 0x554
-  __TEXT.__gxf_code: 0x10a0
+  __TEXT.__gxf_code: 0x10a4
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__const: 0x1e60
   __TEXT._rtk_patchbay: 0x1e8
CStrings:
+ "Aug  8 2024 22:48:52"
- "Jul 30 2024 20:40:46"

```

#### ansf.t8130.release.im4p

>  `ansf.t8130.release.im4p`

```diff

 
   __TEXT.text_first: 0x4488
-  __TEXT.__text: 0x172590
+  __TEXT.__text: 0x172594
   __TEXT.shared: 0xb6e4
   __TEXT.read: 0x5a78
   __TEXT.__const: 0x9088
   __TEXT.idle_hooks: 0x10
-  __TEXT.__cstring: 0x1e5d0
+  __TEXT.__cstring: 0x1e5d2
   __TEXT.__chain_starts: 0x0
   __TEXT.__constructor: 0x0
   __TEXT._rtk_mtab: 0x310
CStrings:
+ "499.0.9~1237"
+ "AppleStorageFirmwarePreASP3-499.0.9~1237"
- "499.0.9~933"
- "AppleStorageFirmwarePreASP3-499.0.9~933"

```

#### aopfw-iphone16aop.RELEASE.im4p

>  `aopfw-iphone16aop.RELEASE.im4p`

```diff

 
-  __TEXT.__text: 0x130acc
+  __TEXT.__text: 0x130b90
   __TEXT.__const: 0x11e00
-  __TEXT.__cstring: 0x81e5
+  __TEXT.__cstring: 0x81e0
   __TEXT.__chain_starts: 0x4c
   __TEXT.__eh_frame: 0x40
   __DATA._rtk_boot: 0x3000

   __DATA._rtk_exc_stack: 0x1000
   __DATA._rtk_ext_stack: 0x1800
   __DATA._rtk_heap: 0x3b340
-  __DATA.__const: 0x132d0
+  __DATA.__const: 0x132d8
   __DATA.__objc_imageinfo: 0x8
   __DATA.__data: 0x72d0
   __DATA._rtk_patchbay: 0x325

   __DATA._rtk_data_uuid: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0xd0d90
+  __DATA.__zerofill: 0xd0e70
   __ETEXT.__StaticInit: 0x78c0
   __ETEXT.__text: 0x38948
   __ETEXT.__const: 0xdce
   __EDATA.__data: 0x60
-  __OS_LOG.__string: 0x27722
+  __OS_LOG.__string: 0x27763
   __MISC.__apf_list: 0xb0
-  __CMA.__cma_log_string: 0x3e2c
-  Functions: 4215
+  __CMA.__cma_log_string: 0x3e38
+  Functions: 4214
   Symbols:   0
-  CStrings:  3635
+  CStrings:  3636
 
CStrings:
+ "04:41:25"
+ "04:50:22"
+ "16.0.0 (clang-1600.0.25.3) [+internal-os]"
+ "22A334"
+ "AppleSPUFirmware-2001.0.19~210"
+ "Aug  6 2024"
+ "SensingAlgsProx-52~434"
+ "[AOP][ALS] Could not find als"
+ "[AOP][ALS] Dispatching temperature %d.%d"
+ "[AOP][ALS] Error processing temperature 0x%x"
+ "[AOP][ALS] Found als service, creating als-die-temp relay"
- "16.0.0 (clang-1600.0.24.2) [+internal-os]"
- "19:32:43"
- "19:38:22"
- "22A5324t"
- "AppleSPUFirmware-2001.0.16.0.3~27"
- "Could not find als-die-temp"
- "Error processing temperature 0x%x"
- "Found als service, creating als-die-temp relay"
- "Jul 26 2024"
- "SensingAlgsProx-52~321"

```

#### rans.t8130.release.im4p

>  `rans.t8130.release.im4p`

```diff

 
   __TEXT.text_first: 0x4488
-  __TEXT.__text: 0x172590
+  __TEXT.__text: 0x172594
   __TEXT.shared: 0xb6e4
   __TEXT.read: 0x5a78
   __TEXT.__const: 0x9088
   __TEXT.idle_hooks: 0x10
-  __TEXT.__cstring: 0x1e5d0
+  __TEXT.__cstring: 0x1e5d2
   __TEXT.__chain_starts: 0x0
   __TEXT.__constructor: 0x0
   __TEXT._rtk_mtab: 0x310
CStrings:
+ "499.0.9~1237"
+ "AppleStorageFirmwarePreASP3-499.0.9~1237"
- "499.0.9~933"
- "AppleStorageFirmwarePreASP3-499.0.9~933"

```

#### sptm.t8122.release.im4p

>  `sptm.t8122.release.im4p`

```diff

-392.0.43.0.1
+392.2.1.0.0
   __TEXT.__cstring: 0xcea2
   __TEXT.__binname: 0x40
   __TEXT.__chain_starts: 0x6c
   __TEXT.__const: 0x9d0
   __DATA_CONST.__const: 0x59c8
   __LATE_CONST.__late_const: 0x5d5e0
-  __TEXT_EXEC.__text: 0x48a9c
+  __TEXT_EXEC.__text: 0x48ab8
   __LAST.__pinst: 0x8
   __DATA.__auth_ptr: 0x18
   __DATA.__data: 0x6

```

#### t8130dcp.im4p

>  `t8130dcp.im4p`

```diff

 
-  __TEXT.__text: 0x2deed8
-  __TEXT.__const: 0x7cf58
-  __TEXT.__cstring: 0x30e8b
+  __TEXT.__text: 0x2e1004
+  __TEXT.__const: 0x7d828
+  __TEXT.__cstring: 0x3103f
   __TEXT.__chain_starts: 0x68
   __DATA.__constructor: 0x8
-  __DATA.__const: 0x4a498
+  __DATA.__const: 0x4a528
   __DATA._rtk_patchbay: 0x710
   __DATA._rtk_data_uuid: 0x40
   __DATA.__data: 0x2b524

   __DATA._afk_sys_objt: 0xbb0
   __DATA._rtk_mtab: 0x5c8
   __DATA.__zerofill: 0x9b230
-  __OS_LOG.__string: 0x20ff2
-  Functions: 6841
+  __OS_LOG.__string: 0x21015
+  Functions: 6852
   Symbols:   0
-  CStrings:  6134
+  CStrings:  6138
 
CStrings:
+ "%s: VideoInterface::Plug IOMFBStatusNotReady\n"
+ "%s: VideoInterface::Unplug IOMFBStatusNotReady\n"
+ "A439_callback__"
+ "A442_callback__"
+ "Dropping this hotplug since system is powering down or previous plug was aborted : %d"
+ "IOMFB %s: TE did not fireReceived: %d Int: %d Start: %d Status: %d\n"
+ "IOMFB DEBUG PANIC: TE watchdog Int: %d Start: %d Status: %d"
+ "IOMFB: %s called without active transaction populated\n"
+ "IOMFB: %s invalid blitter info [ptr %d ID %d num_blits %d]\n"
+ "IOMFB: %s previous submitting swap not cleared\n"
+ "iomfb_keep_trinity_enabled_on_ui"
+ "iomfb_swap_submit_split_enable"
+ "swap_submit_dcp_blitter"
+ "swap_submit_dcp_main"
+ "swap_submit_finish"
+ "virtual IOMFBStatus IOMobileFramebuffer::swap_submit_dcp_main(const IOMFBSwap *, IOMFB::Surface **, const dva_t *, const dva_t *, bool, double, dva_t, bool, uint32_t, bool *, const uint32_t *, uint32_t *)"
- "// off -> on"
- "A436_callback__"
- "A437_callback__"
- "HPDMonitor: %s: isPlug:%d un/plug.aborted: %d%d un/plug.notified:%d%d unplug.was_called:%d \n"
- "UnifiedPipeline.h"
- "VideoInterface::Plug"
- "VideoInterface::Unplug"
- "VideoInterface::Unplug Aborting unplug since plug was aborted previously"
- "VideoInterface::Unplug Dropping this hotplug since system is powering down"
- "VideoInterface::Unplug x"
- "invoke_hotplug_event"
- "plug "

```

#### t8130dcp_restore.im4p

>  `t8130dcp_restore.im4p`

```diff

 
-  __TEXT.__text: 0x2deed8
-  __TEXT.__const: 0x7cf58
-  __TEXT.__cstring: 0x30e8b
+  __TEXT.__text: 0x2e1004
+  __TEXT.__const: 0x7d828
+  __TEXT.__cstring: 0x3103f
   __TEXT.__chain_starts: 0x68
   __DATA.__constructor: 0x8
-  __DATA.__const: 0x4a498
+  __DATA.__const: 0x4a528
   __DATA._rtk_patchbay: 0x710
   __DATA._rtk_data_uuid: 0x40
   __DATA.__data: 0x2b524

   __DATA._afk_sys_objt: 0xbb0
   __DATA._rtk_mtab: 0x5c8
   __DATA.__zerofill: 0x9b230
-  __OS_LOG.__string: 0x20ff2
-  Functions: 6841
+  __OS_LOG.__string: 0x21015
+  Functions: 6852
   Symbols:   0
-  CStrings:  6134
+  CStrings:  6138
 
CStrings:
+ "%s: VideoInterface::Plug IOMFBStatusNotReady\n"
+ "%s: VideoInterface::Unplug IOMFBStatusNotReady\n"
+ "A439_callback__"
+ "A442_callback__"
+ "Dropping this hotplug since system is powering down or previous plug was aborted : %d"
+ "IOMFB %s: TE did not fireReceived: %d Int: %d Start: %d Status: %d\n"
+ "IOMFB DEBUG PANIC: TE watchdog Int: %d Start: %d Status: %d"
+ "IOMFB: %s called without active transaction populated\n"
+ "IOMFB: %s invalid blitter info [ptr %d ID %d num_blits %d]\n"
+ "IOMFB: %s previous submitting swap not cleared\n"
+ "iomfb_keep_trinity_enabled_on_ui"
+ "iomfb_swap_submit_split_enable"
+ "swap_submit_dcp_blitter"
+ "swap_submit_dcp_main"
+ "swap_submit_finish"
+ "virtual IOMFBStatus IOMobileFramebuffer::swap_submit_dcp_main(const IOMFBSwap *, IOMFB::Surface **, const dva_t *, const dva_t *, bool, double, dva_t, bool, uint32_t, bool *, const uint32_t *, uint32_t *)"
- "// off -> on"
- "A436_callback__"
- "A437_callback__"
- "HPDMonitor: %s: isPlug:%d un/plug.aborted: %d%d un/plug.notified:%d%d unplug.was_called:%d \n"
- "UnifiedPipeline.h"
- "VideoInterface::Plug"
- "VideoInterface::Unplug"
- "VideoInterface::Unplug Aborting unplug since plug was aborted previously"
- "VideoInterface::Unplug Dropping this hotplug since system is powering down"
- "VideoInterface::Unplug x"
- "invoke_hotplug_event"
- "plug "

```

#### txm.iphoneos.release.im4p

>  `txm.iphoneos.release.im4p`

```diff

-135.0.10.0.0
-  __TEXT.__cstring: 0x56eb
+135.2.1.0.0
+  __TEXT.__cstring: 0x570f
   __TEXT.__const: 0x4210
   __TEXT.__binname: 0x40
   __TEXT.__chain_starts: 0x20
   __DATA_CONST.__auth_ptr: 0x50
-  __DATA_CONST.__const: 0x7c78
+  __DATA_CONST.__const: 0x7c80
   __TEXT_EXEC.__text: 0x3f39c
   __TEXT_BOOT_EXEC.__text: 0x4058
   __TEXT_BOOT_EXEC.__bootcode: 0x2c

   __LATE_CONST.__late_const: 0xa8
   Functions: 888
   Symbols:   1
-  CStrings:  707
+  CStrings:  708
 
CStrings:
+ "8ae887e0-8d30-448a-b10d-0312c5b71f05"
+ "@(#)VERSION:Code Signing Monitor Image4 Module Version 7.0.0: Thu Aug  8 00:51:14 PDT 2024; root:AppleImage4_txm-320.0.11~1479/libimage4_TXM/RELEASE_ARM64E"
+ "Code Signing Monitor Image4 Module Version 7.0.0: Thu Aug  8 00:51:14 PDT 2024; root:AppleImage4_txm-320.0.11~1479/libimage4_TXM/RELEASE_ARM64E"
+ "txm.iphoneos.release.TrustedExecutionMonitor_Guarded-135.2.1"
- "@(#)VERSION:Code Signing Monitor Image4 Module Version 7.0.0: Fri Jul 26 19:27:48 PDT 2024; root:AppleImage4_txm-320.0.11~1285/libimage4_TXM/RELEASE_ARM64E"
- "Code Signing Monitor Image4 Module Version 7.0.0: Fri Jul 26 19:27:48 PDT 2024; root:AppleImage4_txm-320.0.11~1285/libimage4_TXM/RELEASE_ARM64E"
- "txm.iphoneos.release.TrustedExecutionMonitor_Guarded-135.0.10"

```


</details>

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 18.0 *(22A5326f)* | 619.1.24.10.2 |
| 18.0 *(22A5338b)* | 619.1.26.30.2 |

### Dylibs

#### 🆕 NEW (1)

- `/System/Library/AccessibilityBundles/FontServices.axbundle/FontServices`

#### ❌ Removed (1)

- `/System/Library/VideoProcessors/FPDisparityV3.bundle/FPDisparityV3`

#### ⬆️ Updated (1158)

<details>
  <summary><i>View Updated</i></summary>

- [/System/Library/AccessibilityBundles/AVKit.axbundle/AVKit](DYLIBS/AVKit.md)
- [/System/Library/AccessibilityBundles/AccessibilitySettingsLoader.bundle/AccessibilitySettingsLoader](DYLIBS/AccessibilitySettingsLoader.md)
- [/System/Library/AccessibilityBundles/BackBoard.axbundle/BackBoard](DYLIBS/BackBoard.md)
- [/System/Library/AccessibilityBundles/Bridge.axbundle/Bridge](DYLIBS/Bridge.md)
- [/System/Library/AccessibilityBundles/CameraEditKitFramework.axbundle/CameraEditKitFramework](DYLIBS/CameraEditKitFramework.md)
- [/System/Library/AccessibilityBundles/CameraUI.axbundle/CameraUI](DYLIBS/CameraUI.md)
- [/System/Library/AccessibilityBundles/ChatKitFramework.axbundle/ChatKitFramework](DYLIBS/ChatKitFramework.md)
- [/System/Library/AccessibilityBundles/ContactsAutocompleteUI.axbundle/ContactsAutocompleteUI](DYLIBS/ContactsAutocompleteUI.md)
- [/System/Library/AccessibilityBundles/ControlCenterUI.axbundle/ControlCenterUI](DYLIBS/ControlCenterUI.md)
- [/System/Library/AccessibilityBundles/EventKitUIFramework.axbundle/EventKitUIFramework](DYLIBS/EventKitUIFramework.md)
- [/System/Library/AccessibilityBundles/KeyboardSettings.axbundle/KeyboardSettings](DYLIBS/KeyboardSettings.md)
- [/System/Library/AccessibilityBundles/MailUI.axbundle/MailUI](DYLIBS/MailUI.md)
- [/System/Library/AccessibilityBundles/MapKitFramework.axbundle/MapKitFramework](DYLIBS/MapKitFramework.md)
- [/System/Library/AccessibilityBundles/MobileCal.axbundle/MobileCal](DYLIBS/MobileCal.md)
- [/System/Library/AccessibilityBundles/MobileMail.axbundle/MobileMail](DYLIBS/MobileMail.md)
- [/System/Library/AccessibilityBundles/MobileSafariFramework.axbundle/MobileSafariFramework](DYLIBS/MobileSafariFramework.md)
- [/System/Library/AccessibilityBundles/MobileSafariUI.axbundle/MobileSafariUI](DYLIBS/MobileSafariUI.md)
- [/System/Library/AccessibilityBundles/PassKitUI.axbundle/PassKitUI](DYLIBS/PassKitUI.md)
- [/System/Library/AccessibilityBundles/PhotosUICore.axbundle/PhotosUICore](DYLIBS/PhotosUICore.md)
- [/System/Library/AccessibilityBundles/PhotosUIFramework.axbundle/PhotosUIFramework](DYLIBS/PhotosUIFramework.md)
- [/System/Library/AccessibilityBundles/Podcasts.axbundle/Podcasts](DYLIBS/Podcasts.md)
- [/System/Library/AccessibilityBundles/PosterKit.axbundle/PosterKit](DYLIBS/PosterKit.md)
- [/System/Library/AccessibilityBundles/PosterUIFoundation.axbundle/PosterUIFoundation](DYLIBS/PosterUIFoundation.md)
- [/System/Library/AccessibilityBundles/Preferences.axbundle/Preferences](DYLIBS/Preferences.md)
- [/System/Library/AccessibilityBundles/QuickSpeak.bundle/QuickSpeak](DYLIBS/QuickSpeak.md)
- [/System/Library/AccessibilityBundles/Setup.axbundle/Setup](DYLIBS/Setup.md)
- [/System/Library/AccessibilityBundles/SpringBoard.axbundle/SpringBoard](DYLIBS/SpringBoard.md)
- [/System/Library/AccessibilityBundles/SpringBoardHome.axbundle/SpringBoardHome](DYLIBS/SpringBoardHome.md)
- [/System/Library/AccessibilityBundles/UIKit.axbundle/UIKit](DYLIBS/UIKit.md)
- [/System/Library/AccessibilityBundles/VideosUIFramework.axbundle/VideosUIFramework](DYLIBS/VideosUIFramework.md)
- [/System/Library/AccessibilityBundles/WebCore.axbundle/WebCore](DYLIBS/WebCore.md)
- [/System/Library/AccessibilityBundles/WebKit.axbundle/WebKit](DYLIBS/WebKit.md)
- [/System/Library/Accounts/Authentication/AppleIDAuthentication.bundle/AppleIDAuthentication](DYLIBS/AppleIDAuthentication.md)
- [/System/Library/Accounts/Notification/CDPAccountNotificationPlugin_IOS.bundle/CDPAccountNotificationPlugin_IOS](DYLIBS/CDPAccountNotificationPlugin_IOS.md)
- [/System/Library/Accounts/Notification/KeychainSyncAccountNotification.bundle/KeychainSyncAccountNotification](DYLIBS/KeychainSyncAccountNotification.md)
- [/System/Library/Assistant/UIPlugins/SiriFindMyUIPlugin.siriUIBundle/Frameworks/SiriFindMyUI.framework/SiriFindMyUI](DYLIBS/SiriFindMyUI.md)
- [/System/Library/ControlCenter/Bundles/AccessibilityHeadphoneLevelsControlCenterModule.bundle/AccessibilityHeadphoneLevelsControlCenterModule](DYLIBS/AccessibilityHeadphoneLevelsControlCenterModule.md)
- [/System/Library/ControlCenter/Bundles/AccessibilityTextSizeModule.bundle/AccessibilityTextSizeModule](DYLIBS/AccessibilityTextSizeModule.md)
- [/System/Library/ControlCenter/Bundles/ConnectivityModule.bundle/ConnectivityModule](DYLIBS/ConnectivityModule.md)
- [/System/Library/ControlCenter/Bundles/HearingDevicesCCModule.bundle/HearingDevicesCCModule](DYLIBS/HearingDevicesCCModule.md)
- [/System/Library/ControlCenter/Bundles/HomeControlCenterModule.bundle/HomeControlCenterModule](DYLIBS/HomeControlCenterModule.md)
- [/System/Library/ControlCenter/Bundles/TimerModule.bundle/TimerModule](DYLIBS/TimerModule.md)
- [/System/Library/CoreAccessories/PlugIns/Features/Communications-iOS.feature/Communications-iOS](DYLIBS/Communications-iOS.md)
- [/System/Library/CoreAccessories/PlugIns/Platform/IOKit.platform/IOKit](DYLIBS/IOKit.md)
- [/System/Library/CoreAccessories/PlugIns/Transports/IOAccessoryManager.transport/IOAccessoryManager](DYLIBS/IOAccessoryManager.md)
- [/System/Library/CoreAccessories/PlugIns/Transports/NFC.transport/NFC](DYLIBS/NFC.md)
- [/System/Library/CoreAccessories/PlugIns/Transports/USBHost.transport/USBHost](DYLIBS/USBHost.md)
- [/System/Library/CoreServices/RawCamera.bundle/RawCamera](DYLIBS/RawCamera.md)
- [/System/Library/Extensions/AGXMetalG16P_A0.bundle/AGXMetalG16P_A0](DYLIBS/AGXMetalG16P_A0.md)
- [/System/Library/Extensions/AGXMetalG16P_B0.bundle/AGXMetalG16P_B0](DYLIBS/AGXMetalG16P_B0.md)
- [/System/Library/Frameworks/AVFAudio.framework/AVFAudio](DYLIBS/AVFAudio.md)
- [/System/Library/Frameworks/AVKit.framework/AVKit](DYLIBS/AVKit.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vImage.framework/vImage](DYLIBS/vImage.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libBLAS.dylib](DYLIBS/libBLAS.dylib.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libBNNS.dylib](DYLIBS/libBNNS.dylib.md)
- [/System/Library/Frameworks/AccessorySetupKit.framework/AccessorySetupKit](DYLIBS/AccessorySetupKit.md)
- [/System/Library/Frameworks/Accounts.framework/Accounts](DYLIBS/Accounts.md)
- [/System/Library/Frameworks/ActivityKit.framework/ActivityKit](DYLIBS/ActivityKit.md)
- [/System/Library/Frameworks/AppIntents.framework/AppIntents](DYLIBS/AppIntents.md)
- [/System/Library/Frameworks/AppTrackingTransparency.framework/AppTrackingTransparency](DYLIBS/AppTrackingTransparency.md)
- [/System/Library/Frameworks/Assignables.framework/Assignables](DYLIBS/Assignables.md)
- [/System/Library/Frameworks/AudioToolbox.framework/AudioCodecs](DYLIBS/AudioCodecs.md)
- [/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox](DYLIBS/AudioToolbox.md)
- [/System/Library/Frameworks/AudioToolbox.framework/libAudioDSP.dylib](DYLIBS/libAudioDSP.dylib.md)
- [/System/Library/Frameworks/AudioToolbox.framework/libEmbeddedSystemAUs.dylib](DYLIBS/libEmbeddedSystemAUs.dylib.md)
- [/System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices](DYLIBS/AuthenticationServices.md)
- [/System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/Frameworks/AACClient.framework/AACClient](DYLIBS/AACClient.md)
- [/System/Library/Frameworks/BrowserEngineKit.framework/BrowserEngineKit](DYLIBS/BrowserEngineKit.md)
- [/System/Library/Frameworks/CFNetwork.framework/CFNetwork](DYLIBS/CFNetwork.md)
- [/System/Library/Frameworks/CarPlay.framework/CarPlay](DYLIBS/CarPlay.md)
- [/System/Library/Frameworks/Charts.framework/Charts](DYLIBS/Charts.md)
- [/System/Library/Frameworks/ClockKit.framework/ClockKit](DYLIBS/ClockKit.md)
- [/System/Library/Frameworks/CloudKit.framework/CloudKit](DYLIBS/CloudKit.md)
- [/System/Library/Frameworks/Combine.framework/Combine](DYLIBS/Combine.md)
- [/System/Library/Frameworks/ContactProvider.framework/ContactProvider](DYLIBS/ContactProvider.md)
- [/System/Library/Frameworks/Contacts.framework/Contacts](DYLIBS/Contacts.md)
- [/System/Library/Frameworks/ContactsUI.framework/ContactsUI](DYLIBS/ContactsUI.md)
- [/System/Library/Frameworks/CoreAudio.framework/CoreAudio](DYLIBS/CoreAudio.md)
- [/System/Library/Frameworks/CoreAudioKit.framework/CoreAudioKit](DYLIBS/CoreAudioKit.md)
- [/System/Library/Frameworks/CoreData.framework/CoreData](DYLIBS/CoreData.md)
- [/System/Library/Frameworks/CoreGraphics.framework/CoreGraphics](DYLIBS/CoreGraphics.md)
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
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterBase.dylib](DYLIBS/libCommCenterBase.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterCommandDrivers.dylib](DYLIBS/libCommCenterCommandDrivers.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterKCommandDrivers.dylib](DYLIBS/libCommCenterKCommandDrivers.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterMCommandDrivers.dylib](DYLIBS/libCommCenterMCommandDrivers.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libSystemDetermination.dylib](DYLIBS/libSystemDetermination.dylib.md)
- [/System/Library/Frameworks/CoreTransferable.framework/CoreTransferable](DYLIBS/CoreTransferable.md)
- [/System/Library/Frameworks/CoreVideo.framework/CoreVideo](DYLIBS/CoreVideo.md)
- [/System/Library/Frameworks/CreateML.framework/CreateML](DYLIBS/CreateML.md)
- [/System/Library/Frameworks/CreateMLComponents.framework/CreateMLComponents](DYLIBS/CreateMLComponents.md)
- [/System/Library/Frameworks/CryptoKit.framework/CryptoKit](DYLIBS/CryptoKit.md)
- [/System/Library/Frameworks/DeveloperToolsSupport.framework/DeveloperToolsSupport](DYLIBS/DeveloperToolsSupport.md)
- [/System/Library/Frameworks/DeviceActivity.framework/DeviceActivity](DYLIBS/DeviceActivity.md)
- [/System/Library/Frameworks/EventKit.framework/EventKit](DYLIBS/EventKit.md)
- [/System/Library/Frameworks/EventKitUI.framework/EventKitUI](DYLIBS/EventKitUI.md)
- [/System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation](DYLIBS/ExtensionFoundation.md)
- [/System/Library/Frameworks/FinanceKit.framework/FinanceKit](DYLIBS/FinanceKit.md)
- [/System/Library/Frameworks/FinanceKitUI.framework/FinanceKitUI](DYLIBS/FinanceKitUI.md)
- [/System/Library/Frameworks/Foundation.framework/Foundation](DYLIBS/Foundation.md)
- [/System/Library/Frameworks/GameKit.framework/GameKit](DYLIBS/GameKit.md)
- [/System/Library/Frameworks/HealthKit.framework/HealthKit](DYLIBS/HealthKit.md)
- [/System/Library/Frameworks/ImageIO.framework/ImageIO](DYLIBS/ImageIO.md)
- [/System/Library/Frameworks/Intents.framework/Intents](DYLIBS/Intents.md)
- [/System/Library/Frameworks/JavaScriptCore.framework/JavaScriptCore](DYLIBS/JavaScriptCore.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication](DYLIBS/LocalAuthentication.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismBase.framework/MechanismBase](DYLIBS/MechanismBase.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/SharedUtils.framework/SharedUtils](DYLIBS/SharedUtils.md)
- [/System/Library/Frameworks/ManagedSettings.framework/ManagedSettings](DYLIBS/ManagedSettings.md)
- [/System/Library/Frameworks/MapKit.framework/MapKit](DYLIBS/MapKit.md)
- [/System/Library/Frameworks/MarketplaceKit.framework/MarketplaceKit](DYLIBS/MarketplaceKit.md)
- [/System/Library/Frameworks/Matter.framework/Matter](DYLIBS/Matter.md)
- [/System/Library/Frameworks/MediaPlayer.framework/MediaPlayer](DYLIBS/MediaPlayer.md)
- [/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox](DYLIBS/MediaToolbox.md)
- [/System/Library/Frameworks/MessageUI.framework/MessageUI](DYLIBS/MessageUI.md)
- [/System/Library/Frameworks/Messages.framework/Messages](DYLIBS/Messages.md)
- [/System/Library/Frameworks/Metal.framework/Metal](DYLIBS/Metal.md)
- [/System/Library/Frameworks/MetalFX.framework/MetalFX](DYLIBS/MetalFX.md)
- [/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSBenchmarkLoop.framework/MPSBenchmarkLoop](DYLIBS/MPSBenchmarkLoop.md)
- [/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNDArray.framework/MPSNDArray](DYLIBS/MPSNDArray.md)
- [/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph](DYLIBS/MetalPerformanceShadersGraph.md)
- [/System/Library/Frameworks/MetricKit.framework/MetricKit](DYLIBS/MetricKit.md)
- [/System/Library/Frameworks/ModelIO.framework/ModelIO](DYLIBS/ModelIO.md)
- [/System/Library/Frameworks/MusicKit.framework/MusicKit](DYLIBS/MusicKit.md)
- [/System/Library/Frameworks/Network.framework/Network](DYLIBS/Network.md)
- [/System/Library/Frameworks/PDFKit.framework/PDFKit](DYLIBS/PDFKit.md)
- [/System/Library/Frameworks/PencilKit.framework/PencilKit](DYLIBS/PencilKit.md)
- [/System/Library/Frameworks/Photos.framework/Photos](DYLIBS/Photos.md)
- [/System/Library/Frameworks/PhotosUI.framework/PhotosUI](DYLIBS/PhotosUI.md)
- [/System/Library/Frameworks/ProximityReader.framework/ProximityReader](DYLIBS/ProximityReader.md)
- [/System/Library/Frameworks/QuartzCore.framework/QuartzCore](DYLIBS/QuartzCore.md)
- [/System/Library/Frameworks/QuickLook.framework/QuickLook](DYLIBS/QuickLook.md)
- [/System/Library/Frameworks/QuickLookThumbnailing.framework/QuickLookThumbnailing](DYLIBS/QuickLookThumbnailing.md)
- [/System/Library/Frameworks/RealityFoundation.framework/RealityFoundation](DYLIBS/RealityFoundation.md)
- [/System/Library/Frameworks/RealityKit.framework/RealityKit](DYLIBS/RealityKit.md)
- [/System/Library/Frameworks/RoomPlan.framework/RoomPlan](DYLIBS/RoomPlan.md)
- [/System/Library/Frameworks/SafariServices.framework/SafariServices](DYLIBS/SafariServices.md)
- [/System/Library/Frameworks/SceneKit.framework/SceneKit](DYLIBS/SceneKit.md)
- [/System/Library/Frameworks/Security.framework/Security](DYLIBS/Security.md)
- [/System/Library/Frameworks/SharedWithYou.framework/SharedWithYou](DYLIBS/SharedWithYou.md)
- [/System/Library/Frameworks/ShazamKit.framework/ShazamKit](DYLIBS/ShazamKit.md)
- [/System/Library/Frameworks/SoundAnalysis.framework/SoundAnalysis](DYLIBS/SoundAnalysis.md)
- [/System/Library/Frameworks/Speech.framework/Speech](DYLIBS/Speech.md)
- [/System/Library/Frameworks/StickerKit.framework/StickerKit](DYLIBS/StickerKit.md)
- [/System/Library/Frameworks/StoreKit.framework/StoreKit](DYLIBS/StoreKit.md)
- [/System/Library/Frameworks/SwiftData.framework/SwiftData](DYLIBS/SwiftData.md)
- [/System/Library/Frameworks/SwiftUI.framework/SwiftUI](DYLIBS/SwiftUI.md)
- [/System/Library/Frameworks/SwiftUICore.framework/SwiftUICore](DYLIBS/SwiftUICore.md)
- [/System/Library/Frameworks/TabularData.framework/TabularData](DYLIBS/TabularData.md)
- [/System/Library/Frameworks/TipKit.framework/TipKit](DYLIBS/TipKit.md)
- [/System/Library/Frameworks/VideoToolbox.framework/VideoToolbox](DYLIBS/VideoToolbox.md)
- [/System/Library/Frameworks/Vision.framework/Vision](DYLIBS/Vision.md)
- [/System/Library/Frameworks/WebKit.framework/WebKit](DYLIBS/WebKit.md)
- [/System/Library/Frameworks/WidgetKit.framework/WidgetKit](DYLIBS/WidgetKit.md)
- [/System/Library/Frameworks/WorkoutKit.framework/WorkoutKit](DYLIBS/WorkoutKit.md)
- [/System/Library/Frameworks/_AppIntents_SwiftUI.framework/_AppIntents_SwiftUI](DYLIBS/_AppIntents_SwiftUI.md)
- [/System/Library/Frameworks/_AppIntents_UIKit.framework/_AppIntents_UIKit](DYLIBS/_AppIntents_UIKit.md)
- [/System/Library/Frameworks/_DeviceActivity_SwiftUI.framework/_DeviceActivity_SwiftUI](DYLIBS/_DeviceActivity_SwiftUI.md)
- [/System/Library/Frameworks/_MapKit_SwiftUI.framework/_MapKit_SwiftUI](DYLIBS/_MapKit_SwiftUI.md)
- [/System/Library/Frameworks/_MusicKit_SwiftUI.framework/_MusicKit_SwiftUI](DYLIBS/_MusicKit_SwiftUI.md)
- [/System/Library/Frameworks/_PassKit_SwiftUI.framework/_PassKit_SwiftUI](DYLIBS/_PassKit_SwiftUI.md)
- [/System/Library/Frameworks/_PhotosUI_SwiftUI.framework/_PhotosUI_SwiftUI](DYLIBS/_PhotosUI_SwiftUI.md)
- [/System/Library/Frameworks/_QuickLook_SwiftUI.framework/_QuickLook_SwiftUI](DYLIBS/_QuickLook_SwiftUI.md)
- [/System/Library/Frameworks/_RealityKit_SwiftUI.framework/_RealityKit_SwiftUI](DYLIBS/_RealityKit_SwiftUI.md)
- [/System/Library/Frameworks/_StoreKit_SwiftUI.framework/_StoreKit_SwiftUI](DYLIBS/_StoreKit_SwiftUI.md)
- [/System/Library/Frameworks/_SwiftData_SwiftUI.framework/_SwiftData_SwiftUI](DYLIBS/_SwiftData_SwiftUI.md)
- [/System/Library/Frameworks/_Translation_SwiftUI.framework/_Translation_SwiftUI](DYLIBS/_Translation_SwiftUI.md)
- [/System/Library/Health/FeedItemPlugins/HearingAppPlugin.healthplugin/HearingAppPlugin](DYLIBS/HearingAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/Heart.healthplugin/Heart](DYLIBS/Heart.md)
- [/System/Library/Health/FeedItemPlugins/Highlights.healthplugin/Highlights](DYLIBS/Highlights.md)
- [/System/Library/Health/FeedItemPlugins/MedicationsHealthAppPlugin.healthplugin/MedicationsHealthAppPlugin](DYLIBS/MedicationsHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/MenstrualCyclesAppPlugin.healthplugin/MenstrualCyclesAppPlugin](DYLIBS/MenstrualCyclesAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/Profiles.healthplugin/Profiles](DYLIBS/Profiles.md)
- [/System/Library/Health/FeedItemPlugins/RespiratoryHealthAppPlugin.healthplugin/RespiratoryHealthAppPlugin](DYLIBS/RespiratoryHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/Safety.healthplugin/Safety](DYLIBS/Safety.md)
- [/System/Library/Health/FeedItemPlugins/SleepHealthAppPlugin.healthplugin/SleepHealthAppPlugin](DYLIBS/SleepHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/Summaries.healthplugin/Summaries](DYLIBS/Summaries.md)
- [/System/Library/Health/FeedItemPlugins/VisionHealthAppPlugin.healthplugin/VisionHealthAppPlugin](DYLIBS/VisionHealthAppPlugin.md)
- [/System/Library/MediaCapture/H16ISP.mediacapture](DYLIBS/H16ISP.mediacapture.md)
- [/System/Library/Messages/PlugIns/FaceTime.imservice/FaceTime](DYLIBS/FaceTime.md)
- [/System/Library/NanoPreferenceBundles/General/AccessibilitySettings.bundle/AccessibilitySettings](DYLIBS/AccessibilitySettings.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/MessagesComplication.bundle/MessagesComplication](DYLIBS/MessagesComplication.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKEsterbrookFaceBundleCompanion.bundle/NTKEsterbrookFaceBundleCompanion](DYLIBS/NTKEsterbrookFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKParmesanFaceBundleCompanion.bundle/NTKParmesanFaceBundleCompanion](DYLIBS/NTKParmesanFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKRhizomeFaceBundleCompanion.bundle/NTKRhizomeFaceBundleCompanion](DYLIBS/NTKRhizomeFaceBundleCompanion.md)
- [/System/Library/PreferenceBundles/BluetoothSettings.bundle/BluetoothSettings](DYLIBS/BluetoothSettings.md)
- [/System/Library/PreferenceBundles/KeyboardSettings.bundle/KeyboardSettings](DYLIBS/KeyboardSettings.md)
- [/System/Library/PrivateFrameworks/AAAFoundation.framework/AAAFoundation](DYLIBS/AAAFoundation.md)
- [/System/Library/PrivateFrameworks/AAAFoundationSwift.framework/AAAFoundationSwift](DYLIBS/AAAFoundationSwift.md)
- [/System/Library/PrivateFrameworks/AACCore.framework/AACCore](DYLIBS/AACCore.md)
- [/System/Library/PrivateFrameworks/ABMHelper.framework/ABMHelper](DYLIBS/ABMHelper.md)
- [/System/Library/PrivateFrameworks/ACSEFoundation.framework/ACSEFoundation](DYLIBS/ACSEFoundation.md)
- [/System/Library/PrivateFrameworks/AGXCompilerCore.framework/AGXCompilerCore](DYLIBS/AGXCompilerCore.md)
- [/System/Library/PrivateFrameworks/AIMLExperimentationAnalytics.framework/AIMLExperimentationAnalytics](DYLIBS/AIMLExperimentationAnalytics.md)
- [/System/Library/PrivateFrameworks/ANECompiler.framework/ANECompiler](DYLIBS/ANECompiler.md)
- [/System/Library/PrivateFrameworks/APFS.framework/APFS](DYLIBS/APFS.md)
- [/System/Library/PrivateFrameworks/APFoundation.framework/APFoundation](DYLIBS/APFoundation.md)
- [/System/Library/PrivateFrameworks/APTransport.framework/APTransport](DYLIBS/APTransport.md)
- [/System/Library/PrivateFrameworks/ASRBridge.framework/ASRBridge](DYLIBS/ASRBridge.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/AVConference](DYLIBS/AVConference.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ViceroyTrace.framework/ViceroyTrace](DYLIBS/ViceroyTrace.md)
- [/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture](DYLIBS/AVFCapture.md)
- [/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore](DYLIBS/AVFCore.md)
- [/System/Library/PrivateFrameworks/AXCoreUtilities.framework/AXCoreUtilities](DYLIBS/AXCoreUtilities.md)
- [/System/Library/PrivateFrameworks/AXMediaUtilities.framework/AXMediaUtilities](DYLIBS/AXMediaUtilities.md)
- [/System/Library/PrivateFrameworks/AXRuntime.framework/AXRuntime](DYLIBS/AXRuntime.md)
- [/System/Library/PrivateFrameworks/AXSpringBoardServerInstance.framework/AXSpringBoardServerInstance](DYLIBS/AXSpringBoardServerInstance.md)
- [/System/Library/PrivateFrameworks/AXWatchRemoteScreenUI.framework/AXWatchRemoteScreenUI](DYLIBS/AXWatchRemoteScreenUI.md)
- [/System/Library/PrivateFrameworks/AccessibilityAudit.framework/AccessibilityAudit](DYLIBS/AccessibilityAudit.md)
- [/System/Library/PrivateFrameworks/AccessibilityPhysicalInteraction.framework/AccessibilityPhysicalInteraction](DYLIBS/AccessibilityPhysicalInteraction.md)
- [/System/Library/PrivateFrameworks/AccessibilitySettingsUI.framework/AccessibilitySettingsUI](DYLIBS/AccessibilitySettingsUI.md)
- [/System/Library/PrivateFrameworks/AccessibilitySharedUISupport.framework/AccessibilitySharedUISupport](DYLIBS/AccessibilitySharedUISupport.md)
- [/System/Library/PrivateFrameworks/AccessibilityUIService.framework/AccessibilityUIService](DYLIBS/AccessibilityUIService.md)
- [/System/Library/PrivateFrameworks/AccessibilityUIUtilities.framework/AccessibilityUIUtilities](DYLIBS/AccessibilityUIUtilities.md)
- [/System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities](DYLIBS/AccessibilityUtilities.md)
- [/System/Library/PrivateFrameworks/AccessoryiAP2Shim.framework/AccessoryiAP2Shim](DYLIBS/AccessoryiAP2Shim.md)
- [/System/Library/PrivateFrameworks/AccountsDaemon.framework/AccountsDaemon](DYLIBS/AccountsDaemon.md)
- [/System/Library/PrivateFrameworks/AccountsUISettings.framework/AccountsUISettings](DYLIBS/AccountsUISettings.md)
- [/System/Library/PrivateFrameworks/ActionButtonConfigurationUI.framework/ActionButtonConfigurationUI](DYLIBS/ActionButtonConfigurationUI.md)
- [/System/Library/PrivateFrameworks/ActionButtonSelector.framework/ActionButtonSelector](DYLIBS/ActionButtonSelector.md)
- [/System/Library/PrivateFrameworks/ActionKit.framework/ActionKit](DYLIBS/ActionKit.md)
- [/System/Library/PrivateFrameworks/ActionKitUI.framework/ActionKitUI](DYLIBS/ActionKitUI.md)
- [/System/Library/PrivateFrameworks/ActionPredictionHeuristicsInternal.framework/ActionPredictionHeuristicsInternal](DYLIBS/ActionPredictionHeuristicsInternal.md)
- [/System/Library/PrivateFrameworks/ActivitySharingDaemonCore.framework/ActivitySharingDaemonCore](DYLIBS/ActivitySharingDaemonCore.md)
- [/System/Library/PrivateFrameworks/ActivitySharingServices.framework/ActivitySharingServices](DYLIBS/ActivitySharingServices.md)
- [/System/Library/PrivateFrameworks/ActivityUIServices.framework/ActivityUIServices](DYLIBS/ActivityUIServices.md)
- [/System/Library/PrivateFrameworks/AdPlatformsCommonUI.framework/AdPlatformsCommonUI](DYLIBS/AdPlatformsCommonUI.md)
- [/System/Library/PrivateFrameworks/AdaptiveVoiceShortcuts.framework/AdaptiveVoiceShortcuts](DYLIBS/AdaptiveVoiceShortcuts.md)
- [/System/Library/PrivateFrameworks/AddressBookLegacy.framework/AddressBookLegacy](DYLIBS/AddressBookLegacy.md)
- [/System/Library/PrivateFrameworks/AeroML.framework/AeroML](DYLIBS/AeroML.md)
- [/System/Library/PrivateFrameworks/AirPlayAndHandoffSettingsSupport.framework/AirPlayAndHandoffSettingsSupport](DYLIBS/AirPlayAndHandoffSettingsSupport.md)
- [/System/Library/PrivateFrameworks/AirPlayKit.framework/AirPlayKit](DYLIBS/AirPlayKit.md)
- [/System/Library/PrivateFrameworks/AirPlayReceiver.framework/AirPlayReceiver](DYLIBS/AirPlayReceiver.md)
- [/System/Library/PrivateFrameworks/AirPlayReceiverKit.framework/AirPlayReceiverKit](DYLIBS/AirPlayReceiverKit.md)
- [/System/Library/PrivateFrameworks/AirPlaySender.framework/AirPlaySender](DYLIBS/AirPlaySender.md)
- [/System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport](DYLIBS/AirPlaySupport.md)
- [/System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit](DYLIBS/AltruisticBodyPoseKit.md)
- [/System/Library/PrivateFrameworks/AmbientUI.framework/AmbientUI](DYLIBS/AmbientUI.md)
- [/System/Library/PrivateFrameworks/Announce.framework/Announce](DYLIBS/Announce.md)
- [/System/Library/PrivateFrameworks/AnnounceDaemon.framework/AnnounceDaemon](DYLIBS/AnnounceDaemon.md)
- [/System/Library/PrivateFrameworks/AppAnalytics.framework/AppAnalytics](DYLIBS/AppAnalytics.md)
- [/System/Library/PrivateFrameworks/AppDistribution.framework/AppDistribution](DYLIBS/AppDistribution.md)
- [/System/Library/PrivateFrameworks/AppIntentsServices.framework/AppIntentsServices](DYLIBS/AppIntentsServices.md)
- [/System/Library/PrivateFrameworks/AppPlaceholderSync.framework/AppPlaceholderSync](DYLIBS/AppPlaceholderSync.md)
- [/System/Library/PrivateFrameworks/AppPredictionClient.framework/AppPredictionClient](DYLIBS/AppPredictionClient.md)
- [/System/Library/PrivateFrameworks/AppPredictionFoundation.framework/AppPredictionFoundation](DYLIBS/AppPredictionFoundation.md)
- [/System/Library/PrivateFrameworks/AppPredictionInternal.framework/AppPredictionInternal](DYLIBS/AppPredictionInternal.md)
- [/System/Library/PrivateFrameworks/AppProtection.framework/AppProtection](DYLIBS/AppProtection.md)
- [/System/Library/PrivateFrameworks/AppProtectionUI.framework/AppProtectionUI](DYLIBS/AppProtectionUI.md)
- [/System/Library/PrivateFrameworks/AppServerSupport.framework/AppServerSupport](DYLIBS/AppServerSupport.md)
- [/System/Library/PrivateFrameworks/AppStoreComponents.framework/AppStoreComponents](DYLIBS/AppStoreComponents.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon](DYLIBS/AppStoreDaemon.md)
- [/System/Library/PrivateFrameworks/AppStoreKitInternal.framework/AppStoreKitInternal](DYLIBS/AppStoreKitInternal.md)
- [/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount](DYLIBS/AppleAccount.md)
- [/System/Library/PrivateFrameworks/AppleAccountUI.framework/AppleAccountUI](DYLIBS/AppleAccountUI.md)
- [/System/Library/PrivateFrameworks/AppleBasebandServices.framework/AppleBasebandServices](DYLIBS/AppleBasebandServices.md)
- [/System/Library/PrivateFrameworks/AppleCV3DModels.framework/AppleCV3DModels](DYLIBS/AppleCV3DModels.md)
- [/System/Library/PrivateFrameworks/AppleCVAPhoto.framework/AppleCVAPhoto](DYLIBS/AppleCVAPhoto.md)
- [/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/AppleDeviceQuerySupport](DYLIBS/AppleDeviceQuerySupport.md)
- [/System/Library/PrivateFrameworks/AppleIDSetup.framework/AppleIDSetup](DYLIBS/AppleIDSetup.md)
- [/System/Library/PrivateFrameworks/AppleIDSetupDaemon.framework/AppleIDSetupDaemon](DYLIBS/AppleIDSetupDaemon.md)
- [/System/Library/PrivateFrameworks/AppleIDSetupUI.framework/AppleIDSetupUI](DYLIBS/AppleIDSetupUI.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices](DYLIBS/AppleMediaServices.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/AppleMediaServicesUI](DYLIBS/AppleMediaServicesUI.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUIDynamic.framework/AppleMediaServicesUIDynamic](DYLIBS/AppleMediaServicesUIDynamic.md)
- [/System/Library/PrivateFrameworks/AppleMobileFileIntegrity.framework/AppleMobileFileIntegrity](DYLIBS/AppleMobileFileIntegrity.md)
- [/System/Library/PrivateFrameworks/ApplePushService.framework/ApplePushService](DYLIBS/ApplePushService.md)
- [/System/Library/PrivateFrameworks/ArchetypeEngine.framework/ArchetypeEngine](DYLIBS/ArchetypeEngine.md)
- [/System/Library/PrivateFrameworks/ArgumentParserInternal.framework/ArgumentParserInternal](DYLIBS/ArgumentParserInternal.md)
- [/System/Library/PrivateFrameworks/AskPermission.framework/AskPermission](DYLIBS/AskPermission.md)
- [/System/Library/PrivateFrameworks/AssetViewer.framework/AssetViewer](DYLIBS/AssetViewer.md)
- [/System/Library/PrivateFrameworks/AssistantSettingsSupport.framework/AssistantSettingsSupport](DYLIBS/AssistantSettingsSupport.md)
- [/System/Library/PrivateFrameworks/AssistiveTouchUI.framework/AssistiveTouchUI](DYLIBS/AssistiveTouchUI.md)
- [/System/Library/PrivateFrameworks/AttributeGraph.framework/AttributeGraph](DYLIBS/AttributeGraph.md)
- [/System/Library/PrivateFrameworks/AudioAnalytics.framework/AudioAnalytics](DYLIBS/AudioAnalytics.md)
- [/System/Library/PrivateFrameworks/AudioAnalyticsBase.framework/AudioAnalyticsBase](DYLIBS/AudioAnalyticsBase.md)
- [/System/Library/PrivateFrameworks/AudioAnalyticsExternal.framework/AudioAnalyticsExternal](DYLIBS/AudioAnalyticsExternal.md)
- [/System/Library/PrivateFrameworks/AudioSession.framework/libSessionUtility.dylib](DYLIBS/libSessionUtility.dylib.md)
- [/System/Library/PrivateFrameworks/AudioSessionServer.framework/AudioSessionServer](DYLIBS/AudioSessionServer.md)
- [/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore](DYLIBS/AudioToolboxCore.md)
- [/System/Library/PrivateFrameworks/AudiogramIngestion.framework/AudiogramIngestion](DYLIBS/AudiogramIngestion.md)
- [/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit](DYLIBS/AuthKit.md)
- [/System/Library/PrivateFrameworks/AuthKitUI.framework/AuthKitUI](DYLIBS/AuthKitUI.md)
- [/System/Library/PrivateFrameworks/AuthenticationServicesCore.framework/AuthenticationServicesCore](DYLIBS/AuthenticationServicesCore.md)
- [/System/Library/PrivateFrameworks/AutoFillUI.framework/AutoFillUI](DYLIBS/AutoFillUI.md)
- [/System/Library/PrivateFrameworks/AutomationMode.framework/AutomationMode](DYLIBS/AutomationMode.md)
- [/System/Library/PrivateFrameworks/AvatarKit.framework/AvatarKit](DYLIBS/AvatarKit.md)
- [/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices](DYLIBS/BackBoardServices.md)
- [/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost](DYLIBS/BacklightServicesHost.md)
- [/System/Library/PrivateFrameworks/BarcodeSupportUI.framework/BarcodeSupportUI](DYLIBS/BarcodeSupportUI.md)
- [/System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard](DYLIBS/BaseBoard.md)
- [/System/Library/PrivateFrameworks/BasebandTraceHelper.framework/BasebandTraceHelper](DYLIBS/BasebandTraceHelper.md)
- [/System/Library/PrivateFrameworks/BatteryAlgorithms.framework/BatteryAlgorithms](DYLIBS/BatteryAlgorithms.md)
- [/System/Library/PrivateFrameworks/BatteryCenter.framework/BatteryCenter](DYLIBS/BatteryCenter.md)
- [/System/Library/PrivateFrameworks/BatteryCenterUI.framework/BatteryCenterUI](DYLIBS/BatteryCenterUI.md)
- [/System/Library/PrivateFrameworks/BiomeFlexibleStorage.framework/BiomeFlexibleStorage](DYLIBS/BiomeFlexibleStorage.md)
- [/System/Library/PrivateFrameworks/BiomeFoundation.framework/BiomeFoundation](DYLIBS/BiomeFoundation.md)
- [/System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary](DYLIBS/BiomeLibrary.md)
- [/System/Library/PrivateFrameworks/BiomeStorage.framework/BiomeStorage](DYLIBS/BiomeStorage.md)
- [/System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams](DYLIBS/BiomeStreams.md)
- [/System/Library/PrivateFrameworks/BiomeSync.framework/BiomeSync](DYLIBS/BiomeSync.md)
- [/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI](DYLIBS/BiometricKitUI.md)
- [/System/Library/PrivateFrameworks/Blackbeard.framework/Blackbeard](DYLIBS/Blackbeard.md)
- [/System/Library/PrivateFrameworks/BlastDoor.framework/BlastDoor](DYLIBS/BlastDoor.md)
- [/System/Library/PrivateFrameworks/BlockMonitoring.framework/BlockMonitoring](DYLIBS/BlockMonitoring.md)
- [/System/Library/PrivateFrameworks/BookDataStore.framework/BookDataStore](DYLIBS/BookDataStore.md)
- [/System/Library/PrivateFrameworks/BookLibraryCore.framework/BookLibraryCore](DYLIBS/BookLibraryCore.md)
- [/System/Library/PrivateFrameworks/BulletinDistributorCompanion.framework/BulletinDistributorCompanion](DYLIBS/BulletinDistributorCompanion.md)
- [/System/Library/PrivateFrameworks/C2.framework/C2](DYLIBS/C2.md)
- [/System/Library/PrivateFrameworks/CAFCombine.framework/CAFCombine](DYLIBS/CAFCombine.md)
- [/System/Library/PrivateFrameworks/CAFUI.framework/CAFUI](DYLIBS/CAFUI.md)
- [/System/Library/PrivateFrameworks/CDMFoundation.framework/CDMFoundation](DYLIBS/CDMFoundation.md)
- [/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture](DYLIBS/CMCapture.md)
- [/System/Library/PrivateFrameworks/CMCaptureCore.framework/CMCaptureCore](DYLIBS/CMCaptureCore.md)
- [/System/Library/PrivateFrameworks/CMContinuityCaptureCore.framework/CMContinuityCaptureCore](DYLIBS/CMContinuityCaptureCore.md)
- [/System/Library/PrivateFrameworks/CMImaging.framework/CMImaging](DYLIBS/CMImaging.md)
- [/System/Library/PrivateFrameworks/CMPhoto.framework/CMPhoto](DYLIBS/CMPhoto.md)
- [/System/Library/PrivateFrameworks/CSExattrCrypto.framework/CSExattrCrypto](DYLIBS/CSExattrCrypto.md)
- [/System/Library/PrivateFrameworks/CTCarrierSpace.framework/CTCarrierSpace](DYLIBS/CTCarrierSpace.md)
- [/System/Library/PrivateFrameworks/Calculate.framework/Calculate](DYLIBS/Calculate.md)
- [/System/Library/PrivateFrameworks/CalculateUI.framework/CalculateUI](DYLIBS/CalculateUI.md)
- [/System/Library/PrivateFrameworks/CalendarLink.framework/CalendarLink](DYLIBS/CalendarLink.md)
- [/System/Library/PrivateFrameworks/CalendarUIKit.framework/CalendarUIKit](DYLIBS/CalendarUIKit.md)
- [/System/Library/PrivateFrameworks/CalendarUIKitInternal.framework/CalendarUIKitInternal](DYLIBS/CalendarUIKitInternal.md)
- [/System/Library/PrivateFrameworks/CalendarWidget.framework/CalendarWidget](DYLIBS/CalendarWidget.md)
- [/System/Library/PrivateFrameworks/CameraEditKit.framework/CameraEditKit](DYLIBS/CameraEditKit.md)
- [/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI](DYLIBS/CameraUI.md)
- [/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework](DYLIBS/CarAccessoryFramework.md)
- [/System/Library/PrivateFrameworks/CarCommandsUIFramework.framework/CarCommandsUIFramework](DYLIBS/CarCommandsUIFramework.md)
- [/System/Library/PrivateFrameworks/CarKit.framework/CarKit](DYLIBS/CarKit.md)
- [/System/Library/PrivateFrameworks/CarPlayAssetUI.framework/CarPlayAssetUI](DYLIBS/CarPlayAssetUI.md)
- [/System/Library/PrivateFrameworks/CarPlayServices.framework/CarPlayServices](DYLIBS/CarPlayServices.md)
- [/System/Library/PrivateFrameworks/CarPlaySupport.framework/CarPlaySupport](DYLIBS/CarPlaySupport.md)
- [/System/Library/PrivateFrameworks/CarouselPreferenceServices.framework/CarouselPreferenceServices](DYLIBS/CarouselPreferenceServices.md)
- [/System/Library/PrivateFrameworks/CascadeEngine.framework/CascadeEngine](DYLIBS/CascadeEngine.md)
- [/System/Library/PrivateFrameworks/CascadeSets.framework/CascadeSets](DYLIBS/CascadeSets.md)
- [/System/Library/PrivateFrameworks/Catalyst.framework/Catalyst](DYLIBS/Catalyst.md)
- [/System/Library/PrivateFrameworks/CellularPlanManager.framework/CellularPlanManager](DYLIBS/CellularPlanManager.md)
- [/System/Library/PrivateFrameworks/ChatKit.framework/ChatKit](DYLIBS/ChatKit.md)
- [/System/Library/PrivateFrameworks/Chirp.framework/Chirp](DYLIBS/Chirp.md)
- [/System/Library/PrivateFrameworks/ChronoCore.framework/ChronoCore](DYLIBS/ChronoCore.md)
- [/System/Library/PrivateFrameworks/ChronoCore.framework/Support/WidgetPreviewsExtensionAgent.bundle/WidgetPreviewsExtensionAgent](DYLIBS/WidgetPreviewsExtensionAgent.md)
- [/System/Library/PrivateFrameworks/ChronoKit.framework/ChronoKit](DYLIBS/ChronoKit.md)
- [/System/Library/PrivateFrameworks/ChronoServices.framework/ChronoServices](DYLIBS/ChronoServices.md)
- [/System/Library/PrivateFrameworks/ChronoUIServices.framework/ChronoUIServices](DYLIBS/ChronoUIServices.md)
- [/System/Library/PrivateFrameworks/CinematicFraming.framework/CinematicFraming](DYLIBS/CinematicFraming.md)
- [/System/Library/PrivateFrameworks/CipherML.framework/CipherML](DYLIBS/CipherML.md)
- [/System/Library/PrivateFrameworks/ClassroomKit.framework/Frameworks/ClassroomUIKit.framework/ClassroomUIKit](DYLIBS/ClassroomUIKit.md)
- [/System/Library/PrivateFrameworks/ClockPoster.framework/ClockPoster](DYLIBS/ClockPoster.md)
- [/System/Library/PrivateFrameworks/CloudAssetDaemon.framework/CloudAssetDaemon](DYLIBS/CloudAssetDaemon.md)
- [/System/Library/PrivateFrameworks/CloudAttestation.framework/CloudAttestation](DYLIBS/CloudAttestation.md)
- [/System/Library/PrivateFrameworks/CloudDocs.framework/CloudDocs](DYLIBS/CloudDocs.md)
- [/System/Library/PrivateFrameworks/CloudDocsDaemon.framework/CloudDocsDaemon](DYLIBS/CloudDocsDaemon.md)
- [/System/Library/PrivateFrameworks/CloudKitDaemon.framework/CloudKitDaemon](DYLIBS/CloudKitDaemon.md)
- [/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/CloudPhotoLibrary](DYLIBS/CloudPhotoLibrary.md)
- [/System/Library/PrivateFrameworks/CloudRecommendationUI.framework/CloudRecommendationUI](DYLIBS/CloudRecommendationUI.md)
- [/System/Library/PrivateFrameworks/CloudSharingUI.framework/CloudSharingUI](DYLIBS/CloudSharingUI.md)
- [/System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/CloudSubscriptionFeatures](DYLIBS/CloudSubscriptionFeatures.md)
- [/System/Library/PrivateFrameworks/CloudTelemetryTools.framework/CloudTelemetryTools](DYLIBS/CloudTelemetryTools.md)
- [/System/Library/PrivateFrameworks/Coherence.framework/Coherence](DYLIBS/Coherence.md)
- [/System/Library/PrivateFrameworks/CollectionsInternal.framework/CollectionsInternal](DYLIBS/CollectionsInternal.md)
- [/System/Library/PrivateFrameworks/CommandAndControlUI.framework/CommandAndControlUI](DYLIBS/CommandAndControlUI.md)
- [/System/Library/PrivateFrameworks/CommunicationsSetupUI.framework/CommunicationsSetupUI](DYLIBS/CommunicationsSetupUI.md)
- [/System/Library/PrivateFrameworks/CommunicationsUI.framework/CommunicationsUI](DYLIBS/CommunicationsUI.md)
- [/System/Library/PrivateFrameworks/ComplicationDisplay.framework/ComplicationDisplay](DYLIBS/ComplicationDisplay.md)
- [/System/Library/PrivateFrameworks/ConditionInducer.framework/ConditionInducer](DYLIBS/ConditionInducer.md)
- [/System/Library/PrivateFrameworks/ContactlessReaderUI.framework/ContactlessReaderUI](DYLIBS/ContactlessReaderUI.md)
- [/System/Library/PrivateFrameworks/ContactsAutocomplete.framework/ContactsAutocomplete](DYLIBS/ContactsAutocomplete.md)
- [/System/Library/PrivateFrameworks/ContactsAutocompleteUI.framework/ContactsAutocompleteUI](DYLIBS/ContactsAutocompleteUI.md)
- [/System/Library/PrivateFrameworks/ContactsFoundation.framework/ContactsFoundation](DYLIBS/ContactsFoundation.md)
- [/System/Library/PrivateFrameworks/ContentKit.framework/ContentKit](DYLIBS/ContentKit.md)
- [/System/Library/PrivateFrameworks/ContextKit.framework/ContextKit](DYLIBS/ContextKit.md)
- [/System/Library/PrivateFrameworks/ControlCenterServices.framework/ControlCenterServices](DYLIBS/ControlCenterServices.md)
- [/System/Library/PrivateFrameworks/ControlCenterUI.framework/ControlCenterUI](DYLIBS/ControlCenterUI.md)
- [/System/Library/PrivateFrameworks/ControlCenterUIKit.framework/ControlCenterUIKit](DYLIBS/ControlCenterUIKit.md)
- [/System/Library/PrivateFrameworks/ControlCenterUIServices.framework/ControlCenterUIServices](DYLIBS/ControlCenterUIServices.md)
- [/System/Library/PrivateFrameworks/ConversationKit.framework/ConversationKit](DYLIBS/ConversationKit.md)
- [/System/Library/PrivateFrameworks/CoreAccessories.framework/CoreAccessories](DYLIBS/CoreAccessories.md)
- [/System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP](DYLIBS/CoreCDP.md)
- [/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal](DYLIBS/CoreCDPInternal.md)
- [/System/Library/PrivateFrameworks/CoreCDPUI.framework/CoreCDPUI](DYLIBS/CoreCDPUI.md)
- [/System/Library/PrivateFrameworks/CoreCDPUIInternal.framework/CoreCDPUIInternal](DYLIBS/CoreCDPUIInternal.md)
- [/System/Library/PrivateFrameworks/CoreDAV.framework/CoreDAV](DYLIBS/CoreDAV.md)
- [/System/Library/PrivateFrameworks/CoreDiagnostics.framework/CoreDiagnostics](DYLIBS/CoreDiagnostics.md)
- [/System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet](DYLIBS/CoreDuet.md)
- [/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/CoreEmbeddedSpeechRecognition](DYLIBS/CoreEmbeddedSpeechRecognition.md)
- [/System/Library/PrivateFrameworks/CoreEmoji.framework/CoreEmoji](DYLIBS/CoreEmoji.md)
- [/System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp](DYLIBS/CoreFollowUp.md)
- [/System/Library/PrivateFrameworks/CoreHAP.framework/CoreHAP](DYLIBS/CoreHAP.md)
- [/System/Library/PrivateFrameworks/CoreHID.framework/CoreHID](DYLIBS/CoreHID.md)
- [/System/Library/PrivateFrameworks/CoreHandwriting.framework/CoreHandwriting](DYLIBS/CoreHandwriting.md)
- [/System/Library/PrivateFrameworks/CoreIDV.framework/CoreIDV](DYLIBS/CoreIDV.md)
- [/System/Library/PrivateFrameworks/CoreIDVPAD.framework/CoreIDVPAD](DYLIBS/CoreIDVPAD.md)
- [/System/Library/PrivateFrameworks/CoreIDVRGBLiveness.framework/CoreIDVRGBLiveness](DYLIBS/CoreIDVRGBLiveness.md)
- [/System/Library/PrivateFrameworks/CoreIDVUI.framework/CoreIDVUI](DYLIBS/CoreIDVUI.md)
- [/System/Library/PrivateFrameworks/CoreKnowledge.framework/CoreKnowledge](DYLIBS/CoreKnowledge.md)
- [/System/Library/PrivateFrameworks/CoreMaterial.framework/CoreMaterial](DYLIBS/CoreMaterial.md)
- [/System/Library/PrivateFrameworks/CoreMediaStream.framework/CoreMediaStream](DYLIBS/CoreMediaStream.md)
- [/System/Library/PrivateFrameworks/CoreMotionAlgorithms.framework/CoreMotionAlgorithms](DYLIBS/CoreMotionAlgorithms.md)
- [/System/Library/PrivateFrameworks/CoreNLP.framework/CoreNLP](DYLIBS/CoreNLP.md)
- [/System/Library/PrivateFrameworks/CoreOC.framework/CoreOC](DYLIBS/CoreOC.md)
- [/System/Library/PrivateFrameworks/CoreODI.framework/CoreODI](DYLIBS/CoreODI.md)
- [/System/Library/PrivateFrameworks/CoreODIEssentials.framework/CoreODIEssentials](DYLIBS/CoreODIEssentials.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/CoreParsec](DYLIBS/CoreParsec.md)
- [/System/Library/PrivateFrameworks/CorePhotogrammetry.framework/CorePhotogrammetry](DYLIBS/CorePhotogrammetry.md)
- [/System/Library/PrivateFrameworks/CoreRE.framework/CoreRE](DYLIBS/CoreRE.md)
- [/System/Library/PrivateFrameworks/CoreRealityIO.framework/CoreRealityIO](DYLIBS/CoreRealityIO.md)
- [/System/Library/PrivateFrameworks/CoreRepairUI.framework/CoreRepairUI](DYLIBS/CoreRepairUI.md)
- [/System/Library/PrivateFrameworks/CoreSDB.framework/CoreSDB](DYLIBS/CoreSDB.md)
- [/System/Library/PrivateFrameworks/CoreSceneUnderstanding.framework/CoreSceneUnderstanding](DYLIBS/CoreSceneUnderstanding.md)
- [/System/Library/PrivateFrameworks/CoreServicesInternal.framework/CoreServicesInternal](DYLIBS/CoreServicesInternal.md)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/CoreSpeech](DYLIBS/CoreSpeech.md)
- [/System/Library/PrivateFrameworks/CoreSpeechExclave.framework/CoreSpeechExclave](DYLIBS/CoreSpeechExclave.md)
- [/System/Library/PrivateFrameworks/CoreSpeechFoundation.framework/CoreSpeechFoundation](DYLIBS/CoreSpeechFoundation.md)
- [/System/Library/PrivateFrameworks/CoreSuggestionsInternals.framework/CoreSuggestionsInternals](DYLIBS/CoreSuggestionsInternals.md)
- [/System/Library/PrivateFrameworks/CoreUARP.framework/CoreUARP](DYLIBS/CoreUARP.md)
- [/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI](DYLIBS/CoreUI.md)
- [/System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils](DYLIBS/CoreUtils.md)
- [/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi](DYLIBS/CoreWiFi.md)
- [/System/Library/PrivateFrameworks/CoverSheet.framework/CoverSheet](DYLIBS/CoverSheet.md)
- [/System/Library/PrivateFrameworks/CryptoKitPrivate.framework/CryptoKitPrivate](DYLIBS/CryptoKitPrivate.md)
- [/System/Library/PrivateFrameworks/DMCApps.framework/DMCApps](DYLIBS/DMCApps.md)
- [/System/Library/PrivateFrameworks/DMCEnrollmentProvider.framework/DMCEnrollmentProvider](DYLIBS/DMCEnrollmentProvider.md)
- [/System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities](DYLIBS/DMCUtilities.md)
- [/System/Library/PrivateFrameworks/DarwinDirectoryInternal.framework/DarwinDirectoryInternal](DYLIBS/DarwinDirectoryInternal.md)
- [/System/Library/PrivateFrameworks/DashBoard.framework/DashBoard](DYLIBS/DashBoard.md)
- [/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DACardDAV.framework/DACardDAV](DYLIBS/DACardDAV.md)
- [/System/Library/PrivateFrameworks/DataAccessExpress.framework/DataAccessExpress](DYLIBS/DataAccessExpress.md)
- [/System/Library/PrivateFrameworks/DataDetectorsCore.framework/DataDetectorsCore](DYLIBS/DataDetectorsCore.md)
- [/System/Library/PrivateFrameworks/DataDetectorsNaturalLanguage.framework/DataDetectorsNaturalLanguage](DYLIBS/DataDetectorsNaturalLanguage.md)
- [/System/Library/PrivateFrameworks/DataDetectorsUI.framework/DataDetectorsUI](DYLIBS/DataDetectorsUI.md)
- [/System/Library/PrivateFrameworks/DataFlow.framework/DataFlow](DYLIBS/DataFlow.md)
- [/System/Library/PrivateFrameworks/DeepThought.framework/DeepThought](DYLIBS/DeepThought.md)
- [/System/Library/PrivateFrameworks/DepthCore.framework/DepthCore](DYLIBS/DepthCore.md)
- [/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/DesktopServicesPriv](DYLIBS/DesktopServicesPriv.md)
- [/System/Library/PrivateFrameworks/DeviceAccess.framework/DeviceAccess](DYLIBS/DeviceAccess.md)
- [/System/Library/PrivateFrameworks/DeviceDiscoveryUI.framework/DeviceDiscoveryUI](DYLIBS/DeviceDiscoveryUI.md)
- [/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/DeviceExpertIntents](DYLIBS/DeviceExpertIntents.md)
- [/System/Library/PrivateFrameworks/DeviceExpertUI.framework/DeviceExpertUI](DYLIBS/DeviceExpertUI.md)
- [/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/DifferentialPrivacy](DYLIBS/DifferentialPrivacy.md)
- [/System/Library/PrivateFrameworks/DistributedEvaluation.framework/DistributedEvaluation](DYLIBS/DistributedEvaluation.md)
- [/System/Library/PrivateFrameworks/DistributedTimers.framework/DistributedTimers](DYLIBS/DistributedTimers.md)
- [/System/Library/PrivateFrameworks/DistributedTimersDaemon.framework/DistributedTimersDaemon](DYLIBS/DistributedTimersDaemon.md)
- [/System/Library/PrivateFrameworks/DoNotDisturbServer.framework/DoNotDisturbServer](DYLIBS/DoNotDisturbServer.md)
- [/System/Library/PrivateFrameworks/DockKitCore.framework/DockKitCore](DYLIBS/DockKitCore.md)
- [/System/Library/PrivateFrameworks/DocumentManager.framework/DocumentManager](DYLIBS/DocumentManager.md)
- [/System/Library/PrivateFrameworks/DocumentManagerCore.framework/DocumentManagerCore](DYLIBS/DocumentManagerCore.md)
- [/System/Library/PrivateFrameworks/DocumentManagerExecutables.framework/DocumentManagerExecutables](DYLIBS/DocumentManagerExecutables.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/DocumentManagerUICore](DYLIBS/DocumentManagerUICore.md)
- [/System/Library/PrivateFrameworks/DocumentUnderstanding.framework/DocumentUnderstanding](DYLIBS/DocumentUnderstanding.md)
- [/System/Library/PrivateFrameworks/DrawingBoard.framework/DrawingBoard](DYLIBS/DrawingBoard.md)
- [/System/Library/PrivateFrameworks/DropInCore.framework/DropInCore](DYLIBS/DropInCore.md)
- [/System/Library/PrivateFrameworks/DropletUI.framework/DropletUI](DYLIBS/DropletUI.md)
- [/System/Library/PrivateFrameworks/EcosystemAnalytics.framework/EcosystemAnalytics](DYLIBS/EcosystemAnalytics.md)
- [/System/Library/PrivateFrameworks/Email.framework/Email](DYLIBS/Email.md)
- [/System/Library/PrivateFrameworks/EmailCore.framework/EmailCore](DYLIBS/EmailCore.md)
- [/System/Library/PrivateFrameworks/EmailDaemon.framework/EmailDaemon](DYLIBS/EmailDaemon.md)
- [/System/Library/PrivateFrameworks/EmbeddedAcousticRecognition.framework/EmbeddedAcousticRecognition](DYLIBS/EmbeddedAcousticRecognition.md)
- [/System/Library/PrivateFrameworks/EmojiFoundation.framework/EmojiFoundation](DYLIBS/EmojiFoundation.md)
- [/System/Library/PrivateFrameworks/EmojiPoster.framework/EmojiPoster](DYLIBS/EmojiPoster.md)
- [/System/Library/PrivateFrameworks/EnergyKit.framework/EnergyKit](DYLIBS/EnergyKit.md)
- [/System/Library/PrivateFrameworks/Espresso.framework/Espresso](DYLIBS/Espresso.md)
- [/System/Library/PrivateFrameworks/FMCoreLite.framework/FMCoreLite](DYLIBS/FMCoreLite.md)
- [/System/Library/PrivateFrameworks/FMFCore.framework/FMFCore](DYLIBS/FMFCore.md)
- [/System/Library/PrivateFrameworks/FMFindingUI.framework/FMFindingUI](DYLIBS/FMFindingUI.md)
- [/System/Library/PrivateFrameworks/FMIPCore.framework/FMIPCore](DYLIBS/FMIPCore.md)
- [/System/Library/PrivateFrameworks/FPFS.framework/FPFS](DYLIBS/FPFS.md)
- [/System/Library/PrivateFrameworks/FaceTimeMessageStore.framework/FaceTimeMessageStore](DYLIBS/FaceTimeMessageStore.md)
- [/System/Library/PrivateFrameworks/FamilyCircle.framework/FamilyCircle](DYLIBS/FamilyCircle.md)
- [/System/Library/PrivateFrameworks/FamilyCircleUI.framework/FamilyCircleUI](DYLIBS/FamilyCircleUI.md)
- [/System/Library/PrivateFrameworks/FeatureStore.framework/FeatureStore](DYLIBS/FeatureStore.md)
- [/System/Library/PrivateFrameworks/Feedback.framework/Feedback](DYLIBS/Feedback.md)
- [/System/Library/PrivateFrameworks/FeedbackCore.framework/FeedbackCore](DYLIBS/FeedbackCore.md)
- [/System/Library/PrivateFrameworks/FeedbackService.framework/FeedbackService](DYLIBS/FeedbackService.md)
- [/System/Library/PrivateFrameworks/FileProviderDaemon.framework/FileProviderDaemon](DYLIBS/FileProviderDaemon.md)
- [/System/Library/PrivateFrameworks/FinHealthCore.framework/FinHealthCore](DYLIBS/FinHealthCore.md)
- [/System/Library/PrivateFrameworks/FinanceDaemon.framework/FinanceDaemon](DYLIBS/FinanceDaemon.md)
- [/System/Library/PrivateFrameworks/FindMyBase.framework/FindMyBase](DYLIBS/FindMyBase.md)
- [/System/Library/PrivateFrameworks/FindMyBluetooth.framework/FindMyBluetooth](DYLIBS/FindMyBluetooth.md)
- [/System/Library/PrivateFrameworks/FindMyMessaging.framework/FindMyMessaging](DYLIBS/FindMyMessaging.md)
- [/System/Library/PrivateFrameworks/FindMyUICore.framework/FindMyUICore](DYLIBS/FindMyUICore.md)
- [/System/Library/PrivateFrameworks/FitnessAppRoot.framework/FitnessAppRoot](DYLIBS/FitnessAppRoot.md)
- [/System/Library/PrivateFrameworks/FitnessAsset.framework/FitnessAsset](DYLIBS/FitnessAsset.md)
- [/System/Library/PrivateFrameworks/FitnessBrowsing.framework/FitnessBrowsing](DYLIBS/FitnessBrowsing.md)
- [/System/Library/PrivateFrameworks/FitnessCanvasUI.framework/FitnessCanvasUI](DYLIBS/FitnessCanvasUI.md)
- [/System/Library/PrivateFrameworks/FitnessCoaching.framework/FitnessCoaching](DYLIBS/FitnessCoaching.md)
- [/System/Library/PrivateFrameworks/FitnessCoachingServices.framework/FitnessCoachingServices](DYLIBS/FitnessCoachingServices.md)
- [/System/Library/PrivateFrameworks/FitnessCoreUI.framework/FitnessCoreUI](DYLIBS/FitnessCoreUI.md)
- [/System/Library/PrivateFrameworks/FitnessFiltering.framework/FitnessFiltering](DYLIBS/FitnessFiltering.md)
- [/System/Library/PrivateFrameworks/FitnessForYou.framework/FitnessForYou](DYLIBS/FitnessForYou.md)
- [/System/Library/PrivateFrameworks/FitnessLibrary.framework/FitnessLibrary](DYLIBS/FitnessLibrary.md)
- [/System/Library/PrivateFrameworks/FitnessMarketing.framework/FitnessMarketing](DYLIBS/FitnessMarketing.md)
- [/System/Library/PrivateFrameworks/FitnessOnboarding.framework/FitnessOnboarding](DYLIBS/FitnessOnboarding.md)
- [/System/Library/PrivateFrameworks/FitnessSearch.framework/FitnessSearch](DYLIBS/FitnessSearch.md)
- [/System/Library/PrivateFrameworks/FitnessUI.framework/FitnessUI](DYLIBS/FitnessUI.md)
- [/System/Library/PrivateFrameworks/FitnessUtilities.framework/FitnessUtilities](DYLIBS/FitnessUtilities.md)
- [/System/Library/PrivateFrameworks/Fluid.framework/Fluid](DYLIBS/Fluid.md)
- [/System/Library/PrivateFrameworks/FocusSettingsUI.framework/FocusSettingsUI](DYLIBS/FocusSettingsUI.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/libGSFont.dylib](DYLIBS/libGSFont.dylib.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/libGSFontCache.dylib](DYLIBS/libGSFontCache.dylib.md)
- [/System/Library/PrivateFrameworks/FramePacing.framework/FramePacing](DYLIBS/FramePacing.md)
- [/System/Library/PrivateFrameworks/FriendKit.framework/FriendKit](DYLIBS/FriendKit.md)
- [/System/Library/PrivateFrameworks/GRDBInternal.framework/GRDBInternal](DYLIBS/GRDBInternal.md)
- [/System/Library/PrivateFrameworks/GameCenterFoundation.framework/GameCenterFoundation](DYLIBS/GameCenterFoundation.md)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/GameCenterUI](DYLIBS/GameCenterUI.md)
- [/System/Library/PrivateFrameworks/GamePolicy.framework/GamePolicy](DYLIBS/GamePolicy.md)
- [/System/Library/PrivateFrameworks/GenerationalStorage.framework/GenerationalStorage](DYLIBS/GenerationalStorage.md)
- [/System/Library/PrivateFrameworks/GenerativeExperiences.framework/GenerativeExperiences](DYLIBS/GenerativeExperiences.md)
- [/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/GenerativeExperiencesRuntime](DYLIBS/GenerativeExperiencesRuntime.md)
- [/System/Library/PrivateFrameworks/GenerativeFunctions.framework/GenerativeFunctions](DYLIBS/GenerativeFunctions.md)
- [/System/Library/PrivateFrameworks/GenerativeFunctionsFoundation.framework/GenerativeFunctionsFoundation](DYLIBS/GenerativeFunctionsFoundation.md)
- [/System/Library/PrivateFrameworks/GenerativeFunctionsInstrumentation.framework/GenerativeFunctionsInstrumentation](DYLIBS/GenerativeFunctionsInstrumentation.md)
- [/System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels](DYLIBS/GenerativeModels.md)
- [/System/Library/PrivateFrameworks/GenerativeModelsFoundation.framework/GenerativeModelsFoundation](DYLIBS/GenerativeModelsFoundation.md)
- [/System/Library/PrivateFrameworks/GeoServices.framework/GeoServices](DYLIBS/GeoServices.md)
- [/System/Library/PrivateFrameworks/GeoUIFramework.framework/GeoUIFramework](DYLIBS/GeoUIFramework.md)
- [/System/Library/PrivateFrameworks/GroupKitCrypto.framework/GroupKitCrypto](DYLIBS/GroupKitCrypto.md)
- [/System/Library/PrivateFrameworks/HDRProcessing.framework/HDRProcessing](DYLIBS/HDRProcessing.md)
- [/System/Library/PrivateFrameworks/Hands.framework/Hands](DYLIBS/Hands.md)
- [/System/Library/PrivateFrameworks/HeadGestures.framework/HeadGestures](DYLIBS/HeadGestures.md)
- [/System/Library/PrivateFrameworks/HeadphoneConfigs.framework/HeadphoneConfigs](DYLIBS/HeadphoneConfigs.md)
- [/System/Library/PrivateFrameworks/HeadphoneManager.framework/HeadphoneManager](DYLIBS/HeadphoneManager.md)
- [/System/Library/PrivateFrameworks/HeadphoneProxFeatureService.framework/HeadphoneProxFeatureService](DYLIBS/HeadphoneProxFeatureService.md)
- [/System/Library/PrivateFrameworks/HealthAppServices.framework/HealthAppServices](DYLIBS/HealthAppServices.md)
- [/System/Library/PrivateFrameworks/HealthBalance.framework/HealthBalance](DYLIBS/HealthBalance.md)
- [/System/Library/PrivateFrameworks/HealthBalanceDaemon.framework/HealthBalanceDaemon](DYLIBS/HealthBalanceDaemon.md)
- [/System/Library/PrivateFrameworks/HealthBalanceUI.framework/HealthBalanceUI](DYLIBS/HealthBalanceUI.md)
- [/System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon](DYLIBS/HealthDaemon.md)
- [/System/Library/PrivateFrameworks/HealthExperience.framework/HealthExperience](DYLIBS/HealthExperience.md)
- [/System/Library/PrivateFrameworks/HealthExperienceUI.framework/HealthExperienceUI](DYLIBS/HealthExperienceUI.md)
- [/System/Library/PrivateFrameworks/HealthExposureNotificationUI.framework/HealthExposureNotificationUI](DYLIBS/HealthExposureNotificationUI.md)
- [/System/Library/PrivateFrameworks/HealthKitAdditions.framework/HealthKitAdditions](DYLIBS/HealthKitAdditions.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsUI.framework/HealthMedicationsUI](DYLIBS/HealthMedicationsUI.md)
- [/System/Library/PrivateFrameworks/HealthMenstrualCycles.framework/HealthMenstrualCycles](DYLIBS/HealthMenstrualCycles.md)
- [/System/Library/PrivateFrameworks/HealthMenstrualCyclesDaemon.framework/HealthMenstrualCyclesDaemon](DYLIBS/HealthMenstrualCyclesDaemon.md)
- [/System/Library/PrivateFrameworks/HealthOrchestration.framework/HealthOrchestration](DYLIBS/HealthOrchestration.md)
- [/System/Library/PrivateFrameworks/HealthPlatform.framework/HealthPlatform](DYLIBS/HealthPlatform.md)
- [/System/Library/PrivateFrameworks/HealthPlatformCore.framework/HealthPlatformCore](DYLIBS/HealthPlatformCore.md)
- [/System/Library/PrivateFrameworks/HealthPluginHost.framework/HealthPluginHost](DYLIBS/HealthPluginHost.md)
- [/System/Library/PrivateFrameworks/HealthRecordsDaemon.framework/HealthRecordsDaemon](DYLIBS/HealthRecordsDaemon.md)
- [/System/Library/PrivateFrameworks/HealthRecordsUI.framework/HealthRecordsUI](DYLIBS/HealthRecordsUI.md)
- [/System/Library/PrivateFrameworks/HealthVisualization.framework/HealthVisualization](DYLIBS/HealthVisualization.md)
- [/System/Library/PrivateFrameworks/HearingUI.framework/HearingUI](DYLIBS/HearingUI.md)
- [/System/Library/PrivateFrameworks/HearingUtilities.framework/HearingUtilities](DYLIBS/HearingUtilities.md)
- [/System/Library/PrivateFrameworks/Home.framework/Home](DYLIBS/Home.md)
- [/System/Library/PrivateFrameworks/HomeAccessoryControlUI.framework/HomeAccessoryControlUI](DYLIBS/HomeAccessoryControlUI.md)
- [/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/HomeAutomationInternal](DYLIBS/HomeAutomationInternal.md)
- [/System/Library/PrivateFrameworks/HomeDataModel.framework/HomeDataModel](DYLIBS/HomeDataModel.md)
- [/System/Library/PrivateFrameworks/HomeEnergyDaemon.framework/HomeEnergyDaemon](DYLIBS/HomeEnergyDaemon.md)
- [/System/Library/PrivateFrameworks/HomeEnergyUI.framework/HomeEnergyUI](DYLIBS/HomeEnergyUI.md)
- [/System/Library/PrivateFrameworks/HomeKitCore.framework/HomeKitCore](DYLIBS/HomeKitCore.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemon.framework/HomeKitDaemon](DYLIBS/HomeKitDaemon.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemonLegacy.framework/HomeKitDaemonLegacy](DYLIBS/HomeKitDaemonLegacy.md)
- [/System/Library/PrivateFrameworks/HomeKitEvents.framework/HomeKitEvents](DYLIBS/HomeKitEvents.md)
- [/System/Library/PrivateFrameworks/HomeKitMatter.framework/HomeKitMatter](DYLIBS/HomeKitMatter.md)
- [/System/Library/PrivateFrameworks/HomePodSettings.framework/HomePodSettings](DYLIBS/HomePodSettings.md)
- [/System/Library/PrivateFrameworks/HomeUI.framework/HomeUI](DYLIBS/HomeUI.md)
- [/System/Library/PrivateFrameworks/HomeUI2.framework/HomeUI2](DYLIBS/HomeUI2.md)
- [/System/Library/PrivateFrameworks/HomeUICommon.framework/HomeUICommon](DYLIBS/HomeUICommon.md)
- [/System/Library/PrivateFrameworks/HomeUtilityServices.framework/HomeUtilityServices](DYLIBS/HomeUtilityServices.md)
- [/System/Library/PrivateFrameworks/HomeWidgetIntents.framework/HomeWidgetIntents](DYLIBS/HomeWidgetIntents.md)
- [/System/Library/PrivateFrameworks/HoverTextUI.framework/HoverTextUI](DYLIBS/HoverTextUI.md)
- [/System/Library/PrivateFrameworks/Human.framework/Human](DYLIBS/Human.md)
- [/System/Library/PrivateFrameworks/HumanUI.framework/HumanUI](DYLIBS/HumanUI.md)
- [/System/Library/PrivateFrameworks/HumanUnderstandingFoundation.framework/HumanUnderstandingFoundation](DYLIBS/HumanUnderstandingFoundation.md)
- [/System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation](DYLIBS/IDSFoundation.md)
- [/System/Library/PrivateFrameworks/IMAVCore.framework/IMAVCore](DYLIBS/IMAVCore.md)
- [/System/Library/PrivateFrameworks/IMAssistantCore.framework/IMAssistantCore](DYLIBS/IMAssistantCore.md)
- [/System/Library/PrivateFrameworks/IMCore.framework/IMCore](DYLIBS/IMCore.md)
- [/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence](DYLIBS/IMDPersistence.md)
- [/System/Library/PrivateFrameworks/IMDaemonCore.framework/IMDaemonCore](DYLIBS/IMDaemonCore.md)
- [/System/Library/PrivateFrameworks/IMFoundation.framework/IMFoundation](DYLIBS/IMFoundation.md)
- [/System/Library/PrivateFrameworks/IMRCSTransfer.framework/IMRCSTransfer](DYLIBS/IMRCSTransfer.md)
- [/System/Library/PrivateFrameworks/IMSharedUtilities.framework/IMSharedUtilities](DYLIBS/IMSharedUtilities.md)
- [/System/Library/PrivateFrameworks/IMTranscoderAgent.framework/IMTranscoderAgent](DYLIBS/IMTranscoderAgent.md)
- [/System/Library/PrivateFrameworks/IMTransferAgent.framework/IMTransferAgent](DYLIBS/IMTransferAgent.md)
- [/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU](DYLIBS/IOGPU.md)
- [/System/Library/PrivateFrameworks/IOMobileFramebuffer.framework/IOMobileFramebuffer](DYLIBS/IOMobileFramebuffer.md)
- [/System/Library/PrivateFrameworks/IPTelephony.framework/Support/libIPTelephony.dylib](DYLIBS/libIPTelephony.dylib.md)
- [/System/Library/PrivateFrameworks/IconFoundation.framework/IconFoundation](DYLIBS/IconFoundation.md)
- [/System/Library/PrivateFrameworks/IconServices.framework/IconServices](DYLIBS/IconServices.md)
- [/System/Library/PrivateFrameworks/IdleTimerHosting.framework/IdleTimerHosting](DYLIBS/IdleTimerHosting.md)
- [/System/Library/PrivateFrameworks/ImagePlayground.framework/ImagePlayground](DYLIBS/ImagePlayground.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlow.framework/IntelligenceFlow](DYLIBS/IntelligenceFlow.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowContext.framework/IntelligenceFlowContext](DYLIBS/IntelligenceFlowContext.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowContextRuntime.framework/IntelligenceFlowContextRuntime](DYLIBS/IntelligenceFlowContextRuntime.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/IntelligenceFlowPlannerRuntime](DYLIBS/IntelligenceFlowPlannerRuntime.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowPlannerSupport.framework/IntelligenceFlowPlannerSupport](DYLIBS/IntelligenceFlowPlannerSupport.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/IntelligenceFlowRuntime](DYLIBS/IntelligenceFlowRuntime.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatform.framework/IntelligencePlatform](DYLIBS/IntelligencePlatform.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/IntelligencePlatformCore](DYLIBS/IntelligencePlatformCore.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformLibrary.framework/IntelligencePlatformLibrary](DYLIBS/IntelligencePlatformLibrary.md)
- [/System/Library/PrivateFrameworks/IntelligentTrackingCore.framework/IntelligentTrackingCore](DYLIBS/IntelligentTrackingCore.md)
- [/System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf](DYLIBS/InternalSwiftProtobuf.md)
- [/System/Library/PrivateFrameworks/JetEngine.framework/JetEngine](DYLIBS/JetEngine.md)
- [/System/Library/PrivateFrameworks/JetUI.framework/JetUI](DYLIBS/JetUI.md)
- [/System/Library/PrivateFrameworks/KeyboardArbiter.framework/KeyboardArbiter](DYLIBS/KeyboardArbiter.md)
- [/System/Library/PrivateFrameworks/KeychainCircle.framework/KeychainCircle](DYLIBS/KeychainCircle.md)
- [/System/Library/PrivateFrameworks/KnowledgeGraphKit.framework/KnowledgeGraphKit](DYLIBS/KnowledgeGraphKit.md)
- [/System/Library/PrivateFrameworks/KnowledgeMonitor.framework/KnowledgeMonitor](DYLIBS/KnowledgeMonitor.md)
- [/System/Library/PrivateFrameworks/LanguageModeling.framework/LanguageModeling](DYLIBS/LanguageModeling.md)
- [/System/Library/PrivateFrameworks/LearnedFeatures.framework/LearnedFeatures](DYLIBS/LearnedFeatures.md)
- [/System/Library/PrivateFrameworks/LegalAndRegulatorySettingsSupport.framework/LegalAndRegulatorySettingsSupport](DYLIBS/LegalAndRegulatorySettingsSupport.md)
- [/System/Library/PrivateFrameworks/Lexicon.framework/Lexicon](DYLIBS/Lexicon.md)
- [/System/Library/PrivateFrameworks/LiftUI.framework/LiftUI](DYLIBS/LiftUI.md)
- [/System/Library/PrivateFrameworks/LighthouseBitacoraFramework.framework/LighthouseBitacoraFramework](DYLIBS/LighthouseBitacoraFramework.md)
- [/System/Library/PrivateFrameworks/LighthouseDataProcessor.framework/LighthouseDataProcessor](DYLIBS/LighthouseDataProcessor.md)
- [/System/Library/PrivateFrameworks/LinkMetadata.framework/LinkMetadata](DYLIBS/LinkMetadata.md)
- [/System/Library/PrivateFrameworks/LinkServices.framework/LinkServices](DYLIBS/LinkServices.md)
- [/System/Library/PrivateFrameworks/LiveExecutionResultsProbe.framework/LiveExecutionResultsProbe](DYLIBS/LiveExecutionResultsProbe.md)
- [/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore](DYLIBS/LocalAuthenticationCore.md)
- [/System/Library/PrivateFrameworks/LockedContentServices.framework/LockedContentServices](DYLIBS/LockedContentServices.md)
- [/System/Library/PrivateFrameworks/MCCKitCategorization.framework/MCCKitCategorization](DYLIBS/MCCKitCategorization.md)
- [/System/Library/PrivateFrameworks/MDMClientLibrary.framework/MDMClientLibrary](DYLIBS/MDMClientLibrary.md)
- [/System/Library/PrivateFrameworks/MFAAuthentication.framework/MFAAuthentication](DYLIBS/MFAAuthentication.md)
- [/System/Library/PrivateFrameworks/MLAssetIO.framework/MLAssetIO](DYLIBS/MLAssetIO.md)
- [/System/Library/PrivateFrameworks/MLModelSpecification.framework/MLModelSpecification](DYLIBS/MLModelSpecification.md)
- [/System/Library/PrivateFrameworks/MMCS.framework/MMCS](DYLIBS/MMCS.md)
- [/System/Library/PrivateFrameworks/MOVStreamIO.framework/MOVStreamIO](DYLIBS/MOVStreamIO.md)
- [/System/Library/PrivateFrameworks/MacinTalk.framework/MacinTalk](DYLIBS/MacinTalk.md)
- [/System/Library/PrivateFrameworks/MagnifierSupport.framework/MagnifierSupport](DYLIBS/MagnifierSupport.md)
- [/System/Library/PrivateFrameworks/MailUI.framework/MailUI](DYLIBS/MailUI.md)
- [/System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration](DYLIBS/ManagedConfiguration.md)
- [/System/Library/PrivateFrameworks/ManagedConfigurationUI.framework/ManagedConfigurationUI](DYLIBS/ManagedConfigurationUI.md)
- [/System/Library/PrivateFrameworks/ManagedSettingsObjC.framework/ManagedSettingsObjC](DYLIBS/ManagedSettingsObjC.md)
- [/System/Library/PrivateFrameworks/MapsSuggestions.framework/MapsSuggestions](DYLIBS/MapsSuggestions.md)
- [/System/Library/PrivateFrameworks/MapsSync.framework/MapsSync](DYLIBS/MapsSync.md)
- [/System/Library/PrivateFrameworks/MapsUI.framework/MapsUI](DYLIBS/MapsUI.md)
- [/System/Library/PrivateFrameworks/Marrs.framework/Marrs](DYLIBS/Marrs.md)
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/MediaAnalysis](DYLIBS/MediaAnalysis.md)
- [/System/Library/PrivateFrameworks/MediaAnalysisServices.framework/MediaAnalysisServices](DYLIBS/MediaAnalysisServices.md)
- [/System/Library/PrivateFrameworks/MediaControlSender.framework/MediaControlSender](DYLIBS/MediaControlSender.md)
- [/System/Library/PrivateFrameworks/MediaControls.framework/MediaControls](DYLIBS/MediaControls.md)
- [/System/Library/PrivateFrameworks/MediaCoreUI.framework/MediaCoreUI](DYLIBS/MediaCoreUI.md)
- [/System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience](DYLIBS/MediaExperience.md)
- [/System/Library/PrivateFrameworks/MediaFoundation.framework/MediaFoundation](DYLIBS/MediaFoundation.md)
- [/System/Library/PrivateFrameworks/MediaML.framework/MediaML](DYLIBS/MediaML.md)
- [/System/Library/PrivateFrameworks/MediaMiningKit.framework/MediaMiningKit](DYLIBS/MediaMiningKit.md)
- [/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore](DYLIBS/MediaPlaybackCore.md)
- [/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote](DYLIBS/MediaRemote.md)
- [/System/Library/PrivateFrameworks/MediaServices.framework/MediaServices](DYLIBS/MediaServices.md)
- [/System/Library/PrivateFrameworks/MediaStream.framework/MediaStream](DYLIBS/MediaStream.md)
- [/System/Library/PrivateFrameworks/MedicalIDUI.framework/MedicalIDUI](DYLIBS/MedicalIDUI.md)
- [/System/Library/PrivateFrameworks/MentalHealthUI.framework/MentalHealthUI](DYLIBS/MentalHealthUI.md)
- [/System/Library/PrivateFrameworks/Mercury.framework/Mercury](DYLIBS/Mercury.md)
- [/System/Library/PrivateFrameworks/Message.framework/Message](DYLIBS/Message.md)
- [/System/Library/PrivateFrameworks/MessageProtection.framework/MessageProtection](DYLIBS/MessageProtection.md)
- [/System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity](DYLIBS/MessageSecurity.md)
- [/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/MessagesBlastDoorSupport](DYLIBS/MessagesBlastDoorSupport.md)
- [/System/Library/PrivateFrameworks/MessagesCloudSync.framework/MessagesCloudSync](DYLIBS/MessagesCloudSync.md)
- [/System/Library/PrivateFrameworks/MessagesSettingsUI.framework/MessagesSettingsUI](DYLIBS/MessagesSettingsUI.md)
- [/System/Library/PrivateFrameworks/MetadataUtilities.framework/MetadataUtilities](DYLIBS/MetadataUtilities.md)
- [/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools](DYLIBS/MetalTools.md)
- [/System/Library/PrivateFrameworks/MetricMeasurement.framework/MetricMeasurement](DYLIBS/MetricMeasurement.md)
- [/System/Library/PrivateFrameworks/MetricsFramework.framework/MetricsFramework](DYLIBS/MetricsFramework.md)
- [/System/Library/PrivateFrameworks/MicroLocation.framework/MicroLocation](DYLIBS/MicroLocation.md)
- [/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon](DYLIBS/MicroLocationDaemon.md)
- [/System/Library/PrivateFrameworks/MicroLocationUtilities.framework/MicroLocationUtilities](DYLIBS/MicroLocationUtilities.md)
- [/System/Library/PrivateFrameworks/MigrationKit.framework/MigrationKit](DYLIBS/MigrationKit.md)
- [/System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset](DYLIBS/MobileAsset.md)
- [/System/Library/PrivateFrameworks/MobileMailUI.framework/MobileMailUI](DYLIBS/MobileMailUI.md)
- [/System/Library/PrivateFrameworks/MobileSafari.framework/MobileSafari](DYLIBS/MobileSafari.md)
- [/System/Library/PrivateFrameworks/MobileSafariUI.framework/MobileSafariUI](DYLIBS/MobileSafariUI.md)
- [/System/Library/PrivateFrameworks/MobileSpotlightIndex.framework/MobileSpotlightIndex](DYLIBS/MobileSpotlightIndex.md)
- [/System/Library/PrivateFrameworks/MobileStoreDemoKit.framework/MobileStoreDemoKit](DYLIBS/MobileStoreDemoKit.md)
- [/System/Library/PrivateFrameworks/MobileStoreDemoSetupUI.framework/MobileStoreDemoSetupUI](DYLIBS/MobileStoreDemoSetupUI.md)
- [/System/Library/PrivateFrameworks/MobileStoreUI.framework/MobileStoreUI](DYLIBS/MobileStoreUI.md)
- [/System/Library/PrivateFrameworks/MobileTimerSupport.framework/MobileTimerSupport](DYLIBS/MobileTimerSupport.md)
- [/System/Library/PrivateFrameworks/ModelCatalog.framework/ModelCatalog](DYLIBS/ModelCatalog.md)
- [/System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/ModelCatalogRuntime](DYLIBS/ModelCatalogRuntime.md)
- [/System/Library/PrivateFrameworks/ModelManagerServices.framework/ModelManagerServices](DYLIBS/ModelManagerServices.md)
- [/System/Library/PrivateFrameworks/Morpheus.framework/Morpheus](DYLIBS/Morpheus.md)
- [/System/Library/PrivateFrameworks/MusicKitInternal.framework/MusicKitInternal](DYLIBS/MusicKitInternal.md)
- [/System/Library/PrivateFrameworks/MusicLibrary.framework/MusicLibrary](DYLIBS/MusicLibrary.md)
- [/System/Library/PrivateFrameworks/MusicUI.framework/MusicUI](DYLIBS/MusicUI.md)
- [/System/Library/PrivateFrameworks/NanoAppRegistry.framework/NanoAppRegistry](DYLIBS/NanoAppRegistry.md)
- [/System/Library/PrivateFrameworks/NanoPassKit.framework/NanoPassKit](DYLIBS/NanoPassKit.md)
- [/System/Library/PrivateFrameworks/NanoTimeKit.framework/NanoTimeKit](DYLIBS/NanoTimeKit.md)
- [/System/Library/PrivateFrameworks/Navigation.framework/Navigation](DYLIBS/Navigation.md)
- [/System/Library/PrivateFrameworks/NetAppsUtilities.framework/NetAppsUtilities](DYLIBS/NetAppsUtilities.md)
- [/System/Library/PrivateFrameworks/NetworkStatistics.framework/NetworkStatistics](DYLIBS/NetworkStatistics.md)
- [/System/Library/PrivateFrameworks/NeuralNetworks.framework/NeuralNetworks](DYLIBS/NeuralNetworks.md)
- [/System/Library/PrivateFrameworks/NeutrinoCore.framework/NeutrinoCore](DYLIBS/NeutrinoCore.md)
- [/System/Library/PrivateFrameworks/NeutrinoKit.framework/NeutrinoKit](DYLIBS/NeutrinoKit.md)
- [/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/NewDeviceOutreach](DYLIBS/NewDeviceOutreach.md)
- [/System/Library/PrivateFrameworks/NewDeviceOutreachUI.framework/NewDeviceOutreachUI](DYLIBS/NewDeviceOutreachUI.md)
- [/System/Library/PrivateFrameworks/NewsAds.framework/NewsAds](DYLIBS/NewsAds.md)
- [/System/Library/PrivateFrameworks/NewsAnalytics.framework/NewsAnalytics](DYLIBS/NewsAnalytics.md)
- [/System/Library/PrivateFrameworks/NewsArticles.framework/NewsArticles](DYLIBS/NewsArticles.md)
- [/System/Library/PrivateFrameworks/NewsCore.framework/NewsCore](DYLIBS/NewsCore.md)
- [/System/Library/PrivateFrameworks/NewsFeed.framework/NewsFeed](DYLIBS/NewsFeed.md)
- [/System/Library/PrivateFrameworks/NewsFoundation.framework/NewsFoundation](DYLIBS/NewsFoundation.md)
- [/System/Library/PrivateFrameworks/NewsLiveActivitiesCore.framework/NewsLiveActivitiesCore](DYLIBS/NewsLiveActivitiesCore.md)
- [/System/Library/PrivateFrameworks/NewsPersonalization.framework/NewsPersonalization](DYLIBS/NewsPersonalization.md)
- [/System/Library/PrivateFrameworks/NewsSubscription.framework/NewsSubscription](DYLIBS/NewsSubscription.md)
- [/System/Library/PrivateFrameworks/NewsUI2.framework/NewsUI2](DYLIBS/NewsUI2.md)
- [/System/Library/PrivateFrameworks/NexusDaemon.framework/NexusDaemon](DYLIBS/NexusDaemon.md)
- [/System/Library/PrivateFrameworks/NightingaleTraining.framework/NightingaleTraining](DYLIBS/NightingaleTraining.md)
- [/System/Library/PrivateFrameworks/NotesEditor.framework/NotesEditor](DYLIBS/NotesEditor.md)
- [/System/Library/PrivateFrameworks/NotesShared.framework/NotesShared](DYLIBS/NotesShared.md)
- [/System/Library/PrivateFrameworks/NotesUI.framework/NotesUI](DYLIBS/NotesUI.md)
- [/System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit](DYLIBS/OnBoardingKit.md)
- [/System/Library/PrivateFrameworks/PBBridgeSupport.framework/PBBridgeSupport](DYLIBS/PBBridgeSupport.md)
- [/System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry](DYLIBS/PairedDeviceRegistry.md)
- [/System/Library/PrivateFrameworks/PairedSync.framework/PairedSync](DYLIBS/PairedSync.md)
- [/System/Library/PrivateFrameworks/PaperBoardUI.framework/PaperBoardUI](DYLIBS/PaperBoardUI.md)
- [/System/Library/PrivateFrameworks/PaperKit.framework/PaperKit](DYLIBS/PaperKit.md)
- [/System/Library/PrivateFrameworks/ParsecSubscriptionServiceSupport.framework/ParsecSubscriptionServiceSupport](DYLIBS/ParsecSubscriptionServiceSupport.md)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore](DYLIBS/PassKitCore.md)
- [/System/Library/PrivateFrameworks/PassKitUI.framework/PassKitUI](DYLIBS/PassKitUI.md)
- [/System/Library/PrivateFrameworks/PasswordManagerUI.framework/PasswordManagerUI](DYLIBS/PasswordManagerUI.md)
- [/System/Library/PrivateFrameworks/Pasteboard.framework/Pasteboard](DYLIBS/Pasteboard.md)
- [/System/Library/PrivateFrameworks/PaymentUIBase.framework/PaymentUIBase](DYLIBS/PaymentUIBase.md)
- [/System/Library/PrivateFrameworks/PegasusAPI.framework/PegasusAPI](DYLIBS/PegasusAPI.md)
- [/System/Library/PrivateFrameworks/PegasusConfiguration.framework/PegasusConfiguration](DYLIBS/PegasusConfiguration.md)
- [/System/Library/PrivateFrameworks/PegasusKit.framework/PegasusKit](DYLIBS/PegasusKit.md)
- [/System/Library/PrivateFrameworks/PegasusPersistence.framework/PegasusPersistence](DYLIBS/PegasusPersistence.md)
- [/System/Library/PrivateFrameworks/People.framework/People](DYLIBS/People.md)
- [/System/Library/PrivateFrameworks/PeopleSuggester.framework/PeopleSuggester](DYLIBS/PeopleSuggester.md)
- [/System/Library/PrivateFrameworks/PeopleSuggesterLighthouse.framework/PeopleSuggesterLighthouse](DYLIBS/PeopleSuggesterLighthouse.md)
- [/System/Library/PrivateFrameworks/PerfPowerServicesMetadata.framework/PerfPowerServicesMetadata](DYLIBS/PerfPowerServicesMetadata.md)
- [/System/Library/PrivateFrameworks/PerfPowerServicesReader.framework/PerfPowerServicesReader](DYLIBS/PerfPowerServicesReader.md)
- [/System/Library/PrivateFrameworks/PersistentConnection.framework/PersistentConnection](DYLIBS/PersistentConnection.md)
- [/System/Library/PrivateFrameworks/PersonalizationPortraitInternals.framework/PersonalizationPortraitInternals](DYLIBS/PersonalizationPortraitInternals.md)
- [/System/Library/PrivateFrameworks/PhotoAnalysis.framework/PhotoAnalysis](DYLIBS/PhotoAnalysis.md)
- [/System/Library/PrivateFrameworks/PhotoImaging.framework/PhotoImaging](DYLIBS/PhotoImaging.md)
- [/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/PhotoLibraryServices](DYLIBS/PhotoLibraryServices.md)
- [/System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/PhotoLibraryServicesCore](DYLIBS/PhotoLibraryServicesCore.md)
- [/System/Library/PrivateFrameworks/PhotosFace.framework/PhotosFace](DYLIBS/PhotosFace.md)
- [/System/Library/PrivateFrameworks/PhotosFaceCore.framework/PhotosFaceCore](DYLIBS/PhotosFaceCore.md)
- [/System/Library/PrivateFrameworks/PhotosFaceLayoutCore.framework/PhotosFaceLayoutCore](DYLIBS/PhotosFaceLayoutCore.md)
- [/System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats](DYLIBS/PhotosFormats.md)
- [/System/Library/PrivateFrameworks/PhotosGraph.framework/PhotosGraph](DYLIBS/PhotosGraph.md)
- [/System/Library/PrivateFrameworks/PhotosImagingFoundation.framework/PhotosImagingFoundation](DYLIBS/PhotosImagingFoundation.md)
- [/System/Library/PrivateFrameworks/PhotosIntelligence.framework/PhotosIntelligence](DYLIBS/PhotosIntelligence.md)
- [/System/Library/PrivateFrameworks/PhotosSwiftUICore.framework/PhotosSwiftUICore](DYLIBS/PhotosSwiftUICore.md)
- [/System/Library/PrivateFrameworks/PhotosUICore.framework/PhotosUICore](DYLIBS/PhotosUICore.md)
- [/System/Library/PrivateFrameworks/PhotosUIEdit.framework/PhotosUIEdit](DYLIBS/PhotosUIEdit.md)
- [/System/Library/PrivateFrameworks/PhotosUIFoundation.framework/PhotosUIFoundation](DYLIBS/PhotosUIFoundation.md)
- [/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PhotosUIPrivate](DYLIBS/PhotosUIPrivate.md)
- [/System/Library/PrivateFrameworks/PhotosensitivityProcessing.framework/PhotosensitivityProcessing](DYLIBS/PhotosensitivityProcessing.md)
- [/System/Library/PrivateFrameworks/PlugInKit.framework/PlugInKit](DYLIBS/PlugInKit.md)
- [/System/Library/PrivateFrameworks/PnROnDeviceFramework.framework/PnROnDeviceFramework](DYLIBS/PnROnDeviceFramework.md)
- [/System/Library/PrivateFrameworks/PodcastsFoundation.framework/PodcastsFoundation](DYLIBS/PodcastsFoundation.md)
- [/System/Library/PrivateFrameworks/PodcastsUI.framework/PodcastsUI](DYLIBS/PodcastsUI.md)
- [/System/Library/PrivateFrameworks/PoirotBlocks.framework/PoirotBlocks](DYLIBS/PoirotBlocks.md)
- [/System/Library/PrivateFrameworks/PoirotUDFs.framework/PoirotUDFs](DYLIBS/PoirotUDFs.md)
- [/System/Library/PrivateFrameworks/PostSiriEngagement.framework/PostSiriEngagement](DYLIBS/PostSiriEngagement.md)
- [/System/Library/PrivateFrameworks/PosterBoard.framework/PosterBoard](DYLIBS/PosterBoard.md)
- [/System/Library/PrivateFrameworks/PosterBoardServices.framework/PosterBoardServices](DYLIBS/PosterBoardServices.md)
- [/System/Library/PrivateFrameworks/PosterFoundation.framework/PosterFoundation](DYLIBS/PosterFoundation.md)
- [/System/Library/PrivateFrameworks/PosterKit.framework/PosterKit](DYLIBS/PosterKit.md)
- [/System/Library/PrivateFrameworks/PosterPlatformSupport.framework/PosterPlatformSupport](DYLIBS/PosterPlatformSupport.md)
- [/System/Library/PrivateFrameworks/PosterUIFoundation.framework/PosterUIFoundation](DYLIBS/PosterUIFoundation.md)
- [/System/Library/PrivateFrameworks/PowerExperience.framework/PowerExperience](DYLIBS/PowerExperience.md)
- [/System/Library/PrivateFrameworks/PowerLog.framework/PowerLog](DYLIBS/PowerLog.md)
- [/System/Library/PrivateFrameworks/PowerlogControl.framework/PowerlogControl](DYLIBS/PowerlogControl.md)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore](DYLIBS/PowerlogCore.md)
- [/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators](DYLIBS/PowerlogHelperdOperators.md)
- [/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators](DYLIBS/PowerlogLiteOperators.md)
- [/System/Library/PrivateFrameworks/Preferences.framework/Preferences](DYLIBS/Preferences.md)
- [/System/Library/PrivateFrameworks/PreferencesExtended.framework/PreferencesExtended](DYLIBS/PreferencesExtended.md)
- [/System/Library/PrivateFrameworks/PreferencesUI.framework/PreferencesUI](DYLIBS/PreferencesUI.md)
- [/System/Library/PrivateFrameworks/PreviewShellKit.framework/PreviewShellKit](DYLIBS/PreviewShellKit.md)
- [/System/Library/PrivateFrameworks/PreviewsFoundationOS.framework/PreviewsFoundationOS](DYLIBS/PreviewsFoundationOS.md)
- [/System/Library/PrivateFrameworks/PrintKit.framework/PrintKit](DYLIBS/PrintKit.md)
- [/System/Library/PrivateFrameworks/PrivacyAccounting.framework/PrivacyAccounting](DYLIBS/PrivacyAccounting.md)
- [/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PrivateFederatedLearning](DYLIBS/PrivateFederatedLearning.md)
- [/System/Library/PrivateFrameworks/ProVideo.framework/ProVideo](DYLIBS/ProVideo.md)
- [/System/Library/PrivateFrameworks/ProactiveContextClient.framework/ProactiveContextClient](DYLIBS/ProactiveContextClient.md)
- [/System/Library/PrivateFrameworks/ProactiveEventTracker.framework/ProactiveEventTracker](DYLIBS/ProactiveEventTracker.md)
- [/System/Library/PrivateFrameworks/ProactiveExperiments.framework/ProactiveExperiments](DYLIBS/ProactiveExperiments.md)
- [/System/Library/PrivateFrameworks/ProactiveHarvesting.framework/ProactiveHarvesting](DYLIBS/ProactiveHarvesting.md)
- [/System/Library/PrivateFrameworks/ProactiveML.framework/ProactiveML](DYLIBS/ProactiveML.md)
- [/System/Library/PrivateFrameworks/ProactiveSummarization.framework/ProactiveSummarization](DYLIBS/ProactiveSummarization.md)
- [/System/Library/PrivateFrameworks/ProactiveSummarizationClient.framework/ProactiveSummarizationClient](DYLIBS/ProactiveSummarizationClient.md)
- [/System/Library/PrivateFrameworks/ProactiveSupport.framework/ProactiveSupport](DYLIBS/ProactiveSupport.md)
- [/System/Library/PrivateFrameworks/ProductKit.framework/ProductKit](DYLIBS/ProductKit.md)
- [/System/Library/PrivateFrameworks/PromotedContent.framework/PromotedContent](DYLIBS/PromotedContent.md)
- [/System/Library/PrivateFrameworks/PromotedContentUI.framework/PromotedContentUI](DYLIBS/PromotedContentUI.md)
- [/System/Library/PrivateFrameworks/PromptKit.framework/PromptKit](DYLIBS/PromptKit.md)
- [/System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/ProtectedCloudStorage](DYLIBS/ProtectedCloudStorage.md)
- [/System/Library/PrivateFrameworks/PrototypeToolsUI.framework/PrototypeToolsUI](DYLIBS/PrototypeToolsUI.md)
- [/System/Library/PrivateFrameworks/ProxCardKit.framework/ProxCardKit](DYLIBS/ProxCardKit.md)
- [/System/Library/PrivateFrameworks/ProximityAppleIDSetup.framework/ProximityAppleIDSetup](DYLIBS/ProximityAppleIDSetup.md)
- [/System/Library/PrivateFrameworks/ProximityAppleIDSetupUI.framework/ProximityAppleIDSetupUI](DYLIBS/ProximityAppleIDSetupUI.md)
- [/System/Library/PrivateFrameworks/ProximityControl.framework/ProximityControl](DYLIBS/ProximityControl.md)
- [/System/Library/PrivateFrameworks/ProximityReaderDaemon.framework/ProximityReaderDaemon](DYLIBS/ProximityReaderDaemon.md)
- [/System/Library/PrivateFrameworks/QOSToolkit.framework/QOSToolkit](DYLIBS/QOSToolkit.md)
- [/System/Library/PrivateFrameworks/Quagga.framework/Quagga](DYLIBS/Quagga.md)
- [/System/Library/PrivateFrameworks/QueryParser.framework/QueryParser](DYLIBS/QueryParser.md)
- [/System/Library/PrivateFrameworks/QuickLookSupport.framework/QuickLookSupport](DYLIBS/QuickLookSupport.md)
- [/System/Library/PrivateFrameworks/QuickLookThumbnailingDaemon.framework/QuickLookThumbnailingDaemon](DYLIBS/QuickLookThumbnailingDaemon.md)
- [/System/Library/PrivateFrameworks/QuickLookUICore.framework/QuickLookUICore](DYLIBS/QuickLookUICore.md)
- [/System/Library/PrivateFrameworks/RTTUI.framework/RTTUI](DYLIBS/RTTUI.md)
- [/System/Library/PrivateFrameworks/Rapport.framework/Rapport](DYLIBS/Rapport.md)
- [/System/Library/PrivateFrameworks/RapportUI.framework/RapportUI](DYLIBS/RapportUI.md)
- [/System/Library/PrivateFrameworks/Recap.framework/Recap](DYLIBS/Recap.md)
- [/System/Library/PrivateFrameworks/Recon3D.framework/Recon3D](DYLIBS/Recon3D.md)
- [/System/Library/PrivateFrameworks/RegulatoryDomain.framework/RegulatoryDomain](DYLIBS/RegulatoryDomain.md)
- [/System/Library/PrivateFrameworks/RelevanceEngine.framework/RelevanceEngine](DYLIBS/RelevanceEngine.md)
- [/System/Library/PrivateFrameworks/ReminderKitInternal.framework/ReminderKitInternal](DYLIBS/ReminderKitInternal.md)
- [/System/Library/PrivateFrameworks/RemindersAppIntents.framework/RemindersAppIntents](DYLIBS/RemindersAppIntents.md)
- [/System/Library/PrivateFrameworks/RemindersIntentsFramework.framework/RemindersIntentsFramework](DYLIBS/RemindersIntentsFramework.md)
- [/System/Library/PrivateFrameworks/RemindersUICore.framework/RemindersUICore](DYLIBS/RemindersUICore.md)
- [/System/Library/PrivateFrameworks/RemoteConfiguration.framework/RemoteConfiguration](DYLIBS/RemoteConfiguration.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/RemoteManagement](DYLIBS/RemoteManagement.md)
- [/System/Library/PrivateFrameworks/RemoteManagementModel.framework/RemoteManagementModel](DYLIBS/RemoteManagementModel.md)
- [/System/Library/PrivateFrameworks/RemoteManagementStore.framework/RemoteManagementStore](DYLIBS/RemoteManagementStore.md)
- [/System/Library/PrivateFrameworks/RemotePairingDevice.framework/RemotePairingDevice](DYLIBS/RemotePairingDevice.md)
- [/System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/RemoteServiceDiscovery](DYLIBS/RemoteServiceDiscovery.md)
- [/System/Library/PrivateFrameworks/RemoteUI.framework/RemoteUI](DYLIBS/RemoteUI.md)
- [/System/Library/PrivateFrameworks/RemoteXPC.framework/RemoteXPC](DYLIBS/RemoteXPC.md)
- [/System/Library/PrivateFrameworks/RenderBox.framework/RenderBox](DYLIBS/RenderBox.md)
- [/System/Library/PrivateFrameworks/ReplicatorCore.framework/ReplicatorCore](DYLIBS/ReplicatorCore.md)
- [/System/Library/PrivateFrameworks/ReplicatorEngine.framework/ReplicatorEngine](DYLIBS/ReplicatorEngine.md)
- [/System/Library/PrivateFrameworks/ReplicatorServices.framework/ReplicatorServices](DYLIBS/ReplicatorServices.md)
- [/System/Library/PrivateFrameworks/ReportingPlugin.framework/ReportingPlugin](DYLIBS/ReportingPlugin.md)
- [/System/Library/PrivateFrameworks/RequestDispatcherBridges.framework/RequestDispatcherBridges](DYLIBS/RequestDispatcherBridges.md)
- [/System/Library/PrivateFrameworks/RunningBoard.framework/RunningBoard](DYLIBS/RunningBoard.md)
- [/System/Library/PrivateFrameworks/RuntimeInternal.framework/RuntimeInternal](DYLIBS/RuntimeInternal.md)
- [/System/Library/PrivateFrameworks/SIMSetupSupport.framework/SIMSetupSupport](DYLIBS/SIMSetupSupport.md)
- [/System/Library/PrivateFrameworks/SOS.framework/SOS](DYLIBS/SOS.md)
- [/System/Library/PrivateFrameworks/SOSUI.framework/SOSUI](DYLIBS/SOSUI.md)
- [/System/Library/PrivateFrameworks/SafariCore.framework/SafariCore](DYLIBS/SafariCore.md)
- [/System/Library/PrivateFrameworks/SafariFoundation.framework/SafariFoundation](DYLIBS/SafariFoundation.md)
- [/System/Library/PrivateFrameworks/SafariShared.framework/SafariShared](DYLIBS/SafariShared.md)
- [/System/Library/PrivateFrameworks/SafariSharedUI.framework/SafariSharedUI](DYLIBS/SafariSharedUI.md)
- [/System/Library/PrivateFrameworks/SafetyMonitor.framework/SafetyMonitor](DYLIBS/SafetyMonitor.md)
- [/System/Library/PrivateFrameworks/SafetyMonitorUI.framework/SafetyMonitorUI](DYLIBS/SafetyMonitorUI.md)
- [/System/Library/PrivateFrameworks/Sage.framework/Sage](DYLIBS/Sage.md)
- [/System/Library/PrivateFrameworks/SampleAnalysis.framework/Frameworks/SAHelper.framework/SAHelper](DYLIBS/SAHelper.md)
- [/System/Library/PrivateFrameworks/SampleAnalysis.framework/SampleAnalysis](DYLIBS/SampleAnalysis.md)
- [/System/Library/PrivateFrameworks/ScreenReaderBrailleDriver.framework/ScreenReaderBrailleDriver](DYLIBS/ScreenReaderBrailleDriver.md)
- [/System/Library/PrivateFrameworks/ScreenReaderCore.framework/ScreenReaderCore](DYLIBS/ScreenReaderCore.md)
- [/System/Library/PrivateFrameworks/ScreenReaderOutput.framework/ScreenReaderOutput](DYLIBS/ScreenReaderOutput.md)
- [/System/Library/PrivateFrameworks/ScreenSharingKit.framework/ScreenSharingKit](DYLIBS/ScreenSharingKit.md)
- [/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore](DYLIBS/ScreenTimeCore.md)
- [/System/Library/PrivateFrameworks/ScreenTimeSettingsUI.framework/ScreenTimeSettingsUI](DYLIBS/ScreenTimeSettingsUI.md)
- [/System/Library/PrivateFrameworks/ScreenTimeUICore.framework/ScreenTimeUICore](DYLIBS/ScreenTimeUICore.md)
- [/System/Library/PrivateFrameworks/Search.framework/Search](DYLIBS/Search.md)
- [/System/Library/PrivateFrameworks/SearchAds.framework/SearchAds](DYLIBS/SearchAds.md)
- [/System/Library/PrivateFrameworks/SearchFoundation.framework/SearchFoundation](DYLIBS/SearchFoundation.md)
- [/System/Library/PrivateFrameworks/SearchUI.framework/SearchUI](DYLIBS/SearchUI.md)
- [/System/Library/PrivateFrameworks/SearchUICardKitProviderSupport.framework/SearchUICardKitProviderSupport](DYLIBS/SearchUICardKitProviderSupport.md)
- [/System/Library/PrivateFrameworks/Seeding.framework/Seeding](DYLIBS/Seeding.md)
- [/System/Library/PrivateFrameworks/SensingAlgsService.framework/SensingAlgsService](DYLIBS/SensingAlgsService.md)
- [/System/Library/PrivateFrameworks/SentencePiece.framework/SentencePiece](DYLIBS/SentencePiece.md)
- [/System/Library/PrivateFrameworks/SentencePieceInternal.framework/SentencePieceInternal](DYLIBS/SentencePieceInternal.md)
- [/System/Library/PrivateFrameworks/ServiceExtensions.framework/ServiceExtensions](DYLIBS/ServiceExtensions.md)
- [/System/Library/PrivateFrameworks/ServiceManagement.framework/ServiceManagement](DYLIBS/ServiceManagement.md)
- [/System/Library/PrivateFrameworks/SessionAssertion.framework/SessionAssertion](DYLIBS/SessionAssertion.md)
- [/System/Library/PrivateFrameworks/SessionCore.framework/SessionCore](DYLIBS/SessionCore.md)
- [/System/Library/PrivateFrameworks/SessionFoundation.framework/SessionFoundation](DYLIBS/SessionFoundation.md)
- [/System/Library/PrivateFrameworks/SessionPushNotifications.framework/SessionPushNotifications](DYLIBS/SessionPushNotifications.md)
- [/System/Library/PrivateFrameworks/SessionSyncEngine.framework/SessionSyncEngine](DYLIBS/SessionSyncEngine.md)
- [/System/Library/PrivateFrameworks/Settings.framework/Settings](DYLIBS/Settings.md)
- [/System/Library/PrivateFrameworks/Settings/DisplayAndBrightnessSettings.framework/DisplayAndBrightnessSettings](DYLIBS/DisplayAndBrightnessSettings.md)
- [/System/Library/PrivateFrameworks/Settings/GeneralSettingsUI.framework/GeneralSettingsUI](DYLIBS/GeneralSettingsUI.md)
- [/System/Library/PrivateFrameworks/Settings/PrivacySettingsUI.framework/PrivacySettingsUI](DYLIBS/PrivacySettingsUI.md)
- [/System/Library/PrivateFrameworks/Settings/SettingsUIKitPrivate.framework/SettingsUIKitPrivate](DYLIBS/SettingsUIKitPrivate.md)
- [/System/Library/PrivateFrameworks/SettingsCellularUI.framework/SettingsCellularUI](DYLIBS/SettingsCellularUI.md)
- [/System/Library/PrivateFrameworks/SettingsFoundation.framework/SettingsFoundation](DYLIBS/SettingsFoundation.md)
- [/System/Library/PrivateFrameworks/SetupAssistantUI.framework/SetupAssistantUI](DYLIBS/SetupAssistantUI.md)
- [/System/Library/PrivateFrameworks/SetupKit.framework/SetupKit](DYLIBS/SetupKit.md)
- [/System/Library/PrivateFrameworks/SeymourClient.framework/SeymourClient](DYLIBS/SeymourClient.md)
- [/System/Library/PrivateFrameworks/SeymourClientServices.framework/SeymourClientServices](DYLIBS/SeymourClientServices.md)
- [/System/Library/PrivateFrameworks/SeymourCore.framework/SeymourCore](DYLIBS/SeymourCore.md)
- [/System/Library/PrivateFrameworks/SeymourMedia.framework/SeymourMedia](DYLIBS/SeymourMedia.md)
- [/System/Library/PrivateFrameworks/SeymourServices.framework/SeymourServices](DYLIBS/SeymourServices.md)
- [/System/Library/PrivateFrameworks/SeymourUI.framework/SeymourUI](DYLIBS/SeymourUI.md)
- [/System/Library/PrivateFrameworks/ShaderGraph.framework/ShaderGraph](DYLIBS/ShaderGraph.md)
- [/System/Library/PrivateFrameworks/Sharing.framework/Sharing](DYLIBS/Sharing.md)
- [/System/Library/PrivateFrameworks/ShazamCore.framework/ShazamCore](DYLIBS/ShazamCore.md)
- [/System/Library/PrivateFrameworks/ShazamEvents.framework/ShazamEvents](DYLIBS/ShazamEvents.md)
- [/System/Library/PrivateFrameworks/ShazamKitUI.framework/ShazamKitUI](DYLIBS/ShazamKitUI.md)
- [/System/Library/PrivateFrameworks/ShellSceneKit.framework/ShellSceneKit](DYLIBS/ShellSceneKit.md)
- [/System/Library/PrivateFrameworks/ShimGameServices.framework/ShimGameServices](DYLIBS/ShimGameServices.md)
- [/System/Library/PrivateFrameworks/SignpostCollection.framework/SignpostCollection](DYLIBS/SignpostCollection.md)
- [/System/Library/PrivateFrameworks/SignpostSupport.framework/SignpostSupport](DYLIBS/SignpostSupport.md)
- [/System/Library/PrivateFrameworks/Silex.framework/Silex](DYLIBS/Silex.md)
- [/System/Library/PrivateFrameworks/SiriAnalytics.framework/SiriAnalytics](DYLIBS/SiriAnalytics.md)
- [/System/Library/PrivateFrameworks/SiriAppLaunchIntents.framework/SiriAppLaunchIntents](DYLIBS/SiriAppLaunchIntents.md)
- [/System/Library/PrivateFrameworks/SiriAudioSupport.framework/SiriAudioSupport](DYLIBS/SiriAudioSupport.md)
- [/System/Library/PrivateFrameworks/SiriAutoComplete.framework/SiriAutoComplete](DYLIBS/SiriAutoComplete.md)
- [/System/Library/PrivateFrameworks/SiriCalendarIntents.framework/SiriCalendarIntents](DYLIBS/SiriCalendarIntents.md)
- [/System/Library/PrivateFrameworks/SiriCalendarUI.framework/SiriCalendarUI](DYLIBS/SiriCalendarUI.md)
- [/System/Library/PrivateFrameworks/SiriCam.framework/SiriCam](DYLIBS/SiriCam.md)
- [/System/Library/PrivateFrameworks/SiriContactsIntents.framework/SiriContactsIntents](DYLIBS/SiriContactsIntents.md)
- [/System/Library/PrivateFrameworks/SiriContactsUI.framework/SiriContactsUI](DYLIBS/SiriContactsUI.md)
- [/System/Library/PrivateFrameworks/SiriCore.framework/SiriCore](DYLIBS/SiriCore.md)
- [/System/Library/PrivateFrameworks/SiriCorrections.framework/SiriCorrections](DYLIBS/SiriCorrections.md)
- [/System/Library/PrivateFrameworks/SiriCrossDeviceArbitration.framework/SiriCrossDeviceArbitration](DYLIBS/SiriCrossDeviceArbitration.md)
- [/System/Library/PrivateFrameworks/SiriExpanseInternal.framework/SiriExpanseInternal](DYLIBS/SiriExpanseInternal.md)
- [/System/Library/PrivateFrameworks/SiriExpanseInternalUI.framework/SiriExpanseInternalUI](DYLIBS/SiriExpanseInternalUI.md)
- [/System/Library/PrivateFrameworks/SiriFindMy.framework/SiriFindMy](DYLIBS/SiriFindMy.md)
- [/System/Library/PrivateFrameworks/SiriFlowEnvironment.framework/SiriFlowEnvironment](DYLIBS/SiriFlowEnvironment.md)
- [/System/Library/PrivateFrameworks/SiriGestureBridge.framework/SiriGestureBridge](DYLIBS/SiriGestureBridge.md)
- [/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/SiriIdentityInternal](DYLIBS/SiriIdentityInternal.md)
- [/System/Library/PrivateFrameworks/SiriInCall.framework/SiriInCall](DYLIBS/SiriInCall.md)
- [/System/Library/PrivateFrameworks/SiriInference.framework/SiriInference](DYLIBS/SiriInference.md)
- [/System/Library/PrivateFrameworks/SiriInferenceFlow.framework/SiriInferenceFlow](DYLIBS/SiriInferenceFlow.md)
- [/System/Library/PrivateFrameworks/SiriInformationSearch.framework/SiriInformationSearch](DYLIBS/SiriInformationSearch.md)
- [/System/Library/PrivateFrameworks/SiriKitFlow.framework/SiriKitFlow](DYLIBS/SiriKitFlow.md)
- [/System/Library/PrivateFrameworks/SiriKitRuntime.framework/SiriKitRuntime](DYLIBS/SiriKitRuntime.md)
- [/System/Library/PrivateFrameworks/SiriMailUI.framework/SiriMailUI](DYLIBS/SiriMailUI.md)
- [/System/Library/PrivateFrameworks/SiriMessageBus.framework/SiriMessageBus](DYLIBS/SiriMessageBus.md)
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
- [/System/Library/PrivateFrameworks/SiriPaymentsIntents.framework/SiriPaymentsIntents](DYLIBS/SiriPaymentsIntents.md)
- [/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/SiriPlaybackControlIntents](DYLIBS/SiriPlaybackControlIntents.md)
- [/System/Library/PrivateFrameworks/SiriPlaybackControlSupport.framework/SiriPlaybackControlSupport](DYLIBS/SiriPlaybackControlSupport.md)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningAnalytics.framework/SiriPrivateLearningAnalytics](DYLIBS/SiriPrivateLearningAnalytics.md)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningInference.framework/SiriPrivateLearningInference](DYLIBS/SiriPrivateLearningInference.md)
- [/System/Library/PrivateFrameworks/SiriReferenceResolver.framework/SiriReferenceResolver](DYLIBS/SiriReferenceResolver.md)
- [/System/Library/PrivateFrameworks/SiriRemembers.framework/SiriRemembers](DYLIBS/SiriRemembers.md)
- [/System/Library/PrivateFrameworks/SiriSettingsIntents.framework/SiriSettingsIntents](DYLIBS/SiriSettingsIntents.md)
- [/System/Library/PrivateFrameworks/SiriSetup.framework/SiriSetup](DYLIBS/SiriSetup.md)
- [/System/Library/PrivateFrameworks/SiriSignals.framework/SiriSignals](DYLIBS/SiriSignals.md)
- [/System/Library/PrivateFrameworks/SiriSuggestions.framework/SiriSuggestions](DYLIBS/SiriSuggestions.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsIntelligence.framework/SiriSuggestionsIntelligence](DYLIBS/SiriSuggestionsIntelligence.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsKit.framework/SiriSuggestionsKit](DYLIBS/SiriSuggestionsKit.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsSupport.framework/SiriSuggestionsSupport](DYLIBS/SiriSuggestionsSupport.md)
- [/System/Library/PrivateFrameworks/SiriTTSService.framework/SiriTTSService](DYLIBS/SiriTTSService.md)
- [/System/Library/PrivateFrameworks/SiriTimeTimerInternal.framework/SiriTimeTimerInternal](DYLIBS/SiriTimeTimerInternal.md)
- [/System/Library/PrivateFrameworks/SiriTranslationIntents.framework/SiriTranslationIntents](DYLIBS/SiriTranslationIntents.md)
- [/System/Library/PrivateFrameworks/SiriTurnTakingManager.framework/SiriTurnTakingManager](DYLIBS/SiriTurnTakingManager.md)
- [/System/Library/PrivateFrameworks/SiriUIBridge.framework/SiriUIBridge](DYLIBS/SiriUIBridge.md)
- [/System/Library/PrivateFrameworks/SiriUserSegments.framework/SiriUserSegments](DYLIBS/SiriUserSegments.md)
- [/System/Library/PrivateFrameworks/SiriUtilities.framework/SiriUtilities](DYLIBS/SiriUtilities.md)
- [/System/Library/PrivateFrameworks/SiriVideoIntents.framework/SiriVideoIntents](DYLIBS/SiriVideoIntents.md)
- [/System/Library/PrivateFrameworks/SleepHealthDaemon.framework/SleepHealthDaemon](DYLIBS/SleepHealthDaemon.md)
- [/System/Library/PrivateFrameworks/SleepHealthUI.framework/SleepHealthUI](DYLIBS/SleepHealthUI.md)
- [/System/Library/PrivateFrameworks/SleepWidgetUI.framework/SleepWidgetUI](DYLIBS/SleepWidgetUI.md)
- [/System/Library/PrivateFrameworks/SnippetKit.framework/SnippetKit](DYLIBS/SnippetKit.md)
- [/System/Library/PrivateFrameworks/SnippetUI.framework/SnippetUI](DYLIBS/SnippetUI.md)
- [/System/Library/PrivateFrameworks/SocialLayer.framework/SocialLayer](DYLIBS/SocialLayer.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateServicesUI.framework/SoftwareUpdateServicesUI](DYLIBS/SoftwareUpdateServicesUI.md)
- [/System/Library/PrivateFrameworks/SonicFoundation.framework/SonicFoundation](DYLIBS/SonicFoundation.md)
- [/System/Library/PrivateFrameworks/SpatialInspectorFoundation.framework/SpatialInspectorFoundation](DYLIBS/SpatialInspectorFoundation.md)
- [/System/Library/PrivateFrameworks/SpeechRecognitionCommandAndControl.framework/SpeechRecognitionCommandAndControl](DYLIBS/SpeechRecognitionCommandAndControl.md)
- [/System/Library/PrivateFrameworks/SpeechRecognitionCommandServices.framework/SpeechRecognitionCommandServices](DYLIBS/SpeechRecognitionCommandServices.md)
- [/System/Library/PrivateFrameworks/Spotlight.framework/Spotlight](DYLIBS/Spotlight.md)
- [/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon](DYLIBS/SpotlightDaemon.md)
- [/System/Library/PrivateFrameworks/SpotlightLinguistics.framework/SpotlightLinguistics](DYLIBS/SpotlightLinguistics.md)
- [/System/Library/PrivateFrameworks/SpotlightReceiver.framework/SpotlightReceiver](DYLIBS/SpotlightReceiver.md)
- [/System/Library/PrivateFrameworks/SpotlightResources.framework/SpotlightResources](DYLIBS/SpotlightResources.md)
- [/System/Library/PrivateFrameworks/SpotlightServices.framework/SpotlightServices](DYLIBS/SpotlightServices.md)
- [/System/Library/PrivateFrameworks/SpotlightSettingsSupport.framework/SpotlightSettingsSupport](DYLIBS/SpotlightSettingsSupport.md)
- [/System/Library/PrivateFrameworks/SpotlightUIInternal.framework/SpotlightUIInternal](DYLIBS/SpotlightUIInternal.md)
- [/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard](DYLIBS/SpringBoard.md)
- [/System/Library/PrivateFrameworks/SpringBoardDisplayServices.framework/SpringBoardDisplayServices](DYLIBS/SpringBoardDisplayServices.md)
- [/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation](DYLIBS/SpringBoardFoundation.md)
- [/System/Library/PrivateFrameworks/SpringBoardHome.framework/SpringBoardHome](DYLIBS/SpringBoardHome.md)
- [/System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices](DYLIBS/SpringBoardServices.md)
- [/System/Library/PrivateFrameworks/SpringBoardUI.framework/SpringBoardUI](DYLIBS/SpringBoardUI.md)
- [/System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices](DYLIBS/SpringBoardUIServices.md)
- [/System/Library/PrivateFrameworks/Stateful.framework/Stateful](DYLIBS/Stateful.md)
- [/System/Library/PrivateFrameworks/StatusKitAgentCore.framework/StatusKitAgentCore](DYLIBS/StatusKitAgentCore.md)
- [/System/Library/PrivateFrameworks/Stickers.framework/Stickers](DYLIBS/Stickers.md)
- [/System/Library/PrivateFrameworks/StocksCore.framework/StocksCore](DYLIBS/StocksCore.md)
- [/System/Library/PrivateFrameworks/StocksUI.framework/StocksUI](DYLIBS/StocksUI.md)
- [/System/Library/PrivateFrameworks/StorageKit.framework/StorageKit](DYLIBS/StorageKit.md)
- [/System/Library/PrivateFrameworks/StoreKitUI.framework/StoreKitUI](DYLIBS/StoreKitUI.md)
- [/System/Library/PrivateFrameworks/StreamingExtractor.framework/StreamingExtractor](DYLIBS/StreamingExtractor.md)
- [/System/Library/PrivateFrameworks/SuggestionsSpotlightMetrics.framework/SuggestionsSpotlightMetrics](DYLIBS/SuggestionsSpotlightMetrics.md)
- [/System/Library/PrivateFrameworks/SymptomShared.framework/SymptomShared](DYLIBS/SymptomShared.md)
- [/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomEvaluator.framework/SymptomEvaluator](DYLIBS/SymptomEvaluator.md)
- [/System/Library/PrivateFrameworks/Synapse.framework/Synapse](DYLIBS/Synapse.md)
- [/System/Library/PrivateFrameworks/SyncedModels.framework/SyncedModels](DYLIBS/SyncedModels.md)
- [/System/Library/PrivateFrameworks/SystemApertureUI.framework/SystemApertureUI](DYLIBS/SystemApertureUI.md)
- [/System/Library/PrivateFrameworks/SystemStatusUI.framework/SystemStatusUI](DYLIBS/SystemStatusUI.md)
- [/System/Library/PrivateFrameworks/SystemUIAnimationKit.framework/SystemUIAnimationKit](DYLIBS/SystemUIAnimationKit.md)
- [/System/Library/PrivateFrameworks/TSReading.framework/TSReading](DYLIBS/TSReading.md)
- [/System/Library/PrivateFrameworks/TVAppServices.framework/TVAppServices](DYLIBS/TVAppServices.md)
- [/System/Library/PrivateFrameworks/TVMLKit.framework/TVMLKit](DYLIBS/TVMLKit.md)
- [/System/Library/PrivateFrameworks/TVRemoteUI.framework/TVRemoteUI](DYLIBS/TVRemoteUI.md)
- [/System/Library/PrivateFrameworks/TeaCharts.framework/TeaCharts](DYLIBS/TeaCharts.md)
- [/System/Library/PrivateFrameworks/TeaFoundation.framework/TeaFoundation](DYLIBS/TeaFoundation.md)
- [/System/Library/PrivateFrameworks/TeaUI.framework/TeaUI](DYLIBS/TeaUI.md)
- [/System/Library/PrivateFrameworks/TelephonyBlastDoorSupport.framework/TelephonyBlastDoorSupport](DYLIBS/TelephonyBlastDoorSupport.md)
- [/System/Library/PrivateFrameworks/TelephonyUI.framework/TelephonyUI](DYLIBS/TelephonyUI.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities](DYLIBS/TelephonyUtilities.md)
- [/System/Library/PrivateFrameworks/TemplateKit.framework/TemplateKit](DYLIBS/TemplateKit.md)
- [/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer](DYLIBS/TextComposer.md)
- [/System/Library/PrivateFrameworks/TextFormattingUI.framework/TextFormattingUI](DYLIBS/TextFormattingUI.md)
- [/System/Library/PrivateFrameworks/TextInput.framework/TextInput](DYLIBS/TextInput.md)
- [/System/Library/PrivateFrameworks/TextInputCore.framework/TextInputCore](DYLIBS/TextInputCore.md)
- [/System/Library/PrivateFrameworks/TextInputUI.framework/TextInputUI](DYLIBS/TextInputUI.md)
- [/System/Library/PrivateFrameworks/TextToSpeech.framework/TextToSpeech](DYLIBS/TextToSpeech.md)
- [/System/Library/PrivateFrameworks/TextToSpeechBundleSupport.framework/TextToSpeechBundleSupport](DYLIBS/TextToSpeechBundleSupport.md)
- [/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingUI.framework/TextToSpeechVoiceBankingUI](DYLIBS/TextToSpeechVoiceBankingUI.md)
- [/System/Library/PrivateFrameworks/ThirdPartyApplicationSettings.framework/ThirdPartyApplicationSettings](DYLIBS/ThirdPartyApplicationSettings.md)
- [/System/Library/PrivateFrameworks/Timeline.framework/Timeline](DYLIBS/Timeline.md)
- [/System/Library/PrivateFrameworks/TipKitCore.framework/TipKitCore](DYLIBS/TipKitCore.md)
- [/System/Library/PrivateFrameworks/TipsDaemon.framework/TipsDaemon](DYLIBS/TipsDaemon.md)
- [/System/Library/PrivateFrameworks/TipsUI.framework/TipsUI](DYLIBS/TipsUI.md)
- [/System/Library/PrivateFrameworks/TokenGeneration.framework/TokenGeneration](DYLIBS/TokenGeneration.md)
- [/System/Library/PrivateFrameworks/TokenGenerationCore.framework/TokenGenerationCore](DYLIBS/TokenGenerationCore.md)
- [/System/Library/PrivateFrameworks/TokenGenerationInference.framework/TokenGenerationInference](DYLIBS/TokenGenerationInference.md)
- [/System/Library/PrivateFrameworks/ToolKit.framework/ToolKit](DYLIBS/ToolKit.md)
- [/System/Library/PrivateFrameworks/TranslationUI.framework/TranslationUI](DYLIBS/TranslationUI.md)
- [/System/Library/PrivateFrameworks/UIAccessibility.framework/UIAccessibility](DYLIBS/UIAccessibility.md)
- [/System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation](DYLIBS/UIFoundation.md)
- [/System/Library/PrivateFrameworks/UIIntelligenceSupportAgent.framework/UIIntelligenceSupportAgent](DYLIBS/UIIntelligenceSupportAgent.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore](DYLIBS/UIKitCore.md)
- [/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices](DYLIBS/UIKitServices.md)
- [/System/Library/PrivateFrameworks/UINavigationKit.framework/UINavigationKit](DYLIBS/UINavigationKit.md)
- [/System/Library/PrivateFrameworks/UIUnderstanding.framework/UIUnderstanding](DYLIBS/UIUnderstanding.md)
- [/System/Library/PrivateFrameworks/UniversalDrag.framework/UniversalDrag](DYLIBS/UniversalDrag.md)
- [/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTracking](DYLIBS/UsageTracking.md)
- [/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_apfs.dylib](DYLIBS/livefiles_apfs.dylib.md)
- [/System/Library/PrivateFrameworks/UserNotificationsCore.framework/UserNotificationsCore](DYLIBS/UserNotificationsCore.md)
- [/System/Library/PrivateFrameworks/UserNotificationsUIKit.framework/UserNotificationsUIKit](DYLIBS/UserNotificationsUIKit.md)
- [/System/Library/PrivateFrameworks/VDAF.framework/VDAF](DYLIBS/VDAF.md)
- [/System/Library/PrivateFrameworks/VFX.framework/VFX](DYLIBS/VFX.md)
- [/System/Library/PrivateFrameworks/VectorKit.framework/VectorKit](DYLIBS/VectorKit.md)
- [/System/Library/PrivateFrameworks/VectorSearch.framework/VectorSearch](DYLIBS/VectorSearch.md)
- [/System/Library/PrivateFrameworks/VideoProcessing.framework/VideoProcessing](DYLIBS/VideoProcessing.md)
- [/System/Library/PrivateFrameworks/VideoSubscriberAccountUI.framework/VideoSubscriberAccountUI](DYLIBS/VideoSubscriberAccountUI.md)
- [/System/Library/PrivateFrameworks/VideosUI.framework/VideosUI](DYLIBS/VideosUI.md)
- [/System/Library/PrivateFrameworks/VideosUICore.framework/VideosUICore](DYLIBS/VideosUICore.md)
- [/System/Library/PrivateFrameworks/VirtualGarage.framework/VirtualGarage](DYLIBS/VirtualGarage.md)
- [/System/Library/PrivateFrameworks/VisionCore.framework/VisionCore](DYLIBS/VisionCore.md)
- [/System/Library/PrivateFrameworks/VisionKitCore.framework/VisionKitCore](DYLIBS/VisionKitCore.md)
- [/System/Library/PrivateFrameworks/VisionKitInternal.framework/VisionKitInternal](DYLIBS/VisionKitInternal.md)
- [/System/Library/PrivateFrameworks/VisualGeneration.framework/VisualGeneration](DYLIBS/VisualGeneration.md)
- [/System/Library/PrivateFrameworks/VisualIntelligence.framework/VisualIntelligence](DYLIBS/VisualIntelligence.md)
- [/System/Library/PrivateFrameworks/VisualUnderstanding.framework/VisualUnderstanding](DYLIBS/VisualUnderstanding.md)
- [/System/Library/PrivateFrameworks/VoiceActions.framework/VoiceActions](DYLIBS/VoiceActions.md)
- [/System/Library/PrivateFrameworks/VoiceControl.framework/VoiceControl](DYLIBS/VoiceControl.md)
- [/System/Library/PrivateFrameworks/VoiceOverServices.framework/VoiceOverServices](DYLIBS/VoiceOverServices.md)
- [/System/Library/PrivateFrameworks/VoiceShortcutClient.framework/VoiceShortcutClient](DYLIBS/VoiceShortcutClient.md)
- [/System/Library/PrivateFrameworks/VoiceShortcuts.framework/VoiceShortcuts](DYLIBS/VoiceShortcuts.md)
- [/System/Library/PrivateFrameworks/WPDaemon.framework/WPDaemon](DYLIBS/WPDaemon.md)
- [/System/Library/PrivateFrameworks/WallpaperKit.framework/WallpaperKit](DYLIBS/WallpaperKit.md)
- [/System/Library/PrivateFrameworks/WatchListKit.framework/WatchListKit](DYLIBS/WatchListKit.md)
- [/System/Library/PrivateFrameworks/WeatherCore.framework/WeatherCore](DYLIBS/WeatherCore.md)
- [/System/Library/PrivateFrameworks/WeatherDaemon.framework/WeatherDaemon](DYLIBS/WeatherDaemon.md)
- [/System/Library/PrivateFrameworks/WeatherMaps.framework/WeatherMaps](DYLIBS/WeatherMaps.md)
- [/System/Library/PrivateFrameworks/WeatherUI.framework/WeatherUI](DYLIBS/WeatherUI.md)
- [/System/Library/PrivateFrameworks/WebBookmarks.framework/WebBookmarks](DYLIBS/WebBookmarks.md)
- [/System/Library/PrivateFrameworks/WebBookmarksSwift.framework/WebBookmarksSwift](DYLIBS/WebBookmarksSwift.md)
- [/System/Library/PrivateFrameworks/WebCore.framework/Frameworks/libwebrtc.dylib](DYLIBS/libwebrtc.dylib.md)
- [/System/Library/PrivateFrameworks/WebCore.framework/WebCore](DYLIBS/WebCore.md)
- [/System/Library/PrivateFrameworks/WebKitLegacy.framework/WebKitLegacy](DYLIBS/WebKitLegacy.md)
- [/System/Library/PrivateFrameworks/WebSheet.framework/WebSheet](DYLIBS/WebSheet.md)
- [/System/Library/PrivateFrameworks/WebUI.framework/WebUI](DYLIBS/WebUI.md)
- [/System/Library/PrivateFrameworks/WelcomeKitUI.framework/WelcomeKitUI](DYLIBS/WelcomeKitUI.md)
- [/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics](DYLIBS/WiFiAnalytics.md)
- [/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit](DYLIBS/WiFiKit.md)
- [/System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI](DYLIBS/WiFiKitUI.md)
- [/System/Library/PrivateFrameworks/WidgetRenderer.framework/WidgetRenderer](DYLIBS/WidgetRenderer.md)
- [/System/Library/PrivateFrameworks/WorkflowEditor.framework/WorkflowEditor](DYLIBS/WorkflowEditor.md)
- [/System/Library/PrivateFrameworks/WorkflowKit.framework/WorkflowKit](DYLIBS/WorkflowKit.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/WorkflowUI](DYLIBS/WorkflowUI.md)
- [/System/Library/PrivateFrameworks/WorkflowUICore.framework/WorkflowUICore](DYLIBS/WorkflowUICore.md)
- [/System/Library/PrivateFrameworks/WorkflowUIServices.framework/WorkflowUIServices](DYLIBS/WorkflowUIServices.md)
- [/System/Library/PrivateFrameworks/WorkoutCore.framework/WorkoutCore](DYLIBS/WorkoutCore.md)
- [/System/Library/PrivateFrameworks/WorkoutUI.framework/WorkoutUI](DYLIBS/WorkoutUI.md)
- [/System/Library/PrivateFrameworks/WritingToolsUI.framework/WritingToolsUI](DYLIBS/WritingToolsUI.md)
- [/System/Library/PrivateFrameworks/XOJIT.framework/XOJIT](DYLIBS/XOJIT.md)
- [/System/Library/PrivateFrameworks/_JetEngine_SwiftUI.framework/_JetEngine_SwiftUI](DYLIBS/_JetEngine_SwiftUI.md)
- [/System/Library/PrivateFrameworks/_MusicKitInternal_MediaPlaybackCore.framework/_MusicKitInternal_MediaPlaybackCore](DYLIBS/_MusicKitInternal_MediaPlaybackCore.md)
- [/System/Library/PrivateFrameworks/_MusicKitInternal_SwiftUI.framework/_MusicKitInternal_SwiftUI](DYLIBS/_MusicKitInternal_SwiftUI.md)
- [/System/Library/PrivateFrameworks/_SonicKit_MusicKit.framework/_SonicKit_MusicKit](DYLIBS/_SonicKit_MusicKit.md)
- [/System/Library/PrivateFrameworks/caulk.framework/caulk](DYLIBS/caulk.md)
- [/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore](DYLIBS/iCloudDriveCore.md)
- [/System/Library/PrivateFrameworks/iCloudQuota.framework/iCloudQuota](DYLIBS/iCloudQuota.md)
- [/System/Library/PrivateFrameworks/iCloudQuotaUI.framework/iCloudQuotaUI](DYLIBS/iCloudQuotaUI.md)
- [/System/Library/PrivateFrameworks/iCloudSettings.framework/iCloudSettings](DYLIBS/iCloudSettings.md)
- [/System/Library/PrivateFrameworks/iCloudSubscriptionOptimizerDaemon.framework/iCloudSubscriptionOptimizerDaemon](DYLIBS/iCloudSubscriptionOptimizerDaemon.md)
- [/System/Library/PrivateFrameworks/iTunesCloud.framework/iTunesCloud](DYLIBS/iTunesCloud.md)
- [/System/Library/PrivateFrameworks/icloudMCCKit.framework/icloudMCCKit](DYLIBS/icloudMCCKit.md)
- [/System/Library/TextInput/TextInput_ko.bundle/TextInput_ko](DYLIBS/TextInput_ko.md)
- [/System/Library/VideoDecoders/AV1SW.videodecoder](DYLIBS/AV1SW.videodecoder.md)
- [/System/Library/VideoDecoders/H264H8.videodecoder](DYLIBS/H264H8.videodecoder.md)
- [/System/Library/VideoEncoders/H264H9.videoencoder](DYLIBS/H264H9.videoencoder.md)
- [/System/Library/VideoEncoders/H9.videoencoder](DYLIBS/H9.videoencoder.md)
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
- [/usr/lib/dyld](DYLIBS/dyld.md)
- [/usr/lib/libATCommandStudioDynamic.dylib](DYLIBS/libATCommandStudioDynamic.dylib.md)
- [/usr/lib/libAccessibility.dylib](DYLIBS/libAccessibility.dylib.md)
- [/usr/lib/libAppleArchive.dylib](DYLIBS/libAppleArchive.dylib.md)
- [/usr/lib/libAppletTranslationLibrary.dylib](DYLIBS/libAppletTranslationLibrary.dylib.md)
- [/usr/lib/libBBUpdaterDynamic.dylib](DYLIBS/libBBUpdaterDynamic.dylib.md)
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
- [/usr/lib/libMTLHud.dylib](DYLIBS/libMTLHud.dylib.md)
- [/usr/lib/libQMIParserDynamic.dylib](DYLIBS/libQMIParserDynamic.dylib.md)
- [/usr/lib/libSoftwareUpdateSSO.dylib](DYLIBS/libSoftwareUpdateSSO.dylib.md)
- [/usr/lib/libTelephonyBasebandDynamic.dylib](DYLIBS/libTelephonyBasebandDynamic.dylib.md)
- [/usr/lib/libTelephonyCapabilities.dylib](DYLIBS/libTelephonyCapabilities.dylib.md)
- [/usr/lib/libTelephonyDebugDynamic.dylib](DYLIBS/libTelephonyDebugDynamic.dylib.md)
- [/usr/lib/libTelephonyUtilDynamic.dylib](DYLIBS/libTelephonyUtilDynamic.dylib.md)
- [/usr/lib/libThaiTokenizer.dylib](DYLIBS/libThaiTokenizer.dylib.md)
- [/usr/lib/libVinylNonUpdater.dylib](DYLIBS/libVinylNonUpdater.dylib.md)
- [/usr/lib/libauthinstall.dylib](DYLIBS/libauthinstall.dylib.md)
- [/usr/lib/libbsm.0.dylib](DYLIBS/libbsm.0.dylib.md)
- [/usr/lib/libcoreroutine.dylib](DYLIBS/libcoreroutine.dylib.md)
- [/usr/lib/libicucore.A.dylib](DYLIBS/libicucore.A.dylib.md)
- [/usr/lib/libmdns.dylib](DYLIBS/libmdns.dylib.md)
- [/usr/lib/libmecabra.dylib](DYLIBS/libmecabra.dylib.md)
- [/usr/lib/libmis.dylib](DYLIBS/libmis.dylib.md)
- [/usr/lib/libncurses.5.4.dylib](DYLIBS/libncurses.5.4.dylib.md)
- [/usr/lib/libnwswifttls.dylib](DYLIBS/libnwswifttls.dylib.md)
- [/usr/lib/libsysmon.dylib](DYLIBS/libsysmon.dylib.md)
- [/usr/lib/libxml2.2.dylib](DYLIBS/libxml2.2.dylib.md)
- [/usr/lib/swift/libswiftAVFoundation.dylib](DYLIBS/libswiftAVFoundation.dylib.md)
- [/usr/lib/swift/libswiftAccelerate.dylib](DYLIBS/libswiftAccelerate.dylib.md)
- [/usr/lib/swift/libswiftCoreLocation.dylib](DYLIBS/libswiftCoreLocation.dylib.md)
- [/usr/lib/swift/libswiftSpatial.dylib](DYLIBS/libswiftSpatial.dylib.md)
- [/usr/lib/swift/libswiftSystem.dylib](DYLIBS/libswiftSystem.dylib.md)
- [/usr/lib/swift/libswiftXPC.dylib](DYLIBS/libswiftXPC.dylib.md)
- [/usr/lib/system/libdyld.dylib](DYLIBS/libdyld.dylib.md)
- [/usr/lib/system/liblaunch.dylib](DYLIBS/liblaunch.dylib.md)
- [/usr/lib/system/libsystem_kernel.dylib](DYLIBS/libsystem_kernel.dylib.md)
- [/usr/lib/system/libsystem_notify.dylib](DYLIBS/libsystem_notify.dylib.md)
- [/usr/lib/updaters/libVinylUpdater.dylib](DYLIBS/libVinylUpdater.dylib.md)

</details>

### Feature Flags

#### ❌ Removed (1)

- `Domain/DeviceSharing.plist`

#### ⬆️ Updated (12)

<details>
  <summary><i>View Updated</i></summary>

#### Contacts.plist

>  `Domain/Contacts.plist`

```diff

 		<key>Enabled</key>
 		<true/>
 	</dict>
+	<key>second_stage_autoreprompt</key>
+	<dict>
+		<key>Enabled</key>
+		<true/>
+	</dict>
 	<key>snap_allow_multiple_phone_numbers</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### DocumentManager.plist

>  `Domain/DocumentManager.plist`

```diff

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
-	<key>SemanticSearch</key>
-	<dict>
-		<key>DevelopmentPhase</key>
-		<string>FeatureComplete</string>
-	</dict>
 	<key>ShowTips</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### MachineReadableCode.plist

>  `Domain/MachineReadableCode.plist`

```diff

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
+	<key>ANMDPreprocessingUsingVideoToolbox_visionOS</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>IIE</key>
 	<dict>
 		<key>DevelopmentPhase</key>

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
+	<key>PyramidGenerationOnDemandWithoutCropping_visionOS</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>PyramidGenerationUsingMSR</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### SpringBoard.plist

>  `Domain/SpringBoard.plist`

```diff

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
+	<key>ButtonInteractionNonJindo</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>CSC</key>
 	<dict>
 		<key>DevelopmentPhase</key>

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
+	<key>OnenessHomeScreenEditing</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>PAUOcclusion</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### TelephonyUtilities.plist

>  `Domain/TelephonyUtilities.plist`

```diff

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
-	<key>CallRecording</key>
-	<dict>
-		<key>DevelopmentPhase</key>
-		<string>FeatureComplete</string>
-		<key>DisclosureRequired</key>
-		<string>1b3196a9-6a20-4559-60fd-bb3743219ab3</string>
-	</dict>
 	<key>CallScreeningEnabled</key>
 	<dict>
 		<key>DevelopmentPhase</key>

 		<key>Enabled</key>
 		<true/>
 	</dict>
-	<key>recentsCallTapTargets</key>
-	<dict>
-		<key>DevelopmentPhase</key>
-		<string>FeatureComplete</string>
-	</dict>
 	<key>remoteControlClientSideCursor</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### AppleAccount.plist

>  `Domain/AppleAccount.plist`

```diff

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
-	<key>iCloudConfigurationBagDaemonCache</key>
-	<dict>
-		<key>DevelopmentPhase</key>
-		<string>FeatureComplete</string>
-	</dict>
 </dict>
 </plist>
 

```

#### MediaControls.plist

>  `Domain/MediaControls.plist`

```diff

 		<key>Enabled</key>
 		<true/>
 	</dict>
+	<key>RouteExpandAllLayouts</key>
+	<dict>
+		<key>Enabled</key>
+		<true/>
+	</dict>
 	<key>RoutePickerNotCollapseGroupsAutomatically</key>
 	<dict>
 		<key>Enabled</key>

```

#### Music.plist

>  `Domain/Music.plist`

```diff

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
+	<key>in_with_the_new</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>mantis</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### Podcasts.plist

>  `Domain/Podcasts.plist`

```diff

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
+	<key>BatchFeedFetchOnPushWatch</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>BlueMoonHomepod</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### Safari.plist

>  `Domain/Safari.plist`

```diff

 	<dict>
 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
-		<key>DisclosureRequired</key>
-		<string>03d84bad-ad3c-e422-c11e-4033a5bfdd94</string>
 	</dict>
 </dict>
 </plist>

```

#### ScreenTime.plist

>  `Domain/ScreenTime.plist`

```diff

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
+	<key>data_validation</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>feature_decoupling</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### Cascade.plist

>  `Domain/Cascade.plist`

```diff

 <?xml version="1.0" encoding="UTF-8"?>
 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
-<dict/>
+<dict>
+	<key>enableSetDeletion</key>
+	<dict>
+		<key>Enabled</key>
+		<true/>
+	</dict>
+</dict>
 </plist>
 

```


</details>

## EOF
