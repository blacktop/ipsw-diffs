## mobilerepaird

> `/usr/libexec/mobilerepaird`

### Sections with Same Size but Changed Content

- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`

```diff

-1307.40.51.0.0
-  __TEXT.__text: 0x1d7d8
-  __TEXT.__auth_stubs: 0x9a0
-  __TEXT.__objc_stubs: 0x37a0
-  __TEXT.__objc_methlist: 0x1844
-  __TEXT.__const: 0x162
-  __TEXT.__gcc_except_tab: 0x980
-  __TEXT.__objc_methname: 0x40f9
-  __TEXT.__cstring: 0x3f89
-  __TEXT.__oslogstring: 0x2e00
-  __TEXT.__objc_classname: 0x55f
-  __TEXT.__objc_methtype: 0xd1b
+1307.40.64.0.0
+  __TEXT.__text: 0x1f2ec
+  __TEXT.__auth_stubs: 0x9b0
+  __TEXT.__objc_stubs: 0x3a40
+  __TEXT.__objc_methlist: 0x1a14
+  __TEXT.__const: 0x172
+  __TEXT.__gcc_except_tab: 0xa08
+  __TEXT.__objc_methname: 0x463e
+  __TEXT.__cstring: 0x40d0
+  __TEXT.__oslogstring: 0x3461
+  __TEXT.__objc_classname: 0x59f
+  __TEXT.__objc_methtype: 0xe41
   __TEXT.__ustring: 0x12a
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_typeref: 0x3b
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_capture: 0x20
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x8e8
-  __DATA_CONST.__const: 0xcc0
-  __DATA_CONST.__cfstring: 0x3fe0
-  __DATA_CONST.__objc_classlist: 0x160
-  __DATA_CONST.__objc_protolist: 0x58
+  __TEXT.__unwind_info: 0x9e8
+  __DATA_CONST.__const: 0xdb0
+  __DATA_CONST.__cfstring: 0x4060
+  __DATA_CONST.__objc_classlist: 0x168
+  __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x118
+  __DATA_CONST.__objc_superrefs: 0x120
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA_CONST.__auth_got: 0x4e0
-  __DATA_CONST.__got: 0x4b0
+  __DATA_CONST.__auth_got: 0x4e8
+  __DATA_CONST.__got: 0x4c0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x2e28
-  __DATA.__objc_selrefs: 0x10a8
-  __DATA.__objc_ivar: 0x12c
-  __DATA.__objc_data: 0xe20
-  __DATA.__data: 0x458
+  __DATA.__objc_const: 0x3098
+  __DATA.__objc_selrefs: 0x11a0
+  __DATA.__objc_ivar: 0x148
+  __DATA.__objc_data: 0xe70
+  __DATA.__data: 0x4c0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 609
-  Symbols:   298
-  CStrings:  1583
+  Functions: 668
+  Symbols:   299
+  CStrings:  1664
 
Symbols:
+ _NSClassFromString
+ _objc_retain_x6
- _objc_retain_x28
CStrings:
+ "%@ request failed"
+ "%s: ship-charge-limit state unreadable; treating ship mode as unavailable (will retry)"
+ "%s: ship-status publish not permitted: not in trade-in ship mode (marker=%d viaTradeIn=%d)"
+ "+[CRShipModeHelper mayPublishShipModeStatus]"
+ "@\"<CRShipModeStepProviders>\""
+ "@\"NSData\""
+ "@\"NSError\"40@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32"
+ "@\"NSNumber\""
+ "@20@0:8B16"
+ "@40@0:8@16@24@32"
+ "@48@0:8@16@24@32@40"
+ "@?16@0:8"
+ "CRShipModeBatteryDischargeDriver: ignoring backend seam on a non-internal build"
+ "CRShipModeDefaultStepProviders"
+ "CRShipModeHelper: cleared ship lock marker (device-error latch reset, pending device-error report activity cancelled)"
+ "CRShipModeHelper: ignoring battery-trust seam on a non-internal build"
+ "CRShipModeHelper: ignoring flags-reader seam on a non-internal build"
+ "CRShipModeHelper: set ship lock marker (viaTradeIn=%d, wasPresent=%d, device-error latch reset=%d)"
+ "CRShipModeNotifyEngine: overrideCertificatePEM set without overrideSignature; ignoring it rather than signing with a NULL key"
+ "CRShipModeNotifyEngine: refusing to install the %{public}s seam outside a test process"
+ "CRShipModeOperationScheduler: DG9 report already delivered this session; skipping for %{public}@"
+ "CRShipModeOperationScheduler: DG9 report for %{public}@ delivered"
+ "CRShipModeOperationScheduler: DG9 report for %{public}@ failed: %{public}@; will retry on the next attempt"
+ "CRShipModeOperationScheduler: ignoring compliance-cadence seam on a non-internal build"
+ "CRShipModeOperationScheduler: ignoring injected step providers outside a test process"
+ "CRShipModeOperationScheduler: ignoring injected store outside a test process"
+ "CRShipModeOperationScheduler: notify for %{public}@ abandoned: ship-mode authorization revoked before the POST"
+ "CRShipModeOperationScheduler: refusing DG9 report for %{public}@: operation carries no server notify"
+ "CRShipModeOperationScheduler: reporting DG9 device error for %{public}@ (untrusted battery at lock attempt)"
+ "CRShipModeStepProviders"
+ "FINISH_CAMERA_CONTROL_REPAIR_DESC"
+ "FINISH_CAMERA_CONTROL_REPAIR_TITLE"
+ "Non-HTTP response to %@ request"
+ "NotifyServerAbandoned"
+ "PART_CAMERA_CONTROL"
+ "Ship-mode authorization was revoked before the notify POST"
+ "ShipModeNotify: %{public}@ HTTP %ld"
+ "ShipModeNotify: %{public}@ non-HTTP response"
+ "ShipModeNotify: %{public}@ transport failure: %{private}@"
+ "ShipModeNotify: authorization revoked during BAA issuance; abandoning POST"
+ "T@\"<CRShipModeStepProviders>\",&,N,V_providers"
+ "T@\"NSData\",C,N,V_overrideSignature"
+ "T@\"NSError\",C,N,V_overrideCredentialError"
+ "T@\"NSNumber\",C,N,V_internalBuildOverride"
+ "T@\"NSString\",C,N,V_overrideCertificatePEM"
+ "T@?,C,N,V_transport"
+ "TB,N,V_notifyAuthorizedByShipMode"
+ "XCTestCase"
+ "_clearReadyToShipFollowUp"
+ "_failureForResponse:data:transportError:command:"
+ "_internalBuildOverride"
+ "_issueCredentials:certificatePEM:error:"
+ "_notifyAuthorizedByShipMode"
+ "_overrideCertificatePEM"
+ "_overrideCredentialError"
+ "_overrideSignature"
+ "_parseBodyAndReply:replyOnce:"
+ "_postReadyToShipFollowUpViaTradeIn:"
+ "_providers"
+ "_reportDG9DeviceErrorForFailedLatch:"
+ "_runWithEnabled:deviceError:partnerID:stillAuthorized:replyOnce:"
+ "_sendRequest:endpointURL:completion:"
+ "_transport"
+ "clearFollowUpItemWithUniqueID:"
+ "initWithFileURL:"
+ "initWithStore:providers:"
+ "internalBuildOverride"
+ "mayPublishShipModeStatus"
+ "notifyAuthorizedByShipMode"
+ "overrideCertificatePEM"
+ "overrideCredentialError"
+ "overrideSignature"
+ "performEraseWithCompletion:"
+ "postFollowUpItemWithUniqueID:title:informativeText:"
+ "providers"
+ "resetShipModeAvailabilityCacheForTesting"
+ "setBatteryTrustReaderForTesting:"
+ "setComplianceCheckIntervalSecondsForTesting:"
+ "setInternalBuildOverride:"
+ "setNotifyAuthorizedByShipMode:"
+ "setOverrideCertificatePEM:"
+ "setOverrideCredentialError:"
+ "setOverrideSignature:"
+ "setProviders:"
+ "setShipChargeLimitFlagsReaderForTesting:"
+ "setTransport:"
+ "shiplock-eval(daemon-start): marker present but cannot ship (enabled=%d compliant=%d trusted=%d); clearing Ready to Ship followup"
+ "shiplock-eval(daemon-start): scheduling network-gated device-error report"
+ "shiplock-eval: no longer in trade-in ship mode; abandoning the device-error report"
+ "submitNotifyWithEnabled:deviceError:partnerID:stillAuthorized:completion:"
+ "submitWithEnabled:deviceError:partnerID:stillAuthorized:completion:"
+ "transport"
+ "v24@0:8@\"NSString\"16"
+ "v24@0:8@?<v@?B@\"NSString\">16"
+ "v32@?0@\"NSData\"8@\"NSHTTPURLResponse\"16@\"NSError\"24"
+ "v48@0:8B16B20@\"NSString\"24@?<B@?>32@?<v@?@\"NSError\">40"
+ "v48@0:8B16B20@24@?32@?40"
- "%s: IOPSShippingChargeLimitGetState failed (0x%08x); treating ship mode as unavailable (will retry)"
- "CRShipModeHelper: cleared ship lock marker"
- "CRShipModeHelper: set ship lock marker (viaTradeIn=%d)"
- "Network request failed"
- "Non-HTTP response"
- "Non-HTTP response to status request"
- "ShipModeNotify: HTTP %ld"
- "ShipModeNotify: status HTTP %ld"
- "ShipModeNotify: status transport failure: %{private}@"
- "ShipModeNotify: transport failure: %{private}@"
- "Status request failed"
- "T@\"CRShipModeNotifyEngine\",R,N,V_engine"
- "_runWithEnabled:deviceError:partnerID:replyOnce:"
- "engine"
- "shiplock-eval(daemon-start): marker present but cannot ship (enabled=%d compliant=%d trusted=%d); clearing Ready to Ship followup and scheduling network-gated device-error report"
- "submitWithEnabled:deviceError:partnerID:completion:"
```
