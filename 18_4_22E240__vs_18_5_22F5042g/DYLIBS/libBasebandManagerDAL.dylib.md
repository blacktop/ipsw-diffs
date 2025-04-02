## libBasebandManagerDAL.dylib

> `/usr/lib/libBasebandManagerDAL.dylib`

```diff

 1249.1.0.0.0
-  __TEXT.__text: 0x11803c
-  __TEXT.__auth_stubs: 0x2300
-  __TEXT.__init_offsets: 0xb8
+  __TEXT.__text: 0x11aa1c
+  __TEXT.__auth_stubs: 0x23c0
+  __TEXT.__init_offsets: 0xc4
   __TEXT.__objc_methlist: 0x274
-  __TEXT.__const: 0x659f
-  __TEXT.__gcc_except_tab: 0x1b12c
-  __TEXT.__oslogstring: 0x55d7
-  __TEXT.__cstring: 0x2f61
-  __TEXT.__unwind_info: 0x54f0
+  __TEXT.__const: 0x6677
+  __TEXT.__gcc_except_tab: 0x1b758
+  __TEXT.__oslogstring: 0x576c
+  __TEXT.__cstring: 0x30c8
+  __TEXT.__unwind_info: 0x55d8
   __TEXT.__objc_classname: 0x68
   __TEXT.__objc_methname: 0x626
   __TEXT.__objc_methtype: 0x1289
   __TEXT.__objc_stubs: 0x500
-  __DATA_CONST.__got: 0x11e0
-  __DATA_CONST.__const: 0x1010
+  __DATA_CONST.__got: 0x1210
+  __DATA_CONST.__const: 0x1030
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x218
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x1190
-  __AUTH_CONST.__const: 0x8bb8
-  __AUTH_CONST.__cfstring: 0x2c0
+  __AUTH_CONST.__auth_got: 0x11f0
+  __AUTH_CONST.__const: 0x8c28
+  __AUTH_CONST.__cfstring: 0x300
   __AUTH_CONST.__objc_const: 0x418
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x1c
-  __DATA.__data: 0x6a8
-  __DATA.__common: 0x20
-  __DATA.__bss: 0x1c8
-  __DATA_DIRTY.__data: 0x78
+  __DATA.__data: 0x740
+  __DATA.__common: 0x28
+  __DATA.__bss: 0x1f8
+  __DATA_DIRTY.__data: 0x80
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3160
-  Symbols:   4697
-  CStrings:  1188
+  Functions: 3172
+  Symbols:   4730
+  CStrings:  1210
 
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
+ "Baseband Hard-Reset: "
+ "Capability %s returning overridden value"
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
- "Default pattern masks will be used"

```
