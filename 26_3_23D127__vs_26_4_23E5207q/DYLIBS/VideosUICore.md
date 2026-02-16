## VideosUICore

> `/System/Library/PrivateFrameworks/VideosUICore.framework/VideosUICore`

```diff

-1061.30.15.0.1
-  __TEXT.__text: 0x2e29c
-  __TEXT.__auth_stubs: 0xc10
-  __TEXT.__objc_methlist: 0x4dec
+1061.40.51.0.2
+  __TEXT.__text: 0x30d60
+  __TEXT.__auth_stubs: 0xbc0
+  __TEXT.__objc_methlist: 0x4e5c
   __TEXT.__const: 0x1e0
-  __TEXT.__cstring: 0x2bce
-  __TEXT.__oslogstring: 0xd7a
-  __TEXT.__gcc_except_tab: 0x850
+  __TEXT.__cstring: 0x2cbd
+  __TEXT.__oslogstring: 0xda7
+  __TEXT.__gcc_except_tab: 0x7d8
   __TEXT.__ustring: 0x6a
-  __TEXT.__unwind_info: 0xf40
-  __TEXT.__objc_classname: 0x8c8
-  __TEXT.__objc_methname: 0xd7bb
-  __TEXT.__objc_methtype: 0x22ab
-  __TEXT.__objc_stubs: 0x89a0
-  __DATA_CONST.__got: 0x5d0
-  __DATA_CONST.__const: 0x1b90
+  __TEXT.__unwind_info: 0x1128
+  __TEXT.__objc_classname: 0x8e2
+  __TEXT.__objc_methname: 0xd8b3
+  __TEXT.__objc_methtype: 0x22f2
+  __TEXT.__objc_stubs: 0x89c0
+  __DATA_CONST.__got: 0x5d8
+  __DATA_CONST.__const: 0x1b98
   __DATA_CONST.__objc_classlist: 0x230
   __DATA_CONST.__objc_catlist: 0xb0
-  __DATA_CONST.__objc_protolist: 0xa8
+  __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3458
+  __DATA_CONST.__objc_selrefs: 0x3488
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x198
-  __AUTH_CONST.__auth_got: 0x618
-  __AUTH_CONST.__const: 0x560
-  __AUTH_CONST.__cfstring: 0x56e0
-  __AUTH_CONST.__objc_const: 0x7e08
+  __AUTH_CONST.__auth_got: 0x5f0
+  __AUTH_CONST.__const: 0x540
+  __AUTH_CONST.__cfstring: 0x5840
+  __AUTH_CONST.__objc_const: 0x7ea0
   __AUTH_CONST.__objc_intobj: 0x300
   __AUTH_CONST.__objc_doubleobj: 0xc0
   __AUTH.__objc_data: 0x780
-  __DATA.__objc_ivar: 0x52c
-  __DATA.__data: 0x7f8
+  __DATA.__objc_ivar: 0x530
+  __DATA.__data: 0x858
   __DATA.__bss: 0x78
   __DATA_DIRTY.__objc_data: 0xe60
   __DATA_DIRTY.__data: 0x10

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0E4182D7-A67C-3817-8160-1AC841BC5D0C
-  Functions: 1667
-  Symbols:   6148
-  CStrings:  4201
+  UUID: 5D9C9759-AB95-3571-86F1-2537F834B6BA
+  Functions: 1676
+  Symbols:   6169
+  CStrings:  4237
 
Symbols:
+ +[VUIDevice isPhoneOrPad]
+ +[VUIImageFactory URLFromSource:extension:p3Specifier:cropCode:imageSize:displayScaleIsPointMultiplier:centerGrowth:focusSizeIncrease:displayScale:]
+ -[VUIDebugDefaults dealloc]
+ -[VUIDebugDefaults userDefaultsDidChange:]
+ -[VUIImage uiImageWithScale:]
+ -[VUIRemoteImageDescriptor displayScale]
+ -[VUIRemoteImageDescriptor setDisplayScale:]
+ _NSUserDefaultsDidChangeNotification
+ _OBJC_IVAR_$_VUIRemoteImageDescriptor._displayScale
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _URLFromSource:extension:p3Specifier:cropCode:imageSize:displayScaleIsPointMultiplier:centerGrowth:focusSizeIncrease:displayScale:.onceToken
+ _URLFromSource:extension:p3Specifier:cropCode:imageSize:displayScaleIsPointMultiplier:centerGrowth:focusSizeIncrease:displayScale:.sPointMultiplier
+ _VUIDefaultsIsTapToRadarEnabled
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_VUISelectingViewPressing
+ __OBJC_$_PROTOCOL_METHOD_TYPES_VUISelectingViewPressing
+ __OBJC_$_PROTOCOL_REFS_VUISelectingViewPressing
+ __OBJC_LABEL_PROTOCOL_$_VUISelectingViewPressing
+ __OBJC_PROTOCOL_$_VUISelectingViewPressing
+ ___148+[VUIImageFactory URLFromSource:extension:p3Specifier:cropCode:imageSize:displayScaleIsPointMultiplier:centerGrowth:focusSizeIncrease:displayScale:]_block_invoke
+ ___81-[VUIAssetLibrary _setImageAsset:forKey:inGroupOfType:expiryDate:overWrite:tags:]_block_invoke.50
+ _objc_msgSend$URLFromSource:extension:p3Specifier:cropCode:imageSize:displayScaleIsPointMultiplier:centerGrowth:focusSizeIncrease:displayScale:
+ _objc_msgSend$displayScale
- +[VUIImageFactory URLFromSource:extension:p3Specifier:cropCode:imageSize:displayScaleIsPointMultiplier:centerGrowth:focusSizeIncrease:].cold.1
- _URLFromSource:extension:p3Specifier:cropCode:imageSize:displayScaleIsPointMultiplier:centerGrowth:focusSizeIncrease:.onceToken
- _URLFromSource:extension:p3Specifier:cropCode:imageSize:displayScaleIsPointMultiplier:centerGrowth:focusSizeIncrease:.sPointMultiplier
- ___135+[VUIImageFactory URLFromSource:extension:p3Specifier:cropCode:imageSize:displayScaleIsPointMultiplier:centerGrowth:focusSizeIncrease:]_block_invoke
- ___81-[VUIAssetLibrary _setImageAsset:forKey:inGroupOfType:expiryDate:overWrite:tags:]_block_invoke.47
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$URLFromSource:extension:p3Specifier:cropCode:imageSize:displayScaleIsPointMultiplier:centerGrowth:focusSizeIncrease:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
CStrings:
+ "6"
+ "@\"UIViewController\"16@0:8"
+ "@88@0:8@16@24@32@40{CGSize=dd}48B64B68d72d80"
+ "CarPlayOverlayCache"
+ "DebugDefault:: debugUIEnabled changed to: %d"
+ "Derelicte"
+ "SimpleProfiles"
+ "Td,N,V_displayScale"
+ "URLFromSource:extension:p3Specifier:cropCode:imageSize:displayScaleIsPointMultiplier:centerGrowth:focusSizeIncrease:displayScale:"
+ "VUISelectingViewPressing"
+ "_displayScale"
+ "a6"
+ "bars-6"
+ "bars-a6"
+ "derelicte"
+ "disableSparkleSearch"
+ "displayScale"
+ "enableSparkleCategoryV3"
+ "enableSparkleFilter"
+ "europa"
+ "isPhoneOrPad"
+ "isTapToRadarEnabled"
+ "kalamazoo"
+ "setDisplayScale:"
+ "simple_profiles"
+ "sparkleCanonicalBrowse"
+ "sparkleCategoryV3"
+ "sparkleContentTypeV2"
+ "sparkleFilter"
+ "sparkleSearch"
+ "sparkleUTS"
+ "uiImageWithScale:"
+ "userDefaultsDidChange:"
+ "zoomer"
- "clayface"
- "huracan"
- "juniper"
- "kobey"
- "malone"
- "nimbus"
- "opal"
- "puget"
- "tyria"

```
