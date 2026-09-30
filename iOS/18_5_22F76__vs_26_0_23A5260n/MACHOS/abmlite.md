## abmlite

> `/usr/bin/abmlite`

```diff

-1249.1.0.0.0
-  __TEXT.__text: 0x193d4
-  __TEXT.__auth_stubs: 0x770
+1371.0.1.0.0
+  __TEXT.__text: 0x19828
+  __TEXT.__auth_stubs: 0x760
   __TEXT.__objc_stubs: 0x560
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x14
   __TEXT.__const: 0x390
-  __TEXT.__gcc_except_tab: 0x1b80
-  __TEXT.__cstring: 0x991
+  __TEXT.__gcc_except_tab: 0x1ba8
+  __TEXT.__cstring: 0x923
   __TEXT.__oslogstring: 0xc6
   __TEXT.__objc_classname: 0xd
   __TEXT.__objc_methtype: 0x14
   __TEXT.__objc_methname: 0x31e
-  __TEXT.__unwind_info: 0x480
-  __DATA_CONST.__auth_got: 0x3d0
-  __DATA_CONST.__got: 0x298
+  __TEXT.__unwind_info: 0x488
+  __DATA_CONST.__auth_got: 0x3c8
+  __DATA_CONST.__got: 0x2a0
   __DATA_CONST.__const: 0x490
   __DATA_CONST.__cfstring: 0x160
   __DATA_CONST.__objc_classlist: 0x8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libedit.3.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 23739CF1-7139-3BB9-AB10-489D7D99875F
-  Functions: 139
-  Symbols:   328
+  UUID: 8DAC3B12-7DCF-31B3-A517-1FC449CEE619
+  Functions: 141
+  Symbols:   323
   CStrings:  162
 
Symbols:
+ _TelephonyBasebandWatchdogStartWithStackshot
+ _TelephonyBasebandWatchdogStop
+ __ZN3abm12HelperClient6createEPKc
+ __ZTVNSt3__115basic_streambufIcNS_11char_traitsIcEEEE
- __ZN3abm12HelperClient6createEPKcNSt3__110shared_ptrIN3ctu9LogServerEEE
- __ZN3ctu12OsLogContextC1ERKS0_
- __ZN3ctu12StaticLoggerC1ENS_12OsLogContextERKNSt3__110shared_ptrINS_9LogServerEEE
- __ZN3ctu12StaticLoggerC1Ev
- __ZN3ctu12StaticLoggerD1Ev
- __ZN3ctu16LoggerCommonBaseaSERKS0_
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEEC2Ev
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEED2Ev
- ___cxa_guard_abort
CStrings:
+ " to find your logs"
+ "B40@?0{group={object=^{dispatch_object_s}}}8{list<std::string, std::allocator<std::string>>={__list_node_base<std::string, void *>=^v^v}Q}16"
+ "Collecting logs during shutdown, please go to "
+ "v48@?0{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}8^v40"
- ")>> "
- ".."
- "B40@?0{group={object=^{dispatch_object_s}}}8{list<std::string, std::allocator<std::string>>={__list_node_base<std::string, void *>=^v^v}{__compressed_pair<unsigned long, std::allocator<std::__list_node<std::string, void *>>>=Q}}16"
- "v48@?0{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}}8^v40"

```
