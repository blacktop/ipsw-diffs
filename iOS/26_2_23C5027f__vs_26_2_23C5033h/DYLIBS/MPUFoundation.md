## MPUFoundation

> `/System/Library/PrivateFrameworks/MPUFoundation.framework/MPUFoundation`

```diff

 4025.100.2.0.0
-  __TEXT.__text: 0x18e0c
+  __TEXT.__text: 0x18e1c
   __TEXT.__auth_stubs: 0x830
   __TEXT.__objc_methlist: 0x22a4
   __TEXT.__cstring: 0xc90

   __TEXT.__unwind_info: 0x950
   __TEXT.__objc_classname: 0x4da
   __TEXT.__objc_methname: 0x6395
-  __TEXT.__objc_methtype: 0x126c
+  __TEXT.__objc_methtype: 0x1276
   __TEXT.__objc_stubs: 0x42a0
   __DATA_CONST.__got: 0x518
   __DATA_CONST.__const: 0x458

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: 89749593-F667-3C54-84DC-DE40000422FF
+  UUID: DE4AC9C7-A294-33F1-B03E-D2D4643D90F9
   Functions: 770
   Symbols:   2998
   CStrings:  1592
Functions:
~ __ZNSt3__16vectorIN3MPU18LayoutInterpolator16EntriesContainerENS_9allocatorIS3_EEE18__assign_with_sizeB8ne200100IPS3_S8_EEvT_T0_l : 328 -> 332
~ __ZNSt3__16vectorIN3MPU18LayoutInterpolator16EntriesContainerENS_9allocatorIS3_EEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorIN3MPU18LayoutInterpolator5EntryENS_9allocatorIS3_EEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorIN3MPU18LayoutInterpolator16EntriesContainerENS_9allocatorIS3_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS3_RS5_EEPS3_ : 188 -> 192
CStrings:
+ "{vector<MPU::LayoutInterpolator::EntriesContainer, std::allocator<MPU::LayoutInterpolator::EntriesContainer>>=\"__begin_\"^{EntriesContainer}\"__end_\"^{EntriesContainer}\"\"{?=\"__cap_\"^{EntriesContainer}}}"
+ "{vector<MPU::Point3D, std::allocator<MPU::Point3D>>=^{Point3D}^{Point3D}{?=^{Point3D}}}56@0:8^v16{Point3D=ddd}24d48"
- "{vector<MPU::LayoutInterpolator::EntriesContainer, std::allocator<MPU::LayoutInterpolator::EntriesContainer>>=\"__begin_\"^{EntriesContainer}\"__end_\"^{EntriesContainer}\"__cap_\"^{EntriesContainer}}"
- "{vector<MPU::Point3D, std::allocator<MPU::Point3D>>=^{Point3D}^{Point3D}^{Point3D}}56@0:8^v16{Point3D=ddd}24d48"

```
