## FeedbackCore

> `/System/Library/PrivateFrameworks/FeedbackCore.framework/Versions/A/FeedbackCore`

```diff

-235.0.0.0.0
-  __TEXT.__text: 0x10142c
+242.0.0.0.0
+  __TEXT.__text: 0x102aa4
   __TEXT.__lazy_helpers: 0x2a0
-  __TEXT.__objc_methlist: 0x703c
-  __TEXT.__const: 0x1c84
-  __TEXT.__cstring: 0x84de
-  __TEXT.__oslogstring: 0x9332
+  __TEXT.__objc_methlist: 0x7144
+  __TEXT.__const: 0x1c74
+  __TEXT.__cstring: 0x863e
+  __TEXT.__oslogstring: 0x9552
   __TEXT.__gcc_except_tab: 0x121c
   __TEXT.__ustring: 0xdc
   __TEXT.__dlopen_cstrs: 0x62

   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0xc
   __TEXT.__swift_as_cont: 0x24
-  __TEXT.__unwind_info: 0x3590
-  __TEXT.__eh_frame: 0x12c0
+  __TEXT.__unwind_info: 0x35f8
+  __TEXT.__eh_frame: 0x1340
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xff8
-  __DATA_CONST.__objc_classlist: 0x350
+  __DATA_CONST.__const: 0xfd0
+  __DATA_CONST.__objc_classlist: 0x358
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4e58
+  __DATA_CONST.__objc_selrefs: 0x4f08
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__objc_superrefs: 0x1b0
+  __DATA_CONST.__objc_superrefs: 0x1b8
   __DATA_CONST.__objc_arraydata: 0x4c8
-  __DATA_CONST.__got: 0xc38
-  __AUTH_CONST.__const: 0x5fc8
-  __AUTH_CONST.__cfstring: 0x86a0
-  __AUTH_CONST.__objc_const: 0xe3d8
+  __DATA_CONST.__got: 0xc78
+  __AUTH_CONST.__const: 0x6018
+  __AUTH_CONST.__cfstring: 0x8760
+  __AUTH_CONST.__objc_const: 0xe598
   __AUTH_CONST.__lazy_load_got: 0x40
   __AUTH_CONST.__objc_intobj: 0x318
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0x468
-  __AUTH_CONST.__auth_got: 0xed8
+  __AUTH_CONST.__auth_got: 0xee0
   __AUTH_CONST.__auth_ptr: 0x488
-  __AUTH.__objc_data: 0x350
-  __AUTH.__data: 0x210
-  __DATA.__objc_ivar: 0x440
-  __DATA.__data: 0x1624
-  __DATA.__bss: 0x1e08
-  __DATA.__common: 0x108
-  __DATA_DIRTY.__objc_data: 0x2360
-  __DATA_DIRTY.__data: 0x3d8
-  __DATA_DIRTY.__bss: 0x148
-  __DATA_DIRTY.__common: 0x18
+  __AUTH.__objc_data: 0x2700
+  __AUTH.__data: 0x5a8
+  __DATA.__objc_ivar: 0x458
+  __DATA.__data: 0x1664
+  __DATA.__bss: 0x1f68
+  __DATA.__common: 0x120
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/Combine.framework/Versions/A/Combine

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5119
-  Symbols:   7234
-  CStrings:  2236
+  Functions: 5158
+  Symbols:   7301
+  CStrings:  2251
 
Symbols:
+ +[FBKEnvironmentConfig configForEnvironmentName:]
+ +[FBKEnvironmentConfig internalEnvironmentsByName]
+ +[FBKEnvironmentConfig isInternalInstall]
+ +[FBKEnvironmentConfig productionConfig]
+ +[FBKEnvironmentConfig resolvedConfigForEnvironmentName:]
+ +[FBKEnvironmentConfig resolvedConfigForEnvironmentName:defaults:]
+ +[FBKSharedConstants currentConfigLogDescription]
+ +[FBKSharedConstants currentConfig]
+ +[FBKSharedConstants displayTitleForEnvironmentName:]
+ +[FBKSharedConstants seedingCookieName]
+ +[FBKSharedConstants seedingFilerURL]
+ +[FBKSharedConstants usesCertificatePinning]
+ +[FBKSharedConstants usesProductionAuthentication]
+ -[FBKEnvironmentConfig .cxx_destruct]
+ -[FBKEnvironmentConfig cookieName]
+ -[FBKEnvironmentConfig description]
+ -[FBKEnvironmentConfig disableCertificatePinning]
+ -[FBKEnvironmentConfig filerURL]
+ -[FBKEnvironmentConfig host]
+ -[FBKEnvironmentConfig initWithName:host:disableCertificatePinning:usesUATAuth:cookieName:filerURL:]
+ -[FBKEnvironmentConfig logDescription]
+ -[FBKEnvironmentConfig name]
+ -[FBKEnvironmentConfig usesUATAuth]
+ FBKValidateBoolField
+ FBKValidateStringField
+ OBJC_IVAR_$_FBKEnvironmentConfig._cookieName
+ OBJC_IVAR_$_FBKEnvironmentConfig._disableCertificatePinning
+ OBJC_IVAR_$_FBKEnvironmentConfig._filerURL
+ OBJC_IVAR_$_FBKEnvironmentConfig._host
+ OBJC_IVAR_$_FBKEnvironmentConfig._name
+ OBJC_IVAR_$_FBKEnvironmentConfig._usesUATAuth
+ _DEDDevicePlatformHomeAccessory
+ _FBKBoolFromPlistEntry
+ _FBKSCustomCookieNameKey
+ _FBKSCustomDisableCertificatePinningKey
+ _FBKSCustomFilerURLKey
+ _FBKSCustomHostKey
+ _FBKSCustomUsesUATAuthKey
+ _FBKSLog
+ _FBKStringFromPlistEntry
+ _FBKValidateBoolField
+ _FBKValidateStringField
+ _OBJC_CLASS_$_FBKEnvironmentConfig
+ _OBJC_METACLASS_$_FBKEnvironmentConfig
+ __50+[FBKEnvironmentConfig internalEnvironmentsByName]_block_invoke
+ __OBJC_$_CLASS_METHODS_FBKEnvironmentConfig
+ __OBJC_$_INSTANCE_METHODS_FBKEnvironmentConfig
+ __OBJC_$_INSTANCE_VARIABLES_FBKEnvironmentConfig
+ __OBJC_$_PROP_LIST_FBKEnvironmentConfig
+ __OBJC_CLASS_RO_$_FBKEnvironmentConfig
+ __OBJC_METACLASS_RO_$_FBKEnvironmentConfig
+ ___40+[FBKEnvironmentConfig productionConfig]_block_invoke
+ ___50+[FBKEnvironmentConfig internalEnvironmentsByName]_block_invoke
+ ___block_descriptor_40_e8_32s_e15_v32?0816^B24l
+ ___block_descriptor_65_e8_32s40bs_e18_v16?0"NSString"8l
+ _objc_msgSend$configForEnvironmentName:
+ _objc_msgSend$cookieName
+ _objc_msgSend$currentConfig
+ _objc_msgSend$currentConfigLogDescription
+ _objc_msgSend$dictionaryWithContentsOfFile:
+ _objc_msgSend$disableCertificatePinning
+ _objc_msgSend$enumerateKeysAndObjectsUsingBlock:
+ _objc_msgSend$filerURL
+ _objc_msgSend$initWithName:host:disableCertificatePinning:usesUATAuth:cookieName:filerURL:
+ _objc_msgSend$internalEnvironmentsByName
+ _objc_msgSend$isInternalInstall
+ _objc_msgSend$logDescription
+ _objc_msgSend$productionConfig
+ _objc_msgSend$resolvedConfigForEnvironmentName:
+ _objc_msgSend$resolvedConfigForEnvironmentName:defaults:
+ _objc_msgSend$seedingCookieName
+ _objc_msgSend$seedingFilerURL
+ _objc_msgSend$setSeedingCookieName:
+ _objc_msgSend$setSeedingFilerURL:
+ _objc_msgSend$setSeedingUsesPinning:
+ _objc_msgSend$usesCertificatePinning
+ _objc_msgSend$usesProductionAuthentication
+ _objc_msgSend$usesUATAuth
+ internalEnvironmentsByName.environments
+ internalEnvironmentsByName.onceToken
+ productionConfig.config
+ productionConfig.onceToken
- +[FBKDEDHelper _seedingHost]
- +[FBKSharedConstants isProductionEnvironment]
- _FBKDraftingExtensionResourceMemoryLimit
- _FBKSEnvironmentDemoString
- _FBKSEnvironmentDevelopmentString
- _FBKSEnvironmentProductionString
- _FBKSEnvironmentStagingDevString
- _FBKSEnvironmentStagingString
- ___28+[FBKDEDHelper _seedingHost]_block_invoke
- ___block_descriptor_73_e8_32s40bs_e18_v16?0"NSString"8l
- _objc_msgSend$_seedingHost
- _objc_msgSend$hostUrl
- _objc_msgSend$isProductionEnvironment
- _seedingHost._host
- _seedingHost.onceToken
CStrings:
+ "/AppleInternal/Library/Application Support/com.apple.feedback/environments.plist"
+ "<%@: %@ host=%@ disablePinning=%@ usesUATAuth=%@>"
+ "Running in custom environment; skipping pinning check (internal only)."
+ "_seedportal_session"
+ "cookieName"
+ "disableCertificatePinning"
+ "environments.plist at %{public}@ is missing or not a dictionary"
+ "environments.plist contains a malformed top-level entry (key or value has wrong type); skipping"
+ "environments.plist entry '%{public}@' failed validation; skipping"
+ "environments.plist entry '%{public}@' missing or invalid required bool field '%{public}@'"
+ "environments.plist entry '%{public}@' missing or invalid required string field '%{public}@'"
+ "filerURL"
+ "host"
+ "https://cssubmissions.apple.com/CusSeedSub/submit?version=2"
+ "https://fba.apple.com/"
+ "name=[%@] host=[%@] cookie=[%@] filer=[%@] disablePinning=[%@] usesUATAuth=[%@]"
+ "non-production followup submission for FFU [%d]: %{public}@"
+ "non-production login: %{public}@"
+ "non-production submission for form [%d]: %{public}@"
+ "usesUATAuth"
+ "v32@?0@8@16^B24"
- "Running in development/stagingDev mode; skipping pinning check (internal only)."
- "demo"
- "development"
- "sp"
- "staging"
- "stagingDev"
```
