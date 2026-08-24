## ShareKit

> `/System/Library/PrivateFrameworks/ShareKit.framework/Versions/A/ShareKit`

```diff

-2126.10.4.0.0
-  __TEXT.__text: 0x783c8
-  __TEXT.__objc_methlist: 0x5a2c
+2130.10.2.1.5
+  __TEXT.__text: 0x78430
+  __TEXT.__objc_methlist: 0x5a44
   __TEXT.__const: 0x20c
-  __TEXT.__cstring: 0x45c0
+  __TEXT.__cstring: 0x45fb
   __TEXT.__gcc_except_tab: 0x13e0
   __TEXT.__oslogstring: 0x62ba
   __TEXT.__ustring: 0x128
   __TEXT.__dlopen_cstrs: 0x52
-  __TEXT.__unwind_info: 0x1b80
+  __TEXT.__unwind_info: 0x1b88
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x47d0
+  __DATA_CONST.__objc_selrefs: 0x47d8
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_arraydata: 0x68
   __DATA_CONST.__got: 0x918
   __AUTH_CONST.__const: 0x2e30
-  __AUTH_CONST.__cfstring: 0x4c20
-  __AUTH_CONST.__objc_const: 0xae30
+  __AUTH_CONST.__cfstring: 0x4c60
+  __AUTH_CONST.__objc_const: 0xae40
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0xa8

   - /System/Library/PrivateFrameworks/ViewBridge.framework/Versions/A/ViewBridge
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2546
-  Symbols:   6236
-  CStrings:  1243
+  Functions: 2547
+  Symbols:   6239
+  CStrings:  1245
 
Symbols:
+ -[SHKSharingServicePicker fetchExistingShareForFileOrFolderURL:completionHandler:]
+ GCC_except_table116
+ GCC_except_table149
+ GCC_except_table167
+ GCC_except_table181
+ GCC_except_table190
+ GCC_except_table193
+ GCC_except_table67
+ GCC_except_table90
+ _objc_msgSend$fetchExistingShareForFileOrFolderURL:completionHandler:
- GCC_except_table115
- GCC_except_table159
- GCC_except_table166
- GCC_except_table189
- GCC_except_table192
- GCC_except_table66
- GCC_except_table89
Functions:
~ -[SHKSharingServicePicker showRequestAccessAlertForActivityType:shareSupportsRequestAccess:optionsIncludeAccessRequestsOption:completionHandler:] : 1144 -> 1160
+ -[SHKSharingServicePicker fetchExistingShareForFileOrFolderURL:completionHandler:]
~ -[SHKSharingServicePicker _shouldUseCollaborationItemsForService:] : 208 -> 132
~ -[SHKSharingServicePicker _performActionWithIdentifier:] : 476 -> 504
~ -[SHKInviteWithLinkSharingService init] : 264 -> 296
~ -[SHKInviteWithLinkSharingService canPerformWithItems:] : 384 -> 356
CStrings:
+ "Add"
+ "Add Access"
+ "SHARE_LINK_ACCESS_REQUESTS_ALREADY_ON_MESSAGE"
+ "SHARE_LINK_ACCESS_REQUESTS_UNSUPPORTED_MESSAGE"
+ "person.badge.plus"
- "Create Link"
- "Invite with Link"
- "SHARE_LINK_ACCESS_REQUESTS_ON_MESSAGE"
```
