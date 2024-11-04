## MediaPlayer

> `/System/Library/Frameworks/MediaPlayer.framework/MediaPlayer`

```diff

-4024.300.15.0.0
-  __TEXT.__text: 0x336174
-  __TEXT.__auth_stubs: 0x5030
-  __TEXT.__objc_methlist: 0x23a88
-  __TEXT.__cstring: 0x2d192
+4024.300.24.0.0
+  __TEXT.__text: 0x335224
+  __TEXT.__auth_stubs: 0x5040
+  __TEXT.__objc_methlist: 0x23a98
+  __TEXT.__cstring: 0x2cf83
   __TEXT.__const: 0x16bd8
   __TEXT.__constg_swiftt: 0x80
   __TEXT.__swift5_typeref: 0x42

   __TEXT.__swift5_fieldmd: 0x2c
   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_types: 0x8
-  __TEXT.__gcc_except_tab: 0x18b34
-  __TEXT.__oslogstring: 0x13c15
+  __TEXT.__gcc_except_tab: 0x18b08
+  __TEXT.__oslogstring: 0x13b2c
   __TEXT.__dlopen_cstrs: 0x4bd
   __TEXT.__ustring: 0x1ca
-  __TEXT.__unwind_info: 0xc048
+  __TEXT.__unwind_info: 0xbfb8
   __TEXT.__eh_frame: 0x1538
   __TEXT.__objc_classname: 0x5fc6
-  __TEXT.__objc_methname: 0x5e5d3
+  __TEXT.__objc_methname: 0x5e5ee
   __TEXT.__objc_methtype: 0xd9dd
-  __TEXT.__objc_stubs: 0x30de0
-  __DATA_CONST.__got: 0x2df8
-  __DATA_CONST.__const: 0xce48
+  __TEXT.__objc_stubs: 0x30c20
+  __DATA_CONST.__got: 0x2e08
+  __DATA_CONST.__const: 0xce18
   __DATA_CONST.__objc_classlist: 0x1458
   __DATA_CONST.__objc_catlist: 0x108
   __DATA_CONST.__objc_protolist: 0x3f8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11e38
+  __DATA_CONST.__objc_selrefs: 0x11e30
   __DATA_CONST.__objc_protorefs: 0xd8
   __DATA_CONST.__objc_superrefs: 0xd48
   __DATA_CONST.__objc_arraydata: 0x7e0
-  __AUTH_CONST.__auth_got: 0x2830
+  __AUTH_CONST.__auth_got: 0x2838
   __AUTH_CONST.__auth_ptr: 0x90
-  __AUTH_CONST.__const: 0xe800
-  __AUTH_CONST.__cfstring: 0x24a00
-  __AUTH_CONST.__objc_const: 0x48038
-  __AUTH_CONST.__objc_intobj: 0x888
+  __AUTH_CONST.__const: 0xe7e0
+  __AUTH_CONST.__cfstring: 0x24700
+  __AUTH_CONST.__objc_const: 0x48058
+  __AUTH_CONST.__objc_intobj: 0x870
   __AUTH_CONST.__objc_arrayobj: 0xe58
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0xa140
   __AUTH.__data: 0xd8
-  __DATA.__objc_ivar: 0x2ad4
+  __DATA.__objc_ivar: 0x2ad8
   __DATA.__data: 0x3418
-  __DATA.__bss: 0xd10
+  __DATA.__bss: 0xce0
   __DATA.__common: 0xa25
   __DATA_DIRTY.__objc_data: 0x29e0
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x268
+  __DATA_DIRTY.__bss: 0x270
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 16253
-  Symbols:   20725
-  CStrings:  22649
+  Functions: 16251
+  Symbols:   20728
+  CStrings:  22622
 
Symbols:
+ _ICStoreArtworkInfoImageFormatJPEG
+ _MSVCurrentProcessIsNonUIPlaybackService
+ _OBJC_CLASS_$_MRAVOutputDeviceSymbolProvider
+ _OBJC_CLASS_$_MRDeviceIdentifierSymbolProvider
- _OBJC_CLASS_$_ISSymbol
CStrings:
+ "@\"NSArray\"16@?0@\"MPAVRoute\"8"
+ "Invalid request database path=%!@(MISSING), mediaLibrary=%!@(MISSING)"
+ "MPAVItem playerItem property is being used without prior loadAssetAndPlayerItem %!{(MISSING)public}@"
+ "SELECT child_identifier FROM object_relationships WHERE parent_identifier = @parentIdentifier AND person_id = @personID AND parent_version_hash = @parentVersionHash AND child_key = @childKey ORDER BY suborder"
+ "_orderedSectionIDs"
+ "_relatedIdentifierSetsForParentIdentifierSet:parentVersionHash:childKey:"
+ "_updateOrderedSectionIDsWithExclusiveAccessToken:"
+ "_validateRequest"
+ "currentDeviceRoutingSymbolName"
+ "osi"
+ "symbolNameForModelID:"
+ "symbolNameForOutputDevices:"
+ "symbolNameForProductIdentifier:"
- "Failed to find bluetooth symbol with model: %!{(MISSING)public}@ uti: %!{(MISSING)public}@ error: %!{(MISSING)public}@"
- "Failed to find product symbol with model: %!{(MISSING)public}@ uti: %!{(MISSING)public}@ error: %!{(MISSING)public}@"
- "Failed to find symbol with uti: %!{(MISSING)public}@ error: %!{(MISSING)public}@"
- "MPAVItem player property is being used without prior loadAssetAndPlayerItem %!{(MISSING)public}@"
- "SELECT child_identifier, token FROM object_relationships LEFT OUTER JOIN playback_authorization_token ON child_identifier = identifier WHERE parent_identifier = @parentIdentifier AND object_relationships.person_id = @personID AND child_key = @childKey AND parent_version_hash = @parentVersionHash ORDER BY suborder"
- "_fallbackSymbolNameForRoute:"
- "_symbolNameForClusterRoute:"
- "_symbolNameMap"
- "_typeOfCurrentDevice"
- "_typeWithBluetoothProductID:vendorID:"
- "_typeWithDeviceModelCode:"
- "appletv.fill"
- "beatslogo"
- "car.fill"
- "carplay"
- "hearingdevice.ear"
- "hifispeaker.2.fill"
- "hifispeaker.and.appletv"
- "hifispeaker.and.homepod.fill"
- "hifispeaker.and.homepodmini.fill"
- "hifispeaker.fill"
- "homepod.2.fill"
- "homepod.and.appletv.fill"
- "homepod.and.homepodmini.fill"
- "homepod.fill"
- "homepodmini.2.fill"
- "homepodmini.and.appletv.fill"
- "homepodmini.fill"
- "letterCharacterSet"
- "mediastick"
- "person.2.fill"
- "speaker.bluetooth.fill"
- "speaker.wave.2.fill"
- "symbolForTypeIdentifier:withResolutionStrategy:variantOptions:error:"
- "tv.and.mediabox"
- "tv.inset.filled"
- "v32@?0@\"MPAVRoute\"8q16@\"NSString\"24"
- "versionHash != nil"
- "vision.pro"

```
