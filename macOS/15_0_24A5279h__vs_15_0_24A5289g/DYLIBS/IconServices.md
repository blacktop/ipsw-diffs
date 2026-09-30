## IconServices

> `/System/Library/PrivateFrameworks/IconServices.framework/Versions/A/IconServices`

```diff

-624.0.0.0.0
-  __TEXT.__text: 0x61400
+627.0.0.0.0
+  __TEXT.__text: 0x62450
   __TEXT.__auth_stubs: 0x1390
-  __TEXT.__objc_methlist: 0x5504
-  __TEXT.__const: 0x531a
+  __TEXT.__objc_methlist: 0x55dc
+  __TEXT.__const: 0x533a
   __TEXT.__gcc_except_tab: 0x684
-  __TEXT.__cstring: 0x44b1
-  __TEXT.__oslogstring: 0x2722
-  __TEXT.__unwind_info: 0x1650
-  __TEXT.__objc_classname: 0xf8c
-  __TEXT.__objc_methname: 0xa2ea
+  __TEXT.__cstring: 0x4500
+  __TEXT.__oslogstring: 0x273e
+  __TEXT.__unwind_info: 0x1660
+  __TEXT.__objc_classname: 0xfa3
+  __TEXT.__objc_methname: 0xa6a1
   __TEXT.__objc_methtype: 0x1851
-  __TEXT.__objc_stubs: 0x8b00
+  __TEXT.__objc_stubs: 0x8ce0
   __DATA_CONST.__got: 0x730
   __DATA_CONST.__const: 0x500
-  __DATA_CONST.__objc_classlist: 0x478
+  __DATA_CONST.__objc_classlist: 0x480
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2b00
+  __DATA_CONST.__objc_selrefs: 0x2b80
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x348
   __DATA_CONST.__objc_arraydata: 0x98
   __AUTH_CONST.__auth_got: 0x9e0
   __AUTH_CONST.__auth_ptr: 0x10
   __AUTH_CONST.__const: 0x16b0
-  __AUTH_CONST.__cfstring: 0x4a80
-  __AUTH_CONST.__objc_const: 0x113e8
+  __AUTH_CONST.__cfstring: 0x4aa0
+  __AUTH_CONST.__objc_const: 0x115f0
   __AUTH_CONST.__objc_intobj: 0x4f8
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH.__objc_data: 0x2cb0
+  __AUTH.__objc_data: 0x2d00
   __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0x55c
+  __DATA.__objc_ivar: 0x570
   __DATA.__data: 0x1d48
   __DATA.__bss: 0x7f8
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2136
-  Symbols:   6227
-  CStrings:  779
+  Functions: 2155
+  Symbols:   6274
+  CStrings:  782
 
Symbols:
+ +[ISRecipeInfo appRecipeForPlatformStyle:descriptor:]
+ +[ISRecipeInfo appRecipeForPlatformStyle:descriptor:].cold.1
+ -[ISDefaults isDarkIconColorEnhancementEnabled]
+ -[ISDefaults isDarkIconDimmingEnabled]
+ -[ISIconSegmentation enableColorEnhancementInDarkImage]
+ -[ISIconSegmentation enableRecoloringSingleForegroundColorWithGradientBackgroundInDarkImage]
+ -[ISIconSegmentation setEnableColorEnhancementInDarkImage:]
+ -[ISIconSegmentation setEnableRecoloringSingleForegroundColorWithGradientBackgroundInDarkImage:]
+ -[ISImageDescriptor platformStyle]
+ -[ISImageDescriptor setPlatformStyle:]
+ -[ISIntelligentDimEffect filterWithBackgroundImage:inputImage:]
+ -[ISResourceProvider _configureForDarkAndTintableWithDescriptor:]
+ -[ISResourceProvider allowAlterationsToResourceArt]
+ -[ISResourceProvider allowNonDefaultAppearances]
+ -[ISResourceProvider setAllowAlterationsToResourceArt:]
+ -[ISResourceProvider setAllowNonDefaultAppearances:]
+ -[ISStaticResources _addStaticImage:withKey:]
+ -[ISStaticResources _findStaticImageWithKey:]
+ OBJC_IVAR_$_ISIconSegmentation._enableColorEnhancementInDarkImage
+ OBJC_IVAR_$_ISIconSegmentation._enableRecoloringSingleForegroundColorWithGradientBackgroundInDarkImage
+ OBJC_IVAR_$_ISImageDescriptor._platformStyle
+ OBJC_IVAR_$_ISResourceProvider._allowAlterationsToResourceArt
+ OBJC_IVAR_$_ISResourceProvider._allowNonDefaultAppearances
+ _OBJC_CLASS_$_ISIntelligentDimEffect
+ _OBJC_METACLASS_$_ISIntelligentDimEffect
+ __OBJC_$_INSTANCE_METHODS_ISIntelligentDimEffect
+ __OBJC_$_PROP_LIST_ISIconSegmentation
+ __OBJC_$_PROP_LIST_ISIntelligentDimEffect
+ __OBJC_CLASS_PROTOCOLS_$_ISIntelligentDimEffect
+ __OBJC_CLASS_RO_$_ISIntelligentDimEffect
+ __OBJC_METACLASS_RO_$_ISIntelligentDimEffect
+ __block_literal_global.95
+ _lightenColorOverDarkBackground
+ _objc_msgSend$_configureForDarkAndTintableWithDescriptor:
+ _objc_msgSend$allowAlterationsToResourceArt
+ _objc_msgSend$allowNonDefaultAppearances
+ _objc_msgSend$appRecipeForPlatformStyle:descriptor:
+ _objc_msgSend$createDimmedImage
+ _objc_msgSend$hasDarkResource
+ _objc_msgSend$hasTintableResource
+ _objc_msgSend$isDarkIconColorEnhancementEnabled
+ _objc_msgSend$isDarkIconDimmingEnabled
+ _objc_msgSend$platformStyle
+ _objc_msgSend$setAllowAlterationsToResourceArt:
+ _objc_msgSend$setAllowNonDefaultAppearances:
+ _objc_msgSend$setEnableColorEnhancementInDarkImage:
+ _objc_msgSend$setEnableRecoloringSingleForegroundColorWithGradientBackgroundInDarkImage:
+ _objc_msgSend$setPlatformStyle:
+ _testColorContrastOverDarkBackground
- __block_literal_global.93
- _testColorOverDarkBackground
CStrings:
+ "%!f(MISSING):%!l(MISSING)d:%!@(MISSING):%!l(MISSING)u:%!@(MISSING):%!@(MISSING):%!@(MISSING):%!@(MISSING):%!@(MISSING)"
+ "%!@(MISSING) - (%!f(MISSING), %!f(MISSING))@%!f(MISSING)x v:%!l(MISSING)x l:%!l(MISSING)u a:%!@(MISSING) t:%!@(MISSING) b:%!@(MISSING) s:%!@(MISSING) ps:%!@(MISSING) digest: %!@(MISSING)"
+ "dark_icon_segmentation_color_enhancement"
+ "dim_dark_icons"
+ "platformStyle"
- "%!f(MISSING):%!l(MISSING)d:%!@(MISSING):%!l(MISSING)u:%!@(MISSING):%!@(MISSING):%!@(MISSING):%!@(MISSING)"
- "%!@(MISSING) - (%!f(MISSING), %!f(MISSING))@%!f(MISSING)x v:%!l(MISSING)x l:%!l(MISSING)u a:%!@(MISSING) t:%!@(MISSING) b:%!@(MISSING) s:%!@(MISSING) digest: %!@(MISSING)"

```
