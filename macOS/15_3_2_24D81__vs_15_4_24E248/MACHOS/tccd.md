## tccd

> `/System/Library/PrivateFrameworks/TCC.framework/Support/tccd`

```diff

-820.0.2.0.6
-  __TEXT.__text: 0x5e160
-  __TEXT.__auth_stubs: 0x13f0
-  __TEXT.__objc_stubs: 0x6e00
-  __TEXT.__objc_methlist: 0x2cbc
-  __TEXT.__cstring: 0xbb1d
+822.0.4.0.0
+  __TEXT.__text: 0x60858
+  __TEXT.__auth_stubs: 0x1400
+  __TEXT.__objc_stubs: 0x6fc0
+  __TEXT.__objc_methlist: 0x2edc
+  __TEXT.__cstring: 0xbc16
   __TEXT.__const: 0x5f0
-  __TEXT.__gcc_except_tab: 0x2460
-  __TEXT.__objc_methname: 0xb4f3
-  __TEXT.__oslogstring: 0x96e5
-  __TEXT.__objc_classname: 0x3a1
-  __TEXT.__objc_methtype: 0xe87
-  __TEXT.__unwind_info: 0xe90
-  __DATA_CONST.__auth_got: 0xa08
-  __DATA_CONST.__got: 0x3e8
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x1b18
-  __DATA_CONST.__cfstring: 0x6520
+  __TEXT.__gcc_except_tab: 0x24e8
+  __TEXT.__objc_methname: 0xb7c3
+  __TEXT.__oslogstring: 0x982f
+  __TEXT.__objc_classname: 0x3a2
+  __TEXT.__objc_methtype: 0xec4
+  __TEXT.__unwind_info: 0xf18
+  __DATA_CONST.__auth_got: 0xa10
+  __DATA_CONST.__got: 0x3e0
+  __DATA_CONST.__auth_ptr: 0x20
+  __DATA_CONST.__const: 0x1bb8
+  __DATA_CONST.__cfstring: 0x65c0
   __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x108
-  __DATA_CONST.__objc_arraydata: 0xec8
-  __DATA_CONST.__objc_dictobj: 0xc30
+  __DATA_CONST.__objc_arraydata: 0xe98
+  __DATA_CONST.__objc_dictobj: 0xc08
   __DATA_CONST.__objc_arrayobj: 0x90
-  __DATA_CONST.__objc_intobj: 0x378
-  __DATA.__objc_const: 0x57f0
-  __DATA.__objc_selrefs: 0x1fc0
-  __DATA.__objc_ivar: 0x4bc
+  __DATA_CONST.__objc_intobj: 0x3a8
+  __DATA.__objc_const: 0x5558
+  __DATA.__objc_selrefs: 0x20c8
+  __DATA.__objc_ivar: 0x4c0
   __DATA.__objc_data: 0xbe0
   __DATA.__data: 0x240
   __DATA.__crash_info: 0x40

   - /System/Library/PrivateFrameworks/IconServices.framework/Versions/A/IconServices
   - /System/Library/PrivateFrameworks/PlugInKit.framework/Versions/A/PlugInKit
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/Versions/A/RunningBoardServices
+  - /System/Library/PrivateFrameworks/SetupAssistantFramework.framework/Versions/A/SetupAssistantFramework
   - /System/Library/PrivateFrameworks/SystemPolicy.framework/Versions/A/SystemPolicy
   - /System/Library/PrivateFrameworks/TCC.framework/Versions/A/TCC
+  - /usr/lib/libEndpointSecuritySystem.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: CEC8FFD8-9D24-39EC-8809-0FA524274922
-  Functions: 1709
-  Symbols:   455
-  CStrings:  4586
+  UUID: 50572452-8674-332F-A741-0F7EBE95D9AA
+  Functions: 1752
+  Symbols:   457
+  CStrings:  4627
 
Symbols:
+ _OBJC_CLASS_$_SAUserSetupState
+ _ess_notify_tcc_modify
CStrings:
+ "%{public}@ attempted to call %{public}@ without the recommended %{public}@ entitlement"
+ "-[TCCDPlatform sendAnalyticsForAction:service:subjectIdentity:indirectObjectIdentity:authValue:includeV1AuthValue:v1AuthValue:desiredAuth:domainReason:promptType:macBuddyStatus:]_block_invoke"
+ "-[TCCDServer publishAccessChangedEvent:forService:client:clientType:authValue:authReason:andKillClient:attributionChain:]"
+ "<Invalid MacBuddy Status>"
+ "MacBuddy is off"
+ "MacBuddy is on"
+ "TCCD_MSG_MESSAGE_OPTION_INCLUDE_POLICY_RECORDS_KEY"
+ "TCCD_MSG_METRICS_SERVICE_NAME"
+ "TCCExternalMetrics"
+ "Tq,V_macBuddyStatus"
+ "_locked_populateGeneralAuthorzationFieldsForService:info:entry:"
+ "_locked_populateIndirectAuthorzationFieldsForService:info:entry:"
+ "_locked_populatePolicyAuthorizationForSubjectWithInfoDict:message:"
+ "_locked_populatePolicyAuthorizationsForClient:message:"
+ "_locked_populatePolicyAuthorizationsForService(): failed to allocate recordInfo dictionary."
+ "_locked_populatePolicyAuthorizationsForService:message:specifiedAuth:"
+ "_macBuddyStatus"
+ "addBundleIdWithSpecifiedAuth:infoDict:message:"
+ "checkMacBuddyStatus"
+ "client: %@  has no MDM records for service: %@"
+ "client: %@ msg: %@"
+ "com.apple.dt.Xcode"
+ "com.apple.private.tcc.external.report"
+ "external-report"
+ "getSetupStateForUser:"
+ "internal policy"
+ "macBuddy status: %@"
+ "macBuddyStatus"
+ "macbuddy_on"
+ "non_modifiable"
+ "populatePolicyAuthorizationsForClient:message:"
+ "populatePolicyAuthorizationsForService:message:specifiedAuth:"
+ "publishAccessChangedEvent:forService:client:clientType:authValue:authReason:andKillClient:attributionChain:"
+ "sendAnalyticsForAction:service:subjectIdentity:indirectObjectIdentity:authValue:includeV1AuthValue:v1AuthValue:desiredAuth:domainReason:promptType:macBuddyStatus:"
+ "sendAnalyticsForExternal:withMacBuddyStatus:function:"
+ "service: %@ msg: %@"
+ "setMacBuddyStatus:"
+ "stringForAnalyticsMacBuddyStatus:"
+ "system tccd handling external metrics report"
+ "v100@0:8q16@24@32@40Q48B56Q60Q68@76q84q92"
+ "v40@0:8@16@24Q32"
+ "v40@0:8@16q24@32"
+ "v40@0:8Q16@24@32"
+ "v72@0:8Q16@24@32i40Q44Q52B60@64"
- "-[TCCDPlatform sendAnalyticsForAction:service:subjectIdentity:indirectObjectIdentity:authValue:includeV1AuthValue:v1AuthValue:desiredAuth:domainReason:promptType:]_block_invoke"
- "-[TCCDServer publishAccessChangedEvent:forService:client:clientType:authValue:andKillClient:]"
- "NSUserAvailabilityNameUsageDescription"
- "kTCCServiceUserAvailability"
- "publishAccessChangedEvent:forService:client:clientType:authValue:andKillClient:"
- "sendAnalyticsForAction:service:subjectIdentity:indirectObjectIdentity:authValue:includeV1AuthValue:v1AuthValue:desiredAuth:domainReason:promptType:"
- "v56@0:8Q16@24@32i40Q44B52"
- "v92@0:8q16@24@32@40Q48B56Q60Q68@76q84"

```
