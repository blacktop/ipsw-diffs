## IMCore

> `/System/Library/PrivateFrameworks/IMCore.framework/IMCore`

```diff

-1402.200.111.2.17
-  __TEXT.__text: 0x1bd99c
-  __TEXT.__auth_stubs: 0x2700
+1402.300.129.2.15
+  __TEXT.__text: 0x1bf100
+  __TEXT.__auth_stubs: 0x2710
   __TEXT.__delay_stubs: 0x58
   __TEXT.__delay_helper: 0xec
-  __TEXT.__objc_methlist: 0x13238
+  __TEXT.__objc_methlist: 0x13378
   __TEXT.__const: 0x16b0
-  __TEXT.__gcc_except_tab: 0x15e88
-  __TEXT.__cstring: 0x105d7
-  __TEXT.__oslogstring: 0x1e089
+  __TEXT.__gcc_except_tab: 0x1602c
+  __TEXT.__cstring: 0x10697
+  __TEXT.__oslogstring: 0x1e219
   __TEXT.__ustring: 0xc0
   __TEXT.__dlopen_cstrs: 0x184
   __TEXT.__constg_swiftt: 0x550

   __TEXT.__swift5_proto: 0x128
   __TEXT.__swift5_types: 0x6c
   __TEXT.__swift5_capture: 0x4ac
-  __TEXT.__unwind_info: 0x7d18
+  __TEXT.__unwind_info: 0x7dd0
   __TEXT.__eh_frame: 0x8c8
-  __TEXT.__objc_classname: 0x24dc
-  __TEXT.__objc_methname: 0x3ca8f
-  __TEXT.__objc_methtype: 0x6482
-  __TEXT.__objc_stubs: 0x24440
-  __DATA_CONST.__got: 0x1ec0
-  __DATA_CONST.__const: 0x5048
-  __DATA_CONST.__objc_classlist: 0x720
+  __TEXT.__objc_classname: 0x251f
+  __TEXT.__objc_methname: 0x3cdad
+  __TEXT.__objc_methtype: 0x6495
+  __TEXT.__objc_stubs: 0x24720
+  __DATA_CONST.__got: 0x1ed8
+  __DATA_CONST.__const: 0x5098
+  __DATA_CONST.__objc_classlist: 0x728
   __DATA_CONST.__objc_catlist: 0xc0
-  __DATA_CONST.__objc_protolist: 0x418
+  __DATA_CONST.__objc_protolist: 0x428
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc818
-  __DATA_CONST.__objc_protorefs: 0x190
-  __DATA_CONST.__objc_superrefs: 0x558
+  __DATA_CONST.__objc_selrefs: 0xc8c0
+  __DATA_CONST.__objc_protorefs: 0x198
+  __DATA_CONST.__objc_superrefs: 0x560
   __DATA_CONST.__objc_arraydata: 0xa8
-  __AUTH_CONST.__auth_got: 0x13a0
+  __AUTH_CONST.__auth_got: 0x13a8
   __AUTH_CONST.__auth_ptr: 0x318
-  __AUTH_CONST.__const: 0x41c8
-  __AUTH_CONST.__cfstring: 0xbca0
-  __AUTH_CONST.__objc_const: 0x20e60
+  __AUTH_CONST.__const: 0x41e8
+  __AUTH_CONST.__cfstring: 0xbd00
+  __AUTH_CONST.__objc_const: 0x210c0
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0x28f0
+  __AUTH.__objc_data: 0x2940
   __AUTH.__data: 0x100
-  __DATA.__objc_ivar: 0x1118
-  __DATA.__data: 0x28c0
-  __DATA.__bss: 0x2d48
+  __DATA.__objc_ivar: 0x112c
+  __DATA.__data: 0x2920
+  __DATA.__bss: 0x2d58
   __DATA.__common: 0x50
   __DATA_DIRTY.__objc_data: 0x2348
   __DATA_DIRTY.__data: 0x3c8

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 8854
-  Symbols:   2342
-  CStrings:  14299
+  Functions: 8889
+  Symbols:   2348
+  CStrings:  14348
 
Symbols:
+ _IMDaemonBackgroundMessagingProtocolXPCInterface
+ _IMSPIReceiveMSMessagePayloadWithCallback
+ _IMSetupInfoApprovedClientCapabilitiesKey
+ _OBJC_CLASS_$_IMBackgroundMessagingAPIConnection
+ _OBJC_CLASS_$_NSISO8601DateFormatter
+ _OBJC_METACLASS_$_IMBackgroundMessagingAPIConnection
CStrings:
+ "\x1a"
+ " => Updating existing composing message to recording message: %!@(MISSING)"
+ "&\x15"
+ "@\"NSXPCConnection\""
+ "BackgroundMessagingAPI"
+ "Connection Interrupted"
+ "Connection Invalidated"
+ "Connection error"
+ "Finished remote intent download for guid: %!@(MISSING). Posting IMFileTransferUpdatedNotification."
+ "IMBackgroundMessagingAPIConnection"
+ "IMBackgroundMessagingAPIConnectionQueue"
+ "IMDaemonRemoteIntentProtocol"
+ "Ignoring finished remote intent download notification for transfer guid: %!@(MISSING)"
+ "LastMessage"
+ "Requested to report RCS spam for a non-RCS message!"
+ "T@\"NSDate\",&,N,V_date"
+ "T@\"NSString\",&,N,V_effectID"
+ "TQ,N,V_processCapabilities"
+ "_backgroundMessagingAPIServiceWithErrorHandler:"
+ "_calculateTimestamp"
+ "_clearConnection"
+ "_currentConnection"
+ "_dateFormatter"
+ "_effectID"
+ "_handleFileTransferFinishedRemoteIntentDownload:"
+ "_lastIncomingFinishedMessageItemWithTextContent"
+ "_messageToReportJunk"
+ "_processCapabilities"
+ "_setQueue:"
+ "chatDictionariesForChat: did not find chatDictionary for guid; %!@(MISSING)"
+ "checkAuthorizationStatusForRecipients"
+ "checkAuthorizationStatusForRecipients:completion:"
+ "com.apple.messages.critical-messaging"
+ "critical-messaging-app-name"
+ "criticalMessagingAppName"
+ "dateFromString:"
+ "effectID"
+ "fileTransferFinishedRemoteIntentDownload:"
+ "isLastMessageTypingIndicator"
+ "lastIncomingFinishedMessageItem"
+ "requestBackgroundMessagingAuthorizationForRecipients"
+ "requestBackgroundMessagingAuthorizationForRecipients:completion:"
+ "requestContactsForIdentifiers:reply:"
+ "requestedCapabilities"
+ "requiresCriticalMessagingAPIAttribution"
+ "sendBackgroundMessage"
+ "sendBackgroundMessage:toRecipient:completion:"
+ "serviceForChatItems:"
+ "setEffectID:"
+ "setProcessCapabilities:"
+ "simulateAppDeletion"
+ "simulateAppInstallation"
- " => Updating existing composeing message to recording message: %!@(MISSING)"
- "Auto collecting logs because:(%!@(MISSING)), sending to %!@(MISSING)"
- "_lastIncomingFinishedMessage"
- "_lastIncomingFinishedMessageWithTextContent"

```
