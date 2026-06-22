## universalaccessd

> `/usr/sbin/universalaccessd`

```diff

-767.0.0.0.0
-  __TEXT.__text: 0xe60 sha256:5021f7eb5ecb414a06347c1fc29998f42857b5ca686bb9527a9fc95efdf26552
-  __TEXT.__auth_stubs: 0x220 sha256:96dda208637b5747a6dac2ed86e5a2535669e555a7c0574cbd805d4714603b59
-  __TEXT.__objc_stubs: 0xa0 sha256:8297f5baeda1026a6c486986d68fe412beb6a32376d74dfb70978736e8b7e513
+770.0.0.0.0
+  __TEXT.__text: 0x1414 sha256:21d32e7aee5b0241c582b855703d988b31fa323b01b6eacda7cca5b6e9e82f0f
+  __TEXT.__auth_stubs: 0x260 sha256:5875022444d71eec273dde1f09541f192b3d6212256cc9dee688721f34fa9955
+  __TEXT.__objc_stubs: 0x100 sha256:aed49960c379fee222a10aa414127f377ede60c6c5c12918c40cee7ed076f0ba
   __TEXT.__const: 0x20 sha256:6fa8a75fd74245fec47ccd9abc6cb761faacc07e7a4d67cc6045886655c97658
-  __TEXT.__cstring: 0xcf sha256:2e14d2f73da1166a866abde3af850b83f642150584f97112e6b9e02239bf6e81
-  __TEXT.__oslogstring: 0x2de sha256:a630d603270ed8cd12cf30a342c651339ff75b33b7d9ed9f6fb678a04e4383e9
-  __TEXT.__objc_methname: 0x5a sha256:0eda71cf911d87360371ad7124d3894517f7f24e3254464f10ddb9c02eb0bece
-  __TEXT.__unwind_info: 0x80 sha256:1e0e011205a059af43a516d08fd15242d91ca02ee39c89f61b3d05722c1a397f
-  __DATA_CONST.__const: 0x258 sha256:bb7496e7f181ec3018a2b746d20f4d61f442a8c5885a74aaa906d9fc9475f4ee
-  __DATA_CONST.__cfstring: 0x40 sha256:43abc71e6e4edc004bc28c984d6211d7917c59c7ca2c3701c917cfd7783fa90f
+  __TEXT.__cstring: 0x15d sha256:14e0a9c2aa319273d6804d9520f2d693c9f0fccef5f8b35d3972b7b799c26d25
+  __TEXT.__oslogstring: 0x373 sha256:1801102bda7e5d4537115c230708e53cd1be5337d57dc6c189bba9118ac6b9f8
+  __TEXT.__objc_methname: 0x8f sha256:1a5b88609e2b840888441e06ddfbc9ba67941f8f7237142a494eec509ccaba13
+  __TEXT.__unwind_info: 0x90 sha256:3e9ad4bcb09bbdc69a79f9d6b817fe065c758ace9d3c5fd54296ef2803c8a2ee
+  __DATA_CONST.__const: 0x2a8 sha256:016dd1cba4d85c7ebdb52f685a376900981c818762361e1d139f221a0a8f7c51
+  __DATA_CONST.__cfstring: 0xc0 sha256:999fada53d56cc23dc579b116d2744087c9420f6b6025d1750a38fbad1f4cfdc
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:1fa65ffcccc24c72d5d7f804a2be05ae57dfbb8769ffb33c4272ed6795b7e61c
-  __DATA_CONST.__auth_got: 0x118 sha256:fbea4cabc0d59e9677f04766754ab8e0b6afc81ffa298d9305c0bf27359a702a
-  __DATA_CONST.__got: 0x60 sha256:9dd1d8760ac425cb05efd53df988a794b9454fca5e319f5097c828743d4ce541
-  __DATA.__objc_selrefs: 0x28 sha256:4321858e3376c56197fda59473c15098545dc88c76fd94bec00bab39f7400eec
+  __DATA_CONST.__auth_got: 0x138 sha256:b070d35edd416f3377cd6563b76486ec963d3c2696d1df3143d2675cac2bb930
+  __DATA_CONST.__got: 0x78 sha256:d04bc2d44f3e20baf7f1ffa9711f573dacb4e5f793b69ac605334d02b35dd261
+  __DATA.__objc_selrefs: 0x40 sha256:73f9ca281730b79b23864029fcdc889fde0b5946dcc19234fd6ddbe8ae37169c
   __DATA.__bss: 0x20 sha256:66687aadf862bd776c8fc18b8e9f8e20089714856ee233b3902a591d0d5f2925
   __CGPreLoginApp.__cgpreloginapp: 0x0
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
+  - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/PrivateFrameworks/UniversalAccess.framework/Versions/A/Frameworks/UAEHCommon.framework/Versions/A/Libraries/libUADaemon.dylib
   - /System/Library/PrivateFrameworks/UniversalAccess.framework/Versions/A/Frameworks/UniversalAccessCore.framework/Versions/A/UniversalAccessCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A4C10D6D-2029-36B1-BD86-310B4C1A351A
-  Functions: 18
-  Symbols:   51
-  CStrings:  29
+  UUID: CC95770C-DA62-3226-848B-D8B934A54BA8
+  Functions: 22
+  Symbols:   58
+  CStrings:  43
 
Symbols:
+ _OBJC_CLASS_$_NSNotificationCenter
+ _OBJC_CLASS_$_NSNumber
+ _SecTaskCopyValueForEntitlement
+ _SecTaskCreateWithAuditToken
+ _kCFAllocatorDefault
+ _objc_opt_class
+ _objc_opt_isKindOfClass
CStrings:
+ "_UADInternalDFRHUDHiding"
+ "_UADInternalDFRHUDShowing"
+ "_UADXDaemonQuit: rejecting unauthorized caller"
+ "_UADXZoomWindowQuit: rejecting unauthorized caller"
+ "_UADXZoomWindowZoom: rejecting unauthorized caller"
+ "boolValue"
+ "com.apple.private.accessibility.visuals"
+ "com.apple.private.security.storage.universalaccess"
+ "defaultCenter"
+ "postNotificationName:object:"

```
