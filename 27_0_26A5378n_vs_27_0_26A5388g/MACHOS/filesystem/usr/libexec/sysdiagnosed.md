## sysdiagnosed

> `/usr/libexec/sysdiagnosed`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1598.0.0.0.0
-  __TEXT.__text: 0x5b984
+1598.0.4.0.0
+  __TEXT.__text: 0x5bba8
   __TEXT.__auth_stubs: 0x1460
-  __TEXT.__objc_stubs: 0x83e0
-  __TEXT.__objc_methlist: 0x38ac
+  __TEXT.__objc_stubs: 0x8420
+  __TEXT.__objc_methlist: 0x38bc
   __TEXT.__const: 0x1dc
-  __TEXT.__cstring: 0xe8c0
+  __TEXT.__cstring: 0xe93a
   __TEXT.__oslogstring: 0x72e5
   __TEXT.__objc_classname: 0x322
-  __TEXT.__objc_methtype: 0xf05
+  __TEXT.__objc_methtype: 0xf1c
   __TEXT.__gcc_except_tab: 0xd58
-  __TEXT.__objc_methname: 0x8f74
-  __TEXT.__unwind_info: 0xff8
+  __TEXT.__objc_methname: 0x8fca
+  __TEXT.__unwind_info: 0x1000
   __DATA_CONST.__const: 0x1130
-  __DATA_CONST.__cfstring: 0x100e0
+  __DATA_CONST.__cfstring: 0x101c0
   __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x88
-  __DATA_CONST.__objc_arraydata: 0x12d8
-  __DATA_CONST.__objc_arrayobj: 0x1848
+  __DATA_CONST.__objc_arraydata: 0x12e0
+  __DATA_CONST.__objc_arrayobj: 0x1860
   __DATA_CONST.__objc_intobj: 0x228
   __DATA_CONST.__auth_got: 0xa40
   __DATA_CONST.__got: 0x3c0
   __DATA_CONST.__auth_ptr: 0x60
   __DATA.__objc_const: 0x4bb8
-  __DATA.__objc_selrefs: 0x2438
+  __DATA.__objc_selrefs: 0x2448
   __DATA.__objc_ivar: 0x41c
   __DATA.__objc_data: 0xb40
   __DATA.__data: 0x278

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsysdiagnose.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 1623
+  Functions: 1625
   Symbols:   441
-  CStrings:  4371
+  CStrings:  4381
 
CStrings:
+ "--report"
+ "/usr/local/bin/switchcl"
+ "@48@0:8@16@24I32I36@40"
+ "ContainerManager"
+ "RosettaSoftware.spx"
+ "SPLegacySoftwareDataType"
+ "Switch"
+ "TASK_TYPE_CONTAINER_MANAGER"
+ "getSwitchContainer"
+ "logs/ContainerManager"
+ "logs/Switch"
+ "switch_report.json"
+ "taskWithCommand:arguments:inBootstrapDomainOfUID:asUID:outputFile:"
- "/usr/local/bin/ecosystemtool"
- "rosetta-usage"
- "rosetta_usage.txt"
```
