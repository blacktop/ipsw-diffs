## signpost_reporter

> `/usr/libexec/signpost_reporter`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 203.0.0.0.0
-  __TEXT.__text: 0xaa18
-  __TEXT.__auth_stubs: 0x8d0
-  __TEXT.__objc_stubs: 0x1780
+  __TEXT.__text: 0xaee0
+  __TEXT.__auth_stubs: 0x910
+  __TEXT.__objc_stubs: 0x1800
   __TEXT.__objc_methlist: 0x62c
   __TEXT.__const: 0x10a
-  __TEXT.__objc_methname: 0x1a63
-  __TEXT.__cstring: 0x1216
+  __TEXT.__objc_methname: 0x1ab3
+  __TEXT.__cstring: 0x12b6
   __TEXT.__objc_classname: 0x17f
   __TEXT.__objc_methtype: 0x244
-  __TEXT.__oslogstring: 0x99d
-  __TEXT.__gcc_except_tab: 0x3cc
+  __TEXT.__oslogstring: 0xc26
+  __TEXT.__gcc_except_tab: 0x3f8
   __TEXT.__swift5_typeref: 0x83
   __TEXT.__constg_swiftt: 0x48
   __TEXT.__swift5_reflstr: 0x60
   __TEXT.__swift5_fieldmd: 0x7c
   __TEXT.__swift5_capture: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x308
-  __DATA_CONST.__const: 0x6c0
-  __DATA_CONST.__cfstring: 0x16c0
+  __TEXT.__unwind_info: 0x310
+  __DATA_CONST.__const: 0x6e8
+  __DATA_CONST.__cfstring: 0x1700
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x10

   __DATA_CONST.__objc_arraydata: 0x378
   __DATA_CONST.__objc_dictobj: 0xc8
   __DATA_CONST.__objc_arrayobj: 0x90
-  __DATA_CONST.__auth_got: 0x478
-  __DATA_CONST.__got: 0x148
+  __DATA_CONST.__auth_got: 0x498
+  __DATA_CONST.__got: 0x150
   __DATA_CONST.__auth_ptr: 0x20
   __DATA.__objc_const: 0x10e8
-  __DATA.__objc_selrefs: 0x638
+  __DATA.__objc_selrefs: 0x650
   __DATA.__objc_ivar: 0x80
   __DATA.__objc_data: 0x510
   __DATA.__data: 0x1c8

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 265
-  Symbols:   205
-  CStrings:  580
+  Functions: 266
+  Symbols:   210
+  CStrings:  596
 
Symbols:
+ _OBJC_CLASS_$_AnalyticsConfigurationObserver
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _dispatch_time
+ _os_variant_has_internal_diagnostics
- _objc_retain_x27
Functions:
~ sub_100004b9c : 2852 -> 3352
+ sub_100007938
CStrings:
+ "Not reporting based on not being tasked-on by CoreAnalytics ('%@' is false)"
+ "Not reporting based on not being tasked-on by CoreAnalytics (Non-NSDictionary configuration object)"
+ "Not reporting based on not being tasked-on by CoreAnalytics (Timeout waiting for config)"
+ "Not reporting based on not being tasked-on by CoreAnalytics (nil configuration object)"
+ "Not reporting based on not being tasked-on by CoreAnalytics (unexpected type string: '%@')"
+ "Not reporting since is not tasked-on by CoreAnalytics (nil value for %@ key)"
+ "Not reporting since not tasked-on by CoreAnalytics (Wrong value class for class for %@)"
+ "Reporting based on being tasked-on by CoreAnalytics"
+ "Reporting based on os_variant result"
+ "TaskedOn"
+ "boolValue"
+ "com.apple.performance.signpost_reporter_tasking"
+ "com.apple.signpost"
+ "setConfigurationObserverDelegate:queue:"
+ "signpost_reporter configuration observing queue"
+ "startObservingConfigurationType:"
+ "v24@?0@\"NSObject\"8@\"NSString\"16"
- "Reporting based on being a customer seed build."
```
