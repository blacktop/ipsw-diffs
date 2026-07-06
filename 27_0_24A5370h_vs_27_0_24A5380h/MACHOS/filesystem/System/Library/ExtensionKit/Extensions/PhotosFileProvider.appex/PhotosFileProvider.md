## PhotosFileProvider

> `/System/Library/ExtensionKit/Extensions/PhotosFileProvider.appex/PhotosFileProvider`

```diff

-  __TEXT.__text: 0x24c4
-  __TEXT.__auth_stubs: 0x300
-  __TEXT.__objc_stubs: 0x9c0
+  __TEXT.__text: 0x27ac
+  __TEXT.__auth_stubs: 0x320
+  __TEXT.__objc_stubs: 0xaa0
   __TEXT.__objc_methlist: 0x11c
   __TEXT.__const: 0x48
-  __TEXT.__objc_methname: 0x9d8
-  __TEXT.__oslogstring: 0x564
-  __TEXT.__cstring: 0x265
+  __TEXT.__objc_methname: 0xa7e
+  __TEXT.__oslogstring: 0x64f
+  __TEXT.__cstring: 0x296
   __TEXT.__objc_classname: 0x40
   __TEXT.__objc_methtype: 0xdf
   __TEXT.__unwind_info: 0xb8
-  __DATA_CONST.__const: 0xe0
-  __DATA_CONST.__cfstring: 0x2e0
+  __DATA_CONST.__const: 0x108
+  __DATA_CONST.__cfstring: 0x300
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__auth_got: 0x188
-  __DATA_CONST.__got: 0x100
+  __DATA_CONST.__auth_got: 0x198
+  __DATA_CONST.__got: 0x110
   __DATA.__objc_const: 0x2e0
-  __DATA.__objc_selrefs: 0x2a0
+  __DATA.__objc_selrefs: 0x2d8
   __DATA.__objc_ivar: 0x18
   __DATA.__objc_data: 0xf0
   __DATA.__bss: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 27
-  Symbols:   90
-  CStrings:  189
+  Symbols:   94
+  CStrings:  200
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_data : content changed
Symbols:
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_PHFetchOptions
+ _objc_retain_x25
+ _objc_retain_x26
Functions:
~ sub_1000017d0 : 2032 -> 2092
~ sub_100001fc0 -> sub_100001ffc : 40 -> 724
CStrings:
+ "Adjustment timestamp changed during export for asset %{public}@: expected %{public}@, current %{public}@"
+ "Asset adjustment timestamp changed during export"
+ "Nil result refetching asset %{public}@, may have been expunged during export, but after the share action, will proceed with share"
+ "arrayWithObjects:count:"
+ "fetchAssetsWithLocalIdentifiers:options:"
+ "firstObject"
+ "setIncludeGuestAssets:"
+ "setIncludeHiddenAssets:"
+ "setIncludeTrashedAssets:"
+ "setPhotoLibrary:"

```
