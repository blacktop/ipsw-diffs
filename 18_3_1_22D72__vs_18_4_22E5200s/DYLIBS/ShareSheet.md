## ShareSheet

> `/System/Library/PrivateFrameworks/ShareSheet.framework/ShareSheet`

```diff

-2060.40.21.0.0
-  __TEXT.__text: 0xb7a78
-  __TEXT.__auth_stubs: 0xe90
-  __TEXT.__objc_methlist: 0xd91c
-  __TEXT.__const: 0x5c0
-  __TEXT.__oslogstring: 0x6419
-  __TEXT.__cstring: 0x6640
+2060.50.111.2.1
+  __TEXT.__text: 0xb886c
+  __TEXT.__auth_stubs: 0xeb0
+  __TEXT.__objc_methlist: 0x102ec
+  __TEXT.__const: 0x5d0
+  __TEXT.__gcc_except_tab: 0x2198
+  __TEXT.__oslogstring: 0x65d5
+  __TEXT.__cstring: 0x68b4
   __TEXT.__dlopen_cstrs: 0x831
   __TEXT.__ustring: 0xca
-  __TEXT.__gcc_except_tab: 0x20e0
-  __TEXT.__unwind_info: 0x2fe8
-  __TEXT.__objc_classname: 0x239e
-  __TEXT.__objc_methname: 0x2b484
-  __TEXT.__objc_methtype: 0x70a8
-  __TEXT.__objc_stubs: 0x1b080
+  __TEXT.__unwind_info: 0x30e8
+  __TEXT.__objc_classname: 0x23b7
+  __TEXT.__objc_methname: 0x2b6fe
+  __TEXT.__objc_methtype: 0x71fb
+  __TEXT.__objc_stubs: 0x1b200
   __DATA_CONST.__got: 0xf58
-  __DATA_CONST.__const: 0x2718
+  __DATA_CONST.__const: 0x2740
   __DATA_CONST.__objc_classlist: 0x608
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x3a0
+  __DATA_CONST.__objc_protolist: 0x3a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7e98
+  __DATA_CONST.__objc_selrefs: 0x85d8
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x3d8
   __DATA_CONST.__objc_arraydata: 0x678
-  __AUTH_CONST.__auth_got: 0x758
+  __AUTH_CONST.__auth_got: 0x768
   __AUTH_CONST.__const: 0x1060
-  __AUTH_CONST.__cfstring: 0x4fc0
-  __AUTH_CONST.__objc_const: 0x2ce18
+  __AUTH_CONST.__cfstring: 0x5400
+  __AUTH_CONST.__objc_const: 0x283a0
   __AUTH_CONST.__objc_arrayobj: 0x510
   __AUTH_CONST.__objc_dictobj: 0x730
   __AUTH_CONST.__objc_intobj: 0x78
-  __AUTH.__objc_data: 0x1db0
-  __AUTH.__data: 0x178
-  __DATA.__objc_ivar: 0x134c
-  __DATA.__data: 0x2b88
-  __DATA.__bss: 0x7b0
-  __DATA_DIRTY.__objc_data: 0x1ea0
-  __DATA_DIRTY.__data: 0x78
+  __AUTH.__objc_data: 0x20a8
+  __AUTH.__data: 0x170
+  __DATA.__objc_ivar: 0x1358
+  __DATA.__data: 0x2be8
+  __DATA.__bss: 0x7c0
+  __DATA_DIRTY.__objc_data: 0x1ba8
+  __DATA_DIRTY.__data: 0x70
   __DATA_DIRTY.__bss: 0x2a0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5424
-  Symbols:   6501
-  CStrings:  8605
+  Functions: 5531
+  Symbols:   6642
+  CStrings:  8673
 
Symbols:
+ _OBJC_CLASS_$_SFShareSheetSessionTestingSnapshot
+ _SFFilterStringsAndWebURLsFromList
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x10
- _OBJC_CLASS_$_UITransitionView
- _SFFilterStringsFromList
CStrings:
+ "\x11D"
+ "2\x11\x12\x14\x19\x14\x11"
+ "?D!"
+ "@\"<SFActivityItemsService>\""
+ "@\"<SFActivityItemsService>\"24@0:8@\"SHSheetSession\"16"
+ "@\"SFShareSheetSessionTestingSnapshot\""
+ "B24@0:8@\"NSURL\"16"
+ "B56@0:8@16@24@32@40@48"
+ "SFActivityItemsService"
+ "ShareSheet.RemoteContainerView"
+ "ShareSheetSnapshotCollection"
+ "T@\"<SFActivityItemsService>\",R,W,N,V_service"
+ "T@\"<SHSheetActivityItemsManagerCollaborationDelegate>\",R,W,N,V_collaborationDelegate"
+ "T@\"<SHSheetActivityItemsManagerDelegate>\",R,W,N,V_delegate"
+ "T@\"SFShareSheetSessionTestingSnapshot\",&,N,V_testingSnapshot"
+ "UIAVC: ignoring _updateActivityItems request activityItemsNeedsUpdate:%@  applicationActivitiesNeedsUpdate:%@ isAppearingOrAppeared:%@ shouldCheckIsAppearingOrAppeared:%@"
+ "URL:%{private}@ is not shareable by client."
+ "_activityItemsService"
+ "_appearState"
+ "_configureContentManagedForActivityItem:activityItemValue:outURLs:outScopedURLs:activity:"
+ "_isAppearingOrAppeared"
+ "_service"
+ "_testingSnapshot"
+ "_updateActivityItems called when Share Sheet is not appearing or appeared! Please only call _updateActivityItems when Share Sheet is fully presented."
+ "aURL:%{private}@ is not shareable by client."
+ "actionGroupCell"
+ "activityCell"
+ "activityItemsServiceForSession:"
+ "activityViewControllerDidDisappearWithSessionID:testingSnapshot:"
+ "airDropCell"
+ "canShareFileURL:"
+ "canShareFileURL:completionHandler:"
+ "cellTitleLabel"
+ "collectionView.footerEditView"
+ "collectionView.footerView"
+ "collectionView.sectionFooter"
+ "collectionView.sectionHeader"
+ "footer.textView"
+ "header.closeButton"
+ "header.linkView"
+ "header.titleLabel"
+ "header.titleView"
+ "heroActionCell"
+ "initWithActivityItems:activityViewController:delegate:collaborationDelegate:service:"
+ "initWithItems:applicationBundleID:pid:"
+ "magicHeadCell.contentView"
+ "peopleCell"
+ "placeholderActivityItemValuesForSendCopyMode"
+ "setAccessibilityIdentifier:"
+ "setTestingSnapshot:"
+ "shareCell"
+ "shareSheet.activity.contentView"
+ "skipping activityItem:%{private}@"
+ "testingSnapshot"
+ "textField:insertInputSuggestion:"
+ "textView:insertInputSuggestion:"
+ "updateWithFinalItems:forActivityType:forCollaboration:"
+ "updateWithPlaceholderItems:collaborationItem:supportsCollaboration:supportsSendCopy:"
+ "v32@0:8@\"NSString\"16@\"SFShareSheetSessionTestingSnapshot\"24"
+ "v32@0:8@\"NSURL\"16@?<v@?B>24"
+ "v32@0:8@\"UITextField\"16@\"UIInputSuggestion\"24"
+ "v32@0:8@\"UITextView\"16@\"UIInputSuggestion\"24"
- "\x114"
- "2\x11\x12\x14\x19\x14"
- "?D"
- "T@\"<SHSheetActivityItemsManagerCollaborationDelegate>\",W,N,V_collaborationDelegate"
- "T@\"<SHSheetActivityItemsManagerDelegate>\",W,N,V_delegate"
- "_configureContentManagedForActivityItem:activityItemValue:outURLs:outScopedURLs:"
- "activityViewControllerDidDisappearWithSessionID:"
- "defaultDurationForTransition:"
- "initWithActivityItems:activityViewController:delegate:collaborationDelegate:"

```
