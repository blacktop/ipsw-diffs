## IDS

> `/System/Library/PrivateFrameworks/IDS.framework/IDS`

```diff

-1814.200.71.2.7
-  __TEXT.__text: 0x113920
+1814.300.81.2.2
+  __TEXT.__text: 0x11484c
   __TEXT.__auth_stubs: 0x1aa0
-  __TEXT.__objc_methlist: 0x8980
+  __TEXT.__objc_methlist: 0x8ab0
   __TEXT.__const: 0x2b8
-  __TEXT.__gcc_except_tab: 0x3230
-  __TEXT.__oslogstring: 0x1604b
-  __TEXT.__cstring: 0xef7a
+  __TEXT.__gcc_except_tab: 0x3240
+  __TEXT.__oslogstring: 0x1611a
+  __TEXT.__cstring: 0xefc3
   __TEXT.__dlopen_cstrs: 0x102
   __TEXT.__ustring: 0xac
-  __TEXT.__unwind_info: 0x40c0
-  __TEXT.__objc_classname: 0x1329
-  __TEXT.__objc_methname: 0x1a056
-  __TEXT.__objc_methtype: 0x63a5
-  __TEXT.__objc_stubs: 0x10dc0
+  __TEXT.__unwind_info: 0x4100
+  __TEXT.__objc_classname: 0x132b
+  __TEXT.__objc_methname: 0x1a94a
+  __TEXT.__objc_methtype: 0x6487
+  __TEXT.__objc_stubs: 0x11020
   __DATA_CONST.__got: 0x9a0
-  __DATA_CONST.__const: 0x4330
+  __DATA_CONST.__const: 0x4390
   __DATA_CONST.__objc_classlist: 0x430
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x188
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2eca0
-  __DATA_CONST.__objc_selrefs: 0x5558
+  __DATA_CONST.__objc_const: 0x2ed20
+  __DATA_CONST.__objc_selrefs: 0x5638
   __AUTH_CONST.__objc_const: 0x31c0
-  __AUTH_CONST.__cfstring: 0x6200
+  __AUTH_CONST.__cfstring: 0x6240
   __AUTH_CONST.__const: 0x1220
   __AUTH_CONST.__objc_intobj: 0x3d8
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__auth_got: 0xd60
   __AUTH.__objc_data: 0x1630
   __DATA.__objc_protorefs: 0xa8
-  __DATA.__objc_classrefs: 0x728
+  __DATA.__objc_classrefs: 0x738
   __DATA.__objc_superrefs: 0x358
-  __DATA.__objc_ivar: 0xa80
+  __DATA.__objc_ivar: 0xa7c
   __DATA.__data: 0x1350
   __DATA.__bss: 0x199c
   __DATA_DIRTY.__objc_data: 0x13b0

   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 5454
-  Symbols:   1361
-  CStrings:  7779
+  Functions: 5483
+  Symbols:   1365
+  CStrings:  7820
 
Symbols:
+ _IDSSendMessageOptionForceQuery
+ _IDSSendMessageOptionKTVerificationUUIDKey
+ _OBJC_CLASS_$_IDSCacheClearRequest
+ _OBJC_CLASS_$_IDSCacheClearRequestContext
CStrings:
+ "\v"
+ "@52@0:8@16@24@32B40@44"
+ "Account enabled {account: %@}"
+ "Account has KT error, we're going to force disable it. { accountID: %@ }"
+ "B64@0:8@16@24@32@40@48@?56"
+ "B68@0:8@16@24@32@40B48@52@?60"
+ "B68@0:8@16@24@32B40@44@52@?60"
+ "B76@0:8@16@24@32@40@48B56@?60@?68"
+ "B80@0:8@16@24@32Q40@48@56@64@?72"
+ "B84@0:8@16@24@32@40B48B52B56B60B64@68@?76"
+ "IDSSendMessageOptionForceQuery"
+ "IDSSendMessageOptionKTVerificationUUIDKey"
+ "This has been deprecated, please adopt the preferredFromID query APIs"
+ "Transparency requested to clear IDS query cache. { Request: %@ }"
+ "_currentCachedRemoteDevicesForDestinations:service:preferredFromID:listenerID:"
+ "_currentIDStatusForDestination:service:preferredFromID:listenerID:"
+ "_currentIDStatusForDestination:service:preferredFromID:respectExpiry:listenerID:"
+ "_currentIDStatusForDestinations:service:preferredFromID:listenerID:"
+ "_currentIDStatusForDestinations:service:preferredFromID:respectExpiry:listenerID:"
+ "_currentRemoteDevicesForDestinations:service:preferredFromID:listenerID:queue:waitForReply:completionBlock:completionBlockWithError:"
+ "_idStatusForDestinations:service:preferredFromID:listenerID:allowRenew:respectExpiry:waitForReply:forceRefresh:bypassLimit:completionBlock:"
+ "_refreshIDStatusForDestination:service:preferredFromID:listenerID:"
+ "_refreshIDStatusForDestinations:service:preferredFromID:listenerID:"
+ "_refreshIDStatusForDestinations:service:preferredFromID:listenerID:allowRefresh:respectExpiry:waitForReply:forceRefresh:bypassLimit:queue:completionBlock:"
+ "_requestCachedStatusForDestinations:fromID:service:waitForReply:respectExpiry:listenerID:completionBlock:"
+ "_requestIDInfoForDestinations:fromID:service:infoTypes:options:listenerID:queue:completionBlock:"
+ "_sync_currentIDStatusForDestinations:service:preferredFromID:respectExpiry:listenerID:completionBlock:"
+ "_sync_currentRemoteDevicesForDestinations:service:preferredFromID:listenerID:completionBlock:"
+ "_sync_refreshIDStatusForDestinations:service:preferredFromID:listenerID:completionBlock:"
+ "cacheClearRequest:"
+ "currentIDStatusForDestination:service:preferredFromID:listenerID:queue:completionBlock:"
+ "currentIDStatusForDestination:service:preferredFromID:respectExpiry:listenerID:queue:completionBlock:"
+ "currentIDStatusForDestinations:service:preferredFromID:listenerID:queue:completionBlock:"
+ "currentIDStatusForDestinations:service:preferredFromID:respectExpiry:listenerID:queue:completionBlock:"
+ "currentRemoteDevicesForDestinations:service:preferredFromID:listenerID:queue:completionBlock:"
+ "currentRemoteDevicesForDestinations:service:preferredFromID:listenerID:queue:completionBlockWithError:"
+ "firewallCollaboratorForService:withCompletion:"
+ "firewallCollaboratorForService:withErrorHandler:"
+ "forceDisableAccount:"
+ "forceRefreshIDStatusForDestinations:service:preferredFromID:listenerID:queue:completionBlock:"
+ "idInfoForDestinations:service:preferredFromID:infoTypes:options:listenerID:queue:completionBlock:"
+ "nw_connection_receive_message: Null context"
+ "participantsForDestinations:service:preferredFromID:listenerID:queue:completionBlock:"
+ "q48@0:8@16@24@32@40"
+ "q52@0:8@16@24@32B40@44"
+ "refreshIDStatusForDestination:service:preferredFromID:listenerID:queue:completionBlock:"
+ "refreshIDStatusForDestinations:service:preferredFromID:listenerID:forceRefresh:queue:completionBlock:"
+ "refreshIDStatusForDestinations:service:preferredFromID:listenerID:queue:completionBlock:"
+ "refreshIDStatusForDestinations:service:preferredFromID:listenerID:queue:errorCompletionBlock:"
+ "requestIDStatusForDestination:service:preferredFromID:listenerID:queue:completionBlock:"
+ "requestIDStatusForDestinations:service:preferredFromID:listenerID:queue:completionBlock:"
+ "requiredIDStatusForDestination:service:preferredFromID:listenerID:queue:completionBlock:"
+ "requiredIDStatusForDestinations:service:preferredFromID:listenerID:queue:completionBlock:"
+ "sendInvitationUpdate - overriding fromID to %@"
+ "setForceQuery:"
+ "setKeyTransparencyURIVerificationMap:"
+ "setQuickRelayUserTypeForSession:withUserType:"
+ "v24@0:8@\"IDSCacheClearRequest\"16"
+ "v28@0:8@\"NSString\"16S24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"<IDSXPCFirewall>\"@\"NSError\">24"
+ "v64@0:8@16@24@32B40B44@48@?56"
+ "v76@0:8@16@24@32@40B48B52B56B60B64@?68"
+ "v80@0:8@16@24@32Q40@48@56@64@?72"
- "B48@0:8@16@24@32@?40"
- "B52@0:8@16@24B32@36@?44"
- "B68@0:8@16@24@32@40B48@?52@?60"
- "B76@0:8@16@24@32B40B44B48B52B56@60@?68"
- "Using client fromID for query: { fromID: %@ }"
- "_currentRemoteDevicesForDestinations:service:listenerID:queue:waitForReply:completionBlock:completionBlockWithError:"
- "_idStatusForDestinations:service:listenerID:allowRenew:respectExpiry:waitForReply:forceRefresh:bypassLimit:completionBlock:"
- "_refreshIDStatusForDestinations:service:listenerID:allowRefresh:respectExpiry:waitForReply:forceRefresh:bypassLimit:queue:completionBlock:"
- "_requestCachedStatusForDestinations:service:waitForReply:respectExpiry:listenerID:completionBlock:"
- "_requestIDInfoForDestinations:service:infoTypes:options:listenerID:queue:completionBlock:"
- "_sync_currentIDStatusForDestinations:service:respectExpiry:listenerID:completionBlock:"
- "_sync_currentRemoteDevicesForDestinations:service:listenerID:completionBlock:"
- "_sync_refreshIDStatusForDestinations:service:listenerID:completionBlock:"
- "firewallCollaboratorWithCompletion:"
- "firewallCollaboratorWithErrorHandler:"
- "refreshIDStatusForDestinations:service:listenerID:forceRefresh:queue:completionBlock:"
- "sendInvitation - overriding fromID"
- "sendInvitationUpdate - overriding fromID"
- "v24@0:8@?<v@?@\"<IDSXPCFirewall>\"@\"NSError\">16"
- "v56@0:8@16@24B32B36@40@?48"
- "v68@0:8@16@24@32B40B44B48B52B56@?60"
- "v72@0:8@16@24Q32@40@48@56@?64"

```
