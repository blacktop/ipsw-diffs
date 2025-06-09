## libunwind.dylib

> `/usr/lib/system/libunwind.dylib`

```diff

 1900.125.0.0.0
-  __TEXT.__text: 0x69ac
+  __TEXT.__text: 0x6940
   __TEXT.__auth_stubs: 0x110
   __TEXT.__cstring: 0xa7a
-  __TEXT.__unwind_info: 0x160
+  __TEXT.__unwind_info: 0x168
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__const: 0x310
   __AUTH_CONST.__auth_got: 0x88

   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
-  UUID: 0AB49CF9-D5D3-314F-99EB-7DA7A94343D9
+  UUID: 9F4B8247-1766-3134-8A1F-2D274948D6A1
   Functions: 77
   Symbols:   170
   CStrings:  128
Functions:
~ __ZN9libunwind12UnwindCursorINS_17LocalAddressSpaceENS_15Registers_arm64EE24setInfoBasedOnIPRegisterEb : 2516 -> 2468
~ __ZN9libunwind12UnwindCursorINS_17LocalAddressSpaceENS_15Registers_arm64EE23getInfoFromDwarfSectionEmRKNS_18UnwindInfoSectionsEj : 880 -> 860
~ __ZN9libunwind12UnwindCursorINS_17LocalAddressSpaceENS_15Registers_arm64EE17getInfoFromFdeCieERKNS_10CFI_ParserIS1_E8FDE_InfoERKNS5_8CIE_InfoEmm : 444 -> 440
~ __ZN9libunwind12UnwindCursorINS_17LocalAddressSpaceENS_15Registers_arm64EE7getInfoEP15unw_proc_info_t : 492 -> 464
~ __ZN9libunwind12UnwindCursorINS_17LocalAddressSpaceENS_15Registers_arm64EE4stepEb : 2840 -> 2868
~ ___unw_is_pointer_auth_enabled : 424 -> 416
~ __ZN9libunwind17DwarfInstructionsINS_17LocalAddressSpaceENS_15Registers_arm64EE18evaluateExpressionEmRS1_RKS2_m : 2048 -> 2056
~ ___unw_set_reg : 820 -> 824
~ __Unwind_RaiseException : 828 -> 824
~ _unwind_phase2 : 744 -> 740
~ _unwind_phase2_forced : 620 -> 616
~ __Unwind_GetLanguageSpecificData : 204 -> 196
~ __Unwind_GetRegionStart : 200 -> 192
~ __Unwind_GetIP : 264 -> 268
~ __Unwind_FindEnclosingFunction : 544 -> 536
~ __Unwind_Find_FDE : 608 -> 596
~ __Unwind_GetIPInfo : 312 -> 316

```
