## perfdata

> `/System/Library/PrivateFrameworks/perfdata.framework/Versions/A/perfdata`

```diff

 121.0.0.0.0
-  __TEXT.__text: 0x80a4
+  __TEXT.__text: 0x80ac
   __TEXT.__auth_stubs: 0x5f0
   __TEXT.__objc_methlist: 0x680
   __TEXT.__const: 0x60
   __TEXT.__cstring: 0x10ce
   __TEXT.__gcc_except_tab: 0x14
-  __TEXT.__unwind_info: 0x228
+  __TEXT.__unwind_info: 0x220
   __TEXT.__objc_classname: 0x73
   __TEXT.__objc_methname: 0x12a0
   __TEXT.__objc_methtype: 0x208
   __TEXT.__objc_stubs: 0x10e0
-  __DATA_CONST.__got: 0xe0
+  __DATA_CONST.__got: 0xc0
   __DATA_CONST.__const: 0xe98
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libSMC.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: ED318D59-2E86-38F0-B352-FCE9FD5BEEC2
-  Functions: 230
-  Symbols:   1039
+  UUID: 71906827-F271-3DE4-8265-AD82A2DE886A
+  Functions: 231
+  Symbols:   1040
   CStrings:  819
 
Symbols:
+ get_metric_filter_variables.cold.1
Functions:
~ _pdwriter_defer : 180 -> 136
~ _pdwriter_flush : 248 -> 272
~ _pddefer_flush : 280 -> 284
~ _pdwriter_start_extension : 76 -> 80
~ _config_emit : 2728 -> 2704
~ _json_end_object : 160 -> 164
~ _json_end_array : 160 -> 164
~ _json_comma : 228 -> 244
~ -[PDAggregateMeasurement initWithContainer:metric:unitString:] : 352 -> 344
~ -[PDContainer initWithFileURL:error:] : 268 -> 272
~ -[PDContainer initWithJSONData:error:] : 212 -> 216
~ -[PDContainer enumerateMeasurementsMatchingNullableFilter:error:usingBlock:] : 1136 -> 1152
~ _get_metric_filter_variables : 828 -> 808
~ -[PDMeasurement enumeratePercentilesWithError:usingBlock:] : 800 -> 804

```
