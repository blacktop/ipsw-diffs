## LACC

> `/System/Library/PrivateFrameworks/LACC.framework/LACC`

```diff

-6.19.1.0.0
-  __TEXT.__text: 0xeb44
-  __TEXT.__auth_stubs: 0x5f0
-  __TEXT.__gcc_except_tab: 0x9d0
-  __TEXT.__cstring: 0xb8e
-  __TEXT.__const: 0x635
-  __TEXT.__unwind_info: 0x600
+8.1.2.0.0
+  __TEXT.__text: 0x10814
+  __TEXT.__auth_stubs: 0x760
+  __TEXT.__gcc_except_tab: 0xb6c
+  __TEXT.__cstring: 0xc70
+  __TEXT.__const: 0x71e
+  __TEXT.__unwind_info: 0x678
   __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__got: 0x68
+  __DATA_CONST.__got: 0x90
   __DATA_CONST.__const: 0x28
-  __AUTH_CONST.__const: 0x798
-  __AUTH_CONST.__auth_got: 0x300
+  __AUTH_CONST.__const: 0x858
+  __AUTH_CONST.__auth_got: 0x3b8
   __DATA.__common: 0x4
-  __DATA.__bss: 0x158
+  __DATA.__bss: 0x1d8
   - /System/Library/PrivateFrameworks/AppleCVHWA.framework/AppleCVHWA
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libncurses.5.4.dylib
-  UUID: 6E90D478-700C-3115-A905-6B4047CB2532
-  Functions: 363
-  Symbols:   214
-  CStrings:  122
+  UUID: FBE2CDA1-B467-387B-B0EB-C9E1DC070D8C
+  Functions: 383
+  Symbols:   245
+  CStrings:  134
 
Symbols:
+ _CVHWAGeneralProcessingRunProgram
+ _CVHWAGetLaccArchVersion
+ __ZN4lacc7LaccABI14dump_registersERNS_13CallInterfaceE
+ __ZNK13lacc_hardware12LaccHardwarecvRN4lacc13CallInterfaceEEv
+ __ZNK13lacc_hardware12LaccHardwarecvRN4lacc15ConfigInterfaceEEv
+ __ZNK13lacc_hardware12LaccHardwarecvRNS_6LaccHwEEv
+ __ZNKSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strEv
+ __ZNKSt3__16locale9use_facetERNS0_2idE
+ __ZNKSt3__18ios_base6getlocEv
+ __ZNKSt9exception4whatEv
+ __ZNSt11logic_errorC2ERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7reserveEm
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE6sentryC1ERS3_
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE6sentryD1Ev
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEj
+ __ZNSt3__114basic_iostreamIcNS_11char_traitsIcEEED2Ev
+ __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEEC2Ev
+ __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEED2Ev
+ __ZNSt3__115recursive_mutexD1Ev
+ __ZNSt3__15ctypeIcE2idE
+ __ZNSt3__16localeD1Ev
+ __ZNSt3__18ios_base33__set_badbit_and_consider_rethrowEv
+ __ZNSt3__18ios_base4initEPv
+ __ZNSt3__18ios_base5clearEj
+ __ZNSt3__19basic_iosIcNS_11char_traitsIcEEED2Ev
+ __ZNSt3__19to_stringEi
+ __ZNSt3__19to_stringEm
+ __ZNSt9exceptionD2Ev
+ __ZTISt9exception
+ __ZTTNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE
+ __ZTVNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEE
+ __ZTVNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE
+ ___cxa_end_catch
+ _getenv
+ _memset
+ _posix_madvise
+ _strcmp
- _MGGetProductType
- __ZN13lacc_hardware12LaccHardwarecvRN4lacc13CallInterfaceEEv
- __ZN13lacc_hardware12LaccHardwarecvRN4lacc15ConfigInterfaceEEv
- __ZN13lacc_hardware12LaccHardwarecvRNS_6LaccHwEEv
- __ZNSt3__111__call_onceERVmPvPFvS2_E
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_
CStrings:
+ " has invalid sh_entsize: expected "
+ ") is larger than maximum value for size type ("
+ ", but got "
+ ": "
+ "PC"
+ "PKTS"
+ "R"
+ "RET"
+ "SHT_LLVM_BB_ADDR_MAP"
+ "SHT_MSP430_ATTRIBUTES"
+ "STAT0"
+ "SmallVector capacity unable to grow. Already at maximum size "
+ "SmallVector unable to grow. Requested capacity ("
+ "TERM"
+ "e_shstrndx == SHN_XINDEX, but the section header table is empty"
- " has an invalid sh_entsize: "
- "SmallVector capacity overflow during allocation"
- "SmallVector capacity unable to grow"

```
