## CoreRepairCore

> `/System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore`

```diff

-921.100.255.0.0
-  __TEXT.__text: 0x8e224
+921.100.263.0.0
+  __TEXT.__text: 0x8e23c
   __TEXT.__auth_stubs: 0x1660
   __TEXT.__objc_methlist: 0x3eb4
   __TEXT.__const: 0x828
-  __TEXT.__oslogstring: 0x976b
-  __TEXT.__cstring: 0x5ffa
+  __TEXT.__oslogstring: 0x97ac
+  __TEXT.__cstring: 0x600f
   __TEXT.__gcc_except_tab: 0x183c
-  __TEXT.__unwind_info: 0x15f0
+  __TEXT.__unwind_info: 0x15e8
   __TEXT.__objc_classname: 0x8af
-  __TEXT.__objc_methname: 0x86cd
-  __TEXT.__objc_methtype: 0x15dd
+  __TEXT.__objc_methname: 0x8721
+  __TEXT.__objc_methtype: 0x15fb
   __TEXT.__objc_stubs: 0x6c20
   __DATA_CONST.__got: 0x598
   __DATA_CONST.__const: 0x8d8

   __DATA_CONST.__objc_arraydata: 0xb70
   __AUTH_CONST.__auth_got: 0xb40
   __AUTH_CONST.__const: 0x520
-  __AUTH_CONST.__cfstring: 0x7880
+  __AUTH_CONST.__cfstring: 0x78a0
   __AUTH_CONST.__objc_const: 0x6020
   __AUTH_CONST.__objc_arrayobj: 0x7b0
   __AUTH_CONST.__objc_dictobj: 0x230

   - /usr/lib/updaters/libSavageRestoreInfo_iOS.dylib
   - /usr/lib/updaters/libSavageUpdater_iOS.dylib
   - /usr/lib/updaters/libT200Updater.dylib
-  UUID: AA5E819E-5FE4-3151-8C72-15FA7972A9D8
-  Functions: 2396
-  Symbols:   8216
-  CStrings:  5051
+  UUID: 383ACC70-B3D1-3607-B20E-3D2BDF2EB0EE
+  Functions: 2397
+  Symbols:   8210
+  CStrings:  5056
 
Symbols:
+ -[CRFDRBaseDeviceHandler performPostSealingStage:patchClasses:patchInstances:patchValues:mergedDataClasses:mergedDataInstances:error:]
+ -[CRFDRDisplay1DeviceHandler performPostSealingStage:patchClasses:patchInstances:patchValues:mergedDataClasses:mergedDataInstances:error:]
+ -[CRFDRDisplay1DeviceHandler performPostSealingStage:patchClasses:patchInstances:patchValues:mergedDataClasses:mergedDataInstances:error:].cold.1
+ -[CRFDRDisplay1DeviceHandler performPostSealingStage:patchClasses:patchInstances:patchValues:mergedDataClasses:mergedDataInstances:error:].cold.2
+ -[CRFDRDisplay1DeviceHandler performPostSealingStage:patchClasses:patchInstances:patchValues:mergedDataClasses:mergedDataInstances:error:].cold.3
+ -[CRFDRDisplay2DeviceHandler performPostSealingStage:patchClasses:patchInstances:patchValues:mergedDataClasses:mergedDataInstances:error:]
+ -[CRFDRSeal sealWithDataClass:fdrError:registerOnly:].cold.17
+ -[CRFDRWatch1DeviceHandler performPostSealingStage:patchClasses:patchInstances:patchValues:mergedDataClasses:mergedDataInstances:error:]
+ _objc_msgSend$performPostSealingStage:patchClasses:patchInstances:patchValues:mergedDataClasses:mergedDataInstances:error:
- -[CRFDRBaseDeviceHandler performPostSealingStage:]
- -[CRFDRDisplay1DeviceHandler performPostSealingStage:]
- -[CRFDRDisplay1DeviceHandler performPostSealingStage:].cold.1
- -[CRFDRDisplay1DeviceHandler performPostSealingStage:].cold.2
- -[CRFDRDisplay1DeviceHandler performPostSealingStage:].cold.3
- -[CRFDRDisplay2DeviceHandler performPostSealingStage:]
- -[CRFDRSeal(RealSealing) performRealToRealRepair:fdrLocal:fdrRemote:].cold.9
- -[CRFDRSeal(RealSealing) performStagedToRealRepair:fdrLocal:fdrRemote:].cold.12
- -[CRFDRSeal(StagedSealing) performRealToStagedRepair:fdrLocal:fdrRemote:].cold.10
- -[CRFDRSeal(StagedSealing) performStagedToStagedRepair:fdrLocal:fdrRemote:].cold.6
- -[CRFDRWatch1DeviceHandler performPostSealingStage:]
- _objc_msgSend$performPostSealingStage:
Functions:
~ +[CRSalvageStatus isDateAfterEffectiveDate:] : 160 -> 420
~ +[CRFDRUtils _getUnsealedMesaData:mesaState:] : 864 -> 820
~ -[CRFDRSeal(StagedSealing) performRealToStagedRepair:fdrLocal:fdrRemote:] : 1820 -> 1696
~ -[CRFDRSeal(StagedSealing) performStagedToStagedRepair:fdrLocal:fdrRemote:] : 1680 -> 1556
~ -[CRFDRSeal sealWithDataClass:fdrError:registerOnly:] : 4580 -> 4820
~ -[CRFDRSeal(RealSealing) performRealToRealRepair:fdrLocal:fdrRemote:] : 2528 -> 2384
~ -[CRFDRSeal(RealSealing) performStagedToRealRepair:fdrLocal:fdrRemote:] : 2056 -> 1940
- -[CRFDRSeal(StagedSealing) performStagedToStagedRepair:fdrLocal:fdrRemote:].cold.2
~ -[CRFDRSeal sealWithDataClass:fdrError:registerOnly:].cold.13 : 88 -> 76
+ -[CRFDRSeal sealWithDataClass:fdrError:registerOnly:].cold.17
+ -[CRFDRSeal patchWithOptions:amfdr:dataClasses:dataInstances:values:datas:error:local:].cold.17
CStrings:
+ "/Library/Caches/com.apple.xbs/A7E5D582-9078-4EED-AEBE-ADA7D5324A2F/TemporaryDirectory.K6sp6R/Sources/Mesa/AppleBiometricServices/MesaFactoryC/MesaFactoryC.c"
+ "/Library/Caches/com.apple.xbs/DF8D7722-9644-4C01-B6E4-E43D90C40BEE/TemporaryDirectory.7Innhl/Sources/Pearl_Kernel/PearlFactoryLib/PearlFactoryLib.m"
+ "2026/03/23"
+ "Overriding SalvageEffectiveDate string: %@"
+ "Post Sealing Stage"
+ "Post Sealing Stage Failed: %@"
+ "SalvageEffectiveDate"
+ "performPostSealingStage:patchClasses:patchInstances:patchValues:mergedDataClasses:mergedDataInstances:error:"
+ "q72@0:8@16@24@32@40@48@56^@64"
- "/Library/Caches/com.apple.xbs/05BC2D32-1B21-4498-8369-DABC4A1C2388/TemporaryDirectory.TPxQAa/Sources/Pearl_Kernel/PearlFactoryLib/PearlFactoryLib.m"
- "/Library/Caches/com.apple.xbs/0D5DB0DE-8B78-4337-8C24-2A796C2A60A9/TemporaryDirectory.9CsVvz/Sources/Mesa/AppleBiometricServices/MesaFactoryC/MesaFactoryC.c"
- "2025/11/01"
- "Post Sealing Stage Failed."
- "performPostSealingStage:"

```
