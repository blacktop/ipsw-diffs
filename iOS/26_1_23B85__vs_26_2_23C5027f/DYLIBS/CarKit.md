## CarKit

> `/System/Library/PrivateFrameworks/CarKit.framework/CarKit`

```diff

-746.11.0.0.0
-  __TEXT.__text: 0x56f7c
-  __TEXT.__auth_stubs: 0xe50
-  __TEXT.__objc_methlist: 0x5b8c
-  __TEXT.__const: 0x600
-  __TEXT.__cstring: 0x54d1
-  __TEXT.__oslogstring: 0x611a
+746.17.0.0.0
+  __TEXT.__text: 0x58908
+  __TEXT.__auth_stubs: 0xe60
+  __TEXT.__objc_methlist: 0x5d94
+  __TEXT.__const: 0x610
+  __TEXT.__cstring: 0x56b1
+  __TEXT.__oslogstring: 0x63ea
   __TEXT.__gcc_except_tab: 0xa48
   __TEXT.__ustring: 0x24
   __TEXT.__dlopen_cstrs: 0x15e

   __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_types: 0x1c
   __TEXT.__swift5_fieldmd: 0xac
-  __TEXT.__unwind_info: 0x18b8
-  __TEXT.__objc_classname: 0xacb
-  __TEXT.__objc_methname: 0x100a0
-  __TEXT.__objc_methtype: 0x234b
-  __TEXT.__objc_stubs: 0x9120
-  __DATA_CONST.__got: 0x778
-  __DATA_CONST.__const: 0x1e98
-  __DATA_CONST.__objc_classlist: 0x240
+  __TEXT.__unwind_info: 0x18f0
+  __TEXT.__objc_classname: 0xae6
+  __TEXT.__objc_methname: 0x10693
+  __TEXT.__objc_methtype: 0x23a6
+  __TEXT.__objc_stubs: 0x9480
+  __DATA_CONST.__got: 0x788
+  __DATA_CONST.__const: 0x1ea8
+  __DATA_CONST.__objc_classlist: 0x248
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3350
+  __DATA_CONST.__objc_selrefs: 0x3478
   __DATA_CONST.__objc_protorefs: 0x100
-  __DATA_CONST.__objc_superrefs: 0x1d8
-  __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x738
-  __AUTH_CONST.__const: 0x1b30
-  __AUTH_CONST.__cfstring: 0x5700
-  __AUTH_CONST.__objc_const: 0xea88
+  __DATA_CONST.__objc_superrefs: 0x1e0
+  __DATA_CONST.__objc_arraydata: 0x50
+  __AUTH_CONST.__auth_got: 0x740
+  __AUTH_CONST.__const: 0x1b50
+  __AUTH_CONST.__cfstring: 0x5920
+  __AUTH_CONST.__objc_const: 0xee08
   __AUTH_CONST.__objc_intobj: 0x108
-  __AUTH_CONST.__objc_arrayobj: 0x48
+  __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x1070
+  __AUTH.__objc_data: 0x10c0
   __AUTH.__data: 0x58
-  __DATA.__objc_ivar: 0x6c8
-  __DATA.__data: 0x1098
+  __DATA.__objc_ivar: 0x6fc
+  __DATA.__data: 0x10a8
   __DATA.__bss: 0x8d0
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x690

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 16B94777-83E6-3693-8144-D1068A1704DA
-  Functions: 2719
-  Symbols:   8929
-  CStrings:  4876
+  UUID: F088E11A-62E5-378D-8C14-01D68B7B2CDD
+  Functions: 2773
+  Symbols:   9096
+  CStrings:  4990
 
Symbols:
+ +[CRCarPlayFeatureDenyList _denyFeatureListFromPreferences]
+ +[CRCarPlayFeatureDenyList _readDenyListContentFrom:error:]
+ +[CRCarPlayFeatureDenyList _readDenyListContentFrom:error:].cold.1
+ +[CRCarPlayFeatureDenyList reloadWithURL:notify:]
+ +[CRCarPlayFeatureDenyList reloadWithURL:notify:].cold.1
+ +[CRCarPlayFeatureDenyList reloadWithURL:notify:].cold.2
+ -[CARSession handleChangeUIConfiguration:screenID:]
+ -[CARSession handleChangeUIConfiguration:screenID:].cold.1
+ -[CARSessionConfiguration routeSharingMode]
+ -[CARSessionConfiguration vehicleDataPluginConfigs]
+ -[CRCarPlayCapabilities routeSharingMode]
+ -[CRCarPlayCapabilities setRouteSharingMode:]
+ -[CRCarPlayFeatureDenyList .cxx_destruct]
+ -[CRCarPlayFeatureDenyList _featureDisabledWithIdentifier:]
+ -[CRCarPlayFeatureDenyList _featureWithName:disabledForiOSVersion:]
+ -[CRCarPlayFeatureDenyList _featureWithName:disabledForiOSVersion:].cold.1
+ -[CRCarPlayFeatureDenyList _requestDenylistUpdate]
+ -[CRCarPlayFeatureDenyList _setupConnection]
+ -[CRCarPlayFeatureDenyList connection]
+ -[CRCarPlayFeatureDenyList dealloc]
+ -[CRCarPlayFeatureDenyList featureDisabledWithUpdateHandler:]
+ -[CRCarPlayFeatureDenyList featureDisabled]
+ -[CRCarPlayFeatureDenyList featureIdentifier]
+ -[CRCarPlayFeatureDenyList featureList]
+ -[CRCarPlayFeatureDenyList handleServiceChangeNotification]
+ -[CRCarPlayFeatureDenyList handleServiceChangeNotification].cold.1
+ -[CRCarPlayFeatureDenyList initWithIdentifier:]
+ -[CRCarPlayFeatureDenyList initWithURL:]
+ -[CRCarPlayFeatureDenyList initWithURL:].cold.1
+ -[CRCarPlayFeatureDenyList observeServiceChanges]
+ -[CRCarPlayFeatureDenyList observeServiceChanges].cold.1
+ -[CRCarPlayFeatureDenyList setConnection:]
+ -[CRCarPlayFeatureDenyList setFeatureIdentifier:]
+ -[CRCarPlayFeatureDenyList setFeatureList:]
+ -[CRCarPlayFeatureDenyList setUpdateHandler:]
+ -[CRCarPlayFeatureDenyList updateHandler]
+ -[CRCarPlayPreferences isCarPlayRouteSharingEnabled].cold.1
+ -[CRVehicle _routeSharingDebugDescription]
+ -[CRVehicle hasShownRouteSharingFollowup]
+ -[CRVehicle oemName]
+ -[CRVehicle routeSharingReason]
+ -[CRVehicle routeSharingStatus]
+ -[CRVehicle setHasShownRouteSharingFollowup:]
+ -[CRVehicle setOemName:]
+ -[CRVehicle setRouteSharingReason:]
+ -[CRVehicle setRouteSharingStatus:]
+ -[CRVehicle setSupportsLodWidgets:]
+ -[CRVehicle setSupportsRouteSharing:]
+ -[CRVehicle supportsLodWidgets]
+ -[CRVehicle supportsRouteSharing]
+ GCC_except_table108
+ GCC_except_table143
+ GCC_except_table166
+ GCC_except_table172
+ GCC_except_table198
+ _CARLimitedUIValueUserInterfaceLongUserAlert
+ _CARkVehicleStateProtocolInfoKey_PluginConfigs
+ _CFStringCompare
+ _CRCarPlayFeatureDenyListChangedHandler
+ _CRRouteSharingConsentDidChangeNotification
+ _OBJC_CLASS_$_CRCarPlayFeatureDenyList
+ _OBJC_CLASS_$_NSDecimalNumber
+ _OBJC_CLASS_$_NSProcessInfo
+ _OBJC_IVAR_$_CARSessionConfiguration._routeSharingMode
+ _OBJC_IVAR_$_CARSessionConfiguration._vehicleDataPluginConfigs
+ _OBJC_IVAR_$_CRCarPlayCapabilities._routeSharingMode
+ _OBJC_IVAR_$_CRCarPlayFeatureDenyList._connection
+ _OBJC_IVAR_$_CRCarPlayFeatureDenyList._featureIdentifier
+ _OBJC_IVAR_$_CRCarPlayFeatureDenyList._featureList
+ _OBJC_IVAR_$_CRCarPlayFeatureDenyList._updateHandler
+ _OBJC_IVAR_$_CRVehicle._hasShownRouteSharingFollowup
+ _OBJC_IVAR_$_CRVehicle._oemName
+ _OBJC_IVAR_$_CRVehicle._routeSharingReason
+ _OBJC_IVAR_$_CRVehicle._routeSharingStatus
+ _OBJC_IVAR_$_CRVehicle._supportsLodWidgets
+ _OBJC_IVAR_$_CRVehicle._supportsRouteSharing
+ _OBJC_METACLASS_$_CRCarPlayFeatureDenyList
+ __OBJC_$_CLASS_METHODS_CRCarPlayFeatureDenyList
+ __OBJC_$_INSTANCE_METHODS_CRCarPlayFeatureDenyList
+ __OBJC_$_INSTANCE_VARIABLES_CRCarPlayFeatureDenyList
+ __OBJC_$_PROP_LIST_CRCarPlayFeatureDenyList
+ __OBJC_CLASS_RO_$_CRCarPlayFeatureDenyList
+ __OBJC_METACLASS_RO_$_CRCarPlayFeatureDenyList
+ ___24-[CARSession suggestUI:]_block_invoke.421
+ ___50-[CRCarPlayFeatureDenyList _requestDenylistUpdate]_block_invoke
+ ___50-[CRCarPlayFeatureDenyList _requestDenylistUpdate]_block_invoke.cold.1
+ ___55-[CARSession initWithFigEndpoint:sessionStatusOptions:]_block_invoke.358
+ ___59-[CRCarPlayFeatureDenyList handleServiceChangeNotification]_block_invoke
+ ___63+[CRCarPlayCapabilities waitForCarCapabilitiesValuesWithReply:]_block_invoke.160
+ ___63+[CRCarPlayCapabilities waitForCarCapabilitiesValuesWithReply:]_block_invoke.160.cold.1
+ ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke.614.cold.1
+ ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke.614.cold.2
+ ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke.619
+ ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke.623
+ ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke_2.624
+ ___CARHandleSuggestUI_block_invoke.417
+ ___block_literal_global.159
+ ___block_literal_global.303
+ ___block_literal_global.416
+ ___block_literal_global.426
+ ___block_literal_global.632
+ ___block_literal_global.737
+ _objc_msgSend$_denyFeatureListFromPreferences
+ _objc_msgSend$_featureDisabledWithIdentifier:
+ _objc_msgSend$_featureWithName:disabledForiOSVersion:
+ _objc_msgSend$_readDenyListContentFrom:error:
+ _objc_msgSend$_routeSharingDebugDescription
+ _objc_msgSend$decimalNumberWithString:
+ _objc_msgSend$dictionaryWithContentsOfURL:
+ _objc_msgSend$featureIdentifier
+ _objc_msgSend$featureList
+ _objc_msgSend$handleServiceChangeNotification
+ _objc_msgSend$hasShownRouteSharingFollowup
+ _objc_msgSend$isExceptionWithScreenType:physicalSize:pixelSize:
+ _objc_msgSend$observeServiceChanges
+ _objc_msgSend$operatingSystemVersion
+ _objc_msgSend$processInfo
+ _objc_msgSend$routeSharingMode
+ _objc_msgSend$routeSharingStatus
+ _objc_msgSend$session:didUpdateUIConfiguration:forScreenUUID:
+ _objc_msgSend$setFeatureList:
+ _objc_msgSend$setHasShownRouteSharingFollowup:
+ _objc_msgSend$setRouteSharingMode:
+ _objc_msgSend$setRouteSharingStatus:
+ _objc_msgSend$setSupportsLodWidgets:
+ _objc_msgSend$setSupportsRouteSharing:
+ _objc_msgSend$setUpdateHandler:
+ _objc_msgSend$supportsLodWidgets
+ _objc_msgSend$supportsRouteSharing
+ _objc_msgSend$updateHandler
- -[CRDisplayScaleInfo _customZoomEnabled]
- GCC_except_table142
- GCC_except_table165
- GCC_except_table171
- GCC_except_table197
- GCC_except_table39
- ___24-[CARSession suggestUI:]_block_invoke.419
- ___55-[CARSession initWithFigEndpoint:sessionStatusOptions:]_block_invoke.356
- ___63+[CRCarPlayCapabilities waitForCarCapabilitiesValuesWithReply:]_block_invoke.157
- ___63+[CRCarPlayCapabilities waitForCarCapabilitiesValuesWithReply:]_block_invoke.157.cold.1
- ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke.605
- ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke.605.cold.1
- ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke.605.cold.2
- ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke.610
- ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke_2.615
- ___CARHandleSuggestUI_block_invoke.415
- ___block_literal_global.156
- ___block_literal_global.300
- ___block_literal_global.414
- ___block_literal_global.424
- ___block_literal_global.620
- ___block_literal_global.734
- _objc_msgSend$_customZoomEnabled
CStrings:
+ "%@ (identifier: %@, PPID: %@, pairing: %@, startSessionRequest: %@, cluster{supported: %@ id: %@ versions{ %@, %@}, enhancedIntegration: %@, routeSharing: %@, disabledFeatures: %@, isSiriBargeInDisabled: %@, supportsMixableAudio: %@, albumArtUserPreference: %@, %@: %@, %@: %@, %@: %@, %@: %@, %@: %@, %@: %@, %@: %@)"
+ "%ld.%ld"
+ "<%@: %p> version = %@, disabledFeature = %@, nowPlayingAlbumArtMode = %@, liveActivitiesMode = %@, lodWidgetsMode = %@, routeSharingMode = %@, userInterfaceStyle = %@, viewAreaInset = %@, dashboardRoundedCorners = %@, userInfo = %@, persisted = %@, zoomFactor = %@"
+ "<%@: %p> version = %@, disabledFeature = %@, nowPlayingAlbumArtMode = %ld, liveActivitiesMode = %ld, lodWidgetsMode = %ld, routeSharingMode = %ld,userInterfaceStyle = %ld, viewAreaInset = %@, dashboardRoundedCorners = %@, userInfo = %@, persisted = %@, zoomFactor = %@"
+ "@32@0:8@16^@24"
+ "B24@0:8@?16"
+ "B24@0:8Q16"
+ "B56@0:8Q16{CGSize=dd}24{CGSize=dd}40"
+ "CRCapabilitiesRouteSharingKey"
+ "CRCarPlayFeatureDenyList"
+ "CRRouteSharingConsentDidChangeNotificationName"
+ "FeatureDenyList"
+ "FeatureDenyList: %@ result %@"
+ "FeatureDenyList: %{public}@ result %@ for %{public}@ (range)"
+ "FeatureDenyList: %{public}@ result %{public}@ (disabled)"
+ "FeatureDenyList: CarPlay denylist service error: %@"
+ "FeatureDenyList: Connecting to app denylist service."
+ "FeatureDenyList: Failed to parse CarPlay MobileAssets file"
+ "FeatureDenyList: Posting feature deny list changed"
+ "FeatureDenyList: error reading file"
+ "FeatureDenyList: loading plist"
+ "FeatureDenyList: observing change notifications"
+ "FeatureDenyList: received change notification"
+ "FeatureDenyList: sending client update block for feature %@, with result %@"
+ "Horizontal density is too low: pixelSize:%{public}@; physicalSize:%{public}@"
+ "Long User Alert"
+ "RouteSharing"
+ "T@\"NSArray\",R,C,N,V_vehicleDataPluginConfigs"
+ "T@\"NSDictionary\",&,N,V_featureList"
+ "T@\"NSNumber\",&,N,V_hasShownRouteSharingFollowup"
+ "T@\"NSNumber\",&,N,V_supportsLodWidgets"
+ "T@\"NSNumber\",&,N,V_supportsRouteSharing"
+ "T@\"NSString\",C,N,V_oemName"
+ "T@\"NSString\",C,N,V_routeSharingReason"
+ "T@?,C,N,V_updateHandler"
+ "TQ,N,V_featureIdentifier"
+ "TQ,N,V_routeSharingStatus"
+ "The screen is an exception, only optimized display scale allowed"
+ "Tq,N,V_routeSharingMode"
+ "Tq,R,N,V_routeSharingMode"
+ "UIConfiguration change: %{public}@ for screen: %{public}@"
+ "Vertical density is too low: pixelSize:%{public}@; physicalSize:%{public}@"
+ "_denyFeatureListFromPreferences"
+ "_featureDisabledWithIdentifier:"
+ "_featureIdentifier"
+ "_featureList"
+ "_featureWithName:disabledForiOSVersion:"
+ "_hasShownRouteSharingFollowup"
+ "_oemName"
+ "_readDenyListContentFrom:error:"
+ "_routeSharingDebugDescription"
+ "_routeSharingMode"
+ "_routeSharingReason"
+ "_routeSharingStatus"
+ "_supportsLodWidgets"
+ "_supportsRouteSharing"
+ "_updateHandler"
+ "_vehicleDataPluginConfigs"
+ "com.apple.carkit.app"
+ "com.apple.carkit.app.featureDenyList-changed"
+ "decimalNumberWithString:"
+ "dictionaryWithContentsOfURL:"
+ "featureDisabled"
+ "featureDisabledWithUpdateHandler:"
+ "featureIdentifier"
+ "featureList"
+ "handleChangeUIConfiguration:screenID:"
+ "handleServiceChangeNotification"
+ "hasShownRouteSharingFollowup"
+ "isExceptionWithScreenType:physicalSize:pixelSize:"
+ "longUserAlert"
+ "observeServiceChanges"
+ "oemName"
+ "operatingSystemVersion"
+ "pluginConfigs"
+ "processInfo"
+ "reloadWithURL:notify:"
+ "routeSharingMode"
+ "routeSharingReason"
+ "routeSharingStatus"
+ "session:didUpdateUIConfiguration:forScreenUUID:"
+ "setFeatureIdentifier:"
+ "setFeatureList:"
+ "setHasShownRouteSharingFollowup:"
+ "setOemName:"
+ "setRouteSharingMode:"
+ "setRouteSharingReason:"
+ "setRouteSharingStatus:"
+ "setSupportsLodWidgets:"
+ "setSupportsRouteSharing:"
+ "setUpdateHandler:"
+ "start"
+ "stop"
+ "supportsLodWidgets"
+ "supportsRouteSharing"
+ "unsupported"
+ "updateHandler"
+ "v40@0:8@\"CARSession\"16@\"NSDictionary\"24@\"NSString\"32"
+ "vehicle identifier = %@\nplist version = %@\ndisabledFeature mask = %@\nnowPlayingAlbumArtMode = %@\nliveActivitiesMode = %@\nlodWidgetsMode = %@\nrouteSharingMode = %@\nuserInterfaceStyle = %@\nviewAreaInset = %@\ndashboardRoundedCorners = %@\nuserInfo = %@, persisted = %@\nzoomFactor = %@"
+ "vehicleDataPluginConfigs"
+ "\xf0\xf0q"
- "%@ (identifier: %@, PPID: %@, pairing: %@, startSessionRequest: %@, cluster{supported: %@ id: %@ versions{ %@, %@}, enhancedIntegration: %@, disabledFeatures: %@, isSiriBargeInDisabled: %@, supportsMixableAudio: %@, albumArtUserPreference: %@, %@: %@, %@: %@, %@: %@, %@: %@, %@: %@, %@: %@, %@: %@)"
- "<%@: %p> version = %@, disabledFeature = %@, nowPlayingAlbumArtMode = %@, liveActivitiesMode = %@, lodWidgetsMode = %@, userInterfaceStyle = %@, viewAreaInset = %@, dashboardRoundedCorners = %@, userInfo = %@, persisted = %@, zoomFactor = %@"
- "<%@: %p> version = %@, disabledFeature = %@, nowPlayingAlbumArtMode = %ld, liveActivitiesMode = %ld, lodWidgetsMode = %ld, userInterfaceStyle = %ld, viewAreaInset = %@, dashboardRoundedCorners = %@, userInfo = %@, persisted = %@, zoomFactor = %@"
- "Horizontal density is too low: pixelSize:%{publiic}@; physicalSize:%{public}@"
- "Vertical density is too low: pixelSize:%{publiic}@; physicalSize:%{public}@"
- "_customZoomEnabled"
- "vehicle identifier = %@\nplist version = %@\ndisabledFeature mask = %@\nnowPlayingAlbumArtMode = %@\nliveActivitiesMode = %@\nlodWidgetsMode = %@\nuserInterfaceStyle = %@\nviewAreaInset = %@\ndashboardRoundedCorners = %@\nuserInfo = %@, persisted = %@\nzoomFactor = %@"
- "\xf0\xf0Q"

```
