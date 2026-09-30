## sysdiagnose_helper

> `/usr/libexec/sysdiagnose_helper`

```diff

-1438.80.3.0.0
-  __TEXT.__text: 0x34958
+1438.100.33.0.0
+  __TEXT.__text: 0x361ac
   __TEXT.__auth_stubs: 0xb60
   __TEXT.__objc_stubs: 0x13e0
-  __TEXT.__objc_methlist: 0x514
-  __TEXT.__const: 0x3c8
-  __TEXT.__gcc_except_tab: 0x7e8
+  __TEXT.__objc_methlist: 0x544
+  __TEXT.__const: 0x3f8
+  __TEXT.__gcc_except_tab: 0x7ec
   __TEXT.__oslogstring: 0x202b
-  __TEXT.__cstring: 0x2b6f2
+  __TEXT.__cstring: 0x2c663
   __TEXT.__objc_classname: 0xc4
   __TEXT.__objc_methtype: 0x29b
   __TEXT.__objc_methname: 0x1434
-  __TEXT.__unwind_info: 0x500
+  __TEXT.__unwind_info: 0x508
   __DATA_CONST.__auth_got: 0x5c0
-  __DATA_CONST.__got: 0x230
+  __DATA_CONST.__got: 0x198
+  __DATA_CONST.__auth_ptr: 0x98
   __DATA_CONST.__const: 0x640
   __DATA_CONST.__cfstring: 0x1a60
   __DATA_CONST.__objc_classlist: 0x30

   __DATA_CONST.__objc_arraydata: 0x110
   __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA.__objc_const: 0x718
+  __DATA.__objc_const: 0x6d8
   __DATA.__objc_selrefs: 0x568
   __DATA.__objc_ivar: 0x38
   __DATA.__objc_data: 0x1e0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libtzupdate.dylib
-  Functions: 312
+  Functions: 304
   Symbols:   244
-  CStrings:  3771
+  CStrings:  3854
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_retain_x25
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
+ "activeTimeInThrottleZone"
+ "asyncMessageHisto"
+ "asyncMessageHisto_"
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
+ "numOfThrottlingLevels"
+ "numPerfOptionalRefreshes"
+ "numRefreshOnErrNandRefreshPerfOpt"
+ "numRefreshOnErrNandRefreshPerfOptOpen"
+ "perstStatFree"
+ "prefetchNofHits"
+ "prefetchRedundantBufs"
+ "prefetchUsedBufs"
+ "realGBBPerDipOfFailingDie"
+ "realGBBPerDipOfFailingDie_"
+ "regularReadBlockAge"
+ "secInColdHisto"
+ "secInHotHisto"
+ "tempChangedEnterETHisto"
+ "tempChangedEnterETHisto_"
+ "tempChangedHisto"
+ "tempChangedHisto_"
+ "thermalSelfThrottlingEnabled"
+ "thermalSelfThrottlingSupported"
+ "unhappyVertGC"
+ "unhappyVertGC_"
+ "unhappyWideGC1"
+ "unhappyWideGC1_"
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
- "bandKill_formatUserExcessive"
- "band_rbo_allocated"
- "dmFlatten"
- "fallbackToWaterfallValidity"
- "gcPDusterSrcFound"
- "gcPDusterSrcInvalidatedByGC"
- "gcPDusterSrcRemoved"
- "offlineDieCnt"

```
