## uarpd

> `/usr/libexec/uarpd`

```diff

-1338.40.19.0.0
-  __TEXT.__text: 0x84bf4
+1338.40.28.0.0
+  __TEXT.__text: 0x85d40
   __TEXT.__auth_stubs: 0x960
-  __TEXT.__objc_stubs: 0x7a20
-  __TEXT.__objc_methlist: 0x6a90
-  __TEXT.__objc_methname: 0xb691
+  __TEXT.__objc_stubs: 0x7b00
+  __TEXT.__objc_methlist: 0x6af8
+  __TEXT.__objc_methname: 0xb783
   __TEXT.__objc_classname: 0x1664
   __TEXT.__objc_methtype: 0x25e6
   __TEXT.__const: 0x130
-  __TEXT.__cstring: 0x8783
-  __TEXT.__oslogstring: 0x5d75
+  __TEXT.__cstring: 0x8896
+  __TEXT.__oslogstring: 0x5fe9
   __TEXT.__gcc_except_tab: 0x158
-  __TEXT.__unwind_info: 0x1a80
+  __TEXT.__unwind_info: 0x1a90
   __DATA_CONST.__auth_got: 0x4c0
   __DATA_CONST.__got: 0x490
   __DATA_CONST.__const: 0xee0
-  __DATA_CONST.__cfstring: 0x44a0
+  __DATA_CONST.__cfstring: 0x44e0
   __DATA_CONST.__objc_classlist: 0x4b0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x70

   __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA.__objc_const: 0xd420
-  __DATA.__objc_selrefs: 0x25b8
+  __DATA.__objc_selrefs: 0x25e8
   __DATA.__objc_ivar: 0x910
   __DATA.__objc_data: 0x2ee0
   __DATA.__data: 0x548

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  UUID: D68BBF24-0A4E-30FE-BEE7-45111AA28D16
-  Functions: 3098
+  UUID: 83A363AD-C55B-3DF5-BE71-4E517679B8ED
+  Functions: 3107
   Symbols:   206
-  CStrings:  4357
+  CStrings:  4381
 
CStrings:
+ "%s: Asset %@ DENIED due to Deployment"
+ "%s: Asset %@ DENIED due to OS Version"
+ "%s: Asset is %salready staged"
+ "%s: Asset: %@; %@ Deployment BLOCKED by %@"
+ "%s: Asset: %@; Deployment %@ BLOCKED by %@"
+ "%s: Asset: %@; Deployment Percentage Rule %@"
+ "%s: Asset: %@; Deployment Rule until %@ is in the past; today is %@"
+ "%s: Asset: %@; My deployment percent is %lu, which is lower than the deployment rule %lu percent "
+ "%s: Asset: %@; Rule country code %@ does not match country code self %@"
+ "%s: No deployment percentage rules for asset %@"
+ "%s: Staged firmware version is %@ for endpoint %@"
+ "%s: endpoint %@Available firmware version %@ is not greater than Staged firmware version %@ "
+ "-[UARPHostManager preflightAvailableGreaterThanStaged:hostEndpoint:]"
+ "-[UARPHostManager preflightOfferRestrictionByDeploymentCountry:]"
+ "-[UARPHostManager preflightOfferRestrictionByDeploymentPercentage:]"
+ "<today is %@, my deployment percentage is %lu>"
+ "calculateDeploymentPercent:"
+ "calculateWeeklyDeploymentDay:"
+ "country code %@ today %@>"
+ "preflightAvailableGreaterThanStaged:hostEndpoint:"
+ "preflightOfferRestrictionByDeployment:"
+ "preflightOfferRestrictionByDeploymentCountry:"
+ "preflightOfferRestrictionByDeploymentPercentage:"
- "%s: Asset DENIED due to OS Version %@"

```
