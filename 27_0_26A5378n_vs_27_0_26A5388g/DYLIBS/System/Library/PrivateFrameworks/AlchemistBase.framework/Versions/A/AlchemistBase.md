## AlchemistBase

> `/System/Library/PrivateFrameworks/AlchemistBase.framework/Versions/A/AlchemistBase`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`

```diff

-32.0.2.0.0
-  __TEXT.__text: 0x2e348
+32.0.3.0.0
+  __TEXT.__text: 0x2ebf0
   __TEXT.__objc_methlist: 0xb0c
   __TEXT.__const: 0x2658
   __TEXT.__swift5_typeref: 0x898
-  __TEXT.__cstring: 0xc10
+  __TEXT.__cstring: 0xc30
   __TEXT.__constg_swiftt: 0xbe0
   __TEXT.__swift5_reflstr: 0x992
   __TEXT.__swift5_fieldmd: 0xb74
   __TEXT.__swift5_builtin: 0xf0
   __TEXT.__swift5_assocty: 0x168
-  __TEXT.__oslogstring: 0xc89
+  __TEXT.__oslogstring: 0xec1
   __TEXT.__swift5_proto: 0x19c
   __TEXT.__swift5_types: 0xec
   __TEXT.__swift5_capture: 0x50
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_mpenum: 0x18
   __TEXT.__unwind_info: 0x890
-  __TEXT.__eh_frame: 0x13f0
+  __TEXT.__eh_frame: 0x1400
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __AUTH_CONST.__const: 0x1a68
   __AUTH_CONST.__objc_const: 0x5668
   __AUTH_CONST.__auth_got: 0x830
-  __AUTH.__objc_data: 0x50
-  __AUTH.__data: 0x1b0
-  __DATA.__data: 0x860
-  __DATA.__bss: 0x3280
-  __DATA.__common: 0x48
-  __DATA_DIRTY.__objc_data: 0x50
-  __DATA_DIRTY.__data: 0xa28
-  __DATA_DIRTY.__common: 0x68
+  __DATA.__data: 0x700
+  __DATA.__bss: 0x2980
+  __DATA.__common: 0x28
+  __DATA_DIRTY.__objc_data: 0xa0
+  __DATA_DIRTY.__data: 0xd78
+  __DATA_DIRTY.__bss: 0x900
+  __DATA_DIRTY.__common: 0x88
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 801
   Symbols:   649
-  CStrings:  146
+  CStrings:  153
 
Functions:
~ sub_22747e7d8 -> sub_22876a740 : 1324 -> 2120
~ sub_22747ed04 -> sub_22876af88 : 516 -> 828
~ sub_22747ef08 -> sub_22876b2c4 : 1324 -> 2120
~ sub_22747f434 -> sub_22876bb0c : 516 -> 828
CStrings:
+ "%{public}@ already contains linearized colorspace."
+ "%{public}@ cannot be linearized, set to linearSRGB."
+ "ANE session started for asset at %{private}s with pages: %ld/%ld"
+ "ANE session stopped for asset at %{private}s"
+ "Active ROI aspect ratio is less than lowest enumerated aspect ratio (%{public}f, %{public}f)"
+ "CVPixelBuffer already has %{public}@ colorSpace, skipping convert."
+ "CVPixelBufferCreate failed with error code: %{public}d"
+ "Downsize the pano image with %{public}f aspect ratio, tiling mode: %{public}s."
+ "Error converting MLMultiArray from Float32 to Float16: %{public}ld"
+ "Failed to create image source image from %{private}s."
+ "FoV predictor model loaded"
+ "FoV predictor model unloading."
+ "Gaussian composition %{public}ld/%{public}ld..."
+ "Incorrect FoV predictor path specified: %{private}s"
+ "Incorrect Gaussian predictor path specified: %{private}s"
+ "Input CIImage to CVPixelBuffer conversion completed with info: %{public}@"
+ "Joint predictor model is too old (date: %{public}s). Panorama images require models from 2025_09_16 or later."
+ "Joint predictor model loaded."
+ "Joint predictor model unloading."
+ "Loading FoV predictor model. (%{public}s)"
+ "Loading joint predictor. (%{public}s)"
+ "Model to be loaded has been identified as %{public}s version.\n  "
+ "Saved depth map to %{private}s."
+ "Saved normalized depth map to %{private}s."
+ "The mono-depth buffer shape is invalid. Expect %{public}ld x %{public}ld, but got %{public}s"
+ "Tile prediction %{public}ld/%{public}ld..."
+ "Unable to fetch ANE session starting data for asset at %{private}s"
+ "[FOV] (min constrain) cur %{public}f, maxFPx %{public}f -> %{public}f"
+ "[FOV] ROI to crop horizontal to fit hFOV_degrees(%{public}f) width: %{public}ld -> %{public}f (%{public}f%%)"
+ "[FOV] panoFocalLengthPx %{public}f"
+ "[FOV] roiW, roiH, roiAR: %{public}ld, %{public}ld, %{public}f"
+ "replacing existing"
- "%@ already contains linearized colorspace."
- "%@ cannot be linearized, set to linearSRGB."
- "ANE session started for asset at %{public}s with pages: %ld/%ld"
- "ANE session stopped for asset at %{public}s"
- "Active ROI aspect ratio is less than lowest enumerated aspect ratio (%f, %f)"
- "CVPixelBuffer already has %@ colorSpace, skipping convert."
- "CVPixelBufferCreate failed with error code: %d"
- "Downsize the pano image with %f aspect ratio, tiling mode: %s."
- "Error converting MLMultiArray from Float32 to Float16: %ld"
- "Failed to create image source image from %s."
- "Gaussian composition %ld/%ld..."
- "Incorrect FoV predictor path specified: %s"
- "Incorrect Gaussian predictor path specified: %s"
- "Input CIImage to CVPixelBuffer conversion completed with info: %@"
- "Joint predictor model is too old (date: %s). Panorama images require models from 2025_09_16 or later."
- "Model to be loaded has been identified as %s version.\n  "
- "Saved depth map to %s."
- "Saved normalized depth map to %s."
- "The mono-depth buffer shape is invalid. Expect %ld x %ld, but got %s"
- "Tile prediction %ld/%ld..."
- "Unable to fetch ANE session starting data for asset at %{public}s"
- "[FOV] (min constrain) cur %f, maxFPx %f -> %f"
- "[FOV] ROI to crop horizontal to fit hFOV_degrees(%f) width: %ld -> %f (%f%%)"
- "[FOV] panoFocalLengthPx %f"
- "[FOV] roiW, roiH, roiAR: %ld, %ld, %f"
```
