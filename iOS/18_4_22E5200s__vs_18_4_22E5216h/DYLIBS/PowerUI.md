## PowerUI

> `/System/Library/PrivateFrameworks/PowerUI.framework/PowerUI`

```diff

-651.0.0.0.0
-  __TEXT.__text: 0xbbcc4
+651.100.3.0.0
+  __TEXT.__text: 0xbc268
   __TEXT.__auth_stubs: 0xaf0
-  __TEXT.__objc_methlist: 0x1b0dc
+  __TEXT.__objc_methlist: 0x1b114
   __TEXT.__const: 0x4d8
-  __TEXT.__cstring: 0xd8e3
-  __TEXT.__oslogstring: 0xa9d8
+  __TEXT.__cstring: 0xd911
+  __TEXT.__oslogstring: 0xab29
   __TEXT.__gcc_except_tab: 0x1234
-  __TEXT.__unwind_info: 0x1bf8
+  __TEXT.__unwind_info: 0x1c18
   __TEXT.__objc_classname: 0xb0f
-  __TEXT.__objc_methname: 0x3dac0
+  __TEXT.__objc_methname: 0x3db14
   __TEXT.__objc_methtype: 0x4090
-  __TEXT.__objc_stubs: 0xc520
+  __TEXT.__objc_stubs: 0xc5a0
   __DATA_CONST.__got: 0x4e8
   __DATA_CONST.__const: 0x13e0
   __DATA_CONST.__objc_classlist: 0x2e0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5250
+  __DATA_CONST.__objc_selrefs: 0x5270
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x2b8
   __DATA_CONST.__objc_arraydata: 0x6e70
   __AUTH_CONST.__auth_got: 0x588
   __AUTH_CONST.__const: 0x640
-  __AUTH_CONST.__cfstring: 0xb620
+  __AUTH_CONST.__cfstring: 0xb660
   __AUTH_CONST.__objc_const: 0x35b30
   __AUTH_CONST.__objc_intobj: 0x8e8
   __AUTH_CONST.__objc_arrayobj: 0x378

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 9632
-  Symbols:   10162
-  CStrings:  7191
+  Functions: 9640
+  Symbols:   10168
+  CStrings:  7204
 
CStrings:
+ "%@: (%@ g/kWh CO2e)"
+ "Already evaluated shouldChargeNow in last %.0f mins. Skipping"
+ "Current time: %@. Found next clean interval to be in %.0lf hours, starting at %@."
+ "Demo CEC Phase update from %lu to %lu (%@ --> %@); BatteryLevel %ld, PluggedIn %d"
+ "Demo CEC will use the following resampled forecast: %@"
+ "Device no longer plugged into a power source."
+ "Device no longer plugged into a power source. Disengaging and resetting state."
+ "Enabled Ambrosia!"
+ "Evaluating phase. Trigger: %@ (CurrentPhase %lu batteryLevel %ld, isPluggedIn %d)"
+ "No clean intervals set. Unable to compute time to next clean interval."
+ "No upcoming clean intervals. All clean intervals already occured!"
+ "Unable to compute time until next clean session. Defaulting to registering %.0f minute timer."
+ "Unkown"
+ "[Internal] IBLM"
+ "ambrosia"
+ "ambrosiaAlways"
+ "balancingAuthority"
+ "balancingAuthorityName"
+ "disableMitigations"
+ "enableMitigations"
+ "timeToNextCleanInterval"
- "%@: (%@)"
- "Already evaluated shouldChargeNow in last %lu mins. Skipping"
- "Demo CEC Phase update from %lu to %lu (%@ --> %@); BatteryLevel %ld, PluggedIntoEligibleSource %d"
- "Device no longer plugged into an eligible power source. Disengaging and resetting state."
- "Device no longer plugged into eligible source."
- "Enable LPM!"
- "Evaluating phase. Trigger: %@ (CurrentPhase %lu batteryLevel %ld, isPluggedIntoEligibleSource %d)"
- "[Internal] Low Power Mode"

```
