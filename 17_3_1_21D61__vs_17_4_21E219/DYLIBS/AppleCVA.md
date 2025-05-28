## AppleCVA

> `/System/Library/PrivateFrameworks/AppleCVA.framework/AppleCVA`

```diff

-104.1.6.0.0
-  __TEXT.__text: 0xaab40
-  __TEXT.__auth_stubs: 0x19a0
+1000.2.4.0.0
+  __TEXT.__text: 0xbab3c
+  __TEXT.__auth_stubs: 0x19e0
   __TEXT.__objc_methlist: 0x44
-  __TEXT.__const: 0x34e0
-  __TEXT.__gcc_except_tab: 0x35b0
-  __TEXT.__cstring: 0x540d
-  __TEXT.__oslogstring: 0x70c0
-  __TEXT.__unwind_info: 0x1180
-  __TEXT.__objc_classname: 0x21
+  __TEXT.__gcc_except_tab: 0x3838
+  __TEXT.__const: 0x640
+  __TEXT.__cstring: 0x5541
+  __TEXT.__oslogstring: 0x7626
+  __TEXT.__unwind_info: 0x12b8
+  __TEXT.__objc_classname: 0x36
   __TEXT.__objc_methname: 0xc38
   __TEXT.__objc_methtype: 0xc7
   __TEXT.__objc_stubs: 0x1180
   __DATA_CONST.__got: 0x130
   __DATA_CONST.__const: 0xcf0
-  __DATA_CONST.__objc_classlist: 0x10
+  __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x138
+  __DATA_CONST.__objc_const: 0x1c8
   __DATA_CONST.__objc_selrefs: 0x468
+  __DATA_CONST.__objc_classrefs: 0xc0
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__cfstring: 0x3580
-  __AUTH_CONST.__const: 0x38
-  __AUTH_CONST.__objc_dictobj: 0x28
+  __AUTH_CONST.__cfstring: 0x3480
+  __AUTH_CONST.__const: 0x570
   __AUTH_CONST.__objc_const: 0x0
+  __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__auth_ptr: 0x40
-  __AUTH_CONST.__auth_got: 0xce0
-  __DATA.__objc_classrefs: 0xb8
+  __AUTH_CONST.__auth_got: 0xd00
+  __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x14
   __DATA.__data: 0x40
-  __DATA.__bss: 0x800
-  __DATA_DIRTY.__const: 0x2648
+  __DATA.__bss: 0x358
+  __DATA_DIRTY.__const: 0x1ac8
   __DATA_DIRTY.__objc_const: 0x90
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__data: 0x88

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1116
-  Symbols:   905
-  CStrings:  1705
+  Functions: 1238
+  Symbols:   901
+  CStrings:  1729
 
Symbols:
+ _CFDataGetBytePtr
+ _CGRectCreateDictionaryRepresentation
+ _CGRectZero
+ _CMTimeCopyAsDictionary
+ _CMTimeMake
+ _CVAFaceTrackingLiteGetOutput
+ __ZN3cva11ItemHandler11createValueIyEES0_RKT_
+ __ZN3cva11ItemHandler12createVectorIjEES0_RKNS_6MatrixIT_Lj0ELj1EXclsr6detailE7IsSmallIS3_XLj0EEXLj1EEEEEEE
+ __ZN3cva17DictionaryHandlerC1EOS0_
+ _kCVA_Q35DcgKuncOJWlqId9n8b3E1
+ _powf
+ _uuid_generate
+ _uuid_parse
+ _uuid_unparse_upper
- _CFArrayAppendValue
- _CFArrayCreate
- _CFArrayCreateMutable
- _CFUUIDCreate
- _CFUUIDCreateString
- _CVAFaceTrackingLiteEncodeOutput
- __ZNKSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strEv
- __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strERKNS_12basic_stringIcS2_S4_EE
- __ZTINSt3__113basic_istreamIcNS_11char_traitsIcEEEE
- __ZTINSt3__113basic_ostreamIcNS_11char_traitsIcEEEE
- __ZTINSt3__114basic_iostreamIcNS_11char_traitsIcEEEE
- __ZTINSt3__117__assoc_sub_stateE
- __ZTINSt3__119__shared_weak_countE
- __ZTVN10__cxxabiv119__pointer_type_infoE
- __ZTVN10__cxxabiv120__function_type_infoE
- __ZTVN10__cxxabiv121__vmi_class_type_infoE
- _kCFTypeArrayCallBacks
- _kCVAFaceTracking_TensorUUID
CStrings:
+ "%s: Cluster index %lu match -> adding point. Total points in cluster: %d"
+ "%s: No cluster match -> adding new cluster. Total cluster count: %lu"
+ "%s: No cluster representation. Adding first cluster."
+ "(%p uuid=%s)"
+ "(null)"
+ "/Library/Caches/com.apple.xbs/Sources/AppleCVA/shared/src/modules/avatar/facekit/facekitdictionaryconverter.cpp"
+ "Added tracked user %s with no faceprint to DB. New DB size %zu"
+ "AppleCVABundleFinder"
+ "CVAFaceTracking created (%p)."
+ "CVAFaceTrackingLite does not support recognition."
+ "CVAFaceTrackingLite supports color input only."
+ "Camera parameters dictionary missing or incomplete."
+ "Camera parameters size (%d, %d) does not match buffer size (%d, %d)."
+ "Creating FaceKit with *default* options (user has given no options)."
+ "Decreasing max distance for tracking to %f mm; due to previous error detected (user %s)."
+ "Depth camera dictionary is ignored when depth camera parameters are set from color camera."
+ "Excluding user %s from matches, they are currently being tracked"
+ "FaceKit processing failed"
+ "Failed to extract camera parameters from dictionary."
+ "Failed to extract color camera parameters from input dictionary."
+ "Failed to extract color data from the input dictionary."
+ "Failed to extract depth data from the input dictionary."
+ "Failed to set camera depth from color. Missing color camera parameters."
+ "Finalizing FaceTracking (%p)."
+ "Found match: recognized user %s, replacing user %s"
+ "I/O device"
+ "Incorrect scaled size. Expected size (%d, %d), actual size (%d, %d)."
+ "Increasing min distance for tracking to %f mm; due to previous error detected (user %s)."
+ "Invalid color buffer."
+ "Invalid depth or normalized disparity."
+ "Invalid disparity normalization multiplier %g"
+ "Invalid kCVA_Q35DcgKuncOJWlqId9n8b3E1: %f"
+ "Invalid pyramid behavior %d"
+ "Missing callback function."
+ "Missing color camera parameters."
+ "Missing color data."
+ "Missing face detections."
+ "Missing one or more normalized disparity parameters."
+ "Missing or invalid depth camera parameters."
+ "Original size (%d, %d) and target size (%d, %d) have different aspect ratio."
+ "Recorded distinct users %s and %s"
+ "Resetting due to face too close to camera (user %s)"
+ "Resetting due to face too far from camera (user %s)"
+ "Resetting due to too high angular acceleration (user %s)"
+ "Resetting due to too high angular velocity (user %s)"
+ "Resetting due to too high translational acceleration (user %s)"
+ "Resetting due to too high translational velocity (user %s)"
+ "Resetting due to too much rotation (user %s)"
+ "Resetting face due to ML failure coefficient (%g > %g, user %s)"
+ "Resetting face due to bounding box outside of the image (user %s)"
+ "Running without an image pyramid (pyramid behavior %d ignored)."
+ "Set network failure threshold to %f; due to previous error detected (user %s)."
+ "Skipping recognition due to ML failure coefficient (%g > %g, user %s)."
+ "Start initializing identity fitting."
+ "Transferred cluster information from user %s to %s. New cluster count: %lu."
+ "Unknown user, assigned new UUID %s. New DB size %zu. Closest mismatch %s, d=%f"
+ "Wait for identity fitting to finish initialization."
+ "cannot expand a non-owned data buffer."
+ "color or depth data missing"
+ "couldn't convert face rectangle dictionary"
+ "dictionary doesn't contain face detection keys"
+ "failed to initialize network resources."
+ "failed to initialize the identity fitting."
+ "failure reading tracking dictionary: invalid user_uuid"
+ "getUUID has been called on a FaceKitUser without an assigned UUID"
+ "invalid FaceKit input parameters"
+ "invalid facekit input parameters"
+ "kCVA_Q35DcgKuncOJWlqId9n8b3E1"
+ "n/a"
+ "not a valid format for processing, format 0x%x ('%s')"
+ "processSecondary called"
+ "request faceprint for user %s at (%.0f,%.0f), bbox size (%.0f,%.0f), pose=%s, isRepresented=%d"
+ "using pyramid behavior: %d"
+ "~FaceKitLiteScheduler"
- "225a1eb8-fe58-11ea-883b-00163e7c7c7c"
- "52AFE7DB-CB1F-433D-8A19-C9B16906AF9C"
- "Added new user. New DB SIZE %zu"
- "Added tracked user with no faceprint to DB. New DB SIZE %zu"
- "CVAFaceTracking created."
- "Cluster index %lu match -> adding point. Total points in cluster: %d"
- "Creating CVAFaceTracking."
- "Creating FaceKit with *defaults* options (user has given no options)."
- "Decreasing max distance for tracking to %f mm; due to previous error detected."
- "Depth source not specified - defaulting to Pearl"
- "Finalizing FaceTracking."
- "Height"
- "Increasing min distance for tracking to %f mm; due to previous error detected."
- "No cluster match -> adding new cluster. Total cluster count: %lu"
- "No cluster representation. Adding first cluster."
- "Resetting due to face too close to camera"
- "Resetting due to face too far from camera"
- "Resetting due to too high angular acceleration"
- "Resetting due to too high angular velocity"
- "Resetting due to too high translational acceleration"
- "Resetting due to too high translational velocity"
- "Resetting due to too much rotation"
- "Resetting face due to bounding box outside of the image"
- "Resetting face due to failure detection (%g) > (%g)"
- "Set network failure threshold to %f; due to previous error detected."
- "Skipping recognition: due to failure detection (%g) > (%g)."
- "Start initializing identity fitting thread."
- "Transferred user' cluster information. New cluster count: %lu."
- "Using resource folder %s"
- "Wait for identity fitting thread to finish initialization."
- "Width"
- "X"
- "Y"
- "cannot read fitting flag"
- "cannot set depth camera parameters from rgb"
- "depth camera parameters missing"
- "epoch"
- "face detections missing"
- "failed to allocate network resources."
- "failed to initialize the identity fitting thread."
- "flags"
- "invalid disparity normalization multiplier %g"
- "mismatching tensor model UUID"
- "missing rgb camera parameters"
- "not a valid rgb format for processing, format 0x%x ('%s')"
- "request faceprint for user UUID=%s, isRepresented=%d"
- "rgb camera parameters missing"
- "timescale"
- "unexpected tensor UUID."
- "using max pyramid levels: %d"
- "value"

```
