## WelcomeKitUI

> `/System/Library/PrivateFrameworks/WelcomeKitUI.framework/WelcomeKitUI`

```diff

-1224.122.6.0.0
-  __TEXT.__text: 0x1506c
-  __TEXT.__auth_stubs: 0x500
+1410.0.0.0.0
+  __TEXT.__text: 0x14350
   __TEXT.__objc_methlist: 0x1ac4
   __TEXT.__const: 0x92
-  __TEXT.__cstring: 0x4dc0
+  __TEXT.__cstring: 0x4df0
   __TEXT.__gcc_except_tab: 0x2ac
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_typeref: 0x14
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x640
-  __TEXT.__objc_classname: 0x4ba
-  __TEXT.__objc_methname: 0x4813
-  __TEXT.__objc_methtype: 0x12fa
-  __TEXT.__objc_stubs: 0x3b40
-  __DATA_CONST.__got: 0x2a0
-  __DATA_CONST.__const: 0x580
+  __TEXT.__unwind_info: 0x600
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x588
   __DATA_CONST.__objc_classlist: 0x140
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x58

   __DATA_CONST.__objc_selrefs: 0x1458
   __DATA_CONST.__objc_superrefs: 0x108
   __DATA_CONST.__objc_arraydata: 0xb68
-  __AUTH_CONST.__auth_got: 0x290
+  __DATA_CONST.__got: 0x2a0
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x4c20
   __AUTH_CONST.__objc_const: 0x37f8
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x28
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xce0
   __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x234

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F45B3432-8BEE-3C10-9393-C565772E8B51
+  UUID: 58097B77-45BD-3B6F-B5D7-D7E1A6137906
   Functions: 494
-  Symbols:   2175
-  CStrings:  2283
+  Symbols:   2178
+  CStrings:  1251
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftCoreLocation_$_WelcomeKitUI
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x4
+ _objc_retain_x5
- _objc_retain_x26
- _objc_retain_x27
- _objc_retain_x28
Functions:
~ -[UIView(OnBoardingKit) wl_progressLabel] : 900 -> 908
~ -[WLAsset initWithName:remoteURL:] : 232 -> 224
~ -[WLAsset download] : 1100 -> 1060
~ -[WLCancellationViewController initWithWelcomeController:] : 636 -> 592
~ -[WLCancellationViewController viewWillAppear:] : 84 -> 88
~ -[WLCancellationViewController viewDidDisappear:] : 84 -> 88
~ -[WLCancellationViewController _continue] : 32 -> 36
~ -[WLCancellationViewController _retry] : 100 -> 108
~ -[WLCancellationViewController continueBlock] : 16 -> 20
~ -[WLCancellationViewController retryBlock] : 16 -> 20
~ -[WLCompletedViewCell initWithStyle:reuseIdentifier:] : 1900 -> 1748
~ -[WLCompletedViewCell setItem:] : 908 -> 848
~ -[WLCompletedViewCell customWarningAccessoryView] : 1004 -> 924
~ -[WLCompletedViewCell customErrorAccessoryView] : 1004 -> 924
~ -[WLCompletedViewCell customCheckmarkAccessoryView] : 416 -> 400
~ -[WLCompletedViewController initWithWelcomeController:context:imported:] : 988 -> 924
~ -[WLCompletedViewController viewDidLoad] : 348 -> 324
~ -[WLCompletedViewController _continueTapped:] : 32 -> 36
~ -[WLCompletedViewController tableView:numberOfRowsInSection:] : 16 -> 20
~ -[WLCompletedViewController tableView:cellForRowAtIndexPath:] : 172 -> 168
~ -[WLCompletedViewController tableView:didSelectRowAtIndexPath:] : 220 -> 216
~ -[WLCompletedViewController continueHandler] : 16 -> 20
~ -[WLDetailItem initWithType:count:secondaryText:alternativeTextUsed:symbolFilled:symbolTintColor:] : 944 -> 940
~ +[WLDetailItem contexts:] : 892 -> 816
~ +[WLDetailItem items:size:] : 1056 -> 1024
~ +[WLDetailItem items:] : 1752 -> 1668
~ +[WLDetailItem importDescriptionForType:import:total:] : 164 -> 156
~ -[WLDetailItem setSymbolTintColor:] : 64 -> 12
~ -[WLDetailViewController initWithContext:] : 1060 -> 984
~ -[WLDetailViewController viewDidLoad] : 196 -> 188
~ -[WLDetailViewController setCustomNavigationTitleView] : 1432 -> 1296
~ -[WLDetailViewController numberOfSectionsInTableView:] : 60 -> 68
~ -[WLDetailViewController tableView:numberOfRowsInSection:] : 88 -> 92
~ -[WLDetailViewController tableView:cellForRowAtIndexPath:] : 520 -> 480
~ -[WLDetailViewController tableView:titleForFooterInSection:] : 176 -> 172
~ -[WLDetailWarningViewController initWithWLDetailItem:] : 300 -> 280
~ -[WLFailureViewController initWithWelcomeController:context:] : 1116 -> 1024
~ -[WLFailureViewController _reset] : 32 -> 36
~ -[WLFailureViewController _detailTapped:] : 148 -> 152
~ -[WLFailureViewController resetBlock] : 16 -> 20
~ -[WLImportViewController initWithWelcomeController:] : 400 -> 372
~ -[WLInterfaceStyleAsset initWithLight:dark:] : 136 -> 140
~ -[WLInterfaceStyleAsset setLight:] : 64 -> 12
~ -[WLInterfaceStyleAsset setDark:] : 64 -> 12
~ -[WLOnboardingProgressViewController viewDidLoad] : 100 -> 96
~ -[WLOnboardingViewController viewDidLoad] : 100 -> 96
~ -[WLPairingCodeViewController initWithPairingCode:wifiPSK:ssid:welcomeController:] : 1584 -> 1468
~ -[WLPairingCodeViewController _appleInternalOptionsTapped:] : 216 -> 212
~ ___59-[WLPairingCodeViewController _appleInternalOptionsTapped:]_block_invoke_2 : 636 -> 628
~ -[WLPairingCodeViewController _setStashDataLocally:] : 152 -> 144
~ -[WLPairingCodeViewController _importLocalContent] : 132 -> 124
~ -[WLPairingCodeViewController showActivityIndicatorView] : 148 -> 144
~ -[WLPairingCodeViewController viewWillDisappear:] : 276 -> 260
~ -[WLPairingCodeViewController showCancelButton] : 16 -> 20
~ -[WLPairingCodeViewController setShowCancelButton:] : 16 -> 20
~ -[WLPairingCodeViewController viewWillDisappearBlock] : 16 -> 20
~ -[WLPairingCodeViewController getLocalImportOptionsHandler] : 16 -> 20
~ -[WLPairingCodeViewController stashDataLocallyHandler] : 16 -> 20
~ -[WLPairingCodeViewController importLocalContentHandler] : 16 -> 20
~ -[WLPairingCodeViewController cancellationBlock] : 16 -> 20
~ -[WLPairingCodeViewController viewWillDismissBlock] : 16 -> 20
~ -[WLPreparationViewController initWithWelcomeController:] : 228 -> 216
~ -[WLPreparationViewController viewDidLoad] : 200 -> 196
~ -[WLPreparationViewController showActivityIndicatorView] : 148 -> 144
~ -[WLPreparationViewController viewWillDisappear:] : 212 -> 204
~ -[WLPreparationViewController showCancelButton] : 16 -> 20
~ -[WLPreparationViewController setShowCancelButton:] : 16 -> 20
~ -[WLPreparationViewController cancellationBlock] : 16 -> 20
~ -[WLPreparationViewController viewWillDismissBlock] : 16 -> 20
~ -[WLProgressBar initWithFrame:] : 1316 -> 1220
~ -[WLProgressBar setProgress:] : 20 -> 24
~ -[WLProgressBar setProgressText:] : 16 -> 20
~ -[WLQRCode initWithName:title:URL:code:scale:] : 208 -> 220
~ -[WLQRCode createQRCodeImage:] : 328 -> 308
~ -[WLQRCodeDefaultViewController initWithDefaultQRCode:] : 592 -> 556
~ -[WLQRCodeDefaultViewController viewDidLoad] : 588 -> 556
~ -[WLQRCodeDefaultViewController viewWillDisappear:] : 100 -> 104
~ -[WLQRCodeDefaultViewController _listButtonTapped:] : 112 -> 116
~ -[WLQRCodeDefaultViewController requestCodes] : 144 -> 156
~ -[WLQRCodeDefaultViewController setIndicatorHidden:] : 152 -> 156
~ -[WLQRCodeDefaultViewController providerDidProvide:] : 96 -> 104
~ -[WLQRCodeDefaultViewController pushListViewController] : 216 -> 208
~ -[WLQRCodeDefaultViewController codes] : 16 -> 20
~ -[WLQRCodeDefaultViewController setCodes:] : 80 -> 20
~ -[WLQRCodeListViewController viewDidLoad] : 292 -> 272
~ -[WLQRCodeListViewController tableView:numberOfRowsInSection:] : 16 -> 20
~ -[WLQRCodeListViewController tableView:cellForRowAtIndexPath:] : 304 -> 288
~ -[WLQRCodeListViewController tableView:didSelectRowAtIndexPath:] : 456 -> 424
~ -[WLQRCodeListViewController qrcodes] : 16 -> 20
~ -[WLQRCodeListViewController setQrcodes:] : 80 -> 20
~ -[WLQRCodeProvider request] : 576 -> 556
~ -[WLQRCodeProvider drainQueue] : 180 -> 176
~ -[WLQRCodeProvider requestDidFinish:] : 612 -> 580
~ -[WLQRCodeViewController initQRCode] : 884 -> 812
~ -[WLQRCodeViewController qrcode] : 16 -> 20
~ -[WLQRCodeViewController setQrcode:] : 80 -> 20
~ +[WLRecord isInterrupted] : 120 -> 112
~ +[WLRecord startRecording] : 140 -> 132
~ +[WLRecord stopRecording] : 92 -> 88
~ -[WLRejectViewController initWithWelcomeController:] : 472 -> 452
~ -[WLRejectViewController viewWillAppear:] : 84 -> 88
~ -[WLRejectViewController viewDidDisappear:] : 84 -> 88
~ -[WLRejectViewController _retry] : 100 -> 108
~ -[WLRejectViewController retryBlock] : 16 -> 20
~ -[WLRequest request:redirect:] : 428 -> 408
~ ___30-[WLRequest request:redirect:]_block_invoke : 248 -> 268
~ -[WLRequest sessionDidFinish:response:error:redirect:] : 520 -> 504
~ -[WLRetryViewController initWithWelcomeController:] : 472 -> 452
~ -[WLRetryViewController viewWillAppear:] : 84 -> 88
~ -[WLRetryViewController viewDidDisappear:] : 84 -> 88
~ -[WLRetryViewController _retry:] : 100 -> 108
~ -[WLRetryViewController retryBlock] : 16 -> 20
~ +[WLTipAssetRemoteDocumentIdentifier documentIDs] : 60 -> 12
~ -[WLTips initWithTitle:desc:thumbnail:image:video:] : 216 -> 240
~ +[WLTips tips] : 2012 -> 1916
~ +[WLTips download] : 1068 -> 1012
~ -[WLTips setThumbnail:] : 64 -> 12
~ -[WLTips setImage:] : 64 -> 12
~ -[WLTips setVideo:] : 64 -> 12
~ -[WLTipsListViewController initWithItems] : 344 -> 328
~ -[WLTipsListViewController viewDidLoad] : 488 -> 456
~ -[WLTipsListViewController userInterfaceStyleDidChange] : 68 -> 64
~ -[WLTipsListViewController tableView:numberOfRowsInSection:] : 16 -> 20
~ -[WLTipsListViewController tableView:cellForRowAtIndexPath:] : 788 -> 708
~ -[WLTipsListViewController tableView:didSelectRowAtIndexPath:] : 212 -> 208
~ -[WLTipsVideoView initWithTips:] : 532 -> 520
~ -[WLTipsVideoView dealloc] : 104 -> 100
~ -[WLTipsVideoView setTipsImage] : 276 -> 248
~ -[WLTipsVideoView setTipsVideo] : 392 -> 360
~ -[WLTipsVideoView layoutSublayersOfLayer:] : 64 -> 68
~ -[WLTipsViewController viewDidLoad] : 3736 -> 3356
~ -[WLTipsViewController tips] : 16 -> 20
~ -[WLTipsViewController setTips:] : 80 -> 20
~ -[WLTransferCancellationViewController initWithWelcomeController:context:] : 1116 -> 1024
~ -[WLTransferCancellationViewController _reset] : 32 -> 36
~ -[WLTransferCancellationViewController _detailTapped:] : 148 -> 152
~ -[WLTransferCancellationViewController resetBlock] : 16 -> 20
~ -[WLTransferringViewController initWithSourceDevice:welcomeController:showsTips:] : 852 -> 808
~ -[WLTransferringViewController viewDidLoad] : 260 -> 256
~ -[WLTransferringViewController showActivityIndicatorView] : 148 -> 144
~ -[WLTransferringViewController viewWillDisappear:] : 220 -> 212
~ -[WLTransferringViewController setProgress:] : 112 -> 120
~ -[WLTransferringViewController setRemainingDownloadTime:] : 336 -> 344
~ -[WLTransferringViewController setCompletedOperationCount:totalOperationCount:] : 28 -> 36
~ -[WLTransferringViewController updateProgressText] : 488 -> 492
~ -[WLTransferringViewController _cancelRemainingDownloadTimeUpdateTimer] : 88 -> 92
~ -[WLTransferringViewController setIsImporting:] : 224 -> 220
~ -[WLTransferringViewController tipsButtonPressed:] : 124 -> 120
~ -[WLTransferringViewController addProgressBar] : 724 -> 680
~ -[WLTransferringViewController showCancelButton] : 16 -> 20
~ -[WLTransferringViewController setShowCancelButton:] : 16 -> 20
~ -[WLTransferringViewController isImporting] : 16 -> 20
~ -[WLTransferringViewController cancellationBlock] : 16 -> 20
~ -[WLTransferringViewController viewWillDismissBlock] : 16 -> 20
~ -[WLUIClient initWithHostname:brand:model:name:] : 192 -> 204
~ -[WLWaitingForDataTypeSelectionViewController initWithWelcomeController:] : 400 -> 372
~ -[WLWaitingForDataTypeSelectionViewController showActivityIndicatorView] : 148 -> 144
~ -[WLWaitingForDataTypeSelectionViewController viewWillDisappear:] : 212 -> 204
~ -[WLWaitingForDataTypeSelectionViewController showCancelButton] : 16 -> 20
~ -[WLWaitingForDataTypeSelectionViewController setShowCancelButton:] : 16 -> 20
~ -[WLWaitingForDataTypeSelectionViewController cancellationBlock] : 16 -> 20
~ -[WLWaitingForDataTypeSelectionViewController viewWillDismissBlock] : 16 -> 20
~ -[WLWelcomeController initWithWelcomeViewController:forceUITestMode:forceUITestModeDownloadError:] : 292 -> 288
~ -[WLWelcomeController _startPairing] : 456 -> 448
~ ___36-[WLWelcomeController _startPairing]_block_invoke : 352 -> 372
~ -[WLWelcomeController didDiscoverCandidate:] : 204 -> 196
~ ___64-[WLWelcomeController sourceDeviceController:didDiscoverDevice:]_block_invoke_2 : 156 -> 152
~ ___64-[WLWelcomeController sourceDeviceController:didDiscoverDevice:]_block_invoke_3 : 144 -> 140
~ -[WLWelcomeController _showPairingCode:wifiPSK:ssid:] : 1032 -> 1044
~ ___53-[WLWelcomeController _showPairingCode:wifiPSK:ssid:]_block_invoke_5 : 264 -> 260
~ -[WLWelcomeController _sourceDevicePairingPeriodDidEnd] : 200 -> 192
~ -[WLWelcomeController _setStashDataLocally:] : 164 -> 156
~ ___42-[WLWelcomeController _importLocalContent]_block_invoke : 192 -> 184
~ -[WLWelcomeController dataMigratorDidFinish:withImportErrors:context:] : 360 -> 364
~ ___70-[WLWelcomeController dataMigratorDidFinish:withImportErrors:context:]_block_invoke_3 : 420 -> 392
~ -[WLWelcomeController dataMigrator:didFailWithError:] : 200 -> 204
~ ___53-[WLWelcomeController dataMigrator:didFailWithError:]_block_invoke : 584 -> 548
~ -[WLWelcomeController dataMigrator:didUpdateMigrationState:] : 228 -> 224
~ ___64-[WLWelcomeController dataMigrator:didUpdateProgressPercentage:]_block_invoke : 132 -> 128
~ ___67-[WLWelcomeController dataMigrator:didUpdateRemainingDownloadTime:]_block_invoke : 128 -> 124
~ -[WLWelcomeController _didCompleteMigrationWithSuccess:retry:context:] : 396 -> 388
~ -[WLWelcomeController _updateTransferringForImport] : 120 -> 116
~ -[WLWelcomeController _completeWithSuccess:] : 264 -> 260
~ -[WLWelcomeController setNavigationController:] : 64 -> 12
~ -[WLWelcomeController _pushViewController:andRemovePreviousTopmostViewControllerWithCompletion:] : 596 -> 604
~ ___96-[WLWelcomeController _pushViewController:andRemovePreviousTopmostViewControllerWithCompletion:]_block_invoke : 156 -> 152
~ -[WLWelcomeController showCancellationAlert:] : 580 -> 548
~ -[WLWelcomeController setClient:brand:model:name:] : 220 -> 232
~ -[WLWelcomeController complete:] : 156 -> 152
~ -[WLWelcomeController change:context:] : 244 -> 232
~ -[WLWelcomeController daemon:didReceiveClient:brand:model:name:] : 284 -> 312
~ -[WLWelcomeController daemon:didImportWithContext:] : 192 -> 204
~ -[WLWelcomeController daemon:didChangeState:withContext:] : 208 -> 212
~ -[WLWelcomeController daemonDidGetInterrupted] : 124 -> 120
~ -[WLWelcomeController downloadTips] : 184 -> 180
~ -[WLWelcomeController downloadTipsInBackground] : 104 -> 100
~ -[WLWelcomeController setClient:] : 64 -> 12
~ -[WLWelcomeController setMigrationKitController:] : 64 -> 12
~ -[WLWelcomeViewController _initWithForceUITestMode:forceUITestModeDownloadError:] : 464 -> 444
~ -[WLWelcomeViewController viewDidLoad] : 188 -> 180
~ -[WLWelcomeViewController _qrcodeTapped:] : 288 -> 272
~ -[WLWelcomeViewController setCompletionHandler:] : 16 -> 20
~ -[WLWelcomeViewController completionHandler] : 16 -> 20
~ -[WLWelcomeViewController setResetHandler:] : 16 -> 20
~ -[WLWelcomeViewController resetHandler] : 16 -> 20
~ -[WLWelcomeViewController setOsMigrationHandler:] : 316 -> 308
~ -[WLWelcomeViewController _osMigrationButtonTapped:] : 104 -> 112
~ -[WLWelcomeViewController viewWillAppear:] : 84 -> 88
~ -[WLWelcomeViewController viewDidAppear:] : 168 -> 164
~ -[WLWelcomeViewController viewDidDisappear:] : 84 -> 88
~ -[WLWelcomeViewController osMigrationHandler] : 16 -> 20
~ -[WLWelcomeViewController continueHandler] : 16 -> 20
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<UIViewControllerAnimatedTransitioning>\"48@0:8@\"UINavigationController\"16q24@\"UIViewController\"32@\"UIViewController\"40"
- "@\"<UIViewControllerInteractiveTransitioning>\"32@0:8@\"UINavigationController\"16@\"<UIViewControllerAnimatedTransitioning>\"24"
- "@\"<WLQRCodeProviderDelegate>\""
- "@\"<WLRequestDelegate>\""
- "@\"AVPlayerLayer\""
- "@\"AVPlayerLooper\""
- "@\"AVQueuePlayer\""
- "@\"BFFNavigationController\""
- "@\"NSArray\""
- "@\"NSArray\"24@0:8@\"UITableView\"16"
- "@\"NSArray\"32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "@\"NSDateComponentsFormatter\""
- "@\"NSIndexPath\"24@0:8@\"UITableView\"16"
- "@\"NSIndexPath\"32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "@\"NSIndexPath\"40@0:8@\"UITableView\"16@\"NSIndexPath\"24@\"NSIndexPath\"32"
- "@\"NSMutableArray\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_source>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSString\"32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "@\"NSString\"32@0:8@\"UITableView\"16q24"
- "@\"OBLinkTrayButton\""
- "@\"OBTrayButton\""
- "@\"UIActivityIndicatorView\""
- "@\"UIColor\""
- "@\"UIContextMenuConfiguration\"48@0:8@\"UITableView\"16@\"NSIndexPath\"24{CGPoint=dd}32"
- "@\"UILabel\""
- "@\"UIProgressView\""
- "@\"UISwipeActionsConfiguration\"32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "@\"UITableViewCell\"32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "@\"UITargetedPreview\"32@0:8@\"UITableView\"16@\"UIContextMenuConfiguration\"24"
- "@\"UIView\""
- "@\"UIView\"24@0:8@\"UIScrollView\"16"
- "@\"UIView\"32@0:8@\"UITableView\"16q24"
- "@\"WLAsset\""
- "@\"WLContext\""
- "@\"WLDataMigrationController\""
- "@\"WLImportViewController\""
- "@\"WLInterfaceStyleAsset\""
- "@\"WLMigrationKitController\""
- "@\"WLProgressBar\""
- "@\"WLQRCode\""
- "@\"WLQRCodeProvider\""
- "@\"WLRequest\""
- "@\"WLSourceDevice\""
- "@\"WLSourceDevicesController\""
- "@\"WLTips\""
- "@\"WLTransferringViewController\""
- "@\"WLUIClient\""
- "@\"WLWelcomeController\""
- "@16@0:8"
- "@20@0:8B16"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8B16B20"
- "@24@0:8d16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16B24B28"
- "@32@0:8@16^Q24"
- "@32@0:8@16q24"
- "@32@0:8q16@24"
- "@36@0:8@16@24B32"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8q16Q24Q32"
- "@48@0:8@16@24@32@40"
- "@48@0:8@16@24{CGPoint=dd}32"
- "@48@0:8@16q24@32@40"
- "@48@0:8q16@24@32B40B44"
- "@48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "@56@0:8@16@24@32@40@48"
- "@56@0:8@16@24@32@40d48"
- "@56@0:8q16Q24@32B40B44@48"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@\"UIScrollView\"16"
- "B24@0:8@16"
- "B32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "B32@0:8@\"UITableView\"16@\"UITableViewFocusUpdateContext\"24"
- "B32@0:8@16@24"
- "B40@0:8@\"UITableView\"16@\"NSIndexPath\"24@\"<UISpringLoadedInteractionContext>\"32"
- "B40@0:8@16@24@32"
- "B48@0:8@\"UITableView\"16:24@\"NSIndexPath\"32@40"
- "B48@0:8@16:24@32@40"
- "BFFNavigationControllerDelegate"
- "Discoverability"
- "NSObject"
- "OBSetupAssistantSupport"
- "OnBoardingKit"
- "Q16@0:8"
- "Q24@0:8@\"UINavigationController\"16"
- "Q24@0:8@16"
- "Signals"
- "T#,R"
- "T@\"<WLQRCodeProviderDelegate>\",W,N,V_delegate"
- "T@\"<WLRequestDelegate>\",W,N,V_delegate"
- "T@\"NSArray\",&,N,V_codes"
- "T@\"NSArray\",&,N,V_qrcodes"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_brand"
- "T@\"NSString\",C,N,V_code"
- "T@\"NSString\",C,N,V_desc"
- "T@\"NSString\",C,N,V_detailText"
- "T@\"NSString\",C,N,V_hostname"
- "T@\"NSString\",C,N,V_localFile"
- "T@\"NSString\",C,N,V_model"
- "T@\"NSString\",C,N,V_name"
- "T@\"NSString\",C,N,V_remoteURL"
- "T@\"NSString\",C,N,V_secondaryText"
- "T@\"NSString\",C,N,V_symbol"
- "T@\"NSString\",C,N,V_text"
- "T@\"NSString\",C,N,V_title"
- "T@\"NSString\",C,N,V_url"
- "T@\"NSString\",R,C"
- "T@\"UIColor\",&,N,V_symbolTintColor"
- "T@\"WLAsset\",&,N,V_dark"
- "T@\"WLAsset\",&,N,V_light"
- "T@\"WLImportViewController\",W,N,V_importViewController"
- "T@\"WLInterfaceStyleAsset\",&,N,V_image"
- "T@\"WLInterfaceStyleAsset\",&,N,V_thumbnail"
- "T@\"WLInterfaceStyleAsset\",&,N,V_video"
- "T@\"WLMigrationKitController\",&,N,V_migrationKitController"
- "T@\"WLQRCode\",&,N,V_qrcode"
- "T@\"WLTips\",&,N,V_tips"
- "T@\"WLTransferringViewController\",W,N,V_transferringViewController"
- "T@\"WLUIClient\",&,N,V_client"
- "T@?,C,N"
- "T@?,C,N,V_cancellationBlock"
- "T@?,C,N,V_completionHandler"
- "T@?,C,N,V_continueBlock"
- "T@?,C,N,V_continueHandler"
- "T@?,C,N,V_getLocalImportOptionsHandler"
- "T@?,C,N,V_importLocalContentHandler"
- "T@?,C,N,V_osMigrationHandler"
- "T@?,C,N,V_resetBlock"
- "T@?,C,N,V_resetHandler"
- "T@?,C,N,V_retryBlock"
- "T@?,C,N,V_stashDataLocallyHandler"
- "T@?,C,N,V_viewWillDisappearBlock"
- "T@?,C,N,V_viewWillDismissBlock"
- "TB,N,V_enableDisplayZoom"
- "TB,N,V_failed"
- "TB,N,V_isImporting"
- "TB,N,V_showCancelButton"
- "TB,N,V_showDetailDisclosureButton"
- "TB,N,V_useGooglePlayStore"
- "TB,N,V_useMigrationKit"
- "TB,N,V_useMigrationKitInAP"
- "TQ,R"
- "UINavigationControllerDelegate"
- "UIScrollViewDelegate"
- "UITableViewDataSource"
- "UITableViewDelegate"
- "URLWithString:"
- "Vv16@0:8"
- "WLAsset"
- "WLCancellationViewController"
- "WLCompletedViewController"
- "WLDataMigrationDelegate"
- "WLDetailItem"
- "WLDetailViewController"
- "WLDetailWarningViewController"
- "WLDeviceCapability"
- "WLFailureViewController"
- "WLImportCancellationViewController"
- "WLImportViewController"
- "WLInterfaceStyleAsset"
- "WLOnboardingProgressViewController"
- "WLOnboardingViewController"
- "WLPairingCodeViewController"
- "WLPreparationViewController"
- "WLProgressBar"
- "WLQRCode"
- "WLQRCodeController"
- "WLQRCodeDefaultViewController"
- "WLQRCodeListViewController"
- "WLQRCodeProvider"
- "WLQRCodeProviderDelegate"
- "WLQRCodeViewController"
- "WLRecord"
- "WLRejectViewController"
- "WLRequestDelegate"
- "WLRetryViewController"
- "WLSettings"
- "WLSourceDevicesDelegate"
- "WLTipAssetRemoteDocumentIdentifier"
- "WLTips"
- "WLTipsListViewController"
- "WLTipsVideoView"
- "WLTipsViewController"
- "WLTransferCancellationViewController"
- "WLTransferringViewController"
- "WLUIClient"
- "WLWaitingForDataTypeSelectionViewController"
- "WLWelcomeController"
- "WLWelcomeViewController"
- "^{_NSZone=}16@0:8"
- "_TtC12WelcomeKitUI6Signal"
- "_accessoryView"
- "_appleInternalOptionsButton"
- "_appleInternalOptionsTapped:"
- "_attempts"
- "_brand"
- "_cancelRemainingDownloadTimeUpdateTimer"
- "_cancellationBlock"
- "_client"
- "_code"
- "_codes"
- "_completeWithSuccess:"
- "_completedOperationCount"
- "_completionHandler"
- "_configureWelcomeViewController:"
- "_context"
- "_continue"
- "_continueBlock"
- "_continueButton"
- "_continueHandler"
- "_continueTapped:"
- "_dark"
- "_data"
- "_delegate"
- "_desc"
- "_descriptionLabel"
- "_detailTapped:"
- "_detailText"
- "_didCompleteMigrationWithSuccess:retry:context:"
- "_didPairWithSourceDevice:"
- "_dismissAfterSourceDevicePairingTimeout"
- "_enableDisplayZoom"
- "_failed"
- "_forceUITestModeDownloadError"
- "_formatter"
- "_getLocalImportOptionsHandler"
- "_hasTips"
- "_hostname"
- "_image"
- "_importLocalContent"
- "_importLocalContentHandler"
- "_importProgressDescription"
- "_importViewController"
- "_indicatorView"
- "_initWithForceUITestMode:forceUITestModeDownloadError:"
- "_initialized"
- "_isImporting"
- "_isNothingImported"
- "_isPairingCanceled"
- "_items"
- "_label"
- "_light"
- "_listButtonTapped:"
- "_localFile"
- "_migrateUsingRetryPolicies"
- "_migrationConcluded"
- "_migrationController"
- "_migrationControllerDelegateQueueTargetedAtMainQueue"
- "_migrationControllerIsRestartable"
- "_migrationKitController"
- "_migrationState"
- "_model"
- "_name"
- "_osMigrationButton"
- "_osMigrationButtonTapped:"
- "_osMigrationHandler"
- "_player"
- "_playerLayer"
- "_playerLooper"
- "_progress"
- "_progressBar"
- "_progressView"
- "_provider"
- "_pushViewController:andRemovePreviousTopmostViewControllerWithCompletion:"
- "_qrcode"
- "_qrcodeLoaded"
- "_qrcodeTapped:"
- "_qrcodes"
- "_remainingDownloadTime"
- "_remainingDownloadTimeFormatter"
- "_remainingDownloadTimeUpdateTimer"
- "_remoteURL"
- "_request"
- "_reset"
- "_resetBlock"
- "_resetHandler"
- "_retry"
- "_retry:"
- "_retryBlock"
- "_retryButton"
- "_scale"
- "_secondaryText"
- "_setStashDataLocally:"
- "_showCancelButton"
- "_showCompleted:"
- "_showDetailDisclosureButton"
- "_showPairingCode:wifiPSK:ssid:"
- "_showPreparation:"
- "_showRetry"
- "_showTransferring"
- "_showWaitingForDataTypeSelection"
- "_size"
- "_sourceDevice"
- "_sourceDevicePairingPeriodDidEnd"
- "_sourceDevicesController"
- "_ssid"
- "_startMigration"
- "_startPairing"
- "_stashDataLocallyHandler"
- "_symbol"
- "_symbolTintColor"
- "_text"
- "_thumbnail"
- "_tips"
- "_title"
- "_titleLabel"
- "_totalOperationCount"
- "_transferProgressDescription"
- "_transferringViewController"
- "_uiTestMode"
- "_updateTransferringForImport"
- "_url"
- "_urls"
- "_useGooglePlayStore"
- "_useMigrationKit"
- "_useMigrationKitInAP"
- "_video"
- "_viewWillDisappearBlock"
- "_viewWillDismissBlock"
- "_welcomeController"
- "_wifiPSK"
- "accessibilitySetting"
- "account"
- "actionWithTitle:style:handler:"
- "activateConstraints:"
- "addAction:"
- "addAttribute:value:range:"
- "addButton:"
- "addObject:"
- "addObjectsFromArray:"
- "addObserver:selector:name:object:"
- "addProgressBar"
- "addSublayer:"
- "addSubview:"
- "addTarget:action:forControlEvents:"
- "addTopBorderWithColor:andWidth:"
- "album"
- "alertControllerWithTitle:message:preferredStyle:"
- "allHeaderFields"
- "appendString:"
- "application"
- "applicationWillEnterForeground"
- "arrayWithObjects:count:"
- "authenticate"
- "autorelease"
- "boldButton"
- "boldSystemFontOfSize:"
- "boolForKey:"
- "boolValue"
- "bottomAnchor"
- "bounds"
- "brand"
- "bundleForClass:"
- "buttonTray"
- "callHistory"
- "cancel"
- "cancellationBlock"
- "centerXAnchor"
- "centerYAnchor"
- "change:context:"
- "class"
- "clearColor"
- "client"
- "code"
- "codes"
- "complete"
- "complete:"
- "completionHandler"
- "configurationWithPointSize:"
- "conformsToProtocol:"
- "constraintEqualToAnchor:"
- "constraintEqualToAnchor:constant:"
- "constraintEqualToConstant:"
- "contact"
- "container"
- "containsObject:"
- "contentView"
- "contexts:"
- "continueBlock"
- "continueHandler"
- "controllerDidGetInterrupted"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "countryCode"
- "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
- "createQRCodeImage:"
- "currentDevice"
- "currentLocale"
- "customCheckmarkAccessoryView"
- "customErrorAccessoryView"
- "customWarningAccessoryView"
- "d"
- "d16@0:8"
- "d32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "d32@0:8@\"UITableView\"16q24"
- "d32@0:8@16@24"
- "d32@0:8@16q24"
- "daemon:didChangeState:withContext:"
- "daemon:didCreateCode:"
- "daemon:didImportWithContext:"
- "daemon:didReceiveClient:brand:model:name:"
- "daemon:didUpdateProgress:remainingTime:completedOperationCount:totalOperationCount:"
- "daemonDidAuthenticateClient:"
- "daemonDidGetInterrupted"
- "daemonDidRejectClient:"
- "daemonWillImport:"
- "dark"
- "dataMigrator:didFailWithError:"
- "dataMigrator:didUpdateMigrationState:"
- "dataMigrator:didUpdateProgressPercentage:"
- "dataMigrator:didUpdateRemainingDownloadTime:"
- "dataMigratorDidBecomeRestartable:"
- "dataMigratorDidFinish:withImportErrors:context:"
- "dataMigratorDidGetInterrupted"
- "dataTaskWithRequest:completionHandler:"
- "dataUsingEncoding:"
- "dealloc"
- "debugDescription"
- "defaultCenter"
- "defaultManager"
- "defaultSessionConfiguration"
- "delegate"
- "deleteMessages"
- "dequeueReusableCellWithIdentifier:"
- "dequeueReusableCellWithIdentifier:forIndexPath:"
- "desc"
- "description"
- "deselectRowAtIndexPath:animated:"
- "detailText"
- "deviceDidFailWithTimeout"
- "dictionaryWithObjects:forKeys:count:"
- "didDiscoverCandidate:"
- "didLoadAndroidStore:selected:canceled:inAttempts:"
- "didLoadQRCode:"
- "didStartWiFiAndDeviceDiscoveryWithCode:ssid:passphrase:started:"
- "directionalLayoutMargins"
- "disableLooping"
- "dismiss"
- "dismissViewControllerAnimated:completion:"
- "displaySetting"
- "documentIDs"
- "domain"
- "download"
- "downloadTaskWithRequest:completionHandler:"
- "downloadTips"
- "downloadTipsInBackground"
- "drainQueue"
- "enableDisplayZoom"
- "errorWithDomain:code:userInfo:"
- "extent"
- "failed"
- "file"
- "fileExistsAtPath:"
- "fileURLWithPath:"
- "filterWithName:"
- "firstObject"
- "frame"
- "getLocalImportOptionsHandler"
- "getLocalImportOptionsWithCompletion:"
- "hasActionButton"
- "hasDynamicIsland"
- "hasHomeButton"
- "hash"
- "headerView"
- "height"
- "heightAnchor"
- "hidesBusyIndicator"
- "hostname"
- "image"
- "imageByApplyingTransform:"
- "imageNamed:"
- "imageNamed:inBundle:"
- "imageProperties"
- "imageView"
- "imageWithCIImage:scale:orientation:"
- "import"
- "importCount"
- "importDescriptionForType:import:total:"
- "importErrorCount"
- "importLocalContent"
- "importLocalContentHandler"
- "importViewController"
- "indexPathForPreferredFocusedViewInTableView:"
- "init"
- "initForUITestWithForceDownloadError:"
- "initQRCode"
- "initWithActivityIndicatorStyle:"
- "initWithArrangedSubviews:"
- "initWithBarButtonSystemItem:target:action:"
- "initWithContentIdentifier:context:osBuild:userInfo:"
- "initWithContext:"
- "initWithCustomView:"
- "initWithDefaultQRCode:"
- "initWithDelegate:"
- "initWithDelegate:forceDownloadError:"
- "initWithFrame:"
- "initWithFrame:style:"
- "initWithHostname:brand:model:name:"
- "initWithImage:"
- "initWithImage:style:target:action:"
- "initWithItems"
- "initWithLight:dark:"
- "initWithName:remoteURL:"
- "initWithName:title:URL:code:scale:"
- "initWithObjects:"
- "initWithPairingCode:wifiPSK:ssid:welcomeController:"
- "initWithPlayerItem:"
- "initWithProgressViewStyle:"
- "initWithRootViewController:"
- "initWithScale:"
- "initWithSourceDevice:welcomeController:showsTips:"
- "initWithSpinnerText:"
- "initWithString:"
- "initWithStyle:reuseIdentifier:"
- "initWithTips:"
- "initWithTitle:desc:thumbnail:image:video:"
- "initWithTitle:detailText:icon:"
- "initWithTitle:detailText:icon:adoptTableViewScrollView:"
- "initWithTitle:detailText:icon:contentLayout:"
- "initWithTitle:detailText:symbolName:"
- "initWithTitle:detailText:symbolName:adoptTableViewScrollView:"
- "initWithType:count:secondaryText:alternativeTextUsed:symbolFilled:symbolTintColor:"
- "initWithType:secondaryText:detailText:showDetailDisclosureButton:failed:"
- "initWithURL:"
- "initWithWLDetailItem:"
- "initWithWelcomeController:"
- "initWithWelcomeController:context:"
- "initWithWelcomeController:context:imported:"
- "initWithWelcomeViewController:forceUITestMode:forceUITestModeDownloadError:"
- "initialize"
- "insertItem:afterItem:"
- "integerValue"
- "invalidateDaemonConnection"
- "isAnimating"
- "isBeingDismissed"
- "isEnabled"
- "isEqual:"
- "isEqualToString:"
- "isImporting"
- "isInternal"
- "isInterrupted"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isMovingFromParentViewController"
- "isProxy"
- "items:"
- "items:size:"
- "labelColor"
- "lastBaselineAnchor"
- "layer"
- "layoutSublayersOfLayer:"
- "leadingAnchor"
- "leftAnchor"
- "length"
- "light"
- "linkButton"
- "localFile"
- "localizedStringWithFormat:"
- "lookupAppDataContainer:"
- "migrationKitController"
- "model"
- "modelSpecificLocalizedStringKeyForKey:"
- "monospacedSystemFontOfSize:weight:"
- "moveItemAtURL:toURL:error:"
- "mutableCopy"
- "name"
- "navigationController"
- "navigationController:animationControllerForOperation:fromViewController:toViewController:"
- "navigationController:didShowViewController:animated:"
- "navigationController:didShowViewController:operation:animated:"
- "navigationController:interactionControllerForAnimationController:"
- "navigationController:willShowViewController:animated:"
- "navigationController:willShowViewController:operation:animated:"
- "navigationControllerPreferredInterfaceOrientationForPresentation:"
- "navigationControllerSupportedInterfaceOrientations:"
- "navigationItem"
- "numberOfSectionsInTableView:"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLongLong:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "order"
- "osMigrationHandler"
- "outputImage"
- "pause"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "placeholder"
- "plainButtonConfiguration"
- "play"
- "playerLayerWithPlayer:"
- "playerLooperWithPlayer:templateItem:"
- "popViewController"
- "popViewControllerAnimated:"
- "preferredFontForTextStyle:"
- "presentViewController:animated:completion:"
- "providerDidProvide:"
- "pushListViewController"
- "pushViewController:animated:"
- "pushViewController:completion:"
- "q24@0:8@\"UINavigationController\"16"
- "q24@0:8@\"UITableView\"16"
- "q24@0:8@16"
- "q32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "q32@0:8@\"UITableView\"16q24"
- "q32@0:8@16@24"
- "q32@0:8@16q24"
- "q40@0:8@\"UITableView\"16@\"NSString\"24q32"
- "q40@0:8@16@24q32"
- "qrcodes"
- "registerClass:forCellReuseIdentifier:"
- "registerForTraitChanges:withAction:"
- "reject"
- "release"
- "reloadData"
- "remoteURL"
- "removeAllItems"
- "removeButton:"
- "removeForKey:"
- "removeFromSuperview"
- "removeObjectAtIndex:"
- "removeObjectForKey:"
- "removeObjectsInArray:"
- "removeObserver:"
- "removeProgressBar"
- "request"
- "request:redirect:"
- "requestCodes"
- "requestDidFinish:"
- "requestWithURL:"
- "requestWithURL:cachePolicy:timeoutInterval:"
- "reset"
- "resetBlock"
- "resetHandler"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "retry"
- "retryBlock"
- "rightAnchor"
- "row"
- "run"
- "run:"
- "scale"
- "scheduleSurrogateDeviceDiscovery"
- "screen"
- "scrollViewDidChangeAdjustedContentInset:"
- "scrollViewDidEndDecelerating:"
- "scrollViewDidEndDragging:willDecelerate:"
- "scrollViewDidEndScrollingAnimation:"
- "scrollViewDidEndZooming:withView:atScale:"
- "scrollViewDidScroll:"
- "scrollViewDidScrollToTop:"
- "scrollViewDidZoom:"
- "scrollViewShouldScrollToTop:"
- "scrollViewWillBeginDecelerating:"
- "scrollViewWillBeginDragging:"
- "scrollViewWillBeginZooming:withView:"
- "scrollViewWillEndDragging:withVelocity:targetContentOffset:"
- "secondaryLabelColor"
- "secondarySystemBackgroundColor"
- "secondaryText"
- "secondaryTextProperties"
- "section"
- "sectionIndexTitlesForTableView:"
- "self"
- "send"
- "sendEvent:"
- "sessionDidFinish:response:error:redirect:"
- "sessionWithConfiguration:"
- "setAccessibilityIdentifier:"
- "setAccessoryType:"
- "setActive:"
- "setAlignment:"
- "setAllowedUnits:"
- "setAlwaysBounceVertical:"
- "setAttributedText:"
- "setAutoresizingMask:"
- "setAxis:"
- "setBackgroundColor:"
- "setBrand:"
- "setCancellationBlock:"
- "setClient:"
- "setClient:brand:model:name:"
- "setCode:"
- "setCodes:"
- "setCompletedOperationCount:totalOperationCount:"
- "setCompletionHandler:"
- "setConfiguration:"
- "setContentConfiguration:"
- "setContentMode:"
- "setContinueBlock:"
- "setContinueHandler:"
- "setCustomNavigationTitleView"
- "setDark:"
- "setDataSource:"
- "setDelegate:"
- "setDesc:"
- "setDetailText:"
- "setEnableDisplayZoom:"
- "setEnabled:"
- "setFailed:"
- "setFont:"
- "setFrame:"
- "setGetLocalImportOptionsHandler:"
- "setHTTPMaximumConnectionsPerHost:"
- "setHidden:"
- "setHidesBackButton:"
- "setHidesBackButton:animated:"
- "setHostname:"
- "setImage:"
- "setImagePadding:"
- "setImagePlacement:"
- "setImportLocalContentHandler:"
- "setImportViewController:"
- "setIncludesApproximationPhrase:"
- "setIndicatorHidden:"
- "setInterruptionHandler:"
- "setIsImporting:"
- "setItem:"
- "setLayoutMargins:"
- "setLayoutMarginsRelativeArrangement:"
- "setLeftBarButtonItem:"
- "setLight:"
- "setLineBreakMode:"
- "setLocalFile:"
- "setMaximumSize:"
- "setMigrationKitController:"
- "setModalPresentationStyle:"
- "setModel:"
- "setName:"
- "setNavigationController:"
- "setNumberOfLines:"
- "setNumberStyle:"
- "setObject:forKey:"
- "setOsMigrationHandler:"
- "setProgress:"
- "setProgressDescription:"
- "setProgressText:"
- "setQrcode:"
- "setQrcodes:"
- "setRemainingDownloadTime:"
- "setRemoteURL:"
- "setResetBlock:"
- "setResetHandler:"
- "setRetryBlock:"
- "setRightBarButtonItem:"
- "setSecondaryText:"
- "setShowCancelButton:"
- "setShowDetailDisclosureButton:"
- "setStashDataLocally:"
- "setStashDataLocallyHandler:"
- "setSymbol:"
- "setSymbolTintColor:"
- "setTLSMaximumSupportedProtocolVersion:"
- "setTLSMinimumSupportedProtocolVersion:"
- "setTableView:"
- "setText:"
- "setTextAlignment:"
- "setTextColor:"
- "setThumbnail:"
- "setTintColor:"
- "setTips:"
- "setTipsImage"
- "setTipsVideo"
- "setTitle:"
- "setTitle:forState:"
- "setTitleHyphenationFactor:"
- "setTitleView:"
- "setTransferringViewController:"
- "setTranslatesAutoresizingMaskIntoConstraints:"
- "setUnitsStyle:"
- "setUrl:"
- "setUseGooglePlayStore:"
- "setUseMigrationKit:"
- "setUseMigrationKitInAP:"
- "setUserInteractionEnabled:"
- "setValue:forKey:"
- "setVideo:"
- "setViewControllers:"
- "setViewWillDisappearBlock:"
- "setViewWillDismissBlock:"
- "setWithObjects:"
- "sharedInstance"
- "showActivityIndicatorView"
- "showCancelButton"
- "showCancellation:"
- "showCancellationAlert:"
- "showDetailDisclosureButton"
- "showFailure:"
- "showImport"
- "showReject"
- "showsBusyIndicator"
- "sim"
- "size"
- "sizeToFit"
- "source"
- "sourceDeviceController:didDiscoverCandidate:"
- "sourceDeviceController:didDiscoverDevice:"
- "standardUserDefaults"
- "startAnimating"
- "startMigrationUsingRetryPolicies:"
- "startRecording"
- "startWiFiAndDeviceDiscoveryWithCompletion:"
- "stashDataLocallyHandler"
- "statusCode"
- "stop"
- "stopAP"
- "stopAnimating"
- "stopDeviceDiscoveryWithCompletion:"
- "stopRecording"
- "stopWiFiAndDeviceDiscoveryWithCompletion:"
- "stringByAppendingFormat:"
- "stringByAppendingPathComponent:"
- "stringByAppendingString:"
- "stringByDeletingLastPathComponent"
- "stringFromByteCount:"
- "stringFromNumber:"
- "stringFromTimeInterval:"
- "stringWithFormat:"
- "subviews"
- "superclass"
- "symbol"
- "symbolTintColor"
- "synchronize"
- "systemBackgroundColor"
- "systemBlueColor"
- "systemFontOfSize:"
- "systemGray4Color"
- "systemGrayColor"
- "systemImageNamed:"
- "systemImageNamed:withConfiguration:"
- "systemLightGrayColor"
- "systemOrangeColor"
- "systemRedColor"
- "tableView"
- "tableView:accessoryButtonTappedForRowWithIndexPath:"
- "tableView:accessoryTypeForRowWithIndexPath:"
- "tableView:canEditRowAtIndexPath:"
- "tableView:canFocusRowAtIndexPath:"
- "tableView:canMoveRowAtIndexPath:"
- "tableView:canPerformAction:forRowAtIndexPath:withSender:"
- "tableView:canPerformPrimaryActionForRowAtIndexPath:"
- "tableView:cellForRowAtIndexPath:"
- "tableView:commitEditingStyle:forRowAtIndexPath:"
- "tableView:contextMenuConfigurationForRowAtIndexPath:point:"
- "tableView:didBeginMultipleSelectionInteractionAtIndexPath:"
- "tableView:didDeselectRowAtIndexPath:"
- "tableView:didEndDisplayingCell:forRowAtIndexPath:"
- "tableView:didEndDisplayingFooterView:forSection:"
- "tableView:didEndDisplayingHeaderView:forSection:"
- "tableView:didEndEditingRowAtIndexPath:"
- "tableView:didHighlightRowAtIndexPath:"
- "tableView:didSelectRowAtIndexPath:"
- "tableView:didUnhighlightRowAtIndexPath:"
- "tableView:didUpdateFocusInContext:withAnimationCoordinator:"
- "tableView:editActionsForRowAtIndexPath:"
- "tableView:editingStyleForRowAtIndexPath:"
- "tableView:estimatedHeightForFooterInSection:"
- "tableView:estimatedHeightForHeaderInSection:"
- "tableView:estimatedHeightForRowAtIndexPath:"
- "tableView:heightForFooterInSection:"
- "tableView:heightForHeaderInSection:"
- "tableView:heightForRowAtIndexPath:"
- "tableView:indentationLevelForRowAtIndexPath:"
- "tableView:leadingSwipeActionsConfigurationForRowAtIndexPath:"
- "tableView:moveRowAtIndexPath:toIndexPath:"
- "tableView:numberOfRowsInSection:"
- "tableView:performAction:forRowAtIndexPath:withSender:"
- "tableView:performPrimaryActionForRowAtIndexPath:"
- "tableView:previewForDismissingContextMenuWithConfiguration:"
- "tableView:previewForHighlightingContextMenuWithConfiguration:"
- "tableView:sectionForSectionIndexTitle:atIndex:"
- "tableView:selectionFollowsFocusForRowAtIndexPath:"
- "tableView:shouldBeginMultipleSelectionInteractionAtIndexPath:"
- "tableView:shouldHighlightRowAtIndexPath:"
- "tableView:shouldIndentWhileEditingRowAtIndexPath:"
- "tableView:shouldShowMenuForRowAtIndexPath:"
- "tableView:shouldSpringLoadRowAtIndexPath:withContext:"
- "tableView:shouldUpdateFocusInContext:"
- "tableView:targetIndexPathForMoveFromRowAtIndexPath:toProposedIndexPath:"
- "tableView:titleForDeleteConfirmationButtonForRowAtIndexPath:"
- "tableView:titleForFooterInSection:"
- "tableView:titleForHeaderInSection:"
- "tableView:trailingSwipeActionsConfigurationForRowAtIndexPath:"
- "tableView:viewForFooterInSection:"
- "tableView:viewForHeaderInSection:"
- "tableView:willBeginEditingRowAtIndexPath:"
- "tableView:willDeselectRowAtIndexPath:"
- "tableView:willDisplayCell:forRowAtIndexPath:"
- "tableView:willDisplayContextMenuWithConfiguration:animator:"
- "tableView:willDisplayFooterView:forSection:"
- "tableView:willDisplayHeaderView:forSection:"
- "tableView:willEndContextMenuInteractionWithConfiguration:animator:"
- "tableView:willPerformPreviewActionForMenuWithConfiguration:animator:"
- "tableView:willSelectRowAtIndexPath:"
- "tableViewDidEndMultipleSelectionInteraction:"
- "tertiaryLabelColor"
- "testAMSPurchase"
- "text"
- "textLabel"
- "textProperties"
- "thumbnail"
- "tipsButtonPressed:"
- "title"
- "titleLabel"
- "topAnchor"
- "trailingAnchor"
- "traitCollection"
- "transferringViewController"
- "transitionCoordinator"
- "updateProgress:remainingTime:completedOperationCount:totalOperationCount:"
- "updateProgressText"
- "uppercaseString"
- "url"
- "url:"
- "useGooglePlayStore"
- "useMigrationKit"
- "useMigrationKitInAP"
- "userInfo"
- "userInterfaceIdiom"
- "userInterfaceStyle"
- "userInterfaceStyleDidChange"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"<WLDataMigratorProtocol>\"16"
- "v24@0:8@\"NSArray\"16"
- "v24@0:8@\"UIScrollView\"16"
- "v24@0:8@\"UITableView\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8d16"
- "v28@0:8@\"<WLDataMigratorProtocol>\"16f24"
- "v28@0:8@\"UIScrollView\"16B24"
- "v28@0:8@16B24"
- "v28@0:8@16f24"
- "v32@0:8@\"<WLDataMigratorProtocol>\"16@\"NSError\"24"
- "v32@0:8@\"<WLDataMigratorProtocol>\"16@\"NSString\"24"
- "v32@0:8@\"<WLDataMigratorProtocol>\"16@\"WLContext\"24"
- "v32@0:8@\"<WLDataMigratorProtocol>\"16Q24"
- "v32@0:8@\"<WLDataMigratorProtocol>\"16d24"
- "v32@0:8@\"UIScrollView\"16@\"UIView\"24"
- "v32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "v32@0:8@\"WLSourceDevicesController\"16@\"WLSourceDevice\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16Q24"
- "v32@0:8@16d24"
- "v32@0:8B16B20@24"
- "v32@0:8Q16Q24"
- "v32@0:8q16@24"
- "v36@0:8@\"<WLDataMigratorProtocol>\"16B24@\"WLContext\"28"
- "v36@0:8@\"UINavigationController\"16@\"UIViewController\"24B32"
- "v36@0:8@16@24B32"
- "v36@0:8@16B24@28"
- "v40@0:8@\"<WLDataMigratorProtocol>\"16q24@\"WLContext\"32"
- "v40@0:8@\"UIScrollView\"16@\"UIView\"24d32"
- "v40@0:8@\"UITableView\"16@\"NSIndexPath\"24@\"NSIndexPath\"32"
- "v40@0:8@\"UITableView\"16@\"UIContextMenuConfiguration\"24@\"<UIContextMenuInteractionAnimating>\"32"
- "v40@0:8@\"UITableView\"16@\"UIContextMenuConfiguration\"24@\"<UIContextMenuInteractionCommitAnimating>\"32"
- "v40@0:8@\"UITableView\"16@\"UITableViewCell\"24@\"NSIndexPath\"32"
- "v40@0:8@\"UITableView\"16@\"UITableViewFocusUpdateContext\"24@\"UIFocusAnimationCoordinator\"32"
- "v40@0:8@\"UITableView\"16@\"UIView\"24q32"
- "v40@0:8@\"UITableView\"16q24@\"NSIndexPath\"32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24d32"
- "v40@0:8@16@24q32"
- "v40@0:8@16q24@32"
- "v44@0:8@\"BFFNavigationController\"16@\"UIViewController\"24q32B40"
- "v44@0:8@16@24@32B40"
- "v44@0:8@16@24q32B40"
- "v44@0:8f16Q20Q28Q36"
- "v48@0:8@\"UIScrollView\"16{CGPoint=dd}24N^{CGPoint=dd}40"
- "v48@0:8@\"UITableView\"16:24@\"NSIndexPath\"32@40"
- "v48@0:8@16:24@32@40"
- "v48@0:8@16@24@32@40"
- "v48@0:8@16{CGPoint=dd}24N^{CGPoint=dd}40"
- "v52@0:8@\"<WLDataMigratorProtocol>\"16f24Q28Q36Q44"
- "v52@0:8@16f24Q28Q36Q44"
- "v56@0:8@\"<WLDataMigratorProtocol>\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48"
- "v56@0:8@16@24@32@40@48"
- "valueCellConfiguration"
- "video"
- "view"
- "viewControllerForKey:"
- "viewControllers"
- "viewDidAppear:"
- "viewDidDisappear:"
- "viewDidLoad"
- "viewForZoomingInScrollView:"
- "viewWillAppear:"
- "viewWillDisappear:"
- "viewWillDisappearBlock"
- "viewWillDismissBlock"
- "voiceMemo"
- "widthAnchor"
- "wifiAndDeviceDiscoveryDidGetInterrupted"
- "window"
- "wl_progressLabel"
- "zone"

```
