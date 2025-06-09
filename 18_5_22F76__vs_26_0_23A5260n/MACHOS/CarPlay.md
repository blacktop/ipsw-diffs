## CarPlay

> `/System/Library/CoreServices/CarPlay.app/CarPlay`

```diff

-385.24.1.0.0
+512.2.4.0.0
   __TEXT.__text: 0x4
   __TEXT.__auth_stubs: 0x10
   __TEXT.__unwind_info: 0x58

   - /System/Library/PrivateFrameworks/CAFUI.framework/CAFUI
   - /System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework
   - /System/Library/PrivateFrameworks/CarPlayAssetUI.framework/CarPlayAssetUI
+  - /System/Library/PrivateFrameworks/ContextualSuggestionClient.framework/ContextualSuggestionClient
   - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi
   - /System/Library/PrivateFrameworks/DashBoard.framework/DashBoard
   - /System/Library/PrivateFrameworks/HangTracer.framework/HangTracer

   - /usr/lib/libMemoryResourceException.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1EA2B8CE-439D-32BF-A3D3-63FECA9655B8
+  UUID: A187F140-CA40-36B4-A195-1EA70CCC61FE
   Functions: 1
   Symbols:   3
   CStrings:  0

```
