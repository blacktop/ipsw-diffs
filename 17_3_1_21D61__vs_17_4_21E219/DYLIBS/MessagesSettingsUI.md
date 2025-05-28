## MessagesSettingsUI

> `/System/Library/PrivateFrameworks/MessagesSettingsUI.framework/MessagesSettingsUI`

```diff

-1262.400.41.2.3
-  __TEXT.__text: 0x72f0
-  __TEXT.__auth_stubs: 0x490
-  __TEXT.__objc_methlist: 0x758
+1262.500.151.2.4
+  __TEXT.__text: 0x76b8
+  __TEXT.__auth_stubs: 0x4a0
+  __TEXT.__objc_methlist: 0x788
   __TEXT.__const: 0xca
-  __TEXT.__cstring: 0x962
-  __TEXT.__gcc_except_tab: 0x610
-  __TEXT.__oslogstring: 0x33a
+  __TEXT.__cstring: 0x972
+  __TEXT.__gcc_except_tab: 0x658
+  __TEXT.__oslogstring: 0x3cd
   __TEXT.__dlopen_cstrs: 0x58
   __TEXT.__constg_swiftt: 0x48
   __TEXT.__swift5_typeref: 0x6
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x2fc
+  __TEXT.__unwind_info: 0x31c
   __TEXT.__objc_classname: 0x143
-  __TEXT.__objc_methname: 0x20b3
+  __TEXT.__objc_methname: 0x2123
   __TEXT.__objc_methtype: 0x4a9
-  __TEXT.__objc_stubs: 0x1c80
+  __TEXT.__objc_stubs: 0x1d20
   __DATA_CONST.__got: 0xe0
-  __DATA_CONST.__const: 0x2b0
+  __DATA_CONST.__const: 0x2d0
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1060
-  __DATA_CONST.__objc_selrefs: 0x830
-  __AUTH_CONST.__cfstring: 0x9c0
+  __DATA_CONST.__objc_const: 0x1090
+  __DATA_CONST.__objc_selrefs: 0x858
+  __DATA_CONST.__objc_classrefs: 0x130
+  __DATA_CONST.__objc_superrefs: 0x38
+  __AUTH_CONST.__cfstring: 0x9e0
   __AUTH_CONST.__objc_const: 0x288
-  __AUTH_CONST.__const: 0x60
+  __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH_CONST.__auth_got: 0x258
+  __AUTH_CONST.__auth_got: 0x260
   __AUTH.__objc_data: 0x280
   __AUTH.__data: 0x98
-  __DATA.__objc_classrefs: 0x130
-  __DATA.__objc_superrefs: 0x38
   __DATA.__objc_ivar: 0x68
   __DATA.__data: 0x120
   __DATA.__bss: 0x80

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 183
-  Symbols:   949
-  CStrings:  549
+  Functions: 188
+  Symbols:   969
+  CStrings:  560
 
Symbols:
+ -[CKCloudSettingsViewController syncButtonPressed:]
+ -[CKiCloudSettingsSyncController cancelCurrentSync]
+ -[CKiCloudSettingsViewModel isSyncButtonEnabled]
+ -[CKiCloudSettingsViewModel syncButtonText]
+ -[CKiCloudSettingsViewModel syncSupportsCancellation]
+ GCC_except_table31
+ GCC_except_table32
+ _IMStringFromIMCloudKitSyncType
+ ___51-[CKiCloudSettingsSyncController cancelCurrentSync]_block_invoke
+ ___block_descriptor_32_e11_v20?0B8Q12l
+ ___block_literal_global.53
+ _objc_msgSend$cancelCurrentSync
+ _objc_msgSend$cancelSync:
+ _objc_msgSend$isSyncButtonEnabled
+ _objc_msgSend$remainingMessagesCount
+ _objc_msgSend$syncButtonText
+ _objc_msgSend$syncSupportsCancellation
+ _objc_msgSend$syncType
- -[CKCloudSettingsViewController startSync:]
- GCC_except_table29
- GCC_except_table30
- _objc_msgSend$syncedMessageCount
- _objc_msgSend$totalMessageCount
CStrings:
+ "Attempting to cancelling ongoing sync."
+ "CANCEL_SYNCING"
+ "Canceling {%@} sync. success={%@}"
+ "T@\"NSString\",?,R,C"
+ "Tried to cancel a sync via UI, but we are not syncing. Programming error."
+ "cancelCurrentSync"
+ "cancelSync:"
+ "isSyncButtonEnabled"
+ "remainingMessagesCount"
+ "syncButtonPressed:"
+ "syncButtonText"
+ "syncSupportsCancellation"
+ "syncType"
+ "v20@?0B8Q12"
- "startSync:"
- "syncedMessageCount"
- "totalMessageCount"

```
