## PowerlogCore

> `/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`

```diff

-1775.2.1.0.0
-  __TEXT.__text: 0xceb70
-  __TEXT.__auth_stubs: 0x1960
-  __TEXT.__objc_methlist: 0x7ad4
+1787.40.67.0.0
+  __TEXT.__text: 0xcfd14
+  __TEXT.__auth_stubs: 0x1970
+  __TEXT.__objc_methlist: 0x7b0c
   __TEXT.__const: 0x14a0
-  __TEXT.__cstring: 0x327da
-  __TEXT.__gcc_except_tab: 0x20e0
-  __TEXT.__oslogstring: 0x5917
-  __TEXT.__unwind_info: 0x29cc
+  __TEXT.__cstring: 0x33177
+  __TEXT.__gcc_except_tab: 0x2140
+  __TEXT.__oslogstring: 0x5ba4
+  __TEXT.__unwind_info: 0x29f4
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x83e
-  __TEXT.__objc_methname: 0x11a68
-  __TEXT.__objc_methtype: 0x185c
-  __TEXT.__objc_stubs: 0xe4e0
+  __TEXT.__objc_methname: 0x11af6
+  __TEXT.__objc_methtype: 0x186a
+  __TEXT.__objc_stubs: 0xe600
   __DATA_CONST.__got: 0x338
-  __DATA_CONST.__const: 0x2370
+  __DATA_CONST.__const: 0x23c0
   __DATA_CONST.__objc_classlist: 0x300
   __DATA_CONST.__objc_nlclslist: 0x80
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x6530
-  __DATA_CONST.__objc_selrefs: 0x49b8
-  __DATA_CONST.__objc_arraydata: 0x30020
+  __DATA_CONST.__objc_selrefs: 0x49f8
+  __DATA_CONST.__objc_arraydata: 0x30780
   __AUTH_CONST.__const: 0x1aa0
-  __AUTH_CONST.__cfstring: 0x4cf80
+  __AUTH_CONST.__cfstring: 0x4dd60
   __AUTH_CONST.__objc_const: 0x29c0
   __AUTH_CONST.__objc_intobj: 0x4308
   __AUTH_CONST.__objc_doubleobj: 0xca0
   __AUTH_CONST.__objc_arrayobj: 0xf00
-  __AUTH_CONST.__objc_dictobj: 0xc3f0
-  __AUTH_CONST.__auth_got: 0xcc8
+  __AUTH_CONST.__objc_dictobj: 0xc558
+  __AUTH_CONST.__auth_got: 0xcd0
   __AUTH.__objc_data: 0x3c0
   __DATA.__objc_protorefs: 0x20
   __DATA.__objc_classrefs: 0x3f0

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libsystemstats.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 90D2F9FD-4156-31C8-AC65-BD7575FFEFA4
-  Functions: 4448
-  Symbols:   14488
-  CStrings:  24242
+  UUID: 654C5AB1-8C32-3D8A-9068-B64263E828F6
+  Functions: 4473
+  Symbols:   14552
+  CStrings:  24495
 
Symbols:
+ +[PLModelingUtilities isAppleVision]
+ +[PLPlatform isAppleVision]
+ +[PLUtilities markFileAsPurgeable:withUrgency:]
+ +[PLUtilities markFileAsPurgeable:withUrgency:].cold.1
+ +[PLUtilities numFilesAtPath:]
+ +[PLUtilities numFilesAtPath:].cold.1
+ +[PLUtilities shouldCreateQuarantine]
+ -[PLSQLiteConnection moveDatabaseToPath:].cold.1
+ -[PLSQLiteConnection truncateDB]
+ -[PLSQLiteConnection truncateDB].cold.1
+ -[PLSubmissionFileMSS generateMSS].cold.6
+ -[RbdcConverterHelper processRbdc:withServiceType:].cold.1
+ -[RbdcConverterHelper processRbdc:withServiceType:].cold.2
+ -[uarpRbdcClient dynamicAssetSolicitationComplete:]
+ -[uarpRbdcClient dynamicAssetSolicitationComplete:].cold.1
+ -[uarpRbdcClient dynamicAssetSolicitationComplete:].cold.2
+ -[uarpRbdcClient dynamicAssetSolicitationComplete:].cold.3
+ -[uarpRbdcClient dynamicAssetSolicitationComplete:].cold.4
+ -[uarpRbdcClient setSolicitedAssetList:]
+ -[uarpRbdcClient solicitAssetsForTag:andModelNumber:]
+ -[uarpRbdcClient solicitAssetsForTag:andModelNumber:].cold.1
+ -[uarpRbdcClient solicitedAssetList]
+ GCC_except_table133
+ GCC_except_table29
+ _OBJC_IVAR_$_uarpRbdcClient._solicitedAssetList
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ ___39+[PLUtilities quarantineToPath:action:]_block_invoke
+ ___39+[PLUtilities quarantineToPath:action:]_block_invoke.cold.1
+ ___39+[PLUtilities quarantineToPath:action:]_block_invoke.cold.2
+ ___42-[RbdcConverterHelper createXPCConnection]_block_invoke.41
+ ___42-[RbdcConverterHelper createXPCConnection]_block_invoke.41.cold.1
+ ___42-[RbdcConverterHelper createXPCConnection]_block_invoke.44
+ ___42-[RbdcConverterHelper createXPCConnection]_block_invoke.44.cold.1
+ ___51-[RbdcConverterHelper processRbdc:withServiceType:]_block_invoke.13
+ ___51-[RbdcConverterHelper processRbdc:withServiceType:]_block_invoke.13.cold.1
+ ___53-[uarpRbdcClient solicitAssetsForTag:andModelNumber:]_block_invoke
+ ___53-[uarpRbdcClient solicitAssetsForTag:andModelNumber:]_block_invoke.cold.1
+ ___block_descriptor_40_e8_32s_e30_v24?0"NSNumber"8"NSError"16ls32l8
+ ___block_descriptor_41_e8_32s_e15_v32?0816^B24ls32l8
+ ___block_literal_global.355
+ ___block_literal_global.361
+ ___block_literal_global.363
+ ___block_literal_global.368
+ ___block_literal_global.373
+ ___block_literal_global.375
+ ___block_literal_global.377
+ ___block_literal_global.381
+ ___block_literal_global.384
+ ___block_literal_global.387
+ ___block_literal_global.390
+ ___block_literal_global.393
+ ___block_literal_global.398
+ ___block_literal_global.403
+ ___block_literal_global.412
+ ___block_literal_global.420
+ ___block_literal_global.429
+ ___block_literal_global.47
+ __unnamed_array_storage.344
+ _ffsctl
+ _objc_msgSend$dynamicAssetSolicitation:modelNumbers:notifyService:reply:
+ _objc_msgSend$getResponseURLs
+ _objc_msgSend$isAppleVision
+ _objc_msgSend$markFileAsPurgeable:withUrgency:
+ _objc_msgSend$modelNumber
+ _objc_msgSend$numFilesAtPath:
+ _objc_msgSend$objCType
+ _objc_msgSend$setSolicitedAssetList:
+ _objc_msgSend$shouldCreateQuarantine
+ _objc_msgSend$solicitedAssetList
+ _objc_msgSend$truncateDB
- -[uarpRbdcClient dynamicAssetSolicitation:modelNumber:]
- -[uarpRbdcClient dynamicAssetSolicitation:modelNumber:].cold.1
- -[uarpRbdcClient dynamicAssetSolicitationComplete:modelNumber:]
- -[uarpRbdcClient setSolicitedAsset:]
- -[uarpRbdcClient solicitedAsset]
- GCC_except_table130
- GCC_except_table132
- _OBJC_IVAR_$_uarpRbdcClient._solicitedAsset
- ___42-[RbdcConverterHelper createXPCConnection]_block_invoke.17
- ___42-[RbdcConverterHelper createXPCConnection]_block_invoke.17.cold.1
- ___42-[RbdcConverterHelper createXPCConnection]_block_invoke.20
- ___42-[RbdcConverterHelper createXPCConnection]_block_invoke.20.cold.1
- ___51-[RbdcConverterHelper processRbdc:withServiceType:]_block_invoke.7
- ___51-[RbdcConverterHelper processRbdc:withServiceType:]_block_invoke.7.cold.1
- ___55-[uarpRbdcClient dynamicAssetSolicitation:modelNumber:]_block_invoke
- ___55-[uarpRbdcClient dynamicAssetSolicitation:modelNumber:]_block_invoke.cold.1
- ___block_literal_global.16
- ___block_literal_global.334
- ___block_literal_global.354
- ___block_literal_global.360
- ___block_literal_global.362
- ___block_literal_global.367
- ___block_literal_global.372
- ___block_literal_global.374
- ___block_literal_global.376
- ___block_literal_global.380
- ___block_literal_global.383
- ___block_literal_global.386
- ___block_literal_global.389
- ___block_literal_global.392
- ___block_literal_global.397
- ___block_literal_global.402
- ___block_literal_global.411
- ___block_literal_global.419
- ___block_literal_global.428
- ___block_literal_global.468
- _objc_msgSend$dynamicAssetSolicitation:modelNumber:notifyService:reply:
- _objc_msgSend$solicitedAsset
CStrings:
+ "%.6e"
+ "-[uarpRbdcClient dynamicAssetSolicitationComplete:]"
+ "-[uarpRbdcClient solicitAssetsForTag:andModelNumber:]"
+ "-[uarpRbdcClient solicitAssetsForTag:andModelNumber:]_block_invoke"
+ "ActionButtonInteraction"
+ "ActionButtonSelection"
+ "ActionButtonSelectionChanged"
+ "AirDropSession"
+ "AmbientModeMotionToWake"
+ "B32@0:8@16Q24"
+ "BDC_PARSER: %s: received assets: %@"
+ "BDC_PARSER: Solicited %@ assets for %@"
+ "BDC_PARSER: assetLocations empty for record %@ model %@"
+ "BDC_PARSER: assetLocations error for record %@ model %@"
+ "BDC_PARSER: modelNumber error for record %@"
+ "BDC_PARSER: no error with %@"
+ "BatteryConfig"
+ "Dod0AtQualifiedQmax"
+ "Failed to get EPSQL file attributes with error %@"
+ "Failed to get num files at path: %@ error: %@"
+ "Failed to mark %@ purgeable - can't open error: %s"
+ "Failed to mark %@ purgeable - flags 0x%llx returned %d (%s)"
+ "Failed to truncate db %d : %s"
+ "FedPdSpecRevision"
+ "FedPwrPolicySt"
+ "FedSnkConfReason"
+ "FedSrcConfReason"
+ "FxS_F1 AC"
+ "FxS_F1 PD"
+ "FxS_F1 SR"
+ "FxS_F2 AC"
+ "FxS_F2 PD"
+ "FxS_F2 SR"
+ "FxS_F3 AC"
+ "FxS_F3 PD"
+ "FxS_F3 SR"
+ "FxS_F4 AC"
+ "FxS_F4 PD"
+ "FxS_F4 SR"
+ "FxS_F5 AC"
+ "FxS_F5 PD"
+ "FxS_F5 SR"
+ "Generating MSS with start date %@ and end date %@"
+ "IPBR"
+ "LastSystemOffset"
+ "Locale"
+ "Marked %@ purgeable with urgency: %llu"
+ "Num files at %@ = %d"
+ "PLApplicationAgent_EventForward_MotionToWake"
+ "PLButtonAgent_EventForward_ActionButtonInteraction"
+ "PLButtonAgent_EventForward_ActionButtonSelection"
+ "PLIOReportAgent_EventBackward_PMPDRAMBW"
+ "PLIOReportAgent_EventBackward_PMPDRAMState"
+ "PLIOReportAgent_EventBackward_PMPFabricBW"
+ "PLLocationAgent_EventForward_SuppressionManagerClient"
+ "PLLocationAgent_EventForward_ViewObstructed"
+ "PLXPCAgent_EventForward_AirDropSession"
+ "PortControllerActiveContractRdo"
+ "PortControllerCapMismatch"
+ "PortControllerDataRoleSwapCount"
+ "PortControllerDataRoleSwapFailCount"
+ "PortControllerElectionFailReason"
+ "PortControllerFwVersion"
+ "PortControllerInpFetEnFailCount"
+ "PortControllerIrqCntAlert"
+ "PortControllerIrqCntAppLd"
+ "PortControllerIrqCntConSrc"
+ "PortControllerIrqCntHrdRst"
+ "PortControllerIrqCntPdStsUpd"
+ "PortControllerIrqCntPlg"
+ "PortControllerIrqCntPwrStsUpd"
+ "PortControllerIrqCntRxIdSop"
+ "PortControllerIrqCntRxRdo"
+ "PortControllerIrqCntRxSnkCap"
+ "PortControllerIrqCntRxSrcCap"
+ "PortControllerIrqCntStsUpd"
+ "PortControllerIrqCntUsb2Plg"
+ "PortControllerIrqCntUsb2Wak"
+ "PortControllerIrqCntUvdmEnum"
+ "PortControllerIrqCntUvdmStsUpd"
+ "PortControllerIrqCntldcm"
+ "PortControllerNEprPDOs"
+ "PortControllerPDst"
+ "PortControllerPortMode"
+ "PortControllerPortPDO0"
+ "PortControllerPortPDO1"
+ "PortControllerPortPDO10"
+ "PortControllerPortPDO11"
+ "PortControllerPortPDO12"
+ "PortControllerPortPDO13"
+ "PortControllerPortPDO14"
+ "PortControllerPortPDO2"
+ "PortControllerPortPDO3"
+ "PortControllerPortPDO4"
+ "PortControllerPortPDO5"
+ "PortControllerPortPDO6"
+ "PortControllerPortPDO7"
+ "PortControllerPortPDO8"
+ "PortControllerPortPDO9"
+ "PortControllerPwrRoleSwapCount"
+ "PortControllerPwrRoleSwapFailCount"
+ "PortControllerShortDetectCount"
+ "PortControllerSrcTypes"
+ "PortControllerSrdoCount"
+ "PortControllerSrdoRetryCount"
+ "PortControllerSrdyCount"
+ "PortControllerSurpriseAckCount"
+ "PortControllerSurpriseNackCount"
+ "PortControllerUvdmStatus"
+ "PortControllerVdoFailCount"
+ "PortControllerWakeFailCount"
+ "Quarantine dst: %@"
+ "Quarantine src: %@"
+ "RBDC metrics: %@"
+ "RBDC reply received: result=%@"
+ "SuppressionManagerClientStateChange"
+ "T@\"NSMutableArray\",&,V_solicitedAssetList"
+ "Time for RBDC processing to run: %f, %@, %@"
+ "VMAX RD"
+ "VMAX WR"
+ "VMIN RD"
+ "VMIN WR"
+ "VNOM RD"
+ "VNOM WR"
+ "VOEvent"
+ "VOVD RD"
+ "VOVD WR"
+ "VP0R"
+ "ViewObstructedStateChange"
+ "_solicitedAssetList"
+ "clientEvent"
+ "clientNumbers"
+ "clientType"
+ "f"
+ "fileSizeInBytes"
+ "getResponseURLs"
+ "isAppleVision"
+ "markFileAsPurgeable:withUrgency:"
+ "modelNumber"
+ "numFilesAtPath:"
+ "objCType"
+ "rbdcDurationInSeconds"
+ "rbdcStatus"
+ "setSolicitedAssetList:"
+ "should quarantine: %d"
+ "shouldCreateQuarantine"
+ "solicitAssetsForTag:andModelNumber:"
+ "solicitedAssetList"
+ "truncateDB"
+ "uptimeInSeconds"
+ "v24@?0@\"NSNumber\"8@\"NSError\"16"
+ "{\"metric\":\"%{public}@\",\"value\":%{public}@,\"pid\":%{public}@}"
+ "{\"metric\":\"%{public}@\",\"value\":%{public}@}"
- "-[uarpRbdcClient dynamicAssetSolicitation:modelNumber:]"
- "-[uarpRbdcClient dynamicAssetSolicitation:modelNumber:]_block_invoke"
- "-[uarpRbdcClient dynamicAssetSolicitationComplete:modelNumber:]"
- "BDC_PARSER: %s: received assets: %@ for device with model number: %@."
- "PLIOReportAgent_EventBackward_PMPDRAMBWAMCC"
- "T@\"NSMutableDictionary\",&,V_solicitedAsset"
- "Time for RBDC processing reading to run: %f, %@, %@"
- "_solicitedAsset"
- "dynamicAssetSolicitation:modelNumber:"
- "setSolicitedAsset:"
- "solicitedAsset"
- "{\"Metric\":\"%{public}@\",\"Source\":\"%{public}@\",\"Time\":%{public}.6f,\"Value\":%{public}.6e}"

```
