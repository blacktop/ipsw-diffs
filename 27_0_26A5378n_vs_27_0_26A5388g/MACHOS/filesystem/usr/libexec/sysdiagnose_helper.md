## sysdiagnose_helper

> `/usr/libexec/sysdiagnose_helper`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1598.0.0.0.0
-  __TEXT.__text: 0x256a4
-  __TEXT.__auth_stubs: 0xdd0
-  __TEXT.__objc_stubs: 0x1b20
-  __TEXT.__objc_methlist: 0x778
-  __TEXT.__const: 0x388
-  __TEXT.__cstring: 0x9529
-  __TEXT.__objc_methname: 0x1c2a
-  __TEXT.__oslogstring: 0x2745
+1598.0.4.0.0
+  __TEXT.__text: 0x25d24
+  __TEXT.__auth_stubs: 0xdf0
+  __TEXT.__objc_stubs: 0x1b60
+  __TEXT.__objc_methlist: 0x780
+  __TEXT.__const: 0x390
+  __TEXT.__cstring: 0x95e4
+  __TEXT.__objc_methname: 0x1c73
+  __TEXT.__oslogstring: 0x284d
   __TEXT.__objc_classname: 0x128
   __TEXT.__objc_methtype: 0x52c
-  __TEXT.__gcc_except_tab: 0x748
-  __TEXT.__unwind_info: 0x5a8
-  __DATA_CONST.__const: 0x780
-  __DATA_CONST.__cfstring: 0x1a80
+  __TEXT.__gcc_except_tab: 0x764
+  __TEXT.__unwind_info: 0x5c0
+  __DATA_CONST.__const: 0x7e0
+  __DATA_CONST.__cfstring: 0x1ae0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_intobj: 0x60
   __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA_CONST.__auth_got: 0x6f8
+  __DATA_CONST.__auth_got: 0x708
   __DATA_CONST.__got: 0x220
   __DATA_CONST.__auth_ptr: 0x98
   __DATA.__objc_const: 0x938
-  __DATA.__objc_selrefs: 0x838
+  __DATA.__objc_selrefs: 0x848
   __DATA.__objc_ivar: 0x34
   __DATA.__objc_data: 0x230
   __DATA.__data: 0x19a0

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 343
-  Symbols:   308
-  CStrings:  2270
+  Functions: 349
+  Symbols:   310
+  CStrings:  2284
 
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
