## com.apple.plugin.IOgPTPPlugin

> `com.apple.plugin.IOgPTPPlugin`

```diff

-1450.2.0.0.0
-  __TEXT.__cstring: 0x7034
-  __TEXT.__os_log: 0x1c6f5
+1500.96.0.0.0
+  __TEXT.__cstring: 0x6bd6
+  __TEXT.__os_log: 0x1bd96
   __TEXT.__const: 0x2d2
-  __TEXT_EXEC.__text: 0x70a68
+  __TEXT_EXEC.__text: 0x6e43c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
-  __DATA.__common: 0x600
+  __DATA.__common: 0x5d8
   __DATA.__bss: 0xc8
-  __DATA_CONST.__auth_got: 0x790
-  __DATA_CONST.__got: 0x1c8
-  __DATA_CONST.__mod_init_func: 0x118
-  __DATA_CONST.__mod_term_func: 0x118
-  __DATA_CONST.__const: 0xf168
-  __DATA_CONST.__kalloc_type: 0x9c0
-  __DATA_CONST.__kalloc_var: 0x280
-  UUID: 8CF88242-7B0B-3000-A401-C5142CE1045D
-  Functions: 1664
+  __DATA_CONST.__mod_init_func: 0x110
+  __DATA_CONST.__mod_term_func: 0x110
+  __DATA_CONST.__const: 0xea70
+  __DATA_CONST.__kalloc_type: 0x980
+  __DATA_CONST.__auth_got: 0x718
+  __DATA_CONST.__got: 0x1b0
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
