## com.apple.plugin.IOgPTPPlugin

> `com.apple.plugin.IOgPTPPlugin`

```diff

-1450.2.0.0.0
-  __TEXT.__cstring: 0x7034 sha256:091e509b016146e606a0526c9873e984a4c773645f7de102241b3c6c7c002ade
-  __TEXT.__os_log: 0x1c6f5 sha256:5adf93310e5cf80e610a333d92dbe5ae2f82031ddff88db105f1e3299a4a3a0c
+1500.96.0.0.0
+  __TEXT.__cstring: 0x6bd6 sha256:3afb6554d9a8c4982f5acc3b34577f46d9429fde6d2d74dbf2d0cc69b43c1723
+  __TEXT.__os_log: 0x1bd96 sha256:c2e6670fc1bd0082e05e3d3a0e2453728cb3fd827fd11232351633985e0f234f
   __TEXT.__const: 0x2d2 sha256:88e1b7b6082434d3f4b5cb85443c8b916080e932481bed8ca396701badec81fa
-  __TEXT_EXEC.__text: 0x70a68 sha256:f7394199b9e6b57d60bbdd86c7afe90de6d29bf4996bc516b00c3830045ecb65
+  __TEXT_EXEC.__text: 0x6e43c sha256:5de02a50e15cb83b7e21def12b49fb05b1921192ede6941a27659d164cbdb0af
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xc8 sha256:d9fcf513d0c2e751eb31dc5b68344e3ab678c7439722e32882c3a86c657d1dcb
-  __DATA.__common: 0x600 sha256:80422bc3d307b4a25bdafcc84ac7fb01cb55a09810e8b0f37bb12e0edb5c48ca
+  __DATA.__data: 0xc8 sha256:4004698b182e137221007144f1c15ee3711275d75d03a32d368e392913d90c33
+  __DATA.__common: 0x5d8 sha256:2010b55891b05a55428204b4cc0e2d03cd13f0727289c1bda6dc6d8935538218
   __DATA.__bss: 0xc8 sha256:6d9c54dee5660c46886f32d80e57e9dd0ffa57ee0cd2a762b036d9c8e0c3a33a
-  __DATA_CONST.__auth_got: 0x790 sha256:d2d3b1e8d277d1c6dc57b9a18246e25f77d4abc4eee3be280f319a80cacfa471
-  __DATA_CONST.__got: 0x1c8 sha256:3da43610174296c1adb70a04fadb22cf2b7eb0d10875d9456cf9c62030424962
-  __DATA_CONST.__mod_init_func: 0x118 sha256:443ac2647f770d6aa70bc19b67ee4c6e4717700bce6f43f413d8bf8367d80465
-  __DATA_CONST.__mod_term_func: 0x118 sha256:f9d67b58bab1ce9c0bd649ce543045e1e227acff6decd2ab96100342865f43c9
-  __DATA_CONST.__const: 0xf168 sha256:93650a2d25ba66c3b8d18d7205aec63e73dc685efee0109f4e294307ad995a96
-  __DATA_CONST.__kalloc_type: 0x9c0 sha256:a8e3ff836fe7595e73f18e59e90f8814dd164ab9a139ee21874189ced888a58e
-  __DATA_CONST.__kalloc_var: 0x280 sha256:d287682eec7afc2533e2a0a5025ad04308f9a8dbd06584b826951e69be7b27b0
-  UUID: 8CF88242-7B0B-3000-A401-C5142CE1045D
-  Functions: 1664
+  __DATA_CONST.__mod_init_func: 0x110 sha256:febc2016313a67b190628b44d90be62d7b395a783858b7cdbaa3effc43cc9ec7
+  __DATA_CONST.__mod_term_func: 0x110 sha256:69551ec58995dd7b43c79e3344bd1c3afab4af9560e07b57584b62e775b339e2
+  __DATA_CONST.__const: 0xea70 sha256:5dd507b390555732a13ee5ef90ff9d415faa58611b729589e80369ac5cdae7fc
+  __DATA_CONST.__kalloc_type: 0x980 sha256:3cf49a2fec065e527dc89951d1a1b9040d667ffcfdf1af4e87d3f8fe01ff369a
+  __DATA_CONST.__auth_got: 0x718 sha256:7e54b738ddf74b04eb8d52f3913aa391394ab68f826713d6e623483733b32e9a
+  __DATA_CONST.__got: 0x1b0 sha256:49493d716773acd4e53223325f6d8092e108a8eba0dfb39a32d43c91388d870f
+  UUID: FCC6B92B-4641-357C-AAF3-CE27119569A6
+  Functions: 1633
   Symbols:   0
-  CStrings:  1589
+  CStrings:  1534
 
CStrings:
+ "12111112122212121111211111122111111111111111111111122222222222221222222222222222222222222222222222222222222222222222222222211111111111111111111111111112222222"
+ "Failed userIDStr allocation\n"
+ "IOTimeSyncLocalClockPort::attach frequency info: toleranceLower=%d(%d) toleranceUpper=%d(%d) stabilityLower=%d(%d) stabilityUpper=%d(%d) oscillatorType=%u\n"
+ "IOTimeSyncgPTPManager::init timesync node frequency info: toleranceLower=%d(%d) toleranceUpper=%d(%d) stabilityLower=%d(%d) stabilityUpper=%d(%d) oscillatorType=%u\n"
+ "NULL == userIDStr"
- "  %s(%s): #####fTransmitPacketLatency %llu fTransmitDMAOffset %llu\n"
- "  %s(%s): $$$$$$------ Successfully started transmit thread\n"
- "  %s(%s): $$$$$$------ Waiting for transmit thread start\n"
- "  %s(%s): @@@@@fTransmitNICPacketLatency %llu fTransmitNICFetchDelay %llu\n"
- "  %s(%s): Failed to convert transmit thread to realtime. Error 0x%08x\n"
- "  %s(%s): Flushing queue %u write head %u read head %u\n"
- "  %s(%s): Rejecting attempt to set preferred GM on domain %#llx of type %u"
- "$$$$$$------ Stopping transmit thread\n"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/TimeSync_kext/IOgPTPPlugin/IOTimeSyncEthernetSoftDMAInterfaceAdapater.cpp"
- "1"
- "1122"
- "121111121222121211111111122111111111111111111111122222222222221222222222222222222222222222222222222222222222222222222222211111111111111111111111111112222222"
- "121111121222121211112222111111211111211212112212121112111121112222"
- "21212121222222222222111111"
- "AppleEthernetBroadcomCaesar"
- "BCM5701Enet"
- "Could not allocate packet array\n"
- "Could not create Uncopied fill pattern\n"
- "Could not get number of transmit queues, Error: %d (0x%X)\n"
- "Error starting transmit thread, Error: %d (0x%X)\n"
- "Failed to allocate DMA ring\n"
- "Failed to allocate DMA ring pointers\n"
- "Failed to allocate NIC fetch delay\n"
- "Failed to allocate NIC packet latency\n"
- "Failed to allocate dma offsets\n"
- "Failed to allocate packet latency\n"
- "Failed to allocate read heads\n"
- "Failed to allocate write heads\n"
- "Failed to create DMA command for stream headers\n"
- "Failed to create buffer memory descriptor for stream headers\n"
- "Failed to create transmit thread\n"
- "Failed to set buffer descrptior 0x%08x, Error: %d (0x%X)\n"
- "IOTimeSyncEthernetSoftDMAInterfaceAdapter"
- "Must have at least one transmit queus\n"
- "NULL == fPacketDMACommand"
- "NULL == fPacketDescriptor"
- "NULL == fPackets"
- "NULL == fTransmitDMAOffset"
- "NULL == fTransmitNICFetchDelay"
- "NULL == fTransmitNICPacketLatency"
- "NULL == fTransmitPacketLatency"
- "NULL == fTransmitRing"
- "NULL == fTransmitRingReadHead"
- "NULL == fTransmitRingWriteHead"
- "NULL == fTransmitRing[index]"
- "NULL == fTransmitThread"
- "NULL == fUncopiedPattern"
- "SoftDMA-%s"
- "SoftDMA-Unknown"
- "could not create start semaphore\n"
- "could not create stop semaphore\n"
- "fTransmitRingCount == 0"
- "kIOReturnSuccess != semaphore_create(kernel_task, &fTransmitStartSemaphore, SYNC_POLICY_FIFO, 0)"
- "kIOReturnSuccess != semaphore_create(kernel_task, &fTransmitStopSemaphore, SYNC_POLICY_FIFO, 0)"
- "model"
- "site.IOEthernetController::IOEthernetAVBPacket"
- "site.IOTSESDIATransmitRingEntry"
- "site.IOTSESDIATransmitRingEntry *"
- "site.IOTimeSyncEthernetSoftDMAInterfaceAdapter"
- "timesync_softdma"

```
