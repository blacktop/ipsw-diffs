## amsaccountsd

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/amsaccountsd`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_types2`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__linkguard`

```diff

-10.1.11.2.1
-  __TEXT.__text: 0x255530
-  __TEXT.__auth_stubs: 0x4660
-  __TEXT.__objc_stubs: 0xbdc0
-  __TEXT.__objc_methlist: 0x618c
-  __TEXT.__const: 0x23c50
-  __TEXT.__objc_methname: 0x11bdb
-  __TEXT.__oslogstring: 0xfdf9
-  __TEXT.__cstring: 0xccdc
-  __TEXT.__objc_methtype: 0x5218
-  __TEXT.__objc_classname: 0x1b0b
-  __TEXT.__gcc_except_tab: 0xd28
+10.1.13.2.1
+  __TEXT.__text: 0x25b574
+  __TEXT.__auth_stubs: 0x46b0
+  __TEXT.__objc_stubs: 0xbf60
+  __TEXT.__objc_methlist: 0x61ec
+  __TEXT.__const: 0x23f70
+  __TEXT.__oslogstring: 0xff29
+  __TEXT.__objc_methname: 0x11d8b
+  __TEXT.__cstring: 0xceac
+  __TEXT.__objc_methtype: 0x5268
+  __TEXT.__objc_classname: 0x1b3b
+  __TEXT.__gcc_except_tab: 0xd20
   __TEXT.__dlopen_cstrs: 0x3f7
-  __TEXT.__swift5_typeref: 0x7cc6
-  __TEXT.__swift5_capture: 0x1078
-  __TEXT.__constg_swiftt: 0x64ec
-  __TEXT.__swift5_reflstr: 0x4f8c
-  __TEXT.__swift5_fieldmd: 0x7674
-  __TEXT.__swift5_builtin: 0x190
-  __TEXT.__swift5_assocty: 0xa60
-  __TEXT.__swift5_proto: 0x1b24
-  __TEXT.__swift5_types: 0x820
-  __TEXT.__swift_as_entry: 0x3b8
-  __TEXT.__swift_as_ret: 0x4b8
-  __TEXT.__swift_as_cont: 0x9d8
+  __TEXT.__constg_swiftt: 0x65a4
+  __TEXT.__swift5_typeref: 0x7d96
+  __TEXT.__swift5_reflstr: 0x503c
+  __TEXT.__swift5_fieldmd: 0x7760
+  __TEXT.__swift5_builtin: 0x1a4
+  __TEXT.__swift5_capture: 0x110c
+  __TEXT.__swift5_mpenum: 0x110
+  __TEXT.__swift5_assocty: 0xa78
+  __TEXT.__swift5_proto: 0x1b3c
+  __TEXT.__swift5_types: 0x834
+  __TEXT.__swift_as_entry: 0x3e8
+  __TEXT.__swift_as_ret: 0x4ec
+  __TEXT.__swift_as_cont: 0xa1c
   __TEXT.__swift5_protos: 0xd0
-  __TEXT.__swift5_mpenum: 0x108
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__unwind_info: 0xc9f8
-  __TEXT.__eh_frame: 0x13a50
-  __DATA_CONST.__const: 0x137e0
-  __DATA_CONST.__cfstring: 0x4de0
-  __DATA_CONST.__objc_classlist: 0x428
+  __TEXT.__unwind_info: 0xcc38
+  __TEXT.__eh_frame: 0x13f98
+  __DATA_CONST.__const: 0x13ce0
+  __DATA_CONST.__cfstring: 0x4e40
+  __DATA_CONST.__objc_classlist: 0x430
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x290
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x1b8
-  __DATA_CONST.__objc_intobj: 0xa8
   __DATA_CONST.__linkguard: 0x2c
-  __DATA_CONST.__auth_got: 0x2340
-  __DATA_CONST.__got: 0x14a8
-  __DATA_CONST.__auth_ptr: 0x2ce8
-  __DATA.__objc_const: 0xc9a8
-  __DATA.__objc_selrefs: 0x4098
-  __DATA.__objc_ivar: 0x3a8
-  __DATA.__objc_data: 0x2fa0
-  __DATA.__data: 0xc108
+  __DATA_CONST.__objc_intobj: 0xa8
+  __DATA_CONST.__auth_got: 0x2368
+  __DATA_CONST.__got: 0x14b0
+  __DATA_CONST.__auth_ptr: 0x2d28
+  __DATA.__objc_const: 0xca78
+  __DATA.__objc_selrefs: 0x4100
+  __DATA.__objc_ivar: 0x3ac
+  __DATA.__objc_data: 0x3070
+  __DATA.__data: 0xc218
   __DATA.__common: 0x1e0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 16174
-  Symbols:   2103
-  CStrings:  5689
+  Functions: 16328
+  Symbols:   2109
+  CStrings:  5728
 
Symbols:
+ _$s10Foundation12NotificationV36_unconditionallyBridgeFromObjectiveCyACSo14NSNotificationCSgFZ
+ _$s10Foundation12NotificationVMa
+ _$s18AppleMediaServices13DeviceDetailsO23deviceUnlockedSinceBootSbSgyFZ
+ _$s18AppleMediaServices3LogV8purchaseACvgZ
+ _$s18AppleMediaServices8FlagKeysO26CardEnrollmentCacheWarmingyA2CmFWC
+ _$s2os12OSSignpostIDV3logACSo03OS_a1_D0C_tcfC
CStrings:
+ "%{public}@ Card-enrollment cache warming is disabled, not scheduling"
+ "%{public}@ Scheduled card-enrollment cache warming"
+ "%{public}@[auto-enrollment] Default pass lookup timed out after %{public}.1f seconds"
+ "%{public}@[auto-enrollment] Dropping cache write, invalidated while fetching"
+ "@\"_TtC12amsaccountsd25CardEnrollmentCacheWarmer\""
+ "AMSDDefaultPaymentPassCacheDidInvalidateNotification"
+ "AMSDPurchaseService.CacheWarming"
+ "[cache-warming] Default pass warm failed: "
+ "[cache-warming] Skipping: "
+ "[cache-warming] ["
+ "_TtC12amsaccountsd25CardEnrollmentCacheWarmer"
+ "_cardEnrollmentCacheWarmer"
+ "_defaultPaymentPassCacheGenerationBox"
+ "_fetchDefaultPaymentPassIdentifierWithLogKey:completion:"
+ "addObserverForName:object:queue:usingBlock:"
+ "alreadyWarming"
+ "arrayWithObject:"
+ "card-enrollment-warming-disabled"
+ "card-enrollment-warming-limit"
+ "cardEnrollmentWarmWindowCount"
+ "cardEnrollmentWarmWindowStart"
+ "com.apple.amsaccountsd.cardenrollmentwarming"
+ "currentDefaultPaymentPassIdentifierWithLogKey:completion:"
+ "defaultPaymentPass"
+ "initWithInteger:"
+ "invalidationObserver"
+ "isWarming"
+ "limitReached"
+ "makeIfEnabled"
+ "notUnlockedSinceBoot"
+ "nothingRegistered"
+ "postNotificationName:object:"
+ "setCardEnrollmentWarmWindowCount:"
+ "setCardEnrollmentWarmWindowStart:"
+ "setObject:atIndexedSubscript:"
+ "setupWarmingScheduleWithCompletionHandler:"
+ "success: %{public}s"
+ "v16@?0@\"NSNotification\"8"
+ "warmDefaultPaymentPass(logKey:)"
+ "warmers"
- "_currentDefaultPaymentPassIdentifierWithLogKey:completion:"
```
