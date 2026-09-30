## AudioServerDriverTransports_IOA2

> `/System/Library/PrivateFrameworks/AudioServerDriverTransports_IOA2.framework/AudioServerDriverTransports_IOA2`

```diff

-320.1.0.0.0
-  __TEXT.__text: 0x1e9e0
+320.2.0.0.0
+  __TEXT.__text: 0x1ea1c
   __TEXT.__auth_stubs: 0xac0
   __TEXT.__objc_methlist: 0x11a4
   __TEXT.__gcc_except_tab: 0x40f8

   __TEXT.__unwind_info: 0x11c8
   __TEXT.__objc_classname: 0x218
   __TEXT.__objc_methname: 0x28bf
-  __TEXT.__objc_methtype: 0x103c
+  __TEXT.__objc_methtype: 0x1064
   __TEXT.__objc_stubs: 0x2260
   __DATA_CONST.__got: 0x1f8
   __DATA_CONST.__const: 0x238

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0B04F6A2-CA9A-34EA-ADF8-E9BA7515A55F
+  UUID: D40CB9B8-0C7C-3929-A039-C57E3ED200B3
   Functions: 677
   Symbols:   2354
   CStrings:  1027
Functions:
~ __ZNSt3__16vectorIjNS_9allocatorIjEEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZN10applesauce2CF7details20make_CFDictionaryRefINS0_9StringRefENS0_7TypeRefEEEDaRKNSt3__13mapIT_T0_NS6_4lessIS8_EENS6_9allocatorINS6_4pairIKS8_S9_EEEEEE : 280 -> 284
~ __ZNSt3__16vectorIN10applesauce2CF11TypeRefPairENS_9allocatorIS3_EEE7reserveEm : 188 -> 204
~ __ZN10applesauce2CF7details20make_CFDictionaryRefERKNSt3__16vectorINS0_11TypeRefPairENS2_9allocatorIS4_EEEE : 776 -> 792
~ __ZNSt3__16vectorIN10applesauce2CF11TypeRefPairENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRKNS2_9StringRefERKNS2_7TypeRefEEEEPS3_DpOT_ : 284 -> 296
~ __ZN10applesauce2CF7details15make_CFArrayRefIjEEDaRKNSt3__16vectorIT_NS4_9allocatorIS6_EEEENS1_15counterpart_tagE : 416 -> 420
~ __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE11__vallocateB8ne200100Em : 60 -> 64
CStrings:
+ "{VolumeCurve=\"mTag\"I\"mCurveMap\"{map<ASDT::RawPoint, ASDT::DBPoint, std::less<ASDT::RawPoint>, std::allocator<std::pair<const ASDT::RawPoint, ASDT::DBPoint>>>=\"__tree_\"{__tree<std::__value_type<ASDT::RawPoint, ASDT::DBPoint>, std::__map_value_compare<ASDT::RawPoint, std::__value_type<ASDT::RawPoint, ASDT::DBPoint>, std::less<ASDT::RawPoint>>, std::allocator<std::__value_type<ASDT::RawPoint, ASDT::DBPoint>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}\"mIsApplyingTransferFunction\"B\"mTransferFunction\"I\"mRawToScalarExponentNumerator\"f\"mRawToScalarExponentDenominator\"f}"
+ "{VolumeCurve=I{map<ASDT::RawPoint, ASDT::DBPoint, std::less<ASDT::RawPoint>, std::allocator<std::pair<const ASDT::RawPoint, ASDT::DBPoint>>>={__tree<std::__value_type<ASDT::RawPoint, ASDT::DBPoint>, std::__map_value_compare<ASDT::RawPoint, std::__value_type<ASDT::RawPoint, ASDT::DBPoint>, std::less<ASDT::RawPoint>>, std::allocator<std::__value_type<ASDT::RawPoint, ASDT::DBPoint>>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}}BIff}24@0:8@16"
+ "{unique_ptr<ASDT::Exclaves::StatusTracker, std::default_delete<ASDT::Exclaves::StatusTracker>>=\"\"{?=\"__ptr_\"^{StatusTracker}}}"
+ "{unique_ptr<ASDT::IOA2UserClient, std::default_delete<ASDT::IOA2UserClient>>=\"\"{?=\"__ptr_\"^{IOA2UserClient}}}"
+ "{unique_ptr<ASDT::IOA2UserClient, std::default_delete<ASDT::IOA2UserClient>>={?=^{IOA2UserClient}}}20@0:8I16"
+ "{unique_ptr<ASDT::MachPort, std::default_delete<ASDT::MachPort>>={?=^{MachPort}}}16@0:8"
- "{VolumeCurve=\"mTag\"I\"mCurveMap\"{map<ASDT::RawPoint, ASDT::DBPoint, std::less<ASDT::RawPoint>, std::allocator<std::pair<const ASDT::RawPoint, ASDT::DBPoint>>>=\"__tree_\"{__tree<std::__value_type<ASDT::RawPoint, ASDT::DBPoint>, std::__map_value_compare<ASDT::RawPoint, std::__value_type<ASDT::RawPoint, ASDT::DBPoint>, std::less<ASDT::RawPoint>>, std::allocator<std::__value_type<ASDT::RawPoint, ASDT::DBPoint>>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}\"mIsApplyingTransferFunction\"B\"mTransferFunction\"I\"mRawToScalarExponentNumerator\"f\"mRawToScalarExponentDenominator\"f}"
- "{VolumeCurve=I{map<ASDT::RawPoint, ASDT::DBPoint, std::less<ASDT::RawPoint>, std::allocator<std::pair<const ASDT::RawPoint, ASDT::DBPoint>>>={__tree<std::__value_type<ASDT::RawPoint, ASDT::DBPoint>, std::__map_value_compare<ASDT::RawPoint, std::__value_type<ASDT::RawPoint, ASDT::DBPoint>, std::less<ASDT::RawPoint>>, std::allocator<std::__value_type<ASDT::RawPoint, ASDT::DBPoint>>>=^v{__tree_end_node<std::__tree_node_base<void *> *>=^v}Q}}BIff}24@0:8@16"
- "{unique_ptr<ASDT::Exclaves::StatusTracker, std::default_delete<ASDT::Exclaves::StatusTracker>>=\"__ptr_\"^{StatusTracker}}"
- "{unique_ptr<ASDT::IOA2UserClient, std::default_delete<ASDT::IOA2UserClient>>=\"__ptr_\"^{IOA2UserClient}}"
- "{unique_ptr<ASDT::IOA2UserClient, std::default_delete<ASDT::IOA2UserClient>>=^{IOA2UserClient}}20@0:8I16"
- "{unique_ptr<ASDT::MachPort, std::default_delete<ASDT::MachPort>>=^{MachPort}}16@0:8"

```
