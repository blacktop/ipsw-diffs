## libBasebandManagerICE.dylib

> `/usr/lib/libBasebandManagerICE.dylib`

```diff

 1249.1.0.0.0
-  __TEXT.__text: 0x1f6c78
-  __TEXT.__auth_stubs: 0x3260
-  __TEXT.__init_offsets: 0x144
+  __TEXT.__text: 0x1f9840
+  __TEXT.__auth_stubs: 0x3320
+  __TEXT.__init_offsets: 0x150
   __TEXT.__objc_methlist: 0x46c
-  __TEXT.__const: 0xccb7
-  __TEXT.__gcc_except_tab: 0x320e8
-  __TEXT.__oslogstring: 0xb1d2
-  __TEXT.__cstring: 0x6d7a
-  __TEXT.__unwind_info: 0x99d0
+  __TEXT.__const: 0xcda7
+  __TEXT.__gcc_except_tab: 0x32750
+  __TEXT.__oslogstring: 0xb367
+  __TEXT.__cstring: 0x6f55
+  __TEXT.__unwind_info: 0x9ac8
   __TEXT.__objc_classname: 0x109
   __TEXT.__objc_methname: 0x1187
   __TEXT.__objc_methtype: 0x1753
   __TEXT.__objc_stubs: 0xfa0
-  __DATA_CONST.__got: 0x2160
-  __DATA_CONST.__const: 0x1ba8
+  __DATA_CONST.__got: 0x2190
+  __DATA_CONST.__const: 0x1bc8
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x568
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x1940
+  __AUTH_CONST.__auth_got: 0x19a0
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x10210
-  __AUTH_CONST.__cfstring: 0x760
+  __AUTH_CONST.__const: 0x10280
+  __AUTH_CONST.__cfstring: 0x7a0
   __AUTH_CONST.__objc_const: 0x918
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x40
-  __DATA.__data: 0x5b8
+  __DATA.__data: 0x600
   __DATA.__common: 0x29
   __DATA_DIRTY.__objc_data: 0xf0
-  __DATA_DIRTY.__data: 0x500
-  __DATA_DIRTY.__common: 0xb0
-  __DATA_DIRTY.__bss: 0x21a
+  __DATA_DIRTY.__data: 0x558
+  __DATA_DIRTY.__common: 0xb8
+  __DATA_DIRTY.__bss: 0x24a
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CallKit.framework/CallKit
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libprotobuf.dylib
-  Functions: 5902
-  Symbols:   8661
-  CStrings:  2444
+  Functions: 5914
+  Symbols:   8694
+  CStrings:  2468
 
Symbols:
+ _CFUserNotificationCreate
+ _CFUserNotificationDisplayNotice
+ _CFUserNotificationReceiveResponse
+ _TelephonyBasebandWatchdogStartWithStackshot
+ _TelephonyUtilTriggerNMI
+ _TelephonyUtilWriteStackshot
+ __ZGVN3ctu9SingletonI21CapabilitiesOverridesS1_NS_23PthreadMutexGuardPolicyIS1_EEE9sInstanceE
+ __ZN12capabilities3abs17shouldBlockResetsEv
+ __ZN12capabilities3abs26shouldPanicOnBasebandResetEv
+ __ZN12capabilities3abs27kKeySupportsCMHandDetectionE
+ __ZN12capabilities3abs39shouldTriggerStackshotOnShutdownTimeoutEv
+ __ZN3ctu5power7manager20simulateNotificationEjb
+ __ZN3ctu9SingletonI21CapabilitiesOverridesS1_NS_23PthreadMutexGuardPolicyIS1_EEE9sInstanceE
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _kCFUserNotificationAlertHeaderKey
+ _kCFUserNotificationAlertMessageKey
+ _kCFUserNotificationDefaultButtonTitleKey
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
+ "Baseband Firmware Not Found"
+ "Baseband Hard-Reset: "
+ "Capability %s returning overridden value"
+ "Did you forget to check update baseband or set permissions if you used a custom build?"
+ "Incompatible Baseband firmware."
+ "No ResetInfoRegexPatterns entry found in ABMProperties, so the default patterns will be used"
+ "OK"
+ "PANIC: %s"
+ "ResetInfoReasonRegexPattern"
+ "ResetInfoReasonRegexPatternMask"
+ "ResetInfoRegexPatterns"
+ "ServiceManager sleep timeout"
+ "ServiceManager wake timeout"
+ "Triggering stackshot, goes with "
+ "Unexpected behavior may occur. Please upgrade to a newer firmware."
+ "Unsupported ABM profile, check your plist!"
+ "com.apple.telephony.capabilities"
- "-l 0xffffffdf -v 0 -N"
- "Default pattern masks will be used"

```
