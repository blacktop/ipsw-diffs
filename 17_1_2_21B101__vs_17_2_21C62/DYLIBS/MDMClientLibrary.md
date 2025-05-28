## MDMClientLibrary

> `/System/Library/PrivateFrameworks/MDMClientLibrary.framework/MDMClientLibrary`

```diff

-3.26.2.3.0
-  __TEXT.__text: 0x14efc
+3.26.3.6.0
+  __TEXT.__text: 0x151ec
   __TEXT.__auth_stubs: 0x650
-  __TEXT.__objc_methlist: 0xf94
+  __TEXT.__objc_methlist: 0xfcc
   __TEXT.__const: 0x81
-  __TEXT.__gcc_except_tab: 0x2c8
-  __TEXT.__cstring: 0x1c37
-  __TEXT.__oslogstring: 0x1c62
+  __TEXT.__gcc_except_tab: 0x2d4
+  __TEXT.__cstring: 0x1c64
+  __TEXT.__oslogstring: 0x1cc5
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x494
+  __TEXT.__unwind_info: 0x4a8
   __TEXT.__objc_classname: 0x295
-  __TEXT.__objc_methname: 0x3bdd
+  __TEXT.__objc_methname: 0x3c89
   __TEXT.__objc_methtype: 0x7e2
-  __TEXT.__objc_stubs: 0x2b40
+  __TEXT.__objc_stubs: 0x2bc0
   __DATA_CONST.__got: 0x178
-  __DATA_CONST.__const: 0xda8
+  __DATA_CONST.__const: 0xdb0
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x2908
-  __DATA_CONST.__objc_selrefs: 0xe10
-  __AUTH_CONST.__cfstring: 0x2b20
+  __DATA_CONST.__objc_selrefs: 0xe38
+  __AUTH_CONST.__cfstring: 0x2b60
   __AUTH_CONST.__objc_const: 0xd8
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__const: 0x80

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 422
-  Symbols:   2081
-  CStrings:  1202
+  Functions: 428
+  Symbols:   2096
+  CStrings:  1210
 
Symbols:
+ +[MDMConfiguration _emptyTokenErrorWithUnderlayingError:]
+ +[MDMManagedMediaReader _metadataByBundleIDExcludeDDMApps:]
+ +[MDMManagedMediaReader attributesByAppIDExcludeDDMApps:]
+ +[MDMManagedMediaReader managedAppIDsExcludeDDMApps:]
+ +[MDMManagedMediaReader managedAppIDsWithFlags:excludeDDMApps:]
+ GCC_except_table11
+ GCC_except_table15
+ GCC_except_table17
+ GCC_except_table19
+ _kMDMManagedAppMetadataSource
+ _objc_msgSend$_emptyTokenErrorWithUnderlayingError:
+ _objc_msgSend$_metadataByBundleIDExcludeDDMApps:
+ _objc_msgSend$attributesByAppIDExcludeDDMApps:
+ _objc_msgSend$managedAppIDsExcludeDDMApps:
+ _objc_msgSend$managedAppIDsWithFlags:excludeDDMApps:
- GCC_except_table16
- GCC_except_table18
- GCC_except_table20
- _objc_msgSend$attributesByAppID
CStrings:
+ "DMC_SERVER_RESPONSE_EMPTY_TOKEN_VALUE"
+ "MDMConfiguration: Failed to covert TokenData to a string. The data might not be properly encoded."
+ "MDMConfiguration: readConfigurationOutError:"
+ "_emptyTokenErrorWithUnderlayingError:"
+ "_metadataByBundleIDExcludeDDMApps:"
+ "attributesByAppIDExcludeDDMApps:"
+ "managedAppIDsExcludeDDMApps:"
+ "managedAppIDsWithFlags:excludeDDMApps:"
+ "source"
- "MDMConfiguration: readConfigrationOutError:"

```
