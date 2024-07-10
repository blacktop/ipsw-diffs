## airportd

> `/usr/libexec/airportd`

```diff

-19001.53.0.0.0
-  __TEXT.__text: 0xea930
-  __TEXT.__auth_stubs: 0x1fa0
-  __TEXT.__objc_stubs: 0x11400
+19001.51.0.0.0
+  __TEXT.__text: 0xe9a60
+  __TEXT.__auth_stubs: 0x1f80
+  __TEXT.__objc_stubs: 0x11340
   __TEXT.__objc_methlist: 0x5924
-  __TEXT.__objc_methname: 0x15e62
+  __TEXT.__objc_methname: 0x15e14
   __TEXT.__objc_classname: 0x3fe
-  __TEXT.__objc_methtype: 0x3cc0
-  __TEXT.__const: 0x1d28
-  __TEXT.__gcc_except_tab: 0x1d18
-  __TEXT.__cstring: 0x2b05f
+  __TEXT.__objc_methtype: 0x3caf
+  __TEXT.__const: 0x1d18
+  __TEXT.__gcc_except_tab: 0x1d0c
+  __TEXT.__cstring: 0x2a9ac
   __TEXT.__oslogstring: 0x90a
   __TEXT.__info_plist: 0x434
   __TEXT.__unwind_info: 0x2858
   __TEXT.__eh_frame: 0xf8
-  __DATA_CONST.__auth_got: 0xfe0
-  __DATA_CONST.__got: 0xa18
+  __DATA_CONST.__auth_got: 0xfd0
+  __DATA_CONST.__got: 0xa08
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x34b0
-  __DATA_CONST.__cfstring: 0x9fa0
+  __DATA_CONST.__cfstring: 0x9f00
   __DATA_CONST.__objc_classlist: 0x140
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x58

   __DATA_CONST.__objc_arrayobj: 0x90
   __DATA_CONST.__objc_dictobj: 0xc8
   __DATA.__objc_const: 0x93a8
-  __DATA.__objc_selrefs: 0x4db0
+  __DATA.__objc_selrefs: 0x4d80
   __DATA.__objc_ivar: 0x928
   __DATA.__objc_data: 0xc80
   __DATA.__data: 0x4b8
   __DATA.__bss: 0x240
-  __DATA.__common: 0x148
+  __DATA.__common: 0x140
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/Versions/A/CoreLocation

   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/Frameworks/SecurityFoundation.framework/Versions/A/SecurityFoundation
   - /System/Library/Frameworks/SystemConfiguration.framework/Versions/A/SystemConfiguration
-  - /System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/Versions/A/AppleDeviceQuerySupport
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreCaptureControl.framework/Versions/A/CoreCaptureControl
   - /System/Library/PrivateFrameworks/CoreWiFi.framework/Versions/A/CoreWiFi
   - /System/Library/PrivateFrameworks/IO80211.framework/Versions/A/IO80211
   - /System/Library/PrivateFrameworks/LockdownMode.framework/Versions/A/LockdownMode
-  - /System/Library/PrivateFrameworks/MobileStoreDemoCore.framework/Versions/A/MobileStoreDemoCore
   - /System/Library/PrivateFrameworks/RegulatoryDomain.framework/Versions/A/RegulatoryDomain
   - /System/Library/PrivateFrameworks/Sharing.framework/Versions/A/Sharing
   - /System/Library/PrivateFrameworks/Symptoms.framework/Versions/A/Frameworks/ManagedEvent.framework/Versions/A/ManagedEvent

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 3174
-  Symbols:   857
-  CStrings:  4086
+  Functions: 3172
+  Symbols:   854
+  CStrings:  4056
 
Symbols:
- _OBJC_CLASS_$_MSDCHelper
- _ZhuGeCopyValueWithError
- _os_eligibility_get_domain_answer
CStrings:
+ "%!s(MISSING): <%!@(MISSING)> event=%!l(MISSING)d, flags=0x%!X(MISSING), lastPowerPref=%!s(MISSING), valid[%!u(MISSING)]\n"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AirPort_executables/Tools/airportd/airportProcessCommand.m"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AirPort_executables/Tools/airportd/airportdCommandLine.m"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AirPort_executables/Tools/airportd/airportdMain.m"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AirPort_executables/Tools/airportd/airportdPreferences.m"
+ "<%!s(MISSING)[%!d(MISSING)]> %!s(MISSING): <%!@(MISSING)> event=%!l(MISSING)d, flags=0x%!X(MISSING), lastPowerPref=%!s(MISSING), valid[%!u(MISSING)]\n"
+ "<%!s(MISSING)[%!d(MISSING)]> %!s(MISSING): System wake reason: <%!@(MISSING)>, %!s(MISSING) woken by WiFi\n"
- "%!s(MISSING): <%!@(MISSING)> @[%!l(MISSING)lu.%!l(MISSING)lu], took %!l(MISSING)lu.%!l(MISSING)lu\n"
- "%!s(MISSING): <%!@(MISSING)> event=%!l(MISSING)d, @[%!l(MISSING)lu.%!l(MISSING)lu], took %!l(MISSING)lu.%!l(MISSING)lu\n"
- "%!s(MISSING): <%!@(MISSING)> event=%!l(MISSING)d, flags=0x%!X(MISSING), lastPowerPref=%!s(MISSING), valid[%!u(MISSING)], @[%!l(MISSING)lu.%!l(MISSING)lu] now[%!l(MISSING)lu.%!l(MISSING)lu]\n"
- "%!s(MISSING): <%!@(MISSING)> event=%!l(MISSING)d, flags=0x%!X(MISSING), lastPowerPref=%!s(MISSING), valid[%!u(MISSING)], @[%!l(MISSING)lu.%!l(MISSING)lu], took %!l(MISSING)lu.%!l(MISSING)lu\n"
- "%!s(MISSING): <%!@(MISSING)> eventType[%!l(MISSING)u] @[%!l(MISSING)lu.%!l(MISSING)lu], took %!l(MISSING)lu.%!l(MISSING)lu\n"
- "%!s(MISSING): <%!@(MISSING)> isConstrained[%!u(MISSING)] @[%!l(MISSING)lu.%!l(MISSING)lu], took %!l(MISSING)lu.%!l(MISSING)lu\n"
- "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AirPort_executables/Tools/airportd/airportProcessCommand.m"
- "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AirPort_executables/Tools/airportd/airportdCommandLine.m"
- "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AirPort_executables/Tools/airportd/airportdMain.m"
- "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AirPort_executables/Tools/airportd/airportdPreferences.m"
- "<%!s(MISSING)[%!d(MISSING)]> %!s(MISSING):  @[%!l(MISSING)lu.%!l(MISSING)lu], airportdUpdateDynamicStore: took %!l(MISSING)lu.%!l(MISSING)lu\n"
- "<%!s(MISSING)[%!d(MISSING)]> %!s(MISSING): %!s(MISSING): IOC %!d(MISSING) returned error %!d(MISSING)\n"
- "<%!s(MISSING)[%!d(MISSING)]> %!s(MISSING): %!s(MISSING): Manufacture Date not being set because device in demo mode\n\n"
- "<%!s(MISSING)[%!d(MISSING)]> %!s(MISSING): %!s(MISSING): mimo eligibility : (os_eligibility_get_domain_answer:out_answer:res) %!p(MISSING):%!l(MISSING)lu:%!d(MISSING)\n"
- "<%!s(MISSING)[%!d(MISSING)]> %!s(MISSING): <%!@(MISSING)> @[%!l(MISSING)lu.%!l(MISSING)lu], took %!l(MISSING)lu.%!l(MISSING)lu\n"
- "<%!s(MISSING)[%!d(MISSING)]> %!s(MISSING): <%!@(MISSING)> event=%!l(MISSING)d, @[%!l(MISSING)lu.%!l(MISSING)lu], took %!l(MISSING)lu.%!l(MISSING)lu\n"
- "<%!s(MISSING)[%!d(MISSING)]> %!s(MISSING): <%!@(MISSING)> event=%!l(MISSING)d, flags=0x%!X(MISSING), lastPowerPref=%!s(MISSING), valid[%!u(MISSING)], @[%!l(MISSING)lu.%!l(MISSING)lu] now[%!l(MISSING)lu.%!l(MISSING)lu]\n"
- "<%!s(MISSING)[%!d(MISSING)]> %!s(MISSING): <%!@(MISSING)> event=%!l(MISSING)d, flags=0x%!X(MISSING), lastPowerPref=%!s(MISSING), valid[%!u(MISSING)], @[%!l(MISSING)lu.%!l(MISSING)lu], took %!l(MISSING)lu.%!l(MISSING)lu\n"
- "<%!s(MISSING)[%!d(MISSING)]> %!s(MISSING): <%!@(MISSING)> eventType[%!l(MISSING)u] @[%!l(MISSING)lu.%!l(MISSING)lu], took %!l(MISSING)lu.%!l(MISSING)lu\n"
- "<%!s(MISSING)[%!d(MISSING)]> %!s(MISSING): <%!@(MISSING)> isConstrained[%!u(MISSING)] @[%!l(MISSING)lu.%!l(MISSING)lu], took %!l(MISSING)lu.%!l(MISSING)lu\n"
- "<%!s(MISSING)[%!d(MISSING)]> %!s(MISSING): Changed keys: filtered: count[%!u(MISSING)], @[%!l(MISSING)lu.%!l(MISSING)lu], took %!l(MISSING)lu.%!l(MISSING)lu\n"
- "<%!s(MISSING)[%!d(MISSING)]> %!s(MISSING): Processed events, count[%!l(MISSING)u], @[%!l(MISSING)lu.%!l(MISSING)lu], took %!l(MISSING)lu.%!l(MISSING)lu\n"
- "<%!s(MISSING)[%!d(MISSING)]> %!s(MISSING): System wake reason: <%!@(MISSING)>, %!s(MISSING) woken by WiFi, %!s(MISSING) woken by Bluetooth\n"
- "<%!s(MISSING)[%!d(MISSING)]> %!s(MISSING): WiFiCC : MIMO eligibility set failed : %!d(MISSING)\n\n"
- "<%!s(MISSING)[%!d(MISSING)]> %!s(MISSING): WiFiCC : WiFiCC : MIMO eligibility successfully set\n\n"
- "<%!s(MISSING)[%!d(MISSING)]> %!s(MISSING): WiFiCC : setting MIMO eligibility on Power changed : %!@(MISSING)\n"
- "<%!s(MISSING)[%!d(MISSING)]> %!s(MISSING): WiFiDeviceSetManufactureDate %!@(MISSING) %!d(MISSING)/%!d(MISSING)/%!d(MISSING) \n\n"
- "FactoryShippingSettingTime"
- "Processed events, count[%!l(MISSING)u], @[%!l(MISSING)lu.%!l(MISSING)lu], took %!l(MISSING)lu.%!l(MISSING)lu"
- "SCAN_MIN_TIMESTAMP"
- "ZZ"
- "__SCDynamicStoreDisconnectCallBack"
- "_checkMimoEligibility"
- "_setManufactureDate"
- "_setMimoEligibility"
- "airportdUpdateDynamicStore"
- "bluetooth-pcie"

```
