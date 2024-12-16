## ABMHelper

> `/System/Library/PrivateFrameworks/ABMHelper.framework/ABMHelper`

```diff

-1211.0.0.0.0
-  __TEXT.__text: 0x13aef4
-  __TEXT.__auth_stubs: 0x2480
-  __TEXT.__init_offsets: 0xb8
+1218.0.0.0.0
+  __TEXT.__text: 0x13dca0
+  __TEXT.__auth_stubs: 0x2500
+  __TEXT.__init_offsets: 0xc0
   __TEXT.__objc_methlist: 0x14
-  __TEXT.__gcc_except_tab: 0x18528
-  __TEXT.__const: 0x5f22
-  __TEXT.__cstring: 0x6566
-  __TEXT.__oslogstring: 0x8903
-  __TEXT.__unwind_info: 0x5b78
+  __TEXT.__gcc_except_tab: 0x18c00
+  __TEXT.__const: 0x6032
+  __TEXT.__cstring: 0x6921
+  __TEXT.__oslogstring: 0x8a84
+  __TEXT.__unwind_info: 0x5c48
   __TEXT.__objc_classname: 0x16
   __TEXT.__objc_methname: 0x5e6
   __TEXT.__objc_methtype: 0x28
   __TEXT.__objc_stubs: 0x9c0
-  __DATA_CONST.__got: 0x5b0
-  __DATA_CONST.__const: 0x1fc8
+  __DATA_CONST.__got: 0x5c8
+  __DATA_CONST.__const: 0x1fe0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x270
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x1258
-  __AUTH_CONST.__const: 0x7e50
-  __AUTH_CONST.__cfstring: 0x7a0
+  __AUTH_CONST.__auth_got: 0x1298
+  __AUTH_CONST.__const: 0x7ea0
+  __AUTH_CONST.__cfstring: 0x820
   __AUTH_CONST.__objc_const: 0x90
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28
-  __DATA.__data: 0x3a0
+  __DATA.__data: 0x430
   __DATA.__common: 0x20
   __DATA.__bss: 0x8
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
-  Symbols:   4770
-  CStrings:  2006
+  Functions: 3504
+  Symbols:   4797
+  CStrings:  2042
 
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
+ __ZN3abm18kKeyLogDumpHistoryE
+ __ZN3abm22kCommandQueryLogDumpDBE
+ __ZN3abm26kKeyTracePeakBandwidthMbpsE
+ __ZN3abm5trace11TraceReader20updateTraceBandwidthEj
+ __ZN3abm5trace11TraceReader6createENSt3__110shared_ptrIN3ctu9LogServerEEERKN8dispatch5queueEPKcRKN19TraceFileCollection10ParametersESG_N5trace17LiveFilterSettingEN21TraceDataRateObserver10ParametersE
+ __ZN3ctu9SingletonI21CapabilitiesOverridesS1_NS_23PthreadMutexGuardPolicyIS1_EEE9sInstanceE
+ __ZN8INTTrace25setPropBandwidthMbps_syncEN8dispatch5groupENSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEES8_
+ __ZN8defaults7bbtrace14bandwidth_mbpsEv
- __ZN3abm5trace11TraceReader6createENSt3__110shared_ptrIN3ctu9LogServerEEERKN8dispatch5queueEPKcRKN19TraceFileCollection10ParametersESG_N5trace17LiveFilterSettingE
CStrings:
+ " Mbps"
+ "#I Creating Trace Command Driver"
+ "#I Peak bandwidth already set to : %u"
+ "#I Setting peak bandwidth from %d Mbps to %d Mbps"
+ "#I Showing notification: %s"
+ "#I error=%d, responseFlags=0x%lx"
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
+ "Failed to get peak bandwidth property"
+ "Failed to set peak bandwidth property"
+ "Failed to start trace reader during sleep exit"
+ "Failure to handle app crash"
+ "Integrity check for DMC file found an issue. Please file a radar under Purple ETL"
+ "Invalid input trace bandwidth - %u Mbps"
+ "Log Dump History"
+ "Mode has changed. Please, reboot the device"
+ "No ResetInfoRegexPatterns entry found in ABMProperties, so the default patterns will be used"
+ "OK"
+ "Peak Bandwidth (Mbps) : "
+ "PeakBandwidthMbps"
+ "Reboot the device before continuing to use the baseband trace"
+ "ResetInfoReasonRegexPattern"
+ "ResetInfoReasonRegexPatternMask"
+ "ResetInfoRegexPatterns"
+ "Resetting the baseband to apply your change"
+ "Restart the device before continuing to use DIAG trace"
+ "Restart the device before continuing to use the baseband trace"
+ "To control notifications please go to:\n\nSettings > Carrier Settings > Baseband Manager > Logging Settings > Radar Notifications"
+ "Trace is disabled. Skip snapshot processing"
+ "Watchdog timed out"
+ "com.apple.telephony.capabilities"
+ "kCommandQueryLogDumpDB"
- "#I Trace Command Driver is creating!"
- "Default pattern masks will be used"
- "Failed to open TRACE transport during sleep exit"
- "Trace is disabled. Skip snapshot processing!"

```
