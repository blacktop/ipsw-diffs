## uarpd

> `/usr/libexec/uarpd`

```diff

-1338.40.31.0.1
-  __TEXT.__text: 0x85e60
-  __TEXT.__auth_stubs: 0x960
-  __TEXT.__objc_stubs: 0x7b00
-  __TEXT.__objc_methlist: 0x6af8
-  __TEXT.__objc_methname: 0xb783
+1338.60.16.0.0
+  __TEXT.__text: 0x863e8
+  __TEXT.__auth_stubs: 0x970
+  __TEXT.__objc_stubs: 0x7b40
+  __TEXT.__objc_methlist: 0x6b18
+  __TEXT.__objc_methname: 0xb805
   __TEXT.__objc_classname: 0x1664
   __TEXT.__objc_methtype: 0x25e6
   __TEXT.__const: 0x130
   __TEXT.__cstring: 0x8896
-  __TEXT.__oslogstring: 0x6029
+  __TEXT.__oslogstring: 0x60c5
   __TEXT.__gcc_except_tab: 0x158
   __TEXT.__unwind_info: 0x1a90
-  __DATA_CONST.__auth_got: 0x4c0
+  __DATA_CONST.__auth_got: 0x4c8
   __DATA_CONST.__got: 0x490
   __DATA_CONST.__const: 0xee0
   __DATA_CONST.__cfstring: 0x44e0

   __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA.__objc_const: 0xd420
-  __DATA.__objc_selrefs: 0x25e8
+  __DATA.__objc_selrefs: 0x2600
   __DATA.__objc_ivar: 0x910
   __DATA.__objc_data: 0x2ee0
   __DATA.__data: 0x548

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
+  - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/UARPAssetManager.framework/UARPAssetManager
   - /System/Library/PrivateFrameworks/UARPKit.framework/UARPKit
   - /usr/lib/libMobileGestalt.dylib

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  UUID: DC4E66D2-4170-345D-9633-1FECA9162D2A
-  Functions: 3107
-  Symbols:   206
-  CStrings:  4382
+  UUID: A18847DE-6178-3CD5-BD11-D6E00820A384
+  Functions: 3110
+  Symbols:   207
+  CStrings:  4387
 
Symbols:
+ _MKBGetDeviceLockState
CStrings:
+ "%s: UARP: current keybag state <%d> for apple connect based personalization"
+ "%s: UARP: unsupported keybag state <%d> for apple connect based personalization"
+ "addManifestEpoch:componentTag:tatsuTicket:keyName:"
+ "addProvisioining:componentTag:tatsuTicket:keyName:"
+ "updateDefaultPropertyValue:"

```
