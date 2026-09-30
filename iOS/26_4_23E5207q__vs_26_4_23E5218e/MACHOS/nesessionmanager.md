## nesessionmanager

> `/usr/libexec/nesessionmanager`

```diff

-2226.100.24.0.0
-  __TEXT.__text: 0xbab00
+2226.100.30.0.1
+  __TEXT.__text: 0xbbb48
   __TEXT.__auth_stubs: 0x1cf0
-  __TEXT.__objc_stubs: 0x8020
+  __TEXT.__objc_stubs: 0x80e0
   __TEXT.__objc_methlist: 0x3dbc
   __TEXT.__const: 0x188
-  __TEXT.__gcc_except_tab: 0x2270
-  __TEXT.__objc_methname: 0x91c1
-  __TEXT.__oslogstring: 0xfa56
+  __TEXT.__gcc_except_tab: 0x22ac
+  __TEXT.__objc_methname: 0x9238
+  __TEXT.__oslogstring: 0xfd4a
   __TEXT.__cstring: 0x54b5
   __TEXT.__objc_classname: 0xbbc
-  __TEXT.__objc_methtype: 0x2148
-  __TEXT.__unwind_info: 0x1648
+  __TEXT.__objc_methtype: 0x215e
+  __TEXT.__unwind_info: 0x1668
   __DATA_CONST.__auth_got: 0xe88
-  __DATA_CONST.__got: 0x770
+  __DATA_CONST.__got: 0x780
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x1d80
+  __DATA_CONST.__const: 0x1e10
   __DATA_CONST.__cfstring: 0x2660
   __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_protolist: 0x148

   __DATA_CONST.__objc_superrefs: 0x218
   __DATA_CONST.__objc_arraydata: 0x140
   __DATA_CONST.__objc_arrayobj: 0x120
-  __DATA_CONST.__objc_intobj: 0x210
+  __DATA_CONST.__objc_intobj: 0x228
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA.__objc_const: 0x8158
-  __DATA.__objc_selrefs: 0x23b0
+  __DATA.__objc_selrefs: 0x23d8
   __DATA.__objc_ivar: 0x794
   __DATA.__objc_data: 0x18b0
   __DATA.__data: 0xf80

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 41D82ACE-82F8-3711-8F23-33EB190EE704
-  Functions: 1890
-  Symbols:   686
-  CStrings:  4348
+  UUID: FD7B8697-4785-36E9-9E2A-E5FADC9E99F2
+  Functions: 1898
+  Symbols:   688
+  CStrings:  4367
 
Symbols:
+ _OBJC_CLASS_$_NEGuardProxyManager
+ _OBJC_CLASS_$_NEPvDConfiguration
CStrings:
+ "%@: Deregister last Filter Session calling stopGuardProxyManager: %@"
+ "%@: Failed to clear cached PvD configuration: %@"
+ "%@: Failed to load configuration to clear cached PvD: %@"
+ "%@: Failed to load configuration to persist PvD: %@"
+ "%@: Failed to save cached PvD configuration: %@"
+ "%@: Started guard proxy."
+ "@\"NEPvDConfiguration\""
+ "Clearing cached PvD configuration for %@"
+ "NESessionManager: starting guard proxy manager."
+ "NESessionManager: stopping guard proxy manager."
+ "Persisted PvD configuration for %@"
+ "PvD: %@ configuration with %lu rules exceeds maximum policy rule limit, installed first %d rules from %lu match rules"
+ "PvD: %@ installed %lu policy rules from %lu match rules (within limit of %d)"
+ "PvD: Adding PvDRulesExceeded error to extended status (total %lu policy rules, limit %d)"
+ "cachedPvDConfig"
+ "initFlowDivertControlSocketWithParams:isGuardProxy:order:"
+ "initWithDelegate:queue:url:identityRef:additionalHTTPHeaders:cachedPvDConfig:"
+ "proxyPolicyRuleCount"
+ "setCachedPvDConfig:"
+ "start"
+ "stopWithCompletionHandler:"
- "initFlowDivertControlSocketWithParams:order:"
- "initWithDelegate:queue:url:identityRef:additionalHTTPHeaders:"

```
