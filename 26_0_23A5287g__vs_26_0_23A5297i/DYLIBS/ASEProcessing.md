## ASEProcessing

> `/System/Library/PrivateFrameworks/ASEProcessing.framework/ASEProcessing`

```diff

-1.45.0.0.0
-  __TEXT.__text: 0x6e70
+1.46.3.0.0
+  __TEXT.__text: 0x7544
   __TEXT.__auth_stubs: 0x280
-  __TEXT.__objc_methlist: 0x288
+  __TEXT.__objc_methlist: 0x294
   __TEXT.__const: 0x1be2c
   __TEXT.__oslogstring: 0x25c
   __TEXT.__cstring: 0x340
-  __TEXT.__unwind_info: 0x140
+  __TEXT.__unwind_info: 0x148
   __TEXT.__objc_classname: 0x32
   __TEXT.__objc_methname: 0x6d4
-  __TEXT.__objc_methtype: 0x1a83
+  __TEXT.__objc_methtype: 0x1ae3
   __TEXT.__objc_stubs: 0x4a0
   __DATA_CONST.__got: 0x48
-  __DATA_CONST.__const: 0xe8
+  __DATA_CONST.__const: 0x168
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x158

   __AUTH_CONST.__cfstring: 0x160
   __AUTH_CONST.__objc_const: 0x600
   __DATA.__objc_ivar: 0x80
-  __DATA.__data: 0x1a8a0
-  __DATA.__common: 0x18
+  __DATA.__data: 0x1ad00
+  __DATA.__common: 0x14
   __DATA_DIRTY.__objc_data: 0xf0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 55C46763-FC8A-3043-94D6-6C99C58AEF3F
-  Functions: 100
-  Symbols:   748
-  CStrings:  166
+  UUID: 9578484A-3C20-3E9E-8644-01D11FBF99DC
+  Functions: 101
+  Symbols:   757
+  CStrings:  167
 
Symbols:
+ -[ASEProcessingT1 printAseMeasurementOutput:]
+ _defaultBlendLumaCurve_L1
+ _defaultBlendLumaCurve_L2
+ _defaultBlendLumaCurve_L3
+ _defaultBlendLumaCurve_heavy
+ _defaultWeightedBlendConfig_L1
+ _defaultWeightedBlendConfig_L2
+ _defaultWeightedBlendConfig_L3
+ _defaultWeightedBlendConfig_heavy
- _enableT1Sim
Functions:
~ -[ASEProcessingT1 processFrameWithInput:outputData:] : 588 -> 596
+ -[ASEProcessingT1 printAseMeasurementOutput:]
~ _calculate_control_setting_V3 : 3356 -> 4812
~ _getCurrentProductType : 680 -> 616
~ _calculate_control_setting_V2 : 6132 -> 6256
~ _calculate_control_setting_V1 : 2688 -> 2856
CStrings:
+ " [1.46.3]     %s: src={ %dw x %dh }, dest={ %dw x %dh }, aseFunctionOnYesOffNo=%d\n"
+ " [1.46.3]     %s: src={ %dw x %dh }, dest={ %dw x %dh }, aseFunctionOnYesOffNo=%d, fps=%f\n"
+ " [1.46.3] %s : aseMeasurementOutput=%p, aseFrameProcessingControl=%p"
+ " [1.46.3] %s : bad argument, retVal=%ld, aseMeasurementOutput=%p, completionCallback=%p\n"
+ " [1.46.3] %s : config=%p"
+ " [1.46.3] %s : instance=%p, productType=%u, destinationWidth=%d,  destinationHeight=%d"
+ " [1.46.3] %s : unknownProcessingType=%d, strength=%f, wxh=%dx%d"
+ " [1.46.3] %s : unknownProcessingType=%d, strength=%f, wxh=%dx%d\n"
+ " [1.46.3] ++ %s: ASEApiVer=%d\n"
+ "v24@0:8r^{?=IIIIIIIIIIIIIII[8I][8I][8I][8I][16I][16I][16I][5I][5I][5I][5I]I}16"
+ "v32@0:8r^{?=IIIIIIIIIIIIIII[8I][8I][8I][8I][16I][16I][16I][5I][5I][5I][5I]I}16^{hwConfigurationUnitsV3_t={MSRHcuHeader_t=II}{MSRHcuEntryHeader_t=II}{?=IIIIII}{MSRHcuEntryHeader_t=II}{?=[4[32f]]}{MSRHcuEntryHeader_t=II}{?=I{?=[32{?=fff}]}{?=[32{?=fff}]}{?=[32{?=fff}]}{?=IIIII}[2i][3i][4i][5i][6i][7i]}{MSRHcuEntryHeader_t=II}{?=[5{?=[32{?=fff}]}]{?=III}[13{?=II}][6{?=III}]}{MSRHcuEntryHeader_t=II}{?=[4{?=[32{?=fff}]}]{?=IIII}}{MSRHcuEntryHeader_t=II}{?=II}{MSRHcuEntryHeader_t=II}{?={?={?=II}{?=III}}}}24"
- " [1.45.0]     %s: src={ %dw x %dh }, dest={ %dw x %dh }, aseFunctionOnYesOffNo=%d\n"
- " [1.45.0]     %s: src={ %dw x %dh }, dest={ %dw x %dh }, aseFunctionOnYesOffNo=%d, fps=%f\n"
- " [1.45.0] %s : aseMeasurementOutput=%p, aseFrameProcessingControl=%p"
- " [1.45.0] %s : bad argument, retVal=%ld, aseMeasurementOutput=%p, completionCallback=%p\n"
- " [1.45.0] %s : config=%p"
- " [1.45.0] %s : instance=%p, productType=%u, destinationWidth=%d,  destinationHeight=%d"
- " [1.45.0] %s : unknownProcessingType=%d, strength=%f, wxh=%dx%d"
- " [1.45.0] %s : unknownProcessingType=%d, strength=%f, wxh=%dx%d\n"
- " [1.45.0] ++ %s: ASEApiVer=%d\n"
- "v32@0:8r^{?=IIIIIIIIIIIIIII[8I][8I][8I][8I][16I][16I][16I]}16^{hwConfigurationUnitsV3_t={MSRHcuHeader_t=II}{MSRHcuEntryHeader_t=II}{?=IIIIII}{MSRHcuEntryHeader_t=II}{?=[4[32f]]}{MSRHcuEntryHeader_t=II}{?=I{?=[32{?=fff}]}{?=[32{?=fff}]}{?=[32{?=fff}]}{?=IIIII}[2i][3i][4i][5i][6i][7i]}{MSRHcuEntryHeader_t=II}{?=[5{?=[32{?=fff}]}]{?=III}[13{?=II}][6{?=III}]}{MSRHcuEntryHeader_t=II}{?=[4{?=[32{?=fff}]}]{?=IIII}}{MSRHcuEntryHeader_t=II}{?=II}{MSRHcuEntryHeader_t=II}{?={?={?=II}{?=III}}}}24"

```
