## ContactsUI

> `/System/Library/Frameworks/ContactsUI.framework/Versions/A/ContactsUI`

```diff

-2765.100.1.1.1
-  __TEXT.__text: 0xdb164
-  __TEXT.__objc_methlist: 0xe5a0
-  __TEXT.__cstring: 0x52d3
-  __TEXT.__const: 0x7a54
+2768.200.41.0.0
+  __TEXT.__text: 0xdba18
+  __TEXT.__objc_methlist: 0xe5c0
+  __TEXT.__cstring: 0x52f3
+  __TEXT.__const: 0x7a64
   __TEXT.__gcc_except_tab: 0xae4
-  __TEXT.__oslogstring: 0x1b6a
+  __TEXT.__oslogstring: 0x1c1a
   __TEXT.__ustring: 0x5ec
   __TEXT.__dlopen_cstrs: 0x1df
   __TEXT.__constg_swiftt: 0x1be8

   __TEXT.__swift5_capture: 0x948
   __TEXT.__swift5_mpenum: 0x58
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x4db0
+  __TEXT.__unwind_info: 0x4dc8
   __TEXT.__eh_frame: 0xd8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x358
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8568
+  __DATA_CONST.__objc_selrefs: 0x8598
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x498
   __DATA_CONST.__objc_arraydata: 0xe0
-  __DATA_CONST.__got: 0x1980
-  __AUTH_CONST.__const: 0x67f0
+  __DATA_CONST.__got: 0x1988
+  __AUTH_CONST.__const: 0x6820
   __AUTH_CONST.__cfstring: 0x3b60
   __AUTH_CONST.__objc_const: 0x17fb0
   __AUTH_CONST.__objc_arrayobj: 0xa8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6637
-  Symbols:   13241
-  CStrings:  902
+  Functions: 6643
+  Symbols:   13254
+  CStrings:  909
 
Symbols:
+ -[CNContactCardViewController didSelectActionItem:actionType:sourceView:]
+ -[CNContactCardViewController finishDowntimeWhitelistSaveDidSucceed:revertingToContact:]
+ -[CNContactCardViewController saveDowntimeWhitelisted:forContact:]
+ -[CNContactCardViewController setDowntimeWhitelisted:]
+ GCC_except_table189
+ GCC_except_table195
+ _CNDowntimeWhitelistDisallowed
+ __54-[CNContactCardViewController setDowntimeWhitelisted:]_block_invoke
+ ___54-[CNContactCardViewController setDowntimeWhitelisted:]_block_invoke
+ ___block_descriptor_49_e8_32s40s_e44_v24?0"CNUIContactFetchResult"8"NSError"16l
+ _objc_msgSend$areKeysAvailable:
+ _objc_msgSend$cnui_isUnknown
+ _objc_msgSend$downtimeWhitelist
+ _objc_msgSend$finishDowntimeWhitelistSaveDidSucceed:revertingToContact:
+ _objc_msgSend$saveDowntimeWhitelisted:forContact:
+ _objc_msgSend$setDowntimeWhitelisted:
- -[CNContactCardViewController didSelectActionItem:actionType:]
- GCC_except_table185
- GCC_except_table191
CStrings:
+ "Failed to %{public}s contact %@ downtime whitelist: %@"
+ "Failed to fetch a non-unified contact %@ to update its downtime whitelist: %@"
+ "Updated downtime whitelist for contact %@ to %{public}s"
+ "add"
+ "allowed"
+ "disallowed"
+ "remove"
```
