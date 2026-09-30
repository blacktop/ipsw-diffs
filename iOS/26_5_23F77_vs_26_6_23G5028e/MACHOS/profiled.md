## profiled

> `/usr/libexec/profiled`

```diff

-2438.120.3.0.0
-  __TEXT.__text: 0xd1a58
+2438.160.3.0.0
+  __TEXT.__text: 0xd1fa8
   __TEXT.__auth_stubs: 0x2800
-  __TEXT.__objc_stubs: 0x130c0
-  __TEXT.__objc_methlist: 0x617c
+  __TEXT.__objc_stubs: 0x13140
+  __TEXT.__objc_methlist: 0x6194
   __TEXT.__const: 0x12fe
   __TEXT.__gcc_except_tab: 0x1afc
-  __TEXT.__oslogstring: 0x10130
+  __TEXT.__oslogstring: 0x10240
   __TEXT.__cstring: 0xa74a
-  __TEXT.__objc_methname: 0x16817
+  __TEXT.__objc_methname: 0x16852
   __TEXT.__objc_classname: 0xc1e
   __TEXT.__objc_methtype: 0x2392
   __TEXT.__constg_swiftt: 0xdc0

   __TEXT.__swift5_types: 0xac
   __TEXT.__swift5_protos: 0x70
   __TEXT.__swift5_capture: 0x80
-  __TEXT.__unwind_info: 0x1ca0
+  __TEXT.__unwind_info: 0x1cb0
   __TEXT.__eh_frame: 0x1c0
   __DATA_CONST.__auth_got: 0x1410
   __DATA_CONST.__got: 0x2048

   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA.__objc_const: 0x6fd8
-  __DATA.__objc_selrefs: 0x53c8
+  __DATA.__objc_selrefs: 0x53e8
   __DATA.__objc_ivar: 0x204
   __DATA.__objc_data: 0x1ea8
   __DATA.__data: 0x8e8

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 0652D642-D480-3892-921E-112D640B1462
-  Functions: 2695
+  UUID: 0C709FA3-D31B-3F4E-AA11-8EE5ECE0B21F
+  Functions: 2698
   Symbols:   1769
-  CStrings:  6832
+  CStrings:  6839
 
CStrings:
+ "MCBackgroundTask verification FAILED for task '%{public}@': task is active but no request found in scheduler"
+ "MCBackgroundTask verified task '%{public}@': scheduleAfter=%{public}f, trySchedulingBefore=%{public}f"
+ "MCBackgroundTaskManager failed to schedule task with error: %{public}@"
+ "_verifyScheduledTasks"
+ "scheduleAfter"
+ "trySchedulingBefore"
+ "verify"

```
