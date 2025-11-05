## IntelligentRouting

> `/System/Library/PrivateFrameworks/IntelligentRouting.framework/Versions/A/IntelligentRouting`

```diff

 96.0.6.0.1
-  __TEXT.__text: 0x9f10
+  __TEXT.__text: 0x9f14
   __TEXT.__auth_stubs: 0x230
-  __TEXT.__objc_methlist: 0xdc8
+  __TEXT.__objc_methlist: 0xfec
   __TEXT.__const: 0x68
   __TEXT.__cstring: 0xdb7
   __TEXT.__gcc_except_tab: 0x80
   __TEXT.__oslogstring: 0x975
-  __TEXT.__unwind_info: 0x308
+  __TEXT.__unwind_info: 0x310
   __TEXT.__objc_classname: 0x15d
   __TEXT.__objc_methname: 0x183c
   __TEXT.__objc_methtype: 0x44a

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5b0
+  __DATA_CONST.__objc_selrefs: 0x640
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x80
   __AUTH_CONST.__auth_got: 0x128
   __AUTH_CONST.__const: 0x110
   __AUTH_CONST.__cfstring: 0x1080
-  __AUTH_CONST.__objc_const: 0x1c30
+  __AUTH_CONST.__objc_const: 0x1838
   __AUTH.__objc_data: 0x500
   __DATA.__objc_ivar: 0xc4
   __DATA.__data: 0x248

   - /System/Library/PrivateFrameworks/IntelligentRoutingServices.framework/Versions/A/IntelligentRoutingServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F1521A96-E84C-33E1-8CF7-5113C2D59FAB
-  Functions: 303
-  Symbols:   747
+  UUID: 0CA1529E-DC68-309E-8621-DE972A605E4F
+  Functions: 304
+  Symbols:   748
   CStrings:  710
 
Symbols:
+ IRSetupLogging.cold.1
Functions:
~ -[IRMediaBundle isEqual:] : 316 -> 312
~ -[IRAppleTVControlEvent isEqual:] : 504 -> 500
~ -[IRContext isEqual:] : 628 -> 624
~ -[IRCandidate isEqual:] : 904 -> 900
~ -[IRSession init] : 736 -> 728
~ -[IRSession _manageSessionAvailableNotificationObservation:] : 472 -> 468
~ _OUTLINED_FUNCTION_1 : 32 -> 16
~ _OUTLINED_FUNCTION_3 : 20 -> 32
~ _IRSetupLogging : 40 -> 44
~ -[IRSession requestCurrentContext].cold.1 : 176 -> 180
~ -[IRSession requestCurrentContextWithBundleID:].cold.1 : 176 -> 68
~ -[IRSession requestCurrentContextWithBundleID:].cold.2 : 68 -> 180
~ -[IRSession setSpotOnLocationWithParameters:].cold.1 : 176 -> 180

```
