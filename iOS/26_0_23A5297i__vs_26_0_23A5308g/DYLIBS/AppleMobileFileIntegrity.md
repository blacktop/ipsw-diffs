## AppleMobileFileIntegrity

> `/System/Library/PrivateFrameworks/AppleMobileFileIntegrity.framework/AppleMobileFileIntegrity`

```diff

-1045.0.25.0.0
-  __TEXT.__text: 0xb26c
+1045.0.35.0.0
+  __TEXT.__text: 0xb37c
   __TEXT.__auth_stubs: 0x7e0
   __TEXT.__objc_methlist: 0x2f4
   __TEXT.__const: 0x1b8
-  __TEXT.__cstring: 0x14bb
+  __TEXT.__cstring: 0x14fb
   __TEXT.__oslogstring: 0xbf0
   __TEXT.__gcc_except_tab: 0x2b0
-  __TEXT.__unwind_info: 0x330
+  __TEXT.__unwind_info: 0x328
   __TEXT.__objc_classname: 0x75
-  __TEXT.__objc_methname: 0x97f
-  __TEXT.__objc_methtype: 0x349
+  __TEXT.__objc_methname: 0x9c7
+  __TEXT.__objc_methtype: 0x352
   __TEXT.__objc_stubs: 0xa40
   __DATA_CONST.__got: 0x1c8
   __DATA_CONST.__const: 0x828

   __DATA_CONST.__objc_superrefs: 0x18
   __AUTH_CONST.__auth_got: 0x400
   __AUTH_CONST.__const: 0x268
-  __AUTH_CONST.__cfstring: 0x600
+  __AUTH_CONST.__cfstring: 0x660
   __AUTH_CONST.__objc_const: 0x658
   __DATA.__objc_ivar: 0x40
   __DATA.__data: 0xc0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 12C3FDF9-38CF-3C4F-A013-5E09CEF7AABC
+  UUID: D3E2C99A-25E9-3CC9-BDEF-298A31D3E4AA
   Functions: 250
   Symbols:   866
-  CStrings:  479
+  CStrings:  485
 
Symbols:
+ +[ValidationMetrics sendSHA1CodeDirectoryMetricWithFilename:withSigningID:withCDHash:withTeamID:withBundleID:withVersion:withIsApple:withSigningTimestamp:withExecutableFormat:withHasRestrictedEntitlements:]
+ ___206+[ValidationMetrics sendSHA1CodeDirectoryMetricWithFilename:withSigningID:withCDHash:withTeamID:withBundleID:withVersion:withIsApple:withSigningTimestamp:withExecutableFormat:withHasRestrictedEntitlements:]_block_invoke
+ ___block_descriptor_98_e8_32s40s48s56s64s72s80s88s_e19_"NSDictionary"8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
- +[ValidationMetrics sendSHA1CodeDirectoryMetricWithFilename:withSigningID:withCDHash:withTeamID:withBundleID:withVersion:withIsApple:]
- ___134+[ValidationMetrics sendSHA1CodeDirectoryMetricWithFilename:withSigningID:withCDHash:withTeamID:withBundleID:withVersion:withIsApple:]_block_invoke
- ___block_descriptor_81_e8_32s40s48s56s64s72s_e19_"NSDictionary"8?0ls32l8s40l8s48l8s56l8s64l8s72l8
Functions:
~ +[ValidationMetrics sendSHA1CodeDirectoryMetricWithFilename:withSigningID:withCDHash:withTeamID:withBundleID:withVersion:withIsApple:] -> +[ValidationMetrics sendSHA1CodeDirectoryMetricWithFilename:withSigningID:withCDHash:withTeamID:withBundleID:withVersion:withIsApple:withSigningTimestamp:withExecutableFormat:withHasRestrictedEntitlements:] : 348 -> 440
~ ___134+[ValidationMetrics sendSHA1CodeDirectoryMetricWithFilename:withSigningID:withCDHash:withTeamID:withBundleID:withVersion:withIsApple:]_block_invoke -> ___206+[ValidationMetrics sendSHA1CodeDirectoryMetricWithFilename:withSigningID:withCDHash:withTeamID:withBundleID:withVersion:withIsApple:withSigningTimestamp:withExecutableFormat:withHasRestrictedEntitlements:]_block_invoke : 584 -> 764
CStrings:
+ "executable_format"
+ "has_restricted_entitlements"
+ "sendSHA1CodeDirectoryMetricWithFilename:withSigningID:withCDHash:withTeamID:withBundleID:withVersion:withIsApple:withSigningTimestamp:withExecutableFormat:withHasRestrictedEntitlements:"
+ "signing_timestamp"
+ "v88@0:8@16@24@32@40@48@56B64@68@76B84"
- "sendSHA1CodeDirectoryMetricWithFilename:withSigningID:withCDHash:withTeamID:withBundleID:withVersion:withIsApple:"
- "v68@0:8@16@24@32@40@48@56B64"

```
