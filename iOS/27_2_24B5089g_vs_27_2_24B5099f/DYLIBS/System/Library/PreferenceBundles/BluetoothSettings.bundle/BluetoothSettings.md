## BluetoothSettings

> `/System/Library/PreferenceBundles/BluetoothSettings.bundle/BluetoothSettings`

```diff

-2701.2.0.0.0
+2701.4.0.0.0
   __TEXT.__text: 0x235c0
   __TEXT.__objc_methlist: 0x17e4
   __TEXT.__cstring: 0x1af1
   __TEXT.__const: 0x598
   __TEXT.__gcc_except_tab: 0x2e8
-  __TEXT.__oslogstring: 0x2172
+  __TEXT.__oslogstring: 0x2182
   __TEXT.__ustring: 0x8c
   __TEXT.__swift5_typeref: 0x34a
   __TEXT.__constg_swiftt: 0x15c
Symbols:
+ -[BTSDevicesController handleDADaemonSessionEvent:]
+ -[BTSDevicesController reinitDADaemonSession]
+ _OBJC_CLASS_$_DADaemonSession
+ ___45-[BTSDevicesController reinitDADaemonSession]_block_invoke
- -[BTSDevicesController handleDASessionEvent:]
- -[BTSDevicesController reinitDASession]
- _OBJC_CLASS_$_DASession
- ___39-[BTSDevicesController reinitDASession]_block_invoke
CStrings:
+ "DADaemonSession from BTSettings activated"
+ "Re-init DADaemonSession"
- "DASession from BTSettings activated"
- "Re-init DASession"
```
