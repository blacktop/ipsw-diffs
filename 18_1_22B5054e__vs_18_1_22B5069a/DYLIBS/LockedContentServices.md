## LockedContentServices

> `/System/Library/PrivateFrameworks/LockedContentServices.framework/LockedContentServices`

```diff

-58.1.1.0.0
-  __TEXT.__text: 0x81e4
+58.1.3.101.0
+  __TEXT.__text: 0x9204
   __TEXT.__auth_stubs: 0x480
-  __TEXT.__objc_methlist: 0x56c
+  __TEXT.__objc_methlist: 0x71c
   __TEXT.__const: 0xa8
-  __TEXT.__gcc_except_tab: 0x1f8
-  __TEXT.__cstring: 0x5ff
-  __TEXT.__oslogstring: 0xbb1
-  __TEXT.__unwind_info: 0x290
-  __TEXT.__objc_classname: 0x1b1
-  __TEXT.__objc_methname: 0x1b0f
-  __TEXT.__objc_methtype: 0x57a
-  __TEXT.__objc_stubs: 0x1600
-  __DATA_CONST.__got: 0x1a8
-  __DATA_CONST.__const: 0x318
-  __DATA_CONST.__objc_classlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x68
+  __TEXT.__gcc_except_tab: 0x22c
+  __TEXT.__oslogstring: 0xc19
+  __TEXT.__cstring: 0x64d
+  __TEXT.__unwind_info: 0x2e0
+  __TEXT.__objc_classname: 0x233
+  __TEXT.__objc_methname: 0x2213
+  __TEXT.__objc_methtype: 0x680
+  __TEXT.__objc_stubs: 0x1ae0
+  __DATA_CONST.__got: 0x208
+  __DATA_CONST.__const: 0x368
+  __DATA_CONST.__objc_classlist: 0x50
+  __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x658
-  __DATA_CONST.__objc_superrefs: 0x38
+  __DATA_CONST.__objc_selrefs: 0x828
+  __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0x28
   __AUTH_CONST.__auth_got: 0x250
   __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0x4e0
-  __AUTH_CONST.__objc_const: 0x2290
+  __AUTH_CONST.__cfstring: 0x540
+  __AUTH_CONST.__objc_const: 0x2960
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x98
-  __DATA.__data: 0x4e0
+  __AUTH.__objc_data: 0x190
+  __DATA.__objc_ivar: 0xbc
+  __DATA.__data: 0x5a0
   __DATA.__bss: 0x28
   __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__bss: 0x30

   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/AppProtection.framework/AppProtection
+  - /System/Library/PrivateFrameworks/AppProtectionUI.framework/AppProtectionUI
   - /System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
+  - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
   - /System/Library/PrivateFrameworks/LinkMetadata.framework/LinkMetadata
   - /System/Library/PrivateFrameworks/LinkServices.framework/LinkServices
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag

   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 204
-  Symbols:   356
-  CStrings:  489
+  Functions: 241
+  Symbols:   409
+  CStrings:  585
 
Symbols:
+ _OBJC_CLASS_$_APBaseExtensionShieldView
+ _OBJC_CLASS_$_APExtension
+ _OBJC_CLASS_$_APExtensionSubjectMonitorRegistry
+ _OBJC_CLASS_$_APGuard
+ _OBJC_CLASS_$_BSDescriptionBuilder
+ _OBJC_CLASS_$_ISIcon
+ _OBJC_CLASS_$_ISImageDescriptor
+ _OBJC_CLASS_$_LCSAppProtectionShieldViewController
+ _OBJC_CLASS_$_LCSExtensionAppProtectionAssistant
+ _OBJC_CLASS_$_LSApplicationRecord
+ _OBJC_CLASS_$_UIImage
+ _OBJC_CLASS_$_UIViewController
+ _OBJC_METACLASS_$_LCSAppProtectionShieldViewController
+ _OBJC_METACLASS_$_LCSExtensionAppProtectionAssistant
+ _OBJC_METACLASS_$_UIViewController
+ __dispatch_main_q
CStrings:
+ "\x02"
+ "\x04\x13"
+ "\x15"
+ "%!{(MISSING)public}@ will request unshielding"
+ "@\"<APSubjectMonitorSubscription>\""
+ "@\"APBaseExtensionShieldView\""
+ "@\"APExtension\""
+ "@\"APExtensionSubjectMonitorRegistry\""
+ "@\"LCSExtension\""
+ "@\"LCSExtensionAppProtectionAssistant\""
+ "APBaseExtensionShieldViewDelegate"
+ "APSubjectMonitor"
+ "AppProtectionLocalizedDescription"
+ "CGImage"
+ "LCSAppProtectionShieldViewController"
+ "LCSExtensionAppProtectionAssistant"
+ "T@\"<APSubjectMonitorSubscription>\",&,N,V_subscription"
+ "T@\"APBaseExtensionShieldView\",&,N,V_shieldView"
+ "T@\"APExtension\",&,N,V_appProtectionExtension"
+ "T@\"APExtensionSubjectMonitorRegistry\",&,N,V_appProtectionRegistry"
+ "T@\"LCSExtension\",&,N,V_extension"
+ "T@\"LCSExtensionAppProtectionAssistant\",&,N,V_assistant"
+ "T@\"NSHashTable\",R,N,V_observers"
+ "T@\"NSString\",R,C,N"
+ "T@\"NSString\",R,C,N,V_localizedDisplayName"
+ "TB,R,N,V_shouldShield"
+ "_appProtectionExtension"
+ "_appProtectionRegistry"
+ "_assistant"
+ "_canShowWhileLocked"
+ "_localizedDisplayName"
+ "_observers"
+ "_shieldView"
+ "_shouldShield"
+ "_subscription"
+ "addMonitor:"
+ "addSubview:"
+ "allObjects"
+ "appProtectionExtension"
+ "appProtectionRegistry"
+ "appProtectionSubjectsChanged:forSubscription:"
+ "appendBodySectionWithName:multilinePrefix:block:"
+ "appendBool:withName:ifEqualTo:"
+ "appendString:withName:"
+ "applicationIconImage"
+ "assistant"
+ "authenticateForExtension:reasonDescription:completion:"
+ "authenticateForSubject: %!@(MISSING) with success: %!{(MISSING)BOOL}u error: %!{(MISSING)public}@"
+ "bounds"
+ "build"
+ "builderWithObject:"
+ "bundleForClass:"
+ "createShieldUIViewController"
+ "descriptionBuilderWithMultilinePrefix:"
+ "descriptionWithMultilinePrefix:"
+ "extensionAppProtectionAssistantShouldShieldDidChange:"
+ "imageWithCGImage:scale:orientation:"
+ "initWithApplicationExtensionRecord:"
+ "initWithAssistant:"
+ "initWithBundleIdentifier:"
+ "initWithExtension:"
+ "initWithExtensionSubject:"
+ "initWithLocalizedApplicationName:iconImage:"
+ "initWithNibName:bundle:"
+ "initWithSize:scale:"
+ "isEffectivelyLocked"
+ "localizedDisplayName"
+ "localizedName"
+ "localizedStringForKey:value:table:"
+ "observers"
+ "prepareImageForDescriptor:"
+ "requestUnshielding"
+ "scale"
+ "setAppProtectionExtension:"
+ "setAppProtectionRegistry:"
+ "setAssistant:"
+ "setAutoresizingMask:"
+ "setDrawBorder:"
+ "setExtension:"
+ "setFrame:"
+ "setShieldView:"
+ "setSubscription:"
+ "sharedGuard"
+ "shieldView"
+ "shieldViewUnlockButtonPressed:"
+ "shouldShield"
+ "subscription"
+ "succinctDescription"
+ "succinctDescriptionBuilder"
+ "v20@?0B8@\"NSError\"12"
+ "v24@0:8@\"APBaseExtensionShieldView\"16"
+ "v32@0:8@\"NSArray\"16@\"<APSubjectMonitorSubscription>\"24"
+ "view"
+ "viewDidLoad"

```
