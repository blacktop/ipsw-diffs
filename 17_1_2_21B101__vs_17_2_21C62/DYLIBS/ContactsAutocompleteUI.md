## ContactsAutocompleteUI

> `/System/Library/PrivateFrameworks/ContactsAutocompleteUI.framework/ContactsAutocompleteUI`

```diff

-723.0.0.0.0
-  __TEXT.__text: 0x41fec
+727.0.0.0.0
+  __TEXT.__text: 0x42c98
   __TEXT.__auth_stubs: 0x960
-  __TEXT.__objc_methlist: 0x2eb8
+  __TEXT.__objc_methlist: 0x2ed0
   __TEXT.__const: 0x2d0
-  __TEXT.__cstring: 0x1565
+  __TEXT.__cstring: 0x1590
   __TEXT.__gcc_except_tab: 0x41c
-  __TEXT.__oslogstring: 0x764
+  __TEXT.__oslogstring: 0xaf4
   __TEXT.__ustring: 0x14
   __TEXT.__dlopen_cstrs: 0x4a
   __TEXT.__objc_const_ax: 0x1e1c
-  __TEXT.__unwind_info: 0x1288
+  __TEXT.__unwind_info: 0x1290
   __TEXT.__objc_classname: 0xbd6
-  __TEXT.__objc_methname: 0x13c1f
+  __TEXT.__objc_methname: 0x13c7f
   __TEXT.__objc_methtype: 0x4ebf
-  __TEXT.__objc_stubs: 0xd040
+  __TEXT.__objc_stubs: 0xd080
   __DATA_CONST.__got: 0x280
   __DATA_CONST.__const: 0x1248
   __DATA_CONST.__objc_classlist: 0x210
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xb118
-  __DATA_CONST.__objc_selrefs: 0x3de8
+  __DATA_CONST.__objc_const: 0xb158
+  __DATA_CONST.__objc_selrefs: 0x3df8
   __AUTH_CONST.__cfstring: 0x10c0
   __AUTH_CONST.__objc_const: 0x1a88
-  __AUTH_CONST.__const: 0x560
+  __AUTH_CONST.__const: 0x580
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x4c0
   __AUTH.__objc_data: 0xbe0

   __DATA.__objc_ivar: 0x574
   __DATA.__objc_const_ax: 0x0
   __DATA.__data: 0xd80
-  __DATA.__bss: 0x120
+  __DATA.__bss: 0x130
   __DATA.__common: 0x1
   __DATA_DIRTY.__objc_data: 0x8c0
   __DATA_DIRTY.__bss: 0x58

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 18D3F774-1565-32D3-B184-2533CF200440
-  Functions: 1849
-  Symbols:   7035
-  CStrings:  4017
+  UUID: 6ECB9F75-04F3-3575-B8CB-46425571182B
+  Functions: 1870
+  Symbols:   7082
+  CStrings:  4036
 
Symbols:
+ +[CNComposeRecipient namingLog]
+ -[CNComposeRecipient _makeCompositeName]
+ -[CNComposeRecipient _makeCompositeName].cold.1
+ -[CNComposeRecipient _makeCompositeName].cold.2
+ -[CNComposeRecipient _makeCompositeName].cold.3
+ -[CNComposeRecipient _makeCompositeName].cold.4
+ -[CNComposeRecipient alternativeToDisplayString].cold.1
+ -[CNComposeRecipient alternativeToDisplayString].cold.2
+ -[CNComposeRecipient alternativeToDisplayString].cold.3
+ -[CNComposeRecipient displayStringPreferringNickname:].cold.1
+ -[CNComposeRecipient displayStringPreferringNickname:].cold.2
+ -[CNComposeRecipient displayStringPreferringNickname:].cold.3
+ -[CNComposeRecipient displayString].cold.1
+ -[CNComposeRecipient displayString].cold.2
+ -[CNComposeRecipient initWithContact:address:displayString:kind:].cold.1
+ -[CNComposeRecipientGroup compositeName].cold.1
+ -[CNComposeRecipientGroup displayString].cold.1
+ GCC_except_table117
+ GCC_except_table63
+ ___31+[CNComposeRecipient namingLog]_block_invoke
+ ___block_literal_global.37
+ ___block_literal_global.75
+ ___block_literal_global.77
+ _namingLog.cn_once_object_6
+ _namingLog.cn_once_token_6
+ _objc_msgSend$_makeCompositeName
+ _objc_msgSend$namingLog
- GCC_except_table114
- GCC_except_table60
- ___block_literal_global.72
- ___block_literal_global.74
CStrings:
+ "Initializing %{public}@ %p with displayString '%{private}@'"
+ "Name (compositeName) of %{public}@ %p: %{private}@"
+ "Name (displayString) of %{public}@ %p: %{private}@"
+ "Preferring nickname for displayString for %{public}@ %p: %{private}@"
+ "T@\"NSObject<OS_os_log>\",R"
+ "Unable to generate composite name for %{public}@ %p"
+ "Using address as alternative to displayString for %{public}@ %p: %{private}@"
+ "Using alternative to displayString for %{public}@ %p: %{private}@"
+ "Using compositeName as alternative to displayString for %{public}@ %p: %{private}@"
+ "Using displayString as injected for %{public}@ %p: %{private}@"
+ "Using name built from commented email address for composite name for %{public}@ %p: %{private}@"
+ "Using name built from components for composite name for %{public}@ %p: %{private}@"
+ "Using name built from contact for composite name for %{public}@ %p: %{private}@"
+ "Using placeholder as alternative to displayString for %{public}@ %p: %{private}@"
+ "_makeCompositeName"
+ "autoFillDidInsertWithExplicitInvocationMode:"
+ "compose-recipient"
+ "compose-recipient-naming"
+ "namingLog"

```
