## signpost_reporter

> `/usr/libexec/signpost_reporter`

```diff

 151.8.0.0.0
-  __TEXT.__text: 0x816c
-  __TEXT.__auth_stubs: 0x580
-  __TEXT.__objc_stubs: 0x16a0
+  __TEXT.__text: 0x7c78
+  __TEXT.__auth_stubs: 0x530
+  __TEXT.__objc_stubs: 0x1620
   __TEXT.__objc_methlist: 0x5e4
   __TEXT.__const: 0x78
-  __TEXT.__objc_methname: 0x1923
-  __TEXT.__cstring: 0x125c
+  __TEXT.__objc_methname: 0x18d0
+  __TEXT.__cstring: 0x11c0
   __TEXT.__objc_classname: 0x17d
   __TEXT.__objc_methtype: 0x226
-  __TEXT.__oslogstring: 0xc18
-  __TEXT.__gcc_except_tab: 0x374
-  __TEXT.__unwind_info: 0x260
-  __DATA_CONST.__auth_got: 0x2d0
-  __DATA_CONST.__got: 0xd8
-  __DATA_CONST.__const: 0x5f8
-  __DATA_CONST.__cfstring: 0x16a0
+  __TEXT.__oslogstring: 0x98f
+  __TEXT.__gcc_except_tab: 0x348
+  __TEXT.__unwind_info: 0x258
+  __DATA_CONST.__auth_got: 0x2a8
+  __DATA_CONST.__got: 0xd0
+  __DATA_CONST.__const: 0x5d0
+  __DATA_CONST.__cfstring: 0x1660
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x10

   __DATA_CONST.__objc_dictobj: 0xc8
   __DATA_CONST.__objc_arrayobj: 0x90
   __DATA.__objc_const: 0xf60
-  __DATA.__objc_selrefs: 0x5f8
+  __DATA.__objc_selrefs: 0x5e0
   __DATA.__objc_ivar: 0x80
   __DATA.__objc_data: 0x410
   __DATA.__data: 0x120

   - /System/Library/PrivateFrameworks/WorkflowResponsiveness.framework/WorkflowResponsiveness
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F6028E96-24A7-3A4C-A580-3117D29C2C84
-  Functions: 205
-  Symbols:   130
-  CStrings:  750
+  UUID: E1D2BC3C-D19B-3EB5-BDE5-5DEF9CEF6AD5
+  Functions: 206
+  Symbols:   124
+  CStrings:  732
 
Symbols:
- _OBJC_CLASS_$_AnalyticsConfigurationObserver
- _dispatch_semaphore_create
- _dispatch_semaphore_signal
- _dispatch_semaphore_wait
- _dispatch_time
- _os_variant_has_internal_diagnostics
CStrings:
+ "Reporting based on being a customer seed build."
- "Not reporting based on not being tasked-on by CoreAnalytics ('%@' is false)"
- "Not reporting based on not being tasked-on by CoreAnalytics (Non-NSDictionary configuration object)"
- "Not reporting based on not being tasked-on by CoreAnalytics (Timeout waiting for config)"
- "Not reporting based on not being tasked-on by CoreAnalytics (nil configuration object)"
- "Not reporting based on not being tasked-on by CoreAnalytics (unexpected type string: '%@')"
- "Not reporting since is not tasked-on by CoreAnalytics (nil value for %@ key)"
- "Not reporting since not tasked-on by CoreAnalytics (Wrong value class for class for %@)"
- "Reporting based on being tasked-on by CoreAnalytics"
- "Reporting based on os_variant result"
- "TaskedOn"
- "boolValue"
- "com.apple.performance.signpost_reporter_tasking"
- "com.apple.signpost"
- "setConfigurationObserverDelegate:queue:"
- "signpost_reporter configuration observing queue"
- "startObservingConfigurationType:"
- "v24@?0@\"NSObject\"8@\"NSString\"16"

```
