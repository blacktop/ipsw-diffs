## MediaRemote

> `/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote`

```diff

-4025.210.2.0.0
-  __TEXT.__text: 0x2f2a2c
+4025.300.6.0.0
+  __TEXT.__text: 0x2f3984
   __TEXT.__auth_stubs: 0x16f0
-  __TEXT.__objc_methlist: 0x2afa0
+  __TEXT.__objc_methlist: 0x2b080
   __TEXT.__const: 0x5f8
-  __TEXT.__cstring: 0x2bb21
-  __TEXT.__oslogstring: 0xdb49
-  __TEXT.__gcc_except_tab: 0x648c
+  __TEXT.__cstring: 0x2bc5c
+  __TEXT.__oslogstring: 0xdb82
+  __TEXT.__gcc_except_tab: 0x65a8
   __TEXT.__dlopen_cstrs: 0x514
   __TEXT.__ustring: 0x796
-  __TEXT.__unwind_info: 0xb240
-  __TEXT.__objc_classname: 0x4d83
-  __TEXT.__objc_methname: 0x4d394
-  __TEXT.__objc_methtype: 0x903b
-  __TEXT.__objc_stubs: 0x28380
+  __TEXT.__unwind_info: 0xb298
+  __TEXT.__objc_classname: 0x4dad
+  __TEXT.__objc_methname: 0x4d4c4
+  __TEXT.__objc_methtype: 0x9061
+  __TEXT.__objc_stubs: 0x28460
   __DATA_CONST.__got: 0x1440
-  __DATA_CONST.__const: 0xae90
-  __DATA_CONST.__objc_classlist: 0x11a0
+  __DATA_CONST.__const: 0xb1f8
+  __DATA_CONST.__objc_classlist: 0x11a8
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x260
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xefa8
+  __DATA_CONST.__objc_selrefs: 0xf008
   __DATA_CONST.__objc_protorefs: 0x88
-  __DATA_CONST.__objc_superrefs: 0xfc8
+  __DATA_CONST.__objc_superrefs: 0xfd0
   __DATA_CONST.__objc_arraydata: 0x260
   __AUTH_CONST.__auth_got: 0xb88
   __AUTH_CONST.__const: 0x3080
-  __AUTH_CONST.__cfstring: 0x23000
-  __AUTH_CONST.__objc_const: 0x45b98
+  __AUTH_CONST.__cfstring: 0x23140
+  __AUTH_CONST.__objc_const: 0x45c98
   __AUTH_CONST.__objc_arrayobj: 0x180
-  __AUTH_CONST.__objc_intobj: 0x4c8
+  __AUTH_CONST.__objc_intobj: 0x4e0
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x82f0
+  __AUTH.__objc_data: 0x8390
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0x322c
+  __DATA.__objc_ivar: 0x3234
   __DATA.__data: 0x1ce0
   __DATA.__bss: 0x870
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x2d50
+  __DATA_DIRTY.__objc_data: 0x2d00
   __DATA_DIRTY.__data: 0x48
   __DATA_DIRTY.__bss: 0x500
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B519092E-D1AB-3E31-8C81-51D9D16952C0
-  Functions: 20146
-  Symbols:   55303
-  CStrings:  24346
+  UUID: 63FDF0F0-2CD1-3D8B-A3F1-E6D6E65BEE71
+  Functions: 20164
+  Symbols:   55363
+  CStrings:  24379
 
Symbols:
+ -[MRActiveSystemEndpointAssertion acquireAssertion]
+ -[MRActiveSystemEndpointAssertion dealloc]
+ -[MRActiveSystemEndpointAssertion handleDidRestoreConnectionNotification:]
+ -[MRActiveSystemEndpointAssertion init]
+ -[MRActiveSystemEndpointAssertion isValid]
+ -[MRActiveSystemEndpointAssertion releaseAssertion]
+ -[MRCriticalSectionMonitor .cxx_destruct]
+ -[MRCriticalSectionMonitor _handleCriticalSectionDidBecomeCritical:]
+ -[MRCriticalSectionMonitor _handleCriticalSectionDidStopBeingCritical:]
+ -[MRCriticalSectionMonitor _handleMediaRemoteDeath:]
+ -[MRCriticalSectionMonitor _notifyIsCritical:]
+ -[MRCriticalSectionMonitor _updateCriticalState:]
+ -[MRCriticalSectionMonitor dealloc]
+ -[MRCriticalSectionMonitor delegateQueue]
+ -[MRCriticalSectionMonitor delegate]
+ -[MRCriticalSectionMonitor initWithDelegate:delegateQueue:]
+ -[MRCriticalSectionMonitor isCritical]
+ -[MRCriticalSectionMonitor isObserving]
+ -[MRCriticalSectionMonitor setCritical:]
+ -[MRCriticalSectionMonitor setDelegate:]
+ -[MRCriticalSectionMonitor setDelegateQueue:]
+ -[MRCriticalSectionMonitor setObserving:]
+ -[MRCriticalSectionMonitor startObserving]
+ -[MRCriticalSectionMonitor stopObserving]
+ _OBJC_CLASS_$_MRActiveSystemEndpointAssertion
+ _OBJC_CLASS_$_MRCriticalSectionMonitor
+ _OBJC_IVAR_$_MRActiveSystemEndpointAssertion._valid
+ _OBJC_IVAR_$_MRCriticalSectionMonitor._critical
+ _OBJC_IVAR_$_MRCriticalSectionMonitor._delegate
+ _OBJC_IVAR_$_MRCriticalSectionMonitor._delegateQueue
+ _OBJC_IVAR_$_MRCriticalSectionMonitor._observing
+ _OBJC_METACLASS_$_MRActiveSystemEndpointAssertion
+ _OBJC_METACLASS_$_MRCriticalSectionMonitor
+ __MRCriticalSectionMonitorDidBecomeCriticalNotification
+ __MRCriticalSectionMonitorDidStopBeingCriticalNotification
+ __OBJC_$_INSTANCE_METHODS_MRActiveSystemEndpointAssertion
+ __OBJC_$_INSTANCE_METHODS_MRCriticalSectionMonitor
+ __OBJC_$_INSTANCE_VARIABLES_MRActiveSystemEndpointAssertion
+ __OBJC_$_INSTANCE_VARIABLES_MRCriticalSectionMonitor
+ __OBJC_$_PROP_LIST_MRActiveSystemEndpointAssertion
+ __OBJC_$_PROP_LIST_MRCriticalSectionMonitor
+ __OBJC_CLASS_RO_$_MRActiveSystemEndpointAssertion
+ __OBJC_CLASS_RO_$_MRCriticalSectionMonitor
+ __OBJC_METACLASS_RO_$_MRActiveSystemEndpointAssertion
+ __OBJC_METACLASS_RO_$_MRCriticalSectionMonitor
+ ___46-[MRCriticalSectionMonitor _notifyIsCritical:]_block_invoke
+ ____MRMediaRemoteGetDeviceUIDWithRetryIntervals_block_invoke.486
+ ____MRMediaRemoteGetDeviceUIDWithRetryIntervals_block_invoke.487
+ ___block_literal_global.484
+ ___block_literal_global.625
+ ___block_literal_global.652
+ ___block_literal_global.687
+ _objc_msgSend$_notifyIsCritical:
+ _objc_msgSend$_updateCriticalState:
+ _objc_msgSend$acquireAssertion
+ _objc_msgSend$criticalSectionMonitorDidBecomeCritical:
+ _objc_msgSend$criticalSectionMonitorDidStopBeingCritical:
+ _objc_msgSend$setCritical:
+ _objc_msgSend$stopObserving
- -[MRNotification .cxx_destruct]
- -[MRNotification _createNotificationMessage:userInfo:]
- -[MRNotification initWithNotification:userInfo:]
- -[MRNotification notification]
- -[MRNotification setXpcMessage:]
- -[MRNotification userInfo]
- -[MRNotification xpcMessage]
- _OBJC_CLASS_$_MRNotification
- _OBJC_IVAR_$_MRNotification._notification
- _OBJC_IVAR_$_MRNotification._userInfo
- _OBJC_IVAR_$_MRNotification._xpcMessage
- _OBJC_METACLASS_$_MRNotification
- __OBJC_$_INSTANCE_METHODS_MRNotification
- __OBJC_$_INSTANCE_VARIABLES_MRNotification
- __OBJC_$_PROP_LIST_MRNotification
- __OBJC_CLASS_RO_$_MRNotification
- __OBJC_METACLASS_RO_$_MRNotification
- ____MRMediaRemoteGetDeviceUIDWithRetryIntervals_block_invoke.456
- ____MRMediaRemoteGetDeviceUIDWithRetryIntervals_block_invoke.457
- ___block_literal_global.454
- ___block_literal_global.592
- ___block_literal_global.595
- ___block_literal_global.657
CStrings:
+ "<%@: %p | session id: %@ | audio format: %@ - %@ | channel #: %@ | available: %@ | eligible: %@ | active: %@ | intended :%ld | resolved :%ld | rendering :%ld | pid: %i | bundleID: %@>"
+ "@\"<MRCriticalSectionMonitorDelegate>\""
+ "ApplicationDisabled"
+ "CommandNotSupported"
+ "MRActiveSystemEndpointAssertion"
+ "MRActiveSystemEndpointAssertion.acquire"
+ "MRActiveSystemEndpointAssertion.release"
+ "MRCriticalSectionMonitor"
+ "T@\"<MRCriticalSectionMonitorDelegate>\",W,N,V_delegate"
+ "TB,N,GisCritical,V_critical"
+ "TimedoutWaitingForCanBeNowPlaying"
+ "Unknown(%ld)"
+ "[MRGroupSession] Will begin assertion %@ for session: %@"
+ "_MRCriticalSectionMonitorDidBecomeCriticalNotification"
+ "_MRCriticalSectionMonitorDidStopBeingCriticalNotification"
+ "_critical"
+ "_handleCriticalSectionDidBecomeCritical:"
+ "_handleCriticalSectionDidStopBeingCritical:"
+ "_handleMediaRemoteDeath:"
+ "_notifyIsCritical:"
+ "_updateCriticalState:"
+ "acquireAssertion"
+ "critical"
+ "criticalSectionMonitorDidBecomeCritical:"
+ "criticalSectionMonitorDidStopBeingCritical:"
+ "externalErrorCode"
+ "handleDidRestoreConnectionNotification:"
+ "initWithDelegate:delegateQueue:"
+ "isCritical"
+ "releaseAssertion"
+ "setCritical:"
+ "startObserving"
+ "stopObserving"
- "<%@: %p | session id: %@ | audio format: %@ - %@ | channel #: %@ | available: %@ | eligible: %@ | active: %@ | intended :%ld | resolved :%ld | pid: %i | bundleID: %@>"
- "MRNotification"
- "T@\"NSDictionary\",R,N,V_userInfo"
- "T@\"NSObject<OS_xpc_object>\",&,N,V_xpcMessage"
- "T@\"NSString\",R,N,V_notification"
- "_notification"
- "_xpcMessage"
- "initWithNotification:userInfo:"
- "setXpcMessage:"
- "xpcMessage"

```
