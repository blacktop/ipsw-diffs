## MediaRemote

> `/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote`

```diff

 4025.300.6.0.0
-  __TEXT.__text: 0x2f3984
+  __TEXT.__text: 0x2f3a24
   __TEXT.__auth_stubs: 0x16f0
-  __TEXT.__objc_methlist: 0x2b080
+  __TEXT.__objc_methlist: 0x2b090
   __TEXT.__const: 0x5f8
   __TEXT.__cstring: 0x2bc5c
   __TEXT.__oslogstring: 0xdb82

   __TEXT.__ustring: 0x796
   __TEXT.__unwind_info: 0xb298
   __TEXT.__objc_classname: 0x4dad
-  __TEXT.__objc_methname: 0x4d4c4
-  __TEXT.__objc_methtype: 0x9061
+  __TEXT.__objc_methname: 0x4d504
+  __TEXT.__objc_methtype: 0x90b9
   __TEXT.__objc_stubs: 0x28460
   __DATA_CONST.__got: 0x1440
   __DATA_CONST.__const: 0xb1f8

   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x260
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf008
+  __DATA_CONST.__objc_selrefs: 0xf010
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0xfd0
   __DATA_CONST.__objc_arraydata: 0x260
   __AUTH_CONST.__auth_got: 0xb88
   __AUTH_CONST.__const: 0x3080
   __AUTH_CONST.__cfstring: 0x23140
-  __AUTH_CONST.__objc_const: 0x45c98
+  __AUTH_CONST.__objc_const: 0x45ca0
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_intobj: 0x4e0
   __AUTH_CONST.__objc_dictobj: 0x50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 63FDF0F0-2CD1-3D8B-A3F1-E6D6E65BEE71
+  UUID: 5D3C7E65-14AD-3E86-A9B4-EDE35E759C33
   Functions: 20164
   Symbols:   55363
-  CStrings:  24379
+  CStrings:  24382
 
Functions:
~ -[MRAVConcreteOutputContext _unregisterNotifications] : 128 -> 124
~ -[MRAVConcreteOutputContext _reloadPredictedOutputDevice] : 192 -> 208
~ -[MROutputContextController _registerNotifications] : 396 -> 408
~ -[MRAVOutputContextEndpoint _reloadOutputDevicesFromContext] : 104 -> 116
~ -[MRAVLocalEndpoint registerNotifications] : 120 -> 132
~ -[MROutputContextDataSource notifyDataSourceReloaded] : 116 -> 112
~ -[MRAVXPCPipeTransport stream:handleEvent:] : 212 -> 232
~ -[MRDistantExternalDevice _updateHostedDeviceDesiredNotifications:] : 160 -> 156
~ -[MRDistantExternalDevice _updateHostedDeviceDesiredCallbacks:] : 160 -> 156
~ -[MRDistantExternalDevice setConnectionState:] : 140 -> 152
~ -[MRAVConcreteOutputContext _reloadOutputContext] : 152 -> 148
~ -[MRMediaSuggestionPreferences _registerForNotifications] : 144 -> 156
~ -[MRMediaSuggestionPreferences _notifyListener] : 188 -> 184
~ -[MRCoreUtilsPairingSession _handleSetupExchangeComplete] : 132 -> 128
~ -[MRMediaRemoteServiceClient _invalidateConnection] : 248 -> 244
~ -[MRMediaRemoteServiceClient _resumeConnection] : 176 -> 172
~ -[MRMediaRemoteServiceClient _restoreConnection] : 316 -> 332
~ -[MRAVDistantEndpoint _handleEndpointDidConnectWithExternalDevice:] : 100 -> 108
~ -[MRAVDistantEndpoint _handleEndpointDidDisconnectWithError:] : 108 -> 120
~ -[MRAVDistantEndpoint _unregisterNotificationsForExternalDevice:] : 176 -> 192
~ -[MRAVDistantEndpoint _registerNotificationsForExternalDevice:] : 192 -> 208
~ -[MRNowPlayingOriginClientManager _clearSystemEndpointForType:reason:queue:] : 188 -> 204
~ -[MRAVReconnaissanceSession _onQueue_endSearch] : 192 -> 208
CStrings:
+ "service:account:didReceiveLocalNetworkHandshake:fromID:context:"
+ "v52@0:8@\"IDSService\"16@\"IDSAccount\"24B32@\"NSString\"36@\"NSData\"44"
+ "v52@0:8@16@24B32@36@44"

```
