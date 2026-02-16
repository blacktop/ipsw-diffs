## CaptiveNetworkSupport

> `/System/Library/SystemConfiguration/CaptiveNetworkSupport.bundle/CaptiveNetworkSupport`

```diff

-514.80.3.0.1
-  __TEXT.__text: 0x30a18
-  __TEXT.__auth_stubs: 0x1600
+514.100.16.0.0
+  __TEXT.__text: 0x30fac
+  __TEXT.__auth_stubs: 0x15f0
   __TEXT.__objc_methlist: 0x45c
-  __TEXT.__const: 0x200
-  __TEXT.__gcc_except_tab: 0x218
-  __TEXT.__oslogstring: 0x580e
-  __TEXT.__cstring: 0x2097
-  __TEXT.__unwind_info: 0x910
+  __TEXT.__const: 0x210
+  __TEXT.__oslogstring: 0x594d
+  __TEXT.__gcc_except_tab: 0x210
+  __TEXT.__cstring: 0x209a
+  __TEXT.__unwind_info: 0x930
   __TEXT.__objc_classname: 0x8e
-  __TEXT.__objc_methname: 0xc8c
+  __TEXT.__objc_methname: 0xca9
   __TEXT.__objc_methtype: 0x5a9
-  __TEXT.__objc_stubs: 0xaa0
-  __DATA_CONST.__got: 0x398
+  __TEXT.__objc_stubs: 0xae0
+  __DATA_CONST.__got: 0x3d0
   __DATA_CONST.__const: 0xaa8
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x448
+  __DATA_CONST.__objc_selrefs: 0x458
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xb10
+  __AUTH_CONST.__auth_got: 0xb08
   __AUTH_CONST.__const: 0x740
-  __AUTH_CONST.__cfstring: 0x21c0
+  __AUTH_CONST.__cfstring: 0x21e0
   __AUTH_CONST.__objc_const: 0x5d0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x30

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 35BD0543-8C3B-3D46-A6BB-18FF1B02AE9B
-  Functions: 760
-  Symbols:   2349
-  CStrings:  1592
+  UUID: D0E8F9C6-C02A-39AB-B6FF-4CB474AD8311
+  Functions: 764
+  Symbols:   2365
+  CStrings:  1599
 
Symbols:
+ _CFStringReplace
+ _CopyProxyConfiguration
+ _CopyRedactedString
+ _NetIFWiFiNetworkIsWAC
+ _SCDynamicStoreCopyProxiesWithOptions
+ _SCNetworkProxiesCopyMatching
+ _kSCPropNetProxiesBypassAllowed
+ _kSCPropNetProxiesHTTPEnable
+ _kSCPropNetProxiesHTTPSEnable
+ _kSCPropNetProxiesProxyAutoConfigEnable
+ _kSCPropNetProxiesProxyAutoDiscoveryEnable
+ _kSCPropNetProxiesSOCKSEnable
+ _kSCProxiesNoGlobal
+ _objc_msgSend$initWithDictionary:
+ _objc_msgSend$intValue
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x26
+ _valueForProxyConfigurationKey
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x25
- _objc_retain_x9
CStrings:
+ "  ssid:        %{private}@"
+ " [captive allow-list]"
+ " with remediation"
+ "%@ reporting inconclusive captive evaluation for Wi-Fi to symptoms"
+ "%@: %@ the Wi-Fi network"
+ "%@: %s"
+ "%@: %s detected for the Wi-Fi network"
+ "%@: BrokenBackhaulMonitor can probe again (%g >= %g)"
+ "%@: BrokenBackhaulMonitor can't probe yet (%g < %g)"
+ "%@: Launching Websheet with URL \"%@\""
+ "%@: Login succeeded for the captive Wi-Fi network"
+ "%@: Not probing the Wi-Fi network (%@)"
+ "%@: Not probing the Wi-Fi network (cache indicates not captive)"
+ "%@: Not probing the Wi-Fi network (ignoring until next association)"
+ "%@: Wi-Fi is captive Confidence: %s"
+ "%@: Wi-Fi not updated"
+ "%@: Wi-Fi updated"
+ "%@: current Wi-Fi %smarked whitelisted"
+ "%@: device is associated to CarPlay Wi-Fi in %s mode"
+ "%@: disabling broken backhaul monitor"
+ "%@: failed to trust the server certificate chain"
+ "%@: ignoring WAC network"
+ "%@: probed timed out for the Wi-Fi network, assuming online"
+ "%@: received TLS connection abort from the Wi-Fi network"
+ "%@: received too big html document from the Wi-Fi network"
+ "%@: reporting quick probe %s"
+ "%@: the Wi-Fi network allow-lists our probe"
+ "%s<%p> %0.09g DisplayID %@ SSID=%{private}@ Signatures=%{private}@"
+ "%s<%p> %0.09g Not Captive SSID=%{private}@ Signatures=%{private}@"
+ "*"
+ "BBMonitor: detected broken%s"
+ "BBMonitor: skipping probing allow-listed network"
+ "BrokenBackhaulMonitor started on %@"
+ "CaptiveNetworkSupport-514.100.16"
+ "Disabling AutoJoin on Wi-Fi [Reason: %@]"
+ "Matching on host=%@"
+ "Re-enabling AutoJoin on Wi-Fi"
+ "Switching to 'CarPlay Only' mode"
+ "Temporarily disabling Wi-Fi (deny-listing)"
+ "Timer fired with NULL state"
+ "Unable to launch WebSheet because %s, adding the Wi-Fi network to the 'do not join again soon' list"
+ "Wi-Fi became captive network"
+ "[%@] is no longer maintaining the captive network"
+ "adding/updating the Wi-Fi network to network cache"
+ "calling process does not have [%s] entitlement"
+ "continuing to evaluate CarPlay Wi-Fi"
+ "found valid interface (%@) proxy configuration: %@"
+ "global proxy configuration has captive bypass disabled"
+ "initWithDictionary:"
+ "intValue"
+ "looking for accounts"
+ "proxies: %@"
+ "received NE configuration change notification"
- "  ssid:        %@"
- " [captive whitelist]"
- "%@ Wi-Fi network [%@] is %s"
- "%@ reporting inconclusive captive evaluation for '%@' to symptoms"
- "%@: %@ %smarked whitelisted"
- "%@: %@ '%@'"
- "%@: %@ BrokenBackhaulMonitor can probe again (%g >= %g)"
- "%@: %@ BrokenBackhaulMonitor can't probe yet (%g < %g)"
- "%@: %@ disabling broken backhaul monitor"
- "%@: %@ not updated (new %@)"
- "%@: %@ updated"
- "%@: %@ whitelists our probe"
- "%@: %s detected on '%@'"
- "%@: Launching Websheet on SSID %@ with URL \"%@\""
- "%@: Login succeeded on '%@'"
- "%@: Not probing '%@' (%@)"
- "%@: Not probing '%@' (cache indicates not captive)"
- "%@: Not probing '%@' (ignoring until next association)"
- "%@: SSID '%@' reporting quick probe %s"
- "%@: Switching to 'CarPlay Only' mode"
- "%@: device is associated to CarPlay network SSID '%@' in %s mode"
- "%@: failed to trust the server certificate chain on '%@'"
- "%@: network [%@] is captive Confidence: %s"
- "%@: received TLS connection abort on '%@'"
- "%@: received too big html document on '%@'"
- "%s on %@ (%@)"
- "%s<%p> %0.09g DisplayID %@ SSID=%@ Signatures=%@"
- "%s<%p> %0.09g Not Captive SSID=%@ Signatures=%@"
- "BBMonitor: detected broken"
- "BBMonitor: skipping probing whitelisted network"
- "BrokenBackhaulMonitor started on %@ (%@)"
- "CaptiveNetworkSupport-514.80.3.0.1"
- "Disabling AutoJoin for %@ [Reason: %@]"
- "Matching on ssid=%@, host=%@"
- "Re-enabling %@"
- "SSID %@ became captive network"
- "Temporarily disabling (blacklisting) %@"
- "Timed out on %@ (%@), assuming online"
- "Unable to launch WebSheet because %s, blacklisting network [%@]"
- "[%@] is no longer maintaining captive network [%@]"
- "adding/updating network [%@] to network cache"
- "calling procss does not have [%s] entitlement"
- "continuing to evaluate CarPlay Wi-Fi %@"
- "looking for accounts for SSID %@"
- "recived NE configuration change notification"
- "secure"
- "unsecure"

```
