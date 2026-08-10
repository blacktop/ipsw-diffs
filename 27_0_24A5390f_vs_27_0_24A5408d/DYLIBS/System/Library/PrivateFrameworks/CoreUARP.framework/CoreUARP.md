## CoreUARP

> `/System/Library/PrivateFrameworks/CoreUARP.framework/CoreUARP`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__DATA.__data`

```diff

-1587.0.27.0.0
-  __TEXT.__text: 0x89758
-  __TEXT.__objc_methlist: 0x8a38
+1587.2.2.0.0
+  __TEXT.__text: 0x893dc
+  __TEXT.__objc_methlist: 0x8980
   __TEXT.__const: 0x230
-  __TEXT.__cstring: 0x7da1
+  __TEXT.__cstring: 0x7d16
   __TEXT.__oslogstring: 0x6c43
   __TEXT.__gcc_except_tab: 0x88c
   __TEXT.__dlopen_cstrs: 0xa4
-  __TEXT.__unwind_info: 0x26d0
+  __TEXT.__unwind_info: 0x26b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x20c8
-  __DATA_CONST.__objc_classlist: 0x628
+  __DATA_CONST.__objc_classlist: 0x618
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3260
+  __DATA_CONST.__objc_selrefs: 0x3258
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x618
+  __DATA_CONST.__objc_superrefs: 0x608
   __DATA_CONST.__objc_arraydata: 0x20
-  __DATA_CONST.__got: 0x718
+  __DATA_CONST.__got: 0x708
   __AUTH_CONST.__const: 0x260
-  __AUTH_CONST.__cfstring: 0x7180
-  __AUTH_CONST.__objc_const: 0x11410
+  __AUTH_CONST.__cfstring: 0x7060
+  __AUTH_CONST.__objc_const: 0x112a0
   __AUTH_CONST.__objc_intobj: 0xca8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x520
-  __AUTH.__objc_data: 0x20d0
-  __DATA.__objc_ivar: 0xbc4
+  __AUTH.__objc_data: 0x2080
+  __DATA.__objc_ivar: 0xbbc
   __DATA.__data: 0x40d
   __DATA.__bss: 0x1a4b
-  __DATA_DIRTY.__objc_data: 0x1cc0
+  __DATA_DIRTY.__objc_data: 0x1c70
   __DATA_DIRTY.__bss: 0xe0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  Functions: 3970
-  Symbols:   7775
-  CStrings:  2048
+  Functions: 3960
+  Symbols:   7748
+  CStrings:  2039
 
Symbols:
+ _UARPLayer2RequestAssetBuffer
+ _UARPLayer2ReturnAssetBuffer
- +[UARPSupportedAccessoryA2562 appleModelNumber]
- +[UARPSupportedAccessoryA2562 modelUUID]
- +[UARPSupportedAccessoryd5b67c73d2e5e518 appleModelNumber]
- +[UARPSupportedAccessoryd5b67c73d2e5e518 productGroup]
- +[UARPSupportedAccessoryd5b67c73d2e5e518 productID]
- +[UARPSupportedAccessoryd5b67c73d2e5e518 productNumber]
- +[UARPSupportedAccessoryd5b67c73d2e5e518 vendorID]
- -[UARPSupportedAccessoryA2562 .cxx_destruct]
- -[UARPSupportedAccessoryA2562 init]
- -[UARPSupportedAccessoryd5b67c73d2e5e518 .cxx_destruct]
- -[UARPSupportedAccessoryd5b67c73d2e5e518 description]
- -[UARPSupportedAccessoryd5b67c73d2e5e518 init]
- _OBJC_CLASS_$_UARPSupportedAccessoryA2562
- _OBJC_CLASS_$_UARPSupportedAccessoryd5b67c73d2e5e518
- _OBJC_IVAR_$_UARPSupportedAccessoryA2562.hwID
- _OBJC_IVAR_$_UARPSupportedAccessoryd5b67c73d2e5e518.hwID
- _OBJC_METACLASS_$_UARPSupportedAccessoryA2562
- _OBJC_METACLASS_$_UARPSupportedAccessoryd5b67c73d2e5e518
- __OBJC_$_CLASS_METHODS_UARPSupportedAccessoryA2562
- __OBJC_$_CLASS_METHODS_UARPSupportedAccessoryd5b67c73d2e5e518
- __OBJC_$_INSTANCE_METHODS_UARPSupportedAccessoryA2562
- __OBJC_$_INSTANCE_METHODS_UARPSupportedAccessoryd5b67c73d2e5e518
- __OBJC_$_INSTANCE_VARIABLES_UARPSupportedAccessoryA2562
- __OBJC_$_INSTANCE_VARIABLES_UARPSupportedAccessoryd5b67c73d2e5e518
- __OBJC_CLASS_RO_$_UARPSupportedAccessoryA2562
- __OBJC_CLASS_RO_$_UARPSupportedAccessoryd5b67c73d2e5e518
- __OBJC_METACLASS_RO_$_UARPSupportedAccessoryA2562
- __OBJC_METACLASS_RO_$_UARPSupportedAccessoryd5b67c73d2e5e518
- _objc_msgSend$modelUUID
CStrings:
- "693FBEFE-C1E0-4125-96AC-10F8915DA1F3"
- "A2562"
- "HardwareID: %@"
- "PG/PN: %@%@, "
- "Sidekick"
- "Unity Remote"
- "Universal Electronics Inc."
- "d2e5e518"
- "d5b67c73"
```
