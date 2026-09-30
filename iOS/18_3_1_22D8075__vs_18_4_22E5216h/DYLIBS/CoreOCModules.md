## CoreOCModules

> `/System/Library/PrivateFrameworks/CoreOCModules.framework/CoreOCModules`

```diff

-10.12.0.0.0
-  __TEXT.__text: 0x6ecd4
-  __TEXT.__auth_stubs: 0x1140
-  __TEXT.__objc_methlist: 0xbc
-  __TEXT.__const: 0x4c14
-  __TEXT.__gcc_except_tab: 0x3244
-  __TEXT.__cstring: 0x4874
-  __TEXT.__oslogstring: 0x6a70
-  __TEXT.__unwind_info: 0x1020
+10.13.1.0.0
+  __TEXT.__text: 0x6c808
+  __TEXT.__auth_stubs: 0x1190
+  __TEXT.__objc_methlist: 0x1f4
+  __TEXT.__const: 0x4d44
+  __TEXT.__gcc_except_tab: 0x3330
+  __TEXT.__cstring: 0x487a
+  __TEXT.__oslogstring: 0x6d91
+  __TEXT.__unwind_info: 0x1018
+  __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0x56
-  __TEXT.__objc_methname: 0x124b
+  __TEXT.__objc_methname: 0x1272
   __TEXT.__objc_methtype: 0x1a7
-  __TEXT.__objc_stubs: 0x14c0
+  __TEXT.__objc_stubs: 0x1500
   __DATA_CONST.__got: 0x378
   __DATA_CONST.__const: 0x468
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x550
-  __AUTH_CONST.__auth_got: 0x8b8
+  __DATA_CONST.__objc_selrefs: 0x600
+  __AUTH_CONST.__auth_got: 0x8e0
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x1088
-  __AUTH_CONST.__cfstring: 0x1920
-  __AUTH_CONST.__objc_const: 0x510
+  __AUTH_CONST.__cfstring: 0x1940
+  __AUTH_CONST.__objc_const: 0x2d0
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 838
-  Symbols:   620
-  CStrings:  1013
+  Functions: 832
+  Symbols:   625
+  CStrings:  1024
 
Symbols:
+ _ARAdjustIntrincisForOrientation
+ _CFDictionaryGetValueIfPresent
+ _CFNumberGetTypeID
+ _acos
+ _objc_retain_x28
CStrings:
+ "%s:%{public}d Specified voxelHashingCapacity = %{public}u is insufficient/excessive to fill the bounding box with extents: [%{public}f, %{public}f, %{public}f], adjusted voxelHashingCapacity to %{public}u"
+ "2.0.0"
+ "HEIC Deserialization: Did not read object mask."
+ "HEIC Deserialization: Read HEIC version: %s"
+ "HEIC Deserialization: Read orientation: %d"
+ "HEIC Deserialization: Unbaking orientation=%d from camera matrices..."
+ "HEIC Serialization: Convert Coordinates unknown coordinate system!"
+ "HEIC Serialization: Convert Coordinates was already in correct coordinates."
+ "HEIC Serialization: Converting intrinsics and extrinsics into post-orientation camera coordinates per HEIC specification using orientation=%d"
+ "HEIC Serialization: NOT converting intrinsics and extrinsics into post-orientation camera coordinates since version requested to serialize is older than the version this was introduced!"
+ "HEIC Serialization: Updating in-place will bake orientation:%d into the camera extrinsics."
+ "Image Folder Reader: Found portrait effects matte. NOT using this as an object mask! Ignoring..."
+ "Will not bake orientation into camera transform since version %s isn't high enough!"
+ "cStringUsingEncoding:"
+ "compare:options:"
- "%s:%{public}d Specified voxelHashingCapacity = %{public}d is insufficient/excessive to fill the bounding box with extents: [%{public}f, %{public}f, %{public}f], adjusted voxelHashingCapacity to %{public}d"
- "HEIC Deserialization: Cannot read object mask."
- "HEIC Deserialization: Read HEIC version."
- "Image Folder Reader: Read object mask from deprecated key."

```
