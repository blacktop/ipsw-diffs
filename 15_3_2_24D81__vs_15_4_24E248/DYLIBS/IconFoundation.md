## IconFoundation

> `/System/Library/PrivateFrameworks/IconFoundation.framework/Versions/A/IconFoundation`

```diff

-644.11.0.0.0
-  __TEXT.__text: 0x3409c
+657.10.0.0.0
+  __TEXT.__text: 0x34110
   __TEXT.__auth_stubs: 0xe70
-  __TEXT.__objc_methlist: 0x2be0
-  __TEXT.__const: 0x7d8
+  __TEXT.__objc_methlist: 0x2d6c
+  __TEXT.__const: 0x7d0
   __TEXT.__cstring: 0x5694
   __TEXT.__oslogstring: 0x950
   __TEXT.__gcc_except_tab: 0x40
-  __TEXT.__unwind_info: 0xcd0
+  __TEXT.__unwind_info: 0xcc0
   __TEXT.__objc_classname: 0x540
   __TEXT.__objc_methname: 0x60e2
   __TEXT.__objc_methtype: 0x1599

   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c30
+  __DATA_CONST.__objc_selrefs: 0x1ca8
   __DATA_CONST.__objc_superrefs: 0x108
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x748
   __AUTH_CONST.__const: 0x8f8
   __AUTH_CONST.__cfstring: 0x19e0
-  __AUTH_CONST.__objc_const: 0x4b00
+  __AUTH_CONST.__objc_const: 0x4830
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0xf00
   __DATA.__objc_ivar: 0x304

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DBF2F73F-E6A1-3EF4-AFFE-D29ED708EB3E
-  Functions: 1310
-  Symbols:   2978
+  UUID: 77625A9D-9859-3C8E-899D-A3C6992A6A90
+  Functions: 1343
+  Symbols:   3030
   CStrings:  2552
 
Symbols:
+ +[CUIPlaceholderCUIRuntimeStatistics sharedRuntimeStatistics].cold.1
+ +[IFBundle appIconOverrideBundle].cold.1
+ +[IFBundle coreGlyphsBundle].cold.1
+ +[IFBundle coreGlyphsPrivateBundle].cold.1
+ +[IFBundle coreTypesBundle].cold.1
+ +[IFBundle frameworkBundle].cold.1
+ +[IFBundle iconFoundationFrameworkBundle].cold.1
+ +[IFBundle iconsetResourceBundle].cold.1
+ +[IFBundle mainBundle].cold.1
+ +[IFBundle mobileIconsFrameworkBundle].cold.1
+ +[IFColor deviceGreyColorSpace].cold.1
+ +[IFColor deviceRGBColorSpace].cold.1
+ +[IFDeviceInfo sharedInstance].cold.1
+ +[IFGraphicSymbolDefaults sharedInstance].cold.1
+ +[IFGraphicSymbolOverrides overridesFileURL].cold.1
+ +[IFGraphicSymbolOverrides overrides].cold.2
+ +[IFIconSpecification(Constructors) iosAppIconSpecification].cold.1
+ +[IFIconSpecification(Constructors) iosDocumentGlyphSpecification].cold.1
+ +[IFIconSpecification(Constructors) iosDocumentIconSpecification].cold.1
+ +[IFIconSpecification(Constructors) iosMessagesAppIconSpecification].cold.1
+ +[IFIconSpecification(Constructors) macosDocumentIconSpecification].cold.1
+ +[IFIconSpecification(Constructors) macosIconSpecification].cold.1
+ +[IFIconSpecification(Constructors) macosTemplateIconSpecification].cold.1
+ +[IFIconSpecification(Constructors) rOSAppIconSpecification].cold.1
+ +[IFIconSpecification(Constructors) tvAppIconSpecification].cold.1
+ +[IFIconSpecification(Constructors) watchAppIconSpecification].cold.1
+ +[IFImage defaultCGColorSpace].cold.1
+ +[IFPlatformInfo sharedInstance].cold.1
+ +[IFPlistParser topLevelAppBundleIconKeys].cold.1
+ +[IFResourceMetadata metadataWithFileName:].cold.3
+ +[IFSymbol _coreGlyphsBundle].cold.1
+ +[IFSymbol _coreGlyphsPrivateBundle].cold.1
+ +[NSURL(IconFoundationAdditions_Internal) coreGlyphsBundleURL].cold.1
+ +[NSURL(IconFoundationAdditions_Internal) coreGlyphsPrivateBundleURL].cold.1
+ +[NSUUID(IconFoundationAdditions) _IF_nullUUID].cold.1
+ -[IFGraphicSymbolDescriptor _debugDynamicGraphicIconColor].cold.1
+ -[IFGraphicSymbolDescriptor _isDebugGraphicIconColourEnabled].cold.1
+ -[IFImage _isDummyCALayerEnabled].cold.1
+ BOMExceptionHandlerSet.cold.1
+ BOMStorageCopyFromBlockRange.cold.1
+ BOMStorageCopyToBlockRange.cold.1
+ BOMStorageCopyToBlockRange.cold.2
+ BOMStorageCopyToBlockRange.cold.3
+ BOMStorageCopyToBlockRange.cold.4
+ BOMStorageCopyToBlockRange.cold.5
+ BOMStreamReadBuffer.cold.1
+ CGImageProviderAuxInfo.cold.1
+ IFDefaultLog.cold.1
+ __BOMExceptionMessageString.cold.1
+ __BOMGlobalExceptionHandler.cold.1
+ getGraphicsClassUsage.cold.1
- ___VectorGlyphDimension2ToPointSizeTableWatch
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreUI/Bom/Common/BOMStack.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreUI/Bom/Common/BOMSystemCmds.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreUI/Bom/Storage/BOMStorage.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreUI/Bom/Storage/BOMStream.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreUI/Bom/Storage/BOMTree.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreUI/Bom/Common/BOMStack.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreUI/Bom/Common/BOMSystemCmds.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreUI/Bom/Storage/BOMStorage.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreUI/Bom/Storage/BOMStream.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreUI/Bom/Storage/BOMTree.c"

```
