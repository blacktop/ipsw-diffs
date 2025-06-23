## BatteryIntelligence

> `/System/Library/PrivateFrameworks/BatteryIntelligence.framework/BatteryIntelligence`

```diff

-155.0.0.502.2
-  __TEXT.__text: 0x4e00
+160.0.0.0.0
+  __TEXT.__text: 0x4e44
   __TEXT.__auth_stubs: 0x440
   __TEXT.__objc_methlist: 0x7c4
   __TEXT.__const: 0xa0
-  __TEXT.__cstring: 0x5fa
+  __TEXT.__cstring: 0x61a
   __TEXT.__oslogstring: 0x3ed
   __TEXT.__gcc_except_tab: 0x264
   __TEXT.__unwind_info: 0x248
   __TEXT.__objc_classname: 0x1ba
-  __TEXT.__objc_methname: 0x10e2
-  __TEXT.__objc_methtype: 0x36e
+  __TEXT.__objc_methname: 0x10d7
+  __TEXT.__objc_methtype: 0x360
   __TEXT.__objc_stubs: 0xd80
   __DATA_CONST.__got: 0xd8
   __DATA_CONST.__const: 0x1c0

   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x230
   __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0x400
+  __AUTH_CONST.__cfstring: 0x420
   __AUTH_CONST.__objc_const: 0x1308
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x30

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DEC22E48-BA90-342F-BA08-1F39F729747D
+  UUID: 961542B2-3209-316A-A61E-C26D195FBFC1
   Functions: 178
   Symbols:   782
-  CStrings:  391
+  CStrings:  392
 
Symbols:
+ -[BIBatteryAnalysisClient formattedEstimateForOutput:]
+ ___38-[BIBatteryAnalysisManagerClient init]_block_invoke.172
+ ___38-[BIBatteryAnalysisManagerClient init]_block_invoke.172.cold.1
+ ___43-[BIBatteryAnalysisClient initWithTargets:]_block_invoke.87
+ ___43-[BIBatteryAnalysisClient initWithTargets:]_block_invoke.87.cold.1
+ ___43-[BIBatteryAnalysisClient initWithTargets:]_block_invoke.89
+ ___51-[BIBatteryAnalysisClient updateEstimateForTarget:]_block_invoke.92
+ ___51-[BIBatteryAnalysisClient updateEstimateForTarget:]_block_invoke.92.cold.1
+ ___52-[BIBatteryAnalysisManagerClient adHocRunWithError:]_block_invoke.176
+ ___52-[BIBatteryAnalysisManagerClient adHocRunWithError:]_block_invoke.176.cold.1
+ ___70-[BIBatteryAnalysisManagerClient updateTarget:withEstimate:withError:]_block_invoke.174
+ ___70-[BIBatteryAnalysisManagerClient updateTarget:withEstimate:withError:]_block_invoke.174.cold.1
+ _objc_msgSend$formattedEstimateForOutput:
- -[BIBatteryAnalysisClient formattedEstimateForOutput:withTarget:]
- ___38-[BIBatteryAnalysisManagerClient init]_block_invoke.169
- ___38-[BIBatteryAnalysisManagerClient init]_block_invoke.169.cold.1
- ___43-[BIBatteryAnalysisClient initWithTargets:]_block_invoke.84
- ___43-[BIBatteryAnalysisClient initWithTargets:]_block_invoke.84.cold.1
- ___43-[BIBatteryAnalysisClient initWithTargets:]_block_invoke.86
- ___51-[BIBatteryAnalysisClient updateEstimateForTarget:]_block_invoke.89
- ___51-[BIBatteryAnalysisClient updateEstimateForTarget:]_block_invoke.89.cold.1
- ___52-[BIBatteryAnalysisManagerClient adHocRunWithError:]_block_invoke.173
- ___52-[BIBatteryAnalysisManagerClient adHocRunWithError:]_block_invoke.173.cold.1
- ___70-[BIBatteryAnalysisManagerClient updateTarget:withEstimate:withError:]_block_invoke.171
- ___70-[BIBatteryAnalysisManagerClient updateTarget:withEstimate:withError:]_block_invoke.171.cold.1
- _objc_msgSend$formattedEstimateForOutput:withTarget:
Functions:
~ -[BIBatteryAnalysisClient estimateFromCache:withError:] : 1136 -> 1124
~ -[BIBatteryAnalysisClient formattedEstimateForOutput:withTarget:] -> -[BIBatteryAnalysisClient formattedEstimateForOutput:] : 364 -> 444
CStrings:
+ "CHARGE_TIME_LESS_THAN_THRESHOLD"
+ "formattedEstimateForOutput:"
- "@32@0:8@16q24"
- "formattedEstimateForOutput:withTarget:"

```
