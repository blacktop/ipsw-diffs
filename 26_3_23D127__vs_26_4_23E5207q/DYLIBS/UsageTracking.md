## UsageTracking

> `/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTracking`

```diff

-392.2.3.0.0
-  __TEXT.__text: 0x29830
-  __TEXT.__auth_stubs: 0x5b0
-  __TEXT.__objc_methlist: 0x1628
+392.4.7.0.0
+  __TEXT.__text: 0x2a644
+  __TEXT.__auth_stubs: 0x540
+  __TEXT.__objc_methlist: 0x1678
   __TEXT.__const: 0x108
-  __TEXT.__gcc_except_tab: 0x75c
-  __TEXT.__cstring: 0x1296
+  __TEXT.__gcc_except_tab: 0x72c
+  __TEXT.__cstring: 0x12e8
   __TEXT.__oslogstring: 0x1227
-  __TEXT.__unwind_info: 0x6e8
-  __TEXT.__eh_frame: 0x70
-  __TEXT.__objc_classname: 0x29f
-  __TEXT.__objc_methname: 0x6fb3
-  __TEXT.__objc_methtype: 0xfb0
+  __TEXT.__unwind_info: 0x720
+  __TEXT.__objc_classname: 0x2e2
+  __TEXT.__objc_methname: 0x70b8
+  __TEXT.__objc_methtype: 0x10b5
   __TEXT.__objc_stubs: 0x4260
   __DATA_CONST.__got: 0x318
-  __DATA_CONST.__const: 0xea8
-  __DATA_CONST.__objc_classlist: 0xb8
-  __DATA_CONST.__objc_protolist: 0x40
+  __DATA_CONST.__const: 0xeb8
+  __DATA_CONST.__objc_classlist: 0xc0
+  __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x13b0
-  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_selrefs: 0x13c8
+  __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x88
-  __AUTH_CONST.__auth_got: 0x2e8
+  __AUTH_CONST.__auth_got: 0x2b0
   __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0xdc0
-  __AUTH_CONST.__objc_const: 0x2798
+  __AUTH_CONST.__cfstring: 0xe00
+  __AUTH_CONST.__objc_const: 0x2838
   __AUTH_CONST.__objc_intobj: 0x60
+  __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x194
-  __DATA.__data: 0x300
+  __DATA.__data: 0x360
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x730
   __DATA_DIRTY.__bss: 0x20

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F1AAE944-F929-3A58-8331-97F54F1E07B7
-  Functions: 594
-  Symbols:   2406
-  CStrings:  1329
+  UUID: 407AB1A4-0F31-3962-BA7B-55C1F9A6EF85
+  Functions: 608
+  Symbols:   2461
+  CStrings:  1342
 
Symbols:
+ +[USTrackingAgentDataAccessConnection connectionHasFamilyControlsDataEntitlement:]
+ +[USTrackingAgentDataAccessConnection newConnection]
+ +[USTrackingAgentDataAccessConnection newInterface]
+ _FamilyControlsDataEntitlement
+ _OBJC_CLASS_$_USTrackingAgentDataAccessConnection
+ _OBJC_METACLASS_$_USTrackingAgentDataAccessConnection
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _USMachServiceNameUsageTrackingDataAccess
+ __OBJC_$_CLASS_METHODS_USTrackingAgentDataAccessConnection
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_USUsageTrackingAgentDataAccess
+ __OBJC_$_PROTOCOL_METHOD_TYPES_USUsageTrackingAgentDataAccess
+ __OBJC_CLASS_RO_$_USTrackingAgentDataAccessConnection
+ __OBJC_LABEL_PROTOCOL_$_USUsageTrackingAgentDataAccess
+ __OBJC_METACLASS_RO_$_USTrackingAgentDataAccessConnection
+ __OBJC_PROTOCOL_$_USUsageTrackingAgentDataAccess
+ __OBJC_PROTOCOL_REFERENCE_$_USUsageTrackingAgentDataAccess
+ _objc_release_x2
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x10
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
- _objc_retain_x9
CStrings:
+ "USTrackingAgentDataAccessConnection"
+ "USUsageTrackingAgentDataAccess"
+ "com.apple.UsageTrackingAgent.data-access"
+ "com.apple.developer.family-controls-data"
+ "connectionHasFamilyControlsDataEntitlement:"
+ "fetchActivityForSegmentInterval:dateInterval:users:devices:applications:categories:webDomains:refreshActivity:replyHandler:"
+ "fetchActivitySegmentForUserAltDSID:deviceIdentifier:segmentInterval:recordName:replyHandler:"
+ "v56@0:8@\"NSString\"16@\"NSString\"24q32@\"NSString\"40@?<v@?@\"NSData\"@\"NSError\">48"
+ "v56@0:8@16@24q32@40@?48"
+ "v84@0:8q16@\"NSDateInterval\"24@\"NSNumber\"32@\"NSArray\"40@\"NSArray\"48@\"NSArray\"56@\"NSArray\"64B72@?<v@?@\"NSArray\"@\"NSError\">76"
+ "v84@0:8q16@24@32@40@48@56@64B72@?76"

```
