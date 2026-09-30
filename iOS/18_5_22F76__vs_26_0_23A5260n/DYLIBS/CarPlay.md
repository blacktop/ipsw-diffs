## CarPlay

> `/System/Library/Frameworks/CarPlay.framework/CarPlay`

```diff

-347.26.2.0.0
-  __TEXT.__text: 0x42578
-  __TEXT.__auth_stubs: 0x640
-  __TEXT.__objc_methlist: 0x6a20
-  __TEXT.__const: 0x208
-  __TEXT.__cstring: 0x3746
-  __TEXT.__oslogstring: 0x1cd3
-  __TEXT.__gcc_except_tab: 0x7c0
-  __TEXT.__unwind_info: 0x1580
-  __TEXT.__objc_classname: 0xee2
-  __TEXT.__objc_methname: 0xd865
-  __TEXT.__objc_methtype: 0x2152
-  __TEXT.__objc_stubs: 0x8720
-  __DATA_CONST.__got: 0x5b8
-  __DATA_CONST.__const: 0x1968
-  __DATA_CONST.__objc_classlist: 0x2e8
+474.4.2.0.0
+  __TEXT.__text: 0x46c04
+  __TEXT.__auth_stubs: 0x680
+  __TEXT.__objc_methlist: 0x7170
+  __TEXT.__const: 0x238
+  __TEXT.__cstring: 0x3b29
+  __TEXT.__oslogstring: 0x1e29
+  __TEXT.__gcc_except_tab: 0x808
+  __TEXT.__unwind_info: 0x1718
+  __TEXT.__objc_classname: 0xfca
+  __TEXT.__objc_methname: 0xe488
+  __TEXT.__objc_methtype: 0x221c
+  __TEXT.__objc_stubs: 0x8ce0
+  __DATA_CONST.__got: 0x5f0
+  __DATA_CONST.__const: 0x1ae8
+  __DATA_CONST.__objc_classlist: 0x320
   __DATA_CONST.__objc_catlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x218
+  __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2e70
+  __DATA_CONST.__objc_selrefs: 0x30c8
   __DATA_CONST.__objc_protorefs: 0x108
-  __DATA_CONST.__objc_superrefs: 0x250
-  __AUTH_CONST.__auth_got: 0x330
-  __AUTH_CONST.__const: 0x820
-  __AUTH_CONST.__cfstring: 0x3ae0
-  __AUTH_CONST.__objc_const: 0x192a8
+  __DATA_CONST.__objc_superrefs: 0x288
+  __AUTH_CONST.__auth_got: 0x350
+  __AUTH_CONST.__const: 0x8a0
+  __AUTH_CONST.__cfstring: 0x3dc0
+  __AUTH_CONST.__objc_const: 0x1a188
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0x70c
-  __DATA.__data: 0x1920
-  __DATA.__bss: 0x1e8
+  __AUTH.__objc_data: 0x4b0
+  __DATA.__objc_ivar: 0x768
+  __DATA.__data: 0x1980
+  __DATA.__bss: 0x228
   __DATA_DIRTY.__objc_data: 0x1a90
   __DATA_DIRTY.__bss: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/NetAppsUtilities.framework/NetAppsUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7AD61963-4FEE-33BE-8EEB-1E2F5EF303E5
-  Functions: 2250
-  Symbols:   8449
-  CStrings:  3863
+  UUID: 6EB88C52-D986-3BEC-B2B7-012EA1EFA638
+  Functions: 2410
+  Symbols:   8943
+  CStrings:  4036
 
Symbols:
+ +[CPGridTemplate _setMaximumGridButtonImageSize:]
+ +[CPGridTemplate maximumGridButtonImageSize]
+ +[CPListImageRowItemCardElement convertImage:showImageFullHeight:]
+ +[CPListImageRowItemCardElement maximumFullHeightImageSize]
+ +[CPListImageRowItemCardElement maximumImageSize]
+ +[CPListImageRowItemCardElement supportsSecureCoding]
+ +[CPListImageRowItemCondensedElement maximumImageSize]
+ +[CPListImageRowItemCondensedElement supportsSecureCoding]
+ +[CPListImageRowItemElement _setMaximumImageSize:]
+ +[CPListImageRowItemElement convertImage:]
+ +[CPListImageRowItemElement maximumImageSize]
+ +[CPListImageRowItemElement supportsSecureCoding]
+ +[CPListImageRowItemGridElement maximumImageSize]
+ +[CPListImageRowItemGridElement supportsSecureCoding]
+ +[CPListImageRowItemImageGridElement maximumImageSize]
+ +[CPListImageRowItemImageGridElement supportsSecureCoding]
+ +[CPListImageRowItemRowElement supportsSecureCoding]
+ +[CPListSection allowedItemClasses]
+ +[CPListTemplate _setMaximumGridButtonImageSize:]
+ +[CPListTemplate maximumGridButtonImageSize]
+ +[CPListTemplate maximumHeaderGridButtonCount]
+ +[CPMessageGridItemConfiguration supportsSecureCoding]
+ -[CPGridButton handlePressesEnd]
+ -[CPGridButton handlePressesStart]
+ -[CPGridButton initWithTitleVariants:image:messageConfiguration:handler:]
+ -[CPGridButton messageConfiguration]
+ -[CPGridButton updateImage:]
+ -[CPGridButton updateTitleVariants:]
+ -[CPGridTemplate gridButton:setImageSet:]
+ -[CPGridTemplate gridButton:setTitleVariants:]
+ -[CPGridTemplate gridButton:setUnread:]
+ -[CPListImageRowItem _initWithText:elements:]
+ -[CPListImageRowItem _initWithText:elements:allowsMultipleLines:]
+ -[CPListImageRowItem _populateElementsFromImages:andImageTitles:]
+ -[CPListImageRowItem allowsMultipleLines]
+ -[CPListImageRowItem elements]
+ -[CPListImageRowItem initWithCoder:].cold.1
+ -[CPListImageRowItem initWithCoder:].cold.2
+ -[CPListImageRowItem initWithText:cardElements:allowsMultipleLines:]
+ -[CPListImageRowItem initWithText:condensedElements:allowsMultipleLines:]
+ -[CPListImageRowItem initWithText:elements:allowsMultipleLines:]
+ -[CPListImageRowItem initWithText:elements:style:]
+ -[CPListImageRowItem initWithText:gridElements:allowsMultipleLines:]
+ -[CPListImageRowItem initWithText:imageGridElements:allowsMultipleLines:]
+ -[CPListImageRowItem setElements:]
+ -[CPListImageRowItem style]
+ -[CPListImageRowItemCardElement .cxx_destruct]
+ -[CPListImageRowItemCardElement encodeWithCoder:]
+ -[CPListImageRowItemCardElement initWithCoder:]
+ -[CPListImageRowItemCardElement initWithImage:showImageFullHeight:title:subtitle:tintColor:]
+ -[CPListImageRowItemCardElement setSubtitle:]
+ -[CPListImageRowItemCardElement setTintColor:]
+ -[CPListImageRowItemCardElement setTitle:]
+ -[CPListImageRowItemCardElement showImageFullHeight]
+ -[CPListImageRowItemCardElement subtitle]
+ -[CPListImageRowItemCardElement tintColor]
+ -[CPListImageRowItemCardElement title]
+ -[CPListImageRowItemCondensedElement .cxx_destruct]
+ -[CPListImageRowItemCondensedElement accessorySymbolName]
+ -[CPListImageRowItemCondensedElement encodeWithCoder:]
+ -[CPListImageRowItemCondensedElement imageShape]
+ -[CPListImageRowItemCondensedElement initWithCoder:]
+ -[CPListImageRowItemCondensedElement initWithImage:imageShape:title:subtitle:accessorySymbolName:]
+ -[CPListImageRowItemCondensedElement setAccessorySymbolName:]
+ -[CPListImageRowItemCondensedElement setSubtitle:]
+ -[CPListImageRowItemCondensedElement setTitle:]
+ -[CPListImageRowItemCondensedElement subtitle]
+ -[CPListImageRowItemCondensedElement title]
+ -[CPListImageRowItemElement .cxx_destruct]
+ -[CPListImageRowItemElement _setNeedsUpdate]
+ -[CPListImageRowItemElement encodeWithCoder:]
+ -[CPListImageRowItemElement identifier]
+ -[CPListImageRowItemElement imageSet]
+ -[CPListImageRowItemElement image]
+ -[CPListImageRowItemElement initWithCoder:]
+ -[CPListImageRowItemElement initWithImage:]
+ -[CPListImageRowItemElement initWithImageSet:]
+ -[CPListImageRowItemElement isEnabled]
+ -[CPListImageRowItemElement rowItem]
+ -[CPListImageRowItemElement setEnabled:]
+ -[CPListImageRowItemElement setImage:]
+ -[CPListImageRowItemElement setImageSet:]
+ -[CPListImageRowItemElement setRowItem:]
+ -[CPListImageRowItemGridElement initWithImage:]
+ -[CPListImageRowItemImageGridElement encodeWithCoder:]
+ -[CPListImageRowItemImageGridElement imageShape]
+ -[CPListImageRowItemImageGridElement initWithCoder:]
+ -[CPListImageRowItemImageGridElement initWithImage:imageShape:]
+ -[CPListImageRowItemRowElement .cxx_destruct]
+ -[CPListImageRowItemRowElement encodeWithCoder:]
+ -[CPListImageRowItemRowElement initWithCoder:]
+ -[CPListImageRowItemRowElement initWithImage:title:subtitle:]
+ -[CPListImageRowItemRowElement setSubtitle:]
+ -[CPListImageRowItemRowElement setTitle:]
+ -[CPListImageRowItemRowElement subtitle]
+ -[CPListImageRowItemRowElement title]
+ -[CPListTemplate _gridButtonsByFilteringAndTrimming:]
+ -[CPListTemplate gridButton:setImageSet:]
+ -[CPListTemplate gridButton:setTitleVariants:]
+ -[CPListTemplate gridButton:setUnread:]
+ -[CPListTemplate headerGridButtons]
+ -[CPListTemplate initWithTitle:sections:assistantCellConfiguration:headerGridButtons:]
+ -[CPListTemplate reloadHeaderButtons]
+ -[CPListTemplate setHeaderGridButtons:]
+ -[CPListTemplate setReloadHeaderButtons:]
+ -[CPMapTemplate clientPitchGestureBegan]
+ -[CPMapTemplate clientPitchGestureEndedWithCenterPoint:]
+ -[CPMapTemplate clientPitchGestureWithCenterPoint:]
+ -[CPMapTemplate clientRotationGestureBegan]
+ -[CPMapTemplate clientRotationGestureEndedWithVelocity:]
+ -[CPMapTemplate clientRotationGestureWithCenterPoint:rotation:velocity:]
+ -[CPMapTemplate clientZoomGestureBegan]
+ -[CPMapTemplate clientZoomGestureEndedWithVelocity:]
+ -[CPMapTemplate clientZoomGestureWithCenterPoint:scale:velocity:]
+ -[CPMessageGridItemConfiguration .cxx_destruct]
+ -[CPMessageGridItemConfiguration conversationIdentifier]
+ -[CPMessageGridItemConfiguration encodeWithCoder:]
+ -[CPMessageGridItemConfiguration hash]
+ -[CPMessageGridItemConfiguration initWithCoder:]
+ -[CPMessageGridItemConfiguration initWithConversationIdentifier:unread:]
+ -[CPMessageGridItemConfiguration isEqual:]
+ -[CPMessageGridItemConfiguration isEqualToMessageGridItemConfiguration:]
+ -[CPMessageGridItemConfiguration isUnread]
+ -[CPMessageGridItemConfiguration setUnread:]
+ -[CPMessageGridItemConfiguration setUnreadChangeHandler:]
+ -[CPMessageGridItemConfiguration unreadChangeHandler]
+ -[CPMessageListItem leadingDetailTextImageSet]
+ -[CPMessageListItem leadingDetailTextImage]
+ -[CPMessageListItem setLeadingDetailTextImage:]
+ -[CPMessageListItem setLeadingDetailTextImageSet:]
+ -[CPTemplate templateDidDismissWithIdentifier:]
+ GCC_except_table112
+ GCC_except_table21
+ GCC_except_table25
+ GCC_except_table40
+ GCC_except_table47
+ GCC_except_table55
+ _CPCurrentProcessHasVideoEntitlement
+ _CPMaximumMessageItemLeadingDetailTextImageSize
+ _CPVideoTemplateClasses
+ _CPVideoTemplateClasses.classes
+ _CPVideoTemplateClasses.cold.1
+ _CPVideoTemplateClasses.onceToken
+ _OBJC_CLASS_$_CPListImageRowItemCardElement
+ _OBJC_CLASS_$_CPListImageRowItemCondensedElement
+ _OBJC_CLASS_$_CPListImageRowItemElement
+ _OBJC_CLASS_$_CPListImageRowItemGridElement
+ _OBJC_CLASS_$_CPListImageRowItemImageGridElement
+ _OBJC_CLASS_$_CPListImageRowItemRowElement
+ _OBJC_CLASS_$_CPMessageGridItemConfiguration
+ _OBJC_IVAR_$_CPGridButton._messageConfiguration
+ _OBJC_IVAR_$_CPListImageRowItem._allowsMultipleLines
+ _OBJC_IVAR_$_CPListImageRowItem._elements
+ _OBJC_IVAR_$_CPListImageRowItem._style
+ _OBJC_IVAR_$_CPListImageRowItemCardElement._showImageFullHeight
+ _OBJC_IVAR_$_CPListImageRowItemCardElement._subtitle
+ _OBJC_IVAR_$_CPListImageRowItemCardElement._tintColor
+ _OBJC_IVAR_$_CPListImageRowItemCardElement._title
+ _OBJC_IVAR_$_CPListImageRowItemCondensedElement._accessorySymbolName
+ _OBJC_IVAR_$_CPListImageRowItemCondensedElement._imageShape
+ _OBJC_IVAR_$_CPListImageRowItemCondensedElement._subtitle
+ _OBJC_IVAR_$_CPListImageRowItemCondensedElement._title
+ _OBJC_IVAR_$_CPListImageRowItemElement._enabled
+ _OBJC_IVAR_$_CPListImageRowItemElement._identifier
+ _OBJC_IVAR_$_CPListImageRowItemElement._image
+ _OBJC_IVAR_$_CPListImageRowItemElement._rowItem
+ _OBJC_IVAR_$_CPListImageRowItemImageGridElement._imageShape
+ _OBJC_IVAR_$_CPListImageRowItemRowElement._subtitle
+ _OBJC_IVAR_$_CPListImageRowItemRowElement._title
+ _OBJC_IVAR_$_CPListTemplate._headerGridButtons
+ _OBJC_IVAR_$_CPListTemplate._reloadHeaderButtons
+ _OBJC_IVAR_$_CPMessageGridItemConfiguration._conversationIdentifier
+ _OBJC_IVAR_$_CPMessageGridItemConfiguration._unread
+ _OBJC_IVAR_$_CPMessageGridItemConfiguration._unreadChangeHandler
+ _OBJC_IVAR_$_CPMessageListItem._leadingDetailTextImageSet
+ _OBJC_METACLASS_$_CPListImageRowItemCardElement
+ _OBJC_METACLASS_$_CPListImageRowItemCondensedElement
+ _OBJC_METACLASS_$_CPListImageRowItemElement
+ _OBJC_METACLASS_$_CPListImageRowItemGridElement
+ _OBJC_METACLASS_$_CPListImageRowItemImageGridElement
+ _OBJC_METACLASS_$_CPListImageRowItemRowElement
+ _OBJC_METACLASS_$_CPMessageGridItemConfiguration
+ __OBJC_$_CLASS_METHODS_CPListImageRowItemCardElement
+ __OBJC_$_CLASS_METHODS_CPListImageRowItemCondensedElement
+ __OBJC_$_CLASS_METHODS_CPListImageRowItemElement
+ __OBJC_$_CLASS_METHODS_CPListImageRowItemGridElement
+ __OBJC_$_CLASS_METHODS_CPListImageRowItemImageGridElement
+ __OBJC_$_CLASS_METHODS_CPListImageRowItemRowElement
+ __OBJC_$_CLASS_METHODS_CPMessageGridItemConfiguration
+ __OBJC_$_CLASS_PROP_LIST_CPGridTemplate
+ __OBJC_$_CLASS_PROP_LIST_CPListImageRowItemCardElement
+ __OBJC_$_CLASS_PROP_LIST_CPListImageRowItemElement
+ __OBJC_$_CLASS_PROP_LIST_CPMessageGridItemConfiguration
+ __OBJC_$_INSTANCE_METHODS_CPListImageRowItemCardElement
+ __OBJC_$_INSTANCE_METHODS_CPListImageRowItemCondensedElement
+ __OBJC_$_INSTANCE_METHODS_CPListImageRowItemElement
+ __OBJC_$_INSTANCE_METHODS_CPListImageRowItemGridElement
+ __OBJC_$_INSTANCE_METHODS_CPListImageRowItemImageGridElement
+ __OBJC_$_INSTANCE_METHODS_CPListImageRowItemRowElement
+ __OBJC_$_INSTANCE_METHODS_CPMessageGridItemConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_CPListImageRowItemCardElement
+ __OBJC_$_INSTANCE_VARIABLES_CPListImageRowItemCondensedElement
+ __OBJC_$_INSTANCE_VARIABLES_CPListImageRowItemElement
+ __OBJC_$_INSTANCE_VARIABLES_CPListImageRowItemImageGridElement
+ __OBJC_$_INSTANCE_VARIABLES_CPListImageRowItemRowElement
+ __OBJC_$_INSTANCE_VARIABLES_CPMessageGridItemConfiguration
+ __OBJC_$_PROP_LIST_CPListImageRowItemCardElement
+ __OBJC_$_PROP_LIST_CPListImageRowItemCondensedElement
+ __OBJC_$_PROP_LIST_CPListImageRowItemElement
+ __OBJC_$_PROP_LIST_CPListImageRowItemImageGridElement
+ __OBJC_$_PROP_LIST_CPListImageRowItemRowElement
+ __OBJC_$_PROP_LIST_CPMessageGridItemConfiguration
+ __OBJC_$_PROTOCOL_CLASS_METHODS_OPT_CPGridButtonDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CPControlDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CPGridButtonDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CPListTemplateProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CPGridButtonDelegate
+ __OBJC_$_PROTOCOL_REFS_CPGridButtonDelegate
+ __OBJC_CLASS_PROTOCOLS_$_CPListImageRowItemElement
+ __OBJC_CLASS_PROTOCOLS_$_CPMessageGridItemConfiguration
+ __OBJC_CLASS_RO_$_CPListImageRowItemCardElement
+ __OBJC_CLASS_RO_$_CPListImageRowItemCondensedElement
+ __OBJC_CLASS_RO_$_CPListImageRowItemElement
+ __OBJC_CLASS_RO_$_CPListImageRowItemGridElement
+ __OBJC_CLASS_RO_$_CPListImageRowItemImageGridElement
+ __OBJC_CLASS_RO_$_CPListImageRowItemRowElement
+ __OBJC_CLASS_RO_$_CPMessageGridItemConfiguration
+ __OBJC_LABEL_PROTOCOL_$_CPGridButtonDelegate
+ __OBJC_METACLASS_RO_$_CPListImageRowItemCardElement
+ __OBJC_METACLASS_RO_$_CPListImageRowItemCondensedElement
+ __OBJC_METACLASS_RO_$_CPListImageRowItemElement
+ __OBJC_METACLASS_RO_$_CPListImageRowItemGridElement
+ __OBJC_METACLASS_RO_$_CPListImageRowItemImageGridElement
+ __OBJC_METACLASS_RO_$_CPListImageRowItemRowElement
+ __OBJC_METACLASS_RO_$_CPMessageGridItemConfiguration
+ __OBJC_PROTOCOL_$_CPGridButtonDelegate
+ ___24-[CPMapButton setImage:]_block_invoke
+ ___28-[CPGridButton setDelegate:]_block_invoke
+ ___28-[CPGridButton updateImage:]_block_invoke
+ ___31-[CPListTemplate performUpdate]_block_invoke.126
+ ___36-[CPListImageRowItem initWithCoder:]_block_invoke
+ ___37-[CPListImageRowItem setImageTitles:]_block_invoke
+ ___39-[CPGridTemplate gridButton:setUnread:]_block_invoke
+ ___39-[CPListTemplate gridButton:setUnread:]_block_invoke
+ ___39-[CPMapTemplate clientZoomGestureBegan]_block_invoke
+ ___40-[CPMapTemplate clientPitchGestureBegan]_block_invoke
+ ___41-[CPGridTemplate gridButton:setImageSet:]_block_invoke
+ ___41-[CPListTemplate gridButton:setImageSet:]_block_invoke
+ ___42+[CPListImageRowItemElement convertImage:]_block_invoke
+ ___43-[CPMapTemplate clientRotationGestureBegan]_block_invoke
+ ___46-[CPGridTemplate gridButton:setTitleVariants:]_block_invoke
+ ___46-[CPListTemplate gridButton:setTitleVariants:]_block_invoke
+ ___47-[CPMessageListItem setLeadingDetailTextImage:]_block_invoke
+ ___47-[CPTemplate templateDidDismissWithIdentifier:]_block_invoke
+ ___51-[CPMapTemplate clientPitchGestureWithCenterPoint:]_block_invoke
+ ___52-[CPInterfaceController _connectToListenerEndpoint:]_block_invoke.431
+ ___52-[CPInterfaceController _connectToListenerEndpoint:]_block_invoke.431.cold.1
+ ___52-[CPInterfaceController _connectToListenerEndpoint:]_block_invoke.432
+ ___52-[CPMapTemplate clientZoomGestureEndedWithVelocity:]_block_invoke
+ ___53-[CPListTemplate _gridButtonsByFilteringAndTrimming:]_block_invoke
+ ___54-[CPInterfaceController _completeSetupWithCompletion:]_block_invoke_3
+ ___54-[CPInterfaceController _completeSetupWithCompletion:]_block_invoke_4
+ ___56-[CPMapTemplate clientPitchGestureEndedWithCenterPoint:]_block_invoke
+ ___56-[CPMapTemplate clientRotationGestureEndedWithVelocity:]_block_invoke
+ ___62-[CPInterfaceController clientPushNowPlayingTemplateAnimated:]_block_invoke.446
+ ___64-[CPTemplateApplicationScene initWithSession:connectionOptions:]_block_invoke.6
+ ___65-[CPListImageRowItem _populateElementsFromImages:andImageTitles:]_block_invoke
+ ___65-[CPMapTemplate clientZoomGestureWithCenterPoint:scale:velocity:]_block_invoke
+ ___66+[CPListImageRowItemCardElement convertImage:showImageFullHeight:]_block_invoke
+ ___72-[CPMapTemplate clientRotationGestureWithCenterPoint:rotation:velocity:]_block_invoke
+ ___73-[CPGridButton initWithTitleVariants:image:messageConfiguration:handler:]_block_invoke
+ ___96-[CPListTemplate listTemplateWithIdentifier:didSelectImageAtIndex:inImageRowItemWithIdentifier:]_block_invoke.152
+ ___CPVideoTemplateClasses_block_invoke
+ ___block_descriptor_32_e20_16?0"CPImageSet"8l
+ ___block_descriptor_40_e26_"UIImage"16?0"UIImage"8l
+ ___block_descriptor_40_e8_32s_e17_v16?0"NSValue"8ls32l8
+ ___block_descriptor_40_e8_32w_e8_v12?0B8lw32l8
+ ___block_descriptor_41_e26_"UIImage"16?0"UIImage"8l
+ ___block_descriptor_41_e8_32s_e35_v16?0"<CPGridTemplateProviding>"8ls32l8
+ ___block_descriptor_41_e8_32s_e35_v16?0"<CPListTemplateProviding>"8ls32l8
+ ___block_descriptor_48_e26_"UIImage"16?0"UIImage"8l
+ ___block_descriptor_48_e8_32s40r_e28_v32?0"<CPControl>"8Q16^B24ls32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e24_v32?0"UIImage"8Q16^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e25_v32?0"NSString"8Q16^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e35_v16?0"<CPGridTemplateProviding>"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e37_v32?0"<CPListTemplateItem>"8Q16^B24ls32l8
+ ___block_descriptor_72_e8_32s40s48r_e29_v32?0"CPGridButton"8Q16^B24lr48l8s32l8s40l8
+ ___block_literal_global.114
+ ___block_literal_global.155
+ ___block_literal_global.437
+ ___block_literal_global.448
+ ___block_literal_global.453
+ ___block_literal_global.461
+ ___block_literal_global.466
+ ___block_literal_global.590
+ ___block_literal_global.593
+ ___block_literal_global.595
+ ___block_literal_global.597
+ ___block_literal_global.599
+ ___block_literal_global.601
+ ___block_literal_global.603
+ ___block_literal_global.605
+ ___block_literal_global.607
+ ___block_literal_global.609
+ ___block_literal_global.611
+ ___block_literal_global.613
+ ___block_literal_global.615
+ ___block_literal_global.83
+ __maximumGridButtonImageSize.0
+ __maximumGridButtonImageSize.1
+ _dispatch_group_create
+ _dispatch_group_enter
+ _dispatch_group_leave
+ _dispatch_group_notify
+ _kCPSVideoEntitlementKey
+ _objc_msgSend$UUIDString
+ _objc_msgSend$_gridButtonsByFilteringAndTrimming:
+ _objc_msgSend$_initWithText:elements:
+ _objc_msgSend$_initWithText:elements:allowsMultipleLines:
+ _objc_msgSend$_populateElementsFromImages:andImageTitles:
+ _objc_msgSend$_setMaximumGridButtonImageSize:
+ _objc_msgSend$accessorySymbolName
+ _objc_msgSend$allowedItemClasses
+ _objc_msgSend$allowsMultipleLines
+ _objc_msgSend$convertImage:
+ _objc_msgSend$convertImage:showImageFullHeight:
+ _objc_msgSend$elements
+ _objc_msgSend$gridButton:setImageSet:
+ _objc_msgSend$gridButton:setTitleVariants:
+ _objc_msgSend$gridButton:setUnread:
+ _objc_msgSend$headerGridButtons
+ _objc_msgSend$imageShape
+ _objc_msgSend$initWithImage:title:subtitle:
+ _objc_msgSend$initWithImageSet:
+ _objc_msgSend$initWithTitle:sections:assistantCellConfiguration:
+ _objc_msgSend$initWithTitleVariants:image:messageConfiguration:handler:
+ _objc_msgSend$isEqualToMessageGridItemConfiguration:
+ _objc_msgSend$leadingDetailTextImageSet
+ _objc_msgSend$mapTemplate:didEndZoomGestureWithVelocity:
+ _objc_msgSend$mapTemplate:didRotateWithCenter:rotation:velocity:
+ _objc_msgSend$mapTemplate:didUpdateZoomGestureWithCenter:scale:velocity:
+ _objc_msgSend$mapTemplate:pitchEndedWithCenter:
+ _objc_msgSend$mapTemplate:pitchWithCenter:
+ _objc_msgSend$mapTemplate:rotationDidEndWithVelocity:
+ _objc_msgSend$mapTemplateDidBeginPitchGesture:
+ _objc_msgSend$mapTemplateDidBeginRotationGesture:
+ _objc_msgSend$mapTemplateDidBeginZoomGesture:
+ _objc_msgSend$maximumFullHeightImageSize
+ _objc_msgSend$maximumGridButtonImageSize
+ _objc_msgSend$maximumHeaderGridButtonCount
+ _objc_msgSend$messageConfiguration
+ _objc_msgSend$na_map:
+ _objc_msgSend$preferredGridMaximumGridButtonImageSizeWithReply:
+ _objc_msgSend$preferredListMaximumGridButtonImageSizeWithReply:
+ _objc_msgSend$reloadHeaderButtons
+ _objc_msgSend$reloadTableHeaderGridButtons:
+ _objc_msgSend$rowItem
+ _objc_msgSend$setByAddingObjectsFromSet:
+ _objc_msgSend$setElements:
+ _objc_msgSend$setReloadHeaderButtons:
+ _objc_msgSend$setRowItem:
+ _objc_msgSend$setUnreadChangeHandler:
+ _objc_msgSend$showImageFullHeight
+ _objc_msgSend$tintColor
+ _objc_msgSend$unreadChangeHandler
- -[CPListImageRowItem gridImagesSet]
- -[CPListImageRowItem imageTitles]
- -[CPListImageRowItem setGridImagesSet:]
- GCC_except_table109
- GCC_except_table12
- GCC_except_table31
- GCC_except_table44
- GCC_except_table45
- _OBJC_IVAR_$_CPListImageRowItem._gridImagesSet
- _OBJC_IVAR_$_CPListImageRowItem._imageTitles
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CPControlDelegate
- ___52-[CPGridButton initWithTitleVariants:image:handler:]_block_invoke
- ___52-[CPInterfaceController _connectToListenerEndpoint:]_block_invoke.401
- ___52-[CPInterfaceController _connectToListenerEndpoint:]_block_invoke.401.cold.1
- ___62-[CPInterfaceController clientPushNowPlayingTemplateAnimated:]_block_invoke.412
- ___64-[CPTemplateApplicationScene initWithSession:connectionOptions:]_block_invoke.5
- ___64-[CPTemplateApplicationScene initWithSession:connectionOptions:]_block_invoke_4
- ___64-[CPTemplateApplicationScene initWithSession:connectionOptions:]_block_invoke_5
- ___96-[CPListTemplate listTemplateWithIdentifier:didSelectImageAtIndex:inImageRowItemWithIdentifier:]_block_invoke.146
- ___block_descriptor_40_e37_v32?0"<CPListTemplateItem>"8Q16^B24l
- ___block_descriptor_40_e8_32bs_e17_v16?0"NSValue"8ls32l8
- ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSValue"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40r_e25_v32?0"CPButton"8Q16^B24ls32l8r40l8
- ___block_literal_global.149
- ___block_literal_global.414
- ___block_literal_global.419
- ___block_literal_global.427
- ___block_literal_global.432
- ___block_literal_global.556
- ___block_literal_global.559
- ___block_literal_global.561
- ___block_literal_global.563
- ___block_literal_global.565
- ___block_literal_global.567
- ___block_literal_global.569
- ___block_literal_global.571
- ___block_literal_global.573
- ___block_literal_global.575
- ___block_literal_global.577
- ___block_literal_global.579
- ___block_literal_global.80
- _objc_msgSend$arrayWithCapacity:
- _objc_msgSend$gridImagesSet
- _objc_msgSend$imageTitles
- _objc_msgSend$updateImages:
CStrings:
+ "@\"<CPGridButtonDelegate>\""
+ "@\"CPListImageRowItem\""
+ "@\"CPMessageGridItemConfiguration\""
+ "@16@?0@\"CPImageSet\"8"
+ "@32@0:8@16Q24"
+ "@52@0:8@16B24@28@36@44"
+ "@56@0:8@16Q24@32@40@48"
+ "Application declares video entitlement."
+ "B40@0:8{?=@BBBBBBBBBB}16"
+ "CPGridButtonConversationKey"
+ "CPGridButtonDelegate"
+ "CPGridButtonUnreadKey"
+ "CPGridTemplate setting maxImageSize (%{public}f,%{public}f)"
+ "CPListImageRowItemCardElement"
+ "CPListImageRowItemCondensedElement"
+ "CPListImageRowItemElement"
+ "CPListImageRowItemElement setting maxImageSize (%{public}f,%{public}f)"
+ "CPListImageRowItemGridElement"
+ "CPListImageRowItemImageGridElement"
+ "CPListImageRowItemRowElement"
+ "CPListTemplate setting maxImageSize (%{public}f,%{public}f)"
+ "CPMessageGridItemConfiguration"
+ "Decoding from older version"
+ "Fetched interface controller image sizes."
+ "Sending List Template header update for %@ with %{public}@"
+ "Setting elements: %@"
+ "T@\"<CPGridButtonDelegate>\",W,N,V_delegate"
+ "T@\"CPImageSet\",&,N,V_image"
+ "T@\"CPImageSet\",&,N,V_leadingDetailTextImageSet"
+ "T@\"CPListImageRowItem\",W,N,V_rowItem"
+ "T@\"CPMessageGridItemConfiguration\",R,N,V_messageConfiguration"
+ "T@\"NSArray\",C,N,V_elements"
+ "T@\"NSArray\",C,N,V_headerGridButtons"
+ "T@\"NSArray\",R,C,D,N"
+ "T@\"NSArray\",R,D,N"
+ "T@\"NSString\",C,N,V_accessorySymbolName"
+ "T@\"NSString\",R,N,V_conversationIdentifier"
+ "T@\"UIColor\",C,N,V_tintColor"
+ "T@\"UIImage\",C,D,N"
+ "T@\"UIImage\",C,N"
+ "T@?,C,N,V_unreadChangeHandler"
+ "TB,N,GisUnread,V_unread"
+ "TB,N,V_reloadHeaderButtons"
+ "TB,R,N,V_allowsMultipleLines"
+ "TB,R,N,V_showImageFullHeight"
+ "TQ,R,N,V_imageShape"
+ "UUIDString"
+ "_accessorySymbolName"
+ "_allowsMultipleLines"
+ "_elements"
+ "_gridButtonsByFilteringAndTrimming:"
+ "_headerGridButtons"
+ "_imageShape"
+ "_initWithText:elements:"
+ "_initWithText:elements:allowsMultipleLines:"
+ "_leadingDetailTextImageSet"
+ "_messageConfiguration"
+ "_populateElementsFromImages:andImageTitles:"
+ "_reloadHeaderButtons"
+ "_rowItem"
+ "_setMaximumGridButtonImageSize:"
+ "_showImageFullHeight"
+ "_tintColor"
+ "_unreadChangeHandler"
+ "_zombifyWindow:"
+ "accessorySymbolName"
+ "allowedItemClasses"
+ "allowsMultipleLines"
+ "clientPitchGestureBegan"
+ "clientPitchGestureEndedWithCenterPoint:"
+ "clientPitchGestureWithCenterPoint:"
+ "clientRotationGestureBegan"
+ "clientRotationGestureEndedWithVelocity:"
+ "clientRotationGestureWithCenterPoint:rotation:velocity:"
+ "clientZoomGestureBegan"
+ "clientZoomGestureEndedWithVelocity:"
+ "clientZoomGestureWithCenterPoint:scale:velocity:"
+ "com.apple.developer.carplay-video"
+ "convertImage:"
+ "convertImage:showImageFullHeight:"
+ "elements"
+ "gridButton:setImageSet:"
+ "gridButton:setTitleVariants:"
+ "gridButton:setUnread:"
+ "headerGridButtons"
+ "imageShape"
+ "initWithConversationIdentifier:unread:"
+ "initWithImage:imageShape:"
+ "initWithImage:imageShape:title:subtitle:accessorySymbolName:"
+ "initWithImage:showImageFullHeight:title:subtitle:tintColor:"
+ "initWithImage:title:subtitle:"
+ "initWithImageSet:"
+ "initWithText:cardElements:allowsMultipleLines:"
+ "initWithText:condensedElements:allowsMultipleLines:"
+ "initWithText:elements:allowsMultipleLines:"
+ "initWithText:elements:style:"
+ "initWithText:gridElements:allowsMultipleLines:"
+ "initWithText:imageGridElements:allowsMultipleLines:"
+ "initWithTitle:sections:assistantCellConfiguration:headerGridButtons:"
+ "initWithTitleVariants:image:messageConfiguration:handler:"
+ "isEqualToMessageGridItemConfiguration:"
+ "kCPListImageRowItemAllowMultipleLinesKey"
+ "kCPListImageRowItemCardElementShowImageFullHeightKey"
+ "kCPListImageRowItemCardElementSubtitleKey"
+ "kCPListImageRowItemCardElementTintColorKey"
+ "kCPListImageRowItemCardElementTitleKey"
+ "kCPListImageRowItemCondensedElementAccessorySymbolNameKey"
+ "kCPListImageRowItemCondensedElementImageShapeKey"
+ "kCPListImageRowItemCondensedElementSubtitleKey"
+ "kCPListImageRowItemCondensedElementTitleKey"
+ "kCPListImageRowItemElementIdentifierKey"
+ "kCPListImageRowItemElementImageKey"
+ "kCPListImageRowItemElementIsEnabledKey"
+ "kCPListImageRowItemImageElementsKey"
+ "kCPListImageRowItemImageGridElementImageShapeKey"
+ "kCPListImageRowItemRowElementSubtitleKey"
+ "kCPListImageRowItemRowElementTitleKey"
+ "kCPListImageRowItemStyleKey"
+ "kCPListTemplateHeaderGridButtonsKey"
+ "kCPMessageListItemLeadingDetailTextImageSetKey"
+ "leadingDetailTextImage"
+ "leadingDetailTextImageSet"
+ "mapTemplate:didEndZoomGestureWithVelocity:"
+ "mapTemplate:didRotateWithCenter:rotation:velocity:"
+ "mapTemplate:didUpdateZoomGestureWithCenter:scale:velocity:"
+ "mapTemplate:pitchEndedWithCenter:"
+ "mapTemplate:pitchWithCenter:"
+ "mapTemplate:rotationDidEndWithVelocity:"
+ "mapTemplateDidBeginPitchGesture:"
+ "mapTemplateDidBeginRotationGesture:"
+ "mapTemplateDidBeginZoomGesture:"
+ "maximumFullHeightImageSize"
+ "maximumGridButtonImageSize"
+ "maximumHeaderGridButtonCount"
+ "messageConfiguration"
+ "na_map:"
+ "preferredGridMaximumGridButtonImageSizeWithReply:"
+ "preferredListMaximumGridButtonImageSizeWithReply:"
+ "reloadHeaderButtons"
+ "reloadTableHeaderGridButtons:"
+ "rowItem"
+ "setAccessorySymbolName:"
+ "setByAddingObjectsFromSet:"
+ "setElements:"
+ "setHeaderGridButtons:"
+ "setLeadingDetailTextImage:"
+ "setLeadingDetailTextImageSet:"
+ "setReloadHeaderButtons:"
+ "setRowItem:"
+ "setTintColor:"
+ "setUnread:"
+ "setUnreadChangeHandler:"
+ "showImageFullHeight"
+ "tintColor"
+ "unreadChangeHandler"
+ "updateImage:"
+ "updateTitleVariants:"
+ "v32@0:8@\"NSUUID\"16@\"NSArray\"24"
+ "v32@?0@\"<CPControl>\"8Q16^B24"
+ "v32@?0@\"NSString\"8Q16^B24"
+ "v32@?0@\"UIImage\"8Q16^B24"
+ "v48@0:8{CGPoint=dd}16d32d40"
- "&"
- "B40@0:8{?=@BBBBBBBBB}16"
- "T@\"NSArray\",&,N,V_gridImagesSet"
- "T@\"NSArray\",C,N,V_imageTitles"
- "Unable to identify a grid image for %@"
- "_gridImagesSet"
- "_imageTitles"
- "arrayWithCapacity:"
- "gridImagesSet"
- "setGridImagesSet:"
- "v32@?0@\"CPButton\"8Q16^B24"
- "\x81"
- "\xa1"

```
