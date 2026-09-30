## IMAP

> `/System/Library/PrivateFrameworks/VisualVoicemail.framework/IMAP.framework/IMAP`

```diff

-899.0.0.0.0
-  __TEXT.__text: 0xaea60
+901.0.0.0.0
+  __TEXT.__text: 0xb0f7c
   __TEXT.__auth_stubs: 0x1aa0
-  __TEXT.__objc_methlist: 0xaa0c
-  __TEXT.__const: 0x2a8
-  __TEXT.__gcc_except_tab: 0xb9dc
-  __TEXT.__cstring: 0x73b0
-  __TEXT.__oslogstring: 0x4174
+  __TEXT.__objc_methlist: 0xaa9c
+  __TEXT.__const: 0x2c8
+  __TEXT.__gcc_except_tab: 0xbd8c
+  __TEXT.__cstring: 0x73d4
+  __TEXT.__oslogstring: 0x4715
   __TEXT.__ustring: 0x14d0
-  __TEXT.__unwind_info: 0x4230
-  __TEXT.__objc_classname: 0xffd
-  __TEXT.__objc_methname: 0x15f25
-  __TEXT.__objc_methtype: 0x3072
-  __TEXT.__objc_stubs: 0x11a60
-  __DATA_CONST.__got: 0xbf0
+  __TEXT.__unwind_info: 0x4378
+  __TEXT.__objc_classname: 0xffe
+  __TEXT.__objc_methname: 0x16034
+  __TEXT.__objc_methtype: 0x30ac
+  __TEXT.__objc_stubs: 0x11c00
+  __DATA_CONST.__got: 0xbe8
   __DATA_CONST.__const: 0x2eb0
   __DATA_CONST.__objc_classlist: 0x450
   __DATA_CONST.__objc_catlist: 0x98
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5f08
+  __DATA_CONST.__objc_selrefs: 0x5f70
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x3b0
   __DATA_CONST.__objc_arraydata: 0x98
   __AUTH_CONST.__auth_got: 0xd68
   __AUTH_CONST.__const: 0xdf8
-  __AUTH_CONST.__cfstring: 0x9860
-  __AUTH_CONST.__objc_const: 0x12a48
+  __AUTH_CONST.__cfstring: 0x9980
+  __AUTH_CONST.__objc_const: 0x12af8
   __AUTH_CONST.__objc_arrayobj: 0x138
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x1540
-  __DATA.__objc_ivar: 0xac0
+  __DATA.__objc_ivar: 0xad4
   __DATA.__data: 0xae0
-  __DATA.__bss: 0x318
+  __DATA.__bss: 0x330
   __DATA_DIRTY.__objc_data: 0x15e0
   __DATA_DIRTY.__data: 0x50
-  __DATA_DIRTY.__bss: 0x1c8
+  __DATA_DIRTY.__bss: 0x1b8
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CallKit.framework/CallKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 782FE6FA-770D-3A48-A197-3189CE3195DC
-  Functions: 4074
-  Symbols:   14459
-  CStrings:  7694
+  UUID: 6BF398F5-7C48-3BDA-A22F-A7503703FC6F
+  Functions: 4109
+  Symbols:   14569
+  CStrings:  7756
 
Symbols:
+ -[MFConnection abortSocket:]
+ -[MFConnection createSocket]
+ -[MFConnection getSocket]
+ -[MFConnection hostname]
+ -[MFConnection performAtomicAccessorBlock:]
+ -[MFConnection port]
+ -[MFConnection resetSocket]
+ -[MFIMAPConnection handleStreamEvent:].cold.1
+ -[MFIMAPConnection handleStreamEvent:].cold.2
+ -[MFInvocationQueue initWithDomain:]
+ -[MFInvocationQueue initWithMambaID:mambaID:]
+ -[MFInvocationQueue initWithMaxThreadCount:domain:mambaID:]
+ -[_MFSocket disableEphemeralDiffieHellman]
+ -[_MFSocket getClosingEventHandler]
+ -[_MFSocket getConnectionServiceType]
+ -[_MFSocket getEventHandler]
+ -[_MFSocket performAtomicAccessorBlock:]
+ -[_MFSocket resetConnectionServiceType]
+ -[_MFSocket setCertificates:]
+ -[_MFSocket setSettings:]
+ -[_MFSocket usesOpportunisticSocketsStatus]
+ _OBJC_IVAR_$_MFConnection._socket
+ _OBJC_IVAR_$_MFConnection.lock
+ _OBJC_IVAR_$_MFInvocationQueue.domain
+ _OBJC_IVAR_$_MFInvocationQueue.instanceID
+ _OBJC_IVAR_$_MFInvocationQueue.logger
+ _OBJC_IVAR_$_MFInvocationQueue.mambaID
+ _OBJC_IVAR_$__MFSocket.lock
+ __ZL23_setupWriteErrorMessageP12MFConnectionP9_MFSocket
+ ___20-[_MFSocket timeout]_block_invoke
+ ___24-[_MFSocket setTimeout:]_block_invoke
+ ___25-[MFConnection getSocket]_block_invoke
+ ___27-[MFConnection resetSocket]_block_invoke
+ ___27-[_MFSocket remoteHostname]_block_invoke
+ ___28-[MFConnection createSocket]_block_invoke
+ ___28-[_MFSocket getEventHandler]_block_invoke
+ ___29-[_MFSocket remotePortNumber]_block_invoke
+ ___29-[_MFSocket setEventHandler:]_block_invoke
+ ___31-[_MFSocket serverCertificates]_block_invoke
+ ___33-[_MFSocket isCellularConnection]_block_invoke
+ ___35-[_MFSocket getClosingEventHandler]_block_invoke
+ ___36-[_MFSocket setClosingEventHandler:]_block_invoke
+ ___37-[_MFSocket getConnectionServiceType]_block_invoke
+ ___40-[MFInvocationQueue _processInvocation:]_block_invoke.54
+ ___76-[MFAttachmentComposeManager _fetchDataForAttachment:withProvider:syncLock:]_block_invoke.13
+ ___88-[MFAttachmentComposeManager _callProgressBlockForAttachmentURL:withBytes:expectedSize:]_block_invoke.27
+ ___block_descriptor_44_ea8_32s_e5_v8?0ls32l8
+ ___block_literal_global.206
+ ___block_literal_global.223
+ ___block_literal_global.539
+ ___block_literal_global.68
+ ___block_literal_global.760
+ __drainQueue:.invocationQueueDebug
+ _execute_networkthread_block_sync
+ _g_object_instance_id
+ _g_thread_instance_id
+ _objc_msgSend$abortSocket:
+ _objc_msgSend$createSocket
+ _objc_msgSend$disableEphemeralDiffieHellman
+ _objc_msgSend$getClosingEventHandler
+ _objc_msgSend$getConnectionServiceType
+ _objc_msgSend$getEventHandler
+ _objc_msgSend$getSocket
+ _objc_msgSend$initWithDomain:
+ _objc_msgSend$initWithMambaID:mambaID:
+ _objc_msgSend$initWithMaxThreadCount:domain:mambaID:
+ _objc_msgSend$performAtomicAccessorBlock:
+ _objc_msgSend$port
+ _objc_msgSend$resetConnectionServiceType
+ _objc_msgSend$resetSocket
+ _objc_msgSend$setCertificates:
+ _objc_msgSend$setSettings:
+ _objc_msgSend$usesOpportunisticSocketsStatus
+ _os_unfair_lock_lock_with_options
- -[MFConnection _setupSocketWithSettings:]
- -[MFInvocationQueue initWithMaxThreadCount:]
- -[MFInvocationQueue init]
- -[MFMonitoredInvocation mf_shouldLogInvocation]
- -[MFMonitoredInvocation setShouldLogInvocation:]
- -[NSInvocation(MailExtensions) mf_shouldLogInvocation]
- OBJC_IVAR_$_MFConnection._socket
- OBJC_IVAR_$_MFMonitoredInvocation._shouldLogInvocation
- __OBJC_$_CATEGORY_INSTANCE_METHODS_NSInvocation_$_MailExtensions
- ___40-[MFInvocationQueue _processInvocation:]_block_invoke.44
- ___76-[MFAttachmentComposeManager _fetchDataForAttachment:withProvider:syncLock:]_block_invoke.11
- ___88-[MFAttachmentComposeManager _callProgressBlockForAttachmentURL:withBytes:expectedSize:]_block_invoke.25
- ___block_descriptor_48_ea8_32s_e5_v8?0ls32l8
- ___block_literal_global.181
- ___block_literal_global.222
- ___block_literal_global.538
- ___block_literal_global.67
- ___block_literal_global.755
- ___stderrp
- __drainQueue:.DebugInvocationThreads
- __drainQueue:.c
- _fprintf
- _objc_msgSend$_setupSocketWithSettings:
- _objc_msgSend$inAirplaneMode
- _objc_msgSend$initWithMaxThreadCount:
- _objc_msgSend$mf_shouldLogInvocation
CStrings:
+ "#D %s%s%{public}@%shandleStreamEvent kCFStreamEventEndEncountered"
+ "#D %s%s%{public}@%shandleStreamEvent kCFStreamEventHasBytesAvailable"
+ "#E %s%s%{public}@%s*** _NSSocket.m:%d (%s) failed; error=(%@, %ld)"
+ "#I %@ socket (%p) connectToHost %@"
+ "#I %@ socket (%p) disconnectAndNotifyDelegate [%s]"
+ "#I %s %@ socket (%p) abort"
+ "#I %s %@ socket (%p) aborting"
+ "#I %s %@ socket (%p) disconnect"
+ "#I %s %@ socket (%p) setClosingEventHandler"
+ "#I %s %@ socket (%p) setClosingEventHandler, recreated"
+ "#I %s%s%{public}@%s<%@ %p> Connection created"
+ "#I %s%s%{public}@%s<%@ %p> Connection deleted"
+ "#I %s%s%{public}@%s<%@, %p> Connection deleting"
+ "#I %s%s%{public}@%sabortSocket: aborting deleted socket"
+ "#I %s%s%{public}@%sabortSocket: aborting invalid socket (%p), self socket (%p)"
+ "#I %s%s%{public}@%scan't change throughput monitoring, socket closed"
+ "#I %s%s%{public}@%scan't change throughput monitoring, stream closed"
+ "#I %s%s%{public}@%sconnectUsingAccount %@ %@"
+ "#I %s%s%{public}@%sdisconnectAndNotifyDelegate, repeated [%s] (socket already closed)"
+ "#I %s%s%{public}@%sisCellularConnection = %@"
+ "#I %s%s%{public}@%ssocket (%p) aborted, stream closed"
+ "#I %s%s%{public}@%ssocket (%p) deleted"
+ "#I %s%s%{public}@%ssocket (%p) setSettings:%@"
+ "#I %s%s%{public}@%ssocket (%p) unexpected abort, stream already closed"
+ "#I %s%s%{public}@%sstream deleting"
+ "#I %s%s%{public}@%sstream is going to be closed from read half, unprocessed data: len %zu [%s]"
+ "#I %{public}@%s%@ --> MFInvocationQueue finished invocation ['%s' %@] in %5.5fs\n"
+ "#I %{public}@%s%@ <%@ %p> finished, num threads %lu"
+ "#I %{public}@%s%@ <%@ %p> started [%@]"
+ "#I %{public}@%s%@ ==> MFInvocationQueue starting invocation ['%s' %@]"
+ "#I %{public}@%s<%@ %p> Created"
+ "#I %{public}@%s<%@ %p> Deleted"
+ "#I %{public}@%sAdding invocation ['%s' %@]"
+ "#I %{public}@%sCreating invocation thread for priority %lu, num threads %lu"
+ "#I %{public}@%sCreating invocation thread, num threads %lu"
+ "%@ socket: %p\n"
+ "%s inv.%lu"
+ "(read) socket deleted"
+ "(write) socket deleted"
+ "*** _NSSocket.m:%d (%s) failed; error=(%@, %ld)"
+ "@\"NSObject<OS_os_log>\""
+ "@32@0:8r*16r*24"
+ "@40@0:8Q16r*24r*32"
+ "InvocationQueueDebug"
+ "T@\"_MFSocket\",R,N,GgetSocket,V_socket"
+ "Ti,R,N,V_timeout"
+ "abortSocket:"
+ "com.apple.voicemail.invThread.%s-inv.%lu-th.%lu"
+ "com.apple.voicemail.networkThread"
+ "createSocket"
+ "disableEphemeralDiffieHellman"
+ "failed"
+ "getClosingEventHandler"
+ "getConnectionServiceType"
+ "getEventHandler"
+ "getSocket"
+ "initWithDomain:"
+ "initWithMambaID:mambaID:"
+ "initWithMaxThreadCount:domain:mambaID:"
+ "instanceID"
+ "inv.%lu"
+ "invc.comp"
+ "invc.con"
+ "invc.del"
+ "invc.dmn"
+ "invc.lib"
+ "invc.load"
+ "performAtomicAccessorBlock:"
+ "proc.open"
+ "resetConnectionServiceType"
+ "resetSocket"
+ "setCertificates:"
+ "setSettings:"
+ "socket"
+ "succeeded"
+ "th.%lu"
+ "usesOpportunisticSocketsStatus"
+ "write"
- "#E %s%s%{public}@%s*** _NSSocket.m:%s failed; error=(%@,%ld)"
- "#I %s%s%{public}@%s%d for %@"
- "#I %s%s%{public}@%sConnection created"
- "#I %s%s%{public}@%sConnection destroyed"
- "#I %s%s%{public}@%sdestroying connection"
- "#I %s%s%{public}@%sdisconnectAndNotifyDelegate [%s]%s"
- "#I %s%s%{public}@%ssocket aborted, stream closed"
- "#I %s%s%{public}@%ssocket destroyed"
- "#I %s%s%{public}@%sstream is going to be closed from read half, Unprocessed data: %s"
- "%@ _socket: %p\n"
- "*** _NSSocket.m:%s failed; error=(%@,%ld)"
- ", Throw away our socket"
- ", socket is/was closed"
- "-[MFConnection _setupSocketWithSettings:]"
- "DebugWorkerThreads"
- "MFInvocationQueue finished invocation %p [%s %s] in %5.5fs\n"
- "MFInvocationQueue starting invocation %p [%s %s]\n"
- "T@\"NSArray\",R"
- "Ti,V_timeout"
- "_setupSocketWithSettings:"
- "_shouldLogInvocation"
- "deallocating %p %@"
- "initWithMaxThreadCount:"
- "mf_shouldLogInvocation"
- "setShouldLogInvocation:"

```
