## MobileStoreDemoKit

> `/System/Library/PrivateFrameworks/MobileStoreDemoKit.framework/MobileStoreDemoKit`

```diff

-1871.40.61.0.0
-  __TEXT.__text: 0x2d240
-  __TEXT.__objc_methlist: 0x2594
+1871.40.62.0.0
+  __TEXT.__text: 0x2d7b8
+  __TEXT.__objc_methlist: 0x25e4
   __TEXT.__const: 0xe8
-  __TEXT.__oslogstring: 0x399c
-  __TEXT.__cstring: 0x7d1e
+  __TEXT.__oslogstring: 0x3ac6
+  __TEXT.__cstring: 0x7dc4
   __TEXT.__gcc_except_tab: 0xcc0
-  __TEXT.__unwind_info: 0x10f8
+  __TEXT.__unwind_info: 0x1108
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x628
-  __DATA_CONST.__objc_classlist: 0xe0
+  __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1988
+  __DATA_CONST.__objc_selrefs: 0x19c0
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0xc0
+  __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0x380
-  __DATA_CONST.__got: 0x2f0
+  __DATA_CONST.__got: 0x2f8
   __AUTH_CONST.__const: 0x2a0
-  __AUTH_CONST.__cfstring: 0x5320
-  __AUTH_CONST.__objc_const: 0x3908
+  __AUTH_CONST.__cfstring: 0x53e0
+  __AUTH_CONST.__objc_const: 0x3a08
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__objc_ivar: 0x248
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x250
   __DATA.__data: 0x9e0
   __DATA_DIRTY.__objc_data: 0x8c0
   __DATA_DIRTY.__bss: 0x80

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1219
-  Symbols:   1719
-  CStrings:  1260
+  Functions: 1228
+  Symbols:   1734
+  CStrings:  1272
 
Symbols:
+ +[MSDKDemoOverlayAsset demoOverlayAssetForApplicationWithBundleIdentifier:]
+ -[MSDKDemoOverlayAsset .cxx_destruct]
+ -[MSDKDemoOverlayAsset assetPath]
+ -[MSDKDemoOverlayAsset assetType]
+ -[MSDKDemoOverlayAsset initWithAssetType:andAssetPath:]
+ _OBJC_CLASS_$_MSDKDemoOverlayAsset
+ _OBJC_IVAR_$_MSDKDemoOverlayAsset._assetPath
+ _OBJC_IVAR_$_MSDKDemoOverlayAsset._assetType
+ _OBJC_METACLASS_$_MSDKDemoOverlayAsset
+ __OBJC_$_CLASS_METHODS_MSDKDemoOverlayAsset
+ __OBJC_$_INSTANCE_METHODS_MSDKDemoOverlayAsset
+ __OBJC_$_INSTANCE_VARIABLES_MSDKDemoOverlayAsset
+ __OBJC_$_PROP_LIST_MSDKDemoOverlayAsset
+ __OBJC_CLASS_RO_$_MSDKDemoOverlayAsset
+ __OBJC_METACLASS_RO_$_MSDKDemoOverlayAsset
CStrings:
+ "%s - Failed to open asset preferences file %{public}@ - %{public}@"
+ "%s - No overlay assets found at path %{public}@ for app  %{public}@"
+ "%s - Unrecognized preferred overlay asset type: %{public}@ - Default to Image."
+ "%s - assetPath:  %{public}@ - Asset type:  %ld"
+ "%s - preferredAssetType:  %{public}@"
+ "+[MSDKDemoOverlayAsset demoOverlayAssetForApplicationWithBundleIdentifier:]"
+ ".mov"
+ ".png"
+ "/var/mobile/Library/RetailDemo/OverlayAssets"
+ "AssetPreferences.plist"
+ "Image"
+ "Video"
```
