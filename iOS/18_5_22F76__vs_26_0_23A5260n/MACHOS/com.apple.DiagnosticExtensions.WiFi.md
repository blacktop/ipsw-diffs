## com.apple.DiagnosticExtensions.WiFi

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.WiFi.appex/com.apple.DiagnosticExtensions.WiFi`

```diff

-500.0.0.0.0
-  __TEXT.__text: 0x16fc
-  __TEXT.__auth_stubs: 0x1a0
-  __TEXT.__objc_stubs: 0x360
-  __TEXT.__objc_methlist: 0x5c
+503.0.0.0.0
+  __TEXT.__text: 0x1f20
+  __TEXT.__auth_stubs: 0x270
+  __TEXT.__objc_stubs: 0x540
+  __TEXT.__objc_methlist: 0x8c
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__const: 0x18
+  __TEXT.__const: 0x20
   __TEXT.__gcc_except_tab: 0x20
-  __TEXT.__cstring: 0x198
-  __TEXT.__oslogstring: 0x13
+  __TEXT.__cstring: 0x370
+  __TEXT.__oslogstring: 0xba
   __TEXT.__objc_classname: 0x1a
-  __TEXT.__objc_methname: 0x2c3
-  __TEXT.__objc_methtype: 0x13
-  __TEXT.__unwind_info: 0xa8
-  __DATA_CONST.__auth_got: 0xe0
-  __DATA_CONST.__got: 0x70
-  __DATA_CONST.__const: 0x60
-  __DATA_CONST.__cfstring: 0x2c0
+  __TEXT.__objc_methname: 0x3f6
+  __TEXT.__objc_methtype: 0x34
+  __TEXT.__unwind_info: 0xc0
+  __DATA_CONST.__auth_got: 0x148
+  __DATA_CONST.__got: 0x78
+  __DATA_CONST.__const: 0xc8
+  __DATA_CONST.__cfstring: 0x3c0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0xe8
+  __DATA.__objc_selrefs: 0x160
   __DATA.__objc_data: 0x50
-  __DATA.__bss: 0x18
+  __DATA.__bss: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/DiagnosticExtensions.framework/DiagnosticExtensions
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E8C6D547-3040-3B84-BB70-FE34A432604E
-  Functions: 13
-  Symbols:   50
-  CStrings:  85
+  UUID: 8A284A21-F4B0-327F-A094-9C73DB2F012E
+  Functions: 19
+  Symbols:   65
+  CStrings:  130
 
Symbols:
+ _AnalyticsSendEventLazy
+ _CFAbsoluteTimeGetCurrent
+ _CFGetTypeID
+ _CFRelease
+ _CFStringGetTypeID
+ _MGCopyAnswer
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSNumber
+ __NSConcreteGlobalBlock
+ __os_log_impl
+ _dispatch_once
+ _objc_enumerationMutation
+ _objc_release_x1
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x20
+ _objc_retain_x21
+ _os_log_create
- __os_log_default
- __os_log_error_impl
CStrings:
+ "%{public}s::%d: attachmentList called"
+ "%{public}s::%d: called with param: %@"
+ "%{public}s::%d: called with parameters: %@"
+ "%{public}s::%d: done"
+ "%{public}s::%d: sent telemetry metricDict: %@"
+ "-[WiFiDiagnosticsExtension attachmentList]"
+ "-[WiFiDiagnosticsExtension attachmentsForParameters:]"
+ "-[WiFiDiagnosticsExtension sendTelemetryAndClearTimers:withAttachments:]"
+ "-[WiFiDiagnosticsExtension sendTelemetryAndClearTimers:withAttachments:]_block_invoke"
+ "@\"NSDictionary\"8@?0"
+ "Q24@0:8@16"
+ "ReleaseType"
+ "WiFiDE"
+ "WiFiDELog"
+ "addObjectsFromArray:"
+ "attachmentCollectionDuration"
+ "attachmentCount"
+ "attachmentSize"
+ "attachmentSizes:"
+ "class"
+ "clearTimers"
+ "com.apple.wifi.WiFiDiagnosticExtension"
+ "com.apple.wifi.diagnosticextension"
+ "count"
+ "countByEnumeratingWithState:objects:count:"
+ "dictionary"
+ "filesize"
+ "numberWithDouble:"
+ "numberWithUnsignedInteger:"
+ "numberWithUnsignedLongLong:"
+ "objectForKey:"
+ "releaseType"
+ "sendTelemetryAndClearTimers:withAttachments:"
+ "setObject:forKeyedSubscript:"
+ "unsignedIntValue"
+ "v16@0:8"
+ "v32@0:8@16@24"
- "WiFi DE: params=%@"

```
