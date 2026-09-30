## IntelligentDistortionCorrectionV1

> `/System/Library/VideoProcessors/IntelligentDistortionCorrectionV1.bundle/IntelligentDistortionCorrectionV1`

```diff

-575.14.1.0.0
-  __TEXT.__text: 0x131f4
-  __TEXT.__auth_stubs: 0x3e0
-  __TEXT.__objc_methlist: 0x7ac
+575.15.1.0.0
+  __TEXT.__text: 0x1352c
+  __TEXT.__auth_stubs: 0x3d0
+  __TEXT.__objc_methlist: 0x854
   __TEXT.__const: 0x1d0
-  __TEXT.__cstring: 0x4278
+  __TEXT.__cstring: 0x42b9
   __TEXT.__unwind_info: 0x208
-  __TEXT.__objc_classname: 0x66c
-  __TEXT.__objc_methname: 0x2675
-  __TEXT.__objc_methtype: 0x2f09
+  __TEXT.__objc_classname: 0x66e
+  __TEXT.__objc_methname: 0x2a54
+  __TEXT.__objc_methtype: 0x3134
   __TEXT.__objc_stubs: 0x10e0
   __DATA_CONST.__got: 0x120
   __DATA_CONST.__const: 0x48
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x638
+  __DATA_CONST.__objc_selrefs: 0x6a8
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x1f8
+  __AUTH_CONST.__auth_got: 0x1f0
   __AUTH_CONST.__auth_ptr: 0x10
   __AUTH_CONST.__cfstring: 0xd60
-  __AUTH_CONST.__objc_const: 0x1b50
-  __DATA.__objc_ivar: 0x120
+  __AUTH_CONST.__objc_const: 0x1ed0
+  __DATA.__objc_ivar: 0x13c
   __DATA.__data: 0x180
   __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__bss: 0x8

   - /System/Library/PrivateFrameworks/CMImaging.framework/CMImaging
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 181
-  Symbols:   123
-  CStrings:  949
+  Functions: 195
+  Symbols:   122
+  CStrings:  990
 
Symbols:
- _objc_retain_x27
CStrings:
+ "_applyStereoRectificationHomography"
+ "setOpticalCenterOffset:"
+ "i64@0:8^{?=BfffI{?=ffffffff}{?=ffffffff}B{?=[3]}BBB{?=IIIIfI}[6f]{?={?=iiiiii}{?=iiiiii}{?=iiiiii}{?=iiiiii}}{?={?=iiiiii}}{?=iiiiii}{?=IfIIIfffII}{?=ffffII}BI[10{?=[7f]}]I[10{?=Bif}]ff}16@24@32@40@48@56"
+ "{?=\"finalImageDimensions\"\"replicatePixels\"B\"digitalZoomRatio\"f\"pixelSize\"f\"opticalCenterOffset\"\"dynamicDistortionFactor\"f\"quadraBinningFactor\"I\"gdcForwardPolynomial\"{?=\"c0\"f\"c2\"f\"c4\"f\"c6\"f\"c8\"f\"c10\"f\"c12\"f\"c14\"f}\"gdcInversePolynomial\"{?=\"c0\"f\"c2\"f\"c4\"f\"c6\"f\"c8\"f\"c10\"f\"c12\"f\"c14\"f}\"doUndistortion\"B\"stereoRectificationInverseHomography\"{?=\"columns\"[3]}\"applyStereoRectificationHomography\"B\"useBilinearInterpolation\"B\"precomputedGDCPolynomials\"B\"classifier\"{?=\"maskGatingThreshold\"I\"maximumFaceRectangleThreshold\"I\"minimumFaceRectangleThreshold\"I\"centerRadiusThreshold\"I\"centerRadiusScale\"f\"centerMaskThreshold\"I}\"barrelDistortionPolynomial\"[6f]\"inputImageDimensions\"{?=\"full\"{?=\"x0\"i\"y0\"i\"x1\"i\"y1\"i\"width\"i\"height\"i}\"valid\"{?=\"x0\"i\"y0\"i\"x1\"i\"y1\"i\"width\"i\"height\"i}\"sensor\"{?=\"x0\"i\"y0\"i\"x1\"i\"y1\"i\"width\"i\"height\"i}\"crop\"{?=\"x0\"i\"y0\"i\"x1\"i\"y1\"i\"width\"i\"height\"i}}\"outputImageDimensions\"{?=\"full\"{?=\"x0\"i\"y0\"i\"x1\"i\"y1\"i\"width\"i\"height\"i}}\"segmentationMaskBoundingRectangle\"{?=\"x0\"i\"y0\"i\"x1\"i\"y1\"i\"width\"i\"height\"i}\"lineDetector\"{?=\"downscaleFactor\"I\"gradientMagnitudeThreshold\"f\"gradientNormalizationRadius\"I\"anchorScanInterval\"I\"lineFitInitialLength\"I\"lineFitErrorThreshold\"f\"lineMergeDeviationThreshold\"f\"lineMergeDistanceThreshold\"f\"minimumLineLength\"I\"segmentationMaskDilationRadius\"I}\"contentPreservingWarping\"{?=\"esWeight1\"f\"esWeight2\"f\"edWeight\"f\"elWeight\"f\"pareDownConstant\"I\"segmentationMaskErosionRadius\"I}\"applyAdjustedEsWeights\"B\"numCurveOptions\"I\"curveOptions\"[10{?=\"coefficients\"[7f]}]\"numClassificationOptions\"I\"classificationOptions\"[10{?=\"gated\"B\"curveOption\"i\"distortionTarget\"f}]\"curveFalloffMu\"f\"curveFalloffSigma\"f}"
+ "i32@0:8^{?=BfffI{?=ffffffff}{?=ffffffff}B{?=[3]}BBB{?=IIIIfI}[6f]{?={?=iiiiii}{?=iiiiii}{?=iiiiii}{?=iiiiii}}{?={?=iiiiii}}{?=iiiiii}{?=IfIIIfffII}{?=ffffII}BI[10{?=[7f]}]I[10{?=Bif}]ff}16^24"
+ "i64@0:8^{?=BfffI{?=ffffffff}{?=ffffffff}B{?=[3]}BBB{?=IIIIfI}[6f]{?={?=iiiiii}{?=iiiiii}{?=iiiiii}{?=iiiiii}}{?={?=iiiiii}}{?=iiiiii}{?=IfIIIfffII}{?=ffffII}BI[10{?=[7f]}]I[10{?=Bif}]ff}16@24@32@40^{?=IIQ@}48^{?=@[4I]}56"
+ "_gdcInversePolynomial"
+ "v32@0:8^{?=BfffI{?=ffffffff}{?=ffffffff}B{?=[3]}BBB{?=IIIIfI}[6f]{?={?=iiiiii}{?=iiiiii}{?=iiiiii}{?=iiiiii}}{?={?=iiiiii}}{?=iiiiii}{?=IfIIIfffII}{?=ffffII}BI[10{?=[7f]}]I[10{?=Bif}]ff}16^24"
+ "\x0f\x03\xf0\xf0A"
+ "v32@0:8^{?=BB{?=f}{?=ffffffff}{?=ffffffff}BBf{?=[3]}BB}16^{?=BfffI{?=ffffffff}{?=ffffffff}B{?=[3]}BBB{?=IIIIfI}[6f]{?={?=iiiiii}{?=iiiiii}{?=iiiiii}{?=iiiiii}}{?={?=iiiiii}}{?=iiiiii}{?=IfIIIfffII}{?=ffffII}BI[10{?=[7f]}]I[10{?=Bif}]ff}24"
+ "setGdcInversePolynomial:"
+ "i48@0:8^{?=Q}16^{?=BfffI{?=ffffffff}{?=ffffffff}B{?=[3]}BBB{?=IIIIfI}[6f]{?={?=iiiiii}{?=iiiiii}{?=iiiiii}{?=iiiiii}}{?={?=iiiiii}}{?=iiiiii}{?=IfIIIfffII}{?=ffffII}BI[10{?=[7f]}]I[10{?=Bif}]ff}24I32I36I40I44"
+ "i48@0:8^{?=BfffI{?=ffffffff}{?=ffffffff}B{?=[3]}BBB{?=IIIIfI}[6f]{?={?=iiiiii}{?=iiiiii}{?=iiiiii}{?=iiiiii}}{?={?=iiiiii}}{?=iiiiii}{?=IfIIIfffII}{?=ffffII}BI[10{?=[7f]}]I[10{?=Bif}]ff}16@24@32@40"
+ "usePrecomputedPolynomialsAndOpticalCenterOffset"
+ "T@\"NSData\",&,N,V_gdcForwardPolynomial"
+ "applyStereoRectificationHomography"
+ "v24@0:8^{?=BfffI{?=ffffffff}{?=ffffffff}B{?=[3]}BBB{?=IIIIfI}[6f]{?={?=iiiiii}{?=iiiiii}{?=iiiiii}{?=iiiiii}}{?={?=iiiiii}}{?=iiiiii}{?=IfIIIfffII}{?=ffffII}BI[10{?=[7f]}]I[10{?=Bif}]ff}16"
+ "i156@0:8^{?=BfffI{?=ffffffff}{?=ffffffff}B{?=[3]}BBB{?=IIIIfI}[6f]{?={?=iiiiii}{?=iiiiii}{?=iiiiii}{?=iiiiii}}{?={?=iiiiii}}{?=iiiiii}{?=IfIIIfffII}{?=ffffII}BI[10{?=[7f]}]I[10{?=Bif}]ff}16@24@32{CGRect={CGPoint=dd}{CGSize=dd}}40{?=ii}72f80f84f88f92@96f104f108@112B120@124{?=iiiiii}132"
+ "setUsePrecomputedPolynomialsAndOpticalCenterOffset:"
+ "i48@0:8^{?=BfffI{?=ffffffff}{?=ffffffff}B{?=[3]}BBB{?=IIIIfI}[6f]{?={?=iiiiii}{?=iiiiii}{?=iiiiii}{?=iiiiii}}{?={?=iiiiii}}{?=iiiiii}{?=IfIIIfffII}{?=ffffII}BI[10{?=[7f]}]I[10{?=Bif}]ff}16@24^@32^i40"
+ "setGdcForwardPolynomial:"
+ "@\"NSData\"16@0:8"
+ "TB,N,V_usePrecomputedPolynomialsAndOpticalCenterOffset"
+ "{CGPoint=\"x\"d\"y\"d}"
+ "i40@0:8^{?=BfffI{?=ffffffff}{?=ffffffff}B{?=[3]}BBB{?=IIIIfI}[6f]{?={?=iiiiii}{?=iiiiii}{?=iiiiii}{?=iiiiii}}{?={?=iiiiii}}{?=iiiiii}{?=IfIIIfffII}{?=ffffII}BI[10{?=[7f]}]I[10{?=Bif}]ff}16^24*32"
+ "setApplyStereoRectificationHomography:"
+ "opticalCenterOffset"
+ "i40@0:8^{?=BfffI{?=ffffffff}{?=ffffffff}B{?=[3]}BBB{?=IIIIfI}[6f]{?={?=iiiiii}{?=iiiiii}{?=iiiiii}{?=iiiiii}}{?={?=iiiiii}}{?=iiiiii}{?=IfIIIfffII}{?=ffffII}BI[10{?=[7f]}]I[10{?=Bif}]ff}16@24@32"
+ "{?=\"parameters\"{?=\"inputToFullImageScalingCoefs\"\"fullImageToSensorImageOffset\"\"sensorImagePosToMeshCellPosScalingFactor\"\"finalImageDims\"\"replicatePixels\"B\"outputSecondaryToPrimaryCoef\"\"inputScalingCoef\"\"inputShift\"\"inputPrimaryToSecondaryCoef\"\"isDepthData\"B\"geometricDistortionCommon\"{?=\"center\"\"mmFactor\"f}\"inverseGeometricDistortionPolynomial\"{?=\"c0\"f\"c2\"f\"c4\"f\"c6\"f\"c8\"f\"c10\"f\"c12\"f\"c14\"f}\"forwardGeometricDistortionPolynomial\"{?=\"c0\"f\"c2\"f\"c4\"f\"c6\"f\"c8\"f\"c10\"f\"c12\"f\"c14\"f}\"doUndistortion\"B\"haveMesh\"B\"aspectRatio\"f\"stereoRectificationInverseHomography\"{?=\"columns\"[3]}\"applyStereoRectificationHomography\"B\"useBilinearInterpolation\"B}\"primaryOutputImageWidth\"I\"primaryOutputImageHeight\"I\"roi\"@\"<MTLBuffer>\"}"
+ "_stereoRectificationInverseHomography"
+ "T@\"NSData\",&,N"
+ "setStereoRectificationInverseHomography:"
+ "_usePrecomputedPolynomialsAndOpticalCenterOffset"
+ "gdcInversePolynomial"
+ "stereoRectificationInverseHomography"
+ "setUseBilinearInterpolation:"
+ "useBilinearInterpolation"
+ "I44@0:8^{?=BfffI{?=ffffffff}{?=ffffffff}B{?=[3]}BBB{?=IIIIfI}[6f]{?={?=iiiiii}{?=iiiiii}{?=iiiiii}{?=iiiiii}}{?={?=iiiiii}}{?=iiiiii}{?=IfIIIfffII}{?=ffffII}BI[10{?=[7f]}]I[10{?=Bif}]ff}16^{?=^I}24r^32I40"
+ "T@\"NSData\",&,N,V_gdcInversePolynomial"
+ "v40@0:8^{?=BfffI{?=ffffffff}{?=ffffffff}B{?=[3]}BBB{?=IIIIfI}[6f]{?={?=iiiiii}{?=iiiiii}{?=iiiiii}{?=iiiiii}}{?={?=iiiiii}}{?=iiiiii}{?=IfIIIfffII}{?=ffffII}BI[10{?=[7f]}]I[10{?=Bif}]ff}16@24^i32"
+ "v64@0:8{?=[3]}16"
+ "T{CGPoint=dd},N,V_opticalCenterOffset"
+ "i32@0:8^{?=BfffI{?=ffffffff}{?=ffffffff}B{?=[3]}BBB{?=IIIIfI}[6f]{?={?=iiiiii}{?=iiiiii}{?=iiiiii}{?=iiiiii}}{?={?=iiiiii}}{?=iiiiii}{?=IfIIIfffII}{?=ffffII}BI[10{?=[7f]}]I[10{?=Bif}]ff}16^{?=IIQ@}24"
+ "v32@0:8{CGPoint=dd}16"
+ "@\"NSData\""
+ "_opticalCenterOffset"
+ "_useBilinearInterpolation"
+ "i56@0:8^{?=BfffI{?=ffffffff}{?=ffffffff}B{?=[3]}BBB{?=IIIIfI}[6f]{?={?=iiiiii}{?=iiiiii}{?=iiiiii}{?=iiiiii}}{?={?=iiiiii}}{?=iiiiii}{?=IfIIIfffII}{?=ffffII}BI[10{?=[7f]}]I[10{?=Bif}]ff}16@24@32@40^{?=iiiiii}48"
+ "T{CGPoint=dd},N"
+ "TB,N,V_useBilinearInterpolation"
+ "T{?=[3]},N"
+ "gdcForwardPolynomial"
+ "{CGPoint=dd}16@0:8"
+ "TB,N,V_applyStereoRectificationHomography"
+ "\x02r#C\xf0\xf0\xf0\xf0\xf0\xf0\xf0$u2"
+ "v24@0:8@\"NSData\"16"
+ "_gdcForwardPolynomial"
+ "T{?=[3]},N,V_stereoRectificationInverseHomography"
- "i48@0:8^{?=BfffI{?=ffffffff}{?=ffffffff}B{?=IIIIfI}[6f]{?={?=iiiiii}{?=iiiiii}{?=iiiiii}{?=iiiiii}}{?={?=iiiiii}}{?=iiiiii}{?=IfIIIfffII}{?=ffffII}BI[10{?=[7f]}]I[10{?=Bif}]ff}16@24^@32^i40"
- "i32@0:8^{?=BfffI{?=ffffffff}{?=ffffffff}B{?=IIIIfI}[6f]{?={?=iiiiii}{?=iiiiii}{?=iiiiii}{?=iiiiii}}{?={?=iiiiii}}{?=iiiiii}{?=IfIIIfffII}{?=ffffII}BI[10{?=[7f]}]I[10{?=Bif}]ff}16^{?=IIQ@}24"
- "{?=\"parameters\"{?=\"inputToFullImageScalingCoefs\"\"fullImageToSensorImageOffset\"\"sensorImagePosToMeshCellPosScalingFactor\"\"finalImageDims\"\"replicatePixels\"B\"outputSecondaryToPrimaryCoef\"\"inputScalingCoef\"\"inputShift\"\"inputPrimaryToSecondaryCoef\"\"isDepthData\"B\"geometricDistortionCommon\"{?=\"center\"\"mmFactor\"f}\"inverseGeometricDistortionPolynomial\"{?=\"c0\"f\"c2\"f\"c4\"f\"c6\"f\"c8\"f\"c10\"f\"c12\"f\"c14\"f}\"forwardGeometricDistortionPolynomial\"{?=\"c0\"f\"c2\"f\"c4\"f\"c6\"f\"c8\"f\"c10\"f\"c12\"f\"c14\"f}\"doUndistortion\"B\"haveMesh\"B\"aspectRatio\"f}\"primaryOutputImageWidth\"I\"primaryOutputImageHeight\"I\"roi\"@\"<MTLBuffer>\"}"
- "i40@0:8^{?=BfffI{?=ffffffff}{?=ffffffff}B{?=IIIIfI}[6f]{?={?=iiiiii}{?=iiiiii}{?=iiiiii}{?=iiiiii}}{?={?=iiiiii}}{?=iiiiii}{?=IfIIIfffII}{?=ffffII}BI[10{?=[7f]}]I[10{?=Bif}]ff}16^24*32"
- "v24@0:8^{?=BfffI{?=ffffffff}{?=ffffffff}B{?=IIIIfI}[6f]{?={?=iiiiii}{?=iiiiii}{?=iiiiii}{?=iiiiii}}{?={?=iiiiii}}{?=iiiiii}{?=IfIIIfffII}{?=ffffII}BI[10{?=[7f]}]I[10{?=Bif}]ff}16"
- "v32@0:8^{?=BfffI{?=ffffffff}{?=ffffffff}B{?=IIIIfI}[6f]{?={?=iiiiii}{?=iiiiii}{?=iiiiii}{?=iiiiii}}{?={?=iiiiii}}{?=iiiiii}{?=IfIIIfffII}{?=ffffII}BI[10{?=[7f]}]I[10{?=Bif}]ff}16^24"
- "\x0f\x03\xf0\x91"
- "i64@0:8^{?=BfffI{?=ffffffff}{?=ffffffff}B{?=IIIIfI}[6f]{?={?=iiiiii}{?=iiiiii}{?=iiiiii}{?=iiiiii}}{?={?=iiiiii}}{?=iiiiii}{?=IfIIIfffII}{?=ffffII}BI[10{?=[7f]}]I[10{?=Bif}]ff}16@24@32@40^{?=IIQ@}48^{?=@[4I]}56"
- "\x02r#C\xf0\xf0\xf0\xf0\xf0\xf0\x94s2"
- "v32@0:8^{?=BB{?=f}{?=ffffffff}{?=ffffffff}BBf}16^{?=BfffI{?=ffffffff}{?=ffffffff}B{?=IIIIfI}[6f]{?={?=iiiiii}{?=iiiiii}{?=iiiiii}{?=iiiiii}}{?={?=iiiiii}}{?=iiiiii}{?=IfIIIfffII}{?=ffffII}BI[10{?=[7f]}]I[10{?=Bif}]ff}24"
- "i48@0:8^{?=Q}16^{?=BfffI{?=ffffffff}{?=ffffffff}B{?=IIIIfI}[6f]{?={?=iiiiii}{?=iiiiii}{?=iiiiii}{?=iiiiii}}{?={?=iiiiii}}{?=iiiiii}{?=IfIIIfffII}{?=ffffII}BI[10{?=[7f]}]I[10{?=Bif}]ff}24I32I36I40I44"
- "i56@0:8^{?=BfffI{?=ffffffff}{?=ffffffff}B{?=IIIIfI}[6f]{?={?=iiiiii}{?=iiiiii}{?=iiiiii}{?=iiiiii}}{?={?=iiiiii}}{?=iiiiii}{?=IfIIIfffII}{?=ffffII}BI[10{?=[7f]}]I[10{?=Bif}]ff}16@24@32@40^{?=iiiiii}48"
- "v40@0:8^{?=BfffI{?=ffffffff}{?=ffffffff}B{?=IIIIfI}[6f]{?={?=iiiiii}{?=iiiiii}{?=iiiiii}{?=iiiiii}}{?={?=iiiiii}}{?=iiiiii}{?=IfIIIfffII}{?=ffffII}BI[10{?=[7f]}]I[10{?=Bif}]ff}16@24^i32"
- "i48@0:8^{?=BfffI{?=ffffffff}{?=ffffffff}B{?=IIIIfI}[6f]{?={?=iiiiii}{?=iiiiii}{?=iiiiii}{?=iiiiii}}{?={?=iiiiii}}{?=iiiiii}{?=IfIIIfffII}{?=ffffII}BI[10{?=[7f]}]I[10{?=Bif}]ff}16@24@32@40"
- "I44@0:8^{?=BfffI{?=ffffffff}{?=ffffffff}B{?=IIIIfI}[6f]{?={?=iiiiii}{?=iiiiii}{?=iiiiii}{?=iiiiii}}{?={?=iiiiii}}{?=iiiiii}{?=IfIIIfffII}{?=ffffII}BI[10{?=[7f]}]I[10{?=Bif}]ff}16^{?=^I}24r^32I40"
- "i40@0:8^{?=BfffI{?=ffffffff}{?=ffffffff}B{?=IIIIfI}[6f]{?={?=iiiiii}{?=iiiiii}{?=iiiiii}{?=iiiiii}}{?={?=iiiiii}}{?=iiiiii}{?=IfIIIfffII}{?=ffffII}BI[10{?=[7f]}]I[10{?=Bif}]ff}16@24@32"
- "i64@0:8^{?=BfffI{?=ffffffff}{?=ffffffff}B{?=IIIIfI}[6f]{?={?=iiiiii}{?=iiiiii}{?=iiiiii}{?=iiiiii}}{?={?=iiiiii}}{?=iiiiii}{?=IfIIIfffII}{?=ffffII}BI[10{?=[7f]}]I[10{?=Bif}]ff}16@24@32@40@48@56"
- "i32@0:8^{?=BfffI{?=ffffffff}{?=ffffffff}B{?=IIIIfI}[6f]{?={?=iiiiii}{?=iiiiii}{?=iiiiii}{?=iiiiii}}{?={?=iiiiii}}{?=iiiiii}{?=IfIIIfffII}{?=ffffII}BI[10{?=[7f]}]I[10{?=Bif}]ff}16^24"
- "{?=\"finalImageDimensions\"\"replicatePixels\"B\"digitalZoomRatio\"f\"pixelSize\"f\"opticalCenterOffset\"\"dynamicDistortionFactor\"f\"quadraBinningFactor\"I\"gdcForwardPolynomial\"{?=\"c0\"f\"c2\"f\"c4\"f\"c6\"f\"c8\"f\"c10\"f\"c12\"f\"c14\"f}\"gdcInversePolynomial\"{?=\"c0\"f\"c2\"f\"c4\"f\"c6\"f\"c8\"f\"c10\"f\"c12\"f\"c14\"f}\"doUndistortion\"B\"classifier\"{?=\"maskGatingThreshold\"I\"maximumFaceRectangleThreshold\"I\"minimumFaceRectangleThreshold\"I\"centerRadiusThreshold\"I\"centerRadiusScale\"f\"centerMaskThreshold\"I}\"barrelDistortionPolynomial\"[6f]\"inputImageDimensions\"{?=\"full\"{?=\"x0\"i\"y0\"i\"x1\"i\"y1\"i\"width\"i\"height\"i}\"valid\"{?=\"x0\"i\"y0\"i\"x1\"i\"y1\"i\"width\"i\"height\"i}\"sensor\"{?=\"x0\"i\"y0\"i\"x1\"i\"y1\"i\"width\"i\"height\"i}\"crop\"{?=\"x0\"i\"y0\"i\"x1\"i\"y1\"i\"width\"i\"height\"i}}\"outputImageDimensions\"{?=\"full\"{?=\"x0\"i\"y0\"i\"x1\"i\"y1\"i\"width\"i\"height\"i}}\"segmentationMaskBoundingRectangle\"{?=\"x0\"i\"y0\"i\"x1\"i\"y1\"i\"width\"i\"height\"i}\"lineDetector\"{?=\"downscaleFactor\"I\"gradientMagnitudeThreshold\"f\"gradientNormalizationRadius\"I\"anchorScanInterval\"I\"lineFitInitialLength\"I\"lineFitErrorThreshold\"f\"lineMergeDeviationThreshold\"f\"lineMergeDistanceThreshold\"f\"minimumLineLength\"I\"segmentationMaskDilationRadius\"I}\"contentPreservingWarping\"{?=\"esWeight1\"f\"esWeight2\"f\"edWeight\"f\"elWeight\"f\"pareDownConstant\"I\"segmentationMaskErosionRadius\"I}\"applyAdjustedEsWeights\"B\"numCurveOptions\"I\"curveOptions\"[10{?=\"coefficients\"[7f]}]\"numClassificationOptions\"I\"classificationOptions\"[10{?=\"gated\"B\"curveOption\"i\"distortionTarget\"f}]\"curveFalloffMu\"f\"curveFalloffSigma\"f}"
- "i156@0:8^{?=BfffI{?=ffffffff}{?=ffffffff}B{?=IIIIfI}[6f]{?={?=iiiiii}{?=iiiiii}{?=iiiiii}{?=iiiiii}}{?={?=iiiiii}}{?=iiiiii}{?=IfIIIfffII}{?=ffffII}BI[10{?=[7f]}]I[10{?=Bif}]ff}16@24@32{CGRect={CGPoint=dd}{CGSize=dd}}40{?=ii}72f80f84f88f92@96f104f108@112B120@124{?=iiiiii}132"

```
