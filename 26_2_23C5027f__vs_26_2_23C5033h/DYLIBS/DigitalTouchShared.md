## DigitalTouchShared

> `/System/Library/PrivateFrameworks/DigitalTouchShared.framework/DigitalTouchShared`

```diff

 577.0.0.0.0
-  __TEXT.__text: 0x2d1ec
+  __TEXT.__text: 0x2d200
   __TEXT.__auth_stubs: 0xcc0
   __TEXT.__objc_methlist: 0x3564
   __TEXT.__const: 0x3ac

   __TEXT.__oslogstring: 0x5bd
   __TEXT.__unwind_info: 0xf40
   __TEXT.__objc_classname: 0x34a
-  __TEXT.__objc_methname: 0x83ab
-  __TEXT.__objc_methtype: 0x13d1
+  __TEXT.__objc_methname: 0x83c7
+  __TEXT.__objc_methtype: 0x1407
   __TEXT.__objc_stubs: 0x6800
   __DATA_CONST.__got: 0x3f0
   __DATA_CONST.__const: 0xa18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0B359031-2F67-325A-8106-50801F912BD5
+  UUID: 7C36A002-5E87-34CC-9812-BE33C29847CA
   Functions: 1275
   Symbols:   4673
   CStrings:  2308
Functions:
~ __ZNSt3__16vectorINS0_IDv2_fNS_9allocatorIS1_EEEENS2_IS4_EEE11__vallocateB8ne200100Em : 76 -> 80
~ __ZNSt3__16vectorINS0_IDv2_fNS_9allocatorIS1_EEEENS2_IS4_EEE18__assign_with_sizeB8ne200100IPS4_S8_EEvT_T0_l : 376 -> 380
~ __ZNSt3__16vectorImNS_9allocatorImEEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorINS0_IDv2_fNS_9allocatorIS1_EEEENS2_IS4_EEE24__emplace_back_slow_pathIJRKS4_EEEPS4_DpOT_ : 304 -> 300
~ -[ETTapMessage initWithArchiveData:] : 1596 -> 1600
~ -[ETTapMessage addTapAtPoint:time:color:] : 880 -> 888
CStrings:
+ "T{vector<float __attribute__((ext_vector_type(2))), std::allocator<float __attribute__((ext_vector_type(2)))>>=^^{?=^}},N,V_controlBatches"
+ "T{vector<float __attribute__((ext_vector_type(2))), std::allocator<float __attribute__((ext_vector_type(2)))>>=^^{?=^}},N,V_controlPoints"
+ "T{vector<float __attribute__((ext_vector_type(2))), std::allocator<float __attribute__((ext_vector_type(2)))>>=^^{?=^}},N,V_points"
+ "T{vector<float __attribute__((ext_vector_type(2))), std::allocator<float __attribute__((ext_vector_type(2)))>>=^^{?=^}},N,V_prevPoints"
+ "T{vector<std::vector<float __attribute__((ext_vector_type(2)))>, std::allocator<std::vector<float __attribute__((ext_vector_type(2)))>>>=^v^v{?=^v}},N,V_vertexBatches"
+ "T{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q{?=^Q}},N,V_secondaryVertexBatchCount"
+ "T{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q{?=^Q}},N,V_vertexBatchCount"
+ "v40@0:8{vector<float __attribute__((ext_vector_type(2))), std::allocator<float __attribute__((ext_vector_type(2)))>>=^^{?=^}}16"
+ "v40@0:8{vector<std::vector<float __attribute__((ext_vector_type(2)))>, std::allocator<std::vector<float __attribute__((ext_vector_type(2)))>>>=^v^v{?=^v}}16"
+ "v40@0:8{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q{?=^Q}}16"
+ "{vector<CGPoint, std::allocator<CGPoint>>=\"__begin_\"^{CGPoint}\"__end_\"^{CGPoint}\"\"{?=\"__cap_\"^{CGPoint}}}"
+ "{vector<double, std::allocator<double>>=\"__begin_\"^d\"__end_\"^d\"\"{?=\"__cap_\"^d}}"
+ "{vector<float __attribute__((ext_vector_type(2))), std::allocator<float __attribute__((ext_vector_type(2)))>>=\"__begin_\"^\"__end_\"^\"\"{?=\"__cap_\"^}}"
+ "{vector<float __attribute__((ext_vector_type(2))), std::allocator<float __attribute__((ext_vector_type(2)))>>=^^{?=^}}16@0:8"
+ "{vector<std::vector<float __attribute__((ext_vector_type(2)))>, std::allocator<std::vector<float __attribute__((ext_vector_type(2)))>>>=\"__begin_\"^v\"__end_\"^v\"\"{?=\"__cap_\"^v}}"
+ "{vector<std::vector<float __attribute__((ext_vector_type(2)))>, std::allocator<std::vector<float __attribute__((ext_vector_type(2)))>>>=^v^v{?=^v}}16@0:8"
+ "{vector<unsigned long, std::allocator<unsigned long>>=\"__begin_\"^Q\"__end_\"^Q\"\"{?=\"__cap_\"^Q}}"
+ "{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q{?=^Q}}16@0:8"
- "T{vector<float __attribute__((ext_vector_type(2))), std::allocator<float __attribute__((ext_vector_type(2)))>>=^^^},N,V_controlBatches"
- "T{vector<float __attribute__((ext_vector_type(2))), std::allocator<float __attribute__((ext_vector_type(2)))>>=^^^},N,V_controlPoints"
- "T{vector<float __attribute__((ext_vector_type(2))), std::allocator<float __attribute__((ext_vector_type(2)))>>=^^^},N,V_points"
- "T{vector<float __attribute__((ext_vector_type(2))), std::allocator<float __attribute__((ext_vector_type(2)))>>=^^^},N,V_prevPoints"
- "T{vector<std::vector<float __attribute__((ext_vector_type(2)))>, std::allocator<std::vector<float __attribute__((ext_vector_type(2)))>>>=^v^v^v},N,V_vertexBatches"
- "T{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q^Q},N,V_secondaryVertexBatchCount"
- "T{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q^Q},N,V_vertexBatchCount"
- "v40@0:8{vector<float __attribute__((ext_vector_type(2))), std::allocator<float __attribute__((ext_vector_type(2)))>>=^^^}16"
- "v40@0:8{vector<std::vector<float __attribute__((ext_vector_type(2)))>, std::allocator<std::vector<float __attribute__((ext_vector_type(2)))>>>=^v^v^v}16"
- "v40@0:8{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q^Q}16"
- "{vector<CGPoint, std::allocator<CGPoint>>=\"__begin_\"^{CGPoint}\"__end_\"^{CGPoint}\"__cap_\"^{CGPoint}}"
- "{vector<double, std::allocator<double>>=\"__begin_\"^d\"__end_\"^d\"__cap_\"^d}"
- "{vector<float __attribute__((ext_vector_type(2))), std::allocator<float __attribute__((ext_vector_type(2)))>>=\"__begin_\"^\"__end_\"^\"__cap_\"^}"
- "{vector<float __attribute__((ext_vector_type(2))), std::allocator<float __attribute__((ext_vector_type(2)))>>=^^^}16@0:8"
- "{vector<std::vector<float __attribute__((ext_vector_type(2)))>, std::allocator<std::vector<float __attribute__((ext_vector_type(2)))>>>=\"__begin_\"^v\"__end_\"^v\"__cap_\"^v}"
- "{vector<std::vector<float __attribute__((ext_vector_type(2)))>, std::allocator<std::vector<float __attribute__((ext_vector_type(2)))>>>=^v^v^v}16@0:8"
- "{vector<unsigned long, std::allocator<unsigned long>>=\"__begin_\"^Q\"__end_\"^Q\"__cap_\"^Q}"
- "{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q^Q}16@0:8"

```
