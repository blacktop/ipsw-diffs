## SpotlightKnowledgeDaemon

> `/System/Library/PrivateFrameworks/SpotlightKnowledgeDaemon.framework/SpotlightKnowledgeDaemon`

```diff

-2400.11.100.0.0
-  __TEXT.__text: 0xefda0
+2400.13.1.101.0
+  __TEXT.__text: 0xf01f8
   __TEXT.__auth_stubs: 0x2570
-  __TEXT.__objc_methlist: 0x7fc0
+  __TEXT.__objc_methlist: 0x7fb8
   __TEXT.__const: 0x1b78
-  __TEXT.__oslogstring: 0x8993
+  __TEXT.__oslogstring: 0x8b03
   __TEXT.__cstring: 0x9347
-  __TEXT.__gcc_except_tab: 0x5aa4
+  __TEXT.__gcc_except_tab: 0x5aa8
   __TEXT.__dlopen_cstrs: 0x5e
   __TEXT.__swift5_typeref: 0x847
   __TEXT.__swift5_fieldmd: 0x6a4

   __TEXT.__unwind_info: 0x36b8
   __TEXT.__eh_frame: 0x378
   __TEXT.__objc_classname: 0xeee
-  __TEXT.__objc_methname: 0x115be
+  __TEXT.__objc_methname: 0x115a8
   __TEXT.__objc_methtype: 0x1e3d
   __TEXT.__objc_stubs: 0xef00
   __DATA_CONST.__got: 0xc90

   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4600
+  __DATA_CONST.__objc_selrefs: 0x45f8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x3d0
   __DATA_CONST.__objc_arraydata: 0x878

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 3ED7EA69-20E7-3DEA-A33C-B649CEBFB3FA
-  Functions: 4865
-  Symbols:   14422
-  CStrings:  7000
+  UUID: 715BDC00-4727-39E8-9D6A-8D6F330CED13
+  Functions: 4874
+  Symbols:   14440
+  CStrings:  7005
 
Symbols:
+ -[CSScheduledReceiverUpdater shouldHandleJournalItem:bundleID:].cold.1
+ -[CSScheduledReceiverUpdater shouldHandleJournalItem:bundleID:].cold.2
+ -[CSScheduledReceiverUpdater shouldHandleJournalItem:bundleID:].cold.3
+ -[CSScheduledReceiverUpdater shouldHandleJournalItem:bundleID:].cold.4
+ -[CSScheduledReceiverUpdater shouldHandleJournalItem:bundleID:].cold.5
+ GCC_except_table31
+ ___88-[CSScheduledReceiverUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:]_block_invoke.62.cold.1
+ ___block_descriptor_81_e8_32s40s48s56s64r72r_e36_B16?0"CSEventDonationJournalItem"8ls32l8s40l8s48l8r64l8s56l8r72l8
+ _objc_msgSend$isUpdate
- -[CSScheduledReceiverUpdater supportedJournalItem:]
- -[CSScheduledReceiverUpdater supportedJournalItem:].cold.1
- ___block_descriptor_73_e8_32s40s48s56r64r_e36_B16?0"CSEventDonationJournalItem"8ls32l8s40l8r56l8s48l8r64l8
- _objc_msgSend$supportedJournalItem:
CStrings:
+ "### RECEIVER %s logging debug item type='%s' sn:'%llu'"
+ "### RECEIVER ignoring for '%s' due to invalid bundle '%s'"
+ "### RECEIVER ignoring for '%s' due to invalid contentType '%s'"
+ "### RECEIVER ignoring for '%s', '%s' due to new item"
+ "### RECEIVER ignoring for '%s', '%s' due to old item"
+ "### RECEIVER ignoring for '%s','%s' as user activity"
+ "### RECEIVER ignoring item for '%s' due to invalid bundle '%s'"
+ "### RECEIVER ignoring item for '%s', isUpdate: %d (required: <%s>)"
+ "### RECEIVER ignoring item in batch for '%s', '%s'"
- "### cancelling '%s' due to invalid bundle '%s'"
- "### ignoring batch for '%s' due to invalid bundle '%s'"
- "### ignoring item for '%s' (required: <%s>)"
- "supportedJournalItem:"

```
