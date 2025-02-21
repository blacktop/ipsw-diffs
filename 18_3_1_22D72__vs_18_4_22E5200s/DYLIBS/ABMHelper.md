## ABMHelper

> `/System/Library/PrivateFrameworks/ABMHelper.framework/ABMHelper`

```diff

-1220.0.0.0.0
-  __TEXT.__text: 0x13b8c4
-  __TEXT.__auth_stubs: 0x2490
-  __TEXT.__init_offsets: 0xb8
+1245.0.0.0.0
+  __TEXT.__text: 0x13828c
+  __TEXT.__auth_stubs: 0x2500
+  __TEXT.__init_offsets: 0xc4
   __TEXT.__objc_methlist: 0x14
-  __TEXT.__gcc_except_tab: 0x185dc
-  __TEXT.__const: 0x5f22
-  __TEXT.__cstring: 0x65bf
-  __TEXT.__oslogstring: 0x89e4
-  __TEXT.__unwind_info: 0x5b78
+  __TEXT.__const: 0x60ea
+  __TEXT.__gcc_except_tab: 0x18e1c
+  __TEXT.__cstring: 0x68d7
+  __TEXT.__oslogstring: 0x8b7a
+  __TEXT.__unwind_info: 0x5d08
   __TEXT.__objc_classname: 0x16
   __TEXT.__objc_methname: 0x5e6
   __TEXT.__objc_methtype: 0x28
   __TEXT.__objc_stubs: 0x9c0
-  __DATA_CONST.__got: 0x5b0
-  __DATA_CONST.__const: 0x1fe0
+  __DATA_CONST.__got: 0x5e0
+  __DATA_CONST.__const: 0x1d10
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x270
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x1260
-  __AUTH_CONST.__const: 0x7e50
-  __AUTH_CONST.__cfstring: 0x7a0
+  __AUTH_CONST.__auth_got: 0x1298
+  __AUTH_CONST.__const: 0x7f30
+  __AUTH_CONST.__cfstring: 0x820
   __AUTH_CONST.__objc_const: 0x90
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28
-  __DATA.__data: 0x3a0
-  __DATA.__common: 0x20
+  __DATA.__data: 0x430
   __DATA.__bss: 0x8
+  __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x50
-  __DATA_DIRTY.__data: 0x228
-  __DATA_DIRTY.__bss: 0x500
+  __DATA_DIRTY.__data: 0x230
+  __DATA_DIRTY.__bss: 0x530
   __DATA_DIRTY.__common: 0xc0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsysdiagnose.dylib
-  Functions: 3491
-  Symbols:   4774
-  CStrings:  2017
+  Functions: 3513
+  Symbols:   4901
+  CStrings:  2048
 
Symbols:
+ _CFArrayGetCount
+ _CFArrayGetTypeID
+ _CFArrayGetValueAtIndex
+ _CFUserNotificationCancel
+ _CFUserNotificationDisplayNotice
+ _TelephonyBasebandWatchdogStartWithStackshot
+ _TelephonyBasebandWatchdogStop
+ __ZGVN3ctu9SingletonI21CapabilitiesOverridesS1_NS_23PthreadMutexGuardPolicyIS1_EEE9sInstanceE
+ __ZN12capabilities3abs27kKeySupportsCMHandDetectionE
+ __ZN17KernelPCIABPTrace17fileSnapshot_syncEv
+ __ZN17KernelPCIABPTrace22createBuffContext_syncEmRNSt3__110shared_ptrINS_11PipeContextEEEN8dispatch13group_sessionE
+ __ZN3ctu9SingletonI21CapabilitiesOverridesS1_NS_23PthreadMutexGuardPolicyIS1_EEE9sInstanceE
+ __ZNSt3__117bad_function_callD0Ev
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTINSt3__117bad_function_callE
+ __ZTVNSt3__117bad_function_callE
+ _dispatch_group_notify_f
- __ZN17KernelPCIABPTrace17fileSnapshot_syncERNSt3__110shared_ptrINS_11PipeContextEEE
- __ZN17KernelPCIABPTrace22createBuffContext_syncEmRNSt3__110shared_ptrINS_11PipeContextEEE
- __ZNSt9exceptionD2Ev
CStrings:
+ "#I CellularLogging has not started yet"
+ "#I Showing notification: %s"
+ "#I Snapshot completion received (flush completion with null-log)"
+ "#I Snapshotting for shutdown, the logs from scratch will not be moved"
+ "#I Trace Mode is not set to Active on AP. Skip starting trace reader"
+ "#I error=%d, responseFlags=0x%lx"
+ "#I snapshot (coredump) complete"
+ "Active on AP (Background)"
+ "Active on AP (Streaming)"
+ "Baseband DIAG DMC Integrity Match"
+ "Baseband Logging Mode has been changed"
+ "Baseband Trace Mode has been changed"
+ "Capability %s returning overridden value"
+ "Cellular Problem"
+ "Cellular Radar Notifications Disabled"
+ "Cellular Sysdiagnose Complete"
+ "DIAG Mode changed"
+ "DIAG Service Error"
+ "ETB Configuration"
+ "Integrity check for DMC file found an issue. Please file a radar under Purple ETL"
+ "Mode has changed. Please, reboot the device"
+ "No ResetInfoRegexPatterns entry found in ABMProperties, so the default patterns will be used"
+ "OK"
+ "Reboot the device before continuing to use the baseband trace"
+ "ResetInfoReasonRegexPattern"
+ "ResetInfoReasonRegexPatternMask"
+ "ResetInfoRegexPatterns"
+ "Resetting the baseband to apply your change"
+ "Restart the device before continuing to use DIAG trace"
+ "Restart the device before continuing to use the baseband trace"
+ "To control notifications please go to:\n\nSettings > Carrier Settings > Baseband Manager > Logging Settings > Radar Notifications"
+ "Trace is disabled / mode is - Active Background. Skip snapshot processing"
+ "Watchdog timed out"
+ "com.apple.telephony.capabilities"
+ "v112@?0{TraceInfoEntry=i{Timestamp={map<Timestamp::TimeDomain, timeval, std::less<Timestamp::TimeDomain>, std::allocator<std::pair<const Timestamp::TimeDomain, timeval>>>={__tree<std::__value_type<Timestamp::TimeDomain, timeval>, std::__map_value_compare<Timestamp::TimeDomain, std::__value_type<Timestamp::TimeDomain, timeval>, std::less<Timestamp::TimeDomain>>, std::allocator<std::__value_type<Timestamp::TimeDomain, timeval>>>=^v{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<Timestamp::TimeDomain, timeval>, void *>>>={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{__compressed_pair<unsigned long, std::__map_value_compare<Timestamp::TimeDomain, std::__value_type<Timestamp::TimeDomain, timeval>, std::less<Timestamp::TimeDomain>>>=Q}}}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}}8"
+ "v32@?0{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}8"
+ "v36@?0i8{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}12"
+ "v48@?0{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}}8^v40"
+ "v48@?0{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}}8{dict={object=^v}}40"
- "#I Trace Mode is not set to AP. Skip starting trace reader"
- "Default pattern masks will be used"
- "Trace is disabled. Skip snapshot processing"
- "v112@?0{TraceInfoEntry=i{Timestamp={map<Timestamp::TimeDomain, timeval, std::less<Timestamp::TimeDomain>, std::allocator<std::pair<const Timestamp::TimeDomain, timeval>>>={__tree<std::__value_type<Timestamp::TimeDomain, timeval>, std::__map_value_compare<Timestamp::TimeDomain, std::__value_type<Timestamp::TimeDomain, timeval>, std::less<Timestamp::TimeDomain>>, std::allocator<std::__value_type<Timestamp::TimeDomain, timeval>>>=^v{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<Timestamp::TimeDomain, timeval>, void *>>>={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{__compressed_pair<unsigned long, std::__map_value_compare<Timestamp::TimeDomain, std::__value_type<Timestamp::TimeDomain, timeval>, std::less<Timestamp::TimeDomain>>>=Q}}}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}}8"
- "v32@?0{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}8"
- "v36@?0i8{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}12"
- "v48@?0{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}}8^v40"
- "v48@?0{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}}8{dict={object=^v}}40"

```
