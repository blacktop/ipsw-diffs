## VisionCore

> `/System/Library/PrivateFrameworks/VisionCore.framework/VisionCore`

```diff

-9.0.53.0.0
+9.3.0.0.0
   __TEXT.__text: 0x2e8cc
   __TEXT.__auth_stubs: 0xed0
   __TEXT.__objc_methlist: 0x28ac

   __TEXT.__unwind_info: 0xfe8
   __TEXT.__objc_classname: 0xac6
   __TEXT.__objc_methname: 0x7aa0
-  __TEXT.__objc_methtype: 0x1c53
+  __TEXT.__objc_methtype: 0x1caf
   __TEXT.__objc_stubs: 0x4000
   __DATA_CONST.__got: 0x368
   __DATA_CONST.__const: 0x680

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 82DDDF63-5992-3577-B284-018107D7F0E8
+  UUID: D53DEBB2-495F-3DBC-8300-25CDE744261C
   Functions: 944
   Symbols:   3799
   CStrings:  2365
CStrings:
+ "@152@0:8{VisionCoreHomography={Geometry2D_cart2D=^f^fi}{Geometry2D_cart2D=^f^fi}{vector<float, std::allocator<float>>=^f^f{?=^f}}{vector<bool, std::allocator<bool>>=^QQ{?=Q}}{vector<float, std::allocator<float>>=^f^f{?=^f}}{_RANSAC_Parameters_=ifif}}16"
+ "@160@0:8@16{VisionCoreHomography={Geometry2D_cart2D=^f^fi}{Geometry2D_cart2D=^f^fi}{vector<float, std::allocator<float>>=^f^f{?=^f}}{vector<bool, std::allocator<bool>>=^QQ{?=Q}}{vector<float, std::allocator<float>>=^f^f{?=^f}}{_RANSAC_Parameters_=ifif}}24"
+ "i44@0:8i16{vector<int, std::allocator<int>>=^i^i{?=^i}}20"
+ "v40@0:8{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q{?=^Q}}16"
+ "{?=[3]}152@0:8{VisionCoreHomography={Geometry2D_cart2D=^f^fi}{Geometry2D_cart2D=^f^fi}{vector<float, std::allocator<float>>=^f^f{?=^f}}{vector<bool, std::allocator<bool>>=^QQ{?=Q}}{vector<float, std::allocator<float>>=^f^f{?=^f}}{_RANSAC_Parameters_=ifif}}16"
+ "{VisionCoreHomography={Geometry2D_cart2D=^f^fi}{Geometry2D_cart2D=^f^fi}{vector<float, std::allocator<float>>=^f^f{?=^f}}{vector<bool, std::allocator<bool>>=^QQ{?=Q}}{vector<float, std::allocator<float>>=^f^f{?=^f}}{_RANSAC_Parameters_=ifif}}36@0:8^v16^v24f32"
+ "{vector<VisionCoreHomography, std::allocator<VisionCoreHomography>>=^{VisionCoreHomography}^{VisionCoreHomography}{?=^{VisionCoreHomography}}}60@0:8^{__CVBuffer=}16B24@28^@36^v44@52"
+ "{vector<VisionCoreValueConfidencePoint, std::allocator<VisionCoreValueConfidencePoint>>=\"__begin_\"^{VisionCoreValueConfidencePoint}\"__end_\"^{VisionCoreValueConfidencePoint}\"\"{?=\"__cap_\"^{VisionCoreValueConfidencePoint}}}"
+ "{vector<__fp16, std::allocator<__fp16>>=\"__begin_\"^ \"__end_\"^ \"\"{?=\"__cap_\"^ }}"
+ "{vector<__fp16, std::allocator<__fp16>>=^ ^ {?=^ }}24@0:8f16i20"
+ "{vector<int, std::allocator<int>>=^i^i{?=^i}}32@0:8^v16^v24"
+ "{vector<long, std::allocator<long>>=\"__begin_\"^q\"__end_\"^q\"\"{?=\"__cap_\"^q}}"
+ "{vector<unsigned long, std::allocator<unsigned long>>=\"__begin_\"^Q\"__end_\"^Q\"\"{?=\"__cap_\"^Q}}"
- "@152@0:8{VisionCoreHomography={Geometry2D_cart2D=^f^fi}{Geometry2D_cart2D=^f^fi}{vector<float, std::allocator<float>>=^f^f^f}{vector<bool, std::allocator<bool>>=^QQQ}{vector<float, std::allocator<float>>=^f^f^f}{_RANSAC_Parameters_=ifif}}16"
- "@160@0:8@16{VisionCoreHomography={Geometry2D_cart2D=^f^fi}{Geometry2D_cart2D=^f^fi}{vector<float, std::allocator<float>>=^f^f^f}{vector<bool, std::allocator<bool>>=^QQQ}{vector<float, std::allocator<float>>=^f^f^f}{_RANSAC_Parameters_=ifif}}24"
- "i44@0:8i16{vector<int, std::allocator<int>>=^i^i^i}20"
- "v40@0:8{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q^Q}16"
- "{?=[3]}152@0:8{VisionCoreHomography={Geometry2D_cart2D=^f^fi}{Geometry2D_cart2D=^f^fi}{vector<float, std::allocator<float>>=^f^f^f}{vector<bool, std::allocator<bool>>=^QQQ}{vector<float, std::allocator<float>>=^f^f^f}{_RANSAC_Parameters_=ifif}}16"
- "{VisionCoreHomography={Geometry2D_cart2D=^f^fi}{Geometry2D_cart2D=^f^fi}{vector<float, std::allocator<float>>=^f^f^f}{vector<bool, std::allocator<bool>>=^QQQ}{vector<float, std::allocator<float>>=^f^f^f}{_RANSAC_Parameters_=ifif}}36@0:8^v16^v24f32"
- "{vector<VisionCoreHomography, std::allocator<VisionCoreHomography>>=^{VisionCoreHomography}^{VisionCoreHomography}^{VisionCoreHomography}}60@0:8^{__CVBuffer=}16B24@28^@36^v44@52"
- "{vector<VisionCoreValueConfidencePoint, std::allocator<VisionCoreValueConfidencePoint>>=\"__begin_\"^{VisionCoreValueConfidencePoint}\"__end_\"^{VisionCoreValueConfidencePoint}\"__cap_\"^{VisionCoreValueConfidencePoint}}"
- "{vector<__fp16, std::allocator<__fp16>>=\"__begin_\"^ \"__end_\"^ \"__cap_\"^ }"
- "{vector<__fp16, std::allocator<__fp16>>=^ ^ ^ }24@0:8f16i20"
- "{vector<int, std::allocator<int>>=^i^i^i}32@0:8^v16^v24"
- "{vector<long, std::allocator<long>>=\"__begin_\"^q\"__end_\"^q\"__cap_\"^q}"
- "{vector<unsigned long, std::allocator<unsigned long>>=\"__begin_\"^Q\"__end_\"^Q\"__cap_\"^Q}"

```
