## WiFiCloudSyncEngine

> `/System/Library/PrivateFrameworks/WiFiCloudSyncEngine.framework/WiFiCloudSyncEngine`

```diff

-825.8.0.0.0
-  __TEXT.__text: 0x11328
-  __TEXT.__auth_stubs: 0x4b0
+825.13.0.0.0
+  __TEXT.__text: 0x11440
+  __TEXT.__auth_stubs: 0x4d0
   __TEXT.__objc_methlist: 0x1dc
   __TEXT.__const: 0x30
   __TEXT.__oslogstring: 0x24ec
   __TEXT.__cstring: 0x14f1
-  __TEXT.__unwind_info: 0x1e0
+  __TEXT.__unwind_info: 0x1d8
   __TEXT.__objc_classname: 0x33
   __TEXT.__objc_methname: 0x8ce
   __TEXT.__objc_methtype: 0xfe

   __DATA_CONST.__objc_selrefs: 0x310
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0xf0
-  __AUTH_CONST.__auth_got: 0x260
+  __AUTH_CONST.__auth_got: 0x270
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0xc20
   __AUTH_CONST.__objc_const: 0x280

   - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FD7A2BA3-682A-395C-AA99-0B036FE2A154
+  UUID: 6791EDC8-AD46-3345-8D57-F45784A8E5B0
   Functions: 259
-  Symbols:   732
+  Symbols:   734
   CStrings:  558
 
Symbols:
+ _objc_retain_x19
+ _objc_retain_x20
Functions:
~ -[WiFiCloudSyncEngineCore addToKVStore:synchronize:] : 2308 -> 2316
~ ___52-[WiFiCloudSyncEngineCore addToKVStore:synchronize:]_block_invoke : 8 -> 60
~ ___52-[WiFiCloudSyncEngineCore addToKVStore:synchronize:]_block_invoke.62 : 8 -> 60
~ -[WiFiCloudSyncEngineCore removeFromKVStore:] : 392 -> 396
~ ___45-[WiFiCloudSyncEngineCore removeFromKVStore:]_block_invoke : 8 -> 60
~ -[WiFiCloudSyncEngineCore clearKVS] : 536 -> 540
~ ___35-[WiFiCloudSyncEngineCore clearKVS]_block_invoke : 8 -> 60
~ -[WiFiCloudSyncEngineCore subscribeKVStoreNotficationsForBundleId:] : 632 -> 636
~ ___67-[WiFiCloudSyncEngineCore subscribeKVStoreNotficationsForBundleId:]_block_invoke : 8 -> 60
CStrings:
+ "20:31:02"
+ "Sep 29 2025"
- "20:18:12"
- "Sep 11 2025"

```
