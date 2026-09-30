# 18.3 (22D5034e) .vs 18.3 (22D5040d)

## IPSWs

- `iPhone17,1_18.3_22D5034e_Restore.ipsw`
- `iPhone17,1_18.3_22D5040d_Restore.ipsw`

## Kernel

### Version

| iOS               | Version | Build               | Date                        |
| :---------------- | :------ | :------------------ | :-------------------------- |
| 18.3 *(22D5034e)* | 24.3.0  | 11215.80.25.502.1~1 | Mon, 09Dec2024 20:19:15 PST |
| 18.3 *(22D5040d)* | 24.3.0  | 11215.80.28.502.2~1 | Tue, 17Dec2024 22:51:07 PST |

### Kexts

#### ⬆️ Updated (21)

<details>
  <summary><i>View Updated</i></summary>

>  `com.apple.driver.AppleARMWatchdogTimer`

```diff

-277.80.1.0.0
-  __TEXT.__cstring: 0x1206
-  __TEXT_EXEC.__text: 0x5054
+277.80.2.0.0
+  __TEXT.__cstring: 0x123e
+  __TEXT_EXEC.__text: 0x5064
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x118
   __DATA.__common: 0xc0

   __DATA_CONST.__kalloc_var: 0x190
   Functions: 162
   Symbols:   0
-  CStrings:  119
+  CStrings:  120
 
CStrings:
+ "\"Reconfig Watchdog monitoring can't be disabled\" @%s:%d"

```

>  `com.apple.driver.AppleAVE2`

```diff

-803.52.0.0.0
+803.48.1.0.0
   __TEXT.__const: 0x2ee30
-  __TEXT.__cstring: 0x359bd
+  __TEXT.__cstring: 0x359b5
   __TEXT.__os_log: 0x40a21
-  __TEXT_EXEC.__text: 0x146530
+  __TEXT_EXEC.__text: 0x1464b0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x290
   __DATA.__common: 0x130

   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x38
   __DATA_CONST.__mod_term_func: 0x38
-  __DATA_CONST.__const: 0x6318
+  __DATA_CONST.__const: 0x6310
   __DATA_CONST.__kalloc_type: 0x3040
   __DATA_CONST.__kalloc_var: 0xfa0
   Functions: 2499
   Symbols:   0
-  CStrings:  7015
+  CStrings:  7014
 
CStrings:
+ "23:35:43"
+ "803.48.1"
+ "Dec 17 2024"
+ "ID: %d | Process: "
- "20:20:33"
- "803.52.0"
- "Dec  9 2024"
- "ID: %d | Input: "
- "Process: "

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

>  `com.apple.driver.AppleH16ANEInterface`

```diff

-8.203.4.0.0
-  __TEXT.__os_log: 0x3303b
+8.300.0.0.0
+  __TEXT.__os_log: 0x330b3
   __TEXT.__cstring: 0xa5cd
   __TEXT.__const: 0x690
-  __TEXT_EXEC.__text: 0xa3bb0
+  __TEXT_EXEC.__text: 0xa3c60
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x3948
   __DATA.__common: 0x3c8
CStrings:
+ "ANE%d: %s: ERROR: ANE_ProgramDestroy_gated failed for programHandle: 0x%llx. result= 0x%x\n"
+ "ANE%d: %s: woken up by a new fDriverInitiatedSleepAssertions: %u\n"
- "ANE%d: %s: ERROR: ANE_ProgramDestroy_gated() failed for programHandle: 0x%llx. result= 0x%x\n"
- "ANE%d: %s: woken up by a new fDriverInitiatedSleepAssertions.\n"

```

>  `com.apple.driver.AppleHIDTransportSPI`

```diff

-8100.32.0.0.0
+8140.4.0.0.0
   __TEXT.__const: 0x348
-  __TEXT.__cstring: 0x7a73
-  __TEXT_EXEC.__text: 0x3d4b0
+  __TEXT.__cstring: 0x7d1f
+  __TEXT_EXEC.__text: 0x3eebc
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xc8
+  __DATA.__data: 0x348
   __DATA.__common: 0xd8
-  __DATA_CONST.__auth_got: 0x300
-  __DATA_CONST.__got: 0x178
+  __DATA_CONST.__auth_got: 0x320
+  __DATA_CONST.__got: 0x180
   __DATA_CONST.__mod_init_func: 0x28
   __DATA_CONST.__mod_term_func: 0x28
-  __DATA_CONST.__const: 0x3210
+  __DATA_CONST.__const: 0x32c0
   __DATA_CONST.__kalloc_type: 0xa80
   __DATA_CONST.__kalloc_var: 0x320
-  Functions: 655
+  Functions: 674
   Symbols:   0
-  CStrings:  858
+  CStrings:  897
 
CStrings:
+ "%.*s\n"
+ "/AppleInternal/Library/BuildRoots/cb6e5652-bcd9-11ef-b66e-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/hidspi/HSMDevice.h"
+ "/AppleInternal/Library/BuildRoots/cb6e5652-bcd9-11ef-b66e-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/hidspi/HSMDeviceInterface.h"
+ "/AppleInternal/Library/BuildRoots/cb6e5652-bcd9-11ef-b66e-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/hidspi/HSMDeviceTest.h"
+ "/AppleInternal/Library/BuildRoots/cb6e5652-bcd9-11ef-b66e-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/hidspi/HSMHIDInterface.h"
+ "/AppleInternal/Library/BuildRoots/cb6e5652-bcd9-11ef-b66e-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/hidspi/HSMParserTest.h"
+ "/AppleInternal/Library/BuildRoots/cb6e5652-bcd9-11ef-b66e-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/hidspi/HSMSPITest.h"
+ "/AppleInternal/Library/BuildRoots/cb6e5652-bcd9-11ef-b66e-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/hidspi/HSMTransferDevice.h"
+ "/AppleInternal/Library/BuildRoots/cb6e5652-bcd9-11ef-b66e-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/hidspi/HSMTransferTest.h"
+ "/AppleInternal/Library/BuildRoots/cb6e5652-bcd9-11ef-b66e-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/hidspi/HSParserDevice.h"
+ "/AppleInternal/Library/BuildRoots/cb6e5652-bcd9-11ef-b66e-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/hidspi/HSParserTest.h"
+ "/AppleInternal/Library/BuildRoots/cb6e5652-bcd9-11ef-b66e-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/hidspi/HSTransferTest.h"
+ "/chosen"
+ "BackGlass"
+ "Battery"
+ "Camera"
+ "Checking for %s\n"
+ "CmCl"
+ "Components"
+ "CoverGlass"
+ "Display"
+ "FSCl"
+ "FaceID"
+ "Invalid parameters: %p, %p, %lu\n"
+ "LCfg"
+ "MTUB"
+ "McTUB"
+ "RepairHistory"
+ "SrvP"
+ "TouchID"
+ "Unknown component: %s\n"
+ "[0x%llx][%llx][%s::%s]: ERROR!! Component array not found"
+ "[0x%llx][%llx][%s::%s]: ERROR!! Description not found"
+ "[0x%llx][%llx][%s::%s]: ERROR!! Fail to convert array to iterator"
+ "[0x%llx][%llx][%s::%s]: Repair history detected for %s"
+ "[0x%llx][%llx][%s::%s]: Repair history entry not found"
+ "[0x%llx][%llx][%s::%s]: Repair history property not found"
+ "[0x%llx][%llx][%s::%s]: [%s] : %s"
+ "bCfg"
+ "bcrt"
+ "componentArray"
+ "dCfg"
+ "detected"
+ "found data %s\n"
+ "not detected"
+ "prpc"
+ "psd2"
+ "repair-history"
+ "tcrt"
+ "vcrt"
- "/AppleInternal/Library/BuildRoots/3e45148f-b7b4-11ef-b253-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/hidspi/HSMDevice.h"
- "/AppleInternal/Library/BuildRoots/3e45148f-b7b4-11ef-b253-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/hidspi/HSMDeviceInterface.h"
- "/AppleInternal/Library/BuildRoots/3e45148f-b7b4-11ef-b253-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/hidspi/HSMDeviceTest.h"
- "/AppleInternal/Library/BuildRoots/3e45148f-b7b4-11ef-b253-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/hidspi/HSMHIDInterface.h"
- "/AppleInternal/Library/BuildRoots/3e45148f-b7b4-11ef-b253-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/hidspi/HSMParserTest.h"
- "/AppleInternal/Library/BuildRoots/3e45148f-b7b4-11ef-b253-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/hidspi/HSMSPITest.h"
- "/AppleInternal/Library/BuildRoots/3e45148f-b7b4-11ef-b253-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/hidspi/HSMTransferDevice.h"
- "/AppleInternal/Library/BuildRoots/3e45148f-b7b4-11ef-b253-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/hidspi/HSMTransferTest.h"
- "/AppleInternal/Library/BuildRoots/3e45148f-b7b4-11ef-b253-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/hidspi/HSParserDevice.h"
- "/AppleInternal/Library/BuildRoots/3e45148f-b7b4-11ef-b253-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/hidspi/HSParserTest.h"
- "/AppleInternal/Library/BuildRoots/3e45148f-b7b4-11ef-b253-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/hidspi/HSTransferTest.h"

```

>  `com.apple.driver.AppleM2ScalerCSCDriver`

```diff

-148.6.4.0.0
+148.6.5.0.0
   __TEXT.__cstring: 0x1673a
   __TEXT.__const: 0x4ecc8
-  __TEXT_EXEC.__text: 0xd6024
+  __TEXT_EXEC.__text: 0xd6078
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x1fe40
   __DATA.__common: 0x20a8

```

>  `com.apple.driver.AppleOLYHAL`

```diff

-425.2.0.0.0
+425.3.0.0.0
   __TEXT.__const: 0x7a8
   __TEXT.__cstring: 0x45ad
-  __TEXT_EXEC.__text: 0x1ca10
+  __TEXT_EXEC.__text: 0x1ca14
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x18c
   __DATA.__common: 0x170

```

>  `com.apple.driver.AppleSARService`

```diff

-1218.0.0.0.0
+1219.0.0.0.0
   __TEXT.__const: 0x790
-  __TEXT.__cstring: 0xaacb
-  __TEXT.__os_log: 0xcac7
-  __TEXT_EXEC.__text: 0x5b7d4
+  __TEXT.__cstring: 0xaac1
+  __TEXT.__os_log: 0xcabd
+  __TEXT_EXEC.__text: 0x5b7fc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd8
   __DATA.__common: 0x5f0
CStrings:
+ "%s::%s:%d: Current Configuration: HSAR: %s, simulation mode: %s, simulation sleep mode: %s, sleep ts: %llu, wake ts: %llu\n"
+ "%s::%s:%d: Trying to do an action due to 0 SAR budget"
+ "%s::%s:%d: Trying to do an action due to the sequence number mismatch! The received sequence number (%u) is not consecutive. The previous sequence number is %u\n"
- "#D: %s::%s:%d: Current Configuration: HSAR: %s, simulation mode: %s, simulation sleep mode: %s, sleep ts: %llu, wake ts: %llu\n"
- "%s::%s:%d: Trying to trigger logdump due to 0 SAR budget"
- "%s::%s:%d: Trying to trigger logdump due to the sequence number mismatch! The received sequence number (%u) is not consecutive. The previous sequence number is %u\n"

```

>  `com.apple.driver.AppleSEPKeyStore`

```diff

-1827.80.9.0.0
-  __TEXT.__cstring: 0x3ace
+1827.80.10.0.0
+  __TEXT.__cstring: 0x3acf
   __TEXT.__const: 0x874
   __TEXT_EXEC.__text: 0x3d788
   __TEXT_EXEC.__auth_stubs: 0x0
CStrings:
+ "1827.80.10"
+ "23:23:34"
+ "Dec 17 2024"
- "1827.80.9"
- "20:19:10"
- "Dec  9 2024"

```

>  `com.apple.driver.AppleT8140CLPC`

```diff

-1175.80.2.0.0
+1175.80.3.0.0
   __TEXT.__cstring: 0x2b9e
-  __TEXT.__const: 0xc8c
-  __TEXT_EXEC.__text: 0x4fee4
+  __TEXT.__const: 0xc7c
+  __TEXT_EXEC.__text: 0x4ff2c
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xaff0
+  __DATA.__data: 0xb030
   __DATA.__common: 0x8121
   __DATA.__bss: 0x278
   __DATA_CONST.__auth_got: 0x4b0
   __DATA_CONST.__got: 0xd8
   __DATA_CONST.__mod_init_func: 0x118
   __DATA_CONST.__mod_term_func: 0x18
-  __DATA_CONST.__const: 0x54d8
+  __DATA_CONST.__const: 0x54f0
   __DATA_CONST.__kalloc_type: 0x380
   __DATA_CONST.__kalloc_var: 0x370
   Functions: 1327
CStrings:
+ "2024-12-17T23:18:35-08:00"
+ "AppleCLPC-1175.80.3"
- "2024-12-09T20:16:50-08:00"
- "AppleCLPC-1175.80.2"

```

>  `com.apple.driver.AppleThunderboltDPAdapterFamily`

```diff

-864.80.1.0.0
+864.80.2.0.0
   __TEXT.__cstring: 0xd79f
   __TEXT.__const: 0x20
-  __TEXT_EXEC.__text: 0x3d43c
+  __TEXT_EXEC.__text: 0x3d5a8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0xd8

```

>  `com.apple.driver.IOPAudioVoiceTriggerDevice`

```diff

 420.7.0.0.0
   __TEXT.__const: 0x78
-  __TEXT.__cstring: 0x2c2b
+  __TEXT.__cstring: 0x2c22
   __TEXT.__os_log: 0x16e9
   __TEXT_EXEC.__text: 0xb458
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__kalloc_type: 0xc0
   Functions: 326
   Symbols:   0
-  CStrings:  232
+  CStrings:  231
 
CStrings:
+ "23:39:06"
+ "Dec 17 2024"
- "20:22:51"
- "20:22:52"
- "Dec  9 2024"

```

>  `com.apple.filesystems.apfs`

```diff

-2317.80.2.0.1
+2317.80.3.0.2
   __TEXT.__const: 0x790
-  __TEXT.__cstring: 0x489fb
-  __TEXT_EXEC.__text: 0x13b2b8
+  __TEXT.__cstring: 0x48aa8
+  __TEXT_EXEC.__text: 0x13b504
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x698
   __DATA.__bss: 0xc60

   __DATA_CONST.__kalloc_var: 0x28a0
   Functions: 2278
   Symbols:   0
-  CStrings:  6310
+  CStrings:  6313
 
CStrings:
+ "%s:%d: %s This operation is not valid on a non-content-protected volume.\n"
+ "%s:%d: %s failed to remove mapping %lld->%lld (%lld) from mapping tree, error %d\n"
+ "2024/12/17"
+ "2317.80.3.0.2"
+ "23:06:25"
+ "Dec 17 2024"
+ "apfs-2317.80.3.0.2"
+ "apfs_removexattr"
- "2024/12/09"
- "20:09:10"
- "2317.80.2.0.1"
- "Dec  9 2024"
- "apfs-2317.80.2.0.1"

```

>  `com.apple.iokit.IOAVFamily`

```diff

-483.80.3.0.0
+483.80.4.0.1
   __TEXT.__cstring: 0xa784
-  __TEXT.__os_log: 0x9a1d
+  __TEXT.__os_log: 0x9995
   __TEXT.__const: 0xe7d4
-  __TEXT_EXEC.__text: 0x844e4
+  __TEXT_EXEC.__text: 0x840c0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd0
   __DATA.__common: 0x988

```

>  `com.apple.iokit.IOAccessoryManager`

```diff

-1004.80.3.0.0
+1004.80.3.0.1
   __TEXT.__const: 0x304
   __TEXT.__cstring: 0x1081c
   __TEXT.__os_log: 0x10799
-  __TEXT_EXEC.__text: 0xed928
+  __TEXT_EXEC.__text: 0xed97c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x7e8
   __DATA.__common: 0x1630

```

>  `com.apple.iokit.IOHIDFamily`

```diff

-2104.80.2.0.0
-  __TEXT.__cstring: 0x24b6
+2104.80.4.0.0
+  __TEXT.__cstring: 0x24b5
   __TEXT.__const: 0x6c8
   __TEXT.__os_log: 0x2a2f
-  __TEXT_EXEC.__text: 0x63218
+  __TEXT_EXEC.__text: 0x6335c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xbcc
   __DATA.__common: 0x748
CStrings:
+ "2211121121111122111111222222111212222222222222111111111111111121211"
- "22111211211111221111111222222111212222222222222111111111111111121211"

```

>  `com.apple.iokit.IOTimeSyncFamily`

```diff

-1320.8.0.0.0
+1330.2.0.0.0
   __TEXT.__cstring: 0x3298
-  __TEXT.__os_log: 0x74e4
+  __TEXT.__os_log: 0x7566
   __TEXT.__const: 0x1d8
-  __TEXT_EXEC.__text: 0x2f424
+  __TEXT_EXEC.__text: 0x2f4e8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd0
   __DATA.__common: 0x638
   __DATA.__bss: 0x39
-  __DATA_CONST.__auth_got: 0x3e8
+  __DATA_CONST.__auth_got: 0x3f8
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__mod_init_func: 0xf8
   __DATA_CONST.__mod_term_func: 0xf8

   __DATA_CONST.__kalloc_var: 0x280
   Functions: 1202
   Symbols:   0
-  CStrings:  629
+  CStrings:  631
 
CStrings:
+ "  %s(%s): Callback thread stop semaphore signal returned error %d"
+ "  %s(%s): Callback thread stop semaphore wait returned error %d"

```

>  `com.apple.kernel`

```diff

-11215.80.25.502.1
+11215.80.28.502.2
   __TEXT.__const: 0x34280
   __TEXT.__copyio_vectors: 0xf0
-  __TEXT.__cstring: 0x72e0b
+  __TEXT.__cstring: 0x731a5
   __TEXT.__os_log: 0x276f6
   __TEXT.__eh_frame: 0x610
   __DATA_CONST.__auth_ptr: 0x8

   __DATA_CONST.__brk_desc: 0x78
   __DATA_SPTM.__const: 0x3c000
   __TEXT_EXEC.__hib_text: 0xc68
-  __TEXT_EXEC.__text: 0x7f324c
+  __TEXT_EXEC.__text: 0x7f39bc
   __TEXT_BOOT_EXEC.__bootcode: 0x4cd8
   __KLD.__text: 0x1644
   __LASTDATA_CONST.__mod_init_func: 0x8
   __LAST.__pinst: 0x8
   __LAST.__last: 0x0
   __KLDDATA.__cstring: 0x6e1
-  __KLDDATA.__const: 0x25c0
+  __KLDDATA.__const: 0x25f0
   __KLDDATA.__mod_init_func: 0x8
   __KLDDATA.__mod_term_func: 0x8
   __KLDDATA.__bss: 0x1
   __DATA.__data: 0x18441
   __DATA.__lock_grp: 0x5908
   __DATA.__percpu: 0x6e30
-  __DATA.__common: 0x586e0
+  __DATA.__common: 0x58730
   __DATA.__bss: 0x95748
   __BOOTDATA.__data: 0x18000
-  __BOOTDATA.__init_entry_set: 0x10c20
+  __BOOTDATA.__init_entry_set: 0x10c38
   __BOOTDATA.__init: 0x5b138
   __PRELINK_TEXT.__text: 0x0
   __PRELINK_INFO.__info: 0x0

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x45b4f
-  Functions: 20495
+  Functions: 20496
   Symbols:   0
-  CStrings:  17259
+  CStrings:  17285
 
CStrings:
+ "%s out of range bind ordinal %u (max %u) @%s:%d"
+ "%s(): Invalid ptr auth key %d @%s:%d"
+ "%s(): No segment for user VA 0x%llx @%s:%d"
+ "%s(): Range not found for offset 0x%llx @%s:%d"
+ "%s(): chain 0x%llx out of range 0x%llx..0x%llx @%s:%d"
+ "%s(): dyld pager slide error %d at 0x%llx @%s:%d"
+ "%s(): out of range bind ordinal %u (max %u) @%s:%d"
+ "%s(): out of range segInfo->page_start[overflowIndex] @%s:%d"
+ "%s(): out of range segInfo->page_start[pageIndex] @%s:%d"
+ "%s(): seg->page_count out of bounds @%s:%d"
+ "%s(): seg->page_count too small @%s:%d"
+ "%s(): seg->size out of bounds @%s:%d"
+ "%s(): seg->size too small @%s:%d"
+ "%s(): seg_info out of bounds @%s:%d"
+ "%s(): shared region slide error %d @%s:%d"
+ "%s(): unknown pointer_format %d @%s:%d"
+ "%s(): upl_request(%p, 0x%llx, 0x%llx) ret %d @%s:%d"
+ "dyld_pager_data_request"
+ "fixupCachePageAuth64"
+ "fixupChain32"
+ "fixupPage32"
+ "fixupPage64"
+ "fixupPageAuth64"
+ "fixup_page"
+ "shared_region_pager_data_request"
+ "signPointer"

```

>  `com.apple.security.sandbox`

```diff

-2401.80.8.0.1
-  __TEXT.__const: 0x18fd71
+2401.80.11.0.0
+  __TEXT.__const: 0x1904f1
   __TEXT.__cstring: 0x70ba
   __TEXT.__os_log: 0x2058
   __TEXT_EXEC.__text: 0x30ff8

```

</details>

## MachO

### ❌ Removed (1)

- `/Applications/Tamale.app/PlugIns/TamaleWidgetExtension.appex/TamaleWidgetExtension`

### ⬆️ Updated (415)

<details>
  <summary><i>View Updated</i></summary>

- [/Applications/AccessorySetupUI.app/AccessorySetupUI](MACHOS/AccessorySetupUI.md)
- [/Applications/AirDropUI.app/AirDropUI](MACHOS/AirDropUI.md)
- [/Applications/BusinessExtensionsWrapper.app/PlugIns/Business.appex/Business](MACHOS/Business.md)
- [/Applications/CarCamera.app/CarCamera](MACHOS/CarCamera.md)
- [/Applications/Charge.app/Charge](MACHOS/Charge.md)
- [/Applications/ClarityCamera.app/ClarityCamera](MACHOS/ClarityCamera.md)
- [/Applications/Climate.app/Climate](MACHOS/Climate.md)
- [/Applications/ClockAngel.app/ClockAngel](MACHOS/ClockAngel.md)
- [/Applications/Closures.app/Closures](MACHOS/Closures.md)
- [/Applications/ColorPickerUIService.app/ColorPickerUIService](MACHOS/ColorPickerUIService.md)
- [/Applications/CoreAuthUI.app/CoreAuthUI](MACHOS/CoreAuthUI.md)
- [/Applications/Diagnostics.app/Diagnostics](MACHOS/Diagnostics.md)
- [/Applications/EventViewService.app/EventViewService](MACHOS/EventViewService.md)
- [/Applications/FTMInternal-4.app/FTMInternal-4](MACHOS/FTMInternal-4.md)
- [/Applications/Family.app/PlugIns/InviteMessageBubbleExtension.appex/InviteMessageBubbleExtension](MACHOS/InviteMessageBubbleExtension.md)
- [/Applications/FontPickerUIService.app/FontPickerUIService](MACHOS/FontPickerUIService.md)
- [/Applications/GameCenterUIService.app/PlugIns/GameCenterMessageExtension.appex/GameCenterMessageExtension](MACHOS/GameCenterMessageExtension.md)
- [/Applications/GameCenterWidgets.app/PlugIns/GCWidgets.appex/GCWidgets](MACHOS/GCWidgets.md)
- [/Applications/GameOverlayUI.app/GameOverlayUI](MACHOS/GameOverlayUI.md)
- [/Applications/HDSViewService.app/HDSViewService](MACHOS/HDSViewService.md)
- [/Applications/HeadphoneProxService.app/HeadphoneProxService](MACHOS/HeadphoneProxService.md)
- [/Applications/HomeCaptiveViewService.app/HomeCaptiveViewService](MACHOS/HomeCaptiveViewService.md)
- [/Applications/InCallService.app/InCallService](MACHOS/InCallService.md)
- [/Applications/InCallService.app/PlugIns/IntentsUI.appex/IntentsUI](MACHOS/IntentsUI.md)
- [/Applications/MTLReplayer.app/Frameworks/MTLReplayController.framework/MTLReplayController](MACHOS/MTLReplayController.md)
- [/Applications/MTLReplayer.app/MTLReplayer](MACHOS/MTLReplayer.md)
- [/Applications/MagnifierAngel.app/MagnifierAngel](MACHOS/MagnifierAngel.md)
- [/Applications/Media.app/Media](MACHOS/Media.md)
- [/Applications/MediaRemoteUI.app/MediaRemoteUI](MACHOS/MediaRemoteUI.md)
- [/Applications/MobilePhone.app/MobilePhone](MACHOS/MobilePhone.md)
- [/Applications/MobilePhone.app/PlugIns/VoicemailMessageNotificationExtension.appex/VoicemailMessageNotificationExtension](MACHOS/VoicemailMessageNotificationExtension.md)
- [/Applications/MomentsUIService.app/MomentsUIService](MACHOS/MomentsUIService.md)
- [/Applications/MusicRecognition.app/MusicRecognition](MACHOS/MusicRecognition.md)
- [/Applications/PCViewService.app/PCViewService](MACHOS/PCViewService.md)
- [/Applications/PeopleMessageService.app/PlugIns/PeopleMessagesScreenTime.appex/PeopleMessagesScreenTime](MACHOS/PeopleMessagesScreenTime.md)
- [/Applications/PosterBoard.app/XPCServices/PosterPlatformSupportBundleService.xpc/PosterPlatformSupportBundleService](MACHOS/PosterPlatformSupportBundleService.md)
- [/Applications/Preferences.app/Preferences](MACHOS/Preferences.md)
- [/Applications/PreviewShell.app/PreviewShell](MACHOS/PreviewShell.md)
- [/Applications/SOSBuddy.app/SOSBuddy](MACHOS/SOSBuddy.md)
- [/Applications/Screen Time.app/PlugIns/ScreenTimeWidgetExtension.appex/ScreenTimeWidgetExtension](MACHOS/ScreenTimeWidgetExtension.md)
- [/Applications/Setup.app/Setup](MACHOS/Setup.md)
- [/Applications/SharingViewService.app/SharingViewService](MACHOS/SharingViewService.md)
- [/Applications/ShazamEventsApp.app/ShazamEventsApp](MACHOS/ShazamEventsApp.md)
- [/Applications/Sidecar.app/PlugIns/ContinuityDisplay.appex/ContinuityDisplay](MACHOS/ContinuityDisplay.md)
- [/Applications/Sidecar.app/Sidecar](MACHOS/Sidecar.md)
- [/Applications/Siri.app/PlugIns/TypeToSiriWidgetExtension.appex/TypeToSiriWidgetExtension](MACHOS/TypeToSiriWidgetExtension.md)
- [/Applications/Siri.app/Siri](MACHOS/Siri.md)
- [/Applications/SoftwareUpdateUIService.app/SoftwareUpdateUIService](MACHOS/SoftwareUpdateUIService.md)
- [/Applications/StickersUltra.app/PlugIns/StickersUltraExtension.appex/StickersUltraExtension](MACHOS/StickersUltraExtension.md)
- [/Applications/TDGSharingViewService.app/TDGSharingViewService](MACHOS/TDGSharingViewService.md)
- [/Applications/Tamale.app/Tamale](MACHOS/Tamale.md)
- [/Applications/Trip.app/Trip](MACHOS/Trip.md)
- [/Applications/Vehicle.app/Vehicle](MACHOS/Vehicle.md)
- [/Applications/WritingToolsUIService.app/WritingToolsUIService](MACHOS/WritingToolsUIService.md)
- [/Library/Audio/Plug-Ins/HAL/VirtualAudio.plugin/VirtualAudio](MACHOS/VirtualAudio.md)
- [/System/Applications/Family/InviteMessageBubbleExtension.appex/InviteMessageBubbleExtension](MACHOS/InviteMessageBubbleExtension.md)
- [/System/DriverKit/usr/lib/system/libsystem_platform_debug.dylib](MACHOS/libsystem_platform_debug.dylib.md)
- [/System/ExclaveKit/System/Library/Frameworks/Foundation.framework/Foundation](MACHOS/Foundation.md)
- [/System/ExclaveKit/System/Library/Frameworks/MobileAssetExclaveComponent.framework/MobileAssetExclaveComponent](MACHOS/MobileAssetExclaveComponent.md)
- [/System/ExclaveKit/System/Library/Frameworks/SoundAnalysis.framework/SoundAnalysis](MACHOS/SoundAnalysis.md)
- [/System/ExclaveKit/System/Library/Frameworks/T8140_IR_ISP_EK_Component.framework/T8140_IR_ISP_EK_Component](MACHOS/T8140_IR_ISP_EK_Component.md)
- [/System/ExclaveKit/System/Library/Frameworks/Vision.framework/Vision](MACHOS/Vision.md)
- [/System/ExclaveKit/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore](MACHOS/AudioToolboxCore.md)
- [/System/ExclaveKit/System/Library/PrivateFrameworks/CollectionsInternal.framework/CollectionsInternal](MACHOS/CollectionsInternal.md)
- [/System/ExclaveKit/System/Library/PrivateFrameworks/CoreSpeechExclaveComponent.framework/CoreSpeechExclaveComponent](MACHOS/CoreSpeechExclaveComponent.md)
- [/System/ExclaveKit/System/Library/PrivateFrameworks/Espresso.framework/Espresso](MACHOS/Espresso.md)
- [/System/ExclaveKit/System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam](MACHOS/Tightbeam.md)
- [/System/ExclaveKit/usr/lib/dyld](MACHOS/dyld.md)
- [/System/ExclaveKit/usr/lib/swift/libswiftos.dylib](MACHOS/libswiftos.dylib.md)
- [/System/Library/AccessibilityBundles/LiveSpeechUIService.axuiservice/LiveSpeechUIService](MACHOS/LiveSpeechUIService.md)
- [/System/Library/AccessibilityBundles/ZoomWindow.axuiservice/ZoomWindow](MACHOS/ZoomWindow.md)
- [/System/Library/Accounts/DataclassOwners/FreeformDataclassOwner.bundle/FreeformDataclassOwner](MACHOS/FreeformDataclassOwner.md)
- [/System/Library/Accounts/ServiceOwners/AMSMediaServiceOwner.bundle/AMSMediaServiceOwner](MACHOS/AMSMediaServiceOwner.md)
- [/System/Library/AppleMediaServices/DynamicUI/PlugIns/CoreDynamicUIPlugin.bundle/CoreDynamicUIPlugin](MACHOS/CoreDynamicUIPlugin.md)
- [/System/Library/AppleMediaServices/DynamicUI/PlugIns/StoreDynamicUIPlugin.bundle/StoreDynamicUIPlugin](MACHOS/StoreDynamicUIPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/AudioFlowDelegatePlugin](MACHOS/AudioFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/CarCommandsFlowDelegatePlugin.bundle/CarCommandsFlowDelegatePlugin](MACHOS/CarCommandsFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/DailyBriefingFlowPlugin.bundle/DailyBriefingFlowPlugin](MACHOS/DailyBriefingFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/EmergencyFlowPlugin.bundle/EmergencyFlowPlugin](MACHOS/EmergencyFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/HealthFlowDelegatePlugin.bundle/HealthFlowDelegatePlugin](MACHOS/HealthFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/HomeCommunicationFlowDelegatePlugin.bundle/HomeCommunicationFlowDelegatePlugin](MACHOS/HomeCommunicationFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/IFFlowPlugin](MACHOS/IFFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/PhoneCallFlowDelegatePlugin](MACHOS/PhoneCallFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/SocialConversationFlowDelegatePlugin](MACHOS/SocialConversationFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/WellnessFlowPlugin](MACHOS/WellnessFlowPlugin.md)
- [/System/Library/Assistant/Plugins/Maps.assistantBundle/Maps](MACHOS/Maps.md)
- [/System/Library/Assistant/Plugins/PreferencesAssistant.assistantBundle/PreferencesAssistant](MACHOS/PreferencesAssistant.md)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriPrivateLearningPatternExtractionPlugin.bundle/SiriPrivateLearningPatternExtractionPlugin](MACHOS/SiriPrivateLearningPatternExtractionPlugin.md)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriPrivateLearningTTSMispronunciationPlugin.bundle/SiriPrivateLearningTTSMispronunciationPlugin](MACHOS/SiriPrivateLearningTTSMispronunciationPlugin.md)
- [/System/Library/Assistant/UIPlugins/Maps.siriUIBundle/Maps](MACHOS/Maps.md)
- [/System/Library/Audio/Plug-Ins/RemoteInput/JarvisPlugin.bundle/JarvisPlugin](MACHOS/JarvisPlugin.md)
- [/System/Library/CoreImage/PortraitFilters.cifilter/portrait_filters_fullsize_archive_bin.metallib](MACHOS/portrait_filters_fullsize_archive_bin.metallib.md)
- [/System/Library/CoreServices/ClarityBoard.app/ClarityBoard](MACHOS/ClarityBoard.md)
- [/System/Library/CoreServices/IntelligentLight.app/IntelligentLight](MACHOS/IntelligentLight.md)
- [/System/Library/CoreServices/osanalyticshelper](MACHOS/osanalyticshelper.md)
- [/System/Library/CoreServices/powerd.bundle/powerd](MACHOS/powerd.md)
- [/System/Library/DataClassMigrators/MobileAsset.migrator/MobileAsset](MACHOS/MobileAsset.md)
- [/System/Library/DataClassMigrators/PreferencesMigrator.migrator/PreferencesMigrator](MACHOS/PreferencesMigrator.md)
- [/System/Library/DigitalSeparation/SharingSources/FindMyPeopleDigitalSeparation.bundle/FindMyPeopleDigitalSeparation](MACHOS/FindMyPeopleDigitalSeparation.md)
- [/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN](MACHOS/com.apple.DriverKit-AppleBCMWLAN.md)
- [/System/Library/ExtensionKit/Extensions/AirDropSettingsIntents.appex/AirDropSettingsIntents](MACHOS/AirDropSettingsIntents.md)
- [/System/Library/ExtensionKit/Extensions/AppleAccountIntents.appex/AppleAccountIntents](MACHOS/AppleAccountIntents.md)
- [/System/Library/ExtensionKit/Extensions/AssistantSettingsControlsExtension.appex/AssistantSettingsControlsExtension](MACHOS/AssistantSettingsControlsExtension.md)
- [/System/Library/ExtensionKit/Extensions/DocumentAppIntents.appex/DocumentAppIntents](MACHOS/DocumentAppIntents.md)
- [/System/Library/ExtensionKit/Extensions/EventKitUIRemoteUIExtension.appex/EventKitUIRemoteUIExtension](MACHOS/EventKitUIRemoteUIExtension.md)
- [/System/Library/ExtensionKit/Extensions/FamilyIntents.appex/FamilyIntents](MACHOS/FamilyIntents.md)
- [/System/Library/ExtensionKit/Extensions/GeneralSettingsIntents.appex/GeneralSettingsIntents](MACHOS/GeneralSettingsIntents.md)
- [/System/Library/ExtensionKit/Extensions/GenerativeAssistantExtension.appex/GenerativeAssistantExtension](MACHOS/GenerativeAssistantExtension.md)
- [/System/Library/ExtensionKit/Extensions/MercuryPosterExtension.appex/MercuryPosterExtension](MACHOS/MercuryPosterExtension.md)
- [/System/Library/ExtensionKit/Extensions/MessagesSettingsWidgetKitExtension.appex/MessagesSettingsWidgetKitExtension](MACHOS/MessagesSettingsWidgetKitExtension.md)
- [/System/Library/ExtensionKit/Extensions/MusicEngagementExtension.appex/MusicEngagementExtension](MACHOS/MusicEngagementExtension.md)
- [/System/Library/ExtensionKit/Extensions/OfficeThumbnailExtension.appex/OfficeThumbnailExtension](MACHOS/OfficeThumbnailExtension.md)
- [/System/Library/ExtensionKit/Extensions/PridePosterExtension.appex/PridePosterExtension](MACHOS/PridePosterExtension.md)
- [/System/Library/ExtensionKit/Extensions/PrivateEvolutionPlugin.appex/PrivateEvolutionPlugin](MACHOS/PrivateEvolutionPlugin.md)
- [/System/Library/ExtensionKit/Extensions/ProductPageExtension.appex/ProductPageExtension](MACHOS/ProductPageExtension.md)
- [/System/Library/ExtensionKit/Extensions/SafariAssistantWorker.appex/SafariAssistantWorker](MACHOS/SafariAssistantWorker.md)
- [/System/Library/ExtensionKit/Extensions/ScreenTimeAppIntentsExtension.appex/ScreenTimeAppIntentsExtension](MACHOS/ScreenTimeAppIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/SubscribePageExtension.appex/SubscribePageExtension](MACHOS/SubscribePageExtension.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.fskit.msdos.appex/com.apple.fskit.msdos](MACHOS/com.apple.fskit.msdos.md)
- [/System/Library/Extensions/AppleH15MCD.kext/AppleH15MCD](MACHOS/AppleH15MCD.md)
- [/System/Library/Frameworks/AutomatedDeviceEnrollment.framework/PlugIns/AddDevicesToAutomatedDeviceEnrollmentExtension.appex/AddDevicesToAutomatedDeviceEnrollmentExtension](MACHOS/AddDevicesToAutomatedDeviceEnrollmentExtension.md)
- [/System/Library/Frameworks/CoreLocation.framework/PlugIns/CoreLocationMapLNPromptPlugin.appex/CoreLocationMapLNPromptPlugin](MACHOS/CoreLocationMapLNPromptPlugin.md)
- [/System/Library/Frameworks/CoreLocation.framework/PlugIns/CoreLocationNumberedMapCalloutPromptPlugin.appex/CoreLocationNumberedMapCalloutPromptPlugin](MACHOS/CoreLocationNumberedMapCalloutPromptPlugin.md)
- [/System/Library/Frameworks/CoreLocation.framework/PlugIns/CoreLocationRepromptAlwaysAuthPromptPlugin.appex/CoreLocationRepromptAlwaysAuthPromptPlugin](MACHOS/CoreLocationRepromptAlwaysAuthPromptPlugin.md)
- [/System/Library/Frameworks/CoreLocationUI.framework/XPCServices/com.apple.corelocation.locationUI.xpc/com.apple.corelocation.locationUI](MACHOS/com.apple.corelocation.locationUI.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenterMobileHelper](MACHOS/CommCenterMobileHelper.md)
- [/System/Library/Frameworks/FamilyControls.framework/FamilyControlsAgent](MACHOS/FamilyControlsAgent.md)
- [/System/Library/Frameworks/FileProvider.framework/PlugIns/LocalStorageFileProvider.appex/LocalStorageFileProvider](MACHOS/LocalStorageFileProvider.md)
- [/System/Library/Frameworks/ManagedSettings.framework/ManagedSettingsAgent](MACHOS/ManagedSettingsAgent.md)
- [/System/Library/Frameworks/Security.framework/XPCServices/TrustedPeersHelper.xpc/TrustedPeersHelper](MACHOS/TrustedPeersHelper.md)
- [/System/Library/Frameworks/StoreKit.framework/Support/storekitd](MACHOS/storekitd.md)
- [/System/Library/Frameworks/SystemConfiguration.framework/SCHelper](MACHOS/SCHelper.md)
- [/System/Library/Frameworks/UIKit.framework/PlugIns/com.apple.UIKit.ColorPicker.appex/com.apple.UIKit.ColorPicker](MACHOS/com.apple.UIKit.ColorPicker.md)
- [/System/Library/Frameworks/UIKit.framework/PlugIns/com.apple.UIKit.screenpicker.appex/com.apple.UIKit.screenpicker](MACHOS/com.apple.UIKit.screenpicker.md)
- [/System/Library/Frameworks/_DeviceActivity_SwiftUI.framework/PlugIns/DeviceActivityReportService.appex/DeviceActivityReportService](MACHOS/DeviceActivityReportService.md)
- [/System/Library/HIDPlugins/ServicePlugins/GenericGamepadHIDServicePlugin.plugin/GenericGamepadHIDServicePlugin](MACHOS/GenericGamepadHIDServicePlugin.md)
- [/System/Library/LocationBundles/AltimeterHarvest.bundle/AltimeterHarvest](MACHOS/AltimeterHarvest.md)
- [/System/Library/LocationBundles/AppGenius.bundle/AppGenius](MACHOS/AppGenius.md)
- [/System/Library/LocationBundles/CompassCalibration.bundle/CompassCalibration](MACHOS/CompassCalibration.md)
- [/System/Library/LocationBundles/IonosphereHarvest.bundle/IonosphereHarvest](MACHOS/IonosphereHarvest.md)
- [/System/Library/LocationBundles/LocationFenceSync.bundle/LocationFenceSync](MACHOS/LocationFenceSync.md)
- [/System/Library/LocationBundles/LocationPromptUI.bundle/LocationPromptUI](MACHOS/LocationPromptUI.md)
- [/System/Library/LocationBundles/MotionCalibration.bundle/MotionCalibration](MACHOS/MotionCalibration.md)
- [/System/Library/LocationBundles/PLAMonitor.bundle/PLAMonitor](MACHOS/PLAMonitor.md)
- [/System/Library/LocationBundles/SystemCustomization.bundle/SystemCustomization](MACHOS/SystemCustomization.md)
- [/System/Library/LocationBundles/TimeZone.bundle/TimeZone](MACHOS/TimeZone.md)
- [/System/Library/Messages/PlugIns/SatelliteSMS.imservice/SatelliteSMS](MACHOS/SatelliteSMS.md)
- [/System/Library/Messages/iMessageBalloons/ASMessagesProvider.bundle/ASMessagesProvider](MACHOS/ASMessagesProvider.md)
- [/System/Library/NanoPreferenceBundles/General/CompanionAutoLaunchSettings.bundle/CompanionAutoLaunchSettings](MACHOS/CompanionAutoLaunchSettings.md)
- [/System/Library/NanoPreferenceBundles/General/CompanionInternationalSettings.bundle/CompanionInternationalSettings](MACHOS/CompanionInternationalSettings.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/ActivityBridgeSetup.bundle/ActivityBridgeSetup](MACHOS/ActivityBridgeSetup.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/HealthFeaturesBridgeSetupPlugin.bundle/HealthFeaturesBridgeSetupPlugin](MACHOS/HealthFeaturesBridgeSetupPlugin.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/WGAEltonPhoneBuddyFlowPanel.bundle/WGAEltonPhoneBuddyFlowPanel](MACHOS/WGAEltonPhoneBuddyFlowPanel.md)
- [/System/Library/PreferenceBundles/AccountSettings/CloudKitSettings.bundle/CloudKitSettings](MACHOS/CloudKitSettings.md)
- [/System/Library/PreferenceBundles/AccountSettings/icloudMailSettings.bundle/icloudMailSettings](MACHOS/icloudMailSettings.md)
- [/System/Library/PreferenceBundles/AirDropSettings.bundle/AirDropSettings](MACHOS/AirDropSettings.md)
- [/System/Library/PreferenceBundles/DefaultAppsSettingsUIPlugin.bundle/DefaultAppsSettingsUIPlugin](MACHOS/DefaultAppsSettingsUIPlugin.md)
- [/System/Library/PreferenceBundles/HearingSettings.bundle/HearingSettings](MACHOS/HearingSettings.md)
- [/System/Library/PreferenceBundles/InternationalSettings.bundle/InternationalSettings](MACHOS/InternationalSettings.md)
- [/System/Library/PreferenceBundles/JournalSettings.bundle/JournalSettings](MACHOS/JournalSettings.md)
- [/System/Library/PreferenceBundles/MapsSettings.bundle/MapsSettings](MACHOS/MapsSettings.md)
- [/System/Library/PreferenceBundles/MeasureSettings.bundle/MeasureSettings](MACHOS/MeasureSettings.md)
- [/System/Library/PreferenceBundles/MobileSafariSettings.bundle/MobileSafariSettings](MACHOS/MobileSafariSettings.md)
- [/System/Library/PreferenceBundles/MultitaskingAndGesturesSettings.bundle/MultitaskingAndGesturesSettings](MACHOS/MultitaskingAndGesturesSettings.md)
- [/System/Library/PreferenceBundles/PrivacyAndSecuritySettings.bundle/PrivacyAndSecuritySettings](MACHOS/PrivacyAndSecuritySettings.md)
- [/System/Library/PreferenceBundles/StorageSettingsUI.bundle/StorageSettingsUI](MACHOS/StorageSettingsUI.md)
- [/System/Library/PreferenceBundles/VoiceControlSettings.bundle/VoiceControlSettings](MACHOS/VoiceControlSettings.md)
- [/System/Library/PreferenceBundles/WallpaperSettings.bundle/WallpaperSettings](MACHOS/WallpaperSettings.md)
- [/System/Library/PreferencesSyncBundles/CoreLocationSync.bundle/CoreLocationSync](MACHOS/CoreLocationSync.md)
- [/System/Library/PrivateFrameworks/ABMHelper.framework/Support/abm-helper](MACHOS/abm-helper.md)
- [/System/Library/PrivateFrameworks/ASOctaneSupport.framework/XPCServices/ASOctaneSupportXPCService.xpc/ASOctaneSupportXPCService](MACHOS/ASOctaneSupportXPCService.md)
- [/System/Library/PrivateFrameworks/AppSSO.framework/Support/AppSSODaemon](MACHOS/AppSSODaemon.md)
- [/System/Library/PrivateFrameworks/AppStoreComponents.framework/Support/appstorecomponentsd](MACHOS/appstorecomponentsd.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored](MACHOS/appstored.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/amsaccountsd](MACHOS/amsaccountsd.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/Extensions/UtilityExtension.appex/UtilityExtension](MACHOS/UtilityExtension.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/amsengagementd](MACHOS/amsengagementd.md)
- [/System/Library/PrivateFrameworks/BookDataStore.framework/Support/bookdatastored](MACHOS/bookdatastored.md)
- [/System/Library/PrivateFrameworks/BusinessChatService.framework/businessservicesd](MACHOS/businessservicesd.md)
- [/System/Library/PrivateFrameworks/CallHistory.framework/Support/CallHistorySyncHelper](MACHOS/CallHistorySyncHelper.md)
- [/System/Library/PrivateFrameworks/ClassroomKit.framework/XPCServices/BooksService.xpc/BooksService](MACHOS/BooksService.md)
- [/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.MobileDocumentsFileProvider.appex/com.apple.CloudDocs.MobileDocumentsFileProvider](MACHOS/com.apple.CloudDocs.MobileDocumentsFileProvider.md)
- [/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.MobileDocumentsFileProviderManaged.appex/com.apple.CloudDocs.MobileDocumentsFileProviderManaged](MACHOS/com.apple.CloudDocs.MobileDocumentsFileProviderManaged.md)
- [/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.MobileDocumentsFileProviderUI.appex/com.apple.CloudDocs.MobileDocumentsFileProviderUI](MACHOS/com.apple.CloudDocs.MobileDocumentsFileProviderUI.md)
- [/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.iCloudDriveFileProvider.appex/com.apple.CloudDocs.iCloudDriveFileProvider](MACHOS/com.apple.CloudDocs.iCloudDriveFileProvider.md)
- [/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.iCloudDriveFileProviderManaged.appex/com.apple.CloudDocs.iCloudDriveFileProviderManaged](MACHOS/com.apple.CloudDocs.iCloudDriveFileProviderManaged.md)
- [/System/Library/PrivateFrameworks/CloudKitDaemon.framework/Support/ckdiscretionaryd](MACHOS/ckdiscretionaryd.md)
- [/System/Library/PrivateFrameworks/CloudSharing.framework/XPCServices/SPIHelper-iOS.xpc/SPIHelper-iOS](MACHOS/SPIHelper-iOS.md)
- [/System/Library/PrivateFrameworks/CloudSharingUI.framework/PlugIns/com.apple.CloudSharingUI.CloudSharing.appex/com.apple.CloudSharingUI.CloudSharing](MACHOS/com.apple.CloudSharingUI.CloudSharing.md)
- [/System/Library/PrivateFrameworks/CloudTelemetry.framework/XPCServices/CloudTelemetryService.xpc/CloudTelemetryService](MACHOS/CloudTelemetryService.md)
- [/System/Library/PrivateFrameworks/CoreAccessories.framework/Support/accessoryd](MACHOS/accessoryd.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/parsecd](MACHOS/parsecd.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/LocationDiagnosticExtension.appex/LocationDiagnosticExtension](MACHOS/LocationDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.B389.appex/com.apple.DiagnosticExtensions.B389](MACHOS/com.apple.DiagnosticExtensions.B389.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Cellular.appex/com.apple.DiagnosticExtensions.Cellular](MACHOS/com.apple.DiagnosticExtensions.Cellular.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Microstackshot.appex/com.apple.DiagnosticExtensions.Microstackshot](MACHOS/com.apple.DiagnosticExtensions.Microstackshot.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Telephony.appex/com.apple.DiagnosticExtensions.Telephony](MACHOS/com.apple.DiagnosticExtensions.Telephony.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAppPopover.appex/RecentsAppPopover](MACHOS/RecentsAppPopover.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAvocado.appex/RecentsAvocado](MACHOS/RecentsAvocado.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAvocadoIntentHandler.appex/RecentsAvocadoIntentHandler](MACHOS/RecentsAvocadoIntentHandler.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/SaveToFiles.appex/SaveToFiles](MACHOS/SaveToFiles.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/com.apple.DocumentManager.Service.appex/com.apple.DocumentManager.Service](MACHOS/com.apple.DocumentManager.Service.md)
- [/System/Library/PrivateFrameworks/DocumentUnderstanding.framework/Support/textunderstandingd](MACHOS/textunderstandingd.md)
- [/System/Library/PrivateFrameworks/EmailDaemon.framework/maild](MACHOS/maild.md)
- [/System/Library/PrivateFrameworks/FamilyCircle.framework/familycircled](MACHOS/familycircled.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/Resources/UITypographyPanel.bundle/UITypographyPanel](MACHOS/UITypographyPanel.md)
- [/System/Library/PrivateFrameworks/GPUToolsCapture.framework/GPUToolsCapture](MACHOS/GPUToolsCapture.md)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/PlugIns/GameCenterMatchmakerExtension.appex/GameCenterMatchmakerExtension](MACHOS/GameCenterMatchmakerExtension.md)
- [/System/Library/PrivateFrameworks/HomePlatformSettingsUI.framework/PlugIns/HPSUIViewService.appex/HPSUIViewService](MACHOS/HPSUIViewService.md)
- [/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd](MACHOS/identityservicesd.md)
- [/System/Library/PrivateFrameworks/MLKit.framework/PlugIns/com.apple.MLKit.MLModelPreview.appex/com.apple.MLKit.MLModelPreview](MACHOS/com.apple.MLKit.MLModelPreview.md)
- [/System/Library/PrivateFrameworks/MLKit.framework/PlugIns/com.apple.MLKit.MLPackagePreview.appex/com.apple.MLKit.MLPackagePreview](MACHOS/com.apple.MLKit.MLPackagePreview.md)
- [/System/Library/PrivateFrameworks/MapsSuggestions.framework/destinationd](MACHOS/destinationd.md)
- [/System/Library/PrivateFrameworks/MapsSupport.framework/navd](MACHOS/navd.md)
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd](MACHOS/mediaanalysisd.md)
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd-service](MACHOS/mediaanalysisd-service.md)
- [/System/Library/PrivateFrameworks/MediaRemote.framework/Support/mediaremoted](MACHOS/mediaremoted.md)
- [/System/Library/PrivateFrameworks/MediaServicesBroker.framework/PlugIns/MediaSetupViewService.appex/MediaSetupViewService](MACHOS/MediaSetupViewService.md)
- [/System/Library/PrivateFrameworks/Message.framework/XPCServices/SearchIndexer.xpc/SearchIndexer](MACHOS/SearchIndexer.md)
- [/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/XPCServices/MessagesBlastDoorService.xpc/MessagesBlastDoorService](MACHOS/MessagesBlastDoorService.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/Support/accessoryupdaterd](MACHOS/accessoryupdaterd.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/Accessory Updater Service.xpc/Accessory Updater Service](MACHOS/Accessory_Updater_Service.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceDFU.xpc/UARPUpdaterServiceDFU](MACHOS/UARPUpdaterServiceDFU.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceHID.xpc/UARPUpdaterServiceHID](MACHOS/UARPUpdaterServiceHID.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceLegacyAudio.xpc/UARPUpdaterServiceLegacyAudio](MACHOS/UARPUpdaterServiceLegacyAudio.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceUSBPD.xpc/UARPUpdaterServiceUSBPD](MACHOS/UARPUpdaterServiceUSBPD.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/USBCAccessoryUpdaterService.xpc/USBCAccessoryUpdaterService](MACHOS/USBCAccessoryUpdaterService.md)
- [/System/Library/PrivateFrameworks/MobileAsset.framework/XPCServices/ManifestStorageService.xpc/ManifestStorageService](MACHOS/ManifestStorageService.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/backupd](MACHOS/backupd.md)
- [/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/Support/softwareupdated](MACHOS/softwareupdated.md)
- [/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/XPCServices/com.apple.MobileSoftwareUpdate.CleanupPreparePathService.xpc/com.apple.MobileSoftwareUpdate.CleanupPreparePathService](MACHOS/com.apple.MobileSoftwareUpdate.CleanupPreparePathService.md)
- [/System/Library/PrivateFrameworks/NeighborhoodActivityConduit.framework/XPCServices/com.apple.NeighborhoodActivityConduitService.xpc/com.apple.NeighborhoodActivityConduitService](MACHOS/com.apple.NeighborhoodActivityConduitService.md)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/passd](MACHOS/passd.md)
- [/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PlugIns/AmbientPhotoFramePosterProvider.appex/AmbientPhotoFramePosterProvider](MACHOS/AmbientPhotoFramePosterProvider.md)
- [/System/Library/PrivateFrameworks/PowerLog.framework/XPCServices/PerfPowerTelemetryClientRegistrationService.xpc/PerfPowerTelemetryClientRegistrationService](MACHOS/PerfPowerTelemetryClientRegistrationService.md)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/PlugIns/DEPowerlogEPL.appex/DEPowerlogEPL](MACHOS/DEPowerlogEPL.md)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/PlugIns/com.apple.PowerlogCore.diagnosticextension.appex/com.apple.PowerlogCore.diagnosticextension](MACHOS/com.apple.PowerlogCore.diagnosticextension.md)
- [/System/Library/PrivateFrameworks/PreviewsOSSupport.framework/Support/previewsd](MACHOS/previewsd.md)
- [/System/Library/PrivateFrameworks/PrivateCloudCompute.framework/privatecloudcomputed.app/privatecloudcomputed](MACHOS/privatecloudcomputed.md)
- [/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeAgent](MACHOS/ScreenTimeAgent.md)
- [/System/Library/PrivateFrameworks/SiriAppLaunchIntents.framework/PlugIns/AppLaunchIntentExtension.appex/AppLaunchIntentExtension](MACHOS/AppLaunchIntentExtension.md)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningAnalytics.framework/PlugIns/SiriUserFeedbackLearningUniversalSuggestionsPlugin.appex/SiriUserFeedbackLearningUniversalSuggestionsPlugin](MACHOS/SiriUserFeedbackLearningUniversalSuggestionsPlugin.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/PlugIns/SUSFollowUpExtension.appex/SUSFollowUpExtension](MACHOS/SUSFollowUpExtension.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateServicesUI.framework/Plugins/SoftwareUpdateServicesUIPlugin.servicebundle/SoftwareUpdateServicesUIPlugin](MACHOS/SoftwareUpdateServicesUIPlugin.md)
- [/System/Library/PrivateFrameworks/SpaceAttribution.framework/spaceattributiond](MACHOS/spaceattributiond.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/XPCServices/com.apple.FTLivePhotoService.xpc/com.apple.FTLivePhotoService](MACHOS/com.apple.FTLivePhotoService.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd](MACHOS/callservicesd.md)
- [/System/Library/PrivateFrameworks/TranslationUIServices.framework/PlugIns/TranslationUIService.appex/TranslationUIService](MACHOS/TranslationUIService.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/CarPlayArtwork.bundle/CarPlayArtwork](MACHOS/CarPlayArtwork.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/TextEffectsCatalog.bundle/TextEffectsCatalog](MACHOS/TextEffectsCatalog.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/XPCServices/SecureControlService.xpc/SecureControlService](MACHOS/SecureControlService.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/XPCServices/com.apple.UIKit.KeyboardManagement.xpc/com.apple.UIKit.KeyboardManagement](MACHOS/com.apple.UIKit.KeyboardManagement.md)
- [/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTrackingAgent](MACHOS/UsageTrackingAgent.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/ExtragalacticPoster.appex/ExtragalacticPoster](MACHOS/ExtragalacticPoster.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/KaleidoscopePoster.appex/KaleidoscopePoster](MACHOS/KaleidoscopePoster.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/RhizomePoster.appex/RhizomePoster](MACHOS/RhizomePoster.md)
- [/System/Library/PrivateFrameworks/WeatherDaemon.framework/weatherd](MACHOS/weatherd.md)
- [/System/Library/PrivateFrameworks/WiFiPolicy.framework/XPCServices/WiFiCloudAssetsXPCService.xpc/WiFiCloudAssetsXPCService](MACHOS/WiFiCloudAssetsXPCService.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/FocusConfigurationExtension.appex/FocusConfigurationExtension](MACHOS/FocusConfigurationExtension.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/SystemActionConfigurationExtension.appex/SystemActionConfigurationExtension](MACHOS/SystemActionConfigurationExtension.md)
- [/System/Library/PrivateFrameworks/iCloudDriveService.framework/XPCServices/TelemetryDiskChecker.xpc/TelemetryDiskChecker](MACHOS/TelemetryDiskChecker.md)
- [/System/Library/Settings/InstalledApps.settings/InstalledApps](MACHOS/InstalledApps.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/AudioSuggestionsPlugin.bundle/AudioSuggestionsPlugin](MACHOS/AudioSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/HomeAutomationSiriSuggestions.bundle/HomeAutomationSiriSuggestions](MACHOS/HomeAutomationSiriSuggestions.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriNotebookSuggestionsPlugin.bundle/SiriNotebookSuggestionsPlugin](MACHOS/SiriNotebookSuggestionsPlugin.md)
- [/System/Library/Snippets/UIPlugins/ResponseGenerationUIPlugin.bundle/ResponseGenerationUIPlugin](MACHOS/ResponseGenerationUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SystemPlugin.bundle/SystemPlugin](MACHOS/SystemPlugin.md)
- [/System/Library/UsageBundles/SoftwareUpdateUsage.bundle/SoftwareUpdateUsage](MACHOS/SoftwareUpdateUsage.md)
- [/System/Library/UserEventPlugins/AHTUserEventAgent.plugin/AHTUserEventAgent](MACHOS/AHTUserEventAgent.md)
- [/System/Library/UserEventPlugins/PerfPowerServicesEventListenerPlugin.plugin/PerfPowerServicesEventListenerPlugin](MACHOS/PerfPowerServicesEventListenerPlugin.md)
- [/System/Library/UserEventPlugins/com.apple.cts.plugin/com.apple.cts](MACHOS/com.apple.cts.md)
- [/System/Library/UserEventPlugins/locationd.events.plugin/locationd.events](MACHOS/locationd.events.md)
- [/System/Library/Video/Plug-Ins/AppleMCTF.bundle/AppleMCTF](MACHOS/AppleMCTF.md)
- [/System/Library/Video/Plug-Ins/AppleVideoEncoder.bundle/AppleVideoEncoder](MACHOS/AppleVideoEncoder.md)
- [/private/var/staged_system_apps/AppStore.app/AppStore](MACHOS/AppStore.md)
- [/private/var/staged_system_apps/AppStore.app/PlugIns/AppStoreWidgetsExtension.appex/AppStoreWidgetsExtension](MACHOS/AppStoreWidgetsExtension.md)
- [/private/var/staged_system_apps/AppleTV.app/PlugIns/TVWidgetExtension.appex/TVWidgetExtension](MACHOS/TVWidgetExtension.md)
- [/private/var/staged_system_apps/Books.app/Books](MACHOS/Books.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookAnalytics.framework/BookAnalytics](MACHOS/BookAnalytics.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookEPUB.framework/BookEPUB](MACHOS/BookEPUB.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookStoreUI.framework/BookStoreUI](MACHOS/BookStoreUI.md)
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
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyWidgetPeople.appex/FindMyWidgetPeople](MACHOS/FindMyWidgetPeople.md)
- [/private/var/staged_system_apps/Fitness.app/Fitness](MACHOS/Fitness.md)
- [/private/var/staged_system_apps/Fitness.app/PlugIns/FitnessWidget.appex/FitnessWidget](MACHOS/FitnessWidget.md)
- [/private/var/staged_system_apps/Freeform.app/Extensions/USDRendererExtension.appex/USDRendererExtension](MACHOS/USDRendererExtension.md)
- [/private/var/staged_system_apps/Freeform.app/Freeform](MACHOS/Freeform.md)
- [/private/var/staged_system_apps/Freeform.app/PlugIns/FreeformSharingExtension.appex/FreeformSharingExtension](MACHOS/FreeformSharingExtension.md)
- [/private/var/staged_system_apps/Freeform.app/PlugIns/FreeformWidgetKitExtension.appex/FreeformWidgetKitExtension](MACHOS/FreeformWidgetKitExtension.md)
- [/private/var/staged_system_apps/Health.app/Health](MACHOS/Health.md)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeEnergyWidgetsExtension.appex/HomeEnergyWidgetsExtension](MACHOS/HomeEnergyWidgetsExtension.md)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeNotification.appex/HomeNotification](MACHOS/HomeNotification.md)
- [/private/var/staged_system_apps/Journal.app/Journal](MACHOS/Journal.md)
- [/private/var/staged_system_apps/Journal.app/PlugIns/JournalWidgets.appex/JournalWidgets](MACHOS/JournalWidgets.md)
- [/private/var/staged_system_apps/Journal.app/PlugIns/JournalWidgetsSecure.appex/JournalWidgetsSecure](MACHOS/JournalWidgetsSecure.md)
- [/private/var/staged_system_apps/Maps.app/Maps](MACHOS/Maps.md)
- [/private/var/staged_system_apps/Maps.app/PlugIns/GeneralMapsWidget.appex/GeneralMapsWidget](MACHOS/GeneralMapsWidget.md)
- [/private/var/staged_system_apps/Measure.app/Measure](MACHOS/Measure.md)
- [/private/var/staged_system_apps/MobileCal.app/MobileCal](MACHOS/MobileCal.md)
- [/private/var/staged_system_apps/MobileCal.app/PlugIns/CalendarWidgetExtension.appex/CalendarWidgetExtension](MACHOS/CalendarWidgetExtension.md)
- [/private/var/staged_system_apps/MobileMail.app/MobileMail](MACHOS/MobileMail.md)
- [/private/var/staged_system_apps/MobileMail.app/PlugIns/MailNotificationContentExtension.appex/MailNotificationContentExtension](MACHOS/MailNotificationContentExtension.md)
- [/private/var/staged_system_apps/MobileMail.app/PlugIns/MailQuickLookExtension.appex/MailQuickLookExtension](MACHOS/MailQuickLookExtension.md)
- [/private/var/staged_system_apps/MobileNotes.app/MobileNotes](MACHOS/MobileNotes.md)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.SharingExtension.appex/com.apple.mobilenotes.SharingExtension](MACHOS/com.apple.mobilenotes.SharingExtension.md)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.WidgetExtension.appex/com.apple.mobilenotes.WidgetExtension](MACHOS/com.apple.mobilenotes.WidgetExtension.md)
- [/private/var/staged_system_apps/MobileSafari.app/PlugIns/SafariWidgetExtension.appex/SafariWidgetExtension](MACHOS/SafariWidgetExtension.md)
- [/private/var/staged_system_apps/Music.app/Frameworks/MusicApplication.framework/MusicApplication](MACHOS/MusicApplication.md)
- [/private/var/staged_system_apps/Music.app/Frameworks/MusicApplication.framework/XPCServices/MusicScriptUpdateService.xpc/MusicScriptUpdateService](MACHOS/MusicScriptUpdateService.md)
- [/private/var/staged_system_apps/Music.app/Music](MACHOS/Music.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/MusicMessagesApp.appex/MusicMessagesApp](MACHOS/MusicMessagesApp.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/MusicWidgets.appex/MusicWidgets](MACHOS/MusicWidgets.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsToday2.appex/NewsToday2](MACHOS/NewsToday2.md)
- [/private/var/staged_system_apps/Passbook.app/PlugIns/PassbookLockedWidgetsExtension.appex/PassbookLockedWidgetsExtension](MACHOS/PassbookLockedWidgetsExtension.md)
- [/private/var/staged_system_apps/Passbook.app/PlugIns/PassbookWidgetsExtension-iPhone.appex/PassbookWidgetsExtension-iPhone](MACHOS/PassbookWidgetsExtension-iPhone.md)
- [/private/var/staged_system_apps/Photos.app/Photos](MACHOS/Photos.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/NowPlayingUI.framework/NowPlayingUI](MACHOS/NowPlayingUI.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/PodcastsTranscripts.framework/PodcastsTranscripts](MACHOS/PodcastsTranscripts.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/ShelfKit.framework/ShelfKit](MACHOS/ShelfKit.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/ShelfKitCollectionViews.framework/ShelfKitCollectionViews](MACHOS/ShelfKitCollectionViews.md)
- [/private/var/staged_system_apps/Podcasts.app/Podcasts](MACHOS/Podcasts.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersIntentsExtension.appex/RemindersIntentsExtension](MACHOS/RemindersIntentsExtension.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersIntentsUIExtension.appex/RemindersIntentsUIExtension](MACHOS/RemindersIntentsUIExtension.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersSharingExtension.appex/RemindersSharingExtension](MACHOS/RemindersSharingExtension.md)
- [/private/var/staged_system_apps/Reminders.app/Reminders](MACHOS/Reminders.md)
- [/private/var/staged_system_apps/SequoiaTranslator.app/PlugIns/TranslationWidgetsExtension.appex/TranslationWidgetsExtension](MACHOS/TranslationWidgetsExtension.md)
- [/private/var/staged_system_apps/SequoiaTranslator.app/SequoiaTranslator](MACHOS/SequoiaTranslator.md)
- [/private/var/staged_system_apps/Shortcuts.app/PlugIns/ShortcutsWidgetExtension.appex/ShortcutsWidgetExtension](MACHOS/ShortcutsWidgetExtension.md)
- [/private/var/staged_system_apps/Shortcuts.app/Shortcuts](MACHOS/Shortcuts.md)
- [/private/var/staged_system_apps/Stocks.app/PlugIns/StocksWidget.appex/StocksWidget](MACHOS/StocksWidget.md)
- [/private/var/staged_system_apps/Tips.app/PlugIns/TipsNotification.appex/TipsNotification](MACHOS/TipsNotification.md)
- [/private/var/staged_system_apps/Tips.app/Tips](MACHOS/Tips.md)
- [/private/var/staged_system_apps/VoiceMemos.app/VoiceMemos](MACHOS/VoiceMemos.md)
- [/private/var/staged_system_apps/Weather.app/PlugIns/WeatherWidget.appex/WeatherWidget](MACHOS/WeatherWidget.md)
- [/private/var/staged_system_apps/Weather.app/Weather](MACHOS/Weather.md)
- [/sbin/launchd](MACHOS/launchd.md)
- [/usr/bin/abmlite](MACHOS/abmlite.md)
- [/usr/bin/swift-inspect](MACHOS/swift-inspect.md)
- [/usr/lib/dyld](MACHOS/dyld.md)
- [/usr/lib/libmobileassetd.dylib](MACHOS/libmobileassetd.dylib.md)
- [/usr/libexec/AuthenticationServicesAgent](MACHOS/AuthenticationServicesAgent.md)
- [/usr/libexec/BackupAgent2](MACHOS/BackupAgent2.md)
- [/usr/libexec/PerfPowerServices](MACHOS/PerfPowerServices.md)
- [/usr/libexec/PerfPowerServicesExtended](MACHOS/PerfPowerServicesExtended.md)
- [/usr/libexec/SidecarRelay](MACHOS/SidecarRelay.md)
- [/usr/libexec/appleaccountd](MACHOS/appleaccountd.md)
- [/usr/libexec/applekeystored](MACHOS/applekeystored.md)
- [/usr/libexec/assessmentagent](MACHOS/assessmentagent.md)
- [/usr/libexec/audioaccessoryd](MACHOS/audioaccessoryd.md)
- [/usr/libexec/audioanalyticsd](MACHOS/audioanalyticsd.md)
- [/usr/libexec/bluetoothuserd](MACHOS/bluetoothuserd.md)
- [/usr/libexec/configd](MACHOS/configd.md)
- [/usr/libexec/coreidvd](MACHOS/coreidvd.md)
- [/usr/libexec/corerepaird](MACHOS/corerepaird.md)
- [/usr/libexec/cryptexd](MACHOS/cryptexd.md)
- [/usr/libexec/dasd](MACHOS/dasd.md)
- [/usr/libexec/dockaccessoryd](MACHOS/dockaccessoryd.md)
- [/usr/libexec/driverkitd](MACHOS/driverkitd.md)
- [/usr/libexec/feedbackd](MACHOS/feedbackd.md)
- [/usr/libexec/findmylocated](MACHOS/findmylocated.md)
- [/usr/libexec/gamed](MACHOS/gamed.md)
- [/usr/libexec/gamepolicyd](MACHOS/gamepolicyd.md)
- [/usr/libexec/gpsd](MACHOS/gpsd.md)
- [/usr/libexec/handwritingd](MACHOS/handwritingd.md)
- [/usr/libexec/icloudmailagent](MACHOS/icloudmailagent.md)
- [/usr/libexec/idcredd](MACHOS/idcredd.md)
- [/usr/libexec/linkd](MACHOS/linkd.md)
- [/usr/libexec/locationd](MACHOS/locationd.md)
- [/usr/libexec/mlhostd](MACHOS/mlhostd.md)
- [/usr/libexec/mmaintenanced](MACHOS/mmaintenanced.md)
- [/usr/libexec/mobilerepaird](MACHOS/mobilerepaird.md)
- [/usr/libexec/modelmanagerd](MACHOS/modelmanagerd.md)
- [/usr/libexec/momentsd](MACHOS/momentsd.md)
- [/usr/libexec/nanoregistryd](MACHOS/nanoregistryd.md)
- [/usr/libexec/nearbyd](MACHOS/nearbyd.md)
- [/usr/libexec/nfcd](MACHOS/nfcd.md)
- [/usr/libexec/nptocompaniond](MACHOS/nptocompaniond.md)
- [/usr/libexec/photosfaced](MACHOS/photosfaced.md)
- [/usr/libexec/pipelined](MACHOS/pipelined.md)
- [/usr/libexec/promotedcontentd](MACHOS/promotedcontentd.md)
- [/usr/libexec/proximitycontrold](MACHOS/proximitycontrold.md)
- [/usr/libexec/ptpcamerad](MACHOS/ptpcamerad.md)
- [/usr/libexec/ptpd](MACHOS/ptpd.md)
- [/usr/libexec/remindd](MACHOS/remindd.md)
- [/usr/libexec/remotepairingdeviced](MACHOS/remotepairingdeviced.md)
- [/usr/libexec/rtcreportingd](MACHOS/rtcreportingd.md)
- [/usr/libexec/safetyalertsd](MACHOS/safetyalertsd.md)
- [/usr/libexec/screenshotsyncd](MACHOS/screenshotsyncd.md)
- [/usr/libexec/searchpartyd](MACHOS/searchpartyd.md)
- [/usr/libexec/seserviced](MACHOS/seserviced.md)
- [/usr/libexec/sportsd](MACHOS/sportsd.md)
- [/usr/libexec/storagekitd](MACHOS/storagekitd.md)
- [/usr/libexec/swtransparencyd](MACHOS/swtransparencyd.md)
- [/usr/libexec/thermalmonitord](MACHOS/thermalmonitord.md)
- [/usr/libexec/transparencyd](MACHOS/transparencyd.md)
- [/usr/libexec/trustd](MACHOS/trustd.md)
- [/usr/libexec/tzd](MACHOS/tzd.md)
- [/usr/libexec/webbookmarksd](MACHOS/webbookmarksd.md)
- [/usr/libexec/wifip2pd](MACHOS/wifip2pd.md)
- [/usr/libexec/xpcproxy](MACHOS/xpcproxy.md)
- [/usr/libexec/xpcroleaccountd](MACHOS/xpcroleaccountd.md)
- [/usr/sbin/BlueTool](MACHOS/BlueTool.md)
- [/usr/sbin/WirelessRadioManagerd](MACHOS/WirelessRadioManagerd.md)
- [/usr/sbin/bluetoothd](MACHOS/bluetoothd.md)
- [/usr/sbin/mDNSResponder](MACHOS/mDNSResponder.md)
- [/usr/sbin/wifid](MACHOS/wifid.md)

</details>

### 🔑 Entitlements

- [Entitlements DIFF](Entitlements.md)

## Firmware

### ⬆️ Updated (7)

<details>
  <summary><i>View Updated</i></summary>

#### AppleAVE2FW_H17.im4p

>  `AppleAVE2FW_H17.im4p`

```diff

 
-  __TEXT.__text: 0xe388c
-  __TEXT.__cstring: 0x141ef
+  __TEXT.__text: 0xe3b2c
+  __TEXT.__cstring: 0x1429d
   __TEXT.__const: 0x22764
   __TEXT.__chain_starts: 0x0
   __TEXT._rtk_mtab: 0x2d0

   __DATA._rtk_heap: 0x0
   __DATA.__zerofill: 0xcbd38
   Functions: 0
-  Symbols:   1545
-  CStrings:  2421
+  Symbols:   1547
+  CStrings:  2426
 
Symbols:
+ __ZN22CAvePipeMcpuISRManager12HandleSourceEj
+ __ZN22CAvePipeMcpuISRManager14ServiceRoutineEv
+ __ZN22CAvePipeMcpuISRManager24RegisteredServiceRoutineEPv
- __ZN18CAVEPipeISRManager12TimerHandlerEPv
CStrings:
+ "%s::%s() case %d"
+ "./AppleAVE2FW/MCPU/Image/common/CAvePipeMcpuISRManager.cpp"
+ "8002.30.0"
+ "CAvePipeMcpuISRManager"
+ "HandleSource"
+ "Reference buffers are not in recon buffers!"
+ "ServiceRoutine"
+ "entry != NULL"
+ "entry->callback || entry->callback_with_source"
- "%s:%d unsupported %p"
- "8002.34.0"
- "AVE_CallbackWrap"
- "CPlatformISRManager"

```

#### adc-rheia-d9x.im4p

>  `adc-rheia-d9x.im4p`

```diff

 
-  __TEXT.__text: 0x75287c
+  __TEXT.__text: 0x75307c
   __TEXT.__data_copy: 0x200000
   __TEXT.__const: 0x9feaa0
-  __TEXT.__cstring: 0xa3455
+  __TEXT.__cstring: 0xa3304
   __TEXT._rtk_mtab: 0x2b8
   __TEXT.__constructor: 0x0
   __TEXT.__chain_starts: 0x0
   __TEXT.text_env: 0x4fdac
   __TEXT.__eh_frame: 0x408
-  __DATA.__const: 0x57bf0
+  __DATA.__const: 0x57c70
   __DATA._rtk_heap: 0x1000
-  __DATA.__data: 0xe0cc8
+  __DATA.__data: 0xe28c8
   __DATA._rtk_power: 0x3a8
   __DATA._rtk_patchbay: 0x238
   __DATA._rtk_init_stack: 0x2000

   __DATA.__zerofill: 0x654420
   Functions: 0
   Symbols:   0
-  CStrings:  17893
+  CStrings:  17887
 
CStrings:
+ "%#zx: %#x %#x\n"
+ "19:28:21"
+ "ChangeMode"
+ "Dec 18 2024"
+ "Err: %s\n"
+ "Error: Chroma ch=%u Ms=%d Step=%d out=(%d %d) fmt=%d cmp=%d\n"
+ "Error: Luma ch=%u Ms=%d Step=%d out=(%d %d) fmt=%d %d cmp=%d\n"
+ "Height > 0 && Height <= pDescr->paramBES.m2mGdcBufferHeight"
+ "LCAUX Ch%zu Executing %s\n"
+ "LCAUX Ch%zu Finished %s\n"
+ "M2MGDC w/o output: scl0 %d %d, scl1 %d %d, overwritten by %d %d, m2mbuf %d %d\n"
+ "Width > 0 && Width <= pDescr->paramBES.m2mGdcBufferWidth"
+ "outHeight > 0 && outHeight <= pDescr->paramBES.m2mGdcBufferHeight"
+ "outWidth > 0 && outWidth <= pDescr->paramBES.m2mGdcBufferWidth"
+ "textSize: exp %zu act %zu, scalerId=%d\n"
- "%s: FD FLASH AF (mac2inf): matrixParams.snrPercentileThLimit=[%f]\n\n"
- "%s: afBlurMDataCompromised=[%d]\n\n"
- "%s: afBlurMDataCompromised_FD=[%d]\n\n"
- "%s: afBlurMDataCompromised_FD_Default=[%d]\n\n"
- "%s: afFdBestPosCompromised=[%d]\n\n"
- "%s: afFdBestPosCompromised=[%d],afFdBestPosCompromised_BlurM=[%d]\n\n"
- "%s: afFdBestPosCompromised_BlurM=[%d]\n\n"
- "%s: afFdBestPosCompromised_SingleWin=[%d]\n\n"
- "%s: bAfBlurMCompromised_FD=[%d]\n\n"
- "%s: bAfBlurMCompromised_FD_Default=[%d]\n\n"
- "%s: bestScanPos=[%d]\n\n"
- "%s: bestScanPosFD_Default=[%d],matrixUsedDefaultLensPos=[%d]\n\n"
- "%s: bestScanPosFD_FD=[%d],bestScanPosFD_Default=[%d]\n\n"
- "%s: bestScanPosFD_FD=[%d],bestScanPosFD_FD_BlurM=[%d]\n\n"
- "%s: bestScanPosFD_FD=[%d],matrixUsedDefaultLensPos=[%d]\n\n"
- "%s: bestScanPosFD_FD_BlurM=[%d],matrixUsedDefaultLensPos=[%d]\n\n"
- "%s: bestScanPosFD_FD_SingleWin=[%d]\n\n"
- "%s: bestScanPosFD_FD_SingleWin=[%d],bestScanPosFD_Default=[%d]\n\n"
- "%s: matrixParams.fdBestPosSourceSel=[%d]\n\n"
- "01:38:27"
- "Dec  6 2024"

```

#### exclave_kernel

>  `exclave_kernel`

```diff

 
   __TEXT.__head: 0x1b0
-  __TEXT.__text: 0xfc04
+  __TEXT.__text: 0xfdcc
   __TEXT.__const: 0xa50
-  __TEXT.__cstring: 0x8f0
+  __TEXT.__cstring: 0x954
   __DATA.__data: 0x130
   __DATA.__bss: 0x19a00
   __DATA.__common: 0x50
   __IMAGE_END.__image_end: 0x0
-  Functions: 155
-  Symbols:   413
-  CStrings:  161
+  Functions: 156
+  Symbols:   414
+  CStrings:  166
 
CStrings:
+ "cL4 microkernel (cL4 (495.80.2))"
+ "devicetree.c:164"
+ "devicetree.c:207"
+ "devicetree.c:215"
+ "devicetree.c:240"
+ "devicetree.c:246"
+ "devicetree.c:75"
+ "exclave-io-ranges"
+ "iop-audio-controller"
+ "lp-mic-io-buffer-device"
+ "memcache-aperture"
- "cL4 microkernel (cL4 (495.80.1))"
- "devicetree.c:166"
- "devicetree.c:188"
- "devicetree.c:196"
- "devicetree.c:70"
- "pmap-io-ranges"

```

#### exclave_sharedcache

>  `exclave_sharedcache`

```diff

 460.80.5.0.0
-  __TEXT.__text: 0x4c27e8
+  __TEXT.__text: 0x4c295c
   __TEXT.__lcxx_override: 0x200
   __TEXT.__cstring: 0x30b5f
   __TEXT.__const: 0xe2768

   __TEXT.__term_offsets: 0x0
   __TEXT.__swift5_replace: 0x0
   __TEXT.__thread_starts: 0x3c
-  __TEXT.__eh_frame: 0x23acc
+  __TEXT.__eh_frame: 0x23abc
   __DATA.__got: 0x18
   __DATA.__auth_ptr: 0x280
   __DATA.__mod_init_func: 0x38

   __PDATA.__common: 0x1fc0
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  Functions: 18492
+  Functions: 18494
   Symbols:   0
   CStrings:  5151
 
CStrings:
+ "/AppleInternal/Library/BuildRoots/7d2a62ca-bb83-11ef-9317-6efa4e70477e/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.3.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
+ "/AppleInternal/Library/BuildRoots/7d2a62ca-bb83-11ef-9317-6efa4e70477e/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.3.Internal.sdk/System/ExclaveCore/usr/local/standalone/RTKit/usr/include/protocols/mbi_tightbeam_protocol.h"
- "/AppleInternal/Library/BuildRoots/d6ad906a-b370-11ef-a1b4-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.3.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
- "/AppleInternal/Library/BuildRoots/d6ad906a-b370-11ef-a1b4-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.3.Internal.sdk/System/ExclaveCore/usr/local/standalone/RTKit/usr/include/protocols/mbi_tightbeam_protocol.h"

```

#### h17_ane_fw_theia_d9x.im4p

>  `h17_ane_fw_theia_d9x.im4p`

```diff

 
-  __TEXT.__text: 0x96388
+  __TEXT.__text: 0xb9040
   __TEXT.__const: 0x4214
-  __TEXT.__cstring: 0x12c93
+  __TEXT.__cstring: 0x1ad6e
   __TEXT.ce_env: 0x4000
   __TEXT.__constructor: 0x0
   __TEXT.text_env: 0x20
-  __DATA.__const: 0x9ba0
+  __DATA.__const: 0x9be0
   __DATA._rtk_heap: 0x1000
-  __DATA.__data: 0xd70
+  __DATA.__data: 0xf70
   __DATA._rtk_power: 0x3b8
   __DATA._rtk_patchbay: 0x258
   __DATA._rtk_init_stack: 0x10000

   __DATA._rtk_mtab: 0x2a0
   __DATA.__gxf_data: 0x10
   __DATA.__mod_init_func: 0x0
-  __DATA.__zerofill: 0x55948
-  Functions: 1351
+  __DATA.__zerofill: 0x55998
+  Functions: 1467
   Symbols:   0
-  CStrings:  2148
+  CStrings:  3291
 
CStrings:
+ "\tFW Latency Signposts 0x%x id 0x%x ts %lld"
+ "\x1b[31m\"    Found Matched Priority Q[%d]S[%d] during Termination\"\x1b[39m"
+ "\x1b[31m\"ABORT queue %d slot %d (nid %d) with multi segment\"\x1b[39m"
+ "\x1b[31m\"Fail\"\x1b[39m"
+ "\x1b[31m\"[ABORT] Suspend other TQs for TQ[%d]S[%d] at %lld\"\x1b[39m"
+ "\x1b[31m\"[ABORT] TQ abort Q[%d] -> at %lld\"\x1b[39m"
+ "\x1b[31m\"[ABORT] TQ abort Q[%d] -> both slots, first slot is %d\"\x1b[39m"
+ "\x1b[31m\"[ABORT] TQ abort Q[%d] -> slot [%d]\"\x1b[39m"
+ "\x1b[31m\"[StopTqInt] nid %d\"\x1b[39m"
+ "\x1b[31m[VERIFICATION]\x1b[39m BAR[%d] bufferIndex %d is NOT matched with any buffer!"
+ "\x1b[31m[VERIFICATION]\x1b[39m BAR[%d] bufferIndex %d is matched with buffers more than one!"
+ "\x1b[31m[VERIFICATION]\x1b[39m BAR[%d] index %d should <= %d!"
+ "\x1b[31m[VERIFICATION]\x1b[39m Generic ANE[%d] nbrOfNe %d exceeds H11 max NE %d!"
+ "\x1b[31m[VERIFICATION]\x1b[39m Generic section (%lu) is smaller than actual (%lu)!"
+ "\x1b[31m[VERIFICATION]\x1b[39m Generic section buffer[%d] is not valid!"
+ "\x1b[31m[VERIFICATION]\x1b[39m Generic section buffer[%d] is wrong type %d!"
+ "\x1b[31m[VERIFICATION]\x1b[39m KernelProp[%d] exceeds limit (offset, len) (0x%llx, %lld) section size %lu!"
+ "\x1b[31m[VERIFICATION]\x1b[39m KernelProp[%d] offset 0x%llx is overlapped with the previous offset 0x%llx len %lld!"
+ "\x1b[31m[VERIFICATION]\x1b[39m Operation BAR setup number %d is exceed MAX_BAR_SLOTS %d!"
+ "\x1b[31m[VERIFICATION]\x1b[39m Operation number %d exceeds MAX Operation number (%d)!"
+ "\x1b[31m[VERIFICATION]\x1b[39m Operation section (%lu) is smaller than actual (%lu)!"
+ "\x1b[31m[VERIFICATION]\x1b[39m Operation[%d] BAR setup is wrong!"
+ "\x1b[31m[VERIFICATION]\x1b[39m Operation[%d] bar[%d] index %d exceeds H11 bar slots %d!"
+ "\x1b[31m[VERIFICATION]\x1b[39m Operation[%d] nbrOfLocalbarSetup %d exceeds EAnsProgramBarMaxIndex %d!"
+ "\x1b[31m[VERIFICATION]\x1b[39m Operation[%d] nbrOfNe %d exceeds H11 max NE %d!"
+ "\x1b[31m[VERIFICATION]\x1b[39m Operation[%d] wrong opType %d!"
+ "\x1b[31m[VERIFICATION]\x1b[39m Procedure[%d] exceeds limit (offset, len) (0x%llx, %lld) section size %lu!"
+ "\x1b[31m[VERIFICATION]\x1b[39m Procedure[%d] offset 0x%llx is overlapped with the previous offset 0x%llx len %lld!"
+ "\x1b[31m[VERIFICATION]\x1b[39m SegmentProp section (%lu) is smaller than actual (%lu)!"
+ "\x1b[31m[VERIFICATION]\x1b[39m Segment[%d] Addr %p EON %d last TID %d with Liveouts 0x%x"
+ "\x1b[31m[VERIFICATION]\x1b[39m Segment[%d] Addr %p TID %d with 0 size"
+ "\x1b[31m[VERIFICATION]\x1b[39m Segment[%d] exceeds limit (offset, len) (0x%llx, %lld) section size %lu!"
+ "\x1b[31m[VERIFICATION]\x1b[39m Segment[%d] len %lld is smaller than ane_Network_Seg_Hdr_t (BranchEn %d)!"
+ "\x1b[31m[VERIFICATION]\x1b[39m Segment[%d] number of TD (%d) does not match value in prop (%d)"
+ "\x1b[31m[VERIFICATION]\x1b[39m TD[%d] offset 0x%llx is overlapped with the previous offset 0x%llx len %lld!"
+ "\x1b[31m[VERIFICATION]\x1b[39m maxAneUsed %d :: H11 maxAneUsed should be %d!"
+ "\x1b[31m[VERIFICATION]\x1b[39m sCSneCmdProcedureCall buffer[%d] is not valid!"
+ "\x1b[31m[VERIFICATION]\x1b[39m sCSneCmdProcedureCall buffer[%d]:index[%d] SHOULD not match with Kernel!"
+ "\x1b[31m[VERIFICATION]\x1b[39m sCSneCmdProcedureCall buffer[%d]:index[%d] SHOULD not match with segment!"
+ "\x1b[31m[VERIFICATION]\x1b[39m sCSneCmdProcedureCall buffer[%d]:index[%d] is matched more than one!"
+ "\x1b[31m[VERIFICATION]\x1b[39m sCSneCmdProcedureCall buffer[%d]:index[%d] is not matched with any of buffers!"
+ "\x1b[31m[VERIFICATION]\x1b[39m sCSneCmdProcedureCall buffer[%d]:index[%d](%lld)=>Generic:buffer[%d](%lld). But wrong size!"
+ "\x1b[31m[VERIFICATION]\x1b[39m sCSneCmdProcedureCall buffer[%d]:index[%d]=>Generic:buffer[%d]. But not valid!"
+ "\x1b[31m[VERIFICATION]\x1b[39m sCSneCmdProcedureCall nbfOfbuffers %d (range 1 <= # <= 64)!"
+ "\x1b[31m[VERIFICATION]\x1b[39m totalBufferNbr %d :: range should 0 < # < ECSneProgramMaxBuf (%d)!"
+ "\x1b[32m\"Success\"\x1b[39m"
+ "\x1b[33m\"Saving KMem from 0x%zx with 0x%zx\"\x1b[39m"
+ "\x1b[33m\"Saving L2 from 0x%zx with 0x%zx\"\x1b[39m"
+ "\x1b[33m\"Saving ane registers from 0x%zx with 0x%zx\"\x1b[39m"
+ "\x1b[33m\"Start saving out after running into TD#%d from (%d-%d-%d)\"\x1b[39m"
+ "\x1b[33m* PROGRAM :\x1b[39m"
+ "\x1b[33m* TD :\x1b[39m"
+ "\x1b[33m***** ANE RUN INFO ***** : program (0x%x)\x1b[39m"
+ "\x1b[33m***** ANE TD INFO ***** : program (0x%x)\x1b[39m"
+ "\x1b[33m************************\x1b[39m"
+ "\x1b[34m* OPTIONS *\x1b[39m"
+ "\x1b[34m***** ANE STATS *****\x1b[39m"
+ "\x1b[34m***** PROCEDURE INFO *****\x1b[39m"
+ "\x1b[34m***** PROCESS INFO *****\x1b[39m"
+ "\x1b[34m***** PROGRAM INFO *****\x1b[39m"
+ "\x1b[34m*********************\x1b[39m"
+ "\x1b[34m************************\x1b[39m"
+ "\x1b[34m**************************\x1b[39m"
+ " "
+ "          Bar[%d] : barIndex %d bufIndex %d"
+ "     [%d] : Offset %lld length %lld"
+ "     [%d] : Type %d nbrNe %d nbrOfLocalbarSetup %d"
+ "     [%d] : Type %d startAddr 0x%x endAddr 0x%x Size %x nbrNe %d nbrOfLocalbarSetup %d"
+ "     [%d] : format %d isCompressed 0x%x len 0x%llx offset %llx"
+ "     aneMapping[%d] : %d"
+ "     nBuf %d inputEvent %d priority %d uuid 0x%llx"
+ "   %6u : [P:%d, %s] -- [T:%d, %s] -> ERROR: %s\n"
+ "   %6u : [P:%d, %s] -- [T:%d, %s] -> [S:%d, %s]\n"
+ "   %6u : [P:%d, %s] -- [T:%d] -> ERROR: WRONG EVENT\n"
+ "  %s : There no state transitions\n"
+ "  %s [%p]: Last %zu transitions [total = %zu]:\n"
+ " %d : handle 0x%x offset 0x%lx len 0x%lx with Remap count %d\n"
+ " %d : handle 0x%x offset 0x%lx len 0x%lx with map count %d\n"
+ " %d [%#x]"
+ " %p"
+ " %s: event (%d, %s)"
+ " %s: event (%d, %s), rc = %d [%#x]"
+ " %s: event=%d [%s] cb %s"
+ " Acquired %p"
+ " Acquiring %p"
+ " Released %p"
+ " To release %p"
+ "!(pageWiringOn && forceWiring)"
+ "!bSubNetworkCustomExecuteOrder"
+ "!commandBufPhysAddr"
+ "!endPointCb[pCmd->endPointId].shareMem.item[i].used"
+ "!pEntry->child"
+ "!reader"
+ "%-30s %-16.4f %-16lld %-16lld %-8lld\n"
+ "%-30s %-16s %-16s %-16s %-8s\n"
+ "%-30s %-6s %-8.4f %-8.4f\n"
+ "%-30s %-6s %-8.4f %-8s %-10.4f %-16lld %-16lld %-8lld\n"
+ "%-30s %-6s %-8s %-8.4f %-10.4f %-16lld %-16lld %-8lld\n"
+ "%-30s %-6s %-8s %-8s %-10.4f %-16lld %-16lld %-8lld\n"
+ "%-30s %-6s %-8s %-8s %-10s %-16s %-16s %-8s\n"
+ "%d : buf %p size 0x%lx index 0x%x\n"
+ "%lld delay trigger, %lld ignored due to exceeded execTimestamp"
+ "%s : *** ACK: Endpoint command %d with ticket %u seq %u\n"
+ "%s : *** endPoint %d cmd %d ack 0x%x ack_rc 0x%x ticket %u seq %u\n"
+ "%s : Configure pCmd endPointId = %d\n"
+ "%s : Free Shared Memory endPointId = %d at %p\n"
+ "%s : Get EndPoint Status %d\n"
+ "%s : Get Outstanding Ticket Cnt %d\n"
+ "%s : Malloc Shared Memory endPointId = %d\n"
+ "%s : SAP Register endPointId = %d sapId = 0x%x\n"
+ "%s : SAP UnRegister endPointId = %d sapId = 0x%x\n"
+ "%s : Send Buf endPointId %d sapId 0x%x %d\n"
+ "%s : Unset pCmd endPointId = %d\n"
+ "%s : valid %d bufIndex %d type %d addr 0x%llx memType %d size %lld tag %llx"
+ "%s: (%d, %s): [%d, %s]->[%d, %s]"
+ "%s: CH = %zu START"
+ "%s: CH = %zu STOP"
+ "%s: GOING TO STOP"
+ "%s: SETUP"
+ "%s: START"
+ "%s: STOP"
+ "%s: TEARDOWN"
+ "(%s) %s\n"
+ "(((size_t)(blockArray[dBlock])) % alignment[dBlock]) == 0"
+ "((size_t)pointer) < ((size_t)(h->pMsg)) + h->queueDepth * sizeof(struct ffwInterProcMsg)"
+ "((size_t)pointer) >= ((size_t)(h->pMsg))"
+ "((uintptr_t)entry->stack & (RTK_CRT_STACK_ALIGNMENT - 1)) == 0"
+ "(*parent == logDepth) || (*parent == index)"
+ "(*parent == logDepth) || (*parent == pEntry->parent)"
+ "(FFWMUTEX)0 != lock"
+ "(IOP_RINGBUFFER_VERSION == (pBuf->_header._version>>16)) || (IOP_RINGBUFFER_VERSION_V2 == (pBuf->_header._version>>16))"
+ "(SEMA)0 != cmd.syncCmdSema"
+ "(callback == NULL) || (user_signal == 0)"
+ "(ffwQueueCount (queue) == 0) || (((size_t) ffwQueueCount (queue)) == buffers)"
+ "(idx >= 0) && (idx < (mNumEntriesPerPool * mMaxPoolNum))"
+ "(idx >= 0) && (idx < hash_entries_num)"
+ "(inputs > 0) || (outputs > 0)"
+ "(mCurrPoolNum + pool_num) <= mMaxPoolNum"
+ "(new_end & HEAP_OFFSET) == 0"
+ "(operation == LOG_OPERATION_WIRED) || (operation == LOG_OPERATION_UNWIRED)"
+ "(pCmd->pBufIndex[i] & ~maskRemapIndex) < sizeof(endPointCb[pCmd->endPointId].shareMem.remap)/sizeof(endPointCb[pCmd->endPointId].shareMem.remap[0])"
+ "(pCmd->pBufIndex[i]) < sizeof(endPointCb[pCmd->endPointId].shareMem.item)/sizeof(endPointCb[pCmd->endPointId].shareMem.item[0])"
+ "(size_t) ffwQueueCount (queue) == available"
+ "(size_t)source < INTERRUPT_SRC_TOTAL"
+ "(stacksize & (RTK_CRT_STACK_ALIGNMENT - 1)) == 0"
+ "*extra_heap_size >= extra_heap_size_min"
+ "*idx < CTASKPOOL_MAXTASK_HIST_ENTRIES"
+ "*indexOut == logDepth"
+ "*outsize <= maxOutsize"
+ "*outsize >= sizeof(struct sCSneCmdPrintEnable)"
+ "*print_buffer_base != 0"
+ "*sm_base != 0"
+ "*sm_size != 0"
+ "-----------interval------------\n"
+ "./ffw64_rtxc/ffw/CBuffer.cpp"
+ "./ffw64_rtxc/ffw/CBufferPool.cpp"
+ "./ffw64_rtxc/ffw/CBufferPoolStatic.cpp"
+ "./ffw64_rtxc/ffw/CChannelManager.cpp"
+ "./ffw64_rtxc/ffw/CController.cpp"
+ "./ffw64_rtxc/ffw/CExpandablePool.cpp"
+ "./ffw64_rtxc/ffw/CFifo.cpp"
+ "./ffw64_rtxc/ffw/CFilter.cpp"
+ "./ffw64_rtxc/ffw/CGPIOManager.cpp"
+ "./ffw64_rtxc/ffw/CHashTable.cpp"
+ "./ffw64_rtxc/ffw/CIPSynchro.cpp"
+ "./ffw64_rtxc/ffw/CInterruptBuffer.cpp"
+ "./ffw64_rtxc/ffw/CLatencyProfiler.cpp"
+ "./ffw64_rtxc/ffw/CList.cpp"
+ "./ffw64_rtxc/ffw/CLoggerInterProcessor.cpp"
+ "./ffw64_rtxc/ffw/CLoggerSharedBuffer.cpp"
+ "./ffw64_rtxc/ffw/CMMU.cpp"
+ "./ffw64_rtxc/ffw/CMMULoggerPA.cpp"
+ "./ffw64_rtxc/ffw/CMMULoggerVA.cpp"
+ "./ffw64_rtxc/ffw/CMultiFilter.cpp"
+ "./ffw64_rtxc/ffw/CObject.cpp"
+ "./ffw64_rtxc/ffw/CObjectTree.cpp"
+ "./ffw64_rtxc/ffw/CPipe.cpp"
+ "./ffw64_rtxc/ffw/CPool.cpp"
+ "./ffw64_rtxc/ffw/CRoot.cpp"
+ "./ffw64_rtxc/ffw/CSharedMemory.cpp"
+ "./ffw64_rtxc/ffw/CSignalPool.cpp"
+ "./ffw64_rtxc/ffw/CTerminalOut.cpp"
+ "./ffw64_rtxc/ffw/CTimeProfiler.cpp"
+ "./ffw64_rtxc/ffw/ffwCRC.cpp"
+ "./ffw64_rtxc/ffw/rtkit/CDebugAgent.cpp"
+ "./ffw64_rtxc/ffw/rtkit/CEnvironment.cpp"
+ "./ffw64_rtxc/ffw/rtkit/CISRManager.cpp"
+ "./ffw64_rtxc/ffw/rtkit/CMailboxPool.cpp"
+ "./ffw64_rtxc/ffw/rtkit/CQueuePool.cpp"
+ "./ffw64_rtxc/ffw/rtkit/CRTOSObjectPool.cpp"
+ "./ffw64_rtxc/ffw/rtkit/CResourcePool.cpp"
+ "./ffw64_rtxc/ffw/rtkit/CScopedLock.cpp"
+ "./ffw64_rtxc/ffw/rtkit/CSemaphorePool.cpp"
+ "./ffw64_rtxc/ffw/rtkit/CSharedMemoryHeap.cpp"
+ "./ffw64_rtxc/ffw/rtkit/CSharedMemoryHost.cpp"
+ "./ffw64_rtxc/ffw/rtkit/CTaskPool.cpp"
+ "./ffw64_rtxc/ffw/rtkit/CTimerManager.cpp"
+ "./ffw64_rtxc/ffw/rtkit/CTimerPool.cpp"
+ "./ffw64_rtxc/ffw/rtkit/CTraceEventBuffer.cpp"
+ "./ffw64_rtxc/ffw/rtkit/ffwSharedMemory.cpp"
+ "./ffw64_rtxc/platform/common/CFakeChannel.cpp"
+ "./ffw64_rtxc/platform/common/CIPSynchroFake.cpp"
+ "./ffw64_rtxc/platform/common/ChannelTable.cpp"
+ "./ffw64_rtxc/platform/common/FakeChannelTable.cpp"
+ "./ffw64_rtxc/platform/theia/rtkit/CPlatformEnvironment.cpp"
+ "./ffw64_rtxc/platform/theia/rtkit/CPlatformGPIOManager.cpp"
+ "./ffw64_rtxc/platform/theia/rtkit/CPlatformISRManager.cpp"
+ "./ffw64_rtxc/platform/theia/rtkit/RealChannelTableTarget.cpp"
+ "./sne/drivers/CDeviceDriver.cpp"
+ "./sne/drivers/FE/CConfigDrvH11.cpp"
+ "./sne/ssi/src/rtxc/sema.cpp"
+ "0 < mpGroupBufCnt[group]"
+ "0 == ((size_t)virtualAddr & wiringPageMask)"
+ "0 == (physicalAddr & wiringPageMask)"
+ "0 == matched || 1 == matched"
+ "0 == mpGroupBufCnt[group]"
+ "0 == ret"
+ "0/1"
+ "1"
+ "11:18:11"
+ "<=== CMMU_LOGGER_FFW_ASSERT from %s\n"
+ "===> CMMU_LOGGER_FFW_ASSERT from %s\n"
+ ">>>>>>> Frame ID mismatch, expect: %lld, get: %lld"
+ "ACK \"%s\""
+ "ACTION"
+ "AFPP load is not allowed after program setup done\n"
+ "ALIGN_DOWN(pointer, CMMU::CacheLineSize()) == pointer"
+ "ALL_CPU(%)"
+ "ANE in secure mode, request dropped for cacheHandler 0x%llx"
+ "ANE latency profiler already exists"
+ "ANE latency profiler created"
+ "ANE requestCallProc %zu"
+ "ANE_PROPERTY_PRC Channel related logs are disabled"
+ "ANE_PROPERTY_PRC Channel related logs are enabled"
+ "ANE_PROPERTY_PRC wrong valid"
+ "AddScheduleInfo"
+ "AneVersionGet"
+ "AvailableScheduleInfo"
+ "BAR[%d] barIndex %d : bufferIndex %d"
+ "Buf MSG: sapId 0x%x bufNbr %d subPacketSize %d\n"
+ "Buf[%d] sz %lld type %d"
+ "BufferProcessor"
+ "CAneDebugEventsManager"
+ "CAneServer"
+ "CBufferPool::alignment != 0"
+ "CBufferPool::blockArray != 0"
+ "CBufferPool::size != 0"
+ "CBufferPool::stride != 0"
+ "CDMEDIABUSMANAGER_ENDPOINT_CMD_PING == pCmd->hdr.cmd"
+ "CDMEDIABUSMANAGER_ENDPOINT_CMD_REMAP == pCmd->hdr.cmd"
+ "CDMEDIABUSMANAGER_ENDPOINT_CMD_SEND_BUF_MSG == pCmd->hdr.cmd"
+ "CDMEDIABUSMANAGER_ENDPOINT_CMD_UNMAP == pCmd->hdr.cmd"
+ "CDMediaBusManager"
+ "CExpandablePool allocEntryIdx enter"
+ "CExpandablePool allocEntryIdx exit idx %zu"
+ "CExpandablePool expandPool enter expand pool num %d, mCurrPoolNum %d "
+ "CExpandablePool expandPool exit mCurrPoolNum %d"
+ "CExpandablePool freeEntryIdx enter idx %zu RefCount %d"
+ "CExpandablePool freeEntryIdx exit idx %zu RefCount %d"
+ "CExpandablePool freeEntryIdx free poolIdx %d, mCurrPoolNum %d"
+ "CExpandablePool maximum pool num (%d) allowed already allocated"
+ "CExpandablePool retain enter idx %zu RefCount %d"
+ "CExpandablePool retain exit idx %zu RefCount %d"
+ "CFakeChannel::chDescr"
+ "CGPIOManager::Instance() != NULL"
+ "CMMULoggerPA::hisEntry != 0"
+ "CMMULoggerPA::logEntry != 0"
+ "CMMULoggerVA::hisEntry != 0"
+ "CMMULoggerVA::logEntry != 0"
+ "CMMU_LOGGER_FFW_ASSERT:%d [%zu] PA = 0x%lx, length = 0x%zx\n"
+ "CMMU_LOGGER_FFW_ASSERT:%d [%zu] vir = %p, length = 0x%zx\n"
+ "CMailboxPool::Instance() != 0"
+ "CPU num: %d\n"
+ "CPU_0(%)"
+ "CPU_1(%)"
+ "CPU_ID"
+ "CQueuePool::Instance() != 0"
+ "CRPCClient is down"
+ "CScopedLock"
+ "CSemaphorePool::Instance() != 0"
+ "CSharedMemory::Instance () != 0"
+ "CTaskPool::Instance() != 0"
+ "CTraceEventBuffer.cpp"
+ "CWorkTaskCore"
+ "CacheHandler (0x%llx) already removed from the list in the trigger ISR"
+ "CallProcedure"
+ "CallProcedure nbrOfCustomBars %d"
+ "CallProcedure progId %d procId %d numIoBuffers %d"
+ "CallProcedure progId %d procId %d numIoBuffers %d\n"
+ "CallProcedure2"
+ "ChannelCmd"
+ "ChannelStarted"
+ "ChannelStopped"
+ "Cleanup complete. mpDataChainingStat at %p deallocated"
+ "CmdAFPPLoad"
+ "CmdAFPPUnload"
+ "CmdAcknowledge"
+ "CmdCpuLoadNotification"
+ "CmdDataChainingEvent"
+ "CmdDbgEvent"
+ "CmdDsidEvent"
+ "CmdErrorNotification"
+ "CmdGetEndPointStatus"
+ "CmdGetOutstandingTicketCnt"
+ "CmdIpcEndpointSet"
+ "CmdIpcEndpointUnset"
+ "CmdIpcSharedMemoryFree"
+ "CmdIpcSharedMemoryMalloc"
+ "CmdPowerControl"
+ "CmdProcessor"
+ "CmdProgramEvent"
+ "CmdProgramSetup"
+ "CmdProgramUnsetup"
+ "CmdPropertyAccess"
+ "CmdRegSAP"
+ "CmdResetNotification"
+ "CmdSendBufMsg"
+ "CmdUnRegSAP"
+ "CpuLoadNotification"
+ "Create"
+ "Create,%lu,%s"
+ "Data Chaining Latency for cacheReqIdx %d"
+ "DataChainingProgramEvent"
+ "DataProcessor"
+ "DbgEvent"
+ "Dec 16 2024"
+ "Delete"
+ "Delete,%lu,%s"
+ "DeleteProgram"
+ "DepriorDsid"
+ "DirectPost"
+ "DriverCmdSanityCheck : off"
+ "DriverCmdSanityCheck : on"
+ "DriverCmdSanityCheck TD/overflow : off"
+ "DriverCmdSanityCheck TD/overflow : on"
+ "Dummy network NID %d TD Complete event %lld"
+ "Dummy network for NID %d TQ abort finished at %lld"
+ "DumpAFPP"
+ "EL"
+ "END"
+ "ENT: CFSM.cpp, "
+ "ENT: CScopedLock.cpp, "
+ "ENTER"
+ "EVENT_DISP options:"
+ "EXIT"
+ "EXT: CFSM.cpp, "
+ "EXT: CScopedLock.cpp, "
+ "Enable TQs after Dummy network finish in TQ[%d]"
+ "Enable TQs after letting TQ[%d] finish"
+ "EndPoint %d sends the Ping Message\n"
+ "EndPointUnset remap not by peer %d\n"
+ "EndpointCmdPing"
+ "EndpointCmdRemap"
+ "EndpointCmdSendBufMsg"
+ "EndpointCmdUnmap"
+ "Event %d nbrUsrD %d 22"
+ "EventProcess"
+ "FFWMSG_PAYLOAD_GET(pMsg) <= sizeof(struct ffwMsgBuffRef)"
+ "FFWMSG_PAYLOAD_GET(pMsg) <= sizeof(struct ffwMsgCmd)"
+ "FFWMSG_PAYLOAD_GET(pMsg) <= sizeof(struct ffwMsgData)"
+ "FFW_INTERPROC_BUFF_ACK_FLAG_CHECK(extra) != 0"
+ "FFW_INTERPROC_BUFF_EXCHANGE_FLAG_CHECK(param2)"
+ "FFW_OK == ffwrc"
+ "FSMSwitchNonSecure"
+ "FSMSwitchSecure"
+ "FSM_EVENT_EXELOOP_IN_SECURE"
+ "FSM_EVENT_EXELOOP_START"
+ "FSM_EVENT_EXELOOP_STOP"
+ "FSM_EVENT_EXELOOP_SWITCH_FROM_SECURE"
+ "FSM_EVENT_EXELOOP_SWITCH_TO_SECURE"
+ "FSM_STATE_EXELOOP_IDLE"
+ "FSM_STATE_EXELOOP_PAUSE"
+ "FSM_STATE_EXELOOP_RUN"
+ "FSM_STATE_EXELOOP_RUN_2_PAUSE"
+ "Failed to map command buffer"
+ "FileInfo %s failed"
+ "Filewrite %p %zu bytes"
+ "Filewrite %s %s"
+ "Force Disable already set"
+ "Generic : [%d] bufferIndex %d"
+ "GetCacheReqEvent"
+ "GetCmdBuf"
+ "GetDirectProcCallEvent"
+ "GetLastCommittedTDInfo"
+ "GetPowerStatus"
+ "GetProcInfo"
+ "GetProgInfo"
+ "GetTraceBuffer"
+ "H11ISPInterruptMapping[(size_t)aispSource]->platformIntSrc != PLATFORM_INT_INVALID"
+ "H17TunableManager"
+ "HandleEventInt"
+ "HandleMcwInt"
+ "HandleStopTqInt"
+ "Help"
+ "IDLE"
+ "IDLE_DEFAULT"
+ "ID_GET_SOURCE(id) < INTERRUPT_SRC_TOTAL"
+ "INVALID"
+ "IOP nothing to read"
+ "IOP read done: rtPtr %d wtPtr %d readCount %d"
+ "IOP read init: rtPtr %d wtPtr %d msgLen %zu"
+ "IOP wait for Read"
+ "IOP write done: rtPtr %d wtPtr %d writeCount %d"
+ "IOP write init: rtPtr %d wtPtr %d msgLen %zu (with header)"
+ "IOP write: Message length too big"
+ "IOP write: buffer overflow"
+ "IOP write: buffer wrapup"
+ "IOP write: pBuffer not initialized yet"
+ "IOP write: register 0x%zx 0x%x"
+ "ISR_ID_GET_BANK(id) < lines"
+ "ISR_ID_GET_INDEX(id) < ISR_CALLBACK_MAX"
+ "ISR_ID_GET_LINE(id) < ISR_REG_ENTRY"
+ "In SendSecureModeRequest()\n"
+ "Info"
+ "InitCacheRequest"
+ "InitProcedureCallCmds"
+ "InitProcedureCallCustomBarsCmds"
+ "Initialization"
+ "InqTaskArg"
+ "Invalid log operation"
+ "IpcEndpointSet"
+ "IpcEndpointUnset"
+ "ItqIrqEnable"
+ "Kernel : bufferIndex %d"
+ "KickStartCe"
+ "Load %s failed"
+ "LoadProgramsInAFPP"
+ "LogEnterVerbose"
+ "MapTextSection"
+ "Master asking to release the remap while it is still being used by local user\n"
+ "NO trace buffer to post!"
+ "NULL != clockToMicroSecondConvertFunc"
+ "NULL != encode_handler[encodeScheme]"
+ "NULL != entry"
+ "NULL != instance"
+ "NULL != nbytes"
+ "NULL != pCmd"
+ "NULL != pIpcRingBufferIn[pCmd->endPointId]"
+ "NULL != pIpcRingBufferOut[pCmd->endPointId]"
+ "NULL != pMsg"
+ "NULL != pResourceIndex[endPoint]"
+ "NULL != pResourceIndex[pCmd->endPointId]"
+ "NULL != pTaskHistoryHead"
+ "NULL != physical_addr"
+ "NULL != ppReadBufferAddr"
+ "NULL != ppWriteBufferAddr"
+ "NULL != semalist"
+ "NULL != semaphore"
+ "NULL != timeCodeGetFunc"
+ "NULL != timestampFrequencyFunc"
+ "NULL != virtualAddr"
+ "NULL == instance"
+ "NULL == mpGroups[group][j].buf && STATE_RELEASED == mpGroups[group][j].state"
+ "NULL == pHandler"
+ "NULL == pIpcRingBufferIn[pCmd->endPointId]"
+ "NULL == pIpcRingBufferOut[pCmd->endPointId]"
+ "Need dummy for TQ[%d]S[%d], b_queue_dummy_network %d"
+ "No output buffers are ready for cache request with cacheHandler 0x%llx"
+ "Notify score %u\n"
+ "Overflow detected in dram event log: programId %d processId %d procedureId %d"
+ "POST CONDITION: "
+ "POWEROFF"
+ "POWERON"
+ "PRE CONDITION: "
+ "PROCESSING"
+ "ParseTD"
+ "PerfMode : off"
+ "PerfMode : on"
+ "Performance"
+ "Phase %d: %dus (avg %9.6fus, std sq %9.6fus statsCount %d)"
+ "PiningThreadsTotal: "
+ "PostCallback"
+ "PostCmd"
+ "PowerControl"
+ "PowerDown"
+ "PowerUp"
+ "PowerUpByState"
+ "PreMapProcessStatsBuf"
+ "PrintBufDesc"
+ "PrintDescriptorProp"
+ "PrintGeneric"
+ "PrintKernelProp"
+ "PrintOperation"
+ "PrintProcedure"
+ "ProcessEndpointCmd"
+ "ProcessSubPacket"
+ "ProgramEvent"
+ "PropertyWrite"
+ "Queue dummy network using NID %d Q[%d]S[%d] at %lld"
+ "RESET"
+ "ROUND_DOWN(paddr, CMMU::CacheLineSize()) == paddr"
+ "RPC Id is 0x%x\n"
+ "RPC read file size as %zu"
+ "RTK_ST_IS_SUCCESS(rc)"
+ "RTK_queue_count(queue) == tot"
+ "RTK_vm_unmap failed\n"
+ "Read %s done %zu bytes"
+ "ReadMessage"
+ "Received Signal %p\n"
+ "Received an program whose has 0 operation : %d"
+ "Received an program whose procedure has invalid operation Index : %d vs %d"
+ "RegisterClient"
+ "ReloadTunables"
+ "Remap :  handle 0x%x : base %p : len 0x%lx\n"
+ "RemoveScheduleInfo"
+ "Report Debug Event : Debug Event %d count %d (tid:%d)"
+ "Reset"
+ "ReturnCacheReqEvent"
+ "ReturnDirectProcCallEvent"
+ "RunProc"
+ "RunProc2"
+ "RunProcCacheRequest"
+ "RunProcInternal"
+ "START"
+ "STOP"
+ "STREAM"
+ "STREAM_CMD_APPLY"
+ "STREAM_CMD_APPLY_NOW"
+ "STREAM_IDLE"
+ "STREAM_IDLE_DEFAULT"
+ "STREAM_INSTANDBY"
+ "STREAM_OFF"
+ "STREAM_PROCESSING"
+ "STREAM_RESET"
+ "STREAM_SETUP"
+ "STREAM_STANDBY"
+ "STREAM_START"
+ "STREAM_STOP"
+ "STREAM_TEARDOWN"
+ "SUCC"
+ "SVC"
+ "SaveProcedureCall"
+ "SaveRunToTdStop"
+ "SaveStatsBuffer"
+ "SaveToFile"
+ "Segment : bufferIndex %d"
+ "SendBufMsg"
+ "SendCall"
+ "SendHWRequest"
+ "SendMsg : endPointId %d sapId 0x%x subPacket %p subPacketSize %d\n"
+ "SendSecureModeRequest"
+ "SetPMUBaseAddress"
+ "SetProgram"
+ "SetTQState"
+ "Setting high watermark to %u\n"
+ "Setting low watermark to %u\n"
+ "Setting poll interval to %u seconds\n"
+ "Setting threshold to %u ticks\n"
+ "Setup complete. mpDataChainingStat at %p allocated"
+ "SetupEngineRequest"
+ "SetupExecute"
+ "Started"
+ "StatsBuf sz %lld type %d"
+ "Stopped"
+ "Suspend TQs for Dummy Network"
+ "SwitchExclaveMode"
+ "TD : bufferIndex %d"
+ "TQ[%d] reqRunningStatus 0x%x"
+ "Task"
+ "TaskArg not found"
+ "TearDownExecute"
+ "TerminateCacheRequest"
+ "TerminateProcess"
+ "Thread time"
+ "Total Abort : Raise Priority %d TQ Abort %d"
+ "Total Process create/terminate : %d/%d"
+ "Total Program add/delete       : %d/%d"
+ "Total Scheduled Run : %d (failed %d)"
+ "Total finished  Run : %d"
+ "TracePost2Host"
+ "TransitionProcess"
+ "Trigger input dropped: src 0x%x Surface Id 0x%x Offset 0x%llx"
+ "Trigger input fifo overflow. Dropped: src 0x%x Surface Id 0x%x Offset 0x%llx"
+ "UnMapTextSection"
+ "UnRemap :  handle 0x%x : base : %p len : 0x%lx\n"
+ "Unexpected"
+ "UnsetMem : %p 0x%lx 0x%x\n"
+ "UnsetRemap : %p 0x%lx 0x%x\n"
+ "WriteMessage"
+ "Writer regAddr 0x%lx regValue 0x%x\n"
+ "[%d]: intermediate spill bar id %d, dsid 0x%llx"
+ "[%d]: prefetch bar id %d, dsid 0x%llx"
+ "[%s]  CMD = %#04x [%s] at %lld : type = 0x%x addr = %p, size = %d \n"
+ "[%s] CMD = %#04x [%s] at %lld : enable=%d\n"
+ "[%s] CMD = %#04x [%s] at %lld [0x%x]\n"
+ "[0]: show options"
+ "[1]: TD events sorted by TID"
+ "[2]: TD events sorted by timestamp"
+ "[3]: TD performance profiling"
+ "[4]: show task switch event"
+ "[5]: network performance profiling"
+ "[ANE Exclave] Enter"
+ "[ANE Exclave] Exit"
+ "[ANE Power] down"
+ "[ANE Power] up"
+ "[AneCmd] Allocated processId %d for programId %d at %lld"
+ "[AneCmd] Allocated programId = %d at %lld"
+ "[AneCmd] Terminated processId %d for programId %d at %lld"
+ "[AneCmd] Unloaded programId = %d at %lld"
+ "[Desciptor prop Section] Total %d"
+ "[Descriptor prop Section] X"
+ "[Generic Section] X"
+ "[Generic Section] maxAneUsed %d maxNe %d total Buf %d"
+ "[Kernel Prop Section] Total %d"
+ "[Kernel Prop Section] X"
+ "[MessageBack] cmdId %d counter 0x%x - %dus (cache command # : %zu)"
+ "[No] Generic Section"
+ "[No] Operation Section"
+ "[No] Procedure Section"
+ "[No] Segment Prop Section"
+ "[No] Segment Section"
+ "[OPERATION Section] Total %d"
+ "[OPERATION Section] X"
+ "[POST] cmdId %d counter 0x%x"
+ "[POST] cmdId %d counter 0x%x => Trace # %d"
+ "[PROCEDURE Section] Total %d"
+ "[PROCEDURE Section] X"
+ "[TestCond] ASSERTION is set"
+ "[TestCond] Cmd_Timeout is set"
+ "[WRN] Exeloop cmd %d latency %dus"
+ "[X] kernelPropSection is valid but no buffer!"
+ "[X] kernelSection is valid but no buffer!"
+ "[X] verifyBAR"
+ "[X] verifyDescriptorPropSection"
+ "[X] verifyDescriptors"
+ "[X] verifyGenericSection"
+ "[X] verifyKernelPropSection"
+ "[X] verifyOperationSection"
+ "[X] verifyProcedureSection"
+ "[ipc] Send %llu"
+ "[ipc] callProc Cb %llu"
+ "[ipc] pCb %llu"
+ "_AneCallBack"
+ "_maskUnmaskMutex != (FFWMUTEX)0"
+ "actionbuf.bin"
+ "addDbgEvent"
+ "addEntry"
+ "addr != NULL"
+ "alignment != 0"
+ "allocDbgEventIdx"
+ "allocEntryIdx"
+ "allocL2SpillBufferIdx"
+ "allocatedPoolAddr[i] != NULL"
+ "array != 0"
+ "arrayEmptyBuffer != 0"
+ "array[index].ch != 0"
+ "array[index].ch == 0"
+ "array[index].inuse == false"
+ "available == tot"
+ "bGroupInUse[%d] %d"
+ "b_found == false"
+ "blockArray != 0"
+ "blocks <= CBuffer::idTot"
+ "bootArgs != 0"
+ "buf %d: addr 0x%llx size %lld"
+ "bufMsg->hdr.len <= sizeof(msg)"
+ "bufNbr <= maxAneIpcBufMsg"
+ "buffPointer"
+ "buffPool != 0"
+ "bufferLen == 0"
+ "bufferLen > sizeof(sIOPRingBuffer_t)"
+ "buffers != 0"
+ "buffers <= FFW_INTERPROC_BUFF_TOT"
+ "bundledBlocks <= CBuffer::idTot"
+ "bundledBlocksIn <= CBuffer::idTot"
+ "calcTriggerUsDelay"
+ "ch != 0"
+ "chMan != 0"
+ "chManH2T != 0"
+ "chTot <= ISP_CAMERA_CHANNEL_TOT"
+ "channel < inchannels"
+ "channelBufferSize != 0"
+ "channelPhys != 0"
+ "channelTotal != 0"
+ "channel_mem != NULL"
+ "checkBarEachAneOp"
+ "checkRunningSlotsAfterAbort"
+ "checkpointId < mMaxCheckpoints"
+ "cmdBuffer_mem != 0"
+ "cmdDataCheck"
+ "cmdInternalSema != (SEMA)0"
+ "cmdMbox != (MBOX)0"
+ "cmdMboxSema != (SEMA)0"
+ "cmdSema != (SEMA)0"
+ "cmdSynchronizationSema != (SEMA)0"
+ "context != NULL"
+ "count"
+ "create writeRingBufferLen %d with writeRingBufferAddr at 0x%lx %d\n"
+ "createCacheRequest"
+ "curEntry"
+ "dPrio != 0"
+ "dPrio % 2 == 0"
+ "dPrio <= 124"
+ "dPrio <= RTK_THREAD_PRIORITY_MAX"
+ "dPrio >= RTK_THREAD_PRIORITY_MIN"
+ "dataBufSize == pBuf->_header._size"
+ "dataChainingRecycleOutput"
+ "dataChainingTrigger"
+ "dataChainingTriggerIsr"
+ "decPendingExeLoopCmdCnt"
+ "deferredCmdAck == false"
+ "delay trigger[%lld]: execTimestamp %lld cmdHandleTimestamp %lld"
+ "deleteCacheRequest"
+ "depriorDsid"
+ "descr.indexList != 0"
+ "descr.list != 0"
+ "descr.lock != (FFWMUTEX)0"
+ "dieRequest != (SEMA)0"
+ "dieRequest != 0"
+ "dieSema != (SEMA)0"
+ "dispDataChainingLatency"
+ "duty : %u %\n"
+ "enableEventLogInNetworkDesc"
+ "endPoint < maxEndpoint"
+ "endPointCb[endPoint].shareMem.nbrOfRemapItem < sCDMediaBusManagerShareMemInfo::maxSharedMemInfo"
+ "endPointCb[i].curState < ECDMEDIABUSMANGER_ENDPOINT_CB_STATE_MAX"
+ "endPointCb[pCmd->endPointId].curState != ECDMEDIABUSMANGER_ENDPOINT_CB_STATE_IDLE"
+ "endPointCb[pCmd->endPointId].curState < ECDMEDIABUSMANGER_ENDPOINT_CB_STATE_MAX"
+ "endPointCb[pCmd->endPointId].shareMem.nbrOfItem"
+ "endPointCb[pCmd->endPointId].shareMem.nbrOfItem < sCDMediaBusManagerShareMemInfo::maxSharedMemInfo"
+ "endPointCb[pCmd->endPointId].shareMem.nbrOfItem == 0"
+ "endPointCb[pCmd->endPointId].shareMem.nbrOfRemapItem"
+ "endPointCb[pCmd->endPointId].shareMem.nbrOfRemapItem == 0"
+ "endPointCb[pCmd->endPointId].shareMem.remap[i].refCount==0"
+ "endPointId < maxEndpoint"
+ "entries != 0"
+ "entries > 0"
+ "entries_per_pool > 0"
+ "entry != 0"
+ "entry != NULL"
+ "entry->callback || entry->callback_with_source"
+ "entry->stack != 0"
+ "entry->used == true"
+ "entryList != 0"
+ "entry_size > 0"
+ "exe_interval(%)"
+ "execution(us)"
+ "expandPool"
+ "extra_heap_virt != NULL"
+ "ffwQueueCount (queue) == 0"
+ "ffwrc == FFW_OK"
+ "fileDescs[i].pData != nullptr"
+ "fileDescs[i].size == fileDescs[i].sizeRef"
+ "fileLen"
+ "fileWrite"
+ "filter == (class CObject *)0"
+ "fiq(us)"
+ "found"
+ "freeEntryIdx"
+ "freeL2SpillBuffIdx"
+ "freeUnusedL2SpillBufferPool"
+ "freeUnusedPool"
+ "func != 0"
+ "getActionProperty"
+ "getCacheReqPendingCmdCnt"
+ "getCacheReqState"
+ "getCacheRequestInfo"
+ "getCacheRequestIoBuffers"
+ "getCacheRequestIoBuffersNbr"
+ "getCacheRequestSignalEvents"
+ "getDataChainingInputInfo"
+ "getDirectAneRequestNetworkDesc"
+ "getFileSize"
+ "getL2SpillBufferAddr"
+ "getNbrOfTd"
+ "getProcedureCallType"
+ "getRequestId"
+ "gpTimerArray != 0"
+ "gpTimerArray[0] != 0"
+ "group < MAX_ASYNCBUFFERS_GROUPS"
+ "h"
+ "h != 0"
+ "h->ch != 0"
+ "h->chH2T != 0"
+ "h->chT2H != 0"
+ "h->managed == 0"
+ "h->signature == CFSM_SIGNATURE"
+ "h2tchIOMan != 0"
+ "handle != 0"
+ "handle != NULL"
+ "handleAbortCacheRequest"
+ "handleAbort_abortRaisePriority"
+ "handleCallProcedureWithBar"
+ "handleCmdChannel"
+ "handleDelayedTriggerCmd"
+ "handleInvalidSingleUseCacheRequest"
+ "handleIpcEndpointCmd"
+ "handlePendingCmd"
+ "handler == memHandler"
+ "handshake_info != NULL"
+ "hashNodeIdxMutex != (FFWMUTEX)0"
+ "hash_table_size > 0"
+ "head == 0"
+ "heap->addToPool(heapAddress, size) == RTK_ST_OK"
+ "heapSize != 0"
+ "heapVirt != NULL"
+ "heap_resource != (FFWMUTEX)0"
+ "heap_resource != 0"
+ "i <= 1000"
+ "id < max"
+ "id >= 0 && id < CDMEDIABUSMANAGER_CMD_COMMON_TOT"
+ "idx != 0"
+ "inUseList == 0"
+ "incPendingExeLoopCmdCnt"
+ "index < entries"
+ "index < tot"
+ "index == pEntry->parent"
+ "index >= 0"
+ "indexOfGroup < MAX_ASYNCBUFFERS_IN_GROUP"
+ "info.userData.f.b_queue_dummy_network == 1"
+ "initDbgEventMem"
+ "initSharedEvents"
+ "inputPipe != 0"
+ "inputPipeEnable != nullptr"
+ "insize != CCONTROLLER_INVALID_SHARED_INSIZE"
+ "insize == sizeof(struct sCSneCmdPrintEnable)"
+ "instance != 0"
+ "instance != NULL"
+ "instance == 0"
+ "instance == NULL"
+ "instance == nullptr"
+ "instance->ch != 0"
+ "instance->chT2H != 0"
+ "internalCmdListMutex_ != (FFWMUTEX)0"
+ "interrupt(us)"
+ "interruptTimerSignal != 0"
+ "iobuf0.bin"
+ "iobuf1.bin"
+ "iobuf2.bin"
+ "irqLine != 0"
+ "isAneIdle"
+ "isCacheReqInUse"
+ "isCacheReqValid"
+ "isHWReady"
+ "isrHandle"
+ "isrhandle != 0"
+ "it"
+ "list == 0"
+ "loadMonitorTask != RTK_THREAD_NONE"
+ "lock != (FFWMUTEX) 0"
+ "lock != nullptr"
+ "log != 0"
+ "logCmdData"
+ "logDepth > 0"
+ "logEntry"
+ "logRecvCmdAck"
+ "logTot <= logDepth"
+ "mLatencyStat.maxEntryNum > 0"
+ "mLatencyStat.pCheckpoint"
+ "mLatencyStat.pLatency"
+ "mLatencyStat.pLatency[i]"
+ "mMaxCheckpoints > 0"
+ "mMutex != (RESOURCE)0"
+ "mask cmd : address = 0x%x, actual address = 0x%x\n"
+ "mask cmd : reg addr = 0x%x, data = 0x%x"
+ "mask cmd : size = 0x%x\n"
+ "maskCount[aispSource] > 0"
+ "maxBuff != 0"
+ "max_hash_entries > 0"
+ "max_pool_num > 0 && max_pool_num <= MAX_EXPANDABLE_POOL_NUM"
+ "maxchannels != 0"
+ "maxmbox > 0"
+ "maxqueue > 1"
+ "maxres > 0"
+ "maxsema > 0"
+ "maxsig > 0"
+ "maxtask > 1"
+ "maxtimers > 0"
+ "mboxPool != 0"
+ "mboxPool == 0"
+ "memory != 0"
+ "message != NULL"
+ "messages > 0"
+ "mmu"
+ "mmuLoggerOn == true"
+ "mpEntryIdxRefCount"
+ "mpEntryIdxRefCount[idx] == 0"
+ "mpEntryIdxRefCount[idx] > 0"
+ "mpGroupBufCnt[%d] %d"
+ "mpGroupsOwnerName[%d] %s"
+ "mpPoolInfo"
+ "mpPoolInfo[mFirstUnusedPoolIdx].pIndexPool != NULL"
+ "mpPoolInfo[mFirstUnusedPoolIdx].pPoolBaseAddr == NULL"
+ "mpPoolInfo[poolIdx].pIndexPool != NULL"
+ "mpPoolInfo[poolIdx].valid != 0"
+ "msgHandler"
+ "msgLen > 0"
+ "msgPhys != 0"
+ "mutex != (FFWMUTEX) NULL"
+ "mutex != (RESOURCE) 0"
+ "myDbg"
+ "myProcCb"
+ "nBytes != NULL"
+ "name != 0"
+ "napCount == 0"
+ "nbrOfRemapLeft == endPointCb[pCmd->endPointId].shareMem.nbrOfRemapItem"
+ "newState < ECDMEDIABUSMANGER_ENDPOINT_CB_STATE_MAX"
+ "newTask != RTK_THREAD_NONE"
+ "new_end > new_start"
+ "newrdptr <= pBuf->_header._size"
+ "object != 0"
+ "object != NULL"
+ "ok == true"
+ "operationbuf.bin"
+ "outputAddr && outputSize"
+ "outputPipe != 0"
+ "outsize != 0"
+ "outstanding"
+ "outstanding <= entries"
+ "outstanding == 0"
+ "owner != 0"
+ "pAddr != NULL"
+ "pAneLatencyProfiler != __null"
+ "pBuf->_header._rdptr + sizeof(sIOPRingBufferMsgHeaderV2_t) < pBuf->_header._wrptr"
+ "pBuf->_header._rdptr + sizeof(sIOPRingBufferMsgHeader_t) < pBuf->_header._wrptr"
+ "pBufAddr && pBufSize && pBufIndex"
+ "pBufAddr[i] && pBufSize[i]"
+ "pBuffMsg->buffers <= FFW_INTERPROC_BUFF_TOT"
+ "pCmd != NULL"
+ "pCmd->bufNbr <= maxAneIpcBufMsg"
+ "pCmd->pSubPacket"
+ "pCmd->sharedMemIndex < sCDMediaBusManagerShareMemInfo::maxSharedMemInfo"
+ "pData"
+ "pEntry->parent != index"
+ "pEntry->parent < logDepth"
+ "pEntry->parent == index"
+ "pEntry->physicalAddr"
+ "pEntry->refCount"
+ "pEntry->virtualAddr"
+ "pExchange->buffers > 0"
+ "pInternalCmdArray_"
+ "pInternalCmdFreeList_"
+ "pInternalCmdList_"
+ "pItem->bufferRefCount"
+ "pItem->pBase == pCmd->sharedMemPtr"
+ "pItem->used"
+ "pMMULogger != NULL"
+ "pMMULogger == NULL"
+ "pMsg"
+ "pMsg != 0"
+ "pMyMsg->id == FFW_INTERPROC_MSG_EXCHANGE"
+ "pNodeData != NULL"
+ "pPoolAddrToFree[i] != NULL"
+ "pRingBuffer != 0"
+ "pSize != 0"
+ "pStride != 0"
+ "pSubPacket != NULL"
+ "pTemp"
+ "pTemp + pCmd->pBufSize[i] <= (size_t)pItem->pBase + pItem->memSize"
+ "pTemp >= (size_t)pItem->pBase && pTemp <= (size_t)pItem->pBase + pItem->memSize"
+ "pUserStr != 0"
+ "param1 >= sizeof(struct ffwInterProcMsg)"
+ "parent < logDepth"
+ "parent == logDepth"
+ "parent == pEntry->parent"
+ "parentEntry->child"
+ "parentEntry->physicalAddr"
+ "parentEntry->virtualAddr"
+ "parseOperation"
+ "parseProc"
+ "physicalAddr"
+ "physicalAddr != (uintptr_t) -1"
+ "pin < buffPools"
+ "pin < inputs"
+ "pin < outputs"
+ "pin < portInputs"
+ "pointer"
+ "pointer != 0"
+ "pointer != NULL"
+ "pointer == VP(messagePhys)"
+ "pool != (void *)0"
+ "pool != 0"
+ "pool == ALIGN_DOWN(pool, CMMU::CacheLineSize())"
+ "poolArray != 0"
+ "poolArray[container->attach.id] == 0"
+ "poolArray[id] != 0"
+ "poolBufferReceived != 0"
+ "poolBufferReturned != 0"
+ "poolIdx < mMaxPoolNum"
+ "poolIdx >= 0 && poolIdx < mMaxPoolNum"
+ "poolsizeIn >= CBufferPoolStatic::PoolSizeGet(buffers, newbundledBlocks, newsize, newalignment)"
+ "port < inports"
+ "powerUpAne"
+ "powerUpAneStage1"
+ "powerUpAneStage2"
+ "print"
+ "printCommandInfo"
+ "printInfo"
+ "printStats"
+ "priority != 0"
+ "priority <= RTK_THREAD_PRIORITY_MAX"
+ "priority >= RTK_THREAD_PRIORITY_MIN"
+ "processCmdOnly == true"
+ "processedCmdCounter == 0"
+ "processorEnter"
+ "processorExit"
+ "prog.tdProp.buf %p procValid %d"
+ "programId 0x%x processId 0x%x nbrAneMapping %d"
+ "programId 0x%x processId 0x%x procedureId 0x%x"
+ "propertyWrite"
+ "propertywrite 0x10A5 \x1b[32m1\x1b[39m : ANE stats"
+ "propertywrite 0x10A5 \x1b[32m2\x1b[39m : enable command detail"
+ "propertywrite 0x10A5 \x1b[32m3\x1b[39m : disable command detail"
+ "propertywrite 0x10A5 \x1b[32m4\x1b[39m : enable program info detail"
+ "propertywrite 0x10A5 \x1b[32m5\x1b[39m : disable program info detail"
+ "propertywrite 0x10A5 \x1b[32m6\x1b[39m : enable TD info detail"
+ "propertywrite 0x10A5 \x1b[32m7\x1b[39m : disable TD info detail"
+ "propertywrite 0x10A5 \x1b[32m8\x1b[39m : enable TD Header info"
+ "propertywrite 0x10A5 \x1b[32m9\x1b[39m : disable TD Header info"
+ "pushToHW"
+ "pushToHWDirect"
+ "queue != (FFWQUEUE)0"
+ "queueDepth > 1"
+ "queuePool != 0"
+ "queuePool == 0"
+ "rc != NULL"
+ "rc == 1"
+ "rc == RTK_ST_OK"
+ "rc >= 0"
+ "rdptr + sizeof(sIOPRingBufferMsgHeaderV2_t) < localCopyWrPtr"
+ "rdptr + sizeof(sIOPRingBufferMsgHeaderV2_t) < pBuf->_header._size"
+ "rdptr + sizeof(sIOPRingBufferMsgHeader_t) < localCopyWrPtr"
+ "rdptr + sizeof(sIOPRingBufferMsgHeader_t) < pBuf->_header._size"
+ "reader"
+ "recycleArray != 0"
+ "ref%d/%s"
+ "relocation cmd : X = 0x%x\n"
+ "relocation cmd : address = 0x%x, actual address = 0x%x\n"
+ "relocation cmd : barIdx = 0x%x\n"
+ "relocation cmd : dataHi = 0x%x"
+ "relocation cmd : dataLo = 0x%x"
+ "relocation cmd : size = 0x%x\n"
+ "reportDataChainingTriggerFailed"
+ "reportFinishEvent"
+ "reportStats"
+ "resPool != 0"
+ "resPool == 0"
+ "ret == 0"
+ "retain"
+ "retain == CBuffer::suspended"
+ "retainL2SpillBufferIdx"
+ "returnRequestId"
+ "rtkitSystemTaskList != 0"
+ "sCSneCmdProcedureCall [%d] : bufferIndex %d"
+ "saveToFile"
+ "sema != 0"
+ "sema != NULL"
+ "sema == 0"
+ "semaArray != (SEMA *)0"
+ "semaArray[index] != (SEMA)0"
+ "semaPool != 0"
+ "semaPool == 0"
+ "semaphore == (SEMA)0"
+ "semaphore == h->signalT2H"
+ "sequential cmd : address = 0x%x, actual address = 0x%x\n"
+ "sequential cmd : count = 0x%x\n"
+ "sequential cmd : reg addr = 0x%x, data = 0x%x"
+ "serialPollTimer[i] != 0"
+ "serialPortPoolTimeOut[i] != (SEMA)0"
+ "serialPortSignal[i] != (SEMA)0"
+ "set buf[%d] 0x%llx zero sz %lld"
+ "setAbortMode"
+ "setAbortMode %d"
+ "setCustomBars"
+ "setDataChainingLatencyDisp"
+ "setDataChainingLatencyDisp %d"
+ "setDirectAneRequestInfo"
+ "setEnableDynamicPowerGate"
+ "setForceDisableCacheRequest"
+ "setJobQueueId"
+ "setPerfMode"
+ "setResetMode"
+ "setResetMode %d"
+ "setStartTimestamp"
+ "setTaskSwitchEventDisp"
+ "setTaskSwitchEventDisp %d"
+ "setupCacheRequest"
+ "setupDirectProcCallEvents"
+ "shAddr != NULL"
+ "sharedEventsTrigger"
+ "sharedEventsTriggerIsr"
+ "sharedMem != 0"
+ "shwdStatus == 0"
+ "sigPool == 0"
+ "signal != 0"
+ "signalH2T != 0"
+ "signalResetNotification"
+ "signalSharedEvents"
+ "signalT2H != 0"
+ "size != 0"
+ "size <= sizeof(pBuffMsg->extra)"
+ "sizeInByte % 4 == 0"
+ "sizeInByte > 0"
+ "source < INT_NROF_VECTORS"
+ "source < ISR_REG_ENTRY"
+ "source < lines * ISR_REG_ENTRY"
+ "source >= 0"
+ "src != NULL"
+ "stacksize != 0"
+ "startInvalidateCacheRequestInExeLoop"
+ "started == false"
+ "statsBufferSizeGet"
+ "status == FFW_OK"
+ "status == RTK_ST_OK"
+ "super::Available() == (int)super::Managed()"
+ "switchToIsolatedMode"
+ "syncCmdMutex_ != (FFWMUTEX)0"
+ "synchronization != (SEMA)0"
+ "synchronize != (SEMA)0"
+ "task != (TASK)0"
+ "task != 0"
+ "taskId == self"
+ "taskPool == 0"
+ "taskTime != 0"
+ "td size %zu while usedSize %d"
+ "temp != 0"
+ "this->buffers >= buffers"
+ "threadHistoryLock != (FFWMUTEX) 0"
+ "ticket < cmdDepth"
+ "timerHandle != NULL"
+ "timerSem != NULL"
+ "token != 0"
+ "tot != 0"
+ "tot == 0"
+ "tot > 0"
+ "totalElapsed %lld or totalElapsedInterval %lld is invalid value\n"
+ "totalElapsed(from tracekit) %lld, totalElapsedDuringCheckpoint %lld\n"
+ "totalElapsedInterval(from tracekit) %lld, totalElapsedIntervalDuringCheckpoint %lld\n"
+ "tree_resource != (FFWMUTEX)0"
+ "tree_resource != 0"
+ "unknown TD command type 0x%x"
+ "updateAndEnqueueOneSegment"
+ "updateDefSetting"
+ "updateEngineRequestSegment"
+ "updateStatsBufferData"
+ "vPrintLock != (SEMA)0"
+ "vPrintLock == (SEMA)NULL"
+ "value != NULL"
+ "verifyBAR"
+ "verifyCustomBar"
+ "verifyDescriptorPropSection"
+ "verifyDescriptors"
+ "verifyGenericSection"
+ "verifyKernelPropSection"
+ "verifyOperationSection"
+ "verifyProcedure"
+ "verifyProcedureSection"
+ "verifyProgram"
+ "virtualAddr"
+ "virtualAddr != NULL"
+ "waitTQIdle"
+ "wiringPageSize == 0x4000"
+ "write to overwrite ref%d/%s"
+ "~CScopedLock"
- "%s .Sanity check failure!\n"
- "01:26:27"
- "Couldn't find ShareMemInfoItem to free !!!\n"
- "Dec  6 2024"
- "IPC Endpoint cmd failed %d"
- "IPC Endpoint cmd failure"
- "Procedure %d exceeded maximum for program %d"
- "Run out of CSharedMemory !!!\n"
- "pProc != __null"
- "pProg != __null"
- "unremap WriteMessage failed\n"

```

#### securem3fw-d9x.im4p

>  `securem3fw-d9x.im4p`

```diff

 
-  __TEXT.__text: 0x1281c
+  __TEXT.__text: 0x12818
   __TEXT.__const: 0x2dc0
-  __TEXT.__cstring: 0x16d1
+  __TEXT.__cstring: 0x16d9
   __TEXT.__constructor: 0x0
   __TEXT._rtk_mtab: 0xc0
   __TEXT.__rtk_vtor: 0x254

   __DATA.__zerofill: 0xedc4
   Functions: 0
   Symbols:   0
-  CStrings:  52
+  CStrings:  53
 
CStrings:
+ "11:15:23"
+ "3.408"
+ "Dec 16 2024"
- "01:25:56"
- "Dec  6 2024"

```

#### sptm.t8140.release.im4p

>  `sptm.t8140.release.im4p`

```diff

-392.80.2.0.0
+392.80.3.0.0
   __TEXT.__cstring: 0xd98c
   __TEXT.__binname: 0x40
   __TEXT.__chain_starts: 0x70
   __TEXT.__const: 0xa10
   __DATA_CONST.__const: 0x5d38
   __LATE_CONST.__late_const: 0x5d640
-  __TEXT_EXEC.__text: 0x4aee0
+  __TEXT_EXEC.__text: 0x4b2d4
   __LAST.__pinst: 0x8
   __DATA.__auth_ptr: 0x18
   __DATA.__data: 0x6

```


</details>

## DSC

### WebKit

| iOS               | Version     |
| :---------------- | :---------- |
| 18.3 *(22D5034e)* | 620.2.2.0.0 |
| 18.3 *(22D5040d)* | 620.2.3.0.0 |

### Dylibs

#### ⬆️ Updated (750)

<details>
  <summary><i>View Updated</i></summary>

- [/System/Library/AccessibilityBundles/ControlCenterUIKit.axbundle/ControlCenterUIKit](DYLIBS/ControlCenterUIKit.md)
- [/System/Library/AccessibilityBundles/MobilePhone.axbundle/MobilePhone](DYLIBS/MobilePhone.md)
- [/System/Library/AccessibilityBundles/SpringBoard.axbundle/SpringBoard](DYLIBS/SpringBoard.md)
- [/System/Library/Accounts/Notification/CloudKitNotificationPlugin.bundle/CloudKitNotificationPlugin](DYLIBS/CloudKitNotificationPlugin.md)
- [/System/Library/Assistant/UIPlugins/SiriFindMyUIPlugin.siriUIBundle/Frameworks/SiriFindMyUI.framework/SiriFindMyUI](DYLIBS/SiriFindMyUI.md)
- [/System/Library/CoreAccessories/PlugIns/Transports/IOAccessoryManager.transport/IOAccessoryManager](DYLIBS/IOAccessoryManager.md)
- [/System/Library/Frameworks/AVKit.framework/AVKit](DYLIBS/AVKit.md)
- [/System/Library/Frameworks/AppIntents.framework/AppIntents](DYLIBS/AppIntents.md)
- [/System/Library/Frameworks/Assignables.framework/Assignables](DYLIBS/Assignables.md)
- [/System/Library/Frameworks/AudioToolbox.framework/AudioCodecs](DYLIBS/AudioCodecs.md)
- [/System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/Frameworks/AACClient.framework/AACClient](DYLIBS/AACClient.md)
- [/System/Library/Frameworks/BrowserEngineKit.framework/BrowserEngineKit](DYLIBS/BrowserEngineKit.md)
- [/System/Library/Frameworks/CFNetwork.framework/CFNetwork](DYLIBS/CFNetwork.md)
- [/System/Library/Frameworks/Charts.framework/Charts](DYLIBS/Charts.md)
- [/System/Library/Frameworks/CloudKit.framework/CloudKit](DYLIBS/CloudKit.md)
- [/System/Library/Frameworks/Combine.framework/Combine](DYLIBS/Combine.md)
- [/System/Library/Frameworks/ContactsUI.framework/ContactsUI](DYLIBS/ContactsUI.md)
- [/System/Library/Frameworks/CoreAudio.framework/CoreAudio](DYLIBS/CoreAudio.md)
- [/System/Library/Frameworks/CoreAudioKit.framework/CoreAudioKit](DYLIBS/CoreAudioKit.md)
- [/System/Library/Frameworks/CoreData.framework/CoreData](DYLIBS/CoreData.md)
- [/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation](DYLIBS/CoreFoundation.md)
- [/System/Library/Frameworks/CoreGraphics.framework/CoreGraphics](DYLIBS/CoreGraphics.md)
- [/System/Library/Frameworks/CoreHaptics.framework/CoreHaptics](DYLIBS/CoreHaptics.md)
- [/System/Library/Frameworks/CoreLocation.framework/CoreLocation](DYLIBS/CoreLocation.md)
- [/System/Library/Frameworks/CoreML.framework/CoreML](DYLIBS/CoreML.md)
- [/System/Library/Frameworks/CoreMedia.framework/CoreMedia](DYLIBS/CoreMedia.md)
- [/System/Library/Frameworks/CoreMotion.framework/CoreMotion](DYLIBS/CoreMotion.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight](DYLIBS/CoreSpotlight.md)
- [/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony](DYLIBS/CoreTelephony.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/CTParser.framework/CTParser](DYLIBS/CTParser.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterBase.dylib](DYLIBS/libCommCenterBase.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterCommandDrivers.dylib](DYLIBS/libCommCenterCommandDrivers.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterKCommandDrivers.dylib](DYLIBS/libCommCenterKCommandDrivers.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterMCommandDrivers.dylib](DYLIBS/libCommCenterMCommandDrivers.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libSystemDetermination.dylib](DYLIBS/libSystemDetermination.dylib.md)
- [/System/Library/Frameworks/CoreTransferable.framework/CoreTransferable](DYLIBS/CoreTransferable.md)
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
- [/System/Library/Frameworks/GroupActivities.framework/GroupActivities](DYLIBS/GroupActivities.md)
- [/System/Library/Frameworks/HomeKit.framework/HomeKit](DYLIBS/HomeKit.md)
- [/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit](DYLIBS/IOKit.md)
- [/System/Library/Frameworks/ImageCaptureCore.framework/ImageCaptureCore](DYLIBS/ImageCaptureCore.md)
- [/System/Library/Frameworks/ImageIO.framework/ImageIO](DYLIBS/ImageIO.md)
- [/System/Library/Frameworks/ImagePlayground.framework/ImagePlayground](DYLIBS/ImagePlayground.md)
- [/System/Library/Frameworks/JavaScriptCore.framework/JavaScriptCore](DYLIBS/JavaScriptCore.md)
- [/System/Library/Frameworks/LightweightCodeRequirements.framework/LightweightCodeRequirements](DYLIBS/LightweightCodeRequirements.md)
- [/System/Library/Frameworks/LiveCommunicationKit.framework/LiveCommunicationKit](DYLIBS/LiveCommunicationKit.md)
- [/System/Library/Frameworks/LockedCameraCapture.framework/LockedCameraCapture](DYLIBS/LockedCameraCapture.md)
- [/System/Library/Frameworks/MapKit.framework/MapKit](DYLIBS/MapKit.md)
- [/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox](DYLIBS/MediaToolbox.md)
- [/System/Library/Frameworks/MusicKit.framework/MusicKit](DYLIBS/MusicKit.md)
- [/System/Library/Frameworks/Network.framework/Network](DYLIBS/Network.md)
- [/System/Library/Frameworks/NetworkExtension.framework/NetworkExtension](DYLIBS/NetworkExtension.md)
- [/System/Library/Frameworks/PencilKit.framework/PencilKit](DYLIBS/PencilKit.md)
- [/System/Library/Frameworks/ProximityReader.framework/ProximityReader](DYLIBS/ProximityReader.md)
- [/System/Library/Frameworks/QuickLook.framework/QuickLook](DYLIBS/QuickLook.md)
- [/System/Library/Frameworks/QuickLookThumbnailing.framework/QuickLookThumbnailing](DYLIBS/QuickLookThumbnailing.md)
- [/System/Library/Frameworks/RealityFoundation.framework/RealityFoundation](DYLIBS/RealityFoundation.md)
- [/System/Library/Frameworks/RealityKit.framework/RealityKit](DYLIBS/RealityKit.md)
- [/System/Library/Frameworks/RoomPlan.framework/RoomPlan](DYLIBS/RoomPlan.md)
- [/System/Library/Frameworks/SafariServices.framework/SafariServices](DYLIBS/SafariServices.md)
- [/System/Library/Frameworks/SceneKit.framework/SceneKit](DYLIBS/SceneKit.md)
- [/System/Library/Frameworks/SoundAnalysis.framework/SoundAnalysis](DYLIBS/SoundAnalysis.md)
- [/System/Library/Frameworks/Speech.framework/Speech](DYLIBS/Speech.md)
- [/System/Library/Frameworks/StickerKit.framework/StickerKit](DYLIBS/StickerKit.md)
- [/System/Library/Frameworks/StoreKit.framework/StoreKit](DYLIBS/StoreKit.md)
- [/System/Library/Frameworks/SwiftData.framework/SwiftData](DYLIBS/SwiftData.md)
- [/System/Library/Frameworks/SwiftUI.framework/SwiftUI](DYLIBS/SwiftUI.md)
- [/System/Library/Frameworks/SwiftUICore.framework/SwiftUICore](DYLIBS/SwiftUICore.md)
- [/System/Library/Frameworks/TabularData.framework/TabularData](DYLIBS/TabularData.md)
- [/System/Library/Frameworks/TipKit.framework/TipKit](DYLIBS/TipKit.md)
- [/System/Library/Frameworks/UIKit.framework/UIKit](DYLIBS/UIKit.md)
- [/System/Library/Frameworks/VideoToolbox.framework/VideoToolbox](DYLIBS/VideoToolbox.md)
- [/System/Library/Frameworks/Vision.framework/Vision](DYLIBS/Vision.md)
- [/System/Library/Frameworks/WeatherKit.framework/WeatherKit](DYLIBS/WeatherKit.md)
- [/System/Library/Frameworks/WebKit.framework/WebKit](DYLIBS/WebKit.md)
- [/System/Library/Frameworks/WidgetKit.framework/WidgetKit](DYLIBS/WidgetKit.md)
- [/System/Library/Frameworks/WorkoutKit.framework/WorkoutKit](DYLIBS/WorkoutKit.md)
- [/System/Library/Frameworks/_GroupActivities_UIKit.framework/_GroupActivities_UIKit](DYLIBS/_GroupActivities_UIKit.md)
- [/System/Library/Frameworks/_ManagedAppDistribution_SwiftUI.framework/_ManagedAppDistribution_SwiftUI](DYLIBS/_ManagedAppDistribution_SwiftUI.md)
- [/System/Library/Frameworks/_MapKit_SwiftUI.framework/_MapKit_SwiftUI](DYLIBS/_MapKit_SwiftUI.md)
- [/System/Library/Frameworks/_MusicKit_SwiftUI.framework/_MusicKit_SwiftUI](DYLIBS/_MusicKit_SwiftUI.md)
- [/System/Library/Frameworks/_RealityKit_SwiftUI.framework/_RealityKit_SwiftUI](DYLIBS/_RealityKit_SwiftUI.md)
- [/System/Library/Frameworks/_StoreKit_SwiftUI.framework/_StoreKit_SwiftUI](DYLIBS/_StoreKit_SwiftUI.md)
- [/System/Library/Frameworks/_SwiftData_SwiftUI.framework/_SwiftData_SwiftUI](DYLIBS/_SwiftData_SwiftUI.md)
- [/System/Library/Frameworks/_Translation_SwiftUI.framework/_Translation_SwiftUI](DYLIBS/_Translation_SwiftUI.md)
- [/System/Library/Health/FeedItemPlugins/HearingAppPlugin.healthplugin/HearingAppPlugin](DYLIBS/HearingAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/Heart.healthplugin/Heart](DYLIBS/Heart.md)
- [/System/Library/Health/FeedItemPlugins/HighlightAlerts.healthplugin/HighlightAlerts](DYLIBS/HighlightAlerts.md)
- [/System/Library/Health/FeedItemPlugins/Highlights.healthplugin/Highlights](DYLIBS/Highlights.md)
- [/System/Library/Health/FeedItemPlugins/MedicationsHealthAppPlugin.healthplugin/MedicationsHealthAppPlugin](DYLIBS/MedicationsHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/MenstrualCyclesAppPlugin.healthplugin/MenstrualCyclesAppPlugin](DYLIBS/MenstrualCyclesAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/MentalHealthAppPlugin.healthplugin/MentalHealthAppPlugin](DYLIBS/MentalHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/RespiratoryHealthAppPlugin.healthplugin/RespiratoryHealthAppPlugin](DYLIBS/RespiratoryHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/SleepHealthAppPlugin.healthplugin/SleepHealthAppPlugin](DYLIBS/SleepHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/Summaries.healthplugin/Summaries](DYLIBS/Summaries.md)
- [/System/Library/Health/FeedItemPlugins/VisionHealthAppPlugin.healthplugin/VisionHealthAppPlugin](DYLIBS/VisionHealthAppPlugin.md)
- [/System/Library/MediaCapture/H16ISP.mediacapture](DYLIBS/H16ISP.mediacapture.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/WeatherComplications.bundle/WeatherComplications](DYLIBS/WeatherComplications.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKEsterbrookFaceBundleCompanion.bundle/NTKEsterbrookFaceBundleCompanion](DYLIBS/NTKEsterbrookFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKRhizomeFaceBundleCompanion.bundle/NTKRhizomeFaceBundleCompanion](DYLIBS/NTKRhizomeFaceBundleCompanion.md)
- [/System/Library/Previews/ShellPlugins/WidgetPreviewsShellPlugin.bundle/WidgetPreviewsShellPlugin](DYLIBS/WidgetPreviewsShellPlugin.md)
- [/System/Library/PrivateFrameworks/ABMHelper.framework/ABMHelper](DYLIBS/ABMHelper.md)
- [/System/Library/PrivateFrameworks/AIMLExperimentationAnalytics.framework/AIMLExperimentationAnalytics](DYLIBS/AIMLExperimentationAnalytics.md)
- [/System/Library/PrivateFrameworks/AIMLInstrumentationStreams.framework/AIMLInstrumentationStreams](DYLIBS/AIMLInstrumentationStreams.md)
- [/System/Library/PrivateFrameworks/APFoundation.framework/APFoundation](DYLIBS/APFoundation.md)
- [/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture](DYLIBS/AVFCapture.md)
- [/System/Library/PrivateFrameworks/AXAssetLoader.framework/AXAssetLoader](DYLIBS/AXAssetLoader.md)
- [/System/Library/PrivateFrameworks/AXSoundDetectionUI.framework/AXSoundDetectionUI](DYLIBS/AXSoundDetectionUI.md)
- [/System/Library/PrivateFrameworks/AccessibilityPhysicalInteraction.framework/AccessibilityPhysicalInteraction](DYLIBS/AccessibilityPhysicalInteraction.md)
- [/System/Library/PrivateFrameworks/AccessibilitySettingsUI.framework/AccessibilitySettingsUI](DYLIBS/AccessibilitySettingsUI.md)
- [/System/Library/PrivateFrameworks/AccessibilitySharedUISupport.framework/AccessibilitySharedUISupport](DYLIBS/AccessibilitySharedUISupport.md)
- [/System/Library/PrivateFrameworks/AccountsDaemon.framework/AccountsDaemon](DYLIBS/AccountsDaemon.md)
- [/System/Library/PrivateFrameworks/AccountsUISettings.framework/AccountsUISettings](DYLIBS/AccountsUISettings.md)
- [/System/Library/PrivateFrameworks/ActionButtonConfigurationUI.framework/ActionButtonConfigurationUI](DYLIBS/ActionButtonConfigurationUI.md)
- [/System/Library/PrivateFrameworks/ActionKit.framework/ActionKit](DYLIBS/ActionKit.md)
- [/System/Library/PrivateFrameworks/ActionKitUI.framework/ActionKitUI](DYLIBS/ActionKitUI.md)
- [/System/Library/PrivateFrameworks/ActivityAwardsCore.framework/ActivityAwardsCore](DYLIBS/ActivityAwardsCore.md)
- [/System/Library/PrivateFrameworks/ActivitySharingServices.framework/ActivitySharingServices](DYLIBS/ActivitySharingServices.md)
- [/System/Library/PrivateFrameworks/ActivitySharingUI.framework/ActivitySharingUI](DYLIBS/ActivitySharingUI.md)
- [/System/Library/PrivateFrameworks/ActivityUIServices.framework/ActivityUIServices](DYLIBS/ActivityUIServices.md)
- [/System/Library/PrivateFrameworks/AdaptiveVoiceShortcuts.framework/AdaptiveVoiceShortcuts](DYLIBS/AdaptiveVoiceShortcuts.md)
- [/System/Library/PrivateFrameworks/AirDropSettingsSupport.framework/AirDropSettingsSupport](DYLIBS/AirDropSettingsSupport.md)
- [/System/Library/PrivateFrameworks/AirPlayKit.framework/AirPlayKit](DYLIBS/AirPlayKit.md)
- [/System/Library/PrivateFrameworks/Anvil.framework/Anvil](DYLIBS/Anvil.md)
- [/System/Library/PrivateFrameworks/AppAnalytics.framework/AppAnalytics](DYLIBS/AppAnalytics.md)
- [/System/Library/PrivateFrameworks/AppIntentsServices.framework/AppIntentsServices](DYLIBS/AppIntentsServices.md)
- [/System/Library/PrivateFrameworks/AppPlaceholderSync.framework/AppPlaceholderSync](DYLIBS/AppPlaceholderSync.md)
- [/System/Library/PrivateFrameworks/AppPredictionInternal.framework/AppPredictionInternal](DYLIBS/AppPredictionInternal.md)
- [/System/Library/PrivateFrameworks/AppProtection.framework/AppProtection](DYLIBS/AppProtection.md)
- [/System/Library/PrivateFrameworks/AppProtectionUI.framework/AppProtectionUI](DYLIBS/AppProtectionUI.md)
- [/System/Library/PrivateFrameworks/AppSSO.framework/AppSSO](DYLIBS/AppSSO.md)
- [/System/Library/PrivateFrameworks/AppServerSupport.framework/AppServerSupport](DYLIBS/AppServerSupport.md)
- [/System/Library/PrivateFrameworks/AppStoreComponents.framework/AppStoreComponents](DYLIBS/AppStoreComponents.md)
- [/System/Library/PrivateFrameworks/AppStoreKitInternal.framework/AppStoreKitInternal](DYLIBS/AppStoreKitInternal.md)
- [/System/Library/PrivateFrameworks/AppSupport.framework/AppSupport](DYLIBS/AppSupport.md)
- [/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount](DYLIBS/AppleAccount.md)
- [/System/Library/PrivateFrameworks/AppleAccountUI.framework/AppleAccountUI](DYLIBS/AppleAccountUI.md)
- [/System/Library/PrivateFrameworks/AppleBasebandServices.framework/AppleBasebandServices](DYLIBS/AppleBasebandServices.md)
- [/System/Library/PrivateFrameworks/AppleCareSupport.framework/AppleCareSupport](DYLIBS/AppleCareSupport.md)
- [/System/Library/PrivateFrameworks/AppleIDSetup.framework/AppleIDSetup](DYLIBS/AppleIDSetup.md)
- [/System/Library/PrivateFrameworks/AppleIDSetupDaemon.framework/AppleIDSetupDaemon](DYLIBS/AppleIDSetupDaemon.md)
- [/System/Library/PrivateFrameworks/AppleIDSetupUI.framework/AppleIDSetupUI](DYLIBS/AppleIDSetupUI.md)
- [/System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore](DYLIBS/AppleKeyStore.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices](DYLIBS/AppleMediaServices.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/AppleMediaServicesUI](DYLIBS/AppleMediaServicesUI.md)
- [/System/Library/PrivateFrameworks/ApplePDPHelper.framework/ApplePDPHelper](DYLIBS/ApplePDPHelper.md)
- [/System/Library/PrivateFrameworks/ArgumentParserInternal.framework/ArgumentParserInternal](DYLIBS/ArgumentParserInternal.md)
- [/System/Library/PrivateFrameworks/AskToCore.framework/AskToCore](DYLIBS/AskToCore.md)
- [/System/Library/PrivateFrameworks/AssertionServices.framework/AssertionServices](DYLIBS/AssertionServices.md)
- [/System/Library/PrivateFrameworks/AssetViewer.framework/AssetViewer](DYLIBS/AssetViewer.md)
- [/System/Library/PrivateFrameworks/AssistantSettingsSupport.framework/AssistantSettingsSupport](DYLIBS/AssistantSettingsSupport.md)
- [/System/Library/PrivateFrameworks/AssistantUI.framework/AssistantUI](DYLIBS/AssistantUI.md)
- [/System/Library/PrivateFrameworks/AudioAnalytics.framework/AudioAnalytics](DYLIBS/AudioAnalytics.md)
- [/System/Library/PrivateFrameworks/AudioAnalyticsBase.framework/AudioAnalyticsBase](DYLIBS/AudioAnalyticsBase.md)
- [/System/Library/PrivateFrameworks/AudioAnalyticsExternal.framework/AudioAnalyticsExternal](DYLIBS/AudioAnalyticsExternal.md)
- [/System/Library/PrivateFrameworks/AudioServerDriverTransports_Base.framework/AudioServerDriverTransports_Base](DYLIBS/AudioServerDriverTransports_Base.md)
- [/System/Library/PrivateFrameworks/AudioServerDriverTransports_IOA2.framework/AudioServerDriverTransports_IOA2](DYLIBS/AudioServerDriverTransports_IOA2.md)
- [/System/Library/PrivateFrameworks/AudioServerDriverTransports_IOP.framework/AudioServerDriverTransports_IOP](DYLIBS/AudioServerDriverTransports_IOP.md)
- [/System/Library/PrivateFrameworks/AudioSessionServer.framework/AudioSessionServer](DYLIBS/AudioSessionServer.md)
- [/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore](DYLIBS/AudioToolboxCore.md)
- [/System/Library/PrivateFrameworks/AuthenticationServicesCore.framework/AuthenticationServicesCore](DYLIBS/AuthenticationServicesCore.md)
- [/System/Library/PrivateFrameworks/BasebandTraceHelper.framework/BasebandTraceHelper](DYLIBS/BasebandTraceHelper.md)
- [/System/Library/PrivateFrameworks/BatteryCenterUI.framework/BatteryCenterUI](DYLIBS/BatteryCenterUI.md)
- [/System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary](DYLIBS/BiomeLibrary.md)
- [/System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams](DYLIBS/BiomeStreams.md)
- [/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI](DYLIBS/BiometricKitUI.md)
- [/System/Library/PrivateFrameworks/Blackbeard.framework/Blackbeard](DYLIBS/Blackbeard.md)
- [/System/Library/PrivateFrameworks/BlastDoor.framework/BlastDoor](DYLIBS/BlastDoor.md)
- [/System/Library/PrivateFrameworks/BookDataStore.framework/BookDataStore](DYLIBS/BookDataStore.md)
- [/System/Library/PrivateFrameworks/BrailleSymbology.framework/BrailleSymbology](DYLIBS/BrailleSymbology.md)
- [/System/Library/PrivateFrameworks/BridgePreferences.framework/BridgePreferences](DYLIBS/BridgePreferences.md)
- [/System/Library/PrivateFrameworks/CAFCombine.framework/CAFCombine](DYLIBS/CAFCombine.md)
- [/System/Library/PrivateFrameworks/CAFUI.framework/CAFUI](DYLIBS/CAFUI.md)
- [/System/Library/PrivateFrameworks/CDMFoundation.framework/CDMFoundation](DYLIBS/CDMFoundation.md)
- [/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture](DYLIBS/CMCapture.md)
- [/System/Library/PrivateFrameworks/CMCaptureCore.framework/CMCaptureCore](DYLIBS/CMCaptureCore.md)
- [/System/Library/PrivateFrameworks/CTCarrierSpace.framework/CTCarrierSpace](DYLIBS/CTCarrierSpace.md)
- [/System/Library/PrivateFrameworks/CTLazuliSupport.framework/CTLazuliSupport](DYLIBS/CTLazuliSupport.md)
- [/System/Library/PrivateFrameworks/Calculate.framework/Calculate](DYLIBS/Calculate.md)
- [/System/Library/PrivateFrameworks/CalculateUI.framework/CalculateUI](DYLIBS/CalculateUI.md)
- [/System/Library/PrivateFrameworks/CalendarDaemon.framework/CalendarDaemon](DYLIBS/CalendarDaemon.md)
- [/System/Library/PrivateFrameworks/CalendarIntegrationSupport.framework/CalendarIntegrationSupport](DYLIBS/CalendarIntegrationSupport.md)
- [/System/Library/PrivateFrameworks/CalendarUIKit.framework/CalendarUIKit](DYLIBS/CalendarUIKit.md)
- [/System/Library/PrivateFrameworks/CalendarWidget.framework/CalendarWidget](DYLIBS/CalendarWidget.md)
- [/System/Library/PrivateFrameworks/CallHistory.framework/CallHistory](DYLIBS/CallHistory.md)
- [/System/Library/PrivateFrameworks/CameraColorProcessing.framework/CameraColorProcessing](DYLIBS/CameraColorProcessing.md)
- [/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI](DYLIBS/CameraUI.md)
- [/System/Library/PrivateFrameworks/CarPlayAssetUI.framework/CarPlayAssetUI](DYLIBS/CarPlayAssetUI.md)
- [/System/Library/PrivateFrameworks/CellularPlanManager.framework/CellularPlanManager](DYLIBS/CellularPlanManager.md)
- [/System/Library/PrivateFrameworks/ChatKit.framework/ChatKit](DYLIBS/ChatKit.md)
- [/System/Library/PrivateFrameworks/Chirp.framework/Chirp](DYLIBS/Chirp.md)
- [/System/Library/PrivateFrameworks/ChronoCore.framework/ChronoCore](DYLIBS/ChronoCore.md)
- [/System/Library/PrivateFrameworks/ChronoKit.framework/ChronoKit](DYLIBS/ChronoKit.md)
- [/System/Library/PrivateFrameworks/ChronoServices.framework/ChronoServices](DYLIBS/ChronoServices.md)
- [/System/Library/PrivateFrameworks/ChronoUIServices.framework/ChronoUIServices](DYLIBS/ChronoUIServices.md)
- [/System/Library/PrivateFrameworks/CipherML.framework/CipherML](DYLIBS/CipherML.md)
- [/System/Library/PrivateFrameworks/ClassroomKit.framework/ClassroomKit](DYLIBS/ClassroomKit.md)
- [/System/Library/PrivateFrameworks/ClassroomKit.framework/Frameworks/ClassroomUIKit.framework/ClassroomUIKit](DYLIBS/ClassroomUIKit.md)
- [/System/Library/PrivateFrameworks/ClockPoster.framework/ClockPoster](DYLIBS/ClockPoster.md)
- [/System/Library/PrivateFrameworks/CloudAsset.framework/CloudAsset](DYLIBS/CloudAsset.md)
- [/System/Library/PrivateFrameworks/CloudAssetDaemon.framework/CloudAssetDaemon](DYLIBS/CloudAssetDaemon.md)
- [/System/Library/PrivateFrameworks/CloudAssets.framework/CloudAssets](DYLIBS/CloudAssets.md)
- [/System/Library/PrivateFrameworks/CloudAttestation.framework/CloudAttestation](DYLIBS/CloudAttestation.md)
- [/System/Library/PrivateFrameworks/CloudDocs.framework/CloudDocs](DYLIBS/CloudDocs.md)
- [/System/Library/PrivateFrameworks/CloudDocsDaemon.framework/CloudDocsDaemon](DYLIBS/CloudDocsDaemon.md)
- [/System/Library/PrivateFrameworks/CloudKitDaemon.framework/CloudKitDaemon](DYLIBS/CloudKitDaemon.md)
- [/System/Library/PrivateFrameworks/CloudRecommendationUI.framework/CloudRecommendationUI](DYLIBS/CloudRecommendationUI.md)
- [/System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/CloudSubscriptionFeatures](DYLIBS/CloudSubscriptionFeatures.md)
- [/System/Library/PrivateFrameworks/CloudTelemetryTools.framework/CloudTelemetryTools](DYLIBS/CloudTelemetryTools.md)
- [/System/Library/PrivateFrameworks/Coherence.framework/Coherence](DYLIBS/Coherence.md)
- [/System/Library/PrivateFrameworks/CollectionsInternal.framework/CollectionsInternal](DYLIBS/CollectionsInternal.md)
- [/System/Library/PrivateFrameworks/CommandAndControlUI.framework/CommandAndControlUI](DYLIBS/CommandAndControlUI.md)
- [/System/Library/PrivateFrameworks/CommunicationsSetupUI.framework/CommunicationsSetupUI](DYLIBS/CommunicationsSetupUI.md)
- [/System/Library/PrivateFrameworks/CommunicationsUI.framework/CommunicationsUI](DYLIBS/CommunicationsUI.md)
- [/System/Library/PrivateFrameworks/ConfigurationEngineModel.framework/ConfigurationEngineModel](DYLIBS/ConfigurationEngineModel.md)
- [/System/Library/PrivateFrameworks/ContactlessReaderUI.framework/ContactlessReaderUI](DYLIBS/ContactlessReaderUI.md)
- [/System/Library/PrivateFrameworks/ContactsUICore.framework/ContactsUICore](DYLIBS/ContactsUICore.md)
- [/System/Library/PrivateFrameworks/ContentKit.framework/ContentKit](DYLIBS/ContentKit.md)
- [/System/Library/PrivateFrameworks/ContinuousDialogManagerService.framework/ContinuousDialogManagerService](DYLIBS/ContinuousDialogManagerService.md)
- [/System/Library/PrivateFrameworks/ControlCenterServices.framework/ControlCenterServices](DYLIBS/ControlCenterServices.md)
- [/System/Library/PrivateFrameworks/ControlCenterUI.framework/ControlCenterUI](DYLIBS/ControlCenterUI.md)
- [/System/Library/PrivateFrameworks/ConversationKit.framework/ConversationKit](DYLIBS/ConversationKit.md)
- [/System/Library/PrivateFrameworks/CoreAccessories.framework/CoreAccessories](DYLIBS/CoreAccessories.md)
- [/System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP](DYLIBS/CoreCDP.md)
- [/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal](DYLIBS/CoreCDPInternal.md)
- [/System/Library/PrivateFrameworks/CoreCDPUI.framework/CoreCDPUI](DYLIBS/CoreCDPUI.md)
- [/System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet](DYLIBS/CoreDuet.md)
- [/System/Library/PrivateFrameworks/CoreGEM.framework/CoreGEM.dylib](DYLIBS/CoreGEM.dylib.md)
- [/System/Library/PrivateFrameworks/CoreGPSTest.framework/CoreGPSTest](DYLIBS/CoreGPSTest.md)
- [/System/Library/PrivateFrameworks/CoreHandwriting.framework/CoreHandwriting](DYLIBS/CoreHandwriting.md)
- [/System/Library/PrivateFrameworks/CoreIDVPAD.framework/CoreIDVPAD](DYLIBS/CoreIDVPAD.md)
- [/System/Library/PrivateFrameworks/CoreIDVRGBLiveness.framework/CoreIDVRGBLiveness](DYLIBS/CoreIDVRGBLiveness.md)
- [/System/Library/PrivateFrameworks/CoreIDVShared.framework/CoreIDVShared](DYLIBS/CoreIDVShared.md)
- [/System/Library/PrivateFrameworks/CoreIDVUI.framework/CoreIDVUI](DYLIBS/CoreIDVUI.md)
- [/System/Library/PrivateFrameworks/CoreIndoor.framework/CoreIndoor](DYLIBS/CoreIndoor.md)
- [/System/Library/PrivateFrameworks/CoreKnowledge.framework/CoreKnowledge](DYLIBS/CoreKnowledge.md)
- [/System/Library/PrivateFrameworks/CoreNavigation.framework/CoreNavigation](DYLIBS/CoreNavigation.md)
- [/System/Library/PrivateFrameworks/CoreOC.framework/CoreOC](DYLIBS/CoreOC.md)
- [/System/Library/PrivateFrameworks/CoreODI.framework/CoreODI](DYLIBS/CoreODI.md)
- [/System/Library/PrivateFrameworks/CoreODIEssentials.framework/CoreODIEssentials](DYLIBS/CoreODIEssentials.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/CoreParsec](DYLIBS/CoreParsec.md)
- [/System/Library/PrivateFrameworks/CoreRE.framework/CoreRE](DYLIBS/CoreRE.md)
- [/System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore](DYLIBS/CoreRepairCore.md)
- [/System/Library/PrivateFrameworks/CoreRepairUI.framework/CoreRepairUI](DYLIBS/CoreRepairUI.md)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/CoreSpeech](DYLIBS/CoreSpeech.md)
- [/System/Library/PrivateFrameworks/CoreSpeechFoundation.framework/CoreSpeechFoundation](DYLIBS/CoreSpeechFoundation.md)
- [/System/Library/PrivateFrameworks/CoreUARP.framework/CoreUARP](DYLIBS/CoreUARP.md)
- [/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi](DYLIBS/CoreWiFi.md)
- [/System/Library/PrivateFrameworks/Cosmo.framework/Cosmo](DYLIBS/Cosmo.md)
- [/System/Library/PrivateFrameworks/CoverSheet.framework/CoverSheet](DYLIBS/CoverSheet.md)
- [/System/Library/PrivateFrameworks/CryptoKitPrivate.framework/CryptoKitPrivate](DYLIBS/CryptoKitPrivate.md)
- [/System/Library/PrivateFrameworks/DMCEnrollmentProvider.framework/DMCEnrollmentProvider](DYLIBS/DMCEnrollmentProvider.md)
- [/System/Library/PrivateFrameworks/DarwinDirectory.framework/DarwinDirectory](DYLIBS/DarwinDirectory.md)
- [/System/Library/PrivateFrameworks/DarwinDirectoryInternal.framework/DarwinDirectoryInternal](DYLIBS/DarwinDirectoryInternal.md)
- [/System/Library/PrivateFrameworks/DarwinDirectoryQuery.framework/DarwinDirectoryQuery](DYLIBS/DarwinDirectoryQuery.md)
- [/System/Library/PrivateFrameworks/DashBoard.framework/DashBoard](DYLIBS/DashBoard.md)
- [/System/Library/PrivateFrameworks/DataDetectorsCore.framework/DataDetectorsCore](DYLIBS/DataDetectorsCore.md)
- [/System/Library/PrivateFrameworks/DataDetectorsUI.framework/DataDetectorsUI](DYLIBS/DataDetectorsUI.md)
- [/System/Library/PrivateFrameworks/DataFlow.framework/DataFlow](DYLIBS/DataFlow.md)
- [/System/Library/PrivateFrameworks/DeepThought.framework/DeepThought](DYLIBS/DeepThought.md)
- [/System/Library/PrivateFrameworks/Dendrite.framework/Dendrite](DYLIBS/Dendrite.md)
- [/System/Library/PrivateFrameworks/DeviceDiscoveryUI.framework/DeviceDiscoveryUI](DYLIBS/DeviceDiscoveryUI.md)
- [/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/DeviceExpertIntents](DYLIBS/DeviceExpertIntents.md)
- [/System/Library/PrivateFrameworks/DeviceManagement.framework/DeviceManagement](DYLIBS/DeviceManagement.md)
- [/System/Library/PrivateFrameworks/DictionaryServices.framework/DictionaryServices](DYLIBS/DictionaryServices.md)
- [/System/Library/PrivateFrameworks/DistributedTimersDaemon.framework/DistributedTimersDaemon](DYLIBS/DistributedTimersDaemon.md)
- [/System/Library/PrivateFrameworks/DockKitCore.framework/DockKitCore](DYLIBS/DockKitCore.md)
- [/System/Library/PrivateFrameworks/DocumentManagerExecutables.framework/DocumentManagerExecutables](DYLIBS/DocumentManagerExecutables.md)
- [/System/Library/PrivateFrameworks/DocumentUnderstanding.framework/DocumentUnderstanding](DYLIBS/DocumentUnderstanding.md)
- [/System/Library/PrivateFrameworks/DrawingBoard.framework/DrawingBoard](DYLIBS/DrawingBoard.md)
- [/System/Library/PrivateFrameworks/DropInCore.framework/DropInCore](DYLIBS/DropInCore.md)
- [/System/Library/PrivateFrameworks/Email.framework/Email](DYLIBS/Email.md)
- [/System/Library/PrivateFrameworks/EmailDaemon.framework/EmailDaemon](DYLIBS/EmailDaemon.md)
- [/System/Library/PrivateFrameworks/EnergyKit.framework/EnergyKit](DYLIBS/EnergyKit.md)
- [/System/Library/PrivateFrameworks/Espresso.framework/Espresso](DYLIBS/Espresso.md)
- [/System/Library/PrivateFrameworks/FMFCore.framework/FMFCore](DYLIBS/FMFCore.md)
- [/System/Library/PrivateFrameworks/FMFindingUI.framework/FMFindingUI](DYLIBS/FMFindingUI.md)
- [/System/Library/PrivateFrameworks/FMIPCore.framework/FMIPCore](DYLIBS/FMIPCore.md)
- [/System/Library/PrivateFrameworks/FPFS.framework/FPFS](DYLIBS/FPFS.md)
- [/System/Library/PrivateFrameworks/FamilyCircleUI.framework/FamilyCircleUI](DYLIBS/FamilyCircleUI.md)
- [/System/Library/PrivateFrameworks/FeatureStore.framework/FeatureStore](DYLIBS/FeatureStore.md)
- [/System/Library/PrivateFrameworks/Feedback.framework/Feedback](DYLIBS/Feedback.md)
- [/System/Library/PrivateFrameworks/FeedbackCore.framework/FeedbackCore](DYLIBS/FeedbackCore.md)
- [/System/Library/PrivateFrameworks/FinanceDaemon.framework/FinanceDaemon](DYLIBS/FinanceDaemon.md)
- [/System/Library/PrivateFrameworks/FindMyBase.framework/FindMyBase](DYLIBS/FindMyBase.md)
- [/System/Library/PrivateFrameworks/FindMyBluetooth.framework/FindMyBluetooth](DYLIBS/FindMyBluetooth.md)
- [/System/Library/PrivateFrameworks/FindMyCommon.framework/FindMyCommon](DYLIBS/FindMyCommon.md)
- [/System/Library/PrivateFrameworks/FindMyLocate.framework/FindMyLocate](DYLIBS/FindMyLocate.md)
- [/System/Library/PrivateFrameworks/FindMyMessaging.framework/FindMyMessaging](DYLIBS/FindMyMessaging.md)
- [/System/Library/PrivateFrameworks/FindMyUICore.framework/FindMyUICore](DYLIBS/FindMyUICore.md)
- [/System/Library/PrivateFrameworks/FitnessAppRoot.framework/FitnessAppRoot](DYLIBS/FitnessAppRoot.md)
- [/System/Library/PrivateFrameworks/FitnessAsset.framework/FitnessAsset](DYLIBS/FitnessAsset.md)
- [/System/Library/PrivateFrameworks/FitnessAwards.framework/FitnessAwards](DYLIBS/FitnessAwards.md)
- [/System/Library/PrivateFrameworks/FitnessCanvasUI.framework/FitnessCanvasUI](DYLIBS/FitnessCanvasUI.md)
- [/System/Library/PrivateFrameworks/FitnessCoachingServices.framework/FitnessCoachingServices](DYLIBS/FitnessCoachingServices.md)
- [/System/Library/PrivateFrameworks/FitnessCoreUI.framework/FitnessCoreUI](DYLIBS/FitnessCoreUI.md)
- [/System/Library/PrivateFrameworks/FitnessMarketing.framework/FitnessMarketing](DYLIBS/FitnessMarketing.md)
- [/System/Library/PrivateFrameworks/FitnessProductDetail.framework/FitnessProductDetail](DYLIBS/FitnessProductDetail.md)
- [/System/Library/PrivateFrameworks/FitnessWorkoutPlan.framework/FitnessWorkoutPlan](DYLIBS/FitnessWorkoutPlan.md)
- [/System/Library/PrivateFrameworks/FocusSettingsUI.framework/FocusSettingsUI](DYLIBS/FocusSettingsUI.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/libFontParser.dylib](DYLIBS/libFontParser.dylib.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/libGSFont.dylib](DYLIBS/libGSFont.dylib.md)
- [/System/Library/PrivateFrameworks/GRDBInternal.framework/GRDBInternal](DYLIBS/GRDBInternal.md)
- [/System/Library/PrivateFrameworks/GameCenterFoundation.framework/GameCenterFoundation](DYLIBS/GameCenterFoundation.md)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/GameCenterUI](DYLIBS/GameCenterUI.md)
- [/System/Library/PrivateFrameworks/GameControllerFoundation.framework/GameControllerFoundation](DYLIBS/GameControllerFoundation.md)
- [/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/GenerativeAssistantActions](DYLIBS/GenerativeAssistantActions.md)
- [/System/Library/PrivateFrameworks/GenerativeAssistantCommon.framework/GenerativeAssistantCommon](DYLIBS/GenerativeAssistantCommon.md)
- [/System/Library/PrivateFrameworks/GenerativeAssistantSettings.framework/GenerativeAssistantSettings](DYLIBS/GenerativeAssistantSettings.md)
- [/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/GenerativeExperiencesRuntime](DYLIBS/GenerativeExperiencesRuntime.md)
- [/System/Library/PrivateFrameworks/GenerativeExperiencesUI.framework/GenerativeExperiencesUI](DYLIBS/GenerativeExperiencesUI.md)
- [/System/Library/PrivateFrameworks/GenerativeFunctionsInstrumentation.framework/GenerativeFunctionsInstrumentation](DYLIBS/GenerativeFunctionsInstrumentation.md)
- [/System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels](DYLIBS/GenerativeModels.md)
- [/System/Library/PrivateFrameworks/GenerativeModelsFoundation.framework/GenerativeModelsFoundation](DYLIBS/GenerativeModelsFoundation.md)
- [/System/Library/PrivateFrameworks/GeoUIFramework.framework/GeoUIFramework](DYLIBS/GeoUIFramework.md)
- [/System/Library/PrivateFrameworks/Geometry.framework/Geometry](DYLIBS/Geometry.md)
- [/System/Library/PrivateFrameworks/GroupKitCrypto.framework/GroupKitCrypto](DYLIBS/GroupKitCrypto.md)
- [/System/Library/PrivateFrameworks/Hands.framework/Hands](DYLIBS/Hands.md)
- [/System/Library/PrivateFrameworks/HeadGestures.framework/HeadGestures](DYLIBS/HeadGestures.md)
- [/System/Library/PrivateFrameworks/HeadphoneConfigs.framework/HeadphoneConfigs](DYLIBS/HeadphoneConfigs.md)
- [/System/Library/PrivateFrameworks/HealthArticlesUI.framework/HealthArticlesUI](DYLIBS/HealthArticlesUI.md)
- [/System/Library/PrivateFrameworks/HealthBalanceUI.framework/HealthBalanceUI](DYLIBS/HealthBalanceUI.md)
- [/System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon](DYLIBS/HealthDaemon.md)
- [/System/Library/PrivateFrameworks/HealthExperienceUI.framework/HealthExperienceUI](DYLIBS/HealthExperienceUI.md)
- [/System/Library/PrivateFrameworks/HealthExposureNotificationUI.framework/HealthExposureNotificationUI](DYLIBS/HealthExposureNotificationUI.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsUI.framework/HealthMedicationsUI](DYLIBS/HealthMedicationsUI.md)
- [/System/Library/PrivateFrameworks/HealthMenstrualCycles.framework/HealthMenstrualCycles](DYLIBS/HealthMenstrualCycles.md)
- [/System/Library/PrivateFrameworks/HealthRecordServices.framework/HealthRecordServices](DYLIBS/HealthRecordServices.md)
- [/System/Library/PrivateFrameworks/HealthRecordsDaemon.framework/HealthRecordsDaemon](DYLIBS/HealthRecordsDaemon.md)
- [/System/Library/PrivateFrameworks/HealthRecordsUI.framework/HealthRecordsUI](DYLIBS/HealthRecordsUI.md)
- [/System/Library/PrivateFrameworks/HealthUI.framework/HealthUI](DYLIBS/HealthUI.md)
- [/System/Library/PrivateFrameworks/HealthVisualization.framework/HealthVisualization](DYLIBS/HealthVisualization.md)
- [/System/Library/PrivateFrameworks/HearingModeSettingsUI.framework/HearingModeSettingsUI](DYLIBS/HearingModeSettingsUI.md)
- [/System/Library/PrivateFrameworks/HearingModeUI.framework/HearingModeUI](DYLIBS/HearingModeUI.md)
- [/System/Library/PrivateFrameworks/HearingTest.framework/HearingTest](DYLIBS/HearingTest.md)
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
- [/System/Library/PrivateFrameworks/HomeKitDaemonFoundation.framework/HomeKitDaemonFoundation](DYLIBS/HomeKitDaemonFoundation.md)
- [/System/Library/PrivateFrameworks/HomeKitEvents.framework/HomeKitEvents](DYLIBS/HomeKitEvents.md)
- [/System/Library/PrivateFrameworks/HomePlatformSettingsUI.framework/HomePlatformSettingsUI](DYLIBS/HomePlatformSettingsUI.md)
- [/System/Library/PrivateFrameworks/HomePodSettings.framework/HomePodSettings](DYLIBS/HomePodSettings.md)
- [/System/Library/PrivateFrameworks/HomeUI.framework/HomeUI](DYLIBS/HomeUI.md)
- [/System/Library/PrivateFrameworks/HomeUI2.framework/HomeUI2](DYLIBS/HomeUI2.md)
- [/System/Library/PrivateFrameworks/HomeUtilityServices.framework/HomeUtilityServices](DYLIBS/HomeUtilityServices.md)
- [/System/Library/PrivateFrameworks/HoverTextUI.framework/HoverTextUI](DYLIBS/HoverTextUI.md)
- [/System/Library/PrivateFrameworks/Human.framework/Human](DYLIBS/Human.md)
- [/System/Library/PrivateFrameworks/HumanUI.framework/HumanUI](DYLIBS/HumanUI.md)
- [/System/Library/PrivateFrameworks/IMCore.framework/IMCore](DYLIBS/IMCore.md)
- [/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence](DYLIBS/IMDPersistence.md)
- [/System/Library/PrivateFrameworks/IMDaemonCore.framework/IMDaemonCore](DYLIBS/IMDaemonCore.md)
- [/System/Library/PrivateFrameworks/IMSharedUtilities.framework/IMSharedUtilities](DYLIBS/IMSharedUtilities.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowContextRuntime.framework/IntelligenceFlowContextRuntime](DYLIBS/IntelligenceFlowContextRuntime.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/IntelligenceFlowPlannerRuntime](DYLIBS/IntelligenceFlowPlannerRuntime.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowPlannerSupport.framework/IntelligenceFlowPlannerSupport](DYLIBS/IntelligenceFlowPlannerSupport.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/IntelligenceFlowRuntime](DYLIBS/IntelligenceFlowRuntime.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatform.framework/IntelligencePlatform](DYLIBS/IntelligencePlatform.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/IntelligencePlatformCore](DYLIBS/IntelligencePlatformCore.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformLibrary.framework/IntelligencePlatformLibrary](DYLIBS/IntelligencePlatformLibrary.md)
- [/System/Library/PrivateFrameworks/IntelligentTrackingCore.framework/IntelligentTrackingCore](DYLIBS/IntelligentTrackingCore.md)
- [/System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf](DYLIBS/InternalSwiftProtobuf.md)
- [/System/Library/PrivateFrameworks/JITAppKit.framework/JITAppKit](DYLIBS/JITAppKit.md)
- [/System/Library/PrivateFrameworks/JetEngine.framework/JetEngine](DYLIBS/JetEngine.md)
- [/System/Library/PrivateFrameworks/JetUI.framework/JetUI](DYLIBS/JetUI.md)
- [/System/Library/PrivateFrameworks/KnowledgeGraphKit.framework/KnowledgeGraphKit](DYLIBS/KnowledgeGraphKit.md)
- [/System/Library/PrivateFrameworks/KnowledgeMonitor.framework/KnowledgeMonitor](DYLIBS/KnowledgeMonitor.md)
- [/System/Library/PrivateFrameworks/LiftUI.framework/LiftUI](DYLIBS/LiftUI.md)
- [/System/Library/PrivateFrameworks/LighthouseDataProcessor.framework/LighthouseDataProcessor](DYLIBS/LighthouseDataProcessor.md)
- [/System/Library/PrivateFrameworks/LinkMetadata.framework/LinkMetadata](DYLIBS/LinkMetadata.md)
- [/System/Library/PrivateFrameworks/LinkServices.framework/LinkServices](DYLIBS/LinkServices.md)
- [/System/Library/PrivateFrameworks/LiveExecutionResultsProbe.framework/LiveExecutionResultsProbe](DYLIBS/LiveExecutionResultsProbe.md)
- [/System/Library/PrivateFrameworks/MLModelSpecification.framework/MLModelSpecification](DYLIBS/MLModelSpecification.md)
- [/System/Library/PrivateFrameworks/MagnifierSupport.framework/MagnifierSupport](DYLIBS/MagnifierSupport.md)
- [/System/Library/PrivateFrameworks/MailUI.framework/MailUI](DYLIBS/MailUI.md)
- [/System/Library/PrivateFrameworks/MapsSuggestions.framework/MapsSuggestions](DYLIBS/MapsSuggestions.md)
- [/System/Library/PrivateFrameworks/MapsSupport.framework/MapsSupport](DYLIBS/MapsSupport.md)
- [/System/Library/PrivateFrameworks/MapsSync.framework/MapsSync](DYLIBS/MapsSync.md)
- [/System/Library/PrivateFrameworks/MapsUI.framework/MapsUI](DYLIBS/MapsUI.md)
- [/System/Library/PrivateFrameworks/Marrs.framework/Marrs](DYLIBS/Marrs.md)
- [/System/Library/PrivateFrameworks/MeasureFoundation.framework/MeasureFoundation](DYLIBS/MeasureFoundation.md)
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/MediaAnalysis](DYLIBS/MediaAnalysis.md)
- [/System/Library/PrivateFrameworks/MediaControls.framework/MediaControls](DYLIBS/MediaControls.md)
- [/System/Library/PrivateFrameworks/MediaCoreUI.framework/MediaCoreUI](DYLIBS/MediaCoreUI.md)
- [/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore](DYLIBS/MediaPlaybackCore.md)
- [/System/Library/PrivateFrameworks/MedicalIDUI.framework/MedicalIDUI](DYLIBS/MedicalIDUI.md)
- [/System/Library/PrivateFrameworks/MentalHealthUI.framework/MentalHealthUI](DYLIBS/MentalHealthUI.md)
- [/System/Library/PrivateFrameworks/Message.framework/Message](DYLIBS/Message.md)
- [/System/Library/PrivateFrameworks/MessageProtection.framework/MessageProtection](DYLIBS/MessageProtection.md)
- [/System/Library/PrivateFrameworks/MessagesCloudSync.framework/MessagesCloudSync](DYLIBS/MessagesCloudSync.md)
- [/System/Library/PrivateFrameworks/MessagesSettingsUI.framework/MessagesSettingsUI](DYLIBS/MessagesSettingsUI.md)
- [/System/Library/PrivateFrameworks/MetadataUtilities.framework/MetadataUtilities](DYLIBS/MetadataUtilities.md)
- [/System/Library/PrivateFrameworks/MetricsFramework.framework/MetricsFramework](DYLIBS/MetricsFramework.md)
- [/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon](DYLIBS/MicroLocationDaemon.md)
- [/System/Library/PrivateFrameworks/MigrationKit.framework/MigrationKit](DYLIBS/MigrationKit.md)
- [/System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset](DYLIBS/MobileAsset.md)
- [/System/Library/PrivateFrameworks/MobileAssetExclaveServices.framework/MobileAssetExclaveServices](DYLIBS/MobileAssetExclaveServices.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup](DYLIBS/MobileBackup.md)
- [/System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag](DYLIBS/MobileKeyBag.md)
- [/System/Library/PrivateFrameworks/MobileSafari.framework/MobileSafari](DYLIBS/MobileSafari.md)
- [/System/Library/PrivateFrameworks/MobileSafariUI.framework/MobileSafariUI](DYLIBS/MobileSafariUI.md)
- [/System/Library/PrivateFrameworks/MobileSpotlightIndex.framework/MobileSpotlightIndex](DYLIBS/MobileSpotlightIndex.md)
- [/System/Library/PrivateFrameworks/MobileTimerSupport.framework/MobileTimerSupport](DYLIBS/MobileTimerSupport.md)
- [/System/Library/PrivateFrameworks/ModelManagerServices.framework/ModelManagerServices](DYLIBS/ModelManagerServices.md)
- [/System/Library/PrivateFrameworks/Morpheus.framework/Morpheus](DYLIBS/Morpheus.md)
- [/System/Library/PrivateFrameworks/MusicKitInternal.framework/MusicKitInternal](DYLIBS/MusicKitInternal.md)
- [/System/Library/PrivateFrameworks/MusicUI.framework/MusicUI](DYLIBS/MusicUI.md)
- [/System/Library/PrivateFrameworks/NanoHomeScreenUIServices.framework/NanoHomeScreenUIServices](DYLIBS/NanoHomeScreenUIServices.md)
- [/System/Library/PrivateFrameworks/NanoTimeKit.framework/NanoTimeKit](DYLIBS/NanoTimeKit.md)
- [/System/Library/PrivateFrameworks/NanoTimeKitCompanion.framework/NanoTimeKitCompanion](DYLIBS/NanoTimeKitCompanion.md)
- [/System/Library/PrivateFrameworks/NeuralNetworks.framework/NeuralNetworks](DYLIBS/NeuralNetworks.md)
- [/System/Library/PrivateFrameworks/NeutrinoCore.framework/NeutrinoCore](DYLIBS/NeutrinoCore.md)
- [/System/Library/PrivateFrameworks/NewsAds.framework/NewsAds](DYLIBS/NewsAds.md)
- [/System/Library/PrivateFrameworks/NewsArticles.framework/NewsArticles](DYLIBS/NewsArticles.md)
- [/System/Library/PrivateFrameworks/NewsCore.framework/NewsCore](DYLIBS/NewsCore.md)
- [/System/Library/PrivateFrameworks/NewsFeed.framework/NewsFeed](DYLIBS/NewsFeed.md)
- [/System/Library/PrivateFrameworks/NewsLiveActivitiesCore.framework/NewsLiveActivitiesCore](DYLIBS/NewsLiveActivitiesCore.md)
- [/System/Library/PrivateFrameworks/NewsPersonalization.framework/NewsPersonalization](DYLIBS/NewsPersonalization.md)
- [/System/Library/PrivateFrameworks/NewsSubscription.framework/NewsSubscription](DYLIBS/NewsSubscription.md)
- [/System/Library/PrivateFrameworks/NewsUI2.framework/NewsUI2](DYLIBS/NewsUI2.md)
- [/System/Library/PrivateFrameworks/NightingaleTraining.framework/NightingaleTraining](DYLIBS/NightingaleTraining.md)
- [/System/Library/PrivateFrameworks/NotesEditor.framework/NotesEditor](DYLIBS/NotesEditor.md)
- [/System/Library/PrivateFrameworks/NotesSupport.framework/NotesSupport](DYLIBS/NotesSupport.md)
- [/System/Library/PrivateFrameworks/NotesUI.framework/NotesUI](DYLIBS/NotesUI.md)
- [/System/Library/PrivateFrameworks/ODCurareEvaluationAndReporting.framework/ODCurareEvaluationAndReporting](DYLIBS/ODCurareEvaluationAndReporting.md)
- [/System/Library/PrivateFrameworks/PLSnapshot.framework/PLSnapshot](DYLIBS/PLSnapshot.md)
- [/System/Library/PrivateFrameworks/PaperBoardUI.framework/PaperBoardUI](DYLIBS/PaperBoardUI.md)
- [/System/Library/PrivateFrameworks/PaperKit.framework/PaperKit](DYLIBS/PaperKit.md)
- [/System/Library/PrivateFrameworks/PassKitUI.framework/PassKitUI](DYLIBS/PassKitUI.md)
- [/System/Library/PrivateFrameworks/PasswordManagerUI.framework/PasswordManagerUI](DYLIBS/PasswordManagerUI.md)
- [/System/Library/PrivateFrameworks/PegasusAPI.framework/PegasusAPI](DYLIBS/PegasusAPI.md)
- [/System/Library/PrivateFrameworks/PegasusConfiguration.framework/PegasusConfiguration](DYLIBS/PegasusConfiguration.md)
- [/System/Library/PrivateFrameworks/PegasusKit.framework/PegasusKit](DYLIBS/PegasusKit.md)
- [/System/Library/PrivateFrameworks/People.framework/People](DYLIBS/People.md)
- [/System/Library/PrivateFrameworks/PeopleSuggesterLighthouse.framework/PeopleSuggesterLighthouse](DYLIBS/PeopleSuggesterLighthouse.md)
- [/System/Library/PrivateFrameworks/PerfPowerServicesMetadata.framework/PerfPowerServicesMetadata](DYLIBS/PerfPowerServicesMetadata.md)
- [/System/Library/PrivateFrameworks/PhoneSnippetUI.framework/PhoneSnippetUI](DYLIBS/PhoneSnippetUI.md)
- [/System/Library/PrivateFrameworks/PhotoAnalysis.framework/PhotoAnalysis](DYLIBS/PhotoAnalysis.md)
- [/System/Library/PrivateFrameworks/PhotoImaging.framework/PhotoImaging](DYLIBS/PhotoImaging.md)
- [/System/Library/PrivateFrameworks/PhotosGraph.framework/PhotosGraph](DYLIBS/PhotosGraph.md)
- [/System/Library/PrivateFrameworks/PhotosIntelligence.framework/PhotosIntelligence](DYLIBS/PhotosIntelligence.md)
- [/System/Library/PrivateFrameworks/PhotosSwiftUICore.framework/PhotosSwiftUICore](DYLIBS/PhotosSwiftUICore.md)
- [/System/Library/PrivateFrameworks/PhotosUICore.framework/PhotosUICore](DYLIBS/PhotosUICore.md)
- [/System/Library/PrivateFrameworks/PhotosUIFoundation.framework/PhotosUIFoundation](DYLIBS/PhotosUIFoundation.md)
- [/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PhotosUIPrivate](DYLIBS/PhotosUIPrivate.md)
- [/System/Library/PrivateFrameworks/PlatformSSOCore.framework/PlatformSSOCore](DYLIBS/PlatformSSOCore.md)
- [/System/Library/PrivateFrameworks/PodcastsFoundation.framework/PodcastsFoundation](DYLIBS/PodcastsFoundation.md)
- [/System/Library/PrivateFrameworks/PodcastsUI.framework/PodcastsUI](DYLIBS/PodcastsUI.md)
- [/System/Library/PrivateFrameworks/PoirotBlocks.framework/PoirotBlocks](DYLIBS/PoirotBlocks.md)
- [/System/Library/PrivateFrameworks/PoirotSchematizer.framework/PoirotSchematizer](DYLIBS/PoirotSchematizer.md)
- [/System/Library/PrivateFrameworks/PoirotUDFs.framework/PoirotUDFs](DYLIBS/PoirotUDFs.md)
- [/System/Library/PrivateFrameworks/Portrait.framework/Portrait](DYLIBS/Portrait.md)
- [/System/Library/PrivateFrameworks/PosterBoard.framework/PosterBoard](DYLIBS/PosterBoard.md)
- [/System/Library/PrivateFrameworks/PosterBoardServices.framework/PosterBoardServices](DYLIBS/PosterBoardServices.md)
- [/System/Library/PrivateFrameworks/PosterKit.framework/PosterKit](DYLIBS/PosterKit.md)
- [/System/Library/PrivateFrameworks/PosterPlatformSupport.framework/PosterPlatformSupport](DYLIBS/PosterPlatformSupport.md)
- [/System/Library/PrivateFrameworks/PowerLog.framework/PowerLog](DYLIBS/PowerLog.md)
- [/System/Library/PrivateFrameworks/PowerlogAccounting.framework/PowerlogAccounting](DYLIBS/PowerlogAccounting.md)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore](DYLIBS/PowerlogCore.md)
- [/System/Library/PrivateFrameworks/PowerlogFullOperators.framework/PowerlogFullOperators](DYLIBS/PowerlogFullOperators.md)
- [/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators](DYLIBS/PowerlogHelperdOperators.md)
- [/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators](DYLIBS/PowerlogLiteOperators.md)
- [/System/Library/PrivateFrameworks/PreviewShellKit.framework/PreviewShellKit](DYLIBS/PreviewShellKit.md)
- [/System/Library/PrivateFrameworks/PreviewsFoundationOS.framework/PreviewsFoundationOS](DYLIBS/PreviewsFoundationOS.md)
- [/System/Library/PrivateFrameworks/PreviewsInjection.framework/PreviewsInjection](DYLIBS/PreviewsInjection.md)
- [/System/Library/PrivateFrameworks/PreviewsMessagingOS.framework/PreviewsMessagingOS](DYLIBS/PreviewsMessagingOS.md)
- [/System/Library/PrivateFrameworks/PreviewsOSSupport.framework/PreviewsOSSupport](DYLIBS/PreviewsOSSupport.md)
- [/System/Library/PrivateFrameworks/PreviewsServicesUI.framework/PreviewsServicesUI](DYLIBS/PreviewsServicesUI.md)
- [/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PrivateFederatedLearning](DYLIBS/PrivateFederatedLearning.md)
- [/System/Library/PrivateFrameworks/PrivateMLClient.framework/PrivateMLClient](DYLIBS/PrivateMLClient.md)
- [/System/Library/PrivateFrameworks/ProactiveDaemonSupport.framework/ProactiveDaemonSupport](DYLIBS/ProactiveDaemonSupport.md)
- [/System/Library/PrivateFrameworks/ProactiveSummarization.framework/ProactiveSummarization](DYLIBS/ProactiveSummarization.md)
- [/System/Library/PrivateFrameworks/ProductKit.framework/ProductKit](DYLIBS/ProductKit.md)
- [/System/Library/PrivateFrameworks/PromotedContentUI.framework/PromotedContentUI](DYLIBS/PromotedContentUI.md)
- [/System/Library/PrivateFrameworks/ProximityAppleIDSetup.framework/ProximityAppleIDSetup](DYLIBS/ProximityAppleIDSetup.md)
- [/System/Library/PrivateFrameworks/ProximityAppleIDSetupUI.framework/ProximityAppleIDSetupUI](DYLIBS/ProximityAppleIDSetupUI.md)
- [/System/Library/PrivateFrameworks/ProximityReaderDaemon.framework/ProximityReaderDaemon](DYLIBS/ProximityReaderDaemon.md)
- [/System/Library/PrivateFrameworks/QOSToolkit.framework/QOSToolkit](DYLIBS/QOSToolkit.md)
- [/System/Library/PrivateFrameworks/QueryParser.framework/QueryParser](DYLIBS/QueryParser.md)
- [/System/Library/PrivateFrameworks/QuickLookThumbnailingDaemon.framework/QuickLookThumbnailingDaemon](DYLIBS/QuickLookThumbnailingDaemon.md)
- [/System/Library/PrivateFrameworks/QuickLookUICore.framework/QuickLookUICore](DYLIBS/QuickLookUICore.md)
- [/System/Library/PrivateFrameworks/RESync.framework/RESync](DYLIBS/RESync.md)
- [/System/Library/PrivateFrameworks/RealityIO.framework/RealityIO](DYLIBS/RealityIO.md)
- [/System/Library/PrivateFrameworks/RealityKitInspection.framework/RealityKitInspection](DYLIBS/RealityKitInspection.md)
- [/System/Library/PrivateFrameworks/Recount.framework/Recount](DYLIBS/Recount.md)
- [/System/Library/PrivateFrameworks/RemindersUICore.framework/RemindersUICore](DYLIBS/RemindersUICore.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/RemoteManagement](DYLIBS/RemoteManagement.md)
- [/System/Library/PrivateFrameworks/RemotePairingDevice.framework/RemotePairingDevice](DYLIBS/RemotePairingDevice.md)
- [/System/Library/PrivateFrameworks/RemoteUI.framework/RemoteUI](DYLIBS/RemoteUI.md)
- [/System/Library/PrivateFrameworks/ReplicatorCore.framework/ReplicatorCore](DYLIBS/ReplicatorCore.md)
- [/System/Library/PrivateFrameworks/ReplicatorEngine.framework/ReplicatorEngine](DYLIBS/ReplicatorEngine.md)
- [/System/Library/PrivateFrameworks/RequestDispatcherBridges.framework/RequestDispatcherBridges](DYLIBS/RequestDispatcherBridges.md)
- [/System/Library/PrivateFrameworks/RunningBoard.framework/RunningBoard](DYLIBS/RunningBoard.md)
- [/System/Library/PrivateFrameworks/RuntimeInternal.framework/RuntimeInternal](DYLIBS/RuntimeInternal.md)
- [/System/Library/PrivateFrameworks/SFSymbols.framework/SFSymbols](DYLIBS/SFSymbols.md)
- [/System/Library/PrivateFrameworks/SPShared.framework/SPShared](DYLIBS/SPShared.md)
- [/System/Library/PrivateFrameworks/SafariCore.framework/SafariCore](DYLIBS/SafariCore.md)
- [/System/Library/PrivateFrameworks/SafariFoundation.framework/SafariFoundation](DYLIBS/SafariFoundation.md)
- [/System/Library/PrivateFrameworks/SafariSharedUI.framework/SafariSharedUI](DYLIBS/SafariSharedUI.md)
- [/System/Library/PrivateFrameworks/SafetyMonitorUI.framework/SafetyMonitorUI](DYLIBS/SafetyMonitorUI.md)
- [/System/Library/PrivateFrameworks/Sage.framework/Sage](DYLIBS/Sage.md)
- [/System/Library/PrivateFrameworks/ScreenSharingKit.framework/ScreenSharingKit](DYLIBS/ScreenSharingKit.md)
- [/System/Library/PrivateFrameworks/ScreenTimeUICore.framework/ScreenTimeUICore](DYLIBS/ScreenTimeUICore.md)
- [/System/Library/PrivateFrameworks/SearchFoundation.framework/SearchFoundation](DYLIBS/SearchFoundation.md)
- [/System/Library/PrivateFrameworks/SearchOnDeviceAnalytics.framework/SearchOnDeviceAnalytics](DYLIBS/SearchOnDeviceAnalytics.md)
- [/System/Library/PrivateFrameworks/SearchUI.framework/SearchUI](DYLIBS/SearchUI.md)
- [/System/Library/PrivateFrameworks/SecureCaptureKit.framework/SecureCaptureKit](DYLIBS/SecureCaptureKit.md)
- [/System/Library/PrivateFrameworks/SensitiveContentAnalysisUI.framework/SensitiveContentAnalysisUI](DYLIBS/SensitiveContentAnalysisUI.md)
- [/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts](DYLIBS/SeparationAlerts.md)
- [/System/Library/PrivateFrameworks/SessionCore.framework/SessionCore](DYLIBS/SessionCore.md)
- [/System/Library/PrivateFrameworks/Settings.framework/Settings](DYLIBS/Settings.md)
- [/System/Library/PrivateFrameworks/Settings/GeneralSettingsUI.framework/GeneralSettingsUI](DYLIBS/GeneralSettingsUI.md)
- [/System/Library/PrivateFrameworks/SettingsCellularUI.framework/SettingsCellularUI](DYLIBS/SettingsCellularUI.md)
- [/System/Library/PrivateFrameworks/SeymourClient.framework/SeymourClient](DYLIBS/SeymourClient.md)
- [/System/Library/PrivateFrameworks/SeymourCore.framework/SeymourCore](DYLIBS/SeymourCore.md)
- [/System/Library/PrivateFrameworks/SeymourMedia.framework/SeymourMedia](DYLIBS/SeymourMedia.md)
- [/System/Library/PrivateFrameworks/SeymourServices.framework/SeymourServices](DYLIBS/SeymourServices.md)
- [/System/Library/PrivateFrameworks/SeymourUI.framework/SeymourUI](DYLIBS/SeymourUI.md)
- [/System/Library/PrivateFrameworks/ShaderGraph.framework/ShaderGraph](DYLIBS/ShaderGraph.md)
- [/System/Library/PrivateFrameworks/ShazamCore.framework/ShazamCore](DYLIBS/ShazamCore.md)
- [/System/Library/PrivateFrameworks/ShazamEvents.framework/ShazamEvents](DYLIBS/ShazamEvents.md)
- [/System/Library/PrivateFrameworks/ShazamKitUI.framework/ShazamKitUI](DYLIBS/ShazamKitUI.md)
- [/System/Library/PrivateFrameworks/ShellSceneKit.framework/ShellSceneKit](DYLIBS/ShellSceneKit.md)
- [/System/Library/PrivateFrameworks/ShimGameServices.framework/ShimGameServices](DYLIBS/ShimGameServices.md)
- [/System/Library/PrivateFrameworks/SiriActivation.framework/SiriActivation](DYLIBS/SiriActivation.md)
- [/System/Library/PrivateFrameworks/SiriAnalytics.framework/SiriAnalytics](DYLIBS/SiriAnalytics.md)
- [/System/Library/PrivateFrameworks/SiriAppLaunchIntents.framework/SiriAppLaunchIntents](DYLIBS/SiriAppLaunchIntents.md)
- [/System/Library/PrivateFrameworks/SiriAudioInternal.framework/SiriAudioInternal](DYLIBS/SiriAudioInternal.md)
- [/System/Library/PrivateFrameworks/SiriAudioSupport.framework/SiriAudioSupport](DYLIBS/SiriAudioSupport.md)
- [/System/Library/PrivateFrameworks/SiriAutoComplete.framework/SiriAutoComplete](DYLIBS/SiriAutoComplete.md)
- [/System/Library/PrivateFrameworks/SiriCalendarIntents.framework/SiriCalendarIntents](DYLIBS/SiriCalendarIntents.md)
- [/System/Library/PrivateFrameworks/SiriCalendarUI.framework/SiriCalendarUI](DYLIBS/SiriCalendarUI.md)
- [/System/Library/PrivateFrameworks/SiriCam.framework/SiriCam](DYLIBS/SiriCam.md)
- [/System/Library/PrivateFrameworks/SiriCarCommandsIntents.framework/SiriCarCommandsIntents](DYLIBS/SiriCarCommandsIntents.md)
- [/System/Library/PrivateFrameworks/SiriContactsIntents.framework/SiriContactsIntents](DYLIBS/SiriContactsIntents.md)
- [/System/Library/PrivateFrameworks/SiriContactsUI.framework/SiriContactsUI](DYLIBS/SiriContactsUI.md)
- [/System/Library/PrivateFrameworks/SiriCoreMetrics.framework/SiriCoreMetrics](DYLIBS/SiriCoreMetrics.md)
- [/System/Library/PrivateFrameworks/SiriExpanseInternal.framework/SiriExpanseInternal](DYLIBS/SiriExpanseInternal.md)
- [/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/SiriIdentityInternal](DYLIBS/SiriIdentityInternal.md)
- [/System/Library/PrivateFrameworks/SiriInCall.framework/SiriInCall](DYLIBS/SiriInCall.md)
- [/System/Library/PrivateFrameworks/SiriInference.framework/SiriInference](DYLIBS/SiriInference.md)
- [/System/Library/PrivateFrameworks/SiriKitFlow.framework/SiriKitFlow](DYLIBS/SiriKitFlow.md)
- [/System/Library/PrivateFrameworks/SiriKitRuntime.framework/SiriKitRuntime](DYLIBS/SiriKitRuntime.md)
- [/System/Library/PrivateFrameworks/SiriMailInternal.framework/SiriMailInternal](DYLIBS/SiriMailInternal.md)
- [/System/Library/PrivateFrameworks/SiriMailUI.framework/SiriMailUI](DYLIBS/SiriMailUI.md)
- [/System/Library/PrivateFrameworks/SiriMessageBus.framework/SiriMessageBus](DYLIBS/SiriMessageBus.md)
- [/System/Library/PrivateFrameworks/SiriMessageTypes.framework/SiriMessageTypes](DYLIBS/SiriMessageTypes.md)
- [/System/Library/PrivateFrameworks/SiriMessagesFlow.framework/SiriMessagesFlow](DYLIBS/SiriMessagesFlow.md)
- [/System/Library/PrivateFrameworks/SiriMessagesUI.framework/SiriMessagesUI](DYLIBS/SiriMessagesUI.md)
- [/System/Library/PrivateFrameworks/SiriNLUOverrides.framework/SiriNLUOverrides](DYLIBS/SiriNLUOverrides.md)
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
- [/System/Library/PrivateFrameworks/SiriReferenceResolution.framework/SiriReferenceResolution](DYLIBS/SiriReferenceResolution.md)
- [/System/Library/PrivateFrameworks/SiriRemembers.framework/SiriRemembers](DYLIBS/SiriRemembers.md)
- [/System/Library/PrivateFrameworks/SiriRequestDispatcher.framework/SiriRequestDispatcher](DYLIBS/SiriRequestDispatcher.md)
- [/System/Library/PrivateFrameworks/SiriSettingsIntents.framework/SiriSettingsIntents](DYLIBS/SiriSettingsIntents.md)
- [/System/Library/PrivateFrameworks/SiriSetup.framework/SiriSetup](DYLIBS/SiriSetup.md)
- [/System/Library/PrivateFrameworks/SiriSharedUI.framework/SiriSharedUI](DYLIBS/SiriSharedUI.md)
- [/System/Library/PrivateFrameworks/SiriSignals.framework/SiriSignals](DYLIBS/SiriSignals.md)
- [/System/Library/PrivateFrameworks/SiriSuggestions.framework/SiriSuggestions](DYLIBS/SiriSuggestions.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsAPI.framework/SiriSuggestionsAPI](DYLIBS/SiriSuggestionsAPI.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsIntelligence.framework/SiriSuggestionsIntelligence](DYLIBS/SiriSuggestionsIntelligence.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsKit.framework/SiriSuggestionsKit](DYLIBS/SiriSuggestionsKit.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsSupport.framework/SiriSuggestionsSupport](DYLIBS/SiriSuggestionsSupport.md)
- [/System/Library/PrivateFrameworks/SiriTTSService.framework/SiriTTSService](DYLIBS/SiriTTSService.md)
- [/System/Library/PrivateFrameworks/SiriTranslationIntents.framework/SiriTranslationIntents](DYLIBS/SiriTranslationIntents.md)
- [/System/Library/PrivateFrameworks/SiriTranslationUI.framework/SiriTranslationUI](DYLIBS/SiriTranslationUI.md)
- [/System/Library/PrivateFrameworks/SiriUIActivation.framework/SiriUIActivation](DYLIBS/SiriUIActivation.md)
- [/System/Library/PrivateFrameworks/SiriUIBridge.framework/SiriUIBridge](DYLIBS/SiriUIBridge.md)
- [/System/Library/PrivateFrameworks/SiriUICore.framework/SiriUICore](DYLIBS/SiriUICore.md)
- [/System/Library/PrivateFrameworks/SiriUserSegments.framework/SiriUserSegments](DYLIBS/SiriUserSegments.md)
- [/System/Library/PrivateFrameworks/SiriVideoIntents.framework/SiriVideoIntents](DYLIBS/SiriVideoIntents.md)
- [/System/Library/PrivateFrameworks/SiriVideoUIFramework.framework/SiriVideoUIFramework](DYLIBS/SiriVideoUIFramework.md)
- [/System/Library/PrivateFrameworks/SleepHealthUI.framework/SleepHealthUI](DYLIBS/SleepHealthUI.md)
- [/System/Library/PrivateFrameworks/SleepWidgetUI.framework/SleepWidgetUI](DYLIBS/SleepWidgetUI.md)
- [/System/Library/PrivateFrameworks/SmartReplies.framework/SmartReplies](DYLIBS/SmartReplies.md)
- [/System/Library/PrivateFrameworks/SmartRepliesServer.framework/SmartRepliesServer](DYLIBS/SmartRepliesServer.md)
- [/System/Library/PrivateFrameworks/SnippetKit.framework/SnippetKit](DYLIBS/SnippetKit.md)
- [/System/Library/PrivateFrameworks/SnippetUI.framework/SnippetUI](DYLIBS/SnippetUI.md)
- [/System/Library/PrivateFrameworks/SocialLayer.framework/SocialLayer](DYLIBS/SocialLayer.md)
- [/System/Library/PrivateFrameworks/SoftPosReader.framework/SoftPosReader](DYLIBS/SoftPosReader.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateServicesUI.framework/SoftwareUpdateServicesUI](DYLIBS/SoftwareUpdateServicesUI.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateSettings.framework/SoftwareUpdateSettings](DYLIBS/SoftwareUpdateSettings.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateSettingsUI.framework/SoftwareUpdateSettingsUI](DYLIBS/SoftwareUpdateSettingsUI.md)
- [/System/Library/PrivateFrameworks/SonicFoundation.framework/SonicFoundation](DYLIBS/SonicFoundation.md)
- [/System/Library/PrivateFrameworks/SonicKit.framework/SonicKit](DYLIBS/SonicKit.md)
- [/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon](DYLIBS/SpotlightDaemon.md)
- [/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard](DYLIBS/SpringBoard.md)
- [/System/Library/PrivateFrameworks/SpringBoardHome.framework/SpringBoardHome](DYLIBS/SpringBoardHome.md)
- [/System/Library/PrivateFrameworks/Stateful.framework/Stateful](DYLIBS/Stateful.md)
- [/System/Library/PrivateFrameworks/StocksCore.framework/StocksCore](DYLIBS/StocksCore.md)
- [/System/Library/PrivateFrameworks/StocksUI.framework/StocksUI](DYLIBS/StocksUI.md)
- [/System/Library/PrivateFrameworks/StorageUI.framework/StorageUI](DYLIBS/StorageUI.md)
- [/System/Library/PrivateFrameworks/SummarizationKit.framework/SummarizationKit](DYLIBS/SummarizationKit.md)
- [/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomEvaluator.framework/SymptomEvaluator](DYLIBS/SymptomEvaluator.md)
- [/System/Library/PrivateFrameworks/Synapse.framework/Synapse](DYLIBS/Synapse.md)
- [/System/Library/PrivateFrameworks/SyncedModels.framework/SyncedModels](DYLIBS/SyncedModels.md)
- [/System/Library/PrivateFrameworks/SystemUIAnimationKit.framework/SystemUIAnimationKit](DYLIBS/SystemUIAnimationKit.md)
- [/System/Library/PrivateFrameworks/TDGSharing.framework/TDGSharing](DYLIBS/TDGSharing.md)
- [/System/Library/PrivateFrameworks/TVAppServices.framework/TVAppServices](DYLIBS/TVAppServices.md)
- [/System/Library/PrivateFrameworks/TVRemoteUI.framework/TVRemoteUI](DYLIBS/TVRemoteUI.md)
- [/System/Library/PrivateFrameworks/TeaFoundation.framework/TeaFoundation](DYLIBS/TeaFoundation.md)
- [/System/Library/PrivateFrameworks/TeaSettings.framework/TeaSettings](DYLIBS/TeaSettings.md)
- [/System/Library/PrivateFrameworks/TeaTemplate.framework/TeaTemplate](DYLIBS/TeaTemplate.md)
- [/System/Library/PrivateFrameworks/TeaUI.framework/TeaUI](DYLIBS/TeaUI.md)
- [/System/Library/PrivateFrameworks/TelephonyBlastDoorSupport.framework/TelephonyBlastDoorSupport](DYLIBS/TelephonyBlastDoorSupport.md)
- [/System/Library/PrivateFrameworks/TelephonyUI.framework/TelephonyUI](DYLIBS/TelephonyUI.md)
- [/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer](DYLIBS/TextComposer.md)
- [/System/Library/PrivateFrameworks/TextFormattingUI.framework/TextFormattingUI](DYLIBS/TextFormattingUI.md)
- [/System/Library/PrivateFrameworks/TextInput.framework/TextInput](DYLIBS/TextInput.md)
- [/System/Library/PrivateFrameworks/TextRecognition.framework/TextRecognition](DYLIBS/TextRecognition.md)
- [/System/Library/PrivateFrameworks/TextToSpeech.framework/TextToSpeech](DYLIBS/TextToSpeech.md)
- [/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingUI.framework/TextToSpeechVoiceBankingUI](DYLIBS/TextToSpeechVoiceBankingUI.md)
- [/System/Library/PrivateFrameworks/TextUnderstandingShared.framework/TextUnderstandingShared](DYLIBS/TextUnderstandingShared.md)
- [/System/Library/PrivateFrameworks/TipKitCore.framework/TipKitCore](DYLIBS/TipKitCore.md)
- [/System/Library/PrivateFrameworks/TipKitServices.framework/TipKitServices](DYLIBS/TipKitServices.md)
- [/System/Library/PrivateFrameworks/TipsDaemon.framework/TipsDaemon](DYLIBS/TipsDaemon.md)
- [/System/Library/PrivateFrameworks/TipsTryIt.framework/TipsTryIt](DYLIBS/TipsTryIt.md)
- [/System/Library/PrivateFrameworks/TipsUI.framework/TipsUI](DYLIBS/TipsUI.md)
- [/System/Library/PrivateFrameworks/TokenGeneration.framework/TokenGeneration](DYLIBS/TokenGeneration.md)
- [/System/Library/PrivateFrameworks/TokenGenerationInference.framework/TokenGenerationInference](DYLIBS/TokenGenerationInference.md)
- [/System/Library/PrivateFrameworks/ToolKit.framework/ToolKit](DYLIBS/ToolKit.md)
- [/System/Library/PrivateFrameworks/TouchML.framework/TouchML](DYLIBS/TouchML.md)
- [/System/Library/PrivateFrameworks/TrackingAvoidance.framework/TrackingAvoidance](DYLIBS/TrackingAvoidance.md)
- [/System/Library/PrivateFrameworks/TranslationUI.framework/TranslationUI](DYLIBS/TranslationUI.md)
- [/System/Library/PrivateFrameworks/UARPiCloud.framework/UARPiCloud](DYLIBS/UARPiCloud.md)
- [/System/Library/PrivateFrameworks/UIIntelligenceIntents.framework/UIIntelligenceIntents](DYLIBS/UIIntelligenceIntents.md)
- [/System/Library/PrivateFrameworks/UIIntelligenceSupport.framework/UIIntelligenceSupport](DYLIBS/UIIntelligenceSupport.md)
- [/System/Library/PrivateFrameworks/UIIntelligenceSupportAgent.framework/UIIntelligenceSupportAgent](DYLIBS/UIIntelligenceSupportAgent.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore](DYLIBS/UIKitCore.md)
- [/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices](DYLIBS/UIKitServices.md)
- [/System/Library/PrivateFrameworks/UnifiedMessagingKit.framework/UnifiedMessagingKit](DYLIBS/UnifiedMessagingKit.md)
- [/System/Library/PrivateFrameworks/UniversalDrag.framework/UniversalDrag](DYLIBS/UniversalDrag.md)
- [/System/Library/PrivateFrameworks/UniversalHID.framework/UniversalHID](DYLIBS/UniversalHID.md)
- [/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_apfs.dylib](DYLIBS/livefiles_apfs.dylib.md)
- [/System/Library/PrivateFrameworks/UserNotificationsCore.framework/UserNotificationsCore](DYLIBS/UserNotificationsCore.md)
- [/System/Library/PrivateFrameworks/UserNotificationsUIKit.framework/UserNotificationsUIKit](DYLIBS/UserNotificationsUIKit.md)
- [/System/Library/PrivateFrameworks/VFX.framework/VFX](DYLIBS/VFX.md)
- [/System/Library/PrivateFrameworks/VideosUI.framework/VideosUI](DYLIBS/VideosUI.md)
- [/System/Library/PrivateFrameworks/VisionKitInternal.framework/VisionKitInternal](DYLIBS/VisionKitInternal.md)
- [/System/Library/PrivateFrameworks/VisualGeneration.framework/VisualGeneration](DYLIBS/VisualGeneration.md)
- [/System/Library/PrivateFrameworks/VisualIntelligence.framework/VisualIntelligence](DYLIBS/VisualIntelligence.md)
- [/System/Library/PrivateFrameworks/VoiceActions.framework/VoiceActions](DYLIBS/VoiceActions.md)
- [/System/Library/PrivateFrameworks/VoiceControlUI.framework/VoiceControlUI](DYLIBS/VoiceControlUI.md)
- [/System/Library/PrivateFrameworks/VoiceMemos.framework/VoiceMemos](DYLIBS/VoiceMemos.md)
- [/System/Library/PrivateFrameworks/VoiceShortcuts.framework/VoiceShortcuts](DYLIBS/VoiceShortcuts.md)
- [/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/VoiceTriggerUI](DYLIBS/VoiceTriggerUI.md)
- [/System/Library/PrivateFrameworks/WPDaemon.framework/WPDaemon](DYLIBS/WPDaemon.md)
- [/System/Library/PrivateFrameworks/WallpaperKit.framework/WallpaperKit](DYLIBS/WallpaperKit.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/WatchFacesWallpaperSupport](DYLIBS/WatchFacesWallpaperSupport.md)
- [/System/Library/PrivateFrameworks/WeatherAnalytics.framework/WeatherAnalytics](DYLIBS/WeatherAnalytics.md)
- [/System/Library/PrivateFrameworks/WeatherCore.framework/WeatherCore](DYLIBS/WeatherCore.md)
- [/System/Library/PrivateFrameworks/WeatherDaemon.framework/WeatherDaemon](DYLIBS/WeatherDaemon.md)
- [/System/Library/PrivateFrameworks/WeatherMaps.framework/WeatherMaps](DYLIBS/WeatherMaps.md)
- [/System/Library/PrivateFrameworks/WeatherUI.framework/WeatherUI](DYLIBS/WeatherUI.md)
- [/System/Library/PrivateFrameworks/WebCore.framework/Frameworks/libANGLE-shared.dylib](DYLIBS/libANGLE-shared.dylib.md)
- [/System/Library/PrivateFrameworks/WebCore.framework/WebCore](DYLIBS/WebCore.md)
- [/System/Library/PrivateFrameworks/WebKitLegacy.framework/WebKitLegacy](DYLIBS/WebKitLegacy.md)
- [/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics](DYLIBS/WiFiAnalytics.md)
- [/System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI](DYLIBS/WiFiKitUI.md)
- [/System/Library/PrivateFrameworks/WidgetRenderer.framework/WidgetRenderer](DYLIBS/WidgetRenderer.md)
- [/System/Library/PrivateFrameworks/WorkflowEditor.framework/WorkflowEditor](DYLIBS/WorkflowEditor.md)
- [/System/Library/PrivateFrameworks/WorkflowKit.framework/WorkflowKit](DYLIBS/WorkflowKit.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/WorkflowUI](DYLIBS/WorkflowUI.md)
- [/System/Library/PrivateFrameworks/WorkflowUICore.framework/WorkflowUICore](DYLIBS/WorkflowUICore.md)
- [/System/Library/PrivateFrameworks/WorkflowUIServices.framework/WorkflowUIServices](DYLIBS/WorkflowUIServices.md)
- [/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/WorkoutAnnouncements](DYLIBS/WorkoutAnnouncements.md)
- [/System/Library/PrivateFrameworks/WorkoutUI.framework/WorkoutUI](DYLIBS/WorkoutUI.md)
- [/System/Library/PrivateFrameworks/_JetEngine_SwiftUI.framework/_JetEngine_SwiftUI](DYLIBS/_JetEngine_SwiftUI.md)
- [/System/Library/PrivateFrameworks/_MusicKitInternal_SwiftUI.framework/_MusicKitInternal_SwiftUI](DYLIBS/_MusicKitInternal_SwiftUI.md)
- [/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore](DYLIBS/iCloudDriveCore.md)
- [/System/Library/PrivateFrameworks/iCloudMailAccountUI.framework/iCloudMailAccountUI](DYLIBS/iCloudMailAccountUI.md)
- [/System/Library/PrivateFrameworks/iCloudSettings.framework/iCloudSettings](DYLIBS/iCloudSettings.md)
- [/System/Library/PrivateFrameworks/ktrace.framework/ktrace](DYLIBS/ktrace.md)
- [/System/Library/VideoDecoders/AVD.videodecoder](DYLIBS/AVD.videodecoder.md)
- [/System/Library/VideoDecoders/H264H8.videodecoder](DYLIBS/H264H8.videodecoder.md)
- [/System/Library/VideoEncoders/H264H9.videoencoder](DYLIBS/H264H9.videoencoder.md)
- [/System/Library/VideoEncoders/H9.videoencoder](DYLIBS/H9.videoencoder.md)
- [/usr/lib/dyld](DYLIBS/dyld.md)
- [/usr/lib/libATCommandStudioDynamic.dylib](DYLIBS/libATCommandStudioDynamic.dylib.md)
- [/usr/lib/libAppletTranslationLibrary.dylib](DYLIBS/libAppletTranslationLibrary.dylib.md)
- [/usr/lib/libBBUpdaterDynamic.dylib](DYLIBS/libBBUpdaterDynamic.dylib.md)
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
- [/usr/lib/libPN548_API.dylib](DYLIBS/libPN548_API.dylib.md)
- [/usr/lib/libQMIParserDynamic.dylib](DYLIBS/libQMIParserDynamic.dylib.md)
- [/usr/lib/libSoftwareUpdateSSO.dylib](DYLIBS/libSoftwareUpdateSSO.dylib.md)
- [/usr/lib/libTelephonyBasebandDynamic.dylib](DYLIBS/libTelephonyBasebandDynamic.dylib.md)
- [/usr/lib/libTelephonyCapabilities.dylib](DYLIBS/libTelephonyCapabilities.dylib.md)
- [/usr/lib/libTelephonyDebugDynamic.dylib](DYLIBS/libTelephonyDebugDynamic.dylib.md)
- [/usr/lib/libTelephonyUtilDynamic.dylib](DYLIBS/libTelephonyUtilDynamic.dylib.md)
- [/usr/lib/libVinylNonUpdater.dylib](DYLIBS/libVinylNonUpdater.dylib.md)
- [/usr/lib/libauthinstall.dylib](DYLIBS/libauthinstall.dylib.md)
- [/usr/lib/libcoreroutine.dylib](DYLIBS/libcoreroutine.dylib.md)
- [/usr/lib/libcryptex.dylib](DYLIBS/libcryptex.dylib.md)
- [/usr/lib/libcryptex_core.dylib](DYLIBS/libcryptex_core.dylib.md)
- [/usr/lib/libcryptex_interface.dylib](DYLIBS/libcryptex_interface.dylib.md)
- [/usr/lib/libcryptex_trampoline.dylib](DYLIBS/libcryptex_trampoline.dylib.md)
- [/usr/lib/libindus.dylib](DYLIBS/libindus.dylib.md)
- [/usr/lib/libmdns.dylib](DYLIBS/libmdns.dylib.md)
- [/usr/lib/libsqlite3.dylib](DYLIBS/libsqlite3.dylib.md)
- [/usr/lib/libswiftPrespecialized.dylib](DYLIBS/libswiftPrespecialized.dylib.md)
- [/usr/lib/libxslt.1.dylib](DYLIBS/libxslt.1.dylib.md)
- [/usr/lib/log/liblog_SystemConfiguration.dylib](DYLIBS/liblog_SystemConfiguration.dylib.md)
- [/usr/lib/swift/libswiftAVFoundation.dylib](DYLIBS/libswiftAVFoundation.dylib.md)
- [/usr/lib/swift/libswiftAccelerate.dylib](DYLIBS/libswiftAccelerate.dylib.md)
- [/usr/lib/swift/libswiftSpatial.dylib](DYLIBS/libswiftSpatial.dylib.md)
- [/usr/lib/swift/libswiftSystem.dylib](DYLIBS/libswiftSystem.dylib.md)
- [/usr/lib/swift/libswiftUIKit.dylib](DYLIBS/libswiftUIKit.dylib.md)
- [/usr/lib/swift/libswiftXPC.dylib](DYLIBS/libswiftXPC.dylib.md)
- [/usr/lib/system/liblaunch.dylib](DYLIBS/liblaunch.dylib.md)
- [/usr/lib/updaters/libAce3Updater.dylib](DYLIBS/libAce3Updater.dylib.md)
- [/usr/lib/updaters/libVinylUpdater.dylib](DYLIBS/libVinylUpdater.dylib.md)

</details>

## EOF
