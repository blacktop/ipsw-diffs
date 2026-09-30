## dmd

> `/usr/libexec/dmd`

```diff

-239.0.0.0.0
-  __TEXT.__text: 0x850d0
+240.0.0.0.0
+  __TEXT.__text: 0x86630
   __TEXT.__auth_stubs: 0xef0
-  __TEXT.__objc_stubs: 0xe940
-  __TEXT.__objc_methlist: 0x7bc4
-  __TEXT.__const: 0x160
+  __TEXT.__objc_stubs: 0xe9c0
+  __TEXT.__objc_methlist: 0x7f84
+  __TEXT.__const: 0x168
   __TEXT.__objc_classname: 0x1e74
-  __TEXT.__objc_methname: 0x11801
-  __TEXT.__objc_methtype: 0x1d7f
-  __TEXT.__cstring: 0x5349
-  __TEXT.__oslogstring: 0xb018
-  __TEXT.__gcc_except_tab: 0x11cc
+  __TEXT.__objc_methname: 0x11888
+  __TEXT.__objc_methtype: 0x1d98
+  __TEXT.__cstring: 0x536c
+  __TEXT.__oslogstring: 0xb04d
+  __TEXT.__gcc_except_tab: 0x11d8
   __TEXT.__ustring: 0x80a
   __TEXT.__dlopen_cstrs: 0xaf
-  __TEXT.__unwind_info: 0x2060
+  __TEXT.__unwind_info: 0x2208
   __DATA_CONST.__auth_got: 0x788
-  __DATA_CONST.__got: 0x1330
+  __DATA_CONST.__got: 0x1338
   __DATA_CONST.__const: 0x2748
-  __DATA_CONST.__cfstring: 0x5760
+  __DATA_CONST.__cfstring: 0x5780
   __DATA_CONST.__objc_classlist: 0x6f8
   __DATA_CONST.__objc_catlist: 0x198
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x340
+  __DATA_CONST.__objc_superrefs: 0x618
   __DATA_CONST.__objc_arraydata: 0x508
   __DATA_CONST.__objc_arrayobj: 0x960
   __DATA_CONST.__objc_intobj: 0x318
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x1d298
-  __DATA.__objc_selrefs: 0x4180
-  __DATA.__objc_ivar: 0x42c
+  __DATA.__objc_const: 0x1d2c8
+  __DATA.__objc_selrefs: 0x41a0
+  __DATA.__objc_ivar: 0x430
   __DATA.__objc_data: 0x45b0
   __DATA.__data: 0xc60
   __DATA.__bss: 0x4e8

   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsysdiagnose.dylib
-  UUID: DD51ACA1-E3AF-3596-9C33-A1A0DB4CAF2E
-  Functions: 3103
-  Symbols:   916
-  CStrings:  5290
+  UUID: 6BD420A6-B556-311C-BA0B-243A9863A661
+  Functions: 3199
+  Symbols:   917
+  CStrings:  5300
 
Symbols:
+ _OBJC_CLASS_$_DMCHangDetectionQueue
CStrings:
+ "@\"DMCHangDetectionQueue\""
+ "DMDTaskServerDelegate_task_monitor"
+ "Marking an app in the installing state as installing"
+ "T@\"DMCHangDetectionQueue\",R,N,V_monitorQueue"
+ "_monitorQueue"
+ "initWithQoS:hangThreshold:owner:"
+ "monitorQueue"
+ "queueBlock:"
+ "waitUntilFinished"

```
