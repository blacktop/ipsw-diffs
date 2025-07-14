## wifiFirmwareLoader

> `/usr/libexec/wifiFirmwareLoader`

```diff

-1153.8.3.1.0
-  __TEXT.__text: 0x6554
-  __TEXT.__auth_stubs: 0x6b0
-  __TEXT.__const: 0x723
-  __TEXT.__cstring: 0x1b39
+1160.11.0.0.0
+  __TEXT.__text: 0x6f1c
+  __TEXT.__auth_stubs: 0x6e0
+  __TEXT.__const: 0x770
+  __TEXT.__cstring: 0x1fd6
   __TEXT.__oslogstring: 0x19
-  __TEXT.__unwind_info: 0xa8
-  __DATA_CONST.__auth_got: 0x358
+  __TEXT.__unwind_info: 0xb0
+  __DATA_CONST.__auth_got: 0x370
   __DATA_CONST.__got: 0x60
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x250
-  __DATA_CONST.__cfstring: 0x3a0
+  __DATA_CONST.__const: 0x270
+  __DATA_CONST.__cfstring: 0x520
   __DATA.__data: 0x10
-  __DATA.__bss: 0x1dc
+  __DATA.__bss: 0x1f4
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/PrivateFrameworks/CoreCaptureControl.framework/CoreCaptureControl
   - /usr/lib/libFDR.dylib
   - /usr/lib/libSystem.B.dylib
-  UUID: B7D9D4A4-430A-3278-A886-78DF55E2FE11
-  Functions: 24
-  Symbols:   123
-  CStrings:  240
+  UUID: B9035113-80B9-3828-8E9F-1C861237A44B
+  Functions: 25
+  Symbols:   126
+  CStrings:  273
 
Symbols:
+ _IOPMAssertionCreateWithDescription
+ _IOPMAssertionRelease
+ _sleep
CStrings:
+ "NoDisplaySleepAssertion"
+ "NoIdleSleepAssertion"
+ "PreventSystemSleep"
+ "PreventUserIdleDisplaySleep"
+ "PreventUserIdleSystemSleep"
+ "TimeoutActionTurnOff"
+ "WiFi Firmware processing preferences\n"
+ "WiFi Firmware processing preferences using: assertionEnabled:%u, assertionType:%u mapped['%s'], timeout[%u sec], assertionReleaseDelay[%u sec]\n"
+ "WiFi Firmware processing preferences, adjusting timeout -> timeout[%u sec], adjusted[%u sec]\n"
+ "_createIOPMHelperCreateAssertion 'IOPMAssertionCreateWithDescription': return [0x%08x], id[0x%08x]\n"
+ "_createIOPMHelperCreateAssertion assertionType[%s] assertionName[%s] details[%s] reason[%s] bundle[%s] timeout[%f sec] assertionID[%p] assertionLevel[0x%08x]\n"
+ "assertionEnabled"
+ "assertionReleaseDelay"
+ "assertionTimeout"
+ "assertionType"
+ "com.apple.wifiFirmwareLoader.IOPMAssertion.loading-firmware"
+ "wifiFirmwareLoader: IOPMAssertion: Loading firmware"
+ "wifiFirmwareLoaderServiceThread: _createIOPMHelperCreateAssertion return[0x%08x], id[0x%08x]\n"
+ "wifiFirmwareLoaderServiceThread: _releaseIOPMHelperAssertionRelease return[0x%08x], id[0x%08x], release id[0x%08x]\n"
+ "wifiFirmwareLoaderServiceThread: delay[%u sec] - ended\n"
+ "wifiFirmwareLoaderServiceThread: delay[%u sec] - started\n"

```
