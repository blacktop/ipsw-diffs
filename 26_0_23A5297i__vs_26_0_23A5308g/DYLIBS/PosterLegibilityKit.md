## PosterLegibilityKit

> `/System/Library/PrivateFrameworks/PosterLegibilityKit.framework/PosterLegibilityKit`

```diff

-286.101.0.0.0
-  __TEXT.__text: 0x18f0c
-  __TEXT.__auth_stubs: 0xc60
-  __TEXT.__objc_methlist: 0x1a04
-  __TEXT.__const: 0x2f8
-  __TEXT.__cstring: 0xc8e
-  __TEXT.__oslogstring: 0xd92
-  __TEXT.__gcc_except_tab: 0x58c
-  __TEXT.__unwind_info: 0x7e8
-  __TEXT.__objc_classname: 0x4d3
-  __TEXT.__objc_methname: 0x4349
-  __TEXT.__objc_methtype: 0xc72
-  __TEXT.__objc_stubs: 0x3640
-  __DATA_CONST.__got: 0x348
-  __DATA_CONST.__const: 0x850
-  __DATA_CONST.__objc_classlist: 0xf8
+289.103.0.0.0
+  __TEXT.__text: 0x19ad0
+  __TEXT.__auth_stubs: 0xc90
+  __TEXT.__objc_methlist: 0x1ae4
+  __TEXT.__const: 0x300
+  __TEXT.__cstring: 0xd3a
+  __TEXT.__oslogstring: 0xdc4
+  __TEXT.__gcc_except_tab: 0x650
+  __TEXT.__unwind_info: 0x858
+  __TEXT.__objc_classname: 0x4fa
+  __TEXT.__objc_methname: 0x46f2
+  __TEXT.__objc_methtype: 0xca6
+  __TEXT.__objc_stubs: 0x3740
+  __DATA_CONST.__got: 0x368
+  __DATA_CONST.__const: 0x8a0
+  __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_catlist: 0x50
-  __DATA_CONST.__objc_protolist: 0x68
+  __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x10b8
-  __DATA_CONST.__objc_superrefs: 0xe0
-  __AUTH_CONST.__auth_got: 0x640
-  __AUTH_CONST.__const: 0x1e0
-  __AUTH_CONST.__cfstring: 0xba0
-  __AUTH_CONST.__objc_const: 0x4910
+  __DATA_CONST.__objc_selrefs: 0x1150
+  __DATA_CONST.__objc_superrefs: 0xe8
+  __AUTH_CONST.__auth_got: 0x658
+  __AUTH_CONST.__const: 0x240
+  __AUTH_CONST.__cfstring: 0xd20
+  __AUTH_CONST.__objc_const: 0x4e98
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH.__objc_data: 0x3c0
-  __DATA.__objc_ivar: 0x1e4
-  __DATA.__data: 0x4e0
-  __DATA.__bss: 0x128
-  __DATA_DIRTY.__objc_data: 0x5f0
-  __DATA_DIRTY.__bss: 0x58
+  __AUTH.__objc_data: 0x280
+  __DATA.__objc_ivar: 0x20c
+  __DATA.__data: 0x540
+  __DATA.__bss: 0x100
+  __DATA_DIRTY.__objc_data: 0x780
+  __DATA_DIRTY.__bss: 0x90
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E5E3F9D3-2637-3FAA-9FB7-261E26AF4B71
-  Functions: 621
-  Symbols:   2634
-  CStrings:  1213
+  UUID: F06CCDDF-1AF5-3C62-9773-EFF75351C4D5
+  Functions: 646
+  Symbols:   2739
+  CStrings:  1277
 
Symbols:
+ +[PLKLegibilityContent legibilityContentForLabel:legibilityDescriptor:context:]
+ +[PLKLegibilityContent legibilityContentForLabel:legibilityDescriptor:context:renderer:]
+ +[PLKLegibilityContent legibilityContentForLabel:legibilityDescriptor:context:renderer:].cold.1
+ +[PLKLegibilityContext contextWithIdentifier:preferredCacheCapacity:displayScale:cacheProvider:]
+ +[PLKLegibilityContext contextWithIdentifier:preferredCacheCapacity:displayScale:cacheProvider:].cold.1
+ +[PLKLegibilityContext defaultContext]
+ +[PLKLegibilityContext defaultContext].cold.1
+ -[PLKCachedLegibilityContentDataSource removeAllObjectsWithCompletion:]
+ -[PLKCachedLegibilityContentDataSource synchonrouslyRemoveAllObjects]
+ -[PLKLegibilityContext .cxx_destruct]
+ -[PLKLegibilityContext _memoryWarningDidFire:]
+ -[PLKLegibilityContext cacheIdentifier]
+ -[PLKLegibilityContext cancel]
+ -[PLKLegibilityContext displayScale]
+ -[PLKLegibilityContext imageForKey:generatingIfNil:]
+ -[PLKLegibilityContext initWithCacheIdentifier:preferredCacheCapacity:displayScale:cacheProvider:]
+ -[PLKLegibilityContext mappedImageCachePathProvider]
+ -[PLKLegibilityContext preferredCacheCapacity]
+ -[_PLKUILabelCacheKey stringKey]
+ GCC_except_table0
+ GCC_except_table40
+ GCC_except_table42
+ _CGImageGetAlphaInfo
+ _NSStringFromCGRect
+ _OBJC_CLASS_$_BSAtomicSignal
+ _OBJC_CLASS_$_NSNotificationCenter
+ _OBJC_CLASS_$_NSRunLoop
+ _OBJC_CLASS_$_PLKLegibilityContext
+ _OBJC_CLASS_$_UIScreen
+ _OBJC_IVAR_$_PLKLegibilityContext._LRUCache
+ _OBJC_IVAR_$_PLKLegibilityContext._cacheIdentifier
+ _OBJC_IVAR_$_PLKLegibilityContext._displayScale
+ _OBJC_IVAR_$_PLKLegibilityContext._knownMappedImageCacheKeys
+ _OBJC_IVAR_$_PLKLegibilityContext._mappedImageCache
+ _OBJC_IVAR_$_PLKLegibilityContext._mappedImageCachePathProvider
+ _OBJC_IVAR_$_PLKLegibilityContext._preferredCacheCapacity
+ _OBJC_IVAR_$__PLKUILabelCacheKey._lineBreakStrategy
+ _OBJC_IVAR_$__PLKUILabelCacheKey._minimumScaleFactor
+ _OBJC_IVAR_$__PLKUILabelCacheKey._stringKey
+ _OBJC_METACLASS_$_PLKLegibilityContext
+ _UIApplicationDidReceiveMemoryWarningNotification
+ __OBJC_$_CLASS_METHODS_PLKLegibilityContext
+ __OBJC_$_CLASS_PROP_LIST_PLKLegibilityContext
+ __OBJC_$_INSTANCE_METHODS_PLKLegibilityContext
+ __OBJC_$_INSTANCE_VARIABLES_PLKLegibilityContext
+ __OBJC_$_PROP_LIST_PLKLegibilityContext
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BSCancellable
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BSCancellable
+ __OBJC_$_PROTOCOL_REFS_BSCancellable
+ __OBJC_CLASS_PROTOCOLS_$_PLKLegibilityContext
+ __OBJC_CLASS_RO_$_PLKLegibilityContext
+ __OBJC_LABEL_PROTOCOL_$_BSCancellable
+ __OBJC_METACLASS_RO_$_PLKLegibilityContext
+ __OBJC_PROTOCOL_$_BSCancellable
+ ___30-[PLKLegibilityContext cancel]_block_invoke
+ ___38+[PLKLegibilityContext defaultContext]_block_invoke
+ ___69-[PLKCachedLegibilityContentDataSource synchonrouslyRemoveAllObjects]_block_invoke
+ ___71-[PLKCachedLegibilityContentDataSource removeAllObjectsWithCompletion:]_block_invoke
+ ___88+[PLKLegibilityContent legibilityContentForLabel:legibilityDescriptor:context:renderer:]_block_invoke
+ ___88+[PLKLegibilityContent legibilityContentForLabel:legibilityDescriptor:context:renderer:]_block_invoke.18
+ ___88+[PLKLegibilityContent legibilityContentForLabel:legibilityDescriptor:context:renderer:]_block_invoke_2
+ ___88+[PLKLegibilityContent legibilityContentForLabel:legibilityDescriptor:context:renderer:]_block_invoke_3
+ ___96+[PLKLegibilityContext contextWithIdentifier:preferredCacheCapacity:displayScale:cacheProvider:]_block_invoke
+ ___block_descriptor_120_e8_32s40s48s56s64s72r_e27_"UIImage"16?0"NSString"8lr72l8s32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_40_e8_32bs_e20_v24?08"NSError"16ls32l8
+ ___block_descriptor_72_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_80_e8_32s_e27_"UIImage"16?0"NSString"8ls32l8
+ ___block_literal_global.14
+ ___block_literal_global.3
+ _contextWithIdentifier:preferredCacheCapacity:displayScale:cacheProvider:.cacheIdentifierToContextMapTable
+ _contextWithIdentifier:preferredCacheCapacity:displayScale:cacheProvider:.onceToken
+ _defaultContext.defaultContext
+ _defaultContext.onceToken
+ _legibilityContentForLabel:legibilityDescriptor:context:renderer:.activelyRenderingLabels
+ _legibilityContentForLabel:legibilityDescriptor:context:renderer:.onceToken
+ _legibilityContentForLabel:legibilityDescriptor:context:renderer:.signpostID
+ _objc_msgSend$addObserver:selector:name:object:
+ _objc_msgSend$contextWithIdentifier:preferredCacheCapacity:displayScale:cacheProvider:
+ _objc_msgSend$currentRunLoop
+ _objc_msgSend$dateWithTimeIntervalSinceNow:
+ _objc_msgSend$defaultCenter
+ _objc_msgSend$defaultContext
+ _objc_msgSend$drawTextInRect:
+ _objc_msgSend$imageForKey:generatingIfNil:
+ _objc_msgSend$initWithCacheIdentifier:preferredCacheCapacity:displayScale:cacheProvider:
+ _objc_msgSend$legibilityContentForLabel:legibilityDescriptor:context:renderer:
+ _objc_msgSend$lineBreakStrategy
+ _objc_msgSend$mainScreen
+ _objc_msgSend$minimumScaleFactor
+ _objc_msgSend$removeAllObjectsWithCompletion:
+ _objc_msgSend$runUntilDate:
+ _objc_msgSend$string
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$stringKey
+ _strlen
- +[PLKLegibilityContent legibilityContentForLabel:legibilityDescriptor:renderer:]
- +[PLKLegibilityContent legibilityContentForLabel:legibilityDescriptor:renderer:].cold.1
- GCC_except_table36
- GCC_except_table38
- _OBJC_CLASS_$_BSPlatform
- __UILegibilityStrengthAutomatic
- ___80+[PLKLegibilityContent legibilityContentForLabel:legibilityDescriptor:renderer:]_block_invoke
- ___80+[PLKLegibilityContent legibilityContentForLabel:legibilityDescriptor:renderer:]_block_invoke.20
- ___80+[PLKLegibilityContent legibilityContentForLabel:legibilityDescriptor:renderer:]_block_invoke_2
- ___block_descriptor_40_e8_32s_e38_"UIImage"16?0"_PLKUILabelCacheKey"8ls32l8
- ___block_descriptor_72_e8_32s40s_e5_v8?0ls32l8s40l8
- _legibilityContentForLabel:legibilityDescriptor:renderer:.activelyRenderingLabels
- _legibilityContentForLabel:legibilityDescriptor:renderer:.cachedLabelImages
- _legibilityContentForLabel:legibilityDescriptor:renderer:.onceToken
- _legibilityContentForLabel:legibilityDescriptor:renderer:.overrideLegibilityDescriptor
- _legibilityContentForLabel:legibilityDescriptor:renderer:.signpostID
- _objc_msgSend$_image
- _objc_msgSend$deviceClass
- _objc_msgSend$legibilityContentForLabel:legibilityDescriptor:renderer:
- _objc_msgSend$legibilityDescriptorForUILegibilitySettings:strength:
- _objc_msgSend$objectForKey:ifNil:
- _objc_msgSend$plk_disableUILabelLRUCache
- _objc_msgSend$plk_forceClassicLegibility
- _objc_msgSend$setMinFillHeight:
- _objc_msgSend$sharedInstance
- _objc_msgSend$usesUILegibility
CStrings:
+ "-legibility"
+ "@\"UIImage\"16@?0@\"NSString\"8"
+ "@48@0:8@16@24@32@40"
+ "@48@0:8@16Q24d32@40"
+ "BSCancellable"
+ "DEFAULT_CONTEXT"
+ "Memory warning did fire for legibility context %@"
+ "PLKLegibilityContext"
+ "T@\"<BSPathProviding>\",R,N,V_mappedImageCachePathProvider"
+ "T@\"NSString\",R,C,N,V_cacheIdentifier"
+ "T@\"PLKLegibilityContext\",R,N"
+ "TQ,R,N,V_preferredCacheCapacity"
+ "Td,R,N,V_displayScale"
+ "_LRUCache"
+ "_cacheIdentifier"
+ "_displayScale"
+ "_knownMappedImageCacheKeys"
+ "_lineBreakStrategy"
+ "_mappedImageCache"
+ "_mappedImageCachePathProvider"
+ "_memoryWarningDidFire:"
+ "_minimumScaleFactor"
+ "_preferredCacheCapacity"
+ "_stringKey"
+ "addObserver:selector:name:object:"
+ "adjustsFontSize:%d,"
+ "alignment:%lu,"
+ "attrString:%@,"
+ "bounds:%@,"
+ "cacheIdentifier"
+ "contextWithIdentifier:preferredCacheCapacity:displayScale:cacheProvider:"
+ "currentRunLoop"
+ "dateWithTimeIntervalSinceNow:"
+ "defaultCenter"
+ "defaultContext"
+ "drawTextInRect:"
+ "font:%@,"
+ "imageForKey:generatingIfNil:"
+ "initWithCacheIdentifier:preferredCacheCapacity:displayScale:cacheProvider:"
+ "legibilityContentForLabel:legibilityDescriptor:context:"
+ "legibilityContentForLabel:legibilityDescriptor:context:renderer:"
+ "lineBreakMode:%lu,"
+ "lineBreakStrategy"
+ "lineBreakStrategy:%lu,"
+ "lines:%lu,"
+ "mainScreen"
+ "mappedImageCachePathProvider"
+ "minimumScaleFactor"
+ "minimumScaleFactor:%f,"
+ "preferredCacheCapacity"
+ "removeAllObjectsWithCompletion:"
+ "runUntilDate:"
+ "s1"
+ "string"
+ "stringByAppendingString:"
+ "stringKey"
+ "synchonrouslyRemoveAllObjects"
+ "text:%@,"
+ "v24@0:8@?16"
- "@\"UIImage\"16@?0@\"_PLKUILabelCacheKey\"8"
- "_image"
- "c"
- "deviceClass"
- "legibilityContentForLabel:legibilityDescriptor:renderer:"
- "setMinFillHeight:"
- "sharedInstance"

```
