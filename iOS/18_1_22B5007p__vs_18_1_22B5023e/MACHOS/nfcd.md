## nfcd

> `/usr/libexec/nfcd`

```diff

-350.30.0.0.0
-  __TEXT.__text: 0x25ce54
-  __TEXT.__auth_stubs: 0x17b0
-  __TEXT.__delay_helper: 0xc8
-  __TEXT.__objc_stubs: 0xd440
-  __TEXT.__objc_methlist: 0x75f4
-  __TEXT.__const: 0x1190
-  __TEXT.__oslogstring: 0x237b2
-  __TEXT.__cstring: 0x2d411
+351.1.0.0.0
+  __TEXT.__text: 0x25e9ac
+  __TEXT.__auth_stubs: 0x17c0
+  __TEXT.__delay_helper: 0xec
+  __TEXT.__objc_stubs: 0xd480
+  __TEXT.__objc_methlist: 0x75fc
+  __TEXT.__const: 0x11a0
+  __TEXT.__oslogstring: 0x237df
+  __TEXT.__cstring: 0x2d655
   __TEXT.__objc_classname: 0x1b3e
-  __TEXT.__objc_methname: 0x1640f
-  __TEXT.__objc_methtype: 0x513f
-  __TEXT.__gcc_except_tab: 0x75d0
+  __TEXT.__objc_methname: 0x164ed
+  __TEXT.__objc_methtype: 0x5177
+  __TEXT.__gcc_except_tab: 0x7570
   __TEXT.__dlopen_cstrs: 0x549
-  __TEXT.__unwind_info: 0x35d8
-  __DATA_CONST.__auth_got: 0xbe8
-  __DATA_CONST.__got: 0x420
-  __DATA_CONST.__const: 0x7610
-  __DATA_CONST.__cfstring: 0xfee0
+  __TEXT.__unwind_info: 0x35e0
+  __DATA_CONST.__auth_got: 0xbf0
+  __DATA_CONST.__got: 0x428
+  __DATA_CONST.__const: 0x7660
+  __DATA_CONST.__cfstring: 0x10120
   __DATA_CONST.__objc_classlist: 0x598
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x368
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x1b0
   __DATA_CONST.__objc_superrefs: 0x3e8
-  __DATA_CONST.__objc_intobj: 0x67f8
+  __DATA_CONST.__objc_intobj: 0x68a0
   __DATA_CONST.__objc_arraydata: 0x1df0
   __DATA_CONST.__objc_arrayobj: 0x378
   __DATA_CONST.__objc_dictobj: 0xf28
-  __DATA.__objc_const: 0x16580
-  __DATA.__objc_selrefs: 0x5100
+  __DATA.__objc_const: 0x165a0
+  __DATA.__objc_selrefs: 0x5138
   __DATA.__objc_ivar: 0xf20
   __DATA.__objc_data: 0x37f0
   __DATA.__data: 0x2990

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4282
-  Symbols:   521
-  CStrings:  11889
+  Functions: 4290
+  Symbols:   523
+  CStrings:  11918
 
Symbols:
+ _NFDriverGetReaderProhibitTimer
+ _OBJC_CLASS_$_SESExpress
CStrings:
+ " ; "
+ "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) SERmRunning=%!d(MISSING), HostRMRunning=%!d(MISSING), remainingTime=%!d(MISSING)"
+ "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) SERmRunning=%!d(MISSING), HostRMRunning=%!d(MISSING), remainingTime=%!d(MISSING)"
+ "Failed to request AC decrement timer: 0x%!X(MISSING)"
+ "Failed to request timer running Status: 0x%!X(MISSING)"
+ "Flash page write exceeded %!@(MISSING)"
+ "GetReaderProhibitTimer"
+ "NFCD built from (B&I) Stockholm_Base-351.1"
+ "Q24@0:8^B16"
+ "Vv24@0:8@?<v@?BBI@\"NSError\">16"
+ "Vv28@0:8I16@?<v@?qB@\"NSDictionary\"@\"NSArray\">20"
+ "_openDriver:"
+ "_sync_getReaderProhibitTimer:"
+ "aliroFastTxAttempted"
+ "aliroStandardTxAttempted"
+ "aliroStepUpTxAttempted"
+ "aliroSuccessfulFastTx"
+ "aliroSuccessfulStandardTx"
+ "aliroSuccessfulStepUpTx"
+ "com.apple.sts.dailyHomeHydraDeviceStatistics"
+ "com.apple.sts.dailyHomeHydraTransactionStatistics"
+ "expressModesInfoWithOption:completion:"
+ "getReaderProhibitTimer:"
+ "getReaderProhibitTimerInfo:"
+ "postAnalyticsSEFailureEvent:context:error:"
+ "processConfigurationChange:newConfiguration:"
+ "uaFastTxAttempted"
+ "uaStandardTxAttempted"
+ "uaStepUpTxAttempted"
+ "uaSuccessfulFastTx"
+ "uaSuccessfulStandardTx"
+ "uaSuccessfulStepUpTx"
+ "v28@?0B8B12I16@\"NSError\"20"
- "Flash page write exceeded %!d(MISSING) was %!@(MISSING) is %!@(MISSING)"
- "NFCD built from (B&I) Stockholm_Base-350.30"
- "Vv24@0:8@?<v@?qB@\"NSDictionary\">16"
- "begin, erroe.code: %!d(MISSING)"

```
