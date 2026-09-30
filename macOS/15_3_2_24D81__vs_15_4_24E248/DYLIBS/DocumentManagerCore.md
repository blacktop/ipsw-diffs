## DocumentManagerCore

> `/System/iOSSupport/System/Library/PrivateFrameworks/DocumentManagerCore.framework/Versions/A/DocumentManagerCore`

```diff

-337.4.0.0.0
-  __TEXT.__text: 0x23ab4
-  __TEXT.__auth_stubs: 0x9b0
-  __TEXT.__objc_methlist: 0x2524
+337.5.1.3.0
+  __TEXT.__text: 0x2409c
+  __TEXT.__auth_stubs: 0x9a0
+  __TEXT.__objc_methlist: 0x2c94
   __TEXT.__const: 0x4b6
-  __TEXT.__gcc_except_tab: 0x588
+  __TEXT.__gcc_except_tab: 0x580
   __TEXT.__cstring: 0x2e11
   __TEXT.__oslogstring: 0x16b5
   __TEXT.__ustring: 0x10c

   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_proto: 0x44
   __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0xb28
+  __TEXT.__unwind_info: 0xb78
   __TEXT.__eh_frame: 0x170
   __TEXT.__objc_classname: 0x52d
   __TEXT.__objc_methname: 0x7bc1
   __TEXT.__objc_methtype: 0xc29
   __TEXT.__objc_stubs: 0x4ee0
   __DATA_CONST.__got: 0x378
-  __DATA_CONST.__const: 0x12d0
+  __DATA_CONST.__const: 0x12c8
   __DATA_CONST.__objc_classlist: 0x128
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d80
+  __DATA_CONST.__objc_selrefs: 0x1ed0
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xb8
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0x4e8
+  __AUTH_CONST.__auth_got: 0x4e0
   __AUTH_CONST.__const: 0x740
   __AUTH_CONST.__cfstring: 0x2820
-  __AUTH_CONST.__objc_const: 0x5b10
+  __AUTH_CONST.__objc_const: 0x4d28
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0xbb0

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 6C0AD9C5-0781-3830-A689-65014E5BF7F3
-  Functions: 1155
-  Symbols:   2891
+  UUID: 2A25C3D1-AB1E-3D6A-A424-A3D1B68F491C
+  Functions: 1216
+  Symbols:   2959
   CStrings:  2382
 
Symbols:
+ +[DOCAppProtectionManager sharedManager].cold.1
+ +[DOCConfiguration configurationForExportingDocumentsToURLs:mode:].cold.1
+ +[DOCConfiguration configurationForExportingDocumentsToURLs:mode:].cold.2
+ +[DOCConfiguration configurationForImportingDocumentContentTypes:mode:].cold.1
+ +[DOCFeature _docImplementation_uip_isFloatingTabBarEnabled].cold.1
+ +[DOCFeature _docImplementation_uip_isUIPDocumentLandingEnabled].cold.1
+ +[DOCFeature contextMenuShowsOpenWithApp].cold.1
+ +[DOCFeature dsEnumerationFPv2].cold.1
+ +[DOCFeature dsEnumerationLocal].cold.1
+ +[DOCFeature dsEnumerationSMB].cold.1
+ +[DOCFeature dsEnumerationUSB].cold.1
+ +[DOCFeature forceUnmount].cold.1
+ +[DOCFeature protectedApps].cold.1
+ +[DOCFeature quickLookAllDocumentsInFiles].cold.1
+ +[DOCFeature quickLookEntireFolderInWindow].cold.1
+ +[DOCFeature quickLookInWindowShared].cold.1
+ +[DOCFeature quickLookInWindow].cold.1
+ +[DOCFeature quickLookRestrictContentTypesThatOpenInWindow].cold.1
+ +[DOCFeature returnToSender].cold.1
+ +[DOCFeature semanticSearch].cold.1
+ +[DOCFeature showTips].cold.1
+ +[DOCFeature suggestedMoveToFolderInContextMenu].cold.1
+ +[DOCFeature usbDiskProperties].cold.1
+ +[DOCFeature usbEraseDialog].cold.1
+ +[DOCFeature usbRenameErase].cold.1
+ +[DOCFeature useBlastDoorThumbnails].cold.1
+ +[DOCFeature viewOptionsSizeSetting].cold.1
+ +[DOCFeature workaroundFor_113995648].cold.1
+ +[DOCManagedPermission defaultPermission].cold.1
+ +[DOCNodeStartupManager shared].cold.1
+ +[DOCPostLaunchBuffer shared].cold.1
+ +[DOCProtectedAppContainerCache enabled].cold.1
+ +[DOCTagLocalStorage sharedAppGroupStorage].cold.1
+ +[DOCTagRegistry sharedInstance].cold.1
+ +[DOCUndoManager shared].cold.1
+ -[DOCAppProtectionManager hostAppCanNavigateToAppBundleID:].cold.1
+ -[DOCAppProtectionManager hostAppCanNavigateToFileProviderDomain:].cold.1
+ -[DOCAppProtectionManager hostAppCanNavigateToFileProviderDomain:].cold.2
+ -[DOCAppProtectionManager hostAppCanNavigateToTargetNode:].cold.2
+ -[DOCAppProtectionManager hostAppCanSeeFileProviderDomain:].cold.1
+ -[DOCAppProtectionManager hostAppCanSeeFileProviderDomain:].cold.2
+ -[DOCConfiguration documentContentTypes].cold.1
+ -[DOCConfiguration hostBundleTitle].cold.1
+ -[DOCDownloadImportManager _doc_destinationLocationExists:].cold.1
+ -[DOCDownloadImportManager importPlaceholderAtURLToDownloadsDirectory:completion:].cold.1
+ -[DOCDownloadSettings setDefaultDownloadsLocationItem:completionHandler:].cold.1
+ -[DOCFavoritesManager favoritedLocations].cold.1
+ -[DOCFavoritesManager isGathering].cold.1
+ -[DOCManagedPermission canHostAppPerformAction:accountIdentifier:].cold.1
+ -[DOCManagedPermission canHostAppPerformAction:bundleIdentifier:].cold.1
+ -[DOCManagedPermission canHostAppPerformAction:fileProviderDomain:].cold.1
+ -[DOCManagedPermission canHostAppPerformAction:legacyPickerExtension:].cold.1
+ -[DOCManagedPermission canHostAppPerformAction:targetNode:].cold.1
+ -[DOCManagedPermission dataOwnerStateForiCloudDomain:].cold.1
+ -[DOCTag initWithICloudTagAttributes:].cold.1
+ -[NSFileManager(DOCItemImportSPI) _doc_importItemAtURL:toDestination:error:].cold.1
+ -[UTType(DOCNode) doc_conformsToFolder].cold.1
+ DOCInitLogging.cold.1
+ DOCLogAssertionFailure.cold.2
+ DOCLogAssertionFailure.cold.3
+ DOCLogAssertionFailureMessage_Swift.cold.2
+ DOCLogAssertionFailureMessage_Swift.cold.3
+ DOCProviderDomainIDIsWebDAV.cold.1
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ __39-[DOCDownloadSettings _fetchProviders:]_block_invoke.cold.1
+ __LoadCrashSupportIfNecessary_block_invoke.cold.2
+ documentmanager_perf_log.cold.1
- __swift_FORCE_LOAD_$_swiftFileProvider
- __swift_FORCE_LOAD_$_swiftFileProvider_$_DocumentManagerCore
- _objc_retain_x26

```
