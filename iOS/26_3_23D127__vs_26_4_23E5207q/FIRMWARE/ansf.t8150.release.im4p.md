## ansf.t8150.release.im4p

> `ansf.t8150.release.im4p`

```diff

 
-  __TEXT.text_first: 0x4568
-  __TEXT.__text: 0x1e161c
-  __TEXT.shared: 0xe374
-  __TEXT.read: 0x71d8
-  __TEXT.__const: 0x57b8
-  __TEXT.__cstring: 0x2469a
+  __TEXT.text_first: 0x45b8
+  __TEXT.__text: 0x1e39a4
+  __TEXT.shared: 0xe10c
+  __TEXT.read: 0x7094
+  __TEXT.__const: 0x5948
+  __TEXT.__cstring: 0x24b8c
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x20
   __DATA._rtk_boot: 0x8000
   __DATA._rtk_power: 0x1b0
   __DATA._rtk_patchbay: 0x474
   __DATA._rtk_tunables: 0x6a0
-  __DATA.__const: 0x1b98
   __DATA._rtk_mtab: 0x380
-  __DATA.__data: 0x5b58
+  __DATA.__data: 0x5b68
+  __DATA.__const: 0x1a40
   __DATA.__gxf_data: 0x10
   __DATA.core_globals: 0x167
   __DATA._rtk_init_stack: 0x1000

   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0x2a43a8
+  __DATA.__zerofill: 0x2a50a8
   UUID: 
-  Functions: 1977
+  Functions: 1994
   Symbols:   0
-  CStrings:  3960
+  CStrings:  3977
 
CStrings:
+ "!!!! Aborting paniclog write, no block"
+ "!!!! Failed to erase paniclog block, subsequent writes will fail"
+ "!BGRefresh.massScan.isScanActive"
+ "2973.100.300"
+ "2973.100.300~67"
+ "AppleStorageFirmware-2973.100.300~67"
+ "Block scan result aborted."
+ "CORE_DEBUG_SET_LBA_RD_COUNT: RD value set SUCCESS %u"
+ "CORE_DEBUG_SET_LBA_RD_COUNT: band: %u, boff: %u, dip: %u"
+ "CORE_DEBUG_SET_LBA_RD_COUNT: invalid LBA %u"
+ "CORE_DEBUG_SET_LBA_RD_COUNT: invalid RD_POS"
+ "CORE_DEBUG_SET_LBA_RD_COUNT: lba: %u, new_value: %u"
+ "Cmd_tunnelGetNandMaturity - Error - no tunnel buffer"
+ "DESC:: NI:%d CC:0x%x"
+ "Disabling band orphans - no band"
+ "Disabling band orphans for shutdown or fmt"
+ "EAN flush and WC flush deadlocked?"
+ "Eye_Scan (S6E): Unsupported EyeScan type, %d."
+ "FTL buffer Alocation Error!"
+ "FW Flush in progress: 0x%x\n"
+ "Flush evict finished but still have some segs in dirtyQ"
+ "Invalid write to IOLog"
+ "LOG: entries sz >= coalescer sz (%zu >= %zu)"
+ "MD Memory Violation"
+ "MassScan detected failure on band %d, total %d failed bands during this scan"
+ "MassScan done after %lld seconds, scanned %d bands, found %d failures"
+ "Possible special case of unclean due to partial band:%d cycle:%d from previous clog bump. Max Cycle at bump:%d "
+ "Possible special case of unclean due to partial block:%d cycle:%d from previous clog bump. Max Cycle at bump:%d"
+ "QoS assert while device in thermal throttling and NRP mode: tag %u duration %u ms > qos timeout %u ms"
+ "QoS assert while device in thermal throttling: tag %u duration %u ms > qos timeout %u ms"
+ "Read is blocked due to autowrite (read segIdx:%d, autowrite segIdx:%d"
+ "S=%5u "
+ "SoAvg=%6u "
+ "Staying in rel branch because %d GCmust and %d bandsFoundInScan still exist"
+ "T : Timestamp\nP : Percent Cmd_DoPreempt\nWL:\n Ops p 0/1/2/3\n SumLatency p 0/1/2/3\n MaxLatency p0/1/2/3\nRL:\n Ops p 0/1/2/3\n SumLatency p 0/1/2/3\n MaxLatency p0/1/2/3\nE: Block Erases\nF: Host Flushes\nHR: Host Reads\nHW: Host Writes\nNR: Nand Reads\nNW: Nand Writes\nNUR: Nand Util Reads\nNUW: Nand Util Writes\nCW: Clog Writes\nIW: Ind Writes\nGC: GC Writes\nSoMx: Maximal number of stepovers per host bandsBND: Minimal number of stepovers per host band\nSoAvg: Average number of stepovers per host band\nHPMM: Maximal number of ASI commands per MSPPR: Prefetch Reads\nPH: Prefetch Hits\nPN: Prefetch fetch next ranges\nAW: Writes that were handled by autowrite HW\nWCD: Write cache dirty percentage\nWCFB: Write cache free buffers percentage\nW : Wear Level Bands\nBI: BLKS(SLC)\nBU: BLKS(MLC/TLC)\nBL: BLKS LVL\nTH: Time in Hysteresis (ms)\nS : Free Segs\nV : IndMem Free\nML: IND_Mem_GetFreeSpace output in percents\nX : Expedite Ok/Fail\nU : Host unmaps\nCmin : Host tags(Min)\nCmax : Host tags(Max)\nBGT: Background task time(us)\nUT: Update Time(us)\nNU: Updates\nST: Search Time(us)\nGMT: GC Move Time(us)\nGDF: GC Defrag Time(us)\nNS: Searches\nMB: Cache/Ind MBUs\nIMM: Time Spent in Immediate Cmd (us)\nLHS: Ldefrag host sectors read\nLTS: Ldefrag troll sectors read\nLHF: Ldefrag host fragments read\nLTF: Ldefrag troll fragments read\nCCMB: Segs that were combined on cache level, often after troll read\nWCMB: Segs that were combined on writtenQ level, often after buffer fragmentation\nFDOW: Freagments decrease in indirection, zero if increased\nEX: Extra senses in MSP may slow read perf\nNWSM: Nand writes in SLC mode\nNRSM: Nand reads in SLC mode\nNWTM: Nand writes in TLC mode\nNRTM: Nand reads in TLC mode\nPSRD: Parity subtract reads\nRDS: Sectors read due to RD sampler\nTP: Total padding count\nIP: Immediate padding count\nTEMP: max temperature of all msps\nNWQM: Nand writes in FNC mode\nNRQM: Nand reads in FNC mode\nGCFQ: Force FNC for GC\nTi: IndMem #free tilesDT: delta for +freeTile/-freeTileMTH: IndMem total used mix/highest used mix\nGCS: GC SRC InfoWA: write amplificationGRK: GC src_rk_firstGCST: GC stateGCMT: GC MustList TopGHCO: GC Host choke offsetGCD: GC DST InfoGM: count GC must bands\nUE num ueccs from nand this time period\nGB: total number GBBs\nRH: total number host reconstructions\nRI: total internal reconstruction\nRR: raid sector reads this period\nOBC: Offline blocks count\nDTB: Dir to TLC bands\nRHM: Raid cache HW miss sectors\nRHM: Raid cache HR miss sectors\nBo: oSLC bands\noSLC SM on stateoSLC voters stateREWS: Raid evict engine write sectors\nRFRS: Raid fetch engine read sectors\nADFH:  AES Write Data Beat received from F2H\nADHF: AES Write Data Beat received from H2F\nVBWR: Num Write Data beats rcvd from Vlane\nVBRR: Num Read Data beats sent to Vlane\nCFDWC: Num Write Data beats rcvd from ANS2 CPU\nCFDRC: Num Read Data beats sent to ANS2 CPU\nDLWD: Num Write Data beats rcvd from apcie_0_m\nDLRD: Num Read Data beats sent to apcie_0_m\nUWDF: Num Write Data Beats rcvd from Data Fabric\nURDF: Num Read Data beats sent to Data Fabric\nDPQBI: Num Barriers pushed into Dispatch Queue\nDPQBO: Num Barriers sent out from Dispatch Queue\nTT Read levelTT Prog level"
+ "read seg %d prio:%d (tag %d) is blocked"
+ "seg gens out of order in writtenQ"
+ "source band %u gained validity during GC %u %u"
+ "starting MassScan, request from MSP %d, earlyExitAllowed: %d, trying to scan %d bands in this iteration"
- "2914.80.130"
- "2914.80.130~99"
- "AppleStorageFirmware-2914.80.130~99"
- "Calling Ind_get_seq_lba with LBA: %d, size: %d"
- "Failed to properly defrag GC buffers after %u iterations"
- "First retry boff %u band %u flow %u"
- "LOG: entries sz > coalescer sz (%zu > %zu)"
- "MassScan done after %lld seconds"
- "S=%4u "
- "SetDiesInParallel for abacus %d, to %d"
- "Staying in rel branch because %d GCmust bands still exist"
- "T : Timestamp\nP : Percent Cmd_DoPreempt\nWL:\n Ops p 0/1/2/3\n SumLatency p 0/1/2/3\n MaxLatency p0/1/2/3\nRL:\n Ops p 0/1/2/3\n SumLatency p 0/1/2/3\n MaxLatency p0/1/2/3\nE: Block Erases\nF: Host Flushes\nHR: Host Reads\nHW: Host Writes\nNR: Nand Reads\nNW: Nand Writes\nNUR: Nand Util Reads\nNUW: Nand Util Writes\nCW: Clog Writes\nIW: Ind Writes\nGC: GC Writes\nSoMx: Maximal number of stepovers per host bandsBND: Minimal number of stepovers per host band\nHPMM: Maximal number of ASI commands per MSPPR: Prefetch Reads\nPH: Prefetch Hits\nPN: Prefetch fetch next ranges\nAW: Writes that were handled by autowrite HW\nWCD: Write cache dirty percentage\nWCFB: Write cache free buffers percentage\nW : Wear Level Bands\nBI: BLKS(SLC)\nBU: BLKS(MLC/TLC)\nBL: BLKS LVL\nTH: Time in Hysteresis (ms)\nS : Free Segs\nV : IndMem Free\nML: IND_Mem_GetFreeSpace output in percents\nX : Expedite Ok/Fail\nU : Host unmaps\nCmin : Host tags(Min)\nCmax : Host tags(Max)\nBGT: Background task time(us)\nUT: Update Time(us)\nNU: Updates\nST: Search Time(us)\nGMT: GC Move Time(us)\nGDF: GC Defrag Time(us)\nNS: Searches\nMB: Cache/Ind MBUs\nIMM: Time Spent in Immediate Cmd (us)\nLHS: Ldefrag host sectors read\nLTS: Ldefrag troll sectors read\nLHF: Ldefrag host fragments read\nLTF: Ldefrag troll fragments read\nCCMB: Segs that were combined on cache level, often after troll read\nWCMB: Segs that were combined on writtenQ level, often after buffer fragmentation\nFDOW: Freagments decrease in indirection, zero if increased\nEX: Extra senses in MSP may slow read perf\nNWSM: Nand writes in SLC mode\nNRSM: Nand reads in SLC mode\nNWTM: Nand writes in TLC mode\nNRTM: Nand reads in TLC mode\nPSRD: Parity subtract reads\nRDS: Sectors read due to RD sampler\nTP: Total padding count\nIP: Immediate padding count\nTEMP: max temperature of all msps\nNWQM: Nand writes in FNC mode\nNRQM: Nand reads in FNC mode\nGCFQ: Force FNC for GC\nTi: IndMem #free tilesDT: delta for +freeTile/-freeTileMTH: IndMem total used mix/highest used mix\nGCS: GC SRC InfoWA: write amplificationGRK: GC src_rk_firstGCST: GC stateGCMT: GC MustList TopGHCO: GC Host choke offsetGCD: GC DST InfoGM: count GC must bands\nUE num ueccs from nand this time period\nGB: total number GBBs\nRH: total number host reconstructions\nRI: total internal reconstruction\nRR: raid sector reads this period\nOBC: Offline blocks count\nDTB: Dir to TLC bands\nRHM: Raid cache HW miss sectors\nRHM: Raid cache HR miss sectors\nBo: oSLC bands\noSLC SM on stateoSLC voters stateREWS: Raid evict engine write sectors\nRFRS: Raid fetch engine read sectors\nADFH:  AES Write Data Beat received from F2H\nADHF: AES Write Data Beat received from H2F\nVBWR: Num Write Data beats rcvd from Vlane\nVBRR: Num Read Data beats sent to Vlane\nCFDWC: Num Write Data beats rcvd from ANS2 CPU\nCFDRC: Num Read Data beats sent to ANS2 CPU\nDLWD: Num Write Data beats rcvd from apcie_0_m\nDLRD: Num Read Data beats sent to apcie_0_m\nUWDF: Num Write Data Beats rcvd from Data Fabric\nURDF: Num Read Data beats sent to Data Fabric\nDPQBI: Num Barriers pushed into Dispatch Queue\nDPQBO: Num Barriers sent out from Dispatch Queue\nTT Read levelTT Prog level"
- "Total cuts in this sequence: %d and %d bands"
- "abacus_engine_v2.c"
- "fifoNumElems: %d"
- "fifoSize: %d"
- "idx %u, max %u"
- "mismatch %d >= %d"
- "must be page without Clog"
- "off %u"
- "source band %u gained validity during GC"
- "starting MassScan, request from MSP %d, earlyExitAllowed: %d"

```
