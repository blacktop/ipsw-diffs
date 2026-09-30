## IconServices

> `/System/Library/PrivateFrameworks/IconServices.framework/IconServices`

```diff

-742.101.0.0.0
-  __TEXT.__text: 0x638b8
+742.104.0.0.0
+  __TEXT.__text: 0x63964
   __TEXT.__auth_stubs: 0xf70
   __TEXT.__delay_helper: 0xdc
-  __TEXT.__objc_methlist: 0x66a4
+  __TEXT.__objc_methlist: 0x66bc
   __TEXT.__const: 0x87b2
   __TEXT.__gcc_except_tab: 0x43c
-  __TEXT.__cstring: 0x3e70
+  __TEXT.__cstring: 0x3eff
   __TEXT.__oslogstring: 0x327c
-  __TEXT.__unwind_info: 0x1850
+  __TEXT.__unwind_info: 0x1858
   __TEXT.__eh_frame: 0x88
   __TEXT.__objc_classname: 0x1250
-  __TEXT.__objc_methname: 0xbffc
-  __TEXT.__objc_methtype: 0x18ae
-  __TEXT.__objc_stubs: 0x9680
+  __TEXT.__objc_methname: 0xc087
+  __TEXT.__objc_methtype: 0x18d9
+  __TEXT.__objc_stubs: 0x96c0
   __DATA_CONST.__got: 0x628
   __DATA_CONST.__const: 0x9f0
   __DATA_CONST.__objc_classlist: 0x528
   __DATA_CONST.__objc_catlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2ff8
+  __DATA_CONST.__objc_selrefs: 0x3008
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x400
   __DATA_CONST.__objc_arraydata: 0xb0
   __AUTH_CONST.__auth_got: 0x7d0
   __AUTH_CONST.__const: 0x1188
-  __AUTH_CONST.__cfstring: 0x42a0
-  __AUTH_CONST.__objc_const: 0x13c68
+  __AUTH_CONST.__cfstring: 0x4300
+  __AUTH_CONST.__objc_const: 0x13c78
   __AUTH_CONST.__objc_intobj: 0x528
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH.__objc_data: 0x910
   __DATA.__objc_ivar: 0x6a0
   __DATA.__data: 0x1ce8
-  __DATA.__bss: 0x640
+  __DATA.__bss: 0x648
   __DATA_DIRTY.__objc_data: 0x2a80
   __DATA_DIRTY.__data: 0xc
-  __DATA_DIRTY.__bss: 0x208
+  __DATA_DIRTY.__bss: 0x1f8
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 0C27D10D-E90D-390F-8D9F-1B2A61B4342B
-  Functions: 2522
-  Symbols:   9480
-  CStrings:  4186
+  UUID: 15CB39C1-0573-36BC-B6E2-49B1CF43A631
+  Functions: 2517
+  Symbols:   9466
+  CStrings:  4197
 
Symbols:
+ +[IFImage(ISPlaceholderImage) _placeholderImageWithImageDescriptor:markAsPlaceholder:fallbackTypeID:referenceIcon:variant:]
+ +[IFImage(ISPlaceholderImage) _placeholderImageWithImageDescriptor:markAsPlaceholder:fallbackTypeID:referenceIcon:variant:].cold.1
+ -[ISDefaults isDebugPlaceholderIconsEnabled]
+ -[ISDefaults isInternalBuild]
+ -[ISDefaults isInternalBuild].cold.1
+ -[ISStaticResources cacheMissIconResourceForPlatform:variant:]
+ -[ISStaticResources cacheMissIconResourceForPlatform:variant:].cold.1
+ -[ISStaticResources cacheMissIconResourceForVariant:]
+ -[ISStaticResources fallbackResourceForHint:descriptor:referenceObj:variant:]
+ -[ISStaticResources fallbackResourceForHint:descriptor:referenceObj:variant:].cold.1
+ -[ISStaticResources fallbackResourceForHint:descriptor:referenceObj:variant:].cold.2
+ -[ISStaticResources fallbackResourceForHint:descriptor:referenceObj:variant:].cold.3
+ -[ISStaticResources genericAppIconResourceForPlatform:variant:]
+ -[ISStaticResources genericAppIconResourceForPlatform:variant:].cold.1
+ GCC_except_table27
+ ___29-[ISDefaults isInternalBuild]_block_invoke
+ ___46-[ISConcreteIcon generateImageWithDescriptor:]_block_invoke.17
+ ___46-[ISConcreteIcon generateImageWithDescriptor:]_block_invoke.17.cold.1
+ ___57-[ISConcreteIcon generateImageWithDescriptor:completion:]_block_invoke.23
+ ___block_literal_global.43
+ ___block_literal_global.53
+ ___block_literal_global.69
+ ___block_literal_global.79
+ _isInternalBuild.isInternal
+ _isInternalBuild.once
+ _objc_msgSend$_placeholderImageWithImageDescriptor:markAsPlaceholder:fallbackTypeID:referenceIcon:variant:
+ _objc_msgSend$cacheMissIconResourceForPlatform:variant:
+ _objc_msgSend$cacheMissIconResourceForVariant:
+ _objc_msgSend$fallbackResourceForHint:descriptor:referenceObj:variant:
+ _objc_msgSend$genericAppIconResourceForPlatform:variant:
+ _objc_msgSend$isDebugPlaceholderIconsEnabled
+ _objc_msgSend$isInternalBuild
+ _sharedInstance.onceToken.41
+ _sharedInstance.onceToken.51
+ _sharedInstance.onceToken.67
+ _sharedInstance.onceToken.77
+ _sharedInstance.sharedInstance.40
+ _sharedInstance.sharedInstance.50
+ _sharedInstance.sharedInstance.66
+ _sharedInstance.sharedInstance.76
- +[IFImage(ISPlaceholderImage) _placeholderImageWithImageDescriptor:markAsPlaceholder:fallbackTypeID:referenceIcon:].cold.1
- +[ISResourceProvider(Convenience) placeholderIconResourceProvider]
- -[ISConcreteIcon _placeholderImageForError:descriptor:].cold.1
- -[ISStaticResources fallbackResourceForHint:descriptor:referenceObj:]
- -[ISStaticResources fallbackResourceForHint:descriptor:referenceObj:].cold.1
- -[ISStaticResources fallbackResourceForHint:descriptor:referenceObj:].cold.2
- -[ISStaticResources fallbackResourceForHint:descriptor:referenceObj:].cold.3
- -[ISStaticResources fallbackResourceForHint:descriptor:referenceObj:].cold.4
- -[ISStaticResources fallbackResourceForHint:descriptor:referenceObj:].cold.5
- -[ISStaticResources genericAppIconResourceForPlatform:]
- -[ISStaticResources genericAppIconResourceForPlatform:].cold.1
- -[ISStaticResources placeholderIconResourceForPlatform:]
- -[ISStaticResources placeholderIconResourceForPlatform:].cold.1
- -[ISStaticResources placeholderIconResource]
- GCC_except_table17
- _OUTLINED_FUNCTION_10
- _OUTLINED_FUNCTION_11
- _OUTLINED_FUNCTION_6
- _OUTLINED_FUNCTION_7
- _OUTLINED_FUNCTION_8
- _OUTLINED_FUNCTION_9
- ___46-[ISConcreteIcon generateImageWithDescriptor:]_block_invoke.18
- ___46-[ISConcreteIcon generateImageWithDescriptor:]_block_invoke.18.cold.1
- ___55-[ISConcreteIcon _placeholderImageForError:descriptor:]_block_invoke
- ___57-[ISConcreteIcon generateImageWithDescriptor:completion:]_block_invoke.25
- ___block_literal_global.41
- ___block_literal_global.51
- ___block_literal_global.67
- __placeholderImageForError:descriptor:.isInternal
- __placeholderImageForError:descriptor:.once
- _objc_msgSend$fallbackResourceForHint:descriptor:referenceObj:
- _objc_msgSend$genericAppIconResourceForPlatform:
- _objc_msgSend$placeholderIconResource
- _objc_msgSend$placeholderIconResourceForPlatform:
- _objc_msgSend$placeholderIconResourceProvider
- _sharedInstance.onceToken.39
- _sharedInstance.onceToken.49
- _sharedInstance.onceToken.65
- _sharedInstance.onceToken.75
- _sharedInstance.sharedInstance.38
- _sharedInstance.sharedInstance.48
- _sharedInstance.sharedInstance.64
- _sharedInstance.sharedInstance.74
CStrings:
+ "01:45:02"
+ "@48@0:8@16@24@32Q40"
+ "@52@0:8@16B24@28@36Q44"
+ "CacheMissIcon_iOS_Debug"
+ "CacheMissIcon_iOS_Debug_SPIExplicitlyRequested"
+ "GenericAppIcon_iOS_Debug_SPIExplicitlyRequested"
+ "_placeholderImageWithImageDescriptor:markAsPlaceholder:fallbackTypeID:referenceIcon:variant:"
+ "cacheMissIconResourceForPlatform:variant:"
+ "cacheMissIconResourceForVariant:"
+ "debug_placeholder_icons"
+ "fallbackResourceForHint:descriptor:referenceObj:variant:"
+ "genericAppIconResourceForPlatform:variant:"
+ "isDebugPlaceholderIconsEnabled"
+ "isInternalBuild"
- "18:12:23"
- "fallbackResourceForHint:descriptor:referenceObj:"
- "genericAppIconResourceForPlatform:"
- "placeholderIconResource"
- "placeholderIconResourceForPlatform:"
- "placeholderIconResourceProvider"

```
