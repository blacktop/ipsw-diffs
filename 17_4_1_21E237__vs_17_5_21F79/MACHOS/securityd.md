## securityd

> `/usr/libexec/securityd`

```diff

-61123.100.169.0.0
-  __TEXT.__text: 0x2313ec
+61123.120.34.0.0
+  __TEXT.__text: 0x23209c
   __TEXT.__auth_stubs: 0x38e0
-  __TEXT.__objc_stubs: 0x1ade0
-  __TEXT.__objc_methlist: 0x12efc
+  __TEXT.__objc_stubs: 0x1ae80
+  __TEXT.__objc_methlist: 0x12f34
   __TEXT.__const: 0x70d
-  __TEXT.__cstring: 0x1ff51
-  __TEXT.__oslogstring: 0x28adc
-  __TEXT.__gcc_except_tab: 0x6d60
-  __TEXT.__objc_classname: 0x22b5
-  __TEXT.__objc_methname: 0x2a158
-  __TEXT.__objc_methtype: 0x963b
+  __TEXT.__cstring: 0x20046
+  __TEXT.__oslogstring: 0x28c30
+  __TEXT.__gcc_except_tab: 0x6d54
+  __TEXT.__objc_classname: 0x22c9
+  __TEXT.__objc_methname: 0x2a2e2
+  __TEXT.__objc_methtype: 0x96eb
   __TEXT.__dlopen_cstrs: 0x26a
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x63b8
+  __TEXT.__unwind_info: 0x63b0
   __DATA_CONST.__auth_got: 0x1c80
   __DATA_CONST.__got: 0x8f8
   __DATA_CONST.__auth_ptr: 0x20
   __DATA_CONST.__const: 0x136f0
-  __DATA_CONST.__cfstring: 0x1b080
-  __DATA_CONST.__objc_classlist: 0x8a0
+  __DATA_CONST.__cfstring: 0x1b0e0
+  __DATA_CONST.__objc_classlist: 0x8a8
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA_CONST.__objc_classrefs: 0xd08
-  __DATA_CONST.__objc_superrefs: 0x7f0
+  __DATA_CONST.__objc_classrefs: 0xd10
+  __DATA_CONST.__objc_superrefs: 0x7f8
   __DATA_CONST.__objc_intobj: 0x1428
   __DATA_CONST.__objc_arraydata: 0x468
   __DATA_CONST.__objc_arrayobj: 0x3d8
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x23c48
-  __DATA.__objc_selrefs: 0x8a28
-  __DATA.__objc_ivar: 0x18e0
-  __DATA.__objc_data: 0x5640
+  __DATA.__objc_const: 0x23d28
+  __DATA.__objc_selrefs: 0x8a60
+  __DATA.__objc_ivar: 0x18e4
+  __DATA.__objc_data: 0x5690
   __DATA.__data: 0x2038
-  __DATA.__thread_vars: 0xc0
-  __DATA.__thread_bss: 0x1a
+  __DATA.__thread_vars: 0xd8
+  __DATA.__thread_bss: 0x1e
   __DATA.__bss: 0xaa0
   __DATA.__common: 0x10
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 9245
+  Functions: 9249
   Symbols:   1370
-  CStrings:  15365
+  CStrings:  15383
 
CStrings:
+ "\x03\x12\x11\x1f\x0f\f"
+ "-[CuttlefishXPCWrapper setAllowedMachineIDsWithSpecificUser:allowedMachineIDs:userInitiatedRemovals:evictedRemovals:unknownReasonRemovals:honorIDMSListChanges:version:flowID:deviceSessionID:canSendMetrics:altDSID:trustedDeviceHash:deletedDeviceHash:trustedDevicesUpdateTimestamp:reply:]_block_invoke"
+ "<recursion too deep>"
+ "@\"OTMetricsSessionData\""
+ "Device is not in Octagon yet to set account settings"
+ "OTMetricsSessionData"
+ "OctagonEventSignOut"
+ "Primary key conflict; deleting incoming CK item (%@)%{private}@in favor of old item (%@)%{private}@"
+ "T@\"NSString\",R,V_deviceSessionID"
+ "T@\"NSString\",R,V_flowID"
+ "T@\"OTMetricsSessionData\",&,V_sessionMetrics"
+ "UUID of olditem (%@) is higher than UUID of incoming item (%@), issuing deletion of olditem: %{private}@"
+ "Unable to fetch ckme for old item %@: %@"
+ "_sessionMetrics"
+ "afterAuthKitFetch:userInitiatedRemovals:evictedRemovals:unknownReasonRemovals:trustedDeviceHash:deletedDeviceHash:trustedDevicesUpdateTimestamp:accountIsDemo:version:"
+ "deletedDeviceHash"
+ "device is not in a ready state to set account settings, returning"
+ "initWithFlowID:deviceSessionID:"
+ "mergedAccountSettings:"
+ "replacing corrupted item %{private}@ with %{private}@"
+ "rpcSetAccountSetting: failed to reach Ready state"
+ "sessionMetrics"
+ "setAllowedMachineIDsWithSpecificUser:allowedMachineIDs:userInitiatedRemovals:evictedRemovals:unknownReasonRemovals:honorIDMSListChanges:version:flowID:deviceSessionID:canSendMetrics:altDSID:trustedDeviceHash:deletedDeviceHash:trustedDevicesUpdateTimestamp:reply:"
+ "setSessionMetrics:"
+ "trustedDeviceHash"
+ "trustedDevicesUpdateTimestamp"
+ "v128@0:8@\"TPSpecificUser\"16@\"NSSet\"24@\"NSSet\"32@\"NSSet\"40@\"NSSet\"48B56@\"NSString\"60@\"NSString\"68@\"NSString\"76B84@\"NSString\"88@\"NSString\"96@\"NSString\"104@\"NSNumber\"112@?<v@?B@\"NSError\">120"
+ "v128@0:8@16@24@32@40@48B56@60@68@76B84@88@96@104@112@?120"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSSet\"@\"NSSet\"@\"NSSet\"@\"NSSet\"@\"NSString\"@\"NSString\"@\"NSString\"@\"NSNumber\"@\"NSError\">24"
+ "v80@?0@\"NSSet\"8@\"NSSet\"16@\"NSSet\"24@\"NSSet\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56@\"NSNumber\"64@\"NSError\"72"
+ "v84@0:8@16@24@32@40@48@56@64B72@76"
- "\x03\x12\x11\x11\x1f\x0f\f"
- "-[CuttlefishXPCWrapper setAllowedMachineIDsWithSpecificUser:allowedMachineIDs:userInitiatedRemovals:evictedRemovals:unknownReasonRemovals:honorIDMSListChanges:version:reply:]_block_invoke"
- "Primary key conflict; dropping CK item %{private}@"
- "T@\"NSString\",&,N,V_deviceSessionID"
- "T@\"NSString\",&,N,V_flowID"
- "Unable to fetch ckme: %@"
- "afterAuthKitFetch:userInitiatedRemovals:evictedRemovals:unknownReasonRemovals:accountIsDemo:version:"
- "setAllowedMachineIDsWithSpecificUser:allowedMachineIDs:userInitiatedRemovals:evictedRemovals:unknownReasonRemovals:honorIDMSListChanges:version:reply:"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSSet\"@\"NSSet\"@\"NSSet\"@\"NSSet\"@\"NSString\"@\"NSError\">24"
- "v56@?0@\"NSSet\"8@\"NSSet\"16@\"NSSet\"24@\"NSSet\"32@\"NSString\"40@\"NSError\"48"
- "v60@0:8@16@24@32@40B48@52"
- "v76@0:8@\"TPSpecificUser\"16@\"NSSet\"24@\"NSSet\"32@\"NSSet\"40@\"NSSet\"48B56@\"NSString\"60@?<v@?B@\"NSError\">68"
- "v76@0:8@16@24@32@40@48B56@60@?68"

```
