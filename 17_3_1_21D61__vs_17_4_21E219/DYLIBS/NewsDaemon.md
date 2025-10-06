## NewsDaemon

> `/System/Library/PrivateFrameworks/NewsDaemon.framework/NewsDaemon`

```diff

-5325.6.0.0.0
+5345.2.0.0.0
   __TEXT.__text: 0x36d0
   __TEXT.__auth_stubs: 0x330
   __TEXT.__objc_methlist: 0x298

   __TEXT.__dlopen_cstrs: 0x48
   __TEXT.__unwind_info: 0x14c
   __TEXT.__objc_classname: 0xfe
-  __TEXT.__objc_methname: 0x974
+  __TEXT.__objc_methname: 0x986
   __TEXT.__objc_methtype: 0x44e
   __TEXT.__objc_stubs: 0x780
   __DATA_CONST.__got: 0x20

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0xa90
   __DATA_CONST.__objc_selrefs: 0x270
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_classrefs: 0x90
+  __DATA_CONST.__objc_superrefs: 0x18
   __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__cfstring: 0x200
   __AUTH_CONST.__objc_const: 0x1b0
   __AUTH_CONST.__auth_got: 0x1a8
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x90
-  __DATA.__objc_superrefs: 0x18
   __DATA.__objc_ivar: 0x28
   __DATA.__data: 0x360
   __DATA.__bss: 0x28

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CA4F4B1D-1C6A-32D0-8288-2037F02186F3
+  UUID: E57B3C16-43DB-3406-ABAF-43FBDC5088B0
   Functions: 107
   Symbols:   484
-  CStrings:  259
+  CStrings:  260
 
Symbols:
+ ___64-[NDNewsServiceConnection fetchModuleDescriptorsWithCompletion:]_block_invoke.61
+ ___71-[NDNewsServiceConnection fetchLatestResultsWithParameters:completion:]_block_invoke.65
+ ___76-[NDNewsServiceConnection _unsafeEstablishConnectionIfNeededWithCompletion:]_block_invoke.78
+ ___77-[NDNewsServiceConnection markAnalyticsElements:asSeenAtDate:withCompletion:]_block_invoke.68
+ ___block_literal_global.71
+ ___block_literal_global.76
- ___64-[NDNewsServiceConnection fetchModuleDescriptorsWithCompletion:]_block_invoke.60
- ___71-[NDNewsServiceConnection fetchLatestResultsWithParameters:completion:]_block_invoke.64
- ___76-[NDNewsServiceConnection _unsafeEstablishConnectionIfNeededWithCompletion:]_block_invoke.76
- ___77-[NDNewsServiceConnection markAnalyticsElements:asSeenAtDate:withCompletion:]_block_invoke.67
- ___block_literal_global.70
- ___block_literal_global.75
CStrings:
+ "T@\"NSString\",?,R,C"

```
