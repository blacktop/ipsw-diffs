## InCallService

> `/Applications/InCallService.app/InCallService`

```diff

-3027.200.64.0.0
-  __TEXT.__text: 0x24fdb0
-  __TEXT.__auth_stubs: 0x6320
-  __TEXT.__objc_stubs: 0x28380
-  __TEXT.__objc_methlist: 0x182b0
+3027.200.73.2.1
+  __TEXT.__text: 0x24febc
+  __TEXT.__auth_stubs: 0x6310
+  __TEXT.__objc_stubs: 0x28360
+  __TEXT.__objc_methlist: 0x18288
   __TEXT.__cstring: 0x1146d
-  __TEXT.__objc_methname: 0x3fade
+  __TEXT.__objc_methname: 0x3fac8
   __TEXT.__objc_classname: 0x1fe1
   __TEXT.__objc_methtype: 0x7cfb
   __TEXT.__const: 0x8414
-  __TEXT.__oslogstring: 0x20b8d
+  __TEXT.__oslogstring: 0x20c5d
   __TEXT.__gcc_except_tab: 0x1c90
   __TEXT.__ustring: 0x4
   __TEXT.__dlopen_cstrs: 0x5a

   __TEXT.__swift_as_ret: 0x22c
   __TEXT.__swift5_mpenum: 0x3c
   __TEXT.__swift5_protos: 0x44
-  __TEXT.__unwind_info: 0x92e8
+  __TEXT.__unwind_info: 0x92d0
   __TEXT.__eh_frame: 0x7190
-  __DATA_CONST.__auth_got: 0x31a0
+  __DATA_CONST.__auth_got: 0x3198
   __DATA_CONST.__got: 0x20f8
   __DATA_CONST.__auth_ptr: 0x14e0
   __DATA_CONST.__const: 0xb720

   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__objc_floatobj: 0x90
   __DATA.__objc_const: 0x22968
-  __DATA.__objc_selrefs: 0xdbc0
+  __DATA.__objc_selrefs: 0xdbb8
   __DATA.__objc_ivar: 0x11dc
   __DATA.__objc_data: 0xa0a8
   __DATA.__data: 0x8fb8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: BC0AA39F-114E-3878-ABB0-A9AECAE48979
-  Functions: 14428
-  Symbols:   3164
-  CStrings:  15253
+  UUID: 7628F11C-C82F-30D6-A44B-1CB757978CBE
+  Functions: 14425
+  Symbols:   3163
+  CStrings:  15255
 
Symbols:
- _$s15ConversationKit24ScreeningNumberOverridesV016overridedDisplayD0SSSgyFZ
CStrings:
+ "disconnectedCall requires callback UI"
+ "disconnectedCall: %@ disconnectedReason: %ld (disconnectedCall.contactIdentifiers.count: %lu && \n\n !(disconnectedCall.isOutgoing: %d && disconnectedCall.dateConnected: %@) && \n\n disconnectedCall.provider.isFaceTimeProvider: %d \n\n [[FTDeviceSupport sharedInstance] isGreenTea]) : %d"
+ "setMostRecentlyDisconnectedAudioCall: %@"
+ "showFailureOrFallbackAlertIfNecessaryForCall %@ shouldShowFailureAlert: %d"
- "(disconnectedCall.contactIdentifiers.count: %lu && \n\n !(disconnectedCall.isOutgoing: %d && disconnectedCall.dateConnected: %@) && \n\n disconnectedCall.provider.isFaceTimeProvider: %d \n\n [[FTDeviceSupport sharedInstance] isGreenTea]) : %d"
- "overrideScreeningName"

```
