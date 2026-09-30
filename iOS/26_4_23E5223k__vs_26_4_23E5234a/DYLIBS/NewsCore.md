## NewsCore

> `/System/Library/PrivateFrameworks/NewsCore.framework/NewsCore`

```diff

-5867.0.0.0.0
-  __TEXT.__text: 0x4321b4
+5871.0.0.0.0
+  __TEXT.__text: 0x432968
   __TEXT.__auth_stubs: 0x3ce0
-  __TEXT.__objc_methlist: 0x34ab4
+  __TEXT.__objc_methlist: 0x34bac
   __TEXT.__const: 0xdfc8
   __TEXT.__swift5_typeref: 0x425a
   __TEXT.__constg_swiftt: 0x324c

   __TEXT.__swift5_protos: 0x68
   __TEXT.__swift_as_entry: 0x310
   __TEXT.__swift_as_ret: 0x398
-  __TEXT.__cstring: 0x55112
+  __TEXT.__cstring: 0x551fd
   __TEXT.__swift5_builtin: 0x168
   __TEXT.__swift5_assocty: 0x3a0
   __TEXT.__swift5_mpenum: 0x54
   __TEXT.__gcc_except_tab: 0x50a4
   __TEXT.__dlopen_cstrs: 0x11c
   __TEXT.__ustring: 0x280
-  __TEXT.__unwind_info: 0x10008
+  __TEXT.__unwind_info: 0x10028
   __TEXT.__eh_frame: 0xa058
-  __TEXT.__objc_classname: 0x8060
-  __TEXT.__objc_methname: 0x89220
-  __TEXT.__objc_methtype: 0xcdd3
-  __TEXT.__objc_stubs: 0x35ce0
-  __DATA_CONST.__got: 0x2bc0
-  __DATA_CONST.__const: 0x11850
-  __DATA_CONST.__objc_classlist: 0x1cc0
+  __TEXT.__objc_classname: 0x807e
+  __TEXT.__objc_methname: 0x89630
+  __TEXT.__objc_methtype: 0xce28
+  __TEXT.__objc_stubs: 0x35d20
+  __DATA_CONST.__got: 0x2bc8
+  __DATA_CONST.__const: 0x11870
+  __DATA_CONST.__objc_classlist: 0x1cc8
   __DATA_CONST.__objc_catlist: 0x298
   __DATA_CONST.__objc_protolist: 0x908
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x148e0
+  __DATA_CONST.__objc_selrefs: 0x14948
   __DATA_CONST.__objc_protorefs: 0x258
-  __DATA_CONST.__objc_superrefs: 0x15b8
+  __DATA_CONST.__objc_superrefs: 0x15c0
   __DATA_CONST.__objc_arraydata: 0x2a80
   __AUTH_CONST.__auth_got: 0x1e88
-  __AUTH_CONST.__const: 0xc300
-  __AUTH_CONST.__cfstring: 0x31980
-  __AUTH_CONST.__objc_const: 0x79130
+  __AUTH_CONST.__const: 0xc320
+  __AUTH_CONST.__cfstring: 0x31aa0
+  __AUTH_CONST.__objc_const: 0x79430
   __AUTH_CONST.__objc_arrayobj: 0x6a8
   __AUTH_CONST.__objc_intobj: 0x13c8
   __AUTH_CONST.__objc_dictobj: 0xc30
   __AUTH_CONST.__objc_doubleobj: 0x120
-  __AUTH.__objc_data: 0x40d0
+  __AUTH.__objc_data: 0x4120
   __AUTH.__data: 0x630
-  __DATA.__objc_ivar: 0x4544
+  __DATA.__objc_ivar: 0x4570
   __DATA.__data: 0x67f0
   __DATA.__bss: 0xdd80
   __DATA.__common: 0x88
-  __DATA_DIRTY.__objc_ivar: 0xf90
+  __DATA_DIRTY.__objc_ivar: 0xf9c
   __DATA_DIRTY.__objc_data: 0xdfc0
   __DATA_DIRTY.__data: 0x2d00
   __DATA_DIRTY.__common: 0x490

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 315C1247-338D-3224-89A2-2B7B4559BE92
-  Functions: 24605
-  Symbols:   65800
-  CStrings:  37663
+  UUID: E5719D65-291E-388A-A8F0-A52074F90E84
+  Functions: 24626
+  Symbols:   65864
+  CStrings:  37714
 
Symbols:
+ +[FCFeedTransformationFilter transformationWithFilterOptions:otherArticleIDs:otherClusterIDs:subscribedTagIDs:mutedTagIDs:ignoredTagIDs:readingHistoryItems:playlistArticleIDs:downloadedArticleIDs:briefingsTagID:paidAccessChecker:bundleSubscription:paywalledArticlesMaxCount:]
+ -[FCDraftFeedDescriptor channelPickerConfiguration]
+ -[FCFeedDescriptor channelPickerConfiguration]
+ -[FCNewsAppConfig tagChannelPickerConfigurations]
+ -[FCPrivateZoneFeedDescriptor channelPickerConfiguration]
+ -[FCSingleTagFeedDescriptor channelPickerConfiguration]
+ -[FCSingleTagFeedDescriptor initWithContext:tag:feedConfiguration:referringFeedItemIdentifier:channelPickerConfiguration:]
+ -[FCSingleTagFeedDescriptor initWithContext:tag:sortMethod:filterOptions:personalizationConfigurationSet:feedConfiguration:referringFeedItemIdentifier:channelPickerConfiguration:]
+ -[FCTagChannelPickerConfiguration .cxx_destruct]
+ -[FCTagChannelPickerConfiguration contextMenuSystemImageName]
+ -[FCTagChannelPickerConfiguration contextMenuTitle]
+ -[FCTagChannelPickerConfiguration initWithConfigDictionary:]
+ -[FCTagChannelPickerConfiguration pickerID]
+ -[FCTagChannelPickerConfiguration setShouldAllowSearch:]
+ -[FCTagChannelPickerConfiguration setShouldFilterFollows:]
+ -[FCTagChannelPickerConfiguration setShouldShowManagement:]
+ -[FCTagChannelPickerConfiguration setShowInContextMenu:]
+ -[FCTagChannelPickerConfiguration shouldAllowSearch]
+ -[FCTagChannelPickerConfiguration shouldFilterFollows]
+ -[FCTagChannelPickerConfiguration shouldShowManagement]
+ -[FCTagChannelPickerConfiguration showInContextMenu]
+ -[FCTagChannelPickerConfiguration suggestionsContextTagIDs]
+ -[FCTagChannelPickerConfiguration tagID]
+ _OBJC_CLASS_$_FCTagChannelPickerConfiguration
+ _OBJC_IVAR_$_FCFeedDescriptor._channelPickerConfiguration
+ _OBJC_IVAR_$_FCFeedTransformationFilter._ignoredTagIDs
+ _OBJC_IVAR_$_FCTagChannelPickerConfiguration._contextMenuSystemImageName
+ _OBJC_IVAR_$_FCTagChannelPickerConfiguration._contextMenuTitle
+ _OBJC_IVAR_$_FCTagChannelPickerConfiguration._pickerID
+ _OBJC_IVAR_$_FCTagChannelPickerConfiguration._shouldAllowSearch
+ _OBJC_IVAR_$_FCTagChannelPickerConfiguration._shouldFilterFollows
+ _OBJC_IVAR_$_FCTagChannelPickerConfiguration._shouldShowManagement
+ _OBJC_IVAR_$_FCTagChannelPickerConfiguration._showInContextMenu
+ _OBJC_IVAR_$_FCTagChannelPickerConfiguration._suggestionsContextTagIDs
+ _OBJC_IVAR_$_FCTagChannelPickerConfiguration._tagID
+ _OBJC_METACLASS_$_FCTagChannelPickerConfiguration
+ __OBJC_$_INSTANCE_METHODS_FCTagChannelPickerConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_FCTagChannelPickerConfiguration
+ __OBJC_$_PROP_LIST_FCTagChannelPickerConfiguration
+ __OBJC_CLASS_RO_$_FCTagChannelPickerConfiguration
+ __OBJC_METACLASS_RO_$_FCTagChannelPickerConfiguration
+ ___49-[FCNewsAppConfig tagChannelPickerConfigurations]_block_invoke
+ ___block_descriptor_32_e55_"FCTagChannelPickerConfiguration"16?0"NSDictionary"8l
+ ___block_literal_global.3268
+ _objc_msgSend$initWithContext:tag:feedConfiguration:referringFeedItemIdentifier:channelPickerConfiguration:
+ _objc_msgSend$initWithContext:tag:sortMethod:filterOptions:personalizationConfigurationSet:feedConfiguration:referringFeedItemIdentifier:channelPickerConfiguration:
+ _objc_msgSend$transformationWithFilterOptions:otherArticleIDs:otherClusterIDs:subscribedTagIDs:mutedTagIDs:ignoredTagIDs:readingHistoryItems:playlistArticleIDs:downloadedArticleIDs:briefingsTagID:paidAccessChecker:bundleSubscription:paywalledArticlesMaxCount:
- -[FCNewsAppConfig channelPickerKeepFollowsForCustomChannelPickerIDs]
- -[FCSingleTagFeedDescriptor initWithContext:tag:sortMethod:filterOptions:personalizationConfigurationSet:feedConfiguration:]
- -[FCSingleTagFeedDescriptor initWithContext:tag:sortMethod:filterOptions:personalizationConfigurationSet:feedConfiguration:referringFeedItemIdentifier:]
- _objc_msgSend$initWithContext:tag:sortMethod:filterOptions:personalizationConfigurationSet:feedConfiguration:referringFeedItemIdentifier:
CStrings:
+ "-[FCSingleTagFeedDescriptor initWithContext:tag:sortMethod:filterOptions:personalizationConfigurationSet:feedConfiguration:referringFeedItemIdentifier:channelPickerConfiguration:]"
+ "@\"FCTagChannelPickerConfiguration\""
+ "@\"FCTagChannelPickerConfiguration\"16@?0@\"NSDictionary\"8"
+ "@120@0:8Q16@24@32@40@48@56@64@72@80@88@96@104Q112"
+ "@56@0:8@16@24Q32@40@48"
+ "@80@0:8@16@24q32Q40q48Q56@64@72"
+ "FCTagChannelPickerConfiguration"
+ "IgnoredChannels"
+ "T@\"FCTagChannelPickerConfiguration\",R,N,V_channelPickerConfiguration"
+ "T@\"NSArray\",R,N,V_suggestionsContextTagIDs"
+ "T@\"NSString\",R,N,V_contextMenuSystemImageName"
+ "T@\"NSString\",R,N,V_contextMenuTitle"
+ "TB,N,V_shouldAllowSearch"
+ "TB,N,V_shouldFilterFollows"
+ "TB,N,V_shouldShowManagement"
+ "TB,N,V_showInContextMenu"
+ "_channelPickerConfiguration"
+ "_contextMenuSystemImageName"
+ "_contextMenuTitle"
+ "_ignoredTagIDs"
+ "_shouldAllowSearch"
+ "_shouldFilterFollows"
+ "_shouldShowManagement"
+ "_showInContextMenu"
+ "_suggestionsContextTagIDs"
+ "channelPickerConfiguration"
+ "contextMenuSystemImageName"
+ "contextMenuTitle"
+ "initWithContext:tag:feedConfiguration:referringFeedItemIdentifier:channelPickerConfiguration:"
+ "initWithContext:tag:sortMethod:filterOptions:personalizationConfigurationSet:feedConfiguration:referringFeedItemIdentifier:channelPickerConfiguration:"
+ "setShouldAllowSearch:"
+ "setShouldFilterFollows:"
+ "setShouldShowManagement:"
+ "setShowInContextMenu:"
+ "shouldAllowSearch"
+ "shouldFilterFollows"
+ "shouldShowManagement"
+ "showInContextMenu"
+ "suggestionsContextTagIDs"
+ "tagChannelPickerConfigurations"
+ "transformationWithFilterOptions:otherArticleIDs:otherClusterIDs:subscribedTagIDs:mutedTagIDs:ignoredTagIDs:readingHistoryItems:playlistArticleIDs:downloadedArticleIDs:briefingsTagID:paidAccessChecker:bundleSubscription:paywalledArticlesMaxCount:"
- "-[FCSingleTagFeedDescriptor initWithContext:tag:sortMethod:filterOptions:personalizationConfigurationSet:feedConfiguration:referringFeedItemIdentifier:]"
- "@64@0:8@16@24q32Q40q48Q56"
- "@72@0:8@16@24q32Q40q48Q56@64"
- "channelPickerKeepFollowsForCustomChannelPickerIDs"
- "initWithContext:tag:sortMethod:filterOptions:personalizationConfigurationSet:feedConfiguration:"
- "initWithContext:tag:sortMethod:filterOptions:personalizationConfigurationSet:feedConfiguration:referringFeedItemIdentifier:"

```
