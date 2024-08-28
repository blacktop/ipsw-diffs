## networkserviceproxy

> `/usr/libexec/networkserviceproxy`

```diff

-827.0.0.0.1
-  __TEXT.__text: 0xb2bb8
-  __TEXT.__auth_stubs: 0x1860
-  __TEXT.__objc_stubs: 0xc540
-  __TEXT.__objc_methlist: 0x3ddc
+834.0.0.0.0
+  __TEXT.__text: 0xb3e88
+  __TEXT.__auth_stubs: 0x1890
+  __TEXT.__objc_stubs: 0xc600
+  __TEXT.__objc_methlist: 0x3e04
   __TEXT.__const: 0x310
-  __TEXT.__objc_methname: 0xf3a6
-  __TEXT.__oslogstring: 0xf13e
+  __TEXT.__objc_methname: 0xf477
+  __TEXT.__oslogstring: 0xf31c
   __TEXT.__objc_classname: 0xc61
-  __TEXT.__objc_methtype: 0x2907
-  __TEXT.__gcc_except_tab: 0x424c
-  __TEXT.__cstring: 0xc115
+  __TEXT.__objc_methtype: 0x2915
+  __TEXT.__gcc_except_tab: 0x4310
+  __TEXT.__cstring: 0xc264
   __TEXT.__dlopen_cstrs: 0x64
-  __TEXT.__unwind_info: 0x18d8
-  __DATA_CONST.__auth_got: 0xc40
-  __DATA_CONST.__got: 0x6a8
-  __DATA_CONST.__const: 0x1f20
-  __DATA_CONST.__cfstring: 0x7a60
+  __TEXT.__unwind_info: 0x18f8
+  __DATA_CONST.__auth_got: 0xc58
+  __DATA_CONST.__got: 0x6b0
+  __DATA_CONST.__const: 0x1f70
+  __DATA_CONST.__cfstring: 0x7ae0
   __DATA_CONST.__objc_classlist: 0x2b8
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x78
   __DATA_CONST.__objc_arrayobj: 0xc0
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0xc848
-  __DATA.__objc_selrefs: 0x3408
-  __DATA.__objc_ivar: 0x98c
+  __DATA.__objc_const: 0xc918
+  __DATA.__objc_selrefs: 0x3438
+  __DATA.__objc_ivar: 0x99c
   __DATA.__objc_data: 0x1b30
   __DATA.__data: 0xc10
   __DATA.__bss: 0x1b8

   - /usr/lib/libnetwork.dylib
   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2070
-  Symbols:   621
-  CStrings:  5894
+  Functions: 2080
+  Symbols:   625
+  CStrings:  5920
 
Symbols:
+ _dispatch_queue_create_with_target$V2
+ _dispatch_suspend
+ _os_variant_has_internal_content
+ _objc_retain_x7
+ _OBJC_CLASS_$_AMSFraudReportOptions
- _objc_retain_x6
CStrings:
+ "Resuming token pair fetch, received notification on one-time token for %!@(MISSING)"
+ "%!p(MISSING) oblivious path [%!@(MISSING)] is not ready due to pending transparency status"
+ "TB,N,V_deferAgentCommit"
+ "setShouldIncludeODIAssessment:"
+ "-[NSPPrivacyTokenManager copyQueueToWaitForNonCachedRequestsForIssuerName:]"
+ "Device Identity Retry Count"
+ "DeviceIdentityRetryCount"
+ "&2"
+ "performFraudReportRefreshWithOptions:"
+ "sendRTCReportWithFailureType:errorCode:url:ingressProxy:egressProxy:tokenServer:"
+ "deferAgentCommit"
+ "Resuming token pair fetch, received notification on long-lived token for %!@(MISSING)"
+ "setAccount:"
+ "obliviousPathTransparencyState"
+ "Not waiting for ongoing call to fetch one-time token for %!@(MISSING), returned from cache"
+ "_deviceIdentityRetryCount"
+ "-[NSPPrivacyTokenManager blockNonCachedRequestsForIssuerName:]"
+ "_waitingQueuesForIssuers"
+ "previously failed to fetch device identity, allowing retry %!u(MISSING)"
+ "B20@0:8B16"
+ "Transparency state"
+ "_deferAgentCommit"
+ "Blocked token request queue"
+ "-[NSPPrivacyTokenManager unblockNonCachedRequestsForIssuerName:]"
+ "initWithTransactionIdentifier:nameSpace:fsrData:"
+ "Waiting for ongoing call to fetch long-lived token for %!@(MISSING)"
+ "v60@0:8q16i24@28@36@44@52"
+ "deferCommit"
+ "setDeferAgentCommit:"
+ "Waiting for ongoing call to fetch one-time token for %!@(MISSING)"
- "v52@0:8q16i24@28@36@44"
- "%!"(MISSING)
- "performFraudReportRefreshWithAccount:transactionID:nameSpace:fsrData:keyID:"
- "sendRTCReportWithFailureType:errorCode:url:ingressProxy:egressProxy:"

```
