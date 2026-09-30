## IconServices

> `/System/Library/PrivateFrameworks/IconServices.framework/IconServices`

```diff

-742.104.0.0.0
-  __TEXT.__text: 0x63964
-  __TEXT.__auth_stubs: 0xf70
+742.106.100.0.0
+  __TEXT.__text: 0x66968
+  __TEXT.__auth_stubs: 0xf50
   __TEXT.__delay_helper: 0xdc
-  __TEXT.__objc_methlist: 0x66bc
-  __TEXT.__const: 0x87b2
-  __TEXT.__gcc_except_tab: 0x43c
-  __TEXT.__cstring: 0x3eff
-  __TEXT.__oslogstring: 0x327c
-  __TEXT.__unwind_info: 0x1858
+  __TEXT.__objc_methlist: 0x670c
+  __TEXT.__const: 0x87d0
+  __TEXT.__gcc_except_tab: 0x458
+  __TEXT.__cstring: 0x3f9a
+  __TEXT.__oslogstring: 0x32dd
+  __TEXT.__unwind_info: 0x17e8
   __TEXT.__eh_frame: 0x88
-  __TEXT.__objc_classname: 0x1250
-  __TEXT.__objc_methname: 0xc087
+  __TEXT.__objc_classname: 0x1260
+  __TEXT.__objc_methname: 0xc146
   __TEXT.__objc_methtype: 0x18d9
-  __TEXT.__objc_stubs: 0x96c0
-  __DATA_CONST.__got: 0x628
-  __DATA_CONST.__const: 0x9f0
+  __TEXT.__objc_stubs: 0x97a0
+  __DATA_CONST.__got: 0x638
+  __DATA_CONST.__const: 0xa30
   __DATA_CONST.__objc_classlist: 0x528
-  __DATA_CONST.__objc_catlist: 0xf0
+  __DATA_CONST.__objc_catlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3008
+  __DATA_CONST.__objc_selrefs: 0x3050
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x400
   __DATA_CONST.__objc_arraydata: 0xb0
-  __AUTH_CONST.__auth_got: 0x7d0
+  __AUTH_CONST.__auth_got: 0x7c0
   __AUTH_CONST.__const: 0x1188
-  __AUTH_CONST.__cfstring: 0x4300
-  __AUTH_CONST.__objc_const: 0x13c78
+  __AUTH_CONST.__cfstring: 0x4360
+  __AUTH_CONST.__objc_const: 0x13cb8
   __AUTH_CONST.__objc_intobj: 0x528
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH.__objc_data: 0x910
+  __AUTH.__objc_data: 0x7d0
   __DATA.__objc_ivar: 0x6a0
   __DATA.__data: 0x1ce8
-  __DATA.__bss: 0x648
-  __DATA_DIRTY.__objc_data: 0x2a80
+  __DATA.__bss: 0x650
+  __DATA_DIRTY.__objc_data: 0x2bc0
   __DATA_DIRTY.__data: 0xc
   __DATA_DIRTY.__bss: 0x1f8
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /System/Library/PrivateFrameworks/IconFoundation.framework/IconFoundation
   - /System/Library/PrivateFrameworks/IconRendering.framework/IconRendering
   - /System/Library/PrivateFrameworks/MobileIcons.framework/MobileIcons
+  - /System/Library/PrivateFrameworks/PosterBoardServices.framework/PosterBoardServices
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 478E781F-F4FD-373C-A85B-19969286E03D
-  Functions: 2517
-  Symbols:   9466
-  CStrings:  4197
+  UUID: 8BA10C1B-1D6C-333D-A1C7-83A812283067
+  Functions: 2534
+  Symbols:   9556
+  CStrings:  4216
 
Symbols:
+ -[CIColor(IconServicesAdditions) compontentsOnlyHash]
+ -[IFColor(IconServicesAdditions) isCacheCompatibleColorSpace]
+ -[ISPlaceholderIcon imageForDescriptor:]
+ -[ISRecordResourceProvider(RecipeAdditions) _IS_shouldTreatLikeApp]
+ -[ISResourceProvider(RecipeAdditions) _IS_shouldTreatLikeApp]
+ _CFStringCompare
+ _CGColorGetColorSpace
+ _CGColorSpaceGetName
+ _OBJC_CLASS_$_PRSService
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ __OBJC_$_CATEGORY_CIColor_$_IconServicesAdditions
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_CIColor_$_IconServicesAdditions
+ __OBJC_$_CLASS_METHODS_ISResourceProvider(Convenience|RecipeAdditions)
+ __OBJC_$_INSTANCE_METHODS_IFColor(FolderAdditions|IconServicesAdditions)
+ __OBJC_$_INSTANCE_METHODS_ISRecordResourceProvider(RecipeAdditions)
+ __OBJC_$_INSTANCE_METHODS_ISResourceProvider(Convenience|RecipeAdditions)
+ ___50+[IFColor(IconServicesAdditions) systemTintColors]_block_invoke
+ ___block_descriptor_40_e8_32r_e29_v24?0"NSArray"8"NSError"16lr32l8
+ _kCGColorSpaceExtendedSRGB
+ _objc_msgSend$CGColor
+ _objc_msgSend$_IS_shouldTreatLikeApp
+ _objc_msgSend$accentColor
+ _objc_msgSend$components
+ _objc_msgSend$fetchLockScreenHomeScreenColorConfigurations:
+ _objc_msgSend$numberOfComponents
+ _objc_msgSend$numberWithUnsignedLong:
- __OBJC_$_CLASS_METHODS_ISResourceProvider(Convenience)
- __OBJC_$_INSTANCE_METHODS_ISRecordResourceProvider
- __OBJC_$_INSTANCE_METHODS_ISResourceProvider(Convenience)
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x6
- _objc_retain_x9
CStrings:
+ "%@_%@,%.1f,%.1f,%.f,%@"
+ "%g,%g,%g,%g"
+ "23:57:25"
+ "CGColor"
+ "CacheMissIcon_iOS_Debug_SPIExplicitlyRequested_NoPrepareCalled"
+ "Failed to determine color space for %@"
+ "Failed to determine color space name for space %@ from %@"
+ "RecipeAdditions"
+ "_IS_shouldTreatLikeApp"
+ "accentColor"
+ "com.apple.iconservices.placeholdericon"
+ "components"
+ "compontentsOnlyHash"
+ "fetchLockScreenHomeScreenColorConfigurations:"
+ "isCacheCompatibleColorSpace"
+ "kCGColorSpaceDeviceRGB"
+ "numberOfComponents"
+ "numberWithUnsignedLong:"
+ "v24@?0@\"NSArray\"8@\"NSError\"16"
- "%@_%@,%.1f,%.1f,%.f,%d"
- "%f,%f,%f,%f"
- "00:39:55"

```
