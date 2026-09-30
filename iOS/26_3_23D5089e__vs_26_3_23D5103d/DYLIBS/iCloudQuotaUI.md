## iCloudQuotaUI

> `/System/Library/PrivateFrameworks/iCloudQuotaUI.framework/iCloudQuotaUI`

```diff

-301.23.3.1.0
-  __TEXT.__text: 0x16f4cc
+301.23.3.2.0
+  __TEXT.__text: 0x16fd04
   __TEXT.__auth_stubs: 0x43c0
-  __TEXT.__objc_methlist: 0x9d04
+  __TEXT.__objc_methlist: 0x9d2c
   __TEXT.__const: 0xaf24
   __TEXT.__gcc_except_tab: 0xfe8
-  __TEXT.__cstring: 0xb836
-  __TEXT.__oslogstring: 0xb632
+  __TEXT.__cstring: 0xb846
+  __TEXT.__oslogstring: 0xb6d2
   __TEXT.__dlopen_cstrs: 0x691
   __TEXT.__swift5_typeref: 0x9bde
   __TEXT.__swift5_reflstr: 0x1ab0

   __TEXT.__swift_as_ret: 0x13c
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x54e8
+  __TEXT.__unwind_info: 0x54f0
   __TEXT.__eh_frame: 0x3578
   __TEXT.__objc_classname: 0x1769
-  __TEXT.__objc_methname: 0x1a818
-  __TEXT.__objc_methtype: 0x5ecf
-  __TEXT.__objc_stubs: 0x13ea0
+  __TEXT.__objc_methname: 0x1a86d
+  __TEXT.__objc_methtype: 0x5ee1
+  __TEXT.__objc_stubs: 0x13ee0
   __DATA_CONST.__got: 0x1cc8
   __DATA_CONST.__const: 0x2810
   __DATA_CONST.__objc_classlist: 0x5a8
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x278
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6a58
+  __DATA_CONST.__objc_selrefs: 0x6a60
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x380
   __DATA_CONST.__objc_arraydata: 0x578
   __AUTH_CONST.__auth_got: 0x21f0
   __AUTH_CONST.__const: 0x7020
   __AUTH_CONST.__cfstring: 0x7aa0
-  __AUTH_CONST.__objc_const: 0x22480
+  __AUTH_CONST.__objc_const: 0x224a0
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_dictobj: 0x488
   __AUTH.__objc_data: 0x3b70
   __AUTH.__data: 0x24c8
-  __DATA.__objc_ivar: 0xbd8
+  __DATA.__objc_ivar: 0xbdc
   __DATA.__data: 0x4110
   __DATA.__bss: 0xd4f8
   __DATA.__common: 0x2a8

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5D8AA87C-F2FD-3927-934F-4ECBF120B69C
-  Functions: 8055
-  Symbols:   15598
-  CStrings:  8824
+  UUID: 4AA0C37A-73FC-36FC-A36F-E04DD9658083
+  Functions: 8060
+  Symbols:   15611
+  CStrings:  8830
 
Symbols:
+ -[ICQBundlesHook _removeRefreshURLFromObjectModel]
+ -[ICQBundlesHook _removeRefreshURLFromObjectModel].cold.1
+ -[ICQBundlesHook objectModel]
+ -[ICQBundlesHook setObjectModel:]
+ -[ICQLinkInAppAction isEqual:]
+ _OBJC_IVAR_$_ICQBundlesHook._objectModel
+ _objc_msgSend$_removeRefreshURLFromObjectModel
+ _objc_msgSend$objectModel
CStrings:
+ "%s, purchaseSuccess: %d, purchaseError: %@, _amsAction: %ld"
+ "@\"RUIObjectModel\""
+ "In-App Message (identifier: %@) for bundle ID %@ with title: %@, subTitle: %@, conciseTitle:%@, sfSymbolID:%@ sfSymbolColor:%@, actions:\n%@"
+ "Removed refreshUrl from objectModel.clientInfo to prevent /bundlePurchase request"
+ "T@\"RUIObjectModel\",?,&,N,V_objectModel"
+ "_objectModel"
+ "_removeRefreshURLFromObjectModel"
+ "objectModel is nil, cannot prevent /bundlePurchase request"
- "%s, purchaseSuccess: %d, purchaseError: %@"
- "In-App Message for bundle ID %@ with title: %@, subTitle: %@, conciseTitle:%@, sfSymbolID:%@ sfSymbolColor:%@, actions:\n%@"

```
