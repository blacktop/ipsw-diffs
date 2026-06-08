## LegacyHandle

> `/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/LegacyHandle.framework/LegacyHandle`

```diff

-2205.3.1.0.0
-  __TEXT.__text: 0x72c
-  __TEXT.__auth_stubs: 0xb0
+2235.48.1.0.0
+  __TEXT.__text: 0x760
   __TEXT.__const: 0x40
-  __TEXT.__unwind_info: 0x70
-  __AUTH_CONST.__auth_got: 0x58
+  __TEXT.__unwind_info: 0x78
+  __TEXT.__auth_stubs: 0x0
+  __AUTH_CONST.__auth_got: 0x0
   __DATA_DIRTY.__data: 0xe70
   __DATA_DIRTY.__bss: 0x630
   - /usr/lib/libSystem.B.dylib
-  UUID: 0B073F08-2021-3C27-BDD8-7AC6D3D77ACB
+  UUID: 562B1997-3A14-38E0-A4DB-72F34B572526
   Functions: 6
   Symbols:   27
   CStrings:  0
Functions:
~ _CloseAllHandles -> _CheckInHandleDebug : 124 -> 336
~ _CreateHandle -> _CheckOutHandleDebug : 516 -> 588
~ _CheckInHandleDebug -> _CloseAllHandles : 332 -> 124
~ _CheckOutHandleDebug -> _CreateHandle : 560 -> 532
~ _GetNumHandles : 16 -> 20

```
