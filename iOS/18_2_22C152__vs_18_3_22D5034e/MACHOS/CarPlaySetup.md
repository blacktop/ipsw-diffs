## CarPlaySetup

> `/Applications/CarPlaySetup.app/CarPlaySetup`

```diff

-596.10.0.0.0
-  __TEXT.__text: 0x5d38
+596.13.0.0.0
+  __TEXT.__text: 0x6500
   __TEXT.__auth_stubs: 0x330
-  __TEXT.__objc_stubs: 0xcc0
-  __TEXT.__objc_methlist: 0x41c
+  __TEXT.__objc_stubs: 0xd80
+  __TEXT.__objc_methlist: 0x44c
   __TEXT.__const: 0x60
   __TEXT.__objc_classname: 0x169
-  __TEXT.__objc_methname: 0x2387
-  __TEXT.__objc_methtype: 0x1000
-  __TEXT.__oslogstring: 0x8e3
-  __TEXT.__cstring: 0x113
+  __TEXT.__objc_methname: 0x24f5
+  __TEXT.__objc_methtype: 0x103d
+  __TEXT.__oslogstring: 0x9cf
+  __TEXT.__cstring: 0x140
   __TEXT.__gcc_except_tab: 0x54
-  __TEXT.__unwind_info: 0x1e0
+  __TEXT.__unwind_info: 0x1e8
   __DATA_CONST.__auth_got: 0x1a8
-  __DATA_CONST.__got: 0xf0
+  __DATA_CONST.__got: 0x110
   __DATA_CONST.__const: 0x3b0
-  __DATA_CONST.__cfstring: 0xc0
+  __DATA_CONST.__cfstring: 0xe0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA.__objc_const: 0x21b8
-  __DATA.__objc_selrefs: 0x450
+  __DATA.__objc_const: 0x2238
+  __DATA.__objc_selrefs: 0x490
   __DATA.__objc_ivar: 0x28
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x3c0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard

   - /System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 152
-  Symbols:   94
-  CStrings:  450
+  Functions: 161
+  Symbols:   98
+  CStrings:  466
 
Symbols:
+ _OBJC_CLASS_$_CARSetupAssetUnavailableViewController
+ _OBJC_CLASS_$_LSApplicationWorkspace
+ _OBJC_CLASS_$_NSURL
+ ___NSDictionary0__struct
CStrings:
+ "URLWithString:"
+ "asset unavailable prompt received response: %{public}@"
+ "asset unavailable prompt response: %{public}@"
+ "check for software updates completed presentation"
+ "defaultWorkspace"
+ "initWithDescription:responseHandler:"
+ "openSensitiveURL:withOptions:"
+ "prefs:root=General&path=SOFTWARE_UPDATE_LINK"
+ "present asset unavailable prompt, description: %@"
+ "present check for software updates"
+ "presentAssetUnavailablePromptWithDescription:responseHandler:"
+ "presentCheckForSoftwareUpdatesWithCompletionHandler:"
+ "promptDirector:wantsToCheckForSoftwareUpdatesWithCompletionHandler:"
+ "promptDirector:wantsToPresentAssetUnavailablePromptWithDescription:responseHandler:"
+ "v24@0:8@?<v@?>16"
+ "v32@0:8@\"CARSetupPromptDirector\"16@?<v@?>24"

```
