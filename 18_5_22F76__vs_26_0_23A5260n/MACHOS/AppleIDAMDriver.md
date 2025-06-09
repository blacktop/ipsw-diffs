## AppleIDAMDriver

> `/System/Library/Audio/MIDI Drivers/AppleIDAMDriver.plugin/AppleIDAMDriver`

```diff

-315.500.0.0.0
-  __TEXT.__text: 0x1d494
-  __TEXT.__auth_stubs: 0x880
-  __TEXT.__cstring: 0x77f
-  __TEXT.__gcc_except_tab: 0xd38
+319.0.0.0.0
+  __TEXT.__text: 0x1db40
+  __TEXT.__auth_stubs: 0x840
+  __TEXT.__cstring: 0x78b
+  __TEXT.__gcc_except_tab: 0xd94
   __TEXT.__const: 0x260
-  __TEXT.__oslogstring: 0x3963
-  __TEXT.__unwind_info: 0xa68
-  __DATA_CONST.__auth_got: 0x448
+  __TEXT.__oslogstring: 0x3995
+  __TEXT.__unwind_info: 0xac0
+  __DATA_CONST.__auth_got: 0x428
   __DATA_CONST.__got: 0xe0
   __DATA_CONST.__const: 0xb88
   __DATA_CONST.__cfstring: 0x320
-  __DATA.__data: 0x98
+  __DATA.__data: 0x88
   __DATA.__bss: 0x108
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMIDI.framework/CoreMIDI
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/PrivateFrameworks/caulk.framework/caulk
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 530E4D9F-07A2-3B5C-9567-0E94A334DC25
+  UUID: 750825DE-311C-396E-982C-FA76ADE9C480
   Functions: 530
-  Symbols:   173
-  CStrings:  377
+  Symbols:   169
+  CStrings:  378
 
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
