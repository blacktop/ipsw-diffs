## uarpd

> `/usr/libexec/uarpd`

```diff

-1338.60.16.0.0
-  __TEXT.__text: 0x863e8
-  __TEXT.__auth_stubs: 0x970
-  __TEXT.__objc_stubs: 0x7b40
-  __TEXT.__objc_methlist: 0x6b18
-  __TEXT.__objc_methname: 0xb805
+1338.60.22.0.0
+  __TEXT.__text: 0x8723c
+  __TEXT.__auth_stubs: 0xa00
+  __TEXT.__objc_stubs: 0x7bc0
+  __TEXT.__objc_methlist: 0x6b48
+  __TEXT.__objc_methname: 0xb8a2
   __TEXT.__objc_classname: 0x1664
-  __TEXT.__objc_methtype: 0x25e6
-  __TEXT.__const: 0x130
-  __TEXT.__cstring: 0x8896
-  __TEXT.__oslogstring: 0x60c5
+  __TEXT.__objc_methtype: 0x2606
+  __TEXT.__const: 0x128
+  __TEXT.__cstring: 0x89e5
+  __TEXT.__oslogstring: 0x62a7
   __TEXT.__gcc_except_tab: 0x158
-  __TEXT.__unwind_info: 0x1a90
-  __DATA_CONST.__auth_got: 0x4c8
+  __TEXT.__unwind_info: 0x1aa8
+  __DATA_CONST.__auth_got: 0x510
   __DATA_CONST.__got: 0x490
-  __DATA_CONST.__const: 0xee0
-  __DATA_CONST.__cfstring: 0x44e0
+  __DATA_CONST.__const: 0xf18
+  __DATA_CONST.__cfstring: 0x4520
   __DATA_CONST.__objc_classlist: 0x4b0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x70

   __DATA_CONST.__objc_intobj: 0x3d8
   __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0xd420
-  __DATA.__objc_selrefs: 0x2600
-  __DATA.__objc_ivar: 0x910
+  __DATA.__objc_const: 0xd460
+  __DATA.__objc_selrefs: 0x2620
+  __DATA.__objc_ivar: 0x918
   __DATA.__objc_data: 0x2ee0
   __DATA.__data: 0x548
   __DATA.__bss: 0x1178
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  UUID: A18847DE-6178-3CD5-BD11-D6E00820A384
-  Functions: 3110
-  Symbols:   207
-  CStrings:  4387
+  UUID: E881038E-4E13-3684-8869-A1A16BDECFEB
+  Functions: 3123
+  Symbols:   216
+  CStrings:  4415
 
Symbols:
+ _nw_path_get_status
+ _nw_path_monitor_cancel
+ _nw_path_monitor_create
+ _nw_path_monitor_prohibit_interface_type
+ _nw_path_monitor_set_cancel_handler
+ _nw_path_monitor_set_queue
+ _nw_path_monitor_set_update_handler
+ _nw_path_monitor_start
+ _nw_path_uses_interface_type
CStrings:
+ "%s: Asset DENIED due to lack of network connetion %@"
+ "%s: Cancel Handler"
+ "%s: Could not serialize tatsu request"
+ "%s: Serialized tatsu request cannot be zero length"
+ "%s: Starting Network Monitor"
+ "%s: Update Handler"
+ "%s: asset uuid cannot be nil / zero length"
+ "%s: dropping for endpoint %@; Network = %@ "
+ "%s: endpoint %@; asset %@ has PMAP %@, Network = %@"
+ "%s: endpoint uuid cannot be nil / zero length"
+ "%s: network status %d "
+ "%s: network status satisified for Cellular = %@ for Wi-Fi = %@ for Wired = %@"
+ "%s: ticket count cannot be zero"
+ "-[UARPHostManager handleNetworkPathChange:]_block_invoke"
+ "-[UARPHostManager preflightOfferRestrictionByNetworkConnection:hostEndpoint:]"
+ "-[UARPHostManager startNetworkMonitor]_block_invoke"
+ "-[UARPPersonalizationEventManager personalizationNeeded:endpointUUID:tssServerURL:]"
+ "@\"NSObject<OS_nw_path_monitor>\""
+ "Cancelled"
+ "Cancelled - No Network"
+ "_hasNetwork"
+ "_monitor"
+ "containsPayloadWithMatchingTag:"
+ "handleNetworkPathChange:"
+ "preflightOfferRestrictionByNetworkConnection:hostEndpoint:"
+ "startNetworkMonitor"
+ "v16@?0@\"NSObject<OS_nw_path>\"8"
- "Could not serialize tatsu request %{public}@"

```
