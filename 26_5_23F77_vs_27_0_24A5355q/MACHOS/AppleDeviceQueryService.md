## AppleDeviceQueryService

> `/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/XPCServices/AppleDeviceQueryService.xpc/AppleDeviceQueryService`

```diff

-408.120.3.0.0
-  __TEXT.__text: 0xc1d4
-  __TEXT.__auth_stubs: 0x850
+458.0.0.0.0
+  __TEXT.__text: 0xc76c
+  __TEXT.__auth_stubs: 0x860
   __TEXT.__objc_stubs: 0x11c0
   __TEXT.__objc_methlist: 0x678
   __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x535f
-  __TEXT.__objc_classname: 0xfc
+  __TEXT.__cstring: 0x54cf
+  __TEXT.__objc_classname: 0xf4
   __TEXT.__objc_methname: 0x1256
   __TEXT.__objc_methtype: 0x3b1
   __TEXT.__oslogstring: 0xb
-  __TEXT.__gcc_except_tab: 0x23c
+  __TEXT.__gcc_except_tab: 0x294
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__unwind_info: 0x2d8
-  __DATA_CONST.__auth_got: 0x438
-  __DATA_CONST.__got: 0x118
-  __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x7a8
-  __DATA_CONST.__cfstring: 0x3640
+  __TEXT.__unwind_info: 0x300
+  __DATA_CONST.__const: 0x7e8
+  __DATA_CONST.__cfstring: 0x3700
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x28

   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0xf0
+  __DATA_CONST.__auth_got: 0x440
+  __DATA_CONST.__got: 0x118
+  __DATA_CONST.__auth_ptr: 0x10
   __DATA.__objc_const: 0xa10
   __DATA.__objc_selrefs: 0x5d0
   __DATA.__objc_ivar: 0x38
   __DATA.__objc_data: 0x230
   __DATA.__data: 0xc00
-  __DATA.__bss: 0x258
+  __DATA.__bss: 0x278
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8B486AB1-9BD4-35EE-87F1-999998CF6E9E
-  Functions: 199
-  Symbols:   225
-  CStrings:  1313
+  UUID: 644A22EB-8924-360D-B2BF-8E9EA3C399EE
+  Functions: 210
+  Symbols:   227
+  CStrings:  1331
 
Symbols:
+ _getZhuGeCryptexPathsWithError
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x4
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x25
- _objc_retain_x26
- _objc_retain_x27
CStrings:
+ "/usr/lib/libcryptex.dylib"
+ "/usr/local/lib/libcryptex.dylib"
+ "Added %s to Cryptex paths array"
+ "Failed to copy cryptex list, error %d(%s)"
+ "Failed to get Cryptex paths"
+ "Failed to link libcryptex.dylib!"
+ "com.apple.FactoryCryptexSupport"
+ "cryptexIdentifier pointer is nil!"
+ "cryptex_copy_list_4MSM"
+ "cryptex_msm_array_destroy"
+ "cryptex_msm_get_string"
+ "getZhuGeCryptexPathsWithError"

```
