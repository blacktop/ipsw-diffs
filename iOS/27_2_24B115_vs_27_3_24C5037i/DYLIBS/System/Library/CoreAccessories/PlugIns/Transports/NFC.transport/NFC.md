## NFC

> `/System/Library/CoreAccessories/PlugIns/Transports/NFC.transport/NFC`

```diff

-1219.42.3.0.0
-  __TEXT.__text: 0x9664
-  __TEXT.__objc_methlist: 0x3c4
-  __TEXT.__cstring: 0xe6c
-  __TEXT.__const: 0x1c8c
-  __TEXT.__oslogstring: 0x17a2
+1219.60.10.0.0
+  __TEXT.__text: 0x9aa8
+  __TEXT.__objc_methlist: 0x3ec
+  __TEXT.__cstring: 0xe77
+  __TEXT.__const: 0x1c9c
+  __TEXT.__oslogstring: 0x18be
   __TEXT.__gcc_except_tab: 0xfc
   __TEXT.__dlopen_cstrs: 0xc2
-  __TEXT.__unwind_info: 0x2b8
+  __TEXT.__unwind_info: 0x2c0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x490
+  __DATA_CONST.__objc_selrefs: 0x4a8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x38
-  __DATA_CONST.__got: 0x180
+  __DATA_CONST.__got: 0x188
   __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0x1120
+  __AUTH_CONST.__cfstring: 0x1140
   __AUTH_CONST.__objc_const: 0x5d8
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 149
-  Symbols:   667
-  CStrings:  278
+  Functions: 151
+  Symbols:   672
+  CStrings:  283
 
Symbols:
+ -[AccessoryTransportPluginNFC _exceptionForEdgeCompensationCase:withProperties:]
+ -[AccessoryTransportPluginNFC _isEdgeCompensationCaseSupported]
+ -[AccessoryTransportPluginNFC _isEdgeCompensationCaseTagId:]
+ GCC_except_table27
+ GCC_except_table29
+ GCC_except_table39
+ GCC_except_table53
+ _kACCProperties_Endpoint_NFC_ShowEdgeCompensationAlert
+ _objc_retain_x3
+ _os_eligibility_get_domain_answer
- GCC_except_table24
- GCC_except_table26
- GCC_except_table36
- GCC_except_table50
- _OUTLINED_FUNCTION_14
CStrings:
+ "NFC transport plugin: EdgeCompensation Case eligibility (TRECHUS) err:%d answer:%d"
+ "NFC transport plugin: EdgeCompensation Case is not supported on this product (%@)"
+ "NFC transport plugin: device not eligible for EdgeCompensation Case"
+ "NFC transport plugin: not an EdgeCompensation Case"
+ "iPhone19,4"
```
