## IconServices

> `/System/Library/PrivateFrameworks/IconServices.framework/IconServices`

```diff

-739.0.0.0.0
-  __TEXT.__text: 0x63874
+740.0.0.0.0
+  __TEXT.__text: 0x63870
   __TEXT.__auth_stubs: 0xf70
   __TEXT.__delay_helper: 0xc8
-  __TEXT.__objc_methlist: 0x66bc
+  __TEXT.__objc_methlist: 0x66a4
   __TEXT.__const: 0x87b2
   __TEXT.__gcc_except_tab: 0x42c
-  __TEXT.__cstring: 0x3e65
-  __TEXT.__oslogstring: 0x3208
-  __TEXT.__unwind_info: 0x1848
+  __TEXT.__cstring: 0x3e70
+  __TEXT.__oslogstring: 0x327c
+  __TEXT.__unwind_info: 0x1850
   __TEXT.__eh_frame: 0x88
-  __TEXT.__objc_classname: 0x1228
-  __TEXT.__objc_methname: 0xbf2b
-  __TEXT.__objc_methtype: 0x1851
-  __TEXT.__objc_stubs: 0x9620
+  __TEXT.__objc_classname: 0x1250
+  __TEXT.__objc_methname: 0xbffc
+  __TEXT.__objc_methtype: 0x18ae
+  __TEXT.__objc_stubs: 0x9680
   __DATA_CONST.__got: 0x628
   __DATA_CONST.__const: 0x9f0
   __DATA_CONST.__objc_classlist: 0x528
   __DATA_CONST.__objc_catlist: 0xf0
-  __DATA_CONST.__objc_protolist: 0x108
+  __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2fd8
+  __DATA_CONST.__objc_selrefs: 0x2ff8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x400
   __DATA_CONST.__objc_arraydata: 0xb0
   __AUTH_CONST.__auth_got: 0x7d0
   __AUTH_CONST.__const: 0x1188
   __AUTH_CONST.__cfstring: 0x42a0
-  __AUTH_CONST.__objc_const: 0x13bb0
+  __AUTH_CONST.__objc_const: 0x13c68
   __AUTH_CONST.__objc_intobj: 0x528
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH.__objc_data: 0x910
-  __DATA.__objc_ivar: 0x6ac
-  __DATA.__data: 0x1c88
+  __DATA.__objc_ivar: 0x6a0
+  __DATA.__data: 0x1ce8
   __DATA.__bss: 0x640
   __DATA_DIRTY.__objc_data: 0x2a80
   __DATA_DIRTY.__data: 0xc

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 23522567-653E-3318-B048-71E291A6E4B5
-  Functions: 2526
-  Symbols:   9474
-  CStrings:  4172
+  UUID: 6A96E1B6-A32C-3D13-9B41-83FBFC56E4BB
+  Functions: 2522
+  Symbols:   9480
+  CStrings:  4186
 
Symbols:
+ -[ISCompositingDescriptor CUINamedImageDeviceClass].cold.2
+ -[ISCompositingDescriptor relativeInset]
+ -[ISCompositingDescriptor resolvedRelativeInsetForSize:scale:]
+ -[ISCompositingDescriptor setRelativeInset:]
+ -[ISIconStackAssetCatalogResource _compositingDescriptorWithSize:scale:].cold.1
+ -[ISIconStackAssetCatalogResource compositingDescriptor]
+ -[ISIconStackAssetCatalogResource setCompositingDescriptor:]
+ _OBJC_IVAR_$_ISCompositingDescriptor._relativeInset
+ _OBJC_IVAR_$_ISDynamicIconStackResource.compositingDescriptor
+ _OBJC_IVAR_$_ISIconStackAssetCatalogResource.compositingDescriptor
+ _OBJC_IVAR_$_ISIconStackCompositeResource.compositingDescriptor
+ __OBJC_$_PROP_LIST_ISCompositesWithCompositingDescriptor
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ISCompositesWithCompositingDescriptor
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ISCompositesWithCompositingDescriptor
+ __OBJC_$_PROTOCOL_REFS_ISCompositesWithCompositingDescriptor
+ __OBJC_LABEL_PROTOCOL_$_ISCompositesWithCompositingDescriptor
+ __OBJC_PROTOCOL_$_ISCompositesWithCompositingDescriptor
+ _objc_msgSend$relativeInset
+ _objc_msgSend$resolvedRelativeInsetForSize:scale:
+ _objc_msgSend$setRelativeIconInset:
- -[ISAssetCatalogResource background]
- -[ISAssetCatalogResource setBackground:]
- -[ISAssetCatalogResource setShouldApplyMask:]
- -[ISAssetCatalogResource setTintColor:]
- -[ISAssetCatalogResource shouldApplyMask]
- -[ISAssetCatalogResource tintColor]
- -[ISIconStackAssetCatalogResource platformStyle]
- -[ISIconStackAssetCatalogResource setPlatformStyle:]
- -[ISIconStackAssetCatalogResource setShape:]
- -[ISIconStackAssetCatalogResource shape]
- _OBJC_IVAR_$_ISAssetCatalogResource._background
- _OBJC_IVAR_$_ISAssetCatalogResource._shouldApplyMask
- _OBJC_IVAR_$_ISAssetCatalogResource._tintColor
- _OBJC_IVAR_$_ISDynamicIconStackResource._compositingDescriptor
- _OBJC_IVAR_$_ISIconStackAssetCatalogResource._platformStyle
- _OBJC_IVAR_$_ISIconStackAssetCatalogResource._shape
- _OBJC_IVAR_$_ISIconStackCompositeResource._compositingDescriptor
CStrings:
+ "21:24:30"
+ "<ISCompositingDescriptor: %p> (%0.2f, %0.2f)@%.0fx a:%ld:..:%ld t:%g:%g:%g:%g ps:%ld b:%ld p:%ld mask:%d legCap:%d ld:%ld shape:%ld inset:%.2f "
+ "@\"ISCompositingDescriptor\"16@0:8"
+ "ISCompositesWithCompositingDescriptor"
+ "Preparing to composite icon stack but with no compositing configuration"
+ "T@\"ISCompositingDescriptor\",C"
+ "T@\"ISCompositingDescriptor\",C,VcompositingDescriptor"
+ "Td,N,V_relativeInset"
+ "Unable to map unknown platform to device class"
+ "Unknown platform! Will attempt to use bundle's platform"
+ "_relativeInset"
+ "d40@0:8{CGSize=dd}16d32"
+ "relativeInset"
+ "resolvedRelativeInsetForSize:scale:"
+ "setRelativeIconInset:"
+ "setRelativeInset:"
+ "v24@0:8@\"ISCompositingDescriptor\"16"
- "23:09:25"
- "<ISCompositingDescriptor: %p> (%0.2f, %0.2f)@%.0fx a:%ld:..:%ld t:%g:%g:%g:%g ps:%ld b:%ld p:%ld mask:%d legCap:%d ld:%ld shape:%ld "
- "Unable to map platform to device class for icon stack: %lu"

```
