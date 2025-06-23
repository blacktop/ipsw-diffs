## WorkflowResponsiveness

> `/System/Library/PrivateFrameworks/WorkflowResponsiveness.framework/WorkflowResponsiveness`

```diff

-404.0.0.0.0
-  __TEXT.__text: 0x25d78
+407.0.0.0.0
+  __TEXT.__text: 0x25ec4
   __TEXT.__auth_stubs: 0x750
-  __TEXT.__objc_methlist: 0x790
+  __TEXT.__objc_methlist: 0x798
   __TEXT.__const: 0xe8
-  __TEXT.__gcc_except_tab: 0xba8
-  __TEXT.__cstring: 0x2030
+  __TEXT.__gcc_except_tab: 0xbd0
+  __TEXT.__cstring: 0x2074
   __TEXT.__oslogstring: 0x4014
   __TEXT.__unwind_info: 0x528
   __TEXT.__objc_classname: 0x11a
-  __TEXT.__objc_methname: 0x2436
-  __TEXT.__objc_methtype: 0x26a
-  __TEXT.__objc_stubs: 0x1c80
+  __TEXT.__objc_methname: 0x24e8
+  __TEXT.__objc_methtype: 0x26d
+  __TEXT.__objc_stubs: 0x1ca0
   __DATA_CONST.__got: 0x1b8
-  __DATA_CONST.__const: 0x5e0
+  __DATA_CONST.__const: 0x5e8
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x830
+  __DATA_CONST.__objc_selrefs: 0x838
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x3b8
   __AUTH_CONST.__const: 0x220
-  __AUTH_CONST.__cfstring: 0x1f60
-  __AUTH_CONST.__objc_const: 0x15f0
+  __AUTH_CONST.__cfstring: 0x1fa0
+  __AUTH_CONST.__objc_const: 0x1620
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x140
+  __DATA.__objc_ivar: 0x144
   __DATA.__data: 0xc0
   __DATA.__bss: 0x18
   __DATA_DIRTY.__objc_data: 0x2d0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 757CA114-FE95-3820-AAFF-E36C83DFFB51
-  Functions: 524
-  Symbols:   1779
-  CStrings:  1217
+  UUID: 6F7DBF15-6B18-3996-894C-87D83077DFAA
+  Functions: 525
+  Symbols:   1784
+  CStrings:  1224
 
Symbols:
+ -[WRSignpost customEnvironmentCoreAnalyticsEventName]
+ -[WRSignpost initWithSubsystem:category:name:eventIdentifierFieldName:individuationFieldName:environmentFieldNames:networkBound:customEnvironmentCoreAnalyticsEventName:diagnostics:]
+ _OBJC_IVAR_$_WRSignpost._customEnvironmentCoreAnalyticsEventName
+ _WRSignpostCustomEnvironmentCoreAnalyticsEventNameKey
+ ___block_literal_global.100
+ ___block_literal_global.102
+ _objc_msgSend$customEnvironmentCoreAnalyticsEventName
+ _objc_msgSend$initWithSubsystem:category:name:eventIdentifierFieldName:individuationFieldName:environmentFieldNames:networkBound:customEnvironmentCoreAnalyticsEventName:diagnostics:
- -[WRSignpost initWithSubsystem:category:name:eventIdentifierFieldName:individuationFieldName:environmentFieldNames:networkBound:diagnostics:]
- ___block_literal_global.97
- ___block_literal_global.99
- _objc_msgSend$initWithSubsystem:category:name:eventIdentifierFieldName:individuationFieldName:environmentFieldNames:networkBound:diagnostics:
CStrings:
+ "%@:%@:%@ (event:%@ indiv:%@ env:%@ caEventName:%@ thresholds:%lu)"
+ "@84@0:8@16@24@32@40@48@56B64@68@76"
+ "T@\"NSString\",R,V_customEnvironmentCoreAnalyticsEventName"
+ "_customEnvironmentCoreAnalyticsEventName"
+ "customEnvironmentCoreAnalyticsEventName"
+ "custom_environment_core_analytics_event_name"
+ "default"
+ "initWithSubsystem:category:name:eventIdentifierFieldName:individuationFieldName:environmentFieldNames:networkBound:customEnvironmentCoreAnalyticsEventName:diagnostics:"
- "%@:%@:%@ (event:%@ indiv:%@ env:%@ thresholds:%lu)"
- "@76@0:8@16@24@32@40@48@56B64@68"
- "initWithSubsystem:category:name:eventIdentifierFieldName:individuationFieldName:environmentFieldNames:networkBound:diagnostics:"

```
