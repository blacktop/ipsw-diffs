## DeviceCheck

> `/System/Library/Frameworks/DeviceCheck.framework/DeviceCheck`

```diff

-158.0.0.0.0
-  __TEXT.__text: 0xa184
-  __TEXT.__objc_methlist: 0x674
+162.1.0.0.0
+  __TEXT.__text: 0xa178
+  __TEXT.__objc_methlist: 0x65c
   __TEXT.__const: 0xa8
   __TEXT.__cstring: 0x9c0
   __TEXT.__gcc_except_tab: 0x468
   __TEXT.__oslogstring: 0xcbc
-  __TEXT.__unwind_info: 0x360
+  __TEXT.__unwind_info: 0x358
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x468
+  __DATA_CONST.__objc_selrefs: 0x450
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x18
+  __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__got: 0x160
   __AUTH_CONST.__const: 0x1a0
   __AUTH_CONST.__cfstring: 0x640

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 185
-  Symbols:   427
+  Functions: 183
+  Symbols:   426
   CStrings:  129
 
Symbols:
+ -[DCAppAttestDeviceService init]
+ -[DCAppAttestService init]
+ -[DCAppAttestServicePriv init]
+ -[DCAppAttestWebAuthService init]
+ GCC_except_table11
+ GCC_except_table19
+ GCC_except_table23
+ GCC_except_table28
+ GCC_except_table3
+ GCC_except_table34
+ GCC_except_table41
- -[DCAppAttestController setLegacyUserDefaults:]
- -[DCAppAttestController setUserDefaults:]
- -[DCAppAttestDeviceService setAppAttestController:]
- -[DCAppAttestService setAppAttestController:]
- -[DCAppAttestServicePriv setAppAttestController:]
- -[DCAppAttestWebAuthService setAppAttestController:]
- GCC_except_table13
- GCC_except_table21
- GCC_except_table25
- GCC_except_table30
- GCC_except_table36
- GCC_except_table43
```
