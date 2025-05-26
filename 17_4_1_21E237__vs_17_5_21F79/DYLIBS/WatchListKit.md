## WatchListKit

> `/System/Library/PrivateFrameworks/WatchListKit.framework/WatchListKit`

```diff

-800.40.27.0.0
-  __TEXT.__text: 0x5a94c
+800.50.8.0.0
+  __TEXT.__text: 0x5ba1c
   __TEXT.__auth_stubs: 0x820
-  __TEXT.__objc_methlist: 0x5d48
+  __TEXT.__objc_methlist: 0x5da8
   __TEXT.__const: 0x12c
-  __TEXT.__cstring: 0x6cae
-  __TEXT.__oslogstring: 0x4b7c
-  __TEXT.__gcc_except_tab: 0xb74
+  __TEXT.__cstring: 0x6d1f
+  __TEXT.__oslogstring: 0x4d8b
+  __TEXT.__gcc_except_tab: 0xbf8
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x1974
-  __TEXT.__objc_classname: 0x11e9
-  __TEXT.__objc_methname: 0xe308
-  __TEXT.__objc_methtype: 0x1ade
+  __TEXT.__unwind_info: 0x1a30
+  __TEXT.__objc_classname: 0x11fb
+  __TEXT.__objc_methname: 0xe346
+  __TEXT.__objc_methtype: 0x1b01
   __TEXT.__objc_stubs: 0x8c00
   __DATA_CONST.__got: 0x1e0
-  __DATA_CONST.__const: 0x2150
-  __DATA_CONST.__objc_classlist: 0x508
+  __DATA_CONST.__const: 0x2158
+  __DATA_CONST.__objc_classlist: 0x510
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xd6a8
-  __DATA_CONST.__objc_selrefs: 0x3078
+  __DATA_CONST.__objc_const: 0xd728
+  __DATA_CONST.__objc_selrefs: 0x3088
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_classrefs: 0x690
+  __DATA_CONST.__objc_classrefs: 0x698
   __DATA_CONST.__objc_superrefs: 0x470
   __DATA_CONST.__objc_arraydata: 0x198
-  __AUTH_CONST.__cfstring: 0x83a0
+  __AUTH_CONST.__cfstring: 0x8440
   __AUTH_CONST.__objc_intobj: 0x378
-  __AUTH_CONST.__objc_const: 0x4210
-  __AUTH_CONST.__const: 0xd20
+  __AUTH_CONST.__objc_const: 0xd8
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH_CONST.__objc_arrayobj: 0x60
+  __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__auth_got: 0x420
-  __AUTH.__objc_data: 0x1900
-  __DATA.__objc_ivar: 0x984
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0x988
   __DATA.__data: 0x7a0
-  __DATA.__bss: 0x110
-  __DATA_DIRTY.__objc_data: 0x1950
+  __DATA.__bss: 0x120
+  __DATA_DIRTY.__const: 0xcc0
+  __DATA_DIRTY.__objc_const: 0x41c8
+  __DATA_DIRTY.__objc_data: 0x3200
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x3f0
   __DATA_DIRTY.__common: 0x1

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2383
-  Symbols:   8939
-  CStrings:  4507
+  Functions: 2403
+  Symbols:   8994
+  CStrings:  4527
 
Symbols:
+ +[WLKChannelManager defaultChannelManager]
+ -[WLKChannelManager .cxx_destruct]
+ -[WLKChannelManager _invalidationHandler]
+ -[WLKChannelManager connection]
+ -[WLKChannelManager setConnection:]
+ -[WLKChannelManager vppaConsentedBundleIDsWithCompletion:]
+ -[WLKUserSettings initWithTabId:shouldPin:]
+ _OBJC_CLASS_$_WLKChannelManager
+ _OBJC_IVAR_$_WLKChannelManager._connection
+ _OBJC_METACLASS_$_WLKChannelManager
+ _WLKFetchIsSportsFavoritesEnabled
+ _WLKIsSportsFavoritesEnabled
+ _WLKServerConfigurationResponseKeyFeaturesSportsFavorites
+ _WLKSportsFavoritesEnabledOverride
+ __OBJC_$_CLASS_METHODS_WLKChannelManager
+ __OBJC_$_INSTANCE_METHODS_WLKChannelManager
+ __OBJC_$_INSTANCE_VARIABLES_WLKChannelManager
+ __OBJC_$_PROP_LIST_WLKChannelManager
+ __OBJC_CLASS_RO_$_WLKChannelManager
+ __OBJC_METACLASS_RO_$_WLKChannelManager
+ ___31-[WLKChannelManager connection]_block_invoke
+ ___31-[WLKChannelManager connection]_block_invoke.8
+ ___42+[WLKChannelManager defaultChannelManager]_block_invoke
+ ___55+[WLKURLBagUtilities isFullTVAppEnabledWithCompletion:]_block_invoke
+ ___58-[WLKChannelManager vppaConsentedBundleIDsWithCompletion:]_block_invoke
+ ___WLKFetchBaseURLWithCompletion_block_invoke
+ ___WLKFetchIsSportsFavoritesEnabled_block_invoke
+ ___WLKFetchIsSportsFavoritesEnabled_block_invoke.cold.1
+ ___WLKFetchNowPlayingEnabledReturningError_block_invoke
+ ___WLKIsSportsFavoritesEnabled_block_invoke
+ ___block_literal_global.113
+ ___block_literal_global.122
+ ___block_literal_global.46
+ ___block_literal_global.51
+ _defaultChannelManager.defaultChannelManager
+ _defaultChannelManager.token
+ _objc_msgSend$vppaConsentedBundleIDsWithCompletion:
- -[WLKSettingsAMSBagTracker _amsBagBoolValueForKey:]
- ___block_literal_global.111
- ___block_literal_global.120
- ___block_literal_global.40
- _objc_msgSend$_amsBagBoolValueForKey:
CStrings:
+ "Fetch full tv app enabled: %@"
+ "Fetch now playing enabled: %@"
+ "WLKChannelManager"
+ "WLKChannelManager - Connection interrupted."
+ "WLKChannelManager - Connection invalidated."
+ "WLKChannelManager - Error: Unable to communicate with the remote object proxy (%@)"
+ "WLKFeatureEnablerHelperDomain"
+ "WLKFeatureEnablerHelpers - Sports favorites enabled *override*: %d"
+ "WLKFeatureEnablerHelpers - Timed out getting the config."
+ "WLKSettingsAMSBagTracker - Update now playing enabled: %d"
+ "WLKSettingsAMSBagTracker - Update tracked bag values did change"
+ "WLKSettingsAMSBagTracker - updateTrackedBagValues"
+ "WLKSportsFavoritesEnabledOverride"
+ "catch_up_to_live"
+ "defaultChannelManager"
+ "denali"
+ "initWithTabId:shouldPin:"
+ "isPinned"
+ "sportsFavorites"
+ "v24@0:8@?<v@?@\"NSSet\"@\"NSError\">16"
+ "vppaConsentedBundleIDsWithCompletion:"
- "_amsBagBoolValueForKey:"

```
