## ARKitDaemon

> `/System/Library/PrivateFrameworks/ARKitDaemon.framework/ARKitDaemon`

```diff

-735.0.1.0.0
-  __TEXT.__text: 0xe1a0
+738.0.1.0.0
+  __TEXT.__text: 0xded8
   __TEXT.__auth_stubs: 0x7f0
-  __TEXT.__objc_methlist: 0x1294
+  __TEXT.__objc_methlist: 0x12ac
   __TEXT.__const: 0x90
-  __TEXT.__oslogstring: 0x2189
-  __TEXT.__cstring: 0x73f
-  __TEXT.__gcc_except_tab: 0x65c
-  __TEXT.__unwind_info: 0x4e8
+  __TEXT.__oslogstring: 0x20dd
+  __TEXT.__cstring: 0x713
+  __TEXT.__gcc_except_tab: 0x648
+  __TEXT.__unwind_info: 0x4f0
   __TEXT.__objc_classname: 0x390
-  __TEXT.__objc_methname: 0x2af8
+  __TEXT.__objc_methname: 0x2aee
   __TEXT.__objc_methtype: 0xc41
-  __TEXT.__objc_stubs: 0x1e80
+  __TEXT.__objc_stubs: 0x1ea0
   __DATA_CONST.__got: 0x1d8
   __DATA_CONST.__const: 0x410
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa78
+  __DATA_CONST.__objc_selrefs: 0xa88
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x408
-  __AUTH_CONST.__const: 0x3a0
+  __AUTH_CONST.__const: 0x380
   __AUTH_CONST.__cfstring: 0x760
-  __AUTH_CONST.__objc_const: 0x4450
+  __AUTH_CONST.__objc_const: 0x4410
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x550
-  __DATA.__objc_ivar: 0x12c
+  __DATA.__objc_ivar: 0x124
   __DATA.__data: 0x8a0
   __DATA.__bss: 0x1a0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libchannel.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C35CD3AB-B3EE-39C1-9F94-18EC6A4B0BD9
-  Functions: 358
-  Symbols:   1713
-  CStrings:  889
+  UUID: F340BA81-0434-39E0-BCCE-6A1786157E04
+  Functions: 359
+  Symbols:   1709
+  CStrings:  884
 
Symbols:
+ -[ARServer _createLocalServices]
+ -[ARServer _setupLiteHUDIntegrator]
+ -[ARServer _setupUserProfile]
+ GCC_except_table20
+ GCC_except_table25
+ GCC_except_table36
+ GCC_except_table40
+ GCC_except_table41
+ ___block_literal_global.259
+ ___block_literal_global.266
+ _objc_msgSend$_createLocalServices
+ _objc_msgSend$_setupUserProfile
- -[ARServer _setupHealthReportLogTimer]
- -[ARServer _setupHealthReportLogTimer].cold.1
- -[ARServer _setupHealthReportLogTimer].cold.2
- GCC_except_table17
- GCC_except_table19
- GCC_except_table30
- GCC_except_table37
- GCC_except_table8
- _OBJC_IVAR_$_ARServer._healthReportLogQueue
- _OBJC_IVAR_$_ARServer._healthReportLogTimer
- ___38-[ARServer _setupHealthReportLogTimer]_block_invoke
- ___block_literal_global.109
- ___block_literal_global.267
- ___block_literal_global.270
- _objc_msgSend$_setupHealthReportLogTimer
CStrings:
+ "T@\"NSObject<OS_channel_rt>\",&,V_dispatchChannel"
+ "_createLocalServices"
+ "_setupLiteHUDIntegrator"
+ "_setupUserProfile"
- "%{public}@ <%p>: Could not create timer"
- "%{public}@ <%p>: Timer already exists."
- "Error: %{public}@ <%p>: Could not create timer"
- "Error: %{public}@ <%p>: Timer already exists."
- "T@\"NSObject<OS_channel_rt>\",&,N,V_dispatchChannel"
- "_healthReportLogQueue"
- "_healthReportLogTimer"
- "_setupHealthReportLogTimer"
- "com.apple.arkit.server.healthReportLogQueue"

```
