## CoreAudio

> `/System/Library/Frameworks/CoreAudio.framework/CoreAudio`

```diff

-328.400.0.0.0
-  __TEXT.__text: 0x522e70
-  __TEXT.__auth_stubs: 0x2b30
-  __TEXT.__objc_methlist: 0xf94
-  __TEXT.__gcc_except_tab: 0x57fd4
-  __TEXT.__const: 0x4ce58
-  __TEXT.__oslogstring: 0x3c3fd
-  __TEXT.__cstring: 0x2ae0d
-  __TEXT.__unwind_info: 0x180b0
+328.522.0.0.0
+  __TEXT.__text: 0x5087e0
+  __TEXT.__auth_stubs: 0x2b40
+  __TEXT.__objc_methlist: 0x1384
+  __TEXT.__const: 0x4cf78
+  __TEXT.__gcc_except_tab: 0x57c04
+  __TEXT.__oslogstring: 0x3c71b
+  __TEXT.__cstring: 0x2ae36
+  __TEXT.__unwind_info: 0x17d88
+  __TEXT.__eh_frame: 0x68
   __TEXT.__objc_classname: 0x352
   __TEXT.__objc_methname: 0x38d7
-  __TEXT.__objc_methtype: 0x3cc3
+  __TEXT.__objc_methtype: 0x3cb3
   __TEXT.__objc_stubs: 0x1e60
-  __DATA_CONST.__got: 0x460
-  __DATA_CONST.__const: 0x6418
+  __DATA_CONST.__got: 0x428
+  __DATA_CONST.__const: 0x6480
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9c0
+  __DATA_CONST.__objc_selrefs: 0xa58
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x60
-  __AUTH_CONST.__auth_got: 0x15a8
-  __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x2f1d8
+  __AUTH_CONST.__auth_got: 0x15b0
+  __AUTH_CONST.__auth_ptr: 0x58
+  __AUTH_CONST.__const: 0x2f3a8
   __AUTH_CONST.__cfstring: 0x3860
-  __AUTH_CONST.__objc_const: 0x2738
+  __AUTH_CONST.__objc_const: 0x2018
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x118
   __DATA.__data: 0x760
-  __DATA.__bss: 0x1eb0
+  __DATA.__bss: 0x1ea0
   __DATA_DIRTY.__objc_data: 0x5a0
   __DATA_DIRTY.__data: 0x230
-  __DATA_DIRTY.__bss: 0x1480
+  __DATA_DIRTY.__bss: 0x1490
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 17639
-  Symbols:   19063
-  CStrings:  7203
+  Functions: 17417
+  Symbols:   19130
+  CStrings:  7216
 
Symbols:
+ __ZN5caulk15deferred_logger8create_vEPv
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTINSt3__117bad_function_callE
+ __ZTVNSt3__117bad_function_callE
- __ZNKSt9exception4whatEv
CStrings:
+ "%25s:%-5d    Object ID: %4d | Class: '%s' | Base Class: '%s' | Ref: %4llu"
+ "%25s:%-5d  AudioDeviceDuck(%lu, %f, [%.0f, %llu], %f)"
+ "%25s:%-5d  Device %u starting IO.\n"
+ "%25s:%-5d  Device %u stopping IO.\n"
+ "%25s:%-5d  HALS_BufferFactory::allocate_shared_buffer: [%u] threw exception from HALB_IOBufferManager_Server.Allocate()"
+ "%25s:%-5d  HALS_Device::ClearAllDucking: client %u (pid %d) unducking on device %s (%u)"
+ "%25s:%-5d  HALS_IOContextDescription::SetFromCFRepresentation_ProcessInputStreams: Turning on drift correction for tap: %s [IOC: %u]"
+ "%25s:%-5d  HALS_IOEngine2::PauseAllContexts: still waiting after %u seconds"
+ "%25s:%-5d  HALS_IOEngine2::ResumeAllContexts: still waiting after %u seconds"
+ "%25s:%-5d  HALS_IOProcessorFactoryWorker::do_allocate_processor: sample rate conversion no longer enables drift correction by default [IOC: %u]"
+ "%25s:%-5d  HALthreadID: %llX, start: %llu, wake: %llu, (continuous - absolute): %llu\n"
+ "%25s:%-5d  [hal_dsp][offloads] (Client ID: %u) (Device ID: %u) Offloads are available, but this device will not offload -> %s"
+ "%25s:%-5d  [hal_dsp][offloads] (Client ID: %u) (Device ID: %u) This device will not offload -> %s"
+ "%25s:%-5d  err = %d calling AudioIssueDetectorClientUpdateReportingSessions, mDetectorID = %lld"
+ "%6u %32s:%-5d \t\tHALS_IOEngine2::_StartIO(%u) succeeded on Context %u  new state: Prewarm: %llu Play: %llu State: %s"
+ "%6u %32s:%-5d %s replacer engine object is null for UID %s"
+ "%6u %32s:%-5d %s replacer engine property is not supported"
+ "%6u %32s:%-5d %s replacer engine uid is null"
+ "%6u %32s:%-5d %s the engine replacer device %s is not yet active"
+ "%6u %32s:%-5d +++++> Beginning handling of properties changed for source object, %u"
+ "%6u %32s:%-5d <+++++ Done handling of properties changed for source object, %u"
+ "%6u %32s:%-5d >>> HALS_IOEngine2::_StartIO(%u) called on Context %u  current state: Prewarm: %llu Play: %llu State: %s"
+ "%6u %32s:%-5d AllowNegotiateAdaptInSetComposition: useCaseID = %d, isServerBuild = %s, isIsolatedUseCase = %s, isSharedDsp = %s, istvos = %s, adaptNow = %s"
+ "%6u %32s:%-5d Assertion Failed: %s a required property is missing '%s':%u:%u"
+ "%6u %32s:%-5d AudioDeviceDuck %lu, %f, [%.0f, %llu], %f"
+ "%6u %32s:%-5d Caught exception performing config change %i"
+ "%6u %32s:%-5d Context ADM Adapt results in %s"
+ "%6u %32s:%-5d Context(%u): %u Thread can play: %d, m_can_play_during_notification_wake: %d, m_can_play_during_dark_wake: %d"
+ "%6u %32s:%-5d Context(%u): IO_Thread_Realtime: parked for sleeping"
+ "%6u %32s:%-5d Detected possible coloring mixer glitch on %{public}s: buffer time: %.0f  actual time: %.0f  safety violation: %.0lf  with %u running contexts"
+ "%6u %32s:%-5d Device '%{public}s' has a engine replacer '%{public}s', forwarding volume ducking command"
+ "%6u %32s:%-5d HALS_IOEngine2::_StartIO(%u): play state has not changed on Context %u"
+ "%6u %32s:%-5d HALS_IOEngine2::_StartIO: Caught exception while starting IO on Context %u  result: %d"
+ "%6u %32s:%-5d HALS_IOEngine2::_StartIO: _AllocateTempBuffers on Context %u  returned error: %d"
+ "%6u %32s:%-5d HALS_IOEngine2::_StartIO: _TellHardwareToStart on Context %u  returned error: 0x%X"
+ "%6u %32s:%-5d HALS_IOEngine2::_StopIO(%u) called on Context %u  current state: Prewarm: %llu Play: %llu State: %s"
+ "%6u %32s:%-5d HALS_System::_CreateTap(%s) -> %u"
+ "%6u %32s:%-5d HALS_System::_DestroyTap(%u)"
+ "%6u %32s:%-5d IOContext_Core(%u|\"%s\")::pause: current(%s)  pause_count(%d)"
+ "%6u %32s:%-5d IOContext_Core(%u|\"%s\")::resume: current(%s)  pause_count(%d)"
+ "%6u %32s:%-5d IOContext_Core(%u|\"%s\")::start: request(%s)  current(%s)  pause_count(%d)"
+ "%6u %32s:%-5d IOContext_Core(%u|\"%s\")::stop: request(%s)  current(%s)  pause_count(%d)"
+ "%6u %32s:%-5d IO_Thread_Realtime(%u)::end"
+ "%6u %32s:%-5d IO_Thread_Realtime(%u)::start"
+ "%6u %32s:%-5d Manifest_Queue(%u|\"%s\")::enqueue_manifest: size(%zu)  %s -> %s  (snapshot: %zu)"
+ "%6u %32s:%-5d New replacer device %u, clear the cached replacer device state '%{public}s' %u"
+ "%6u %32s:%-5d Switching to realtime - end of next buffer: %0.f  last valid: %0.f  wakeTime: %0.f  next buffer host: %lld  wake host: %llu"
+ "%6u %32s:%-5d Throwing Exception: %s AMCP::Utility::Thread_Utilities::configure_thread_for_realtime - thread_policy_set failed. \tCycle Size: %llu \tThread Parameters: \t%u \t%u \t%u \t%u"
+ "%6u %32s:%-5d Throwing Exception: %s Failed to register io thread %i"
+ "%6u %32s:%-5d Throwing Exception: %s Failed to set properties changed async callback %i"
+ "%6u %32s:%-5d Throwing Exception: %s Failed to set request config change async callback %i"
+ "%6u %32s:%-5d Throwing Exception: %s Failed to start device %i"
+ "%6u %32s:%-5d Throwing Exception: %s Failed to start io thread %i"
+ "%6u %32s:%-5d Throwing Exception: %s Failed to stop device %i"
+ "%6u %32s:%-5d Throwing Exception: %s Failed to unregister io thread %i"
+ "%6u %32s:%-5d Throwing Exception: %s Index out of bounds - index: %s  size: %zu"
+ "%6u %32s:%-5d Throwing Exception: %s Index out of bounds - index: %zu  size: %zu"
+ "%6u %32s:%-5d Throwing Exception: %s Missing terminal for connection in when building manifest - index: %s  terminals: %zu"
+ "%6u %32s:%-5d Throwing Exception: %s Synchronizer::receive_data on unanchored source: %u  '%s'"
+ "%6u %32s:%-5d Throwing Exception: %s failed to open connection %i"
+ "%6u %32s:%-5d Throwing Exception: %s range too large for ring buffer: range size: %lld  ring buffer size: %lld"
+ "%6u %32s:%-5d [hal_dsp] %p (Context ID: %lu) (Client ID: %lu) (Device ID: %lu (%lu)) Sent Hosted DSP change notification sel:%s scope:%s el:%u"
+ "%6u %32s:%-5d [hal_dsp] %u streams with DSP adapted."
+ "%6u %32s:%-5d [hal_dsp] Adapting a new buffer size %u."
+ "%6u %32s:%-5d [hal_dsp] Negotiate/Adapt during context configuration is %sALLOWED."
+ "%6u %32s:%-5d [hal_dsp] Start DSP - (%u) Refresh/notify client due to DSP-related %s change."
+ "%6u %32s:%-5d [hal_dsp][graph] kAudioDevicePropertyDSPGraphParameter from setHostedDSPProperty scope:%s el:%u err:%s"
+ "AMCP::Utility::Thread_Utilities::configure_thread_for_realtime - thread_policy_set failed. \tCycle Size: %llu \tThread Parameters: \t%u \t%u \t%u \t%u"
+ "API Usage Reporting Queue"
+ "Index out of bounds - index: %s  size: %zu"
+ "Index out of bounds - index: %zu  size: %zu"
+ "Missing terminal for connection in when building manifest - index: %s  terminals: %zu"
+ "NOT "
+ "Synchronizer::receive_data on unanchored source: %u  '%s'"
+ "TapClient"
+ "range too large for ring buffer: range size: %lld  ring buffer size: %lld"
+ "{optional<std::string>=(?=c{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}})B}32@0:8Q16@24"
- "%25s:%-5d    Object ID: %4d | Class: '%s' | Base Class: '%s' | Ref: %4lld"
- "%25s:%-5d  AudioDeviceDuck(%lu, %f, [%.0f, %lld], %f)"
- "%25s:%-5d  Device %d starting IO.\n"
- "%25s:%-5d  Device %d stopping IO.\n"
- "%25s:%-5d  HALS_BufferFactory::allocate_shared_buffer: [%d] threw exception from HALB_IOBufferManager_Server.Allocate()"
- "%25s:%-5d  HALS_IOContextDescription::SetFromCFRepresentation_ProcessInputStreams: Turning on drift correction for tap: %s [IOC: %d]"
- "%25s:%-5d  HALS_IOEngine2::PauseAllContexts: still waiting after %d seconds"
- "%25s:%-5d  HALS_IOEngine2::ResumeAllContexts: still waiting after %d seconds"
- "%25s:%-5d  HALS_IOProcessorFactoryWorker::do_allocate_processor: sample rate conversion no longer enables drift correction by default [IOC: %d]"
- "%25s:%-5d  HALthreadID: %llX, start: %llu, wake: %llu, (continuous - absolute): %lld\n"
- "%25s:%-5d  [hal_dsp][offloads] (Client ID: %d) (Device ID: %d) Offloads are available, but this device will not offload -> %s"
- "%25s:%-5d  [hal_dsp][offloads] (Client ID: %d) (Device ID: %d) This device will not offload -> %s"
- "%25s:%-5d  err = %d calling AudioIssueDetectorClientUpdateReportingSessions, mDetectorID = %llu"
- "%6u %32s:%-5d \t\tHALS_IOEngine2::_StartIO(%d) succeeded on Context %d  new state: Prewarm: %llu Play: %llu State: %s"
- "%6u %32s:%-5d +++++> Beginning handling of properties changed for source object, %d"
- "%6u %32s:%-5d <+++++ Done handling of properties changed for source object, %d"
- "%6u %32s:%-5d >>> HALS_IOEngine2::_StartIO(%d) called on Context %d  current state: Prewarm: %llu Play: %llu State: %s"
- "%6u %32s:%-5d Assertion Failed: %s a required property is missing '%s':%d:%d"
- "%6u %32s:%-5d AudioDeviceDuck %lu, %f, [%.0f, %lld], %f"
- "%6u %32s:%-5d Caught exception performing config change %u"
- "%6u %32s:%-5d Context(%d): %d Thread can play: %d, m_can_play_during_notification_wake: %d, m_can_play_during_dark_wake: %d"
- "%6u %32s:%-5d Context(%d): IO_Thread_Realtime: parked for sleeping"
- "%6u %32s:%-5d Detected possible coloring mixer glitch on %{public}s: buffer time: %.0f  actual time: %.0f  safety violation: %.0lf  with %d running contexts"
- "%6u %32s:%-5d HALS_IOEngine2::_StartIO(%d): play state has not changed on Context %d"
- "%6u %32s:%-5d HALS_IOEngine2::_StartIO: Caught exception while starting IO on Context %d  result: %d"
- "%6u %32s:%-5d HALS_IOEngine2::_StartIO: _AllocateTempBuffers on Context %d  returned error: %d"
- "%6u %32s:%-5d HALS_IOEngine2::_StartIO: _TellHardwareToStart on Context %d  returned error: 0x%X"
- "%6u %32s:%-5d HALS_IOEngine2::_StopIO(%d) called on Context %d  current state: Prewarm: %llu Play: %llu State: %s"
- "%6u %32s:%-5d HALS_System::_CreateTap(%s) -> %d"
- "%6u %32s:%-5d HALS_System::_DestroyTap(%d)"
- "%6u %32s:%-5d IOContext_Core(%d|\"%s\")::pause: current(%s)  pause_count(%d)"
- "%6u %32s:%-5d IOContext_Core(%d|\"%s\")::resume: current(%s)  pause_count(%d)"
- "%6u %32s:%-5d IOContext_Core(%d|\"%s\")::start: request(%s)  current(%s)  pause_count(%d)"
- "%6u %32s:%-5d IOContext_Core(%d|\"%s\")::stop: request(%s)  current(%s)  pause_count(%d)"
- "%6u %32s:%-5d IO_Thread_Realtime(%d)::end"
- "%6u %32s:%-5d IO_Thread_Realtime(%d)::start"
- "%6u %32s:%-5d Manifest_Queue(%d|\"%s\")::enqueue_manifest: size(%zu)  %s -> %s  (snapshot: %zu)"
- "%6u %32s:%-5d Switching to realtime - end of next buffer: %0.f  last valid: %0.f  wakeTime: %0.f  next buffer host: %llu  wake host: %llu"
- "%6u %32s:%-5d Throwing Exception: %s AMCP::Utility::Thread_Utilities::configure_thread_for_realtime - thread_policy_set failed. \tCycle Size: %llu \tThread Parameters: \t%u \t%u \t%u \t%d"
- "%6u %32s:%-5d Throwing Exception: %s Failed to register io thread %u"
- "%6u %32s:%-5d Throwing Exception: %s Failed to set properties changed async callback %u"
- "%6u %32s:%-5d Throwing Exception: %s Failed to set request config change async callback %u"
- "%6u %32s:%-5d Throwing Exception: %s Failed to start device %u"
- "%6u %32s:%-5d Throwing Exception: %s Failed to start io thread %u"
- "%6u %32s:%-5d Throwing Exception: %s Failed to stop device %u"
- "%6u %32s:%-5d Throwing Exception: %s Failed to unregister io thread %u"
- "%6u %32s:%-5d Throwing Exception: %s Index out of bounds - index: %ld  size: %ld"
- "%6u %32s:%-5d Throwing Exception: %s Index out of bounds - index: %s  size: %ld"
- "%6u %32s:%-5d Throwing Exception: %s Missing terminal for connection in when building manifest - index: %s  terminals: %ld"
- "%6u %32s:%-5d Throwing Exception: %s Synchronizer::receive_data on unanchored source: %d  '%s'"
- "%6u %32s:%-5d Throwing Exception: %s failed to open connection %u"
- "%6u %32s:%-5d Throwing Exception: %s range too large for ring buffer: range size: %llu  ring buffer size: %llu"
- "%6u %32s:%-5d [hal_dsp] %d streams with DSP adapted."
- "%6u %32s:%-5d [hal_dsp] %p (Context ID: %lu) (Client ID: %lu) (Device ID: %lu (%lu)) Sent Hosted DSP change notification sel:%s scope:%s el:%d"
- "%6u %32s:%-5d [hal_dsp] Adapting a new buffer size %d."
- "%6u %32s:%-5d [hal_dsp] Start DSP - (%d) Refresh/notify client due to DSP-related %s change."
- "%6u %32s:%-5d [hal_dsp][graph] kAudioDevicePropertyDSPGraphParameter from setHostedDSPProperty scope:%s el:%d err:%s"
- "AMCP::Utility::Thread_Utilities::configure_thread_for_realtime - thread_policy_set failed. \tCycle Size: %llu \tThread Parameters: \t%u \t%u \t%u \t%d"
- "Index out of bounds - index: %ld  size: %ld"
- "Index out of bounds - index: %s  size: %ld"
- "Missing terminal for connection in when building manifest - index: %s  terminals: %ld"
- "Synchronizer::receive_data on unanchored source: %d  '%s'"
- "range too large for ring buffer: range size: %llu  ring buffer size: %llu"
- "{optional<std::string>=(?=c{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}})B}32@0:8Q16@24"

```
