## InstalledContentLibrary

> `/System/Library/PrivateFrameworks/InstalledContentLibrary.framework/InstalledContentLibrary`

```diff

-1513.80.6.0.0
-  __TEXT.__text: 0xb5f40
-  __TEXT.__auth_stubs: 0x17c0
-  __TEXT.__objc_methlist: 0x5474
-  __TEXT.__const: 0xf830
-  __TEXT.__cstring: 0x17d8d
-  __TEXT.__gcc_except_tab: 0xbf8
+1513.100.80.0.0
+  __TEXT.__text: 0xcee18
+  __TEXT.__auth_stubs: 0x1770
+  __TEXT.__objc_methlist: 0x5494
+  __TEXT.__const: 0xf910
+  __TEXT.__cstring: 0x17ce4
+  __TEXT.__gcc_except_tab: 0xc08
   __TEXT.__oslogstring: 0x8eb
   __TEXT.__dlopen_cstrs: 0x111
   __TEXT.__swift5_typeref: 0x30
-  __TEXT.__unwind_info: 0x1770
-  __TEXT.__eh_frame: 0x400
-  __TEXT.__objc_classname: 0x619
-  __TEXT.__objc_methname: 0xeec6
-  __TEXT.__objc_methtype: 0x1e75
-  __TEXT.__objc_stubs: 0x8c20
+  __TEXT.__unwind_info: 0x18d8
+  __TEXT.__eh_frame: 0x380
+  __TEXT.__objc_classname: 0x6ce
+  __TEXT.__objc_methname: 0xf155
+  __TEXT.__objc_methtype: 0x1ed2
+  __TEXT.__objc_stubs: 0x8ea0
   __DATA_CONST.__got: 0x4b8
   __DATA_CONST.__const: 0xed8
   __DATA_CONST.__objc_classlist: 0x208
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2da0
+  __DATA_CONST.__objc_selrefs: 0x2db8
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x170
   __DATA_CONST.__objc_arraydata: 0xb20
-  __AUTH_CONST.__auth_got: 0xbf0
-  __AUTH_CONST.__const: 0x5688
-  __AUTH_CONST.__cfstring: 0xcf00
-  __AUTH_CONST.__objc_const: 0x9c28
+  __AUTH_CONST.__auth_got: 0xbc8
+  __AUTH_CONST.__const: 0x5ba8
+  __AUTH_CONST.__cfstring: 0xcfa0
+  __AUTH_CONST.__objc_const: 0x9c38
   __AUTH_CONST.__objc_dictobj: 0x1270
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH.__objc_data: 0x370
-  __AUTH.__data: 0xd0
+  __AUTH.__data: 0xa0
   __DATA.__objc_ivar: 0x584
-  __DATA.__data: 0x9f0
-  __DATA.__bss: 0x138
-  __DATA.__common: 0xa20
+  __DATA.__data: 0xc60
+  __DATA.__bss: 0x148
+  __DATA.__common: 0xaa8
   __DATA_DIRTY.__objc_data: 0x1180
-  __DATA_DIRTY.__data: 0x70
-  __DATA_DIRTY.__bss: 0x198
+  __DATA_DIRTY.__data: 0x98
+  __DATA_DIRTY.__bss: 0x188
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: 2CB93C42-8EBE-361A-93E7-74A27A78AD42
-  Functions: 2229
-  Symbols:   6902
-  CStrings:  6395
+  UUID: F7B58681-2AAA-3C58-AAE2-C3081B1699A0
+  Functions: 2242
+  Symbols:   6961
+  CStrings:  6394
 
Symbols:
+ -[MIGlobalConfiguration installationDenylist]
+ -[MIGlobalConfiguration installationDenylist].cold.1
+ -[MIMCMContainer replaceExistingContainer:error:].cold.1
+ _CFBooleanGetTypeID
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ ___45-[MIGlobalConfiguration installationDenylist]_block_invoke
+ ___block_literal_global.220
+ ___block_literal_global.235
+ _abort
+ _installationDenylist.denylist
+ _installationDenylist.onceToken
+ _mmap
+ _munmap
+ _objc_msgSend$_appBundleURL
+ _objc_msgSend$_targetDirectoryURL
+ _objc_msgSend$appBundleURL
+ _objc_msgSend$initFromPlistDictionary:error:
+ _objc_msgSend$initInternal
+ _objc_msgSend$initWithAppBundleURL:error:
+ _objc_msgSend$initWithAppBundleURLInternal:
+ _objc_msgSend$initWithCoder:
+ _objc_msgSend$initWithDomain:code:userInfo:
+ _objc_msgSend$initWithTargetDirectoryURL:error:
+ _objc_msgSend$initWithTargetDirectoryURLInternal:
+ _objc_msgSend$installationDenylist
+ _objc_msgSend$isEqualToLocationSystemDefinedBase:
+ _objc_msgSend$isEqualWithLocationSystemDefinedCommon:
+ _objc_msgSend$isEqualWithLocationUserDefined:
+ _objc_msgSend$isEqualWithLocationUserDefinedDirectory:
+ _objc_msgSend$plistDictionary
+ _objc_msgSend$plistTypeName
+ _objc_msgSend$targetDirectoryURL
+ _objc_msgSend$validateWithURLonEmbedded:forLocation:error:
+ _objc_msgSend$volumeUUIDForLocation:error:
+ _sched_yield
- +[ICLFeatureFlags twoStageAppInstallEnabled]
- -[MIGlobalConfiguration installationBlacklist]
- -[MIGlobalConfiguration installationBlacklist].cold.1
- ___46-[MIGlobalConfiguration installationBlacklist]_block_invoke
- ___block_literal_global.217
- ___block_literal_global.232
- _installationBlacklist.blacklist
- _installationBlacklist.onceToken
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$installationBlacklist
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x7
- _objc_retain_x9
CStrings:
+ "App %@ is denylisted; returning failure for capabilities match."
+ "Failed to deserialize container data for token %@"
+ "LSUpgradeInstallConsent"
+ "MIMCMContainer's superclass -init returned a nil self"
+ "UIRequiredDeviceCapabilties in Info.plist has a key that is not a string."
+ "UIRequiredDeviceCapabilties requested key '%@' that did not return a boolean value. Only boolean values are supported. Forcing mismatch."
+ "UIRequiredDeviceCapabilties requested value '%@' that is not a boolean for key '%@'. Only boolean values are supported. Forcing mismatch."
+ "container_query_create_from_container() returned NULL for deserialized container object"
+ "fetchListOfAppsRequiringPreInstallConsent:"
+ "installationDenylist"
+ "registerContentsOnRoot:deferUntilNextBoot:completion:"
+ "storeListOfAppsRequiringPreInstallConsent:completion:"
+ "unregisterContentsOnRoot:deferUntilNextBoot:completion:"
+ "v36@0:8@\"NSSet\"16B24@?<v@?@\"NSError\">28"
- "App %@ is blacklisted; returning failure for capabilities match."
- "Failed to serialize container data %@"
- "MI_Two_Stage_App_Install"
- "UIRequiredDeviceCapabilties in Info.plist has a key that is not a string"
- "installationBlacklist"
- "twoStageAppInstallEnabled"

```
