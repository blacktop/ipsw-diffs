## TVRemoteUI

> `/System/Library/PrivateFrameworks/TVRemoteUI.framework/TVRemoteUI`

```diff

 548.10.24.0.0
-  __TEXT.__text: 0xcdacc
-  __TEXT.__auth_stubs: 0x1b30
-  __TEXT.__objc_methlist: 0xb3d0
-  __TEXT.__const: 0x2614
-  __TEXT.__gcc_except_tab: 0x1ec4
-  __TEXT.__cstring: 0x740a
-  __TEXT.__oslogstring: 0x5a02
+  __TEXT.__text: 0xd6b80
+  __TEXT.__auth_stubs: 0x1b40
+  __TEXT.__objc_methlist: 0xc050
+  __TEXT.__const: 0x2634
+  __TEXT.__gcc_except_tab: 0x20a8
+  __TEXT.__cstring: 0x76fa
+  __TEXT.__oslogstring: 0x5a22
   __TEXT.__ustring: 0x4a
   __TEXT.__dlopen_cstrs: 0x4e
   __TEXT.__constg_swiftt: 0x2dcc

   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0xc
-  __TEXT.__unwind_info: 0x2ac8
+  __TEXT.__unwind_info: 0x2d50
   __TEXT.__eh_frame: 0x878
-  __TEXT.__objc_classname: 0x144f
-  __TEXT.__objc_methname: 0x1b1bc
-  __TEXT.__objc_methtype: 0x44c7
-  __TEXT.__objc_stubs: 0x12fe0
-  __DATA_CONST.__got: 0xd38
-  __DATA_CONST.__const: 0x1950
-  __DATA_CONST.__objc_classlist: 0x5a0
+  __TEXT.__objc_classname: 0x15a7
+  __TEXT.__objc_methname: 0x1c95e
+  __TEXT.__objc_methtype: 0x477e
+  __TEXT.__objc_stubs: 0x14260
+  __DATA_CONST.__got: 0xd78
+  __DATA_CONST.__const: 0x1b28
+  __DATA_CONST.__objc_classlist: 0x5f0
   __DATA_CONST.__objc_catlist: 0x48
-  __DATA_CONST.__objc_protolist: 0x1f0
+  __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x67b0
+  __DATA_CONST.__objc_selrefs: 0x6cc0
   __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_superrefs: 0x3a8
-  __DATA_CONST.__objc_arraydata: 0xe8
-  __AUTH_CONST.__auth_got: 0xda8
-  __AUTH_CONST.__const: 0x2eb8
-  __AUTH_CONST.__cfstring: 0x3a00
-  __AUTH_CONST.__objc_const: 0x14a10
-  __AUTH_CONST.__objc_arrayobj: 0x240
-  __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__objc_intobj: 0xd8
+  __DATA_CONST.__objc_superrefs: 0x3f8
+  __DATA_CONST.__objc_arraydata: 0x110
+  __AUTH_CONST.__auth_got: 0xdb0
+  __AUTH_CONST.__const: 0x2f58
+  __AUTH_CONST.__cfstring: 0x3c80
+  __AUTH_CONST.__objc_const: 0x15fa8
+  __AUTH_CONST.__objc_arrayobj: 0x270
+  __AUTH_CONST.__objc_dictobj: 0x50
+  __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_doubleobj: 0x70
-  __AUTH.__objc_data: 0x6828
+  __AUTH.__objc_data: 0x6b48
   __AUTH.__data: 0x588
-  __DATA.__objc_ivar: 0xb44
-  __DATA.__data: 0x2538
-  __DATA.__bss: 0x2668
+  __DATA.__objc_ivar: 0xc54
+  __DATA.__data: 0x2658
+  __DATA.__bss: 0x2678
   __DATA.__common: 0x4c8
   __DATA_DIRTY.__objc_data: 0x7d0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E767997A-1B04-3BF4-9FA4-BA7332868712
-  Functions: 4701
-  Symbols:   17504
-  CStrings:  7205
+  UUID: 6D5E5432-AFAD-3E51-AFA6-BD2BF3223C59
+  Functions: 4987
+  Symbols:   18410
+  CStrings:  7529
 
Symbols:
+ +[_TVRUIAppInfoItem itemWithAppInfo:]
+ +[_TVRUIAppInfoItem unhideItem]
+ -[TVRUIAppLauncherStackViewController .cxx_destruct]
+ -[TVRUIAppLauncherStackViewController _appInfosDidUpdateNotification:]
+ -[TVRUIAppLauncherStackViewController _appInfosWillUpdateNotification:]
+ -[TVRUIAppLauncherStackViewController _canShowWhileLocked]
+ -[TVRUIAppLauncherStackViewController _confirmOkToOpenApp:withHandler:]
+ -[TVRUIAppLauncherStackViewController actionProvider]
+ -[TVRUIAppLauncherStackViewController collectionView:didSelectItemAtIndexPath:]
+ -[TVRUIAppLauncherStackViewController collectionViewLayout]
+ -[TVRUIAppLauncherStackViewController collectionView]
+ -[TVRUIAppLauncherStackViewController configureHierarchy]
+ -[TVRUIAppLauncherStackViewController dataSource]
+ -[TVRUIAppLauncherStackViewController dealloc]
+ -[TVRUIAppLauncherStackViewController eventHaptic]
+ -[TVRUIAppLauncherStackViewController hideApp:]
+ -[TVRUIAppLauncherStackViewController initWithNibName:bundle:]
+ -[TVRUIAppLauncherStackViewController isCurrentlyPlayingMedia]
+ -[TVRUIAppLauncherStackViewController launchApp:]
+ -[TVRUIAppLauncherStackViewController launchableAppsController]
+ -[TVRUIAppLauncherStackViewController loadingView]
+ -[TVRUIAppLauncherStackViewController nowPlayingProvider]
+ -[TVRUIAppLauncherStackViewController resetContent]
+ -[TVRUIAppLauncherStackViewController setActionProvider:]
+ -[TVRUIAppLauncherStackViewController setCollectionView:]
+ -[TVRUIAppLauncherStackViewController setDataSource:]
+ -[TVRUIAppLauncherStackViewController setEventHaptic:]
+ -[TVRUIAppLauncherStackViewController setLaunchableAppsController:]
+ -[TVRUIAppLauncherStackViewController setLoadingView:]
+ -[TVRUIAppLauncherStackViewController setNowPlayingProvider:]
+ -[TVRUIAppLauncherStackViewController setStyleProvider:]
+ -[TVRUIAppLauncherStackViewController styleProvider]
+ -[TVRUIAppLauncherStackViewController updateFromAppInfosAnimated:]
+ -[TVRUIAppLauncherStackViewController viewDidLoad]
+ -[TVRUIAppLauncherStackViewController viewWillAppear:]
+ -[TVRUIDockController .cxx_destruct]
+ -[TVRUIDockController actionProvider]
+ -[TVRUIDockController device]
+ -[TVRUIDockController dockViewController]
+ -[TVRUIDockController enabled]
+ -[TVRUIDockController hostingViewController]
+ -[TVRUIDockController hostingView]
+ -[TVRUIDockController initWithHostingViewController:actionProvider:upNextProvider:nowPlayingProvider:layoutHandler:]
+ -[TVRUIDockController launchableAppsController]
+ -[TVRUIDockController layoutHandler]
+ -[TVRUIDockController layoutManager]
+ -[TVRUIDockController nowPlayingProvider]
+ -[TVRUIDockController setActionProvider:]
+ -[TVRUIDockController setDevice:]
+ -[TVRUIDockController setEnabled:]
+ -[TVRUIDockController setHostingView:]
+ -[TVRUIDockController setLaunchableAppsController:]
+ -[TVRUIDockController setLayoutHandler:]
+ -[TVRUIDockController setLayoutManager:]
+ -[TVRUIDockController setNowPlayingProvider:]
+ -[TVRUIDockController setStyleProvider:]
+ -[TVRUIDockController setUpNextProvider:]
+ -[TVRUIDockController setViewController:]
+ -[TVRUIDockController styleProvider]
+ -[TVRUIDockController upNextProvider]
+ -[TVRUIDockController viewController]
+ -[TVRUIDockLayoutManager .cxx_destruct]
+ -[TVRUIDockLayoutManager _computeFrames]
+ -[TVRUIDockLayoutManager _configurePlacementDragRecognizer]
+ -[TVRUIDockLayoutManager _didPan:]
+ -[TVRUIDockLayoutManager _invokeLayoutHandlerIfNeeded]
+ -[TVRUIDockLayoutManager _placementForPosition:]
+ -[TVRUIDockLayoutManager controlPanelFrame]
+ -[TVRUIDockLayoutManager dockContainerView]
+ -[TVRUIDockLayoutManager dockHeight]
+ -[TVRUIDockLayoutManager dockHostingView]
+ -[TVRUIDockLayoutManager dockInfoProvider]
+ -[TVRUIDockLayoutManager effectiveControlPanelFrame]
+ -[TVRUIDockLayoutManager effectiveDockFrame]
+ -[TVRUIDockLayoutManager effectiveTouchpadFrame]
+ -[TVRUIDockLayoutManager initWithDockHostingView:dockInfoProvider:]
+ -[TVRUIDockLayoutManager isReordering]
+ -[TVRUIDockLayoutManager placement]
+ -[TVRUIDockLayoutManager reorderingStartPosition]
+ -[TVRUIDockLayoutManager setEffectiveControlPanelFrame:]
+ -[TVRUIDockLayoutManager setEffectiveDockFrame:]
+ -[TVRUIDockLayoutManager setEffectiveTouchpadFrame:]
+ -[TVRUIDockLayoutManager setIsReordering:]
+ -[TVRUIDockLayoutManager setPlacement:]
+ -[TVRUIDockLayoutManager setReorderingStartPosition:]
+ -[TVRUIDockLayoutManager touchpadFrame]
+ -[TVRUIDockLayoutManager updateWithTouchpadFrame:controlPanelFrame:placement:]
+ -[TVRUIDockPreferredStackController .cxx_destruct]
+ -[TVRUIDockPreferredStackController _initialStackKind]
+ -[TVRUIDockPreferredStackController _setupNotificationHandlers]
+ -[TVRUIDockPreferredStackController _teardownNotificationHandlers]
+ -[TVRUIDockPreferredStackController _updateInitialStackKind:]
+ -[TVRUIDockPreferredStackController currentStackIndex]
+ -[TVRUIDockPreferredStackController dealloc]
+ -[TVRUIDockPreferredStackController didBeginPlayingContent]
+ -[TVRUIDockPreferredStackController didChangeCurrentStackIndex:]
+ -[TVRUIDockPreferredStackController didContinueWatching]
+ -[TVRUIDockPreferredStackController didEndPlayingContent]
+ -[TVRUIDockPreferredStackController didLaunchApp]
+ -[TVRUIDockPreferredStackController init]
+ -[TVRUIDockPreferredStackController lastDidChangeDate]
+ -[TVRUIDockPreferredStackController notificationObservers]
+ -[TVRUIDockPreferredStackController preferredStackDidChangeHandler]
+ -[TVRUIDockPreferredStackController setCurrentStackIndex:]
+ -[TVRUIDockPreferredStackController setLastDidChangeDate:]
+ -[TVRUIDockPreferredStackController setPreferredStackDidChangeHandler:]
+ -[TVRUIDockViewController .cxx_destruct]
+ -[TVRUIDockViewController _canShowWhileLocked]
+ -[TVRUIDockViewController _invokeLayoutHandlerIfNeeded]
+ -[TVRUIDockViewController _nowPlayingInfoDidChange:]
+ -[TVRUIDockViewController _updateNowPlayingInfo:previousNowPlayingInfo:]
+ -[TVRUIDockViewController actionProvider]
+ -[TVRUIDockViewController appLauncherViewController]
+ -[TVRUIDockViewController buttonActionsDelegate]
+ -[TVRUIDockViewController castViewController]
+ -[TVRUIDockViewController configureHierarchy]
+ -[TVRUIDockViewController contentView]
+ -[TVRUIDockViewController dealloc]
+ -[TVRUIDockViewController dockContainerView]
+ -[TVRUIDockViewController dockIsCollapsed]
+ -[TVRUIDockViewController dockLayoutHandler]
+ -[TVRUIDockViewController dockPreferredHeight]
+ -[TVRUIDockViewController dockPreferredStackController]
+ -[TVRUIDockViewController enabled]
+ -[TVRUIDockViewController initWithNibName:bundle:]
+ -[TVRUIDockViewController launchableAppsController]
+ -[TVRUIDockViewController layoutHandler]
+ -[TVRUIDockViewController nowPlayingInfo]
+ -[TVRUIDockViewController nowPlayingProvider]
+ -[TVRUIDockViewController nowPlayingViewController]
+ -[TVRUIDockViewController preferredHeight]
+ -[TVRUIDockViewController resetContentAnimated:]
+ -[TVRUIDockViewController selectViewControllerIndex:animated:]
+ -[TVRUIDockViewController setActionProvider:]
+ -[TVRUIDockViewController setAppLauncherViewController:]
+ -[TVRUIDockViewController setButtonActionsDelegate:]
+ -[TVRUIDockViewController setCastViewController:]
+ -[TVRUIDockViewController setContentView:]
+ -[TVRUIDockViewController setDockPreferredStackController:]
+ -[TVRUIDockViewController setEnabled:]
+ -[TVRUIDockViewController setLaunchableAppsController:]
+ -[TVRUIDockViewController setLayoutHandler:]
+ -[TVRUIDockViewController setNowPlayingInfo:]
+ -[TVRUIDockViewController setNowPlayingProvider:]
+ -[TVRUIDockViewController setNowPlayingViewController:]
+ -[TVRUIDockViewController setStyleProvider:]
+ -[TVRUIDockViewController setUpNextProvider:]
+ -[TVRUIDockViewController setUpNextViewController:]
+ -[TVRUIDockViewController styleProvider]
+ -[TVRUIDockViewController upNextProvider]
+ -[TVRUIDockViewController upNextViewController]
+ -[TVRUIDockViewController viewDidAppear:]
+ -[TVRUIDockViewController viewDidLoad]
+ -[TVRUIDockViewController viewWillAppear:]
+ -[TVRUILaunchableAppsController .cxx_destruct]
+ -[TVRUILaunchableAppsController _adjustedAppInfosForAppInfos:]
+ -[TVRUILaunchableAppsController _baseMRUCountAdjustmentForAppInfo:]
+ -[TVRUILaunchableAppsController _fetchAppInfos]
+ -[TVRUILaunchableAppsController _loadHiddenBundleIDs]
+ -[TVRUILaunchableAppsController _loadMRUCountDict]
+ -[TVRUILaunchableAppsController _mruCountForBundleID:]
+ -[TVRUILaunchableAppsController _notifyOrderedAppInfosChanged]
+ -[TVRUILaunchableAppsController _persistHiddenBundleIDs:]
+ -[TVRUILaunchableAppsController _persistMRUCountDict:]
+ -[TVRUILaunchableAppsController _updateMRUCountForLaunchedAppWithBundleID:]
+ -[TVRUILaunchableAppsController _updatedMRUCountDictForCountDict:forBundleID:]
+ -[TVRUILaunchableAppsController activeDevice]
+ -[TVRUILaunchableAppsController appInfos]
+ -[TVRUILaunchableAppsController hasHiddenApps]
+ -[TVRUILaunchableAppsController hiddenBundleIDs]
+ -[TVRUILaunchableAppsController hideAppWithBundleID:]
+ -[TVRUILaunchableAppsController init]
+ -[TVRUILaunchableAppsController launchAppWithBundleID:]
+ -[TVRUILaunchableAppsController mruCountDict]
+ -[TVRUILaunchableAppsController orderedAppInfos]
+ -[TVRUILaunchableAppsController setAppInfos:]
+ -[TVRUILaunchableAppsController setDevice:]
+ -[TVRUILaunchableAppsController setHiddenBundleIDs:]
+ -[TVRUILaunchableAppsController setMruCountDict:]
+ -[TVRUILaunchableAppsController unhideApps]
+ -[TVRUIRemoteViewController _toggleDock]
+ -[TVRUIRemoteViewController dockController]
+ -[TVRUIRemoteViewController setDockController:]
+ -[TVRUIStackViewController .cxx_destruct]
+ -[TVRUIStackViewController _animateToFinalIndex:fromIndex:duration:]
+ -[TVRUIStackViewController _commitSelectedViewControllerIndex:]
+ -[TVRUIStackViewController _commitToFinalPositionForIndex:translation:velocity:]
+ -[TVRUIStackViewController _configureHierarchy]
+ -[TVRUIStackViewController _configurePanGesture]
+ -[TVRUIStackViewController _finalIndexForIndex:translation:velocity:]
+ -[TVRUIStackViewController _hostingViewAboveIndex:]
+ -[TVRUIStackViewController _hostingViewBelowIndex:]
+ -[TVRUIStackViewController _hostingViewForIndex:]
+ -[TVRUIStackViewController _hostingViewIndexIsValid:]
+ -[TVRUIStackViewController _indexAboveIndex:]
+ -[TVRUIStackViewController _indexBelowIndex:]
+ -[TVRUIStackViewController _indexForViewController:]
+ -[TVRUIStackViewController _isIndex:directlyAboveIndex:]
+ -[TVRUIStackViewController _isIndex:directlyBelowIndex:]
+ -[TVRUIStackViewController _multiplierForTranslation:]
+ -[TVRUIStackViewController _panRecognizerDidFire:]
+ -[TVRUIStackViewController _prepareHostingViewTransformsForIndex:]
+ -[TVRUIStackViewController _shouldCommitToFinalPositionForIndex:translation:]
+ -[TVRUIStackViewController _titleForHostingViewIndex:]
+ -[TVRUIStackViewController _transformWithMultiplier:]
+ -[TVRUIStackViewController _transitionToFinalIndex:duration:]
+ -[TVRUIStackViewController _updateHostingViewTransformsForIndex:translation:]
+ -[TVRUIStackViewController _updateViewControllerAppearanceForSelectedViewControllerIndex:]
+ -[TVRUIStackViewController containerView]
+ -[TVRUIStackViewController contentView]
+ -[TVRUIStackViewController hasNoTitle]
+ -[TVRUIStackViewController hostingViews]
+ -[TVRUIStackViewController initWithViewControllers:]
+ -[TVRUIStackViewController pageControl]
+ -[TVRUIStackViewController selectViewControllerIndex:animated:]
+ -[TVRUIStackViewController selectedViewControllerIndex]
+ -[TVRUIStackViewController setContainerView:]
+ -[TVRUIStackViewController setContentView:]
+ -[TVRUIStackViewController setHostingViews:]
+ -[TVRUIStackViewController setPageControl:]
+ -[TVRUIStackViewController setSelectedViewControllerIndex:]
+ -[TVRUIStackViewController setStackBackgroundColor:]
+ -[TVRUIStackViewController setTitleLabel:]
+ -[TVRUIStackViewController setTitleStyle:]
+ -[TVRUIStackViewController stackBackgroundColor]
+ -[TVRUIStackViewController titleLabel]
+ -[TVRUIStackViewController titleOnBottom]
+ -[TVRUIStackViewController titleOnTop]
+ -[TVRUIStackViewController titleStyle]
+ -[TVRUIStackViewController viewControllers]
+ -[TVRUIStackViewController viewDidLoad]
+ -[_TVRUIAppInfoCell .cxx_destruct]
+ -[_TVRUIAppInfoCell appInfo]
+ -[_TVRUIAppInfoCell configureHierarchy]
+ -[_TVRUIAppInfoCell delegate]
+ -[_TVRUIAppInfoCell imageView]
+ -[_TVRUIAppInfoCell initWithFrame:]
+ -[_TVRUIAppInfoCell prepareForReuse]
+ -[_TVRUIAppInfoCell setAppInfo:]
+ -[_TVRUIAppInfoCell setDelegate:]
+ -[_TVRUIAppInfoCell setImageView:]
+ -[_TVRUIAppInfoItem .cxx_destruct]
+ -[_TVRUIAppInfoItem appInfo]
+ -[_TVRUIAppInfoItem hash]
+ -[_TVRUIAppInfoItem initWithAppInfo:isUnhideItem:]
+ -[_TVRUIAppInfoItem isEqual:]
+ -[_TVRUIAppInfoItem isUnhideItem]
+ -[_TVRUIAppInfoUnhideItemsCell _configureHierarchy]
+ -[_TVRUIAppInfoUnhideItemsCell initWithFrame:]
+ GCC_except_table0
+ GCC_except_table120
+ GCC_except_table185
+ GCC_except_table22
+ GCC_except_table60
+ GCC_except_table67
+ _CGAffineTransformScale
+ _OBJC_CLASS_$_TVRCAppInfo
+ _OBJC_CLASS_$_TVRUIAppLauncherStackViewController
+ _OBJC_CLASS_$_TVRUIDockController
+ _OBJC_CLASS_$_TVRUIDockLayoutManager
+ _OBJC_CLASS_$_TVRUIDockPreferredStackController
+ _OBJC_CLASS_$_TVRUIDockViewController
+ _OBJC_CLASS_$_TVRUILaunchableAppsController
+ _OBJC_CLASS_$_TVRUIStackViewController
+ _OBJC_CLASS_$_UIPageControl
+ _OBJC_CLASS_$__TVRUIAppInfoCell
+ _OBJC_CLASS_$__TVRUIAppInfoItem
+ _OBJC_CLASS_$__TVRUIAppInfoUnhideItemsCell
+ _OBJC_IVAR_$_TVRUIAppLauncherStackViewController._actionProvider
+ _OBJC_IVAR_$_TVRUIAppLauncherStackViewController._collectionView
+ _OBJC_IVAR_$_TVRUIAppLauncherStackViewController._dataSource
+ _OBJC_IVAR_$_TVRUIAppLauncherStackViewController._eventHaptic
+ _OBJC_IVAR_$_TVRUIAppLauncherStackViewController._launchableAppsController
+ _OBJC_IVAR_$_TVRUIAppLauncherStackViewController._loadingView
+ _OBJC_IVAR_$_TVRUIAppLauncherStackViewController._nowPlayingProvider
+ _OBJC_IVAR_$_TVRUIAppLauncherStackViewController._styleProvider
+ _OBJC_IVAR_$_TVRUIDockController._actionProvider
+ _OBJC_IVAR_$_TVRUIDockController._device
+ _OBJC_IVAR_$_TVRUIDockController._hostingView
+ _OBJC_IVAR_$_TVRUIDockController._hostingViewController
+ _OBJC_IVAR_$_TVRUIDockController._launchableAppsController
+ _OBJC_IVAR_$_TVRUIDockController._layoutHandler
+ _OBJC_IVAR_$_TVRUIDockController._layoutManager
+ _OBJC_IVAR_$_TVRUIDockController._nowPlayingProvider
+ _OBJC_IVAR_$_TVRUIDockController._styleProvider
+ _OBJC_IVAR_$_TVRUIDockController._upNextProvider
+ _OBJC_IVAR_$_TVRUIDockController._viewController
+ _OBJC_IVAR_$_TVRUIDockController.enabled
+ _OBJC_IVAR_$_TVRUIDockLayoutManager._controlPanelFrame
+ _OBJC_IVAR_$_TVRUIDockLayoutManager._dockHostingView
+ _OBJC_IVAR_$_TVRUIDockLayoutManager._dockInfoProvider
+ _OBJC_IVAR_$_TVRUIDockLayoutManager._effectiveControlPanelFrame
+ _OBJC_IVAR_$_TVRUIDockLayoutManager._effectiveDockFrame
+ _OBJC_IVAR_$_TVRUIDockLayoutManager._effectiveTouchpadFrame
+ _OBJC_IVAR_$_TVRUIDockLayoutManager._isReordering
+ _OBJC_IVAR_$_TVRUIDockLayoutManager._placement
+ _OBJC_IVAR_$_TVRUIDockLayoutManager._reorderingStartPosition
+ _OBJC_IVAR_$_TVRUIDockLayoutManager._touchpadFrame
+ _OBJC_IVAR_$_TVRUIDockPreferredStackController._currentStackIndex
+ _OBJC_IVAR_$_TVRUIDockPreferredStackController._lastDidChangeDate
+ _OBJC_IVAR_$_TVRUIDockPreferredStackController._notificationObservers
+ _OBJC_IVAR_$_TVRUIDockPreferredStackController._preferredStackDidChangeHandler
+ _OBJC_IVAR_$_TVRUIDockViewController._actionProvider
+ _OBJC_IVAR_$_TVRUIDockViewController._appLauncherViewController
+ _OBJC_IVAR_$_TVRUIDockViewController._buttonActionsDelegate
+ _OBJC_IVAR_$_TVRUIDockViewController._castViewController
+ _OBJC_IVAR_$_TVRUIDockViewController._contentView
+ _OBJC_IVAR_$_TVRUIDockViewController._dockPreferredStackController
+ _OBJC_IVAR_$_TVRUIDockViewController._launchableAppsController
+ _OBJC_IVAR_$_TVRUIDockViewController._layoutHandler
+ _OBJC_IVAR_$_TVRUIDockViewController._nowPlayingInfo
+ _OBJC_IVAR_$_TVRUIDockViewController._nowPlayingProvider
+ _OBJC_IVAR_$_TVRUIDockViewController._nowPlayingViewController
+ _OBJC_IVAR_$_TVRUIDockViewController._styleProvider
+ _OBJC_IVAR_$_TVRUIDockViewController._upNextProvider
+ _OBJC_IVAR_$_TVRUIDockViewController._upNextViewController
+ _OBJC_IVAR_$_TVRUIDockViewController.enabled
+ _OBJC_IVAR_$_TVRUILaunchableAppsController._activeDevice
+ _OBJC_IVAR_$_TVRUILaunchableAppsController._appInfos
+ _OBJC_IVAR_$_TVRUILaunchableAppsController._hiddenBundleIDs
+ _OBJC_IVAR_$_TVRUILaunchableAppsController._mruCountDict
+ _OBJC_IVAR_$_TVRUIRemoteViewController._dockController
+ _OBJC_IVAR_$_TVRUIStackViewController._containerView
+ _OBJC_IVAR_$_TVRUIStackViewController._contentView
+ _OBJC_IVAR_$_TVRUIStackViewController._hostingViews
+ _OBJC_IVAR_$_TVRUIStackViewController._pageControl
+ _OBJC_IVAR_$_TVRUIStackViewController._selectedViewControllerIndex
+ _OBJC_IVAR_$_TVRUIStackViewController._stackBackgroundColor
+ _OBJC_IVAR_$_TVRUIStackViewController._titleLabel
+ _OBJC_IVAR_$_TVRUIStackViewController._titleStyle
+ _OBJC_IVAR_$_TVRUIStackViewController._viewControllers
+ _OBJC_IVAR_$__TVRUIAppInfoCell._appInfo
+ _OBJC_IVAR_$__TVRUIAppInfoCell._delegate
+ _OBJC_IVAR_$__TVRUIAppInfoCell._imageView
+ _OBJC_IVAR_$__TVRUIAppInfoItem._appInfo
+ _OBJC_IVAR_$__TVRUIAppInfoItem._isUnhideItem
+ _OBJC_METACLASS_$_TVRUIAppLauncherStackViewController
+ _OBJC_METACLASS_$_TVRUIDockController
+ _OBJC_METACLASS_$_TVRUIDockLayoutManager
+ _OBJC_METACLASS_$_TVRUIDockPreferredStackController
+ _OBJC_METACLASS_$_TVRUIDockViewController
+ _OBJC_METACLASS_$_TVRUILaunchableAppsController
+ _OBJC_METACLASS_$_TVRUIStackViewController
+ _OBJC_METACLASS_$__TVRUIAppInfoCell
+ _OBJC_METACLASS_$__TVRUIAppInfoItem
+ _OBJC_METACLASS_$__TVRUIAppInfoUnhideItemsCell
+ _TVRUILaunchableAppsControllerAppInfosDidChangeNotification
+ _TVRUILaunchableAppsControllerAppInfosDidLaunchAppNotification
+ _TVRUILaunchableAppsControllerAppInfosWillChangeNotification
+ __OBJC_$_CLASS_METHODS__TVRUIAppInfoItem
+ __OBJC_$_INSTANCE_METHODS_TVRUIAppLauncherStackViewController
+ __OBJC_$_INSTANCE_METHODS_TVRUIDockController
+ __OBJC_$_INSTANCE_METHODS_TVRUIDockLayoutManager
+ __OBJC_$_INSTANCE_METHODS_TVRUIDockPreferredStackController
+ __OBJC_$_INSTANCE_METHODS_TVRUIDockViewController
+ __OBJC_$_INSTANCE_METHODS_TVRUILaunchableAppsController
+ __OBJC_$_INSTANCE_METHODS_TVRUIStackViewController
+ __OBJC_$_INSTANCE_METHODS__TVRUIAppInfoCell
+ __OBJC_$_INSTANCE_METHODS__TVRUIAppInfoItem
+ __OBJC_$_INSTANCE_METHODS__TVRUIAppInfoUnhideItemsCell
+ __OBJC_$_INSTANCE_VARIABLES_TVRUIAppLauncherStackViewController
+ __OBJC_$_INSTANCE_VARIABLES_TVRUIDockController
+ __OBJC_$_INSTANCE_VARIABLES_TVRUIDockLayoutManager
+ __OBJC_$_INSTANCE_VARIABLES_TVRUIDockPreferredStackController
+ __OBJC_$_INSTANCE_VARIABLES_TVRUIDockViewController
+ __OBJC_$_INSTANCE_VARIABLES_TVRUILaunchableAppsController
+ __OBJC_$_INSTANCE_VARIABLES_TVRUIStackViewController
+ __OBJC_$_INSTANCE_VARIABLES__TVRUIAppInfoCell
+ __OBJC_$_INSTANCE_VARIABLES__TVRUIAppInfoItem
+ __OBJC_$_PROP_LIST_TVRUIAppInfosProviding
+ __OBJC_$_PROP_LIST_TVRUIAppLauncherStackViewController
+ __OBJC_$_PROP_LIST_TVRUIDockController
+ __OBJC_$_PROP_LIST_TVRUIDockInfoProviding
+ __OBJC_$_PROP_LIST_TVRUIDockLayoutManager
+ __OBJC_$_PROP_LIST_TVRUIDockPreferredStackController
+ __OBJC_$_PROP_LIST_TVRUIDockViewController
+ __OBJC_$_PROP_LIST_TVRUILaunchableAppsController
+ __OBJC_$_PROP_LIST_TVRUIStackViewController
+ __OBJC_$_PROP_LIST__TVRUIAppInfoCell
+ __OBJC_$_PROP_LIST__TVRUIAppInfoItem
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_TVRUIAppInfosProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_TVRUIDockInfoProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__TVRUIAppLaunchDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_TVRUIAppInfosProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_TVRUIDockInfoProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES__TVRUIAppLaunchDelegate
+ __OBJC_$_PROTOCOL_REFS_TVRUIAppInfosProviding
+ __OBJC_CLASS_PROTOCOLS_$_TVRUIAppLauncherStackViewController
+ __OBJC_CLASS_PROTOCOLS_$_TVRUIDockController
+ __OBJC_CLASS_PROTOCOLS_$_TVRUIDockViewController
+ __OBJC_CLASS_PROTOCOLS_$_TVRUILaunchableAppsController
+ __OBJC_CLASS_RO_$_TVRUIAppLauncherStackViewController
+ __OBJC_CLASS_RO_$_TVRUIDockController
+ __OBJC_CLASS_RO_$_TVRUIDockLayoutManager
+ __OBJC_CLASS_RO_$_TVRUIDockPreferredStackController
+ __OBJC_CLASS_RO_$_TVRUIDockViewController
+ __OBJC_CLASS_RO_$_TVRUILaunchableAppsController
+ __OBJC_CLASS_RO_$_TVRUIStackViewController
+ __OBJC_CLASS_RO_$__TVRUIAppInfoCell
+ __OBJC_CLASS_RO_$__TVRUIAppInfoItem
+ __OBJC_CLASS_RO_$__TVRUIAppInfoUnhideItemsCell
+ __OBJC_LABEL_PROTOCOL_$_TVRUIAppInfosProviding
+ __OBJC_LABEL_PROTOCOL_$_TVRUIDockInfoProviding
+ __OBJC_LABEL_PROTOCOL_$__TVRUIAppLaunchDelegate
+ __OBJC_METACLASS_RO_$_TVRUIAppLauncherStackViewController
+ __OBJC_METACLASS_RO_$_TVRUIDockController
+ __OBJC_METACLASS_RO_$_TVRUIDockLayoutManager
+ __OBJC_METACLASS_RO_$_TVRUIDockPreferredStackController
+ __OBJC_METACLASS_RO_$_TVRUIDockViewController
+ __OBJC_METACLASS_RO_$_TVRUILaunchableAppsController
+ __OBJC_METACLASS_RO_$_TVRUIStackViewController
+ __OBJC_METACLASS_RO_$__TVRUIAppInfoCell
+ __OBJC_METACLASS_RO_$__TVRUIAppInfoItem
+ __OBJC_METACLASS_RO_$__TVRUIAppInfoUnhideItemsCell
+ __OBJC_PROTOCOL_$_TVRUIAppInfosProviding
+ __OBJC_PROTOCOL_$_TVRUIDockInfoProviding
+ __OBJC_PROTOCOL_$__TVRUIAppLaunchDelegate
+ __TVRUIDockLog
+ __TVRUIDockLog.cold.1
+ __TVRUIDockLog.log
+ __TVRUIDockLog.onceToken
+ ___33-[TVRUIDockController setDevice:]_block_invoke
+ ___33-[TVRUIRemoteViewController init]_block_invoke
+ ___34-[TVRUIDockLayoutManager _didPan:]_block_invoke
+ ___34-[TVRUIDockLayoutManager _didPan:]_block_invoke_2
+ ___40-[TVRUIRemoteViewController _toggleDock]_block_invoke
+ ___41-[TVRUIDockPreferredStackController init]_block_invoke
+ ___45-[TVRUIDockViewController configureHierarchy]_block_invoke
+ ___45-[TVRUINowPlayingController actionButtonMenu]_block_invoke_6
+ ___45-[TVRUIRemoteViewController startConnections]_block_invoke.125
+ ___45-[TVRUIRemoteViewController startConnections]_block_invoke.132
+ ___46-[TVRUIRemoteViewController _showFindingAlert]_block_invoke.204
+ ___47-[TVRUILaunchableAppsController _fetchAppInfos]_block_invoke
+ ___47-[TVRUILaunchableAppsController _fetchAppInfos]_block_invoke_2
+ ___50-[TVRUIDockViewController initWithNibName:bundle:]_block_invoke
+ ___54-[TVRUIRemoteViewController setSupportsVolumeControl:]_block_invoke.206
+ ___55-[TVRUILaunchableAppsController launchAppWithBundleID:]_block_invoke
+ ___55-[TVRUILaunchableAppsController launchAppWithBundleID:]_block_invoke.cold.1
+ ___57-[TVRUIAppLauncherStackViewController configureHierarchy]_block_invoke
+ ___57-[TVRUIAppLauncherStackViewController configureHierarchy]_block_invoke_2
+ ___57-[TVRUIAppLauncherStackViewController configureHierarchy]_block_invoke_3
+ ___58-[TVRUIRemoteViewController _setupNetworkObserverIfNeeded]_block_invoke.177
+ ___59-[TVRUIAppLauncherStackViewController collectionViewLayout]_block_invoke
+ ___59-[TVRUIRemoteViewController _startFindingSessionForDevice:]_block_invoke.249
+ ___61-[TVRUIStackViewController _transitionToFinalIndex:duration:]_block_invoke
+ ___61-[TVRUIStackViewController _transitionToFinalIndex:duration:]_block_invoke_2
+ ___61-[TVRUIStackViewController _transitionToFinalIndex:duration:]_block_invoke_3
+ ___62-[TVRUILaunchableAppsController _adjustedAppInfosForAppInfos:]_block_invoke
+ ___63-[TVRUIDockPreferredStackController _setupNotificationHandlers]_block_invoke
+ ___63-[TVRUIDockPreferredStackController _setupNotificationHandlers]_block_invoke_2
+ ___63-[TVRUIDockPreferredStackController _setupNotificationHandlers]_block_invoke_3
+ ___63-[TVRUIDockPreferredStackController _setupNotificationHandlers]_block_invoke_4
+ ___68-[TVRUIStackViewController _animateToFinalIndex:fromIndex:duration:]_block_invoke
+ ___68-[TVRUIStackViewController _animateToFinalIndex:fromIndex:duration:]_block_invoke_2
+ ___71-[TVRUIAppLauncherStackViewController _confirmOkToOpenApp:withHandler:]_block_invoke
+ ___71-[TVRUIAppLauncherStackViewController _confirmOkToOpenApp:withHandler:]_block_invoke_2
+ ___72-[TVRUIDockViewController _updateNowPlayingInfo:previousNowPlayingInfo:]_block_invoke
+ ___79-[TVRUIAppLauncherStackViewController collectionView:didSelectItemAtIndexPath:]_block_invoke
+ ___79-[TVRUIAppLauncherStackViewController collectionView:didSelectItemAtIndexPath:]_block_invoke_2
+ ___79-[TVRUIAppLauncherStackViewController collectionView:didSelectItemAtIndexPath:]_block_invoke_3
+ ___79-[TVRUIAppLauncherStackViewController collectionView:didSelectItemAtIndexPath:]_block_invoke_4
+ ____TVRUIDockLog_block_invoke
+ ___block_descriptor_32_e37_q24?0"TVRCAppInfo"8"TVRCAppInfo"16l
+ ___block_descriptor_32_e76_v32?0"_TVRUIAppInfoUnhideItemsCell"8"NSIndexPath"16"_TVRUIAppInfoItem"24l
+ ___block_descriptor_40_e8_32w_e34_v24?0"NSDictionary"8"NSError"16lw32l8
+ ___block_descriptor_40_e8_32w_e65_v32?0"_TVRUIAppInfoCell"8"NSIndexPath"16"_TVRUIAppInfoItem"24lw32l8
+ ___block_descriptor_40_e8_32w_e8_v16?0Q8lw32l8
+ ___block_descriptor_48_e8_32s40s_e86_"UICollectionViewCell"32?0"UICollectionView"8"NSIndexPath"16"_TVRUIAppInfoItem"24ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e8_v12?0B8ls32l8
+ ___block_descriptor_50_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_56_e8_32s40bs_e8_v12?0B8ls40l8s32l8
+ ___block_descriptor_56_e8_32s_e8_v12?0B8ls32l8
+ ___block_descriptor_64_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_literal_global.134
+ ___block_literal_global.38
+ ___block_literal_global.52
+ ___block_literal_global.66
+ __panRecognizerDidFire:.__recognizerCommitted
+ _objc_msgSend$MRUCount
+ _objc_msgSend$_adjustedAppInfosForAppInfos:
+ _objc_msgSend$_animateToFinalIndex:fromIndex:duration:
+ _objc_msgSend$_baseMRUCountAdjustmentForAppInfo:
+ _objc_msgSend$_commitSelectedViewControllerIndex:
+ _objc_msgSend$_commitToFinalPositionForIndex:translation:velocity:
+ _objc_msgSend$_computeFrames
+ _objc_msgSend$_configurePanGesture
+ _objc_msgSend$_configurePlacementDragRecognizer
+ _objc_msgSend$_confirmOkToOpenApp:withHandler:
+ _objc_msgSend$_fetchAppInfos
+ _objc_msgSend$_finalIndexForIndex:translation:velocity:
+ _objc_msgSend$_hostingViewAboveIndex:
+ _objc_msgSend$_hostingViewBelowIndex:
+ _objc_msgSend$_hostingViewForIndex:
+ _objc_msgSend$_hostingViewIndexIsValid:
+ _objc_msgSend$_indexAboveIndex:
+ _objc_msgSend$_indexBelowIndex:
+ _objc_msgSend$_initialStackKind
+ _objc_msgSend$_invokeLayoutHandlerIfNeeded
+ _objc_msgSend$_isIndex:directlyAboveIndex:
+ _objc_msgSend$_loadHiddenBundleIDs
+ _objc_msgSend$_loadMRUCountDict
+ _objc_msgSend$_mruCountForBundleID:
+ _objc_msgSend$_multiplierForTranslation:
+ _objc_msgSend$_notifyOrderedAppInfosChanged
+ _objc_msgSend$_persistHiddenBundleIDs:
+ _objc_msgSend$_persistMRUCountDict:
+ _objc_msgSend$_placementForPosition:
+ _objc_msgSend$_prepareHostingViewTransformsForIndex:
+ _objc_msgSend$_setCanPanHorizontally:
+ _objc_msgSend$_setCanPanVertically:
+ _objc_msgSend$_setupNotificationHandlers
+ _objc_msgSend$_shouldCommitToFinalPositionForIndex:translation:
+ _objc_msgSend$_teardownNotificationHandlers
+ _objc_msgSend$_titleForHostingViewIndex:
+ _objc_msgSend$_toggleDock
+ _objc_msgSend$_toggleDockAppearance
+ _objc_msgSend$_transformWithMultiplier:
+ _objc_msgSend$_transitionToFinalIndex:duration:
+ _objc_msgSend$_updateHostingViewTransformsForIndex:translation:
+ _objc_msgSend$_updateInitialStackKind:
+ _objc_msgSend$_updateMRUCountForLaunchedAppWithBundleID:
+ _objc_msgSend$_updateNowPlayingInfo:previousNowPlayingInfo:
+ _objc_msgSend$_updateViewControllerAppearanceForSelectedViewControllerIndex:
+ _objc_msgSend$_updatedMRUCountDictForCountDict:forBundleID:
+ _objc_msgSend$addChildViewController:
+ _objc_msgSend$allKeys
+ _objc_msgSend$appGenre
+ _objc_msgSend$appInfo
+ _objc_msgSend$appInfoWithBundleID:dictionary:
+ _objc_msgSend$appInfoWithMRUCount:
+ _objc_msgSend$appInfos
+ _objc_msgSend$appLauncherViewController
+ _objc_msgSend$bundleID
+ _objc_msgSend$collectionViewLayout
+ _objc_msgSend$compare:
+ _objc_msgSend$controlPanelFrame
+ _objc_msgSend$currentStackIndex
+ _objc_msgSend$didBeginPlayingContent
+ _objc_msgSend$didChangeCurrentStackIndex:
+ _objc_msgSend$didContinueWatching
+ _objc_msgSend$didEndPlayingContent
+ _objc_msgSend$didLaunchApp
+ _objc_msgSend$didMoveToParentViewController:
+ _objc_msgSend$dockContainerView
+ _objc_msgSend$dockController
+ _objc_msgSend$dockHostingView
+ _objc_msgSend$dockInfoProvider
+ _objc_msgSend$dockIsCollapsed
+ _objc_msgSend$dockLayoutHandler
+ _objc_msgSend$dockPreferredHeight
+ _objc_msgSend$dockPreferredStackController
+ _objc_msgSend$dockViewController
+ _objc_msgSend$effectiveControlPanelFrame
+ _objc_msgSend$effectiveDockFrame
+ _objc_msgSend$effectiveTouchpadFrame
+ _objc_msgSend$hasHiddenApps
+ _objc_msgSend$hasNoTitle
+ _objc_msgSend$hiddenBundleIDs
+ _objc_msgSend$hideAppWithBundleID:
+ _objc_msgSend$hostingViews
+ _objc_msgSend$initWithAppInfo:isUnhideItem:
+ _objc_msgSend$initWithDockHostingView:dockInfoProvider:
+ _objc_msgSend$initWithHostingViewController:actionProvider:upNextProvider:nowPlayingProvider:layoutHandler:
+ _objc_msgSend$isEqualToNowPlayingMetadata:
+ _objc_msgSend$isReordering
+ _objc_msgSend$isTVApp
+ _objc_msgSend$isUnhideItem
+ _objc_msgSend$itemWithAppInfo:
+ _objc_msgSend$launchApp:
+ _objc_msgSend$launchAppWithBundleID:
+ _objc_msgSend$launchableAppsController
+ _objc_msgSend$layoutManager
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$localizedName
+ _objc_msgSend$mruCountDict
+ _objc_msgSend$notificationObservers
+ _objc_msgSend$orderedAppInfos
+ _objc_msgSend$pageControl
+ _objc_msgSend$placement
+ _objc_msgSend$preferredStackDidChangeHandler
+ _objc_msgSend$registerDefaults:
+ _objc_msgSend$reorderingStartPosition
+ _objc_msgSend$resetContent
+ _objc_msgSend$resetContentAnimated:
+ _objc_msgSend$selectViewControllerIndex:animated:
+ _objc_msgSend$selectedViewControllerIndex
+ _objc_msgSend$sendSubviewToBack:
+ _objc_msgSend$setAppInfo:
+ _objc_msgSend$setAppInfos:
+ _objc_msgSend$setAppLauncherViewController:
+ _objc_msgSend$setByAddingObject:
+ _objc_msgSend$setByAddingObjectsFromSet:
+ _objc_msgSend$setContainerView:
+ _objc_msgSend$setCurrentPage:
+ _objc_msgSend$setCurrentStackIndex:
+ _objc_msgSend$setDirection:
+ _objc_msgSend$setDockPreferredStackController:
+ _objc_msgSend$setEffectiveControlPanelFrame:
+ _objc_msgSend$setEffectiveDockFrame:
+ _objc_msgSend$setEffectiveTouchpadFrame:
+ _objc_msgSend$setHiddenBundleIDs:
+ _objc_msgSend$setHorizontalMode:
+ _objc_msgSend$setHostingViews:
+ _objc_msgSend$setIsReordering:
+ _objc_msgSend$setLastDidChangeDate:
+ _objc_msgSend$setLaunchableAppsController:
+ _objc_msgSend$setLoadingView:
+ _objc_msgSend$setMruCountDict:
+ _objc_msgSend$setNumberOfPages:
+ _objc_msgSend$setPageControl:
+ _objc_msgSend$setPlacement:
+ _objc_msgSend$setPreferredStackDidChangeHandler:
+ _objc_msgSend$setReorderingStartPosition:
+ _objc_msgSend$setSelectedViewControllerIndex:
+ _objc_msgSend$setStackBackgroundColor:
+ _objc_msgSend$sortUsingComparator:
+ _objc_msgSend$stackBackgroundColor
+ _objc_msgSend$titleOnTop
+ _objc_msgSend$titleStyle
+ _objc_msgSend$touchpadFrame
+ _objc_msgSend$unhideApps
+ _objc_msgSend$unhideItem
+ _objc_msgSend$updateFromAppInfosAnimated:
+ _objc_msgSend$updateWithTouchpadFrame:controlPanelFrame:placement:
+ _objc_msgSend$viewControllers
+ _objc_msgSend$willMoveToParentViewController:
- GCC_except_table117
- GCC_except_table182
- GCC_except_table29
- GCC_except_table35
- GCC_except_table57
- GCC_except_table64
- ___45-[TVRUIRemoteViewController startConnections]_block_invoke.124
- ___45-[TVRUIRemoteViewController startConnections]_block_invoke.131
- ___46-[TVRUIRemoteViewController _showFindingAlert]_block_invoke.203
- ___54-[TVRUIRemoteViewController setSupportsVolumeControl:]_block_invoke.205
- ___58-[TVRUIRemoteViewController _setupNetworkObserverIfNeeded]_block_invoke.176
- ___59-[TVRUIRemoteViewController _startFindingSessionForDevice:]_block_invoke.248
- ___block_literal_global.133
CStrings:
+ "\""
+ "@\"<TVRUIDockInfoProviding>\""
+ "@\"<_TVRUIAppLaunchDelegate>\""
+ "@\"NSDictionary\""
+ "@\"TVRCAppInfo\""
+ "@\"TVRUIAppLauncherStackViewController\""
+ "@\"TVRUIDockController\""
+ "@\"TVRUIDockLayoutManager\""
+ "@\"TVRUIDockPreferredStackController\""
+ "@\"TVRUIDockViewController\""
+ "@\"TVRUILaunchableAppsController\""
+ "@\"UICollectionViewCell\"32@?0@\"UICollectionView\"8@\"NSIndexPath\"16@\"_TVRUIAppInfoItem\"24"
+ "@\"UIPageControl\""
+ "@56@0:8@16@24@32@40@?48"
+ "@?<v@?>16@0:8"
+ "B24@0:8Q16"
+ "B32@0:8Q16Q24"
+ "B40@0:8Q16{CGPoint=dd}24"
+ "Dock"
+ "HiddenBundleIDs"
+ "Hide Dock"
+ "Internal Only"
+ "MRUCount"
+ "MRUCountDict"
+ "Q32@0:8{CGPoint=dd}16"
+ "Q56@0:8Q16{CGPoint=dd}24{CGPoint=dd}40"
+ "Show Dock"
+ "T@\"<TVRUIActionProviding>\",&,N,V_actionProvider"
+ "T@\"<TVRUIDevice>\",R,N,V_activeDevice"
+ "T@\"<TVRUIDockInfoProviding>\",R,N,V_dockInfoProvider"
+ "T@\"<TVRUINowPlayingProviding>\",&,N,V_nowPlayingProvider"
+ "T@\"<_TVRUIAppLaunchDelegate>\",W,N,V_delegate"
+ "T@\"NSArray\",&,N,V_appInfos"
+ "T@\"NSArray\",&,N,V_hostingViews"
+ "T@\"NSArray\",R,N,V_notificationObservers"
+ "T@\"NSArray\",R,N,V_viewControllers"
+ "T@\"NSDate\",&,N,V_lastDidChangeDate"
+ "T@\"NSDictionary\",&,N,V_mruCountDict"
+ "T@\"NSSet\",&,N"
+ "T@\"TVRCAppInfo\",&,N,V_appInfo"
+ "T@\"TVRCAppInfo\",R,N,V_appInfo"
+ "T@\"TVRUIAppLauncherStackViewController\",&,N,V_appLauncherViewController"
+ "T@\"TVRUIDockController\",&,N,V_dockController"
+ "T@\"TVRUIDockLayoutManager\",&,N,V_layoutManager"
+ "T@\"TVRUIDockPreferredStackController\",&,N,V_dockPreferredStackController"
+ "T@\"TVRUIDockViewController\",&,N,V_viewController"
+ "T@\"TVRUILaunchableAppsController\",&,N,V_launchableAppsController"
+ "T@\"TVRUILoadingView\",&,N,V_loadingView"
+ "T@\"TVRUINowPlayingMiniPlayerViewController\",&,N,V_nowPlayingViewController"
+ "T@\"UIColor\",&,N,V_stackBackgroundColor"
+ "T@\"UIPageControl\",&,N,V_pageControl"
+ "T@\"UIView\",&,N,V_containerView"
+ "T@\"UIView\",&,N,V_hostingView"
+ "T@\"UIView\",R,N,V_dockHostingView"
+ "T@\"UIViewController\",R,N"
+ "T@?,C,N,V_preferredStackDidChangeHandler"
+ "T@?,R,N"
+ "TB,N,V_isReordering"
+ "TB,N,Venabled"
+ "TB,R,N,V_isUnhideItem"
+ "TQ,N,V_currentStackIndex"
+ "TQ,N,V_placement"
+ "TQ,N,V_selectedViewControllerIndex"
+ "TQ,N,V_titleStyle"
+ "TVRUIAppInfosProviding"
+ "TVRUIAppLauncherStackViewController"
+ "TVRUIApps"
+ "TVRUIDockController"
+ "TVRUIDockInfoProviding"
+ "TVRUIDockLayoutManager"
+ "TVRUIDockPreferredStackController"
+ "TVRUIDockViewController"
+ "TVRUILaunchableAppsController"
+ "TVRUILaunchableAppsControllerAppInfosDidChangeNotification"
+ "TVRUILaunchableAppsControllerAppInfosDidLaunchAppNotification"
+ "TVRUILaunchableAppsControllerAppInfosWillChangeNotification"
+ "TVRUINoAppsFound"
+ "TVRUIOpenApp"
+ "TVRUIOpenTitle"
+ "TVRUIShortcutItemKindDock"
+ "TVRUIStackViewController"
+ "TVRUIUnhideApps"
+ "T{CGPoint=dd},N,V_reorderingStartPosition"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_effectiveControlPanelFrame"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_effectiveDockFrame"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_effectiveTouchpadFrame"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_controlPanelFrame"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_touchpadFrame"
+ "_TVRUIAppInfoCell"
+ "_TVRUIAppInfoItem"
+ "_TVRUIAppInfoUnhideItemsCell"
+ "_TVRUIAppLaunchDelegate"
+ "_adjustedAppInfosForAppInfos:"
+ "_animateToFinalIndex:fromIndex:duration:"
+ "_appInfo"
+ "_appInfos"
+ "_appInfosDidUpdateNotification:"
+ "_appInfosWillUpdateNotification:"
+ "_appLauncherViewController"
+ "_baseMRUCountAdjustmentForAppInfo:"
+ "_commitSelectedViewControllerIndex:"
+ "_commitToFinalPositionForIndex:translation:velocity:"
+ "_computeFrames"
+ "_configurePanGesture"
+ "_configurePlacementDragRecognizer"
+ "_confirmOkToOpenApp:withHandler:"
+ "_containerView"
+ "_controlPanelFrame"
+ "_currentStackIndex"
+ "_didPan:"
+ "_dockController"
+ "_dockHostingView"
+ "_dockInfoProvider"
+ "_dockPreferredStackController"
+ "_effectiveControlPanelFrame"
+ "_effectiveDockFrame"
+ "_effectiveTouchpadFrame"
+ "_fetchAppInfos"
+ "_finalIndexForIndex:translation:velocity:"
+ "_hiddenBundleIDs"
+ "_hostingView"
+ "_hostingViewAboveIndex:"
+ "_hostingViewBelowIndex:"
+ "_hostingViewForIndex:"
+ "_hostingViewIndexIsValid:"
+ "_hostingViews"
+ "_indexAboveIndex:"
+ "_indexBelowIndex:"
+ "_indexForViewController:"
+ "_initialStackKind"
+ "_invokeLayoutHandlerIfNeeded"
+ "_isIndex:directlyAboveIndex:"
+ "_isIndex:directlyBelowIndex:"
+ "_isReordering"
+ "_isUnhideItem"
+ "_lastDidChangeDate"
+ "_launchableAppsController"
+ "_layoutManager"
+ "_loadHiddenBundleIDs"
+ "_loadMRUCountDict"
+ "_mruCountDict"
+ "_mruCountForBundleID:"
+ "_multiplierForTranslation:"
+ "_notificationObservers"
+ "_notifyOrderedAppInfosChanged"
+ "_nowPlayingInfoDidChange:"
+ "_pageControl"
+ "_panRecognizerDidFire:"
+ "_persistHiddenBundleIDs:"
+ "_persistMRUCountDict:"
+ "_placement"
+ "_placementForPosition:"
+ "_preferredStackDidChangeHandler"
+ "_prepareHostingViewTransformsForIndex:"
+ "_reorderingStartPosition"
+ "_selectedViewControllerIndex"
+ "_setCanPanHorizontally:"
+ "_setCanPanVertically:"
+ "_setupNotificationHandlers"
+ "_shouldCommitToFinalPositionForIndex:translation:"
+ "_stackBackgroundColor"
+ "_teardownNotificationHandlers"
+ "_titleForHostingViewIndex:"
+ "_titleStyle"
+ "_toggleDock"
+ "_touchpadFrame"
+ "_transformWithMultiplier:"
+ "_transitionToFinalIndex:duration:"
+ "_updateHostingViewTransformsForIndex:translation:"
+ "_updateInitialStackKind:"
+ "_updateMRUCountForLaunchedAppWithBundleID:"
+ "_updateNowPlayingInfo:previousNowPlayingInfo:"
+ "_updateViewControllerAppearanceForSelectedViewControllerIndex:"
+ "_updatedMRUCountDictForCountDict:forBundleID:"
+ "_viewControllers"
+ "addChildViewController:"
+ "allKeys"
+ "appGenre"
+ "appInfo"
+ "appInfoWithBundleID:dictionary:"
+ "appInfoWithMRUCount:"
+ "appInfos"
+ "appLauncherViewController"
+ "bundleID"
+ "collectionViewLayout"
+ "com.apple.TVMovies"
+ "com.apple.TVShows"
+ "com.apple.tvos.remote.shortcut.dock"
+ "compare:"
+ "controlPanelFrame"
+ "currentStackIndex"
+ "d32@0:8{CGPoint=dd}16"
+ "didBeginPlayingContent"
+ "didChangeCurrentStackIndex:"
+ "didContinueWatching"
+ "didEndPlayingContent"
+ "didLaunchApp"
+ "didMoveToParentViewController:"
+ "dock.rectangle"
+ "dockContainerView"
+ "dockController"
+ "dockHeight"
+ "dockHostingView"
+ "dockInfoProvider"
+ "dockIsCollapsed"
+ "dockLayoutHandler"
+ "dockPreferredHeight"
+ "dockPreferredStackController"
+ "dockViewController"
+ "effectiveControlPanelFrame"
+ "effectiveDockFrame"
+ "effectiveTouchpadFrame"
+ "hasHiddenApps"
+ "hasNoTitle"
+ "hiddenBundleIDs"
+ "hideApp:"
+ "hideAppWithBundleID:"
+ "hostingView"
+ "hostingViews"
+ "initWithAppInfo:isUnhideItem:"
+ "initWithDockHostingView:dockInfoProvider:"
+ "initWithHostingViewController:actionProvider:upNextProvider:nowPlayingProvider:layoutHandler:"
+ "initWithViewControllers:"
+ "initialStackKind"
+ "isEqualToNowPlayingMetadata:"
+ "isReordering"
+ "isTVApp"
+ "isUnhideItem"
+ "itemWithAppInfo:"
+ "lastDidChangeDate"
+ "launchApp:"
+ "launchAppWithBundleID %@ failed: %@"
+ "launchAppWithBundleID:"
+ "launchableAppsController"
+ "layoutManager"
+ "localizedDescription"
+ "localizedName"
+ "main-section"
+ "mruCountDict"
+ "notificationObservers"
+ "orderedAppInfos"
+ "pageControl"
+ "placement"
+ "preferredStackDidChangeHandler"
+ "q24@?0@\"TVRCAppInfo\"8@\"TVRCAppInfo\"16"
+ "registerDefaults:"
+ "reorderingStartPosition"
+ "resetContentAnimated:"
+ "selectViewControllerIndex:animated:"
+ "selectedViewControllerIndex"
+ "sendSubviewToBack:"
+ "setAppInfo:"
+ "setAppInfos:"
+ "setAppLauncherViewController:"
+ "setByAddingObject:"
+ "setByAddingObjectsFromSet:"
+ "setContainerView:"
+ "setCurrentPage:"
+ "setCurrentStackIndex:"
+ "setDirection:"
+ "setDockController:"
+ "setDockPreferredStackController:"
+ "setEffectiveControlPanelFrame:"
+ "setEffectiveDockFrame:"
+ "setEffectiveTouchpadFrame:"
+ "setHiddenBundleIDs:"
+ "setHostingView:"
+ "setHostingViews:"
+ "setIsReordering:"
+ "setLastDidChangeDate:"
+ "setLaunchableAppsController:"
+ "setLayoutManager:"
+ "setLoadingView:"
+ "setMruCountDict:"
+ "setNumberOfPages:"
+ "setPageControl:"
+ "setPlacement:"
+ "setPreferredStackDidChangeHandler:"
+ "setReorderingStartPosition:"
+ "setSelectedViewControllerIndex:"
+ "setStackBackgroundColor:"
+ "setTitleStyle:"
+ "sortUsingComparator:"
+ "stackBackgroundColor"
+ "titleOnBottom"
+ "titleOnTop"
+ "titleStyle"
+ "touchpadFrame"
+ "unhideApps"
+ "unhideItem"
+ "updateFromAppInfosAnimated:"
+ "updateWithTouchpadFrame:controlPanelFrame:placement:"
+ "v16@?0Q8"
+ "v24@0:8@\"TVRCAppInfo\"16"
+ "v32@0:8Q16d24"
+ "v32@?0@\"_TVRUIAppInfoCell\"8@\"NSIndexPath\"16@\"_TVRUIAppInfoItem\"24"
+ "v32@?0@\"_TVRUIAppInfoUnhideItemsCell\"8@\"NSIndexPath\"16@\"_TVRUIAppInfoItem\"24"
+ "v40@0:8Q16Q24d32"
+ "v40@0:8Q16{CGPoint=dd}24"
+ "v56@0:8Q16{CGPoint=dd}24{CGPoint=dd}40"
+ "v88@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48Q80"
+ "viewControllers"
+ "willMoveToParentViewController:"
+ "{CGAffineTransform=dddddd}24@0:8d16"
+ "\xf0\xf0\x92"
- "%?\r!"
- "\xf0\xf0\x82"

```
