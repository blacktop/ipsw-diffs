## TelephonyUtilities

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`

### Sections with Same Size but Changed Content

- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_reflstr`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-1614.100.3.2.1
-  __TEXT.__text: 0x19db34
-  __TEXT.__objc_methlist: 0x1b630
-  __TEXT.__cstring: 0x14236
-  __TEXT.__const: 0x40a8
-  __TEXT.__oslogstring: 0x13b77
-  __TEXT.__gcc_except_tab: 0x181c
+1616.100.2.2.1
+  __TEXT.__text: 0x19b298
+  __TEXT.__objc_methlist: 0x1b300
+  __TEXT.__cstring: 0x13f76
+  __TEXT.__const: 0x40c8
+  __TEXT.__oslogstring: 0x13897
+  __TEXT.__gcc_except_tab: 0x1788
   __TEXT.__ustring: 0xde
-  __TEXT.__dlopen_cstrs: 0x8df
+  __TEXT.__dlopen_cstrs: 0x845
   __TEXT.__constg_swiftt: 0xcc0
   __TEXT.__swift5_typeref: 0x103d
   __TEXT.__swift5_builtin: 0xb4
   __TEXT.__swift5_reflstr: 0xa29
   __TEXT.__swift5_fieldmd: 0x1068
   __TEXT.__swift5_assocty: 0xa8
-  __TEXT.__swift5_proto: 0x360
+  __TEXT.__swift5_proto: 0x364
   __TEXT.__swift5_types: 0x124
   __TEXT.__swift5_capture: 0x1d0
   __TEXT.__swift_as_entry: 0x94

   __TEXT.__swift_as_cont: 0x13c
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x6d50
-  __TEXT.__eh_frame: 0x2040
+  __TEXT.__unwind_info: 0x6c80
+  __TEXT.__eh_frame: 0x2078
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x37d8
-  __DATA_CONST.__objc_classlist: 0x888
+  __DATA_CONST.__const: 0x37b0
+  __DATA_CONST.__objc_classlist: 0x878
   __DATA_CONST.__objc_catlist: 0xb8
-  __DATA_CONST.__objc_protolist: 0x420
+  __DATA_CONST.__objc_protolist: 0x408
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb7c0
+  __DATA_CONST.__objc_selrefs: 0xb5e0
   __DATA_CONST.__objc_protorefs: 0x110
-  __DATA_CONST.__objc_superrefs: 0x6e8
-  __DATA_CONST.__objc_arraydata: 0xa00
-  __DATA_CONST.__got: 0xff8
-  __AUTH_CONST.__const: 0x46d8
-  __AUTH_CONST.__cfstring: 0x125a0
-  __AUTH_CONST.__objc_const: 0x2af38
+  __DATA_CONST.__objc_superrefs: 0x6d8
+  __DATA_CONST.__objc_arraydata: 0x9e8
+  __DATA_CONST.__got: 0xff0
+  __AUTH_CONST.__const: 0x46f8
+  __AUTH_CONST.__cfstring: 0x124c0
+  __AUTH_CONST.__objc_const: 0x2aa48
   __AUTH_CONST.__objc_intobj: 0x540
-  __AUTH_CONST.__objc_arrayobj: 0x2d0
   __AUTH_CONST.__objc_doubleobj: 0x40
-  __AUTH_CONST.__auth_got: 0x14f8
-  __AUTH.__objc_data: 0x2fd8
+  __AUTH_CONST.__objc_arrayobj: 0x2b8
+  __AUTH_CONST.__auth_got: 0x1500
+  __AUTH.__objc_data: 0x2f38
   __AUTH.__data: 0xc30
-  __DATA.__objc_ivar: 0x1900
-  __DATA.__data: 0x3d58
-  __DATA.__bss: 0x7650
+  __DATA.__objc_ivar: 0x18dc
+  __DATA.__data: 0x3c38
+  __DATA.__bss: 0x7610
   __DATA.__common: 0x88
   __DATA_DIRTY.__objc_data: 0x26f0
   __DATA_DIRTY.__data: 0x58

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11544
-  Symbols:   20459
-  CStrings:  4603
+  Functions: 11471
+  Symbols:   20287
+  CStrings:  4563
 
Symbols:
+ +[TUHardwareControlsBroadcaster hidServiceMatchingDictionaries]
+ -[TUConfigurationProvider numberForKeyHierarchy:subscriptionContext:error:]
+ -[TUConversation dealloc]
+ -[TUConversation didRegisterContactStoreObserver]
+ -[TUConversation setDidRegisterContactStoreObserver:]
+ GCC_except_table208
+ GCC_except_table91
+ _OBJC_IVAR_$_TUConversation._didRegisterContactStoreObserver
+ _TUBundleIdentifierPreferences
+ __OBJC_$_CLASS_METHODS_TUHardwareControlsBroadcaster
+ _objc_msgSend$hidServiceMatchingDictionaries
+ _objc_msgSend$numberForKeyHierarchy:subscriptionContext:error:
- -[TUCall requiresRemoteVideo]
- -[TUCall setLocalVideoLayer:forMode:]
- -[TUCall setRemoteVideoLayer:forMode:]
- -[TUCall setRequiresRemoteVideo:]
- -[TUFeatureFlags outgoingCallCallerIDEnabled]
- -[TUProxyCall _cameraTypeForVideoAttributeCamera:]
- -[TUProxyCall _createLocalVideoIfNecessary]
- -[TUProxyCall _createRemoteVideoIfNecessary]
- -[TUProxyCall _orientationForVideoAttributesOrientation:]
- -[TUProxyCall _synchronizeLocalVideo]
- -[TUProxyCall _synchronizeRemoteVideo]
- -[TUProxyCall avcRemoteVideoModeForMode:]
- -[TUProxyCall localVideo]
- -[TUProxyCall remoteVideoClient:remoteMediaDidStall:]
- -[TUProxyCall remoteVideoClient:remoteScreenAttributesDidChange:]
- -[TUProxyCall remoteVideoClient:remoteVideoAttributesDidChange:]
- -[TUProxyCall remoteVideoClient:remoteVideoDidPause:]
- -[TUProxyCall remoteVideoClient:videoDidDegrade:]
- -[TUProxyCall remoteVideoModeToLayer]
- -[TUProxyCall remoteVideo]
- -[TUProxyCall requiresRemoteVideo]
- -[TUProxyCall setLocalVideo:]
- -[TUProxyCall setLocalVideoLayer:forMode:]
- -[TUProxyCall setRemoteVideo:]
- -[TUProxyCall setRemoteVideoLayer:forMode:]
- -[TUProxyCall setRemoteVideoModeToLayer:]
- -[TUProxyCall setRequiresRemoteVideo:]
- -[TUProxyCall setVideoCaptureModeToLayer:]
- -[TUProxyCall videoCaptureModeToLayer]
- -[TURemoteVideoClient .cxx_destruct]
- -[TURemoteVideoClient cleanUpSubLayerForLayer:]
- -[TURemoteVideoClient initWithVideoContextSlotIdentifier:]
- -[TURemoteVideoClient init]
- -[TURemoteVideoClient insertSubLayerInLayer:videoSlotIdentifier:]
- -[TURemoteVideoClient nameForSubLayer]
- -[TURemoteVideoClient setVideoLayer:]
- -[TURemoteVideoClient setVideoLayer:forMode:]
- -[TURemoteVideoClient videoContextSlotIdentifier]
- -[TURemoteVideoClient videoLayer]
- -[TUVideoDeviceController availableVideoEffects]
- -[TUVideoDeviceController currentVideoEffect]
- -[TUVideoDeviceController setCurrentVideoEffect:]
- -[TUVideoDeviceControllerProvider availableVideoEffects]
- -[TUVideoDeviceControllerProvider currentVideoEffect]
- -[TUVideoDeviceControllerProvider setCurrentVideoEffect:]
- -[TUVideoDeviceControllerProvider thumbnailImageForVideoEffectName:]
- -[TUVideoEffect .cxx_destruct]
- -[TUVideoEffect hash]
- -[TUVideoEffect initWithName:thumbnailImage:]
- -[TUVideoEffect init]
- -[TUVideoEffect isEqual:]
- -[TUVideoEffect isEqualToEffect:]
- -[TUVideoEffect name]
- -[TUVideoEffect thumbnailImage]
- GCC_except_table205
- GCC_except_table94
- _CoreGraphicsLibraryCore.frameworkLibrary
- _OBJC_CLASS_$_TURemoteVideoClient
- _OBJC_CLASS_$_TUVideoEffect
- _OBJC_IVAR_$_TUProxyCall._localVideo
- _OBJC_IVAR_$_TUProxyCall._remoteVideo
- _OBJC_IVAR_$_TUProxyCall._remoteVideoModeToLayer
- _OBJC_IVAR_$_TUProxyCall._requiresRemoteVideo
- _OBJC_IVAR_$_TUProxyCall._videoCaptureModeToLayer
- _OBJC_IVAR_$_TURemoteVideoClient._videoContextSlotIdentifier
- _OBJC_IVAR_$_TURemoteVideoClient._videoLayer
- _OBJC_IVAR_$_TUVideoDeviceControllerProvider._currentVideoEffect
- _OBJC_IVAR_$_TUVideoEffect._name
- _OBJC_IVAR_$_TUVideoEffect._thumbnailImage
- _OBJC_METACLASS_$_TURemoteVideoClient
- _OBJC_METACLASS_$_TUVideoEffect
- _QuartzCoreLibrary
- _QuartzCoreLibraryCore.frameworkLibrary
- __OBJC_$_INSTANCE_METHODS_TURemoteVideoClient
- __OBJC_$_INSTANCE_METHODS_TUVideoEffect
- __OBJC_$_INSTANCE_VARIABLES_TURemoteVideoClient
- __OBJC_$_INSTANCE_VARIABLES_TUVideoEffect
- __OBJC_$_PROP_LIST_TURemoteVideoClient
- __OBJC_$_PROP_LIST_TUVideoEffect
- __OBJC_$_PROP_LIST_TUVideoEffectsProvider
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_AVCRemoteVideoClientDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_TURemoteVideoClient
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_TUVideoEffectsProvider
- __OBJC_$_PROTOCOL_METHOD_TYPES_AVCRemoteVideoClientDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_TURemoteVideoClient
- __OBJC_$_PROTOCOL_METHOD_TYPES_TUVideoEffectsProvider
- __OBJC_$_PROTOCOL_REFS_AVCRemoteVideoClientDelegate
- __OBJC_$_PROTOCOL_REFS_TURemoteVideoClient
- __OBJC_$_PROTOCOL_REFS_TUVideoEffectsProvider
- __OBJC_CLASS_PROTOCOLS_$_TURemoteVideoClient
- __OBJC_CLASS_RO_$_TURemoteVideoClient
- __OBJC_CLASS_RO_$_TUVideoEffect
- __OBJC_LABEL_PROTOCOL_$_AVCRemoteVideoClientDelegate
- __OBJC_LABEL_PROTOCOL_$_TURemoteVideoClient
- __OBJC_LABEL_PROTOCOL_$_TUVideoEffectsProvider
- __OBJC_METACLASS_RO_$_TURemoteVideoClient
- __OBJC_METACLASS_RO_$_TUVideoEffect
- __OBJC_PROTOCOL_$_AVCRemoteVideoClientDelegate
- __OBJC_PROTOCOL_$_TURemoteVideoClient
- __OBJC_PROTOCOL_$_TUVideoEffectsProvider
- ___49-[TUProxyCall remoteVideoClient:videoDidDegrade:]_block_invoke
- ___53-[TUProxyCall remoteVideoClient:remoteMediaDidStall:]_block_invoke
- ___53-[TUProxyCall remoteVideoClient:remoteVideoDidPause:]_block_invoke
- ___64-[TUProxyCall remoteVideoClient:remoteVideoAttributesDidChange:]_block_invoke
- ___65-[TUProxyCall remoteVideoClient:remoteScreenAttributesDidChange:]_block_invoke
- ___65-[TURemoteVideoClient insertSubLayerInLayer:videoSlotIdentifier:]_block_invoke
- ___CoreGraphicsLibraryCore_block_invoke
- ___QuartzCoreLibraryCore_block_invoke
- ___getCAContextClass_block_invoke
- ___getCALayerClass_block_invoke
- ___getCATransactionClass_block_invoke
- ___getCATransform3DMakeAffineTransformSymbolLoc_block_invoke
- ___getCGAffineTransformMakeRotationSymbolLoc_block_invoke
- ___getkCAGravityResizeAspectFillSymbolLoc_block_invoke
- _audit_stringCoreGraphics
- _audit_stringQuartzCore
- _getCAContextClass.softClass
- _getCALayerClass.softClass
- _getCATransactionClass
- _getCATransactionClass.softClass
- _getCATransform3DMakeAffineTransformSymbolLoc.ptr
- _getCGAffineTransformMakeRotationSymbolLoc.ptr
- _getkCAGravityResizeAspectFill
- _getkCAGravityResizeAspectFillSymbolLoc.ptr
- _objc_msgSend$_cameraTypeForVideoAttributeCamera:
- _objc_msgSend$_createLocalVideoIfNecessary
- _objc_msgSend$_createRemoteVideoIfNecessary
- _objc_msgSend$_orientationForVideoAttributesOrientation:
- _objc_msgSend$_synchronizeLocalVideo
- _objc_msgSend$_synchronizeRemoteVideo
- _objc_msgSend$addSublayer:
- _objc_msgSend$animojiNames
- _objc_msgSend$availableVideoEffects
- _objc_msgSend$avcRemoteVideoModeForMode:
- _objc_msgSend$begin
- _objc_msgSend$bounds
- _objc_msgSend$camera
- _objc_msgSend$cleanUpSubLayerForLayer:
- _objc_msgSend$commit
- _objc_msgSend$currentVideoEffect
- _objc_msgSend$initWithName:thumbnailImage:
- _objc_msgSend$initWithStreamToken:delegate:
- _objc_msgSend$initWithVideoContextSlotIdentifier:
- _objc_msgSend$insertSubLayerInLayer:videoSlotIdentifier:
- _objc_msgSend$isEqualToEffect:
- _objc_msgSend$layer
- _objc_msgSend$localVideo
- _objc_msgSend$nameForSubLayer
- _objc_msgSend$objectForSlot:
- _objc_msgSend$outgoingCallCallerIDEnabled
- _objc_msgSend$remoteVideo
- _objc_msgSend$remoteVideoModeToLayer
- _objc_msgSend$removeFromSuperlayer
- _objc_msgSend$requiresRemoteVideo
- _objc_msgSend$setAnimoji:
- _objc_msgSend$setBounds:
- _objc_msgSend$setCameraType:
- _objc_msgSend$setContents:
- _objc_msgSend$setContentsGravity:
- _objc_msgSend$setCurrentVideoEffect:
- _objc_msgSend$setLocalVideo:
- _objc_msgSend$setMediaStalled:
- _objc_msgSend$setRemoteAspectRatio:
- _objc_msgSend$setRemoteScreenLandscapeAspectRatio:
- _objc_msgSend$setRemoteScreenOrientation:
- _objc_msgSend$setRemoteScreenPortraitAspectRatio:
- _objc_msgSend$setRemoteVideo:
- _objc_msgSend$setRemoteVideoContentRect:
- _objc_msgSend$setRemoteVideoModeToLayer:
- _objc_msgSend$setTransform:
- _objc_msgSend$setVideoCaptureModeToLayer:
- _objc_msgSend$setVideoDegraded:
- _objc_msgSend$setVideoLayer:
- _objc_msgSend$setVideoLayer:forMode:
- _objc_msgSend$setVideoMirrored:
- _objc_msgSend$setVideoPaused:
- _objc_msgSend$sublayers
- _objc_msgSend$thumbnailForAnimojiNamed:options:
- _objc_msgSend$thumbnailImage
- _objc_msgSend$thumbnailImageForVideoEffectName:
- _objc_msgSend$videoCaptureModeToLayer
- _objc_msgSend$videoContextSlotIdentifier
- _objc_msgSend$videoLayer
- _objc_msgSend$videoMirrored
CStrings:
+ "DeviceUsagePage"
+ "PhoneSettings"
+ "Retrieved ShowBCIDSwitch feature capability value '%@' for subscription %@"
+ "Retrieving ShowBCIDSwitch feature capability value for subscription %@ failed with error %@"
+ "ShowBCIDSwitch"
+ "com.apple.Preferences"
+ "\xf0\xf0\xf0A"
- "%@-%p"
- "-[TURemoteVideoClient init]"
- "-[TUVideoEffect initWithName:thumbnailImage:]"
- "-[TUVideoEffect init]"
- "AVCRemoteVideoClient"
- "AVTAnimoji"
- "Asked to set local video layer %@ for mode %ld"
- "Asked to set remote video layer %@ for mode %ld"
- "AvatarKit"
- "CAContext"
- "CALayer"
- "CATransaction"
- "CATransform3D _CATransform3DMakeAffineTransform(CGAffineTransform)"
- "CATransform3DMakeAffineTransform"
- "CGAffineTransform _CGAffineTransformMakeRotation(CGFloat)"
- "CGAffineTransformMakeRotation"
- "Class getCAContextClass(void)_block_invoke"
- "Class getCALayerClass(void)_block_invoke"
- "Class getCATransactionClass(void)_block_invoke"
- "Client asked to synchronize remote video layers but we don't have a AVCRemoteVideoClient which is only created once we have a nonzero videoStreamToken"
- "Creating AVCRemoteVideoClient with stream token %ld"
- "DeviceUsage"
- "Disabled"
- "NSString *getkCAGravityResizeAspectFill(void)"
- "No layers to synchronize so setting self.remoteVideo to nil"
- "No layers to synchronize, set local TURemoteVideoClient to nil"
- "Retrieved verstat feature capability value '%@' for subscription %@"
- "Retrieving verstat feature capability value for subscription %@ failed with error %@"
- "Setting video layer %@ for mode %d"
- "TURemoteVideoClient.m"
- "TURemoteVideoSubLayer"
- "TUVideoEffect.m"
- "Unable to weak-link symbol kCAGravityResizeAspectFill"
- "VerstatFeatureCapability"
- "[WARN] Cannot create TUVideoEffect named %@ with nil thumbnailImage"
- "kCAGravityResizeAspectFill"
- "outgoingCallCallerID"
- "self.videoStreamToken: %ld didPause: %d"
- "self.videoStreamToken: %ld didStall: %d"
- "self.videoStreamToken: %ld screenAttributes: %@"
- "self.videoStreamToken: %ld videoAttributes: %@"
- "softlink:r:path:/System/Library/Frameworks/CoreGraphics.framework/CoreGraphics"
- "softlink:r:path:/System/Library/Frameworks/QuartzCore.framework/QuartzCore"
- "thumbnailImage"
- "void *CoreGraphicsLibrary(void)"
- "void *QuartzCoreLibrary(void)"
- "\xf0\xf0\xf0Q"
```
