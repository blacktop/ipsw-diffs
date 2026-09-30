## sysdiagnose_helper

> `/usr/libexec/sysdiagnose_helper`

```diff

-1438.100.41.0.0
-  __TEXT.__text: 0x3ee70
+1438.120.5.0.0
+  __TEXT.__text: 0x3f4d0
   __TEXT.__auth_stubs: 0xdb0
   __TEXT.__objc_stubs: 0x19c0
   __TEXT.__objc_methlist: 0x738
   __TEXT.__const: 0x3a8
-  __TEXT.__cstring: 0x43741
+  __TEXT.__cstring: 0x43e62
   __TEXT.__objc_methname: 0x1b3a
   __TEXT.__oslogstring: 0x2243
   __TEXT.__objc_classname: 0x132

   - /usr/lib/libtailspin.dylib
   - /usr/lib/libtzupdate.dylib
   - @rpath/CoreRepairCore.framework/Versions/A/CoreRepairCore
-  Functions: 349
+  Functions: 348
   Symbols:   295
-  CStrings:  5386
+  CStrings:  5424
 
CStrings:
+ "ASPFTLParseBufferToCxt: BP_readThrottleActualSize(1410) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: BP_readThrottleEngagedCnt(1409) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: HUPolicyPrevPeSlc(1230) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: HUPolicyPrevPeTlc(1231) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: HUPolicySwitchPeGap(1227) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: HUPolicySwitchPeInt(1226) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: HUPolicySwitchPeMinSlc(1225) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: HUPolicyWidthDown(1228): (#6) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: HUPolicyWidthDown(1228): Cannot add 6 elements to context"
+ "ASPFTLParseBufferToCxt: HUPolicyWidthUp(1229): (#6) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: HUPolicyWidthUp(1229): Cannot add 6 elements to context"
+ "ASPFTLParseBufferToCxt: cbdrHPScanHP(1392) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: cbdrMPScanHP(1394) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: cbdrMPScanMP(1393) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: cbdrScanHP(1282) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: cbdrScanMP(1283) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: gcMustReasons(1362): (#20) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: gcMustReasons(1362): Cannot add 20 elements to context"
+ "ASPFTLParseBufferToCxt: powerDownTime(1190): (#11) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: powerDownTime(1190): Cannot add 11 elements to context"
+ "BP_readThrottleActualSize"
+ "BP_readThrottleEngagedCnt"
+ "HUPolicyWidthDown_"
+ "HUPolicyWidthUp_"
+ "SleepAllVotes"
+ "SleepForcedShutdowns"
+ "SleepMaximumNoVoteSeconds"
+ "SleepNoHisto"
+ "SleepNoVotes"
+ "SleepTimeOuts"
+ "SleepWillNotSleepsNotUs"
+ "cbdrSlcForcedRefreshes"
+ "crossTempFinishScan"
+ "gcMustReasons_"
+ "invalidTemp"
+ "msPerThrottleZone"
+ "oSlcAllGo"
+ "readBlocksBelowHP"
+ "smsgDoubleErases"
+ "unhappyForceVertGC"
+ "unhappyForceWideGC1"
- "ASPFTLParseBufferToCxt: powerDownTime(1190): (#12) cfg elements != (%d) buffer elements"
- "ASPFTLParseBufferToCxt: powerDownTime(1190): Cannot add 12 elements to context"
- "activeTimeInThrottleZone"

```
