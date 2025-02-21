## hangreporter

> `/usr/libexec/hangreporter`

```diff

-331.3.0.0.0
-  __TEXT.__text: 0x36f3c
-  __TEXT.__auth_stubs: 0xe80
-  __TEXT.__objc_stubs: 0x2aa0
-  __TEXT.__objc_methlist: 0xd2c
+352.0.0.0.0
+  __TEXT.__text: 0x390d8
+  __TEXT.__auth_stubs: 0xea0
+  __TEXT.__objc_stubs: 0x2a80
+  __TEXT.__objc_methlist: 0xebc
   __TEXT.__const: 0x198
-  __TEXT.__cstring: 0x2bc63
-  __TEXT.__oslogstring: 0x41f7
-  __TEXT.__gcc_except_tab: 0x7ac
-  __TEXT.__objc_methname: 0x4cd2
+  __TEXT.__cstring: 0x2cb83
+  __TEXT.__oslogstring: 0x424b
+  __TEXT.__gcc_except_tab: 0xd10
+  __TEXT.__objc_methname: 0x4e01
   __TEXT.__objc_classname: 0x113
   __TEXT.__objc_methtype: 0x851
-  __TEXT.__unwind_info: 0x448
-  __DATA_CONST.__auth_got: 0x750
+  __TEXT.__unwind_info: 0x488
+  __DATA_CONST.__auth_got: 0x760
   __DATA_CONST.__got: 0x258
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x1330
-  __DATA_CONST.__cfstring: 0x4880
+  __DATA_CONST.__const: 0x12d0
+  __DATA_CONST.__cfstring: 0x48a0
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x50
-  __DATA_CONST.__objc_intobj: 0x90
+  __DATA_CONST.__objc_intobj: 0x78
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x2658
-  __DATA.__objc_selrefs: 0xef0
-  __DATA.__objc_ivar: 0x23c
+  __DATA.__objc_const: 0x2450
+  __DATA.__objc_selrefs: 0xf88
+  __DATA.__objc_ivar: 0x248
   __DATA.__objc_data: 0x370
   __DATA.__data: 0x638
   __DATA.__bss: 0xb8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 558
-  Symbols:   318
-  CStrings:  4634
+  Functions: 624
+  Symbols:   320
+  CStrings:  4714
 
Symbols:
+ __os_log_error_impl
+ _objc_retainAutoreleasedReturnValue
CStrings:
+ "%ld"
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
+ "Failed to create or access the following directories: %@, %@"
+ "HangTracerConsecutiveHangWaitTimeoutDuration"
+ "Not attempting to save a tailspin. HTPrefs: shouldSaveTailspins = %d"
+ "PDSEPrefWBClientHangKillSwitch"
+ "PDSEPrefWBClientHangPeriodDays"
+ "RD_closedBandEvictBlocks"
+ "RD_closedBlocksTHHist"
+ "RD_closedBlocksTHHist_"
+ "RD_openBandEvictBlocks"
+ "TB,R,V_pdseWBClientHangKillSwitch"
+ "TB,R,V_shouldAugmentSentryTailspinWithSignposts"
+ "TQ,R,V_consecutiveHangWaitTimeoutDurationMSec"
+ "Ti,R,V_pdseWBClientHangPeriodDays"
+ "_consecutiveHangWaitTimeoutDurationMSec"
+ "_pdseWBClientHangKillSwitch"
+ "_pdseWBClientHangPeriodDays"
+ "_shouldAugmentSentryTailspinWithSignposts"
+ "asyncMessageHisto"
+ "asyncMessageHisto_"
+ "consecutiveHangWaitTimeoutDurationMSec"
+ "cpu limit"
+ "crossTempColdEvict"
+ "crossTempColdHotEvict"
+ "crossTempHotEvict"
+ "deviceTempHigh"
+ "deviceTempLow"
+ "deviceTempMax"
+ "gt:"
+ "lt:"
+ "massScanEarlyExits"
+ "massScanFullRounds"
+ "massScanIgnoredTooFrequent"
+ "massScanMspEarlyExitRequests"
+ "massScanMspFullScanRequests"
+ "numOfThrottlingLevels"
+ "numRefreshOnErrNandRefreshPerfOpt"
+ "numRefreshOnErrNandRefreshPerfOptOpen"
+ "pdseWBClientHangKillSwitch"
+ "pdseWBClientHangPeriodDays"
+ "prefetchNofHits"
+ "raidBlkParityBands"
+ "raidBlkParitySecs"
+ "realGBBPerDipOfFailingDie"
+ "realGBBPerDipOfFailingDie_"
+ "self restrict"
+ "shouldAugmentSentryTailspinWithSignposts"
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
+ "\xf0\xf0A!&!"
- "238"
- "248"
- "302"
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
- "Regular Launch"
- "Slow Launch"
- "TB,R,V_shouldCollectOSSignpostsDeferred"
- "_shouldCollectOSSignpostsDeferred"
- "ge:"
- "le:"
- "mainBinaryPath field was nil in SATask object"
- "setDisplayKernelFrames:"
- "shouldCollectOSSignpostsDeferred"
- "\xf0\xf0A\x11&!"

```
