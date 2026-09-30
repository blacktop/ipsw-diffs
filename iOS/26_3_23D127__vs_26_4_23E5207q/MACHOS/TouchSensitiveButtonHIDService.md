## TouchSensitiveButtonHIDService

> `/System/Library/HIDPlugins/ServicePlugins/TouchSensitiveButtonHIDService.plugin/TouchSensitiveButtonHIDService`

```diff

-9130.2.0.0.0
-  __TEXT.__text: 0x2d58
-  __TEXT.__auth_stubs: 0x3b0
-  __TEXT.__objc_stubs: 0x6a0
-  __TEXT.__objc_methlist: 0x428
+9140.1.0.0.0
+  __TEXT.__text: 0x2eb8
+  __TEXT.__auth_stubs: 0x380
+  __TEXT.__objc_stubs: 0x6c0
+  __TEXT.__objc_methlist: 0x448
   __TEXT.__const: 0xd0
-  __TEXT.__gcc_except_tab: 0x340
-  __TEXT.__cstring: 0x2e6
-  __TEXT.__oslogstring: 0x37d
-  __TEXT.__objc_methname: 0x890
+  __TEXT.__gcc_except_tab: 0x370
+  __TEXT.__cstring: 0x306
+  __TEXT.__oslogstring: 0x3c2
+  __TEXT.__objc_methname: 0x8f5
   __TEXT.__objc_classname: 0x78
-  __TEXT.__objc_methtype: 0x521
-  __TEXT.__unwind_info: 0x188
-  __DATA_CONST.__auth_got: 0x1f0
+  __TEXT.__objc_methtype: 0x53b
+  __TEXT.__unwind_info: 0x1a8
+  __DATA_CONST.__auth_got: 0x1d8
   __DATA_CONST.__got: 0x68
   __DATA_CONST.__const: 0x1f0
-  __DATA_CONST.__cfstring: 0x280
+  __DATA_CONST.__cfstring: 0x2a0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__objc_intobj: 0x60
+  __DATA_CONST.__objc_intobj: 0x90
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x8a0
-  __DATA.__objc_selrefs: 0x2e8
-  __DATA.__objc_ivar: 0x30
+  __DATA.__objc_const: 0x8d0
+  __DATA.__objc_selrefs: 0x300
+  __DATA.__objc_ivar: 0x34
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x120
   __DATA.__bss: 0x20

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BD31A212-851B-345D-B843-2627BB5EBC7F
-  Functions: 73
-  Symbols:   297
-  CStrings:  264
+  UUID: 29AAC013-C46C-366E-BA9C-B0903DDB2114
+  Functions: 82
+  Symbols:   309
+  CStrings:  274
 
Symbols:
+ -[TouchSensitiveButtonHIDService injectAlgsPropertyOnQueue:value:]
+ -[TouchSensitiveButtonHIDService injectAlgsPropertyOnQueue:value:].cold.1
+ -[TouchSensitiveButtonHIDService resetDelay]
+ -[TouchSensitiveButtonHIDService setResetDelay:]
+ GCC_except_table13
+ GCC_except_table15
+ OBJC_IVAR_$_TouchSensitiveButtonHIDService._resetDelay
+ _MGGetProductType
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ ___66-[TouchSensitiveButtonHIDService injectAlgsPropertyOnQueue:value:]_block_invoke
+ _objc_msgSend$injectAlgsPropertyOnQueue:value:
+ _objc_retainAutoreleasedReturnValue
- GCC_except_table14
- ___53-[TouchSensitiveButtonHIDService setProperty:forKey:]_block_invoke
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x8
CStrings:
+ "@\"NSNumber\""
+ "DispatchQueue unavailable when injecting property key: %@, value: %@"
+ "ResetDelayAfterScanDeactivation"
+ "T@\"NSNumber\",&,N,V_resetDelay"
+ "_resetDelay"
+ "injectAlgsPropertyOnQueue:value:"
+ "resetDelay"
+ "setResetDelay:"
+ "v32@0:8@16@24"

```
