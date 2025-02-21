## NANDTaskScheduler

> `/usr/libexec/NANDTaskScheduler`

```diff

-592.40.2.0.0
-  __TEXT.__text: 0x1a164
+616.100.5.0.0
+  __TEXT.__text: 0x1b184
   __TEXT.__auth_stubs: 0x240
-  __TEXT.__cstring: 0x284c2
+  __TEXT.__cstring: 0x29382
   __TEXT.__const: 0xb8
   __TEXT.__oslogstring: 0x191
-  __TEXT.__unwind_info: 0xf0
+  __TEXT.__unwind_info: 0xe8
   __DATA_CONST.__auth_got: 0x120
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__const: 0x40

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
-  Functions: 85
+  Functions: 76
   Symbols:   47
-  CStrings:  2858
+  CStrings:  2928
 
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
+ "RD_closedBandEvictBlocks"
+ "RD_closedBlocksTHHist"
+ "RD_closedBlocksTHHist_"
+ "RD_openBandEvictBlocks"
+ "asyncMessageHisto"
+ "asyncMessageHisto_"
+ "crossTempColdEvict"
+ "crossTempColdHotEvict"
+ "crossTempHotEvict"
+ "deviceTempHigh"
+ "deviceTempLow"
+ "deviceTempMax"
+ "massScanEarlyExits"
+ "massScanFullRounds"
+ "massScanIgnoredTooFrequent"
+ "massScanMspEarlyExitRequests"
+ "massScanMspFullScanRequests"
+ "numOfThrottlingLevels"
+ "numRefreshOnErrNandRefreshPerfOpt"
+ "numRefreshOnErrNandRefreshPerfOptOpen"
+ "prefetchNofHits"
+ "raidBlkParityBands"
+ "raidBlkParitySecs"
+ "realGBBPerDipOfFailingDie"
+ "realGBBPerDipOfFailingDie_"
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

```
