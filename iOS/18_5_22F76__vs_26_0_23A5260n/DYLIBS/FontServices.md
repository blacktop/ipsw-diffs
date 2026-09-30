## FontServices

> `/System/Library/PrivateFrameworks/FontServices.framework/FontServices`

```diff

-137.4.0.1.0
-  __TEXT.__text: 0xaec8
-  __TEXT.__auth_stubs: 0x700
-  __TEXT.__objc_methlist: 0xde4
-  __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x187b
-  __TEXT.__gcc_except_tab: 0x3cc
-  __TEXT.__dlopen_cstrs: 0xf0
+150.0.0.0.0
+  __TEXT.__text: 0xa6b8
+  __TEXT.__auth_stubs: 0x6c0
+  __TEXT.__delay_helper: 0x1fc
+  __TEXT.__objc_methlist: 0xdfc
+  __TEXT.__const: 0x60
+  __TEXT.__cstring: 0x18a7
+  __TEXT.__gcc_except_tab: 0x38c
   __TEXT.__oslogstring: 0x3
-  __TEXT.__unwind_info: 0x590
-  __TEXT.__objc_classname: 0x321
-  __TEXT.__objc_methname: 0x1e22
+  __TEXT.__unwind_info: 0x548
+  __TEXT.__objc_classname: 0x320
+  __TEXT.__objc_methname: 0x1e56
   __TEXT.__objc_methtype: 0xa5f
   __TEXT.__objc_stubs: 0x1560
-  __DATA_CONST.__got: 0x178
-  __DATA_CONST.__const: 0x638
+  __DATA_CONST.__got: 0x180
+  __DATA_CONST.__const: 0x5a8
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x880
+  __DATA_CONST.__objc_selrefs: 0x890
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x38
-  __AUTH_CONST.__auth_got: 0x398
-  __AUTH_CONST.__const: 0x860
-  __AUTH_CONST.__cfstring: 0xb80
-  __AUTH_CONST.__objc_const: 0x1ad8
+  __AUTH_CONST.__auth_got: 0x378
+  __AUTH_CONST.__const: 0x840
+  __AUTH_CONST.__cfstring: 0xba0
+  __AUTH_CONST.__objc_const: 0x10d8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x2d0
   __DATA.__objc_ivar: 0x5c
-  __DATA.__data: 0x670
-  __DATA.__bss: 0xc0
+  __DATA.__data: 0x678
+  __DATA.__bss: 0x80
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__bss: 0x40

   - /System/Library/Frameworks/CoreText.framework/CoreText
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
-  - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/FontServices.framework/libGSFont.dylib
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
-  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B66C5B1D-58CE-33F9-B514-B750F9E276C3
-  Functions: 349
-  Symbols:   1409
+  UUID: 83F88827-E0A3-39EC-B4A7-AFA0B23BDDEB
+  Functions: 339
+  Symbols:   1349
   CStrings:  692
 
Symbols:
+ +[FSUserFontManager cachedDownloadFamiles]
+ +[FSUserFontManager fontProviderFileDirectoryPath]
+ GCC_except_table36
+ GCC_except_table51
+ GCC_except_table54
+ GCC_except_table57
+ GCC_except_table63
+ GCC_except_table66
+ GCC_except_table74
+ _GSFontGetDownloadFamilyNames
+ _OBJC_CLASS_$_MAAssetQuery
+ ___43-[FontProviderManager registeredFontsInfo:]_block_invoke.50
+ ___block_literal_global.19
+ ___block_literal_global.21
+ ___block_literal_global.25
+ ___block_literal_global.27
+ ___block_literal_global.29
+ ___block_literal_global.306
+ ___block_literal_global.31
+ ___block_literal_global.313
+ ___block_literal_global.319
+ ___block_literal_global.33
+ ___block_literal_global.35
+ ___block_literal_global.369
+ ___block_literal_global.37
+ ___block_literal_global.382
+ ___block_literal_global.46
+ ___block_literal_global.53
+ ___block_literal_global.55
+ ___block_literal_global.57
+ ___block_literal_global.59
+ ___block_literal_global.83
+ ___block_literal_global.88
+ _dlopenHelper$MobileAsset
+ _dlopenHelper$SpringBoardServices
+ _dlopenHelperFlag$MobileAsset
+ _dlopenHelperFlag$SpringBoardServices
+ _gotLoadHelper_x8$_OBJC_CLASS_$_MAAssetQuery
+ _gotLoadHelper_x8$_OBJC_CLASS_$_SBSRemoteAlertActivationContext
+ _gotLoadHelper_x8$_OBJC_CLASS_$_SBSRemoteAlertConfigurationContext
+ _gotLoadHelper_x8$_OBJC_CLASS_$_SBSRemoteAlertDefinition
+ _gotLoadHelper_x8$_OBJC_CLASS_$_SBSRemoteAlertHandle
- GCC_except_table35
- GCC_except_table37
- GCC_except_table50
- GCC_except_table52
- GCC_except_table55
- GCC_except_table61
- GCC_except_table64
- GCC_except_table72
- GCC_except_table8
- _GetAssetQueryClass
- _GetAssetQueryClass.cold.1
- _GetAssetQueryClass.maAssetQueryClass
- _GetAssetQueryClass.once
- _UIKitCoreLibraryCore.frameworkLibrary
- ___43-[FontProviderManager registeredFontsInfo:]_block_invoke.47
- ___GetAssetQueryClass_block_invoke
- ___UIKitCoreLibraryCore_block_invoke
- ___block_descriptor_40_e5_v8?0l
- ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
- ___block_literal_global.11
- ___block_literal_global.16
- ___block_literal_global.18
- ___block_literal_global.20
- ___block_literal_global.22
- ___block_literal_global.24
- ___block_literal_global.26
- ___block_literal_global.28
- ___block_literal_global.30
- ___block_literal_global.303
- ___block_literal_global.309
- ___block_literal_global.311
- ___block_literal_global.317
- ___block_literal_global.32
- ___block_literal_global.34
- ___block_literal_global.366
- ___block_literal_global.376
- ___block_literal_global.43
- ___block_literal_global.50
- ___block_literal_global.52
- ___block_literal_global.54
- ___block_literal_global.56
- ___block_literal_global.85
- ___getUIFontClass_block_invoke
- ___getUIFontClass_block_invoke.cold.1
- ___getUIWindowClass_block_invoke
- ___getUIWindowClass_block_invoke.cold.1
- __sl_dlopen
- _abort_report_np
- _audit_stringUIKitCore
- _free
- _getUIFontClass
- _getUIFontClass.softClass
- _getUIWindowClass.softClass
- _objc_getClass
- _objc_retain_x9
CStrings:
+ "/System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices"
+ "cachedDownloadFamiles"
+ "fontProviderFileDirectoryPath"
- "MAAssetQuery"
- "Unable to find class %s"
- "softlink:r:path:/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore"

```
