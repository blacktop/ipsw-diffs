## Recon3D

> `/System/Library/PrivateFrameworks/Recon3D.framework/Recon3D`

```diff

-8.25.6.11.2
-  __TEXT.__text: 0x175f6dc
-  __TEXT.__auth_stubs: 0x2620
-  __TEXT.__const: 0x1127f0
-  __TEXT.__cstring: 0x4374c
-  __TEXT.__gcc_except_tab: 0xeb6d8
-  __TEXT.__oslogstring: 0x77db
-  __TEXT.__unwind_info: 0x32e70
-  __TEXT.__eh_frame: 0x9b8
+8.25.6.25.0
+  __TEXT.__text: 0x187bae8
+  __TEXT.__auth_stubs: 0x2720
+  __TEXT.__const: 0x113a30
+  __TEXT.__cstring: 0x43f6f
+  __TEXT.__gcc_except_tab: 0xecc8c
+  __TEXT.__oslogstring: 0x7b3a
+  __TEXT.__unwind_info: 0x33960
+  __TEXT.__eh_frame: 0x14a4
   __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0xc19
   __TEXT.__objc_stubs: 0x1080

   __DATA_CONST.__const: 0x1ca8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x420
-  __AUTH_CONST.__auth_got: 0x1320
-  __AUTH_CONST.__const: 0x5cbe8
+  __AUTH_CONST.__auth_got: 0x13a0
+  __AUTH_CONST.__const: 0x5d960
   __AUTH_CONST.__cfstring: 0x280
   __AUTH.__data: 0x8
   __AUTH.__thread_vars: 0x48
   __AUTH.__thread_bss: 0x38
-  __DATA.__data: 0x5600
+  __DATA.__data: 0x55e0
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x248
   __DATA.__common: 0x798
   __DATA_DIRTY.__data: 0x68
-  __DATA_DIRTY.__bss: 0x3af0
+  __DATA_DIRTY.__bss: 0x3ba0
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A803EC9A-657D-32F0-9D59-C2EA4AD6FC09
-  Functions: 35407
-  Symbols:   1721
-  CStrings:  7146
+  UUID: 7A9C253D-802B-3320-B3CF-F4E671289BEC
+  Functions: 36763
+  Symbols:   1737
+  CStrings:  7220
 
Symbols:
+ _BLASStateRelease
+ _BLASStateRetain
+ _acos
+ _asin
+ _cblas_dcopy
+ _cblas_ddot
+ _cblas_dgemm
+ _cblas_dgemv
+ _cblas_dscal
+ _cblas_dsyrk$NEWLAPACK
+ _cblas_dtrsm
+ _cblas_dtrsv
+ _dpotrs$NEWLAPACK
+ _malloc_type_aligned_alloc
+ _memset_pattern8
+ _xerbla_
CStrings:
+ " (with port in [0,65535]) but is '"
+ " < "
+ "%s: Config string contains more than one file path; first path: '%s'; following path '%s' ignored"
+ "%s: Config string contains more than one server address; first address: '%s'; following address '%s' ignored"
+ "%s: Enabling log contexts: %s"
+ "%s: Failed to start logging to file at '%s': %s"
+ "%s: Failed to start logging to file at '%s': another file exporter already exists at the same location"
+ "%s: Failed to start logging via network to server at '%s' : %s"
+ "%s: Invalid config string '%s': %s"
+ "%s: Not enabling any log contexts"
+ "%s: Not enabling any log contexts since logger has no destinations"
+ "%s: Starting logging to file at '%s'"
+ "%s: Starting logging via network to server at '%s'"
+ "%s: Stopping logging to file at '%s'"
+ "%s: Stopping logging via network"
+ "'host:port'"
+ "'host[:port]'"
+ ",;"
+ "->"
+ "/AppleInternal/Library/BuildRoots/4~B5T_ugAhTXpTY2UEIQ9N1iVvcfIq0umlL5sQCYU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/has_self_intersections.hpp"
+ "/AppleInternal/Library/BuildRoots/4~B5T_ugAhTXpTY2UEIQ9N1iVvcfIq0umlL5sQCYU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/overlay/add_rings.hpp"
+ "/AppleInternal/Library/BuildRoots/4~B5T_ugAhTXpTY2UEIQ9N1iVvcfIq0umlL5sQCYU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/overlay/get_turn_info_la.hpp"
+ "/AppleInternal/Library/BuildRoots/4~B5T_ugAhTXpTY2UEIQ9N1iVvcfIq0umlL5sQCYU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/boost/rational.hpp"
+ "/Library/Caches/com.apple.xbs/Sources/Recon3D/library/Reconstruction/SceneQuery/src/SurfaceRefinement.cpp"
+ ": failed a TimeframeSync: "
+ "CameraPose"
+ "Convergence in the cost: "
+ "Convergence in the gradient"
+ "Convergence in the parameters"
+ "DPOTRF"
+ "DPOTRF2"
+ "DenseHessian"
+ "KFE:CCK:TC:%zu, SC:%zu, KLM:%zu"
+ "LevenbergMarquardt"
+ "Linearize FAILED"
+ "M cannot be less than zero; it is set to %d."
+ "N cannot be less than zero; it is set to %d."
+ "N.A."
+ "NaN"
+ "Normal was flipped during SR, returning initial estimate"
+ "Order must be %d or %d, but is set to %d"
+ "POTRF"
+ "PlaneRefinement: Using %zu points from %zu keyframes"
+ "PlaneRefinement: Using %zu points from %zu keyframes %f %f"
+ "PlaneRefinement: Was able to fit a plane Angular deviation %f deg. #points: %zu from #keyframes: %zu normal: %f, %f, %f"
+ "PointCloud"
+ "RegionGraph"
+ "SIDE must be %d or %d, but is set to %d"
+ "Solve FAILED"
+ "TransA must be %d, %d or %d, but is set to %d"
+ "UPLO must be %d or %d, but is set to %d"
+ "UUID does not exist in state"
+ "Unable to refine plane"
+ "Update norm is too large. Skip it."
+ "[error][grad < gtol]["
+ "[iter][old->new][delta < ptol][grad < gtol][delta < ctol]["
+ "[iter][old->new][delta < ptol][grad < gtol][delta < ctol][lambda]["
+ "]["
+ "acv::SurfaceDetectionVisualLogging"
+ "candidate_kfs"
+ "cblas_dgemm"
+ "cblas_dgemv"
+ "cblas_dscal_sequential"
+ "cblas_dtrsm"
+ "collection.points.size() == collection.point_to_keyframe.size()"
+ "given tcp address must be of pattern "
+ "lda must be >= MAX(M,1): lda=%d M=%d"
+ "lda must be >= MAX(N,1): lda=%d N=%d"
+ "ldb must be >= MAX(M,1): ldb=%d M=%d"
+ "ldb must be >= MAX(N,1): ldb=%d N=%d"
+ "normalsRGB"
+ "semanticsRGB"
+ "visible_voxels"
- "/AppleInternal/Library/BuildRoots/4~B4EsugBK_KRV2-6lw5c7O1wY58qLA8XLrOdS5MI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/has_self_intersections.hpp"
- "/AppleInternal/Library/BuildRoots/4~B4EsugBK_KRV2-6lw5c7O1wY58qLA8XLrOdS5MI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/overlay/add_rings.hpp"
- "/AppleInternal/Library/BuildRoots/4~B4EsugBK_KRV2-6lw5c7O1wY58qLA8XLrOdS5MI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/overlay/get_turn_info_la.hpp"
- "/AppleInternal/Library/BuildRoots/4~B4EsugBK_KRV2-6lw5c7O1wY58qLA8XLrOdS5MI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/boost/rational.hpp"
- "Connecting to VisualLogger %s"
- "File logger not initialized: %s"
- "Initializing FileLogger %s"
- "KFE:CCK:TC:%zu, SC:%zu"
- "PlaneRefinement: Was able to fit a plane Angular deviation %f deg. inliers: %zu total: %zu"
- "UUID doesnt exist in state"
- "Unable to fit a plane to ransac inliers"
- "Unable to fit a ransac plane"

```
