## ViceroyTrace

> `/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ViceroyTrace.framework/ViceroyTrace`

```diff

-2145.50.1.0.0
-  __TEXT.__text: 0xacb24
+2145.53.2.0.0
+  __TEXT.__text: 0xacbe4
   __TEXT.__auth_stubs: 0xd60
-  __TEXT.__objc_methlist: 0x8ca8
+  __TEXT.__objc_methlist: 0x8cb0
   __TEXT.__const: 0x2478
-  __TEXT.__cstring: 0xe7ea
+  __TEXT.__cstring: 0xe81f
   __TEXT.__oslogstring: 0xc59e
   __TEXT.__gcc_except_tab: 0x3b4
   __TEXT.__dlopen_cstrs: 0xa0
-  __TEXT.__unwind_info: 0x1688
+  __TEXT.__unwind_info: 0x1690
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0x599
-  __TEXT.__objc_methname: 0x1b8a7
+  __TEXT.__objc_methname: 0x1b941
   __TEXT.__objc_methtype: 0x240f
-  __TEXT.__objc_stubs: 0xec60
+  __TEXT.__objc_stubs: 0xeca0
   __DATA_CONST.__got: 0x238
   __DATA_CONST.__const: 0xd68
   __DATA_CONST.__objc_classlist: 0x1d0
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4278
+  __DATA_CONST.__objc_selrefs: 0x4288
   __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_arraydata: 0x220
   __AUTH_CONST.__auth_got: 0x6c0
   __AUTH_CONST.__const: 0x280
-  __AUTH_CONST.__cfstring: 0xdc80
-  __AUTH_CONST.__objc_const: 0x166e8
+  __AUTH_CONST.__cfstring: 0xdce0
+  __AUTH_CONST.__objc_const: 0x16718
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__objc_intobj: 0x468
+  __AUTH_CONST.__objc_intobj: 0x480
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x1ff0
-  __DATA.__data: 0x698
-  __DATA.__bss: 0x70
+  __DATA.__objc_ivar: 0x1ff4
+  __DATA.__data: 0x670
+  __DATA.__bss: 0x78
   __DATA.__common: 0x1
   __DATA_DIRTY.__objc_data: 0x1040
-  __DATA_DIRTY.__data: 0x50
-  __DATA_DIRTY.__bss: 0x9a
+  __DATA_DIRTY.__data: 0x78
+  __DATA_DIRTY.__bss: 0x92
   __DATA_DIRTY.__common: 0x22
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 3AF4B7F7-43DB-3F58-ABD6-71407F6E34AD
-  Functions: 3933
-  Symbols:   12963
-  CStrings:  9199
+  UUID: 3AC1DE67-9709-329D-B628-EA9B95F230DE
+  Functions: 3942
+  Symbols:   12980
+  CStrings:  9209
 
Symbols:
+ -[VCAggregatorMultiway hdCaptureBenefitDistribution]
+ -[VCAggregatorMultiway hdCaptureDurationsMsec]
+ -[VCAggregatorMultiway processHDCaptureBenefitDistribution:]
+ -[VCAggregatorMultiway processHDCaptureEnabledWithPayload:withType:withTimestamp:]
+ -[VCAggregatorMultiway processHDCaptureEnabledWithPayload:withType:withTimestamp:].cold.1
+ _OBJC_IVAR_$_VCAggregatorMultiway._hdCaptureBenefitDistribution
+ __MergedGlobals.1000
+ _objc_msgSend$numberWithInteger:
+ _objc_msgSend$processHDCaptureBenefitDistribution:
+ _objc_msgSend$processHDCaptureEnabledWithPayload:withType:withTimestamp:
- -[VCAggregatorMultiway HDCaptureDurationsMsec]
- -[VCAggregatorMultiway processHDCaptureEnabledWithType:withTimestamp:]
- -[VCAggregatorMultiway processHDCaptureEnabledWithType:withTimestamp:].cold.1
- -[VCAggregatorMultiway setHDCaptureDurationsMsec:]
- _filterParams
- _gBacklightService
- _gPowerService
- _kN41FilterParams
- _kN94FilterParams
- _matchingSensors
- _objc_msgSend$processHDCaptureEnabledWithType:withTimestamp:
CStrings:
+ "-[VCAggregatorMultiway processHDCaptureEnabledWithPayload:withType:withTimestamp:]"
+ "T@\"NSMutableArray\",R,V_hdCaptureBenefitDistribution"
+ "T@\"NSMutableArray\",R,V_hdCaptureDurationsMsec"
+ "VTSCBD"
+ "VTxSCBenefitCount"
+ "VTxSCTotalCount"
+ "_hdCaptureBenefitDistribution"
+ "hdCaptureBenefitDistribution"
+ "hdCaptureDurationsMsec"
+ "numberWithInteger:"
+ "processHDCaptureBenefitDistribution:"
+ "processHDCaptureEnabledWithPayload:withType:withTimestamp:"
- "-[VCAggregatorMultiway processHDCaptureEnabledWithType:withTimestamp:]"
- "HDCaptureDurationsMsec"
- "T@\"NSMutableArray\",V_hdCaptureDurationsMsec"
- "processHDCaptureEnabledWithType:withTimestamp:"
- "setHDCaptureDurationsMsec:"

```
