## libBasebandManagerICE.dylib

> `/usr/lib/libBasebandManagerICE.dylib`

```diff

 1183.0.0.0.0
-  __TEXT.__text: 0x1ee5c0
-  __TEXT.__auth_stubs: 0x3220
-  __TEXT.__init_offsets: 0x120
+  __TEXT.__text: 0x1eb84c
+  __TEXT.__auth_stubs: 0x3160
+  __TEXT.__init_offsets: 0x114
   __TEXT.__objc_methlist: 0x238
-  __TEXT.__const: 0xc6a7
-  __TEXT.__gcc_except_tab: 0x2fd1c
-  __TEXT.__oslogstring: 0xa6c7
-  __TEXT.__cstring: 0x6b9e
-  __TEXT.__unwind_info: 0x90d0
+  __TEXT.__const: 0xc5c7
+  __TEXT.__gcc_except_tab: 0x2f6d0
+  __TEXT.__oslogstring: 0xa532
+  __TEXT.__cstring: 0x69c3
+  __TEXT.__unwind_info: 0x8fd0
   __TEXT.__objc_classname: 0xdb
   __TEXT.__objc_methname: 0x10e9
   __TEXT.__objc_methtype: 0x170a
   __TEXT.__objc_stubs: 0xf00
-  __DATA_CONST.__got: 0x2028
-  __DATA_CONST.__const: 0x1a50
+  __DATA_CONST.__got: 0x1ff8
+  __DATA_CONST.__const: 0x1a30
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x440
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x1920
-  __AUTH_CONST.__const: 0xfa48
-  __AUTH_CONST.__cfstring: 0x7a0
+  __AUTH_CONST.__auth_got: 0x18c0
+  __AUTH_CONST.__const: 0xf9d8
+  __AUTH_CONST.__cfstring: 0x760
   __AUTH_CONST.__objc_const: 0xb08
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x30
-  __DATA.__data: 0x5a0
+  __DATA.__data: 0x558
   __DATA.__common: 0x29
   __DATA_DIRTY.__objc_data: 0xf0
-  __DATA_DIRTY.__data: 0x4a8
-  __DATA_DIRTY.__common: 0xb8
-  __DATA_DIRTY.__bss: 0x230
+  __DATA_DIRTY.__data: 0x450
+  __DATA_DIRTY.__common: 0xb0
+  __DATA_DIRTY.__bss: 0x200
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libprotobuf.dylib
-  Functions: 5622
-  Symbols:   8057
-  CStrings:  2343
+  Functions: 5610
+  Symbols:   8025
+  CStrings:  2319
 
Symbols:
- _CFUserNotificationCreate
- _CFUserNotificationDisplayNotice
- _CFUserNotificationReceiveResponse
- _TelephonyBasebandWatchdogStartWithStackshot
- _TelephonyUtilTriggerNMI
- _TelephonyUtilWriteStackshot
- __ZGVN3ctu9SingletonI21CapabilitiesOverridesS1_NS_23PthreadMutexGuardPolicyIS1_EEE9sInstanceE
- __ZN12capabilities3abs17shouldBlockResetsEv
- __ZN12capabilities3abs26shouldPanicOnBasebandResetEv
- __ZN12capabilities3abs27kKeySupportsCMHandDetectionE
- __ZN12capabilities3abs39shouldTriggerStackshotOnShutdownTimeoutEv
- __ZN3ctu5power7manager20simulateNotificationEjb
- __ZN3ctu9SingletonI21CapabilitiesOverridesS1_NS_23PthreadMutexGuardPolicyIS1_EEE9sInstanceE
- _dispatch_semaphore_signal
- _dispatch_semaphore_wait
- _kCFUserNotificationAlertHeaderKey
- _kCFUserNotificationAlertMessageKey
- _kCFUserNotificationDefaultButtonTitleKey
CStrings:
+ "-l 0xffffffdf -v 0 -N"
+ "Default pattern masks will be used"
- "#D     %!s(MISSING)"
- "#D Enumerating HealthEvents to be written to disk:"
- "#D HealthEvents dictionary representation to be written to disk: %!@(MISSING)"
- "#I Simulated notification: %!s(MISSING)"
- "#I Triggering stackshot"
- "#I Triggering stackshot  -- done"
- "#I blocking reset until user signals"
- ", reason "
- "-l 0xffffffff -v 99 -N"
- "Baseband Firmware Not Found"
- "Baseband Hard-Reset: "
- "Capability %!s(MISSING) returning overridden value"
- "Did you forget to check update baseband or set permissions if you used a custom build?"
- "Incompatible Baseband firmware."
- "No ResetInfoRegexPatterns entry found in ABMProperties, so the default patterns will be used"
- "OK"
- "PANIC: %!s(MISSING)"
- "ResetInfoReasonRegexPattern"
- "ResetInfoReasonRegexPatternMask"
- "ResetInfoRegexPatterns"
- "ServiceManager sleep timeout"
- "ServiceManager wake timeout"
- "Triggering stackshot, goes with "
- "Unexpected behavior may occur. Please upgrade to a newer firmware."
- "Unsupported ABM profile, check your plist!"
- "com.apple.telephony.capabilities"

```
