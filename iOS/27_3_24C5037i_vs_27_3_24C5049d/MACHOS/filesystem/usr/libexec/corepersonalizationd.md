## corepersonalizationd

> `/usr/libexec/corepersonalizationd`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_acfuncs`
- `__DATA_CONST.__objc_classlist`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-5.8.0.2.0
-  __TEXT.__text: 0x49190
-  __TEXT.__auth_stubs: 0x2390
+5.12.0.0.0
+  __TEXT.__text: 0x4d65c
+  __TEXT.__auth_stubs: 0x2630
   __TEXT.__objc_stubs: 0x140
-  __TEXT.__const: 0x1840
-  __TEXT.__swift5_typeref: 0xa98
+  __TEXT.__const: 0x1908
+  __TEXT.__swift5_typeref: 0xac6
   __TEXT.__swift5_capture: 0x1e8
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x308
+  __TEXT.__constg_swiftt: 0x388
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_reflstr: 0x219
-  __TEXT.__swift5_fieldmd: 0x1b8
-  __TEXT.__swift5_types: 0x24
-  __TEXT.__swift_as_entry: 0x1e8
-  __TEXT.__swift_as_ret: 0x2e0
-  __TEXT.__swift_as_cont: 0x4f4
+  __TEXT.__swift5_reflstr: 0x249
+  __TEXT.__swift5_fieldmd: 0x1d0
+  __TEXT.__swift5_types: 0x28
+  __TEXT.__swift_as_entry: 0x1fc
+  __TEXT.__swift_as_ret: 0x30c
+  __TEXT.__swift_as_cont: 0x52c
   __TEXT.__objc_classname: 0x15f
-  __TEXT.__objc_methname: 0x1d1
+  __TEXT.__objc_methname: 0x1f1
   __TEXT.__objc_methtype: 0x1
-  __TEXT.__cstring: 0x4eb
-  __TEXT.__oslogstring: 0xf68
+  __TEXT.__oslogstring: 0x12e8
+  __TEXT.__cstring: 0x59e
   __TEXT.__swift5_proto: 0x84
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_assocty: 0xa0
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_acfuncs: 0xa0
-  __TEXT.__unwind_info: 0x1e08
-  __TEXT.__eh_frame: 0x5ed0
-  __DATA_CONST.__const: 0x7c8
+  __TEXT.__unwind_info: 0x1b38
+  __TEXT.__eh_frame: 0x62c0
+  __DATA_CONST.__const: 0x7f8
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x11d0
-  __DATA_CONST.__got: 0xc08
-  __DATA_CONST.__auth_ptr: 0x590
-  __DATA.__objc_const: 0x538
+  __DATA_CONST.__auth_got: 0x1320
+  __DATA_CONST.__got: 0xc88
+  __DATA_CONST.__auth_ptr: 0x5a0
+  __DATA.__objc_const: 0x578
   __DATA.__objc_selrefs: 0x50
   __DATA.__objc_data: 0xa0
-  __DATA.__data: 0xc40
+  __DATA.__data: 0xcf0
   __DATA.__common: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/IntelligencePlatformLibrary.framework/IntelligencePlatformLibrary
   - /System/Library/PrivateFrameworks/ProactiveDaemonSupport.framework/ProactiveDaemonSupport
   - /System/Library/PrivateFrameworks/XPCDistributed.framework/XPCDistributed
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1664
-  Symbols:   139
-  CStrings:  135
+  Functions: 1692
+  Symbols:   146
+  CStrings:  149
 
Symbols:
+ _CFBooleanGetTypeID
+ _CFBooleanGetValue
+ _CFGetTypeID
+ _MGCopyAnswerWithError
+ _swift_beginAccess
+ _swift_dynamicCastUnknownClassUnconditional
+ _swift_endAccess
CStrings:
+ "Action Suggestions is active, serving"
+ "Action Suggestions is not active, exiting without serving"
+ "Could not reject sessions on %s: %@"
+ "DeviceSupportsGenerativeModelSystems"
+ "This device does not support Apple Intelligence"
+ "com.apple.corepersonalization.server.workflowExecution"
+ "corepersonalizationd not serving: could not read supportsGenerativeModelSystems (MobileGestalt error %{public}d)"
+ "corepersonalizationd not serving: this device does not support Apple Intelligence (supportsGenerativeModelSystems: false)"
+ "corepersonalizationd started (supportsGenerativeModelSystems: true)"
+ "corepersonalizationd/DistributedWorkflowExecutionServer.swift"
+ "executionStatus"
+ "runWorkOrder %s: could not read the status of execution %s — returning without waiting: %@"
+ "runWorkOrder %s: execution %s is %{public}s — nothing to wait for"
+ "runWorkOrder %s: execution %s still awaiting Cascade confirmation after %{public}s — returning anyway"
+ "runWorkOrder %s: no client is waiting on this run — not holding the reply for Cascade confirmation"
+ "runWorkOrder for %s, rid=%s, priority=%{public}s"
+ "unsupportedDeviceListeners"
- "Failed to acquire the memory graph handle: "
- "corepersonalizationd started"
- "runWorkOrder for %s, rid=%s"
```
