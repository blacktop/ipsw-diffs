## tccd

> `/System/Library/PrivateFrameworks/TCC.framework/Support/tccd`

```diff

-771.0.9.0.0
-  __TEXT.__text: 0x580ec
-  __TEXT.__auth_stubs: 0x1330
+780.0.9.0.0
+  __TEXT.__text: 0x586e0
+  __TEXT.__auth_stubs: 0x1340
   __TEXT.__objc_stubs: 0x7fe0
-  __TEXT.__objc_methlist: 0x36b0
-  __TEXT.__cstring: 0xa858
+  __TEXT.__objc_methlist: 0x3700
+  __TEXT.__cstring: 0xaa3d
   __TEXT.__const: 0x4f8
-  __TEXT.__gcc_except_tab: 0x129c
-  __TEXT.__objc_methname: 0xd4ee
-  __TEXT.__oslogstring: 0x9d5c
-  __TEXT.__objc_classname: 0x558
-  __TEXT.__objc_methtype: 0x1ba5
+  __TEXT.__gcc_except_tab: 0x1284
+  __TEXT.__objc_methname: 0xd61c
+  __TEXT.__oslogstring: 0x9dfd
+  __TEXT.__objc_classname: 0x568
+  __TEXT.__objc_methtype: 0x1bad
   __TEXT.__dlopen_cstrs: 0x47
-  __TEXT.__unwind_info: 0x1164
-  __DATA_CONST.__auth_got: 0x9a8
+  __TEXT.__unwind_info: 0x1168
+  __DATA_CONST.__auth_got: 0x9b0
   __DATA_CONST.__got: 0x180
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA_CONST.__const: 0x1b80
-  __DATA_CONST.__cfstring: 0x5ac0
-  __DATA_CONST.__objc_classlist: 0x170
+  __DATA_CONST.__const: 0x1bd0
+  __DATA_CONST.__cfstring: 0x5c00
+  __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x420
-  __DATA_CONST.__objc_arraydata: 0xb10
+  __DATA_CONST.__objc_classrefs: 0x2a0
+  __DATA_CONST.__objc_superrefs: 0x138
+  __DATA_CONST.__objc_intobj: 0x438
+  __DATA_CONST.__objc_arraydata: 0xb80
   __DATA_CONST.__objc_arrayobj: 0x78
-  __DATA_CONST.__objc_dictobj: 0xac8
-  __DATA.__objc_const: 0x7dc8
-  __DATA.__objc_selrefs: 0x2538
-  __DATA.__objc_classrefs: 0x298
-  __DATA.__objc_superrefs: 0x138
-  __DATA.__objc_ivar: 0x528
-  __DATA.__objc_data: 0xe60
+  __DATA_CONST.__objc_dictobj: 0xb68
+  __DATA.__objc_const: 0x7ed8
+  __DATA.__objc_selrefs: 0x2568
+  __DATA.__objc_ivar: 0x534
+  __DATA.__objc_data: 0xeb0
   __DATA.__data: 0x600
   __DATA.__bss: 0x381
   __DATA.__common: 0x10

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 2150
-  Symbols:   414
-  CStrings:  4126
+  Functions: 2158
+  Symbols:   415
+  CStrings:  4158
 
Symbols:
+ _objc_retain_x10
CStrings:
+ "\x01\x13\x13"
+ "-[TCCDPlatform sendAnalyticsForAction:service:subjectIdentity:indirectObjectIdentity:authValue:includeV1AuthValue:v1AuthValue:authReason:desiredAuth:domainReason:promptType:function:]_block_invoke"
+ "GetIndirectRequestsOutstanding"
+ "GetIndirectRequestsOutstanding, indirect reuqests outstanding: %{public}llu"
+ "NSFinancialDataUsageDescription"
+ "SetIndrectRequesetsOutstanding"
+ "SetIndrectRequesetsOutstanding, requests: %{public}d"
+ "SurfaceIndirectOutstandingAlert"
+ "T@\"NSString\",?,R,C"
+ "TCCAccessCheckAuditToken"
+ "TCCDTapToRadar"
+ "Ti,V_indirectRequestsOutstanding"
+ "Tq,N,V_analyticsAction"
+ "_analyticsAction"
+ "_analyticsQueue"
+ "_indirectRequestsOutstanding"
+ "analyticsAction"
+ "com.apple.TCC.analytics_queue"
+ "function_name"
+ "has_prompted_for_allow"
+ "indirectRequestPipelineStalled"
+ "indirectRequestsOutstanding"
+ "kTCCServiceContactlessAccess"
+ "kTCCServiceFinancialData"
+ "kTCCServiceSecureElementAccess"
+ "kTCCServiceSensorKitHistoricalCardioMetrics"
+ "kTCCServiceSensorKitHistoricalMobilityMetrics"
+ "mchl2844ecab"
+ "result-decided-from-other-ways"
+ "sendAnalyticsForAction:service:subjectIdentity:indirectObjectIdentity:authValue:includeV1AuthValue:v1AuthValue:authReason:desiredAuth:domainReason:promptType:function:"
+ "setAnalyticsAction:"
+ "setIndirectRequestsOutstanding:"
+ "surfaceIndirectAlert:"
+ "v108@0:8q16@24@32@40Q48B56Q60Q68Q76@84q92@100"
- "\x13\x13"
- "-[TCCDPlatform sendAnalyticsForAction:service:subjectIdentity:indirectObjectIdentity:authValue:includeV1AuthValue:v1AuthValue:desiredAuth:domainReason:promptType:]_block_invoke"
- "A"
- "sendAnalyticsForAction:service:subjectIdentity:indirectObjectIdentity:authValue:includeV1AuthValue:v1AuthValue:desiredAuth:domainReason:promptType:"
- "v92@0:8q16@24@32@40Q48B56Q60Q68@76q84"

```
