## FrontBoard

> `/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`

```diff

 1000.0.1.0.0
-  __TEXT.__text: 0x8d7f8
+  __TEXT.__text: 0x8d828
   __TEXT.__auth_stubs: 0xfd0
-  __TEXT.__objc_methlist: 0x5b10
+  __TEXT.__objc_methlist: 0x5b28
   __TEXT.__const: 0x324
   __TEXT.__cstring: 0xb484
   __TEXT.__oslogstring: 0x5f90

   __TEXT.__dlopen_cstrs: 0x20a
   __TEXT.__unwind_info: 0x21e0
   __TEXT.__objc_classname: 0x11d0
-  __TEXT.__objc_methname: 0xf8d9
+  __TEXT.__objc_methname: 0xf90d
   __TEXT.__objc_methtype: 0x3847
-  __TEXT.__objc_stubs: 0xb120
+  __TEXT.__objc_stubs: 0xb140
   __DATA_CONST.__got: 0x900
   __DATA_CONST.__const: 0x2728
   __DATA_CONST.__objc_classlist: 0x2c0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x270
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x37a0
+  __DATA_CONST.__objc_selrefs: 0x37b0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x238
   __DATA_CONST.__objc_arraydata: 0x20
   __AUTH_CONST.__auth_got: 0x7f8
   __AUTH_CONST.__const: 0x840
   __AUTH_CONST.__cfstring: 0x9160
-  __AUTH_CONST.__objc_const: 0xbb20
+  __AUTH_CONST.__objc_const: 0xbb60
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0xcd0
-  __DATA.__objc_ivar: 0x9ac
+  __DATA.__objc_ivar: 0x9b0
   __DATA.__data: 0x1d40
   __DATA.__bss: 0x1f8
   __DATA_DIRTY.__objc_data: 0xeb0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AD4B06F2-99AC-3804-9A96-E32DD0C52BA2
-  Functions: 3046
-  Symbols:   10527
-  CStrings:  6110
+  UUID: ED43ADA7-7107-3242-928F-09708F2FD9F3
+  Functions: 3048
+  Symbols:   10533
+  CStrings:  6114
 
Symbols:
+ -[FBProcessExecutionContext enableMTE]
+ -[FBProcessExecutionContext setEnableMTE:]
+ _OBJC_IVAR_$_FBProcessExecutionContext._enableMTE
+ _objc_msgSend$enableMTE
Functions:
+ -[FBProcessExecutionContext completion]
~ -[FBApplicationProcess _createBootstrapContext] : 548 -> 568
~ -[FBProcessExecutionContext _initWithExecutionContext:] : 392 -> 404
+ -[FBProcessExecutionContext setLaunchIntent:]
CStrings:
+ "TB,N,V_enableMTE"
+ "_enableMTE"
+ "enableMTE"
+ "setEnableMTE:"

```
