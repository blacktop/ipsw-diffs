## AccessibilityRemoteUIServices

> `/System/Library/PrivateFrameworks/AccessibilityRemoteUIServices.framework/AccessibilityRemoteUIServices`

```diff

-3191.7.24.0.0
-  __TEXT.__text: 0x4e50
-  __TEXT.__auth_stubs: 0x3f0
+3191.19.0.0.0
+  __TEXT.__text: 0x5490
+  __TEXT.__auth_stubs: 0x390
   __TEXT.__objc_methlist: 0xb04
   __TEXT.__const: 0x68
   __TEXT.__cstring: 0x4e5
   __TEXT.__gcc_except_tab: 0x54
-  __TEXT.__unwind_info: 0x1e8
+  __TEXT.__unwind_info: 0x220
   __TEXT.__objc_classname: 0x27a
   __TEXT.__objc_methname: 0x2793
   __TEXT.__objc_methtype: 0xe74

   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x208
+  __AUTH_CONST.__auth_got: 0x1d8
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x6a0
   __AUTH_CONST.__objc_const: 0xff8

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B02818E3-C056-3B71-B223-3A95E2CEE681
+  UUID: 61AA2CB4-EE59-36CA-B889-07BE23353CF3
   Functions: 142
-  Symbols:   813
+  Symbols:   807
   CStrings:  598
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x26
- _objc_retain_x3
- _objc_retain_x6
- _objc_retain_x8
Functions:
~ +[_AXRemoteNearbyDevicesViewController presentNearbyDevicesViewControllerWithConnectionHandler:dismissalHandler:] : 248 -> 240
~ ___113+[_AXRemoteNearbyDevicesViewController presentNearbyDevicesViewControllerWithConnectionHandler:dismissalHandler:]_block_invoke : 148 -> 144
~ -[_AXRemoteNearbyDevicesViewController viewServiceDidTerminateWithError:] : 152 -> 160
~ -[AXRVoiceOverTouchPadView _accessibilitySetCurrentGesture:] : 228 -> 244
~ -[AXRNearbyDevicesViewController viewDidLoad] : 240 -> 260
~ -[AXRNearbyDevicesViewController _connectToDevice:] : 224 -> 216
~ -[AXRNearbyDevicesViewController _showActiveDeviceConnectionAlertWithDevice:] : 228 -> 232
~ -[AXRNearbyDevicesViewController _dismissPresentedViewController] : 72 -> 76
~ -[AXRNearbyDevicesViewController _showFailedToConnectAlert] : 224 -> 240
~ -[AXRNearbyDevicesViewController deviceDiscoveryManager:updatedDevices:] : 88 -> 92
~ -[AXRNearbyDevicesViewController tableView:numberOfRowsInSection:] : 108 -> 116
~ -[AXRNearbyDevicesViewController tableView:cellForRowAtIndexPath:] : 444 -> 484
~ -[AXRNearbyDevicesViewController tableView:didSelectRowAtIndexPath:] : 224 -> 236
~ -[AXRNearbyDevicesViewController setDiscoveryManager:] : 20 -> 80
~ -[AXRNearbyDevicesViewController setDiscoveredDevices:] : 20 -> 80
~ -[AXRConnectedDeviceViewController initWithRemoteDevice:] : 140 -> 144
~ -[AXRConnectedDeviceViewController dealloc] : 156 -> 168
~ -[AXRConnectedDeviceViewController viewDidLoad] : 2564 -> 2852
~ ___47-[AXRConnectedDeviceViewController viewDidLoad]_block_invoke : 680 -> 700
~ ___47-[AXRConnectedDeviceViewController viewDidLoad]_block_invoke_3 : 760 -> 820
~ ___47-[AXRConnectedDeviceViewController viewDidLoad]_block_invoke_4 : 284 -> 300
~ -[AXRConnectedDeviceViewController viewWillAppear:] : 244 -> 264
~ -[AXRConnectedDeviceViewController _moreButtonPressed] : 244 -> 252
~ -[AXRConnectedDeviceViewController _dismissCurrentPresentedViewController] : 72 -> 76
~ -[AXRConnectedDeviceViewController _performDeviceRemoteAction:] : 208 -> 204
~ ___63-[AXRConnectedDeviceViewController _performDeviceRemoteAction:]_block_invoke : 220 -> 228
~ -[AXRConnectedDeviceViewController collectionView:didSelectItemAtIndexPath:] : 196 -> 216
~ -[AXRConnectedDeviceViewController collectionView:numberOfItemsInSection:] : 56 -> 60
~ -[AXRConnectedDeviceViewController collectionView:cellForItemAtIndexPath:] : 392 -> 432
~ ___74-[AXRConnectedDeviceViewController remoteDeviceDidUnexpectedlyDisconnect:]_block_invoke : 144 -> 156
~ -[AXRConnectedDeviceViewController voiceOverTouchPadView:didReceiveCommand:] : 160 -> 168
~ ___76-[AXRConnectedDeviceViewController voiceOverTouchPadView:didReceiveCommand:]_block_invoke : 244 -> 256
~ -[AXRConnectedDeviceViewController setActiveDevice:] : 20 -> 80
~ -[AXRConnectedDeviceViewController setEventProcessor:] : 20 -> 80
~ -[AXRConnectedDeviceViewController setActionsCollectionView:] : 20 -> 80
~ -[AXRConnectedDeviceViewController setCollectionViewFlowLayout:] : 20 -> 80
~ -[AXRActionCollectionViewCell initWithFrame:] : 720 -> 792
~ -[AXRActionCollectionViewCell layoutSubviews] : 140 -> 148
~ -[AXRActionCollectionViewCell setImage:title:] : 116 -> 120
~ _AXRUIImageForRemoteAction : 84 -> 88
~ _AXRUIImageForRemoteActionWithDeviceType : 1228 -> 1240
~ -[AXRDeviceActionsViewController initWithRemoteDevice:delegate:] : 140 -> 136
~ -[AXRDeviceActionsViewController viewDidLoad] : 120 -> 124
~ -[AXRDeviceActionsViewController _numberOfSections] : 92 -> 100
~ -[AXRDeviceActionsViewController _numberOfRowsInSection:] : 236 -> 264
~ -[AXRDeviceActionsViewController _titleForSection:] : 232 -> 260
~ -[AXRDeviceActionsViewController _footerForSection:] : 152 -> 164
~ -[AXRDeviceActionsViewController _actionForIndexPath:] : 264 -> 296
~ -[AXRDeviceActionsViewController _handGestureEventUsageForIndexPath:] : 144 -> 156
~ -[AXRDeviceActionsViewController _handleIndexPathSelection:] : 264 -> 284
~ -[AXRDeviceActionsViewController _titleForListItemAtIndexPath:] : 268 -> 296
~ -[AXRDeviceActionsViewController _subtitleForListItemAtIndexPath:] : 200 -> 220
~ -[AXRDeviceActionsViewController _imageForListItemAtIndexPath:] : 216 -> 240
~ -[AXRDeviceActionsViewController _leadingImageViewForListItemAtIndexPath:] : 100 -> 104
~ -[AXRDeviceActionsViewController tableView:cellForRowAtIndexPath:] : 300 -> 328
~ -[AXRDeviceActionsViewController tableView:didSelectRowAtIndexPath:] : 100 -> 104
~ -[AXRDeviceActionsViewController setActiveDevice:] : 20 -> 80
~ -[AXRemoteUIAlertCallbackHolder setRemoteAlertHandle:] : 12 -> 64
~ +[AXRemoteUIAlertManager sharedInstance] : 68 -> 84
~ -[AXRemoteUIAlertManager presentRemoteUIAlertWithIdentifier:viewControllerClassName:userInfo:presentationHandler:dismissalHandler:] : 800 -> 804
~ ___131-[AXRemoteUIAlertManager presentRemoteUIAlertWithIdentifier:viewControllerClassName:userInfo:presentationHandler:dismissalHandler:]_block_invoke : 396 -> 416
~ ___131-[AXRemoteUIAlertManager presentRemoteUIAlertWithIdentifier:viewControllerClassName:userInfo:presentationHandler:dismissalHandler:]_block_invoke_2 : 68 -> 72
~ -[AXRemoteUIAlertManager _sbs_presentRemoteUIAlertWithIdentifier:viewControllerClassName:userInfo:presentationHandler:dismissalHandler:] : 512 -> 508
~ -[AXRemoteUIAlertManager remoteAlertHandleDidActivate:] : 152 -> 156
~ ___55-[AXRemoteUIAlertManager remoteAlertHandleDidActivate:]_block_invoke : 156 -> 172
~ -[AXRemoteUIAlertManager remoteAlertHandleDidDeactivate:] : 152 -> 156
~ ___57-[AXRemoteUIAlertManager remoteAlertHandleDidDeactivate:]_block_invoke : 208 -> 228
~ -[AXRemoteUIAlertManager setRemoteCallbackHolders:] : 12 -> 64

```
