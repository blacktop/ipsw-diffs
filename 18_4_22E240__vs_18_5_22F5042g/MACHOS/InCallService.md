## InCallService

> `/Applications/InCallService.app/InCallService`

```diff

-2975.500.181.2.1
-  __TEXT.__text: 0x1f47a4
+2975.600.1.0.0
+  __TEXT.__text: 0x1f48a0
   __TEXT.__auth_stubs: 0x4df0
-  __TEXT.__objc_stubs: 0x28680
+  __TEXT.__objc_stubs: 0x286a0
   __TEXT.__objc_methlist: 0x16c60
   __TEXT.__cstring: 0x1012d
-  __TEXT.__objc_methname: 0x3e924
+  __TEXT.__objc_methname: 0x3e944
   __TEXT.__objc_classname: 0x2163
   __TEXT.__objc_methtype: 0x80db
   __TEXT.__const: 0x7754
-  __TEXT.__oslogstring: 0x1e72d
+  __TEXT.__oslogstring: 0x1e84d
   __TEXT.__gcc_except_tab: 0x18c0
   __TEXT.__ustring: 0x8
   __TEXT.__dlopen_cstrs: 0xbe

   __TEXT.__eh_frame: 0x4570
   __DATA_CONST.__auth_got: 0x2708
   __DATA_CONST.__got: 0x1da8
-  __DATA_CONST.__auth_ptr: 0x11e0
+  __DATA_CONST.__auth_ptr: 0x11d8
   __DATA_CONST.__const: 0x9670
   __DATA_CONST.__cfstring: 0x7600
   __DATA_CONST.__objc_classlist: 0x8b0

   __DATA_CONST.__objc_floatobj: 0xc0
   __DATA_CONST.__objc_doubleobj: 0x40
   __DATA.__objc_const: 0x211b8
-  __DATA.__objc_selrefs: 0xd8c8
+  __DATA.__objc_selrefs: 0xd8d0
   __DATA.__objc_ivar: 0x10b4
   __DATA.__objc_data: 0x98d0
   __DATA.__data: 0x7e80

   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 12617
   Symbols:   2667
-  CStrings:  14159
+  CStrings:  14161
 
CStrings:
+ "(disconnectedCall.contactIdentifiers.count: %lu && \n\n !(disconnectedCall.isOutgoing: %d && disconnectedCall.dateConnected: %@) && \n\n disconnectedCall.provider.isFaceTimeProvider: %d \n\n [[FTDeviceSupport sharedInstance] isGreenTea]): %d"
+ "(disconnectedCall.contactIdentifiers.count: %lu && \n\n !(disconnectedCall.isOutgoing: %d && disconnectedCall.dateConnected: %@) && \n\n disconnectedCall.provider.isFaceTimeProvider: %d \n\n self.featureFlags.callEndSpamUIEnhancementEnabled): %d"
+ "callEndSpamUIEnhancementEnabled"
+ "not a greentea device && callEndSpamUIEnhancementEnabled is disabled, so we don't show the end call screen"
- "(disconnectedCall.contactIdentifiers.count: %lu && \n\n !(disconnectedCall.isOutgoing: %d && disconnectedCall.dateConnected: %@) && \n\n disconnectedCall.provider.isFaceTimeProvider: %d \n\n [[FTDeviceSupport sharedInstance] isGreenTea]) : %d"
- "not a greentea device, so we don't show the end call screen"

```
