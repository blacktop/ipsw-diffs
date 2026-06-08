## Recon3D

> `/System/Library/PrivateFrameworks/Recon3D.framework/Recon3D`

```diff

-8.25.11.4.5
-  __TEXT.__text: 0x1856148
-  __TEXT.__auth_stubs: 0x2b20
-  __TEXT.__const: 0x119460
-  __TEXT.__cstring: 0x4b810
-  __TEXT.__gcc_except_tab: 0xf2a7c
-  __TEXT.__oslogstring: 0x8331
-  __TEXT.__unwind_info: 0x351c8
+9.26.5.12.6
+  __TEXT.__text: 0x172b0c4
+  __TEXT.__const: 0x1135e0
+  __TEXT.__cstring: 0x4d3ff
+  __TEXT.__gcc_except_tab: 0xed800
+  __TEXT.__oslogstring: 0x88da
+  __TEXT.__unwind_info: 0x37320
   __TEXT.__eh_frame: 0x125c
-  __TEXT.__objc_classname: 0x1
-  __TEXT.__objc_methname: 0xc58
-  __TEXT.__objc_stubs: 0x10e0
-  __DATA_CONST.__got: 0x518
-  __DATA_CONST.__const: 0x1ca8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_methname: 0x0
+  __DATA_CONST.__const: 0x2048
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__weak_got: 0x28
   __DATA_CONST.__objc_selrefs: 0x438
-  __AUTH_CONST.__auth_got: 0x15a0
-  __AUTH_CONST.__const: 0x60b78
+  __DATA_CONST.__got: 0x4f0
+  __AUTH_CONST.__const: 0x60a98
   __AUTH_CONST.__cfstring: 0x4a0
+  __AUTH_CONST.__weak_auth_got: 0x58
   __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__auth_got: 0x1638
   __AUTH.__data: 0x10
   __AUTH.__thread_vars: 0x48
   __AUTH.__thread_bss: 0x38
-  __DATA.__data: 0x57b0
+  __DATA.__data: 0x57c0
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x70
+  __DATA.__bss: 0x68
   __DATA.__common: 0x7a8
   __DATA_DIRTY.__data: 0x68
-  __DATA_DIRTY.__bss: 0x3f38
+  __DATA_DIRTY.__bss: 0x3f60
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 821721B1-8532-34DE-B505-9A4BDF21E7BF
-  Functions: 37656
-  Symbols:   1831
-  CStrings:  7419
+  - /usr/lib/libsqlite3.dylib
+  UUID: 8CDF5445-DDF3-3BEC-8A3C-585B9D3635A8
+  Functions: 38095
+  Symbols:   1890
+  CStrings:  7409
 
Symbols:
+ _CFErrorCopyFailureReason
+ _CFErrorCopyUserInfo
+ _CFErrorGetCode
+ _CFErrorGetDomain
+ _CV3DReconClipPlaneWithVolume
+ _CV3DReconPlaneComputeMeshForConvexHull
+ _CV3DReconPlaneComputeMeshForPolygons
+ _CV3DReconPlaneCopy
+ _CV3DReconPlaneCopyUUID
+ _CV3DReconPlaneDetectionUpdateGetPlaneList
+ _CV3DReconPlaneExtentOrientedBoundingBox
+ _CV3DReconPlaneGetMaterialLabel
+ _CV3DReconPlaneGetOrientation
+ _CV3DReconPlaneGetPersistedStatus
+ _CV3DReconPlaneGetReconSemanticLabel
+ _CV3DReconPlaneListCopyIndexAt
+ _CV3DReconPlaneListLength
+ _CV3DReconPlaneListRelease
+ _CV3DReconPlaneNormal
+ _CV3DReconPlaneRelease
+ _CV3DReconPlaneRetain
+ _CV3DReconPlaneSupport
+ _CV3DReconPlaneTransformationToWorld
+ _CV3DReconPrivacyFilterConfigurationCreate
+ _CV3DReconPrivacyFilterConfigurationRelease
+ _CV3DReconPrivacyFilterConfigurationSetInvertMeshFilter
+ _CV3DReconPrivacyHandlerAddClientWithPrivacyConfiguration
+ _CV3DReconSceneQueryCreateMeshListFromIncrementalUpdate
+ _CV3DReconSceneQueryCreateMeshListFromState
+ _CV3DReconSceneQueryCreatePlaneDetectionUpdateFromIncrementalUpdate
+ _CV3DReconSceneQueryCreatePlaneDetectionUpdateFromState
+ _CV3DReconSceneQueryCreateRemovedMeshUUIDsFromIncrementalUpdate
+ _CV3DReconSceneQuerySessionFindFloorPlane
+ _CV3DReconSlamMetadataGetExternalAnchorCount
+ _CV3DReconSlamMetadataGetExternalAnchorUUID
+ _CV3DReconSlamMetadataGetIs3dof
+ _CV3DReconSlamMetadataGetIsInitialized
+ _CV3DReconSlamMetadataGetMapSize
+ _CV3DReconSlamMetadataGetNearAnchorCount
+ _CV3DReconSlamMetadataGetNearAnchorUUID
+ _CV3DReconSlamMetadataGetNewAnchorCount
+ _CV3DReconSlamMetadataGetNewAnchorUUID
+ _CV3DReconSlamMetadataGetReinitializeAttempts
+ _CV3DReconSlamMetadataGetRemovedAnchorCount
+ _CV3DReconSlamMetadataGetRemovedAnchorUUID
+ _CV3DReconSlamMetadataGetSLAMMode
+ _CV3DReconSlamMetadataGetTimestamp
+ _CV3DReconSlamMetadataGetTrackingIsNominal
+ _CV3DReconSlamMetadataGetUpdatedAnchorCount
+ _CV3DReconSlamMetadataGetUpdatedAnchorUUID
+ __ZNKSt3__110error_code7messageEv
+ __ZNSt3__121recursive_timed_mutex4lockEv
+ __ZNSt3__121recursive_timed_mutex6unlockEv
+ __ZNSt3__121recursive_timed_mutexC1Ev
+ __ZNSt3__121recursive_timed_mutexD1Ev
+ __ZNSt3__16stoullERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi
+ _dispatch_time
+ _kCFErrorUnderlyingErrorKey
+ _kCFNull
+ _kCV3DReconPlaneOrientationHorizontal
+ _kCV3DReconPlaneOrientationOther
+ _kCV3DReconPlaneOrientationVertical
+ _kCV3DReconPlanePersistedStatusLoaded
+ _kCV3DReconPlanePersistedStatusLoadedAndUpdated
+ _kCV3DReconPlanePersistedStatusNew
+ _kCV3DReconSessionPresetXrOSSuppressAllMapping
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
+ _sin
+ _sqlite3_backup_finish
+ _sqlite3_backup_init
+ _sqlite3_backup_step
+ _sqlite3_bind_blob
+ _sqlite3_bind_int64
+ _sqlite3_bind_text
+ _sqlite3_changes
+ _sqlite3_close
+ _sqlite3_column_blob
+ _sqlite3_column_bytes
+ _sqlite3_column_int64
+ _sqlite3_column_text
+ _sqlite3_db_handle
+ _sqlite3_errmsg
+ _sqlite3_exec
+ _sqlite3_finalize
+ _sqlite3_free
+ _sqlite3_open
+ _sqlite3_open_v2
+ _sqlite3_prepare_v2
+ _sqlite3_reset
+ _sqlite3_step
- _AppleDepthRuntimeAPIVersion
- _CFErrorCopyDescription
- _CV3DPlaneDetectionCutIfInside
- _CV3DPlaneDetectionGetMaterialLabel
- _CV3DPlaneDetectionGetReconSemanticLabel
- _CV3DPlaneDetectionPlaneCreateTriangulatedConvexHull
- _CV3DPlaneDetectionPlaneCreateTriangulatedPolygons
- _CV3DPlaneDetectionPlaneExtentPolygons
- _CV3DPlaneDetectionPlanePolygonNumInnerRings
- _CV3DPlaneDetectionPlanePolygonOuterRing
- _CV3DPlaneDetectionPlaneTriangulatedConvexHull
- _CV3DPlaneDetectionPlaneTriangulatedPolygons
- _CV3DPlaneDetectionPolygonAtIndex
- _CV3DPlaneDetectionPolygonInnerRingAtIndex
- _CV3DPlaneDetectionPolygonListLength
- _CV3DPlaneDetectionPolygonPointsNum
- _CV3DPlaneDetectionPolygonPointsRawPtr
- _CV3DPlaneDetectionPolygonRingPointsNum
- _CV3DPlaneDetectionPolygonRingPointsRawPtr
- _CV3DPlaneDetectionSingleShotPlaneAtIndex
- _CV3DPlaneDetectionSingleShotPlaneExtentPolygons
- _CV3DReconPlaneDetectionUpdateGetUpdatedPlanes
- _CV3DReconPlaneDetectionUpdateUpdatedPlanes
- _CV3DReconRoomBoundaryResultGetRoomStability
- _CV3DReconSceneQuerySessionCopyFloorPlane
- _CV3DReconSceneQuerySessionGetFloorPlane
- _dpotrs$NEWLAPACK
- _kCFErrorLocalizedDescriptionKey
- _objc_autorelease
- _objc_release_x27
- _objc_release_x28
- _objc_retain_x24
- _objc_retain_x26
- _objc_retain_x27
- _objc_retain_x28
CStrings:
+ "\n        CREATE TABLE IF NOT EXISTS blob_data (\n            key TEXT PRIMARY KEY,\n            data BLOB NOT NULL,\n            FOREIGN KEY (key) REFERENCES blob_metadata(key) ON DELETE CASCADE\n        )\n    "
+ "\n        CREATE TABLE IF NOT EXISTS blob_metadata (\n            key TEXT PRIMARY KEY,\n            size INTEGER NOT NULL,\n            write_time INTEGER NOT NULL\n        )\n    "
+ "  "
+ "  #"
+ " : %.*s"
+ " but no specialization is available. "
+ " which is not in the provided type list "
+ "!sum.empty()"
+ "%s: %s:%d"
+ "-inf"
+ ". The network connection may be stalled or the server stopped reading. Restart the VisualLogger server and reconnect the client to recover."
+ "/AppleInternal/Library/BuildRoots/4~CRCjugAn_mBnhHTuS7tG5d1VmkabPl9aJqKD8wU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/has_self_intersections.hpp"
+ "/AppleInternal/Library/BuildRoots/4~CRCjugAn_mBnhHTuS7tG5d1VmkabPl9aJqKD8wU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/overlay/add_rings.hpp"
+ "/AppleInternal/Library/BuildRoots/4~CRCjugAn_mBnhHTuS7tG5d1VmkabPl9aJqKD8wU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/overlay/get_turn_info_la.hpp"
+ "/AppleInternal/Library/BuildRoots/4~CRCjugAn_mBnhHTuS7tG5d1VmkabPl9aJqKD8wU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/boost/rational.hpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Recon3D/library/AppleCV3D/Recon3D_framework/src/CV3DReconPlane.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Recon3D/library/Kit/Foundation/src/NumberRef.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Recon3D/library/Kit/IOSurface/src/IOSurfaceRef_maybe_mno_unaligned_access.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Recon3D/library/Kit/SQLite/src/SQLiteBlobStore+Private.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Recon3D/library/Kit/SQLite/src/SQLiteBlobStore.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Recon3D/library/Reconstruction/Common/include/Reconstruction/Common/Types.h"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Recon3D/library/Reconstruction/Filesystem/include/Reconstruction/Filesystem/LRUCache.h"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Recon3D/library/Reconstruction/Frame/src/FrameBundleSample.cpp"
+ "; caused by:\n"
+ "Already in transaction"
+ "An error occurred while loading the image"
+ "ApplyIncrementalUpdate: mesh state exists but no mesh update provided"
+ "ApplyIncrementalUpdate: plane state exists but no plane update provided"
+ "ApplyIncrementalUpdate: room_boundary_state exists but no room update provided"
+ "BEGIN TRANSACTION"
+ "COMMIT"
+ "Cannot clone while transaction is in progress"
+ "Cannot merge mapped meshes - all meshes must be owned"
+ "Cannot read from \"{}\""
+ "Cannot write to \"{}\""
+ "Could not deserialize key (possible corruption), removing: %s"
+ "Could not load keyframe database: %s. Removing %lu keyframes"
+ "Could not read key (possible corruption), removing: %s"
+ "Could not remove orphaned data file (%s) from persistence"
+ "Could not write keyframe metadata: "
+ "DELETE"
+ "DELETE FROM blob_metadata WHERE key = ?"
+ "Database integrity check failed"
+ "Database integrity check returned no result"
+ "Disk access is not yet available. Initializing with in-memory database."
+ "EXCLUSIVE"
+ "Error converting FrameBundle to bytes: %s"
+ "Error listing persistence keys"
+ "Error saving keyframe database after loading it successfully. Error: %s"
+ "Error saving keyframe metadata: %s"
+ "Exception during async transaction execution: %s"
+ "Exception during transaction cleanup: %s"
+ "ExpectedResult<FrameBundle> cv3d::recon::LoadFrameBundleFromVisualLoggerBinary(std::istream &)"
+ "ExpectedResult<FrameBundle> cv3d::recon::frame::FrameBundleFromBytes(const std::span<const std::byte> &)"
+ "ExpectedResult<T> cv3d::recon::sng::GetExpectedOr(std::future<T> &, std::string_view) [T = std::shared_future<bool>]"
+ "ExpectedResult<arr::Array2<SceneTypeBundle>> cv3d::recon::kf::SceneTypePreprocessor::DecodeProbabilities(const img::ConstImageViewBgra8u &, const img::ConstImageViewRgba32f &)"
+ "ExpectedResult<cf::DataRef> cv3d::recon::frame::FrameBundleToData(const FrameBundle &)"
+ "ExpectedResult<optional<ProcessFrameBundleResult::KeyframeReturnType>> cv3d::recon::sng::SessionNodeGroup::Impl::ProcessFrameBundleKF(const FrameBundle &)"
+ "ExpectedResult<optional<T>> cv3d::recon::sng::GetOrError(std::future<ExpectedResult<T>> &, std::string_view) [T = std::shared_ptr<const cv3d::recon::kfplanes::PlaneDetectionResult>]"
+ "ExpectedResult<optional<T>> cv3d::recon::sng::GetOrError(std::future<ExpectedResult<T>> &, std::string_view) [T = std::shared_ptr<cv3d::recon::kf::KeyframeEngineResult>]"
+ "ExpectedResult<optional<T>> cv3d::recon::sng::GetOrWait(std::future<T> &, std::string_view) [T = std::optional<cv3d::recon::sng::MeshingNodeMeshUpdateResult>]"
+ "ExpectedResult<std::future<bool>> cv3d::recon::sng::SessionNodeGroup::Impl::ProcessSaveWorkerSnapshotsTo(const SaveSnapshotToRequest &)"
+ "ExpectedSuccess cv3d::recon::MeshingConfig::SetDepthRange(float, float)"
+ "ExpectedSuccess cv3d::recon::MeshingConfig::SetMaxVoxelWeight(float)"
+ "ExpectedSuccess cv3d::recon::MeshingConfig::SetMinMeshingPeriod(const CFTimeInterval)"
+ "ExpectedSuccess cv3d::recon::MeshingConfig::SetNumFusionSamples(uint32_t)"
+ "ExpectedSuccess cv3d::recon::MeshingConfig::SetOccupancyByProximityConfig(float, float, float)"
+ "ExpectedSuccess cv3d::recon::kf::SceneTypePreprocessor::AddFrame(const FrameBundle &)"
+ "ExpectedSuccess cv3d::recon::sng::GetError(std::future<bool> &, std::string_view)"
+ "ExpectedSuccess cv3d::recon::sng::SessionNodeGroup::Impl::ProcessSaveDiagnosticData(const SaveDiagnosticDataRequest &)"
+ "ExpectedSuccess cv3d::recon::sng::SessionNodeGroup::Impl::ProcessSaveSnapshotTo(const SaveSnapshotToRequest &)"
+ "Failed to convert bundle URL to string"
+ "Failed to create physical SQLite database after file access granted. Continuing with in-memory database."
+ "Failed to import %zu persistence files"
+ "Failed to migrate %zu files from in-memory to file-backed database."
+ "Failed to open/create persistence database: %s. Falling back to in-memory database."
+ "Failed to prepare SQL statement \"{}\": {}"
+ "Failed to prepare quick_check statement"
+ "Failed to remove file after import: "
+ "Failed to write key '%s' during async transaction"
+ "Filesystem access not available"
+ "Folder does not exist: \"{}\""
+ "Folder does not have read permissions: \"{}\""
+ "Folder does not have write permissions: \"{}\""
+ "ForType called with ArithmeticType::"
+ "HasAppleNeuralEngine"
+ "INSERT OR REPLACE INTO blob_data (key, data) VALUES (?, ?)"
+ "INSERT OR REPLACE INTO blob_metadata (key, size, write_time) VALUES (?, ?, ?)"
+ "Imported %zu persistence files (ignored %zu)"
+ "In-memory only mode"
+ "Include <Kit/Common/ArithmeticType_Half.h> to support half type."
+ "Incremental update has no mesh update"
+ "Incremental update has no plane update"
+ "Initializing SurfaceDetection visual logger from user defaults: logger=%s, contexts=%s"
+ "IsOwned()"
+ "Key '%s' not found during async remove"
+ "Keyframe Occupancy Cluster ID: %s"
+ "Keyframe processing suppressed by configuration."
+ "Keyframes persistence disabled. Using temporary folder for data: "
+ "Loaded keyframe database: with %lu keyframes"
+ "Loading from persistence; number of keys=%lu"
+ "MEMORY"
+ "Maximum voxel weight should be in range (0,255]"
+ "Mesh must be owned to set as room mesh"
+ "Migrated %zu files from in-memory to file-backed database."
+ "NORMAL"
+ "Nested transactions are not supported"
+ "Network send did not complete within "
+ "No active transaction to commit"
+ "Not in transaction"
+ "Num files on disk: data (%u), metadata (%zu)"
+ "OFF"
+ "OwnedMesh() called on mapped mesh"
+ "PERSIST"
+ "PRAGMA foreign_keys = 1;\nPRAGMA synchronous = 1;\nPRAGMA temp_store = 2;\nPRAGMA journal_mode = {};\nPRAGMA locking_mode = {};\nPRAGMA cache_size = {};\n"
+ "PRAGMA quick_check"
+ "PRAGMA {}"
+ "PRAGMA {} validation failed. Expected: {}, Actual: {}"
+ "Persistence data migration attempt failed: %s"
+ "Persistence database failed integrity check: %s"
+ "Persistence database is corrupted. Removing file and creating new database. Error: %s"
+ "Persistence filesystem is required"
+ "Plane has no convex hull extent to triangulate"
+ "Plane has no oriented bounding box extent"
+ "Plane has no polygon extent to triangulate"
+ "Plane is NULL"
+ "Plane list is NULL"
+ "Privacy filter configuration is NULL"
+ "ProcessReconResult: keyframing_state requested but no keyframe result provided"
+ "ProcessReconResult: mesh_state requested but no mesh list provided"
+ "ProcessReconResult: plane_state requested but no plane result provided"
+ "ProcessReconResult: room_boundary_state requested but no keyframe result provided"
+ "ProcessReconResult: room_boundary_state requested but no room boundary result provided"
+ "ROLLBACK"
+ "Removed orphaned data file (no metadata): %s"
+ "Removed orphaned metadata (no data file) for key: %s"
+ "SELECT 1 FROM blob_metadata WHERE key = ? LIMIT 1"
+ "SELECT data FROM blob_data WHERE key = ?"
+ "SELECT key, size, write_time FROM blob_metadata ORDER BY key"
+ "SELECT key, size, write_time FROM blob_metadata WHERE key = ?"
+ "SQLite error: "
+ "SQLitePersistenceFilesystem"
+ "State has no mesh state"
+ "State has no plane state"
+ "Stats.Monitoring"
+ "Stats.ObservationMapping"
+ "Successfully purged KFS %.13s that was not loaded in memory from filesystem."
+ "SurfaceDetection Domain"
+ "TRUNCATE"
+ "To be clipped plane has no extents: convexhull-%s"
+ "Transaction was started by a different thread"
+ "Unexpected exception: {}"
+ "Unknown SQLite error"
+ "Unknown exception during async transaction execution"
+ "Unknown exception during transaction cleanup"
+ "WAL"
+ "acv_plane.convexHullExtent"
+ "cache_size"
+ "circular_queue_"
+ "com.apple.surfacedetection.visual_logger.contexts"
+ "com.apple.surfacedetection.visual_logger.logger"
+ "cv3d.applecv3d"
+ "cv3d.cf"
+ "cv3d.function"
+ "cv3d.recon.file_system"
+ "cv3d::kit::sqlite::SQLiteBlobStore::Private::Private(const std::string &, const Config &, const std::shared_ptr<time::IClock> &, OpenMode)"
+ "f16"
+ "foreign_keys"
+ "global_plane.polygons_extent.has_value()"
+ "idx < p_->GetCachedBaseAddresses().size()"
+ "journal_mode"
+ "locking_mode"
+ "main"
+ "mesh_data.IsOwned()"
+ "mesh_data.OwnedMesh().mesh != nullptr"
+ "multiple error causes"
+ "network send timed out (connection may be stalled)"
+ "num_metadata_entries"
+ "persistence.db"
+ "persistence_fs_"
+ "result.convex_hull_extent.has_value()"
+ "sqlite3_stmt *cv3d::kit::sqlite::(anonymous namespace)::PrepareStatement(sqlite3 *, const char *)"
+ "static ExpectedResult<FrameBundle> CV3DReconFrameBundle::LoadVisualLogger(std::string_view, cv3d::kit::fs::IFilesystem &)"
+ "static ExpectedResult<SQLiteBlobStore> cv3d::kit::sqlite::SQLiteBlobStore::Create(const std::string &, const Config &, const std::shared_ptr<time::IClock> &)"
+ "static ExpectedResult<SQLiteBlobStore> cv3d::kit::sqlite::SQLiteBlobStore::Open(const std::string &, const Config &, const std::shared_ptr<time::IClock> &)"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::con::NumbersT<cv3d::kit::memory::Mutability::Const, cv3d::kit::memory::Ownership::Shared>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::concurrency::ChannelOutput<std::experimental::expected<cv3d::recon::frame::KeyframeData, cv3d::esn::Error>>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::memory::Mutability::Const]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::memory::Ownership::Shared]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::memory::Protection::Unprotected]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::ValueData<cv3d::kit::con::NumbersT<cv3d::kit::memory::Mutability::Const, cv3d::kit::memory::Ownership::Shared>>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = std::experimental::expected<cv3d::recon::frame::KeyframeData, cv3d::esn::Error> (const cv3d::esn::random::UUID &)]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = std::experimental::expected<cv3d::recon::frame::KeyframeData, cv3d::esn::Error>]"
+ "synchronous"
+ "temp_store"
+ "virtual ExpectedCpuKeyframePtr cv3d::recon::kf::KeyframeEngine::CopyKeyframeFromUUID(const KeyframeId &) const"
+ "void cv3d::kit::sqlite::(anonymous namespace)::ExecuteSQL(sqlite3 *, const char *)"
+ "vt1 == nullptr"
- " format."
- " from: "
- " option"
- "&"
- "(mesh.colors.size() == 0 || mesh.colors.size() == mesh.vertices.size())"
- "+N9mZUAHooNvMiQnjeTJ8g"
- ".Origins"
- ".Storage"
- "/AppleInternal/Library/BuildRoots/4~CNqDugCTP3lN-PxA5XD01aNoAfB_BYlniW-U-Os/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/has_self_intersections.hpp"
- "/AppleInternal/Library/BuildRoots/4~CNqDugCTP3lN-PxA5XD01aNoAfB_BYlniW-U-Os/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/overlay/add_rings.hpp"
- "/AppleInternal/Library/BuildRoots/4~CNqDugCTP3lN-PxA5XD01aNoAfB_BYlniW-U-Os/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/overlay/get_turn_info_la.hpp"
- "/AppleInternal/Library/BuildRoots/4~CNqDugCTP3lN-PxA5XD01aNoAfB_BYlniW-U-Os/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/include/boost/rational.hpp"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Recon3D/library/AppleCV3D/Recon3D_framework/src/CV3DPlaneDetectionPlane+Private.cpp"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Recon3D/library/AppleCV3D/Recon3D_framework/src/CV3DPlaneDetectionPlane.cpp"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Recon3D/library/Kit/IOSurface/src/IOSurfaceRef.cpp"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Recon3D/library/Reconstruction/Geometry/include/Reconstruction/Geometry/NearestNeighbor3D.hpp"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Recon3D/library/Reconstruction/KeyframePlanes/include_private/Reconstruction/KeyframePlanes/IPersistenceFilesystem.h"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Recon3D/library/Reconstruction/KeyframePlanes/include_private/Reconstruction/KeyframePlanes/LRUCache.h"
- "0 "
- "Cannot read from "
- "Cannot write to "
- "Could not create folder: "
- "Could not load file(possible corruption), deleting: %s"
- "Could not load kfd %s: %s. Removing %lu keyframes"
- "Could not read file(possible corruption), deleting: %s"
- "Could not remove keyframe: "
- "Could not remove orphaned file (%s) from persistence path"
- "Could not remove unloadable file: %s"
- "Could not remove unreadable file: %s"
- "Could not write file: "
- "Edge ID exceeds limit"
- "EraseAllRemove"
- "EraseNotObserve"
- "Error capturing kd to %s after loading it successfully. Error: %s"
- "Error listing contents of "
- "Error saving kd to %s. Error: %s"
- "Failed to estimate %{private}s height room floor/ceiling"
- "Filesystem doesn't support caching"
- "First load attempt; number of files in path=%lu"
- "Folder does not exist: "
- "Folder does not exist: %s"
- "Folder does not have read permissions: "
- "Folder does not have write permissions: "
- "Found active kf being orphaned in persistence path (%s)"
- "GPUEndTime"
- "GPUStartTime"
- "Global plane %.13s does not have oriented bounding box when computing room associations."
- "HoldsTriMeshData()"
- "Input point clouds must have the same size"
- "KFs.KF-%s.%s-%s"
- "Keyframes persistence disabled. Using temporary folder: "
- "Num files on disk: data (%u), metadata (%u)"
- "Persistence disabled, not loading keyframe database: %s"
- "Plane result does not have material label"
- "Plane result does not have recon semantics"
- "Plane result is NULL"
- "Planes"
- "Removed orphaned file (%s) from persistence path"
- "Stack size can't be more than 32"
- "Sucessfully purged KFS %.13s that was not loaded in memory from filesystem."
- "Surface has no bounding box"
- "Surface has no material"
- "Surface has no semantics"
- "To be clipped plane has no extents: obb-%s, convexhull-%s"
- "UTF8String"
- "Unable to read metadata folder: "
- "Unable to read metadata folder: %s"
- "Unexpected exception: "
- "] "
- "_v2"
- "addCompletedHandler:"
- "addObject:"
- "approximate_overlap || boundary_simple_polygon.has_value()"
- "array::at"
- "arrayByAddingObject:"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "bankIds"
- "blitCommandEncoder"
- "cStringUsingEncoding:"
- "cameraPixels"
- "cg_image.IsValid()"
- "colorAttachments"
- "commandBuffer"
- "commandQueue"
- "commit"
- "commitAndWaitUntilSubmitted"
- "computeCommandEncoder"
- "contents"
- "copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:"
- "copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:"
- "dataWithPropertyList:format:options:error:"
- "defaultCStringEncoding"
- "deintegrated"
- "depthAttachment"
- "description"
- "dictionaryRepresentation"
- "dispatchThreadgroups:threadsPerThreadgroup:"
- "drain"
- "drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferOffset:"
- "drawPrimitives:vertexStart:vertexCount:"
- "echoIds"
- "edge_id < mesh.edges.size()"
- "endEncoding"
- "euclideanDistances"
- "fileURLWithPath:"
- "fillBuffer:range:value:"
- "flags"
- "getBytes:bytesPerRow:fromRegion:mipmapLevel:"
- "getBytes:length:"
- "global_plane.polygonsExtent.has_value()"
- "gp.orientedBoxExtent.has_value()"
- "idx < p_->GetCachedBaseAddress().size()"
- "initWithSuiteName:"
- "intensities"
- "iosurface"
- "kLevel < kNumMeshLevels - 1"
- "kernelEndTime"
- "kernelStartTime"
- "length"
- "localizedDescription"
- "maxTotalThreadsPerThreadgroup"
- "mesh.edges.size() > edge_id"
- "newBinaryArchiveWithDescriptor:error:"
- "newBufferWithBytes:length:options:"
- "newBufferWithBytesNoCopy:length:options:deallocator:"
- "newBufferWithLength:options:"
- "newCommandQueue"
- "newComputePipelineStateWithDescriptor:options:reflection:error:"
- "newDepthStencilStateWithDescriptor:"
- "newFunctionWithName:"
- "newLibraryWithURL:error:"
- "newRenderPipelineStateWithDescriptor:options:reflection:error:"
- "newSamplerStateWithDescriptor:"
- "newTextureWithDescriptor:"
- "newTextureWithDescriptor:iosurface:plane:"
- "num_descriptors == spfhs.size()"
- "num_metadata_files"
- "numberWithBool:"
- "numberWithFloat:"
- "numberWithUnsignedChar:"
- "objectAtIndexedSubscript:"
- "plane.orientedBoxExtent.has_value()"
- "pointcloud and spfhs size mismatch."
- "points"
- "processInfo"
- "processName"
- "renderCommandEncoderWithDescriptor:"
- "replaceRegion:mipmapLevel:withBytes:bytesPerRow:"
- "result.convexHullExtent.has_value()"
- "result.orientedBoxExtent.has_value()"
- "setAlphaBlendOperation:"
- "setBinaryArchives:"
- "setBlendingEnabled:"
- "setBuffer:offset:atIndex:"
- "setBytes:length:atIndex:"
- "setClearColor:"
- "setClearDepth:"
- "setComputeFunction:"
- "setComputePipelineState:"
- "setCullMode:"
- "setDepthAttachmentPixelFormat:"
- "setDepthCompareFunction:"
- "setDepthStencilState:"
- "setDepthWriteEnabled:"
- "setDestinationAlphaBlendFactor:"
- "setDestinationRGBBlendFactor:"
- "setFragmentBuffer:offset:atIndex:"
- "setFragmentFunction:"
- "setFrontFacingWinding:"
- "setLabel:"
- "setLoadAction:"
- "setMagFilter:"
- "setMinFilter:"
- "setNormalizedCoordinates:"
- "setObject:forKeyedSubscript:"
- "setPixelFormat:"
- "setRAddressMode:"
- "setRasterSampleCount:"
- "setRenderPipelineState:"
- "setRenderTargetArrayLength:"
- "setRgbBlendOperation:"
- "setSAddressMode:"
- "setSamplerState:atIndex:"
- "setSourceAlphaBlendFactor:"
- "setSourceRGBBlendFactor:"
- "setStorageMode:"
- "setStoreAction:"
- "setTAddressMode:"
- "setTexture:"
- "setTexture:atIndex:"
- "setThreadGroupSizeIsMultipleOfThreadExecutionWidth:"
- "setTriangleFillMode:"
- "setUrl:"
- "setUsage:"
- "setVertexBuffer:offset:atIndex:"
- "setVertexBytes:length:atIndex:"
- "setVertexFunction:"
- "signalToNoiseRatios"
- "spotIds"
- "ss_res.planes.size() == ss_res.segment_image_extents.areas.size()"
- "ss_res.planes.size() == ss_res.segment_image_extents.boxes.size()"
- "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::cf::ErrorRef]"
- "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::con::Numbers]"
- "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::concurrency::ChannelOutput<std::experimental::expected<cv3d::recon::frame::KeyframeData, cv3d::kit::cf::ErrorRef>>]"
- "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::ValueData<cv3d::kit::con::Numbers>]"
- "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = std::experimental::expected<cv3d::recon::frame::KeyframeData, cv3d::kit::cf::ErrorRef> (const cv3d::esn::random::UUID &)]"
- "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = std::experimental::expected<cv3d::recon::frame::KeyframeData, cv3d::kit::cf::ErrorRef>]"
- "stringWithCString:encoding:"
- "stringWithUTF8String:"
- "sum.size() > 0"
- "supportsFamily:"
- "texture2DDescriptorWithPixelFormat:width:height:mipmapped:"
- "threadExecutionWidth"
- "top <= kMaxNodes"
- "tri_mesh_ptr != nullptr"
- "undistortedCameraPixels"
- "waitUntilCompleted"
- "waitUntilScheduled"
- "width"
- "writeToURL:atomically:"
- "{unexpected end after '"

```
