## AppC3D

> `/System/Library/PrivateFrameworks/AppC3D.framework/AppC3D`

```diff

-1.15.4.0.0
-  __TEXT.__text: 0x62eb34
-  __TEXT.__auth_stubs: 0x2160
-  __TEXT.__cstring: 0x11e3a
-  __TEXT.__const: 0x5c597
+1.16.1.0.0
+  __TEXT.__text: 0x63e92c
+  __TEXT.__auth_stubs: 0x2220
+  __TEXT.__cstring: 0x125ad
+  __TEXT.__const: 0x5f4f7
   __TEXT.__oslogstring: 0x36b
-  __TEXT.__gcc_except_tab: 0x4e52c
-  __TEXT.__unwind_info: 0x12e80
+  __TEXT.__gcc_except_tab: 0x4f60c
+  __TEXT.__unwind_info: 0x13300
   __TEXT.__eh_frame: 0x300
   __TEXT.__objc_methname: 0x4f
   __TEXT.__objc_stubs: 0xa0
-  __DATA_CONST.__got: 0x390
+  __DATA_CONST.__got: 0x398
   __DATA_CONST.__const: 0x1470
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x10c0
+  __AUTH_CONST.__auth_got: 0x1120
   __AUTH_CONST.__auth_ptr: 0x68
-  __AUTH_CONST.__const: 0x205d0
-  __AUTH_CONST.__cfstring: 0x300
-  __DATA.__data: 0x5458
+  __AUTH_CONST.__const: 0x20618
+  __AUTH_CONST.__cfstring: 0x320
+  __AUTH.__data: 0x8
+  __DATA.__data: 0x5460
+  __DATA.__llvm_prf_cnts: 0x100
+  __DATA.__llvm_prf_data: 0x300
+  __DATA.__llvm_prf_names: 0x51d
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x90
-  __DATA.__common: 0x90
+  __DATA.__common: 0x80
   __DATA_DIRTY.__data: 0x88
-  __DATA_DIRTY.__bss: 0x2200
+  __DATA_DIRTY.__bss: 0x2220
+  __LLVM_COV.__llvm_covfun: 0x2888
+  __LLVM_COV.__llvm_covmap: 0x158
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 12484
-  Symbols:   695
-  CStrings:  1760
+  Functions: 12648
+  Symbols:   708
+  CStrings:  1826
 
Symbols:
+ __ZNSt3__16localeC1ERKS0_
+ __ZNSt3__16localeC1Ev
+ __ZNSt3__16localeaSERKS0_
+ __ZNSt3__18numpunctIcE2idE
+ __ZNSt3__18to_charsEPcS0_d
+ __ZNSt3__18to_charsEPcS0_dNS_12chars_formatE
+ __ZNSt3__18to_charsEPcS0_dNS_12chars_formatEi
+ __ZNSt3__18to_charsEPcS0_e
+ __ZNSt3__18to_charsEPcS0_eNS_12chars_formatE
+ __ZNSt3__18to_charsEPcS0_eNS_12chars_formatEi
+ __ZNSt3__18to_charsEPcS0_f
+ __ZNSt3__18to_charsEPcS0_fNS_12chars_formatE
+ __ZNSt3__18to_charsEPcS0_fNS_12chars_formatEi
+ ___udivti3
+ ___umodti3
+ _exit
+ _fprintf
- ___invert_d2
- ___invert_d3
- ___invert_f3
- _cblas_sgemv$NEWLAPACK
CStrings:
+ " : {}"
+ " BLAS error: Parameter %!s(MISSING)"
+ " BLAS error: Parameter number %!l(MISSING)d"
+ " does not allow the "
+ " formatting argument"
+ " option"
+ " passed to %!s(MISSING) was %!l(MISSING)d, which is invalid.\n"
+ "'.\n"
+ "/Library/Caches/com.apple.xbs/Sources/AppC3D/library/Essentials/Apple/src/Clock.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/AppC3D/library/Kit/CoreVideo/src/CVImage.cpp:55"
+ "0 == mach_timebase_info(&timebase)"
+ "01"
+ "01234567"
+ "0123456789abcdef"
+ "0123456789abcdefghijklmnopqrstuvwxyz"
+ "0B"
+ "0X"
+ "0b"
+ "0x"
+ "Abort"
+ "An argument index may not have a negative value"
+ "Assert"
+ "End of input while parsing an argument index"
+ "End of input while parsing format specifier precision"
+ "Integral value outside the range of the char type"
+ "Replacement argument isn't a standard signed or unsigned integer type"
+ "The argument index is invalid"
+ "The argument index should end with a ':' or a '}'"
+ "The argument index starts with an invalid character"
+ "The argument index value is too large for the number of arguments supplied"
+ "The fill option contains an invalid value"
+ "The format specifier contains malformed Unicode characters"
+ "The format specifier for "
+ "The format specifier should consume the input or end with a '}'"
+ "The format string contains an invalid escape sequence"
+ "The format string terminates at a '{'"
+ "The numeric value of the format specifier is too large"
+ "The precision option does not contain a value or an argument index"
+ "The replacement field misses a terminating '}'"
+ "The type does not fit in the mask"
+ "The type option contains an invalid value for "
+ "The type option contains an invalid value for a string formatting argument"
+ "The value of the argument index exceeds its maximum value"
+ "The width option should not have a leading zero"
+ "UniqueDeviceID"
+ "Using automatic argument numbering in manual argument numbering mode"
+ "Using manual argument numbering in automatic argument numbering mode"
+ "\\\""
+ "\\'"
+ "\\n"
+ "\\r"
+ "\\t"
+ "a bool"
+ "a character"
+ "a floating-point"
+ "a pointer"
+ "alternate form"
+ "an integer"
+ "infnanINFNAN"
+ "locale-specific form"
+ "precision"
+ "sign"
+ "string_view::substr"
+ "zero-padding"
+ "{:.{}}"
+ "{:<{}}"
+ "{:>{}}"
+ "{:{}}"
+ "{}: {}"
+ "{}:{}{}{}\n"
- " : "
- "/Library/Caches/com.apple.xbs/Sources/AppC3D/library/Kit/CoreVideo/src/CVImage.cpp:51"
- "Abort: "
- "Assert: "

```
