## libswiftCore.dylib

> `/usr/lib/swift/libswiftCore.dylib`

```diff

-6.3.0.122.5
-  __TEXT.__text: 0x493028
+6.3.0.123.4
+  __TEXT.__text: 0x4930bc
   __TEXT.__auth_stubs: 0xd70
   __TEXT.__delay_stubs: 0x180
   __TEXT.__delay_helper: 0x304

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libswiftPrespecialized.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
-  UUID: 729CC053-F7B4-3798-B5B0-9BED2865BE34
+  UUID: 4B64700A-B454-3D27-B307-184FFE6A09D4
   Functions: 22062
   Symbols:   57088
   CStrings:  3058
Symbols:
+ __ZN12_GLOBAL__N_19Remangler43mangleCheckedObjCAsyncCompletionHandlerImplEPN5swift8Demangle9__runtime4NodeEj
- __ZN12_GLOBAL__N_19Remangler46manglePredefinedObjCAsyncCompletionHandlerImplEPN5swift8Demangle9__runtime4NodeEj
Functions:
~ __ZN12_GLOBAL__N_19Remangler46manglePredefinedObjCAsyncCompletionHandlerImplEPN5swift8Demangle9__runtime4NodeEj -> __ZN12_GLOBAL__N_19Remangler43mangleCheckedObjCAsyncCompletionHandlerImplEPN5swift8Demangle9__runtime4NodeEj : 252 -> 400
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CJk5ugA6nkLQB9mRmivobQN7xxaLQNmKCMCzeZs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CJk5ugA6nkLQB9mRmivobQN7xxaLQNmKCMCzeZs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJk5ugA6nkLQB9mRmivobQN7xxaLQNmKCMCzeZs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CJk5ugA6nkLQB9mRmivobQN7xxaLQNmKCMCzeZs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:801: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CJk5ugA6nkLQB9mRmivobQN7xxaLQNmKCMCzeZs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:811: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CJk5ugA6nkLQB9mRmivobQN7xxaLQNmKCMCzeZs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJk5ugA6nkLQB9mRmivobQN7xxaLQNmKCMCzeZs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:329: libc++ Hardening assertion __len <= static_cast<size_type>(numeric_limits<difference_type>::max()) failed: string_view::string_view(_CharT *, size_t): length does not fit in difference_type\n"
+ "CheckedObjCAsyncCompletionHandlerImpl"
+ "checked "
- "/AppleInternal/Library/BuildRoots/4~CI9fugAJcduiWndyfswuf9yj4Z6ouOvfMXp3ok0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CI9fugAJcduiWndyfswuf9yj4Z6ouOvfMXp3ok0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CI9fugAJcduiWndyfswuf9yj4Z6ouOvfMXp3ok0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CI9fugAJcduiWndyfswuf9yj4Z6ouOvfMXp3ok0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:801: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CI9fugAJcduiWndyfswuf9yj4Z6ouOvfMXp3ok0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:811: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CI9fugAJcduiWndyfswuf9yj4Z6ouOvfMXp3ok0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CI9fugAJcduiWndyfswuf9yj4Z6ouOvfMXp3ok0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:329: libc++ Hardening assertion __len <= static_cast<size_type>(numeric_limits<difference_type>::max()) failed: string_view::string_view(_CharT *, size_t): length does not fit in difference_type\n"
- "PredefinedObjCAsyncCompletionHandlerImpl"
- "predefined "

```
