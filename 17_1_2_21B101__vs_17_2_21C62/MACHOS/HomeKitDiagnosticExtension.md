## HomeKitDiagnosticExtension

> `/System/Library/Frameworks/HomeKit.framework/PlugIns/HomeKitDiagnosticExtension.appex/HomeKitDiagnosticExtension`

```diff

-1076.2.8.1.1
-  __TEXT.__text: 0x5c70
+1092.3.10.1.2
+  __TEXT.__text: 0x5ca0
   __TEXT.__auth_stubs: 0x540
   __TEXT.__objc_stubs: 0x1040
   __TEXT.__objc_methlist: 0x50
-  __TEXT.__const: 0x38
-  __TEXT.__gcc_except_tab: 0x288
-  __TEXT.__cstring: 0x709
+  __TEXT.__const: 0x40
+  __TEXT.__gcc_except_tab: 0x294
+  __TEXT.__cstring: 0x62b
   __TEXT.__objc_methname: 0xcf1
   __TEXT.__oslogstring: 0x92e
   __TEXT.__objc_classname: 0x48
CStrings:
+ "process == 'homed' OR process == 'osanalyticshelper' OR process == 'TrustedPeersHelper' OR process == 'homeeventsd' OR process == 'cdpd' OR subsystem == 'com.apple.HomeKit' OR subsystem == 'com.apple.CoreHAP' OR subsystem == 'com.apple.HomeKitEvents' OR sender == 'Matter'"
- "process == 'homed' OR process contains 'reportcrash' OR process == 'osanalyticshelper' OR process == 'wpantund' OR process == 'threadradiod' OR process == 'CoreThreadCommissionerServiced' OR process == 'srp-mdns-proxy' OR process == 'TrustedPeersHelper' OR process == 'homeeventsd' OR process == 'mDNSResponder' OR process == 'cdpd' OR process == 'locationd' OR subsystem == 'com.apple.HomeKit' OR subsystem == 'com.apple.CoreHAP' OR subsystem == 'com.apple.HomeKitEvents' OR sender == 'Matter'"

```
