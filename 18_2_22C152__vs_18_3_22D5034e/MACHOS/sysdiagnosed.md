## sysdiagnosed

> `/usr/libexec/sysdiagnosed`

```diff

-1438.60.6.0.0
-  __TEXT.__text: 0x63a7c
+1438.80.3.0.0
+  __TEXT.__text: 0x63bac
   __TEXT.__auth_stubs: 0x16d0
-  __TEXT.__objc_stubs: 0x9320
-  __TEXT.__objc_methlist: 0x3988
+  __TEXT.__objc_stubs: 0x9340
+  __TEXT.__objc_methlist: 0x3990
   __TEXT.__const: 0x1b4
-  __TEXT.__cstring: 0x104c2
+  __TEXT.__cstring: 0x104ea
   __TEXT.__objc_classname: 0x3a4
   __TEXT.__objc_methtype: 0x164e
   __TEXT.__gcc_except_tab: 0x1248
-  __TEXT.__objc_methname: 0xa531
+  __TEXT.__objc_methname: 0xa545
   __TEXT.__oslogstring: 0x8d30
   __TEXT.__ustring: 0x4e8
   __TEXT.__unwind_info: 0x1108

   __DATA_CONST.__got: 0x418
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x1350
-  __DATA_CONST.__cfstring: 0x10b00
+  __DATA_CONST.__cfstring: 0x10b40
   __DATA_CONST.__objc_classlist: 0x138
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x90
-  __DATA_CONST.__objc_arraydata: 0xe00
-  __DATA_CONST.__objc_arrayobj: 0x12d8
+  __DATA_CONST.__objc_arraydata: 0xe08
+  __DATA_CONST.__objc_arrayobj: 0x12f0
   __DATA_CONST.__objc_intobj: 0x300
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_floatobj: 0x10
   __DATA.__objc_const: 0x5be8
-  __DATA.__objc_selrefs: 0x27e0
+  __DATA.__objc_selrefs: 0x27e8
   __DATA.__objc_ivar: 0x46c
   __DATA.__objc_data: 0xc30
   __DATA.__data: 0x2c8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsysdiagnose.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 1692
+  Functions: 1693
   Symbols:   500
-  CStrings:  5202
+  CStrings:  5205
 
CStrings:
+ "getSysctlsContainer"
+ "security.mac.lockdown_mode_state"
+ "sysctl"

```
