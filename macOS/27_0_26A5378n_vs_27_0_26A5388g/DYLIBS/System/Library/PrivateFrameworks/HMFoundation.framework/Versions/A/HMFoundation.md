## HMFoundation

> `/System/Library/PrivateFrameworks/HMFoundation.framework/Versions/A/HMFoundation`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_protos`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__AUTH.__thread_vars`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-1484.2.0.0.0
-  __TEXT.__text: 0x9b428
+1490.2.0.0.0
+  __TEXT.__text: 0x9b8fc
   __TEXT.__delay_helper: 0xdc
-  __TEXT.__objc_methlist: 0x7714
+  __TEXT.__objc_methlist: 0x773c
   __TEXT.__const: 0x3028
   __TEXT.__dlopen_cstrs: 0x10a
   __TEXT.__swift5_typeref: 0xb6e

   __TEXT.__swift5_fieldmd: 0x7c4
   __TEXT.__swift5_proto: 0x6c
   __TEXT.__swift5_types: 0xb4
-  __TEXT.__cstring: 0x2f88
+  __TEXT.__cstring: 0x2fab
   __TEXT.__swift5_capture: 0x670
   __TEXT.__swift_as_entry: 0x19c
   __TEXT.__swift_as_ret: 0x1c4
   __TEXT.__swift_as_cont: 0x230
   __TEXT.__swift5_protos: 0x20
-  __TEXT.__oslogstring: 0x7976
-  __TEXT.__gcc_except_tab: 0x189c
+  __TEXT.__oslogstring: 0x7abd
+  __TEXT.__gcc_except_tab: 0x18ec
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x30c8
+  __TEXT.__unwind_info: 0x30d8
   __TEXT.__eh_frame: 0x3268
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x1b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3060
+  __DATA_CONST.__objc_selrefs: 0x3078
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x380
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__got: 0x800
   __AUTH_CONST.__const: 0x32c0
   __AUTH_CONST.__cfstring: 0x47a0
-  __AUTH_CONST.__objc_const: 0xdfb0
+  __AUTH_CONST.__objc_const: 0xdfe0
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x10d0
+  __AUTH_CONST.__auth_got: 0x10d8
   __AUTH.__objc_data: 0x1180
   __AUTH.__data: 0x1e8
   __AUTH.__thread_vars: 0x18

   __DATA.__objc_ivar: 0x19c
   __DATA.__data: 0x250c
   __DATA.__bss: 0xa10
-  __DATA_DIRTY.__objc_ivar: 0x558
+  __DATA_DIRTY.__objc_ivar: 0x55c
   __DATA_DIRTY.__objc_data: 0x1a40
   __DATA_DIRTY.__data: 0x270
   __DATA_DIRTY.__bss: 0x5c8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3647
-  Symbols:   6498
-  CStrings:  1362
+  Functions: 3650
+  Symbols:   6504
+  CStrings:  1369
 
Symbols:
+ +[HMFHTTPRequestHandler _isValidMethodPredicate:]
+ -[HMFMemoryMonitor setTriggerSuppressionExpiry:]
+ -[HMFMemoryMonitor triggerProcessMemoryWarning]
+ -[HMFMemoryMonitor triggerSuppressionExpiry]
+ _objc_msgSend$_isValidMethodPredicate:
+ _objc_msgSend$setTriggerSuppressionExpiry:
+ _objc_msgSend$triggerSuppressionExpiry
+ _sysctlbyname
- +[HMFHTTPRequestHandler _isValidMethodPrediate:]
- _objc_msgSend$_isValidMethodPrediate:
CStrings:
+ "Error (%s) sending internal memory pressure event"
+ "Success sending internal memory pressure event"
+ "Suppressing observer dispatch for triggered %@"
+ "[%{public}@] Error (%s) sending internal memory pressure event"
+ "[%{public}@] Success sending internal memory pressure event"
+ "[%{public}@] Suppressing observer dispatch for triggered %@"
+ "kern.memorystatus_vm_pressure_send"
```
