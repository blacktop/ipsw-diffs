## CoreWiFi

> `/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`

```diff

-988.8.0.0.0
-  __TEXT.__text: 0x1affb8
+988.9.0.0.0
+  __TEXT.__text: 0x1b0550
   __TEXT.__auth_stubs: 0x1ad0
   __TEXT.__objc_methlist: 0x107dc
   __TEXT.__const: 0x2f08

   __TEXT.__swift5_proto: 0x270
   __TEXT.__swift5_types: 0xac
   __TEXT.__cstring: 0x1e119
-  __TEXT.__gcc_except_tab: 0x7a9c
-  __TEXT.__oslogstring: 0x1b5d0
+  __TEXT.__gcc_except_tab: 0x7b0c
+  __TEXT.__oslogstring: 0x1b869
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x5560
+  __TEXT.__unwind_info: 0x5568
   __TEXT.__eh_frame: 0x570
   __TEXT.__objc_classname: 0xfb1
   __TEXT.__objc_methname: 0x278e2
   __TEXT.__objc_methtype: 0x3934
-  __TEXT.__objc_stubs: 0x1c3c0
+  __TEXT.__objc_stubs: 0x1c3e0
   __DATA_CONST.__got: 0x918
   __DATA_CONST.__const: 0x50c0
   __DATA_CONST.__objc_classlist: 0x3a8

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 77C9F634-26C6-38E0-A1B2-9E4D03E19F5F
+  UUID: EB09EE11-31CA-3AD4-965D-EE3C152BA179
   Functions: 7540
   Symbols:   1082
-  CStrings:  15075
+  CStrings:  15080
 
Functions:
~ sub_1e18ae060 -> sub_1e1aaf060 : 624 -> 644
~ sub_1e18ae5b8 -> sub_1e1aaf5cc : 564 -> 584
~ sub_1e18af570 -> sub_1e1ab0598 : 352 -> 376
~ sub_1e18b0960 -> sub_1e1ab19a0 : 328 -> 348
~ sub_1e18b0aa8 -> sub_1e1ab1afc : 320 -> 340
~ sub_1e18b2180 -> sub_1e1ab31e8 : 1364 -> 1384
~ sub_1e19522cc -> sub_1e1b53348 : 516 -> 1008
~ sub_1e19a660c -> sub_1e1ba7874 : 828 -> 1200
~ sub_1e19a9e0c -> sub_1e1bab1e8 : 320 -> 612
~ sub_1e19a9f4c -> sub_1e1bab44c : 1344 -> 1312
~ sub_1e19aaf7c -> sub_1e1bac45c : 528 -> 736
~ sub_1e19ae498 -> sub_1e1bafa48 : 336 -> 312
CStrings:
+ "[corewifi] Non-app process is attempting to use CWFServiceTypeWiFiNetworkSharingApp, returning error"
+ "[corewifi] Non-appex process is attempting to use CWFServiceTypeWiFiNetworkSharingExtension, returning error"
+ "[corewifi] [wifi-network-sharing] Applying 'testable' ask-to-share (from app) request rate limit (%lu)"
+ "[corewifi] [wifi-network-sharing] Current network ask-to-share eligible, but proxcard is already presented for matching clientID (clientID=%{public}@, metadata=%{public}@, authLevel=%lu, knownNetwork=%{public}@)"
+ "[corewifi] [wifi-network-sharing] Resetting rate-limit cache for ask-to-share requests from appex (clientID=%{public}@, network=%{public}@)"

```
