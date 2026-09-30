## ASEProcessing

> `/System/Library/PrivateFrameworks/ASEProcessing.framework/ASEProcessing`

```diff

-1.46.3.0.0
-  __TEXT.__text: 0x7544
-  __TEXT.__auth_stubs: 0x280
-  __TEXT.__objc_methlist: 0x294
+1.48.0.0.0
+  __TEXT.__text: 0x8f90
+  __TEXT.__auth_stubs: 0x2c0
+  __TEXT.__objc_methlist: 0x2dc
   __TEXT.__const: 0x1be2c
-  __TEXT.__oslogstring: 0x25c
-  __TEXT.__cstring: 0x340
-  __TEXT.__unwind_info: 0x148
+  __TEXT.__cstring: 0x380
+  __TEXT.__oslogstring: 0x27d
+  __TEXT.__unwind_info: 0x160
   __TEXT.__objc_classname: 0x32
-  __TEXT.__objc_methname: 0x6d4
-  __TEXT.__objc_methtype: 0x1ae3
-  __TEXT.__objc_stubs: 0x4a0
+  __TEXT.__objc_methname: 0x7ea
+  __TEXT.__objc_methtype: 0x23fe
+  __TEXT.__objc_stubs: 0x4e0
   __DATA_CONST.__got: 0x48
-  __DATA_CONST.__const: 0x168
+  __DATA_CONST.__const: 0x188
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x158
+  __DATA_CONST.__objc_selrefs: 0x180
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x148
+  __AUTH_CONST.__auth_got: 0x168
+  __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x160
-  __AUTH_CONST.__objc_const: 0x600
-  __DATA.__objc_ivar: 0x80
-  __DATA.__data: 0x1ad00
-  __DATA.__common: 0x14
+  __AUTH_CONST.__objc_const: 0x630
+  __DATA.__objc_ivar: 0x84
+  __DATA.__data: 0x1af80
+  __DATA.__bss: 0x8
+  __DATA.__common: 0x1c
   __DATA_DIRTY.__objc_data: 0xf0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/Frameworks/IOSurface.framework/IOSurface
   - /System/Library/PrivateFrameworks/IOSurfaceAccelerator.framework/IOSurfaceAccelerator
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9578484A-3C20-3E9E-8644-01D11FBF99DC
-  Functions: 101
-  Symbols:   757
-  CStrings:  167
+  UUID: 98E602CC-9470-3180-BB9E-643DBC5508CF
+  Functions: 115
+  Symbols:   809
+  CStrings:  184
 
Symbols:
+ -[ASEProcessing inputType]
+ -[ASEProcessing processFrameWithInput:Measurement:Output:]
+ -[ASEProcessing processFrameWithInput:Measurement:callback:]
+ -[ASEProcessing processFrameWithInput:Measurement:outputData:]
+ -[ASEProcessing setInputType:]
+ -[ASEProcessingT0 configControlHeader_V1:]
+ -[ASEProcessingT0 configControlHeader_V2:]
+ -[ASEProcessingT0 processFrameWithInput:Measurement:Output:]
+ -[ASEProcessingT0 processFrameWithInput:Measurement:callback:]
+ -[ASEProcessingT0 processFrameWithInput:Measurement:outputData:]
+ -[ASEProcessingT0 processPixelWithInput:Measurement:controlUnit:]
+ -[ASEProcessingT0 processPixelWithInput_V1:Measurement:Output:]
+ -[ASEProcessingT0 processPixelWithInput_V2:Measurement:Output:]
+ -[ASEProcessingT0 processPixelWithMeasurement_V1:Measurement:pixelControl:]
+ -[ASEProcessingT0 processPixelWithMeasurement_V2:Measurement:Output:]
+ -[ASEProcessingT0 processPixelWithPixelControl_V1:Output:]
+ -[ASEProcessingT0 processPixelWithPixelControl_V2:Output:]
+ -[ASEProcessingT0 setInputType:]
+ -[ASEProcessingT1 processFrameWithInput:Measurement:callback:]
+ -[ASEProcessingT1 processFrameWithInput:Measurement:outputData:]
+ -[ASEProcessingT1 processPixelWithInput:Measurement:controlUnitV3:]
+ -[ASEProcessingT1 processPixelWithInput_V3:Measurement:Output:]
+ -[ASEProcessingT1 processPixelWithMeasurement_V3:Measurement:Output:]
+ -[ASEProcessingT1 processPixelWithPixelControl_V3:Output:]
+ OBJC_IVAR_$_ASEProcessingT0._inputType
+ _IOSurfaceGetBulkAttachments
+ _IOSurfaceGetPixelFormat
+ _OBJC_IVAR_$_ASEProcessing._inputType
+ __NSConcreteGlobalBlock
+ ___62-[ASEProcessingT0 processFrameWithInput:Measurement:callback:]_block_invoke
+ ___62-[ASEProcessingT0 processFrameWithInput:Measurement:callback:]_block_invoke_2
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_436_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_literal_global
+ ___getFourCCforType_block_invoke
+ _disableSampleShift
+ _dispatch_once
+ _getFourCCforType
+ _getFourCCforType.cold.1
+ _getFourCCforType.onceToken
+ _getInputType
+ _getInputTypeString
+ _getTransferFunction
+ _getTransferFunctionString
+ _lumaBlend_FixedSettingDigitalZoom_V1
+ _lumaBlend_FixedSettingDigitalZoom_V2
+ _lumaBlend_FixedSettingGraphics_V1
+ _lumaBlend_FixedSettingGraphics_V2
+ _lumaBlend_FixedSettingLivePhoto_V1
+ _lumaBlend_FixedSettingLivePhoto_V2
+ _lumaBlend_SettingVideo_Heavy_FG_V2
+ _lumaBlend_SettingVideo_NFG_V2
+ _lumaBlend_SettingVideo_level1_FG_V2
+ _lumaBlend_SettingVideo_level2_FG_V2
+ _lumaBlend_SettingVideo_level3_FG_V2
+ _lumaBlend_SettingVideo_light_FG_V2
+ _lumaBlend_default
+ _objc_msgSend$configControlHeader_V1:
+ _objc_msgSend$configControlHeader_V2:
+ _objc_msgSend$inputType
+ _objc_msgSend$processFrameWithInput:Measurement:Output:
+ _objc_msgSend$processFrameWithInput:Measurement:callback:
+ _objc_msgSend$processFrameWithInput:Measurement:outputData:
+ _objc_msgSend$processPixelWithInput:Measurement:controlUnit:
+ _objc_msgSend$processPixelWithInput:Measurement:controlUnitV3:
+ _objc_msgSend$processPixelWithInput_V1:Measurement:Output:
+ _objc_msgSend$processPixelWithInput_V2:Measurement:Output:
+ _objc_msgSend$processPixelWithInput_V3:Measurement:Output:
+ _objc_msgSend$processPixelWithMeasurement_V1:Measurement:pixelControl:
+ _objc_msgSend$processPixelWithMeasurement_V2:Measurement:Output:
+ _objc_msgSend$processPixelWithMeasurement_V3:Measurement:Output:
+ _objc_msgSend$processPixelWithPixelControl_V1:Output:
+ _objc_msgSend$processPixelWithPixelControl_V2:Output:
+ _objc_msgSend$processPixelWithPixelControl_V3:Output:
+ _objc_msgSend$setInputType:
+ _objc_retain_x22
+ _objc_retain_x4
+ _overrideEnhancement
+ _overrideFGLevel
+ _overrideInputTransferFunction
+ _overrideInputType
+ _readDefaultsWriteEnabled
+ _updateConfigsPerFrame
- -[ASEProcessingT0 configControlHeader:]
- -[ASEProcessingT0 processFrameWithInput:Output:]
- -[ASEProcessingT0 processFrameWithInput:callback:]
- -[ASEProcessingT0 processFrameWithInput:outputData:]
- -[ASEProcessingT0 processPixelWithInput:Output:]
- -[ASEProcessingT0 processPixelWithInput:controlUnit:]
- -[ASEProcessingT0 processPixelWithInput_V1:Output:]
- -[ASEProcessingT0 processPixelWithInput_V2:Output:]
- -[ASEProcessingT0 processPixelWithMeasurement_V1:pixelControl:]
- -[ASEProcessingT0 processPixelWithMeasurement_V2:Output:]
- -[ASEProcessingT0 processPixelWithPixelControl_V1:]
- -[ASEProcessingT0 processPixelWithPixelControl_V2:]
- -[ASEProcessingT1 processFrameWithInput:callback:]
- -[ASEProcessingT1 processFrameWithInput:outputData:]
- -[ASEProcessingT1 processPixelWithInput:controlUnitV3:]
- -[ASEProcessingT1 processPixelWithInput_V3:Output:]
- -[ASEProcessingT1 processPixelWithMeasurement_V3:Output:]
- -[ASEProcessingT1 processPixelWithPixelControl_V3:]
- _OBJC_IVAR_$_ASEProcessingT0._aseFrameProcessing
- ___50-[ASEProcessingT0 processFrameWithInput:callback:]_block_invoke
- ___50-[ASEProcessingT0 processFrameWithInput:callback:]_block_invoke_2
- ___block_descriptor_428_e8_32s40bs_e5_v8?0ls32l8s40l8
- _objc_msgSend$configControlHeader:
- _objc_msgSend$processFrameWithInput:Output:
- _objc_msgSend$processFrameWithInput:callback:
- _objc_msgSend$processFrameWithInput:outputData:
- _objc_msgSend$processPixelWithInput:Output:
- _objc_msgSend$processPixelWithInput:controlUnit:
- _objc_msgSend$processPixelWithInput:controlUnitV3:
- _objc_msgSend$processPixelWithInput_V1:Output:
- _objc_msgSend$processPixelWithInput_V2:Output:
- _objc_msgSend$processPixelWithInput_V3:Output:
- _objc_msgSend$processPixelWithMeasurement_V1:pixelControl:
- _objc_msgSend$processPixelWithMeasurement_V2:Output:
- _objc_msgSend$processPixelWithMeasurement_V3:Output:
- _objc_msgSend$processPixelWithPixelControl_V1:
- _objc_msgSend$processPixelWithPixelControl_V2:
- _objc_msgSend$processPixelWithPixelControl_V3:
- _objc_retain_x21
CStrings:
+ " [1.48.0]     %s: src={ %dw x %dh }, dest={ %dw x %dh }, aseFunctionOnYesOffNo=%d\n"
+ " [1.48.0]     %s: src={ %dw x %dh }, dest={ %dw x %dh }, aseFunctionOnYesOffNo=%d, fps=%f\n"
+ " [1.48.0] %s : bad argument, retVal=%ld, input=%p, aseMeasurementOutput=%p, completionCallback=%p\n"
+ " [1.48.0] %s : config=%p"
+ " [1.48.0] %s : input=%p, aseMeasurementOutput=%p, aseFrameProcessingControl=%p"
+ " [1.48.0] %s : instance=%p, productType=%u, destinationWidth=%d, destinationHeight=%d, inputType=%s"
+ " [1.48.0] %s : unknownProcessingType=%d, strength=%f, wxh=%dx%d"
+ " [1.48.0] %s : unknownProcessingType=%d, strength=%f, wxh=%dx%d\n"
+ " [1.48.0] ++ %s: ASEApiVer=%d\n"
+ "-[ASEProcessingT0 processFrameWithInput:Measurement:Output:]"
+ "-[ASEProcessingT0 processFrameWithInput:Measurement:callback:]"
+ "-[ASEProcessingT0 processFrameWithInput:Measurement:outputData:]"
+ "-[ASEProcessingT1 processFrameWithInput:Measurement:outputData:]"
+ "@24@0:8^{aseConfigurationUnitsV3_t={MSRHcuHeader_t=II}{MSRHcuEntryHeader_t=II}{?=IIIIII}{MSRHcuEntryHeader_t=II}{?=[4[32f]]}{MSRHcuEntryHeader_t=II}{?=I{?=[32{?=fff}]}{?=[32{?=fff}]}{?=[32{?=fff}]}{?=IIIII}[2i][3i][4i][5i][6i][7i]}{MSRHcuEntryHeader_t=II}{?=[5{?=[32{?=fff}]}]{?=III}[13{?=II}][6{?=III}]}{MSRHcuEntryHeader_t=II}{?=[4{?=[32{?=fff}]}]{?=IIII}}{MSRHcuEntryHeader_t=II}{?=II}{MSRHcuEntryHeader_t=II}{?={?={?=II}{?=III}}}}16"
+ "B"
+ "B16@0:8"
+ "HDR"
+ "PQ"
+ "SDR"
+ "TB,N,V_inputType"
+ "^{aseConfigurationUnitsV2_t={MSRHcuHeader_t=II}{MSRHcuEntryHeader_t=II}{?={?=(?={?=iIB(?={?=BI{?=III}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIIII}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIII}{?={?=II}{?=III}}})})}}{MSRHcuEntryHeader_t=II}{?=I}{MSRHcuEntryHeader_t=II}{?={?=fffff}}{MSRHcuEntryHeader_t=II}{?={?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}}{MSRHcuEntryHeader_t=II}{?={?=IIIII}{?=IIIII}{?=IIIII}}{MSRHcuEntryHeader_t=II}{?=[4{?=b11b11b10}][4{?=b12b12b8}][4{?=b11b11b10}]}}"
+ "^{aseConfigurationUnitsV3_t={MSRHcuHeader_t=II}{MSRHcuEntryHeader_t=II}{?=IIIIII}{MSRHcuEntryHeader_t=II}{?=[4[32f]]}{MSRHcuEntryHeader_t=II}{?=I{?=[32{?=fff}]}{?=[32{?=fff}]}{?=[32{?=fff}]}{?=IIIII}[2i][3i][4i][5i][6i][7i]}{MSRHcuEntryHeader_t=II}{?=[5{?=[32{?=fff}]}]{?=III}[13{?=II}][6{?=III}]}{MSRHcuEntryHeader_t=II}{?=[4{?=[32{?=fff}]}]{?=IIII}}{MSRHcuEntryHeader_t=II}{?=II}{MSRHcuEntryHeader_t=II}{?={?={?=II}{?=III}}}}"
+ "_inputType"
+ "configControlHeader_V1:"
+ "configControlHeader_V2:"
+ "inputType"
+ "processFrameWithInput:Measurement:Output:"
+ "processFrameWithInput:Measurement:callback:"
+ "processFrameWithInput:Measurement:outputData:"
+ "processPixelWithInput:Measurement:controlUnit:"
+ "processPixelWithInput:Measurement:controlUnitV3:"
+ "processPixelWithInput_V1:Measurement:Output:"
+ "processPixelWithInput_V2:Measurement:Output:"
+ "processPixelWithInput_V3:Measurement:Output:"
+ "processPixelWithMeasurement_V1:Measurement:pixelControl:"
+ "processPixelWithMeasurement_V2:Measurement:Output:"
+ "processPixelWithMeasurement_V3:Measurement:Output:"
+ "processPixelWithPixelControl_V1:Output:"
+ "processPixelWithPixelControl_V2:Output:"
+ "processPixelWithPixelControl_V3:Output:"
+ "q40@0:8^{__IOSurface=}16^{?=IIIIIIIIIIIIIII[8I][8I][8I][8I][16I][16I][16I]}24@?32"
+ "q40@0:8^{__IOSurface=}16^{?=IIIIIIIIIIIIIII[8I][8I][8I][8I][16I][16I][16I]}24^@32"
+ "q40@0:8^{__IOSurface=}16^{?=IIIIIIIIIIIIIII[8I][8I][8I][8I][16I][16I][16I]}24^{?=(?={?=iIB(?={?=BI{?=III}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIIII}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIII}{?={?=II}{?=III}}})})}32"
+ "sRGB"
+ "setInputType:"
+ "v20@0:8B16"
+ "v24@0:8^{aseConfigurationUnitsV1_t={MSRHcuHeader_t=II}{MSRHcuEntryHeader_t=II}{?={?=(?={?=iIB(?={?=BI{?=III}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIIII}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIII}{?={?=II}{?=III}}})})}}{MSRHcuEntryHeader_t=II}{?=[4{?=b11b11b10}][4{?=b12b12b8}][4{?=b11b11b10}]}}16"
+ "v24@0:8^{aseConfigurationUnitsV2_t={MSRHcuHeader_t=II}{MSRHcuEntryHeader_t=II}{?={?=(?={?=iIB(?={?=BI{?=III}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIIII}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIII}{?={?=II}{?=III}}})})}}{MSRHcuEntryHeader_t=II}{?=I}{MSRHcuEntryHeader_t=II}{?={?=fffff}}{MSRHcuEntryHeader_t=II}{?={?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}}{MSRHcuEntryHeader_t=II}{?={?=IIIII}{?=IIIII}{?=IIIII}}{MSRHcuEntryHeader_t=II}{?=[4{?=b11b11b10}][4{?=b12b12b8}][4{?=b11b11b10}]}}16"
+ "v24@0:8^{aseConfigurationUnitsV3_t={MSRHcuHeader_t=II}{MSRHcuEntryHeader_t=II}{?=IIIIII}{MSRHcuEntryHeader_t=II}{?=[4[32f]]}{MSRHcuEntryHeader_t=II}{?=I{?=[32{?=fff}]}{?=[32{?=fff}]}{?=[32{?=fff}]}{?=IIIII}[2i][3i][4i][5i][6i][7i]}{MSRHcuEntryHeader_t=II}{?=[5{?=[32{?=fff}]}]{?=III}[13{?=II}][6{?=III}]}{MSRHcuEntryHeader_t=II}{?=[4{?=[32{?=fff}]}]{?=IIII}}{MSRHcuEntryHeader_t=II}{?=II}{MSRHcuEntryHeader_t=II}{?={?={?=II}{?=III}}}}16"
+ "v32@0:8^{__IOSurface=}16^{aseConfigurationUnitsV1_t={MSRHcuHeader_t=II}{MSRHcuEntryHeader_t=II}{?={?=(?={?=iIB(?={?=BI{?=III}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIIII}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIII}{?={?=II}{?=III}}})})}}{MSRHcuEntryHeader_t=II}{?=[4{?=b11b11b10}][4{?=b12b12b8}][4{?=b11b11b10}]}}24"
+ "v32@0:8^{__IOSurface=}16^{aseConfigurationUnitsV2_t={MSRHcuHeader_t=II}{MSRHcuEntryHeader_t=II}{?={?=(?={?=iIB(?={?=BI{?=III}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIIII}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIII}{?={?=II}{?=III}}})})}}{MSRHcuEntryHeader_t=II}{?=I}{MSRHcuEntryHeader_t=II}{?={?=fffff}}{MSRHcuEntryHeader_t=II}{?={?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}}{MSRHcuEntryHeader_t=II}{?={?=IIIII}{?=IIIII}{?=IIIII}}{MSRHcuEntryHeader_t=II}{?=[4{?=b11b11b10}][4{?=b12b12b8}][4{?=b11b11b10}]}}24"
+ "v32@0:8^{__IOSurface=}16^{aseConfigurationUnitsV3_t={MSRHcuHeader_t=II}{MSRHcuEntryHeader_t=II}{?=IIIIII}{MSRHcuEntryHeader_t=II}{?=[4[32f]]}{MSRHcuEntryHeader_t=II}{?=I{?=[32{?=fff}]}{?=[32{?=fff}]}{?=[32{?=fff}]}{?=IIIII}[2i][3i][4i][5i][6i][7i]}{MSRHcuEntryHeader_t=II}{?=[5{?=[32{?=fff}]}]{?=III}[13{?=II}][6{?=III}]}{MSRHcuEntryHeader_t=II}{?=[4{?=[32{?=fff}]}]{?=IIII}}{MSRHcuEntryHeader_t=II}{?=II}{MSRHcuEntryHeader_t=II}{?={?={?=II}{?=III}}}}24"
+ "v40@0:8^{__IOSurface=}16r^{?=IIIIIIIIIIIIIII[8I][8I][8I][8I][16I][16I][16I][5I][5I][5I][5I]I}24^{aseConfigurationUnitsV3_t={MSRHcuHeader_t=II}{MSRHcuEntryHeader_t=II}{?=IIIIII}{MSRHcuEntryHeader_t=II}{?=[4[32f]]}{MSRHcuEntryHeader_t=II}{?=I{?=[32{?=fff}]}{?=[32{?=fff}]}{?=[32{?=fff}]}{?=IIIII}[2i][3i][4i][5i][6i][7i]}{MSRHcuEntryHeader_t=II}{?=[5{?=[32{?=fff}]}]{?=III}[13{?=II}][6{?=III}]}{MSRHcuEntryHeader_t=II}{?=[4{?=[32{?=fff}]}]{?=IIII}}{MSRHcuEntryHeader_t=II}{?=II}{MSRHcuEntryHeader_t=II}{?={?={?=II}{?=III}}}}32"
+ "v40@0:8^{__IOSurface=}16r^{?=IIIIIIIIIIIIIII[8I][8I][8I][8I][16I][16I][16I]}24^{aseConfigurationUnitsV1_t={MSRHcuHeader_t=II}{MSRHcuEntryHeader_t=II}{?={?=(?={?=iIB(?={?=BI{?=III}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIIII}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIII}{?={?=II}{?=III}}})})}}{MSRHcuEntryHeader_t=II}{?=[4{?=b11b11b10}][4{?=b12b12b8}][4{?=b11b11b10}]}}32"
+ "v40@0:8^{__IOSurface=}16r^{?=IIIIIIIIIIIIIII[8I][8I][8I][8I][16I][16I][16I]}24^{aseConfigurationUnitsV2_t={MSRHcuHeader_t=II}{MSRHcuEntryHeader_t=II}{?={?=(?={?=iIB(?={?=BI{?=III}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIIII}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIII}{?={?=II}{?=III}}})})}}{MSRHcuEntryHeader_t=II}{?=I}{MSRHcuEntryHeader_t=II}{?={?=fffff}}{MSRHcuEntryHeader_t=II}{?={?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}}{MSRHcuEntryHeader_t=II}{?={?=IIIII}{?=IIIII}{?=IIIII}}{MSRHcuEntryHeader_t=II}{?=[4{?=b11b11b10}][4{?=b12b12b8}][4{?=b11b11b10}]}}32"
- " [1.46.3]     %s: src={ %dw x %dh }, dest={ %dw x %dh }, aseFunctionOnYesOffNo=%d\n"
- " [1.46.3]     %s: src={ %dw x %dh }, dest={ %dw x %dh }, aseFunctionOnYesOffNo=%d, fps=%f\n"
- " [1.46.3] %s : aseMeasurementOutput=%p, aseFrameProcessingControl=%p"
- " [1.46.3] %s : bad argument, retVal=%ld, aseMeasurementOutput=%p, completionCallback=%p\n"
- " [1.46.3] %s : config=%p"
- " [1.46.3] %s : instance=%p, productType=%u, destinationWidth=%d,  destinationHeight=%d"
- " [1.46.3] %s : unknownProcessingType=%d, strength=%f, wxh=%dx%d"
- " [1.46.3] %s : unknownProcessingType=%d, strength=%f, wxh=%dx%d\n"
- " [1.46.3] ++ %s: ASEApiVer=%d\n"
- "-[ASEProcessingT0 processFrameWithInput:Output:]"
- "-[ASEProcessingT0 processFrameWithInput:callback:]"
- "-[ASEProcessingT0 processFrameWithInput:outputData:]"
- "-[ASEProcessingT1 processFrameWithInput:outputData:]"
- "@24@0:8^{hwConfigurationUnitsV3_t={MSRHcuHeader_t=II}{MSRHcuEntryHeader_t=II}{?=IIIIII}{MSRHcuEntryHeader_t=II}{?=[4[32f]]}{MSRHcuEntryHeader_t=II}{?=I{?=[32{?=fff}]}{?=[32{?=fff}]}{?=[32{?=fff}]}{?=IIIII}[2i][3i][4i][5i][6i][7i]}{MSRHcuEntryHeader_t=II}{?=[5{?=[32{?=fff}]}]{?=III}[13{?=II}][6{?=III}]}{MSRHcuEntryHeader_t=II}{?=[4{?=[32{?=fff}]}]{?=IIII}}{MSRHcuEntryHeader_t=II}{?=II}{MSRHcuEntryHeader_t=II}{?={?={?=II}{?=III}}}}16"
- "^{?=(?={?=iIB(?={?=BI{?=III}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIIII}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIII}{?={?=II}{?=III}}})})}"
- "^{hwConfigurationUnitsV3_t={MSRHcuHeader_t=II}{MSRHcuEntryHeader_t=II}{?=IIIIII}{MSRHcuEntryHeader_t=II}{?=[4[32f]]}{MSRHcuEntryHeader_t=II}{?=I{?=[32{?=fff}]}{?=[32{?=fff}]}{?=[32{?=fff}]}{?=IIIII}[2i][3i][4i][5i][6i][7i]}{MSRHcuEntryHeader_t=II}{?=[5{?=[32{?=fff}]}]{?=III}[13{?=II}][6{?=III}]}{MSRHcuEntryHeader_t=II}{?=[4{?=[32{?=fff}]}]{?=IIII}}{MSRHcuEntryHeader_t=II}{?=II}{MSRHcuEntryHeader_t=II}{?={?={?=II}{?=III}}}}"
- "^{hwConfigurationUnits_t={MSRHcuHeader_t=II}{MSRHcuEntryHeader_t=II}{?={?=(?={?=iIB(?={?=BI{?=III}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIIII}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIII}{?={?=II}{?=III}}})})}}{MSRHcuEntryHeader_t=II}{?=I}{MSRHcuEntryHeader_t=II}{?={?=fffff}}{MSRHcuEntryHeader_t=II}{?={?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}}{MSRHcuEntryHeader_t=II}{?={?=IIIII}{?=IIIII}{?=IIIII}}}"
- "_aseFrameProcessing"
- "configControlHeader:"
- "processPixelWithInput:Output:"
- "processPixelWithInput:controlUnit:"
- "processPixelWithInput:controlUnitV3:"
- "processPixelWithInput_V1:Output:"
- "processPixelWithInput_V2:Output:"
- "processPixelWithInput_V3:Output:"
- "processPixelWithMeasurement_V1:pixelControl:"
- "processPixelWithMeasurement_V2:Output:"
- "processPixelWithMeasurement_V3:Output:"
- "processPixelWithPixelControl_V1:"
- "processPixelWithPixelControl_V2:"
- "processPixelWithPixelControl_V3:"
- "v24@0:8^{?=BI{?=III}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIIII}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIII}{?={?=II}{?=III}}}16"
- "v24@0:8^{hwConfigurationUnitsV3_t={MSRHcuHeader_t=II}{MSRHcuEntryHeader_t=II}{?=IIIIII}{MSRHcuEntryHeader_t=II}{?=[4[32f]]}{MSRHcuEntryHeader_t=II}{?=I{?=[32{?=fff}]}{?=[32{?=fff}]}{?=[32{?=fff}]}{?=IIIII}[2i][3i][4i][5i][6i][7i]}{MSRHcuEntryHeader_t=II}{?=[5{?=[32{?=fff}]}]{?=III}[13{?=II}][6{?=III}]}{MSRHcuEntryHeader_t=II}{?=[4{?=[32{?=fff}]}]{?=IIII}}{MSRHcuEntryHeader_t=II}{?=II}{MSRHcuEntryHeader_t=II}{?={?={?=II}{?=III}}}}16"
- "v24@0:8^{hwConfigurationUnits_t={MSRHcuHeader_t=II}{MSRHcuEntryHeader_t=II}{?={?=(?={?=iIB(?={?=BI{?=III}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIIII}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIII}{?={?=II}{?=III}}})})}}{MSRHcuEntryHeader_t=II}{?=I}{MSRHcuEntryHeader_t=II}{?={?=fffff}}{MSRHcuEntryHeader_t=II}{?={?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}}{MSRHcuEntryHeader_t=II}{?={?=IIIII}{?=IIIII}{?=IIIII}}}16"
- "v32@0:8r^{?=IIIIIIIIIIIIIII[8I][8I][8I][8I][16I][16I][16I][5I][5I][5I][5I]I}16^{hwConfigurationUnitsV3_t={MSRHcuHeader_t=II}{MSRHcuEntryHeader_t=II}{?=IIIIII}{MSRHcuEntryHeader_t=II}{?=[4[32f]]}{MSRHcuEntryHeader_t=II}{?=I{?=[32{?=fff}]}{?=[32{?=fff}]}{?=[32{?=fff}]}{?=IIIII}[2i][3i][4i][5i][6i][7i]}{MSRHcuEntryHeader_t=II}{?=[5{?=[32{?=fff}]}]{?=III}[13{?=II}][6{?=III}]}{MSRHcuEntryHeader_t=II}{?=[4{?=[32{?=fff}]}]{?=IIII}}{MSRHcuEntryHeader_t=II}{?=II}{MSRHcuEntryHeader_t=II}{?={?={?=II}{?=III}}}}24"
- "v32@0:8r^{?=IIIIIIIIIIIIIII[8I][8I][8I][8I][16I][16I][16I]}16^{?=(?={?=iIB(?={?=BI{?=III}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIIII}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIII}{?={?=II}{?=III}}})})}24"
- "v32@0:8r^{?=IIIIIIIIIIIIIII[8I][8I][8I][8I][16I][16I][16I]}16^{?=BI{?=III}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIIII}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIII}{?={?=II}{?=III}}}24"
- "v32@0:8r^{?=IIIIIIIIIIIIIII[8I][8I][8I][8I][16I][16I][16I]}16^{hwConfigurationUnits_t={MSRHcuHeader_t=II}{MSRHcuEntryHeader_t=II}{?={?=(?={?=iIB(?={?=BI{?=III}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIIII}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?=IIII}{?={?=II}{?=III}}})})}}{MSRHcuEntryHeader_t=II}{?=I}{MSRHcuEntryHeader_t=II}{?={?=fffff}}{MSRHcuEntryHeader_t=II}{?={?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}{?={?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}{?=fff}}}{MSRHcuEntryHeader_t=II}{?={?=IIIII}{?=IIIII}{?=IIIII}}}24"

```
