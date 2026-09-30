## CarKit

> `/System/Library/PrivateFrameworks/CarKit.framework/CarKit`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-794.0.0.0.0
-  __TEXT.__text: 0x619d0
+797.0.0.0.0
+  __TEXT.__text: 0x61a40
   __TEXT.__delay_stubs: 0x40
   __TEXT.__delay_helper: 0xa4
-  __TEXT.__objc_methlist: 0x62fc
+  __TEXT.__objc_methlist: 0x632c
   __TEXT.__const: 0x558
-  __TEXT.__gcc_except_tab: 0x9e8
+  __TEXT.__gcc_except_tab: 0x9f8
   __TEXT.__oslogstring: 0x6ae6
   __TEXT.__cstring: 0x5a9d
   __TEXT.__dlopen_cstrs: 0x15e

   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x36e0
+  __DATA_CONST.__objc_selrefs: 0x36f8
   __DATA_CONST.__objc_protorefs: 0x108
   __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0xc0
   __DATA_CONST.__got: 0x870
   __AUTH_CONST.__const: 0x1bb0
   __AUTH_CONST.__cfstring: 0x5c40
-  __AUTH_CONST.__objc_const: 0x10290
+  __AUTH_CONST.__objc_const: 0x102d8
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0xac8
   __AUTH.__objc_data: 0x1400
   __AUTH.__data: 0x1b8
-  __DATA.__objc_ivar: 0x72c
+  __DATA.__objc_ivar: 0x730
   __DATA.__data: 0x11a0
   __DATA.__bss: 0x740
   __DATA_DIRTY.__objc_data: 0x640

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3038
-  Symbols:   5995
+  Functions: 3041
+  Symbols:   6000
   CStrings:  1418
 
Symbols:
+ -[CRFeatureAvailability deviceSupportedCarPlayFeaturesForThemeAssetID:]
+ -[CRVehicleAccessory setThemeAssetIdentifier:]
+ -[CRVehicleAccessory themeAssetIdentifier]
+ GCC_except_table14
+ GCC_except_table63
+ GCC_except_table71
+ GCC_except_table88
+ _OBJC_IVAR_$_CRVehicleAccessory._themeAssetIdentifier
+ ___71-[CRFeatureAvailability deviceSupportedCarPlayFeaturesForThemeAssetID:]_block_invoke
+ ___71-[CRFeatureAvailability deviceSupportedCarPlayFeaturesForThemeAssetID:]_block_invoke_2
+ _objc_msgSend$deviceSupportedCarPlayFeaturesForThemeAssetID:
+ _objc_msgSend$deviceSupportedCarPlayFeaturesForThemeAssetID:reply:
+ _objc_msgSend$themeAssetIdentifier
- GCC_except_table17
- GCC_except_table21
- GCC_except_table61
- GCC_except_table69
- GCC_except_table86
- ___55-[CRFeatureAvailability deviceSupportedCarPlayFeatures]_block_invoke
- ___55-[CRFeatureAvailability deviceSupportedCarPlayFeatures]_block_invoke_2
- _objc_msgSend$deviceSupportedCarPlayFeaturesWithReply:
```
