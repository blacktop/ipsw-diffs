## APTransport

> `/System/Library/PrivateFrameworks/APTransport.framework/APTransport`

```diff

-800.68.1.0.0
-  __TEXT.__text: 0x8ba98
-  __TEXT.__auth_stubs: 0x2f80
+830.2.0.0.0
+  __TEXT.__text: 0x8e33c
+  __TEXT.__auth_stubs: 0x2f90
   __TEXT.__objc_methlist: 0x93c
-  __TEXT.__cstring: 0x27a4e
+  __TEXT.__cstring: 0x280de
   __TEXT.__const: 0x248
   __TEXT.__gcc_except_tab: 0x394
   __TEXT.__oslogstring: 0x16e
-  __TEXT.__unwind_info: 0x1588
+  __TEXT.__unwind_info: 0x1600
   __TEXT.__objc_classname: 0x111
   __TEXT.__objc_methname: 0x3135
   __TEXT.__objc_methtype: 0xb27
   __TEXT.__objc_stubs: 0x31a0
   __DATA_CONST.__got: 0x398
-  __DATA_CONST.__const: 0x2f20
+  __DATA_CONST.__const: 0x3378
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xd20
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x17d0
-  __AUTH_CONST.__const: 0x2948
+  __AUTH_CONST.__auth_got: 0x17d8
+  __AUTH_CONST.__const: 0x29f8
   __AUTH_CONST.__cfstring: 0x5680
   __AUTH_CONST.__objc_const: 0x1790
   __AUTH_CONST.__objc_arrayobj: 0x18

   __AUTH.__data: 0xb8
   __DATA.__objc_ivar: 0x118
   __DATA.__data: 0xf30
-  __DATA.__bss: 0x194
+  __DATA.__bss: 0x17c
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__data: 0xa18
-  __DATA_DIRTY.__bss: 0x1a8
+  __DATA_DIRTY.__bss: 0x1c0
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /usr/lib/libIOReport.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1809
-  Symbols:   2995
-  CStrings:  4508
+  Functions: 1842
+  Symbols:   3029
+  CStrings:  4539
 
Symbols:
+ _APTTrafficMetricsMessageProcessed
+ _APTTrafficMetricsMessageReadFinished
+ _APTTrafficMetricsMessageReadStarted
+ _dispatch_get_global_queue
- _APTTrafficMetricsDataReceiveAboutToProcess
- _APTTrafficMetricsDataReceiveAboutToRead
- _APTTrafficMetricsDataReceiveFinished
- _APTTrafficMetricsDataReceiveFinishedProcess
- _APTTrafficMetricsDataReceiveFinishedRead
- _APTTrafficMetricsDataReceiveStarted
CStrings:
+ "830.2"
+ "APTransportConnectionHTTP.event.%!{(MISSING)ptr}"
+ "APTransportStream.%!{(MISSING)ptr}.notification"
+ "APTransportStreamUnbuffered.%!{(MISSING)ptr}.data"
+ "APTransportStreamUnbuffered.%!{(MISSING)ptr}.notification"
+ "Failed to allocate server state mutex"
+ "OSStatus httpconnection_SendPackage(APTransportConnectionRef, APTransportPackageRef)"
+ "OSStatus stream_enableReverseControlInternal(FigTransportStreamRef)"
+ "OSStatus stream_resumeInternal(FigTransportStreamRef)"
+ "OSStatus stream_waitUntilConnectionSetup(FigTransportStreamRef, APTransportStreamConnectionType)_block_invoke"
+ "OSStatus stream_waitUntilConnectionSetup(FigTransportStreamRef, APTransportStreamConnectionType)_block_invoke_2"
+ "[%!{(MISSING)ptr}] %!s(MISSING): Incoming http connection connected \n"
+ "[%!{(MISSING)ptr}] Connection %!s(MISSING)%!?(MISSING)#m."
+ "[%!{(MISSING)ptr}] Connection %!s(MISSING)."
+ "[%!{(MISSING)ptr}] Connection resumed.\n"
+ "[%!{(MISSING)ptr}] Connection statistics: I:%!z(MISSING)u/%!z(MISSING)u/%!l(MISSING)lu/%!l(MISSING)lu/%!l(MISSING)lu/%!l(MISSING)lu %!s(MISSING) T:%!z(MISSING)u/%!z(MISSING)u/%!l(MISSING)lu/%!l(MISSING)lu/%!l(MISSING)lu/%!l(MISSING)lu\n"
+ "[%!{(MISSING)ptr}] Dispatching event %!'(MISSING)s to %!l(MISSING)d clients"
+ "[%!{(MISSING)ptr}] Event message reply %!s(MISSING) to %!a(MISSING), HTTP Status: %!d(MISSING), Body %!z(MISSING)u bytes, ID 0x%!X(MISSING)%!?(MISSING){end} error: %!m(MISSING)"
+ "[%!{(MISSING)ptr}] Ignoring late response for event 0x%!X(MISSING)"
+ "[%!{(MISSING)ptr}] Message processed.\n"
+ "[%!{(MISSING)ptr}] Message read finished.\n"
+ "[%!{(MISSING)ptr}] Message read started.\n"
+ "[%!{(MISSING)ptr}] Received event %!s(MISSING) from connection [%!{(MISSING)ptr}] %!?(MISSING){end}with data %!{(MISSING)ptr}\n"
+ "[%!{(MISSING)ptr}] Shifted read finished by %!l(MISSING)lums\n"
+ "[%!{(MISSING)ptr}] Waiting for connection [%!{(MISSING)ptr}]."
+ "[%!{(MISSING)ptr}] connection failed\n"
+ "event queue allocation failed"
+ "failed to send"
+ "invalidated or failed with err="
+ "sent"
+ "stream_SetReadyToSendBatchCallback_block_invoke"
+ "stream_SetReadyToSendCallback_block_invoke"
+ "stream_SignalDataAvailable_block_invoke"
+ "stream_configureEncryptionInternal"
+ "stream_enableReverseControlInternal"
+ "stream_handleEventFromConnection_block_invoke"
+ "stream_handleEventFromSendConnection_block_invoke"
+ "stream_postCachedConnectionEvent"
+ "stream_readyToSendBatchCallback_block_invoke"
+ "stream_readyToSendCallback_block_invoke"
+ "stream_resumeInternal"
+ "stream_waitUntilConnectedInternal"
+ "stream_waitUntilConnectedInternal_block_invoke"
+ "stream_waitUntilConnectionSetup_block_invoke"
+ "stream_waitUntilConnectionSetup_block_invoke_2"
+ "succeeded"
+ "void aptTrafficMetrics_receiverIntervalTimerHandler(APTTrafficMetricsRef)"
+ "void aptTrafficMetrics_senderIntervalTimerHandler(APTTrafficMetricsRef)"
+ "void stream_sendReplyMessage(FigTransportStreamRef, uint64_t, uint32_t, OSStatus, CMBlockBufferRef)"
+ "void tcpconnection_handleListenerConnected(APTConnectionListenerRef, void *, SocketRef, APSNetworkAddressRef)"
- "%!s(MISSING), connection failed\n"
- "800.68.1"
- "APTransportStream.notification.%!@(MISSING)"
- "APTransportStreamEnableReverseControl"
- "APTransportStreamUnbuffered.notification.%!@(MISSING)"
- "OSStatus APTransportStreamEnableReverseControl(FigTransportStreamRef)"
- "OSStatus stream_Resume(FigTransportStreamRef)"
- "[%!{(MISSING)ptr}] Event message reply sent to %!a(MISSING), HTTP Status: %!d(MISSING), Body %!z(MISSING)u bytes, ID 0x%!X(MISSING)\n"
- "[%!{(MISSING)ptr}] Notifying %!l(MISSING)d clients of event %!'(MISSING)s"
- "stream_AcquireMessageBBuf"
- "stream_Resume"
- "stream_SendMessage"
- "stream_SetProperty"
- "stream_SignalDataAvailable"
- "stream_WaitUntilConnected"
- "stream_WaitUntilConnectedEx"
- "stream_waitUntilConnectionSetup"
- "void aptTrafficMetrics_intervalTimerHandler(void *)"
- "void stream_sendReplyMessage(FigTransportStreamRef, uint64_t, OSStatus, CMBlockBufferRef)"

```
