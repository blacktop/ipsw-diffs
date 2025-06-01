## anomalydetectiond

> `/usr/libexec/anomalydetectiond`

```diff

-92.0.1.0.1
-  __TEXT.__text: 0x2e90f0
-  __TEXT.__auth_stubs: 0x1670
-  __TEXT.__objc_stubs: 0x8160
-  __TEXT.__objc_methlist: 0x7908
-  __TEXT.__objc_methname: 0xaa4a
-  __TEXT.__cstring: 0x17398
+92.0.1.0.4
+  __TEXT.__text: 0x2ec250
+  __TEXT.__auth_stubs: 0x1690
+  __TEXT.__objc_stubs: 0x8220
+  __TEXT.__objc_methlist: 0x7988
+  __TEXT.__objc_methname: 0xab9e
+  __TEXT.__cstring: 0x17588
   __TEXT.__objc_classname: 0xfc2
-  __TEXT.__objc_methtype: 0x54c3
-  __TEXT.__const: 0x74b7
-  __TEXT.__gcc_except_tab: 0xb4ec
-  __TEXT.__oslogstring: 0xb9ec
-  __TEXT.__unwind_info: 0xad7c
+  __TEXT.__objc_methtype: 0x552c
+  __TEXT.__const: 0x7667
+  __TEXT.__gcc_except_tab: 0xb5a8
+  __TEXT.__oslogstring: 0xbaa0
+  __TEXT.__unwind_info: 0xae3c
   __TEXT.__eh_frame: 0x6a8
-  __DATA_CONST.__auth_got: 0xb50
-  __DATA_CONST.__got: 0x400
+  __DATA_CONST.__auth_got: 0xb60
+  __DATA_CONST.__got: 0x408
   __DATA_CONST.__auth_ptr: 0x38
-  __DATA_CONST.__const: 0x1c740
-  __DATA_CONST.__cfstring: 0x5140
+  __DATA_CONST.__const: 0x1c930
+  __DATA_CONST.__cfstring: 0x5200
   __DATA_CONST.__objc_classlist: 0x468
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_classrefs: 0x598
-  __DATA_CONST.__objc_superrefs: 0x3f0
+  __DATA_CONST.__objc_superrefs: 0x3f8
   __DATA_CONST.__objc_intobj: 0x16e0
   __DATA_CONST.__objc_arraydata: 0x1a0
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x1b8
-  __DATA.__objc_const: 0x10848
-  __DATA.__objc_selrefs: 0x2868
-  __DATA.__objc_ivar: 0x8b0
+  __DATA.__objc_const: 0x10910
+  __DATA.__objc_selrefs: 0x28a0
+  __DATA.__objc_ivar: 0x8bc
   __DATA.__objc_data: 0x2c10
   __DATA.__data: 0x1fc0
   __DATA.__bss: 0x218

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 4C24AB9D-531B-37CB-9FE5-3A8D3DFA494D
-  Functions: 14317
-  Symbols:   509
-  CStrings:  8494
+  UUID: DBBE21FA-2F56-367F-B5A5-1BF90153FC05
+  Functions: 14392
+  Symbols:   512
+  CStrings:  8540
 
Symbols:
+ __ZNKSt9exception4whatEv
+ __ZdaPv
+ __ZnamSt19__type_descriptor_t
CStrings:
+ "%u mag100 %llu"
+ "@24@0:8r^{MagSample=ffffQ}16"
+ "Fastpath %s already opened."
+ "MagFp"
+ "TS,N,V_armedSecMartyLocal"
+ "TS,N,V_armedSecMartyRemote"
+ "T^{MagSample=ffffQ},R,N"
+ "Ti,N,V_martyArmedSecondsLocal"
+ "Ti,N,V_martyArmedSecondsRemote"
+ "^{MagSample=ffffQ}16@0:8"
+ "_armedSecMartyLocal"
+ "_armedSecMartyRemote"
+ "_martyArmedSecondsLocal"
+ "_martyArmedSecondsRemote"
+ "armedSecMartyLocal"
+ "armedSecMartyRemote"
+ "avgRelOmegaRps"
+ "clients %d %d %d %d"
+ "closing fastpaths"
+ "firstRingSensorTimeStampMicroSeconds"
+ "initWithStruct:"
+ "isExtendedPretriggerDMDevice"
+ "isExtendedPretriggerMagDevice"
+ "kappa sec %d marty local %d remote %d bicycle %d"
+ "martyArmedSecondsLocal"
+ "martyArmedSecondsRemote"
+ "medianBufferNumSamples"
+ "medianNorthAlignmentEstimateRad"
+ "newNorthAlignmentEstimateRad"
+ "numCrashesDetectedAllSessionsCycle"
+ "numCrashesDetectedAllSessionsMotorbike"
+ "numRingSensorSamples"
+ "opening fastpaths"
+ "opening fastpaths device %p"
+ "overrideModeBitmap"
+ "pencilFusionDMYawAlignmentUpdate"
+ "pencilFusionRingSensorTrustModelUpdate"
+ "receiving marty upload request uuid %{public}s %{public}d"
+ "requestCompanionUpload:"
+ "reset fastpaths"
+ "ringSensorTrustModelMode"
+ "sending marty upload request uuid %{public}s %{public}d"
+ "setArmedSecMartyLocal:"
+ "setArmedSecMartyRemote:"
+ "setMartyArmedSecondsLocal:"
+ "setMartyArmedSecondsRemote:"
+ "setting fastpaths device %p"
+ "timeElapsedSinceLastUpdateMicroSeconds"
+ "totalDrivingTimeMotorcycleLocal"
+ "totalDrivingTimeMotorcycleRemote"
+ "trustPencilRingSensorBool"
+ "uploadReason"
+ "{MagSample=\"x\"f\"y\"f\"z\"f\"temperature\"f\"timestamp\"Q}"
- "Ignoring trigger because fastpath is invalid"
- "TS,N,V_armedSecMarty"
- "Ti,N,V_martyArmedSeconds"
- "_armedSecMarty"
- "_martyArmedSeconds"
- "armedSecMarty"
- "clients %d %d %d"
- "receiving marty upload request uuid %{public}s"
- "requestCompanionUpload"
- "sending marty upload request uuid %{public}s"
- "setArmedSecMarty:"
- "setMartyArmedSeconds:"

```
