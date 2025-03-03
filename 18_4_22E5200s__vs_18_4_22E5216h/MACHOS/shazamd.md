## shazamd

> `/System/Library/Frameworks/ShazamKit.framework/shazamd`

```diff

-312.0.0.0.0
-  __TEXT.__text: 0x4620c
-  __TEXT.__auth_stubs: 0x770
-  __TEXT.__objc_stubs: 0xb960
-  __TEXT.__objc_methlist: 0x578c
+316.0.0.0.0
+  __TEXT.__text: 0x466ec
+  __TEXT.__auth_stubs: 0x780
+  __TEXT.__objc_stubs: 0xba40
+  __TEXT.__objc_methlist: 0x57e4
   __TEXT.__const: 0x160
   __TEXT.__gcc_except_tab: 0xca0
-  __TEXT.__objc_methname: 0xef2b
-  __TEXT.__cstring: 0x2591
-  __TEXT.__oslogstring: 0x3923
-  __TEXT.__objc_classname: 0x12da
-  __TEXT.__objc_methtype: 0x2bc9
+  __TEXT.__objc_methname: 0xf06b
+  __TEXT.__cstring: 0x25f2
+  __TEXT.__oslogstring: 0x39be
+  __TEXT.__objc_classname: 0x12f1
+  __TEXT.__objc_methtype: 0x2c88
   __TEXT.__ustring: 0x164
-  __TEXT.__unwind_info: 0x12b8
-  __DATA_CONST.__auth_got: 0x3d0
-  __DATA_CONST.__got: 0x7d8
+  __TEXT.__unwind_info: 0x12e0
+  __DATA_CONST.__auth_got: 0x3d8
+  __DATA_CONST.__got: 0x7e0
   __DATA_CONST.__const: 0x1698
-  __DATA_CONST.__cfstring: 0x21c0
-  __DATA_CONST.__objc_classlist: 0x480
+  __DATA_CONST.__cfstring: 0x21e0
+  __DATA_CONST.__objc_classlist: 0x488
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x1c0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x358
+  __DATA_CONST.__objc_superrefs: 0x350
   __DATA_CONST.__objc_intobj: 0xa8
-  __DATA.__objc_const: 0xc058
-  __DATA.__objc_selrefs: 0x3480
+  __DATA.__objc_const: 0xc108
+  __DATA.__objc_selrefs: 0x34c8
   __DATA.__objc_ivar: 0x574
-  __DATA.__objc_data: 0x2d00
+  __DATA.__objc_data: 0x2d50
   __DATA.__data: 0x1500
   __DATA.__bss: 0x100
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1672
-  Symbols:   385
-  CStrings:  3527
+  Functions: 1679
+  Symbols:   387
+  CStrings:  3543
 
Symbols:
+ _CLLocationCoordinate2DMake
+ _OBJC_CLASS_$_SHLocationTransformer
+ _SHMediaItemMatchLocationCoordinate
- _SHMediaItemMatchLocation
CStrings:
+ "@\"SHMusicalFeaturesBagConfiguration\""
+ "@32@0:8{CLLocationCoordinate2D=dd}16"
+ "Error occured with serializing raw response %@"
+ "Error occured with serializing song response for AdamID %@. Error: %@"
+ "Models available for %@ are CREMA %d and CREPE %d with minimum signature duration of %f"
+ "SHLLibraryTrackLocationLatitude"
+ "SHLLibraryTrackLocationLongitude"
+ "SHLLocationTransformer"
+ "SHMediaLibraryDataStoreRawResponseSongsData"
+ "T@\"SHMusicalFeaturesBagConfiguration\",R,N,V_configuration"
+ "T{CLLocationCoordinate2D=dd},D,N"
+ "T{CLLocationCoordinate2D=dd},N,V_locationCoordinate"
+ "_locationCoordinate"
+ "coordinateFromLocation:"
+ "coordinateValueFromLocation:"
+ "dataFromManagedObjectRawResponseDictionary:"
+ "initWithCremaModelURL:crepeModelURL:minimumDuration:error:"
+ "initWithCremaModelURL:minimumDuration:error:"
+ "initWithCrepeModelURL:minimumDuration:error:"
+ "initWithTrackSyncID:creationDate:releaseDate:groupSyncID:labels:lastUpdatedDate:providerIdentifier:trackMetadata:providerName:shazamKey:recognitionID:title:subtitle:artworkURL:appleMusicID:appleMusicURL:shazamURL:videoURL:isExplicit:albumName:isrc:shazamCount:locationCoordinate:genres:rawSongResponse:"
+ "locationCoordinate"
+ "locationCoordinateFromCoder:"
+ "locationFromCoordinate:"
+ "minimumDurationInSecondsForClientIdentifier:"
+ "minimumDurationPerCurrentIdentifier"
+ "musicalFeaturesBagConfigurationWithPromise"
+ "rawResponseDataWithCampaignToken:"
+ "setLocationCoordinate:"
+ "set_rawResponseSongsData:"
+ "sh_ShazamKitBundle"
+ "v32@0:8{CLLocationCoordinate2D=dd}16"
+ "{CLLocationCoordinate2D=\"latitude\"d\"longitude\"d}"
+ "{CLLocationCoordinate2D=dd}16@0:8"
+ "{CLLocationCoordinate2D=dd}24@0:8@16"
- "@\"SHMusicalFeaturesModelsConfiguration\""
- "Models available for %@ are CREMA %d and CREPE %d"
- "T@\"CLLocation\",&,D,N"
- "T@\"NSURL\",R,N,V_cremaModelURL"
- "T@\"NSURL\",R,N,V_crepeModelURL"
- "T@\"SHMusicalFeaturesModelsConfiguration\",R,N,V_configuration"
- "_cremaModelURL"
- "_crepeModelURL"
- "crema"
- "crepe"
- "initWithCremaModelURL:crepeModelURL:error:"
- "initWithCremaModelURL:error:"
- "initWithCremaURL:crepeModelURL:"
- "initWithCrepeModelURL:error:"
- "initWithTrackSyncID:creationDate:releaseDate:groupSyncID:labels:lastUpdatedDate:providerIdentifier:trackMetadata:providerName:shazamKey:recognitionID:title:subtitle:artworkURL:appleMusicID:appleMusicURL:shazamURL:videoURL:isExplicit:albumName:isrc:shazamCount:location:genres:rawSongResponse:"
- "musicalFeaturesConfigurationWithPromise"
- "rawResponseWithCampaignToken:"
- "set_rawResponseSongs:"

```
