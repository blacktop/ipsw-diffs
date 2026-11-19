## FeedbackService

> `/System/Library/PrivateFrameworks/FeedbackService.framework/Versions/A/FeedbackService`

```diff

-235.0.0.0.0
-  __TEXT.__text: 0x9a3cc
-  __TEXT.__objc_methlist: 0x1430
-  __TEXT.__const: 0xcb24
-  __TEXT.__oslogstring: 0x1406
-  __TEXT.__cstring: 0x2af2
+242.0.0.0.0
+  __TEXT.__text: 0x9c178
+  __TEXT.__objc_methlist: 0x1518
+  __TEXT.__const: 0xcb44
+  __TEXT.__oslogstring: 0x15b6
+  __TEXT.__cstring: 0x2d12
   __TEXT.__ustring: 0xd8
   __TEXT.__gcc_except_tab: 0xbc
-  __TEXT.__swift5_typeref: 0x2b5b
+  __TEXT.__swift5_typeref: 0x2b75
   __TEXT.__constg_swiftt: 0x25a4
   __TEXT.__swift5_reflstr: 0x1382
   __TEXT.__swift5_fieldmd: 0x2790

   __TEXT.__swift5_mpenum: 0x44
   __TEXT.__swift5_proto: 0xb5c
   __TEXT.__swift5_types: 0x380
-  __TEXT.__swift5_capture: 0x5dc
-  __TEXT.__swift_as_entry: 0x90
-  __TEXT.__swift_as_ret: 0x9c
-  __TEXT.__swift_as_cont: 0x170
+  __TEXT.__swift5_capture: 0x60c
+  __TEXT.__swift_as_entry: 0x94
+  __TEXT.__swift_as_ret: 0xa0
+  __TEXT.__swift_as_cont: 0x17c
   __TEXT.__swift5_assocty: 0x168
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x27c0
-  __TEXT.__eh_frame: 0x2b40
+  __TEXT.__unwind_info: 0x2828
+  __TEXT.__eh_frame: 0x2bf0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3d8
-  __DATA_CONST.__objc_classlist: 0x150
+  __DATA_CONST.__const: 0x400
+  __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbf8
+  __DATA_CONST.__objc_selrefs: 0xc80
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x70
-  __DATA_CONST.__got: 0x450
-  __AUTH_CONST.__const: 0x6389
-  __AUTH_CONST.__cfstring: 0xe20
-  __AUTH_CONST.__objc_const: 0x2fe8
+  __DATA_CONST.__objc_superrefs: 0x78
+  __DATA_CONST.__got: 0x458
+  __AUTH_CONST.__const: 0x6479
+  __AUTH_CONST.__cfstring: 0x1000
+  __AUTH_CONST.__objc_const: 0x31b0
   __AUTH_CONST.__auth_got: 0xaa0
   __AUTH_CONST.__auth_ptr: 0x370
-  __AUTH.__objc_data: 0x3f0
+  __AUTH.__objc_data: 0x440
   __AUTH.__data: 0x110
-  __DATA.__objc_ivar: 0x120
-  __DATA.__data: 0x1340
-  __DATA.__bss: 0xb570
-  __DATA.__common: 0x28
+  __DATA.__objc_ivar: 0x138
+  __DATA.__data: 0x1620
+  __DATA.__bss: 0xb620
+  __DATA.__common: 0x40
   __DATA_DIRTY.__objc_data: 0x18d0
-  __DATA_DIRTY.__data: 0x1aa8
-  __DATA_DIRTY.__common: 0xe8
-  __DATA_DIRTY.__bss: 0xb6c0
+  __DATA_DIRTY.__data: 0x17e0
+  __DATA_DIRTY.__bss: 0xb620
+  __DATA_DIRTY.__common: 0xd0
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3925
-  Symbols:   2342
-  CStrings:  464
+  Functions: 3969
+  Symbols:   2408
+  CStrings:  489
 
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
+ FBKValidateBoolField
+ FBKValidateStringField
+ OBJC_IVAR_$_FBKEnvironmentConfig._cookieName
+ OBJC_IVAR_$_FBKEnvironmentConfig._disableCertificatePinning
+ OBJC_IVAR_$_FBKEnvironmentConfig._filerURL
+ OBJC_IVAR_$_FBKEnvironmentConfig._host
+ OBJC_IVAR_$_FBKEnvironmentConfig._name
+ OBJC_IVAR_$_FBKEnvironmentConfig._usesUATAuth
+ _FBKBoolFromPlistEntry
+ _FBKSCustomCookieNameKey
+ _FBKSCustomDisableCertificatePinningKey
+ _FBKSCustomFilerURLKey
+ _FBKSCustomHostKey
+ _FBKSCustomUsesUATAuthKey
+ _FBKSUltraChoiceEnabledKey
+ _FBKStringFromPlistEntry
+ _FBKValidateBoolField
+ _FBKValidateStringField
+ _OBJC_CLASS_$_FBKEnvironmentConfig
+ _OBJC_CLASS_$_NSUUID
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
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_e8_32s_e15_v32?0816^B24l
+ ___copy_helper_block_e8_32s
+ _objc_msgSend$configForEnvironmentName:
+ _objc_msgSend$cookieName
+ _objc_msgSend$deleteDonationsWithDonationIDs:completion:
+ _objc_msgSend$dictionaryWithContentsOfFile:
+ _objc_msgSend$disableCertificatePinning
+ _objc_msgSend$enumerateKeysAndObjectsUsingBlock:
+ _objc_msgSend$filerURL
+ _objc_msgSend$initWithArray:
+ _objc_msgSend$initWithName:host:disableCertificatePinning:usesUATAuth:cookieName:filerURL:
+ _objc_msgSend$internalEnvironmentsByName
+ _objc_msgSend$isInternalInstall
+ _objc_msgSend$logDescription
+ _objc_msgSend$productionConfig
+ _objc_msgSend$resolvedConfigForEnvironmentName:
+ _objc_msgSend$resolvedConfigForEnvironmentName:defaults:
+ _objc_msgSend$usesCertificatePinning
+ _objc_msgSend$usesUATAuth
+ _symbolic So6NSUUIDCm
+ _symbolic So7NSArrayCm
+ internalEnvironmentsByName.environments
+ internalEnvironmentsByName.onceToken
+ productionConfig.config
+ productionConfig.onceToken
- +[FBKSSharedConstants overrideEnvironment:host:]
- _FBKSDevelopmentHostKey
- _FBKSEnvironmentDemoString
- _FBKSEnvironmentDevelopmentString
- _FBKSEnvironmentProductionString
- _FBKSEnvironmentStagingDevString
- _FBKSEnvironmentStagingString
- __overrideHostString
CStrings:
+ "%{public}s count: %{public}ld"
+ "%{public}s: -> %{public}@"
+ "%{public}s: resolved from defaults -> %{public}@"
+ "+[FBKSSharedConstants environment]"
+ "+[FBKSSharedConstants overrideEnvironment:]"
+ "/AppleInternal/Library/Application Support/com.apple.feedback/environments.plist"
+ "<%@: %@ host=%@ disablePinning=%@ usesUATAuth=%@>"
+ "Running in custom environment; skipping pinning check (internal only)."
+ "UltraChoiceEnabled"
+ "cookieName"
+ "custom"
+ "customCookieName"
+ "customDisableCertificatePinning"
+ "customFilerURL"
+ "customHost"
+ "customUsesUATAuth"
+ "delete(donationIDs:)"
+ "delete(donationIDs:_:)"
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
+ "ultra"
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
