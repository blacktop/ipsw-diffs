## AE

> `/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/AE.framework/Versions/A/AE`

```diff

-994.0.0.0.0
-  __TEXT.__text: 0x6166c
+995.0.0.0.0
+  __TEXT.__text: 0x61f08
   __TEXT.__const: 0xae4
   __TEXT.__cstring: 0x315e
-  __TEXT.__oslogstring: 0x988f
+  __TEXT.__oslogstring: 0x9b56
   __TEXT.__dof_AE_DTRACE: 0x643
   __TEXT.__unwind_info: 0x14e8
   __TEXT.__eh_frame: 0x50

   __AUTH_CONST.__const: 0x1848
   __AUTH_CONST.__cfstring: 0xc00
   __AUTH_CONST.__weak_auth_got: 0x30
-  __AUTH_CONST.__auth_got: 0xe38
+  __AUTH_CONST.__auth_got: 0xe30
   __AUTH.__data: 0x60
   __DATA.__data: 0xc0
   __DATA.__bss: 0x370

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   Functions: 1346
-  Symbols:   814
-  CStrings:  1054
+  Symbols:   813
+  CStrings:  1059
 
Symbols:
- _sprintf
Functions:
~ _AEProcessMessage : 6592 -> 9028
~ __AEEventRequiresSecurityHandlerChecks : 2440 -> 2396
~ _AEGetDescDataRange : 388 -> 384
~ sub_1890680d4 -> sub_1890b9a28 : 664 -> 636
~ sub_18906a5e0 -> sub_1890bbf18 : 284 -> 292
~ sub_18906ad64 -> sub_1890bc6a4 : 224 -> 232
~ sub_18906c650 -> sub_1890bdf98 : 1076 -> 1028
~ sub_18906d08c -> sub_1890be9a4 : 988 -> 964
~ _AESendMessage : 5660 -> 5608
~ _AERemoveEventHandler : 516 -> 492
~ sub_189087358 -> sub_1890d8c0c : 3472 -> 3492
~ sub_189088188 -> sub_1890d9a50 : 116 -> 120
~ sub_18908b31c -> sub_1890dcbe8 : 1116 -> 1124
~ sub_189092b2c -> sub_1890e4400 : 1144 -> 1112
~ sub_1890ace0c -> sub_1890fe6c0 : 1284 -> 1260
CStrings:
+ "%{public}*c%{public}s(%{public}s,%{public}s handler=%p isSys=%{BOOL}d) err=%d/%{public}s"
+ "%{public}*cAEProcessMessage(), incoming message descriptorType mismatch, %c%c%c%c vs %c%c%c%c, returning %{public}d/errAEEventNotPermitted for event %{private}s"
+ "%{public}*cAEProcessMessage(), incoming message eventClass ID mismatch, %c%c%c%c vs %c%c%c%c, returning %{public}d/errAEEventNotPermitted for event %{private}s"
+ "%{public}*cAEProcessMessage(), incoming message eventID ID mismatch, %c%c%c%c vs %c%c%c%c, returning %{public}d/errAEEventNotPermitted for event %{private}s"
+ "%{public}*cAEProcessMessage(): error unflattening desc: %d %{public}s"
+ "%{public}*cAEProcessMessage: Discrepency between bundle.getForRecording() and impl->getForRecording(), so ignoring event, returning %{public}d/errAEEventNotHandled"
+ "%{public}*cAEProcessMessage: Unable to decode incoming message into AEEventImpl, so ignoring event, returning %{public}d/errAEEventNotHandled."
+ "%{public}*cCompleted running runloop waiting for reply, waited %d seconds ( max=%g ), destValid=%{BOOL}d"
+ "%{public}*cEPPCIOStream::becomeSecure( asServer=%{BOOL}d)"
+ "%{public}*cRESULT: found=%{BOOL}d for %{public}s inSandbox=%{BOOL}d keyRef=%{public}@ out=%{public}s"
+ "%{public}*c_AECopyEntitlementForToken() RESULT=%d %{public}s inSandbox=%{BOOL}d"
+ "%{public}*c_AEEventRequiresSecurityHandlerChecks((%{public}s) = %{BOOL}d"
+ "%{public}*ceEntitlements, for pid %d sandboxed=%{BOOL}d entitlements=%{public}s"
+ "%{public}*crunning the run loop waiting for a reply for %g seconds, remaining = %d ticks destValid=%{BOOL}d"
+ "%{public}*csenderHasSpecificEntitlementForThisAppleEvent, result=%{BOOL}d"
+ "%{public}*ctoken=%{public}s inSandbox=%{BOOL}d entitlementsRef=%{public}s keyRef=%{public}@ out=%p"
- "%{public}*c%{public}s(%{public}s,%{public}s handler=%p isSys=%{public}s) err=%d/%{public}s"
- "%{public}*cAEProcessMessage: Discrepency between bundle.getForRecording() and impl->getForRecording(), so ignoring event."
- "%{public}*cCompleted running runloop waiting for reply, waited %d seconds ( max=%g ), destValid=%{public}s"
- "%{public}*cEPPCIOStream::becomeSecure( asServer=%{public}s)"
- "%{public}*cRESULT: found=%{public}s for %{public}s inSandbox=%{public}s keyRef=%{public}@ out=%{public}s"
- "%{public}*c_AECopyEntitlementForToken() RESULT=%d %{public}s inSandbox=%{public}s"
- "%{public}*c_AEEventRequiresSecurityHandlerChecks((%{public}s) = %{public}s"
- "%{public}*ceEntitlements, for pid %d sandboxed=%{public}s entitlements=%{public}s"
- "%{public}*crunning the run loop waiting for a reply for %g seconds, remaining = %d ticks destValid=%{public}s"
- "%{public}*csenderHasSpecificEntitlementForThisAppleEvent, result=%{public}s"
- "%{public}*ctoken=%{public}s inSandbox=%{public}s entitlementsRef=%{public}s keyRef=%{public}@ out=%p"
```
