## MediaRemote

> `/System/Library/PrivateFrameworks/MediaRemote.framework/Versions/A/MediaRemote`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__DATA_DIRTY.__objc_data`

```diff

-4026.100.75.0.0
-  __TEXT.__text: 0x31e514
-  __TEXT.__objc_methlist: 0x2b7ac
-  __TEXT.__const: 0x5c0
-  __TEXT.__cstring: 0x2c444
-  __TEXT.__oslogstring: 0xd205
-  __TEXT.__gcc_except_tab: 0x582c
+4026.100.79.0.0
+  __TEXT.__text: 0x31f104
+  __TEXT.__objc_methlist: 0x2b7fc
+  __TEXT.__const: 0x5c8
+  __TEXT.__cstring: 0x2c4da
+  __TEXT.__oslogstring: 0xd2bc
+  __TEXT.__gcc_except_tab: 0x5898
   __TEXT.__dlopen_cstrs: 0x40b
   __TEXT.__ustring: 0x7b8
-  __TEXT.__unwind_info: 0xb168
+  __TEXT.__unwind_info: 0xb1a0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4b40
+  __DATA_CONST.__const: 0x4b70
   __DATA_CONST.__objc_classlist: 0x11c0
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x228
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf090
+  __DATA_CONST.__objc_selrefs: 0xf0c0
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0xff0
   __DATA_CONST.__objc_arraydata: 0x260
-  __DATA_CONST.__got: 0x1418
+  __DATA_CONST.__got: 0x1420
   __AUTH_CONST.__const: 0xa410
-  __AUTH_CONST.__cfstring: 0x23ca0
-  __AUTH_CONST.__objc_const: 0x46468
+  __AUTH_CONST.__cfstring: 0x23d80
+  __AUTH_CONST.__objc_const: 0x46578
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_intobj: 0x4c8
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0xa90
   __AUTH.__objc_data: 0x8430
-  __DATA.__objc_ivar: 0x32d0
-  __DATA.__data: 0x1a40
-  __DATA.__bss: 0x868
+  __DATA.__objc_ivar: 0x32e8
+  __DATA.__data: 0x1a08
+  __DATA.__bss: 0x888
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x2d50
-  __DATA_DIRTY.__data: 0x48
+  __DATA_DIRTY.__data: 0x88
   __DATA_DIRTY.__bss: 0x5a0
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/AVRouting.framework/Versions/A/AVRouting

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 20569
-  Symbols:   35104
-  CStrings:  6494
+  Functions: 20578
+  Symbols:   35122
+  CStrings:  6503
 
Symbols:
+ +[MRSystemMediaBundles _offProcessPlaybackHostBundleIDsForBundle:]
+ +[MRSystemMediaBundles processBundleID:mayDonateEntitiesForBundleID:]
+ -[MRAVOutputDevice(MRAVRoutingDiscoverySessionAdditions) mr_debugName]
+ -[MRCreateHostedEndpointResponseMessage details]
+ -[MRCreateHostedEndpointResponseMessage initWithGroupUID:details:]
+ -[MRUserSettings bypassAvailabilityChecksForLiveAppEntityFeedDonations]
+ -[_MRCreateHostedEndpointResponseProtobuf details]
+ -[_MRCreateHostedEndpointResponseProtobuf hasDetails]
+ -[_MRCreateHostedEndpointResponseProtobuf setDetails:]
+ GCC_except_table148
+ OBJC_IVAR_$_MRAVRoutingDiscoverySession._lastLoggedEndpoints
+ OBJC_IVAR_$_MRAVRoutingDiscoverySession._lastLoggedOutputDevicesOutputDevices
+ OBJC_IVAR_$_MRAVRoutingDiscoverySession._verboseEndpointLoggingQueue
+ OBJC_IVAR_$_MRAVRoutingDiscoverySession._verboseOutputDeviceLoggingQueue
+ OBJC_IVAR_$_MRUserSettings._bypassAvailabilityChecksForLiveAppEntityFeedDonations
+ OBJC_IVAR_$__MRCreateHostedEndpointResponseProtobuf._details
+ _MRMediaRemoteCopyDisabledReasonDescription
+ _OBJC_CLASS_$_NSBlockOperation
+ __OBJC_$_INSTANCE_METHODS_MRAVOutputDevice(MRAVRoutingDiscoverySessionAdditions)
+ ___66+[MRSystemMediaBundles _offProcessPlaybackHostBundleIDsForBundle:]_block_invoke
+ ___71-[MRUserSettings bypassAvailabilityChecksForLiveAppEntityFeedDonations]_block_invoke
+ _objc_msgSend$_offProcessPlaybackHostBundleIDsForBundle:
+ _objc_msgSend$blockOperationWithBlock:
+ _objc_msgSend$mr_debugName
+ _objc_msgSend$originalGUID
+ _offProcessPlaybackHostBundleIDsForBundle:.__musicHosts
+ _offProcessPlaybackHostBundleIDsForBundle:.__once
+ _offProcessPlaybackHostBundleIDsForBundle:.__podcastsHosts
+ bypassAvailabilityChecksForLiveAppEntityFeedDonations.onceToken
- -[MRCreateHostedEndpointResponseMessage initWithGroupUID:]
- _MRUserSettingsGroupSessionBoopContext
- _MRUserSettingsGroupSessionNearbyDiscoveryContext
- _MRUserSettingsNearbyDeviceIdentifiersContext
- _MRUserSettingsRoutePickerAirPlayAllowListContext
- _MRUserSettingsRoutePickerAirPlayDenyListContext
- _MRUserSettingsSystemVolumeCapabilitiesDidChangeContext
- _MRUserSettingsSystemVolumeDidChangeContext
- __72-[MRAVRoutingDiscoverySession logOutputDevicesChanged:oldOutputDevices:]_block_invoke_6
- __OBJC_$_INSTANCE_METHODS_MRAVOutputDevice
- __OBJC_$_PROP_LIST_MRAVOutputDevice
CStrings:
+ "%{public}@ - Verbose Endpoints changed\n%{public}@"
+ "%{public}@ - Verbose Output devices changed\n%{public}@"
+ "BypassAvailabilityChecksForLiveAppEntityFeedDonations"
+ "LowPerformance"
+ "LowPowerMode"
+ "PlayingAd"
+ "ThermalPressure"
+ "[MRIDSCompanionConnection] Message Sent<%lu>: data=%@ type=%@ destination=%@ session=%@ idsID=%@"
+ "[MRIDSCompanionConnection] Message received<%@>: data=%@ type=%@ destination=%@ session=%@ replyID=%@ idsGUID=%@"
+ "[MRIDSCompanionConnection] Unhandled message<%@>: no handler for type=%@ destination=%@ session=%@ idsGUID=%@"
+ "com.apple.AirMusic"
+ "com.apple.AirPodcasts"
- "Attempting to send IDS messages before first unlock"
- "[MRIDSCompanionConnection] Message Sent<%lu>: data=%@ type=%@ destination=%@ session=%@"
- "[MRIDSCompanionConnection] Message received<%@>: data=%@ type=%@ destination=%@ session=%@ replyID=%@"
```
