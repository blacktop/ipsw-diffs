## AppleLOM

> `/System/Library/PrivateFrameworks/AppleLOM.framework/Versions/A/AppleLOM`

```diff

-74.0.1.0.0
-  __TEXT.__text: 0x1f704
-  __TEXT.__objc_methlist: 0xe04
+74.40.4.0.0
+  __TEXT.__text: 0x1fb60
+  __TEXT.__objc_methlist: 0xe24
   __TEXT.__const: 0xc8
-  __TEXT.__gcc_except_tab: 0xb78
-  __TEXT.__oslogstring: 0x35b9
-  __TEXT.__cstring: 0x1125
-  __TEXT.__unwind_info: 0x6f8
+  __TEXT.__gcc_except_tab: 0xb80
+  __TEXT.__oslogstring: 0x36aa
+  __TEXT.__cstring: 0x1183
+  __TEXT.__unwind_info: 0x708
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7c0
+  __DATA_CONST.__objc_selrefs: 0x7d8
   __DATA_CONST.__objc_superrefs: 0x88
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__got: 0x210
-  __AUTH_CONST.__const: 0x9d0
-  __AUTH_CONST.__cfstring: 0x12e0
-  __AUTH_CONST.__objc_const: 0x2028
+  __AUTH_CONST.__const: 0xa00
+  __AUTH_CONST.__cfstring: 0x1340
+  __AUTH_CONST.__objc_const: 0x2048
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x550
-  __DATA.__objc_ivar: 0x148
+  __DATA.__objc_ivar: 0x14c
   __DATA.__data: 0x420
   __DATA.__bss: 0x80
   __DATA.__common: 0x4

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  Functions: 626
-  Symbols:   1351
-  CStrings:  615
+  Functions: 632
+  Symbols:   1363
+  CStrings:  623
 
Symbols:
+ -[LOMConnection cancel:]
+ -[LOMDeviceServerConsolidated releasePowerCommandAssertion]
+ -[LOMDeviceServerConsolidated takePowerCommandAssertion]
+ GCC_except_table32
+ GCC_except_table39
+ GCC_except_table44
+ GCC_except_table48
+ GCC_except_table51
+ OBJC_IVAR_$_LOMDeviceServerConsolidated._requestPowerAssertionID
+ _IOPMAssertionRelease
+ ___block_descriptor_56_e8_32s40bs48w_e5_v8?0l
+ ___copy_helper_block_e8_32s40b48w
+ ___destroy_helper_block_e8_32s40s48w
+ _nw_connection_cancel
+ _objc_msgSend$cancel:
+ _objc_msgSend$releasePowerCommandAssertion
+ _objc_msgSend$takePowerCommandAssertion
- GCC_except_table24
- GCC_except_table37
- GCC_except_table43
- GCC_except_table47
- GCC_except_table50
CStrings:
+ "%@ cancel connection force:%d"
+ "%@ handleResponse — building RPAK for generation:%llx"
+ "%@ remote connection terminated after data responseSent:%d hasRequest:%d"
+ "%@ sendResponseAck"
+ "%@ sendResponseAck completion error:%@"
+ "%@ takePowerCommandAssertion status:%x id:%u"
+ "LOM power command in progress"
+ "PreventSystemSleep"
+ "com.apple.lightsoutmanagementd.power-command"
- "%@ cancel connection"
```
