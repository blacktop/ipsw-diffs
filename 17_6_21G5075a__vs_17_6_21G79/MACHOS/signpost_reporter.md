## signpost_reporter

> `/usr/libexec/signpost_reporter`

```diff

 125.1.0.0.0
-  __TEXT.__text: 0x7bb0
-  __TEXT.__auth_stubs: 0x540
-  __TEXT.__objc_stubs: 0x14e0
+  __TEXT.__text: 0x8260
+  __TEXT.__auth_stubs: 0x5a0
+  __TEXT.__objc_stubs: 0x1580
   __TEXT.__objc_methlist: 0x5b8
   __TEXT.__const: 0x30
-  __TEXT.__objc_methname: 0x17fc
-  __TEXT.__cstring: 0x1170
+  __TEXT.__objc_methname: 0x1868
+  __TEXT.__cstring: 0x120c
   __TEXT.__objc_classname: 0x17d
   __TEXT.__objc_methtype: 0x226
-  __TEXT.__oslogstring: 0x8ff
-  __TEXT.__gcc_except_tab: 0x260
-  __TEXT.__unwind_info: 0x240
-  __DATA_CONST.__auth_got: 0x2b0
+  __TEXT.__oslogstring: 0xb88
+  __TEXT.__gcc_except_tab: 0x284
+  __TEXT.__unwind_info: 0x244
+  __DATA_CONST.__auth_got: 0x2e0
   __DATA_CONST.__got: 0x28
-  __DATA_CONST.__const: 0x5d0
-  __DATA_CONST.__cfstring: 0x1600
+  __DATA_CONST.__const: 0x5f8
+  __DATA_CONST.__cfstring: 0x1640
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_classrefs: 0x100
+  __DATA_CONST.__objc_classrefs: 0x110
   __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_intobj: 0x78
   __DATA_CONST.__objc_arraydata: 0x378
   __DATA_CONST.__objc_dictobj: 0xc8
   __DATA_CONST.__objc_arrayobj: 0x90
   __DATA.__objc_const: 0xfa0
-  __DATA.__objc_selrefs: 0x590
+  __DATA.__objc_selrefs: 0x5b0
   __DATA.__objc_ivar: 0x80
   __DATA.__objc_data: 0x410
   __DATA.__data: 0x110

   - /System/Library/PrivateFrameworks/WorkflowResponsiveness.framework/WorkflowResponsiveness
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 219
-  Symbols:   124
-  CStrings:  544
+  Functions: 228
+  Symbols:   131
+  CStrings:  561
 
Symbols:
+ _OBJC_CLASS_$_AnalyticsConfigurationObserver
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _dispatch_time
+ _objc_retain_x27
+ _os_variant_has_internal_diagnostics
CStrings:
+ "Not reporting based on not being tasked-on by CoreAnalytics ('%!@(MISSING)' is false)"
+ "Not reporting based on not being tasked-on by CoreAnalytics (Non-NSDictionary configuration object)"
+ "Not reporting based on not being tasked-on by CoreAnalytics (Timeout waiting for config)"
+ "Not reporting based on not being tasked-on by CoreAnalytics (nil configuration object)"
+ "Not reporting based on not being tasked-on by CoreAnalytics (unexpected type string: '%!@(MISSING)')"
+ "Not reporting since is not tasked-on by CoreAnalytics (nil value for %!@(MISSING) key)"
+ "Not reporting since not tasked-on by CoreAnalytics (Wrong value class for class for %!@(MISSING))"
+ "Reporting based on being tasked-on by CoreAnalytics"
+ "Reporting based on os_variant result"
+ "TaskedOn"
+ "addSubsystem:category:"
+ "boolValue"
+ "com.apple.performance.signpost_reporter_tasking"
+ "com.apple.signpost"
+ "setConfigurationObserverDelegate:queue:"
+ "signpost_reporter configuration observing queue"
+ "startObservingConfigurationType:"
+ "v24@?0@\"NSObject\"8@\"NSString\"16"
- "Reporting based on being a customer seed build."

```
