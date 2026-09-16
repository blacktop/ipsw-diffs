## StatusKit

> `/System/Library/PrivateFrameworks/StatusKit.framework/StatusKit`

```diff

-154.100.1.0.0
-  __TEXT.__text: 0x4274c
-  __TEXT.__objc_methlist: 0x2128
+154.200.11.0.0
+  __TEXT.__text: 0x42960
+  __TEXT.__objc_methlist: 0x2168
   __TEXT.__const: 0x1918
   __TEXT.__gcc_except_tab: 0x884
-  __TEXT.__oslogstring: 0x5469
+  __TEXT.__oslogstring: 0x5529
   __TEXT.__cstring: 0x1c7e
-  __TEXT.__swift5_typeref: 0x7f0
-  __TEXT.__swift5_capture: 0x234
+  __TEXT.__swift5_typeref: 0x800
+  __TEXT.__swift5_capture: 0x244
   __TEXT.__constg_swiftt: 0x51c
   __TEXT.__swift5_reflstr: 0x2f5
   __TEXT.__swift5_fieldmd: 0x400

   __TEXT.__swift5_assocty: 0x100
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_acfuncs: 0xb4
-  __TEXT.__unwind_info: 0x19f8
+  __TEXT.__unwind_info: 0x1a08
   __TEXT.__eh_frame: 0x1c08
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf28
+  __DATA_CONST.__objc_selrefs: 0xf40
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0xd8
   __DATA_CONST.__objc_arraydata: 0xd0
   __DATA_CONST.__got: 0x390
-  __AUTH_CONST.__const: 0xe68
+  __AUTH_CONST.__const: 0xe90
   __AUTH_CONST.__cfstring: 0x1180
-  __AUTH_CONST.__objc_const: 0x3850
+  __AUTH_CONST.__objc_const: 0x3868
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0xaf0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1704
-  Symbols:   3798
-  CStrings:  538
+  Functions: 1709
+  Symbols:   3809
+  CStrings:  541
 
Symbols:
+ -[SKPresence presenceDaemonConnectionDidInterrupt:]
+ -[SKStatusPublishingService publishingDaemonConnectionDidInterrupt:]
+ -[SKStatusSubscriptionService subscriptionDaemonConnectionDidInterrupt:]
+ GCC_except_table145
+ GCC_except_table151
+ GCC_except_table156
+ GCC_except_table159
+ GCC_except_table57
+ GCC_except_table62
+ _$sSo10SecTaskRefa9StatusKitE07currentB0ABSgvgZTf4d_n
+ _$sSo10SecTaskRefa9StatusKitE21codeSigningIdentifierSSSgvg
+ _$ss9UnmanagedVMn
+ ___swift__destructor
+ ___swift_closure_destructor.33Tm
+ _objc_msgSend$presenceDaemonConnectionDidInterrupt:
+ _objc_msgSend$publishingDaemonConnectionDidInterrupt:
+ _objc_msgSend$subscriptionDaemonConnectionDidInterrupt:
+ _symbolic _____y_____GSg s9UnmanagedV So10CFErrorRefa
- GCC_except_table144
- GCC_except_table149
- GCC_except_table155
- GCC_except_table158
- GCC_except_table55
- _$s9StatusKit21SKPresenceXPCListenerC35currentProcessCodeSigningIdentifier33_B8CF45FBD8FB9DEE23DFD917EA1AC8D3LLSSSgvgZTf4d_n
- ___swift_closure_destructor.31Tm
CStrings:
+ "Asked to reconnect yet we already have a connection (likely interrupted)"
+ "_delegateLock presenceDaemonConnectionDidInterrupt locked"
+ "_delegateLock presenceDaemonConnectionDidInterrupt unlocked"
+ "_delegateLock presenceDaemonConnectionDidInterrupt waiting"
- "Tried to reconnect, but we already have a connection"
```
