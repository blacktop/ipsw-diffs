## com.apple.DiagnosticExtensions.Telephony

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Telephony.appex/com.apple.DiagnosticExtensions.Telephony`

```diff

-1249.1.0.0.0
-  __TEXT.__text: 0x25028
-  __TEXT.__auth_stubs: 0xbc0
+1371.0.1.0.0
+  __TEXT.__text: 0x257e4
+  __TEXT.__auth_stubs: 0xbe0
   __TEXT.__objc_stubs: 0x580
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x1c0
   __TEXT.__const: 0x4b8
-  __TEXT.__gcc_except_tab: 0x35a4
-  __TEXT.__cstring: 0x611
-  __TEXT.__oslogstring: 0xa54
+  __TEXT.__gcc_except_tab: 0x35e4
+  __TEXT.__cstring: 0x5ea
+  __TEXT.__oslogstring: 0xa96
   __TEXT.__objc_methname: 0x497
   __TEXT.__objc_classname: 0x47
-  __TEXT.__objc_methtype: 0x2e4
-  __TEXT.__unwind_info: 0x770
-  __DATA_CONST.__auth_got: 0x5f0
+  __TEXT.__objc_methtype: 0x282
+  __TEXT.__unwind_info: 0x780
+  __DATA_CONST.__auth_got: 0x600
   __DATA_CONST.__got: 0x2f0
-  __DATA_CONST.__const: 0x920
+  __DATA_CONST.__const: 0x9a0
   __DATA_CONST.__cfstring: 0x220
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_ivar: 0x28
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x50
-  __DATA.__bss: 0x38
+  __DATA.__bss: 0x78
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/ABMHelper.framework/ABMHelper

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 003DF832-1E1A-3AA1-8574-FB6B51EC751B
-  Functions: 287
-  Symbols:   381
-  CStrings:  266
+  UUID: 535C5D7A-D233-351F-8EED-887917B794CD
+  Functions: 289
+  Symbols:   376
+  CStrings:  267
 
Symbols:
+ _TelephonyBasebandWatchdogStartWithStackshot
+ _TelephonyBasebandWatchdogStop
+ __ZN3abm12HelperClient6createEPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEmc
+ __ZTVNSt3__115basic_streambufIcNS_11char_traitsIcEEEE
+ _objc_release_x28
- __Z15GetOsLogContextv
- __ZN3abm12HelperClient6createEPKcNSt3__110shared_ptrIN3ctu9LogServerEEE
- __ZN3ctu12OsLogContextC1ERKS0_
- __ZN3ctu12StaticLoggerC1ENS_12OsLogContextERKNSt3__110shared_ptrINS_9LogServerEEE
- __ZN3ctu12StaticLoggerC1Ev
- __ZN3ctu12StaticLoggerD1Ev
- __ZN3ctu16LoggerCommonBaseaSERKS0_
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEEC2Ev
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEED2Ev
- ___cxa_guard_abort
- ___tolower
CStrings:
+ "Failed to open base directory %s (%s)"
+ "Failed to open info baseband log info file %s"
+ "Ignoring dump with timestamp %s for sysdiagnose"
+ "No baseband info file found for timestamp %s"
+ "Watchdog timed out"
+ "logging.profile"
+ "supports.fs"
+ "util"
+ "v48@?0{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}8^v40"
+ "{basic_string<char, std::char_traits<char>, std::allocator<char>>=\"__rep_\"(__rep=\"__s\"{__short=\"__data_\"[23c]\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"*\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1})}"
- ".*"
- ": "
- "Error %s (%s)\n"
- "Failed to open info file: %s"
- "Ignore dump for sysdiagnose: %s"
- "No baseband info file found for %s"
- "global"
- "v48@?0{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}}8^v40"
- "{basic_string<char, std::char_traits<char>, std::allocator<char>>=\"__r_\"{__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=\"__value_\"(__rep=\"__s\"{__short=\"__data_\"[23c]\"__padding_\"[0C]\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"*\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1})}}"

```
