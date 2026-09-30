## SpringBoardUI

> `/System/Library/PrivateFrameworks/SpringBoardUI.framework/SpringBoardUI`

```diff

-4503.5.9.0.0
-  __TEXT.__text: 0x16fa0
-  __TEXT.__auth_stubs: 0x650
-  __TEXT.__objc_methlist: 0x3074
+4552.106.0.0.0
+  __TEXT.__text: 0x1784c
+  __TEXT.__auth_stubs: 0x680
+  __TEXT.__objc_methlist: 0x306c
   __TEXT.__const: 0x360
-  __TEXT.__cstring: 0x1bdb
+  __TEXT.__cstring: 0x1c64
   __TEXT.__oslogstring: 0x9c5
-  __TEXT.__gcc_except_tab: 0x124
-  __TEXT.__unwind_info: 0x8a0
-  __TEXT.__objc_classname: 0x803
-  __TEXT.__objc_methname: 0x8566
-  __TEXT.__objc_methtype: 0x156b
-  __TEXT.__objc_stubs: 0x5600
-  __DATA_CONST.__got: 0x3b8
-  __DATA_CONST.__const: 0xbe8
+  __TEXT.__gcc_except_tab: 0x138
+  __TEXT.__unwind_info: 0x8d0
+  __TEXT.__objc_classname: 0x804
+  __TEXT.__objc_methname: 0x850c
+  __TEXT.__objc_methtype: 0x14ef
+  __TEXT.__objc_stubs: 0x5740
+  __DATA_CONST.__got: 0x3d0
+  __DATA_CONST.__const: 0xc38
   __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_nlclslist: 0x8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x20f0
+  __DATA_CONST.__objc_selrefs: 0x2148
   __DATA_CONST.__objc_superrefs: 0xf8
-  __AUTH_CONST.__auth_got: 0x338
+  __AUTH_CONST.__auth_got: 0x350
   __AUTH_CONST.__const: 0x160
-  __AUTH_CONST.__cfstring: 0x23a0
+  __AUTH_CONST.__cfstring: 0x2460
   __AUTH_CONST.__objc_const: 0x7ec0
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x870
-  __DATA.__objc_ivar: 0x3a8
+  __DATA.__objc_ivar: 0x3ac
   __DATA.__data: 0x9c8
   __DATA.__bss: 0x98
   __DATA_DIRTY.__objc_data: 0x5f0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FCD63812-FCF4-337F-A154-2E3A01983041
-  Functions: 983
-  Symbols:   3800
-  CStrings:  2389
+  UUID: E7E35380-F1A9-34A0-9B02-84B6AB694E4E
+  Functions: 987
+  Symbols:   3828
+  CStrings:  2414
 
Symbols:
+ -[SBSceneHandle _didUpdateClientSettings:]
+ -[SBSceneHandle scene:didUpdateClientSettings:]
+ -[SBSceneHandle scene:didUpdateSettings:]
+ -[SBSceneHandle sceneDidInvalidate:withContext:]
+ -[SBSceneHandle sceneDidInvalidate:withContext:].cold.1
+ -[SBSceneHandle sceneManager:didAddScene:]
+ -[SBSceneHandleBlockObserver sceneHandle:didUpdateClientSettings:]
+ -[SBSceneView _addStateCaptureHandler]
+ -[SBSceneView _configureBackgroundColorWithLiveSnapshotPresentationContext:]
+ -[SBSceneView _configureSceneSnapshot:]
+ -[SBSceneView _presenterMayBeZombified]
+ -[SBSceneView _updateFlattenMode]
+ -[SBSceneView _updateFullyOccluded]
+ -[SBSceneView flattenMode]
+ -[SBSceneView fullyOccluded]
+ -[SBSceneView setFlattenMode:]
+ -[SBSceneView setFlattenMode:].cold.1
+ -[SBSceneView setFullyOccluded:]
+ -[SBSystemApertureSceneElementScenePresenterView _updateTraits]
+ -[_SBAlertController viewIsAppearing:]
+ -[_SBSceneHandleObserverBehavior didUpdateClientSettings]
+ -[_SBSceneHandleObserverBehavior setDidUpdateClientSettings:]
+ GCC_except_table18
+ GCC_except_table91
+ _BSLogAddStateCaptureBlockWithTitle
+ _OBJC_CLASS_$_CAWindowLayer
+ _OBJC_CLASS_$_FBSceneManager
+ _OBJC_IVAR_$_SBSceneHandle._hash
+ _OBJC_IVAR_$_SBSceneView._flattenMode
+ _OBJC_IVAR_$_SBSceneView._fullyOccluded
+ _OBJC_IVAR_$_SBSceneView._stateCaptureInvalidatable
+ _OBJC_IVAR_$__SBSceneHandleObserverBehavior._didUpdateClientSettings
+ _SBActionButtonPressedNotification
+ _SBFIsWindowFlatteningAvailable
+ _SBSUIUserNotificationContentCornerRadius
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_FBSceneManagerObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FBSceneManagerObserver
+ __OBJC_$_PROTOCOL_REFS_FBSceneManagerObserver
+ __OBJC_LABEL_PROTOCOL_$_FBSceneManagerObserver
+ __OBJC_PROTOCOL_$_FBSceneManagerObserver
+ __UISolariumEnabled
+ ___26-[SBSceneView description]_block_invoke
+ ___33-[SBSceneView _updateFlattenMode]_block_invoke
+ ___33-[SBSceneView _updateFlattenMode]_block_invoke_2
+ ___35-[SBSceneView _updateFullyOccluded]_block_invoke
+ ___35-[SBSceneView _updateFullyOccluded]_block_invoke_2
+ ___38-[SBSceneView _addStateCaptureHandler]_block_invoke
+ ___42-[SBSceneHandle _didUpdateClientSettings:]_block_invoke
+ ___63-[SBSystemApertureSceneElementScenePresenterView _updateTraits]_block_invoke
+ ___block_descriptor_40_e8_32s_e54_v16?0"UIMutableSceneWindowLayerPresentationContext"8ls32l8
+ ___block_descriptor_40_e8_32w_e5_8?0lw32l8
+ _kCAWindowLayerFlattenModeNever
+ _objc_msgSend$_addStateCaptureHandler
+ _objc_msgSend$_configureBackgroundColorWithLiveSnapshotPresentationContext:
+ _objc_msgSend$_didUpdateClientSettings:
+ _objc_msgSend$_headerContentViewController
+ _objc_msgSend$_presenterMayBeZombified
+ _objc_msgSend$_updateFlattenMode
+ _objc_msgSend$_updateFullyOccluded
+ _objc_msgSend$_updateTraits
+ _objc_msgSend$activeMultilinePrefix
+ _objc_msgSend$appendTimeInterval:withName:decomposeUnits:
+ _objc_msgSend$captureSnapshotPresentationView
+ _objc_msgSend$contentViewControllerLayoutGuide
+ _objc_msgSend$didUpdateClientSettings
+ _objc_msgSend$flattenMode
+ _objc_msgSend$fullyOccluded
+ _objc_msgSend$ignoreAnimations
+ _objc_msgSend$isHosting
+ _objc_msgSend$modifyWindowLayerPresentationContextWithBlock:
+ _objc_msgSend$newSnapshotPresentationView
+ _objc_msgSend$postCommitDuration
+ _objc_msgSend$presentationContext
+ _objc_msgSend$previousSettings
+ _objc_msgSend$sceneHandle:didUpdateClientSettings:
+ _objc_msgSend$sceneWithIdentifier:
+ _objc_msgSend$setFlattenMode:
+ _objc_msgSend$setFullyOccluded:
+ _objc_msgSend$setShouldSupportFlattening:
+ _objc_msgSend$settingsDiff
+ _objc_msgSend$zombifiesHostedContext
- -[SBSceneHandle _createMonitor]
- -[SBSceneHandle _didUpdateClientSettingsWithDiff:transitionContext:]
- -[SBSceneHandle _didUpdatePairingStatusForExternalSceneIdentifiers:]
- -[SBSceneHandle _initWithDefinition:scene:displayIdentity:].cold.2
- -[SBSceneHandle _sceneMonitor]
- -[SBSceneHandle _setSceneMonitor:]
- -[SBSceneHandle sceneMonitor:pairingStatusDidChangeForExternalSceneIDs:]
- -[SBSceneHandle sceneMonitor:sceneClientSettingsDidChangeWithDiff:transitionContext:]
- -[SBSceneHandle sceneMonitor:sceneSettingsDidChangeWithDiff:previousSettings:]
- -[SBSceneHandle sceneMonitor:sceneWasCreated:]
- -[SBSceneHandle sceneMonitor:sceneWasDestroyed:]
- -[SBSceneHandle sceneMonitor:sceneWasDestroyed:].cold.1
- -[SBSceneHandleBlockObserver observeDidUpdatePairingStatusForExternalIdentifiers:]
- -[SBSceneHandleBlockObserver sceneHandle:didUpdateClientSettingsWithDiff:transitionContext:]
- -[SBSceneHandleBlockObserver sceneHandle:didUpdatePairingStatusForExternalSceneIdentifiers:]
- -[SBSceneView _configureBackgroundColorForLiveSnapshot:]
- -[SBSceneView _configureSceneSnapshotContext:]
- -[SBSceneView newSnapshot]
- -[_SBSceneHandleObserverBehavior didUpdateClientSettingsWithDiff]
- -[_SBSceneHandleObserverBehavior didUpdatePairingStatusForExternalSceneIdentifiers]
- -[_SBSceneHandleObserverBehavior setDidUpdateClientSettingsWithDiff:]
- -[_SBSceneHandleObserverBehavior setDidUpdatePairingStatusForExternalSceneIdentifiers:]
- GCC_except_table16
- _OBJC_CLASS_$_FBSceneMonitor
- _OBJC_IVAR_$_SBSceneHandle._sceneMonitor
- _OBJC_IVAR_$_SBSceneHandleBlockObserver._didUpdatePairingStatusBlocks
- _OBJC_IVAR_$__SBSceneHandleObserverBehavior._didUpdateClientSettingsWithDiff
- _OBJC_IVAR_$__SBSceneHandleObserverBehavior._didUpdatePairingStatusForExternalSceneIdentifiers
- _SBRingerButtonDownNotification
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_FBSceneMonitorDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_FBSceneMonitorDelegate
- __OBJC_$_PROTOCOL_REFS_FBSceneMonitorDelegate
- __OBJC_LABEL_PROTOCOL_$_FBSceneMonitorDelegate
- __OBJC_PROTOCOL_$_FBSceneMonitorDelegate
- ___24-[SBSceneHandle dealloc]_block_invoke
- ___68-[SBSceneHandle _didUpdateClientSettingsWithDiff:transitionContext:]_block_invoke
- ___68-[SBSceneHandle _didUpdatePairingStatusForExternalSceneIdentifiers:]_block_invoke
- ___75-[SBSystemApertureSceneElementScenePresenterView traitCollectionDidChange:]_block_invoke
- _objc_msgSend$_configureBackgroundColorForLiveSnapshot:
- _objc_msgSend$_configureSceneSnapshotContext:
- _objc_msgSend$_createMonitor
- _objc_msgSend$_didUpdateClientSettingsWithDiff:transitionContext:
- _objc_msgSend$_didUpdatePairingStatusForExternalSceneIdentifiers:
- _objc_msgSend$appendSuper
- _objc_msgSend$createSnapshotWithContext:
- _objc_msgSend$defaultPresentationContext
- _objc_msgSend$didUpdateClientSettingsWithDiff
- _objc_msgSend$didUpdatePairingStatusForExternalSceneIdentifiers
- _objc_msgSend$initWithSceneID:
- _objc_msgSend$isPairedWithExternalSceneID:
- _objc_msgSend$newSnapshot
- _objc_msgSend$newSnapshotContext
- _objc_msgSend$scene
- _objc_msgSend$sceneHandle
- _objc_msgSend$sceneHandle:didUpdateClientSettingsWithDiff:transitionContext:
- _objc_msgSend$sceneHandle:didUpdatePairingStatusForExternalSceneIdentifiers:
- _objc_msgSend$snapshotPresentationForSnapshot:
CStrings:
+ "@\"<BSInvalidatable>\""
+ "@8@?0"
+ "FBSceneManagerObserver"
+ "SBActionButtonPressedNotification"
+ "SpringBoard - %@ - %p"
+ "T@\"NSString\",C,N,V_flattenMode"
+ "TB,N,V_didUpdateClientSettings"
+ "TB,N,V_fullyOccluded"
+ "_addStateCaptureHandler"
+ "_configureBackgroundColorWithLiveSnapshotPresentationContext:"
+ "_configureSceneSnapshot:"
+ "_didUpdateClientSettings"
+ "_didUpdateClientSettings:"
+ "_flattenMode"
+ "_fullyOccluded"
+ "_hash"
+ "_headerContentViewController"
+ "_presenterMayBeZombified"
+ "_stateCaptureInvalidatable"
+ "_updateFlattenMode"
+ "_updateFullyOccluded"
+ "_updateTraits"
+ "activeMultilinePrefix"
+ "appendTimeInterval:withName:decomposeUnits:"
+ "captureSnapshotPresentationView"
+ "contentViewControllerLayoutGuide"
+ "didUpdateClientSettings"
+ "flattenMode"
+ "fullyOccluded"
+ "ignoreAnimations"
+ "isHosting"
+ "modifyWindowLayerPresentationContextWithBlock:"
+ "newSnapshotPresentationView"
+ "postCommitDuration"
+ "presentationContext"
+ "previousSettings"
+ "sceneHandle:didUpdateClientSettings:"
+ "sceneManager:didAddScene:"
+ "sceneManager:didCommitUpdateForScene:transactionID:"
+ "sceneManager:didDestroyScene:"
+ "sceneManager:willCommitUpdateForScene:transactionID:"
+ "sceneManager:willRemoveScene:"
+ "sceneManager:willUpdateScene:withSettings:transitionContext:"
+ "sceneWithIdentifier:"
+ "setDidUpdateClientSettings:"
+ "setFlattenMode:"
+ "setFullyOccluded:"
+ "setShouldSupportFlattening:"
+ "settingsDiff"
+ "v16@?0@\"UIMutableSceneWindowLayerPresentationContext\"8"
+ "v32@0:8@\"FBSceneManager\"16@\"FBScene\"24"
+ "v32@0:8@\"SBSceneHandle\"16@\"FBSSceneUpdate\"24"
+ "v40@0:8@\"FBSceneManager\"16@\"FBScene\"24Q32"
+ "v40@0:8@16@24Q32"
+ "v48@0:8@\"FBSceneManager\"16@\"FBScene\"24@\"FBSSceneSettings\"32@\"FBSSceneTransitionContext\"40"
+ "viewIsAppearing:"
+ "window layer"
+ "zombifiesHostedContext"
+ "\xf0\xa1"
- "@\"FBSceneMonitor\""
- "FBSceneMonitorDelegate"
- "Given scene and monitor'd scene do not match."
- "SBRingerButtonDownNotification"
- "T@\"FBSceneMonitor\",&,N,G_sceneMonitor,S_setSceneMonitor:,V_sceneMonitor"
- "TB,N,V_didUpdateClientSettingsWithDiff"
- "TB,N,V_didUpdatePairingStatusForExternalSceneIdentifiers"
- "_configureBackgroundColorForLiveSnapshot:"
- "_configureSceneSnapshotContext:"
- "_createMonitor"
- "_didUpdateClientSettingsWithDiff"
- "_didUpdateClientSettingsWithDiff:transitionContext:"
- "_didUpdatePairingStatusBlocks"
- "_didUpdatePairingStatusForExternalSceneIdentifiers"
- "_didUpdatePairingStatusForExternalSceneIdentifiers:"
- "_sceneMonitor"
- "_setSceneMonitor:"
- "appendSuper"
- "createSnapshotWithContext:"
- "defaultPresentationContext"
- "didUpdateClientSettingsWithDiff"
- "didUpdatePairingStatusForExternalSceneIdentifiers"
- "initWithSceneID:"
- "isPairedWithExternalSceneID:"
- "newSnapshot"
- "newSnapshotContext"
- "observeDidUpdatePairingStatusForExternalIdentifiers:"
- "sceneHandle:didUpdateClientSettingsWithDiff:transitionContext:"
- "sceneHandle:didUpdatePairingStatusForExternalSceneIdentifiers:"
- "sceneMonitor"
- "sceneMonitor:pairingStatusDidChangeForExternalSceneIDs:"
- "sceneMonitor:sceneClientSettingsDidChangeWithDiff:transitionContext:"
- "sceneMonitor:sceneSettingsDidChangeWithDiff:previousSettings:"
- "sceneMonitor:sceneWasCreated:"
- "sceneMonitor:sceneWasDestroyed:"
- "setDidUpdateClientSettingsWithDiff:"
- "setDidUpdatePairingStatusForExternalSceneIdentifiers:"
- "snapshotPresentationForSnapshot:"
- "v32@0:8@\"FBSceneMonitor\"16@\"FBScene\"24"
- "v32@0:8@\"FBSceneMonitor\"16@\"NSSet\"24"
- "v32@0:8@\"SBSceneHandle\"16@\"NSSet\"24"
- "v40@0:8@\"FBSceneMonitor\"16@\"FBSSceneClientSettingsDiff\"24@\"FBSSceneTransitionContext\"32"
- "v40@0:8@\"FBSceneMonitor\"16@\"FBSSceneSettingsDiff\"24@\"FBSSceneSettings\"32"
- "v40@0:8@\"SBSceneHandle\"16@\"FBSSceneClientSettingsDiff\"24@\"FBSSceneTransitionContext\"32"
- "\xf0\x81"

```
