## OSUpdate

> `/System/Library/PrivateFrameworks/OSUpdate.framework/Versions/A/OSUpdate`

```diff

-2412.1.1.0.0
-  __TEXT.__text: 0x906d4
-  __TEXT.__objc_methlist: 0x7b94
+2412.40.11.0.0
+  __TEXT.__text: 0x90708
+  __TEXT.__objc_methlist: 0x7c1c
   __TEXT.__const: 0x201
-  __TEXT.__cstring: 0x8138
-  __TEXT.__oslogstring: 0xdc6b
-  __TEXT.__gcc_except_tab: 0x1b34
+  __TEXT.__cstring: 0x8126
+  __TEXT.__oslogstring: 0xdc55
+  __TEXT.__gcc_except_tab: 0x1b38
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x2b30
+  __TEXT.__unwind_info: 0x2b40
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xd68
-  __DATA_CONST.__objc_classlist: 0x280
+  __DATA_CONST.__const: 0xd60
+  __DATA_CONST.__objc_classlist: 0x290
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4b28
+  __DATA_CONST.__objc_selrefs: 0x4b08
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x1e0
+  __DATA_CONST.__objc_superrefs: 0x1e8
   __DATA_CONST.__objc_arraydata: 0x6f8
-  __DATA_CONST.__got: 0xa58
+  __DATA_CONST.__got: 0xa08
   __AUTH_CONST.__const: 0x2ca0
-  __AUTH_CONST.__cfstring: 0x6140
-  __AUTH_CONST.__objc_const: 0xa098
+  __AUTH_CONST.__cfstring: 0x6100
+  __AUTH_CONST.__objc_const: 0xa268
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_dictobj: 0x190
-  __AUTH_CONST.__auth_got: 0x5e0
-  __AUTH.__objc_data: 0xc80
-  __DATA.__objc_ivar: 0x784
+  __AUTH_CONST.__auth_got: 0x5d0
+  __AUTH.__objc_data: 0xd70
+  __DATA.__objc_ivar: 0x78c
   __DATA.__data: 0x612
-  __DATA_DIRTY.__objc_data: 0xc80
+  __DATA_DIRTY.__objc_data: 0xc30
   __DATA_DIRTY.__bss: 0x80
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbootpolicy.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3349
-  Symbols:   7226
-  CStrings:  2241
+  Functions: 3358
+  Symbols:   7237
+  CStrings:  2238
 
Symbols:
+ +[SUOSUInstallConfig supportsSecureCoding]
+ +[SUOSUScanOptions optionsWithBackground:mdmInitiated:]
+ +[SUOSUScanOptions supportsSecureCoding]
+ -[SUOSUCatalogConfiguration initWithCatalogHostName:configurationType:pallasAudienceID:]
+ -[SUOSUInBoxUpdateConfiguration .cxx_destruct]
+ -[SUOSUInBoxUpdateConfiguration description]
+ -[SUOSUInBoxUpdateConfiguration personalizationServerURL]
+ -[SUOSUInBoxUpdateConfiguration setPersonalizationServerURL:]
+ -[SUOSUInBoxUpdateController initWithDelegate:configuration:]
+ -[SUOSUInBoxUpdateController installConfig]
+ -[SUOSUInBoxUpdateController setInstallConfig:]
+ -[SUOSUInstallConfig .cxx_destruct]
+ -[SUOSUInstallConfig description]
+ -[SUOSUInstallConfig encodeWithCoder:]
+ -[SUOSUInstallConfig initWithCoder:]
+ -[SUOSUInstallConfig personalizationServerURL]
+ -[SUOSUInstallConfig setPersonalizationServerURL:]
+ -[SUOSUMobileSoftwareUpdateController _overridesWithIsBackground:mdmInitiated:installConfig:]
+ -[SUOSUMobileSoftwareUpdateController applyUpdateWithDescriptor:installConfig:withCompletion:]
+ -[SUOSUMobileSoftwareUpdateController commitStashForDescriptor:withOverrides:installConfig:withProgressCompletion:withCompletion:]
+ -[SUOSUMobileSoftwareUpdateController downloadAndPrepareDescriptor:inBackground:mdmInitiated:installConfig:withProgressCompletion:withCompletion:]
+ -[SUOSUScanOptions .cxx_destruct]
+ -[SUOSUScanOptions background]
+ -[SUOSUScanOptions description]
+ -[SUOSUScanOptions disablePSUS]
+ -[SUOSUScanOptions encodeWithCoder:]
+ -[SUOSUScanOptions initWithCoder:]
+ -[SUOSUScanOptions mdmInitiated]
+ -[SUOSUScanOptions requestedProductMarketingVersion]
+ -[SUOSUScanOptions setBackground:]
+ -[SUOSUScanOptions setDisablePSUS:]
+ -[SUOSUScanOptions setMdmInitiated:]
+ -[SUOSUScanOptions setRequestedProductMarketingVersion:]
+ -[SUOSUScanOptions setSplatOnly:]
+ -[SUOSUScanOptions splatOnly]
+ -[SUOSUServiceDaemon _applyMobileSoftwareUpdateDescriptor:overrides:installConfig:completion:]
+ -[SUOSUServiceDaemon applyMobileSoftwareUpdate:installConfig:completion:]
+ -[SUOSUServiceDaemon applyQueuedPostLogoutMobileSoftwareUpdateWithCompletion:]
+ -[SUOSUServiceDaemon commitStashForDescriptor:installConfig:withCompletion:]
+ -[SUOSUServiceDaemon downloadAndPrepareInBoxUpdateWithDescriptor:installConfig:completion:]
+ -[SUOSUServiceDaemon downloadAndPrepareMobileSoftwareUpdateWithDescriptor:inBackground:mdmInitiated:installConfig:completion:]
+ -[SUOSUUpdateController applyMobileSoftwareUpdate:installConfig:completion:]
+ -[SUOSUUpdateController applyQueuedPostLogoutMobileSoftwareUpdate]
+ -[SUOSUUpdateController commitStashWithDescriptor:installConfig:completion:]
+ -[SUOSUUpdateController downloadAndPrepareInBoxUpdateWithDescriptor:installConfig:completion:]
+ GCC_except_table6
+ OBJC_IVAR_$_SUOSUInBoxUpdateConfiguration._personalizationServerURL
+ OBJC_IVAR_$_SUOSUInBoxUpdateController._installConfig
+ OBJC_IVAR_$_SUOSUInstallConfig._personalizationServerURL
+ OBJC_IVAR_$_SUOSUScanOptions._background
+ OBJC_IVAR_$_SUOSUScanOptions._disablePSUS
+ OBJC_IVAR_$_SUOSUScanOptions._mdmInitiated
+ OBJC_IVAR_$_SUOSUScanOptions._requestedProductMarketingVersion
+ OBJC_IVAR_$_SUOSUScanOptions._splatOnly
+ _OBJC_CLASS_$_SUOSUInBoxUpdateConfiguration
+ _OBJC_CLASS_$_SUOSUInstallConfig
+ _OBJC_CLASS_$_SUOSUScanOptions
+ _OBJC_METACLASS_$_SUOSUInBoxUpdateConfiguration
+ _OBJC_METACLASS_$_SUOSUInstallConfig
+ _OBJC_METACLASS_$_SUOSUScanOptions
+ _OUTLINED_FUNCTION_30
+ __126-[SUOSUServiceDaemon downloadAndPrepareMobileSoftwareUpdateWithDescriptor:inBackground:mdmInitiated:installConfig:completion:]_block_invoke
+ __126-[SUOSUServiceDaemon downloadAndPrepareMobileSoftwareUpdateWithDescriptor:inBackground:mdmInitiated:installConfig:completion:]_block_invoke_2
+ __130-[SUOSUMobileSoftwareUpdateController commitStashForDescriptor:withOverrides:installConfig:withProgressCompletion:withCompletion:]_block_invoke
+ __146-[SUOSUMobileSoftwareUpdateController downloadAndPrepareDescriptor:inBackground:mdmInitiated:installConfig:withProgressCompletion:withCompletion:]_block_invoke
+ __76-[SUOSUServiceDaemon commitStashForDescriptor:installConfig:withCompletion:]_block_invoke_2
+ __76-[SUOSUUpdateController applyMobileSoftwareUpdate:installConfig:completion:]_block_invoke
+ __76-[SUOSUUpdateController commitStashWithDescriptor:installConfig:completion:]_block_invoke
+ __78-[SUOSUServiceDaemon applyQueuedPostLogoutMobileSoftwareUpdateWithCompletion:]_block_invoke
+ __91-[SUOSUServiceDaemon downloadAndPrepareInBoxUpdateWithDescriptor:installConfig:completion:]_block_invoke
+ __94-[SUOSUServiceDaemon _applyMobileSoftwareUpdateDescriptor:overrides:installConfig:completion:]_block_invoke
+ __94-[SUOSUUpdateController downloadAndPrepareInBoxUpdateWithDescriptor:installConfig:completion:]_block_invoke
+ __OBJC_$_CLASS_METHODS_SUOSUInstallConfig
+ __OBJC_$_CLASS_METHODS_SUOSUScanOptions
+ __OBJC_$_CLASS_PROP_LIST_SUOSUInstallConfig
+ __OBJC_$_CLASS_PROP_LIST_SUOSUScanOptions
+ __OBJC_$_INSTANCE_METHODS_SUOSUInBoxUpdateConfiguration
+ __OBJC_$_INSTANCE_METHODS_SUOSUInstallConfig
+ __OBJC_$_INSTANCE_METHODS_SUOSUScanOptions
+ __OBJC_$_INSTANCE_VARIABLES_SUOSUInBoxUpdateConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_SUOSUInstallConfig
+ __OBJC_$_INSTANCE_VARIABLES_SUOSUScanOptions
+ __OBJC_$_PROP_LIST_SUOSUInBoxUpdateConfiguration
+ __OBJC_$_PROP_LIST_SUOSUInstallConfig
+ __OBJC_$_PROP_LIST_SUOSUScanOptions
+ __OBJC_CLASS_PROTOCOLS_$_SUOSUInstallConfig
+ __OBJC_CLASS_PROTOCOLS_$_SUOSUScanOptions
+ __OBJC_CLASS_RO_$_SUOSUInBoxUpdateConfiguration
+ __OBJC_CLASS_RO_$_SUOSUInstallConfig
+ __OBJC_CLASS_RO_$_SUOSUScanOptions
+ __OBJC_METACLASS_RO_$_SUOSUInBoxUpdateConfiguration
+ __OBJC_METACLASS_RO_$_SUOSUInstallConfig
+ __OBJC_METACLASS_RO_$_SUOSUScanOptions
+ ___126-[SUOSUServiceDaemon downloadAndPrepareMobileSoftwareUpdateWithDescriptor:inBackground:mdmInitiated:installConfig:completion:]_block_invoke
+ ___126-[SUOSUServiceDaemon downloadAndPrepareMobileSoftwareUpdateWithDescriptor:inBackground:mdmInitiated:installConfig:completion:]_block_invoke_2
+ ___130-[SUOSUMobileSoftwareUpdateController commitStashForDescriptor:withOverrides:installConfig:withProgressCompletion:withCompletion:]_block_invoke
+ ___146-[SUOSUMobileSoftwareUpdateController downloadAndPrepareDescriptor:inBackground:mdmInitiated:installConfig:withProgressCompletion:withCompletion:]_block_invoke
+ ___66-[SUOSUUpdateController applyQueuedPostLogoutMobileSoftwareUpdate]_block_invoke
+ ___73-[SUOSUServiceDaemon applyMobileSoftwareUpdate:installConfig:completion:]_block_invoke
+ ___73-[SUOSUServiceDaemon applyMobileSoftwareUpdate:installConfig:completion:]_block_invoke_2
+ ___76-[SUOSUServiceDaemon commitStashForDescriptor:installConfig:withCompletion:]_block_invoke
+ ___76-[SUOSUServiceDaemon commitStashForDescriptor:installConfig:withCompletion:]_block_invoke_2
+ ___76-[SUOSUUpdateController applyMobileSoftwareUpdate:installConfig:completion:]_block_invoke
+ ___76-[SUOSUUpdateController commitStashWithDescriptor:installConfig:completion:]_block_invoke
+ ___78-[SUOSUServiceDaemon applyQueuedPostLogoutMobileSoftwareUpdateWithCompletion:]_block_invoke
+ ___91-[SUOSUServiceDaemon downloadAndPrepareInBoxUpdateWithDescriptor:installConfig:completion:]_block_invoke
+ ___94-[SUOSUMobileSoftwareUpdateController applyUpdateWithDescriptor:installConfig:withCompletion:]_block_invoke
+ ___94-[SUOSUMobileSoftwareUpdateController applyUpdateWithDescriptor:installConfig:withCompletion:]_block_invoke_2
+ ___94-[SUOSUServiceDaemon _applyMobileSoftwareUpdateDescriptor:overrides:installConfig:completion:]_block_invoke
+ ___94-[SUOSUUpdateController downloadAndPrepareInBoxUpdateWithDescriptor:installConfig:completion:]_block_invoke
+ ___block_descriptor_66_e8_32s40s48s56bs_e5_v8?0l
+ _objc_msgSend$OSName
+ _objc_msgSend$_applyMobileSoftwareUpdateDescriptor:overrides:installConfig:completion:
+ _objc_msgSend$_overridesWithIsBackground:mdmInitiated:installConfig:
+ _objc_msgSend$applyMobileSoftwareUpdate:installConfig:completion:
+ _objc_msgSend$applyQueuedPostLogoutMobileSoftwareUpdate
+ _objc_msgSend$applyQueuedPostLogoutMobileSoftwareUpdateWithCompletion:
+ _objc_msgSend$applyUpdateWithDescriptor:installConfig:withCompletion:
+ _objc_msgSend$commitStashForDescriptor:installConfig:withCompletion:
+ _objc_msgSend$commitStashForDescriptor:withOverrides:installConfig:withProgressCompletion:withCompletion:
+ _objc_msgSend$commitStashWithDescriptor:installConfig:completion:
+ _objc_msgSend$downloadAndPrepareDescriptor:inBackground:mdmInitiated:installConfig:withProgressCompletion:withCompletion:
+ _objc_msgSend$downloadAndPrepareInBoxUpdateWithDescriptor:installConfig:completion:
+ _objc_msgSend$downloadAndPrepareMobileSoftwareUpdateWithDescriptor:inBackground:mdmInitiated:installConfig:completion:
+ _objc_msgSend$initWithCatalogHostName:configurationType:pallasAudienceID:
+ _objc_msgSend$initWithDelegate:configuration:
+ _objc_msgSend$installConfig
+ _objc_setProperty_nonatomic_copy
- +[SUOSUMSUScanOptions optionsWithBackground:mdmInitiated:]
- +[SUOSUMSUScanOptions supportsSecureCoding]
- +[SUOSUUtilities getMDMOrgNameForManagingSU]
- +[SUOSUUtilities preferencesAreManagedWithMDMOrgName:]
- -[SUOSUAuthorizationController _managedPreferenceForKey:domain:]
- -[SUOSUCatalogConfiguration initWithCatalogHostName:managedByOrganizationName:configurationType:pallasAudienceID:]
- -[SUOSUCatalogConfiguration managedByOrganizationName]
- -[SUOSUCatalogConfiguration setManagedByOrganizationName:]
- -[SUOSUMSUScanOptions .cxx_destruct]
- -[SUOSUMSUScanOptions background]
- -[SUOSUMSUScanOptions description]
- -[SUOSUMSUScanOptions disablePSUS]
- -[SUOSUMSUScanOptions encodeWithCoder:]
- -[SUOSUMSUScanOptions initWithCoder:]
- -[SUOSUMSUScanOptions mdmInitiated]
- -[SUOSUMSUScanOptions requestedProductMarketingVersion]
- -[SUOSUMSUScanOptions setBackground:]
- -[SUOSUMSUScanOptions setDisablePSUS:]
- -[SUOSUMSUScanOptions setMdmInitiated:]
- -[SUOSUMSUScanOptions setRequestedProductMarketingVersion:]
- -[SUOSUMSUScanOptions setSplatOnly:]
- -[SUOSUMSUScanOptions splatOnly]
- -[SUOSUMobileSoftwareUpdateController _overridesWithIsBackground:mdmInitiated:]
- -[SUOSUMobileSoftwareUpdateController applyUpdateWithDescriptor:withCompletion:]
- -[SUOSUMobileSoftwareUpdateController commitStashForDescriptor:withOverrides:withProgressCompletion:withCompletion:]
- -[SUOSUMobileSoftwareUpdateController downloadAndPrepareDescriptor:inBackground:mdmInitiated:withProgressCompletion:withCompletion:]
- -[SUOSUServiceDaemon _applyMobileSoftwareUpdateDescriptor:overrides:completion:]
- -[SUOSUServiceDaemon applyMobileSoftwareUpdate:completion:]
- -[SUOSUServiceDaemon applyMobileSoftwareUpdateWithCompletion:]
- -[SUOSUServiceDaemon commitStashForDescriptor:withCompletion:]
- -[SUOSUServiceDaemon downloadAndPrepareInBoxUpdateWithDescriptor:completion:]
- -[SUOSUServiceDaemon downloadAndPrepareMobileSoftwareUpdateWithDescriptor:inBackground:mdmInitiated:completion:]
- -[SUOSUUpdateController applyMobileSoftwareUpdate:completion:]
- -[SUOSUUpdateController applyMobileSoftwareUpdate]
- -[SUOSUUpdateController commitStashWithDescriptor:completion:]
- -[SUOSUUpdateController downloadAndPrepareInBoxUpdateWithDescriptor:completion:]
- GCC_except_table5
- OBJC_IVAR_$_SUOSUCatalogConfiguration._managedByOrganizationName
- OBJC_IVAR_$_SUOSUMSUScanOptions._background
- OBJC_IVAR_$_SUOSUMSUScanOptions._disablePSUS
- OBJC_IVAR_$_SUOSUMSUScanOptions._mdmInitiated
- OBJC_IVAR_$_SUOSUMSUScanOptions._requestedProductMarketingVersion
- OBJC_IVAR_$_SUOSUMSUScanOptions._splatOnly
- _CFPreferencesAppValueIsForced
- _CP_IsEnrolledWithMDMv1
- _CP_MDMOrgInfoManagingDomain
- _OBJC_CLASS_$_SUOSUMSUScanOptions
- _OBJC_METACLASS_$_SUOSUMSUScanOptions
- _OUTLINED_FUNCTION_32
- _SUPrefsDeferredInstallEnabledKey
- _SUPrefsDeferredMajorOSInstallEnabledKey
- _SUPrefsDeferredNonOSInstallEnabledKey
- _SUPrefsDisableSoftwareUpdateNotifications
- _SUPrefsManagedDeferredInstallDelayKey
- _SUPrefsManagedMajorOSDeferredInstallDelayKey
- _SUPrefsManagedMinorOSDeferredInstallDelayKey
- _SUPrefsManagedNonOSDeferredInstallDelayKey
- _SUScanPrefBackgroundDownloadKey
- _SUScanPrefConfigDataInstallKey
- _SUScanPrefMacOSAutoUpdate
- __112-[SUOSUServiceDaemon downloadAndPrepareMobileSoftwareUpdateWithDescriptor:inBackground:mdmInitiated:completion:]_block_invoke
- __112-[SUOSUServiceDaemon downloadAndPrepareMobileSoftwareUpdateWithDescriptor:inBackground:mdmInitiated:completion:]_block_invoke_2
- __116-[SUOSUMobileSoftwareUpdateController commitStashForDescriptor:withOverrides:withProgressCompletion:withCompletion:]_block_invoke
- __132-[SUOSUMobileSoftwareUpdateController downloadAndPrepareDescriptor:inBackground:mdmInitiated:withProgressCompletion:withCompletion:]_block_invoke
- __62-[SUOSUServiceDaemon applyMobileSoftwareUpdateWithCompletion:]_block_invoke
- __62-[SUOSUServiceDaemon commitStashForDescriptor:withCompletion:]_block_invoke_2
- __62-[SUOSUUpdateController applyMobileSoftwareUpdate:completion:]_block_invoke
- __62-[SUOSUUpdateController commitStashWithDescriptor:completion:]_block_invoke
- __77-[SUOSUServiceDaemon downloadAndPrepareInBoxUpdateWithDescriptor:completion:]_block_invoke
- __80-[SUOSUServiceDaemon _applyMobileSoftwareUpdateDescriptor:overrides:completion:]_block_invoke
- __80-[SUOSUUpdateController downloadAndPrepareInBoxUpdateWithDescriptor:completion:]_block_invoke
- __OBJC_$_CLASS_METHODS_SUOSUMSUScanOptions
- __OBJC_$_CLASS_PROP_LIST_SUOSUMSUScanOptions
- __OBJC_$_INSTANCE_METHODS_SUOSUMSUScanOptions
- __OBJC_$_INSTANCE_VARIABLES_SUOSUMSUScanOptions
- __OBJC_$_PROP_LIST_SUOSUMSUScanOptions
- __OBJC_CLASS_PROTOCOLS_$_SUOSUMSUScanOptions
- __OBJC_CLASS_RO_$_SUOSUMSUScanOptions
- __OBJC_METACLASS_RO_$_SUOSUMSUScanOptions
- ___112-[SUOSUServiceDaemon downloadAndPrepareMobileSoftwareUpdateWithDescriptor:inBackground:mdmInitiated:completion:]_block_invoke
- ___112-[SUOSUServiceDaemon downloadAndPrepareMobileSoftwareUpdateWithDescriptor:inBackground:mdmInitiated:completion:]_block_invoke_2
- ___116-[SUOSUMobileSoftwareUpdateController commitStashForDescriptor:withOverrides:withProgressCompletion:withCompletion:]_block_invoke
- ___132-[SUOSUMobileSoftwareUpdateController downloadAndPrepareDescriptor:inBackground:mdmInitiated:withProgressCompletion:withCompletion:]_block_invoke
- ___50-[SUOSUUpdateController applyMobileSoftwareUpdate]_block_invoke
- ___59-[SUOSUServiceDaemon applyMobileSoftwareUpdate:completion:]_block_invoke
- ___59-[SUOSUServiceDaemon applyMobileSoftwareUpdate:completion:]_block_invoke_2
- ___62-[SUOSUServiceDaemon applyMobileSoftwareUpdateWithCompletion:]_block_invoke
- ___62-[SUOSUServiceDaemon commitStashForDescriptor:withCompletion:]_block_invoke
- ___62-[SUOSUServiceDaemon commitStashForDescriptor:withCompletion:]_block_invoke_2
- ___62-[SUOSUUpdateController applyMobileSoftwareUpdate:completion:]_block_invoke
- ___62-[SUOSUUpdateController commitStashWithDescriptor:completion:]_block_invoke
- ___77-[SUOSUServiceDaemon downloadAndPrepareInBoxUpdateWithDescriptor:completion:]_block_invoke
- ___80-[SUOSUMobileSoftwareUpdateController applyUpdateWithDescriptor:withCompletion:]_block_invoke
- ___80-[SUOSUMobileSoftwareUpdateController applyUpdateWithDescriptor:withCompletion:]_block_invoke_2
- ___80-[SUOSUServiceDaemon _applyMobileSoftwareUpdateDescriptor:overrides:completion:]_block_invoke
- ___80-[SUOSUUpdateController downloadAndPrepareInBoxUpdateWithDescriptor:completion:]_block_invoke
- ___block_descriptor_58_e8_32s40s48bs_e5_v8?0l
- _objc_msgSend$_applyMobileSoftwareUpdateDescriptor:overrides:completion:
- _objc_msgSend$_managedPreferenceForKey:domain:
- _objc_msgSend$_overridesWithIsBackground:mdmInitiated:
- _objc_msgSend$adminDeferredMajorOSInstallEnabled
- _objc_msgSend$adminDeferredNonOSInstallEnabled
- _objc_msgSend$adminDeferredOSInstallEnabled
- _objc_msgSend$applyMobileSoftwareUpdate
- _objc_msgSend$applyMobileSoftwareUpdate:completion:
- _objc_msgSend$applyMobileSoftwareUpdateWithCompletion:
- _objc_msgSend$applyUpdateWithDescriptor:withCompletion:
- _objc_msgSend$commitStashForDescriptor:withCompletion:
- _objc_msgSend$commitStashForDescriptor:withOverrides:withProgressCompletion:withCompletion:
- _objc_msgSend$commitStashWithDescriptor:completion:
- _objc_msgSend$downloadAndPrepareDescriptor:inBackground:mdmInitiated:withProgressCompletion:withCompletion:
- _objc_msgSend$downloadAndPrepareInBoxUpdateWithDescriptor:completion:
- _objc_msgSend$downloadAndPrepareMobileSoftwareUpdateWithDescriptor:inBackground:mdmInitiated:completion:
- _objc_msgSend$getMDMOrgNameForManagingSU
- _objc_msgSend$initWithCatalogHostName:managedByOrganizationName:configurationType:pallasAudienceID:
- _objc_msgSend$preferencesAreManagedWithMDMOrgName:
- _objc_msgSend$setManagedByOrganizationName:
CStrings:
+ "%@: Requiring admin authorization prompt for standard user because admin install is required"
+ "-[SUOSUMobileSoftwareUpdateController _overridesWithIsBackground:mdmInitiated:installConfig:]"
+ "-[SUOSUMobileSoftwareUpdateController downloadAndPrepareDescriptor:inBackground:mdmInitiated:installConfig:withProgressCompletion:withCompletion:]_block_invoke"
+ "personalizationServerURL"
+ "personalizationServerURL=%@"
- "%@: Found applicable MDM org name: %@"
- "%@: Requiring admin authorization prompt for standard user because %s is set"
- "-[SUOSUMobileSoftwareUpdateController _overridesWithIsBackground:mdmInitiated:]"
- "-[SUOSUMobileSoftwareUpdateController downloadAndPrepareDescriptor:inBackground:mdmInitiated:withProgressCompletion:withCompletion:]_block_invoke"
- "Managed"
- "OrganizationName"
- "macOS 27 Golden Gate"
- "restrict-software-update-require-admin-to-install"
```
