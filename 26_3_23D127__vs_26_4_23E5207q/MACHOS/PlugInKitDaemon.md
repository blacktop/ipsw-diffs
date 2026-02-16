## PlugInKitDaemon

> `/System/Library/PrivateFrameworks/PlugInKitDaemon.framework/PlugInKitDaemon`

```diff

-496.0.0.0.0
-  __TEXT.__text: 0x17cb8
-  __TEXT.__auth_stubs: 0xb60
-  __TEXT.__objc_stubs: 0x3040
-  __TEXT.__objc_methlist: 0xfb0
+498.0.0.0.0
+  __TEXT.__text: 0x18fec
+  __TEXT.__auth_stubs: 0xb10
+  __TEXT.__objc_stubs: 0x3080
+  __TEXT.__objc_methlist: 0xfb8
   __TEXT.__const: 0x62
-  __TEXT.__objc_methname: 0x2f22
-  __TEXT.__oslogstring: 0x2c1f
-  __TEXT.__cstring: 0x11b0
+  __TEXT.__objc_methname: 0x2f44
+  __TEXT.__oslogstring: 0x2ce7
+  __TEXT.__cstring: 0x11b6
   __TEXT.__objc_classname: 0x192
   __TEXT.__objc_methtype: 0x6fb
-  __TEXT.__gcc_except_tab: 0x4f4
-  __TEXT.__unwind_info: 0x478
-  __DATA_CONST.__auth_got: 0x5c0
+  __TEXT.__gcc_except_tab: 0x53c
+  __TEXT.__unwind_info: 0x4d8
+  __DATA_CONST.__auth_got: 0x598
   __DATA_CONST.__got: 0x480
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x4f0
-  __DATA_CONST.__cfstring: 0x1140
+  __DATA_CONST.__cfstring: 0x1160
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40

   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA.__objc_const: 0x2768
-  __DATA.__objc_selrefs: 0xde0
+  __DATA.__objc_selrefs: 0xdf0
   __DATA.__objc_ivar: 0x118
   __DATA.__objc_data: 0x4b0
   __DATA.__data: 0x300

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9F92BE14-838D-3FE0-AE3C-1759CA0AE87A
-  Functions: 426
-  Symbols:   1456
-  CStrings:  1223
+  UUID: D7A28228-C24D-3475-B5B2-A6356DAD847F
+  Functions: 447
+  Symbols:   1474
+  CStrings:  1229
 
Symbols:
+ -[PKDPlugIn _subservicesFrom:]
+ GCC_except_table16
+ GCC_except_table38
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _PKServiceExtensionsFormKey
+ _objc_msgSend$_subservicesFrom:
+ _objc_msgSend$arrayWithArray:
- GCC_except_table15
- GCC_except_table36
- _PKServiceExtensionFormKey
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x3
- _objc_retain_x9
CStrings:
+ "%@.%@"
+ "[u %{public}@] [%@(%@)] failed to make the sub mach extension [%@] for [%@]: %{darwin.errno}d. Skip issuing its sandbox extension."
+ "[u %{public}@] [%@(%@)] issued sandbox extension for sub service: %@"
+ "_subservicesFrom:"
+ "arrayWithArray:"

```
