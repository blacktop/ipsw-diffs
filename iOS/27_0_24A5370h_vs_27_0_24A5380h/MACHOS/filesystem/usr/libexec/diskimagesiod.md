## diskimagesiod

> `/usr/libexec/diskimagesiod`

```diff

-  __TEXT.__text: 0x1e242c
-  __TEXT.__auth_stubs: 0x2350
-  __TEXT.__objc_stubs: 0x68a0
-  __TEXT.__objc_methlist: 0x3a34
-  __TEXT.__gcc_except_tab: 0x1b744
-  __TEXT.__const: 0x14137
-  __TEXT.__cstring: 0x162ae
+  __TEXT.__text: 0x1ebdb4
+  __TEXT.__auth_stubs: 0x2450
+  __TEXT.__objc_stubs: 0x6860
+  __TEXT.__objc_methlist: 0x3a1c
+  __TEXT.__gcc_except_tab: 0x1bbc4
+  __TEXT.__const: 0x17397
+  __TEXT.__cstring: 0x172ec
   __TEXT.__oslogstring: 0x2dab
-  __TEXT.__objc_methname: 0x793a
+  __TEXT.__objc_methname: 0x78e1
   __TEXT.__objc_classname: 0x667
-  __TEXT.__objc_methtype: 0x2811
+  __TEXT.__objc_methtype: 0x27fa
   __TEXT.__constg_swiftt: 0x60
   __TEXT.__swift5_typeref: 0x58
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
   __TEXT.__ustring: 0x13c
-  __TEXT.__unwind_info: 0xdcb0
+  __TEXT.__unwind_info: 0xdf68
   __TEXT.__eh_frame: 0xf0
-  __DATA_CONST.__const: 0x38448
+  __DATA_CONST.__const: 0x38548
   __DATA_CONST.__cfstring: 0x4c40
   __DATA_CONST.__objc_classlist: 0x248
   __DATA_CONST.__objc_catlist: 0x10

   __DATA_CONST.__objc_arraydata: 0xa0
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA_CONST.__auth_got: 0x11c0
-  __DATA_CONST.__got: 0x5b8
+  __DATA_CONST.__auth_got: 0x1240
+  __DATA_CONST.__got: 0x628
   __DATA_CONST.__auth_ptr: 0x48
   __DATA.__objc_const: 0x5a18
-  __DATA.__objc_selrefs: 0x1f18
+  __DATA.__objc_selrefs: 0x1f08
   __DATA.__objc_ivar: 0x318
   __DATA.__objc_data: 0x1750
   __DATA.__data: 0xde0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/local/lib/libcurl.4.dylib
-  Functions: 11270
-  Symbols:   782
-  CStrings:  4637
+  Functions: 11425
+  Symbols:   800
+  CStrings:  4697
 
Sections:
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ __ZNKSt13runtime_error4whatEv
+ __ZNSt13runtime_errorC2EPKc
+ __ZNSt13runtime_errorD2Ev
+ __ZNSt3__16localeC1ERKS0_
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
+ _time
CStrings:
+ " does not allow the "
+ " formatting argument"
+ " option"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/__format/formatter_output.h:237: libc++ Hardening assertion __first <= __last failed: Not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/__format/formatter_output.h:250: libc++ Hardening assertion __first <= __last failed: Not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/__format/formatter_output.h:264: libc++ Hardening assertion __first <= __last failed: Not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/__format/parser_std_format_spec.h:594: libc++ Hardening assertion __begin != __end failed: when called with an empty input the function will cause undefined behavior by evaluating data not in the input\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/c++/previous/string_view:329: libc++ Hardening assertion __len <= static_cast<size_type>(numeric_limits<difference_type>::max()) failed: string_view::string_view(_CharT *, size_t): length does not fit in difference_type\n"
+ "01"
+ "01234567"
+ "0123456789abcdef"
+ "0123456789abcdefghijklmnopqrstuvwxyz"
+ "0B"
+ "0X"
+ "0b"
+ "An argument index may not have a negative value"
+ "End of input while parsing an argument index"
+ "End of input while parsing format specifier precision"
+ "Error creating (unlocked) backend"
+ "Integral value outside the range of the char type"
+ "Legacy prepended-header UDIF image is not supported by this framework"
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
+ "Unexpected error creating (unlocked) backend"
+ "Using automatic argument numbering in manual argument numbering mode"
+ "Using manual argument numbering in automatic argument numbering mode"
+ "\\\""
+ "\\'"
+ "\\\\"
+ "\\n"
+ "\\r"
+ "\\t"
+ "\\u{"
+ "\\x{"
+ "a bool"
+ "a character"
+ "a floating-point"
+ "a pointer"
+ "alternate form"
+ "an integer"
+ "auto AEAHelper::key_params_t::run(function &&) [function = di_utils::overloaded<(lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:221:8), (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:225:8), (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:229:8), (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:232:8)> &]"
+ "errorWithDIException:prefix:error:"
+ "false"
+ "infnanINFNAN"
+ "locale-specific form"
+ "precision"
+ "sign"
+ "true"
+ "void crypto::details::unset_futures_errors_reporter<std::ranges::transform_view<std::ranges::ref_view<container_it<std::__deque_iterator<FileLocalAsync::promise_io_t, FileLocalAsync::promise_io_t *, FileLocalAsync::promise_io_t &, FileLocalAsync::promise_io_t **, long>>>, (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/DiskImages2/app/backends/file.cpp:1095:24)>::__iterator<false>>::report_errors(int) [It = std::ranges::transform_view<std::ranges::ref_view<container_it<std::__deque_iterator<FileLocalAsync::promise_io_t, FileLocalAsync::promise_io_t *, FileLocalAsync::promise_io_t &, FileLocalAsync::promise_io_t **, long>>>, (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/DiskImages2/app/backends/file.cpp:1095:24)>::__iterator<false>]"
+ "void crypto::details::unset_futures_errors_reporter<std::ranges::transform_view<std::ranges::ref_view<container_it<std::__wrap_iter<FileLocalAsync::promise_io_t *>>>, (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/DiskImages2/app/backends/file.cpp:997:23)>::__iterator<false>>::report_errors(int) [It = std::ranges::transform_view<std::ranges::ref_view<container_it<std::__wrap_iter<FileLocalAsync::promise_io_t *>>>, (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/DiskImages2/app/backends/file.cpp:997:23)>::__iterator<false>]"
+ "zero-padding"
+ "{:02x}{:02x}"
- "@48@0:8r^v16@24@32^@40"
- "Error creating AEA backend"
- "Failed reading sparse image header"
- "Unexpected error creating AEA backend"
- "auto AEAHelper::key_params_t::run(function &&) [function = di_utils::overloaded<(lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:219:8), (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:223:8), (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:227:8), (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:230:8)> &]"
- "errorWithDIException:description:prefix:error:"
- "failWithDIException:description:error:"
- "nilWithDIException:description:error:"
- "void crypto::details::unset_futures_errors_reporter<std::ranges::transform_view<std::ranges::ref_view<container_it<std::__deque_iterator<FileLocalAsync::promise_io_t, FileLocalAsync::promise_io_t *, FileLocalAsync::promise_io_t &, FileLocalAsync::promise_io_t **, long>>>, (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/DiskImages2/app/backends/file.cpp:1093:24)>::__iterator<false>>::report_errors(int) [It = std::ranges::transform_view<std::ranges::ref_view<container_it<std::__deque_iterator<FileLocalAsync::promise_io_t, FileLocalAsync::promise_io_t *, FileLocalAsync::promise_io_t &, FileLocalAsync::promise_io_t **, long>>>, (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/DiskImages2/app/backends/file.cpp:1093:24)>::__iterator<false>]"

```
