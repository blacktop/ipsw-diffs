## AV1SW.videoencoder

> `/System/Library/VideoEncoders/AV1SW.videoencoder`

```diff

 158.5.0.0.0
-  __TEXT.__text: 0x27bb84
-  __TEXT.__auth_stubs: 0x910
+  __TEXT.__text: 0x27bac0
+  __TEXT.__auth_stubs: 0x900
   __TEXT.__const: 0x8dad0
-  __TEXT.__cstring: 0x8632
+  __TEXT.__cstring: 0x84a9
   __TEXT.__gcc_except_tab: 0x2dc
   __TEXT.__oslogstring: 0x24c
-  __TEXT.__unwind_info: 0x1858
+  __TEXT.__unwind_info: 0x1860
   __TEXT.__eh_frame: 0x4f0
   __DATA_CONST.__got: 0x1d8
   __DATA_CONST.__const: 0xb050
-  __AUTH_CONST.__auth_got: 0x490
+  __AUTH_CONST.__auth_got: 0x488
   __AUTH_CONST.__const: 0x2ae8
   __AUTH_CONST.__cfstring: 0xa0
   __DATA.__data: 0x778

   - /System/Library/Frameworks/VideoToolbox.framework/VideoToolbox
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: B5CE292E-6FF7-32FC-BEBB-AC65CC314371
+  UUID: F13A1D7F-FE55-3ECB-8676-894B6F94ECDE
   Functions: 4471
-  Symbols:   209
-  CStrings:  970
+  Symbols:   208
+  CStrings:  969
 
Symbols:
- __ZNSt3__132__internal_log_hardening_failureEPKc
Functions:
~ sub_29eda0138 -> sub_29f25b138 : 2904 -> 2836
~ sub_29eda2ca4 -> sub_29f25dc60 : 904 -> 804
~ sub_29eda37a4 -> sub_29f25e6fc : 300 -> 272
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJlJugDUjgsvwfsNKipbobj4XJfqKFQ2V9xdfSU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__memory/unique_ptr.h:582: libc++ Hardening assertion __checker_.__in_bounds<deleter_type>(std::__to_address(__ptr_), __i) failed: unique_ptr<T[]>::operator[](index): index out of range\n"

```
