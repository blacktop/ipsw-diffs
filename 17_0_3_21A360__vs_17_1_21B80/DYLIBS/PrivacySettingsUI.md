## PrivacySettingsUI

> `/System/Library/PrivateFrameworks/Settings/PrivacySettingsUI.framework/PrivacySettingsUI`

```diff

-1156.0.0.0.0
-  __TEXT.__text: 0x43ca0
+1160.2.4.0.0
+  __TEXT.__text: 0x44080
   __TEXT.__auth_stubs: 0xbc0
-  __TEXT.__objc_methlist: 0x2d44
-  __TEXT.__const: 0xc0
+  __TEXT.__objc_methlist: 0x2d5c
+  __TEXT.__const: 0xc8
   __TEXT.__gcc_except_tab: 0x898
-  __TEXT.__cstring: 0x5611
-  __TEXT.__dlopen_cstrs: 0x784
-  __TEXT.__oslogstring: 0x1584
+  __TEXT.__cstring: 0x56b1
+  __TEXT.__dlopen_cstrs: 0x7fa
+  __TEXT.__oslogstring: 0x1630
   __TEXT.__objc_const_ax: 0xe8
   __TEXT.__unwind_info: 0xe7c
   __TEXT.__objc_classname: 0x787
-  __TEXT.__objc_methname: 0xa242
+  __TEXT.__objc_methname: 0xa38c
   __TEXT.__objc_methtype: 0xd6e
   __TEXT.__objc_stubs: 0x88a0
   __DATA_CONST.__got: 0x470
-  __DATA_CONST.__const: 0x1038
+  __DATA_CONST.__const: 0x1050
   __DATA_CONST.__objc_classlist: 0x1b8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x4288
-  __DATA_CONST.__objc_selrefs: 0x2738
+  __DATA_CONST.__objc_const: 0x42b8
+  __DATA_CONST.__objc_selrefs: 0x2748
   __DATA_CONST.__objc_arraydata: 0x178
   __AUTH_CONST.__const: 0x4a0
-  __AUTH_CONST.__cfstring: 0x4e80
+  __AUTH_CONST.__cfstring: 0x4f00
   __AUTH_CONST.__objc_const: 0x1430
   __AUTH_CONST.__objc_intobj: 0x2d0
   __AUTH_CONST.__objc_dictobj: 0x50

   __AUTH.__objc_data: 0xb40
   __DATA.__objc_classrefs: 0x4a8
   __DATA.__objc_superrefs: 0x170
-  __DATA.__objc_ivar: 0x360
+  __DATA.__objc_ivar: 0x364
   __DATA.__objc_const_ax: 0x0
   __DATA.__data: 0x3c0
-  __DATA.__bss: 0x278
+  __DATA.__bss: 0x280
   __DATA_DIRTY.__objc_data: 0x5f0
   __DATA_DIRTY.__bss: 0xb8
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1362
-  Symbols:   5250
-  CStrings:  2811
+  Functions: 1364
+  Symbols:   5257
+  CStrings:  2824
 
Symbols:
+ -[PUINetworkController isWaitingForNetworkConfigurationDidChangeInResponseToUserInteractionWithToggle]
+ -[PUINetworkController setIsWaitingForNetworkConfigurationDidChangeInResponseToUserInteractionWithToggle:]
+ _MomentsOnboardingAndSettingsLibraryCore.frameworkLibrary
+ _OBJC_IVAR_$_PUINetworkController._isWaitingForNetworkConfigurationDidChangeInResponseToUserInteractionWithToggle
+ ___40-[PUIAdSupportController viewDidAppear:]_block_invoke.59
+ ___40-[PUIAdSupportController viewDidAppear:]_block_invoke.63
+ ___MomentsOnboardingAndSettingsLibraryCore_block_invoke
+ _audit_stringMomentsOnboardingAndSettings
- -[PUILocationSystemServicesListController _performConsistencyCheckValue:bundles:name:].cold.1
- ___40-[PUIAdSupportController viewDidAppear:]_block_invoke.56
- ___40-[PUIAdSupportController viewDidAppear:]_block_invoke.60
CStrings:
+ "JOURNALING_SUGGESTIONS"
+ "JOURNALING_SUGGESTIONS_GROUP"
+ "MOInternalEnabled"
+ "MOSuggestionSheetSettingsController"
+ "Moments"
+ "Muxed '%{public}@' values were not consistent. Please file a radar with a sysdiagnose to \"Settings - Privacy | iOS\". bundles: %{private}@, authorized: %{private}@, value: %{private}@"
+ "TB,N,V_isWaitingForNetworkConfigurationDidChangeInResponseToUserInteractionWithToggle"
+ "_isWaitingForNetworkConfigurationDidChangeInResponseToUserInteractionWithToggle"
+ "com.apple.graphic-icon.journaling-suggestions"
+ "isWaitingForNetworkConfigurationDidChangeInResponseToUserInteractionWithToggle"
+ "read GEOAddressCorrectionAuthorizationStatus enabled: %@"
+ "set GEOAddressCorrectionAuthorizationStatus: %ld"
+ "setIsWaitingForNetworkConfigurationDidChangeInResponseToUserInteractionWithToggle:"
+ "softlink:r:path:/System/Library/PrivateFrameworks/MomentsOnboardingAndSettings.framework/MomentsOnboardingAndSettings"
- "Muxed '%{public}@' values were not consistent. Please file a radar with a sysdiagnose to \"Settings - Privacy | iOS\"."

```
