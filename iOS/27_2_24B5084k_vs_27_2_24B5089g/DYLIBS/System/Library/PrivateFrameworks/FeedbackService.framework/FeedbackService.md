## FeedbackService

> `/System/Library/PrivateFrameworks/FeedbackService.framework/FeedbackService`

```diff

-238.0.0.0.0
-  __TEXT.__text: 0x9189c
-  __TEXT.__objc_methlist: 0x1420
+240.0.0.0.0
+  __TEXT.__text: 0x928a4
+  __TEXT.__objc_methlist: 0x1500
   __TEXT.__const: 0xcb04
-  __TEXT.__oslogstring: 0x1476
-  __TEXT.__cstring: 0x2bd2
+  __TEXT.__oslogstring: 0x1606
+  __TEXT.__cstring: 0x2d92
   __TEXT.__ustring: 0xd8
   __TEXT.__gcc_except_tab: 0xb8
   __TEXT.__swift5_typeref: 0x2af3

   __TEXT.__swift_as_cont: 0x148
   __TEXT.__swift5_assocty: 0x168
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x3348
+  __TEXT.__unwind_info: 0x33b8
   __TEXT.__eh_frame: 0x28f8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x588
-  __DATA_CONST.__objc_classlist: 0x150
+  __DATA_CONST.__const: 0x5c8
+  __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbe8
+  __DATA_CONST.__objc_selrefs: 0xc60
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x70
-  __DATA_CONST.__got: 0x438
-  __AUTH_CONST.__const: 0x61c9
-  __AUTH_CONST.__cfstring: 0xe40
-  __AUTH_CONST.__objc_const: 0x2fe0
+  __DATA_CONST.__objc_superrefs: 0x78
+  __DATA_CONST.__got: 0x440
+  __AUTH_CONST.__const: 0x61f0
+  __AUTH_CONST.__cfstring: 0xfe0
+  __AUTH_CONST.__objc_const: 0x31a0
   __AUTH_CONST.__auth_got: 0xbc8
-  __AUTH.__objc_data: 0x3f0
+  __AUTH.__objc_data: 0x440
   __AUTH.__data: 0x110
-  __DATA.__objc_ivar: 0x120
-  __DATA.__data: 0x12e8
-  __DATA.__common: 0x28
+  __DATA.__objc_ivar: 0x138
+  __DATA.__data: 0x1638
+  __DATA.__common: 0x40
   __DATA_DIRTY.__objc_data: 0x18d0
-  __DATA_DIRTY.__data: 0x1a80
-  __DATA_DIRTY.__common: 0xe8
-  __DATA_DIRTY.__bss: 0xb6c0
+  __DATA_DIRTY.__data: 0x1730
+  __DATA_DIRTY.__bss: 0xb5a0
+  __DATA_DIRTY.__common: 0xd0
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3897
-  Symbols:   2360
-  CStrings:  467
+  Functions: 3928
+  Symbols:   2416
+  CStrings:  487
 
Symbols:
+ +[FBKEnvironmentConfig configForEnvironmentName:]
+ +[FBKEnvironmentConfig internalEnvironmentsByName]
+ +[FBKEnvironmentConfig isInternalInstall]
+ +[FBKEnvironmentConfig productionConfig]
+ +[FBKEnvironmentConfig resolvedConfigForEnvironmentName:]
+ +[FBKEnvironmentConfig resolvedConfigForEnvironmentName:defaults:]
+ +[FBKSSharedConstants overrideEnvironment:]
+ +[FBKSSharedConstants usesCertificatePinning]
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
+ _FBKBoolFromPlistEntry
+ _FBKSCustomCookieNameKey
+ _FBKSCustomDisableCertificatePinningKey
+ _FBKSCustomFilerURLKey
+ _FBKSCustomHostKey
+ _FBKSCustomUsesUATAuthKey
+ _FBKStringFromPlistEntry
+ _FBKValidateBoolField
+ _FBKValidateStringField
+ _OBJC_CLASS_$_FBKEnvironmentConfig
+ _OBJC_IVAR_$_FBKEnvironmentConfig._cookieName
+ _OBJC_IVAR_$_FBKEnvironmentConfig._disableCertificatePinning
+ _OBJC_IVAR_$_FBKEnvironmentConfig._filerURL
+ _OBJC_IVAR_$_FBKEnvironmentConfig._host
+ _OBJC_IVAR_$_FBKEnvironmentConfig._name
+ _OBJC_IVAR_$_FBKEnvironmentConfig._usesUATAuth
+ _OBJC_METACLASS_$_FBKEnvironmentConfig
+ __OBJC_$_CLASS_METHODS_FBKEnvironmentConfig
+ __OBJC_$_INSTANCE_METHODS_FBKEnvironmentConfig
+ __OBJC_$_INSTANCE_VARIABLES_FBKEnvironmentConfig
+ __OBJC_$_PROP_LIST_FBKEnvironmentConfig
+ __OBJC_CLASS_RO_$_FBKEnvironmentConfig
+ __OBJC_METACLASS_RO_$_FBKEnvironmentConfig
+ ___40+[FBKEnvironmentConfig productionConfig]_block_invoke
+ ___50+[FBKEnvironmentConfig internalEnvironmentsByName]_block_invoke
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_e8_32s_e15_v32?0816^B24ls32l8
+ _internalEnvironmentsByName.environments
+ _internalEnvironmentsByName.onceToken
+ _objc_msgSend$configForEnvironmentName:
+ _objc_msgSend$cookieName
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
+ _objc_msgSend$usesCertificatePinning
+ _objc_msgSend$usesUATAuth
+ _productionConfig.config
+ _productionConfig.onceToken
- +[FBKSSharedConstants overrideEnvironment:host:]
- _FBKSDevelopmentHostKey
- _FBKSEnvironmentDemoString
- _FBKSEnvironmentDevelopmentString
- _FBKSEnvironmentProductionString
- _FBKSEnvironmentStagingDevString
- _FBKSEnvironmentStagingString
- __overrideHostString
CStrings:
+ "%{public}s: -> %{public}@"
+ "%{public}s: resolved from defaults -> %{public}@"
+ "+[FBKSSharedConstants environment]"
+ "+[FBKSSharedConstants overrideEnvironment:]"
+ "/AppleInternal/Library/Application Support/com.apple.feedback/environments.plist"
+ "<%@: %@ host=%@ disablePinning=%@ usesUATAuth=%@>"
+ "Running in custom environment; skipping pinning check (internal only)."
+ "cookieName"
+ "custom"
+ "customCookieName"
+ "customDisableCertificatePinning"
+ "customFilerURL"
+ "customHost"
+ "customUsesUATAuth"
+ "disableCertificatePinning"
+ "environments.plist at %{public}@ is missing or not a dictionary"
+ "environments.plist contains a malformed top-level entry (key or value has wrong type); skipping"
+ "environments.plist entry '%{public}@' failed validation; skipping"
+ "environments.plist entry '%{public}@' missing or invalid required bool field '%{public}@'"
+ "environments.plist entry '%{public}@' missing or invalid required string field '%{public}@'"
+ "filerURL"
+ "host"
+ "https://cssubmissions.apple.com/CusSeedSub/submit?version=2"
+ "name=[%@] host=[%@] cookie=[%@] filer=[%@] disablePinning=[%@] usesUATAuth=[%@]"
+ "uat"
+ "usesUATAuth"
+ "v32@?0@8@16^B24"
- "%{public}s: %hd -> [%hd] [%{public}@]"
- "+[FBKSSharedConstants overrideEnvironment:host:]"
- "Running in development/stagingDev mode; skipping pinning check (internal only)."
- "Using non-production server: %{public}@"
- "developmentHost"
- "staging"
- "stagingDev"
```
