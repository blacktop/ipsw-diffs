## lockdownd

> `/usr/libexec/lockdownd`

```diff

-1319.80.2.0.0
-  __TEXT.__text: 0x102e5c
-  __TEXT.__auth_stubs: 0x2ce0
+1329.100.0.502.1
+  __TEXT.__text: 0x107108
+  __TEXT.__auth_stubs: 0x2cf0
   __TEXT.__objc_stubs: 0x43e0
-  __TEXT.__objc_methlist: 0x3438
-  __TEXT.__cstring: 0x4d48c
-  __TEXT.__const: 0x160f0
+  __TEXT.__objc_methlist: 0x3520
+  __TEXT.__cstring: 0x4e422
+  __TEXT.__const: 0x16100
   __TEXT.__oslogstring: 0x788
-  __TEXT.__gcc_except_tab: 0x399c
-  __TEXT.__objc_classname: 0xbb3
-  __TEXT.__objc_methname: 0x476f
-  __TEXT.__objc_methtype: 0xe80
+  __TEXT.__gcc_except_tab: 0x3a20
+  __TEXT.__objc_classname: 0xbbd
+  __TEXT.__objc_methname: 0x4774
+  __TEXT.__objc_methtype: 0xeb1
   __TEXT.__services: 0x2d8f
-  __TEXT.__unwind_info: 0x2d30
-  __TEXT.__eh_frame: 0x10b8
-  __DATA_CONST.__auth_got: 0x1688
-  __DATA_CONST.__got: 0x698
-  __DATA_CONST.__auth_ptr: 0x50
-  __DATA_CONST.__const: 0xa998
-  __DATA_CONST.__cfstring: 0x17ca0
+  __TEXT.__unwind_info: 0x2f10
+  __TEXT.__eh_frame: 0x10b0
+  __DATA_CONST.__auth_got: 0x1690
+  __DATA_CONST.__got: 0x668
+  __DATA_CONST.__auth_ptr: 0x58
+  __DATA_CONST.__const: 0xa9b8
+  __DATA_CONST.__cfstring: 0x17d60
   __DATA_CONST.__objc_classlist: 0x280
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_intobj: 0x108
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x6290
-  __DATA.__objc_selrefs: 0x1480
+  __DATA.__objc_const: 0x6128
+  __DATA.__objc_selrefs: 0x14a0
   __DATA.__objc_ivar: 0x410
   __DATA.__objc_data: 0x1900
-  __DATA.__data: 0x2b68
-  __DATA.__bss: 0x1052
-  __DATA.__common: 0x1a48
+  __DATA.__data: 0x2b60
+  __DATA.__bss: 0x1058
+  __DATA.__common: 0x1a40
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2942
-  Symbols:   926
-  CStrings:  9473
+  Functions: 3416
+  Symbols:   922
+  CStrings:  9550
 
Symbols:
+ _AMSupportPlatformWriteDataToFileURL
- __ZNK3ctu9SharedRefI14__CFDictionaryNS_2cf16cfretain_functorENS2_17cfrelease_functorES1_E3getEv
- __ZNK3ctu9SharedRefIK10__CFStringNS_2cf16cfretain_functorENS3_17cfrelease_functorES2_E3getEv
- __ZNK3ctu9SharedRefIK14__CFDictionaryNS_2cf16cfretain_functorENS3_17cfrelease_functorES2_E3getEv
- __ZNK3ctu9SharedRefIK8__CFDataNS_2cf16cfretain_functorENS3_17cfrelease_functorES2_E3getEv
- __ZNK3ctu9SharedRefIKvNS_2cf16cfretain_functorENS2_17cfrelease_functorES1_E3getEv
CStrings:
+ "%s::%s: no dataref\n"
+ "%s::%s: no digest in build ID (%s)\n"
+ "%s::%s: optional tag %s missing from build identity, skipping\n"
+ "%s::%s: tag %s missing from firmware, skipping\n"
+ "%s::%s: wrong digest type (%s)\n"
+ "-[MantaFTABFile addSubfileWithTagName:contentsOfURL:]"
+ "-[MantaFTABFile initWithContentsOfURL:]"
+ "-[MantaFTABFile parseFileData]"
+ "@\"MantaFTABSubfile\""
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
+ "Ap,SecurePageTableMonitor"
+ "Ap,TrustedExecutionMonitor"
+ "Ap,cL4"
+ "B32@0:8^{ramrod_update_callbacks=i^?^?^?^?^?^?^?^?^{ramrod_updater}^?^?^?^?^?^?}16^{firmware_update_context=^{RestoredHostConnection}^{__CFDictionary}^v^{__CFDictionary}^{__CFDictionary}CC^v^{__CFDictionary}C}24"
+ "B40@0:8^{ramrod_update_callbacks=i^?^?^?^?^?^?^?^?^{ramrod_updater}^?^?^?^?^?^?}16^{firmware_update_context=^{RestoredHostConnection}^{__CFDictionary}^v^{__CFDictionary}^{__CFDictionary}CC^v^{__CFDictionary}C}24^@32"
+ "HelsinkiRestore-56.4.12"
+ "MantaFTABFile"
+ "MantaFTABSubfile"
+ "RD_closedBandEvictBlocks"
+ "RD_closedBlocksTHHist"
+ "RD_closedBlocksTHHist_"
+ "RD_openBandEvictBlocks"
+ "T@\"MantaFTABSubfile\",R,V_manifest"
+ "VinylRestore-78~6589"
+ "asyncMessageHisto"
+ "asyncMessageHisto_"
+ "createRequest: no digest in build ID"
+ "createRequest: wrong digest type"
+ "crossTempColdEvict"
+ "crossTempColdHotEvict"
+ "crossTempHotEvict"
+ "deviceTempHigh"
+ "deviceTempLow"
+ "deviceTempMax"
+ "excl"
+ "libauthinstall_device-1049.100.21"
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
+ "sptm"
+ "tempChangedEnterETHisto"
+ "tempChangedEnterETHisto_"
+ "tempChangedHisto"
+ "tempChangedHisto_"
+ "thermalSelfThrottlingEnabled"
+ "thermalSelfThrottlingSupported"
+ "trxm"
+ "unhappyVertGC"
+ "unhappyVertGC_"
+ "unhappyWideGC1"
+ "unhappyWideGC1_"
- "%s::%s: Tag '%s' doesn't exist -- moving along\n"
- "-[FTABFile addSubfileWithTagName:contentsOfURL:]"
- "-[FTABFile initWithContentsOfURL:]"
- "-[FTABFile parseFileData]"
- ".."
- "@\"FTABSubfile\""
- "AMAuthInstallPlatformWriteBufferToNativeFilePath"
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
- "B32@0:8^{ramrod_update_callbacks=i^?^?^?^?^?^?^?^?^{ramrod_updater}^?^?^?^?^?^?}16^{firmware_update_context=i^{__CFDictionary}^v^{__CFDictionary}^{__CFDictionary}^vCC^v^{__CFDictionary}C}24"
- "B40@0:8^{ramrod_update_callbacks=i^?^?^?^?^?^?^?^?^{ramrod_updater}^?^?^?^?^?^?}16^{firmware_update_context=i^{__CFDictionary}^v^{__CFDictionary}^{__CFDictionary}^vCC^v^{__CFDictionary}C}24^@32"
- "FTABFile"
- "FTABSubfile"
- "HelsinkiRestore-56.3.2"
- "T@\"FTABSubfile\",R,V_manifest"
- "VinylRestore-78~6396"
- "failed to open file for writing: %s"
- "libauthinstall_device-1033.80.3"
- "path: %s"
- "{}"

```
