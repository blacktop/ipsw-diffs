## sysdiagnose_helper

> `/usr/libexec/sysdiagnose_helper`

```diff

-1438.100.39.0.0
-  __TEXT.__text: 0x36f80
-  __TEXT.__auth_stubs: 0xbb0
-  __TEXT.__objc_stubs: 0x13e0
-  __TEXT.__objc_methlist: 0x544
+1438.100.41.0.0
+  __TEXT.__text: 0x37358
+  __TEXT.__auth_stubs: 0xbd0
+  __TEXT.__objc_stubs: 0x1420
+  __TEXT.__objc_methlist: 0x55c
   __TEXT.__const: 0x3f8
-  __TEXT.__gcc_except_tab: 0x7ec
-  __TEXT.__oslogstring: 0x202b
-  __TEXT.__cstring: 0x2da00
+  __TEXT.__gcc_except_tab: 0x814
+  __TEXT.__oslogstring: 0x208f
+  __TEXT.__cstring: 0x2da45
   __TEXT.__objc_classname: 0xc4
   __TEXT.__objc_methtype: 0x29b
-  __TEXT.__objc_methname: 0x1434
-  __TEXT.__unwind_info: 0x508
-  __DATA_CONST.__auth_got: 0x5e8
+  __TEXT.__objc_methname: 0x1462
+  __TEXT.__unwind_info: 0x520
+  __DATA_CONST.__auth_got: 0x5f8
   __DATA_CONST.__got: 0x198
   __DATA_CONST.__auth_ptr: 0x98
   __DATA_CONST.__const: 0x640
-  __DATA_CONST.__cfstring: 0x1a60
+  __DATA_CONST.__cfstring: 0x1ac0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__objc_intobj: 0x60
   __DATA.__objc_const: 0x6d8
-  __DATA.__objc_selrefs: 0x568
+  __DATA.__objc_selrefs: 0x578
   __DATA.__objc_ivar: 0x38
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x4b8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libtzupdate.dylib
-  Functions: 306
-  Symbols:   249
-  CStrings:  3935
+  Functions: 312
+  Symbols:   251
+  CStrings:  3944
 
Symbols:
+ _objc_release_x2
+ _sysctlbyname
CStrings:
+ "%s : %d"
+ "Could not fetch lockdown mode state, %d"
+ "Failed to write sysctl.txt"
+ "TASK_TYPE_SYSCTL"
+ "Timed out while fetching sysctls"
+ "_getSysctls:withTimeout:"
+ "getLockdownModeState"
+ "security.mac.lockdown_mode_state"
+ "sysctl.txt"

```
