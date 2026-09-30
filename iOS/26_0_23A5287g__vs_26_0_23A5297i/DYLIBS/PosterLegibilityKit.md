## PosterLegibilityKit

> `/System/Library/PrivateFrameworks/PosterLegibilityKit.framework/PosterLegibilityKit`

```diff

-283.101.0.0.0
-  __TEXT.__text: 0x16198
-  __TEXT.__auth_stubs: 0xc30
-  __TEXT.__objc_methlist: 0x181c
-  __TEXT.__const: 0x288
-  __TEXT.__cstring: 0xc49
-  __TEXT.__oslogstring: 0xa00
-  __TEXT.__gcc_except_tab: 0x5e4
-  __TEXT.__unwind_info: 0x770
-  __TEXT.__objc_classname: 0x4d2
-  __TEXT.__objc_methname: 0x4086
-  __TEXT.__objc_methtype: 0xb8b
-  __TEXT.__objc_stubs: 0x34a0
-  __DATA_CONST.__got: 0x358
+286.101.0.0.0
+  __TEXT.__text: 0x18f0c
+  __TEXT.__auth_stubs: 0xc60
+  __TEXT.__objc_methlist: 0x1a04
+  __TEXT.__const: 0x2f8
+  __TEXT.__cstring: 0xc8e
+  __TEXT.__oslogstring: 0xd92
+  __TEXT.__gcc_except_tab: 0x58c
+  __TEXT.__unwind_info: 0x7e8
+  __TEXT.__objc_classname: 0x4d3
+  __TEXT.__objc_methname: 0x4349
+  __TEXT.__objc_methtype: 0xc72
+  __TEXT.__objc_stubs: 0x3640
+  __DATA_CONST.__got: 0x348
   __DATA_CONST.__const: 0x850
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1010
+  __DATA_CONST.__objc_selrefs: 0x10b8
   __DATA_CONST.__objc_superrefs: 0xe0
-  __AUTH_CONST.__auth_got: 0x628
+  __AUTH_CONST.__auth_got: 0x640
   __AUTH_CONST.__const: 0x1e0
-  __AUTH_CONST.__cfstring: 0xb20
-  __AUTH_CONST.__objc_const: 0x46c8
+  __AUTH_CONST.__cfstring: 0xba0
+  __AUTH_CONST.__objc_const: 0x4910
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0x3c0
-  __DATA.__objc_ivar: 0x1cc
+  __DATA.__objc_ivar: 0x1e4
   __DATA.__data: 0x4e0
   __DATA.__bss: 0x128
   __DATA_DIRTY.__objc_data: 0x5f0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6A9DE7A6-010D-3307-9BB7-A28D32417BB3
-  Functions: 557
-  Symbols:   2482
-  CStrings:  1149
+  UUID: E5E3F9D3-2637-3FAA-9FB7-261E26AF4B71
+  Functions: 621
+  Symbols:   2634
+  CStrings:  1213
 
Symbols:
+ +[PLKColorBoxes _mergeColor:withColor:firstWeight:secondWeight:]
+ +[PLKColorBoxes _mergeColor:withColor:firstWeight:secondWeight:].cold.1
+ +[PLKColorBoxes _mergeColor:withColor:firstWeight:secondWeight:].cold.2
+ +[PLKColorBoxes colorBoxesForAverageColor:]
+ +[PLKColorBoxes colorBoxesForAverageColor:contrast:]
+ +[PLKColorBoxes colorBoxesForAverageColor:contrast:].cold.1
+ +[PLKColorBoxes colorBoxesForAverageColor:contrast:].cold.2
+ +[PLKColorBoxes colorBoxesForAverageColor:contrast:].cold.3
+ +[PLKColorBoxes colorBoxesForAverageColor:contrast:].cold.4
+ +[PLKColorBoxes colorBoxesForAverageColor:contrast:].cold.5
+ +[PLKColorBoxes colorBoxesForAverageColor:contrast:].cold.6
+ +[PLKColorBoxes colorBoxesForAverageColor:contrast:].cold.7
+ +[PLKColorBoxes colorBoxesForAverageColor:contrast:].cold.8
+ +[PLKColorBoxes colorBoxesForImage:]
+ +[PLKColorBoxes colorBoxesForImage:].cold.1
+ +[PLKColorBoxes colorBoxesForImage:].cold.2
+ +[PLKColorBoxes colorBoxesForImage:].cold.3
+ +[PLKColorBoxes colorBoxesForImage:].cold.4
+ +[PLKColorBoxes colorBoxesForImage:].cold.5
+ +[PLKColorBoxes supportsSecureCoding]
+ +[PLKLegibilityEnvironmentBuilder legibilityEnvironmentForAverageColor:contrast:saturation:]
+ +[PLKLegibilityEnvironmentBuilder legibilityEnvironmentForAverageColor:contrast:saturation:variants:]
+ +[PLKLegibilityEnvironmentBuilder legibilityEnvironmentForAverageColor:contrast:saturation:variants:].cold.1
+ +[PLKLegibilityEnvironmentBuilder legibilityEnvironmentForAverageColor:contrast:saturation:variants:].cold.2
+ -[PLKColorBoxes .cxx_destruct]
+ -[PLKColorBoxes _calculateMissingSaturationDataIfNeeded]
+ -[PLKColorBoxes averageColorInRect:]
+ -[PLKColorBoxes averageColor]
+ -[PLKColorBoxes colorBoxAtRow:col:]
+ -[PLKColorBoxes colorBoxesRowMajor]
+ -[PLKColorBoxes columnCount]
+ -[PLKColorBoxes contrastInRect:]
+ -[PLKColorBoxes contrast]
+ -[PLKColorBoxes copyWithZone:]
+ -[PLKColorBoxes copyWithZone:].cold.1
+ -[PLKColorBoxes dealloc]
+ -[PLKColorBoxes description]
+ -[PLKColorBoxes downsampledBoxSize]
+ -[PLKColorBoxes effectiveDownsampleFactor]
+ -[PLKColorBoxes encodeWithCoder:]
+ -[PLKColorBoxes hash]
+ -[PLKColorBoxes imageSize]
+ -[PLKColorBoxes initWithCoder:]
+ -[PLKColorBoxes initWithCoder:].cold.1
+ -[PLKColorBoxes initWithCoder:].cold.2
+ -[PLKColorBoxes initWithCoder:].cold.3
+ -[PLKColorBoxes initWithCoder:].cold.4
+ -[PLKColorBoxes initWithCoder:].cold.5
+ -[PLKColorBoxes initWithCoder:].cold.6
+ -[PLKColorBoxes initWithColorBoxes:size:rowCount:columnCount:totalContrast8:totalSaturation8:imageSize:downsampledBoxSize:effectiveDownsampleFactor:pixelHeight:pixelWidth:]
+ -[PLKColorBoxes isEqual:]
+ -[PLKColorBoxes isEqualToColorBoxes:]
+ -[PLKColorBoxes lumaInRect:]
+ -[PLKColorBoxes luma]
+ -[PLKColorBoxes pixelHeight]
+ -[PLKColorBoxes pixelWidth]
+ -[PLKColorBoxes rectForColorBoxAtRow:col:]
+ -[PLKColorBoxes rowCount]
+ -[PLKColorBoxes saturationInRect:]
+ -[PLKColorBoxes saturation]
+ -[PLKColorBoxes setTotalSaturation8:]
+ -[PLKColorBoxes size]
+ -[PLKColorBoxes totalContrast8]
+ -[PLKColorBoxes totalSaturation8]
+ -[PLKColorBoxes version]
+ -[PLKLegibilityEnvironment averageColorInRect:]
+ -[PLKLegibilityEnvironment contrastInRect:]
+ -[PLKLegibilityEnvironment legibilitySettings]
+ -[PLKLegibilityEnvironment lumaInRect:]
+ -[PLKLegibilityEnvironment luma]
+ -[PLKLegibilityEnvironment saturationInRect:]
+ -[PLKLegibilityEnvironment saturation]
+ -[PLKLegibilityEnvironmentBuilder legibilityContextForVariant:]
+ -[PLKLegibilityEnvironmentBuilder updateWithAverageColor:contrast:saturation:variants:]
+ -[PLKLegibilityEnvironmentBuilder updateWithContext:]
+ -[PLKLegibilityEnvironmentBuilder updateWithContext:variants:]
+ -[PLKLegibilityEnvironmentBuilder updateWithLegibilitySettings:contrast:saturation:variants:]
+ -[PLKLegibilityEnvironmentVariantContext _updateWithColorBoxes:]
+ -[PLKLegibilityEnvironmentVariantContext averageColorInRect:]
+ -[PLKLegibilityEnvironmentVariantContext contrastInRect:]
+ -[PLKLegibilityEnvironmentVariantContext initWithVariant:image:]
+ -[PLKLegibilityEnvironmentVariantContext initWithVariant:style:averageColor:contrast:saturation:legibilitySettings:]
+ -[PLKLegibilityEnvironmentVariantContext initWithVariant:style:averageColor:contrast:saturation:primaryColor:secondaryColor:backgroundColor:]
+ -[PLKLegibilityEnvironmentVariantContext initWithVariant:style:colorBoxes:legibilitySettings:]
+ -[PLKLegibilityEnvironmentVariantContext legibilitySettings]
+ -[PLKLegibilityEnvironmentVariantContext lumaInRect:]
+ -[PLKLegibilityEnvironmentVariantContext luma]
+ -[PLKLegibilityEnvironmentVariantContext saturationInRect:]
+ -[PLKLegibilityEnvironmentVariantContext saturation]
+ _OBJC_CLASS_$_PLKColorBoxes
+ _OBJC_IVAR_$_PLKColorBoxes._averageColor
+ _OBJC_IVAR_$_PLKColorBoxes._colorBoxesRowMajor
+ _OBJC_IVAR_$_PLKColorBoxes._columnCount
+ _OBJC_IVAR_$_PLKColorBoxes._downsampledBoxSize
+ _OBJC_IVAR_$_PLKColorBoxes._effectiveDownsampleFactor
+ _OBJC_IVAR_$_PLKColorBoxes._imageSize
+ _OBJC_IVAR_$_PLKColorBoxes._pixelHeight
+ _OBJC_IVAR_$_PLKColorBoxes._pixelWidth
+ _OBJC_IVAR_$_PLKColorBoxes._rowCount
+ _OBJC_IVAR_$_PLKColorBoxes._saturationCalculated
+ _OBJC_IVAR_$_PLKColorBoxes._size
+ _OBJC_IVAR_$_PLKColorBoxes._totalContrast8
+ _OBJC_IVAR_$_PLKColorBoxes._totalSaturation8
+ _OBJC_IVAR_$_PLKColorBoxes._version
+ _OBJC_IVAR_$_PLKLegibilityEnvironmentVariantContext._colorBoxes
+ _OBJC_IVAR_$_PLKLegibilityEnvironmentVariantContext._luma
+ _OBJC_IVAR_$_PLKLegibilityEnvironmentVariantContext._saturation
+ _OBJC_METACLASS_$_PLKColorBoxes
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _PLKAverageColorFromColorBoxes
+ _PLKAverageSaturationFromColorBoxes
+ _PLKAverageSaturationFromColorBoxes.cold.1
+ _PLKAverageSaturationFromColorBoxes.cold.2
+ _PLKAverageSaturationFromColorBoxes.cold.3
+ _PLKAverageSaturationFromColorBoxes.cold.4
+ _PLKCalculateContrastFromColorBoxes
+ _PLKCalculateSaturationFromColorBoxes
+ __OBJC_$_CLASS_METHODS_PLKColorBoxes
+ __OBJC_$_CLASS_PROP_LIST_PLKColorBoxes
+ __OBJC_$_INSTANCE_METHODS_PLKColorBoxes
+ __OBJC_$_INSTANCE_VARIABLES_PLKColorBoxes
+ __OBJC_$_PROP_LIST_PLKColorBoxes
+ __OBJC_CLASS_PROTOCOLS_$_PLKColorBoxes
+ __OBJC_CLASS_RO_$_PLKColorBoxes
+ __OBJC_METACLASS_RO_$_PLKColorBoxes
+ _malloc_type_malloc
+ _memcpy
+ _objc_msgSend$_isSimilarToColor:withinPercentage:
+ _objc_msgSend$_luminance
+ _objc_msgSend$_updateWithColorBoxes:
+ _objc_msgSend$averageColorInRect:
+ _objc_msgSend$colorBoxesForAverageColor:contrast:
+ _objc_msgSend$containsValueForKey:
+ _objc_msgSend$contrastInRect:
+ _objc_msgSend$decodeBytesForKey:returnedLength:
+ _objc_msgSend$decodeIntForKey:
+ _objc_msgSend$encodeBytes:length:forKey:
+ _objc_msgSend$encodeInt:forKey:
+ _objc_msgSend$getRed:green:blue:alpha:
+ _objc_msgSend$initWithVariant:colorBoxes:
+ _objc_msgSend$initWithVariant:style:averageColor:contrast:saturation:primaryColor:secondaryColor:backgroundColor:
+ _objc_msgSend$isEqualToColorBoxes:
+ _objc_msgSend$legibilityEnvironmentForAverageColor:contrast:saturation:variants:
+ _objc_msgSend$luma
+ _objc_msgSend$lumaInRect:
+ _objc_msgSend$saturation
+ _objc_msgSend$saturationInRect:
+ _objc_msgSend$systemGrayColor
+ _objc_msgSend$updateWithAverageColor:contrast:saturation:variants:
+ _objc_msgSend$updateWithContext:variants:
+ _powf
+ _saturation
+ _saturation.cold.1
- +[PLKLegibilityEnvironment supportsSecureCoding]
- +[PLKLegibilityEnvironmentBuilder legibilityEnvironmentForImage:variants:].cold.2
- +[PLKLegibilityEnvironmentVariantContext supportsSecureCoding]
- +[_PLKColorBoxes colorBoxesForImage:]
- +[_PLKColorBoxes colorBoxesForImage:].cold.1
- +[_PLKColorBoxes colorBoxesForImage:].cold.2
- +[_PLKColorBoxes colorBoxesForImage:].cold.3
- +[_PLKColorBoxes colorBoxesForImage:].cold.4
- +[_PLKColorBoxes colorBoxesForImage:].cold.5
- +[_PLKColorBoxes supportsSecureCoding]
- -[PLKLegibilityEnvironment encodeWithCoder:]
- -[PLKLegibilityEnvironment initWithCoder:]
- -[PLKLegibilityEnvironmentBuilder updateWithImage:variants:]
- -[PLKLegibilityEnvironmentVariantContext encodeWithCoder:]
- -[PLKLegibilityEnvironmentVariantContext initWithCoder:]
- -[PLKLegibilityEnvironmentVariantContext initWithStyle:averageColor:contrast:primaryColor:secondaryColor:backgroundColor:]
- -[PLKLegibilityEnvironmentVariantContext initWithVariant:style:averageColor:contrast:primaryColor:secondaryColor:backgroundColor:]
- -[_PLKColorBoxes colorBoxAtRow:col:]
- -[_PLKColorBoxes colorBoxesRowMajor]
- -[_PLKColorBoxes columnCount]
- -[_PLKColorBoxes contrast]
- -[_PLKColorBoxes dealloc]
- -[_PLKColorBoxes description]
- -[_PLKColorBoxes downsampledBoxSize]
- -[_PLKColorBoxes effectiveDownsampleFactor]
- -[_PLKColorBoxes imageSize]
- -[_PLKColorBoxes initWithColorBoxes:size:rowCount:columnCount:totalContrast8:imageSize:downsampledBoxSize:effectiveDownsampleFactor:pixelHeight:pixelWidth:]
- -[_PLKColorBoxes pixelHeight]
- -[_PLKColorBoxes pixelWidth]
- -[_PLKColorBoxes rectForColorBoxAtRow:col:]
- -[_PLKColorBoxes rowCount]
- -[_PLKColorBoxes size]
- -[_PLKColorBoxes totalContrast8]
- GCC_except_table30
- _OBJC_CLASS_$_NSPropertyListSerialization
- _OBJC_CLASS_$__PLKColorBoxes
- _OBJC_IVAR_$_PLKLegibilityEnvironmentBuilder._legibilityProvider
- _OBJC_IVAR_$__PLKColorBoxes._colorBoxesRowMajor
- _OBJC_IVAR_$__PLKColorBoxes._columnCount
- _OBJC_IVAR_$__PLKColorBoxes._downsampledBoxSize
- _OBJC_IVAR_$__PLKColorBoxes._effectiveDownsampleFactor
- _OBJC_IVAR_$__PLKColorBoxes._imageSize
- _OBJC_IVAR_$__PLKColorBoxes._pixelHeight
- _OBJC_IVAR_$__PLKColorBoxes._pixelWidth
- _OBJC_IVAR_$__PLKColorBoxes._rowCount
- _OBJC_IVAR_$__PLKColorBoxes._size
- _OBJC_IVAR_$__PLKColorBoxes._totalContrast8
- _OBJC_METACLASS_$__PLKColorBoxes
- __OBJC_$_CLASS_METHODS__PLKColorBoxes
- __OBJC_$_CLASS_PROP_LIST_PLKLegibilityEnvironment
- __OBJC_$_CLASS_PROP_LIST_PLKLegibilityEnvironmentVariantContext
- __OBJC_$_INSTANCE_METHODS__PLKColorBoxes
- __OBJC_$_INSTANCE_VARIABLES__PLKColorBoxes
- __OBJC_$_PROP_LIST__PLKColorBoxes
- __OBJC_CLASS_RO_$__PLKColorBoxes
- __OBJC_METACLASS_RO_$__PLKColorBoxes
- __PLKAverageColorFromColorBoxes
- __PLKCalculateContrastFromColorBoxes
- _objc_msgSend$dataWithPropertyList:format:options:error:
- _objc_msgSend$decodeDoubleForKey:
- _objc_msgSend$decodeObjectOfClass:forKey:
- _objc_msgSend$decodeObjectOfClasses:forKey:
- _objc_msgSend$encodeDouble:forKey:
- _objc_msgSend$encodeObject:forKey:
- _objc_msgSend$initWithStyle:averageColor:contrast:primaryColor:secondaryColor:backgroundColor:
- _objc_msgSend$initWithVariant:style:averageColor:contrast:primaryColor:secondaryColor:backgroundColor:
- _objc_msgSend$propertyListWithData:options:format:error:
- _objc_msgSend$updateWithImage:variants:
CStrings:
+ "1"
+ "@\"PLKColorBoxes\""
+ "@\"UIColor\"48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
+ "@\"_UILegibilitySettings\"16@0:8"
+ "@40@0:8@16d24d32"
+ "@48@0:8@16Q24@32@40"
+ "@48@0:8@16d24d32@40"
+ "@48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
+ "@64@0:8@16Q24@32d40d48@56"
+ "@80@0:8@16Q24@32d40d48@56@64@72"
+ "B40@0:8@16d24@32"
+ "B48@0:8@16d24d32@40"
+ "Calculated approximate saturation data for legacy color boxes"
+ "Cannot create color boxes for nil color"
+ "Color boxes data length mismatch for v1: expected %lu, got %lu"
+ "Color boxes data length mismatch for v2: expected %lu, got %lu"
+ "Created color boxes for solid color (R:%d G:%d B:%d C:%d S:%d)"
+ "Decoding legacy PLKColorBoxes without version info, assuming version 1"
+ "Failed to allocate color box buffer for solid color"
+ "Failed to allocate memory for color boxes"
+ "Failed to allocate memory for color boxes conversion"
+ "Failed to allocate memory for color boxes copy"
+ "Failed to decode color boxes data"
+ "Failed to extract RGB components from color"
+ "Failed to extract RGB components from first color"
+ "Failed to extract RGB components from second color"
+ "Legacy PLKColorBoxes detected, saturation data will be calculated on demand"
+ "PLKColorBoxes"
+ "PLKColorBoxes.m"
+ "Saturation"
+ "Successfully converted %lu legacy color boxes to current format"
+ "T@\"_UILegibilitySettings\",R,N"
+ "Td,R,N,V_luma"
+ "Td,R,N,V_saturation"
+ "Unsupported PLKColorBoxes version: %ld"
+ "Version"
+ "^{?=CCCCC}"
+ "_colorBoxes"
+ "_isSimilarToColor:withinPercentage:"
+ "_luma"
+ "_luminance"
+ "_saturation"
+ "_saturationCalculated"
+ "_totalSaturation8"
+ "_updateWithColorBoxes:"
+ "_version"
+ "averageColorInRect:"
+ "colorBoxesForAverageColor:"
+ "colorBoxesForAverageColor:contrast:"
+ "colorBoxesRowMajor"
+ "columnCount"
+ "containsValueForKey:"
+ "contrastInRect:"
+ "d48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
+ "decodeBytesForKey:returnedLength:"
+ "decodeIntForKey:"
+ "downsampledBoxSize"
+ "effectiveDownsampleFactor"
+ "encodeBytes:length:forKey:"
+ "encodeInt:forKey:"
+ "getRed:green:blue:alpha:"
+ "imageSize"
+ "initWithVariant:colorBoxes:"
+ "initWithVariant:image:"
+ "initWithVariant:style:averageColor:contrast:saturation:legibilitySettings:"
+ "initWithVariant:style:averageColor:contrast:saturation:primaryColor:secondaryColor:backgroundColor:"
+ "initWithVariant:style:colorBoxes:legibilitySettings:"
+ "isEqualToColorBoxes:"
+ "legibilityContextForVariant:"
+ "legibilityEnvironmentForAverageColor:contrast:saturation:"
+ "legibilityEnvironmentForAverageColor:contrast:saturation:variants:"
+ "luma"
+ "lumaInRect:"
+ "pixelHeight"
+ "pixelWidth"
+ "rowCount"
+ "saturation"
+ "saturationInRect:"
+ "systemGrayColor"
+ "totalContrast8"
+ "totalSaturation8"
+ "updateWithAverageColor:contrast:saturation:variants:"
+ "updateWithContext:"
+ "updateWithContext:variants:"
+ "updateWithLegibilitySettings:contrast:saturation:variants:"
+ "version"
- "@\"_UILegibilitySettingsProvider\""
- "@64@0:8Q16@24d32@40@48@56"
- "@72@0:8@16Q24@32d40@48@56@64"
- "^{?=CCCC}"
- "_PLKColorBoxes"
- "_legibilityProvider"
- "dataWithPropertyList:format:options:error:"
- "decodeDoubleForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "encodeDouble:forKey:"
- "encodeObject:forKey:"
- "initWithStyle:averageColor:contrast:primaryColor:secondaryColor:backgroundColor:"
- "initWithVariant:style:averageColor:contrast:primaryColor:secondaryColor:backgroundColor:"
- "propertyListWithData:options:format:error:"
- "updateWithImage:variants:"
- "v40@0:8@16d24@32"

```
