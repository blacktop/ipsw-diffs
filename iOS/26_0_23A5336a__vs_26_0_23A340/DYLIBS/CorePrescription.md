## CorePrescription

> `/System/Library/PrivateFrameworks/CorePrescription.framework/CorePrescription`

```diff

 207.0.35.0.0
-  __TEXT.__text: 0x33384
-  __TEXT.__auth_stubs: 0x1080
-  __TEXT.__objc_methlist: 0x25f8
-  __TEXT.__const: 0x710c
-  __TEXT.__cstring: 0x48f4
-  __TEXT.__oslogstring: 0xb1d
+  __TEXT.__text: 0x38214
+  __TEXT.__auth_stubs: 0x1090
+  __TEXT.__objc_methlist: 0x2978
+  __TEXT.__const: 0x735c
+  __TEXT.__cstring: 0x4f16
+  __TEXT.__oslogstring: 0xb3d
   __TEXT.__gcc_except_tab: 0x318
-  __TEXT.__swift5_typeref: 0x258
-  __TEXT.__swift5_reflstr: 0x557
-  __TEXT.__swift5_assocty: 0x138
-  __TEXT.__constg_swiftt: 0x7d0
-  __TEXT.__swift5_builtin: 0x104
-  __TEXT.__swift5_fieldmd: 0x4c8
-  __TEXT.__swift5_proto: 0xbc
-  __TEXT.__swift5_types: 0x6c
-  __TEXT.__unwind_info: 0xe58
+  __TEXT.__swift5_typeref: 0x280
+  __TEXT.__swift5_reflstr: 0x633
+  __TEXT.__swift5_assocty: 0x168
+  __TEXT.__constg_swiftt: 0x918
+  __TEXT.__swift5_builtin: 0x12c
+  __TEXT.__swift5_fieldmd: 0x578
+  __TEXT.__swift5_proto: 0xdc
+  __TEXT.__swift5_types: 0x7c
+  __TEXT.__unwind_info: 0xf50
   __TEXT.__eh_frame: 0xf0
-  __TEXT.__objc_classname: 0x3f4
-  __TEXT.__objc_methname: 0x528e
-  __TEXT.__objc_methtype: 0x123c
-  __TEXT.__objc_stubs: 0x3460
-  __DATA_CONST.__got: 0x458
-  __DATA_CONST.__const: 0x10f8
-  __DATA_CONST.__objc_classlist: 0x1a0
+  __TEXT.__objc_classname: 0x3fe
+  __TEXT.__objc_methname: 0x5d56
+  __TEXT.__objc_methtype: 0x13be
+  __TEXT.__objc_stubs: 0x3760
+  __DATA_CONST.__got: 0x470
+  __DATA_CONST.__const: 0x11a0
+  __DATA_CONST.__objc_classlist: 0x1b8
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1390
+  __DATA_CONST.__objc_selrefs: 0x1510
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x110
-  __AUTH_CONST.__auth_got: 0x850
-  __AUTH_CONST.__const: 0x1e0
-  __AUTH_CONST.__cfstring: 0x2500
-  __AUTH_CONST.__objc_const: 0x5a98
+  __DATA_CONST.__objc_superrefs: 0x118
+  __AUTH_CONST.__auth_got: 0x858
+  __AUTH_CONST.__const: 0x220
+  __AUTH_CONST.__cfstring: 0x2700
+  __AUTH_CONST.__objc_const: 0x62d0
   __AUTH_CONST.__objc_intobj: 0x60
-  __AUTH.__objc_data: 0x1480
-  __AUTH.__data: 0x188
-  __DATA.__objc_ivar: 0x2fc
-  __DATA.__data: 0x610
-  __DATA.__bss: 0x17b0
+  __AUTH.__objc_data: 0x1738
+  __AUTH.__data: 0x1f0
+  __DATA.__objc_ivar: 0x344
+  __DATA.__data: 0x690
+  __DATA.__bss: 0x1bb0
   __DATA.__common: 0x4
   __DATA_DIRTY.__objc_data: 0x718
   __DATA_DIRTY.__data: 0x118

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: 102716AF-4B98-3938-8146-C05B25A2BE6F
-  Functions: 1584
-  Symbols:   3117
-  CStrings:  2165
+  UUID: E9924F02-5714-3219-BAF5-AE61861395D8
+  Functions: 1747
+  Symbols:   3272
+  CStrings:  2318
 
Symbols:
+ -[CRXFAppClipCode initWithVersion:lensType:cylLeftSignFlipped:cylRightSignFlipped:leftRXID:leftCalibrationRXID:leftDisplaySphere:leftDisplayCylinder:leftCalibrationSphere:leftCalibrationCylinder:leftAddVR:leftAxisID:leftDisplayAxis:leftCalibrationAxis:leftClamping:leftHorizPrismBaseDirection:leftHorizPrism:leftVertPrismBaseDirection:leftVertPrism:rightRXID:rightCalibrationRXID:rightDisplaySphere:rightDisplayCylinder:rightCalibrationSphere:rightCalibrationCylinder:rightAddVR:rightAxisID:rightDisplayAxis:rightCalibrationAxis:rightClamping:rightHorizPrismBaseDirection:rightHorizPrism:rightVertPrismBaseDirection:rightVertPrism:identifyingColor:secret:randomBits:]
+ -[CRXFAppClipCode leftHorizPrismBaseDirection]
+ -[CRXFAppClipCode leftHorizPrism]
+ -[CRXFAppClipCode leftVertPrismBaseDirection]
+ -[CRXFAppClipCode leftVertPrism]
+ -[CRXFAppClipCode rightHorizPrismBaseDirection]
+ -[CRXFAppClipCode rightHorizPrism]
+ -[CRXFAppClipCode rightVertPrismBaseDirection]
+ -[CRXFAppClipCode rightVertPrism]
+ -[CRXFAppClipCodeBuilder leftHorizPrismBaseDirection]
+ -[CRXFAppClipCodeBuilder leftHorizPrism]
+ -[CRXFAppClipCodeBuilder leftVertPrismBaseDirection]
+ -[CRXFAppClipCodeBuilder leftVertPrism]
+ -[CRXFAppClipCodeBuilder rightHorizPrismBaseDirection]
+ -[CRXFAppClipCodeBuilder rightHorizPrism]
+ -[CRXFAppClipCodeBuilder rightVertPrismBaseDirection]
+ -[CRXFAppClipCodeBuilder rightVertPrism]
+ -[CRXFAppClipCodeBuilder setLeftHorizPrism:]
+ -[CRXFAppClipCodeBuilder setLeftHorizPrismBaseDirection:]
+ -[CRXFAppClipCodeBuilder setLeftVertPrism:]
+ -[CRXFAppClipCodeBuilder setLeftVertPrismBaseDirection:]
+ -[CRXFAppClipCodeBuilder setRightHorizPrism:]
+ -[CRXFAppClipCodeBuilder setRightHorizPrismBaseDirection:]
+ -[CRXFAppClipCodeBuilder setRightVertPrism:]
+ -[CRXFAppClipCodeBuilder setRightVertPrismBaseDirection:]
+ -[CRXFAppClipCodeTranscoder decodeAppClipCodeV6FromBuffer:allowUnsupportedRX:error:]
+ -[CRXFAppClipCodeTranscoder encodeAppClipCodeV6:toBuffer:error:]
+ -[CRXFAppClipCodeTranscoder generateAppClipCodeWithVersion:lensType:haveLeftLens:leftSphere:leftCylinder:leftAxis:leftAddVR:leftHorizPrismBaseDirection:leftHorizPrism:leftVertPrismBaseDirection:leftVertPrism:haveRightLens:rightSphere:rightCylinder:rightAxis:rightAddVR:rightHorizPrismBaseDirection:rightHorizPrism:rightVertPrismBaseDirection:rightVertPrism:identifyingColor:secret:error:]
+ -[CRXFHealthDataProvider createPrescriptionWithSphereRight:cylinderRight:axisRight:prismRight:sphereLeft:cylinderLeft:axisLeft:prismLeft:readerRange:accPayload:description:colorCode:lensTypeCode:serialNumber:issueDate:]
+ -[CRXFHealthDataProvider createVisionPrismForVerticalAmount:verticalDirection:horizontalAmount:horizontalDirection:leftEye:]
+ -[CRXFHealthDataProvider updatePrescription:withMetadata:axisRight:axisLeft:prismRight:prismLeft:]
+ -[CRXFHealthDataProvider updatePrescription:withMetadata:axisRight:axisLeft:prismRight:prismLeft:].cold.1
+ -[CRXFHealthDataProvider updatePrescription:withMetadata:axisRight:axisLeft:prismRight:prismLeft:].cold.2
+ -[CRXFPrism .cxx_destruct]
+ -[CRXFPrism init]
+ -[CRXFPrism isPrismEnabledForLocation:]
+ -[CRXFVisionPrescriptionURLDecoder prescriptionFromURL:withDescription:].cold.4
+ _CRXFLocalizedPrismStringWithArguments
+ _CRXFLocalizedStringForPrism
+ _CRXFPrismBaseDirectionAsString
+ _OBJC_CLASS_$_CRXCEyePrismCorrection
+ _OBJC_CLASS_$_CRXCPrismCorrection
+ _OBJC_CLASS_$_CRXFPrism
+ _OBJC_CLASS_$_HKVisionPrism
+ _OBJC_IVAR_$_CRXFAppClipCode._leftHorizPrism
+ _OBJC_IVAR_$_CRXFAppClipCode._leftHorizPrismBaseDirection
+ _OBJC_IVAR_$_CRXFAppClipCode._leftVertPrism
+ _OBJC_IVAR_$_CRXFAppClipCode._leftVertPrismBaseDirection
+ _OBJC_IVAR_$_CRXFAppClipCode._rightHorizPrism
+ _OBJC_IVAR_$_CRXFAppClipCode._rightHorizPrismBaseDirection
+ _OBJC_IVAR_$_CRXFAppClipCode._rightVertPrism
+ _OBJC_IVAR_$_CRXFAppClipCode._rightVertPrismBaseDirection
+ _OBJC_IVAR_$_CRXFAppClipCodeBuilder._leftHorizPrism
+ _OBJC_IVAR_$_CRXFAppClipCodeBuilder._leftHorizPrismBaseDirection
+ _OBJC_IVAR_$_CRXFAppClipCodeBuilder._leftVertPrism
+ _OBJC_IVAR_$_CRXFAppClipCodeBuilder._leftVertPrismBaseDirection
+ _OBJC_IVAR_$_CRXFAppClipCodeBuilder._rightHorizPrism
+ _OBJC_IVAR_$_CRXFAppClipCodeBuilder._rightHorizPrismBaseDirection
+ _OBJC_IVAR_$_CRXFAppClipCodeBuilder._rightVertPrism
+ _OBJC_IVAR_$_CRXFAppClipCodeBuilder._rightVertPrismBaseDirection
+ _OBJC_IVAR_$_CRXFPrism._prismActivationList
+ _OBJC_IVAR_$_CRXFVisionPrescriptionURLDecoder._prismRange
+ _OBJC_METACLASS_$_CRXCEyePrismCorrection
+ _OBJC_METACLASS_$_CRXCPrismCorrection
+ _OBJC_METACLASS_$_CRXFPrism
+ __CLASS_METHODS_CRXCEyePrismCorrection
+ __CLASS_METHODS_CRXCPrismCorrection
+ __CLASS_PROPERTIES_CRXCEyePrismCorrection
+ __CLASS_PROPERTIES_CRXCPrismCorrection
+ __DATA_CRXCEyePrismCorrection
+ __DATA_CRXCPrismCorrection
+ __INSTANCE_METHODS_CRXCEyePrismCorrection
+ __INSTANCE_METHODS_CRXCPrismCorrection
+ __IVARS_CRXCEyePrismCorrection
+ __IVARS_CRXCPrismCorrection
+ __METACLASS_DATA_CRXCEyePrismCorrection
+ __METACLASS_DATA_CRXCPrismCorrection
+ __OBJC_$_INSTANCE_METHODS_CRXFPrism
+ __OBJC_$_INSTANCE_VARIABLES_CRXFPrism
+ __OBJC_CLASS_RO_$_CRXFPrism
+ __OBJC_METACLASS_RO_$_CRXFPrism
+ __PROPERTIES_CRXCEyePrismCorrection
+ __PROPERTIES_CRXCPrismCorrection
+ __PROTOCOLS_CRXCAppClipCodePayload.40
+ __PROTOCOLS_CRXCEyePrismCorrection
+ __PROTOCOLS_CRXCEyePrismCorrection.3
+ __PROTOCOLS_CRXCPrescriptionInfo.34
+ __PROTOCOLS_CRXCPrescriptionValues.28
+ __PROTOCOLS_CRXCPrismCorrection
+ __PROTOCOLS_CRXCPrismCorrection.9
+ ___110-[CRXFCorePrescriptionServiceClient downloadCalibrationDataForACCPayload:orASAKey:completionQueue:completion:]_block_invoke.179
+ ___110-[CRXFCorePrescriptionServiceClient downloadCalibrationDataForACCPayload:orASAKey:completionQueue:completion:]_block_invoke.179.cold.1
+ ___110-[CRXFCorePrescriptionServiceClient downloadCalibrationDataForACCPayload:orASAKey:completionQueue:completion:]_block_invoke.182
+ ___110-[CRXFCorePrescriptionServiceClient downloadCalibrationDataForACCPayload:orASAKey:completionQueue:completion:]_block_invoke.183
+ ___84-[CRXFAppClipCodeTranscoder decodeAppClipCodeV6FromBuffer:allowUnsupportedRX:error:]_block_invoke
+ ___block_descriptor_233_e8_32s_e32_v16?0"CRXFAppClipCodeBuilder"8ls32l8
+ __os_feature_enabled_impl
+ _associated conformance 16CorePrescription13CRXCPrismTypeOSHAASQ
+ _associated conformance 16CorePrescription22CRXCPrismBaseDirectionOSHAASQ
+ _kCRXFAppClipCodeFirstPrismVersion
+ _objc_msgSend$dataWithContentsOfFile:
+ _objc_msgSend$decodeAppClipCodeV6FromBuffer:allowUnsupportedRX:error:
+ _objc_msgSend$encodeAppClipCodeV6:toBuffer:error:
+ _objc_msgSend$getQuarterDiopterValueForIndex:minValue:maxValue:value:
+ _objc_msgSend$initWithVersion:lensType:cylLeftSignFlipped:cylRightSignFlipped:leftRXID:leftCalibrationRXID:leftDisplaySphere:leftDisplayCylinder:leftCalibrationSphere:leftCalibrationCylinder:leftAddVR:leftAxisID:leftDisplayAxis:leftCalibrationAxis:leftClamping:leftHorizPrismBaseDirection:leftHorizPrism:leftVertPrismBaseDirection:leftVertPrism:rightRXID:rightCalibrationRXID:rightDisplaySphere:rightDisplayCylinder:rightCalibrationSphere:rightCalibrationCylinder:rightAddVR:rightAxisID:rightDisplayAxis:rightCalibrationAxis:rightClamping:rightHorizPrismBaseDirection:rightHorizPrism:rightVertPrismBaseDirection:rightVertPrism:identifyingColor:secret:randomBits:
+ _objc_msgSend$initWithVerticalAmount:verticalBase:horizontalAmount:horizontalBase:eye:
+ _objc_msgSend$leftHorizPrism
+ _objc_msgSend$leftHorizPrismBaseDirection
+ _objc_msgSend$leftVertPrism
+ _objc_msgSend$leftVertPrismBaseDirection
+ _objc_msgSend$pathForResource:ofType:
+ _objc_msgSend$prismActivationLocation
+ _objc_msgSend$prismDiopterUnit
+ _objc_msgSend$rightHorizPrism
+ _objc_msgSend$rightHorizPrismBaseDirection
+ _objc_msgSend$rightVertPrism
+ _objc_msgSend$rightVertPrismBaseDirection
+ _objc_msgSend$setLeftHorizPrism:
+ _objc_msgSend$setLeftHorizPrismBaseDirection:
+ _objc_msgSend$setLeftVertPrism:
+ _objc_msgSend$setLeftVertPrismBaseDirection:
+ _objc_msgSend$setRightHorizPrism:
+ _objc_msgSend$setRightHorizPrismBaseDirection:
+ _objc_msgSend$setRightVertPrism:
+ _objc_msgSend$setRightVertPrismBaseDirection:
+ _symbolic _____ 16CorePrescription13CRXCPrismTypeO
+ _symbolic _____ 16CorePrescription19CRXCPrismCorrectionC
+ _symbolic _____ 16CorePrescription22CRXCEyePrismCorrectionC
+ _symbolic _____ 16CorePrescription22CRXCPrismBaseDirectionO
- -[CRXFAppClipCode initWithVersion:lensType:cylLeftSignFlipped:cylRightSignFlipped:leftRXID:leftCalibrationRXID:leftDisplaySphere:leftDisplayCylinder:leftCalibrationSphere:leftCalibrationCylinder:leftAddVR:leftAxisID:leftDisplayAxis:leftCalibrationAxis:leftClamping:rightRXID:rightCalibrationRXID:rightDisplaySphere:rightDisplayCylinder:rightCalibrationSphere:rightCalibrationCylinder:rightAddVR:rightAxisID:rightDisplayAxis:rightCalibrationAxis:rightClamping:identifyingColor:secret:randomBits:]
- -[CRXFHealthDataProvider createPrescriptionWithSphereRight:cylinderRight:axisRight:sphereLeft:cylinderLeft:axisLeft:readerRange:accPayload:description:colorCode:lensTypeCode:serialNumber:issueDate:]
- -[CRXFHealthDataProvider updatePrescription:withMetadata:axisRight:axisLeft:]
- -[CRXFHealthDataProvider updatePrescription:withMetadata:axisRight:axisLeft:].cold.1
- -[CRXFHealthDataProvider updatePrescription:withMetadata:axisRight:axisLeft:].cold.2
- __PROTOCOLS_CRXCAppClipCodePayload.35
- __PROTOCOLS_CRXCPrescriptionInfo.29
- __PROTOCOLS_CRXCPrescriptionValues.23
- ___110-[CRXFCorePrescriptionServiceClient downloadCalibrationDataForACCPayload:orASAKey:completionQueue:completion:]_block_invoke.170
- ___110-[CRXFCorePrescriptionServiceClient downloadCalibrationDataForACCPayload:orASAKey:completionQueue:completion:]_block_invoke.170.cold.1
- ___110-[CRXFCorePrescriptionServiceClient downloadCalibrationDataForACCPayload:orASAKey:completionQueue:completion:]_block_invoke.173
- ___110-[CRXFCorePrescriptionServiceClient downloadCalibrationDataForACCPayload:orASAKey:completionQueue:completion:]_block_invoke.174
- _objc_msgSend$initWithVersion:lensType:cylLeftSignFlipped:cylRightSignFlipped:leftRXID:leftCalibrationRXID:leftDisplaySphere:leftDisplayCylinder:leftCalibrationSphere:leftCalibrationCylinder:leftAddVR:leftAxisID:leftDisplayAxis:leftCalibrationAxis:leftClamping:rightRXID:rightCalibrationRXID:rightDisplaySphere:rightDisplayCylinder:rightCalibrationSphere:rightCalibrationCylinder:rightAddVR:rightAxisID:rightDisplayAxis:rightCalibrationAxis:rightClamping:identifyingColor:secret:randomBits:
CStrings:
+ "%@<%p> lensType:%@, cylLeftSignFlipped: %@, cylRightSignFlipped: %@, leftRXID: %@, leftCalibrationRXID: %@, leftDisplaySphere:%.02f, leftDisplayCylinder:%.02f, leftCalibrationSphere:%.02f, leftCalibrationCylinder:%.02f, leftAxisID: %@, leftDisplayAxis: %lu, leftCalibrationAxis: %lu, leftClamping: %@ leftHorizPrismDirection: %@, leftHorizPrism:%.02f, leftVertPrismDirection: %@, leftVertPrism:%.02f, rightRXID: %@, rightCalibrationRXID: %@, rightDisplaySphere: %.02f, rightDisplayCylinder: %.02f, rightCalibrationSphere:%.02f, rightCalibrationCylinder:%.02f, rightAxisID: %@, rightDisplayAxis: %lu, rightCalibrationAxis: %lu, rightClamping: %@ rightHorizPrismDirection: %@, rightHorizPrism:%.02f, rightVertPrismDirection: %@, rightVertPrism:%.02f, identifyingColor: %@, secret: %@"
+ "%s @%d: Invalid prism RX values"
+ ", prismActivationLocation: "
+ "-[CRXFHealthDataProvider updatePrescription:withMetadata:axisRight:axisLeft:prismRight:prismLeft:]"
+ "@\"CRXCEyePrismCorrection\""
+ "@112@0:8Q16Q24Q32B40Q44Q52q60Q68q76B84@88@96q104"
+ "@136@0:8d16d24Q32@40d48d56Q64@72@80@88@96Q104Q112@120@128"
+ "@152@0:8Q16Q24B32f36f40Q44f52Q56f64Q68f76B80f84f88Q92f100Q104f112Q116f124Q128@136^@144"
+ "@248@0:8Q16Q24B32B36Q40Q48f56f60f64f68f72Q76Q84Q92Q100Q108f116Q120f128Q132Q140f148f152f156f160f164Q168Q176Q184Q192Q200f208Q212f220Q224@232Q240"
+ "@40@0:8@16@24q32"
+ "@48@0:8q16d24q32d40"
+ "@52@0:8d16Q24d32Q40B48"
+ "CRXFPrism"
+ "CorePrescription.CRXCEyePrismCorrection"
+ "CorePrescription.CRXCPrismCorrection"
+ "LocalizablePrism"
+ "OcularActivationLocations"
+ "SeaLevel"
+ "SeaUrchin"
+ "T@\"CRXCEyePrismCorrection\",N,R,VprismOD"
+ "T@\"CRXCEyePrismCorrection\",N,R,VprismOS"
+ "TQ,N,V_leftHorizPrismBaseDirection"
+ "TQ,N,V_leftVertPrismBaseDirection"
+ "TQ,N,V_rightHorizPrismBaseDirection"
+ "TQ,N,V_rightVertPrismBaseDirection"
+ "TQ,N,VhorizPrismID"
+ "TQ,N,VvertPrismID"
+ "TQ,R,N,V_leftHorizPrismBaseDirection"
+ "TQ,R,N,V_leftVertPrismBaseDirection"
+ "TQ,R,N,V_rightHorizPrismBaseDirection"
+ "TQ,R,N,V_rightVertPrismBaseDirection"
+ "Td,N,R,VhorizontalAmount"
+ "Td,N,R,VverticalAmount"
+ "Tf,N,V_leftHorizPrism"
+ "Tf,N,V_leftVertPrism"
+ "Tf,N,V_rightHorizPrism"
+ "Tf,N,V_rightVertPrism"
+ "Tf,R,N,V_leftHorizPrism"
+ "Tf,R,N,V_leftVertPrism"
+ "Tf,R,N,V_rightHorizPrism"
+ "Tf,R,N,V_rightVertPrism"
+ "Tq,N,R,VhorizontalBaseDirection"
+ "Tq,N,R,Vtype"
+ "Tq,N,R,VverticalBaseDirection"
+ "Tq,N,VhorizPrismBaseDir"
+ "Tq,N,VvertPrismBaseDir"
+ "_leftHorizPrism"
+ "_leftHorizPrismBaseDirection"
+ "_leftVertPrism"
+ "_leftVertPrismBaseDirection"
+ "_prismActivationList"
+ "_prismRange"
+ "_rightHorizPrism"
+ "_rightHorizPrismBaseDirection"
+ "_rightVertPrism"
+ "_rightVertPrismBaseDirection"
+ "createPrescriptionWithSphereRight:cylinderRight:axisRight:prismRight:sphereLeft:cylinderLeft:axisLeft:prismLeft:readerRange:accPayload:description:colorCode:lensTypeCode:serialNumber:issueDate:"
+ "createVisionPrismForVerticalAmount:verticalDirection:horizontalAmount:horizontalDirection:leftEye:"
+ "dataWithContentsOfFile:"
+ "decodeAppClipCodeV6FromBuffer:allowUnsupportedRX:error:"
+ "enabled"
+ "encodeAppClipCodeV6:toBuffer:error:"
+ "fetchPrismCorrectionForUUID:inGroup:completionHandler:"
+ "generateAppClipCodeWithVersion:lensType:haveLeftLens:leftSphere:leftCylinder:leftAxis:leftAddVR:leftHorizPrismBaseDirection:leftHorizPrism:leftVertPrismBaseDirection:leftVertPrism:haveRightLens:rightSphere:rightCylinder:rightAxis:rightAddVR:rightHorizPrismBaseDirection:rightHorizPrism:rightVertPrismBaseDirection:rightVertPrism:identifyingColor:secret:error:"
+ "getPrismActivationLocationWithCompletionHandler:"
+ "getPrismActivationStatusWithCompletionHandler:"
+ "h-in/v-down"
+ "h-out/v-up"
+ "horizPrismBaseDir"
+ "horizPrismID"
+ "horizontalAmount"
+ "horizontalBaseDirection"
+ "initWithHorizontalBaseDirection:horizontalAmount:verticalBaseDirection:verticalAmount:"
+ "initWithPrismOD:prismOS:type:"
+ "initWithRxID:axisID:rxOffsetID:cylinderSignFlipped:calibratedRXID:horizPrismID:horizPrismBaseDir:vertPrismID:vertPrismBaseDir:outOfRange:displayValues:calibrationValues:clampingStatus:"
+ "initWithVersion:lensType:cylLeftSignFlipped:cylRightSignFlipped:leftRXID:leftCalibrationRXID:leftDisplaySphere:leftDisplayCylinder:leftCalibrationSphere:leftCalibrationCylinder:leftAddVR:leftAxisID:leftDisplayAxis:leftCalibrationAxis:leftClamping:leftHorizPrismBaseDirection:leftHorizPrism:leftVertPrismBaseDirection:leftVertPrism:rightRXID:rightCalibrationRXID:rightDisplaySphere:rightDisplayCylinder:rightCalibrationSphere:rightCalibrationCylinder:rightAddVR:rightAxisID:rightDisplayAxis:rightCalibrationAxis:rightClamping:rightHorizPrismBaseDirection:rightHorizPrism:rightVertPrismBaseDirection:rightVertPrism:identifyingColor:secret:randomBits:"
+ "initWithVerticalAmount:verticalBase:horizontalAmount:horizontalBase:eye:"
+ "isPrismEnabledForLocation:"
+ "json"
+ "leftHorizPrism"
+ "leftHorizPrismBaseDirection"
+ "leftVertPrism"
+ "leftVertPrismBaseDirection"
+ "lhp"
+ "lhpd"
+ "lvp"
+ "lvpd"
+ "none"
+ "pathForResource:ofType:"
+ "prismActivationLocation"
+ "prismActivationLocation.string"
+ "prismDiopterUnit"
+ "prismOD"
+ "prismOS"
+ "rhp"
+ "rhpd"
+ "rightHorizPrism"
+ "rightHorizPrismBaseDirection"
+ "rightVertPrism"
+ "rightVertPrismBaseDirection"
+ "rvp"
+ "rvpd"
+ "setHorizPrismBaseDir:"
+ "setHorizPrismID:"
+ "setLeftHorizPrism:"
+ "setLeftHorizPrismBaseDirection:"
+ "setLeftVertPrism:"
+ "setLeftVertPrismBaseDirection:"
+ "setRightHorizPrism:"
+ "setRightHorizPrismBaseDirection:"
+ "setRightVertPrism:"
+ "setRightVertPrismBaseDirection:"
+ "setVertPrismBaseDir:"
+ "setVertPrismID:"
+ "type"
+ "updatePrescription:withMetadata:axisRight:axisLeft:prismRight:prismLeft:"
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
+ "\xf0\xd1"
- "%@<%p> lensType:%@, cylLeftSignFlipped: %@, cylRightSignFlipped: %@, leftRXID: %@, leftCalibrationRXID: %@, leftDisplaySphere:%.02f, leftDisplayCylinder:%.02f, leftCalibrationSphere:%.02f, leftCalibrationCylinder:%.02f, leftAxisID: %@, leftDisplayAxis: %lu, leftCalibrationAxis: %lu, leftClamping: %@ rightRXID: %@, rightCalibrationRXID: %@, rightDisplaySphere: %.02f, rightDisplayCylinder: %.02f, rightCalibrationSphere:%.02f, rightCalibrationCylinder:%.02f, rightAxisID: %@, rightDisplayAxis: %lu, rightCalibrationAxis: %lu, rightClamping: %@ identifyingColor: %@, secret: %@"
- "-[CRXFHealthDataProvider updatePrescription:withMetadata:axisRight:axisLeft:]"
- "@120@0:8d16d24Q32d40d48Q56@64@72@80Q88Q96@104@112"
- "@200@0:8Q16Q24B32B36Q40Q48f56f60f64f68f72Q76Q84Q92Q100Q108Q116f124f128f132f136f140Q144Q152Q160Q168Q176@184Q192"
- "createPrescriptionWithSphereRight:cylinderRight:axisRight:sphereLeft:cylinderLeft:axisLeft:readerRange:accPayload:description:colorCode:lensTypeCode:serialNumber:issueDate:"
- "initWithVersion:lensType:cylLeftSignFlipped:cylRightSignFlipped:leftRXID:leftCalibrationRXID:leftDisplaySphere:leftDisplayCylinder:leftCalibrationSphere:leftCalibrationCylinder:leftAddVR:leftAxisID:leftDisplayAxis:leftCalibrationAxis:leftClamping:rightRXID:rightCalibrationRXID:rightDisplaySphere:rightDisplayCylinder:rightCalibrationSphere:rightCalibrationCylinder:rightAddVR:rightAxisID:rightDisplayAxis:rightCalibrationAxis:rightClamping:identifyingColor:secret:randomBits:"
- "updatePrescription:withMetadata:axisRight:axisLeft:"
- "\xf0q"

```
