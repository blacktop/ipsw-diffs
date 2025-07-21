## UsageTracking

> `/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTracking`

```diff

-377.5.1.0.0
-  __TEXT.__text: 0x27bac
+377.5.2.0.0
+  __TEXT.__text: 0x27bb0
   __TEXT.__auth_stubs: 0x5b0
   __TEXT.__objc_methlist: 0x1550
   __TEXT.__const: 0x100

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 94059313-96BD-3382-A7E2-15B003569580
+  UUID: 1D8B6A2D-590A-36DB-AF0F-4DE47773AD03
   Functions: 560
   Symbols:   2314
   CStrings:  1281
Functions:
~ -[USUsageAccumulator _accumulateDeviceBacklightWithIsBacklit:timestamp:] : 800 -> 796
~ -[USUsageAccumulator _accumulateApplication:timestamp:starting:isUsageTrusted:] : 548 -> 552
~ -[USUsageAccumulator _accumulateWebDomain:bundleIdentifier:timestamp:starting:isUsageTrusted:] : 676 -> 684
~ -[USUsageAccumulator _accumulateMediaNowPlayingWithTimestamp:starting:] : 240 -> 236

```
