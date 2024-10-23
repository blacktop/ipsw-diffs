## AudioServerDriverTransports_IOA2

> `/System/Library/PrivateFrameworks/AudioServerDriverTransports_IOA2.framework/AudioServerDriverTransports_IOA2`

```diff

-200.54.0.0.0
-  __TEXT.__text: 0x32aec
-  __TEXT.__auth_stubs: 0xfe0
-  __TEXT.__objc_methlist: 0x16ac
-  __TEXT.__gcc_except_tab: 0x5394
+220.21.0.0.0
+  __TEXT.__text: 0x352b8
+  __TEXT.__auth_stubs: 0x1060
+  __TEXT.__objc_methlist: 0x1854
+  __TEXT.__gcc_except_tab: 0x5ef0
   __TEXT.__const: 0x710
-  __TEXT.__cstring: 0xfbd
-  __TEXT.__oslogstring: 0x2e30
-  __TEXT.__unwind_info: 0x1db8
-  __TEXT.__objc_classname: 0x314
-  __TEXT.__objc_methname: 0x274e
-  __TEXT.__objc_methtype: 0x1d21
-  __TEXT.__objc_stubs: 0x2300
-  __DATA_CONST.__got: 0x260
-  __DATA_CONST.__const: 0x210
-  __DATA_CONST.__objc_classlist: 0xe8
+  __TEXT.__cstring: 0x1016
+  __TEXT.__oslogstring: 0x30a6
+  __TEXT.__unwind_info: 0x1e88
+  __TEXT.__objc_classname: 0x33e
+  __TEXT.__objc_methname: 0x2bbb
+  __TEXT.__objc_methtype: 0x1d9e
+  __TEXT.__objc_stubs: 0x2720
+  __DATA_CONST.__got: 0x280
+  __DATA_CONST.__const: 0x238
+  __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x20
+  __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb80
-  __DATA_CONST.__objc_superrefs: 0xc8
-  __AUTH_CONST.__auth_got: 0x800
+  __DATA_CONST.__objc_selrefs: 0xc80
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_superrefs: 0xd0
+  __AUTH_CONST.__auth_got: 0x840
   __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__const: 0x858
+  __AUTH_CONST.__const: 0x878
   __AUTH_CONST.__cfstring: 0xc60
-  __AUTH_CONST.__objc_const: 0x2a60
+  __AUTH_CONST.__objc_const: 0x2d28
   __AUTH_CONST.__objc_intobj: 0x288
-  __AUTH.__objc_data: 0x910
-  __DATA.__objc_ivar: 0x180
-  __DATA.__data: 0x180
+  __AUTH.__objc_data: 0x960
+  __DATA.__objc_ivar: 0x198
+  __DATA.__data: 0x1e8
   __DATA.__common: 0x10
+  __DATA.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1313
-  Symbols:   1778
-  CStrings:  1047
+  Functions: 1341
+  Symbols:   1815
+  CStrings:  1113
 
Symbols:
+ _ASDTBaseLogType
+ _ASDTIOA2LogType
+ _OBJC_CLASS_$_ASDTCustomProperty
+ _OBJC_CLASS_$_ASDTIOA2InjectionStream
+ _OBJC_CLASS_$_NSData
+ _OBJC_METACLASS_$_ASDTIOA2InjectionStream
+ __ZN4ASDT8Exclaves11AudioBuffer4ReadEPhjjRNS0_6Sensor6StatusE
+ __ZN4ASDT8Exclaves13StatusTracker4PushERKNS1_6UpdateE
+ __ZN8ASDTTime16machAbsoluteTimeEv
+ __ZNK4ASDT12IOUserClient21GetConnectionRefCountEv
+ __ZNK4ASDT12IOUserClient21GetUserClientRefCountEv
+ __ZNK4ASDT14IOA2UserClient28SupportsInputStreamInjectionEv
+ _dispatch_once
+ _kASDTConfigKeySubclass
+ _kASDTIOA2ConfigKeyExclavesInjectionBufferName
+ _objc_retain_x4
+ _os_log_create
- __ZN4ASDT8Exclaves11NamedBuffer4ReadEPhjj
CStrings:
+ "\x11"
+ "%!@(MISSING): Adding injection stream."
+ "%!@(MISSING): Bad stream dict: %!@(MISSING)"
+ "%!@(MISSING): Error creating device properties."
+ "%!@(MISSING): Failed to create control for dict: %!@(MISSING)"
+ "%!@(MISSING): Failed to create injection stream from %!@(MISSING)."
+ "%!@(MISSING): Failed to create stream from: %!@(MISSING)"
+ "%!@(MISSING): Removing injection stream."
+ "%!@(MISSING): Using deprecated method to create streams."
+ "%!@(MISSING):%!@(MISSING): Bad registry dictionary."
+ "%!@(MISSING):%!@(MISSING): Clearing buffer; user client refs: %!u(MISSING), connection refs: %!u(MISSING)"
+ "%!@(MISSING):%!@(MISSING): Exclaves inbound buffer size: %!u(MISSING)"
+ "%!@(MISSING):%!@(MISSING): Exclaves injection buffer name is not supplied."
+ "%!@(MISSING):%!@(MISSING): Failed to allocate exclaves inbound buffer."
+ "%!@(MISSING):%!@(MISSING): Failed to setup non-secure input path."
+ "%!@(MISSING):%!@(MISSING): Stream not active for ioThread start."
+ "%!u(MISSING)-Injection"
+ "@\"ASDTCustomProperty\""
+ "@\"ASDTIOA2InjectionStream\""
+ "@\"ASDTIOA2Stream\""
+ "@32@0:8I16I20@24"
+ "@40@0:8@16I24I28@32"
+ "A"
+ "ASDTIOA2InjectionStream"
+ "ASDTIOA2Object"
+ "ASDTRawProperty"
+ "ExclavesInjectionBufferName"
+ "IOA2"
+ "T@\"ASDTCustomProperty\",&,N,V_injectionStreamEnableProperty"
+ "T@\"ASDTIOA2InjectionStream\",&,N,V_injectionStream"
+ "T@\"ASDTIOA2InjectionStream\",W,N,V_injectionStream"
+ "T@\"ASDTIOA2Stream\",W,N,V_inputStream"
+ "T@\"NSString\",&,N,V_exclavesInjectionBufferName"
+ "_addStreams:"
+ "_createDeviceProperties"
+ "_exclavesInjectionBufferName"
+ "_getObjectByUCID:fromObjects:"
+ "_injectionStream"
+ "_injectionStreamEnableProperty"
+ "_inputStream"
+ "_markOrCreateStreamsForDirection:"
+ "_removeStreams:"
+ "addObserver:forKeyPath:options:context:"
+ "allocExclavesAudioBuffer:"
+ "asdtExclavesInjectionBufferName"
+ "asdtIOThreadChangeEvent"
+ "asdtIOThreadChangeIsolatedUseCase"
+ "asdtIOThreadUseCaseIsFirstOrWasLast"
+ "clearMark:"
+ "com.apple.audio.ASDT"
+ "containsObject:"
+ "createStreamForUserClientID:direction:registryDict:"
+ "customPropertyForConfig:"
+ "dataWithBytes:length:"
+ "exclavesAudioBuffer"
+ "exclavesBufferName"
+ "exclavesInjectionBufferName"
+ "exclavesSensorManager"
+ "freeExclavesAudioBuffer"
+ "initWithIOA2Device:inputStream:registryDict:"
+ "initWithIOA2Device:userClientID:direction:registryDict:"
+ "injectionStream"
+ "injectionStreamEnableProperty"
+ "input stream injection"
+ "inputStream"
+ "ioThreadStateChange:"
+ "observeValueForKeyPath:ofObject:change:context:"
+ "performTerminate"
+ "removeObserver:forKeyPath:"
+ "setExclavesInjectionBufferName:"
+ "setInjectionStream:"
+ "setInjectionStreamEnableProperty:"
+ "setInputStream:"
+ "shared_lock::unlock: not locked"
+ "statusTracker"
+ "unmarkedObjects:"
+ "updateActiveState"
+ "updateInjectionVisibility"
+ "usesExclavesAudioBuffer"
+ "v48@0:8@16@24@32^v40"
+ "\xf0\xf0\xf0\x92\x13\x13"
- "ASDTIOA2Device.mm"
- "TQ,N,V_exclavesInputBufferID"
- "_exclavesInputBufferID"
- "allocExclavesNamedBuffer:"
- "control"
- "exclavesBuffer"
- "exclavesInputBufferID"
- "freeExclavesNamedBuffer"
- "insertObject:atIndex:"
- "operation"
- "registryDict"
- "setExclavesInputBufferID:"
- "terminate"
- "usesExclavesNamedBuffer"
- "\xf0\xf0\xf0\x92\x11\x11\x11"

```
