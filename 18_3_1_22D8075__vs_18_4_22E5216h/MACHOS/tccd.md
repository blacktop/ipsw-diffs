## tccd

> `/System/Library/PrivateFrameworks/TCC.framework/Support/tccd`

```diff

-820.0.2.0.6
-  __TEXT.__text: 0x5b5d4
-  __TEXT.__auth_stubs: 0x1370
-  __TEXT.__objc_stubs: 0x86a0
-  __TEXT.__objc_methlist: 0x38fc
-  __TEXT.__cstring: 0xb0ca
+822.0.4.0.0
+  __TEXT.__text: 0x5d070
+  __TEXT.__auth_stubs: 0x13a0
+  __TEXT.__objc_stubs: 0x8780
+  __TEXT.__objc_methlist: 0x3f2c
+  __TEXT.__cstring: 0xb134
   __TEXT.__const: 0x670
-  __TEXT.__gcc_except_tab: 0x1950
-  __TEXT.__objc_methname: 0xe064
-  __TEXT.__oslogstring: 0xa57f
+  __TEXT.__gcc_except_tab: 0x194c
+  __TEXT.__objc_methname: 0xe2a2
+  __TEXT.__oslogstring: 0xa688
   __TEXT.__objc_classname: 0x596
-  __TEXT.__objc_methtype: 0x1bc4
+  __TEXT.__objc_methtype: 0x1c01
   __TEXT.__dlopen_cstrs: 0x47
-  __TEXT.__unwind_info: 0x1220
-  __DATA_CONST.__auth_got: 0x9c8
-  __DATA_CONST.__got: 0x3c8
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x1c48
-  __DATA_CONST.__cfstring: 0x61a0
+  __TEXT.__unwind_info: 0x1298
+  __DATA_CONST.__auth_got: 0x9e0
+  __DATA_CONST.__got: 0x3a8
+  __DATA_CONST.__auth_ptr: 0x28
+  __DATA_CONST.__const: 0x1ce8
+  __DATA_CONST.__cfstring: 0x61c0
   __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x140
-  __DATA_CONST.__objc_intobj: 0x468
-  __DATA_CONST.__objc_arraydata: 0xbc0
-  __DATA_CONST.__objc_dictobj: 0xbe0
+  __DATA_CONST.__objc_intobj: 0x498
+  __DATA_CONST.__objc_arraydata: 0xb90
+  __DATA_CONST.__objc_dictobj: 0xbb8
   __DATA_CONST.__objc_arrayobj: 0x78
-  __DATA.__objc_const: 0x8228
-  __DATA.__objc_selrefs: 0x2738
+  __DATA.__objc_const: 0x77a0
+  __DATA.__objc_selrefs: 0x2980
   __DATA.__objc_ivar: 0x55c
   __DATA.__objc_data: 0xf50
   __DATA.__data: 0x608

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 2081
-  Symbols:   441
-  CStrings:  4332
+  Functions: 2120
+  Symbols:   444
+  CStrings:  4353
 
Symbols:
+ _CFDataGetBytePtr
+ _CFDataGetLength
+ _objc_retainAutoreleasedReturnValue
CStrings:
+ "%{public}@ attempted to call %{public}@ without the recommended %{public}@ entitlement"
+ "-[TCCDPlatform sendAnalyticsForAction:service:subjectIdentity:indirectObjectIdentity:authValue:includeV1AuthValue:v1AuthValue:desiredAuth:domainReason:promptType:macBuddyStatus:]_block_invoke"
+ "-[TCCDServer publishAccessChangedEvent:forService:client:clientType:authValue:authReason:andKillClient:attributionChain:]"
+ "TCCD_MSG_METRICS_SERVICE_NAME"
+ "TCCExternalMetrics"
+ "_locked_populateGeneralAuthorzationFieldsForService:info:entry:"
+ "_locked_populateIndirectAuthorzationFieldsForService:info:entry:"
+ "_locked_populatePolicyAuthorizationForSubjectWithInfoDict:message:"
+ "_locked_populatePolicyAuthorizationsForClient:message:"
+ "_locked_populatePolicyAuthorizationsForService(): failed to allocate recordInfo dictionary."
+ "_locked_populatePolicyAuthorizationsForService:message:specifiedAuth:"
+ "addBundleIdWithSpecifiedAuth:infoDict:message:"
+ "client: %@  has no MDM records for service: %@"
+ "client: %@ msg: %@"
+ "com.apple.private.tcc.external.report"
+ "external-report"
+ "macbuddy_on"
+ "non_modifiable"
+ "populatePolicyAuthorizationsForClient:message:"
+ "populatePolicyAuthorizationsForService:message:specifiedAuth:"
+ "publishAccessChangedEvent:forService:client:clientType:authValue:authReason:andKillClient:attributionChain:"
+ "sendAnalyticsForAction:service:subjectIdentity:indirectObjectIdentity:authValue:includeV1AuthValue:v1AuthValue:desiredAuth:domainReason:promptType:macBuddyStatus:"
+ "sendAnalyticsForExternal:withMacBuddyStatus:function:"
+ "service: %@ msg: %@"
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
