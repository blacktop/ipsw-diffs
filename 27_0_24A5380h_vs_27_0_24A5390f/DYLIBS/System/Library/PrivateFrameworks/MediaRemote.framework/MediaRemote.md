## MediaRemote

> `/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote`

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

-4026.110.75.1.0
-  __TEXT.__text: 0x315d6c
-  __TEXT.__objc_methlist: 0x2c708
-  __TEXT.__const: 0x698
-  __TEXT.__cstring: 0x2dd34
-  __TEXT.__oslogstring: 0xe921
-  __TEXT.__gcc_except_tab: 0x6338
+4026.100.79.0.0
+  __TEXT.__text: 0x3168f0
+  __TEXT.__objc_methlist: 0x2c758
+  __TEXT.__const: 0x6a0
+  __TEXT.__cstring: 0x2ddca
+  __TEXT.__oslogstring: 0xe9d8
+  __TEXT.__gcc_except_tab: 0x63a4
   __TEXT.__dlopen_cstrs: 0x777
   __TEXT.__ustring: 0x7b8
-  __TEXT.__unwind_info: 0xbdb0
+  __TEXT.__unwind_info: 0xbde8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xbac8
+  __DATA_CONST.__const: 0xbaf8
   __DATA_CONST.__objc_classlist: 0x1210
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x260
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf8d8
+  __DATA_CONST.__objc_selrefs: 0xf908
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0x1038
   __DATA_CONST.__objc_arraydata: 0x260
-  __DATA_CONST.__got: 0x14c8
+  __DATA_CONST.__got: 0x14d0
   __AUTH_CONST.__const: 0x3460
-  __AUTH_CONST.__cfstring: 0x248c0
-  __AUTH_CONST.__objc_const: 0x47d90
+  __AUTH_CONST.__cfstring: 0x249a0
+  __AUTH_CONST.__objc_const: 0x47ea0
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_intobj: 0x4f8
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0xbc0
   __AUTH.__objc_data: 0x8700
-  __DATA.__objc_ivar: 0x33d0
-  __DATA.__data: 0x1ce0
-  __DATA.__bss: 0x978
+  __DATA.__objc_ivar: 0x33e8
+  __DATA.__data: 0x1ca8
+  __DATA.__bss: 0x998
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x2da0
-  __DATA_DIRTY.__data: 0x48
+  __DATA_DIRTY.__data: 0x88
   __DATA_DIRTY.__bss: 0x5c8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVRouting.framework/AVRouting

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 20997
-  Symbols:   35544
-  CStrings:  6754
+  Functions: 21006
+  Symbols:   35562
+  CStrings:  6763
 
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
+ OBJC_IVAR_$__MRCreateHostedEndpointResponseProtobuf._details
+ _MRMediaRemoteCopyDisabledReasonDescription
+ _OBJC_CLASS_$_NSBlockOperation
+ _OBJC_IVAR_$_MRAVRoutingDiscoverySession._lastLoggedEndpoints
+ _OBJC_IVAR_$_MRAVRoutingDiscoverySession._lastLoggedOutputDevicesOutputDevices
+ _OBJC_IVAR_$_MRAVRoutingDiscoverySession._verboseEndpointLoggingQueue
+ _OBJC_IVAR_$_MRAVRoutingDiscoverySession._verboseOutputDeviceLoggingQueue
+ _OBJC_IVAR_$_MRUserSettings._bypassAvailabilityChecksForLiveAppEntityFeedDonations
+ __OBJC_$_INSTANCE_METHODS_MRAVOutputDevice(MRAVRoutingDiscoverySessionAdditions)
+ ___66+[MRSystemMediaBundles _offProcessPlaybackHostBundleIDsForBundle:]_block_invoke
+ ___71-[MRUserSettings bypassAvailabilityChecksForLiveAppEntityFeedDonations]_block_invoke
+ __offProcessPlaybackHostBundleIDsForBundle:.__musicHosts
+ __offProcessPlaybackHostBundleIDsForBundle:.__once
+ __offProcessPlaybackHostBundleIDsForBundle:.__podcastsHosts
+ _bypassAvailabilityChecksForLiveAppEntityFeedDonations.onceToken
+ _objc_msgSend$_offProcessPlaybackHostBundleIDsForBundle:
+ _objc_msgSend$blockOperationWithBlock:
+ _objc_msgSend$mr_debugName
+ _objc_msgSend$originalGUID
- -[MRCreateHostedEndpointResponseMessage initWithGroupUID:]
- _MRUserSettingsGroupSessionBoopContext
- _MRUserSettingsGroupSessionNearbyDiscoveryContext
- _MRUserSettingsNearbyDeviceIdentifiersContext
- _MRUserSettingsRoutePickerAirPlayAllowListContext
- _MRUserSettingsRoutePickerAirPlayDenyListContext
- _MRUserSettingsSystemVolumeCapabilitiesDidChangeContext
- _MRUserSettingsSystemVolumeDidChangeContext
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
