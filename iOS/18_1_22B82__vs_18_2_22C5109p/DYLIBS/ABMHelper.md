## ABMHelper

> `/System/Library/PrivateFrameworks/ABMHelper.framework/ABMHelper`

```diff

-1183.0.0.0.0
-  __TEXT.__text: 0x137dd0
-  __TEXT.__auth_stubs: 0x2480
-  __TEXT.__init_offsets: 0xa0
+1209.0.0.0.0
+  __TEXT.__text: 0x13d6e4
+  __TEXT.__auth_stubs: 0x24f0
+  __TEXT.__init_offsets: 0xc0
   __TEXT.__objc_methlist: 0x14
-  __TEXT.__gcc_except_tab: 0x180a8
-  __TEXT.__const: 0x5f22
-  __TEXT.__cstring: 0x6400
-  __TEXT.__oslogstring: 0x87dc
-  __TEXT.__unwind_info: 0x5a90
+  __TEXT.__gcc_except_tab: 0x18af8
+  __TEXT.__const: 0x6032
+  __TEXT.__cstring: 0x68c8
+  __TEXT.__oslogstring: 0x8aca
+  __TEXT.__unwind_info: 0x5c18
   __TEXT.__objc_classname: 0x16
   __TEXT.__objc_methname: 0x5e6
   __TEXT.__objc_methtype: 0x28
   __TEXT.__objc_stubs: 0x9c0
-  __DATA_CONST.__got: 0x598
-  __DATA_CONST.__const: 0x1f90
+  __DATA_CONST.__got: 0x5c8
+  __DATA_CONST.__const: 0x1fc8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x270
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x1258
-  __AUTH_CONST.__const: 0x7e50
-  __AUTH_CONST.__cfstring: 0x7a0
+  __AUTH_CONST.__auth_got: 0x1290
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
-  Functions: 3465
-  Symbols:   4739
-  CStrings:  1988
+  Functions: 3499
+  Symbols:   4789
+  CStrings:  2035
 
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
+ __ZN3abm18CellularLoggingEUR8snapshotERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS1_8functionIFvbN3xpc4dictEEEE
+ __ZN3abm18CellularLoggingINT16snapshotInternalEN8dispatch13group_sessionERKNSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEENS3_8functionIFvbN3xpc4dictEEEE
+ __ZN3abm18CellularLoggingINT22restoreToPreviousStateEv
+ __ZN3abm18CellularLoggingINT8snapshotERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS1_8functionIFvbN3xpc4dictEEEE
+ __ZN3abm20kKeyABMDomainHWModelE
+ __ZN3abm21CellularLoggingCommon11getFileSizeEN3xpc4dictERm
+ __ZN3abm21CellularLoggingCommon16setIsAppEntitledEb
+ __ZN3abm21CellularLoggingCommon28convertFileSegmentModeToSizeENS0_19FileSegmentModeEnumE
+ __ZN3abm22kKeyABMDomainBBVersionE
+ __ZN3abm22kKeyABMDomainOSVersionE
+ __ZN3abm26kKeyTraceResetModeOnAPBootE
+ __ZN3abm6helper19kKeyFileSegmentModeE
+ __ZN3abm8asStringENS_22ResetTraceModeOnAPBootE
+ __ZN3ctu9SingletonI21CapabilitiesOverridesS1_NS_23PthreadMutexGuardPolicyIS1_EEE9sInstanceE
+ __ZN3sys18isFWVersionChangedERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
+ __ZN3sys18isOSVersionChangedEv
+ __ZN3sys22isHardwareModelChangedEv
+ __ZN3sys25getCurrentBootSessionUUIDEv
+ __ZN8INTTrace32setPropTraceResetModeReboot_syncEN8dispatch5groupENSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEES8_
+ __ZN8defaults7bbtrace17resetModeOnAPBootEv
- __ZN3abm18CellularLoggingEUR8snapshotENSt3__18functionIFvbN3xpc4dictEEEE
- __ZN3abm18CellularLoggingINT16snapshotInternalENSt3__18functionIFvbN3xpc4dictEEEE
- __ZN3abm18CellularLoggingINT19restoreDefaultStateEv
- __ZN3abm18CellularLoggingINT8snapshotENSt3__18functionIFvbN3xpc4dictEEEE
CStrings:
+ "#D Last sleep entry succeeded with config: %!s(MISSING)"
+ "#I 'Reset mode on AP Boot' is already %!s(MISSING) (%!d(MISSING))"
+ "#I Previous trace file size: %!u(MISSING) KB, Current trace file size: %!z(MISSING)u KB"
+ "#I Previous trace file size: %!z(MISSING)u KB, Current trace file size: %!z(MISSING)u KB"
+ "#I Setting - Reset mode on AP boot - from %!s(MISSING) (%!d(MISSING)) to %!s(MISSING) (%!d(MISSING))"
+ "#I Showing notification: %!s(MISSING)"
+ "#I error=%!d(MISSING), responseFlags=0x%!l(MISSING)x"
+ "#N New boot instance (%!s(MISSING)) for DIAG Trace, resetting trace mode and ownership"
+ "#N New boot instance (%!s(MISSING)) for INT Trace, resetting trace mode and ownership"
+ "#N prefs boot session uuid: %!s(MISSING), current boot session uuid: %!s(MISSING), reset mode on AP boot: %!s(MISSING)"
+ "/private/var/wireless/Library/Preferences/com.apple.AppleBasebandManager.Statistics.plist"
+ "Baseband DIAG DMC Integrity Match"
+ "Baseband IPC Trace ICE Snapshot"
+ "Baseband IPC Trace Snapshot"
+ "Baseband Logging Mode has been changed"
+ "Baseband Trace Mode has been changed"
+ "Both file-size and chunk mode are passed"
+ "Capability %!s(MISSING) returning overridden value"
+ "Cellular Problem"
+ "Cellular Radar Notifications Disabled"
+ "Cellular Sysdiagnose Complete"
+ "DIAG Mode changed"
+ "DIAG Service Error"
+ "ETB Configuration"
+ "Failed to get - Reset mode on AP boot - property!"
+ "Failed to get file size"
+ "Failed to set - Reset mode on AP boot - property!"
+ "File size (%!z(MISSING)u) KB must be the power of 2"
+ "Given file size (%!z(MISSING)u) KB is beyond the minimum boundary, adjusting to (%!u(MISSING)) KB"
+ "Integrity check for DMC file found an issue. Please file a radar under Purple ETL"
+ "Kernel PCI ABP Trace Snapshot"
+ "Kernel PCI Dump Code Registry"
+ "Kernel PCI Trace Snapshot"
+ "Last sleep entry failed with config: %!s(MISSING)"
+ "Last_Used"
+ "Mode has changed. Please, reboot the device"
+ "No ResetInfoRegexPatterns entry found in ABMProperties, so the default patterns will be used"
+ "OK"
+ "Passive external AT Only"
+ "Reboot the device before continuing to use the baseband trace"
+ "Received null input"
+ "Reset Mode On AP Boot  : "
+ "Reset Mode On Reboot  : "
+ "ResetInfoReasonRegexPattern"
+ "ResetInfoReasonRegexPatternMask"
+ "ResetInfoRegexPatterns"
+ "Reset_Mode_Boot"
+ "Resetting the baseband to apply your change"
+ "Restart the device before continuing to use DIAG trace"
+ "Restart the device before continuing to use the baseband trace"
+ "The Given file size %!z(MISSING)u KB is less than minimum %!u(MISSING) KB, adjusting to %!u(MISSING) KB"
+ "To control notifications please go to:\n\nSettings > Carrier Settings > Baseband Manager > Logging Settings > Radar Notifications"
+ "Unexpected trace mode: %!s(MISSING)"
+ "Watchdog timed out"
+ "com.apple.telephony.capabilities"
+ "coredump collection"
+ "kKeyFileSegmentMode"
- "#I Previous trace file size: %!u(MISSING) KB, Current trace file size: %!u(MISSING) KB"
- "#N New boot instance (%!s(MISSING)) for DIAG Trace"
- "#N New boot instance (%!s(MISSING)) for INT Trace"
- "#N prefs boot session uuid: %!s(MISSING), current boot session uuid: %!s(MISSING)"
- "Default pattern masks will be used"
- "File size (%!u(MISSING)) KB must be the power of 2"
- "Given file size (%!u(MISSING)) KB is beyond the boundary."
- "The Given file size %!u(MISSING) KB is less than minimum %!u(MISSING) KB"
- "Triggered by streaming mode"
- "stopWithConfig: Change state error"

```
