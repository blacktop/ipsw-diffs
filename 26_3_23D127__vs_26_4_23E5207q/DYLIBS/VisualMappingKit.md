## VisualMappingKit

> `/System/Library/PrivateFrameworks/VisualMappingKit.framework/VisualMappingKit`

```diff

-8.25.6.25.71
-  __TEXT.__text: 0x658384
-  __TEXT.__auth_stubs: 0x1da0
-  __TEXT.__const: 0x45b20
-  __TEXT.__cstring: 0x10eb9
-  __TEXT.__oslogstring: 0x605
-  __TEXT.__gcc_except_tab: 0x43250
-  __TEXT.__unwind_info: 0x12268
-  __TEXT.__eh_frame: 0xc88
+8.25.12.16.0
+  __TEXT.__text: 0x7ca380
+  __TEXT.__auth_stubs: 0x1ff0
+  __TEXT.__const: 0x4e270
+  __TEXT.__cstring: 0x202b4
+  __TEXT.__gcc_except_tab: 0x53b30
+  __TEXT.__oslogstring: 0x1270
+  __TEXT.__unwind_info: 0x15550
+  __TEXT.__eh_frame: 0xbb0
   __TEXT.__objc_methname: 0x23
   __TEXT.__objc_stubs: 0x60
-  __DATA_CONST.__got: 0x2a8
-  __DATA_CONST.__const: 0x1340
+  __DATA_CONST.__got: 0x320
+  __DATA_CONST.__const: 0x12e0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x18
-  __AUTH_CONST.__auth_got: 0xee0
-  __AUTH_CONST.__const: 0x1f208
-  __AUTH_CONST.__cfstring: 0x280
-  __AUTH.__data: 0x18
-  __DATA.__data: 0x1ca0
+  __AUTH_CONST.__auth_got: 0x1008
+  __AUTH_CONST.__const: 0x250c8
+  __AUTH_CONST.__cfstring: 0x2a0
+  __AUTH.__data: 0x28
+  __DATA.__data: 0x1ce0
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0xad8
-  __DATA.__common: 0x2e0
+  __DATA.__bss: 0xf90
+  __DATA.__common: 0x2b8
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BB80D045-C6D8-3720-81BF-D7C51E89D529
-  Functions: 12027
-  Symbols:   716
-  CStrings:  1787
+  UUID: 1E869011-8596-3DA5-A7E1-2260A891D399
+  Functions: 14263
+  Symbols:   934
+  CStrings:  2597
 
Symbols:
+ _CFAllocatorCreate
+ _CFBundleCopyBundleURL
+ _CFStringCreateWithCString
+ _CFURLGetString
+ _IOSurfaceCreate
+ _IOSurfaceGetBytesPerElement
+ _IOSurfaceGetBytesPerElementOfPlane
+ _IOSurfaceGetBytesPerRow
+ _IOSurfaceGetBytesPerRowOfPlane
+ _IOSurfaceGetElementHeight
+ _IOSurfaceGetElementHeightOfPlane
+ _IOSurfaceGetElementWidth
+ _IOSurfaceGetElementWidthOfPlane
+ _IOSurfaceGetHeight
+ _IOSurfaceGetHeightOfPlane
+ _IOSurfaceGetNumberOfComponentsOfPlane
+ _IOSurfaceGetPixelFormat
+ _IOSurfaceGetWidth
+ _IOSurfaceGetWidthOfPlane
+ _IOSurfaceLock
+ _IOSurfaceUnlock
+ _LFV2KeypointsGetScaleAt
+ _LFV2KeypointsGetScoreAt
+ _LFV2MatchDescriptors
+ _LFV2MatcherHandleCreate
+ _LFV2MatcherHandleRelease
+ _LFV2MatchesGetQueryIndexAt
+ _LFV2MatchesGetReferenceIndexAt
+ _LFV2MatchesGetSize
+ _LFV2RetrievalGetDistanceAt
+ _LFV2RetrievalGetSize
+ _LFV2RetrievalIndexAt
+ _LFV2RetrievalRelease
+ _LFV2RetrievalTopK
+ _VMKAnchorListIsUpdated
+ _VMKDatabaseConfigSetEnableScaleEstimation
+ _VMKDatabaseConfigSetFeatureFilterRadius
+ _VMKDatabaseConfigSetSetFeatureFilterRadius
+ _VMKDatabaseDeserializeDatabaseFrame2
+ _VMKDatabaseGetEstimateRelativePosesList
+ _VMKDatabaseSetCameraIntrinsics
+ _VMKExtrinsicQueryToPrimaryFrameCreate
+ _VMKExtrinsicQueryToPrimaryFrameRelease
+ _VMKExtrinsicQueryToPrimaryFrameRetain
+ _VMKExtrinsicQueryToPrimaryFrameSetRotation
+ _VMKExtrinsicQueryToPrimaryFrameSetTranslation
+ _VMKInitVisualLoggerWithRecorder
+ _VMKInitializeVisualLogger
+ _VMKMapBridgeBlinkerKeyframeCopyIdentifier
+ _VMKMapBridgeBlinkerKeyframeCreate
+ _VMKMapBridgeBlinkerKeyframeGetTransform
+ _VMKMapBridgeBlinkerKeyframeListAppend
+ _VMKMapBridgeBlinkerKeyframeListCopyKeyframeAt
+ _VMKMapBridgeBlinkerKeyframeListCreate
+ _VMKMapBridgeBlinkerKeyframeListGetSize
+ _VMKMapBridgeBlinkerKeyframeListRelease
+ _VMKMapBridgeBlinkerKeyframeListRetain
+ _VMKMapBridgeBlinkerKeyframeRelease
+ _VMKMapBridgeBlinkerKeyframeRetain
+ _VMKMapBridgeConstraintGetConstraintType
+ _VMKMapBridgeConstraintGetNeighborKeyframeIndex
+ _VMKMapBridgeConstraintGetSourceKeyframeIndex
+ _VMKMapBridgeConstraintGetUncertainty
+ _VMKMapBridgeConstraintRelease
+ _VMKMapBridgeConstraintRetain
+ _VMKMapBridgeConstraintSourceToNeighborTransform
+ _VMKMapBridgeKeyframeCameraToGlobalTransform
+ _VMKMapBridgeKeyframeCopyIdentifier
+ _VMKMapBridgeKeyframeFrameId
+ _VMKMapBridgeKeyframeRelease
+ _VMKMapBridgeKeyframeRetain
+ _VMKMapBridgeKeyframeSessionId
+ _VMKMapBridgeKeyframeTimestamp
+ _VMKMapBridgeMapCollectionAt
+ _VMKMapBridgeMapCollectionRelease
+ _VMKMapBridgeMapCollectionRetain
+ _VMKMapBridgeMapCollectionSize
+ _VMKMapBridgeOccupancyDataCopyBlinkerKeyframeList
+ _VMKMapBridgeOccupancyDataCopyRoomBoundaryList
+ _VMKMapBridgeOccupancyDataCopyWalkabilityMap
+ _VMKMapBridgeOccupancyDataCreate
+ _VMKMapBridgeOccupancyDataGetWorldToRoomBoundaryTransform
+ _VMKMapBridgeOccupancyDataRelease
+ _VMKMapBridgeOccupancyDataRetain
+ _VMKMapBridgeRoomBoundaryCopyInnerBoundaries
+ _VMKMapBridgeRoomBoundaryCopyOuterBoundary
+ _VMKMapBridgeRoomBoundaryCreate
+ _VMKMapBridgeRoomBoundaryEdgeTypeListAppend
+ _VMKMapBridgeRoomBoundaryEdgeTypeListCreate
+ _VMKMapBridgeRoomBoundaryEdgeTypeListGetEdgeTypeAt
+ _VMKMapBridgeRoomBoundaryEdgeTypeListGetSize
+ _VMKMapBridgeRoomBoundaryEdgeTypeListRelease
+ _VMKMapBridgeRoomBoundaryEdgeTypeListRetain
+ _VMKMapBridgeRoomBoundaryGetCeilingHeight
+ _VMKMapBridgeRoomBoundaryGetFloorHeight
+ _VMKMapBridgeRoomBoundaryListAppend
+ _VMKMapBridgeRoomBoundaryListCopyBoundaryAt
+ _VMKMapBridgeRoomBoundaryListCreate
+ _VMKMapBridgeRoomBoundaryListGetSize
+ _VMKMapBridgeRoomBoundaryListRelease
+ _VMKMapBridgeRoomBoundaryListRetain
+ _VMKMapBridgeRoomBoundaryPolygonCopyEdgeTypes
+ _VMKMapBridgeRoomBoundaryPolygonCopyPoints
+ _VMKMapBridgeRoomBoundaryPolygonCreate
+ _VMKMapBridgeRoomBoundaryPolygonListAppend
+ _VMKMapBridgeRoomBoundaryPolygonListCopyPolygonAt
+ _VMKMapBridgeRoomBoundaryPolygonListCreate
+ _VMKMapBridgeRoomBoundaryPolygonListGetSize
+ _VMKMapBridgeRoomBoundaryPolygonListRelease
+ _VMKMapBridgeRoomBoundaryPolygonListRetain
+ _VMKMapBridgeRoomBoundaryPolygonPointCreate
+ _VMKMapBridgeRoomBoundaryPolygonPointGetX
+ _VMKMapBridgeRoomBoundaryPolygonPointGetY
+ _VMKMapBridgeRoomBoundaryPolygonPointListAppend
+ _VMKMapBridgeRoomBoundaryPolygonPointListCopyPointAt
+ _VMKMapBridgeRoomBoundaryPolygonPointListCreate
+ _VMKMapBridgeRoomBoundaryPolygonPointListGetSize
+ _VMKMapBridgeRoomBoundaryPolygonPointListRelease
+ _VMKMapBridgeRoomBoundaryPolygonPointListRetain
+ _VMKMapBridgeRoomBoundaryPolygonPointRelease
+ _VMKMapBridgeRoomBoundaryPolygonPointRetain
+ _VMKMapBridgeRoomBoundaryPolygonRelease
+ _VMKMapBridgeRoomBoundaryPolygonRetain
+ _VMKMapBridgeRoomBoundaryRelease
+ _VMKMapBridgeRoomBoundaryRetain
+ _VMKMapBridgeSubMapConstraintAt
+ _VMKMapBridgeSubMapConstraintsSize
+ _VMKMapBridgeSubMapKeyframeAt
+ _VMKMapBridgeSubMapKeyframesSize
+ _VMKMapBridgeSubMapRelease
+ _VMKMapBridgeSubMapRetain
+ _VMKMapBridgeWalkabilityMapCreate
+ _VMKMapBridgeWalkabilityMapGetData
+ _VMKMapBridgeWalkabilityMapGetHeight
+ _VMKMapBridgeWalkabilityMapGetTransform
+ _VMKMapBridgeWalkabilityMapGetWidth
+ _VMKMapBridgeWalkabilityMapRelease
+ _VMKMapBridgeWalkabilityMapRetain
+ _VMKMappingResultMapOptimizationOccurred
+ _VMKPoseEstimationResultCopyRelativePoseEstimateList
+ _VMKPoseEstimationResultGetQueryAttitude
+ _VMKPoseEstimationResultGetQueryGlobalPosition
+ _VMKPoseEstimationResultGetQueryInertialOdometryTimestamp
+ _VMKPoseEstimationResultQueryHasAttitude
+ _VMKPoseEstimationResultQueryHasGlobalPosition
+ _VMKPoseEstimationResultQueryHasInertialOdometryTimestamp
+ _VMKPoseEstimationResultSetExtrinsicQueryToPrimaryFrameData
+ _VMKPoseEstimationResultSetQueryAttitude
+ _VMKPoseEstimationResultSetQueryDeltaRotationToPrimaryTime
+ _VMKPoseEstimationResultSetQueryGlobalPosition
+ _VMKPoseEstimationResultSetQueryInertialOdometryTimestamp
+ _VMKRelativePoseEstimateCopyQueryIdentifier
+ _VMKRelativePoseEstimateCreate2
+ _VMKRelativePoseEstimateGetNumberOfInliers
+ _VMKRelativePoseEstimateGetNumberOfMatches
+ _VMKRelativePoseEstimateGetUncertainty
+ _VMKRelativePoseEstimateGetUpdateType
+ _VMKRelativePoseEstimateListAppend
+ _VMKRelativePoseEstimateListCopyRelativePoseEstimateAt
+ _VMKRelativePoseEstimateListCreate
+ _VMKRelativePoseEstimateListRelease
+ _VMKRelativePoseEstimateListRetain
+ _VMKRelativePoseEstimateListSize
+ _VMKRelativePoseEstimateSetNumberOfInliers
+ _VMKRelativePoseEstimateSetNumberOfMatches
+ _VMKSessionAddAnchorAtTimestamp
+ _VMKSessionAddOccupancyData
+ _VMKSessionConfigSetMaximumMapSize
+ _VMKSessionCopyMapCollection
+ _VMKSessionCopyOccupancyData
+ _VMKSessionGetOccupancyDataCount
+ _VMKSessionGetOccupancyDataTransform
+ _VMKSessionHasOccupancyDataTransform
+ _VMKSessionProcessOdometryWithId
+ _VMKSessionProcessRelativePoseEstimateList
+ _VMKSessionRemoveKeyframesOlderThanTimestamp
+ _VMKSessionReset
+ _VMKSessionSetCameraToImuExtrinsics
+ _VMKVisuaLoggerAddDestination
+ _VMKVisualLogFrameWithIdentifierAndCameraId
+ _VMKVisualLoggerExportCFDataToSequencePath
+ _VMKVisualLoggerExportNewRecordsToCFData
+ _VMKVisualLoggerExportNewRecordsToSequencePath
+ _VMKVisualLoggerReset
+ __ZNSt3__113basic_istreamIcNS_11char_traitsIcEEED0Ev
+ __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEE4syncEv
+ __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEE5imbueERKNS_6localeE
+ __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEE5uflowEv
+ __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEE6setbufEPcl
+ __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEE6xsgetnEPcl
+ __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEE6xsputnEPKcl
+ __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEE7seekoffExNS_8ios_base7seekdirEj
+ __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEE7seekposENS_4fposI11__mbstate_tEEj
+ __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEE8overflowEi
+ __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEE9pbackfailEi
+ __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEE9showmanycEv
+ __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEE9underflowEv
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ __ZNSt3__14stoiERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi
+ __ZTINSt3__113basic_istreamIcNS_11char_traitsIcEEEE
+ __ZTINSt3__115basic_streambufIcNS_11char_traitsIcEEEE
+ __ZTv0_n24_NSt3__113basic_istreamIcNS_11char_traitsIcEEED0Ev
+ __ZTv0_n24_NSt3__113basic_istreamIcNS_11char_traitsIcEEED1Ev
+ ___stdoutp
+ _fflush
+ _kCFNull
+ _kIOSurfaceBytesPerElement
+ _kIOSurfaceBytesPerRow
+ _kIOSurfaceHeight
+ _kIOSurfacePixelFormat
+ _kIOSurfacePlaneBytesPerElement
+ _kIOSurfacePlaneBytesPerRow
+ _kIOSurfacePlaneHeight
+ _kIOSurfacePlaneInfo
+ _kIOSurfacePlaneWidth
+ _kIOSurfaceWidth
+ _matrix_identity_float4x4
+ _objc_retainAutoreleasedReturnValue
+ _puts
+ _strerror
- _CFDataGetBytes
- _objc_claimAutoreleasedReturnValue
CStrings:
+ "\nCoordinates pair (Active, Candidate) ("
+ "\nT_world_to_room_boundary("
+ "\nkeyframes("
+ "\nroom_boundary_list("
+ "\ntotal_count("
+ "\nwalkability_map.T_room_boundary_to_walkability_map("
+ " \t\n\v\f\r"
+ "         "
+ "  #"
+ " (e.g. '10MB') but is '"
+ " - \n"
+ " < %g]\n"
+ " < %g]["
+ " < %g][%g]\n"
+ " < threshold: "
+ " > threshold: "
+ " Anchor timestamp: "
+ " Coordinates ("
+ " Got - count per type: (homeslam, active, candidate)=("
+ " HomeSlam distance: "
+ " Insufficient *in vicinity* colocation coordinates - required="
+ " Insufficient input colocation coordinates - count per type: (homeslam, active, candidate)=("
+ " Keyframe Timestamp: "
+ " Shape "
+ " ValueStride "
+ " Vuelta candidate map distance: "
+ " anchors into the current map "
+ " anchors."
+ " and "
+ " and query_vec is "
+ " and time "
+ " as array of type with size "
+ " as keyframe @ "
+ " at "
+ " at position "
+ " bytes"
+ " candidates."
+ " connected to server at "
+ " current active and external maps and converted them to samples."
+ " diff: "
+ " distance to keyframe: "
+ " does not match descriptor size "
+ " expected alignment "
+ " expected stride "
+ " failed on "
+ " for format with properties:\n"
+ " format."
+ " in "
+ " in map "
+ " in relative pose constraint with query "
+ " into a SharedIOSurfaceImage. The format is not (yet) supported by Kit_IOSurfaceImage."
+ " is already loaded"
+ " is invalid, must be non-zero"
+ " is not present in anchor database"
+ " is not present in any database"
+ " keyframes and "
+ " map database(s) as external maps"
+ " merging maps now"
+ " occupancy maps"
+ " option"
+ " or dimension: "
+ " outlier edges."
+ " pixels), "
+ " retrieved images."
+ " size "
+ " succeeded with pose:"
+ " to keyframe "
+ " to position "
+ " to reference image "
+ " which now contains "
+ " with "
+ " with LimitedRecorder"
+ " | "
+ "!CheckVariableExists(state_id)"
+ "!clusters[0].member_ids.empty() && !clusters[1].member_ids.empty()"
+ "!descs.empty()"
+ "!ext_map->IsEmpty()"
+ "!member_ids.empty()"
+ "!node_ids.empty()"
+ "!poses.empty()"
+ "!session_ids.empty()"
+ "!state_pointers_.contains(state_id)"
+ "!subgraphs_.at(subgraph_id).graph.nodes().contains(node_id)"
+ "!subgraphs_.contains(representative_id)"
+ "%g"
+ "%s: Config string contains more than one recorder; first recorder: '%s'; following recorder '%s' ignored"
+ "%s: Starting logging to local server '%s'"
+ "%s: Starting logging to recorder with: maximum_message_age=%s, maximum_record_count=%s"
+ "%s: Starting logging to recorder without maximum data age/count limits"
+ "%s: Stopping logging to recorder"
+ "', must be '{int size}[kb|mb|gb]'"
+ "(\\d*) ?(kb|mb|gb)?"
+ ")\n"
+ ") and the input blob ("
+ ", as its already present in anchor database"
+ ", buffer end: "
+ ", buffer start: "
+ ", count: "
+ ", error: "
+ ", forgotten: "
+ ", format="
+ ", height="
+ ", imu_id: "
+ ", inlier mask size: "
+ ", local descriptors size: "
+ ", min required: "
+ ", query correspondence indices size: "
+ ", query depth size: "
+ ", query descriptors size: "
+ ", query keypoints size: "
+ ", ref descriptors size: "
+ ", ref keypoints size: "
+ ", size: "
+ ", timestamp "
+ ", xc="
+ ", yaw: "
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:122: libc++ Hardening assertion __i != __last failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:127: libc++ Hardening assertion __j != __first failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:158: libc++ Hardening assertion __i != __last failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:164: libc++ Hardening assertion __j != __first failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__bit_reference:111: libc++ Hardening assertion __ctz + __clz < sizeof(_StorageType) * 8 failed: __fill_masked_range called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__format/formatter_output.h:237: libc++ Hardening assertion __first <= __last failed: Not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__format/formatter_output.h:250: libc++ Hardening assertion __first <= __last failed: Not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__format/formatter_output.h:264: libc++ Hardening assertion __first <= __last failed: Not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__format/parser_std_format_spec.h:594: libc++ Hardening assertion __begin != __end failed: when called with an empty input the function will cause undefined behavior by evaluating data not in the input\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:425: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:437: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:286: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:301: libc++ Hardening assertion !empty() failed: vector<bool>::back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:333: libc++ Hardening assertion !empty() failed: vector<bool>::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:271: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:275: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1522: libc++ Hardening assertion __i < size() failed: deque::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1553: libc++ Hardening assertion !empty() failed: deque::front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2296: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2310: libc++ Hardening assertion !empty() failed: deque::pop_back called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2464: libc++ Hardening assertion __f <= __l failed: deque::erase(first, last) called with an invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:796: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:801: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:806: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:811: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:816: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:457: libc++ Hardening assertion __last - __first >= 0 failed: invalid range in span's constructor (iterator, sentinel)\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:493: libc++ Hardening assertion __count <= size() failed: span<T>::first(count): count out of range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:498: libc++ Hardening assertion __count <= size() failed: span<T>::last(count): count out of range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:512: libc++ Hardening assertion __offset <= size() failed: span<T>::subspan(offset, count): offset out of range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:525: libc++ Hardening assertion __idx < size() failed: span<T>::operator[](index): index out of range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/streambuf:279: libc++ Hardening assertion std::__is_valid_range(__gbeg, __gnext) failed: [gbeg, gnext) must be a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/streambuf:280: libc++ Hardening assertion std::__is_valid_range(__gbeg, __gend) failed: [gbeg, gend) must be a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/streambuf:281: libc++ Hardening assertion std::__is_valid_range(__gnext, __gend) failed: [gnext, gend) must be a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/streambuf:297: libc++ Hardening assertion std::__is_valid_range(__pbeg, __pend) failed: [pbeg, pend) must be a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1332: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1476: libc++ Hardening assertion !empty() failed: string::back(): string is empty\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3362: libc++ Hardening assertion __first <= __last failed: string::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:329: libc++ Hardening assertion __len <= static_cast<size_type>(numeric_limits<difference_type>::max()) failed: string_view::string_view(_CharT *, size_t): length does not fit in difference_type\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDsUqVBVDy290EPSMceiFom_zpsUr5YM_8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Essentials/Apple/src/BundleInfo.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Essentials/Apple/src/Clock.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Essentials/Array/include/Essentials/Array/ArrayView.h"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Essentials/Array/src/ArrayBuffer.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Essentials/Dispatch/src/DispatchQueue.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Essentials/Dispatch/src/DispatchQueueTypeUtil.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Essentials/Dispatch/src/GrandCentralDispatchUtil.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Essentials/IO/include/Essentials/IO/Archive.h"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Essentials/Log/src/APILogging.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/Concurrency/include/Kit/Concurrency/Channel/Node.h"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/Concurrency/include/Kit/Concurrency/Channel/detail/ChannelInputModel.h"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/Concurrency/include/Kit/Concurrency/Channel/detail/Processor.h"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/Concurrency/include/Kit/Concurrency/Channel/detail/ProcessorInputMessageHandlingStrategy.h"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/Concurrency/src/Channel/NodeTaskScheduler.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/Concurrency/src/Channel/NodeTaskSchedulerPool.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/Container/src/Lines.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/Container/src/Points.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/CoreGraphics/src/ColorSpaceRef.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/CoreGraphics/src/DataProviderRef.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/CoreGraphics/src/ImageRef.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/CoreVideo/include/Kit/CoreVideo/PixelBufferRef.h"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/CoreVideo/src/CVImage.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/CoreVideo/src/CVImage.cpp:56"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/CoreVideo/src/PixelBufferRef.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/Foundation/FoundationIO/include/Kit/FoundationIO/DictionaryRefIO.h"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/Foundation/include/Kit/Foundation/Ptr.h"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/Foundation/src/BundleRef.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/Foundation/src/DictionaryRef.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/Foundation/src/Ptr.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/Foundation/src/Ref.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/Foundation/src/URLRef.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/Foundation/src/UUIDRef.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/IOSurface/include/Kit/IOSurface/View.h"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/IOSurface/src/IOSurfaceRef.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/IOSurfaceImage/src/IOSurfaceImage.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/IOSurfaceImage/src/IOSurfaceImage.cpp:47"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/Image/include/Kit/Image/FormatAlgorithm.h"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/Image/include/Kit/Image/ImageBuffer.h"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/Image/include/Kit/Image/ImageView.h:1290"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/Image/include/Kit/Image/ImageView.h:1300"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/Image/include/Kit/Image/SharedImage.h:1237"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/Image/src/Algorithm.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/Image/src/ImageStorage.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/Image/src/Size.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/ImageIO/include/Kit/ImageIO/ImageIO.h"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/ImageIO/src/Apple.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/ImageIO/src/ImageDestinationRef.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/ImageIO/src/ImageIO.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/ImageIO/src/Pnm.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/ImageIO/src/Serialization.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/Memory/include/Kit/Memory/VMAllocator.hpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/Mesh/include/Kit/Mesh/TriMeshAllocator.h"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/Mesh/src/TriMesh.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/Mesh/src/TriMeshAllocator.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/Mesh/src/TriMeshIO.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/Visualization/include/Kit/Visualization/DataIO.h"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/Visualization/include/Kit/Visualization/IData.h"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/Visualization/src/Client.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/Visualization/src/DataIO.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/Visualization/src/DataType.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/Visualization/src/FileIOPrivate.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/Visualization/src/IData.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/Visualization/src/NamedContext.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/Visualization/src/NetworkData.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Kit/Visualization/src/VisualLogger.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/VIO/Calibration/include/VIO/Calibration/CalibrationUtil.h"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/VIO/ComputerVisionTypes/include/VIO/ComputerVisionTypes/CameraStreamId.h"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/VIO/FactorBA/include/VIO/FactorBA/VIOEpipolarFactor.hpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/VIO/FactorBA/include/VIO/FactorBA/viovariables.hpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/VIO/FactorBA/src/VIOPoseFactorUtil.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/VIO/Geometry/include/VIO/Geometry/BicubicHermiteSpline.hpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/VIO/Geometry/include/VIO/Geometry/CubicSplineKnots.hpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/VIO/Geometry/include/VIO/Geometry/LensModel.h"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/VIO/Geometry/include/VIO/Geometry/LensModel.hpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/VIO/Geometry/include/VIO/Geometry/RANSAC/DataPointCorrespondenceUtil.h"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/VIO/Geometry/src/FreeformLensDistortion.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/VIO/Geometry/src/LensModel.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/VIO/Geometry/src/RANSAC/FivePointAdaptiveRansac.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/VIO/Geometry/src/TwoViewEstimators.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/VIO/MapOptimization/include/VIO/MapOptimization/PoseGraphSample.hpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/VIO/MapOptimization/src/PoseGraphNodeGroup.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/VIO/Util/include/VIO/Util/Variant.h"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/Common/src/LocalDescriptors.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/FeatureExtraction/src/FeatureMatching.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/FeatureMatching/src/FeatureMatching.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/Mapping/include_private/Vuelta/Mapping/PoseGraphUtil.hpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/Mapping/src/ParticleFilter.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/Mapping/src/Private/CalibrationData.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/Mapping/src/Private/HierarchicalPoseGraph.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/Mapping/src/Private/IO/BiMapSample.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/Mapping/src/Private/IO/CalibrationDataSample.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/Mapping/src/Private/IPoseGraph.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/Mapping/src/Private/MapDatabase.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/Mapping/src/Private/MapDatabaseUtil.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/Mapping/src/Private/MappingManager.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/Mapping/src/Private/ParticleFilterUtil.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/Mapping/src/Private/PoseGraph.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/Mapping/src/Private/PoseGraphUtil.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/Mapping/src/Private/VisualLoggerUtil.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/MappingInterface/src/IMappingManager.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/MappingUtils/src/EstimationUtil.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/PoseEstimation/include_private/Vuelta/PoseEstimation/DatabaseFrameSample.h"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/PoseEstimation/src/DatabaseFrameSample.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/PoseEstimation/src/ImageDatabase.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/PoseEstimation/src/PoseEstimation.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/VisualMappingKit/VisualMappingKit/include_private/VisualMappingKit/Private/VMKConversion.h"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/VisualMappingKit/VisualMappingKit/src/VMKDataTypes.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/VisualMappingKit/VisualMappingKit/src/VMKDatabase.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/VisualMappingKit/VisualMappingKit/src/VMKDatabaseConfig.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/VisualMappingKit/VisualMappingKit/src/VMKLogging.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/VisualMappingKit/VisualMappingKit/src/VMKSession.cpp"
+ "/Library/Caches/com.apple.xbs/49F57769-4E71-413D-9C12-6C1F46728978/TemporaryDirectory.40u4ZP/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/VisualMappingKit/VisualMappingKit/src/VMKSessionConfig.cpp"
+ "0 "
+ ": received data of timestamp "
+ ": {"
+ "; caused by:\n"
+ "; merging maps now"
+ ">{"
+ "ACTIVITY_LOG_STDERR"
+ "AVERAGE END ERROR(s): "
+ "AVERAGE START ERROR(s): "
+ "Added "
+ "Added HomeSlam colocation coordinates "
+ "Added constraint between: "
+ "Added occupancy data to visual mapping manager: "
+ "Adding ADL anchor "
+ "Adding VMK anchor %s to keyframe %s at %.2fm: %s"
+ "Adding camera constraint between "
+ "Adding occupancy data failed"
+ "Adding pose constraint between "
+ "Adding pose constraint with replacement between "
+ "Allocated object exceeds max pool size."
+ "Already checked that edge doesn't exist"
+ "An error occured while loading the image"
+ "Anchor "
+ "Asynchronous callback not set"
+ "Attempting loop closure on "
+ "Attempting to map iosurface of format "
+ "Binary descriptor vector must not be empty"
+ "Binary not found for callable"
+ "Buffer empty or timestamp not captured in odometry"
+ "Bundle does not have a bundle identifier"
+ "CFData is invalid"
+ "CFLOG_FORCE_STDERR"
+ "CONVERGENCE: "
+ "Calibration data already exists for camera"
+ "Camera ID cannot exceed 16 bits."
+ "Camera to Imu Extrinsics already exists for camera_id: "
+ "CameraToCamera5DoFEpipolarCovariance is not supported in this configuration; JtJ from Essential matrix was not supplied."
+ "Cannot add constraint of kind 'EpipolarWithScale'"
+ "Cannot add constraint of kind 'Other'"
+ "Cannot added the marginalized constraint into the graph because there exist one edge already. This should be changed to merge constraint"
+ "Cannot delete active database"
+ "Cannot get metric pose for constraint of kind 'Other'"
+ "Cannot interpolate pose at non-primary frame t=%lf"
+ "Cannot receive. Connection not initialized"
+ "Cannot reinterpret memory region of byte size "
+ "Cannot select representative from empty member list"
+ "Cannot send. Connection not initialized"
+ "Cannot split subgraph with less than 2 nodes"
+ "Client "
+ "Client cannot receive. Server connection not established."
+ "Client cannot send packet. Server connection not established."
+ "Client failed to send packet to "
+ "Closest state for anchor ahead of buffer window. This should not happen."
+ "Closest state for anchor outside of buffer window. Keyframe Timestamp: "
+ "ClusterIsolatedSubgraph() only applicable for KMeans strategy"
+ "Connection already initialized"
+ "Contains(pf::formats::F16(), ref.Format())"
+ "Contains(pf::formats::F32(), ref.Format())"
+ "Contains(pf::formats::U16(), ref.Format())"
+ "Contains(pf::formats::U8(), ref.Format())"
+ "Convergence in the cost."
+ "Convergence in the cost: %g\n"
+ "Convergence in the cost: N.A."
+ "Convergence in the gradient."
+ "Convergence in the parameters."
+ "Coordinates ("
+ "Coordinates chosen for agreement score computation "
+ "Coordinates pair in HS "
+ "Could not accept new client %d: %s (%d)"
+ "Could not access bundle location from function pointer. Detail: "
+ "Couldn't find the closest state for given timestamp"
+ "Couldn't retrieve neighbor state from edge"
+ "Couldn't retrieve source state from edge"
+ "Database"
+ "Database Frame Deleted. New Database size: "
+ "Delta rotation to primary time or extrinsic to primary is not provided"
+ "Descriptor dimensions must be 64"
+ "Descriptor types must match, but ref_vec is "
+ "Deserialization failed"
+ "Detected odometry outlier edge with edge error = "
+ "Detected reloc outlier edge with edge error = "
+ "Dimension mismatch"
+ "Dropping %zu epipolar constraints (marginalization not yet supported)."
+ "END ERROR(s): "
+ "Edge must have T and JtJ"
+ "Edge must have transform"
+ "Edge should be new (not already in merged subgraph)"
+ "Edge should exist in full graph"
+ "Empty data"
+ "Error closing socket %d: %s (%d)"
+ "Error connecting to %s:%d"
+ "Error connecting to %s:%d %s (%d)"
+ "Error connecting to socket %d: %s (%d)"
+ "Error creating socket: %s (%d)"
+ "Error getting host address %d: %s (%d)"
+ "Error sending data to %d: %s (%d)"
+ "Error setsockopt: %s (%d)"
+ "Error setting socket blocking: %s (%d)"
+ "Error setting socket non-blocking: %s (%d)"
+ "Error starting client socket for "
+ "Error stopping socket %d: %s (%d)"
+ "Error while reading from %s. %s"
+ "Expect current map to empty in offline mode"
+ "Expect relative pose estimates from Blinker in offline mode"
+ "Expected 2 clusters from binary split"
+ "Expecting GetAnchors(true) to return only tracked anchors"
+ "Expecting a keyframe is selected to be pruned"
+ "External map database should not be empty"
+ "FACTOR(s): "
+ "FACTORIZATION: "
+ "Failed to add frame during deserialization: "
+ "Failed to add neighbor variable"
+ "Failed to add relocalization edge"
+ "Failed to add the edge in the pose-graph during deserialization. This should not happen since current design the graph should contain only one edge between each pair per type."
+ "Failed to add the edge in the pose-graph during deserialization. This should not happen since current design the graph should contain only one edges between each pair per type."
+ "Failed to configure logging destinations: "
+ "Failed to create "
+ "Failed to create file exporter"
+ "Failed to export data list to blob"
+ "Failed to export data of type "
+ "Failed to get descriptors"
+ "Failed to import messages from blob"
+ "Failed to initialize from strings: "
+ "Failed to initialize recorder"
+ "Failed to load bundle from "
+ "Failed to obtain executable path"
+ "Failed to process pose estimation for camera %u at time %lf"
+ "Failed to record data of type "
+ "Failed to start new server socket %d (expected if connection was terminated)"
+ "Failure during recording of data of type "
+ "Features after/before filtering: "
+ "FisheyeLens"
+ "FisheyeLensFast1"
+ "FisheyeLensFast2"
+ "FisheyeLensHermesKR4"
+ "FisheyeLensKDR7"
+ "FisheyeLensKDRC7"
+ "FisheyeLensKR7"
+ "FlyoverPerspectiveLens"
+ "Frame already exists in database"
+ "Frame not found in database"
+ "Grabbed "
+ "Graph should not have duplicate edges"
+ "HomeSlam colocation coordinates confirm relocalization (score: "
+ "HomeSlam colocation coordinates reject relocalization (score: "
+ "IDE_DISABLED_OS_ACTIVITY_DT_MODE"
+ "IOSurface"
+ "IOSurface<"
+ "ITERATIONS: [Successful | Total]["
+ "Image Retrieval Candidates with "
+ "Image Retrieval Database Pixel Buffer with "
+ "Image Retrieval Database with "
+ "Image Retrieval Invalid Database mask with "
+ "Image Retrieval Top "
+ "Imu to Camera extrinsics already exists for camera_id: "
+ "Incorporating the external map "
+ "Index out of bounds"
+ "Initializing particle filter with "
+ "Internal inconsistency, Keyframe is not included in uuid_imageid_bimap_"
+ "Invalid LinearSystem."
+ "Invalid interpolation_factor."
+ "Invalid or empty data"
+ "Invalid sample type"
+ "Invalid stride for CVPixelBuffer storage. Strides are chosen to be efficient by CVPixelBuffer creation and no non-default strides are allowed at the moment.To create a valid buffer, do not specify any explicit strides in image creation.\n"
+ "IsConstraintInImuFrame(pg_constraint)"
+ "Isolated subgraph should not contain fixed frame"
+ "JtJ_I0_to_I1.trace() > 0."
+ "JtJ_I0_to_Iquery"
+ "K >= 2 && K <= node_ids.size()"
+ "K must be between 2 and number of nodes"
+ "K must be between 2 and number of nodes for initial centroid selection"
+ "Keyframe "
+ "Keyframe not found in traversal distances"
+ "LFV2DescriptorsRef is null"
+ "Last added keyframe no longer exists in map"
+ "Latest odometry in Global: "
+ "Latest odometry: "
+ "Latest state in Global: "
+ "Latest state in odometry: "
+ "Lens model already exists for camera_id: "
+ "Lens model pointer must be non-null"
+ "Lens model undistortion failed this should not happen"
+ "Lens type not supported: "
+ "LinearLens"
+ "Loop closure succeeded"
+ "METHOD: "
+ "MINIMIZER SUMMARY:"
+ "Map size "
+ "Maximum iterations exceeded."
+ "Multiple camera_id found for imu_id: "
+ "Multiple imu_id found for camera_id: "
+ "N.A. "
+ "Near keyframe not found"
+ "Need at least one node to find centroid"
+ "Neighbor keyframe not found in keyframe_index_mapping"
+ "Neighbor subgraph must exist"
+ "New representative must be in the subgraph"
+ "New representative should not already exist in subgraphs_"
+ "No calibration data in database"
+ "No keyframe in database"
+ "No prunable keyframe found, but keyframes exceed map size"
+ "No valid coordinates pairs found for HomeSlam colocation check - returning 0 to avoid rejection"
+ "Node already in subgraph"
+ "Node must exist in full graph"
+ "Node must exist in full_state_map"
+ "Node must exist in graph"
+ "Non-primary frame t=%lf is not synced with primary frame t=%lf"
+ "NoncentricLens"
+ "NoncentricLensKDR7"
+ "NoncentricLensKDRC7"
+ "NoncentricLensKR7"
+ "Not enough inliers after matching"
+ "Not enough matches after matching"
+ "Not implemented yet"
+ "OS_ACTIVITY_DT_MODE"
+ "Other descriptor store must be SurfaceLocalDescriptors"
+ "Other descriptor store must be VariantLocalDescriptors"
+ "PF state estimate: "
+ "PerspectiveLens"
+ "Pose estimation for query frame @ "
+ "Processed %lu camera pose estimations"
+ "Properties are missing required arguments for surface creation. Required: width, height, format. Given: width="
+ "Pruning id "
+ "Ray mapper type is out of range: "
+ "RearCameraOffsetFromDisplayCenter"
+ "Receiving odometry input from non-primary IMU, switching the primary IMU and reset mapping session"
+ "Recorder not initialized"
+ "Recorder\\{((?:\\.\\s*[a-zA-Z_][a-zA-Z0-9_]*\\s*=\\s*[a-zA-Z0-9_.]+\\s*,?\\s*)*)\\}"
+ "Recorder\\{(.*)\\}"
+ "Recorder{"
+ "Reduced outlier edge information between "
+ "Removed Outlier edge between "
+ "Removing "
+ "Representative must exist in state_pointers_"
+ "Representative variable missing"
+ "Reset all HomeSlam colocation coordinates"
+ "Resetting particle filter after visual loop closure"
+ "Rotation or translation from extrinsic to primary is not provided"
+ "Running map optimization after relocalizing external maps."
+ "SIZE OF VARIABLES(s): "
+ "START ERROR(s): "
+ "Selected a new fixed state "
+ "SharedLocalDescriptors is null"
+ "ShouldRejectRelocalizationBasedOnHomeSlamColocationCoordinatesAgreement - skipping"
+ "Size mismatch between the input archive ("
+ "Skip adding existing constraint between: "
+ "Skipping adding empty database with session ID "
+ "Skipping map database to add since session ID "
+ "Skipping relocation due to HomeSlam colocation coordinates check failure"
+ "Source keyframe not found in keyframe_index_mapping"
+ "Split produced empty cluster"
+ "State ID not found in map"
+ "State in coarse_state_map must be a representative in coarse_graph"
+ "State must be in a subgraph"
+ "State must exist for neighbor in graph"
+ "State must exist for node"
+ "State must exist for node in graph"
+ "Subgraph already exists"
+ "Subgraph must exist"
+ "Successfully incorporated the external map "
+ "Successfully relocalized query frame "
+ "Surface descriptor width must be 64"
+ "Surface format must be OneComponent_8"
+ "Surface format must be OneComponent_8 for binary descriptors"
+ "Surface height "
+ "Surface height must match number of descriptors"
+ "Surface is not valid"
+ "Surface must be OneComponent_8 format"
+ "Surface width does not match descriptor dimension"
+ "Surface width must match binary descriptor dimension (64)"
+ "T_C_to_I_R"
+ "T_C_to_I_t"
+ "T_world_to_occupancy_.size() == occupancy_data_.size()"
+ "The `color_map` may not be empty."
+ "There is always a previous KF in the map (except at the start)."
+ "Timeout connecting to %s:%d"
+ "Timeout while waiting for connection established"
+ "Timstamp not captured in odometry buffer: "
+ "Tracking %zu anchors in current map and there are %zu anchors among %zu external maps"
+ "Transform and occupancy data vectors must have the same size"
+ "Transform not available at index"
+ "Translation candidate to active "
+ "Trying to reduce information on edge with no information specified"
+ "Trying to reduce information on edge with no transform specified"
+ "UUID not found for image during timestamp pruning"
+ "Unable to add Anchor "
+ "Unable to allocate memory for map collection"
+ "Unable to allocate memory for occupancy data"
+ "Unable to find factor in linear system in replacing pose to pose constraint."
+ "Unable to find variable in linear system in replacing pose to pose constraint."
+ "Unable to process pose estimate list"
+ "Undistortion using calibration data failed"
+ "Unexpected relative pose estimates in online mode"
+ "Unknown error"
+ "Unknown error code"
+ "Unknown field name: '"
+ "Unknown ids in pose estimate (query: %s, ref: %s)"
+ "Unknown reference keyframe "
+ "Unsupported RelativePoseUpdateType"
+ "Unsupported descriptor type: "
+ "Unsupported edges."
+ "Unsupported pixel format value "
+ "UpdateIntraMapConstraintInMap(*query_map, ref_image_id, query_image_id, pose_estimate)"
+ "Updated HomeSlam colocation coordinates "
+ "Updated relocalization type: %d to %d"
+ "Updating constraints only implemented for kind 'Pose'"
+ "Updating map constraints only implemented for external constraints."
+ "VARIABLES(s): "
+ "Virtual channel %d not handled"
+ "VueltaVisualLogger"
+ "VueltaVisualLogging"
+ "We should not provide an invalid lens!"
+ "[ "
+ "[error][grad < gtol][%g]["
+ "[iter][old->new][delta < ptol][grad < gtol][delta < ctol][%d][%g->%g][%g < %g]["
+ "[iter][old->new][delta < ptol][grad < gtol][delta < ctol][lambda][%d][%g->%g][%g < %g]["
+ "\\.\\s*([a-zA-Z_][a-zA-Z0-9_]*)\\s*=\\s*([a-zA-Z0-9_.]+)"
+ "\\d+(\\.?\\d+)?"
+ "] "
+ "] = "
+ "added"
+ "anchor"
+ "anchor != nullptr"
+ "anchor.is_tracked"
+ "anchors != nullptr"
+ "blinker_keyframes != nullptr"
+ "boundaries != nullptr"
+ "boundary != nullptr"
+ "boundary_list != nullptr"
+ "bounds.size() % 2 == 0"
+ "bounds.size() >= 2"
+ "bundle_url"
+ "bytes_per_element/row: "
+ "cam-"
+ "camera id: "
+ "camera_id"
+ "camera_id <= 0xffff"
+ "client"
+ "clusters.size() == 2"
+ "coarse_graph.nodes().contains(state_id)"
+ "coarse_graph.nodes().empty() || (fixed_state.has_value() && full_state_map.contains(*fixed_state))"
+ "com.apple.cv3d"
+ "config_.subgraph_clustering_strategy == SubgraphClusteringStrategy::KMeans"
+ "constraint != nullptr"
+ "constraint_Cref_to_Cquery.kind != RelativePoseConstraint::Kind::Epipolar"
+ "constraint_Cref_to_Cquery.kind == util::RelativePoseConstraint::Kind::Epipolar"
+ "constraint_Cref_to_Cquery.kind == util::RelativePoseConstraint::Kind::Pose"
+ "could not interpolate pose for anchor timestamp"
+ "could not interpolate pose for nearest keyframe timestamp"
+ "cv3d.kit.net"
+ "cv3d.vio.geometry"
+ "cv3d.vio.map_optimization"
+ "cv3d.vuelta"
+ "cv3d.vuelta-viz"
+ "cv3d.vuelta.map"
+ "cv3d.vuelta.pe"
+ "data != nullptr"
+ "database.image"
+ "database.keypoints"
+ "database_"
+ "database_->AddToBiMap(result.query_data.query_id, image_id)"
+ "database_->IsEmpty()"
+ "database_to_prune_from != database_"
+ "desc_count == feats.keypoints.size()"
+ "desc_type == kLFV2DescriptorDataTypeUint8 && desc_dim == 64u"
+ "descs != nullptr"
+ "distances_from_start must not be empty"
+ "edge.JtJ_source_to_neighbor.has_value()"
+ "edge.T_source_to_neighbor && edge.JtJ_source_to_neighbor"
+ "edge.T_source_to_neighbor.has_value()"
+ "edge1.T_source_to_neighbor.has_value() && edge1.JtJ_source_to_neighbor.has_value()"
+ "edge1.neighbor_node_id != edge2.neighbor_node_id"
+ "edge2.T_source_to_neighbor.has_value() && edge2.JtJ_source_to_neighbor.has_value()"
+ "edge_iter != edges.end()"
+ "edge_iter->JtJ_source_to_neighbor.has_value()"
+ "edge_iter->T_source_to_neighbor.has_value()"
+ "edge_opt->JtJ_source_to_neighbor.has_value()"
+ "edge_opt->T_source_to_neighbor.has_value()"
+ "edge_opt.has_value()"
+ "edge_ref.has_value()"
+ "edge_type_list != nullptr"
+ "edge_types != nullptr"
+ "element_size: "
+ "entries: "
+ "epipolar_constraint_Cref_to_Cquery.JtJ.norm2() > 1e-10"
+ "epipolar_constraint_Cref_to_Cquery.kind == Kind::Epipolar"
+ "epipolar_constraint_Cref_to_Cquery.kind == Kind::EpipolarWithScale"
+ "exp_descs.has_value()"
+ "exp_query_descs_copy.has_value()"
+ "exp_ref_descs_copy.has_value()"
+ "ext_database"
+ "ext_map.SessionId() != this->SessionId()"
+ "external map load correction (should be 0): "
+ "extrinsics_calibration"
+ "failed to unproject: xd="
+ "feats.op_depth->size() == feats.keypoints.size()"
+ "file exporter"
+ "file://"
+ "first_centroid_iter != distances_from_start.end()"
+ "float"
+ "format: "
+ "from.RuntimeFormat() == to.RuntimeFormat()"
+ "from.Size() == to.Size()"
+ "full_graph.nodes().contains(source_node_id)"
+ "full_graph_.nodes().contains(current_state_id)"
+ "full_graph_.nodes().contains(state_id)"
+ "full_state_map.contains(neighbor_node_id)"
+ "full_state_map.contains(node_id)"
+ "given "
+ "graph.nodes().contains(node_id)"
+ "height != 0"
+ "hostname:port %s:%d not valid"
+ "idx < typed_descs.size()"
+ "image keypoints size: "
+ "image-retrieval"
+ "imu id "
+ "imu_id"
+ "index < boundaries->boundaries.size()"
+ "index < edge_types->edge_types.size()"
+ "index < keyframes->keyframes.size()"
+ "index < map_collection->maps.size()"
+ "index < occupancy_data_.size()"
+ "index < points->points.size()"
+ "index < polygons->polygons.size()"
+ "index < pose_list->poses.size()"
+ "index < result->pose_list.poses.size()"
+ "index < submap->constraints.size()"
+ "index < submap->keyframes.size()"
+ "inner_boundaries != nullptr"
+ "input vecetor must include two bounds per scale."
+ "inserted"
+ "interpolation_factor > 0 && interpolation_factor < 1"
+ "invalid recorder argument string: '"
+ "invalid size limit string '"
+ "key not found in map"
+ "keyframe != nullptr"
+ "keyframe_id != nullptr"
+ "keyframes != nullptr"
+ "kf2.has_value()"
+ "kf_stats.op_selected_keyframe"
+ "limited recorder"
+ "loop_closure_correction: "
+ "ls_"
+ "ls_->removeFactor<vio::VIOEpipolarFactor4DoF<double>>(edge.factor_id)"
+ "m"
+ "map != nullptr"
+ "map_.contains(*fixed_keyframe_)"
+ "map_.empty()"
+ "map_.erase(image_id.view)"
+ "map_collection != nullptr"
+ "mapping.active-map"
+ "mapping.external-map"
+ "mapping.relocalization"
+ "match_ret == kLFReturnNoError"
+ "match_ret == kLFReturnNoError && matches"
+ "matches.has_value()"
+ "max_iterations >= 1"
+ "maximum_message_age"
+ "maximum_record_count"
+ "maximum_records_size"
+ "min_it != state_ids.end()"
+ "minimizer_ptr_"
+ "must be: 'Recorder{[arg_value[, ...]]}' or 'Recorder{.arg_name=arg_value, ...}', with following args:\n#0: maximum_message_age: positive float (or '0' to disable)\n#1: maximum_record_count: positive int (or '0' to disable)\n#2: maximum_records_size: size string '{size}[KB|MB|GB]', e.g. '10KB' (or '0' to disable)"
+ "near_kf_iter != map_.end()"
+ "neighbor_id not found"
+ "neighbor_id_iter != state_id_to_variable_id_map_.end()"
+ "neighbor_keyframe_iter != keyframe_index_mapping.end()"
+ "neighbor_state"
+ "neighbor_state_iter != states.end()"
+ "neighbor_var_iter != ls_->endVariable<vio::VIO4DoFDeltaPoseVariable<double>>()"
+ "neighbor_variable not found"
+ "nio-pose"
+ "node1_iter != nodes_.end()"
+ "node2_iter != nodes_.end()"
+ "node_iter != nodes.end()"
+ "node_to_subgraph_map.contains(*fixed_state)"
+ "node_to_subgraph_map_.at(*fixed_state_) != subgraph_id"
+ "node_to_subgraph_map_.contains(*fixed_state_)"
+ "node_to_subgraph_map_.contains(state_id)"
+ "num_components: "
+ "num_planes: "
+ "number of inliers: "
+ "number of matches: "
+ "number of scale inliers: "
+ "occupancy"
+ "odometry_accumulator_buffer_.size() > 1"
+ "odometry_iter != odometry_accumulator_buffer_.end()"
+ "op_T_C_to_I.has_value()"
+ "op_T_Cneighbor_to_Ineighbor.has_value()"
+ "op_T_Cquery_to_Iquery.has_value()"
+ "op_T_Cref_to_I.has_value() && op_T_Cquery_to_I.has_value()"
+ "op_T_Cref_to_Iref.has_value()"
+ "op_T_Cref_to_Iref.has_value() && op_T_Cquery_to_Iquery.has_value()"
+ "op_T_Csource_to_Isource.has_value()"
+ "op_T_I_to_C.has_value()"
+ "op_T_S_to_N.has_value()"
+ "op_T_U_to_N.has_value()"
+ "op_imu_id.has_value()"
+ "opt_epipolar_constraint_Cref_to_Cquery->kind == util::RelativePoseConstraint::Kind::Epipolar"
+ "opt_query_kf.has_value()"
+ "opt_query_map_and_image_id.has_value()"
+ "opt_ref_kf.has_value()"
+ "opt_ref_map_and_image_id.has_value()"
+ "opt_uuid.has_value()"
+ "outer_boundary != nullptr"
+ "p.second"
+ "particle-filter"
+ "pf_particles"
+ "plane #"
+ "point != nullptr"
+ "point_list != nullptr"
+ "points != nullptr"
+ "polygon != nullptr"
+ "polygon_list != nullptr"
+ "polygons != nullptr"
+ "pose"
+ "pose_estimate.type == RelativePoseUpdateType::Blinker"
+ "pose_graph_->FixState(SelectFixedKeyframe())"
+ "prev_primary_state_N_.timestamp >= odometry_iter->timestamp && prev_primary_state_N_.timestamp < odometry_next_iter->timestamp"
+ "prune_info"
+ "ptr_"
+ "query_keypoints_nsp.size() == num_points * 2"
+ "query_kf"
+ "query_map == database_"
+ "query_map == ref_map"
+ "query_timestamp > prev_primary_state_N_.timestamp"
+ "range::all_of(pose_estimates, [&](const RelativePoseEstimate& pose) { return pose.query_id == result.query_data.query_id && (pose.type == RelativePoseUpdateType::Database || pose.type == RelativePoseUpdateType::DatabaseWithScale); })"
+ "recorder string 'maximum_message_age' argument (#0) invalid: must be positive float but is '"
+ "recorder string 'maximum_record_count' argument (#1) invalid: must be positive int but is '"
+ "recorder string 'maximum_records_size' argument (#2) invalid: must be a size string of pattern "
+ "ref correspondence indices size: "
+ "ref depth size: "
+ "ref keypoints size: "
+ "ref.IsValid()"
+ "ref_kf"
+ "ref_map != database_"
+ "ref_ret"
+ "reloc-info"
+ "result != nullptr"
+ "result->query_data.op_inertial_odometry_timestamp.has_value()"
+ "result->query_data.op_query_attitude_xyzw.has_value()"
+ "result->query_data.op_query_position_in_global.has_value()"
+ "ret != vio::AddPoseGraphEdgeReturn::kSkipDueToDuplicatedEdge"
+ "ret == elog::APILogging::InternalAvailable()"
+ "ret1"
+ "room_boundaries != nullptr"
+ "scale bounds is empty"
+ "size: "
+ "source_id not found"
+ "source_id_iter != state_id_to_variable_id_map_.end()"
+ "source_keyframe_iter != keyframe_index_mapping.end()"
+ "source_state"
+ "source_var_iter != ls_->endVariable<vio::VIO4DoFDeltaPoseVariable<double>>()"
+ "source_variable not found"
+ "state_id_to_variable_id_map.contains(neighbor_node_id)"
+ "state_id_to_variable_id_map.contains(source_node_id)"
+ "state_id_to_variable_id_map.contains(subgraph.representative_id)"
+ "state_id_to_variable_id_map.contains(target_rep_id)"
+ "state_id_to_variable_id_map_[state_id0] == state_var_id0 && state_id_to_variable_id_map_[state_id1] == state_var_id1"
+ "state_iter != states.end()"
+ "state_pointers_.contains(*last_added_keyframe_current_session_)"
+ "state_pointers_.contains(representative_id)"
+ "states.contains(node_id)"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::iosimg::IOSurfaceImageBuffer<img::Format::Abgr8u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::iosimg::IOSurfaceImageBuffer<img::Format::Argb16u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::iosimg::IOSurfaceImageBuffer<img::Format::Argb8u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::iosimg::IOSurfaceImageBuffer<img::Format::Bgr8u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::iosimg::IOSurfaceImageBuffer<img::Format::Bgra8u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::iosimg::IOSurfaceImageBuffer<img::Format::Gray16f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::iosimg::IOSurfaceImageBuffer<img::Format::Gray16u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::iosimg::IOSurfaceImageBuffer<img::Format::Gray32f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::iosimg::IOSurfaceImageBuffer<img::Format::Gray8u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::iosimg::IOSurfaceImageBuffer<img::Format::Rgb16u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::iosimg::IOSurfaceImageBuffer<img::Format::Rgb8u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::iosimg::IOSurfaceImageBuffer<img::Format::Rgba16f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::iosimg::IOSurfaceImageBuffer<img::Format::Rgba32f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::iosimg::IOSurfaceImageBuffer<img::Format::Rgba8u>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::iosimg::IOSurfaceImageBuffer<img::Format::Two16f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::iosimg::IOSurfaceImageBuffer<img::Format::Two32f>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::iosimg::IOSurfaceImageBuffer<img::Format::Two8u>]"
+ "std::aligned_alloc failed to allocate "
+ "std::any owner for CFData backing store"
+ "std::set({util::RelativePoseConstraint::Source::External}) .contains(constraint_Cref_to_Cquery.source)"
+ "std::set({util::RelativePoseConstraint::Source::Vision, util::RelativePoseConstraint::Source::External}) .contains(constraint_Cref_to_Cquery.source)"
+ "std::set({util::RelativePoseConstraint::Source::Vision}) .contains(constraint_Cref_to_Cquery.source)"
+ "subgraph_"
+ "subgraphs_.at(subgraph_id).graph.nodes().contains(new_rep_id)"
+ "subgraphs_.at(subgraph_id).graph.nodes().size() >= 2"
+ "subgraphs_.contains(current_id)"
+ "subgraphs_.contains(neighbor_id)"
+ "subgraphs_.contains(subgraph_id)"
+ "submap != nullptr"
+ "surface"
+ "test_prune_info"
+ "this->surface->Format() == pf::PixelFormat::OneComponent_8"
+ "this->surface->Height() == descs.size()"
+ "this->surface->Width() == BinaryDescriptorType::DIMS"
+ "uint64"
+ "uncertainty != nullptr"
+ "unreachable"
+ "validation_result.has_value()"
+ "var_iter != ls->endVariable<vio::VIO4DoFDeltaPoseVariable<double>>()"
+ "viz::ContextStatistics"
+ "viz::LimitedRecorder"
+ "viz::Records"
+ "viz::UnlimitedRecorder"
+ "vmk_surface_pool"
+ "walkability_map != nullptr"
+ "walkability_map("
+ "width != 0"
+ "with "
+ "xyz: "
+ "{:.7f}"
- " (ENOMEM)"
- " < "
- "->"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Essentials/Apple/src/BundlePath.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Essentials/Apple/src/Clock.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Essentials/Array/include/Essentials/Array/ArrayView.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Essentials/Array/src/ArrayBuffer.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Essentials/Dispatch/src/DispatchQueue.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Essentials/Dispatch/src/DispatchQueueTypeUtil.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Essentials/Dispatch/src/GrandCentralDispatchUtil.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Essentials/IO/include/Essentials/IO/Archive.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Essentials/Log/src/APILogging.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/Concurrency/include/Kit/Concurrency/Channel/Node.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/Concurrency/include/Kit/Concurrency/Channel/detail/ChannelInputModel.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/Concurrency/include/Kit/Concurrency/Channel/detail/Processor.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/Concurrency/include/Kit/Concurrency/Channel/detail/ProcessorInputMessageHandlingStrategy.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/Concurrency/src/Channel/NodeTaskScheduler.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/Concurrency/src/Channel/NodeTaskSchedulerPool.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/Container/src/Lines.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/Container/src/Points.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/CoreGraphics/src/ColorSpaceRef.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/CoreGraphics/src/DataProviderRef.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/CoreGraphics/src/ImageRef.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/CoreVideo/include/Kit/CoreVideo/PixelBufferRef.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/CoreVideo/src/CVImage.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/CoreVideo/src/CVImage.cpp:56"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/CoreVideo/src/PixelBufferRef.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/Foundation/FoundationIO/include/Kit/FoundationIO/DictionaryRefIO.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/Foundation/include/Kit/Foundation/Ptr.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/Foundation/src/BundleRef.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/Foundation/src/DictionaryRef.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/Foundation/src/Ptr.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/Foundation/src/Ref.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/Foundation/src/URLRef.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/Foundation/src/UUIDRef.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/Image/include/Kit/Image/FormatAlgorithm.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/Image/include/Kit/Image/ImageBuffer.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/Image/include/Kit/Image/ImageView.h:1290"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/Image/include/Kit/Image/ImageView.h:1300"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/Image/include/Kit/Image/SharedImage.h:1237"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/Image/src/ImageStorage.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/Image/src/Size.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/ImageIO/include/Kit/ImageIO/ImageIO.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/ImageIO/src/Apple.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/ImageIO/src/ImageDestinationRef.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/ImageIO/src/ImageIO.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/ImageIO/src/Pnm.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/ImageIO/src/Serialization.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/Memory/include/Kit/Memory/VMAllocator.hpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/Mesh/include/Kit/Mesh/TriMeshAllocator.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/Mesh/src/TriMesh.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/Mesh/src/TriMeshAllocator.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/Mesh/src/TriMeshIO.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/Visualization/include/Kit/Visualization/DataIO.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/Visualization/include/Kit/Visualization/IData.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/Visualization/src/Client.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/Visualization/src/DataIO.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/Visualization/src/DataType.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/Visualization/src/FileIOPrivate.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/Visualization/src/IData.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/Visualization/src/NamedContext.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/Visualization/src/NetworkData.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Kit/Visualization/src/VisualLogger.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/VIO/Calibration/include/VIO/Calibration/CalibrationUtil.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/VIO/Geometry/include/VIO/Geometry/BicubicHermiteSpline.hpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/VIO/Geometry/include/VIO/Geometry/CubicSplineKnots.hpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/VIO/Geometry/include/VIO/Geometry/LensModel.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/VIO/Geometry/include/VIO/Geometry/LensModel.hpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/VIO/Geometry/include/VIO/Geometry/RANSAC/DataPointCorrespondenceUtil.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/VIO/Geometry/include/VIO/Geometry/RANSAC/HypothesisUtil.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/VIO/Geometry/src/FreeformLensDistortion.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/VIO/Geometry/src/LensModel.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/VIO/Geometry/src/RANSAC/FivePointPreemptiveRansac.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/VIO/Geometry/src/TwoViewEstimators.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/VIO/MapOptimization/include/VIO/MapOptimization/PoseGraphSample.hpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/VIO/Util/include/VIO/Util/Variant.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/VIO/VIOEstimator/include/VIO/VIOEstimator/VIOEpipolarFactor.hpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/VIO/VIOEstimator/include/VIO/VIOEstimator/viovariables.hpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/FeatureExtraction/src/FeatureMatching.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/FeatureMatching/src/FeatureMatching.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/Mapping/src/Private/CameraCalibration.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/Mapping/src/Private/IO/BiMapSample.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/Mapping/src/Private/MapDatabase.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/Mapping/src/Private/MapDatabaseUtil.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/Mapping/src/Private/MappingManager.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/Mapping/src/Private/PoseGraph.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/Mapping/src/Private/VisualLoggerUtil.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/VisualMappingKit/VisualMappingKit/include_private/VisualMappingKit/Private/VMKConversion.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/VisualMappingKit/VisualMappingKit/src/VMKDataTypes.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/VisualMappingKit/VisualMappingKit/src/VMKDatabase.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/VisualMappingKit/VisualMappingKit/src/VMKDatabaseConfig.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/VisualMappingKit/VisualMappingKit/src/VMKLogging.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/VisualMappingKit/VisualMappingKit/src/VMKSession.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/VisualMappingKit/VisualMappingKit/src/VMKSessionConfig.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/VisualMappingKit/include_private/Vuelta/VisualMappingKit/DatabaseFrameSample.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/VisualMappingKit/src/DataFrameSample.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualMappingKit/library/Vuelta/VisualMappingKit/src/Database.cpp"
- ": error code "
- "AddDatabaseFrame(frame)"
- "Camera calibration already exists"
- "Convergence in the cost: "
- "Create database failed error: %s"
- "DescriptorCountMismatch"
- "Failed to add epipolar edge"
- "Image ID not found in map"
- "Image uuid already in database"
- "Iref_to_Iquery must be set if Cref_to_Cquery is set"
- "No UUID for removed keyframe"
- "NoCalibrationData"
- "NotEnoughInliers"
- "NotEnoughMatches"
- "Source ID mismatch, this is not supported"
- "T_Iref_to_Iquery.has_value()"
- "UndistortionFailed"
- "Unsupported camera config"
- "Unsupported lens type!"
- "[%s] %s"
- "[error][grad < gtol]["
- "[iter][old->new][delta < ptol][grad < gtol][delta < ctol]["
- "[iter][old->new][delta < ptol][grad < gtol][delta < ctol][lambda]["
- "]["
- "cf_current_bundle"
- "cg_image.IsValid()"
- "config_.debug_config.loop_closure_constraint_type == RelativeCameraPoseConstraintType::CameraToCamera5DoFEpipolarCovariance || config_.debug_config.loop_closure_constraint_type == RelativeCameraPoseConstraintType::CameraToCamera5DoFHeuristicCovariance"
- "current_state_id_ > 0u"
- "database_->AddToBiMap(result.query_id, image_id)"
- "eval.external_maps"
- "eval.map"
- "ext_map->SessionId() != this->SessionId()"
- "image_id.source == source_id_"
- "image_retrieval"
- "index < result->relative_poses.size()"
- "keypoints"
- "m().database.find(frame.uuid) == m().database.end()"
- "map_.erase(image_id)"
- "max_hypothesis <= max_trials"
- "max_hypothesis > 0"
- "op_result.has_value()"
- "op_uuid"
- "posix_memalign failed to allocate "
- "ratio<"
- "received data of timestamp "
- "ref_image_id.source == vio::cv_types::CameraSourceID{0}"
- "ref_ret && \"Lens model undistortion failed this should not happen\""
- "reloc_info"
- "selected_keyframe"
- "vuelta::VueltaVisualLogging"

```
