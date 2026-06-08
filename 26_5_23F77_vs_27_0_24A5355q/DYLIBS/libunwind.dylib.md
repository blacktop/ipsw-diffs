## libunwind.dylib

> `/usr/lib/system/libunwind.dylib`

```diff

-2100.2.0.0.0
-  __TEXT.__text: 0x6c28
-  __TEXT.__auth_stubs: 0x100
-  __TEXT.__cstring: 0x9e4
-  __TEXT.__unwind_info: 0x168
-  __DATA_CONST.__got: 0x10
+2200.5.0.0.0
+  __TEXT.__text: 0x6bac
+  __TEXT.__cstring: 0xb38
+  __TEXT.__unwind_info: 0x170
+  __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x310
-  __AUTH_CONST.__auth_got: 0x80
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x90
+  __AUTH_CONST.__auth_got: 0x80
   __DATA.__data: 0x1b0
   __DATA.__bss: 0x851
   - /usr/lib/system/libcompiler_rt.dylib

   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
-  UUID: EF282139-9BD2-3B2D-9323-418BFFFAA3C4
-  Functions: 76
-  Symbols:   167
-  CStrings:  123
+  UUID: 3E44CD79-A6C0-3602-A174-C6DE33949CD0
+  Functions: 80
+  Symbols:   174
+  CStrings:  138
 
Symbols:
+ __ZN9libunwind10CFI_ParserINS_17LocalAddressSpaceEE20parseFDEInstructionsINS_15Registers_arm64EEEbRS1_RKNS2_8FDE_InfoERKNS2_8CIE_InfoENT_23link_hardened_reg_arg_tEiPNS2_10PrologInfoE
+ __ZN9libunwind10CFI_ParserINS_17LocalAddressSpaceEE7findFDEINS_15Registers_arm64EEEbRS1_NT_23link_hardened_reg_arg_tEmmmPNS2_8FDE_InfoEPNS2_8CIE_InfoE
+ __ZN9libunwind12UnwindCursorINS_17LocalAddressSpaceENS_15Registers_arm64EE17getInfoFromFdeCieERKNS_10CFI_ParserIS1_E8FDE_InfoERKNS5_8CIE_InfoERU9__ptrauthILj1ELb1ELj33537EEKym
+ __ZN9libunwind15Registers_arm6412setIPPAuthLREyy
+ ___libunwind_Registers_arm64_za_disable
+ ___unw_strerror
+ _unw_strerror
- __ZN9libunwind10CFI_ParserINS_17LocalAddressSpaceEE20parseFDEInstructionsERS1_RKNS2_8FDE_InfoERKNS2_8CIE_InfoEmiPNS2_10PrologInfoE
- __ZN9libunwind10CFI_ParserINS_17LocalAddressSpaceEE7findFDEERS1_mmmmPNS2_8FDE_InfoEPNS2_8CIE_InfoE
- __ZN9libunwind12UnwindCursorINS_17LocalAddressSpaceENS_15Registers_arm64EE17getInfoFromFdeCieERKNS_10CFI_ParserIS1_E8FDE_InfoERKNS5_8CIE_InfoEmm
CStrings:
+ "Bad unwind with PAuth-enabled ABI"
+ "SME ZA disable failed"
+ "attempt to write read-only register"
+ "bad frame"
+ "bad register number"
+ "cross unwind with return address signing"
+ "invalid IP"
+ "invalid error code"
+ "libunwind: Bad unwind with PAuth-enabled ABI (0x%zX, 0x%zX)->0x%zX\n\n"
+ "no error"
+ "no unwind info found"
+ "out of memory"
+ "stop unwinding"
+ "unspecified (general) error"
+ "unsupported operation or bad value"
+ "unwind info has unsupported version"
+ "zaDisable"
- "Bad unwind through arm64e"
- "libunwind: Bad unwind through arm64e (0x%llX, 0x%llX)->0x%llX\n\n"

```
