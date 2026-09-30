## AudioServerDriverTransports_Base

> `/System/Library/PrivateFrameworks/AudioServerDriverTransports_Base.framework/AudioServerDriverTransports_Base`

```diff

-200.54.0.0.0
-  __TEXT.__text: 0x3b208
-  __TEXT.__auth_stubs: 0xec0
-  __TEXT.__objc_methlist: 0x29a4
-  __TEXT.__const: 0x306
-  __TEXT.__oslogstring: 0x2986
-  __TEXT.__cstring: 0x164a
-  __TEXT.__gcc_except_tab: 0x4b0c
-  __TEXT.__unwind_info: 0x1ca8
-  __TEXT.__objc_classname: 0x58c
-  __TEXT.__objc_methname: 0x61ff
-  __TEXT.__objc_methtype: 0xe3e
-  __TEXT.__objc_stubs: 0x5ae0
-  __DATA_CONST.__got: 0x298
-  __DATA_CONST.__const: 0x678
-  __DATA_CONST.__objc_classlist: 0x168
+220.21.0.0.0
+  __TEXT.__text: 0x3f844
+  __TEXT.__auth_stubs: 0xf50
+  __TEXT.__objc_methlist: 0x2c70
+  __TEXT.__gcc_except_tab: 0x5504
+  __TEXT.__const: 0x3d6
+  __TEXT.__cstring: 0x17e7
+  __TEXT.__oslogstring: 0x2d67
+  __TEXT.__unwind_info: 0x1eb0
+  __TEXT.__objc_classname: 0x5fe
+  __TEXT.__objc_methname: 0x67fb
+  __TEXT.__objc_methtype: 0x10ac
+  __TEXT.__objc_stubs: 0x60a0
+  __DATA_CONST.__got: 0x2c8
+  __DATA_CONST.__const: 0x700
+  __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1968
+  __DATA_CONST.__objc_selrefs: 0x1af0
   __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_superrefs: 0x140
-  __AUTH_CONST.__auth_got: 0x778
+  __DATA_CONST.__objc_superrefs: 0x150
+  __AUTH_CONST.__auth_got: 0x7c0
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x1d8
-  __AUTH_CONST.__cfstring: 0x16e0
-  __AUTH_CONST.__objc_const: 0x4f88
+  __AUTH_CONST.__const: 0x320
+  __AUTH_CONST.__cfstring: 0x1860
+  __AUTH_CONST.__objc_const: 0x5470
   __AUTH_CONST.__objc_intobj: 0x120
-  __AUTH.__objc_data: 0x780
-  __DATA.__objc_ivar: 0x2bc
-  __DATA.__data: 0x730
-  __DATA.__bss: 0xd
-  __DATA_DIRTY.__objc_data: 0x690
+  __AUTH.__objc_data: 0x910
+  __DATA.__objc_ivar: 0x2e8
+  __DATA.__data: 0x738
+  __DATA.__bss: 0x3d
+  __DATA_DIRTY.__objc_data: 0x640
   __DATA_DIRTY.__bss: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/AudioServerDriver.framework/AudioServerDriver
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/SystemStatus.framework/SystemStatus
+  - /System/Library/PrivateFrameworks/caulk.framework/caulk
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1613
-  Symbols:   2184
-  CStrings:  1955
+  Functions: 1707
+  Symbols:   2315
+  CStrings:  2074
 
Symbols:
+ _ASDTBaseLogType
+ _OBJC_CLASS_$_ASDTExclavesSensorAutomaticProperty
+ _OBJC_CLASS_$_ASDTExclavesSensorManager
+ _OBJC_CLASS_$_ASDTExclavesStatusProperty
+ _OBJC_CLASS_$_ASDTSystemStatus
+ _OBJC_CLASS_$_MockASDTSystemStatus
+ _OBJC_CLASS_$_STActivityAttribution
+ _OBJC_CLASS_$_STMediaStatusDomainMicrophoneRecordingAttribution
+ _OBJC_CLASS_$_STMediaStatusDomainPublisher
+ _OBJC_METACLASS_$_ASDTExclavesSensorAutomaticProperty
+ _OBJC_METACLASS_$_ASDTExclavesSensorManager
+ _OBJC_METACLASS_$_ASDTExclavesStatusProperty
+ _OBJC_METACLASS_$_ASDTSystemStatus
+ _OBJC_METACLASS_$_MockASDTSystemStatus
+ __ZN4ASDT12IOUserClient19GetIOObjectRefCountEj
+ __ZN4ASDT8Exclaves11AudioBuffer4ReadEPNS1_6VectorEmRNS0_6Sensor6StatusE
+ __ZN4ASDT8Exclaves11AudioBuffer4ReadEPhjjRNS0_6Sensor6StatusE
+ __ZN4ASDT8Exclaves11AudioBuffer4ReadEPhjjjyRNS0_6Sensor6StatusE
+ __ZN4ASDT8Exclaves11AudioBuffer6CreateEPKcy
+ __ZN4ASDT8Exclaves11AudioBufferC1EPKcy
+ __ZN4ASDT8Exclaves11AudioBufferC2EPKcy
+ __ZN4ASDT8Exclaves11AudioBufferD0Ev
+ __ZN4ASDT8Exclaves11AudioBufferD1Ev
+ __ZN4ASDT8Exclaves11AudioBufferD2Ev
+ __ZN4ASDT8Exclaves13InboundBuffer5WriteEPKNS1_6VectorEm
+ __ZN4ASDT8Exclaves13InboundBuffer5WriteEPKhjj
+ __ZN4ASDT8Exclaves13InboundBuffer5WriteEPKhjjjy
+ __ZN4ASDT8Exclaves13InboundBuffer6CreateEPKcy
+ __ZN4ASDT8Exclaves13InboundBufferC1EPKcy
+ __ZN4ASDT8Exclaves13InboundBufferC2EPKcy
+ __ZN4ASDT8Exclaves13InboundBufferD0Ev
+ __ZN4ASDT8Exclaves13InboundBufferD1Ev
+ __ZN4ASDT8Exclaves13InboundBufferD2Ev
+ __ZN4ASDT8Exclaves13StatusTracker14SetSignalBlockEU13block_pointerFvvE
+ __ZN4ASDT8Exclaves13StatusTracker3PopEj
+ __ZN4ASDT8Exclaves13StatusTracker4PushERKNS1_6UpdateE
+ __ZN4ASDT8Exclaves13StatusTracker5ResetEv
+ __ZN4ASDT8Exclaves13StatusTracker6CreateERKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE
+ __ZN4ASDT8Exclaves13StatusTracker7ProcessERNS1_7MessageE
+ __ZN4ASDT8Exclaves13StatusTrackerC1ERKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE
+ __ZN4ASDT8Exclaves13StatusTrackerC2ERKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE
+ __ZN4ASDT8Exclaves13StatusTrackerD0Ev
+ __ZN4ASDT8Exclaves13StatusTrackerD1Ev
+ __ZN4ASDT8Exclaves13StatusTrackerD2Ev
+ __ZN4ASDT8Exclaves6Sensor13ConvertStatusE24exclaves_sensor_status_tRNS1_6StatusEPKc
+ __ZN5caulk10concurrent7messageD2Ev
+ __ZN5caulk10concurrent9messenger20shared_high_priorityEv
+ __ZN5caulk10concurrent9messenger7enqueueERNS0_7messageE
+ __ZN5caulk10concurrent9messengerC1ENS1_15thread_strategyERKNS_6thread10attributesE
+ __ZN5caulk10concurrent9messengerD1Ev
+ __ZNK4ASDT12IOUserClient21GetConnectionRefCountEv
+ __ZNK4ASDT12IOUserClient21GetUserClientRefCountEv
+ __ZNK4ASDT8Exclaves13StatusTracker8GetCountEv
+ __ZTIN4ASDT8Exclaves11AudioBufferE
+ __ZTIN4ASDT8Exclaves13InboundBufferE
+ __ZTIN4ASDT8Exclaves13StatusTrackerE
+ __ZTIN5caulk10concurrent7messageE
+ __ZTSN4ASDT8Exclaves11AudioBufferE
+ __ZTSN4ASDT8Exclaves13InboundBufferE
+ __ZTSN4ASDT8Exclaves13StatusTrackerE
+ __ZTVN10__cxxabiv120__si_class_type_infoE
+ __ZTVN4ASDT8Exclaves11AudioBufferE
+ __ZTVN4ASDT8Exclaves13InboundBufferE
+ __ZTVN4ASDT8Exclaves13StatusTrackerE
+ ___NSArray0__struct
+ _exclaves_audio_buffer_copyout_with_status
+ _exclaves_inbound_buffer_copyin
+ _exclaves_inbound_buffer_create
+ _kASDTExclavesStatusPropertyAddress
+ _kASDTIOThreadCountKey
+ _kASDTIOThreadIsFirstOrWasLast
+ _mach_port_get_refs
+ _objc_retain_x1
+ _os_log_create
+ _task_info
- _OBJC_CLASS_$_ASDTExclavesSensorPMEnabler
- _OBJC_METACLASS_$_ASDTExclavesSensorPMEnabler
- __ZN4ASDT8Exclaves11NamedBuffer4ReadEPNS1_6VectorEm
- __ZN4ASDT8Exclaves11NamedBuffer4ReadEPhjj
- __ZN4ASDT8Exclaves11NamedBuffer4ReadEPhjjjy
- __ZN4ASDT8Exclaves11NamedBuffer6CreateEPKcy
- __ZN4ASDT8Exclaves11NamedBufferC1EPKcy
- __ZN4ASDT8Exclaves11NamedBufferC2EPKcy
- __ZN4ASDT8Exclaves11NamedBufferD0Ev
- __ZN4ASDT8Exclaves11NamedBufferD1Ev
- __ZN4ASDT8Exclaves11NamedBufferD2Ev
- __ZTIN4ASDT8Exclaves11NamedBufferE
- __ZTSN4ASDT8Exclaves11NamedBufferE
- __ZTVN4ASDT8Exclaves11NamedBufferE
- _exclaves_audio_buffer_copyout
- _objc_retain_x24
- _objc_retain_x25
CStrings:
+ "\x04"
+ "%!@(MISSING): PM state transition '%!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING)' failed for %!@(MISSING): %!x(MISSING) '%!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING)'"
+ "%!@(MISSING): Thread context %!u(MISSING) %!s(MISSING) with use case %!u(MISSING), count: %!u(MISSING)"
+ "'"
+ "-[ASDTExclavesStream exclavesWriteMix]_block_invoke"
+ "220.21"
+ "@\"ASDTExclavesSensorManager\""
+ "@\"STMediaStatusDomainMicrophoneRecordingAttribution\""
+ "@\"STMediaStatusDomainPublisher\""
+ "ASDTAudioDevice.mm"
+ "ASDTExclavesSensorAutomaticProperty"
+ "ASDTExclavesSensorManager"
+ "ASDTExclavesSensorManager(%!@(MISSING)): Exclaves sensor creation fails unexpectedly."
+ "ASDTExclavesSensorManager(%!@(MISSING)): Failed to allocate memory."
+ "ASDTExclavesStatusProperty"
+ "ASDTExclavesStatusProperty(%!@(MISSING)): Failed to create sensor manager."
+ "ASDTExclavesStatusProperty: The sensor name must be specified."
+ "ASDTIOThread"
+ "ASDTSystemStatus"
+ "AudioBuffer: Exclaves not available."
+ "AudioBuffer: Failed to create with name: %!s(MISSING), size: %!l(MISSING)lu (%!l(MISSING)lu): %!x(MISSING)"
+ "AudioBuffer::Read: Failed to copyout: name: %!s(MISSING), addr: %!p(MISSING), length1: %!l(MISSING)lu, offset1: %!l(MISSING)lu, length2: %!l(MISSING)lu, offset2: %!l(MISSING)lu, ret: %!x(MISSING)"
+ "Base"
+ "Context ID"
+ "Event"
+ "Failed to allocate self.ioThreads"
+ "Failed to create SystemStatus object."
+ "Failed to create activity attribution."
+ "Failed to create an audit token."
+ "Failed to create recording attribution."
+ "Failed to create system status publisher."
+ "I20@0:8I16"
+ "I24@0:8@16"
+ "IOThread dictionary not empty. Contents: %!@(MISSING)"
+ "IOUserClient: Failed mach_port_get_refs for %!u(MISSING): %!x(MISSING) (%!u(MISSING))"
+ "InboundBuffer: Exclaves not available."
+ "InboundBuffer: Failed to create with name: %!s(MISSING), size: %!l(MISSING)lu (%!l(MISSING)lu): %!x(MISSING)"
+ "InboundBuffer::Write: Failed to copyin: name: %!s(MISSING), addr: %!p(MISSING), length1: %!l(MISSING)lu, offset1: %!l(MISSING)lu, length2: %!l(MISSING)lu, offset2: %!l(MISSING)lu, ret: %!x(MISSING)"
+ "Isolated Use Case"
+ "MockASDTSystemStatus"
+ "Pending"
+ "Sensor: Exclaves not available."
+ "StatusTracker(%!s(MISSING)): %!s(MISSING); time: %!l(MISSING)luns, sample: %!l(MISSING)lu"
+ "StatusTracker(%!s(MISSING)): No messages available to push update for %!s(MISSING) at %!l(MISSING)luns, mat: %!l(MISSING)lu, sample: %!l(MISSING)lu"
+ "SystemStatus is not supported on this system."
+ "T@\"ASDTCondition\",&,N,V_mutex"
+ "T@\"ASDTExclavesSensorManager\",&,N,V_exclavesSensorManager"
+ "T@\"ASDTExclavesSensorManager\",&,N,V_sensorManager"
+ "T@\"NSMutableDictionary\",&,N,V_ioThreads"
+ "T@\"NSMutableSet\",&,N,V_deviceUIDs"
+ "T@\"NSString\",&,N,V_sensorName"
+ "T@\"STMediaStatusDomainMicrophoneRecordingAttribution\",&,N,V_attribution"
+ "T@\"STMediaStatusDomainPublisher\",&,N,V_publisher"
+ "TB,N,V_publishedEnabled"
+ "T^v,R,N"
+ "_attribution"
+ "_audioBuffer"
+ "_deviceUIDs"
+ "_exclavesSensorManager"
+ "_inboundBuffer"
+ "_ioThreads"
+ "_publishedEnabled"
+ "_publisher"
+ "_sensorManager"
+ "_sensorName"
+ "_statusTracker"
+ "addMicrophoneAttribution:"
+ "allocExclavesAudioBuffer:"
+ "asdtIOThreadChangeContextID"
+ "asdtIOThreadChangeEvent"
+ "asdtIOThreadChangeIsolatedUseCase"
+ "asdtIOThreadUseCaseIsFirstOrWasLast"
+ "asdtIOThreadUseCaseThreadCount"
+ "attribution"
+ "attributionWithAuditToken:"
+ "com.apple.AudioServerDriverTransports.SystemStatus"
+ "com.apple.audio.ASDT"
+ "deviceUIDs"
+ "doTerminate"
+ "enabled"
+ "exclavesAudioBuffer"
+ "exclavesInboundBuffer"
+ "exclavesSensorManager"
+ "exclavesWriteMix"
+ "forMic"
+ "forSensorName:"
+ "freeExclavesAudioBuffer"
+ "initWithActivityAttribution:"
+ "initWithSensorName:"
+ "ioReferenceQueue"
+ "ioThreadStartStop:"
+ "ioThreadStateChange:"
+ "ioThreads"
+ "isFirstOrWasLast"
+ "machAbsoluteTime"
+ "mutex"
+ "numberOfIOThreadsForUseCaseID:"
+ "numberOfIOThreadsForUseCaseInDescription:"
+ "operation"
+ "performIOThreadStateChange:"
+ "performTerminate"
+ "publishMicrophoneEnabled:"
+ "publishedEnabled"
+ "publisher"
+ "recordingIsEnabled:forDeviceUID:"
+ "removeMicrophoneAttribution:"
+ "sensor"
+ "sensorManager"
+ "sensorName"
+ "sensorStatusChanged"
+ "setAttribution:"
+ "setDeviceUIDs:"
+ "setExclavesSensorManager:"
+ "setIoThreads:"
+ "setMutex:"
+ "setPublishedEnabled:"
+ "setPublisher:"
+ "setSensorManager:"
+ "setSensorName:"
+ "statusRawValue"
+ "statusTracker"
+ "systemStatus"
+ "timeNanoseconds"
+ "unknown"
+ "updateIOThreadStateChangeDescription:"
+ "updateSensorForIOThreadStateChange:"
+ "updateVolatileDataWithBlock:"
+ "useCaseThreadCount"
+ "usesExclavesAudioBuffer"
+ "v16@?0@\"STMutableMediaStatusDomainData\"8"
+ "v28@0:8B16@20"
+ "{unique_ptr<ASDT::Exclaves::AudioBuffer, std::default_delete<ASDT::Exclaves::AudioBuffer>>=\"__ptr_\"{__compressed_pair<ASDT::Exclaves::AudioBuffer *, std::default_delete<ASDT::Exclaves::AudioBuffer>>=\"__value_\"^{AudioBuffer}}}"
+ "{unique_ptr<ASDT::Exclaves::InboundBuffer, std::default_delete<ASDT::Exclaves::InboundBuffer>>=\"__ptr_\"{__compressed_pair<ASDT::Exclaves::InboundBuffer *, std::default_delete<ASDT::Exclaves::InboundBuffer>>=\"__value_\"^{InboundBuffer}}}"
+ "{unique_ptr<ASDT::Exclaves::StatusTracker, std::default_delete<ASDT::Exclaves::StatusTracker>>=\"__ptr_\"{__compressed_pair<ASDT::Exclaves::StatusTracker *, std::default_delete<ASDT::Exclaves::StatusTracker>>=\"__value_\"^{StatusTracker}}}"
- "%!@(MISSING): Exclaves sensor creation fails unexpectedly."
- "%!@(MISSING): Failed to create sensor."
- "%!@(MISSING): PM state change failed for %!@(MISSING): %!x(MISSING) '%!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING)'"
- "%!@(MISSING): The name of this object must be specified."
- "&"
- "200.54"
- "ASDTExclavesSensorPMEnabler"
- "NamedBuffer: Exclaves not available."
- "NamedBuffer: Failed to create with name: %!s(MISSING), size: %!l(MISSING)lu (%!l(MISSING)lu): %!x(MISSING)"
- "NamedBuffer::Read: Failed to copyout: name: %!s(MISSING), addr: %!p(MISSING), length1: %!l(MISSING)lu, offset1: %!l(MISSING)lu, length2: %!l(MISSING)lu, offset2: %!l(MISSING)lu, ret: %!x(MISSING)"
- "_exclavesBuffer"
- "allocExclavesNamedBuffer:"
- "configForAutoSensorProperty"
- "exclavesBuffer"
- "freeExclavesNamedBuffer"
- "usesExclavesNamedBuffer"
- "{unique_ptr<ASDT::Exclaves::NamedBuffer, std::default_delete<ASDT::Exclaves::NamedBuffer>>=\"__ptr_\"{__compressed_pair<ASDT::Exclaves::NamedBuffer *, std::default_delete<ASDT::Exclaves::NamedBuffer>>=\"__value_\"^{NamedBuffer}}}"

```
