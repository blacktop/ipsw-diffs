## ReportCrashService

> `/System/Library/Frameworks/OSAnalytics.framework/XPCServices/ReportCrashService.xpc/ReportCrashService`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1056.0.17.0.0
-  __TEXT.__text: 0x5336c
+1056.0.22.0.0
+  __TEXT.__text: 0x53478
   __TEXT.__auth_stubs: 0x2710
-  __TEXT.__objc_stubs: 0x3de0
-  __TEXT.__objc_methlist: 0x1034
+  __TEXT.__objc_stubs: 0x3e00
+  __TEXT.__objc_methlist: 0x103c
   __TEXT.__const: 0x12f0
-  __TEXT.__cstring: 0x5ac5
-  __TEXT.__objc_methname: 0x47fd
+  __TEXT.__cstring: 0x5ad5
+  __TEXT.__objc_methname: 0x484d
   __TEXT.__oslogstring: 0x348e
   __TEXT.__objc_classname: 0x4d1
   __TEXT.__objc_methtype: 0xd71

   __TEXT.__unwind_info: 0xcd8
   __TEXT.__eh_frame: 0xa10
   __DATA_CONST.__const: 0x1998
-  __DATA_CONST.__cfstring: 0x7aa0
+  __DATA_CONST.__cfstring: 0x7ac0
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x38

   __DATA_CONST.__got: 0x5a0
   __DATA_CONST.__auth_ptr: 0x360
   __DATA.__objc_const: 0x2c10
-  __DATA.__objc_selrefs: 0x1148
+  __DATA.__objc_selrefs: 0x1150
   __DATA.__objc_ivar: 0x280
   __DATA.__objc_data: 0x958
   __DATA.__data: 0xcd0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1128
+  Functions: 1129
   Symbols:   623
-  CStrings:  2318
+  CStrings:  2320
 
CStrings:
+ "Namespace %@, Code 0x%llx"
+ "initWithMetaData:applicationVersion:signpostData:reportedStateData:pid:terminationReason:applicationSpecificInfo:virtualMemoryRegionInfo:exceptionType:exceptionCode:exceptionReason:signal:terminationNamespace:terminationCode:stackTrace:"
+ "terminationReasonApprovedForExternalReports"
- "initWithMetaData:applicationVersion:signpostData:reportedStateData:pid:terminationReason:applicationSpecificInfo:virtualMemoryRegionInfo:exceptionType:exceptionCode:exceptionReason:signal:stackTrace:"
```
