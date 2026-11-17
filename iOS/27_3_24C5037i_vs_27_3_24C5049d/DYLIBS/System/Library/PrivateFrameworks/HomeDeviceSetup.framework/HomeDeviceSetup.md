## HomeDeviceSetup

> `/System/Library/PrivateFrameworks/HomeDeviceSetup.framework/HomeDeviceSetup`

```diff

-405.20.10.0.0
-  __TEXT.__text: 0x7b744
-  __TEXT.__objc_methlist: 0x3714
+405.20.17.0.0
+  __TEXT.__text: 0x7dc74
+  __TEXT.__objc_methlist: 0x37ac
   __TEXT.__const: 0x728
-  __TEXT.__cstring: 0x1b944
-  __TEXT.__oslogstring: 0x83d
+  __TEXT.__cstring: 0x1c1f4
+  __TEXT.__oslogstring: 0x84d
   __TEXT.__gcc_except_tab: 0x2b8
   __TEXT.__swift5_typeref: 0x1e3
   __TEXT.__swift5_reflstr: 0xbb

   __TEXT.__swift_as_entry: 0x44
   __TEXT.__swift_as_ret: 0x64
   __TEXT.__swift_as_cont: 0x90
-  __TEXT.__unwind_info: 0x2910
+  __TEXT.__unwind_info: 0x29c8
   __TEXT.__eh_frame: 0xac0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1b00
+  __DATA_CONST.__const: 0x1b20
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2f80
+  __DATA_CONST.__objc_selrefs: 0x3080
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_arraydata: 0x230
   __DATA_CONST.__got: 0x4d8
-  __AUTH_CONST.__const: 0xeb8
-  __AUTH_CONST.__cfstring: 0x57e0
-  __AUTH_CONST.__objc_const: 0x7e68
+  __AUTH_CONST.__const: 0xef8
+  __AUTH_CONST.__cfstring: 0x5a40
+  __AUTH_CONST.__objc_const: 0x7ed8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x3c0
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__auth_got: 0xa38
   __AUTH.__objc_data: 0x9f8
-  __AUTH.__data: 0x3a0
-  __DATA.__objc_ivar: 0xaa0
+  __AUTH.__data: 0x3c0
+  __DATA.__objc_ivar: 0xaac
   __DATA.__data: 0xc38
   __DATA.__common: 0x40
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3313
-  Symbols:   3490
-  CStrings:  3221
+  Functions: 3363
+  Symbols:   3521
+  CStrings:  3284
 
Symbols:
+ +[HDSDefaults forceFallbackAssets]
+ -[HDSSetupService _siriClassicLanguageOverrideForRequest:]
+ -[HDSSetupService _siriLanguageCodesForSiriKind:]
+ -[HDSSetupSession _checkPreAuthSiriLanguage:]
+ -[HDSSetupSession _checksSiriLanguageAfterSiriV2]
+ -[HDSSetupSession _defersSiriLanguageToSiriV2]
+ -[HDSSetupSession _preferredNetworkFromCandidates:primaryResidentSSID:]
+ -[HDSSetupSession _runWiFi5GHz]
+ -[HDSSetupSession _siriDisabledFallbackLanguageCode]
+ -[HDSSetupSession _updateSelectedHomeLocationServicesEnabled:]
+ -[HDSSetupSession _userChoseNoSiri]
+ -[HDSSetupSession _wifi5GHzColocatedNetworks]
+ -[HDSSetupSession siriPasscodeLanguageCode]
+ GCC_except_table339
+ GCC_except_table403
+ GCC_except_table408
+ GCC_except_table458
+ _HDSSiriLanguageCodes
+ _OBJC_IVAR_$_HDSSetupSession._homePodWiFi5GHzCapable
+ _OBJC_IVAR_$_HDSSetupSession._offeredSiriLanguageCodes
+ _OBJC_IVAR_$_HDSSetupSession._wifi5GHzState
+ _SODeviceDescriptorFunction
+ _SOHomePodDescriptorFunction
+ _SiriAvailabilityLibrary.sLib
+ _SiriAvailabilityLibrary.sOnce
+ ___31-[HDSSetupSession _runWiFi5GHz]_block_invoke
+ ___31-[HDSSetupSession _runWiFi5GHz]_block_invoke_2
+ ___62-[HDSSetupSession _updateSelectedHomeLocationServicesEnabled:]_block_invoke
+ ___SiriAvailabilityLibrary_block_invoke
+ _classSODeviceDescriptor
+ _classSOHomePodDescriptor
+ _getSODeviceDescriptorClass
+ _getSOHomePodDescriptorClass
+ _initSODeviceDescriptor
+ _initSOHomePodDescriptor
+ _kDefaultsKey_ForceFallbackAssets
- GCC_except_table327
- GCC_except_table391
- GCC_except_table396
- GCC_except_table446
- ___34-[HDSSetupSession locationEnable:]_block_invoke_2
CStrings:
+ "### No selected home to update Location to %s\n"
+ "### WiFi5GHz add failed: %{error}\n"
+ "### WiFi5GHz skipping secured network without password: ssid=%@\n"
+ "-"
+ "-[HDSSetupService _siriClassicLanguageOverrideForRequest:]"
+ "-[HDSSetupService _siriLanguageCodesForSiriKind:]"
+ "-[HDSSetupSession _checkPreAuthSiriLanguage:]"
+ "-[HDSSetupSession _preferredNetworkFromCandidates:primaryResidentSSID:]"
+ "-[HDSSetupSession _runWiFi5GHz]"
+ "-[HDSSetupSession _runWiFi5GHz]_block_invoke_2"
+ "-[HDSSetupSession _updateSelectedHomeLocationServicesEnabled:]"
+ "-[HDSSetupSession _updateSelectedHomeLocationServicesEnabled:]_block_invoke"
+ "-[HDSSetupSession _wifi5GHzColocatedNetworks]"
+ "/System/Library/PrivateFrameworks/SiriAvailability.framework/SiriAvailability"
+ "AI"
+ "Classic"
+ "HomeKit doesn't support them"
+ "HomePod WiFi 5GHz capable: %s | %#m\n"
+ "Preferred network %@ is the phone's network\n"
+ "Preferred network %@ is the primary resident's network\n"
+ "Preferred network falling back to the HomePod's best network\n"
+ "RecognizeVoice check languages skip, user chose not to use Siri\n"
+ "Refetched filtered scan results\n"
+ "SODeviceDescriptor"
+ "SOHomePodDescriptor"
+ "Siri %s languages: %##@\n"
+ "Siri disabled, sending supported language '%@'\n"
+ "Siri language '%@' needs Siri AI, which this HomePod won't run: using en-US\n"
+ "Siri language '%@' not supported by HomePod Siri Classic\n"
+ "Siri language '%@' supported, HomePod lacks Siri voice '%@'\n"
+ "Siri languages offered, HomePod Siri Classic only: %##@\n"
+ "Siri listen language '%@' accepted as Siri Classic '%@'\n"
+ "Siri listen language '%@' not supported by Siri Classic\n"
+ "Siri voice '%@' (%@) not valid on this HomePod for language %@\n"
+ "SiriUnrecognizedUserSettings"
+ "Unrecognized user settings not sent: %s\n"
+ "Unrecognized user settings not sent: Home/SiriUnrecognizedUserSettings is off\n"
+ "Unrecognized user settings: explicit %s, BWK %s, math %s, writing %s, sensitive topics %s, Safari %s, web filter %s\n"
+ "WiFi5GHz"
+ "WiFi5GHz add succeeded\n"
+ "WiFi5GHz add: count=%lu\n"
+ "WiFi5GHz colocated networks: count=%lu\n"
+ "WiFi5GHz skipping enterprise network: ssid=%@\n"
+ "WiFi5GHz skipping with no colocated network\n"
+ "_"
+ "_hds_wifi5g_add"
+ "_runPreflightMisc Location has been enabled (iPhone %s, home %s, prompt handler %s)\n"
+ "_runPreflightMisc skipping Siri with existing HomePod in account\n"
+ "forceFallbackAssets"
+ "hds_sl_cc"
+ "hp_wifi5g_c"
+ "hp_wifi5g_hi"
+ "hp_wifi5g_nn"
+ "hp_wifi5g_ns"
+ "hp_wifi5g_pw"
+ "hp_wifi5g_st"
+ "limit adult websites"
+ "no home"
+ "not set"
+ "unrestricted"
+ "uu_bwk"
+ "uu_ec"
+ "uu_math"
+ "uu_saf"
+ "uu_st"
+ "uu_wcf"
+ "uu_wt"
- "-[HDSSetupSession locationEnable:]_block_invoke_2"
- "Refetched filtered scan results %@\n"
- "Siri voice language '%@' not supported for language %@: %{error}\n"
- "_runPreflightMisc Location has been enabled %s\n"
```
