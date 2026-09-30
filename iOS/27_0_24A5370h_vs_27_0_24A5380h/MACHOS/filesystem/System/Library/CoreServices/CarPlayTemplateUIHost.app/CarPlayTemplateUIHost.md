## CarPlayTemplateUIHost

> `/System/Library/CoreServices/CarPlayTemplateUIHost.app/CarPlayTemplateUIHost`

```diff

-  __TEXT.__text: 0xd050
+  __TEXT.__text: 0xb280
   __TEXT.__auth_stubs: 0x3e0
-  __TEXT.__objc_stubs: 0x2c20
-  __TEXT.__objc_methlist: 0x138c
-  __TEXT.__const: 0x40
-  __TEXT.__gcc_except_tab: 0x2c0
-  __TEXT.__objc_methname: 0x3e01
-  __TEXT.__oslogstring: 0xd51
-  __TEXT.__cstring: 0x5ce
-  __TEXT.__objc_classname: 0x322
-  __TEXT.__objc_methtype: 0xd01
-  __TEXT.__unwind_info: 0x340
+  __TEXT.__objc_stubs: 0x2680
+  __TEXT.__objc_methlist: 0x110c
+  __TEXT.__const: 0x38
+  __TEXT.__gcc_except_tab: 0x254
+  __TEXT.__objc_methname: 0x35ad
+  __TEXT.__oslogstring: 0xc52
+  __TEXT.__cstring: 0x5ad
+  __TEXT.__objc_classname: 0x29a
+  __TEXT.__objc_methtype: 0xbb2
+  __TEXT.__unwind_info: 0x300
   __DATA_CONST.__const: 0x3d0
-  __DATA_CONST.__cfstring: 0x3e0
-  __DATA_CONST.__objc_classlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x80
+  __DATA_CONST.__cfstring: 0x320
+  __DATA_CONST.__objc_classlist: 0x48
+  __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x50
+  __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__auth_got: 0x200
-  __DATA_CONST.__got: 0x1f0
-  __DATA.__objc_const: 0x3ac8
-  __DATA.__objc_selrefs: 0xf28
-  __DATA.__objc_ivar: 0x144
-  __DATA.__objc_data: 0x370
-  __DATA.__data: 0x600
+  __DATA_CONST.__got: 0x1a8
+  __DATA.__objc_const: 0x3128
+  __DATA.__objc_selrefs: 0xd20
+  __DATA.__objc_ivar: 0x10c
+  __DATA.__objc_data: 0x2d0
+  __DATA.__data: 0x540
   __DATA.__bss: 0x10c
   - /System/Library/Frameworks/CarPlay.framework/CarPlay
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices
-  - /System/Library/PrivateFrameworks/BannerKit.framework/BannerKit
   - /System/Library/PrivateFrameworks/CarKit.framework/CarKit
   - /System/Library/PrivateFrameworks/CarPlayServices.framework/CarPlayServices
   - /System/Library/PrivateFrameworks/CarPlaySupport.framework/CarPlaySupport

   - /System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 369
-  Symbols:   138
-  CStrings:  951
+  Functions: 322
+  Symbols:   129
+  CStrings:  826
 
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_protorefs : content changed
Symbols:
- _CGRectZero
- _OBJC_CLASS_$_BNSceneSettings
- _OBJC_CLASS_$_CARSessionStatus
- _OBJC_CLASS_$_NSURL
- _OBJC_CLASS_$_UILabel
- _OBJC_CLASS_$_UILayoutGuide
- _UISceneDidEnterBackgroundNotification
- _UISceneWillEnterForegroundNotification
- ___NSArray0__struct
CStrings:
- "1"
- "2"
- "3"
- "@\"CARSessionStatus\""
- "@\"CARTemplateUIDashboardButton\""
- "@\"CARTemplateUIHostInstrumentClusterViewController\""
- "@\"CRSUIClusterWindow\""
- "@\"NSXPCConnection\""
- "@\"UIView\""
- "@\"UIWindow\""
- "Banner scene disconnected: %@"
- "Banner scene entering foreground: %@"
- "CARTemplateUIDashboardButton"
- "CARTemplateUIHostDashboardViewController"
- "CRSUIDashboardFocusableItemProviding"
- "Other scene disconnected: %@"
- "Scene entering foreground for client: %@"
- "T@\"CARSessionStatus\",&,N,V_sessionStatus"
- "T@\"CARTemplateUIDashboardButton\",&,N,V_button1"
- "T@\"CARTemplateUIDashboardButton\",&,N,V_button2"
- "T@\"CARTemplateUIDashboardButton\",&,N,V_button3"
- "T@\"CARTemplateUIHostInstrumentClusterViewController\",&,N,V_instrumentClusterViewController"
- "T@\"CRSUIClusterWindow\",&,N,V_instrumentClusterWindow"
- "T@\"CRSUIDashboardWidgetWindow\",&,N,V_largeDashboardWindow"
- "T@\"CRSUIDashboardWidgetWindow\",&,N,V_smallDashboardWindow"
- "T@\"NSArray\",R,N"
- "T@\"NSXPCConnection\",&,N,V_connection"
- "T@\"UIView\",&,N,V_safeView"
- "T@\"UIWindow\",&,N,V_mainWindow"
- "T@\"UIWindow\",W,N,V_activeWindow"
- "T@\"UIWindowScene\",W,N,V_activeBannerScene"
- "UIApplicationDelegatePrivate"
- "URLWithString:"
- "Unable to find environment for scene: %@"
- "Unexpected scene entering foreground: %@"
- "You are using: %@"
- "_activeBannerScene"
- "_activeWindow"
- "_application:handleSiriTask:"
- "_application:statusBarTouchesEnded:"
- "_button1"
- "_button1Triggered"
- "_button2"
- "_button2Triggered"
- "_button3"
- "_button3Triggered"
- "_connection"
- "_instrumentClusterViewController"
- "_instrumentClusterWindow"
- "_largeDashboardWindow"
- "_mainWindow"
- "_safeView"
- "_sceneDidDidEnterBackground:"
- "_sceneWillEnterForeground:"
- "_sessionStatus"
- "_smallDashboardWindow"
- "activeBannerScene"
- "activeWindow"
- "addLayoutGuide:"
- "addTarget:action:forControlEvents:"
- "application:didFinishLaunchingSuspendedWithOptions:"
- "application:userAcceptedCloudKitShareWithMetadata:"
- "blueColor"
- "button1"
- "button2"
- "button3"
- "buttonWithType:"
- "centerXAnchor"
- "centerYAnchor"
- "connection"
- "constraintEqualToAnchor:constant:"
- "constraintLessThanOrEqualToAnchor:constant:"
- "currentSession"
- "focusableItemFocused:"
- "focusableItemPressed:"
- "focusableItemSelected"
- "initAndWaitUntilSessionUpdated"
- "initWithFrame:"
- "instrumentClusterViewController"
- "instrumentClusterWindow"
- "largeDashboardWindow"
- "mainWindow"
- "maps:"
- "redColor"
- "safeAreaLayoutGuide"
- "safeView"
- "scene: (%@) didUpdateSettings: (%@)"
- "sendActionsForControlEvents:"
- "sessionStatus"
- "setActiveBannerScene:"
- "setActiveWindow:"
- "setBackgroundColor:"
- "setButton1:"
- "setButton2:"
- "setButton3:"
- "setConnection:"
- "setFocusableViews:"
- "setHighlighted:"
- "setInstrumentClusterViewController:"
- "setInstrumentClusterWindow:"
- "setLargeDashboardWindow:"
- "setMainWindow:"
- "setNumberOfLines:"
- "setSafeView:"
- "setSessionStatus:"
- "setSmallDashboardWindow:"
- "setTextAlignment:"
- "setTextColor:"
- "setTintColor:"
- "setTitle:forState:"
- "smallDashboardWindow"
- "suggestUI:"
- "v32@0:8@\"UIApplication\"16@\"AFSiriTask\"24"
- "v32@0:8@\"UIApplication\"16@\"CKShareMetadata\"24"
- "v32@0:8@\"UIApplication\"16@\"NSDictionary\"24"
- "v32@0:8@\"UIApplication\"16@\"UIEvent\"24"
- "viewDidAppear:"
- "whiteColor"
- "yellowColor"

```
