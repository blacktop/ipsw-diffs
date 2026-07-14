## libBasebandManager.dylib

> `/usr/lib/libBasebandManager.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__DATA_DIRTY.__objc_data`

```diff

-  __TEXT.__text: 0x228fec
-  __TEXT.__auth_stubs: 0x3350
-  __TEXT.__init_offsets: 0x160
+  __TEXT.__text: 0x22455c
+  __TEXT.__auth_stubs: 0x32b0
+  __TEXT.__init_offsets: 0x150
   __TEXT.__objc_methlist: 0x52c
-  __TEXT.__const: 0xf59f
+  __TEXT.__const: 0xf4bf
   __TEXT.__dlopen_cstrs: 0x52
-  __TEXT.__gcc_except_tab: 0x35d84
-  __TEXT.__cstring: 0x84b9
-  __TEXT.__oslogstring: 0xc18d
-  __TEXT.__unwind_info: 0xa4b8
+  __TEXT.__gcc_except_tab: 0x352c0
+  __TEXT.__cstring: 0x82ba
+  __TEXT.__oslogstring: 0xc01c
+  __TEXT.__unwind_info: 0xa388
   __TEXT.__objc_classname: 0x13f
   __TEXT.__objc_methname: 0x160f
   __TEXT.__objc_methtype: 0x12ad
   __TEXT.__objc_stubs: 0x12e0
-  __DATA_CONST.__got: 0x22f0
-  __DATA_CONST.__const: 0x2198
+  __DATA_CONST.__got: 0x22b0
+  __DATA_CONST.__const: 0x2118
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x668
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x19b8
-  __AUTH_CONST.__const: 0xecc8
-  __AUTH_CONST.__cfstring: 0x9e0
+  __AUTH_CONST.__auth_got: 0x1968
+  __AUTH_CONST.__const: 0xebf8
+  __AUTH_CONST.__cfstring: 0x9a0
   __AUTH_CONST.__objc_const: 0xa68
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x4c
-  __DATA.__data: 0x580
+  __DATA.__data: 0x538
   __DATA.__bss: 0x4d0
   __DATA.__common: 0xa
   __DATA_DIRTY.__objc_data: 0xf0
-  __DATA_DIRTY.__data: 0x630
-  __DATA_DIRTY.__common: 0xd8
-  __DATA_DIRTY.__bss: 0x2ba
+  __DATA_DIRTY.__data: 0x5d8
+  __DATA_DIRTY.__common: 0xd0
+  __DATA_DIRTY.__bss: 0x28a
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CallKit.framework/CallKit
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libprotobuf.dylib
-  Functions: 6167
-  Symbols:   10907
-  CStrings:  2841
+  Functions: 6147
+  Symbols:   10867
+  CStrings:  2817
 
Symbols:
+ GCC_except_table224
+ GCC_except_table255
+ GCC_except_table297
+ GCC_except_table299
+ GCC_except_table301
+ GCC_except_table309
+ GCC_except_table333
+ GCC_except_table336
+ GCC_except_table338
+ GCC_except_table351
+ GCC_except_table358
+ GCC_except_table367
+ GCC_except_table372
+ GCC_except_table375
+ GCC_except_table396
+ GCC_except_table409
+ GCC_except_table413
+ GCC_except_table420
+ GCC_except_table424
+ GCC_except_table435
+ GCC_except_table452
+ GCC_except_table468
+ GCC_except_table472
+ ___copy_helper_block_e8_32c35_ZTSNSt3__18weak_ptrI10BootModuleEE
+ ___destroy_helper_block_e8_32c35_ZTSNSt3__18weak_ptrI10BootModuleEE
- GCC_except_table270
- GCC_except_table288
- GCC_except_table298
- GCC_except_table300
- GCC_except_table302
- GCC_except_table332
- GCC_except_table335
- GCC_except_table337
- GCC_except_table349
- GCC_except_table354
- GCC_except_table357
- GCC_except_table364
- GCC_except_table370
- GCC_except_table398
- GCC_except_table403
- GCC_except_table406
- GCC_except_table412
- GCC_except_table464
- GCC_except_table471
- _CFUserNotificationDisplayNotice
- _TelephonyBasebandWatchdogStartWithStackshot
- _TelephonyUtilTriggerNMI
- _TelephonyUtilWriteStackshot
- __ZGVN3ctu9SingletonI21CapabilitiesOverridesS1_NS_23PthreadMutexGuardPolicyIS1_EEE9sInstanceE
- __ZN10DataModule20setDataProperty_syncEN3xpc4dictEN8dispatch5blockIU13block_pointerFviS1_EEE
- __ZN12capabilities3abs17shouldBlockResetsEv
- __ZN12capabilities3abs24kKeyDataPowerSaveEnabledE
- __ZN12capabilities3abs26kKeyDataFlowControlEnabledE
- __ZN12capabilities3abs26shouldPanicOnBasebandResetEv
- __ZN12capabilities3abs27kKeyDataAggregationProtocolE
- __ZN12capabilities3abs27kKeySupportsCMHandDetectionE
- __ZN12capabilities3abs31kKeyDataAggregationMaxSizeBytesE
- __ZN12capabilities3abs35kKeyDataAggregationDatagramMaxCountE
- __ZN12capabilities3abs39shouldTriggerStackshotOnShutdownTimeoutEv
- __ZN3ctu23PthreadMutexGuardPolicyI21CapabilitiesOverridesED1Ev
- __ZN3ctu23PthreadMutexGuardPolicyI21CapabilitiesOverridesED2Ev
- __ZN3ctu2cf6insertIPK10__CFStringS4_EEbP14__CFDictionaryT_T0_PK13__CFAllocator
- __ZN3ctu5power7manager20simulateNotificationEjb
- __ZN3ctu9SingletonI21CapabilitiesOverridesS1_NS_23PthreadMutexGuardPolicyIS1_EEE9sInstanceE
- __ZN7support2uiL17gNotificationLockE
- __ZN7support2uiL9isAllowedEv
- __ZN9Overrides13getPreferenceIbEEbRKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERT_
- __ZN9Overrides13setPreferenceIbEEbRKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEET_b
- __ZNKSt3__120__shared_ptr_pointerIP21CapabilitiesOverridesNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEE13__get_deleterERKSt9type_info
- __ZNSt3__110shared_ptrI21CapabilitiesOverridesED1B9nqe210106Ev
- __ZNSt3__110shared_ptrI21CapabilitiesOverridesED2B9nqe210106Ev
- __ZNSt3__110shared_ptrIN3ctu5power7managerEED2B9nqe210106Ev
- __ZNSt3__110unique_ptrI21CapabilitiesOverridesNS_14default_deleteIS1_EEED2B9nqe210106Ev
- __ZNSt3__110unique_ptrIZNK3ctu20SharedSynchronizableI9SimulatorE15execute_wrappedIZZNS3_26registerEventHandlers_syncEvENK3$_0clEN8dispatch13group_sessionEN3xpc4dictEEUlvE_EEvOT_EUlvE_NS_14default_deleteISE_EEED1B9nqe210106Ev
- __ZNSt3__110unique_ptrIZZN9Simulator26registerEventHandlers_syncEvENK3$_0clEN8dispatch13group_sessionEN3xpc4dictEEUlvE_NS_14default_deleteIS7_EEED1B9nqe210106Ev
- __ZNSt3__120__shared_ptr_pointerIP21CapabilitiesOverridesNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEE16__on_zero_sharedEv
- __ZNSt3__120__shared_ptr_pointerIP21CapabilitiesOverridesNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEE21__on_zero_shared_weakEv
- __ZNSt3__120__shared_ptr_pointerIP21CapabilitiesOverridesNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEED0Ev
- __ZNSt3__120__shared_ptr_pointerIP21CapabilitiesOverridesNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEED1Ev
- __ZNSt3__16vectorImNS_9allocatorImEEE20__throw_length_errorB9nqe210106Ev
- __ZTINSt3__120__shared_ptr_pointerIP21CapabilitiesOverridesNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEEE
- __ZTSNSt3__110shared_ptrI21CapabilitiesOverridesE27__shared_ptr_default_deleteIS1_S1_EE
- __ZTSNSt3__120__shared_ptr_pointerIP21CapabilitiesOverridesNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEEE
- __ZTVNSt3__120__shared_ptr_pointerIP21CapabilitiesOverridesNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEEE
- __ZZN9ABMServer10getProfileEvE11sABMProfile
- __ZZN9ABMServer10getProfileEvE9onceToken
- ____ZN19QMITransportService13enterLowPowerEN8dispatch13group_sessionE_block_invoke_3
- ____ZN9ABMServer10getProfileEv_block_invoke
- _dispatch_semaphore_signal
- _dispatch_semaphore_wait
CStrings:
+ "-l 0xffffffff -v 0 -N"
+ "AppleBasebandManager-AppleBasebandServices_Manager-1420"
+ "AppleBasebandServices_Manager-1420"
- "#D     %s"
- "#D Enumerating HealthEvents to be written to disk:"
- "#D HealthEvents dictionary representation to be written to disk: %@"
- "#I Simulated notification: %s"
- "#I Triggering stackshot"
- "#I Triggering stackshot  -- done"
- "#I blocking reset until user signals"
- ", reason "
- "-l 0xffffffff -v 99 -N"
- "AppleBasebandManager-AppleBasebandServices_Manager-1419"
- "AppleBasebandServices_Manager-1419"
- "Baseband Firmware Not Found"
- "Baseband Hard-Reset: "
- "Capability %s returning overridden value"
- "Did you forget to check update baseband or set permissions if you used a custom build?"
- "Incompatible Baseband firmware."
- "Invalid property type"
- "OK"
- "PANIC: %s"
- "PanicString"
- "QMI low power, please file radar in Purple Telephony - 1.0"
- "ServiceManager sleep timeout"
- "ServiceManager wake timeout"
- "Triggering stackshot, goes with "
- "Unexpected behavior may occur. Please upgrade to a newer firmware."
- "Unsupported ABM profile, check your plist!"
- "com.apple.telephony.capabilities"
```
