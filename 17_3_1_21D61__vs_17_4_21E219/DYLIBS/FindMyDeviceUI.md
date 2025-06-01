## FindMyDeviceUI

> `/System/Library/PrivateFrameworks/FindMyDeviceUI.framework/FindMyDeviceUI`

```diff

-136.1.1.0.0
-  __TEXT.__text: 0x39e4
-  __TEXT.__auth_stubs: 0x330
-  __TEXT.__objc_methlist: 0x394
+139.1.0.0.0
+  __TEXT.__text: 0x4024
+  __TEXT.__auth_stubs: 0x340
+  __TEXT.__objc_methlist: 0x3c4
   __TEXT.__const: 0x8
   __TEXT.__gcc_except_tab: 0x98
-  __TEXT.__cstring: 0x6ea
-  __TEXT.__oslogstring: 0xa9
-  __TEXT.__unwind_info: 0x194
+  __TEXT.__cstring: 0x774
+  __TEXT.__oslogstring: 0x13a
+  __TEXT.__unwind_info: 0x1a0
   __TEXT.__objc_classname: 0x3f
-  __TEXT.__objc_methname: 0x1098
-  __TEXT.__objc_methtype: 0xbb
-  __TEXT.__objc_stubs: 0xfe0
-  __DATA_CONST.__got: 0xb0
+  __TEXT.__objc_methname: 0x1198
+  __TEXT.__objc_methtype: 0xcf
+  __TEXT.__objc_stubs: 0x10e0
+  __DATA_CONST.__got: 0xb8
   __DATA_CONST.__const: 0x2f0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x328
-  __DATA_CONST.__objc_selrefs: 0x4b0
-  __AUTH_CONST.__cfstring: 0x5a0
+  __DATA_CONST.__objc_selrefs: 0x4f8
+  __DATA_CONST.__objc_classrefs: 0xf0
+  __DATA_CONST.__objc_superrefs: 0x10
+  __AUTH_CONST.__cfstring: 0x680
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__objc_const: 0xd8
-  __AUTH_CONST.__auth_got: 0x1a8
+  __AUTH_CONST.__auth_got: 0x1b0
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_classrefs: 0xd8
-  __DATA.__objc_superrefs: 0x10
   __DATA.__objc_ivar: 0x38
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication
   - /System/Library/Frameworks/MobileCoreServices.framework/MobileCoreServices
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B10131A2-909D-3B19-A90B-5A4053FBCF99
-  Functions: 102
-  Symbols:   501
-  CStrings:  302
+  UUID: E1BB537D-D957-3280-B8F6-1654B4C6C57B
+  Functions: 107
+  Symbols:   524
+  CStrings:  330
 
Symbols:
+ -[FMDUIFMIPiCloudSettingsViewController addHyperLinkStyleToText:inString:action:forGroup:]
+ -[FMDUIFMIPiCloudSettingsViewController addHyperLinkStyleToText:inString:action:forGroup:].cold.1
+ -[FMDUIFMIPiCloudSettingsViewController isDTOEnabledAndFindMyOn]
+ -[FMDUIFMIPiCloudSettingsViewController isFMIPSwitchEnabled]
+ -[FMDUIFMIPiCloudSettingsViewController showLearnMoreLinkInDTODisclosure:]
+ GCC_except_table42
+ GCC_except_table51
+ _OBJC_CLASS_$_LARatchetManager
+ _OBJC_CLASS_$_NSURL
+ _OBJC_CLASS_$_PSFooterMultiHyperlinkView
+ ___NSDictionary0__struct
+ __os_log_error_impl
+ _objc_msgSend$URLWithString:
+ _objc_msgSend$addFooterHyperlinkWithRange:target:action:
+ _objc_msgSend$addHyperLinkStyleToText:inString:action:forGroup:
+ _objc_msgSend$isDTOEnabledAndFindMyOn
+ _objc_msgSend$isFMIPSwitchEnabled
+ _objc_msgSend$isFeatureEnabled
+ _objc_msgSend$openSensitiveURL:withOptions:error:
+ _objc_msgSend$propertyForKey:
- GCC_except_table38
- GCC_except_table43
CStrings:
+ "\n\n"
+ "%@ %@%@%@"
+ "Could not open %@ through FindMy"
+ "FMD_ICLOUD_SETTINGS_FMIP_GROUP_FOOTER_TOP_DTO"
+ "FMD_TOP_DTO_LEARN_MORE_LINK_TITLE"
+ "Group must use %@ as footer cell class"
+ "NO"
+ "Should FMIP Button be enabled %@"
+ "Should show DTO Disclaimer - %{public}@"
+ "URLWithString:"
+ "YES"
+ "addFooterHyperlinkWithRange:target:action:"
+ "addHyperLinkStyleToText:inString:action:forGroup:"
+ "https://support.apple.com/kb/HT212510"
+ "isDTOEnabledAndFindMyOn"
+ "isFMIPSwitchEnabled"
+ "isFeatureEnabled"
+ "openSensitiveURL:withOptions:error:"
+ "propertyForKey:"
+ "showLearnMoreLinkInDTODisclosure:"
+ "v48@0:8@16@24:32@40"

```
