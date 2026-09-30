## ABMHelper

> `/System/Library/PrivateFrameworks/ABMHelper.framework/ABMHelper`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__DATA_DIRTY.__objc_data`

```diff

-1576.0.0.0.0
-  __TEXT.__text: 0x1cf444
+1580.0.0.0.0
+  __TEXT.__text: 0x1d058c
   __TEXT.__init_offsets: 0x16c
   __TEXT.__objc_methlist: 0x14
   __TEXT.__const: 0x7220
-  __TEXT.__gcc_except_tab: 0x21888
-  __TEXT.__cstring: 0x88c2
-  __TEXT.__oslogstring: 0xdb4d
-  __TEXT.__unwind_info: 0x7118
+  __TEXT.__gcc_except_tab: 0x21a08
+  __TEXT.__cstring: 0x88e8
+  __TEXT.__oslogstring: 0xdbc4
+  __TEXT.__unwind_info: 0x7148
   __TEXT.__eh_frame: 0x138
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2960
+  __DATA_CONST.__const: 0x2968
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0xb8
   __DATA_CONST.__objc_selrefs: 0x2f0
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__got: 0x578
-  __AUTH_CONST.__const: 0x9120
+  __AUTH_CONST.__const: 0x91b0
   __AUTH_CONST.__cfstring: 0x9c0
   __AUTH_CONST.__objc_const: 0x90
   __AUTH_CONST.__weak_auth_got: 0x20
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__data: 0x460
+  __DATA.__data: 0x468
   __DATA.__bss: 0x20
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsysdiagnose.dylib
-  Functions: 4314
-  Symbols:   6893
-  CStrings:  2789
+  Functions: 4319
+  Symbols:   6901
+  CStrings:  2794
 
Symbols:
+ GCC_except_table149
+ GCC_except_table177
+ GCC_except_table178
+ GCC_except_table185
+ __ZN3abm5trace33kPCIDriverSnapshotDirectorySuffixE
+ __ZN3abm6helper30kCommandCollectAllBasebandLogsE
+ ___copy_helper_block_e8_40c32_ZTSNSt3__110shared_ptrI5TraceEE56c45_ZTSN3ctu2cf11CFSharedRefIK14__CFDictionaryEE64c32_ZTSNSt3__110shared_ptrI5TraceEE
+ ___destroy_helper_block_e8_40c32_ZTSNSt3__110shared_ptrI5TraceEE56c45_ZTSN3ctu2cf11CFSharedRefIK14__CFDictionaryEE64c32_ZTSNSt3__110shared_ptrI5TraceEE
CStrings:
+ "-pci-bin"
+ "CommandCollectAllBasebandLogs"
+ "Request to collect baseband and driver logs"
+ "Snapshot baseband and driver: Begin"
+ "Snapshot baseband and driver: Complete"
```
