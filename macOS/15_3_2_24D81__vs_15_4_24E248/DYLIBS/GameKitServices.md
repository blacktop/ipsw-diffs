## GameKitServices

> `/System/Library/PrivateFrameworks/GameKitServices.framework/Versions/A/GameKitServices`

```diff

-2100.5.1.0.0
-  __TEXT.__text: 0x7dedc
-  __TEXT.__auth_stubs: 0x11f0
-  __TEXT.__objc_methlist: 0x2a20
-  __TEXT.__const: 0x1988
-  __TEXT.__gcc_except_tab: 0x930
-  __TEXT.__cstring: 0x68bc
-  __TEXT.__oslogstring: 0x117c0
-  __TEXT.__unwind_info: 0xf98
+2105.10.1.0.0
+  __TEXT.__text: 0x7d848
+  __TEXT.__auth_stubs: 0x11e0
+  __TEXT.__objc_methlist: 0x2ea8
+  __TEXT.__const: 0x1980
+  __TEXT.__gcc_except_tab: 0x934
+  __TEXT.__cstring: 0x68b9
+  __TEXT.__oslogstring: 0x11774
+  __TEXT.__unwind_info: 0xfd0
   __TEXT.__objc_classname: 0x459
   __TEXT.__objc_methname: 0x6cb9
   __TEXT.__objc_methtype: 0x19a5

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1a48
+  __DATA_CONST.__objc_selrefs: 0x1ba0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x108
   __DATA_CONST.__objc_arraydata: 0xb8
-  __AUTH_CONST.__auth_got: 0x910
+  __AUTH_CONST.__auth_got: 0x908
   __AUTH_CONST.__const: 0xb60
   __AUTH_CONST.__cfstring: 0x1f80
-  __AUTH_CONST.__objc_const: 0x5558
+  __AUTH_CONST.__objc_const: 0x4d30
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0x60

   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: C53A462A-AF46-354F-8698-EDBB401C9E0B
-  Functions: 1579
-  Symbols:   3527
-  CStrings:  3712
+  UUID: 34DD0EEE-AC64-352D-AFC6-284E07D17A0A
+  Functions: 1602
+  Symbols:   3553
+  CStrings:  3710
 
Symbols:
+ +[GKConnection isRelayEnabled].cold.1
+ -[CDXClient initWithOptions:delegate:].cold.1
+ -[CDXClient initWithOptions:delegate:].cold.2
+ -[CDXClient startListeningOnSockets].cold.1
+ -[CDXClient start].cold.1
+ -[CDXClient start].cold.2
+ -[CDXClient start].cold.3
+ -[GKConnectionInternal extractBlobUsingData:withSourcePID:destPID:].cold.1
+ -[GKConnectionInternal internalUpdateRelayWithParticipant:withConnectionData:withRelayInfo:didInitiate:].cold.1
+ -[GKConnectionInternal internalUpdateRelayWithParticipant:withConnectionData:withRelayInfo:didInitiate:].cold.2
+ -[GKSessionInternal(callback) sendCallbacksToDelegate:remotePeer:].cold.1
+ -[GKSessionInternal(callback) sendCallbacksToDelegate:remotePeer:].cold.2
+ -[GKSessionInternal(callback) sendCallbacksToDelegate:remotePeer:].cold.3
+ -[GKSessionInternal(callback) sendCallbacksToDelegate:remotePeer:].cold.4
+ GCC_except_table124
+ SendUDPPacketCList.cold.1
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ __MergedGlobals
+ gckSessionRecvProc.cold.4
+ machTimeScale.cold.1
- -[CDXClientSession sendData:toParticipants:].cold.1
- -[CDXClientSession sendData:toParticipants:].cold.2
- -[CDXClientSession sendRaw:toParticipants:].cold.1
- -[CDXClientSession sendRaw:toParticipants:].cold.2
- -[GKConnectionInternal CDXClientSession:receivedData:from:].cold.1
- -[GKConnectionInternal connectPendingConnectionsFromList:sessionInfo:].cold.1
- -[GKConnectionInternal createInsecureTicketUsingSortedConnectionsFromList:].cold.1
- SendUDPPacketCList.g_dLastReport
- SendUDPPacketCList.g_nPktBytes
- SendUDPPacketCList.g_nPktBytes_LastReport
- SendUDPPacketCList.g_nPktCount
- SendUDPPacketCList.g_nPktCount_LastReport
- _strncmp
- machTimeScale.did_init
- machTimeScale.timeScale
CStrings:
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/BWE/BWE_GCK.c:%d: GCK_BWE_CreateHandle failed"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/BWE/BWE_GCK.c:%d: calloc(%d) failed"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: Couldn't find pCList for [%08X]"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: Maximum # of nodes reached.  Ignoring node [%08X]\n"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: No more node allowed"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: No network interface found."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: SendUDPPacketCList failed(%X)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: StartEventCallbackThread failed(%X)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: Wrong Connection Data. Participant ID from remote connection data = %08X, local participant ID = %08X\n"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: bind failed(%X) for all ports in range"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: calloc(%d) failed"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: calloc(%d) failed(%X)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: cannot add any more nodes"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: gckSessionCreate failed(%X)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: gckSessionSendHello failed(%X)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: gckSessionWaitForHello failed(%X)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: getaddrinfo failed(%X)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: getaddrinfo returned NULL"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: getsockname failed(%X)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: iRemoteConnectionDataSize wrong(%d)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: pthread_create failed(%X)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: pthread_mutexattr_init failed(%X)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: recv failed(%d)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: recv(%d) failed(%X)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: recv(%d) returned 0: Shutting down connection"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: recvmsg(%d) failed(%X)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: recvmsg(%d) returned 0: empty message"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: remoteID is invalid"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: select failed(%X)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: socket failed(%X)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GKSession_Internal.m:%d: Local side accepted but PID (0x%08X) disconnected. event->eventType = %d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GKSession_Internal.m:%d: PID 0x%08X timed out, but not known to us."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GKSession_Internal.m:%d: Received unknown event->status %08x (%d) for an unknown PID (0x%08X)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/OSPF.c:%d: malloc failed"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/CDX/CDXClient.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/CDX/cdxticketgen.c:%d: Assert Failed (%s)\n"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GKNATTraversal.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GKSession_Internal.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GKVoiceChatServicePrivate.m"
+ "23:03:42"
+ "Mar  7 2025"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/BWE/BWE_GCK.c:%d: GCK_BWE_CreateHandle failed"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/BWE/BWE_GCK.c:%d: calloc(%d) failed"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: Couldn't find pCList for [%08X]"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: Maximum # of nodes reached.  Ignoring node [%08X]\n"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: No more node allowed"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: No network interface found."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: SendUDPPacketCList failed(%X)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: StartEventCallbackThread failed(%X)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: Wrong Connection Data. Participant ID from remote connection data = %08X, local participant ID = %08X\n"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: bind failed(%X) for all ports in range"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: calloc(%d) failed"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: calloc(%d) failed(%X)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: cannot add any more nodes"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: gckSessionCreate failed(%X)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: gckSessionSendHello failed(%X)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: gckSessionWaitForHello failed(%X)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: getaddrinfo failed(%X)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: getaddrinfo returned NULL"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: getsockname failed(%X)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: iRemoteConnectionDataSize wrong(%d)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: pthread_create failed(%X)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: pthread_mutexattr_init failed(%X)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: recv failed(%d)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: recv(%d) failed(%X)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: recv(%d) returned 0: Shutting down connection"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: recvmsg(%d) failed(%X)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: recvmsg(%d) returned 0: empty message"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: remoteID is invalid"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: select failed(%X)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GCKSession.c:%d: socket failed(%X)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GKSession_Internal.m:%d: Local side accepted but PID (0x%08X) disconnected. event->eventType = %d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GKSession_Internal.m:%d: PID 0x%08X timed out, but not known to us."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GKSession_Internal.m:%d: Received unknown event->status %08x (%d) for an unknown PID (0x%08X)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/OSPF.c:%d: malloc failed"
- " [%s] %s:%d GCKSessionReceiveDOOB: received unknown message of obType == %d"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/CDX/CDXClient.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/CDX/cdxticketgen.c:%d: Assert Failed (%s)\n"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GKNATTraversal.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GKSession_Internal.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/GameKitServices.subproj/Sources/Gecko/GKVoiceChatServicePrivate.m"
- "22:50:57"
- "Dec 19 2024"
- "en"

```
