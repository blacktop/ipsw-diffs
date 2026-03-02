## libswiftDemangle.dylib

> `/usr/lib/swift/libswiftDemangle.dylib`

```diff

-6.3.0.122.5
-  __TEXT.__text: 0x5a470
+6.3.0.123.4
+  __TEXT.__text: 0x5a504
   __TEXT.__auth_stubs: 0x1f0
-  __TEXT.__cstring: 0x588e
+  __TEXT.__cstring: 0x5888
   __TEXT.__const: 0x158
   __TEXT.__unwind_info: 0x6e0
   __DATA_CONST.__got: 0x8

   __DATA.__crash_info: 0x40
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 5D3872FD-8651-3014-A25A-508FAFFD3A14
+  UUID: 7B5D2588-3A3C-38E2-9788-CD79D55375E2
   Functions: 675
   Symbols:   1091
   CStrings:  1350
Symbols:
+ __ZN12_GLOBAL__N_19Remangler43mangleCheckedObjCAsyncCompletionHandlerImplEPN5swift8Demangle4NodeEj
- __ZN12_GLOBAL__N_19Remangler46manglePredefinedObjCAsyncCompletionHandlerImplEPN5swift8Demangle4NodeEj
Functions:
~ __ZN12_GLOBAL__N_19Remangler46manglePredefinedObjCAsyncCompletionHandlerImplEPN5swift8Demangle4NodeEj -> __ZN12_GLOBAL__N_19Remangler43mangleCheckedObjCAsyncCompletionHandlerImplEPN5swift8Demangle4NodeEj : 252 -> 400
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CJjiugDo-tq706MfEon8r5OhlOIojNNmaepRl48/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CJjiugDo-tq706MfEon8r5OhlOIojNNmaepRl48/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:811: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CJjiugDo-tq706MfEon8r5OhlOIojNNmaepRl48/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJjiugDo-tq706MfEon8r5OhlOIojNNmaepRl48/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:329: libc++ Hardening assertion __len <= static_cast<size_type>(numeric_limits<difference_type>::max()) failed: string_view::string_view(_CharT *, size_t): length does not fit in difference_type\n"
+ "CheckedObjCAsyncCompletionHandlerImpl"
+ "checked "
- "/AppleInternal/Library/BuildRoots/4~CI9cugA00TAU80bsN6CiNZavpofVDUOMmsjZCHc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CI9cugA00TAU80bsN6CiNZavpofVDUOMmsjZCHc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:811: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CI9cugA00TAU80bsN6CiNZavpofVDUOMmsjZCHc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CI9cugA00TAU80bsN6CiNZavpofVDUOMmsjZCHc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:329: libc++ Hardening assertion __len <= static_cast<size_type>(numeric_limits<difference_type>::max()) failed: string_view::string_view(_CharT *, size_t): length does not fit in difference_type\n"
- "PredefinedObjCAsyncCompletionHandlerImpl"
- "predefined "

```
