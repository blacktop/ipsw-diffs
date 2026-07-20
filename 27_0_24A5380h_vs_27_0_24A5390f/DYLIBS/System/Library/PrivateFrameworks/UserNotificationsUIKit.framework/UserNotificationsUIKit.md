## UserNotificationsUIKit

> `/System/Library/PrivateFrameworks/UserNotificationsUIKit.framework/UserNotificationsUIKit`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift_as_ret`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA.__objc_stublist`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-1065.0.0.0.0
-  __TEXT.__text: 0x1bf2ec
-  __TEXT.__objc_methlist: 0x1ac4c
+1070.0.0.0.0
+  __TEXT.__text: 0x1c001c
+  __TEXT.__objc_methlist: 0x1acac
   __TEXT.__const: 0x43e4
-  __TEXT.__gcc_except_tab: 0x2d28
-  __TEXT.__cstring: 0x9fbd
-  __TEXT.__oslogstring: 0xfd69
+  __TEXT.__gcc_except_tab: 0x2d3c
+  __TEXT.__cstring: 0x9fcd
+  __TEXT.__oslogstring: 0x100b9
   __TEXT.__ustring: 0x22
   __TEXT.__constg_swiftt: 0x1cd8
   __TEXT.__swift5_typeref: 0x3d26

   __TEXT.__swift5_proto: 0x180
   __TEXT.__swift5_types: 0x12c
   __TEXT.__swift5_mpenum: 0x5c
-  __TEXT.__swift5_capture: 0xd24
+  __TEXT.__swift5_capture: 0xd34
   __TEXT.__swift5_protos: 0x20
   __TEXT.__swift_as_entry: 0x2c
   __TEXT.__swift_as_cont: 0x50
   __TEXT.__swift_as_ret: 0x1c
-  __TEXT.__unwind_info: 0x7418
+  __TEXT.__unwind_info: 0x7420
   __TEXT.__eh_frame: 0xd30
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0xb0
   __DATA_CONST.__objc_protolist: 0x608
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xcb18
+  __DATA_CONST.__objc_selrefs: 0xcb10
   __DATA_CONST.__objc_protorefs: 0xd8
   __DATA_CONST.__objc_superrefs: 0x570
   __DATA_CONST.__objc_arraydata: 0x158
-  __DATA_CONST.__got: 0x18a0
-  __AUTH_CONST.__const: 0x51c0
-  __AUTH_CONST.__cfstring: 0x7ea0
-  __AUTH_CONST.__objc_const: 0x26bb8
+  __DATA_CONST.__got: 0x18a8
+  __AUTH_CONST.__const: 0x51e8
+  __AUTH_CONST.__cfstring: 0x7ee0
+  __AUTH_CONST.__objc_const: 0x26bc8
   __AUTH_CONST.__objc_intobj: 0x330
   __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__objc_dictobj: 0x28

   __AUTH_CONST.__auth_got: 0x15a0
   __AUTH.__objc_data: 0x24d8
   __AUTH.__data: 0x3d8
-  __DATA.__objc_ivar: 0x1774
+  __DATA.__objc_ivar: 0x1770
   __DATA.__data: 0x5248
   __DATA.__objc_stublist: 0x8
   __DATA.__bss: 0x14c8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10958
-  Symbols:   19836
-  CStrings:  2149
+  Functions: 10966
+  Symbols:   19839
+  CStrings:  2162
 
Symbols:
+ -[NCAppPickerViewController _collectionViewContentHeight]
+ -[NCAppPickerViewController _updateLayoutSizesForWidth:onLayout:]
+ -[NCAppPickerViewController preferredContentSize]
+ -[NCAppPickerViewController viewWillLayoutSubviews]
+ -[NCDigestOnboardingNavigationController viewDidLoad]
+ -[NCNotificationGroupList contentRevealRelayArmed]
+ -[NCNotificationGroupList contentRevealReportCount]
+ -[NCNotificationGroupList setContentRevealRelayArmed:]
+ -[NCNotificationGroupList setContentRevealReportCount:]
+ -[NCNotificationStructuredSectionList notificationListPresentableGroup:didUpdatePreferredContentSize:]
+ GCC_except_table103
+ GCC_except_table147
+ GCC_except_table178
+ GCC_except_table200
+ GCC_except_table203
+ GCC_except_table232
+ _OBJC_IVAR_$_NCAppPickerViewController._cachedLayoutWidth
+ _OBJC_IVAR_$_NCAppPickerViewController._collectionViewHeightConstraint
+ _OBJC_IVAR_$_NCNotificationGroupList._contentRevealRelayArmed
+ _OBJC_IVAR_$_NCNotificationGroupList._contentRevealReportCount
+ _objc_msgSend$_collectionViewContentHeight
+ _objc_msgSend$_updateLayoutSizesForWidth:onLayout:
+ _objc_msgSend$contentRevealRelayArmed
+ _objc_msgSend$contentRevealReportCount
+ _objc_msgSend$convertRect:fromCoordinateSpace:
+ _objc_msgSend$notificationListBaseComponent:didUpdatePreferredContentSize:
+ _objc_msgSend$notificationListPresentableGroup:didUpdatePreferredContentSize:
+ _objc_msgSend$preferredContentSizeForView:
+ _objc_msgSend$setContentRevealRelayArmed:
+ _objc_msgSend$setContentRevealReportCount:
- +[NCAppPickerViewHeader _descriptionFont]
- +[NCAppPickerViewHeader _descriptionText]
- +[NCAppPickerViewHeader _titleFont]
- +[NCAppPickerViewHeader _titleText]
- -[NCAppPickerViewController _updateHeightConstraintAndLayoutIfNeeded:]
- -[NCAppPickerViewController _updateHeightConstraintAndLayout]
- GCC_except_table177
- GCC_except_table184
- GCC_except_table199
- GCC_except_table231
- _OBJC_IVAR_$_NCAppPickerViewController._collectionViewVisibleHeight
- _OBJC_IVAR_$_NCAppPickerViewController._heightConstraint
- _OBJC_IVAR_$_NCAppPickerViewController._topConstraint
- _OBJC_IVAR_$_NCAppPickerViewHeader._descriptionLabel
- _OBJC_IVAR_$_NCAppPickerViewHeader._titleLabel
- ___81-[NCNotificationSeamlessContentView _layoutSubviewInBounds:measuringOnly:traits:]_block_invoke_20
- _objc_msgSend$_descriptionFont
- _objc_msgSend$_descriptionText
- _objc_msgSend$_updateHeightConstraintAndLayoutIfNeeded:
- _objc_msgSend$fontDescriptorWithSymbolicTraits:
- _objc_msgSend$needsUpdateConstraints
- _objc_msgSend$notificationStructuredListViewControllerRequestsVerticalSizeClass:
- _objc_msgSend$performSelector:withObject:afterDelay:
- _objc_msgSend$preferredFontDescriptorWithTextStyle:
- _objc_msgSend$setVerticalSizeClass:
- _objc_msgSend$userInterfaceSizeClass
- _objc_msgSend$verticalScrollIndicatorInsets
CStrings:
+ "%{public}@ content-reveal last report; re-pinning root stack"
+ "%{public}@ content-reveal relay %{public}@ (deviceAuthenticated %d)"
+ "%{public}@ content-reveal report %lu of %lu for %{public}@ (h=%.1f)"
+ "%{public}@ onInsert escalating to reloadNotificationRequest: request=%{public}@; hadCellUnderSelf=%{BOOL}d"
+ "%{public}@ orientation updated; verticalSizeClass: %lu"
+ "Skip content-reveal re-pin: a scroll is already queued"
+ "Skip content-reveal re-pin: currentPageType is nil"
+ "Skip content-reveal re-pin: history section reveal does not move the stack"
+ "Skip content-reveal re-pin: no below-the-fold content to scroll"
+ "Skip content-reveal re-pin: no page for target type %{public}s"
+ "Skip content-reveal re-pin: user is engaging the view; isUserEngagingView: %{bool}d; isTracking: %{bool}d; isDragging: %{bool}d"
+ "Skipping layout of %{public}@ with non-finite frame %{public}@"
+ "armed"
+ "deviceAuthenticated set to %{bool,public}d; backlightLuminance %{public}ld; shouldAllowScrollValidation %{bool,public}d"
+ "disarmed"
- "%{public}@ orientation updated; verticalSizeClass: %lu; global verticalSizeClass: %lu"
- "ListView's window is nil, using view bounds as a fallback size for orientation check"
```
