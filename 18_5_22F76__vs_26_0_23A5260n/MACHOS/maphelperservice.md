## maphelperservice

> `/System/Library/Frameworks/CoreLocation.framework/XPCServices/maphelperservice.xpc/maphelperservice`

```diff

-2964.0.4.0.0
-  __TEXT.__text: 0x1ac0
-  __TEXT.__auth_stubs: 0x2e0
-  __TEXT.__objc_stubs: 0x9a0
-  __TEXT.__objc_methlist: 0x214
-  __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x618
+3051.0.3.0.0
+  __TEXT.__text: 0xb610
+  __TEXT.__auth_stubs: 0x640
+  __TEXT.__objc_stubs: 0xba0
+  __TEXT.__objc_methlist: 0x27c
+  __TEXT.__const: 0x40c
+  __TEXT.__gcc_except_tab: 0xcac
+  __TEXT.__cstring: 0xcc4
   __TEXT.__oslogstring: 0x1a7
   __TEXT.__objc_classname: 0x6b
-  __TEXT.__objc_methname: 0x873
-  __TEXT.__objc_methtype: 0x250
-  __TEXT.__gcc_except_tab: 0x44
-  __TEXT.__unwind_info: 0xc8
-  __DATA_CONST.__auth_got: 0x180
-  __DATA_CONST.__got: 0x60
-  __DATA_CONST.__const: 0xd8
-  __DATA_CONST.__cfstring: 0x660
+  __TEXT.__objc_methname: 0xc45
+  __TEXT.__objc_methtype: 0x4c0
+  __TEXT.__unwind_info: 0x418
+  __DATA_CONST.__auth_got: 0x330
+  __DATA_CONST.__got: 0xb8
+  __DATA_CONST.__const: 0x398
+  __DATA_CONST.__cfstring: 0xba0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x438
-  __DATA.__objc_selrefs: 0x340
-  __DATA.__objc_ivar: 0x1c
+  __DATA.__objc_const: 0x4c8
+  __DATA.__objc_selrefs: 0x3d0
+  __DATA.__objc_ivar: 0x24
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x120
+  __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf.dylib
-  UUID: 0CDDEB94-294D-375E-8F86-BBB4A34E7FCD
-  Functions: 21
-  Symbols:   81
-  CStrings:  260
+  UUID: BBE2CCF4-1D69-381F-8E70-9DB8F8ADFF70
+  Functions: 184
+  Symbols:   222
+  CStrings:  400
 
Symbols:
+ __ZN11CLRouteRoad10initializeENSt3__110shared_ptrI9CLMapRoadEE
+ __ZN11CLRouteRoad25isConnectedToStopJunctionERKNSt3__110shared_ptrIS_EE
+ __ZN11CLRouteRoad26isConnectedToStartJunctionERKNSt3__110shared_ptrIS_EE
+ __ZN11CLRouteRoad8isSameAsERKNSt3__110shared_ptrIS_EE
+ __ZN14CLDistanceCalc14calculateRadiiERKd
+ __ZN14CLDistanceCalc16calculateAzimuthERK16CLDaemonLocationS2_
+ __ZN14CLDistanceCalc16calculateAzimuthEdddd
+ __ZN14CLDistanceCalc17calculateDistanceERK16CLDaemonLocationS2_
+ __ZN14CLDistanceCalc17calculateDistanceERK16CLDaemonLocationdd
+ __ZN14CLDistanceCalc17calculateDistanceEddddd
+ __ZN14CLDistanceCalc17getDeltaLongitudeEdd
+ __ZN14CLDistanceCalc17propagateLocationEddddddPdS0_
+ __ZN14CLDistanceCalc19calculateDistance3DEdddddd
+ __ZN14CLDistanceCalc21calculateDistanceFastEdddd
+ __ZN14CLDistanceCalc22calculatePosDifferenceEddddddRdS0_S0_
+ __ZN14CLDistanceCalc25calculateAlongAcrossTrackEddddddRdS0_
+ __ZN14CLDistanceCalc25calculateDistanceVincentyERK16CLDaemonLocationS2_
+ __ZN14CLDistanceCalc25calculateDistanceVincentyEdddd
+ __ZN14CLDistanceCalc25calculateNewPosUsingDeltaEddddddRdS0_S0_
+ __ZN14CLDistanceCalc30calculateDistanceHighPrecisionEdddd
+ __ZN14CLDistanceCalc31calculateNewPosUsingAcrossTrackEdddddRdS0_
+ __ZN14CLDistanceCalc32calculateNewPosUsingDeltaNoLimitEddddddRdS0_S0_
+ __ZN14CLDistanceCalc36calculatePosDifferenceWithArcMethodsEddddddPdS0_S0_
+ __ZN14CLDistanceCalc5resetEv
+ __ZN14CLDistanceCalc9calc_dNdEEddRdS0_
+ __ZN14CLDistanceCalcC1Ev
+ __ZN14CLDistanceCalcC2Ev
+ __ZN16CLRouteRoadArray21getPathWithLowestCostERNSt3__110shared_ptrI11CLRouteRoadEE
+ __ZN16CLRouteRoadArray3addERKNSt3__110shared_ptrI11CLRouteRoadEE
+ __ZN16CLRouteRoadArray4findERKNSt3__110shared_ptrI11CLRouteRoadEE
+ __ZN16CLRouteRoadArray6removeERKNSt3__110shared_ptrI11CLRouteRoadEE
+ __ZN18CLFamiliarRoadData19addToFamiliarityMapERKyS1_S1_d
+ __ZN18CLFamiliarRoadData21getFamiliarityDataForE12CLMapRoadKeyRKy
+ __ZN18CLFamiliarRoadData30getFamiliarRoadDataForThisRoadERK12CLMapRoadKeyRNSt3__16vectorINS3_10shared_ptrI17CLFamiliarityDataEENS3_9allocatorIS7_EEEE
+ __ZN18CLFamiliarRoadData36trimNeighborsBasedOnFamiliarityIndexENSt3__110shared_ptrI9CLMapRoadEERNS0_6vectorIS3_NS0_9allocatorIS3_EEEE
+ __ZN18CLFamiliarRoadData37trimRoadVectorBasedOnFamiliarityIndexERNSt3__13mapI12CLMapRoadKeyNS0_10shared_ptrI9CLMapRoadEENS0_4lessIS2_EENS0_9allocatorINS0_4pairIKS2_S5_EEEEEE
+ __ZN18CLFamiliarRoadData37trimRoadVectorBasedOnFamiliarityIndexERNSt3__16vectorINS0_10shared_ptrI9CLMapRoadEENS0_9allocatorIS4_EEEE
+ __ZN18CLFamiliarRoadData38isFamiliarRoadDataAvailableForThisRoadERK12CLMapRoadKey
+ __ZN18CLMapRoadAnalytics19m_ZeroLengthCounterE
+ __ZN18CLMapRoadAnalytics28m_HeadingComputationsCounterE
+ __ZN18CLMapRoadAnalytics29m_DistanceComputationsCounterE
+ __ZN9CLMapRoad11getAsStringEv
+ __ZN9CLMapRoad13isUTurnRoadOfERKNSt3__110shared_ptrIS_EE
+ __ZN9CLMapRoad17reverseRoadVectorEv
+ __ZN9CLMapRoad19curvedSectionsCountEv
+ __ZN9CLMapRoad20addSegmentCoordinateERK23GEOLocationCoordinate2Db
+ __ZN9CLMapRoad20addSegmentCoordinateEddb
+ __ZN9CLMapRoad20getHeadingForSegmentEi
+ __ZN9CLMapRoad20getLastSegmentCourseEv
+ __ZN9CLMapRoad21getFirstSegmentCourseEv
+ __ZN9CLMapRoad22computeSegmentHeadingsEv
+ __ZN9CLMapRoad23computeSegmentDistancesEv
+ __ZN9CLMapRoad25fillFromGEOMapFeatureRoadEP17GEOMapFeatureRoadb
+ __ZN9CLMapRoad26isParticleOnACurvedSegmentEddb
+ __ZN9CLMapRoad34fillFromMapHelperNSDictionaryArrayER14CLDistanceCalcP12NSDictionaryb
+ __ZNK11CLRouteRoad24endJunctionIsConnectedToERKNSt3__110shared_ptrIS_EE
+ __ZNK11CLRouteRoad26startJunctionIsConnectedToERKNSt3__110shared_ptrIS_EE
+ __ZNK11CLRouteRoad29getCourseOfRoadAtIntersectionEb
+ __ZNK9CLMapRoad11getAltitudeEd
+ __ZNK9CLMapRoad13isConnectedToERKNSt3__110shared_ptrIS_EE
+ __ZNK9CLMapRoad15isNonZeroLengthEv
+ __ZNK9CLMapRoad17isConnectedToStopERKNSt3__110shared_ptrIS_EE
+ __ZNK9CLMapRoad17stopIsConnectedToERKNSt3__110shared_ptrIS_EE
+ __ZNK9CLMapRoad18isConnectedToStartERKNSt3__110shared_ptrIS_EE
+ __ZNK9CLMapRoad18startIsConnectedToERKNSt3__110shared_ptrIS_EE
+ __ZNK9CLMapRoad20getCoordinateAtIndexEi
+ __ZNK9CLMapRoad21stopIsConnectedToStopERKNSt3__110shared_ptrIS_EE
+ __ZNK9CLMapRoad22startIsConnectedToStopERKNSt3__110shared_ptrIS_EE
+ __ZNK9CLMapRoad22stopIsConnectedToStartERKNSt3__110shared_ptrIS_EE
+ __ZNK9CLMapRoad23startIsConnectedToStartERKNSt3__110shared_ptrIS_EE
+ __ZNK9CLMapRoad26calculateBearingForSegmentEii
+ __ZNK9CLMapRoad27headingChangeIndicatesCurveEddd
+ __ZNKSt3__119__shared_weak_count13__get_deleterERKSt9type_info
+ __ZNKSt3__16locale9use_facetERNS0_2idE
+ __ZNKSt3__18ios_base6getlocEv
+ __ZNSt11logic_errorC2EPKc
+ __ZNSt12length_errorD1Ev
+ __ZNSt20bad_array_new_lengthC1Ev
+ __ZNSt20bad_array_new_lengthD1Ev
+ __ZNSt3__112__next_primeEm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKcm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6resizeEmc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEaSERKS5_
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE6sentryC1ERS3_
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE6sentryD1Ev
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEb
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEd
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEi
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEy
+ __ZNSt3__114basic_iostreamIcNS_11char_traitsIcEEED2Ev
+ __ZNSt3__119__shared_weak_count14__release_weakEv
+ __ZNSt3__119__shared_weak_countD2Ev
+ __ZNSt3__119piecewise_constructE
+ __ZNSt3__15ctypeIcE2idE
+ __ZNSt3__16localeC1Ev
+ __ZNSt3__16localeD1Ev
+ __ZNSt3__18ios_base33__set_badbit_and_consider_rethrowEv
+ __ZNSt3__18ios_base4initEPv
+ __ZNSt3__18ios_base5clearEj
+ __ZNSt3__19basic_iosIcNS_11char_traitsIcEEED2Ev
+ __ZNSt3__19to_stringEi
+ __ZSt9terminatev
+ __ZTINSt3__119__shared_weak_countE
+ __ZTISt12length_error
+ __ZTISt20bad_array_new_length
+ __ZTTNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE
+ __ZTVN10__cxxabiv117__class_type_infoE
+ __ZTVN10__cxxabiv120__si_class_type_infoE
+ __ZTVNSt3__115basic_streambufIcNS_11char_traitsIcEEEE
+ __ZTVNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEE
+ __ZTVNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE
+ __ZTVSt12length_error
+ __ZdlPv
+ __ZdlPvSt19__type_descriptor_t
+ __ZnwmSt19__type_descriptor_t
+ ___cxa_allocate_exception
+ ___cxa_begin_catch
+ ___cxa_end_catch
+ ___cxa_free_exception
+ ___cxa_throw
+ ___gxx_personality_v0
+ ___sincos_stret
+ _atan
+ _atan2
+ _cos
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _fmod
+ _memcpy
+ _memmove
+ _memset
+ _objc_release_x28
+ _objc_release_x9
+ _objc_retain
+ _objc_retain_x26
+ _objc_retain_x8
+ _sin
+ _strcmp
+ _strlen
+ _tan
- ___objc_personality_v0
CStrings:
+ "%.7lf"
+ "(unknown: %i)"
+ ","
+ ",bikeableSide,"
+ ",bridge,"
+ ",clRoadId,"
+ ",course"
+ ",course,"
+ ",fow,"
+ ",frc,"
+ ",laneCount,"
+ ",latitude"
+ ",latitude,"
+ ",longitude"
+ ",longitude,"
+ ",name,"
+ ",oneWay,"
+ ",railway,"
+ ",roadID,"
+ ",startAlt,"
+ ",startAtTileBorder,"
+ ",startJunction,"
+ ",stopAlt,"
+ ",stopAtTileBorder,"
+ ",stopJunction,"
+ ",travelDirection,"
+ ",tunnel,"
+ ",walkableSide,"
+ ",width,"
+ "@\"<GEOMapFeatureAccessRequest>\""
+ "@132@0:8{CLLocationCoordinate2D=dd}16Q32Q40d48{CLLocationCoordinate2D=dd}56Q72Q80d88d96B104B108B112d116@124"
+ "@24@0:8^v16"
+ "A_MAJOR_ROAD_LESS_IMPORTANT_THAN_A_MOTORWAY"
+ "B56@0:8{shared_ptr<CLMapRoad>=^{CLMapRoad}^{__shared_weak_count}}16B32B36B40B44^v48"
+ "B60@0:8d16d24d32B40B44B48@52"
+ "CLMM,CLTSP,Roads,queryForRoadsWithinDistance returned error"
+ "CLMM,CLTSP,Roads,queryForRoadsWithinDistance,semaphore timed out"
+ "CLTSP,CLMM,MaphelperService,cancelRoadDataRequest"
+ "CLTSP,CLMM,MaphelperService,cancelRoadDataRequest processed"
+ "CLTSP,CLMM,MaphelperService,cancelRoadDataRequest,query not in progress"
+ "CLTSP,CLMM,MaphelperService,function call does not support constructing route for pedestrian/cycling use case"
+ "CLTSP,CLMM,MaphelperService,getCLMapRoadDataFromTripSegmentRoad,failed to find clMapRoad"
+ "CLTSP,CLMM,MaphelperService,getGEOMapFeatureRoadDataAroundCoordinate failed"
+ "CLTSP,CLMM,MaphelperService,invalid null-island coordinates for road data query"
+ "ENTRANCE_EXIT_TO_FROM_A_CAR_PARK"
+ "FOW_CONNECTOR"
+ "FOW_CUL_DE_SAC"
+ "FOW_ETA_GALLERY"
+ "FOW_STAIRS"
+ "FOW_UNKNOWN"
+ "LOCAL_CONNECTING_ROAD"
+ "LOCAL_ROAD"
+ "LOCAL_ROAD_OF_HIGH_IMPORTANCE"
+ "LOCAL_ROAD_OF_MINOR_IMPORTANCE"
+ "MOTORWAY_FREEWAY_OR_OTHER_MAJOR_ROAD"
+ "OTHER_MAJOR_ROAD"
+ "OTHER_ROAD"
+ "PART_OF_AN_ETA_PARKING_GARAGE_BUILDING"
+ "PART_OF_AN_ETA_PARKING_PLACE"
+ "PART_OF_AN_ETA_UNSTRUCTURED_TRAFFIC_SQUARE"
+ "PART_OF_A_PEDESTRIAN_ZONE"
+ "PART_OF_A_ROUNDABOUT"
+ "PART_OF_A_SERVICE_ROAD"
+ "PART_OF_A_SINGLE_CARRIAGEWAY_DEFAULT"
+ "PART_OF_A_SLIP_ROAD"
+ "PART_OF_A_WALKWAY"
+ "PART_OF_MOTORWAY"
+ "PART_OF_MULTI_CARRIAGEWAY_WHICH_IS_NOT_A_MOTORWAY"
+ "ROAD_FOR_AUTHORITIES"
+ "SECONDARY_ROAD"
+ "SPECIAL_TRAFFIC_FIGURES"
+ "UNKNOWN_ROAD"
+ "basic_string"
+ "boolValue"
+ "cancel"
+ "cancelRoadDataRequest"
+ "componentsSeparatedByString:"
+ "constructRouteFromLocation:roadID:clRoadID:projection:toLocation:toRoadID:toCLRoadID:toProjection:maxRouteLength:allowNetwork:isPedestrianOrCycling:clearTiles:iOSTime:familiarityData:withReply:"
+ "convertCLMapRoadVectorToRoadDictionaryArray:"
+ "coord%i"
+ "doubleValue"
+ "fGeoMapFeatureRoadRequest"
+ "fRoadDataRequestInProgress"
+ "fetchGEORoadDataAtIntersectionOf:allowNetwork:isPedestrianOrCycling:clearTiles:ignoreUTurns:returnRoads:"
+ "getCLMapRoadForLocation:roadID:clRoadID:allowNetwork:isPedestrianOrCycling:clearTiles:"
+ "getGEOMapFeatureRoadDataAroundLatitude:longitude:inRadius:allowNetwork:isPedestrianOrCycling:clearTiles:returnRoads:"
+ "intValue"
+ "internalConstructVehicularRouteFromLocation:roadID:clRoadID:projection:toLocation:toRoadID:toCLRoadID:toProjection:maxRouteLength:allowNetwork:isPedestrianOrCycling:clearTiles:iOSTime:familiarityData:"
+ "internalRoadName"
+ "laneCount"
+ "longLongValue"
+ "removeAllObjects"
+ "speedLimitIsMPH"
+ "v140@0:8{CLLocationCoordinate2D=dd}16Q32Q40d48{CLLocationCoordinate2D=dd}56Q72Q80d88d96B104B108B112d116@\"NSArray\"124@?<v@?@\"NSArray\">132"
+ "v140@0:8{CLLocationCoordinate2D=dd}16Q32Q40d48{CLLocationCoordinate2D=dd}56Q72Q80d88d96B104B108B112d116@124@?132"
+ "valueForKey:"
+ "vector"
+ "{shared_ptr<CLMapRoad>=^{CLMapRoad}^{__shared_weak_count}}60@0:8{CLLocationCoordinate2D=dd}16Q32Q40B48B52B56"

```
