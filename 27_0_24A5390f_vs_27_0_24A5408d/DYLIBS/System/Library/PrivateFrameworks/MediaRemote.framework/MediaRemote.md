## MediaRemote

> `/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-4026.100.79.0.0
-  __TEXT.__text: 0x3168f0
-  __TEXT.__objc_methlist: 0x2c758
-  __TEXT.__const: 0x6a0
-  __TEXT.__cstring: 0x2ddca
-  __TEXT.__oslogstring: 0xe9d8
-  __TEXT.__gcc_except_tab: 0x63a4
+4026.110.83.1.0
+  __TEXT.__text: 0x317068
+  __TEXT.__objc_methlist: 0x2c788
+  __TEXT.__const: 0x6b0
+  __TEXT.__cstring: 0x2de92
+  __TEXT.__oslogstring: 0xea48
+  __TEXT.__gcc_except_tab: 0x6368
   __TEXT.__dlopen_cstrs: 0x777
   __TEXT.__ustring: 0x7b8
-  __TEXT.__unwind_info: 0xbde8
+  __TEXT.__unwind_info: 0xbe10
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xbaf8
+  __DATA_CONST.__const: 0xbb08
   __DATA_CONST.__objc_classlist: 0x1210
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x260
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf908
+  __DATA_CONST.__objc_selrefs: 0xf930
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0x1038
   __DATA_CONST.__objc_arraydata: 0x260
   __DATA_CONST.__got: 0x14d0
-  __AUTH_CONST.__const: 0x3460
-  __AUTH_CONST.__cfstring: 0x249a0
-  __AUTH_CONST.__objc_const: 0x47ea0
+  __AUTH_CONST.__const: 0x3440
+  __AUTH_CONST.__cfstring: 0x24a20
+  __AUTH_CONST.__objc_const: 0x47e80
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_intobj: 0x4f8
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0xbc0
   __AUTH.__objc_data: 0x8700
-  __DATA.__objc_ivar: 0x33e8
+  __DATA.__objc_ivar: 0x33e4
   __DATA.__data: 0x1ca8
   __DATA.__bss: 0x998
   __DATA.__common: 0x8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 21006
-  Symbols:   35562
-  CStrings:  6763
+  Functions: 21013
+  Symbols:   35571
+  CStrings:  6771
 
Symbols:
+ -[MRAVLocalControlCenterEndpoint _newVolumeController]
+ -[MRAVVolumeClientEndpoint _initWithSliderType:uniqueIdentifier:]
+ -[MRAVVolumeClientEndpoint _newVolumeController]
+ -[MRAVVolumeClientEndpoint _onVolumeQueue_maybeLazyInitVolumeController]
+ -[MRAudioIntentDetails dictionaryRepresentation]
+ -[MRAudioIntentDetails initWithDictionaryRepresentation:]
+ -[MRMediaRemoteService triggerClusterErrorDialogForRouteUID:status:completion:]
+ -[MRUserSettings clearClusterConnectionThrottleOnNetworkChange]
+ GCC_except_table124
+ GCC_except_table145
+ GCC_except_table352
+ _MRCreateUUIDv5
+ _MRNowPlayingCreateDerivedIdentifier
+ _MRNowPlayingGetArtworkSize
+ ___52-[MRProximityProvider _migrateForDevice:completion:]_block_invoke_2
+ ___65-[MRAVVolumeClientEndpoint _initWithSliderType:uniqueIdentifier:]_block_invoke
+ ___65-[MRAVVolumeClientEndpoint _initWithSliderType:uniqueIdentifier:]_block_invoke_2
+ ___79-[MRMediaRemoteService triggerClusterErrorDialogForRouteUID:status:completion:]_block_invoke
+ ___block_descriptor_64_e8_32s40s48s56bs_e35_v16?0"MRMigrationBehaviorResult"8ls32l8s40l8s48l8s56l8
+ _currentDeviceRoutingSymbolName.lock
+ _kMRNowPlayingRootNamespace
+ _objc_msgSend$_newVolumeController
+ _objc_msgSend$_onVolumeQueue_maybeLazyInitVolumeController
+ _objc_msgSend$getUUIDBytes:
+ _objc_msgSend$initWithOutputDeviceUIDs:startDate:
+ _objc_msgSend$initWithUUIDBytes:
+ _objc_msgSend$setVolumeController:
- -[MRAVLocalControlCenterEndpoint .cxx_destruct]
- -[MRAVLocalControlCenterEndpoint controlCenterVolumeController]
- -[MRAVLocalControlCenterEndpoint setControlCenterVolumeController:]
- -[MRAVVolumeClientEndpoint _initWithAVVolumeClient:sliderType:uniqueIdentifier:]
- GCC_except_table119
- GCC_except_table122
- GCC_except_table125
- GCC_except_table143
- GCC_except_table350
- _OBJC_IVAR_$_MRAVLocalControlCenterEndpoint._controlCenterVolumeController
- __OBJC_$_INSTANCE_VARIABLES_MRAVLocalControlCenterEndpoint
- __OBJC_$_PROP_LIST_MRAVLocalControlCenterEndpoint
- ___66+[MRDeviceIdentifierSymbolProvider currentDeviceRoutingSymbolName]_block_invoke
- ___80-[MRAVVolumeClientEndpoint _initWithAVVolumeClient:sliderType:uniqueIdentifier:]_block_invoke
- ___80-[MRAVVolumeClientEndpoint _initWithAVVolumeClient:sliderType:uniqueIdentifier:]_block_invoke_2
- ___80-[MRAVVolumeClientEndpoint _initWithAVVolumeClient:sliderType:uniqueIdentifier:]_block_invoke_3
- ___block_descriptor_56_e8_32s40s48bs_e35_v16?0"MRMigrationBehaviorResult"8ls32l8s40l8s48l8
- _currentDeviceRoutingSymbolName.onceToken
CStrings:
+ "-[MRAVVolumeClientEndpoint _newVolumeController]"
+ "Infra6GSteerNoCandidate"
+ "MRXPC_ROUTE_STATUS_KEY"
+ "UnsupportedProtocolRequiredRevertToLocal"
+ "[MRAVVolumeClientEndpoint] Creating %{public}@"
+ "[MRAVVolumeClientEndpoint] Initializing volumeController.."
+ "[MRAVVolumeClientEndpoint] VolumeController unavailable; will retry on next activation"
+ "clearClusterConnectionThrottleOnNetworkChange"
+ "migrateForDevice"
- "[MRAVVolumeClientEndpoint] Creating %{public}@ with volumeController: %{public}@"
```
