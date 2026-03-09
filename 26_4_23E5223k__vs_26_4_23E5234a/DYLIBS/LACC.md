## LACC

> `/System/Library/PrivateFrameworks/LACC.framework/LACC`

```diff

 8.2.1.0.0
-  __TEXT.__text: 0x10248
-  __TEXT.__auth_stubs: 0x6b0
+  __TEXT.__text: 0x10034
+  __TEXT.__auth_stubs: 0x6a0
   __TEXT.__gcc_except_tab: 0xc20
-  __TEXT.__cstring: 0x1154
+  __TEXT.__cstring: 0xd30
   __TEXT.__const: 0x860
   __TEXT.__unwind_info: 0x618
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__const: 0x28
-  __AUTH_CONST.__auth_got: 0x360
+  __AUTH_CONST.__auth_got: 0x358
   __AUTH_CONST.__const: 0x818
   __AUTH.__data: 0x10
   __DATA.__bss: 0x140

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libncurses.5.4.dylib
-  UUID: F54463DE-DADA-3943-A9BD-F8C7E8CCC707
+  UUID: 28C9ADB4-74DB-32A7-925D-444585BE8B55
   Functions: 311
-  Symbols:   185
-  CStrings:  141
+  Symbols:   184
+  CStrings:  138
 
Symbols:
- __ZNSt3__132__internal_log_hardening_failureEPKc
Functions:
~ __ZNK4lacc9ELFLoader12arch_versionEv : 212 -> 140
~ sub_25d2de3a0 -> sub_25d266358 : 1004 -> 960
~ sub_25d2de854 -> sub_25d2667e0 : 3104 -> 2936
~ __ZNK4lacc9ELFLoader5startEv : 80 -> 16
~ __ZNK4lacc9ELFLoader5flagsEv : 80 -> 16
~ sub_25d2e2714 -> sub_25d26a578 : 1448 -> 1368
~ sub_25d2e6960 -> sub_25d26e774 : 248 -> 268
~ sub_25d2e8cdc -> sub_25d270b04 : 808 -> 724
~ sub_25d2ed6bc -> sub_25d275490 : 60 -> 84
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJk9ugAiMDVUzRpR8aYjuoVLR4vDppOuluGu35k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:796: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CJk9ugAiMDVUzRpR8aYjuoVLR4vDppOuluGu35k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:801: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CJk9ugAiMDVUzRpR8aYjuoVLR4vDppOuluGu35k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:329: libc++ Hardening assertion __len <= static_cast<size_type>(numeric_limits<difference_type>::max()) failed: string_view::string_view(_CharT *, size_t): length does not fit in difference_type\n"

```
