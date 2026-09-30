## EAP-KRB

> `/System/Library/SystemConfiguration/PPPController.bundle/Contents/PlugIns/EAP-KRB.ppp/Contents/MacOS/EAP-KRB`

```diff

 1016.0.0.0.0
-  __TEXT.__text: 0x14dc
+  __TEXT.__text: 0x14bc
   __TEXT.__auth_stubs: 0x290
   __TEXT.__cstring: 0x2f6
   __TEXT.__const: 0x8

   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Kerberos.framework/Versions/A/Kerberos
   - /usr/lib/libSystem.B.dylib
-  UUID: CF6B9A56-3385-3DA8-9A91-BD96E26911FC
+  UUID: 4F8D0D66-E992-3C60-99E3-27282A450B3C
   Functions: 21
   Symbols:   72
   CStrings:  23
Functions:
~ _Server_Dispose : 80 -> 84
~ _Server_Authorize : 980 -> 972
~ _eapkrb_ui_tgt : 264 -> 256
~ _printGSSErrors : 264 -> 260
~ _InteractiveUI : 68 -> 80
~ sub_38cc -> sub_1ab4 : 252 -> 224

```
