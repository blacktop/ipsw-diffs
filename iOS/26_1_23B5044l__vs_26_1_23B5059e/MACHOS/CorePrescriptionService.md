## CorePrescriptionService

> `/System/Library/PrivateFrameworks/CorePrescription.framework/XPCServices/CorePrescriptionService.xpc/CorePrescriptionService`

```diff

 207.0.35.0.0
-  __TEXT.__text: 0x7a5f4
+  __TEXT.__text: 0x7e10c
   __TEXT.__auth_stubs: 0x1be0
   __TEXT.__objc_stubs: 0x600
-  __TEXT.__objc_methlist: 0x1458
-  __TEXT.__const: 0xab78
-  __TEXT.__objc_methname: 0x1fd4
+  __TEXT.__objc_methlist: 0x1658
+  __TEXT.__const: 0xae58
+  __TEXT.__objc_methname: 0x22d0
   __TEXT.__objc_classname: 0xec
   __TEXT.__objc_methtype: 0x5e8
-  __TEXT.__cstring: 0x47f3
-  __TEXT.__oslogstring: 0xf18
+  __TEXT.__cstring: 0x4ec3
+  __TEXT.__oslogstring: 0xfb8
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x1b6c
-  __TEXT.__swift5_typeref: 0x1154
-  __TEXT.__swift5_builtin: 0x168
-  __TEXT.__swift5_reflstr: 0x1653
-  __TEXT.__swift5_fieldmd: 0x1694
-  __TEXT.__swift5_assocty: 0x330
-  __TEXT.__swift5_proto: 0x350
-  __TEXT.__swift5_types: 0x17c
+  __TEXT.__constg_swiftt: 0x1cd4
+  __TEXT.__swift5_typeref: 0x11c6
+  __TEXT.__swift5_builtin: 0x190
+  __TEXT.__swift5_reflstr: 0x18a3
+  __TEXT.__swift5_fieldmd: 0x17ec
+  __TEXT.__swift5_assocty: 0x360
+  __TEXT.__swift5_proto: 0x370
+  __TEXT.__swift5_types: 0x18c
   __TEXT.__swift5_mpenum: 0x18
   __TEXT.__swift5_protos: 0x10
-  __TEXT.__swift5_capture: 0x90c
-  __TEXT.__swift_as_entry: 0x1a8
-  __TEXT.__swift_as_ret: 0x210
-  __TEXT.__unwind_info: 0x2258
-  __TEXT.__eh_frame: 0x4c78
+  __TEXT.__swift5_capture: 0xa10
+  __TEXT.__swift_as_entry: 0x1cc
+  __TEXT.__swift_as_ret: 0x238
+  __TEXT.__unwind_info: 0x2448
+  __TEXT.__eh_frame: 0x5030
   __DATA_CONST.__auth_got: 0xdf8
-  __DATA_CONST.__got: 0x520
-  __DATA_CONST.__auth_ptr: 0x638
-  __DATA_CONST.__const: 0x2aa0
+  __DATA_CONST.__got: 0x528
+  __DATA_CONST.__auth_ptr: 0x648
+  __DATA_CONST.__const: 0x2de0
   __DATA_CONST.__cfstring: 0x2c0
-  __DATA_CONST.__objc_classlist: 0x190
+  __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x30
-  __DATA.__objc_const: 0x4ac0
-  __DATA.__objc_selrefs: 0xa30
+  __DATA.__objc_const: 0x4f20
+  __DATA.__objc_selrefs: 0xae0
   __DATA.__objc_ivar: 0x80
-  __DATA.__objc_data: 0x16b0
-  __DATA.__data: 0x30f8
-  __DATA.__bss: 0x6820
+  __DATA.__objc_data: 0x1938
+  __DATA.__data: 0x31e0
+  __DATA.__bss: 0x6c20
   __DATA.__common: 0x20c
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C6114AB4-B744-3873-B424-3A0A31B010A2
-  Functions: 2669
-  Symbols:   462
-  CStrings:  1237
+  UUID: 03718507-AEA0-3FF1-962C-06ED5A68AE21
+  Functions: 2826
+  Symbols:   466
+  CStrings:  1317
 
Symbols:
+ _OBJC_CLASS_$_CRXCEyePrismCorrection
+ _OBJC_CLASS_$_CRXCPrismCorrection
+ _OBJC_METACLASS_$_CRXCEyePrismCorrection
+ _OBJC_METACLASS_$_CRXCPrismCorrection
CStrings:
+ ", prismActivationLocation: "
+ "@\"CRXCEyePrismCorrection\""
+ "@112@0:8Q16Q24Q32B40Q44Q52q60Q68q76B84@88@96q104"
+ "@40@0:8@16@24q32"
+ "@48@0:8q16d24q32d40"
+ "CorePrescriptionService.CRXCEyePrismCorrection"
+ "CorePrescriptionService.CRXCPrismCorrection"
+ "Invalid prism data"
+ "T@\"CRXCEyePrismCorrection\",N,R,VprismOD"
+ "T@\"CRXCEyePrismCorrection\",N,R,VprismOS"
+ "TQ,N,VhorizPrismID"
+ "TQ,N,VvertPrismID"
+ "Td,N,R,VhorizontalAmount"
+ "Td,N,R,VverticalAmount"
+ "Tq,N,R,VhorizontalBaseDirection"
+ "Tq,N,R,Vtype"
+ "Tq,N,R,VverticalBaseDirection"
+ "Tq,N,VhorizPrismBaseDir"
+ "Tq,N,VvertPrismBaseDir"
+ "fetchPrismCorrection(forUUID:inGroup:)"
+ "fetchPrismCorrectionForUUID:inGroup:completionHandler:"
+ "getPrismActivationLocation()"
+ "getPrismActivationLocationWithCompletionHandler:"
+ "getPrismActivationStatus()"
+ "getPrismActivationStatusWithCompletionHandler:"
+ "horizPrismBaseDir"
+ "horizPrismID"
+ "horizontalAmount"
+ "horizontalBaseDirection"
+ "initWithHorizontalBaseDirection:horizontalAmount:verticalBaseDirection:verticalAmount:"
+ "initWithPrismOD:prismOS:type:"
+ "initWithRxID:axisID:rxOffsetID:cylinderSignFlipped:calibratedRXID:horizPrismID:horizPrismBaseDir:vertPrismID:vertPrismBaseDir:outOfRange:displayValues:calibrationValues:clampingStatus:"
+ "prismActivationLocation"
+ "prismActivationRegion"
+ "prismData2"
+ "prismDataTables"
+ "prismHorizontalBaseDirLeft"
+ "prismHorizontalBaseDirRight"
+ "prismHorizontalValueLeft"
+ "prismHorizontalValueRight"
+ "prismOD"
+ "prismOS"
+ "prismType"
+ "prismVerticalBaseDirLeft"
+ "prismVerticalBaseDirRight"
+ "prismVerticalValueLeft"
+ "prismVerticalValueRight"
+ "seaUrchin"
+ "seaUrchinActivationLocation"
+ "setHorizPrismBaseDir:"
+ "setHorizPrismID:"
+ "setVertPrismBaseDir:"
+ "setVertPrismID:"
+ "updatePrismCorrection(_:forUUID:inGroup:)"
+ "updatePrismCorrection:forUUID:inGroup:completionHandler:"
+ "v24@0:8@?<v@?B@\"NSString\"@\"NSError\">16"
+ "v40@0:8@\"NSString\"16q24@?<v@?@\"CRXCPrismCorrection\"@\"NSError\">32"
+ "v40@0:8@16q24@?32"
+ "v48@0:8@\"CRXCPrismCorrection\"16@\"NSString\"24q32@?<v@?@\"NSError\">40"
+ "v48@0:8@16@24q32@?40"
+ "vertPrismBaseDir"
+ "vertPrismID"
+ "verticalAmount"
+ "verticalBaseDirection"

```
