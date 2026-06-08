## YamahaUSBMIDIDriver

> `/System/Library/Audio/MIDI Drivers/YamahaUSBMIDIDriver.plugin/YamahaUSBMIDIDriver`

```diff

-324.501.0.6.0
-  __TEXT.__text: 0x1ee30
-  __TEXT.__auth_stubs: 0x800
-  __TEXT.__cstring: 0x7c1
-  __TEXT.__gcc_except_tab: 0xeac
-  __TEXT.__const: 0x280
+328.0.0.0.0
+  __TEXT.__text: 0x1e5a4
+  __TEXT.__realtime: 0x4c8
+  __TEXT.__auth_stubs: 0x770
+  __TEXT.__const: 0x290
+  __TEXT.__cstring: 0x282d
+  __TEXT.__gcc_except_tab: 0xda4
   __TEXT.__oslogstring: 0x3c7e
-  __TEXT.__unwind_info: 0xac0
-  __DATA_CONST.__auth_got: 0x408
-  __DATA_CONST.__got: 0xe8
-  __DATA_CONST.__const: 0xca0
+  __TEXT.__unwind_info: 0xa98
+  __DATA_CONST.__const: 0xc48
   __DATA_CONST.__cfstring: 0x360
+  __DATA_CONST.__auth_got: 0x3c0
+  __DATA_CONST.__got: 0xc8
   __DATA.__data: 0x98
-  __DATA.__bss: 0x109
+  __DATA.__bss: 0x99
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMIDI.framework/CoreMIDI
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/caulk.framework/caulk
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 4628E235-A3B5-3C10-ACC1-E986AD0D3190
-  Functions: 554
-  Symbols:   166
-  CStrings:  377
+  UUID: 33D4622A-9812-327B-BCDB-396F5C556D64
+  Functions: 545
+  Symbols:   152
+  CStrings:  404
 
Symbols:
+ __ZN5caulk14cf_preferences14interpret_boolEPKv
+ __ZN5caulk14cf_preferences15interpret_int64EPKv
+ __ZN5caulk14cf_preferences7monitor12_add_handlerEPK10__CFStringS4_ONSt3__18functionIFbPKvEEE
+ __ZN5caulk14cf_preferences7monitor8instanceEv
+ __ZNSt3__112system_errorC1EiRKNS_14error_categoryE
+ __ZNSt3__112system_errorD1Ev
+ __ZNSt3__115system_categoryEv
+ __ZNSt3__132__internal_log_hardening_failureEPKc
- _CFBooleanGetTypeID
- _CFBooleanGetValue
- _CFPreferencesCopyAppValue
- _CFPreferencesSynchronize
- _CFSetAddValue
- _CFSetApplyFunction
- _CFSetCreateMutable
- _CFStringGetCString
- _CFStringGetTypeID
- __NSConcreteStackBlock
- __ZTVN10__cxxabiv121__vmi_class_type_infoE
- ___cxa_guard_abort
- ___tolower
- __dispatch_source_type_signal
- _dispatch_get_global_queue
- _dispatch_resume
- _dispatch_source_create
- _dispatch_source_set_event_handler
- _kCFPreferencesCurrentHost
- _kCFPreferencesCurrentUser
- _kCFTypeSetCallBacks
- _sscanf
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/__ranges/view_interface.h:122: libc++ Hardening assertion !empty() failed: Precondition `!empty()` not satisfied. `.front()` called on an empty view.\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/__ranges/view_interface.h:140: libc++ Hardening assertion !empty() failed: Precondition `!empty()` not satisfied. `.back()` called on an empty view.\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/array:271: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/array:275: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/deque:1522: libc++ Hardening assertion __i < size() failed: deque::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/deque:2296: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/list:1420: libc++ Hardening assertion __p != end() failed: list::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/span:512: libc++ Hardening assertion __offset <= size() failed: span<T>::subspan(offset, count): offset out of range\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/span:525: libc++ Hardening assertion __idx < size() failed: span<T>::operator[](index): index out of range\n"
+ "PartialUMP"
+ "buffer.size() % sizeof(word_t) == 0"
+ "fill_up"
+ "partial_ump.size() < 4"
+ "ump_span.h"
+ "ump_span_impl"
+ "words.size() <= mWords.size() - mSize"
- "%d"
- "CAException"
- "v8@?0"

```
