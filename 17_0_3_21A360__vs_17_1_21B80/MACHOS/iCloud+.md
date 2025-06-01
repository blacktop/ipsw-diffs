## iCloud+

> `/Applications/iCloud+.app/iCloud+`

```diff

-301.21.0.16.0
-  __TEXT.__text: 0xff0
-  __TEXT.__auth_stubs: 0x1f0
-  __TEXT.__objc_stubs: 0x460
-  __TEXT.__objc_methlist: 0xdc
-  __TEXT.__const: 0x40
-  __TEXT.__oslogstring: 0x247
-  __TEXT.__cstring: 0xff
-  __TEXT.__objc_classname: 0x58
-  __TEXT.__objc_methname: 0xde7
-  __TEXT.__objc_methtype: 0x966
-  __TEXT.__unwind_info: 0xa0
-  __DATA_CONST.__auth_got: 0x100
-  __DATA_CONST.__got: 0x20
+301.21.1.3.0
+  __TEXT.__text: 0x1520
+  __TEXT.__auth_stubs: 0x210
+  __TEXT.__objc_stubs: 0x640
+  __TEXT.__objc_methlist: 0x130
+  __TEXT.__const: 0x48
+  __TEXT.__oslogstring: 0x26d
+  __TEXT.__cstring: 0x11b
+  __TEXT.__objc_classname: 0x78
+  __TEXT.__objc_methname: 0x104b
+  __TEXT.__objc_methtype: 0xa06
+  __TEXT.__unwind_info: 0xb4
+  __DATA_CONST.__auth_got: 0x110
+  __DATA_CONST.__got: 0x60
   __DATA_CONST.__const: 0x50
-  __DATA_CONST.__cfstring: 0xa0
+  __DATA_CONST.__cfstring: 0x100
   __DATA_CONST.__objc_classlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x10
+  __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0xc10
-  __DATA.__objc_selrefs: 0x130
-  __DATA.__objc_classrefs: 0x40
+  __DATA.__objc_const: 0x1030
+  __DATA.__objc_selrefs: 0x1c8
+  __DATA.__objc_classrefs: 0x68
+  __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0xf0
-  __DATA.__data: 0xc0
+  __DATA.__data: 0x120
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp
+  - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/iCloudQuota.framework/iCloudQuota
   - /System/Library/PrivateFrameworks/iCloudQuotaUI.framework/iCloudQuotaUI
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F8C29D0F-35D9-39E8-A358-EFF0182C2CAA
-  Functions: 26
-  Symbols:   50
-  CStrings:  222
+  UUID: E3881F77-FC3C-3805-87A5-3F082866FC33
+  Functions: 37
+  Symbols:   65
+  CStrings:  258
 
Symbols:
+ _FBSOpenApplicationOptionKeyPromptUnlockDevice
+ _ICQActionParameterDismissLockScreenKey
+ _ICQActionParameterFollowUpIdentifierKey
+ _ICQActionParameterSkipCFUKey
+ _ICQBundleId
+ _ICQiCloudSettingsUniversalURL
+ _OBJC_CLASS_$_FLFollowUpController
+ _OBJC_CLASS_$_ICQOffer
+ _OBJC_CLASS_$_ICQUpgradeFlowManager
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSString
+ ___kCFBooleanTrue
+ __dispatch_main_q
+ _dispatch_async
+ _objc_storeStrong
- _OBJC_CLASS_$_ICQUpgradeFlowPresenter
CStrings:
+ ""
+ "\x01"
+ "-[ICQLinkAppDelegate handleSkipCFUWithURL:]"
+ "-[ICQLinkAppDelegate launchFlowWithContext:]"
+ ".cxx_destruct"
+ "/%@"
+ "@\"ICQUpgradeFlowManager\""
+ "ICQUpgradeFlowManagerDelegate"
+ "Launching freshmint flow with context: %@"
+ "Unable to launch URL %@"
+ "Upgrade flow cancelled."
+ "Upgrade flow completed."
+ "Upgrade flow failed with error: %@"
+ "_upgradeFlowManager"
+ "beginFlowWithPresentingViewController:"
+ "date"
+ "dictionaryWithObjects:forKeys:count:"
+ "handleSkipCFUWithURL:"
+ "icq_URLByAppendingQueryParamName:value:"
+ "icq_dismissFollowUpWithIdentifier:"
+ "icq_queryItemForName:"
+ "initSubclassWithOffer:"
+ "initWithServerDictionary:accountAltDSID:notificationID:retrievalDate:callbackInterval:bundleIdentifier:"
+ "launchFlowWithContext:"
+ "launchURLWithDeviceUnlockPrompt:"
+ "manager:loadDidFailWithError:"
+ "setContext:"
+ "setDelegate:"
+ "setFlowOptions:"
+ "stringByAppendingString:"
+ "stringWithFormat:"
+ "true"
+ "upgradeFlowManager:didPresentViewController:"
+ "upgradeFlowManagerDidCancel:"
+ "upgradeFlowManagerDidComplete:"
+ "upgradeFlowManagerDidFail:error:"
+ "v24@0:8@\"ICQUpgradeFlowManager\"16"
+ "v32@0:8@\"ICQUpgradeFlowManager\"16@\"NSError\"24"
+ "v32@0:8@\"ICQUpgradeFlowManager\"16@\"UIViewController\"24"
+ "v8@?0"
+ "value"
- "-[ICQLinkAppDelegate launchFlowWithContext:completion:]"
- "Flow returned"
- "Freshmint Flow ended with success = %d and error = %@"
- "Launching Freshmint Flow with context = %@"
- "launchFlowWithContext:completion:"
- "presentFlowWithContext:completion:"
- "v20@?0B8@\"NSError\"12"

```
