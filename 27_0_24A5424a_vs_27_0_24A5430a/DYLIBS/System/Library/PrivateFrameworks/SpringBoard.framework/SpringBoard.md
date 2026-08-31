## SpringBoard

> `/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`

```diff

-4636.112.0.0.0
-  __TEXT.__text: 0xb09e38
+4636.115.0.0.0
+  __TEXT.__text: 0xb0a100
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xbdb48
+  __TEXT.__objc_methlist: 0xbdc30
   __TEXT.__const: 0x11270
-  __TEXT.__oslogstring: 0x64eda
+  __TEXT.__oslogstring: 0x64e7b
   __TEXT.__cstring: 0x84f3f
   __TEXT.__gcc_except_tab: 0x18640
   __TEXT.__ustring: 0xd04
   __TEXT.__dlopen_cstrs: 0x373
-  __TEXT.__unwind_info: 0x2e530
+  __TEXT.__unwind_info: 0x2e548
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0x54d0
   __DATA_CONST.__objc_catlist: 0x338
   __DATA_CONST.__objc_nlcatlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x2ad0
+  __DATA_CONST.__objc_protolist: 0x2ad8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4e8b0
+  __DATA_CONST.__objc_selrefs: 0x4e920
   __DATA_CONST.__objc_protorefs: 0xd8
   __DATA_CONST.__objc_superrefs: 0x4088
   __DATA_CONST.__objc_arraydata: 0x1888
   __DATA_CONST.__got: 0xa900
   __AUTH_CONST.__const: 0x10b88
   __AUTH_CONST.__cfstring: 0x746a0
-  __AUTH_CONST.__objc_const: 0x2879f0
+  __AUTH_CONST.__objc_const: 0x287bc8
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x1728
   __AUTH_CONST.__objc_doubleobj: 0x850

   __AUTH_CONST.__auth_got: 0x2bc0
   __AUTH.__objc_data: 0xe470
   __DATA.__objc_ivar: 0xfc5c
-  __DATA.__data: 0x20ec0
+  __DATA.__data: 0x20f20
   __DATA.__common: 0xa40
   __DATA_DIRTY.__objc_data: 0x26bb0
   __DATA_DIRTY.__data: 0x140

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libutil.dylib
-  Functions: 73497
-  Symbols:   152045
-  CStrings:  23492
+  Functions: 73508
+  Symbols:   152075
+  CStrings:  23491
 
Symbols:
+ -[SBDeviceApplicationAppRestrictionSceneOverlayViewProvider _hostWouldPresentLiveContentIfReady]
+ -[SBDeviceApplicationAppRestrictionSceneOverlayViewProvider _makePreflightViewController]
+ -[SBDeviceApplicationAppRestrictionSceneOverlayViewProvider _updateActivation]
+ -[SBDeviceApplicationAppRestrictionSceneOverlayViewProvider noteDisplayModeChange:]
+ -[SBDeviceApplicationAppRestrictionSceneOverlayViewProvider noteLiveContentDisableReasonsChanged]
+ -[SBDeviceApplicationAppRestrictionSceneOverlayViewProvider sceneHandle:didCreateScene:]
+ -[SBDeviceApplicationAppRestrictionSceneOverlayViewProvider sceneHandle:didDestroyScene:]
+ -[SBDeviceApplicationSceneOverlayViewProvider noteLiveContentDisableReasonsChanged]
+ -[SBDeviceApplicationSceneViewController overlayViewProviderHostDisplayMode:]
+ -[SBDeviceApplicationSceneViewController overlayViewProviderHostLiveContentDisableReasons:]
+ -[SBDeviceApplicationSceneViewController overlayViewProviderHostPresentationPriority:]
+ -[SBDeviceApplicationSceneViewController sceneViewDidChangeLiveContentDisableReasons:]
+ -[SBRecordingIndicatorManager _systemApertureHighLevelGainMapDefeatingLayer]
+ -[SBRecordingIndicatorSystemApertureElement highLevelContainerRenderingConfigurationDidChange:]
+ -[SBRecordingIndicatorViewController highLevelGainMapDefeatingLayer]
+ GCC_except_table110
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBSystemApertureHighLevelContainerRenderingObserving
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBSystemApertureHighLevelContainerRenderingObserving
+ __OBJC_$_PROTOCOL_REFS_SBSystemApertureHighLevelContainerRenderingObserving
+ __OBJC_LABEL_PROTOCOL_$_SBSystemApertureHighLevelContainerRenderingObserving
+ __OBJC_PROTOCOL_$_SBSystemApertureHighLevelContainerRenderingObserving
+ _objc_msgSend$_hostWouldPresentLiveContentIfReady
+ _objc_msgSend$_makePreflightViewController
+ _objc_msgSend$_systemApertureHighLevelGainMapDefeatingLayer
+ _objc_msgSend$_updateActivation
+ _objc_msgSend$highLevelContainerRenderingConfigurationDidChange:
+ _objc_msgSend$highLevelGainMapDefeatingLayer
+ _objc_msgSend$hostingPriority
+ _objc_msgSend$initWithPreflightingScene:presentationPriority:
+ _objc_msgSend$liveContentDisableReasons
+ _objc_msgSend$noteLiveContentDisableReasonsChanged
+ _objc_msgSend$overlayViewProviderHostDisplayMode:
+ _objc_msgSend$overlayViewProviderHostLiveContentDisableReasons:
+ _objc_msgSend$overlayViewProviderHostPresentationPriority:
- -[SBDeviceApplicationAppRestrictionSceneOverlayViewProvider sceneDidInvalidate:]
- -[SBDeviceApplicationAppRestrictionSceneOverlayViewProvider sceneManager:didAddScene:]
- _OUTLINED_FUNCTION_36
- _OUTLINED_FUNCTION_37
CStrings:
+ "[%{public}@] didCreateScene"
+ "[%{public}@] didDestroyScene"
+ "[%{public}@] init without scene; waiting for scene creation"
- "[%{public}@] didAddScene"
- "[%{public}@] init without scene; waiting for scene manager"
- "[%{public}@] requiresPreflight = NO; waiting for preflight callback"
- "[%{public}@] requiresPreflight = YES; attempting activation"
```
