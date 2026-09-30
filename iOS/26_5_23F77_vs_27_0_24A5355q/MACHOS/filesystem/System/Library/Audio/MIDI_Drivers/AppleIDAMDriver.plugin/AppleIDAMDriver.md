## AppleIDAMDriver

> `/System/Library/Audio/MIDI Drivers/AppleIDAMDriver.plugin/AppleIDAMDriver`

```diff

-324.501.0.6.0
-  __TEXT.__text: 0x1d1fc sha256:0a8db3e53bd675401fc83d100d4f23b142a2566ca76f7a4f850a73ad51f67580
-  __TEXT.__auth_stubs: 0x840 sha256:ab27711838f25c0e37312b829556daa312a02b0e3dfa2d7168c8785c18f3df79
-  __TEXT.__cstring: 0x7a9 sha256:12ff6392ca0c5717623fe77edf5fd297733a240213418f7ca09476ef7ebf2741
-  __TEXT.__gcc_except_tab: 0xd78 sha256:7ee84be77926787919c0426ab1f7512131ba2306fde446d573b108e4c9187342
-  __TEXT.__const: 0x260 sha256:f2dbf7a393d96417dced042fab1377e09a9dcf41cb5393f0203ee9feb7bfedc2
+328.0.0.0.0
+  __TEXT.__text: 0x1c674 sha256:3b80257dc962525fa53104593e008358eaa64d48450500739033bd88959a52b2
+  __TEXT.__realtime: 0x4c8 sha256:8a9189acad9341bd2133ccc9ec7a641226049384d57d5bf4e117f9a002aecb25
+  __TEXT.__auth_stubs: 0x790 sha256:e454321e40ce0d5709e75da2ff32a7c96b8990970ebe2f95d1ce5fc9d43606d6
+  __TEXT.__const: 0x290 sha256:9e6eaf847757d1c869ed55dca8890e29ebfe2a42ce4c8010a27620bd18806bb7
+  __TEXT.__gcc_except_tab: 0xc60 sha256:7d32382228873640163ced6f51021bb0d62830fa3a13182be257b32c1cb7aa1c
   __TEXT.__oslogstring: 0x39c8 sha256:61262057c9e2516322a8ea002ff23c0663ee5635c4d3bc33a93788f01a174880
-  __TEXT.__unwind_info: 0xab8 sha256:333cc4ec15447a5635e867a8716438cf49c786c30d1c5c52e9d7c69c6b04bc72
-  __DATA_CONST.__auth_got: 0x428 sha256:17fa0c2f6637e850a05de58bee936c08b3222e6a21f8b919ccb27420ac5839dd
-  __DATA_CONST.__got: 0xe0 sha256:5b14a73a4f48fc53b5666438528fa5749a56669c02208faff73870fbadb63d81
-  __DATA_CONST.__const: 0xbb8 sha256:89d3c18041f9bfd305f99add8c60cebe5da15798e3041005f0ea43c5bdd0a3fa
-  __DATA_CONST.__cfstring: 0x320 sha256:8da3307e3e030281a4746ba8b2663c47d3952cec949afc5a1d1e80a3de4a3641
-  __DATA.__data: 0x98 sha256:c627730049d7860940d1b38c7882dba9880ce2d45b7e6cc55fef612b58730c51
-  __DATA.__bss: 0x110 sha256:e4d879a3407de578f579dfab4366fcea75a6649c683d9efe4f056f6505437574
+  __TEXT.__cstring: 0x22c0 sha256:6374b30c3b311278644fc8c7640bfc9e9ebbdcba1aa1e827e0626b3f5b2c35c8
+  __TEXT.__unwind_info: 0xa80 sha256:fa61d98880ce80b5f93e620b598264ee044eb68d19e30a3b9bc7ece051eaaeff
+  __DATA_CONST.__const: 0xb60 sha256:e2a271706911bd7a590e37800e4377e39b386ba86af0a187942b4575ecc13994
+  __DATA_CONST.__cfstring: 0x320 sha256:ed29519e3f9cccc56b7c983b06be7e336028506527d575c0f3480cbf98cec3cb
+  __DATA_CONST.__auth_got: 0x3d0 sha256:5e7b1d75be2f3ca435152a7e54462abd4cc1e5888c5b1becd266cd96de64d1e5
+  __DATA_CONST.__got: 0xc8 sha256:44f69db6e414d733895b05031366b4e35accc9c37b47c69fe1bb0cb481b7d572
+  __DATA.__data: 0x98 sha256:bb93a8c22bbe00f2e7c0371964a65bb0204441784249a173b7da16bf38e7bce7
+  __DATA.__bss: 0xa0 sha256:b393978842a0fa3d3e1470196f098f473f9678e72463cb65ec4ab5581856c2e4
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMIDI.framework/CoreMIDI
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/caulk.framework/caulk
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 076DA212-F8E0-3314-816F-C44FDD58B7A6
-  Functions: 548
-  Symbols:   169
-  CStrings:  379
+  UUID: 89749E7B-D4C2-3ADC-88F9-17EF6F1A7C60
+  Functions: 533
+  Symbols:   154
+  CStrings:  403
 
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
- _CFGetTypeID
- _CFNumberGetTypeID
- _CFNumberGetValue
- _CFPreferencesCopyAppValue
- _CFPreferencesSynchronize
- _CFSetAddValue
- _CFSetApplyFunction
- _CFSetCreateMutable
- _CFStringGetCString
- _CFStringGetTypeID
- __ZTVN10__cxxabiv121__vmi_class_type_infoE
- ___cxa_guard_abort
- ___tolower
- __dispatch_source_type_signal
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
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/array:271: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/array:275: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
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

```
