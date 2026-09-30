## SpringBoard

> `/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`

```diff

-4557.5.3.0.0
-  __TEXT.__text: 0xb1ea4c
+4557.5.5.100.0
+  __TEXT.__text: 0xb1b960
   __TEXT.__auth_stubs: 0x55a0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xb9980
-  __TEXT.__const: 0x13100
-  __TEXT.__oslogstring: 0x5ee0e
-  __TEXT.__cstring: 0x7e6a2
+  __TEXT.__objc_methlist: 0xb99b8
+  __TEXT.__const: 0x130f0
+  __TEXT.__oslogstring: 0x5ee42
+  __TEXT.__cstring: 0x7e6b5
   __TEXT.__gcc_except_tab: 0x195ac
   __TEXT.__ustring: 0xcce
   __TEXT.__dlopen_cstrs: 0x313
-  __TEXT.__unwind_info: 0x303b0
-  __TEXT.__eh_frame: 0x48
+  __TEXT.__unwind_info: 0x303d0
+  __TEXT.__eh_frame: 0x80
   __TEXT.__objc_classname: 0x22535
-  __TEXT.__objc_methname: 0x1d5b4f
+  __TEXT.__objc_methname: 0x1d5ca2
   __TEXT.__objc_methtype: 0x4d89f
-  __TEXT.__objc_stubs: 0xf6820
-  __DATA_CONST.__got: 0xa4a0
+  __TEXT.__objc_stubs: 0xf68c0
+  __DATA_CONST.__got: 0xa4a8
   __DATA_CONST.__const: 0x1cf60
   __DATA_CONST.__objc_classlist: 0x5310
   __DATA_CONST.__objc_catlist: 0x358
   __DATA_CONST.__objc_nlcatlist: 0x8
   __DATA_CONST.__objc_protolist: 0x2930
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4b788
+  __DATA_CONST.__objc_selrefs: 0x4b7c0
   __DATA_CONST.__objc_protorefs: 0xb8
   __DATA_CONST.__objc_superrefs: 0x4010
   __DATA_CONST.__objc_arraydata: 0x1870
   __AUTH_CONST.__auth_got: 0x2ae8
-  __AUTH_CONST.__const: 0x10248
-  __AUTH_CONST.__cfstring: 0x704e0
-  __AUTH_CONST.__objc_const: 0x26f450
+  __AUTH_CONST.__const: 0x10258
+  __AUTH_CONST.__cfstring: 0x70500
+  __AUTH_CONST.__objc_const: 0x26f490
   __AUTH_CONST.__objc_arrayobj: 0x1770
   __AUTH_CONST.__objc_doubleobj: 0x790
   __AUTH_CONST.__objc_intobj: 0x2cb8
   __AUTH_CONST.__objc_dictobj: 0x320
   __AUTH.__objc_data: 0x10860
-  __DATA.__objc_ivar: 0xf6f4
+  __DATA.__objc_ivar: 0xf6f8
   __DATA.__data: 0x1fb08
   __DATA.__bss: 0xac0
   __DATA.__common: 0xa48

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libutil.dylib
-  UUID: E28D32EF-D36F-3588-B35D-756D60D7B0A0
-  Functions: 71494
-  Symbols:   241838
-  CStrings:  105343
+  UUID: 2C8C5ED9-B12C-36C7-B1DD-355767741E10
+  Functions: 71500
+  Symbols:   241857
+  CStrings:  105357
 
Symbols:
+ -[SBApplication isDefaultWebBrowser]
+ -[SBCoverSheetIconFlyInAnimator _restoreIconGlassGroupingBehaviors]
+ -[SBCoverSheetPresentationManager flyOutOccurredWhileDecelerating]
+ -[SBCoverSheetPresentationManager setFlyOutOccurredWhileDecelerating:]
+ -[SBHomeScreenController iconManager:didRemoveConfigurableDataSource:ofIcon:]
+ _OBJC_CLASS_$_SBFolderIconImageView
+ _OBJC_IVAR_$_SBCoverSheetIconFlyInAnimator._disableGlassGroupingAssertionsForIconViews
+ _OBJC_IVAR_$_SBCoverSheetPresentationManager._flyOutOccurredWhileDecelerating
+ ___62-[SBCoverSheetIconFlyInAnimator prepareWithVelocity:forFlyIn:]_block_invoke
+ ___71-[SBCoverSheetIconFlyInAnimator _updateLabelAlphaForPresentationValue:]_block_invoke.53
+ ___72-[SBCoverSheetIconFlyInAnimator _updateSpreadMultiplierForPresentation:]_block_invoke.47
+ _objc_msgSend$_restoreIconGlassGroupingBehaviors
+ _objc_msgSend$defaultApplicationForCategory:error:
+ _objc_msgSend$disallowGlassGroupingForReason:
+ _objc_msgSend$iconImageView
+ _objc_msgSend$isDefaultWebBrowser
+ _objc_msgSend$isScrollDecelerating
+ _objc_msgSend$setAllowsGlassGroupingOnMiniGridViews:
- _OBJC_IVAR_$_SBCoverSheetIconFlyInAnimator._savedIconGlassGroupingBehaviors
- ___71-[SBCoverSheetIconFlyInAnimator _updateLabelAlphaForPresentationValue:]_block_invoke.46
- ___72-[SBCoverSheetIconFlyInAnimator _updateSpreadMultiplierForPresentation:]_block_invoke.40
- _objc_msgSend$iconGlassGroupingBehavior
- _objc_msgSend$setIconGlassGroupingBehavior:
CStrings:
+ "%{public}@: removed config data for key: %{public}@"
+ "CoverSheetFlyInOut"
+ "TB,N,V_flyOutOccurredWhileDecelerating"
+ "TB,R,N,GisDefaultWebBrowser"
+ "_disableGlassGroupingAssertionsForIconViews"
+ "_flyOutOccurredWhileDecelerating"
+ "_restoreIconGlassGroupingBehaviors"
+ "defaultApplicationForCategory:error:"
+ "defaultWebBrowser"
+ "disallowGlassGroupingForReason:"
+ "flyOutOccurredWhileDecelerating"
+ "iconImageView"
+ "isDefaultWebBrowser"
+ "isScrollDecelerating"
+ "setAllowsGlassGroupingOnMiniGridViews:"
+ "setFlyOutOccurredWhileDecelerating:"
- "_savedIconGlassGroupingBehaviors"
- "iconGlassGroupingBehavior"
- "setIconGlassGroupingBehavior:"

```
