# 18.5 (22F5068a) .vs 18.5 (22F75)

## IPSWs

- `iPhone17,1_18.5_22F5068a_Restore.ipsw`
- `iPhone17,1_18.5_22F75_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 18.5 *(22F5068a)* | 24.5.0 | 11417.122.4~2 | Tue, 22Apr2025 21:26:13 PDT |
| 18.5 *(22F75)* | 24.5.0 | 11417.122.4~1 | Tue, 22Apr2025 20:38:09 PDT |

### Kexts

#### ❌ Removed (1)

- `com.apple.kec.AppleEncryptedArchive`

#### ⬆️ Updated (12)

<details>
  <summary><i>View Updated</i></summary>

>  `com.apple.driver.AppleAOPAudio`

```diff

   __TEXT.__cstring: 0xc591
   __TEXT.__const: 0x136
   __TEXT.__os_log: 0xf
-  __TEXT_EXEC.__text: 0x31a10
+  __TEXT_EXEC.__text: 0x31a24
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2f0
   __DATA.__common: 0x660
   __DATA.__bss: 0x49
-  __DATA_CONST.__auth_got: 0x318
+  __DATA_CONST.__auth_got: 0x328
   __DATA_CONST.__got: 0xe8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0xe8
CStrings:
+ "18:26:57"
+ "18:27:20"
+ "Apr 27 2025"
- "22:33:02"
- "22:33:14"
- "Apr 23 2025"

```

>  `com.apple.driver.AppleAVD`

```diff

 863.1.0.0.0
-  __TEXT.__os_log: 0x15e72
-  __TEXT.__cstring: 0x59b2
-  __TEXT.__const: 0xcebf8
-  __TEXT_EXEC.__text: 0x5a474
+  __TEXT.__os_log: 0x16b7a
+  __TEXT.__cstring: 0x5a23
+  __TEXT.__const: 0xe1678
+  __TEXT_EXEC.__text: 0x5e314
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x12dc
   __DATA.__common: 0x78

   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0x4098
-  __DATA_CONST.__kalloc_type: 0x30c0
-  __DATA_CONST.__kalloc_var: 0xfa0
-  Functions: 1904
+  __DATA_CONST.__const: 0x4388
+  __DATA_CONST.__kalloc_type: 0x32c0
+  __DATA_CONST.__kalloc_var: 0xff0
+  Functions: 1987
   Symbols:   0
-  CStrings:  1568
+  CStrings:  1574
 
CStrings:
+ "CAvdApCommThyme"
+ "CAvdMcpuThyme"
+ "CAvdWrapCtrlThyme"
+ "site.CAvdApCommThyme"
+ "site.CAvdMcpuThyme"
+ "site.CPriorityQueueThyme"

```

>  `com.apple.driver.AppleBasebandPCI`

```diff

 853.0.0.0.0
-  __TEXT.__cstring: 0xc1e4
-  __TEXT.__const: 0x2449
-  __TEXT_EXEC.__text: 0x7764c
+  __TEXT.__cstring: 0x37b3
+  __TEXT.__const: 0x23e9
+  __TEXT_EXEC.__text: 0x34714
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x3f8
-  __DATA.__common: 0x648
-  __DATA.__bss: 0x80
-  __DATA_CONST.__auth_got: 0x620
-  __DATA_CONST.__got: 0x180
-  __DATA_CONST.__mod_init_func: 0x788
-  __DATA_CONST.__mod_term_func: 0xe8
-  __DATA_CONST.__const: 0x86b8
-  __DATA_CONST.__kalloc_type: 0x1d80
-  __DATA_CONST.__kalloc_var: 0x690
-  Functions: 2014
+  __DATA.__data: 0x33c
+  __DATA.__common: 0x5a0
+  __DATA.__bss: 0x78
+  __DATA_CONST.__auth_got: 0x560
+  __DATA_CONST.__got: 0x178
+  __DATA_CONST.__mod_init_func: 0x768
+  __DATA_CONST.__mod_term_func: 0xc8
+  __DATA_CONST.__const: 0x7bb0
+  __DATA_CONST.__kalloc_type: 0x1980
+  __DATA_CONST.__kalloc_var: 0x550
+  Functions: 1853
   Symbols:   0
-  CStrings:  1364
+  CStrings:  441
 
CStrings:
+ "121111121222121211111111121111211111111111112112112112111121121111121"
+ "1211111212221212111111111211112111111111111121121121121111211211111212"
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
- "1211111212221212111111111211112111111111111112112112112111121121111121"
- "12111112122212121111111112111121111111111111121121121121111211211111212"
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

 853.0.0.0.0
   __TEXT.__const: 0x1526
-  __TEXT.__cstring: 0x67bb
-  __TEXT_EXEC.__text: 0x47ac4
+  __TEXT.__cstring: 0x1192
+  __TEXT_EXEC.__text: 0x1cd1c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
-  __DATA.__common: 0x100
-  __DATA_CONST.__auth_got: 0x288
-  __DATA_CONST.__got: 0xb8
-  __DATA_CONST.__mod_init_func: 0x510
-  __DATA_CONST.__mod_term_func: 0x30
-  __DATA_CONST.__const: 0x3180
-  __DATA_CONST.__kalloc_type: 0xc80
+  __DATA.__common: 0xd8
+  __DATA_CONST.__auth_got: 0x248
+  __DATA_CONST.__got: 0xa8
+  __DATA_CONST.__mod_init_func: 0x508
+  __DATA_CONST.__mod_term_func: 0x28
+  __DATA_CONST.__const: 0x2ff8
+  __DATA_CONST.__kalloc_type: 0xc40
   __DATA_CONST.__kalloc_var: 0x5a0
-  Functions: 872
+  Functions: 851
   Symbols:   0
-  CStrings:  717
+  CStrings:  174
 
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

>  `com.apple.driver.AppleBasebandPCIMAVPDP`

```diff

 853.0.0.0.0
   __TEXT.__const: 0x30
-  __TEXT.__cstring: 0x4b98
-  __TEXT_EXEC.__text: 0x254dc
+  __TEXT.__cstring: 0xce8
+  __TEXT_EXEC.__text: 0xbacc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x128
-  __DATA_CONST.__auth_got: 0x2c8
-  __DATA_CONST.__got: 0x78
+  __DATA_CONST.__auth_got: 0x2a8
+  __DATA_CONST.__got: 0x68
   __DATA_CONST.__mod_init_func: 0x38
   __DATA_CONST.__mod_term_func: 0x38
-  __DATA_CONST.__const: 0x3408
+  __DATA_CONST.__const: 0x3400
   __DATA_CONST.__kalloc_type: 0x400
-  Functions: 379
+  Functions: 370
   Symbols:   0
-  CStrings:  360
+  CStrings:  51
 
CStrings:
+ "1211111212221212111111111211112111111111111121121121121111211211111212222"
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
- "12111112122212121111111112111121111111111111121121121121111211211111212222"
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

>  `com.apple.driver.AppleOLYHAL`

```diff

 450.20.0.0.0
   __TEXT.__const: 0x7b8
   __TEXT.__cstring: 0x45f5
-  __TEXT_EXEC.__text: 0x1d4f4
+  __TEXT_EXEC.__text: 0x1d504
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x18c
   __DATA.__common: 0x170

```

>  `com.apple.driver.IOPAudioVoiceTriggerDevice`

```diff

 440.4.0.0.0
   __TEXT.__const: 0x78
-  __TEXT.__cstring: 0x2c32
+  __TEXT.__cstring: 0x2c29
   __TEXT.__os_log: 0x16f1
   __TEXT_EXEC.__text: 0xafb0
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__kalloc_type: 0xc0
   Functions: 258
   Symbols:   0
-  CStrings:  233
+  CStrings:  232
 
CStrings:
+ "18:27:20"
+ "Apr 27 2025"
- "22:33:30"
- "22:33:31"
- "Apr 23 2025"

```

>  `com.apple.driver.corecapture`

```diff

   __TEXT.__os_log: 0x40cf
   __TEXT.__const: 0x130
   __TEXT.__cstring: 0x1ef9
-  __TEXT_EXEC.__text: 0x2792c
+  __TEXT_EXEC.__text: 0x27938
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x2e0

```

>  `com.apple.filesystems.apfs`

```diff

   __TEXT.__cstring: 0x49f8a
   __TEXT_EXEC.__text: 0x140340
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x6a0
+  __DATA.__data: 0x698
   __DATA.__bss: 0xca8
   __DATA_CONST.__auth_got: 0x1120
   __DATA_CONST.__got: 0x1b0
CStrings:
+ "20:17:30"
- "21:09:18"

```

>  `com.apple.iokit.AppleARMIISAudio`

```diff

   __TEXT.__os_log: 0x2862
   __TEXT.__cstring: 0x2e47
   __TEXT.__const: 0xc8
-  __TEXT_EXEC.__text: 0x157e4
+  __TEXT_EXEC.__text: 0x15800
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x188
   __DATA.__common: 0x60
-  __DATA_CONST.__auth_got: 0x2a0
+  __DATA_CONST.__auth_got: 0x2b0
   __DATA_CONST.__got: 0x90
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x10

   __DATA_CONST.__const: 0x1150
   __DATA_CONST.__kalloc_type: 0x240
   __DATA_CONST.__kalloc_var: 0x1e0
-  Functions: 300
+  Functions: 301
   Symbols:   0
   CStrings:  389
 

```

>  `com.apple.kernel`

```diff

 11417.122.4.0.0
-  __TEXT.__const: 0x34540
+  __TEXT.__const: 0x344b0
   __TEXT.__copyio_vectors: 0xf0
-  __TEXT.__cstring: 0x7685a
+  __TEXT.__cstring: 0x7332b
   __TEXT.__os_log: 0x2a68a
   __TEXT.__eh_frame: 0x610
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x2d8
-  __DATA_CONST.__const: 0xabce8
+  __DATA_CONST.__const: 0xabae8
   __DATA_CONST.__hib_const: 0x120
-  __DATA_CONST.__kalloc_type: 0x13980
+  __DATA_CONST.__kalloc_type: 0x136c0
   __DATA_CONST.__kalloc_var: 0x7ee0
   __DATA_CONST.__assert: 0xf0
   __DATA_CONST.__exclaves_bt: 0x60
-  __DATA_CONST.__brk_desc: 0x78
+  __DATA_CONST.__brk_desc: 0x60
   __DATA_SPTM.__const: 0x3c000
   __TEXT_EXEC.__hib_text: 0xcc8
-  __TEXT_EXEC.__text: 0x828c68
+  __TEXT_EXEC.__text: 0x815510
   __TEXT_BOOT_EXEC.__bootcode: 0x514c
   __KLD.__text: 0x1638
   __LASTDATA_CONST.__mod_init_func: 0x8

   __KLDDATA.__mod_init_func: 0x8
   __KLDDATA.__mod_term_func: 0x8
   __KLDDATA.__bss: 0x1
-  __DATA.__data: 0x185c1
-  __DATA.__lock_grp: 0x5a68
+  __DATA.__data: 0x17d81
+  __DATA.__lock_grp: 0x59b8
   __DATA.__percpu: 0x6e90
-  __DATA.__common: 0x5bd30
+  __DATA.__common: 0x5ba50
   __DATA.__bss: 0x96258
   __BOOTDATA.__data: 0x18000
-  __BOOTDATA.__init_entry_set: 0x111f0
+  __BOOTDATA.__init_entry_set: 0x110e8
   __BOOTDATA.__init: 0x5b178
   __BOOTDATA.__static_ifinit: 0x8
   __BOOTDATA.__static_if: 0x0

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x4667d
-  Functions: 20183
+  Functions: 19975
   Symbols:   0
-  CStrings:  17889
+  CStrings:  17604
 
CStrings:
- "\n(kern_coredump_routine) : kern_dump_record_file failed with %d\n"
- "\nBeginning coredump of %s\n"
- "\nBeginning dump of panic region of size 0x%zx\n"
- "\nCore dump took %llu cycles\n"
- " Compressed file length is %llu bytes\n"
- "%"
- "%.12s-cp"
- "%lld..\n"
- "%lu"
- "%qx:%x"
- "%s (during forwarding) returned 0x%x\n"
- "%s (passing along request) returned 0x%x\n"
- "%s kvtophys() for address %p returned NULL\n"
- "%s next stage output failed\n"
- "%s%c%s%c%s%c"
- "%s(%p, %llu, %p) : called with invalid length %llu\n"
- "%s(%p, %llu, %p) : called with too much data, %llu written, %llu left\n"
- "%s() : failed to write data (%llu bytes remaining) :%d\n"
- "%s() : failed to write legacy bin spec version : coredump_save_note_data() returned 0x%x\n"
- "%s() : failed to write mach header : kdp_core_output(%p, %lu, %p) returned error 0x%x\n"
- "%s() : failed to write main bin spec structure : coredump_save_note_data() returned 0x%x\n"
- "%s() : failed to write note %llu of %llu : kdp_core_output() returned  error 0x%x\n"
- "%s() : failed to write sw_vers string : coredump_save_note_data() returned 0x%x\n"
- "%s() : failed to write thread data : kdp_core_output() returned 0x%x\n"
- "%s() : failed to write zero fill padding : kdp_core_output(%p, %llu, NULL) returned 0x%x\n"
- "%s() : found %d expected LC_THREAD (%d)\n"
- "%s() : ran out of space to save threads with %llu of %llu remaining\n"
- "%s() called too many times, %llu note descriptions already recorded\n"
- "%s() called with invalid data_owner\n"
- "%s(): encountered unknown debug header entry %d, including anyway with name '%s'\n"
- "%s(): failed to write load binary spec structure for binary #%d ('%s'): callback returned 0x%x\n"
- "%s(0x%llx, 0x%llx, %p) : called with invalid addresses : start 0x%llx >= end 0x%llx\n"
- "%s(0x%llx, 0x%llx, %p) : called with invalid addresses for 32-bit : start 0x%llx, end 0x%llx\n"
- "%s(0x%llx, 0x%llx, %p) : coredump_save_segment_descriptions() called too many times, %llu segment descriptions already recorded\n"
- "%s(0x%llx, 0x%llx, %p) : failed to write segment %llu of %llu : kdp_core_output(%p, %lu, %p) returned  error 0x%x\n"
- "%s(0x%llx, 0x%llx, %p) : failed to write segment %llu of %llu. kdp_core_output(%p, %lu, %p) returned error %d\n"
- "%s(0x%llx, 0x%llx, %p) : ran out of space to save commands with %llu of %llu remaining\n"
- "%s-%s-%u.%u.%u.%u-%x%s"
- "%s/%s"
- "%s: cannot exclude region starting at %p with size %zu (not page aligned) @%s:%d"
- "%s: cannot exclude region starting at %p with size %zu (zero or overflowing size) @%s:%d"
- "%s: context allocation failure\n"
- "%s: no task is set\n"
- "%s: skipping inactive task\n"
- "%s: skipping kernel because excluded regions list is locked\n"
- "%s: skipping locked task\n"
- "%s: skipping task with locked vm map\n"
- "%s: vm map traversal failed: %d\n"
- "(%s) : coredump_init failed with %d\n"
- "(%s) : coredump_save_note_description returned %d while writing binary info LC_NOTE description"
- "(%s) : get_summary failed with %d\n"
- "(%s) : header size not populated after coredump_get_summary\n"
- "(%s) : kcc_coredump_save_note_data failed with 0x%x\n"
- "(%s) : kcc_coredump_save_note_data returned without all note data written, %llu of %llu remaining\n"
- "(%s) : kcc_coredump_save_note_descriptions failed with %d\n"
- "(%s) : kcc_coredump_save_sw_vers failed with 0x%x\n"
- "(%s) : kcc_coredump_save_sw_vers_detail_cb failed with 0x%x\n"
- "(%s) : save_note_descriptions returned without all note descriptions written, %llu of %llu remaining\n"
- "(%s) : save_note_note_summary failed with %d\n"
- "(%s) : save_segment_descriptions failed with %d\n"
- "(%s) : save_segment_descriptions returned without all segment descriptions written, %llu of %llu remaining\n"
- "(%s) : save_thread_state failed with %d\n"
- "(%s) : save_thread_state returned without all thread descriptions written, %llu of %llu remaining\n"
- "(aea_read_callback) next stage read proc returned 0x%x\n"
- "(aea_stage_outproc) aea_close() returned %d\n"
- "(aea_stage_outproc) aea_open() returned %d\n"
- "(aea_stage_outproc) aea_write() returned %zd\n"
- "(aea_stage_reset) aea_close() returned %d\n"
- "(aea_write_callback) next stage outproc returned 0x%x\n"
- "(disk_stage_read) IOPolledFileRead(%llu) returned 0x%x\n"
- "(disk_stage_read) IOPolledFileSeek(0x%llx) returned 0x%x\n"
- "(disk_stage_read) IOPolledFileWrite (during seek) returned 0x%x\n"
- "(disk_stage_read) Kickstarting IOPolledFileRead(0) returned 0x%x\n"
- "(disk_stage_write) IOPolledFileSeek(0x%llx) returned 0x%x\n"
- "(disk_stage_write) IOPolledFileWrite (during final flush) returned 0x%x\n"
- "(disk_stage_write) IOPolledFileWrite(gIOPolledCoreFileVars, %p, 0x%llx, NULL) returned 0x%x\n"
- "(disk_stage_write) disk_stage_read (during final chunk seek) returned 0x%x\n"
- "(disk_stage_write) disk_stage_read (during seek) returned 0x%x\n"
- "(do_kern_dump close) outproc(KDP_EOF, NULL, 0, 0) returned 0x%x\n"
- "(do_kern_dump coredump log) outproc(KDP_DATA, NULL, %lu, %p) returned 0x%x\n"
- "(do_kern_dump paniclog) outproc(KDP_DATA, NULL, %lu, %p) returned 0x%x\n"
- "(do_kern_dump seek begin) outproc(KDP_SEEK, NULL, %lu, %p) foffset = 0x%llx returned 0x%x\n"
- "(do_kern_dump seek logfile) outproc(KDP_SEEK, NULL, %lu, %p) foffset = 0x%llx returned 0x%x\n"
- "(do_kern_dump write public key) returned 0x%x\n"
- "(kdp_core_output) outproc(KDP_DATA, NULL, 0x%llx, %p) returned 0x%x\n"
- "(kdp_reset_output_vars) Encryption requested, is unavailable, and enforcement is active. Skipping current core.\n"
- "(kern_coredump_routine) : failed to flush final core data : kdp_core_output(%p, 0, NULL) returned 0x%x\n"
- "(kern_coredump_routine) : failed to write zero fill padding (%llu bytes remaining) : kdp_core_output(%p, %llu, NULL) returned 0x%x\n"
- "(kern_coredump_routine) : save_segment_data returned without all segment data written, %llu of %llu remaining\n"
- "(kern_dump_seek_to_next_file) outproc(KDP_SEEK, NULL, %lu, %p) foffset = 0x%llx returned 0x%x\n"
- "(kern_dump_update_header) outproc data flush returned 0x%x\n"
- "(kern_dump_update_header) outproc explicit flush returned 0x%x\n"
- "(kern_dump_update_header) outproc(KDP_DATA, NULL, %lu, %p) returned 0x%x\n"
- "(kern_dump_update_header) outproc(KDP_SEEK, NULL, %lu, %p) foffset = 0x%llx returned 0x%x\n"
- "(kern_dump_write_public_key) outproc data flush returned 0x%x\n"
- "(kern_dump_write_public_key) outproc explicit flush returned 0x%x\n"
- "(kern_dump_write_public_key) outproc(KDP_DATA, NULL, %llu, NULL) returned 0x%x\n"
- "(kern_dump_write_public_key) outproc(KDP_DATA, NULL, %u, %p) returned 0x%x\n"
- "(kern_dump_write_public_key) outproc(KDP_SEEK, NULL, %lu, %p) foffset = 0x%llx returned 0x%x\n"
- "(zlib_zoutput) outproc(KDP_DATA, NULL, 0x%x, %p) returned 0x%x\n"
- ".gz"
- "/cores/core.%d"
- "/private/preboot/kernelcore"
- "/private/var/cores"
- "/private/var/dextcores"
- "/private/var/vm/kernelcore"
- "100.."
- "11122221222222222222222112"
- "121212112"
- "; UUID="
- "; stext="
- "A dump server was not specified in the boot-args, terminating kernel core dump.\n"
- "Attempting connection to panic server configured at IP %s, port %d\n"
- "Boot-args specify %d MB kernel corefile\n"
- "Corefile is not yet initialized. Cannot write a coredump to disk\n"
- "Couldn't retrieve volume status. Error %d\n"
- "Detected remote error, terminating...\n"
- "Detected stale/invalid seq num. Expected: %d, received %d\n"
- "Done\nCoredump complete of %s, dumped %llu segments (%llu bytes), %llu threads (%llu bytes) overall uncompressed file length %llu bytes."
- "EOF Flush: Detected stale/invalid seq num. Expected: %d, received %d\n"
- "Error: No transport device registered for kernel crashdump\n"
- "Failed to %s the corefile. Error %d\n"
- "Failed to dump coprocessor cores\n"
- "Failed to dump userspace process cores\n"
- "Failed to flush panic region data : kdp_core_output(%p, 0, NULL) returned 0x%x\n"
- "Failed to open corefile of size %llu MB (low disk space)\n"
- "Failed to open corefile of size %llu MB (returned error 0x%x)\n"
- "Failed to open the corefile. Error %d\n"
- "Failed to record panic region in corefile header, kern_dump_record_file returned 0x%x\n"
- "Failed to seek to beginning of next core\n"
- "Failed to seek to panic region file offset 0x%llx, kern_dump_seek_to_next_file returned 0x%x\n"
- "Failed to write panic region to file, kdp_coreoutput(outstate, %zu, %p) returned 0x%x\n"
- "IOPolledFileFlush() returned 0x%x\n"
- "IOPolledFileFlush(0x%p) : IOStartPolledIO(0x%p, kIOPolledFlush, 0, 0, 0) returned 0x%x\n"
- "IOPolledFilePollersClose (during EOF) returned 0x%x\n"
- "IOPolledFilePollersOpen returned 0x%x\n"
- "IOPolledFilePollersSetup for corefile failed with error: 0x%x\n"
- "IOPolledFilePollersSetup(%d) error 0x%x\n"
- "IOPolledFileSeek(0x%llx) returned 0x%x\n"
- "IOPolledFileSeek(gIOPolledCoreFileVars, 0) returned 0x%x\n"
- "IOPolledFileSeek: called to seek to 0x%llx greater than file size of 0x%llx\n"
- "IOPolledFileWrite (during EOF) returned 0x%x\n"
- "IOPolledFileWrite (during seek) returned 0x%x\n"
- "IOPolledFileWrite(0x%p, 0x%p, %llu, 0x%p) : IOStartPolledIO(0x%p, kIOPolledWrite, %llu, 0x%llx, %d) returned 0x%x\n"
- "IOPolledFileWrite(gIOPolledCoreFileVars, %p, 0x%llx, NULL) returned 0x%x\n"
- "IOPolledInterface::checkForWork[%d] 0x%x\n"
- "IOPolledInterface::close[%d] 0x%x\n"
- "IOPolledInterface::ioStatus 0x%x\n"
- "IOPolledInterface::open[%d] 0x%x\n"
- "IOPolledInterface::probe[%d] 0x%x\n"
- "IOPolledInterface::startIO[%d] 0x%x\n"
- "IOPolledInterfaceActive"
- "IOPolledInterfaceStack"
- "KDPCoreStageInit"
- "Kernel map size is %llu\n"
- "Kernel timed out waiting for hardware debugger to update handshake structure."
- "LZ4 stage is not yet initialized. Cannot write a coredump to disk\n"
- "No contact in %d seconds\n"
- "Opened corefile of size %llu MB\n"
- "Opened file %s, size %qd, extents %ld, maxio %qx ssd %d\n"
- "Original panic string:\n"
- "Preferred Block Size"
- "Recorded panic region in corefile at offset 0x%llx, compressed to %llu bytes\n"
- "Resolved %s's (or proxy's) link level address\n"
- "Routing through specified router IP %s (%u)\n"
- "Sending write request for %s\n"
- "Set a new encryption key for coredumps"
- "Setting coredump status as done!\n"
- "Skipping coredump\n"
- "Skipping panic region dump\n"
- "Skipping userspace coredump, coredump list is locked\n"
- "System dump aborted.\n"
- "Transmitting kernel state, please wait:\n"
- "Transmitting packets to link level address: %02x:%02x:%02x:%02x:%02x:%02x\n"
- "Transmitting panic log, please wait: "
- "Transmitting system log, please wait: "
- "Unable to create core header packet.\n"
- "Unable to retrieve range for root memory device %d\n"
- "Unknown format character %c in `%s'\n"
- "Volume is low on space. Not allocating kernel corefile.\n"
- "Waiting for hardware shared memory debugger, handshake structure is at virt: %p, phys %p\n"
- "We were in the middle of initializing LZ4 stage. Cannot write a coredump to disk\n"
- "We were in the middle of initializing encryption. Marking it as unavailable\n"
- "We were in the middle of initializing the disk stage. Cannot write a coredump to disk\n"
- "Writing local cores...\n"
- "ZERR %d\n"
- "Zlib stage is not initialized. Cannot write a coredump to shared memory\n"
- "Zlib stage is not initialized. Cannot write a coredump to the network\n"
- "_kdp_ipstr"
- "_panicd_corename"
- "_panicd_ip"
- "_router_ip"
- "addrable bits"
- "apple_encrypted_archive interface registration callback is already set @%s:%d"
- "buffer_stage_outproc (during flush) returned 0x%x\n"
- "buffer_stage_outproc (during forwarding) returned 0x%x\n"
- "com.apple.private.coredump-encryption-key"
- "com.apple.private.custom-coredump-location"
- "com.apple.private.enable-coredump-on-panic-seed-privacy-approved"
- "com.apple.private.security.file-unencrypt-access"
- "compression interface registration callback is already set @%s:%d"
- "coredump"
- "coredump_encryption"
- "coredump_encryption_key"
- "coredump_init returned KERN_NODE_DOWN, skipping this core\n"
- "coredump_save_note_data"
- "coredump_save_note_description"
- "coredump_save_segment_data"
- "coredump_save_segment_data failed with %d\n"
- "coredump_save_segment_descriptions"
- "coredump_save_summary"
- "coredump_save_sw_vers"
- "coredump_save_sw_vers_legacy"
- "coredump_save_thread_state"
- "corefile"
- "corefile path selection in device-tree is not one of the allowed values: %s, Using default %s\n"
- "corefile path selection in device-tree was set to: %s (value: %s)\n"
- "corefile_size_mb"
- "custom"
- "drivercorefile"
- "dumpinfo does not fit into KDP packet.\n"
- "error 0x%x from IOGetHibernationCryptKey\n"
- "error 0x%x opening polled file\n"
- "handshake structure not initialized\n"
- "hwm_user_cores"
- "inet_aton() failed interpreting %s as a panic server IP\n"
- "inet_aton() failed interpreting %s as an IP\n"
- "inline call to debugger(machine_startup)"
- "kdp panic: %s"
- "kdp_core.c"
- "kdp_core_exclude_region"
- "kdp_corefile"
- "kdp_crashdump_pkt_size"
- "kdp_ip_addr"
- "kdp_panic_dump: unexpected pending input packet"
- "kdp_poll"
- "kdp_raise_exception"
- "kdp_reply: no input packet"
- "kdp_send: no input packet"
- "kdp_send: packet too large (%u > %d)"
- "kdp_send_crashdump_data returned 0x%x\n"
- "kdp_send_crashdump_pkt failed with error %d\n"
- "kdp_set_dump_info: Skipping invalid panicd port %u (using %d)\n"
- "kern ver str"
- "kern_coredump_routine"
- "kern_dump_init"
- "kern_dump_save_note_data"
- "kern_open_file_for_direct_io took %qd ms\n"
- "kernel-core-dump-location"
- "load binary"
- "main bin spec"
- "memory_backing_aware_buffer_stage_outproc"
- "misaligned file pos %qx\n"
- "octet"
- "outproc(KDP_WRQ, NULL, 0, NULL) returned 0x%x\n"
- "panic context"
- "panic_region"
- "panicd_port"
- "paniclog"
- "pid %ld (%s), uid (%u): corename is too long\n"
- "pid %ld (%s), uid (%u): unexpected end of string after %% token\n"
- "polled file major %d, minor %d, blocksize %ld, pollers %d\n"
- "preboot"
- "progress_notify_stage_outproc"
- "read from"
- "save_seg_data: pmap traversal failed: %d\n"
- "save_seg_desc: pmap traversal failed: %d\n"
- "save_summary: pmap traversal failed: %d\n"
- "secure_core: Unable to seek to the start of file: %d\n"
- "site.IOPolledFileIOVars"
- "site.struct kern_userspace_coredump_context"
- "site.typeof(*data)"
- "site.typeof(*region)"
- "skipping local kernel core because core file could not be opened prior to panic (mode : 0x%x, error : 0x%x)\n"
- "skipping local kernel core because the SPTM is in INTERRUPTED state and can't support core dump generation\n"
- "skipping local kernel core because the SPTM is in PANIC state and can't support core dump generation\n"
- "sugid_coredump"
- "systemlog"
- "user_dump_init"
- "user_dump_save_seg_descriptions"
- "user_dump_save_segment_data"
- "user_dump_save_summary"
- "write to"
- "xnu"
- "xnu-"

```

>  `com.apple.security.sandbox`

```diff

 2401.122.2.0.0
   __TEXT.__os_log: 0x2092
-  __TEXT.__const: 0x1b9a99
+  __TEXT.__const: 0x1b9b19
   __TEXT.__cstring: 0x71c6
   __TEXT_EXEC.__text: 0x31510
   __TEXT_EXEC.__auth_stubs: 0x0

```

</details>

## MachO

### 🆕 NEW (2)

- `/System/Library/NanoTimeKit/FaceBundles/NTKPride2025FaceBundle.bundle/NTKPride2025FaceBundle`
- `/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceSharedConfigurationXPCService.xpc/FindMyDeviceSharedConfigurationXPCService`

### ❌ Removed (2)

- `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/AirPlayDiagnosticExtension.appex/AirPlayDiagnosticExtension`
- `/usr/libexec/memoryanalyticsd`

### ⬆️ Updated (330)

<details>
  <summary><i>View Updated</i></summary>

- [/Applications/AccessorySetupUI.app/AccessorySetupUI](MACHOS/AccessorySetupUI.md)
- [/Applications/ActivityProgressUI.app/ActivityProgressUI](MACHOS/ActivityProgressUI.md)
- [/Applications/AirDropUI.app/AirDropUI](MACHOS/AirDropUI.md)
- [/Applications/AirPlayReceiver.app/AirPlayReceiver](MACHOS/AirPlayReceiver.md)
- [/Applications/AppleIDSetupUIService.app/AppleIDSetupUIService](MACHOS/AppleIDSetupUIService.md)
- [/Applications/BusinessExtensionsWrapper.app/PlugIns/Business.appex/Business](MACHOS/Business.md)
- [/Applications/CarPlaySettings.app/CarPlaySettings](MACHOS/CarPlaySettings.md)
- [/Applications/Charge.app/Charge](MACHOS/Charge.md)
- [/Applications/Climate.app/Climate](MACHOS/Climate.md)
- [/Applications/ClockAngel.app/ClockAngel](MACHOS/ClockAngel.md)
- [/Applications/ColorPickerUIService.app/ColorPickerUIService](MACHOS/ColorPickerUIService.md)
- [/Applications/CoreAuthUI.app/CoreAuthUI](MACHOS/CoreAuthUI.md)
- [/Applications/Diagnostics.app/Diagnostics](MACHOS/Diagnostics.md)
- [/Applications/DiagnosticsReporter.app/DiagnosticsReporter](MACHOS/DiagnosticsReporter.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-7004.appex/Diagnostic-7004](MACHOS/Diagnostic-7004.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8185.appex/Diagnostic-8185](MACHOS/Diagnostic-8185.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8268.appex/Diagnostic-8268](MACHOS/Diagnostic-8268.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8340.appex/Diagnostic-8340](MACHOS/Diagnostic-8340.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8343.appex/Diagnostic-8343](MACHOS/Diagnostic-8343.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9006.appex/Diagnostic-9006](MACHOS/Diagnostic-9006.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9008.appex/Diagnostic-9008](MACHOS/Diagnostic-9008.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9010.appex/Diagnostic-9010](MACHOS/Diagnostic-9010.md)
- [/Applications/DiagnosticsService.app/PlugIns/SystemReport-AirPods.appex/SystemReport-AirPods](MACHOS/SystemReport-AirPods.md)
- [/Applications/DiagnosticsService.app/PlugIns/SystemReport-BatteryCase.appex/SystemReport-BatteryCase](MACHOS/SystemReport-BatteryCase.md)
- [/Applications/DiagnosticsService.app/PlugIns/SystemReport.appex/SystemReport](MACHOS/SystemReport.md)
- [/Applications/FMDMagSafeSetupRemoteUI.app/FMDMagSafeSetupRemoteUI](MACHOS/FMDMagSafeSetupRemoteUI.md)
- [/Applications/FTMInternal-4.app/FTMInternal-4](MACHOS/FTMInternal-4.md)
- [/Applications/Family.app/PlugIns/InviteMessageBubbleExtension.appex/InviteMessageBubbleExtension](MACHOS/InviteMessageBubbleExtension.md)
- [/Applications/Feedback Assistant iOS.app/Feedback Assistant iOS](MACHOS/Feedback_Assistant_iOS.md)
- [/Applications/FinanceUIService.app/FinanceUIService](MACHOS/FinanceUIService.md)
- [/Applications/FindMyExtensionContainer.app/PlugIns/FMDMagSafeExtension.appex/FMDMagSafeExtension](MACHOS/FMDMagSafeExtension.md)
- [/Applications/FindMyExtensionContainer.app/PlugIns/FindMyDeviceBluetoothExtension.appex/FindMyDeviceBluetoothExtension](MACHOS/FindMyDeviceBluetoothExtension.md)
- [/Applications/FontPickerUIService.app/FontPickerUIService](MACHOS/FontPickerUIService.md)
- [/Applications/GameCenterWidgets.app/PlugIns/GCWidgets.appex/GCWidgets](MACHOS/GCWidgets.md)
- [/Applications/HDSViewService.app/HDSViewService](MACHOS/HDSViewService.md)
- [/Applications/HeadphoneProxService.app/HeadphoneProxService](MACHOS/HeadphoneProxService.md)
- [/Applications/HealthENLauncher.app/HealthENLauncher](MACHOS/HealthENLauncher.md)
- [/Applications/HomeCaptiveViewService.app/HomeCaptiveViewService](MACHOS/HomeCaptiveViewService.md)
- [/Applications/InCallService.app/InCallService](MACHOS/InCallService.md)
- [/Applications/MTLReplayer.app/Frameworks/MTLReplayController.framework/MTLReplayController](MACHOS/MTLReplayController.md)
- [/Applications/Media.app/Media](MACHOS/Media.md)
- [/Applications/MediaRemoteUI.app/MediaRemoteUI](MACHOS/MediaRemoteUI.md)
- [/Applications/MobilePhone.app/PlugIns/VoicemailMessageNotificationExtension.appex/VoicemailMessageNotificationExtension](MACHOS/VoicemailMessageNotificationExtension.md)
- [/Applications/MomentsUIService.app/MomentsUIService](MACHOS/MomentsUIService.md)
- [/Applications/MusicRecognition.app/MusicRecognition](MACHOS/MusicRecognition.md)
- [/Applications/PCViewService.app/PCViewService](MACHOS/PCViewService.md)
- [/Applications/Preferences.app/Preferences](MACHOS/Preferences.md)
- [/Applications/PreviewShell.app/PreviewShell](MACHOS/PreviewShell.md)
- [/Applications/SMS Filter.app/PlugIns/extensionFilter.appex/extensionFilter](MACHOS/extensionFilter.md)
- [/Applications/SOSBuddy.app/SOSBuddy](MACHOS/SOSBuddy.md)
- [/Applications/Screen Time.app/PlugIns/ScreenTimeWidgetExtension.appex/ScreenTimeWidgetExtension](MACHOS/ScreenTimeWidgetExtension.md)
- [/Applications/Screen Time.app/PlugIns/ScreenTimeWidgetIntentsExtension.appex/ScreenTimeWidgetIntentsExtension](MACHOS/ScreenTimeWidgetIntentsExtension.md)
- [/Applications/ScreenContinuityShell.app/ScreenContinuityShell](MACHOS/ScreenContinuityShell.md)
- [/Applications/Setup.app/Setup](MACHOS/Setup.md)
- [/Applications/SharingUIService.app/SharingUIService](MACHOS/SharingUIService.md)
- [/Applications/SharingViewService.app/SharingViewService](MACHOS/SharingViewService.md)
- [/Applications/ShazamEventsApp.app/ShazamEventsApp](MACHOS/ShazamEventsApp.md)
- [/Applications/Sidecar.app/PlugIns/ContinuityDisplay.appex/ContinuityDisplay](MACHOS/ContinuityDisplay.md)
- [/Applications/Siri.app/Siri](MACHOS/Siri.md)
- [/Applications/TDGSharingViewService.app/TDGSharingViewService](MACHOS/TDGSharingViewService.md)
- [/Applications/TVSetupUIService.app/TVSetupUIService](MACHOS/TVSetupUIService.md)
- [/Applications/Tamale.app/Tamale](MACHOS/Tamale.md)
- [/Applications/TirePressure.app/TirePressure](MACHOS/TirePressure.md)
- [/Applications/Trip.app/Trip](MACHOS/Trip.md)
- [/Applications/Vehicle.app/Vehicle](MACHOS/Vehicle.md)
- [/Applications/WritingToolsUIService.app/WritingToolsUIService](MACHOS/WritingToolsUIService.md)
- [/System/Applications/Family/InviteMessageBubbleExtension.appex/InviteMessageBubbleExtension](MACHOS/InviteMessageBubbleExtension.md)
- [/System/Library/AccessibilityBundles/LiveSpeechUIService.axuiservice/LiveSpeechUIService](MACHOS/LiveSpeechUIService.md)
- [/System/Library/AccessibilityBundles/VoiceOver.axuiservice/VoiceOver](MACHOS/VoiceOver.md)
- [/System/Library/Accounts/ServiceOwners/AMSMediaServiceOwner.bundle/AMSMediaServiceOwner](MACHOS/AMSMediaServiceOwner.md)
- [/System/Library/AppleMediaServices/DynamicUI/PlugIns/CoreDynamicUIPlugin.bundle/CoreDynamicUIPlugin](MACHOS/CoreDynamicUIPlugin.md)
- [/System/Library/AppleMediaServices/DynamicUI/PlugIns/StoreDynamicUIPlugin.bundle/StoreDynamicUIPlugin](MACHOS/StoreDynamicUIPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/AlarmFlowPlugin.bundle/AlarmFlowPlugin](MACHOS/AlarmFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/AudioFlowDelegatePlugin](MACHOS/AudioFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/CAMRootFlowPlugin.bundle/CAMRootFlowPlugin](MACHOS/CAMRootFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/CarCommandsFlowDelegatePlugin.bundle/CarCommandsFlowDelegatePlugin](MACHOS/CarCommandsFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/DailyBriefingFlowPlugin.bundle/DailyBriefingFlowPlugin](MACHOS/DailyBriefingFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/EdutainmentFlowPlugin.bundle/EdutainmentFlowPlugin](MACHOS/EdutainmentFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/EmergencyFlowPlugin.bundle/EmergencyFlowPlugin](MACHOS/EmergencyFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/HealthFlowDelegatePlugin.bundle/HealthFlowDelegatePlugin](MACHOS/HealthFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/IFFlowPlugin](MACHOS/IFFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/PhoneCallFlowDelegatePlugin](MACHOS/PhoneCallFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/SocialConversationFlowDelegatePlugin](MACHOS/SocialConversationFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/TimerFlowDelegatePlugin.bundle/TimerFlowDelegatePlugin](MACHOS/TimerFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/WellnessFlowPlugin](MACHOS/WellnessFlowPlugin.md)
- [/System/Library/Assistant/Plugins/PreferencesAssistant.assistantBundle/PreferencesAssistant](MACHOS/PreferencesAssistant.md)
- [/System/Library/Assistant/Plugins/activity.assistantBundle/activity](MACHOS/activity.md)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriPrivateLearningTTSMispronunciationPlugin.bundle/SiriPrivateLearningTTSMispronunciationPlugin](MACHOS/SiriPrivateLearningTTSMispronunciationPlugin.md)
- [/System/Library/Assistant/UIPlugins/RemindersSiriUIPlugin.siriUIBundle/RemindersSiriUIPlugin](MACHOS/RemindersSiriUIPlugin.md)
- [/System/Library/CoreServices/AccessibilityUIServer.app/PlugIns/AccessibilityControlsExtension.appex/AccessibilityControlsExtension](MACHOS/AccessibilityControlsExtension.md)
- [/System/Library/CoreServices/BluetoothUIService.app/BluetoothUIService](MACHOS/BluetoothUIService.md)
- [/System/Library/CoreServices/ClarityBoard.app/ClarityBoard](MACHOS/ClarityBoard.md)
- [/System/Library/CoreServices/LiveTranscriptionUI.app/LiveTranscriptionUI](MACHOS/LiveTranscriptionUI.md)
- [/System/Library/DataClassMigrators/BuddyMigrator.migrator/BuddyMigrator](MACHOS/BuddyMigrator.md)
- [/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN](MACHOS/com.apple.DriverKit-AppleBCMWLAN.md)
- [/System/Library/ExtensionKit/Extensions/AccessibilityControlsExtension.appex/AccessibilityControlsExtension](MACHOS/AccessibilityControlsExtension.md)
- [/System/Library/ExtensionKit/Extensions/AppStoreEvalLighthouseWorker.appex/AppStoreEvalLighthouseWorker](MACHOS/AppStoreEvalLighthouseWorker.md)
- [/System/Library/ExtensionKit/Extensions/AssistantSettingsControlsExtension.appex/AssistantSettingsControlsExtension](MACHOS/AssistantSettingsControlsExtension.md)
- [/System/Library/ExtensionKit/Extensions/DocumentAppIntents.appex/DocumentAppIntents](MACHOS/DocumentAppIntents.md)
- [/System/Library/ExtensionKit/Extensions/FamilyIntents.appex/FamilyIntents](MACHOS/FamilyIntents.md)
- [/System/Library/ExtensionKit/Extensions/FedStatsMLHostPluginClassA.appex/FedStatsMLHostPluginClassA](MACHOS/FedStatsMLHostPluginClassA.md)
- [/System/Library/ExtensionKit/Extensions/FedStatsMLHostPluginClassB.appex/FedStatsMLHostPluginClassB](MACHOS/FedStatsMLHostPluginClassB.md)
- [/System/Library/ExtensionKit/Extensions/GenerativeAssistantExtension.appex/GenerativeAssistantExtension](MACHOS/GenerativeAssistantExtension.md)
- [/System/Library/ExtensionKit/Extensions/LighthouseAVExtension.appex/LighthouseAVExtension](MACHOS/LighthouseAVExtension.md)
- [/System/Library/ExtensionKit/Extensions/PridePosterExtension.appex/PridePosterExtension](MACHOS/PridePosterExtension.md)
- [/System/Library/ExtensionKit/Extensions/PrivateEvolutionPlugin.appex/PrivateEvolutionPlugin](MACHOS/PrivateEvolutionPlugin.md)
- [/System/Library/ExtensionKit/Extensions/ProductPageExtension.appex/ProductPageExtension](MACHOS/ProductPageExtension.md)
- [/System/Library/ExtensionKit/Extensions/ScreenTimeAppIntentsExtension.appex/ScreenTimeAppIntentsExtension](MACHOS/ScreenTimeAppIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/SubscribePageExtension.appex/SubscribePageExtension](MACHOS/SubscribePageExtension.md)
- [/System/Library/ExtensionKit/Extensions/WirelessModemSettingsControlsExtension.appex/WirelessModemSettingsControlsExtension](MACHOS/WirelessModemSettingsControlsExtension.md)
- [/System/Library/Frameworks/AutomatedDeviceEnrollment.framework/PlugIns/AddDevicesToAutomatedDeviceEnrollmentExtension.appex/AddDevicesToAutomatedDeviceEnrollmentExtension](MACHOS/AddDevicesToAutomatedDeviceEnrollmentExtension.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenterMobileHelper](MACHOS/CommCenterMobileHelper.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenterRootHelper](MACHOS/CommCenterRootHelper.md)
- [/System/Library/Frameworks/FamilyControls.framework/FamilyControlsAgent](MACHOS/FamilyControlsAgent.md)
- [/System/Library/Frameworks/FamilyControls.framework/PlugIns/ActivityPickerExtension.appex/ActivityPickerExtension](MACHOS/ActivityPickerExtension.md)
- [/System/Library/Frameworks/ManagedSettings.framework/ManagedSettingsAgent](MACHOS/ManagedSettingsAgent.md)
- [/System/Library/Frameworks/StoreKit.framework/Support/storekitd](MACHOS/storekitd.md)
- [/System/Library/Frameworks/UIKit.framework/PlugIns/com.apple.UIKit.ColorPicker.appex/com.apple.UIKit.ColorPicker](MACHOS/com.apple.UIKit.ColorPicker.md)
- [/System/Library/Messages/PlugIns/RCS.imservice/RCS](MACHOS/RCS.md)
- [/System/Library/Messages/iMessageBalloons/ASMessagesProvider.bundle/ASMessagesProvider](MACHOS/ASMessagesProvider.md)
- [/System/Library/Messages/iMessageBalloons/DigitalTouchBalloonProvider.bundle/DigitalTouchBalloonProvider](MACHOS/DigitalTouchBalloonProvider.md)
- [/System/Library/NanoPreferenceBundles/General/CSLCompanionLiveActivitiesSettings.bundle/CSLCompanionLiveActivitiesSettings](MACHOS/CSLCompanionLiveActivitiesSettings.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/ActivityBridgeSetup.bundle/ActivityBridgeSetup](MACHOS/ActivityBridgeSetup.md)
- [/System/Library/PreferenceBundles/AccountSettings/CloudKitSettings.bundle/CloudKitSettings](MACHOS/CloudKitSettings.md)
- [/System/Library/PreferenceBundles/AccountSettings/icloudMailSettings.bundle/icloudMailSettings](MACHOS/icloudMailSettings.md)
- [/System/Library/PreferenceBundles/AdAttributionKitDeveloperSettings.bundle/AdAttributionKitDeveloperSettings](MACHOS/AdAttributionKitDeveloperSettings.md)
- [/System/Library/PreferenceBundles/AppClipDeveloperSettings.bundle/AppClipDeveloperSettings](MACHOS/AppClipDeveloperSettings.md)
- [/System/Library/PreferenceBundles/CarKitSettings.bundle/CarKitSettings](MACHOS/CarKitSettings.md)
- [/System/Library/PreferenceBundles/GameControlleriOSSettings.bundle/GameControlleriOSSettings](MACHOS/GameControlleriOSSettings.md)
- [/System/Library/PreferenceBundles/JournalSettings.bundle/JournalSettings](MACHOS/JournalSettings.md)
- [/System/Library/PreferenceBundles/MobileStoreSettings.bundle/MobileStoreSettings](MACHOS/MobileStoreSettings.md)
- [/System/Library/PreferenceBundles/PodcastsSettingsPlugin.bundle/PodcastsSettingsPlugin](MACHOS/PodcastsSettingsPlugin.md)
- [/System/Library/PreferenceBundles/StorageSettingsUI.bundle/StorageSettingsUI](MACHOS/StorageSettingsUI.md)
- [/System/Library/PreferenceBundles/WallpaperSettings.bundle/WallpaperSettings](MACHOS/WallpaperSettings.md)
- [/System/Library/PrivateFrameworks/ABMHelper.framework/Support/abm-helper](MACHOS/abm-helper.md)
- [/System/Library/PrivateFrameworks/ASOctaneSupport.framework/XPCServices/ASOctaneSupportXPCService.xpc/ASOctaneSupportXPCService](MACHOS/ASOctaneSupportXPCService.md)
- [/System/Library/PrivateFrameworks/AppStoreComponents.framework/Support/appstorecomponentsd](MACHOS/appstorecomponentsd.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored](MACHOS/appstored.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/amsaccountsd](MACHOS/amsaccountsd.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/Extensions/UtilityExtension.appex/UtilityExtension](MACHOS/UtilityExtension.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/amsengagementd](MACHOS/amsengagementd.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd](MACHOS/assistantd.md)
- [/System/Library/PrivateFrameworks/AuthKit.framework/akd](MACHOS/akd.md)
- [/System/Library/PrivateFrameworks/BookDataStore.framework/Support/bookdatastored](MACHOS/bookdatastored.md)
- [/System/Library/PrivateFrameworks/CacheDelete.framework/deleted_helper](MACHOS/deleted_helper.md)
- [/System/Library/PrivateFrameworks/CloudDocsUI.framework/PlugIns/com.apple.CloudDocsUI.CloudSharing.appex/com.apple.CloudDocsUI.CloudSharing](MACHOS/com.apple.CloudDocsUI.CloudSharing.md)
- [/System/Library/PrivateFrameworks/CloudKitDaemon.framework/Support/ckdiscretionaryd](MACHOS/ckdiscretionaryd.md)
- [/System/Library/PrivateFrameworks/CloudSharing.framework/XPCServices/SPIHelper-iOS.xpc/SPIHelper-iOS](MACHOS/SPIHelper-iOS.md)
- [/System/Library/PrivateFrameworks/CloudSharingUI.framework/PlugIns/com.apple.CloudSharingUI.AddParticipants.appex/com.apple.CloudSharingUI.AddParticipants](MACHOS/com.apple.CloudSharingUI.AddParticipants.md)
- [/System/Library/PrivateFrameworks/CloudSharingUI.framework/PlugIns/com.apple.CloudSharingUI.CloudSharing.appex/com.apple.CloudSharingUI.CloudSharing](MACHOS/com.apple.CloudSharingUI.CloudSharing.md)
- [/System/Library/PrivateFrameworks/CloudTelemetry.framework/XPCServices/CloudTelemetryService.xpc/CloudTelemetryService](MACHOS/CloudTelemetryService.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/parsec-fbf](MACHOS/parsec-fbf.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/parsecd](MACHOS/parsecd.md)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd](MACHOS/corespeechd.md)
- [/System/Library/PrivateFrameworks/CoreThreadCommissionerService.framework/CoreThreadCommissionerServiced](MACHOS/CoreThreadCommissionerServiced.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/XPCServices/com.apple.dt.DTMLModelRunnerService.xpc/com.apple.dt.DTMLModelRunnerService](MACHOS/com.apple.dt.DTMLModelRunnerService.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Cellular.appex/com.apple.DiagnosticExtensions.Cellular](MACHOS/com.apple.DiagnosticExtensions.Cellular.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Telephony.appex/com.apple.DiagnosticExtensions.Telephony](MACHOS/com.apple.DiagnosticExtensions.Telephony.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAppPopover.appex/RecentsAppPopover](MACHOS/RecentsAppPopover.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAvocado.appex/RecentsAvocado](MACHOS/RecentsAvocado.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/SaveToFiles.appex/SaveToFiles](MACHOS/SaveToFiles.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/com.apple.DocumentManager.Service.appex/com.apple.DocumentManager.Service](MACHOS/com.apple.DocumentManager.Service.md)
- [/System/Library/PrivateFrameworks/EcosystemAnalytics.framework/Support/ecosystemanalyticsd](MACHOS/ecosystemanalyticsd.md)
- [/System/Library/PrivateFrameworks/FinHealth.framework/ClientTools/finhealthclient](MACHOS/finhealthclient.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceBTDiscoveryXPCService.xpc/FindMyDeviceBTDiscoveryXPCService](MACHOS/FindMyDeviceBTDiscoveryXPCService.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceEmergencyCallInfoPublisherXPCService.xpc/FindMyDeviceEmergencyCallInfoPublisherXPCService](MACHOS/FindMyDeviceEmergencyCallInfoPublisherXPCService.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceEraseXPCService.xpc/FindMyDeviceEraseXPCService](MACHOS/FindMyDeviceEraseXPCService.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceHelperXPCService.xpc/FindMyDeviceHelperXPCService](MACHOS/FindMyDeviceHelperXPCService.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceIdentityXPCService.xpc/FindMyDeviceIdentityXPCService](MACHOS/FindMyDeviceIdentityXPCService.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceUserNotificationsXPCService.xpc/FindMyDeviceUserNotificationsXPCService](MACHOS/FindMyDeviceUserNotificationsXPCService.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/Resources/UITypographyPanel.bundle/UITypographyPanel](MACHOS/UITypographyPanel.md)
- [/System/Library/PrivateFrameworks/GPUToolsCapture.framework/GPUToolsCapture](MACHOS/GPUToolsCapture.md)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/PlugIns/GameCenterMatchmakerExtension.appex/GameCenterMatchmakerExtension](MACHOS/GameCenterMatchmakerExtension.md)
- [/System/Library/PrivateFrameworks/HangTracer.framework/PlugIns/HangLogsDiagnosticExtension.appex/HangLogsDiagnosticExtension](MACHOS/HangLogsDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/HangTracer.framework/PlugIns/PerformanceLoggingDiagnosticExtension.appex/PerformanceLoggingDiagnosticExtension](MACHOS/PerformanceLoggingDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/HomePlatformSettingsUI.framework/PlugIns/HPSUIViewService.appex/HPSUIViewService](MACHOS/HPSUIViewService.md)
- [/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd](MACHOS/identityservicesd.md)
- [/System/Library/PrivateFrameworks/IDSBlastDoorSupport.framework/XPCServices/IDSBlastDoorService.xpc/IDSBlastDoorService](MACHOS/IDSBlastDoorService.md)
- [/System/Library/PrivateFrameworks/MLKit.framework/PlugIns/com.apple.MLKit.MLModelPreview.appex/com.apple.MLKit.MLModelPreview](MACHOS/com.apple.MLKit.MLModelPreview.md)
- [/System/Library/PrivateFrameworks/MediaRemote.framework/Support/mediaremoted](MACHOS/mediaremoted.md)
- [/System/Library/PrivateFrameworks/MediaServicesBroker.framework/PlugIns/MediaSetupViewService.appex/MediaSetupViewService](MACHOS/MediaSetupViewService.md)
- [/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/XPCServices/MessagesAirlockService.xpc/MessagesAirlockService](MACHOS/MessagesAirlockService.md)
- [/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/XPCServices/MessagesBlastDoorService.xpc/MessagesBlastDoorService](MACHOS/MessagesBlastDoorService.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/Support/accessoryupdaterd](MACHOS/accessoryupdaterd.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/EAUpdaterService.xpc/EAUpdaterService](MACHOS/EAUpdaterService.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceLegacyAudio.xpc/UARPUpdaterServiceLegacyAudio](MACHOS/UARPUpdaterServiceLegacyAudio.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/backupd](MACHOS/backupd.md)
- [/System/Library/PrivateFrameworks/NeighborhoodActivityConduit.framework/XPCServices/com.apple.NeighborhoodActivityConduitService.xpc/com.apple.NeighborhoodActivityConduitService](MACHOS/com.apple.NeighborhoodActivityConduitService.md)
- [/System/Library/PrivateFrameworks/OnDeviceStorage.framework/Support/amsondevicestoraged](MACHOS/amsondevicestoraged.md)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/passd](MACHOS/passd.md)
- [/System/Library/PrivateFrameworks/People.framework/peopled](MACHOS/peopled.md)
- [/System/Library/PrivateFrameworks/PersonalizedSensing.framework/XPCServices/PersonalizedSensingService.xpc/PersonalizedSensingService](MACHOS/PersonalizedSensingService.md)
- [/System/Library/PrivateFrameworks/PrivateCloudCompute.framework/privatecloudcomputed.app/privatecloudcomputed](MACHOS/privatecloudcomputed.md)
- [/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeAgent](MACHOS/ScreenTimeAgent.md)
- [/System/Library/PrivateFrameworks/Search.framework/PlugIns/SpotlightDiagnostic.appex/SpotlightDiagnostic](MACHOS/SpotlightDiagnostic.md)
- [/System/Library/PrivateFrameworks/SiriVideoIntents.framework/PlugIns/VideoIntentExtension.appex/VideoIntentExtension](MACHOS/VideoIntentExtension.md)
- [/System/Library/PrivateFrameworks/SonicKit.framework/PlugIns/SonicDiagnostics.appex/SonicDiagnostics](MACHOS/SonicDiagnostics.md)
- [/System/Library/PrivateFrameworks/SoundScapesUtility.framework/PlugIns/SoundScapesViewServices.appex/SoundScapesViewServices](MACHOS/SoundScapesViewServices.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd](MACHOS/callservicesd.md)
- [/System/Library/PrivateFrameworks/TranslationUIServices.framework/PlugIns/TranslationUIService.appex/TranslationUIService](MACHOS/TranslationUIService.md)
- [/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTrackingAgent](MACHOS/UsageTrackingAgent.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/ExtragalacticPoster.appex/ExtragalacticPoster](MACHOS/ExtragalacticPoster.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/KaleidoscopePoster.appex/KaleidoscopePoster](MACHOS/KaleidoscopePoster.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/RhizomePoster.appex/RhizomePoster](MACHOS/RhizomePoster.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/FocusConfigurationExtension.appex/FocusConfigurationExtension](MACHOS/FocusConfigurationExtension.md)
- [/System/Library/PrivateFrameworks/iTunesStore.framework/Support/itunesstored](MACHOS/itunesstored.md)
- [/System/Library/Settings/InstalledApps.settings/InstalledApps](MACHOS/InstalledApps.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/HomeAutomationSiriSuggestions.bundle/HomeAutomationSiriSuggestions](MACHOS/HomeAutomationSiriSuggestions.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriNotebookSuggestionsPlugin.bundle/SiriNotebookSuggestionsPlugin](MACHOS/SiriNotebookSuggestionsPlugin.md)
- [/private/var/staged_system_apps/AppStore.app/AppStore](MACHOS/AppStore.md)
- [/private/var/staged_system_apps/AppStore.app/PlugIns/AppStoreWidgetsExtension.appex/AppStoreWidgetsExtension](MACHOS/AppStoreWidgetsExtension.md)
- [/private/var/staged_system_apps/AppleTV.app/PlugIns/TVWidgetExtension.appex/TVWidgetExtension](MACHOS/TVWidgetExtension.md)
- [/private/var/staged_system_apps/AppleVisionProApp.app/AppleVisionProApp](MACHOS/AppleVisionProApp.md)
- [/private/var/staged_system_apps/Books.app/Books](MACHOS/Books.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookAnalytics.framework/BookAnalytics](MACHOS/BookAnalytics.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookCore.framework/BookCore](MACHOS/BookCore.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookEPUB.framework/BookEPUB](MACHOS/BookEPUB.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookStoreUI.framework/BookStoreUI](MACHOS/BookStoreUI.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BooksPersonalization.framework/BooksPersonalization](MACHOS/BooksPersonalization.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BooksUI.framework/BooksUI](MACHOS/BooksUI.md)
- [/private/var/staged_system_apps/Books.app/PlugIns/BooksWidgetExtension.appex/BooksWidgetExtension](MACHOS/BooksWidgetExtension.md)
- [/private/var/staged_system_apps/Bridge.app/Bridge](MACHOS/Bridge.md)
- [/private/var/staged_system_apps/Calculator.app/Calculator](MACHOS/Calculator.md)
- [/private/var/staged_system_apps/Files.app/Files](MACHOS/Files.md)
- [/private/var/staged_system_apps/FindMy.app/FindMy](MACHOS/FindMy.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyNotificationsContent.appex/FindMyNotificationsContent](MACHOS/FindMyNotificationsContent.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyNotificationsService.appex/FindMyNotificationsService](MACHOS/FindMyNotificationsService.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyWidgetPeople.appex/FindMyWidgetPeople](MACHOS/FindMyWidgetPeople.md)
- [/private/var/staged_system_apps/Fitness.app/Fitness](MACHOS/Fitness.md)
- [/private/var/staged_system_apps/Fitness.app/PlugIns/FitnessWidget.appex/FitnessWidget](MACHOS/FitnessWidget.md)
- [/private/var/staged_system_apps/Freeform.app/Extensions/USDRendererExtension.appex/USDRendererExtension](MACHOS/USDRendererExtension.md)
- [/private/var/staged_system_apps/Freeform.app/Freeform](MACHOS/Freeform.md)
- [/private/var/staged_system_apps/Freeform.app/PlugIns/FreeformWidgetKitExtension.appex/FreeformWidgetKitExtension](MACHOS/FreeformWidgetKitExtension.md)
- [/private/var/staged_system_apps/Health.app/Health](MACHOS/Health.md)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeEnergyWidgetsExtension.appex/HomeEnergyWidgetsExtension](MACHOS/HomeEnergyWidgetsExtension.md)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeWidget.appex/HomeWidget](MACHOS/HomeWidget.md)
- [/private/var/staged_system_apps/Journal.app/Journal](MACHOS/Journal.md)
- [/private/var/staged_system_apps/Journal.app/PlugIns/JournalShareExtension.appex/JournalShareExtension](MACHOS/JournalShareExtension.md)
- [/private/var/staged_system_apps/Journal.app/PlugIns/JournalWidgetsSecure.appex/JournalWidgetsSecure](MACHOS/JournalWidgetsSecure.md)
- [/private/var/staged_system_apps/Maps.app/Maps](MACHOS/Maps.md)
- [/private/var/staged_system_apps/Maps.app/PlugIns/GeneralMapsWidget.appex/GeneralMapsWidget](MACHOS/GeneralMapsWidget.md)
- [/private/var/staged_system_apps/Measure.app/Measure](MACHOS/Measure.md)
- [/private/var/staged_system_apps/MobileMail.app/MobileMail](MACHOS/MobileMail.md)
- [/private/var/staged_system_apps/MobileMail.app/PlugIns/MailWidgetExtension.appex/MailWidgetExtension](MACHOS/MailWidgetExtension.md)
- [/private/var/staged_system_apps/MobileNotes.app/MobileNotes](MACHOS/MobileNotes.md)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.SharingExtension.appex/com.apple.mobilenotes.SharingExtension](MACHOS/com.apple.mobilenotes.SharingExtension.md)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.WidgetExtension.appex/com.apple.mobilenotes.WidgetExtension](MACHOS/com.apple.mobilenotes.WidgetExtension.md)
- [/private/var/staged_system_apps/MobileSafari.app/PlugIns/SafariWidgetExtension.appex/SafariWidgetExtension](MACHOS/SafariWidgetExtension.md)
- [/private/var/staged_system_apps/MobileTimer.app/PlugIns/WorldClockWidget.appex/WorldClockWidget](MACHOS/WorldClockWidget.md)
- [/private/var/staged_system_apps/Music.app/Frameworks/MusicApplication.framework/MusicApplication](MACHOS/MusicApplication.md)
- [/private/var/staged_system_apps/Music.app/Music](MACHOS/Music.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/MusicMessagesApp.appex/MusicMessagesApp](MACHOS/MusicMessagesApp.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/MusicWidgets.appex/MusicWidgets](MACHOS/MusicWidgets.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsTag.appex/NewsTag](MACHOS/NewsTag.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsToday2.appex/NewsToday2](MACHOS/NewsToday2.md)
- [/private/var/staged_system_apps/Passbook.app/PlugIns/PassbookLockedWidgetsExtension.appex/PassbookLockedWidgetsExtension](MACHOS/PassbookLockedWidgetsExtension.md)
- [/private/var/staged_system_apps/Passbook.app/PlugIns/PassbookWidgetsExtension-iPhone.appex/PassbookWidgetsExtension-iPhone](MACHOS/PassbookWidgetsExtension-iPhone.md)
- [/private/var/staged_system_apps/Photos.app/PlugIns/PhotosReliveWidget.appex/PhotosReliveWidget](MACHOS/PhotosReliveWidget.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/NowPlayingUI.framework/NowPlayingUI](MACHOS/NowPlayingUI.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/PodcastsTranscripts.framework/PodcastsTranscripts](MACHOS/PodcastsTranscripts.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/ShelfKit.framework/ShelfKit](MACHOS/ShelfKit.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/ShelfKitCollectionViews.framework/ShelfKitCollectionViews](MACHOS/ShelfKitCollectionViews.md)
- [/private/var/staged_system_apps/Podcasts.app/Podcasts](MACHOS/Podcasts.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersIntentsExtension.appex/RemindersIntentsExtension](MACHOS/RemindersIntentsExtension.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersIntentsUIExtension.appex/RemindersIntentsUIExtension](MACHOS/RemindersIntentsUIExtension.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersSharingExtension.appex/RemindersSharingExtension](MACHOS/RemindersSharingExtension.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersWidgetExtension.appex/RemindersWidgetExtension](MACHOS/RemindersWidgetExtension.md)
- [/private/var/staged_system_apps/Reminders.app/Reminders](MACHOS/Reminders.md)
- [/private/var/staged_system_apps/SequoiaTranslator.app/SequoiaTranslator](MACHOS/SequoiaTranslator.md)
- [/private/var/staged_system_apps/Shortcuts.app/PlugIns/ShortcutsWidgetExtension.appex/ShortcutsWidgetExtension](MACHOS/ShortcutsWidgetExtension.md)
- [/private/var/staged_system_apps/Shortcuts.app/Shortcuts](MACHOS/Shortcuts.md)
- [/private/var/staged_system_apps/Stocks.app/PlugIns/StocksWidget.appex/StocksWidget](MACHOS/StocksWidget.md)
- [/private/var/staged_system_apps/Tips.app/Tips](MACHOS/Tips.md)
- [/private/var/staged_system_apps/VoiceMemos.app/VoiceMemos](MACHOS/VoiceMemos.md)
- [/private/var/staged_system_apps/Weather.app/PlugIns/WeatherWidget.appex/WeatherWidget](MACHOS/WeatherWidget.md)
- [/private/var/staged_system_apps/Weather.app/Weather](MACHOS/Weather.md)
- [/usr/bin/abmlite](MACHOS/abmlite.md)
- [/usr/bin/swift-inspect](MACHOS/swift-inspect.md)
- [/usr/lib/libmobileassetd.dylib](MACHOS/libmobileassetd.dylib.md)
- [/usr/libexec/DumpPanic](MACHOS/DumpPanic.md)
- [/usr/libexec/ReportMemoryException](MACHOS/ReportMemoryException.md)
- [/usr/libexec/SidecarRelay](MACHOS/SidecarRelay.md)
- [/usr/libexec/anomalydetectiond](MACHOS/anomalydetectiond.md)
- [/usr/libexec/appleaccountd](MACHOS/appleaccountd.md)
- [/usr/libexec/applekeystored](MACHOS/applekeystored.md)
- [/usr/libexec/assessmentagent](MACHOS/assessmentagent.md)
- [/usr/libexec/audioaccessoryd](MACHOS/audioaccessoryd.md)
- [/usr/libexec/audioanalyticsd](MACHOS/audioanalyticsd.md)
- [/usr/libexec/bluetoothuserd](MACHOS/bluetoothuserd.md)
- [/usr/libexec/checkpointd](MACHOS/checkpointd.md)
- [/usr/libexec/coreidvd](MACHOS/coreidvd.md)
- [/usr/libexec/corerepaird](MACHOS/corerepaird.md)
- [/usr/libexec/dockaccessoryd](MACHOS/dockaccessoryd.md)
- [/usr/libexec/driverkitd](MACHOS/driverkitd.md)
- [/usr/libexec/feedbackd](MACHOS/feedbackd.md)
- [/usr/libexec/findmydeviced](MACHOS/findmydeviced.md)
- [/usr/libexec/findmylocated](MACHOS/findmylocated.md)
- [/usr/libexec/gamed](MACHOS/gamed.md)
- [/usr/libexec/gamepolicyd](MACHOS/gamepolicyd.md)
- [/usr/libexec/hangreporter](MACHOS/hangreporter.md)
- [/usr/libexec/icloudmailagent](MACHOS/icloudmailagent.md)
- [/usr/libexec/idcredd](MACHOS/idcredd.md)
- [/usr/libexec/locationd](MACHOS/locationd.md)
- [/usr/libexec/mlhostd](MACHOS/mlhostd.md)
- [/usr/libexec/mobileassetd](MACHOS/mobileassetd.md)
- [/usr/libexec/modelmanagerd](MACHOS/modelmanagerd.md)
- [/usr/libexec/momentsd](MACHOS/momentsd.md)
- [/usr/libexec/online-auth-agent](MACHOS/online-auth-agent.md)
- [/usr/libexec/perfdiagsselfenabled](MACHOS/perfdiagsselfenabled.md)
- [/usr/libexec/photosfaced](MACHOS/photosfaced.md)
- [/usr/libexec/proactiveeventtrackerd](MACHOS/proactiveeventtrackerd.md)
- [/usr/libexec/promotedcontentd](MACHOS/promotedcontentd.md)
- [/usr/libexec/proximitycontrold](MACHOS/proximitycontrold.md)
- [/usr/libexec/remindd](MACHOS/remindd.md)
- [/usr/libexec/remotepairingdeviced](MACHOS/remotepairingdeviced.md)
- [/usr/libexec/rtcreportingd](MACHOS/rtcreportingd.md)
- [/usr/libexec/searchpartyd](MACHOS/searchpartyd.md)
- [/usr/libexec/securityuploadd](MACHOS/securityuploadd.md)
- [/usr/libexec/seserviced](MACHOS/seserviced.md)
- [/usr/libexec/signpost_reporter](MACHOS/signpost_reporter.md)
- [/usr/libexec/spindump_fileparser](MACHOS/spindump_fileparser.md)
- [/usr/libexec/sportsd](MACHOS/sportsd.md)
- [/usr/libexec/swtransparencyd](MACHOS/swtransparencyd.md)
- [/usr/libexec/tailspind](MACHOS/tailspind.md)
- [/usr/libexec/transparencyd](MACHOS/transparencyd.md)
- [/usr/libexec/wifivelocityd](MACHOS/wifivelocityd.md)
- [/usr/sbin/WirelessRadioManagerd](MACHOS/WirelessRadioManagerd.md)
- [/usr/sbin/bluetoothd](MACHOS/bluetoothd.md)
- [/usr/sbin/spindump](MACHOS/spindump.md)
- [/usr/sbin/wifid](MACHOS/wifid.md)

</details>

### 🔑 Entitlements

- [Entitlements DIFF](Entitlements.md)

## Firmware

### ⬆️ Updated (1)

<details>
  <summary><i>View Updated</i></summary>

#### AppleAVE2FW_H17.im4p

>  `AppleAVE2FW_H17.im4p`

```diff

   __TEXT.__chain_starts: 0x0
   __DATA.__const: 0x2a20
   __DATA._rtk_patchbay: 0x228
-  __DATA.__data: 0x1078
+  __DATA.__data: 0x1070
   __DATA._rtk_power: 0x368
   __DATA.__gxf_data: 0x10
   __DATA._rtk_tunables: 0x6a0

```


</details>

### iBoot

| iOS | Version |
| :-- | :------ |
| 18.5 *(22F5068a)* | iBoot-11881.122.1 |
| 18.5 *(22F75)* | iBoot-11881.122.1 |

#### 🆕 NEW (1)

<details>
  <summary><i>View NEW</i></summary>

##### `iboot`
  - `root@hn6kq.p1l.plx.sd...2025/04/22@20:26:21`
  - ` ApplePMUFirmware-503.120.3~468.release`
  - `MCE FW E001- built on Sat Apr 19 04:10:41 UTC 2025 by root`

</details>

#### ❌ Removed (1)

<details>
  <summary><i>View Removed</i></summary>

##### `iboot`
  - `root@q64km.p1l.plx.sd...2025/04/22@21:17:27`
  - ` ApplePMUFirmware-503.120.3~471.release`
  - `MCE FW E001- built on Sun Apr 20 08:41:46 UTC 2025 by root`

</details>

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 18.5 *(22F5068a)* | 621.2.5.10.6 |
| 18.5 *(22F75)* | 621.2.5.10.10 |

### Dylibs

#### ⬆️ Updated (189)

<details>
  <summary><i>View Updated</i></summary>

- [/System/Library/AccessibilityBundles/Moments.axbundle/Moments](DYLIBS/Moments.md)
- [/System/Library/Accounts/Notification/FindMyDeviceAccountNotificationPlugin.bundle/FindMyDeviceAccountNotificationPlugin](DYLIBS/FindMyDeviceAccountNotificationPlugin.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vImage.framework/vImage](DYLIBS/vImage.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libBNNS.dylib](DYLIBS/libBNNS.dylib.md)
- [/System/Library/Frameworks/AppIntents.framework/AppIntents](DYLIBS/AppIntents.md)
- [/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox](DYLIBS/AudioToolbox.md)
- [/System/Library/Frameworks/AudioToolbox.framework/libAudioDSP.dylib](DYLIBS/libAudioDSP.dylib.md)
- [/System/Library/Frameworks/AudioToolbox.framework/libEmbeddedSystemAUs.dylib](DYLIBS/libEmbeddedSystemAUs.dylib.md)
- [/System/Library/Frameworks/CloudKit.framework/CloudKit](DYLIBS/CloudKit.md)
- [/System/Library/Frameworks/CoreLocation.framework/CoreLocation](DYLIBS/CoreLocation.md)
- [/System/Library/Frameworks/CoreMedia.framework/CoreMedia](DYLIBS/CoreMedia.md)
- [/System/Library/Frameworks/CoreMediaIO.framework/CoreMediaIO](DYLIBS/CoreMediaIO.md)
- [/System/Library/Frameworks/CoreMotion.framework/CoreMotion](DYLIBS/CoreMotion.md)
- [/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony](DYLIBS/CoreTelephony.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/CTParser.framework/CTParser](DYLIBS/CTParser.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterBase.dylib](DYLIBS/libCommCenterBase.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterCommandDrivers.dylib](DYLIBS/libCommCenterCommandDrivers.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterKCommandDrivers.dylib](DYLIBS/libCommCenterKCommandDrivers.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterMCommandDrivers.dylib](DYLIBS/libCommCenterMCommandDrivers.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libSystemDetermination.dylib](DYLIBS/libSystemDetermination.dylib.md)
- [/System/Library/Frameworks/DeveloperToolsSupport.framework/DeveloperToolsSupport](DYLIBS/DeveloperToolsSupport.md)
- [/System/Library/Frameworks/FileProvider.framework/FileProvider](DYLIBS/FileProvider.md)
- [/System/Library/Frameworks/HealthKit.framework/HealthKit](DYLIBS/HealthKit.md)
- [/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit](DYLIBS/IOKit.md)
- [/System/Library/Frameworks/JavaScriptCore.framework/JavaScriptCore](DYLIBS/JavaScriptCore.md)
- [/System/Library/Frameworks/LiveCommunicationKit.framework/LiveCommunicationKit](DYLIBS/LiveCommunicationKit.md)
- [/System/Library/Frameworks/Network.framework/Network](DYLIBS/Network.md)
- [/System/Library/Frameworks/ProximityReader.framework/ProximityReader](DYLIBS/ProximityReader.md)
- [/System/Library/Frameworks/PushKit.framework/PushKit](DYLIBS/PushKit.md)
- [/System/Library/Frameworks/QuartzCore.framework/QuartzCore](DYLIBS/QuartzCore.md)
- [/System/Library/Frameworks/RoomPlan.framework/RoomPlan](DYLIBS/RoomPlan.md)
- [/System/Library/Frameworks/SceneKit.framework/SceneKit](DYLIBS/SceneKit.md)
- [/System/Library/Frameworks/WebKit.framework/WebKit](DYLIBS/WebKit.md)
- [/System/Library/Frameworks/WidgetKit.framework/WidgetKit](DYLIBS/WidgetKit.md)
- [/System/Library/PreferenceBundles/KeyboardSettings.bundle/KeyboardSettings](DYLIBS/KeyboardSettings.md)
- [/System/Library/PrivateFrameworks/ABMHelper.framework/ABMHelper](DYLIBS/ABMHelper.md)
- [/System/Library/PrivateFrameworks/ASEProcessing.framework/ASEProcessing](DYLIBS/ASEProcessing.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/AVConference](DYLIBS/AVConference.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ViceroyTrace.framework/ViceroyTrace](DYLIBS/ViceroyTrace.md)
- [/System/Library/PrivateFrameworks/Anvil.framework/Anvil](DYLIBS/Anvil.md)
- [/System/Library/PrivateFrameworks/AppC3D.framework/AppC3D](DYLIBS/AppC3D.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon](DYLIBS/AppStoreDaemon.md)
- [/System/Library/PrivateFrameworks/AppleAccountUI.framework/AppleAccountUI](DYLIBS/AppleAccountUI.md)
- [/System/Library/PrivateFrameworks/AppleBasebandServices.framework/AppleBasebandServices](DYLIBS/AppleBasebandServices.md)
- [/System/Library/PrivateFrameworks/AppleCV3D.framework/AppleCV3D](DYLIBS/AppleCV3D.md)
- [/System/Library/PrivateFrameworks/AppleCVAPhoto.framework/AppleCVAPhoto](DYLIBS/AppleCVAPhoto.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices](DYLIBS/AppleMediaServices.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/AppleMediaServicesUI](DYLIBS/AppleMediaServicesUI.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices](DYLIBS/AssistantServices.md)
- [/System/Library/PrivateFrameworks/AudioAnalyticsBase.framework/AudioAnalyticsBase](DYLIBS/AudioAnalyticsBase.md)
- [/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore](DYLIBS/AudioToolboxCore.md)
- [/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit](DYLIBS/AuthKit.md)
- [/System/Library/PrivateFrameworks/AutoBugCaptureCore.framework/AutoBugCaptureCore](DYLIBS/AutoBugCaptureCore.md)
- [/System/Library/PrivateFrameworks/AvatarKit.framework/AvatarKit](DYLIBS/AvatarKit.md)
- [/System/Library/PrivateFrameworks/BasebandTraceHelper.framework/BasebandTraceHelper](DYLIBS/BasebandTraceHelper.md)
- [/System/Library/PrivateFrameworks/CMImaging.framework/CMImaging](DYLIBS/CMImaging.md)
- [/System/Library/PrivateFrameworks/CTCarrierSpace.framework/CTCarrierSpace](DYLIBS/CTCarrierSpace.md)
- [/System/Library/PrivateFrameworks/CameraColorProcessing.framework/CameraColorProcessing](DYLIBS/CameraColorProcessing.md)
- [/System/Library/PrivateFrameworks/CarPlaySupport.framework/CarPlaySupport](DYLIBS/CarPlaySupport.md)
- [/System/Library/PrivateFrameworks/CellularPlanManager.framework/CellularPlanManager](DYLIBS/CellularPlanManager.md)
- [/System/Library/PrivateFrameworks/ChatKit.framework/ChatKit](DYLIBS/ChatKit.md)
- [/System/Library/PrivateFrameworks/CiderAudioServer.framework/CiderAudioServer](DYLIBS/CiderAudioServer.md)
- [/System/Library/PrivateFrameworks/CloudAssetDaemon.framework/CloudAssetDaemon](DYLIBS/CloudAssetDaemon.md)
- [/System/Library/PrivateFrameworks/CloudDocsUI.framework/CloudDocsUI](DYLIBS/CloudDocsUI.md)
- [/System/Library/PrivateFrameworks/CloudKitDaemon.framework/CloudKitDaemon](DYLIBS/CloudKitDaemon.md)
- [/System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/CloudSubscriptionFeatures](DYLIBS/CloudSubscriptionFeatures.md)
- [/System/Library/PrivateFrameworks/CloudTelemetryTools.framework/CloudTelemetryTools](DYLIBS/CloudTelemetryTools.md)
- [/System/Library/PrivateFrameworks/CoordinationCore.framework/CoordinationCore](DYLIBS/CoordinationCore.md)
- [/System/Library/PrivateFrameworks/CoreCaptureDaemon.framework/CoreCaptureDaemon](DYLIBS/CoreCaptureDaemon.md)
- [/System/Library/PrivateFrameworks/CoreDAV.framework/CoreDAV](DYLIBS/CoreDAV.md)
- [/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/CoreEmbeddedSpeechRecognition](DYLIBS/CoreEmbeddedSpeechRecognition.md)
- [/System/Library/PrivateFrameworks/CoreIDVRGBLiveness.framework/CoreIDVRGBLiveness](DYLIBS/CoreIDVRGBLiveness.md)
- [/System/Library/PrivateFrameworks/CorePhotogrammetry.framework/CorePhotogrammetry](DYLIBS/CorePhotogrammetry.md)
- [/System/Library/PrivateFrameworks/CoreRepairUI.framework/CoreRepairUI](DYLIBS/CoreRepairUI.md)
- [/System/Library/PrivateFrameworks/CoreUARP.framework/CoreUARP](DYLIBS/CoreUARP.md)
- [/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi](DYLIBS/CoreWiFi.md)
- [/System/Library/PrivateFrameworks/DailyBriefingCommon.framework/DailyBriefingCommon](DYLIBS/DailyBriefingCommon.md)
- [/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/DeviceExpertIntents](DYLIBS/DeviceExpertIntents.md)
- [/System/Library/PrivateFrameworks/DiagnosticRequestService.framework/DiagnosticRequestService](DYLIBS/DiagnosticRequestService.md)
- [/System/Library/PrivateFrameworks/DiagnosticsReporterServices.framework/DiagnosticsReporterServices](DYLIBS/DiagnosticsReporterServices.md)
- [/System/Library/PrivateFrameworks/DialogEngine.framework/DialogEngine](DYLIBS/DialogEngine.md)
- [/System/Library/PrivateFrameworks/DisembarkUI.framework/DisembarkUI](DYLIBS/DisembarkUI.md)
- [/System/Library/PrivateFrameworks/DistributedEvaluation.framework/DistributedEvaluation](DYLIBS/DistributedEvaluation.md)
- [/System/Library/PrivateFrameworks/DoNotDisturbServer.framework/DoNotDisturbServer](DYLIBS/DoNotDisturbServer.md)
- [/System/Library/PrivateFrameworks/Feedback.framework/Feedback](DYLIBS/Feedback.md)
- [/System/Library/PrivateFrameworks/FeedbackCore.framework/FeedbackCore](DYLIBS/FeedbackCore.md)
- [/System/Library/PrivateFrameworks/FeedbackService.framework/FeedbackService](DYLIBS/FeedbackService.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/FindMyDevice](DYLIBS/FindMyDevice.md)
- [/System/Library/PrivateFrameworks/FindMyUICore.framework/FindMyUICore](DYLIBS/FindMyUICore.md)
- [/System/Library/PrivateFrameworks/Hands.framework/Hands](DYLIBS/Hands.md)
- [/System/Library/PrivateFrameworks/HangTracer.framework/HangTracer](DYLIBS/HangTracer.md)
- [/System/Library/PrivateFrameworks/HeadphoneConfigs.framework/HeadphoneConfigs](DYLIBS/HeadphoneConfigs.md)
- [/System/Library/PrivateFrameworks/HelpKit.framework/HelpKit](DYLIBS/HelpKit.md)
- [/System/Library/PrivateFrameworks/HomeDeviceSetup.framework/HomeDeviceSetup](DYLIBS/HomeDeviceSetup.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemon.framework/HomeKitDaemon](DYLIBS/HomeKitDaemon.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemonLegacy.framework/HomeKitDaemonLegacy](DYLIBS/HomeKitDaemonLegacy.md)
- [/System/Library/PrivateFrameworks/HomeUI.framework/HomeUI](DYLIBS/HomeUI.md)
- [/System/Library/PrivateFrameworks/IMCore.framework/IMCore](DYLIBS/IMCore.md)
- [/System/Library/PrivateFrameworks/IMSharedUtilities.framework/IMSharedUtilities](DYLIBS/IMSharedUtilities.md)
- [/System/Library/PrivateFrameworks/ImagePlaygroundInternal.framework/ImagePlaygroundInternal](DYLIBS/ImagePlaygroundInternal.md)
- [/System/Library/PrivateFrameworks/IntelligenceEngine.framework/IntelligenceEngine](DYLIBS/IntelligenceEngine.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/IntelligencePlatformCore](DYLIBS/IntelligencePlatformCore.md)
- [/System/Library/PrivateFrameworks/JetEngine.framework/JetEngine](DYLIBS/JetEngine.md)
- [/System/Library/PrivateFrameworks/KeyboardSettings.framework/KeyboardSettings](DYLIBS/KeyboardSettings.md)
- [/System/Library/PrivateFrameworks/KeyboardSettingsFeedback.framework/KeyboardSettingsFeedback](DYLIBS/KeyboardSettingsFeedback.md)
- [/System/Library/PrivateFrameworks/LighthouseDataProcessor.framework/LighthouseDataProcessor](DYLIBS/LighthouseDataProcessor.md)
- [/System/Library/PrivateFrameworks/MTLToolsDeviceSupport.framework/MTLToolsDeviceSupport](DYLIBS/MTLToolsDeviceSupport.md)
- [/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore](DYLIBS/MediaPlaybackCore.md)
- [/System/Library/PrivateFrameworks/MetricsFramework.framework/MetricsFramework](DYLIBS/MetricsFramework.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup](DYLIBS/MobileBackup.md)
- [/System/Library/PrivateFrameworks/Moments.framework/Moments](DYLIBS/Moments.md)
- [/System/Library/PrivateFrameworks/MomentsOnboardingAndSettings.framework/MomentsOnboardingAndSettings](DYLIBS/MomentsOnboardingAndSettings.md)
- [/System/Library/PrivateFrameworks/NetworkServiceProxy.framework/NetworkServiceProxy](DYLIBS/NetworkServiceProxy.md)
- [/System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics](DYLIBS/OSAnalytics.md)
- [/System/Library/PrivateFrameworks/OmniSearch.framework/OmniSearch](DYLIBS/OmniSearch.md)
- [/System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit](DYLIBS/OnBoardingKit.md)
- [/System/Library/PrivateFrameworks/OnDeviceStorageCore.framework/OnDeviceStorageCore](DYLIBS/OnDeviceStorageCore.md)
- [/System/Library/PrivateFrameworks/OnDeviceStorageInternal.framework/OnDeviceStorageInternal](DYLIBS/OnDeviceStorageInternal.md)
- [/System/Library/PrivateFrameworks/PaperKit.framework/PaperKit](DYLIBS/PaperKit.md)
- [/System/Library/PrivateFrameworks/PegasusConfiguration.framework/PegasusConfiguration](DYLIBS/PegasusConfiguration.md)
- [/System/Library/PrivateFrameworks/PersonalizedSensing.framework/PersonalizedSensing](DYLIBS/PersonalizedSensing.md)
- [/System/Library/PrivateFrameworks/PhotosUICore.framework/PhotosUICore](DYLIBS/PhotosUICore.md)
- [/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PhotosUIPrivate](DYLIBS/PhotosUIPrivate.md)
- [/System/Library/PrivateFrameworks/PodcastsKit.framework/PodcastsKit](DYLIBS/PodcastsKit.md)
- [/System/Library/PrivateFrameworks/Preferences.framework/Preferences](DYLIBS/Preferences.md)
- [/System/Library/PrivateFrameworks/ProactiveSummarization.framework/ProactiveSummarization](DYLIBS/ProactiveSummarization.md)
- [/System/Library/PrivateFrameworks/Recon3D.framework/Recon3D](DYLIBS/Recon3D.md)
- [/System/Library/PrivateFrameworks/SearchAssets.framework/SearchAssets](DYLIBS/SearchAssets.md)
- [/System/Library/PrivateFrameworks/SensingAlgsService.framework/SensingAlgsService](DYLIBS/SensingAlgsService.md)
- [/System/Library/PrivateFrameworks/SensingAlgsTouchButtonHost.framework/SensingAlgsTouchButtonHost](DYLIBS/SensingAlgsTouchButtonHost.md)
- [/System/Library/PrivateFrameworks/Sentry.framework/Sentry](DYLIBS/Sentry.md)
- [/System/Library/PrivateFrameworks/Settings/PrivacySettingsUI.framework/PrivacySettingsUI](DYLIBS/PrivacySettingsUI.md)
- [/System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant](DYLIBS/SetupAssistant.md)
- [/System/Library/PrivateFrameworks/SiriAnalytics.framework/SiriAnalytics](DYLIBS/SiriAnalytics.md)
- [/System/Library/PrivateFrameworks/SiriNotebook.framework/SiriNotebook](DYLIBS/SiriNotebook.md)
- [/System/Library/PrivateFrameworks/SiriTTSService.framework/SiriTTSService](DYLIBS/SiriTTSService.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateController.framework/SoftwareUpdateController](DYLIBS/SoftwareUpdateController.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices](DYLIBS/SoftwareUpdateServices.md)
- [/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon](DYLIBS/SpotlightDaemon.md)
- [/System/Library/PrivateFrameworks/SpotlightServices.framework/SpotlightServices](DYLIBS/SpotlightServices.md)
- [/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard](DYLIBS/SpringBoard.md)
- [/System/Library/PrivateFrameworks/StoreServices.framework/StoreServices](DYLIBS/StoreServices.md)
- [/System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter](DYLIBS/SymptomDiagnosticReporter.md)
- [/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomEvaluator.framework/SymptomEvaluator](DYLIBS/SymptomEvaluator.md)
- [/System/Library/PrivateFrameworks/TextInputCore.framework/TextInputCore](DYLIBS/TextInputCore.md)
- [/System/Library/PrivateFrameworks/TipsCore.framework/TipsCore](DYLIBS/TipsCore.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore](DYLIBS/UIKitCore.md)
- [/System/Library/PrivateFrameworks/UserNotificationsCore.framework/UserNotificationsCore](DYLIBS/UserNotificationsCore.md)
- [/System/Library/PrivateFrameworks/UserNotificationsKit.framework/UserNotificationsKit](DYLIBS/UserNotificationsKit.md)
- [/System/Library/PrivateFrameworks/VFX.framework/VFX](DYLIBS/VFX.md)
- [/System/Library/PrivateFrameworks/VideoProcessing.framework/VideoProcessing](DYLIBS/VideoProcessing.md)
- [/System/Library/PrivateFrameworks/VideosUI.framework/VideosUI](DYLIBS/VideosUI.md)
- [/System/Library/PrivateFrameworks/VisualGeneration.framework/VisualGeneration](DYLIBS/VisualGeneration.md)
- [/System/Library/PrivateFrameworks/WPDaemon.framework/WPDaemon](DYLIBS/WPDaemon.md)
- [/System/Library/PrivateFrameworks/WebBookmarks.framework/WebBookmarks](DYLIBS/WebBookmarks.md)
- [/System/Library/PrivateFrameworks/WebCore.framework/WebCore](DYLIBS/WebCore.md)
- [/System/Library/PrivateFrameworks/WebKitLegacy.framework/WebKitLegacy](DYLIBS/WebKitLegacy.md)
- [/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy](DYLIBS/WiFiPolicy.md)
- [/System/Library/PrivateFrameworks/XCTTargetBootstrap.framework/XCTTargetBootstrap](DYLIBS/XCTTargetBootstrap.md)
- [/System/Library/PrivateFrameworks/iCloudQuotaUI.framework/iCloudQuotaUI](DYLIBS/iCloudQuotaUI.md)
- [/System/Library/VideoCodecs/VCPHEVC.videocodec](DYLIBS/VCPHEVC.videocodec.md)
- [/System/Library/VideoDecoders/AVD.videodecoder](DYLIBS/AVD.videodecoder.md)
- [/System/Library/VideoProcessors/STF.bundle/STF](DYLIBS/STF.md)
- [/usr/lib/libATCommandStudioDynamic.dylib](DYLIBS/libATCommandStudioDynamic.dylib.md)
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
- [/usr/lib/libMemoryResourceException.dylib](DYLIBS/libMemoryResourceException.dylib.md)
- [/usr/lib/libMobileGestalt.dylib](DYLIBS/libMobileGestalt.dylib.md)
- [/usr/lib/libQMIParserDynamic.dylib](DYLIBS/libQMIParserDynamic.dylib.md)
- [/usr/lib/libTelephonyBasebandDynamic.dylib](DYLIBS/libTelephonyBasebandDynamic.dylib.md)
- [/usr/lib/libTelephonyCapabilities.dylib](DYLIBS/libTelephonyCapabilities.dylib.md)
- [/usr/lib/libTelephonyDebugDynamic.dylib](DYLIBS/libTelephonyDebugDynamic.dylib.md)
- [/usr/lib/libTelephonyUtilDynamic.dylib](DYLIBS/libTelephonyUtilDynamic.dylib.md)
- [/usr/lib/libVinylNonUpdater.dylib](DYLIBS/libVinylNonUpdater.dylib.md)
- [/usr/lib/libchannel.dylib](DYLIBS/libchannel.dylib.md)
- [/usr/lib/libmecabra.dylib](DYLIBS/libmecabra.dylib.md)
- [/usr/lib/libswiftPrespecialized.dylib](DYLIBS/libswiftPrespecialized.dylib.md)
- [/usr/lib/updaters/libVinylUpdater.dylib](DYLIBS/libVinylUpdater.dylib.md)

</details>

## Files

### 🆕 New

#### filesystem (743)

<details>
  <summary><i>View Files</i></summary>

- `/System/Library/AccessibilityBundles/Moments.axbundle/Accessibility-Jurassic.loctable`
- `/System/Library/AccessibilityBundles/Music.axbundle/Accessibility-AQ.loctable`
- `/System/Library/AccessibilityBundles/MusicApplication.axbundle/Accessibility-AQ.loctable`
- `/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/Templates/dialog/wellness.catfamily/regionNotSupportedForMeds.cat/_params.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/Templates/dialog/wellness.catfamily/regionNotSupportedForMeds.cat/de.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/Templates/dialog/wellness.catfamily/regionNotSupportedForMeds.cat/en-au.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/Templates/dialog/wellness.catfamily/regionNotSupportedForMeds.cat/en-ca.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/Templates/dialog/wellness.catfamily/regionNotSupportedForMeds.cat/en-gb.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/Templates/dialog/wellness.catfamily/regionNotSupportedForMeds.cat/en.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/Templates/dialog/wellness.catfamily/regionNotSupportedForMeds.cat/es.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/Templates/dialog/wellness.catfamily/regionNotSupportedForMeds.cat/he.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/Templates/dialog/wellness.catfamily/regionNotSupportedForMeds.cat/it.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/Templates/dialog/wellness.catfamily/regionNotSupportedForMeds.cat/nb.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/Templates/dialog/wellness.catfamily/regionNotSupportedForMeds.cat/nl-be.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/Templates/dialog/wellness.catfamily/regionNotSupportedForMeds.cat/pt.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/Templates/dialog/wellness.catfamily/regionNotSupportedForMeds.cat/sv.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/Templates/dialog/wellness.catfamily/regionNotSupportedForMeds.cat/vi.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/Templates/dialog/wellness.catfamily/regionNotSupportedForMeds.cat/zh-tw.cat.bin`
- `/System/Library/CoreServices/BluetoothUIService.app/Banner-PID-8218-Seed/Banner-PID-8218-8-Seed.png`
- `/System/Library/CoreServices/BluetoothUIService.app/Banner-PID-8218-Seed/Banner-PID-8218-9-Seed.png`
- `/System/Library/NanoTimeKit/FaceBundles/NTKPride2025FaceBundle.bundle/Assets.car`
- `/System/Library/NanoTimeKit/FaceBundles/NTKPride2025FaceBundle.bundle/Info.plist`
- `/System/Library/NanoTimeKit/FaceBundles/NTKPride2025FaceBundle.bundle/Localizable.loctable`
- `/System/Library/NanoTimeKit/FaceBundles/NTKPride2025FaceBundle.bundle/NTKPride2025FaceBundle`
- `/System/Library/NanoTimeKit/FaceBundles/NTKPride2025FaceBundle.bundle/_CodeSignature/CodeResources`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/f949be2b5bc29e8d9e985afc0fa7fbf4a3559fb0.asset/AssetData/settings.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/f949be2b5bc29e8d9e985afc0fa7fbf4a3559fb0.asset/Info.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_SharingDeviceAssets/7f50a81a71f8ff6cebbf2d151474b0256a253146.asset/AssetData/empty.txt`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_SharingDeviceAssets/7f50a81a71f8ff6cebbf2d151474b0256a253146.asset/Info.plist`
- `/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceSharedConfigurationXPCService.xpc/FindMyDeviceSharedConfigurationXPCService`
- `/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceSharedConfigurationXPCService.xpc/Info.plist`
- `/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceSharedConfigurationXPCService.xpc/InfoPlist.loctable`
- `/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceSharedConfigurationXPCService.xpc/_CodeSignature/CodeResources`
- `/System/Library/PrivateFrameworks/HeadphoneConfigs.framework/DeviceConfig-Seed.loctable`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/exerciseRingCompleted.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/exerciseRingCompleted.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/exerciseRingCompleted.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/exerciseRingCompleted.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/exerciseRingCompleted.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/exerciseRingCompleted.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/exerciseRingCompleted.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/exerciseRingCompleted.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/exerciseRingCompleted.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/goalCompletion.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/goalCompletion.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/goalCompletion.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/goalCompletion.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/goalCompletion.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/goalCompletion.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/goalCompletion.cat/es-us.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/goalCompletion.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/goalCompletion.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/goalCompletion.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/goalCompletion.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/goalCompletion.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/goalCompletion.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/goalCompletion.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/goalCompletion.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/goalHalfwayPoint.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/goalHalfwayPoint.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/goalHalfwayPoint.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalEnded.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalEnded.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalEnded.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalEnded.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalEnded.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalEnded.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalEnded.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalEnded.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalEnded.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalEnded.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalEnded.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalEnded.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalEnded.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalEnded.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalEnded.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalEnded.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalEnded.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalEnded.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalEnded.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalEnded.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalEnded.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalEnded.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalEnded.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingCurrentInterval.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingCurrentInterval.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingCurrentInterval.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingCurrentInterval.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingCurrentInterval.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingCurrentInterval.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingCurrentInterval.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingCurrentInterval.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingCurrentInterval.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingCurrentInterval.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingCurrentInterval.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingCurrentInterval.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingCurrentInterval.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingCurrentInterval.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingHeartRateZone.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingHeartRateZone.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingHeartRateZone.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingHeartRateZone.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingHeartRateZone.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingHeartRateZone.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingHeartRateZone.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingHeartRateZone.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingHeartRateZone.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingHeartRateZone.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingHeartRateZone.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingHeartRateZone.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingHeartRateZone.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingHeartRateZone.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingHeartRateZone.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingHeartRateZone.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingHeartRateZone.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingHeartRateZone.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingHeartRateZone.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingNonPace.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingNonPace.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingNonPace.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingNonPace.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingNonPace.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingNonPace.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingNonPace.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingNonPace.cat/es-us.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingNonPace.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingNonPace.cat/fr-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingNonPace.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingNonPace.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingNonPace.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingNonPace.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingNonPace.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingNonPace.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingNonPace.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingNonPace.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingNonPace.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingNonPace.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingNonPace.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingNonPace.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingNonPace.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/fr-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPace.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPreviousInterval.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPreviousInterval.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPreviousInterval.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPreviousInterval.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPreviousInterval.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPreviousInterval.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPreviousInterval.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPreviousInterval.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingPreviousInterval.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/intervalUpcomingSpeed.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/de-ch.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/fr-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionPace.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/lapCompletionSpeed.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/moveRingCompleted.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/moveRingCompleted.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/moveRingCompleted.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/moveRingCompleted.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/moveRingCompleted.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/moveRingCompleted.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/moveRingCompleted.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/moveRingCompleted.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/moveRingCompleted.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/moveRingCompleted.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/moveRingCompleted.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/moveRingCompleted.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/moveRingCompleted.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/moveRingCompleted.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/moveRingCompleted.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/moveRingCompleted.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/moveRingCompleted.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/moveRingCompleted.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/moveRingCompleted.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/moveRingCompleted.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/moveRingCompleted.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/moveRingCompleted.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/moveRingCompleted.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/moveRingCompleted.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/moveRingCompleted.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/moveRingCompleted.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/moveRingCompleted.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/moveRingCompleted.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/moveRingCompleted.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/pacerGoalCompletion.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/pacerGoalCompletion.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/pacerGoalCompletion.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/pacerGoalCompletion.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/pacerGoalCompletion.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/pacerGoalCompletion.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/pacerGoalCompletion.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/pacerGoalCompletion.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceAheadOfGhost.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceAheadOfGhost.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceAheadOfGhost.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceAheadOfGhost.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceBehindGhost.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceBehindGhost.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceBehindGhost.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceBehindGhost.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceBehindGhost.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceBehindGhost.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceBehindGhost.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceBehindGhost.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceBehindGhost.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceBehindGhost.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceBehindGhost.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceBehindGhost.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceBehindGhost.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceBehindGhost.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceBehindGhost.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceBehindGhost.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceBehindGhost.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceBehindGhost.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceBehindGhost.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceBehindGhost.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceExpired.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceExpired.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceExpired.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceExpired.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOffRoute.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOffRoute.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOffRoute.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOffRoute.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOffRoute.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOffRoute.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOffRoute.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOffRoute.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOffRoute.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOffRoute.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOffRoute.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOffRoute.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOffRoute.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOffRoute.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOffRoute.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOffRoute.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOffRoute.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOffRoute.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOffRoute.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOffRoute.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOnRoute.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOnRoute.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOnRoute.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOnRoute.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOnRoute.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOnRoute.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOnRoute.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOnRoute.cat/en-ie.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOnRoute.cat/en-sg.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOnRoute.cat/en-za.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOnRoute.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOnRoute.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOnRoute.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOnRoute.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOnRoute.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOnRoute.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOnRoute.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOnRoute.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOnRoute.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOnRoute.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOnRoute.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOnRoute.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOnRoute.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOnRoute.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOnRoute.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOnRoute.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOnRoute.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOnRoute.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOnRoute.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOnRoute.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOnRoute.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOnRoute.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceOnRoute.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompleteRaceWon.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompletedRaceLost.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompletedRaceLost.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompletedRaceLost.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompletedRaceLost.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompletedRaceLost.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompletedRaceLost.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompletedRaceLost.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompletedRaceLost.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompletedRaceLost.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompletedRaceLost.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompletedRaceLost.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompletedRaceLost.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompletedRaceLost.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompletedRaceLost.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompletedRaceLost.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompletedRaceLost.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompletedRaceLost.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompletedRaceLost.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompletedRaceLost.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompletedRaceLost.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompletedRaceLost.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompletedRaceLost.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompletedRaceLost.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/raceRouteCompletedRaceLost.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/segmentMarked.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/segmentMarked.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/segmentMarked.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/segmentMarked.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/segmentMarked.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/segmentMarked.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/segmentMarked.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/segmentMarked.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/segmentMarked.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/segmentMarked.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/segmentMarked.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/segmentMarked.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/segmentMarked.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/segmentMarked.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/segmentMarked.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/segmentMarked.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/segmentMarked.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/segmentMarked.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/trackStatusChanged.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/trackStatusChanged.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/trackStatusChanged.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/trackStatusChanged.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/trackStatusChanged.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/trackStatusChanged.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/trackStatusChanged.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/trackStatusChanged.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/trackStatusChanged.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/trackStatusChanged.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/trackStatusChanged.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/trackStatusChanged.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/trackStatusChanged.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/trackStatusChanged.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/trackStatusChanged.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/trackStatusChanged.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/trackStatusChanged.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/trackStatusChanged.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/trackStatusChanged.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/trackStatusChanged.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/trackStatusChanged.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/trackStatusChanged.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/trackStatusChanged.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistancePace.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistancePace.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistancePace.cat/de-ch.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistancePace.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistancePace.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistancePace.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistancePace.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistancePace.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistancePace.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistancePace.cat/fr-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistancePace.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistancePace.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistancePace.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistancePace.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistancePace.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistancePace.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistancePace.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistancePace.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistancePace.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistancePace.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistanceSpeed.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistanceSpeed.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistanceSpeed.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistanceSpeed.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistanceSpeed.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableDistanceSpeed.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableTime.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableTime.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableTime.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableTime.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableTime.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableTime.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableTime.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableTime.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableTime.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableTime.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableTime.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableTime.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableTime.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableTime.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableTime.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableTime.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableTime.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/transitionedNotableTime.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/workoutPaused.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/workoutPaused.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/workoutPaused.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/workoutPaused.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/workoutPaused.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/workoutPaused.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/workoutPaused.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/workoutResumed.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/workoutResumed.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/workoutResumed.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/workoutResumed.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/workoutResumed.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/workoutResumed.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/workoutResumed.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/workoutResumed.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/workoutResumed.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/workoutResumed.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/workoutResumed.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/workoutResumed.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/workoutResumed.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/workoutResumed.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/workoutResumed.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredNonPace.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredNonPace.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredNonPace.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredNonPace.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredNonPace.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredNonPace.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredNonPace.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredPace.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredPace.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredPace.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredPace.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredPace.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredPace.cat/fr-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredPace.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredPace.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredPace.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredPace.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredPace.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredPace.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredPace.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredPace.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredPace.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredPace.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredSpeed.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredSpeed.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredSpeed.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredSpeed.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredSpeed.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredSpeed.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredSpeed.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredSpeed.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredSpeed.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredSpeed.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredSpeed.cat/fr-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredSpeed.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredSpeed.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredSpeed.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredSpeed.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredSpeed.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredSpeed.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredSpeed.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredSpeed.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredSpeed.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredSpeed.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredSpeed.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneEnteredSpeed.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveNonPace.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveNonPace.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveNonPace.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveNonPace.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveNonPace.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveNonPace.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveNonPace.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveNonPace.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveNonPace.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAbovePace.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAbovePace.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAbovePace.cat/de-ch.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAbovePace.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAbovePace.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAbovePace.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAbovePace.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAbovePace.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAbovePace.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAbovePace.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAbovePace.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAbovePace.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAbovePace.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveSpeed.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveSpeed.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveSpeed.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveSpeed.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveSpeed.cat/fr-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveSpeed.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveSpeed.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveSpeed.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveSpeed.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedAboveSpeed.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/fr-ca.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowNonPace.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/de-ch.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowPace.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowSpeed.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowSpeed.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowSpeed.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/Templates/dialog/workoutVoiceFeedback.catfamily/zoneExitedBelowSpeed.cat/nb.cat.bin`
- `/System/Library/ProductDocuments/SoftwareLicenseAgreements/AudioAccessory.bundle/bg.lproj/License.html`
- `/System/Library/ProductDocuments/SoftwareLicenseAgreements/AudioAccessory.bundle/kk.lproj/License.html`
- `/System/Library/ProductDocuments/SoftwareLicenseAgreements/iOS.bundle/bg.lproj/License.html`
- `/System/Library/ProductDocuments/SoftwareLicenseAgreements/iOS.bundle/kk.lproj/License.html`
- `/private/var/staged_system_apps/Tips.app/ar.lproj/nlu.appintents/ace60a36ead8b8be9c5b8b48df7fdf76.version`
- `/private/var/staged_system_apps/Tips.app/bg.lproj/nlu.appintents/b0c9dfc139d9d192df746644b0e77922.version`
- `/private/var/staged_system_apps/Tips.app/bn.lproj/nlu.appintents/08274c26994aefabf227ce4dd5896e7f.version`
- `/private/var/staged_system_apps/Tips.app/ca.lproj/nlu.appintents/fb7053593a2d6ae6949fc3b1be6b9b71.version`
- `/private/var/staged_system_apps/Tips.app/cs.lproj/nlu.appintents/138cbc89858f6bc30a3315b69c39c8c0.version`
- `/private/var/staged_system_apps/Tips.app/da.lproj/nlu.appintents/3ed9416d6f48d62b74a420c0f8d9a371.version`
- `/private/var/staged_system_apps/Tips.app/de.lproj/nlu.appintents/449007623bce0704d9fcf92783abd8ee.version`
- `/private/var/staged_system_apps/Tips.app/el.lproj/nlu.appintents/7bb702b13f29723ccad0252ba8c85c06.version`
- `/private/var/staged_system_apps/Tips.app/en.lproj/nlu.appintents/b581f9b1c0c46266c4287e3785b9965c.version`
- `/private/var/staged_system_apps/Tips.app/en_AU.lproj/nlu.appintents/4a3c0bb569820a17b0b79e931f6fb1db.version`
- `/private/var/staged_system_apps/Tips.app/en_GB.lproj/nlu.appintents/f2b1d80bbd443c4849ada2b20a2227bc.version`
- `/private/var/staged_system_apps/Tips.app/es.lproj/nlu.appintents/1472b61d982ba353e4de17ea0b088142.version`
- `/private/var/staged_system_apps/Tips.app/es_419.lproj/nlu.appintents/01237cff2bc05f7a29d62fd93f5ce090.version`
- `/private/var/staged_system_apps/Tips.app/es_US.lproj/nlu.appintents/4a9b9533fd67c6452fd3825e8de70a16.version`
- `/private/var/staged_system_apps/Tips.app/fi.lproj/nlu.appintents/900a6d5c880e1dbfa33f2cb37f8abeda.version`
- `/private/var/staged_system_apps/Tips.app/fr.lproj/nlu.appintents/0b0bd4893064ca5c5bae6a84350b9be5.version`
- `/private/var/staged_system_apps/Tips.app/fr_CA.lproj/nlu.appintents/563526bd06beb488ce1e0d3ce1506c56.version`
- `/private/var/staged_system_apps/Tips.app/gu.lproj/nlu.appintents/e4f1b3c41d45d619fccf5e5bdadd6ea3.version`
- `/private/var/staged_system_apps/Tips.app/he.lproj/nlu.appintents/b2071eb51883502b7b758432519610f8.version`
- `/private/var/staged_system_apps/Tips.app/hi.lproj/nlu.appintents/1c40b30caa0740cd04c31e28b92e16df.version`
- `/private/var/staged_system_apps/Tips.app/hr.lproj/nlu.appintents/ae93eb81f77aa26918d205fccd4a3925.version`
- `/private/var/staged_system_apps/Tips.app/hu.lproj/nlu.appintents/8413727c35e44a96ecba66dbaceac55a.version`
- `/private/var/staged_system_apps/Tips.app/id.lproj/nlu.appintents/e288d2690720135476745945c58f5861.version`
- `/private/var/staged_system_apps/Tips.app/it.lproj/nlu.appintents/4e4ceb24f4332cb6572206e5f67266ea.version`
- `/private/var/staged_system_apps/Tips.app/ja.lproj/nlu.appintents/b128b9fb765feceb94fe981bb99ff328.version`
- `/private/var/staged_system_apps/Tips.app/kk.lproj/nlu.appintents/d35b7c2e580eee92a7684a1e96e605be.version`
- `/private/var/staged_system_apps/Tips.app/kn.lproj/nlu.appintents/3bbe3a3dc8b2e4a80041203d28b8a088.version`
- `/private/var/staged_system_apps/Tips.app/ko.lproj/nlu.appintents/6501adabd355a8063d8fa5fa08b025cb.version`
- `/private/var/staged_system_apps/Tips.app/lt.lproj/nlu.appintents/baa6291f70531a4018c31fd64bcc8904.version`
- `/private/var/staged_system_apps/Tips.app/ml.lproj/nlu.appintents/6968591fc9670194f643da4e31eb4421.version`
- `/private/var/staged_system_apps/Tips.app/mr.lproj/nlu.appintents/cc892e3441633d7ae69773ac99442eee.version`
- `/private/var/staged_system_apps/Tips.app/ms.lproj/nlu.appintents/6c6f878456e326c02a1fd5ed3844c20c.version`
- `/private/var/staged_system_apps/Tips.app/nl.lproj/nlu.appintents/06fb33bed14a3cf64a668002eb0442ed.version`
- `/private/var/staged_system_apps/Tips.app/no.lproj/nlu.appintents/3546b1dc62dde8456ef0249e64c923ea.version`
- `/private/var/staged_system_apps/Tips.app/or.lproj/nlu.appintents/462d4bcb8c53e729e7477fdf50cf00ad.version`
- `/private/var/staged_system_apps/Tips.app/pa.lproj/nlu.appintents/abbe9ee086e5231a8e482ad10486c37c.version`
- `/private/var/staged_system_apps/Tips.app/pl.lproj/nlu.appintents/9ea374d7f5d69813e1b5c20969bf7c48.version`
- `/private/var/staged_system_apps/Tips.app/pt_BR.lproj/nlu.appintents/f453029321a38ea7122e63dc1b4029cc.version`
- `/private/var/staged_system_apps/Tips.app/ro.lproj/nlu.appintents/4b46cd33515f98532d03ae49cabd1eda.version`
- `/private/var/staged_system_apps/Tips.app/ru.lproj/nlu.appintents/b916a4a9a2de3847ac7f392851475fcb.version`
- `/private/var/staged_system_apps/Tips.app/sk.lproj/nlu.appintents/6b881bb472688dd185a43f4e09fcef17.version`
- `/private/var/staged_system_apps/Tips.app/sl.lproj/nlu.appintents/6f2ae46f8e11007c16a490c848e9d0b2.version`
- `/private/var/staged_system_apps/Tips.app/sv.lproj/nlu.appintents/d246c31f3f25da2341ead5052661dde8.version`
- `/private/var/staged_system_apps/Tips.app/ta.lproj/nlu.appintents/867a3efd56d15993bc63f1174fab7a28.version`
- `/private/var/staged_system_apps/Tips.app/th.lproj/nlu.appintents/e659e6084b2da6474cffdfc4c6929d5b.version`
- `/private/var/staged_system_apps/Tips.app/tr.lproj/nlu.appintents/e6ecf85a76411b57b777cc14aebb15d6.version`
- `/private/var/staged_system_apps/Tips.app/uk.lproj/nlu.appintents/9efd93a204b479613b575bcecf2c72cb.version`
- `/private/var/staged_system_apps/Tips.app/ur.lproj/nlu.appintents/a080ac67ecc47c83ec935a91c9de883b.version`
- `/private/var/staged_system_apps/Tips.app/vi.lproj/nlu.appintents/ed55676c5daf9eb5936612dbe9dbdb87.version`
- `/private/var/staged_system_apps/Tips.app/zh_CN.lproj/nlu.appintents/db03d101388dc2176c8ef8a9764e94b5.version`
- `/private/var/staged_system_apps/Tips.app/zh_HK.lproj/nlu.appintents/736a40efe15e4819211b798963656a4f.version`
- `/private/var/staged_system_apps/Tips.app/zh_TW.lproj/nlu.appintents/0ee4f144219e7f4fb4be1c0d9e815755.version`
- `/private/var/staged_system_apps/VoiceMemos.app/en.lproj/nlu.appintents/dc732588c0cd37105440f8970afe845f.version`

</details>

### ❌ Removed

#### filesystem (79)

<details>
  <summary><i>View Files</i></summary>

- `/System/Library/Frameworks/SystemConfiguration.framework/get-mobility-info`
- `/System/Library/LaunchDaemons/com.apple.memoryanalyticsd.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.FaceTime.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.IDS.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.Messages.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.MessagesEvents.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.Registration.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.StatusKit.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.Transport.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.apsd.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.calls.calldirectory.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.calls.callkit.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.calls.callservicesd.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.calls.conversationkit.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.calls.facetime.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.calls.identitylookup.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.calls.incallservice.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.calls.messagefilter.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.calls.mobilephone.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.calls.telephonyui.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.calls.telephonyutilities.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.voicemail.plist`
- `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/AirPlayDiagnosticExtension.appex/AirPlayDiagnosticExtension`
- `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/AirPlayDiagnosticExtension.appex/Info.plist`
- `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/AirPlayDiagnosticExtension.appex/_CodeSignature/CodeResources`
- `/private/var/staged_system_apps/Tips.app/ar.lproj/nlu.appintents/4728d85cdbf7b3580e4b3b80b9e30fb2.version`
- `/private/var/staged_system_apps/Tips.app/bg.lproj/nlu.appintents/1428c8d75ce1dff809f4142f6fd12dcb.version`
- `/private/var/staged_system_apps/Tips.app/bn.lproj/nlu.appintents/d4dca2d8b43ebbcd825f4d2922ce132e.version`
- `/private/var/staged_system_apps/Tips.app/ca.lproj/nlu.appintents/22292dd88fca6cabff3b6e0ccc9d55a7.version`
- `/private/var/staged_system_apps/Tips.app/cs.lproj/nlu.appintents/9ce6fcbd8cfd38251786828815da4dba.version`
- `/private/var/staged_system_apps/Tips.app/da.lproj/nlu.appintents/bb94fccf0e60c39ba51856f4b69a9d78.version`
- `/private/var/staged_system_apps/Tips.app/de.lproj/nlu.appintents/5d6e06dff7380a780461eae63630b0e2.version`
- `/private/var/staged_system_apps/Tips.app/el.lproj/nlu.appintents/ee1a787a45d3f133aa9a855f2c899236.version`
- `/private/var/staged_system_apps/Tips.app/en.lproj/nlu.appintents/cb9d507db7d0a83d8097a6d012f7259f.version`
- `/private/var/staged_system_apps/Tips.app/en_AU.lproj/nlu.appintents/b26f8fa4c14a268ae08bdd8f39cf6ddc.version`
- `/private/var/staged_system_apps/Tips.app/en_GB.lproj/nlu.appintents/95c39a2e1de44b45a854e154fdb7f3be.version`
- `/private/var/staged_system_apps/Tips.app/es.lproj/nlu.appintents/0b909522c9526e3b97ce21b3a9fb57bd.version`
- `/private/var/staged_system_apps/Tips.app/es_419.lproj/nlu.appintents/8c7f70c2f5c27c6a9d6b99fe1582fe2d.version`
- `/private/var/staged_system_apps/Tips.app/es_US.lproj/nlu.appintents/1339b18492eb52e2a772b1227c0208ce.version`
- `/private/var/staged_system_apps/Tips.app/fi.lproj/nlu.appintents/3822b4c6c31ddac4541ad7f4500112d1.version`
- `/private/var/staged_system_apps/Tips.app/fr.lproj/nlu.appintents/fa3c6d64a734f59f88a60414254b580f.version`
- `/private/var/staged_system_apps/Tips.app/fr_CA.lproj/nlu.appintents/ef730f90ae9eac85b35f65da5d5c4b6b.version`
- `/private/var/staged_system_apps/Tips.app/gu.lproj/nlu.appintents/9e3fbccabf5abe4668bbd8e580e81aef.version`
- `/private/var/staged_system_apps/Tips.app/he.lproj/nlu.appintents/d953558d47b66922335a5eb91c9a0d97.version`
- `/private/var/staged_system_apps/Tips.app/hi.lproj/nlu.appintents/bac95a6a4cee5e312a870b5dd66ee611.version`
- `/private/var/staged_system_apps/Tips.app/hr.lproj/nlu.appintents/8c7835573b9aba02456c055bb16fc1f9.version`
- `/private/var/staged_system_apps/Tips.app/hu.lproj/nlu.appintents/76d05b8e16319063ca81e673bd97e145.version`
- `/private/var/staged_system_apps/Tips.app/id.lproj/nlu.appintents/a1195f9bea00930f1dbbc4fc0e7092fe.version`
- `/private/var/staged_system_apps/Tips.app/it.lproj/nlu.appintents/ad93749896c30d778647ab6f90b0258e.version`
- `/private/var/staged_system_apps/Tips.app/ja.lproj/nlu.appintents/1164e579c8037e75eeb4ae6c5c2140d2.version`
- `/private/var/staged_system_apps/Tips.app/kk.lproj/nlu.appintents/32b20c6dbb7ced387a84e57323a0d9f4.version`
- `/private/var/staged_system_apps/Tips.app/kn.lproj/nlu.appintents/7f739accf58a800c85b60e2ed46094f0.version`
- `/private/var/staged_system_apps/Tips.app/ko.lproj/nlu.appintents/da420b505d5cf2c4a1b66bfe8661ad2b.version`
- `/private/var/staged_system_apps/Tips.app/lt.lproj/nlu.appintents/46bdc8d27bae1ff60c1c348195579fa0.version`
- `/private/var/staged_system_apps/Tips.app/ml.lproj/nlu.appintents/756a4005e92aa4c75a01498b389ab8d2.version`
- `/private/var/staged_system_apps/Tips.app/mr.lproj/nlu.appintents/6e24e2a6c254778765afdbeae8f72d72.version`
- `/private/var/staged_system_apps/Tips.app/ms.lproj/nlu.appintents/f18e675a9f2233aa92e4ad264d5a235c.version`
- `/private/var/staged_system_apps/Tips.app/nl.lproj/nlu.appintents/a8f22818ef4f694b8fad6cfd58fec12a.version`
- `/private/var/staged_system_apps/Tips.app/no.lproj/nlu.appintents/578867246a385ba8ff8ab406efd420c2.version`
- `/private/var/staged_system_apps/Tips.app/or.lproj/nlu.appintents/55269225074f4723f863342d3db927d2.version`
- `/private/var/staged_system_apps/Tips.app/pa.lproj/nlu.appintents/ca535a65ffb0ca7a64f07ad8c81307a6.version`
- `/private/var/staged_system_apps/Tips.app/pl.lproj/nlu.appintents/e59f5fbb437590d4c1cb0333c043538c.version`
- `/private/var/staged_system_apps/Tips.app/pt_BR.lproj/nlu.appintents/6bb584064225c6d864e819deb93d3c2c.version`
- `/private/var/staged_system_apps/Tips.app/ro.lproj/nlu.appintents/d4a04856da463222a60e696ab5f54d01.version`
- `/private/var/staged_system_apps/Tips.app/ru.lproj/nlu.appintents/bc570adc7c2b950201879878d23b187c.version`
- `/private/var/staged_system_apps/Tips.app/sk.lproj/nlu.appintents/adb24457f08a998b6016beb856555193.version`
- `/private/var/staged_system_apps/Tips.app/sl.lproj/nlu.appintents/2f4e7b4a2cf5260302dc6b0754bd90ae.version`
- `/private/var/staged_system_apps/Tips.app/sv.lproj/nlu.appintents/a7070117af18c8d82ef48227061b26f0.version`
- `/private/var/staged_system_apps/Tips.app/ta.lproj/nlu.appintents/3c7482ac4b289e0f7c773df5d0509fd7.version`
- `/private/var/staged_system_apps/Tips.app/th.lproj/nlu.appintents/c279798735024110de8f170357d3a9bd.version`
- `/private/var/staged_system_apps/Tips.app/tr.lproj/nlu.appintents/80f4866224acd710b52e752f5c6868d3.version`
- `/private/var/staged_system_apps/Tips.app/uk.lproj/nlu.appintents/16c9f6cb19a891749f5a92999ccfffc8.version`
- `/private/var/staged_system_apps/Tips.app/ur.lproj/nlu.appintents/4ae57218da3ad7c832be326eaa670c5a.version`
- `/private/var/staged_system_apps/Tips.app/vi.lproj/nlu.appintents/e570ca6f941b3cc4e8366cf1e883d737.version`
- `/private/var/staged_system_apps/Tips.app/zh_CN.lproj/nlu.appintents/b25ee90b6213fd22cc67ef6e998ceaca.version`
- `/private/var/staged_system_apps/Tips.app/zh_HK.lproj/nlu.appintents/f5852e4f5276460bd2f2e3b12461527b.version`
- `/private/var/staged_system_apps/Tips.app/zh_TW.lproj/nlu.appintents/21babc96cd60bc61dfce66ce60b30273.version`
- `/private/var/staged_system_apps/VoiceMemos.app/en.lproj/nlu.appintents/6df263de6e0df9cd51884917d9bff7dd.version`
- `/usr/libexec/memoryanalyticsd`

</details>

## Feature Flags

### ⬆️ Updated (2)

<details>
  <summary><i>View Updated</i></summary>

#### NanoTimeKit.plist

>  `Domain/NanoTimeKit.plist`

```diff

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
+	<key>pride2025</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>rhizome</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### GlobalDisclosures.plist

>  `GlobalDisclosures.plist`

```diff

 		<key>Disclosed</key>
 		<true/>
 	</dict>
+	<key>1b3196a9-6a20-4559-60fd-bb3743219ab3</key>
+	<dict>
+		<key>Disclosed</key>
+		<true/>
+	</dict>
 	<key>2298f8e4-f510-4776-b2c1-a85ea314b1f8</key>
 	<dict>
 		<key>Disclosed</key>

```


</details>

## EOF
