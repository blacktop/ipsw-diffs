## ScreenTimeUI

> `/System/Library/PrivateFrameworks/ScreenTimeUI.framework/ScreenTimeUI`

```diff

-503.4.14.0.0
-  __TEXT.__text: 0x19b10
+503.5.12.3.0
+  __TEXT.__text: 0x19fdc
   __TEXT.__auth_stubs: 0x620
   __TEXT.__objc_methlist: 0x11f4
-  __TEXT.__const: 0x78
+  __TEXT.__const: 0x80
   __TEXT.__cstring: 0xc46
   __TEXT.__gcc_except_tab: 0x39c
-  __TEXT.__oslogstring: 0x20b3
+  __TEXT.__oslogstring: 0x21d6
   __TEXT.__unwind_info: 0x710
   __TEXT.__objc_classname: 0x1a3
-  __TEXT.__objc_methname: 0x51ca
+  __TEXT.__objc_methname: 0x51d0
   __TEXT.__objc_methtype: 0x7a0
-  __TEXT.__objc_stubs: 0x4280
+  __TEXT.__objc_stubs: 0x42a0
   __DATA_CONST.__got: 0xd8
   __DATA_CONST.__const: 0xa58
   __DATA_CONST.__objc_classlist: 0x58

   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x1ac0
-  __DATA_CONST.__objc_selrefs: 0x1368
+  __DATA_CONST.__objc_selrefs: 0x1370
   __DATA_CONST.__objc_classrefs: 0x280
   __DATA_CONST.__objc_superrefs: 0x38
   __AUTH_CONST.__objc_const: 0x530

   - /System/Library/PrivateFrameworks/URLFormatting.framework/URLFormatting
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 074A8225-6ED1-3A0F-A702-7C04706CCD7D
-  Functions: 645
-  Symbols:   2354
-  CStrings:  1363
+  UUID: 9F696E3B-1812-3FE0-99E7-14C8E7E52EF0
+  Functions: 654
+  Symbols:   2373
+  CStrings:  1368
 
Symbols:
+ -[STIconCache imageForBundleIdentifier:].cold.1
+ -[STIconCache imageForBundleIdentifier:].cold.2
+ -[STIconCache imageForBundleIdentifier:].cold.3
+ -[STIconCache imageForBundleIdentifier:].cold.4
+ -[STIconCache imageForBundleIdentifier:completionHandler:].cold.1
+ -[STIconCache imageForBundleIdentifier:completionHandler:].cold.2
+ -[STIconCache imageForBundleIdentifier:completionHandler:].cold.3
+ -[STIconCache imageForBundleIdentifier:completionHandler:].cold.4
+ ___40-[STIconCache imageForBundleIdentifier:]_block_invoke.65
+ ___58-[STIconCache imageForBundleIdentifier:completionHandler:]_block_invoke.62
+ ___76-[STIconCache _fetchFamilyPhotoWithDSID:fullName:appleID:completionHandler:]_block_invoke.133
+ ___85-[STIconCache _handleiTunesResponseForAppInfo:response:data:error:completionHandler:]_block_invoke.64
+ _objc_msgSend$appInfo
- ___40-[STIconCache imageForBundleIdentifier:]_block_invoke_2
- ___58-[STIconCache imageForBundleIdentifier:completionHandler:]_block_invoke_2
- ___76-[STIconCache _fetchFamilyPhotoWithDSID:fullName:appleID:completionHandler:]_block_invoke.130
- ___85-[STIconCache _handleiTunesResponseForAppInfo:response:data:error:completionHandler:]_block_invoke.62
CStrings:
+ "STIconCache failed to get icon for synced app %@ ; using blank image"
+ "STIconCache failed to get icon from artworkData for synced app %@"
+ "STIconCache failed to get icon from launch services for app %@ ; using blank image"
+ "STIconCache found no artworkURL for App Store app %@ ; using blank image"
+ "appInfo"

```
