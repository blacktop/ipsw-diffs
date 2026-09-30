## ReportCrash

> `/System/Library/CoreServices/ReportCrash`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__oslogstring`
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
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1056.0.17.0.0
-  __TEXT.__text: 0x50a7c
+1056.0.22.0.0
+  __TEXT.__text: 0x50b60
   __TEXT.__auth_stubs: 0x22e0
-  __TEXT.__objc_stubs: 0x4380
-  __TEXT.__objc_methlist: 0x10c0
-  __TEXT.__cstring: 0x5b8b
+  __TEXT.__objc_stubs: 0x43a0
+  __TEXT.__objc_methlist: 0x10d0
+  __TEXT.__cstring: 0x5bab
   __TEXT.__const: 0x10f8
-  __TEXT.__objc_methname: 0x4bad
+  __TEXT.__objc_methname: 0x4bed
   __TEXT.__oslogstring: 0x2e71
   __TEXT.__objc_classname: 0x2b4
   __TEXT.__objc_methtype: 0xa9e

   __TEXT.__unwind_info: 0xc28
   __TEXT.__eh_frame: 0x638
   __DATA_CONST.__const: 0x1a88
-  __DATA_CONST.__cfstring: 0x7c60
+  __DATA_CONST.__cfstring: 0x7c80
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10

   __DATA_CONST.__got: 0x610
   __DATA_CONST.__auth_ptr: 0x338
   __DATA.__objc_const: 0x2980
-  __DATA.__objc_selrefs: 0x12b8
+  __DATA.__objc_selrefs: 0x12c0
   __DATA.__objc_ivar: 0x2c4
   __DATA.__objc_data: 0x968
   __DATA.__data: 0x9f0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1129
+  Functions: 1130
   Symbols:   848
-  CStrings:  2347
+  CStrings:  2349
 
CStrings:
+ "ECOUnsupportedApplicationListClient"
+ "Namespace %@, Code 0x%llx"
+ "failed to create ECOUnsupportedApplicationListClient for Rosetta usage check"
+ "initWithMetaData:applicationVersion:signpostData:reportedStateData:pid:terminationReason:applicationSpecificInfo:virtualMemoryRegionInfo:exceptionType:exceptionCode:exceptionReason:signal:terminationNamespace:terminationCode:stackTrace:"
+ "terminationReasonApprovedForExternalReports"
- "UnsupportedApplicationListClient"
- "failed to create UnsupportedApplicationListClient for Rosetta usage check"
- "initWithMetaData:applicationVersion:signpostData:reportedStateData:pid:terminationReason:applicationSpecificInfo:virtualMemoryRegionInfo:exceptionType:exceptionCode:exceptionReason:signal:stackTrace:"
```
