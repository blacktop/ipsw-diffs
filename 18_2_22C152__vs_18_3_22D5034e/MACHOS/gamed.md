## gamed

> `/usr/libexec/gamed`

```diff

-819.2.13.0.0
-  __TEXT.__text: 0x221e68
-  __TEXT.__auth_stubs: 0x2e80
-  __TEXT.__objc_stubs: 0x18fc0
-  __TEXT.__objc_methlist: 0xb45c
-  __TEXT.__const: 0x12500
+819.3.4.0.0
+  __TEXT.__text: 0x222504
+  __TEXT.__auth_stubs: 0x2ea0
+  __TEXT.__objc_stubs: 0x19040
+  __TEXT.__objc_methlist: 0xb47c
+  __TEXT.__const: 0x124a0
   __TEXT.__objc_classname: 0x1d70
-  __TEXT.__oslogstring: 0x1548b
-  __TEXT.__objc_methname: 0x2074e
-  __TEXT.__cstring: 0x1a47a
-  __TEXT.__objc_methtype: 0x5b77
+  __TEXT.__oslogstring: 0x155cb
+  __TEXT.__objc_methname: 0x207b7
+  __TEXT.__cstring: 0x1a43a
+  __TEXT.__objc_methtype: 0x5bc1
   __TEXT.__gcc_except_tab: 0x31ec
-  __TEXT.__swift5_typeref: 0x1af0
-  __TEXT.__constg_swiftt: 0x1590
-  __TEXT.__swift5_reflstr: 0xd4a
-  __TEXT.__swift5_fieldmd: 0x126c
+  __TEXT.__swift5_typeref: 0x1b68
+  __TEXT.__constg_swiftt: 0x1584
+  __TEXT.__swift5_reflstr: 0xd2a
+  __TEXT.__swift5_fieldmd: 0x1278
   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_types: 0x184
-  __TEXT.__swift5_capture: 0xa38
+  __TEXT.__swift5_capture: 0xa4c
   __TEXT.__swift5_protos: 0x1c
   __TEXT.__swift5_proto: 0x218
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__unwind_info: 0x70d8
-  __TEXT.__eh_frame: 0x68d0
-  __DATA_CONST.__auth_got: 0x1758
-  __DATA_CONST.__got: 0x1918
-  __DATA_CONST.__auth_ptr: 0x8a8
-  __DATA_CONST.__const: 0x11538
-  __DATA_CONST.__cfstring: 0xbf00
+  __TEXT.__unwind_info: 0x7100
+  __TEXT.__eh_frame: 0x6990
+  __DATA_CONST.__auth_got: 0x1768
+  __DATA_CONST.__got: 0x1908
+  __DATA_CONST.__auth_ptr: 0x8b8
+  __DATA_CONST.__const: 0x11678
+  __DATA_CONST.__cfstring: 0xbf20
   __DATA_CONST.__objc_classlist: 0x8e8
   __DATA_CONST.__objc_catlist: 0x130
   __DATA_CONST.__objc_protolist: 0x208

   __DATA_CONST.__objc_arraydata: 0x398
   __DATA_CONST.__objc_dictobj: 0x280
   __DATA_CONST.__objc_arrayobj: 0x150
-  __DATA.__objc_const: 0x225a0
-  __DATA.__objc_selrefs: 0x77f0
+  __DATA.__objc_const: 0x225c0
+  __DATA.__objc_selrefs: 0x7808
   __DATA.__objc_ivar: 0x754
   __DATA.__objc_data: 0x6638
-  __DATA.__data: 0x4b28
+  __DATA.__data: 0x4a78
   __DATA.__bss: 0x43f8
   __DATA.__common: 0xe4
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 9444
+  Functions: 9462
   Symbols:   1785
-  CStrings:  10227
+  CStrings:  10235
 
Symbols:
+ _$sSS10FoundationE4data8encodingSSSgAA4DataVh_SSAAE8EncodingVtcfC
+ _$sSS10FoundationE8EncodingV4utf8ACvgZ
+ _$sSS10FoundationE8EncodingVMa
- _$sScg4next9isolationxSgScA_pSgYi_tYaKF
- _$sScg4next9isolationxSgScA_pSgYi_tYaKFTu
- _OBJC_CLASS_$_NSISO8601DateFormatter
CStrings:
+ "-[GKGameServicePrivate getAppMetadataForBundleIDs:adamIDs:ttlOption:withCompletion:]"
+ "Failed to create JSON data for response item: %s, error: %@"
+ "Failed to start contacts controller as part of UI launching. Error: %@"
+ "Failed to update metadata cache for game: %@"
+ "Finished fetching metadata as part of game UI launching: %@"
+ "GKUtilityService: willLaunchGameCenterUIForGameDescriptor:completionHandler"
+ "No tasks to perform, returning nil."
+ "Vv32@0:8@\"GKGameDescriptor\"16@?<v@?@\"NSError\">24"
+ "Vv48@0:8@\"NSArray\"16@\"NSArray\"24q32@?<v@?@\"NSDictionary\"@\"NSError\">40"
+ "Vv48@0:8@16@24q32@?40"
+ "artwork,bundleId,deviceFamilies,name,shortName,supportsArcade,supportsGameController,isGameCenterEnabled,offers"
+ "can-receive-friend-invitation"
+ "getAppMetadataForBundleIDs:adamIDs:ttlOption:withCompletion:"
+ "getFriendIDsForPlayer: filter %d kept %lu player IDs from %lu filterable friends"
+ "getFriendIDsForPlayer: returning nil because no playerID set"
+ "initWithBundleID:adamID:name:shortName:artwork:supportsGameCenter:supportsArcade:supportsGameController:deviceFamilies:genreDisplayName:rawResponse:"
+ "rawResponse"
+ "refreshAppMetadataForGameDescriptor:"
+ "setIncludeArcade:"
+ "shouldUseGameOverlayUI"
+ "willLaunchGameCenterUIForGameDescriptor:completionHandler:"
- "-[GKGameServicePrivate getAppMetadataForBundleIDs:adamIDs:withCompletion:]"
- "Failed to refresh expired adamIDs with error: %@"
- "No IDs to fetch, returning nil."
- "Vv40@0:8@\"NSArray\"16@\"NSArray\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
- "artwork,bundleId,deviceFamilies,latestVersionInfo,name,shortName,supportsArcade,supportsGameController,isGameCenterEnabled"
- "dateFromString:"
- "getAppMetadataForBundleIDs:adamIDs:withCompletion:"
- "getFriendIDsForPlayer: filter %d kept %lu player IDs from %lu filterable players"
- "initWithBundleID:adamID:name:shortName:artwork:supportsGameCenter:supportsArcade:supportsGameController:deviceFamilies:latestVersionReleaseDate:genreDisplayName:"
- "latestVersionInfo"
- "latestVersionReleaseDate"
- "releaseTimestamp"

```
