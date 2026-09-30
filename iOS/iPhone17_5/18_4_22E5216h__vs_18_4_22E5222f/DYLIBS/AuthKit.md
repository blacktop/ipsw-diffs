## AuthKit

> `/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit`

```diff

-493.460.2.0.0
-  __TEXT.__text: 0xd1ec4
-  __TEXT.__auth_stubs: 0xda0
-  __TEXT.__objc_methlist: 0xcec4
+493.461.0.0.0
+  __TEXT.__text: 0xd2284
+  __TEXT.__auth_stubs: 0xdb0
+  __TEXT.__objc_methlist: 0xcfd4
   __TEXT.__const: 0x22f1
-  __TEXT.__cstring: 0xe201
+  __TEXT.__cstring: 0xe291
   __TEXT.__oslogstring: 0x106a4
   __TEXT.__gcc_except_tab: 0x5480
   __TEXT.__ustring: 0x1b8
   __TEXT.__dlopen_cstrs: 0x16c
-  __TEXT.__unwind_info: 0x3d90
-  __TEXT.__objc_classname: 0x1a7e
-  __TEXT.__objc_methname: 0x204a6
-  __TEXT.__objc_methtype: 0x43ad
-  __TEXT.__objc_stubs: 0xe580
-  __DATA_CONST.__got: 0x9b0
+  __TEXT.__unwind_info: 0x3da8
+  __TEXT.__objc_classname: 0x1aba
+  __TEXT.__objc_methname: 0x20646
+  __TEXT.__objc_methtype: 0x43ca
+  __TEXT.__objc_stubs: 0xe5c0
+  __DATA_CONST.__got: 0x9b8
   __DATA_CONST.__const: 0x5770
-  __DATA_CONST.__objc_classlist: 0x5c8
+  __DATA_CONST.__objc_classlist: 0x5d0
   __DATA_CONST.__objc_catlist: 0x88
-  __DATA_CONST.__objc_protolist: 0x1e0
+  __DATA_CONST.__objc_protolist: 0x1e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6a40
+  __DATA_CONST.__objc_selrefs: 0x6a88
   __DATA_CONST.__objc_protorefs: 0xd8
-  __DATA_CONST.__objc_superrefs: 0x398
+  __DATA_CONST.__objc_superrefs: 0x3a0
   __DATA_CONST.__objc_arraydata: 0x1c8
-  __AUTH_CONST.__auth_got: 0x6e0
+  __AUTH_CONST.__auth_got: 0x6e8
   __AUTH_CONST.__auth_ptr: 0x20
   __AUTH_CONST.__const: 0x10f0
-  __AUTH_CONST.__cfstring: 0xe900
-  __AUTH_CONST.__objc_const: 0x23168
+  __AUTH_CONST.__cfstring: 0xe9a0
+  __AUTH_CONST.__objc_const: 0x23748
   __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x280
-  __AUTH.__objc_data: 0x2260
-  __DATA.__objc_ivar: 0xf30
-  __DATA.__data: 0x16c0
+  __AUTH.__objc_data: 0x22b0
+  __DATA.__objc_ivar: 0xf40
+  __DATA.__data: 0x1720
   __DATA.__bss: 0x640
   __DATA_DIRTY.__objc_data: 0x1770
   __DATA_DIRTY.__bss: 0x248

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5912
-  Symbols:   8039
-  CStrings:  9204
+  Functions: 5928
+  Symbols:   8058
+  CStrings:  9229
 
Symbols:
+ _OBJC_CLASS_$_AKAuthenticatableResource
+ _OBJC_METACLASS_$_AKAuthenticatableResource
+ _SOSCCIsSOSTrustAndSyncingEnabledCachedValue
CStrings:
+ "\a\x15\x87\x16<\x17\x15\x17\x18"
+ "<%@: %p {\n\tUUID: %@,\n\tusername: %@,\n\teditable-username: %@,\n\taltDSID: %@,\n\tDSID: %@,\n\tdependentAltDSID: %@,\n\tpassword: %@,\n\tservice-type: %ld,\n\tservice IDs: %@,\n\treason: %@\n\tephemeral: %@,\n\tpassword-only: %@,\n\tpasswordlessToken: %@,\n\tidmsDataToken: %@,\n\tauthentication-type: %@,\n\tauthenticationMode: %@, \n\tisMDMInfoRequired: %@, \n\tupdate-service-tokens: %@,\n\toffer-upgrade: %@,\n\toffer-upgrade-context: %@,\n\tproxying-for-app: %@,\n\tproxied-app-id: %@,\n\tproxied-device: %@,\n\tcompanion-device: %@\n\tmax-login-attempts: %@\n\tappleid-login-enabled: %@\n\thas-empty-password: %@\n\trequest-slt: %@\n\tshort-lived-token: %@\n\tidentity-token: %@\n\ttriggered-by-push: %@\n\tskip-alert: %@\n\tskip-reachability-check: %@\n\tattempt-index: %lu,\n\tmasterKey: %@,\n\tperformUIOutOfProcess: %@,\n\tbroadcastProximityAuthOnly: %@, \n\tVerifyCredentialReason: %@, \n\tEnablePasscodeAuth: %@, \n\tPasscodeOnlyPolicy: %@, \n\tSourceAltDSID: %@, \n\tServiceToken: %@, \n\tisNativeTakeover: %@, \n\tignorePasswordCache: %@, \n\tisRequestedFromOOPViewService: %@, \n\tProxiedAppleID: %@, \n\ttelemetryDeviceSessionID: %@, \n\ttelemetryFlowID: %@, \n\tpiggybackingForTrustedDevice: %@, \n\tprotoAccountContextGivenName: %@, \n\tauthenticatableResource: %@, \n}>"
+ "@\"AKAuthenticatableResource\""
+ "AKAuthenticatableResource"
+ "AKAuthenticatableResourceProtocol"
+ "T@\"AKAuthenticatableResource\",&,N,V_authenticatableResource"
+ "T@\"NSString\",C,N,V_resourceName"
+ "Tq,N,V_internalSiwADefaultHME"
+ "Tq,N,V_resourceType"
+ "_AKInternalSiwADefaultHME"
+ "_authenticatableResource"
+ "_internalSiwADefaultHME"
+ "_resourceName"
+ "_resourceType"
+ "authenticatableResource"
+ "initWithResourceType:resourceName:"
+ "internalSiwADefaultHME"
+ "resourceName"
+ "resourceType"
+ "resourceType: %ld, resourceName: %@"
+ "setAuthenticatableResource:"
+ "setInternalSiwADefaultHME:"
+ "setResourceName:"
+ "setResourceType:"
- "\a\x15\x87\x16;\x17\x15\x17\x18"
- "<%@: %p {\n\tUUID: %@,\n\tusername: %@,\n\teditable-username: %@,\n\taltDSID: %@,\n\tDSID: %@,\n\tdependentAltDSID: %@,\n\tpassword: %@,\n\tservice-type: %ld,\n\tservice IDs: %@,\n\treason: %@\n\tephemeral: %@,\n\tpassword-only: %@,\n\tpasswordlessToken: %@,\n\tidmsDataToken: %@,\n\tauthentication-type: %@,\n\tauthenticationMode: %@, \n\tisMDMInfoRequired: %@, \n\tupdate-service-tokens: %@,\n\toffer-upgrade: %@,\n\toffer-upgrade-context: %@,\n\tproxying-for-app: %@,\n\tproxied-app-id: %@,\n\tproxied-device: %@,\n\tcompanion-device: %@\n\tmax-login-attempts: %@\n\tappleid-login-enabled: %@\n\thas-empty-password: %@\n\trequest-slt: %@\n\tshort-lived-token: %@\n\tidentity-token: %@\n\ttriggered-by-push: %@\n\tskip-alert: %@\n\tskip-reachability-check: %@\n\tattempt-index: %lu,\n\tmasterKey: %@,\n\tperformUIOutOfProcess: %@,\n\tbroadcastProximityAuthOnly: %@, \n\tVerifyCredentialReason: %@, \n\tEnablePasscodeAuth: %@, \n\tPasscodeOnlyPolicy: %@, \n\tSourceAltDSID: %@, \n\tServiceToken: %@, \n\tisNativeTakeover: %@, \n\tignorePasswordCache: %@, \n\tisRequestedFromOOPViewService: %@, \n\tProxiedAppleID: %@, \n\ttelemetryDeviceSessionID: %@, \n\ttelemetryFlowID: %@, \n\tpiggybackingForTrustedDevice: %@, \n\tprotoAccountContextGivenName: %@, \n}>"

```
