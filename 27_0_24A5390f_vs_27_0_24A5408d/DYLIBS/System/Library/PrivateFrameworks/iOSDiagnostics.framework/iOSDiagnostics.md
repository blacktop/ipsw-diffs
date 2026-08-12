## iOSDiagnostics

> `/System/Library/PrivateFrameworks/iOSDiagnostics.framework/iOSDiagnostics`

```diff

-1374.0.27.0.0
-  __TEXT.__text: 0x55dc
-  __TEXT.__objc_methlist: 0xa1c
+1374.2.1.0.0
+  __TEXT.__text: 0x58d8
+  __TEXT.__objc_methlist: 0xa44
   __TEXT.__const: 0x90
-  __TEXT.__cstring: 0xb07
+  __TEXT.__cstring: 0xb11
   __TEXT.__oslogstring: 0x4f5
-  __TEXT.__gcc_except_tab: 0xb8
-  __TEXT.__unwind_info: 0x208
+  __TEXT.__gcc_except_tab: 0xd4
+  __TEXT.__unwind_info: 0x228
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x380
+  __DATA_CONST.__const: 0x3a8
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x718
+  __DATA_CONST.__objc_selrefs: 0x740
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x8
-  __DATA_CONST.__got: 0x140
+  __DATA_CONST.__got: 0x148
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x5a0
-  __AUTH_CONST.__objc_const: 0x1bb8
+  __AUTH_CONST.__objc_const: 0x1c08
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x2d0
-  __DATA.__objc_ivar: 0x78
+  __DATA.__objc_ivar: 0x80
   __DATA.__data: 0x4e0
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 191
-  Symbols:   653
-  CStrings:  94
+  Functions: 195
+  Symbols:   667
+  CStrings:  95
 
Symbols:
+ -[DADiagnosticsLauncher clearDiagnosticsCheckupServiceIfEqualTo:]
+ -[DADiagnosticsLauncher diagnosticsCheckupService]
+ -[DADiagnosticsLauncher setDiagnosticsCheckupService:]
+ GCC_except_table16
+ GCC_except_table18
+ _OBJC_CLASS_$_NSLock
+ _OBJC_IVAR_$_DADiagnosticsLauncher._diagnosticsCheckupServiceLock
+ _OBJC_IVAR_$_DADiagnosticsLauncher._diagnosticsCheckupServiceStorage
+ ___51-[DADiagnosticsLauncher _establishDaemonConnection]_block_invoke
+ ___block_descriptor_48_e8_32w40w_e8_v16?0q8lw32l8w40l8
+ _objc_msgSend$clearDiagnosticsCheckupServiceIfEqualTo:
+ _objc_msgSend$launchDaemon:sessionTerminationHandler:
+ _objc_msgSend$lock
+ _objc_msgSend$setDiagnosticsCheckupService:
+ _objc_msgSend$unlock
+ _objc_retain_x8
- GCC_except_table14
- _objc_msgSend$launchDaemon
CStrings:
+ "v16@?0q8"
```
