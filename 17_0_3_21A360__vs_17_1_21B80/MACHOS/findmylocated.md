## findmylocated

> `/usr/libexec/findmylocated`

```diff

-62.0.4.0.0
-  __TEXT.__text: 0x298900
-  __TEXT.__auth_stubs: 0x3420
+63.1.7.0.0
+  __TEXT.__text: 0x2aff78
+  __TEXT.__auth_stubs: 0x3450
   __TEXT.__objc_methlist: 0x2c
-  __TEXT.__cstring: 0xe7eb
-  __TEXT.__swift5_typeref: 0x2ec8
-  __TEXT.__swift5_fieldmd: 0x3654
-  __TEXT.__const: 0x8fb2
-  __TEXT.__constg_swiftt: 0x2bc0
+  __TEXT.__cstring: 0xf2ab
+  __TEXT.__swift5_typeref: 0x2f3a
+  __TEXT.__swift5_fieldmd: 0x3760
+  __TEXT.__const: 0x91f2
+  __TEXT.__constg_swiftt: 0x2c7c
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_reflstr: 0x2e75
+  __TEXT.__swift5_reflstr: 0x2f45
   __TEXT.__swift5_assocty: 0x2e8
-  __TEXT.__swift5_protos: 0x3c
-  __TEXT.__swift5_proto: 0x948
+  __TEXT.__swift5_protos: 0x40
+  __TEXT.__swift5_proto: 0x974
   __TEXT.__swift5_types: 0x2bc
-  __TEXT.__objc_methname: 0x17e2
+  __TEXT.__objc_methname: 0x17d0
   __TEXT.__objc_classname: 0xa3
   __TEXT.__objc_methtype: 0x7a7
-  __TEXT.__swift5_capture: 0x1b40
+  __TEXT.__swift5_capture: 0x1bb4
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0xbab4
-  __TEXT.__eh_frame: 0x21f18
-  __DATA_CONST.__auth_got: 0x1a10
-  __DATA_CONST.__got: 0xdd8
+  __TEXT.__unwind_info: 0xb6c0
+  __TEXT.__eh_frame: 0x23978
+  __DATA_CONST.__auth_got: 0x1a28
+  __DATA_CONST.__got: 0xdd0
   __DATA_CONST.__auth_ptr: 0x218
-  __DATA_CONST.__const: 0xa800
+  __DATA_CONST.__const: 0xab30
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__linkguard: 0x15
-  __DATA.__objc_const: 0x2c00
-  __DATA.__objc_selrefs: 0x440
+  __DATA.__objc_const: 0x2c80
+  __DATA.__objc_selrefs: 0x438
   __DATA.__objc_protorefs: 0x80
   __DATA.__objc_classrefs: 0x158
   __DATA.__objc_data: 0xc20
-  __DATA.__data: 0x8a58
-  __DATA.__bss: 0x12900
-  __DATA.__common: 0xb30
+  __DATA.__data: 0x8c90
+  __DATA.__bss: 0x12e80
+  __DATA.__common: 0xb58
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 9446
-  Symbols:   1590
-  CStrings:  1554
+  Functions: 9723
+  Symbols:   1595
+  CStrings:  1603
 
Symbols:
+ _$s10FindMyBase11XPCActivityC8CriteriaVMn
+ _$s10FindMyBase23OnceCheckedContinuationC6resume8throwingyq__tF
+ _$s10FindMyBase23OnceCheckedContinuationC6resumeyyytRszrlF
+ _$s10FindMyBase23OnceCheckedContinuationCMn
+ _$s10FindMyBase35withOnceCheckedThrowingContinuation8function_xSS_yAA0efH0Cyxs5Error_pGYbXEtYaKlF
+ _$s10FindMyBase35withOnceCheckedThrowingContinuation8function_xSS_yAA0efH0Cyxs5Error_pGYbXEtYaKlFTu
+ _$s19FindMyDaemonSupport0C0C6sharedACvgZ
+ _$s8Dispatch0A3QoSV10backgroundACvgZ
+ _$ss6ResultOMn
- _$s10FindMyBase10SystemInfoO9deviceSKUSSSgvgZ
- _$s10FindMyBase42withCancellableCheckedThrowingContinuationyxyScCyxs5Error_pGYbXEYaKs8SendableRzlF
- _$s10FindMyBase42withCancellableCheckedThrowingContinuationyxyScCyxs5Error_pGYbXEYaKs8SendableRzlFTu
- _$s12FindMyLocate17FriendshipRequestVs23CustomStringConvertibleAAMc
CStrings:
+ "\nserverContext: "
+ "%s succeeded!"
+ "%{private,mask.hash}s legacy locations count: %ld."
+ "%{public}s Checking if we should send to %{public}s"
+ "%{public}s completed with %{public}s"
+ "%{public}s entered queue."
+ "%{public}s error: %{private,mask.hash}s"
+ "%{public}s from %{private,mask.hash}s\nlocal peerToken: %{public}s doesn't match with recieved peerToken: %{public}@, ignore it"
+ "%{public}s no more active session for %{public}s handle: %{private,mask.hash}s. Need to unsubscribe."
+ "%{public}s not eligible, since we have non-nil serverSettings already."
+ "%{public}s receive state .run"
+ "%{public}s request priority: %{public}s"
+ "%{public}s should not schedule legacyRefresh"
+ "%{public}s statusCode: %s"
+ "%{public}s subscription successful. With location? %{bool}d"
+ "%{public}s to device: %{public}s"
+ "%{public}s token: %{private,mask.hash}@"
+ "%{public}s type: %{public}s shouldRefresh: %{bool,public}d"
+ "%{public}s with empty handles"
+ "After process, current legacyLocations count: %ld."
+ "CommandManager %{public}s\nrequest: %{public}s\nresponse: %s"
+ "CommandManager %{public}s\nresponse: %s"
+ "CommandManager %{public}s no refresh request left in the coalescedCommands"
+ "CommandManager %{public}s request: %{private,mask.hash}s"
+ "CommandManager %{public}s response: %s"
+ "CommandManager %{public}s result: %s"
+ "CommandManager %{public}s with\nserverId:%{private,mask.hash}s\nresponse: %s"
+ "CommandManager server response contains mapping packet with token %{private,mask.hash}s for handleId:%{private,mask.hash}s"
+ "Current Device locationEnabled? %{bool,public}d"
+ "Current Device meDevice? %{bool}d"
+ "Current Device newFriendshipRequestsAllowed? %{bool,public}d"
+ "Current MeDevice isActive? %{bool}d"
+ "DataManager load LocalStorage friends with types %{public}s count:%ld"
+ "DataManager load friends not checking expiry with types %{public}s"
+ "DataManager: `PostInstall` activity defer"
+ "DataManager: `PostInstall` activity run"
+ "DataManager: start checking in `PostInstall` XPC activity"
+ "Exceeded retry limit: %ld"
+ "Force refreshClient call failed with %{public}s\nre-register an XPC activity fired after %{public}f"
+ "Force refreshClient call succeed, terminate scheduling XPC Activity to force refreshClient."
+ "Force refreshClient, since we have nil server settings in local DB."
+ "FriendService: send Friends Update to all clients:\nclients count:%ld\nhandle: %{private,mask.hash}s\ntype: %{public}s\nby: %{public}s"
+ "Get legacy latest location for handle: %{private,mask.hash}s"
+ "Invalid status code: %ld"
+ "LocalStorageService shouldForceRefreshClient: %{bool,public}dsettings %{private,mask.hash}s"
+ "LocalStorageService write new serverSettings\nmyInfo: %{public}s\nprefs: %{private,mask.hash}s\ncontext: %{private,mask.hash}s\nconfig: %{private,mask.hash}s"
+ "LocationService: send handles with unavailable locations to all clients:\nclients count:%ld\nunavailable handles count:%ld"
+ "LocationService: send location Update for handle: %{private,mask.hash}s"
+ "LocationService: send locations Update to all clients:\nclients count:%ld\nupdates count:%ld"
+ "LocationService: send unavailable location Update for handle: %{private,mask.hash}s"
+ "Me device: %{private,mask.hash}s\nisThisDevice? %{bool,public}d\nisActive? %{bool,public}d"
+ "Need to renew credentials. Retry count: %ld"
+ "No legacy location return from server, should not process."
+ "Not %{public}s to server since no client is interested legacy refresh"
+ "Not %{public}s to server since no clients connected"
+ "Not %{public}s to server since no followings"
+ "Not update cached legacy location for handle: %{private,mask.hash}s\nsince new location location date: %{private,mask.hash}s\nis older cached date: %{private,mask.hash}s."
+ "One-shot %{public}s pulled from daemon cache on disk\nfor handle: %{private,mask.hash}s"
+ "REQUEST: %s"
+ "RESPONSE: %s"
+ "Read LocalStorage serverSettings:\nmyInfo: %{public}s\nprefs: %{private,mask.hash}s\ncontext: %{private,mask.hash}s\nconfig: %{private,mask.hash}s"
+ "Received refresh client response: %s"
+ "Renewing credentials..."
+ "Retry sending command to %s %s"
+ "Scheduling resubscription for %{private,mask.hash}s after %{public}s priority: %{public}s"
+ "Start Refresh Location with priority: %{public}s for"
+ "State: %{public}s -> %{public}s"
+ "TRACE: removeSubscription: client: %s\npriority: %{public}s handle: %{private,mask.hash}s"
+ "TRACE: trackNewSubscription: client: %s\npriority: %{public}s handle: %{private,mask.hash}s"
+ "Unable to send IDS Mapping packet for handleId:%{private,mask.hash}s due to %{public}@"
+ "Unhandled status: %{public}s"
+ "Unsubscribe %s for handle: %{private,mask.hash}s"
+ "Unsubscribing %{public}s friend: %{private,mask.hash}s"
+ "XPCForceActivityIntervalInSeconds"
+ "`siblingIdentifiers` is empty for %s!"
+ "check if settings From Storage is nil"
+ "checkInPostInstallXPCActivity"
+ "com.apple.findmy.findmylocate.ForceRefreshClient"
+ "com.apple.findmy.findmylocated.post-install"
+ "dataManagerStateStream: sharing current secure locations key with new follower,\nhandleId: %{private,mask.hash}s\nserverID: %{private,mask.hash}s,\nidsHandles: %{private,mask.hash}s"
+ "exceededRetryLimit"
+ "forceRefreshClientActivity"
+ "forceRefreshClientWithThresholdWhenNoServerSettingsIfNeeded()"
+ "forceRefreshCriteria(_:)"
+ "handleServerResponseStatus(endpoint:content:response:)"
+ "legacy location Request for: %{private,mask.hash}s"
+ "locationUpdateQueue"
+ "migrationPerformed"
+ "myInfo: %s"
+ "priority: %{private,mask.hash}s: :%{private,mask.hash}s"
+ "priority: %{public}s): :%{private,mask.hash}s"
+ "receiveFindingToken error: %{public}@"
+ "registerForceRefreshClientActivity()"
+ "respondToFindingTokenRequest error: %{public}@"
+ "retryCount"
+ "revokeFindingToken error: %{public}@"
+ "secure location Request for: %{private,mask.hash}s"
+ "sendFriendshipOffer type: %{public}s\nto handle: %{private,mask.hash}s"
+ "sendToClients unavailableHandles error: %{public}@"
+ "sendToClients(locationsForHandles:)"
+ "sendToClients(unavailableHandles:)"
+ "serverSettings drop error %{public}@"
+ "startLatestLocationTask(_:with:)"
+ "stopRefresh priority: %{public}s for %{private,mask.hash}s"
+ "stopRefreshing: no handles to unsubscribe %{public}s"
+ "stopRefreshingLocation LegacyRefresh handle count: %ld"
+ "write(serverSettings:)"
- "%s error: %{private,mask.hash}s"
- "%s should not schedule legacyRefresh"
- "%s subscription successful. With location? %{bool}d"
- "%s with empty handles"
- "%{private,mask.hash}s legacy locations count: %{public}ld"
- "%{public}s\nlegacy location Request: %{private,mask.hash}s\nsecure location request: %{private,mask.hash}s"
- "%{public}s from %{mask.hash}s\nlocal peerToken: %{public}s doesn't match with recieved peerToken: %{public}@, ignore it"
- "%{public}s no more active session for %{public}s handles: %{private,mask.hash}s. Need to unsubscribe."
- "%{public}s request: %s"
- "%{public}s token: %{mask.hash}@"
- "%{public}s, not write serverSettings since no updates"
- "After process, current legacyLocations: %{private,mask.hash}s"
- "CommandManager %s no refresh request left in the coalescedCommands"
- "CommandManager %s request: %{private,mask.hash}s"
- "CommandManager %s response: %{private,mask.hash}s"
- "CommandManager %{public}s\nrequest: %{public}s\nresponse: %{private,mask.hash}s"
- "CommandManager %{public}s\nresponse: %{private,mask.hash}s"
- "CommandManager %{public}s response: %{private,mask.hash}s"
- "CommandManager %{public}s result: %{private,mask.hash}s"
- "CommandManager %{public}s with\nserverId:%{private,mask.hash}s\nresponse: %{private,mask.hash}s"
- "CommandManager server response contains mapping packet with\ntoken %{private,mask.hash}s\nfor handleId:%{private,mask.hash}s"
- "DataManager load LocalStorage friends with types %s count:%ld"
- "DataManager load friends not checking expiry with types %s"
- "FriendService: send Friends Update to all clients:\nclients count:%ld\nupdates:%{private,mask.hash}s"
- "Legacy latest location: %{private,mask.hash}s"
- "LocalStorageSerivice write new serverSettings\nprefs: %{private,mask.hash}s\ncontext: %{private,mask.hash}s\nconfig: %{private,mask.hash}s"
- "LocalStorageService shouldForceRefreshClient: %{bool,public}dsettings %{mask.hash}s"
- "LocationService: send handles with unavailable locations to all clients:\nclients count:%ld\nunavailable handles:%{private,mask.hash}s"
- "LocationService: send locations Update to all clients:\nclients count:%ld\nupdates:%{private,mask.hash}s"
- "Me device: %{private,mask.hash}s"
- "No legacy location return from server, should not process"
- "Not %s to server since no client is interested legacy refresh"
- "Not %s to server since no clients connected"
- "Not %s to server since no followings"
- "Not update cached legacy location for handle: %{private,mask.hash}s\nsince new location location date: %{private,mask.hash}s\nis older cached date: %{private,mask.hash}s"
- "One-shot %{public}s pulled from the daemon cache on disk for handles: %s"
- "REQUEST: %{public}s"
- "RESPONSE: %{public}s"
- "Read LocalStorage serverSettings:\nprefs: %{private,mask.hash}s\ncontext: %{private,mask.hash}s\nconfig: %{private,mask.hash}s"
- "Received refresh client response: %{public}s"
- "Request content: %{private,mask.hash}s"
- "Scheduling resubscription for %{private,mask.hash}s after %s priority: %s"
- "Sending %s to server"
- "ServerContext: %s"
- "TRACE: removeSubscription: client: %s priority: %s handles: %s"
- "TRACE: trackNewSubscription: client: %s priority: %s handles: %s"
- "Unable to sending IDS Mapping packet due to %{public}s"
- "Unsubscribe %s for handles: %{private,mask.hash}s"
- "Unsubscribing %s friends: %s"
- "dataManagerStateStream: sharing current secure locations key with new follower,\nserverID: %{private,mask.hash}s,\nidsHandles: %{private,mask.hash}s"
- "migrationPeformed"
- "priority: %{mask.hash}s: :%{private,mask.hash}s"
- "processIdentifier"
- "sendFriendshipOffer: %{public}s"
- "stopRefresh for %{private,mask.hash}s"
- "stopRefreshing: no handles to unsubscribe %s"
- "stopRefreshingLocation LegacyRefresh handle count: %{public}ld"
- "write(with:serverContext:serverPrefs:)"

```
