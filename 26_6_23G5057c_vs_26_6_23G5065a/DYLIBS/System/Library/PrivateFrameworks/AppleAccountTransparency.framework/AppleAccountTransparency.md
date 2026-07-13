## AppleAccountTransparency

> `/System/Library/PrivateFrameworks/AppleAccountTransparency.framework/AppleAccountTransparency`

```diff

-  __TEXT.__text: 0x52718
-  __TEXT.__auth_stubs: 0x1260
-  __TEXT.__objc_methlist: 0x3f8
-  __TEXT.__const: 0x2cb0
-  __TEXT.__constg_swiftt: 0xd98
-  __TEXT.__swift5_typeref: 0x10d7
+  __TEXT.__text: 0x53e00
+  __TEXT.__auth_stubs: 0x12b0
+  __TEXT.__objc_methlist: 0x3d8
+  __TEXT.__const: 0x2d38
+  __TEXT.__constg_swiftt: 0xde4
+  __TEXT.__swift5_typeref: 0x10da
   __TEXT.__swift5_builtin: 0x50
-  __TEXT.__swift5_reflstr: 0xb52
-  __TEXT.__swift5_fieldmd: 0xb74
-  __TEXT.__swift5_types: 0xb0
-  __TEXT.__oslogstring: 0x2cdc
+  __TEXT.__swift5_reflstr: 0xb7a
+  __TEXT.__swift5_fieldmd: 0xba4
+  __TEXT.__swift5_types: 0xb4
+  __TEXT.__oslogstring: 0x2ede
   __TEXT.__swift5_protos: 0x54
   __TEXT.__swift5_proto: 0x160
-  __TEXT.__cstring: 0x1949
-  __TEXT.__swift5_capture: 0x744
-  __TEXT.__swift_as_entry: 0x1a8
-  __TEXT.__swift_as_ret: 0x1b0
-  __TEXT.__swift5_assocty: 0x108
+  __TEXT.__cstring: 0x1987
+  __TEXT.__swift_as_entry: 0x1b8
+  __TEXT.__swift_as_ret: 0x1c0
+  __TEXT.__swift5_capture: 0x750
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x1658
-  __TEXT.__eh_frame: 0x4ae8
-  __TEXT.__objc_classname: 0x589
-  __TEXT.__objc_methname: 0x1189
-  __TEXT.__objc_methtype: 0x60e
-  __TEXT.__objc_stubs: 0xce0
-  __DATA_CONST.__got: 0x268
+  __TEXT.__swift5_assocty: 0x108
+  __TEXT.__unwind_info: 0x1698
+  __TEXT.__eh_frame: 0x4bf0
+  __TEXT.__objc_classname: 0x5b7
+  __TEXT.__objc_methname: 0x1199
+  __TEXT.__objc_methtype: 0x5fa
+  __TEXT.__objc_stubs: 0xd00
+  __DATA_CONST.__got: 0x270
   __DATA_CONST.__const: 0x90
-  __DATA_CONST.__objc_classlist: 0x90
-  __DATA_CONST.__objc_protolist: 0x70
+  __DATA_CONST.__objc_classlist: 0x98
+  __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x450
-  __DATA_CONST.__objc_protorefs: 0x40
-  __AUTH_CONST.__auth_got: 0x938
-  __AUTH_CONST.__const: 0x23a0
-  __AUTH_CONST.__objc_const: 0x1908
+  __DATA_CONST.__objc_protorefs: 0x38
+  __AUTH_CONST.__auth_got: 0x960
+  __AUTH_CONST.__const: 0x23f8
+  __AUTH_CONST.__objc_const: 0x1978
   __AUTH.__objc_data: 0x4f8
-  __AUTH.__data: 0xa88
-  __DATA.__data: 0x7a8
+  __AUTH.__data: 0xb38
+  __DATA.__data: 0x798
   __DATA.__common: 0x70
   __DATA.__bss: 0x2180
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1429
-  Symbols:   1018
-  CStrings:  547
+  Functions: 1449
+  Symbols:   1022
+  CStrings:  557
 
Sections:
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __AUTH.__objc_data : content changed
Symbols:
+ __DATA__TtC24AppleAccountTransparencyP33_E6620FDB736EB60F373829B9563727CB17BGSystemTaskAcker
+ __IVARS__TtC24AppleAccountTransparencyP33_E6620FDB736EB60F373829B9563727CB17BGSystemTaskAcker
+ __METACLASS_DATA__TtC24AppleAccountTransparencyP33_E6620FDB736EB60F373829B9563727CB17BGSystemTaskAcker
+ _objc_msgSend$setTaskExpiredWithRetryAfter:error:
+ _symbolic BAyt______pIeghHgILrzo_ s5ErrorP
+ _symbolic SS8callSite_t
+ _symbolic Sd
+ _symbolic _____ 24AppleAccountTransparency17BGSystemTaskAcker33_E6620FDB736EB60F373829B9563727CBLLC
- __PROTOCOL_INSTANCE_METHODS__TtP24AppleAccountTransparency14FlowIDSettable_
- __PROTOCOL_METHOD_TYPES__TtP24AppleAccountTransparency14FlowIDSettable_
- __PROTOCOL_PROPERTIES__TtP24AppleAccountTransparency14FlowIDSettable_
- __PROTOCOL__TtP24AppleAccountTransparency14FlowIDSettable_
- _swift_dynamicCastObjCProtocolConditional
- _symbolic $s24AppleAccountTransparency14FlowIDSettableP
CStrings:
+ "AAT XPC timeout: %s after %fs"
+ "AATBackgroundTaskScheduler: No signed-in account — completing task without fetch: %@"
+ "AATBackgroundTaskScheduler: Outer BGST budget (%fs) exceeded — acking as expired"
+ "AATBackgroundTaskScheduler: Task cancelled while fetching altDSID — exiting"
+ "AATBackgroundTaskScheduler: Task completed"
+ "AATBackgroundTaskScheduler: Task expired with retryAfter %f"
+ "AATBackgroundTaskScheduler: Workload exited with %@"
+ "AATBackgroundTaskScheduler: setTaskExpiredWithRetryAfter failed: %{public}@ — falling back to setTaskCompleted"
+ "Failed to connect to daemon: "
+ "XPC call timed out at "
+ "_TtC24AppleAccountTransparencyP33_E6620FDB736EB60F373829B9563727CB17BGSystemTaskAcker"
+ "bgTask"
+ "lock"
+ "makeFetchTask(acker:)"
+ "outerBudget"
+ "setTaskExpiredWithRetryAfter:error:"
- "AATBackgroundTaskScheduler: No signed-in account — completing task without fetch"
- "Failed to connect to daemon"
- "T@\"NSString\",N,C"
- "_TtP24AppleAccountTransparency14FlowIDSettable_"
- "telemetryFlowID"
- "v24@0:8@\"NSString\"16"

```
