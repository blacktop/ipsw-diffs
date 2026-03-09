## E5MLCompiler

> `/System/Library/PrivateFrameworks/CoreMLOdie.framework/XPCServices/E5MLCompiler.xpc/E5MLCompiler`

```diff

 3520.10.1.0.0
-  __TEXT.__text: 0xfb38
-  __TEXT.__auth_stubs: 0x8f0
+  __TEXT.__text: 0xfa54
+  __TEXT.__auth_stubs: 0x8e0
   __TEXT.__objc_stubs: 0x40
   __TEXT.__init_offsets: 0x4
   __TEXT.__swift5_entry: 0x8

   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_reflstr: 0x74
   __TEXT.__swift5_fieldmd: 0x138
-  __TEXT.__cstring: 0x8cb
+  __TEXT.__cstring: 0x4a8
   __TEXT.__swift5_types: 0x1c
   __TEXT.__objc_classname: 0x4a
   __TEXT.__swift5_proto: 0x20

   __TEXT.__swift5_protos: 0x8
   __TEXT.__unwind_info: 0x3e8
   __TEXT.__eh_frame: 0x80
-  __DATA_CONST.__auth_got: 0x480
+  __DATA_CONST.__auth_got: 0x478
   __DATA_CONST.__got: 0xa8
   __DATA_CONST.__auth_ptr: 0x100
   __DATA_CONST.__const: 0x680

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: C03B80D6-AF24-3646-89B6-3E04CE7F8811
+  UUID: 69A553BF-7ED6-34B4-AB6D-FD6BCA4CDFCD
   Functions: 313
-  Symbols:   296
-  CStrings:  74
+  Symbols:   295
+  CStrings:  71
 
Symbols:
- __ZNSt3__132__internal_log_hardening_failureEPKc
Functions:
~ __ZN4llvm19formatv_object_base17parseFormatStringENS_9StringRefEmb : 1636 -> 1580
~ __ZNK4llvm14raw_fd_ostream10has_colorsEv : 60 -> 84
~ sub_10000c964 -> sub_10000c944 : 3652 -> 3628
~ __ZN4llvm3sys17findProgramByNameENS_9StringRefENS_8ArrayRefIS1_EE : 1072 -> 1016
~ sub_10000dfa8 -> sub_10000df38 : 196 -> 180
~ sub_10000e310 -> sub_10000e290 : 724 -> 692
~ sub_10000f64c -> sub_10000f5ac : 1104 -> 1052
~ sub_10000fa9c -> sub_10000f9c8 : 308 -> 292
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJlVugD6ORTTwsrIeclsMJzCIobQ85QTZvhB18w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:801: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CJlVugD6ORTTwsrIeclsMJzCIobQ85QTZvhB18w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:811: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CJlVugD6ORTTwsrIeclsMJzCIobQ85QTZvhB18w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:329: libc++ Hardening assertion __len <= static_cast<size_type>(numeric_limits<difference_type>::max()) failed: string_view::string_view(_CharT *, size_t): length does not fit in difference_type\n"

```
