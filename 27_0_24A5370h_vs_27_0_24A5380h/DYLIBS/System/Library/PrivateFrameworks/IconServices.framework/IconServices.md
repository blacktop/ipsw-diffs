## IconServices

> `/System/Library/PrivateFrameworks/IconServices.framework/IconServices`

```diff

-  __TEXT.__text: 0x676b0
+  __TEXT.__text: 0x670e4
   __TEXT.__delay_stubs: 0x80
   __TEXT.__delay_helper: 0xa4
-  __TEXT.__objc_methlist: 0x69bc
+  __TEXT.__objc_methlist: 0x6964
   __TEXT.__const: 0x8840
-  __TEXT.__cstring: 0x454f
-  __TEXT.__oslogstring: 0x40fc
+  __TEXT.__cstring: 0x44f1
+  __TEXT.__oslogstring: 0x406a
   __TEXT.__gcc_except_tab: 0x610
-  __TEXT.__unwind_info: 0x19d8
+  __TEXT.__unwind_info: 0x19c8
   __TEXT.__eh_frame: 0x80
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xa10
+  __DATA_CONST.__const: 0xa38
   __DATA_CONST.__objc_classlist: 0x530
   __DATA_CONST.__objc_catlist: 0xf8
-  __DATA_CONST.__objc_protolist: 0x118
+  __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x31b0
-  __DATA_CONST.__objc_protorefs: 0x30
+  __DATA_CONST.__objc_selrefs: 0x3180
+  __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x400
   __DATA_CONST.__objc_arraydata: 0xc8
-  __DATA_CONST.__got: 0x650
+  __DATA_CONST.__got: 0x6a8
   __AUTH_CONST.__const: 0x11a8
-  __AUTH_CONST.__cfstring: 0x48e0
-  __AUTH_CONST.__objc_const: 0x143a8
+  __AUTH_CONST.__cfstring: 0x48a0
+  __AUTH_CONST.__objc_const: 0x13f98
   __AUTH_CONST.__objc_intobj: 0x570
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__auth_got: 0x7f0
-  __AUTH.__objc_data: 0x820
+  __AUTH.__objc_data: 0x870
   __DATA.__objc_ivar: 0x6d0
-  __DATA.__data: 0x1d4c
-  __DATA.__bss: 0x688
-  __DATA_DIRTY.__objc_data: 0x2bc0
+  __DATA.__data: 0x1cf0
+  __DATA.__bss: 0x698
+  __DATA_DIRTY.__objc_data: 0x2b70
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x1d0
+  __DATA_DIRTY.__bss: 0x1c0
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2609
-  Symbols:   9781
-  CStrings:  1669
+  Functions: 2606
+  Symbols:   9730
+  CStrings:  1661
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __DATA.__objc_ivar : content changed
Symbols:
+ -[ISGenericRecipe isDebugModeEnabled]
+ -[ISGenericRecipe setDebugModeEnabled:]
+ _ISIsTransparent
+ _OBJC_IVAR_$_ISGenericRecipe._debugModeEnabled
+ ___78-[ICRFinalizedIcon(IconServicesAdditions) _IS_imageWithCompositingDescriptor:]_block_invoke
+ ___block_descriptor_56_e8_32s40s48s_e15_^{CGImage=}8?0ls32l8s40l8s48l8
+ _objc_msgSend$isDebugModeEnabled
+ _objc_msgSend$setDebugModeEnabled:
- -[ISCompositingDescriptor cacheFinalizedIconOnGeneratedImage]
- -[ISCompositingDescriptor setCacheFinalizedIconOnGeneratedImage:]
- -[ISDefaults isCalistogaEnabled]
- -[ISDynamicIconStackResource layerDataForSize:scale:]
- -[ISICRCompositor layerDataForCompositingDescriptor:]
- -[ISIconStackAssetCatalogResource layerDataForSize:scale:]
- -[ISIconStackCompositeResource layerDataForSize:scale:]
- _OBJC_IVAR_$_ISCompositingDescriptor._cacheFinalizedIconOnGeneratedImage
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_ISLayerScalableCompositorResource
- __OBJC_$_PROTOCOL_METHOD_TYPES_ISLayerScalableCompositorResource
- __OBJC_$_PROTOCOL_REFS_ISLayerScalableCompositorResource
- __OBJC_LABEL_PROTOCOL_$_ISLayerScalableCompositorResource
- __OBJC_PROTOCOL_$_ISLayerScalableCompositorResource
- __OBJC_PROTOCOL_REFERENCE_$_ISLayerScalableCompositorResource
- _objc_msgSend$borderWidth
- _objc_msgSend$cacheFinalizedIconOnGeneratedImage
- _objc_msgSend$initWithCGImage:scale:finalizedIcon:
- _objc_msgSend$initWithCGImage:scale:layerData:
- _objc_msgSend$initWithLineWidth:color:
- _objc_msgSend$isCalistogaEnabled
- _objc_msgSend$layerDataForCompositingDescriptor:
- _objc_msgSend$layerDataForSize:scale:
- _objc_msgSend$serializedDataWithError:
CStrings:
+ "12:43:35"
+ "Central pixel is still transparent even with retry."
+ "Flattened representation is seemingly a fully transparent image: %@"
+ "^{CGImage=}8@?0"
+ "debug layer"
+ "figure.skating"
- "%d"
- ".calistoga"
- "00:30:55"
- "Calistoga"
- "CalistogaIconServicesOnly"
- "Failed to serialize finalized composite icon for size: (%f,%f) scale:(%lf). Error:%@"
- "Failed to serialize finalized icon for icon stack %@ with descriptor: %@"
- "Failed to serialize finalized icon for named: %@ for size: (%f,%f) scale:(%lf). Error:%@"
- "Remapping %@ -> %@"
- "SwiftUI"
- "com.apple.application-icon.calendar.base"
- "com.apple.application-icon.clock.base"

```
