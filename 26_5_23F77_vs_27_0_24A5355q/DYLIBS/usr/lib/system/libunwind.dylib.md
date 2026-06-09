## libunwind.dylib

> `/usr/lib/system/libunwind.dylib`

```diff

-2100.2.0.0.0
-  __TEXT.__text: 0x6c28 sha256:5ea031af64842f669a10a9412bf924662d4fbddc910e39ac2cccd688c2a761ef
-  __TEXT.__auth_stubs: 0x100 sha256:39dc960b9e38cb8fb29e467ea8017c983e697bf0c4561953ebfad519a30826c8
-  __TEXT.__cstring: 0x9e4 sha256:ed01c5622484348608d2d125c204a71463a80b4f84d3e65e34b6b979210d68ae
-  __TEXT.__unwind_info: 0x168 sha256:ecde7d967820ea44def732b9c2a2bdbb53f2f0aae97af06c74d3155455f3f003
-  __DATA_CONST.__got: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
-  __DATA_CONST.__const: 0x310 sha256:791f4e921cb96a233c9543f48118a6e4b1c04dbde85d7a1af032ad9b0e675d0e
+2200.5.0.0.0
+  __TEXT.__text: 0x6bac sha256:e9391c82b9fa25279cf423db4abb5aaf1f9a4765dd9ae6c6c961d6f4dfce0a47
+  __TEXT.__cstring: 0xb38 sha256:131cae6b4d42e92337fae1f955a5252fd872c12430865a7783ffff6a127fc93d
+  __TEXT.__unwind_info: 0x170 sha256:e4f57269f02c2bec56bf6e68c7c5578fd459d20641ee513326c97e7c2c334a69
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__const: 0x310 sha256:74d11dc3494111ef6bd06cd83cc0a152b80d17bb3c28d6d0e3dd78eb64c07dad
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x90 sha256:570ad30fa0e0403faa7abe4cd1926299f86d60a59976d2fb0108c971458bd119
   __AUTH_CONST.__auth_got: 0x80 sha256:38723a2e5e8a17aa7950dc008209944e898f69a7bd10a23c839d341e935fd5ca
-  __AUTH_CONST.__const: 0x90 sha256:019824f4cb70f3c2cf4595af42ee04557cfee1c4a0da400e5d4df9cb234c9cee
-  __DATA.__data: 0x1b0 sha256:6559c122113a0ad900b3f360577771300f8b14128ada6aa91ced2a2bec169bd5
+  __DATA.__data: 0x1b0 sha256:89333117742702dfd0a0c7470352a11aaa148533fe13db557a92b33965b398d2
   __DATA.__bss: 0x851 sha256:15363029bae7ae8c6be079e0c74d6c2346fbe28bc512ad18badfa63da98782fe
   - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libdyld.dylib

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
