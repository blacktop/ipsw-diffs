# 18.4 (22E240) .vs 18.5 (22F5042g)

## IPSWs

- `iPhone17,1_18.4_22E240_Restore.ipsw`
- `iPhone17,1_18.5_22F5042g_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 18.4 *(22E240)* | 24.4.0 | 11417.102.9~20 | Sat, 15Mar2025 18:26:55 PDT |
| 18.5 *(22F5042g)* | 24.5.0 | 11417.120.80.0.3~45 | Mon, 24Mar2025 20:10:57 PDT |

### Kexts

#### 🆕 NEW (1)

- `com.apple.kec.AppleEncryptedArchive`

#### ⬆️ Updated (30)

<details>
  <summary><i>View Updated</i></summary>

>  `com.apple.driver.AppleAOPAudio`

```diff

   __TEXT.__cstring: 0xc591
   __TEXT.__const: 0x136
   __TEXT.__os_log: 0xf
-  __TEXT_EXEC.__text: 0x31a24
+  __TEXT_EXEC.__text: 0x31a10
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2f0
   __DATA.__common: 0x660
   __DATA.__bss: 0x49
-  __DATA_CONST.__auth_got: 0x328
+  __DATA_CONST.__auth_got: 0x318
   __DATA_CONST.__got: 0xe8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0xe8
CStrings:
+ "19:55:11"
+ "19:55:16"
+ "Mar 24 2025"
- "19:46:32"
- "19:46:33"
- "Mar 17 2025"

```

>  `com.apple.driver.AppleAVD`

```diff

 862.0.0.0.0
-  __TEXT.__os_log: 0x16b7a
-  __TEXT.__cstring: 0x5a23
-  __TEXT.__const: 0xe1678
-  __TEXT_EXEC.__text: 0x5e2f4
+  __TEXT.__os_log: 0x15e72
+  __TEXT.__cstring: 0x59b2
+  __TEXT.__const: 0xcebf8
+  __TEXT_EXEC.__text: 0x5a454
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x12dc
   __DATA.__common: 0x78

   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0x4388
-  __DATA_CONST.__kalloc_type: 0x32c0
-  __DATA_CONST.__kalloc_var: 0xff0
-  Functions: 1987
+  __DATA_CONST.__const: 0x4098
+  __DATA_CONST.__kalloc_type: 0x30c0
+  __DATA_CONST.__kalloc_var: 0xfa0
+  Functions: 1904
   Symbols:   0
-  CStrings:  1574
+  CStrings:  1568
 
CStrings:
- "CAvdApCommThyme"
- "CAvdMcpuThyme"
- "CAvdWrapCtrlThyme"
- "site.CAvdApCommThyme"
- "site.CAvdMcpuThyme"
- "site.CPriorityQueueThyme"

```

>  `com.apple.driver.AppleBasebandPCI`

```diff

-852.0.0.0.0
-  __TEXT.__cstring: 0x37b3
-  __TEXT.__const: 0x23e9
-  __TEXT_EXEC.__text: 0x34714
+853.0.0.0.0
+  __TEXT.__cstring: 0xc1e4
+  __TEXT.__const: 0x2449
+  __TEXT_EXEC.__text: 0x7764c
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x33c
-  __DATA.__common: 0x5a0
-  __DATA.__bss: 0x78
-  __DATA_CONST.__auth_got: 0x560
-  __DATA_CONST.__got: 0x178
-  __DATA_CONST.__mod_init_func: 0x768
-  __DATA_CONST.__mod_term_func: 0xc8
-  __DATA_CONST.__const: 0x7bb0
-  __DATA_CONST.__kalloc_type: 0x1980
-  __DATA_CONST.__kalloc_var: 0x550
-  Functions: 1853
+  __DATA.__data: 0x3f8
+  __DATA.__common: 0x648
+  __DATA.__bss: 0x80
+  __DATA_CONST.__auth_got: 0x620
+  __DATA_CONST.__got: 0x180
+  __DATA_CONST.__mod_init_func: 0x788
+  __DATA_CONST.__mod_term_func: 0xe8
+  __DATA_CONST.__const: 0x86b8
+  __DATA_CONST.__kalloc_type: 0x1d80
+  __DATA_CONST.__kalloc_var: 0x690
+  Functions: 2014
   Symbols:   0
-  CStrings:  441
+  CStrings:  1364
 
CStrings:
+ "\t%06ld.%06d %s %llx\n"
+ "%02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x"
+ "%06ld.%06d %s::%s: \n"
+ "%06ld.%06d %s::%s:  --done\n"
+ "%06ld.%06d %s::%s:  MSI owner cannot be NULL\n"
+ "%06ld.%06d %s::%s:  MSI owner or handler cannot be NULL\n"
+ "%06ld.%06d %s::%s:  PDP manager registration with IP Appender failed\n"
+ "%06ld.%06d %s::%s:  Type= %s\n HwClass= %s\n HwError= %s\n IsWrite= %s\n HwStatus= %#llX\n SID= %#llx\n Address= %#llx\n"
+ "%06ld.%06d %s::%s:  qctun interface tx slot count: %u\n"
+ "%06ld.%06d %s::%s: \"%s\" not found in plist\n"
+ "%06ld.%06d %s::%s: %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x\n"
+ "%06ld.%06d %s::%s: %d\n"
+ "%06ld.%06d %s::%s: %s\n"
+ "%06ld.%06d %s::%s: %s -> %s\n"
+ "%06ld.%06d %s::%s: %s TCP packet: len %u, seq %u, ack %u\n"
+ "%06ld.%06d %s::%s: %s override\n"
+ "%06ld.%06d %s::%s: %s rx slot count %u\n"
+ "%06ld.%06d %s::%s: %s tx slot count %u\n"
+ "%06ld.%06d %s::%s: %s%02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x\n"
+ "%06ld.%06d %s::%s: %s%s\n"
+ "%06ld.%06d %s::%s: %s: --> \n"
+ "%06ld.%06d %s::%s: %u\n"
+ "%06ld.%06d %s::%s: (async) failed client is not attached\n"
+ "%06ld.%06d %s::%s: (async) failed to create memory decriptor\n"
+ "%06ld.%06d %s::%s: (async) failed to prepare image command\n"
+ "%06ld.%06d %s::%s: (async) failed to prepare memory command\n"
+ "%06ld.%06d %s::%s: (async) returned 0x%x\n"
+ "%06ld.%06d %s::%s: (sync < 4K) failed client is not attached\n"
+ "%06ld.%06d %s::%s: (sync < 4K) failed to create memory decriptor\n"
+ "%06ld.%06d %s::%s: (sync < 4K) failed to prepare image command\n"
+ "%06ld.%06d %s::%s: (sync < 4K) failed to prepare memory command\n"
+ "%06ld.%06d %s::%s: (sync < 4K) returned 0x%x\n"
+ "%06ld.%06d %s::%s: (sync > 4K) failed client is not attached\n"
+ "%06ld.%06d %s::%s: (sync > 4K) failed to prepare image command\n"
+ "%06ld.%06d %s::%s: (sync > 4K) failed to prepare memory command\n"
+ "%06ld.%06d %s::%s: (sync > 4K) no memory decriptor\n"
+ "%06ld.%06d %s::%s: (sync > 4K) returned 0x%x\n"
+ "%06ld.%06d %s::%s: +\n"
+ "%06ld.%06d %s::%s: -\n"
+ "%06ld.%06d %s::%s: -- done\n"
+ "%06ld.%06d %s::%s: -- done %u\n"
+ "%06ld.%06d %s::%s: --done\n"
+ "%06ld.%06d %s::%s: AER was already registered\n"
+ "%06ld.%06d %s::%s: ASPML1 disabled on endpoint\n"
+ "%06ld.%06d %s::%s: ASPML1 disabled on root port\n"
+ "%06ld.%06d %s::%s: AppleBasebandPCI workloop onThread %u, inGate %u\n"
+ "%06ld.%06d %s::%s: AppleBasebandPCIControl workloop onThread %u, inGate %u\n"
+ "%06ld.%06d %s::%s: Base Rx slot count not found in plist\n"
+ "%06ld.%06d %s::%s: Base Tx slot count not found in plist\n"
+ "%06ld.%06d %s::%s: Bearer switch trigger failed, ret: 0x%08x\n"
+ "%06ld.%06d %s::%s: Client lacks entitlement\n"
+ "%06ld.%06d %s::%s: Closing pci service: %p\n"
+ "%06ld.%06d %s::%s: Could not open PCI service\n"
+ "%06ld.%06d %s::%s: Created qctun interface, pService: %p\n"
+ "%06ld.%06d %s::%s: Creating QueueSet failed, index: %u\n"
+ "%06ld.%06d %s::%s: Creating logical link failed\n"
+ "%06ld.%06d %s::%s: Creating qctun interface\n"
+ "%06ld.%06d %s::%s: Creating queue sets for logical link failed\n"
+ "%06ld.%06d %s::%s: DART error handler registeration failed!, ret: 0x%08x\n"
+ "%06ld.%06d %s::%s: DART window: 0x%llx --> 0x%llx\n"
+ "%06ld.%06d %s::%s: DL limit set to %u\n"
+ "%06ld.%06d %s::%s: De-Allocate pkts directly to pool, dir: %lu\n"
+ "%06ld.%06d %s::%s: Default pci service not published! enabled: %u, shouldEnable: %u\n"
+ "%06ld.%06d %s::%s: Default soft flow control thresholds: on %u, off %u\n"
+ "%06ld.%06d %s::%s: Device Status/Control register: 0x%lx, isPending: %u\n"
+ "%06ld.%06d %s::%s: DeviceCtl 0x%08x DeviceStatus 0x%08x LinkStatus 0x%08x\n"
+ "%06ld.%06d %s::%s: Enqueue failed, dir: %u, ret: 0x%08x\n"
+ "%06ld.%06d %s::%s: Failed to allocate memory for interface advisory report\n"
+ "%06ld.%06d %s::%s: Failed to calculate qctun buffer pool capacity!\n"
+ "%06ld.%06d %s::%s: Failed to create Create Dedicated Queue Set\n"
+ "%06ld.%06d %s::%s: Failed to create Create Default Queue Set\n"
+ "%06ld.%06d %s::%s: Failed to create logical link!\n"
+ "%06ld.%06d %s::%s: Failed to create/attach interface, 0x%x\n"
+ "%06ld.%06d %s::%s: Failed to get Transaction Pending bit, ret: 0x%llx\n"
+ "%06ld.%06d %s::%s: Failed to get device reset state!\n"
+ "%06ld.%06d %s::%s: Failed to read AER Capability Structure\n"
+ "%06ld.%06d %s::%s: Failed to read PCIe Express Capability Structure\n"
+ "%06ld.%06d %s::%s: Flow control service not active\n"
+ "%06ld.%06d %s::%s: Getting BB reset state failed\n"
+ "%06ld.%06d %s::%s: HMAP VSEC regs(@0x%x)= 0x%x\n"
+ "%06ld.%06d %s::%s: HMAP capability not found\n"
+ "%06ld.%06d %s::%s: HeaderLog 0 to 3 0x%08x 0x%08x 0x%x 0x%08x\n"
+ "%06ld.%06d %s::%s: IOMemoryDescriptor %p\n"
+ "%06ld.%06d %s::%s: IOMemoryDescriptor %p, info 0x%llx\n"
+ "%06ld.%06d %s::%s: IOSkywalkFamily querying free space, interface: %u, returning: %u\n"
+ "%06ld.%06d %s::%s: IPAppender message, message: 0x%u\n"
+ "%06ld.%06d %s::%s: Init failed, intf: %p, manager: %p\n"
+ "%06ld.%06d %s::%s: Interface non-existent interface ID: %u\n"
+ "%06ld.%06d %s::%s: Interface: %u, Rx pkt compl cnt: %lu\n"
+ "%06ld.%06d %s::%s: Interface: %u, Tx pkt compl cnt: %lu\n"
+ "%06ld.%06d %s::%s: Invalid POSTROM link speed setting, will use defaults\n"
+ "%06ld.%06d %s::%s: Invalid ROM link speed setting, will use defaults\n"
+ "%06ld.%06d %s::%s: Invalid bearer ID\n"
+ "%06ld.%06d %s::%s: Invalid data service: %u\n"
+ "%06ld.%06d %s::%s: Invalid direction, dir: %u\n"
+ "%06ld.%06d %s::%s: Invalid direction, direction: %u\n"
+ "%06ld.%06d %s::%s: Invalid filter rule, descriptor type: \n"
+ "%06ld.%06d %s::%s: Invalid interface ID: %u\n"
+ "%06ld.%06d %s::%s: Invalid payload length, expected: %u, received: %u\n"
+ "%06ld.%06d %s::%s: Invalid service ID: %u\n"
+ "%06ld.%06d %s::%s: L1SS control 1 reg: 0x%x\n"
+ "%06ld.%06d %s::%s: L1SS control 2 reg: 0x%x\n"
+ "%06ld.%06d %s::%s: Logical link NOT supported!\n"
+ "%06ld.%06d %s::%s: Low Latency data NOT supported!\n"
+ "%06ld.%06d %s::%s: MSI address 0x%x\n"
+ "%06ld.%06d %s::%s: MSI capability not found\n"
+ "%06ld.%06d %s::%s: MSI registration failed with pci service, ret: 0x%08x\n"
+ "%06ld.%06d %s::%s: MSI registration for index %u already exists!\n"
+ "%06ld.%06d %s::%s: Mapped bearer ID: %u, queueSetID: 0x%llx\n"
+ "%06ld.%06d %s::%s: NOT EOT, bail! status 0x%x, size %u, eot %d\n"
+ "%06ld.%06d %s::%s: NULL input argument(s)\n"
+ "%06ld.%06d %s::%s: NULL logical link\n"
+ "%06ld.%06d %s::%s: NULL message argument\n"
+ "%06ld.%06d %s::%s: NULL output arguments\n"
+ "%06ld.%06d %s::%s: NULL payload\n"
+ "%06ld.%06d %s::%s: NULL traffic descriptor\n"
+ "%06ld.%06d %s::%s: Network stack rejected link status report: 0x%x\n"
+ "%06ld.%06d %s::%s: Not a valid PCI service\n"
+ "%06ld.%06d %s::%s: Not in low power, bailing!\n"
+ "%06ld.%06d %s::%s: Not supported for non logical link interfaces\n"
+ "%06ld.%06d %s::%s: Opened successfully! _pciService: %p\n"
+ "%06ld.%06d %s::%s: Opening PCI data service failed, ret: 0x%08x\n"
+ "%06ld.%06d %s::%s: Opening _pciService: %p\n"
+ "%06ld.%06d %s::%s: Opening pci service: %p\n"
+ "%06ld.%06d %s::%s: PCI notification\n"
+ "%06ld.%06d %s::%s: PCI service to switch not active, service ID: %u\n"
+ "%06ld.%06d %s::%s: PCIE capability not found\n"
+ "%06ld.%06d %s::%s: PCIe link is down or is going down\n"
+ "%06ld.%06d %s::%s: PDP event oob allocation, check for potential flaw\n"
+ "%06ld.%06d %s::%s: PDP manager service not active\n"
+ "%06ld.%06d %s::%s: PDP manager stopped\n"
+ "%06ld.%06d %s::%s: POSTROM link speed overridden to: %u\n"
+ "%06ld.%06d %s::%s: Packet dump\n"
+ "%06ld.%06d %s::%s: Queue Set ID: %u\n"
+ "%06ld.%06d %s::%s: ROM link speed overridden to: %u\n"
+ "%06ld.%06d %s::%s: Read config space link speed: %u\n"
+ "%06ld.%06d %s::%s: Received AER, Config Reg Space Dump : UnCorErrStat 0x%08x CorrErrStat 0x%08x AERCapCtl 0x%08x\n"
+ "%06ld.%06d %s::%s: Removed region ID: %u from list\n"
+ "%06ld.%06d %s::%s: Reporting interface advisory failed, ret: 0x%08x %u\n"
+ "%06ld.%06d %s::%s: Returning packet: %p\n"
+ "%06ld.%06d %s::%s: Rx SubQ finalize failed, ret: 0x%llx\n"
+ "%06ld.%06d %s::%s: Rx dequeue request\n"
+ "%06ld.%06d %s::%s: Rx pkt -  Sub cnt: %u, Compl cnt: %lu\n"
+ "%06ld.%06d %s::%s: Rx pkt compl cnt: %lu\n"
+ "%06ld.%06d %s::%s: Rx subQ not enabled\n"
+ "%06ld.%06d %s::%s: Rx, default queueset: %u\n"
+ "%06ld.%06d %s::%s: Setting link control2 to: 0x%08x, new target link speed: %u\n"
+ "%06ld.%06d %s::%s: Skip creating qctun intf, qctun_enabled: %u\n"
+ "%06ld.%06d %s::%s: Skip dedicated bearer switch for IMS\n"
+ "%06ld.%06d %s::%s: Skip queue set disable for IMS\n"
+ "%06ld.%06d %s::%s: Skip service id: %u, not a data pci service\n"
+ "%06ld.%06d %s::%s: Soft flow control off: %u\n"
+ "%06ld.%06d %s::%s: Soft flow control on: %u\n"
+ "%06ld.%06d %s::%s: TBD: HMAP MSI-X support\n"
+ "%06ld.%06d %s::%s: Timout waiting for bridge to power off! Continuing with potentially unsafe port disable.\n"
+ "%06ld.%06d %s::%s: Transaction Pending bit cleared (count: %u)\n"
+ "%06ld.%06d %s::%s: Transaction Pending bit poll timed out\n"
+ "%06ld.%06d %s::%s: Trigger MSI failed - No event source\n"
+ "%06ld.%06d %s::%s: Tx pkt -  Sub cnt: %u, Compl cnt: %lu\n"
+ "%06ld.%06d %s::%s: Tx pkt compl cnt: %lu\n"
+ "%06ld.%06d %s::%s: Tx subQ not enabled\n"
+ "%06ld.%06d %s::%s: Tx, default queueset: %u\n"
+ "%06ld.%06d %s::%s: Unable to find the mapped queue set, bearer ID: %u, isDefaultBearer: %u !\n"
+ "%06ld.%06d %s::%s: Unable to map to queue set! bearer ID: %u, isDefaultBearer: %u\n"
+ "%06ld.%06d %s::%s: Unmapping bearer ID: %u from queue set failed\n"
+ "%06ld.%06d %s::%s: Unsupported direction: %u"
+ "%06ld.%06d %s::%s: Unsupported direction: %u\n"
+ "%06ld.%06d %s::%s: Unsupported notification type: %u\n"
+ "%06ld.%06d %s::%s: VSEC ID at offset 0x%x matched HMAP 0x%x\n"
+ "%06ld.%06d %s::%s: VSEC ID at offset 0x%x not matched HMAP. Expected 0x0024, found 0x%x\n"
+ "%06ld.%06d %s::%s: _asyncMode 0x%08x, asyncMode 0x%08x, arg1 %p\n"
+ "%06ld.%06d %s::%s: _enabled: %u\n"
+ "%06ld.%06d %s::%s: _inLowPower %u\n"
+ "%06ld.%06d %s::%s: _mapper %p\n"
+ "%06ld.%06d %s::%s: _mediaInterfaceCount = %u\n"
+ "%06ld.%06d %s::%s: _mediaInterfaceMaxPendingWriteBytes = %u\n"
+ "%06ld.%06d %s::%s: _mediaInterfaceStart = %u\n"
+ "%06ld.%06d %s::%s: _memoryAlloc %u\n"
+ "%06ld.%06d %s::%s: _pciService: %p\n"
+ "%06ld.%06d %s::%s: _pendLockPort %u\n"
+ "%06ld.%06d %s::%s: _pendPortEnable %u\n"
+ "%06ld.%06d %s::%s: _vmForce: 0x%llx\n"
+ "%06ld.%06d %s::%s: _wiredCount: %u\n"
+ "%06ld.%06d %s::%s: _workLoopControl was not set yet\n"
+ "%06ld.%06d %s::%s: action %s\n"
+ "%06ld.%06d %s::%s: async call failed with 0x%08x\n"
+ "%06ld.%06d %s::%s: asyncMode 0x%08x\n"
+ "%06ld.%06d %s::%s: attempts %d\n"
+ "%06ld.%06d %s::%s: bad refCon %p, _pciPublishNotifier %p, _pciTerminateNotifier %p\n"
+ "%06ld.%06d %s::%s: bar0 %p\n"
+ "%06ld.%06d %s::%s: baseband chipset unknown, using default\n"
+ "%06ld.%06d %s::%s: baseband service is %s\n"
+ "%06ld.%06d %s::%s: bearer ID : %u, switched to default data service!\n"
+ "%06ld.%06d %s::%s: bearer ID : %u, switched to low latency data service!\n"
+ "%06ld.%06d %s::%s: bearer ID: %u, enable: %u, serviceID: %u\n"
+ "%06ld.%06d %s::%s: bearerID: %u, interfaceID: %u, enable: %u, ipAppenderSvc: %u\n"
+ "%06ld.%06d %s::%s: blockForCommand %u\n"
+ "%06ld.%06d %s::%s: bootStage %u\n"
+ "%06ld.%06d %s::%s: buff %p, size %u\n"
+ "%06ld.%06d %s::%s: buff %p, size %u, info 0x%llx\n"
+ "%06ld.%06d %s::%s: buff 0x%llx, size %llu, completion %p\n"
+ "%06ld.%06d %s::%s: buff 0x%llx, size %llu, flush %d, completion %p\n"
+ "%06ld.%06d %s::%s: buff 0x%llx, size %u, completion %p\n"
+ "%06ld.%06d %s::%s: buffer allocation of %uB failed\n"
+ "%06ld.%06d %s::%s: calling _provider->close()\n"
+ "%06ld.%06d %s::%s: can't allocate map\n"
+ "%06ld.%06d %s::%s: cf %p, arg0 %p, arg1 %p\n"
+ "%06ld.%06d %s::%s: cf %p, intervalUs %llu, arg0 %p, arg1 %p\n"
+ "%06ld.%06d %s::%s: checking link speed, expect %u\n"
+ "%06ld.%06d %s::%s: cmdSize %llu\n"
+ "%06ld.%06d %s::%s: cmdSize %llu, policyInfo %p\n"
+ "%06ld.%06d %s::%s: command %p\n"
+ "%06ld.%06d %s::%s: command packets exhausted\n"
+ "%06ld.%06d %s::%s: command: %p\n"
+ "%06ld.%06d %s::%s: count (%u) > gaurantee (%u) + speculative (%u) counts\n "
+ "%06ld.%06d %s::%s: count: %u\n"
+ "%06ld.%06d %s::%s: count: %u, dequeued: %u\n"
+ "%06ld.%06d %s::%s: creating dedicated queue set, index: %u\n"
+ "%06ld.%06d %s::%s: creating default queue set, index: %u\n"
+ "%06ld.%06d %s::%s: current asyncMode 0x%08x\n"
+ "%06ld.%06d %s::%s: current state: %s\n"
+ "%06ld.%06d %s::%s: dealloc packet %p directly\n"
+ "%06ld.%06d %s::%s: dedicated queue set [ %u ]: %u\n"
+ "%06ld.%06d %s::%s: default queue set [ %u ]: %u\n"
+ "%06ld.%06d %s::%s: default queue set config is NULL!\n"
+ "%06ld.%06d %s::%s: device %p, powerStateOrdinal %lu\n"
+ "%06ld.%06d %s::%s: device %p, stateNumber %lu\n"
+ "%06ld.%06d %s::%s: device descriptor name: %s\n"
+ "%06ld.%06d %s::%s: device name: %s, pcie reset sep workaround needed: %d\n"
+ "%06ld.%06d %s::%s: dir: %u\n"
+ "%06ld.%06d %s::%s: direction %s, completion %p\n"
+ "%06ld.%06d %s::%s: domain %u\n"
+ "%06ld.%06d %s::%s: domain: %u, buff 0x%llx, size %llu, completion %p\n"
+ "%06ld.%06d %s::%s: domainState: 0x%lx\n"
+ "%06ld.%06d %s::%s: enable %u\n"
+ "%06ld.%06d %s::%s: enable %u, failureFatal %u, enabled state: %u\n"
+ "%06ld.%06d %s::%s: enable AER notification\n"
+ "%06ld.%06d %s::%s: enable interrupt %u\n"
+ "%06ld.%06d %s::%s: enable sleep %u\n"
+ "%06ld.%06d %s::%s: enable: %u\n"
+ "%06ld.%06d %s::%s: enablePCIPowerManagement failed 0x%x\n"
+ "%06ld.%06d %s::%s: enabled %u, status 0x%08x\n"
+ "%06ld.%06d %s::%s: enabled %u, status 0x%x\n"
+ "%06ld.%06d %s::%s: enabled: %u, shouldEnable: %u\n"
+ "%06ld.%06d %s::%s: enabling L1SS\n"
+ "%06ld.%06d %s::%s: endpoint L1PMSS capability not found\n"
+ "%06ld.%06d %s::%s: endpoint port PCIe capability not found\n"
+ "%06ld.%06d %s::%s: error type %u, arg0 %p, arg1 %p\n"
+ "%06ld.%06d %s::%s: failed bytes %llu, size %llu\n"
+ "%06ld.%06d %s::%s: failed client is not attached\n"
+ "%06ld.%06d %s::%s: failed err %d\n"
+ "%06ld.%06d %s::%s: failed to add AER event source\n"
+ "%06ld.%06d %s::%s: failed to add Rx submission queue event source workLoop: 0x%x\n"
+ "%06ld.%06d %s::%s: failed to add interrupt source\n"
+ "%06ld.%06d %s::%s: failed to add matching notification - Default\n"
+ "%06ld.%06d %s::%s: failed to add node\n"
+ "%06ld.%06d %s::%s: failed to allocate MessageQueue\n"
+ "%06ld.%06d %s::%s: failed to allocate Queues\n"
+ "%06ld.%06d %s::%s: failed to allocate _lock\n"
+ "%06ld.%06d %s::%s: failed to allocate _pciServiceLock\n"
+ "%06ld.%06d %s::%s: failed to allocate _rdQueueLock\n"
+ "%06ld.%06d %s::%s: failed to allocate commandGate\n"
+ "%06ld.%06d %s::%s: failed to allocate io command\n"
+ "%06ld.%06d %s::%s: failed to allocate link speed timer\n"
+ "%06ld.%06d %s::%s: failed to allocate memory\n"
+ "%06ld.%06d %s::%s: failed to allocate timer\n"
+ "%06ld.%06d %s::%s: failed to allocate workloop\n"
+ "%06ld.%06d %s::%s: failed to allocatePrepareMemory 0x%x\n"
+ "%06ld.%06d %s::%s: failed to calculate pool capacity\n"
+ "%06ld.%06d %s::%s: failed to create AER event source\n"
+ "%06ld.%06d %s::%s: failed to create AppleBasebandPCIIOCommand node\n"
+ "%06ld.%06d %s::%s: failed to create AppleBasebandPCIMemoryCommand node\n"
+ "%06ld.%06d %s::%s: failed to create AppleBasebandPCIMemoryPolicy node\n"
+ "%06ld.%06d %s::%s: failed to create AppleBasebandPCIRequest node\n"
+ "%06ld.%06d %s::%s: failed to create DMA command\n"
+ "%06ld.%06d %s::%s: failed to create MessageQueue\n"
+ "%06ld.%06d %s::%s: failed to create Rx Completion queue!\n"
+ "%06ld.%06d %s::%s: failed to create Rx Submission queue!\n"
+ "%06ld.%06d %s::%s: failed to create Rx pool\n"
+ "%06ld.%06d %s::%s: failed to create Rx queue\n"
+ "%06ld.%06d %s::%s: failed to create Rx submission queue\n"
+ "%06ld.%06d %s::%s: failed to create Tx Completion queue!\n"
+ "%06ld.%06d %s::%s: failed to create Tx Submission queue!\n"
+ "%06ld.%06d %s::%s: failed to create Tx completion queue\n"
+ "%06ld.%06d %s::%s: failed to create Tx pool\n"
+ "%06ld.%06d %s::%s: failed to create Tx queue\n"
+ "%06ld.%06d %s::%s: failed to create command gate\n"
+ "%06ld.%06d %s::%s: failed to create event source at %u\n"
+ "%06ld.%06d %s::%s: failed to create interrupt event source\n"
+ "%06ld.%06d %s::%s: failed to create lock\n"
+ "%06ld.%06d %s::%s: failed to create memory descriptor\n"
+ "%06ld.%06d %s::%s: failed to create memory policy info\n"
+ "%06ld.%06d %s::%s: failed to create pci service notifiers\n"
+ "%06ld.%06d %s::%s: failed to create pool\n"
+ "%06ld.%06d %s::%s: failed to create registration entry\n"
+ "%06ld.%06d %s::%s: failed to get link speed: 0x%08x\n"
+ "%06ld.%06d %s::%s: failed to get mapper\n"
+ "%06ld.%06d %s::%s: failed to get provider of IOPCI2PCIBridge\n"
+ "%06ld.%06d %s::%s: failed to get provider of IOPCIDevice\n"
+ "%06ld.%06d %s::%s: failed to get work loop\n"
+ "%06ld.%06d %s::%s: failed to initialize Rx submission queue: 0x%x\n"
+ "%06ld.%06d %s::%s: failed to map bar0\n"
+ "%06ld.%06d %s::%s: failed to map bar1\n"
+ "%06ld.%06d %s::%s: failed to map bar2\n"
+ "%06ld.%06d %s::%s: failed to map memory for %p\n"
+ "%06ld.%06d %s::%s: failed to open service\n"
+ "%06ld.%06d %s::%s: failed to prepare 0x%x\n"
+ "%06ld.%06d %s::%s: failed to prepare Rx pool, 0x%x\n"
+ "%06ld.%06d %s::%s: failed to prepare Tx pool, 0x%x\n"
+ "%06ld.%06d %s::%s: failed to prepare dma memory for %p\n"
+ "%06ld.%06d %s::%s: failed to prepare io command\n"
+ "%06ld.%06d %s::%s: failed to prepare log buffer\n"
+ "%06ld.%06d %s::%s: failed to prepare qctun Rx buffer pool, 0x%x\n"
+ "%06ld.%06d %s::%s: failed to prepare qctun Tx buffer pool, 0x%x\n"
+ "%06ld.%06d %s::%s: failed to queue log buffer\n"
+ "%06ld.%06d %s::%s: failed to read back bytes %llu, expected size %u\n"
+ "%06ld.%06d %s::%s: failed to register network interface: 0x%x\n"
+ "%06ld.%06d %s::%s: failed to retrieve DMA segment: 0x%x\n"
+ "%06ld.%06d %s::%s: failed to retrieve any of the constants from plist\n"
+ "%06ld.%06d %s::%s: failed to retrieve baseband chipset information\n"
+ "%06ld.%06d %s::%s: failed to retrieve chipset device map\n"
+ "%06ld.%06d %s::%s: failed to retrieve chipset name\n"
+ "%06ld.%06d %s::%s: failed to retrieve dart window: 0x%x\n"
+ "%06ld.%06d %s::%s: failed to retrieve device descriptor\n"
+ "%06ld.%06d %s::%s: failed to retrieve device descriptor map\n"
+ "%06ld.%06d %s::%s: failed to retrieve device descriptor name\n"
+ "%06ld.%06d %s::%s: failed to retrieve pcie reset seperation workaround dict\n"
+ "%06ld.%06d %s::%s: failed to retrieve workaround value\n"
+ "%06ld.%06d %s::%s: failed to save registration entry\n"
+ "%06ld.%06d %s::%s: failed to set link speed: 0x%08x\n"
+ "%06ld.%06d %s::%s: failed to setup baseband service\n"
+ "%06ld.%06d %s::%s: failed to setup control %p\n"
+ "%06ld.%06d %s::%s: failed to setup port control %p\n"
+ "%06ld.%06d %s::%s: failed to start reporting\n"
+ "%06ld.%06d %s::%s: failed: 0x%x\n"
+ "%06ld.%06d %s::%s: faled to copy data out of mbuf\n"
+ "%06ld.%06d %s::%s: flags 0x%x, current state: %s\n"
+ "%06ld.%06d %s::%s: flush %u\n"
+ "%06ld.%06d %s::%s: forClient %p\n"
+ "%06ld.%06d %s::%s: forClient %p, options 0x%08x, inGate %u\n"
+ "%06ld.%06d %s::%s: forClient is not AppleBasebandPCIPDPSkywalkInterface\n"
+ "%06ld.%06d %s::%s: force: %u, inReset = %u\n"
+ "%06ld.%06d %s::%s: free count: %u\n"
+ "%06ld.%06d %s::%s: got kOffPowerState\n"
+ "%06ld.%06d %s::%s: got kOnPowerState\n"
+ "%06ld.%06d %s::%s: got pci publish notifier\n"
+ "%06ld.%06d %s::%s: got pci termination notifier\n"
+ "%06ld.%06d %s::%s: got publish notifier\n"
+ "%06ld.%06d %s::%s: got termination notifier\n"
+ "%06ld.%06d %s::%s: ifnet_eflags not in plist\n"
+ "%06ld.%06d %s::%s: ifp 0x%p, cmd 0x%x, data 0x%p\n"
+ "%06ld.%06d %s::%s: ignore event %d\n"
+ "%06ld.%06d %s::%s: ignoring transition\n"
+ "%06ld.%06d %s::%s: in-band assert %u\n"
+ "%06ld.%06d %s::%s: inReset %u\n"
+ "%06ld.%06d %s::%s: index %d\n"
+ "%06ld.%06d %s::%s: index %d, getInterruptType error 0x%08x\n"
+ "%06ld.%06d %s::%s: index %d, not msi %d\n"
+ "%06ld.%06d %s::%s: index %u\n"
+ "%06ld.%06d %s::%s: index out of range %d\n"
+ "%06ld.%06d %s::%s: interface %u %s\n"
+ "%06ld.%06d %s::%s: interface down\n"
+ "%06ld.%06d %s::%s: interface was not able to deallocate packet, force deallocating\n"
+ "%06ld.%06d %s::%s: interfaces not available\n"
+ "%06ld.%06d %s::%s: interval in us %llu, time mode %u\n"
+ "%06ld.%06d %s::%s: intfPropMatches %u\n"
+ "%06ld.%06d %s::%s: invalid descriptor\n"
+ "%06ld.%06d %s::%s: invalid device\n"
+ "%06ld.%06d %s::%s: invalid max_rsc_pkts config\n"
+ "%06ld.%06d %s::%s: invalid max_rx_aggregation config\n"
+ "%06ld.%06d %s::%s: invalid memory %p+%llu\n"
+ "%06ld.%06d %s::%s: invalid message %u\n"
+ "%06ld.%06d %s::%s: invalid param\n"
+ "%06ld.%06d %s::%s: invalid plist, constants not dictionary\n"
+ "%06ld.%06d %s::%s: invalid range: 0x%llx (+ 0x%llx)\n"
+ "%06ld.%06d %s::%s: io: %p, iocmd: %p, status 0x%x, size %u, eot %d\n"
+ "%06ld.%06d %s::%s: iocmd: %p, prev: %p, io: %p, pa: 0x%llx, OOO IO: %u, Intf Idx: %u, Chan Idx: %u, id: %u\n"
+ "%06ld.%06d %s::%s: isDefaultQueueSet: %u\n"
+ "%06ld.%06d %s::%s: link control2: 0x%08x, current target link speed: %u\n"
+ "%06ld.%06d %s::%s: link control2: 0x%08x, target link speed: %u\n"
+ "%06ld.%06d %s::%s: link speed mismatch: expected %u, actual %u\n"
+ "%06ld.%06d %s::%s: linkState %u\n"
+ "%06ld.%06d %s::%s: logical link / interface down\n"
+ "%06ld.%06d %s::%s: logical link property is NULL!\n"
+ "%06ld.%06d %s::%s: map %u\n"
+ "%06ld.%06d %s::%s: mapped bar0 address 0x%llx (pa: 0x%llx) (+0x%x)\n"
+ "%06ld.%06d %s::%s: mapped bar1 address 0x%llx (pa: 0x%llx) (+0x%x)\n"
+ "%06ld.%06d %s::%s: mapped bar2 address 0x%llx (pa: 0x%llx) (+0x%x)\n"
+ "%06ld.%06d %s::%s: mapper %p\n"
+ "%06ld.%06d %s::%s: mapper 0x%p\n"
+ "%06ld.%06d %s::%s: mapper cleared\n"
+ "%06ld.%06d %s::%s: mapping bearer ID: %u, to queueset failed!\n"
+ "%06ld.%06d %s::%s: mapping pending segments\n"
+ "%06ld.%06d %s::%s: mbuf allocate failed err %d\n"
+ "%06ld.%06d %s::%s: mem: %p\n"
+ "%06ld.%06d %s::%s: memory limit reached\n"
+ "%06ld.%06d %s::%s: memory not dart page aligned 0x%llx\n"
+ "%06ld.%06d %s::%s: memory size not multiple of dart page size %llu\n"
+ "%06ld.%06d %s::%s: memoryAllocLimit %llu, mapper %p\n"
+ "%06ld.%06d %s::%s: messaging clients: message %s (0x%x), arg %p\n"
+ "%06ld.%06d %s::%s: mmio read fail at %p\n"
+ "%06ld.%06d %s::%s: muxed rx slot count not found in plist\n"
+ "%06ld.%06d %s::%s: name: %s"
+ "%06ld.%06d %s::%s: no manager\n"
+ "%06ld.%06d %s::%s: no mapper\n"
+ "%06ld.%06d %s::%s: no memory\n"
+ "%06ld.%06d %s::%s: no pci service\n"
+ "%06ld.%06d %s::%s: no provider\n"
+ "%06ld.%06d %s::%s: no registration for time domain %u\n"
+ "%06ld.%06d %s::%s: no slot available\n"
+ "%06ld.%06d %s::%s: nomem\n"
+ "%06ld.%06d %s::%s: nonmem for interface array\n"
+ "%06ld.%06d %s::%s: not an AppleBasebandPCIPDPSkywalkInterface\n"
+ "%06ld.%06d %s::%s: not disabling a device in reset\n"
+ "%06ld.%06d %s::%s: not in sleep, bail\n"
+ "%06ld.%06d %s::%s: nothing to process\n"
+ "%06ld.%06d %s::%s: notifying AppleBaseband that PCI driver is registered for notifications\n"
+ "%06ld.%06d %s::%s: oob Tx info allocation\n"
+ "%06ld.%06d %s::%s: open failed, _pciService: %p\n"
+ "%06ld.%06d %s::%s: options 0x%08x\n"
+ "%06ld.%06d %s::%s: owner %u\n"
+ "%06ld.%06d %s::%s: owner: %p, bearer ID: %u, status: %u\n"
+ "%06ld.%06d %s::%s: packet %p\n"
+ "%06ld.%06d %s::%s: packet allocation failed: 0x%x\n"
+ "%06ld.%06d %s::%s: packet return %p\n"
+ "%06ld.%06d %s::%s: pci bridge - device %p, stateNumber %lu\n"
+ "%06ld.%06d %s::%s: pci bridge -- power on\n"
+ "%06ld.%06d %s::%s: pci control, stateNumber %lu\n"
+ "%06ld.%06d %s::%s: pci device open ret %u\n"
+ "%06ld.%06d %s::%s: pci low power entry ack timeout\n"
+ "%06ld.%06d %s::%s: pci low power entry acknowledged\n"
+ "%06ld.%06d %s::%s: pci low power entry deferred\n"
+ "%06ld.%06d %s::%s: pci service - device %p, stateNumber %lu\n"
+ "%06ld.%06d %s::%s: pci service ID: %u\n"
+ "%06ld.%06d %s::%s: pci service entered low power\n"
+ "%06ld.%06d %s::%s: pci service exited low power\n"
+ "%06ld.%06d %s::%s: pci service missing or in low power\n"
+ "%06ld.%06d %s::%s: pci service not available\n"
+ "%06ld.%06d %s::%s: pci service not available for MSI registration\n"
+ "%06ld.%06d %s::%s: pci service open failed, service ID: %p\n"
+ "%06ld.%06d %s::%s: pci service open failed, service: %p\n"
+ "%06ld.%06d %s::%s: pci service: %p, isPublished: %u\n"
+ "%06ld.%06d %s::%s: pciService not available\n"
+ "%06ld.%06d %s::%s: pending\n"
+ "%06ld.%06d %s::%s: plist does not contain constants for fallback (\"%s\")\n"
+ "%06ld.%06d %s::%s: plist doesn't have Rx throughput specification\n"
+ "%06ld.%06d %s::%s: plist doesn't have rx slot size\n"
+ "%06ld.%06d %s::%s: plist doesn't have tx slot size\n"
+ "%06ld.%06d %s::%s: plist error, constants property is not dictionary\n"
+ "%06ld.%06d %s::%s: pool capacity: tx=%u, rx=%u\n"
+ "%06ld.%06d %s::%s: pool not available\n"
+ "%06ld.%06d %s::%s: pool: %p, Intf idx: %u\n"
+ "%06ld.%06d %s::%s: port %p\n"
+ "%06ld.%06d %s::%s: port already disabled\n"
+ "%06ld.%06d %s::%s: port enable failed\n"
+ "%06ld.%06d %s::%s: port enable failed!, ret: 0x%08x\n"
+ "%06ld.%06d %s::%s: port enable panic setting: %u\n"
+ "%06ld.%06d %s::%s: port is locked\n"
+ "%06ld.%06d %s::%s: provider %p, options 0x%08x\n"
+ "%06ld.%06d %s::%s: provider %p, options 0x%08x, defer %p\n"
+ "%06ld.%06d %s::%s: provider is NULL\n"
+ "%06ld.%06d %s::%s: provider is not AppleBasebandPCIPDPManagerBase\n"
+ "%06ld.%06d %s::%s: provider is not an instance of AppleBasebandPCIInterface\n"
+ "%06ld.%06d %s::%s: publishing %u PDP interfaces\n"
+ "%06ld.%06d %s::%s: qctun interface enabled\n"
+ "%06ld.%06d %s::%s: qctun interface number: %u\n"
+ "%06ld.%06d %s::%s: qctun interface rx slot count not specified in plist!\n "
+ "%06ld.%06d %s::%s: qctun interface rx slot count: %u\n"
+ "%06ld.%06d %s::%s: qctun interface slot size not specified in plist!\n "
+ "%06ld.%06d %s::%s: qctun interface slot size: %u\n"
+ "%06ld.%06d %s::%s: qctun interface tx slot count not specified in plist!\n "
+ "%06ld.%06d %s::%s: queue set config is NULL!\n"
+ "%06ld.%06d %s::%s: queueSetID: 0x%llx, _isDefault: %u, index: %u\n"
+ "%06ld.%06d %s::%s: raw Tx cached pkts: %u\n"
+ "%06ld.%06d %s::%s: raw Tx freed pkts: %u\n"
+ "%06ld.%06d %s::%s: refCon %p, _pciPublishNotifier %p, _pciTerminateNotifier %p\n"
+ "%06ld.%06d %s::%s: refcon: %p, pci service: %p\n"
+ "%06ld.%06d %s::%s: reg %d, size %d\n"
+ "%06ld.%06d %s::%s: reg %u, buff %p, size %u\n"
+ "%06ld.%06d %s::%s: region %u already mapped\n"
+ "%06ld.%06d %s::%s: region %u not mapped\n"
+ "%06ld.%06d %s::%s: region ID: %u, memory: %p, memorySize: %llu\n"
+ "%06ld.%06d %s::%s: region Id: %u\n"
+ "%06ld.%06d %s::%s: registered %p and set level to %u\n"
+ "%06ld.%06d %s::%s: requested: %u, queued: %u\n"
+ "%06ld.%06d %s::%s: requesting power state to be OFF\n"
+ "%06ld.%06d %s::%s: requesting power state to be ON\n"
+ "%06ld.%06d %s::%s: ret 0x%x, info 0x%llx\n"
+ "%06ld.%06d %s::%s: retry %d\n"
+ "%06ld.%06d %s::%s: root port L1PMSS capability not found\n"
+ "%06ld.%06d %s::%s: root port PCIe capability not found\n"
+ "%06ld.%06d %s::%s: rsc_service not present in plist or unsupported\n"
+ "%06ld.%06d %s::%s: runAction failed with 0x%08x\n"
+ "%06ld.%06d %s::%s: runAsync failed: %s\n"
+ "%06ld.%06d %s::%s: rx pool capacity count not found in plist\n"
+ "%06ld.%06d %s::%s: rx pool unavailable\n"
+ "%06ld.%06d %s::%s: same mapper, skip remapping\n"
+ "%06ld.%06d %s::%s: segment %p\n"
+ "%06ld.%06d %s::%s: served %u raw Tx, %u remain\n"
+ "%06ld.%06d %s::%s: service %p is not AppleBasebandPCI object\n"
+ "%06ld.%06d %s::%s: service ID: %u\n"
+ "%06ld.%06d %s::%s: service already open by %p\n"
+ "%06ld.%06d %s::%s: service is terminating\n"
+ "%06ld.%06d %s::%s: serviceID: %u, not present\n"
+ "%06ld.%06d %s::%s: serviceID: %u, serviceObj: %p published\n"
+ "%06ld.%06d %s::%s: set link speed to %u\n"
+ "%06ld.%06d %s::%s: set power request %d\n"
+ "%06ld.%06d %s::%s: shared mem unmapping failed: 0x%x\n"
+ "%06ld.%06d %s::%s: shared memory mapping for region: %u, failed\n"
+ "%06ld.%06d %s::%s: signal output request\n"
+ "%06ld.%06d %s::%s: size %llu\n"
+ "%06ld.%06d %s::%s: skipping port enable due to system power (sleep %d, shutdown %d)\n"
+ "%06ld.%06d %s::%s: staged: %u\n"
+ "%06ld.%06d %s::%s: success\n"
+ "%06ld.%06d %s::%s: super class failed to initialize\n"
+ "%06ld.%06d %s::%s: super failed\n"
+ "%06ld.%06d %s::%s: super match failed\n"
+ "%06ld.%06d %s::%s: super returned false\n"
+ "%06ld.%06d %s::%s: super::init failed\n"
+ "%06ld.%06d %s::%s: super::start failed\n"
+ "%06ld.%06d %s::%s: t %u, arg0 %p, arg1 %p\n"
+ "%06ld.%06d %s::%s: this %p\n"
+ "%06ld.%06d %s::%s: this %p, pool %p, memPolicy %p\n"
+ "%06ld.%06d %s::%s: this %p, status 0x%x, size %llu, cookie %p\n"
+ "%06ld.%06d %s::%s: this: %p\n"
+ "%06ld.%06d %s::%s: thread call failed with 0x%08x\n"
+ "%06ld.%06d %s::%s: time event for domain %u is already registered\n"
+ "%06ld.%06d %s::%s: timerMode %u, arg1 %p\n"
+ "%06ld.%06d %s::%s: trigger power state change\n"
+ "%06ld.%06d %s::%s: tx pool unavailable\n"
+ "%06ld.%06d %s::%s: type %d status 0x%x header 0x%x 0x%x 0x%x 0x%x\n"
+ "%06ld.%06d %s::%s: unRegistering MSI for index %u\n"
+ "%06ld.%06d %s::%s: unable to allocate link status report staging buffer\n"
+ "%06ld.%06d %s::%s: unable to configure the IPAppender for ifnet\n"
+ "%06ld.%06d %s::%s: unable to create PCIfoundAB dictionary\n"
+ "%06ld.%06d %s::%s: unable to create link speed dictionary\n"
+ "%06ld.%06d %s::%s: unable to create matching dictionary\n"
+ "%06ld.%06d %s::%s: unable to create port enable dictionaries\n"
+ "%06ld.%06d %s::%s: unable to create port sleep enable/disable dictionaries\n"
+ "%06ld.%06d %s::%s: unable to find AppleBasebandPCIPDPManagerBase service\n"
+ "%06ld.%06d %s::%s: unable to find AppleIPAppender service\n"
+ "%06ld.%06d %s::%s: unable to initialize pending segment list\n"
+ "%06ld.%06d %s::%s: unable to unmap memory segment.\n"
+ "%06ld.%06d %s::%s: unit number %u already has a session open\n"
+ "%06ld.%06d %s::%s: unit number %u invalid or nonexistent\n"
+ "%06ld.%06d %s::%s: unknown baseband chipset %s, no fallback option\n"
+ "%06ld.%06d %s::%s: unknown client\n"
+ "%06ld.%06d %s::%s: unknown message 0x%x\n"
+ "%06ld.%06d %s::%s: unmapped bar\n"
+ "%06ld.%06d %s::%s: unmapping leftover region %u\n"
+ "%06ld.%06d %s::%s: va 0x%llx, pa 0x%llx, offset %llu\n"
+ "%06ld.%06d %s::%s: vendorID = 0x%04x, deviceID = 0x%04x\n"
+ "%06ld.%06d %s::%s: wait %u, event %p\n"
+ "%06ld.%06d %s::%s: workloop: %p\n"
+ "%3u"
+ "%3u to %3u"
+ "%3u to inf"
+ "%d. size %llu, %p "
+ "%s Close"
+ "%s Open "
+ "%s Read "
+ "%s TimeSync"
+ "%s Write"
+ "%s: %u:%u was not found\n"
+ "%s: logger user knob %u:%u already registered\n"
+ "+-----------------------------------------------+----------------+"
+ "/Library/Caches/com.apple.xbs/Sources/AppleBasebandPCI/AppleBasebandPCIControl/AppleBasebandPCILogger.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/AppleBasebandPCI/AppleBasebandPCIPDP/AppleBasebandPCIPDPReporter.cpp"
+ "11211"
+ "112111111"
+ "1211"
+ "1211111212221212111111111211112111111111111112112112112111121121111121"
+ "12111112122212121111111112111121111111111111121121121121111211211111212"
+ "121111121222121211112111222222212111112222212121"
+ "121111121222121212111111111111111111111122122122221111111111222"
+ "12111112122212121212111111111111111111111122222222222222222222222222222222222111111111111111111111111111111111111111111111111111111111111111111111122222222222222222111112112222222"
+ "12111112122212121222222222111222112111112"
+ "12112221111111111111"
+ "12212"
+ "Advanced Error Reporting"
+ "Aggregated Block"
+ "AppleBasebandPCI state dump:\n"
+ "AppleBasebandPCI::start: failed to get logger\n"
+ "AppleBasebandPCIControlReporter"
+ "AppleBasebandPCILogger"
+ "AppleBasebandPCILogger.cpp"
+ "AppleBasebandPCILogger::initWithInfo: AppleBasebandPCILogger instance already exists\n"
+ "AppleBasebandPCILogger::initWithInfo: pDictionary creation failed\n"
+ "AppleBasebandPCILogger::initWithInfo: super::init failed\n"
+ "AppleBasebandPCILogger::start: failed to allocate memory for snapshot buffer\n"
+ "AppleBasebandPCIPDPManagerBase::start: failed to get logger\n"
+ "AppleBasebandPCIPDPReporter"
+ "AppleBasebandPCIPDPReporter.cpp"
+ "AppleBasebandPCIReporter"
+ "AppleBasebandPCIReporter::%s: could not create a legend\n"
+ "AppleBasebandPCIReporter::%s: could not create a set object\n"
+ "AppleBasebandPCIReporter::%s: invalid argument\n"
+ "AppleBasebandPCIReporter::%s: setProperty failed\n"
+ "AppleBasebandPCIReporter::%s: subclass failed to add reporters\n"
+ "Correctable Error"
+ "Counters"
+ "Current State Index"
+ "DL"
+ "DL Aggregation Histogram"
+ "DL Drop Counters"
+ "DL Limit"
+ "DL Limiter State"
+ "Downlink Bytes"
+ "Downlink Pkts"
+ "Dropped Downlink Bytes"
+ "Dropped Downlink Packets"
+ "Error"
+ "False"
+ "Fatal Error"
+ "Flow Control"
+ "Global"
+ "I"
+ "I/O"
+ "IOReportLegend"
+ "IOReportLegendPublic"
+ "Interfaces"
+ "Interrupt"
+ "Invalid Interface"
+ "Link Status Notifications"
+ "Non-Fatal Error"
+ "PDP"
+ "PDP packet dump level"
+ "PDP packet dump new level: %u\n"
+ "PDP packet dump size"
+ "Power"
+ "Publish Count"
+ "Secondary ISR Count"
+ "Secondary Interrupt Handler"
+ "State Summary"
+ "States"
+ "Terminate Count"
+ "True"
+ "UL"
+ "UL Aggregation Histogram"
+ "Uplink Bytes"
+ "Uplink Pkts"
+ "abortChannel"
+ "abp-debug"
+ "abp-debug-buf-size"
+ "abp-flags"
+ "abp-kdbg-trace"
+ "abp-reporting"
+ "addNode"
+ "allocQueues"
+ "allocatePrepareMemory"
+ "allocateRawTxCache"
+ "allocateReturnCommand"
+ "asyncFunction"
+ "asyncThreadCallGated"
+ "bounceIn"
+ "bounceOut"
+ "calculateBufferPoolCapacity"
+ "callAsync"
+ "cancel"
+ "cancelAsync"
+ "cancelCompletion"
+ "cancelTimer"
+ "changeState"
+ "checkPortAction"
+ "checkPortOffCycleGated"
+ "cleanCommandParamters"
+ "cleanRequestParamters"
+ "clearDMATransfer"
+ "clientClose"
+ "clientCloseGated"
+ "close"
+ "closeGated"
+ "closePublishedPCIDataServicesGated"
+ "closeServiceGated"
+ "complete"
+ "completeGatedFunction"
+ "completeMemory"
+ "configureReport"
+ "createDedicatedQueueSet"
+ "createDefaultQueueSet"
+ "createInitRxSubmissionQueue"
+ "createLogicalLinkGated_block_invoke"
+ "createQueueSets"
+ "createQueues"
+ "createRxSubmissionQueue"
+ "createSetupPort"
+ "currentLogSnapshotBufferSize"
+ "dartErrorHandler"
+ "deRegisterPort"
+ "deregisterTimeEvent"
+ "deregisterUserKnob"
+ "deviceAwakeCheck"
+ "deviceWakeAsync"
+ "deviceWakeFunction"
+ "didTerminate"
+ "disableLockPort"
+ "disableLockPortGated"
+ "discardRxPacket"
+ "down"
+ "enableASPMGated"
+ "enableDefaultQueueSet"
+ "enableHostMemProtectionGated"
+ "enableL1SSGated"
+ "enableUnlockPort"
+ "enableUnlockPortGated"
+ "enqueuePDPEvent"
+ "enqueuePackets"
+ "enterLowPower"
+ "errorFunction"
+ "exitLowPower"
+ "failed to create logger\n"
+ "flushQueueSets"
+ "flushStageQueue"
+ "free"
+ "freeRawTxCache"
+ "gatedReturnCommand"
+ "gatherEPConfigRegSpace"
+ "getChipsetConstants"
+ "getCommand"
+ "getCurrentLinkSpeedGated"
+ "getDeviceDescriptorDict"
+ "getDeviceResetState"
+ "getEPTransactionPendingBit"
+ "getInLowPower"
+ "getInReset"
+ "getQCTunBufferPool"
+ "handleAER"
+ "handleClose"
+ "handleIsOpen"
+ "handleOpen"
+ "handlePCIMessage"
+ "handlePCIServiceSwitch"
+ "initBSDInterfaceParameters"
+ "initUserDefaults"
+ "initWithInfo"
+ "initWithName"
+ "initWithOptions"
+ "initWithPool"
+ "initWithWorkLoop"
+ "initialPowerStateForDomainState"
+ "initialize"
+ "invokeAsync"
+ "ioCompletionFunction"
+ "ipAppenderMessage"
+ "isPCIServicePublished"
+ "linkDown"
+ "linkDownCheck"
+ "linkSpeedCheck"
+ "linkStateUpFunction"
+ "linkUp"
+ "linkUpCheck"
+ "lockPort"
+ "logPacket"
+ "logSnapshotBufferSize"
+ "logger attach/start failed %p\n"
+ "manualDisablePort"
+ "manualEnablePort"
+ "map"
+ "mapBarGated"
+ "mapBearerToQueueSet"
+ "mapSharedMemory"
+ "mapSharedMemory_block_invoke"
+ "matchPropertyTable"
+ "mmioRead"
+ "mmioReadMemory"
+ "msiInterrupt"
+ "newMemorySegment"
+ "newPacket"
+ "notify"
+ "notifyDedicatedBearer"
+ "notifyPCIServiceDidTerminateGated"
+ "notifyPCIServiceGated"
+ "notifyPortStateChange"
+ "notifyTerminateAck"
+ "notifyTerminateAckGated"
+ "open"
+ "openGated"
+ "openPublishedPCIDataServicesGated"
+ "openServiceGated"
+ "packetDump"
+ "pciMessageGated"
+ "pciNotifier"
+ "pciRegisterGated"
+ "pciServiceNotifyDidTerminate"
+ "pciServiceNotifyDidTerminateGated"
+ "pciServiceNotifyPublishGated"
+ "pciServiceNotifyTerminateGated"
+ "pcieResetSeperationROMWA"
+ "pdp:%s: error %d\n"
+ "pdp:%s: size (%u) out of range.\n"
+ "pdpEventHandler"
+ "pdp_dump_level"
+ "pdp_dump_size"
+ "pdp_ip%u"
+ "portAction"
+ "portActionDone"
+ "portChangeFunction"
+ "portDeepSleep"
+ "portEnable"
+ "portEnabled"
+ "portManualEnableFunction"
+ "portQuiesceWaitFunction"
+ "portSleep"
+ "portWake"
+ "powerStateDidChangeTo"
+ "powerStateDidChangeToGated"
+ "powerStateWillChangeTo"
+ "powerStateWillChangeToGated"
+ "prepare"
+ "prepareBSDInterface"
+ "prepareDMATransfer"
+ "prepareIn"
+ "prepareMemory"
+ "prepareOut"
+ "preparePoolsWithMapper"
+ "processBSDCommand"
+ "processCurrentPortAction"
+ "publish"
+ "qctunBufferPoolCapacity"
+ "queryFreeSpace"
+ "queueLogBuffer"
+ "queueRxBuffersGated"
+ "rawTxPrepare"
+ "read"
+ "readLogs"
+ "registerAER"
+ "registerDARTErrorHandler"
+ "registerDebugObject"
+ "registerMSI"
+ "registerMSI_block_invoke"
+ "registerPort"
+ "registerRead"
+ "registerTimeEvent"
+ "registerUserKnob"
+ "registerWorkLoop"
+ "releaseBasebandService"
+ "reportError"
+ "reportInterfaceAdvisory"
+ "reportLinkStatus"
+ "reportMessage"
+ "requestDequeue"
+ "requestPortOffCycleGated"
+ "requestTxGated"
+ "resetStageQueue"
+ "returnPacket"
+ "running"
+ "rxQueueCallbackGated"
+ "scan"
+ "sendImage"
+ "serveRawTxQueue"
+ "serviceNotifier"
+ "serviceRegisterGated"
+ "setBootStage"
+ "setIO"
+ "setInReset"
+ "setLinkSpeedGated"
+ "setMapper"
+ "setName"
+ "setPowerOn"
+ "setPowerState"
+ "setPowerStateGated"
+ "setQueueSetId"
+ "setRunningState"
+ "setTargetLinkSpeedGated"
+ "setupBasebandService"
+ "setupDARTWindowGated"
+ "setupPort"
+ "shared memory"
+ "site.AppleBasebandPCIControlReporter"
+ "site.AppleBasebandPCILogger"
+ "site.AppleBasebandPCIPDPReporter"
+ "site.AppleBasebandPCIReporter"
+ "site.IOSimpleReporter*"
+ "site.IOStateReporter*"
+ "site.StateEntry"
+ "site.UserKnob"
+ "site.logBuffer"
+ "site.logBufferQueue"
+ "site.struct StateEntry"
+ "sleepAckFunction"
+ "sleepCheck"
+ "some logs dropped\n"
+ "stagePkts"
+ "stageQueueGetRxPkts"
+ "stageQueueGetTxPkts"
+ "startChannel"
+ "startReporting"
+ "startSleepTimer"
+ "startTimer"
+ "stop"
+ "stopped"
+ "switchBearerTrafficToService"
+ "syncSIOCSIFFLAGS"
+ "sysctl_pdp_dump_level"
+ "sysctl_pdp_dump_size"
+ "teardownPort"
+ "telescoperRecordCompletedPackets"
+ "terminate"
+ "timeSync"
+ "timer"
+ "timerCompletion"
+ "timerFunction"
+ "transferDone"
+ "triggerMSI"
+ "triggerTxDequeue"
+ "txCompletionCallbackGated"
+ "txQueueCallbackGated"
+ "unRegisterMSI"
+ "unRegisterMSI_block_invoke"
+ "unlockPort"
+ "unmap"
+ "unmapBarGated"
+ "unmapBearerFromQueueSet"
+ "unmapSharedMemory"
+ "unmapSharedMemory_block_invoke"
+ "up"
+ "updateEnabled"
+ "updateReport"
+ "usesLowLatencyService"
+ "usesRSCService"
+ "validateMSIIndex"
+ "willTerminate"
+ "willTerminateGated"
+ "write"
+ "|%02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x|%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c|"
+ "~ABPControl"
+ "~ABPNullDevice"
+ "~ABPPort"
- "121111121222121211111111121111211111111111112112112112111121121111121"
- "1211111212221212111111111211112111111111111121121121121111211211111212"
- "12111112122212121111211122222221211111222221212"
- "12111112122212121211111111111111111111112212212222111111111222"
- "1211111212221212121211111111111111111111122222222222222222222222222222222222111111111111111111111111111111111111111111111111111111111111111111111122222222222222222111112112222222"

```

>  `com.apple.driver.AppleBasebandPCIMAVControl`

```diff

-852.0.0.0.0
+853.0.0.0.0
   __TEXT.__const: 0x1526
-  __TEXT.__cstring: 0x1192
-  __TEXT_EXEC.__text: 0x1cd1c
+  __TEXT.__cstring: 0x67bb
+  __TEXT_EXEC.__text: 0x47ac4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
-  __DATA.__common: 0xd8
-  __DATA_CONST.__auth_got: 0x248
-  __DATA_CONST.__got: 0xa8
-  __DATA_CONST.__mod_init_func: 0x508
-  __DATA_CONST.__mod_term_func: 0x28
-  __DATA_CONST.__const: 0x2ff8
-  __DATA_CONST.__kalloc_type: 0xc40
+  __DATA.__common: 0x100
+  __DATA_CONST.__auth_got: 0x288
+  __DATA_CONST.__got: 0xb8
+  __DATA_CONST.__mod_init_func: 0x510
+  __DATA_CONST.__mod_term_func: 0x30
+  __DATA_CONST.__const: 0x3180
+  __DATA_CONST.__kalloc_type: 0xc80
   __DATA_CONST.__kalloc_var: 0x5a0
-  Functions: 851
+  Functions: 872
   Symbols:   0
-  CStrings:  174
+  CStrings:  717
 
CStrings:
+ "%06ld.%06d %s::%s: \n"
+ "%06ld.%06d %s::%s:  --done\n"
+ "%06ld.%06d %s::%s: %d. \n"
+ "%06ld.%06d %s::%s: %d.  --done\n"
+ "%06ld.%06d %s::%s: %d. %p [0x%llx]\n"
+ "%06ld.%06d %s::%s: %d. %p [0x%llx], queued IOs: %lu\n"
+ "%06ld.%06d %s::%s: %d. %s -> %s\n"
+ "%06ld.%06d %s::%s: %d. (async) failed to prepare memory command\n"
+ "%06ld.%06d %s::%s: %d. (async) returned 0x%x\n"
+ "%06ld.%06d %s::%s: %d. -- done\n"
+ "%06ld.%06d %s::%s: %d. -- done %u\n"
+ "%06ld.%06d %s::%s: %d. --done\n"
+ "%06ld.%06d %s::%s: %d. Copy memory command\n"
+ "%06ld.%06d %s::%s: %d. Device is IN RESET state, bailing\n"
+ "%06ld.%06d %s::%s: %d. Exclusive workloop interface, failed to create a control commandGate!\n"
+ "%06ld.%06d %s::%s: %d. Getting BB reset state failed\n"
+ "%06ld.%06d %s::%s: %d. Unmap shared memory failed\n"
+ "%06ld.%06d %s::%s: %d. Virtual timesync interface\n"
+ "%06ld.%06d %s::%s: %d. _asyncMode 0x%08x, asyncMode 0x%08x, arg1 %p\n"
+ "%06ld.%06d %s::%s: %d. asyncMode 0x%08x\n"
+ "%06ld.%06d %s::%s: %d. buffer: 0x%llx, size: %llu, seqNum: %u\n"
+ "%06ld.%06d %s::%s: %d. calling completion, ret: 0x%llx\n"
+ "%06ld.%06d %s::%s: %d. cf %p, arg0 %p, arg1 %p\n"
+ "%06ld.%06d %s::%s: %d. chunk too large\n"
+ "%06ld.%06d %s::%s: %d. commandSleep (THREAD_INTERRUPTIBLE) woke with reason 0x%x\n"
+ "%06ld.%06d %s::%s: %d. current asyncMode 0x%08x\n"
+ "%06ld.%06d %s::%s: %d. direction %s\n"
+ "%06ld.%06d %s::%s: %d. direction %u\n"
+ "%06ld.%06d %s::%s: %d. direction: %u, workloop: %p\n"
+ "%06ld.%06d %s::%s: %d. do not support no copy for mbuf\n"
+ "%06ld.%06d %s::%s: %d. error %u\n"
+ "%06ld.%06d %s::%s: %d. error type %u, arg0 %p, arg1 %p\n"
+ "%06ld.%06d %s::%s: %d. eventIndex %u\n"
+ "%06ld.%06d %s::%s: %d. exclusive workloop: %p, msi index: %u\n"
+ "%06ld.%06d %s::%s: %d. failed to allocate async interrupt source\n"
+ "%06ld.%06d %s::%s: %d. failed to allocate commandGate\n"
+ "%06ld.%06d %s::%s: %d. failed to allocate io pool\n"
+ "%06ld.%06d %s::%s: %d. failed to allocate memory\n"
+ "%06ld.%06d %s::%s: %d. failed to allocate memory command\n"
+ "%06ld.%06d %s::%s: %d. failed to create async call lock\n"
+ "%06ld.%06d %s::%s: %d. failed to create pools\n"
+ "%06ld.%06d %s::%s: %d. failed to prepare memory 0x%x\n"
+ "%06ld.%06d %s::%s: %d. failed to prepare memory command\n"
+ "%06ld.%06d %s::%s: %d. failed to register channel\n"
+ "%06ld.%06d %s::%s: %d. failed to retrieve channel direction\n"
+ "%06ld.%06d %s::%s: %d. failed to setup channel\n"
+ "%06ld.%06d %s::%s: %d. failed to setup interface _outChannel %p, _inChannel %p\n"
+ "%06ld.%06d %s::%s: %d. failed to setup transfer ring\n"
+ "%06ld.%06d %s::%s: %d. forClient %p, options 0x%08x\n"
+ "%06ld.%06d %s::%s: %d. forClient %p, options 0x%08x, arg %p\n"
+ "%06ld.%06d %s::%s: %d. forClient %p, options 0x%08x, arg %p, inGate %u\n"
+ "%06ld.%06d %s::%s: %d. forClient %p, options 0x%08x, inGate %u\n"
+ "%06ld.%06d %s::%s: %d. incomplete io\n"
+ "%06ld.%06d %s::%s: %d. index %u\n"
+ "%06ld.%06d %s::%s: %d. interface is inactive\n"
+ "%06ld.%06d %s::%s: %d. invalid channel direction\n"
+ "%06ld.%06d %s::%s: %d. invalid channel protocol\n"
+ "%06ld.%06d %s::%s: %d. invalid direction: %u for the interface\n"
+ "%06ld.%06d %s::%s: %d. io %p, pa: 0x%llx, tre %p\n"
+ "%06ld.%06d %s::%s: %d. io %p, size %u, pa 0x%llx\n"
+ "%06ld.%06d %s::%s: %d. io %p, tre %p, io->_pa %p, cookie 0x%lx\n"
+ "%06ld.%06d %s::%s: %d. io: %p, pa 0x%llx\n"
+ "%06ld.%06d %s::%s: %d. io: %p, status 0x%x\n"
+ "%06ld.%06d %s::%s: %d. io: %p, type: %u, status 0x%x, last: %u\n"
+ "%06ld.%06d %s::%s: %d. malformed count, count: %u\n"
+ "%06ld.%06d %s::%s: %d. map buffer ack failed: 0x%llx\n"
+ "%06ld.%06d %s::%s: %d. map buffer ack timed out: 0x%llx\n"
+ "%06ld.%06d %s::%s: %d. map completion failed\n"
+ "%06ld.%06d %s::%s: %d. map completion failed, mem is NULL\n"
+ "%06ld.%06d %s::%s: %d. map completion success\n"
+ "%06ld.%06d %s::%s: %d. memCmd %p, size %llu\n"
+ "%06ld.%06d %s::%s: %d. mem[%llu] %p, direction %u\n"
+ "%06ld.%06d %s::%s: %d. mhiDevice %p\n"
+ "%06ld.%06d %s::%s: %d. no in channel\n"
+ "%06ld.%06d %s::%s: %d. no out channel\n"
+ "%06ld.%06d %s::%s: %d. num of chunks in io too large\n"
+ "%06ld.%06d %s::%s: %d. openGated failed, result: 0x%08x\n"
+ "%06ld.%06d %s::%s: %d. options 0x%08x\n"
+ "%06ld.%06d %s::%s: %d. pa 0x%llx, size %u, code %u\n"
+ "%06ld.%06d %s::%s: %d. pa 0x%llx, size %u, code %u, ccid %u, queued IOs: %lu\n"
+ "%06ld.%06d %s::%s: %d. packetChain %p\n"
+ "%06ld.%06d %s::%s: %d. part1 subDescSize %llu, offset %llu\n"
+ "%06ld.%06d %s::%s: %d. part1 subDesc[%llu] physical address 0x%llx\n"
+ "%06ld.%06d %s::%s: %d. part2 subDescSize %llu, offset %llu\n"
+ "%06ld.%06d %s::%s: %d. part2 subDesc[%llu] physical address 0x%llx\n"
+ "%06ld.%06d %s::%s: %d. part3 subDescSize %llu, offset %llu\n"
+ "%06ld.%06d %s::%s: %d. part3 subDesc[%llu] physical address 0x%llx\n"
+ "%06ld.%06d %s::%s: %d. prop %p\n"
+ "%06ld.%06d %s::%s: %d. provider %p, options 0x%08x\n"
+ "%06ld.%06d %s::%s: %d. provider %p, options 0x%08x, defer %p\n"
+ "%06ld.%06d %s::%s: %d. queued IOs: %u\n"
+ "%06ld.%06d %s::%s: %d. reap elements\n"
+ "%06ld.%06d %s::%s: %d. reliable %u\n"
+ "%06ld.%06d %s::%s: %d. res = 0x%x, size = %llu, cookie %p\n"
+ "%06ld.%06d %s::%s: %d. reset the channels\n"
+ "%06ld.%06d %s::%s: %d. result: %u, seqNum: %u, bytes read: %u\n"
+ "%06ld.%06d %s::%s: %d. ring - va: 0x%llx, pa: 0x%llx\\n"
+ "%06ld.%06d %s::%s: %d. ring not aligned to %u\n"
+ "%06ld.%06d %s::%s: %d. ring not large enough %u\n"
+ "%06ld.%06d %s::%s: %d. ring va 0x%llx, pa 0x%llx, size %u\n"
+ "%06ld.%06d %s::%s: %d. sending map message failed: 0x%llx\n"
+ "%06ld.%06d %s::%s: %d. sending unmap message failed: 0x%llx\n"
+ "%06ld.%06d %s::%s: %d. service is terminating\n"
+ "%06ld.%06d %s::%s: %d. setting defaultInt %d, defaultIEOT %d, defaultIEOB %d\n"
+ "%06ld.%06d %s::%s: %d. setting doorbellSetting time %llu, threshold %u\n"
+ "%06ld.%06d %s::%s: %d. setting threshold intThreshold %d, ieotThreshold %d, ieobThreshold %d\n"
+ "%06ld.%06d %s::%s: %d. setting up map message completion failed: 0x%llx\n"
+ "%06ld.%06d %s::%s: %d. setting up unmap message completion failed: 0x%llx\n"
+ "%06ld.%06d %s::%s: %d. sharedER %u\n"
+ "%06ld.%06d %s::%s: %d. skipping channel setup for channel protocol: %s\n"
+ "%06ld.%06d %s::%s: %d. status 0x%x\n"
+ "%06ld.%06d %s::%s: %d. status: %u, size: %u\n"
+ "%06ld.%06d %s::%s: %d. status: 0x%llx, size: %llu\n"
+ "%06ld.%06d %s::%s: %d. super::start failed\n"
+ "%06ld.%06d %s::%s: %d. sync %u\n"
+ "%06ld.%06d %s::%s: %d. tre %p, size %u, code %u, last %u, io %p\n"
+ "%06ld.%06d %s::%s: %d. trigger %u, index %u\n"
+ "%06ld.%06d %s::%s: %d. type %u\n"
+ "%06ld.%06d %s::%s: %d. type %u, completion code %u, asyncMode %u\n"
+ "%06ld.%06d %s::%s: %d. unmap buffer ack timed out: 0x%llx\n"
+ "%06ld.%06d %s::%s: %d. unmap completion failed\n"
+ "%06ld.%06d %s::%s: %d. unmap completion failed, mem is NULL\n"
+ "%06ld.%06d %s::%s: %d. unmap completion success\n"
+ "%06ld.%06d %s::%s: %d. waiting for map completion\n"
+ "%06ld.%06d %s::%s: %d. waiting for unmap completion\n"
+ "%06ld.%06d %s::%s: %s -> %s\n"
+ "%06ld.%06d %s::%s: %u\n"
+ "%06ld.%06d %s::%s: (async) failed to create memory decriptor for shared memory region\n"
+ "%06ld.%06d %s::%s: -- done\n"
+ "%06ld.%06d %s::%s: -- done %u\n"
+ "%06ld.%06d %s::%s: --done\n"
+ "%06ld.%06d %s::%s: ABPDevice %p, type %u\n"
+ "%06ld.%06d %s::%s: Bailing, device not alive\n!"
+ "%06ld.%06d %s::%s: Both channels should have same msi_index values, (%u, %u)\n"
+ "%06ld.%06d %s::%s: CHDBOFF (0x%x) invalid\n"
+ "%06ld.%06d %s::%s: Could not find %s dictionary for time_sync!\n"
+ "%06ld.%06d %s::%s: Could not find time_sync dictionary!\n"
+ "%06ld.%06d %s::%s: Cur expiry: %llu\n"
+ "%06ld.%06d %s::%s: Cur expiry: %llu < timeout: %llu\n"
+ "%06ld.%06d %s::%s: Desired link speed: %u, boot stage: %u\n"
+ "%06ld.%06d %s::%s: Device in Reset state! Skip sending unmap message!\n"
+ "%06ld.%06d %s::%s: Device in low power, cannot immediately initiate time sync\n"
+ "%06ld.%06d %s::%s: Device in low power, cannot initiate time sync\n"
+ "%06ld.%06d %s::%s: ERDBOFF (0x%x) invalid\n"
+ "%06ld.%06d %s::%s: ERE: res: 0x%lx, cookie: 0x%lx, code %u, ccid: %u, len: %u, allFields: 0x%lx\n"
+ "%06ld.%06d %s::%s: Error 0x%x\n"
+ "%06ld.%06d %s::%s: Error getting channel doorbell number for time_sync property!\n"
+ "%06ld.%06d %s::%s: Event Ring Index %u: shared channel: %u\n"
+ "%06ld.%06d %s::%s: Failed to allocate pending event queue for shared ER index: %u\n"
+ "%06ld.%06d %s::%s: Failed to find time sync capability register\n"
+ "%06ld.%06d %s::%s: Failed to get device properties dictionary\n"
+ "%06ld.%06d %s::%s: Found time sync capability register\n"
+ "%06ld.%06d %s::%s: Host sleep Deferred\n"
+ "%06ld.%06d %s::%s: Inserting shared mem region with ID: %u\n"
+ "%06ld.%06d %s::%s: Invalid domain: %u\n"
+ "%06ld.%06d %s::%s: MHI Status: 0x%x\n"
+ "%06ld.%06d %s::%s: MHI in error state! MHI Status: 0x%x\n"
+ "%06ld.%06d %s::%s: MHI reset complete, MHICTRL: 0x%x\n"
+ "%06ld.%06d %s::%s: MHI reset procedure failed!\n"
+ "%06ld.%06d %s::%s: MSI registration failed, index: %u\n"
+ "%06ld.%06d %s::%s: Map / Prepare shared memory failed: 0x%llx\n"
+ "%06ld.%06d %s::%s: No MHI capability regiter found!\n"
+ "%06ld.%06d %s::%s: No MHIChannel\n"
+ "%06ld.%06d %s::%s: Registration for domain %u already exists\n"
+ "%06ld.%06d %s::%s: Shared mem pa: 0x%llx, mem desc pa: %p\n"
+ "%06ld.%06d %s::%s: Starting timer: New expiry: %llu, timeout: %llu\n"
+ "%06ld.%06d %s::%s: Time capability addr: %p\n"
+ "%06ld.%06d %s::%s: Time capability not present\n"
+ "%06ld.%06d %s::%s: Time event call back registration is NULL\n"
+ "%06ld.%06d %s::%s: Time sync completion unit: %u, time: %llu, domain: %u, seq: %u\n"
+ "%06ld.%06d %s::%s: Time sync is not supported\n"
+ "%06ld.%06d %s::%s: Time sync not supported\n"
+ "%06ld.%06d %s::%s: Total shared ER count: %u\n"
+ "%06ld.%06d %s::%s: Triggering MSI index: %u, failed ret: 0x%llx\n"
+ "%06ld.%06d %s::%s: Unexpected Time sync completion unit, unit: %u\n"
+ "%06ld.%06d %s::%s: Unmapping region Id: %u, buffer addr: %p\n"
+ "%06ld.%06d %s::%s: Unsupported time domain for device wake assertion\n"
+ "%06ld.%06d %s::%s: Using exclusive timer workloop\n"
+ "%06ld.%06d %s::%s: _commandContext %p, _commandContextPa 0x%llx\n"
+ "%06ld.%06d %s::%s: _commandRing va 0x%llx, pa 0x%llx, size %u\n"
+ "%06ld.%06d %s::%s: _commandSetting._doorbellSetting time %llu, threshold %u\n"
+ "%06ld.%06d %s::%s: _eventRing[%d] va 0x%llx, pa 0x%llx, size %u\n"
+ "%06ld.%06d %s::%s: _eventSetting[%d] _intmod %d, _doorbellSetting time %llu, threshold %u, sync %u\n"
+ "%06ld.%06d %s::%s: _mapBase 0x%llx, _mapLimit 0x%llx\n"
+ "%06ld.%06d %s::%s: _msiRange[%d]: low %d, high %d\n"
+ "%06ld.%06d %s::%s: _numChannelContext %u, _channelContext %p, _channelContextPa 0x%llx\n"
+ "%06ld.%06d %s::%s: _numEventContext %u, _eventContext %p, _eventContextPa 0x%llx\n"
+ "%06ld.%06d %s::%s: _numEvents %d\n"
+ "%06ld.%06d %s::%s: _numHWEvents: %u, NUMHWER (from device): %d\n"
+ "%06ld.%06d %s::%s: _numMSI %d\n"
+ "%06ld.%06d %s::%s: _shadowChannelDoorbell[%u] 0x%llx\n"
+ "%06ld.%06d %s::%s: _shadowCommandDoorbell 0x%llx\n"
+ "%06ld.%06d %s::%s: _shadowEventDoorbell[%u] 0x%llx\n"
+ "%06ld.%06d %s::%s: abort client io completion\n"
+ "%06ld.%06d %s::%s: adjusted memSize %llu\n"
+ "%06ld.%06d %s::%s: alignment %u\n"
+ "%06ld.%06d %s::%s: allocate memory pool for %u\n"
+ "%06ld.%06d %s::%s: applying device wake 0x%x\n"
+ "%06ld.%06d %s::%s: assert %d, vote 0x%x, deviceWakeCurrent 0x%x _deviceWake 0x%x\n"
+ "%06ld.%06d %s::%s: assert: %u, vote: 0x%08x\n"
+ "%06ld.%06d %s::%s: bar0 0x%llx (+0x%x)\n"
+ "%06ld.%06d %s::%s: bar1 0x%llx (+0x%x)\n"
+ "%06ld.%06d %s::%s: bhi attach/start device failed %p\n"
+ "%06ld.%06d %s::%s: bhi attach/start interface failed %p\n"
+ "%06ld.%06d %s::%s: can't access device wake -- the doorbell is unavailable\n"
+ "%06ld.%06d %s::%s: can't access device wake -- the link is not up\n"
+ "%06ld.%06d %s::%s: capability count: %u, next cap: 0x%p\n"
+ "%06ld.%06d %s::%s: cf %p, intervalUs %llu, arg0 %p, arg1 %p\n"
+ "%06ld.%06d %s::%s: chID: %u, type: 0x%x, res2: 0x%x, allFlags: 0x%lx\n"
+ "%06ld.%06d %s::%s: change M-state %d -> %d\n"
+ "%06ld.%06d %s::%s: channel %u, instance %p, ring physical address 0x%llx\n"
+ "%06ld.%06d %s::%s: channel count %d\n"
+ "%06ld.%06d %s::%s: channelMemoryAllocInfo._pa 0x%llx\n"
+ "%06ld.%06d %s::%s: channelMemoryAllocInfo._size %llu\n"
+ "%06ld.%06d %s::%s: channelMemoryAllocInfo._va 0x%llx\n"
+ "%06ld.%06d %s::%s: chipset_name: %s\n"
+ "%06ld.%06d %s::%s: commandSleep (THREAD_INTERRUPTIBLE) woke with reason 0x%x\n"
+ "%06ld.%06d %s::%s: control %p\n"
+ "%06ld.%06d %s::%s: could not allocate _memoryPoolArray\n"
+ "%06ld.%06d %s::%s: cre %p\n"
+ "%06ld.%06d %s::%s: create %u, type %u\n"
+ "%06ld.%06d %s::%s: direction invalid\n"
+ "%06ld.%06d %s::%s: dmaCmd %p\n"
+ "%06ld.%06d %s::%s: domain: %u, seq: %u, fullSeq: 0x%lx, mach continuous_begin: %llu\n"
+ "%06ld.%06d %s::%s: done processing event rings\n"
+ "%06ld.%06d %s::%s: duplicate send image\n"
+ "%06ld.%06d %s::%s: error type %u, arg0 %p, arg1 %p\n"
+ "%06ld.%06d %s::%s: event index out of range\n"
+ "%06ld.%06d %s::%s: execution environment for current interfaces is %d. BB is changing to %d\n"
+ "%06ld.%06d %s::%s: failed readBytes %llu, size %llu\n"
+ "%06ld.%06d %s::%s: failed to alloc dma command\n"
+ "%06ld.%06d %s::%s: failed to allocate _interface\n"
+ "%06ld.%06d %s::%s: failed to allocate async call lock\n"
+ "%06ld.%06d %s::%s: failed to allocate commandGate\n"
+ "%06ld.%06d %s::%s: failed to allocate io pool\n"
+ "%06ld.%06d %s::%s: failed to allocate lock\n"
+ "%06ld.%06d %s::%s: failed to allocate memory\n"
+ "%06ld.%06d %s::%s: failed to allocate memory for channels\n"
+ "%06ld.%06d %s::%s: failed to allocate memory pool of size %d\n"
+ "%06ld.%06d %s::%s: failed to allocate request pool\n"
+ "%06ld.%06d %s::%s: failed to allocate resources for async completion\n"
+ "%06ld.%06d %s::%s: failed to allocate timer\n"
+ "%06ld.%06d %s::%s: failed to allocate timer commandGate\n"
+ "%06ld.%06d %s::%s: failed to allocate timer workloop\n"
+ "%06ld.%06d %s::%s: failed to allocate timesync event source\n"
+ "%06ld.%06d %s::%s: failed to create bhi device\n"
+ "%06ld.%06d %s::%s: failed to create bhi interface\n"
+ "%06ld.%06d %s::%s: failed to create mhi device\n"
+ "%06ld.%06d %s::%s: failed to create mhi interface\n"
+ "%06ld.%06d %s::%s: failed to create pools\n"
+ "%06ld.%06d %s::%s: failed to gen DMA address: 0x%x, numSeg %u, len %llu\n"
+ "%06ld.%06d %s::%s: failed to get bhi offset\n"
+ "%06ld.%06d %s::%s: failed to map memory in dart\n"
+ "%06ld.%06d %s::%s: failed to map result buffer\n"
+ "%06ld.%06d %s::%s: failed to prepare for DMA: 0x%x\n"
+ "%06ld.%06d %s::%s: failed to prepare image 0x%x\n"
+ "%06ld.%06d %s::%s: failed to prepare memory: 0x%x\n"
+ "%06ld.%06d %s::%s: failed to read CHDBOFF\n"
+ "%06ld.%06d %s::%s: failed to read ERDBOFF\n"
+ "%06ld.%06d %s::%s: failed to read MHICFG\n"
+ "%06ld.%06d %s::%s: failed to read MHISTATUS\n"
+ "%06ld.%06d %s::%s: failed to read MHIVER\n"
+ "%06ld.%06d %s::%s: failed to read capability register\n"
+ "%06ld.%06d %s::%s: failed to read capability register offset\n"
+ "%06ld.%06d %s::%s: failed to read execution environment\n"
+ "%06ld.%06d %s::%s: failed to read getMHICTRL\n"
+ "%06ld.%06d %s::%s: failed to read memory pool array object\n"
+ "%06ld.%06d %s::%s: failed to setup channel %p\n"
+ "%06ld.%06d %s::%s: failed to setup command ring\n"
+ "%06ld.%06d %s::%s: failed to setup context\n"
+ "%06ld.%06d %s::%s: failed to setup device\n"
+ "%06ld.%06d %s::%s: failed to setup device %p\n"
+ "%06ld.%06d %s::%s: failed to setup event ring\n"
+ "%06ld.%06d %s::%s: forClient %p, options 0x%08x, inGate %u\n"
+ "%06ld.%06d %s::%s: force: %u\n"
+ "%06ld.%06d %s::%s: from %s -> %s\n"
+ "%06ld.%06d %s::%s: fullSeq: 0x%lx\n"
+ "%06ld.%06d %s::%s: got completion for deregistered channel %u\n"
+ "%06ld.%06d %s::%s: hit %u, doorbell: %u\n"
+ "%06ld.%06d %s::%s: ignore m1 entry\n"
+ "%06ld.%06d %s::%s: imageSize = %llu\n"
+ "%06ld.%06d %s::%s: image[%u] pa 0x%llx\n"
+ "%06ld.%06d %s::%s: img %p\n"
+ "%06ld.%06d %s::%s: in sleep, ignore\n"
+ "%06ld.%06d %s::%s: incorrect alignment\n"
+ "%06ld.%06d %s::%s: index %u\n"
+ "%06ld.%06d %s::%s: index %u, ccid %u, cookie: 0x%lx, size %u, code %u, last %u\n"
+ "%06ld.%06d %s::%s: index %u, command %u, seq %u, reliable %u\n"
+ "%06ld.%06d %s::%s: index %u, ere %p, type %u\n"
+ "%06ld.%06d %s::%s: index %u, pa 0x%llx, size %u, code %u\n"
+ "%06ld.%06d %s::%s: index %u, write physical address 0x%llx\n"
+ "%06ld.%06d %s::%s: index out of range\n"
+ "%06ld.%06d %s::%s: initializing device wake to %s\n"
+ "%06ld.%06d %s::%s: interface is inactive\n"
+ "%06ld.%06d %s::%s: interval %llu\n"
+ "%06ld.%06d %s::%s: interval in us %llu, time mode %u\n"
+ "%06ld.%06d %s::%s: intfIdx %lu\n"
+ "%06ld.%06d %s::%s: link state already up\n"
+ "%06ld.%06d %s::%s: link state: %u, bailing!\n"
+ "%06ld.%06d %s::%s: linkState %u\n"
+ "%06ld.%06d %s::%s: looking for next cap at: 0x%p, offset (from bar0): %u\n"
+ "%06ld.%06d %s::%s: memSize %llu\n"
+ "%06ld.%06d %s::%s: memSize = %llu\n"
+ "%06ld.%06d %s::%s: memory is not page aligned\n"
+ "%06ld.%06d %s::%s: memory size is not page aligned\n"
+ "%06ld.%06d %s::%s: mhi attach/start device failed %p\n"
+ "%06ld.%06d %s::%s: mhi attach/start interface failed %p\n"
+ "%06ld.%06d %s::%s: mhi state: %u\n"
+ "%06ld.%06d %s::%s: msi in unexpected state %u\n"
+ "%06ld.%06d %s::%s: msi index out of range\n"
+ "%06ld.%06d %s::%s: msi index range overrun\n"
+ "%06ld.%06d %s::%s: msi index: %u\n"
+ "%06ld.%06d %s::%s: msi range malformed\n"
+ "%06ld.%06d %s::%s: nothing to do here... bailing.\n"
+ "%06ld.%06d %s::%s: numChannelContext (%u) greater than supported by device %d\n"
+ "%06ld.%06d %s::%s: numEvents (%u) greater than supported by device %d\n"
+ "%06ld.%06d %s::%s: numHWChannelContext (%u) greater than supported by device %d\n"
+ "%06ld.%06d %s::%s: numHWEvents (%u) greater than supported by device %d\n"
+ "%06ld.%06d %s::%s: options 0x%08x\n"
+ "%06ld.%06d %s::%s: pa 0x%llx\n"
+ "%06ld.%06d %s::%s: pa 0x%llx, completion code %u\n"
+ "%06ld.%06d %s::%s: pcie reset seperation workaround needed in ROM!\n"
+ "%06ld.%06d %s::%s: polling for MHICTRL.RESET to be 0, MHICTRL: 0x%x\n"
+ "%06ld.%06d %s::%s: pool needs to be atleast of dart page size %u\n"
+ "%06ld.%06d %s::%s: provider %p, options 0x%08x\n"
+ "%06ld.%06d %s::%s: provider %p, options 0x%08x, defer %p\n"
+ "%06ld.%06d %s::%s: read %u, buffer %p, size %u\n"
+ "%06ld.%06d %s::%s: region %u does not exist\n"
+ "%06ld.%06d %s::%s: region Id: %u\n"
+ "%06ld.%06d %s::%s: register %u, buff %p, size %u\n"
+ "%06ld.%06d %s::%s: register time event callback failed, ret: 0x%08x\n"
+ "%06ld.%06d %s::%s: res = 0x%x, code %u, size = %u\n"
+ "%06ld.%06d %s::%s: res = 0x%x, size = %llu, cookie %p\n"
+ "%06ld.%06d %s::%s: ring %d, 0x%llx\n"
+ "%06ld.%06d %s::%s: ring %d, not aligned to %u\n"
+ "%06ld.%06d %s::%s: ring %d, not large enough %u\n"
+ "%06ld.%06d %s::%s: ring 0x%llx\n"
+ "%06ld.%06d %s::%s: ring not aligned to %u\n"
+ "%06ld.%06d %s::%s: ring not large enough %u\n"
+ "%06ld.%06d %s::%s: shared mem region Id: %u, already present, client needs to it unmap first!\n"
+ "%06ld.%06d %s::%s: size %u\n"
+ "%06ld.%06d %s::%s: skip doorbell flush %u, pa 0x%llx\n"
+ "%06ld.%06d %s::%s: status %u, dbg1 0x%x, dbg2 0x%x, dbg3 0x%x, errCode %u\n"
+ "%06ld.%06d %s::%s: stopping memory pool for %llu\n"
+ "%06ld.%06d %s::%s: super::start failed\n"
+ "%06ld.%06d %s::%s: t %u, arg0 %p, arg1 %p\n"
+ "%06ld.%06d %s::%s: there are more event rings than context array can hold\n"
+ "%06ld.%06d %s::%s: time config: addr: 0x%p, 0x%lx\n"
+ "%06ld.%06d %s::%s: time sync -> doorbell num: %u, event num: %u\n"
+ "%06ld.%06d %s::%s: timerMode %u, arg1 %p\n"
+ "%06ld.%06d %s::%s: to %s\n"
+ "%06ld.%06d %s::%s: unable to allocate _cacheChannelRP array\n"
+ "%06ld.%06d %s::%s: unable to allocate _channel instance array\n"
+ "%06ld.%06d %s::%s: unable to allocate _msiRange\n"
+ "%06ld.%06d %s::%s: unable to allocate _shadowChannelDoorbell array\n"
+ "%06ld.%06d %s::%s: unable to allocate _shadowEventDoorbell array\n"
+ "%06ld.%06d %s::%s: unexpected memory pool array object entry %u\n"
+ "%06ld.%06d %s::%s: unexpected msi %d\n"
+ "%06ld.%06d %s::%s: unexpected register read request\n"
+ "%06ld.%06d %s::%s: unexpected size\n"
+ "%06ld.%06d %s::%s: va 0x%llx\n"
+ "%06ld.%06d %s::%s: version 0x%08x, expected 0x%08x\n"
+ "%06ld.%06d %s::%s: will process event rings %d to %d\n"
+ "1211111212221212121111111111111111111111221221222211111111112222"
+ "12111122111"
+ "AppleBasebandPCIMAVControl::%s: failed to create/init a reporter\n"
+ "AppleBasebandPCIMAVControl::%s: failed to start reporting\n"
+ "AppleBasebandPCIMAVControlReporter"
+ "AppleBasebandPCIMAVControlReporter::%s: Failed to retrieve Device Descriptor\n"
+ "abortChannel"
+ "abortChannelGated"
+ "abortChannels"
+ "allocateChannelMemory"
+ "allocateDeviceMemory"
+ "asserted"
+ "assignChannelMemory"
+ "asyncCallCountUpdate"
+ "asyncCompletion"
+ "asyncFunction"
+ "attach"
+ "callAsync"
+ "cancelAsync"
+ "cancelImage"
+ "cancelTimer"
+ "changeState"
+ "changeToM1"
+ "checkCompletedIO"
+ "checkIndexMSIRange"
+ "checkPendingCommand"
+ "checkPendingIO"
+ "close"
+ "closeGated"
+ "coalescedTransferCompletion"
+ "commandCompletion"
+ "completeIO"
+ "completeSharedEventIO"
+ "computeChannelMemory"
+ "computeDeviceMemory"
+ "createDeviceFunction"
+ "createPools"
+ "createSetupChannel"
+ "createSetupControl"
+ "createSetupDevice"
+ "createSetupInterface"
+ "createSetupInterfaces"
+ "deRegisterChannel"
+ "deasserted"
+ "deregisterTimeEventCallback"
+ "detach"
+ "deviceAlive"
+ "deviceWake"
+ "deviceWakeAsync"
+ "device_wake assert vote"
+ "device_wake deassert vote"
+ "device_wake off"
+ "device_wake on"
+ "didTerminate"
+ "engage"
+ "enterError"
+ "enterErrorCompletion"
+ "enterLowPower"
+ "errorFunction"
+ "execEnvChangeFunction"
+ "execEnvironmentChange"
+ "exitLowPower"
+ "findTimeCapability"
+ "finishImageCommand"
+ "finishMemoryCommand"
+ "free"
+ "getChannelMSIConfig"
+ "getChannelProperties"
+ "getDesiredLinkSpeed"
+ "getReporterInterfaceNames"
+ "initWithInfo"
+ "initialize"
+ "initializeDeviceWakeDoorbell"
+ "invokeAsync"
+ "ioCompletion"
+ "ioTransfer"
+ "linkDown"
+ "linkRecovery"
+ "linkUp"
+ "mStateChangeFunction"
+ "mapAckComplete_block_invoke"
+ "mapSharedMemory"
+ "mapSharedMemory_block_invoke"
+ "mapUnmapMessageComplete"
+ "mhiReset"
+ "mhiResetDone"
+ "msiInterrupt"
+ "notifyError"
+ "open"
+ "openGated"
+ "performTimeSync"
+ "prepareImageCommand"
+ "prepareMemoryCommand"
+ "prepareTimeSync"
+ "printChannelParams"
+ "printDeviceParams"
+ "processCurrentCommand"
+ "processERE"
+ "processTRE"
+ "queueCommand"
+ "queueTransfer"
+ "read"
+ "readExecutionEnvironment"
+ "readGated"
+ "readRegister"
+ "readRegisterGated"
+ "recoveryCheck"
+ "registerChannel"
+ "registerTimeEventCallback"
+ "resetChannel"
+ "resetChannelComplete"
+ "rscIOCompletion"
+ "scanCheck"
+ "sendCommand"
+ "sendImage"
+ "sendImageCompletion"
+ "sendImageCompletionGated"
+ "sendImageGated"
+ "sendMapUnmapMessage"
+ "sendTransfer"
+ "setDevice"
+ "setUpTimeConfig"
+ "setupChannel"
+ "setupCommandRing"
+ "setupContext"
+ "setupController"
+ "setupDevice"
+ "setupDeviceParams"
+ "setupEventRing"
+ "setupMapUnmapCompletion"
+ "setupTransferRing"
+ "shadowDBCheckFunction_block_invoke"
+ "shadowDBFunction_block_invoke"
+ "shadowDoorbell"
+ "shadowDoorbellCheck"
+ "shadowDoorbellFlush"
+ "shadowDoorbellProcess"
+ "site.AppleBasebandPCIMAVControlReporter"
+ "start"
+ "startChannel"
+ "startChannelComplete"
+ "startChannelGated"
+ "startChannels"
+ "startCheck"
+ "startTimer"
+ "stateTransition"
+ "stop"
+ "stopChannel"
+ "stopChannelComplete"
+ "synchronousFunction"
+ "teardownChannel"
+ "teardownController"
+ "teardownDevice"
+ "teardownPools"
+ "terminate"
+ "terminateDevice"
+ "terminateInterface"
+ "terminateInterfaces"
+ "terminate_block_invoke"
+ "timeDomainToDeviceWakeVote"
+ "timeSync"
+ "timeSyncCompletion"
+ "timeSyncEventCallback"
+ "timeSync_block_invoke"
+ "timer"
+ "timerCompletion"
+ "timerFunction_block_invoke"
+ "transferCompletion"
+ "triggerAsync"
+ "triggerMSIFunction"
+ "triggerRecovery"
+ "unmapAckComplete_block_invoke"
+ "unmapSharedMemory"
+ "unmapSharedMemory_block_invoke"
+ "willTerminate"
+ "write"
+ "writeGated"
+ "~ABPBHIChannel"
+ "~ABPBHIDevice"
+ "~ABPMHIChannel"
+ "~ABPMHIDevice"
- "121111121222121212111111111111111111111122122122221111111112222"

```

>  `com.apple.driver.AppleBasebandPCIMAVPDP`

```diff

-852.0.0.0.0
+853.0.0.0.0
   __TEXT.__const: 0x30
-  __TEXT.__cstring: 0xce8
-  __TEXT_EXEC.__text: 0xbacc
+  __TEXT.__cstring: 0x4b98
+  __TEXT_EXEC.__text: 0x254dc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x128
-  __DATA_CONST.__auth_got: 0x2a8
-  __DATA_CONST.__got: 0x68
+  __DATA_CONST.__auth_got: 0x2c8
+  __DATA_CONST.__got: 0x78
   __DATA_CONST.__mod_init_func: 0x38
   __DATA_CONST.__mod_term_func: 0x38
-  __DATA_CONST.__const: 0x3400
+  __DATA_CONST.__const: 0x3408
   __DATA_CONST.__kalloc_type: 0x400
-  Functions: 370
+  Functions: 379
   Symbols:   0
-  CStrings:  51
+  CStrings:  360
 
CStrings:
+ "%06ld.%06d %s::%s: \n"
+ "%06ld.%06d %s::%s: %s: --> \n"
+ "%06ld.%06d %s::%s: %u commands, pdp:packets: 0:%u 1:%u 2:%u 3:%u 4:%u 5:%u 6:%u 7:%u\n"
+ "%06ld.%06d %s::%s: -- Done.\n"
+ "%06ld.%06d %s::%s: -- done!\n"
+ "%06ld.%06d %s::%s: --done\n"
+ "%06ld.%06d %s::%s: Adding Tx pkt meta data failed with 0x%08x\n"
+ "%06ld.%06d %s::%s: Avail data indication -- qmap hdr 0x%08x\n"
+ "%06ld.%06d %s::%s: Avail data indication raw data 0x%08x %08x %08x %08x\n"
+ "%06ld.%06d %s::%s: Avail data timer expired, but interface was closed\n"
+ "%06ld.%06d %s::%s: Available data is non-zero, bytes: %u\n"
+ "%06ld.%06d %s::%s: Bad DL dump (offset=%llu, remain=%llu)\n"
+ "%06ld.%06d %s::%s: Bad RSC header\n"
+ "%06ld.%06d %s::%s: Bearer already mapped to Default Service\n"
+ "%06ld.%06d %s::%s: Bearer already mapped to Low Latency Service\n"
+ "%06ld.%06d %s::%s: Bearer switch already pending, ownerID: %u, bearerID: %u\n"
+ "%06ld.%06d %s::%s: Bearer switch complete !\n"
+ "%06ld.%06d %s::%s: Bearer switch in progress\n"
+ "%06ld.%06d %s::%s: Bearer switch notify!\n"
+ "%06ld.%06d %s::%s: Bearer switch request for ownerID: %u, bearer ID: %u, req type: %u\n"
+ "%06ld.%06d %s::%s: BearerID: %u not present for OwnerID: %u"
+ "%06ld.%06d %s::%s: Blocking outgoing traffic due to IP appender (unit number %u)\n"
+ "%06ld.%06d %s::%s: Cmd header: name 0x%02x: type 0x%02x: reserved 0x%04x: trans_id 0x%08x\n"
+ "%06ld.%06d %s::%s: Command response raw data 0x%08x %08x %08x %08x %08x\n"
+ "%06ld.%06d %s::%s: Creating interface: pdp_qctun\n"
+ "%06ld.%06d %s::%s: DFC End Marker Ack already pending for ownerID: %u\n"
+ "%06ld.%06d %s::%s: DFC End Marker command invalid length %u\n"
+ "%06ld.%06d %s::%s: DFC End Marker command raw data 0x%08x %08x %08x\n"
+ "%06ld.%06d %s::%s: DFC Info Query response raw data 0x%08x %08x\n"
+ "%06ld.%06d %s::%s: DFC Info query -- qmap hdr 0x%08x\n"
+ "%06ld.%06d %s::%s: DFC Info query -- qmap hdr 0x%08x %08x\n"
+ "%06ld.%06d %s::%s: DFC Info query for bearer ID: %u, ownerID: %u\n"
+ "%06ld.%06d %s::%s: DFC Info query raw data 0x%08x\n"
+ "%06ld.%06d %s::%s: DFC Query info response invalid length %u\n"
+ "%06ld.%06d %s::%s: DFC notify command invalid length %u\n"
+ "%06ld.%06d %s::%s: DFC notify command raw data 0x%08x %08x %08x\n"
+ "%06ld.%06d %s::%s: DFC power save mode ack not received!\n"
+ "%06ld.%06d %s::%s: DFC_INFO_QUERY response, ignore query response for inactive bearer ownerID: %u, bearer ID: %u, credits: %u\n"
+ "%06ld.%06d %s::%s: DFC_INFO_QUERY response, ignore query response for unmapped bearer ownerID: %u, bearer ID: %u, credits: %u\n"
+ "%06ld.%06d %s::%s: DL packet dump\n"
+ "%06ld.%06d %s::%s: DL packet dump (offset=%llu, length=%u, remain=%llu)\n"
+ "%06ld.%06d %s::%s: Data powersave mode command -- qmap hdr 0x%08x\n"
+ "%06ld.%06d %s::%s: Data powersave mode command raw data 0x%08x %08x %08x %08x %08x\n"
+ "%06ld.%06d %s::%s: Deferring Ack for DFC End Marker\n"
+ "%06ld.%06d %s::%s: Delete _CreditsQueue entries for intf: %u\n"
+ "%06ld.%06d %s::%s: Duplicate / redundant bearer removed notification for bearerID: %u, ownerID: %u, seq num: %u\n"
+ "%06ld.%06d %s::%s: Duplicate DFC_NOTIFY command for bearerID: %u, ownerID: %u, seq num: %u\n"
+ "%06ld.%06d %s::%s: Error detected on Modem - removing bearerID: %u\n"
+ "%06ld.%06d %s::%s: Failed to create matching dictionary\n"
+ "%06ld.%06d %s::%s: Flushing pci service's stage queue pkts to queue set, packetCnt: %u\n"
+ "%06ld.%06d %s::%s: Got reset bearers marker: %u for this interface\n"
+ "%06ld.%06d %s::%s: Hdr Size:%u interface %u, pkt size %u, padding %u\n"
+ "%06ld.%06d %s::%s: IP Appender failed with 0x%08x\n"
+ "%06ld.%06d %s::%s: Incorrect bearer mapping state, ownerID: %u, bearerID: %u, current mapped owner: %u\n"
+ "%06ld.%06d %s::%s: Inserting at HEAD\n"
+ "%06ld.%06d %s::%s: Inserting at Tail\n"
+ "%06ld.%06d %s::%s: Inserting before ownerID: %u, bearer ID: %u, credits: %u,\n"
+ "%06ld.%06d %s::%s: Interface advisory report: owner %u: payload bytes %u\n"
+ "%06ld.%06d %s::%s: Invalid NL pair data length, expected: %u, actual: %u\n"
+ "%06ld.%06d %s::%s: Invalid bearer status : %u\n"
+ "%06ld.%06d %s::%s: Invalid bearer status: %u, for bearer ID: %u\n"
+ "%06ld.%06d %s::%s: Invalid bearer switch request type, req type: %u\n"
+ "%06ld.%06d %s::%s: Invalid chksm\n"
+ "%06ld.%06d %s::%s: Invalid intf number: %u!\n"
+ "%06ld.%06d %s::%s: Invalid number of NLs, received: %u, max: %u\n"
+ "%06ld.%06d %s::%s: Invalid number of bearers: %u\n"
+ "%06ld.%06d %s::%s: Invalid ownerID : %u\n"
+ "%06ld.%06d %s::%s: Invalid ownerID: %u\n"
+ "%06ld.%06d %s::%s: Invalid ownerID: %u, bearerID: %u already mapped to ownerID: %u\n"
+ "%06ld.%06d %s::%s: LL Bearer Switch Ack raw data 0x%08x %08x\n"
+ "%06ld.%06d %s::%s: LL Bearer Switch Request Ack invalid length %u != (Header + Payload) size: %u\n"
+ "%06ld.%06d %s::%s: LL Bearer Switch Request Ack invalid length %u < Header Size: %u\n"
+ "%06ld.%06d %s::%s: LL Bearer Switch Status command, invalid length %u != (Header + Payload) size: %u\n"
+ "%06ld.%06d %s::%s: LL Bearer Switch Status raw data 0x%08x %08x\n"
+ "%06ld.%06d %s::%s: LQM report: owner %u: payload bytes %u\n"
+ "%06ld.%06d %s::%s: NL pair data len (%u), exceeded max len\n"
+ "%06ld.%06d %s::%s: NL[%u](Length: %u, chksum map: 0x%x, NumPkts: %u)\n"
+ "%06ld.%06d %s::%s: NULL owner!\n"
+ "%06ld.%06d %s::%s: No UL pkts queued for ownerID: %u\n"
+ "%06ld.%06d %s::%s: No bearer present for this OwnerID: %u\n"
+ "%06ld.%06d %s::%s: No bearer present for this ownerID: %u\n"
+ "%06ld.%06d %s::%s: No credit update for owner: %u\n"
+ "%06ld.%06d %s::%s: PCIe link is down or is going down\n"
+ "%06ld.%06d %s::%s: Packet txid: %u, Expected txid: %u\n"
+ "%06ld.%06d %s::%s: Packet type is not QMAP control! \n"
+ "%06ld.%06d %s::%s: Packet: %p, Txid: %u\n"
+ "%06ld.%06d %s::%s: Preparing response: %s\n"
+ "%06ld.%06d %s::%s: Previous tail entry - ownerID: %u, bearer ID: %u, credits: %u,\n"
+ "%06ld.%06d %s::%s: RSC service: %u\n"
+ "%06ld.%06d %s::%s: Received DFC_END_MARKER for ownerID: %u, bearer ID: %u, seqNum: %u\n"
+ "%06ld.%06d %s::%s: Received DFC_INFO_QUERY response for ownerID: %u, bearer ID: %u, credits: %u\n"
+ "%06ld.%06d %s::%s: Received DFC_NOTIFY for ownerID: %u, bearer ID: %u, credits: %u, seq num: %u, bearer status: %u\n"
+ "%06ld.%06d %s::%s: Redundant bearer removed notificaiton, bearer ID: %u already removed\n"
+ "%06ld.%06d %s::%s: Removing bearer failed!\n"
+ "%06ld.%06d %s::%s: Request Bearer Switch -- qmap cmd hdr 0x%08x %08x\n"
+ "%06ld.%06d %s::%s: Request Bearer Switch -- qmap hdr 0x%08x\n"
+ "%06ld.%06d %s::%s: Request Bearer Switch raw data 0x%08x %08x\n"
+ "%06ld.%06d %s::%s: Sending DFC End Marker Ack for ownerID: %u\n"
+ "%06ld.%06d %s::%s: Setting packet buffer base / limit failed: 0x%llx\n"
+ "%06ld.%06d %s::%s: Start --\n"
+ "%06ld.%06d %s::%s: Start, options 0x%08x --\n"
+ "%06ld.%06d %s::%s: Stop queueing pkts - DFC end marker / UL flow switched!\n"
+ "%06ld.%06d %s::%s: Tcp Ack Allowed: %u\n"
+ "%06ld.%06d %s::%s: Temp failure in switching bearer ID: %u\n"
+ "%06ld.%06d %s::%s: Trigger DFC End Marker Ack\n"
+ "%06ld.%06d %s::%s: UL packet dump\n"
+ "%06ld.%06d %s::%s: Unexpected - bearer info entry is NULL!\n"
+ "%06ld.%06d %s::%s: Unexpected Tx\n"
+ "%06ld.%06d %s::%s: Unexpected command in RSC channel\n"
+ "%06ld.%06d %s::%s: Unexpected control packet for out of band Qmap control service\n"
+ "%06ld.%06d %s::%s: Unexpected next header for RSC\n"
+ "%06ld.%06d %s::%s: Unexpected pci service ID: %u\n"
+ "%06ld.%06d %s::%s: Unknown or unhandled command, name: %u\n"
+ "%06ld.%06d %s::%s: Unmapping bearerID: %u from OwnerID: %u\n"
+ "%06ld.%06d %s::%s: Unsupported status\n"
+ "%06ld.%06d %s::%s: Updated credits for ownerID: %u, credits remaining: %u\n"
+ "%06ld.%06d %s::%s: [%u] bearerID: %u, credits: %u\n"
+ "%06ld.%06d %s::%s: _rxHEAD: %p, _rxTail: %p\n"
+ "%06ld.%06d %s::%s: allowed Tx bytes: %u\n"
+ "%06ld.%06d %s::%s: bad command packet size: %u\n"
+ "%06ld.%06d %s::%s: bad length %u for link status report payload\n"
+ "%06ld.%06d %s::%s: bearer switch ack, bearer ID: %u, status: %u\n"
+ "%06ld.%06d %s::%s: bearer switch status, bearer ID: %u, status: %u\n"
+ "%06ld.%06d %s::%s: bearer switch was not pending! bearer ID: %u, \n"
+ "%06ld.%06d %s::%s: bearer switch was not successful! bearer ID: %u, \n"
+ "%06ld.%06d %s::%s: bearer switch was not successful! bearer ID: %u, status: %u \n"
+ "%06ld.%06d %s::%s: bytesRead (%llu) != header (%lu) + body (%u)\n"
+ "%06ld.%06d %s::%s: cache max reached, dropping packet\n"
+ "%06ld.%06d %s::%s: cannot receive interface advisory report for nonexisting owner %u\n"
+ "%06ld.%06d %s::%s: cannot receive link status report for nonexisting owner %u\n"
+ "%06ld.%06d %s::%s: chain length = %u\n"
+ "%06ld.%06d %s::%s: chain length = %u, txid 0x%u --> 0x%u, total DL data %u bytes\n"
+ "%06ld.%06d %s::%s: cksmValid: %u, numNLs: %u, incIPID: %u\n"
+ "%06ld.%06d %s::%s: close called on an unopened client %p\n"
+ "%06ld.%06d %s::%s: closeVal: %u, closeType: %u, contextID: %u\n"
+ "%06ld.%06d %s::%s: cmd header: name 0x%02x: type 0x%02x: reserved 0x%04x: trans_id 0x%08x\n"
+ "%06ld.%06d %s::%s: cmd version: %u\n"
+ "%06ld.%06d %s::%s: command header raw data: 0x%08x 0x%08x\n"
+ "%06ld.%06d %s::%s: command name: %u\n"
+ "%06ld.%06d %s::%s: consumed:%u\n"
+ "%06ld.%06d %s::%s: count %u\n"
+ "%06ld.%06d %s::%s: count %u, telescoping limit %u\n"
+ "%06ld.%06d %s::%s: count: %u\n"
+ "%06ld.%06d %s::%s: dealloc packet %p directly\n"
+ "%06ld.%06d %s::%s: device: %p, stateNumber: %lu\n"
+ "%06ld.%06d %s::%s: disable soft flow control for pdp_ip%u due to %u pending write bytes\n"
+ "%06ld.%06d %s::%s: disabling flow control due to QMAP command\n"
+ "%06ld.%06d %s::%s: draining pci service's stage queue pkts to queue set, packetCnt: %u\n"
+ "%06ld.%06d %s::%s: duplicate QMAP extension header type (%u)\n"
+ "%06ld.%06d %s::%s: enabling flow control due to QMAP command\n"
+ "%06ld.%06d %s::%s: enabling flow control for pdp_ip%u due to %u pending Tx bytes\n"
+ "%06ld.%06d %s::%s: error 0x%08x\n"
+ "%06ld.%06d %s::%s: failed to clone packet\n"
+ "%06ld.%06d %s::%s: failed to create Available data zero indication timer\n"
+ "%06ld.%06d %s::%s: failed to create Rx queue\n"
+ "%06ld.%06d %s::%s: failed to create Tx completion queue\n"
+ "%06ld.%06d %s::%s: failed to create Tx queue\n"
+ "%06ld.%06d %s::%s: failed to create power save mode timer\n"
+ "%06ld.%06d %s::%s: failed to open provider\n"
+ "%06ld.%06d %s::%s: failed to set packet limits: 0x%08x\n"
+ "%06ld.%06d %s::%s: flow control %s: owner %u: ipFamily %u: sequence 0x%04x: QoS 0x%08x\n"
+ "%06ld.%06d %s::%s: flow control command invalid IP family %u\n"
+ "%06ld.%06d %s::%s: flow control command invalid length %u\n"
+ "%06ld.%06d %s::%s: flow control command raw data 0x%08x %08x\n"
+ "%06ld.%06d %s::%s: flow control disable sequence number mismatch (got %u, expected %u)\n"
+ "%06ld.%06d %s::%s: flow controlling bearerID: %u, ownerID: %u\n"
+ "%06ld.%06d %s::%s: found client, unit %u\n"
+ "%06ld.%06d %s::%s: free count: %u\n"
+ "%06ld.%06d %s::%s: interface %u not opened yet, packet will be queued\n"
+ "%06ld.%06d %s::%s: interface %u, size %u, padding %u, command %u\n"
+ "%06ld.%06d %s::%s: interface 0x%p not found\n"
+ "%06ld.%06d %s::%s: interface down\n"
+ "%06ld.%06d %s::%s: intf %p, count %u\n"
+ "%06ld.%06d %s::%s: intf number: %u, open: %u, owner = %p\n"
+ "%06ld.%06d %s::%s: invalid interface %d\n"
+ "%06ld.%06d %s::%s: invalid length for LQM command, length: %u\n"
+ "%06ld.%06d %s::%s: invalid null header\n"
+ "%06ld.%06d %s::%s: invoked with packetCount = 0\n"
+ "%06ld.%06d %s::%s: kOffPowerState\n"
+ "%06ld.%06d %s::%s: kOffPowerState, enable data powersave mode, allow notification: %u\n"
+ "%06ld.%06d %s::%s: kOnPowerState, disable data powersave mode\n"
+ "%06ld.%06d %s::%s: konPowerState\n"
+ "%06ld.%06d %s::%s: last queued pkt completed, trigger DFC end marker Ack for %u\n"
+ "%06ld.%06d %s::%s: link status report: owner %u: payload bytes %u\n"
+ "%06ld.%06d %s::%s: low latency service: %u\n"
+ "%06ld.%06d %s::%s: null header\n"
+ "%06ld.%06d %s::%s: out of band QMAP control: %u\n"
+ "%06ld.%06d %s::%s: oversize header (%u < %u)\n"
+ "%06ld.%06d %s::%s: oversize header (%u < %zu)\n"
+ "%06ld.%06d %s::%s: owner %u does not exist, processing command anyway\n"
+ "%06ld.%06d %s::%s: owner: %u is inactive\n"
+ "%06ld.%06d %s::%s: owner: %u is not active\n"
+ "%06ld.%06d %s::%s: owner: %u is not opened yet\n"
+ "%06ld.%06d %s::%s: ownerID: %u\n"
+ "%06ld.%06d %s::%s: ownerID: %u has no bearer info entry for bearerID: %u\n"
+ "%06ld.%06d %s::%s: ownerID: %u was previously flow controlled, updated credits: %u\n"
+ "%06ld.%06d %s::%s: ownerID: %u, avail data bytes: %u\n"
+ "%06ld.%06d %s::%s: ownerID: %u, bearerID: %u, Active -> Removed\n"
+ "%06ld.%06d %s::%s: ownerID: %u, bearerID: %u, Inactive -> Active\n"
+ "%06ld.%06d %s::%s: ownerID: %u, bearerID: %u, curr bearer state: %u, new status: %u\n"
+ "%06ld.%06d %s::%s: ownerID: %u, bearerID: %u, switchStatus: %u\n"
+ "%06ld.%06d %s::%s: ownerID: %u, credits queue...\n"
+ "%06ld.%06d %s::%s: packet 0x%p, count: %u\n"
+ "%06ld.%06d %s::%s: packet: %p, TxID: %u\n"
+ "%06ld.%06d %s::%s: packet: %p, TxID: %u, next TxID: %u, count: %u\n"
+ "%06ld.%06d %s::%s: pad bytes (%u) is >= total length (%u)\n"
+ "%06ld.%06d %s::%s: pci service not available\n"
+ "%06ld.%06d %s::%s: pciService not available\n"
+ "%06ld.%06d %s::%s: pdp:packets: 0:%u 1:%u 2:%u 3:%u 4:%u 5:%u 6:%u 7:%u\n"
+ "%06ld.%06d %s::%s: pdp_ip%u flow controlled, but continue until soft flow control is enabled\n"
+ "%06ld.%06d %s::%s: qmap_control_service not present in plist\n"
+ "%06ld.%06d %s::%s: read size too small: %llu\n"
+ "%06ld.%06d %s::%s: received ack for Data Powersave Mode Control command\n"
+ "%06ld.%06d %s::%s: redundant flow control disable command for owner %u\n"
+ "%06ld.%06d %s::%s: redundant flow control enable command for owner %u\n"
+ "%06ld.%06d %s::%s: refCon 0x%p, status 0x%x\n"
+ "%06ld.%06d %s::%s: refcon: %p, status 0x%x\n"
+ "%06ld.%06d %s::%s: refcon: %p, status 0x%x, enqueue: %u\n"
+ "%06ld.%06d %s::%s: registering callback for ownerID: %u\n"
+ "%06ld.%06d %s::%s: requesting upto: %llu usecs to PM\n"
+ "%06ld.%06d %s::%s: residue (%llu) < header (%lu) + body (%u)\n"
+ "%06ld.%06d %s::%s: returning free space: %u, service id: %u\n"
+ "%06ld.%06d %s::%s: sending data powersave mode, ownerID: %u, enable: %u\n"
+ "%06ld.%06d %s::%s: sending response...\n"
+ "%06ld.%06d %s::%s: sending response: %s\n"
+ "%06ld.%06d %s::%s: sent bytes: %u\n"
+ "%06ld.%06d %s::%s: sent bytes: %u, pkt cnt: %u\n"
+ "%06ld.%06d %s::%s: setting %u msecs timer\n"
+ "%06ld.%06d %s::%s: skipping disable powersave mode, first power on\n"
+ "%06ld.%06d %s::%s: soft flow control active on pdp_ip%u\n"
+ "%06ld.%06d %s::%s: staged: %u\n"
+ "%06ld.%06d %s::%s: super::handleOpen() failed\n!"
+ "%06ld.%06d %s::%s: super::open failed\n"
+ "%06ld.%06d %s::%s: too many packets in transfer (limit %u), dropping packet\n"
+ "%06ld.%06d %s::%s: transfer size %u, interface %u, txid %u\n"
+ "%06ld.%06d %s::%s: txid 0x%08x: status 0x%x, packet 0x%p\n"
+ "%06ld.%06d %s::%s: txid 0x%x\n"
+ "%06ld.%06d %s::%s: unable to get unsent bytes: 0x%x\n"
+ "%06ld.%06d %s::%s: unexpected command type %u\n"
+ "%06ld.%06d %s::%s: unexpected command type: %u\n"
+ "%06ld.%06d %s::%s: unit number %u invalid or nonexistent\n"
+ "%06ld.%06d %s::%s: unrecognized QMAP extension header type (%u)\n"
+ "%06ld.%06d %s::%s: unsupported command: name 0x%02x: type %u: transactionID 0x%08x\n"
+ "%06ld.%06d %s::%s: unsupported flow control QoS 0x%08x\n"
+ "%06ld.%06d %s::%s: updating bearer credits failed!\n"
+ "%06ld.%06d %s::%s: updating owners in QMAP control intf failed\n"
+ "%06ld.%06d %s::%s: waiting for Low Latency service\n"
+ "%06ld.%06d %s::%s: waiting for QMAP control service\n"
+ "%06ld.%06d %s::%s: waiting for RSC service\n"
+ "12111112122212121111111112111121111111111111121121121121111211211111212222"
+ "121111121222121211112111222222212111112222212121"
+ "121111121222121212121111111111111111111111222222222222222222222222222222222221111111111111111111111111111111111111111111111111111111111111111111111222222222222222221111121122222222221111111111111111222122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222111111111111111111111111111111112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211111111111111112222"
+ "121111121222121212121111111111111111111111222222222222222222222222222222222221111111111111111111111111111111111111111111111111111111111111111111111222222222222222221111121122222222222222222222222212212112"
+ "1211111212221212121211111111111111111111112222222222222222222222222222222222211111111111111111111111111111111111111111111111111111111111111111111112222222222222222211111211222222222222222222222222122121121"
+ "addTxPktMetaData"
+ "allocQueues"
+ "availDataZeroTimerCompletion"
+ "bearerSwitchComplete_block_invoke"
+ "closeGated"
+ "commandResponse"
+ "commandResponse_block_invoke"
+ "createRxSubmissionQueue"
+ "decodeQMAPHeader"
+ "decodeQMAPRSCHeader"
+ "disable"
+ "discardRxPacket"
+ "dumpOwnerCreditsQueue"
+ "enable"
+ "flowControlAllBearers"
+ "free"
+ "getAvailData"
+ "getOwnerCredits_block_invoke"
+ "handleOpen"
+ "initWithOptions"
+ "openGated"
+ "outputComplete"
+ "powerSaveModeTimerCompletion"
+ "powerStateWillChangeTo"
+ "powerStateWillChangeTo_block_invoke"
+ "processBearerCreditsGated"
+ "processCtrlPacket"
+ "processDFCEndMarker"
+ "processDFCInfoQuery"
+ "processDFCLLSwitchRequest"
+ "processDFCLLSwitchStatus"
+ "processDFCNotify"
+ "processDFCPowerSaveMode"
+ "processMavExtCmdAdvisoryReport"
+ "processMavExtCmdLQM"
+ "queryFlowControlCredits_block_invoke"
+ "queryFreeULSpace"
+ "queueRxBuffersGated"
+ "readComplete"
+ "registerBearerSwitchCallback"
+ "requestBearerSwitchGated"
+ "requestTxGated"
+ "resetOwnerCreditsQueue"
+ "rxQueueCallbackGated"
+ "sendAvailDataIndication_block_invoke"
+ "sendDFCEndMarkerAck_block_invoke"
+ "sendDataPowerSaveMode_block_invoke"
+ "setBearerSwitchPending_block_invoke"
+ "setInterfaceOwnerGated"
+ "setPowerStateGated"
+ "start"
+ "terminate"
+ "triggerBearerSwitch_block_invoke"
+ "triggerRxDequeue_block_invoke"
+ "txCompletionCallbackGated"
+ "txQueueCallbackGated"
+ "updateOwnerCreditsGated_block_invoke"
+ "usesQmapControlService"
+ "willTerminate"
+ "willTerminate_block_invoke"
- "1211111212221212111111111211112111111111111121121121121111211211111212222"
- "12111112122212121111211122222221211111222221212"
- "12111112122212121212111111111111111111111222222222222222222222222222222222221111111111111111111111111111111111111111111111111111111111111111111111222222222222222221111121122222222221111111111111111222122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222111111111111111111111111111111112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211111111111111112222"
- "12111112122212121212111111111111111111111222222222222222222222222222222222221111111111111111111111111111111111111111111111111111111111111111111111222222222222222221111121122222222222222222222222212212112"
- "121111121222121212121111111111111111111112222222222222222222222222222222222211111111111111111111111111111111111111111111111111111111111111111111112222222222222222211111211222222222222222222222222122121121"

```

>  `com.apple.driver.AppleConvergedIPCOLYBTControl`

```diff

-126.0.0.0.0
-  __TEXT.__cstring: 0x7c34
+150.0.0.0.0
+  __TEXT.__cstring: 0x7cc1
   __TEXT.__const: 0x90
-  __TEXT_EXEC.__text: 0x4878c
+  __TEXT_EXEC.__text: 0x490d4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x1f0

   __DATA_CONST.__got: 0xf8
   __DATA_CONST.__mod_init_func: 0x58
   __DATA_CONST.__mod_term_func: 0x58
-  __DATA_CONST.__const: 0x4cc0
+  __DATA_CONST.__const: 0x4d10
   __DATA_CONST.__kalloc_type: 0xc40
   __DATA_CONST.__kalloc_var: 0x500
-  Functions: 968
+  Functions: 975
   Symbols:   0
-  CStrings:  1001
+  CStrings:  1007
 
CStrings:
+ "%s::%s: Chip is inaccessible \n"
+ "%s::%s: trigger DAR based trap\n"
+ "12222221221121212122212222222211111222222222112211111111111111111222222"
+ "isChipInaccessible"
+ "setChipInaccessible"
+ "setDARBasedTrap"
+ "updateDARTrapDoorbell"
- "1222222122112121212221222222221111122222222211221111111111111111122222"

```

>  `com.apple.driver.AppleConvergedPCI`

```diff

-126.0.0.0.0
+150.0.0.0.0
   __TEXT.__const: 0x1e0
-  __TEXT.__cstring: 0x6c62
-  __TEXT_EXEC.__text: 0x3f640
+  __TEXT.__cstring: 0x6c99
+  __TEXT_EXEC.__text: 0x3fa24
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x248
   __DATA.__common: 0x2d0

   __DATA_CONST.__got: 0x108
   __DATA_CONST.__mod_init_func: 0x68
   __DATA_CONST.__mod_term_func: 0x68
-  __DATA_CONST.__const: 0x4878
+  __DATA_CONST.__const: 0x48a8
   __DATA_CONST.__kalloc_type: 0x1380
-  Functions: 1076
+  Functions: 1082
   Symbols:   0
-  CStrings:  898
+  CStrings:  901
 
CStrings:
+ "isChipInaccessible"
+ "setChipInaccessible"
+ "setDARBasedTrap"

```

>  `com.apple.driver.AppleDiskImages2`

```diff

-385.100.33.0.0
-  __TEXT.__cstring: 0x20c4
+385.120.3.0.0
+  __TEXT.__cstring: 0x20c3
   __TEXT.__os_log: 0x11d7
   __TEXT.__const: 0x90
   __TEXT_EXEC.__text: 0xd808
CStrings:
+ "385.120.3"
- "385.100.33"

```

>  `com.apple.driver.AppleGPIOICController`

```diff

-57.0.0.0.0
+59.0.0.0.0
   __TEXT.__const: 0x150
   __TEXT.__cstring: 0xe10
-  __TEXT_EXEC.__text: 0xaacc
+  __TEXT_EXEC.__text: 0xab24
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x128

```

>  `com.apple.driver.AppleH16ANEInterface`

```diff

-8.509.0.0.0
+8.510.0.0.0
   __TEXT.__const: 0x6f0
   __TEXT.__cstring: 0xc831
   __TEXT.__os_log: 0x346e3
-  __TEXT_EXEC.__text: 0xb9e1c
+  __TEXT_EXEC.__text: 0xb9e40
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x3948
   __DATA.__common: 0x3f0

```

>  `com.apple.driver.AppleMobileFileIntegrity`

```diff

-938.100.89.0.0
+938.120.9.0.1
   __TEXT.__cstring: 0xb0d5
-  __TEXT.__const: 0x1540
+  __TEXT.__const: 0x1560
   __TEXT.__os_log: 0x32d
-  __TEXT_EXEC.__text: 0x269f8
+  __TEXT_EXEC.__text: 0x26a54
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x402
   __DATA.__common: 0xb0
CStrings:
+ "19:54:30"
+ "Mar 24 2025"
- "17:58:56"
- "Mar 15 2025"

```

>  `com.apple.driver.AppleOLYHAL`

```diff

 450.19.0.0.0
   __TEXT.__const: 0x798
   __TEXT.__cstring: 0x45f5
-  __TEXT_EXEC.__text: 0x1d270
+  __TEXT_EXEC.__text: 0x1d260
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x18c
   __DATA.__common: 0x170

```

>  `com.apple.driver.ApplePearlSEPDriver`

```diff

-754.100.55.0.0
+754.120.3.0.0
   __TEXT.__const: 0x308
   __TEXT.__cstring: 0x99ea
   __TEXT.__os_log: 0x45d6
-  __TEXT_EXEC.__text: 0x3ccb4
+  __TEXT_EXEC.__text: 0x3cc94
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xcd
   __DATA.__common: 0x1d8

```

>  `com.apple.driver.AppleProcessorTrace`

```diff

-52.100.16.0.0
-  __TEXT.__cstring: 0x4398
+52.120.4.0.0
+  __TEXT.__cstring: 0x4355
   __TEXT.__const: 0x398
   __TEXT.__os_log: 0x1586
-  __TEXT_EXEC.__text: 0x213bc
+  __TEXT_EXEC.__text: 0x21370
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x380

   __DATA_CONST.__const: 0x83f8
   __DATA_CONST.__kalloc_type: 0x580
   __DATA_CONST.__kalloc_var: 0xa0
-  Functions: 1214
+  Functions: 1213
   Symbols:   0
-  CStrings:  418
+  CStrings:  417
 
CStrings:
- "IOMemoryMap *AppleProcessorTraceSession::getTraceBufferMap() const"

```

>  `com.apple.driver.AppleSPURose`

```diff

-1014.100.12.0.0
+1014.120.2.0.0
   __TEXT.__const: 0x30
-  __TEXT.__cstring: 0x1f7c
+  __TEXT.__cstring: 0x1f98
   __TEXT.__os_log: 0x1d43
-  __TEXT_EXEC.__text: 0x186ec
+  __TEXT_EXEC.__text: 0x187b4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x248
   __DATA.__common: 0x268

   __DATA_CONST.__got: 0xd0
   __DATA_CONST.__mod_init_func: 0x78
   __DATA_CONST.__mod_term_func: 0x78
-  __DATA_CONST.__const: 0x32c8
+  __DATA_CONST.__const: 0x32f8
   __DATA_CONST.__kalloc_type: 0x3c0
-  Functions: 655
+  Functions: 658
   Symbols:   0
-  CStrings:  369
+  CStrings:  370
 
CStrings:
+ "121111121222121212222222222222222211111111211212212212212212212212212212212212212212212212212212212222111121122222222111121"
+ "function-rose_smc_ds_reset"
- "12111112122212121222222222222222221111111121121221221221221221221221221221221221221221221221221221222211112112222222211121"

```

>  `com.apple.driver.AppleT8110DART`

```diff

-458.100.10.0.0
+458.120.3.0.0
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x2828
-  __TEXT_EXEC.__text: 0xdd6c
+  __TEXT.__cstring: 0x286b
+  __TEXT_EXEC.__text: 0xdf30
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x38
-  __DATA_CONST.__auth_got: 0x170
+  __DATA_CONST.__auth_got: 0x178
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__mod_init_func: 0x8
   __DATA_CONST.__mod_term_func: 0x8
   __DATA_CONST.__const: 0x758
   __DATA_CONST.__kalloc_type: 0x2c0
   __DATA_CONST.__kalloc_var: 0x410
-  Functions: 145
+  Functions: 146
   Symbols:   0
-  CStrings:  223
+  CStrings:  224
 
CStrings:
+ "(%s) %s::%s: DART interrupt while dirty shutdown is in progress\n"
+ "12111112122212121112211211111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111112222222222222222222222221212223312111111111111111111111111111111111111111111111111111111111111111112112112112111121222122321212212111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111121112222222222211122222222222111222222222222111211121112211121112111221111111111111111111111111111111111111111111111111111"
- "121111121222121211122112111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222222212122233121111111111111111111111111111111111111111111111111111111111111111121121121121111212221223212122111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111121112222222222211122222222222111222222222222111211121112211121112111221111111111111111111111111111111111111111111111111111"

```

>  `com.apple.driver.AppleT8140CLPC`

```diff

-1175.100.103.0.0
-  __TEXT.__cstring: 0x2be6
-  __TEXT.__const: 0xb7c
-  __TEXT_EXEC.__text: 0x51000
+1175.120.17.0.0
+  __TEXT.__cstring: 0x2c16
+  __TEXT.__const: 0xbd4
+  __TEXT_EXEC.__text: 0x52c5c
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xb288
-  __DATA.__common: 0x9321
-  __DATA.__bss: 0x278
+  __DATA.__data: 0xb2c8
+  __DATA.__common: 0x9521
+  __DATA.__bss: 0x288
   __DATA_CONST.__auth_got: 0x4b0
   __DATA_CONST.__got: 0xd8
-  __DATA_CONST.__mod_init_func: 0x118
+  __DATA_CONST.__mod_init_func: 0x120
   __DATA_CONST.__mod_term_func: 0x18
-  __DATA_CONST.__const: 0x55e0
+  __DATA_CONST.__const: 0x55f8
   __DATA_CONST.__kalloc_type: 0x380
   __DATA_CONST.__kalloc_var: 0x370
-  Functions: 1195
+  Functions: 1197
   Symbols:   0
-  CStrings:  466
+  CStrings:  468
 
CStrings:
+ "2025-03-24T20:15:02-07:00"
+ "AppleCLPC-1175.120.17"
+ "OperatingStates"
+ "map_perf_scores[type][base_index] >= bottom_first"
+ "setBudgetToAGXFunction"
- "2025-03-15T18:26:16-07:00"
- "AppleCLPC-1175.100.103"
- "perf_scores[type][base] >= bottom_first"

```

>  `com.apple.driver.AudioDMAController-T8140`

```diff

-440.39.0.0.0
+450.3.0.0.0
   __TEXT.__const: 0x1e0
-  __TEXT.__cstring: 0x7c94
-  __TEXT.__os_log: 0x289
-  __TEXT_EXEC.__text: 0x2d908
+  __TEXT.__cstring: 0x7cac
+  __TEXT.__os_log: 0x24d
+  __TEXT_EXEC.__text: 0x2d9b0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x248
   __DATA.__common: 0x150

   __DATA_CONST.__got: 0xe0
   __DATA_CONST.__mod_init_func: 0x28
   __DATA_CONST.__mod_term_func: 0x20
-  __DATA_CONST.__const: 0x16a0
+  __DATA_CONST.__const: 0x16b0
   __DATA_CONST.__kalloc_type: 0x400
-  Functions: 410
+  Functions: 411
   Symbols:   0
   CStrings:  802
 
CStrings:
+ "20:30:45"
+ "Mar 24 2025"
+ "_theMachine->canSleep()"
- "%s: Could not suspend in deadline of %u seconds (CSM = %s)."
- "18:13:02"
- "Mar 15 2025"

```

>  `com.apple.driver.EXDisplayPipeH17P`

```diff

-6.1.10.7.0
+6.2.2.0.0
   __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x1bd4
-  __TEXT_EXEC.__text: 0x7648
+  __TEXT.__cstring: 0x1bd2
+  __TEXT_EXEC.__text: 0x7424
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x60

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xf00
   __DATA_CONST.__kalloc_type: 0x80
-  Functions: 152
+  Functions: 150
   Symbols:   0
-  CStrings:  146
+  CStrings:  145
 
CStrings:
+ "EXDisplayPipe: error: submitTelemetry(...) failed\n"
- "[EXDisplayPipe] %s: Invalid message\n"
- "exbrightMessage"

```

>  `com.apple.driver.FairPlayIOKit`

```diff

 72.13.0.0.0
   __TEXT.__cstring: 0x1cc7
   __TEXT.__const: 0x49850
-  __TEXT_EXEC.__text: 0x1ccd10
+  __TEXT_EXEC.__text: 0x1cd144
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x13a8
   __DATA.__common: 0x5fe9

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
+ "20:27:45"
+ "20:27:46"
+ "Mar 24 2025"
- "19:48:02"
- "Mar 17 2025"

```

>  `com.apple.driver.corecapture`

```diff

   __TEXT.__os_log: 0x40cf
   __TEXT.__const: 0x130
   __TEXT.__cstring: 0x1ef9
-  __TEXT_EXEC.__text: 0x27938
+  __TEXT_EXEC.__text: 0x2792c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x2e0

```

>  `com.apple.filesystems.apfs`

```diff

-2332.102.1.0.0
+2332.120.27.0.0
   __TEXT.__const: 0x990
-  __TEXT.__cstring: 0x49d66
-  __TEXT_EXEC.__text: 0x140104
+  __TEXT.__cstring: 0x49f8b
+  __TEXT_EXEC.__text: 0x14035c
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x698
+  __DATA.__data: 0x6a0
   __DATA.__bss: 0xca8
   __DATA_CONST.__auth_got: 0x1120
   __DATA_CONST.__got: 0x1b0

   __DATA_CONST.__assert: 0x14
   Functions: 2268
   Symbols:   0
-  CStrings:  6419
+  CStrings:  6429
 
CStrings:
+ "%s:%d: %s Deleting incompatible volume %s\n"
+ "%s:%d: %s Deleting volume %s, volume index %u\n"
+ "%s:%d: %s Request to delete volume %u was denied, nx is read only\n"
+ "%s:%d: %s Request to delete volume %u was denied, user not authorized to delete the volume\n"
+ "%s:%d: %s Request to delete volume %u was denied, volume is still open\n"
+ "%s:%d: %s Request to delete volume %u was denied, wrong volume index\n"
+ "%s:%d: %s Request to delete volume index %u, made by process %s (pid %d)\n"
+ "%s:%d: %s can't mark compressed inode as a purgeable fault\n"
+ "19:57:23"
+ "19:57:24"
+ "2025/03/24"
+ "2332.120.27"
+ "Mar 24 2025"
+ "apfs-2332.120.27"
+ "volumeDelete"
- "17:47:17"
- "2025/03/15"
- "2332.102.1"
- "Mar 15 2025"
- "apfs-2332.102.1"

```

>  `com.apple.iokit.AppleARMIISAudio`

```diff

   __TEXT.__os_log: 0x2862
   __TEXT.__cstring: 0x2e47
   __TEXT.__const: 0xc8
-  __TEXT_EXEC.__text: 0x15800
+  __TEXT_EXEC.__text: 0x157e4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x188
   __DATA.__common: 0x60
-  __DATA_CONST.__auth_got: 0x2b0
+  __DATA_CONST.__auth_got: 0x2a0
   __DATA_CONST.__got: 0x90
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x10

   __DATA_CONST.__const: 0x1150
   __DATA_CONST.__kalloc_type: 0x240
   __DATA_CONST.__kalloc_var: 0x1e0
-  Functions: 301
+  Functions: 300
   Symbols:   0
   CStrings:  389
 

```

>  `com.apple.iokit.IODisplayPortFamily`

```diff

-739.100.9.0.0
-  __TEXT.__cstring: 0x7d18
-  __TEXT.__os_log: 0x9562
-  __TEXT.__const: 0x300
-  __TEXT_EXEC.__text: 0x5beb8
+739.120.3.0.0
+  __TEXT.__cstring: 0x7d78
+  __TEXT.__os_log: 0x950b
+  __TEXT.__const: 0x440
+  __TEXT_EXEC.__text: 0x5bca0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x550
   __DATA.__bss: 0x10
-  __DATA_CONST.__auth_got: 0x538
+  __DATA_CONST.__auth_got: 0x540
   __DATA_CONST.__got: 0x170
   __DATA_CONST.__mod_init_func: 0x110
   __DATA_CONST.__mod_term_func: 0x108
-  __DATA_CONST.__const: 0xf8e8
+  __DATA_CONST.__const: 0xf8c8
   __DATA_CONST.__kalloc_type: 0x840
   __DATA_CONST.__kalloc_var: 0x280
   Functions: 2355
CStrings:
+ "121111121222121211122222111111111122212222212222222122222122222122222222222222222222222222222222222222222222222222211111111121111111122221111112222222222222222222211"
+ "121222221111211112212222222222"
+ "A44602"
+ "A44606"
+ "A44610"
+ "D1baba"
- "1212222211111211112212222222222"
- "AVRoot"
- "AVRoot(%llx) is not in the DT plane for transport=%s, len=%d\n"
- "IOAV[%d] %s<0x%llx>::%s: AVRoot(%llx) is not in the DT plane for transport=%s, len=%d\n"
- "NULL"
- "setAVRoot_block_invoke"

```

>  `com.apple.iokit.IONVMeFamily`

```diff

-775.100.17.0.0
+775.120.7.0.0
   __TEXT.__const: 0x708
-  __TEXT.__cstring: 0xf8eb
-  __TEXT_EXEC.__text: 0x600a0
+  __TEXT.__cstring: 0xfaef
+  __TEXT_EXEC.__text: 0x60884
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x4e4
   __DATA.__common: 0x528
   __DATA.__bss: 0x10
   __DATA_CONST.__auth_got: 0x688
-  __DATA_CONST.__got: 0x180
+  __DATA_CONST.__got: 0x188
   __DATA_CONST.__mod_init_func: 0x100
   __DATA_CONST.__mod_term_func: 0x100
-  __DATA_CONST.__const: 0xcc98
+  __DATA_CONST.__const: 0xccc0
   __DATA_CONST.__kalloc_type: 0x7c0
   __DATA_CONST.__kalloc_var: 0x550
-  Functions: 3169
+  Functions: 3183
   Symbols:   0
-  CStrings:  1710
+  CStrings:  1718
 
CStrings:
+ "%s::%d:Sleep Notification Tunnel for msg type %u took %llu us\n"
+ "%s::%d:cancelling S2R IDLE Sleep\n"
+ "%s::%d:nvme: ANS Sleep Notification with Opcode %lu failed with ASP status 0x%x\n"
+ "%s::%d:nvme: ANS Sleep Notification with Opcode %lu failed with status 0x%x\n"
+ "%s::%d:received systemPowerChange 0x%x\n"
+ "( 0 != fSystemPowerNotifier )"
+ "121111121222121211211111111221222111111111112222112122222222222121111111222221122221211111111111111111111111111111111222122212211111111111221112111111111111111111111111111111111111111111111111111111111111111122222222222222222222222222222222222112122112111111111111111112111112111121121121111111111111112212122"
+ "12111112122212121121111111122122211111111111222211212222222222212111111122222112222121111111111111111111111111111111122212221221111111111122111211111111111111111111111111111111111111111111111111111111111111112222222222222222222222222222222222211212211211111111111111111211111211112112112111111111111111221212212"
+ "IOReturn AppleANS2NVMeController::SendSleepNotificationToANS(uint32_t, bool *)"
+ "virtual IOReturn AppleANS2NVMeController::systemPowerChange(void *, UInt32, IOService *, void *, vm_size_t)"
- "1211111212221212112111111112212221111111111122221121222222222221211111112222211222212111111111111111111111111111111112221222122111111111112211121111111111111111111111111111111111111111111111111111111111111111222222222222222222222222222222222221121221121111111111111111121111121111211211211111111111111122122"
- "121111121222121211211111111221222111111111112222112122222222222121111111222221122221211111111111111111111111111111111222122212211111111111221112111111111111111111111111111111111111111111111111111111111111111122222222222222222222222222222222222112122112111111111111111112111112111121121121111111111111112212212"

```

>  `com.apple.iokit.IOPCIFamily`

```diff

-681.100.11.0.0
+681.120.2.0.0
   __TEXT.__const: 0x710
   __TEXT.__cstring: 0x548e
-  __TEXT_EXEC.__text: 0x2fca4
+  __TEXT_EXEC.__text: 0x2fca8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xcc
   __DATA.__common: 0x218
CStrings:
+ "19:54:23"
+ "Mar 24 2025"
- "17:44:25"
- "Mar 15 2025"

```

>  `com.apple.iokit.IOSkywalkFamily`

```diff

-521.102.1.0.0
+521.120.3.0.0
   __TEXT.__cstring: 0x1b0e
-  __TEXT.__const: 0xe30
-  __TEXT_EXEC.__text: 0x37f0c
+  __TEXT.__const: 0xe10
+  __TEXT_EXEC.__text: 0x37e78
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xe8
   __DATA.__common: 0x6b0

```

>  `com.apple.kernel`

```diff

-11417.102.9.0.0
-  __TEXT.__const: 0x34860
+11417.120.80.0.3
+  __TEXT.__const: 0x34500
   __TEXT.__copyio_vectors: 0xf0
-  __TEXT.__cstring: 0x731db
-  __TEXT.__os_log: 0x2a64c
+  __TEXT.__cstring: 0x7686c
+  __TEXT.__os_log: 0x2a698
   __TEXT.__eh_frame: 0x610
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x2d8
-  __DATA_CONST.__const: 0xaba08
+  __DATA_CONST.__const: 0xabbb8
   __DATA_CONST.__hib_const: 0x120
-  __DATA_CONST.__kalloc_type: 0x136c0
+  __DATA_CONST.__kalloc_type: 0x13980
   __DATA_CONST.__kalloc_var: 0x7ee0
-  __DATA_CONST.__assert: 0xf0
+  __DATA_CONST.__assert: 0x1cc
   __DATA_CONST.__exclaves_bt: 0x60
-  __DATA_CONST.__brk_desc: 0x60
+  __DATA_CONST.__brk_desc: 0x78
   __DATA_SPTM.__const: 0x3c000
   __TEXT_EXEC.__hib_text: 0xcc8
-  __TEXT_EXEC.__text: 0x80a344
+  __TEXT_EXEC.__text: 0x81e4fc
   __TEXT_BOOT_EXEC.__bootcode: 0x514c
   __KLD.__text: 0x1638
   __LASTDATA_CONST.__mod_init_func: 0x8

   __KLDDATA.__mod_init_func: 0x8
   __KLDDATA.__mod_term_func: 0x8
   __KLDDATA.__bss: 0x1
-  __DATA.__data: 0x17d81
-  __DATA.__lock_grp: 0x5960
+  __DATA.__data: 0x185c1
+  __DATA.__lock_grp: 0x5a10
   __DATA.__percpu: 0x6e80
-  __DATA.__common: 0x5b9f0
-  __DATA.__bss: 0x96008
+  __DATA.__common: 0x5bd30
+  __DATA.__bss: 0x96208
   __BOOTDATA.__data: 0x18000
-  __BOOTDATA.__init_entry_set: 0x11070
-  __BOOTDATA.__init: 0x5b180
+  __BOOTDATA.__init_entry_set: 0x11190
+  __BOOTDATA.__init: 0x5b188
   __BOOTDATA.__static_ifinit: 0x8
   __BOOTDATA.__static_if: 0x0
   __PRELINK_TEXT.__text: 0x0

   __PLK_DATA_CONST.__data: 0x0
   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
-  __LINKINFO.__symbolsets: 0x4662c
-  Functions: 19948
+  __LINKINFO.__symbolsets: 0x46658
+  Functions: 20175
   Symbols:   0
-  CStrings:  17594
+  CStrings:  17886
 
CStrings:
+ "\n(kern_coredump_routine) : kern_dump_record_file failed with %d\n"
+ "\nBeginning coredump of %s\n"
+ "\nBeginning dump of panic region of size 0x%zx\n"
+ "\nCore dump took %llu cycles\n"
+ " Compressed file length is %llu bytes\n"
+ "!os_add_overflow(*__counter, 1, __counter)"
+ "!os_sub_overflow(*__counter, 1, __counter)"
+ "!os_sub_overflow(*__counter, list.vmpl_count, __counter)"
+ "%"
+ "%.12s-cp"
+ "%lld..\n"
+ "%lu"
+ "%qx:%x"
+ "%s (during forwarding) returned 0x%x\n"
+ "%s (passing along request) returned 0x%x\n"
+ "%s kvtophys() for address %p returned NULL\n"
+ "%s next stage output failed\n"
+ "%s%c%s%c%s%c"
+ "%s(%p, %llu, %p) : called with invalid length %llu\n"
+ "%s(%p, %llu, %p) : called with too much data, %llu written, %llu left\n"
+ "%s() : failed to write data (%llu bytes remaining) :%d\n"
+ "%s() : failed to write legacy bin spec version : coredump_save_note_data() returned 0x%x\n"
+ "%s() : failed to write mach header : kdp_core_output(%p, %lu, %p) returned error 0x%x\n"
+ "%s() : failed to write main bin spec structure : coredump_save_note_data() returned 0x%x\n"
+ "%s() : failed to write note %llu of %llu : kdp_core_output() returned  error 0x%x\n"
+ "%s() : failed to write sw_vers string : coredump_save_note_data() returned 0x%x\n"
+ "%s() : failed to write thread data : kdp_core_output() returned 0x%x\n"
+ "%s() : failed to write zero fill padding : kdp_core_output(%p, %llu, NULL) returned 0x%x\n"
+ "%s() : found %d expected LC_THREAD (%d)\n"
+ "%s() : ran out of space to save threads with %llu of %llu remaining\n"
+ "%s() called too many times, %llu note descriptions already recorded\n"
+ "%s() called with invalid data_owner\n"
+ "%s(): encountered unknown debug header entry %d, including anyway with name '%s'\n"
+ "%s(): failed to write load binary spec structure for binary #%d ('%s'): callback returned 0x%x\n"
+ "%s(0x%llx, 0x%llx, %p) : called with invalid addresses : start 0x%llx >= end 0x%llx\n"
+ "%s(0x%llx, 0x%llx, %p) : called with invalid addresses for 32-bit : start 0x%llx, end 0x%llx\n"
+ "%s(0x%llx, 0x%llx, %p) : coredump_save_segment_descriptions() called too many times, %llu segment descriptions already recorded\n"
+ "%s(0x%llx, 0x%llx, %p) : failed to write segment %llu of %llu : kdp_core_output(%p, %lu, %p) returned  error 0x%x\n"
+ "%s(0x%llx, 0x%llx, %p) : failed to write segment %llu of %llu. kdp_core_output(%p, %lu, %p) returned error %d\n"
+ "%s(0x%llx, 0x%llx, %p) : ran out of space to save commands with %llu of %llu remaining\n"
+ "%s-%s-%u.%u.%u.%u-%x%s"
+ "%s/%s"
+ "%s: cannot exclude region starting at %p with size %zu (not page aligned) @%s:%d"
+ "%s: cannot exclude region starting at %p with size %zu (zero or overflowing size) @%s:%d"
+ "%s: context allocation failure\n"
+ "%s: no task is set\n"
+ "%s: skipping inactive task\n"
+ "%s: skipping kernel because excluded regions list is locked\n"
+ "%s: skipping locked task\n"
+ "%s: skipping task with locked vm map\n"
+ "%s: vm map traversal failed: %d\n"
+ "(%s) : coredump_init failed with %d\n"
+ "(%s) : coredump_save_note_description returned %d while writing binary info LC_NOTE description"
+ "(%s) : get_summary failed with %d\n"
+ "(%s) : header size not populated after coredump_get_summary\n"
+ "(%s) : kcc_coredump_save_note_data failed with 0x%x\n"
+ "(%s) : kcc_coredump_save_note_data returned without all note data written, %llu of %llu remaining\n"
+ "(%s) : kcc_coredump_save_note_descriptions failed with %d\n"
+ "(%s) : kcc_coredump_save_sw_vers failed with 0x%x\n"
+ "(%s) : kcc_coredump_save_sw_vers_detail_cb failed with 0x%x\n"
+ "(%s) : save_note_descriptions returned without all note descriptions written, %llu of %llu remaining\n"
+ "(%s) : save_note_note_summary failed with %d\n"
+ "(%s) : save_segment_descriptions failed with %d\n"
+ "(%s) : save_segment_descriptions returned without all segment descriptions written, %llu of %llu remaining\n"
+ "(%s) : save_thread_state failed with %d\n"
+ "(%s) : save_thread_state returned without all thread descriptions written, %llu of %llu remaining\n"
+ "(aea_read_callback) next stage read proc returned 0x%x\n"
+ "(aea_stage_outproc) aea_close() returned %d\n"
+ "(aea_stage_outproc) aea_open() returned %d\n"
+ "(aea_stage_outproc) aea_write() returned %zd\n"
+ "(aea_stage_reset) aea_close() returned %d\n"
+ "(aea_write_callback) next stage outproc returned 0x%x\n"
+ "(disk_stage_read) IOPolledFileRead(%llu) returned 0x%x\n"
+ "(disk_stage_read) IOPolledFileSeek(0x%llx) returned 0x%x\n"
+ "(disk_stage_read) IOPolledFileWrite (during seek) returned 0x%x\n"
+ "(disk_stage_read) Kickstarting IOPolledFileRead(0) returned 0x%x\n"
+ "(disk_stage_write) IOPolledFileSeek(0x%llx) returned 0x%x\n"
+ "(disk_stage_write) IOPolledFileWrite (during final flush) returned 0x%x\n"
+ "(disk_stage_write) IOPolledFileWrite(gIOPolledCoreFileVars, %p, 0x%llx, NULL) returned 0x%x\n"
+ "(disk_stage_write) disk_stage_read (during final chunk seek) returned 0x%x\n"
+ "(disk_stage_write) disk_stage_read (during seek) returned 0x%x\n"
+ "(do_kern_dump close) outproc(KDP_EOF, NULL, 0, 0) returned 0x%x\n"
+ "(do_kern_dump coredump log) outproc(KDP_DATA, NULL, %lu, %p) returned 0x%x\n"
+ "(do_kern_dump paniclog) outproc(KDP_DATA, NULL, %lu, %p) returned 0x%x\n"
+ "(do_kern_dump seek begin) outproc(KDP_SEEK, NULL, %lu, %p) foffset = 0x%llx returned 0x%x\n"
+ "(do_kern_dump seek logfile) outproc(KDP_SEEK, NULL, %lu, %p) foffset = 0x%llx returned 0x%x\n"
+ "(do_kern_dump write public key) returned 0x%x\n"
+ "(kdp_core_output) outproc(KDP_DATA, NULL, 0x%llx, %p) returned 0x%x\n"
+ "(kdp_reset_output_vars) Encryption requested, is unavailable, and enforcement is active. Skipping current core.\n"
+ "(kern_coredump_routine) : failed to flush final core data : kdp_core_output(%p, 0, NULL) returned 0x%x\n"
+ "(kern_coredump_routine) : failed to write zero fill padding (%llu bytes remaining) : kdp_core_output(%p, %llu, NULL) returned 0x%x\n"
+ "(kern_coredump_routine) : save_segment_data returned without all segment data written, %llu of %llu remaining\n"
+ "(kern_dump_seek_to_next_file) outproc(KDP_SEEK, NULL, %lu, %p) foffset = 0x%llx returned 0x%x\n"
+ "(kern_dump_update_header) outproc data flush returned 0x%x\n"
+ "(kern_dump_update_header) outproc explicit flush returned 0x%x\n"
+ "(kern_dump_update_header) outproc(KDP_DATA, NULL, %lu, %p) returned 0x%x\n"
+ "(kern_dump_update_header) outproc(KDP_SEEK, NULL, %lu, %p) foffset = 0x%llx returned 0x%x\n"
+ "(kern_dump_write_public_key) outproc data flush returned 0x%x\n"
+ "(kern_dump_write_public_key) outproc explicit flush returned 0x%x\n"
+ "(kern_dump_write_public_key) outproc(KDP_DATA, NULL, %llu, NULL) returned 0x%x\n"
+ "(kern_dump_write_public_key) outproc(KDP_DATA, NULL, %u, %p) returned 0x%x\n"
+ "(kern_dump_write_public_key) outproc(KDP_SEEK, NULL, %lu, %p) foffset = 0x%llx returned 0x%x\n"
+ "(zlib_zoutput) outproc(KDP_DATA, NULL, 0x%x, %p) returned 0x%x\n"
+ ".gz"
+ "/cores/core.%d"
+ "/private/preboot/kernelcore"
+ "/private/var/cores"
+ "/private/var/dextcores"
+ "/private/var/vm/kernelcore"
+ "100.."
+ "11122221222222222222222112"
+ "121212112"
+ "; UUID="
+ "; stext="
+ "A dump server was not specified in the boot-args, terminating kernel core dump.\n"
+ "Attempting connection to panic server configured at IP %s, port %d\n"
+ "B16@?0^{task={lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}{os_refcnt=AI}BBBBIIQ^{_vm_map}{queue_entry=^{queue_entry}^{queue_entry}}^{task_watchports}^v{queue_entry=^{queue_entry}^{queue_entry}}^{restartable_ranges}^{processor_set}^{affinity_space}iIiiissiQ{recount_task=^{recount_track}^{recount_usage}}{lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}[4^{ipc_port}]^{ipc_port}[14{exception_action=^{ipc_port}iiii^{label}}]{hardened_exception_action={exception_action=^{ipc_port}iiii^{label}}II}^{ipc_port}^{ipc_port}^{ipc_port}^{ipc_port}^{ipc_port}[3^{ipc_port}]^^{ipc_port}^{ipc_space}^{ledger}{queue_entry=^{queue_entry}^{queue_entry}}iI^vQQCACQQQiBBB^Q^Q^Q^Q^Q^Q^Q^Q^QIIIIII^{proc_ro}^{kcdata_descriptor}Q{queue_entry=^{queue_entry}^{queue_entry}}^{label}IIQQIBBBBb4b4b4b4CCCCCB*^{vm_shared_region}QQQ^{thread_call}{queue_entry=^{queue_entry}^{queue_entry}}ii^{bank_task}^{ipc_importance_task}{vm_extmod_statistics=qqqqqq}{task_requested_policy=b1b1b2b2b1b1b2b1b3b3b3b1b5b3b3b1b3b1b1b3b1b3b1b1b17}{task_effective_policy=b1b1b2b1b1b1b2b1b1b3b3b1b1b1b4b1b1b1b3b3b1b1b29}{task_pend_token=(?={?=b1b1b1b1b1b1b1b1b1b1b1b1b1}I)}b1b1b1b1b1b27b1b1b1b1b28^{io_stat_info}{task_writes_counters=QQQQ}{task_writes_counters=QQQQ}{_cpu_time_qos_stats=QQQQQQQ}{_cpu_time_qos_stats=QQQQQQQ}IIQCCCiii{queue_entry=^{queue_entry}^{queue_entry}}{lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}b16b1b1b1b1b1b1b1[2^{coalition}][2{queue_entry=^{queue_entry}^{queue_entry}}]Q^vCCCCIQ{queue_entry=^{queue_entry}^{queue_entry}}{queue_entry=^{queue_entry}^{queue_entry}}iIQ[16C]Q^{_vmobject_list_output_}Q^{vm_deferred_reclamation_metadata_s}^v^vIQ{task_security_config=(?={?=b1b1b1}C)}}8"
+ "Boot-args specify %d MB kernel corefile\n"
+ "Corefile is not yet initialized. Cannot write a coredump to disk\n"
+ "Couldn't retrieve volume status. Error %d\n"
+ "Detected remote error, terminating...\n"
+ "Detected stale/invalid seq num. Expected: %d, received %d\n"
+ "Done\nCoredump complete of %s, dumped %llu segments (%llu bytes), %llu threads (%llu bytes) overall uncompressed file length %llu bytes."
+ "EOF Flush: Detected stale/invalid seq num. Expected: %d, received %d\n"
+ "Error: No transport device registered for kernel crashdump\n"
+ "Failed to %s the corefile. Error %d\n"
+ "Failed to dump coprocessor cores\n"
+ "Failed to dump userspace process cores\n"
+ "Failed to flush panic region data : kdp_core_output(%p, 0, NULL) returned 0x%x\n"
+ "Failed to open corefile of size %llu MB (low disk space)\n"
+ "Failed to open corefile of size %llu MB (returned error 0x%x)\n"
+ "Failed to open the corefile. Error %d\n"
+ "Failed to record panic region in corefile header, kern_dump_record_file returned 0x%x\n"
+ "Failed to seek to beginning of next core\n"
+ "Failed to seek to panic region file offset 0x%llx, kern_dump_seek_to_next_file returned 0x%x\n"
+ "Failed to write panic region to file, kdp_coreoutput(outstate, %zu, %p) returned 0x%x\n"
+ "IOPolledFileFlush() returned 0x%x\n"
+ "IOPolledFileFlush(0x%p) : IOStartPolledIO(0x%p, kIOPolledFlush, 0, 0, 0) returned 0x%x\n"
+ "IOPolledFilePollersClose (during EOF) returned 0x%x\n"
+ "IOPolledFilePollersOpen returned 0x%x\n"
+ "IOPolledFilePollersSetup for corefile failed with error: 0x%x\n"
+ "IOPolledFilePollersSetup(%d) error 0x%x\n"
+ "IOPolledFileSeek(0x%llx) returned 0x%x\n"
+ "IOPolledFileSeek(gIOPolledCoreFileVars, 0) returned 0x%x\n"
+ "IOPolledFileSeek: called to seek to 0x%llx greater than file size of 0x%llx\n"
+ "IOPolledFileWrite (during EOF) returned 0x%x\n"
+ "IOPolledFileWrite (during seek) returned 0x%x\n"
+ "IOPolledFileWrite(0x%p, 0x%p, %llu, 0x%p) : IOStartPolledIO(0x%p, kIOPolledWrite, %llu, 0x%llx, %d) returned 0x%x\n"
+ "IOPolledFileWrite(gIOPolledCoreFileVars, %p, 0x%llx, NULL) returned 0x%x\n"
+ "IOPolledInterface::checkForWork[%d] 0x%x\n"
+ "IOPolledInterface::close[%d] 0x%x\n"
+ "IOPolledInterface::ioStatus 0x%x\n"
+ "IOPolledInterface::open[%d] 0x%x\n"
+ "IOPolledInterface::probe[%d] 0x%x\n"
+ "IOPolledInterface::startIO[%d] 0x%x\n"
+ "IOPolledInterfaceActive"
+ "IOPolledInterfaceStack"
+ "KDPCoreStageInit"
+ "Kernel map size is %llu\n"
+ "Kernel timed out waiting for hardware debugger to update handshake structure."
+ "LZ4 stage is not yet initialized. Cannot write a coredump to disk\n"
+ "No contact in %d seconds\n"
+ "Opened corefile of size %llu MB\n"
+ "Opened file %s, size %qd, extents %ld, maxio %qx ssd %d\n"
+ "Original panic string:\n"
+ "Preferred Block Size"
+ "Recorded panic region in corefile at offset 0x%llx, compressed to %llu bytes\n"
+ "Resolved %s's (or proxy's) link level address\n"
+ "Routing through specified router IP %s (%u)\n"
+ "Sending write request for %s\n"
+ "Set a new encryption key for coredumps"
+ "Setting coredump status as done!\n"
+ "Skipping coredump\n"
+ "Skipping panic region dump\n"
+ "Skipping userspace coredump, coredump list is locked\n"
+ "System dump aborted.\n"
+ "Transmitting kernel state, please wait:\n"
+ "Transmitting packets to link level address: %02x:%02x:%02x:%02x:%02x:%02x\n"
+ "Transmitting panic log, please wait: "
+ "Transmitting system log, please wait: "
+ "Unable to create core header packet.\n"
+ "Unable to retrieve range for root memory device %d\n"
+ "Unknown format character %c in `%s'\n"
+ "Volume is low on space. Not allocating kernel corefile.\n"
+ "Waiting for hardware shared memory debugger, handshake structure is at virt: %p, phys %p\n"
+ "We were in the middle of initializing LZ4 stage. Cannot write a coredump to disk\n"
+ "We were in the middle of initializing encryption. Marking it as unavailable\n"
+ "We were in the middle of initializing the disk stage. Cannot write a coredump to disk\n"
+ "Writing local cores...\n"
+ "ZERR %d\n"
+ "Zlib stage is not initialized. Cannot write a coredump to shared memory\n"
+ "Zlib stage is not initialized. Cannot write a coredump to the network\n"
+ "_kdp_ipstr"
+ "_panicd_corename"
+ "_panicd_ip"
+ "_router_ip"
+ "addrable bits"
+ "apple_encrypted_archive interface registration callback is already set @%s:%d"
+ "buffer_stage_outproc (during flush) returned 0x%x\n"
+ "buffer_stage_outproc (during forwarding) returned 0x%x\n"
+ "com.apple.private.coredump-encryption-key"
+ "com.apple.private.custom-coredump-location"
+ "com.apple.private.enable-coredump-on-panic-seed-privacy-approved"
+ "com.apple.private.exclaves.indicator_min_on_time"
+ "com.apple.private.security.file-unencrypt-access"
+ "compression interface registration callback is already set @%s:%d"
+ "coredump"
+ "coredump_encryption"
+ "coredump_encryption_key"
+ "coredump_init returned KERN_NODE_DOWN, skipping this core\n"
+ "coredump_save_note_data"
+ "coredump_save_note_description"
+ "coredump_save_segment_data"
+ "coredump_save_segment_data failed with %d\n"
+ "coredump_save_segment_descriptions"
+ "coredump_save_summary"
+ "coredump_save_sw_vers"
+ "coredump_save_sw_vers_legacy"
+ "coredump_save_thread_state"
+ "corefile"
+ "corefile path selection in device-tree is not one of the allowed values: %s, Using default %s\n"
+ "corefile path selection in device-tree was set to: %s (value: %s)\n"
+ "corefile_size_mb"
+ "custom"
+ "drivercorefile"
+ "dumpinfo does not fit into KDP packet.\n"
+ "error 0x%x from IOGetHibernationCryptKey\n"
+ "error 0x%x opening polled file\n"
+ "handshake structure not initialized\n"
+ "hwm_user_cores"
+ "inet_aton() failed interpreting %s as a panic server IP\n"
+ "inet_aton() failed interpreting %s as an IP\n"
+ "inline call to debugger(machine_startup)"
+ "kdp panic: %s"
+ "kdp_core.c"
+ "kdp_core_exclude_region"
+ "kdp_corefile"
+ "kdp_crashdump_pkt_size"
+ "kdp_ip_addr"
+ "kdp_panic_dump: unexpected pending input packet"
+ "kdp_poll"
+ "kdp_raise_exception"
+ "kdp_reply: no input packet"
+ "kdp_send: no input packet"
+ "kdp_send: packet too large (%u > %d)"
+ "kdp_send_crashdump_data returned 0x%x\n"
+ "kdp_send_crashdump_pkt failed with error %d\n"
+ "kdp_set_dump_info: Skipping invalid panicd port %u (using %d)\n"
+ "kern ver str"
+ "kern_coredump_routine"
+ "kern_dump_init"
+ "kern_dump_save_note_data"
+ "kern_open_file_for_direct_io took %qd ms\n"
+ "kernel-core-dump-location"
+ "load binary"
+ "main bin spec"
+ "memory_backing_aware_buffer_stage_outproc"
+ "memorystatus_kill_on_zone_map_exhaustion: failed to allocate jetsam reason\n"
+ "misaligned file pos %qx\n"
+ "octet"
+ "outproc(KDP_WRQ, NULL, 0, NULL) returned 0x%x\n"
+ "panic context"
+ "panic_region"
+ "panicd_port"
+ "paniclog"
+ "physical page is before the start of DRAM: %#x < %#x) @%s:%d"
+ "physical page is beyond the end of managed DRAM: %#x >= %#x) @%s:%d"
+ "pid %ld (%s), uid (%u): corename is too long\n"
+ "pid %ld (%s), uid (%u): unexpected end of string after %% token\n"
+ "polled file major %d, minor %d, blocksize %ld, pollers %d\n"
+ "preboot"
+ "progress_notify_stage_outproc"
+ "read from"
+ "save_seg_data: pmap traversal failed: %d\n"
+ "save_seg_desc: pmap traversal failed: %d\n"
+ "save_summary: pmap traversal failed: %d\n"
+ "secure_core: Unable to seek to the start of file: %d\n"
+ "security_config="
+ "security_config=0x%x"
+ "site.IOPolledFileIOVars"
+ "site.struct kern_userspace_coredump_context"
+ "site.typeof(*data)"
+ "site.typeof(*region)"
+ "skipping local kernel core because core file could not be opened prior to panic (mode : 0x%x, error : 0x%x)\n"
+ "skipping local kernel core because the SPTM is in INTERRUPTED state and can't support core dump generation\n"
+ "skipping local kernel core because the SPTM is in PANIC state and can't support core dump generation\n"
+ "stackshot_te_flags_mask"
+ "sugid_coredump"
+ "systemlog"
+ "user_dump_init"
+ "user_dump_save_seg_descriptions"
+ "user_dump_save_segment_data"
+ "user_dump_save_summary"
+ "v12@?0B8"
+ "v16@?0{exclaveindicatorcontroller_requesterror_s=Q}8"
+ "v32@?0{exclaveindicatorcontroller_motstate_s=QQQ}8"
+ "write to"
+ "xnu"
+ "xnu-"
- "%s: entitlement is not OSBoolean @%s:%d"
- "(u_int)off <= pbuf->pb_packet_len"
- "B16@?0^{task={lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}{os_refcnt=AI}BBBBIIQ^{_vm_map}{queue_entry=^{queue_entry}^{queue_entry}}^{task_watchports}^v{queue_entry=^{queue_entry}^{queue_entry}}^{restartable_ranges}^{processor_set}^{affinity_space}iIiiissiQ{recount_task=^{recount_track}^{recount_usage}}{lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}[4^{ipc_port}]^{ipc_port}[14{exception_action=^{ipc_port}iiii^{label}}]{hardened_exception_action={exception_action=^{ipc_port}iiii^{label}}II}^{ipc_port}^{ipc_port}^{ipc_port}^{ipc_port}^{ipc_port}[3^{ipc_port}]^^{ipc_port}^{ipc_space}^{ledger}{queue_entry=^{queue_entry}^{queue_entry}}iI^vQQCACQQQiBBB^Q^Q^Q^Q^Q^Q^Q^Q^QIIIIII^{proc_ro}^{kcdata_descriptor}Q{queue_entry=^{queue_entry}^{queue_entry}}^{label}IIQQIBBBBb4b4b4b4CCCCCB*^{vm_shared_region}QQQ^{thread_call}{queue_entry=^{queue_entry}^{queue_entry}}ii^{bank_task}^{ipc_importance_task}{vm_extmod_statistics=qqqqqq}{task_requested_policy=b1b1b2b2b1b1b2b1b3b3b3b1b5b3b3b1b3b1b1b3b1b3b1b1b17}{task_effective_policy=b1b1b2b1b1b1b2b1b1b3b3b1b1b1b4b1b1b1b3b3b1b1b29}{task_pend_token=(?={?=b1b1b1b1b1b1b1b1b1b1b1b1b1}I)}b1b1b1b1b1b27b1b1b1b1b28^{io_stat_info}{task_writes_counters=QQQQ}{task_writes_counters=QQQQ}{_cpu_time_qos_stats=QQQQQQQ}{_cpu_time_qos_stats=QQQQQQQ}IIQCCCiii{queue_entry=^{queue_entry}^{queue_entry}}{lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}b16b1b1b1b1b1b1b1[2^{coalition}][2{queue_entry=^{queue_entry}^{queue_entry}}]Q^vCCCCIQ{queue_entry=^{queue_entry}^{queue_entry}}{queue_entry=^{queue_entry}^{queue_entry}}iIQ[16C]Q^{_vmobject_list_output_}Q^{vm_deferred_reclamation_metadata_s}^v^vIQ}8"
- "IN_ARE_ADDR_EQUAL(&odst->natv4addr, &iph2->ip_src)"
- "IOVnodeGetBooleanEntitlement"
- "available"
- "hardened_heap=1"

```

>  `com.apple.security.sandbox`

```diff

-2401.102.1.0.0
+2401.120.9.0.0
   __TEXT.__os_log: 0x2092
-  __TEXT.__const: 0x1b36b1
+  __TEXT.__const: 0x1b65f1
   __TEXT.__cstring: 0x719d
   __TEXT_EXEC.__text: 0x315a4
   __TEXT_EXEC.__auth_stubs: 0x0

```

</details>

## MachO

### 🆕 NEW (9)

- `/System/Library/CoreServices/diagnosticservicesd`
- `/System/Library/ExtensionKit/Extensions/LighthouseAVShadowEval.appex/LighthouseAVShadowEval`
- `/System/Library/ExtensionKit/Extensions/MessageCenterApplicationServiceDiscoveryExtension.appex/MessageCenterApplicationServiceDiscoveryExtension`
- `/System/Library/ExtensionKit/Extensions/NeighborhoodActivityConduitIntentsExtension.appex/NeighborhoodActivityConduitIntentsExtension`
- `/System/Library/ExtensionKit/Extensions/PRIMLCKPreemptivePing.appex/PRIMLCKPreemptivePing`
- `/System/Library/ExtensionKit/Extensions/ZeoliteEvalExtension.appex/ZeoliteEvalExtension`
- `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/AirPlayDiagnosticExtension.appex/AirPlayDiagnosticExtension`
- `/System/Library/PrivateFrameworks/NeighborhoodActivityConduitIntents.framework/NeighborhoodActivityConduitIntents`
- `/usr/libexec/memoryanalyticsd`

### ❌ Removed (6)

- `/System/Library/ExtensionKit/Extensions/ConditionalEngineAppIntentsExtension.appex/ConditionalEngineAppIntentsExtension`
- `/System/Library/ExtensionKit/Extensions/ConditionalEngineLighthouseExtension.appex/ConditionalEngineLighthouseExtension`
- `/System/Library/ExtensionKit/Extensions/IEMetricsWorker.appex/IEMetricsWorker`
- `/System/Library/ExtensionKit/Extensions/ZeoliteExtension.appex/ZeoliteExtension`
- `/System/Library/Frameworks/VideoToolbox.framework/XPCServices/videodecodeservice.xpc/videodecodeservice`
- `/usr/libexec/fusiond`

### ⬆️ Updated (583)

<details>
  <summary><i>View Updated</i></summary>

- [/Applications/AMSEngagementViewService.app/AMSEngagementViewService](MACHOS/AMSEngagementViewService.md)
- [/Applications/AccessorySetupUI.app/AccessorySetupUI](MACHOS/AccessorySetupUI.md)
- [/Applications/ActivityMessagesApp.app/PlugIns/ActivityMessagesExtension.appex/ActivityMessagesExtension](MACHOS/ActivityMessagesExtension.md)
- [/Applications/ActivityProgressUI.app/ActivityProgressUI](MACHOS/ActivityProgressUI.md)
- [/Applications/AirDropUI.app/AirDropUI](MACHOS/AirDropUI.md)
- [/Applications/AskPermissionUI.app/AskPermissionUI](MACHOS/AskPermissionUI.md)
- [/Applications/BusinessExtensionsWrapper.app/PlugIns/Business.appex/Business](MACHOS/Business.md)
- [/Applications/CarCamera.app/CarCamera](MACHOS/CarCamera.md)
- [/Applications/ClarityCamera.app/ClarityCamera](MACHOS/ClarityCamera.md)
- [/Applications/Climate.app/Climate](MACHOS/Climate.md)
- [/Applications/ClockAngel.app/ClockAngel](MACHOS/ClockAngel.md)
- [/Applications/ColorPickerUIService.app/ColorPickerUIService](MACHOS/ColorPickerUIService.md)
- [/Applications/CompanionViewService.app/CompanionViewService](MACHOS/CompanionViewService.md)
- [/Applications/CoreAuthUI.app/CoreAuthUI](MACHOS/CoreAuthUI.md)
- [/Applications/Coverage Details.app/Coverage Details](MACHOS/Coverage_Details.md)
- [/Applications/Diagnostics.app/Diagnostics](MACHOS/Diagnostics.md)
- [/Applications/DiagnosticsReporter.app/DiagnosticsReporter](MACHOS/DiagnosticsReporter.md)
- [/Applications/DiagnosticsService.app/DiagnosticsService](MACHOS/DiagnosticsService.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4009.appex/Diagnostic-4009](MACHOS/Diagnostic-4009.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4153.appex/Diagnostic-4153](MACHOS/Diagnostic-4153.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6004.appex/Diagnostic-6004](MACHOS/Diagnostic-6004.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-7004.appex/Diagnostic-7004](MACHOS/Diagnostic-7004.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8079.appex/Diagnostic-8079](MACHOS/Diagnostic-8079.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8185.appex/Diagnostic-8185](MACHOS/Diagnostic-8185.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8246.appex/Diagnostic-8246](MACHOS/Diagnostic-8246.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8268.appex/Diagnostic-8268](MACHOS/Diagnostic-8268.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8340.appex/Diagnostic-8340](MACHOS/Diagnostic-8340.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8343.appex/Diagnostic-8343](MACHOS/Diagnostic-8343.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8389.appex/Diagnostic-8389](MACHOS/Diagnostic-8389.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9006.appex/Diagnostic-9006](MACHOS/Diagnostic-9006.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9008.appex/Diagnostic-9008](MACHOS/Diagnostic-9008.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9010.appex/Diagnostic-9010](MACHOS/Diagnostic-9010.md)
- [/Applications/DiagnosticsService.app/PlugIns/SystemReport-AirPods.appex/SystemReport-AirPods](MACHOS/SystemReport-AirPods.md)
- [/Applications/DiagnosticsService.app/PlugIns/SystemReport-BatteryCase.appex/SystemReport-BatteryCase](MACHOS/SystemReport-BatteryCase.md)
- [/Applications/DiagnosticsService.app/PlugIns/SystemReport.appex/SystemReport](MACHOS/SystemReport.md)
- [/Applications/EventViewService.app/EventViewService](MACHOS/EventViewService.md)
- [/Applications/FMDMagSafeSetupRemoteUI.app/FMDMagSafeSetupRemoteUI](MACHOS/FMDMagSafeSetupRemoteUI.md)
- [/Applications/FTMInternal-4.app/FTMInternal-4](MACHOS/FTMInternal-4.md)
- [/Applications/Family.app/PlugIns/InviteMessageBubbleExtension.appex/InviteMessageBubbleExtension](MACHOS/InviteMessageBubbleExtension.md)
- [/Applications/Feedback Assistant iOS.app/Feedback Assistant iOS](MACHOS/Feedback_Assistant_iOS.md)
- [/Applications/FindMyExtensionContainer.app/PlugIns/FMDMagSafeExtension.appex/FMDMagSafeExtension](MACHOS/FMDMagSafeExtension.md)
- [/Applications/FindMyExtensionContainer.app/PlugIns/FindMyDeviceBluetoothExtension.appex/FindMyDeviceBluetoothExtension](MACHOS/FindMyDeviceBluetoothExtension.md)
- [/Applications/FindMyRemoteUIService.app/FindMyRemoteUIService](MACHOS/FindMyRemoteUIService.md)
- [/Applications/GameCenterWidgets.app/PlugIns/GCWidgets.appex/GCWidgets](MACHOS/GCWidgets.md)
- [/Applications/GameOverlayUI.app/GameOverlayUI](MACHOS/GameOverlayUI.md)
- [/Applications/HDSViewService.app/HDSViewService](MACHOS/HDSViewService.md)
- [/Applications/HeadphoneProxService.app/HeadphoneProxService](MACHOS/HeadphoneProxService.md)
- [/Applications/HealthENLauncher.app/HealthENLauncher](MACHOS/HealthENLauncher.md)
- [/Applications/HomeCaptiveViewService.app/HomeCaptiveViewService](MACHOS/HomeCaptiveViewService.md)
- [/Applications/InCallService.app/InCallService](MACHOS/InCallService.md)
- [/Applications/MTLReplayer.app/Frameworks/MTLReplayController.framework/MTLReplayController](MACHOS/MTLReplayController.md)
- [/Applications/MagnifierAngel.app/MagnifierAngel](MACHOS/MagnifierAngel.md)
- [/Applications/Media.app/Media](MACHOS/Media.md)
- [/Applications/MediaRemoteUI.app/MediaRemoteUI](MACHOS/MediaRemoteUI.md)
- [/Applications/MobilePhone.app/MobilePhone](MACHOS/MobilePhone.md)
- [/Applications/MobilePhone.app/PlugIns/VoicemailMessageNotificationExtension.appex/VoicemailMessageNotificationExtension](MACHOS/VoicemailMessageNotificationExtension.md)
- [/Applications/MomentsUIService.app/MomentsUIService](MACHOS/MomentsUIService.md)
- [/Applications/MusicRecognition.app/MusicRecognition](MACHOS/MusicRecognition.md)
- [/Applications/PCViewService.app/PCViewService](MACHOS/PCViewService.md)
- [/Applications/PeopleMessageService.app/PlugIns/PeopleMessagesScreenTime.appex/PeopleMessagesScreenTime](MACHOS/PeopleMessagesScreenTime.md)
- [/Applications/PeopleViewService.app/PeopleViewService](MACHOS/PeopleViewService.md)
- [/Applications/PeopleViewService.app/PlugIns/PeopleWidget_iOSExtension.appex/PeopleWidget_iOSExtension](MACHOS/PeopleWidget_iOSExtension.md)
- [/Applications/Preferences.app/Preferences](MACHOS/Preferences.md)
- [/Applications/PreviewShell.app/PreviewShell](MACHOS/PreviewShell.md)
- [/Applications/SMS Filter.app/PlugIns/extensionFilter.appex/extensionFilter](MACHOS/extensionFilter.md)
- [/Applications/SOSBuddy.app/SOSBuddy](MACHOS/SOSBuddy.md)
- [/Applications/Screen Time.app/PlugIns/ScreenTimeWidgetExtension.appex/ScreenTimeWidgetExtension](MACHOS/ScreenTimeWidgetExtension.md)
- [/Applications/Setup.app/Setup](MACHOS/Setup.md)
- [/Applications/SharingViewService.app/SharingViewService](MACHOS/SharingViewService.md)
- [/Applications/ShazamEventsApp.app/ShazamEventsApp](MACHOS/ShazamEventsApp.md)
- [/Applications/Sidecar.app/PlugIns/ContinuityDisplay.appex/ContinuityDisplay](MACHOS/ContinuityDisplay.md)
- [/Applications/Siri.app/Siri](MACHOS/Siri.md)
- [/Applications/StickersUltra.app/PlugIns/StickersUltraExtension.appex/StickersUltraExtension](MACHOS/StickersUltraExtension.md)
- [/Applications/TDGSharingViewService.app/TDGSharingViewService](MACHOS/TDGSharingViewService.md)
- [/Applications/TVSetupUIService.app/TVSetupUIService](MACHOS/TVSetupUIService.md)
- [/Applications/Tamale.app/Tamale](MACHOS/Tamale.md)
- [/Applications/Trip.app/Trip](MACHOS/Trip.md)
- [/Applications/WritingToolsUIService.app/WritingToolsUIService](MACHOS/WritingToolsUIService.md)
- [/Library/Audio/Plug-Ins/HAL/VirtualAudio.plugin/VirtualAudio](MACHOS/VirtualAudio.md)
- [/System/Applications/Family/InviteMessageBubbleExtension.appex/InviteMessageBubbleExtension](MACHOS/InviteMessageBubbleExtension.md)
- [/System/DriverKit/usr/lib/system/libdispatch_debug.dylib](MACHOS/libdispatch_debug.dylib.md)
- [/System/DriverKit/usr/lib/system/libdispatch_profile.dylib](MACHOS/libdispatch_profile.dylib.md)
- [/System/DriverKit/usr/lib/system/libsystem_malloc_debug.dylib](MACHOS/libsystem_malloc_debug.dylib.md)
- [/System/DriverKit/usr/lib/system/libsystem_trace_debug.dylib](MACHOS/libsystem_trace_debug.dylib.md)
- [/System/ExclaveKit/usr/lib/dyld](MACHOS/dyld.md)
- [/System/ExclaveKit/usr/lib/system/libsystem_malloc_debug.dylib](MACHOS/libsystem_malloc_debug.dylib.md)
- [/System/Library/AccessibilityBundles/AXMotionCuesServer.axuiservice/AXMotionCuesServer](MACHOS/AXMotionCuesServer.md)
- [/System/Library/AccessibilityBundles/VoiceOver.axuiservice/VoiceOver](MACHOS/VoiceOver.md)
- [/System/Library/Accounts/ServiceOwners/AMSMediaServiceOwner.bundle/AMSMediaServiceOwner](MACHOS/AMSMediaServiceOwner.md)
- [/System/Library/AppleMediaServices/DynamicUI/PlugIns/CoreDynamicUIPlugin.bundle/CoreDynamicUIPlugin](MACHOS/CoreDynamicUIPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/AlarmFlowPlugin.bundle/AlarmFlowPlugin](MACHOS/AlarmFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/AudioFlowDelegatePlugin](MACHOS/AudioFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/CarCommandsFlowDelegatePlugin.bundle/CarCommandsFlowDelegatePlugin](MACHOS/CarCommandsFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/DailyBriefingFlowPlugin.bundle/DailyBriefingFlowPlugin](MACHOS/DailyBriefingFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/EmergencyFlowPlugin.bundle/EmergencyFlowPlugin](MACHOS/EmergencyFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/HealthFlowDelegatePlugin.bundle/HealthFlowDelegatePlugin](MACHOS/HealthFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/HomeCommunicationFlowDelegatePlugin.bundle/HomeCommunicationFlowDelegatePlugin](MACHOS/HomeCommunicationFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/IFFlowPlugin](MACHOS/IFFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/InformationFlowPlugin](MACHOS/InformationFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/PCSReadingFlowDelegatePlugin.bundle/PCSReadingFlowDelegatePlugin](MACHOS/PCSReadingFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/PhoneCallFlowDelegatePlugin](MACHOS/PhoneCallFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SettingsFlowDelegatePlugin.bundle/SettingsFlowDelegatePlugin](MACHOS/SettingsFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SiriLinkFlowPlugin.bundle/SiriLinkFlowPlugin](MACHOS/SiriLinkFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/SocialConversationFlowDelegatePlugin](MACHOS/SocialConversationFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/TimerFlowDelegatePlugin.bundle/TimerFlowDelegatePlugin](MACHOS/TimerFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/WellnessFlowPlugin](MACHOS/WellnessFlowPlugin.md)
- [/System/Library/Assistant/Plugins/Applications.assistantBundle/Applications](MACHOS/Applications.md)
- [/System/Library/Assistant/Plugins/PreferencesAssistant.assistantBundle/PreferencesAssistant](MACHOS/PreferencesAssistant.md)
- [/System/Library/Assistant/Plugins/activity.assistantBundle/activity](MACHOS/activity.md)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriPrivateLearningInferencePlugin.bundle/SiriPrivateLearningInferencePlugin](MACHOS/SiriPrivateLearningInferencePlugin.md)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriPrivateLearningPatternExtractionPlugin.bundle/SiriPrivateLearningPatternExtractionPlugin](MACHOS/SiriPrivateLearningPatternExtractionPlugin.md)
- [/System/Library/Audio/Plug-Ins/AVC/AVCHalogen.driver/AVCHalogen](MACHOS/AVCHalogen.md)
- [/System/Library/Audio/Plug-Ins/HAL/AirPlayHalogen.driver/AirPlayHalogen](MACHOS/AirPlayHalogen.md)
- [/System/Library/Audio/Plug-Ins/HAL/BTAudioHALPlugin.driver/BTAudioHALPlugin](MACHOS/BTAudioHALPlugin.md)
- [/System/Library/Audio/Plug-Ins/HAL/CarPlayHalogen.driver/CarPlayHalogen](MACHOS/CarPlayHalogen.md)
- [/System/Library/Audio/Plug-Ins/HAL/OctaviaHalogen.driver/OctaviaHalogen](MACHOS/OctaviaHalogen.md)
- [/System/Library/Audio/Plug-Ins/usbaudio.bundle/usbaudiod](MACHOS/usbaudiod.md)
- [/System/Library/CoreImage/CIInpainting.cifilter/CIInpainting](MACHOS/CIInpainting.md)
- [/System/Library/CoreServices/AccessibilityUIServer.app/PlugIns/AccessibilityControlsExtension.appex/AccessibilityControlsExtension](MACHOS/AccessibilityControlsExtension.md)
- [/System/Library/CoreServices/AssistiveTouch.app/assistivetouchd](MACHOS/assistivetouchd.md)
- [/System/Library/CoreServices/BluetoothUIService.app/BluetoothUIService](MACHOS/BluetoothUIService.md)
- [/System/Library/CoreServices/CarPlayTemplateUIHost.app/CarPlayTemplateUIHost](MACHOS/CarPlayTemplateUIHost.md)
- [/System/Library/CoreServices/ClarityBoard.app/ClarityBoard](MACHOS/ClarityBoard.md)
- [/System/Library/CoreServices/HangHUD.app/HangHUD](MACHOS/HangHUD.md)
- [/System/Library/CoreServices/IntelligentLight.app/IntelligentLight](MACHOS/IntelligentLight.md)
- [/System/Library/CoreServices/LiveTranscriptionUI.app/LiveTranscriptionUI](MACHOS/LiveTranscriptionUI.md)
- [/System/Library/CoreServices/ReportCrash](MACHOS/ReportCrash.md)
- [/System/Library/CoreServices/VoiceOverTouch.app/vot](MACHOS/vot.md)
- [/System/Library/CoreServices/osanalyticshelper](MACHOS/osanalyticshelper.md)
- [/System/Library/DataClassMigrators/BuddyMigrator.migrator/BuddyMigrator](MACHOS/BuddyMigrator.md)
- [/System/Library/DataClassMigrators/CookieDataMigrator.migrator/CookieDataMigrator](MACHOS/CookieDataMigrator.md)
- [/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN](MACHOS/com.apple.DriverKit-AppleBCMWLAN.md)
- [/System/Library/ExtensionKit/Extensions/AccessibilityControlsExtension.appex/AccessibilityControlsExtension](MACHOS/AccessibilityControlsExtension.md)
- [/System/Library/ExtensionKit/Extensions/AppStoreEvalLighthouseWorker.appex/AppStoreEvalLighthouseWorker](MACHOS/AppStoreEvalLighthouseWorker.md)
- [/System/Library/ExtensionKit/Extensions/AppleAccountIntents.appex/AppleAccountIntents](MACHOS/AppleAccountIntents.md)
- [/System/Library/ExtensionKit/Extensions/AssistantCoreFollowupExtension.appex/AssistantCoreFollowupExtension](MACHOS/AssistantCoreFollowupExtension.md)
- [/System/Library/ExtensionKit/Extensions/AssistantSettingsControlsExtension.appex/AssistantSettingsControlsExtension](MACHOS/AssistantSettingsControlsExtension.md)
- [/System/Library/ExtensionKit/Extensions/BiomeSELFIngestor.appex/BiomeSELFIngestor](MACHOS/BiomeSELFIngestor.md)
- [/System/Library/ExtensionKit/Extensions/DocumentAppIntents.appex/DocumentAppIntents](MACHOS/DocumentAppIntents.md)
- [/System/Library/ExtensionKit/Extensions/FamilyIntents.appex/FamilyIntents](MACHOS/FamilyIntents.md)
- [/System/Library/ExtensionKit/Extensions/FedStatsMLHostPlugin.appex/FedStatsMLHostPlugin](MACHOS/FedStatsMLHostPlugin.md)
- [/System/Library/ExtensionKit/Extensions/FedStatsMLHostPluginClassA.appex/FedStatsMLHostPluginClassA](MACHOS/FedStatsMLHostPluginClassA.md)
- [/System/Library/ExtensionKit/Extensions/FedStatsMLHostPluginClassB.appex/FedStatsMLHostPluginClassB](MACHOS/FedStatsMLHostPluginClassB.md)
- [/System/Library/ExtensionKit/Extensions/FindMyIntentsExtension.appex/FindMyIntentsExtension](MACHOS/FindMyIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/GMSSELFIngestor.appex/GMSSELFIngestor](MACHOS/GMSSELFIngestor.md)
- [/System/Library/ExtensionKit/Extensions/GenerativeAssistantExtension.appex/GenerativeAssistantExtension](MACHOS/GenerativeAssistantExtension.md)
- [/System/Library/ExtensionKit/Extensions/GenerativeAssistantSettingsExtension.appex/GenerativeAssistantSettingsExtension](MACHOS/GenerativeAssistantSettingsExtension.md)
- [/System/Library/ExtensionKit/Extensions/LighthouseAVExtension.appex/LighthouseAVExtension](MACHOS/LighthouseAVExtension.md)
- [/System/Library/ExtensionKit/Extensions/MercuryPosterExtension.appex/MercuryPosterExtension](MACHOS/MercuryPosterExtension.md)
- [/System/Library/ExtensionKit/Extensions/MusicEngagementExtension.appex/MusicEngagementExtension](MACHOS/MusicEngagementExtension.md)
- [/System/Library/ExtensionKit/Extensions/NewDeviceOutreachIntents_iOS.appex/NewDeviceOutreachIntents_iOS](MACHOS/NewDeviceOutreachIntents_iOS.md)
- [/System/Library/ExtensionKit/Extensions/ODDIPoirotMetricsExtension.appex/ODDIPoirotMetricsExtension](MACHOS/ODDIPoirotMetricsExtension.md)
- [/System/Library/ExtensionKit/Extensions/PridePosterExtension.appex/PridePosterExtension](MACHOS/PridePosterExtension.md)
- [/System/Library/ExtensionKit/Extensions/PrivateEvolutionPlugin.appex/PrivateEvolutionPlugin](MACHOS/PrivateEvolutionPlugin.md)
- [/System/Library/ExtensionKit/Extensions/ProductPageExtension.appex/ProductPageExtension](MACHOS/ProductPageExtension.md)
- [/System/Library/ExtensionKit/Extensions/RepackagingWorker.appex/RepackagingWorker](MACHOS/RepackagingWorker.md)
- [/System/Library/ExtensionKit/Extensions/SafariAssistantWorker.appex/SafariAssistantWorker](MACHOS/SafariAssistantWorker.md)
- [/System/Library/ExtensionKit/Extensions/ScreenTimeAppIntentsExtension.appex/ScreenTimeAppIntentsExtension](MACHOS/ScreenTimeAppIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/SubscribePageExtension.appex/SubscribePageExtension](MACHOS/SubscribePageExtension.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.fskit.apfs.appex/com.apple.fskit.apfs](MACHOS/com.apple.fskit.apfs.md)
- [/System/Library/Extensions/AppleSPURose.kext/PlugIns/RoseControllerLib.plugin/RoseControllerLib](MACHOS/RoseControllerLib.md)
- [/System/Library/Filesystems/apfs.fs/apfs_condenser](MACHOS/apfs_condenser.md)
- [/System/Library/Filesystems/apfs.fs/apfs_vol_converter](MACHOS/apfs_vol_converter.md)
- [/System/Library/Filesystems/apfs.fs/fsck_apfs](MACHOS/fsck_apfs.md)
- [/System/Library/Filesystems/apfs.fs/newfs_apfs](MACHOS/newfs_apfs.md)
- [/System/Library/Frameworks/AutomatedDeviceEnrollment.framework/PlugIns/AddDevicesToAutomatedDeviceEnrollmentExtension.appex/AddDevicesToAutomatedDeviceEnrollmentExtension](MACHOS/AddDevicesToAutomatedDeviceEnrollmentExtension.md)
- [/System/Library/Frameworks/CFNetwork.framework/AuthBrokerAgent](MACHOS/AuthBrokerAgent.md)
- [/System/Library/Frameworks/CallKit.framework/XPCServices/com.apple.CallKit.CallDirectory.xpc/com.apple.CallKit.CallDirectory](MACHOS/com.apple.CallKit.CallDirectory.md)
- [/System/Library/Frameworks/Contacts.framework/Support/contactsd](MACHOS/contactsd.md)
- [/System/Library/Frameworks/ContactsUI.framework/PlugIns/MonogramPosterExtension.appex/MonogramPosterExtension](MACHOS/MonogramPosterExtension.md)
- [/System/Library/Frameworks/ContactsUI.framework/XPCServices/ContactsButtonXPCService.xpc/ContactsButtonXPCService](MACHOS/ContactsButtonXPCService.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/spotlightknowledged](MACHOS/spotlightknowledged.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenterMobileHelper](MACHOS/CommCenterMobileHelper.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenterRootHelper](MACHOS/CommCenterRootHelper.md)
- [/System/Library/Frameworks/FamilyControls.framework/PlugIns/ActivityPickerExtension.appex/ActivityPickerExtension](MACHOS/ActivityPickerExtension.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismPlugins/MechTouchId.bundle/MechTouchId](MACHOS/MechTouchId.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/ModulePlugins/ModuleACM.bundle/ModuleACM](MACHOS/ModuleACM.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/coreauthd](MACHOS/coreauthd.md)
- [/System/Library/Frameworks/ManagedSettings.framework/ManagedSettingsAgent](MACHOS/ManagedSettingsAgent.md)
- [/System/Library/Frameworks/ScreenTime.framework/PlugIns/ScreenTimeWebExtension.appex/ScreenTimeWebExtension](MACHOS/ScreenTimeWebExtension.md)
- [/System/Library/Frameworks/Security.framework/XPCServices/TrustedPeersHelper.xpc/TrustedPeersHelper](MACHOS/TrustedPeersHelper.md)
- [/System/Library/Frameworks/StoreKit.framework/Support/storekitd](MACHOS/storekitd.md)
- [/System/Library/Frameworks/UIKit.framework/PlugIns/com.apple.UIKit.ColorPicker.appex/com.apple.UIKit.ColorPicker](MACHOS/com.apple.UIKit.ColorPicker.md)
- [/System/Library/Frameworks/WeatherKit.framework/XPCServices/com.apple.weatherkit.authservice.xpc/com.apple.weatherkit.authservice](MACHOS/com.apple.weatherkit.authservice.md)
- [/System/Library/HIDPlugins/ColourSensorFilterPlugin.plugin/ColourSensorFilterPlugin](MACHOS/ColourSensorFilterPlugin.md)
- [/System/Library/HIDPlugins/ServiceFilters/AppleProxServiceFilter.plugin/AppleProxServiceFilter](MACHOS/AppleProxServiceFilter.md)
- [/System/Library/HIDPlugins/ServiceFilters/IOHIDSensorPowerLoggingFilter.plugin/IOHIDSensorPowerLoggingFilter](MACHOS/IOHIDSensorPowerLoggingFilter.md)
- [/System/Library/HIDPlugins/SessionFilters/FTRemoteEventHIDSessionFilter.plugin/FTRemoteEventHIDSessionFilter](MACHOS/FTRemoteEventHIDSessionFilter.md)
- [/System/Library/HIDPlugins/SessionFilters/IOHIDMotionEventSessionFilter.plugin/IOHIDMotionEventSessionFilter](MACHOS/IOHIDMotionEventSessionFilter.md)
- [/System/Library/HIDPlugins/SessionFilters/TactSwitchHIDSessionFilter.plugin/TactSwitchHIDSessionFilter](MACHOS/TactSwitchHIDSessionFilter.md)
- [/System/Library/Health/Plugins/HealthRecordsPlugin.bundle/HealthRecordsPlugin](MACHOS/HealthRecordsPlugin.md)
- [/System/Library/Messages/PlugIns/RCS.imservice/RCS](MACHOS/RCS.md)
- [/System/Library/Messages/PlugIns/iMessage.imservice/iMessage](MACHOS/iMessage.md)
- [/System/Library/Messages/iMessageBalloons/ASMessagesProvider.bundle/ASMessagesProvider](MACHOS/ASMessagesProvider.md)
- [/System/Library/Messages/iMessageBalloons/DigitalTouchBalloonProvider.bundle/DigitalTouchBalloonProvider](MACHOS/DigitalTouchBalloonProvider.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/ActivityBridgeSetup.bundle/ActivityBridgeSetup](MACHOS/ActivityBridgeSetup.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/DepthComplicationBundleCompanion.bundle/DepthComplicationBundleCompanion](MACHOS/DepthComplicationBundleCompanion.md)
- [/System/Library/PreferenceBundles/AccessibilitySettings.bundle/AccessibilitySettings](MACHOS/AccessibilitySettings.md)
- [/System/Library/PreferenceBundles/AccountSettings/AppleAccountSettings.bundle/AppleAccountSettings](MACHOS/AppleAccountSettings.md)
- [/System/Library/PreferenceBundles/AccountSettings/icloudMailSettings.bundle/icloudMailSettings](MACHOS/icloudMailSettings.md)
- [/System/Library/PreferenceBundles/AdAttributionKitDeveloperSettings.bundle/AdAttributionKitDeveloperSettings](MACHOS/AdAttributionKitDeveloperSettings.md)
- [/System/Library/PreferenceBundles/AppClipDeveloperSettings.bundle/AppClipDeveloperSettings](MACHOS/AppClipDeveloperSettings.md)
- [/System/Library/PreferenceBundles/GameControlleriOSSettings.bundle/GameControlleriOSSettings](MACHOS/GameControlleriOSSettings.md)
- [/System/Library/PreferenceBundles/InternationalSettings.bundle/InternationalSettings](MACHOS/InternationalSettings.md)
- [/System/Library/PreferenceBundles/JournalSettings.bundle/JournalSettings](MACHOS/JournalSettings.md)
- [/System/Library/PreferenceBundles/MobileSafariSettings.bundle/MobileSafariSettings](MACHOS/MobileSafariSettings.md)
- [/System/Library/PreferenceBundles/MultitaskingAndGesturesSettings.bundle/MultitaskingAndGesturesSettings](MACHOS/MultitaskingAndGesturesSettings.md)
- [/System/Library/PreferenceBundles/PodcastsSettingsPlugin.bundle/PodcastsSettingsPlugin](MACHOS/PodcastsSettingsPlugin.md)
- [/System/Library/PreferenceBundles/PrivacyAndSecuritySettings.bundle/PrivacyAndSecuritySettings](MACHOS/PrivacyAndSecuritySettings.md)
- [/System/Library/PreferenceBundles/ScreenTimeSettings.bundle/ScreenTimeSettings](MACHOS/ScreenTimeSettings.md)
- [/System/Library/PreferenceBundles/StorageSettingsUI.bundle/StorageSettingsUI](MACHOS/StorageSettingsUI.md)
- [/System/Library/PreferenceBundles/WallpaperSettings.bundle/WallpaperSettings](MACHOS/WallpaperSettings.md)
- [/System/Library/PreferencesSyncBundles/FindMyDevicePreferencesSync.bundle/FindMyDevicePreferencesSync](MACHOS/FindMyDevicePreferencesSync.md)
- [/System/Library/PrivateFrameworks/ABMHelper.framework/Support/abm-helper](MACHOS/abm-helper.md)
- [/System/Library/PrivateFrameworks/ASOctaneSupport.framework/XPCServices/ASOctaneSupportXPCService.xpc/ASOctaneSupportXPCService](MACHOS/ASOctaneSupportXPCService.md)
- [/System/Library/PrivateFrameworks/AppSSO.framework/Support/AppSSODaemon](MACHOS/AppSSODaemon.md)
- [/System/Library/PrivateFrameworks/AppStoreComponents.framework/Support/appstorecomponentsd](MACHOS/appstorecomponentsd.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored](MACHOS/appstored.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/amsaccountsd](MACHOS/amsaccountsd.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/Extensions/UtilityExtension.appex/UtilityExtension](MACHOS/UtilityExtension.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/amsengagementd](MACHOS/amsengagementd.md)
- [/System/Library/PrivateFrameworks/AssetCacheServices.framework/XPCServices/AssetCacheLocatorService.xpc/AssetCacheLocatorService](MACHOS/AssetCacheLocatorService.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd](MACHOS/assistantd.md)
- [/System/Library/PrivateFrameworks/AuthKit.framework/akd](MACHOS/akd.md)
- [/System/Library/PrivateFrameworks/BookDataStore.framework/Support/bookdatastored](MACHOS/bookdatastored.md)
- [/System/Library/PrivateFrameworks/CMCapture.framework/PlugIns/CMCaptureDiagnosticExtension.appex/CMCaptureDiagnosticExtension](MACHOS/CMCaptureDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/CacheDelete.framework/deleted](MACHOS/deleted.md)
- [/System/Library/PrivateFrameworks/CacheDelete.framework/deleted_helper](MACHOS/deleted_helper.md)
- [/System/Library/PrivateFrameworks/CallHistory.framework/Support/CallHistorySyncHelper](MACHOS/CallHistorySyncHelper.md)
- [/System/Library/PrivateFrameworks/CloudDocsUI.framework/PlugIns/com.apple.CloudDocsUI.CloudSharing.appex/com.apple.CloudDocsUI.CloudSharing](MACHOS/com.apple.CloudDocsUI.CloudSharing.md)
- [/System/Library/PrivateFrameworks/CloudSharing.framework/XPCServices/SPIHelper-iOS.xpc/SPIHelper-iOS](MACHOS/SPIHelper-iOS.md)
- [/System/Library/PrivateFrameworks/CloudSharingUI.framework/PlugIns/com.apple.CloudSharingUI.CloudSharing.appex/com.apple.CloudSharingUI.CloudSharing](MACHOS/com.apple.CloudSharingUI.CloudSharing.md)
- [/System/Library/PrivateFrameworks/CloudTelemetry.framework/XPCServices/CloudTelemetryService.xpc/CloudTelemetryService](MACHOS/CloudTelemetryService.md)
- [/System/Library/PrivateFrameworks/CommunicationsFilter.framework/CMFSyncAgent](MACHOS/CMFSyncAgent.md)
- [/System/Library/PrivateFrameworks/CoreAccessories.framework/Support/accessoryd](MACHOS/accessoryd.md)
- [/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsd](MACHOS/analyticsd.md)
- [/System/Library/PrivateFrameworks/CoreDuetContext.framework/Resources/contextstored](MACHOS/contextstored.md)
- [/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/XPCServices/com.apple.siri.embeddedspeech.xpc/com.apple.siri.embeddedspeech](MACHOS/com.apple.siri.embeddedspeech.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/parsec-fbf](MACHOS/parsec-fbf.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/parsecd](MACHOS/parsecd.md)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd](MACHOS/corespeechd.md)
- [/System/Library/PrivateFrameworks/CoreSymbolication.framework/coresymbolicationd](MACHOS/coresymbolicationd.md)
- [/System/Library/PrivateFrameworks/CoreThreadCommissionerService.framework/CoreThreadCommissionerServiced](MACHOS/CoreThreadCommissionerServiced.md)
- [/System/Library/PrivateFrameworks/CoreThreadRadio.framework/threadradiod](MACHOS/threadradiod.md)
- [/System/Library/PrivateFrameworks/DeviceCheckInternal.framework/devicecheckd](MACHOS/devicecheckd.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Cellular.appex/com.apple.DiagnosticExtensions.Cellular](MACHOS/com.apple.DiagnosticExtensions.Cellular.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Microstackshot.appex/com.apple.DiagnosticExtensions.Microstackshot](MACHOS/com.apple.DiagnosticExtensions.Microstackshot.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Telephony.appex/com.apple.DiagnosticExtensions.Telephony](MACHOS/com.apple.DiagnosticExtensions.Telephony.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.sysdiagnose.appex/com.apple.DiagnosticExtensions.sysdiagnose](MACHOS/com.apple.DiagnosticExtensions.sysdiagnose.md)
- [/System/Library/PrivateFrameworks/DiagnosticsSessionAvailability.framework/XPCServices/DiagnosticsSessionAvailabilityService.xpc/DiagnosticsSessionAvailabilityService](MACHOS/DiagnosticsSessionAvailabilityService.md)
- [/System/Library/PrivateFrameworks/DialogEngine.framework/catutil](MACHOS/catutil.md)
- [/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/XPCServices/DPSubmissionService.xpc/DPSubmissionService](MACHOS/DPSubmissionService.md)
- [/System/Library/PrivateFrameworks/DiskImages2.framework/XPCServices/diskimagescontroller.xpc/diskimagescontroller](MACHOS/diskimagescontroller.md)
- [/System/Library/PrivateFrameworks/DiskSpaceDiagnostics.framework/XPCServices/FilesystemMetadataSnapshotService.xpc/FilesystemMetadataSnapshotService](MACHOS/FilesystemMetadataSnapshotService.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAppPopover.appex/RecentsAppPopover](MACHOS/RecentsAppPopover.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAvocado.appex/RecentsAvocado](MACHOS/RecentsAvocado.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/SaveToFiles.appex/SaveToFiles](MACHOS/SaveToFiles.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/com.apple.DocumentManager.Service.appex/com.apple.DocumentManager.Service](MACHOS/com.apple.DocumentManager.Service.md)
- [/System/Library/PrivateFrameworks/EcosystemAnalytics.framework/Support/ecosystemanalyticsd](MACHOS/ecosystemanalyticsd.md)
- [/System/Library/PrivateFrameworks/EmailDaemon.framework/maild](MACHOS/maild.md)
- [/System/Library/PrivateFrameworks/EyeRelief.framework/Resources/eyereliefd](MACHOS/eyereliefd.md)
- [/System/Library/PrivateFrameworks/FamilyCircle.framework/familycircled](MACHOS/familycircled.md)
- [/System/Library/PrivateFrameworks/FileProviderDaemon.framework/PlugIns/FileProviderDiagnosticExtension.appex/FileProviderDiagnosticExtension](MACHOS/FileProviderDiagnosticExtension.md)
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
- [/System/Library/PrivateFrameworks/GeoAnalytics.framework/geoanalyticsd](MACHOS/geoanalyticsd.md)
- [/System/Library/PrivateFrameworks/GeoServices.framework/geod](MACHOS/geod.md)
- [/System/Library/PrivateFrameworks/HangTracer.framework/PlugIns/HangLogsDiagnosticExtension.appex/HangLogsDiagnosticExtension](MACHOS/HangLogsDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/HangTracer.framework/PlugIns/PerformanceLoggingDiagnosticExtension.appex/PerformanceLoggingDiagnosticExtension](MACHOS/PerformanceLoggingDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/HealthAlgorithms.framework/XPCServices/DayStreamProcessorService.xpc/DayStreamProcessorService](MACHOS/DayStreamProcessorService.md)
- [/System/Library/PrivateFrameworks/HealthPluginHost.framework/healthappd](MACHOS/healthappd.md)
- [/System/Library/PrivateFrameworks/HomePlatformSettingsUI.framework/PlugIns/HPSUIViewService.appex/HPSUIViewService](MACHOS/HPSUIViewService.md)
- [/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd](MACHOS/identityservicesd.md)
- [/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/imagent](MACHOS/imagent.md)
- [/System/Library/PrivateFrameworks/IPConfiguration.framework/XPCServices/IPConfigurationHelper.xpc/IPConfigurationHelper](MACHOS/IPConfigurationHelper.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/PlugIns/IntelligenceFlowDiagnostics.appex/IntelligenceFlowDiagnostics](MACHOS/IntelligenceFlowDiagnostics.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/intelligenceflowd](MACHOS/intelligenceflowd.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatform.framework/PlugIns/DiagnosticExtension.appex/DiagnosticExtension](MACHOS/DiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCompute.framework/XPCServices/IntelligencePlatformComputeService.xpc/IntelligencePlatformComputeService](MACHOS/IntelligencePlatformComputeService.md)
- [/System/Library/PrivateFrameworks/LockdownMode.framework/lockdownmoded](MACHOS/lockdownmoded.md)
- [/System/Library/PrivateFrameworks/MLKit.framework/PlugIns/com.apple.MLKit.MLModelPreview.appex/com.apple.MLKit.MLModelPreview](MACHOS/com.apple.MLKit.MLModelPreview.md)
- [/System/Library/PrivateFrameworks/MLKit.framework/PlugIns/com.apple.MLKit.MLPackagePreview.appex/com.apple.MLKit.MLPackagePreview](MACHOS/com.apple.MLKit.MLPackagePreview.md)
- [/System/Library/PrivateFrameworks/MapsSupport.framework/mapspushd](MACHOS/mapspushd.md)
- [/System/Library/PrivateFrameworks/MapsSupport.framework/navd](MACHOS/navd.md)
- [/System/Library/PrivateFrameworks/MediaRemote.framework/Support/mediaremoted](MACHOS/mediaremoted.md)
- [/System/Library/PrivateFrameworks/MediaServicesBroker.framework/PlugIns/MediaSetupViewService.appex/MediaSetupViewService](MACHOS/MediaSetupViewService.md)
- [/System/Library/PrivateFrameworks/Message.framework/XPCServices/SearchIndexer.xpc/SearchIndexer](MACHOS/SearchIndexer.md)
- [/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/XPCServices/MessagesBlastDoorService.xpc/MessagesBlastDoorService](MACHOS/MessagesBlastDoorService.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/Support/accessoryupdaterd](MACHOS/accessoryupdaterd.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/Accessory Updater Service.xpc/Accessory Updater Service](MACHOS/Accessory_Updater_Service.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/EAUpdaterService.xpc/EAUpdaterService](MACHOS/EAUpdaterService.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceLegacyAudio.xpc/UARPUpdaterServiceLegacyAudio](MACHOS/UARPUpdaterServiceLegacyAudio.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/backupd](MACHOS/backupd.md)
- [/System/Library/PrivateFrameworks/MusicLibrary.framework/Support/medialibraryd](MACHOS/medialibraryd.md)
- [/System/Library/PrivateFrameworks/NeighborhoodActivityConduit.framework/XPCServices/com.apple.NeighborhoodActivityConduitService.xpc/com.apple.NeighborhoodActivityConduitService](MACHOS/com.apple.NeighborhoodActivityConduitService.md)
- [/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/PlugIns/NewDeviceOutreachExtension.appex/NewDeviceOutreachExtension](MACHOS/NewDeviceOutreachExtension.md)
- [/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/ndoagent](MACHOS/ndoagent.md)
- [/System/Library/PrivateFrameworks/OnDeviceStorage.framework/Support/amsondevicestoraged](MACHOS/amsondevicestoraged.md)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/passd](MACHOS/passd.md)
- [/System/Library/PrivateFrameworks/People.framework/peopled](MACHOS/peopled.md)
- [/System/Library/PrivateFrameworks/PersonalizedSensing.framework/XPCServices/PersonalizedSensingService.xpc/PersonalizedSensingService](MACHOS/PersonalizedSensingService.md)
- [/System/Library/PrivateFrameworks/PlugInKitDaemon.framework/PlugInKitDaemon](MACHOS/PlugInKitDaemon.md)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/PlugIns/DEPowerlogEPL.appex/DEPowerlogEPL](MACHOS/DEPowerlogEPL.md)
- [/System/Library/PrivateFrameworks/PreviewsOSSupport.framework/Support/previewsd](MACHOS/previewsd.md)
- [/System/Library/PrivateFrameworks/PrivacyAccounting.framework/Versions/A/Resources/privacyaccountingd](MACHOS/privacyaccountingd.md)
- [/System/Library/PrivateFrameworks/PrivateCloudCompute.framework/privatecloudcomputed.app/privatecloudcomputed](MACHOS/privatecloudcomputed.md)
- [/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeAgent](MACHOS/ScreenTimeAgent.md)
- [/System/Library/PrivateFrameworks/ScreenTimeUI.framework/PlugIns/ScreenTimeNotificationContentExtension.appex/ScreenTimeNotificationContentExtension](MACHOS/ScreenTimeNotificationContentExtension.md)
- [/System/Library/PrivateFrameworks/Search.framework/PlugIns/SpotlightDiagnostic.appex/SpotlightDiagnostic](MACHOS/SpotlightDiagnostic.md)
- [/System/Library/PrivateFrameworks/Search.framework/searchd](MACHOS/searchd.md)
- [/System/Library/PrivateFrameworks/SiriAppLaunchIntents.framework/PlugIns/AppLaunchIntentExtension.appex/AppLaunchIntentExtension](MACHOS/AppLaunchIntentExtension.md)
- [/System/Library/PrivateFrameworks/SiriTTSService.framework/sirittsd](MACHOS/sirittsd.md)
- [/System/Library/PrivateFrameworks/SiriVOX.framework/SiriHeadlessService](MACHOS/SiriHeadlessService.md)
- [/System/Library/PrivateFrameworks/SiriVideoIntents.framework/PlugIns/VideoIntentExtension.appex/VideoIntentExtension](MACHOS/VideoIntentExtension.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateServicesUI.framework/Plugins/SoftwareUpdateServicesUIPlugin.servicebundle/SoftwareUpdateServicesUIPlugin](MACHOS/SoftwareUpdateServicesUIPlugin.md)
- [/System/Library/PrivateFrameworks/SonicKit.framework/PlugIns/SonicDiagnostics.appex/SonicDiagnostics](MACHOS/SonicDiagnostics.md)
- [/System/Library/PrivateFrameworks/SpaceAttribution.framework/spaceattributiond](MACHOS/spaceattributiond.md)
- [/System/Library/PrivateFrameworks/SystemStatusServer.framework/Support/systemstatusd](MACHOS/systemstatusd.md)
- [/System/Library/PrivateFrameworks/TCC.framework/Support/tccd](MACHOS/tccd.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd](MACHOS/callservicesd.md)
- [/System/Library/PrivateFrameworks/TranslationUIServices.framework/PlugIns/TranslationUIService.appex/TranslationUIService](MACHOS/TranslationUIService.md)
- [/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTrackingAgent](MACHOS/UsageTrackingAgent.md)
- [/System/Library/PrivateFrameworks/UserActivity.framework/Agents/useractivityd](MACHOS/useractivityd.md)
- [/System/Library/PrivateFrameworks/VideosUI.framework/PlugIns/TVProductPageExtension.appex/TVProductPageExtension](MACHOS/TVProductPageExtension.md)
- [/System/Library/PrivateFrameworks/VisualVoicemail.framework/vmd](MACHOS/vmd.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/ExtragalacticPoster.appex/ExtragalacticPoster](MACHOS/ExtragalacticPoster.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/RhizomePoster.appex/RhizomePoster](MACHOS/RhizomePoster.md)
- [/System/Library/PrivateFrameworks/WatchListKit.framework/Support/watchlistd](MACHOS/watchlistd.md)
- [/System/Library/PrivateFrameworks/WiFiPolicy.framework/XPCServices/WiFiCloudAssetsXPCService.xpc/WiFiCloudAssetsXPCService](MACHOS/WiFiCloudAssetsXPCService.md)
- [/System/Library/PrivateFrameworks/WirelessInsights.framework/Support/wirelessinsightsd](MACHOS/wirelessinsightsd.md)
- [/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/BackgroundShortcutRunner.xpc/BackgroundShortcutRunner](MACHOS/BackgroundShortcutRunner.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/SystemActionConfigurationExtension.appex/SystemActionConfigurationExtension](MACHOS/SystemActionConfigurationExtension.md)
- [/System/Library/PrivateFrameworks/iCloudNotification.framework/ind](MACHOS/ind.md)
- [/System/Library/PrivateFrameworks/iOSDiagnostics.framework/XPCServices/com.apple.DiagnosticsSessionAvailibility.xpc/com.apple.DiagnosticsSessionAvailibility](MACHOS/com.apple.DiagnosticsSessionAvailibility.md)
- [/System/Library/PrivateFrameworks/iOSDiagnostics.framework/iosdiagnosticsd](MACHOS/iosdiagnosticsd.md)
- [/System/Library/PrivateFrameworks/iTunesCloud.framework/Support/itunescloudd](MACHOS/itunescloudd.md)
- [/System/Library/PrivateFrameworks/iTunesStore.framework/Support/itunesstored](MACHOS/itunesstored.md)
- [/System/Library/ScreenReader/BrailleTables/Rhine.brailletable/Rhine](MACHOS/Rhine.md)
- [/System/Library/Settings/InstalledApps.settings/InstalledApps](MACHOS/InstalledApps.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/AudioSuggestionsPlugin.bundle/AudioSuggestionsPlugin](MACHOS/AudioSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/HomeAutomationSiriSuggestions.bundle/HomeAutomationSiriSuggestions](MACHOS/HomeAutomationSiriSuggestions.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriLinkSuggestionsPlugin.bundle/SiriLinkSuggestionsPlugin](MACHOS/SiriLinkSuggestionsPlugin.md)
- [/System/Library/Snippets/UIPlugins/AudioUIPlugin.bundle/AudioUIPlugin](MACHOS/AudioUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/PhoneUIPlugin.bundle/PhoneUIPlugin](MACHOS/PhoneUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/ResponseGenerationUIPlugin.bundle/ResponseGenerationUIPlugin](MACHOS/ResponseGenerationUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SearchToolUIPlugin.bundle/SearchToolUIPlugin](MACHOS/SearchToolUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SiriInformationUIPlugin.bundle/SiriInformationUIPlugin](MACHOS/SiriInformationUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SystemPlugin.bundle/SystemPlugin](MACHOS/SystemPlugin.md)
- [/System/Library/SystemConfiguration/EAPOLController.bundle/EAPOLController](MACHOS/EAPOLController.md)
- [/System/Library/SystemConfiguration/EAPOLController.bundle/eapolclient](MACHOS/eapolclient.md)
- [/System/Library/SystemConfiguration/IPConfiguration.bundle/IPConfiguration](MACHOS/IPConfiguration.md)
- [/System/Library/UserEventPlugins/MemoryMonitor.plugin/MemoryMonitor](MACHOS/MemoryMonitor.md)
- [/System/Library/UserEventPlugins/PerfPowerServicesEventListenerPlugin.plugin/PerfPowerServicesEventListenerPlugin](MACHOS/PerfPowerServicesEventListenerPlugin.md)
- [/System/Library/UserEventPlugins/com.apple.BackgroundTaskAgentPlugin.plugin/com.apple.BackgroundTaskAgentPlugin](MACHOS/com.apple.BackgroundTaskAgentPlugin.md)
- [/System/Library/UserEventPlugins/com.apple.cts.plugin/com.apple.cts](MACHOS/com.apple.cts.md)
- [/System/Library/UserEventPlugins/com.apple.fsevents.matching.plugin/com.apple.fsevents.matching](MACHOS/com.apple.fsevents.matching.md)
- [/System/Library/UserEventPlugins/com.apple.netsvcproxy.plugin/com.apple.netsvcproxy](MACHOS/com.apple.netsvcproxy.md)
- [/System/Library/UserEventPlugins/com.apple.nsurlsessiond.plugin/com.apple.nsurlsessiond](MACHOS/com.apple.nsurlsessiond.md)
- [/System/Library/UserEventPlugins/com.apple.telemetry.plugin/com.apple.telemetry](MACHOS/com.apple.telemetry.md)
- [/System/Library/VideoProcessors/ColourConstancyV1.bundle/ColourConstancyV1](MACHOS/ColourConstancyV1.md)
- [/System/Library/VideoProcessors/SemanticStyleV1.bundle/SemanticStyleV1](MACHOS/SemanticStyleV1.md)
- [/System/Library/VideoProcessors/SmartStyleV1.bundle/SmartStyleV1](MACHOS/SmartStyleV1.md)
- [/System/Library/VideoProcessors/SuperResolutionV2.bundle/SuperResolutionV2](MACHOS/SuperResolutionV2.md)
- [/System/Library/VideoProcessors/VideoDeghostingV1.bundle/VideoDeghostingV1](MACHOS/VideoDeghostingV1.md)
- [/System/Library/VideoProcessors/VideoDeghostingV2.bundle/VideoDeghostingV2](MACHOS/VideoDeghostingV2.md)
- [/System/Library/VideoProcessors/VideoStabilizationV2.bundle/VideoStabilizationV2](MACHOS/VideoStabilizationV2.md)
- [/private/var/staged_system_apps/AppStore.app/AppStore](MACHOS/AppStore.md)
- [/private/var/staged_system_apps/AppleTV.app/PlugIns/TVWidgetExtension.appex/TVWidgetExtension](MACHOS/TVWidgetExtension.md)
- [/private/var/staged_system_apps/AppleVisionProApp.app/AppleVisionProApp](MACHOS/AppleVisionProApp.md)
- [/private/var/staged_system_apps/Books.app/Books](MACHOS/Books.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/AEBookPlugins.framework/AEBookPlugins](MACHOS/AEBookPlugins.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BlissReader.framework/BlissReader](MACHOS/BlissReader.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookAnalytics.framework/BookAnalytics](MACHOS/BookAnalytics.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookEPUB.framework/BookEPUB](MACHOS/BookEPUB.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookStoreUI.framework/BookStoreUI](MACHOS/BookStoreUI.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BooksPersonalization.framework/BooksPersonalization](MACHOS/BooksPersonalization.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BooksUI.framework/BooksUI](MACHOS/BooksUI.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/JSApp.framework/JSApp](MACHOS/JSApp.md)
- [/private/var/staged_system_apps/Books.app/PlugIns/BooksWidgetExtension.appex/BooksWidgetExtension](MACHOS/BooksWidgetExtension.md)
- [/private/var/staged_system_apps/Bridge.app/Bridge](MACHOS/Bridge.md)
- [/private/var/staged_system_apps/Calculator.app/Calculator](MACHOS/Calculator.md)
- [/private/var/staged_system_apps/Files.app/Files](MACHOS/Files.md)
- [/private/var/staged_system_apps/FindMy.app/FindMy](MACHOS/FindMy.md)
- [/private/var/staged_system_apps/FindMy.app/Frameworks/FindMyAppCore.framework/FindMyAppCore](MACHOS/FindMyAppCore.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyNotificationsService.appex/FindMyNotificationsService](MACHOS/FindMyNotificationsService.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyWidgetItems.appex/FindMyWidgetItems](MACHOS/FindMyWidgetItems.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyWidgetPeople.appex/FindMyWidgetPeople](MACHOS/FindMyWidgetPeople.md)
- [/private/var/staged_system_apps/Fitness.app/Fitness](MACHOS/Fitness.md)
- [/private/var/staged_system_apps/Freeform.app/Extensions/USDRendererExtension.appex/USDRendererExtension](MACHOS/USDRendererExtension.md)
- [/private/var/staged_system_apps/Freeform.app/Freeform](MACHOS/Freeform.md)
- [/private/var/staged_system_apps/Freeform.app/PlugIns/FreeformWidgetKitExtension.appex/FreeformWidgetKitExtension](MACHOS/FreeformWidgetKitExtension.md)
- [/private/var/staged_system_apps/Health.app/Health](MACHOS/Health.md)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeEnergyWidgetsExtension.appex/HomeEnergyWidgetsExtension](MACHOS/HomeEnergyWidgetsExtension.md)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeWidget.appex/HomeWidget](MACHOS/HomeWidget.md)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeWidgetLockScreen.appex/HomeWidgetLockScreen](MACHOS/HomeWidgetLockScreen.md)
- [/private/var/staged_system_apps/Journal.app/Journal](MACHOS/Journal.md)
- [/private/var/staged_system_apps/Journal.app/PlugIns/JournalShareExtension.appex/JournalShareExtension](MACHOS/JournalShareExtension.md)
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
- [/private/var/staged_system_apps/MobileMail.app/PlugIns/MailWidgetExtension.appex/MailWidgetExtension](MACHOS/MailWidgetExtension.md)
- [/private/var/staged_system_apps/MobileNotes.app/MobileNotes](MACHOS/MobileNotes.md)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.WidgetExtension.appex/com.apple.mobilenotes.WidgetExtension](MACHOS/com.apple.mobilenotes.WidgetExtension.md)
- [/private/var/staged_system_apps/MobileSafari.app/PlugIns/SafariWidgetExtension.appex/SafariWidgetExtension](MACHOS/SafariWidgetExtension.md)
- [/private/var/staged_system_apps/MobileTimer.app/PlugIns/WorldClockWidget.appex/WorldClockWidget](MACHOS/WorldClockWidget.md)
- [/private/var/staged_system_apps/Music.app/Frameworks/MusicApplication.framework/MusicApplication](MACHOS/MusicApplication.md)
- [/private/var/staged_system_apps/Music.app/Frameworks/MusicApplication.framework/XPCServices/MusicScriptUpdateService.xpc/MusicScriptUpdateService](MACHOS/MusicScriptUpdateService.md)
- [/private/var/staged_system_apps/Music.app/Music](MACHOS/Music.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/MusicMessagesApp.appex/MusicMessagesApp](MACHOS/MusicMessagesApp.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/MusicWidgets.appex/MusicWidgets](MACHOS/MusicWidgets.md)
- [/private/var/staged_system_apps/News.app/News](MACHOS/News.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsToday2.appex/NewsToday2](MACHOS/NewsToday2.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsTodayIntents.appex/NewsTodayIntents](MACHOS/NewsTodayIntents.md)
- [/private/var/staged_system_apps/Passbook.app/PlugIns/PassbookLockedWidgetsExtension.appex/PassbookLockedWidgetsExtension](MACHOS/PassbookLockedWidgetsExtension.md)
- [/private/var/staged_system_apps/Passbook.app/PlugIns/PassbookWidgetsExtension-iPhone.appex/PassbookWidgetsExtension-iPhone](MACHOS/PassbookWidgetsExtension-iPhone.md)
- [/private/var/staged_system_apps/Photos.app/Photos](MACHOS/Photos.md)
- [/private/var/staged_system_apps/Photos.app/PlugIns/PhotosNotificationsUpdates.appex/PhotosNotificationsUpdates](MACHOS/PhotosNotificationsUpdates.md)
- [/private/var/staged_system_apps/Photos.app/PlugIns/PhotosReliveWidget.appex/PhotosReliveWidget](MACHOS/PhotosReliveWidget.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/NowPlayingUI.framework/NowPlayingUI](MACHOS/NowPlayingUI.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/PodcastsTranscripts.framework/PodcastsTranscripts](MACHOS/PodcastsTranscripts.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/ShelfKit.framework/ShelfKit](MACHOS/ShelfKit.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/ShelfKitCollectionViews.framework/ShelfKitCollectionViews](MACHOS/ShelfKitCollectionViews.md)
- [/private/var/staged_system_apps/Podcasts.app/PlugIns/com.apple.podcasts.DiagnosticExtension.appex/com.apple.podcasts.DiagnosticExtension](MACHOS/com.apple.podcasts.DiagnosticExtension.md)
- [/private/var/staged_system_apps/Podcasts.app/PlugIns/com.apple.podcasts.SpotlightIndexExtension.appex/com.apple.podcasts.SpotlightIndexExtension](MACHOS/com.apple.podcasts.SpotlightIndexExtension.md)
- [/private/var/staged_system_apps/Podcasts.app/Podcasts](MACHOS/Podcasts.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersIntentsExtension.appex/RemindersIntentsExtension](MACHOS/RemindersIntentsExtension.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersIntentsUIExtension.appex/RemindersIntentsUIExtension](MACHOS/RemindersIntentsUIExtension.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersSharingExtension.appex/RemindersSharingExtension](MACHOS/RemindersSharingExtension.md)
- [/private/var/staged_system_apps/Reminders.app/Reminders](MACHOS/Reminders.md)
- [/private/var/staged_system_apps/SequoiaTranslator.app/SequoiaTranslator](MACHOS/SequoiaTranslator.md)
- [/private/var/staged_system_apps/Shortcuts.app/Shortcuts](MACHOS/Shortcuts.md)
- [/private/var/staged_system_apps/Stocks.app/PlugIns/StocksWidget.appex/StocksWidget](MACHOS/StocksWidget.md)
- [/private/var/staged_system_apps/Stocks.app/Stocks](MACHOS/Stocks.md)
- [/private/var/staged_system_apps/Tips.app/Tips](MACHOS/Tips.md)
- [/private/var/staged_system_apps/VoiceMemos.app/VoiceMemos](MACHOS/VoiceMemos.md)
- [/private/var/staged_system_apps/Weather.app/PlugIns/WeatherPoster.appex/WeatherPoster](MACHOS/WeatherPoster.md)
- [/private/var/staged_system_apps/Weather.app/PlugIns/WeatherWidget.appex/WeatherWidget](MACHOS/WeatherWidget.md)
- [/private/var/staged_system_apps/Weather.app/Weather](MACHOS/Weather.md)
- [/sbin/launchd](MACHOS/launchd.md)
- [/usr/bin/abmlite](MACHOS/abmlite.md)
- [/usr/bin/swift-inspect](MACHOS/swift-inspect.md)
- [/usr/lib/dyld](MACHOS/dyld.md)
- [/usr/lib/libmobileassetd.dylib](MACHOS/libmobileassetd.dylib.md)
- [/usr/lib/libramrod.dylib](MACHOS/libramrod.dylib.md)
- [/usr/lib/system/introspection/libdispatch.dylib](MACHOS/libdispatch.dylib.md)
- [/usr/libexec/ASPCarryLog](MACHOS/ASPCarryLog.md)
- [/usr/libexec/DumpPanic](MACHOS/DumpPanic.md)
- [/usr/libexec/NANDTaskScheduler](MACHOS/NANDTaskScheduler.md)
- [/usr/libexec/ReportMemoryException](MACHOS/ReportMemoryException.md)
- [/usr/libexec/UserEventAgent](MACHOS/UserEventAgent.md)
- [/usr/libexec/anomalydetectiond](MACHOS/anomalydetectiond.md)
- [/usr/libexec/aonsensed](MACHOS/aonsensed.md)
- [/usr/libexec/appleaccountd](MACHOS/appleaccountd.md)
- [/usr/libexec/appleh16camerad](MACHOS/appleh16camerad.md)
- [/usr/libexec/applekeystored](MACHOS/applekeystored.md)
- [/usr/libexec/assessmentagent](MACHOS/assessmentagent.md)
- [/usr/libexec/audioaccessoryd](MACHOS/audioaccessoryd.md)
- [/usr/libexec/audioanalyticsd](MACHOS/audioanalyticsd.md)
- [/usr/libexec/audioclocksyncd](MACHOS/audioclocksyncd.md)
- [/usr/libexec/backboardd](MACHOS/backboardd.md)
- [/usr/libexec/batteryintelligenced](MACHOS/batteryintelligenced.md)
- [/usr/libexec/biomesyncd](MACHOS/biomesyncd.md)
- [/usr/libexec/bluetoothuserd](MACHOS/bluetoothuserd.md)
- [/usr/libexec/bootpd](MACHOS/bootpd.md)
- [/usr/libexec/cameracaptured](MACHOS/cameracaptured.md)
- [/usr/libexec/captiveagent](MACHOS/captiveagent.md)
- [/usr/libexec/caraccessoryd](MACHOS/caraccessoryd.md)
- [/usr/libexec/checkpointd](MACHOS/checkpointd.md)
- [/usr/libexec/companiond](MACHOS/companiond.md)
- [/usr/libexec/configd](MACHOS/configd.md)
- [/usr/libexec/coreidvd](MACHOS/coreidvd.md)
- [/usr/libexec/corerepaird](MACHOS/corerepaird.md)
- [/usr/libexec/cryptexd](MACHOS/cryptexd.md)
- [/usr/libexec/dasd](MACHOS/dasd.md)
- [/usr/libexec/demod](MACHOS/demod.md)
- [/usr/libexec/demod_helper](MACHOS/demod_helper.md)
- [/usr/libexec/dhcp6d](MACHOS/dhcp6d.md)
- [/usr/libexec/diskimagesiod](MACHOS/diskimagesiod.md)
- [/usr/libexec/dmd](MACHOS/dmd.md)
- [/usr/libexec/dockaccessoryd](MACHOS/dockaccessoryd.md)
- [/usr/libexec/driverkitd](MACHOS/driverkitd.md)
- [/usr/libexec/eligibilityd](MACHOS/eligibilityd.md)
- [/usr/libexec/feedbackd](MACHOS/feedbackd.md)
- [/usr/libexec/findmydeviced](MACHOS/findmydeviced.md)
- [/usr/libexec/findmylocated](MACHOS/findmylocated.md)
- [/usr/libexec/fmflocatord](MACHOS/fmflocatord.md)
- [/usr/libexec/fseventsd](MACHOS/fseventsd.md)
- [/usr/libexec/gamed](MACHOS/gamed.md)
- [/usr/libexec/gamepolicyd](MACHOS/gamepolicyd.md)
- [/usr/libexec/gpsd](MACHOS/gpsd.md)
- [/usr/libexec/hangreporter](MACHOS/hangreporter.md)
- [/usr/libexec/hangtracerd](MACHOS/hangtracerd.md)
- [/usr/libexec/icloudmailagent](MACHOS/icloudmailagent.md)
- [/usr/libexec/idcredd](MACHOS/idcredd.md)
- [/usr/libexec/inboxupdaterd](MACHOS/inboxupdaterd.md)
- [/usr/libexec/launchd_cache_loader](MACHOS/launchd_cache_loader.md)
- [/usr/libexec/linkd](MACHOS/linkd.md)
- [/usr/libexec/locationd](MACHOS/locationd.md)
- [/usr/libexec/lockdownd](MACHOS/lockdownd.md)
- [/usr/libexec/logd](MACHOS/logd.md)
- [/usr/libexec/logd_helper](MACHOS/logd_helper.md)
- [/usr/libexec/logd_reporter](MACHOS/logd_reporter.md)
- [/usr/libexec/lskdd](MACHOS/lskdd.md)
- [/usr/libexec/mediaparserd](MACHOS/mediaparserd.md)
- [/usr/libexec/mediaplaybackd](MACHOS/mediaplaybackd.md)
- [/usr/libexec/mlhostd](MACHOS/mlhostd.md)
- [/usr/libexec/mobile_obliterator](MACHOS/mobile_obliterator.md)
- [/usr/libexec/mobileactivationd](MACHOS/mobileactivationd.md)
- [/usr/libexec/mobileassetd](MACHOS/mobileassetd.md)
- [/usr/libexec/modelmanagerd](MACHOS/modelmanagerd.md)
- [/usr/libexec/momentsd](MACHOS/momentsd.md)
- [/usr/libexec/nanoregistryd](MACHOS/nanoregistryd.md)
- [/usr/libexec/nearbyd](MACHOS/nearbyd.md)
- [/usr/libexec/nehelper](MACHOS/nehelper.md)
- [/usr/libexec/nesessionmanager](MACHOS/nesessionmanager.md)
- [/usr/libexec/networkserviceproxy](MACHOS/networkserviceproxy.md)
- [/usr/libexec/nfcd](MACHOS/nfcd.md)
- [/usr/libexec/nsurlsessiond](MACHOS/nsurlsessiond.md)
- [/usr/libexec/online-auth-agent](MACHOS/online-auth-agent.md)
- [/usr/libexec/perfdiagsselfenabled](MACHOS/perfdiagsselfenabled.md)
- [/usr/libexec/photosfaced](MACHOS/photosfaced.md)
- [/usr/libexec/pipelined](MACHOS/pipelined.md)
- [/usr/libexec/powerexperienced](MACHOS/powerexperienced.md)
- [/usr/libexec/proactiveeventtrackerd](MACHOS/proactiveeventtrackerd.md)
- [/usr/libexec/profiled](MACHOS/profiled.md)
- [/usr/libexec/promotedcontentd](MACHOS/promotedcontentd.md)
- [/usr/libexec/proximitycontrold](MACHOS/proximitycontrold.md)
- [/usr/libexec/rapportd](MACHOS/rapportd.md)
- [/usr/libexec/remindd](MACHOS/remindd.md)
- [/usr/libexec/remoteappintentsd](MACHOS/remoteappintentsd.md)
- [/usr/libexec/remotepairingdeviced](MACHOS/remotepairingdeviced.md)
- [/usr/libexec/rtcreportingd](MACHOS/rtcreportingd.md)
- [/usr/libexec/screenshotsyncd](MACHOS/screenshotsyncd.md)
- [/usr/libexec/searchpartyd](MACHOS/searchpartyd.md)
- [/usr/libexec/security-sysdiagnose](MACHOS/security-sysdiagnose.md)
- [/usr/libexec/securityd](MACHOS/securityd.md)
- [/usr/libexec/securityuploadd](MACHOS/securityuploadd.md)
- [/usr/libexec/seserviced](MACHOS/seserviced.md)
- [/usr/libexec/sharingd](MACHOS/sharingd.md)
- [/usr/libexec/signpost_reporter](MACHOS/signpost_reporter.md)
- [/usr/libexec/softposreaderd](MACHOS/softposreaderd.md)
- [/usr/libexec/spindump_fileparser](MACHOS/spindump_fileparser.md)
- [/usr/libexec/sportsd](MACHOS/sportsd.md)
- [/usr/libexec/swtransparencyd](MACHOS/swtransparencyd.md)
- [/usr/libexec/sysdiagnose_helper](MACHOS/sysdiagnose_helper.md)
- [/usr/libexec/sysdiagnosed](MACHOS/sysdiagnosed.md)
- [/usr/libexec/systemservicemonitord](MACHOS/systemservicemonitord.md)
- [/usr/libexec/tailspind](MACHOS/tailspind.md)
- [/usr/libexec/terminusd](MACHOS/terminusd.md)
- [/usr/libexec/thermalmonitord](MACHOS/thermalmonitord.md)
- [/usr/libexec/timed](MACHOS/timed.md)
- [/usr/libexec/transparencyd](MACHOS/transparencyd.md)
- [/usr/libexec/trustd](MACHOS/trustd.md)
- [/usr/libexec/tvremoted](MACHOS/tvremoted.md)
- [/usr/libexec/usermanagerd](MACHOS/usermanagerd.md)
- [/usr/libexec/videocodecd](MACHOS/videocodecd.md)
- [/usr/libexec/watchdogd](MACHOS/watchdogd.md)
- [/usr/libexec/wifip2pd](MACHOS/wifip2pd.md)
- [/usr/libexec/wifivelocityd](MACHOS/wifivelocityd.md)
- [/usr/libexec/xpcproxy](MACHOS/xpcproxy.md)
- [/usr/libexec/xpcroleaccountd](MACHOS/xpcroleaccountd.md)
- [/usr/sbin/WirelessRadioManagerd](MACHOS/WirelessRadioManagerd.md)
- [/usr/sbin/appleh16camerad](MACHOS/appleh16camerad.md)
- [/usr/sbin/bluetoothd](MACHOS/bluetoothd.md)
- [/usr/sbin/distnoted](MACHOS/distnoted.md)
- [/usr/sbin/mDNSResponder](MACHOS/mDNSResponder.md)
- [/usr/sbin/spindump](MACHOS/spindump.md)
- [/usr/sbin/wifid](MACHOS/wifid.md)

</details>

### 🔑 Entitlements

- [Entitlements DIFF](Entitlements.md)

## Firmware

### ⬆️ Updated (16)

<details>
  <summary><i>View Updated</i></summary>

#### AppleAVE2FW_H17.im4p

>  `AppleAVE2FW_H17.im4p`

```diff

   __TEXT.__chain_starts: 0x0
   __DATA.__const: 0x2a20
   __DATA._rtk_patchbay: 0x228
-  __DATA.__data: 0x1070
+  __DATA.__data: 0x1078
   __DATA._rtk_power: 0x368
   __DATA.__gxf_data: 0x10
   __DATA._rtk_tunables: 0x6a0

```

#### adc-rheia-d9x.im4p

>  `adc-rheia-d9x.im4p`

```diff

 
-  __TEXT.__text: 0x833638
+  __TEXT.__text: 0x833634
   __TEXT.__const: 0x9b5960
   __TEXT.text_env: 0x4fda4
   __TEXT._rtk_mtab: 0x2b8
CStrings:
+ "23:28:24"
- "20:15:45"

```

#### agx_a000

>  `agx_a000`

```diff

 
-  __TEXT.__text: 0x34dec
+  __TEXT.__text: 0x34dc4
   __TEXT.__gxf_shr_code: 0x55c
   __TEXT.__gxf_code: 0x1230
   __TEXT.__gxf_code_pad: 0x0
-  __TEXT.__const: 0x1b78
+  __TEXT.__const: 0x1b40
   __TEXT._rtk_patchbay: 0x228
   __TEXT._rtk_tunables: 0x6a0
   __TEXT.__chain_starts: 0x2c
-  __TEXT.__cstring: 0x2311
+  __TEXT.__cstring: 0x230e
   __DATA.__gxf_data: 0x4200
   __DATA.__data: 0x14a28
   __DATA.__const: 0x5d0

   __DATA.__xnu_shared: 0x3c000
   __DATA._rtk_mtab: 0x390
   __DATA.__zerofill: 0x58058
-  Functions: 418
+  Functions: 417
   Symbols:   230
   CStrings:  237
 
CStrings:
+ "GFX %s %s FW %s! (%s)"
+ "Mar 24 2025 19:57:51"
- "GFX %s %u %s FW %s! (%s)"
- "Mar 15 2025 17:46:33"

```

#### agx_a010

>  `agx_a010`

```diff

 
-  __TEXT.__text: 0x34d34
+  __TEXT.__text: 0x34d0c
   __TEXT.__gxf_shr_code: 0x55c
   __TEXT.__gxf_code: 0x1230
   __TEXT.__gxf_code_pad: 0x0
-  __TEXT.__const: 0x1b78
+  __TEXT.__const: 0x1b40
   __TEXT._rtk_patchbay: 0x228
   __TEXT._rtk_tunables: 0x6a0
   __TEXT.__chain_starts: 0x2c
-  __TEXT.__cstring: 0x22a3
+  __TEXT.__cstring: 0x22a0
   __DATA.__gxf_data: 0x4200
   __DATA.__data: 0x14a28
   __DATA.__const: 0x5d0

   __DATA.__xnu_shared: 0x3c000
   __DATA._rtk_mtab: 0x390
   __DATA.__zerofill: 0x58058
-  Functions: 416
+  Functions: 415
   Symbols:   230
   CStrings:  235
 
CStrings:
+ "GFX %s %s FW %s! (%s)"
+ "Mar 24 2025 20:04:54"
- "GFX %s %u %s FW %s! (%s)"
- "Mar 15 2025 17:52:11"

```

#### agx_b000

>  `agx_b000`

```diff

 
-  __TEXT.__text: 0x34c10
+  __TEXT.__text: 0x34be8
   __TEXT.__gxf_shr_code: 0x55c
   __TEXT.__gxf_code: 0x1230
   __TEXT.__gxf_code_pad: 0x0
-  __TEXT.__const: 0x1b78
+  __TEXT.__const: 0x1b40
   __TEXT._rtk_patchbay: 0x228
   __TEXT._rtk_tunables: 0x6a0
   __TEXT.__chain_starts: 0x2c
-  __TEXT.__cstring: 0x22a3
+  __TEXT.__cstring: 0x22a0
   __DATA.__gxf_data: 0x4200
   __DATA.__data: 0x14a28
   __DATA.__const: 0x5d0

   __DATA.__xnu_shared: 0x3c000
   __DATA._rtk_mtab: 0x390
   __DATA.__zerofill: 0x58058
-  Functions: 416
+  Functions: 415
   Symbols:   230
   CStrings:  235
 
CStrings:
+ "GFX %s %s FW %s! (%s)"
+ "Mar 24 2025 20:02:13"
- "GFX %s %u %s FW %s! (%s)"
- "Mar 15 2025 17:49:58"

```

#### agx_b010

>  `agx_b010`

```diff

 
-  __TEXT.__text: 0x34c9c
+  __TEXT.__text: 0x34c74
   __TEXT.__gxf_shr_code: 0x55c
   __TEXT.__gxf_code: 0x1230
   __TEXT.__gxf_code_pad: 0x0
-  __TEXT.__const: 0x1b78
+  __TEXT.__const: 0x1b40
   __TEXT._rtk_patchbay: 0x228
   __TEXT._rtk_tunables: 0x6a0
   __TEXT.__chain_starts: 0x2c
-  __TEXT.__cstring: 0x22a3
+  __TEXT.__cstring: 0x22a0
   __DATA.__gxf_data: 0x4200
   __DATA.__data: 0x14a28
   __DATA.__const: 0x5d0

   __DATA.__xnu_shared: 0x3c000
   __DATA._rtk_mtab: 0x390
   __DATA.__zerofill: 0x58058
-  Functions: 416
+  Functions: 415
   Symbols:   230
   CStrings:  235
 
CStrings:
+ "GFX %s %s FW %s! (%s)"
+ "Mar 24 2025 20:06:09"
- "GFX %s %u %s FW %s! (%s)"
- "Mar 15 2025 17:53:15"

```

#### agx_b100

>  `agx_b100`

```diff

 
-  __TEXT.__text: 0x34b78
+  __TEXT.__text: 0x34b50
   __TEXT.__gxf_shr_code: 0x55c
   __TEXT.__gxf_code: 0x1230
   __TEXT.__gxf_code_pad: 0x0
-  __TEXT.__const: 0x1b78
+  __TEXT.__const: 0x1b40
   __TEXT._rtk_patchbay: 0x228
   __TEXT._rtk_tunables: 0x6a0
   __TEXT.__chain_starts: 0x2c
-  __TEXT.__cstring: 0x22a3
+  __TEXT.__cstring: 0x22a0
   __DATA.__gxf_data: 0x4200
   __DATA.__data: 0x14a28
   __DATA.__const: 0x5d0

   __DATA.__xnu_shared: 0x3c000
   __DATA._rtk_mtab: 0x390
   __DATA.__zerofill: 0x58058
-  Functions: 416
+  Functions: 415
   Symbols:   230
   CStrings:  235
 
CStrings:
+ "GFX %s %s FW %s! (%s)"
+ "Mar 24 2025 20:03:38"
- "GFX %s %u %s FW %s! (%s)"
- "Mar 15 2025 17:51:07"

```

#### ansf.t8140.release.im4p

>  `ansf.t8140.release.im4p`

```diff

 
   __TEXT.text_first: 0x4488
-  __TEXT.__text: 0x1c1400
-  __TEXT.shared: 0xd914
-  __TEXT.read: 0x6b14
-  __TEXT.__const: 0x5398
+  __TEXT.__text: 0x1c3070
+  __TEXT.shared: 0xdd00
+  __TEXT.read: 0x6e90
+  __TEXT.__const: 0x5418
   __TEXT.idle_hooks: 0x10
-  __TEXT.__cstring: 0x229a1
+  __TEXT.__cstring: 0x22c84
   __TEXT.__chain_starts: 0x0
   __TEXT.__constructor: 0x0
   __TEXT._rtk_mtab: 0x310

   __DATA._rtk_power: 0x160
   __DATA._rtk_patchbay: 0x3f3
   __DATA._rtk_tunables: 0x6a0
-  __DATA.__const: 0x1aa0
-  __DATA.__data: 0x6008
+  __DATA.__const: 0x1ab0
+  __DATA.__data: 0x6000
   __DATA._rtk_init_stack: 0x1000
   __DATA._rtk_irq_stack: 0x1000
   __DATA._rtk_exc_stack: 0x1000

   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__mod_init_func: 0x0
-  __DATA.core_globals: 0x156
+  __DATA.core_globals: 0x157
   __DATA.large_stacks: 0x20000
   __DATA.small_stacks: 0x2000
-  __DATA.__zerofill: 0x246248
+  __DATA.__zerofill: 0x246388
   Functions: 0
   Symbols:   0
-  CStrings:  3766
+  CStrings:  3775
 
CStrings:
+ " BandsTemp_getDeviceTemperatureAll -> %ums"
+ "2077.120.68.0.1"
+ "77.120.68.0.1~86"
+ "AppleStorageFirmware-2077.120.68.0.1~86"
+ "FADUMP: Dumping FA to memory..."
+ "FADUMP: ERROR! Couldn't assert asi device %d"
+ "FADUMP: ERROR! FA dump is disabled"
+ "FADUMP: ERROR! FA dump is not supported"
+ "FADUMP: ERROR! FA dump was already executed"
+ "FADUMP: ERROR! FAdump Init failed!"
+ "FADUMP: ERROR! Memory address is not 0x%x aligned!"
+ "FADUMP: ERROR! Memory size is not 0x%x aligned!"
+ "FADUMP: ERROR! Nand Discovery not completed"
+ "FADUMP: ERROR! No memory!"
+ "FADUMP: ERROR! No space in Util panic log for MSP FA"
+ "FADUMP: ERROR! RTK_mc_assume failed: %d"
+ "FADUMP: Error: failed to check if device %d is asserted"
+ "FADUMP: FA stored 0x%x"
+ "FADUMP: FA_AllocationSize: %d"
+ "FADUMP: FA_Init isEnabled: %d, Size: %d"
+ "FADUMP: Finalizing FA dump: magic 0x%x, crc 0x%x"
+ "FADUMP: Forcing assert on asi device %d"
+ "FADUMP: Found Prev Assert[%d][%d,%d,%d]"
+ "FADUMP: MSP FA size: %d"
+ "FADUMP: Possible data incoherency"
+ "FADUMP: WARNING! Compression buffer allocation failed."
+ "FADUMP: WARNING! Couldn't get fa size for asi device %d"
+ "FADUMP: WARNING! FA Mem Release failed. status: 0x%x"
+ "FADUMP: WARNING! Failed to compress MSP %d"
+ "FADUMP: WARNING! Failed to store ASI logger"
+ "FADUMP: WARNING! Failed to store FTL entry %d"
+ "FADUMP: WARNING! No space left to store MSP %d"
+ "FADUMP: WARNING! Not extracting asi logger. size %d, addr 0x%x"
+ "FADUMP: WARNING! failed to read FA data for asi device %d"
+ "FADUMP: comressed req:%d, SizeAvg %d"
+ "FADUMP: deflate failed. status %d, Sec left to store: %d"
+ "FADUMP: deflateEnd failed. status %d"
+ "FADUMP: deflateInit2 failed. status %d"
+ "MassScan: Pilot scan done on %d bands after %lld seconds, but can't exit early, because %d bands failed, need to continue to full scan"
+ "Set DC table ver %u by %s, has_thermal_throttling 0"
+ "Such status is not allowed for block scan read command"
+ "TT cross temp init"
+ "Tried to read feature bit %d but feature bits struct is not initialized"
+ "WARNING! RAID config changed: Old: %u New: %u"
+ "cross temp detected, band %u temp (%d,%d) read temp (%d,%d), opType %d, isNew %u"
+ "cross temp isQualityError, band %u, opType %u"
+ "cross temp thershold not set yet"
+ "e=0x%x"
+ "forced temperature: %d, core temp %d, enable %u, reset stats %u"
+ "fwp"
+ "host"
+ "thermal_throttle.c"
+ "wrong high threshold crossed %u %d %d"
+ "wrong low threshold crossed %u %d %d"
- " PreNandEng_getDeviceTemperature -> %ums"
- ".100.377.0.1~112"
- "2077.100.377.0.1"
- "AppleStorageFirmware-2077.100.377.0.1~112"
- "CTL cross temp detected on flow %d, lba %d opType %d, size %d shouldCount %d"
- "Dumping FA to memory..."
- "ERROR! Couldn't assert asi device %d"
- "ERROR! FA dump is disabled"
- "ERROR! FA dump is not supported"
- "ERROR! FA dump was already executed"
- "ERROR! FAdump Init failed!"
- "ERROR! Memory address is not 0x%x aligned!"
- "ERROR! Memory size is not 0x%x aligned!"
- "ERROR! Nand Discovery not completed"
- "ERROR! No memory!"
- "ERROR! No space in Util panic log for MSP FA"
- "ERROR! RTK_mc_assume failed: %d"
- "Error: failed to check if device %d is asserted"
- "FA stored 0x%x"
- "FA_AllocationSize: %d"
- "FA_Init isEnabled: %d, Size: %d"
- "Finalizing FA dump: magic 0x%x, crc 0x%x"
- "Forcing assert on asi device %d"
- "Found Prev Assert[%d][%d,%d,%d]"
- "MSP FA size: %d"
- "Possible data incoherency"
- "WARNING! Compression buffer allocation failed."
- "WARNING! Couldn't get fa size for asi device %d"
- "WARNING! FA Mem Release failed. status: 0x%x"
- "WARNING! Failed to compress MSP %d"
- "WARNING! Failed to store ASI logger"
- "WARNING! Failed to store FTL entry %d"
- "WARNING! No space left to store MSP %d"
- "WARNING! Not extracting asi logger. size %d, addr 0x%x"
- "WARNING! failed to read FA data for asi device %d"
- "comressed req:%d, SizeAvg %d"
- "deflate failed. status %d, Sec left to store: %d"
- "deflateEnd failed. status %d"
- "deflateInit2 failed. status %d"
- "done scan ET bands %u"
- "forced device temperature is: %d"
- "forced tunnel temperature is: %d"
- "must be blocking"
- "must be valid temperatute at this point"
- "reset temprature stats"

```

#### exclave_ExclaveStackshotServer

>  `exclave_ExclaveStackshotServer`

```diff

 64.0.0.0.0
-  __TEXT.__text: 0x32eac0
+  __TEXT.__text: 0x32ec58
   __TEXT.__lcxx_override: 0x204
   __TEXT.__const: 0xd7d80
   __TEXT.__cstring: 0x2324b

   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x28
   __DATA.__bss: 0x451e0
-  __DATA.__common: 0x2754
+  __DATA.__common: 0x2764
   __PDATA.__mod_init_func: 0x0
   __PDATA.__shared_cache: 0x0
   __DATA_CONST.__mod_init_func: 0x0
CStrings:
+ "/AppleInternal/Library/BuildRoots/a8fb6168-0667-11f0-a4eb-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.5.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
- "/AppleInternal/Library/BuildRoots/f42a321a-fb9b-11ef-8bf4-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.4.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"

```

#### exclave_pmm_exclave

>  `exclave_pmm_exclave`

```diff

-839.102.1.0.0
-  __TEXT.__text: 0x398f0
+839.120.23.0.1
+  __TEXT.__text: 0x395dc
   __TEXT.__const: 0x1c950
-  __TEXT.__cstring: 0xd56b
+  __TEXT.__cstring: 0xd550
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0
   __TEXT.__term_offsets: 0x0

   __DATA_CONST.__mod_term_func: 0x0
   __PDATA.__mod_init_func: 0x0
   __PDATA.__shared_cache: 0x0
-  Functions: 1029
+  Functions: 1022
   Symbols:   4
-  CStrings:  1277
+  CStrings:  1276
 
CStrings:
+ "/AppleInternal/Library/BuildRoots/a8fb6168-0667-11f0-a4eb-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.5.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
- "/AppleInternal/Library/BuildRoots/f42a321a-fb9b-11ef-8bf4-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.4.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
- "TB_ERROR_SUCCESS == tb_err"

```

#### exclave_roottask

>  `exclave_roottask`

```diff

-839.102.1.0.0
-  __TEXT.__text: 0x4a7c98
+839.120.23.0.1
+  __TEXT.__text: 0x4a90e0
   __TEXT.__lcxx_override: 0x200
-  __TEXT.__const: 0xe4a76
+  __TEXT.__const: 0xe4a56
   __TEXT.__cstring: 0x2fe4a
   __TEXT.__swift5_typeref: 0xa472
-  __TEXT.__swift5_capture: 0x1804
+  __TEXT.__swift5_capture: 0x1834
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__swift5_reflstr: 0x9135
+  __TEXT.__swift5_reflstr: 0x9125
   __TEXT.__swift5_assocty: 0x62d0
-  __TEXT.__constg_swiftt: 0x114a0
-  __TEXT.__swift5_fieldmd: 0xe58c
-  __TEXT.__swift5_builtin: 0xce4
-  __TEXT.__swift5_proto: 0x232c
-  __TEXT.__swift5_types: 0x1004
+  __TEXT.__constg_swiftt: 0x115ac
+  __TEXT.__swift5_fieldmd: 0xe564
+  __TEXT.__swift5_builtin: 0xcd0
+  __TEXT.__swift5_proto: 0x2328
+  __TEXT.__swift5_types: 0x1000
   __TEXT.__swift5_protos: 0x32c
-  __TEXT.__swift5_mpenum: 0x444
+  __TEXT.__swift5_mpenum: 0x434
   __TEXT.__swift5_types2: 0x10
   __TEXT.__swift_as_entry: 0x210
   __TEXT.__swift_as_ret: 0x298

   __TEXT.__swift5_replace: 0x0
   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x24
-  __TEXT.__eh_frame: 0x1a24c
+  __TEXT.__eh_frame: 0x1a4cc
   __DATA.__got: 0x198
   __DATA.__auth_ptr: 0x140
   __DATA.__mod_init_func: 0x50
-  __DATA.__const: 0x2d6d0
+  __DATA.__const: 0x2d620
   __DATA.__objc_imageinfo: 0x8
-  __DATA.__data: 0x94e8
+  __DATA.__data: 0x9660
   __DATA.__shared_cache: 0x70
   __DATA.__DEVICETREE: 0x30
   __DATA.__ENDPOINTS: 0x62a

   __PDATA.__shared_cache: 0x0
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  Functions: 17515
+  Functions: 17561
   Symbols:   23
-  CStrings:  5322
+  CStrings:  5323
 
CStrings:
+ "/AppleInternal/Library/BuildRoots/a8fb6168-0667-11f0-a4eb-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.5.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
+ "DefaultXzoneZone"
+ "Trying to release released vaddr in ExclavesVMM"
+ "Unimplemented for core"
+ "Wrong offset for populate in ExclavesVMM"
+ "appendSegmentRegionLocked(machoFile:segment:)"
+ "range permissions vmaPriv vmaAttrs kind "
- "/AppleInternal/Library/BuildRoots/f42a321a-fb9b-11ef-8bf4-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.4.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
- "ExtVMRegion{ExclaveCore::: vbase: 0x"
- "Unexpected shadow region "
- "addFaultableRange(span:roCaps:canSetIncomplete:)"
- "cannot map a faultable region "
- "range permissions faultability vmaPriv vmaAttrs kind "

```

#### exclave_sharedcache

>  `exclave_sharedcache`

```diff

-543.102.2.0.0
-  __TEXT.__text: 0x4ef4bc
+543.120.22.0.0
+  __TEXT.__text: 0x4efc24
   __TEXT.__lcxx_override: 0x200
-  __TEXT.__cstring: 0x39d4f
-  __TEXT.__const: 0xfcb48
-  __TEXT.__swift5_typeref: 0xfa33
-  __TEXT.__swift5_reflstr: 0xa868
+  __TEXT.__cstring: 0x39bef
+  __TEXT.__const: 0xfcd98
+  __TEXT.__swift5_typeref: 0xfa01
+  __TEXT.__swift5_reflstr: 0xa7e8
   __TEXT.__swift5_assocty: 0x6e80
-  __TEXT.__swift5_fieldmd: 0x11f48
-  __TEXT.__constg_swiftt: 0x1cea0
+  __TEXT.__swift5_fieldmd: 0x11ef4
+  __TEXT.__constg_swiftt: 0x1cea8
   __TEXT.__swift5_protos: 0x700
-  __TEXT.__swift5_proto: 0x2bc0
+  __TEXT.__swift5_proto: 0x2bc8
   __TEXT.__swift5_types: 0x1844
   __TEXT.__swift5_types2: 0x1c
   __TEXT.__swift5_builtin: 0xeb0

   __TEXT.__term_offsets: 0x0
   __TEXT.__swift5_replace: 0x0
   __TEXT.__thread_starts: 0x40
-  __TEXT.__eh_frame: 0x27564
+  __TEXT.__eh_frame: 0x274cc
   __DATA.__got: 0x18
   __DATA.__auth_ptr: 0x2a8
   __DATA.__mod_init_func: 0x38
-  __DATA.__const: 0x30ba0
+  __DATA.__const: 0x30bb8
   __DATA.__objc_imageinfo: 0x8
-  __DATA.__data: 0x11858
+  __DATA.__data: 0x11838
   __DATA.__shared_cache: 0xe0
-  __DATA.__TIGHTBEAM_VT: 0x4e0
-  __DATA.__TIGHTBEAM: 0x130
-  __DATA.__ENDPOINTS: 0xdeef
+  __DATA.__TIGHTBEAM_VT: 0x4b0
+  __DATA.__TIGHTBEAM: 0x128
+  __DATA.__ENDPOINTS: 0xe30b
   __DATA.__thread_vars: 0x60
   __DATA.__mod_term_func: 0x0
   __DATA.__DARTS: 0x93f

   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x28
   __DATA.__common: 0x6c6
-  __DATA.__bss: 0x9120
+  __DATA.__bss: 0x9170
   __PDATA.__data: 0x1bf0
   __PDATA.__const: 0x43f8
   __PDATA.__ENDPOINTS: 0x731

   __PDATA.__auth_ptr: 0x38
   __PDATA.__objc_imageinfo: 0x8
   __PDATA.__bss: 0x47b8
-  __PDATA.__common: 0x2528
+  __PDATA.__common: 0x2530
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  Functions: 19764
+  Functions: 19759
   Symbols:   0
   CStrings:  5764
 
CStrings:
+ "/AppleInternal/Library/BuildRoots/a8fb6168-0667-11f0-a4eb-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.5.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
+ "/AppleInternal/Library/BuildRoots/a8fb6168-0667-11f0-a4eb-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.5.Internal.sdk/System/ExclaveCore/usr/local/standalone/RTKit/usr/include/protocols/mbi_tightbeam_protocol.h"
+ "BUG IN LIBTRACE: Received a BATCH_ERROR while creating a LogBatch"
+ "DefaultXzoneZone"
+ "OSLogServerComponent/LogServer.swift"
+ "[%s][error] Tracepoint header size %lu exceeded maximum of %lu\n"
+ "[XNUP] Spawned pmm upcall thread %p on endpoint 0x%lx\n"
+ "_os_log_payload_size(olp), OS_LOG_PAYLOAD_HARD_MAX_SIZE"
+ "data_size <= max_payload_size"
+ "olp->olp_tpb.tp_size, OS_LOG_PAYLOAD_HDR_SIZE"
- "$JgExclaveIndicatorControllerComponent.ExclaveIndicatorController.init(allowInternalEICSecurityPolicies:isRestore:exAudioArbiter:exHealthCheck:scAOP:cameraRestriction:buttonDetection:crashDetection:sepVariables:voiceTriggerEvent:prox:)"
- "/AppleInternal/Library/BuildRoots/a55c1311-fff2-11ef-a3d7-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.4.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
- "/AppleInternal/Library/BuildRoots/a55c1311-fff2-11ef-a3d7-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.4.Internal.sdk/System/ExclaveCore/usr/local/standalone/RTKit/usr/include/protocols/mbi_tightbeam_protocol.h"
- "/AppleInternal/Library/BuildRoots/f42a321a-fb9b-11ef-8bf4-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.4.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
- "[%s][error] Dropped oversized log of length %u\n"
- "[%s][error] Dropped oversized log of length %zu\n"
- "_os_log_payload_flattened_size(olp)"
- "_os_log_payload_size(olp), OS_LOG_BUFFER_MAX_SIZE"
- "data_size <= OS_LOG_BUFFER_MAX_SIZE"
- "pub_data_size <= data_size"

```

#### h17_ane_fw_theia_d9x.im4p

>  `h17_ane_fw_theia_d9x.im4p`

```diff

 
-  __TEXT.__text: 0xbdef8
-  __TEXT.__const: 0x41f4
-  __TEXT.__cstring: 0x1ba03
+  __TEXT.__text: 0x9ba10
+  __TEXT.__const: 0x41e0
+  __TEXT.__cstring: 0x13811
   __TEXT.ce_env: 0x4000
   __TEXT.__constructor: 0x0
   __TEXT.text_env: 0x20
-  __DATA.__const: 0x9f50
+  __DATA.__const: 0x9f10
   __DATA._rtk_heap: 0x1000
-  __DATA.__data: 0xf68
+  __DATA.__data: 0xd68
   __DATA._rtk_power: 0x3b8
   __DATA._rtk_patchbay: 0x278
   __DATA._rtk_init_stack: 0x10000

   __DATA._rtk_mtab: 0x2a0
   __DATA.__gxf_data: 0x10
   __DATA.__mod_init_func: 0x0
-  __DATA.__zerofill: 0x1cdf20
-  Functions: 1506
+  __DATA.__zerofill: 0x1f9f20
+  Functions: 1392
   Symbols:   0
-  CStrings:  3400
+  CStrings:  2239
 
CStrings:
+ "%s .Sanity check failure!\n"
+ "21:14:01"
+ "Couldn't find ShareMemInfoItem to free !!!\n"
+ "IPC Endpoint cmd failed %d"
+ "IPC Endpoint cmd failure"
+ "Mar 21 2025"
+ "Procedure %d exceeded maximum for program %d"
+ "Run out of CSharedMemory !!!\n"
+ "fwPriority < 8"
+ "hwqId < 8"
+ "pProc != __null"
+ "pProg != __null"
+ "unremap WriteMessage failed\n"
- "\tFW Latency Signposts 0x%x id 0x%x ts %lld"
- "\x1b[31m\"    Found Matched Priority Q[%d]S[%d] during Termination\"\x1b[39m"
- "\x1b[31m\"ABORT queue %d slot %d (nid %d) with multi segment\"\x1b[39m"
- "\x1b[31m\"Fail\"\x1b[39m"
- "\x1b[31m\"[ABORT] Suspend other TQs for TQ[%d]S[%d] at %lld\"\x1b[39m"
- "\x1b[31m\"[ABORT] TQ abort Q[%d] -> at %lld\"\x1b[39m"
- "\x1b[31m\"[ABORT] TQ abort Q[%d] -> both slots, first slot is %d\"\x1b[39m"
- "\x1b[31m\"[ABORT] TQ abort Q[%d] -> slot [%d]\"\x1b[39m"
- "\x1b[31m\"[StopTqInt] nid %d\"\x1b[39m"
- "\x1b[31m[VERIFICATION]\x1b[39m BAR[%d] bufferIndex %d is NOT matched with any buffer!"
- "\x1b[31m[VERIFICATION]\x1b[39m BAR[%d] bufferIndex %d is matched with buffers more than one!"
- "\x1b[31m[VERIFICATION]\x1b[39m BAR[%d] index %d should <= %d!"
- "\x1b[31m[VERIFICATION]\x1b[39m Generic ANE[%d] nbrOfNe %d exceeds H11 max NE %d!"
- "\x1b[31m[VERIFICATION]\x1b[39m Generic section (%lu) is smaller than actual (%lu)!"
- "\x1b[31m[VERIFICATION]\x1b[39m Generic section buffer[%d] is not valid!"
- "\x1b[31m[VERIFICATION]\x1b[39m Generic section buffer[%d] is wrong type %d!"
- "\x1b[31m[VERIFICATION]\x1b[39m KernelProp[%d] exceeds limit (offset, len) (0x%llx, %lld) section size %lu!"
- "\x1b[31m[VERIFICATION]\x1b[39m KernelProp[%d] offset 0x%llx is overlapped with the previous offset 0x%llx len %lld!"
- "\x1b[31m[VERIFICATION]\x1b[39m Operation BAR setup number %d is exceed MAX_BAR_SLOTS %d!"
- "\x1b[31m[VERIFICATION]\x1b[39m Operation number %d exceeds MAX Operation number (%d)!"
- "\x1b[31m[VERIFICATION]\x1b[39m Operation section (%lu) is smaller than actual (%lu)!"
- "\x1b[31m[VERIFICATION]\x1b[39m Operation[%d] BAR setup is wrong!"
- "\x1b[31m[VERIFICATION]\x1b[39m Operation[%d] bar[%d] index %d exceeds H11 bar slots %d!"
- "\x1b[31m[VERIFICATION]\x1b[39m Operation[%d] nbrOfLocalbarSetup %d exceeds EAnsProgramBarMaxIndex %d!"
- "\x1b[31m[VERIFICATION]\x1b[39m Operation[%d] nbrOfNe %d exceeds H11 max NE %d!"
- "\x1b[31m[VERIFICATION]\x1b[39m Operation[%d] wrong opType %d!"
- "\x1b[31m[VERIFICATION]\x1b[39m Procedure[%d] exceeds limit (offset, len) (0x%llx, %lld) section size %lu!"
- "\x1b[31m[VERIFICATION]\x1b[39m Procedure[%d] offset 0x%llx is overlapped with the previous offset 0x%llx len %lld!"
- "\x1b[31m[VERIFICATION]\x1b[39m SegmentProp section (%lu) is smaller than actual (%lu)!"
- "\x1b[31m[VERIFICATION]\x1b[39m Segment[%d] Addr %p EON %d last TID %d with Liveouts 0x%x"
- "\x1b[31m[VERIFICATION]\x1b[39m Segment[%d] Addr %p TID %d with 0 size"
- "\x1b[31m[VERIFICATION]\x1b[39m Segment[%d] exceeds limit (offset, len) (0x%llx, %lld) section size %lu!"
- "\x1b[31m[VERIFICATION]\x1b[39m Segment[%d] len %lld is smaller than ane_Network_Seg_Hdr_t (BranchEn %d)!"
- "\x1b[31m[VERIFICATION]\x1b[39m Segment[%d] number of TD (%d) does not match value in prop (%d)"
- "\x1b[31m[VERIFICATION]\x1b[39m TD[%d] offset 0x%llx is overlapped with the previous offset 0x%llx len %lld!"
- "\x1b[31m[VERIFICATION]\x1b[39m maxAneUsed %d :: H11 maxAneUsed should be %d!"
- "\x1b[31m[VERIFICATION]\x1b[39m sCSneCmdProcedureCall buffer[%d] is not valid!"
- "\x1b[31m[VERIFICATION]\x1b[39m sCSneCmdProcedureCall buffer[%d]:index[%d] SHOULD not match with Kernel!"
- "\x1b[31m[VERIFICATION]\x1b[39m sCSneCmdProcedureCall buffer[%d]:index[%d] SHOULD not match with segment!"
- "\x1b[31m[VERIFICATION]\x1b[39m sCSneCmdProcedureCall buffer[%d]:index[%d] is matched more than one!"
- "\x1b[31m[VERIFICATION]\x1b[39m sCSneCmdProcedureCall buffer[%d]:index[%d] is not matched with any of buffers!"
- "\x1b[31m[VERIFICATION]\x1b[39m sCSneCmdProcedureCall buffer[%d]:index[%d](%lld)=>Generic:buffer[%d](%lld). But wrong size!"
- "\x1b[31m[VERIFICATION]\x1b[39m sCSneCmdProcedureCall buffer[%d]:index[%d]=>Generic:buffer[%d]. But not valid!"
- "\x1b[31m[VERIFICATION]\x1b[39m sCSneCmdProcedureCall nbfOfbuffers %d (range 1 <= # <= 64)!"
- "\x1b[31m[VERIFICATION]\x1b[39m totalBufferNbr %d :: range should 0 < # < ECSneProgramMaxBuf (%d)!"
- "\x1b[32m\"Success\"\x1b[39m"
- "\x1b[33m\"Saving KMem from 0x%zx with 0x%zx\"\x1b[39m"
- "\x1b[33m\"Saving L2 from 0x%zx with 0x%zx\"\x1b[39m"
- "\x1b[33m\"Saving ane registers from 0x%zx with 0x%zx\"\x1b[39m"
- "\x1b[33m\"Start saving out after running into TD#%d from (%d-%d-%d)\"\x1b[39m"
- "\x1b[33m* PROGRAM :\x1b[39m"
- "\x1b[33m* TD :\x1b[39m"
- "\x1b[33m***** ANE RUN INFO ***** : program (0x%x)\x1b[39m"
- "\x1b[33m***** ANE TD INFO ***** : program (0x%x)\x1b[39m"
- "\x1b[33m************************\x1b[39m"
- "\x1b[34m* OPTIONS *\x1b[39m"
- "\x1b[34m***** ANE STATS *****\x1b[39m"
- "\x1b[34m***** PROCEDURE INFO *****\x1b[39m"
- "\x1b[34m***** PROCESS INFO *****\x1b[39m"
- "\x1b[34m***** PROGRAM INFO *****\x1b[39m"
- "\x1b[34m*********************\x1b[39m"
- "\x1b[34m************************\x1b[39m"
- "\x1b[34m**************************\x1b[39m"
- " "
- "          Bar[%d] : barIndex %d bufIndex %d"
- "     [%d] : Offset %lld length %lld"
- "     [%d] : Type %d nbrNe %d nbrOfLocalbarSetup %d"
- "     [%d] : Type %d startAddr 0x%x endAddr 0x%x Size %x nbrNe %d nbrOfLocalbarSetup %d"
- "     [%d] : format %d isCompressed 0x%x len 0x%llx offset %llx"
- "     aneMapping[%d] : %d"
- "     nBuf %d inputEvent %d priority %d uuid 0x%llx"
- "   %6u : [P:%d, %s] -- [T:%d, %s] -> ERROR: %s\n"
- "   %6u : [P:%d, %s] -- [T:%d, %s] -> [S:%d, %s]\n"
- "   %6u : [P:%d, %s] -- [T:%d] -> ERROR: WRONG EVENT\n"
- "  %s : There no state transitions\n"
- "  %s [%p]: Last %zu transitions [total = %zu]:\n"
- " %d : handle 0x%x offset 0x%lx len 0x%lx with Remap count %d\n"
- " %d : handle 0x%x offset 0x%lx len 0x%lx with map count %d\n"
- " %d [%#x]"
- " %p"
- " %s: event (%d, %s)"
- " %s: event (%d, %s), rc = %d [%#x]"
- " %s: event=%d [%s] cb %s"
- " Acquired %p"
- " Acquiring %p"
- " Released %p"
- " To release %p"
- "!(pageWiringOn && forceWiring)"
- "!bSubNetworkCustomExecuteOrder"
- "!commandBufPhysAddr"
- "!endPointCb[pCmd->endPointId].shareMem.item[i].used"
- "!pEntry->child"
- "!reader"
- "%-30s %-16.4f %-16lld %-16lld %-8lld\n"
- "%-30s %-16s %-16s %-16s %-8s\n"
- "%-30s %-6s %-8.4f %-8.4f\n"
- "%-30s %-6s %-8.4f %-8s %-10.4f %-16lld %-16lld %-8lld\n"
- "%-30s %-6s %-8s %-8.4f %-10.4f %-16lld %-16lld %-8lld\n"
- "%-30s %-6s %-8s %-8s %-10.4f %-16lld %-16lld %-8lld\n"
- "%-30s %-6s %-8s %-8s %-10s %-16s %-16s %-8s\n"
- "%d : buf %p size 0x%lx index 0x%x\n"
- "%lld delay trigger, %lld ignored due to exceeded execTimestamp"
- "%s : *** ACK: Endpoint command %d with ticket %u seq %u\n"
- "%s : *** endPoint %d cmd %d ack 0x%x ack_rc 0x%x ticket %u seq %u\n"
- "%s : Configure pCmd endPointId = %d\n"
- "%s : Free Shared Memory endPointId = %d at %p\n"
- "%s : Get EndPoint Status %d\n"
- "%s : Get Outstanding Ticket Cnt %d\n"
- "%s : Malloc Shared Memory endPointId = %d\n"
- "%s : SAP Register endPointId = %d sapId = 0x%x\n"
- "%s : SAP UnRegister endPointId = %d sapId = 0x%x\n"
- "%s : Send Buf endPointId %d sapId 0x%x %d\n"
- "%s : Unset pCmd endPointId = %d\n"
- "%s : valid %d bufIndex %d type %d addr 0x%llx memType %d size %lld tag %llx"
- "%s: (%d, %s): [%d, %s]->[%d, %s]"
- "%s: CH = %zu START"
- "%s: CH = %zu STOP"
- "%s: GOING TO STOP"
- "%s: SETUP"
- "%s: START"
- "%s: STOP"
- "%s: TEARDOWN"
- "(%s) %s\n"
- "(((size_t)(blockArray[dBlock])) % alignment[dBlock]) == 0"
- "((size_t)pointer) < ((size_t)(h->pMsg)) + h->queueDepth * sizeof(struct ffwInterProcMsg)"
- "((size_t)pointer) >= ((size_t)(h->pMsg))"
- "((uintptr_t)entry->stack & (RTK_CRT_STACK_ALIGNMENT - 1)) == 0"
- "(*parent == logDepth) || (*parent == index)"
- "(*parent == logDepth) || (*parent == pEntry->parent)"
- "(FFWMUTEX)0 != lock"
- "(IOP_RINGBUFFER_VERSION == (pBuf->_header._version>>16)) || (IOP_RINGBUFFER_VERSION_V2 == (pBuf->_header._version>>16))"
- "(SEMA)0 != cmd.syncCmdSema"
- "(callback == NULL) || (user_signal == 0)"
- "(ffwQueueCount (queue) == 0) || (((size_t) ffwQueueCount (queue)) == buffers)"
- "(idx >= 0) && (idx < (mNumEntriesPerPool * mMaxPoolNum))"
- "(idx >= 0) && (idx < hash_entries_num)"
- "(inputs > 0) || (outputs > 0)"
- "(mCurrPoolNum + pool_num) <= mMaxPoolNum"
- "(new_end & HEAP_OFFSET) == 0"
- "(operation == LOG_OPERATION_WIRED) || (operation == LOG_OPERATION_UNWIRED)"
- "(pCmd->pBufIndex[i] & ~maskRemapIndex) < sizeof(endPointCb[pCmd->endPointId].shareMem.remap)/sizeof(endPointCb[pCmd->endPointId].shareMem.remap[0])"
- "(pCmd->pBufIndex[i]) < sizeof(endPointCb[pCmd->endPointId].shareMem.item)/sizeof(endPointCb[pCmd->endPointId].shareMem.item[0])"
- "(size_t) ffwQueueCount (queue) == available"
- "(size_t)source < INTERRUPT_SRC_TOTAL"
- "(stacksize & (RTK_CRT_STACK_ALIGNMENT - 1)) == 0"
- "*extra_heap_size >= extra_heap_size_min"
- "*idx < CTASKPOOL_MAXTASK_HIST_ENTRIES"
- "*indexOut == logDepth"
- "*outsize <= maxOutsize"
- "*outsize >= sizeof(struct sCSneCmdPrintEnable)"
- "*print_buffer_base != 0"
- "*sm_base != 0"
- "*sm_size != 0"
- "-----------interval------------\n"
- "./ffw64_rtxc/ffw/CBuffer.cpp"
- "./ffw64_rtxc/ffw/CBufferPool.cpp"
- "./ffw64_rtxc/ffw/CBufferPoolStatic.cpp"
- "./ffw64_rtxc/ffw/CChannelManager.cpp"
- "./ffw64_rtxc/ffw/CController.cpp"
- "./ffw64_rtxc/ffw/CExpandablePool.cpp"
- "./ffw64_rtxc/ffw/CFifo.cpp"
- "./ffw64_rtxc/ffw/CFilter.cpp"
- "./ffw64_rtxc/ffw/CGPIOManager.cpp"
- "./ffw64_rtxc/ffw/CHashTable.cpp"
- "./ffw64_rtxc/ffw/CIPSynchro.cpp"
- "./ffw64_rtxc/ffw/CInterruptBuffer.cpp"
- "./ffw64_rtxc/ffw/CLatencyProfiler.cpp"
- "./ffw64_rtxc/ffw/CList.cpp"
- "./ffw64_rtxc/ffw/CLoggerInterProcessor.cpp"
- "./ffw64_rtxc/ffw/CLoggerSharedBuffer.cpp"
- "./ffw64_rtxc/ffw/CMMU.cpp"
- "./ffw64_rtxc/ffw/CMMULoggerPA.cpp"
- "./ffw64_rtxc/ffw/CMMULoggerVA.cpp"
- "./ffw64_rtxc/ffw/CMultiFilter.cpp"
- "./ffw64_rtxc/ffw/CObject.cpp"
- "./ffw64_rtxc/ffw/CObjectTree.cpp"
- "./ffw64_rtxc/ffw/CPipe.cpp"
- "./ffw64_rtxc/ffw/CPool.cpp"
- "./ffw64_rtxc/ffw/CRoot.cpp"
- "./ffw64_rtxc/ffw/CSharedMemory.cpp"
- "./ffw64_rtxc/ffw/CSignalPool.cpp"
- "./ffw64_rtxc/ffw/CTerminalOut.cpp"
- "./ffw64_rtxc/ffw/CTimeProfiler.cpp"
- "./ffw64_rtxc/ffw/ffwCRC.cpp"
- "./ffw64_rtxc/ffw/rtkit/CDebugAgent.cpp"
- "./ffw64_rtxc/ffw/rtkit/CEnvironment.cpp"
- "./ffw64_rtxc/ffw/rtkit/CISRManager.cpp"
- "./ffw64_rtxc/ffw/rtkit/CMailboxPool.cpp"
- "./ffw64_rtxc/ffw/rtkit/CQueuePool.cpp"
- "./ffw64_rtxc/ffw/rtkit/CRTOSObjectPool.cpp"
- "./ffw64_rtxc/ffw/rtkit/CResourcePool.cpp"
- "./ffw64_rtxc/ffw/rtkit/CScopedLock.cpp"
- "./ffw64_rtxc/ffw/rtkit/CSemaphorePool.cpp"
- "./ffw64_rtxc/ffw/rtkit/CSharedMemoryHeap.cpp"
- "./ffw64_rtxc/ffw/rtkit/CSharedMemoryHost.cpp"
- "./ffw64_rtxc/ffw/rtkit/CTaskPool.cpp"
- "./ffw64_rtxc/ffw/rtkit/CTimerManager.cpp"
- "./ffw64_rtxc/ffw/rtkit/CTimerPool.cpp"
- "./ffw64_rtxc/ffw/rtkit/CTraceEventBuffer.cpp"
- "./ffw64_rtxc/ffw/rtkit/ffwSharedMemory.cpp"
- "./ffw64_rtxc/platform/common/CFakeChannel.cpp"
- "./ffw64_rtxc/platform/common/CIPSynchroFake.cpp"
- "./ffw64_rtxc/platform/common/ChannelTable.cpp"
- "./ffw64_rtxc/platform/common/FakeChannelTable.cpp"
- "./ffw64_rtxc/platform/theia/rtkit/CPlatformEnvironment.cpp"
- "./ffw64_rtxc/platform/theia/rtkit/CPlatformGPIOManager.cpp"
- "./ffw64_rtxc/platform/theia/rtkit/CPlatformISRManager.cpp"
- "./ffw64_rtxc/platform/theia/rtkit/RealChannelTableTarget.cpp"
- "./sne/drivers/CDeviceDriver.cpp"
- "./sne/drivers/FE/CConfigDrvH11.cpp"
- "./sne/ssi/src/rtxc/sema.cpp"
- "0 < mpGroupBufCnt[group]"
- "0 == ((size_t)virtualAddr & wiringPageMask)"
- "0 == (physicalAddr & wiringPageMask)"
- "0 == matched || 1 == matched"
- "0 == mpGroupBufCnt[group]"
- "0 == ret"
- "0/1"
- "1"
- "21:15:31"
- "<=== CMMU_LOGGER_FFW_ASSERT from %s\n"
- "================="
- "===> CMMU_LOGGER_FFW_ASSERT from %s\n"
- ">>>>>>> Frame ID mismatch, expect: %lld, get: %lld"
- "ACK \"%s\""
- "ACTION"
- "AFPP load is not allowed after program setup done\n"
- "ALIGN_DOWN(pointer, CMMU::CacheLineSize()) == pointer"
- "ALL_CPU(%)"
- "ANE latency profiler already exists"
- "ANE latency profiler created"
- "ANE requestCallProc %zu"
- "ANE_PROPERTY_PRC Channel related logs are disabled"
- "ANE_PROPERTY_PRC Channel related logs are enabled"
- "ANE_PROPERTY_PRC wrong valid"
- "AddScheduleInfo"
- "AneVersionGet"
- "AvailableScheduleInfo"
- "BAR[%d] barIndex %d : bufferIndex %d"
- "Buf MSG: sapId 0x%x bufNbr %d subPacketSize %d\n"
- "Buf[%d] sz %lld type %d"
- "BufferProcessor"
- "CAneDebugEventsManager"
- "CAneServer"
- "CBufferPool::alignment != 0"
- "CBufferPool::blockArray != 0"
- "CBufferPool::size != 0"
- "CBufferPool::stride != 0"
- "CDMEDIABUSMANAGER_ENDPOINT_CMD_PING == pCmd->hdr.cmd"
- "CDMEDIABUSMANAGER_ENDPOINT_CMD_REMAP == pCmd->hdr.cmd"
- "CDMEDIABUSMANAGER_ENDPOINT_CMD_SEND_BUF_MSG == pCmd->hdr.cmd"
- "CDMEDIABUSMANAGER_ENDPOINT_CMD_UNMAP == pCmd->hdr.cmd"
- "CDMediaBusManager"
- "CExpandablePool allocEntryIdx enter"
- "CExpandablePool allocEntryIdx exit idx %zu"
- "CExpandablePool expandPool enter expand pool num %d, mCurrPoolNum %d "
- "CExpandablePool expandPool exit mCurrPoolNum %d"
- "CExpandablePool freeEntryIdx enter idx %zu RefCount %d"
- "CExpandablePool freeEntryIdx exit idx %zu RefCount %d"
- "CExpandablePool freeEntryIdx free poolIdx %d, mCurrPoolNum %d"
- "CExpandablePool maximum pool num (%d) allowed already allocated"
- "CExpandablePool retain enter idx %zu RefCount %d"
- "CExpandablePool retain exit idx %zu RefCount %d"
- "CFakeChannel::chDescr"
- "CGPIOManager::Instance() != NULL"
- "CMMULoggerPA::hisEntry != 0"
- "CMMULoggerPA::logEntry != 0"
- "CMMULoggerVA::hisEntry != 0"
- "CMMULoggerVA::logEntry != 0"
- "CMMU_LOGGER_FFW_ASSERT:%d [%zu] PA = 0x%lx, length = 0x%zx\n"
- "CMMU_LOGGER_FFW_ASSERT:%d [%zu] vir = %p, length = 0x%zx\n"
- "CMailboxPool::Instance() != 0"
- "CPU num: %d\n"
- "CPU_0(%)"
- "CPU_1(%)"
- "CPU_ID"
- "CQueuePool::Instance() != 0"
- "CRPCClient is down"
- "CScopedLock"
- "CSemaphorePool::Instance() != 0"
- "CSharedMemory::Instance () != 0"
- "CTaskPool::Instance() != 0"
- "CTraceEventBuffer.cpp"
- "CWorkTaskCore"
- "CacheHandler (0x%llx) already removed from the list in the trigger ISR"
- "CallProcedure"
- "CallProcedure nbrOfCustomBars %d"
- "CallProcedure progId %d procId %d numIoBuffers %d"
- "CallProcedure progId %d procId %d numIoBuffers %d\n"
- "CallProcedure2"
- "ChannelCmd"
- "ChannelStarted"
- "ChannelStopped"
- "Cleanup complete. mpDataChainingStat at %p deallocated"
- "CmdAFPPLoad"
- "CmdAFPPUnload"
- "CmdAcknowledge"
- "CmdCpuLoadNotification"
- "CmdDataChainingEvent"
- "CmdDbgEvent"
- "CmdDsidEvent"
- "CmdErrorNotification"
- "CmdGetEndPointStatus"
- "CmdGetOutstandingTicketCnt"
- "CmdIpcEndpointSet"
- "CmdIpcEndpointUnset"
- "CmdIpcSharedMemoryFree"
- "CmdIpcSharedMemoryMalloc"
- "CmdPowerControl"
- "CmdProcessor"
- "CmdProgramEvent"
- "CmdProgramSetup"
- "CmdProgramUnsetup"
- "CmdPropertyAccess"
- "CmdRegSAP"
- "CmdReqProcessId"
- "CmdReqProgramId"
- "CmdResetNotification"
- "CmdReturnProcessId"
- "CmdReturnProgramId"
- "CmdSendBufMsg"
- "CmdUnRegSAP"
- "CpuLoadNotification"
- "Create"
- "Create,%lu,%s"
- "Data Chaining Latency for cacheReqIdx %d"
- "DataChainingProgramEvent"
- "DataProcessor"
- "DbgEvent"
- "Delete"
- "Delete,%lu,%s"
- "DeleteProgram"
- "DeleteRTGraphProgram"
- "DepriorDsid"
- "DirectPost"
- "DriverCmdSanityCheck : off"
- "DriverCmdSanityCheck : on"
- "DriverCmdSanityCheck TD/overflow : off"
- "DriverCmdSanityCheck TD/overflow : on"
- "Dummy network NID %d TD Complete event %lld"
- "Dummy network for NID %d TQ abort finished at %lld"
- "DumpAFPP"
- "EL"
- "END"
- "ENT: CFSM.cpp, "
- "ENT: CScopedLock.cpp, "
- "ENTER"
- "EVENT_DISP options:"
- "EXIT"
- "EXT: CFSM.cpp, "
- "EXT: CScopedLock.cpp, "
- "Enable TQs after Dummy network finish in TQ[%d]"
- "Enable TQs after letting TQ[%d] finish"
- "EndPoint %d sends the Ping Message\n"
- "EndPointUnset remap not by peer %d\n"
- "EndpointCmdPing"
- "EndpointCmdRemap"
- "EndpointCmdSendBufMsg"
- "EndpointCmdUnmap"
- "Entry %d"
- "Event %d nbrUsrD %d 22"
- "EventProcess"
- "FFWMSG_PAYLOAD_GET(pMsg) <= sizeof(struct ffwMsgBuffRef)"
- "FFWMSG_PAYLOAD_GET(pMsg) <= sizeof(struct ffwMsgCmd)"
- "FFWMSG_PAYLOAD_GET(pMsg) <= sizeof(struct ffwMsgData)"
- "FFW_INTERPROC_BUFF_ACK_FLAG_CHECK(extra) != 0"
- "FFW_INTERPROC_BUFF_EXCHANGE_FLAG_CHECK(param2)"
- "FFW_OK == ffwrc"
- "FSMSwitchNonSecure"
- "FSMSwitchSecure"
- "FSM_EVENT_EXELOOP_IN_SECURE"
- "FSM_EVENT_EXELOOP_START"
- "FSM_EVENT_EXELOOP_STOP"
- "FSM_EVENT_EXELOOP_SWITCH_FROM_SECURE"
- "FSM_EVENT_EXELOOP_SWITCH_TO_SECURE"
- "FSM_STATE_EXELOOP_IDLE"
- "FSM_STATE_EXELOOP_PAUSE"
- "FSM_STATE_EXELOOP_RUN"
- "FSM_STATE_EXELOOP_RUN_2_PAUSE"
- "Failed to map command buffer"
- "FileInfo %s failed"
- "Filewrite %p %zu bytes"
- "Filewrite %s %s"
- "Force Disable already set"
- "Generic : [%d] bufferIndex %d"
- "GetCacheReqEvent"
- "GetCmdBuf"
- "GetDirectProcCallEvent"
- "GetLastCommittedTDInfo"
- "GetPowerStatus"
- "GetProcInfo"
- "GetProgInfo"
- "GetTraceBuffer"
- "H11ISPInterruptMapping[(size_t)aispSource]->platformIntSrc != PLATFORM_INT_INVALID"
- "H17TunableManager"
- "HandleEventInt"
- "HandleMcwInt"
- "HandleStopTqInt"
- "Hash Node %lld"
- "Help"
- "IDLE"
- "IDLE_DEFAULT"
- "ID_GET_SOURCE(id) < INTERRUPT_SRC_TOTAL"
- "INVALID"
- "IOP nothing to read"
- "IOP read done: rtPtr %d wtPtr %d readCount %d"
- "IOP read init: rtPtr %d wtPtr %d msgLen %zu"
- "IOP wait for Read"
- "IOP write done: rtPtr %d wtPtr %d writeCount %d"
- "IOP write init: rtPtr %d wtPtr %d msgLen %zu (with header)"
- "IOP write: Message length too big"
- "IOP write: buffer overflow"
- "IOP write: buffer wrapup"
- "IOP write: pBuffer not initialized yet"
- "IOP write: register 0x%zx 0x%x"
- "ISR_ID_GET_BANK(id) < lines"
- "ISR_ID_GET_INDEX(id) < ISR_CALLBACK_MAX"
- "ISR_ID_GET_LINE(id) < ISR_REG_ENTRY"
- "In SendSecureModeRequest()\n"
- "Info"
- "InitCacheRequest"
- "InitProcedureCallCmds"
- "InitProcedureCallCustomBarsCmds"
- "Initialization"
- "InqTaskArg"
- "Invalid log operation"
- "IpcEndpointSet"
- "IpcEndpointUnset"
- "ItqIrqEnable"
- "Kernel : bufferIndex %d"
- "Key[%lld]: 0x%zx"
- "KickStartCe"
- "Load %s failed"
- "LoadProgramsInAFPP"
- "LogEnterVerbose"
- "MapTextSection"
- "Mar  7 2025"
- "Master asking to release the remap while it is still being used by local user\n"
- "NO trace buffer to post!"
- "NULL != clockToMicroSecondConvertFunc"
- "NULL != encode_handler[encodeScheme]"
- "NULL != entry"
- "NULL != instance"
- "NULL != nbytes"
- "NULL != pCmd"
- "NULL != pIpcRingBufferIn[pCmd->endPointId]"
- "NULL != pIpcRingBufferOut[pCmd->endPointId]"
- "NULL != pMsg"
- "NULL != pResourceIndex[endPoint]"
- "NULL != pResourceIndex[pCmd->endPointId]"
- "NULL != pTaskHistoryHead"
- "NULL != physical_addr"
- "NULL != ppReadBufferAddr"
- "NULL != ppWriteBufferAddr"
- "NULL != semalist"
- "NULL != semaphore"
- "NULL != timeCodeGetFunc"
- "NULL != timestampFrequencyFunc"
- "NULL != virtualAddr"
- "NULL == instance"
- "NULL == mpGroups[group][j].buf && STATE_RELEASED == mpGroups[group][j].state"
- "NULL == pHandler"
- "NULL == pIpcRingBufferIn[pCmd->endPointId]"
- "NULL == pIpcRingBufferOut[pCmd->endPointId]"
- "Need dummy for TQ[%d]S[%d], b_queue_dummy_network %d"
- "Notify score %u\n"
- "Overflow detected in dram event log: programId %d processId %d procedureId %d"
- "POST CONDITION: "
- "POWEROFF"
- "POWERON"
- "PRE CONDITION: "
- "PROCESSING"
- "ParseTD"
- "PerfMode : off"
- "PerfMode : on"
- "Performance"
- "Phase %d: %dus (avg %9.6fus, std sq %9.6fus statsCount %d)"
- "PiningThreadsTotal: "
- "PostCallback"
- "PostCmd"
- "PowerControl"
- "PowerDown"
- "PowerUp"
- "PowerUpByState"
- "PreMapProcessStatsBuf"
- "PrintBufDesc"
- "PrintDescriptorProp"
- "PrintGeneric"
- "PrintKernelProp"
- "PrintOperation"
- "PrintProcedure"
- "ProcessEndpointCmd"
- "ProcessSubPacket"
- "ProgramEvent"
- "PropertyWrite"
- "Queue dummy network using NID %d Q[%d]S[%d] at %lld"
- "RESET"
- "ROUND_DOWN(paddr, CMMU::CacheLineSize()) == paddr"
- "RPC Id is 0x%x\n"
- "RPC read file size as %zu"
- "RTK_ST_IS_SUCCESS(rc)"
- "RTK_ST_OK == ret"
- "RTK_queue_count(queue) == tot"
- "RTK_vm_map_memory failed for 0x%llx length 0x%zu\n"
- "RTK_vm_unmap failed\n"
- "Read %s done %zu bytes"
- "ReadMessage"
- "Received Signal %p\n"
- "Received an program whose has 0 operation : %d"
- "Received an program whose procedure has invalid operation Index : %d vs %d"
- "RegisterClient"
- "ReloadTunables"
- "Remap :  handle 0x%x : base %p : len 0x%lx\n"
- "RemoveScheduleInfo"
- "Report Debug Event : Debug Event %d count %d (tid:%d)"
- "Reset"
- "ReturnCacheReqEvent"
- "ReturnDirectProcCallEvent"
- "RunProc"
- "RunProc2"
- "RunProcCacheRequest"
- "RunProcInternal"
- "START"
- "STOP"
- "STREAM"
- "STREAM_CMD_APPLY"
- "STREAM_CMD_APPLY_NOW"
- "STREAM_IDLE"
- "STREAM_IDLE_DEFAULT"
- "STREAM_INSTANDBY"
- "STREAM_OFF"
- "STREAM_PROCESSING"
- "STREAM_RESET"
- "STREAM_SETUP"
- "STREAM_STANDBY"
- "STREAM_START"
- "STREAM_STOP"
- "STREAM_TEARDOWN"
- "SUCC"
- "SVC"
- "SaveProcedureCall"
- "SaveRunToTdStop"
- "SaveStatsBuffer"
- "SaveToFile"
- "Segment : bufferIndex %d"
- "SendBufMsg"
- "SendCall"
- "SendHWRequest"
- "SendMsg : endPointId %d sapId 0x%x subPacket %p subPacketSize %d\n"
- "SendSecureModeRequest"
- "SetPMUBaseAddress"
- "SetProgram"
- "SetTQState"
- "Setting high watermark to %u\n"
- "Setting low watermark to %u\n"
- "Setting poll interval to %u seconds\n"
- "Setting threshold to %u ticks\n"
- "Setup complete. mpDataChainingStat at %p allocated"
- "SetupEngineRequest"
- "SetupExecute"
- "Started"
- "StatsBuf sz %lld type %d"
- "Stopped"
- "Suspend TQs for Dummy Network"
- "SwitchExclaveMode"
- "TD : bufferIndex %d"
- "TQ[%d] reqRunningStatus 0x%x"
- "Task"
- "TaskArg not found"
- "TearDownExecute"
- "TerminateCacheRequest"
- "TerminateProcess"
- "Thread time"
- "Total Abort : Raise Priority %d TQ Abort %d"
- "Total Process create/terminate : %d/%d"
- "Total Program add/delete       : %d/%d"
- "Total Scheduled Run : %d (failed %d)"
- "Total finished  Run : %d"
- "TracePost2Host"
- "TransitionProcess"
- "UnMapTextSection"
- "UnRemap :  handle 0x%x : base : %p len : 0x%lx\n"
- "UnsetMem : %p 0x%lx 0x%x\n"
- "UnsetRemap : %p 0x%lx 0x%x\n"
- "WireShared"
- "WriteMessage"
- "Writer regAddr 0x%lx regValue 0x%x\n"
- "[%d]: intermediate spill bar id %d, dsid 0x%llx"
- "[%d]: prefetch bar id %d, dsid 0x%llx"
- "[%s]  CMD = %#04x [%s] at %lld : type = 0x%x addr = %p, size = %d \n"
- "[%s] CMD = %#04x [%s] at %lld : enable=%d\n"
- "[%s] CMD = %#04x [%s] at %lld [0x%x]\n"
- "[0]: show options"
- "[1]: TD events sorted by TID"
- "[2]: TD events sorted by timestamp"
- "[3]: TD performance profiling"
- "[4]: show task switch event"
- "[5]: network performance profiling"
- "[ANE Exclave] Enter"
- "[ANE Exclave] Exit"
- "[ANE Power] down"
- "[ANE Power] up"
- "[AneCmd] Allocated processId %d for programId %d at %lld"
- "[AneCmd] Allocated processId %d for programId %d at %lld.\n"
- "[AneCmd] Allocated programId = %d at %lld"
- "[AneCmd] Allocated programId = %d at %lld."
- "[AneCmd] Returned programId = %d at %lld."
- "[AneCmd] Terminated processId %d for programId %d at %lld"
- "[AneCmd] Unloaded programId = %d at %lld"
- "[AneCmd] returned processId %d for programId %d at %lld."
- "[Desciptor prop Section] Total %d"
- "[Descriptor prop Section] X"
- "[Generic Section] X"
- "[Generic Section] maxAneUsed %d maxNe %d total Buf %d"
- "[Kernel Prop Section] Total %d"
- "[Kernel Prop Section] X"
- "[MessageBack] cmdId %d counter 0x%x - %dus (cache command # : %zu)"
- "[No] Generic Section"
- "[No] Operation Section"
- "[No] Procedure Section"
- "[No] Segment Prop Section"
- "[No] Segment Section"
- "[OPERATION Section] Total %d"
- "[OPERATION Section] X"
- "[POST] cmdId %d counter 0x%x"
- "[POST] cmdId %d counter 0x%x => Trace # %d"
- "[PROCEDURE Section] Total %d"
- "[PROCEDURE Section] X"
- "[TestCond] ASSERTION is set"
- "[TestCond] Cmd_Timeout is set"
- "[WRN] Exeloop cmd %d latency %dus"
- "[X] kernelPropSection is valid but no buffer!"
- "[X] kernelSection is valid but no buffer!"
- "[X] verifyBAR"
- "[X] verifyDescriptorPropSection"
- "[X] verifyDescriptors"
- "[X] verifyGenericSection"
- "[X] verifyKernelPropSection"
- "[X] verifyOperationSection"
- "[X] verifyProcedureSection"
- "[ipc] Send %llu"
- "[ipc] callProc Cb %llu"
- "[ipc] pCb %llu"
- "_AneCallBack"
- "_maskUnmaskMutex != (FFWMUTEX)0"
- "actionbuf.bin"
- "addDbgEvent"
- "addEntry"
- "addr != NULL"
- "alignment != 0"
- "allocDbgEventIdx"
- "allocEntryIdx"
- "allocL2SpillBufferIdx"
- "allocatedPoolAddr[i] != NULL"
- "appPriorityToFwPriority"
- "array != 0"
- "arrayEmptyBuffer != 0"
- "array[index].ch != 0"
- "array[index].ch == 0"
- "array[index].inuse == false"
- "available == tot"
- "bGroupInUse[%d] %d"
- "b_found == false"
- "blockArray != 0"
- "blocks <= CBuffer::idTot"
- "bootArgs != 0"
- "buf %d: addr 0x%llx size %lld"
- "bufMsg->hdr.len <= sizeof(msg)"
- "bufNbr <= maxAneIpcBufMsg"
- "buffPointer"
- "buffPool != 0"
- "bufferLen == 0"
- "bufferLen > sizeof(sIOPRingBuffer_t)"
- "buffers != 0"
- "buffers <= FFW_INTERPROC_BUFF_TOT"
- "bundledBlocks <= CBuffer::idTot"
- "bundledBlocksIn <= CBuffer::idTot"
- "cachedAddr != 0"
- "calcTriggerUsDelay"
- "ch != 0"
- "chMan != 0"
- "chManH2T != 0"
- "chTot <= ISP_CAMERA_CHANNEL_TOT"
- "channel < inchannels"
- "channelBufferSize != 0"
- "channelPhys != 0"
- "channelTotal != 0"
- "channel_mem != NULL"
- "checkBarEachAneOp"
- "checkRunningSlotsAfterAbort"
- "checkpointId < mMaxCheckpoints"
- "cmdBuffer_mem != 0"
- "cmdDataCheck"
- "cmdInternalSema != (SEMA)0"
- "cmdMbox != (MBOX)0"
- "cmdMboxSema != (SEMA)0"
- "cmdSema != (SEMA)0"
- "cmdSynchronizationSema != (SEMA)0"
- "context != NULL"
- "count"
- "create writeRingBufferLen %d with writeRingBufferAddr at 0x%lx %d\n"
- "createCacheRequest"
- "curEntry"
- "dPrio != 0"
- "dPrio % 2 == 0"
- "dPrio <= 124"
- "dPrio <= RTK_THREAD_PRIORITY_MAX"
- "dPrio >= RTK_THREAD_PRIORITY_MIN"
- "dataBufSize == pBuf->_header._size"
- "dataChainingRecycleOutput"
- "dataChainingTrigger"
- "dataChainingTriggerIsr"
- "decPendingExeLoopCmdCnt"
- "deferredCmdAck == false"
- "delay trigger[%lld]: execTimestamp %lld cmdHandleTimestamp %lld"
- "deleteCacheRequest"
- "depriorDsid"
- "descr.indexList != 0"
- "descr.list != 0"
- "descr.lock != (FFWMUTEX)0"
- "dieRequest != (SEMA)0"
- "dieRequest != 0"
- "dieSema != (SEMA)0"
- "dispDataChainingLatency"
- "dummy return\n"
- "duty : %u %\n"
- "enableEventLogInNetworkDesc"
- "endPoint < maxEndpoint"
- "endPointCb[endPoint].shareMem.nbrOfRemapItem < sCDMediaBusManagerShareMemInfo::maxSharedMemInfo"
- "endPointCb[i].curState < ECDMEDIABUSMANGER_ENDPOINT_CB_STATE_MAX"
- "endPointCb[pCmd->endPointId].curState != ECDMEDIABUSMANGER_ENDPOINT_CB_STATE_IDLE"
- "endPointCb[pCmd->endPointId].curState < ECDMEDIABUSMANGER_ENDPOINT_CB_STATE_MAX"
- "endPointCb[pCmd->endPointId].shareMem.nbrOfItem"
- "endPointCb[pCmd->endPointId].shareMem.nbrOfItem < sCDMediaBusManagerShareMemInfo::maxSharedMemInfo"
- "endPointCb[pCmd->endPointId].shareMem.nbrOfItem == 0"
- "endPointCb[pCmd->endPointId].shareMem.nbrOfRemapItem"
- "endPointCb[pCmd->endPointId].shareMem.nbrOfRemapItem == 0"
- "endPointCb[pCmd->endPointId].shareMem.remap[i].refCount==0"
- "endPointId < maxEndpoint"
- "entries != 0"
- "entries > 0"
- "entries_per_pool > 0"
- "entry != 0"
- "entry != NULL"
- "entry->callback || entry->callback_with_source"
- "entry->stack != 0"
- "entry->used == true"
- "entryList != 0"
- "entry_size > 0"
- "exe_interval(%)"
- "execution(us)"
- "expandPool"
- "extra_heap_virt != NULL"
- "ffwQueueCount (queue) == 0"
- "ffwrc == FFW_OK"
- "fileDescs[i].pData != nullptr"
- "fileDescs[i].size == fileDescs[i].sizeRef"
- "fileLen"
- "fileWrite"
- "filter == (class CObject *)0"
- "fiq(us)"
- "found"
- "freeEntryIdx"
- "freeL2SpillBuffIdx"
- "freeUnusedL2SpillBufferPool"
- "freeUnusedPool"
- "func != 0"
- "getActionProperty"
- "getCacheReqPendingCmdCnt"
- "getCacheReqState"
- "getCacheRequestInfo"
- "getCacheRequestIoBuffers"
- "getCacheRequestIoBuffersNbr"
- "getCacheRequestSignalEvents"
- "getDataChainingInputInfo"
- "getFileSize"
- "getL2SpillBufferAddr"
- "getNbrOfTd"
- "getNetworkDescBufAddr"
- "getProcedureCallType"
- "getRequestId"
- "getReservedNetworkDesc"
- "gpTimerArray != 0"
- "gpTimerArray[0] != 0"
- "group < MAX_ASYNCBUFFERS_GROUPS"
- "h"
- "h != 0"
- "h->ch != 0"
- "h->chH2T != 0"
- "h->chT2H != 0"
- "h->managed == 0"
- "h->signature == CFSM_SIGNATURE"
- "h2tchIOMan != 0"
- "handle != 0"
- "handle != NULL"
- "handleAbortCacheRequest"
- "handleAbort_abortRaisePriority"
- "handleCallProcedureWithBar"
- "handleCmdChannel"
- "handleDelayedTriggerCmd"
- "handleInferenceCall_inThread"
- "handleInvalidSingleUseCacheRequest"
- "handleIpcEndpointCmd"
- "handlePendingCmd"
- "handler == memHandler"
- "handshake_info != NULL"
- "hashNodeIdxMutex != (FFWMUTEX)0"
- "hash_table_size > 0"
- "head == 0"
- "heapSize != 0"
- "heap_resource != (FFWMUTEX)0"
- "heap_resource != 0"
- "i <= 1000"
- "id < max"
- "id >= 0 && id < CDMEDIABUSMANAGER_CMD_COMMON_TOT"
- "idx != 0"
- "inUseList == 0"
- "incPendingExeLoopCmdCnt"
- "index < entries"
- "index < tot"
- "index == pEntry->parent"
- "index >= 0"
- "indexOfGroup < MAX_ASYNCBUFFERS_IN_GROUP"
- "info"
- "initDbgEventMem"
- "initSharedEvents"
- "inputPipe != 0"
- "inputPipeEnable != nullptr"
- "insize != CCONTROLLER_INVALID_SHARED_INSIZE"
- "insize == sizeof(struct sCSneCmdPrintEnable)"
- "instance != 0"
- "instance != NULL"
- "instance == 0"
- "instance == NULL"
- "instance == nullptr"
- "instance->ch != 0"
- "instance->chT2H != 0"
- "internalCmdListMutex_ != (FFWMUTEX)0"
- "interrupt(us)"
- "interruptTimerSignal != 0"
- "iobuf0.bin"
- "iobuf1.bin"
- "iobuf2.bin"
- "irqLine != 0"
- "isAneIdle"
- "isCacheReqInUse"
- "isCacheReqSingleUse"
- "isCacheReqValid"
- "isHWReady"
- "isrHandle"
- "isrhandle != 0"
- "it"
- "list == 0"
- "loadMonitorTask != RTK_THREAD_NONE"
- "lock != (FFWMUTEX) 0"
- "lock != nullptr"
- "log != 0"
- "logCmdData"
- "logDepth > 0"
- "logEntry"
- "logRecvCmdAck"
- "logTot <= logDepth"
- "mLatencyStat.maxEntryNum > 0"
- "mLatencyStat.pCheckpoint"
- "mLatencyStat.pCheckpoint[i]"
- "mLatencyStat.pLatency"
- "mLatencyStat.pLatency[i]"
- "mMaxCheckpoints > 0"
- "mMutex != (RESOURCE)0"
- "mask cmd : address = 0x%x, actual address = 0x%x\n"
- "mask cmd : reg addr = 0x%x, data = 0x%x"
- "mask cmd : size = 0x%x\n"
- "maskCount[aispSource] > 0"
- "maxBuff != 0"
- "max_hash_entries > 0"
- "max_pool_num > 0 && max_pool_num <= MAX_EXPANDABLE_POOL_NUM"
- "maxchannels != 0"
- "maxmbox > 0"
- "maxqueue > 1"
- "maxres > 0"
- "maxsema > 0"
- "maxsig > 0"
- "maxtask > 1"
- "maxtimers > 0"
- "mboxPool != 0"
- "mboxPool == 0"
- "memory != 0"
- "message != NULL"
- "messages > 0"
- "mmu"
- "mmuLoggerOn == true"
- "mpEntryIdxRefCount"
- "mpEntryIdxRefCount[idx] == 0"
- "mpEntryIdxRefCount[idx] > 0"
- "mpGroupBufCnt[%d] %d"
- "mpGroupsOwnerName[%d] %s"
- "mpPoolInfo"
- "mpPoolInfo[mFirstUnusedPoolIdx].pIndexPool != NULL"
- "mpPoolInfo[mFirstUnusedPoolIdx].pPoolBaseAddr == NULL"
- "mpPoolInfo[poolIdx].pIndexPool != NULL"
- "mpPoolInfo[poolIdx].valid != 0"
- "msgHandler"
- "msgLen > 0"
- "msgPhys != 0"
- "mutex != (FFWMUTEX) NULL"
- "mutex != (RESOURCE) 0"
- "myDbg"
- "myProcCb"
- "nBytes != NULL"
- "name != 0"
- "napCount == 0"
- "nbrOfRemapLeft == endPointCb[pCmd->endPointId].shareMem.nbrOfRemapItem"
- "newState < ECDMEDIABUSMANGER_ENDPOINT_CB_STATE_MAX"
- "newTask != RTK_THREAD_NONE"
- "new_end > new_start"
- "newrdptr <= pBuf->_header._size"
- "object != 0"
- "object != NULL"
- "ok == true"
- "operationbuf.bin"
- "outputAddr && outputSize"
- "outputPipe != 0"
- "outsize != 0"
- "outstanding"
- "outstanding <= entries"
- "outstanding == 0"
- "owner != 0"
- "pAddr != NULL"
- "pAneLatencyProfiler != __null"
- "pBuf->_header._rdptr + sizeof(sIOPRingBufferMsgHeaderV2_t) < pBuf->_header._wrptr"
- "pBuf->_header._rdptr + sizeof(sIOPRingBufferMsgHeader_t) < pBuf->_header._wrptr"
- "pBufAddr && pBufSize && pBufIndex"
- "pBufAddr[i] && pBufSize[i]"
- "pBuffMsg->buffers <= FFW_INTERPROC_BUFF_TOT"
- "pCmd != NULL"
- "pCmd->bufNbr <= maxAneIpcBufMsg"
- "pCmd->pSubPacket"
- "pCmd->sharedMemIndex < sCDMediaBusManagerShareMemInfo::maxSharedMemInfo"
- "pData"
- "pEntry->parent != index"
- "pEntry->parent < logDepth"
- "pEntry->parent == index"
- "pEntry->physicalAddr"
- "pEntry->refCount"
- "pEntry->virtualAddr"
- "pExchange->buffers > 0"
- "pInternalCmdArray_"
- "pInternalCmdFreeList_"
- "pInternalCmdList_"
- "pItem->bufferRefCount"
- "pItem->pBase == pCmd->sharedMemPtr"
- "pItem->used"
- "pMMULogger != NULL"
- "pMMULogger == NULL"
- "pMsg"
- "pMsg != 0"
- "pMyMsg->id == FFW_INTERPROC_MSG_EXCHANGE"
- "pNodeData != NULL"
- "pPoolAddrToFree[i] != NULL"
- "pRingBuffer != 0"
- "pSize != 0"
- "pStride != 0"
- "pSubPacket != NULL"
- "pTemp"
- "pTemp + pCmd->pBufSize[i] <= (size_t)pItem->pBase + pItem->memSize"
- "pTemp >= (size_t)pItem->pBase && pTemp <= (size_t)pItem->pBase + pItem->memSize"
- "pUserStr != 0"
- "param1 >= sizeof(struct ffwInterProcMsg)"
- "parent < logDepth"
- "parent == logDepth"
- "parent == pEntry->parent"
- "parentEntry->child"
- "parentEntry->physicalAddr"
- "parentEntry->virtualAddr"
- "parseOperation"
- "parseProc"
- "physicalAddr"
- "physicalAddr != (uintptr_t) -1"
- "pin < buffPools"
- "pin < inputs"
- "pin < outputs"
- "pin < portInputs"
- "pointer"
- "pointer != 0"
- "pointer != NULL"
- "pointer == VP(messagePhys)"
- "pool != (void *)0"
- "pool != 0"
- "pool == ALIGN_DOWN(pool, CMMU::CacheLineSize())"
- "poolArray != 0"
- "poolArray[container->attach.id] == 0"
- "poolArray[id] != 0"
- "poolBufferReceived != 0"
- "poolBufferReturned != 0"
- "poolIdx < mMaxPoolNum"
- "poolIdx >= 0 && poolIdx < mMaxPoolNum"
- "poolsizeIn >= CBufferPoolStatic::PoolSizeGet(buffers, newbundledBlocks, newsize, newalignment)"
- "port < inports"
- "powerUpAne"
- "powerUpAneStage1"
- "powerUpAneStage2"
- "print"
- "printCommandInfo"
- "printInfo"
- "printStats"
- "priority != 0"
- "priority <= RTK_THREAD_PRIORITY_MAX"
- "priority >= RTK_THREAD_PRIORITY_MIN"
- "processCmdOnly == true"
- "processedCmdCounter == 0"
- "processorEnter"
- "processorExit"
- "prog.tdProp.buf %p procValid %d"
- "programId 0x%x processId 0x%x nbrAneMapping %d"
- "programId 0x%x processId 0x%x procedureId 0x%x"
- "propertyWrite"
- "propertywrite 0x10A5 \x1b[32m1\x1b[39m : ANE stats"
- "propertywrite 0x10A5 \x1b[32m2\x1b[39m : enable command detail"
- "propertywrite 0x10A5 \x1b[32m3\x1b[39m : disable command detail"
- "propertywrite 0x10A5 \x1b[32m4\x1b[39m : enable program info detail"
- "propertywrite 0x10A5 \x1b[32m5\x1b[39m : disable program info detail"
- "propertywrite 0x10A5 \x1b[32m6\x1b[39m : enable TD info detail"
- "propertywrite 0x10A5 \x1b[32m7\x1b[39m : disable TD info detail"
- "propertywrite 0x10A5 \x1b[32m8\x1b[39m : enable TD Header info"
- "propertywrite 0x10A5 \x1b[32m9\x1b[39m : disable TD Header info"
- "pushToHW"
- "pushToHWDirect"
- "queue != (FFWQUEUE)0"
- "queueDepth > 1"
- "queuePool != 0"
- "queuePool == 0"
- "rc != NULL"
- "rc == 1"
- "rc == RTK_ST_OK"
- "rc >= 0"
- "rdptr + sizeof(sIOPRingBufferMsgHeaderV2_t) < localCopyWrPtr"
- "rdptr + sizeof(sIOPRingBufferMsgHeaderV2_t) < pBuf->_header._size"
- "rdptr + sizeof(sIOPRingBufferMsgHeader_t) < localCopyWrPtr"
- "rdptr + sizeof(sIOPRingBufferMsgHeader_t) < pBuf->_header._size"
- "reader"
- "recycleArray != 0"
- "ref%d/%s"
- "relocation cmd : X = 0x%x\n"
- "relocation cmd : address = 0x%x, actual address = 0x%x\n"
- "relocation cmd : barIdx = 0x%x\n"
- "relocation cmd : dataHi = 0x%x"
- "relocation cmd : dataLo = 0x%x"
- "relocation cmd : size = 0x%x\n"
- "reportDataChainingTriggerFailed"
- "reportFinishEvent"
- "reportStats"
- "resPool != 0"
- "resPool == 0"
- "ret == 0"
- "retain"
- "retain == CBuffer::suspended"
- "retainL2SpillBufferIdx"
- "returnRequestId"
- "rtkitSystemTaskList != 0"
- "sCSneCmdProcedureCall [%d] : bufferIndex %d"
- "saveToFile"
- "sema != 0"
- "sema != NULL"
- "sema == 0"
- "semaArray != (SEMA *)0"
- "semaArray[index] != (SEMA)0"
- "semaPool != 0"
- "semaPool == 0"
- "semaphore == (SEMA)0"
- "semaphore == h->signalT2H"
- "sendEnqueueEvt_prepareFinishEvt_inIsr"
- "sequential cmd : address = 0x%x, actual address = 0x%x\n"
- "sequential cmd : count = 0x%x\n"
- "sequential cmd : reg addr = 0x%x, data = 0x%x"
- "serialPollTimer[i] != 0"
- "serialPortPoolTimeOut[i] != (SEMA)0"
- "serialPortSignal[i] != (SEMA)0"
- "set buf[%d] 0x%llx zero sz %lld"
- "setCustomBars"
- "setDataChainingLatencyDisp"
- "setDataChainingLatencyDisp %d"
- "setDirectAneRequestInfo"
- "setEnableDynamicPowerGate"
- "setForceDisableCacheRequest"
- "setInitFlags"
- "setJobQueueId"
- "setPerfMode"
- "setResetMode"
- "setResetMode %d"
- "setStartTimestamp"
- "setTaskSwitchEventDisp"
- "setTaskSwitchEventDisp %d"
- "setupAneReq_inIsr"
- "setupCacheRequest"
- "setupDirectProcCallEvents"
- "setupEngineReqInternal"
- "setupNetworkDescriptor_withBars"
- "shAddr != NULL"
- "sharedEventsTrigger"
- "sharedEventsTriggerIsr"
- "sharedMem != 0"
- "shwdStatus == 0"
- "sigPool == 0"
- "signal != 0"
- "signalH2T != 0"
- "signalResetNotification"
- "signalSharedEvents"
- "signalT2H != 0"
- "size != 0"
- "size <= sizeof(pBuffMsg->extra)"
- "sizeInByte % 4 == 0"
- "sizeInByte > 0"
- "source < INT_NROF_VECTORS"
- "source < ISR_REG_ENTRY"
- "source < lines * ISR_REG_ENTRY"
- "source >= 0"
- "src != NULL"
- "stacksize != 0"
- "startInvalidateCacheRequestInExeLoop"
- "started == false"
- "statsBufferSizeGet"
- "status == FFW_OK"
- "status == RTK_ST_OK"
- "super::Available() == (int)super::Managed()"
- "switchToIsolatedMode"
- "syncCmdMutex_ != (FFWMUTEX)0"
- "synchronization != (SEMA)0"
- "synchronize != (SEMA)0"
- "task != (TASK)0"
- "task != 0"
- "taskId == self"
- "taskPool == 0"
- "taskTime != 0"
- "td size %zu while usedSize %d"
- "temp != 0"
- "this->buffers >= buffers"
- "threadHistoryLock != (FFWMUTEX) 0"
- "ticket < cmdDepth"
- "timerHandle != NULL"
- "timerSem != NULL"
- "token != 0"
- "tot != 0"
- "tot == 0"
- "tot > 0"
- "totalElapsed %lld or totalElapsedInterval %lld is invalid value\n"
- "totalElapsed(from tracekit) %lld, totalElapsedDuringCheckpoint %lld\n"
- "totalElapsedInterval(from tracekit) %lld, totalElapsedIntervalDuringCheckpoint %lld\n"
- "tqEnqueueReq_inIsr"
- "tree_resource != (FFWMUTEX)0"
- "tree_resource != 0"
- "unknown TD command type 0x%x"
- "updateAndEnqueueOneSegment"
- "updateDefSetting"
- "updateEngineRequestSegment"
- "updateStatsBufferData"
- "vPrintLock != (SEMA)0"
- "vPrintLock == (SEMA)NULL"
- "value != NULL"
- "verifyBAR"
- "verifyCustomBar"
- "verifyDescriptorPropSection"
- "verifyDescriptors"
- "verifyGenericSection"
- "verifyKernelPropSection"
- "verifyOperationSection"
- "verifyProcedure"
- "verifyProcedureSection"
- "verifyProgram"
- "virtualAddr"
- "virtualAddr != NULL"
- "waitTQIdle"
- "wiringPageSize == 0x4000"
- "write to overwrite ref%d/%s"
- "~CScopedLock"

```

#### rans.t8140.release.im4p

>  `rans.t8140.release.im4p`

```diff

 
   __TEXT.text_first: 0x4488
-  __TEXT.__text: 0x1c1400
-  __TEXT.shared: 0xd914
-  __TEXT.read: 0x6b14
-  __TEXT.__const: 0x5398
+  __TEXT.__text: 0x1c3070
+  __TEXT.shared: 0xdd00
+  __TEXT.read: 0x6e90
+  __TEXT.__const: 0x5418
   __TEXT.idle_hooks: 0x10
-  __TEXT.__cstring: 0x229a1
+  __TEXT.__cstring: 0x22c84
   __TEXT.__chain_starts: 0x0
   __TEXT.__constructor: 0x0
   __TEXT._rtk_mtab: 0x310

   __DATA._rtk_power: 0x160
   __DATA._rtk_patchbay: 0x3f3
   __DATA._rtk_tunables: 0x6a0
-  __DATA.__const: 0x1aa0
-  __DATA.__data: 0x6008
+  __DATA.__const: 0x1ab0
+  __DATA.__data: 0x6000
   __DATA._rtk_init_stack: 0x1000
   __DATA._rtk_irq_stack: 0x1000
   __DATA._rtk_exc_stack: 0x1000

   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__mod_init_func: 0x0
-  __DATA.core_globals: 0x156
+  __DATA.core_globals: 0x157
   __DATA.large_stacks: 0x20000
   __DATA.small_stacks: 0x2000
-  __DATA.__zerofill: 0x246248
+  __DATA.__zerofill: 0x246388
   Functions: 0
   Symbols:   0
-  CStrings:  3766
+  CStrings:  3775
 
CStrings:
+ " BandsTemp_getDeviceTemperatureAll -> %ums"
+ "2077.120.68.0.1"
+ "77.120.68.0.1~86"
+ "AppleStorageFirmware-2077.120.68.0.1~86"
+ "FADUMP: Dumping FA to memory..."
+ "FADUMP: ERROR! Couldn't assert asi device %d"
+ "FADUMP: ERROR! FA dump is disabled"
+ "FADUMP: ERROR! FA dump is not supported"
+ "FADUMP: ERROR! FA dump was already executed"
+ "FADUMP: ERROR! FAdump Init failed!"
+ "FADUMP: ERROR! Memory address is not 0x%x aligned!"
+ "FADUMP: ERROR! Memory size is not 0x%x aligned!"
+ "FADUMP: ERROR! Nand Discovery not completed"
+ "FADUMP: ERROR! No memory!"
+ "FADUMP: ERROR! No space in Util panic log for MSP FA"
+ "FADUMP: ERROR! RTK_mc_assume failed: %d"
+ "FADUMP: Error: failed to check if device %d is asserted"
+ "FADUMP: FA stored 0x%x"
+ "FADUMP: FA_AllocationSize: %d"
+ "FADUMP: FA_Init isEnabled: %d, Size: %d"
+ "FADUMP: Finalizing FA dump: magic 0x%x, crc 0x%x"
+ "FADUMP: Forcing assert on asi device %d"
+ "FADUMP: Found Prev Assert[%d][%d,%d,%d]"
+ "FADUMP: MSP FA size: %d"
+ "FADUMP: Possible data incoherency"
+ "FADUMP: WARNING! Compression buffer allocation failed."
+ "FADUMP: WARNING! Couldn't get fa size for asi device %d"
+ "FADUMP: WARNING! FA Mem Release failed. status: 0x%x"
+ "FADUMP: WARNING! Failed to compress MSP %d"
+ "FADUMP: WARNING! Failed to store ASI logger"
+ "FADUMP: WARNING! Failed to store FTL entry %d"
+ "FADUMP: WARNING! No space left to store MSP %d"
+ "FADUMP: WARNING! Not extracting asi logger. size %d, addr 0x%x"
+ "FADUMP: WARNING! failed to read FA data for asi device %d"
+ "FADUMP: comressed req:%d, SizeAvg %d"
+ "FADUMP: deflate failed. status %d, Sec left to store: %d"
+ "FADUMP: deflateEnd failed. status %d"
+ "FADUMP: deflateInit2 failed. status %d"
+ "MassScan: Pilot scan done on %d bands after %lld seconds, but can't exit early, because %d bands failed, need to continue to full scan"
+ "Set DC table ver %u by %s, has_thermal_throttling 0"
+ "Such status is not allowed for block scan read command"
+ "TT cross temp init"
+ "Tried to read feature bit %d but feature bits struct is not initialized"
+ "WARNING! RAID config changed: Old: %u New: %u"
+ "cross temp detected, band %u temp (%d,%d) read temp (%d,%d), opType %d, isNew %u"
+ "cross temp isQualityError, band %u, opType %u"
+ "cross temp thershold not set yet"
+ "e=0x%x"
+ "forced temperature: %d, core temp %d, enable %u, reset stats %u"
+ "fwp"
+ "host"
+ "thermal_throttle.c"
+ "wrong high threshold crossed %u %d %d"
+ "wrong low threshold crossed %u %d %d"
- " PreNandEng_getDeviceTemperature -> %ums"
- ".100.377.0.1~112"
- "2077.100.377.0.1"
- "AppleStorageFirmware-2077.100.377.0.1~112"
- "CTL cross temp detected on flow %d, lba %d opType %d, size %d shouldCount %d"
- "Dumping FA to memory..."
- "ERROR! Couldn't assert asi device %d"
- "ERROR! FA dump is disabled"
- "ERROR! FA dump is not supported"
- "ERROR! FA dump was already executed"
- "ERROR! FAdump Init failed!"
- "ERROR! Memory address is not 0x%x aligned!"
- "ERROR! Memory size is not 0x%x aligned!"
- "ERROR! Nand Discovery not completed"
- "ERROR! No memory!"
- "ERROR! No space in Util panic log for MSP FA"
- "ERROR! RTK_mc_assume failed: %d"
- "Error: failed to check if device %d is asserted"
- "FA stored 0x%x"
- "FA_AllocationSize: %d"
- "FA_Init isEnabled: %d, Size: %d"
- "Finalizing FA dump: magic 0x%x, crc 0x%x"
- "Forcing assert on asi device %d"
- "Found Prev Assert[%d][%d,%d,%d]"
- "MSP FA size: %d"
- "Possible data incoherency"
- "WARNING! Compression buffer allocation failed."
- "WARNING! Couldn't get fa size for asi device %d"
- "WARNING! FA Mem Release failed. status: 0x%x"
- "WARNING! Failed to compress MSP %d"
- "WARNING! Failed to store ASI logger"
- "WARNING! Failed to store FTL entry %d"
- "WARNING! No space left to store MSP %d"
- "WARNING! Not extracting asi logger. size %d, addr 0x%x"
- "WARNING! failed to read FA data for asi device %d"
- "comressed req:%d, SizeAvg %d"
- "deflate failed. status %d, Sec left to store: %d"
- "deflateEnd failed. status %d"
- "deflateInit2 failed. status %d"
- "done scan ET bands %u"
- "forced device temperature is: %d"
- "forced tunnel temperature is: %d"
- "must be blocking"
- "must be valid temperatute at this point"
- "reset temprature stats"

```

#### sptm.t8140.release.im4p

>  `sptm.t8140.release.im4p`

```diff

-392.102.1.0.0
+392.120.12.0.0
   __TEXT.__cstring: 0xe522
   __TEXT.__binname: 0x40
   __TEXT.__const: 0xb00
   __TEXT.__chain_starts: 0x78
   __DATA_CONST.__const: 0x68c8
   __LATE_CONST.__late_const: 0x5d660
-  __TEXT_EXEC.__text: 0x5078c
+  __TEXT_EXEC.__text: 0x5089c
   __LAST.__pinst: 0x8
   __DATA.__auth_ptr: 0x18
   __DATA.__data: 0x6
   __DATA.__common: 0x5810
   __DATA.__bss: 0x5c20
   __BOOTDATA.__data: 0x14000
-  Functions: 354
+  Functions: 355
   Symbols:   1
   CStrings:  1809
 

```

#### t8140pmp.im4p

>  `t8140pmp.im4p`

```diff

 
   __TEXT.__text: 0x3788c
-  __TEXT.__const: 0x235c
+  __TEXT.__const: 0x235a
   __TEXT.__cstring: 0x1540
   __TEXT._rtk_mtab: 0x5e8
   __TEXT.__constructor: 0x0

```


</details>

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 18.4 *(22E240)* | 621.1.15.10.7 |
| 18.5 *(22F5042g)* | 621.2.1.10.3 |

### Dylibs

#### 🆕 NEW (5)

- `/System/Library/PrivateFrameworks/CosmeticAssessment.framework/CosmeticAssessment`
- `/System/Library/PrivateFrameworks/NDOAPI.framework/NDOAPI`
- `/System/Library/PrivateFrameworks/NDOUI.framework/NDOUI`
- `/System/Library/PrivateFrameworks/SensorAccess.framework/SensorAccess`
- `/System/Library/PrivateFrameworks/SiriLocalization.framework/SiriLocalization`

#### ❌ Removed (5)

- `/System/Library/Assistant/Plugins/SurfStatusSync.assistantBundle/SurfStatusSync`
- `/System/Library/PrivateFrameworks/ConditionalEngineAppIntents.framework/ConditionalEngineAppIntents`
- `/System/Library/PrivateFrameworks/ConditionalEngineClient.framework/ConditionalEngineClient`
- `/System/Library/PrivateFrameworks/ConditionalEngineRuntime.framework/ConditionalEngineRuntime`
- `/System/Library/PrivateFrameworks/ConditionalEngineShared.framework/ConditionalEngineShared`

#### ⬆️ Updated (1390)

<details>
  <summary><i>View Updated</i></summary>

- [/System/Library/AccessibilityBundles/Moments.axbundle/Moments](DYLIBS/Moments.md)
- [/System/Library/AccessibilityBundles/Music.axbundle/Music](DYLIBS/Music.md)
- [/System/Library/AccessibilityBundles/Podcasts.axbundle/Podcasts](DYLIBS/Podcasts.md)
- [/System/Library/AccessibilityBundles/SpringBoard.axbundle/SpringBoard](DYLIBS/SpringBoard.md)
- [/System/Library/AccessibilityBundles/SwiftUI.axbundle/SwiftUI](DYLIBS/SwiftUI.md)
- [/System/Library/AccessibilityBundles/SystemApertureUI.axbundle/SystemApertureUI](DYLIBS/SystemApertureUI.md)
- [/System/Library/AccessibilityBundles/SystemStatusUI.axbundle/SystemStatusUI](DYLIBS/SystemStatusUI.md)
- [/System/Library/AccessibilityBundles/TextInputUI.axbundle/TextInputUI](DYLIBS/TextInputUI.md)
- [/System/Library/AccessibilityBundles/UIKit.axbundle/UIKit](DYLIBS/UIKit.md)
- [/System/Library/AccessibilityBundles/UserNotificationsUIKit.axbundle/UserNotificationsUIKit](DYLIBS/UserNotificationsUIKit.md)
- [/System/Library/AccessibilityBundles/VoiceTriggerUI.axbundle/VoiceTriggerUI](DYLIBS/VoiceTriggerUI.md)
- [/System/Library/Accounts/Notification/FindMyDeviceAccountNotificationPlugin.bundle/FindMyDeviceAccountNotificationPlugin](DYLIBS/FindMyDeviceAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/HomeKitAccountNotificationPlugin.bundle/HomeKitAccountNotificationPlugin](DYLIBS/HomeKitAccountNotificationPlugin.md)
- [/System/Library/Assistant/UIPlugins/SiriFindMyUIPlugin.siriUIBundle/Frameworks/SiriFindMyUI.framework/SiriFindMyUI](DYLIBS/SiriFindMyUI.md)
- [/System/Library/ControlCenter/Bundles/HomeControlCenterModule.bundle/HomeControlCenterModule](DYLIBS/HomeControlCenterModule.md)
- [/System/Library/ControlCenter/Bundles/HomeControlCenterSingleTileModule.bundle/HomeControlCenterSingleTileModule](DYLIBS/HomeControlCenterSingleTileModule.md)
- [/System/Library/CoreAccessories/PlugIns/Transports/USBHost.transport/USBHost](DYLIBS/USBHost.md)
- [/System/Library/Extensions/AppleSPU.kext/PlugIns/AppleSPULib.plugin/AppleSPULib](DYLIBS/AppleSPULib.md)
- [/System/Library/Extensions/AppleSPU.kext/PlugIns/GNSSPassthroughLib.plugin/GNSSPassthroughLib](DYLIBS/GNSSPassthroughLib.md)
- [/System/Library/Frameworks/AVFAudio.framework/AVFAudio](DYLIBS/AVFAudio.md)
- [/System/Library/Frameworks/AVKit.framework/AVKit](DYLIBS/AVKit.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vImage.framework/vImage](DYLIBS/vImage.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libBLAS.dylib](DYLIBS/libBLAS.dylib.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libBNNS.dylib](DYLIBS/libBNNS.dylib.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libLAPACK.dylib](DYLIBS/libLAPACK.dylib.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libSparse.dylib](DYLIBS/libSparse.dylib.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libSparseBLAS.dylib](DYLIBS/libSparseBLAS.dylib.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libvDSP.dylib](DYLIBS/libvDSP.dylib.md)
- [/System/Library/Frameworks/Accessibility.framework/Accessibility](DYLIBS/Accessibility.md)
- [/System/Library/Frameworks/ActivityKit.framework/ActivityKit](DYLIBS/ActivityKit.md)
- [/System/Library/Frameworks/AppIntents.framework/AppIntents](DYLIBS/AppIntents.md)
- [/System/Library/Frameworks/Assignables.framework/Assignables](DYLIBS/Assignables.md)
- [/System/Library/Frameworks/AudioToolbox.framework/AudioCodecs](DYLIBS/AudioCodecs.md)
- [/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox](DYLIBS/AudioToolbox.md)
- [/System/Library/Frameworks/AudioToolbox.framework/libAudioDSP.dylib](DYLIBS/libAudioDSP.dylib.md)
- [/System/Library/Frameworks/AudioToolbox.framework/libEmbeddedSystemAUs.dylib](DYLIBS/libEmbeddedSystemAUs.dylib.md)
- [/System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices](DYLIBS/AuthenticationServices.md)
- [/System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/Frameworks/AACClient.framework/AACClient](DYLIBS/AACClient.md)
- [/System/Library/Frameworks/BackgroundTasks.framework/BackgroundTasks](DYLIBS/BackgroundTasks.md)
- [/System/Library/Frameworks/BrowserEngineKit.framework/BrowserEngineKit](DYLIBS/BrowserEngineKit.md)
- [/System/Library/Frameworks/CFNetwork.framework/CFNetwork](DYLIBS/CFNetwork.md)
- [/System/Library/Frameworks/CallKit.framework/CallKit](DYLIBS/CallKit.md)
- [/System/Library/Frameworks/CarPlay.framework/CarPlay](DYLIBS/CarPlay.md)
- [/System/Library/Frameworks/Charts.framework/Charts](DYLIBS/Charts.md)
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
- [/System/Library/Frameworks/CoreML.framework/CoreML](DYLIBS/CoreML.md)
- [/System/Library/Frameworks/CoreMedia.framework/CoreMedia](DYLIBS/CoreMedia.md)
- [/System/Library/Frameworks/CoreMediaIO.framework/CoreMediaIO](DYLIBS/CoreMediaIO.md)
- [/System/Library/Frameworks/CoreMotion.framework/CoreMotion](DYLIBS/CoreMotion.md)
- [/System/Library/Frameworks/CoreServices.framework/CoreServices](DYLIBS/CoreServices.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight](DYLIBS/CoreSpotlight.md)
- [/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony](DYLIBS/CoreTelephony.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/CTParser.framework/CTParser](DYLIBS/CTParser.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterAWDMetrics.dylib](DYLIBS/libCommCenterAWDMetrics.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterBase.dylib](DYLIBS/libCommCenterBase.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterCommandDrivers.dylib](DYLIBS/libCommCenterCommandDrivers.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterKCommandDrivers.dylib](DYLIBS/libCommCenterKCommandDrivers.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterMCommandDrivers.dylib](DYLIBS/libCommCenterMCommandDrivers.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libSystemDetermination.dylib](DYLIBS/libSystemDetermination.dylib.md)
- [/System/Library/Frameworks/CoreText.framework/CoreText](DYLIBS/CoreText.md)
- [/System/Library/Frameworks/CoreVideo.framework/CoreVideo](DYLIBS/CoreVideo.md)
- [/System/Library/Frameworks/CreateML.framework/CreateML](DYLIBS/CreateML.md)
- [/System/Library/Frameworks/CreateMLComponents.framework/CreateMLComponents](DYLIBS/CreateMLComponents.md)
- [/System/Library/Frameworks/CryptoKit.framework/CryptoKit](DYLIBS/CryptoKit.md)
- [/System/Library/Frameworks/DeveloperToolsSupport.framework/DeveloperToolsSupport](DYLIBS/DeveloperToolsSupport.md)
- [/System/Library/Frameworks/DeviceActivity.framework/DeviceActivity](DYLIBS/DeviceActivity.md)
- [/System/Library/Frameworks/DeviceCheck.framework/DeviceCheck](DYLIBS/DeviceCheck.md)
- [/System/Library/Frameworks/EventKit.framework/EventKit](DYLIBS/EventKit.md)
- [/System/Library/Frameworks/EventKitUI.framework/EventKitUI](DYLIBS/EventKitUI.md)
- [/System/Library/Frameworks/ExposureNotification.framework/ExposureNotification](DYLIBS/ExposureNotification.md)
- [/System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation](DYLIBS/ExtensionFoundation.md)
- [/System/Library/Frameworks/FileProvider.framework/FileProvider](DYLIBS/FileProvider.md)
- [/System/Library/Frameworks/FinanceKit.framework/FinanceKit](DYLIBS/FinanceKit.md)
- [/System/Library/Frameworks/FinanceKitUI.framework/FinanceKitUI](DYLIBS/FinanceKitUI.md)
- [/System/Library/Frameworks/Foundation.framework/Foundation](DYLIBS/Foundation.md)
- [/System/Library/Frameworks/GroupActivities.framework/GroupActivities](DYLIBS/GroupActivities.md)
- [/System/Library/Frameworks/HealthKit.framework/HealthKit](DYLIBS/HealthKit.md)
- [/System/Library/Frameworks/HomeKit.framework/HomeKit](DYLIBS/HomeKit.md)
- [/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit](DYLIBS/IOKit.md)
- [/System/Library/Frameworks/IOSurface.framework/IOSurface](DYLIBS/IOSurface.md)
- [/System/Library/Frameworks/IdentityLookup.framework/IdentityLookup](DYLIBS/IdentityLookup.md)
- [/System/Library/Frameworks/ImageIO.framework/ImageIO](DYLIBS/ImageIO.md)
- [/System/Library/Frameworks/Intents.framework/Intents](DYLIBS/Intents.md)
- [/System/Library/Frameworks/JavaScriptCore.framework/JavaScriptCore](DYLIBS/JavaScriptCore.md)
- [/System/Library/Frameworks/LiveCommunicationKit.framework/LiveCommunicationKit](DYLIBS/LiveCommunicationKit.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication](DYLIBS/LocalAuthentication.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/DaemonUtils.framework/DaemonUtils](DYLIBS/DaemonUtils.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismBase.framework/MechanismBase](DYLIBS/MechanismBase.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/ModuleBase.framework/ModuleBase](DYLIBS/ModuleBase.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/SharedUtils.framework/SharedUtils](DYLIBS/SharedUtils.md)
- [/System/Library/Frameworks/MapKit.framework/MapKit](DYLIBS/MapKit.md)
- [/System/Library/Frameworks/Matter.framework/Matter](DYLIBS/Matter.md)
- [/System/Library/Frameworks/MediaPlayer.framework/MediaPlayer](DYLIBS/MediaPlayer.md)
- [/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox](DYLIBS/MediaToolbox.md)
- [/System/Library/Frameworks/MessageUI.framework/MessageUI](DYLIBS/MessageUI.md)
- [/System/Library/Frameworks/Metal.framework/Metal](DYLIBS/Metal.md)
- [/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNDArray.framework/MPSNDArray](DYLIBS/MPSNDArray.md)
- [/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork](DYLIBS/MPSNeuralNetwork.md)
- [/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph](DYLIBS/MetalPerformanceShadersGraph.md)
- [/System/Library/Frameworks/ModelIO.framework/ModelIO](DYLIBS/ModelIO.md)
- [/System/Library/Frameworks/MusicKit.framework/MusicKit](DYLIBS/MusicKit.md)
- [/System/Library/Frameworks/Network.framework/Network](DYLIBS/Network.md)
- [/System/Library/Frameworks/NetworkExtension.framework/NetworkExtension](DYLIBS/NetworkExtension.md)
- [/System/Library/Frameworks/OSLog.framework/OSLog](DYLIBS/OSLog.md)
- [/System/Library/Frameworks/PencilKit.framework/PencilKit](DYLIBS/PencilKit.md)
- [/System/Library/Frameworks/PhotosUI.framework/PhotosUI](DYLIBS/PhotosUI.md)
- [/System/Library/Frameworks/ProximityReader.framework/ProximityReader](DYLIBS/ProximityReader.md)
- [/System/Library/Frameworks/PushKit.framework/PushKit](DYLIBS/PushKit.md)
- [/System/Library/Frameworks/QuartzCore.framework/QuartzCore](DYLIBS/QuartzCore.md)
- [/System/Library/Frameworks/QuickLook.framework/QuickLook](DYLIBS/QuickLook.md)
- [/System/Library/Frameworks/QuickLookThumbnailing.framework/QuickLookThumbnailing](DYLIBS/QuickLookThumbnailing.md)
- [/System/Library/Frameworks/RealityFoundation.framework/RealityFoundation](DYLIBS/RealityFoundation.md)
- [/System/Library/Frameworks/RoomPlan.framework/RoomPlan](DYLIBS/RoomPlan.md)
- [/System/Library/Frameworks/SafariServices.framework/SafariServices](DYLIBS/SafariServices.md)
- [/System/Library/Frameworks/SceneKit.framework/SceneKit](DYLIBS/SceneKit.md)
- [/System/Library/Frameworks/Security.framework/Security](DYLIBS/Security.md)
- [/System/Library/Frameworks/SharedWithYou.framework/SharedWithYou](DYLIBS/SharedWithYou.md)
- [/System/Library/Frameworks/SharedWithYouCore.framework/SharedWithYouCore](DYLIBS/SharedWithYouCore.md)
- [/System/Library/Frameworks/SoundAnalysis.framework/SoundAnalysis](DYLIBS/SoundAnalysis.md)
- [/System/Library/Frameworks/Speech.framework/Speech](DYLIBS/Speech.md)
- [/System/Library/Frameworks/StickerKit.framework/StickerKit](DYLIBS/StickerKit.md)
- [/System/Library/Frameworks/StoreKit.framework/StoreKit](DYLIBS/StoreKit.md)
- [/System/Library/Frameworks/SwiftData.framework/SwiftData](DYLIBS/SwiftData.md)
- [/System/Library/Frameworks/SwiftUI.framework/SwiftUI](DYLIBS/SwiftUI.md)
- [/System/Library/Frameworks/SwiftUICore.framework/SwiftUICore](DYLIBS/SwiftUICore.md)
- [/System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration](DYLIBS/SystemConfiguration.md)
- [/System/Library/Frameworks/TabularData.framework/TabularData](DYLIBS/TabularData.md)
- [/System/Library/Frameworks/TipKit.framework/TipKit](DYLIBS/TipKit.md)
- [/System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers](DYLIBS/UniformTypeIdentifiers.md)
- [/System/Library/Frameworks/UserNotifications.framework/UserNotifications](DYLIBS/UserNotifications.md)
- [/System/Library/Frameworks/VideoToolbox.framework/VideoToolbox](DYLIBS/VideoToolbox.md)
- [/System/Library/Frameworks/Vision.framework/Vision](DYLIBS/Vision.md)
- [/System/Library/Frameworks/WeatherKit.framework/WeatherKit](DYLIBS/WeatherKit.md)
- [/System/Library/Frameworks/WebKit.framework/WebKit](DYLIBS/WebKit.md)
- [/System/Library/Frameworks/WidgetKit.framework/WidgetKit](DYLIBS/WidgetKit.md)
- [/System/Library/Frameworks/_AppIntents_SwiftUI.framework/_AppIntents_SwiftUI](DYLIBS/_AppIntents_SwiftUI.md)
- [/System/Library/Frameworks/_AppIntents_UIKit.framework/_AppIntents_UIKit](DYLIBS/_AppIntents_UIKit.md)
- [/System/Library/Frameworks/_MapKit_SwiftUI.framework/_MapKit_SwiftUI](DYLIBS/_MapKit_SwiftUI.md)
- [/System/Library/Frameworks/_MusicKit_SwiftUI.framework/_MusicKit_SwiftUI](DYLIBS/_MusicKit_SwiftUI.md)
- [/System/Library/Frameworks/_RealityKit_SwiftUI.framework/_RealityKit_SwiftUI](DYLIBS/_RealityKit_SwiftUI.md)
- [/System/Library/Frameworks/_StoreKit_SwiftUI.framework/_StoreKit_SwiftUI](DYLIBS/_StoreKit_SwiftUI.md)
- [/System/Library/HIDPlugins/IOHIDEventProcessorFilter.plugin/IOHIDEventProcessorFilter](DYLIBS/IOHIDEventProcessorFilter.md)
- [/System/Library/HIDPlugins/IOHIDEventSystemStatistics.plugin/IOHIDEventSystemStatistics](DYLIBS/IOHIDEventSystemStatistics.md)
- [/System/Library/HIDPlugins/PearlEventFilter.plugin/PearlEventFilter](DYLIBS/PearlEventFilter.md)
- [/System/Library/Health/FeedItemPlugins/HealthArticles.healthplugin/HealthArticles](DYLIBS/HealthArticles.md)
- [/System/Library/Health/FeedItemPlugins/HealthRecords.healthplugin/HealthRecords](DYLIBS/HealthRecords.md)
- [/System/Library/Health/FeedItemPlugins/HearingAppPlugin.healthplugin/HearingAppPlugin](DYLIBS/HearingAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/Heart.healthplugin/Heart](DYLIBS/Heart.md)
- [/System/Library/Health/FeedItemPlugins/HighlightAlerts.healthplugin/HighlightAlerts](DYLIBS/HighlightAlerts.md)
- [/System/Library/Health/FeedItemPlugins/Highlights.healthplugin/Highlights](DYLIBS/Highlights.md)
- [/System/Library/Health/FeedItemPlugins/MedicationsHealthAppPlugin.healthplugin/MedicationsHealthAppPlugin](DYLIBS/MedicationsHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/MenstrualCyclesAppPlugin.healthplugin/MenstrualCyclesAppPlugin](DYLIBS/MenstrualCyclesAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/MentalHealthAppPlugin.healthplugin/MentalHealthAppPlugin](DYLIBS/MentalHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/Profiles.healthplugin/Profiles](DYLIBS/Profiles.md)
- [/System/Library/Health/FeedItemPlugins/ResearchApp.healthplugin/ResearchApp](DYLIBS/ResearchApp.md)
- [/System/Library/Health/FeedItemPlugins/RespiratoryHealthAppPlugin.healthplugin/RespiratoryHealthAppPlugin](DYLIBS/RespiratoryHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/Safety.healthplugin/Safety](DYLIBS/Safety.md)
- [/System/Library/Health/FeedItemPlugins/SleepHealthAppPlugin.healthplugin/SleepHealthAppPlugin](DYLIBS/SleepHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/Summaries.healthplugin/Summaries](DYLIBS/Summaries.md)
- [/System/Library/Health/FeedItemPlugins/VisionHealthAppPlugin.healthplugin/VisionHealthAppPlugin](DYLIBS/VisionHealthAppPlugin.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/WeatherComplications.bundle/WeatherComplications](DYLIBS/WeatherComplications.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKEsterbrookFaceBundleCompanion.bundle/NTKEsterbrookFaceBundleCompanion](DYLIBS/NTKEsterbrookFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKParmesanFaceBundleCompanion.bundle/NTKParmesanFaceBundleCompanion](DYLIBS/NTKParmesanFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKRhizomeFaceBundleCompanion.bundle/NTKRhizomeFaceBundleCompanion](DYLIBS/NTKRhizomeFaceBundleCompanion.md)
- [/System/Library/PreferenceBundles/KeyboardSettings.bundle/KeyboardSettings](DYLIBS/KeyboardSettings.md)
- [/System/Library/Previews/ShellPlugins/WidgetPreviewsShellPlugin.bundle/WidgetPreviewsShellPlugin](DYLIBS/WidgetPreviewsShellPlugin.md)
- [/System/Library/PrivateFrameworks/AAAFoundation.framework/AAAFoundation](DYLIBS/AAAFoundation.md)
- [/System/Library/PrivateFrameworks/AAAFoundationSwift.framework/AAAFoundationSwift](DYLIBS/AAAFoundationSwift.md)
- [/System/Library/PrivateFrameworks/ABMHelper.framework/ABMHelper](DYLIBS/ABMHelper.md)
- [/System/Library/PrivateFrameworks/AIMLInstrumentationStreams.framework/AIMLInstrumentationStreams](DYLIBS/AIMLInstrumentationStreams.md)
- [/System/Library/PrivateFrameworks/ALDataTypes.framework/ALDataTypes.dylib](DYLIBS/ALDataTypes.dylib.md)
- [/System/Library/PrivateFrameworks/ANECompiler.framework/ANECompiler](DYLIBS/ANECompiler.md)
- [/System/Library/PrivateFrameworks/AONSense.framework/AONSense.dylib](DYLIBS/AONSense.dylib.md)
- [/System/Library/PrivateFrameworks/APFS.framework/APFS](DYLIBS/APFS.md)
- [/System/Library/PrivateFrameworks/APFoundation.framework/APFoundation](DYLIBS/APFoundation.md)
- [/System/Library/PrivateFrameworks/APTransport.framework/APTransport](DYLIBS/APTransport.md)
- [/System/Library/PrivateFrameworks/ARKitCore.framework/ARKitCore](DYLIBS/ARKitCore.md)
- [/System/Library/PrivateFrameworks/ASEProcessing.framework/ASEProcessing](DYLIBS/ASEProcessing.md)
- [/System/Library/PrivateFrameworks/ASRBridge.framework/ASRBridge](DYLIBS/ASRBridge.md)
- [/System/Library/PrivateFrameworks/ATFoundation.framework/ATFoundation](DYLIBS/ATFoundation.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/AVConference](DYLIBS/AVConference.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ViceroyTrace.framework/ViceroyTrace](DYLIBS/ViceroyTrace.md)
- [/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture](DYLIBS/AVFCapture.md)
- [/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore](DYLIBS/AVFCore.md)
- [/System/Library/PrivateFrameworks/AXSoundDetectionUI.framework/AXSoundDetectionUI](DYLIBS/AXSoundDetectionUI.md)
- [/System/Library/PrivateFrameworks/AccessibilitySettingsUI.framework/AccessibilitySettingsUI](DYLIBS/AccessibilitySettingsUI.md)
- [/System/Library/PrivateFrameworks/AccessibilitySharedSupport.framework/AccessibilitySharedSupport](DYLIBS/AccessibilitySharedSupport.md)
- [/System/Library/PrivateFrameworks/AccessibilitySharedUISupport.framework/AccessibilitySharedUISupport](DYLIBS/AccessibilitySharedUISupport.md)
- [/System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities](DYLIBS/AccessibilityUtilities.md)
- [/System/Library/PrivateFrameworks/AccountsDaemon.framework/AccountsDaemon](DYLIBS/AccountsDaemon.md)
- [/System/Library/PrivateFrameworks/ActionButtonConfigurationUI.framework/ActionButtonConfigurationUI](DYLIBS/ActionButtonConfigurationUI.md)
- [/System/Library/PrivateFrameworks/ActionButtonSelector.framework/ActionButtonSelector](DYLIBS/ActionButtonSelector.md)
- [/System/Library/PrivateFrameworks/ActionKit.framework/ActionKit](DYLIBS/ActionKit.md)
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
- [/System/Library/PrivateFrameworks/ActivitySharingServices.framework/ActivitySharingServices](DYLIBS/ActivitySharingServices.md)
- [/System/Library/PrivateFrameworks/ActivityUIServices.framework/ActivityUIServices](DYLIBS/ActivityUIServices.md)
- [/System/Library/PrivateFrameworks/AdCore.framework/AdCore](DYLIBS/AdCore.md)
- [/System/Library/PrivateFrameworks/AdID.framework/AdID](DYLIBS/AdID.md)
- [/System/Library/PrivateFrameworks/AdPlatformsCommon.framework/AdPlatformsCommon](DYLIBS/AdPlatformsCommon.md)
- [/System/Library/PrivateFrameworks/AdPlatformsCommonUI.framework/AdPlatformsCommonUI](DYLIBS/AdPlatformsCommonUI.md)
- [/System/Library/PrivateFrameworks/AdaptiveVoiceShortcuts.framework/AdaptiveVoiceShortcuts](DYLIBS/AdaptiveVoiceShortcuts.md)
- [/System/Library/PrivateFrameworks/AddressBookLegacy.framework/AddressBookLegacy](DYLIBS/AddressBookLegacy.md)
- [/System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary](DYLIBS/AggregateDictionary.md)
- [/System/Library/PrivateFrameworks/AirPlayKit.framework/AirPlayKit](DYLIBS/AirPlayKit.md)
- [/System/Library/PrivateFrameworks/AirPlayReceiver.framework/AirPlayReceiver](DYLIBS/AirPlayReceiver.md)
- [/System/Library/PrivateFrameworks/AirPlayReceiverKit.framework/AirPlayReceiverKit](DYLIBS/AirPlayReceiverKit.md)
- [/System/Library/PrivateFrameworks/AirPlayRoutePrediction.framework/AirPlayRoutePrediction](DYLIBS/AirPlayRoutePrediction.md)
- [/System/Library/PrivateFrameworks/AirPlaySender.framework/AirPlaySender](DYLIBS/AirPlaySender.md)
- [/System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport](DYLIBS/AirPlaySupport.md)
- [/System/Library/PrivateFrameworks/AirTrafficDevice.framework/AirTrafficDevice](DYLIBS/AirTrafficDevice.md)
- [/System/Library/PrivateFrameworks/Announce.framework/Announce](DYLIBS/Announce.md)
- [/System/Library/PrivateFrameworks/AnnounceDaemon.framework/AnnounceDaemon](DYLIBS/AnnounceDaemon.md)
- [/System/Library/PrivateFrameworks/Anvil.framework/Anvil](DYLIBS/Anvil.md)
- [/System/Library/PrivateFrameworks/AppAnalytics.framework/AppAnalytics](DYLIBS/AppAnalytics.md)
- [/System/Library/PrivateFrameworks/AppAttestInternal.framework/AppAttestInternal](DYLIBS/AppAttestInternal.md)
- [/System/Library/PrivateFrameworks/AppC3D.framework/AppC3D](DYLIBS/AppC3D.md)
- [/System/Library/PrivateFrameworks/AppConduit.framework/AppConduit](DYLIBS/AppConduit.md)
- [/System/Library/PrivateFrameworks/AppIntentsServices.framework/AppIntentsServices](DYLIBS/AppIntentsServices.md)
- [/System/Library/PrivateFrameworks/AppMigrationKit.framework/AppMigrationKit](DYLIBS/AppMigrationKit.md)
- [/System/Library/PrivateFrameworks/AppPredictionClient.framework/AppPredictionClient](DYLIBS/AppPredictionClient.md)
- [/System/Library/PrivateFrameworks/AppPredictionInternal.framework/AppPredictionInternal](DYLIBS/AppPredictionInternal.md)
- [/System/Library/PrivateFrameworks/AppProtection.framework/AppProtection](DYLIBS/AppProtection.md)
- [/System/Library/PrivateFrameworks/AppSSOCore.framework/AppSSOCore](DYLIBS/AppSSOCore.md)
- [/System/Library/PrivateFrameworks/AppServerSupport.framework/AppServerSupport](DYLIBS/AppServerSupport.md)
- [/System/Library/PrivateFrameworks/AppState.framework/AppState](DYLIBS/AppState.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon](DYLIBS/AppStoreDaemon.md)
- [/System/Library/PrivateFrameworks/AppStoreFoundation.framework/AppStoreFoundation](DYLIBS/AppStoreFoundation.md)
- [/System/Library/PrivateFrameworks/AppStoreKit.framework/AppStoreKit](DYLIBS/AppStoreKit.md)
- [/System/Library/PrivateFrameworks/AppSupportUI.framework/AppSupportUI](DYLIBS/AppSupportUI.md)
- [/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount](DYLIBS/AppleAccount.md)
- [/System/Library/PrivateFrameworks/AppleAccountUI.framework/AppleAccountUI](DYLIBS/AppleAccountUI.md)
- [/System/Library/PrivateFrameworks/AppleBasebandManager.framework/AppleBasebandManager](DYLIBS/AppleBasebandManager.md)
- [/System/Library/PrivateFrameworks/AppleBasebandServices.framework/AppleBasebandServices](DYLIBS/AppleBasebandServices.md)
- [/System/Library/PrivateFrameworks/AppleCV3D.framework/AppleCV3D](DYLIBS/AppleCV3D.md)
- [/System/Library/PrivateFrameworks/AppleCVAPhoto.framework/AppleCVAPhoto](DYLIBS/AppleCVAPhoto.md)
- [/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/AppleDeviceQuerySupport](DYLIBS/AppleDeviceQuerySupport.md)
- [/System/Library/PrivateFrameworks/AppleFSCompression.framework/AppleFSCompression](DYLIBS/AppleFSCompression.md)
- [/System/Library/PrivateFrameworks/AppleIDSSOAuthentication.framework/AppleIDSSOAuthentication](DYLIBS/AppleIDSSOAuthentication.md)
- [/System/Library/PrivateFrameworks/AppleIDSetup.framework/AppleIDSetup](DYLIBS/AppleIDSetup.md)
- [/System/Library/PrivateFrameworks/AppleIDSetupDaemon.framework/AppleIDSetupDaemon](DYLIBS/AppleIDSetupDaemon.md)
- [/System/Library/PrivateFrameworks/AppleIDSetupUI.framework/AppleIDSetupUI](DYLIBS/AppleIDSetupUI.md)
- [/System/Library/PrivateFrameworks/AppleJPEG.framework/AppleJPEG](DYLIBS/AppleJPEG.md)
- [/System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore](DYLIBS/AppleKeyStore.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices](DYLIBS/AppleMediaServices.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesKitInternal.framework/AppleMediaServicesKitInternal](DYLIBS/AppleMediaServicesKitInternal.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/AppleMediaServicesUI](DYLIBS/AppleMediaServicesUI.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUIDynamic.framework/AppleMediaServicesUIDynamic](DYLIBS/AppleMediaServicesUIDynamic.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUIPaymentSheets.framework/AppleMediaServicesUIPaymentSheets](DYLIBS/AppleMediaServicesUIPaymentSheets.md)
- [/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine](DYLIBS/AppleNeuralEngine.md)
- [/System/Library/PrivateFrameworks/ApplePushService.framework/ApplePushService](DYLIBS/ApplePushService.md)
- [/System/Library/PrivateFrameworks/AppleServiceToolkit.framework/AppleServiceToolkit](DYLIBS/AppleServiceToolkit.md)
- [/System/Library/PrivateFrameworks/ArgumentParserInternal.framework/ArgumentParserInternal](DYLIBS/ArgumentParserInternal.md)
- [/System/Library/PrivateFrameworks/AskPermission.framework/AskPermission](DYLIBS/AskPermission.md)
- [/System/Library/PrivateFrameworks/AskToCore.framework/AskToCore](DYLIBS/AskToCore.md)
- [/System/Library/PrivateFrameworks/AskToDaemon.framework/AskToDaemon](DYLIBS/AskToDaemon.md)
- [/System/Library/PrivateFrameworks/AssertionServices.framework/AssertionServices](DYLIBS/AssertionServices.md)
- [/System/Library/PrivateFrameworks/AssetCacheServices.framework/AssetCacheServices](DYLIBS/AssetCacheServices.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices](DYLIBS/AssistantServices.md)
- [/System/Library/PrivateFrameworks/AssistantSettingsSupport.framework/AssistantSettingsSupport](DYLIBS/AssistantSettingsSupport.md)
- [/System/Library/PrivateFrameworks/AssistantUI.framework/AssistantUI](DYLIBS/AssistantUI.md)
- [/System/Library/PrivateFrameworks/AttentionAwareness.framework/AttentionAwareness](DYLIBS/AttentionAwareness.md)
- [/System/Library/PrivateFrameworks/AttributeGraph.framework/AttributeGraph](DYLIBS/AttributeGraph.md)
- [/System/Library/PrivateFrameworks/AudioAnalytics.framework/AudioAnalytics](DYLIBS/AudioAnalytics.md)
- [/System/Library/PrivateFrameworks/AudioAnalyticsBase.framework/AudioAnalyticsBase](DYLIBS/AudioAnalyticsBase.md)
- [/System/Library/PrivateFrameworks/AudioAnalyticsExternal.framework/AudioAnalyticsExternal](DYLIBS/AudioAnalyticsExternal.md)
- [/System/Library/PrivateFrameworks/AudioDSPManager.framework/AudioDSPManager](DYLIBS/AudioDSPManager.md)
- [/System/Library/PrivateFrameworks/AudioServerDriver.framework/AudioServerDriver](DYLIBS/AudioServerDriver.md)
- [/System/Library/PrivateFrameworks/AudioServerDriverTransports_Base.framework/AudioServerDriverTransports_Base](DYLIBS/AudioServerDriverTransports_Base.md)
- [/System/Library/PrivateFrameworks/AudioServerDriverTransports_IOA2.framework/AudioServerDriverTransports_IOA2](DYLIBS/AudioServerDriverTransports_IOA2.md)
- [/System/Library/PrivateFrameworks/AudioSession.framework/AudioSession](DYLIBS/AudioSession.md)
- [/System/Library/PrivateFrameworks/AudioSessionServer.framework/AudioSessionServer](DYLIBS/AudioSessionServer.md)
- [/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore](DYLIBS/AudioToolboxCore.md)
- [/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit](DYLIBS/AuthKit.md)
- [/System/Library/PrivateFrameworks/AuthenticationServicesCore.framework/AuthenticationServicesCore](DYLIBS/AuthenticationServicesCore.md)
- [/System/Library/PrivateFrameworks/AutoBugCaptureCore.framework/AutoBugCaptureCore](DYLIBS/AutoBugCaptureCore.md)
- [/System/Library/PrivateFrameworks/AvatarKit.framework/AvatarKit](DYLIBS/AvatarKit.md)
- [/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation](DYLIBS/BackBoardHIDEventFoundation.md)
- [/System/Library/PrivateFrameworks/BackBoardHIDEventProcessors.framework/BackBoardHIDEventProcessors](DYLIBS/BackBoardHIDEventProcessors.md)
- [/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices](DYLIBS/BackBoardServices.md)
- [/System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks](DYLIBS/BackgroundSystemTasks.md)
- [/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices](DYLIBS/BacklightServices.md)
- [/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost](DYLIBS/BacklightServicesHost.md)
- [/System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard](DYLIBS/BaseBoard.md)
- [/System/Library/PrivateFrameworks/BaseBoardUI.framework/BaseBoardUI](DYLIBS/BaseBoardUI.md)
- [/System/Library/PrivateFrameworks/BasebandTraceHelper.framework/BasebandTraceHelper](DYLIBS/BasebandTraceHelper.md)
- [/System/Library/PrivateFrameworks/BiomeFoundation.framework/BiomeFoundation](DYLIBS/BiomeFoundation.md)
- [/System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary](DYLIBS/BiomeLibrary.md)
- [/System/Library/PrivateFrameworks/BiomePubSub.framework/BiomePubSub](DYLIBS/BiomePubSub.md)
- [/System/Library/PrivateFrameworks/BiomeStorage.framework/BiomeStorage](DYLIBS/BiomeStorage.md)
- [/System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams](DYLIBS/BiomeStreams.md)
- [/System/Library/PrivateFrameworks/Blackbeard.framework/Blackbeard](DYLIBS/Blackbeard.md)
- [/System/Library/PrivateFrameworks/BlastDoor.framework/BlastDoor](DYLIBS/BlastDoor.md)
- [/System/Library/PrivateFrameworks/BoardServices.framework/BoardServices](DYLIBS/BoardServices.md)
- [/System/Library/PrivateFrameworks/BookCoverUtility.framework/BookCoverUtility](DYLIBS/BookCoverUtility.md)
- [/System/Library/PrivateFrameworks/BookDataStore.framework/BookDataStore](DYLIBS/BookDataStore.md)
- [/System/Library/PrivateFrameworks/BookFoundation.framework/BookFoundation](DYLIBS/BookFoundation.md)
- [/System/Library/PrivateFrameworks/BookLibraryCore.framework/BookLibraryCore](DYLIBS/BookLibraryCore.md)
- [/System/Library/PrivateFrameworks/BookUtility.framework/BookUtility](DYLIBS/BookUtility.md)
- [/System/Library/PrivateFrameworks/BrailleSymbology.framework/BrailleSymbology](DYLIBS/BrailleSymbology.md)
- [/System/Library/PrivateFrameworks/BulletinBoard.framework/BulletinBoard](DYLIBS/BulletinBoard.md)
- [/System/Library/PrivateFrameworks/BusinessChatService.framework/BusinessChatService](DYLIBS/BusinessChatService.md)
- [/System/Library/PrivateFrameworks/C2.framework/C2](DYLIBS/C2.md)
- [/System/Library/PrivateFrameworks/CAFCombine.framework/CAFCombine](DYLIBS/CAFCombine.md)
- [/System/Library/PrivateFrameworks/CDMFoundation.framework/CDMFoundation](DYLIBS/CDMFoundation.md)
- [/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture](DYLIBS/CMCapture.md)
- [/System/Library/PrivateFrameworks/CMCaptureCore.framework/CMCaptureCore](DYLIBS/CMCaptureCore.md)
- [/System/Library/PrivateFrameworks/CMContinuityCaptureCore.framework/CMContinuityCaptureCore](DYLIBS/CMContinuityCaptureCore.md)
- [/System/Library/PrivateFrameworks/CMImaging.framework/CMImaging](DYLIBS/CMImaging.md)
- [/System/Library/PrivateFrameworks/CMPhoto.framework/CMPhoto](DYLIBS/CMPhoto.md)
- [/System/Library/PrivateFrameworks/CTBlastDoorSupport.framework/CTBlastDoorSupport](DYLIBS/CTBlastDoorSupport.md)
- [/System/Library/PrivateFrameworks/CTCarrierSpace.framework/CTCarrierSpace](DYLIBS/CTCarrierSpace.md)
- [/System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete](DYLIBS/CacheDelete.md)
- [/System/Library/PrivateFrameworks/Calculate.framework/Calculate](DYLIBS/Calculate.md)
- [/System/Library/PrivateFrameworks/CalculateUI.framework/CalculateUI](DYLIBS/CalculateUI.md)
- [/System/Library/PrivateFrameworks/CalendarDaemon.framework/CalendarDaemon](DYLIBS/CalendarDaemon.md)
- [/System/Library/PrivateFrameworks/CalendarDatabase.framework/CalendarDatabase](DYLIBS/CalendarDatabase.md)
- [/System/Library/PrivateFrameworks/CalendarIntegrationSupport.framework/CalendarIntegrationSupport](DYLIBS/CalendarIntegrationSupport.md)
- [/System/Library/PrivateFrameworks/CalendarLink.framework/CalendarLink](DYLIBS/CalendarLink.md)
- [/System/Library/PrivateFrameworks/CalendarUIKit.framework/CalendarUIKit](DYLIBS/CalendarUIKit.md)
- [/System/Library/PrivateFrameworks/CalendarUIKitInternal.framework/CalendarUIKitInternal](DYLIBS/CalendarUIKitInternal.md)
- [/System/Library/PrivateFrameworks/CalendarWidget.framework/CalendarWidget](DYLIBS/CalendarWidget.md)
- [/System/Library/PrivateFrameworks/CallHistory.framework/CallHistory](DYLIBS/CallHistory.md)
- [/System/Library/PrivateFrameworks/CameraColorProcessing.framework/CameraColorProcessing](DYLIBS/CameraColorProcessing.md)
- [/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI](DYLIBS/CameraUI.md)
- [/System/Library/PrivateFrameworks/CarKit.framework/CarKit](DYLIBS/CarKit.md)
- [/System/Library/PrivateFrameworks/CarKitNavigation.framework/CarKitNavigation](DYLIBS/CarKitNavigation.md)
- [/System/Library/PrivateFrameworks/CarPlayAssetUI.framework/CarPlayAssetUI](DYLIBS/CarPlayAssetUI.md)
- [/System/Library/PrivateFrameworks/CarPlaySupport.framework/CarPlaySupport](DYLIBS/CarPlaySupport.md)
- [/System/Library/PrivateFrameworks/CarPlayUI.framework/CarPlayUI](DYLIBS/CarPlayUI.md)
- [/System/Library/PrivateFrameworks/CascadeEngine.framework/CascadeEngine](DYLIBS/CascadeEngine.md)
- [/System/Library/PrivateFrameworks/CascadeSets.framework/CascadeSets](DYLIBS/CascadeSets.md)
- [/System/Library/PrivateFrameworks/Celestial.framework/Celestial](DYLIBS/Celestial.md)
- [/System/Library/PrivateFrameworks/CellularPlanManager.framework/CellularPlanManager](DYLIBS/CellularPlanManager.md)
- [/System/Library/PrivateFrameworks/ChatKit.framework/ChatKit](DYLIBS/ChatKit.md)
- [/System/Library/PrivateFrameworks/ChronoCore.framework/ChronoCore](DYLIBS/ChronoCore.md)
- [/System/Library/PrivateFrameworks/ChronoCore.framework/Support/WidgetPreviewsExtensionAgent.bundle/WidgetPreviewsExtensionAgent](DYLIBS/WidgetPreviewsExtensionAgent.md)
- [/System/Library/PrivateFrameworks/ChronoKit.framework/ChronoKit](DYLIBS/ChronoKit.md)
- [/System/Library/PrivateFrameworks/ChronoServices.framework/ChronoServices](DYLIBS/ChronoServices.md)
- [/System/Library/PrivateFrameworks/ChronoUIServices.framework/ChronoUIServices](DYLIBS/ChronoUIServices.md)
- [/System/Library/PrivateFrameworks/CiderAudioServer.framework/CiderAudioServer](DYLIBS/CiderAudioServer.md)
- [/System/Library/PrivateFrameworks/CinematicFraming.framework/CinematicFraming](DYLIBS/CinematicFraming.md)
- [/System/Library/PrivateFrameworks/CipherML.framework/CipherML](DYLIBS/CipherML.md)
- [/System/Library/PrivateFrameworks/ClassroomKit.framework/Frameworks/ClassroomUIKit.framework/ClassroomUIKit](DYLIBS/ClassroomUIKit.md)
- [/System/Library/PrivateFrameworks/ClockKitUI.framework/ClockKitUI](DYLIBS/ClockKitUI.md)
- [/System/Library/PrivateFrameworks/ClockPoster.framework/ClockPoster](DYLIBS/ClockPoster.md)
- [/System/Library/PrivateFrameworks/CloudDocs.framework/CloudDocs](DYLIBS/CloudDocs.md)
- [/System/Library/PrivateFrameworks/CloudDocsUI.framework/CloudDocsUI](DYLIBS/CloudDocsUI.md)
- [/System/Library/PrivateFrameworks/CloudKitDaemon.framework/CloudKitDaemon](DYLIBS/CloudKitDaemon.md)
- [/System/Library/PrivateFrameworks/CloudRecommendationUI.framework/CloudRecommendationUI](DYLIBS/CloudRecommendationUI.md)
- [/System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/CloudSubscriptionFeatures](DYLIBS/CloudSubscriptionFeatures.md)
- [/System/Library/PrivateFrameworks/CloudTelemetry.framework/CloudTelemetry](DYLIBS/CloudTelemetry.md)
- [/System/Library/PrivateFrameworks/CloudTelemetryTools.framework/CloudTelemetryTools](DYLIBS/CloudTelemetryTools.md)
- [/System/Library/PrivateFrameworks/Coherence.framework/Coherence](DYLIBS/Coherence.md)
- [/System/Library/PrivateFrameworks/CollectionViewCore.framework/CollectionViewCore](DYLIBS/CollectionViewCore.md)
- [/System/Library/PrivateFrameworks/CollectionsInternal.framework/CollectionsInternal](DYLIBS/CollectionsInternal.md)
- [/System/Library/PrivateFrameworks/CommandAndControlUI.framework/CommandAndControlUI](DYLIBS/CommandAndControlUI.md)
- [/System/Library/PrivateFrameworks/CommonUtilities.framework/CommonUtilities](DYLIBS/CommonUtilities.md)
- [/System/Library/PrivateFrameworks/CommunicationsUI.framework/CommunicationsUI](DYLIBS/CommunicationsUI.md)
- [/System/Library/PrivateFrameworks/CompanionSync.framework/CompanionSync](DYLIBS/CompanionSync.md)
- [/System/Library/PrivateFrameworks/CompassUI.framework/CompassUI](DYLIBS/CompassUI.md)
- [/System/Library/PrivateFrameworks/ContactlessReaderUI.framework/ContactlessReaderUI](DYLIBS/ContactlessReaderUI.md)
- [/System/Library/PrivateFrameworks/ContactsAutocomplete.framework/ContactsAutocomplete](DYLIBS/ContactsAutocomplete.md)
- [/System/Library/PrivateFrameworks/ContactsAutocompleteUI.framework/ContactsAutocompleteUI](DYLIBS/ContactsAutocompleteUI.md)
- [/System/Library/PrivateFrameworks/ContactsFoundation.framework/ContactsFoundation](DYLIBS/ContactsFoundation.md)
- [/System/Library/PrivateFrameworks/ContactsUICore.framework/ContactsUICore](DYLIBS/ContactsUICore.md)
- [/System/Library/PrivateFrameworks/ContainerManagerCommon.framework/ContainerManagerCommon](DYLIBS/ContainerManagerCommon.md)
- [/System/Library/PrivateFrameworks/ContentKit.framework/ContentKit](DYLIBS/ContentKit.md)
- [/System/Library/PrivateFrameworks/ContextKitExtraction.framework/ContextKitExtraction](DYLIBS/ContextKitExtraction.md)
- [/System/Library/PrivateFrameworks/ContextualUnderstanding.framework/ContextualUnderstanding](DYLIBS/ContextualUnderstanding.md)
- [/System/Library/PrivateFrameworks/ControlCenterUI.framework/ControlCenterUI](DYLIBS/ControlCenterUI.md)
- [/System/Library/PrivateFrameworks/ControlCenterUIKit.framework/ControlCenterUIKit](DYLIBS/ControlCenterUIKit.md)
- [/System/Library/PrivateFrameworks/ConversationKit.framework/ConversationKit](DYLIBS/ConversationKit.md)
- [/System/Library/PrivateFrameworks/CookingKit.framework/CookingKit](DYLIBS/CookingKit.md)
- [/System/Library/PrivateFrameworks/CookingSupport.framework/CookingSupport](DYLIBS/CookingSupport.md)
- [/System/Library/PrivateFrameworks/CoordinationCore.framework/CoordinationCore](DYLIBS/CoordinationCore.md)
- [/System/Library/PrivateFrameworks/CopresenceCore.framework/CopresenceCore](DYLIBS/CopresenceCore.md)
- [/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics](DYLIBS/CoreAnalytics.md)
- [/System/Library/PrivateFrameworks/CoreAppleCVA.framework/CoreAppleCVA](DYLIBS/CoreAppleCVA.md)
- [/System/Library/PrivateFrameworks/CoreAutoLayout.framework/CoreAutoLayout](DYLIBS/CoreAutoLayout.md)
- [/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness](DYLIBS/CoreBrightness.md)
- [/System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP](DYLIBS/CoreCDP.md)
- [/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal](DYLIBS/CoreCDPInternal.md)
- [/System/Library/PrivateFrameworks/CoreCDPUI.framework/CoreCDPUI](DYLIBS/CoreCDPUI.md)
- [/System/Library/PrivateFrameworks/CoreCaptureDaemon.framework/CoreCaptureDaemon](DYLIBS/CoreCaptureDaemon.md)
- [/System/Library/PrivateFrameworks/CoreDiagnostics.framework/CoreDiagnostics](DYLIBS/CoreDiagnostics.md)
- [/System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet](DYLIBS/CoreDuet.md)
- [/System/Library/PrivateFrameworks/CoreDuetContext.framework/CoreDuetContext](DYLIBS/CoreDuetContext.md)
- [/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/CoreEmbeddedSpeechRecognition](DYLIBS/CoreEmbeddedSpeechRecognition.md)
- [/System/Library/PrivateFrameworks/CoreEmoji.framework/CoreEmoji](DYLIBS/CoreEmoji.md)
- [/System/Library/PrivateFrameworks/CoreGEM.framework/CoreGEM.dylib](DYLIBS/CoreGEM.dylib.md)
- [/System/Library/PrivateFrameworks/CoreHAP.framework/CoreHAP](DYLIBS/CoreHAP.md)
- [/System/Library/PrivateFrameworks/CoreHID.framework/CoreHID](DYLIBS/CoreHID.md)
- [/System/Library/PrivateFrameworks/CoreIDVRGBLiveness.framework/CoreIDVRGBLiveness](DYLIBS/CoreIDVRGBLiveness.md)
- [/System/Library/PrivateFrameworks/CoreIDVShared.framework/CoreIDVShared](DYLIBS/CoreIDVShared.md)
- [/System/Library/PrivateFrameworks/CoreIDVUI.framework/CoreIDVUI](DYLIBS/CoreIDVUI.md)
- [/System/Library/PrivateFrameworks/CoreIndoor.framework/CoreIndoor](DYLIBS/CoreIndoor.md)
- [/System/Library/PrivateFrameworks/CoreKnowledge.framework/CoreKnowledge](DYLIBS/CoreKnowledge.md)
- [/System/Library/PrivateFrameworks/CoreMaterial.framework/CoreMaterial](DYLIBS/CoreMaterial.md)
- [/System/Library/PrivateFrameworks/CoreNLP.framework/CoreNLP](DYLIBS/CoreNLP.md)
- [/System/Library/PrivateFrameworks/CoreNavigation.framework/CoreNavigation](DYLIBS/CoreNavigation.md)
- [/System/Library/PrivateFrameworks/CoreODI.framework/CoreODI](DYLIBS/CoreODI.md)
- [/System/Library/PrivateFrameworks/CoreODIEssentials.framework/CoreODIEssentials](DYLIBS/CoreODIEssentials.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/CoreParsec](DYLIBS/CoreParsec.md)
- [/System/Library/PrivateFrameworks/CorePhoneNumbers.framework/CorePhoneNumbers](DYLIBS/CorePhoneNumbers.md)
- [/System/Library/PrivateFrameworks/CorePhotogrammetry.framework/CorePhotogrammetry](DYLIBS/CorePhotogrammetry.md)
- [/System/Library/PrivateFrameworks/CoreRecents.framework/CoreRecents](DYLIBS/CoreRecents.md)
- [/System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore](DYLIBS/CoreRepairCore.md)
- [/System/Library/PrivateFrameworks/CoreRepairUI.framework/CoreRepairUI](DYLIBS/CoreRepairUI.md)
- [/System/Library/PrivateFrameworks/CoreRoutine.framework/CoreRoutine](DYLIBS/CoreRoutine.md)
- [/System/Library/PrivateFrameworks/CoreSVG.framework/CoreSVG](DYLIBS/CoreSVG.md)
- [/System/Library/PrivateFrameworks/CoreServicesStore.framework/CoreServicesStore](DYLIBS/CoreServicesStore.md)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/CoreSpeech](DYLIBS/CoreSpeech.md)
- [/System/Library/PrivateFrameworks/CoreSpeechExclave.framework/CoreSpeechExclave](DYLIBS/CoreSpeechExclave.md)
- [/System/Library/PrivateFrameworks/CoreSpeechFoundation.framework/CoreSpeechFoundation](DYLIBS/CoreSpeechFoundation.md)
- [/System/Library/PrivateFrameworks/CoreSpeechUtils.framework/CoreSpeechUtils](DYLIBS/CoreSpeechUtils.md)
- [/System/Library/PrivateFrameworks/CoreSuggestions.framework/CoreSuggestions](DYLIBS/CoreSuggestions.md)
- [/System/Library/PrivateFrameworks/CoreSuggestionsInternals.framework/CoreSuggestionsInternals](DYLIBS/CoreSuggestionsInternals.md)
- [/System/Library/PrivateFrameworks/CoreSuggestionsUI.framework/CoreSuggestionsUI](DYLIBS/CoreSuggestionsUI.md)
- [/System/Library/PrivateFrameworks/CoreThreadRadio.framework/CoreThreadRadio](DYLIBS/CoreThreadRadio.md)
- [/System/Library/PrivateFrameworks/CoreTime.framework/CoreTime](DYLIBS/CoreTime.md)
- [/System/Library/PrivateFrameworks/CoreUARP.framework/CoreUARP](DYLIBS/CoreUARP.md)
- [/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI](DYLIBS/CoreUI.md)
- [/System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils](DYLIBS/CoreUtils.md)
- [/System/Library/PrivateFrameworks/CoreUtilsExtras.framework/CoreUtilsExtras](DYLIBS/CoreUtilsExtras.md)
- [/System/Library/PrivateFrameworks/CoreUtilsSwift.framework/CoreUtilsSwift](DYLIBS/CoreUtilsSwift.md)
- [/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi](DYLIBS/CoreWiFi.md)
- [/System/Library/PrivateFrameworks/Cosmo.framework/Cosmo](DYLIBS/Cosmo.md)
- [/System/Library/PrivateFrameworks/CoverSheet.framework/CoverSheet](DYLIBS/CoverSheet.md)
- [/System/Library/PrivateFrameworks/CoverSheetKit.framework/CoverSheetKit](DYLIBS/CoverSheetKit.md)
- [/System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport](DYLIBS/CrashReporterSupport.md)
- [/System/Library/PrivateFrameworks/CryptexServer.framework/CryptexServer](DYLIBS/CryptexServer.md)
- [/System/Library/PrivateFrameworks/CryptoKitPrivate.framework/CryptoKitPrivate](DYLIBS/CryptoKitPrivate.md)
- [/System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities](DYLIBS/DMCUtilities.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/DVTInstrumentsFoundation](DYLIBS/DVTInstrumentsFoundation.md)
- [/System/Library/PrivateFrameworks/DailyBriefingCommon.framework/DailyBriefingCommon](DYLIBS/DailyBriefingCommon.md)
- [/System/Library/PrivateFrameworks/DarwinDirectory.framework/DarwinDirectory](DYLIBS/DarwinDirectory.md)
- [/System/Library/PrivateFrameworks/DarwinDirectoryInternal.framework/DarwinDirectoryInternal](DYLIBS/DarwinDirectoryInternal.md)
- [/System/Library/PrivateFrameworks/DashBoard.framework/DashBoard](DYLIBS/DashBoard.md)
- [/System/Library/PrivateFrameworks/DataFlow.framework/DataFlow](DYLIBS/DataFlow.md)
- [/System/Library/PrivateFrameworks/DeepThought.framework/DeepThought](DYLIBS/DeepThought.md)
- [/System/Library/PrivateFrameworks/DeepThoughtBiomeFoundation.framework/DeepThoughtBiomeFoundation](DYLIBS/DeepThoughtBiomeFoundation.md)
- [/System/Library/PrivateFrameworks/Dendrite.framework/Dendrite](DYLIBS/Dendrite.md)
- [/System/Library/PrivateFrameworks/DepthCore.framework/DepthCore](DYLIBS/DepthCore.md)
- [/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/DesktopServicesPriv](DYLIBS/DesktopServicesPriv.md)
- [/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/DeviceExpertIntents](DYLIBS/DeviceExpertIntents.md)
- [/System/Library/PrivateFrameworks/DeviceExpertUI.framework/DeviceExpertUI](DYLIBS/DeviceExpertUI.md)
- [/System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity](DYLIBS/DeviceIdentity.md)
- [/System/Library/PrivateFrameworks/DeviceManagement.framework/DeviceManagement](DYLIBS/DeviceManagement.md)
- [/System/Library/PrivateFrameworks/DeviceSharing.framework/DeviceSharing](DYLIBS/DeviceSharing.md)
- [/System/Library/PrivateFrameworks/DiagnosticRequestService.framework/DiagnosticRequestService](DYLIBS/DiagnosticRequestService.md)
- [/System/Library/PrivateFrameworks/DiagnosticsReporterServices.framework/DiagnosticsReporterServices](DYLIBS/DiagnosticsReporterServices.md)
- [/System/Library/PrivateFrameworks/DialogEngine.framework/DialogEngine](DYLIBS/DialogEngine.md)
- [/System/Library/PrivateFrameworks/DigitalAccess.framework/DigitalAccess](DYLIBS/DigitalAccess.md)
- [/System/Library/PrivateFrameworks/DiskImages2.framework/DiskImages2](DYLIBS/DiskImages2.md)
- [/System/Library/PrivateFrameworks/DistributedEvaluation.framework/DistributedEvaluation](DYLIBS/DistributedEvaluation.md)
- [/System/Library/PrivateFrameworks/DistributedTimers.framework/DistributedTimers](DYLIBS/DistributedTimers.md)
- [/System/Library/PrivateFrameworks/DoNotDisturb.framework/DoNotDisturb](DYLIBS/DoNotDisturb.md)
- [/System/Library/PrivateFrameworks/DoNotDisturbServer.framework/DoNotDisturbServer](DYLIBS/DoNotDisturbServer.md)
- [/System/Library/PrivateFrameworks/DockKitCore.framework/DockKitCore](DYLIBS/DockKitCore.md)
- [/System/Library/PrivateFrameworks/DocumentManager.framework/DocumentManager](DYLIBS/DocumentManager.md)
- [/System/Library/PrivateFrameworks/DocumentManagerCore.framework/DocumentManagerCore](DYLIBS/DocumentManagerCore.md)
- [/System/Library/PrivateFrameworks/DocumentManagerExecutables.framework/DocumentManagerExecutables](DYLIBS/DocumentManagerExecutables.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/DocumentManagerUICore](DYLIBS/DocumentManagerUICore.md)
- [/System/Library/PrivateFrameworks/DocumentUnderstanding.framework/DocumentUnderstanding](DYLIBS/DocumentUnderstanding.md)
- [/System/Library/PrivateFrameworks/DocumentUnderstandingClient.framework/DocumentUnderstandingClient](DYLIBS/DocumentUnderstandingClient.md)
- [/System/Library/PrivateFrameworks/DrawingBoard.framework/DrawingBoard](DYLIBS/DrawingBoard.md)
- [/System/Library/PrivateFrameworks/DropInCore.framework/DropInCore](DYLIBS/DropInCore.md)
- [/System/Library/PrivateFrameworks/DropletUI.framework/DropletUI](DYLIBS/DropletUI.md)
- [/System/Library/PrivateFrameworks/DuetActivityScheduler.framework/DuetActivityScheduler](DYLIBS/DuetActivityScheduler.md)
- [/System/Library/PrivateFrameworks/Dyld.framework/Dyld](DYLIBS/Dyld.md)
- [/System/Library/PrivateFrameworks/EAP8021X.framework/EAP8021X](DYLIBS/EAP8021X.md)
- [/System/Library/PrivateFrameworks/EDPSecurity.framework/EDPSecurity](DYLIBS/EDPSecurity.md)
- [/System/Library/PrivateFrameworks/EXDisplayPipe.framework/EXDisplayPipe](DYLIBS/EXDisplayPipe.md)
- [/System/Library/PrivateFrameworks/EcosystemAnalytics.framework/EcosystemAnalytics](DYLIBS/EcosystemAnalytics.md)
- [/System/Library/PrivateFrameworks/Email.framework/Email](DYLIBS/Email.md)
- [/System/Library/PrivateFrameworks/EmailAddressing.framework/EmailAddressing](DYLIBS/EmailAddressing.md)
- [/System/Library/PrivateFrameworks/EmailCore.framework/EmailCore](DYLIBS/EmailCore.md)
- [/System/Library/PrivateFrameworks/EmailDaemon.framework/EmailDaemon](DYLIBS/EmailDaemon.md)
- [/System/Library/PrivateFrameworks/EmailFoundation.framework/EmailFoundation](DYLIBS/EmailFoundation.md)
- [/System/Library/PrivateFrameworks/EmbeddedAcousticRecognition.framework/EmbeddedAcousticRecognition](DYLIBS/EmbeddedAcousticRecognition.md)
- [/System/Library/PrivateFrameworks/EmbeddingService.framework/EmbeddingService](DYLIBS/EmbeddingService.md)
- [/System/Library/PrivateFrameworks/EmojiKit.framework/EmojiKit](DYLIBS/EmojiKit.md)
- [/System/Library/PrivateFrameworks/EnergyKit.framework/EnergyKit](DYLIBS/EnergyKit.md)
- [/System/Library/PrivateFrameworks/Espresso.framework/Espresso](DYLIBS/Espresso.md)
- [/System/Library/PrivateFrameworks/ExposureNotificationDaemon.framework/ExposureNotificationDaemon](DYLIBS/ExposureNotificationDaemon.md)
- [/System/Library/PrivateFrameworks/FMFCore.framework/FMFCore](DYLIBS/FMFCore.md)
- [/System/Library/PrivateFrameworks/FMFindingUI.framework/FMFindingUI](DYLIBS/FMFindingUI.md)
- [/System/Library/PrivateFrameworks/FMIPCore.framework/FMIPCore](DYLIBS/FMIPCore.md)
- [/System/Library/PrivateFrameworks/FSEvents.framework/FSEvents](DYLIBS/FSEvents.md)
- [/System/Library/PrivateFrameworks/FSKit.framework/FSKit](DYLIBS/FSKit.md)
- [/System/Library/PrivateFrameworks/FTServices.framework/FTServices](DYLIBS/FTServices.md)
- [/System/Library/PrivateFrameworks/FaceTimeFeatureControl.framework/FaceTimeFeatureControl](DYLIBS/FaceTimeFeatureControl.md)
- [/System/Library/PrivateFrameworks/FaceTimeMessageStore.framework/FaceTimeMessageStore](DYLIBS/FaceTimeMessageStore.md)
- [/System/Library/PrivateFrameworks/FamilyCircle.framework/FamilyCircle](DYLIBS/FamilyCircle.md)
- [/System/Library/PrivateFrameworks/FamilyCircleUI.framework/FamilyCircleUI](DYLIBS/FamilyCircleUI.md)
- [/System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags](DYLIBS/FeatureFlags.md)
- [/System/Library/PrivateFrameworks/FeatureStore.framework/FeatureStore](DYLIBS/FeatureStore.md)
- [/System/Library/PrivateFrameworks/FedStats.framework/FedStats](DYLIBS/FedStats.md)
- [/System/Library/PrivateFrameworks/FedStatsPluginCore.framework/FedStatsPluginCore](DYLIBS/FedStatsPluginCore.md)
- [/System/Library/PrivateFrameworks/Feedback.framework/Feedback](DYLIBS/Feedback.md)
- [/System/Library/PrivateFrameworks/FeedbackCore.framework/FeedbackCore](DYLIBS/FeedbackCore.md)
- [/System/Library/PrivateFrameworks/FeedbackService.framework/FeedbackService](DYLIBS/FeedbackService.md)
- [/System/Library/PrivateFrameworks/FileProviderDaemon.framework/FileProviderDaemon](DYLIBS/FileProviderDaemon.md)
- [/System/Library/PrivateFrameworks/FinanceDaemon.framework/FinanceDaemon](DYLIBS/FinanceDaemon.md)
- [/System/Library/PrivateFrameworks/FindMyBase.framework/FindMyBase](DYLIBS/FindMyBase.md)
- [/System/Library/PrivateFrameworks/FindMyCore.framework/FindMyCore](DYLIBS/FindMyCore.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/FindMyDevice](DYLIBS/FindMyDevice.md)
- [/System/Library/PrivateFrameworks/FindMyLocate.framework/FindMyLocate](DYLIBS/FindMyLocate.md)
- [/System/Library/PrivateFrameworks/FindMyServerInteraction.framework/FindMyServerInteraction](DYLIBS/FindMyServerInteraction.md)
- [/System/Library/PrivateFrameworks/FindMyUICore.framework/FindMyUICore](DYLIBS/FindMyUICore.md)
- [/System/Library/PrivateFrameworks/FitnessActions.framework/FitnessActions](DYLIBS/FitnessActions.md)
- [/System/Library/PrivateFrameworks/FitnessAppRoot.framework/FitnessAppRoot](DYLIBS/FitnessAppRoot.md)
- [/System/Library/PrivateFrameworks/FitnessAsset.framework/FitnessAsset](DYLIBS/FitnessAsset.md)
- [/System/Library/PrivateFrameworks/FitnessAwards.framework/FitnessAwards](DYLIBS/FitnessAwards.md)
- [/System/Library/PrivateFrameworks/FitnessBrowsing.framework/FitnessBrowsing](DYLIBS/FitnessBrowsing.md)
- [/System/Library/PrivateFrameworks/FitnessCanvas.framework/FitnessCanvas](DYLIBS/FitnessCanvas.md)
- [/System/Library/PrivateFrameworks/FitnessCanvasUI.framework/FitnessCanvasUI](DYLIBS/FitnessCanvasUI.md)
- [/System/Library/PrivateFrameworks/FitnessCoaching.framework/FitnessCoaching](DYLIBS/FitnessCoaching.md)
- [/System/Library/PrivateFrameworks/FitnessCoachingServices.framework/FitnessCoachingServices](DYLIBS/FitnessCoachingServices.md)
- [/System/Library/PrivateFrameworks/FitnessCoreUI.framework/FitnessCoreUI](DYLIBS/FitnessCoreUI.md)
- [/System/Library/PrivateFrameworks/FitnessFiltering.framework/FitnessFiltering](DYLIBS/FitnessFiltering.md)
- [/System/Library/PrivateFrameworks/FitnessForYou.framework/FitnessForYou](DYLIBS/FitnessForYou.md)
- [/System/Library/PrivateFrameworks/FitnessLibrary.framework/FitnessLibrary](DYLIBS/FitnessLibrary.md)
- [/System/Library/PrivateFrameworks/FitnessMarketing.framework/FitnessMarketing](DYLIBS/FitnessMarketing.md)
- [/System/Library/PrivateFrameworks/FitnessOnboarding.framework/FitnessOnboarding](DYLIBS/FitnessOnboarding.md)
- [/System/Library/PrivateFrameworks/FitnessProductDetail.framework/FitnessProductDetail](DYLIBS/FitnessProductDetail.md)
- [/System/Library/PrivateFrameworks/FitnessSearch.framework/FitnessSearch](DYLIBS/FitnessSearch.md)
- [/System/Library/PrivateFrameworks/FitnessSharePlaySession.framework/FitnessSharePlaySession](DYLIBS/FitnessSharePlaySession.md)
- [/System/Library/PrivateFrameworks/FitnessSiriSession.framework/FitnessSiriSession](DYLIBS/FitnessSiriSession.md)
- [/System/Library/PrivateFrameworks/FitnessSync.framework/FitnessSync](DYLIBS/FitnessSync.md)
- [/System/Library/PrivateFrameworks/FitnessTrainerTips.framework/FitnessTrainerTips](DYLIBS/FitnessTrainerTips.md)
- [/System/Library/PrivateFrameworks/FitnessUI.framework/FitnessUI](DYLIBS/FitnessUI.md)
- [/System/Library/PrivateFrameworks/FitnessUtilities.framework/FitnessUtilities](DYLIBS/FitnessUtilities.md)
- [/System/Library/PrivateFrameworks/FitnessWorkoutPlan.framework/FitnessWorkoutPlan](DYLIBS/FitnessWorkoutPlan.md)
- [/System/Library/PrivateFrameworks/FocusSettingsUI.framework/FocusSettingsUI](DYLIBS/FocusSettingsUI.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/FontServices](DYLIBS/FontServices.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/libFontParser.dylib](DYLIBS/libFontParser.dylib.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/libGSFont.dylib](DYLIBS/libGSFont.dylib.md)
- [/System/Library/PrivateFrameworks/FoundInAppsPlugins.framework/FoundInAppsPlugins](DYLIBS/FoundInAppsPlugins.md)
- [/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard](DYLIBS/FrontBoard.md)
- [/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices](DYLIBS/FrontBoardServices.md)
- [/System/Library/PrivateFrameworks/GRDBInternal.framework/GRDBInternal](DYLIBS/GRDBInternal.md)
- [/System/Library/PrivateFrameworks/GameCenterFoundation.framework/GameCenterFoundation](DYLIBS/GameCenterFoundation.md)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/GameCenterUI](DYLIBS/GameCenterUI.md)
- [/System/Library/PrivateFrameworks/GameServicesCore.framework/GameServicesCore](DYLIBS/GameServicesCore.md)
- [/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/GenerativeAssistantActions](DYLIBS/GenerativeAssistantActions.md)
- [/System/Library/PrivateFrameworks/GenerativeAssistantCommon.framework/GenerativeAssistantCommon](DYLIBS/GenerativeAssistantCommon.md)
- [/System/Library/PrivateFrameworks/GenerativeAssistantSettings.framework/GenerativeAssistantSettings](DYLIBS/GenerativeAssistantSettings.md)
- [/System/Library/PrivateFrameworks/GenerativeAssistantUI.framework/GenerativeAssistantUI](DYLIBS/GenerativeAssistantUI.md)
- [/System/Library/PrivateFrameworks/GenerativeExperiences.framework/GenerativeExperiences](DYLIBS/GenerativeExperiences.md)
- [/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/GenerativeExperiencesRuntime](DYLIBS/GenerativeExperiencesRuntime.md)
- [/System/Library/PrivateFrameworks/GenerativeExperiencesUI.framework/GenerativeExperiencesUI](DYLIBS/GenerativeExperiencesUI.md)
- [/System/Library/PrivateFrameworks/GenerativeFunctionsFoundation.framework/GenerativeFunctionsFoundation](DYLIBS/GenerativeFunctionsFoundation.md)
- [/System/Library/PrivateFrameworks/GenerativeFunctionsInstrumentation.framework/GenerativeFunctionsInstrumentation](DYLIBS/GenerativeFunctionsInstrumentation.md)
- [/System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels](DYLIBS/GenerativeModels.md)
- [/System/Library/PrivateFrameworks/GenerativeModelsFoundation.framework/GenerativeModelsFoundation](DYLIBS/GenerativeModelsFoundation.md)
- [/System/Library/PrivateFrameworks/GeoAnalytics.framework/GeoAnalytics](DYLIBS/GeoAnalytics.md)
- [/System/Library/PrivateFrameworks/GeoServices.framework/GeoServices](DYLIBS/GeoServices.md)
- [/System/Library/PrivateFrameworks/Geometry.framework/Geometry](DYLIBS/Geometry.md)
- [/System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices](DYLIBS/GraphicsServices.md)
- [/System/Library/PrivateFrameworks/HIDAnalytics.framework/HIDAnalytics](DYLIBS/HIDAnalytics.md)
- [/System/Library/PrivateFrameworks/HMFoundation.framework/HMFoundation](DYLIBS/HMFoundation.md)
- [/System/Library/PrivateFrameworks/Hands.framework/Hands](DYLIBS/Hands.md)
- [/System/Library/PrivateFrameworks/HangTracer.framework/HangTracer](DYLIBS/HangTracer.md)
- [/System/Library/PrivateFrameworks/HangTracerSettingsClient.framework/HangTracerSettingsClient](DYLIBS/HangTracerSettingsClient.md)
- [/System/Library/PrivateFrameworks/HeadGestures.framework/HeadGestures](DYLIBS/HeadGestures.md)
- [/System/Library/PrivateFrameworks/HealthAlgorithms.framework/HealthAlgorithms](DYLIBS/HealthAlgorithms.md)
- [/System/Library/PrivateFrameworks/HealthAppHealthDaemon.framework/HealthAppHealthDaemon](DYLIBS/HealthAppHealthDaemon.md)
- [/System/Library/PrivateFrameworks/HealthAppHealthDaemonSupport.framework/HealthAppHealthDaemonSupport](DYLIBS/HealthAppHealthDaemonSupport.md)
- [/System/Library/PrivateFrameworks/HealthAppServices.framework/HealthAppServices](DYLIBS/HealthAppServices.md)
- [/System/Library/PrivateFrameworks/HealthArticlesGeneration.framework/HealthArticlesGeneration](DYLIBS/HealthArticlesGeneration.md)
- [/System/Library/PrivateFrameworks/HealthBalance.framework/HealthBalance](DYLIBS/HealthBalance.md)
- [/System/Library/PrivateFrameworks/HealthBalanceUI.framework/HealthBalanceUI](DYLIBS/HealthBalanceUI.md)
- [/System/Library/PrivateFrameworks/HealthDaemonFoundation.framework/HealthDaemonFoundation](DYLIBS/HealthDaemonFoundation.md)
- [/System/Library/PrivateFrameworks/HealthDomainsTools.framework/HealthDomainsTools](DYLIBS/HealthDomainsTools.md)
- [/System/Library/PrivateFrameworks/HealthExperience.framework/HealthExperience](DYLIBS/HealthExperience.md)
- [/System/Library/PrivateFrameworks/HealthExperienceUI.framework/HealthExperienceUI](DYLIBS/HealthExperienceUI.md)
- [/System/Library/PrivateFrameworks/HealthExposureNotificationUI.framework/HealthExposureNotificationUI](DYLIBS/HealthExposureNotificationUI.md)
- [/System/Library/PrivateFrameworks/HealthKitAdditions.framework/HealthKitAdditions](DYLIBS/HealthKitAdditions.md)
- [/System/Library/PrivateFrameworks/HealthMedications.framework/HealthMedications](DYLIBS/HealthMedications.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsDaemonPlugin.framework/HealthMedicationsDaemonPlugin](DYLIBS/HealthMedicationsDaemonPlugin.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsUI.framework/HealthMedicationsUI](DYLIBS/HealthMedicationsUI.md)
- [/System/Library/PrivateFrameworks/HealthMenstrualCycles.framework/HealthMenstrualCycles](DYLIBS/HealthMenstrualCycles.md)
- [/System/Library/PrivateFrameworks/HealthMenstrualCyclesDaemon.framework/HealthMenstrualCyclesDaemon](DYLIBS/HealthMenstrualCyclesDaemon.md)
- [/System/Library/PrivateFrameworks/HealthMobilityUI.framework/HealthMobilityUI](DYLIBS/HealthMobilityUI.md)
- [/System/Library/PrivateFrameworks/HealthPlatform.framework/HealthPlatform](DYLIBS/HealthPlatform.md)
- [/System/Library/PrivateFrameworks/HealthPlatformCore.framework/HealthPlatformCore](DYLIBS/HealthPlatformCore.md)
- [/System/Library/PrivateFrameworks/HealthPluginHost.framework/HealthPluginHost](DYLIBS/HealthPluginHost.md)
- [/System/Library/PrivateFrameworks/HealthRecordServices.framework/HealthRecordServices](DYLIBS/HealthRecordServices.md)
- [/System/Library/PrivateFrameworks/HealthRecordsConceptsSupport.framework/HealthRecordsConceptsSupport](DYLIBS/HealthRecordsConceptsSupport.md)
- [/System/Library/PrivateFrameworks/HealthRecordsDaemon.framework/HealthRecordsDaemon](DYLIBS/HealthRecordsDaemon.md)
- [/System/Library/PrivateFrameworks/HealthRecordsUI.framework/HealthRecordsUI](DYLIBS/HealthRecordsUI.md)
- [/System/Library/PrivateFrameworks/HealthUI.framework/HealthUI](DYLIBS/HealthUI.md)
- [/System/Library/PrivateFrameworks/HealthVisualization.framework/HealthVisualization](DYLIBS/HealthVisualization.md)
- [/System/Library/PrivateFrameworks/HearingTest.framework/HearingTest](DYLIBS/HearingTest.md)
- [/System/Library/PrivateFrameworks/HearingTestUI.framework/HearingTestUI](DYLIBS/HearingTestUI.md)
- [/System/Library/PrivateFrameworks/HeartHealthDaemon.framework/HeartHealthDaemon](DYLIBS/HeartHealthDaemon.md)
- [/System/Library/PrivateFrameworks/HelpKit.framework/HelpKit](DYLIBS/HelpKit.md)
- [/System/Library/PrivateFrameworks/Home.framework/Home](DYLIBS/Home.md)
- [/System/Library/PrivateFrameworks/HomeAI.framework/HomeAI](DYLIBS/HomeAI.md)
- [/System/Library/PrivateFrameworks/HomeAccessoryControlUI.framework/HomeAccessoryControlUI](DYLIBS/HomeAccessoryControlUI.md)
- [/System/Library/PrivateFrameworks/HomeAppIntents.framework/HomeAppIntents](DYLIBS/HomeAppIntents.md)
- [/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/HomeAutomationInternal](DYLIBS/HomeAutomationInternal.md)
- [/System/Library/PrivateFrameworks/HomeAutomationUIFramework.framework/HomeAutomationUIFramework](DYLIBS/HomeAutomationUIFramework.md)
- [/System/Library/PrivateFrameworks/HomeDataModel.framework/HomeDataModel](DYLIBS/HomeDataModel.md)
- [/System/Library/PrivateFrameworks/HomeDeviceSetup.framework/HomeDeviceSetup](DYLIBS/HomeDeviceSetup.md)
- [/System/Library/PrivateFrameworks/HomeEnergyDaemon.framework/HomeEnergyDaemon](DYLIBS/HomeEnergyDaemon.md)
- [/System/Library/PrivateFrameworks/HomeEnergyUI.framework/HomeEnergyUI](DYLIBS/HomeEnergyUI.md)
- [/System/Library/PrivateFrameworks/HomeKitBackingStore.framework/HomeKitBackingStore](DYLIBS/HomeKitBackingStore.md)
- [/System/Library/PrivateFrameworks/HomeKitCore.framework/HomeKitCore](DYLIBS/HomeKitCore.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemon.framework/HomeKitDaemon](DYLIBS/HomeKitDaemon.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemonFoundation.framework/HomeKitDaemonFoundation](DYLIBS/HomeKitDaemonFoundation.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemonLegacy.framework/HomeKitDaemonLegacy](DYLIBS/HomeKitDaemonLegacy.md)
- [/System/Library/PrivateFrameworks/HomeKitEventRouter.framework/HomeKitEventRouter](DYLIBS/HomeKitEventRouter.md)
- [/System/Library/PrivateFrameworks/HomeKitEvents.framework/HomeKitEvents](DYLIBS/HomeKitEvents.md)
- [/System/Library/PrivateFrameworks/HomeKitMatter.framework/HomeKitMatter](DYLIBS/HomeKitMatter.md)
- [/System/Library/PrivateFrameworks/HomeKitMetrics.framework/HomeKitMetrics](DYLIBS/HomeKitMetrics.md)
- [/System/Library/PrivateFrameworks/HomePodSettings.framework/HomePodSettings](DYLIBS/HomePodSettings.md)
- [/System/Library/PrivateFrameworks/HomeServices.framework/HomeServices](DYLIBS/HomeServices.md)
- [/System/Library/PrivateFrameworks/HomeUI.framework/HomeUI](DYLIBS/HomeUI.md)
- [/System/Library/PrivateFrameworks/HomeUI2.framework/HomeUI2](DYLIBS/HomeUI2.md)
- [/System/Library/PrivateFrameworks/HomeUICommon.framework/HomeUICommon](DYLIBS/HomeUICommon.md)
- [/System/Library/PrivateFrameworks/HomeUtilityServices.framework/HomeUtilityServices](DYLIBS/HomeUtilityServices.md)
- [/System/Library/PrivateFrameworks/HoverTextUI.framework/HoverTextUI](DYLIBS/HoverTextUI.md)
- [/System/Library/PrivateFrameworks/Human.framework/Human](DYLIBS/Human.md)
- [/System/Library/PrivateFrameworks/HumanUI.framework/HumanUI](DYLIBS/HumanUI.md)
- [/System/Library/PrivateFrameworks/HumanUnderstandingEvidence.framework/HumanUnderstandingEvidence](DYLIBS/HumanUnderstandingEvidence.md)
- [/System/Library/PrivateFrameworks/HumanUnderstandingFoundation.framework/HumanUnderstandingFoundation](DYLIBS/HumanUnderstandingFoundation.md)
- [/System/Library/PrivateFrameworks/IDS.framework/IDS](DYLIBS/IDS.md)
- [/System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation](DYLIBS/IDSFoundation.md)
- [/System/Library/PrivateFrameworks/IMCore.framework/IMCore](DYLIBS/IMCore.md)
- [/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence](DYLIBS/IMDPersistence.md)
- [/System/Library/PrivateFrameworks/IMDaemonCore.framework/IMDaemonCore](DYLIBS/IMDaemonCore.md)
- [/System/Library/PrivateFrameworks/IMFoundation.framework/IMFoundation](DYLIBS/IMFoundation.md)
- [/System/Library/PrivateFrameworks/IMSharedUI.framework/IMSharedUI](DYLIBS/IMSharedUI.md)
- [/System/Library/PrivateFrameworks/IMSharedUtilities.framework/IMSharedUtilities](DYLIBS/IMSharedUtilities.md)
- [/System/Library/PrivateFrameworks/IO80211.framework/IO80211](DYLIBS/IO80211.md)
- [/System/Library/PrivateFrameworks/IOAccelerator.framework/IOAccelerator](DYLIBS/IOAccelerator.md)
- [/System/Library/PrivateFrameworks/IOAccessoryManager.framework/IOAccessoryManager](DYLIBS/IOAccessoryManager.md)
- [/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU](DYLIBS/IOGPU.md)
- [/System/Library/PrivateFrameworks/IOKitten.framework/IOKitten](DYLIBS/IOKitten.md)
- [/System/Library/PrivateFrameworks/IOSurfaceAccelerator.framework/IOSurfaceAccelerator](DYLIBS/IOSurfaceAccelerator.md)
- [/System/Library/PrivateFrameworks/IPTelephony.framework/Support/libIPTelephony.dylib](DYLIBS/libIPTelephony.dylib.md)
- [/System/Library/PrivateFrameworks/IconFoundation.framework/IconFoundation](DYLIBS/IconFoundation.md)
- [/System/Library/PrivateFrameworks/IconServices.framework/IconServices](DYLIBS/IconServices.md)
- [/System/Library/PrivateFrameworks/ImagePlaygroundInternal.framework/ImagePlaygroundInternal](DYLIBS/ImagePlaygroundInternal.md)
- [/System/Library/PrivateFrameworks/InAppMessages.framework/InAppMessages](DYLIBS/InAppMessages.md)
- [/System/Library/PrivateFrameworks/InertiaCam.framework/InertiaCam](DYLIBS/InertiaCam.md)
- [/System/Library/PrivateFrameworks/InputAccessoriesSettings.framework/InputAccessoriesSettings](DYLIBS/InputAccessoriesSettings.md)
- [/System/Library/PrivateFrameworks/InputAnalytics.framework/InputAnalytics](DYLIBS/InputAnalytics.md)
- [/System/Library/PrivateFrameworks/InputAnalyticsServer.framework/InputAnalyticsServer](DYLIBS/InputAnalyticsServer.md)
- [/System/Library/PrivateFrameworks/IntelligenceEngine.framework/IntelligenceEngine](DYLIBS/IntelligenceEngine.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlow.framework/IntelligenceFlow](DYLIBS/IntelligenceFlow.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowContext.framework/IntelligenceFlowContext](DYLIBS/IntelligenceFlowContext.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowContextRuntime.framework/IntelligenceFlowContextRuntime](DYLIBS/IntelligenceFlowContextRuntime.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/IntelligenceFlowPlannerRuntime](DYLIBS/IntelligenceFlowPlannerRuntime.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowPlannerSupport.framework/IntelligenceFlowPlannerSupport](DYLIBS/IntelligenceFlowPlannerSupport.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/IntelligenceFlowRuntime](DYLIBS/IntelligenceFlowRuntime.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowShared.framework/IntelligenceFlowShared](DYLIBS/IntelligenceFlowShared.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatform.framework/IntelligencePlatform](DYLIBS/IntelligencePlatform.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/IntelligencePlatformCore](DYLIBS/IntelligencePlatformCore.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformLibrary.framework/IntelligencePlatformLibrary](DYLIBS/IntelligencePlatformLibrary.md)
- [/System/Library/PrivateFrameworks/IntelligentRoutingDaemon.framework/IntelligentRoutingDaemon](DYLIBS/IntelligentRoutingDaemon.md)
- [/System/Library/PrivateFrameworks/IntelligentRoutingMediaBundles.framework/IntelligentRoutingMediaBundles](DYLIBS/IntelligentRoutingMediaBundles.md)
- [/System/Library/PrivateFrameworks/IntelligentTrackingCore.framework/IntelligentTrackingCore](DYLIBS/IntelligentTrackingCore.md)
- [/System/Library/PrivateFrameworks/IntentsCore.framework/IntentsCore](DYLIBS/IntentsCore.md)
- [/System/Library/PrivateFrameworks/IntentsFoundation.framework/IntentsFoundation](DYLIBS/IntentsFoundation.md)
- [/System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf](DYLIBS/InternalSwiftProtobuf.md)
- [/System/Library/PrivateFrameworks/InternationalSupport.framework/InternationalSupport](DYLIBS/InternationalSupport.md)
- [/System/Library/PrivateFrameworks/IntlPreferences.framework/IntlPreferences](DYLIBS/IntlPreferences.md)
- [/System/Library/PrivateFrameworks/IsolatedCoreAudioClient.framework/IsolatedCoreAudioClient](DYLIBS/IsolatedCoreAudioClient.md)
- [/System/Library/PrivateFrameworks/JetEngine.framework/JetEngine](DYLIBS/JetEngine.md)
- [/System/Library/PrivateFrameworks/JetUI.framework/JetUI](DYLIBS/JetUI.md)
- [/System/Library/PrivateFrameworks/KeyboardArbiter.framework/KeyboardArbiter](DYLIBS/KeyboardArbiter.md)
- [/System/Library/PrivateFrameworks/KeyboardSettings.framework/KeyboardSettings](DYLIBS/KeyboardSettings.md)
- [/System/Library/PrivateFrameworks/KeyboardSettingsFeedback.framework/KeyboardSettingsFeedback](DYLIBS/KeyboardSettingsFeedback.md)
- [/System/Library/PrivateFrameworks/KnowledgeGraphKit.framework/KnowledgeGraphKit](DYLIBS/KnowledgeGraphKit.md)
- [/System/Library/PrivateFrameworks/KnowledgeMonitor.framework/KnowledgeMonitor](DYLIBS/KnowledgeMonitor.md)
- [/System/Library/PrivateFrameworks/Koa.framework/Koa](DYLIBS/Koa.md)
- [/System/Library/PrivateFrameworks/KoaMapper.framework/KoaMapper](DYLIBS/KoaMapper.md)
- [/System/Library/PrivateFrameworks/LiftUI.framework/LiftUI](DYLIBS/LiftUI.md)
- [/System/Library/PrivateFrameworks/LighthouseAV.framework/LighthouseAV](DYLIBS/LighthouseAV.md)
- [/System/Library/PrivateFrameworks/LighthouseBackground.framework/LighthouseBackground](DYLIBS/LighthouseBackground.md)
- [/System/Library/PrivateFrameworks/LighthouseDataProcessor.framework/LighthouseDataProcessor](DYLIBS/LighthouseDataProcessor.md)
- [/System/Library/PrivateFrameworks/LimitAdTracking.framework/LimitAdTracking](DYLIBS/LimitAdTracking.md)
- [/System/Library/PrivateFrameworks/LinkMetadata.framework/LinkMetadata](DYLIBS/LinkMetadata.md)
- [/System/Library/PrivateFrameworks/LinkServices.framework/LinkServices](DYLIBS/LinkServices.md)
- [/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore](DYLIBS/LocalAuthenticationCore.md)
- [/System/Library/PrivateFrameworks/LocationSupport.framework/LocationSupport](DYLIBS/LocationSupport.md)
- [/System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport](DYLIBS/LoggingSupport.md)
- [/System/Library/PrivateFrameworks/MCCKitCategorization.framework/MCCKitCategorization](DYLIBS/MCCKitCategorization.md)
- [/System/Library/PrivateFrameworks/MDMClientLibrary.framework/MDMClientLibrary](DYLIBS/MDMClientLibrary.md)
- [/System/Library/PrivateFrameworks/MIME.framework/MIME](DYLIBS/MIME.md)
- [/System/Library/PrivateFrameworks/MLModelSpecification.framework/MLModelSpecification](DYLIBS/MLModelSpecification.md)
- [/System/Library/PrivateFrameworks/MMCS.framework/MMCS](DYLIBS/MMCS.md)
- [/System/Library/PrivateFrameworks/MTLCompiler.framework/Versions/32024/MTLCompiler](DYLIBS/MTLCompiler.md)
- [/System/Library/PrivateFrameworks/MTLToolsDeviceSupport.framework/MTLToolsDeviceSupport](DYLIBS/MTLToolsDeviceSupport.md)
- [/System/Library/PrivateFrameworks/MagnifierSupport.framework/MagnifierSupport](DYLIBS/MagnifierSupport.md)
- [/System/Library/PrivateFrameworks/MailSupport.framework/MailSupport](DYLIBS/MailSupport.md)
- [/System/Library/PrivateFrameworks/MailUI.framework/MailUI](DYLIBS/MailUI.md)
- [/System/Library/PrivateFrameworks/MallocStackLogging.framework/MallocStackLogging](DYLIBS/MallocStackLogging.md)
- [/System/Library/PrivateFrameworks/ManagedAppsCore.framework/ManagedAppsCore](DYLIBS/ManagedAppsCore.md)
- [/System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration](DYLIBS/ManagedConfiguration.md)
- [/System/Library/PrivateFrameworks/ManagedSettingsObjC.framework/ManagedSettingsObjC](DYLIBS/ManagedSettingsObjC.md)
- [/System/Library/PrivateFrameworks/MapsSuggestions.framework/MapsSuggestions](DYLIBS/MapsSuggestions.md)
- [/System/Library/PrivateFrameworks/MapsSupport.framework/MapsSupport](DYLIBS/MapsSupport.md)
- [/System/Library/PrivateFrameworks/MapsSync.framework/MapsSync](DYLIBS/MapsSync.md)
- [/System/Library/PrivateFrameworks/MapsUI.framework/MapsUI](DYLIBS/MapsUI.md)
- [/System/Library/PrivateFrameworks/Marrs.framework/Marrs](DYLIBS/Marrs.md)
- [/System/Library/PrivateFrameworks/MaterialKit.framework/MaterialKit](DYLIBS/MaterialKit.md)
- [/System/Library/PrivateFrameworks/MatterPlugin.framework/MatterPlugin](DYLIBS/MatterPlugin.md)
- [/System/Library/PrivateFrameworks/MeasureFoundation.framework/MeasureFoundation](DYLIBS/MeasureFoundation.md)
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/MediaAnalysis](DYLIBS/MediaAnalysis.md)
- [/System/Library/PrivateFrameworks/MediaControlSender.framework/MediaControlSender](DYLIBS/MediaControlSender.md)
- [/System/Library/PrivateFrameworks/MediaControls.framework/MediaControls](DYLIBS/MediaControls.md)
- [/System/Library/PrivateFrameworks/MediaCoreUI.framework/MediaCoreUI](DYLIBS/MediaCoreUI.md)
- [/System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience](DYLIBS/MediaExperience.md)
- [/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore](DYLIBS/MediaPlaybackCore.md)
- [/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote](DYLIBS/MediaRemote.md)
- [/System/Library/PrivateFrameworks/MediaSafetyNet.framework/MediaSafetyNet](DYLIBS/MediaSafetyNet.md)
- [/System/Library/PrivateFrameworks/MediaServices.framework/MediaServices](DYLIBS/MediaServices.md)
- [/System/Library/PrivateFrameworks/Message.framework/Message](DYLIBS/Message.md)
- [/System/Library/PrivateFrameworks/MessageProtection.framework/MessageProtection](DYLIBS/MessageProtection.md)
- [/System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity](DYLIBS/MessageSecurity.md)
- [/System/Library/PrivateFrameworks/MessagesCloudSync.framework/MessagesCloudSync](DYLIBS/MessagesCloudSync.md)
- [/System/Library/PrivateFrameworks/MetadataUtilities.framework/MetadataUtilities](DYLIBS/MetadataUtilities.md)
- [/System/Library/PrivateFrameworks/MetricsFramework.framework/MetricsFramework](DYLIBS/MetricsFramework.md)
- [/System/Library/PrivateFrameworks/MicroLocation.framework/MicroLocation](DYLIBS/MicroLocation.md)
- [/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon](DYLIBS/MicroLocationDaemon.md)
- [/System/Library/PrivateFrameworks/MigrationKit.framework/MigrationKit](DYLIBS/MigrationKit.md)
- [/System/Library/PrivateFrameworks/MobileActivation.framework/MobileActivation](DYLIBS/MobileActivation.md)
- [/System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset](DYLIBS/MobileAsset.md)
- [/System/Library/PrivateFrameworks/MobileAssetExclaveServices.framework/MobileAssetExclaveServices](DYLIBS/MobileAssetExclaveServices.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup](DYLIBS/MobileBackup.md)
- [/System/Library/PrivateFrameworks/MobileBluetooth.framework/MobileBluetooth](DYLIBS/MobileBluetooth.md)
- [/System/Library/PrivateFrameworks/MobileInBoxUpdate.framework/MobileInBoxUpdate](DYLIBS/MobileInBoxUpdate.md)
- [/System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag](DYLIBS/MobileKeyBag.md)
- [/System/Library/PrivateFrameworks/MobileMulticastTransfer.framework/MobileMulticastTransfer](DYLIBS/MobileMulticastTransfer.md)
- [/System/Library/PrivateFrameworks/MobileSafari.framework/MobileSafari](DYLIBS/MobileSafari.md)
- [/System/Library/PrivateFrameworks/MobileSafariUI.framework/MobileSafariUI](DYLIBS/MobileSafariUI.md)
- [/System/Library/PrivateFrameworks/MobileSpotlightIndex.framework/MobileSpotlightIndex](DYLIBS/MobileSpotlightIndex.md)
- [/System/Library/PrivateFrameworks/MobileStoreDemoKit.framework/MobileStoreDemoKit](DYLIBS/MobileStoreDemoKit.md)
- [/System/Library/PrivateFrameworks/MobileStoreDemoSetupUI.framework/MobileStoreDemoSetupUI](DYLIBS/MobileStoreDemoSetupUI.md)
- [/System/Library/PrivateFrameworks/MobileStoreUI.framework/MobileStoreUI](DYLIBS/MobileStoreUI.md)
- [/System/Library/PrivateFrameworks/MobileTimer.framework/MobileTimer](DYLIBS/MobileTimer.md)
- [/System/Library/PrivateFrameworks/MobileTimerSupport.framework/MobileTimerSupport](DYLIBS/MobileTimerSupport.md)
- [/System/Library/PrivateFrameworks/MobileTimerUI.framework/MobileTimerUI](DYLIBS/MobileTimerUI.md)
- [/System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi](DYLIBS/MobileWiFi.md)
- [/System/Library/PrivateFrameworks/ModelCatalog.framework/ModelCatalog](DYLIBS/ModelCatalog.md)
- [/System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/ModelCatalogRuntime](DYLIBS/ModelCatalogRuntime.md)
- [/System/Library/PrivateFrameworks/ModelManagerServices.framework/ModelManagerServices](DYLIBS/ModelManagerServices.md)
- [/System/Library/PrivateFrameworks/Moments.framework/Moments](DYLIBS/Moments.md)
- [/System/Library/PrivateFrameworks/MomentsOnboardingAndSettings.framework/MomentsOnboardingAndSettings](DYLIBS/MomentsOnboardingAndSettings.md)
- [/System/Library/PrivateFrameworks/Morpheus.framework/Morpheus](DYLIBS/Morpheus.md)
- [/System/Library/PrivateFrameworks/MorpheusExtensions.framework/MorpheusExtensions](DYLIBS/MorpheusExtensions.md)
- [/System/Library/PrivateFrameworks/MorphunAssets.framework/MorphunAssets](DYLIBS/MorphunAssets.md)
- [/System/Library/PrivateFrameworks/MusicKitInternal.framework/MusicKitInternal](DYLIBS/MusicKitInternal.md)
- [/System/Library/PrivateFrameworks/MusicLibrary.framework/MusicLibrary](DYLIBS/MusicLibrary.md)
- [/System/Library/PrivateFrameworks/MusicUI.framework/MusicUI](DYLIBS/MusicUI.md)
- [/System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync](DYLIBS/NanoPreferencesSync.md)
- [/System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry](DYLIBS/NanoRegistry.md)
- [/System/Library/PrivateFrameworks/NanoSystemSettings.framework/NanoSystemSettings](DYLIBS/NanoSystemSettings.md)
- [/System/Library/PrivateFrameworks/NanoTimeKit.framework/NanoTimeKit](DYLIBS/NanoTimeKit.md)
- [/System/Library/PrivateFrameworks/NearField.framework/NearField](DYLIBS/NearField.md)
- [/System/Library/PrivateFrameworks/NetAppsUtilities.framework/NetAppsUtilities](DYLIBS/NetAppsUtilities.md)
- [/System/Library/PrivateFrameworks/NetworkInfo.framework/NetworkInfo](DYLIBS/NetworkInfo.md)
- [/System/Library/PrivateFrameworks/NetworkRelay.framework/NetworkRelay](DYLIBS/NetworkRelay.md)
- [/System/Library/PrivateFrameworks/NetworkServiceProxy.framework/NetworkServiceProxy](DYLIBS/NetworkServiceProxy.md)
- [/System/Library/PrivateFrameworks/NetworkStatistics.framework/NetworkStatistics](DYLIBS/NetworkStatistics.md)
- [/System/Library/PrivateFrameworks/NeuralNetworks.framework/NeuralNetworks](DYLIBS/NeuralNetworks.md)
- [/System/Library/PrivateFrameworks/NeutrinoCore.framework/NeutrinoCore](DYLIBS/NeutrinoCore.md)
- [/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/NewDeviceOutreach](DYLIBS/NewDeviceOutreach.md)
- [/System/Library/PrivateFrameworks/NewDeviceOutreachUI.framework/NewDeviceOutreachUI](DYLIBS/NewDeviceOutreachUI.md)
- [/System/Library/PrivateFrameworks/NewsAds.framework/NewsAds](DYLIBS/NewsAds.md)
- [/System/Library/PrivateFrameworks/NewsAnalytics.framework/NewsAnalytics](DYLIBS/NewsAnalytics.md)
- [/System/Library/PrivateFrameworks/NewsArticles.framework/NewsArticles](DYLIBS/NewsArticles.md)
- [/System/Library/PrivateFrameworks/NewsCore.framework/NewsCore](DYLIBS/NewsCore.md)
- [/System/Library/PrivateFrameworks/NewsEngagement.framework/NewsEngagement](DYLIBS/NewsEngagement.md)
- [/System/Library/PrivateFrameworks/NewsEngagementCollector.framework/NewsEngagementCollector](DYLIBS/NewsEngagementCollector.md)
- [/System/Library/PrivateFrameworks/NewsFeed.framework/NewsFeed](DYLIBS/NewsFeed.md)
- [/System/Library/PrivateFrameworks/NewsFoundation.framework/NewsFoundation](DYLIBS/NewsFoundation.md)
- [/System/Library/PrivateFrameworks/NewsLiveActivitiesCore.framework/NewsLiveActivitiesCore](DYLIBS/NewsLiveActivitiesCore.md)
- [/System/Library/PrivateFrameworks/NewsPersonalization.framework/NewsPersonalization](DYLIBS/NewsPersonalization.md)
- [/System/Library/PrivateFrameworks/NewsSubscription.framework/NewsSubscription](DYLIBS/NewsSubscription.md)
- [/System/Library/PrivateFrameworks/NewsToday.framework/NewsToday](DYLIBS/NewsToday.md)
- [/System/Library/PrivateFrameworks/NewsTransport.framework/NewsTransport](DYLIBS/NewsTransport.md)
- [/System/Library/PrivateFrameworks/NewsUI.framework/NewsUI](DYLIBS/NewsUI.md)
- [/System/Library/PrivateFrameworks/NewsUI2.framework/NewsUI2](DYLIBS/NewsUI2.md)
- [/System/Library/PrivateFrameworks/Nexus.framework/Nexus](DYLIBS/Nexus.md)
- [/System/Library/PrivateFrameworks/NightingaleTraining.framework/NightingaleTraining](DYLIBS/NightingaleTraining.md)
- [/System/Library/PrivateFrameworks/Notes.framework/Notes](DYLIBS/Notes.md)
- [/System/Library/PrivateFrameworks/NotesAnalytics.framework/NotesAnalytics](DYLIBS/NotesAnalytics.md)
- [/System/Library/PrivateFrameworks/NotesEditor.framework/NotesEditor](DYLIBS/NotesEditor.md)
- [/System/Library/PrivateFrameworks/NotesShared.framework/NotesShared](DYLIBS/NotesShared.md)
- [/System/Library/PrivateFrameworks/NotesSupport.framework/NotesSupport](DYLIBS/NotesSupport.md)
- [/System/Library/PrivateFrameworks/NotesUI.framework/NotesUI](DYLIBS/NotesUI.md)
- [/System/Library/PrivateFrameworks/ODDIFramework.framework/ODDIFramework](DYLIBS/ODDIFramework.md)
- [/System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics](DYLIBS/OSAnalytics.md)
- [/System/Library/PrivateFrameworks/OSEligibility.framework/OSEligibility](DYLIBS/OSEligibility.md)
- [/System/Library/PrivateFrameworks/OSIntelligence.framework/OSIntelligence](DYLIBS/OSIntelligence.md)
- [/System/Library/PrivateFrameworks/OmniSearch.framework/OmniSearch](DYLIBS/OmniSearch.md)
- [/System/Library/PrivateFrameworks/OmniSearchTypes.framework/OmniSearchTypes](DYLIBS/OmniSearchTypes.md)
- [/System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit](DYLIBS/OnBoardingKit.md)
- [/System/Library/PrivateFrameworks/OnDeviceStorageCore.framework/OnDeviceStorageCore](DYLIBS/OnDeviceStorageCore.md)
- [/System/Library/PrivateFrameworks/OnDeviceStorageInternal.framework/OnDeviceStorageInternal](DYLIBS/OnDeviceStorageInternal.md)
- [/System/Library/PrivateFrameworks/OpenAPIURLSessionInternal.framework/OpenAPIURLSessionInternal](DYLIBS/OpenAPIURLSessionInternal.md)
- [/System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry](DYLIBS/PairedDeviceRegistry.md)
- [/System/Library/PrivateFrameworks/PairedSync.framework/PairedSync](DYLIBS/PairedSync.md)
- [/System/Library/PrivateFrameworks/PairingProximity.framework/PairingProximity](DYLIBS/PairingProximity.md)
- [/System/Library/PrivateFrameworks/PaperBoardUI.framework/PaperBoardUI](DYLIBS/PaperBoardUI.md)
- [/System/Library/PrivateFrameworks/PaperKit.framework/PaperKit](DYLIBS/PaperKit.md)
- [/System/Library/PrivateFrameworks/ParsecSubscriptionServiceSupport.framework/ParsecSubscriptionServiceSupport](DYLIBS/ParsecSubscriptionServiceSupport.md)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore](DYLIBS/PassKitCore.md)
- [/System/Library/PrivateFrameworks/PassKitUI.framework/PassKitUI](DYLIBS/PassKitUI.md)
- [/System/Library/PrivateFrameworks/PasswordManagerUI.framework/PasswordManagerUI](DYLIBS/PasswordManagerUI.md)
- [/System/Library/PrivateFrameworks/Pasteboard.framework/Pasteboard](DYLIBS/Pasteboard.md)
- [/System/Library/PrivateFrameworks/PegasusConfiguration.framework/PegasusConfiguration](DYLIBS/PegasusConfiguration.md)
- [/System/Library/PrivateFrameworks/PegasusKit.framework/PegasusKit](DYLIBS/PegasusKit.md)
- [/System/Library/PrivateFrameworks/PegasusPersistence.framework/PegasusPersistence](DYLIBS/PegasusPersistence.md)
- [/System/Library/PrivateFrameworks/PeopleSuggesterLighthouse.framework/PeopleSuggesterLighthouse](DYLIBS/PeopleSuggesterLighthouse.md)
- [/System/Library/PrivateFrameworks/PerformanceControlKit.framework/PerformanceControlKit](DYLIBS/PerformanceControlKit.md)
- [/System/Library/PrivateFrameworks/PersistentConnection.framework/PersistentConnection](DYLIBS/PersistentConnection.md)
- [/System/Library/PrivateFrameworks/PersonaKit.framework/PersonaKit](DYLIBS/PersonaKit.md)
- [/System/Library/PrivateFrameworks/PersonaUI.framework/PersonaUI](DYLIBS/PersonaUI.md)
- [/System/Library/PrivateFrameworks/PersonalizationPortraitInternals.framework/PersonalizationPortraitInternals](DYLIBS/PersonalizationPortraitInternals.md)
- [/System/Library/PrivateFrameworks/PersonalizedSensing.framework/PersonalizedSensing](DYLIBS/PersonalizedSensing.md)
- [/System/Library/PrivateFrameworks/PhoneNumberResolver.framework/PhoneNumberResolver](DYLIBS/PhoneNumberResolver.md)
- [/System/Library/PrivateFrameworks/PhoneSnippetUI.framework/PhoneSnippetUI](DYLIBS/PhoneSnippetUI.md)
- [/System/Library/PrivateFrameworks/PhotoAnalysis.framework/PhotoAnalysis](DYLIBS/PhotoAnalysis.md)
- [/System/Library/PrivateFrameworks/PhotoImaging.framework/PhotoImaging](DYLIBS/PhotoImaging.md)
- [/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/PhotoLibraryServices](DYLIBS/PhotoLibraryServices.md)
- [/System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/PhotoLibraryServicesCore](DYLIBS/PhotoLibraryServicesCore.md)
- [/System/Library/PrivateFrameworks/PhotosGraph.framework/PhotosGraph](DYLIBS/PhotosGraph.md)
- [/System/Library/PrivateFrameworks/PhotosIntelligence.framework/PhotosIntelligence](DYLIBS/PhotosIntelligence.md)
- [/System/Library/PrivateFrameworks/PhotosSwiftUICore.framework/PhotosSwiftUICore](DYLIBS/PhotosSwiftUICore.md)
- [/System/Library/PrivateFrameworks/PhotosUICore.framework/PhotosUICore](DYLIBS/PhotosUICore.md)
- [/System/Library/PrivateFrameworks/PhotosUIEdit.framework/PhotosUIEdit](DYLIBS/PhotosUIEdit.md)
- [/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PhotosUIPrivate](DYLIBS/PhotosUIPrivate.md)
- [/System/Library/PrivateFrameworks/PlugInKit.framework/PlugInKit](DYLIBS/PlugInKit.md)
- [/System/Library/PrivateFrameworks/PnROnDeviceFramework.framework/PnROnDeviceFramework](DYLIBS/PnROnDeviceFramework.md)
- [/System/Library/PrivateFrameworks/PodcastsFoundation.framework/PodcastsFoundation](DYLIBS/PodcastsFoundation.md)
- [/System/Library/PrivateFrameworks/PodcastsKit.framework/PodcastsKit](DYLIBS/PodcastsKit.md)
- [/System/Library/PrivateFrameworks/PodcastsUI.framework/PodcastsUI](DYLIBS/PodcastsUI.md)
- [/System/Library/PrivateFrameworks/PoirotSchematizer.framework/PoirotSchematizer](DYLIBS/PoirotSchematizer.md)
- [/System/Library/PrivateFrameworks/PoirotUDFs.framework/PoirotUDFs](DYLIBS/PoirotUDFs.md)
- [/System/Library/PrivateFrameworks/PosterBoard.framework/PosterBoard](DYLIBS/PosterBoard.md)
- [/System/Library/PrivateFrameworks/PosterKit.framework/PosterKit](DYLIBS/PosterKit.md)
- [/System/Library/PrivateFrameworks/PosterUIFoundation.framework/PosterUIFoundation](DYLIBS/PosterUIFoundation.md)
- [/System/Library/PrivateFrameworks/PowerExperience.framework/PowerExperience](DYLIBS/PowerExperience.md)
- [/System/Library/PrivateFrameworks/PowerLog.framework/PowerLog](DYLIBS/PowerLog.md)
- [/System/Library/PrivateFrameworks/PowerUI.framework/PowerUI](DYLIBS/PowerUI.md)
- [/System/Library/PrivateFrameworks/PowerlogAccounting.framework/PowerlogAccounting](DYLIBS/PowerlogAccounting.md)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore](DYLIBS/PowerlogCore.md)
- [/System/Library/PrivateFrameworks/PowerlogFullOperators.framework/PowerlogFullOperators](DYLIBS/PowerlogFullOperators.md)
- [/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators](DYLIBS/PowerlogHelperdOperators.md)
- [/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators](DYLIBS/PowerlogLiteOperators.md)
- [/System/Library/PrivateFrameworks/Preferences.framework/Preferences](DYLIBS/Preferences.md)
- [/System/Library/PrivateFrameworks/PreferencesExtended.framework/PreferencesExtended](DYLIBS/PreferencesExtended.md)
- [/System/Library/PrivateFrameworks/PreviewShellKit.framework/PreviewShellKit](DYLIBS/PreviewShellKit.md)
- [/System/Library/PrivateFrameworks/PreviewsFoundationOS.framework/PreviewsFoundationOS](DYLIBS/PreviewsFoundationOS.md)
- [/System/Library/PrivateFrameworks/PreviewsInjection.framework/PreviewsInjection](DYLIBS/PreviewsInjection.md)
- [/System/Library/PrivateFrameworks/PreviewsMessagingOS.framework/PreviewsMessagingOS](DYLIBS/PreviewsMessagingOS.md)
- [/System/Library/PrivateFrameworks/PreviewsOSSupportUI.framework/PreviewsOSSupportUI](DYLIBS/PreviewsOSSupportUI.md)
- [/System/Library/PrivateFrameworks/PreviewsServicesUI.framework/PreviewsServicesUI](DYLIBS/PreviewsServicesUI.md)
- [/System/Library/PrivateFrameworks/PrivacyAccounting.framework/PrivacyAccounting](DYLIBS/PrivacyAccounting.md)
- [/System/Library/PrivateFrameworks/PrivacyDisclosureCore.framework/PrivacyDisclosureCore](DYLIBS/PrivacyDisclosureCore.md)
- [/System/Library/PrivateFrameworks/PrivateCloudCompute.framework/PrivateCloudCompute](DYLIBS/PrivateCloudCompute.md)
- [/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PrivateFederatedLearning](DYLIBS/PrivateFederatedLearning.md)
- [/System/Library/PrivateFrameworks/PrivateMLClient.framework/PrivateMLClient](DYLIBS/PrivateMLClient.md)
- [/System/Library/PrivateFrameworks/ProVideo.framework/ProVideo](DYLIBS/ProVideo.md)
- [/System/Library/PrivateFrameworks/ProactiveDaemonSupport.framework/ProactiveDaemonSupport](DYLIBS/ProactiveDaemonSupport.md)
- [/System/Library/PrivateFrameworks/ProactiveEventTracker.framework/ProactiveEventTracker](DYLIBS/ProactiveEventTracker.md)
- [/System/Library/PrivateFrameworks/ProactiveHarvesting.framework/ProactiveHarvesting](DYLIBS/ProactiveHarvesting.md)
- [/System/Library/PrivateFrameworks/ProactiveInputPredictionsInternals.framework/ProactiveInputPredictionsInternals](DYLIBS/ProactiveInputPredictionsInternals.md)
- [/System/Library/PrivateFrameworks/ProactiveML.framework/ProactiveML](DYLIBS/ProactiveML.md)
- [/System/Library/PrivateFrameworks/ProactiveSuggestionClientModel.framework/ProactiveSuggestionClientModel](DYLIBS/ProactiveSuggestionClientModel.md)
- [/System/Library/PrivateFrameworks/ProactiveSummarization.framework/ProactiveSummarization](DYLIBS/ProactiveSummarization.md)
- [/System/Library/PrivateFrameworks/ProactiveSupport.framework/ProactiveSupport](DYLIBS/ProactiveSupport.md)
- [/System/Library/PrivateFrameworks/ProductKit.framework/ProductKit](DYLIBS/ProductKit.md)
- [/System/Library/PrivateFrameworks/PromotedContent.framework/PromotedContent](DYLIBS/PromotedContent.md)
- [/System/Library/PrivateFrameworks/PromotedContentJetClient.framework/PromotedContentJetClient](DYLIBS/PromotedContentJetClient.md)
- [/System/Library/PrivateFrameworks/PromotedContentProxy.framework/PromotedContentProxy](DYLIBS/PromotedContentProxy.md)
- [/System/Library/PrivateFrameworks/PromotedContentSupport.framework/PromotedContentSupport](DYLIBS/PromotedContentSupport.md)
- [/System/Library/PrivateFrameworks/PromotedContentUI.framework/PromotedContentUI](DYLIBS/PromotedContentUI.md)
- [/System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/ProtectedCloudStorage](DYLIBS/ProtectedCloudStorage.md)
- [/System/Library/PrivateFrameworks/ProtoDataExtractor.framework/ProtoDataExtractor](DYLIBS/ProtoDataExtractor.md)
- [/System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer](DYLIBS/ProtocolBuffer.md)
- [/System/Library/PrivateFrameworks/PrototypeTools.framework/PrototypeTools](DYLIBS/PrototypeTools.md)
- [/System/Library/PrivateFrameworks/ProxCardKit.framework/ProxCardKit](DYLIBS/ProxCardKit.md)
- [/System/Library/PrivateFrameworks/Proximity.framework/Proximity](DYLIBS/Proximity.md)
- [/System/Library/PrivateFrameworks/ProximityAppleIDSetup.framework/ProximityAppleIDSetup](DYLIBS/ProximityAppleIDSetup.md)
- [/System/Library/PrivateFrameworks/ProximityAppleIDSetupUI.framework/ProximityAppleIDSetupUI](DYLIBS/ProximityAppleIDSetupUI.md)
- [/System/Library/PrivateFrameworks/ProximityControl.framework/ProximityControl](DYLIBS/ProximityControl.md)
- [/System/Library/PrivateFrameworks/ProximityReaderDaemon.framework/ProximityReaderDaemon](DYLIBS/ProximityReaderDaemon.md)
- [/System/Library/PrivateFrameworks/QOSToolkit.framework/QOSToolkit](DYLIBS/QOSToolkit.md)
- [/System/Library/PrivateFrameworks/QueryParser.framework/QueryParser](DYLIBS/QueryParser.md)
- [/System/Library/PrivateFrameworks/QuickLookThumbnailingDaemon.framework/QuickLookThumbnailingDaemon](DYLIBS/QuickLookThumbnailingDaemon.md)
- [/System/Library/PrivateFrameworks/RTCReporting.framework/RTCReporting](DYLIBS/RTCReporting.md)
- [/System/Library/PrivateFrameworks/RTTUtilities.framework/RTTUtilities](DYLIBS/RTTUtilities.md)
- [/System/Library/PrivateFrameworks/RapidResourceDelivery.framework/RapidResourceDelivery](DYLIBS/RapidResourceDelivery.md)
- [/System/Library/PrivateFrameworks/Rapport.framework/Rapport](DYLIBS/Rapport.md)
- [/System/Library/PrivateFrameworks/Recap.framework/Recap](DYLIBS/Recap.md)
- [/System/Library/PrivateFrameworks/Recon3D.framework/Recon3D](DYLIBS/Recon3D.md)
- [/System/Library/PrivateFrameworks/Recount.framework/Recount](DYLIBS/Recount.md)
- [/System/Library/PrivateFrameworks/RegulatoryDomain.framework/RegulatoryDomain](DYLIBS/RegulatoryDomain.md)
- [/System/Library/PrivateFrameworks/RelevanceEngine.framework/RelevanceEngine](DYLIBS/RelevanceEngine.md)
- [/System/Library/PrivateFrameworks/ReminderKit.framework/ReminderKit](DYLIBS/ReminderKit.md)
- [/System/Library/PrivateFrameworks/ReminderKitInternal.framework/ReminderKitInternal](DYLIBS/ReminderKitInternal.md)
- [/System/Library/PrivateFrameworks/RemindersAppIntents.framework/RemindersAppIntents](DYLIBS/RemindersAppIntents.md)
- [/System/Library/PrivateFrameworks/RemindersIntentsFramework.framework/RemindersIntentsFramework](DYLIBS/RemindersIntentsFramework.md)
- [/System/Library/PrivateFrameworks/RemindersUICore.framework/RemindersUICore](DYLIBS/RemindersUICore.md)
- [/System/Library/PrivateFrameworks/RemoteConfiguration.framework/RemoteConfiguration](DYLIBS/RemoteConfiguration.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/RemoteManagement](DYLIBS/RemoteManagement.md)
- [/System/Library/PrivateFrameworks/RemotePairingDevice.framework/RemotePairingDevice](DYLIBS/RemotePairingDevice.md)
- [/System/Library/PrivateFrameworks/RemoteUI.framework/RemoteUI](DYLIBS/RemoteUI.md)
- [/System/Library/PrivateFrameworks/RemoteXPC.framework/RemoteXPC](DYLIBS/RemoteXPC.md)
- [/System/Library/PrivateFrameworks/RenderBox.framework/RenderBox](DYLIBS/RenderBox.md)
- [/System/Library/PrivateFrameworks/ReplicatorCore.framework/ReplicatorCore](DYLIBS/ReplicatorCore.md)
- [/System/Library/PrivateFrameworks/ReplicatorEngine.framework/ReplicatorEngine](DYLIBS/ReplicatorEngine.md)
- [/System/Library/PrivateFrameworks/RequestDispatcherBridges.framework/RequestDispatcherBridges](DYLIBS/RequestDispatcherBridges.md)
- [/System/Library/PrivateFrameworks/RespiratoryHealth.framework/RespiratoryHealth](DYLIBS/RespiratoryHealth.md)
- [/System/Library/PrivateFrameworks/ResponseUI.framework/ResponseUI](DYLIBS/ResponseUI.md)
- [/System/Library/PrivateFrameworks/RunningBoard.framework/RunningBoard](DYLIBS/RunningBoard.md)
- [/System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices](DYLIBS/RunningBoardServices.md)
- [/System/Library/PrivateFrameworks/RuntimeInternal.framework/RuntimeInternal](DYLIBS/RuntimeInternal.md)
- [/System/Library/PrivateFrameworks/SAObjects.framework/SAObjects](DYLIBS/SAObjects.md)
- [/System/Library/PrivateFrameworks/SFSymbols.framework/SFSymbols](DYLIBS/SFSymbols.md)
- [/System/Library/PrivateFrameworks/SPOwner.framework/SPOwner](DYLIBS/SPOwner.md)
- [/System/Library/PrivateFrameworks/SafariCore.framework/SafariCore](DYLIBS/SafariCore.md)
- [/System/Library/PrivateFrameworks/SafariShared.framework/SafariShared](DYLIBS/SafariShared.md)
- [/System/Library/PrivateFrameworks/SafariSharedUI.framework/SafariSharedUI](DYLIBS/SafariSharedUI.md)
- [/System/Library/PrivateFrameworks/SafetyMonitorUI.framework/SafetyMonitorUI](DYLIBS/SafetyMonitorUI.md)
- [/System/Library/PrivateFrameworks/SampleAnalysis.framework/SampleAnalysis](DYLIBS/SampleAnalysis.md)
- [/System/Library/PrivateFrameworks/ScreenReaderOutput.framework/ScreenReaderOutput](DYLIBS/ScreenReaderOutput.md)
- [/System/Library/PrivateFrameworks/ScreenSharingKit.framework/ScreenSharingKit](DYLIBS/ScreenSharingKit.md)
- [/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore](DYLIBS/ScreenTimeCore.md)
- [/System/Library/PrivateFrameworks/ScreenTimeSettingsUI.framework/ScreenTimeSettingsUI](DYLIBS/ScreenTimeSettingsUI.md)
- [/System/Library/PrivateFrameworks/ScreenTimeUI.framework/ScreenTimeUI](DYLIBS/ScreenTimeUI.md)
- [/System/Library/PrivateFrameworks/ScreenTimeUICore.framework/ScreenTimeUICore](DYLIBS/ScreenTimeUICore.md)
- [/System/Library/PrivateFrameworks/SearchAds.framework/SearchAds](DYLIBS/SearchAds.md)
- [/System/Library/PrivateFrameworks/SearchAssets.framework/SearchAssets](DYLIBS/SearchAssets.md)
- [/System/Library/PrivateFrameworks/SearchFoundation.framework/SearchFoundation](DYLIBS/SearchFoundation.md)
- [/System/Library/PrivateFrameworks/SearchOnDeviceAnalytics.framework/SearchOnDeviceAnalytics](DYLIBS/SearchOnDeviceAnalytics.md)
- [/System/Library/PrivateFrameworks/SearchUI.framework/SearchUI](DYLIBS/SearchUI.md)
- [/System/Library/PrivateFrameworks/SensingAlgsService.framework/SensingAlgsService](DYLIBS/SensingAlgsService.md)
- [/System/Library/PrivateFrameworks/SensingAlgsTouchButtonHost.framework/SensingAlgsTouchButtonHost](DYLIBS/SensingAlgsTouchButtonHost.md)
- [/System/Library/PrivateFrameworks/SensitiveContentAnalysisUI.framework/SensitiveContentAnalysisUI](DYLIBS/SensitiveContentAnalysisUI.md)
- [/System/Library/PrivateFrameworks/Sentry.framework/Sentry](DYLIBS/Sentry.md)
- [/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts](DYLIBS/SeparationAlerts.md)
- [/System/Library/PrivateFrameworks/ServiceManagement.framework/ServiceManagement](DYLIBS/ServiceManagement.md)
- [/System/Library/PrivateFrameworks/SessionCore.framework/SessionCore](DYLIBS/SessionCore.md)
- [/System/Library/PrivateFrameworks/SessionFoundation.framework/SessionFoundation](DYLIBS/SessionFoundation.md)
- [/System/Library/PrivateFrameworks/SessionPushNotifications.framework/SessionPushNotifications](DYLIBS/SessionPushNotifications.md)
- [/System/Library/PrivateFrameworks/SessionSyncEngine.framework/SessionSyncEngine](DYLIBS/SessionSyncEngine.md)
- [/System/Library/PrivateFrameworks/Settings/PrivacySettingsUI.framework/PrivacySettingsUI](DYLIBS/PrivacySettingsUI.md)
- [/System/Library/PrivateFrameworks/Settings/SettingsUIKitPrivate.framework/SettingsUIKitPrivate](DYLIBS/SettingsUIKitPrivate.md)
- [/System/Library/PrivateFrameworks/SettingsCellular.framework/SettingsCellular](DYLIBS/SettingsCellular.md)
- [/System/Library/PrivateFrameworks/SettingsCellularUI.framework/SettingsCellularUI](DYLIBS/SettingsCellularUI.md)
- [/System/Library/PrivateFrameworks/SettingsFoundation.framework/SettingsFoundation](DYLIBS/SettingsFoundation.md)
- [/System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant](DYLIBS/SetupAssistant.md)
- [/System/Library/PrivateFrameworks/SeymourClient.framework/SeymourClient](DYLIBS/SeymourClient.md)
- [/System/Library/PrivateFrameworks/SeymourClientServices.framework/SeymourClientServices](DYLIBS/SeymourClientServices.md)
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
- [/System/Library/PrivateFrameworks/Silex.framework/Silex](DYLIBS/Silex.md)
- [/System/Library/PrivateFrameworks/SiriAnalytics.framework/SiriAnalytics](DYLIBS/SiriAnalytics.md)
- [/System/Library/PrivateFrameworks/SiriAppLaunchIntents.framework/SiriAppLaunchIntents](DYLIBS/SiriAppLaunchIntents.md)
- [/System/Library/PrivateFrameworks/SiriAppLaunchUIFramework.framework/SiriAppLaunchUIFramework](DYLIBS/SiriAppLaunchUIFramework.md)
- [/System/Library/PrivateFrameworks/SiriAudioInternal.framework/SiriAudioInternal](DYLIBS/SiriAudioInternal.md)
- [/System/Library/PrivateFrameworks/SiriAudioSupport.framework/SiriAudioSupport](DYLIBS/SiriAudioSupport.md)
- [/System/Library/PrivateFrameworks/SiriAutoComplete.framework/SiriAutoComplete](DYLIBS/SiriAutoComplete.md)
- [/System/Library/PrivateFrameworks/SiriAutoCompleteAPI.framework/SiriAutoCompleteAPI](DYLIBS/SiriAutoCompleteAPI.md)
- [/System/Library/PrivateFrameworks/SiriCalendarIntents.framework/SiriCalendarIntents](DYLIBS/SiriCalendarIntents.md)
- [/System/Library/PrivateFrameworks/SiriCam.framework/SiriCam](DYLIBS/SiriCam.md)
- [/System/Library/PrivateFrameworks/SiriContactsIntents.framework/SiriContactsIntents](DYLIBS/SiriContactsIntents.md)
- [/System/Library/PrivateFrameworks/SiriContactsUI.framework/SiriContactsUI](DYLIBS/SiriContactsUI.md)
- [/System/Library/PrivateFrameworks/SiriCore.framework/SiriCore](DYLIBS/SiriCore.md)
- [/System/Library/PrivateFrameworks/SiriCrossDeviceArbitration.framework/SiriCrossDeviceArbitration](DYLIBS/SiriCrossDeviceArbitration.md)
- [/System/Library/PrivateFrameworks/SiriDialogEngine.framework/SiriDialogEngine](DYLIBS/SiriDialogEngine.md)
- [/System/Library/PrivateFrameworks/SiriExpanseInternal.framework/SiriExpanseInternal](DYLIBS/SiriExpanseInternal.md)
- [/System/Library/PrivateFrameworks/SiriFindMy.framework/SiriFindMy](DYLIBS/SiriFindMy.md)
- [/System/Library/PrivateFrameworks/SiriFlowEnvironment.framework/SiriFlowEnvironment](DYLIBS/SiriFlowEnvironment.md)
- [/System/Library/PrivateFrameworks/SiriGestureBridge.framework/SiriGestureBridge](DYLIBS/SiriGestureBridge.md)
- [/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/SiriIdentityInternal](DYLIBS/SiriIdentityInternal.md)
- [/System/Library/PrivateFrameworks/SiriInference.framework/SiriInference](DYLIBS/SiriInference.md)
- [/System/Library/PrivateFrameworks/SiriInferenceFlow.framework/SiriInferenceFlow](DYLIBS/SiriInferenceFlow.md)
- [/System/Library/PrivateFrameworks/SiriInferredHelpfulness.framework/SiriInferredHelpfulness](DYLIBS/SiriInferredHelpfulness.md)
- [/System/Library/PrivateFrameworks/SiriInformationSearch.framework/SiriInformationSearch](DYLIBS/SiriInformationSearch.md)
- [/System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation](DYLIBS/SiriInstrumentation.md)
- [/System/Library/PrivateFrameworks/SiriKitFlow.framework/SiriKitFlow](DYLIBS/SiriKitFlow.md)
- [/System/Library/PrivateFrameworks/SiriKitRuntime.framework/SiriKitRuntime](DYLIBS/SiriKitRuntime.md)
- [/System/Library/PrivateFrameworks/SiriMailInternal.framework/SiriMailInternal](DYLIBS/SiriMailInternal.md)
- [/System/Library/PrivateFrameworks/SiriMailUI.framework/SiriMailUI](DYLIBS/SiriMailUI.md)
- [/System/Library/PrivateFrameworks/SiriMessageBus.framework/SiriMessageBus](DYLIBS/SiriMessageBus.md)
- [/System/Library/PrivateFrameworks/SiriMessageTypes.framework/SiriMessageTypes](DYLIBS/SiriMessageTypes.md)
- [/System/Library/PrivateFrameworks/SiriMessagesCommon.framework/SiriMessagesCommon](DYLIBS/SiriMessagesCommon.md)
- [/System/Library/PrivateFrameworks/SiriMessagesFlow.framework/SiriMessagesFlow](DYLIBS/SiriMessagesFlow.md)
- [/System/Library/PrivateFrameworks/SiriMessagesUI.framework/SiriMessagesUI](DYLIBS/SiriMessagesUI.md)
- [/System/Library/PrivateFrameworks/SiriNLUTypes.framework/SiriNLUTypes](DYLIBS/SiriNLUTypes.md)
- [/System/Library/PrivateFrameworks/SiriNaturalLanguageGeneration.framework/SiriNaturalLanguageGeneration](DYLIBS/SiriNaturalLanguageGeneration.md)
- [/System/Library/PrivateFrameworks/SiriNaturalLanguageParsing.framework/SiriNaturalLanguageParsing](DYLIBS/SiriNaturalLanguageParsing.md)
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
- [/System/Library/PrivateFrameworks/SiriTTS.framework/SiriTTS](DYLIBS/SiriTTS.md)
- [/System/Library/PrivateFrameworks/SiriTTSService.framework/SiriTTSService](DYLIBS/SiriTTSService.md)
- [/System/Library/PrivateFrameworks/SiriTimeTimerInternal.framework/SiriTimeTimerInternal](DYLIBS/SiriTimeTimerInternal.md)
- [/System/Library/PrivateFrameworks/SiriTranslationIntents.framework/SiriTranslationIntents](DYLIBS/SiriTranslationIntents.md)
- [/System/Library/PrivateFrameworks/SiriUI.framework/SiriUI](DYLIBS/SiriUI.md)
- [/System/Library/PrivateFrameworks/SiriUIActivation.framework/SiriUIActivation](DYLIBS/SiriUIActivation.md)
- [/System/Library/PrivateFrameworks/SiriUICore.framework/SiriUICore](DYLIBS/SiriUICore.md)
- [/System/Library/PrivateFrameworks/SiriUIFoundation.framework/SiriUIFoundation](DYLIBS/SiriUIFoundation.md)
- [/System/Library/PrivateFrameworks/SiriVOX.framework/SiriVOX](DYLIBS/SiriVOX.md)
- [/System/Library/PrivateFrameworks/SiriVideoIntents.framework/SiriVideoIntents](DYLIBS/SiriVideoIntents.md)
- [/System/Library/PrivateFrameworks/SiriVirtualDeviceResolution.framework/SiriVirtualDeviceResolution](DYLIBS/SiriVirtualDeviceResolution.md)
- [/System/Library/PrivateFrameworks/Sleep.framework/Sleep](DYLIBS/Sleep.md)
- [/System/Library/PrivateFrameworks/SleepDaemon.framework/SleepDaemon](DYLIBS/SleepDaemon.md)
- [/System/Library/PrivateFrameworks/SleepHealthUI.framework/SleepHealthUI](DYLIBS/SleepHealthUI.md)
- [/System/Library/PrivateFrameworks/SleepWidgetUI.framework/SleepWidgetUI](DYLIBS/SleepWidgetUI.md)
- [/System/Library/PrivateFrameworks/SmartReplies.framework/SmartReplies](DYLIBS/SmartReplies.md)
- [/System/Library/PrivateFrameworks/SnippetKit.framework/SnippetKit](DYLIBS/SnippetKit.md)
- [/System/Library/PrivateFrameworks/SnippetUI.framework/SnippetUI](DYLIBS/SnippetUI.md)
- [/System/Library/PrivateFrameworks/SocialLayer.framework/SocialLayer](DYLIBS/SocialLayer.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateController.framework/SoftwareUpdateController](DYLIBS/SoftwareUpdateController.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/SoftwareUpdateCore](DYLIBS/SoftwareUpdateCore.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport](DYLIBS/SoftwareUpdateCoreSupport.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices](DYLIBS/SoftwareUpdateServices.md)
- [/System/Library/PrivateFrameworks/SonicFoundation.framework/SonicFoundation](DYLIBS/SonicFoundation.md)
- [/System/Library/PrivateFrameworks/SonicKit.framework/SonicKit](DYLIBS/SonicKit.md)
- [/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition](DYLIBS/SpeakerRecognition.md)
- [/System/Library/PrivateFrameworks/SplashBoard.framework/SplashBoard](DYLIBS/SplashBoard.md)
- [/System/Library/PrivateFrameworks/Spotlight.framework/Spotlight](DYLIBS/Spotlight.md)
- [/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon](DYLIBS/SpotlightDaemon.md)
- [/System/Library/PrivateFrameworks/SpotlightEmbedding.framework/SpotlightEmbedding](DYLIBS/SpotlightEmbedding.md)
- [/System/Library/PrivateFrameworks/SpotlightFoundation.framework/SpotlightFoundation](DYLIBS/SpotlightFoundation.md)
- [/System/Library/PrivateFrameworks/SpotlightKnowledge.framework/SpotlightKnowledge](DYLIBS/SpotlightKnowledge.md)
- [/System/Library/PrivateFrameworks/SpotlightLinguistics.framework/SpotlightLinguistics](DYLIBS/SpotlightLinguistics.md)
- [/System/Library/PrivateFrameworks/SpotlightRecommendation.framework/SpotlightRecommendation](DYLIBS/SpotlightRecommendation.md)
- [/System/Library/PrivateFrameworks/SpotlightResources.framework/SpotlightResources](DYLIBS/SpotlightResources.md)
- [/System/Library/PrivateFrameworks/SpotlightServices.framework/SpotlightServices](DYLIBS/SpotlightServices.md)
- [/System/Library/PrivateFrameworks/SpotlightUI.framework/SpotlightUI](DYLIBS/SpotlightUI.md)
- [/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard](DYLIBS/SpringBoard.md)
- [/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation](DYLIBS/SpringBoardFoundation.md)
- [/System/Library/PrivateFrameworks/SpringBoardHome.framework/SpringBoardHome](DYLIBS/SpringBoardHome.md)
- [/System/Library/PrivateFrameworks/SpringBoardIntents.framework/SpringBoardIntents](DYLIBS/SpringBoardIntents.md)
- [/System/Library/PrivateFrameworks/SpringBoardUI.framework/SpringBoardUI](DYLIBS/SpringBoardUI.md)
- [/System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices](DYLIBS/SpringBoardUIServices.md)
- [/System/Library/PrivateFrameworks/Stickers.framework/Stickers](DYLIBS/Stickers.md)
- [/System/Library/PrivateFrameworks/StocksAnalytics.framework/StocksAnalytics](DYLIBS/StocksAnalytics.md)
- [/System/Library/PrivateFrameworks/StocksCore.framework/StocksCore](DYLIBS/StocksCore.md)
- [/System/Library/PrivateFrameworks/StocksPersonalization.framework/StocksPersonalization](DYLIBS/StocksPersonalization.md)
- [/System/Library/PrivateFrameworks/StocksUI.framework/StocksUI](DYLIBS/StocksUI.md)
- [/System/Library/PrivateFrameworks/StorageUI.framework/StorageUI](DYLIBS/StorageUI.md)
- [/System/Library/PrivateFrameworks/StoreServices.framework/StoreServices](DYLIBS/StoreServices.md)
- [/System/Library/PrivateFrameworks/SuggestionsSpotlightMetrics.framework/SuggestionsSpotlightMetrics](DYLIBS/SuggestionsSpotlightMetrics.md)
- [/System/Library/PrivateFrameworks/SummarizationKit.framework/SummarizationKit](DYLIBS/SummarizationKit.md)
- [/System/Library/PrivateFrameworks/SwiftSQLite.framework/SwiftSQLite](DYLIBS/SwiftSQLite.md)
- [/System/Library/PrivateFrameworks/Symbolication.framework/Symbolication](DYLIBS/Symbolication.md)
- [/System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter](DYLIBS/SymptomDiagnosticReporter.md)
- [/System/Library/PrivateFrameworks/SymptomReporter.framework/SymptomReporter](DYLIBS/SymptomReporter.md)
- [/System/Library/PrivateFrameworks/SymptomShared.framework/SymptomShared](DYLIBS/SymptomShared.md)
- [/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/ManagedEvent.framework/ManagedEvent](DYLIBS/ManagedEvent.md)
- [/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomAnalytics.framework/SymptomAnalytics](DYLIBS/SymptomAnalytics.md)
- [/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomEvaluator.framework/SymptomEvaluator](DYLIBS/SymptomEvaluator.md)
- [/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomPresentationFeed.framework/SymptomPresentationFeed](DYLIBS/SymptomPresentationFeed.md)
- [/System/Library/PrivateFrameworks/Synapse.framework/Synapse](DYLIBS/Synapse.md)
- [/System/Library/PrivateFrameworks/SyncedDefaults.framework/SyncedDefaults](DYLIBS/SyncedDefaults.md)
- [/System/Library/PrivateFrameworks/SyncedDefaultsDaemon.framework/SyncedDefaultsDaemon](DYLIBS/SyncedDefaultsDaemon.md)
- [/System/Library/PrivateFrameworks/SyncedModels.framework/SyncedModels](DYLIBS/SyncedModels.md)
- [/System/Library/PrivateFrameworks/SystemServiceMonitor.framework/SystemServiceMonitor](DYLIBS/SystemServiceMonitor.md)
- [/System/Library/PrivateFrameworks/SystemStatus.framework/SystemStatus](DYLIBS/SystemStatus.md)
- [/System/Library/PrivateFrameworks/SystemStatusServer.framework/SystemStatusServer](DYLIBS/SystemStatusServer.md)
- [/System/Library/PrivateFrameworks/SystemStatusUI.framework/SystemStatusUI](DYLIBS/SystemStatusUI.md)
- [/System/Library/PrivateFrameworks/SystemUIAnimationKit.framework/SystemUIAnimationKit](DYLIBS/SystemUIAnimationKit.md)
- [/System/Library/PrivateFrameworks/TCC.framework/TCC](DYLIBS/TCC.md)
- [/System/Library/PrivateFrameworks/TSReading.framework/TSReading](DYLIBS/TSReading.md)
- [/System/Library/PrivateFrameworks/TVAppServices.framework/TVAppServices](DYLIBS/TVAppServices.md)
- [/System/Library/PrivateFrameworks/TVLatency.framework/TVLatency](DYLIBS/TVLatency.md)
- [/System/Library/PrivateFrameworks/TVPlayback.framework/TVPlayback](DYLIBS/TVPlayback.md)
- [/System/Library/PrivateFrameworks/TVRemoteCore.framework/TVRemoteCore](DYLIBS/TVRemoteCore.md)
- [/System/Library/PrivateFrameworks/TVRemoteUI.framework/TVRemoteUI](DYLIBS/TVRemoteUI.md)
- [/System/Library/PrivateFrameworks/Tabi.framework/Tabi](DYLIBS/Tabi.md)
- [/System/Library/PrivateFrameworks/TeaBreeze.framework/TeaBreeze](DYLIBS/TeaBreeze.md)
- [/System/Library/PrivateFrameworks/TeaCharts.framework/TeaCharts](DYLIBS/TeaCharts.md)
- [/System/Library/PrivateFrameworks/TeaDB.framework/TeaDB](DYLIBS/TeaDB.md)
- [/System/Library/PrivateFrameworks/TeaFoundation.framework/TeaFoundation](DYLIBS/TeaFoundation.md)
- [/System/Library/PrivateFrameworks/TeaSettings.framework/TeaSettings](DYLIBS/TeaSettings.md)
- [/System/Library/PrivateFrameworks/TeaSnappy.framework/TeaSnappy](DYLIBS/TeaSnappy.md)
- [/System/Library/PrivateFrameworks/TeaTemplate.framework/TeaTemplate](DYLIBS/TeaTemplate.md)
- [/System/Library/PrivateFrameworks/TeaUI.framework/TeaUI](DYLIBS/TeaUI.md)
- [/System/Library/PrivateFrameworks/TelephonyBlastDoorSupport.framework/TelephonyBlastDoorSupport](DYLIBS/TelephonyBlastDoorSupport.md)
- [/System/Library/PrivateFrameworks/TelephonyKit.framework/TelephonyKit](DYLIBS/TelephonyKit.md)
- [/System/Library/PrivateFrameworks/TelephonyUI.framework/TelephonyUI](DYLIBS/TelephonyUI.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities](DYLIBS/TelephonyUtilities.md)
- [/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer](DYLIBS/TextComposer.md)
- [/System/Library/PrivateFrameworks/TextInput.framework/TextInput](DYLIBS/TextInput.md)
- [/System/Library/PrivateFrameworks/TextInputCore.framework/TextInputCore](DYLIBS/TextInputCore.md)
- [/System/Library/PrivateFrameworks/TextInputUI.framework/TextInputUI](DYLIBS/TextInputUI.md)
- [/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingUI.framework/TextToSpeechVoiceBankingUI](DYLIBS/TextToSpeechVoiceBankingUI.md)
- [/System/Library/PrivateFrameworks/TextUnderstandingShared.framework/TextUnderstandingShared](DYLIBS/TextUnderstandingShared.md)
- [/System/Library/PrivateFrameworks/ThirdPartyApplicationSettings.framework/ThirdPartyApplicationSettings](DYLIBS/ThirdPartyApplicationSettings.md)
- [/System/Library/PrivateFrameworks/TipKitCore.framework/TipKitCore](DYLIBS/TipKitCore.md)
- [/System/Library/PrivateFrameworks/TipsCore.framework/TipsCore](DYLIBS/TipsCore.md)
- [/System/Library/PrivateFrameworks/TipsDaemon.framework/TipsDaemon](DYLIBS/TipsDaemon.md)
- [/System/Library/PrivateFrameworks/TipsTryIt.framework/TipsTryIt](DYLIBS/TipsTryIt.md)
- [/System/Library/PrivateFrameworks/TipsUI.framework/TipsUI](DYLIBS/TipsUI.md)
- [/System/Library/PrivateFrameworks/TokenGeneration.framework/TokenGeneration](DYLIBS/TokenGeneration.md)
- [/System/Library/PrivateFrameworks/TokenGenerationCore.framework/TokenGenerationCore](DYLIBS/TokenGenerationCore.md)
- [/System/Library/PrivateFrameworks/TokenGenerationInference.framework/TokenGenerationInference](DYLIBS/TokenGenerationInference.md)
- [/System/Library/PrivateFrameworks/ToolKit.framework/ToolKit](DYLIBS/ToolKit.md)
- [/System/Library/PrivateFrameworks/TrackingAvoidance.framework/TrackingAvoidance](DYLIBS/TrackingAvoidance.md)
- [/System/Library/PrivateFrameworks/TraitsArbiter.framework/TraitsArbiter](DYLIBS/TraitsArbiter.md)
- [/System/Library/PrivateFrameworks/TranslationDaemon.framework/TranslationDaemon](DYLIBS/TranslationDaemon.md)
- [/System/Library/PrivateFrameworks/TranslationUI.framework/TranslationUI](DYLIBS/TranslationUI.md)
- [/System/Library/PrivateFrameworks/TransparencyUI.framework/TransparencyUI](DYLIBS/TransparencyUI.md)
- [/System/Library/PrivateFrameworks/Trial.framework/Trial](DYLIBS/Trial.md)
- [/System/Library/PrivateFrameworks/TrialProto.framework/TrialProto](DYLIBS/TrialProto.md)
- [/System/Library/PrivateFrameworks/TrialServer.framework/TrialServer](DYLIBS/TrialServer.md)
- [/System/Library/PrivateFrameworks/TrustKit.framework/TrustKit](DYLIBS/TrustKit.md)
- [/System/Library/PrivateFrameworks/TypistFramework.framework/TypistFramework](DYLIBS/TypistFramework.md)
- [/System/Library/PrivateFrameworks/UIAccessibility.framework/UIAccessibility](DYLIBS/UIAccessibility.md)
- [/System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation](DYLIBS/UIFoundation.md)
- [/System/Library/PrivateFrameworks/UIIntelligenceIntents.framework/UIIntelligenceIntents](DYLIBS/UIIntelligenceIntents.md)
- [/System/Library/PrivateFrameworks/UIIntelligenceSupport.framework/UIIntelligenceSupport](DYLIBS/UIIntelligenceSupport.md)
- [/System/Library/PrivateFrameworks/UIIntelligenceSupportAgent.framework/UIIntelligenceSupportAgent](DYLIBS/UIIntelligenceSupportAgent.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore](DYLIBS/UIKitCore.md)
- [/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices](DYLIBS/UIKitServices.md)
- [/System/Library/PrivateFrameworks/UINavigationKit.framework/UINavigationKit](DYLIBS/UINavigationKit.md)
- [/System/Library/PrivateFrameworks/UIUnderstanding.framework/UIUnderstanding](DYLIBS/UIUnderstanding.md)
- [/System/Library/PrivateFrameworks/URLFormatting.framework/URLFormatting](DYLIBS/URLFormatting.md)
- [/System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework](DYLIBS/UnifiedAssetFramework.md)
- [/System/Library/PrivateFrameworks/UnifiedMessagingKit.framework/UnifiedMessagingKit](DYLIBS/UnifiedMessagingKit.md)
- [/System/Library/PrivateFrameworks/UniversalDrag.framework/UniversalDrag](DYLIBS/UniversalDrag.md)
- [/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTracking](DYLIBS/UsageTracking.md)
- [/System/Library/PrivateFrameworks/UserActivity.framework/UserActivity](DYLIBS/UserActivity.md)
- [/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_apfs.dylib](DYLIBS/livefiles_apfs.dylib.md)
- [/System/Library/PrivateFrameworks/UserManagement.framework/UserManagement](DYLIBS/UserManagement.md)
- [/System/Library/PrivateFrameworks/UserNotificationsCore.framework/UserNotificationsCore](DYLIBS/UserNotificationsCore.md)
- [/System/Library/PrivateFrameworks/UserNotificationsKit.framework/UserNotificationsKit](DYLIBS/UserNotificationsKit.md)
- [/System/Library/PrivateFrameworks/UserNotificationsServer.framework/UserNotificationsServer](DYLIBS/UserNotificationsServer.md)
- [/System/Library/PrivateFrameworks/UserNotificationsUIKit.framework/UserNotificationsUIKit](DYLIBS/UserNotificationsUIKit.md)
- [/System/Library/PrivateFrameworks/VFX.framework/VFX](DYLIBS/VFX.md)
- [/System/Library/PrivateFrameworks/VectorKit.framework/VectorKit](DYLIBS/VectorKit.md)
- [/System/Library/PrivateFrameworks/VectorSearch.framework/VectorSearch](DYLIBS/VectorSearch.md)
- [/System/Library/PrivateFrameworks/VideoProcessing.framework/VideoProcessing](DYLIBS/VideoProcessing.md)
- [/System/Library/PrivateFrameworks/VideosUI.framework/VideosUI](DYLIBS/VideosUI.md)
- [/System/Library/PrivateFrameworks/VirtualGarage.framework/VirtualGarage](DYLIBS/VirtualGarage.md)
- [/System/Library/PrivateFrameworks/VisionCompanion.framework/VisionCompanion](DYLIBS/VisionCompanion.md)
- [/System/Library/PrivateFrameworks/VisionCore.framework/VisionCore](DYLIBS/VisionCore.md)
- [/System/Library/PrivateFrameworks/VisualGeneration.framework/VisualGeneration](DYLIBS/VisualGeneration.md)
- [/System/Library/PrivateFrameworks/VisualIntelligence.framework/VisualIntelligence](DYLIBS/VisualIntelligence.md)
- [/System/Library/PrivateFrameworks/VisualPairing.framework/VisualPairing](DYLIBS/VisualPairing.md)
- [/System/Library/PrivateFrameworks/VisualUnderstanding.framework/VisualUnderstanding](DYLIBS/VisualUnderstanding.md)
- [/System/Library/PrivateFrameworks/VisualVoicemail.framework/IMAP.framework/IMAP](DYLIBS/IMAP.md)
- [/System/Library/PrivateFrameworks/VisualVoicemail.framework/VisualVoicemail](DYLIBS/VisualVoicemail.md)
- [/System/Library/PrivateFrameworks/VoiceControlUI.framework/VoiceControlUI](DYLIBS/VoiceControlUI.md)
- [/System/Library/PrivateFrameworks/VoiceMemos.framework/VoiceMemos](DYLIBS/VoiceMemos.md)
- [/System/Library/PrivateFrameworks/VoiceShortcutClient.framework/VoiceShortcutClient](DYLIBS/VoiceShortcutClient.md)
- [/System/Library/PrivateFrameworks/VoiceShortcuts.framework/VoiceShortcuts](DYLIBS/VoiceShortcuts.md)
- [/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/VoiceTriggerUI](DYLIBS/VoiceTriggerUI.md)
- [/System/Library/PrivateFrameworks/WPDaemon.framework/WPDaemon](DYLIBS/WPDaemon.md)
- [/System/Library/PrivateFrameworks/WallpaperKit.framework/WallpaperKit](DYLIBS/WallpaperKit.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/WatchFacesWallpaperSupport](DYLIBS/WatchFacesWallpaperSupport.md)
- [/System/Library/PrivateFrameworks/WatchListKit.framework/WatchListKit](DYLIBS/WatchListKit.md)
- [/System/Library/PrivateFrameworks/WeatherAnalytics.framework/WeatherAnalytics](DYLIBS/WeatherAnalytics.md)
- [/System/Library/PrivateFrameworks/WeatherAppSupport.framework/WeatherAppSupport](DYLIBS/WeatherAppSupport.md)
- [/System/Library/PrivateFrameworks/WeatherCore.framework/WeatherCore](DYLIBS/WeatherCore.md)
- [/System/Library/PrivateFrameworks/WeatherDaemon.framework/WeatherDaemon](DYLIBS/WeatherDaemon.md)
- [/System/Library/PrivateFrameworks/WeatherData.framework/WeatherData](DYLIBS/WeatherData.md)
- [/System/Library/PrivateFrameworks/WeatherMaps.framework/WeatherMaps](DYLIBS/WeatherMaps.md)
- [/System/Library/PrivateFrameworks/WeatherUI.framework/WeatherUI](DYLIBS/WeatherUI.md)
- [/System/Library/PrivateFrameworks/WebBookmarks.framework/WebBookmarks](DYLIBS/WebBookmarks.md)
- [/System/Library/PrivateFrameworks/WebBookmarksSwift.framework/WebBookmarksSwift](DYLIBS/WebBookmarksSwift.md)
- [/System/Library/PrivateFrameworks/WebContentAnalysis.framework/WebContentAnalysis](DYLIBS/WebContentAnalysis.md)
- [/System/Library/PrivateFrameworks/WebCore.framework/Frameworks/libANGLE-shared.dylib](DYLIBS/libANGLE-shared.dylib.md)
- [/System/Library/PrivateFrameworks/WebCore.framework/WebCore](DYLIBS/WebCore.md)
- [/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit](DYLIBS/WiFiKit.md)
- [/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer](DYLIBS/WiFiPeerToPeer.md)
- [/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy](DYLIBS/WiFiPolicy.md)
- [/System/Library/PrivateFrameworks/WidgetRenderer.framework/WidgetRenderer](DYLIBS/WidgetRenderer.md)
- [/System/Library/PrivateFrameworks/WirelessProximity.framework/WirelessProximity](DYLIBS/WirelessProximity.md)
- [/System/Library/PrivateFrameworks/WorkflowEditor.framework/WorkflowEditor](DYLIBS/WorkflowEditor.md)
- [/System/Library/PrivateFrameworks/WorkflowKit.framework/WorkflowKit](DYLIBS/WorkflowKit.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/WorkflowUI](DYLIBS/WorkflowUI.md)
- [/System/Library/PrivateFrameworks/WorkflowUICore.framework/WorkflowUICore](DYLIBS/WorkflowUICore.md)
- [/System/Library/PrivateFrameworks/WorkflowUIServices.framework/WorkflowUIServices](DYLIBS/WorkflowUIServices.md)
- [/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/WorkoutAnnouncements](DYLIBS/WorkoutAnnouncements.md)
- [/System/Library/PrivateFrameworks/WorkoutCore.framework/WorkoutCore](DYLIBS/WorkoutCore.md)
- [/System/Library/PrivateFrameworks/WorkoutUI.framework/WorkoutUI](DYLIBS/WorkoutUI.md)
- [/System/Library/PrivateFrameworks/WritingToolsUI.framework/WritingToolsUI](DYLIBS/WritingToolsUI.md)
- [/System/Library/PrivateFrameworks/XGBoostFramework.framework/XGBoostFramework](DYLIBS/XGBoostFramework.md)
- [/System/Library/PrivateFrameworks/XOJIT.framework/XOJIT](DYLIBS/XOJIT.md)
- [/System/Library/PrivateFrameworks/XavierNews.framework/XavierNews](DYLIBS/XavierNews.md)
- [/System/Library/PrivateFrameworks/ZeoliteFramework.framework/ZeoliteFramework](DYLIBS/ZeoliteFramework.md)
- [/System/Library/PrivateFrameworks/ZeoliteLanguage.framework/ZeoliteLanguage](DYLIBS/ZeoliteLanguage.md)
- [/System/Library/PrivateFrameworks/ZhuGeSupport.framework/ZhuGeSupport](DYLIBS/ZhuGeSupport.md)
- [/System/Library/PrivateFrameworks/_IconServices_SwiftUI.framework/_IconServices_SwiftUI](DYLIBS/_IconServices_SwiftUI.md)
- [/System/Library/PrivateFrameworks/_JetEngine_SwiftUI.framework/_JetEngine_SwiftUI](DYLIBS/_JetEngine_SwiftUI.md)
- [/System/Library/PrivateFrameworks/_MusicKitInternal_SwiftUI.framework/_MusicKitInternal_SwiftUI](DYLIBS/_MusicKitInternal_SwiftUI.md)
- [/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore](DYLIBS/iCloudDriveCore.md)
- [/System/Library/PrivateFrameworks/iCloudMailAccountUI.framework/iCloudMailAccountUI](DYLIBS/iCloudMailAccountUI.md)
- [/System/Library/PrivateFrameworks/iCloudQuota.framework/iCloudQuota](DYLIBS/iCloudQuota.md)
- [/System/Library/PrivateFrameworks/iCloudQuotaUI.framework/iCloudQuotaUI](DYLIBS/iCloudQuotaUI.md)
- [/System/Library/PrivateFrameworks/iCloudSettings.framework/iCloudSettings](DYLIBS/iCloudSettings.md)
- [/System/Library/PrivateFrameworks/iOSDiagnostics.framework/iOSDiagnostics](DYLIBS/iOSDiagnostics.md)
- [/System/Library/PrivateFrameworks/iTunesCloud.framework/iTunesCloud](DYLIBS/iTunesCloud.md)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSText.framework/TSText](DYLIBS/TSText.md)
- [/System/Library/PrivateFrameworks/icloudMCCKit.framework/icloudMCCKit](DYLIBS/icloudMCCKit.md)
- [/System/Library/PrivateFrameworks/ktrace.framework/ktrace](DYLIBS/ktrace.md)
- [/System/Library/PrivateFrameworks/libEDR.framework/libEDR](DYLIBS/libEDR.md)
- [/System/Library/PrivateFrameworks/shared_cache_page_prewarming.framework/shared_cache_page_prewarming](DYLIBS/shared_cache_page_prewarming.md)
- [/System/Library/SystemConfiguration/CaptiveNetworkSupport.bundle/CaptiveNetworkSupport](DYLIBS/CaptiveNetworkSupport.md)
- [/System/Library/VideoCodecs/VCPHEVC.videocodec](DYLIBS/VCPHEVC.videocodec.md)
- [/System/Library/VideoDecoders/AVD.videodecoder](DYLIBS/AVD.videodecoder.md)
- [/System/Library/VideoDecoders/JPEGH1.videodecoder](DYLIBS/JPEGH1.videodecoder.md)
- [/System/Library/VideoEncoders/JPEGH1.videoencoder](DYLIBS/JPEGH1.videoencoder.md)
- [/System/Library/VideoProcessors/BarcodeScanner.videoprocessor](DYLIBS/BarcodeScanner.videoprocessor.md)
- [/System/Library/VideoProcessors/CalibrationV1.bundle/CalibrationV1](DYLIBS/CalibrationV1.md)
- [/System/Library/VideoProcessors/DepthProcessorV2.bundle/DepthProcessorV2](DYLIBS/DepthProcessorV2.md)
- [/System/Library/VideoProcessors/DisparityV5.bundle/DisparityV5](DYLIBS/DisparityV5.md)
- [/System/Library/VideoProcessors/FPDisparityV3.bundle/FPDisparityV3](DYLIBS/FPDisparityV3.md)
- [/System/Library/VideoProcessors/IntelligentDistortionCorrectionV1.bundle/IntelligentDistortionCorrectionV1](DYLIBS/IntelligentDistortionCorrectionV1.md)
- [/System/Library/VideoProcessors/MattingV2.bundle/MattingV2](DYLIBS/MattingV2.md)
- [/System/Library/VideoProcessors/MetalFilter.bundle/MetalFilter](DYLIBS/MetalFilter.md)
- [/System/Library/VideoProcessors/NRFV2.bundle/NRFV2](DYLIBS/NRFV2.md)
- [/System/Library/VideoProcessors/NRFV4.bundle/NRFV4](DYLIBS/NRFV4.md)
- [/System/Library/VideoProcessors/SDOFRenderingV5.bundle/SDOFRenderingV5](DYLIBS/SDOFRenderingV5.md)
- [/System/Library/VideoProcessors/STF.bundle/STF](DYLIBS/STF.md)
- [/usr/lib/dyld](DYLIBS/dyld.md)
- [/usr/lib/libATCommandStudioDynamic.dylib](DYLIBS/libATCommandStudioDynamic.dylib.md)
- [/usr/lib/libAppletTranslationLibrary.dylib](DYLIBS/libAppletTranslationLibrary.dylib.md)
- [/usr/lib/libAudioIssueDetector.dylib](DYLIBS/libAudioIssueDetector.dylib.md)
- [/usr/lib/libAudioToolboxUtility.dylib](DYLIBS/libAudioToolboxUtility.dylib.md)
- [/usr/lib/libBBUpdaterDynamic.dylib](DYLIBS/libBBUpdaterDynamic.dylib.md)
- [/usr/lib/libBKDM2.dylib](DYLIBS/libBKDM2.dylib.md)
- [/usr/lib/libBasebandCommandDrivers.dylib](DYLIBS/libBasebandCommandDrivers.dylib.md)
- [/usr/lib/libBasebandCommandDriversARI.dylib](DYLIBS/libBasebandCommandDriversARI.dylib.md)
- [/usr/lib/libBasebandCommandDriversMIPC.dylib](DYLIBS/libBasebandCommandDriversMIPC.dylib.md)
- [/usr/lib/libBasebandCommandDriversQMI.dylib](DYLIBS/libBasebandCommandDriversQMI.dylib.md)
- [/usr/lib/libBasebandManager.dylib](DYLIBS/libBasebandManager.dylib.md)
- [/usr/lib/libBasebandManagerDAL.dylib](DYLIBS/libBasebandManagerDAL.dylib.md)
- [/usr/lib/libBasebandManagerICE.dylib](DYLIBS/libBasebandManagerICE.dylib.md)
- [/usr/lib/libCTGreenTeaLogger.dylib](DYLIBS/libCTGreenTeaLogger.dylib.md)
- [/usr/lib/libCoreEntitlements.dylib](DYLIBS/libCoreEntitlements.dylib.md)
- [/usr/lib/libETLDLFDynamic.dylib](DYLIBS/libETLDLFDynamic.dylib.md)
- [/usr/lib/libETLDLOADCoreDumpDynamic.dylib](DYLIBS/libETLDLOADCoreDumpDynamic.dylib.md)
- [/usr/lib/libETLDLOADDynamic.dylib](DYLIBS/libETLDLOADDynamic.dylib.md)
- [/usr/lib/libETLDMCDynamic.dylib](DYLIBS/libETLDMCDynamic.dylib.md)
- [/usr/lib/libETLDynamic.dylib](DYLIBS/libETLDynamic.dylib.md)
- [/usr/lib/libETLSAHDynamic.dylib](DYLIBS/libETLSAHDynamic.dylib.md)
- [/usr/lib/libFDR.dylib](DYLIBS/libFDR.dylib.md)
- [/usr/lib/libIOReport.dylib](DYLIBS/libIOReport.dylib.md)
- [/usr/lib/libMemoryResourceException.dylib](DYLIBS/libMemoryResourceException.dylib.md)
- [/usr/lib/libMobileGestalt.dylib](DYLIBS/libMobileGestalt.dylib.md)
- [/usr/lib/libMobileGestaltExtensions.dylib](DYLIBS/libMobileGestaltExtensions.dylib.md)
- [/usr/lib/libNFC_Comet.dylib](DYLIBS/libNFC_Comet.dylib.md)
- [/usr/lib/libPCITransport.dylib](DYLIBS/libPCITransport.dylib.md)
- [/usr/lib/libPN548_API.dylib](DYLIBS/libPN548_API.dylib.md)
- [/usr/lib/libQMIParserDynamic.dylib](DYLIBS/libQMIParserDynamic.dylib.md)
- [/usr/lib/libSMC.dylib](DYLIBS/libSMC.dylib.md)
- [/usr/lib/libSecureMAHelper.dylib](DYLIBS/libSecureMAHelper.dylib.md)
- [/usr/lib/libTelephonyBasebandDynamic.dylib](DYLIBS/libTelephonyBasebandDynamic.dylib.md)
- [/usr/lib/libTelephonyCapabilities.dylib](DYLIBS/libTelephonyCapabilities.dylib.md)
- [/usr/lib/libTelephonyDebugDynamic.dylib](DYLIBS/libTelephonyDebugDynamic.dylib.md)
- [/usr/lib/libTelephonyUtilDynamic.dylib](DYLIBS/libTelephonyUtilDynamic.dylib.md)
- [/usr/lib/libVinylNonUpdater.dylib](DYLIBS/libVinylNonUpdater.dylib.md)
- [/usr/lib/libapp_launch_measurement.dylib](DYLIBS/libapp_launch_measurement.dylib.md)
- [/usr/lib/libapple_nghttp2.dylib](DYLIBS/libapple_nghttp2.dylib.md)
- [/usr/lib/libarchive.2.dylib](DYLIBS/libarchive.2.dylib.md)
- [/usr/lib/libauthinstall.dylib](DYLIBS/libauthinstall.dylib.md)
- [/usr/lib/libboringssl.dylib](DYLIBS/libboringssl.dylib.md)
- [/usr/lib/libchannel.dylib](DYLIBS/libchannel.dylib.md)
- [/usr/lib/libcmark-gfm.dylib](DYLIBS/libcmark-gfm.dylib.md)
- [/usr/lib/libcompression.dylib](DYLIBS/libcompression.dylib.md)
- [/usr/lib/libcoreroutine.dylib](DYLIBS/libcoreroutine.dylib.md)
- [/usr/lib/libcoretls.dylib](DYLIBS/libcoretls.dylib.md)
- [/usr/lib/libcryptex.dylib](DYLIBS/libcryptex.dylib.md)
- [/usr/lib/libcryptex_core.dylib](DYLIBS/libcryptex_core.dylib.md)
- [/usr/lib/libcryptex_interface.dylib](DYLIBS/libcryptex_interface.dylib.md)
- [/usr/lib/libcryptex_trampoline.dylib](DYLIBS/libcryptex_trampoline.dylib.md)
- [/usr/lib/libcupolicy.dylib](DYLIBS/libcupolicy.dylib.md)
- [/usr/lib/libdns_services.dylib](DYLIBS/libdns_services.dylib.md)
- [/usr/lib/libenergytrace.dylib](DYLIBS/libenergytrace.dylib.md)
- [/usr/lib/libexpat.1.dylib](DYLIBS/libexpat.1.dylib.md)
- [/usr/lib/libfire7.dylib](DYLIBS/libfire7.dylib.md)
- [/usr/lib/liblockdown.dylib](DYLIBS/liblockdown.dylib.md)
- [/usr/lib/liblzma.5.dylib](DYLIBS/liblzma.5.dylib.md)
- [/usr/lib/libmdns.dylib](DYLIBS/libmdns.dylib.md)
- [/usr/lib/libnetquality.dylib](DYLIBS/libnetquality.dylib.md)
- [/usr/lib/libnetworkextension.dylib](DYLIBS/libnetworkextension.dylib.md)
- [/usr/lib/libnfshared.dylib](DYLIBS/libnfshared.dylib.md)
- [/usr/lib/libnwswifttls.dylib](DYLIBS/libnwswifttls.dylib.md)
- [/usr/lib/libobjc.A.dylib](DYLIBS/libobjc.A.dylib.md)
- [/usr/lib/libprequelite.dylib](DYLIBS/libprequelite.dylib.md)
- [/usr/lib/libprotobuf-lite.dylib](DYLIBS/libprotobuf-lite.dylib.md)
- [/usr/lib/libprotobuf.dylib](DYLIBS/libprotobuf.dylib.md)
- [/usr/lib/libswiftPrespecialized.dylib](DYLIBS/libswiftPrespecialized.dylib.md)
- [/usr/lib/libtidy.A.dylib](DYLIBS/libtidy.A.dylib.md)
- [/usr/lib/libusrtcp.dylib](DYLIBS/libusrtcp.dylib.md)
- [/usr/lib/libxo.dylib](DYLIBS/libxo.dylib.md)
- [/usr/lib/libz.1.dylib](DYLIBS/libz.1.dylib.md)
- [/usr/lib/swift/libswiftAccelerate.dylib](DYLIBS/libswiftAccelerate.dylib.md)
- [/usr/lib/swift/libswiftCoreFoundation.dylib](DYLIBS/libswiftCoreFoundation.dylib.md)
- [/usr/lib/swift/libswiftDispatch.dylib](DYLIBS/libswiftDispatch.dylib.md)
- [/usr/lib/swift/libswiftNaturalLanguage.dylib](DYLIBS/libswiftNaturalLanguage.dylib.md)
- [/usr/lib/swift/libswiftSystem.dylib](DYLIBS/libswiftSystem.dylib.md)
- [/usr/lib/swift/libswiftUniformTypeIdentifiers.dylib](DYLIBS/libswiftUniformTypeIdentifiers.dylib.md)
- [/usr/lib/swift/libswiftXPC.dylib](DYLIBS/libswiftXPC.dylib.md)
- [/usr/lib/swift/libswift_errno.dylib](DYLIBS/libswift_errno.dylib.md)
- [/usr/lib/swift/libswiftos.dylib](DYLIBS/libswiftos.dylib.md)
- [/usr/lib/system/libcommonCrypto.dylib](DYLIBS/libcommonCrypto.dylib.md)
- [/usr/lib/system/libdispatch.dylib](DYLIBS/libdispatch.dylib.md)
- [/usr/lib/system/libdyld.dylib](DYLIBS/libdyld.dylib.md)
- [/usr/lib/system/liblaunch.dylib](DYLIBS/liblaunch.dylib.md)
- [/usr/lib/system/libmacho.dylib](DYLIBS/libmacho.dylib.md)
- [/usr/lib/system/libsystem_asl.dylib](DYLIBS/libsystem_asl.dylib.md)
- [/usr/lib/system/libsystem_blocks.dylib](DYLIBS/libsystem_blocks.dylib.md)
- [/usr/lib/system/libsystem_c.dylib](DYLIBS/libsystem_c.dylib.md)
- [/usr/lib/system/libsystem_configuration.dylib](DYLIBS/libsystem_configuration.dylib.md)
- [/usr/lib/system/libsystem_containermanager.dylib](DYLIBS/libsystem_containermanager.dylib.md)
- [/usr/lib/system/libsystem_dnssd.dylib](DYLIBS/libsystem_dnssd.dylib.md)
- [/usr/lib/system/libsystem_eligibility.dylib](DYLIBS/libsystem_eligibility.dylib.md)
- [/usr/lib/system/libsystem_featureflags.dylib](DYLIBS/libsystem_featureflags.dylib.md)
- [/usr/lib/system/libsystem_info.dylib](DYLIBS/libsystem_info.dylib.md)
- [/usr/lib/system/libsystem_kernel.dylib](DYLIBS/libsystem_kernel.dylib.md)
- [/usr/lib/system/libsystem_m.dylib](DYLIBS/libsystem_m.dylib.md)
- [/usr/lib/system/libsystem_malloc.dylib](DYLIBS/libsystem_malloc.dylib.md)
- [/usr/lib/system/libsystem_networkextension.dylib](DYLIBS/libsystem_networkextension.dylib.md)
- [/usr/lib/system/libsystem_platform.dylib](DYLIBS/libsystem_platform.dylib.md)
- [/usr/lib/system/libsystem_pthread.dylib](DYLIBS/libsystem_pthread.dylib.md)
- [/usr/lib/system/libsystem_sandbox.dylib](DYLIBS/libsystem_sandbox.dylib.md)
- [/usr/lib/system/libsystem_sanitizers.dylib](DYLIBS/libsystem_sanitizers.dylib.md)
- [/usr/lib/system/libsystem_symptoms.dylib](DYLIBS/libsystem_symptoms.dylib.md)
- [/usr/lib/system/libsystem_trace.dylib](DYLIBS/libsystem_trace.dylib.md)
- [/usr/lib/updaters/libVinylUpdater.dylib](DYLIBS/libVinylUpdater.dylib.md)

</details>

### Feature Flags

#### 🆕 NEW (1)

<details>
  <summary><i>View New</i></summary>

#### Diagnostics.plist

>  `Domain/Diagnostics.plist`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict/>
</plist>

```

</details>

#### ❌ Removed (1)

- `Domain/ConditionalEngine.plist`

#### ⬆️ Updated (19)

<details>
  <summary><i>View Updated</i></summary>

#### AVKit.plist

>  `Domain/AVKit.plist`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>IntegratedTimeline</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>animatedSkipButtons</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### AppleIDSetup.plist

>  `Domain/AppleIDSetup.plist`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>AgeAttestationSettings</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>ChildSetupSignIn</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### AudioSession.plist

>  `Domain/AudioSession.plist`

```diff

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
+	<key>EnableSecureSessionOnMacOS</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>OffloadActivationOffACQ</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### BluetoothFeatures.plist

>  `Domain/BluetoothFeatures.plist`

```diff

 		<key>Enabled</key>
 		<true/>
 	</dict>
+	<key>Maestro</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>NativeHealth</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### CompanionServices.plist

>  `Domain/CompanionServices.plist`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>AdditionalSiriDialogue</key>
-	<dict>
-		<key>DevelopmentPhase</key>
-		<string>FeatureComplete</string>
-	</dict>
 	<key>AppleMusic</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### Home.plist

>  `Domain/Home.plist`

```diff

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
+	<key>RapportoverBLE</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>ResidentSelection</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### MediaExperience.plist

>  `Domain/MediaExperience.plist`

```diff

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
+	<key>StravinskyOrchestration</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>SystemRemoteDisplay</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### MediaRemote.plist

>  `Domain/MediaRemote.plist`

```diff

 		<key>Enabled</key>
 		<true/>
 	</dict>
-	<key>rapport_remote_control_transport</key>
-	<dict>
-		<key>Enabled</key>
-		<true/>
-	</dict>
 	<key>session_based_lock_screen_platter</key>
 	<dict>
 		<key>Enabled</key>

```

#### MobileAsset.plist

>  `Domain/MobileAsset.plist`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>LiveStorageExclaveNonce</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>com_apple_mobileassetd_conclave</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### OmniSearch.plist

>  `Domain/OmniSearch.plist`

```diff

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
+	<key>preExtractedIDs</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>reflectionToken</key>
 	<dict>
 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
-	<key>urgentPCCPrewarm</key>
+	<key>searchInAppRows</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
+	<key>shortCircuitMusicSearch</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
+	<key>shortCircuitPhotoSearch</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
+	<key>showInternalErrorInfo</key>
 	<dict>
 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>

```

#### Oneness.plist

>  `Domain/Oneness.plist`

```diff

 		<key>DisclosureRequired</key>
 		<string>8f6f8e85-8d9d-8330-8c15-a603765b90f3</string>
 	</dict>
+	<key>RemoteTextInput</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>Shell</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### PrivateCloudCompute.plist

>  `Domain/PrivateCloudCompute.plist`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>enforceEnvironment</key>
-	<dict>
-		<key>DevelopmentPhase</key>
-		<string>FeatureComplete</string>
-	</dict>
-	<key>productionEnvironmentAvailable</key>
+	<key>trustedProxyProtocol</key>
 	<dict>
 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>

```

#### ScreenTime.plist

>  `Domain/ScreenTime.plist`

```diff

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
+	<key>passcode_activity</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 </dict>
 </plist>
 

```

#### SiriUI.plist

>  `Domain/SiriUI.plist`

```diff

 		<key>Enabled</key>
 		<true/>
 	</dict>
+	<key>response_coordination_wordtiming_fallback</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>sae</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### Spotlight.plist

>  `Domain/Spotlight.plist`

```diff

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
-	<key>SearchToolAllBundles</key>
-	<dict>
-		<key>DevelopmentPhase</key>
-		<string>FeatureComplete</string>
-	</dict>
-	<key>SearchToolCleanSlateDenseRetrieval</key>
-	<dict>
-		<key>DevelopmentPhase</key>
-		<string>FeatureComplete</string>
-	</dict>
 	<key>SearchToolLLMQueryUnderstanding</key>
 	<dict>
 		<key>DevelopmentPhase</key>

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
-	<key>SearchToolRanking</key>
-	<dict>
-		<key>DevelopmentPhase</key>
-		<string>FeatureComplete</string>
-	</dict>
 	<key>SearchToolRetrievalSparseScoringV2</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### SpringBoard.plist

>  `Domain/SpringBoard.plist`

```diff

 		<key>DisclosureRequired</key>
 		<string>843d7545-f18c-4301-863c-e4e20100acf7</string>
 	</dict>
+	<key>HomeScreen2DMovement</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>IconStylesOutsideSpringBoard</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### Summarization.plist

>  `Domain/Summarization.plist`

```diff

 <?xml version="1.0" encoding="UTF-8"?>
 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
-<dict/>
+<dict>
+	<key>FactualConsistencyClassifier</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
+</dict>
 </plist>
 

```

#### TelephonyUtilities.plist

>  `Domain/TelephonyUtilities.plist`

```diff

 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
+	<key>CallEndSpamUIEnhancement</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>CallManagerEnabled</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### GlobalDisclosures.plist

>  `GlobalDisclosures.plist`

```diff

 		<key>Disclosed</key>
 		<true/>
 	</dict>
-	<key>1b3196a9-6a20-4559-60fd-bb3743219ab3</key>
-	<dict>
-		<key>Disclosed</key>
-		<true/>
-	</dict>
 	<key>2298f8e4-f510-4776-b2c1-a85ea314b1f8</key>
 	<dict>
 		<key>Disclosed</key>

```


</details>

### Files

#### 🆕 New

##### IPSW (2)

- `Firmware/Mav24-1.54.01.Release.bbfw`
- `Firmware/Mav24-1.54.01.Release.plist`

##### filesystem (713)

<details>
  <summary><i>View Files</i></summary>

- `/Applications/Diagnostics.app/Localizable-Assessment.loctable`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/_params.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/ar.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/da.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/de.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/en-au.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/en-ca.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/en-gb.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/en.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/es-mx.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/es.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/fi.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/fr.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/he.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/hi.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/it.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/ja.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/ko.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/ms.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/nb.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/nl.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/pt.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/ru.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/sv.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/th.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/tr.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/vi.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/yue.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/zh-cn.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/zh-hk.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Templates/dialog/PlayMediaIntent.catfamily/CannotOpenOnApp.cat/zh-tw.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/CAMRootFlowPlugin.bundle/Templates/dialog/UserSession.catfamily/ActiveSessionUserNotRecognized.cat/en-za.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/DialogAssetDelivery.plist`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/CommonErrors.catfamily/GenericError.cat/_params.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/CommonErrors.catfamily/GenericError.cat/ar.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/CommonErrors.catfamily/GenericError.cat/da.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/CommonErrors.catfamily/GenericError.cat/de-ch.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/CommonErrors.catfamily/GenericError.cat/de.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/CommonErrors.catfamily/GenericError.cat/en-au.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/CommonErrors.catfamily/GenericError.cat/en-ca.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/CommonErrors.catfamily/GenericError.cat/en-gb.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/CommonErrors.catfamily/GenericError.cat/en.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/CommonErrors.catfamily/GenericError.cat/es-cl.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/CommonErrors.catfamily/GenericError.cat/es-mx.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/CommonErrors.catfamily/GenericError.cat/es.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/CommonErrors.catfamily/GenericError.cat/fi.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/CommonErrors.catfamily/GenericError.cat/fr.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/CommonErrors.catfamily/GenericError.cat/he.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/CommonErrors.catfamily/GenericError.cat/it.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/CommonErrors.catfamily/GenericError.cat/ja.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/CommonErrors.catfamily/GenericError.cat/ko.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/CommonErrors.catfamily/GenericError.cat/ms.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/CommonErrors.catfamily/GenericError.cat/nb.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/CommonErrors.catfamily/GenericError.cat/nl.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/CommonErrors.catfamily/GenericError.cat/pt.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/CommonErrors.catfamily/GenericError.cat/ru.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/CommonErrors.catfamily/GenericError.cat/sv.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/CommonErrors.catfamily/GenericError.cat/tr.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/CommonErrors.catfamily/GenericError.cat/vi.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/CommonErrors.catfamily/GenericError.cat/yue.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/CommonErrors.catfamily/GenericError.cat/zh-cn.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/CommonErrors.catfamily/GenericError.cat/zh-hk.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/CommonErrors.catfamily/GenericError.cat/zh-tw.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/IFFlow.catfamily/UserLocationUnknown.cat/_params.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/IFFlow.catfamily/UserLocationUnknown.cat/en.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/_params.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/ar.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/da.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/de.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/en-au.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/en-ca.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/en-gb.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/en.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/es-mx.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/es-us.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/es.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/fi.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/fr.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/he.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/it.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/ja.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/ko.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/ms.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/nb.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/nl.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/pt.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/ru.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/sv.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/th.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/tr.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/vi.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/yue.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/zh-cn.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/zh-hk.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/AirplaneMode.cat/zh-tw.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/_params.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/ar.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/da.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/de.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/en-au.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/en-ca.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/en-gb.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/en.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/es-mx.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/es.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/fi.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/fr.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/he.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/it.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/ja.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/ko.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/ms.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/nb.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/nl.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/pt.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/ru.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/sv.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/th.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/tr.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/vi.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/yue.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/zh-cn.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/zh-hk.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/NoConnection.cat/zh-tw.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/_params.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/ar.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/da.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/de-ch.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/de.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/en-au.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/en-ca.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/en-gb.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/en-za.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/en.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/es-cl.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/es-mx.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/es.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/fi.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/fr.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/he.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/it.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/ja.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/ko.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/ms.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/nb.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/nl.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/pt.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/ru.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/sv.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/th.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/tr.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/vi.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/yue.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/zh-cn.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/zh-hk.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/NetworkAvailability.catfamily/Timeout.cat/zh-tw.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/_params.cat.xml`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/ar.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/da.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/de.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/en-au.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/en-ca.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/en.cat.xml`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/es-mx.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/es.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/fr.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/it.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/ja.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/ko.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/ms.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/nb.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/nl-be.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/nl.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/pt.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/ru.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/sv.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/tr.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/vi.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/zh-cn.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/zh-hk.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmation.cat/zh-tw.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/_params.cat.xml`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/ar.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/da.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/de.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/en-au.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/en-ca.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/en-gb.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/en.cat.xml`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/es-mx.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/es.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/fr.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/he.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/it.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/ja.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/ko.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/ms.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/nb.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/nl.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/pt.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/sv.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/tr.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/vi.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/zh-cn.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/zh-hk.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationNoLabel.cat/zh-tw.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/_params.cat.xml`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/ar.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/da.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/de.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/en-au.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/en-ca.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/en-gb.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/en.cat.xml`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/es-mx.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/es.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/fr.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/he.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/it.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/ja.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/ko.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/ms.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/nb.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/nl.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/pt.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/sv.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/tr.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/vi.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/zh-cn.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/zh-hk.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/Templates/dialog/runInformationFlow.catfamily/disableConfirmRequestsConfirmationYesLabel.cat/zh-tw.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/Templates/dialog/SearchCallHistory.catfamily/IntentHandledResponse.cat/en-ie.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/Templates/dialog/SearchCallHistory.catfamily/IntentHandledResponse.cat/en-sg.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/Templates/dialog/SearchCallHistory.catfamily/IntentHandledResponse.cat/en-za.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/Templates/dialog/SearchCallHistory.catfamily/IntentHandledResponseMissedCall.cat/en-ie.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/Templates/dialog/SearchCallHistory.catfamily/IntentHandledResponseMissedCall.cat/en-sg.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/Templates/dialog/SearchCallHistory.catfamily/IntentHandledResponseMissedCall.cat/en-za.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/Templates/dialog/StartCall.catfamily/IntentConfirmationEmergency.cat/en-ie.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/Templates/dialog/StartCall.catfamily/IntentConfirmationEmergency.cat/en-in.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/Templates/dialog/StartCall.catfamily/IntentConfirmationEmergency.cat/en-sg.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/Templates/dialog/StartCall.catfamily/IntentConfirmationEmergency.cat/en-za.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/Templates/dialog/StartCall.catfamily/IntentConfirmationEmergency.cat/es-cl.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/Templates/dialog/UnsupportedFlow.catfamily/StartCallEmergency.cat/en-ie.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/Templates/dialog/UnsupportedFlow.catfamily/StartCallEmergency.cat/en-in.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/Templates/dialog/UnsupportedFlow.catfamily/StartCallEmergency.cat/en-sg.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/Templates/dialog/UnsupportedFlow.catfamily/StartCallEmergency.cat/en-za.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/TimerFlowDelegatePlugin.bundle/Templates/dialog/createTimer.catfamily/errorWithCode.cat/de-ch.cat.bin`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/Info.plist`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/ar.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/bg.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/bn.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/ca.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/carrier.loctable`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/carrier.plist`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/cs.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/da.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/de.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/el.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/en.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/en_AU.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/en_GB.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/es.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/es_419.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/fi.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/fr.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/fr_CA.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/gu.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/he.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/hi.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/hr.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/hu.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/id.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/it.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/ja.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/kk.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/kn.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/ko.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/lt.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/ml.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/mr.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/ms.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/nl.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/no.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/or.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/overrides_D93_D94_D47_D48.der.pri`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/overrides_D93_D94_D47_D48.plist`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/pa.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/pl.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/pt.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/pt_PT.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/ro.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/ru.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/signatures`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/signatures/common.plist`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/signatures/overrides_D93_D94_D47_D48.plist`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/sk.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/sl.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/sv.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/ta.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/te.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/th.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/tr.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/uk.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/ur.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/vi.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/zh_CN.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/zh_HK.lproj`
- `/System/Library/Carrier Bundles/iPhone/ATT_MVNO_US.bundle/zh_TW.lproj`
- `/System/Library/Carrier Bundles/iPhone/LMT_lv.bundle/CarrierCA.crt`
- `/System/Library/Carrier Bundles/iPhone/SingTel_sg.bundle/CarrierCA.crt`
- `/System/Library/CoreServices/diagnosticservicesd`
- `/System/Library/CountryBundles/iPhone/Japan.bundle/overrides_D93_D94_D47_D48.plist`
- `/System/Library/CountryBundles/iPhone/Japan.bundle/signatures/overrides_D93_D94_D47_D48.plist`
- `/System/Library/ExtensionKit/Extensions/LighthouseAVShadowEval.appex/Info.plist`
- `/System/Library/ExtensionKit/Extensions/LighthouseAVShadowEval.appex/LighthouseAVShadowEval`
- `/System/Library/ExtensionKit/Extensions/LighthouseAVShadowEval.appex/_CodeSignature/CodeResources`
- `/System/Library/ExtensionKit/Extensions/MessageCenterApplicationServiceDiscoveryExtension.appex/Info.plist`
- `/System/Library/ExtensionKit/Extensions/MessageCenterApplicationServiceDiscoveryExtension.appex/MessageCenterApplicationServiceDiscoveryExtension`
- `/System/Library/ExtensionKit/Extensions/MessageCenterApplicationServiceDiscoveryExtension.appex/_CodeSignature/CodeResources`
- `/System/Library/ExtensionKit/Extensions/NeighborhoodActivityConduitIntentsExtension.appex/Info.plist`
- `/System/Library/ExtensionKit/Extensions/NeighborhoodActivityConduitIntentsExtension.appex/InfoPlist.loctable`
- `/System/Library/ExtensionKit/Extensions/NeighborhoodActivityConduitIntentsExtension.appex/NeighborhoodActivityConduitIntentsExtension`
- `/System/Library/ExtensionKit/Extensions/NeighborhoodActivityConduitIntentsExtension.appex/_CodeSignature/CodeResources`
- `/System/Library/ExtensionKit/Extensions/PRIMLCKPreemptivePing.appex/Info.plist`
- `/System/Library/ExtensionKit/Extensions/PRIMLCKPreemptivePing.appex/PRIMLCKPreemptivePing`
- `/System/Library/ExtensionKit/Extensions/PRIMLCKPreemptivePing.appex/_CodeSignature/CodeResources`
- `/System/Library/ExtensionKit/Extensions/ZeoliteEvalExtension.appex/Info.plist`
- `/System/Library/ExtensionKit/Extensions/ZeoliteEvalExtension.appex/ZeoliteEvalExtension`
- `/System/Library/ExtensionKit/Extensions/ZeoliteEvalExtension.appex/_CodeSignature/CodeResources`
- `/System/Library/FeatureFlags/Domain/Diagnostics.plist`
- `/System/Library/Frameworks/NetworkExtension.framework/PlugIns/NEIKEv2Provider.appex/InfoPlist.loctable`
- `/System/Library/Frameworks/SystemConfiguration.framework/get-mobility-info`
- `/System/Library/LaunchDaemons/com.apple.diagnosticservicesd.plist`
- `/System/Library/LaunchDaemons/com.apple.memoryanalyticsd.plist`
- `/System/Library/MLHost/StaticTasks/com.apple.priml.PRIMLCKPreemptivePing.plist`
- `/System/Library/PreferenceBundles/ScreenTimeSettings.bundle/Localizable.loctable`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.FaceTime.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.IDS.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.Messages.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.MessagesEvents.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.ProximityControl.plist`
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
- `/System/Library/Preferences/Logging/Subsystems/com.apple.findmy.framework.FindMyServerInteraction.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.podcasts.plist`
- `/System/Library/Preferences/Logging/Subsystems/com.apple.voicemail.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/19911f1e113a20108585dfe9b5da1c7300e3281a.asset/AssetData/country.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/19911f1e113a20108585dfe9b5da1c7300e3281a.asset/AssetData/general.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/19911f1e113a20108585dfe9b5da1c7300e3281a.asset/Info.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/34da9f8eb25207abcf4fdc11acc49379f56b2a8c.asset/AssetData/country.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/34da9f8eb25207abcf4fdc11acc49379f56b2a8c.asset/AssetData/general.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/34da9f8eb25207abcf4fdc11acc49379f56b2a8c.asset/Info.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/4bd84b4cc282163f5d10f33994945587f88edcee.asset/AssetData/country.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/4bd84b4cc282163f5d10f33994945587f88edcee.asset/AssetData/general.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/4bd84b4cc282163f5d10f33994945587f88edcee.asset/Info.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/8ae2328860d35a993f455454ebd56a837bf47c29.asset/AssetData/country.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/8ae2328860d35a993f455454ebd56a837bf47c29.asset/AssetData/general.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/8ae2328860d35a993f455454ebd56a837bf47c29.asset/Info.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/920ab89c787d62795c8e92a78282f1ba49ea8709.asset/AssetData/country.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/920ab89c787d62795c8e92a78282f1ba49ea8709.asset/AssetData/general.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/920ab89c787d62795c8e92a78282f1ba49ea8709.asset/Info.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/a7a9b218c3bb7d22758f57acf2cbe5898e7c7ebf.asset/AssetData/country.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/a7a9b218c3bb7d22758f57acf2cbe5898e7c7ebf.asset/AssetData/general.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/a7a9b218c3bb7d22758f57acf2cbe5898e7c7ebf.asset/Info.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/bf41380cdb1545c21644915f9b9c7eb0bc62859f.asset/AssetData/country.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/bf41380cdb1545c21644915f9b9c7eb0bc62859f.asset/AssetData/general.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/bf41380cdb1545c21644915f9b9c7eb0bc62859f.asset/Info.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/c69bb9986166f2e214bd309e14e3b1125cbe2370.asset/AssetData/country.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/c69bb9986166f2e214bd309e14e3b1125cbe2370.asset/AssetData/general.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/c69bb9986166f2e214bd309e14e3b1125cbe2370.asset/Info.plist`
- `/System/Library/PrivateFrameworks/CosmeticAssessment.framework/Assets.car`
- `/System/Library/PrivateFrameworks/CosmeticAssessment.framework/Info.plist`
- `/System/Library/PrivateFrameworks/CosmeticAssessment.framework/Localizable.loctable`
- `/System/Library/PrivateFrameworks/CosmeticAssessment.framework/_CodeSignature/CodeResources`
- `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/AirPlayDiagnosticExtension.appex/AirPlayDiagnosticExtension`
- `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/AirPlayDiagnosticExtension.appex/Info.plist`
- `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/AirPlayDiagnosticExtension.appex/_CodeSignature/CodeResources`
- `/System/Library/PrivateFrameworks/FedStats.framework/PlugIns/FedStatsMLRPlugin.appex/FedStatsCohortValueAllowList.plist`
- `/System/Library/PrivateFrameworks/FedStats.framework/PlugIns/FedStatsMLRPlugin.appex/FedStatsCohortValueBlockList.plist`
- `/System/Library/PrivateFrameworks/FedStats.framework/PlugIns/FedStatsMLRPluginClassB.appex/FedStatsCohortValueAllowList.plist`
- `/System/Library/PrivateFrameworks/FedStats.framework/PlugIns/FedStatsMLRPluginClassB.appex/FedStatsCohortValueBlockList.plist`
- `/System/Library/PrivateFrameworks/FedStats.framework/PlugIns/FedStatsMLRPluginNonDnU.appex/FedStatsCohortValueAllowList.plist`
- `/System/Library/PrivateFrameworks/FedStats.framework/PlugIns/FedStatsMLRPluginNonDnU.appex/FedStatsCohortValueBlockList.plist`
- `/System/Library/PrivateFrameworks/FedStatsPluginCore.framework/FedStatsCohortValueAllowList.plist`
- `/System/Library/PrivateFrameworks/FedStatsPluginCore.framework/FedStatsCohortValueBlockList.plist`
- `/System/Library/PrivateFrameworks/FedStatsPluginCore.framework/FedStatsPluginCoreConsentConfiguration.plist`
- `/System/Library/PrivateFrameworks/FedStatsPluginCore.framework/FedStatsPluginPrunableStreams.plist`
- `/System/Library/PrivateFrameworks/FindMyUICore.framework/TNLLocalized.loctable`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/1D6RNH4501N0I/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/1GMIFJUEYC9G7/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/2KFAWY931H6YZ/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/2KWH1YPUOUULL/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/2PSKMK9MFR195/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/3HBXMT4PZNSFK/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/3LPJ6LBW1QH5X/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/3V22A4DGPOK48/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/3VWWSX02U9HUF/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/53OO8VRPCIMA/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/79CBRUPBQWI7/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/featureUnsupportedForRemoteClients.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/unavailableWithoutEnablement.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/Templates/dialog/HomeAutomation.catfamily/BlockMulticardinalRequests.cat/es-cl.cat.bin`
- `/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/Templates/dialog/HomeAutomation.catfamily/ConfirmTemperature.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/Templates/dialog/HomeAutomation.catfamily/ConfirmTemperature.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/Templates/schema/homeAutomation.AbstractMeasurements.catschema.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Metadata.generativefunctions/-Ct5aF7INvkwygqcxVy0urnCJVg.`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Metadata.generativefunctions/8wlV3JjCjJ6-OBHCd-Ffo-aCUo0.`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Metadata.generativefunctions/OWs1BM2VPV56LUF6803Ztuz8sO0.`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerSupport.framework/ToolBoxAllowList.plist`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerSupport.framework/ToolPromptOverride.json`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerSupport.framework/ToolRetrievalContextAllowList.plist`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerSupport.framework/spiece_mmap.model`
- `/System/Library/PrivateFrameworks/NDOAPI.framework/Info.plist`
- `/System/Library/PrivateFrameworks/NDOAPI.framework/_CodeSignature/CodeResources`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Assets.car`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Info.plist`
- `/System/Library/PrivateFrameworks/NDOUI.framework/Localizable.loctable`
- `/System/Library/PrivateFrameworks/NDOUI.framework/_CodeSignature/CodeResources`
- `/System/Library/PrivateFrameworks/NeighborhoodActivityConduitIntents.framework/Info.plist`
- `/System/Library/PrivateFrameworks/NeighborhoodActivityConduitIntents.framework/Localizable.loctable`
- `/System/Library/PrivateFrameworks/NeighborhoodActivityConduitIntents.framework/_CodeSignature/CodeResources`
- `/System/Library/PrivateFrameworks/OmniSearch.framework/NamespaceDescriptor.SEARCH_TOOL_ANSWER_SYNTHESIS.plist`
- `/System/Library/PrivateFrameworks/OmniSearch.framework/default_factors_SEARCH_TOOL_ANSWER_SYNTHESIS.pb`
- `/System/Library/PrivateFrameworks/PodcastsFoundation.framework/com.apple.podcasts.plist`
- `/System/Library/PrivateFrameworks/SensorAccess.framework/Info.plist`
- `/System/Library/PrivateFrameworks/SensorAccess.framework/_CodeSignature/CodeResources`
- `/System/Library/PrivateFrameworks/SiriContactsIntents.framework/Templates/dialog/GetContactAttribute.catfamily/IntentHandledShowAddress.cat/vi_VN_u_sd_vnct.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/AlreadyActive.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/AlreadyActive.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/AnswerWhoAmI.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/AnswerWhoAmI.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/CannotSwitchForSingleProfile.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/CannotSwitchForSingleProfile.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/ConfirmRemotePlay.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/ConfirmRemotePlay.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/ConfirmationCancelled.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/ConfirmationCancelled.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/EstablishMultiUser.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/EstablishMultiUser.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/EstablishSingleUser.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/EstablishSingleUser.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/HomeUserAccountDoesNotExist.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/HomeUserAccountDoesNotExist.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/Identify.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/Identify.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/MissingMeCardData.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/MissingMeCardData.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/MultiUserUnavailable.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/MultiUserUnavailable.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/PartialMeCardData.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/PartialMeCardData.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/ProfileSelectPrompt.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/ProfileSelectPrompt.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/RemoteDeviceNotFound.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/RemoteDeviceNotFound.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/RemotePlayDisambiguateResults.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/RemotePlayDisambiguateResults.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/RemotePlayDisambiguateResultsDisplay.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/RemotePlayDisambiguateResultsDisplay.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/Unrecognized.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/Unrecognized.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/UnrecognizedAmbiguous.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/UnrecognizedAmbiguous.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/UnrecognizedOfferVoiceId.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/UnrecognizedOfferVoiceId.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/Unsupported.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/Unsupported.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/UserUnknown.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/UserUnknown.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/VoiceNotRecognizedButOneAccount.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/VoiceNotRecognizedButOneAccount.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/HandoffErrors.catfamily/CompanionLanguageMismatch.cat/es-us.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/UserIdentityCheck.catfamily/UnrecognizedSpeaker.cat/de-ch.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/es-cl.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/UserIdentityCheck.catfamily/UnsupportedICloudUser.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/SiriLocalization.framework/Info.plist`
- `/System/Library/PrivateFrameworks/SiriLocalization.framework/_CodeSignature/CodeResources`
- `/System/Library/PrivateFrameworks/SiriMessagesFlow.framework/Templates/dialog/SearchForMessages.catfamily/OfferSendMessageIntent.cat/en-za.cat.bin`
- `/System/Library/PrivateFrameworks/SiriMessagesFlow.framework/Templates/dialog/SearchForMessages.catfamily/OfferSendMessageIntent.cat/vi_VN_u_sd_vnct.cat.bin`
- `/System/Library/PrivateFrameworks/SiriMessagesFlow.framework/Templates/dialog/SearchForMessages.catfamily/ReadSpokenGenericCountableComponent.cat/it-ch.cat.bin`
- `/System/Library/PrivateFrameworks/SiriMessagesFlow.framework/Templates/dialog/SendMessage.catfamily/FailureCantMessage.cat/nl-be.cat.bin`
- `/System/Library/PrivateFrameworks/SiriMessagesFlow.framework/Templates/dialog/SendMessage.catfamily/HoldSend.cat/en-in.cat.bin`
- `/System/Library/PrivateFrameworks/SiriMessagesFlow.framework/Templates/dialog/SendMessage.catfamily/HoldSend.cat/es-us.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/de-ch.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/es-cl.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/nl-be.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/SetLyricsStateFailed.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/Localizable.loctable`
- `/System/Library/PrivateFrameworks/TVLatency.framework/Tones.bundle/241016_gain_reduced_calibrationTone_AtmosSpiral.ec3`
- `/System/Library/PrivateFrameworks/WorkflowResponsiveness.framework/WorkflowPlists/PodcastsCoreDataPrivateContext.plist`
- `/System/Library/PrivateFrameworks/WorkflowResponsiveness.framework/WorkflowPlists/SiriQueryDecorator_GetContextTimeouts.plist`
- `/System/Library/SESStorage/Asset/DCK/XPEV.plist`
- `/System/Library/Security/Certificates.bundle/Anchors/B296DC3BCF451217D7AD4F84FB8EE25CC92FC659CAFA0EB4A8B5B4DB3D0215C2.cer`
- `/System/Library/Siri/DM/SiriSuggestions/Owners/AudioSuggestionsPlugin.bundle/Templates/dialog/AudioSuggestions.catfamily/PlayPlaylist.cat/fr-be.cat.bin`
- `/System/Library/Siri/DM/SiriSuggestions/Owners/AudioSuggestionsPlugin.bundle/Templates/dialog/AudioSuggestions.catfamily/PlayPlaylist.cat/fr-ch.cat.bin`
- `/System/Library/Siri/DM/SiriSuggestions/Owners/AudioSuggestionsPlugin.bundle/Templates/dialog/AudioSuggestions.catfamily/PlayPlaylist.cat/vi_VN_u_sd_vnct.cat.bin`
- `/System/Library/Trial/NamespaceDescriptors/NamespaceDescriptor.AIRPLAY.plist`
- `/System/Library/Trial/NamespaceDescriptors/NamespaceDescriptor.BATTERYINTELLIGENCE_BATTERY_ANALYSIS.plist`
- `/System/Library/Trial/NamespaceDescriptors/NamespaceDescriptor.COREOS_PERFPOWER_IDLE_REAPER.plist`
- `/System/Library/Trial/NamespaceDescriptors/NamespaceDescriptor.COREOS_XNU_LATENCY_GUARDS.plist`
- `/System/Library/Trial/NamespaceDescriptors/NamespaceDescriptor.ENHANCED_DEBUGGING_LIBSANITIZERS.plist`
- `/System/Library/Trial/NamespaceDescriptors/NamespaceDescriptor.MAPS_SRP_AUTOCOMPLETE.plist`
- `/System/Library/Trial/NamespaceDescriptors/NamespaceDescriptor.MEDIAEXPERIENCE.plist`
- `/System/Library/Trial/NamespaceDescriptors/NamespaceDescriptor.POWER_EXCEPTIONS_MITIGATIONS.plist`
- `/System/Library/Trial/NamespaceDescriptors/NamespaceDescriptor.RULES_ENGINE_ENABLED_MIGRATION.plist`
- `/System/Library/Trial/NamespaceDescriptors/NamespaceDescriptor.SEARCH_TOOL_ANSWER_SYNTHESIS.plist`
- `/System/Library/Trial/NamespaceDescriptors/NamespaceDescriptor.SIML_ADM_PERSONALIZATION.plist`
- `/System/Library/Trial/NamespaceDescriptors/NamespaceDescriptor.SMS_FILTER_FELIS.plist`
- `/System/Library/Trial/NamespaceDescriptors/NamespaceDescriptor.SMS_FILTER_KYOTO.plist`
- `/System/Library/Trial/NamespaceDescriptors/NamespaceDescriptor.TELEPHONY_WIFI_CELLULAR_HANDOVER_POLICY.plist`
- `/System/Library/Trial/NamespaceDescriptors/NamespaceDescriptor.WEBKIT_LIBPAS_PGM.plist`
- `/System/Library/Trial/NamespaceDescriptors/NamespaceDescriptor.WEBKIT_PROBABILISTIC_GUARD_MALLOC.plist`
- `/System/Library/UnifiedAssetFramework/AssetSets/com.apple.MobileAsset.CN.Guardrail.plist`
- `/System/Library/UnifiedAssetFramework/UsageAliases/com.apple.Siri.Planner.migration.18.4.plist`
- `/System/Library/UnifiedAssetFramework/UsageAliases/safety.chinaGuardrail.migration.18.4.plist`
- `/System/Library/UnifiedAssetFramework/UsageAliases/safety.chinaGuardrail.plist`
- `/System/Library/UserNotifications/Bundles/com.apple.NewDeviceOutreach.UserNotificationsBundle.bundle/Assets.car`
- `/System/Library/UserNotifications/Bundles/com.apple.NewDeviceOutreach.UserNotificationsBundle.bundle/Info.plist`
- `/System/Library/UserNotifications/Bundles/com.apple.NewDeviceOutreach.UserNotificationsBundle.bundle/InfoPlist.strings`
- `/System/Library/UserNotifications/Bundles/com.apple.NewDeviceOutreach.UserNotificationsBundle.bundle/_CodeSignature/CodeDirectory`
- `/System/Library/UserNotifications/Bundles/com.apple.NewDeviceOutreach.UserNotificationsBundle.bundle/_CodeSignature/CodeRequirements`
- `/System/Library/UserNotifications/Bundles/com.apple.NewDeviceOutreach.UserNotificationsBundle.bundle/_CodeSignature/CodeRequirements-1`
- `/System/Library/UserNotifications/Bundles/com.apple.NewDeviceOutreach.UserNotificationsBundle.bundle/_CodeSignature/CodeResources`
- `/System/Library/UserNotifications/Bundles/com.apple.NewDeviceOutreach.UserNotificationsBundle.bundle/_CodeSignature/CodeSignature`
- `/private/var/staged_system_apps/Home.app/PlugIns/HomeUtilNotification.appex/es_US.lproj`
- `/private/var/staged_system_apps/Passbook.app/PlugIns/PassbookQuicklookPreviewExtension.appex/es_US.lproj`
- `/private/var/staged_system_apps/Tips.app/ar.lproj/nlu.appintents/4ce88f9ab13774e2fa08561adbdfc6a4.version`
- `/private/var/staged_system_apps/Tips.app/bg.lproj/nlu.appintents/92eedf52305103d45ec3db6c379763f7.version`
- `/private/var/staged_system_apps/Tips.app/bn.lproj/nlu.appintents/be40118d21edb3107703a848280924ad.version`
- `/private/var/staged_system_apps/Tips.app/ca.lproj/nlu.appintents/316646dff0af41ec886e07d4c57239c1.version`
- `/private/var/staged_system_apps/Tips.app/cs.lproj/nlu.appintents/558dcff039686910fabd512a40354121.version`
- `/private/var/staged_system_apps/Tips.app/da.lproj/nlu.appintents/2bb39621730990b7acc9d6798a3bcc5c.version`
- `/private/var/staged_system_apps/Tips.app/de.lproj/nlu.appintents/0d982e838064c38e73ae27ac917a1821.version`
- `/private/var/staged_system_apps/Tips.app/el.lproj/nlu.appintents/067468e3c90c3a5cbe4284b5feccd4ad.version`
- `/private/var/staged_system_apps/Tips.app/en.lproj/nlu.appintents/f5ea9305e9172e9a4930cff0f09797d8.version`
- `/private/var/staged_system_apps/Tips.app/en_AU.lproj/nlu.appintents/18fdeafc63fc445608e2af272c8a9469.version`
- `/private/var/staged_system_apps/Tips.app/en_GB.lproj/nlu.appintents/ef4b4bd01ba92cbb110240cb135ae63b.version`
- `/private/var/staged_system_apps/Tips.app/es.lproj/nlu.appintents/9c49d46ec6357b5bf7bd2ac6813e4489.version`
- `/private/var/staged_system_apps/Tips.app/es_419.lproj/nlu.appintents/a8ec9ba761f0337e65dad35eff856181.version`
- `/private/var/staged_system_apps/Tips.app/es_US.lproj/nlu.appintents/c2e08ce7e721791e2cfd6f06b3163026.version`
- `/private/var/staged_system_apps/Tips.app/fi.lproj/nlu.appintents/875871b36d955301dd9b2f8cb61d9b88.version`
- `/private/var/staged_system_apps/Tips.app/fr.lproj/nlu.appintents/f8178299d3bbeb612ac25e9f0e6f0ee1.version`
- `/private/var/staged_system_apps/Tips.app/fr_CA.lproj/nlu.appintents/0ef8258a97dd31ba071834dad3a8507c.version`
- `/private/var/staged_system_apps/Tips.app/gu.lproj/nlu.appintents/f70dd8f824f4e5988391da60c1d52559.version`
- `/private/var/staged_system_apps/Tips.app/he.lproj/nlu.appintents/50b0341c005859c8b5e3c4c738de3c85.version`
- `/private/var/staged_system_apps/Tips.app/hi.lproj/nlu.appintents/a4ec72e13dd959447bfe0ea56d568fc9.version`
- `/private/var/staged_system_apps/Tips.app/hr.lproj/nlu.appintents/05c6c4c924d1fd9541e39a6042b09789.version`
- `/private/var/staged_system_apps/Tips.app/hu.lproj/nlu.appintents/46d14ddcb8eb0ffc9de605c3f6c264ca.version`
- `/private/var/staged_system_apps/Tips.app/id.lproj/nlu.appintents/589a547951c80c4d8635b57895b0a172.version`
- `/private/var/staged_system_apps/Tips.app/it.lproj/nlu.appintents/c60eb066fa220dea2f276584d228a251.version`
- `/private/var/staged_system_apps/Tips.app/ja.lproj/nlu.appintents/a2d9ecd74b505815ad8e72a5cf87f9cc.version`
- `/private/var/staged_system_apps/Tips.app/kk.lproj/nlu.appintents/97cc8c5a35bc54e7ce177afaf0757e74.version`
- `/private/var/staged_system_apps/Tips.app/kn.lproj/nlu.appintents/ae4876d34bedcdb9dd69d22ae412b78d.version`
- `/private/var/staged_system_apps/Tips.app/ko.lproj/nlu.appintents/ee8c7577556b625362c85fe5b4071150.version`
- `/private/var/staged_system_apps/Tips.app/lt.lproj/nlu.appintents/d9f5dc825f20d7a9cf45871365bd6f2c.version`
- `/private/var/staged_system_apps/Tips.app/ml.lproj/nlu.appintents/09df8c8314e542d83dd49a54c7f93c70.version`
- `/private/var/staged_system_apps/Tips.app/mr.lproj/nlu.appintents/dd508e065cd0719b2d9c55ee06405cff.version`
- `/private/var/staged_system_apps/Tips.app/ms.lproj/nlu.appintents/7436b46c847717f3ac615ef63aa61548.version`
- `/private/var/staged_system_apps/Tips.app/nl.lproj/nlu.appintents/4de77665ffc6ac40791a35a6ff40ad06.version`
- `/private/var/staged_system_apps/Tips.app/no.lproj/nlu.appintents/8d9490eda2cabae8f828ef4abc58365e.version`
- `/private/var/staged_system_apps/Tips.app/or.lproj/nlu.appintents/8dd3234a59541ce2549e1746cd614bcc.version`
- `/private/var/staged_system_apps/Tips.app/pa.lproj/nlu.appintents/4ec0795fc8a33925773a112c3e1f68a0.version`
- `/private/var/staged_system_apps/Tips.app/pl.lproj/nlu.appintents/f4fc32471b0a33a3c63f285fc2e9c316.version`
- `/private/var/staged_system_apps/Tips.app/pt_BR.lproj/nlu.appintents/58de1d37bfac4f59d497aaa3828952b3.version`
- `/private/var/staged_system_apps/Tips.app/ro.lproj/nlu.appintents/6766b4b96b55937269dfec81bd33fa0a.version`
- `/private/var/staged_system_apps/Tips.app/ru.lproj/nlu.appintents/d6b96091f2fad0a17a6f61cf36b4c3e5.version`
- `/private/var/staged_system_apps/Tips.app/sk.lproj/nlu.appintents/d2df1ed3a020c50cd71ab34575eefb3b.version`
- `/private/var/staged_system_apps/Tips.app/sl.lproj/nlu.appintents/d68e82a9f59df8c21d8d9c1d53561849.version`
- `/private/var/staged_system_apps/Tips.app/sv.lproj/nlu.appintents/973e120826973b6ff6de4709489261c1.version`
- `/private/var/staged_system_apps/Tips.app/ta.lproj/nlu.appintents/7aa05f8559dc0bd81fd9aa20daa1fffc.version`
- `/private/var/staged_system_apps/Tips.app/th.lproj/nlu.appintents/ced853510beaf719d18c75031e285c11.version`
- `/private/var/staged_system_apps/Tips.app/tr.lproj/nlu.appintents/7e3459b98374b9202e106d2a0570d7b4.version`
- `/private/var/staged_system_apps/Tips.app/uk.lproj/nlu.appintents/28e62e86331e35471be92c12c845f86b.version`
- `/private/var/staged_system_apps/Tips.app/ur.lproj/nlu.appintents/43e271af0bf311e21e773dbbce4f25c3.version`
- `/private/var/staged_system_apps/Tips.app/vi.lproj/nlu.appintents/86eed2b82170d923d15bc6c5dd21a5ee.version`
- `/private/var/staged_system_apps/Tips.app/zh_CN.lproj/nlu.appintents/8536ceb7fa51dbde2540766320fcc4a6.version`
- `/private/var/staged_system_apps/Tips.app/zh_HK.lproj/nlu.appintents/a04fbb28bcd850f3385e1b80828526a8.version`
- `/private/var/staged_system_apps/Tips.app/zh_TW.lproj/nlu.appintents/ee7d0b0e16cda0c2db252b3122853466.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Base.lproj/nlu.appintents/b20123b8367c52d86ce4c69c22564b1a.version`
- `/private/var/staged_system_apps/VoiceMemos.app/en.lproj/nlu.appintents/c308d7bfdfb1012dad6f5552b0fdac87.version`
- `/usr/libexec/memoryanalyticsd`
- `/usr/share/firmware/bluetooth/BCM4399C2_22.6.161.731_PCIE_Cephalotus_CLPC_OS_STATS_20250313.bin`
- `/usr/share/firmware/bluetooth/BCM4399C2_22.6.161.732_PCIE_Cephalotus_CLPC_OS_USI_20250313.bin`

</details>

##### SystemOS (1)

- `/System/Library/PrivateFrameworks/NeighborhoodActivityConduitIntents.framework/NeighborhoodActivityConduitIntents`

##### ExclaveOS (24)

<details>
  <summary><i>View Files</i></summary>

- `/System/ExclaveKit/System/Library/Frameworks/IsolatedAudioMeterClientExclaveComponent.framework/Info.plist`
- `/System/ExclaveKit/System/Library/Frameworks/IsolatedAudioMeterClientExclaveComponent.framework/_CodeSignature/CodeResources`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-AU/AssetData/megatron_hsjs_8bit_compressed_v1_fp32_mil2bnns.mlmodelc.bnnsir`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-AU/AssetData/megatron_hsjs_8bit_compressed_v1_fp32_mil2bnns.mlmodelc.weights`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-AU/AssetData/rtblob_aop_1_4.bin`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-AU/AssetData/rtblob_aop_1_4.signature`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-GB/AssetData/megatron_hsjs_8bit_compressed_v1_fp32_mil2bnns.mlmodelc.bnnsir`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-GB/AssetData/megatron_hsjs_8bit_compressed_v1_fp32_mil2bnns.mlmodelc.weights`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-GB/AssetData/rtblob_aop_1_4.bin`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-GB/AssetData/rtblob_aop_1_4.signature`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-IE/AssetData/megatron_hsjs_8bit_compressed_v1_fp32_mil2bnns.mlmodelc.bnnsir`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-IE/AssetData/megatron_hsjs_8bit_compressed_v1_fp32_mil2bnns.mlmodelc.weights`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-IE/AssetData/rtblob_aop_1_4.bin`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-IE/AssetData/rtblob_aop_1_4.signature`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-US/AssetData/megatron_hsjs_8bit_compressed_v1_fp32_mil2bnns.mlmodelc.bnnsir`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-US/AssetData/megatron_hsjs_8bit_compressed_v1_fp32_mil2bnns.mlmodelc.weights`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-US/AssetData/rtblob_aop_1_4.bin`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-US/AssetData/rtblob_aop_1_4.signature`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-ZA/AssetData/megatron_hsjs_8bit_compressed_v1_fp32_mil2bnns.mlmodelc.bnnsir`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-ZA/AssetData/megatron_hsjs_8bit_compressed_v1_fp32_mil2bnns.mlmodelc.weights`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-ZA/AssetData/rtblob_aop_1_4.bin`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-ZA/AssetData/rtblob_aop_1_4.signature`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/vi-VN/AssetData/megatron_hsjs_8bit_compressed_v1_fp32_mil2bnns.mlmodelc.bnnsir`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/vi-VN/AssetData/megatron_hsjs_8bit_compressed_v1_fp32_mil2bnns.mlmodelc.weights`

</details>

#### ❌ Removed

##### IPSW (2)

- `Firmware/Mav24-1.54.03.Release.bbfw`
- `Firmware/Mav24-1.54.03.Release.plist`

##### filesystem (974)

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
- `/System/Library/Assistant/Plugins/SurfStatusSync.assistantBundle/Info.plist`
- `/System/Library/Assistant/Plugins/SurfStatusSync.assistantBundle/_CodeSignature/CodeResources`
- `/System/Library/CoreServices/BluetoothUIService.app/Banner-PID-8218-Seed/Banner-PID-8218-6-Seed.png`
- `/System/Library/CoreServices/BluetoothUIService.app/Banner-PID-8218-Seed/Banner-PID-8218-7-Seed.png`
- `/System/Library/ExtensionKit/Extensions/ConditionalEngineAppIntentsExtension.appex/ConditionalEngineAppIntentsExtension`
- `/System/Library/ExtensionKit/Extensions/ConditionalEngineAppIntentsExtension.appex/Info.plist`
- `/System/Library/ExtensionKit/Extensions/ConditionalEngineAppIntentsExtension.appex/_CodeSignature/CodeResources`
- `/System/Library/ExtensionKit/Extensions/ConditionalEngineLighthouseExtension.appex/ConditionalEngineLighthouseExtension`
- `/System/Library/ExtensionKit/Extensions/ConditionalEngineLighthouseExtension.appex/Info.plist`
- `/System/Library/ExtensionKit/Extensions/ConditionalEngineLighthouseExtension.appex/_CodeSignature/CodeResources`
- `/System/Library/ExtensionKit/Extensions/IEMetricsWorker.appex/IEMetricsWorker`
- `/System/Library/ExtensionKit/Extensions/IEMetricsWorker.appex/Info.plist`
- `/System/Library/ExtensionKit/Extensions/IEMetricsWorker.appex/_CodeSignature/CodeResources`
- `/System/Library/ExtensionKit/Extensions/ZeoliteExtension.appex/Info.plist`
- `/System/Library/ExtensionKit/Extensions/ZeoliteExtension.appex/ZeoliteExtension`
- `/System/Library/ExtensionKit/Extensions/ZeoliteExtension.appex/_CodeSignature/CodeResources`
- `/System/Library/FeatureFlags/Domain/ConditionalEngine.plist`
- `/System/Library/Frameworks/VideoToolbox.framework/XPCServices/videodecodeservice.xpc/Info.plist`
- `/System/Library/Frameworks/VideoToolbox.framework/XPCServices/videodecodeservice.xpc/_CodeSignature/CodeResources`
- `/System/Library/Frameworks/VideoToolbox.framework/XPCServices/videodecodeservice.xpc/videodecodeservice`
- `/System/Library/LaunchDaemons/com.apple.fusiond.plist`
- `/System/Library/MLHost/StaticTasks/com.apple.conditionalengine.daily.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/00cc9eccd1704afb1e0b66bf53fe4c7801a1b77b.asset/AssetData/UnitedStatesSettings.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/00cc9eccd1704afb1e0b66bf53fe4c7801a1b77b.asset/AssetData/countryInfoMap.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/00cc9eccd1704afb1e0b66bf53fe4c7801a1b77b.asset/AssetData/settings.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/00cc9eccd1704afb1e0b66bf53fe4c7801a1b77b.asset/Info.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/979f422c64f5dc8b5f786fe9d8b7c3d1c8039de8.asset/AssetData/country.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/979f422c64f5dc8b5f786fe9d8b7c3d1c8039de8.asset/AssetData/general.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/979f422c64f5dc8b5f786fe9d8b7c3d1c8039de8.asset/Info.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/98a6334f5a90e8c2f1bcc9a8780f5b3cfb80ca3f.asset/AssetData/UnitedStatesSettings.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/98a6334f5a90e8c2f1bcc9a8780f5b3cfb80ca3f.asset/AssetData/countryInfoMap.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/98a6334f5a90e8c2f1bcc9a8780f5b3cfb80ca3f.asset/AssetData/settings.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/98a6334f5a90e8c2f1bcc9a8780f5b3cfb80ca3f.asset/Info.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/993bcb8246fd0c7489847880e8121b0418b2733e.asset/AssetData/country.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/993bcb8246fd0c7489847880e8121b0418b2733e.asset/AssetData/general.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/993bcb8246fd0c7489847880e8121b0418b2733e.asset/Info.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/a446c82856426792fcd002e7703a4fdae0e229dc.asset/AssetData/country.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/a446c82856426792fcd002e7703a4fdae0e229dc.asset/AssetData/general.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/a446c82856426792fcd002e7703a4fdae0e229dc.asset/Info.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/b4704b12e5952bcfc34e7b78f10c940eed3a71a8.asset/AssetData/country.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/b4704b12e5952bcfc34e7b78f10c940eed3a71a8.asset/AssetData/general.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/b4704b12e5952bcfc34e7b78f10c940eed3a71a8.asset/Info.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/bcb4eb8cf2eb3e1b6bf6aa73b445eee7785dc373.asset/AssetData/UnitedStatesSettings.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/bcb4eb8cf2eb3e1b6bf6aa73b445eee7785dc373.asset/AssetData/countryInfoMap.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/bcb4eb8cf2eb3e1b6bf6aa73b445eee7785dc373.asset/AssetData/settings.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/bcb4eb8cf2eb3e1b6bf6aa73b445eee7785dc373.asset/Info.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/c47322d3262595a786c4e3840ec37b3004376ffd.asset/AssetData/country.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/c47322d3262595a786c4e3840ec37b3004376ffd.asset/AssetData/general.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/c47322d3262595a786c4e3840ec37b3004376ffd.asset/Info.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/da3da61caa72667e7006399442c48e8b09432088.asset/AssetData/country.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/da3da61caa72667e7006399442c48e8b09432088.asset/AssetData/general.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/da3da61caa72667e7006399442c48e8b09432088.asset/Info.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/e938a243854db21ccc0ee07c17ddf43af1bf6d6b.asset/AssetData/country.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/e938a243854db21ccc0ee07c17ddf43af1bf6d6b.asset/AssetData/general.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/e938a243854db21ccc0ee07c17ddf43af1bf6d6b.asset/Info.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/f776268c091a41c53acc3a6c5bda0181fccb221e.asset/AssetData/country.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/f776268c091a41c53acc3a6c5bda0181fccb221e.asset/AssetData/general.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/f776268c091a41c53acc3a6c5bda0181fccb221e.asset/Info.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/f949be2b5bc29e8d9e985afc0fa7fbf4a3559fb0.asset/AssetData/settings.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_CoreLocationConfig/f949be2b5bc29e8d9e985afc0fa7fbf4a3559fb0.asset/Info.plist`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_SharingDeviceAssets/7f50a81a71f8ff6cebbf2d151474b0256a253146.asset/AssetData/empty.txt`
- `/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_SharingDeviceAssets/7f50a81a71f8ff6cebbf2d151474b0256a253146.asset/Info.plist`
- `/System/Library/PrivateFrameworks/ConditionalEngineAppIntents.framework/Info.plist`
- `/System/Library/PrivateFrameworks/ConditionalEngineAppIntents.framework/Metadata.appintents/extract.actionsdata`
- `/System/Library/PrivateFrameworks/ConditionalEngineAppIntents.framework/Metadata.appintents/version.json`
- `/System/Library/PrivateFrameworks/ConditionalEngineAppIntents.framework/_CodeSignature/CodeResources`
- `/System/Library/PrivateFrameworks/ConditionalEngineClient.framework/Info.plist`
- `/System/Library/PrivateFrameworks/ConditionalEngineClient.framework/_CodeSignature/CodeResources`
- `/System/Library/PrivateFrameworks/ConditionalEngineRuntime.framework/Info.plist`
- `/System/Library/PrivateFrameworks/ConditionalEngineRuntime.framework/_CodeSignature/CodeResources`
- `/System/Library/PrivateFrameworks/ConditionalEngineShared.framework/Info.plist`
- `/System/Library/PrivateFrameworks/ConditionalEngineShared.framework/_CodeSignature/CodeResources`
- `/System/Library/PrivateFrameworks/CoreThreadRadio.framework/BCM4388C2_MangosteenA_154_FINALv1_OS_STATS_20240625.ptb`
- `/System/Library/PrivateFrameworks/CoreThreadRadio.framework/BCM4388C2_MangosteenA_154_FINALv1_OS_USI_20240625.ptb`
- `/System/Library/PrivateFrameworks/CoreThreadRadio.framework/BCM4399C2_Audreyii_154_FINALv1_OS_STATS_20240727.ptb`
- `/System/Library/PrivateFrameworks/CoreThreadRadio.framework/BCM4399C2_Audreyii_154_FINALv1_OS_USI_20240727.ptb`
- `/System/Library/PrivateFrameworks/CoreThreadRadio.framework/BCM4399C2_Cephalotus_154_FINALv1_OS_STATS_20240708.ptb`
- `/System/Library/PrivateFrameworks/CoreThreadRadio.framework/BCM4399C2_Cephalotus_154_FINALv1_OS_USI_20240708.ptb`
- `/System/Library/PrivateFrameworks/CoreThreadRadio.framework/BCM4399C2_Nepenthes_154_FINALv1_OS_STATS_20240726.ptb`
- `/System/Library/PrivateFrameworks/CoreThreadRadio.framework/BCM4399C2_Nepenthes_154_FINALv1_OS_USI_20240726.ptb`
- `/System/Library/PrivateFrameworks/CoreThreadRadio.framework/BCM4399C2_Sundew_154_FINALv1_OS_STATS_20240704.ptb`
- `/System/Library/PrivateFrameworks/CoreThreadRadio.framework/BCM4399C2_Sundew_154_FINALv1_OS_USI_20240704.ptb`
- `/System/Library/PrivateFrameworks/FedStats.framework/PlugIns/FedStatsMLRPluginClassB.appex/assets_1546/recipe.json`
- `/System/Library/PrivateFrameworks/FedStats.framework/PlugIns/FedStatsMLRPluginClassB.appex/default_factors_1546.pb`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/119AIYY46DF82/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/11M6YI6YM3ACK/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/1FAEO8UOR7GBS/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/1V22TRM6AGX7Y/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/26FR7AG36FN51/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/2BZAB7GTLKTDY/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/2HE1M8DT1EOFB/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/2VF98EJC3E91B/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/3IOM7AA9K6TOQ/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/3L4840OQW6Q8D/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/lib/clang/32023.619/include/metal/prebuilt_implicit_modules/F725L7MPDOQU/monolithic_metal.pcm`
- `/System/Library/PrivateFrameworks/HeadphoneConfigs.framework/DeviceConfig-Seed.loctable`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Metadata.generativefunctions/DcOJ-FWQMD-aA7pq_XOiZhJ8IWY.`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Metadata.generativefunctions/HlrafOOIrVhnS2vlnrbNsA3Effw.`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Metadata.generativefunctions/UQRDb-9XZO8ErFlJAoiZJiGfvRM.`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Templates/dialog/responseGeneration.catfamily/actionConfirmation.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Templates/dialog/responseGeneration.catfamily/actionConfirmation.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Templates/dialog/responseGeneration.catfamily/actionFailure.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Templates/dialog/responseGeneration.catfamily/actionFailure.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Templates/dialog/responseGeneration.catfamily/actionRequirement.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Templates/dialog/responseGeneration.catfamily/actionRequirement.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Templates/dialog/responseGeneration.catfamily/actionSuccess.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Templates/dialog/responseGeneration.catfamily/actionSuccess.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Templates/dialog/responseGeneration.catfamily/actionUndo.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Templates/dialog/responseGeneration.catfamily/actionUndo.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Templates/dialog/responseGeneration.catfamily/conjunction.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Templates/dialog/responseGeneration.catfamily/conjunction.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Templates/dialog/responseGeneration.catfamily/continueOnDevice.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Templates/dialog/responseGeneration.catfamily/continueOnDevice.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Templates/dialog/responseGeneration.catfamily/error.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Templates/dialog/responseGeneration.catfamily/error.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Templates/dialog/responseGeneration.catfamily/labels.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Templates/dialog/responseGeneration.catfamily/labels.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Templates/dialog/responseGeneration.catfamily/parameterConfirmation.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Templates/dialog/responseGeneration.catfamily/parameterConfirmation.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Templates/dialog/responseGeneration.catfamily/parameterDisambiguation.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Templates/dialog/responseGeneration.catfamily/parameterDisambiguation.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Templates/dialog/responseGeneration.catfamily/parameterNeedsValue.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Templates/dialog/responseGeneration.catfamily/parameterNeedsValue.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Templates/dialog/responseGeneration.catfamily/parameterNotAllowed.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Templates/dialog/responseGeneration.catfamily/parameterNotAllowed.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Templates/schema/responseGeneration.ResponseDialog.catschema.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/Templates/schema/responseGeneration.Value.catschema.bin`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerSupport.framework/ToolBoxAllowList-CrystalE.plist`
- `/System/Library/PrivateFrameworks/IntelligenceFlowPlannerSupport.framework/spiece.model`
- `/System/Library/PrivateFrameworks/NewDeviceOutreachUI.framework/Base.lproj/NDOAppleCareView.nib`
- `/System/Library/PrivateFrameworks/NewDeviceOutreachUI.framework/Base.lproj/NDOAppleCareWebView.nib`
- `/System/Library/PrivateFrameworks/NewDeviceOutreachUI.framework/NDOAppleCareView.loctable`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/AlreadyActive.cat/_params.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/AlreadyActive.cat/en.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/AnswerWhoAmI.cat/_params.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/AnswerWhoAmI.cat/en.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/CannotSwitchForSingleProfile.cat/_params.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/CannotSwitchForSingleProfile.cat/en.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/ConfirmRemotePlay.cat/_params.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/ConfirmRemotePlay.cat/en.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/ConfirmationCancelled.cat/_params.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/ConfirmationCancelled.cat/en.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/EstablishMultiUser.cat/_params.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/EstablishMultiUser.cat/en.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/EstablishSingleUser.cat/_params.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/EstablishSingleUser.cat/en.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/HomeUserAccountDoesNotExist.cat/_params.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/HomeUserAccountDoesNotExist.cat/en.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/Identify.cat/_params.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/Identify.cat/en.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/MissingMeCardData.cat/_params.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/MissingMeCardData.cat/en.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/MultiUserUnavailable.cat/_params.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/MultiUserUnavailable.cat/en.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/PartialMeCardData.cat/_params.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/PartialMeCardData.cat/en.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/ProfileSelectPrompt.cat/_params.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/ProfileSelectPrompt.cat/en.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/RemoteDeviceNotFound.cat/_params.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/RemoteDeviceNotFound.cat/en.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/RemotePlayDisambiguateResults.cat/_params.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/RemotePlayDisambiguateResults.cat/en.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/RemotePlayDisambiguateResultsDisplay.cat/_params.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/RemotePlayDisambiguateResultsDisplay.cat/en.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/Unrecognized.cat/_params.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/Unrecognized.cat/en.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/UnrecognizedAmbiguous.cat/_params.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/UnrecognizedAmbiguous.cat/en.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/UnrecognizedOfferVoiceId.cat/_params.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/UnrecognizedOfferVoiceId.cat/en.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/Unsupported.cat/_params.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/Unsupported.cat/en.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/UserUnknown.cat/_params.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/UserUnknown.cat/en.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/VoiceNotRecognizedButOneAccount.cat/_params.cat.xml`
- `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/Templates/dialog/Identity.catfamily/VoiceNotRecognizedButOneAccount.cat/en.cat.xml`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/HandoffErrors.catfamily/CompanionLanguageMismatch.cat/en-ie.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/es-cl.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/es-us.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/fr-ca.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/NoTopologyChanges.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/_params.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/de-ch.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/en.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/es-cl.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/Templates/dialog/PlaybackControls.catfamily/ShowLyricsFailed.cat/zh-tw.cat.bin`
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
- `/System/Library/Trial/NamespaceDescriptors/com.apple.Trial.NamespaceDescriptor.1546.plist`
- `/private/var/staged_system_apps/Tips.app/ar.lproj/nlu.appintents/f52f22573f0dde4f74f17e8cf6e16ff6.version`
- `/private/var/staged_system_apps/Tips.app/bg.lproj/nlu.appintents/107ce16c8a2738f71c100f93043c5d15.version`
- `/private/var/staged_system_apps/Tips.app/bn.lproj/nlu.appintents/7a3a8c38490cca089a11814aa025568f.version`
- `/private/var/staged_system_apps/Tips.app/ca.lproj/nlu.appintents/5223c4fa6c4d19fb16c72a22fdd5732b.version`
- `/private/var/staged_system_apps/Tips.app/cs.lproj/nlu.appintents/117b06260aa0a8b2cb81df3713d668e8.version`
- `/private/var/staged_system_apps/Tips.app/da.lproj/nlu.appintents/f753328de977f065a4e05b8e3b117614.version`
- `/private/var/staged_system_apps/Tips.app/de.lproj/nlu.appintents/2a105c672ea821bad90446c4bbaf1459.version`
- `/private/var/staged_system_apps/Tips.app/el.lproj/nlu.appintents/d2de2beda870d4e36b61c28e162640f4.version`
- `/private/var/staged_system_apps/Tips.app/en.lproj/nlu.appintents/743360949b189f77dbd06f026b73a88c.version`
- `/private/var/staged_system_apps/Tips.app/en_AU.lproj/nlu.appintents/dfa3fedf9a1cbe8c63a36d367507eba7.version`
- `/private/var/staged_system_apps/Tips.app/en_GB.lproj/nlu.appintents/fb071e179e2dd651dc76a8c34687cc9e.version`
- `/private/var/staged_system_apps/Tips.app/es.lproj/nlu.appintents/e5be84b8c5afbff64e54b0d7e69f5aab.version`
- `/private/var/staged_system_apps/Tips.app/es_419.lproj/nlu.appintents/4db0abf3c72d026df12ccc25cf016fe8.version`
- `/private/var/staged_system_apps/Tips.app/es_US.lproj/nlu.appintents/87d7e2b7148e45296694d48b58357874.version`
- `/private/var/staged_system_apps/Tips.app/fi.lproj/nlu.appintents/2b31b4d478f7a3aea210ffbb22a39b2a.version`
- `/private/var/staged_system_apps/Tips.app/fr.lproj/nlu.appintents/a5adb59d06d25e03dbeeed58fb3001d6.version`
- `/private/var/staged_system_apps/Tips.app/fr_CA.lproj/nlu.appintents/73f92980b7c7d3ce9ff2b08f118be014.version`
- `/private/var/staged_system_apps/Tips.app/gu.lproj/nlu.appintents/de893beff03a3aa491f40d1d29c0dca5.version`
- `/private/var/staged_system_apps/Tips.app/he.lproj/nlu.appintents/502d0442a2a536961bd63fdff701590a.version`
- `/private/var/staged_system_apps/Tips.app/hi.lproj/nlu.appintents/e89436db045d3e9209b16848cb6ccc57.version`
- `/private/var/staged_system_apps/Tips.app/hr.lproj/nlu.appintents/1170d0c05da19fc8ddbc40b1f3902b05.version`
- `/private/var/staged_system_apps/Tips.app/hu.lproj/nlu.appintents/4facff71218ee0d57a695d64755b4824.version`
- `/private/var/staged_system_apps/Tips.app/id.lproj/nlu.appintents/bae6722c09346a37ccc6cc6cf81ae98f.version`
- `/private/var/staged_system_apps/Tips.app/it.lproj/nlu.appintents/a6223acdf7c47db9c7a440ef69d01016.version`
- `/private/var/staged_system_apps/Tips.app/ja.lproj/nlu.appintents/5bb00ea09d41a2b5eeec91c84c1029dd.version`
- `/private/var/staged_system_apps/Tips.app/kk.lproj/nlu.appintents/83e7a5f6a43899150c442d0fa6283881.version`
- `/private/var/staged_system_apps/Tips.app/kn.lproj/nlu.appintents/d47c85c189f956b3e5a40b65d489b470.version`
- `/private/var/staged_system_apps/Tips.app/ko.lproj/nlu.appintents/5578055fe567b329030cb3c46562830f.version`
- `/private/var/staged_system_apps/Tips.app/lt.lproj/nlu.appintents/d938a2b10365c6eb8070ab5e7658582c.version`
- `/private/var/staged_system_apps/Tips.app/ml.lproj/nlu.appintents/c506fbf66988ca3f6320de033c7e13ce.version`
- `/private/var/staged_system_apps/Tips.app/mr.lproj/nlu.appintents/24f3f7c46fb0ad2791138debc7ebe586.version`
- `/private/var/staged_system_apps/Tips.app/ms.lproj/nlu.appintents/ba3d927cedad8d6ea8a2d4308133978b.version`
- `/private/var/staged_system_apps/Tips.app/nl.lproj/nlu.appintents/bba646cd12c0715cdfd64d46495835f1.version`
- `/private/var/staged_system_apps/Tips.app/no.lproj/nlu.appintents/a4a03af13e6c2333376be5671b2cef55.version`
- `/private/var/staged_system_apps/Tips.app/or.lproj/nlu.appintents/504a8405a8f1ffbcfc54a72d950ff725.version`
- `/private/var/staged_system_apps/Tips.app/pa.lproj/nlu.appintents/a503a998601fe5ca2cd22472ef35619f.version`
- `/private/var/staged_system_apps/Tips.app/pl.lproj/nlu.appintents/7acb006fb9f3fcee7fbca32fb280d7cd.version`
- `/private/var/staged_system_apps/Tips.app/pt_BR.lproj/nlu.appintents/295817fac48e922568dfc36e5fefd6e7.version`
- `/private/var/staged_system_apps/Tips.app/ro.lproj/nlu.appintents/0f4dad1550148da254ea3642f23236aa.version`
- `/private/var/staged_system_apps/Tips.app/ru.lproj/nlu.appintents/b189956067b75d28e51eaea36a5eb244.version`
- `/private/var/staged_system_apps/Tips.app/sk.lproj/nlu.appintents/0675212b87dba2a7a5081009c7934889.version`
- `/private/var/staged_system_apps/Tips.app/sl.lproj/nlu.appintents/f83c48241060cdf1662854f8b3586ff8.version`
- `/private/var/staged_system_apps/Tips.app/sv.lproj/nlu.appintents/c8a452862ec4ae5400c2ae5a2ec9a58f.version`
- `/private/var/staged_system_apps/Tips.app/ta.lproj/nlu.appintents/f6c5233edb197990598de90451c054ca.version`
- `/private/var/staged_system_apps/Tips.app/th.lproj/nlu.appintents/b20c63fd793f458424379033db4ef91d.version`
- `/private/var/staged_system_apps/Tips.app/tr.lproj/nlu.appintents/8a8008dbdae601df4d18eddbd1ccf119.version`
- `/private/var/staged_system_apps/Tips.app/uk.lproj/nlu.appintents/6995939b2625f159e6bbbb6cf96a8046.version`
- `/private/var/staged_system_apps/Tips.app/ur.lproj/nlu.appintents/6dfa775e43f0f65d476064f25c649f6a.version`
- `/private/var/staged_system_apps/Tips.app/vi.lproj/nlu.appintents/a5babf8094454b27549ecf6942986785.version`
- `/private/var/staged_system_apps/Tips.app/zh_CN.lproj/nlu.appintents/375a00e6a4cdcb41e5a8f50d9de8fce4.version`
- `/private/var/staged_system_apps/Tips.app/zh_HK.lproj/nlu.appintents/23722c5e8985c29d78c8990a9e15a30d.version`
- `/private/var/staged_system_apps/Tips.app/zh_TW.lproj/nlu.appintents/20c76c172c7301df06b73579ad318cdd.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Base.lproj/nlu.appintents/4e5e049c991a5f0053d0a40ae5ce0df5.version`
- `/private/var/staged_system_apps/VoiceMemos.app/en.lproj/nlu.appintents/fbecab5bfe86c6283fa6b1158f7fc784.version`
- `/usr/libexec/fusiond`
- `/usr/share/firmware/bluetooth/BCM4399C2_22.5.157.701_PCIE_Cephalotus_CLPC_OS_STATS_20250214.bin`
- `/usr/share/firmware/bluetooth/BCM4399C2_22.5.157.702_PCIE_Cephalotus_CLPC_OS_USI_20250214.bin`

</details>

##### ExclaveOS (32)

<details>
  <summary><i>View Files</i></summary>

- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-AU/AssetData/galvatron_hsjs_v1_8bit_fp16_mil2bnns.mlmodelc.bnnsir`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-AU/AssetData/int8_conformer_matrix_split_exclave.mlmodelc.bnnsir`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-AU/AssetData/megatron_hsjs_8bit_compressed_v1_fp16_mil2bnns.mlmodelc.bnnsir`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-AU/AssetData/megatron_hsjs_8bit_compressed_v1_fp16_mil2bnns.mlmodelc.weights`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-AU/AssetData/rtblob_aop_1_2.bin`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-AU/AssetData/rtblob_aop_1_2.signature`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-GB/AssetData/galvatron_hsjs_v1_8bit_fp16_mil2bnns.mlmodelc.bnnsir`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-GB/AssetData/int8_conformer_matrix_split_exclave.mlmodelc.bnnsir`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-GB/AssetData/megatron_hsjs_8bit_compressed_v1_fp16_mil2bnns.mlmodelc.bnnsir`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-GB/AssetData/megatron_hsjs_8bit_compressed_v1_fp16_mil2bnns.mlmodelc.weights`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-GB/AssetData/rtblob_aop_1_2.bin`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-GB/AssetData/rtblob_aop_1_2.signature`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-IE/AssetData/galvatron_hsjs_v1_8bit_fp16_mil2bnns.mlmodelc.bnnsir`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-IE/AssetData/int8_conformer_matrix_split_exclave.mlmodelc.bnnsir`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-IE/AssetData/megatron_hsjs_8bit_compressed_v1_fp16_mil2bnns.mlmodelc.bnnsir`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-IE/AssetData/megatron_hsjs_8bit_compressed_v1_fp16_mil2bnns.mlmodelc.weights`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-IE/AssetData/rtblob_aop_1_2.bin`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-IE/AssetData/rtblob_aop_1_2.signature`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-US/AssetData/galvatron_hsjs_v1_8bit_fp16_mil2bnns.mlmodelc.bnnsir`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-US/AssetData/int8_conformer_matrix_split_exclave.mlmodelc.bnnsir`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-US/AssetData/megatron_hsjs_8bit_compressed_v1_fp16_mil2bnns.mlmodelc.bnnsir`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-US/AssetData/megatron_hsjs_8bit_compressed_v1_fp16_mil2bnns.mlmodelc.weights`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-US/AssetData/rtblob_aop_1_2.bin`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-US/AssetData/rtblob_aop_1_2.signature`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-ZA/AssetData/galvatron_hsjs_v1_8bit_fp16_mil2bnns.mlmodelc.bnnsir`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-ZA/AssetData/int8_conformer_matrix_split_exclave.mlmodelc.bnnsir`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-ZA/AssetData/megatron_hsjs_8bit_compressed_v1_fp16_mil2bnns.mlmodelc.bnnsir`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-ZA/AssetData/megatron_hsjs_8bit_compressed_v1_fp16_mil2bnns.mlmodelc.weights`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-ZA/AssetData/rtblob_aop_1_2.bin`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/en-ZA/AssetData/rtblob_aop_1_2.signature`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/vi-VN/AssetData/megatron_hsjs_8bit_compressed_v1_fp16_mil2bnns.mlmodelc.bnnsir`
- `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets_exclavekit.framework/H17/vi-VN/AssetData/megatron_hsjs_8bit_compressed_v1_fp16_mil2bnns.mlmodelc.weights`

</details>

## EOF
