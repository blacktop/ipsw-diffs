## CloudFamilyRestrictionsDaemon

> `/System/Library/PrivateFrameworks/CloudFamilyRestrictionsDaemon.framework/Versions/A/CloudFamilyRestrictionsDaemon`

```diff

 27.0.0.0.0
-  __TEXT.__text: 0xe28c
+  __TEXT.__text: 0xe264
   __TEXT.__auth_stubs: 0x380
-  __TEXT.__objc_methlist: 0x8e0
+  __TEXT.__objc_methlist: 0xa8c
   __TEXT.__const: 0x68
   __TEXT.__cstring: 0x19c0
   __TEXT.__oslogstring: 0x27

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x890
+  __DATA_CONST.__objc_selrefs: 0x958
   __DATA_CONST.__objc_superrefs: 0x8
   __AUTH_CONST.__auth_got: 0x1c8
   __AUTH_CONST.__const: 0x50
   __AUTH_CONST.__cfstring: 0x24c0
-  __AUTH_CONST.__objc_const: 0x7a8
+  __AUTH_CONST.__objc_const: 0x488
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x18

   - /System/Library/PrivateFrameworks/TCC.framework/Versions/A/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D963ABDD-6E8A-3A79-92F2-605D8B7F34D5
-  Functions: 191
-  Symbols:   655
+  UUID: 110480C7-093C-3720-9A95-6C09F2F7F861
+  Functions: 192
+  Symbols:   656
   CStrings:  966
 
Symbols:
+ CFRLog.cold.1
Functions:
~ -[CFRPushManager connection:didChangeConnectedStatus:] : 160 -> 156
~ _CFRLog : 700 -> 660
~ -[CFRSettingsDispatcher setDefaultRestrictionsForLevel:] : 2572 -> 2560
~ -[CFRSettingsDispatcher setAllowPrinterAdministration:] : 600 -> 596
~ -[CFRSettingsDispatcher allowPrinterAdministration] : 268 -> 272
~ -[CFRSettingsDispatcher setLimitDictionaryContentEnabled:] : 652 -> 648
+ CFRLog.cold.1

```
