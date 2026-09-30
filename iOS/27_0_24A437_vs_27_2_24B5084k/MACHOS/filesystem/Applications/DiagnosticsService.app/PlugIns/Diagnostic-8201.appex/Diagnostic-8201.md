## Diagnostic-8201

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8201.appex/Diagnostic-8201`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-60.0.0.0.0
-  __TEXT.__text: 0x255e4
+62.0.0.0.0
+  __TEXT.__text: 0x2ceb4
   __TEXT.__auth_stubs: 0x900
   __TEXT.__objc_stubs: 0xb60
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x324
-  __TEXT.__gcc_except_tab: 0x2c0c
+  __TEXT.__gcc_except_tab: 0x3c58
   __TEXT.__const: 0x258
-  __TEXT.__cstring: 0x676b
+  __TEXT.__cstring: 0x67b9
+  __TEXT.__oslogstring: 0xa99
   __TEXT.__objc_classname: 0x50
-  __TEXT.__objc_methname: 0xc46
+  __TEXT.__objc_methname: 0xc50
   __TEXT.__objc_methtype: 0x6c9
   __TEXT.__ustring: 0x14a
-  __TEXT.__oslogstring: 0xa8e
-  __TEXT.__unwind_info: 0xa38
-  __DATA_CONST.__const: 0x5a8
-  __DATA_CONST.__cfstring: 0x4ac0
+  __TEXT.__unwind_info: 0xa30
+  __DATA_CONST.__const: 0x5e0
+  __DATA_CONST.__cfstring: 0x4b40
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__auth_got: 0x498
   __DATA_CONST.__got: 0x360
-  __DATA.__objc_const: 0x678
+  __DATA.__objc_const: 0x698
   __DATA.__objc_selrefs: 0x3e8
-  __DATA.__objc_ivar: 0x70
+  __DATA.__objc_ivar: 0x74
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0xc0
   __DATA.__common: 0x10

   - /usr/lib/libobjc.A.dylib
   Functions: 495
   Symbols:   438
-  CStrings:  1089
+  CStrings:  1095
 
Symbols:
+ _objc_retain_x25
- _NSLog
CStrings:
+ "%{public}s"
+ "ETROG projector version detected"
+ "ExclaveStatus"
+ "PEARL_PROJECTOR_HW_VERSION"
+ "RGB"
+ "m_isEtrog"
```
