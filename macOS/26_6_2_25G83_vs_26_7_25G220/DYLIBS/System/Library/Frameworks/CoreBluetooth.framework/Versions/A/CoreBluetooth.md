## CoreBluetooth

> `/System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth`

```diff

-196.5.0.0.0
-  __TEXT.__text: 0xbba14
+196.5.0.3.0
+  __TEXT.__text: 0xbc0c4
   __TEXT.__auth_stubs: 0x11f0
   __TEXT.__objc_methlist: 0x9a5c
-  __TEXT.__const: 0x27eb
+  __TEXT.__const: 0x282b
   __TEXT.__oslogstring: 0x265e
-  __TEXT.__cstring: 0x14acd
+  __TEXT.__cstring: 0x14bcd
   __TEXT.__gcc_except_tab: 0x2cd8
   __TEXT.__ustring: 0x82
   __TEXT.__unwind_info: 0x23a8

   __TEXT.__objc_methtype: 0x241b
   __TEXT.__objc_stubs: 0xb4e0
   __DATA_CONST.__got: 0x388
-  __DATA_CONST.__const: 0x43b8
+  __DATA_CONST.__const: 0x46b0
   __DATA_CONST.__objc_classlist: 0x1f8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xe8

   __DATA_CONST.__objc_arraydata: 0x130
   __AUTH_CONST.__auth_got: 0x908
   __AUTH_CONST.__const: 0x1380
-  __AUTH_CONST.__cfstring: 0xccc0
+  __AUTH_CONST.__cfstring: 0xce80
   __AUTH_CONST.__objc_const: 0x111e8
-  __AUTH_CONST.__objc_intobj: 0x930
+  __AUTH_CONST.__objc_intobj: 0x960
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0xa0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 4225
-  Symbols:   7825
-  CStrings:  8297
+  Symbols:   7833
+  CStrings:  8318
 
Symbols:
+ _CBProductInfoB518
+ _CBProductInfoB522
+ _CBProductInfoB790
+ _CBProductInfoB790CH
+ _CBProductInfoB868CHE
+ _CBProductInfoB868CHM
+ _CBProductInfoB868E
+ _CBProductInfoB868M
Functions:
~ sub_199b5d4d8 -> sub_199b534d8 : 184 -> 220
~ sub_199b5d5c4 -> sub_199b535e8 : 176 -> 192
~ sub_199b5d72c -> sub_199b53760 : 184 -> 220
~ sub_199b5d7e4 -> sub_199b5383c : 184 -> 220
~ sub_199b5f2d0 -> sub_199b5534c : 184 -> 220
~ -[CBPowerSource description] : 3244 -> 3408
~ -[CBPowerSource hasAllComponents] : 248 -> 252
~ +[CBAccessoryLogging getProductNameFromProductID:] : 788 -> 832
~ _CBProductIDToString : 868 -> 1032
~ +[CBProductInfo productInfoWithProductID:] : 2476 -> 2796
~ _CBDiscoveryTypeFromCString : 2036 -> 2124
~ _CBDiscoveryTypeFromString : 2024 -> 2112
~ _CBNearbyActionTypeAllCases : 168 -> 240
~ _CBNearbyActionTypeFromString : 2068 -> 2148
~ _CBProductIDToString : 884 -> 1056
~ -[CBDevice _parseNearbyActionPtr:end:] : 2532 -> 2776
~ _CBProductIDFromNSString : 1152 -> 1264
CStrings:
+ "ATVRemote1,5"
+ "AirPods3,5"
+ "B522 FW"
+ "B790 SW"
+ "B868 SW"
+ "Beats Headphones"
+ "Device1,21761"
+ "Device1,8234"
+ "Device1,8236"
+ "Device1,8238"
+ "Device1,8240"
+ "Device1,8241"
+ "Device1,8242"
+ "Device1,8246"
+ "Device1,8247"
+ "Device1,8248"
+ "HomeAccessory"
+ "J490Setup"
+ "J491Setup"
+ "MobileBluetooth-196.5.0.3"
+ "PowerBeats"
+ "Powerbeats"
- "MobileBluetooth-196.5"
```
