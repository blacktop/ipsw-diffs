## CoreOCModules

> `/System/Library/PrivateFrameworks/CoreOCModules.framework/Versions/A/CoreOCModules`

```diff

-10.12.0.0.0
-  __TEXT.__text: 0x70d70
-  __TEXT.__auth_stubs: 0xee0
-  __TEXT.__objc_methlist: 0xbc
-  __TEXT.__const: 0x4c00
-  __TEXT.__gcc_except_tab: 0x32b8
-  __TEXT.__cstring: 0x483a
-  __TEXT.__oslogstring: 0x699f
-  __TEXT.__unwind_info: 0x1028
+10.13.1.0.0
+  __TEXT.__text: 0x6e8ec
+  __TEXT.__auth_stubs: 0xf20
+  __TEXT.__objc_methlist: 0x1f4
+  __TEXT.__const: 0x4d10
+  __TEXT.__gcc_except_tab: 0x3394
+  __TEXT.__cstring: 0x48a4
+  __TEXT.__oslogstring: 0x6cc0
+  __TEXT.__unwind_info: 0x1030
+  __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0x56
-  __TEXT.__objc_methname: 0x1235
+  __TEXT.__objc_methname: 0x125c
   __TEXT.__objc_methtype: 0x1a7
-  __TEXT.__objc_stubs: 0x1480
+  __TEXT.__objc_stubs: 0x14c0
   __DATA_CONST.__got: 0x350
   __DATA_CONST.__const: 0x3c8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x540
-  __AUTH_CONST.__auth_got: 0x788
+  __DATA_CONST.__objc_selrefs: 0x5f0
+  __AUTH_CONST.__auth_got: 0x7a8
   __AUTH_CONST.__const: 0x1140
-  __AUTH_CONST.__cfstring: 0x1960
-  __AUTH_CONST.__objc_const: 0x510
+  __AUTH_CONST.__cfstring: 0x1980
+  __AUTH_CONST.__objc_const: 0x2d0
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 96711932-5272-3ADC-81AA-7EB4CA0C7D47
-  Functions: 843
-  Symbols:   588
-  CStrings:  1207
+  UUID: 3C881480-63B4-3BEE-8E67-AE2EFE36BD06
+  Functions: 839
+  Symbols:   592
+  CStrings:  1221
 
Symbols:
+ _CFDictionaryGetValueIfPresent
+ _CFNumberGetTypeID
+ __ZNSt3__122__libcpp_verbose_abortEPKcz
+ _acos
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
+ "bad_function_call was thrown in -fno-exceptions mode"
+ "cStringUsingEncoding:"
+ "compare:options:"
+ "regex_error was thrown in -fno-exceptions mode"
- "%s:%{public}d Specified voxelHashingCapacity = %{public}d is insufficient/excessive to fill the bounding box with extents: [%{public}f, %{public}f, %{public}f], adjusted voxelHashingCapacity to %{public}d"
- "HEIC Deserialization: Cannot read object mask."
- "HEIC Deserialization: Read HEIC version."
- "Image Folder Reader: Read object mask from deprecated key."

```
