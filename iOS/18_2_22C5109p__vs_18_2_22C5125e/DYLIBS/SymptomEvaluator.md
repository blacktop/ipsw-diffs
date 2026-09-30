## SymptomEvaluator

> `/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomEvaluator.framework/SymptomEvaluator`

```diff

-2001.60.15.0.0
-  __TEXT.__text: 0x2560d8
-  __TEXT.__auth_stubs: 0x22f0
-  __TEXT.__objc_methlist: 0x161c0
-  __TEXT.__cstring: 0x23182
+2001.60.17.0.0
+  __TEXT.__text: 0x254160
+  __TEXT.__auth_stubs: 0x22d0
+  __TEXT.__objc_methlist: 0x15ed8
+  __TEXT.__cstring: 0x231aa
   __TEXT.__const: 0xa78
   __TEXT.__gcc_except_tab: 0x51b4
-  __TEXT.__oslogstring: 0x3ff8b
+  __TEXT.__oslogstring: 0x3ffa7
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.evaluator_cfg: 0x634d
   __TEXT.default_clp: 0x2fe0
   __TEXT.symptoms_clp: 0x5f90
   __TEXT.network_clp: 0x4b40
-  __TEXT.baseband_clp: 0xee50
+  __TEXT.baseband_clp: 0xee70
   __TEXT.bb_MAV_clp: 0xa690
-  __TEXT.bb_INT_clp: 0x2f20
+  __TEXT.bb_INT_clp: 0x6360
   __TEXT.modules_clp: 0x16e0
-  __TEXT.__unwind_info: 0x6698
-  __TEXT.__objc_classname: 0x1cca
-  __TEXT.__objc_methname: 0x3b911
-  __TEXT.__objc_methtype: 0x66b2
-  __TEXT.__objc_stubs: 0x24c20
+  __TEXT.__unwind_info: 0x6688
+  __TEXT.__objc_classname: 0x1ca0
+  __TEXT.__objc_methname: 0x3b2c1
+  __TEXT.__objc_methtype: 0x65a9
+  __TEXT.__objc_stubs: 0x24aa0
   __DATA_CONST.__got: 0xde8
   __DATA_CONST.__const: 0x6500
-  __DATA_CONST.__objc_classlist: 0x830
+  __DATA_CONST.__objc_classlist: 0x828
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc4b8
+  __DATA_CONST.__objc_selrefs: 0xc340
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x578
+  __DATA_CONST.__objc_superrefs: 0x570
   __DATA_CONST.__objc_arraydata: 0x820
-  __AUTH_CONST.__auth_got: 0x1190
+  __AUTH_CONST.__auth_got: 0x1180
   __AUTH_CONST.__auth_ptr: 0x18
   __AUTH_CONST.__const: 0x2320
   __AUTH_CONST.__cfstring: 0x1bfa0
-  __AUTH_CONST.__objc_const: 0x3b8a0
+  __AUTH_CONST.__objc_const: 0x3b460
   __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__objc_dictobj: 0x8c0
   __AUTH_CONST.__objc_intobj: 0x750
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH.__objc_data: 0x1428
-  __DATA.__objc_ivar: 0x2c7c
+  __DATA.__objc_ivar: 0x2c44
   __DATA.__data: 0x1c00
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x320
   __DATA.__common: 0xb1
-  __DATA_DIRTY.__objc_data: 0x3db8
+  __DATA_DIRTY.__objc_data: 0x3d68
   __DATA_DIRTY.__data: 0xc8
   __DATA_DIRTY.__bss: 0x14a8
   __DATA_DIRTY.__common: 0x1a0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 10864
-  Symbols:   12172
-  CStrings:  22186
+  Functions: 10802
+  Symbols:   12109
+  CStrings:  22113
 
Symbols:
- _PBDataWriterWriteDataField
- _PBReaderReadData
CStrings:
+ "Failed to post LIM kernel metric"
+ "Posted LIM kernel metric: %!@(MISSING)"
+ "com.apple.symptoms.LowInternetModeKernelStats"
+ "limConnTimeoutPercent"
+ "limDLMaxBandwidthBps"
+ "limPacketLossPercent"
+ "limPacketOOOPercent"
+ "limRTTVarianceMilliseconds"
+ "limULMaxBandwidthBps"
- "AWDSymptomsNetworkLowInternetModeRecord"
- "Posting AWD LIM Kernel metric: %!@(MISSING)"
- "T@\"NSData\",&,N,V_limSignature"
- "TI,N,V_limDLDetected"
- "TI,N,V_limInterfaceType"
- "TI,N,V_limULDetected"
- "TQ,N,V_limConnTimeoutRatePercent"
- "TQ,N,V_limDLMaxBWBps"
- "TQ,N,V_limPacketLossRatePercent"
- "TQ,N,V_limPacketOOORatePercent"
- "TQ,N,V_limRTTAvgMilliseconds"
- "TQ,N,V_limRTTMinMilliseconds"
- "TQ,N,V_limRTTVarMilliseconds"
- "TQ,N,V_limULMaxBWBps"
- "_limConnTimeoutRatePercent"
- "_limDLDetected"
- "_limDLMaxBWBps"
- "_limInterfaceType"
- "_limPacketLossRatePercent"
- "_limPacketOOORatePercent"
- "_limRTTAvgMilliseconds"
- "_limRTTMinMilliseconds"
- "_limRTTVarMilliseconds"
- "_limSignature"
- "_limULDetected"
- "_limULMaxBWBps"
- "hasLimConnTimeoutRatePercent"
- "hasLimDLDetected"
- "hasLimDLMaxBWBps"
- "hasLimInterfaceType"
- "hasLimPacketLossRatePercent"
- "hasLimPacketOOORatePercent"
- "hasLimRTTAvgMilliseconds"
- "hasLimRTTMinMilliseconds"
- "hasLimRTTVarMilliseconds"
- "hasLimSignature"
- "hasLimULDetected"
- "hasLimULMaxBWBps"
- "limConnTimeoutRatePercent"
- "limDLMaxBWBps"
- "limPacketLossRatePercent"
- "limPacketOOORatePercent"
- "limRTTVarMilliseconds"
- "limSignature"
- "limULMaxBWBps"
- "setHasLimConnTimeoutRatePercent:"
- "setHasLimDLDetected:"
- "setHasLimDLMaxBWBps:"
- "setHasLimInterfaceType:"
- "setHasLimPacketLossRatePercent:"
- "setHasLimPacketOOORatePercent:"
- "setHasLimRTTAvgMilliseconds:"
- "setHasLimRTTMinMilliseconds:"
- "setHasLimRTTVarMilliseconds:"
- "setHasLimULDetected:"
- "setHasLimULMaxBWBps:"
- "setLimConnTimeoutRatePercent:"
- "setLimDLDetected:"
- "setLimDLMaxBWBps:"
- "setLimInterfaceType:"
- "setLimPacketLossRatePercent:"
- "setLimPacketOOORatePercent:"
- "setLimRTTAvgMilliseconds:"
- "setLimRTTMinMilliseconds:"
- "setLimRTTVarMilliseconds:"
- "setLimSignature:"
- "setLimULDetected:"
- "setLimULMaxBWBps:"
- "{?=\"limConnTimeoutRatePercent\"b1\"limDLMaxBWBps\"b1\"limPacketLossRatePercent\"b1\"limPacketOOORatePercent\"b1\"limRTTAvgMilliseconds\"b1\"limRTTMinMilliseconds\"b1\"limRTTVarMilliseconds\"b1\"limULMaxBWBps\"b1\"timestamp\"b1\"limDLDetected\"b1\"limInterfaceType\"b1\"limULDetected\"b1}"
- "\xa1"

```
