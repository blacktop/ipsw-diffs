## UserFontManager

> `/System/Library/PrivateFrameworks/FontServices.framework/XPCServices/UserFontManager.xpc/UserFontManager`

```diff

-137.4.0.1.0
-  __TEXT.__text: 0x9058
-  __TEXT.__auth_stubs: 0x480
-  __TEXT.__objc_stubs: 0x11e0
+150.0.0.0.0
+  __TEXT.__text: 0x85dc
+  __TEXT.__auth_stubs: 0x3e0
+  __TEXT.__delay_helper: 0xc8
+  __TEXT.__objc_stubs: 0x10c0
   __TEXT.__objc_methlist: 0x600
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0xb40
+  __TEXT.__cstring: 0xa64
   __TEXT.__objc_classname: 0x8e
-  __TEXT.__objc_methname: 0x12d7
+  __TEXT.__objc_methname: 0x11ec
   __TEXT.__objc_methtype: 0x488
-  __TEXT.__gcc_except_tab: 0x1d4
-  __TEXT.__unwind_info: 0x250
-  __DATA_CONST.__auth_got: 0x250
-  __DATA_CONST.__got: 0x120
-  __DATA_CONST.__const: 0x580
-  __DATA_CONST.__cfstring: 0xba0
+  __TEXT.__gcc_except_tab: 0x1b0
+  __TEXT.__unwind_info: 0x1f8
+  __DATA_CONST.__auth_got: 0x200
+  __DATA_CONST.__got: 0x100
+  __DATA_CONST.__const: 0x438
+  __DATA_CONST.__cfstring: 0xaa0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA.__objc_const: 0x4c0
-  __DATA.__objc_selrefs: 0x640
+  __DATA.__objc_selrefs: 0x5f8
   __DATA.__objc_ivar: 0x10
   __DATA.__objc_data: 0xf0
-  __DATA.__data: 0x120
-  __DATA.__bss: 0x40
+  __DATA.__data: 0x124
+  __DATA.__bss: 0xa
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/FontServices.framework/FontServices
   - /System/Library/PrivateFrameworks/FontServices.framework/libGSFont.dylib
+  - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A466E1AB-4EBF-34BC-B0EF-AF3EDFD40ACE
-  Functions: 146
-  Symbols:   162
-  CStrings:  471
+  UUID: 5C5F56F9-E958-3209-A309-CF54CA5CA58B
+  Functions: 119
+  Symbols:   127
+  CStrings:  442
 
Symbols:
+ _OBJC_CLASS_$_MAAssetQuery
- _APP_SANDBOX_READ
- _FSFontProviderRegisterFonts
- _FSFontProviderRegisteredFontsInfo
- _FSFontProviderRequestFonts
- _FSFontProviderSynchronizeFontAsset
- _FSFontProviderUnregisterFonts
- _FSFontProviderUpdateApplicationInfo
- _FontProviderErrorIdentifierKey
- _GSFontNotificationAddedKey
- _GSFontNotificationFontKindKey
- _GSFontNotificationURLsKey
- _GSFontProcessRegistrationInfoForFontProvider
- _GSFontRequestUserFonts
- _GSFontSetupForUserInstalledFonts
- _GSFontUserFontsAvailable
- _IsApplicationIdentifierGrantedFontEnumeration
- _IsPathConfigurationProfileFontFile
- _IsPathFontAssetFontFile
- _IsPathUserInstalledFontFile
- _NSClassFromString
- _OBJC_CLASS_$_FontProviderManager
- _OBJC_CLASS_$_NSData
- _RegisteredFontAssetFileDirectoryPath
- _SANDBOX_CHECK_NO_REPORT
- _SANDBOX_EXTENSION_DEFAULT
- _SandboxExtensionsForPathsAndAuditToken
- _StartAccessingFontAssets
- _UserInstalledFontFileDirectoryPath
- _UserInstalledFontFileDirectoryURL
- _dispatch_once
- _kFontAssetType
- _kProfileFontsDirPath
- _objc_release_x9
- _sandbox_check_by_audit_token
- _sandbox_extension_issue_file_to_process
- _strlen
CStrings:
- "/"
- "/var/mobile/Library/Fonts/Managed/"
- "/var/mobile/Library/UserFonts/FontFiles/"
- "Identifier"
- "MAAssetQuery"
- "UTF8String"
- "added"
- "dataWithBytesNoCopy:length:freeWhenDone:"
- "file-read-data"
- "kind"
- "queryMetaDataSync"
- "registerFonts:enabled:completionHandler:"
- "registeredFontsInfo:"
- "stringByAppendingString:"
- "synchronizeFontAssets:reply:"
- "unregisterFonts:completionHandler:"
- "updateAppInfo"
- "urls"
- "v16@?0^{__CFDictionary=}8"
- "v20@?0B8@\"NSDictionary\"12"
- "v24@?0@\"NSArray\"8@\"NSDictionary\"16"

```
