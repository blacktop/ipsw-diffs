## SoftwareUpdateSettingsUI

> `/System/Library/PrivateFrameworks/SoftwareUpdateSettingsUI.framework/SoftwareUpdateSettingsUI`

```diff

-412.100.1.0.0
-  __TEXT.__text: 0xffa20
+412.100.2.0.0
+  __TEXT.__text: 0x107948
   __TEXT.__auth_stubs: 0x980
   __TEXT.__objc_methlist: 0x4b24
-  __TEXT.__cstring: 0x9cb9
-  __TEXT.__oslogstring: 0x15874
-  __TEXT.__gcc_except_tab: 0x3b54
+  __TEXT.__cstring: 0x9e09
+  __TEXT.__oslogstring: 0x158e4
+  __TEXT.__gcc_except_tab: 0x4bb0
   __TEXT.__dlopen_cstrs: 0x658
   __TEXT.__const: 0x46
   __TEXT.__swift5_typeref: 0xc3
   __TEXT.__swift5_capture: 0xbc
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x8
-  __TEXT.__unwind_info: 0x16a8
+  __TEXT.__unwind_info: 0x17d8
   __TEXT.__eh_frame: 0xf0
   __TEXT.__objc_classname: 0x6f5
   __TEXT.__objc_methname: 0xe514
   __TEXT.__objc_methtype: 0x246f
   __TEXT.__objc_stubs: 0x9740
   __DATA_CONST.__got: 0x700
-  __DATA_CONST.__const: 0x9698
+  __DATA_CONST.__const: 0x98c8
   __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x88

   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 2101
   Symbols:   2520
-  CStrings:  3705
+  CStrings:  3711
 
CStrings:
+ "%s [%{public}@]: The task has already been canceled. Stopping."
+ "%s: Self is nil in %{public}@. Stopping."
+ "-[SUSettingsScanOperation action_ReportScanCanceled:error:]_block_invoke"
+ "-[SUSettingsScanOperation action_ReportScanOutcome:error:]_block_invoke"
+ "-[SUSettingsScanOperation checkForBetaPrograms:withReplyHandler:]_block_invoke"
+ "-[SUSettingsScanOperation queryDDMDeclaration:withReplyHandler:]_block_invoke"
+ "-[SUSettingsScanOperation refreshBetaProgramsWithOptions:completionHandler:]_block_invoke"
+ "-[SUSettingsUpdateOperation action_PresentDownloadConstraints:error:]_block_invoke"
+ "-[SUSettingsUpdateOperation action_ReportUpdateOperationOutcome:error:]_block_invoke"
+ "-[SUSettingsUpdateOperation promoteDownloadToUserInitiated:completionHandler:]_block_invoke"
- "-[SUSettingsUpdateOperation action_AquireKeybag:error:]_block_invoke_3"
- "-[SUSettingsUpdateOperation action_PresentDownloadConstraints:error:]_block_invoke_3"
- "-[SUSettingsUpdateOperation action_PresentTermsConditions:error:]_block_invoke_3"
- "-[SUSettingsUpdateOperation action_PurgeSpace:error:]_block_invoke_3"

```
