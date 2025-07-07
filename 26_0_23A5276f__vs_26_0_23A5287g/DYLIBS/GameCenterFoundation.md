## GameCenterFoundation

> `/System/Library/PrivateFrameworks/GameCenterFoundation.framework/GameCenterFoundation`

```diff

-820.0.59.0.0
-  __TEXT.__text: 0x166828
-  __TEXT.__auth_stubs: 0x27d0
-  __TEXT.__objc_methlist: 0x12034
-  __TEXT.__cstring: 0x19693
-  __TEXT.__const: 0x5b88
+820.0.64.0.0
+  __TEXT.__text: 0x166a20
+  __TEXT.__auth_stubs: 0x27e0
+  __TEXT.__objc_methlist: 0x1205c
+  __TEXT.__cstring: 0x196b3
+  __TEXT.__const: 0x5b70
   __TEXT.__gcc_except_tab: 0x1450
   __TEXT.__oslogstring: 0xd9eb
   __TEXT.__ustring: 0x18
   __TEXT.__dlopen_cstrs: 0xba
   __TEXT.__swift5_typeref: 0x1ef2
-  __TEXT.__swift5_capture: 0x8d0
+  __TEXT.__swift5_capture: 0x8c0
   __TEXT.__swift5_fieldmd: 0x16c0
   __TEXT.__constg_swiftt: 0x184c
   __TEXT.__swift5_reflstr: 0x10d3

   __TEXT.__swift_as_entry: 0x190
   __TEXT.__swift_as_ret: 0x1dc
   __TEXT.__swift5_mpenum: 0x48
-  __TEXT.__unwind_info: 0x64c0
+  __TEXT.__unwind_info: 0x64b8
   __TEXT.__eh_frame: 0x5480
-  __TEXT.__objc_classname: 0x1ea6
-  __TEXT.__objc_methname: 0x268ee
-  __TEXT.__objc_methtype: 0x62de
+  __TEXT.__objc_classname: 0x1ea9
+  __TEXT.__objc_methname: 0x269e8
+  __TEXT.__objc_methtype: 0x62ea
   __TEXT.__objc_stubs: 0x14d60
   __DATA_CONST.__got: 0x10c8
-  __DATA_CONST.__const: 0x6070
+  __DATA_CONST.__const: 0x6048
   __DATA_CONST.__objc_classlist: 0x808
   __DATA_CONST.__objc_catlist: 0x100
   __DATA_CONST.__objc_protolist: 0x228
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8418
+  __DATA_CONST.__objc_selrefs: 0x8430
   __DATA_CONST.__objc_protorefs: 0x128
   __DATA_CONST.__objc_superrefs: 0x4f8
   __DATA_CONST.__objc_arraydata: 0x280
-  __AUTH_CONST.__auth_got: 0x13f8
-  __AUTH_CONST.__const: 0x57d0
-  __AUTH_CONST.__cfstring: 0x11140
-  __AUTH_CONST.__objc_const: 0x24418
+  __AUTH_CONST.__auth_got: 0x1400
+  __AUTH_CONST.__const: 0x57a8
+  __AUTH_CONST.__cfstring: 0x11180
+  __AUTH_CONST.__objc_const: 0x244a8
   __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH.__objc_data: 0x2b48
   __AUTH.__data: 0x1128
-  __DATA.__objc_ivar: 0xfec
+  __DATA.__objc_ivar: 0xff8
   __DATA.__data: 0x3970
   __DATA.__bss: 0x8320
   __DATA.__common: 0x20

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: ADADFAA9-FA13-3BE2-B2A6-09FF76004E51
-  Functions: 10734
-  Symbols:   24464
-  CStrings:  13498
+  UUID: 6D912747-C16E-3C97-A6D1-1A3F8B82C8E2
+  Functions: 10737
+  Symbols:   24480
+  CStrings:  13511
 
Symbols:
+ -[GKAppMetadata initWithBundleID:adamID:platform:name:shortName:artwork:customIconArtwork:supportsGameCenter:supportsArcade:supportsGameController:isEligibleForGamesApp:supportedGameCenterFeatures:deviceFamilies:genreDisplayName:rawResponse:isIOSBinaryMacOSCompatible:]
+ -[GKAppMetadata isIOSBinaryMacOSCompatible]
+ -[GKInstallMetadata initWithBundleID:adamID:bundleShortVersion:name:shortName:estimatedInstallDate:supportsGameController:isArcade:platform:isHidden:metadataEligibility:applicationType:isBeta:persistentRecordID:]
+ -[GKInstallMetadata isBeta]
+ -[GKInstallMetadata persistentRecordID]
+ _OBJC_IVAR_$_GKAppMetadata._isIOSBinaryMacOSCompatible
+ _OBJC_IVAR_$_GKInstallMetadata._isBeta
+ _OBJC_IVAR_$_GKInstallMetadata._persistentRecordID
+ _block_copy_helper.189
+ _block_copy_helper.212
+ _block_descriptor.191
+ _block_descriptor.214
+ _block_destroy_helper.190
+ _block_destroy_helper.213
+ _objectdestroy.153Tm
+ _objectdestroy.164Tm
- -[GKAppMetadata initWithBundleID:adamID:platform:name:shortName:artwork:customIconArtwork:supportsGameCenter:supportsArcade:supportsGameController:isEligibleForGamesApp:supportedGameCenterFeatures:deviceFamilies:genreDisplayName:rawResponse:]
- -[GKInstallMetadata initWithBundleID:adamID:bundleShortVersion:name:shortName:estimatedInstallDate:supportsGameController:isArcade:platform:isHidden:metadataEligibility:applicationType:]
- _OUTLINED_FUNCTION_184
- _OUTLINED_FUNCTION_185
- ___block_descriptor_56_e8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
- _block_copy_helper.193
- _block_copy_helper.226
- _block_descriptor.195
- _block_descriptor.228
- _block_destroy_helper.194
- _block_destroy_helper.227
- _objectdestroy.157Tm
- _objectdestroy.168Tm
CStrings:
+ "@112@0:8@16@24@32@40@48@56B64B68q72B80q84q92B100@104"
+ "@132@0:8@16@24@32@40@48@56@64@72B80@84B92@96@104@112@120B128"
+ "T@\"NSData\",R,N,V_persistentRecordID"
+ "TB,R,N,V_isBeta"
+ "TB,R,N,V_isIOSBinaryMacOSCompatible"
+ "Tq,R,N,V_applicationType"
+ "Tq,R,N,V_metadataEligibility"
+ "_isBeta"
+ "_isIOSBinaryMacOSCompatible"
+ "_persistentRecordID"
+ "initWithBundleID:adamID:bundleShortVersion:name:shortName:estimatedInstallDate:supportsGameController:isArcade:platform:isHidden:metadataEligibility:applicationType:isBeta:persistentRecordID:"
+ "initWithBundleID:adamID:platform:name:shortName:artwork:customIconArtwork:supportsGameCenter:supportsArcade:supportsGameController:isEligibleForGamesApp:supportedGameCenterFeatures:deviceFamilies:genreDisplayName:rawResponse:isIOSBinaryMacOSCompatible:"
+ "isBeta"
+ "isIOSBinaryMacOSCompatible"
+ "persistentRecordID"
- "@100@0:8@16@24@32@40@48@56B64B68q72B80Q84Q92"
- "@128@0:8@16@24@32@40@48@56@64@72B80@84B92@96@104@112@120"
- "TQ,R,N,V_applicationType"
- "TQ,R,N,V_metadataEligibility"
- "initWithBundleID:adamID:bundleShortVersion:name:shortName:estimatedInstallDate:supportsGameController:isArcade:platform:isHidden:metadataEligibility:applicationType:"
- "initWithBundleID:adamID:platform:name:shortName:artwork:customIconArtwork:supportsGameCenter:supportsArcade:supportsGameController:isEligibleForGamesApp:supportedGameCenterFeatures:deviceFamilies:genreDisplayName:rawResponse:"

```
