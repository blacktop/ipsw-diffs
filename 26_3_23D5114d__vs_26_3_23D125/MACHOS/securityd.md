## securityd

> `/usr/libexec/securityd`

```diff

-61901.80.24.0.0
+61901.80.25.0.0
   __TEXT.__text: 0x25dfd4
   __TEXT.__auth_stubs: 0x42b0
   __TEXT.__objc_stubs: 0x1c8e0
   __TEXT.__objc_methlist: 0x153e8
   __TEXT.__const: 0x919
-  __TEXT.__objc_methname: 0x2c896
-  __TEXT.__cstring: 0x211d7
+  __TEXT.__objc_methname: 0x2c864
+  __TEXT.__cstring: 0x211cd
   __TEXT.__oslogstring: 0x2d61c
   __TEXT.__swift5_typeref: 0x37a
   __TEXT.__swift5_fieldmd: 0x120

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: F7B07F72-4046-38F7-BB3B-9BBB00C77F69
+  UUID: AD3B7251-DFB0-37D7-BDAB-4D7B0C208590
   Functions: 9650
   Symbols:   1778
   CStrings:  19665
Symbols:
+ _kSecurityRTCFieldAccountIsDBR
- _kSecurityRTCFieldAccountIsG
CStrings:
+ "-[CuttlefishXPCWrapper performCKServerUnreadableDataRemovalWithSpecificUser:isDBRv2:accountIsW:internalAccount:demoAccount:altDSID:flowID:deviceSessionID:canSendMetrics:reply:]_block_invoke"
+ "-[CuttlefishXPCWrapper resetWithSpecificUser:resetReason:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:internalAccount:demoAccount:isDBRv2:accountIsW:accountType:altDSID:flowID:deviceSessionID:canSendMetrics:reply:]_block_invoke"
+ "TB,N,V_accountIsD"
+ "_accountIsD"
+ "_isDBRv2"
+ "accountIsD"
+ "clearCliqueFromAccount:resetReason:isDBRv2:reply:"
+ "initForContainer:contextID:activeAccount:stateHolder:flagHandler:sosAdapter:octagonAdapter:accountsAdapter:authKitAdapter:personaAdapter:deviceInfoAdapter:secureBackupAdapter:laContextAdapter:ckksAccountSync:lockStateTracker:cuttlefishXPCWrapper:escrowRequestClass:notifierClass:flowID:deviceSessionID:permittedToSendMetrics:accountIsD:accountIsW:reachabilityTracker:escrowChecker:"
+ "performCKServerUnreadableDataRemoval:isDBRv2:accountIsW:altDSID:reply:"
+ "performCKServerUnreadableDataRemovalWithSpecificUser:isDBRv2:accountIsW:internalAccount:demoAccount:altDSID:flowID:deviceSessionID:canSendMetrics:reply:"
+ "resetAndEstablish:resetReason:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:accountSettings:isDBRv2:accountIsW:reply:"
+ "resetAndEstablish:resetReason:isDBRv2:accountIsW:reply:"
+ "resetWithSpecificUser:resetReason:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:internalAccount:demoAccount:isDBRv2:accountIsW:accountType:altDSID:flowID:deviceSessionID:canSendMetrics:reply:"
+ "rpcReset:isDBRv2:reply:"
+ "rpcResetAndEstablish:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:accountSettings:isDBRv2:accountIsW:reply:"
+ "rpcResetAndEstablish:isDBRv2:reply:"
+ "setAccountIsD:"
- "-[CuttlefishXPCWrapper performCKServerUnreadableDataRemovalWithSpecificUser:isGuitarfish:accountIsW:internalAccount:demoAccount:altDSID:flowID:deviceSessionID:canSendMetrics:reply:]_block_invoke"
- "-[CuttlefishXPCWrapper resetWithSpecificUser:resetReason:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:internalAccount:demoAccount:isGuitarfish:accountIsW:accountType:altDSID:flowID:deviceSessionID:canSendMetrics:reply:]_block_invoke"
- "TB,N,V_accountIsG"
- "_accountIsG"
- "_isGuitarfish"
- "accountIsG"
- "clearCliqueFromAccount:resetReason:isGuitarfish:reply:"
- "initForContainer:contextID:activeAccount:stateHolder:flagHandler:sosAdapter:octagonAdapter:accountsAdapter:authKitAdapter:personaAdapter:deviceInfoAdapter:secureBackupAdapter:laContextAdapter:ckksAccountSync:lockStateTracker:cuttlefishXPCWrapper:escrowRequestClass:notifierClass:flowID:deviceSessionID:permittedToSendMetrics:accountIsG:accountIsW:reachabilityTracker:escrowChecker:"
- "performCKServerUnreadableDataRemoval:isGuitarfish:accountIsW:altDSID:reply:"
- "performCKServerUnreadableDataRemovalWithSpecificUser:isGuitarfish:accountIsW:internalAccount:demoAccount:altDSID:flowID:deviceSessionID:canSendMetrics:reply:"
- "resetAndEstablish:resetReason:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:accountSettings:isGuitarfish:accountIsW:reply:"
- "resetAndEstablish:resetReason:isGuitarfish:accountIsW:reply:"
- "resetWithSpecificUser:resetReason:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:internalAccount:demoAccount:isGuitarfish:accountIsW:accountType:altDSID:flowID:deviceSessionID:canSendMetrics:reply:"
- "rpcReset:isGuitarfish:reply:"
- "rpcResetAndEstablish:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:accountSettings:isGuitarfish:accountIsW:reply:"
- "rpcResetAndEstablish:isGuitarfish:reply:"
- "setAccountIsG:"

```
