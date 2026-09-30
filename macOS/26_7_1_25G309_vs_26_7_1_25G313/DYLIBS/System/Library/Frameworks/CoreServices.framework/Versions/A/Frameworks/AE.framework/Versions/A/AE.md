## AE

> `/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/AE.framework/Versions/A/AE`

```diff

-982.4.3.0.0
-  __TEXT.__text: 0x63918
+982.4.4.0.0
+  __TEXT.__text: 0x64588
   __TEXT.__auth_stubs: 0x1cd0
   __TEXT.__const: 0x9c4
   __TEXT.__cstring: 0x33a2
-  __TEXT.__oslogstring: 0x925d
+  __TEXT.__oslogstring: 0x95de
   __TEXT.__dof_AE_DTRACE: 0x643
   __TEXT.__unwind_info: 0xa0
   __TEXT.__eh_frame: 0x50

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 1332
+  Functions: 1331
   Symbols:   815
-  CStrings:  1055
+  CStrings:  1063
 
Symbols:
+ __LSCopyRunningApplicationArray
- __LSCopyApplicationArray
CStrings:
+ "%{public}sAEProcessMessage(), incoming message descriptorType mismatch, %c%c%c%c vs %c%c%c%c, returning %{public}d/errAEEventNotPermitted for event %{private}s"
+ "%{public}sAEProcessMessage(), incoming message eventClass ID mismatch, %c%c%c%c vs %c%c%c%c, returning %{public}d/errAEEventNotPermitted for event %{private}s"
+ "%{public}sAEProcessMessage(), incoming message eventID ID mismatch, %c%c%c%c vs %c%c%c%c, returning %{public}d/errAEEventNotPermitted for event %{private}s"
+ "%{public}sAEProcessMessage(): error unflattening desc: %d %{public}s"
+ "%{public}sAEProcessMessage: Discrepency between bundle.getForRecording() and impl->getForRecording(), so ignoring event, returning %{public}d/errAEEventNotHandled"
+ "%{public}sAEProcessMessage: Unable to decode incoming message into AEEventImpl, so ignoring event, returning %{public}d/errAEEventNotHandled."
+ "%{public}sDenying kAENotifyStartRecording bacause the event or event sender is not permitted, %{public}s"
+ "%{public}sSending ourselves a start notify recording event - already have listeners"
+ "%{public}saeStartRecording()"
+ "%{public}saeStopRecording()"
- "%{public}sAEProcessMessage: Discrepency between bundle.getForRecording() and impl->getForRecording(), so ignoring event."
- "%{public}sSending ourselves a start recording event - already have listeners"
```
