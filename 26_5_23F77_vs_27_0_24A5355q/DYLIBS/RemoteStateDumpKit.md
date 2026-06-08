## RemoteStateDumpKit

> `/System/Library/PrivateFrameworks/RemoteStateDumpKit.framework/RemoteStateDumpKit`

```diff

-375.5.2.100.0
-  __TEXT.__text: 0x27e8
-  __TEXT.__auth_stubs: 0x280
+387.0.0.0.0
+  __TEXT.__text: 0x24a4
   __TEXT.__objc_methlist: 0x44c
   __TEXT.__const: 0x70
   __TEXT.__gcc_except_tab: 0x4c
-  __TEXT.__cstring: 0x112
+  __TEXT.__cstring: 0x11c
   __TEXT.__oslogstring: 0x2c0
   __TEXT.__dlopen_cstrs: 0x61
-  __TEXT.__unwind_info: 0x138
-  __TEXT.__objc_classname: 0xcd
-  __TEXT.__objc_methname: 0xba6
-  __TEXT.__objc_methtype: 0x4d2
-  __TEXT.__objc_stubs: 0x7c0
-  __DATA_CONST.__got: 0x48
+  __TEXT.__unwind_info: 0x118
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x130
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x348
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x150
+  __DATA_CONST.__got: 0x48
   __AUTH_CONST.__cfstring: 0xc0
   __AUTH_CONST.__objc_const: 0xca0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x28
   __DATA.__data: 0x180

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F7B289F9-E769-3E76-A2F8-720F783C8A12
+  UUID: B6D0CFBA-8D29-310B-B15A-1A9FA77CD82B
   Functions: 66
-  Symbols:   339
-  CStrings:  222
+  Symbols:   342
+  CStrings:  34
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutorelease
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x8
- _objc_autorelease
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x23
Functions:
~ -[RSPeerToPeerClientController prepareForConnection] : 404 -> 396
~ -[RSPeerToPeerClientController abort] : 140 -> 132
~ -[RSPeerToPeerClientController browser:foundPeer:withDiscoveryInfo:] : 188 -> 196
~ ___68-[RSPeerToPeerClientController browser:foundPeer:withDiscoveryInfo:]_block_invoke : 104 -> 100
~ -[RSPeerToPeerClientController browser:lostPeer:] : 244 -> 196
~ -[RSPeerToPeerClientController browser:didNotStartBrowsingForPeers:] : 244 -> 196
~ -[RSPeerToPeerClientController serviceBrowser] : 16 -> 20
~ -[RSPeerToPeerClientController setServiceBrowser:] : 80 -> 20
~ -[RSPeerToPeerConnectionController prepareForConnection] : 608 -> 588
~ -[RSPeerToPeerConnectionController abort] : 136 -> 128
~ -[RSPeerToPeerConnectionController attemptConnectionWithPeer:successBlock:] : 116 -> 112
~ -[RSPeerToPeerConnectionController sendState:withInfo:toPeer:] : 428 -> 412
~ -[RSPeerToPeerConnectionController requestState:fromPeer:] : 520 -> 496
~ -[RSPeerToPeerConnectionController _shouldInteractWithPeer:] : 288 -> 260
~ -[RSPeerToPeerConnectionController _connectedPeerWithDisplayName:] : 428 -> 372
~ ___66-[RSPeerToPeerConnectionController _connectedPeerWithDisplayName:]_block_invoke : 96 -> 92
~ -[RSPeerToPeerConnectionController _stateDataWithRequestType:stateContent:info:] : 596 -> 532
~ -[RSPeerToPeerConnectionController _sendData:toPeers:] : 320 -> 272
~ -[RSPeerToPeerConnectionController session:peer:didChangeState:] : 404 -> 376
~ -[RSPeerToPeerConnectionController session:didReceiveData:fromPeer:] : 1228 -> 1112
~ -[RSPeerToPeerConnectionController setLocalPeerID:] : 64 -> 12
~ -[RSPeerToPeerConnectionController setSession:] : 64 -> 12
~ -[RSPeerToPeerConnectionController setAlreadyConnectedPeerIDs:] : 64 -> 12
~ -[RSPeerToPeerServerController prepareForConnection] : 408 -> 400
~ -[RSPeerToPeerServerController abort] : 152 -> 148
~ -[RSPeerToPeerServerController didStartAcceptingConnections] : 40 -> 48
~ ___102-[RSPeerToPeerServerController advertiser:didReceiveInvitationFromPeer:withContext:invitationHandler:]_block_invoke : 100 -> 96
~ -[RSPeerToPeerServerController advertiser:didNotStartAdvertisingPeer:] : 260 -> 216
~ -[RSPeerToPeerServerController serviceAdvertiser] : 16 -> 20
~ -[RSPeerToPeerServerController setServiceAdvertiser:] : 80 -> 20
~ -[RSPeerToPeerServerController advertiserDidNotStartAdvertising] : 16 -> 20
~ -[RSPeerToPeerServerController setAdvertiserDidNotStartAdvertising:] : 16 -> 20
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<RSPeerToPeerConnectionControllerDataSource>\""
- "@\"<RSPeerToPeerConnectionControllerDelegate>\""
- "@\"MCNearbyServiceAdvertiser\""
- "@\"MCNearbyServiceBrowser\""
- "@\"MCPeerID\""
- "@\"MCSession\""
- "@\"NSMutableArray\""
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8Q16q24"
- "@40@0:8:16@24@32"
- "@40@0:8Q16@24@32"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "JSONObjectWithData:options:error:"
- "MCNearbyServiceAdvertiserDelegate"
- "MCNearbyServiceBrowserDelegate"
- "MCSessionDelegate"
- "NSObject"
- "Q"
- "Q16@0:8"
- "RSPeerToPeerClientController"
- "RSPeerToPeerConnectionController"
- "RSPeerToPeerServerController"
- "RSStateInfo"
- "T#,R"
- "T@\"<RSPeerToPeerConnectionControllerDataSource>\",W,N,V_dataSource"
- "T@\"<RSPeerToPeerConnectionControllerDelegate>\",W,N,V_delegate"
- "T@\"MCNearbyServiceAdvertiser\",&,N,V_serviceAdvertiser"
- "T@\"MCNearbyServiceBrowser\",&,N,V_serviceBrowser"
- "T@\"MCPeerID\",&,N,V_localPeerID"
- "T@\"MCSession\",&,N,V_session"
- "T@\"NSMutableArray\",&,N,V_alreadyConnectedPeerIDs"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TB,N,V_advertiserDidNotStartAdvertising"
- "TQ,N,V_stateType"
- "TQ,R"
- "Tq,N,V_actionRevision"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_actionRevision"
- "_advertiserDidNotStartAdvertising"
- "_alreadyConnectedPeerIDs"
- "_connectedPeerWithDisplayName:"
- "_dataSource"
- "_delegate"
- "_localPeerID"
- "_sendData:toPeers:"
- "_serviceAdvertiser"
- "_serviceBrowser"
- "_session"
- "_shouldInteractWithPeer:"
- "_stateDataWithRequestType:stateContent:info:"
- "_stateType"
- "abort"
- "actionRevision"
- "addObject:"
- "advertiser:didNotStartAdvertisingPeer:"
- "advertiser:didReceiveInvitationFromPeer:withContext:invitationHandler:"
- "advertiserDidNotStartAdvertising"
- "allowedRemotePeerDisplayNames"
- "alreadyConnectedPeerIDs"
- "array"
- "arrayWithObjects:count:"
- "attemptConnectionWithPeer:successBlock:"
- "autorelease"
- "browser:didNotStartBrowsingForPeers:"
- "browser:foundPeer:withDiscoveryInfo:"
- "browser:lostPeer:"
- "class"
- "conformsToProtocol:"
- "connectedPeers"
- "containsObject:"
- "dataSource"
- "dataWithJSONObject:options:error:"
- "dealloc"
- "debugDescription"
- "delegate"
- "description"
- "dictionary"
- "didConnectToRemotePeer:"
- "didDisconnectFromRemotePeer:"
- "didReceiveState:withInfo:fromPeer:"
- "didStartAcceptingConnections"
- "disconnect"
- "hash"
- "indexOfObjectPassingTest:"
- "init"
- "initWithDataSource:"
- "initWithDisplayName:"
- "initWithPeer:discoveryInfo:serviceType:"
- "initWithPeer:securityIdentity:encryptionPreference:"
- "initWithPeer:serviceType:"
- "initWithType:revision:"
- "integerValue"
- "invitePeer:toSession:withContext:timeout:"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "localPeerDisplayName"
- "localPeerID"
- "localizedDescription"
- "numberWithInteger:"
- "numberWithUnsignedInteger:"
- "objectAtIndex:"
- "objectForKey:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "prepareForConnection"
- "q"
- "q16@0:8"
- "release"
- "removeObject:"
- "requestState:fromPeer:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "sendData:toPeers:withMode:error:"
- "sendState:withInfo:toPeer:"
- "serviceAdvertiser"
- "serviceBrowser"
- "session"
- "session:didFinishReceivingResourceWithName:fromPeer:atURL:withError:"
- "session:didReceiveCertificate:fromPeer:certificateHandler:"
- "session:didReceiveData:fromPeer:"
- "session:didReceiveStream:withName:fromPeer:"
- "session:didStartReceivingResourceWithName:fromPeer:withProgress:"
- "session:peer:didChangeState:"
- "setActionRevision:"
- "setAdvertiserDidNotStartAdvertising:"
- "setAlreadyConnectedPeerIDs:"
- "setDataSource:"
- "setDelegate:"
- "setLocalPeerID:"
- "setObject:forKey:"
- "setServiceAdvertiser:"
- "setServiceBrowser:"
- "setSession:"
- "setStateType:"
- "startAdvertisingPeer"
- "startBrowsingForPeers"
- "stateForStateType:withCompletionHandler:"
- "stateType"
- "stopAdvertisingPeer"
- "stopBrowsingForPeers"
- "superclass"
- "supportedStateTypes"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v24@0:8q16"
- "v32@0:8@\"MCNearbyServiceAdvertiser\"16@\"NSError\"24"
- "v32@0:8@\"MCNearbyServiceBrowser\"16@\"MCPeerID\"24"
- "v32@0:8@\"MCNearbyServiceBrowser\"16@\"NSError\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v40@0:8@\"MCNearbyServiceBrowser\"16@\"MCPeerID\"24@\"NSDictionary\"32"
- "v40@0:8@\"MCSession\"16@\"MCPeerID\"24q32"
- "v40@0:8@\"MCSession\"16@\"NSData\"24@\"MCPeerID\"32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24q32"
- "v48@0:8@\"MCNearbyServiceAdvertiser\"16@\"MCPeerID\"24@\"NSData\"32@?<v@?B@\"MCSession\">40"
- "v48@0:8@\"MCSession\"16@\"NSArray\"24@\"MCPeerID\"32@?<v@?B>40"
- "v48@0:8@\"MCSession\"16@\"NSInputStream\"24@\"NSString\"32@\"MCPeerID\"40"
- "v48@0:8@\"MCSession\"16@\"NSString\"24@\"MCPeerID\"32@\"NSProgress\"40"
- "v48@0:8@16@24@32@40"
- "v48@0:8@16@24@32@?40"
- "v56@0:8@\"MCSession\"16@\"NSString\"24@\"MCPeerID\"32@\"NSURL\"40@\"NSError\"48"
- "v56@0:8@16@24@32@40@48"
- "valueForKey:"
- "willConnectToRemotePeer:"
- "zone"

```
