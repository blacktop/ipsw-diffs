## mlhostd

> `/usr/libexec/mlhostd`

```diff

-3.0.10.0.0
-  __TEXT.__text: 0x49838
-  __TEXT.__auth_stubs: 0x1930
+3.1.14.0.0
+  __TEXT.__text: 0x49f78
+  __TEXT.__auth_stubs: 0x1910
   __TEXT.__objc_methlist: 0x38
   __TEXT.__const: 0xf94
-  __TEXT.__cstring: 0xb62a
+  __TEXT.__cstring: 0xb6da
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x354
   __TEXT.__swift5_typeref: 0x71f

   __TEXT.__swift5_assocty: 0xd8
   __TEXT.__swift5_proto: 0xd4
   __TEXT.__swift5_types: 0x50
-  __TEXT.__objc_methname: 0xab0
+  __TEXT.__objc_methname: 0xabb
   __TEXT.__objc_classname: 0x1f
   __TEXT.__objc_methtype: 0x342
-  __TEXT.__swift5_capture: 0x1b4
-  __TEXT.__unwind_info: 0x8e4
+  __TEXT.__swift5_capture: 0x1bc
+  __TEXT.__unwind_info: 0x8d4
   __TEXT.__eh_frame: 0x1108
-  __DATA_CONST.__auth_got: 0xc98
+  __DATA_CONST.__auth_got: 0xc88
   __DATA_CONST.__got: 0x3c0
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0xf08
+  __DATA_CONST.__const: 0xf58
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_const: 0xac8
   __DATA.__objc_selrefs: 0x2d0
   __DATA.__objc_data: 0x170
-  __DATA.__data: 0x5248
+  __DATA.__data: 0x5228
   __DATA.__bss: 0x1a80
   __DATA.__common: 0x30
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 731
-  Symbols:   670
-  CStrings:  1528
+  Functions: 733
+  Symbols:   668
+  CStrings:  1532
 
Symbols:
+ _$s20LighthouseBackground12MLHostResultC11errorStringSSSgvg
+ _$s20LighthouseBackground30GetOnDemandTaskRequestResponseV6result7messageACSb_SStcfC
- _$s20LighthouseBackground10TaskStatusO12isTerminatedySbACFZ
- _$s20LighthouseBackground12MLHostResultC11errorStringSSSgvgTj
- _$s20LighthouseBackground30GetOnDemandTaskRequestResponseV6resultACSS_tcfC
- _objc_retain_x9
CStrings:
+ " is deferred during shouldRun."
+ "Task %s asked to terminate because of deferral after %s."
+ "Task %s completed after %s. TaskResult: %@"
+ "Task %s completed doWork with result %@."
+ "Task %s completed shouldRun with result %@."
+ "Task %s continuing execution, shouldRun = %{bool}d, after %s."
+ "Task %s deferred after awaiting %s for its cooperative termination. TaskResult: %@"
+ "Task %s returned error in shouldRun: %s"
+ "Task %s returned nil, marking DAS task as completed."
+ "Task %s skipping execution, isDeferred = %{bool}d, after %s."
+ "Task %s skipping execution, shouldRun = %{bool}d, after %s."
+ "Task %s starting with extension: %s"
+ "com.apple.mlhost.container"
+ "deleteWithPolicy:eventsPassingTest:"
- "Completed activity %s after %s. TaskResult: %@"
- "Deferred activity %s after awaiting %s for its cooperative termination. TaskResult: %@"
- "Executing activity %s with extension: %s"
- "Extension %s asked to terminate because of deferral after %s."
- "Extension %s completed doWork with result %@."
- "Extension %s completed shouldRun with result %@."
- "Task %s continuing execution, shouldRun = true."
- "Task %s skipping execution, isDeferred = %{bool}d."
- "Task %s skipping execution, shouldRun = false."
- "deleteEventsPassingTest:"

```
