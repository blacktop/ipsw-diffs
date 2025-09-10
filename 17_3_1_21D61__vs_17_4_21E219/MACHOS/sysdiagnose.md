## sysdiagnose

> `/usr/bin/sysdiagnose`

```diff

-1270.80.1.0.0
-  __TEXT.__text: 0x4114
-  __TEXT.__auth_stubs: 0x610
+1295.100.44.0.0
+  __TEXT.__text: 0x41c0
+  __TEXT.__auth_stubs: 0x600
   __TEXT.__objc_stubs: 0x820
   __TEXT.__objc_methlist: 0xac
-  __TEXT.__const: 0x50
+  __TEXT.__const: 0x58
   __TEXT.__gcc_except_tab: 0x60
-  __TEXT.__cstring: 0x22ea
+  __TEXT.__cstring: 0x2315
   __TEXT.__oslogstring: 0x68d
   __TEXT.__objc_methname: 0x5f6
   __TEXT.__objc_classname: 0x14
   __TEXT.__objc_methtype: 0x5b
   __TEXT.__unwind_info: 0x124
-  __DATA_CONST.__auth_got: 0x318
+  __DATA_CONST.__auth_got: 0x310
   __DATA_CONST.__got: 0xb0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x2c8
-  __DATA_CONST.__cfstring: 0x6a0
+  __DATA_CONST.__const: 0x2e8
+  __DATA_CONST.__cfstring: 0x6c0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x98
+  __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0xd0
   __DATA.__objc_selrefs: 0x238
-  __DATA.__objc_classrefs: 0x98
-  __DATA.__objc_superrefs: 0x8
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x30

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsysdiagnose.dylib
-  UUID: 9558F517-7577-3E51-B84D-242CC950F381
-  Functions: 67
-  Symbols:   149
-  CStrings:  285
+  UUID: B4CE9F6D-B20D-3DAE-95AE-2DCF303690A8
+  Functions: 66
+  Symbols:   148
+  CStrings:  286
 
Symbols:
- ___assert_rtn
CStrings:
+ "Platform does not support --collectAllTrusted flag"
+ "Sysdiagnoses can be found at '%s'\n"
+ "collectAllTrusted"
+ "shouldCollectAllTrusted"
- "Sysdiagnoses can be found at \"%s\""
- "bar_count <= bar_length"
- "generateProgressBar"
- "main.m"

```
