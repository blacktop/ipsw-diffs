## lockdownd

> `/usr/libexec/lockdownd`

```diff

-1329.100.2.0.0
-  __TEXT.__text: 0x10ae20
+1329.120.9.502.1
+  __TEXT.__text: 0x10b8c8
   __TEXT.__auth_stubs: 0x2d40
-  __TEXT.__objc_stubs: 0x43e0
+  __TEXT.__objc_stubs: 0x4400
   __TEXT.__objc_methlist: 0x3520
-  __TEXT.__cstring: 0x5013f
+  __TEXT.__cstring: 0x50a1d
   __TEXT.__const: 0x161f0
   __TEXT.__oslogstring: 0x788
-  __TEXT.__gcc_except_tab: 0x3d48
+  __TEXT.__gcc_except_tab: 0x3d28
   __TEXT.__objc_classname: 0xbbd
-  __TEXT.__objc_methname: 0x4774
+  __TEXT.__objc_methname: 0x4784
   __TEXT.__objc_methtype: 0xeb1
   __TEXT.__services: 0x2d8f
-  __TEXT.__unwind_info: 0x3008
+  __TEXT.__unwind_info: 0x3020
   __TEXT.__eh_frame: 0x10a0
   __DATA_CONST.__auth_got: 0x16b8
   __DATA_CONST.__got: 0x680
   __DATA_CONST.__auth_ptr: 0x60
-  __DATA_CONST.__const: 0xadb8
-  __DATA_CONST.__cfstring: 0x18260
+  __DATA_CONST.__const: 0xadd8
+  __DATA_CONST.__cfstring: 0x18320
   __DATA_CONST.__objc_classlist: 0x280
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA.__objc_const: 0x6128
-  __DATA.__objc_selrefs: 0x14a0
+  __DATA.__objc_selrefs: 0x14a8
   __DATA.__objc_ivar: 0x410
   __DATA.__objc_data: 0x1900
   __DATA.__data: 0x2d10

   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 3459
+  Functions: 3466
   Symbols:   931
-  CStrings:  9727
+  CStrings:  9773
 
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
+ "HUPolicyPrevPeSlc"
+ "HUPolicyPrevPeTlc"
+ "HUPolicySwitchPeGap"
+ "HUPolicySwitchPeInt"
+ "HUPolicySwitchPeMinSlc"
+ "HUPolicyWidthDown"
+ "HUPolicyWidthDown_"
+ "HUPolicyWidthUp"
+ "HUPolicyWidthUp_"
+ "HelsinkiRestore-56.5.1"
+ "Passcode changed (invalidating pair records as buddy is complete)."
+ "Passcode changed (skipping invalidation of pair records as feature is explicitly disabled)."
+ "Passcode changed (skipping invalidation of pair records as we're still in buddy)."
+ "Removing non-automation pair records because USB host disconnected while in Setup."
+ "Skipping upgrade key rolling as feature is disabled."
+ "VinylRestore-78~6980"
+ "cbdrHPScanHP"
+ "cbdrMPScanHP"
+ "cbdrMPScanMP"
+ "cbdrScanHP"
+ "cbdrScanMP"
+ "containsString:"
+ "destroy_all_non_automation_pair_records_block_invoke_2"
+ "gcMustReasons"
+ "gcMustReasons_"
+ "is_automation_pair_record"
+ "kern.bootargs"
+ "on_queue_destroy_pair_record"
+ "skip-lockdown-pair-record-rolling=1"
+ "usb_host_disconnected"
- "ASPFTLParseBufferToCxt: powerDownTime(1190): (#12) cfg elements != (%d) buffer elements"
- "ASPFTLParseBufferToCxt: powerDownTime(1190): Cannot add 12 elements to context"
- "HelsinkiRestore-56.4.13"
- "VinylRestore-78~6885"
- "destroy_pair_record_block_invoke"
- "perform_migration_block_invoke"

```
