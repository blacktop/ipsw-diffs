## rans.t8140.release.im4p

> `rans.t8140.release.im4p`

```diff

 
   __TEXT.text_first: 0x4488
-  __TEXT.__text: 0x1b4f18
-  __TEXT.shared: 0xd37c
-  __TEXT.read: 0x65c4
-  __TEXT.__const: 0x53c8
+  __TEXT.__text: 0x1c1250
+  __TEXT.shared: 0xd90c
+  __TEXT.read: 0x6b18
+  __TEXT.__const: 0x52a8
   __TEXT.idle_hooks: 0x10
-  __TEXT.__cstring: 0x2124e
+  __TEXT.__cstring: 0x223f7
   __TEXT.__chain_starts: 0x0
   __TEXT.__constructor: 0x0
   __TEXT._rtk_mtab: 0x310
   __DATA._rtk_boot: 0x8000
   __DATA._rtk_power: 0x160
-  __DATA._rtk_patchbay: 0x3c7
+  __DATA._rtk_patchbay: 0x3f3
   __DATA._rtk_tunables: 0x6a0
-  __DATA.__const: 0x1bb8
-  __DATA.__data: 0x5ff0
+  __DATA.__const: 0x1a48
+  __DATA.__data: 0x6008
   __DATA._rtk_init_stack: 0x1000
   __DATA._rtk_irq_stack: 0x1000
   __DATA._rtk_exc_stack: 0x1000

   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__mod_init_func: 0x0
-  __DATA.core_globals: 0x154
+  __DATA.core_globals: 0x156
   __DATA.large_stacks: 0x20000
   __DATA.small_stacks: 0x2000
-  __DATA.__zerofill: 0x2315b8
+  __DATA.__zerofill: 0x2461f8
   Functions: 0
   Symbols:   0
-  CStrings:  3648
+  CStrings:  3757
 
CStrings:
+ "\nInd_MC %d  Ind_C %d\n"
+ "\nMSP FW Params Version: 0x%x\n"
+ "\nMSP PHY FW Version: %s\n"
+ "      : 0x%02X 0x%02X 0x%02X 0x%02X 0x%02X 0x%02X 0x%02X 0x%02X"
+ " Bands_RefreshWorstETBand -> %ums"
+ "%d\t"
+ "%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t"
+ "%s\t"
+ "%s Flow %d Num %d\n"
+ "%s%s%s%s%s%s\n"
+ ".100.345.0.1~285"
+ "2077.100.345.0.1"
+ "Abacuses, mode %d err %d wake %d\n"
+ "AppleStorageFirmware-2077.100.345.0.1~285"
+ "Async cmd set asi_log_ctx_arr[%d].seg_ctx_idx from %d to %d"
+ "At least of the scan types should've been requested"
+ "BDR AF: 0x%02X 0x%02X 0x%02X 0x%02X 0x%02X 0x%02X 0x%02X 0x%02X"
+ "BDR HP AF %u exceeds maximum allowed %u"
+ "BDR cross temp init"
+ "BDR-AF table ignored, s6eTunnel %d bcmTunnel %d featureBit %d workMode %d"
+ "BG_TODO_SET(BG.todo.findET) was called when host is idle"
+ "BMX"
+ "CBDR Algo Tables values: HP SOL %u EOL %u | scan rate SOL %u EOL %u"
+ "Cmax=%3u "
+ "Cmin=%3u"
+ "Command to set CBDR HP ac. factor %u -> %u"
+ "Completion error for nandOp %u (segIdx %u, compl msg 0x%llx 0x%llx)"
+ "Controller"
+ "DC table ignored, s6eTunnel %d bcmTunnel %d featureBit %d workMode %d"
+ "DCTable v=%d, rc=%d, fbm=%d, "
+ "Deallocate NS: %s"
+ "Drive Index does not exist"
+ "ERR: async message buffer should be init"
+ "ERROR - No Tunnel Buffer"
+ "ERROR - Not enough buffer. Needed: %u, Available: %u"
+ "ERROR - Tunnel buffer size not in correct size range. Must be >= %u and <= %u. Received: %u"
+ "ERROR injection is not supported for S6E yet."
+ "ERROR! Nand Discovery not completed"
+ "Erase\n"
+ "Extent Count %u, Extents Processed %u, Frags Count %u\n"
+ "Failed to erase band %u (%u)"
+ "Failed to generate async message %u"
+ "GCST=%2u"
+ "GC_isInactive()"
+ "GHCO=%4u"
+ "HBJ=%10d "
+ "HPMM=%2u "
+ "I"
+ "INFO - Out of output buffer space"
+ "MSP %d already requested scan?"
+ "MSP%u"
+ "Maintaince done. reset DB"
+ "Mass scan is active"
+ "MassScan done"
+ "MassScan done after %lld seconds"
+ "MassScan isn't supposed to be used together with other CBDR debug mode: %d"
+ "MassScan: previous scan was %lld seconds ago, avoid scan this time"
+ "Next LBA to process %u\n"
+ "No ratio mode for BCM."
+ "No ratio throttling for simplified Z3."
+ "No simplified zone 3 sync throttling."
+ "Options File: GPT Offset: %u, Extent Count: %u, Merge Frags: %u"
+ "P"
+ "PB table ignored, s6eTunnel %d bcmTunnel %d featureBit %d workMode %d"
+ "PB table ignored, v5Supported %d s6eTunnel %d bcmTunnel %d workMode %d"
+ "PMX"
+ "PNW[%d] band %d boff %d page %d secLeftCommit %d widthSecs %d\n"
+ "PreNandEng_free_asi_log - hix: %d"
+ "Previously had %lld massScans. This one started %lld seconds ago"
+ "Processing LBA %u, Size %u\n"
+ "Prog phase %d [Head: i %d band %d off %d flow %d tag %d], [Tail: i %d band %d off %d flow %d tag %d], Acc: %d \n"
+ "Prog, DInP %d\n"
+ "R"
+ "Read\n"
+ "Refresh rates: HP SOL %u EOL %u"
+ "Retiring lun %d, dip %u"
+ "SL Interrupt! SL_IDX %u F2H? %d"
+ "SLC BURST Z1: %llu"
+ "SLC BURST Z2: %llu"
+ "SLC GCoff Size: %llu"
+ "SLC Reserve: %u"
+ "SoMx=%2u "
+ "T : Timestamp\nP : Percent Cmd_DoPreempt\nWL:\n Ops p 0/1/2/3\n SumLatency p 0/1/2/3\n MaxLatency p0/1/2/3\nRL:\n Ops p 0/1/2/3\n SumLatency p 0/1/2/3\n MaxLatency p0/1/2/3\nE: Block Erases\nF: Host Flushes\nHR: Host Reads\nHW: Host Writes\nNR: Nand Reads\nNW: Nand Writes\nNUR: Nand Util Reads\nNUW: Nand Util Writes\nCW: Clog Writes\nIW: Ind Writes\nGC: GC Writes\nSoMx: Maximal number of stepovers per host bandsBND: Minimal number of stepovers per host band\nHPMM: Maximal number of ASI commands per MSPPR: Prefetch Reads\nPH: Prefetch Hits\nPN: Prefetch fetch next ranges\nAW: Writes that were handled by autowrite HW\nWCD: Write cache dirty percentage\nWCFB: Write cache free buffers percentage\nW : Wear Level Bands\nBI: BLKS(SLC)\nBU: BLKS(MLC/TLC)\nBL: BLKS LVL\nTH: Time in Hysteresis (ms)\nS : Free Segs\nV : IndMem Free\nML: IND_Mem_GetFreeSpace output in percents\nX : Expedite Ok/Fail\nU : Host unmaps\nCmin : Host tags(Min)\nCmax : Host tags(Max)\nBGT: Background task time(us)\nUT: Update Time(us)\nNU: Updates\nST: Search Time(us)\nGMT: GC Move Time(us)\nNS: Searches\nMB: Cache/Ind MBUs\nIMM: Time Spent in Immediate Cmd (us)\nLHS: Ldefrag host sectors read\nLTS: Ldefrag troll sectors read\nLHF: Ldefrag host fragments read\nLTF: Ldefrag troll fragments read\nCCMB: Segs that were combined on cache level, often after troll read\nWCMB: Segs that were combined on writtenQ level, often after buffer fragmentation\nFDOW: Freagments decrease in indirection, zero if increased\nEX: Extra senses in MSP may slow read perf\nNWSM: Nand writes in SLC mode\nNRSM: Nand reads in SLC mode\nNWTM: Nand writes in TLC mode\nNRTM: Nand reads in TLC mode\nPSRD: Parity subtract reads\nTi: IndMem #free tilesDT: delta for +freeTile/-freeTileMTH: IndMem total used mix/highest used mix\nGCS: GC SRC InfoWA: write amplificationGRK: GC src_rk_firstGCST: GC stateGHCO: GC Host choke offsetGCD: GC DST InfoGM: count GC must bands\nUE num ueccs from nand this time period\nGB: total number GBBs\nRH: total number host reconstructions\nRI: total internal reconstruction\nRR: raid sector reads this period\nOBC: Offline blocks count\nDTB: Dir to TLC bands\nBo: oSLC bands\noSLC SM on stateoSLC voters stateREWS: Raid evict engine write sectors\nRFRS: Raid fetch engine read sectors\nADFH:  AES Write Data Beat received from F2H\nADHF: AES Write Data Beat received from H2F\nVBWR: Num Write Data beats rcvd from Vlane\nVBRR: Num Read Data beats sent to Vlane\nCFDWC: Num Write Data beats rcvd from ANS2 CPU\nCFDRC: Num Read Data beats sent to ANS2 CPU\nDLWD: Num Write Data beats rcvd from apcie_0_m\nDLRD: Num Read Data beats sent to apcie_0_m\nUWDF: Num Write Data Beats rcvd from Data Fabric\nURDF: Num Read Data beats sent to Data Fabric\nDPQBI: Num Barriers pushed into Dispatch Queue\nDPQBO: Num Barriers sent out from Dispatch Queue\n"
+ "Temperature"
+ "The device doesnt support thermal throttling"
+ "This version doesn't support %u"
+ "U"
+ "Unexpected non-TLC/non-BCM config. Default to PMX on HW %u "
+ "Unit\tband\tidx\tpendProg\tsegIdx\tinitialized planesDone\treadyPlanes\tlastInPG\tFlags\n"
+ "Unknown ASI cmd size!"
+ "Using 64bytes format for 32bytes ASI command"
+ "Using cmd size different than 64B or 32B need to update DISPATCHER_INCOMING_FIFO_SIZE"
+ "Using default CBDR HP ac. factor instead."
+ "WARNING: thermal self throttling is not supported"
+ "[Head: i %d band %d off %d flow %d tag %d], [Tail: i %d band %d off %d flow %d tag %d], Acc: %d\n"
+ "[Head: i %d band %d off %d flow %d tag %d], [Tail: i %d band %d off %d flow %d tag %d], Acc: %d \n"
+ "asi%u: [ASI_LINK_SPEED_LIMIT] ASI device max speed override = %d"
+ "asi%u: [ASI_LINK_SPEED_LIMIT] ASI device max speed override to value from patchbay = %d"
+ "asi%u: [ASI_LINK_SPEED_LIMIT] Limiting link speed to Gen1 for apcie %d link %d"
+ "asi%u: asi CMD size chosen is: %d"
+ "asi%u: invalid command size %u original bar0 %u"
+ "asiExt allocate: cmd=%u cmpl=%u async mess %u"
+ "asiExt set asyncMess=%p size=%u"
+ "asiExt set cmdExt=%p size=%u"
+ "asiExt set cmplExt=%p size=%u"
+ "async message ASYNC_MESSAGE_ID_MASS_REFRESH from msp: %u, earlyExitAllowed: %u"
+ "async message buf not init"
+ "b=%d, cr=%d/%d/%d cr1=%d/%d/%d cp=%d/%d/%d"
+ "band %u (%llu sectors, %u usec)"
+ "band %u (%llu sectors, %u usec, %llu sec/usec)"
+ "bdr table min max == 0"
+ "completion: payload_dward_1_2=%X, payload_dward_0=%X"
+ "cross temp init %d, %d, %d, %d"
+ "cross temp init defaults %d, %d, %d, %d"
+ "cross temp was not init %x"
+ "ctx band %d off %d flow %d tag %d szLeft %d\n"
+ "done scan ET bands %u"
+ "host ctx band %d off %d flow %d tag %d szLeft %d\n"
+ "internal ctx band %d off %d flow %d tag %d szLeft %d\n"
+ "invalid ET state, band %u, isCold %u, isHot %u"
+ "invalid band temp %u"
+ "invalid msp %u"
+ "invalid params %d, %d"
+ "invalid threshold crossed %u %u"
+ "invalid triggerType %u"
+ "isScanActive should be true"
+ "key_count %u, value_count %u, value_size actual %u)"
+ "no new async message %u"
+ "out of range %p, %u, %u"
+ "out of range %p, %u, %u, buf %p"
+ "prevServed %d nextToServe %d pBM %x rBM %x\n"
+ "raid log\n"
+ "reject device config table"
+ "sBND=%5u "
+ "set disableIdleGC %u"
+ "should not get here: randBandIdx: %d, countBands: %d, numValidPilotScanBands: %d"
+ "sl_hal.c"
+ "starting MassScan, request from MSP %d, earlyExitAllowed: %d"
+ "tt=%u/%u stt=%u/%u/%u/%u/%u ct=%u/%u/%u/%u"
+ "underflow wip Q phase %d, flow %d"
+ "unexpected MIN_SOL_BLOCKS %d"
+ "unexpected async message id %u"
+ "unexpected flags %d"
+ "unexpected flow %d"
+ "unexpected host flow %d"
+ "unexpected mode %d"
+ "unexpected non last phase seg completion, flow %d, band %d, phase %d"
+ "unexpected phase %d"
+ "unit mngr used\n"
+ "unmatch message %u != %u, i: %u, msp : %u"
+ "updateHintQ"
+ "we dont expect PMX to be saved in a BCM band"
+ "wrong power budget table size, expected %u found %u"
+ "{ 'trace_id': 'NANDENG_PROG_DISPATCH', 'tp_func': %d, 'timestamp': %llu, 'die': %u, 'dieDepth_and_hix': %u, 'page': %u, 'band_and_size': %u }\n"
+ "{ 'trace_id': 'NANDENG_PROG_IO_DONE', 'tp_func': %d, 'timestamp': %llu, 'die': %u, 'dieDepth_and_hix': %u, 'page': %u, 'band_and_size': %u }\n"
+ "{ 'trace_id': 'NANDENG_READ_DISPATCH', 'tp_func': %d, 'timestamp': %llu, 'die': %u, 'dieDepth_and_hix': %u, 'page': %u, 'band_and_size': %u }\n"
+ "{ 'trace_id': 'NANDENG_READ_STATUS_DONE', 'tp_func': %d, 'timestamp': %llu, 'die': %u, 'dieDepth_and_hix': %u, 'page': %u, 'band_and_size': %u }\n"
+ "{ 'trace_id': 'PREFETCH_DISCARD', 'tp_func': %d, 'timestamp': %llu, 'lba': %u }\n"
+ "{ 'trace_id': 'PREFETCH_DO', 'tp_func': %d, 'timestamp': %llu, 'origLba': %u, 'prefetchedLba': %u, 'hit': %u }\n"
+ "{ 'trace_id': 'PREFETCH_DONE', 'tp_func': %d, 'timestamp': %llu, 'lba': %u, 'size': %u }\n"
+ "{ 'trace_id': 'PREFETCH_UNMAPPED', 'tp_func': %d, 'timestamp': %llu, 'lba': %u, 'size': %u }\n"
- "\nInd_MC %d  Ind_C %d"
- "%p %u %u %u %lu"
- "/%4u "
- "0x%llX -> 0x%llX"
- "2032.80.3"
- "2032.80.3~461"
- "AppleStorageFirmware-2032.80.3~461"
- "BDR-AF table ignored, s6eTunnel %d featureBit %d"
- "C=%2u"
- "Completion error for nandOp %u (segIdx %u, compl msg 0x%llx)"
- "Conditional bgr_check moving to ric phase %d."
- "Conditional bgr_check, state = %d, phase ric? %d, band = %d"
- "DC table ignored, s6eTunnel %d featureBit %d"
- "DL=%2u "
- "DM=%6u"
- "DU=%6u"
- "Deallocate NS: %d"
- "FAJ=%8u "
- "Failed to set reliability refresh for msp %d"
- "GC Source Rank not defined %u"
- "GC_isOff()"
- "HBO=%8u "
- "Interrupt! SL_IDX %u F2H? %d"
- "Invalid program cycle index %u"
- "PB table ignored, s6eTunnel %d featureBit %d"
- "PUM=%2u"
- "Retiring die %d, dip %u"
- "SLC pages :%d. TLC pages:%d, groups: %d, pages SLC: %d, pages TLC: %d"
- "T : Timestamp\nP : Percent Cmd_DoPreempt\nWL:\n Ops p 0/1/2/3\n SumLatency p 0/1/2/3\n MaxLatency p0/1/2/3\nRL:\n Ops p 0/1/2/3\n SumLatency p 0/1/2/3\n MaxLatency p0/1/2/3\nE: Block Erases\nF: Host Flushes\nHR: Host Reads\nHW: Host Writes\nNR: Nand Reads\nNW: Nand Writes\nNUR: Nand Util Reads\nNUW: Nand Util Writes\nCW: Clog Writes\nIW: Ind Writes\nGC: GC Writes\nPR: Prefetch Reads\nPH: Prefetch Hits\nPN: Prefetch fetch next ranges\nAW: Writes that were handled by autowrite HW\nWCD: Write cache dirty percentage\nWCFB: Write cache free buffers percentage\nW : Wear Level Bands\nBI: BLKS(SLC)\nBU: BLKS(MLC/TLC)\nBL: BLKS LVL\nTH: Time in Hysteresis (ms)\nS : Free Segs\nV : IndMem Free\nML: IND_Mem_GetFreeSpace output in percents\nX : Expedite Ok/Fail\nU : Host unmaps\nC : Host tags(Min/Max)\nBGT: Background task time(us)\nUT: Update Time(us)\nNU: Updates\nST: Search Time(us)\nGMT: GC Move Time(us)\nNS: Searches\nMB: Cache/Ind MBUs\nIMM: Time Spent in Immediate Cmd (us)\nLHS: Ldefrag host sectors read\nLTS: Ldefrag troll sectors read\nLHF: Ldefrag host fragments read\nLTF: Ldefrag troll fragments read\nCCMB: Segs that were combined on cache level, often after troll read\nWCMB: Segs that were combined on writtenQ level, often after buffer fragmentation\nFDOW: Freagments decrease in indirection, zero if increased\nEX: Extra senses in MSP may slow read perf\nNWSM: Nand writes in SLC mode\nNRSM: Nand reads in SLC mode\nNWTM: Nand writes in TLC mode\nNRTM: Nand reads in TLC mode\nPSRD: Parity subtract reads\nTi: IndMem #free tilesDT: delta for +freeTile/-freeTileDL: delta for GC #L iterationsDM: delta for GC L LBAs moved/frags movedDU: delta for GC L LBAs updated/frags updatedPUM: L moves/updates% LBAs/fragsMTH: IndMem total used mix/highest used mix\nGCS: GC SRC InfoWA: write amplificationGRK: GC src_rk_firstGCD: GC DST InfoGM: count GC must bands\nUE num ueccs from nand this time period\nGB: total number GBBs\nRH: total number host reconstructions\nRI: total internal reconstruction\nRR: raid sector reads this period\nOBC: Offline blocks count\nDTB: Dir to TLC bands\nBo: oSLC bands\noSLC SM on stateoSLC voters stateREWS: Raid evict engine write sectors\nRFRS: Raid fetch engine read sectors\nADFH:  AES Write Data Beat received from F2H\nADHF: AES Write Data Beat received from H2F\nVBWR: Num Write Data beats rcvd from Vlane\nVBRR: Num Read Data beats sent to Vlane\nCFDWC: Num Write Data beats rcvd from ANS2 CPU\nCFDRC: Num Read Data beats sent to ANS2 CPU\nDLWD: Num Write Data beats rcvd from apcie_0_m\nDLRD: Num Read Data beats sent to apcie_0_m\nUWDF: Num Write Data Beats rcvd from Data Fabric\nURDF: Num Read Data beats sent to Data Fabric\nDPQBI: Num Barriers pushed into Dispatch Queue\nDPQBO: Num Barriers sent out from Dispatch Queue\n"
- "Unexpected non-TLC config. Default to PMX on HW %u "
- "Unknown mmu_attribute type: %d"
- "Using cmd size different than 32B need to update DISPATCHER_INCOMING_FIFO_SIZE"
- "asi%u: invalid command size %u (expected %u, original bar0 %u)"
- "asiExt allocate: cmd=%u cmpl=%u"
- "asiExt set cmd=%p size=%u"
- "asiExt set cmpl=%p size=%u"
- "completion: status_0_31=%X, status_32_47=%X"
- "dispatcher_monitor.c"
- "flow %d, pt %d, barrierSkips %d"
- "flow %s accum %u"
- "invalid band %d for flow %d"
- "invalid pool idx - %d"
- "key_count %u, value_count %u, value_size actual %u expected %u)"
- "prefetchFreeQ"
- "shifted_pool_phys_addr = %llx"
- "unexpected ICC duration index"
- "unexpected bmx size!, band %d, bmxGroup %d"
- "unrecognized fence tracker: %u"
- "{ 'trace_id': 'NANDENG_PROG_DISPATCH', 'tp_func': %d, 'timestamp': %llu, 'die': %u, 'dieDepth': %u, 'page': %u, 'band': %u }\n"
- "{ 'trace_id': 'NANDENG_PROG_IO_DONE', 'tp_func': %d, 'timestamp': %llu, 'die': %u, 'stepovers': %u, 'page': %u, 'band': %u }\n"
- "{ 'trace_id': 'NANDENG_READ_DISPATCH', 'tp_func': %d, 'timestamp': %llu, 'die': %u, 'dieDepth': %u, 'page': %u, 'band': %u }\n"
- "{ 'trace_id': 'NANDENG_READ_STATUS_DONE', 'tp_func': %d, 'timestamp': %llu, 'die': %u, 'dieDepth': %u, 'page': %u, 'band': %u }\n"

```
