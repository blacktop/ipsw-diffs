## libMetalMetricsInterpose.dylib

> `/usr/lib/libMetalMetricsInterpose.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__thread_vars`

```diff

-5.0.22.0.0
-  __TEXT.__text: 0x14800
-  __TEXT.__auth_stubs: 0x6e0
-  __TEXT.__objc_stubs: 0xf40
+5.0.24.0.0
+  __TEXT.__text: 0x149f0
+  __TEXT.__auth_stubs: 0x720
+  __TEXT.__objc_stubs: 0xf80
   __TEXT.__objc_methlist: 0xf8
-  __TEXT.__gcc_except_tab: 0x1308
+  __TEXT.__gcc_except_tab: 0x12fc
   __TEXT.__const: 0x4c8
-  __TEXT.__cstring: 0x5c9
-  __TEXT.__objc_methname: 0xdab
+  __TEXT.__cstring: 0x689
+  __TEXT.__objc_methname: 0xdc2
   __TEXT.__objc_classname: 0x1e
   __TEXT.__objc_methtype: 0x3b7
   __TEXT.__unwind_info: 0x8d8
-  __DATA_CONST.__const: 0xc08
-  __DATA_CONST.__cfstring: 0x1e0
+  __DATA_CONST.__const: 0xc48
+  __DATA_CONST.__cfstring: 0x2c0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x380
+  __DATA_CONST.__auth_got: 0x3a0
   __DATA_CONST.__got: 0x110
   __DATA.__objc_const: 0x220
-  __DATA.__objc_selrefs: 0x438
+  __DATA.__objc_selrefs: 0x448
   __DATA.__objc_ivar: 0x2c
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x10
   __DATA.__thread_vars: 0xa8
   __DATA.__thread_bss: 0x7
   __DATA.__common: 0x9
-  __DATA.__bss: 0xf8
+  __DATA.__bss: 0x118
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics
   - /System/Library/Frameworks/CoreImage.framework/Versions/A/CoreImage

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 391
-  Symbols:   962
-  CStrings:  222
+  Functions: 399
+  Symbols:   978
+  CStrings:  232
 
Symbols:
+ FPMTLMetricsCanUseIMPTrampolines
+ FPMTLMetricsIsElectronOrCEFHelperProcess.isHelper
+ FPMTLMetricsIsElectronOrCEFHelperProcess.onceToken
+ FPMTLMetricsIsExcluded
+ FPMTLMetricsIsExcluded.isBlastDoor
+ FPMTLMetricsIsExcluded.onceToken
+ FPMTLMetricsIsProcessTranslated.onceToken
+ FPMTLMetricsIsProcessTranslated.ret
+ GCC_except_table20
+ GCC_except_table55
+ GCC_except_table63
+ _CFBundleGetIdentifier
+ _CFBundleGetMainBundle
+ _CFStringCompare
+ _FPMTLMetricsCanUseIMPTrampolines
+ _FPMTLMetricsIsExcluded
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ ___FPMTLMetricsIsElectronOrCEFHelperProcess_block_invoke
+ ___FPMTLMetricsIsExcluded_block_invoke
+ ___FPMTLMetricsIsProcessTranslated_block_invoke
+ _objc_msgSend$hasSuffix:
+ _objc_msgSend$processName
+ _sysctlbyname
- FPMTLMetricsInterposeEnableCompilerStats
- GCC_except_table18
- GCC_except_table21
- GCC_except_table54
- GCC_except_table77
- __ZZ40FPMTLMetricsInterposeEnableCompilerStatsE10isAppleGPU
- __ZZ40FPMTLMetricsInterposeEnableCompilerStatsE9onceToken
- ___FPMTLMetricsInterposeEnableCompilerStats_block_invoke
CStrings:
+ " Helper (GPU)"
+ " Helper (Plugin)"
+ " Helper (Renderer)"
+ "com.apple.InCallService"
+ "com.apple.MessagesAirlockService"
+ "com.apple.MessagesBlastDoorService"
+ "com.apple.gputoolsserviced"
+ "hasSuffix:"
+ "processName"
+ "sysctl.proc_translated"
```
