## InstalledContentLibrary

> `/System/Library/PrivateFrameworks/InstalledContentLibrary.framework/InstalledContentLibrary`

```diff

-1513.40.8.0.0
-  __TEXT.__text: 0xb5304
+1513.40.11.502.1
+  __TEXT.__text: 0xb5694
   __TEXT.__auth_stubs: 0x17c0
-  __TEXT.__objc_methlist: 0x53f4
-  __TEXT.__const: 0xf7f0
-  __TEXT.__cstring: 0x17aed
+  __TEXT.__objc_methlist: 0x5414
+  __TEXT.__const: 0xf810
+  __TEXT.__cstring: 0x17b1d
   __TEXT.__gcc_except_tab: 0xbf8
   __TEXT.__oslogstring: 0x8eb
   __TEXT.__dlopen_cstrs: 0x111

   __TEXT.__unwind_info: 0x1758
   __TEXT.__eh_frame: 0x400
   __TEXT.__objc_classname: 0x619
-  __TEXT.__objc_methname: 0xec48
-  __TEXT.__objc_methtype: 0x1e3f
+  __TEXT.__objc_methname: 0xed06
+  __TEXT.__objc_methtype: 0x1e64
   __TEXT.__objc_stubs: 0x8b20
   __DATA_CONST.__got: 0x4b0
-  __DATA_CONST.__const: 0xed0
+  __DATA_CONST.__const: 0xed8
   __DATA_CONST.__objc_classlist: 0x208
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2d38
+  __DATA_CONST.__objc_selrefs: 0x2d50
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x170
   __DATA_CONST.__objc_arraydata: 0xb20
   __AUTH_CONST.__auth_got: 0xbf0
   __AUTH_CONST.__const: 0x5688
-  __AUTH_CONST.__cfstring: 0xcd00
-  __AUTH_CONST.__objc_const: 0x9b70
+  __AUTH_CONST.__cfstring: 0xcd20
+  __AUTH_CONST.__objc_const: 0x9b88
   __AUTH_CONST.__objc_dictobj: 0x1270
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH.__objc_data: 0x370
-  __AUTH.__data: 0xc8
+  __AUTH.__data: 0xd0
   __DATA.__objc_ivar: 0x57c
-  __DATA.__data: 0x9e0
+  __DATA.__data: 0x9f0
   __DATA.__bss: 0x138
   __DATA.__common: 0xa20
   __DATA_DIRTY.__objc_data: 0x1180

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: 6CC51F65-9C07-33B5-9CF0-E9DE19639D4D
+  UUID: 10C52A86-6455-3B7F-A00B-8E6F201D2FAF
   Functions: 2216
   Symbols:   6867
-  CStrings:  6341
+  CStrings:  6348
 
Symbols:
+ -[MIContainer markContainerAsStagedUpdateWithError:]
+ ___block_literal_global.199
+ ___block_literal_global.332
+ ___block_literal_global.344
+ ___block_literal_global.390
+ ___block_literal_global.395
+ _objc_msgSend$URLIsOnAttachedEntityType:at:
+ _objc_msgSend$appBundleIDsOnAttachedEntityType:
+ _objc_msgSend$appInfoForBundleID:onAttachedEntityType:
+ _objc_msgSend$attachedContentPathsForEntityType:
+ _objc_msgSend$bundleID:isOnAttachedEntityType:
- -[MIContainer markContainerAsStagedUpdateContainer:]
- ___block_literal_global.196
- ___block_literal_global.329
- ___block_literal_global.341
- ___block_literal_global.387
- ___block_literal_global.392
- _objc_msgSend$URLIsOnKnownImageMount:
- _objc_msgSend$bundleIDIsOnKnownImageMount:
- _objc_msgSend$diskImageAppBundleIDs
- _objc_msgSend$diskImageAppInfoForBundleID:
- _objc_msgSend$diskMountPaths
Functions:
~ +[MIContainer _allContainersForIdentifier:persona:options:error:] : 1644 -> 1688
~ -[MIBundle bundleType] : 1032 -> 1100
~ -[MIBundle isStaticContent] : 1244 -> 1300
~ -[MIFilesystemScanner performScanWithError:] : 2212 -> 2828
~ -[MIDaemonConfiguration builtInApplicationBundleIDs] : 168 -> 216
~ -[MIInstalledInfoGatherer bundleRecordWithError:] : 484 -> 492
~ _MobileInstallerProtocolInterface : 568 -> 652
~ -[MIExecutableBundle needsDataContainer] : 644 -> 648
~ -[MIExecutableBundle updateMCMWithCodeSigningInfoAsAdvanceCopy:withError:] : 804 -> 816
~ -[MIExecutableBundle _codeSigningInfoFromMCM] : 432 -> 436
~ -[MIExecutableBundle hasNoConflictsWithOtherInstalledEntitiesForSigningInfo:forPersona:error:] : 888 -> 892
~ -[MIBundleContainer makeContainerLiveReplacingContainer:reason:waitForDeletion:withError:] : 456 -> 420
CStrings:
+ "-[MIContainer markContainerAsStagedUpdateWithError:]"
+ "Failed to clear staged update container status for %@ after making it live : %@"
+ "OS Module app"
+ "URLIsOnAttachedEntityType:at:"
+ "_OSModuleApplicationsDirectories"
+ "appBundleIDsOnAttachedEntityType:"
+ "appInfoForBundleID:onAttachedEntityType:"
+ "attachedContentPathsForEntityType:"
+ "bundleID:isOnAttachedEntityType:"
+ "markContainerAsStagedUpdateWithError:"
+ "reconcileContentsOnKnownOSModules:completion:"
+ "registerContentsOnOSModuleAtURL:completion:"
+ "unregisterContentsOnOSModuleAtURL:completion:"
+ "v32@0:8@\"NSSet\"16@?<v@?@\"NSError\">24"
- "-[MIContainer markContainerAsStagedUpdateContainer:]"
- "Failed to clear staged update container %@ after failing to make it live %@ : %@"
- "URLIsOnKnownImageMount:"
- "bundleIDIsOnKnownImageMount:"
- "diskImageAppBundleIDs"
- "diskImageAppInfoForBundleID:"
- "diskMountPaths"
- "markContainerAsStagedUpdateContainer:"

```
