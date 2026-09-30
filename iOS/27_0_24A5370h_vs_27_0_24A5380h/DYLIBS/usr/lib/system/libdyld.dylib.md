## libdyld.dylib

> `/usr/lib/system/libdyld.dylib`

```diff

-  __TEXT.__text: 0x1c7cc
+  __TEXT.__text: 0x1ce38
   __TEXT.__const: 0x32c
-  __TEXT.__cstring: 0x4be0
+  __TEXT.__cstring: 0x4cb5
   __TEXT.__gcc_except_tab: 0x20
-  __TEXT.__unwind_info: 0xda0
+  __TEXT.__unwind_info: 0xd98
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x1990
   __DATA_CONST.__helper: 0x8

   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libunwind.dylib
   - /usr/lib/system/libxpc.dylib
-  Functions: 853
+  Functions: 852
   Symbols:   2221
-  CStrings:  536
+  CStrings:  540
 
Sections:
~ __TEXT.__const : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__helper : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __DATA.__data : content changed
Symbols:
+ __ZNK6mach_o6Policy26enforceSegmentSectionNamesEv
- __ZN6mach_o12read_uleb128ENSt3__14spanIKhLm18446744073709551615EEERmRb
Functions:
~ ____ZNK6mach_o12UnsafeHeader14forEachSectionEU13block_pointerFvRKNS0_11SectionInfoERbE_block_invoke : 612 -> 584
~ ____ZN4dyld20ThreadLocalVariables24initializeThunksFromDiskEPK11mach_header_block_invoke : 284 -> 268
~ __ZNK6mach_o12Architecture6nameSVEv : 124 -> 128
~ ___clang_call_terminate : 20 -> 28
~ __ZNK6mach_o11BindOpcodes11forEachBindEU13block_pointerFv7CStringibhybiS1_bxbRbE : 1404 -> 1892
~ __ZNK6mach_o47PointerFormat_DYLD_CHAINED_PTR_ARM64E_SEGMENTED15writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE : 676 -> 668
~ __ZNK6mach_o11GenericTrie14recursiveVisitEmmmRbU13block_pointerFvNSt3__14spanIKhLm18446744073709551615EEES1_EU13block_pointerFb7CStringymmS1_EPNS_5ErrorE : 656 -> 720
~ __ZNK6mach_o11ExportsTrie23terminalPayloadToSymbolE7CStringNSt3__14spanIKhLm18446744073709551615EEERNS_6SymbolE : 776 -> 936
~ __ZNK6mach_o21FunctionVariantFixups5validENSt3__14spanIKNS_13MappedSegmentELm18446744073709551615EEE : 200 -> 188
~ __ZNK6mach_o6Header22validSemanticsSegmentsERKNS_6PolicyEy : 1724 -> 1684
~ __ZNK6mach_o6Header22validStructureLinkeditERKNS_6PolicyEy : 1620 -> 1612
~ __ZNK6mach_o6Header27parse_linker_option_commandERKNS0_15LoadCommandInfoEPNS_5ErrorE : 360 -> 376
~ __ZNK6mach_o6Header27validSemanticsSingleSegmentILb1EEENS_5ErrorERKNS_6PolicyEyNSt3__14spanIKhLm18446744073709551615EEE : 2092 -> 2416
~ __ZNK6mach_o6Header27validSemanticsSingleSegmentILb0EEENS_5ErrorERKNS_6PolicyEyNSt3__14spanIKhLm18446744073709551615EEE : 2056 -> 2380
- __ZN6mach_o12read_uleb128ENSt3__14spanIKhLm18446744073709551615EEERmRb
~ __ZNK6mach_o18PlatformInfo_macOS14yearForVersionENS_9Version32ERtRb : 60 -> 92
~ __ZNK6mach_o13RebaseOpcodes13forEachRebaseEU13block_pointerFv7CStringibhyRbE : 908 -> 1356
CStrings:
+ "section '%s' has an empty segment name"
+ "section '%s' segment name '%s' does not match containing segment's name '%s'"
+ "section in segment '%s' has an empty section name"
+ "segment load command has an empty segment name"

```
