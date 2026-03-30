## SafariCore

> `/System/Library/PrivateFrameworks/SafariCore.framework/SafariCore`

```diff

-624.1.16.10.6
-  __TEXT.__text: 0x14d6ac
+624.2.1.10.1
+  __TEXT.__text: 0x14dce0
   __TEXT.__auth_stubs: 0x3310
-  __TEXT.__objc_methlist: 0xbf0c
+  __TEXT.__objc_methlist: 0xbf44
   __TEXT.__const: 0x3570
   __TEXT.__gcc_except_tab: 0x7054
-  __TEXT.__cstring: 0x13045
+  __TEXT.__cstring: 0x130b5
   __TEXT.__ustring: 0x2826
-  __TEXT.__oslogstring: 0xb053
+  __TEXT.__oslogstring: 0xb073
   __TEXT.__dlopen_cstrs: 0x157
   __TEXT.__swift5_typeref: 0x10d1
   __TEXT.__constg_swiftt: 0xb7c

   __TEXT.__swift_as_ret: 0xf4
   __TEXT.__swift5_capture: 0x70c
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0x69d8
+  __TEXT.__unwind_info: 0x69f8
   __TEXT.__eh_frame: 0x3a00
   __TEXT.__objc_classname: 0x1de5
-  __TEXT.__objc_methname: 0x26045
+  __TEXT.__objc_methname: 0x260e5
   __TEXT.__objc_methtype: 0x46aa
-  __TEXT.__objc_stubs: 0x12ba0
+  __TEXT.__objc_stubs: 0x12bc0
   __DATA_CONST.__got: 0xea0
-  __DATA_CONST.__const: 0x51c0
+  __DATA_CONST.__const: 0x5230
   __DATA_CONST.__objc_classlist: 0x610
   __DATA_CONST.__objc_catlist: 0x160
   __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6dd8
+  __DATA_CONST.__objc_selrefs: 0x6df0
   __DATA_CONST.__objc_protorefs: 0xa8
   __DATA_CONST.__objc_superrefs: 0x4a0
   __DATA_CONST.__objc_arraydata: 0x2a20
   __AUTH_CONST.__auth_got: 0x19a0
   __AUTH_CONST.__const: 0x6c08
-  __AUTH_CONST.__cfstring: 0x19b40
-  __AUTH_CONST.__objc_const: 0x13a68
+  __AUTH_CONST.__cfstring: 0x19b80
+  __AUTH_CONST.__objc_const: 0x13a88
   __AUTH_CONST.__objc_intobj: 0x870
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_arrayobj: 0x5a0
   __AUTH.__objc_data: 0x2710
   __AUTH.__data: 0x660
-  __DATA.__objc_ivar: 0xc68
+  __DATA.__objc_ivar: 0xc6c
   __DATA.__data: 0x1a58
   __DATA.__bss: 0x5190
   __DATA.__common: 0x30

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 67F1D1C3-E389-38D0-9060-F1B79806495C
-  Functions: 7991
-  Symbols:   21343
-  CStrings:  13307
+  UUID: C600C369-642F-33CD-B16C-BB8E60D0D9F5
+  Functions: 8001
+  Symbols:   21371
+  CStrings:  13316
 
Symbols:
+ -[NSError(SafariCoreExtras) safari_underlyingErrorMatchesErrorDomain:andCode:]
+ -[NSError(SafariCoreExtras) safari_underlyingErrorMatchesErrorDomainsAndCodes:]
+ -[NSFileManager(SafariNSFileManagerExtras) safari_ensureDirectoryExists:error:]
+ -[WBSPasswordWarningManager _issuesForPassword:withWeakPasswordEvaluation:passwordIsReused:supportsAnyWellKnownPasskeyEndpointsURL:breachResultRecord:]
+ -[WBSPasswordWarningManager _resetWebsiteMetadataCache]
+ GCC_except_table58
+ _OBJC_IVAR_$_WBSPasswordWarningManager._cachedDomainToMetadataEntry
+ _WBSMailAppApplicationIdentifier
+ _WBSMailAppBundleIdentifier
+ _WBSMessagesAppApplicationIdentifier
+ _WBSMessagesAppBundleIdentifier
+ ___111-[WBSPasswordWarningManager _getBreachResultRecordsForPasswords:startSessionIfNecessary:withCompletionHandler:]_block_invoke.60
+ ___55-[WBSPasswordWarningManager _resetWebsiteMetadataCache]_block_invoke
+ ___55-[WBSPasswordWarningManager _resetWebsiteMetadataCache]_block_invoke_2
+ ___55-[WBSPasswordWarningManager _resetWebsiteMetadataCache]_block_invoke_3
+ ___block_descriptor_40_e8_32s_e22_v16?0"NSDictionary"8ls32l8
+ ___block_descriptor_40_e8_32s_e65_v32?0"NSString"8"WBSPasswordManagerWebsiteMetadataEntry"16^B24ls32l8
+ ___block_literal_global.41
+ ___block_literal_global.62
+ ___block_literal_global.74
+ _objc_msgSend$_issuesForPassword:withWeakPasswordEvaluation:passwordIsReused:supportsAnyWellKnownPasskeyEndpointsURL:breachResultRecord:
+ _objc_msgSend$_resetWebsiteMetadataCache
+ _objc_msgSend$allMetadataWithCompletionHandler:
+ _objc_msgSend$checkResourceIsReachableAndReturnError:
+ _objc_msgSend$safari_ensureDirectoryExists:error:
- -[WBSPasswordWarningManager _issuesForPassword:withWeakPasswordEvaluation:passwordIsReused:websiteMetadataEntry:breachResultRecord:]
- GCC_except_table56
- ___111-[WBSPasswordWarningManager _getBreachResultRecordsForPasswords:startSessionIfNecessary:withCompletionHandler:]_block_invoke.59
- ___block_literal_global.40
- ___block_literal_global.73
- _objc_msgSend$_issuesForPassword:withWeakPasswordEvaluation:passwordIsReused:websiteMetadataEntry:breachResultRecord:
- _objc_msgSend$createDirectoryAtPath:withIntermediateDirectories:attributes:error:
- _objc_msgSend$isReadableFileAtPath:
- _objc_msgSend$supportsPasskeys
CStrings:
+ "Failed to create folder hierarchy at (%{sensitive}@). Error: %{public}@"
+ "Failed to replace the file at (%{sensitive}@). Error: %{public}@"
+ "File to replace still exists after removal at %{sensitive}@. Error: %{public}@"
+ "Origin file is not readable %{sensitive}@. Cancelling replacement of %{sensitive}@."
+ "Q48@0:8@16@24B32B36@40"
+ "_cachedDomainToMetadataEntry"
+ "_issuesForPassword:withWeakPasswordEvaluation:passwordIsReused:supportsAnyWellKnownPasskeyEndpointsURL:breachResultRecord:"
+ "_resetWebsiteMetadataCache"
+ "checkResourceIsReachableAndReturnError:"
+ "com.apple.MobileSMS"
+ "com.apple.mobilemail"
+ "safari_ensureDirectoryExists:error:"
+ "safari_underlyingErrorMatchesErrorDomain:andCode:"
+ "safari_underlyingErrorMatchesErrorDomainsAndCodes:"
+ "v32@?0@\"NSString\"8@\"WBSPasswordManagerWebsiteMetadataEntry\"16^B24"
- "Cancelled replacing file because Destination path is empty."
- "Failed to replace the file at (%{public}@). Error: %{public}@"
- "File to replace still exist after removal at %{public}@. Error: %{public}@"
- "Origin file is not readable %{public}@. Cancelling replacement of %{public}@."
- "Q52@0:8@16@24B32@36@44"
- "_issuesForPassword:withWeakPasswordEvaluation:passwordIsReused:websiteMetadataEntry:breachResultRecord:"
- "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
- "isReadableFileAtPath:"

```
