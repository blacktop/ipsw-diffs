## CloudKitDaemon

> `/System/Library/PrivateFrameworks/CloudKitDaemon.framework/CloudKitDaemon`

```diff

-2150.34.1.0.0
-  __TEXT.__text: 0x310350
-  __TEXT.__auth_stubs: 0x3460
-  __TEXT.__objc_methlist: 0x2967c
+2160.17.1.0.0
+  __TEXT.__text: 0x310cf4
+  __TEXT.__auth_stubs: 0x3490
+  __TEXT.__objc_methlist: 0x296cc
   __TEXT.__const: 0x22c8
   __TEXT.__swift5_typeref: 0xb8e
-  __TEXT.__cstring: 0x2260f
+  __TEXT.__cstring: 0x226dd
   __TEXT.__swift5_capture: 0x218
   __TEXT.__swift5_reflstr: 0x480
   __TEXT.__swift5_assocty: 0x78

   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_proto: 0x1e4
   __TEXT.__swift5_types: 0xa0
-  __TEXT.__gcc_except_tab: 0x7ce0
-  __TEXT.__oslogstring: 0x25fd6
+  __TEXT.__gcc_except_tab: 0x7ba4
+  __TEXT.__oslogstring: 0x2614a
   __TEXT.__ustring: 0x2c
-  __TEXT.__unwind_info: 0xaf1c
+  __TEXT.__unwind_info: 0xb100
   __TEXT.__eh_frame: 0x1898
-  __TEXT.__objc_classname: 0x4b12
-  __TEXT.__objc_methname: 0x50b6b
-  __TEXT.__objc_methtype: 0x853d
+  __TEXT.__objc_classname: 0x4b2e
+  __TEXT.__objc_methname: 0x50b8f
+  __TEXT.__objc_methtype: 0x8567
   __TEXT.__objc_stubs: 0x32520
-  __DATA_CONST.__got: 0xce8
-  __DATA_CONST.__const: 0x7dc0
-  __DATA_CONST.__objc_classlist: 0x1198
+  __DATA_CONST.__got: 0xce0
+  __DATA_CONST.__const: 0x7cc8
+  __DATA_CONST.__objc_classlist: 0x11a0
   __DATA_CONST.__objc_catlist: 0x128
   __DATA_CONST.__objc_protolist: 0x168
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x32710
+  __DATA_CONST.__objc_const: 0x327c0
   __DATA_CONST.__objc_selrefs: 0x10358
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_classrefs: 0x1808
   __DATA_CONST.__objc_superrefs: 0x10e0
   __DATA_CONST.__objc_arraydata: 0x13e0
   __AUTH_CONST.__const: 0x3a10
-  __AUTH_CONST.__objc_const: 0xe4e8
-  __AUTH_CONST.__cfstring: 0x1da40
+  __AUTH_CONST.__objc_const: 0xe530
+  __AUTH_CONST.__cfstring: 0x1dbe0
   __AUTH_CONST.__objc_arrayobj: 0x3a8
   __AUTH_CONST.__objc_dictobj: 0xaa0
   __AUTH_CONST.__objc_intobj: 0xa50
-  __AUTH_CONST.__auth_got: 0x1a40
-  __AUTH.__objc_data: 0x5980
+  __AUTH_CONST.__auth_got: 0x1a58
+  __AUTH.__objc_data: 0x5930
   __AUTH.__data: 0x1f8
   __DATA.__objc_ivar: 0x14fc
   __DATA.__objc_data: 0x20
   __DATA.__data: 0x51e8
   __DATA.__bss: 0x2128
   __DATA.__common: 0x360
-  __DATA_DIRTY.__objc_ivar: 0x1720
-  __DATA_DIRTY.__objc_data: 0x5a30
-  __DATA_DIRTY.__data: 0x5a0
+  __DATA_DIRTY.__objc_ivar: 0x172c
+  __DATA_DIRTY.__objc_data: 0x5ad0
+  __DATA_DIRTY.__data: 0x5a8
   __DATA_DIRTY.__common: 0x18
-  __DATA_DIRTY.__bss: 0x2478
+  __DATA_DIRTY.__bss: 0x2488
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4419E7B4-0D4A-3568-956C-4BCC7018B671
-  Functions: 17552
-  Symbols:   2649
-  CStrings:  24902
+  UUID: B9D5CC75-5DE8-34DE-B9FC-9F00E5DF2D88
+  Functions: 17569
+  Symbols:   2652
+  CStrings:  24936
 
Symbols:
+ _CKAddResponseHeaderValuesToUserInfoDictionary
+ _OBJC_CLASS_$_NSProxy
+ _OBJC_METACLASS_$_NSProxy
+ _notify_register_check
+ _notify_set_state
- _CKHTTPHeaderRetryAfter
- _OBJC_CLASS_$_NSHTTPURLResponse
CStrings:
+ "%@(%d)"
+ "/setup"
+ "@32@0:8^{_OpaquePCSShareProtection=}16Q24"
+ "AllowThrottling"
+ "CKDURLResponseOverrideProxy"
+ "Couldn't create a PCS etag for zone for tests %@: %@"
+ "Couldn't replace primary key of PCS"
+ "Couldn't serialize zone PCS for tests: %@"
+ "Failed to remove server provided invited key %{public}@ from zone %@: %@"
+ "Failed to roll primary key of the PCS for zone %@: %@"
+ "Failed to roll primary key of the invited PCS for zone-wide share in zone %@: %@"
+ "Failed to roll primary key of the zone PCS %@: %@"
+ "ForceZoneResaveButNoKeysRolled"
+ "HTTPResponseBodyOverride"
+ "HTTPResponseHeaderOverrides"
+ "HTTPResponseStatusOverride"
+ "Only for testing"
+ "TestInjectedThrottles"
+ "Thu Apr 18 18:50:57 2024"
+ "Warn: PCS does not have a single primary key, skipping primary key replacement. keys: %@"
+ "_realResponse"
+ "_responseHeaderOverrides"
+ "_statusCode"
+ "clearSharedMockIdentitySetsCache"
+ "initWithResponse:overrides:"
+ "partitionLookupFailed"
+ "quotaServiceUnavailable"
+ "replacePrimaryKeyInPCS:ofType:"
+ "setFlag:"
+ "solrError"
+ "timeoutOnInternalBackends"
+ "transactionTimeout"
+ "userAssignmentLocked"
- "%s(%d)"
- "Failed to remove server provided invited key %{public}@ from zone: %@"
- "ForceReturn200StatusCode"
- "HTTP/1.1"
- "Mon Feb 12 16:33:59 2024"
- "Simulate503ResponseWithRetryInterval"
- "_jsonObjectParsedBlock"
- "_xmlObjectParsedBlock"
- "initWithURL:statusCode:HTTPVersion:headerFields:"
- "setIsServerThrottle:"
- "v24@?0@\"NSDictionary\"8@\"NSData\"16"
- "v24@?0@8@\"NSData\"16"

```
