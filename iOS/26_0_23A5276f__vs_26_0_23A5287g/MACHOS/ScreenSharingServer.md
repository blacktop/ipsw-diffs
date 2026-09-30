## ScreenSharingServer

> `/System/Library/CoreServices/ScreenSharingServer.app/ScreenSharingServer`

```diff

-113.0.0.0.0
-  __TEXT.__text: 0x40174
+114.0.0.0.0
+  __TEXT.__text: 0x41ad8
   __TEXT.__auth_stubs: 0xe50
-  __TEXT.__objc_stubs: 0x43e0
-  __TEXT.__objc_methlist: 0x1c74
+  __TEXT.__objc_stubs: 0x4400
+  __TEXT.__objc_methlist: 0x1c7c
   __TEXT.__const: 0xe2
-  __TEXT.__objc_methname: 0x5c76
-  __TEXT.__cstring: 0xaf9e
-  __TEXT.__oslogstring: 0x6e44
+  __TEXT.__objc_methname: 0x5c80
+  __TEXT.__cstring: 0xb00e
+  __TEXT.__oslogstring: 0x7407
   __TEXT.__objc_classname: 0x2c8
   __TEXT.__objc_methtype: 0x3084
   __TEXT.__gcc_except_tab: 0x3e0
-  __TEXT.__unwind_info: 0x548
+  __TEXT.__unwind_info: 0x550
   __DATA_CONST.__auth_got: 0x738
   __DATA_CONST.__got: 0x3d8
   __DATA_CONST.__const: 0x660
-  __DATA_CONST.__cfstring: 0x1ce0
+  __DATA_CONST.__cfstring: 0x1d60
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x70

   __DATA_CONST.__objc_intobj: 0x60
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA.__objc_const: 0x25d0
-  __DATA.__objc_selrefs: 0x1600
+  __DATA.__objc_selrefs: 0x1608
   __DATA.__objc_ivar: 0x1f0
   __DATA.__objc_data: 0x410
   __DATA.__data: 0x590

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 0DFE23ED-B442-343C-9C82-E99C0BC0BBDF
+  UUID: 745FFB42-0315-3267-A861-112F777393CE
   Functions: 605
   Symbols:   369
-  CStrings:  3489
+  CStrings:  3528
 
CStrings:
+ "PinningDisabled: %d"
+ "URLSession:task:didCompleteWithError: %s"
+ "[%s:%d] Ignoring invitation -- pendingSession already active from: %s %s"
+ "[%s:%d] Ignoring invitation.  Session already established with fromID %s."
+ "[%s:%d] NWDatagramConnection error: %s"
+ "[%s:%d] Not a valid request: %s"
+ "[%s:%d] PinningDisabled: %d"
+ "[%s:%d] SESSION END receivedSessionEndFromID %s data: %s for session %s"
+ "[%s:%d] SESSION END sessionEnded:session %s withReason:%d error:%s"
+ "[%s:%d] SendPacketToAllReceivers  error %d %s"
+ "[%s:%d] SendPacketToAllReceivers - unable to set outgoing interface %x err %d %s"
+ "[%s:%d] SendPacketToAllReceivers multicast error %d %d %s"
+ "[%s:%d] SendStatusBack errno %d %s r->readSockFD = %d"
+ "[%s:%d] UDPWriteNetworkPacket result looks wrong %d %s"
+ "[%s:%d] URLSession:task:didCompleteWithError: %s"
+ "[%s:%d] allowNonProductionServers: %d"
+ "[%s:%d] args = %s"
+ "[%s:%d] connection state for %p is %s"
+ "[%s:%d] destination string %s"
+ "[%s:%d] doDeclineIDSInvitationWithReasonString: %s for %s"
+ "[%s:%d] error closing socket %s"
+ "[%s:%d] error: %s"
+ "[%s:%d] hostIdentifier: %s"
+ "[%s:%d] inviteOptions: %s"
+ "[%s:%d] inviteReceivedForSession from %s"
+ "[%s:%d] no HID event client"
+ "[%s:%d] no longer monitoring touch events"
+ "[%s:%d] receivedInvitationAcceptFromID fromID:%s"
+ "[%s:%d] receivedInvitationAcceptFromID fromID:%s data:%s"
+ "[%s:%d] receivedInvitationCancelFromID fromID:%s"
+ "[%s:%d] receivedInvitationCancelFromID fromID:%s data:%s"
+ "[%s:%d] receivedInvitationDeclineFromID fromID:%s"
+ "[%s:%d] receivedInvitationDeclineFromID fromID:%s data:%s"
+ "[%s:%d] receivedSessionMessageFromID fromID:%s data:%s"
+ "[%s:%d] sendMessage error: %s"
+ "[%s:%d] serverDiedForConference delegate called.  Server will exit."
+ "[%s:%d] sessionStarted bad session: session=%s, socket=%d"
+ "[%s:%d] shouldStartScreenSharingSession called for %s"
+ "[%s:%d] system information error: %s"
+ "[%s:%d] trustResult: %d"
+ "[%s:%d] woke up from semaphore"
+ "[%s:%d] xpc_set_event_stream_handler: xpcEvent: %s"
+ "allowNonProductionServers: %d"
+ "args = %s"
+ "inviteOptions: %s"
+ "isAppleTV"
+ "kSSSelectAcceptAppleSupportAppleTV"
+ "kSSSelectAcceptAppleTV"
+ "kSSSelectAcceptShareSettingsAppleSupportAppleTV"
+ "kSSSelectAcceptShareSettingsAppleTV"
+ "no HID event client"
+ "no longer monitoring touch events"
+ "serverDiedForConference delegate called.  Server will exit."
+ "shouldStartScreenSharingSession called for %s"
+ "trustResult: %d"
+ "woke up from semaphore"
+ "xpc_set_event_stream_handler: xpcEvent: %s"
- "***error: %s"
- "***serverDiedForConference delegate called.  fatal error server will exit"
- "@@shouldstartscreensharingsession called for %s"
- "PinningDisabled:%d"
- "URLSession:task:didCompleteWithError:%s"
- "[%s:%d] ***serverDiedForConference delegate called.  fatal error server will exit"
- "[%s:%d] @@shouldstartscreensharingsession called for %s"
- "[%s:%d] PinningDisabled:%d"
- "[%s:%d] allowNonProductionServers:%d"
- "[%s:%d] no hid event client"
- "[%s:%d] no lopnger monitoring touch events"
- "[%s:%d] trustResult:%d"
- "[%s:%d] woke up from sempahore"
- "[%s:%d] xpc_set_event_stream_handler: xpcEvent:%s"
- "ags = %s"
- "allowNonProductionServers:%d"
- "inviteOptions:%s"
- "no hid event client"
- "no lopnger monitoring touch events"
- "trustResult:%d"
- "woke up from sempahore"
- "xpc_set_event_stream_handler: xpcEvent:%s"

```
