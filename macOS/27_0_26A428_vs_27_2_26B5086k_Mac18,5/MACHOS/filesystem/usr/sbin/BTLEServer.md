## BTLEServer

> `/usr/sbin/BTLEServer`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2700.39.0.0.0
+2701.2.0.0.0
   __TEXT.__text: 0x48aa8
   __TEXT.__auth_stubs: 0xc70
   __TEXT.__objc_stubs: 0x7180
-  __TEXT.__objc_methlist: 0x487c
+  __TEXT.__objc_methlist: 0x489c
   __TEXT.__objc_classname: 0x524
   __TEXT.__objc_methtype: 0x1b55
   __TEXT.__cstring: 0x1f82
   __TEXT.__const: 0x680
-  __TEXT.__objc_methname: 0xaed7
+  __TEXT.__objc_methname: 0xaf11
   __TEXT.__oslogstring: 0x70ae
   __TEXT.__gcc_except_tab: 0x10a8
   __TEXT.__ustring: 0xbe

   __DATA_CONST.__auth_got: 0x650
   __DATA_CONST.__got: 0x510
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA.__objc_const: 0x9a78
-  __DATA.__objc_selrefs: 0x26a0
+  __DATA.__objc_const: 0x9a88
+  __DATA.__objc_selrefs: 0x26b0
   __DATA.__objc_ivar: 0x4f0
   __DATA.__objc_data: 0xfa0
   __DATA.__data: 0x660

   - /usr/lib/libobjc.A.dylib
   Functions: 1802
   Symbols:   366
-  CStrings:  3073
+  CStrings:  3075
 
CStrings:
+ "deviceInactivityTimeout:"
+ "deviceNoFirmwareUpdateAvailable:"
```
