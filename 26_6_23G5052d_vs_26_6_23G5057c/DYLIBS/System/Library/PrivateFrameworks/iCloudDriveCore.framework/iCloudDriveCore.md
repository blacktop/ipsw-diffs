## iCloudDriveCore

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore`

```diff

-  __TEXT.__text: 0x325a8c
+  __TEXT.__text: 0x325a0c
   __TEXT.__auth_stubs: 0x1a80
   __TEXT.__objc_methlist: 0x1ac2c
   __TEXT.__const: 0x510
   __TEXT.__cstring: 0x7f189
-  __TEXT.__oslogstring: 0x3bb27
-  __TEXT.__gcc_except_tab: 0x1a1b8
+  __TEXT.__oslogstring: 0x3bb17
+  __TEXT.__gcc_except_tab: 0x1a1a4
   __TEXT.__ustring: 0x36
   __TEXT.__unwind_info: 0xa878
   __TEXT.__objc_classname: 0x2b45

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 13821
-  Symbols:   45517
+  Functions: 13822
+  Symbols:   45521
   CStrings:  28019
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Functions:
~ -[BRCXPCRegularIPCsClient updateContainerMetadataForID:] : 1292 -> 1288
~ -[BRCXPCRegularIPCsClient getApplicationDocumentUsageInfoForBundleID:withReply:] : 1628 -> 1616
~ -[BRCXPCRegularIPCsClient simulateHealthIssueWithContainer:status:reply:] : 3072 -> 2916
~ -[BRCXPCRegularIPCsClient updateContainerMetadataForID:].cold.1 : 76 -> 68
~ -[BRCXPCRegularIPCsClient _t_createFileAtURL:reply:].cold.1 : 80 -> 68
~ -[BRCXPCRegularIPCsClient _t_canReadFileAtURL:reply:].cold.2 : 80 -> 68
+ -[BRCXPCRegularIPCsClient waitUntilIdle:timeout:reply:].cold.1
CStrings:
+ "[ERROR] nonexistent container%@"
+ "[WARNING] unable to find bundleID%@"
- "[NOTICE] simulating health issue on %@: %@%@"
- "[WARNING] unable to find bundleID %@%@"

```
