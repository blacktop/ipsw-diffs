## CarPlaySupport

> `/System/Library/PrivateFrameworks/CarPlaySupport.framework/CarPlaySupport`

```diff

-515.10.1.0.0
-  __TEXT.__text: 0x1171c4
-  __TEXT.__auth_stubs: 0x11a0
-  __TEXT.__objc_methlist: 0xa354
+515.14.1.0.0
+  __TEXT.__text: 0x11a43c
+  __TEXT.__auth_stubs: 0x11b0
+  __TEXT.__objc_methlist: 0xa3fc
   __TEXT.__const: 0xba4
-  __TEXT.__cstring: 0x1ccd
-  __TEXT.__oslogstring: 0x2ad2
-  __TEXT.__gcc_except_tab: 0x2528
+  __TEXT.__cstring: 0x1d0d
+  __TEXT.__oslogstring: 0x2b85
+  __TEXT.__gcc_except_tab: 0x24e4
   __TEXT.__ustring: 0x4
   __TEXT.__constg_swiftt: 0x448
   __TEXT.__swift5_typeref: 0xd1a

   __TEXT.__swift5_capture: 0x60
   __TEXT.__swift5_proto: 0x1c
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__unwind_info: 0x1c08
+  __TEXT.__unwind_info: 0x1c48
   __TEXT.__objc_classname: 0x17ce
-  __TEXT.__objc_methname: 0x1cdfe
-  __TEXT.__objc_methtype: 0x51e4
-  __TEXT.__objc_stubs: 0x13c00
+  __TEXT.__objc_methname: 0x1d00e
+  __TEXT.__objc_methtype: 0x5244
+  __TEXT.__objc_stubs: 0x13d80
   __DATA_CONST.__got: 0xdb0
-  __DATA_CONST.__const: 0x2be8
+  __DATA_CONST.__const: 0x2cd0
   __DATA_CONST.__objc_classlist: 0x408
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x328
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x64b0
+  __DATA_CONST.__objc_selrefs: 0x6528
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x308
   __DATA_CONST.__objc_arraydata: 0x100
-  __AUTH_CONST.__auth_got: 0x8e0
-  __AUTH_CONST.__const: 0x8b0
+  __AUTH_CONST.__auth_got: 0x8e8
+  __AUTH_CONST.__const: 0x8d0
   __AUTH_CONST.__cfstring: 0x1ba0
-  __AUTH_CONST.__objc_const: 0x1ed38
+  __AUTH_CONST.__objc_const: 0x1ed10
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x2bf0
   __AUTH.__data: 0x270
-  __DATA.__objc_ivar: 0xa30
+  __DATA.__objc_ivar: 0xa2c
   __DATA.__data: 0x28c8
   __DATA.__bss: 0x4f0
   __DATA.__common: 0x40

   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreImage.framework/CoreImage
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
+  - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreText.framework/CoreText
   - /System/Library/Frameworks/EventKit.framework/EventKit

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D1204BD6-BC5D-3138-A054-E4D7EE872713
-  Functions: 3552
-  Symbols:   14371
-  CStrings:  6023
+  UUID: 063816F1-CFE9-36DA-AF7E-087BA10BD5B3
+  Functions: 3573
+  Symbols:   14434
+  CStrings:  6040
 
Symbols:
+ -[CPSListTemplateViewController _clearDetailsHeader]
+ -[CPSListTemplateViewController _configureBackgroundViewsForListHeader:]
+ -[CPSListTemplateViewController _configureConstraintsForDetailsHeader:inContainer:]
+ -[CPSListTemplateViewController _createDetailsButtonsFromListHeader:]
+ -[CPSListTemplateViewController _createDetailsHeaderViewModelForListHeader:]
+ -[CPSListTemplateViewController _createImageOverlayFromListHeader:]
+ -[CPSListTemplateViewController _createNewDetailsHeaderWithViewModel:margins:]
+ -[CPSListTemplateViewController _createSportsOverlayFromListHeader:]
+ -[CPSListTemplateViewController _detailsHeaderFromContainer:]
+ -[CPSListTemplateViewController _tableViewMarginsForDetailsHeader]
+ -[CPSListTemplateViewController _updateExistingDetailsHeader:container:viewModel:margins:]
+ -[CPSTemplateInstance instrumentClusterCardViewControllerForDisplayIdentifier:]
+ -[CPSTemplateInstance instrumentClusterCardViewControllerMapTable]
+ -[CPSTemplateInstance instrumentClusterSceneForDisplayIdentifier:]
+ -[CPSTemplateInstance instrumentClusterSceneMapTable]
+ -[CPSTemplateInstance setInstrumentClusterCardViewControllerMapTable:]
+ -[CPSTemplateInstance setInstrumentClusterScene:forDisplayIdentifier:]
+ -[CPSTemplateInstance setInstrumentClusterSceneMapTable:]
+ GCC_except_table100
+ GCC_except_table107
+ GCC_except_table113
+ GCC_except_table134
+ GCC_except_table136
+ GCC_except_table64
+ GCC_except_table78
+ GCC_except_table97
+ GCC_except_table98
+ GCC_except_table99
+ _CMTimeGetSeconds
+ _OBJC_IVAR_$_CPSTemplateInstance._instrumentClusterCardViewControllerMapTable
+ _OBJC_IVAR_$_CPSTemplateInstance._instrumentClusterSceneMapTable
+ ___42-[CPSTemplateInstance didCreateNavigator:]_block_invoke_3
+ ___46-[CPSTemplateInstance safeAreaInsetsForScene:]_block_invoke
+ ___53-[CPSListTemplateViewController updateDetailsHeader:]_block_invoke.235
+ ___53-[CPSListTemplateViewController updateDetailsHeader:]_block_invoke_3
+ ___62-[CPSTemplateInstance viewController:didUpdateSafeAreaInsets:]_block_invoke.219
+ ___62-[CPSTemplateInstance viewController:didUpdateSafeAreaInsets:]_block_invoke.221
+ ___62-[CPSTemplateInstance viewController:didUpdateSafeAreaInsets:]_block_invoke.222
+ ___62-[CPSTemplateInstance viewController:didUpdateSafeAreaInsets:]_block_invoke_2
+ ___69-[CPSListTemplateViewController _createDetailsButtonsFromListHeader:]_block_invoke
+ ___69-[CPSListTemplateViewController _createDetailsButtonsFromListHeader:]_block_invoke_2
+ ___70-[CPSTemplateInstance _instrumentClusterConnectionInvalidationHandler]_block_invoke_3
+ ___70-[CPSTemplateInstance setInstrumentClusterScene:forDisplayIdentifier:]_block_invoke
+ ___70-[CPSTemplateInstance setInstrumentClusterScene:forDisplayIdentifier:]_block_invoke_2
+ ___77-[CPSTemplateInstance presentVoiceTemplate:withProxyDelegate:animated:reply:]_block_invoke.126
+ ___86-[CPSTemplateInstance templateViewController:requestsPlaybackPresentation:completion:]_block_invoke.216
+ ___90-[CPSTemplateInstance pushMapTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.113
+ ___91-[CPSTemplateInstance pushGridTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.109
+ ___91-[CPSTemplateInstance pushListTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.116
+ ___91-[CPSTemplateInstance pushListTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.118
+ ___93-[CPSTemplateInstance pushEntityTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.133
+ ___93-[CPSTemplateInstance pushSearchTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.122
+ ___97-[CPSTemplateInstance pushNowPlayingTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.119
+ ___98-[CPSTemplateInstance pushInformationTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.111
+ ___99-[CPSTemplateInstance pushVoiceControlTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.127
+ ___block_descriptor_32_e55_v32?0"CPSInstrumentClusterCardViewController"8Q16^B24l
+ ___block_descriptor_40_e8_32s_e37_"CPUIDetailsButton"16?0"CPButton"8ls32l8
+ ___block_descriptor_40_e8_32s_e55_v32?0"CPSInstrumentClusterCardViewController"8Q16^B24ls32l8
+ ___block_descriptor_48_e8_32s40r_e43_v16?0"UIMutableApplicationSceneSettings"8ls32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e55_v32?0"CPSInstrumentClusterCardViewController"8Q16^B24ls32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e43_v16?0"UIMutableApplicationSceneSettings"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40r48r_e55_v32?0"CPSInstrumentClusterCardViewController"8Q16^B24ls32l8r40l8r48l8
+ ___block_descriptor_56_e8_32s40s48r_e55_v32?0"CPSInstrumentClusterCardViewController"8Q16^B24ls32l8s40l8r48l8
+ ___block_literal_global.142
+ ___block_literal_global.146
+ ___block_literal_global.150
+ ___block_literal_global.153
+ _objc_msgSend$_clearDetailsHeader
+ _objc_msgSend$_configureBackgroundViewsForListHeader:
+ _objc_msgSend$_configureConstraintsForDetailsHeader:inContainer:
+ _objc_msgSend$_createDetailsButtonsFromListHeader:
+ _objc_msgSend$_createDetailsHeaderViewModelForListHeader:
+ _objc_msgSend$_createImageOverlayFromListHeader:
+ _objc_msgSend$_createNewDetailsHeaderWithViewModel:margins:
+ _objc_msgSend$_createSportsOverlayFromListHeader:
+ _objc_msgSend$_detailsHeaderFromContainer:
+ _objc_msgSend$_tableViewMarginsForDetailsHeader
+ _objc_msgSend$_updateExistingDetailsHeader:container:viewModel:margins:
+ _objc_msgSend$initWithIdentifier:title:image:type:
+ _objc_msgSend$instrumentClusterCardViewControllerForDisplayIdentifier:
+ _objc_msgSend$instrumentClusterCardViewControllerMapTable
+ _objc_msgSend$instrumentClusterSceneMapTable
+ _objc_msgSend$keyEnumerator
- -[CPSTemplateInstance instrumentClusterCardViewController]
- -[CPSTemplateInstance instrumentClusterMapETAViewController]
- -[CPSTemplateInstance instrumentClusterScene]
- -[CPSTemplateInstance setInstrumentClusterCardViewController:]
- -[CPSTemplateInstance setInstrumentClusterScene:]
- GCC_except_table103
- GCC_except_table110
- GCC_except_table63
- GCC_except_table81
- GCC_except_table83
- GCC_except_table85
- GCC_except_table87
- _OBJC_IVAR_$_CPSTemplateInstance._instrumentClusterCardViewController
- _OBJC_IVAR_$_CPSTemplateInstance._instrumentClusterMapETAViewController
- _OBJC_IVAR_$_CPSTemplateInstance._instrumentClusterScene
- _UIRectGetMinY
- ___49-[CPSTemplateInstance setInstrumentClusterScene:]_block_invoke
- ___49-[CPSTemplateInstance setInstrumentClusterScene:]_block_invoke_2
- ___53-[CPSListTemplateViewController updateDetailsHeader:]_block_invoke.241
- ___62-[CPSTemplateInstance viewController:didUpdateSafeAreaInsets:]_block_invoke.217
- ___62-[CPSTemplateInstance viewController:didUpdateSafeAreaInsets:]_block_invoke.218
- ___77-[CPSTemplateInstance presentVoiceTemplate:withProxyDelegate:animated:reply:]_block_invoke.127
- ___86-[CPSTemplateInstance templateViewController:requestsPlaybackPresentation:completion:]_block_invoke.215
- ___90-[CPSTemplateInstance pushMapTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.114
- ___91-[CPSTemplateInstance pushGridTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.110
- ___91-[CPSTemplateInstance pushListTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.117
- ___91-[CPSTemplateInstance pushListTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.119
- ___93-[CPSTemplateInstance pushEntityTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.134
- ___93-[CPSTemplateInstance pushSearchTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.123
- ___97-[CPSTemplateInstance pushNowPlayingTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.120
- ___98-[CPSTemplateInstance pushInformationTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.112
- ___99-[CPSTemplateInstance pushVoiceControlTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.128
- ___block_descriptor_48_e8_32s40w_e5_v8?0ls32l8w40l8
- ___block_descriptor_56_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
- ___block_literal_global.144
- ___block_literal_global.148
- ___block_literal_global.152
- _objc_msgSend$instrumentClusterCardViewController
- _objc_msgSend$instrumentClusterMapETAViewController
- _objc_msgSend$instrumentClusterScene
- _objc_msgSend$setInstrumentClusterCardViewController:
CStrings:
+ "%@ Undefined layout (0), will not show cluster content."
+ "T@\"NSMapTable\",&,N,V_instrumentClusterCardViewControllerMapTable"
+ "T@\"NSMapTable\",&,N,V_instrumentClusterSceneMapTable"
+ "[Cluster] Creating CPSInstrumentClusterCardViewController for display %@ for %@"
+ "[Cluster] Creating new instrumentClusterCardViewController for display %@"
+ "[Cluster] Setting new scene for display %@"
+ "[Cluster] Unable to setup card view controller for scene that has not been created %@ "
+ "_clearDetailsHeader"
+ "_configureBackgroundViewsForListHeader:"
+ "_configureConstraintsForDetailsHeader:inContainer:"
+ "_createDetailsButtonsFromListHeader:"
+ "_createDetailsHeaderViewModelForListHeader:"
+ "_createImageOverlayFromListHeader:"
+ "_createNewDetailsHeaderWithViewModel:margins:"
+ "_createSportsOverlayFromListHeader:"
+ "_detailsHeaderFromContainer:"
+ "_instrumentClusterCardViewControllerMapTable"
+ "_instrumentClusterSceneMapTable"
+ "_tableViewMarginsForDetailsHeader"
+ "_updateExistingDetailsHeader:container:viewModel:margins:"
+ "instrumentClusterCardViewControllerForDisplayIdentifier:"
+ "instrumentClusterCardViewControllerMapTable"
+ "instrumentClusterSceneForDisplayIdentifier:"
+ "instrumentClusterSceneMapTable"
+ "keyEnumerator"
+ "nowPlayingViewControllerShouldOverrideLeftBarButtons:"
+ "setInstrumentClusterCardViewControllerMapTable:"
+ "setInstrumentClusterScene:forDisplayIdentifier:"
+ "setInstrumentClusterSceneMapTable:"
+ "v32@?0@\"CPSInstrumentClusterCardViewController\"8Q16^B24"
+ "v56@0:8@16{NSDirectionalEdgeInsets=dddd}24"
+ "v72@0:8@16@24@32{NSDirectionalEdgeInsets=dddd}40"
+ "{NSDirectionalEdgeInsets=dddd}16@0:8"
- "\"\x8f\v"
- "%@ Setting constraints for ETA Card with layout: %@"
- "%@ Setting constraints for platter view with layout: %@"
- "@\"CPSInstrumentClusterCardViewController\""
- "Creating _instrumentClusterCardViewController for %@"
- "T@\"CPSInstrumentClusterCardViewController\",&,N,V_instrumentClusterCardViewController"
- "T@\"CPSInstrumentClusterCardViewController\",R,N,V_instrumentClusterMapETAViewController"
- "T@\"FBScene\",W,N,V_instrumentClusterScene"
- "_instrumentClusterCardViewController"
- "_instrumentClusterMapETAViewController"
- "_instrumentClusterScene"
- "instrumentClusterCardViewController"
- "instrumentClusterMapETAViewController"
- "instrumentClusterScene"
- "setInstrumentClusterCardViewController:"
- "setInstrumentClusterScene:"

```
