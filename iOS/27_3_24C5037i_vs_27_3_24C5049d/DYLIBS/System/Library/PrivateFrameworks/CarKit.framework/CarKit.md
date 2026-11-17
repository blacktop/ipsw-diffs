## CarKit

> `/System/Library/PrivateFrameworks/CarKit.framework/CarKit`

```diff

-808.6.0.0.0
-  __TEXT.__text: 0x61278
-  __TEXT.__objc_methlist: 0x64a4
-  __TEXT.__const: 0x558
+808.9.1.0.0
+  __TEXT.__text: 0x61b1c
+  __TEXT.__objc_methlist: 0x65e4
+  __TEXT.__const: 0x568
   __TEXT.__gcc_except_tab: 0xa44
   __TEXT.__oslogstring: 0x6e16
-  __TEXT.__cstring: 0x5bbd
+  __TEXT.__cstring: 0x5cdd
   __TEXT.__dlopen_cstrs: 0x15e
   __TEXT.__constg_swiftt: 0x1a0
   __TEXT.__swift5_typeref: 0x17e

   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x10
-  __TEXT.__unwind_info: 0x2658
+  __TEXT.__unwind_info: 0x26a0
   __TEXT.__eh_frame: 0x80
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x20f0
-  __DATA_CONST.__objc_classlist: 0x280
+  __DATA_CONST.__objc_classlist: 0x288
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x37c8
+  __DATA_CONST.__objc_selrefs: 0x3880
   __DATA_CONST.__objc_protorefs: 0x108
-  __DATA_CONST.__objc_superrefs: 0x1e0
+  __DATA_CONST.__objc_superrefs: 0x1e8
   __DATA_CONST.__objc_arraydata: 0xc0
-  __DATA_CONST.__got: 0x8a8
+  __DATA_CONST.__got: 0x8b0
   __AUTH_CONST.__const: 0x1bc0
-  __AUTH_CONST.__cfstring: 0x5da0
-  __AUTH_CONST.__objc_const: 0x10548
+  __AUTH_CONST.__cfstring: 0x5e60
+  __AUTH_CONST.__objc_const: 0x10750
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0xad0
-  __AUTH.__objc_data: 0x1450
+  __AUTH.__objc_data: 0x14a0
   __AUTH.__data: 0x188
-  __DATA.__objc_ivar: 0x744
+  __DATA.__objc_ivar: 0x758
   __DATA.__data: 0x1190
   __DATA_DIRTY.__objc_data: 0x640
   __DATA_DIRTY.__data: 0x30

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3080
-  Symbols:   4795
-  CStrings:  1447
+  Functions: 3106
+  Symbols:   4834
+  CStrings:  1453
 
Symbols:
+ +[CRCarPlayFeatureDenyList _featureDisabledWithIdentifier:inFeatureList:]
+ +[CRCarPlayFeatureDenyList _featureWithName:disabledForiOSVersion:inFeatureList:]
+ +[CRCarPlayFeatureDenyList featureDisabledForIdentifier:]
+ +[CRCarPlayPreferences isAppIntegrationOptionsEnabled]
+ +[CRCarPlayPreferences setAppIntegrationOptionsEnabled:]
+ +[CRVehicleMessagingSupport supportWithHandling:handlingWithAI:]
+ -[CARSessionConfiguration appIntegrationOptionsMode]
+ -[CRCarPlayCapabilities appIntegrationOptionsMode]
+ -[CRCarPlayCapabilities setAppIntegrationOptionsMode:]
+ -[CRVehicle contactsSyncStatus]
+ -[CRVehicle hasAcceptedVehicleHandlesMessagingWithAIPrompt]
+ -[CRVehicle setContactsSyncStatus:]
+ -[CRVehicle setHasAcceptedVehicleHandlesMessagingWithAIPrompt:]
+ -[CRVehicle setSupportsVehicleHandlesMessagingWithAI:]
+ -[CRVehicle setVehicleHandlesMessagingWithAIStatus:]
+ -[CRVehicle setVehicleMessagingSelection:]
+ -[CRVehicle supportsVehicleHandlesMessagingWithAI]
+ -[CRVehicle vehicleHandlesMessagingWithAIStatus]
+ -[CRVehicle vehicleMessagingSelection]
+ -[CRVehicle vehicleMessagingSupport]
+ -[CRVehicleMessagingSupport builtInSelection]
+ -[CRVehicleMessagingSupport description]
+ -[CRVehicleMessagingSupport initWithHandling:handlingWithAI:]
+ -[CRVehicleMessagingSupport isAIOptional]
+ -[CRVehicleMessagingSupport kind]
+ -[CRVehicleMessagingSupport offersAI]
+ -[CRVehicleMessagingSupport offersBuiltIn]
+ -[CRVehicleMessagingSupport selectionForAIPromptAccepted:]
+ -[CRVehicleMessagingSupport supportedSelectionForSelection:]
+ GCC_except_table40
+ _OBJC_CLASS_$_CRVehicleMessagingSupport
+ _OBJC_IVAR_$_CARSessionConfiguration._appIntegrationOptionsMode
+ _OBJC_IVAR_$_CRCarPlayCapabilities._appIntegrationOptionsMode
+ _OBJC_IVAR_$_CRVehicle._contactsSyncStatus
+ _OBJC_IVAR_$_CRVehicle._hasAcceptedVehicleHandlesMessagingWithAIPrompt
+ _OBJC_IVAR_$_CRVehicle._supportsVehicleHandlesMessagingWithAI
+ _OBJC_IVAR_$_CRVehicle._vehicleHandlesMessagingWithAIStatus
+ _OBJC_IVAR_$_CRVehicleMessagingSupport._kind
+ _OBJC_METACLASS_$_CRVehicleMessagingSupport
+ __OBJC_$_CLASS_METHODS_CRVehicleMessagingSupport
+ __OBJC_$_CLASS_PROP_LIST_CRCarPlayPreferences
+ __OBJC_$_INSTANCE_METHODS_CRVehicleMessagingSupport
+ __OBJC_$_INSTANCE_VARIABLES_CRVehicleMessagingSupport
+ __OBJC_$_PROP_LIST_CRVehicleMessagingSupport
+ __OBJC_CLASS_RO_$_CRVehicleMessagingSupport
+ __OBJC_METACLASS_RO_$_CRVehicleMessagingSupport
- -[CRVehicle setSupportsVehicleMessageAIProcessing:]
- -[CRVehicle setVehicleMessageAIProcessingStatus:]
- -[CRVehicle supportsVehicleMessageAIProcessing]
- -[CRVehicle vehicleMessageAIProcessingStatus]
- GCC_except_table37
- _OBJC_IVAR_$_CRVehicle._supportsVehicleMessageAIProcessing
- _OBJC_IVAR_$_CRVehicle._vehicleMessageAIProcessingStatus
CStrings:
+ "<%@: %p kind: %lu>"
+ "<%@: %p> version = %@, disabledFeature = %@, nowPlayingAlbumArtMode = %@, liveActivitiesMode = %@, lodWidgetsMode = %@, routeSharingMode = %@, appIntegrationOptionsMode = %@, userInterfaceStyle = %@, viewAreaInset = %@, dashboardRoundedCorners = %@, userInfo = %@, persisted = %@, zoomFactor = %@, zoomFactorByDisplayIndex = %@, hideSmartZoom = %@"
+ "<%@: %p> version = %@, disabledFeature = %@, nowPlayingAlbumArtMode = %ld, liveActivitiesMode = %ld, lodWidgetsMode = %ld, routeSharingMode = %ld, appIntegrationOptionsMode = %ld,userInterfaceStyle = %ld, viewAreaInset = %@, dashboardRoundedCorners = %@, userInfo = %@, persisted = %@, zoomFactor = %@, zoomFactorByDisplayIndex = %@, hideSmartZoom = %@"
+ "AppIntegrationOptions"
+ "CRCapabilitiesAppIntegrationOptionsKey"
+ "EnableAppIntegrationOptions"
+ "contactsSyncStatus"
+ "hasAcceptedVehicleHandlesMessagingWithAIPrompt"
+ "supportsVehicleHandlesMessagingWithAI"
+ "vehicle identifier = %@\nplist version = %@\ndisabledFeature mask = %@\nnowPlayingAlbumArtMode = %@\nliveActivitiesMode = %@\nlodWidgetsMode = %@\nrouteSharingMode = %@\nappIntegrationOptionsMode = %@\nuserInterfaceStyle = %@\nviewAreaInset = %@\ndashboardRoundedCorners = %@\nuserInfo = %@, persisted = %@\nzoomFactor = %@\nzoomFactorByDisplayIndex = %@\nhideSmartZoom = %@"
+ "vehicleHandlesMessagingWithAIStatus"
+ "\xf0\xf0\xa1"
- "<%@: %p> version = %@, disabledFeature = %@, nowPlayingAlbumArtMode = %@, liveActivitiesMode = %@, lodWidgetsMode = %@, routeSharingMode = %@, userInterfaceStyle = %@, viewAreaInset = %@, dashboardRoundedCorners = %@, userInfo = %@, persisted = %@, zoomFactor = %@, zoomFactorByDisplayIndex = %@, hideSmartZoom = %@"
- "<%@: %p> version = %@, disabledFeature = %@, nowPlayingAlbumArtMode = %ld, liveActivitiesMode = %ld, lodWidgetsMode = %ld, routeSharingMode = %ld,userInterfaceStyle = %ld, viewAreaInset = %@, dashboardRoundedCorners = %@, userInfo = %@, persisted = %@, zoomFactor = %@, zoomFactorByDisplayIndex = %@, hideSmartZoom = %@"
- "supportsVehicleMessageAIProcessing"
- "vehicle identifier = %@\nplist version = %@\ndisabledFeature mask = %@\nnowPlayingAlbumArtMode = %@\nliveActivitiesMode = %@\nlodWidgetsMode = %@\nrouteSharingMode = %@\nuserInterfaceStyle = %@\nviewAreaInset = %@\ndashboardRoundedCorners = %@\nuserInfo = %@, persisted = %@\nzoomFactor = %@\nzoomFactorByDisplayIndex = %@\nhideSmartZoom = %@"
- "vehicleMessageAIProcessingStatus"
- "\xf0\xf0\x91"
```
