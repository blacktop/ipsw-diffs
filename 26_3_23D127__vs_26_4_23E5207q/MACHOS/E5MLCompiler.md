## E5MLCompiler

> `/System/Library/PrivateFrameworks/CoreMLOdie.framework/XPCServices/E5MLCompiler.xpc/E5MLCompiler`

```diff

-3510.2.1.0.0
-  __TEXT.__text: 0xf6f0
-  __TEXT.__auth_stubs: 0x8e0
+3520.10.1.0.0
+  __TEXT.__text: 0xfb38
+  __TEXT.__auth_stubs: 0x8f0
+  __TEXT.__objc_stubs: 0x40
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methname: 0x1c
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0x768
+  __TEXT.__const: 0x728
   __TEXT.__constg_swiftt: 0x234
   __TEXT.__swift5_typeref: 0xec
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_reflstr: 0x74
   __TEXT.__swift5_fieldmd: 0x138
-  __TEXT.__cstring: 0x54e
+  __TEXT.__cstring: 0x8cb
   __TEXT.__swift5_types: 0x1c
+  __TEXT.__objc_classname: 0x4a
   __TEXT.__swift5_proto: 0x20
+  __TEXT.__objc_methname: 0x3f
+  __TEXT.__objc_methtype: 0x1
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x3c0
+  __TEXT.__unwind_info: 0x3e8
   __TEXT.__eh_frame: 0x80
-  __DATA_CONST.__auth_got: 0x470
+  __DATA_CONST.__auth_got: 0x480
   __DATA_CONST.__got: 0xa8
   __DATA_CONST.__auth_ptr: 0x100
   __DATA_CONST.__const: 0x680

   __DATA.__objc_selrefs: 0x10
   __DATA.__data: 0x388
   __DATA.__common: 0x1b
-  __DATA.__bss: 0xf78
+  __DATA.__bss: 0xf60
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/MIL.framework/MIL
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: 11941AFE-EF9E-30AF-BC17-F4B8F0EEC3DC
-  Functions: 308
-  Symbols:   291
-  CStrings:  73
+  UUID: 01EE5051-2B4C-3AF6-A9C4-E47379522DE8
+  Functions: 313
+  Symbols:   296
+  CStrings:  74
 
Symbols:
+ __Z21collectAddressSymbolsPPvjPKcRKNSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE
+ __Z21getLLVMSymbolizerPathN4llvm9StringRefE
+ __ZN4llvm13write_integerERNS_11raw_ostreamEjmNS_12IntegerStyleE
+ __ZN4llvm15SmallVectorBaseIjE13mallocForGrowEPvmmRm
+ __ZN4llvm21reportFatalUsageErrorERKNS_5TwineE
+ __ZNSt3__132__internal_log_hardening_failureEPKc
- __ZN4llvm13write_integerERNS_11raw_ostreamEimNS_12IntegerStyleE
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CHoZugAh0Pg-QQhjLh8Y07oQtf-TTRbs96T9X4g/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:801: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoZugAh0Pg-QQhjLh8Y07oQtf-TTRbs96T9X4g/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:811: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoZugAh0Pg-QQhjLh8Y07oQtf-TTRbs96T9X4g/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:329: libc++ Hardening assertion __len <= static_cast<size_type>(numeric_limits<difference_type>::max()) failed: string_view::string_view(_CharT *, size_t): length does not fit in difference_type\n"
- "\" doesn't exist!"
- "Executable \""

```
