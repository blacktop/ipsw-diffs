## SoftwareUpdateCoreSupport

> `/System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/Versions/A/SoftwareUpdateCoreSupport`

```diff

-2082.80.5.0.0
-  __TEXT.__text: 0x3a864
+2171.101.1.0.0
+  __TEXT.__text: 0x3aa14
   __TEXT.__auth_stubs: 0x510
-  __TEXT.__objc_methlist: 0x31a4
-  __TEXT.__cstring: 0x7e28
-  __TEXT.__const: 0xc0
-  __TEXT.__gcc_except_tab: 0x580
+  __TEXT.__objc_methlist: 0x3324
+  __TEXT.__cstring: 0x7edf
+  __TEXT.__const: 0xe0
+  __TEXT.__gcc_except_tab: 0x58c
   __TEXT.__oslogstring: 0x51d0
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0xb28
+  __TEXT.__unwind_info: 0xb30
   __TEXT.__objc_classname: 0x256
-  __TEXT.__objc_methname: 0xb270
+  __TEXT.__objc_methname: 0xb2ec
   __TEXT.__objc_methtype: 0xcf8
-  __TEXT.__objc_stubs: 0x72a0
-  __DATA_CONST.__got: 0x2b8
-  __DATA_CONST.__const: 0xaa8
+  __TEXT.__objc_stubs: 0x7300
+  __DATA_CONST.__got: 0x2a0
+  __DATA_CONST.__const: 0xad8
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x22e0
+  __DATA_CONST.__objc_selrefs: 0x23b0
   __DATA_CONST.__objc_superrefs: 0xc0
   __AUTH_CONST.__auth_got: 0x298
   __AUTH_CONST.__const: 0x9e0
-  __AUTH_CONST.__cfstring: 0x7f00
-  __AUTH_CONST.__objc_const: 0x4900
+  __AUTH_CONST.__cfstring: 0x7f60
+  __AUTH_CONST.__objc_const: 0x4668
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0x820
   __DATA.__objc_ivar: 0x434
   __DATA.__data: 0x180
-  __DATA.__bss: 0x108
+  __DATA.__bss: 0xf8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbootpolicy.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F25B693F-3FF9-3E28-91A5-BC0B5DB4F22A
-  Functions: 1266
-  Symbols:   3152
-  CStrings:  4184
+  UUID: 43A11D50-E6FF-3D1E-874A-4A6D461475D1
+  Functions: 1258
+  Symbols:   3163
+  CStrings:  4196
 
Symbols:
+ +[SUCore sharedCore].cold.1
+ +[SUCore stringFromDate:].cold.1
+ +[SUCoreDevice sharedDevice].cold.1
+ +[SUCoreDiag sharedDiag].cold.1
+ +[SUCoreErrorInformation sharedErrorInformation].cold.1
+ +[SUCoreLog sharedLogger].cold.1
+ +[SUCoreRestoreVersion _enableVerboseLogging].cold.1
+ +[SUCoreSimulate sharedSimulator].cold.1
+ +[SUCoreSplunkHistory sharedHistory].cold.1
+ -[SUCoreRestoreVersion getNextNearestRestoreVersionOf:and:]
+ _BIDeviceInfoGetMacPlatformString
+ _OBJC_CLASS_$_NSProcessInfo
+ __59+[SUCoreErrorInformation indicationsForError:matchingMask:]_block_invoke.489
+ __BIDeviceInfoGetMacPlatform
+ ___59-[SUCoreRestoreVersion getNextNearestRestoreVersionOf:and:]_block_invoke
+ ___block_descriptor_32_e55_q24?0"SUCoreRestoreVersion"8"SUCoreRestoreVersion"16l
+ __block_literal_global.45
+ _objc_msgSend$indexOfObjectIdenticalTo:
+ _objc_msgSend$isLowPowerModeEnabled
+ _objc_msgSend$processInfo
+ _objc_msgSend$sortedArrayUsingComparator:
- BIDeviceInfoGetMacPlatform.once
- BIDeviceInfoGetMacPlatform.platform
- _BIDeviceInfoGetMacPlatform
- _OUTLINED_FUNCTION_7
- _OUTLINED_FUNCTION_8
- _OUTLINED_FUNCTION_9
- __59+[SUCoreErrorInformation indicationsForError:matchingMask:]_block_invoke.480
- ___BIDeviceInfoGetMacPlatform_block_invoke
- _objc_msgSend$isSharediPad
CStrings:
+ "getNextNearestRestoreVersionOf:and:"
+ "indexOfObjectIdenticalTo:"
+ "isLowPowerModeEnabled"
+ "kSUCoreErrorSpaceMobileAssetEstimateEvictableFailed"
+ "kSUCoreErrorSpaceMobileAssetResumeFailed"
+ "kSUCoreErrorSpaceMobileAssetSuspendFailed"
+ "lowPowerMode"
+ "other"
+ "processInfo"
+ "q24@?0@\"SUCoreRestoreVersion\"8@\"SUCoreRestoreVersion\"16"
+ "sortedArrayUsingComparator:"
- "sharediPad"
- "virtual_machine"

```
