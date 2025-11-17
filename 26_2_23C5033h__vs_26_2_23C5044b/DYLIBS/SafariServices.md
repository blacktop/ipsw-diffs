## SafariServices

> `/System/Library/Frameworks/SafariServices.framework/SafariServices`

```diff

-623.1.13.10.3
-  __TEXT.__text: 0x166778
-  __TEXT.__auth_stubs: 0x2760
-  __TEXT.__objc_methlist: 0x1a4dc
+623.1.14.10.6
+  __TEXT.__text: 0x166788
+  __TEXT.__auth_stubs: 0x2740
+  __TEXT.__objc_methlist: 0x1a4fc
   __TEXT.__const: 0x2db4
-  __TEXT.__cstring: 0xc5fe
-  __TEXT.__gcc_except_tab: 0xe15c
+  __TEXT.__cstring: 0xc57e
+  __TEXT.__gcc_except_tab: 0xe158
   __TEXT.__dlopen_cstrs: 0xbd3
-  __TEXT.__oslogstring: 0x7997
+  __TEXT.__oslogstring: 0x79d7
   __TEXT.__ustring: 0x353a
   __TEXT.__swift5_typeref: 0x582
   __TEXT.__swift5_capture: 0x380

   __TEXT.__swift5_reflstr: 0x38
   __TEXT.__swift5_fieldmd: 0x80
   __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0x84f8
+  __TEXT.__unwind_info: 0x84e8
   __TEXT.__eh_frame: 0x8a8
-  __TEXT.__objc_classname: 0x4827
-  __TEXT.__objc_methname: 0x5549a
+  __TEXT.__objc_classname: 0x483e
+  __TEXT.__objc_methname: 0x5553d
   __TEXT.__objc_methtype: 0x1279b
-  __TEXT.__objc_stubs: 0x32d00
+  __TEXT.__objc_stubs: 0x32de0
   __DATA_CONST.__got: 0x23d8
-  __DATA_CONST.__const: 0x7198
+  __DATA_CONST.__const: 0x71e8
   __DATA_CONST.__objc_classlist: 0xa10
   __DATA_CONST.__objc_catlist: 0x100
-  __DATA_CONST.__objc_protolist: 0x888
+  __DATA_CONST.__objc_protolist: 0x878
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x113c8
-  __DATA_CONST.__objc_protorefs: 0x168
-  __DATA_CONST.__objc_superrefs: 0x838
+  __DATA_CONST.__objc_selrefs: 0x113e8
+  __DATA_CONST.__objc_protorefs: 0x158
+  __DATA_CONST.__objc_superrefs: 0x840
   __DATA_CONST.__objc_arraydata: 0x548
-  __AUTH_CONST.__auth_got: 0x13c8
+  __AUTH_CONST.__auth_got: 0x13b8
   __AUTH_CONST.__const: 0x1d70
   __AUTH_CONST.__cfstring: 0xaf40
-  __AUTH_CONST.__objc_const: 0x2a8f0
+  __AUTH_CONST.__objc_const: 0x2a940
   __AUTH_CONST.__objc_intobj: 0x990
   __AUTH_CONST.__objc_arrayobj: 0x4c8
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH.__objc_data: 0x5930
-  __AUTH.__data: 0x220
-  __DATA.__objc_ivar: 0x1db0
-  __DATA.__data: 0x6450
+  __AUTH.__objc_data: 0x5910
+  __AUTH.__data: 0x200
+  __DATA.__objc_ivar: 0x1db8
+  __DATA.__data: 0x6430
   __DATA.__bss: 0x698
   __DATA.__common: 0x60
   __DATA_DIRTY.__objc_data: 0xca8

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C0EBEB27-A2CD-3847-8246-76B226D518A3
-  Functions: 8552
-  Symbols:   32874
-  CStrings:  17381
+  UUID: 53A9CD96-30EC-340B-803A-5682CF039AF2
+  Functions: 8550
+  Symbols:   32902
+  CStrings:  17385
 
Symbols:
+ +[SFSafariExtensionState supportsSecureCoding]
+ +[_SFFeatureAvailability shouldShowChineseOrRussianFeatures]
+ -[SFDefaultBrowserPromptController _isPromptBlockedByManagedConfiguration]
+ -[SFDefaultBrowserPromptController shouldDisplayIconSwapAlert]
+ -[SFDefaultBrowserServiceViewController _setupDismissButton:onLeading:]
+ -[SFDefaultBrowserServiceViewController _updateDefaultBrowserWithRecord:shouldOpenBrowser:]
+ -[SFSafariExtensionState encodeWithCoder:]
+ -[SFSafariExtensionState initWithCoder:]
+ -[SFSafariExtensionState initWithEnabled:]
+ -[SFSafariExtensionState isEnabled]
+ -[SFSafariExtensionState setEnabled:]
+ GCC_except_table232
+ _OBJC_IVAR_$_SFDefaultBrowserListView._didOpenAppFromDetailPage
+ _OBJC_IVAR_$_SFSafariExtensionState._enabled
+ __OBJC_$_CLASS_METHODS_SFSafariExtensionState
+ __OBJC_$_CLASS_PROP_LIST_SFSafariExtensionState
+ __OBJC_$_INSTANCE_METHODS_SFSafariExtensionState
+ __OBJC_$_INSTANCE_VARIABLES_SFSafariExtensionState
+ __OBJC_$_PROP_LIST_SFSafariExtensionState
+ __OBJC_CLASS_PROTOCOLS_$_SFSafariExtensionState
+ __OBJC_CLASS_RO_$_SFSafariExtensionState
+ __OBJC_METACLASS_RO_$_SFSafariExtensionState
+ ___44-[SFFormAutocompleteState _autoFillWithSet:]_block_invoke
+ ___60-[SFFormAutocompleteState newAutoFillablePasskeysAvailable:]_block_invoke.451
+ ___71-[SFDefaultBrowserServiceViewController _setupDismissButton:onLeading:]_block_invoke
+ ___91-[SFDefaultBrowserServiceViewController _updateDefaultBrowserWithRecord:shouldOpenBrowser:]_block_invoke
+ ___91-[SFDefaultBrowserServiceViewController _updateDefaultBrowserWithRecord:shouldOpenBrowser:]_block_invoke.156
+ ___91-[SFDefaultBrowserServiceViewController _updateDefaultBrowserWithRecord:shouldOpenBrowser:]_block_invoke.156.cold.1
+ ___91-[SFDefaultBrowserServiceViewController _updateDefaultBrowserWithRecord:shouldOpenBrowser:]_block_invoke.cold.1
+ ___block_descriptor_48_e8_32s40s_e25_v32?0"NSString"8Q16^B24ls32l8s40l8
+ ___block_descriptor_49_e8_32s40s_e20_v20?0B8"NSError"12ls32l8s40l8
+ ___block_literal_global.460
+ _objc_msgSend$_isPromptBlockedByManagedConfiguration
+ _objc_msgSend$_setupDismissButton:onLeading:
+ _objc_msgSend$_shouldShowChineseFeatures
+ _objc_msgSend$_shouldShowRussianFeatures
+ _objc_msgSend$_updateDefaultBrowserWithRecord:shouldOpenBrowser:
+ _objc_msgSend$ageRatingValue
+ _objc_msgSend$ams_activeiCloudAccount
+ _objc_msgSend$fillIdentifiers
+ _objc_msgSend$initWithEnabled:
+ _objc_msgSend$lockupWithTitle:
+ _objc_msgSend$showAutoFillPromptInWebView:title:message:cancelButtonTitle:otherButtonTitles:cancelWhenAppEntersBackground:makeFirstButtonSuggestedAction:headerViewController:promptType:completionHandler:
- -[SFDefaultBrowserServiceViewController _setupDismissButton:]
- -[SFDefaultBrowserServiceViewController _updateDefaultBrowserWithRecord:]
- GCC_except_table190
- __CLASS_METHODS_SFSafariExtensionState
- __CLASS_PROPERTIES_SFSafariExtensionState
- __DATA_SFSafariExtensionState
- __INSTANCE_METHODS_SFSafariExtensionState
- __IVARS_SFSafariExtensionState
- __METACLASS_DATA_SFSafariExtensionState
- __PROPERTIES_SFSafariExtensionState
- __PROTOCOLS_SFSafariExtensionState
- __PROTOCOLS_SFSafariExtensionState.2
- ___60-[SFFormAutocompleteState newAutoFillablePasskeysAvailable:]_block_invoke.450
- ___61-[SFDefaultBrowserServiceViewController _setupDismissButton:]_block_invoke
- ___73-[SFDefaultBrowserServiceViewController _updateDefaultBrowserWithRecord:]_block_invoke
- ___73-[SFDefaultBrowserServiceViewController _updateDefaultBrowserWithRecord:]_block_invoke.153
- ___73-[SFDefaultBrowserServiceViewController _updateDefaultBrowserWithRecord:]_block_invoke.153.cold.1
- ___73-[SFDefaultBrowserServiceViewController _updateDefaultBrowserWithRecord:]_block_invoke.cold.1
- ___block_literal_global.459
- _objc_msgSend$_setupDismissButton:
- _objc_msgSend$_updateDefaultBrowserWithRecord:
- _objc_msgSend$lockupWithSubtitle:
- _objc_msgSend$showAutoFillPromptInWebView:title:message:cancelButtonTitle:otherButtonTitles:cancelWhenAppEntersBackground:makeFirstButtonSuggestedAction:headerViewController:completionHandler:
- _swift_deallocPartialClassInstance
- _swift_getObjCClassFromObject
CStrings:
+ "%@ (Current Default)"
+ "Do not present the screen. stored version: %@; current version: %@;"
+ "_didOpenAppFromDetailPage"
+ "_isPromptBlockedByManagedConfiguration"
+ "_setupDismissButton:onLeading:"
+ "_updateDefaultBrowserWithRecord:shouldOpenBrowser:"
+ "ageRatingValue"
+ "ams_activeiCloudAccount"
+ "fillIdentifiers"
+ "initWithEnabled:"
+ "lockupWithTitle:"
+ "shouldDisplayIconSwapAlert"
+ "shouldShowChineseOrRussianFeatures"
+ "showAutoFillPromptInWebView:title:message:cancelButtonTitle:otherButtonTitles:cancelWhenAppEntersBackground:makeFirstButtonSuggestedAction:headerViewController:promptType:completionHandler:"
+ "v32@?0@\"NSString\"8Q16^B24"
- "Current Default"
- "TB,N,VextensionIsEnabled"
- "_setupDismissButton:"
- "_updateDefaultBrowserWithRecord:"
- "bundleRecordForCurrentProcess"
- "extensionIsEnabled"
- "lockupWithSubtitle:"
- "setExtensionIsEnabled:"
- "showAutoFillPromptInWebView:title:message:cancelButtonTitle:otherButtonTitles:cancelWhenAppEntersBackground:makeFirstButtonSuggestedAction:headerViewController:completionHandler:"

```
