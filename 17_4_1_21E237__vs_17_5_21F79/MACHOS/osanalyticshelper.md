## osanalyticshelper

> `/System/Library/CoreServices/osanalyticshelper`

```diff

-656.100.20.0.0
-  __TEXT.__text: 0xe614
-  __TEXT.__auth_stubs: 0x890
-  __TEXT.__objc_stubs: 0x2140
-  __TEXT.__objc_methlist: 0x680
+656.122.3.0.0
+  __TEXT.__text: 0xeb94
+  __TEXT.__auth_stubs: 0x8d0
+  __TEXT.__objc_stubs: 0x21a0
+  __TEXT.__objc_methlist: 0x6ac
   __TEXT.__const: 0xd0
   __TEXT.__gcc_except_tab: 0x130
-  __TEXT.__cstring: 0x1938
-  __TEXT.__objc_methname: 0x1d67
-  __TEXT.__objc_classname: 0x140
+  __TEXT.__cstring: 0x19e4
+  __TEXT.__objc_methname: 0x1d99
+  __TEXT.__objc_classname: 0x15a
   __TEXT.__objc_methtype: 0x586
-  __TEXT.__oslogstring: 0x12c4
-  __TEXT.__unwind_info: 0x31c
-  __DATA_CONST.__auth_got: 0x458
+  __TEXT.__oslogstring: 0x138a
+  __TEXT.__unwind_info: 0x320
+  __DATA_CONST.__auth_got: 0x478
   __DATA_CONST.__got: 0x100
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x768
-  __DATA_CONST.__cfstring: 0x1e20
-  __DATA_CONST.__objc_classlist: 0x60
+  __DATA_CONST.__const: 0x7a8
+  __DATA_CONST.__cfstring: 0x1f60
+  __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_classrefs: 0x1d8

   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x15e0
-  __DATA.__objc_selrefs: 0x8d0
+  __DATA.__objc_const: 0x1670
+  __DATA.__objc_selrefs: 0x8e8
   __DATA.__objc_ivar: 0xb4
-  __DATA.__objc_data: 0x3c0
+  __DATA.__objc_data: 0x410
   __DATA.__data: 0x180
   __DATA.__bss: 0x90
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 229
-  Symbols:   234
-  CStrings:  880
+  Functions: 235
+  Symbols:   237
+  CStrings:  901
 
Symbols:
+ _CFBooleanGetValue
+ _MGCopyAnswer
+ _objc_autorelease
+ _rtcsc_send_realtime
- _OBJC_CLASS_$_OSADailyTelemetryMonitor
CStrings:
+ "Collecting developer opt in telemetry"
+ "NO"
+ "OSADailyTelemetryMonitor"
+ "Registering the boot time rtc beacon activity."
+ "Running daily telemetry monitor."
+ "Running the post-boot telemetry."
+ "Sending RTC Beacon"
+ "Sending RTC Beacon CA Event"
+ "SerialNumber"
+ "SigningFuse"
+ "YES"
+ "collectDeveloperOptIn"
+ "com.apple.osanalytics.beacon"
+ "com.apple.osanalytics.developerOptIn"
+ "com.apple.osanalytics.postboot.telemetry"
+ "no_serial"
+ "optIn3rdParty"
+ "prodFused"
+ "sendRTCBeacon:"
+ "serial"

```
