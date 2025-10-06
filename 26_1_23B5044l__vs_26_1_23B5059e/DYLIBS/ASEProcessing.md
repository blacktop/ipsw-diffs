## ASEProcessing

> `/System/Library/PrivateFrameworks/ASEProcessing.framework/ASEProcessing`

```diff

-1.49.1.0.0
-  __TEXT.__text: 0x8e7c
+1.50.3.0.0
+  __TEXT.__text: 0x8578
   __TEXT.__auth_stubs: 0x2c0
   __TEXT.__objc_methlist: 0x2dc
   __TEXT.__const: 0x1be2c

   __TEXT.__objc_methtype: 0x23fe
   __TEXT.__objc_stubs: 0x4e0
   __DATA_CONST.__got: 0x48
-  __DATA_CONST.__const: 0x188
+  __DATA_CONST.__const: 0x228
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x180

   __AUTH_CONST.__cfstring: 0x160
   __AUTH_CONST.__objc_const: 0x630
   __DATA.__objc_ivar: 0x84
-  __DATA.__data: 0x1af80
-  __DATA.__bss: 0x8
-  __DATA.__common: 0x1c
+  __DATA.__data: 0x1c818
+  __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0xf0
+  __DATA_DIRTY.__bss: 0x8
+  __DATA_DIRTY.__common: 0x4
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0B8E1406-C94C-38A2-B72F-5403DA03E326
+  UUID: 962CD7D7-2813-3B16-AFB4-E0AC989B8694
   Functions: 116
-  Symbols:   810
+  Symbols:   824
   CStrings:  184
 
Symbols:
+ _defaultBlendEbeFactorCurve_heavy_HDR
+ _defaultBlendEbeFactorCurve_heavy_HDR_less
+ _defaultBlendLumaCurve_5
+ _defaultBlendLumaCurve_7
+ _defaultBlendLumaCurve_heavy_HDR
+ _defaultBlendLumaCurve_noEnh
+ _defaultBlendWPeakingCurve_5
+ _defaultBlendWPeakingCurve_L3
+ _defaultBlendWPeakingCurve_L3_h
+ _defaultBlendWPeakingCurve_heavy_HDR
+ _defaultWeightedBlendConfig_1
+ _defaultWeightedBlendConfig_2
+ _defaultWeightedBlendConfig_3
+ _defaultWeightedBlendConfig_4
+ _defaultWeightedBlendConfig_5
+ _defaultWeightedBlendConfig_6
+ _defaultWeightedBlendConfig_7
+ _defaultWeightedBlendConfig_8
+ _defaultWeightedBlendConfig_noEnh
- _defaultBlendLumaCurve_heavy
- _defaultWeightedBlendConfig_L1
- _defaultWeightedBlendConfig_L2
- _defaultWeightedBlendConfig_L3
- _defaultWeightedBlendConfig_heavy
Functions:
~ -[ASEProcessingT1 initWithConfig:aseProcessing:productType:] : 276 -> 304
~ _getMSRBaseAddr : 76 -> 96
~ _calculate_control_setting_V3 : 5076 -> 2660
~ _getCurrentProductType : 616 -> 668
~ _isT1OrNewer : 32 -> 40
CStrings:
+ " [1.50.3]     %s: src={ %dw x %dh }, dest={ %dw x %dh }, aseFunctionOnYesOffNo=%d\n"
+ " [1.50.3]     %s: src={ %dw x %dh }, dest={ %dw x %dh }, aseFunctionOnYesOffNo=%d, fps=%f\n"
+ " [1.50.3] %s : bad argument, retVal=%ld, input=%p, aseMeasurementOutput=%p, completionCallback=%p\n"
+ " [1.50.3] %s : config=%p"
+ " [1.50.3] %s : input=%p, aseMeasurementOutput=%p, aseFrameProcessingControl=%p"
+ " [1.50.3] %s : instance=%p, productType=%u, destinationWidth=%d, destinationHeight=%d, inputType=%s"
+ " [1.50.3] %s : unknownProcessingType=%d, strength=%f, wxh=%dx%d"
+ " [1.50.3] %s : unknownProcessingType=%d, strength=%f, wxh=%dx%d\n"
+ " [1.50.3] ++ %s: ASEApiVer=%d\n"
- " [1.49.1]     %s: src={ %dw x %dh }, dest={ %dw x %dh }, aseFunctionOnYesOffNo=%d\n"
- " [1.49.1]     %s: src={ %dw x %dh }, dest={ %dw x %dh }, aseFunctionOnYesOffNo=%d, fps=%f\n"
- " [1.49.1] %s : bad argument, retVal=%ld, input=%p, aseMeasurementOutput=%p, completionCallback=%p\n"
- " [1.49.1] %s : config=%p"
- " [1.49.1] %s : input=%p, aseMeasurementOutput=%p, aseFrameProcessingControl=%p"
- " [1.49.1] %s : instance=%p, productType=%u, destinationWidth=%d, destinationHeight=%d, inputType=%s"
- " [1.49.1] %s : unknownProcessingType=%d, strength=%f, wxh=%dx%d"
- " [1.49.1] %s : unknownProcessingType=%d, strength=%f, wxh=%dx%d\n"
- " [1.49.1] ++ %s: ASEApiVer=%d\n"

```
