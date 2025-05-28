## AppleCV3D

> `/System/Library/PrivateFrameworks/AppleCV3D.framework/AppleCV3D`

```diff

-6.58.55.0.0
-  __TEXT.__text: 0x1bd3e28
+6.58.70.0.0
+  __TEXT.__text: 0x1bd3d14
   __TEXT.__auth_stubs: 0x31e0
   __TEXT.__init_offsets: 0x14
-  __TEXT.__const: 0x12f1ab
-  __TEXT.__gcc_except_tab: 0xf3904
-  __TEXT.__cstring: 0x86b5c
-  __TEXT.__oslogstring: 0xad97
-  __TEXT.__unwind_info: 0x3fa8c
+  __TEXT.__const: 0x12fa3b
+  __TEXT.__gcc_except_tab: 0xf3710
+  __TEXT.__cstring: 0x86952
+  __TEXT.__oslogstring: 0xae41
+  __TEXT.__unwind_info: 0x3fae4
   __TEXT.__eh_frame: 0xebc
   __TEXT.__objc_methname: 0x2fd
   __TEXT.__objc_stubs: 0x4a0
   __DATA_CONST.__got: 0x488
-  __DATA_CONST.__const: 0x1b78
+  __DATA_CONST.__const: 0x1be8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x128
   __DATA_CONST.__objc_classrefs: 0x68

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/librealtime_safety.dylib
-  Functions: 48994
+  Functions: 49002
   Symbols:   1787
-  CStrings:  10848
+  CStrings:  10862
 
CStrings:
+ " has a calibration for "
+ "!opt_camera_calib"
+ "CORRUPT"
+ "Failed to unsample SID: %llu with error: %s."
+ "Height must be between supported is 160 and 8192, configured dimension %lux%lu"
+ "J507"
+ "J508"
+ "J537"
+ "J538"
+ "J717"
+ "J718"
+ "J720"
+ "J721"
+ "Must have a radar link"
+ "Width must be between 160 and 640, configured dimension %lux%lu"
+ "[%s] was removed due to failing deserialization."
+ "cd.is_peridot_"
+ "config.IsValid()"
+ "rdar://117369109"
+ "rdar://117453278"
+ "rdar://117498781"
+ "rdar://117498850"
+ "rdar_link != \"\""
- "!ExactlyEqual(camera_matrix[0], 0.0) && ExactlyEqual(camera_matrix[1], 0.0) && !ExactlyEqual(camera_matrix[2], 0.0) && ExactlyEqual(camera_matrix[3], 0.0) && !ExactlyEqual(camera_matrix[4], 0.0) && !ExactlyEqual(camera_matrix[5], 0.0) && ExactlyEqual(camera_matrix[6], 0.0) && ExactlyEqual(camera_matrix[7], 0.0) && ExactlyEqual(camera_matrix[8], 1.0)"
- "Camera matrix must be a valid projection matrix."
- "Camera to IMU rotation must be a 3x3 orthogonal matrix."
- "Camera to IMU translation larger than device dimensions?"
- "Fail to add the edge to the graph"
- "Image dimensions must be strictly positive."
- "IsGaussianPyramidGeneratorConfigValid(config)"
- "IsKeyPointAndDescriptorGeneratorConfigValid(config)"
- "Max dimensions supported is 640x8192, configured dimension %lux%lu"
- "image_width > 0 && image_height > 0"
- "math::IsOrthogonal3x3(&camera_to_imu_rotation.front(), 1e-5)"
- "std::max(std::fabs(camera_to_imu_position[0]), std::max(std::fabs(camera_to_imu_position[1]), std::fabs(camera_to_imu_position[2]))) < 0.3"

```
