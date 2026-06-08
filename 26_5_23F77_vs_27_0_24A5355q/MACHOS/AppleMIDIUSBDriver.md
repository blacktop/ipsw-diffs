## AppleMIDIUSBDriver

> `/System/Library/Audio/MIDI Drivers/AppleMIDIUSBDriver.plugin/AppleMIDIUSBDriver`

```diff

-324.501.0.6.0
-  __TEXT.__text: 0x1fecc sha256:dafb7a7f5156cc7a91e74a23ac2b7d9b6169760a7586d0c34abaaec8af935c0e
-  __TEXT.__auth_stubs: 0x810 sha256:bce31e902eaa45dab8a6471630c2f90fa0e83b801fe88fdc682436887b885100
-  __TEXT.__gcc_except_tab: 0xee8 sha256:b10901fe7c6130be1573260828fbcd5bc6fb3a3b0fd0315ce6b15abbaa0f7027
-  __TEXT.__cstring: 0x86e sha256:19a94f65b66a6611659ef4f1e16ee6c8a50bec347efd71a166ac4b51ff55f722
-  __TEXT.__const: 0x282 sha256:a464a559dca575229ac514e0611ac159a5dba71873bad5a828a17d4273431652
+328.0.0.0.0
+  __TEXT.__text: 0x1f534 sha256:cec5e7ee45d0e2595e466921dbffd482f6f8eb6fcee10a94751b0792599aebed
+  __TEXT.__realtime: 0x4c8 sha256:822662b8cf0e8bd6483ffe43b66cf44d16383052397a371f6b87d92cf5308fe8
+  __TEXT.__auth_stubs: 0x780 sha256:e0df9d24f29789a424f1fdca656ac71f56c592a4990b57c0854305087c3da27b
+  __TEXT.__gcc_except_tab: 0xdbc sha256:46ab218e600fd0c7ad50ac8279c8f1ce79d7bf8e0f84819ac57306e23538ab24
+  __TEXT.__cstring: 0x28da sha256:22b41adb1feaf792446a8304b06b4b6dd47bf406c90975d08e052e7c12a79da8
+  __TEXT.__const: 0x293 sha256:6dadd9e5404d1f4da074e496f8129258938f3e98fbb51aa3999f0cac8a03fbb6
   __TEXT.__oslogstring: 0x43cb sha256:64f1248ea944040a47e13c023756ba11299cc108b588bca620b14e149673741d
-  __TEXT.__unwind_info: 0xb18 sha256:1d3d3e28a0c2f5d9992661f2dccb04123e78010c2ca240bb603d7a55c4876b8b
-  __DATA_CONST.__auth_got: 0x410 sha256:00b2b3d763c53a431a0a423cc630fbcf58c3c57dd723b6c0455490ad56e0a37b
-  __DATA_CONST.__got: 0xf0 sha256:13bc02f8f16c1c6bb304920c1151e5479b2915e475db715c1b8f2f224778343b
-  __DATA_CONST.__const: 0xca8 sha256:1738aeb90d0a25834151ac8ff114439061e0a82def662a6524628f6c8b9d4138
-  __DATA_CONST.__cfstring: 0x3e0 sha256:d92da652f7bd7db2b0df47f7c664a455c7f9301be09f757055110effe1aff3d2
-  __DATA.__data: 0xb0 sha256:5369c63bf15d486657da2cde53cee5e9ac6d5cb27bcc9db9ef0ccd8074b33545
-  __DATA.__bss: 0x140 sha256:7b6436b0c98f62380866d9432c2af0ee08ce16a171bda6951aecd95ee1307d61
+  __TEXT.__unwind_info: 0xae8 sha256:0c9bf65a6082996f93a2905c6127ddafbf1f3f8068d24308b32d9b3d9b95f26a
+  __DATA_CONST.__const: 0xc50 sha256:4891b64dc97dcfa7a232d3299db3abd8af7b476883bd6b1168fc1e462417e8b5
+  __DATA_CONST.__cfstring: 0x3e0 sha256:900e1904ecf43a0a8a9e57c5703cd564b10cc17ef238c6bc9c7b898405d7de79
+  __DATA_CONST.__auth_got: 0x3c8 sha256:3465f90914ed2f611d334ab97d6401109ae8029003783237d1f656458a9aa039
+  __DATA_CONST.__got: 0xd0 sha256:2108c05fe3f641f64d25a0967c65435a7067c3e87a2e338e53feaf54755625c4
+  __DATA.__data: 0xb0 sha256:b6c0cc9bc293405eacb3bf7db8f1e60cfdf19447c14a210c0e13326128b46c5f
+  __DATA.__bss: 0xd0 sha256:46f531b7ea0428fbf2c3ca2b60e8dc33d6bbfa000e0fd1b489c5e39140a47006
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMIDI.framework/CoreMIDI
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/caulk.framework/caulk
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: A4C6F41A-C283-32F9-B8B7-BF3718850DF5
-  Functions: 579
-  Symbols:   168
-  CStrings:  416
+  UUID: CF3E1C36-EB77-3403-9FBB-5CB8C2CF13EC
+  Functions: 570
+  Symbols:   154
+  CStrings:  443
 
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
