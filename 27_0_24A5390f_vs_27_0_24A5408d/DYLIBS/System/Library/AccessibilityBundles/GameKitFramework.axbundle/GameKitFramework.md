## GameKitFramework

> `/System/Library/AccessibilityBundles/GameKitFramework.axbundle/GameKitFramework`

```diff

-3045.0.0.0.0
-  __TEXT.__text: 0x344
-  __TEXT.__objc_methlist: 0x14
-  __TEXT.__cstring: 0x153
-  __TEXT.__unwind_info: 0x78
+3048.0.0.0.0
+  __TEXT.__text: 0xe84
+  __TEXT.__objc_methlist: 0x124
+  __TEXT.__const: 0x8
+  __TEXT.__cstring: 0x213
+  __TEXT.__unwind_info: 0xc0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x60
-  __DATA_CONST.__objc_classlist: 0x8
+  __DATA_CONST.__const: 0x90
+  __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x58
-  __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0x220
-  __AUTH_CONST.__objc_const: 0x90
+  __DATA_CONST.__objc_selrefs: 0x1f8
+  __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__got: 0x70
+  __AUTH_CONST.__const: 0xc0
+  __AUTH_CONST.__cfstring: 0x360
+  __AUTH_CONST.__objc_const: 0x380
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__bss: 0x10
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0xc
+  __DATA.__bss: 0x20
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/PrivateFrameworks/AXRuntime.framework/AXRuntime
   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
   - /System/Library/PrivateFrameworks/UIAccessibility.framework/UIAccessibility
   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 7
-  Symbols:   49
-  CStrings:  23
+  Functions: 28
+  Symbols:   191
+  CStrings:  33
 
Symbols:
+ +[AXGameKitAccessPointBridge accessPointElementForWindow:]
+ +[AXGameKitAccessPointBridge sharedBridge]
+ +[UIWindowAccessibility__GameKit__UIKit(SafeCategory) safeCategoryBaseClass]
+ +[UIWindowAccessibility__GameKit__UIKit(SafeCategory) safeCategoryTargetClassName]
+ -[AXGameKitAccessPointBridge .cxx_destruct]
+ -[AXGameKitAccessPointBridge _accessibilityAccessPointChanged:]
+ -[AXGameKitAccessPointBridge _attachWithIdentifier:angelPid:]
+ -[AXGameKitAccessPointBridge _detach]
+ -[AXGameKitAccessPointBridge _foregroundSceneForIdentifier:]
+ -[AXGameKitAccessPointBridge _keyWindowForScene:]
+ -[AXGameKitAccessPointBridge attachedWindow]
+ -[AXGameKitAccessPointBridge clientElement]
+ -[AXGameKitAccessPointBridge setAttachedWindow:]
+ -[AXGameKitAccessPointBridge setClientElement:]
+ -[AXGameKitAccessPointElement _accessibilitySortPriority]
+ -[AXGameKitAccessPointElement accessibilityFrame]
+ -[AXGameKitAccessPointElement axOrderingFrame]
+ -[AXGameKitAccessPointElement setAxOrderingFrame:]
+ -[UIWindowAccessibility__GameKit__UIKit _accessibilityAdditionalElements]
+ _AXGameCenterAccessPointDidChangeNotification
+ _NSClassFromString
+ _OBJC_CLASS_$_AXGameKitAccessPointBridge
+ _OBJC_CLASS_$_AXGameKitAccessPointElement
+ _OBJC_CLASS_$_AXRemoteElement
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSNotificationCenter
+ _OBJC_CLASS_$_NSString
+ _OBJC_CLASS_$_UIAccessibilitySafeCategory
+ _OBJC_CLASS_$_UIApplication
+ _OBJC_CLASS_$_UIWindowAccessibility__GameKit__UIKit
+ _OBJC_CLASS_$_UIWindowScene
+ _OBJC_CLASS_$___UIWindowAccessibility__GameKit__UIKit_super
+ _OBJC_IVAR_$_AXGameKitAccessPointBridge._attachedWindow
+ _OBJC_IVAR_$_AXGameKitAccessPointBridge._clientElement
+ _OBJC_IVAR_$_AXGameKitAccessPointElement._axOrderingFrame
+ _OBJC_METACLASS_$_AXGameKitAccessPointBridge
+ _OBJC_METACLASS_$_AXGameKitAccessPointElement
+ _OBJC_METACLASS_$_AXRemoteElement
+ _OBJC_METACLASS_$_UIAccessibilitySafeCategory
+ _OBJC_METACLASS_$_UIWindowAccessibility__GameKit__UIKit
+ _OBJC_METACLASS_$___UIWindowAccessibility__GameKit__UIKit_super
+ _UIAccessibilityConvertFrameToScreenCoordinates
+ _UIAccessibilityLayoutChangedNotification
+ _UIAccessibilityPostNotification
+ __NSConcreteStackBlock
+ __OBJC_$_CLASS_METHODS_AXGameKitAccessPointBridge
+ __OBJC_$_CLASS_METHODS_UIWindowAccessibility__GameKit__UIKit(SafeCategory)
+ __OBJC_$_INSTANCE_METHODS_AXGameKitAccessPointBridge
+ __OBJC_$_INSTANCE_METHODS_AXGameKitAccessPointElement
+ __OBJC_$_INSTANCE_METHODS_UIWindowAccessibility__GameKit__UIKit
+ __OBJC_$_INSTANCE_VARIABLES_AXGameKitAccessPointBridge
+ __OBJC_$_INSTANCE_VARIABLES_AXGameKitAccessPointElement
+ __OBJC_$_PROP_LIST_AXGameKitAccessPointBridge
+ __OBJC_$_PROP_LIST_AXGameKitAccessPointElement
+ __OBJC_CLASS_RO_$_AXGameKitAccessPointBridge
+ __OBJC_CLASS_RO_$_AXGameKitAccessPointElement
+ __OBJC_CLASS_RO_$_UIWindowAccessibility__GameKit__UIKit
+ __OBJC_CLASS_RO_$___UIWindowAccessibility__GameKit__UIKit_super
+ __OBJC_METACLASS_RO_$_AXGameKitAccessPointBridge
+ __OBJC_METACLASS_RO_$_AXGameKitAccessPointElement
+ __OBJC_METACLASS_RO_$_UIWindowAccessibility__GameKit__UIKit
+ __OBJC_METACLASS_RO_$___UIWindowAccessibility__GameKit__UIKit_super
+ ___42+[AXGameKitAccessPointBridge sharedBridge]_block_invoke
+ ___63-[AXGameKitAccessPointBridge _accessibilityAccessPointChanged:]_block_invoke
+ ___block_descriptor_53_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___stack_chk_fail
+ ___stack_chk_guard
+ __dispatch_main_q
+ _dispatch_async
+ _objc_alloc
+ _objc_alloc_init
+ _objc_destroyWeak
+ _objc_enumerationMutation
+ _objc_loadWeakRetained
+ _objc_msgSend$_attachWithIdentifier:angelPid:
+ _objc_msgSend$_detach
+ _objc_msgSend$_foregroundSceneForIdentifier:
+ _objc_msgSend$_keyWindowForScene:
+ _objc_msgSend$accessPointElementForWindow:
+ _objc_msgSend$activationState
+ _objc_msgSend$addObserver:selector:name:object:
+ _objc_msgSend$alpha
+ _objc_msgSend$arrayWithObjects:count:
+ _objc_msgSend$attachedWindow
+ _objc_msgSend$axArrayWithPossiblyNilArrays:
+ _objc_msgSend$axOrderingFrame
+ _objc_msgSend$boolValue
+ _objc_msgSend$bounds
+ _objc_msgSend$clientElement
+ _objc_msgSend$connectedScenes
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$defaultCenter
+ _objc_msgSend$firstObject
+ _objc_msgSend$frameInScreenCoordinates
+ _objc_msgSend$initWithUUID:andRemotePid:andContextId:
+ _objc_msgSend$installSafeCategory:canInteractWithTargetClass:
+ _objc_msgSend$intValue
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$isHidden
+ _objc_msgSend$keyWindow
+ _objc_msgSend$length
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$persistentIdentifier
+ _objc_msgSend$postNotificationName:object:
+ _objc_msgSend$remotePid
+ _objc_msgSend$session
+ _objc_msgSend$setAccessibilityContainer:
+ _objc_msgSend$setAttachedWindow:
+ _objc_msgSend$setAxOrderingFrame:
+ _objc_msgSend$setClientElement:
+ _objc_msgSend$setOnClientSide:
+ _objc_msgSend$sharedApplication
+ _objc_msgSend$sharedBridge
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$unregister
+ _objc_msgSend$userInfo
+ _objc_msgSend$uuid
+ _objc_msgSend$valueForKey:
+ _objc_msgSend$windows
+ _objc_msgSendSuper2
+ _objc_opt_class
+ _objc_opt_isKindOfClass
+ _objc_opt_respondsToSelector
+ _objc_release_x1
+ _objc_release_x21
+ _objc_release_x22
+ _objc_release_x23
+ _objc_release_x24
+ _objc_release_x25
+ _objc_release_x8
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x19
+ _objc_retain_x2
+ _objc_retain_x21
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x8
+ _objc_storeStrong
+ _objc_storeWeak
+ _objc_unsafeClaimAutoreleasedReturnValue
+ _sharedBridge.bridge
+ _sharedBridge.onceToken
Functions:
~ ___55+[AXGameKitFrameworkGlue accessibilityInitializeBundle]_block_invoke : 100 -> 104
~ ___55+[AXGameKitFrameworkGlue accessibilityInitializeBundle]_block_invoke_4 : 4 -> 20
CStrings:
+ "AXGameCenterAccessPointDidChange"
+ "AXGameCenterAccessPointStateRequest"
+ "GKAccessPoint"
+ "UIWindow"
+ "UIWindowAccessibility__GameKit__UIKit"
+ "active"
+ "angelPid"
+ "gc-access-point:%@"
+ "sceneIdentifier"
+ "shared"
```
