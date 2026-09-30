## libJP2.dylib

> `/System/Library/Frameworks/ImageIO.framework/Versions/A/Resources/libJP2.dylib`

```diff

-2847.1.0.0.0
-  __TEXT.__text: 0xd2914
-  __TEXT.__gcc_except_tab: 0x5f24
-  __TEXT.__const: 0x2e6e
-  __TEXT.__cstring: 0x27fae
-  __TEXT.__unwind_info: 0x2028
+2851.0.0.0.0
+  __TEXT.__text: 0xd2a90
+  __TEXT.__gcc_except_tab: 0x5f64
+  __TEXT.__const: 0x2e7e
+  __TEXT.__cstring: 0x280af
+  __TEXT.__unwind_info: 0x2030
   __TEXT.__eh_frame: 0x48
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0xc0

   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 2386
+  Functions: 2385
   Symbols:   2426
   CStrings:  2023
 
Functions:
~ __ZN12kd_mct_stage25apply_output_restrictionsEN7bounded2v111bounded_ptrI19kd_output_comp_infoEEiNS2_IKiEE : 3564 -> 3980
~ __ZN22kd_precinct_size_class17augment_free_listEv : 616 -> 640
~ _JP2SetOptimalScalingFactor : 332 -> 292
- _ZN10kdu_output3putEh.cold.1
~ _ZN12kd_mct_stage25apply_output_restrictionsEN7bounded2v111bounded_ptrI19kd_output_comp_infoEEiNS2_IKiEE.cold.7 : 40 -> 48
~ _ZN12kd_mct_stage25apply_output_restrictionsEN7bounded2v111bounded_ptrI19kd_output_comp_infoEEiNS2_IKiEE.cold.8 : 40 -> 48
~ _ZN12kd_mct_stage25apply_output_restrictionsEN7bounded2v111bounded_ptrI19kd_output_comp_infoEEiNS2_IKiEE.cold.9 : 40 -> 48
CStrings:
+ "Invalid DWT transform block geometry in multi-component transform.  The declared number of decomposition levels does not fully partition the block's inputs."
+ "Invalid DWT transform block geometry in multi-component transform.  The declared number of decomposition levels is inconsistent with the number of block inputs."
- "get_total_composition_dims never succeeded\n"
- "total_nodes >= 0"
```
