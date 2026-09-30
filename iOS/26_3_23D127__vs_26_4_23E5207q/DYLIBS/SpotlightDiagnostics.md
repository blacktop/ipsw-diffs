## SpotlightDiagnostics

> `/System/Library/PrivateFrameworks/SpotlightDiagnostics.framework/SpotlightDiagnostics`

```diff

-2400.22.0.0.0
-  __TEXT.__text: 0x240c
-  __TEXT.__auth_stubs: 0x390
-  __TEXT.__objc_methlist: 0x120
-  __TEXT.__const: 0x68
-  __TEXT.__gcc_except_tab: 0x188
-  __TEXT.__cstring: 0x334
-  __TEXT.__oslogstring: 0xcc
-  __TEXT.__unwind_info: 0x110
+2418.4.8.2.100
+  __TEXT.__text: 0x2b98
+  __TEXT.__auth_stubs: 0x310
+  __TEXT.__objc_methlist: 0x158
+  __TEXT.__const: 0x80
+  __TEXT.__gcc_except_tab: 0x21c
+  __TEXT.__cstring: 0x34d
+  __TEXT.__oslogstring: 0x1dd
+  __TEXT.__unwind_info: 0x140
   __TEXT.__objc_classname: 0x4e
-  __TEXT.__objc_methname: 0x69e
-  __TEXT.__objc_methtype: 0xf1
-  __TEXT.__objc_stubs: 0x680
-  __DATA_CONST.__got: 0xb0
-  __DATA_CONST.__const: 0x140
+  __TEXT.__objc_methname: 0x718
+  __TEXT.__objc_methtype: 0xff
+  __TEXT.__objc_stubs: 0x6c0
+  __DATA_CONST.__got: 0xc0
+  __DATA_CONST.__const: 0x168
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x200
+  __DATA_CONST.__objc_selrefs: 0x220
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x1d8
+  __AUTH_CONST.__auth_got: 0x198
   __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0x3e0
-  __AUTH_CONST.__objc_const: 0x2e0
+  __AUTH_CONST.__cfstring: 0x400
+  __AUTH_CONST.__objc_const: 0x300
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x24
+  __DATA.__objc_ivar: 0x28
   __DATA.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
   - /System/Library/Frameworks/Foundation.framework/Foundation
-  - /System/Library/PrivateFrameworks/MobileSpotlightIndex.framework/MobileSpotlightIndex
+  - /System/Library/PrivateFrameworks/SpotlightIndex.framework/SpotlightIndex
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 704A29A0-D914-3655-B855-7EDCDF9CE753
-  Functions: 61
-  Symbols:   306
-  CStrings:  173
+  UUID: CDE8E07C-4EFF-3F79-A531-699C23609084
+  Functions: 75
+  Symbols:   333
+  CStrings:  188
 
Symbols:
+ +[SDCoreSpotlightDiagnosticClient testClientWithBundleID:protectionClass:]
+ -[SDCoreSpotlightDiagnosticClient dateStringForDaysAgo:]
+ -[SDCoreSpotlightDiagnosticClient findSpotlightIndexDropsForDays:]
+ -[SDCoreSpotlightDiagnosticClient findSpotlightIndexDropsForDays:].cold.1
+ -[SDCoreSpotlightDiagnosticClient getSpotlightHeartbeatData].cold.2
+ -[SDCoreSpotlightDiagnosticClient initWithBundleID:protectionClass:path:private:managed:test:]
+ -[SDCoreSpotlightDiagnosticClient isTestIndex]
+ GCC_except_table14
+ GCC_except_table21
+ GCC_except_table26
+ GCC_except_table28
+ _OBJC_CLASS_$_CSTestSearchQuery
+ _OBJC_CLASS_$_CSTestSearchableIndex
+ _OBJC_IVAR_$_SDCoreSpotlightDiagnosticClient._testIndex
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ ___60-[SDCoreSpotlightDiagnosticClient getSpotlightHeartbeatData]_block_invoke.cold.2
+ ___66-[SDCoreSpotlightDiagnosticClient findSpotlightIndexDropsForDays:]_block_invoke
+ ___66-[SDCoreSpotlightDiagnosticClient findSpotlightIndexDropsForDays:]_block_invoke.cold.1
+ ___78-[SDCoreSpotlightDiagnosticClient copySpotlightIndexDropsToDirectory:forDays:]_block_invoke.cold.1
+ ___block_descriptor_56_e8_32s40s48r_e28_v24?0"NSData"8"NSError"16lr48l8s32l8s40l8
+ _objc_msgSend$dateStringForDaysAgo:
+ _objc_msgSend$initWithBundleID:protectionClass:path:private:managed:test:
+ _objc_msgSend$isTestIndex
- -[SDCoreSpotlightDiagnosticClient initWithBundleID:protectionClass:path:private:managed:]
- GCC_except_table12
- GCC_except_table19
- GCC_except_table23
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$initWithBundleID:protectionClass:path:private:managed:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x25
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x8
CStrings:
+ "@20@0:8I16"
+ "@52@0:8@16@24@32B40B44B48"
+ "_testIndex"
+ "analytics:findreports:%@"
+ "completed copy of %lu index drop reports"
+ "dateStringForDaysAgo:"
+ "error getting heartbeat data for %@: %@"
+ "error trying to copy index drop reports: %@"
+ "error trying to find index drop reports: %@"
+ "findSpotlightIndexDropsForDays:"
+ "found %lu index drop reports"
+ "got heartbeat data for %@"
+ "initWithBundleID:protectionClass:path:private:managed:test:"
+ "isTestIndex"
+ "testClientWithBundleID:protectionClass:"
+ "timed out getting heartbeat data for %@"
+ "timed out searching for index drop reports"
- "@48@0:8@16@24@32B40B44"
- "completed index drop reports copy"
- "initWithBundleID:protectionClass:path:private:managed:"

```
