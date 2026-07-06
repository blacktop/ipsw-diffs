## libARI.dylib

> `/usr/lib/libARI.dylib`

```diff

-  __TEXT.__text: 0x205c3c
+  __TEXT.__text: 0x2067d4
   __TEXT.__init_offsets: 0x8
-  __TEXT.__const: 0x151e0
-  __TEXT.__gcc_except_tab: 0x1aaa8
-  __TEXT.__cstring: 0x3e1e6
+  __TEXT.__const: 0x15290
+  __TEXT.__gcc_except_tab: 0x1ab20
+  __TEXT.__cstring: 0x3e32b
   __TEXT.__oslogstring: 0x4499
-  __TEXT.__unwind_info: 0xdb00
+  __TEXT.__unwind_info: 0xdb68
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0x464b0
+  __DATA_CONST.__const: 0x46698
   __DATA_CONST.__weak_got: 0x10
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x2a260
+  __AUTH_CONST.__const: 0x2a3b0
   __AUTH_CONST.__cfstring: 0x20
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__auth_got: 0x0

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 17182
-  Symbols:   32763
-  CStrings:  9446
+  Functions: 17218
+  Symbols:   32827
+  CStrings:  9459
 
Sections:
~ __DATA_CONST.__weak_got : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH.__data : content changed
Symbols:
+ GCC_except_table251
+ _ARI_IBICpsBBFeatureState_DEC_F
+ _ARI_IBICpsBBFeatureState_ENC_F
+ _ARI_IBICpsFeatureId_DEC_F
+ _ARI_IBICpsFeatureId_ENC_F
+ __Z8asString15IBICpsFeatureId
+ __Z8asString19IBICpsFeatureStatus
+ __ZL27ARI_IBICpsFeatureId_1_CODEC
+ __ZL32ARI_IBICpsBBFeatureState_1_CODEC
+ __ZN6AriSdk32ARI_IBICpsFeatureStatusIndCb_SDK4packEPP6AriMsg
+ __ZN6AriSdk32ARI_IBICpsFeatureStatusIndCb_SDK6unpackEv
+ __ZN6AriSdk32ARI_IBICpsFeatureStatusIndCb_SDKC1EPKhj
+ __ZN6AriSdk32ARI_IBICpsFeatureStatusIndCb_SDKC1Ev
+ __ZN6AriSdk32ARI_IBICpsFeatureStatusIndCb_SDKC2EPKhj
+ __ZN6AriSdk32ARI_IBICpsFeatureStatusIndCb_SDKC2Ev
+ __ZN6AriSdk32ARI_IBICpsFeatureStatusIndCb_SDKD0Ev
+ __ZN6AriSdk32ARI_IBICpsFeatureStatusIndCb_SDKD1Ev
+ __ZN6AriSdk32ARI_IBICpsFeatureStatusIndCb_SDKD2Ev
+ __ZN6AriSdk33ARI_IBICpsGetFeatureStatusReq_SDK4packEPP6AriMsg
+ __ZN6AriSdk33ARI_IBICpsGetFeatureStatusReq_SDK6unpackEv
+ __ZN6AriSdk33ARI_IBICpsGetFeatureStatusReq_SDKC1EPKhj
+ __ZN6AriSdk33ARI_IBICpsGetFeatureStatusReq_SDKC1Ev
+ __ZN6AriSdk33ARI_IBICpsGetFeatureStatusReq_SDKC2EPKhj
+ __ZN6AriSdk33ARI_IBICpsGetFeatureStatusReq_SDKC2Ev
+ __ZN6AriSdk33ARI_IBICpsGetFeatureStatusReq_SDKD0Ev
+ __ZN6AriSdk33ARI_IBICpsGetFeatureStatusReq_SDKD1Ev
+ __ZN6AriSdk33ARI_IBICpsGetFeatureStatusReq_SDKD2Ev
+ __ZN6AriSdk35ARI_IBICpsGetFeatureStatusRspCb_SDK4packEPP6AriMsg
+ __ZN6AriSdk35ARI_IBICpsGetFeatureStatusRspCb_SDK6unpackEv
+ __ZN6AriSdk35ARI_IBICpsGetFeatureStatusRspCb_SDKC1EPKhj
+ __ZN6AriSdk35ARI_IBICpsGetFeatureStatusRspCb_SDKC1Ev
+ __ZN6AriSdk35ARI_IBICpsGetFeatureStatusRspCb_SDKC2EPKhj
+ __ZN6AriSdk35ARI_IBICpsGetFeatureStatusRspCb_SDKC2Ev
+ __ZN6AriSdk35ARI_IBICpsGetFeatureStatusRspCb_SDKD0Ev
+ __ZN6AriSdk35ARI_IBICpsGetFeatureStatusRspCb_SDKD1Ev
+ __ZN6AriSdk35ARI_IBICpsGetFeatureStatusRspCb_SDKD2Ev
+ __ZN6AriSdk3TlvI20IBICpsBBFeatureStateEaSIRS1_vEERS2_OT_
+ __ZNK6AriSdk32ARI_IBICpsFeatureStatusIndCb_SDK15hasDeclaredGmidEv
+ __ZNK6AriSdk33ARI_IBICpsGetFeatureStatusReq_SDK15hasDeclaredGmidEv
+ __ZNK6AriSdk35ARI_IBICpsGetFeatureStatusRspCb_SDK15hasDeclaredGmidEv
+ __ZTIN6AriSdk32ARI_IBICpsFeatureStatusIndCb_SDKE
+ __ZTIN6AriSdk33ARI_IBICpsGetFeatureStatusReq_SDKE
+ __ZTIN6AriSdk35ARI_IBICpsGetFeatureStatusRspCb_SDKE
+ __ZTSN6AriSdk32ARI_IBICpsFeatureStatusIndCb_SDKE
+ __ZTSN6AriSdk33ARI_IBICpsGetFeatureStatusReq_SDKE
+ __ZTSN6AriSdk35ARI_IBICpsGetFeatureStatusRspCb_SDKE
+ __ZTVN6AriSdk32ARI_IBICpsFeatureStatusIndCb_SDKE
+ __ZTVN6AriSdk33ARI_IBICpsGetFeatureStatusReq_SDKE
+ __ZTVN6AriSdk35ARI_IBICpsGetFeatureStatusRspCb_SDKE
- GCC_except_table241
- GCC_except_table261
- GCC_except_table271
CStrings:
+ "IBICpsBBFeatureState"
+ "IBICpsFeatureId"
+ "IBICpsFeatureStatusIndCb"
+ "IBICpsGetFeatureStatusReq"
+ "IBICpsGetFeatureStatusRspCb"
+ "IBI_CPS_FEATURE_STATUS_DISABLED"
+ "IBI_CPS_FEATURE_STATUS_ENABLED"
+ "IBI_CPS_FEATURE_STATUS_UNKNOWN"
+ "IBI_CPS_FEATURE_TAR"
+ "IBI_NC_RESULT_NOT_ENOUGH_MEMORY_FOR_NEW_BCOM"
+ "feature_id_t3"
+ "feature_status_t2"
+ "feature_status_t3"

```
