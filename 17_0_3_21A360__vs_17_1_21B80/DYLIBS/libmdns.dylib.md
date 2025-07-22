## libmdns.dylib

> `/usr/lib/libmdns.dylib`

```diff

-2200.0.8.0.0
-  __TEXT.__text: 0x30be4
+2200.40.37.0.1
+  __TEXT.__text: 0x30d2c
   __TEXT.__auth_stubs: 0x1c90
   __TEXT.__objc_methlist: 0x10c
   __TEXT.__cstring: 0x1fab
   __TEXT.__const: 0xa6
   __TEXT.__gcc_except_tab: 0x78
-  __TEXT.__oslogstring: 0x355d
-  __TEXT.__unwind_info: 0x91c
+  __TEXT.__oslogstring: 0x364f
+  __TEXT.__unwind_info: 0x920
   __TEXT.__eh_frame: 0x7c
   __TEXT.__objc_classname: 0x523
   __TEXT.__objc_methname: 0xca9
   __TEXT.__objc_methtype: 0x5ec
   __TEXT.__objc_stubs: 0xc20
-  __DATA_CONST.__got: 0x200
+  __DATA_CONST.__got: 0x208
   __DATA_CONST.__const: 0x2888
   __DATA_CONST.__objc_classlist: 0x180
   __DATA_CONST.__objc_protolist: 0x1a0

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BA869A1D-D231-38C7-90D2-239B6082BDD3
+  UUID: 6C3E1BC9-486E-3311-B771-A18885787DB9
   Functions: 790
-  Symbols:   2900
-  CStrings:  1152
+  Symbols:   2901
+  CStrings:  1157
 
Symbols:
+ ____mdns_create_dns_over_bytestream_framer_block_invoke.1136
+ ___block_descriptor_tmp.1.1483
+ ___block_descriptor_tmp.10.1131
+ ___block_descriptor_tmp.1037
+ ___block_descriptor_tmp.1189
+ ___block_descriptor_tmp.1385
+ ___block_descriptor_tmp.14.1140
+ ___block_descriptor_tmp.1425
+ ___block_descriptor_tmp.1441
+ ___block_descriptor_tmp.1470
+ ___block_descriptor_tmp.1480
+ ___block_descriptor_tmp.18.1144
+ ___block_descriptor_tmp.22.1138
+ ___block_descriptor_tmp.27.1134
+ ___block_descriptor_tmp.37.1149
+ ___block_descriptor_tmp.39.1146
+ ___block_descriptor_tmp.4.1318
+ ___block_descriptor_tmp.41.1128
+ ___block_descriptor_tmp.44.1118
+ ___block_descriptor_tmp.46.1114
+ ___block_descriptor_tmp.49.1319
+ ___block_descriptor_tmp.5.1324
+ ___block_descriptor_tmp.50.1209
+ ___block_descriptor_tmp.67.1192
+ ___block_descriptor_tmp.69.1193
+ ___block_descriptor_tmp.7.1334
+ ___block_descriptor_tmp.70.1216
+ ___block_descriptor_tmp.71.1215
+ ___block_descriptor_tmp.72.1213
+ ___block_descriptor_tmp.92.1269
+ ___block_descriptor_tmp.97.1245
+ ___block_literal_global.1034
+ ___block_literal_global.12.1129
+ ___block_literal_global.1322
+ ___block_literal_global.1381
+ ___block_literal_global.1423
+ ___block_literal_global.1439
+ ___block_literal_global.1467
+ ___block_literal_global.1478
+ ___block_literal_global.16.1137
+ ___block_literal_global.20.1142
+ __mdns_pf_create_thread_filter_rule_user
+ __mdns_pf_create_thread_nat64_rule_user
+ _kPFProtocol
- ____mdns_create_dns_over_bytestream_framer_block_invoke.1134
- ___block_descriptor_tmp.1.1481
- ___block_descriptor_tmp.10.1129
- ___block_descriptor_tmp.1035
- ___block_descriptor_tmp.1187
- ___block_descriptor_tmp.1383
- ___block_descriptor_tmp.14.1138
- ___block_descriptor_tmp.1423
- ___block_descriptor_tmp.1439
- ___block_descriptor_tmp.1468
- ___block_descriptor_tmp.1478
- ___block_descriptor_tmp.18.1142
- ___block_descriptor_tmp.22.1136
- ___block_descriptor_tmp.27.1132
- ___block_descriptor_tmp.37.1147
- ___block_descriptor_tmp.39.1144
- ___block_descriptor_tmp.4.1316
- ___block_descriptor_tmp.41.1126
- ___block_descriptor_tmp.44.1116
- ___block_descriptor_tmp.46.1112
- ___block_descriptor_tmp.49.1317
- ___block_descriptor_tmp.5.1322
- ___block_descriptor_tmp.50.1207
- ___block_descriptor_tmp.67.1190
- ___block_descriptor_tmp.69.1191
- ___block_descriptor_tmp.7.1332
- ___block_descriptor_tmp.70.1214
- ___block_descriptor_tmp.71.1213
- ___block_descriptor_tmp.72.1211
- ___block_descriptor_tmp.92.1267
- ___block_descriptor_tmp.97.1243
- ___block_literal_global.1032
- ___block_literal_global.12.1127
- ___block_literal_global.1320
- ___block_literal_global.1379
- ___block_literal_global.1421
- ___block_literal_global.1437
- ___block_literal_global.1465
- ___block_literal_global.1476
- ___block_literal_global.16.1135
- ___block_literal_global.20.1140
- __mdns_pf_create_thread_pass_all_user_for_conn_tracking
- __mdns_pf_create_thread_user
CStrings:
+ "Failed to create conn tracking rule XPC dictionary"
+ "Failed to create pass IGMP rule XPC dictionary"
+ "PFUserAddRule() for connection tracking failed"
+ "PFUserAddRule() for pass IGMP failed"
+ "PFUserCreate() failed to create filter rule user"
+ "PFUserCreate() failed to create nat64 rule user"
- "PFUserCreate() failed to create user"

```
