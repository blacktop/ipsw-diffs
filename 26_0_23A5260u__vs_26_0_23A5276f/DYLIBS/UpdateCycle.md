## UpdateCycle

> `/System/Library/PrivateFrameworks/UpdateCycle.framework/UpdateCycle`

```diff

-9060.0.0.0.0
-  __TEXT.__text: 0x974
-  __TEXT.__auth_stubs: 0x170
+9073.0.0.0.0
+  __TEXT.__text: 0x1140
+  __TEXT.__auth_stubs: 0x270
   __TEXT.__const: 0x40
-  __DATA_CONST.__got: 0x8
+  __TEXT.__cstring: 0x86
+  __TEXT.__objc_methname: 0x73
+  __TEXT.__objc_stubs: 0xc0
+  __DATA_CONST.__got: 0x18
+  __DATA_CONST.__const: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __AUTH_CONST.__auth_got: 0xb8
-  __AUTH_CONST.__const: 0x38
+  __DATA_CONST.__objc_selrefs: 0x30
+  __AUTH_CONST.__auth_got: 0x140
+  __AUTH_CONST.__const: 0x58
+  __AUTH_CONST.__cfstring: 0x60
+  __AUTH.__data: 0x8
+  __DATA.__bss: 0x10
   __DATA_DIRTY.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 76C87C0B-11F2-33AA-B163-FE3EFEC6F9D8
-  Functions: 42
-  Symbols:   86
-  CStrings:  0
+  UUID: 530EE8ED-578F-3114-9778-F5D99E805552
+  Functions: 49
+  Symbols:   132
+  CStrings:  15
 
Symbols:
+ _OBJC_CLASS_$_NSString
+ _OBJC_CLASS_$_NSUserDefaults
+ _UCDebugTracingModeCheck
+ __NSConcreteGlobalBlock
+ __ZL25initDebugTracingModeCheckv
+ __ZL27debugTracingModeTracepointsv
+ __ZL41debugTracingModeTracepointsWithCallstacksv
+ __ZN2UC10DriverCore18continueProcessingEv
+ __ZN2UC10MakeMethodIXadL_ZNS_10DriverCore12timerHandlerEvEEE4callEPv
+ __ZN2UC10MakeMethodIXadL_ZNS_10DriverCore13returnHandlerEvEEE4callEPv
+ __ZN2UC10MakeMethodIXadL_ZNS_10DriverCore13signalHandlerEvEEE4callEPv
+ __ZN2UC11SignalsCore10notifyLostEv
+ __ZN2UC11SignalsCore16acceptProcessingEybb
+ __ZN2UC16LoopTapCFRunLoop7onEntryEP19__CFRunLoopObservermPv
+ __ZN2UC16LoopTapCFRunLoop7onTimerEP12__CFMachPortPvlS3_
+ __ZN2UC16LoopTapCFRunLoop8onSignalEPv
+ __ZN2UCL60ERROR_NESTED_RUN_LOOP_IS_NOT_SUPPORTED_DURING_THIS_OPERATIONEv
+ __ZZN12_GLOBAL__N_116immutableOptionsEvE4once
+ __ZZN12_GLOBAL__N_116immutableOptionsEvE7options.2
+ ___CFConstantStringClassReference
+ ____ZN12_GLOBAL__N_116immutableOptionsEv_block_invoke
+ ___block_descriptor_32_e5_v8?0l
+ ___block_literal_global
+ __os_crash
+ _atoi
+ _dispatch_once
+ _dyld_program_sdk_at_least
+ _getenv
+ _getppid
+ _kdebug_trace
+ _objc_alloc
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend
+ _objc_msgSend$addSuiteNamed:
+ _objc_msgSend$dictionaryRepresentation
+ _objc_msgSend$initWithSuiteName:
+ _objc_msgSend$intValue
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$stringWithUTF8String:
+ _objc_release
+ _objc_release_x19
+ _objc_release_x20
+ _objc_release_x21
+ _objc_retain_x20
+ _os_variant_allows_internal_security_policies
+ _os_variant_has_internal_diagnostics
- __ZN2UC10DriverCore19_continueProcessingEv
- __ZN2UC10MakeMethodIXadL_ZNS_10DriverCore13_timerHandlerEvEEE4callEPv
- __ZN2UC10MakeMethodIXadL_ZNS_10DriverCore14_returnHandlerEvEEE4callEPv
- __ZN2UC10MakeMethodIXadL_ZNS_10DriverCore14_signalHandlerEvEEE4callEPv
- __ZN2UC16LoopTapCFRunLoop8_onEntryEP19__CFRunLoopObservermPv
- __ZN2UC16LoopTapCFRunLoop8_onTimerEP12__CFMachPortPvlS3_
- __ZN2UC16LoopTapCFRunLoop9_onSignalEPv
CStrings:
+ "Nested run loop is not supported during this operation."
+ "UCDebugTracing"
+ "UpdateCycleTracing"
+ "addSuiteNamed:"
+ "com.apple.UIKit"
+ "com.apple.UpdateCycle"
+ "dictionaryRepresentation"
+ "initWithSuiteName:"
+ "intValue"
+ "objectForKeyedSubscript:"
+ "stringWithUTF8String:"
+ "v8@?0"

```
