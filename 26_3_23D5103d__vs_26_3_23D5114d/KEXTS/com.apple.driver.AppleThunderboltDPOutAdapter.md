## com.apple.driver.AppleThunderboltDPOutAdapter

> `com.apple.driver.AppleThunderboltDPOutAdapter`

```diff

-871.0.0.0.0
-  __TEXT.__cstring: 0x1c89d
-  __TEXT_EXEC.__text: 0x48ca8
+873.0.0.0.0
+  __TEXT.__cstring: 0x1c8d0
+  __TEXT_EXEC.__text: 0x48dc0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x308
   __DATA.__common: 0x178

   __DATA_CONST.__mod_term_func: 0x48
   __DATA_CONST.__const: 0x4d18
   __DATA_CONST.__kalloc_type: 0x240
-  UUID: 589184A3-60EF-3F7C-95F9-AD6CACE54EF2
+  UUID: FA2E36B2-2834-37B4-848E-8B79C13BB459
   Functions: 610
   Symbols:   0
-  CStrings:  1068
+  CStrings:  1070
 
Functions:
~ sub_fffffe0009ed6514 -> sub_fffffe0009ed83a4 : 608 -> 756
~ sub_fffffe0009ed6ac4 -> sub_fffffe0009ed89e8 : 216 -> 280
~ __ZN30AppleThunderboltDPOutAdapterOS24updateEstimatedBandwidthEv : 1724 -> 1792
CStrings:
+ "%lldus AppleThunderboltDPOutAdapterOS<%p>::setLateSleepFlagsInternal - disable reactivateOnWake\n"
+ "%lldus AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::updateEstimatedBandwidth - done, fCachedEstimatedBW = %u, estimated_bandwidth = %u, status = 0x%08x\n"
+ "12111112122212121112222221111111111111222222221112122222111111111121111111112222112222222"
+ "Cached Estimated Bandwidth"
+ "Cached Local DP Capabilities Presleep"
- "%lldus AppleThunderboltDPOutAdapterOS::setLateSleepFlagsInternal - disable reactivateOnWake\n"
- "%lldus AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::updateEstimatedBandwidth - done, estimated_bandwidth_100_megabit_scale = %u, estimated_bandwidth = %u, status = 0x%08x\n"
- "1211111212221212111222222111111111111122222222111212222211111111112111111111222211222222"

```
