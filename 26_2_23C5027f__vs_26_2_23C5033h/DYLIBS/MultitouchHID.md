## MultitouchHID

> `/System/Library/Extensions/AppleMultitouchSPI.kext/PlugIns/MultitouchHID.plugin/MultitouchHID`

```diff

 9110.1.0.0.0
-  __TEXT.__text: 0x52690
+  __TEXT.__text: 0x52680
   __TEXT.__auth_stubs: 0x1760
   __TEXT.__objc_methlist: 0x1e4
   __TEXT.__const: 0x1881

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 550998A3-7496-316A-9246-71C24998706A
+  UUID: 9AE60AFB-73C6-339D-98D7-D96D4CCE9FB4
   Functions: 1572
   Symbols:   2892
   CStrings:  2146
Functions:
~ __ZN11MTABCLogger5_initEP10__MTDevice : 128 -> 124
~ __ZN21MTInterferenceMonitor5_stopEv : 140 -> 136
~ __ZN21MTInterferenceMonitor27isWirelessChargingAvailableEPKvPv : 168 -> 164
~ __ZN21MTInterferenceMonitor22isUSBChargingAvailableEPKvPv : 212 -> 208

```
