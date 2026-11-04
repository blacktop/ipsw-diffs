## sharingd

> `/usr/libexec/sharingd`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`

```diff

-2131.21.31.2.5
-  __TEXT.__text: 0x67d114
-  __TEXT.__auth_stubs: 0xb230
-  __TEXT.__objc_stubs: 0x37980
-  __TEXT.__objc_methlist: 0x1e6cc
-  __TEXT.__cstring: 0x3f541
-  __TEXT.__objc_methname: 0x4ef85
-  __TEXT.__objc_classname: 0x5b67
-  __TEXT.__objc_methtype: 0xbce2
-  __TEXT.__const: 0x160d8
+2131.30.43.2.1
+  __TEXT.__text: 0x681958
+  __TEXT.__auth_stubs: 0xb240
+  __TEXT.__objc_stubs: 0x37a20
+  __TEXT.__objc_methlist: 0x1e7ac
+  __TEXT.__cstring: 0x3f651
+  __TEXT.__objc_methname: 0x4f1b5
+  __TEXT.__objc_classname: 0x5b57
+  __TEXT.__objc_methtype: 0xbcd2
+  __TEXT.__const: 0x16108
   __TEXT.__gcc_except_tab: 0x68e0
-  __TEXT.__oslogstring: 0x3d973
+  __TEXT.__oslogstring: 0x3deb8
   __TEXT.__ustring: 0x94
   __TEXT.__dlopen_cstrs: 0x438
-  __TEXT.__swift5_typeref: 0x8186
-  __TEXT.__swift5_fieldmd: 0x604c
-  __TEXT.__constg_swiftt: 0x79c8
+  __TEXT.__swift5_typeref: 0x81c0
+  __TEXT.__swift5_fieldmd: 0x6094
+  __TEXT.__constg_swiftt: 0x7a28
   __TEXT.__swift5_builtin: 0x2f8
-  __TEXT.__swift5_reflstr: 0x5b59
+  __TEXT.__swift5_reflstr: 0x5c27
   __TEXT.__swift5_assocty: 0xcf0
   __TEXT.__swift5_protos: 0xd4
   __TEXT.__swift5_proto: 0xce0
   __TEXT.__swift5_types: 0x5fc
-  __TEXT.__swift_as_entry: 0xe60
-  __TEXT.__swift_as_cont: 0x2230
-  __TEXT.__swift5_capture: 0x52a4
-  __TEXT.__swift_as_ret: 0xf78
+  __TEXT.__swift_as_entry: 0xe68
+  __TEXT.__swift_as_cont: 0x2240
+  __TEXT.__swift5_capture: 0x52dc
+  __TEXT.__swift_as_ret: 0xf88
   __TEXT.__swift5_mpenum: 0x24
-  __TEXT.__unwind_info: 0x19cf0
-  __TEXT.__eh_frame: 0x259ec
-  __DATA_CONST.__const: 0x1ce58
-  __DATA_CONST.__cfstring: 0x19940
+  __TEXT.__unwind_info: 0x19d68
+  __TEXT.__eh_frame: 0x25a74
+  __DATA_CONST.__const: 0x1cf78
+  __DATA_CONST.__cfstring: 0x19960
   __DATA_CONST.__objc_classlist: 0xe20
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x748

   __DATA_CONST.__objc_dictobj: 0x1720
   __DATA_CONST.__objc_arrayobj: 0x720
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA_CONST.__auth_got: 0x5928
+  __DATA_CONST.__auth_got: 0x5930
   __DATA_CONST.__got: 0x3b78
-  __DATA_CONST.__auth_ptr: 0x4490
-  __DATA.__objc_const: 0x38860
-  __DATA.__objc_selrefs: 0x111a0
-  __DATA.__objc_ivar: 0x2950
-  __DATA.__objc_data: 0xa208
-  __DATA.__data: 0x14bc8
-  __DATA.__common: 0x978
+  __DATA_CONST.__auth_ptr: 0x4488
+  __DATA.__objc_const: 0x389d8
+  __DATA.__objc_selrefs: 0x11200
+  __DATA.__objc_ivar: 0x2960
+  __DATA.__objc_data: 0xa3b8
+  __DATA.__data: 0x14b38
+  __DATA.__common: 0x980
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 26482
-  Symbols:   5089
-  CStrings:  27667
+  Functions: 26535
+  Symbols:   5090
+  CStrings:  27717
 
Symbols:
+ _$s16AutoUnlockDaemon23SDAuthenticationManagerC19idsDevicesDidChangeyyF
+ _$s7Sharing21SFAirDropUserDefaultsC16liveActivitiesUISbvg
+ _nw_http3_set_idle_timeout
- _$s7Sharing9SFAirDropO14NetworkMetricsV3log19senderTLSCertDigestySS_tF
- _$s7Sharing9SFAirDropO14NetworkMetricsV3log21receiverTLSCertDigestySS_tF
CStrings:
+ "AIRDROP_ITEM_FROM_TEXT"
+ "AutoUnlockTransportDevicesChanged"
+ "Failed to get known device identities: %@"
+ "Failed to register for SpringBoard finishedstartup with status %u, Pencil Pairing Angel will not launch"
+ "Failed to register for SpringBoard finishedstartup with status %u, not prewarming Pencil Pairing Angel"
+ "Ignoring message for stale session ID: %@ (current session ID: %@)"
+ "Never heard back, sending failed SDUnlockSessionConfirmation"
+ "Not waking Pencil Pairing Angel for %s, SpringBoard hasn't finished startup"
+ "Pencil Pairing Server requested a relaunch, resending attach in 1s"
+ "ProximityServiceThirdPartyHomeSetup"
+ "Received SpringBoard finishedstartup notification"
+ "Removing legacy persisted Stream ID"
+ "Rendezvous name issued too recently to rotate"
+ "Rotated rendezvous name"
+ "Skipping AirDropUI activateConnection because transfer UI should be handled by notifications"
+ "Skipping AirDropUI endConnection because transfer UI should be handled by notifications"
+ "Skipping AirDropUI launch because transfer UI should be handled by notifications"
+ "Skipping AirDropUI update because transfer UI should be handled by notifications"
+ "Skipping airDropUIServer because transfer UI should be handled by notifications"
+ "SpringBoard (pid %llu) finished startup, prewarming Pencil Pairing Angel in 5s"
+ "SpringBoard hasn't finished startup, deferring Pencil Pairing Angel prewarm"
+ "T@\"NSString\",&,V_rendezvousName"
+ "TB,V_sentInitialRequest"
+ "Td,V_rendezvousNameIssuedAt"
+ "T{os_unfair_lock_s=I},R,N,V_rendezvousLock"
+ "_rendezvousLock"
+ "_rendezvousName"
+ "_rendezvousNameIssuedAt"
+ "_sentInitialRequest"
+ "accessoryDidConnect()"
+ "accessoryDidDetach()"
+ "addParticipantsAllowedForURL:share:auditToken:completionHandler:"
+ "com.apple.springboard.finishedstartup"
+ "currentRendezvousName"
+ "deviceDidUnlock()"
+ "didReceiveLowPowerUpdate(source:)"
+ "idsDevicesChangedObserver"
+ "knownDeviceIDsBrowseStart"
+ "prewarmedSBPID"
+ "rendezvousLock"
+ "rendezvousName"
+ "rendezvousNameIssuedAt"
+ "rendezvousNameWithReply:"
+ "requestRelaunchAfterExit"
+ "rotateRendezvousNameIfIdle"
+ "sbFinishedStartupToken"
+ "sentInitialRequest"
+ "setRendezvousName:"
+ "setRendezvousNameIssuedAt:"
+ "setSentInitialRequest:"
+ "tokenFromNSXPCConnection:"
+ "v24@0:8@?<v@?@\"NSString\">16"
+ "v40@0:8@\"NSString\"16@\"<SFCompanionServiceManagerClient>\"24@?<v@?@\"<SFCompanionServiceManagerProtocol>\"@\"NSString\"@\"NSString\"@\"NSError\">32"
- "addParticipantsAllowedForURL:share:completionHandler:"
- "receiverDeviceType"
- "v40@0:8@\"NSString\"16@\"<SFCompanionServiceManagerClient>\"24@?<v@?@\"<SFCompanionServiceManagerProtocol>\"@\"NSString\"@\"NSString\"@\"NSString\"@\"NSError\">32"
```
