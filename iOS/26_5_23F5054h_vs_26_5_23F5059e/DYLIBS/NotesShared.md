## NotesShared

> `/System/Library/PrivateFrameworks/NotesShared.framework/NotesShared`

```diff

-2952.120.3.0.0
-  __TEXT.__text: 0x364128
+2952.120.4.0.0
+  __TEXT.__text: 0x364544
   __TEXT.__auth_stubs: 0x5230
   __TEXT.__delay_stubs: 0x240
   __TEXT.__delay_helper: 0x830
-  __TEXT.__objc_methlist: 0x17e8c
+  __TEXT.__objc_methlist: 0x17e9c
   __TEXT.__const: 0xdcf8
   __TEXT.__cstring: 0x18e71
-  __TEXT.__oslogstring: 0x1bf48
+  __TEXT.__oslogstring: 0x1bff8
   __TEXT.__gcc_except_tab: 0xf808
-  __TEXT.__ustring: 0x38e
+  __TEXT.__ustring: 0x392
   __TEXT.__swift5_typeref: 0x43d4
   __TEXT.__swift5_fieldmd: 0x2d9c
   __TEXT.__constg_swiftt: 0x368c

   __TEXT.__swift_as_entry: 0x19c
   __TEXT.__swift_as_ret: 0x1c8
   __TEXT.__swift5_mpenum: 0x74
-  __TEXT.__unwind_info: 0xf578
+  __TEXT.__unwind_info: 0xf580
   __TEXT.__eh_frame: 0x8ce8
   __TEXT.__objc_classname: 0x2ada
-  __TEXT.__objc_methname: 0x37a6f
+  __TEXT.__objc_methname: 0x37a9f
   __TEXT.__objc_methtype: 0x516f
-  __TEXT.__objc_stubs: 0x28740
+  __TEXT.__objc_stubs: 0x28760
   __DATA_CONST.__got: 0x2138
   __DATA_CONST.__const: 0x62f0
   __DATA_CONST.__objc_classlist: 0xa40
   __DATA_CONST.__objc_catlist: 0x138
   __DATA_CONST.__objc_protolist: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc980
+  __DATA_CONST.__objc_selrefs: 0xc988
   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0x6b8
   __DATA_CONST.__objc_arraydata: 0x1e8
   __AUTH_CONST.__auth_got: 0x2978
   __AUTH_CONST.__const: 0xd7f0
-  __AUTH_CONST.__cfstring: 0xf400
+  __AUTH_CONST.__cfstring: 0xf440
   __AUTH_CONST.__objc_const: 0x21d10
   __AUTH_CONST.__objc_intobj: 0x438
   __AUTH_CONST.__objc_arrayobj: 0x240

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 8BE613CA-67BB-3DC8-97F4-3DD8B2E3A4BD
-  Functions: 18407
-  Symbols:   38917
-  CStrings:  16502
+  UUID: 4861CD43-8D6E-359E-ACAC-AF50588E8A69
+  Functions: 18410
+  Symbols:   38922
+  CStrings:  16509
 
Symbols:
+ +[ICCloudSyncingObject identifierContainsInvalidCharacters:]
+ +[ICMedia containerDirectoryURLForMediaWithIdentifier:account:].cold.1
+ +[ICMedia purgeMediaFilesForIdentifiers:account:].cold.1
+ -[ICCloudSyncingObject validateIdentifier:error:].cold.1
+ GCC_except_table145
+ GCC_except_table282
+ ___27-[ICMedia writeData:error:]_block_invoke.38
+ ___38-[ICMedia writeDataFromFileURL:error:]_block_invoke.23
+ ___42-[ICMedia writeDataFromFileWrapper:error:]_block_invoke.40
+ ___53-[ICAttachment(Previews) checkPreviewImagesIntegrity]_block_invoke.1127
+ ___62+[ICCloudSyncingObject deleteTemporaryAssetFilesForOperation:]_block_invoke.253
+ ___block_literal_global.1125
+ ___block_literal_global.135
+ ___block_literal_global.138
+ ___block_literal_global.199
+ ___block_literal_global.236
+ ___block_literal_global.240
+ ___block_literal_global.256
+ ___block_literal_global.348
+ ___block_literal_global.486
+ ___block_literal_global.512
+ ___block_literal_global.515
+ ___block_literal_global.517
+ ___block_literal_global.56
+ _objc_msgSend$identifierContainsInvalidCharacters:
- ___27-[ICMedia writeData:error:]_block_invoke.37
- ___38-[ICMedia writeDataFromFileURL:error:]_block_invoke.22
- ___42-[ICMedia writeDataFromFileWrapper:error:]_block_invoke.39
- ___53-[ICAttachment(Previews) checkPreviewImagesIntegrity]_block_invoke.1126
- ___62+[ICCloudSyncingObject deleteTemporaryAssetFilesForOperation:]_block_invoke.247
- ___block_literal_global.1124
- ___block_literal_global.131
- ___block_literal_global.192
- ___block_literal_global.230
- ___block_literal_global.234
- ___block_literal_global.244
- ___block_literal_global.317
- ___block_literal_global.347
- ___block_literal_global.480
- ___block_literal_global.497
- ___block_literal_global.500
- ___block_literal_global.511
- ___block_literal_global.55
CStrings:
+ "\x00"
+ ".."
+ "Rejecting identifier containing invalid characters for %@"
+ "Rejecting media identifier with invalid characters"
+ "Skipping purge for media identifier with invalid characters"
+ "identifierContainsInvalidCharacters:"

```
