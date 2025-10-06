## CarPlayUIServices

> `/System/Library/PrivateFrameworks/CarPlayUIServices.framework/CarPlayUIServices`

```diff

-309.5.6.0.0
-  __TEXT.__text: 0xa018
-  __TEXT.__auth_stubs: 0x430
-  __TEXT.__objc_methlist: 0xf54
+332.13.2.0.0
+  __TEXT.__text: 0x1685c
+  __TEXT.__auth_stubs: 0x4c0
+  __TEXT.__objc_methlist: 0x1f30
   __TEXT.__const: 0x90
-  __TEXT.__cstring: 0xa00
-  __TEXT.__gcc_except_tab: 0x104
-  __TEXT.__oslogstring: 0x425
-  __TEXT.__unwind_info: 0x308
-  __TEXT.__objc_classname: 0x81c
-  __TEXT.__objc_methname: 0x2b83
-  __TEXT.__objc_methtype: 0x8e1
-  __TEXT.__objc_stubs: 0x2100
-  __DATA_CONST.__got: 0x28
-  __DATA_CONST.__const: 0x498
-  __DATA_CONST.__objc_classlist: 0x150
+  __TEXT.__oslogstring: 0x8fd
+  __TEXT.__cstring: 0x1095
+  __TEXT.__gcc_except_tab: 0x254
+  __TEXT.__unwind_info: 0x734
+  __TEXT.__objc_classname: 0xcbb
+  __TEXT.__objc_methname: 0x4c45
+  __TEXT.__objc_methtype: 0x1107
+  __TEXT.__objc_stubs: 0x33e0
+  __DATA_CONST.__got: 0x40
+  __DATA_CONST.__const: 0x7a0
+  __DATA_CONST.__objc_classlist: 0x230
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0xc0
+  __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x54c8
-  __DATA_CONST.__objc_selrefs: 0xae0
-  __AUTH_CONST.__const: 0x1e0
-  __AUTH_CONST.__objc_const: 0xdf0
-  __AUTH_CONST.__cfstring: 0x8c0
-  __AUTH_CONST.__auth_got: 0x228
-  __AUTH.__objc_data: 0xd20
-  __DATA.__objc_protorefs: 0x40
-  __DATA.__objc_classrefs: 0x1f8
-  __DATA.__objc_superrefs: 0x78
-  __DATA.__objc_ivar: 0xbc
-  __DATA.__data: 0x908
-  __DATA.__bss: 0x70
+  __DATA_CONST.__objc_const: 0xb7b8
+  __DATA_CONST.__objc_selrefs: 0x1100
+  __DATA_CONST.__objc_protorefs: 0x70
+  __DATA_CONST.__objc_classrefs: 0x2e8
+  __DATA_CONST.__objc_superrefs: 0x140
+  __AUTH_CONST.__objc_const: 0x1930
+  __AUTH_CONST.__const: 0x380
+  __AUTH_CONST.__cfstring: 0xf60
+  __AUTH_CONST.__auth_got: 0x270
+  __AUTH.__objc_data: 0x15e0
+  __DATA.__objc_ivar: 0x25c
+  __DATA.__data: 0xd88
+  __DATA.__bss: 0x98
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/CarKit.framework/CarKit

   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 234CE420-BC58-36DD-BBAB-9DDFC7653207
-  Functions: 355
-  Symbols:   1752
-  CStrings:  822
+  UUID: 3771D4DB-12C4-3CF9-9515-203444EA63CB
+  Functions: 749
+  Symbols:   3328
+  CStrings:  1413
 
Symbols:
+ +[CRSUIClusterThemeCAPackageAsset supportsBSXPCSecureCoding]
+ +[CRSUIClusterThemeCAPackageWallpaper supportsBSXPCSecureCoding]
+ +[CRSUIClusterThemeColorWallpaper supportsBSXPCSecureCoding]
+ +[CRSUIClusterThemeDisplay supportsBSXPCSecureCoding]
+ +[CRSUIClusterThemeImageAsset supportsBSXPCSecureCoding]
+ +[CRSUIClusterThemeImageWallpaper supportsBSXPCSecureCoding]
+ +[CRSUIClusterThemeLayout supportsBSXPCSecureCoding]
+ +[CRSUIClusterThemeLayoutPreview supportsBSXPCSecureCoding]
+ +[CRSUIClusterThemePalette supportsBSXPCSecureCoding]
+ +[CRSUIClusterThemeSpecification identifier]
+ +[CRSUIClusterThemeSpecification interface]
+ +[CRSUIClusterThemeSpecification serviceQuality]
+ +[CRSUIClusterThemeWallpaper supportsBSXPCSecureCoding]
+ +[CRSUIPunchThroughSpecification identifier]
+ +[CRSUIPunchThroughSpecification interface]
+ +[CRSUIPunchThroughSpecification serviceQuality]
+ +[CRSUISystemWallpaper _wallpaperInfo]
+ +[CRSUISystemWallpaper defaultWallpaper]
+ +[CRSUISystemWallpaper wallpaperWithIdentifier:]
+ +[CRSUISystemWallpaper wallpapers]
+ +[CRSUIWallpaperTraits supportsSecureCoding]
+ +[_CRSUIClusterThemeData supportsBSXPCSecureCoding]
+ +[_CRSUIClusterThemeLayoutData supportsBSXPCSecureCoding]
+ -[CRSUIApplicationSceneSettings frameRateLimit]
+ -[CRSUIApplicationSceneSettingsDiffInspector observeFrameRateLimitWithBlock:]
+ -[CRSUIAssetWallpaper .cxx_destruct]
+ -[CRSUIAssetWallpaper data]
+ -[CRSUIAssetWallpaper description]
+ -[CRSUIAssetWallpaper displayID]
+ -[CRSUIAssetWallpaper identifier]
+ -[CRSUIAssetWallpaper initWithIdentifier:displayID:layoutID:traits:]
+ -[CRSUIAssetWallpaper layoutID]
+ -[CRSUIAssetWallpaper traits]
+ -[CRSUIAssetWallpaper wallpaperIdentifier]
+ -[CRSUICAPackageView .cxx_destruct]
+ -[CRSUICAPackageView initWithPackage:]
+ -[CRSUICAPackageView initWithPackage:dynamicStateProvider:]
+ -[CRSUICAPackageView initWithPackage:state:]
+ -[CRSUICAPackageView initWithPackage:state:dynamicStateProvider:]
+ -[CRSUICAPackageView initWithPackage:state:dynamicStateProvider:].cold.1
+ -[CRSUICAPackageView layoutSubviews]
+ -[CRSUICAPackageView package]
+ -[CRSUICAPackageView setState:]
+ -[CRSUICAPackageView setState:animated:]
+ -[CRSUICAPackageView sizeThatFits:]
+ -[CRSUICAPackageView state]
+ -[CRSUICAPackageView userInterfaceStyleChanged]
+ -[CRSUIClimateOverlaySceneClientSettings presentedPopoverFrames]
+ -[CRSUIClimatePopoverAction init]
+ -[CRSUIClimatePopoverBSActionsHandler .cxx_destruct]
+ -[CRSUIClimatePopoverBSActionsHandler _respondToActions:forFBSScene:inUIScene:fromTransitionContext:]
+ -[CRSUIClimatePopoverBSActionsHandler delegate]
+ -[CRSUIClimatePopoverBSActionsHandler initWithDelegate:]
+ -[CRSUIClimatePopoverBSActionsHandler setDelegate:]
+ -[CRSUIClusterPressAction actionType]
+ -[CRSUIClusterPressAction initWithPressType:]
+ -[CRSUIClusterPressBSActionsHandler .cxx_destruct]
+ -[CRSUIClusterPressBSActionsHandler _respondToActions:forFBSScene:inUIScene:fromTransitionContext:]
+ -[CRSUIClusterPressBSActionsHandler delegate]
+ -[CRSUIClusterPressBSActionsHandler initWithDelegate:]
+ -[CRSUIClusterPressBSActionsHandler setDelegate:]
+ -[CRSUIClusterThemeCAPackageAsset .cxx_destruct]
+ -[CRSUIClusterThemeCAPackageAsset encodeWithBSXPCCoder:]
+ -[CRSUIClusterThemeCAPackageAsset identifier]
+ -[CRSUIClusterThemeCAPackageAsset initWithBSXPCCoder:]
+ -[CRSUIClusterThemeCAPackageAsset initWithIdentifier:url:packageType:]
+ -[CRSUIClusterThemeCAPackageAsset packageType]
+ -[CRSUIClusterThemeCAPackageAsset url]
+ -[CRSUIClusterThemeCAPackageWallpaper .cxx_destruct]
+ -[CRSUIClusterThemeCAPackageWallpaper asset]
+ -[CRSUIClusterThemeCAPackageWallpaper encodeWithBSXPCCoder:]
+ -[CRSUIClusterThemeCAPackageWallpaper initWithAsset:type:lightModeState:darkModeState:]
+ -[CRSUIClusterThemeCAPackageWallpaper initWithAsset:type:lightModeState:darkModeState:supportsDynamicAppearance:]
+ -[CRSUIClusterThemeCAPackageWallpaper initWithAsset:type:state:]
+ -[CRSUIClusterThemeCAPackageWallpaper initWithBSXPCCoder:]
+ -[CRSUIClusterThemeCAPackageWallpaper stateForInterfaceStyle:]
+ -[CRSUIClusterThemeCAPackageWallpaper supportsDynamicAppearance]
+ -[CRSUIClusterThemeCAPackageWallpaper type]
+ -[CRSUIClusterThemeColorWallpaper .cxx_destruct]
+ -[CRSUIClusterThemeColorWallpaper _initWithLightModeColor:darkModeColor:]
+ -[CRSUIClusterThemeColorWallpaper color]
+ -[CRSUIClusterThemeColorWallpaper encodeWithBSXPCCoder:]
+ -[CRSUIClusterThemeColorWallpaper initWithBSXPCCoder:]
+ -[CRSUIClusterThemeColorWallpaper initWithColor:]
+ -[CRSUIClusterThemeColorWallpaper initWithLightModeColor:darkModeColor:]
+ -[CRSUIClusterThemeDisplay .cxx_destruct]
+ -[CRSUIClusterThemeDisplay displayType]
+ -[CRSUIClusterThemeDisplay encodeWithBSXPCCoder:]
+ -[CRSUIClusterThemeDisplay identifier]
+ -[CRSUIClusterThemeDisplay initWithBSXPCCoder:]
+ -[CRSUIClusterThemeDisplay initWithIdentifier:displayType:size:layouts:]
+ -[CRSUIClusterThemeDisplay layouts]
+ -[CRSUIClusterThemeDisplay size]
+ -[CRSUIClusterThemeImageAsset .cxx_destruct]
+ -[CRSUIClusterThemeImageAsset encodeWithBSXPCCoder:]
+ -[CRSUIClusterThemeImageAsset identifier]
+ -[CRSUIClusterThemeImageAsset initWithBSXPCCoder:]
+ -[CRSUIClusterThemeImageAsset initWithIdentifier:url:]
+ -[CRSUIClusterThemeImageAsset url]
+ -[CRSUIClusterThemeImageWallpaper .cxx_destruct]
+ -[CRSUIClusterThemeImageWallpaper assetForInterfaceStyle:]
+ -[CRSUIClusterThemeImageWallpaper encodeWithBSXPCCoder:]
+ -[CRSUIClusterThemeImageWallpaper initWithAsset:]
+ -[CRSUIClusterThemeImageWallpaper initWithBSXPCCoder:]
+ -[CRSUIClusterThemeImageWallpaper initWithLightModeAsset:darkModeAsset:]
+ -[CRSUIClusterThemeImageWallpaper initWithLightModeAsset:darkModeAsset:supportsDynamicAppearance:]
+ -[CRSUIClusterThemeImageWallpaper supportsDynamicAppearance]
+ -[CRSUIClusterThemeLayout .cxx_destruct]
+ -[CRSUIClusterThemeLayout displayName]
+ -[CRSUIClusterThemeLayout encodeWithBSXPCCoder:]
+ -[CRSUIClusterThemeLayout identifier]
+ -[CRSUIClusterThemeLayout initWithBSXPCCoder:]
+ -[CRSUIClusterThemeLayout initWithIdentifier:displayName:palettes:wallpapers:preview:]
+ -[CRSUIClusterThemeLayout isCustomizable]
+ -[CRSUIClusterThemeLayout palettes]
+ -[CRSUIClusterThemeLayout preview]
+ -[CRSUIClusterThemeLayout wallpapers]
+ -[CRSUIClusterThemeLayoutPreview .cxx_destruct]
+ -[CRSUIClusterThemeLayoutPreview asset]
+ -[CRSUIClusterThemeLayoutPreview encodeWithBSXPCCoder:]
+ -[CRSUIClusterThemeLayoutPreview initWithAsset:lightModeStateForPaletteID:darkModeStateForPaletteID:]
+ -[CRSUIClusterThemeLayoutPreview initWithAsset:lightModeStateForPaletteID:darkModeStateForPaletteID:supportsDynamicAppearance:]
+ -[CRSUIClusterThemeLayoutPreview initWithAsset:stateForPaletteID:]
+ -[CRSUIClusterThemeLayoutPreview initWithBSXPCCoder:]
+ -[CRSUIClusterThemeLayoutPreview stateForPaletteIDWithInterfaceStyle:]
+ -[CRSUIClusterThemeLayoutPreview supportsDynamicAppearance]
+ -[CRSUIClusterThemeManager .cxx_destruct]
+ -[CRSUIClusterThemeManager _getURLForAssetWithIdentifier:displayID:completion:]
+ -[CRSUIClusterThemeManager _handleConnectionActivated]
+ -[CRSUIClusterThemeManager _processThemeLayoutData:error:]
+ -[CRSUIClusterThemeManager _processThemeLayoutData:error:].cold.1
+ -[CRSUIClusterThemeManager _setThemeData:completion:]
+ -[CRSUIClusterThemeManager connectionQueue]
+ -[CRSUIClusterThemeManager connection]
+ -[CRSUIClusterThemeManager dataProviderDelegate]
+ -[CRSUIClusterThemeManager defaultWallpapers]
+ -[CRSUIClusterThemeManager delegate]
+ -[CRSUIClusterThemeManager displayID]
+ -[CRSUIClusterThemeManager displays]
+ -[CRSUIClusterThemeManager dynamicAppearanceWallpapersForVehicle:]
+ -[CRSUIClusterThemeManager extraAssetsURL]
+ -[CRSUIClusterThemeManager getURLForAssetWithIdentifier:displayID:completion:]
+ -[CRSUIClusterThemeManager init]
+ -[CRSUIClusterThemeManager invalidate]
+ -[CRSUIClusterThemeManager isReady]
+ -[CRSUIClusterThemeManager loadWallpaperFromData:]
+ -[CRSUIClusterThemeManager loadWallpaperFromData:].cold.1
+ -[CRSUIClusterThemeManager resolveWallpaper:withCompletion:]
+ -[CRSUIClusterThemeManager resolveWallpaper:withCompletion:].cold.1
+ -[CRSUIClusterThemeManager setConnection:]
+ -[CRSUIClusterThemeManager setConnectionQueue:]
+ -[CRSUIClusterThemeManager setDataProviderDelegate:]
+ -[CRSUIClusterThemeManager setDelegate:]
+ -[CRSUIClusterThemeManager setDisplays:]
+ -[CRSUIClusterThemeManager setExtraAssetsURL:]
+ -[CRSUIClusterThemeManager setThemeData:]
+ -[CRSUIClusterThemeManager setThemeData:completion:]
+ -[CRSUIClusterThemeManager themeData]
+ -[CRSUIClusterThemeManager updateExtraAssetsURL:]
+ -[CRSUIClusterThemeManager wallpapers]
+ -[CRSUIClusterThemePalette .cxx_destruct]
+ -[CRSUIClusterThemePalette colorScheme]
+ -[CRSUIClusterThemePalette colors]
+ -[CRSUIClusterThemePalette displayName]
+ -[CRSUIClusterThemePalette encodeWithBSXPCCoder:]
+ -[CRSUIClusterThemePalette identifier]
+ -[CRSUIClusterThemePalette initWithBSXPCCoder:]
+ -[CRSUIClusterThemePalette initWithIdentifier:displayName:colorScheme:sortIndex:colors:]
+ -[CRSUIClusterThemePalette sortIndex]
+ -[CRSUIClusterThemeService .cxx_destruct]
+ -[CRSUIClusterThemeService _connectionQueue_addConnection:]
+ -[CRSUIClusterThemeService _connectionQueue_removeConnection:]
+ -[CRSUIClusterThemeService connectionQueue]
+ -[CRSUIClusterThemeService connections]
+ -[CRSUIClusterThemeService delegate]
+ -[CRSUIClusterThemeService getClusterThemeLayoutData:]
+ -[CRSUIClusterThemeService getClusterThemeLayoutData:].cold.1
+ -[CRSUIClusterThemeService getURLForAssetWithIdentifier:displayID:reply:]
+ -[CRSUIClusterThemeService getURLForAssetWithIdentifier:displayID:reply:].cold.1
+ -[CRSUIClusterThemeService init]
+ -[CRSUIClusterThemeService invalidate]
+ -[CRSUIClusterThemeService listener:didReceiveConnection:withContext:]
+ -[CRSUIClusterThemeService listener:didReceiveConnection:withContext:].cold.1
+ -[CRSUIClusterThemeService listener]
+ -[CRSUIClusterThemeService setConnectionQueue:]
+ -[CRSUIClusterThemeService setConnections:]
+ -[CRSUIClusterThemeService setDelegate:]
+ -[CRSUIClusterThemeService setListener:]
+ -[CRSUIClusterThemeService setThemeData:reply:]
+ -[CRSUIClusterThemeService setThemeDataProvider:]
+ -[CRSUIClusterThemeService themeDataProvider]
+ -[CRSUIClusterThemeService updateExtraAssetsURL:]
+ -[CRSUIClusterThemeWallpaper .cxx_destruct]
+ -[CRSUIClusterThemeWallpaper associatedPaletteID]
+ -[CRSUIClusterThemeWallpaper color]
+ -[CRSUIClusterThemeWallpaper data]
+ -[CRSUIClusterThemeWallpaper displayName]
+ -[CRSUIClusterThemeWallpaper encodeWithBSXPCCoder:]
+ -[CRSUIClusterThemeWallpaper identifier]
+ -[CRSUIClusterThemeWallpaper image]
+ -[CRSUIClusterThemeWallpaper initWithBSXPCCoder:]
+ -[CRSUIClusterThemeWallpaper initWithIdentifier:displayName:color:associatedPaletteID:isDefault:data:traits:]
+ -[CRSUIClusterThemeWallpaper initWithIdentifier:displayName:image:associatedPaletteID:isDefault:data:traits:]
+ -[CRSUIClusterThemeWallpaper initWithIdentifier:displayName:image:package:color:associatedPaletteID:isDefault:data:traits:]
+ -[CRSUIClusterThemeWallpaper initWithIdentifier:displayName:package:associatedPaletteID:isDefault:data:traits:]
+ -[CRSUIClusterThemeWallpaper isDefault]
+ -[CRSUIClusterThemeWallpaper package]
+ -[CRSUIClusterThemeWallpaper traits]
+ -[CRSUIDashboardWidgetSceneSettings frameRateLimit]
+ -[CRSUIInstrumentClusterSceneSettings frameRateLimit]
+ -[CRSUIMutableApplicationSceneSettings frameRateLimit]
+ -[CRSUIMutableApplicationSceneSettings setFrameRateLimit:]
+ -[CRSUIMutableClimateOverlaySceneClientSettings presentedPopoverFrames]
+ -[CRSUIMutableClimateOverlaySceneClientSettings setPresentedPopoverFrames:]
+ -[CRSUIMutableDashboardWidgetSceneSettings frameRateLimit]
+ -[CRSUIMutableDashboardWidgetSceneSettings setFrameRateLimit:]
+ -[CRSUIMutableInstrumentClusterSceneSettings frameRateLimit]
+ -[CRSUIMutableInstrumentClusterSceneSettings setFrameRateLimit:]
+ -[CRSUIMutableProxyApplicationSceneSettings frameRateLimit]
+ -[CRSUIMutableProxyApplicationSceneSettings setFrameRateLimit:]
+ -[CRSUIMutableWallpaperSceneSettings .cxx_destruct]
+ -[CRSUIMutableWallpaperSceneSettings setWallpaper:]
+ -[CRSUIMutableWallpaperSceneSettings wallpaper]
+ -[CRSUIProxyApplicationSceneSettings frameRateLimit]
+ -[CRSUIPunchThroughController .cxx_destruct]
+ -[CRSUIPunchThroughController _handleConnectionActivated]
+ -[CRSUIPunchThroughController connection]
+ -[CRSUIPunchThroughController delegate]
+ -[CRSUIPunchThroughController initWithPunchThroughIdentifier:]
+ -[CRSUIPunchThroughController invalidate]
+ -[CRSUIPunchThroughController punchThroughIdentifier]
+ -[CRSUIPunchThroughController requestDismissalWithCompletion:]
+ -[CRSUIPunchThroughController requestPresentationWithCompletion:]
+ -[CRSUIPunchThroughController serverDismissedPunchThroughIdentifier:]
+ -[CRSUIPunchThroughController setConnection:]
+ -[CRSUIPunchThroughController setDelegate:]
+ -[CRSUIPunchThroughController setPunchThroughIdentifier:]
+ -[CRSUIPunchThroughService .cxx_destruct]
+ -[CRSUIPunchThroughService _connectionQueue_addConnection:]
+ -[CRSUIPunchThroughService _connectionQueue_removeConnection:]
+ -[CRSUIPunchThroughService clientRequestDismissalForPunchThroughIdentifier:completion:]
+ -[CRSUIPunchThroughService clientRequestPresentationForPunchThroughIdentifier:completion:]
+ -[CRSUIPunchThroughService connectionQueue]
+ -[CRSUIPunchThroughService connectionToPunchThroughIdentifierMap]
+ -[CRSUIPunchThroughService connections]
+ -[CRSUIPunchThroughService delegate]
+ -[CRSUIPunchThroughService initWithDelegate:]
+ -[CRSUIPunchThroughService invalidate]
+ -[CRSUIPunchThroughService listener:didReceiveConnection:withContext:]
+ -[CRSUIPunchThroughService listener:didReceiveConnection:withContext:].cold.1
+ -[CRSUIPunchThroughService listener]
+ -[CRSUIPunchThroughService punchThroughIdentifierDidDismiss:]
+ -[CRSUIPunchThroughService setConnectionQueue:]
+ -[CRSUIPunchThroughService setConnectionToPunchThroughIdentifierMap:]
+ -[CRSUIPunchThroughService setConnections:]
+ -[CRSUIPunchThroughService setDelegate:]
+ -[CRSUIPunchThroughService setListener:]
+ -[CRSUIResolvedWallpaper .cxx_destruct]
+ -[CRSUIResolvedWallpaper initWithWallpaperInformation:color:]
+ -[CRSUIResolvedWallpaper initWithWallpaperInformation:imageResolver:]
+ -[CRSUIResolvedWallpaper initWithWallpaperInformation:imageResolver:thumbnailResolver:]
+ -[CRSUIResolvedWallpaper initWithWallpaperInformation:imageResolver:thumbnailResolver:statefulPackage:color:]
+ -[CRSUIResolvedWallpaper initWithWallpaperInformation:statefulPackage:]
+ -[CRSUIResolvedWallpaper thumbnailWithCompatibleTraitCollection:]
+ -[CRSUIResolvedWallpaper view]
+ -[CRSUIResolvedWallpaper view].cold.1
+ -[CRSUIResolvedWallpaper wallpaper]
+ -[CRSUIStatefulCAPackage .cxx_destruct]
+ -[CRSUIStatefulCAPackage darkModeState]
+ -[CRSUIStatefulCAPackage hasDynamicState]
+ -[CRSUIStatefulCAPackage initWithPackage:lightModeState:darkModeState:]
+ -[CRSUIStatefulCAPackage initWithPackage:lightModeState:darkModeState:hasDynamicState:]
+ -[CRSUIStatefulCAPackage initWithPackage:state:]
+ -[CRSUIStatefulCAPackage lightModeState]
+ -[CRSUIStatefulCAPackage package]
+ -[CRSUIStatusBarStyleService addObserver:]
+ -[CRSUIStatusBarStyleService init]
+ -[CRSUIStatusBarStyleService observers]
+ -[CRSUIStatusBarStyleService removeObserver:]
+ -[CRSUIStatusBarStyleService setObservers:]
+ -[CRSUISystemWallpaper .cxx_destruct]
+ -[CRSUISystemWallpaper _imageURLWithCompatibleTraitCollection:]
+ -[CRSUISystemWallpaper _thumbnailImageURLWithCompatibleTraitCollection:]
+ -[CRSUISystemWallpaper color]
+ -[CRSUISystemWallpaper data]
+ -[CRSUISystemWallpaper description]
+ -[CRSUISystemWallpaper identifier]
+ -[CRSUISystemWallpaper initWithIdentifier:]
+ -[CRSUISystemWallpaper resolveWallpaper]
+ -[CRSUISystemWallpaper systemIdentifier]
+ -[CRSUISystemWallpaper thumbnailAssetCatalogName]
+ -[CRSUISystemWallpaper traits]
+ -[CRSUISystemWallpaper wallpaperAssetCatalogName]
+ -[CRSUISystemWallpaperProvider .cxx_destruct]
+ -[CRSUISystemWallpaperProvider dataProviderDelegate]
+ -[CRSUISystemWallpaperProvider defaultWallpapers]
+ -[CRSUISystemWallpaperProvider displayID]
+ -[CRSUISystemWallpaperProvider dynamicAppearanceWallpapersForVehicle:]
+ -[CRSUISystemWallpaperProvider dynamicAppearanceWallpapersForVehicle:].cold.1
+ -[CRSUISystemWallpaperProvider invalidate]
+ -[CRSUISystemWallpaperProvider isReady]
+ -[CRSUISystemWallpaperProvider loadWallpaperFromData:]
+ -[CRSUISystemWallpaperProvider loadWallpaperFromData:].cold.1
+ -[CRSUISystemWallpaperProvider resolveWallpaper:withCompletion:]
+ -[CRSUISystemWallpaperProvider resolveWallpaper:withCompletion:].cold.1
+ -[CRSUISystemWallpaperProvider setDataProviderDelegate:]
+ -[CRSUISystemWallpaperProvider wallpapers]
+ -[CRSUIWallpaperPreferences _hasGaugeClusterScreen]
+ -[CRSUIWallpaperPreferences dataProvider]
+ -[CRSUIWallpaperPreferences initWithDataProvider:]
+ -[CRSUIWallpaperPreferences setDataProvider:]
+ -[CRSUIWallpaperPreferences updateHasGaugeClusterScreen:]
+ -[CRSUIWallpaperPreferences updateThemeData:]
+ -[CRSUIWallpaperPreferences updateWallpaperToSupportDynamicAppearance]
+ -[CRSUIWallpaperPreferences updateWallpaperToSupportDynamicAppearance].cold.1
+ -[CRSUIWallpaperPreferences updateWallpaperToSupportDynamicAppearance].cold.2
+ -[CRSUIWallpaperPreferences wallpaperForLayoutIdentifier:]
+ -[CRSUIWallpaperPreferences wallpaperForLayoutIdentifier:].cold.1
+ -[CRSUIWallpaperSceneSettings wallpaper]
+ -[CRSUIWallpaperTraits description]
+ -[CRSUIWallpaperTraits encodeWithCoder:]
+ -[CRSUIWallpaperTraits hideRoundedCorners]
+ -[CRSUIWallpaperTraits iconLabelsRequireBackground]
+ -[CRSUIWallpaperTraits initWithCoder:]
+ -[CRSUIWallpaperTraits initWithSupportsDynamicAppearance:supportsDashboardPlatterMaterials:iconLabelsRequireBackground:hideRoundedCorners:black:]
+ -[CRSUIWallpaperTraits isBlack]
+ -[CRSUIWallpaperTraits supportsDashboardPlatterMaterials]
+ -[CRSUIWallpaperTraits supportsDynamicAppearance]
+ -[_CRSUIClusterThemeData .cxx_destruct]
+ -[_CRSUIClusterThemeData encodeWithBSXPCCoder:]
+ -[_CRSUIClusterThemeData initWithBSXPCCoder:]
+ -[_CRSUIClusterThemeData initWithThemeData:]
+ -[_CRSUIClusterThemeData themeData]
+ -[_CRSUIClusterThemeLayoutData .cxx_destruct]
+ -[_CRSUIClusterThemeLayoutData displays]
+ -[_CRSUIClusterThemeLayoutData encodeWithBSXPCCoder:]
+ -[_CRSUIClusterThemeLayoutData extraAssetsURL]
+ -[_CRSUIClusterThemeLayoutData initWithBSXPCCoder:]
+ -[_CRSUIClusterThemeLayoutData setDisplays:]
+ -[_CRSUIClusterThemeLayoutData setExtraAssetsURL:]
+ -[_CRSUIClusterThemeLayoutData setThemeData:]
+ -[_CRSUIClusterThemeLayoutData themeData]
+ GCC_except_table14
+ GCC_except_table3
+ _BSDispatchQueueCreateSerial
+ _CATransform3DMakeScale
+ _CRSUICAPackageViewWithStatefulPackage
+ _CRSUICarPlayTestAppSetUISyncDisabled
+ _CRSUIImageViewWithResolver
+ _NSLocalizedDescriptionKey
+ _NSStringFromClass
+ _OBJC_CLASS_$_CAPackage
+ _OBJC_CLASS_$_CAStateController
+ _OBJC_CLASS_$_CRAssetWallpaperData
+ _OBJC_CLASS_$_CRDisplayThemeData
+ _OBJC_CLASS_$_CRSUIAssetWallpaper
+ _OBJC_CLASS_$_CRSUICAPackageView
+ _OBJC_CLASS_$_CRSUIClimatePopoverAction
+ _OBJC_CLASS_$_CRSUIClimatePopoverBSActionsHandler
+ _OBJC_CLASS_$_CRSUIClusterPressAction
+ _OBJC_CLASS_$_CRSUIClusterPressBSActionsHandler
+ _OBJC_CLASS_$_CRSUIClusterThemeCAPackageAsset
+ _OBJC_CLASS_$_CRSUIClusterThemeCAPackageWallpaper
+ _OBJC_CLASS_$_CRSUIClusterThemeColorWallpaper
+ _OBJC_CLASS_$_CRSUIClusterThemeDisplay
+ _OBJC_CLASS_$_CRSUIClusterThemeImageAsset
+ _OBJC_CLASS_$_CRSUIClusterThemeImageWallpaper
+ _OBJC_CLASS_$_CRSUIClusterThemeLayout
+ _OBJC_CLASS_$_CRSUIClusterThemeLayoutPreview
+ _OBJC_CLASS_$_CRSUIClusterThemeManager
+ _OBJC_CLASS_$_CRSUIClusterThemePalette
+ _OBJC_CLASS_$_CRSUIClusterThemeService
+ _OBJC_CLASS_$_CRSUIClusterThemeSpecification
+ _OBJC_CLASS_$_CRSUIClusterThemeWallpaper
+ _OBJC_CLASS_$_CRSUIPunchThroughController
+ _OBJC_CLASS_$_CRSUIPunchThroughService
+ _OBJC_CLASS_$_CRSUIPunchThroughSpecification
+ _OBJC_CLASS_$_CRSUIResolvedWallpaper
+ _OBJC_CLASS_$_CRSUIStatefulCAPackage
+ _OBJC_CLASS_$_CRSUISystemWallpaper
+ _OBJC_CLASS_$_CRSUISystemWallpaperProvider
+ _OBJC_CLASS_$_CRSUIWallpaperTraits
+ _OBJC_CLASS_$_CRSystemWallpaperData
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSMapTable
+ _OBJC_CLASS_$_NSSecurityScopedURLWrapper
+ _OBJC_CLASS_$_UIImageAsset
+ _OBJC_CLASS_$_UIImageView
+ _OBJC_CLASS_$_UITraitUserInterfaceStyle
+ _OBJC_CLASS_$__CRSUIClusterThemeData
+ _OBJC_CLASS_$__CRSUIClusterThemeLayoutData
+ _OBJC_IVAR_$_CRSUIAssetWallpaper._displayID
+ _OBJC_IVAR_$_CRSUIAssetWallpaper._layoutID
+ _OBJC_IVAR_$_CRSUIAssetWallpaper._traits
+ _OBJC_IVAR_$_CRSUIAssetWallpaper._wallpaperIdentifier
+ _OBJC_IVAR_$_CRSUICAPackageView._dynamicStateProvider
+ _OBJC_IVAR_$_CRSUICAPackageView._package
+ _OBJC_IVAR_$_CRSUICAPackageView._packageSize
+ _OBJC_IVAR_$_CRSUICAPackageView._rootLayer
+ _OBJC_IVAR_$_CRSUICAPackageView._state
+ _OBJC_IVAR_$_CRSUICAPackageView._stateController
+ _OBJC_IVAR_$_CRSUIClimatePopoverBSActionsHandler._delegate
+ _OBJC_IVAR_$_CRSUIClusterPressBSActionsHandler._delegate
+ _OBJC_IVAR_$_CRSUIClusterThemeCAPackageAsset._identifier
+ _OBJC_IVAR_$_CRSUIClusterThemeCAPackageAsset._packageType
+ _OBJC_IVAR_$_CRSUIClusterThemeCAPackageAsset._url
+ _OBJC_IVAR_$_CRSUIClusterThemeCAPackageWallpaper._asset
+ _OBJC_IVAR_$_CRSUIClusterThemeCAPackageWallpaper._darkModeState
+ _OBJC_IVAR_$_CRSUIClusterThemeCAPackageWallpaper._lightModeState
+ _OBJC_IVAR_$_CRSUIClusterThemeCAPackageWallpaper._supportsDynamicAppearance
+ _OBJC_IVAR_$_CRSUIClusterThemeCAPackageWallpaper._type
+ _OBJC_IVAR_$_CRSUIClusterThemeColorWallpaper._darkModeColor
+ _OBJC_IVAR_$_CRSUIClusterThemeColorWallpaper._lightModeColor
+ _OBJC_IVAR_$_CRSUIClusterThemeDisplay._displayType
+ _OBJC_IVAR_$_CRSUIClusterThemeDisplay._identifier
+ _OBJC_IVAR_$_CRSUIClusterThemeDisplay._layouts
+ _OBJC_IVAR_$_CRSUIClusterThemeDisplay._size
+ _OBJC_IVAR_$_CRSUIClusterThemeImageAsset._identifier
+ _OBJC_IVAR_$_CRSUIClusterThemeImageAsset._url
+ _OBJC_IVAR_$_CRSUIClusterThemeImageWallpaper._darkModeAsset
+ _OBJC_IVAR_$_CRSUIClusterThemeImageWallpaper._lightModeAsset
+ _OBJC_IVAR_$_CRSUIClusterThemeImageWallpaper._supportsDynamicAppearance
+ _OBJC_IVAR_$_CRSUIClusterThemeLayout._displayName
+ _OBJC_IVAR_$_CRSUIClusterThemeLayout._identifier
+ _OBJC_IVAR_$_CRSUIClusterThemeLayout._palettes
+ _OBJC_IVAR_$_CRSUIClusterThemeLayout._preview
+ _OBJC_IVAR_$_CRSUIClusterThemeLayout._wallpapers
+ _OBJC_IVAR_$_CRSUIClusterThemeLayoutPreview._asset
+ _OBJC_IVAR_$_CRSUIClusterThemeLayoutPreview._darkModeStateForPaletteID
+ _OBJC_IVAR_$_CRSUIClusterThemeLayoutPreview._lightModeStateForPaletteID
+ _OBJC_IVAR_$_CRSUIClusterThemeLayoutPreview._supportsDynamicAppearance
+ _OBJC_IVAR_$_CRSUIClusterThemeManager._connection
+ _OBJC_IVAR_$_CRSUIClusterThemeManager._connectionQueue
+ _OBJC_IVAR_$_CRSUIClusterThemeManager._dataProviderDelegate
+ _OBJC_IVAR_$_CRSUIClusterThemeManager._delegate
+ _OBJC_IVAR_$_CRSUIClusterThemeManager._displays
+ _OBJC_IVAR_$_CRSUIClusterThemeManager._extraAssetsURL
+ _OBJC_IVAR_$_CRSUIClusterThemeManager._lock
+ _OBJC_IVAR_$_CRSUIClusterThemeManager._lock_connectionActivated
+ _OBJC_IVAR_$_CRSUIClusterThemeManager._lock_invalidated
+ _OBJC_IVAR_$_CRSUIClusterThemeManager._themeData
+ _OBJC_IVAR_$_CRSUIClusterThemePalette._colorScheme
+ _OBJC_IVAR_$_CRSUIClusterThemePalette._colors
+ _OBJC_IVAR_$_CRSUIClusterThemePalette._displayName
+ _OBJC_IVAR_$_CRSUIClusterThemePalette._identifier
+ _OBJC_IVAR_$_CRSUIClusterThemePalette._sortIndex
+ _OBJC_IVAR_$_CRSUIClusterThemeService._connectionQueue
+ _OBJC_IVAR_$_CRSUIClusterThemeService._connections
+ _OBJC_IVAR_$_CRSUIClusterThemeService._delegate
+ _OBJC_IVAR_$_CRSUIClusterThemeService._listener
+ _OBJC_IVAR_$_CRSUIClusterThemeService._themeDataProvider
+ _OBJC_IVAR_$_CRSUIClusterThemeWallpaper._associatedPaletteID
+ _OBJC_IVAR_$_CRSUIClusterThemeWallpaper._color
+ _OBJC_IVAR_$_CRSUIClusterThemeWallpaper._data
+ _OBJC_IVAR_$_CRSUIClusterThemeWallpaper._displayName
+ _OBJC_IVAR_$_CRSUIClusterThemeWallpaper._identifier
+ _OBJC_IVAR_$_CRSUIClusterThemeWallpaper._image
+ _OBJC_IVAR_$_CRSUIClusterThemeWallpaper._isDefault
+ _OBJC_IVAR_$_CRSUIClusterThemeWallpaper._package
+ _OBJC_IVAR_$_CRSUIClusterThemeWallpaper._traits
+ _OBJC_IVAR_$_CRSUIMutableWallpaperSceneSettings._wallpaper
+ _OBJC_IVAR_$_CRSUIPunchThroughController._connection
+ _OBJC_IVAR_$_CRSUIPunchThroughController._delegate
+ _OBJC_IVAR_$_CRSUIPunchThroughController._lock
+ _OBJC_IVAR_$_CRSUIPunchThroughController._lock_connectionActivated
+ _OBJC_IVAR_$_CRSUIPunchThroughController._lock_hasPendingPresentationRequest
+ _OBJC_IVAR_$_CRSUIPunchThroughController._lock_invalidated
+ _OBJC_IVAR_$_CRSUIPunchThroughController._lock_pendingPresentationCompletion
+ _OBJC_IVAR_$_CRSUIPunchThroughController._lock_presented
+ _OBJC_IVAR_$_CRSUIPunchThroughController._punchThroughIdentifier
+ _OBJC_IVAR_$_CRSUIPunchThroughService._connectionQueue
+ _OBJC_IVAR_$_CRSUIPunchThroughService._connectionToPunchThroughIdentifierMap
+ _OBJC_IVAR_$_CRSUIPunchThroughService._connections
+ _OBJC_IVAR_$_CRSUIPunchThroughService._delegate
+ _OBJC_IVAR_$_CRSUIPunchThroughService._listener
+ _OBJC_IVAR_$_CRSUIPunchThroughService._lock
+ _OBJC_IVAR_$_CRSUIResolvedWallpaper._color
+ _OBJC_IVAR_$_CRSUIResolvedWallpaper._imageResolver
+ _OBJC_IVAR_$_CRSUIResolvedWallpaper._statefulPackage
+ _OBJC_IVAR_$_CRSUIResolvedWallpaper._thumbnailResolver
+ _OBJC_IVAR_$_CRSUIResolvedWallpaper._wallpaper
+ _OBJC_IVAR_$_CRSUIStatefulCAPackage._darkModeState
+ _OBJC_IVAR_$_CRSUIStatefulCAPackage._hasDynamicState
+ _OBJC_IVAR_$_CRSUIStatefulCAPackage._lightModeState
+ _OBJC_IVAR_$_CRSUIStatefulCAPackage._package
+ _OBJC_IVAR_$_CRSUIStatusBarStyleService._observers
+ _OBJC_IVAR_$_CRSUISystemWallpaper._systemIdentifier
+ _OBJC_IVAR_$_CRSUISystemWallpaper._thumbnailAssetCatalogName
+ _OBJC_IVAR_$_CRSUISystemWallpaper._traits
+ _OBJC_IVAR_$_CRSUISystemWallpaper._wallpaperAssetCatalogName
+ _OBJC_IVAR_$_CRSUISystemWallpaper.identifier
+ _OBJC_IVAR_$_CRSUISystemWallpaperProvider.dataProviderDelegate
+ _OBJC_IVAR_$_CRSUIWallpaperPreferences._dataProvider
+ _OBJC_IVAR_$_CRSUIWallpaperTraits._black
+ _OBJC_IVAR_$_CRSUIWallpaperTraits._hideRoundedCorners
+ _OBJC_IVAR_$_CRSUIWallpaperTraits._iconLabelsRequireBackground
+ _OBJC_IVAR_$_CRSUIWallpaperTraits._supportsDashboardPlatterMaterials
+ _OBJC_IVAR_$_CRSUIWallpaperTraits._supportsDynamicAppearance
+ _OBJC_IVAR_$__CRSUIClusterThemeData._themeData
+ _OBJC_IVAR_$__CRSUIClusterThemeLayoutData._displays
+ _OBJC_IVAR_$__CRSUIClusterThemeLayoutData._extraAssetsURL
+ _OBJC_IVAR_$__CRSUIClusterThemeLayoutData._themeData
+ _OBJC_METACLASS_$_CRSUIAssetWallpaper
+ _OBJC_METACLASS_$_CRSUICAPackageView
+ _OBJC_METACLASS_$_CRSUIClimatePopoverAction
+ _OBJC_METACLASS_$_CRSUIClimatePopoverBSActionsHandler
+ _OBJC_METACLASS_$_CRSUIClusterPressAction
+ _OBJC_METACLASS_$_CRSUIClusterPressBSActionsHandler
+ _OBJC_METACLASS_$_CRSUIClusterThemeCAPackageAsset
+ _OBJC_METACLASS_$_CRSUIClusterThemeCAPackageWallpaper
+ _OBJC_METACLASS_$_CRSUIClusterThemeColorWallpaper
+ _OBJC_METACLASS_$_CRSUIClusterThemeDisplay
+ _OBJC_METACLASS_$_CRSUIClusterThemeImageAsset
+ _OBJC_METACLASS_$_CRSUIClusterThemeImageWallpaper
+ _OBJC_METACLASS_$_CRSUIClusterThemeLayout
+ _OBJC_METACLASS_$_CRSUIClusterThemeLayoutPreview
+ _OBJC_METACLASS_$_CRSUIClusterThemeManager
+ _OBJC_METACLASS_$_CRSUIClusterThemePalette
+ _OBJC_METACLASS_$_CRSUIClusterThemeService
+ _OBJC_METACLASS_$_CRSUIClusterThemeSpecification
+ _OBJC_METACLASS_$_CRSUIClusterThemeWallpaper
+ _OBJC_METACLASS_$_CRSUIPunchThroughController
+ _OBJC_METACLASS_$_CRSUIPunchThroughService
+ _OBJC_METACLASS_$_CRSUIPunchThroughSpecification
+ _OBJC_METACLASS_$_CRSUIResolvedWallpaper
+ _OBJC_METACLASS_$_CRSUIStatefulCAPackage
+ _OBJC_METACLASS_$_CRSUISystemWallpaper
+ _OBJC_METACLASS_$_CRSUISystemWallpaperProvider
+ _OBJC_METACLASS_$_CRSUIWallpaperTraits
+ _OBJC_METACLASS_$_UIView
+ _OBJC_METACLASS_$__CRSUIClusterThemeData
+ _OBJC_METACLASS_$__CRSUIClusterThemeLayoutData
+ _OUTLINED_FUNCTION_1
+ __OBJC_$_CLASS_METHODS_CRSUIClusterThemeCAPackageAsset
+ __OBJC_$_CLASS_METHODS_CRSUIClusterThemeCAPackageWallpaper
+ __OBJC_$_CLASS_METHODS_CRSUIClusterThemeColorWallpaper
+ __OBJC_$_CLASS_METHODS_CRSUIClusterThemeDisplay
+ __OBJC_$_CLASS_METHODS_CRSUIClusterThemeImageAsset
+ __OBJC_$_CLASS_METHODS_CRSUIClusterThemeImageWallpaper
+ __OBJC_$_CLASS_METHODS_CRSUIClusterThemeLayout
+ __OBJC_$_CLASS_METHODS_CRSUIClusterThemeLayoutPreview
+ __OBJC_$_CLASS_METHODS_CRSUIClusterThemePalette
+ __OBJC_$_CLASS_METHODS_CRSUIClusterThemeSpecification
+ __OBJC_$_CLASS_METHODS_CRSUIClusterThemeWallpaper
+ __OBJC_$_CLASS_METHODS_CRSUIPunchThroughSpecification
+ __OBJC_$_CLASS_METHODS_CRSUISystemWallpaper
+ __OBJC_$_CLASS_METHODS_CRSUIWallpaperTraits
+ __OBJC_$_CLASS_METHODS__CRSUIClusterThemeData
+ __OBJC_$_CLASS_METHODS__CRSUIClusterThemeLayoutData
+ __OBJC_$_CLASS_PROP_LIST_CRSUIClusterThemeSpecification
+ __OBJC_$_CLASS_PROP_LIST_CRSUIPunchThroughSpecification
+ __OBJC_$_CLASS_PROP_LIST_CRSUIWallpaperTraits
+ __OBJC_$_INSTANCE_METHODS_CRSUIAssetWallpaper
+ __OBJC_$_INSTANCE_METHODS_CRSUICAPackageView
+ __OBJC_$_INSTANCE_METHODS_CRSUIClimatePopoverAction
+ __OBJC_$_INSTANCE_METHODS_CRSUIClimatePopoverBSActionsHandler
+ __OBJC_$_INSTANCE_METHODS_CRSUIClusterPressAction
+ __OBJC_$_INSTANCE_METHODS_CRSUIClusterPressBSActionsHandler
+ __OBJC_$_INSTANCE_METHODS_CRSUIClusterThemeCAPackageAsset
+ __OBJC_$_INSTANCE_METHODS_CRSUIClusterThemeCAPackageWallpaper
+ __OBJC_$_INSTANCE_METHODS_CRSUIClusterThemeColorWallpaper
+ __OBJC_$_INSTANCE_METHODS_CRSUIClusterThemeDisplay
+ __OBJC_$_INSTANCE_METHODS_CRSUIClusterThemeImageAsset
+ __OBJC_$_INSTANCE_METHODS_CRSUIClusterThemeImageWallpaper
+ __OBJC_$_INSTANCE_METHODS_CRSUIClusterThemeLayout
+ __OBJC_$_INSTANCE_METHODS_CRSUIClusterThemeLayoutPreview
+ __OBJC_$_INSTANCE_METHODS_CRSUIClusterThemeManager
+ __OBJC_$_INSTANCE_METHODS_CRSUIClusterThemePalette
+ __OBJC_$_INSTANCE_METHODS_CRSUIClusterThemeService
+ __OBJC_$_INSTANCE_METHODS_CRSUIClusterThemeWallpaper
+ __OBJC_$_INSTANCE_METHODS_CRSUIPunchThroughController
+ __OBJC_$_INSTANCE_METHODS_CRSUIPunchThroughService
+ __OBJC_$_INSTANCE_METHODS_CRSUIResolvedWallpaper
+ __OBJC_$_INSTANCE_METHODS_CRSUIStatefulCAPackage
+ __OBJC_$_INSTANCE_METHODS_CRSUISystemWallpaper
+ __OBJC_$_INSTANCE_METHODS_CRSUISystemWallpaperProvider
+ __OBJC_$_INSTANCE_METHODS_CRSUIWallpaperTraits
+ __OBJC_$_INSTANCE_METHODS__CRSUIClusterThemeData
+ __OBJC_$_INSTANCE_METHODS__CRSUIClusterThemeLayoutData
+ __OBJC_$_INSTANCE_VARIABLES_CRSUIAssetWallpaper
+ __OBJC_$_INSTANCE_VARIABLES_CRSUICAPackageView
+ __OBJC_$_INSTANCE_VARIABLES_CRSUIClimatePopoverBSActionsHandler
+ __OBJC_$_INSTANCE_VARIABLES_CRSUIClusterPressBSActionsHandler
+ __OBJC_$_INSTANCE_VARIABLES_CRSUIClusterThemeCAPackageAsset
+ __OBJC_$_INSTANCE_VARIABLES_CRSUIClusterThemeCAPackageWallpaper
+ __OBJC_$_INSTANCE_VARIABLES_CRSUIClusterThemeColorWallpaper
+ __OBJC_$_INSTANCE_VARIABLES_CRSUIClusterThemeDisplay
+ __OBJC_$_INSTANCE_VARIABLES_CRSUIClusterThemeImageAsset
+ __OBJC_$_INSTANCE_VARIABLES_CRSUIClusterThemeImageWallpaper
+ __OBJC_$_INSTANCE_VARIABLES_CRSUIClusterThemeLayout
+ __OBJC_$_INSTANCE_VARIABLES_CRSUIClusterThemeLayoutPreview
+ __OBJC_$_INSTANCE_VARIABLES_CRSUIClusterThemeManager
+ __OBJC_$_INSTANCE_VARIABLES_CRSUIClusterThemePalette
+ __OBJC_$_INSTANCE_VARIABLES_CRSUIClusterThemeService
+ __OBJC_$_INSTANCE_VARIABLES_CRSUIClusterThemeWallpaper
+ __OBJC_$_INSTANCE_VARIABLES_CRSUIMutableWallpaperSceneSettings
+ __OBJC_$_INSTANCE_VARIABLES_CRSUIPunchThroughController
+ __OBJC_$_INSTANCE_VARIABLES_CRSUIPunchThroughService
+ __OBJC_$_INSTANCE_VARIABLES_CRSUIResolvedWallpaper
+ __OBJC_$_INSTANCE_VARIABLES_CRSUIStatefulCAPackage
+ __OBJC_$_INSTANCE_VARIABLES_CRSUISystemWallpaper
+ __OBJC_$_INSTANCE_VARIABLES_CRSUISystemWallpaperProvider
+ __OBJC_$_INSTANCE_VARIABLES_CRSUIWallpaperTraits
+ __OBJC_$_INSTANCE_VARIABLES__CRSUIClusterThemeData
+ __OBJC_$_INSTANCE_VARIABLES__CRSUIClusterThemeLayoutData
+ __OBJC_$_PROP_LIST_CRSUIApplicationSceneSettings.57
+ __OBJC_$_PROP_LIST_CRSUIAssetWallpaper
+ __OBJC_$_PROP_LIST_CRSUICAPackageView
+ __OBJC_$_PROP_LIST_CRSUIClimatePopoverBSActionsHandler
+ __OBJC_$_PROP_LIST_CRSUIClusterPressBSActionsHandler
+ __OBJC_$_PROP_LIST_CRSUIClusterThemeAsset
+ __OBJC_$_PROP_LIST_CRSUIClusterThemeCAPackageAsset
+ __OBJC_$_PROP_LIST_CRSUIClusterThemeCAPackageWallpaper
+ __OBJC_$_PROP_LIST_CRSUIClusterThemeColorWallpaper
+ __OBJC_$_PROP_LIST_CRSUIClusterThemeDisplay
+ __OBJC_$_PROP_LIST_CRSUIClusterThemeImageAsset
+ __OBJC_$_PROP_LIST_CRSUIClusterThemeImageWallpaper
+ __OBJC_$_PROP_LIST_CRSUIClusterThemeLayout
+ __OBJC_$_PROP_LIST_CRSUIClusterThemeLayoutPreview
+ __OBJC_$_PROP_LIST_CRSUIClusterThemeManager
+ __OBJC_$_PROP_LIST_CRSUIClusterThemePalette
+ __OBJC_$_PROP_LIST_CRSUIClusterThemeService
+ __OBJC_$_PROP_LIST_CRSUIClusterThemeWallpaper
+ __OBJC_$_PROP_LIST_CRSUIDashboardWidgetSceneSettings.60
+ __OBJC_$_PROP_LIST_CRSUIFrameRateLimitProviding
+ __OBJC_$_PROP_LIST_CRSUIInstrumentClusterSceneSettings.70
+ __OBJC_$_PROP_LIST_CRSUIMutableFrameRateLimitProviding
+ __OBJC_$_PROP_LIST_CRSUIProxyApplicationSceneSettings.55
+ __OBJC_$_PROP_LIST_CRSUIPunchThroughController
+ __OBJC_$_PROP_LIST_CRSUIPunchThroughService
+ __OBJC_$_PROP_LIST_CRSUIResolvedWallpaper
+ __OBJC_$_PROP_LIST_CRSUIStatefulCAPackage
+ __OBJC_$_PROP_LIST_CRSUISystemWallpaper
+ __OBJC_$_PROP_LIST_CRSUISystemWallpaperProvider
+ __OBJC_$_PROP_LIST_CRSUITemplateDashboardWidgetSceneSettings.89
+ __OBJC_$_PROP_LIST_CRSUITemplateInstrumentClusterSceneSettings.107
+ __OBJC_$_PROP_LIST_CRSUIWallpaperDataProviding
+ __OBJC_$_PROP_LIST_CRSUIWallpaperTraits
+ __OBJC_$_PROP_LIST__CRSUIClusterThemeData
+ __OBJC_$_PROP_LIST__CRSUIClusterThemeLayoutData
+ __OBJC_$_PROTOCOL_CLASS_METHODS_BSXPCSecureCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BSXPCSecureCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CRSUIClimatePopoverActionDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CRSUIClusterThemeAsset
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CRSUIClusterThemeClientToServerInterface
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CRSUIClusterThemeServerToClientInterface
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CRSUIFrameRateLimitProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CRSUIMutableFrameRateLimitProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CRSUIPunchThroughClientToServerInterface
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CRSUIPunchThroughServerToClientInterface
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CRSUIStatusBarStyleServiceObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CRSUIWallpaper
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CRSUIWallpaperDataProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BSXPCSecureCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CRSUIClimatePopoverActionDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CRSUIClusterThemeAsset
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CRSUIClusterThemeClientToServerInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CRSUIClusterThemeServerToClientInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CRSUIFrameRateLimitProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CRSUIMutableFrameRateLimitProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CRSUIPunchThroughClientToServerInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CRSUIPunchThroughServerToClientInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CRSUIStatusBarStyleServiceObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CRSUIWallpaper
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CRSUIWallpaperDataProviding
+ __OBJC_$_PROTOCOL_REFS_BSXPCSecureCoding
+ __OBJC_$_PROTOCOL_REFS_CRSUIClimatePopoverActionDelegate
+ __OBJC_$_PROTOCOL_REFS_CRSUIClusterThemeAsset
+ __OBJC_$_PROTOCOL_REFS_CRSUIClusterThemeClientToServerInterface
+ __OBJC_$_PROTOCOL_REFS_CRSUIClusterThemeServerToClientInterface
+ __OBJC_$_PROTOCOL_REFS_CRSUIFrameRateLimitProviding
+ __OBJC_$_PROTOCOL_REFS_CRSUIMutableFrameRateLimitProviding
+ __OBJC_$_PROTOCOL_REFS_CRSUIPunchThroughClientToServerInterface
+ __OBJC_$_PROTOCOL_REFS_CRSUIPunchThroughServerToClientInterface
+ __OBJC_$_PROTOCOL_REFS_CRSUIStatusBarStyleServiceObserver
+ __OBJC_$_PROTOCOL_REFS_CRSUIWallpaper
+ __OBJC_$_PROTOCOL_REFS_CRSUIWallpaperDataProviding
+ __OBJC_CLASS_PROTOCOLS_$_CRSUIAssetWallpaper
+ __OBJC_CLASS_PROTOCOLS_$_CRSUIClimatePopoverBSActionsHandler
+ __OBJC_CLASS_PROTOCOLS_$_CRSUIClusterPressBSActionsHandler
+ __OBJC_CLASS_PROTOCOLS_$_CRSUIClusterThemeCAPackageAsset
+ __OBJC_CLASS_PROTOCOLS_$_CRSUIClusterThemeCAPackageWallpaper
+ __OBJC_CLASS_PROTOCOLS_$_CRSUIClusterThemeColorWallpaper
+ __OBJC_CLASS_PROTOCOLS_$_CRSUIClusterThemeDisplay
+ __OBJC_CLASS_PROTOCOLS_$_CRSUIClusterThemeImageAsset
+ __OBJC_CLASS_PROTOCOLS_$_CRSUIClusterThemeImageWallpaper
+ __OBJC_CLASS_PROTOCOLS_$_CRSUIClusterThemeLayout
+ __OBJC_CLASS_PROTOCOLS_$_CRSUIClusterThemeLayoutPreview
+ __OBJC_CLASS_PROTOCOLS_$_CRSUIClusterThemeManager
+ __OBJC_CLASS_PROTOCOLS_$_CRSUIClusterThemePalette
+ __OBJC_CLASS_PROTOCOLS_$_CRSUIClusterThemeService
+ __OBJC_CLASS_PROTOCOLS_$_CRSUIClusterThemeWallpaper
+ __OBJC_CLASS_PROTOCOLS_$_CRSUIPunchThroughController
+ __OBJC_CLASS_PROTOCOLS_$_CRSUIPunchThroughService
+ __OBJC_CLASS_PROTOCOLS_$_CRSUISystemWallpaper
+ __OBJC_CLASS_PROTOCOLS_$_CRSUISystemWallpaperProvider
+ __OBJC_CLASS_PROTOCOLS_$_CRSUIWallpaperTraits
+ __OBJC_CLASS_PROTOCOLS_$__CRSUIClusterThemeData
+ __OBJC_CLASS_PROTOCOLS_$__CRSUIClusterThemeLayoutData
+ __OBJC_CLASS_RO_$_CRSUIAssetWallpaper
+ __OBJC_CLASS_RO_$_CRSUICAPackageView
+ __OBJC_CLASS_RO_$_CRSUIClimatePopoverAction
+ __OBJC_CLASS_RO_$_CRSUIClimatePopoverBSActionsHandler
+ __OBJC_CLASS_RO_$_CRSUIClusterPressAction
+ __OBJC_CLASS_RO_$_CRSUIClusterPressBSActionsHandler
+ __OBJC_CLASS_RO_$_CRSUIClusterThemeCAPackageAsset
+ __OBJC_CLASS_RO_$_CRSUIClusterThemeCAPackageWallpaper
+ __OBJC_CLASS_RO_$_CRSUIClusterThemeColorWallpaper
+ __OBJC_CLASS_RO_$_CRSUIClusterThemeDisplay
+ __OBJC_CLASS_RO_$_CRSUIClusterThemeImageAsset
+ __OBJC_CLASS_RO_$_CRSUIClusterThemeImageWallpaper
+ __OBJC_CLASS_RO_$_CRSUIClusterThemeLayout
+ __OBJC_CLASS_RO_$_CRSUIClusterThemeLayoutPreview
+ __OBJC_CLASS_RO_$_CRSUIClusterThemeManager
+ __OBJC_CLASS_RO_$_CRSUIClusterThemePalette
+ __OBJC_CLASS_RO_$_CRSUIClusterThemeService
+ __OBJC_CLASS_RO_$_CRSUIClusterThemeSpecification
+ __OBJC_CLASS_RO_$_CRSUIClusterThemeWallpaper
+ __OBJC_CLASS_RO_$_CRSUIPunchThroughController
+ __OBJC_CLASS_RO_$_CRSUIPunchThroughService
+ __OBJC_CLASS_RO_$_CRSUIPunchThroughSpecification
+ __OBJC_CLASS_RO_$_CRSUIResolvedWallpaper
+ __OBJC_CLASS_RO_$_CRSUIStatefulCAPackage
+ __OBJC_CLASS_RO_$_CRSUISystemWallpaper
+ __OBJC_CLASS_RO_$_CRSUISystemWallpaperProvider
+ __OBJC_CLASS_RO_$_CRSUIWallpaperTraits
+ __OBJC_CLASS_RO_$__CRSUIClusterThemeData
+ __OBJC_CLASS_RO_$__CRSUIClusterThemeLayoutData
+ __OBJC_LABEL_PROTOCOL_$_BSXPCSecureCoding
+ __OBJC_LABEL_PROTOCOL_$_CRSUIClimatePopoverActionDelegate
+ __OBJC_LABEL_PROTOCOL_$_CRSUIClusterThemeAsset
+ __OBJC_LABEL_PROTOCOL_$_CRSUIClusterThemeClientToServerInterface
+ __OBJC_LABEL_PROTOCOL_$_CRSUIClusterThemeServerToClientInterface
+ __OBJC_LABEL_PROTOCOL_$_CRSUIFrameRateLimitProviding
+ __OBJC_LABEL_PROTOCOL_$_CRSUIMutableFrameRateLimitProviding
+ __OBJC_LABEL_PROTOCOL_$_CRSUIPunchThroughClientToServerInterface
+ __OBJC_LABEL_PROTOCOL_$_CRSUIPunchThroughServerToClientInterface
+ __OBJC_LABEL_PROTOCOL_$_CRSUIStatusBarStyleServiceObserver
+ __OBJC_LABEL_PROTOCOL_$_CRSUIWallpaper
+ __OBJC_LABEL_PROTOCOL_$_CRSUIWallpaperDataProviding
+ __OBJC_METACLASS_RO_$_CRSUIAssetWallpaper
+ __OBJC_METACLASS_RO_$_CRSUICAPackageView
+ __OBJC_METACLASS_RO_$_CRSUIClimatePopoverAction
+ __OBJC_METACLASS_RO_$_CRSUIClimatePopoverBSActionsHandler
+ __OBJC_METACLASS_RO_$_CRSUIClusterPressAction
+ __OBJC_METACLASS_RO_$_CRSUIClusterPressBSActionsHandler
+ __OBJC_METACLASS_RO_$_CRSUIClusterThemeCAPackageAsset
+ __OBJC_METACLASS_RO_$_CRSUIClusterThemeCAPackageWallpaper
+ __OBJC_METACLASS_RO_$_CRSUIClusterThemeColorWallpaper
+ __OBJC_METACLASS_RO_$_CRSUIClusterThemeDisplay
+ __OBJC_METACLASS_RO_$_CRSUIClusterThemeImageAsset
+ __OBJC_METACLASS_RO_$_CRSUIClusterThemeImageWallpaper
+ __OBJC_METACLASS_RO_$_CRSUIClusterThemeLayout
+ __OBJC_METACLASS_RO_$_CRSUIClusterThemeLayoutPreview
+ __OBJC_METACLASS_RO_$_CRSUIClusterThemeManager
+ __OBJC_METACLASS_RO_$_CRSUIClusterThemePalette
+ __OBJC_METACLASS_RO_$_CRSUIClusterThemeService
+ __OBJC_METACLASS_RO_$_CRSUIClusterThemeSpecification
+ __OBJC_METACLASS_RO_$_CRSUIClusterThemeWallpaper
+ __OBJC_METACLASS_RO_$_CRSUIPunchThroughController
+ __OBJC_METACLASS_RO_$_CRSUIPunchThroughService
+ __OBJC_METACLASS_RO_$_CRSUIPunchThroughSpecification
+ __OBJC_METACLASS_RO_$_CRSUIResolvedWallpaper
+ __OBJC_METACLASS_RO_$_CRSUIStatefulCAPackage
+ __OBJC_METACLASS_RO_$_CRSUISystemWallpaper
+ __OBJC_METACLASS_RO_$_CRSUISystemWallpaperProvider
+ __OBJC_METACLASS_RO_$_CRSUIWallpaperTraits
+ __OBJC_METACLASS_RO_$__CRSUIClusterThemeData
+ __OBJC_METACLASS_RO_$__CRSUIClusterThemeLayoutData
+ __OBJC_PROTOCOL_$_BSXPCSecureCoding
+ __OBJC_PROTOCOL_$_CRSUIClimatePopoverActionDelegate
+ __OBJC_PROTOCOL_$_CRSUIClusterThemeAsset
+ __OBJC_PROTOCOL_$_CRSUIClusterThemeClientToServerInterface
+ __OBJC_PROTOCOL_$_CRSUIClusterThemeServerToClientInterface
+ __OBJC_PROTOCOL_$_CRSUIFrameRateLimitProviding
+ __OBJC_PROTOCOL_$_CRSUIMutableFrameRateLimitProviding
+ __OBJC_PROTOCOL_$_CRSUIPunchThroughClientToServerInterface
+ __OBJC_PROTOCOL_$_CRSUIPunchThroughServerToClientInterface
+ __OBJC_PROTOCOL_$_CRSUIStatusBarStyleServiceObserver
+ __OBJC_PROTOCOL_$_CRSUIWallpaper
+ __OBJC_PROTOCOL_$_CRSUIWallpaperDataProviding
+ __OBJC_PROTOCOL_REFERENCE_$_CRSUIClimatePopoverActionDelegate
+ __OBJC_PROTOCOL_REFERENCE_$_CRSUIClusterThemeClientToServerInterface
+ __OBJC_PROTOCOL_REFERENCE_$_CRSUIClusterThemeServerToClientInterface
+ __OBJC_PROTOCOL_REFERENCE_$_CRSUIPunchThroughClientToServerInterface
+ __OBJC_PROTOCOL_REFERENCE_$_CRSUIPunchThroughServerToClientInterface
+ __OBJC_PROTOCOL_REFERENCE_$_CRSUIStatusBarStyleServiceObserver
+ ___101-[CRSUIClimatePopoverBSActionsHandler _respondToActions:forFBSScene:inUIScene:fromTransitionContext:]_block_invoke
+ ___101-[CRSUIClimatePopoverBSActionsHandler _respondToActions:forFBSScene:inUIScene:fromTransitionContext:]_block_invoke_2
+ ___101-[CRSUIClimatePopoverBSActionsHandler _respondToActions:forFBSScene:inUIScene:fromTransitionContext:]_block_invoke_3
+ ___29-[CRSUISystemWallpaper color]_block_invoke
+ ___32-[CRSUIClusterThemeManager init]_block_invoke
+ ___32-[CRSUIClusterThemeManager init]_block_invoke.17
+ ___32-[CRSUIClusterThemeManager init]_block_invoke.17.cold.1
+ ___32-[CRSUIClusterThemeManager init]_block_invoke.18
+ ___32-[CRSUIClusterThemeManager init]_block_invoke.18.cold.1
+ ___32-[CRSUIClusterThemeManager init]_block_invoke_2
+ ___32-[CRSUIClusterThemeService init]_block_invoke
+ ___34+[CRSUISystemWallpaper wallpapers]_block_invoke
+ ___34-[CRSUIStatusBarStyleService init]_block_invoke
+ ___38+[CRSUISystemWallpaper _wallpaperInfo]_block_invoke
+ ___40-[CRSUIClusterThemeColorWallpaper color]_block_invoke
+ ___40-[CRSUISystemWallpaper resolveWallpaper]_block_invoke
+ ___40-[CRSUISystemWallpaper resolveWallpaper]_block_invoke_2
+ ___43+[CRSUIClusterThemeSpecification interface]_block_invoke
+ ___43+[CRSUIPunchThroughSpecification interface]_block_invoke
+ ___45-[CRSUIPunchThroughService initWithDelegate:]_block_invoke
+ ___45-[CRSUIWallpaperPreferences updateThemeData:]_block_invoke
+ ___45-[CRSUIWallpaperPreferences updateThemeData:]_block_invoke.cold.1
+ ___49-[CRSUIClusterThemeManager updateExtraAssetsURL:]_block_invoke
+ ___49-[CRSUIClusterThemeService updateExtraAssetsURL:]_block_invoke
+ ___50-[CRSUIClusterThemeManager loadWallpaperFromData:]_block_invoke
+ ___50-[CRSUIClusterThemeManager loadWallpaperFromData:]_block_invoke_2
+ ___50-[CRSUIClusterThemeManager loadWallpaperFromData:]_block_invoke_3
+ ___52-[CRSUIClusterThemeManager setThemeData:completion:]_block_invoke
+ ___53-[CRSUIClusterThemeManager _setThemeData:completion:]_block_invoke
+ ___53-[CRSUIClusterThemeManager _setThemeData:completion:]_block_invoke.33
+ ___53-[CRSUIClusterThemeManager _setThemeData:completion:]_block_invoke.cold.1
+ ___54-[CRSUIClusterThemeManager _handleConnectionActivated]_block_invoke
+ ___57-[CRSUIPunchThroughController _handleConnectionActivated]_block_invoke
+ ___57-[CRSUIPunchThroughController _handleConnectionActivated]_block_invoke_2
+ ___57-[CRSUIWallpaperPreferences updateHasGaugeClusterScreen:]_block_invoke
+ ___57-[CRSUIWallpaperPreferences updateHasGaugeClusterScreen:]_block_invoke.cold.1
+ ___58-[CRSUIClusterThemeManager _processThemeLayoutData:error:]_block_invoke
+ ___60-[CRSUIClusterThemeManager resolveWallpaper:withCompletion:]_block_invoke
+ ___60-[CRSUIClusterThemeManager resolveWallpaper:withCompletion:]_block_invoke.cold.1
+ ___62-[CRSUIPunchThroughController initWithPunchThroughIdentifier:]_block_invoke
+ ___62-[CRSUIPunchThroughController initWithPunchThroughIdentifier:]_block_invoke.4
+ ___62-[CRSUIPunchThroughController initWithPunchThroughIdentifier:]_block_invoke.4.cold.1
+ ___62-[CRSUIPunchThroughController initWithPunchThroughIdentifier:]_block_invoke.5
+ ___62-[CRSUIPunchThroughController initWithPunchThroughIdentifier:]_block_invoke.5.cold.1
+ ___62-[CRSUIPunchThroughController initWithPunchThroughIdentifier:]_block_invoke_2
+ ___62-[CRSUIPunchThroughController requestDismissalWithCompletion:]_block_invoke
+ ___62-[CRSUIPunchThroughController requestDismissalWithCompletion:]_block_invoke_2
+ ___62-[CRSUIPunchThroughService _connectionQueue_removeConnection:]_block_invoke
+ ___65-[CRSUIPunchThroughController requestPresentationWithCompletion:]_block_invoke
+ ___65-[CRSUIPunchThroughController requestPresentationWithCompletion:]_block_invoke_2
+ ___66-[CRSUIClusterThemeManager dynamicAppearanceWallpapersForVehicle:]_block_invoke
+ ___66-[CRSUIClusterThemeManager dynamicAppearanceWallpapersForVehicle:]_block_invoke_2
+ ___66-[CRSUIClusterThemeManager dynamicAppearanceWallpapersForVehicle:]_block_invoke_3
+ ___69-[CRSUIPunchThroughController serverDismissedPunchThroughIdentifier:]_block_invoke
+ ___70-[CRSUIClusterThemeService listener:didReceiveConnection:withContext:]_block_invoke
+ ___70-[CRSUIClusterThemeService listener:didReceiveConnection:withContext:]_block_invoke.13
+ ___70-[CRSUIClusterThemeService listener:didReceiveConnection:withContext:]_block_invoke_2
+ ___70-[CRSUIClusterThemeService listener:didReceiveConnection:withContext:]_block_invoke_2.cold.1
+ ___70-[CRSUIPunchThroughService listener:didReceiveConnection:withContext:]_block_invoke
+ ___70-[CRSUIPunchThroughService listener:didReceiveConnection:withContext:]_block_invoke.13
+ ___70-[CRSUIPunchThroughService listener:didReceiveConnection:withContext:]_block_invoke_2
+ ___70-[CRSUIPunchThroughService listener:didReceiveConnection:withContext:]_block_invoke_2.cold.1
+ ___70-[CRSUISystemWallpaperProvider dynamicAppearanceWallpapersForVehicle:]_block_invoke
+ ___72-[CRSUIStatusBarStyleService listener:didReceiveConnection:withContext:]_block_invoke.100
+ ___77-[CRSUIApplicationSceneSettingsDiffInspector observeFrameRateLimitWithBlock:]_block_invoke
+ ___78-[CRSUIClusterThemeManager getURLForAssetWithIdentifier:displayID:completion:]_block_invoke
+ ___79-[CRSUIClusterThemeManager _getURLForAssetWithIdentifier:displayID:completion:]_block_invoke
+ ___79-[CRSUIClusterThemeManager _getURLForAssetWithIdentifier:displayID:completion:]_block_invoke.35
+ ___79-[CRSUIClusterThemeManager _getURLForAssetWithIdentifier:displayID:completion:]_block_invoke.cold.1
+ ___87-[CRSUIPunchThroughService clientRequestDismissalForPunchThroughIdentifier:completion:]_block_invoke
+ ___90-[CRSUIPunchThroughService clientRequestPresentationForPunchThroughIdentifier:completion:]_block_invoke
+ ___99-[CRSUIClusterPressBSActionsHandler _respondToActions:forFBSScene:inUIScene:fromTransitionContext:]_block_invoke
+ ___99-[CRSUIClusterPressBSActionsHandler _respondToActions:forFBSScene:inUIScene:fromTransitionContext:]_block_invoke_2
+ ___CRSUICAPackageViewWithStatefulPackage_block_invoke
+ ___NSArray0__struct
+ ___block_descriptor_32_e26_B16?0"<CRSUIWallpaper>"8l
+ ___block_descriptor_32_e36_B16?0"CRSUIClusterThemeWallpaper"8l
+ ___block_descriptor_32_e57_v16?0"BSServiceConnection<BSServiceConnectionContext>"8l
+ ___block_descriptor_40_e8_32bs_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_40_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_40_e8_32s_e33_B16?0"CRSUIClusterThemeLayout"8ls32l8
+ ___block_descriptor_40_e8_32s_e34_B16?0"CRSUIClusterThemeDisplay"8ls32l8
+ ___block_descriptor_40_e8_32s_e36_"UIImage"16?0"UITraitCollection"8ls32l8
+ ___block_descriptor_40_e8_32s_e36_B16?0"CRSUIClusterThemeWallpaper"8ls32l8
+ ___block_descriptor_40_e8_32s_e37_"NSString"16?0"UITraitCollection"8ls32l8
+ ___block_descriptor_40_e8_32s_e37_v24?0"CRSUIClusterPressAction"8^B16ls32l8
+ ___block_descriptor_40_e8_32s_e39_v24?0"CRSUIClimatePopoverAction"8^B16ls32l8
+ ___block_descriptor_40_e8_32w_e42_v16?0"<BSServiceConnectionConfiguring>"8lw32l8
+ ___block_descriptor_40_e8_32w_e50_v24?0"_CRSUIClusterThemeLayoutData"8"NSError"16lw32l8
+ ___block_descriptor_40_e8_32w_e57_v16?0"BSServiceConnection<BSServiceConnectionContext>"8lw32l8
+ ___block_descriptor_41_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e36_"UIColor"16?0"UITraitCollection"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e48_v24?0"NSSecurityScopedURLWrapper"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_65_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_literal_global.17
+ ___block_literal_global.19
+ ___block_literal_global.20
+ ___block_literal_global.237
+ ___block_literal_global.42
+ ___block_literal_global.44
+ ___block_literal_global.66
+ ___block_literal_global.7
+ ___block_literal_global.92
+ __os_log_fault_impl
+ _kCFBooleanTrue
+ _objc_msgSend$URLForResource:withExtension:
+ _objc_msgSend$_getURLForAssetWithIdentifier:displayID:completion:
+ _objc_msgSend$_initWithLightModeColor:darkModeColor:
+ _objc_msgSend$_processThemeLayoutData:error:
+ _objc_msgSend$_setThemeData:completion:
+ _objc_msgSend$actionType
+ _objc_msgSend$addSublayer:
+ _objc_msgSend$appendObject:withName:
+ _objc_msgSend$asset
+ _objc_msgSend$assetDescription
+ _objc_msgSend$assetForInterfaceStyle:
+ _objc_msgSend$associatedPaletteID
+ _objc_msgSend$clientRequestDismissalForPunchThroughIdentifier:completion:
+ _objc_msgSend$clientRequestPresentationForPunchThroughIdentifier:completion:
+ _objc_msgSend$clusterThemeDisplays
+ _objc_msgSend$clusterThemeManager:didUpdateDisplays:
+ _objc_msgSend$clusterThemeManager:didUpdateExtraAssetsURL:
+ _objc_msgSend$clusterThemeManager:didUpdateThemeData:
+ _objc_msgSend$clusterThemeService:didSetThemeData:error:
+ _objc_msgSend$color
+ _objc_msgSend$colorScheme
+ _objc_msgSend$colors
+ _objc_msgSend$connectionToPunchThroughIdentifierMap
+ _objc_msgSend$containsValueForKey:
+ _objc_msgSend$contentMode
+ _objc_msgSend$currentLayoutID
+ _objc_msgSend$currentTraitCollection
+ _objc_msgSend$currentWallpaper
+ _objc_msgSend$darkModeState
+ _objc_msgSend$data
+ _objc_msgSend$dataProvider
+ _objc_msgSend$dataProviderDelegate
+ _objc_msgSend$dataProviderIsReady:
+ _objc_msgSend$dataWithContentsOfURL:
+ _objc_msgSend$decodeBoolForKey:
+ _objc_msgSend$decodeCGSizeForKey:
+ _objc_msgSend$decodeCollectionOfClass:containingClass:forKey:
+ _objc_msgSend$decodeDictionaryOfClass:forKey:
+ _objc_msgSend$decodeStringForKey:
+ _objc_msgSend$decodeUInt64ForKey:
+ _objc_msgSend$defaultWallpapers
+ _objc_msgSend$displayID
+ _objc_msgSend$displayName
+ _objc_msgSend$displayThemeData
+ _objc_msgSend$displayType
+ _objc_msgSend$displays
+ _objc_msgSend$dynamicAppearanceWallpapersForVehicle:
+ _objc_msgSend$encodeBool:forKey:
+ _objc_msgSend$encodeCGSize:forKey:
+ _objc_msgSend$encodeCollection:forKey:
+ _objc_msgSend$encodeDictionary:forKey:
+ _objc_msgSend$encodeUInt64:forKey:
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$extraAssetsURL
+ _objc_msgSend$frame
+ _objc_msgSend$getClusterThemeLayoutData:
+ _objc_msgSend$getURLForAssetWithIdentifier:displayID:
+ _objc_msgSend$getURLForAssetWithIdentifier:displayID:reply:
+ _objc_msgSend$handleTapOutsidePopoverFrames
+ _objc_msgSend$hasDynamicState
+ _objc_msgSend$hasGaugeClusterScreen
+ _objc_msgSend$hideRoundedCorners
+ _objc_msgSend$image
+ _objc_msgSend$imageWithTraitCollection:
+ _objc_msgSend$initWithAsset:lightModeStateForPaletteID:darkModeStateForPaletteID:supportsDynamicAppearance:
+ _objc_msgSend$initWithAsset:type:lightModeState:darkModeState:supportsDynamicAppearance:
+ _objc_msgSend$initWithBool:
+ _objc_msgSend$initWithIdentifier:
+ _objc_msgSend$initWithIdentifier:displayID:layoutID:traits:
+ _objc_msgSend$initWithIdentifier:displayName:colorScheme:sortIndex:colors:
+ _objc_msgSend$initWithIdentifier:displayName:image:package:color:associatedPaletteID:isDefault:data:traits:
+ _objc_msgSend$initWithIdentifier:displayName:palettes:wallpapers:preview:
+ _objc_msgSend$initWithIdentifier:displayType:size:layouts:
+ _objc_msgSend$initWithIdentifier:url:
+ _objc_msgSend$initWithIdentifier:url:packageType:
+ _objc_msgSend$initWithImage:
+ _objc_msgSend$initWithLayer:
+ _objc_msgSend$initWithLightModeAsset:darkModeAsset:supportsDynamicAppearance:
+ _objc_msgSend$initWithLightModeColor:darkModeColor:
+ _objc_msgSend$initWithPackage:dynamicStateProvider:
+ _objc_msgSend$initWithPackage:lightModeState:darkModeState:
+ _objc_msgSend$initWithPackage:lightModeState:darkModeState:hasDynamicState:
+ _objc_msgSend$initWithPackage:state:
+ _objc_msgSend$initWithPackage:state:dynamicStateProvider:
+ _objc_msgSend$initWithSupportsDynamicAppearance:supportsDashboardPlatterMaterials:iconLabelsRequireBackground:hideRoundedCorners:black:
+ _objc_msgSend$initWithThemeData:
+ _objc_msgSend$initWithWallpaperIdentifier:displayID:layoutID:
+ _objc_msgSend$initWithWallpaperInformation:color:
+ _objc_msgSend$initWithWallpaperInformation:imageResolver:
+ _objc_msgSend$initWithWallpaperInformation:imageResolver:thumbnailResolver:statefulPackage:color:
+ _objc_msgSend$initWithWallpaperInformation:statefulPackage:
+ _objc_msgSend$isBlack
+ _objc_msgSend$isDefault
+ _objc_msgSend$isEqualToDictionary:
+ _objc_msgSend$isEqualToNumber:
+ _objc_msgSend$isGeometryFlipped
+ _objc_msgSend$layer
+ _objc_msgSend$layoutID
+ _objc_msgSend$layouts
+ _objc_msgSend$lightModeState
+ _objc_msgSend$loadWallpaperFromData:
+ _objc_msgSend$package
+ _objc_msgSend$packageType
+ _objc_msgSend$packageWithContentsOfURL:type:options:error:
+ _objc_msgSend$palettes
+ _objc_msgSend$preview
+ _objc_msgSend$previousSystemWallpaperData
+ _objc_msgSend$punchThroughControllerDidDismiss:
+ _objc_msgSend$punchThroughIdentifier
+ _objc_msgSend$punchThroughService:dismissPunchThroughWithIdentifier:
+ _objc_msgSend$punchThroughService:presentPunchThroughWithIdentifier:
+ _objc_msgSend$registerForTraitChanges:withAction:
+ _objc_msgSend$registerImage:withTraitCollection:
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$resolveWallpaper
+ _objc_msgSend$rootLayer
+ _objc_msgSend$selectButtonPressedWithType:
+ _objc_msgSend$serverDismissedPunchThroughIdentifier:
+ _objc_msgSend$setAppearanceModePreference:
+ _objc_msgSend$setBackgroundColor:
+ _objc_msgSend$setContentMode:
+ _objc_msgSend$setCurrentWallpaper:
+ _objc_msgSend$setDisplayThemeData:
+ _objc_msgSend$setDisplays:
+ _objc_msgSend$setExtraAssetsURL:
+ _objc_msgSend$setGeometryFlipped:
+ _objc_msgSend$setHasGaugeClusterScreen:
+ _objc_msgSend$setObject:forKey:
+ _objc_msgSend$setPosition:
+ _objc_msgSend$setState:animated:
+ _objc_msgSend$setState:ofLayer:
+ _objc_msgSend$setState:ofLayer:transitionSpeed:
+ _objc_msgSend$setThemeData:
+ _objc_msgSend$setThemeData:reply:
+ _objc_msgSend$setTransform:
+ _objc_msgSend$setWallpaper:forDisplayWithID:requiresDarkAppearance:
+ _objc_msgSend$size
+ _objc_msgSend$sortIndex
+ _objc_msgSend$stateForInterfaceStyle:
+ _objc_msgSend$stateWithName:
+ _objc_msgSend$strongToStrongObjectsMapTable
+ _objc_msgSend$systemIdentifier
+ _objc_msgSend$themeData
+ _objc_msgSend$themeDataProvider
+ _objc_msgSend$themeDataWithCurrentWallpaper:
+ _objc_msgSend$traits
+ _objc_msgSend$type
+ _objc_msgSend$updateExtraAssetsURL:
+ _objc_msgSend$updateThemeData:
+ _objc_msgSend$url
+ _objc_msgSend$wallpaperDescription
+ _objc_msgSend$wallpaperForDisplayWithID:
+ _objc_msgSend$wallpaperForLayout
+ _objc_msgSend$wallpaperID
+ _objc_msgSend$wallpaperWithIdentifier:
+ _objc_msgSend$wallpapers
+ _objc_retainBlock
+ _objc_retain_x25
+ _objc_retain_x27
+ _objc_retain_x28
+ _objc_setProperty_nonatomic_copy
+ _wallpapers._systemWallpapers
+ _wallpapers.onceToken
- +[CRSUIWallpaper _wallpaperInfo]
- +[CRSUIWallpaperPreferences _wallpaperWithIdentifier:]
- +[CRSUIWallpaperPreferences availableWallpapers]
- +[CRSUIWallpaperPreferences defaultWallpaper]
- +[CRSUIWallpaperPreferences wallpaperWithIdentifier:]
- -[CRSUIMutableWallpaperSceneSettings setWallpaperIdentifier:]
- -[CRSUIMutableWallpaperSceneSettings wallpaperIdentifier]
- -[CRSUIStatusBarStyleService delegate]
- -[CRSUIStatusBarStyleService initWithDelegate:]
- -[CRSUIStatusBarStyleService setDelegate:]
- -[CRSUIWallpaper .cxx_destruct]
- -[CRSUIWallpaper description]
- -[CRSUIWallpaper iconLabelsRequireBackground]
- -[CRSUIWallpaper initWithWallpaperIdentifier:]
- -[CRSUIWallpaper setThumbnailAssetCatalogName:]
- -[CRSUIWallpaper setWallpaperAssetCatalogName:]
- -[CRSUIWallpaper supportsDashboardPlatterMaterials]
- -[CRSUIWallpaper supportsDynamicAppearance]
- -[CRSUIWallpaper thumbnailAssetCatalogName]
- -[CRSUIWallpaper thumbnailColor]
- -[CRSUIWallpaper thumbnailImageCompatibleWithTraitCollection:]
- -[CRSUIWallpaper wallpaperAssetCatalogName]
- -[CRSUIWallpaper wallpaperColor]
- -[CRSUIWallpaper wallpaperIdentifier]
- -[CRSUIWallpaper wallpaperImageCompatibleWithTraitCollection:]
- -[CRSUIWallpaperPreferences init]
- -[CRSUIWallpaperSceneSettings wallpaperIdentifier]
- _OBJC_CLASS_$_CRSUIWallpaper
- _OBJC_IVAR_$_CRSUIStatusBarStyleService._delegate
- _OBJC_IVAR_$_CRSUIWallpaper._iconLabelsRequireBackground
- _OBJC_IVAR_$_CRSUIWallpaper._supportsDashboardPlatterMaterials
- _OBJC_IVAR_$_CRSUIWallpaper._supportsDynamicAppearance
- _OBJC_IVAR_$_CRSUIWallpaper._thumbnailAssetCatalogName
- _OBJC_IVAR_$_CRSUIWallpaper._wallpaperAssetCatalogName
- _OBJC_IVAR_$_CRSUIWallpaper._wallpaperIdentifier
- _OBJC_METACLASS_$_CRSUIWallpaper
- __OBJC_$_CLASS_METHODS_CRSUIWallpaper
- __OBJC_$_CLASS_METHODS_CRSUIWallpaperPreferences
- __OBJC_$_CLASS_PROP_LIST_CRSUIWallpaperPreferences
- __OBJC_$_INSTANCE_METHODS_CRSUIWallpaper
- __OBJC_$_INSTANCE_VARIABLES_CRSUIWallpaper
- __OBJC_$_PROP_LIST_CRSUIApplicationSceneSettings.51
- __OBJC_$_PROP_LIST_CRSUIDashboardWidgetSceneSettings.54
- __OBJC_$_PROP_LIST_CRSUIInstrumentClusterSceneSettings.64
- __OBJC_$_PROP_LIST_CRSUIProxyApplicationSceneSettings.53
- __OBJC_$_PROP_LIST_CRSUITemplateDashboardWidgetSceneSettings.79
- __OBJC_$_PROP_LIST_CRSUITemplateInstrumentClusterSceneSettings.96
- __OBJC_CLASS_RO_$_CRSUIWallpaper
- __OBJC_METACLASS_RO_$_CRSUIWallpaper
- ___32+[CRSUIWallpaper _wallpaperInfo]_block_invoke
- ___32-[CRSUIWallpaper wallpaperColor]_block_invoke
- ___47-[CRSUIStatusBarStyleService initWithDelegate:]_block_invoke
- ___48+[CRSUIWallpaperPreferences availableWallpapers]_block_invoke
- ___53+[CRSUIWallpaperPreferences wallpaperWithIdentifier:]_block_invoke
- ___54+[CRSUIWallpaperPreferences _wallpaperWithIdentifier:]_block_invoke
- ___72-[CRSUIStatusBarStyleService listener:didReceiveConnection:withContext:]_block_invoke.45
- ___block_descriptor_40_e8_32s_e24_B16?0"CRSUIWallpaper"8ls32l8
- ___block_literal_global.177
- ___block_literal_global.184
- ___block_literal_global.76
- _availableWallpapers._availableWallpapers
- _availableWallpapers.onceToken
- _objc_msgSend$_wallpaperWithIdentifier:
- _objc_msgSend$availableWallpapers
- _objc_msgSend$initWithWallpaperIdentifier:
- _objc_msgSend$setPreviousWallpaperIdentifier:
- _objc_msgSend$setWallpaperIdentifier:
CStrings:
+ "\x01\x11"
+ "\x01\x17"
+ "\x02\x12"
+ "\x02!"
+ "\x02#"
+ "\x03"
+ "\x04"
+ "\x05"
+ "\x11\x12"
+ "\x12"
+ "\x15"
+ "#"
+ "$"
+ "-[CRSUICAPackageView initWithPackage:state:dynamicStateProvider:]"
+ "-[CRSUIWallpaperPreferences updateWallpaperToSupportDynamicAppearance]"
+ "5"
+ "@\"<CRSUIClimatePopoverActionDelegate>\""
+ "@\"<CRSUIClusterPressBSActionActionDelegate>\""
+ "@\"<CRSUIClusterThemeDataProviding>\""
+ "@\"<CRSUIClusterThemeManagerDelegate>\""
+ "@\"<CRSUIClusterThemeServiceDelegate>\""
+ "@\"<CRSUIPunchThroughControllerDelegate>\""
+ "@\"<CRSUIPunchThroughServiceDelegate>\""
+ "@\"<CRSUIWallpaper>\""
+ "@\"<CRSUIWallpaper>\"24@0:8@\"<CRWallpaperData>\"16"
+ "@\"<CRSUIWallpaperDataProviding>\""
+ "@\"<CRSUIWallpaperDataProvidingDelegate>\""
+ "@\"<CRSUIWallpaperDataProvidingDelegate>\"16@0:8"
+ "@\"<CRWallpaperData>\""
+ "@\"<CRWallpaperData>\"16@0:8"
+ "@\"CALayer\""
+ "@\"CAPackage\""
+ "@\"CAStateController\""
+ "@\"CRAssetWallpaperData\""
+ "@\"CRSUIClusterThemeCAPackageAsset\""
+ "@\"CRSUIClusterThemeCAPackageWallpaper\""
+ "@\"CRSUIClusterThemeColorWallpaper\""
+ "@\"CRSUIClusterThemeImageAsset\""
+ "@\"CRSUIClusterThemeImageWallpaper\""
+ "@\"CRSUIClusterThemeLayoutPreview\""
+ "@\"CRSUIStatefulCAPackage\""
+ "@\"CRSUIWallpaperTraits\""
+ "@\"CRSUIWallpaperTraits\"16@0:8"
+ "@\"NSArray\"16@0:8"
+ "@\"NSArray\"24@0:8@\"CRVehicle\"16"
+ "@\"NSDictionary\""
+ "@\"NSMapTable\""
+ "@\"NSNumber\"16@0:8"
+ "@\"NSSecurityScopedURLWrapper\""
+ "@\"NSSecurityScopedURLWrapper\"16@0:8"
+ "@\"NSString\"16@?0@\"UITraitCollection\"8"
+ "@\"UIColor\""
+ "@\"UIImage\"16@?0@\"UITraitCollection\"8"
+ "@24@0:8@\"<BSXPCDecoding>\"16"
+ "@24@0:8Q16"
+ "@32@0:8@16@?24"
+ "@36@0:8@16@24B32"
+ "@36@0:8B16B20B24B28B32"
+ "@40@0:8@16@24@32"
+ "@40@0:8@16@24@?32"
+ "@40@0:8@16@?24@?32"
+ "@44@0:8@16@24@32B40"
+ "@52@0:8@16@24@32@40B48"
+ "@56@0:8@16@24@32@40@48"
+ "@56@0:8@16@24Q32q40@48"
+ "@56@0:8@16@?24@?32@40@48"
+ "@56@0:8@16Q24{CGSize=dd}32@48"
+ "@68@0:8@16@24@32@40B48@52@60"
+ "@84@0:8@16@24@32@40@48@56B64@68@76"
+ "@?"
+ "B16@?0@\"<CRSUIWallpaper>\"8"
+ "B16@?0@\"CRSUIClusterThemeDisplay\"8"
+ "B16@?0@\"CRSUIClusterThemeLayout\"8"
+ "B16@?0@\"CRSUIClusterThemeWallpaper\"8"
+ "B28@0:8@16B24"
+ "BSXPCSecureCoding"
+ "CRSUIAssetWallpaper"
+ "CRSUICAPackageView"
+ "CRSUICAPackageView.m"
+ "CRSUIClimatePopoverAction"
+ "CRSUIClimatePopoverActionDelegate"
+ "CRSUIClimatePopoverBSActionsHandler"
+ "CRSUIClusterPressAction"
+ "CRSUIClusterPressBSActionsHandler"
+ "CRSUIClusterThemeAsset"
+ "CRSUIClusterThemeCAPackageAsset"
+ "CRSUIClusterThemeCAPackageWallpaper"
+ "CRSUIClusterThemeClientToServerInterface"
+ "CRSUIClusterThemeColorWallpaper"
+ "CRSUIClusterThemeDisplay"
+ "CRSUIClusterThemeImageAsset"
+ "CRSUIClusterThemeImageWallpaper"
+ "CRSUIClusterThemeLayout"
+ "CRSUIClusterThemeLayoutPreview"
+ "CRSUIClusterThemeManager"
+ "CRSUIClusterThemePalette"
+ "CRSUIClusterThemeServerToClientInterface"
+ "CRSUIClusterThemeService"
+ "CRSUIClusterThemeSpecification"
+ "CRSUIClusterThemeWallpaper"
+ "CRSUIFrameRateLimitProviding"
+ "CRSUIMutableFrameRateLimitProviding"
+ "CRSUIPunchThroughClientToServerInterface"
+ "CRSUIPunchThroughController"
+ "CRSUIPunchThroughServerToClientInterface"
+ "CRSUIPunchThroughService"
+ "CRSUIPunchThroughSpecification"
+ "CRSUIResolvedWallpaper"
+ "CRSUIStatefulCAPackage"
+ "CRSUIStatusBarStyleServiceObserver"
+ "CRSUISystemWallpaper"
+ "CRSUISystemWallpaperProvider"
+ "CRSUIWallpaperDataProviding"
+ "CRSUIWallpaperPreferences.m"
+ "CRSUIWallpaperTraits"
+ "ClusterTheme"
+ "Error getting url of %@:%@: %@"
+ "Error loading CAPackage from %@: %@"
+ "Error loading image from %@"
+ "Error retrieving cluster layouts: %@"
+ "Error setting theme data: %@"
+ "Has gauge cluster screen already set with value: %d"
+ "Ignoring duplicated update to theme data"
+ "Invalid wallpaper information"
+ "Invalidating listener! %@"
+ "Invalidating service"
+ "Missing dynamic appearance wallpapers"
+ "No theme data provider set! Unable to complete request for assert URL"
+ "No theme data provider set! Unable to complete request for cluster layouts"
+ "No wallpaper supports dynamic appearance for %@:%@"
+ "Punch through %{public}@ dismissed by server, informing client %{public}@"
+ "Q"
+ "Received %d displays"
+ "Received request for asset url (connection: %@): %@:%@"
+ "Received request for cluster layouts (connection: %@)"
+ "Received request to set theme data (connection: %@): %@"
+ "Requesting cluster layouts"
+ "Setting theme data: %@"
+ "Successfully set theme data"
+ "T@\"<CRSUIClimatePopoverActionDelegate>\",W,N,V_delegate"
+ "T@\"<CRSUIClusterPressBSActionActionDelegate>\",W,N,V_delegate"
+ "T@\"<CRSUIClusterThemeDataProviding>\",W,N,V_themeDataProvider"
+ "T@\"<CRSUIClusterThemeManagerDelegate>\",W,N,V_delegate"
+ "T@\"<CRSUIClusterThemeServiceDelegate>\",W,N,V_delegate"
+ "T@\"<CRSUIPunchThroughControllerDelegate>\",W,N,V_delegate"
+ "T@\"<CRSUIPunchThroughServiceDelegate>\",W,N,V_delegate"
+ "T@\"<CRSUIWallpaper>\",&,N"
+ "T@\"<CRSUIWallpaper>\",R,N,V_wallpaper"
+ "T@\"<CRSUIWallpaperDataProviding>\",&,N,V_dataProvider"
+ "T@\"<CRSUIWallpaperDataProvidingDelegate>\",W,N"
+ "T@\"<CRSUIWallpaperDataProvidingDelegate>\",W,N,V_dataProviderDelegate"
+ "T@\"<CRSUIWallpaperDataProvidingDelegate>\",W,N,VdataProviderDelegate"
+ "T@\"<CRWallpaperData>\",&,N,V_wallpaper"
+ "T@\"<CRWallpaperData>\",R,N"
+ "T@\"BSServiceInterface\",R,N"
+ "T@\"BSServiceQuality\",R,N"
+ "T@\"CAPackage\",R,N,V_package"
+ "T@\"CRAssetWallpaperData\",R,N,V_data"
+ "T@\"CRSUIClusterThemeCAPackageAsset\",R,N,V_asset"
+ "T@\"CRSUIClusterThemeCAPackageWallpaper\",R,N,V_package"
+ "T@\"CRSUIClusterThemeImageWallpaper\",R,N,V_image"
+ "T@\"CRSUIClusterThemeLayoutPreview\",R,N,V_preview"
+ "T@\"CRSUIWallpaperTraits\",R,N"
+ "T@\"CRSUIWallpaperTraits\",R,N,V_traits"
+ "T@\"NSArray\",&,N"
+ "T@\"NSArray\",&,N,V_displays"
+ "T@\"NSArray\",R,C,N,V_layouts"
+ "T@\"NSArray\",R,N,V_colors"
+ "T@\"NSArray\",R,N,V_palettes"
+ "T@\"NSArray\",R,N,V_wallpapers"
+ "T@\"NSDictionary\",&,N,V_themeData"
+ "T@\"NSDictionary\",R,N,V_themeData"
+ "T@\"NSMapTable\",&,N,V_connectionToPunchThroughIdentifierMap"
+ "T@\"NSNumber\",N"
+ "T@\"NSSecurityScopedURLWrapper\",&,N,V_extraAssetsURL"
+ "T@\"NSSecurityScopedURLWrapper\",R,N"
+ "T@\"NSSecurityScopedURLWrapper\",R,N,V_url"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",C,N,V_punchThroughIdentifier"
+ "T@\"NSString\",C,N,V_state"
+ "T@\"NSString\",R,C,N,V_associatedPaletteID"
+ "T@\"NSString\",R,C,N,V_darkModeState"
+ "T@\"NSString\",R,C,N,V_displayID"
+ "T@\"NSString\",R,C,N,V_displayName"
+ "T@\"NSString\",R,C,N,V_identifier"
+ "T@\"NSString\",R,C,N,V_layoutID"
+ "T@\"NSString\",R,C,N,V_lightModeState"
+ "T@\"NSString\",R,C,N,V_packageType"
+ "T@\"NSString\",R,C,N,V_systemIdentifier"
+ "T@\"NSString\",R,C,N,V_thumbnailAssetCatalogName"
+ "T@\"NSString\",R,C,N,V_type"
+ "T@\"NSString\",R,C,N,V_wallpaperAssetCatalogName"
+ "T@\"NSString\",R,C,N,Videntifier"
+ "T@\"UIColor\",R,C,N"
+ "TB,R,N,GisBlack,V_black"
+ "TB,R,N,GisCustomizable"
+ "TB,R,N,V_hasDynamicState"
+ "TB,R,N,V_hideRoundedCorners"
+ "TB,R,N,V_isDefault"
+ "TQ,R,N,V_colorScheme"
+ "TQ,R,N,V_displayType"
+ "Tq,R,N,V_sortIndex"
+ "T{CGSize=dd},R,N,V_size"
+ "UISyncChannelDisabled"
+ "URLForResource:withExtension:"
+ "Unable to find dynamic appearance supporting wallpaper"
+ "Unable to retrieve asset url"
+ "Unable to retrieve cluster theme data"
+ "Unsupported wallpaper type: %{public}@"
+ "Vehicle missing theme data. Asset: %@ Wallpaper: %@"
+ "Vv24@0:8@\"NSSecurityScopedURLWrapper\"16"
+ "Vv24@0:8@\"NSString\"16"
+ "Vv24@0:8@16"
+ "Vv24@0:8@?16"
+ "Vv24@0:8@?<v@?@\"_CRSUIClusterThemeLayoutData\"@\"NSError\">16"
+ "Vv32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
+ "Vv32@0:8@\"_CRSUIClusterThemeData\"16@?<v@?@\"NSError\">24"
+ "Vv32@0:8@16@?24"
+ "Vv40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSSecurityScopedURLWrapper\"@\"NSError\">32"
+ "Vv40@0:8@16@24@?32"
+ "[CRSUIWallpaperPreferences] Ignoring #wallpaper update to %{public}@ for vehicle"
+ "[CRSUIWallpaperPreferences] Unknown wallpaper: %{public}@"
+ "_CRSUIClusterThemeData"
+ "_CRSUIClusterThemeLayoutData"
+ "_asset"
+ "_associatedPaletteID"
+ "_black"
+ "_color"
+ "_colorScheme"
+ "_colors"
+ "_connectionToPunchThroughIdentifierMap"
+ "_darkModeAsset"
+ "_darkModeColor"
+ "_darkModeState"
+ "_darkModeStateForPaletteID"
+ "_data"
+ "_dataProvider"
+ "_dataProviderDelegate"
+ "_displayID"
+ "_displayName"
+ "_displayType"
+ "_displays"
+ "_dynamicStateProvider"
+ "_extraAssetsURL"
+ "_getURLForAssetWithIdentifier:displayID:completion:"
+ "_hasDynamicState"
+ "_hasGaugeClusterScreen"
+ "_hideRoundedCorners"
+ "_image"
+ "_imageResolver"
+ "_imageURLWithCompatibleTraitCollection:"
+ "_initWithLightModeColor:darkModeColor:"
+ "_isDefault"
+ "_layoutID"
+ "_layouts"
+ "_lightModeAsset"
+ "_lightModeColor"
+ "_lightModeState"
+ "_lightModeStateForPaletteID"
+ "_lock_hasPendingPresentationRequest"
+ "_lock_pendingPresentationCompletion"
+ "_lock_presented"
+ "_package"
+ "_packageSize"
+ "_packageType"
+ "_palettes"
+ "_preview"
+ "_processThemeLayoutData:error:"
+ "_punchThroughIdentifier"
+ "_rootLayer"
+ "_setThemeData:completion:"
+ "_size"
+ "_sortIndex"
+ "_state"
+ "_stateController"
+ "_statefulPackage"
+ "_systemIdentifier"
+ "_themeData"
+ "_themeDataProvider"
+ "_thumbnailImageURLWithCompatibleTraitCollection:"
+ "_thumbnailResolver"
+ "_traits"
+ "_type"
+ "_url"
+ "_wallpaper"
+ "_wallpapers"
+ "actionType"
+ "addSublayer:"
+ "appendObject:withName:"
+ "asset"
+ "assetDescription"
+ "assetForInterfaceStyle:"
+ "associatedPaletteID"
+ "black"
+ "clientRequestDismissalForPunchThroughIdentifier:completion:"
+ "clientRequestPresentationForPunchThroughIdentifier:completion:"
+ "clusterThemeDisplays"
+ "clusterThemeManager:didUpdateDisplays:"
+ "clusterThemeManager:didUpdateExtraAssetsURL:"
+ "clusterThemeManager:didUpdateThemeData:"
+ "clusterThemeService:didSetThemeData:error:"
+ "color"
+ "colorScheme"
+ "colors"
+ "com.apple.CarPlay.ClusterTheme"
+ "com.apple.CarPlay.PunchThrough"
+ "com.apple.CarPlayApp.cluster-theme"
+ "com.apple.CarPlayApp.cluster-theme-service"
+ "com.apple.CarPlayApp.punch-through"
+ "com.apple.CarPlayApp.punch-through-service"
+ "com.apple.CarPlayUIServices.CRSUIClusterThemeManager"
+ "com.apple.CarPlayUIServices.CRSUIClusterThemeService"
+ "com.apple.CarPlayUIServices.CRSUIPunchThroughService"
+ "com.apple.CarPlayUIServices.cluster-theme-service"
+ "com.apple.private.CarPlayUIServices.cluster-theme"
+ "com.apple.private.CarPlayUIServices.punch-through"
+ "connectionToPunchThroughIdentifierMap"
+ "containsValueForKey:"
+ "contentMode"
+ "currentLayoutID"
+ "currentTraitCollection"
+ "customizable"
+ "darkModeAsset"
+ "darkModeColor"
+ "darkModeState"
+ "darkModeStateForPaletteID"
+ "data"
+ "dataProvider"
+ "dataProviderDelegate"
+ "dataProviderIsReady:"
+ "dataWithContentsOfURL:"
+ "decodeBoolForKey:"
+ "decodeCGSizeForKey:"
+ "decodeCollectionOfClass:containingClass:forKey:"
+ "decodeDictionaryOfClass:forKey:"
+ "decodeStringForKey:"
+ "decodeUInt64ForKey:"
+ "default"
+ "defaultWallpapers"
+ "displayID"
+ "displayName"
+ "displayThemeData"
+ "displayType"
+ "displays"
+ "dynamicAppearanceWallpapersForVehicle:"
+ "encodeBool:forKey:"
+ "encodeCGSize:forKey:"
+ "encodeCollection:forKey:"
+ "encodeDictionary:forKey:"
+ "encodeUInt64:forKey:"
+ "encodeWithBSXPCCoder:"
+ "errorWithDomain:code:userInfo:"
+ "extraAssetsURL"
+ "frameRateLimit"
+ "getClusterThemeLayoutData:"
+ "getURLForAssetWithIdentifier:displayID:"
+ "getURLForAssetWithIdentifier:displayID:completion:"
+ "getURLForAssetWithIdentifier:displayID:reply:"
+ "handleTapOutsidePopoverFrames"
+ "hasDynamicState"
+ "hasGaugeClusterScreen"
+ "hideRoundedCorners"
+ "image"
+ "imageWithTraitCollection:"
+ "initWithAsset:"
+ "initWithAsset:lightModeStateForPaletteID:darkModeStateForPaletteID:"
+ "initWithAsset:lightModeStateForPaletteID:darkModeStateForPaletteID:supportsDynamicAppearance:"
+ "initWithAsset:stateForPaletteID:"
+ "initWithAsset:type:lightModeState:darkModeState:"
+ "initWithAsset:type:lightModeState:darkModeState:supportsDynamicAppearance:"
+ "initWithAsset:type:state:"
+ "initWithBSXPCCoder:"
+ "initWithBool:"
+ "initWithColor:"
+ "initWithDataProvider:"
+ "initWithFrame:"
+ "initWithIdentifier:"
+ "initWithIdentifier:displayID:layoutID:traits:"
+ "initWithIdentifier:displayName:color:associatedPaletteID:isDefault:data:traits:"
+ "initWithIdentifier:displayName:colorScheme:sortIndex:colors:"
+ "initWithIdentifier:displayName:image:associatedPaletteID:isDefault:data:traits:"
+ "initWithIdentifier:displayName:image:package:color:associatedPaletteID:isDefault:data:traits:"
+ "initWithIdentifier:displayName:package:associatedPaletteID:isDefault:data:traits:"
+ "initWithIdentifier:displayName:palettes:wallpapers:preview:"
+ "initWithIdentifier:displayType:size:layouts:"
+ "initWithIdentifier:url:"
+ "initWithIdentifier:url:packageType:"
+ "initWithImage:"
+ "initWithInfo:responder:"
+ "initWithLayer:"
+ "initWithLightModeAsset:darkModeAsset:"
+ "initWithLightModeAsset:darkModeAsset:supportsDynamicAppearance:"
+ "initWithLightModeColor:darkModeColor:"
+ "initWithPackage:"
+ "initWithPackage:dynamicStateProvider:"
+ "initWithPackage:lightModeState:darkModeState:"
+ "initWithPackage:lightModeState:darkModeState:hasDynamicState:"
+ "initWithPackage:state:"
+ "initWithPackage:state:dynamicStateProvider:"
+ "initWithPressType:"
+ "initWithPunchThroughIdentifier:"
+ "initWithSupportsDynamicAppearance:supportsDashboardPlatterMaterials:iconLabelsRequireBackground:hideRoundedCorners:black:"
+ "initWithThemeData:"
+ "initWithWallpaperIdentifier:displayID:layoutID:"
+ "initWithWallpaperInformation:color:"
+ "initWithWallpaperInformation:imageResolver:"
+ "initWithWallpaperInformation:imageResolver:thumbnailResolver:"
+ "initWithWallpaperInformation:imageResolver:thumbnailResolver:statefulPackage:color:"
+ "initWithWallpaperInformation:statefulPackage:"
+ "isBlack"
+ "isCustomizable"
+ "isDefault"
+ "isEqualToDictionary:"
+ "isEqualToNumber:"
+ "isGeometryFlipped"
+ "isReady"
+ "layer"
+ "layoutID"
+ "layoutSubviews"
+ "layouts"
+ "lightModeAsset"
+ "lightModeColor"
+ "lightModeState"
+ "lightModeStateForPaletteID"
+ "loadWallpaperFromData:"
+ "manager extraAssetsURL=%@"
+ "observeFrameRateLimitWithBlock:"
+ "package"
+ "packageType"
+ "packageWithContentsOfURL:type:options:error:"
+ "palettes"
+ "presentedPopoverFrames"
+ "preview"
+ "previousSystemWallpaperData"
+ "punchThroughControllerDidDismiss:"
+ "punchThroughIdentifier"
+ "punchThroughIdentifierDidDismiss:"
+ "punchThroughService:dismissPunchThroughWithIdentifier:"
+ "punchThroughService:presentPunchThroughWithIdentifier:"
+ "registerForTraitChanges:withAction:"
+ "registerImage:withTraitCollection:"
+ "removeObjectForKey:"
+ "requestDismissalWithCompletion:"
+ "requestPresentationWithCompletion:"
+ "resolveWallpaper"
+ "resolveWallpaper:withCompletion:"
+ "rootLayer"
+ "selectButtonPressedWithType:"
+ "serverDismissedPunchThroughIdentifier:"
+ "service extraAssetsURL=%@"
+ "setAppearanceModePreference:"
+ "setBackgroundColor:"
+ "setConnectionToPunchThroughIdentifierMap:"
+ "setContentMode:"
+ "setDataProvider:"
+ "setDataProviderDelegate:"
+ "setDisplayThemeData:"
+ "setDisplays:"
+ "setExtraAssetsURL:"
+ "setFrameRateLimit:"
+ "setGeometryFlipped:"
+ "setHasGaugeClusterScreen:"
+ "setObject:forKey:"
+ "setPosition:"
+ "setPresentedPopoverFrames:"
+ "setPunchThroughIdentifier:"
+ "setState:"
+ "setState:animated:"
+ "setState:ofLayer:"
+ "setState:ofLayer:transitionSpeed:"
+ "setThemeData:"
+ "setThemeData:completion:"
+ "setThemeData:reply:"
+ "setThemeDataProvider:"
+ "setTransform:"
+ "setWallpaper:"
+ "setWallpaper:forDisplayWithID:requiresDarkAppearance:"
+ "size"
+ "sizeThatFits:"
+ "sortIndex"
+ "state"
+ "stateForInterfaceStyle:"
+ "stateForPaletteIDWithInterfaceStyle:"
+ "stateWithName:"
+ "strongToStrongObjectsMapTable"
+ "supportsBSXPCSecureCoding"
+ "systemIdentifier"
+ "themeData"
+ "themeDataProvider"
+ "themeDataWithCurrentWallpaper:"
+ "thumbnailWithCompatibleTraitCollection:"
+ "traits"
+ "type"
+ "updateExtraAssetsURL:"
+ "updateHasGaugeClusterScreen:"
+ "updateThemeData:"
+ "updateWallpaperToSupportDynamicAppearance"
+ "url"
+ "userInterfaceStyleChanged"
+ "v16@?0@\"NSError\"8"
+ "v24@0:8@\"<BSXPCEncoding>\"16"
+ "v24@0:8@\"<CRSUIWallpaperDataProvidingDelegate>\"16"
+ "v24@0:8@\"NSNumber\"16"
+ "v24@?0@\"CRSUIClimatePopoverAction\"8^B16"
+ "v24@?0@\"CRSUIClusterPressAction\"8^B16"
+ "v24@?0@\"NSSecurityScopedURLWrapper\"8@\"NSError\"16"
+ "v24@?0@\"_CRSUIClusterThemeLayoutData\"8@\"NSError\"16"
+ "v32@0:8@\"<CRSUIWallpaper>\"16@?<v@?@\"CRSUIResolvedWallpaper\">24"
+ "v32@0:8@\"CRSUIStatusBarStyleService\"16@\"BSAnimationSettings\"24"
+ "v32@0:8@16@24"
+ "v32@0:8@16@?24"
+ "v40@0:8@16@24@?32"
+ "view"
+ "wallpaper"
+ "wallpaperDescription"
+ "wallpaperForDisplayWithID:"
+ "wallpaperForLayout"
+ "wallpaperForLayoutIdentifier:"
+ "wallpaperID"
+ "wallpapers"
+ "wallpapers.count == 1"
+ "{CGSize=\"width\"d\"height\"d}"
+ "{CGSize=dd}16@0:8"
+ "{CGSize=dd}32@0:8{CGSize=dd}16"
- "\x11\x13"
- "@\"<CRSUIStatusBarStyleServiceDelegate>\""
- "B16@?0@\"CRSUIWallpaper\"8"
- "T@\"<CRSUIStatusBarStyleServiceDelegate>\",W,N,V_delegate"
- "T@\"CRSUIWallpaper\",&,N"
- "T@\"CRSUIWallpaper\",R,N"
- "T@\"NSString\",&,N,V_thumbnailAssetCatalogName"
- "T@\"NSString\",&,N,V_wallpaperAssetCatalogName"
- "_wallpaperWithIdentifier:"
- "availableWallpapers"
- "initWithWallpaperIdentifier:"
- "setPreviousWallpaperIdentifier:"
- "setThumbnailAssetCatalogName:"
- "setWallpaperAssetCatalogName:"
- "setWallpaperIdentifier:"
- "thumbnailColor"
- "thumbnailImageCompatibleWithTraitCollection:"
- "wallpaperColor"
- "wallpaperImageCompatibleWithTraitCollection:"

```
