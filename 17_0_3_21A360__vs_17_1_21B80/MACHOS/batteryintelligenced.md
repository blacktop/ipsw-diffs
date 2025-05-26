## batteryintelligenced

> `/usr/libexec/batteryintelligenced`

```diff

-29.0.0.0.0
-  __TEXT.__text: 0xf79c
+31.0.0.0.0
+  __TEXT.__text: 0xf7fc
   __TEXT.__auth_stubs: 0x540
   __TEXT.__objc_stubs: 0x18e0
   __TEXT.__objc_methlist: 0x1264
-  __TEXT.__objc_methname: 0x1b94
-  __TEXT.__oslogstring: 0x1097
-  __TEXT.__cstring: 0x856
+  __TEXT.__objc_methname: 0x1c4c
+  __TEXT.__oslogstring: 0x1145
+  __TEXT.__cstring: 0x879
   __TEXT.__objc_classname: 0x138
   __TEXT.__objc_methtype: 0x3d7
-  __TEXT.__const: 0x60
+  __TEXT.__const: 0x58
   __TEXT.__gcc_except_tab: 0xd0
-  __TEXT.__unwind_info: 0x2ac
+  __TEXT.__unwind_info: 0x2b0
   __DATA_CONST.__auth_got: 0x2b0
   __DATA_CONST.__got: 0x80
   __DATA_CONST.__const: 0x418

   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 533
+  Functions: 531
   Symbols:   141
-  CStrings:  738
+  CStrings:  739
 
CStrings:
+ "Computing the median values over the follow arrays NCCp:%@ WRa:%@ QMaxp%@"
+ "Could not get model predictions for %@ for %@"
+ "Fetching data for stream %@ in range %@ - %@"
+ "Fetching data from %@ stream in range %@ - %@"
+ "Fetching past predictions in range %@ - %@"
+ "Manufacture date %@ isValid:%d. Estimated age: %f"
+ "Resampling BDC_SBC data"
+ "Running inference for model %@ for prediction duration = %@ days"
+ "Td,N,V_age_estimate"
+ "Td,N,V_elapsed_days"
+ "Td,N,V_hist_end_cycles"
+ "Td,N,V_hist_end_nccp"
+ "Td,N,V_hist_end_qmaxp"
+ "Td,N,V_hist_end_wra"
+ "Td,N,V_target_delta_nccp"
+ "Td,N,V_target_delta_qmaxp"
+ "Td,N,V_target_delta_wra"
+ "_age_estimate"
+ "_elapsed_days"
+ "_hist_end_cycles"
+ "_hist_end_nccp"
+ "_hist_end_qmaxp"
+ "_hist_end_wra"
+ "_target_delta_nccp"
+ "_target_delta_qmaxp"
+ "_target_delta_wra"
+ "age_estimate"
+ "elapsed_days"
+ "hist_end_cycles"
+ "hist_end_nccp"
+ "hist_end_qmaxp"
+ "hist_end_wra"
+ "initWithLT_5c:_5c:_4c:_3c:_2c:_1c:_0c:_1c_1:_2c_1:_3c_1:_4c_1:GT5c:_0s:_10s:_20s:_30s:_40s:_50s:_60s:_70s:_80s:_90s:LT20t:_20t:_22t:_24t:_26t:_28t:_30t:_32t:_34t:_36t:_38t:GT40t:hist_end_cycles:age_estimate:elapsed_days:hist_end_nccp:hist_end_wra:hist_end_qmaxp:"
+ "initWithTarget_delta_nccp:"
+ "initWithTarget_delta_qmaxp:"
+ "initWithTarget_delta_wra:"
+ "predictionFromLT_5c:_5c:_4c:_3c:_2c:_1c:_0c:_1c_1:_2c_1:_3c_1:_4c_1:GT5c:_0s:_10s:_20s:_30s:_40s:_50s:_60s:_70s:_80s:_90s:LT20t:_20t:_22t:_24t:_26t:_28t:_30t:_32t:_34t:_36t:_38t:GT40t:hist_end_cycles:age_estimate:elapsed_days:hist_end_nccp:hist_end_wra:hist_end_qmaxp:error:"
+ "setAge_estimate:"
+ "setElapsed_days:"
+ "setHist_end_cycles:"
+ "setHist_end_nccp:"
+ "setHist_end_qmaxp:"
+ "setHist_end_wra:"
+ "setTarget_delta_nccp:"
+ "setTarget_delta_qmaxp:"
+ "setTarget_delta_wra:"
+ "target_delta_nccp"
+ "target_delta_qmaxp"
+ "target_delta_wra"
- "Arrays NCCp:%@ WRa:%@ QMaxp%@"
- "Could not get model predictions for %@"
- "Date %@ isValid:%d"
- "Fetching data in range %@ - %@"
- "Fetching date in range %@ - %@"
- "Fetching predictions in range %@ - %@"
- "Running inference for model %@"
- "Td,N,V_delta_nccp"
- "Td,N,V_delta_qmaxp"
- "Td,N,V_delta_wra"
- "Td,N,V_elapsed_years"
- "Td,N,V_start_age"
- "Td,N,V_start_cycles"
- "Td,N,V_start_nccp"
- "Td,N,V_start_qmaxp"
- "Td,N,V_start_wra"
- "_delta_nccp"
- "_delta_qmaxp"
- "_delta_wra"
- "_elapsed_years"
- "_start_age"
- "_start_cycles"
- "_start_nccp"
- "_start_qmaxp"
- "_start_wra"
- "delta_nccp"
- "delta_qmaxp"
- "delta_wra"
- "elapsed_years"
- "initWithDelta_nccp:"
- "initWithDelta_qmaxp:"
- "initWithDelta_wra:"
- "initWithElapsed_years:start_age:start_cycles:start_nccp:start_wra:start_qmaxp:_0s:_10s:_20s:_30s:_40s:_50s:_60s:_70s:_80s:_90s:LT20t:_20t:_22t:_24t:_26t:_28t:_30t:_32t:_34t:_36t:_38t:GT40t:LT_5c:_5c:_4c:_3c:_2c:_1c:_0c:_1c_1:_2c_1:_3c_1:_4c_1:GT5c:"
- "predictionFromElapsed_years:start_age:start_cycles:start_nccp:start_wra:start_qmaxp:_0s:_10s:_20s:_30s:_40s:_50s:_60s:_70s:_80s:_90s:LT20t:_20t:_22t:_24t:_26t:_28t:_30t:_32t:_34t:_36t:_38t:GT40t:LT_5c:_5c:_4c:_3c:_2c:_1c:_0c:_1c_1:_2c_1:_3c_1:_4c_1:GT5c:error:"
- "setDelta_nccp:"
- "setDelta_qmaxp:"
- "setDelta_wra:"
- "setElapsed_years:"
- "setStart_age:"
- "setStart_cycles:"
- "setStart_nccp:"
- "setStart_qmaxp:"
- "setStart_wra:"
- "start_age"
- "start_cycles"
- "start_nccp"
- "start_qmaxp"
- "start_wra"

```
