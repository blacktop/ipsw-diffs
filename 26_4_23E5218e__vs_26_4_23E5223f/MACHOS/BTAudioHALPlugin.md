## BTAudioHALPlugin

> `/System/Library/Audio/Plug-Ins/HAL/BTAudioHALPlugin.driver/BTAudioHALPlugin`

```diff

-194.24.0.0.0
-  __TEXT.__text: 0x78dbc
-  __TEXT.__auth_stubs: 0x12f0
+194.25.0.0.0
+  __TEXT.__text: 0x78a90
+  __TEXT.__auth_stubs: 0x12e0
   __TEXT.__objc_stubs: 0x2700
   __TEXT.__init_offsets: 0xa0
   __TEXT.__objc_methlist: 0x1154
   __TEXT.__gcc_except_tab: 0x2298
   __TEXT.__const: 0x189c
-  __TEXT.__cstring: 0x4e65
+  __TEXT.__cstring: 0x4be1
   __TEXT.__oslogstring: 0x14994
   __TEXT.__objc_classname: 0x155
   __TEXT.__objc_methname: 0x3e2c
   __TEXT.__objc_methtype: 0x120c
   __TEXT.__unwind_info: 0x1b10
   __TEXT.__eh_frame: 0x50
-  __DATA_CONST.__auth_got: 0x988
+  __DATA_CONST.__auth_got: 0x980
   __DATA_CONST.__got: 0x2c8
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x4c68

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf.dylib
-  UUID: 3EB767D0-B63A-341C-BD75-3973EA3280BA
+  UUID: D60647D0-9378-3676-BCE6-EA76CC8F1696
   Functions: 2708
-  Symbols:   468
-  CStrings:  3038
+  Symbols:   467
+  CStrings:  3036
 
Symbols:
- __ZNSt3__132__internal_log_hardening_failureEPKc
Functions:
~ sub_49230 : 160 -> 136
~ sub_4b8ec -> sub_4b8d4 : 292 -> 228
~ sub_4ba10 -> sub_4b9b8 : 256 -> 184
~ sub_4bb10 -> sub_4ba70 : 632 -> 312
~ sub_4bd88 -> sub_4bba8 : 352 -> 320
~ sub_4bf20 -> sub_4bd20 : 1064 -> 764
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJRnugBYEgRQloSHT8qUA8xh1phU0GLlFvKjnmU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRnugBYEgRQloSHT8qUA8xh1phU0GLlFvKjnmU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"

```
