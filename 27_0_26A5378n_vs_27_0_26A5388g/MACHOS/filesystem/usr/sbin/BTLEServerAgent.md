## BTLEServerAgent

> `/usr/sbin/BTLEServerAgent`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_ivar`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2700.35.0.0.0
-  __TEXT.__text: 0x48ff0
-  __TEXT.__auth_stubs: 0xc70
-  __TEXT.__objc_stubs: 0x7160
-  __TEXT.__objc_methlist: 0x4874
+2700.38.0.0.0
+  __TEXT.__text: 0x49924
+  __TEXT.__auth_stubs: 0xc90
+  __TEXT.__objc_stubs: 0x7180
+  __TEXT.__objc_methlist: 0x487c
   __TEXT.__objc_classname: 0x524
   __TEXT.__objc_methtype: 0x1b55
   __TEXT.__const: 0x680
-  __TEXT.__gcc_except_tab: 0x10b4
+  __TEXT.__gcc_except_tab: 0x10a8
   __TEXT.__cstring: 0x1f43
-  __TEXT.__oslogstring: 0x6f6f
-  __TEXT.__objc_methname: 0xaeb4
+  __TEXT.__oslogstring: 0x7043
+  __TEXT.__objc_methname: 0xaed7
   __TEXT.__ustring: 0xbe
-  __TEXT.__unwind_info: 0x1108
+  __TEXT.__unwind_info: 0x1130
   __DATA_CONST.__const: 0xe98
   __DATA_CONST.__cfstring: 0x24e0
   __DATA_CONST.__objc_classlist: 0x190

   __DATA_CONST.__objc_arraydata: 0x188
   __DATA_CONST.__objc_arrayobj: 0xc0
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA_CONST.__auth_got: 0x650
+  __DATA_CONST.__auth_got: 0x660
   __DATA_CONST.__got: 0x518
-  __DATA_CONST.__auth_ptr: 0x38
+  __DATA_CONST.__auth_ptr: 0x20
   __DATA.__objc_const: 0x9a78
-  __DATA.__objc_selrefs: 0x2698
+  __DATA.__objc_selrefs: 0x26a0
   __DATA.__objc_ivar: 0x4f0
   __DATA.__objc_data: 0xfa0
   __DATA.__data: 0x660

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1793
-  Symbols:   366
-  CStrings:  3071
+  Functions: 1801
+  Symbols:   368
+  CStrings:  3075
 
Symbols:
+ _dispatch_group_notify
+ _pthread_set_qos_class_self_np
CStrings:
+ "Input report too large (%ld bytes) for report ID 0x%02x"
+ "Peripheral \"%@\" supports deferred service \"%{public}@\" — link now encrypted"
+ "instantiateEncryptionGatedServices"
+ "instantiateEncryptionGatedServices: link not encrypted on \"%@\", nothing to do"
```
