## seld

> `/usr/libexec/seld`

```diff

-365.3.1.0.0
-  __TEXT.__text: 0x291fc
-  __TEXT.__auth_stubs: 0x840
-  __TEXT.__objc_stubs: 0x3340
+370.33.1.0.0
+  __TEXT.__text: 0x27448
+  __TEXT.__auth_stubs: 0x8c0
+  __TEXT.__objc_stubs: 0x33e0
   __TEXT.__objc_methlist: 0xef4
-  __TEXT.__const: 0x1b0
-  __TEXT.__objc_methname: 0x3900
-  __TEXT.__cstring: 0x428a
-  __TEXT.__oslogstring: 0x3fe2
-  __TEXT.__objc_classname: 0x255
+  __TEXT.__const: 0x1b8
+  __TEXT.__objc_methname: 0x3996
+  __TEXT.__cstring: 0x4551
+  __TEXT.__oslogstring: 0x4157
+  __TEXT.__objc_classname: 0x234
   __TEXT.__objc_methtype: 0xced
-  __TEXT.__unwind_info: 0x4e0
-  __DATA_CONST.__auth_got: 0x428
-  __DATA_CONST.__got: 0x230
-  __DATA_CONST.__const: 0x9b8
-  __DATA_CONST.__cfstring: 0x20c0
+  __TEXT.__unwind_info: 0x440
+  __DATA_CONST.__const: 0xa98
+  __DATA_CONST.__cfstring: 0x2420
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0xa0
   __DATA_CONST.__objc_dictobj: 0x168
   __DATA_CONST.__objc_arrayobj: 0x18
+  __DATA_CONST.__auth_got: 0x468
+  __DATA_CONST.__got: 0x238
   __DATA.__objc_const: 0x1ea0
-  __DATA.__objc_selrefs: 0xf70
+  __DATA.__objc_selrefs: 0xf98
   __DATA.__objc_ivar: 0x1dc
   __DATA.__objc_data: 0x370
   __DATA.__data: 0x4e0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8ACCB5DD-8521-3644-94C9-C61BCBFCBE8D
+  UUID: 5B2C6A0F-1723-3B23-A50B-6A134BF142DC
   Functions: 367
-  Symbols:   213
-  CStrings:  1999
+  Symbols:   222
+  CStrings:  2059
 
Symbols:
+ _OBJC_CLASS_$_NSProcessInfo
+ _dispatch_queue_set_specific
+ _free
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x5
+ _objc_retain_x8
+ _xpc_copy_description
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "%@ topic recv (%lf)"
+ "%@ {batchId=%@ taskid=%@ redirectUrl=%@ version=%@ httpStatus=%@ spStatus=%@ step=%d retryAfter=%f pendingImmediateRetry=%d}"
+ "%@, requested identifiers=%@"
+ "%s update"
+ "%s, server=%@, time=%f"
+ "%s, time=%f"
+ "%s: beforeBlockExec=%{bool}d\n%@"
+ "%{public}s:%i %s is enabled (CONSTRAINED=%{bool}d, EXPENSIVE=%{bool}d)"
+ "%{public}s:%i %{public}@ (%lf)"
+ "%{public}s:%i %{public}@ => %{public}@ (%lf)"
+ "%{public}s:%i %{public}s%{public}@"
+ "%{public}s:%i (%lf)"
+ "%{public}s:%i Exceeded session acquisition time expectation (%llu)."
+ "%{public}s:%i Failed getting SELD info (%lf)"
+ "%{public}s:%i Failed to register: %{public}s %{public}s %{public}s"
+ "%{public}s:%i HTTP status: %ld"
+ "%{public}s:%i Invalid object for JSON serialization"
+ "%{public}s:%i Invalid token"
+ "%{public}s:%i Missing expected state info from %{public}@"
+ "%{public}s:%i No event name: skipping %{public}s"
+ "%{public}s:%i No server for applet: %{public}@ (%lf)"
+ "%{public}s:%i Processing %{public}@ (%lf)"
+ "%{public}s:%i Processing server connection request from %{public}@ (%lf)"
+ "%{public}s:%i Queue _startNextSession, reason=\"%{public}@\""
+ "%{public}s:%i Queue _startNextSession."
+ "%{public}s:%i Running through delayed XPCs"
+ "%{public}s:%i Server connection request from %{public}@ (%lf)"
+ "%{public}s:%i URL: %{public}@, Client error: %{public}@ - %{public}@"
+ "%{public}s:%i [TSM] NextState=%@, reason=\"%{public}@\""
+ "%{public}s:%i [TSM] No remaining sessions. reason=\"%{public}@\""
+ "%{public}s:%i [TSM] URL: %{public}@, Server response HTTP status: %ld"
+ "%{public}s:%i [TSM] [TSM] Empty body."
+ "%{public}s:%i _startNextSession is already in queued up, reason=\"%{public}@\""
+ "%{public}s:%i default = %{public}@ (%lf)"
+ "%{public}s:%i identifier : %{public}@ (%lf)"
+ "%{public}s:%i notif: %{public}s"
+ "%{public}s:%i url: %{public}@ (%lf)"
+ "-[_NFRemoteAdminManager _connectToServer:initialClientRequestInfo:sessionToken:epoch:activityBoost:completion:]"
+ "-[_NFRemoteAdminManager _connectToServer:initialClientRequestInfo:sessionToken:epoch:activityBoost:completion:]_block_invoke"
+ "-[_NFRemoteAdminManager _getSELDInfoForBrokerWithEpoch:activityBoost:completion:]_block_invoke"
+ "-[_NFRemoteAdminManager _ingestCard:epoch:callback:]"
+ "-[_NFRemoteAdminManager _ingestCard:epoch:callback:]_block_invoke"
+ "-[_NFRemoteAdminManager _nextRequestForServer:epoch:completion:]"
+ "-[_NFRemoteAdminManager _nextRequestForServer:epoch:completion:]_block_invoke"
+ "-[_NFRemoteAdminManager _queueNFRemoteAdminStateForServerIdentifiers:reason:]_block_invoke"
+ "-[_NFRemoteAdminManager _queueServerConnection:epoch:callback:]"
+ "-[_NFRemoteAdminManager _queueServerConnectionForApplets:epoch:completion:]"
+ "-[_NFRemoteAdminManager _queueStartNextSession:]"
+ "-[_NFRemoteAdminManager _startNextSession:]"
+ "APS connection status update: connected"
+ "APS inited"
+ "Adapter changed notified"
+ "Battery level update (%lf)."
+ "Charging state update (%lf)."
+ "Delete %@ (%lf)"
+ "Delete all %s applets (%lf)"
+ "Delete all applets (%lf)"
+ "Location service is not authorized"
+ "Location simulation detected"
+ "NF hardware state update success"
+ "New APN token"
+ "Queue %@ (%lf)"
+ "Queue for applets %@ (%lf)"
+ "Queue on ingest card after redirect is completed, %@ (%lf)"
+ "Queue on ingest card, %@ (%lf)"
+ "Queue on pending ingest card, %@ (%lf)"
+ "Request Header: "
+ "Requeue after processing %@ (%lf)"
+ "Requeue after processing %@ using child session (%lf)"
+ "Response Header: "
+ "Restricted mode entered (%lf)"
+ "Restricted mode exited (%lf)"
+ "Restricted performance mode entered (%lf)"
+ "System powered on"
+ "Unexpected result, exiting"
+ "User has denied access to location services"
+ "_connectToServer:initialClientRequestInfo:sessionToken:epoch:activityBoost:completion:"
+ "allObjects"
+ "beginActivityWithOptions:reason:"
+ "com.apple.seld.alarm triggered"
+ "com.apple.seld.osupdate triggered"
+ "com.apple.seld.processing triggered"
+ "endActivity:"
+ "initWithBytesNoCopy:length:encoding:freeWhenDone:"
+ "primary region topic %@ update (%lf)"
+ "processInfo"
+ "queuedXPC"
+ "timeIntervalSince1970"
+ "{ServerId: %@, retryInterval: %@, immediate: %s, unsent: %s, sourceURL: %@}"
- "%@ { batchId=%@ taskid=%@ redirectUrl=%@ version=%@ httpStatus=%@ spStatus=%@ step=%d retryAfter=%f pendingImmediateRetry=%d}"
- "%s: beforeBlockExec=%d\n%@"
- "%{public}s:%i %s %s"
- "%{public}s:%i %s is enabled"
- "%{public}s:%i %s network is constrained"
- "%{public}s:%i %s network is expensive"
- "%{public}s:%i %{public}@ => %{public}@"
- "%{public}s:%i Adding _startNextSession to SessionQueue."
- "%{public}s:%i Charging state changed"
- "%{public}s:%i Exceeded session acquisition time expectation."
- "%{public}s:%i Failed getting SELD info"
- "%{public}s:%i Failed to register %@"
- "%{public}s:%i HTTP status: %{public}@"
- "%{public}s:%i Inalid token"
- "%{public}s:%i Listening for battery notifications"
- "%{public}s:%i No event name: skipping"
- "%{public}s:%i No server for applet: %{public}@"
- "%{public}s:%i Processing server connection request from %{public}@"
- "%{public}s:%i Runnning through delayed XPCs"
- "%{public}s:%i Server connection request from %{public}@"
- "%{public}s:%i Unexpected result, exiting"
- "%{public}s:%i [TSM] NextState=%@"
- "%{public}s:%i [TSM] No remaining sessions."
- "%{public}s:%i [TSM] Request Header: %@"
- "%{public}s:%i [TSM] Response Header: %@"
- "%{public}s:%i [TSM] Server response HTTP status: %ld"
- "%{public}s:%i [TSM] URL: %@"
- "%{public}s:%i identifier : %{public}@"
- "%{public}s:%i notif: %s"
- "%{public}s:%i url: %{public}@"
- "-[_NFRemoteAdminManager _connectToServer:initialClientRequestInfo:sessionToken:completion:]"
- "-[_NFRemoteAdminManager _connectToServer:initialClientRequestInfo:sessionToken:completion:]_block_invoke"
- "-[_NFRemoteAdminManager _getSELDInfoForBrokerWithCompletion:]_block_invoke"
- "-[_NFRemoteAdminManager _ingestCard:callback:]"
- "-[_NFRemoteAdminManager _ingestCard:callback:]_block_invoke"
- "-[_NFRemoteAdminManager _nextRequestForServer:completion:]"
- "-[_NFRemoteAdminManager _nextRequestForServer:completion:]_block_invoke"
- "-[_NFRemoteAdminManager _queueNFRemoteAdminStateForServerIdentifiers:]_block_invoke"
- "-[_NFRemoteAdminManager _queueServerConnection:callback:]"
- "-[_NFRemoteAdminManager _queueServerConnectionForApplets:completion:]"
- "-[_NFRemoteAdminManager _queueStartNextSession]"
- "-[_NFRemoteAdminManager _startNextSession]"
- "-[_NFRemoteAdminManager _sync_deleteAllAppletsAndCleanupWithTSM:completion:]"
- "-[_NFRemoteAdminManager _sync_deleteAppletsAndCleanupWithTSM:parentSessionToken:completion:]"
- "-[_NFRemoteAdminManager listenForBatteryChanges]"
- "-[_NFRemoteAdminManager listenForBatteryChanges]_block_invoke_2"
- "-[_NFRemoteAdminManager restrictedModeEntered:]"
- "-[_NFRemoteAdminManager restrictedModeExited]"
- "Delete %@"
- "Delete all %s applets"
- "Delete all applets"
- "QueuedXPC"
- "UTF8String"
- "_connectToServer:initialClientRequestInfo:sessionToken:completion:"
- "initAPSCompletionHandler"
- "{ServerId: %@, retryInterval: %@, immediate: %s, unsent: %s, sourceURL: %@"

```
