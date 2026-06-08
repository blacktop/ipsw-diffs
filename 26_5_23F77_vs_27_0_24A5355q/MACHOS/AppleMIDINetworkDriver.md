## AppleMIDINetworkDriver

> `/System/Library/Audio/MIDI Drivers/AppleMIDINetworkDriver.plugin/AppleMIDINetworkDriver`

```diff

-324.501.0.6.0
-  __TEXT.__text: 0x39694
-  __TEXT.__auth_stubs: 0x1030
+328.0.0.0.0
+  __TEXT.__text: 0x3a278
+  __TEXT.__realtime: 0x5b4
+  __TEXT.__auth_stubs: 0x1090
   __TEXT.__objc_stubs: 0x1e0
-  __TEXT.__gcc_except_tab: 0x3ab0
-  __TEXT.__const: 0x488
-  __TEXT.__oslogstring: 0x1bd5
-  __TEXT.__cstring: 0x1358
+  __TEXT.__gcc_except_tab: 0x39ec
+  __TEXT.__const: 0x498
+  __TEXT.__oslogstring: 0x1d79
+  __TEXT.__cstring: 0x4018
   __TEXT.__objc_methname: 0x136
-  __TEXT.__unwind_info: 0x12a0
-  __DATA_CONST.__auth_got: 0x828
-  __DATA_CONST.__got: 0x1a8
-  __DATA_CONST.__const: 0xe90
+  __TEXT.__unwind_info: 0x1288
+  __DATA_CONST.__const: 0xe40
   __DATA_CONST.__cfstring: 0x640
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0x858
+  __DATA_CONST.__got: 0x1b0
   __DATA.__objc_selrefs: 0x78
   __DATA.__data: 0xa8
   __DATA.__bss: 0x60

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3AA484C5-3BA1-3377-B9C1-8DA9BCB7B5E3
-  Functions: 697
-  Symbols:   322
-  CStrings:  380
+  UUID: 95DF554B-1DFD-3BD5-A984-D662F0BD898B
+  Functions: 705
+  Symbols:   328
+  CStrings:  418
 
Symbols:
+ _CAAssertRtn
+ __ZNSt3__112system_errorC1EiRKNS_14error_categoryE
+ __ZNSt3__112system_errorD1Ev
+ __ZNSt3__115system_categoryEv
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x23
+ _objc_release_x24
- __ZTVN10__cxxabiv121__vmi_class_type_infoE
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "%25s:%-5d [CLIENT] Received Authentication Required but secret authentication was not indicated as supported"
+ "%25s:%-5d [CLIENT] Received User Authentication Required but user authentication was not indicated as supported"
+ "%25s:%-5d [HOST] HandleInvitation: rejecting invitation with empty endpointName or productInstanceId from %s"
+ "%25s:%-5d [HOST] HandleInvitationWithUserAuthentication: rejecting empty username from %s"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/__iterator/counted_iterator.h:108: libc++ Hardening assertion __count_ > 0 failed: Iterator is equal to or past end.\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/__ranges/view_interface.h:122: libc++ Hardening assertion !empty() failed: Precondition `!empty()` not satisfied. `.front()` called on an empty view.\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/array:271: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/array:275: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/optional:796: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/optional:801: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/optional:806: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/optional:811: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/span:457: libc++ Hardening assertion __last - __first >= 0 failed: invalid range in span's constructor (iterator, sentinel)\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/span:493: libc++ Hardening assertion __count <= size() failed: span<T>::first(count): count out of range\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/span:512: libc++ Hardening assertion __offset <= size() failed: span<T>::subspan(offset, count): offset out of range\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/span:516: libc++ Hardening assertion __count <= size() - __offset failed: span<T>::subspan(offset, count): offset + count out of range\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/span:525: libc++ Hardening assertion __idx < size() failed: span<T>::operator[](index): index out of range\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/string:1332: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/string_view:329: libc++ Hardening assertion __len <= static_cast<size_type>(numeric_limits<difference_type>::max()) failed: string_view::string_view(_CharT *, size_t): length does not fit in difference_type\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCfugB4hqQzUUPUbWkTvZ93lzJRAfAeo1l9qwc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
+ "GSL: Precondition failure at /Library/Caches/com.apple.xbs/E0CF15A1-FAF1-4D4F-B7F4-CD9DAA219B8E/TemporaryDirectory.klVCsW/Sources/CoreMIDI_Drivers/Source/MIDI/CppSPI/EventConversion.h: 656"
+ "GSL: Precondition failure at /Library/Caches/com.apple.xbs/E0CF15A1-FAF1-4D4F-B7F4-CD9DAA219B8E/TemporaryDirectory.klVCsW/Sources/CoreMIDI_Drivers/Source/MIDI/CppSPI/EventList.h: 77"
+ "GSL: Precondition failure at /Library/Caches/com.apple.xbs/E0CF15A1-FAF1-4D4F-B7F4-CD9DAA219B8E/TemporaryDirectory.klVCsW/Sources/CoreMIDI_Drivers/Source/MIDI/Drivers/Network/RTP/MIDIRTPSession.cpp: 1738"
+ "Secret authentication not supported"
+ "UMP Endpoint Name and Product Instance Id shall not be empty"
+ "User authentication not supported"
+ "Username shall not be empty"
- "CAException"
- "GSL: Precondition failure at /Library/Caches/com.apple.xbs/714F9FF1-ED95-47E6-BC39-391DCD4EF568/TemporaryDirectory.Wpocr0/Sources/CoreMIDI_Drivers/Source/MIDI/CppSPI/EventConversion.h: 656"
- "GSL: Precondition failure at /Library/Caches/com.apple.xbs/714F9FF1-ED95-47E6-BC39-391DCD4EF568/TemporaryDirectory.Wpocr0/Sources/CoreMIDI_Drivers/Source/MIDI/CppSPI/EventList.h: 76"
- "GSL: Precondition failure at /Library/Caches/com.apple.xbs/714F9FF1-ED95-47E6-BC39-391DCD4EF568/TemporaryDirectory.Wpocr0/Sources/CoreMIDI_Drivers/Source/MIDI/Drivers/Network/RTP/MIDIRTPSession.cpp: 1738"
- "~MIDIPacketEmitter"

```
