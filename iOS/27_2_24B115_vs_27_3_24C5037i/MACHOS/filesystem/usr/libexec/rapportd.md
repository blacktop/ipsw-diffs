## rapportd

> `/usr/libexec/rapportd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_acfuncs`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-751.200.101.0.0
-  __TEXT.__text: 0x19da80
+751.300.41.0.0
+  __TEXT.__text: 0x19e28c
   __TEXT.__auth_stubs: 0x3a50
   __TEXT.__objc_stubs: 0x145c0
-  __TEXT.__objc_methlist: 0xae28
+  __TEXT.__objc_methlist: 0xae18
   __TEXT.__const: 0x6700
-  __TEXT.__cstring: 0x3e426
+  __TEXT.__cstring: 0x3e9e6
   __TEXT.__objc_classname: 0x11af
-  __TEXT.__objc_methtype: 0x4f81
-  __TEXT.__gcc_except_tab: 0x2600
-  __TEXT.__objc_methname: 0x1eaf0
+  __TEXT.__objc_methtype: 0x4f91
+  __TEXT.__gcc_except_tab: 0x2650
+  __TEXT.__objc_methname: 0x1eb00
   __TEXT.__oslogstring: 0x3682
   __TEXT.__swift5_typeref: 0x17d8
   __TEXT.__swift5_capture: 0xb78

   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_acfuncs: 0x104
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x78e8
+  __TEXT.__unwind_info: 0x7908
   __TEXT.__eh_frame: 0x4c8c
-  __DATA_CONST.__const: 0x88a0
-  __DATA_CONST.__cfstring: 0xa6a0
+  __DATA_CONST.__const: 0x88f8
+  __DATA_CONST.__cfstring: 0xa6c0
   __DATA_CONST.__objc_classlist: 0x3d0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x1a0

   __DATA_CONST.__auth_got: 0x1d38
   __DATA_CONST.__got: 0xad8
   __DATA_CONST.__auth_ptr: 0x670
-  __DATA.__objc_const: 0x12d58
-  __DATA.__objc_selrefs: 0x6600
+  __DATA.__objc_const: 0x12d50
+  __DATA.__objc_selrefs: 0x65e8
   __DATA.__objc_ivar: 0x1208
   __DATA.__objc_data: 0x2f70
   __DATA.__data: 0x3e18

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 9010
+  Functions: 9022
   Symbols:   1464
-  CStrings:  11971
+  CStrings:  11994
 
CStrings:
+ "### Family identity convert to AppleID failed (%~@)\n"
+ "### Family identity message decode failed: type %s, fromID '%~@', %#m\n"
+ "### Family identity message not dictionary: type %s, fromID '%~@', %#m\n"
+ "### Friend identity convert to AppleID failed (%~@)\n"
+ "### Friend identity message decode failed: type %s, fromID '%~@', %#m\n"
+ "### Friend identity message not dictionary: type %s, fromID '%~@', %#m\n"
+ "### IDS header truncated from '%~@', %zu bytes\n"
+ "### IDS ignoring unhandled frame 0x%02X (%s), from '%~@', %zu bytes\n"
+ "### IDS payload truncated from '%~@', %zu bytes\n"
+ "### IDS unsupported cloud service: From '%~@', %zu bytes\n"
+ "### Ignoring watch identity from unknown fromID '%~@'\n"
+ "### Ignoring watch identity from unsupported fromID '%~@'\n"
+ "### Watch identity message decode failed: type %s, fromID '%~@', %#m\n"
+ "### Watch identity message not dictionary: type %s, fromID '%~@', %#m\n"
+ "### XPC publisher reply overdue: token %llu, service %@, %.3f seconds\n"
+ "-[RPCompanionLinkDaemon _activeDeviceRemoved:cnx:stillConnectedOn:]"
+ "-[RPCompanionLinkDaemon _activeDeviceRemoved:cnx:stillConnectedOn:]_block_invoke"
+ "-[RPDaemon _xpcPublisherTriggeredToken:payload:responseHandler:]_block_invoke"
+ "@44@0:8@16i24@28@?36"
+ "@?32@0:8Q16@?24"
+ "B16@?0@\"RPConnection\"8"
+ "Connection %@ ended, device still connected on %@: %@\n"
+ "Decoded %@, expected a dictionary"
+ "Family infoResult.endpoints is nil for uri: %~@"
+ "IDS received frame from '%~@', ClSI '%@', ToID %~@, 0x%02X (%s), %zu bytes\n"
+ "No network representation to decode"
+ "ProximityServiceThirdPartyHomeSetup"
+ "Self IDS Correlation Identifier for primary AppleID: %~@ changed from %~@ -> %~@\n"
+ "_activeDeviceRemoved:cnx:stillConnectedOn:"
+ "_addMutualFriendWithAppleID:contactID:sentIdentity:"
+ "_findOtherReadyTCPConnectionForDevice:exceptConnection:"
+ "_shouldPrintSensitiveData"
+ "_xpcPublisherStartReplyCheckWithOverdueMs:overdueHandler:"
+ "com.apple.odeon.myriadRelay"
- "-[RPCompanionLinkDaemon _activeDeviceRemoved:cnx:]"
- "-[RPCompanionLinkDaemon _activeDeviceRemoved:cnx:]_block_invoke"
- "_activeDeviceRemoved:cnx:"
- "_allowMessageForRegistrationOptions:cnx:"
- "_handleFirstUnlock"
- "_isAccountCheckedDevice:"
- "accountOwnerCheckApplies"
- "homeDidSetHasOwnerAcknowledgedHomePodSiriOnboarding:"
- "localAccountUpdated"
- "setIdentifierOverride:"
- "v44@0:8@16i24@28@?36"
```
