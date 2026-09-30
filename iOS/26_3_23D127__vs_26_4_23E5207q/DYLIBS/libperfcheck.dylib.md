## libperfcheck.dylib

> `/usr/lib/libperfcheck.dylib`

```diff

 46.0.0.0.0
-  __TEXT.__text: 0xa2bc
-  __TEXT.__auth_stubs: 0x860
+  __TEXT.__text: 0xa32c
+  __TEXT.__auth_stubs: 0x830
   __TEXT.__const: 0x90
   __TEXT.__cstring: 0x1091
-  __TEXT.__gcc_except_tab: 0x80
+  __TEXT.__gcc_except_tab: 0x7c
   __TEXT.__unwind_info: 0x200
   __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0x4ac

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1f0
   __DATA_CONST.__objc_arraydata: 0x28
-  __AUTH_CONST.__auth_got: 0x440
+  __AUTH_CONST.__auth_got: 0x428
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x520
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /System/Library/PrivateFrameworks/perfdata.framework/perfdata
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2B3CEB1B-1A2B-36CE-A839-895CFB661846
-  Functions: 130
-  Symbols:   418
+  UUID: C9BD5A83-730B-36A6-A1A1-9E5E5BC1DEFB
+  Functions: 132
+  Symbols:   419
   CStrings:  295
 
Symbols:
+ _OUTLINED_FUNCTION_0
+ _create_meas_epbfile.cold.1
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x10
+ _objc_retain_x26
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x8
- _objc_retain_x9
- _objc_storeStrong
Functions:
~ __add_metric : 796 -> 788
~ _abstime_to_ns.cold.1 : 20 -> 4
~ _pc_session_end : 308 -> 312
~ _pc_session_get_value : 1112 -> 1108
~ _pc_session_get_values : 316 -> 308
~ _pc_session_destroy : 316 -> 312
~ _dump_compare_metrics : 724 -> 716
~ _pc_session_create_snapshot_buf : 972 -> 1000
~ _print_metric_value : 1820 -> 1776
~ _findPIDForProcName : 452 -> 448
~ _createCFObjFromFile : 440 -> 432
+ _OUTLINED_FUNCTION_0
~ _pc_session_config_with_ep_args : 2856 -> 2840
~ _run_easyperf : 1040 -> 1036
~ _create_meas_epbfile : 1392 -> 1376
~ __get_results_for_device : 344 -> 336
~ _pc_session_set_exeargs : 200 -> 192
~ __copy_str : 92 -> 96
~ _pc_measurement_graph : 2024 -> 1896
~ _pc_session_process_pdfile : 1664 -> 1628
~ _snapshot_create_with_buf : 1396 -> 1420
~ ____processContainer_block_invoke : 248 -> 264
~ ____processContainer_block_invoke_2 : 1780 -> 1856
~ __getMeasValue : 164 -> 184
~ _makePDContainers : 1136 -> 1116
~ _makeTestHeader : 640 -> 684
~ __outputVariableNames : 164 -> 176
~ _makeMeasurementFooter : 1448 -> 1520
~ __outputVarValues : 464 -> 488
~ __variableDisplayString : 144 -> 152
~ __variableDisplayStringWithDiffs : 616 -> 620
~ _makeMetricDesc : 104 -> 116
~ __getIgnoredVars : 148 -> 160
~ _areMeasComparable : 232 -> 248
+ _create_meas_epbfile.cold.1

```
