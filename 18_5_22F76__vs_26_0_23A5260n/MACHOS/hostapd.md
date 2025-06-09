## hostapd

> `/usr/libexec/hostapd`

```diff

-400.5.0.0.0
-  __TEXT.__text: 0x2a30c
+400.6.0.0.0
+  __TEXT.__text: 0x2a500
   __TEXT.__auth_stubs: 0xc00
   __TEXT.__const: 0xf9a
-  __TEXT.__cstring: 0xaf13
-  __TEXT.__oslogstring: 0xb35
-  __TEXT.__unwind_info: 0x7e8
+  __TEXT.__cstring: 0xaf47
+  __TEXT.__oslogstring: 0xb68
+  __TEXT.__unwind_info: 0x7f0
   __TEXT.__eh_frame: 0x50
   __DATA_CONST.__auth_got: 0x600
   __DATA_CONST.__got: 0x88
-  __DATA_CONST.__const: 0x5a8
+  __DATA_CONST.__const: 0x5c8
   __DATA_CONST.__cfstring: 0x40
   __DATA.__data: 0x308
   __DATA.__bss: 0x1a0

   - /System/Library/PrivateFrameworks/IO80211.framework/IO80211
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libpcap.A.dylib
-  UUID: 0B1FD0EF-802C-3670-BE23-DB901810B701
-  Functions: 703
+  UUID: 4523E409-0186-39B2-9B6E-3E1D3CE50708
+  Functions: 705
   Symbols:   211
-  CStrings:  1291
+  CStrings:  1295
 
Symbols:
+ _Apple80211BindToInterfaceWithParams
- _Apple80211BindToInterface
CStrings:
+ "%s: enter"
+ "%s: exit"
+ "Terminating because DextCrashed"
+ "darwin_wireless_event_service_notification_callback"

```
