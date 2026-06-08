## SpotlightUI

> `/System/Library/PrivateFrameworks/SpotlightUI.framework/SpotlightUI`

```diff

-181.4.6.0.0
-  __TEXT.__text: 0x94b4
-  __TEXT.__auth_stubs: 0x5a0
-  __TEXT.__objc_methlist: 0x110c
-  __TEXT.__const: 0x138
-  __TEXT.__gcc_except_tab: 0x158
-  __TEXT.__cstring: 0x6be
-  __TEXT.__oslogstring: 0x38d
-  __TEXT.__unwind_info: 0x440
-  __TEXT.__objc_classname: 0x323
-  __TEXT.__objc_methname: 0x2c7e
-  __TEXT.__objc_methtype: 0x776
-  __TEXT.__objc_stubs: 0x2580
-  __DATA_CONST.__got: 0x210
-  __DATA_CONST.__const: 0x4d0
-  __DATA_CONST.__objc_classlist: 0xa8
-  __DATA_CONST.__objc_protolist: 0x58
+228.102.0.0.0
+  __TEXT.__text: 0x89c4
+  __TEXT.__objc_methlist: 0xf64
+  __TEXT.__const: 0x120
+  __TEXT.__gcc_except_tab: 0x90
+  __TEXT.__cstring: 0x703
+  __TEXT.__oslogstring: 0x3cd
+  __TEXT.__unwind_info: 0x368
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x528
+  __DATA_CONST.__objc_classlist: 0x78
+  __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc58
+  __DATA_CONST.__objc_selrefs: 0xbf8
   __DATA_CONST.__objc_superrefs: 0x58
-  __AUTH_CONST.__auth_got: 0x2e0
-  __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__cfstring: 0x740
-  __AUTH_CONST.__objc_const: 0x2110
+  __DATA_CONST.__got: 0x1e0
+  __AUTH_CONST.__const: 0x120
+  __AUTH_CONST.__cfstring: 0x700
+  __AUTH_CONST.__objc_const: 0x1b48
   __AUTH_CONST.__objc_intobj: 0x18
-  __DATA.__objc_ivar: 0xcc
-  __DATA.__data: 0x420
-  __DATA_DIRTY.__objc_data: 0x690
+  __AUTH_CONST.__auth_got: 0x0
+  __DATA.__objc_ivar: 0xd4
+  __DATA.__data: 0x300
+  __DATA_DIRTY.__objc_data: 0x4b0
   __DATA_DIRTY.__bss: 0x48
   __DATA_DIRTY.__common: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/ClipServices.framework/ClipServices
   - /System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration

   - /System/Library/PrivateFrameworks/SpringBoardUI.framework/SpringBoardUI
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7294A9FE-5070-3C30-BF80-58AB1AF7D66B
-  Functions: 338
-  Symbols:   1468
-  CStrings:  797
+  UUID: 0F4BAC37-9280-3C07-A41D-710EEBE25AB8
+  Functions: 318
+  Symbols:   1365
+  CStrings:  175
 
Symbols:
+ +[SPUIDefaults isCampoEnabled]
+ +[SPUIRemoteSearchViewController sceneIdentifier]
+ +[SPUISpotlightSceneManager spotlightProcessIdentity]
+ -[SPUISpotlightRemoteViewController delegate]
+ -[SPUISpotlightRemoteViewController scene:clientDidConnect:]
+ -[SPUISpotlightRemoteViewController scene:clientDidConnect:].cold.1
+ -[SPUISpotlightRemoteViewController sceneManager:didAddScene:]
+ -[SPUISpotlightRemoteViewController sceneManager:willRemoveScene:]
+ -[SPUISpotlightRemoteViewController sceneManager:willRemoveScene:].cold.1
+ -[SPUISpotlightRemoteViewController setDelegate:]
+ GCC_except_table18
+ GCC_except_table27
+ GCC_except_table43
+ _AFIsLinwoodEnabledAndAvailable
+ _OBJC_CLASS_$_FBSSceneClientIdentity
+ _OBJC_CLASS_$_FBSceneManager
+ _OBJC_CLASS_$_NSTimer
+ _OBJC_IVAR_$_SPUISearchBarController._backgroundBlurView
+ _OBJC_IVAR_$_SPUISpotlightRemoteViewController._delegate
+ _OBJC_IVAR_$_SPUISpotlightRemoteViewController._recreateSceneTimer
+ __OBJC_$_CLASS_METHODS_SPUIRemoteSearchViewController
+ __OBJC_$_CLASS_PROP_LIST_SPUIRemoteSearchViewController
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_FBSceneManagerObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FBSceneManagerObserver
+ __OBJC_$_PROTOCOL_REFS_FBSceneManagerObserver
+ __OBJC_LABEL_PROTOCOL_$_FBSceneManagerObserver
+ __OBJC_PROTOCOL_$_FBSceneManagerObserver
+ ___61-[SPUISpotlightRemoteViewController createSceneWithPriority:]_block_invoke.70
+ ___61-[SPUISpotlightRemoteViewController createSceneWithPriority:]_block_invoke_2.74
+ ___61-[SPUISpotlightRemoteViewController createSceneWithPriority:]_block_invoke_3
+ ___61-[SPUISpotlightRemoteViewController createSceneWithPriority:]_block_invoke_4
+ ___61-[SPUISpotlightRemoteViewController createSceneWithPriority:]_block_invoke_5
+ ___61-[SPUISpotlightRemoteViewController createSceneWithPriority:]_block_invoke_6
+ ___61-[SPUISpotlightRemoteViewController createSceneWithPriority:]_block_invoke_7
+ ___61-[SPUISpotlightRemoteViewController createSceneWithPriority:]_block_invoke_7.cold.1
+ ___61-[SPUISpotlightRemoteViewController createSceneWithPriority:]_block_invoke_7.cold.2
+ ___62-[SPUISpotlightRemoteViewController sceneManager:didAddScene:]_block_invoke
+ ___66-[SPUISpotlightRemoteViewController sceneManager:willRemoveScene:]_block_invoke
+ ___81-[SPUISpotlightRemoteViewController viewDidMoveToWindow:shouldAppearOrDisappear:]_block_invoke_2
+ ___block_descriptor_32_e33_v16?0"FBSMutableSceneSettings"8l
+ ___block_descriptor_32_e39_v16?0"FBSMutableSceneClientSettings"8l
+ ___block_descriptor_40_e8_32s_e43_v16?0"UIMutableApplicationSceneSettings"8ls32l8
+ ___block_descriptor_41_e8_32s_e33_v16?0"FBSMutableSceneSettings"8ls32l8
+ ___block_descriptor_48_e8_32s_e33_v16?0"FBSMutableSceneSettings"8ls32l8
+ ___block_descriptor_48_e8_32s_e35_v16?0"FBSMutableSceneParameters"8ls32l8
+ ___block_descriptor_48_e8_32s_e63_v24?0"FBSMutableSceneSettings"8"FBSSceneTransitionContext"16ls32l8
+ ___block_descriptor_48_e8_32w_e17_v16?0"NSTimer"8lw32l8
+ ___block_descriptor_56_e8_32s40s_e39_v16?0"<FBSceneManagerSceneCreating>"8ls32l8s40l8
+ ___block_descriptor_64_e8_32s40w_e20_v20?0B8"NSError"12lw40l8s32l8
+ ___block_literal_global.65
+ ___block_literal_global.72
+ ___block_literal_global.85
+ ___block_literal_global.96
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$configureParameters:
+ _objc_msgSend$createScene:
+ _objc_msgSend$error
+ _objc_msgSend$identityForProcessIdentity:
+ _objc_msgSend$invalidate:
+ _objc_msgSend$isCampoEnabled
+ _objc_msgSend$parentViewController
+ _objc_msgSend$performUpdate:withCompletion:
+ _objc_msgSend$scheduledTimerWithTimeInterval:repeats:block:
+ _objc_msgSend$screen
+ _objc_msgSend$setClientIdentity:
+ _objc_msgSend$setExecutionContext:
+ _objc_msgSend$setIdentity:
+ _objc_msgSend$setSpecification:
+ _objc_msgSend$spotlightProcessIdentity
+ _objc_msgSend$spotlightRemoteViewController:didCreateScene:
+ _objc_msgSend$updateClientSettingsWithBlock:
+ _objc_msgSend$updateSettings:
+ _objc_msgSend$updateUISettingsWithBlock:
+ _objc_release_x9
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x8
- +[SPUISpotlightRemoteViewController spotlightSupportedInterfaceOrientations]
- -[SPUIMutableSearchBarSceneSettings animated]
- -[SPUIMutableSearchBarSceneSettings copyWithZone:]
- -[SPUIMutableSearchBarSceneSettings scrollProgress]
- -[SPUIMutableSearchBarSceneSettings setAnimated:]
- -[SPUIMutableSearchBarSceneSettings setScrollProgress:]
- -[SPUISearchBarClientSceneSettings headerHeight]
- -[SPUISearchBarClientSceneSettings mutableCopyWithZone:]
- -[SPUISearchBarController didInvalidateSceneWhenForeground]
- -[SPUISearchBarController initialFittingSize]
- -[SPUISearchBarController scene:didUpdateClientSettings:]
- -[SPUISearchBarController sceneSpecification]
- -[SPUISearchBarController setSceneFrameOnRotation]
- -[SPUISearchBarController updateSceneSettingsWithBlock:]
- -[SPUISearchBarMutableClientSceneSettings copyWithZone:]
- -[SPUISearchBarMutableClientSceneSettings headerHeight]
- -[SPUISearchBarMutableClientSceneSettings setHeaderHeight:]
- -[SPUISearchBarSceneSettings animated]
- -[SPUISearchBarSceneSettings mutableCopyWithZone:]
- -[SPUISearchBarSceneSettings scrollProgress]
- -[SPUISearchBarSceneSpecification clientSettingsClass]
- -[SPUISearchBarSceneSpecification settingsClass]
- -[SPUISearchBarSceneSpecification transitionContextClass]
- -[SPUISearchBarTransitionContext searchBarDidFocus]
- -[SPUISearchBarTransitionContext setSearchBarDidFocus:]
- -[SPUISpotlightRemoteViewController createSceneWithPriority:].cold.1
- -[SPUISpotlightRemoteViewController sceneDidInvalidate:withContext:].cold.1
- -[SPUISpotlightRemoteViewController setTransaction:]
- -[SPUISpotlightRemoteViewController transaction:didCreateScene:]
- -[SPUISpotlightRemoteViewController transaction:didCreateScene:].cold.1
- -[SPUISpotlightRemoteViewController transaction]
- -[SPUISpotlightRemoteViewController updateTraitCollection]
- GCC_except_table12
- GCC_except_table24
- GCC_except_table37
- GCC_except_table65
- _OBJC_CLASS_$_FBApplicationUpdateScenesTransaction
- _OBJC_CLASS_$_FBSMutableSceneParameters
- _OBJC_CLASS_$_NSNotificationCenter
- _OBJC_CLASS_$_SPUIMutableSearchBarSceneSettings
- _OBJC_CLASS_$_SPUISearchBarClientSceneSettings
- _OBJC_CLASS_$_SPUISearchBarMutableClientSceneSettings
- _OBJC_CLASS_$_SPUISearchBarSceneSettings
- _OBJC_CLASS_$_SPUISearchBarSceneSpecification
- _OBJC_CLASS_$_SPUISearchBarTransitionContext
- _OBJC_IVAR_$_SPUISpotlightRemoteViewController._transaction
- _OBJC_METACLASS_$_SPUIMutableSearchBarSceneSettings
- _OBJC_METACLASS_$_SPUISearchBarClientSceneSettings
- _OBJC_METACLASS_$_SPUISearchBarMutableClientSceneSettings
- _OBJC_METACLASS_$_SPUISearchBarSceneSettings
- _OBJC_METACLASS_$_SPUISearchBarSceneSpecification
- _OBJC_METACLASS_$_SPUISearchBarTransitionContext
- _OUTLINED_FUNCTION_3
- _SPSpotlightFocusConstant
- _SPSpotlightHeightOfBarConstant
- _SPUISearchBarAnimatedConstant
- _SPUISearchBarScrollProgressConstant
- _SpotlightBundleID
- __OBJC_$_CLASS_METHODS_SPUISpotlightRemoteViewController
- __OBJC_$_CLASS_PROP_LIST_SPUISpotlightRemoteViewController
- __OBJC_$_INSTANCE_METHODS_SPUIMutableSearchBarSceneSettings
- __OBJC_$_INSTANCE_METHODS_SPUISearchBarClientSceneSettings
- __OBJC_$_INSTANCE_METHODS_SPUISearchBarMutableClientSceneSettings
- __OBJC_$_INSTANCE_METHODS_SPUISearchBarSceneSettings
- __OBJC_$_INSTANCE_METHODS_SPUISearchBarSceneSpecification
- __OBJC_$_INSTANCE_METHODS_SPUISearchBarTransitionContext
- __OBJC_$_PROP_LIST_SPUIMutableSearchBarSceneSettings
- __OBJC_$_PROP_LIST_SPUISearchBarClientSceneSettings
- __OBJC_$_PROP_LIST_SPUISearchBarClientSceneSettings.80
- __OBJC_$_PROP_LIST_SPUISearchBarMutableClientSceneSettings
- __OBJC_$_PROP_LIST_SPUISearchBarSceneSettings
- __OBJC_$_PROP_LIST_SPUISearchBarSceneSettings.59
- __OBJC_$_PROP_LIST_SPUISearchBarTransitionContext
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BSTransactionObserver
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_FBApplicationUpdateScenesTransactionObserver
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SPUISearchBarClientSceneSettings
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SPUISearchBarSceneSettings
- __OBJC_$_PROTOCOL_METHOD_TYPES_BSTransactionObserver
- __OBJC_$_PROTOCOL_METHOD_TYPES_FBApplicationUpdateScenesTransactionObserver
- __OBJC_$_PROTOCOL_METHOD_TYPES_SPUISearchBarClientSceneSettings
- __OBJC_$_PROTOCOL_METHOD_TYPES_SPUISearchBarSceneSettings
- __OBJC_$_PROTOCOL_REFS_BSTransactionObserver
- __OBJC_$_PROTOCOL_REFS_FBApplicationUpdateScenesTransactionObserver
- __OBJC_$_PROTOCOL_REFS_SPUISearchBarClientSceneSettings
- __OBJC_$_PROTOCOL_REFS_SPUISearchBarSceneSettings
- __OBJC_CLASS_PROTOCOLS_$_SPUIMutableSearchBarSceneSettings
- __OBJC_CLASS_PROTOCOLS_$_SPUISearchBarClientSceneSettings
- __OBJC_CLASS_PROTOCOLS_$_SPUISearchBarMutableClientSceneSettings
- __OBJC_CLASS_PROTOCOLS_$_SPUISearchBarSceneSettings
- __OBJC_CLASS_RO_$_SPUIMutableSearchBarSceneSettings
- __OBJC_CLASS_RO_$_SPUISearchBarClientSceneSettings
- __OBJC_CLASS_RO_$_SPUISearchBarMutableClientSceneSettings
- __OBJC_CLASS_RO_$_SPUISearchBarSceneSettings
- __OBJC_CLASS_RO_$_SPUISearchBarSceneSpecification
- __OBJC_CLASS_RO_$_SPUISearchBarTransitionContext
- __OBJC_LABEL_PROTOCOL_$_BSTransactionObserver
- __OBJC_LABEL_PROTOCOL_$_FBApplicationUpdateScenesTransactionObserver
- __OBJC_LABEL_PROTOCOL_$_SPUISearchBarClientSceneSettings
- __OBJC_LABEL_PROTOCOL_$_SPUISearchBarSceneSettings
- __OBJC_METACLASS_RO_$_SPUIMutableSearchBarSceneSettings
- __OBJC_METACLASS_RO_$_SPUISearchBarClientSceneSettings
- __OBJC_METACLASS_RO_$_SPUISearchBarMutableClientSceneSettings
- __OBJC_METACLASS_RO_$_SPUISearchBarSceneSettings
- __OBJC_METACLASS_RO_$_SPUISearchBarSceneSpecification
- __OBJC_METACLASS_RO_$_SPUISearchBarTransitionContext
- __OBJC_PROTOCOL_$_BSTransactionObserver
- __OBJC_PROTOCOL_$_FBApplicationUpdateScenesTransactionObserver
- __OBJC_PROTOCOL_$_SPUISearchBarClientSceneSettings
- __OBJC_PROTOCOL_$_SPUISearchBarSceneSettings
- __UIScreenDefaultTraitCollectionDidChangeNotification
- ___56-[SPUISearchBarController updateSceneSettingsWithBlock:]_block_invoke
- ___56-[SPUISearchBarController updateSceneSettingsWithBlock:]_block_invoke_2
- ___58-[SPUISpotlightRemoteViewController updateTraitCollection]_block_invoke
- ___61-[SPUISpotlightRemoteViewController createSceneWithPriority:]_block_invoke.16
- ___61-[SPUISpotlightRemoteViewController createSceneWithPriority:]_block_invoke.21
- ___61-[SPUISpotlightRemoteViewController createSceneWithPriority:]_block_invoke_2.cold.1
- ___64-[SPUISpotlightRemoteViewController transaction:didCreateScene:]_block_invoke
- ___block_descriptor_40_e8_32bs_e33_v16?0"FBSMutableSceneSettings"8ls32l8
- ___block_descriptor_40_e8_32s_e8_v16?0q8ls32l8
- ___block_descriptor_41_e8_32s_e60_"FBSSceneTransitionContext"16?0"FBSMutableSceneSettings"8ls32l8
- ___block_descriptor_48_e8_32s_e39_"FBMutableProcessExecutionContext"8?0ls32l8
- ___block_descriptor_48_e8_32s_e5_v8?0ls32l8
- ___block_descriptor_48_e8_32s_e60_"FBSSceneTransitionContext"16?0"FBSMutableSceneSettings"8ls32l8
- ___block_descriptor_56_e8_32w_e8_v12?0B8lw32l8
- ___block_literal_global.41
- _dispatch_after
- _dispatch_time
- _objc_alloc_init
- _objc_msgSend$_scene
- _objc_msgSend$addObserver:selector:name:object:
- _objc_msgSend$begin
- _objc_msgSend$clientSettingsClass
- _objc_msgSend$defaultCenter
- _objc_msgSend$headerHeight
- _objc_msgSend$initWithProcessIdentity:executionContextProvider:
- _objc_msgSend$initWithSceneIdentifier:
- _objc_msgSend$intrinsicContentSize
- _objc_msgSend$parametersForSpecification:
- _objc_msgSend$sceneContentStateDidChange:
- _objc_msgSend$searchBarDidFocus
- _objc_msgSend$setClientSettings:
- _objc_msgSend$setCompletionBlock:
- _objc_msgSend$setConstant:
- _objc_msgSend$setNeedsLayout
- _objc_msgSend$setSettings:
- _objc_msgSend$setTransaction:
- _objc_msgSend$setWaitsForSceneCommits:
- _objc_msgSend$settingsClass
- _objc_msgSend$tlks_screen
- _objc_msgSend$transaction
- _objc_msgSend$transitionContextClass
- _objc_msgSend$updateSceneWithIdentity:parameters:transitionContext:
- _objc_msgSend$updateSettingsWithTransitionBlock:
- _objc_msgSend$viewWillAppear:
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x23
- _objc_retain_x25
- _searchScreenSceneIdentifier
CStrings:
+ "\""
+ "SPUISearchViewSceneIdentifier"
+ "Spotlight is running the frontboard create scene request"
+ "Spotlight launch failed retrying in 1 second with error: %{public}@"
+ "Spotlight scene creation passed"
+ "Spotlight scene invalidated with error: %@"
+ "v16@?0@\"<FBSceneManagerSceneCreating>\"8"
+ "v16@?0@\"FBSMutableSceneClientSettings\"8"
+ "v16@?0@\"FBSMutableSceneParameters\"8"
+ "v16@?0@\"NSTimer\"8"
+ "v16@?0@\"UIMutableApplicationSceneSettings\"8"
+ "v20@?0B8@\"NSError\"12"
- "#16@0:8"
- ".cxx_destruct"
- "@\"<SPUIRemoteSearchViewDelegate>\""
- "@\"<SPUISearchBarDelegate>\""
- "@\"<SPUISpotlightSceneManagerDelegate>\""
- "@\"<UIScenePresenter>\""
- "@\"BSTimer\""
- "@\"FBApplicationUpdateScenesTransaction\""
- "@\"FBMutableProcessExecutionContext\"8@?0"
- "@\"FBSDisplayConfiguration\""
- "@\"FBSDisplayLayoutMonitor\""
- "@\"FBSProcessTerminationRequest\"32@0:8@\"FBProcess\"16@\"NSError\"24"
- "@\"FBSProcessWatchdogPolicy\"32@0:8@\"FBProcess\"16@\"FBProcessWatchdogEventContext\"24"
- "@\"FBSSceneTransitionContext\"16@?0@\"FBSMutableSceneSettings\"8"
- "@\"FBScene\""
- "@\"NSHashTable\""
- "@\"NSLayoutConstraint\""
- "@\"NSMutableArray\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSSet\"32@0:8@\"FBScene\"16@\"NSSet\"24"
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"RBSAssertion\""
- "@\"RBSProcessHandle\""
- "@\"SPUIAppService\""
- "@\"SPXPCConnection\""
- "@\"UIView\""
- "@\"UIView<UIScenePresentation>\""
- "@\"_UILegibilitySettings\""
- "@\"_UILegibilitySettings\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8q16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "@40@0:8q16@24Q32"
- "@40@0:8q16@24q32"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "BSTransactionObserver"
- "CGSizeValue"
- "FBApplicationUpdateScenesTransactionObserver"
- "FBProcessWatchdogProviding"
- "FBSceneObserver"
- "I"
- "I16@0:8"
- "NSObject"
- "Q"
- "Q16@0:8"
- "SPUIAppService"
- "SPUIDefaults"
- "SPUILegibilitySceneSettings"
- "SPUIMutableLegibilitySceneSettings"
- "SPUIMutableSearchBarSceneSettings"
- "SPUIMutableSearchViewSceneSettings"
- "SPUIProxySearchField"
- "SPUIRemoteSearchViewController"
- "SPUISearchBarClientSceneSettings"
- "SPUISearchBarController"
- "SPUISearchBarMutableClientSceneSettings"
- "SPUISearchBarSceneSettings"
- "SPUISearchBarSceneSpecification"
- "SPUISearchBarTransitionContext"
- "SPUISearchViewClientSceneSettings"
- "SPUISearchViewMutableClientSceneSettings"
- "SPUISearchViewSceneSettings"
- "SPUISearchViewSceneSpecification"
- "SPUISearchViewSceneTransitionContext"
- "SPUISpotlightRemoteViewController"
- "SPUISpotlightSceneManager"
- "SPUISpotlightSceneManagerDelegate"
- "Spotlight has an existing transaction in progress %@"
- "Spotlight is running the frontboard transaction"
- "Spotlight scene transaction passed"
- "T#,R"
- "T@\"<SPUIRemoteSearchViewDelegate>\",W,N,V_delegate"
- "T@\"<SPUISearchBarDelegate>\",W,N,V_delegate"
- "T@\"<SPUISpotlightSceneManagerDelegate>\",W,N,V_delegate"
- "T@\"<UIScenePresenter>\",&,V_presenter"
- "T@\"BSTimer\",&,V_watchdogTimer"
- "T@\"FBApplicationUpdateScenesTransaction\",&,V_transaction"
- "T@\"FBSDisplayConfiguration\",&,N"
- "T@\"FBSDisplayLayoutMonitor\",&,V_layoutMonitor"
- "T@\"FBScene\",&,V_scene"
- "T@\"NSHashTable\",&,V_foregroundScenes"
- "T@\"NSHashTable\",&,V_managedScenes"
- "T@\"NSLayoutConstraint\",&,V_heightAnchor"
- "T@\"NSMutableArray\",&,V_sceneEventsQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,V_queue"
- "T@\"NSString\",&,V_sceneIdentifier"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"RBSAssertion\",&,V_backgroundingAssertions"
- "T@\"RBSAssertion\",&,V_initializationAssertions"
- "T@\"RBSProcessHandle\",&,V_spotlightProcessHandle"
- "T@\"UIView\",&,N,V_dummyTransitionView"
- "T@\"UIView<UIScenePresentation>\",&,V_hostView"
- "T@\"_UILegibilitySettings\",&,N"
- "T@\"_UILegibilitySettings\",&,N,V_legibilitySettings"
- "T@\"_UILegibilitySettings\",R,N"
- "T@\"_UINavigationBarTitleView\",&,D"
- "T@?,C,N,V_didFinishDismissingSpotlightHandler"
- "T@?,C,N,V_finishedPresentingSpotlightHandler"
- "T@?,C,N,V_willBeginDismissingSpotlightHandler"
- "T@?,C,N,V_willStartPresetingSpotlightHandler"
- "TB,N"
- "TB,N,GisKeyboardPresented"
- "TB,N,GisKeyboardPresented,V_keyboardPresented"
- "TB,N,V_crashedWhileForeground"
- "TB,N,V_roundedCornerVisible"
- "TB,R,GisKeyboardPresented"
- "TB,R,N"
- "TB,R,N,V_prewarmSceneInTheBackground"
- "TI,N"
- "TI,N,V_searchHeaderBackgroundContextID"
- "TI,N,V_searchHeaderBlurContextID"
- "TI,N,V_searchHeaderContextID"
- "TI,R"
- "TQ,N"
- "TQ,N,V_searchHeaderBackgroundLayerRenderID"
- "TQ,N,V_searchHeaderBlurLayerRenderID"
- "TQ,N,V_searchHeaderLayerRenderID"
- "TQ,N,V_source"
- "TQ,R"
- "TQ,R,N"
- "Td,N"
- "Td,N,V_distanceToTopOfIcons"
- "Td,N,V_keyboardHeight"
- "Td,N,V_keyboardProtectorHeight"
- "Td,N,V_revealProgress"
- "Td,N,V_searchBarCornerRadius"
- "Td,R"
- "Td,R,N"
- "Tq,N,V_currentOrientation"
- "T{CGSize=dd},N"
- "T{CGSize=dd},N,V_dockedSearchBarSize"
- "T{CGSize=dd},N,V_searchBarSize"
- "T{CGSize=dd},R"
- "UTF8String"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_FBSScene"
- "_activated"
- "_appConnection"
- "_appService"
- "_appServiceQueue"
- "_appearState"
- "_awakeNotifyToken"
- "_backgroundConnection"
- "_backgroundingAssertions"
- "_canShowWhileLocked"
- "_cancelAwakeNotifyToken"
- "_crashedWhileForeground"
- "_currentOrientation"
- "_delayPresentationTillSceneContentIsReady"
- "_delegate"
- "_didFinishDismissingSpotlightHandler"
- "_displayConfiguration"
- "_distanceToTopOfIcons"
- "_dockedSearchBarSize"
- "_dummyTransitionView"
- "_finishedPresentingSpotlightHandler"
- "_foregroundScenes"
- "_heightAnchor"
- "_hostView"
- "_initializationAssertions"
- "_keyboardHeight"
- "_keyboardPresented"
- "_keyboardProtectorHeight"
- "_layoutMonitor"
- "_legibilitySettings"
- "_managedScenes"
- "_presenter"
- "_prewarmSceneInTheBackground"
- "_queue"
- "_revealProgress"
- "_roundedCornerVisible"
- "_scene"
- "_sceneEventsQueue"
- "_sceneIdentifier"
- "_searchBarCornerRadius"
- "_searchBarSize"
- "_searchHeaderBackgroundContextID"
- "_searchHeaderBackgroundLayerRenderID"
- "_searchHeaderBlurContextID"
- "_searchHeaderBlurLayerRenderID"
- "_searchHeaderContextID"
- "_searchHeaderLayerRenderID"
- "_source"
- "_spotlightProcessHandle"
- "_synchronizedDrawingFence"
- "_toWindowOrientation"
- "_transaction"
- "_watchdogTimer"
- "_willBeginDismissingSpotlightHandler"
- "_willStartPresetingSpotlightHandler"
- "_windowInterfaceOrientation"
- "acquireWithError:"
- "activate"
- "activeInterfaceOrientation"
- "addObject:"
- "addObserver:"
- "addObserver:selector:name:object:"
- "addOrExecuteEventAsNeeded:"
- "addPropagatedProperty:"
- "addScene:"
- "addSubview:"
- "animated"
- "applyAssertionAsNeeded"
- "arrayWithObjects:count:"
- "attributeWithDomain:name:"
- "autorelease"
- "backgroundBlurView"
- "backgroundColorWhileHosting"
- "backgroundingAssertions"
- "begin"
- "boolForKey:"
- "boolForSetting:"
- "bottomAnchor"
- "bottomPaddingToKeyboard"
- "bottomSearchFieldEnabled"
- "bounds"
- "bundleIdentifier"
- "class"
- "clearEventQueue"
- "clientSettings"
- "clientSettingsClass"
- "componentsJoinedByString:"
- "configurationForDefaultMainDisplayMonitor"
- "conformsToProtocol:"
- "constraintEqualToAnchor:"
- "constraintEqualToConstant:"
- "contentState"
- "contextWithIdentity:"
- "copyWithZone:"
- "cornerRadiusConfiguration"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "crashedWhileForeground"
- "createPresenterWithIdentifier:"
- "createSceneIfNeededWithPriority:"
- "createSceneWithPriority:"
- "currentDevice"
- "currentOrientation"
- "currentState"
- "d"
- "d16@0:8"
- "deactivate"
- "debugDescription"
- "defaultCenter"
- "delegate"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "didFinishDismissingSpotlightHandler"
- "didInvalidateSceneWhenForeground"
- "dismissSearchView"
- "displayBacklightLevel"
- "displayConfiguration"
- "displayName"
- "displayNameLoaded"
- "doubleValue"
- "dummyTransitionView"
- "elements"
- "enableFloatingWindow"
- "event"
- "execute:assertion:error:"
- "finishCompletionHandlerIfNeeded"
- "finishedPresentingSpotlightHandler"
- "flagForSetting:"
- "foregroundScenes"
- "frame"
- "hash"
- "headerHeight"
- "height"
- "heightAnchor"
- "hostView"
- "i"
- "identifier"
- "identity"
- "identityForEmbeddedApplicationIdentifier:"
- "identityForIdentifier:workspaceIdentifier:"
- "ignoreOcclusionReasons"
- "init"
- "initWithContext:"
- "initWithExplanation:target:attributes:"
- "initWithFormat:"
- "initWithName:"
- "initWithOptions:capacity:"
- "initWithProcessIdentity:executionContextProvider:"
- "initWithSceneIdentifier:"
- "initWithServiceName:onQueue:"
- "initWithSettings:"
- "initWithSuiteName:"
- "initialFittingSize"
- "initializationAssertions"
- "initialize"
- "integerValue"
- "interfaceOrientation"
- "intrinsicContentSize"
- "invalidate"
- "isContinuityDisplay"
- "isEqual:"
- "isEqualToString:"
- "isExternal"
- "isForeground"
- "isInHardwareKeyboardMode"
- "isKeyboardPresented"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isPhone"
- "isProxy"
- "isRunning"
- "isUISubclass"
- "isValid"
- "keyDescriptionForSetting:"
- "launchSpotlightIfNeededWithForegroundPriority:"
- "layoutIfNeeded"
- "layoutMonitor"
- "leadingAnchor"
- "length"
- "loadView"
- "mainBundle"
- "mainConfiguration"
- "managedScenes"
- "modifyPresentationContext:"
- "monitorWithConfiguration:"
- "mutableCopy"
- "mutableCopyWithZone:"
- "notificationCenterSearchBar"
- "numberWithDouble:"
- "numberWithFloat:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLongLong:"
- "objectForKeyedSubscript:"
- "objectForSetting:"
- "otherSettings"
- "pageDotInvokeEnabled"
- "parametersForSpecification:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "performUpdate:"
- "peripheryInsets"
- "policyWithProvisions:"
- "presentationContext"
- "presentationIntent"
- "presentationView"
- "presenter"
- "prewarmSceneInTheBackground"
- "provisionWithAllowance:"
- "q16@0:8"
- "queue"
- "registerAwakeNotifyToken"
- "release"
- "removeAllObjects"
- "removeFromSuperview"
- "removeObject:"
- "removeObjectForKey:"
- "removeObserver:"
- "removeScene:"
- "renderingEnvironment"
- "requestForProcess:withLabel:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "roundedCornerVisible"
- "safeAreaInsetsPortrait"
- "scene"
- "scene:clientDidConnect:"
- "scene:didApplyUpdateWithContext:"
- "scene:didCompleteUpdateWithContext:error:"
- "scene:didPrepareUpdateWithContext:"
- "scene:didUpdateClientSettings:"
- "scene:didUpdateClientSettingsWithDiff:oldClientSettings:transitionContext:"
- "scene:didUpdateSettings:"
- "scene:handleActions:"
- "sceneContentStateDidChange:"
- "sceneDidActivate:"
- "sceneDidInvalidate:"
- "sceneDidInvalidate:withContext:"
- "sceneEventsQueue"
- "sceneIdentifier"
- "sceneSettings"
- "sceneSettingsFrameFromRect:"
- "sceneSpecification"
- "sceneWillActivate:"
- "sceneWillBackground:"
- "sceneWillDeactivate:withContext:"
- "sceneWillDeactivate:withError:"
- "sceneWillForeground:"
- "scrollProgress"
- "searchBar-notificationCenter"
- "searchBar-todayView"
- "searchBarDidFocus"
- "searchHeaderBackgroundLayerRenderID"
- "searchHeaderBlurContextID"
- "searchHeaderBlurLayerRenderID"
- "searchHeaderLayerRenderID"
- "searchScreen"
- "searchViewKeyboardPresentationStateDidChange"
- "self"
- "sendMessage:"
- "sendMessage:withReply:"
- "separateHeaderBlurLayeringEnabled"
- "setAcceptsDictationSearchResults:"
- "setActive:"
- "setActiveAppearance:"
- "setAlpha:"
- "setAnimated:"
- "setAnimationFence:"
- "setAnimationSettings:"
- "setAppearanceStyle:"
- "setAttributes:"
- "setAutocapitalizationType:"
- "setAutocorrectionType:"
- "setBackgroundColorWhileHosting:"
- "setBackgroundStyle:"
- "setBackgroundingAssertions:"
- "setBarrier:"
- "setBlurProgress:animated:"
- "setClientSettings:"
- "setClippingDisabled:"
- "setCompletionBlock:"
- "setConstant:"
- "setCrashedWhileForeground:"
- "setCurrentOrientation:"
- "setDefaultStatusBarHeight:forOrientation:"
- "setDelegate:"
- "setDeviceOrientationEventsEnabled:"
- "setDidFinishDismissingSpotlightHandler:"
- "setDisplayConfiguration:"
- "setDisplayName:"
- "setDistanceToTopOfIcons:"
- "setDockedSearchBarSize:"
- "setDummyTransitionView:"
- "setEnhancedWindowingEnabled:"
- "setExplanation:"
- "setFinishedPresentingSpotlightHandler:"
- "setFlag:forSetting:"
- "setForcedStatusBarForegroundTransparent:"
- "setForcedStatusBarStyle:"
- "setForeground:"
- "setForegroundScenes:"
- "setFrame:"
- "setHeaderHeight:"
- "setHeight:"
- "setHeightAnchor:"
- "setHostView:"
- "setInfo:"
- "setInitializationAssertions:"
- "setInterfaceOrientation:"
- "setInterruptionPolicy:"
- "setKeyboardHeight:"
- "setKeyboardPresented:"
- "setKeyboardProtectorHeight:"
- "setLaunchIntent:"
- "setLayoutMonitor:"
- "setLegibilitySettings:"
- "setManagedScenes:"
- "setNeedsLayout"
- "setNeedsUserInteractivePriority:"
- "setObject:forSetting:"
- "setPersistenceIdentifier:"
- "setPresentationIntent:"
- "setPresentationSource:"
- "setPresentedLayerTypes:"
- "setPresenter:"
- "setQueue:"
- "setReportType:"
- "setReturnKeyType:"
- "setRevealProgress:"
- "setRootObject:"
- "setRoundedCornerVisible:"
- "setSafeAreaInsetsLandscapeLeft:"
- "setSafeAreaInsetsLandscapeRight:"
- "setSafeAreaInsetsPortrait:"
- "setScene:"
- "setSceneEventsQueue:"
- "setSceneFrameOnRotation"
- "setSceneIdentifier:"
- "setScrollProgress:"
- "setSearchBarCornerRadius:"
- "setSearchBarDidFocus:"
- "setSearchBarSize:"
- "setSearchHeaderBackgroundContextID:"
- "setSearchHeaderBackgroundLayerRenderID:"
- "setSearchHeaderBlurContextID:"
- "setSearchHeaderBlurLayerRenderID:"
- "setSearchHeaderContextID:"
- "setSearchHeaderLayerRenderID:"
- "setSettings:"
- "setShouldBackground:"
- "setShouldDismiss:"
- "setSource:"
- "setSpotlightProcessHandle:"
- "setStatusBarAlpha:"
- "setStatusBarHidden:"
- "setTransaction:"
- "setTransitionHandler:"
- "setTranslatesAutoresizingMaskIntoConstraints:"
- "setUserInterfaceStyle:"
- "setView:"
- "setWaitsForSceneCommits:"
- "setWatchdogProvider:"
- "setWatchdogTimer:"
- "setWillBeginDismissingSpotlightHandler:"
- "setWillStartPresetingSpotlightHandler:"
- "settings"
- "settingsClass"
- "settingsWithDuration:"
- "sharedAppService"
- "sharedInstance"
- "sharedInstanceForStyle:"
- "sharedManager"
- "shouldBackground"
- "shouldDismiss"
- "source"
- "spendMoreTimeReleasingMemory"
- "spotlightProcessHandle"
- "spotlightSupportedInterfaceOrientations"
- "statusBarHeightForOrientation:ignoreHidden:"
- "superclass"
- "targetWithProcessIdentity:"
- "textFieldTraits"
- "tlks_screen"
- "todayViewSearchBar"
- "topAnchor"
- "trailingAnchor"
- "traitCollection"
- "transaction"
- "transaction:didCommitSceneUpdate:"
- "transaction:didCreateScene:"
- "transaction:didLaunchProcess:"
- "transaction:willCommitSceneUpdate:"
- "transaction:willLaunchProcess:"
- "transaction:willUpdateScene:"
- "transactionDidBegin:"
- "transactionDidComplete:"
- "transactionDidFinishWork:"
- "transactionWillBegin:"
- "transitionContext"
- "transitionContextClass"
- "transitionDuration"
- "uiPresentationManager"
- "unsignedIntValue"
- "unsignedLongLongValue"
- "updateIntent:"
- "updateSafeAreasOnSettings:"
- "updateSceneSettingsWithBlock:"
- "updateSceneToOrientation:withTransitionCoordinator:"
- "updateSceneWithIdentity:parameters:transitionContext:"
- "updateSettingsWithBlock:"
- "updateSettingsWithTransitionBlock:"
- "updateTraitCollection"
- "useUnifiedBackground"
- "userInterfaceIdiom"
- "userInterfaceStyle"
- "v12@?0B8"
- "v16@0:8"
- "v16@?0q8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v24@0:8@\"BSTransaction\"16"
- "v24@0:8@\"FBScene\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v28@0:8@16B24"
- "v28@0:8d16B24"
- "v32@0:8@\"FBApplicationUpdateScenesTransaction\"16@\"FBApplicationProcess\"24"
- "v32@0:8@\"FBApplicationUpdateScenesTransaction\"16@\"FBScene\"24"
- "v32@0:8@\"FBScene\"16@\"FBSSceneTransitionContext\"24"
- "v32@0:8@\"FBScene\"16@\"FBSSceneUpdate\"24"
- "v32@0:8@\"FBScene\"16@\"FBSceneClientHandle\"24"
- "v32@0:8@\"FBScene\"16@\"FBSceneUpdateContext\"24"
- "v32@0:8@\"FBScene\"16@\"NSError\"24"
- "v32@0:8@16@24"
- "v32@0:8q16@24"
- "v32@0:8{CGSize=dd}16"
- "v40@0:8@\"FBScene\"16@\"FBSceneUpdateContext\"24@\"NSError\"32"
- "v40@0:8@16@24@32"
- "v40@0:8{CGSize=dd}16@32"
- "v48@0:8@\"FBScene\"16@\"FBSSceneClientSettingsDiff\"24@\"FBSSceneClientSettings\"32@\"FBSSceneTransitionContext\"40"
- "v48@0:8@16@24@32@40"
- "valueDescriptionForFlag:object:ofSetting:"
- "valueWithBytes:objCType:"
- "view"
- "viewDidAppear:"
- "viewDidDisappear:"
- "viewDidLayoutSubviews"
- "viewDidMoveToWindow:shouldAppearOrDisappear:"
- "viewWillAppear:"
- "viewWillDisappear:"
- "viewWillTransitionToSize:withTransitionCoordinator:"
- "watchdogPolicyForProcess:eventContext:"
- "watchdogTerminationRequestForProcess:error:"
- "watchdogTimer"
- "willBeginDismissingSpotlightHandler"
- "willLaunchSpotlightInBackground"
- "willStartPresetingSpotlightHandler"
- "window"
- "windowScene"
- "zone"
- "{CGRect={CGPoint=dd}{CGSize=dd}}48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "{CGSize=\"width\"d\"height\"d}"
- "{CGSize=dd}16@0:8"

```
