## sysdiagnose_helper

> `/usr/libexec/sysdiagnose_helper`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_capture`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1598.0.0.0.0
-  __TEXT.__text: 0x24bec
-  __TEXT.__auth_stubs: 0xfc0
-  __TEXT.__objc_stubs: 0x17a0
-  __TEXT.__objc_methlist: 0x5dc
-  __TEXT.__const: 0x488
-  __TEXT.__gcc_except_tab: 0x7a8
-  __TEXT.__oslogstring: 0x2671
-  __TEXT.__cstring: 0x972f
+1598.0.4.0.0
+  __TEXT.__text: 0x2523c
+  __TEXT.__auth_stubs: 0xfe0
+  __TEXT.__objc_stubs: 0x17e0
+  __TEXT.__objc_methlist: 0x5e4
+  __TEXT.__const: 0x490
+  __TEXT.__gcc_except_tab: 0x7c4
+  __TEXT.__oslogstring: 0x2781
+  __TEXT.__cstring: 0x97dd
   __TEXT.__objc_classname: 0xfc
   __TEXT.__objc_methtype: 0x2a9
-  __TEXT.__objc_methname: 0x16fb
+  __TEXT.__objc_methname: 0x1744
   __TEXT.__swift5_typeref: 0x91
   __TEXT.__swift5_capture: 0x30
   __TEXT.__constg_swiftt: 0x64

   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x8
   __TEXT.__swift_as_cont: 0xc
-  __TEXT.__unwind_info: 0x630
+  __TEXT.__unwind_info: 0x650
   __TEXT.__eh_frame: 0x130
-  __DATA_CONST.__const: 0x848
-  __DATA_CONST.__cfstring: 0x1d40
+  __DATA_CONST.__const: 0x898
+  __DATA_CONST.__cfstring: 0x1da0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x110
   __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA_CONST.__auth_got: 0x7f0
+  __DATA_CONST.__auth_got: 0x800
   __DATA_CONST.__got: 0x230
   __DATA_CONST.__auth_ptr: 0xe0
   __DATA.__objc_const: 0x700
-  __DATA.__objc_selrefs: 0x650
+  __DATA.__objc_selrefs: 0x660
   __DATA.__objc_ivar: 0x34
   __DATA.__objc_data: 0x290
   __DATA.__data: 0x5c0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 359
-  Symbols:   355
-  CStrings:  2176
+  Functions: 365
+  Symbols:   357
+  CStrings:  2190
 
Symbols:
+ _container_debug_dump_state
+ _container_error_copy_unlocalized_description
CStrings:
+ "Container Manager SPI error. Finished: %d, serviced by pid %d, return success: %d"
+ "Container Manager: failed to dump debug state; error = %{public}s"
+ "Container Manager: failed to open [%{public}s] for writing; error = (%d) %{public}s"
+ "Skipping error stats collection"
+ "TASK_TYPE_CONTAINER_MANAGER"
+ "containerManagerTaskWithDir:withTimeout:"
+ "idleStackFlowVCurveCDPEnd"
+ "idleStackFlowVCurveCDPStart"
+ "idleStackPurgeableValidityCurveAtSlowGC"
+ "json"
+ "squarePurgeable"
+ "state"
+ "stringByAppendingPathExtension:"
+ "v16@?0^{container_error_extended_s=}8"
```
