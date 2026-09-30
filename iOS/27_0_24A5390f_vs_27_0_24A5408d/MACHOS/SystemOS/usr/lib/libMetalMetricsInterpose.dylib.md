## libMetalMetricsInterpose.dylib

> `/usr/lib/libMetalMetricsInterpose.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__thread_vars`

```diff

-5.0.22.0.0
-  __TEXT.__text: 0x1409c
-  __TEXT.__auth_stubs: 0x820
+5.0.24.0.0
+  __TEXT.__text: 0x14148
+  __TEXT.__auth_stubs: 0x850
   __TEXT.__objc_stubs: 0xec0
   __TEXT.__objc_methlist: 0xf8
-  __TEXT.__gcc_except_tab: 0x12b8
+  __TEXT.__gcc_except_tab: 0x12a8
   __TEXT.__const: 0x4c8
-  __TEXT.__cstring: 0x5bd
+  __TEXT.__cstring: 0x634
   __TEXT.__objc_methname: 0xd58
   __TEXT.__objc_classname: 0x1e
   __TEXT.__objc_methtype: 0x3b7
   __TEXT.__unwind_info: 0x8c0
-  __DATA_CONST.__const: 0xba8
-  __DATA_CONST.__cfstring: 0x1e0
+  __DATA_CONST.__const: 0xbc8
+  __DATA_CONST.__cfstring: 0x260
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x420
+  __DATA_CONST.__auth_got: 0x438
   __DATA_CONST.__got: 0x110
   __DATA.__objc_const: 0x220
   __DATA.__objc_selrefs: 0x410

   __DATA.__thread_vars: 0xa8
   __DATA.__thread_bss: 0x7
   __DATA.__common: 0x9
-  __DATA.__bss: 0xf0
+  __DATA.__bss: 0xf8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreImage.framework/CoreImage

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 381
-  Symbols:   970
-  CStrings:  216
+  Functions: 386
+  Symbols:   978
+  CStrings:  220
 
Symbols:
+ FPMTLMetricsCanUseIMPTrampolines
+ FPMTLMetricsIsExcluded
+ FPMTLMetricsIsExcluded.isBlastDoor
+ FPMTLMetricsIsExcluded.onceToken
+ FPMTLMetricsIsProcessTranslated.onceToken
+ GCC_except_table23
+ GCC_except_table55
+ GCC_except_table63
+ _CFBundleGetIdentifier
+ _CFBundleGetMainBundle
+ _CFStringCompare
+ _FPMTLMetricsCanUseIMPTrampolines
+ _FPMTLMetricsIsExcluded
+ _OUTLINED_FUNCTION_1
+ ___FPMTLMetricsIsExcluded_block_invoke
+ ___FPMTLMetricsIsProcessTranslated_block_invoke
- FPMTLMetricsInterposeEnableCompilerStats
- GCC_except_table18
- GCC_except_table54
- GCC_except_table56
- GCC_except_table74
- __ZZ40FPMTLMetricsInterposeEnableCompilerStatsE10isAppleGPU
- __ZZ40FPMTLMetricsInterposeEnableCompilerStatsE9onceToken
- ___FPMTLMetricsInterposeEnableCompilerStats_block_invoke
CStrings:
+ "com.apple.InCallService"
+ "com.apple.MessagesAirlockService"
+ "com.apple.MessagesBlastDoorService"
+ "com.apple.gputoolsserviced"
```
