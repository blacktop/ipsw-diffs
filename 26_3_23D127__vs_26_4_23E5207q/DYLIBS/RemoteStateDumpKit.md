## RemoteStateDumpKit

> `/System/Library/PrivateFrameworks/RemoteStateDumpKit.framework/RemoteStateDumpKit`

```diff

-375.2.2.0.0
-  __TEXT.__text: 0x25b0
-  __TEXT.__auth_stubs: 0x2b0
+375.4.1.0.0
+  __TEXT.__text: 0x27e8
+  __TEXT.__auth_stubs: 0x280
   __TEXT.__objc_methlist: 0x44c
   __TEXT.__const: 0x70
   __TEXT.__gcc_except_tab: 0x4c
   __TEXT.__cstring: 0x112
   __TEXT.__oslogstring: 0x2c0
   __TEXT.__dlopen_cstrs: 0x61
-  __TEXT.__unwind_info: 0x118
+  __TEXT.__unwind_info: 0x138
   __TEXT.__objc_classname: 0xcd
   __TEXT.__objc_methname: 0xba6
   __TEXT.__objc_methtype: 0x4d2

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x348
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x168
+  __AUTH_CONST.__auth_got: 0x150
   __AUTH_CONST.__cfstring: 0xc0
   __AUTH_CONST.__objc_const: 0xca0
   __AUTH.__objc_data: 0x140

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E0165AE4-A92D-3AFE-B206-B505AA980E83
+  UUID: E8474C8A-5517-377C-83D7-71E5A2502D93
   Functions: 66
-  Symbols:   342
+  Symbols:   339
   CStrings:  222
 
Symbols:
+ _objc_autorelease
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x23
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutorelease
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x8
Functions:
~ -[RSPeerToPeerClientController prepareForConnection] : 392 -> 404
~ -[RSPeerToPeerClientController abort] : 132 -> 140
~ -[RSPeerToPeerClientController browser:foundPeer:withDiscoveryInfo:] : 196 -> 188
~ ___68-[RSPeerToPeerClientController browser:foundPeer:withDiscoveryInfo:]_block_invoke : 100 -> 104
~ -[RSPeerToPeerClientController browser:lostPeer:] : 240 -> 244
~ -[RSPeerToPeerClientController browser:didNotStartBrowsingForPeers:] : 240 -> 244
~ -[RSPeerToPeerClientController setServiceBrowser:] : 20 -> 80
~ -[RSPeerToPeerConnectionController prepareForConnection] : 588 -> 608
~ -[RSPeerToPeerConnectionController abort] : 128 -> 136
~ -[RSPeerToPeerConnectionController attemptConnectionWithPeer:successBlock:] : 112 -> 116
~ -[RSPeerToPeerConnectionController sendState:withInfo:toPeer:] : 412 -> 428
~ -[RSPeerToPeerConnectionController requestState:fromPeer:] : 496 -> 520
~ -[RSPeerToPeerConnectionController _shouldInteractWithPeer:] : 260 -> 288
~ -[RSPeerToPeerConnectionController _connectedPeerWithDisplayName:] : 416 -> 428
~ ___66-[RSPeerToPeerConnectionController _connectedPeerWithDisplayName:]_block_invoke : 92 -> 96
~ -[RSPeerToPeerConnectionController _stateDataWithRequestType:stateContent:info:] : 576 -> 596
~ -[RSPeerToPeerConnectionController _sendData:toPeers:] : 316 -> 320
~ -[RSPeerToPeerConnectionController session:peer:didChangeState:] : 376 -> 404
~ -[RSPeerToPeerConnectionController session:didReceiveData:fromPeer:] : 1156 -> 1228
~ -[RSPeerToPeerConnectionController setLocalPeerID:] : 12 -> 64
~ -[RSPeerToPeerConnectionController setSession:] : 12 -> 64
~ -[RSPeerToPeerConnectionController setAlreadyConnectedPeerIDs:] : 12 -> 64
~ -[RSPeerToPeerServerController prepareForConnection] : 396 -> 408
~ -[RSPeerToPeerServerController abort] : 144 -> 152
~ ___102-[RSPeerToPeerServerController advertiser:didReceiveInvitationFromPeer:withContext:invitationHandler:]_block_invoke : 96 -> 100
~ -[RSPeerToPeerServerController advertiser:didNotStartAdvertisingPeer:] : 256 -> 260
~ -[RSPeerToPeerServerController setServiceAdvertiser:] : 20 -> 80

```
