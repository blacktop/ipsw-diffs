## AKFollowUpExtension

> `/System/Library/PrivateFrameworks/AuthKitUI.framework/PlugIns/AKFollowUpExtension.appex/AKFollowUpExtension`

```diff

-525.575.8.0.0
-  __TEXT.__text: 0xa580
+550.0.0.0.0
+  __TEXT.__text: 0x9f78
   __TEXT.__auth_stubs: 0x260
-  __TEXT.__objc_stubs: 0x1000
+  __TEXT.__objc_stubs: 0x1060
   __TEXT.__objc_methlist: 0x2ec
   __TEXT.__const: 0x40
-  __TEXT.__gcc_except_tab: 0x610
-  __TEXT.__cstring: 0x628
-  __TEXT.__oslogstring: 0x71b
-  __TEXT.__objc_classname: 0x5d
-  __TEXT.__objc_methname: 0x1062
+  __TEXT.__gcc_except_tab: 0x3cc
+  __TEXT.__cstring: 0x62c
+  __TEXT.__oslogstring: 0x797
+  __TEXT.__objc_methname: 0x10b4
+  __TEXT.__objc_classname: 0x59
   __TEXT.__objc_methtype: 0x35e
   __TEXT.__dlopen_cstrs: 0x1b
-  __TEXT.__unwind_info: 0x220
-  __DATA_CONST.__auth_got: 0x140
-  __DATA_CONST.__got: 0x188
+  __TEXT.__unwind_info: 0x228
   __DATA_CONST.__const: 0x4f0
   __DATA_CONST.__cfstring: 0x2a0
   __DATA_CONST.__objc_classlist: 0x10

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x18
+  __DATA_CONST.__auth_got: 0x140
+  __DATA_CONST.__got: 0x188
   __DATA.__objc_const: 0x3e0
-  __DATA.__objc_selrefs: 0x4e8
+  __DATA.__objc_selrefs: 0x500
   __DATA.__objc_ivar: 0x24
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0xc0

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AAAFoundation.framework/AAAFoundation
+  - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/AuthKitUI.framework/AuthKitUI
   - /System/Library/PrivateFrameworks/CoreFollowUpUI.framework/CoreFollowUpUI

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A65151E0-F4CB-34A1-834D-80FEB2173BE0
+  UUID: CDD795D1-F645-30FC-93A6-51AEC1F5AC1D
   Functions: 116
   Symbols:   114
-  CStrings:  336
+  CStrings:  341
 
CStrings:
+ "Email is already flagged as verified for account %@, skipping account update."
+ "Updating account %@ with verified email flag."
+ "fetchAuthKitAccountWithAltDSID:error:"
+ "saveAccount:error:"
+ "setVerifiedPrimaryEmail:forAccount:"
+ "verifiedPrimaryEmailForAccount:"
- "updateVerifiedEmail:forAccountWithAltDSID:"

```
