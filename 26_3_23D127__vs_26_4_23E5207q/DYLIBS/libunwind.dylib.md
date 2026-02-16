## libunwind.dylib

> `/usr/lib/system/libunwind.dylib`

```diff

-1900.125.0.0.0
-  __TEXT.__text: 0x6940
-  __TEXT.__auth_stubs: 0x110
-  __TEXT.__cstring: 0xa7a
+2100.2.0.0.0
+  __TEXT.__text: 0x6c28
+  __TEXT.__auth_stubs: 0x100
+  __TEXT.__cstring: 0x9e4
   __TEXT.__unwind_info: 0x168
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__const: 0x310
-  __AUTH_CONST.__auth_got: 0x88
+  __AUTH_CONST.__auth_got: 0x80
   __AUTH_CONST.__const: 0x90
   __DATA.__data: 0x1b0
   __DATA.__bss: 0x851
-  __DATA_DIRTY.__bss: 0x8
   - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libdyld.dylib
   - /usr/lib/system/libsystem_c.dylib
   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
-  UUID: 1FD7DCE6-9DE3-3EF2-879F-36388FC8AF78
-  Functions: 77
-  Symbols:   170
-  CStrings:  128
+  UUID: A7F8E23A-0FB7-3A5C-A01D-7803E6D0ED88
+  Functions: 76
+  Symbols:   167
+  CStrings:  123
 
Symbols:
+ __ZN9libunwind12UnwindCursorINS_17LocalAddressSpaceENS_15Registers_arm64EE23getInfoFromDwarfSectionERU9__ptrauthILj1ELb1ELj33537EEKyRKNS_18UnwindInfoSectionsEj
- __ZN9libunwind12UnwindCursorINS_17LocalAddressSpaceENS_15Registers_arm64EE23getInfoFromDwarfSectionEmRKNS_18UnwindInfoSectionsEj
- __ZZ29__unw_is_pointer_auth_enabledE4mode
- ___unw_is_pointer_auth_enabled
- _sysctlbyname
CStrings:
- "Inconsistent invalid authentication state"
- "Invalid authentication state"
- "__unw_is_pointer_auth_enabled"
- "machdep.ptrauth_enabled"
- "normalizeNewLinkRegister"

```
