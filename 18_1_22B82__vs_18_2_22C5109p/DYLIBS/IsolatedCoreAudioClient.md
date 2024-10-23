## IsolatedCoreAudioClient

> `/System/Library/PrivateFrameworks/IsolatedCoreAudioClient.framework/IsolatedCoreAudioClient`

```diff

-5.103.0.0.0
-  __TEXT.__text: 0xefa8
-  __TEXT.__auth_stubs: 0x870
-  __TEXT.__objc_methlist: 0x290
-  __TEXT.__gcc_except_tab: 0xfa4
-  __TEXT.__const: 0x1985
-  __TEXT.__cstring: 0x546
-  __TEXT.__oslogstring: 0x14f2
-  __TEXT.__unwind_info: 0x8f0
-  __TEXT.__objc_classname: 0xdb
-  __TEXT.__objc_methname: 0x7dd
-  __TEXT.__objc_methtype: 0x53e
-  __TEXT.__objc_stubs: 0x5a0
-  __DATA_CONST.__got: 0xa8
-  __DATA_CONST.__const: 0x170
-  __DATA_CONST.__objc_classlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x28
+5.319.0.0.0
+  __TEXT.__text: 0x16624
+  __TEXT.__auth_stubs: 0x920
+  __TEXT.__objc_methlist: 0x5c4
+  __TEXT.__gcc_except_tab: 0x17c8
+  __TEXT.__const: 0x2401
+  __TEXT.__cstring: 0x684
+  __TEXT.__oslogstring: 0x2272
+  __TEXT.__unwind_info: 0xcf0
+  __TEXT.__objc_classname: 0x1ee
+  __TEXT.__objc_methname: 0xf15
+  __TEXT.__objc_methtype: 0xaea
+  __TEXT.__objc_stubs: 0xa80
+  __DATA_CONST.__got: 0xc8
+  __DATA_CONST.__const: 0x1d0
+  __DATA_CONST.__objc_classlist: 0x48
+  __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d8
-  __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x448
-  __AUTH_CONST.__const: 0x1658
-  __AUTH_CONST.__cfstring: 0x1c0
-  __AUTH_CONST.__objc_const: 0x910
-  __DATA.__objc_ivar: 0x18
-  __DATA.__data: 0x1e0
-  __DATA.__bss: 0xa8
+  __DATA_CONST.__objc_selrefs: 0x390
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_superrefs: 0x48
+  __AUTH_CONST.__auth_got: 0x4a0
+  __AUTH_CONST.__const: 0x1ed0
+  __AUTH_CONST.__cfstring: 0x160
+  __AUTH_CONST.__objc_const: 0x1138
+  __AUTH.__objc_data: 0x190
+  __DATA.__objc_ivar: 0x54
+  __DATA.__data: 0x300
+  __DATA.__bss: 0x1a0
   __DATA_DIRTY.__objc_data: 0x140
-  __DATA_DIRTY.__bss: 0x30
+  __DATA_DIRTY.__bss: 0x8
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/caulk.framework/caulk
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 506
-  Symbols:   680
-  CStrings:  254
+  Functions: 731
+  Symbols:   922
+  CStrings:  447
 
Symbols:
+ _CreateIsolatedAudioSiphonPortal
+ _CreateMicrophoneActivityPortal
+ _OBJC_CLASS_$_NSMutableDictionary
+ __ZNSt12out_of_rangeD1Ev
+ __ZNSt3__118condition_variableD1Ev
+ __ZNSt3__119__shared_mutex_base11lock_sharedEv
+ __ZNSt3__119__shared_mutex_base13unlock_sharedEv
+ __ZNSt3__119__shared_mutex_base4lockEv
+ __ZNSt3__119__shared_mutex_base6unlockEv
+ __ZNSt3__119__shared_mutex_baseC1Ev
+ __ZTISt12out_of_range
+ __ZTVSt12out_of_range
+ _audit_token_to_pid
+ _objc_retain_x24
+ _objc_retain_x25
+ _objc_retain_x5
+ _tb_endpoint_set_interface_identifier
+ _tb_message_decode_s32
+ _tb_message_encode_u32
- _objc_release_x9
- _tb_message_decode_bool
CStrings:
+ "\x11"
+ "%!s(MISSING):%!d(MISSING)  Code:\t\t\t%!l(MISSING)d"
+ "%!s(MISSING):%!d(MISSING)  Description:\t%!@(MISSING)"
+ "%!s(MISSING):%!d(MISSING)  Reason:\t\t%!@(MISSING)"
+ "%!s(MISSING):%!d(MISSING)  Suggestion:\t%!@(MISSING)"
+ "%!s(MISSING):%!d(MISSING) %!@(MISSING): %!@(MISSING) %!@(MISSING)\n"
+ "%!s(MISSING):%!d(MISSING) %!s(MISSING) called Start IO"
+ "%!s(MISSING):%!d(MISSING) %!s(MISSING) called Stop IO"
+ "%!s(MISSING):%!d(MISSING) Attempt to connect to IsolatedAudio sever via XPC failed."
+ "%!s(MISSING):%!d(MISSING) AudioClientBase::createDedicatedClient..."
+ "%!s(MISSING):%!d(MISSING) AudioClientBase::createUnitTestClient..."
+ "%!s(MISSING):%!d(MISSING) AudioClientBase::getClient - client:%!p(MISSING)..."
+ "%!s(MISSING):%!d(MISSING) AudioClientBase::getClient..."
+ "%!s(MISSING):%!d(MISSING) AudioClientBase::stubEKs = %!s(MISSING)"
+ "%!s(MISSING):%!d(MISSING) ClientSideAudioSwitchboardIOThread::IOMainWorkloopFunction - timed out waiting for signal from server."
+ "%!s(MISSING):%!d(MISSING) ClientSideAudioSwitchboardIOThread::IOSetUpFunction - timed out waiting for signal from server."
+ "%!s(MISSING):%!d(MISSING) ClientSideAudioSwitchboardIOThread::IOSetUpFunction - unknown error occurred waiting for signal from server."
+ "%!s(MISSING):%!d(MISSING) Could not create get workgroup for deviceID: %!d(MISSING) because of Error:%!@(MISSING)"
+ "%!s(MISSING):%!d(MISSING) CreateIsolatedAudioSiphonPortal allocating portal"
+ "%!s(MISSING):%!d(MISSING) CreateIsolatedAudioSiphonPortal unsupported"
+ "%!s(MISSING):%!d(MISSING) CreateMicrophoneActivityPortal allocating portal"
+ "%!s(MISSING):%!d(MISSING) CreateMicrophoneActivityPortal unsupported"
+ "%!s(MISSING):%!d(MISSING) Disabling lapse handling on %!s(MISSING) client"
+ "%!s(MISSING):%!d(MISSING) Enabling lapse handling on %!s(MISSING) client"
+ "%!s(MISSING):%!d(MISSING) Hello Siphon"
+ "%!s(MISSING):%!d(MISSING) Hello Siphon Tests"
+ "%!s(MISSING):%!d(MISSING) IsolatedCoreAudioClientMultiplexer:: IO has lapsed with status %!d(MISSING)"
+ "%!s(MISSING):%!d(MISSING) IsolatedCoreAudioClientMultiplexer:: IO lapsed during rendezvous."
+ "%!s(MISSING):%!d(MISSING) IsolatedCoreAudioClientMultiplexer::startIOIfNoClientsAreRunning IO already running"
+ "%!s(MISSING):%!d(MISSING) IsolatedCoreAudioClientMultiplexer::startIOIfNoClientsAreRunning IO failed to start with status %!d(MISSING)"
+ "%!s(MISSING):%!d(MISSING) IsolatedCoreAudioClientMultiplexer::startSharedIO failed to start for use case %!s(MISSING) with status %!d(MISSING)"
+ "%!s(MISSING):%!d(MISSING) IsolatedCoreAudioClientMultiplexer::stopIOIfNoClientsAreRunning Stop requested, but no client IO is running IO"
+ "%!s(MISSING):%!d(MISSING) IsolatedCoreAudioClientMultiplexer::stopIOIfNoClientsAreRunning sending Stop message to server"
+ "%!s(MISSING):%!d(MISSING) IsolatedCoreAudioClientNSXPCListenerDelegate - Listener"
+ "%!s(MISSING):%!d(MISSING) IsolatedCoreAudioClientNSXPCListenerDelegate - interruptionHandler"
+ "%!s(MISSING):%!d(MISSING) IsolatedCoreAudioClientNSXPCListenerDelegate - invalidationHandler"
+ "%!s(MISSING):%!d(MISSING) IsolatedCoreAudioXPCSiphon - requestAudio Landed in the catch!"
+ "%!s(MISSING):%!d(MISSING) IsolatedCoreAudioXPCSiphon - setAudioAvailabilityCallback Landed in the catch!"
+ "%!s(MISSING):%!d(MISSING) IsolatedCoreAudioXPCSiphon - startIO Landed in the catch!"
+ "%!s(MISSING):%!d(MISSING) IsolatedCoreAudioXPCSiphon - stopIO Landed in the catch!"
+ "%!s(MISSING):%!d(MISSING) IsolatedDeviceIOProc error: inClientData is NULL!"
+ "%!s(MISSING):%!d(MISSING) Received CreateIsolatedAudioSiphonPortal request"
+ "%!s(MISSING):%!d(MISSING) Received CreateMicrophoneActivityPortal request"
+ "%!s(MISSING):%!d(MISSING) Reverse connection interrupted"
+ "%!s(MISSING):%!d(MISSING) Reverse connection invalidated"
+ "%!s(MISSING):%!d(MISSING) ReverseSiphonDelegate AudioAvailabilityCallback failed."
+ "%!s(MISSING):%!d(MISSING) ReverseSiphonDelegate LapseCallback failed."
+ "%!s(MISSING):%!d(MISSING) ServerSideAudioSwitchboard::addClientUseCase stopping IO for unresponsive client %!s(MISSING)"
+ "%!s(MISSING):%!d(MISSING) ServerSideAudioSwitchboard::startServerIOThread IO not started for client %!s(MISSING)"
+ "%!s(MISSING):%!d(MISSING) ServerSideAudioSwitchboard::stopServerIOThread IO not stopped for client %!s(MISSING)"
+ "%!s(MISSING):%!d(MISSING) SiphonIOClient: Lapse callback threw an exception."
+ "%!s(MISSING):%!d(MISSING) SiphonIOClient::setHasStartedIO - Dispatch Queue has been flushed"
+ "%!s(MISSING):%!d(MISSING) Starting IO on the %!s(MISSING) client"
+ "%!s(MISSING):%!d(MISSING) Stopping IO for %!s(MISSING) client after losing connection to their process recently at pid %!d(MISSING)"
+ "%!s(MISSING):%!d(MISSING) Stopping IO on the %!s(MISSING) client"
+ "%!s(MISSING):%!d(MISSING) Synchronous StopIO Complete for %!s(MISSING) client"
+ "%!s(MISSING):%!d(MISSING) Waiting for Availability callbacks to complete for %!s(MISSING) client"
+ "%!s(MISSING):%!d(MISSING) setAudioAvailabilityCallback called"
+ "%!s(MISSING):%!d(MISSING) setAudioLapseCallback called"
+ "%!s(MISSING):%!d(MISSING) translateFerryToSinkStatus encountered an error! Result: %!d(MISSING)"
+ "@\"NSMutableDictionary\""
+ "@\"NSXPCConnection\""
+ "@\"NSXPCInterface\""
+ "@\"NSXPCListener\""
+ "@20@0:8i16"
+ "@48@0:8{function<void (int)>={__value_func<void (int)>={type=[24C]}^v}}16"
+ "@48@0:8{shared_ptr<SiphonClientMap>=^{SiphonClientMap}^{__shared_weak_count}}16{shared_ptr<ClientLocalServer>=^{ClientLocalServer}^{__shared_weak_count}}32"
+ "AudioAvailabilityCallback:atSample:with:"
+ "AudioClientInstance.cpp"
+ "B"
+ "Error on remote object proxy"
+ "I"
+ "I16@0:8"
+ "I20@0:8i16"
+ "IsolatedCoreAudio"
+ "IsolatedCoreAudioClient"
+ "IsolatedCoreAudioClientBaseNSXPCConnection.mm"
+ "IsolatedCoreAudioClientMultiplexer.cpp"
+ "IsolatedCoreAudioClientNSXPCListenerDelegate"
+ "IsolatedCoreAudioClientNSXPCListenerDelegate.mm"
+ "IsolatedCoreAudioClientWorkgroup.mm"
+ "IsolatedCoreAudioReverseSiphonProtocol"
+ "IsolatedCoreAudioSiphon"
+ "IsolatedCoreAudioSiphonProtocol"
+ "IsolatedCoreAudioUseCaseConnection"
+ "IsolatedCoreAudioXPCSiphon"
+ "IsolatedCoreAudioXPCSiphon.mm"
+ "IsolatedDeviceIOProc.h"
+ "LapseCallback:with:"
+ "MTDClientInterface"
+ "MicActivityClientProtocol"
+ "ReverseSiphonDelegate"
+ "ReverseSiphonDelegate.mm"
+ "SiphonClientMap.cpp"
+ "SiphonIOClient.cpp"
+ "T@\"NSMutableDictionary\",&,N,V_mConnections"
+ "T@\"NSMutableSet\",&,N,V_reverseConnections"
+ "T@\"NSXPCConnection\",&,N,V_connection"
+ "T@\"NSXPCInterface\",&,N,V_mInterface"
+ "T@\"NSXPCInterface\",&,N,V_reverseInterface"
+ "T@\"NSXPCListener\",&,N,V_reverseListener"
+ "TI,N,VuseCaseID"
+ "Ti,N,V_pid"
+ "T{function<void (int)>={__value_func<void (int)>={type=[24C]}^v}},N,V_mClientReaper"
+ "T{shared_ptr<IsolatedCoreAudioSiphon>=^{IsolatedCoreAudioSiphon}^{__shared_weak_count}},N,V_mSiphon"
+ "T{shared_ptr<SiphonClientMap>=^{SiphonClientMap}^{__shared_weak_count}},N,V_mClientMap"
+ "XPC_Connection_PID_Access"
+ "^?"
+ "^v"
+ "_connection"
+ "_mClientMap"
+ "_mClientReaper"
+ "_mConnections"
+ "_mInterface"
+ "_mSiphon"
+ "_pid"
+ "_reverseConnections"
+ "_reverseInterface"
+ "_reverseListener"
+ "activate"
+ "anonymousListener"
+ "auditToken"
+ "com.apple.audio.isolatedcoreaudio.asyncio_"
+ "com.apple.audio.micactivityd"
+ "com.apple.shareddspd"
+ "connectToUseCase:endpoint:"
+ "connection"
+ "createClientReaper"
+ "currentConnection"
+ "dictionary"
+ "disable_microphone_activity_detection_with_reply:"
+ "enable_microphone_activity_detection_with_reply:"
+ "false"
+ "getPIDFromCurrentConnection"
+ "getProcessID"
+ "getUseCaseIDForPID:"
+ "i"
+ "i16@0:8"
+ "initClientMap"
+ "initWithClientMap:andServer:"
+ "initWithClientReaper:"
+ "initWithConnection:"
+ "initWithInterface:"
+ "listen_for_microphone_activity:reply:"
+ "lookupConnectionForPID:"
+ "mAvailabilityCallback"
+ "mAvailabilityData"
+ "mClientMap"
+ "mClientReaper"
+ "mConnections"
+ "mInterface"
+ "mLapseCallback"
+ "mLapseData"
+ "mSiphon"
+ "numberWithInt:"
+ "objectForKey:"
+ "pid"
+ "register_client:reply:"
+ "removeObjectForKey:"
+ "requestAudio:atTime:atSample:with:"
+ "reverseConnections"
+ "reverseInterface"
+ "reverseListener"
+ "setAudioAvailabilityCallback:usingXPC:with:"
+ "setAudioLapseCallback:usingXPC:with:"
+ "setAvailabilityCallback:data:"
+ "setClientReaper:"
+ "setConnection:"
+ "setLapseCallback:data:"
+ "setMClientMap:"
+ "setMClientReaper:"
+ "setMConnections:"
+ "setMInterface:"
+ "setMSiphon:"
+ "setObject:forKey:"
+ "setPid:"
+ "setReverseConnections:"
+ "setReverseInterface:"
+ "setReverseListener:"
+ "setUseCaseID:"
+ "setUseCaseIDForCurrentConnection:"
+ "startIO:with:"
+ "stopIO:with:"
+ "stop_listening_for_microphone_activity_with_reply:"
+ "unordered_map::at: key not found"
+ "useCaseID"
+ "v20@0:8i16"
+ "v24@0:8@?16"
+ "v24@0:8@?<v@?i>16"
+ "v28@0:8I16@20"
+ "v28@0:8i16@?20"
+ "v28@0:8i16@?<v@?i>20"
+ "v32@0:8@\"NSXPCListenerEndpoint\"16@?<v@?i>24"
+ "v32@0:8@16@?24"
+ "v32@0:8^?16^v24"
+ "v32@0:8{shared_ptr<IsolatedCoreAudioSiphon>=^{IsolatedCoreAudioSiphon}^{__shared_weak_count}}16"
+ "v32@0:8{shared_ptr<SiphonClientMap>=^{SiphonClientMap}^{__shared_weak_count}}16"
+ "v36@0:8I16@\"NSXPCListenerEndpoint\"20@?<v@?i>28"
+ "v36@0:8I16@20@?28"
+ "v40@0:8Q16Q24@?32"
+ "v40@0:8Q16Q24@?<v@?i>32"
+ "v44@0:8I16Q20Q28@?36"
+ "v44@0:8I16Q20Q28@?<v@?i>36"
+ "v48@0:8{function<void (int)>={__value_func<void (int)>={type=[24C]}^v}}16"
+ "{function<void (int)>=\"__f_\"{__value_func<void (int)>=\"__buf_\"{type=\"__lx\"[24C]}\"__f_\"^v}}"
+ "{function<void (int)>={__value_func<void (int)>={type=[24C]}^v}}16@0:8"
+ "{shared_ptr<IsolatedCoreAudioSiphon>=\"__ptr_\"^{IsolatedCoreAudioSiphon}\"__cntrl_\"^{__shared_weak_count}}"
+ "{shared_ptr<IsolatedCoreAudioSiphon>=^{IsolatedCoreAudioSiphon}^{__shared_weak_count}}16@0:8"
+ "{shared_ptr<SiphonClientMap>=\"__ptr_\"^{SiphonClientMap}\"__cntrl_\"^{__shared_weak_count}}"
+ "{shared_ptr<SiphonClientMap>=^{SiphonClientMap}^{__shared_weak_count}}16@0:8"
- " Code:\t\t\t%!l(MISSING)d"
- " Description:\t%!@(MISSING)"
- " Reason:\t\t%!@(MISSING)"
- " Suggestion:\t%!@(MISSING)"
- "%!s(MISSING):%!d(MISSING) IsolatedCoreAudioXPCService - Listener"
- "%!s(MISSING):%!d(MISSING) IsolatedCoreAudioXPCService - interruptionHandler"
- "%!s(MISSING):%!d(MISSING) IsolatedCoreAudioXPCService - invalidationHandler"
- "%!s(MISSING):%!d(MISSING) isolatedcoreaudioclient_isolatedcoreaudioclientservice_dosetup result: %!d(MISSING)"
- "Attempt to connect to IsolatedAudio sever via XPC failed."
- "Could not create get workgroup for deviceID: %!d(MISSING) because of Error:%!@(MISSING)"
- "T@\"NSMutableSet\",&,N,V_connections"
- "_connections"
- "clientPrerequisitesMet: "
- "connections"
- "removeObject:"
- "setConnections:"
- "v12@?0B8"

```
