## AssistantUI

> `/System/Library/PrivateFrameworks/AssistantUI.framework/AssistantUI`

```diff

-3302.13.3.1.1
-  __TEXT.__text: 0x48b80
+3304.61.1.0.0
+  __TEXT.__text: 0x47b4c
   __TEXT.__auth_stubs: 0xad0
-  __TEXT.__objc_methlist: 0x42c8
-  __TEXT.__const: 0x2e8
-  __TEXT.__gcc_except_tab: 0xc60
-  __TEXT.__cstring: 0x6adf
-  __TEXT.__oslogstring: 0x42c6
+  __TEXT.__objc_methlist: 0x422c
+  __TEXT.__const: 0x2d8
+  __TEXT.__gcc_except_tab: 0xc78
+  __TEXT.__cstring: 0x6894
+  __TEXT.__oslogstring: 0x40e2
   __TEXT.__dlopen_cstrs: 0x46f
-  __TEXT.__unwind_info: 0x17b8
-  __TEXT.__objc_classname: 0xb15
-  __TEXT.__objc_methname: 0x13857
-  __TEXT.__objc_methtype: 0x415a
-  __TEXT.__objc_stubs: 0xe2a0
+  __TEXT.__unwind_info: 0x1788
+  __TEXT.__objc_classname: 0xad3
+  __TEXT.__objc_methname: 0x13697
+  __TEXT.__objc_methtype: 0x4090
+  __TEXT.__objc_stubs: 0xe0e0
   __DATA_CONST.__got: 0x3b8
-  __DATA_CONST.__const: 0x1750
-  __DATA_CONST.__objc_classlist: 0x178
+  __DATA_CONST.__const: 0x1730
+  __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_catlist: 0x98
-  __DATA_CONST.__objc_protolist: 0x1b0
+  __DATA_CONST.__objc_protolist: 0x1a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x8ea8
-  __DATA_CONST.__objc_selrefs: 0x4478
-  __AUTH_CONST.__objc_const: 0x15e8
+  __DATA_CONST.__objc_const: 0x8d58
+  __DATA_CONST.__objc_selrefs: 0x4408
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_classrefs: 0x6d8
+  __DATA_CONST.__objc_superrefs: 0x100
+  __AUTH_CONST.__objc_const: 0x15a0
   __AUTH_CONST.__const: 0x720
-  __AUTH_CONST.__cfstring: 0x2040
+  __AUTH_CONST.__cfstring: 0x1f80
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__auth_got: 0x578
-  __AUTH.__objc_data: 0x5a0
-  __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x708
-  __DATA.__objc_superrefs: 0x108
-  __DATA.__objc_ivar: 0x49c
-  __DATA.__data: 0x1440
+  __AUTH.__objc_data: 0x550
+  __DATA.__objc_ivar: 0x488
+  __DATA.__data: 0x13e0
   __DATA.__bss: 0xc8
   __DATA_DIRTY.__objc_data: 0x910
   __DATA_DIRTY.__bss: 0x60

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 48388A0C-B2AA-32EB-AA8B-51EF44AF6ADF
-  Functions: 1916
-  Symbols:   7454
-  CStrings:  4455
+  UUID: 95217BC7-522C-3F7B-9961-CA2DFDCE0647
+  Functions: 1896
+  Symbols:   7383
+  CStrings:  4409
 
Symbols:
+ +[AFUICarPlayUtilities isRequestForAnnounceNotification:]
+ +[AFUICarPlayUtilities isRequestForMessageReadBannerTap:]
+ +[AFUICarPlayUtilities shouldPresentForNewRequest:duringCurrentRequest:]
+ +[AFUICarPlayUtilities shouldStartNewRequest:duringCurrentRequest:]
+ -[AFUISiriSession setSupportsCarPlayVehicleData:]
+ -[AFUISiriViewController setSupportsCarPlayVehicleData:]
+ -[AFUISiriViewController siriSessionDidReactivateFromFlexibleFollowups]
+ -[AFUISiriViewController supportsCarPlayVehicleData]
+ GCC_except_table105
+ GCC_except_table191
+ GCC_except_table194
+ GCC_except_table196
+ GCC_except_table203
+ GCC_except_table219
+ GCC_except_table228
+ GCC_except_table347
+ GCC_except_table350
+ GCC_except_table364
+ GCC_except_table367
+ GCC_except_table369
+ GCC_except_table376
+ GCC_except_table378
+ GCC_except_table380
+ _OBJC_CLASS_$_AFUICarPlayUtilities
+ _OBJC_IVAR_$_AFUISiriViewController._supportsCarPlayVehicleData
+ _OBJC_METACLASS_$_AFUICarPlayUtilities
+ __OBJC_$_CLASS_METHODS_AFUICarPlayUtilities
+ __OBJC_$_PROP_LIST_AFUISceneClientSettings.58
+ __OBJC_CLASS_RO_$_AFUICarPlayUtilities
+ __OBJC_METACLASS_RO_$_AFUICarPlayUtilities
+ _objc_msgSend$setSupportsCarPlayVehicleData:
+ _objc_msgSend$siriSessionDidReactivateFromFlexibleFollowups
+ _objc_msgSend$siriViewControllerDidReactivateFromFlexibleFollowups
- +[AFUIStarkUtilities backgroundViewModeForRequestSource:directActionEvent:]
- +[AFUIStarkUtilities backgroundViewModeForRequestSource:directActionEvent:].cold.1
- +[AFUIStarkUtilities isRequestForAnnnounceNotificationServerCommand:]
- +[AFUIStarkUtilities isRequestForAnnounceNotification:]
- +[AFUIStarkUtilities isRequestForMessageReadBannerTap:]
- +[AFUIStarkUtilities shouldPresentForNewRequest:duringCurrentRequest:]
- +[AFUIStarkUtilities shouldStartNewRequest:duringCurrentRequest:]
- -[AFUISiriCarPlayBackgroundView .cxx_destruct]
- -[AFUISiriCarPlayBackgroundView _animateBackgroundsWithVisibility:backgroundViewMode:]
- -[AFUISiriCarPlayBackgroundView _updateCarPlayStatusBarForVisibility:backgroundViewMode:]
- -[AFUISiriCarPlayBackgroundView _updateViewsForVisibility:backgroundViewMode:]
- -[AFUISiriCarPlayBackgroundView _updateViewsForVisibility:backgroundViewMode:].cold.1
- -[AFUISiriCarPlayBackgroundView backgroundViewMode]
- -[AFUISiriCarPlayBackgroundView initWithDelegate:]
- -[AFUISiriCarPlayBackgroundView isVisible]
- -[AFUISiriCarPlayBackgroundView setBackgroundViewMode:]
- -[AFUISiriCarPlayBackgroundView setVisible:]
- -[AFUISiriCarPlayView backgroundView:requestsCarPlayStatusBarOverride:animationSettings:]
- -[AFUISiriCarPlayView updateBackgroundViewMode:]
- -[AFUISiriCarPlayView updateBackgroundVisibility:]
- -[AFUISiriRemoteSceneViewController setCarDisplaySnippetMode:]
- -[AFUISiriViewController siriRemoteViewController:setCarDisplaySnippetMode:]
- GCC_except_table106
- GCC_except_table186
- GCC_except_table192
- GCC_except_table195
- GCC_except_table198
- GCC_except_table204
- GCC_except_table218
- GCC_except_table243
- GCC_except_table346
- GCC_except_table349
- GCC_except_table363
- GCC_except_table366
- GCC_except_table368
- GCC_except_table375
- GCC_except_table377
- GCC_except_table379
- _AFUIStarkBackgroundViewModeGetName
- _AFUIStarkBackgroundViewModeGetName.cold.1
- _OBJC_CLASS_$_AFUISiriCarPlayBackgroundView
- _OBJC_CLASS_$_AFUIStarkUtilities
- _OBJC_CLASS_$_BSSpringAnimationSettings
- _OBJC_CLASS_$_CRSUIStatusBarStyleAssertion
- _OBJC_CLASS_$_SiriUIUtilities
- _OBJC_IVAR_$_AFUISiriCarPlayBackgroundView._backgroundViewMode
- _OBJC_IVAR_$_AFUISiriCarPlayBackgroundView._delegate
- _OBJC_IVAR_$_AFUISiriCarPlayBackgroundView._fullScreenBackgroundView
- _OBJC_IVAR_$_AFUISiriCarPlayBackgroundView._systemBackgroundView
- _OBJC_IVAR_$_AFUISiriCarPlayBackgroundView._visible
- _OBJC_IVAR_$_AFUISiriCarPlayView._backgroundView
- _OBJC_METACLASS_$_AFUISiriCarPlayBackgroundView
- _OBJC_METACLASS_$_AFUIStarkUtilities
- __OBJC_$_CLASS_METHODS_AFUIStarkUtilities
- __OBJC_$_INSTANCE_METHODS_AFUISiriCarPlayBackgroundView
- __OBJC_$_INSTANCE_VARIABLES_AFUISiriCarPlayBackgroundView
- __OBJC_$_PROP_LIST_AFUISceneClientSettings.57
- __OBJC_$_PROP_LIST_AFUISiriCarPlayBackgroundView
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_AFUISiriCarPlayBackgroundViewDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_AFUISiriCarPlayBackgroundViewDelegate
- __OBJC_$_PROTOCOL_REFS_AFUISiriCarPlayBackgroundViewDelegate
- __OBJC_CLASS_RO_$_AFUISiriCarPlayBackgroundView
- __OBJC_CLASS_RO_$_AFUIStarkUtilities
- __OBJC_LABEL_PROTOCOL_$_AFUISiriCarPlayBackgroundViewDelegate
- __OBJC_METACLASS_RO_$_AFUISiriCarPlayBackgroundView
- __OBJC_METACLASS_RO_$_AFUIStarkUtilities
- __OBJC_PROTOCOL_$_AFUISiriCarPlayBackgroundViewDelegate
- ___86-[AFUISiriCarPlayBackgroundView _animateBackgroundsWithVisibility:backgroundViewMode:]_block_invoke
- _objc_msgSend$_animateBackgroundsWithVisibility:backgroundViewMode:
- _objc_msgSend$_updateCarPlayStatusBarForVisibility:backgroundViewMode:
- _objc_msgSend$_updateViewsForVisibility:backgroundViewMode:
- _objc_msgSend$acquireWithAnimationSettings:
- _objc_msgSend$backgroundView:requestsCarPlayStatusBarOverride:animationSettings:
- _objc_msgSend$backgroundViewMode
- _objc_msgSend$backgroundViewModeForRequestSource:directActionEvent:
- _objc_msgSend$initForSiriPresentation
- _objc_msgSend$reliquishWithAnimationSettings:
- _objc_msgSend$setBackgroundViewMode:
- _objc_msgSend$settingsWithMass:stiffness:damping:
- _objc_msgSend$shouldShowHeaderForDirectActionEvent:
- _objc_msgSend$siriRemoteViewController:setCarDisplaySnippetMode:
- _objc_msgSend$tableBackgroundColor
- _objc_msgSend$updateBackgroundViewMode:
- _objc_msgSend$updateBackgroundVisibility:
- _objc_msgSend$updateVisibility:
CStrings:
+ "2\x13\x11\x81A!\x13g"
+ "AFUICarPlayUtilities"
+ "E"
+ "T@\"NSArray\",?,R,C,N"
+ "T@\"NSString\",?,R,C"
+ "TB,N,GsupportsCarPlayVehicleData,SsetSupportsCarPlayVehicleData:,V_supportsCarPlayVehicleData"
+ "_supportsCarPlayVehicleData"
+ "setSupportsCarPlayVehicleData:"
+ "siriSessionDidReactivateFromFlexibleFollowups"
+ "siriViewControllerDidReactivateFromFlexibleFollowups"
+ "supportsCarPlayVehicleData"
+ "\xf0\xf0R"
- "%s #carPlay #punchout Setting fullscreen background with a foreground inactive scene. Reactivating scene and requesting presentation."
- "%s #carPlay backgroundViewMode should never be set to AFUIStarkBackgroundViewModeUnset"
- "%s #carPlay changing from %@ to %@"
- "%s #carPlay requesting CarPlay's status bar to %@ overriden"
- "%s Unsupported AFUIStarkBackgroundViewMode value: %lu, returning back nil."
- "%s Unsupported SASRequestSource value: %lu, returning back AFUIStarkBackgroundViewModeSmall."
- "+[AFUIStarkUtilities backgroundViewModeForRequestSource:directActionEvent:]"
- "-[AFUISiriCarPlayBackgroundView _updateViewsForVisibility:backgroundViewMode:]"
- "-[AFUISiriCarPlayBackgroundView setBackgroundViewMode:]"
- "-[AFUISiriCarPlayView backgroundView:requestsCarPlayStatusBarOverride:animationSettings:]"
- "-[AFUISiriViewController siriRemoteViewController:setCarDisplaySnippetMode:]"
- "2\x13\x11\x81A!\x13W"
- "@\"<AFUISiriCarPlayBackgroundViewDelegate>\""
- "@\"AFUISiriCarPlayBackgroundView\""
- "@\"AFUISiriCarPlayFullScreenBackgroundView\""
- "AFUISiriCarPlayBackgroundView"
- "AFUISiriCarPlayBackgroundViewDelegate"
- "AFUIStarkBackgroundViewModeFullScreen"
- "AFUIStarkBackgroundViewModeFullScreenSystem"
- "AFUIStarkBackgroundViewModeGetName"
- "AFUIStarkBackgroundViewModeSmall"
- "AFUIStarkBackgroundViewModeUnset"
- "AFUIStarkUtilities"
- "BE"
- "F"
- "NOT BE"
- "Tq,N,V_backgroundViewMode"
- "_animateBackgroundsWithVisibility:backgroundViewMode:"
- "_backgroundViewMode"
- "_fullScreenBackgroundView"
- "_systemBackgroundView"
- "_updateCarPlayStatusBarForVisibility:backgroundViewMode:"
- "_updateViewsForVisibility:backgroundViewMode:"
- "acquireWithAnimationSettings:"
- "backgroundView:requestsCarPlayStatusBarOverride:animationSettings:"
- "backgroundViewMode"
- "backgroundViewModeForRequestSource:directActionEvent:"
- "compact_carplay"
- "initForSiriPresentation"
- "isRequestForAnnnounceNotificationServerCommand:"
- "q32@0:8q16q24"
- "reliquishWithAnimationSettings:"
- "setBackgroundViewMode:"
- "setCarDisplaySnippetMode:"
- "settingsWithMass:stiffness:damping:"
- "shouldShowHeaderForDirectActionEvent:"
- "siriRemoteViewController:setCarDisplaySnippetMode:"
- "tableBackgroundColor"
- "updateBackgroundViewMode:"
- "updateBackgroundVisibility:"
- "v36@0:8@\"AFUISiriCarPlayBackgroundView\"16B24@\"BSAnimationSettings\"28"
- "\xf0\xf0B"

```
