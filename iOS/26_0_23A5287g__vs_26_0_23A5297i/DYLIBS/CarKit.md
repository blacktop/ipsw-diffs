## CarKit

> `/System/Library/PrivateFrameworks/CarKit.framework/CarKit`

```diff

-740.1.0.0.0
-  __TEXT.__text: 0x544ac
-  __TEXT.__auth_stubs: 0xd10
-  __TEXT.__objc_methlist: 0x5a3c
+743.0.0.0.0
+  __TEXT.__text: 0x547dc
+  __TEXT.__auth_stubs: 0xd20
+  __TEXT.__objc_methlist: 0x5abc
   __TEXT.__const: 0x42a
-  __TEXT.__cstring: 0x52a1
-  __TEXT.__oslogstring: 0x5e9f
+  __TEXT.__cstring: 0x52d1
+  __TEXT.__oslogstring: 0x5ea0
   __TEXT.__gcc_except_tab: 0xa44
   __TEXT.__ustring: 0x24
   __TEXT.__dlopen_cstrs: 0x15e

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x17e0
-  __TEXT.__objc_classname: 0xab6
-  __TEXT.__objc_methname: 0xfc53
-  __TEXT.__objc_methtype: 0x22f1
-  __TEXT.__objc_stubs: 0x8fe0
-  __DATA_CONST.__got: 0x760
+  __TEXT.__unwind_info: 0x1800
+  __TEXT.__objc_classname: 0xacc
+  __TEXT.__objc_methname: 0xfd85
+  __TEXT.__objc_methtype: 0x2302
+  __TEXT.__objc_stubs: 0x9060
+  __DATA_CONST.__got: 0x768
   __DATA_CONST.__const: 0x1e70
-  __DATA_CONST.__objc_classlist: 0x230
+  __DATA_CONST.__objc_classlist: 0x238
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x32c8
+  __DATA_CONST.__objc_selrefs: 0x32f8
   __DATA_CONST.__objc_protorefs: 0x100
-  __DATA_CONST.__objc_superrefs: 0x1d0
-  __DATA_CONST.__objc_arraydata: 0x58
-  __AUTH_CONST.__auth_got: 0x698
+  __DATA_CONST.__objc_superrefs: 0x1d8
+  __DATA_CONST.__objc_arraydata: 0x48
+  __AUTH_CONST.__auth_got: 0x6a0
   __AUTH_CONST.__const: 0x1740
-  __AUTH_CONST.__cfstring: 0x55e0
-  __AUTH_CONST.__objc_const: 0xe938
+  __AUTH_CONST.__cfstring: 0x5620
+  __AUTH_CONST.__objc_const: 0xea38
   __AUTH_CONST.__objc_intobj: 0x108
-  __AUTH_CONST.__objc_arrayobj: 0x60
+  __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0xf70
+  __AUTH.__objc_data: 0xfc0
   __AUTH.__data: 0x30
-  __DATA.__objc_ivar: 0x6c4
-  __DATA.__data: 0x1060
+  __DATA.__objc_ivar: 0x6cc
+  __DATA.__data: 0x1070
   __DATA.__bss: 0x520
   __DATA_DIRTY.__objc_data: 0x690
   __DATA_DIRTY.__bss: 0x110

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 769A30D6-0144-3919-BDF2-30EFECBF20D5
-  Functions: 2612
-  Symbols:   8783
-  CStrings:  4818
+  UUID: 9B9905EF-AE9E-381C-A2E9-44B6A28C067F
+  Functions: 2623
+  Symbols:   8821
+  CStrings:  4832
 
Symbols:
+ -[CARScreenInfo(CRDisplayScaling) allowsSmartZoom]
+ -[CARSession createRemoteControlSession:channelID:withoutReply:sendAsIs:qualityOfService:streamPriority:error:]
+ -[CARSession createRemoteControlSession:channelID:withoutReply:sendAsIs:qualityOfService:streamPriority:error:].cold.1
+ -[CARSession createRemoteControlSession:channelID:withoutReply:sendAsIs:qualityOfService:streamPriority:error:].cold.2
+ -[CARSession createRemoteControlSession:channelID:withoutReply:sendAsIs:qualityOfService:streamPriority:error:].cold.3
+ -[CARSession createRemoteControlSession:channelID:withoutReply:sendAsIs:qualityOfService:streamPriority:error:].cold.4
+ -[CARSessionChannel initWithSession:channelType:channelID:withoutReply:sendAsIs:qualityOfService:streamPriority:]
+ -[CARSessionChannel sendAsIs]
+ -[CARThemeAssetLibraryAgent notifyFoundNoMatchingAssetForVehicleIdentifier:nextRequiredCompatibilityVersion:requestDescription:]
+ -[CARThemeAssetLibraryObserverProxy service_foundNoMatchingAssetForVehicleIdentifier:nextRequiredCompatibilityVersion:reply:]
+ -[CRCarPlayLiveActivityDenyList .cxx_destruct]
+ -[CRCarPlayLiveActivityDenyList _updateDenyListFromPreferences]
+ -[CRCarPlayLiveActivityDenyList containsBundleIdentifier:]
+ -[CRCarPlayLiveActivityDenyList denyListBundleIdentifiersSet]
+ -[CRCarPlayLiveActivityDenyList handleLiveActivityDenyListChangedNotification:]
+ -[CRCarPlayLiveActivityDenyList init]
+ -[CRCarPlayLiveActivityDenyList setDenyListBundleIdentifiers:]
+ -[CRCarPlayLiveActivityDenyList setDenyListBundleIdentifiersSet:]
+ -[CRCarPlayWidgetDenyList .cxx_destruct]
+ -[CRCarPlayWidgetDenyList _updateDenyListFromPreferences]
+ -[CRCarPlayWidgetDenyList denyListExtensionsSet]
+ -[CRCarPlayWidgetDenyList denyListExtensions]
+ -[CRCarPlayWidgetDenyList handleWidgetDenylistChangedNotification:]
+ -[CRCarPlayWidgetDenyList init]
+ -[CRCarPlayWidgetDenyList setDenyListExtensions:]
+ -[CRCarPlayWidgetDenyList setDenyListExtensionsSet:]
+ -[CRDisplayScaleInfo _allowedScaleModes]
+ -[CRDisplayScaleInfo allowsSmartZoom]
+ _CRCarPlayLiveActivityDenyListPreferenceKey
+ _CRCarPlayWidgetDenyListPreferenceKey
+ _OBJC_CLASS_$_CRCarPlayLiveActivityDenyList
+ _OBJC_CLASS_$_CRCarPlayWidgetDenyList
+ _OBJC_IVAR_$_CARSessionChannel._sendAsIs
+ _OBJC_IVAR_$_CRCarPlayLiveActivityDenyList._denyListBundleIdentifiersSet
+ _OBJC_IVAR_$_CRCarPlayWidgetDenyList._denyListExtensionsSet
+ _OBJC_METACLASS_$_CRCarPlayLiveActivityDenyList
+ _OBJC_METACLASS_$_CRCarPlayWidgetDenyList
+ __OBJC_$_INSTANCE_METHODS_CRCarPlayLiveActivityDenyList
+ __OBJC_$_INSTANCE_METHODS_CRCarPlayWidgetDenyList
+ __OBJC_$_INSTANCE_VARIABLES_CRCarPlayLiveActivityDenyList
+ __OBJC_$_INSTANCE_VARIABLES_CRCarPlayWidgetDenyList
+ __OBJC_$_PROP_LIST_CRCarPlayLiveActivityDenyList
+ __OBJC_$_PROP_LIST_CRCarPlayWidgetDenyList
+ __OBJC_CLASS_RO_$_CRCarPlayLiveActivityDenyList
+ __OBJC_CLASS_RO_$_CRCarPlayWidgetDenyList
+ __OBJC_METACLASS_RO_$_CRCarPlayLiveActivityDenyList
+ __OBJC_METACLASS_RO_$_CRCarPlayWidgetDenyList
+ ___111-[CARSession createRemoteControlSession:channelID:withoutReply:sendAsIs:qualityOfService:streamPriority:error:]_block_invoke
+ ___125-[CARThemeAssetLibraryObserverProxy service_foundNoMatchingAssetForVehicleIdentifier:nextRequiredCompatibilityVersion:reply:]_block_invoke
+ ___128-[CARThemeAssetLibraryAgent notifyFoundNoMatchingAssetForVehicleIdentifier:nextRequiredCompatibilityVersion:requestDescription:]_block_invoke
+ ___128-[CARThemeAssetLibraryAgent notifyFoundNoMatchingAssetForVehicleIdentifier:nextRequiredCompatibilityVersion:requestDescription:]_block_invoke_2
+ ___67-[CRCarPlayWidgetDenyList handleWidgetDenylistChangedNotification:]_block_invoke
+ ___79-[CRCarPlayLiveActivityDenyList handleLiveActivityDenyListChangedNotification:]_block_invoke
+ ___block_literal_global.230
+ ___block_literal_global.235
+ _kFigEndpointRemoteControlSessionClientTypeUUIDKey_FitnessUIOverlay
+ _objc_msgSend$_allowedScaleModes
+ _objc_msgSend$allowsSmartZoom
+ _objc_msgSend$createRemoteControlSession:channelID:withoutReply:sendAsIs:qualityOfService:streamPriority:error:
+ _objc_msgSend$denyListExtensionsSet
+ _objc_msgSend$initWithSession:channelType:channelID:withoutReply:sendAsIs:qualityOfService:streamPriority:
+ _objc_msgSend$sendAsIs
+ _objc_msgSend$service_foundNoMatchingAssetForVehicleIdentifier:nextRequiredCompatibilityVersion:reply:
+ _objc_retain_x7
- -[CARScreenInfo(CRDisplayScaling) allowedDisplayScaleModes]
- -[CARSession createRemoteControlSession:channelID:withoutReply:qualityOfService:streamPriority:error:]
- -[CARSession createRemoteControlSession:channelID:withoutReply:qualityOfService:streamPriority:error:].cold.1
- -[CARSession createRemoteControlSession:channelID:withoutReply:qualityOfService:streamPriority:error:].cold.2
- -[CARSession createRemoteControlSession:channelID:withoutReply:qualityOfService:streamPriority:error:].cold.3
- -[CARSession createRemoteControlSession:channelID:withoutReply:qualityOfService:streamPriority:error:].cold.4
- -[CARThemeAssetLibraryAgent notifyFoundNoMatchingAssetForAssetIdentifier:nextRequiredCompatibilityVersion:requestDescription:]
- -[CARThemeAssetLibraryObserverProxy service_foundNoMatchingAssetForAssetIdentifier:nextRequiredCompatibilityVersion:reply:]
- -[CRCarPlayLiveActivitiesDenylist .cxx_destruct]
- -[CRCarPlayLiveActivitiesDenylist _updateDenyListFromPreferences]
- -[CRCarPlayLiveActivitiesDenylist containsBundleIdentifier:]
- -[CRCarPlayLiveActivitiesDenylist denyListBundleIdentifiersSet]
- -[CRCarPlayLiveActivitiesDenylist handleLiveActivitiesDenylistChangedNotification:]
- -[CRCarPlayLiveActivitiesDenylist init]
- -[CRCarPlayLiveActivitiesDenylist setDenyListBundleIdentifiers:]
- -[CRCarPlayLiveActivitiesDenylist setDenyListBundleIdentifiersSet:]
- -[CRDisplayScaleInfo allowedScaleModes]
- -[CRDisplayScaleInfo pointScaleForMode:]
- _CRCarPlayLiveActivitiesDenylistPreferenceKey
- _OBJC_CLASS_$_CRCarPlayLiveActivitiesDenylist
- _OBJC_IVAR_$_CRCarPlayLiveActivitiesDenylist._denyListBundleIdentifiersSet
- _OBJC_METACLASS_$_CRCarPlayLiveActivitiesDenylist
- __OBJC_$_INSTANCE_METHODS_CRCarPlayLiveActivitiesDenylist
- __OBJC_$_INSTANCE_VARIABLES_CRCarPlayLiveActivitiesDenylist
- __OBJC_$_PROP_LIST_CRCarPlayLiveActivitiesDenylist
- __OBJC_CLASS_RO_$_CRCarPlayLiveActivitiesDenylist
- __OBJC_METACLASS_RO_$_CRCarPlayLiveActivitiesDenylist
- ___102-[CARSession createRemoteControlSession:channelID:withoutReply:qualityOfService:streamPriority:error:]_block_invoke
- ___123-[CARThemeAssetLibraryObserverProxy service_foundNoMatchingAssetForAssetIdentifier:nextRequiredCompatibilityVersion:reply:]_block_invoke
- ___126-[CARThemeAssetLibraryAgent notifyFoundNoMatchingAssetForAssetIdentifier:nextRequiredCompatibilityVersion:requestDescription:]_block_invoke
- ___126-[CARThemeAssetLibraryAgent notifyFoundNoMatchingAssetForAssetIdentifier:nextRequiredCompatibilityVersion:requestDescription:]_block_invoke_2
- ___83-[CRCarPlayLiveActivitiesDenylist handleLiveActivitiesDenylistChangedNotification:]_block_invoke
- ___block_literal_global.221
- ___block_literal_global.227
- ___block_literal_global.232
- ___block_literal_global.237
- _objc_msgSend$allowedScaleModes
- _objc_msgSend$createRemoteControlSession:channelID:withoutReply:qualityOfService:streamPriority:error:
- _objc_msgSend$service_foundNoMatchingAssetForAssetIdentifier:nextRequiredCompatibilityVersion:reply:
CStrings:
+ "@64@0:8@16@24@32B40B44@48@56"
+ "Allowed scale modes: defaultSize:%{public}@, optimizedSize:%{public}@; Original equals to default?: %{public}@"
+ "CRCarPlayLiveActivityDenyList"
+ "CRCarPlayWidgetDenyList"
+ "LiveActivityDenyList"
+ "T@\"NSSet\",&,N,V_denyListExtensionsSet"
+ "TB,R,N,V_sendAsIs"
+ "WidgetDenylist"
+ "^{OpaqueFigEndpointRemoteControlSession=}64@0:8@16@24B32B36@40@48^@56"
+ "_allowedScaleModes"
+ "_denyListExtensionsSet"
+ "_sendAsIs"
+ "allowsSmartZoom"
+ "com.apple.carkit.liveactivity.denylist-changed"
+ "com.apple.carkit.widget.denylist-changed"
+ "createRemoteControlSession:channelID:withoutReply:sendAsIs:qualityOfService:streamPriority:error:"
+ "denyListExtensions"
+ "denyListExtensionsSet"
+ "handleLiveActivityDenyListChangedNotification:"
+ "handleWidgetDenylistChangedNotification:"
+ "initWithSession:channelType:channelID:withoutReply:sendAsIs:qualityOfService:streamPriority:"
+ "notifyFoundNoMatchingAssetForVehicleIdentifier:nextRequiredCompatibilityVersion:requestDescription:"
+ "sendAsIs"
+ "service_foundNoMatchingAssetForVehicleIdentifier:nextRequiredCompatibilityVersion:reply:"
+ "setDenyListExtensions:"
+ "setDenyListExtensionsSet:"
+ "v40@0:8@\"NSUUID\"16@\"NSNumber\"24@\"NSString\"32"
+ "v40@0:8@\"NSUUID\"16@\"NSNumber\"24@?<v@?>32"
- "Allowed scale modes: defaultSize:%{public}@, optimizedSize:%{public}@; Original equals to default: %{public}@"
- "CRCarPlayLiveActivitiesDenylist"
- "Credenza"
- "LiveActivitiesDenylist"
- "^{OpaqueFigEndpointRemoteControlSession=}60@0:8@16@24B32@36@44^@52"
- "allowedDisplayScaleModes"
- "allowedScaleModes"
- "com.apple.carkit.liveactivities.denylist-changed"
- "createRemoteControlSession:channelID:withoutReply:qualityOfService:streamPriority:error:"
- "d24@0:8q16"
- "handleLiveActivitiesDenylistChangedNotification:"
- "notifyFoundNoMatchingAssetForAssetIdentifier:nextRequiredCompatibilityVersion:requestDescription:"
- "pointScaleForMode:"
- "service_foundNoMatchingAssetForAssetIdentifier:nextRequiredCompatibilityVersion:reply:"
- "v40@0:8@\"NSString\"16@\"NSNumber\"24@\"NSString\"32"
- "v40@0:8@\"NSString\"16@\"NSNumber\"24@?<v@?>32"

```
