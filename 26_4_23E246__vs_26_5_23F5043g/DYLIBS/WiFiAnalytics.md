## WiFiAnalytics

> `/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`

```diff

-795.21.4.3.0
-  __TEXT.__text: 0x14cb10
+805.4.0.0.0
+  __TEXT.__text: 0x14c850
   __TEXT.__auth_stubs: 0x1010
-  __TEXT.__objc_methlist: 0xfe38
+  __TEXT.__objc_methlist: 0xfe28
   __TEXT.__const: 0x390
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__cstring: 0x13934
-  __TEXT.__oslogstring: 0x1076c
+  __TEXT.__cstring: 0x138f0
+  __TEXT.__oslogstring: 0x106fa
   __TEXT.__constg_swiftt: 0x1e0
   __TEXT.__swift5_typeref: 0x145
   __TEXT.__swift5_reflstr: 0xb1

   __TEXT.__unwind_info: 0x3018
   __TEXT.__eh_frame: 0x398
   __TEXT.__objc_classname: 0xf79
-  __TEXT.__objc_methname: 0x2109b
+  __TEXT.__objc_methname: 0x21077
   __TEXT.__objc_methtype: 0x3fb4
-  __TEXT.__objc_stubs: 0xe3a0
+  __TEXT.__objc_stubs: 0xe380
   __DATA_CONST.__got: 0x7a0
   __DATA_CONST.__const: 0x2118
   __DATA_CONST.__objc_classlist: 0x438
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x87f0
+  __DATA_CONST.__objc_selrefs: 0x87e8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x318
-  __DATA_CONST.__objc_arraydata: 0x8e0
+  __DATA_CONST.__objc_arraydata: 0x8e8
   __AUTH_CONST.__auth_got: 0x818
   __AUTH_CONST.__const: 0x1450
   __AUTH_CONST.__cfstring: 0xe660

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: A6D5EB72-A5BB-33E9-8287-7A56DDC60F66
-  Functions: 5884
-  Symbols:   16211
-  CStrings:  12590
+  UUID: 1901DDD6-231D-36EA-AF31-1F2783E887D6
+  Functions: 5883
+  Symbols:   16208
+  CStrings:  12586
 
Symbols:
+ GCC_except_table100
+ GCC_except_table102
+ GCC_except_table104
+ GCC_except_table108
+ GCC_except_table142
+ GCC_except_table159
+ GCC_except_table161
+ GCC_except_table173
+ GCC_except_table179
+ GCC_except_table185
+ GCC_except_table191
+ GCC_except_table197
+ GCC_except_table280
+ GCC_except_table85
+ GCC_except_table90
+ GCC_except_table96
+ GCC_except_table98
- -[WADeviceAnalyticsClient updateBSSIDForCachedFaultsIfNeeded:]
- GCC_except_table105
- GCC_except_table107
- GCC_except_table109
- GCC_except_table111
- GCC_except_table150
- GCC_except_table158
- GCC_except_table160
- GCC_except_table281
- GCC_except_table86
- GCC_except_table91
- GCC_except_table97
- GCC_except_table99
- _objc_msgSend$updateBSSIDForCachedFaultsIfNeeded:
Functions:
- -[WADeviceAnalyticsClient updateBSSIDForCachedFaultsIfNeeded:]
~ -[WADeviceAnalyticsClient asyncAddEvent:andDeferReclaimMem:andRunPostProcessing:uponCompletionDo:] : 244 -> 232
~ ___83-[WADeviceAnalyticsClient event:andDeferReclaimMem:andRunPostProcessing:withError:]_block_invoke : 160 -> 152
~ -[WADeviceAnalyticsClient setCachedParamsWithBssid:ssid:] : 828 -> 972
~ ___97-[WADeviceAnalyticsClient joinEventOnBssid:ssid:at:with:andDeferReclaimMem:andRunPostProcessing:]_block_invoke : 436 -> 288
CStrings:
+ "WiFiAnalytics-805.4 Mar 20 2026 22:46:49"
- "%{public}s::%d:BSSID update for event: %@"
- "%{public}s::%d:Resetting AnalyticsProcessor bssidForCachedFaults to nil"
- "-[WADeviceAnalyticsClient updateBSSIDForCachedFaultsIfNeeded:]"
- "WiFiAnalytics-795.21.4.3 Mar  6 2026 18:33:20"
- "updateBSSIDForCachedFaultsIfNeeded:"

```
