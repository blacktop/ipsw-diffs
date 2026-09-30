## YamahaUSBMIDIDriver

> `/System/Library/Audio/MIDI Drivers/YamahaUSBMIDIDriver.plugin/YamahaUSBMIDIDriver`

```diff

-315.500.0.0.0
-  __TEXT.__text: 0x1f9f8
-  __TEXT.__auth_stubs: 0x840
-  __TEXT.__cstring: 0x797
-  __TEXT.__gcc_except_tab: 0xeec
-  __TEXT.__const: 0x270
-  __TEXT.__oslogstring: 0x3c19
-  __TEXT.__unwind_info: 0xa78
-  __DATA_CONST.__auth_got: 0x428
+319.0.0.0.0
+  __TEXT.__text: 0x1f5f0
+  __TEXT.__auth_stubs: 0x800
+  __TEXT.__cstring: 0x7a3
+  __TEXT.__gcc_except_tab: 0xed0
+  __TEXT.__const: 0x280
+  __TEXT.__oslogstring: 0x3c4b
+  __TEXT.__unwind_info: 0xad0
+  __DATA_CONST.__auth_got: 0x408
   __DATA_CONST.__got: 0xe8
   __DATA_CONST.__const: 0xc60
   __DATA_CONST.__cfstring: 0x360
-  __DATA.__data: 0x98
+  __DATA.__data: 0x88
   __DATA.__bss: 0x101
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMIDI.framework/CoreMIDI
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/PrivateFrameworks/caulk.framework/caulk
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 9F1238A7-A93B-308C-9C6D-35E86D6DCB77
+  UUID: 22210529-53F4-3E2A-8A6E-3FB6F3A5688C
   Functions: 537
-  Symbols:   170
-  CStrings:  375
+  Symbols:   166
+  CStrings:  376
 
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
