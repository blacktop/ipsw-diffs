## assetsd

> `/System/Library/Frameworks/AssetsLibrary.framework/Support/assetsd`

```diff

-700.33.101.0.0
-  __TEXT.__text: 0x15c80
-  __TEXT.__auth_stubs: 0xb70
-  __TEXT.__objc_stubs: 0x4100
-  __TEXT.__objc_methlist: 0x998
+700.41.103.0.0
+  __TEXT.__text: 0x15d80
+  __TEXT.__auth_stubs: 0xb80
+  __TEXT.__objc_stubs: 0x4140
+  __TEXT.__objc_methlist: 0x9a8
   __TEXT.__const: 0xe0
   __TEXT.__gcc_except_tab: 0x55c
-  __TEXT.__oslogstring: 0x39c4
+  __TEXT.__oslogstring: 0x3a81
   __TEXT.__objc_classname: 0x5f4
-  __TEXT.__objc_methname: 0x4bb2
-  __TEXT.__objc_methtype: 0x897
+  __TEXT.__objc_methname: 0x4be3
+  __TEXT.__objc_methtype: 0x8cf
   __TEXT.__cstring: 0x1328
   __TEXT.__dlopen_cstrs: 0xb4
   __TEXT.__info_plist: 0x43c
   __TEXT.__unwind_info: 0x510
-  __DATA_CONST.__auth_got: 0x5c8
+  __DATA_CONST.__auth_got: 0x5d0
   __DATA_CONST.__got: 0x700
   __DATA_CONST.__const: 0x8b8
   __DATA_CONST.__cfstring: 0xa40

   __DATA_CONST.__objc_arraydata: 0x38
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_intobj: 0x78
-  __DATA.__objc_const: 0x2d58
-  __DATA.__objc_selrefs: 0x1120
+  __DATA.__objc_const: 0x2d78
+  __DATA.__objc_selrefs: 0x1130
   __DATA.__objc_ivar: 0x6c
   __DATA.__objc_data: 0xc30
   __DATA.__data: 0x300

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 320
-  Symbols:   420
-  CStrings:  1117
+  Functions: 321
+  Symbols:   421
+  CStrings:  1122
 
Symbols:
+ _OBJC_CLASS_$_PLFileBackedLogger
+ _PLSearchFileProtectionTypes
- _OBJC_CLASS_$_PLModelMigratorLog
CStrings:
+ "SpotlightDaemonClient: Aborting unexpected request to reindex all searchable items"
+ "SpotlightDaemonClient: Aborting unexpected request to reindex all searchable items for bundleID: %!@(MISSING)"
+ "SpotlightDaemonClient: Aborting unexpected request to reindex all searchable items for unsupported protectionClass: %!{(MISSING)public}@"
+ "SpotlightDaemonClient: Aborting unexpected request to reindex searchable items for bundleID: %!@(MISSING), identifiers: %!@(MISSING)"
+ "SpotlightDaemonClient: Aborting unexpected request to reindex searchable items with identifiers for unsupported protectionClass: %!{(MISSING)public}@, identifiers: %!@(MISSING)"
+ "SpotlightDaemonClient: Aborting unexpected request to reindex searchable items with identifiers: %!{(MISSING)public}@"
+ "SpotlightDaemonClient: Failed to record reindex all searchable items with error: %!@(MISSING)"
+ "SpotlightDaemonClient: Failed to record reindex searchable items: %!@(MISSING) with error: %!@(MISSING)"
+ "SpotlightDaemonClient: Failed to record request to reindex all searchable items for Core Spotlight"
+ "SpotlightDaemonClient: Failed to record request to reindex searchable item identifiers for Core Spotlight: %!@(MISSING)"
+ "SpotlightDaemonClient: Received request from Spotlight to provideDataForBundleID - no action is implemented by Photos in response to this request"
+ "SpotlightDaemonClient: Received request from Spotlight to provideFileURLForBundleID - no action is implemented by Photos in response to this request"
+ "SpotlightDaemonClient: Received request to reindex all searchable items for Core Spotlight for bundleID: %!@(MISSING)"
+ "SpotlightDaemonClient: Received request to reindex all searchable items for Core Spotlight for bundleID: %!{(MISSING)public}@, protection class: %!{(MISSING)public}@"
+ "SpotlightDaemonClient: Received request to reindex all searchable items for Core Spotlight for bundleID: %!{(MISSING)public}@, reason: %!{(MISSING)public}@, protection class: %!{(MISSING)public}@"
+ "SpotlightDaemonClient: Received request to reindex searchable items for Core Spotlight: %!@(MISSING) for bundleID: %!@(MISSING)"
+ "SpotlightDaemonClient: Received request to reindex searchable items for Core Spotlight: %!@(MISSING) for bundleID: %!@(MISSING), protection class: %!{(MISSING)public}@"
+ "SpotlightDaemonClient: Recorded request to reindex all searchable items for Core Spotlight"
+ "SpotlightDaemonClient: Recorded request to reindex searchable item identifiers for Core Spotlight: %!@(MISSING)"
+ "SpotlightDaemonClient: Unexpected request to reindex searchable items for Spotlight managed index"
+ "SpotlightDaemonClient: Unexpected request to reindex searchable items for bundleID: %!@(MISSING)"
+ "_isValidProtectionClass:"
+ "recordReindexAllItemsForBundleID:reindexReason:"
+ "setImportFilesystemAssetsState:"
+ "setupWithLibraryIdentifier:type:"
+ "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@?<v@?>40"
- "PLSpotlightDonationManager: Aborting unexpected request to reindex all searchable items"
- "PLSpotlightDonationManager: Aborting unexpected request to reindex all searchable items for bundleID: %!@(MISSING)"
- "PLSpotlightDonationManager: Aborting unexpected request to reindex searchable items for bundleID: %!@(MISSING), identifiers: %!@(MISSING)"
- "PLSpotlightDonationManager: Aborting unexpected request to reindex searchable items with identifiers: %!{(MISSING)public}@"
- "PLSpotlightDonationManager: Failed to record reindex all searchable items with error: %!@(MISSING)"
- "PLSpotlightDonationManager: Failed to record reindex searchable items: %!@(MISSING) with error: %!@(MISSING)"
- "PLSpotlightDonationManager: Failed to record request to reindex all searchable items for Core Spotlight"
- "PLSpotlightDonationManager: Failed to record request to reindex searchable item identifiers for Core Spotlight: %!@(MISSING)"
- "PLSpotlightDonationManager: Received request from Spotlight to provideDataForBundleID - no action is implemented by Photos in response to this request"
- "PLSpotlightDonationManager: Received request from Spotlight to provideFileURLForBundleID - no action is implemented by Photos in response to this request"
- "PLSpotlightDonationManager: Received request to reindex all searchable items for Core Spotlight for bundleID: %!@(MISSING)"
- "PLSpotlightDonationManager: Received request to reindex all searchable items for Core Spotlight for bundleID: %!{(MISSING)public}@, protection class: %!{(MISSING)public}@"
- "PLSpotlightDonationManager: Received request to reindex all searchable items for Core Spotlight for bundleID: %!{(MISSING)public}@, reason: %!{(MISSING)public}@, protection class: %!{(MISSING)public}@"
- "PLSpotlightDonationManager: Received request to reindex searchable items for Core Spotlight: %!@(MISSING) for bundleID: %!@(MISSING)"
- "PLSpotlightDonationManager: Received request to reindex searchable items for Core Spotlight: %!@(MISSING) for bundleID: %!@(MISSING), protection class: %!{(MISSING)public}@"
- "PLSpotlightDonationManager: Recorded request to reindex all searchable items for Core Spotlight"
- "PLSpotlightDonationManager: Recorded request to reindex searchable item identifiers for Core Spotlight: %!@(MISSING)"
- "PLSpotlightDonationManager: Unexpected request to reindex searchable items for Spotlight managed index"
- "PLSpotlightDonationManager: Unexpected request to reindex searchable items for bundleID: %!@(MISSING)"
- "forceImportFileSystemDataIntoDatabaseWithPhotoLibrary:"
- "recordReindexAllItemsForBundleID:"

```
