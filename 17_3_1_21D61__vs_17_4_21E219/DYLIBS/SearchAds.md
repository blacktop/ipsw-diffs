## SearchAds

> `/System/Library/PrivateFrameworks/SearchAds.framework/SearchAds`

```diff

-608.0.0.0.0
-  __TEXT.__text: 0xe1bc
+618.0.0.0.0
+  __TEXT.__text: 0xe778
   __TEXT.__auth_stubs: 0x4b0
-  __TEXT.__objc_methlist: 0x11d8
+  __TEXT.__objc_methlist: 0x1208
   __TEXT.__const: 0x88
   __TEXT.__gcc_except_tab: 0x2e8
-  __TEXT.__cstring: 0x24e0
+  __TEXT.__cstring: 0x2688
   __TEXT.__oslogstring: 0x1b
-  __TEXT.__unwind_info: 0x438
+  __TEXT.__unwind_info: 0x43c
   __TEXT.__objc_classname: 0x1d2
-  __TEXT.__objc_methname: 0x43a1
-  __TEXT.__objc_methtype: 0x82e
-  __TEXT.__objc_stubs: 0x3300
-  __DATA_CONST.__got: 0x60
+  __TEXT.__objc_methname: 0x448d
+  __TEXT.__objc_methtype: 0x83c
+  __TEXT.__objc_stubs: 0x33a0
+  __DATA_CONST.__got: 0x70
   __DATA_CONST.__const: 0x3f8
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2110
-  __DATA_CONST.__objc_selrefs: 0x1038
-  __AUTH_CONST.__cfstring: 0x21e0
+  __DATA_CONST.__objc_const: 0x2140
+  __DATA_CONST.__objc_selrefs: 0x1068
+  __DATA_CONST.__objc_classrefs: 0x1d8
+  __DATA_CONST.__objc_superrefs: 0x88
+  __AUTH_CONST.__cfstring: 0x23a0
   __AUTH_CONST.__objc_const: 0x6f0
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__auth_got: 0x268
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_classrefs: 0x1d0
-  __DATA.__objc_superrefs: 0x88
-  __DATA.__objc_ivar: 0x1bc
+  __DATA.__objc_ivar: 0x1c0
   __DATA.__data: 0x1e0
   __DATA_DIRTY.__objc_data: 0x500
   __DATA_DIRTY.__bss: 0x40

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 406
-  Symbols:   1683
-  CStrings:  1204
+  Functions: 410
+  Symbols:   1700
+  CStrings:  1229
 
Symbols:
+ -[ADAppAdvertisement appBinaryTraits]
+ -[ADAppAdvertisement setAppBinaryTraits:]
+ -[ADSearchObject checkForNonWKDiscardOverrides:forAdamID:]
+ -[ADSearchObject filterAdsForNonWK:]
+ _APDefaultsBundleID
+ _OBJC_CLASS_$_ASDAppCapabilities
+ _OBJC_IVAR_$_ADAppAdvertisement._appBinaryTraits
+ ___36-[ADSearchObject setAdvertisements:]_block_invoke.44
+ ___kCFBooleanFalse
+ _objc_msgSend$appBinaryTraits
+ _objc_msgSend$checkForNonWKDiscardOverrides:forAdamID:
+ _objc_msgSend$componentsSeparatedByString:
+ _objc_msgSend$filterAdsForNonWK:
+ _objc_msgSend$isCapableOfAction:capabilities:
- ___36-[ADSearchObject setAdvertisements:]_block_invoke.20
CStrings:
+ "\x05"
+ ","
+ "App Binary Traits: %@"
+ "App discard state after overrides check: isEntitledApp: %d isDMAEligible: %d"
+ "App discard state for %@: isEntitledApp: %d isDMAEligible: %d"
+ "B28@0:8B16@20"
+ "Discarding ad with adamID: %@ "
+ "Discarding ad with adamid: %@ based off overrides."
+ "T@\"NSArray\",&,N,V_appBinaryTraits"
+ "T@\"NSString\",?,R,C"
+ "_appBinaryTraits"
+ "appBinaryTraits"
+ "checkForNonWKDiscardOverrides:forAdamID:"
+ "com.apple.adplatforms.nonWebKitAdverts"
+ "componentsSeparatedByString:"
+ "enableDMAEligible"
+ "enableNonWKOverrides"
+ "filterAdsForNonWK:"
+ "is-custom-browser-engine-app"
+ "isCapableOfAction:capabilities:"
+ "nonWKAppsSearchAds"
+ "placement"
+ "setAppBinaryTraits:"
+ "uses-non-webkit-browser-engine"
+ "wasServed"
- "\x04"

```
