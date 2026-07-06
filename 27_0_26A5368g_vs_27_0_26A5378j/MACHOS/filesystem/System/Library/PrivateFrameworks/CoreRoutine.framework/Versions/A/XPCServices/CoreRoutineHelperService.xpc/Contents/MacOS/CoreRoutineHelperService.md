## CoreRoutineHelperService

> `/System/Library/PrivateFrameworks/CoreRoutine.framework/Versions/A/XPCServices/CoreRoutineHelperService.xpc/Contents/MacOS/CoreRoutineHelperService`

```diff

-  __TEXT.__text: 0xc48a0
+  __TEXT.__text: 0xc4ee8
   __TEXT.__auth_stubs: 0xd70
-  __TEXT.__objc_stubs: 0x5d00
-  __TEXT.__objc_methlist: 0x33c4
+  __TEXT.__objc_stubs: 0x5de0
+  __TEXT.__objc_methlist: 0x346c
   __TEXT.__const: 0x1438
-  __TEXT.__oslogstring: 0x3178
-  __TEXT.__cstring: 0x3acb6
+  __TEXT.__oslogstring: 0x326a
+  __TEXT.__cstring: 0x3acf4
   __TEXT.__objc_classname: 0x5b5
-  __TEXT.__objc_methname: 0x9b7c
-  __TEXT.__objc_methtype: 0x3b46
+  __TEXT.__objc_methname: 0x9e84
+  __TEXT.__objc_methtype: 0x3b9a
   __TEXT.__gcc_except_tab: 0x218c
   __TEXT.__unwind_info: 0x10e0
   __DATA_CONST.__const: 0x1158
-  __DATA_CONST.__cfstring: 0x1fd60
+  __DATA_CONST.__cfstring: 0x1fda0
   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0xe8

   __DATA_CONST.__objc_arrayobj: 0x120
   __DATA_CONST.__objc_doubleobj: 0xa0
   __DATA_CONST.__auth_got: 0x6d0
-  __DATA_CONST.__got: 0x568
+  __DATA_CONST.__got: 0x588
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x3898
-  __DATA.__objc_selrefs: 0x2770
-  __DATA.__objc_ivar: 0x170
+  __DATA.__objc_const: 0x3938
+  __DATA.__objc_selrefs: 0x27e8
+  __DATA.__objc_ivar: 0x178
   __DATA.__objc_data: 0xa50
   __DATA.__data: 0xbc0
   __DATA.__bss: 0x128

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1209
+  Functions: 1219
   Symbols:   460
-  CStrings:  10359
+  CStrings:  10386
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
CStrings:
+ "%@, blended POI muid %@, rankProb %.6f, sigmaProb %.6f, weight %.4f, blended %.6f"
+ "%@, invalid distancePriorWeight %.6f, expected [0, 1]"
+ "%@, tile missing distancePriorWeight, computed default %.6f from modelCoveredMuids count %lu, threshold %u"
+ "@56@0:8@16@24@32@40d48"
+ "Skipping distance model for high density area"
+ "TB,N,V_disableDistancePriorForHighDensity"
+ "Td,N,V_distancePriorWeight"
+ "_disableDistancePriorForHighDensity"
+ "_distancePriorWeight"
+ "createFloorMapForLOI:reply:"
+ "createFloorMapForVisit:reply:"
+ "disableDistancePriorForHighDensity"
+ "disable_distance_prior_for_high_density"
+ "distancePriorWeight"
+ "distance_prior_weight"
+ "fetchTransactionDiagnosticsSampledWithReply:"
+ "hasDisableDistancePriorForHighDensity"
+ "hasDistancePriorWeight"
+ "initWithIdentifier:apToModelMapping:date:disableDistancePriorForHighDensity:distancePriorWeight:distancePriors:downloadKey:geoCacheInfo:geoTileKey:hashedApToModelMapping:hashedApToModelMappingDataURL:hashSalt:modelCalibrationParameters:models:modelURLs:pointsOfInterest:singlePOIMuid:size:"
+ "probabilityDistributionOfNearbyPointsOfInterestsWithReferenceLocation:pointsOfInterest:modelCoveredMuids:distancePriors:distancePriorWeight:"
+ "rankBasedDistributionWithReferenceLocation:pointsOfInterest:modelCoveredMuids:distancePriors:"
+ "setDisableDistancePriorForHighDensity:"
+ "setDistancePriorWeight:"
+ "setHasDisableDistancePriorForHighDensity:"
+ "setHasDistancePriorWeight:"
+ "setTransactionDiagnosticsSampled:reply:"
+ "sigmaBasedDistributionWithReferenceLocation:pointsOfInterest:modelCoveredMuids:"
+ "unionSet:"
+ "{?=\"distancePriorWeight\"b1\"tileKey\"b1\"disableDistancePriorForHighDensity\"b1}"
+ "\x89"
- "Skipping distance model: model has %lu classes"
- "initWithIdentifier:apToModelMapping:date:distancePriors:downloadKey:geoCacheInfo:geoTileKey:hashedApToModelMapping:hashedApToModelMappingDataURL:hashSalt:modelCalibrationParameters:models:modelURLs:pointsOfInterest:singlePOIMuid:size:"
- "probabilityDistributionOfNearbyPointsOfInterestsWithReferenceLocation:pointsOfInterest:modelCoveredMuids:distancePriors:"
- "y"
- "{?=\"tileKey\"b1}"

```
