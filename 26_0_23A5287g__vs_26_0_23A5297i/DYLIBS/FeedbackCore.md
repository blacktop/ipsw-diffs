## FeedbackCore

> `/System/Library/PrivateFrameworks/FeedbackCore.framework/FeedbackCore`

```diff

-184.0.0.0.0
-  __TEXT.__text: 0x140ba8
+187.0.0.0.0
+  __TEXT.__text: 0x140c58
   __TEXT.__auth_stubs: 0x2c60
-  __TEXT.__objc_methlist: 0xb4b8
+  __TEXT.__objc_methlist: 0xb4d0
   __TEXT.__const: 0x2df4
   __TEXT.__cstring: 0xc041
   __TEXT.__oslogstring: 0xa166

   __TEXT.__swift5_types: 0x13c
   __TEXT.__swift5_capture: 0xcb8
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x4a68
+  __TEXT.__unwind_info: 0x4a60
   __TEXT.__eh_frame: 0x1680
-  __TEXT.__objc_classname: 0x11cb
-  __TEXT.__objc_methname: 0x1cd63
-  __TEXT.__objc_methtype: 0x3d91
-  __TEXT.__objc_stubs: 0x14ae0
+  __TEXT.__objc_classname: 0x11c9
+  __TEXT.__objc_methname: 0x1ce3e
+  __TEXT.__objc_methtype: 0x3dc2
+  __TEXT.__objc_stubs: 0x14b40
   __DATA_CONST.__got: 0x11d8
   __DATA_CONST.__const: 0x3f10
   __DATA_CONST.__objc_classlist: 0x530
   __DATA_CONST.__objc_catlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x74c0
+  __DATA_CONST.__objc_selrefs: 0x74d8
   __DATA_CONST.__objc_protorefs: 0x98
   __DATA_CONST.__objc_superrefs: 0x288
   __DATA_CONST.__objc_arraydata: 0x4d0
   __AUTH_CONST.__auth_got: 0x1640
   __AUTH_CONST.__const: 0x44c8
   __AUTH_CONST.__cfstring: 0x8e00
-  __AUTH_CONST.__objc_const: 0x1d500
+  __AUTH_CONST.__objc_const: 0x1d508
   __AUTH_CONST.__objc_intobj: 0x300
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0x498

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D12570FE-5601-34AB-B4F0-4DF976BF2D03
-  Functions: 7264
-  Symbols:   15521
-  CStrings:  9313
+  UUID: 53A88FA9-6F67-3EE5-90AC-CB50270A64D2
+  Functions: 7266
+  Symbols:   15528
+  CStrings:  9316
 
Symbols:
+ +[NSDate(Utils) fbkDateWithYear:month:day:]
+ +[NSDate(Utils) fbkTomorrow]
+ -[FBKBugFormTableViewController _fbkShowSpinnerWithStatus:userInteractionEnabled:]
+ -[FBKBugFormTableViewController fbkShowSpinnerWithStatus:]
+ -[FBKLaunchAction fbkHandlesLogin]
+ -[FBKOSLogViewController _configureSubtitleView]
+ -[NSDate(Utils) fbkIsEarlierThan:]
+ -[NSDictionary(StringToArrayValue) fbkTransformValueToArray]
+ -[NSMutableDictionary(FBKSnakeCaseKeys) fbkReplaceCamelCaseKeysWithSnakeCaseKeys]
+ -[NSString(FBKFile) fbkIsImageFile]
+ -[NSString(FBKFile) fbkIsImageFile].cold.1
+ -[NSString(FBKFile) fbkIsVideoFile]
+ -[NSString(FBKInstalledAppAdditions) fbkDirectoryCountFromRootPath:]
+ -[NSString(FBKUtils) fbkSnakeCaseString]
+ -[NSString(FBKUtils) fbkVisibleCharactersCount]
+ -[NSString(Truncation) fbk_objc_truncate:]
+ -[NSURL(FBKLaunchAction) fbkHandlesLogin]
+ -[UIButtonConfiguration(FBK) withFBKLargeButtonStyle]
+ -[UIButtonConfiguration(FBK) withFBKSemiBoldFont]
+ -[UIImage(PNGRotation) fbkCorrectlyRotatedPNGData]
+ -[UITableViewCell(InsetSeparator) fbk_objc_updateWithSeparatorSpacing:]
+ -[UITableViewController(FBKDocumentPresenter) fbkPresetAttachment:fromIndexPath:]
+ -[UITableViewController(FBKDocumentPresenter) fbkPresetAttachment:fromIndexPath:useRedesign:deleteHandler:]
+ -[UITableViewController(FBKDocumentPresenter) fbkPresetAttachment:fromIndexPath:useRedesign:deleteHandler:].cold.1
+ -[UITableViewController(FBKDocumentPresenter) fbkPresetAttachment:fromIndexPath:useRedesign:deleteHandler:].cold.2
+ -[UITableViewController(FBKDocumentPresenter) fbkPresetAttachmentWithImagePush:fromIndexPath:]
+ -[UITableViewController(FBKDocumentPresenter) fbkPresetAttachmentWithImagePush:fromIndexPath:].cold.1
+ -[UITableViewController(FBKDocumentPresenter) fbkPresetAttachmentWithImagePush:fromIndexPath:useRedesign:deleteHandler:]
+ -[UITableViewController(FBKDocumentPresenter) fbkPresetAttachmentWithImagePush:fromIndexPath:useRedesign:deleteHandler:].cold.1
+ -[UITextView(FBKCursorUtils) fbkCurrentCursorRect]
+ -[UITextView(FBKCursorUtils) fbkIsCursorIsAtEndOfDocument]
+ -[UITextView(FBKCursorUtils) fbkScrollTableToAvoidKeyboardInTableView:keyboardHeight:withPadding:]
+ -[UITextView(FBKCursorUtils) fbkScrollTableToAvoidKeyboardInTableView:keyboardHeight:withPadding:].cold.1
+ -[UITextView(FBKCursorUtils) fbkScrollTableToAvoidKeyboardInTableView:keyboardHeight:withPadding:].cold.2
+ -[UIView(FBKUtils) fbkSuperviewWithClass:]
+ -[UIViewController(PreferredAlertStyle) fbk_objc_preferredAlertStyle]
+ -[UIViewController(Spinner) addAccessiblityLabelToStackView:]
+ -[UIViewController(Spinner) fbkCreateNewFeedback:]
+ -[UIViewController(Spinner) fbkDidTapSubtitleAction:]
+ -[UIViewController(Spinner) fbkHideSpinner]
+ -[UIViewController(Spinner) fbkLeftToolbarItem]
+ -[UIViewController(Spinner) fbkNewFeedbackButtonState]
+ -[UIViewController(Spinner) fbkResumeSpinnerWithStatus:userInteractionEnabled:]
+ -[UIViewController(Spinner) fbkShowSpinnerWithStatus:userInteractionEnabled:]
+ -[UIViewController(Spinner) fbkShowSpinnerWithStatus:userInteractionEnabled:animated:]
+ -[UIViewController(Spinner) fbkShowToolbarWithStatus:animated:]
+ -[UIViewController(Spinner) fbkShowToolbarWithStatus:subtitle:animated:]
+ -[UIViewController(Spinner) fbkUpdateNewFeedbackButtonState]
+ ___43-[UIViewController(Spinner) fbkHideSpinner]_block_invoke
+ ___49-[UIButtonConfiguration(FBK) withFBKSemiBoldFont]_block_invoke
+ _objc_msgSend$_configureSubtitleView
+ _objc_msgSend$_fbkShowSpinnerWithStatus:userInteractionEnabled:
+ _objc_msgSend$accessibilityLabel
+ _objc_msgSend$addAccessiblityLabelToStackView:
+ _objc_msgSend$fbkCorrectlyRotatedPNGData
+ _objc_msgSend$fbkCurrentCursorRect
+ _objc_msgSend$fbkHideSpinner
+ _objc_msgSend$fbkIsEarlierThan:
+ _objc_msgSend$fbkIsImageFile
+ _objc_msgSend$fbkIsVideoFile
+ _objc_msgSend$fbkLeftToolbarItem
+ _objc_msgSend$fbkNewFeedbackButtonState
+ _objc_msgSend$fbkPresetAttachment:fromIndexPath:
+ _objc_msgSend$fbkPresetAttachment:fromIndexPath:useRedesign:deleteHandler:
+ _objc_msgSend$fbkPresetAttachmentWithImagePush:fromIndexPath:
+ _objc_msgSend$fbkReplaceCamelCaseKeysWithSnakeCaseKeys
+ _objc_msgSend$fbkScrollTableToAvoidKeyboardInTableView:keyboardHeight:withPadding:
+ _objc_msgSend$fbkShowSpinnerWithStatus:
+ _objc_msgSend$fbkShowSpinnerWithStatus:userInteractionEnabled:
+ _objc_msgSend$fbkShowSpinnerWithStatus:userInteractionEnabled:animated:
+ _objc_msgSend$fbkShowToolbarWithStatus:animated:
+ _objc_msgSend$fbkSnakeCaseString
+ _objc_msgSend$fbkSuperviewWithClass:
+ _objc_msgSend$fbkTransformValueToArray
+ _objc_msgSend$setLargeSubtitleView:
+ _objc_msgSend$setSubtitleView:
+ _objc_msgSend$withFBKLargeButtonStyle
+ _objc_msgSend$withFBKSemiBoldFont
- +[NSDate(Utils) dateWithYear:month:day:]
- +[NSDate(Utils) tomorrow]
- -[FBKBugFormTableViewController _showSpinnerWithStatus:userInteractionEnabled:]
- -[FBKBugFormTableViewController showSpinnerWithStatus:]
- -[FBKLaunchAction handlesLogin]
- -[NSDate(Utils) isEarlierThan:]
- -[NSDictionary(StringToArrayValue) transformValueToArray]
- -[NSMutableDictionary(FBKSnakeCaseKeys) replaceCamelCaseKeysWithSnakeCaseKeys]
- -[NSString(FBKFile) isImageFile]
- -[NSString(FBKFile) isImageFile].cold.1
- -[NSString(FBKFile) isVideoFile]
- -[NSString(FBKInstalledAppAdditions) directoryCountFromRootPath:]
- -[NSString(FBKUtils) snakeCaseString]
- -[NSString(FBKUtils) visibleCharactersCount]
- -[NSString(Truncation) objc_truncate:]
- -[NSURL(FBKLaunchAction) handlesLogin]
- -[UIButtonConfiguration(FBK) withLargeButtonStyle]
- -[UIButtonConfiguration(FBK) withSemiBoldFont]
- -[UIImage(PNGRotation) correctlyRotatedPNGData]
- -[UITableViewCell(InsetSeparator) objc_updateWithSeparatorSpacing:]
- -[UITableViewController(FBKDocumentPresenter) presentAttachment:fromIndexPath:]
- -[UITableViewController(FBKDocumentPresenter) presentAttachment:fromIndexPath:useRedesign:deleteHandler:]
- -[UITableViewController(FBKDocumentPresenter) presentAttachment:fromIndexPath:useRedesign:deleteHandler:].cold.1
- -[UITableViewController(FBKDocumentPresenter) presentAttachment:fromIndexPath:useRedesign:deleteHandler:].cold.2
- -[UITableViewController(FBKDocumentPresenter) presentAttachmentWithImagePush:fromIndexPath:]
- -[UITableViewController(FBKDocumentPresenter) presentAttachmentWithImagePush:fromIndexPath:].cold.1
- -[UITableViewController(FBKDocumentPresenter) presentAttachmentWithImagePush:fromIndexPath:useRedesign:deleteHandler:]
- -[UITableViewController(FBKDocumentPresenter) presentAttachmentWithImagePush:fromIndexPath:useRedesign:deleteHandler:].cold.1
- -[UITextView(FBKCursorUtils) currentCursorRect]
- -[UITextView(FBKCursorUtils) isCursorIsAtEndOfDocument]
- -[UITextView(FBKCursorUtils) scrollTableToAvoidKeyboardInTableView:keyboardHeight:withPadding:]
- -[UITextView(FBKCursorUtils) scrollTableToAvoidKeyboardInTableView:keyboardHeight:withPadding:].cold.1
- -[UITextView(FBKCursorUtils) scrollTableToAvoidKeyboardInTableView:keyboardHeight:withPadding:].cold.2
- -[UIView(FBKUtils) superviewWithClass:]
- -[UIViewController(PreferredAlertStyle) objc_preferredAlertStyle]
- -[UIViewController(Spinner) createNewFeedback:]
- -[UIViewController(Spinner) didTapSubtitleAction:]
- -[UIViewController(Spinner) hideSpinner]
- -[UIViewController(Spinner) leftToolbarItem]
- -[UIViewController(Spinner) newFeedbackButtonState]
- -[UIViewController(Spinner) resumeSpinnerWithStatus:userInteractionEnabled:]
- -[UIViewController(Spinner) showSpinnerWithStatus:userInteractionEnabled:]
- -[UIViewController(Spinner) showSpinnerWithStatus:userInteractionEnabled:animated:]
- -[UIViewController(Spinner) showToolbarWithStatus:animated:]
- -[UIViewController(Spinner) showToolbarWithStatus:subtitle:animated:]
- -[UIViewController(Spinner) updateNewFeedbackButtonState]
- ___40-[UIViewController(Spinner) hideSpinner]_block_invoke
- ___46-[UIButtonConfiguration(FBK) withSemiBoldFont]_block_invoke
- _objc_msgSend$_setLargeSubtitleView:
- _objc_msgSend$_setSubtitleView:
- _objc_msgSend$_showSpinnerWithStatus:userInteractionEnabled:
- _objc_msgSend$correctlyRotatedPNGData
- _objc_msgSend$currentCursorRect
- _objc_msgSend$hideSpinner
- _objc_msgSend$isEarlierThan:
- _objc_msgSend$isImageFile
- _objc_msgSend$isVideoFile
- _objc_msgSend$leftToolbarItem
- _objc_msgSend$newFeedbackButtonState
- _objc_msgSend$presentAttachment:fromIndexPath:
- _objc_msgSend$presentAttachment:fromIndexPath:useRedesign:deleteHandler:
- _objc_msgSend$presentAttachmentWithImagePush:fromIndexPath:
- _objc_msgSend$replaceCamelCaseKeysWithSnakeCaseKeys
- _objc_msgSend$scrollTableToAvoidKeyboardInTableView:keyboardHeight:withPadding:
- _objc_msgSend$showSpinnerWithStatus:
- _objc_msgSend$showSpinnerWithStatus:userInteractionEnabled:
- _objc_msgSend$showSpinnerWithStatus:userInteractionEnabled:animated:
- _objc_msgSend$showToolbarWithStatus:animated:
- _objc_msgSend$snakeCaseString
- _objc_msgSend$superviewWithClass:
- _objc_msgSend$transformValueToArray
- _objc_msgSend$withLargeButtonStyle
- _objc_msgSend$withSemiBoldFont
Functions:
~ -[FBKOSLogViewController viewDidLoad] : 456 -> 444
~ -[FBKOSLogViewController setLoading:] : 100 -> 116
+ -[FBKOSLogViewController _configureSubtitleView]
~ -[FBKOSLogViewController spinner] : 52 -> 16
~ -[FBKOSLogViewController setSpinner:] : 20 -> 12
~ -[FBKOSLogViewController .cxx_destruct] : 100 -> 104
~ -[UIViewController(Spinner) statusViewWithStatusString:subtitleButtonString:showsSpinner:isForLargeTitle:] : 416 -> 428
~ -[UIViewController(Spinner) statusLabelWithString:] : 200 -> 212
~ -[UIViewController(Spinner) subtitleLabelWithString:] : 180 -> 192
~ -[UIViewController(Spinner) titleAndSubtitleStackWithStatus:subtitleLabel:showsSpinner:isForLargeTitle:] : 852 -> 452
+ -[UIViewController(Spinner) addAccessiblityLabelToStackView:]
CStrings:
+ "B40@0:8@\"UISearchBar\"16@\"NSArray\"24@\"NSString\"32"
+ "T@\"UIActivityIndicatorView\",&,V_spinner"
+ "_configureSubtitleView"
+ "_fbkShowSpinnerWithStatus:userInteractionEnabled:"
+ "addAccessiblityLabelToStackView:"
+ "fbkCorrectlyRotatedPNGData"
+ "fbkCreateNewFeedback:"
+ "fbkCurrentCursorRect"
+ "fbkDateWithYear:month:day:"
+ "fbkDidTapSubtitleAction:"
+ "fbkDirectoryCountFromRootPath:"
+ "fbkHandlesLogin"
+ "fbkHideSpinner"
+ "fbkIsCursorIsAtEndOfDocument"
+ "fbkIsEarlierThan:"
+ "fbkIsImageFile"
+ "fbkIsVideoFile"
+ "fbkLeftToolbarItem"
+ "fbkNewFeedbackButtonState"
+ "fbkPresetAttachment:fromIndexPath:"
+ "fbkPresetAttachment:fromIndexPath:useRedesign:deleteHandler:"
+ "fbkPresetAttachmentWithImagePush:fromIndexPath:"
+ "fbkPresetAttachmentWithImagePush:fromIndexPath:useRedesign:deleteHandler:"
+ "fbkReplaceCamelCaseKeysWithSnakeCaseKeys"
+ "fbkResumeSpinnerWithStatus:userInteractionEnabled:"
+ "fbkScrollTableToAvoidKeyboardInTableView:keyboardHeight:withPadding:"
+ "fbkShowSpinnerWithStatus:"
+ "fbkShowSpinnerWithStatus:userInteractionEnabled:"
+ "fbkShowSpinnerWithStatus:userInteractionEnabled:animated:"
+ "fbkShowToolbarWithStatus:animated:"
+ "fbkShowToolbarWithStatus:subtitle:animated:"
+ "fbkSnakeCaseString"
+ "fbkSuperviewWithClass:"
+ "fbkTomorrow"
+ "fbkTransformValueToArray"
+ "fbkUpdateNewFeedbackButtonState"
+ "fbkVisibleCharactersCount"
+ "fbk_objc_preferredAlertStyle"
+ "fbk_objc_truncate:"
+ "fbk_objc_updateWithSeparatorSpacing:"
+ "searchBar:shouldChangeTextInRanges:replacementText:"
+ "setLargeSubtitleView:"
+ "setSubtitleView:"
+ "withFBKLargeButtonStyle"
+ "withFBKSemiBoldFont"
- "T@\"UIActivityIndicatorView\",W,V_spinner"
- "_setLargeSubtitleView:"
- "_setSubtitleView:"
- "_showSpinnerWithStatus:userInteractionEnabled:"
- "correctlyRotatedPNGData"
- "createNewFeedback:"
- "currentCursorRect"
- "dateWithYear:month:day:"
- "didTapSubtitleAction:"
- "directoryCountFromRootPath:"
- "handlesLogin"
- "hideSpinner"
- "isCursorIsAtEndOfDocument"
- "isEarlierThan:"
- "isImageFile"
- "isVideoFile"
- "leftToolbarItem"
- "newFeedbackButtonState"
- "objc_preferredAlertStyle"
- "objc_truncate:"
- "objc_updateWithSeparatorSpacing:"
- "presentAttachment:fromIndexPath:"
- "presentAttachment:fromIndexPath:useRedesign:deleteHandler:"
- "presentAttachmentWithImagePush:fromIndexPath:"
- "presentAttachmentWithImagePush:fromIndexPath:useRedesign:deleteHandler:"
- "replaceCamelCaseKeysWithSnakeCaseKeys"
- "resumeSpinnerWithStatus:userInteractionEnabled:"
- "scrollTableToAvoidKeyboardInTableView:keyboardHeight:withPadding:"
- "showSpinnerWithStatus:"
- "showSpinnerWithStatus:userInteractionEnabled:"
- "showSpinnerWithStatus:userInteractionEnabled:animated:"
- "showToolbarWithStatus:animated:"
- "showToolbarWithStatus:subtitle:animated:"
- "snakeCaseString"
- "superviewWithClass:"
- "tomorrow"
- "transformValueToArray"
- "updateNewFeedbackButtonState"
- "visibleCharactersCount"
- "withLargeButtonStyle"
- "withSemiBoldFont"

```
