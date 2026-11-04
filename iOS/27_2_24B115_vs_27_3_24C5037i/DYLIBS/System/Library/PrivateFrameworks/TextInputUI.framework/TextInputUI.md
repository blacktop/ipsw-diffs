## TextInputUI

> `/System/Library/PrivateFrameworks/TextInputUI.framework/TextInputUI`

```diff

-9127.1.13.1.105
-  __TEXT.__text: 0x144940
-  __TEXT.__objc_methlist: 0x1089c
+9127.2.6.0.0
+  __TEXT.__text: 0x14bf8c
+  __TEXT.__objc_methlist: 0x10d04
   __TEXT.__dlopen_cstrs: 0x3f1
-  __TEXT.__const: 0x41fe
-  __TEXT.__swift5_typeref: 0x1f0a
-  __TEXT.__swift5_capture: 0x6e0
-  __TEXT.__cstring: 0xd988
-  __TEXT.__constg_swiftt: 0x1acc
-  __TEXT.__swift5_reflstr: 0xe05
+  __TEXT.__const: 0x423e
+  __TEXT.__swift5_typeref: 0x1f2c
+  __TEXT.__swift5_capture: 0x6ec
+  __TEXT.__cstring: 0xdb5d
+  __TEXT.__constg_swiftt: 0x1ad4
+  __TEXT.__swift5_reflstr: 0xe15
   __TEXT.__swift5_assocty: 0x3a0
-  __TEXT.__swift5_fieldmd: 0xfe4
+  __TEXT.__swift5_fieldmd: 0xff0
   __TEXT.__swift5_builtin: 0x17c
-  __TEXT.__oslogstring: 0x6558
+  __TEXT.__oslogstring: 0x6bd2
   __TEXT.__swift5_proto: 0x1c0
   __TEXT.__swift5_types: 0x170
   __TEXT.__swift_as_entry: 0x88
   __TEXT.__swift_as_ret: 0x8c
-  __TEXT.__swift_as_cont: 0x200
+  __TEXT.__swift_as_cont: 0x204
   __TEXT.__swift5_mpenum: 0x1c
   __TEXT.__swift5_protos: 0xc
   __TEXT.__ustring: 0x258
-  __TEXT.__unwind_info: 0x5618
-  __TEXT.__eh_frame: 0x2254
+  __TEXT.__unwind_info: 0x5730
+  __TEXT.__eh_frame: 0x227c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x7b00
-  __DATA_CONST.__objc_classlist: 0x750
+  __DATA_CONST.__const: 0x7b58
+  __DATA_CONST.__objc_classlist: 0x758
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x2c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa9f0
+  __DATA_CONST.__objc_selrefs: 0xacd0
   __DATA_CONST.__objc_protorefs: 0xa8
   __DATA_CONST.__objc_superrefs: 0x468
-  __DATA_CONST.__objc_arraydata: 0xb10
-  __DATA_CONST.__got: 0x16b8
-  __AUTH_CONST.__const: 0x3398
-  __AUTH_CONST.__cfstring: 0xec60
-  __AUTH_CONST.__objc_const: 0x1a948
+  __DATA_CONST.__objc_arraydata: 0xb18
+  __DATA_CONST.__got: 0x1700
+  __AUTH_CONST.__const: 0x33a0
+  __AUTH_CONST.__cfstring: 0xee20
+  __AUTH_CONST.__objc_const: 0x1ae68
   __AUTH_CONST.__objc_intobj: 0x3d8
   __AUTH_CONST.__objc_arrayobj: 0x2b8
   __AUTH_CONST.__objc_doubleobj: 0x1a0
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_floatobj: 0xe0
-  __AUTH_CONST.__auth_got: 0x1e28
-  __AUTH.__objc_data: 0x3b68
-  __AUTH.__data: 0x1038
-  __DATA.__objc_ivar: 0x1250
-  __DATA.__data: 0x2eb8
+  __AUTH_CONST.__auth_got: 0x1e68
+  __AUTH.__objc_data: 0x3bb8
+  __AUTH.__data: 0x1040
+  __DATA.__objc_ivar: 0x12b0
+  __DATA.__data: 0x2ed8
   __DATA.__common: 0x290
-  __DATA_DIRTY.__objc_data: 0x20a0
+  __DATA_DIRTY.__objc_data: 0x20a8
   __DATA_DIRTY.__data: 0x2e8
   __DATA_DIRTY.__bss: 0x500
   __DATA_DIRTY.__common: 0x8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7262
-  Symbols:   11095
-  CStrings:  2756
+  Functions: 7368
+  Symbols:   11236
+  CStrings:  2792
 
Symbols:
+ +[TUIKeyplane layoutClassFromScreenDimensions:screenToNativeScaleRatio:]
+ +[TUIKeyplane maxVariantsPerRowForKey:layoutStyle:rowLimit:maxRows:split:]
+ +[TUIKeyplane variantRowLimitForKey:layoutStyle:variantSelectorType:split:]
+ +[TUIKeyplaneView remoteViewCacheSignatureForKeyplaneName:surface:layoutClass:minorEdgeWidth:handBias:]
+ +[TUIKeyplaneView reuseActionForParentUnchanged:placementUnchanged:appliedAnchorsStillLive:]
+ -[TUIAssistantButtonSizeProvider .cxx_destruct]
+ -[TUIAssistantButtonSizeProvider _fittingWidthForImage:]
+ -[TUIAssistantButtonSizeProvider imageSymbolConfiguration]
+ -[TUIAssistantButtonSizeProvider maximumImageItemWidth]
+ -[TUIAssistantButtonSizeProvider setImageSymbolConfiguration:]
+ -[TUIAssistantButtonSizeProvider setMaximumImageItemWidth:]
+ -[TUIAssistantButtonSizeProvider setSizesImageItemsToFitImage:]
+ -[TUIAssistantButtonSizeProvider sizesImageItemsToFitImage]
+ -[TUICandidateLayout singleRowHeightFittingCollectionView:originY:]
+ -[TUICandidateView arrowButtonHeightFittingBounds:top:]
+ -[TUIGenmojiCandidate initWithInput:rawInput:flow:pregeneratedStickerWrapper:]
+ -[TUIInputSession _newAutofillContextWithConnectedAppInfo:connection:]
+ -[TUIInputSessionProxy _applicationDidBecomeActive:]
+ -[TUIInputSessionProxy _applicationDidEnterBackground:]
+ -[TUIInputSessionProxy _applicationWillEnterForeground:]
+ -[TUIInputSessionProxy _beginExternalMessageSession]
+ -[TUIInputSessionProxy _endExternalMessageSessionPermanently:]
+ -[TUIInputSessionProxy invalidationHandler]
+ -[TUIInputSessionProxy setInvalidationHandler:]
+ -[TUIKBKeyView _inheritEmojiWideEdgeControlKeyCapsuleHeightForFactory:]
+ -[TUIKBKeyView _setRealBackgroundLayerHidden:animated:]
+ -[TUIKBKeyView installedRemoteContentConstraints]
+ -[TUIKBKeyView setInstalledRemoteContentConstraints:]
+ -[TUIKey isSplitLayout]
+ -[TUIKey setSplitLayout:]
+ -[TUIKeyPopupView isSplitLayout]
+ -[TUIKeyPopupView setSplitLayout:]
+ -[TUIKeyboardAnimationInfo convertedNotificationBeginFrame]
+ -[TUIKeyboardAnimationInfo convertedNotificationEndFrame]
+ -[TUIKeyboardAnimationInfo hasConvertedBeginFrame]
+ -[TUIKeyboardAnimationInfo hasConvertedEndFrame]
+ -[TUIKeyboardAnimationInfo invalidateConvertedFrames]
+ -[TUIKeyboardAnimationInfo setConvertedNotificationBeginFrame:]
+ -[TUIKeyboardAnimationInfo setConvertedNotificationEndFrame:]
+ -[TUIKeyboardAnimationInfo updateBeginFrameForConversion:]
+ -[TUIKeyboardAnimationInfo updateEndFrameForConversion:]
+ -[TUIKeyboardTrackingCoordinator adjustedIAVRectForNotificationRect:iavBounds:]
+ -[TUIKeyboardTrackingCoordinator appScreenRectForNotificationRect:iavBounds:]
+ -[TUIKeyboardTrackingCoordinator updateAnimationInfoIfNeeded:]
+ -[TUIKeyboardTrackingProvider shouldConvertFrameForScene:]
+ -[TUIKeyplane currentOverride]
+ -[TUIKeyplane defaultKeysOrderedByRowForKeyplane:isNumPad:]
+ -[TUIKeyplane duplicateKeyToBeDoubleHeight:atIndex:inRow:type:]
+ -[TUIKeyplane moveControlKey:toRowAtIndex:inRows:]
+ -[TUIKeyplane multiplierTotalCountingSplitDuplicateOnceForRow:]
+ -[TUIKeyplane reconcileConcaveCornerForKey:isMultiRow:]
+ -[TUIKeyplane resolvedRowTreesForType:]
+ -[TUIKeyplane rowSetForOverride:type:]
+ -[TUIKeyplane setCurrentOverride:]
+ -[TUIKeyplane setStackedControlColumnSwitchKey:spanningFromRow:toRow:inRows:]
+ -[TUIKeyplane splitDuplicateKeys]
+ -[TUIKeyplane stackedControlColumnSwitchKeyInRows:]
+ -[TUIKeyplane stringFromRowsetOverride:]
+ -[TUIKeyplane unduplicateDoubleHeightKey:fromRow:type:]
+ -[TUIKeyplane updateStackedControlColumnForRows:]
+ -[TUIKeyplane usesIMButtonsInKeyplaneRowSet]
+ -[TUIKeyplaneRow _needsNarrowerSplitReturnKey:rowLayoutType:]
+ -[TUIKeyplaneView _clearStoredVariantViews]
+ -[TUIKeyplaneView _currentRemoteViewCacheSignature]
+ -[TUIKeyplaneView _discardAllRemoteViews]
+ -[TUIKeyplaneView _discardRemoteViewsExcept:]
+ -[TUIKeyplaneView _emojiGridPlacementForHostKeyView:]
+ -[TUIKeyplaneView _installRemoteViewForKeyIfAvailable:liveRemoteViews:]
+ -[TUIKeyplaneView _pushEmojiWideEdgeControlKeyCapsuleHeightToFactory:]
+ -[TUIKeyplaneView _vendRemoteViewForKey:cacheID:]
+ -[TUIKeyplaneView _walkSubtreeForRemoteViews:liveRemoteViews:]
+ -[TUIKeyplaneView dockHidesItemsOverlappingEmoji]
+ -[TUIKeyplaneView emojiBottomRowKeyWidth]
+ -[TUIKeyplaneView emojiBottomRowUsesWideEdgeControlKeys]
+ -[TUIKeyplaneView emojiWideEdgeControlKeyCapsuleHeightForWideMultiplier:]
+ -[TUIKeyplaneView emojiWideEdgeControlKeyMultiplierForBottomRowKeyWidth:]
+ -[TUIKeyplaneView emojiWideEdgeControlKeyMultiplier]
+ -[TUIKeyplaneView maximumRightSplitRowWidth]
+ -[TUIKeyplaneView numberOfRowsForDeterminingKeyplaneInsets]
+ -[TUIKeyplaneView remoteViewCacheSignature]
+ -[TUIKeyplaneView remoteViewPlacementByCacheID]
+ -[TUIKeyplaneView remoteViewsByCacheID]
+ -[TUIKeyplaneView setDockHidesItemsOverlappingEmoji:]
+ -[TUIKeyplaneView setRemoteViewCacheSignature:]
+ -[TUIKeyplaneView setRemoteViewPlacementByCacheID:]
+ -[TUIKeyplaneView setRemoteViewsByCacheID:]
+ -[TUIKeyplaneView setTraitChangeRegistrations:]
+ -[TUIKeyplaneView splitLayoutGuideContainingKeyView:]
+ -[TUIKeyplaneView traitChangeRegistrations]
+ -[TUIRemoteViewPlacement .cxx_destruct]
+ -[TUIRemoteViewPlacement anchorsStillLive]
+ -[TUIRemoteViewPlacement bottomOffset]
+ -[TUIRemoteViewPlacement hostHadWindow]
+ -[TUIRemoteViewPlacement hostInKeyplaneTree]
+ -[TUIRemoteViewPlacement hostWindow]
+ -[TUIRemoteViewPlacement isEqualToPlacement:]
+ -[TUIRemoteViewPlacement leadingExtent]
+ -[TUIRemoteViewPlacement setBottomOffset:]
+ -[TUIRemoteViewPlacement setHostHadWindow:]
+ -[TUIRemoteViewPlacement setHostInKeyplaneTree:]
+ -[TUIRemoteViewPlacement setHostWindow:]
+ -[TUIRemoteViewPlacement setLeadingExtent:]
+ -[TUIRemoteViewPlacement setTopOffset:]
+ -[TUIRemoteViewPlacement setTrailingExtent:]
+ -[TUIRemoteViewPlacement setVerticalExtent:]
+ -[TUIRemoteViewPlacement topOffset]
+ -[TUIRemoteViewPlacement trailingExtent]
+ -[TUIRemoteViewPlacement verticalExtent]
+ -[TUIVariantSelectorView drawsBackground]
+ _CGSizeNearlyEqualToSizeWithTolerance
+ _OBJC_CLASS_$_CATransaction
+ _OBJC_CLASS_$_TUIRemoteViewPlacement
+ _OBJC_CLASS_$_UITextRange
+ _OBJC_IVAR_$_TUIAssistantButtonSizeProvider._imageSymbolConfiguration
+ _OBJC_IVAR_$_TUIAssistantButtonSizeProvider._maximumImageItemWidth
+ _OBJC_IVAR_$_TUIAssistantButtonSizeProvider._sizesImageItemsToFitImage
+ _OBJC_IVAR_$_TUIInputSessionProxy._externalMessageSession
+ _OBJC_IVAR_$_TUIInputSessionProxy._externalMessageSessionDisabled
+ _OBJC_IVAR_$_TUIInputSessionProxy._externalMessageSessionLock
+ _OBJC_IVAR_$_TUIInputSessionProxy._invalidationHandler
+ _OBJC_IVAR_$_TUIKBKeyView._installedRemoteContentConstraints
+ _OBJC_IVAR_$_TUIKey._splitLayout
+ _OBJC_IVAR_$_TUIKeyPopupView._splitLayout
+ _OBJC_IVAR_$_TUIKeyboardAnimationInfo._convertedNotificationBeginFrame
+ _OBJC_IVAR_$_TUIKeyboardAnimationInfo._convertedNotificationEndFrame
+ _OBJC_IVAR_$_TUIKeyplane._currentOverride
+ _OBJC_IVAR_$_TUIKeyplaneView._dockHidesItemsOverlappingEmoji
+ _OBJC_IVAR_$_TUIKeyplaneView._remoteViewCacheSignature
+ _OBJC_IVAR_$_TUIKeyplaneView._remoteViewPlacementByCacheID
+ _OBJC_IVAR_$_TUIKeyplaneView._remoteViewsByCacheID
+ _OBJC_IVAR_$_TUIKeyplaneView._traitChangeRegistrations
+ _OBJC_IVAR_$_TUIRemoteViewPlacement._bottomOffset
+ _OBJC_IVAR_$_TUIRemoteViewPlacement._hostHadWindow
+ _OBJC_IVAR_$_TUIRemoteViewPlacement._hostInKeyplaneTree
+ _OBJC_IVAR_$_TUIRemoteViewPlacement._hostWindow
+ _OBJC_IVAR_$_TUIRemoteViewPlacement._leadingExtent
+ _OBJC_IVAR_$_TUIRemoteViewPlacement._topOffset
+ _OBJC_IVAR_$_TUIRemoteViewPlacement._trailingExtent
+ _OBJC_IVAR_$_TUIRemoteViewPlacement._verticalExtent
+ _OBJC_METACLASS_$_TUIRemoteViewPlacement
+ _TUIViewsShareCommonAncestor
+ _UIApplicationDidBecomeActiveNotification
+ _UIApplicationDidEnterBackgroundNotification
+ _UIApplicationWillEnterForegroundNotification
+ _UIKBTreePropertyRowSetOverride
+ __OBJC_$_INSTANCE_METHODS_TUIRemoteViewPlacement
+ __OBJC_$_INSTANCE_VARIABLES_TUIRemoteViewPlacement
+ __OBJC_$_PROP_LIST_TUIRemoteViewPlacement
+ __OBJC_CLASS_RO_$_TUIRemoteViewPlacement
+ __OBJC_METACLASS_RO_$_TUIRemoteViewPlacement
+ __TUIEmojiSearchFieldHeight
+ ___39-[TUIKeyplane resolvedRowTreesForType:]_block_invoke
+ ___45-[TUIInputSessionProxy _configureConnection:]_block_invoke_2
+ ___65-[TUIKeyboardInputManagerMux newSystemInputManagerWithImplProxy:]_block_invoke
+ ___block_descriptor_40_8_32s_e18_v16?0"UIKBTree"8ls32l8
+ ___block_descriptor_48_8_32w40w_e5_v8?0lw32l8w40l8
+ ___swift_memcpy40_8
+ _kCAFilterColorDodgeBlendMode
+ _symbolic _____Sg 16GenerativeModels0aB12AvailabilityV6PolicyV
+ _symbolic _____XDXMT 11TextInputUI12_Coordinator33_63F729F5376141D9E861BEE38CFE8091LLC
+ _symbolic _____y_____G s23_ContiguousArrayStorageC So8_NSRangeV
+ _type_layout_string So7CGPointV
- +[TUIKeyplane maxVariantsPerRowForKey:layoutStyle:rowLimit:maxRows:]
- +[TUIKeyplane variantRowLimitForKey:layoutStyle:variantSelectorType:]
- -[TUIKeyboardTrackingCoordinator adjustedRectForNotificationRect:iavBounds:]
- -[TUIKeyboardTrackingCoordinator postNotificationsWithInfo:type:start:]
- -[TUIKeyplane defaultKeysOrderedByRowForKeyplane:]
- -[TUIKeyplane duplicateKeyToBeDoubleHeight:atIndex:inRow:]
- -[TUIKeyplane moveControlKey:toRowAtIndex:inRowSet:]
- -[TUIKeyplane setStackedControlColumnSwitchKey:spanningFromRow:toRow:inRowSet:]
- -[TUIKeyplane stackedControlColumnSwitchKeyInRowSet:]
- -[TUIKeyplane unduplicateDoubleHeightKey:fromRow:]
- -[TUIKeyplane updateStackedControlColumnForRowSet:]
- -[TUIKeyplaneView _installRemoteViewForKeyIfAvailable:]
- -[TUIKeyplaneView _walkSubtreeForRemoteViews:]
- -[TUIKeyplaneView setSizeClassTraitChangeRegistration:]
- -[TUIKeyplaneView setTraitChangeRegistration:]
- -[TUIKeyplaneView sizeClassTraitChangeRegistration]
- -[TUIKeyplaneView traitChangeRegistration]
- _NSArgumentDomain
- _OBJC_IVAR_$_TUIKeyplaneView._sizeClassTraitChangeRegistration
- _OBJC_IVAR_$_TUIKeyplaneView._traitChangeRegistration
- _type_layout_string So6CGSizeV
CStrings:
+ "!k"
+ "%@_%@"
+ "%@|%ld|%ld|%ld|%ld"
+ "%s, began external message session"
+ "%s, ending external message session (permanently: %d)"
+ "-[TUIInputSessionProxy _beginExternalMessageSession]"
+ "-[TUIInputSessionProxy _configureConnection:]_block_invoke_2"
+ "-[TUIInputSessionProxy _endExternalMessageSessionPermanently:]"
+ "Duplicate keys found but no split support; number of keys %li number of dupes %li"
+ "EmojiRemoteView Dropped: key %{public}@ was not served on this pass"
+ "EmojiRemoteView Hoisted: key=%{public}@ into containment=%p so its variant selector draws above the search bar"
+ "EmojiRemoteView Host Missing: key=%{public}@ — no host TUIKBKeyView in storedKeyViews; falling back to sibling install"
+ "EmojiRemoteView Installing: key=%{public}@ host=%p hostFrame=%@"
+ "EmojiRemoteView Not Vended: provider returned nil for key %{public}@ displayType=%d"
+ "EmojiRemoteView Reanchored: key=%{public}@ placement changed under a cached remote view — rebuilding its constraints in %p (hadWindow %d→%d, sameWindow %d, inKeyplaneTree %d→%d, extents %ld/%ld/%ld→%ld/%ld/%ld, offsets %.1f/%.1f→%.1f/%.1f)"
+ "EmojiRemoteView Replaced: key=%{public}@ cached remote view can't stay in %p — vending a replacement for %p"
+ "EmojiRemoteView Replaced: key=%{public}@ cached remote view is auto-layout anchored and can't be frame-positioned — vending a replacement"
+ "EmojiRemoteView Window Missing: key=%{public}@ host has no window yet — API fell back to host bounds; a later walk re-anchors it once the host is in a window"
+ "GenerativeModelsAvailability: China policy detected, disabling generative suggestions"
+ "IMButtonsInKeyplane"
+ "KBRowSetOverride"
+ "Number-Alternative-Plane"
+ "Number-Plane"
+ "QWERTY-Lithuanian"
+ "Releasing invalidated system input manager: %@"
+ "Rowset.Override.%@.Row%li"
+ "Rowset.Override.%@.Variant.%@.Row%li"
+ "UIKBTreePropertyRowSetOverride"
+ "W1!"
+ "[FedStats] Could not donate sticker %s to recents: %@"
+ "[Notifications] Converting notification begin frame: %@ to: %@ from: %@"
+ "[Notifications] Converting notification end frame: %@ to: %@ from: %@"
+ "[Notifications] Updating notification info with begin frame: %@ end frame: %@ [%@]"
+ "[Resizing] Keyboard frame %@ does not overlap window %@; posting with the existing notification frame"
+ "[Resizing] Send notifications for size change %@ vs %@"
+ "_%@-%@"
+ "_split_%i"
+ "com.apple.purplebuddy"
+ "didCreate: inserting via UIKeyboardImpl, cannot replace source text"
+ "didCreate: inserting via UITextInput, replacing source text: %{bool}d"
+ "didCreate: inserting via UITextView, replacing source text: %{bool}d"
+ "didCreateSticker: inserting with deleteCount %lu"
+ "keyboard session"
+ "v16@?0@\"UIKBTree\"8"
- "Cached key mismatch but no split support; expected %li vs %li"
- "Provider returned nil for key %{public}@ displayType=%d"
- "W!!"
- "[install-HOIST] key=%{public}@ hoisting grid into containment=%p so its variant selector draws above the search bar"
- "[install-HOST-MISS] key=%{public}@ — no host TUIKBKeyView in storedKeyViews; falling back to sibling install"
- "[install-HOST] key=%{public}@ host=%p hostFrame=%@"
- "[install-WINDOW-MISS] key=%{public}@ host has no window yet — API fell back to host bounds; will retry on next walk"
- "\x8b"
```
