## LACC

> `/System/Library/PrivateFrameworks/LACC.framework/LACC`

```diff

-8.1.3.0.0
-  __TEXT.__text: 0x106b4
-  __TEXT.__auth_stubs: 0x760
-  __TEXT.__gcc_except_tab: 0xc24
-  __TEXT.__cstring: 0xc54
-  __TEXT.__const: 0x710
-  __TEXT.__unwind_info: 0x650
-  __DATA_CONST.__got: 0x98
+8.2.1.0.0
+  __TEXT.__text: 0x10248
+  __TEXT.__auth_stubs: 0x6b0
+  __TEXT.__gcc_except_tab: 0xc20
+  __TEXT.__cstring: 0x1154
+  __TEXT.__const: 0x860
+  __TEXT.__unwind_info: 0x618
+  __DATA_CONST.__got: 0x88
   __DATA_CONST.__const: 0x28
-  __AUTH_CONST.__auth_got: 0x3b8
+  __AUTH_CONST.__auth_got: 0x360
   __AUTH_CONST.__const: 0x818
-  __DATA.__bss: 0x1d8
+  __AUTH.__data: 0x10
+  __DATA.__bss: 0x140
   __DATA.__common: 0x4
   - /System/Library/PrivateFrameworks/AppleCVHWA.framework/AppleCVHWA
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libncurses.5.4.dylib
-  UUID: E3308A8E-2595-36AC-AA47-8571DE7B0D40
-  Functions: 353
-  Symbols:   244
-  CStrings:  130
+  UUID: D390BB51-0DAD-3E2C-8F24-68C5C150113D
+  Functions: 311
+  Symbols:   185
+  CStrings:  141
 
Symbols:
+ __ZN4lacc7LaccABI15allocate_returnEjj
+ __ZN4lacc7LaccABI5startENS0_4PassE
+ __ZN4lacc7LaccABI6insertEPKvjj
+ __ZN4lacc7LaccABI6insertEPvjj
+ __ZNSt3__132__internal_log_hardening_failureEPKc
- __ZN4lacc7LaccABI15allocate_returnEj
- __ZN4lacc7LaccABI17write_stack_itemsEv
- __ZN4lacc7LaccABI3popEDv1_d
- __ZN4lacc7LaccABI3popEDv1_f
- __ZN4lacc7LaccABI3popEDv2_d
- __ZN4lacc7LaccABI3popEDv2_f
- __ZN4lacc7LaccABI3popEDv3_d
- __ZN4lacc7LaccABI3popEDv3_f
- __ZN4lacc7LaccABI3popEDv4_d
- __ZN4lacc7LaccABI3popEDv4_f
- __ZN4lacc7LaccABI3popEDv5_f
- __ZN4lacc7LaccABI3popEDv6_f
- __ZN4lacc7LaccABI3popEDv7_f
- __ZN4lacc7LaccABI3popEDv8_f
- __ZN4lacc7LaccABI3popEj
- __ZN4lacc7LaccABI3popEy
- __ZN4lacc7LaccABI6insertEPKvj
- __ZN4lacc7LaccABI6insertEPvj
- __ZN4lacc7LaccABI7extractEPKvj
- __ZN4lacc7LaccABI7extractEPvj
- __ZN4lacc7LaccABI7releaseEDv1_d
- __ZN4lacc7LaccABI7releaseEDv1_f
- __ZN4lacc7LaccABI7releaseEDv2_d
- __ZN4lacc7LaccABI7releaseEDv2_f
- __ZN4lacc7LaccABI7releaseEDv3_d
- __ZN4lacc7LaccABI7releaseEDv3_f
- __ZN4lacc7LaccABI7releaseEDv4_d
- __ZN4lacc7LaccABI7releaseEDv4_f
- __ZN4lacc7LaccABI7releaseEDv5_f
- __ZN4lacc7LaccABI7releaseEDv6_f
- __ZN4lacc7LaccABI7releaseEDv7_f
- __ZN4lacc7LaccABI7releaseEDv8_f
- __ZN4lacc7LaccABI7releaseEj
- __ZN4lacc7LaccABI7releaseEv
- __ZN4lacc7LaccABI7releaseEy
- __ZN4lacc7LaccABI7reserveEDv1_d
- __ZN4lacc7LaccABI7reserveEDv1_f
- __ZN4lacc7LaccABI7reserveEDv2_d
- __ZN4lacc7LaccABI7reserveEDv2_f
- __ZN4lacc7LaccABI7reserveEDv3_d
- __ZN4lacc7LaccABI7reserveEDv3_f
- __ZN4lacc7LaccABI7reserveEDv4_d
- __ZN4lacc7LaccABI7reserveEDv4_f
- __ZN4lacc7LaccABI7reserveEDv5_f
- __ZN4lacc7LaccABI7reserveEDv6_f
- __ZN4lacc7LaccABI7reserveEDv7_f
- __ZN4lacc7LaccABI7reserveEDv8_f
- __ZN4lacc7LaccABI7reserveEj
- __ZN4lacc7LaccABI7reserveEv
- __ZN4lacc7LaccABI7reserveEy
- __ZNSt3__115recursive_mutex4lockEv
- __ZNSt3__115recursive_mutex6unlockEv
- __ZNSt3__115recursive_mutexC1Ev
- __ZNSt3__115recursive_mutexD1Ev
- __ZNSt3__15mutex4lockEv
- __ZNSt3__15mutex6unlockEv
- __ZNSt3__15mutexD1Ev
- __ZSt7nothrow
- __Znwm
- __ZnwmRKSt9nothrow_t
- _del_curterm
- _set_curterm
- _setupterm
- _tigetnum
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CHn7ugDGXoGKEGnXaEUd2U1F16EPSnCADJweoSo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:796: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CHn7ugDGXoGKEGnXaEUd2U1F16EPSnCADJweoSo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:801: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CHn7ugDGXoGKEGnXaEUd2U1F16EPSnCADJweoSo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:329: libc++ Hardening assertion __len <= static_cast<size_type>(numeric_limits<difference_type>::max()) failed: string_view::string_view(_CharT *, size_t): length does not fit in difference_type\n"
+ "SHT_AARCH64_AUTH_RELR"
+ "SHT_AARCH64_MEMTAG_GLOBALS_DYNAMIC"
+ "SHT_AARCH64_MEMTAG_GLOBALS_STATIC"
+ "SHT_CREL"
+ "SHT_HEXAGON_ATTRIBUTES"
+ "SHT_LLVM_BB_ADDR_MAP_V0"
+ "SHT_LLVM_LTO"
+ "SHT_LLVM_OFFLOADING"
+ "Section has been stripped from the object file"
- "colors"

```
