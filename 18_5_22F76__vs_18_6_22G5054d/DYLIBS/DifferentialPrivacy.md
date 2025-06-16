## DifferentialPrivacy

> `/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/DifferentialPrivacy`

```diff

-659.120.10.0.0
-  __TEXT.__text: 0x5fb40
+659.140.5.0.0
+  __TEXT.__text: 0x5fb0c
   __TEXT.__auth_stubs: 0xef0
-  __TEXT.__objc_methlist: 0x5934
+  __TEXT.__objc_methlist: 0x5924
   __TEXT.__const: 0x830
-  __TEXT.__cstring: 0x2d00d
+  __TEXT.__cstring: 0x2cffd
   __TEXT.__oslogstring: 0x4333
   __TEXT.__gcc_except_tab: 0xd80
   __TEXT.__ustring: 0x578

   __TEXT.__unwind_info: 0x1828
   __TEXT.__eh_frame: 0x548
   __TEXT.__objc_classname: 0xdbb
-  __TEXT.__objc_methname: 0x9e32
+  __TEXT.__objc_methname: 0x9e15
   __TEXT.__objc_methtype: 0x12fe
   __TEXT.__objc_stubs: 0x7fe0
   __DATA_CONST.__got: 0x7a8

   __AUTH_CONST.__auth_got: 0x790
   __AUTH_CONST.__const: 0x5a0
   __AUTH_CONST.__cfstring: 0x9e460
-  __AUTH_CONST.__objc_const: 0xafc8
+  __AUTH_CONST.__objc_const: 0xaf98
   __AUTH_CONST.__objc_intobj: 0x74988
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0xbe0
   __AUTH.__data: 0x118
-  __DATA.__objc_ivar: 0x55c
+  __DATA.__objc_ivar: 0x558
   __DATA.__data: 0x958
   __DATA.__bss: 0x750
   __DATA.__common: 0x18

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 66C36BDF-D48F-320D-8072-C5F1ECB9C6AB
-  Functions: 2408
-  Symbols:   7878
-  CStrings:  42958
+  UUID: 3B6E1CFC-A935-3749-AF6A-A40B713051D3
+  Functions: 2407
+  Symbols:   7875
+  CStrings:  42957
 
Symbols:
+ _objc_msgSend$sendLogWithKey:taskExpiration:minBatchSize:targetCentralEpsilon:targetCentralDelta:localEpsilon:privateAccessToken:ohttp:
- -[_DPAppleIntelligenceReportParameters dimension]
- _OBJC_IVAR_$__DPAppleIntelligenceReportParameters._dimension
- _objc_msgSend$sendLogWithKey:dimension:taskExpiration:minBatchSize:targetCentralEpsilon:targetCentralDelta:localEpsilon:privateAccessToken:ohttp:
Functions:
~ -[_DPAppleIntelligenceReportParameters initWithDonation:] : 532 -> 520
- -[_DPAppleIntelligenceReportParameters ohttp]
~ -[_DPSymmetricRAPPORInternalBuildBudgetAuditor initWithMetadata:plistParameters:error:] : 876 -> 868
~ -[_DPHistogramWithAggregatorDiscreteGaussianBudgetAuditor initWithMetadata:plistParameters:error:] : 1460 -> 1456
~ -[_DPAppleIntelligenceTransparencyLog writeToDiskWithError:] : 584 -> 564
CStrings:
+ "sendLogWithKey:taskExpiration:minBatchSize:targetCentralEpsilon:targetCentralDelta:localEpsilon:privateAccessToken:ohttp:"
+ "v68@0:8@16Q24I32d36d44d52B60B64"
- "TI,R,N,V_dimension"
- "sendLogWithKey:dimension:taskExpiration:minBatchSize:targetCentralEpsilon:targetCentralDelta:localEpsilon:privateAccessToken:ohttp:"
- "v72@0:8@16I24Q28I36d40d48d56B64B68"

```
