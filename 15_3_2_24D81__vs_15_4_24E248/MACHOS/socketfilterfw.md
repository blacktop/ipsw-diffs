## socketfilterfw

> `/usr/libexec/ApplicationFirewall/socketfilterfw`

```diff

-280.80.2.0.0
-  __TEXT.__text: 0x1cb80
-  __TEXT.__auth_stubs: 0xfe0
-  __TEXT.__objc_stubs: 0x1a60
-  __TEXT.__objc_methlist: 0x608
-  __TEXT.__const: 0xf0
-  __TEXT.__oslogstring: 0x25a4
-  __TEXT.__cstring: 0x3b2a
+305.0.0.0.0
+  __TEXT.__text: 0x1cb8c
+  __TEXT.__auth_stubs: 0xff0
+  __TEXT.__objc_stubs: 0x1aa0
+  __TEXT.__objc_methlist: 0x794
+  __TEXT.__const: 0x100
+  __TEXT.__oslogstring: 0x253d
+  __TEXT.__cstring: 0x3b37
   __TEXT.__objc_classname: 0xaf
-  __TEXT.__objc_methname: 0x1c9b
+  __TEXT.__objc_methname: 0x1cf9
   __TEXT.__objc_methtype: 0x3a0
   __TEXT.__gcc_except_tab: 0x1c
-  __TEXT.__unwind_info: 0x458
-  __DATA_CONST.__auth_got: 0x800
-  __DATA_CONST.__got: 0x1d8
-  __DATA_CONST.__auth_ptr: 0x8
+  __TEXT.__unwind_info: 0x448
+  __DATA_CONST.__auth_got: 0x808
+  __DATA_CONST.__got: 0x1d0
+  __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x530
   __DATA_CONST.__cfstring: 0xf60
   __DATA_CONST.__objc_classlist: 0x28

   __DATA_CONST.__objc_intobj: 0xa8
   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0x1090
-  __DATA.__objc_selrefs: 0x750
-  __DATA.__objc_ivar: 0x70
+  __DATA.__objc_const: 0xe00
+  __DATA.__objc_selrefs: 0x7f0
+  __DATA.__objc_ivar: 0x74
   __DATA.__objc_data: 0x190
-  __DATA.__data: 0x620
+  __DATA.__data: 0x820
   __DATA.__common: 0x1c0
   __DATA.__bss: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
+  - /System/Library/Frameworks/Network.framework/Versions/A/Network
   - /System/Library/Frameworks/NetworkExtension.framework/Versions/A/NetworkExtension
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/Versions/A/SystemConfiguration

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E977415E-5805-3BD5-87B4-2F831795F43B
-  Functions: 431
-  Symbols:   326
-  CStrings:  1216
+  UUID: 14CD0146-290F-32DB-AC25-75D3FC21E623
+  Functions: 435
+  Symbols:   327
+  CStrings:  1221
 
Symbols:
+ _nw_endpoint_create_address_from_string
CStrings:
+ "0"
+ "5353"
+ "::"
+ ":h"
+ "Missing observer for not nil filterConfiguration"
+ "TB,V_filterConfigurationObserver"
+ "_filterConfigurationObserver"
+ "filterConfigurationObserver"
+ "processPathFrom:withProcessID:"
+ "setFilterConfigurationObserver:"
+ "stringByRemovingPercentEncoding"
- "Bootstrap Firewall with globalState: %lu"
- "Keeping the firewall off but updating the vendor config"
- "Turning on the firewall and updating the vendor config"
- "addNewFilterRuleFor:"
- "bootstrapFirewallWithCompletionHandler:"
- "processPathFrom:withPocessID:"

```
