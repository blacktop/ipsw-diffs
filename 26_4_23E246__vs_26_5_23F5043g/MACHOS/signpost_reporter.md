## signpost_reporter

> `/usr/libexec/signpost_reporter`

```diff

 174.8.0.0.0
-  __TEXT.__text: 0xb534
-  __TEXT.__auth_stubs: 0x8d0
-  __TEXT.__objc_stubs: 0x1740
+  __TEXT.__text: 0xb018
+  __TEXT.__auth_stubs: 0x870
+  __TEXT.__objc_stubs: 0x16c0
   __TEXT.__objc_methlist: 0x62c
   __TEXT.__const: 0xfa
-  __TEXT.__objc_methname: 0x1a23
-  __TEXT.__cstring: 0x1316
+  __TEXT.__objc_methname: 0x19d3
+  __TEXT.__cstring: 0x1286
   __TEXT.__objc_classname: 0x18a
   __TEXT.__objc_methtype: 0x244
-  __TEXT.__oslogstring: 0xc4f
-  __TEXT.__gcc_except_tab: 0x384
+  __TEXT.__oslogstring: 0x9c6
+  __TEXT.__gcc_except_tab: 0x358
   __TEXT.__swift5_typeref: 0x83
   __TEXT.__constg_swiftt: 0x48
   __TEXT.__swift5_reflstr: 0x60

   __TEXT.__swift5_capture: 0x10
   __TEXT.__swift5_types: 0x4
   __TEXT.__unwind_info: 0x2f8
-  __DATA_CONST.__auth_got: 0x478
-  __DATA_CONST.__got: 0x138
+  __DATA_CONST.__auth_got: 0x448
+  __DATA_CONST.__got: 0x130
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x6a0
-  __DATA_CONST.__cfstring: 0x16c0
+  __DATA_CONST.__const: 0x678
+  __DATA_CONST.__cfstring: 0x1680
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x10

   __DATA_CONST.__objc_dictobj: 0xc8
   __DATA_CONST.__objc_arrayobj: 0x90
   __DATA.__objc_const: 0x10e8
-  __DATA.__objc_selrefs: 0x620
+  __DATA.__objc_selrefs: 0x608
   __DATA.__objc_ivar: 0x80
   __DATA.__objc_data: 0x510
   __DATA.__data: 0x1c8

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: 30711C42-69DA-3B7F-B067-BBD8EAB57E91
+  UUID: 8191C9FB-B286-3F0A-B520-F54727D48169
   Functions: 266
-  Symbols:   205
-  CStrings:  777
+  Symbols:   198
+  CStrings:  759
 
Symbols:
+ _objc_retain_x26
- _OBJC_CLASS_$_AnalyticsConfigurationObserver
- _dispatch_semaphore_create
- _dispatch_semaphore_signal
- _dispatch_semaphore_wait
- _dispatch_time
- _objc_retain_x24
- _objc_retain_x27
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
