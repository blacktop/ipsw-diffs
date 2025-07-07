## IOHIDT8027USBSessionFilter

> `/System/Library/HIDPlugins/IOHIDT8027USBSessionFilter.plugin/IOHIDT8027USBSessionFilter`

```diff

-2222.0.7.0.0
+2222.0.10.0.0
   __TEXT.__text: 0x1c78
   __TEXT.__auth_stubs: 0x3a0
   __TEXT.__gcc_except_tab: 0x120
   __TEXT.__const: 0x136
   __TEXT.__cstring: 0x2b8
   __TEXT.__oslogstring: 0x1dd
-  __TEXT.__unwind_info: 0x1c0
+  __TEXT.__unwind_info: 0x1d0
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__const: 0x48
   __AUTH_CONST.__auth_got: 0x1d8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 52B7C66B-535E-33FC-BB27-0904A6FE18E4
+  UUID: D3EA4C94-E3B3-347D-9190-CE093C342C7A
   Functions: 74
   Symbols:   107
   CStrings:  67
Functions:
~ __ZN26IOHIDT8027USBSessionFilter15registerServiceEP14__IOHIDService -> __ZN26IOHIDT8027USBSessionFilter21_getPropertyForClientEPvPK10__CFStringPKv : 500 -> 4
~ __ZN26IOHIDT8027USBSessionFilter7_filterEPvP14__IOHIDServiceP12__IOHIDEvent -> __ZN26IOHIDT8027USBSessionFilter20getPropertyForClientEPK10__CFStringPKv : 4 -> 160
~ sub_247ebcae0 -> __ZN26IOHIDT8027USBSessionFilter21_setPropertyForClientEPvPK10__CFStringPKvS5_ : 100 -> 4
~ sub_247ebcb44 -> __ZN26IOHIDT8027USBSessionFilter20setPropertyForClientEPK10__CFStringPKvS4_ : 80 -> 304
~ __ZN26IOHIDT8027USBSessionFilter21_setPropertyForClientEPvPK10__CFStringPKvS5_ -> __ZN26IOHIDT8027USBSessionFilter17unregisterServiceEP14__IOHIDService : 4 -> 164
~ __ZN26IOHIDT8027USBSessionFilter20getPropertyForClientEPK10__CFStringPKv -> __ZN26IOHIDT8027USBSessionFilter7_filterEPvP14__IOHIDServiceP12__IOHIDEvent : 160 -> 4
~ __ZN26IOHIDT8027USBSessionFilter20setPropertyForClientEPK10__CFStringPKvS4_ -> __ZN26IOHIDT8027USBSessionFilter6filterEP14__IOHIDServiceP12__IOHIDEvent : 304 -> 248
~ __ZN26IOHIDT8027USBSessionFilter6filterEP14__IOHIDServiceP12__IOHIDEvent -> __ZN26IOHIDT8027USBSessionFilter15registerServiceEP14__IOHIDService : 248 -> 500
~ __ZN26IOHIDT8027USBSessionFilter16_registerServiceEPvP14__IOHIDService -> sub_24844ce5c : 4 -> 100
~ __ZN26IOHIDT8027USBSessionFilter17unregisterServiceEP14__IOHIDService -> sub_24844cec0 : 164 -> 80

```
