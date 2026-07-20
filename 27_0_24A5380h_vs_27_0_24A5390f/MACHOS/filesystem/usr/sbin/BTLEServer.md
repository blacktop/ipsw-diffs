## BTLEServer

> `/usr/sbin/BTLEServer`

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
-  __TEXT.__text: 0x7ee24
-  __TEXT.__auth_stubs: 0x10d0
-  __TEXT.__objc_stubs: 0xcf60
-  __TEXT.__objc_methlist: 0x7e8c
+2700.38.0.0.0
+  __TEXT.__text: 0x7f744
+  __TEXT.__auth_stubs: 0x10f0
+  __TEXT.__objc_stubs: 0xcf80
+  __TEXT.__objc_methlist: 0x7e94
   __TEXT.__const: 0x900
   __TEXT.__cstring: 0x363c
-  __TEXT.__objc_methname: 0x13341
-  __TEXT.__oslogstring: 0xd77e
+  __TEXT.__objc_methname: 0x13364
+  __TEXT.__oslogstring: 0xd852
   __TEXT.__objc_classname: 0x900
   __TEXT.__objc_methtype: 0x318a
-  __TEXT.__gcc_except_tab: 0x13d0
+  __TEXT.__gcc_except_tab: 0x13c4
   __TEXT.__dlopen_cstrs: 0x197
   __TEXT.__ustring: 0xc6
-  __TEXT.__unwind_info: 0x1bf0
+  __TEXT.__unwind_info: 0x1c18
   __DATA_CONST.__const: 0x17c0
   __DATA_CONST.__cfstring: 0x4ca0
   __DATA_CONST.__objc_classlist: 0x2c8

   __DATA_CONST.__objc_arrayobj: 0x138
   __DATA_CONST.__objc_dictobj: 0x118
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA_CONST.__auth_got: 0x880
+  __DATA_CONST.__auth_got: 0x890
   __DATA_CONST.__got: 0x9b8
-  __DATA_CONST.__auth_ptr: 0x40
+  __DATA_CONST.__auth_ptr: 0x20
   __DATA.__objc_const: 0xfcb8
-  __DATA.__objc_selrefs: 0x42e8
+  __DATA.__objc_selrefs: 0x42f0
   __DATA.__objc_ivar: 0x8a0
   __DATA.__objc_data: 0x1bd0
   __DATA.__data: 0xa50

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3158
-  Symbols:   570
-  CStrings:  5251
+  Functions: 3165
+  Symbols:   572
+  CStrings:  5255
 
Symbols:
+ _dispatch_group_notify
+ _pthread_set_qos_class_self_np
CStrings:
+ "Input report too large (%ld bytes) for report ID 0x%02x"
+ "Peripheral \"%@\" supports deferred service \"%{public}@\" — link now encrypted"
+ "instantiateEncryptionGatedServices"
+ "instantiateEncryptionGatedServices: link not encrypted on \"%@\", nothing to do"
```
