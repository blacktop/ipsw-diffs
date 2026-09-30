## com.apple.security.sandbox

> `com.apple.security.sandbox`

```diff

-2680.160.4.0.0
-  __TEXT.__os_log: 0x21df sha256:19d309a1ecb879144ab8abd323116bccdac6ab38e746a2854e6fdbee533d5599
+2680.160.5.0.0
+  __TEXT.__os_log: 0x2213 sha256:9fe2acf060037f387fa77530394780aa30ced9ac185be46e476669fcb63809a9
   __TEXT.__const: 0x1f5cf sha256:16b2c2bf285f9585f1c06dbfd7ad0550b074f62bda14d3844becbbd1259946e1
-  __TEXT.__cstring: 0x7a08 sha256:dbdeb7b143c3c542f84ac37e5a971d2388eca222287cb1d07fe9e00544873cec
-  __TEXT_EXEC.__text: 0x4fa3c sha256:35b1b852bc1fda38b858fe3c4ee34b52112a3a9006626955d25ef8847596a8a7
+  __TEXT.__cstring: 0x7a06 sha256:0fe35b56fda1e833f93f0c89562d70a4fe91d6b96b1184eb53092d49fe521624
+  __TEXT_EXEC.__text: 0x4fa64 sha256:98bacca007ed59da4cdf1813f8f1fce388906d6aa04786dfe0688f19f07e5a0f
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x318 sha256:a25b833c77290ac779bdc5d39c14617f5ea6b328e05f222a65aaaa22c0715ac8
+  __DATA.__data: 0x318 sha256:f19a2c82189920877154029f77075a53fa4431979781141d36001fcbe87d4a5b
   __DATA.__bss: 0x7f120 sha256:c1b2ad20587918619e666424444185278ec27aea01d4e3df8aa46e2b3723c0e9
-  __DATA_CONST.__auth_got: 0xa68 sha256:18c6797584308b98597ea123eda348d828e8af26465f3571e445913fcaf1202e
-  __DATA_CONST.__got: 0xf0 sha256:5806224bfdf33f26dfd5ca3273099fa5a062dfad07ada64f7768f6b537e505d9
-  __DATA_CONST.__auth_ptr: 0x8 sha256:302e9017dfe7bef897ce468363dff0e323ec4e34f3003bc62e49b52faa0564bb
-  __DATA_CONST.__const: 0x3d38 sha256:c4854fc5e263f9401a7945ae02f0e356dcf083a0e6bad02952de14c80df9923c
-  __DATA_CONST.__kalloc_type: 0x14c0 sha256:34921dd2902b3f69b97465c737a37b8cf2de916dbafb3c114332b513ebd42fb1
-  __DATA_CONST.__kalloc_var: 0x4b0 sha256:0ce14b429f46562dcfd6b48abdae0a129b305a134b4893e806c91b55f5d9bde2
-  UUID: 57470467-0045-3D35-A38B-3C13D1994E7F
-  Functions: 920
-  Symbols:   1998
-  CStrings:  1540
+  __DATA_CONST.__auth_got: 0xa68 sha256:3666cbfd42798f6dec891e72f50a2825072110c87f30f23709d711be70f13461
+  __DATA_CONST.__got: 0xf0 sha256:8fcf118d814d3fb0b25ed27aff93dcd2b7b5ef7bda858b8baaf44aa4056b3f9c
+  __DATA_CONST.__auth_ptr: 0x8 sha256:8527f4c43c5c2b5dc668eb976547257d284d15110911cab6cdc11d5aa19d698e
+  __DATA_CONST.__const: 0x3d00 sha256:9ff04329195c3a2a76f4f8315850689b48b02dfc6652e1475de4d1f1c41a915d
+  __DATA_CONST.__kalloc_type: 0x14c0 sha256:40210d1edc553cbce02ba763f92e834272b88087086c96ecf190f76d0379b134
+  __DATA_CONST.__kalloc_var: 0x4b0 sha256:e4c9f427c3b1184ea929a9b10e28d12e43142ed4dde08a025ab6ac2122bcb24a
+  UUID: FDD279E4-F3EC-3072-AB61-62F6D7D7E4B3
+  Functions: 918
+  Symbols:   1995
+  CStrings:  1539
 
Symbols:
+ __block_descriptor_tmp.11.3251
+ __block_descriptor_tmp.15.3224
+ __block_descriptor_tmp.21.3241
+ __block_descriptor_tmp.3235
+ __block_descriptor_tmp.5.3240
+ __block_descriptor_tmp.65
+ __block_descriptor_tmp.8.3246
+ _log_approval_error
+ _sandcastle_dependencies
+ approval_do_callout._os_log_fmt.308
+ approval_do_callout._os_log_fmt.310
+ approval_response_wait._os_log_fmt.312
+ approval_response_wait._os_log_fmt.313
+ log_approval_error._os_log_fmt
+ log_approval_error._os_log_fmt.75
+ log_approval_error._os_log_fmt.76
+ pending_approval_entry_create.kalloc_type_view_1459
+ pending_approval_entry_create.kalloc_type_view_1466
+ pending_approval_entry_release.kalloc_type_view_1438
+ sb_user_approval._os_log_fmt.38
- ___approval_solicit_block_invoke
- __block_descriptor_tmp.11.3254
- __block_descriptor_tmp.15.3227
- __block_descriptor_tmp.21.3244
- __block_descriptor_tmp.306
- __block_descriptor_tmp.3238
- __block_descriptor_tmp.5.3243
- __block_descriptor_tmp.69
- __block_descriptor_tmp.8.3249
- __block_literal_global.308
- _is_sandcastle_dependency
- _pending_approval_entry_release
- approval_do_callout._os_log_fmt.314
- approval_do_callout._os_log_fmt.316
- approval_response_wait._os_log_fmt.318
- approval_response_wait._os_log_fmt.319
- is_sandcastle_dependency.sandcastle_dependencies
- pending_approval_entry_create.kalloc_type_view_1461
- pending_approval_entry_create.kalloc_type_view_1468
- pending_approval_entry_release.kalloc_type_view_1440
- sb_user_approval._os_log_fmt.36
- sb_user_approval._os_log_fmt.41
- sb_user_approval._os_log_fmt.43
CStrings:
+ "com.apple.cfprefsd"
+ "sandboxd rejected approval request from %s for %s (%s): %s"
+ "sandboxd rejected approval request from %s for %s: %s"
- " ("
- ")"
- "sandboxd rejected approval request from %s for %s%s%s%s: %s"
- "v16@?0^{proc=}8"

```
