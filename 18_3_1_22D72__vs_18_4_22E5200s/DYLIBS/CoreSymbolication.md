## CoreSymbolication

> `/System/Library/PrivateFrameworks/CoreSymbolication.framework/CoreSymbolication`

```diff

-64566.101.4.0.0
-  __TEXT.__text: 0xf175c
-  __TEXT.__auth_stubs: 0x1270
-  __TEXT.__const: 0x5916
-  __TEXT.__gcc_except_tab: 0x9e40
+64570.32.1.0.0
+  __TEXT.__text: 0xeb278
+  __TEXT.__auth_stubs: 0x12d0
+  __TEXT.__const: 0x4cb6
+  __TEXT.__gcc_except_tab: 0xa1fc
   __TEXT.__oslogstring: 0x14de
-  __TEXT.__cstring: 0x4587
-  __TEXT.__unwind_info: 0x4e38
-  __DATA_CONST.__got: 0x180
-  __DATA_CONST.__const: 0x1d58
-  __AUTH_CONST.__auth_got: 0x940
-  __AUTH_CONST.__auth_ptr: 0x28
-  __AUTH_CONST.__const: 0x45e0
-  __AUTH_CONST.__cfstring: 0x240
+  __TEXT.__cstring: 0x4930
+  __TEXT.__unwind_info: 0x48f8
+  __DATA_CONST.__got: 0x148
+  __DATA_CONST.__const: 0x1d98
+  __AUTH_CONST.__auth_got: 0x970
+  __AUTH_CONST.__auth_ptr: 0x80
+  __AUTH_CONST.__const: 0x4100
+  __AUTH_CONST.__cfstring: 0x340
   __AUTH.__data: 0x28
-  __DATA.__data: 0x28
-  __DATA.__bss: 0x910
+  __DATA.__data: 0x38
+  __DATA.__bss: 0x8a0
   __DATA_DIRTY.__data: 0x478
   __DATA_DIRTY.__crash_info: 0x40
   __DATA_DIRTY.__common: 0x18
-  __DATA_DIRTY.__bss: 0x148
+  __DATA_DIRTY.__bss: 0x1d8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libRosetta.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 4164
-  Symbols:   5074
-  CStrings:  720
+  Functions: 3850
+  Symbols:   4943
+  CStrings:  746
 
Symbols:
+ _CFArrayGetTypeID
+ _CFDictionaryGetTypeID
+ _CFGetTypeID
+ _CFNumberGetTypeID
+ _CFPropertyListCreateWithData
+ _CFStringGetLength
+ _CFStringGetMaximumSizeForEncoding
+ _CFStringGetTypeID
+ _CSSymbolIsDeduplicated
+ _CSSymbolicationSessionProcessKernelPlistChunkAndArchitecture
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTINSt3__117bad_function_callE
+ __ZTVNSt3__117bad_function_callE
- __ZNKSt9exception4whatEv
- _nanosleep
- _usleep
CStrings:
+ "/System/ExclaveKit/System/Library/dyld/"
+ "<deduplicated_symbol>"
+ "Address"
+ "Binaries"
+ "ERROR, no symbol owners in signature"
+ "Flags"
+ "Name"
+ "Path"
+ "Segments"
+ "Size"
+ "Stack empty for DW_OP_bra"
+ "UUID_String"
+ "could not open file, or it is not a Mach-O core file"
+ "exclaves - failed to dup() core file file descriptor"
+ "exclaves - failed to get segmentinfo_page"
+ "exclaves - failed to read segmentinfo"
+ "exclaves - failed to read segmentinfo_page"
+ "exclaves - failed to read vas_segment_t"
+ "exclaves - found overlapping vas_segment_ts"
+ "exclaves - invalid exclave metadata"
+ "exclaves - invalid segmentinfo_page address"
+ "exclaves - unable to analyze this vsip_version version using this tool"
+ "exclaves - unable to analyze this vsit_version using this tool"
+ "failed to allocate dummy port representing thread"
+ "failed to open core file"
+ "failed to parse 'addrable bits' LC_NOTE"
+ "failed to parse 'task crashinfo' LC_NOTE"
+ "failed to parse 'vm info' LC_NOTE"
+ "failed to parse thread load command"
+ "failed to read core file header"
+ "liblibc_plat.dylib"
+ "v16@?0r^{CSCppDyldSharedCache=[16c]IIIIQQQQQQQ[16C]QIIQQQQQQQQQQQQIb8b1b1b1b1b1b19QQQQQQQQQQQIIQQQQQIIIIQQII[16C]QQQQIIIQQQQQQIIQQQQ}8"
- "#1/"
- "."
- ".."
- "0x"
- "Error mapping dispositions for region %p-%p\n"
- "v16@?0r^{CSCppDyldSharedCache=[16c]IIIIQQQQQQQ[16C]QIIQQQQQQQQQQQQIb8b1b1b1b1b20QQQQQQQQQQQIIQQQQQIIIIQQII[16C]QQQQIIIQQQQQQII}8"

```
