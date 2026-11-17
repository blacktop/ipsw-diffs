## AXAssetLoader

> `/System/Library/PrivateFrameworks/AXAssetLoader.framework/AXAssetLoader`

```diff

-3245.8.14.0.0
-  __TEXT.__text: 0x11f04
+3245.8.23.0.0
+  __TEXT.__text: 0x120e0
   __TEXT.__objc_methlist: 0x11cc
-  __TEXT.__const: 0xa0
+  __TEXT.__const: 0xa8
   __TEXT.__gcc_except_tab: 0x630
   __TEXT.__cstring: 0xccb
-  __TEXT.__oslogstring: 0xf78
+  __TEXT.__oslogstring: 0x1058
   __TEXT.__dlopen_cstrs: 0x1e6
   __TEXT.__unwind_info: 0x760
   __TEXT.__objc_stubs: 0x0

   - /usr/lib/libobjc.A.dylib
   Functions: 461
   Symbols:   913
-  CStrings:  217
+  CStrings:  219
 
Functions:
~ -[AXImageCaptionModelAssetPolicy assetsToDownloadFromRefreshedAssets:] : 1580 -> 1784
~ -[AXAssetMetadataStore requestAssertion:] : 192 -> 464
CStrings:
+ "ImageCaptionModel download evaluation. Refreshed: %lu, installed: %lu, downloadable: %lu. Assertions held: %lu version-locked, %lu upgradable"
+ "Requested assertion for %@ from %@. Store available: %d. Assertions now held: %lu"
```
