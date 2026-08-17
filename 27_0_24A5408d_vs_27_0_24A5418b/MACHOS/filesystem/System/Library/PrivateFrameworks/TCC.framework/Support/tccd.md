## tccd

> `/System/Library/PrivateFrameworks/TCC.framework/Support/tccd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-913.0.0.0.0
-  __TEXT.__text: 0x8bbb4
+913.0.1.0.0
+  __TEXT.__text: 0x8bcf8
   __TEXT.__auth_stubs: 0x1650
-  __TEXT.__objc_stubs: 0xb680
-  __TEXT.__objc_methlist: 0x5504
-  __TEXT.__cstring: 0x12a07
+  __TEXT.__objc_stubs: 0xb6a0
+  __TEXT.__objc_methlist: 0x550c
+  __TEXT.__cstring: 0x12a48
   __TEXT.__const: 0x6f8
   __TEXT.__gcc_except_tab: 0x2fe8
-  __TEXT.__objc_methname: 0x13084
-  __TEXT.__oslogstring: 0x10851
+  __TEXT.__objc_methname: 0x130ae
+  __TEXT.__oslogstring: 0x108a8
   __TEXT.__objc_classname: 0x6da
   __TEXT.__objc_methtype: 0x235f
   __TEXT.__dlopen_cstrs: 0x90
-  __TEXT.__unwind_info: 0x1a58
+  __TEXT.__unwind_info: 0x1a60
   __DATA_CONST.__const: 0x28c0
   __DATA_CONST.__cfstring: 0x8b00
   __DATA_CONST.__objc_classlist: 0x1f0

   __DATA_CONST.__got: 0x4b8
   __DATA_CONST.__auth_ptr: 0x38
   __DATA.__objc_const: 0xa350
-  __DATA.__objc_selrefs: 0x3700
+  __DATA.__objc_selrefs: 0x3708
   __DATA.__objc_ivar: 0x728
   __DATA.__objc_data: 0x1360
   __DATA.__data: 0x738

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 3014
+  Functions: 3016
   Symbols:   506
-  CStrings:  5901
+  CStrings:  5904
 
Functions:
~ sub_10003cdb0 : 1476 -> 332
+ sub_10003cefc
+ sub_100086d30
CStrings:
+ "%s: service %{public}@ has no usageDescriptionKeyName; cannot resolve reminder purpose"
+ "-[TCCDReminderMonitor reminderPurposeForService:client:context:]"
+ "reminderPurposeForService:client:context:"
```
