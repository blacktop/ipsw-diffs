## AutomationNotificationContent

> `/private/var/staged_system_apps/Shortcuts.app/PlugIns/AutomationNotificationContent.appex/AutomationNotificationContent`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-5111.0.2.0.0
-  __TEXT.__text: 0x230
-  __TEXT.__auth_stubs: 0x100
-  __TEXT.__objc_stubs: 0x180
+5113.0.1.1.1
+  __TEXT.__text: 0x3dc
+  __TEXT.__auth_stubs: 0x160
+  __TEXT.__objc_stubs: 0x280
   __TEXT.__objc_methlist: 0x1a4
   __TEXT.__const: 0x8
   __TEXT.__oslogstring: 0x48
   __TEXT.__cstring: 0x4b
   __TEXT.__objc_classname: 0x56
-  __TEXT.__objc_methname: 0x31e
+  __TEXT.__objc_methname: 0x3c1
   __TEXT.__objc_methtype: 0x159
   __TEXT.__unwind_info: 0x68
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x88
-  __DATA_CONST.__got: 0x18
+  __DATA_CONST.__auth_got: 0xb8
+  __DATA_CONST.__got: 0x40
   __DATA.__objc_const: 0x2c8
-  __DATA.__objc_selrefs: 0x150
+  __DATA.__objc_selrefs: 0x190
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x50
   __DATA.__data: 0xc0
+  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 4
-  Symbols:   26
-  CStrings:  78
+  Symbols:   37
+  CStrings:  86
 
Symbols:
+ _OBJC_CLASS_$_WFDatabase
+ _OBJC_CLASS_$_WFInitialization
+ _WFMakeAutomationNotificationListViewController
+ _WFNotificationAutomationsEnabledCategory
+ _WFNotificationTriggerNotifyBackgroundCategory
+ _WFTriggerKeysToDisableFromNotificationUserInfo
+ ___NSArray0__struct
+ _objc_release_x24
+ _objc_release_x25
+ _objc_release_x26
+ _objc_retain_x8
Functions:
~ sub_100000d9c -> sub_100000dfc : 420 -> 848
CStrings:
+ "addChildViewController:"
+ "count"
+ "defaultDatabase"
+ "didMoveToParentViewController:"
+ "initializeProcessWithDatabase:"
+ "preferredContentSize"
+ "setPreferredContentSize:"
+ "userInfo"
```
