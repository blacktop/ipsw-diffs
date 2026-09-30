## ASPCarryLog

> `/usr/libexec/ASPCarryLog`

```diff

-616.100.11.0.0
-  __TEXT.__text: 0x47134
+616.120.4.0.0
+  __TEXT.__text: 0x47934
   __TEXT.__auth_stubs: 0xc10
   __TEXT.__objc_stubs: 0x30a0
   __TEXT.__objc_methlist: 0x14e8
   __TEXT.__gcc_except_tab: 0x58c
-  __TEXT.__cstring: 0x419c3
+  __TEXT.__cstring: 0x42301
   __TEXT.__const: 0x270
   __TEXT.__objc_methname: 0x3325
   __TEXT.__oslogstring: 0x12b8

   __DATA_CONST.__got: 0x1d8
   __DATA_CONST.__auth_ptr: 0x60
   __DATA_CONST.__const: 0x398
-  __DATA_CONST.__cfstring: 0x21d80
+  __DATA_CONST.__cfstring: 0x222e0
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_intobj: 0x10f8
-  __DATA_CONST.__objc_arraydata: 0x11308
+  __DATA_CONST.__objc_arraydata: 0x115b8
   __DATA_CONST.__objc_dictobj: 0x190
   __DATA_CONST.__objc_arrayobj: 0x390
   __DATA.__objc_const: 0x1ea8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/local/lib/libNVMeCTL.dylib
-  Functions: 613
+  Functions: 611
   Symbols:   267
-  CStrings:  8129
+  CStrings:  8198
 
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
+ "HUPolicyWidthDown_0"
+ "HUPolicyWidthDown_1"
+ "HUPolicyWidthDown_2"
+ "HUPolicyWidthDown_3"
+ "HUPolicyWidthDown_4"
+ "HUPolicyWidthDown_5"
+ "HUPolicyWidthUp_"
+ "HUPolicyWidthUp_0"
+ "HUPolicyWidthUp_1"
+ "HUPolicyWidthUp_2"
+ "HUPolicyWidthUp_3"
+ "HUPolicyWidthUp_4"
+ "HUPolicyWidthUp_5"
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
+ "gcMustReasons_0"
+ "gcMustReasons_1"
+ "gcMustReasons_10"
+ "gcMustReasons_11"
+ "gcMustReasons_12"
+ "gcMustReasons_13"
+ "gcMustReasons_14"
+ "gcMustReasons_15"
+ "gcMustReasons_16"
+ "gcMustReasons_17"
+ "gcMustReasons_18"
+ "gcMustReasons_19"
+ "gcMustReasons_2"
+ "gcMustReasons_3"
+ "gcMustReasons_4"
+ "gcMustReasons_5"
+ "gcMustReasons_6"
+ "gcMustReasons_7"
+ "gcMustReasons_8"
+ "gcMustReasons_9"
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
- "powerDownTime_11"

```
