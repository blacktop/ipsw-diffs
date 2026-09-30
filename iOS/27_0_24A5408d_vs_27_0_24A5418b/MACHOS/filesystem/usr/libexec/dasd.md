## dasd

> `/usr/libexec/dasd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
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

-2467.2.1.0.0
-  __TEXT.__text: 0x1779b8
+2467.2.2.0.0
+  __TEXT.__text: 0x178114
   __TEXT.__auth_stubs: 0x2230
-  __TEXT.__objc_stubs: 0x1af80
-  __TEXT.__objc_methlist: 0x131b4
+  __TEXT.__objc_stubs: 0x1b040
+  __TEXT.__objc_methlist: 0x131f4
   __TEXT.__const: 0x1568
-  __TEXT.__objc_methname: 0x2e49d
-  __TEXT.__cstring: 0x10566
-  __TEXT.__oslogstring: 0x16be9
+  __TEXT.__objc_methname: 0x2e5bd
+  __TEXT.__cstring: 0x10586
+  __TEXT.__oslogstring: 0x16c79
   __TEXT.__objc_classname: 0x1ca8
-  __TEXT.__objc_methtype: 0x41c1
+  __TEXT.__objc_methtype: 0x4201
   __TEXT.__gcc_except_tab: 0x4f78
   __TEXT.__dlopen_cstrs: 0x552
   __TEXT.__swift5_typeref: 0x966

   __TEXT.__swift_as_cont: 0x80
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x5050
+  __TEXT.__unwind_info: 0x5068
   __TEXT.__eh_frame: 0xbd0
   __DATA_CONST.__const: 0x4f00
-  __DATA_CONST.__cfstring: 0x118e0
+  __DATA_CONST.__cfstring: 0x11940
   __DATA_CONST.__objc_classlist: 0x708
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x218

   __DATA_CONST.__got: 0xe38
   __DATA_CONST.__auth_ptr: 0x190
   __DATA.__objc_const: 0x33ed8
-  __DATA.__objc_selrefs: 0x9cc0
+  __DATA.__objc_selrefs: 0x9cf0
   __DATA.__objc_ivar: 0x1630
   __DATA.__objc_data: 0x4908
   __DATA.__data: 0x2190

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8343
+  Functions: 8349
   Symbols:   1014
-  CStrings:  12437
+  CStrings:  12452
 
CStrings:
+ "%@|v"
+ "%@|v%ld"
+ "@32@0:8@16q24"
+ "FastPass %{public}@ v%d consumed %.1fs this run, %.1fs cumulative"
+ "FastPass %{public}@ v%d has consumed %.1fs of its %.1fs budget, %.1fs remaining"
+ "FastPassConsumedRuntime"
+ "accrueFastPassRuntimeForActivity:"
+ "addConsumedRuntime:forFastPass:semanticVersion:"
+ "clearConsumedRuntimeForFastPass:resetAll:"
+ "consumedRuntimeForFastPass:semanticVersion:"
+ "consumedRuntimeKeyForFastPass:semanticVersion:"
+ "d32@0:8@16q24"
+ "d40@0:8@16q24d32"
+ "remainingRuntimeForFastPass:semanticVersion:budget:"
+ "v40@0:8d16@24q32"
```
