## CarPlayTemplateUIHost

> `/System/Library/CoreServices/CarPlayTemplateUIHost.app/CarPlayTemplateUIHost`

```diff

-581.7.2.0.0
-  __TEXT.__text: 0xaf68
-  __TEXT.__auth_stubs: 0x3e0
-  __TEXT.__objc_stubs: 0x26a0
-  __TEXT.__objc_methlist: 0x110c
-  __TEXT.__const: 0x38
-  __TEXT.__gcc_except_tab: 0x254
-  __TEXT.__objc_methname: 0x35ca
-  __TEXT.__oslogstring: 0xc52
-  __TEXT.__cstring: 0x5bf
-  __TEXT.__objc_classname: 0x29a
-  __TEXT.__objc_methtype: 0xbb2
-  __TEXT.__unwind_info: 0x3c0
-  __DATA_CONST.__const: 0x410
-  __DATA_CONST.__cfstring: 0x320
-  __DATA_CONST.__objc_classlist: 0x48
-  __DATA_CONST.__objc_protolist: 0x70
+591.2.0.0.0
+  __TEXT.__text: 0xa620
+  __TEXT.__auth_stubs: 0x3c0
+  __TEXT.__objc_stubs: 0x2620
+  __TEXT.__objc_methlist: 0x118c
+  __TEXT.__cstring: 0x59a
+  __TEXT.__const: 0x30
+  __TEXT.__objc_methname: 0x3563
+  __TEXT.__oslogstring: 0xcd2
+  __TEXT.__objc_classname: 0x2d1
+  __TEXT.__objc_methtype: 0xc40
+  __TEXT.__gcc_except_tab: 0x1b8
+  __TEXT.__unwind_info: 0x3b0
+  __DATA_CONST.__const: 0x3e8
+  __DATA_CONST.__cfstring: 0x380
+  __DATA_CONST.__objc_classlist: 0x58
+  __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x40
-  __DATA_CONST.__auth_got: 0x200
-  __DATA_CONST.__got: 0x1a8
-  __DATA.__objc_const: 0x3128
-  __DATA.__objc_selrefs: 0xd28
-  __DATA.__objc_ivar: 0x10c
-  __DATA.__objc_data: 0x2d0
-  __DATA.__data: 0x540
+  __DATA_CONST.__objc_superrefs: 0x48
+  __DATA_CONST.__auth_got: 0x1f0
+  __DATA_CONST.__got: 0x1b0
+  __DATA.__objc_const: 0x3538
+  __DATA.__objc_selrefs: 0xd20
+  __DATA.__objc_ivar: 0x104
+  __DATA.__objc_data: 0x370
+  __DATA.__data: 0x4e0
   - /System/Library/Frameworks/CarPlay.framework/CarPlay
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 323
-  Symbols:   129
-  CStrings:  802
+  Functions: 318
+  Symbols:   133
+  CStrings:  807
 
Symbols:
+ _CGRectGetHeight
+ _OBJC_CLASS_$_CRSUIDashboardWidgetSceneSettings
+ _OBJC_CLASS_$_CRSUIProxyApplicationSceneSpecification
+ _OBJC_CLASS_$_CRSUITemplateInstrumentClusterSceneSpecification
+ _OBJC_CLASS_$_FBSSceneComponent
+ _OBJC_CLASS_$_FBSSceneExtension
+ _OBJC_CLASS_$_UIScene
+ _OBJC_METACLASS_$_FBSSceneComponent
+ _OBJC_METACLASS_$_FBSSceneExtension
- _OBJC_CLASS_$_CRSUIApplicationSceneSettingsDiffInspector
- _UISceneDidDisconnectNotification
- __Block_object_dispose
- _objc_opt_new
- _objc_retain_x26
CStrings:
+ ","
+ "@\"CARTemplateUIAppEnvironment\""
+ "@\"NSSet\"32@0:8@\"FBSScene\"16@\"NSSet\"24"
+ "@28@0:8@16B24"
+ "CARTemplateUIAppEnvironmentClientSceneComponent"
+ "CARTemplateUIAppEnvironmentDelegate"
+ "CARTemplateUIAppEnvironmentSceneExtension"
+ "FBSSceneObserver"
+ "Failed to obtain environment for %{public}@"
+ "No"
+ "Nothing playing, but %{public}@ has no overlay view controller to pop"
+ "Nothing playing; popping %{public}@ to its root template"
+ "Received scene without proxied application bundle identifier %@"
+ "Requesting now playing template for %{public}@"
+ "Should show map widget turn card: %{public}@ (view height: %{public}.1f)"
+ "T@\"<CARTemplateUIAppEnvironmentDelegate>\",&,N"
+ "T@\"CARTemplateUIAppEnvironment\",R,N"
+ "T@\"CARTemplateUIAppEnvironment\",R,N,V_environment"
+ "Yes"
+ "_environment"
+ "_installMapWidgetGuidanceCard"
+ "_invalidateEnvironmentForBundleIdentifier:"
+ "_removeMapWidgetGuidanceCard"
+ "_sceneForFBSScene:"
+ "_sceneFrame"
+ "addLocalExtensions:"
+ "appEnvironmentDidActivate"
+ "appEnvironmentDidDeactivate"
+ "clientComponents"
+ "clientScene"
+ "componentForExtension:ofClass:"
+ "crsui_proxiedApplicationBundleIdentifier"
+ "delegate"
+ "environment"
+ "environmentForBundleIdentifier:createIfNecessary:"
+ "isViewLoaded"
+ "popToRootTemplateAnimated:completion:"
+ "scene:didUpdateHostHandle:"
+ "sceneSettingsDidChange:"
+ "sceneWillInvalidate:"
+ "setInterfaceOrientationMode:"
+ "show-root"
+ "specification"
+ "templateAppEnvironment"
+ "v24@0:8@\"FBSScene\"16"
+ "v32@0:8@\"FBSScene\"16@\"FBSSceneHostHandle\"24"
+ "v32@0:8@\"FBSScene\"16@\"FBSSceneUpdate\"24"
+ "windowSceneDisconnected:"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"
+ "\xf1"
- "-"
- "@\"CRSUIApplicationSceneSettingsDiffInspector\""
- "@\"NSNumber\"16@0:8"
- "CRSUIFrameRateLimitProviding"
- "CRSUIMapStyleProviding"
- "CRSUIMutableFrameRateLimitProviding"
- "Environment %{public}@ will invalidate windowScene: %{public}@"
- "Scene did disconnect for identifier: %@, env: %@"
- "T@\"CRSUIApplicationSceneSettingsDiffInspector\",&,N,V_appSettingsDiffInspector"
- "T@\"NSMutableDictionary\",&,N,V_identifierToEnvironmentMap"
- "T@\"NSNumber\",N"
- "T@\"NSNumber\",R,N"
- "Tq,R,N"
- "Updating frameRateLimit on template app scene"
- "Updating frameRateLimit on template scene"
- "Updating running assertion"
- "_appSettingsDiffInspector"
- "_environmentForIdentifierCreateIfNecessary:"
- "_frameRateLimit"
- "_identifierToEnvironmentMap"
- "_invalidateEnvironmentForIdentifierIfNecessary:"
- "_mapStyle"
- "_sceneDidDisconnect:"
- "_updateRunningAssertionIfNecessary"
- "addObserver:selector:name:object:"
- "appSettingsDiffInspector"
- "didConnectScene:options:"
- "frameRateLimit"
- "identifierToEnvironmentMap"
- "invalidateWindowScene:"
- "mapStyle"
- "object"
- "objectForKeyedSubscript:"
- "observeFrameRateLimitWithBlock:"
- "observeMapStyleWithBlock:"
- "ownsWindowScene:"
- "proxiedApplicationBundleIdentifier"
- "setAppSettingsDiffInspector:"
- "setFrameRateLimit:"
- "setIdentifierToEnvironmentMap:"
- "setMapStyle:"
- "setObject:forKeyedSubscript:"
- "sharedApplication"
- "v24@0:8@\"NSNumber\"16"
- "v32@?0@\"NSString\"8@\"CARTemplateUIAppEnvironment\"16^B24"
```
