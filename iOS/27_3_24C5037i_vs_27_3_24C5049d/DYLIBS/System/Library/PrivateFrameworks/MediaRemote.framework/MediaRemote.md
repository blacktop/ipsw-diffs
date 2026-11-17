## MediaRemote

> `/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote`

```diff

-4026.300.11.0.0
-  __TEXT.__text: 0x3081c8
-  __TEXT.__objc_methlist: 0x2c9b8
+4026.310.18.1.0
+  __TEXT.__text: 0x30b134
+  __TEXT.__objc_methlist: 0x2cb60
   __TEXT.__const: 0x750
-  __TEXT.__cstring: 0x2dfeb
-  __TEXT.__oslogstring: 0xebb9
-  __TEXT.__gcc_except_tab: 0x63e4
+  __TEXT.__cstring: 0x2e1b8
+  __TEXT.__oslogstring: 0xeddf
+  __TEXT.__gcc_except_tab: 0x63f0
   __TEXT.__dlopen_cstrs: 0x777
   __TEXT.__ustring: 0x7b8
-  __TEXT.__unwind_info: 0xee70
+  __TEXT.__unwind_info: 0xef38
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xbc40
-  __DATA_CONST.__objc_classlist: 0x1210
+  __DATA_CONST.__const: 0xbce0
+  __DATA_CONST.__objc_classlist: 0x1218
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x260
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xfa48
+  __DATA_CONST.__objc_selrefs: 0xfb08
   __DATA_CONST.__objc_protorefs: 0x88
-  __DATA_CONST.__objc_superrefs: 0x1038
+  __DATA_CONST.__objc_superrefs: 0x1040
   __DATA_CONST.__objc_arraydata: 0x260
   __DATA_CONST.__got: 0x14e8
-  __AUTH_CONST.__const: 0x34a0
-  __AUTH_CONST.__cfstring: 0x24ca0
-  __AUTH_CONST.__objc_const: 0x481c8
+  __AUTH_CONST.__const: 0x3500
+  __AUTH_CONST.__cfstring: 0x24dc0
+  __AUTH_CONST.__objc_const: 0x484c8
   __AUTH_CONST.__objc_intobj: 0x540
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0xbd8
-  __AUTH.__objc_data: 0x5f00
-  __DATA.__objc_ivar: 0x3418
+  __AUTH_CONST.__auth_got: 0xbe8
+  __AUTH.__objc_data: 0x5f50
+  __DATA.__objc_ivar: 0x344c
   __DATA.__data: 0x1ca8
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x55a0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 21071
-  Symbols:   30328
-  CStrings:  6797
+  Functions: 21131
+  Symbols:   30403
+  CStrings:  6817
 
Symbols:
+ +[_MRDeviceInfoMessageProtobuf homeKitUserIdentifiersType]
+ -[MRClient representsSystemBooksApplication]
+ -[MRClient representsSystemClassicalRoomApplication]
+ -[MRClient representsSystemMediaApplication]
+ -[MRClient representsSystemPodcastsApplication]
+ -[MRDeviceInfo deviceInfoByRedactingHomeKitUserIdentifiers]
+ -[MRDeviceInfo homeKitUserIdentifiers]
+ -[MRDeviceInfo setHomeKitUserIdentifiers:]
+ -[MRNowPlayingControllerHelper controller:deviceLastPlayingDateDidChange:]
+ -[MRNowPlayingControllerHelper deviceLastPlayingDateDidChange]
+ -[MRNowPlayingControllerHelper setDeviceLastPlayingDateDidChange:]
+ -[MRSystemEndpointHomeKitUserObserver .cxx_destruct]
+ -[MRSystemEndpointHomeKitUserObserver _handleActiveSystemEndpointDidChange:]
+ -[MRSystemEndpointHomeKitUserObserver _handleEndpointDeviceInfoDidChange:]
+ -[MRSystemEndpointHomeKitUserObserver _handleEndpointDidDisconnect:]
+ -[MRSystemEndpointHomeKitUserObserver _onQueue_reload]
+ -[MRSystemEndpointHomeKitUserObserver _onQueue_scheduleRetry]
+ -[MRSystemEndpointHomeKitUserObserver _onQueue_updateHomeKitUserIdentifiers:]
+ -[MRSystemEndpointHomeKitUserObserver begin]
+ -[MRSystemEndpointHomeKitUserObserver dealloc]
+ -[MRSystemEndpointHomeKitUserObserver delegate]
+ -[MRSystemEndpointHomeKitUserObserver end]
+ -[MRSystemEndpointHomeKitUserObserver homeKitUserIdentifiers]
+ -[MRSystemEndpointHomeKitUserObserver initWithDelegate:queue:]
+ -[MRSystemEndpointHomeKitUserObserver setDelegate:]
+ -[MRUserSettings resetUserSelectedEndpointOnLocalPlayback]
+ -[MRUserSettings syncHomeKitUser]
+ -[MRV2NowPlayingController _notifyDelegateOfUpdatedDeviceLastPlayingDate:]
+ -[MRV2NowPlayingController _requestDeviceLastPlayingDateForPlayerPath:queue:completion:]
+ -[MRV2NowPlayingController lastKnownPlaybackState]
+ -[MRV2NowPlayingController setLastKnownPlaybackState:]
+ -[_MRDeviceInfoMessageProtobuf addHomeKitUserIdentifiers:]
+ -[_MRDeviceInfoMessageProtobuf clearHomeKitUserIdentifiers]
+ -[_MRDeviceInfoMessageProtobuf homeKitUserIdentifiersAtIndex:]
+ -[_MRDeviceInfoMessageProtobuf homeKitUserIdentifiersCount]
+ -[_MRDeviceInfoMessageProtobuf homeKitUserIdentifiers]
+ -[_MRDeviceInfoMessageProtobuf setHomeKitUserIdentifiers:]
+ GCC_except_table119
+ GCC_except_table195
+ GCC_except_table202
+ _OBJC_CLASS_$_MRSystemEndpointHomeKitUserObserver
+ _OBJC_IVAR_$_MRDeviceInfo._homeKitUserIdentifiers
+ _OBJC_IVAR_$_MRNowPlayingControllerHelper._deviceLastPlayingDateDidChange
+ _OBJC_IVAR_$_MRSystemEndpointHomeKitUserObserver._delegate
+ _OBJC_IVAR_$_MRSystemEndpointHomeKitUserObserver._delegateQueue
+ _OBJC_IVAR_$_MRSystemEndpointHomeKitUserObserver._endpoint
+ _OBJC_IVAR_$_MRSystemEndpointHomeKitUserObserver._generation
+ _OBJC_IVAR_$_MRSystemEndpointHomeKitUserObserver._homeKitUserIdentifiers
+ _OBJC_IVAR_$_MRSystemEndpointHomeKitUserObserver._lock
+ _OBJC_IVAR_$_MRSystemEndpointHomeKitUserObserver._queue
+ _OBJC_IVAR_$_MRSystemEndpointHomeKitUserObserver._retryAttempt
+ _OBJC_IVAR_$_MRSystemEndpointHomeKitUserObserver._running
+ _OBJC_IVAR_$_MRV2NowPlayingController._lastKnownPlaybackState
+ _OBJC_IVAR_$__MRDeviceInfoMessageProtobuf._homeKitUserIdentifiers
+ _OBJC_METACLASS_$_MRSystemEndpointHomeKitUserObserver
+ __OBJC_$_INSTANCE_METHODS_MRSystemEndpointHomeKitUserObserver
+ __OBJC_$_INSTANCE_VARIABLES_MRSystemEndpointHomeKitUserObserver
+ __OBJC_$_PROP_LIST_MRSystemEndpointHomeKitUserObserver
+ __OBJC_CLASS_RO_$_MRSystemEndpointHomeKitUserObserver
+ __OBJC_METACLASS_RO_$_MRSystemEndpointHomeKitUserObserver
+ ___37-[MRNowPlayingController _makeHelper]_block_invoke_23
+ ___37-[MRNowPlayingController _makeHelper]_block_invoke_24
+ ___42-[MRSystemEndpointHomeKitUserObserver end]_block_invoke
+ ___44-[MRSystemEndpointHomeKitUserObserver begin]_block_invoke
+ ___54-[MRSystemEndpointHomeKitUserObserver _onQueue_reload]_block_invoke
+ ___54-[MRSystemEndpointHomeKitUserObserver _onQueue_reload]_block_invoke_2
+ ___61-[MRSystemEndpointHomeKitUserObserver _onQueue_scheduleRetry]_block_invoke
+ ___68-[MRSystemEndpointHomeKitUserObserver _handleEndpointDidDisconnect:]_block_invoke
+ ___68-[MRV2NowPlayingController _handlePlaybackStateChangedNotification:]_block_invoke_2
+ ___68-[MRV2NowPlayingController _handlePlaybackStateChangedNotification:]_block_invoke_3
+ ___74-[MRSystemEndpointHomeKitUserObserver _handleEndpointDeviceInfoDidChange:]_block_invoke
+ ___76-[MRSystemEndpointHomeKitUserObserver _handleActiveSystemEndpointDidChange:]_block_invoke
+ ___77-[MRSystemEndpointHomeKitUserObserver _onQueue_updateHomeKitUserIdentifiers:]_block_invoke
+ ___88-[MRV2NowPlayingController _requestDeviceLastPlayingDateForPlayerPath:queue:completion:]_block_invoke
+ ___block_descriptor_48_e8_32s40s_e28_v24?0"NSDate"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e34_v24?0"MRAVEndpoint"8"NSError"16ls32l8
+ ___block_descriptor_56_e8_32s40s_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ _exp2
+ _objc_retain_x10
- -[MRAVDistantRoutingDiscoverySession configurationWithCompletion:]
- GCC_except_table120
- GCC_except_table186
- GCC_except_table187
- GCC_except_table197
CStrings:
+ "05AC:110B"
+ "MRAVEndpoint.addOutputDevicesWithUIDs"
+ "MRAVEndpoint.moveOutputDevicesWithUIDs"
+ "MRAudioDataBlock.m"
+ "UIDs=(%@), group=%@"
+ "[MRSystemEndpointHomeKitUserObserver] Failed to connect to system endpoint %{public}@: %{public}@"
+ "[MRSystemEndpointHomeKitUserObserver] Failed to resolve system endpoint: %{public}@"
+ "[MRSystemEndpointHomeKitUserObserver] HomeKit user identifiers changed: %{public}@"
+ "[MRSystemEndpointHomeKitUserObserver] Retrying in %.0fs"
+ "[MRSystemEndpointHomeKitUserObserver] System endpoint changed, reloading"
+ "[MRSystemEndpointHomeKitUserObserver] System endpoint disconnected: %{public}@"
+ "addOutputDevicesWithUIDs.xpcInterface"
+ "com.apple.MediaRemote.MRSystemEndpointHomeKitUserObserver"
+ "groupedDeviceUID"
+ "homeKitUserIdentifiers"
+ "homepod.2.and.homepod.mini.2.and.appletv.fill"
+ "invalid buffer size for decoding voice input message (%lu > (%lu * %lu))"
+ "moveOutputDevicesWithUIDs.xpcInterface"
+ "packet descriptions exceed maximum packet capacity (%lu > %lu)"
+ "resetUserSelectedEndpointOnLocalPlayback"
+ "sync_homekit_user"
- "76,4363"
```
