## IconFoundation

> `/System/Library/PrivateFrameworks/IconFoundation.framework/Versions/A/IconFoundation`

```diff

-792.100.0.0.0
-  __TEXT.__text: 0x3a0c8
-  __TEXT.__objc_methlist: 0x317c
-  __TEXT.__cstring: 0x12419
+793.1.10.0.0
+  __TEXT.__text: 0x3a6f4
+  __TEXT.__objc_methlist: 0x31ec
+  __TEXT.__cstring: 0x12403
   __TEXT.__const: 0x9a8
   __TEXT.__oslogstring: 0xc2c
   __TEXT.__constg_swiftt: 0x174

   __TEXT.__swift5_fieldmd: 0xb0
   __TEXT.__swift5_types: 0x2c
   __TEXT.__gcc_except_tab: 0xdc
-  __TEXT.__unwind_info: 0xe60
+  __TEXT.__unwind_info: 0xe78
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f68
-  __DATA_CONST.__objc_superrefs: 0x118
+  __DATA_CONST.__objc_selrefs: 0x1f88
+  __DATA_CONST.__objc_superrefs: 0x120
   __DATA_CONST.__objc_arraydata: 0x18
-  __DATA_CONST.__got: 0x3d8
+  __DATA_CONST.__got: 0x3d0
   __AUTH_CONST.__const: 0xb38
-  __AUTH_CONST.__cfstring: 0x1b80
-  __AUTH_CONST.__objc_const: 0x4df8
+  __AUTH_CONST.__cfstring: 0x1b60
+  __AUTH_CONST.__objc_const: 0x4e38
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__auth_got: 0x7d0
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__objc_data: 0x460
-  __DATA.__objc_ivar: 0x348
-  __DATA.__data: 0x2e8
+  __DATA.__objc_ivar: 0x34c
+  __DATA.__data: 0xd8
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x268
+  __DATA.__bss: 0x288
   __DATA.__common: 0x290
-  __DATA_DIRTY.__objc_data: 0xb40
-  __DATA_DIRTY.__data: 0x98
-  __DATA_DIRTY.__bss: 0x1d8
+  __DATA_DIRTY.__objc_data: 0xfa0
+  __DATA_DIRTY.__data: 0x2a8
+  __DATA_DIRTY.__bss: 0x1c8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics
   - /System/Library/Frameworks/CoreImage.framework/Versions/A/CoreImage

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1556
-  Symbols:   3208
-  CStrings:  2840
+  Functions: 1566
+  Symbols:   3222
+  CStrings:  2839
 
Symbols:
+ +[IFGraphicSymbolOverrides _parseItems]
+ +[IFGraphicSymbolOverrides sharedOverrides]
+ +[IFIconSpecification(Constructors) homeAccessoryAppIconSpecification]
+ -[IFDeviceInfo _isForceHomeAccessoryDeviceEnabled]
+ -[IFDeviceInfo isHomeAccessoryDevice]
+ -[IFGraphicSymbolOverride hash]
+ -[IFGraphicSymbolOverride isEqual:]
+ -[IFGraphicSymbolOverrides flush]
+ -[IFGraphicSymbolOverrides init]
+ -[IFGraphicSymbolOverrides lock]
+ -[IFGraphicSymbolOverrides setLock:]
+ OBJC_IVAR_$_IFGraphicSymbolOverrides._lock
+ ___43+[IFGraphicSymbolOverrides sharedOverrides]_block_invoke
+ ___70+[IFIconSpecification(Constructors) homeAccessoryAppIconSpecification]_block_invoke
+ _objc_msgSend$_parseItems
+ _objc_msgSend$isDefault
+ _objc_msgSend$isHomeAccessoryDevice
+ _objc_msgSend$sharedOverrides
+ homeAccessoryAppIconSpecification.iconSpecification
+ homeAccessoryAppIconSpecification.onceToken
+ sharedOverrides.onceToken
+ sharedOverrides.shared
- +[IFGraphicSymbolOverrides overrides]
- -[IFGraphicSymbolOverrides setItems:]
- _OBJC_CLASS_$_NSCache
- ___37+[IFGraphicSymbolOverrides overrides]_block_invoke
- _objc_msgSend$overrides
- _objc_msgSend$setItems:
- overrides.cache
- overrides.onceToken
CStrings:
+ "force_home_accessory_device"
- "_ReadFreeList: tring to read count of freelist table."
- "overrides"
```
