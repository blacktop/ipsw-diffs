## ASEProcessing

> `/System/Library/PrivateFrameworks/ASEProcessing.framework/Versions/A/ASEProcessing`

```diff

 1.55.0.0.0
-  __TEXT.__text: 0x18f78
+  __TEXT.__text: 0x176d0
   __TEXT.__auth_stubs: 0x280
-  __TEXT.__objc_methlist: 0x3b0
+  __TEXT.__objc_methlist: 0x32c
   __TEXT.__const: 0x3028
-  __TEXT.__oslogstring: 0x48a8
-  __TEXT.__cstring: 0x1229
-  __TEXT.__unwind_info: 0x1e8
-  __TEXT.__objc_classname: 0x42
-  __TEXT.__objc_methname: 0x9d4
-  __TEXT.__objc_methtype: 0x2d92
-  __TEXT.__objc_stubs: 0x680
-  __DATA_CONST.__got: 0x58
+  __TEXT.__oslogstring: 0x417f
+  __TEXT.__cstring: 0x102a
+  __TEXT.__unwind_info: 0x1c0
+  __TEXT.__objc_classname: 0x32
+  __TEXT.__objc_methname: 0x8da
+  __TEXT.__objc_methtype: 0x24a9
+  __TEXT.__objc_stubs: 0x5e0
+  __DATA_CONST.__got: 0x50
   __DATA_CONST.__const: 0x1d8
-  __DATA_CONST.__objc_classlist: 0x20
+  __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1e0
-  __DATA_CONST.__objc_superrefs: 0x18
+  __DATA_CONST.__objc_selrefs: 0x1b8
+  __DATA_CONST.__objc_superrefs: 0x10
   __AUTH_CONST.__auth_got: 0x148
   __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0x3e0
-  __AUTH_CONST.__objc_const: 0x728
-  __DATA.__objc_ivar: 0x90
+  __AUTH_CONST.__cfstring: 0x3c0
+  __AUTH_CONST.__objc_const: 0x650
+  __DATA.__objc_ivar: 0x88
   __DATA.__data: 0x1cb50
   __DATA.__common: 0x20
-  __DATA_DIRTY.__objc_data: 0x140
+  __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__bss: 0x8
   __DATA_DIRTY.__common: 0x4
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 175
-  Symbols:   782
-  CStrings:  510
+  Functions: 156
+  Symbols:   756
+  CStrings:  479
 
Symbols:
- -[ASEProcessingT2 DumpOutputHcus:]
- -[ASEProcessingT2 configControlHeader_V4:]
- -[ASEProcessingT2 dealloc]
- -[ASEProcessingT2 initWithConfig:aseProcessing:productType:]
- -[ASEProcessingT2 populateOutputHcus:]
- -[ASEProcessingT2 processFrameWithInput:Measurement:outputData:]
- -[ASEProcessingT2 processPixelWithInput:Measurement:controlUnitV4:]
- -[ASEProcessingT2 processPixelWithInput_V4:Measurement:Output:]
- -[ASEProcessingT2 processPixelWithMeasurement_V4:Measurement:Output:]
- -[ASEProcessingT2 processPixelWithPixelControl_V4:Output:]
- OBJC_IVAR_$_ASEProcessingT2._aseControlUnitV4
- OBJC_IVAR_$_ASEProcessingT2._aseControlUnitV4Cache
- _OBJC_CLASS_$_ASEProcessingT2
- _OBJC_METACLASS_$_ASEProcessingT2
- __OBJC_$_INSTANCE_METHODS_ASEProcessingT2
- __OBJC_$_INSTANCE_VARIABLES_ASEProcessingT2
- __OBJC_CLASS_RO_$_ASEProcessingT2
- __OBJC_METACLASS_RO_$_ASEProcessingT2
- _calculate_control_setting_V4
- _calculate_graphics_control_setting_V4
- _isT2OrNewer
- _objc_msgSend$configControlHeader_V4:
- _objc_msgSend$processPixelWithInput:Measurement:controlUnitV4:
- _objc_msgSend$processPixelWithInput_V4:Measurement:Output:
- _objc_msgSend$processPixelWithMeasurement_V4:Measurement:Output:
- _objc_msgSend$processPixelWithPixelControl_V4:Output:
CStrings:
- " [1.55.0] Assertion: \"!(!!((_enabledHcus) & (1U << (ASEConfigurationUnitsV3_NoiseConfig))))\" warned in \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/ASEFramework/ASEProcessingT2.m\" at line 164\n"
- " [1.55.0] Assertion: \"(!!((_enabledHcus) & (1U << (ASEConfigurationUnitsV3_NoiseConfig))))\" warned in \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/ASEFramework/ASEProcessingT2.m\" at line 173\n"
- " [1.55.0] Assertion: \"0\" warned in \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/ASEFramework/ASEProcessingT2.m\" at line 178\n"
- " [1.55.0] Assertion: \"0\" warned in \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/ASEFramework/ASEProcessingT2.m\" at line 289\n"
- " [1.55.0] Assertion: \"_aseProcessingType < kASEProcessingTypeLivePhoto || _aseProcessingType > kASEProcessingTypeEnhanceOnly\" failed in \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/ASEFramework/ASEProcessingT2.m\" at line 330 goto EXIT\n"
- " [1.55.0] Assertion: \"isT2OrNewer(_productType)\" warned in \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/ASEFramework/ASEProcessingT2.m\" at line 349\n"
- " [1.55.0] Assertion: \"isT2OrNewer(_productType)\" warned in \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/ASEFramework/ASEProcessingT2.m\" at line 65\n"
- "-[ASEProcessingT2 dealloc]"
- "-[ASEProcessingT2 initWithConfig:aseProcessing:productType:]"
- "-[ASEProcessingT2 populateOutputHcus:]"
- "-[ASEProcessingT2 processFrameWithInput:Measurement:outputData:]"
- "-[ASEProcessingT2 processPixelWithInput:Measurement:controlUnitV4:]"
- "-[ASEProcessingT2 processPixelWithInput_V4:Measurement:Output:]"
- "-[ASEProcessingT2 processPixelWithMeasurement_V4:Measurement:Output:]"
- "-[ASEProcessingT2 processPixelWithPixelControl_V4:Output:]"
- "@24@0:8^{aseConfigurationUnitsV4_t={MSRHcuHeader_t=II}{MSRHcuEntryHeader_t=II}{?=IIIIII}{MSRHcuEntryHeader_t=II}{?=[4[32f]]}{MSRHcuEntryHeader_t=II}{?=I{?=[32{?=fff}]}{?=[32{?=fff}]}{?=[32{?=fff}]}{?=IIIII}[2i][3i][4i][5i][6i][7i]}{MSRHcuEntryHeader_t=II}{?=[5{?=[32{?=fff}]}]{?=III}[13{?=II}][6{?=III}]}{MSRHcuEntryHeader_t=II}{?=[4{?=[32{?=fff}]}]{?=IIII}}{MSRHcuEntryHeader_t=II}{?=II}{MSRHcuEntryHeader_t=II}{?={?={?=II}{?=III}}}}16"
- "ASEProcessingT2"
- "ASEProcessingT2.m"
- "HomeAccessory"
- "^{aseConfigurationUnitsV4_t={MSRHcuHeader_t=II}{MSRHcuEntryHeader_t=II}{?=IIIIII}{MSRHcuEntryHeader_t=II}{?=[4[32f]]}{MSRHcuEntryHeader_t=II}{?=I{?=[32{?=fff}]}{?=[32{?=fff}]}{?=[32{?=fff}]}{?=IIIII}[2i][3i][4i][5i][6i][7i]}{MSRHcuEntryHeader_t=II}{?=[5{?=[32{?=fff}]}]{?=III}[13{?=II}][6{?=III}]}{MSRHcuEntryHeader_t=II}{?=[4{?=[32{?=fff}]}]{?=IIII}}{MSRHcuEntryHeader_t=II}{?=II}{MSRHcuEntryHeader_t=II}{?={?={?=II}{?=III}}}}"
- "_aseControlUnitV4"
- "_aseControlUnitV4Cache"
- "configControlHeader_V4:"
- "isT2OrNewer(_productType)"
- "processPixelWithInput:Measurement:controlUnitV4:"
- "processPixelWithInput_V4:Measurement:Output:"
- "processPixelWithMeasurement_V4:Measurement:Output:"
- "processPixelWithPixelControl_V4:Output:"
- "v24@0:8^{aseConfigurationUnitsV4_t={MSRHcuHeader_t=II}{MSRHcuEntryHeader_t=II}{?=IIIIII}{MSRHcuEntryHeader_t=II}{?=[4[32f]]}{MSRHcuEntryHeader_t=II}{?=I{?=[32{?=fff}]}{?=[32{?=fff}]}{?=[32{?=fff}]}{?=IIIII}[2i][3i][4i][5i][6i][7i]}{MSRHcuEntryHeader_t=II}{?=[5{?=[32{?=fff}]}]{?=III}[13{?=II}][6{?=III}]}{MSRHcuEntryHeader_t=II}{?=[4{?=[32{?=fff}]}]{?=IIII}}{MSRHcuEntryHeader_t=II}{?=II}{MSRHcuEntryHeader_t=II}{?={?={?=II}{?=III}}}}16"
- "v32@0:8^{__IOSurface=}16^{aseConfigurationUnitsV4_t={MSRHcuHeader_t=II}{MSRHcuEntryHeader_t=II}{?=IIIIII}{MSRHcuEntryHeader_t=II}{?=[4[32f]]}{MSRHcuEntryHeader_t=II}{?=I{?=[32{?=fff}]}{?=[32{?=fff}]}{?=[32{?=fff}]}{?=IIIII}[2i][3i][4i][5i][6i][7i]}{MSRHcuEntryHeader_t=II}{?=[5{?=[32{?=fff}]}]{?=III}[13{?=II}][6{?=III}]}{MSRHcuEntryHeader_t=II}{?=[4{?=[32{?=fff}]}]{?=IIII}}{MSRHcuEntryHeader_t=II}{?=II}{MSRHcuEntryHeader_t=II}{?={?={?=II}{?=III}}}}24"
- "v40@0:8^{__IOSurface=}16r^{?=IIIIIIIIIIIIIII[8I][8I][8I][8I][16I][16I][16I][5I][5I][5I][5I]I}24^{aseConfigurationUnitsV4_t={MSRHcuHeader_t=II}{MSRHcuEntryHeader_t=II}{?=IIIIII}{MSRHcuEntryHeader_t=II}{?=[4[32f]]}{MSRHcuEntryHeader_t=II}{?=I{?=[32{?=fff}]}{?=[32{?=fff}]}{?=[32{?=fff}]}{?=IIIII}[2i][3i][4i][5i][6i][7i]}{MSRHcuEntryHeader_t=II}{?=[5{?=[32{?=fff}]}]{?=III}[13{?=II}][6{?=III}]}{MSRHcuEntryHeader_t=II}{?=[4{?=[32{?=fff}]}]{?=IIII}}{MSRHcuEntryHeader_t=II}{?=II}{MSRHcuEntryHeader_t=II}{?={?={?=II}{?=III}}}}32"
```
