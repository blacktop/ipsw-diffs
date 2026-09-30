## ansf.t8140_largemem.release.im4p

> `Firmware/ansf.t8140_largemem.release.im4p`

```diff

   __TEXT.text_first: 0x45a0
-  __TEXT.__text: 0x1e69dc
-  __TEXT.shared: 0xde10
-  __TEXT.read: 0x7320
+  __TEXT.__text: 0x1e6cc0
+  __TEXT.shared: 0xde0c
+  __TEXT.read: 0x7350
   __TEXT.__const: 0x58d8
-  __TEXT.__cstring: 0x24d69
+  __TEXT.__cstring: 0x24d58
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x1c
   __DATA._rtk_boot: 0x8000

   __DATA._rtk_patchbay: 0x3f4
   __DATA._rtk_tunables: 0x6a0
   __DATA._rtk_mtab: 0x310
-  __DATA.__data: 0x7010
+  __DATA.__data: 0x7000
   __DATA.__const: 0x23e8
   __DATA.__gxf_data: 0x10
   __DATA.core_globals: 0x162

   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0x3549d8
+  __DATA.__zerofill: 0x356518
   Functions: 1969
   Symbols:   0
   CStrings:  3957
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__chain_starts : content changed
~ __DATA._rtk_patchbay : content changed
~ __DATA._rtk_mtab : content changed
~ __DATA.__const : content changed
CStrings:
+ "236"
+ "236~187"
+ "AppleStorageFirmwareASP3-236~187"
+ "Sanitize drop - device in shutdown"
+ "T : Timestamp\nP : Percent Cmd_DoPreempt\nWL:\n Ops p 0/1/2/3\n SumLatency p 0/1/2/3\n MaxLatency p0/1/2/3\nRL:\n Ops p 0/1/2/3\n SumLatency p 0/1/2/3\n MaxLatency p0/1/2/3\nE: Block Erases\nF: Host Flushes\nHR: Host Reads\nHW: Host Writes\nNR: Nand Reads\nNW: Nand Writes\nNUR: Nand Util Reads\nNUW: Nand Util Writes\nCW: Clog Writes\nIW: Ind Writes\nGC: GC Writes\nSoMx: Maximal number of stepovers per host bandsBND: Minimal number of stepovers per host band\nSoAvg: Average number of stepovers per host band\nHPMM: Maximal number of ASI commands per MSPPR: Prefetch Reads\nPH: Prefetch Hits\nPN: Prefetch fetch next ranges\nAW: Writes that were handled by autowrite HW\nWCD: Write cache dirty percentage\nWCFB: Write cache free buffers percentage\nW : Wear Level Bands\nBI: BLKS(SLC)\nBU: BLKS(MLC/TLC)\nBL: BLKS LVL\nTH: Time in Hysteresis (ms)\nS : Free Segs\nV : IndMem Free\nML: IND_Mem_GetFreeSpace output in percents\nX : Expedite Ok/Fail\nU : Host unmaps\nCmin : Host tags(Min)\nCmax : Host tags(Max)\nBGT: Background task time(us)\nUT: Update Time(us)\nNU: Updated fragmets in indirection\nST: Search Time(us)\nGMT: GC Move Time(us)\nGDF: GC Defrag Time(us)\nNS: Searches\nMB: Cache/Ind MBUs\nIMM: Time Spent in Immediate Cmd (us)\nLHS: Ldefrag host sectors read\nLTS: Ldefrag troll sectors read\nLHF: Ldefrag host fragments read\nLTF: Ldefrag troll fragments read\nCCMB: Segs that were combined on cache level, often after troll read\nWCMB: Segs that were combined on writtenQ level, often after buffer fragmentation\nFDOW: Freagments decrease in indirection, zero if increased\nEX: Extra senses in MSP may slow read perf\nNWSM: Nand writes in SLC mode\nNRSM: Nand reads in SLC mode\nNWTM: Nand writes in TLC mode\nNRTM: Nand reads in TLC mode\nPSRD: Parity subtract reads\nRDS: Sectors read due to RD sampler\nTP: Total padding count\nIP: Immediate padding count\nTEMP: max temperature of all msps\nUPR: Unaligned Page Reads\nNWQM: Nand writes in FNC mode\nNRQM: Nand reads in FNC mode\nGCFQ: Force FNC for GC\nTi: IndMem #free tilesDT: delta for +freeTile/-freeTileMTH: IndMem total used mix/highest used mix\nGCS: GC SRC InfoWA: write amplificationGRK: GC src_rk_firstGCST: GC stateGCAD: GC average durationGCMT: GC MustList TopGHCO: GC Host choke offsetGCD: GC DST InfoGM: count GC must bands\nUE num ueccs from nand this time period\nGB: total number GBBs\nRH: total number host reconstructions\nRI: total internal reconstruction\nRR: raid sector reads this period\nOBC: Offline blocks count\nDTB: Dir to TLC bands\nRHM: Raid cache HW miss sectors\nRHM: Raid cache HR miss sectors\nBo: oSLC bands\noSLC SM on stateoSLC voters stateREWS: Raid evict engine write sectors\nRFRS: Raid fetch engine read sectors\nADFH:  AES Write Data Beat received from F2H\nADHF: AES Write Data Beat received from H2F\nVBWR: Num Write Data beats rcvd from Vlane\nVBRR: Num Read Data beats sent to Vlane\nCFDWC: Num Write Data beats rcvd from ANS2 CPU\nCFDRC: Num Read Data beats sent to ANS2 CPU\nDLWD: Num Write Data beats rcvd from apcie_0_m\nDLRD: Num Read Data beats sent to apcie_0_m\nUWDF: Num Write Data Beats rcvd from Data Fabric\nURDF: Num Read Data beats sent to Data Fabric\nDPQBI: Num Barriers pushed into Dispatch Queue\nDPQBO: Num Barriers sent out from Dispatch Queue\n"
+ "UPR=%5u "
+ "mark invalid band %u S %u"
+ "mark valid band %u M %u"
- "222.0.0.0.1"
- "222.0.0.0.1~31"
- "AppleStorageFirmwareASP3-222.0.0.0.1~31"
- "Disabling band orphans - no band"
- "T : Timestamp\nP : Percent Cmd_DoPreempt\nWL:\n Ops p 0/1/2/3\n SumLatency p 0/1/2/3\n MaxLatency p0/1/2/3\nRL:\n Ops p 0/1/2/3\n SumLatency p 0/1/2/3\n MaxLatency p0/1/2/3\nE: Block Erases\nF: Host Flushes\nHR: Host Reads\nHW: Host Writes\nNR: Nand Reads\nNW: Nand Writes\nNUR: Nand Util Reads\nNUW: Nand Util Writes\nCW: Clog Writes\nIW: Ind Writes\nGC: GC Writes\nSoMx: Maximal number of stepovers per host bandsBND: Minimal number of stepovers per host band\nSoAvg: Average number of stepovers per host band\nHPMM: Maximal number of ASI commands per MSPPR: Prefetch Reads\nPH: Prefetch Hits\nPN: Prefetch fetch next ranges\nAW: Writes that were handled by autowrite HW\nWCD: Write cache dirty percentage\nWCFB: Write cache free buffers percentage\nW : Wear Level Bands\nBI: BLKS(SLC)\nBU: BLKS(MLC/TLC)\nBL: BLKS LVL\nTH: Time in Hysteresis (ms)\nS : Free Segs\nV : IndMem Free\nML: IND_Mem_GetFreeSpace output in percents\nX : Expedite Ok/Fail\nU : Host unmaps\nCmin : Host tags(Min)\nCmax : Host tags(Max)\nBGT: Background task time(us)\nUT: Update Time(us)\nNU: Updated fragmets in indirection\nST: Search Time(us)\nGMT: GC Move Time(us)\nGDF: GC Defrag Time(us)\nNS: Searches\nMB: Cache/Ind MBUs\nIMM: Time Spent in Immediate Cmd (us)\nLHS: Ldefrag host sectors read\nLTS: Ldefrag troll sectors read\nLHF: Ldefrag host fragments read\nLTF: Ldefrag troll fragments read\nCCMB: Segs that were combined on cache level, often after troll read\nWCMB: Segs that were combined on writtenQ level, often after buffer fragmentation\nFDOW: Freagments decrease in indirection, zero if increased\nEX: Extra senses in MSP may slow read perf\nNWSM: Nand writes in SLC mode\nNRSM: Nand reads in SLC mode\nNWTM: Nand writes in TLC mode\nNRTM: Nand reads in TLC mode\nPSRD: Parity subtract reads\nRDS: Sectors read due to RD sampler\nTP: Total padding count\nIP: Immediate padding count\nTEMP: max temperature of all msps\nNWQM: Nand writes in FNC mode\nNRQM: Nand reads in FNC mode\nGCFQ: Force FNC for GC\nTi: IndMem #free tilesDT: delta for +freeTile/-freeTileMTH: IndMem total used mix/highest used mix\nGCS: GC SRC InfoWA: write amplificationGRK: GC src_rk_firstGCST: GC stateGCAD: GC average durationGCMT: GC MustList TopGHCO: GC Host choke offsetGCD: GC DST InfoGM: count GC must bands\nUE num ueccs from nand this time period\nGB: total number GBBs\nRH: total number host reconstructions\nRI: total internal reconstruction\nRR: raid sector reads this period\nOBC: Offline blocks count\nDTB: Dir to TLC bands\nRHM: Raid cache HW miss sectors\nRHM: Raid cache HR miss sectors\nBo: oSLC bands\noSLC SM on stateoSLC voters stateREWS: Raid evict engine write sectors\nRFRS: Raid fetch engine read sectors\nADFH:  AES Write Data Beat received from F2H\nADHF: AES Write Data Beat received from H2F\nVBWR: Num Write Data beats rcvd from Vlane\nVBRR: Num Read Data beats sent to Vlane\nCFDWC: Num Write Data beats rcvd from ANS2 CPU\nCFDRC: Num Read Data beats sent to ANS2 CPU\nDLWD: Num Write Data beats rcvd from apcie_0_m\nDLRD: Num Read Data beats sent to apcie_0_m\nUWDF: Num Write Data Beats rcvd from Data Fabric\nURDF: Num Read Data beats sent to Data Fabric\nDPQBI: Num Barriers pushed into Dispatch Queue\nDPQBO: Num Barriers sent out from Dispatch Queue\n"
- "mark band %u"
- "mark band %u, isOpen %u"
- "must have valid max temperature for band: %d"

```
