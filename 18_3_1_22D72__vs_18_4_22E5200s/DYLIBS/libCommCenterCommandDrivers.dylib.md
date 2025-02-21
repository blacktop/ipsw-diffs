## libCommCenterCommandDrivers.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterCommandDrivers.dylib`

```diff

-12227.1.1.0.0
-  __TEXT.__text: 0x33e00
+12317.2.0.0.0
+  __TEXT.__text: 0x33b74
   __TEXT.__auth_stubs: 0xf60
   __TEXT.__init_offsets: 0x8
-  __TEXT.__const: 0x4634
-  __TEXT.__gcc_except_tab: 0x4980
-  __TEXT.__oslogstring: 0x1897
-  __TEXT.__cstring: 0x13d8
-  __TEXT.__unwind_info: 0x1730
-  __DATA_CONST.__got: 0x1e8
+  __TEXT.__const: 0x456c
+  __TEXT.__gcc_except_tab: 0x49d4
+  __TEXT.__oslogstring: 0x1bb1
+  __TEXT.__cstring: 0x1479
+  __TEXT.__unwind_info: 0x16e8
+  __DATA_CONST.__got: 0x200
   __DATA_CONST.__const: 0x8b8
   __AUTH_CONST.__auth_got: 0x7b8
-  __AUTH_CONST.__const: 0x4f58
+  __AUTH_CONST.__const: 0x4f30
   __AUTH_CONST.__cfstring: 0x80
-  __DATA_DIRTY.__bss: 0x118
   __DATA_DIRTY.__common: 0x248
+  __DATA_DIRTY.__bss: 0x118
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterBase.dylib
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libTelephonyCapabilities.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 1317
-  Symbols:   2021
-  CStrings:  414
+  Functions: 1303
+  Symbols:   2023
+  CStrings:  429
 
Symbols:
+ __Z8asString16DataCodingScheme
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTINSt3__117bad_function_callE
+ __ZTVNSt3__117bad_function_callE
+ _syslog
- __ZNKSt9exception4whatEv
- __ZNSt9exceptionD2Ev
- __ZTISt9exception
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
