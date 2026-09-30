## sysdiagnosed

> `/usr/libexec/sysdiagnosed`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
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

-1598.0.0.0.0
-  __TEXT.__text: 0x61128
+1598.0.4.0.0
+  __TEXT.__text: 0x6132c
   __TEXT.__auth_stubs: 0x1700
-  __TEXT.__objc_stubs: 0x93c0
-  __TEXT.__objc_methlist: 0x3f54
+  __TEXT.__objc_stubs: 0x9400
+  __TEXT.__objc_methlist: 0x3f6c
   __TEXT.__const: 0x1cc
-  __TEXT.__cstring: 0x10c36
+  __TEXT.__cstring: 0x10cc9
   __TEXT.__objc_classname: 0x38b
-  __TEXT.__objc_methtype: 0x1825
+  __TEXT.__objc_methtype: 0x183c
   __TEXT.__gcc_except_tab: 0xda8
-  __TEXT.__objc_methname: 0xa737
+  __TEXT.__objc_methname: 0xa78d
   __TEXT.__oslogstring: 0x8111
   __TEXT.__ustring: 0x4e8
-  __TEXT.__unwind_info: 0x1190
+  __TEXT.__unwind_info: 0x1198
   __DATA_CONST.__const: 0x13c0
-  __DATA_CONST.__cfstring: 0x11600
+  __DATA_CONST.__cfstring: 0x11720
   __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x90
-  __DATA_CONST.__objc_arraydata: 0xeb0
-  __DATA_CONST.__objc_arrayobj: 0x1410
+  __DATA_CONST.__objc_arraydata: 0xec0
+  __DATA_CONST.__objc_arrayobj: 0x1428
   __DATA_CONST.__objc_intobj: 0x300
   __DATA_CONST.__objc_floatobj: 0x10
   __DATA_CONST.__auth_got: 0xb90
   __DATA_CONST.__got: 0x470
   __DATA_CONST.__auth_ptr: 0x60
   __DATA.__objc_const: 0x53b8
-  __DATA.__objc_selrefs: 0x29f0
+  __DATA.__objc_selrefs: 0x2a00
   __DATA.__objc_ivar: 0x478
   __DATA.__objc_data: 0xbe0
   __DATA.__data: 0x3a0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsysdiagnose.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 1773
+  Functions: 1775
   Symbols:   505
-  CStrings:  4854
+  CStrings:  4866
 
CStrings:
+ "--report"
+ "/usr/local/bin/switchcl"
+ "@48@0:8@16@24I32I36@40"
+ "ContainerManager"
+ "OR_flags"
+ "Switch"
+ "TASK_TYPE_CONTAINER_MANAGER"
+ "getSwitchContainer"
+ "logs/ContainerManager"
+ "logs/Switch"
+ "switch_report.json"
+ "taskWithCommand:arguments:inBootstrapDomainOfUID:asUID:outputFile:"
```
