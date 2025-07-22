## nfcd

> `/usr/libexec/nfcd`

```diff

-360.37.0.0.0
-  __TEXT.__text: 0x2765f8
+360.38.0.0.0
+  __TEXT.__text: 0x2798e0
   __TEXT.__auth_stubs: 0x1840
   __TEXT.__delay_stubs: 0x370
   __TEXT.__delay_helper: 0x120c
-  __TEXT.__objc_stubs: 0xd400
-  __TEXT.__objc_methlist: 0x9c58
+  __TEXT.__objc_stubs: 0xd460
+  __TEXT.__objc_methlist: 0x9c98
   __TEXT.__const: 0x1390
-  __TEXT.__objc_methname: 0x17c68
-  __TEXT.__cstring: 0x2f490
+  __TEXT.__objc_methname: 0x17d9d
+  __TEXT.__cstring: 0x2f6d2
   __TEXT.__objc_classname: 0x1d5f
-  __TEXT.__objc_methtype: 0x563a
-  __TEXT.__oslogstring: 0x2680d
-  __TEXT.__unwind_info: 0x2c30
+  __TEXT.__objc_methtype: 0x567d
+  __TEXT.__oslogstring: 0x2699a
+  __TEXT.__unwind_info: 0x2c50
   __DATA_CONST.__auth_got: 0xcc8
   __DATA_CONST.__got: 0x5d8
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__const: 0x83e0
-  __DATA_CONST.__cfstring: 0x11040
+  __DATA_CONST.__cfstring: 0x110a0
   __DATA_CONST.__objc_classlist: 0x628
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x390
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x1e8
-  __DATA_CONST.__objc_superrefs: 0x468
-  __DATA_CONST.__objc_intobj: 0x77d0
+  __DATA_CONST.__objc_superrefs: 0x470
+  __DATA_CONST.__objc_intobj: 0x7848
   __DATA_CONST.__objc_arraydata: 0x1d88
   __DATA_CONST.__objc_arrayobj: 0x2b8
   __DATA_CONST.__objc_dictobj: 0xfa0
-  __DATA.__objc_const: 0x14898
-  __DATA.__objc_selrefs: 0x55a8
-  __DATA.__objc_ivar: 0x109c
+  __DATA.__objc_const: 0x14920
+  __DATA.__objc_selrefs: 0x55d8
+  __DATA.__objc_ivar: 0x10ac
   __DATA.__objc_data: 0x3d90
   __DATA.__data: 0x2b94
-  __DATA.__bss: 0x278
+  __DATA.__bss: 0x288
   __DATA.__common: 0x12
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A9634131-FF22-3FB2-A3E3-B7FA357F2B40
-  Functions: 4148
+  UUID: CF6EF938-FFE2-3B7C-BD99-3EF346DAD331
+  Functions: 4155
   Symbols:   592
-  CStrings:  14564
+  CStrings:  14592
 
CStrings:
+ "%c[%{public}s %{public}s]:%i AID %{public}@ for pass %{public}@ does not exist; ignoring"
+ "%c[%{public}s %{public}s]:%i Applet is setup in express but express config is not enabled; aid=%{public}@"
+ "%c[%{public}s %{public}s]:%i Burnout cleared, coolOffTimerWasRunning=%d"
+ "%c[%{public}s %{public}s]:%i Method only available on internal builds"
+ "%c[%{public}s %{public}s]:%i No change; skipping update"
+ "%c[%{public}s %{public}s]:%i Setting emulation type based on nftool command to: %d"
+ "%c[%{public}s %{public}s]:%i Skipping some validation when activating applets for test use"
+ "@28@0:8@16i24"
+ "Fail to setup transaction codes"
+ "Keys not supported on applet"
+ "NFCD built from (B&I) Stockholm_Base-360.38"
+ "NF_expressConfigHash"
+ "Vv36@0:8@\"NSArray\"16I24@?<v@?@\"NSArray\"@\"NSError\">28"
+ "_activeApplets"
+ "_effectivePassConfigHash"
+ "_effectiveRestrictedPassIDListHash"
+ "_lastIsLegacyWalletBehaviour"
+ "_loadStoredAppletsOnce"
+ "_selectCRSandReturnGlobalUpdateCounter:"
+ "activateAppletsForTest:"
+ "enableExpressForKeys:onApplet:%@ enable:%d authorization:%d uid:"
+ "handleReaderBurnoutCleared:"
+ "setActiveAppletsForTest:withCardType:"
+ "setActiveAppletsForTest:withCardType:completion:"
+ "setupContactlessTransactionCodes:wiredTransactionCodes:forIdentifier:onApplet:%@ authorization:%d uid:"
- "%c[%{public}s %{public}s]:%i This invocation is immutable and will not change state of applets"
- "%c[%{public}s %{public}s]:%i no applet exist for AID: %{public}@  ignoring"
- "NFCD built from (B&I) Stockholm_Base-360.37"
- "loadStoredApplets"

```
