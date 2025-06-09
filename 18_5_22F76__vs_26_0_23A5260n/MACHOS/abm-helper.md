## abm-helper

> `/System/Library/PrivateFrameworks/ABMHelper.framework/Support/abm-helper`

```diff

-1249.1.0.0.0
-  __TEXT.__text: 0x29b0
-  __TEXT.__auth_stubs: 0x550
-  __TEXT.__const: 0x1ab
-  __TEXT.__gcc_except_tab: 0x184
-  __TEXT.__cstring: 0x64
-  __TEXT.__oslogstring: 0xf2
+1371.0.1.0.0
+  __TEXT.__text: 0xa30
+  __TEXT.__auth_stubs: 0x240
+  __TEXT.__init_offsets: 0x4
+  __TEXT.__gcc_except_tab: 0x50
+  __TEXT.__const: 0x10
+  __TEXT.__cstring: 0x3f
+  __TEXT.__oslogstring: 0xf1
   __TEXT.__objc_classname: 0x1
-  __TEXT.__unwind_info: 0x130
-  __DATA_CONST.__auth_got: 0x2b0
-  __DATA_CONST.__got: 0x88
+  __TEXT.__unwind_info: 0x90
+  __DATA_CONST.__auth_got: 0x128
+  __DATA_CONST.__got: 0x28
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x210
+  __DATA_CONST.__const: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__data: 0x4
-  __DATA.__bss: 0x1
+  __DATA.__data: 0x54
+  __DATA.__bss: 0x9
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libTelephonyDebugDynamic.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  - /usr/lib/libobjc.A.dylib
-  UUID: 7D72CE5A-700F-3745-A3DE-913784D3BFD9
-  Functions: 42
-  Symbols:   194
-  CStrings:  15
+  UUID: 041D4C77-D5C4-3B2D-9207-7CFBB90F23C8
+  Functions: 12
+  Symbols:   163
+  CStrings:  12
 
Symbols:
+ _CFBooleanGetTypeID
+ _CFGetTypeID
+ _CFRelease
+ _TelephonyBasebandWatchdogStartWithStackshot
+ _TelephonyBasebandWatchdogStop
+ __ZN12capabilities3abs27kKeySupportsCMHandDetectionE
+ __ZN3abm12HelperServer6createEv
+ __ZN3ctu2cf12MakeCFStringC1EPKc
+ __ZN3ctu2cf12MakeCFStringD1Ev
+ __ZN3ctu2cf13plist_adapterC1EPK10__CFStringS4_
+ __ZN3ctu2cf13plist_adapterD1Ev
+ __ZN3ctu2cf6assignERbPK11__CFBoolean
+ ___CFConstantStringClassReference
+ _kCFPreferencesCurrentUser
+ _pthread_mutex_lock
+ _pthread_mutex_unlock
- __ZN12capabilities3abs13ABMLogEnabledEv
- __ZN3abm12HelperServer6createENSt3__110shared_ptrIN3ctu9LogServerEEE
- __ZN3abm5trace14kScratchFolderE
- __ZN3ctu12StaticLoggerC1ENS_12OsLogContextERKNSt3__110shared_ptrINS_9LogServerEEE
- __ZN3ctu12StaticLoggerC1Ev
- __ZN3ctu12StaticLoggerD1Ev
- __ZN3ctu16LoggerCommonBaseaSERKS0_
- __ZN3ctu9LogServer5closeEv
- __ZN3ctu9LogServer5startEv
- __ZN3ctu9LogServer6createERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
- __ZN3ctu9LogServer9addWriterENSt3__110shared_ptrINS_9LogWriterEEE
- __ZN3ctu9LogWriter13getFullConfigEv
- __ZN3ctu9LogWriter15getSimpleConfigEv
- __ZN3ctu9LogWriter5flushEN8dispatch13group_sessionE
- __ZN3ctu9LogWriter5writeENSt3__110shared_ptrINS_10LogMessageEEE
- __ZN3ctulsERNSt3__113basic_ostreamIcNS0_11char_traitsIcEEEENS_8LogLevelE
- __ZNK3ctu9LogServer5flushEv
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEmc
- __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE3putEc
- __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE5flushEv
- __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE6sentryC1ERS3_
- __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE6sentryD1Ev
- __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEED2Ev
- __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEd
- __ZNSt3__114basic_ofstreamIcNS_11char_traitsIcEEE4openEPKcj
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEEC2Ev
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEED2Ev
- __ZNSt3__18ios_base33__set_badbit_and_consider_rethrowEv
- __ZTIN3ctu9LogWriterE
- __ZTTNSt3__114basic_ofstreamIcNS_11char_traitsIcEEEE
- __ZTTNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE
- __ZTVN10__cxxabiv121__vmi_class_type_infoE
- __ZTVN3ctu9LogWriterE
- __ZTVNSt3__114basic_ofstreamIcNS_11char_traitsIcEEEE
- __ZTVNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEE
- __ZTVNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE
- ___cxa_guard_abort
- _dispatch_async_and_wait
- _dispatch_barrier_async_f
- _dispatch_group_wait
- _dispatch_queue_create
- _dispatch_sync
- _getprogname
- _memcpy
- _memmove
- _memset
- _objc_msgSend
CStrings:
+ "_set_user_dir_suffix failed!"
- ".log"
- "FlatFileLogWriter"
- "_set_user_dir_suffix failed!\n"
- "basic_string"

```
