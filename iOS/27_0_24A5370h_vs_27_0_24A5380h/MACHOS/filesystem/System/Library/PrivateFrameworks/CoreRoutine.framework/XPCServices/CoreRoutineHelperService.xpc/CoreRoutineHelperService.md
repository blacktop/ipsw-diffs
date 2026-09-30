## CoreRoutineHelperService

> `/System/Library/PrivateFrameworks/CoreRoutine.framework/XPCServices/CoreRoutineHelperService.xpc/CoreRoutineHelperService`

```diff

-  __TEXT.__text: 0xc2af8
+  __TEXT.__text: 0xc311c
   __TEXT.__auth_stubs: 0xf40
-  __TEXT.__objc_stubs: 0x5e00
-  __TEXT.__objc_methlist: 0x3544
+  __TEXT.__objc_stubs: 0x5ee0
+  __TEXT.__objc_methlist: 0x35ec
   __TEXT.__const: 0x1428
   __TEXT.__objc_classname: 0x5ce
-  __TEXT.__objc_methtype: 0x3d07
-  __TEXT.__oslogstring: 0x31a2
-  __TEXT.__cstring: 0x3addf
-  __TEXT.__objc_methname: 0x9ed1
-  __TEXT.__gcc_except_tab: 0x2194
+  __TEXT.__objc_methtype: 0x3d5b
+  __TEXT.__oslogstring: 0x3294
+  __TEXT.__cstring: 0x3ae1d
+  __TEXT.__objc_methname: 0xa1d9
+  __TEXT.__gcc_except_tab: 0x2190
   __TEXT.__unwind_info: 0x10e0
   __DATA_CONST.__const: 0xff0
-  __DATA_CONST.__cfstring: 0x1ff00
+  __DATA_CONST.__cfstring: 0x1ff40
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0xe8

   __DATA_CONST.__objc_arrayobj: 0x120
   __DATA_CONST.__objc_doubleobj: 0xa0
   __DATA_CONST.__auth_got: 0x7b8
-  __DATA_CONST.__got: 0x588
+  __DATA_CONST.__got: 0x5a8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x39e8
-  __DATA.__objc_selrefs: 0x2808
-  __DATA.__objc_ivar: 0x178
+  __DATA.__objc_const: 0x3a88
+  __DATA.__objc_selrefs: 0x2880
+  __DATA.__objc_ivar: 0x180
   __DATA.__objc_data: 0xaa0
   __DATA.__data: 0xbc0
   __DATA.__bss: 0x128

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1203
+  Functions: 1213
   Symbols:   494
-  CStrings:  10421
+  CStrings:  10448
 
Sections:
~ __TEXT.__const : content changed
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
