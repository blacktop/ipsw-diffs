## ptpassivecollectiond

> `/usr/libexec/ptpassivecollectiond`

```diff

-240.0.0.0.0
-  __TEXT.__text: 0x11e90
+241.0.0.0.0
+  __TEXT.__text: 0x11fa0
   __TEXT.__auth_stubs: 0xb70
-  __TEXT.__objc_stubs: 0x1b60
+  __TEXT.__objc_stubs: 0x1b40
   __TEXT.__objc_methlist: 0xd50
   __TEXT.__const: 0x11c
   __TEXT.__gcc_except_tab: 0x3b0
-  __TEXT.__cstring: 0x12e7
-  __TEXT.__oslogstring: 0x1ce9
+  __TEXT.__cstring: 0x1307
+  __TEXT.__oslogstring: 0x1dc9
   __TEXT.__dlopen_cstrs: 0x59
   __TEXT.__objc_classname: 0x129
   __TEXT.__objc_methname: 0x2526

   __DATA_CONST.__got: 0x128
   __DATA_CONST.__auth_ptr: 0x48
   __DATA_CONST.__const: 0x610
-  __DATA_CONST.__cfstring: 0xd40
+  __DATA_CONST.__cfstring: 0xd60
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: B9E703FC-7A52-3316-B03E-D36FC2D8F870
+  UUID: 47346B6A-3548-30E9-BFF1-4A515621A968
   Functions: 401
   Symbols:   251
-  CStrings:  864
+  CStrings:  872
 
Functions:
~ sub_100008588 : 932 -> 980
~ sub_100009f28 -> sub_100009f58 : 744 -> 808
~ sub_10000a274 -> sub_10000a2e4 : 1108 -> 1268
CStrings:
+ "Cannot start due to error enabling MetricMonitor: %{public}@"
+ "MetricMonitor is already disabled"
+ "MetricMonitor is already enabled. We treat requests to start monitoring when already monitoring as an error"
+ "MetricMonitorAlreadyDisabled"
+ "MetricMonitorAlreadyEnabled"
+ "Power profiling is already running"
+ "PowerProfilingFailed"
+ "Updated to '%{public}@'"
+ "UpdatedAppliedPreset"
- "MetricMonitor state matches requested updated state: %{public}@"
- "MetricMonitorAlreadyInRequestedEnabledState"

```
