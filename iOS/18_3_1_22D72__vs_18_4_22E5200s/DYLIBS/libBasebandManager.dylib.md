## libBasebandManager.dylib

> `/usr/lib/libBasebandManager.dylib`

```diff

-1220.0.0.0.0
-  __TEXT.__text: 0x1fff8c
-  __TEXT.__auth_stubs: 0x31e0
-  __TEXT.__init_offsets: 0x124
-  __TEXT.__objc_methlist: 0x270
-  __TEXT.__gcc_except_tab: 0x31078
-  __TEXT.__const: 0xcbab
-  __TEXT.__cstring: 0x6d83
-  __TEXT.__oslogstring: 0xaefb
-  __TEXT.__unwind_info: 0x9408
+1245.0.0.0.0
+  __TEXT.__text: 0x1f8c70
+  __TEXT.__auth_stubs: 0x32a0
+  __TEXT.__init_offsets: 0x134
+  __TEXT.__objc_methlist: 0x46c
+  __TEXT.__const: 0xcc8b
+  __TEXT.__gcc_except_tab: 0x31c78
+  __TEXT.__cstring: 0x6f9f
+  __TEXT.__oslogstring: 0xb090
+  __TEXT.__unwind_info: 0x99b8
   __TEXT.__objc_classname: 0x109
   __TEXT.__objc_methname: 0x1187
-  __TEXT.__objc_methtype: 0x1853
+  __TEXT.__objc_methtype: 0x1753
   __TEXT.__objc_stubs: 0xfa0
-  __DATA_CONST.__got: 0x2038
-  __DATA_CONST.__const: 0x1d90
+  __DATA_CONST.__got: 0x20a8
+  __DATA_CONST.__const: 0x1e10
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x470
+  __DATA_CONST.__objc_selrefs: 0x568
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x1900
-  __AUTH_CONST.__const: 0xfe98
-  __AUTH_CONST.__cfstring: 0x6c0
-  __AUTH_CONST.__objc_const: 0xcc0
+  __AUTH_CONST.__auth_got: 0x1960
+  __AUTH_CONST.__const: 0xff28
+  __AUTH_CONST.__cfstring: 0x700
+  __AUTH_CONST.__objc_const: 0x918
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x40
-  __DATA.__data: 0x5a0
+  __DATA.__data: 0x5e8
   __DATA.__bss: 0x4c8
   __DATA.__common: 0x21
   __DATA_DIRTY.__objc_data: 0xf0
-  __DATA_DIRTY.__data: 0x4f8
-  __DATA_DIRTY.__bss: 0x1ea
-  __DATA_DIRTY.__common: 0xc0
+  __DATA_DIRTY.__data: 0x550
+  __DATA_DIRTY.__common: 0xc8
+  __DATA_DIRTY.__bss: 0x21a
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CallKit.framework/CallKit
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libprotobuf.dylib
-  Functions: 5787
-  Symbols:   8261
-  CStrings:  2454
+  Functions: 5893
+  Symbols:   8644
+  CStrings:  2481
 
Symbols:
+ _CFUserNotificationCreate
+ _CFUserNotificationDisplayNotice
+ _CFUserNotificationReceiveResponse
+ _TelephonyBasebandWatchdogStartWithStackshot
+ _TelephonyUtilTriggerNMI
+ _TelephonyUtilWriteStackshot
+ __ZGVN3ctu9SingletonI21CapabilitiesOverridesS1_NS_23PthreadMutexGuardPolicyIS1_EEE9sInstanceE
+ __ZN10DataModule20setDataProperty_syncEN3xpc4dictEN8dispatch5blockIU13block_pointerFviS1_EEE
+ __ZN12capabilities3abs17shouldBlockResetsEv
+ __ZN12capabilities3abs24kKeyDataPowerSaveEnabledE
+ __ZN12capabilities3abs26kKeyDataFlowControlEnabledE
+ __ZN12capabilities3abs26shouldPanicOnBasebandResetEv
+ __ZN12capabilities3abs27kKeyDataAggregationProtocolE
+ __ZN12capabilities3abs27kKeySupportsCMHandDetectionE
+ __ZN12capabilities3abs31kKeyDataAggregationMaxSizeBytesE
+ __ZN12capabilities3abs35kKeyDataAggregationDatagramMaxCountE
+ __ZN12capabilities3abs39shouldTriggerStackshotOnShutdownTimeoutEv
+ __ZN12capabilities4diag12supportsQDSSEv
+ __ZN3ctu5power7manager20simulateNotificationEjb
+ __ZN3ctu9SingletonI21CapabilitiesOverridesS1_NS_23PthreadMutexGuardPolicyIS1_EEE9sInstanceE
+ __ZNSt3__117bad_function_callD0Ev
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTINSt3__117bad_function_callE
+ __ZTVNSt3__117bad_function_callE
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _kCFUserNotificationAlertHeaderKey
+ _kCFUserNotificationAlertMessageKey
+ _kCFUserNotificationDefaultButtonTitleKey
- __ZNSt9exceptionD2Ev
CStrings:
+ "#D     %s"
+ "#D Enumerating HealthEvents to be written to disk:"
+ "#D HealthEvents dictionary representation to be written to disk: %@"
+ "#I Simulated notification: %s"
+ "#I Triggering stackshot"
+ "#I Triggering stackshot  -- done"
+ "#I blocking reset until user signals"
+ ", reason "
+ "-l 0xffffffff -v 99 -N"
+ "@40@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}16"
+ "AppleBasebandManager-AppleBasebandServices_Manager-1245"
+ "AppleBasebandServices_Manager-1245"
+ "B136@0:8{NotificationInfo={basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}}16@88{CallBackData=@?{queue={object=^{dispatch_object_s}}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}}96"
+ "Baseband Firmware Not Found"
+ "Baseband Hard-Reset: "
+ "Capability %s returning overridden value"
+ "Did you forget to check update baseband or set permissions if you used a custom build?"
+ "Incompatible Baseband firmware."
+ "Invalid property type"
+ "No ResetInfoRegexPatterns entry found in ABMProperties, so the default patterns will be used"
+ "OK"
+ "PANIC: %s"
+ "QMI low power, please file radar in Purple Telephony - 1.0"
+ "ResetInfoReasonRegexPattern"
+ "ResetInfoReasonRegexPatternMask"
+ "ResetInfoRegexPatterns"
+ "ServiceManager sleep timeout"
+ "ServiceManager wake timeout"
+ "Triggering stackshot, goes with "
+ "Unexpected behavior may occur. Please upgrade to a newer firmware."
+ "Unsupported ABM profile, check your plist!"
+ "baseband crash"
+ "com.apple.telephony.capabilities"
+ "v116@0:8i16{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}20{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}44{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}68{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}92"
+ "v128@0:8{NotificationInfo={basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}}16{CallBackData=@?{queue={object=^{dispatch_object_s}}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}}88"
+ "v32@?0{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}8"
+ "v36@?0i8{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}12"
+ "v44@0:8i16{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}20"
+ "v48@?0{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}}8{dict={object=^v}}40"
+ "v48@?0{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}8{CFSharedRef<const __CFDictionary>=^{__CFDictionary}}32{block<void (^)()>=@?}40"
+ "{vector<std::string, std::allocator<std::string>>=^v^v{__compressed_pair<std::string *, std::allocator<std::string>>=^v}}64@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}16{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}40"
- "-l 0xffffffdf -v 0 -N"
- "@40@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}16"
- "AppleBasebandManager-AppleBasebandServices_Manager-1220"
- "AppleBasebandServices_Manager-1220"
- "B136@0:8{NotificationInfo={basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}}16@88{CallBackData=@?{queue={object=^{dispatch_object_s}}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}}96"
- "Default pattern masks will be used"
- "file size cannot be 0"
- "v116@0:8i16{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}20{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}44{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}68{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}92"
- "v128@0:8{NotificationInfo={basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}}16{CallBackData=@?{queue={object=^{dispatch_object_s}}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}}88"
- "v32@?0{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}8"
- "v36@?0i8{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}12"
- "v44@0:8i16{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}20"
- "v48@?0{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}}8{dict={object=^v}}40"
- "v48@?0{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}8{CFSharedRef<const __CFDictionary>=^{__CFDictionary}}32{block<void (^)()>=@?}40"
- "{vector<std::string, std::allocator<std::string>>=^v^v{__compressed_pair<std::string *, std::allocator<std::string>>=^v}}64@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}16{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}40"

```
