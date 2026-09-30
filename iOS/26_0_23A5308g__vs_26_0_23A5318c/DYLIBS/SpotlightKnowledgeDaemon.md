## SpotlightKnowledgeDaemon

> `/System/Library/PrivateFrameworks/SpotlightKnowledgeDaemon.framework/SpotlightKnowledgeDaemon`

```diff

-2391.1.0.0.0
-  __TEXT.__text: 0xef9a8
+2393.100.0.0.0
+  __TEXT.__text: 0xefda0
   __TEXT.__auth_stubs: 0x2570
   __TEXT.__objc_methlist: 0x7fc0
   __TEXT.__const: 0x1b78
-  __TEXT.__oslogstring: 0x8903
+  __TEXT.__oslogstring: 0x8993
   __TEXT.__cstring: 0x9347
-  __TEXT.__gcc_except_tab: 0x5a8c
+  __TEXT.__gcc_except_tab: 0x5aa4
   __TEXT.__dlopen_cstrs: 0x5e
   __TEXT.__swift5_typeref: 0x847
   __TEXT.__swift5_fieldmd: 0x6a4

   __TEXT.__swift5_assocty: 0x1d8
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x36a0
+  __TEXT.__unwind_info: 0x36b8
   __TEXT.__eh_frame: 0x378
   __TEXT.__objc_classname: 0xeee
   __TEXT.__objc_methname: 0x115be

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 49A294B5-B1C8-3A2A-9D1F-1381F24040C6
-  Functions: 4862
-  Symbols:   14415
-  CStrings:  6997
+  UUID: 3103233A-57F3-3C43-8D7B-41D533FDD7FF
+  Functions: 4865
+  Symbols:   14422
+  CStrings:  7000
 
Symbols:
+ -[CSScheduledReceiverUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:].cold.2
+ -[CSScheduledReceiverUpdater supportedJournalItem:].cold.1
+ ___88-[CSScheduledReceiverUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:]_block_invoke.62
+ ___88-[CSScheduledReceiverUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:]_block_invoke.75
+ ___88-[CSScheduledReceiverUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:]_block_invoke.80
- ___88-[CSScheduledReceiverUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:]_block_invoke.59
- ___88-[CSScheduledReceiverUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:]_block_invoke.72
- ___88-[CSScheduledReceiverUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:]_block_invoke.77
Functions:
~ -[CSEventDonationJournalItem containsAnyInAttributes:] : 664 -> 592
~ -[CSScheduledReceiverUpdater shouldHandleJournalItem:bundleID:] : 508 -> 720
~ -[CSScheduledReceiverUpdater supportedJournalItem:] : 132 -> 192
~ -[CSScheduledReceiverUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:] : 2792 -> 3144
+ _OUTLINED_FUNCTION_0
+ -[CSScheduledReceiverUpdater supportedJournalItem:].cold.1
+ -[CSScheduledReceiverUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:].cold.2
CStrings:
+ "### cancelling '%s' due to invalid bundle '%s'"
+ "### ignoring batch for '%s' due to invalid bundle '%s'"
+ "### ignoring item for '%s' (required: <%s>)"

```
