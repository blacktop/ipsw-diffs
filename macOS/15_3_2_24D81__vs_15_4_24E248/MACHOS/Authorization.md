## Authorization

> `/System/Library/MonitorPanels/AppleDisplay.monitorPanels/Contents/Resources/Authorization.monitorPanel/Contents/MacOS/Authorization`

```diff

-374.0.0.0.0
-  __TEXT.__text: 0x8b0
+374.3.2.0.0
+  __TEXT.__text: 0x898
   __TEXT.__auth_stubs: 0xb0
   __TEXT.__objc_stubs: 0xe0
   __TEXT.__objc_methlist: 0x74

   - /System/Library/PrivateFrameworks/MonitorPanel.framework/Versions/A/MonitorPanel
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 19C10AA6-004B-3631-A2C2-05089F85E859
+  UUID: 32D94E0E-082C-3119-A346-FBBCA928E9DD
   Functions: 19
   Symbols:   53
   CStrings:  35
Functions:
~ -[AuthorizationPanel authorizationViewDidAuthorize:] : 132 -> 120
~ -[AuthorizationPanel authorizationViewDidDeauthorize:] : 132 -> 120
~ -[AuthorizationPanel willSelect].cold.1 : 120 -> 128
~ -[AuthorizationPanel willSelect].cold.2 : 128 -> 120
~ authChangedCallback.cold.1 : 120 -> 140
~ authChangedCallback.cold.2 : 140 -> 120

```
