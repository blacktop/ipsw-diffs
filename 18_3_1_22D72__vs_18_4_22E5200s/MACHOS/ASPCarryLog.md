## ASPCarryLog

> `/usr/libexec/ASPCarryLog`

```diff

-592.40.2.0.0
-  __TEXT.__text: 0x44528
-  __TEXT.__auth_stubs: 0xc20
-  __TEXT.__objc_stubs: 0x3040
-  __TEXT.__objc_methlist: 0x1124
+616.100.5.0.0
+  __TEXT.__text: 0x45fe0
+  __TEXT.__auth_stubs: 0xc10
+  __TEXT.__objc_stubs: 0x3060
+  __TEXT.__objc_methlist: 0x14e8
   __TEXT.__gcc_except_tab: 0x58c
-  __TEXT.__cstring: 0x3de5c
-  __TEXT.__const: 0x1e8
-  __TEXT.__objc_methname: 0x32fe
+  __TEXT.__cstring: 0x3fbfa
+  __TEXT.__const: 0x270
+  __TEXT.__objc_methname: 0x330e
   __TEXT.__oslogstring: 0x12b8
   __TEXT.__objc_classname: 0x263
   __TEXT.__objc_methtype: 0x9f6
-  __TEXT.__unwind_info: 0x5a8
-  __DATA_CONST.__auth_got: 0x628
-  __DATA_CONST.__got: 0x228
-  __DATA_CONST.__auth_ptr: 0x10
+  __TEXT.__unwind_info: 0x598
+  __DATA_CONST.__auth_got: 0x620
+  __DATA_CONST.__got: 0x1d8
+  __DATA_CONST.__auth_ptr: 0x60
   __DATA_CONST.__const: 0x370
-  __DATA_CONST.__cfstring: 0x1f840
+  __DATA_CONST.__cfstring: 0x20c00
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x58
-  __DATA_CONST.__objc_intobj: 0xfd8
-  __DATA_CONST.__objc_arraydata: 0xffb8
+  __DATA_CONST.__objc_intobj: 0xff0
+  __DATA_CONST.__objc_arraydata: 0x109b0
   __DATA_CONST.__objc_dictobj: 0x168
   __DATA_CONST.__objc_arrayobj: 0x378
-  __DATA.__objc_const: 0x2598
-  __DATA.__objc_selrefs: 0xdb0
+  __DATA.__objc_const: 0x1ea8
+  __DATA.__objc_selrefs: 0xe50
   __DATA.__objc_ivar: 0x124
   __DATA.__objc_data: 0x550
   __DATA.__data: 0xea8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/local/lib/libNVMeCTL.dylib
-  Functions: 615
-  Symbols:   268
-  CStrings:  7688
+  Functions: 609
+  Symbols:   267
+  CStrings:  7908
 
Symbols:
- _objc_release_x1
CStrings:
+ "ASPFTLParseBufferToCxt: RD_closedBandEvictBlocks(1222) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: RD_closedBlocksTHHist(1223): (#10) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: RD_closedBlocksTHHist(1223): Cannot add 10 elements to context"
+ "ASPFTLParseBufferToCxt: RD_openBandEvictBlocks(1221) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: asyncMessageHisto(1367): (#32) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: asyncMessageHisto(1367): Cannot add 32 elements to context"
+ "ASPFTLParseBufferToCxt: crossTempColdEvict(1355) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: crossTempColdHotEvict(1357) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: crossTempHotEvict(1356) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: deviceTempHigh(1272) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: deviceTempLow(1273) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: deviceTempMax(1271) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: massScanEarlyExits(1327) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: massScanFullRounds(1326) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: massScanIgnoredTooFrequent(1368) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: massScanMspEarlyExitRequests(1329) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: massScanMspFullScanRequests(1328) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: numOfThrottlingEntriesPerLevel(207): (#25) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: numOfThrottlingEntriesPerLevel(207): Cannot add 25 elements to context"
+ "ASPFTLParseBufferToCxt: numOfThrottlingEntriesPerReadLevel(453): (#25) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: numOfThrottlingEntriesPerReadLevel(453): Cannot add 25 elements to context"
+ "ASPFTLParseBufferToCxt: numOfThrottlingEntriesPerWriteLevel(454): (#25) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: numOfThrottlingEntriesPerWriteLevel(454): Cannot add 25 elements to context"
+ "ASPFTLParseBufferToCxt: numOfThrottlingLevels(1354) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: numRefreshOnErrNandRefreshPerfOpt(1264) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: numRefreshOnErrNandRefreshPerfOptOpen(1289) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: prefetchNofHits(1323) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: raidBlkParityBands(964) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: raidBlkParitySecs(965) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: realGBBPerDipOfFailingDie(1369): (#8) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: realGBBPerDipOfFailingDie(1369): Cannot add 8 elements to context"
+ "ASPFTLParseBufferToCxt: tempChangedEnterETHisto(1359): (#13) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: tempChangedEnterETHisto(1359): Cannot add 13 elements to context"
+ "ASPFTLParseBufferToCxt: tempChangedHisto(1358): (#13) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: tempChangedHisto(1358): Cannot add 13 elements to context"
+ "ASPFTLParseBufferToCxt: thermalSelfThrottlingEnabled(1349) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: thermalSelfThrottlingSupported(1348) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: timeOfThrottlingPerLevel(865): (#25) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: timeOfThrottlingPerLevel(865): Cannot add 25 elements to context"
+ "ASPFTLParseBufferToCxt: timeOfThrottlingPerReadLevel(866): (#25) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: timeOfThrottlingPerReadLevel(866): Cannot add 25 elements to context"
+ "ASPFTLParseBufferToCxt: timeOfThrottlingPerWriteLevel(867): (#25) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: timeOfThrottlingPerWriteLevel(867): Cannot add 25 elements to context"
+ "ASPFTLParseBufferToCxt: unhappyVertGC(1345): (#4) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: unhappyVertGC(1345): Cannot add 4 elements to context"
+ "ASPFTLParseBufferToCxt: unhappyWideGC1(1344): (#4) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: unhappyWideGC1(1344): Cannot add 4 elements to context"
+ "BCM"
+ "RD_closedBlocksTHHist_"
+ "RD_closedBlocksTHHist_0"
+ "RD_closedBlocksTHHist_1"
+ "RD_closedBlocksTHHist_2"
+ "RD_closedBlocksTHHist_3"
+ "RD_closedBlocksTHHist_4"
+ "RD_closedBlocksTHHist_5"
+ "RD_closedBlocksTHHist_6"
+ "RD_closedBlocksTHHist_7"
+ "RD_closedBlocksTHHist_8"
+ "RD_closedBlocksTHHist_9"
+ "activeTimeInThrottleZone"
+ "asyncMessageHisto"
+ "asyncMessageHisto_"
+ "asyncMessageHisto_0"
+ "asyncMessageHisto_1"
+ "asyncMessageHisto_10"
+ "asyncMessageHisto_11"
+ "asyncMessageHisto_12"
+ "asyncMessageHisto_13"
+ "asyncMessageHisto_14"
+ "asyncMessageHisto_15"
+ "asyncMessageHisto_16"
+ "asyncMessageHisto_17"
+ "asyncMessageHisto_18"
+ "asyncMessageHisto_19"
+ "asyncMessageHisto_2"
+ "asyncMessageHisto_20"
+ "asyncMessageHisto_21"
+ "asyncMessageHisto_22"
+ "asyncMessageHisto_23"
+ "asyncMessageHisto_24"
+ "asyncMessageHisto_25"
+ "asyncMessageHisto_26"
+ "asyncMessageHisto_27"
+ "asyncMessageHisto_28"
+ "asyncMessageHisto_29"
+ "asyncMessageHisto_3"
+ "asyncMessageHisto_30"
+ "asyncMessageHisto_31"
+ "asyncMessageHisto_4"
+ "asyncMessageHisto_5"
+ "asyncMessageHisto_6"
+ "asyncMessageHisto_7"
+ "asyncMessageHisto_8"
+ "asyncMessageHisto_9"
+ "bandsGBBTempHisto"
+ "bitsPerCell"
+ "blockScanReadBlockAge"
+ "bpHostChokeTime"
+ "bpZone2EntryGCTP"
+ "bpZone2EntryHW"
+ "bpZone2EntryHostTP"
+ "bpZone2EntryTime"
+ "bpZone2ExitGCTP"
+ "bpZone2ExitHW"
+ "bpZone2ExitHostTP"
+ "bpZone2ExitTime"
+ "cbdrLastScannedHrHP"
+ "cbdrScanHP"
+ "cbdrScanMP"
+ "crossTempColdEvict"
+ "crossTempColdHotEvict"
+ "crossTempHotEvict"
+ "deviceTempHigh"
+ "deviceTempLow"
+ "deviceTempMax"
+ "disableIdleGC"
+ "enhancedReadBlockAge"
+ "massScanCurrentState"
+ "massScanEarlyExits"
+ "massScanFullRounds"
+ "massScanIgnoredTooFrequent"
+ "massScanMspEarlyExitRequests"
+ "massScanMspFullScanRequests"
+ "numOfThrottlingEntriesPerLevel_16"
+ "numOfThrottlingEntriesPerLevel_17"
+ "numOfThrottlingEntriesPerLevel_18"
+ "numOfThrottlingEntriesPerLevel_19"
+ "numOfThrottlingEntriesPerLevel_20"
+ "numOfThrottlingEntriesPerLevel_21"
+ "numOfThrottlingEntriesPerLevel_22"
+ "numOfThrottlingEntriesPerLevel_23"
+ "numOfThrottlingEntriesPerLevel_24"
+ "numOfThrottlingEntriesPerReadLevel_16"
+ "numOfThrottlingEntriesPerReadLevel_17"
+ "numOfThrottlingEntriesPerReadLevel_18"
+ "numOfThrottlingEntriesPerReadLevel_19"
+ "numOfThrottlingEntriesPerReadLevel_20"
+ "numOfThrottlingEntriesPerReadLevel_21"
+ "numOfThrottlingEntriesPerReadLevel_22"
+ "numOfThrottlingEntriesPerReadLevel_23"
+ "numOfThrottlingEntriesPerReadLevel_24"
+ "numOfThrottlingEntriesPerWriteLevel_16"
+ "numOfThrottlingEntriesPerWriteLevel_17"
+ "numOfThrottlingEntriesPerWriteLevel_18"
+ "numOfThrottlingEntriesPerWriteLevel_19"
+ "numOfThrottlingEntriesPerWriteLevel_20"
+ "numOfThrottlingEntriesPerWriteLevel_21"
+ "numOfThrottlingEntriesPerWriteLevel_22"
+ "numOfThrottlingEntriesPerWriteLevel_23"
+ "numOfThrottlingEntriesPerWriteLevel_24"
+ "numOfThrottlingLevels"
+ "numPerfOptionalRefreshes"
+ "numRefreshOnErrNandRefreshPerfOpt"
+ "numRefreshOnErrNandRefreshPerfOptOpen"
+ "numberWithChar:"
+ "perstStatFree"
+ "prefetchNofHits"
+ "prefetchRedundantBufs"
+ "prefetchUsedBufs"
+ "realGBBPerDipOfFailingDie"
+ "realGBBPerDipOfFailingDie_"
+ "realGBBPerDipOfFailingDie_0"
+ "realGBBPerDipOfFailingDie_1"
+ "realGBBPerDipOfFailingDie_2"
+ "realGBBPerDipOfFailingDie_3"
+ "realGBBPerDipOfFailingDie_4"
+ "realGBBPerDipOfFailingDie_5"
+ "realGBBPerDipOfFailingDie_6"
+ "realGBBPerDipOfFailingDie_7"
+ "regularReadBlockAge"
+ "secInColdHisto"
+ "secInHotHisto"
+ "tempChangedEnterETHisto"
+ "tempChangedEnterETHisto_"
+ "tempChangedEnterETHisto_0"
+ "tempChangedEnterETHisto_1"
+ "tempChangedEnterETHisto_10"
+ "tempChangedEnterETHisto_11"
+ "tempChangedEnterETHisto_12"
+ "tempChangedEnterETHisto_2"
+ "tempChangedEnterETHisto_3"
+ "tempChangedEnterETHisto_4"
+ "tempChangedEnterETHisto_5"
+ "tempChangedEnterETHisto_6"
+ "tempChangedEnterETHisto_7"
+ "tempChangedEnterETHisto_8"
+ "tempChangedEnterETHisto_9"
+ "tempChangedHisto"
+ "tempChangedHisto_"
+ "tempChangedHisto_0"
+ "tempChangedHisto_1"
+ "tempChangedHisto_10"
+ "tempChangedHisto_11"
+ "tempChangedHisto_12"
+ "tempChangedHisto_2"
+ "tempChangedHisto_3"
+ "tempChangedHisto_4"
+ "tempChangedHisto_5"
+ "tempChangedHisto_6"
+ "tempChangedHisto_7"
+ "tempChangedHisto_8"
+ "tempChangedHisto_9"
+ "thermalSelfThrottlingEnabled"
+ "thermalSelfThrottlingSupported"
+ "timeOfThrottlingPerLevel_16"
+ "timeOfThrottlingPerLevel_17"
+ "timeOfThrottlingPerLevel_18"
+ "timeOfThrottlingPerLevel_19"
+ "timeOfThrottlingPerLevel_20"
+ "timeOfThrottlingPerLevel_21"
+ "timeOfThrottlingPerLevel_22"
+ "timeOfThrottlingPerLevel_23"
+ "timeOfThrottlingPerLevel_24"
+ "timeOfThrottlingPerReadLevel_16"
+ "timeOfThrottlingPerReadLevel_17"
+ "timeOfThrottlingPerReadLevel_18"
+ "timeOfThrottlingPerReadLevel_19"
+ "timeOfThrottlingPerReadLevel_20"
+ "timeOfThrottlingPerReadLevel_21"
+ "timeOfThrottlingPerReadLevel_22"
+ "timeOfThrottlingPerReadLevel_23"
+ "timeOfThrottlingPerReadLevel_24"
+ "timeOfThrottlingPerWriteLevel_16"
+ "timeOfThrottlingPerWriteLevel_17"
+ "timeOfThrottlingPerWriteLevel_18"
+ "timeOfThrottlingPerWriteLevel_19"
+ "timeOfThrottlingPerWriteLevel_20"
+ "timeOfThrottlingPerWriteLevel_21"
+ "timeOfThrottlingPerWriteLevel_22"
+ "timeOfThrottlingPerWriteLevel_23"
+ "timeOfThrottlingPerWriteLevel_24"
+ "unhappyVertGC"
+ "unhappyVertGC_"
+ "unhappyVertGC_0"
+ "unhappyVertGC_1"
+ "unhappyVertGC_2"
+ "unhappyVertGC_3"
+ "unhappyWideGC1"
+ "unhappyWideGC1_"
+ "unhappyWideGC1_0"
+ "unhappyWideGC1_1"
+ "unhappyWideGC1_2"
+ "unhappyWideGC1_3"
- "ASPFTLParseBufferToCxt: numOfThrottlingEntriesPerLevel(207): (#16) cfg elements != (%d) buffer elements"
- "ASPFTLParseBufferToCxt: numOfThrottlingEntriesPerLevel(207): Cannot add 16 elements to context"
- "ASPFTLParseBufferToCxt: numOfThrottlingEntriesPerReadLevel(453): (#16) cfg elements != (%d) buffer elements"
- "ASPFTLParseBufferToCxt: numOfThrottlingEntriesPerReadLevel(453): Cannot add 16 elements to context"
- "ASPFTLParseBufferToCxt: numOfThrottlingEntriesPerWriteLevel(454): (#16) cfg elements != (%d) buffer elements"
- "ASPFTLParseBufferToCxt: numOfThrottlingEntriesPerWriteLevel(454): Cannot add 16 elements to context"
- "ASPFTLParseBufferToCxt: timeOfThrottlingPerLevel(865): (#16) cfg elements != (%d) buffer elements"
- "ASPFTLParseBufferToCxt: timeOfThrottlingPerLevel(865): Cannot add 16 elements to context"
- "ASPFTLParseBufferToCxt: timeOfThrottlingPerReadLevel(866): (#16) cfg elements != (%d) buffer elements"
- "ASPFTLParseBufferToCxt: timeOfThrottlingPerReadLevel(866): Cannot add 16 elements to context"
- "ASPFTLParseBufferToCxt: timeOfThrottlingPerWriteLevel(867): (#16) cfg elements != (%d) buffer elements"
- "ASPFTLParseBufferToCxt: timeOfThrottlingPerWriteLevel(867): Cannot add 16 elements to context"
- "MLC"
- "Unexpected step %@"
- "Wrong IOLog SPD get buffer option %d"
- "bandKill_formatUserExcessive"
- "band_rbo_allocated"
- "dmFlatten"
- "fallbackToWaterfallValidity"
- "gcPDusterSrcFound"
- "gcPDusterSrcInvalidatedByGC"
- "gcPDusterSrcRemoved"
- "offlineDieCnt"

```
