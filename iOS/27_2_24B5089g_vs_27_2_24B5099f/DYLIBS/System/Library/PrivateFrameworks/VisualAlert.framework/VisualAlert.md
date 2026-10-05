## VisualAlert

> `/System/Library/PrivateFrameworks/VisualAlert.framework/VisualAlert`

```diff

-3245.8.2.0.0
-  __TEXT.__text: 0xaeec
+3245.8.4.2.0
+  __TEXT.__text: 0xb068
   __TEXT.__objc_methlist: 0x8a4
   __TEXT.__dlopen_cstrs: 0xb8
   __TEXT.__const: 0x20
   __TEXT.__gcc_except_tab: 0x1c0
-  __TEXT.__cstring: 0x1b99
+  __TEXT.__cstring: 0x1bd7
   __TEXT.__oslogstring: 0xb
   __TEXT.__unwind_info: 0x378
   __TEXT.__objc_stubs: 0x0

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3c8
+  __DATA_CONST.__const: 0x3a0
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__got: 0x148
   __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0x1540
+  __AUTH_CONST.__cfstring: 0x1560
   __AUTH_CONST.__objc_const: 0xf78
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x4b0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 197
-  Symbols:   503
-  CStrings:  206
+  Symbols:   502
+  CStrings:  207
 
Symbols:
+ -[AXVisualAlertManager _processNextVisualAlertComponentForPattern:]
+ ___67-[AXVisualAlertManager _processNextVisualAlertComponentForPattern:]_block_invoke
+ ___67-[AXVisualAlertManager _processNextVisualAlertComponentForPattern:]_block_invoke_2
+ ___block_descriptor_64_e8_32s40s48w_e5_v8?0ls32l8w48l8s40l8
- -[AXVisualAlertManager _processNextVisualAlertComponent]
- ___56-[AXVisualAlertManager _processNextVisualAlertComponent]_block_invoke
- ___56-[AXVisualAlertManager _processNextVisualAlertComponent]_block_invoke_2
- ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
- ___block_descriptor_56_e8_32s40w_e5_v8?0ls32l8w40l8
Functions:
~ -[AXVisualAlertManager _beginVisualAlertForType:repeat:skipAutomaticStopOnUserInteraction:bundleId:] : 4436 -> 4460
~ -[AXVisualAlertManager _processNextVisualAlertComponent] -> -[AXVisualAlertManager _processNextVisualAlertComponentForPattern:] : 880 -> 1192
~ ___56-[AXVisualAlertManager _processNextVisualAlertComponent]_block_invoke -> ___67-[AXVisualAlertManager _processNextVisualAlertComponentForPattern:]_block_invoke : 180 -> 208
~ ___56-[AXVisualAlertManager _processNextVisualAlertComponent]_block_invoke_2 -> ___67-[AXVisualAlertManager _processNextVisualAlertComponentForPattern:]_block_invoke_2 : 52 -> 68
CStrings:
+ "Skipping stale visual alert component; active pattern changed"
```
