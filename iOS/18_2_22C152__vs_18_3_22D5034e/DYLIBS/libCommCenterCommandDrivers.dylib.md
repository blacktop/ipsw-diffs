## libCommCenterCommandDrivers.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterCommandDrivers.dylib`

```diff

-12214.4.0.0.0
-  __TEXT.__text: 0x33cf8
-  __TEXT.__auth_stubs: 0xf60
+12225.1.0.0.0
+  __TEXT.__text: 0x3440c
+  __TEXT.__auth_stubs: 0xf70
   __TEXT.__init_offsets: 0x8
-  __TEXT.__const: 0x460c
-  __TEXT.__gcc_except_tab: 0x4980
-  __TEXT.__oslogstring: 0x1897
-  __TEXT.__cstring: 0x13d8
-  __TEXT.__unwind_info: 0x1728
+  __TEXT.__const: 0x4654
+  __TEXT.__gcc_except_tab: 0x498c
+  __TEXT.__oslogstring: 0x1bb1
+  __TEXT.__cstring: 0x1479
+  __TEXT.__unwind_info: 0x1730
   __DATA_CONST.__got: 0x1e8
   __DATA_CONST.__const: 0x8b8
-  __AUTH_CONST.__auth_got: 0x7b8
-  __AUTH_CONST.__const: 0x4f10
+  __AUTH_CONST.__auth_got: 0x7c0
+  __AUTH_CONST.__const: 0x4f68
   __AUTH_CONST.__cfstring: 0x80
   __DATA_DIRTY.__bss: 0x118
   __DATA_DIRTY.__common: 0x248

   - /usr/lib/libTelephonyCapabilities.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 1314
-  Symbols:   2014
-  CStrings:  414
+  Functions: 1317
+  Symbols:   2022
+  CStrings:  429
 
Symbols:
+ __Z8asString16DataCodingScheme
+ __ZN23SetupEventNotificationsD0Ev
+ __ZN23SetupEventNotificationsD1Ev
+ __ZN23SetupEventNotificationsD2Ev
+ __ZTI23SetupEventNotifications
+ __ZTS23SetupEventNotifications
+ __ZTV23SetupEventNotifications
+ _syslog
- ___TUAssertTrigger
CStrings:
+ "#D Adding Frequency: %llu, Bandwidth: %u, Priority: %d"
+ "#D Carrier has CarrierAllowsRingingMultipleDevices set to false or doesn't have that key defined"
+ "#D Carrier has CarrierAllowsRingingMultipleDevices set to true!"
+ "#D Decoding PLMN name of %lu bytes using coding scheme %s"
+ "#D Duplicated frequency (%llu), keeping higher bandwidth (%u)"
+ "#D No historical bytes, not capable"
+ "#D No report required"
+ "#D Queried hardware model config (%d) and suffix (%s)"
+ "#D SIM authenticate success; reporting result on card %s"
+ "#D Swapped the characters: %s"
+ "#D Vinyl capabilities byte: 0x%02x"
+ "#D We are on an Data-Only device AND we are on an external build"
+ "#D isInternalBuild: %d, voiceCallsAllowedRightNow (Buddy): %d, dataDeviceWithAllowsRingingMultipleDevices: %d, dataOnlyDevice: %d, Thumper Secondar device: %d"
+ "/Library/Caches/com.apple.xbs/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/Awd/AwdCommandDriver.cpp"
+ "Assertion failure: ( %s ), in file %s, line: %d"

```
