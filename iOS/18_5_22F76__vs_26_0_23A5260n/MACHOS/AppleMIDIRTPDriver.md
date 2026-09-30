## AppleMIDIRTPDriver

> `/System/Library/Audio/MIDI Drivers/AppleMIDIRTPDriver.plugin/AppleMIDIRTPDriver`

```diff

-315.500.0.0.0
-  __TEXT.__text: 0x14238
-  __TEXT.__auth_stubs: 0xab0
-  __TEXT.__cstring: 0x6e7
-  __TEXT.__gcc_except_tab: 0x10c8
-  __TEXT.__const: 0x250
-  __TEXT.__oslogstring: 0x676
-  __TEXT.__unwind_info: 0x730
-  __DATA_CONST.__auth_got: 0x560
-  __DATA_CONST.__got: 0xc8
-  __DATA_CONST.__const: 0x798
-  __DATA_CONST.__cfstring: 0x380
-  __DATA.__data: 0x88
+319.0.0.0.0
+  __TEXT.__text: 0x145b8
+  __TEXT.__auth_stubs: 0xac0
+  __TEXT.__cstring: 0x7d9
+  __TEXT.__gcc_except_tab: 0x12c8
+  __TEXT.__const: 0x260
+  __TEXT.__oslogstring: 0x638
+  __TEXT.__unwind_info: 0x7b0
+  __DATA_CONST.__auth_got: 0x568
+  __DATA_CONST.__got: 0xd0
+  __DATA_CONST.__const: 0x680
+  __DATA_CONST.__cfstring: 0x400
+  __DATA.__data: 0x78
   __DATA.__common: 0x38
   __DATA.__bss: 0x18
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMIDI.framework/CoreMIDI
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
+  - /System/Library/PrivateFrameworks/caulk.framework/caulk
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 13A20796-FDCF-300C-8560-6A66D03E97A6
-  Functions: 304
-  Symbols:   205
-  CStrings:  139
+  UUID: 9BE8F00A-EA6D-34B9-AEA8-76A26398F14D
+  Functions: 282
+  Symbols:   207
+  CStrings:  151
 
Symbols:
+ _CAVerboseAbort
+ _CFArrayGetTypeID
+ __ZNSt13runtime_errorC1EPKc
+ __ZNSt13runtime_errorD1Ev
- __Znwm
- __os_log_error_impl
CStrings:
+ "%25s:%-5d  CAMutex::CAMutex: Could not init the mutex"
+ "%25s:%-5d  CAMutex::Lock: Could not lock the mutex"
+ "%25s:%-5d  CAMutex::Try: call to pthread_mutex_trylock failed, Error: %d (%s)"
+ "%25s:%-5d  CAMutex::Unlock: A thread is attempting to unlock a Mutex it doesn't own"
+ "%25s:%-5d  CAMutex::Unlock: Could not unlock the mutex"
+ "%25s:%-5d  CAPThread::Start: A thread could not be created in the detached state."
+ "%25s:%-5d  CAPThread::Start: Could not create a thread."
+ "%25s:%-5d  CAPThread::Start: Thread attributes could not be created."
+ "CAMutex.cpp"
+ "CAPThread.cpp"
+ "CAPThread::SetTimeConstraints: thread_policy_set failed, Error: %d (%s)"
+ "CAPThread::Start: can't start because the thread is already running"
+ "Could not construct"
+ "Could not find item"
+ "GSL: Precondition failure at /Library/Caches/com.apple.xbs/Sources/CoreMIDI_Drivers/Source/MIDI/CppSPI/EventList.h: 76"
+ "connected"
+ "initialized"
+ "running"
+ "state"
- " CAMutex::CAMutex: Could not init the mutex"
- " CAMutex::Lock: Could not lock the mutex"
- " CAMutex::Try: call to pthread_mutex_trylock failed, Error: %d (%s)"
- " CAMutex::Unlock: A thread is attempting to unlock a Mutex it doesn't own"
- " CAMutex::Unlock: Could not unlock the mutex"
- " CAPThread::SetTimeConstraints: thread_policy_set failed, Error: %d (%s)"
- " CAPThread::Start: A thread could not be created in the detached state."
- " CAPThread::Start: Could not create a thread."
- " CAPThread::Start: Thread attributes could not be created."
- " CAPThread::Start: can't start because the thread is already running"
- "GSL: Precondition failure at /Library/Caches/com.apple.xbs/Sources/CoreMIDI_Drivers/Source/MIDI/CppSPI/EventList.h: 74"

```
