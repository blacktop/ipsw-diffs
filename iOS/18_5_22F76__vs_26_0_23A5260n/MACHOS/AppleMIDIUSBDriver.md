## AppleMIDIUSBDriver

> `/System/Library/Audio/MIDI Drivers/AppleMIDIUSBDriver.plugin/AppleMIDIUSBDriver`

```diff

-315.500.0.0.0
-  __TEXT.__text: 0x20140
-  __TEXT.__auth_stubs: 0x850
-  __TEXT.__gcc_except_tab: 0xee4
-  __TEXT.__cstring: 0x844
-  __TEXT.__const: 0x272
-  __TEXT.__oslogstring: 0x4366
-  __TEXT.__unwind_info: 0xac8
-  __DATA_CONST.__auth_got: 0x430
+319.0.0.0.0
+  __TEXT.__text: 0x20618
+  __TEXT.__auth_stubs: 0x810
+  __TEXT.__gcc_except_tab: 0xf0c
+  __TEXT.__cstring: 0x850
+  __TEXT.__const: 0x282
+  __TEXT.__oslogstring: 0x4398
+  __TEXT.__unwind_info: 0xb30
+  __DATA_CONST.__auth_got: 0x410
   __DATA_CONST.__got: 0xf0
   __DATA_CONST.__const: 0xc78
   __DATA_CONST.__cfstring: 0x3e0
-  __DATA.__data: 0xb0
+  __DATA.__data: 0xa0
   __DATA.__bss: 0x138
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMIDI.framework/CoreMIDI
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/PrivateFrameworks/caulk.framework/caulk
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 7121192C-F455-3FFD-9D66-3AE23C5C75D6
-  Functions: 561
-  Symbols:   172
-  CStrings:  414
+  UUID: 76684CE2-5726-30DA-B20A-BEA7CF057057
+  Functions: 562
+  Symbols:   168
+  CStrings:  415
 
Symbols:
- __Znwm
- __os_log_error_impl
- _memset
- _strlen
CStrings:
+ "%25s:%-5d  CAMutex::CAMutex: Could not init the mutex"
+ "%25s:%-5d  CAMutex::Lock: Could not lock the mutex"
+ "%25s:%-5d  CAMutex::Try: call to pthread_mutex_trylock failed, Error: %d (%s)"
+ "%25s:%-5d  CAMutex::Unlock: A thread is attempting to unlock a Mutex it doesn't own"
+ "%25s:%-5d  CAMutex::Unlock: Could not unlock the mutex"
+ "CAMutex.cpp"
- " CAMutex::CAMutex: Could not init the mutex"
- " CAMutex::Lock: Could not lock the mutex"
- " CAMutex::Try: call to pthread_mutex_trylock failed, Error: %d (%s)"
- " CAMutex::Unlock: A thread is attempting to unlock a Mutex it doesn't own"
- " CAMutex::Unlock: Could not unlock the mutex"

```
