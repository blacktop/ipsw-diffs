## NaturalLanguage

> `/System/Library/Frameworks/NaturalLanguage.framework/NaturalLanguage`

```diff

-174.4.0.0.0
-  __TEXT.__text: 0x58c44
+174.5.0.0.0
+  __TEXT.__text: 0x596d4
   __TEXT.__auth_stubs: 0x1680
   __TEXT.__objc_methlist: 0x36cc
-  __TEXT.__const: 0x4e4
-  __TEXT.__cstring: 0x488d
+  __TEXT.__const: 0x4f4
+  __TEXT.__cstring: 0x4a7d
   __TEXT.__ustring: 0x32
-  __TEXT.__gcc_except_tab: 0x2c3c
+  __TEXT.__gcc_except_tab: 0x2d44
   __TEXT.__oslogstring: 0x128
-  __TEXT.__unwind_info: 0x1770
+  __TEXT.__unwind_info: 0x1760
   __TEXT.__objc_classname: 0x5f5
   __TEXT.__objc_methname: 0x6de7
   __TEXT.__objc_methtype: 0x1c8a

   __DATA_CONST.__objc_arraydata: 0xe8
   __AUTH_CONST.__auth_got: 0xb58
   __AUTH_CONST.__const: 0x650
-  __AUTH_CONST.__cfstring: 0x4760
+  __AUTH_CONST.__cfstring: 0x48a0
   __AUTH_CONST.__objc_const: 0x67c8
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0xf0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C6C0FE00-CCE7-343C-93BE-0BF930007A56
+  UUID: 5C58F2F8-CD84-3E13-9246-70920BBDBF34
   Functions: 1601
   Symbols:   5883
-  CStrings:  2603
+  CStrings:  2623
 
Functions:
~ +[NLLanguageRecognizer(Preferences) _isString:words:plausiblyInLanguage:increasedThreshold:] : 1768 -> 1992
~ +[NLLanguageRecognizer(Preferences) prewarmDictionariesForCandidateLanguages:preferredLanguages:waitUntilLoaded:] : 272 -> 572
~ +[NLLanguageRecognizer(Preferences) _candidate:matchesDominantLanguage:] : 408 -> 580
~ +[NLLanguageRecognizer(Preferences) mostAppropriateLanguageForString:candidateLanguages:preferredLanguages:] : 2260 -> 3648
~ +[NLLanguageRecognizer(Preferences) mostAppropriateLanguageForLongString:candidateLanguages:preferredLanguages:numberOfChunks:] : 800 -> 1420
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CJafugAH6Eg6cUuGHYXTNLBUxHaJRDlV8euajqw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJafugAH6Eg6cUuGHYXTNLBUxHaJRDlV8euajqw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJafugAH6Eg6cUuGHYXTNLBUxHaJRDlV8euajqw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJafugAH6Eg6cUuGHYXTNLBUxHaJRDlV8euajqw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJafugAH6Eg6cUuGHYXTNLBUxHaJRDlV8euajqw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJafugAH6Eg6cUuGHYXTNLBUxHaJRDlV8euajqw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJafugAH6Eg6cUuGHYXTNLBUxHaJRDlV8euajqw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJafugAH6Eg6cUuGHYXTNLBUxHaJRDlV8euajqw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJafugAH6Eg6cUuGHYXTNLBUxHaJRDlV8euajqw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJafugAH6Eg6cUuGHYXTNLBUxHaJRDlV8euajqw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJafugAH6Eg6cUuGHYXTNLBUxHaJRDlV8euajqw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJafugAH6Eg6cUuGHYXTNLBUxHaJRDlV8euajqw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CJafugAH6Eg6cUuGHYXTNLBUxHaJRDlV8euajqw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CJafugAH6Eg6cUuGHYXTNLBUxHaJRDlV8euajqw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1332: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "CFRO LID model dominant language: %@"
+ "Detected language for chunk: %@, length of chunk: %lu"
+ "Global LSTM LID model hypotheses: %@"
+ "Indic LID model hypotheses: %@"
+ "Prewarming dictionaries for %@"
+ "Returning early as Indic LID model detected %@ language with high confidence"
+ "UnknownLanguage"
+ "language: %@, increasedThreshold: %d, knownWordCharacterCount: %lu, unknownWordCharacterCount: %lu"
+ "mostAppropriateLanguageForLongString detected language: %@"
+ "mostAppropriateLanguageForString detected language: %@"
- "/AppleInternal/Library/BuildRoots/4~CHocugBWxDmxQ71Qi4ZlGnNq_DtDax7Cwuh7RJ0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CHocugBWxDmxQ71Qi4ZlGnNq_DtDax7Cwuh7RJ0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CHocugBWxDmxQ71Qi4ZlGnNq_DtDax7Cwuh7RJ0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CHocugBWxDmxQ71Qi4ZlGnNq_DtDax7Cwuh7RJ0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CHocugBWxDmxQ71Qi4ZlGnNq_DtDax7Cwuh7RJ0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CHocugBWxDmxQ71Qi4ZlGnNq_DtDax7Cwuh7RJ0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CHocugBWxDmxQ71Qi4ZlGnNq_DtDax7Cwuh7RJ0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CHocugBWxDmxQ71Qi4ZlGnNq_DtDax7Cwuh7RJ0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CHocugBWxDmxQ71Qi4ZlGnNq_DtDax7Cwuh7RJ0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CHocugBWxDmxQ71Qi4ZlGnNq_DtDax7Cwuh7RJ0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CHocugBWxDmxQ71Qi4ZlGnNq_DtDax7Cwuh7RJ0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CHocugBWxDmxQ71Qi4ZlGnNq_DtDax7Cwuh7RJ0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CHocugBWxDmxQ71Qi4ZlGnNq_DtDax7Cwuh7RJ0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CHocugBWxDmxQ71Qi4ZlGnNq_DtDax7Cwuh7RJ0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1332: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"

```
