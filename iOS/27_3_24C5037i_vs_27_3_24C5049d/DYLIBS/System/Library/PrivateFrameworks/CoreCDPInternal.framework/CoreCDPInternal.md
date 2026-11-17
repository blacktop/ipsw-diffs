## CoreCDPInternal

> `/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal`

```diff

-448.250.2.0.0
-  __TEXT.__text: 0x8f64c
-  __TEXT.__objc_methlist: 0x586c
+448.250.5.0.0
+  __TEXT.__text: 0x902b0
+  __TEXT.__objc_methlist: 0x589c
   __TEXT.__const: 0x888
-  __TEXT.__oslogstring: 0x1549e
-  __TEXT.__cstring: 0xef45
+  __TEXT.__oslogstring: 0x1550e
+  __TEXT.__cstring: 0xf025
   __TEXT.__gcc_except_tab: 0xb94
   __TEXT.__dlopen_cstrs: 0xb0
   __TEXT.__swift5_typeref: 0x3b7

   __TEXT.__swift_as_entry: 0x60
   __TEXT.__swift_as_ret: 0x58
   __TEXT.__swift_as_cont: 0x68
-  __TEXT.__unwind_info: 0x2f70
+  __TEXT.__unwind_info: 0x2f80
   __TEXT.__eh_frame: 0x918
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2728
+  __DATA_CONST.__const: 0x2770
   __DATA_CONST.__objc_classlist: 0x2a0
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x188
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3a80
+  __DATA_CONST.__objc_selrefs: 0x3aa0
   __DATA_CONST.__objc_protorefs: 0x50
-  __DATA_CONST.__objc_superrefs: 0x160
-  __DATA_CONST.__objc_arraydata: 0x230
-  __DATA_CONST.__got: 0x1188
-  __AUTH_CONST.__const: 0xb30
-  __AUTH_CONST.__cfstring: 0x9e20
-  __AUTH_CONST.__objc_const: 0x10290
+  __DATA_CONST.__objc_superrefs: 0x168
+  __DATA_CONST.__objc_arraydata: 0x150
+  __DATA_CONST.__got: 0x11a0
+  __AUTH_CONST.__const: 0xb50
+  __AUTH_CONST.__cfstring: 0x9e60
+  __AUTH_CONST.__objc_const: 0x102b0
   __AUTH_CONST.__objc_intobj: 0x180
-  __AUTH_CONST.__objc_arrayobj: 0xc0
+  __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x968
   __AUTH.__objc_data: 0x170
-  __DATA.__objc_ivar: 0x3d4
+  __DATA.__objc_ivar: 0x3d8
   __DATA.__data: 0x1220
   __DATA_DIRTY.__objc_data: 0x19b0
   __DATA_DIRTY.__data: 0x200

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3238
-  Symbols:   4258
-  CStrings:  2916
+  Functions: 3245
+  Symbols:   4268
+  CStrings:  2921
 
Symbols:
+ -[CDPDXPCEventObserver initWithEventStreamRegistrar:]
+ -[CDPDXPCEventObserver init]
+ -[CDPDXPCListener _buildRawEntitlementsBitMaskForConnection:]
+ -[CDPDXPCListener _connection:hasRawEntitlement:]
+ -[CDPWalrusDaemonService _shouldDenyPCSKeysAccess]
+ _OBJC_IVAR_$_CDPDXPCEventObserver._registrar
+ ___28-[CDPDXPCEventObserver init]_block_invoke
+ ___block_descriptor_32_e76_v32?0r*8"NSObject<OS_dispatch_queue>"16?<v?"NSObject<OS_xpc_object>">24l
+ ___block_descriptor_57_e8_32s40s48bs_e20_v20?0B8"NSError"12ls48l8s32l8s40l8
+ _kAAAnalyticsEventDeviceListCacheHit
+ _kAAAnalyticsEventDeviceListCacheMiss
+ _kAAAnalyticsEventDeviceListCacheValidation
- -[CDPDXPCListener _shouldAcceptNewConnectionWithEntitlements:]
- ___72-[CDPDClientHandler deleteRecoveryKeyWithContext:uiProvider:completion:]_block_invoke_2
CStrings:
+ "Accepting new connection %@ with raw entitlements mask %i"
+ "Denying walrus operation. Missing walrus entitlement."
+ "Denying walrus operation. Missing walrus.pcskeys entitlement."
+ "com.apple.appleaccount.custodian.healthcheck.owner.cleanupPhantomCustodian"
+ "com.apple.appleaccount.recoveryContact.custodian.nto.landing"
+ "com.apple.distnoted.matching.trusted"
+ "v32@?0r*8@\"NSObject<OS_dispatch_queue>\"16@?<v@?@\"NSObject<OS_xpc_object>\">24"
- "Accepting new connection %@ with entitlements mask %i"
- "com.apple.distnoted.matching"
```
