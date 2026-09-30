## libPCITransport.dylib

> `/usr/lib/libPCITransport.dylib`

```diff

 1025.0.0.0.0
-  __TEXT.__text: 0x18aac
-  __TEXT.__auth_stubs: 0xd20
-  __TEXT.__gcc_except_tab: 0x1abc
-  __TEXT.__const: 0x835
-  __TEXT.__cstring: 0x1f0b
-  __TEXT.__oslogstring: 0xeae
-  __TEXT.__unwind_info: 0xba0
+  __TEXT.__text: 0x19af8
+  __TEXT.__auth_stubs: 0xd70
+  __TEXT.__gcc_except_tab: 0x1b9c
+  __TEXT.__const: 0xacd
+  __TEXT.__cstring: 0x20ff
+  __TEXT.__oslogstring: 0xf4e
+  __TEXT.__unwind_info: 0xc48
   __DATA_CONST.__got: 0xa0
   __DATA_CONST.__const: 0x8b0
-  __AUTH_CONST.__auth_got: 0x698
-  __AUTH_CONST.__const: 0xab0
+  __AUTH_CONST.__auth_got: 0x6c0
+  __AUTH_CONST.__const: 0xbd0
   __AUTH_CONST.__cfstring: 0x260
   __DATA.__bss: 0x40
   __DATA_DIRTY.__bss: 0x110

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 564
-  Symbols:   848
-  CStrings:  400
+  Functions: 606
+  Symbols:   895
+  CStrings:  418
 
Symbols:
+ _TelephonyUtilIsOversteerEnabled
+ __ZN18telephonytransport9PCIClient14sharedInstanceEv
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKcm
+ __ZNSt3__19to_stringEi
+ _dispatch_queue_create
CStrings:
+ "%s: Oversteer: no tu transport object\n"
+ "%s: creating Oversteer transport \n"
+ "%s: failed to create Oversteer transport internal\n"
+ "%s: failed to validate Oversteer transport parameters\n"
+ "Callback."
+ "Oversteer: no tu transport object"
+ "TelephonyBasebandTransportCreate"
+ "TelephonyBasebandTransportFlushRead"
+ "TelephonyBasebandTransportFree"
+ "TelephonyBasebandTransportIsValid"
+ "TelephonyBasebandTransportRead"
+ "TelephonyBasebandTransportReadRegister"
+ "TelephonyBasebandTransportSendImage"
+ "TelephonyBasebandTransportUnblockRead"
+ "TelephonyBasebandTransportWrite"
+ "creating Oversteer transport "
+ "failed to create Oversteer transport internal"
+ "failed to validate Oversteer transport parameters"

```
