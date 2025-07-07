## MobileMulticastTransfer

> `/System/Library/PrivateFrameworks/MobileMulticastTransfer.framework/MobileMulticastTransfer`

```diff

-144.0.0.0.0
-  __TEXT.__text: 0x2d038
+149.0.0.0.0
+  __TEXT.__text: 0x2d034
   __TEXT.__auth_stubs: 0xc80
   __TEXT.__objc_methlist: 0x1578
   __TEXT.__const: 0x4908
   __TEXT.__cstring: 0xe08
-  __TEXT.__oslogstring: 0x3695
+  __TEXT.__oslogstring: 0x3696
   __TEXT.__gcc_except_tab: 0x654
   __TEXT.__unwind_info: 0xca0
   __TEXT.__objc_classname: 0x31a

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8FF459F8-8999-32E2-9784-ADF8BD6EFE8B
+  UUID: CB0FFAB4-D1EE-3ED9-B469-80AB28074D38
   Functions: 1248
   Symbols:   4385
   CStrings:  1282
Functions:
~ -[MIBUNANPublisher publisher:receivedMessage:fromSubscriberID:subscriberAddress:] : 308 -> 304
CStrings:
+ "%{public}@: NAN publisher received message: %{public}@ from peer: %{public}@"
+ "Stopping NAN client listener and multicast socket."
- "%{public}@: NAN publisher received message: %{publc}@ from peer: %{public}@"
- "Stopping NAN client lisenter and multicast socket."

```
