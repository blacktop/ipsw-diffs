## SleepWidgetUI

> `/System/Library/PrivateFrameworks/SleepWidgetUI.framework/SleepWidgetUI`

```diff

-5132.0.0.0.0
-  __TEXT.__text: 0x876fc
-  __TEXT.__auth_stubs: 0x1c70
-  __TEXT.__const: 0x3170
+5138.0.1.1.0
+  __TEXT.__text: 0x86ea4
+  __TEXT.__auth_stubs: 0x1c60
+  __TEXT.__const: 0x3190
   __TEXT.__cstring: 0xa4d
   __TEXT.__constg_swiftt: 0x11d0
   __TEXT.__swift5_typeref: 0x140c

   __TEXT.__oslogstring: 0xbd4
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__unwind_info: 0x14a0
-  __TEXT.__eh_frame: 0x3a0
+  __TEXT.__unwind_info: 0x1498
+  __TEXT.__eh_frame: 0x330
   __TEXT.__objc_methname: 0x435
-  __DATA_CONST.__got: 0x800
-  __DATA_CONST.__const: 0x120
+  __DATA_CONST.__got: 0x810
+  __DATA_CONST.__const: 0x160
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1d8
-  __AUTH_CONST.__auth_got: 0xe38
-  __AUTH_CONST.__auth_ptr: 0x8e8
+  __AUTH_CONST.__auth_got: 0xe30
+  __AUTH_CONST.__auth_ptr: 0x890
   __AUTH_CONST.__const: 0x1680
   __AUTH_CONST.__objc_const: 0x120
-  __AUTH.__data: 0x9c8
-  __DATA.__data: 0xd58
+  __AUTH.__data: 0x930
+  __DATA.__data: 0xd10
   __DATA.__bss: 0x1e20
   __DATA.__common: 0x18
-  __DATA_DIRTY.__data: 0x13e0
+  __DATA_DIRTY.__data: 0x14c0
   __DATA_DIRTY.__bss: 0x1180
   __DATA_DIRTY.__common: 0x28
   - /System/Library/Frameworks/AppIntents.framework/AppIntents

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftWebKit.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1944
-  Symbols:   216
-  CStrings:  0
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 1943
+  Symbols:   222
+  CStrings:  108
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
- _swift_continuation_await
- _swift_continuation_init
CStrings:
+ "15SmallVectorImplINS_9StringRefEEE"
+ "_7ELFTypeILNS_7support10endiannessE1ELb0EEEE14dynamicEntriesEv"
+ "__ZN4llvm10ThreadPool4growEi"
+ "__ZN4llvm10TimeRecord14getCurrentTimeEb"
+ "__ZN4llvm13getNamedTimerENS_9StringRefES0_"
+ "__ZN4llvm16NamedRegionTimerC1ENS_9StringRefES1_S1_S1_b"
+ "__ZN4llvm16StoreIntToMemoryERKNS_5APIntEPhj"
+ "__ZN4llvm17BranchProbabilityC1Ejj"
+ "__ZN4llvm17ConvertUTF8toWideEjNS_9StringRefERPcRPKh"
+ "__ZN4llvm17LoadIntFromMemoryERNS_5APIntEPKhj"
+ "__ZN4llvm17isLegalUTF8StringEPPKhS1_"
+ "__ZN4llvm18ConvertUTF8toUTF32EPPKhS1_PPjS3_NS_15ConversionFlagsE"
+ "__ZN4llvm18getNumBytesForUTF8Eh"
+ "__ZN4llvm19isLegalUTF8SequenceEPKhS1_"
+ "__ZN4llvm22timeTraceProfilerBeginENS_9StringRefENS_12function_refIFNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEvEEE"
+ "__ZN4llvm22timeTraceProfilerBeginENS_9StringRefES0_"
+ "__ZN4llvm24convertUTF16ToUTF8StringENS_8ArrayRefIcEERNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE"
+ "__ZN4llvm28getTimeTraceProfilerInstanceEv"
+ "__ZN4llvm2cl16AddLiteralOptionERNS0_6OptionENS_9StringRefE"
+ "__ZN4llvm2cl17PrintOptionValuesEv"
+ "__ZN4llvm2cl18getGeneralCategoryEv"
+ "__ZN4llvm2cl23ParseCommandLineOptionsEiPKPKcNS_9StringRefEPNS_11raw_ostreamES2_b"
+ "__ZN4llvm2cl3optINSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEELb0ENS0_6parserIS8_EEE10setDefaultEv"
+ "__ZN4llvm2cl3optINSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEELb0ENS0_6parserIS8_EEE16handleOccurrenceEjNS_9StringRefESC_"
+ "__ZN4llvm2cl3optIbLb0ENS0_6parserIbEEE10setDefaultEv"
+ "__ZN4llvm2cl3optIcLb0ENS0_6parserIcEEE10setDefaultEv"
+ "__ZN4llvm2cl3optIcLb0ENS0_6parserIcEEE16handleOccurrenceEjNS_9StringRefES5_"
+ "__ZN4llvm2cl3optIcLb0ENS0_6parserIcEEE19getExtraOptionNamesERNS_15SmallVectorImplINS_9StringRefEEE"
+ "__ZN4llvm2cl3optIiLb0ENS0_6parserIiEEE10setDefaultEv"
+ "__ZN4llvm2cl3optIjLb0ENS0_6parserIjEEE10setDefaultEv"
+ "__ZN4llvm2cl6Option11addArgumentEv"
+ "__ZN4llvm2cl6Option9setArgStrENS_9StringRefE"
+ "__ZN4llvm3ARM21parseBranchProtectionENS_9StringRefERNS0_22ParsedBranchProtectionERS1_"
+ "__ZN4llvm5APInt11shlSlowCaseEj"
+ "__ZN4llvm5APInt12ashrSlowCaseEj"
+ "__ZN4llvm5APInt12lshrSlowCaseEj"
+ "__ZN4llvm5APInt7udivremERKS0_S2_RS0_S3_"
+ "__ZN4llvm5APInt7udivremERKS0_yRS0_Ry"
+ "__ZN4llvm5APIntlSERKS0_"
+ "__ZN4llvm5RISCV12parseCPUKindENS_9StringRefE"
+ "__ZN4llvm5RISCV16parseTuneCPUKindENS_9StringRefEb"
+ "__ZN4llvm5RISCV20fillValidCPUArchListERNS_15SmallVectorImplINS_9StringRefEEEb"
+ "__ZN4llvm5RISCV24fillValidTuneCPUArchListERNS_15SmallVectorImplINS_9StringRefEEEb"
+ "__ZN4llvm5Timer5clearEv"
+ "__ZN4llvm6Triple13getOSTypeNameENS0_6OSTypeE"
+ "__ZN4llvm6Triple9normalizeENS_9StringRefE"
+ "__ZN4llvm6TripleC1ERKNS_5TwineE"
+ "__ZN4llvm8BisectorINSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEE15serializeToFileENS_9StringRefE"
+ "__ZNK4llvm2cl19generic_parser_base14getOptionWidthERKNS0_6OptionE"
+ "__ZNK4llvm2cl3optIcLb0ENS0_6parserIcEEE14getOptionWidthEv"
+ "__ZNK4llvm2cl3optIcLb0ENS0_6parserIcEEE15printOptionInfoEm"
+ "__ZNK4llvm2cl3optIcLb0ENS0_6parserIcEEE16printOptionValueEmb"
+ "__ZNK4llvm2cl3optIcLb0ENS0_6parserIcEEE27getValueExpectedFlagDefaultEv"
+ "__ZNK4llvm2cl6parserIyE15printOptionDiffERKNS0_6OptionEyNS0_11OptionValueIyEEm"
+ "__ZNK4llvm5APInt10sextOrSelfEj"
+ "__ZNK4llvm5APInt11reverseBitsEv"
+ "__ZNK4llvm5APInt11sextOrTruncEj"
+ "__ZNK4llvm5APInt11zextOrTruncEj"
+ "__ZNK4llvm5APInt23countPopulationSlowCaseEv"
+ "__ZNK4llvm5APInt4rotrEj"
+ "__ZNK4llvm5APInt4sdivERKS0_"
+ "__ZNK4llvm5APInt4sextEj"
+ "__ZNK4llvm5APInt4sremERKS0_"
+ "__ZNK4llvm5APInt4udivERKS0_"
+ "__ZNK4llvm5APInt4udivEy"
+ "__ZNK4llvm5APInt4uremERKS0_"
+ "__ZNK4llvm5APInt4uremEy"
+ "__ZNK4llvm5APInt4zextEj"
+ "__ZNK4llvm5APInt5printERNS_11raw_ostreamEb"
+ "__ZNK4llvm5APInt5truncEj"
+ "__ZNK4llvm5APInt7sadd_ovERKS0_Rb"
+ "__ZNK4llvm5APInt7sdiv_ovERKS0_Rb"
+ "__ZNK4llvm5APInt7smul_ovERKS0_Rb"
+ "__ZNK4llvm5APInt7sshl_ovERKS0_Rb"
+ "__ZNK4llvm5APInt7ssub_ovERKS0_Rb"
+ "__ZNK4llvm5APInt7uadd_ovERKS0_Rb"
+ "__ZNK4llvm5APInt7umul_ovERKS0_Rb"
+ "__ZNK4llvm5APInt7ushl_ovERKS0_Rb"
+ "__ZNK4llvm5APInt7usub_ovERKS0_Rb"
+ "__ZNK4llvm5APInt8byteSwapEv"
+ "__ZNK4llvm5APInt8toStringERNS_15SmallVectorImplIcEEjbb"
+ "__ZNK4llvm6APSInt7ProfileERNS_16FoldingSetNodeIDE"
+ "__ZNK4llvm6Triple11getArchNameEv"
+ "__ZNK4llvm6Triple13getVendorNameEv"
+ "__ZNK4llvm6Triple18getEnvironmentNameEv"
+ "__ZNK4llvm6Triple9getOSNameEv"
+ "__ZNK4llvm6object7ELFFileINS0_7ELFTypeILNS_7support10endiannessE0ELb0EEEE11notes_beginERKNS0_13Elf_Phdr_ImplIS5_EERNS_5ErrorE"
+ "__ZNK4llvm6object7ELFFileINS0_7ELFTypeILNS_7support10endiannessE0ELb0EEEE11notes_beginERKNS0_13Elf_Shdr_ImplIS5_EERNS_5ErrorE"
+ "__ZNK4llvm6object7ELFFileINS0_7ELFTypeILNS_7support10endiannessE0ELb0EEEE12toMappedAddrEyNS_12function_refIFNS_5ErrorERKNS_5TwineEEEE"
+ "__ZNK4llvm6object7ELFFileINS0_7ELFTypeILNS_7support10endiannessE0ELb0EEEE14dynamicEntriesEv"
+ "__ZNK4llvm6object7ELFFileINS0_7ELFTypeILNS_7support10endiannessE0ELb0EEEE15program_headersEv"
+ "__ZNK4llvm6object7ELFFileINS0_7ELFTypeILNS_7support10endiannessE0ELb0EEEE21getDynamicTagAsStringEjy"
+ "__ZNK4llvm6object7ELFFileINS0_7ELFTypeILNS_7support10endiannessE0ELb0EEEE23getStringTableForSymtabERKNS0_13Elf_Shdr_ImplIS5_EENS_8ArrayRefIS8_EE"
+ "__ZNK4llvm6object7ELFFileINS0_7ELFTypeILNS_7support10endiannessE0ELb1EEEE14dynamicEntriesEv"
+ "__ZNK4llvm6object7ELFFileINS0_7ELFTypeILNS_7support10endiannessE0ELb1EEEE23getStringTableForSymtabERKNS0_13Elf_Shdr_ImplIS5_EENS_8ArrayRefIS8_EE"
+ "__ZNK4llvm6object7ELFFileINS0_7ELFTypeILNS_7support10endiannessE1ELb0EEEE11notes_beginERKNS0_13Elf_Phdr_ImplIS5_EERNS_5ErrorE"
+ "__ZNK4llvm6object7ELFFileINS0_7ELFTypeILNS_7support10endiannessE1ELb0EEEE11notes_beginERKNS0_13Elf_Shdr_ImplIS5_EERNS_5ErrorE"
+ "__ZNK4llvm6object7ELFFileINS0_7ELFTypeILNS_7support10endiannessE1ELb0EEEE12toMappedAddrEyNS_12function_refIFNS_5ErrorERKNS_5TwineEEEE"
+ "__ZNK4llvm6object7ELFFileINS0_7ELFTypeILNS_7support10endiannessE1ELb0EEEE15program_headersEv"
+ "__ZNK4llvm6object7ELFFileINS0_7ELFTypeILNS_7support10endiannessE1ELb0EEEE21getDynamicTagAsStringEjy"
+ "__ZNK4llvm6object7ELFFileINS0_7ELFTypeILNS_7support10endiannessE1ELb1EEEE11notes_beginERKNS0_13Elf_Phdr_ImplIS5_EERNS_5ErrorE"
+ "__ZNK4llvm6object7ELFFileINS0_7ELFTypeILNS_7support10endiannessE1ELb1EEEE11notes_beginERKNS0_13Elf_Shdr_ImplIS5_EERNS_5ErrorE"
+ "__ZNK4llvm6object7ELFFileINS0_7ELFTypeILNS_7support10endiannessE1ELb1EEEE12toMappedAddrEyNS_12function_refIFNS_5ErrorERKNS_5TwineEEEE"
+ "__ZNK4llvm6object7ELFFileINS0_7ELFTypeILNS_7support10endiannessE1ELb1EEEE14dynamicEntriesEv"
+ "__ZNK4llvm6object7ELFFileINS0_7ELFTypeILNS_7support10endiannessE1ELb1EEEE15program_headersEv"
+ "__ZNK4llvm6object7ELFFileINS0_7ELFTypeILNS_7support10endiannessE1ELb1EEEE21getDynamicTagAsStringEjy"
+ "__ZNK4llvm6object7ELFFileINS0_7ELFTypeILNS_7support10endiannessE1ELb1EEEE23getStringTableForSymtabERKNS0_13Elf_Shdr_ImplIS5_EENS_8ArrayRefIS8_EE"
+ "v"

```
