## UsageTracking

> `/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTracking`

```diff

-388.0.0.0.0
-  __TEXT.__text: 0x298c8
+389.0.0.0.0
+  __TEXT.__text: 0x298cc
   __TEXT.__auth_stubs: 0x5b0
   __TEXT.__objc_methlist: 0x1618
   __TEXT.__const: 0x100

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BC34BC39-AFF9-33FB-8AE3-15D22F292279
+  UUID: 91652625-4D11-3554-9204-515D2E6B17C2
   Functions: 591
   Symbols:   2396
   CStrings:  1326
Functions:
~ -[USUsageAccumulator _accumulateDeviceBacklightWithIsBacklit:timestamp:] : 800 -> 796
~ -[USUsageAccumulator _accumulateApplication:timestamp:starting:isUsageTrusted:] : 548 -> 552
~ -[USUsageAccumulator _accumulateWebDomain:bundleIdentifier:timestamp:starting:isUsageTrusted:] : 676 -> 684
~ -[USUsageAccumulator _accumulateMediaNowPlayingWithTimestamp:starting:] : 240 -> 236

```
