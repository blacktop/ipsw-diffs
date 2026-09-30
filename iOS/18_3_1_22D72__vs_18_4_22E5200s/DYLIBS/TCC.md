## TCC

> `/System/Library/PrivateFrameworks/TCC.framework/TCC`

```diff

-820.0.2.0.6
-  __TEXT.__text: 0x11bb0
+822.0.4.0.0
+  __TEXT.__text: 0x11dbc
   __TEXT.__auth_stubs: 0xa80
-  __TEXT.__objc_methlist: 0x14
-  __TEXT.__cstring: 0x26e9
+  __TEXT.__objc_methlist: 0x11c
+  __TEXT.__cstring: 0x279e
   __TEXT.__const: 0x398
-  __TEXT.__oslogstring: 0xe7c
-  __TEXT.__unwind_info: 0x4a8
-  __TEXT.__objc_classname: 0x111
+  __TEXT.__oslogstring: 0xead
+  __TEXT.__unwind_info: 0x4e8
+  __TEXT.__objc_classname: 0x120
   __TEXT.__objc_methname: 0x147
   __TEXT.__objc_methtype: 0xb5
   __DATA_CONST.__got: 0xc8
-  __DATA_CONST.__const: 0x1360
-  __DATA_CONST.__objc_classlist: 0x60
-  __DATA_CONST.__objc_protolist: 0x68
+  __DATA_CONST.__const: 0x1388
+  __DATA_CONST.__objc_classlist: 0x68
+  __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8
+  __DATA_CONST.__objc_selrefs: 0xa8
   __DATA_CONST.__objc_superrefs: 0x8
   __AUTH_CONST.__auth_got: 0x540
   __AUTH_CONST.__const: 0x298
-  __AUTH_CONST.__cfstring: 0x12e0
-  __AUTH_CONST.__objc_const: 0xf38
-  __AUTH.__objc_data: 0x50
-  __AUTH.__data: 0x1b8
-  __DATA.__data: 0x818
+  __AUTH_CONST.__cfstring: 0x1300
+  __AUTH_CONST.__objc_const: 0xe50
+  __AUTH.__objc_data: 0xa0
+  __AUTH.__data: 0x1e0
+  __DATA.__data: 0x870
   __DATA.__bss: 0x70
   __DATA_DIRTY.__objc_data: 0x370
   __DATA_DIRTY.__bss: 0x90

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 437
-  Symbols:   747
-  CStrings:  514
+  Functions: 464
+  Symbols:   815
+  CStrings:  523
 
Symbols:
+ _tcc_authorization_record_get_non_modifiable
+ _tcc_authorization_record_set_non_modifiable
+ _tcc_message_options_get_include_policy
+ _tcc_message_options_set_include_policy
+ _tcc_metrics_create
+ _tcc_metrics_get_service_name
+ _tcc_metrics_set_service_name
+ _tcc_server_send_analytics
- _kTCCServiceUserAvailability
CStrings:
+ "Allow Standard User to Set System Service, "
+ "Failed to report external prompt"
+ "Has Prompted For Allow, "
+ "Non-modifiable, "
+ "OS_tcc_metrics"
+ "Prompt reported"
+ "TCCD_MSG_MESSAGE_OPTION_INCLUDE_POLICY_RECORDS_KEY"
+ "TCCD_MSG_MESSAGE_OPTION_SET_NO_KILL_KEY"
+ "TCCD_MSG_METRICS_SERVICE_NAME"
+ "TCCExternalMetrics"
+ "non_modifiable"
- "Allow Standard User to Set System Service"
- "Has Prompted For Allow"
- "kTCCServiceUserAvailability"

```
