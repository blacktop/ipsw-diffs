## CoreRepairCore

> `/System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore`

```diff

-921.60.24.0.0
+921.60.26.0.0
   __TEXT.__text: 0x8844c
   __TEXT.__auth_stubs: 0x1690
   __TEXT.__objc_methlist: 0x3be4

   - /usr/lib/updaters/libSavageRestoreInfo_iOS.dylib
   - /usr/lib/updaters/libSavageUpdater_iOS.dylib
   - /usr/lib/updaters/libT200Updater.dylib
-  UUID: 8C906B3A-9958-3B6F-A23B-9CA2E3849360
-  Functions: 2301
-  Symbols:   7601
+  UUID: 3569460E-C5A8-3E12-A9D6-4BE4E861CABE
+  Functions: 2302
+  Symbols:   7603
   CStrings:  4871
 
Symbols:
+ _OUTLINED_FUNCTION_54
+ _OUTLINED_FUNCTION_60
- _OUTLINED_FUNCTION_59
Functions:
~ -[CREANController setupVersionedFDRWithApTicket:] : 1180 -> 1200
+ _OUTLINED_FUNCTION_54
~ _DERImg4DecodePayloadWithProperties : 184 -> 180
~ _DERImg4DecodePayloadProperties : 128 -> 124
~ _DERImg4DecodeRestoreInfo : 128 -> 124
~ _aks_params_free : 88 -> 80
~ _aks_ref_key_free : 144 -> 140
~ __set_blob : 288 -> 284
~ _encode_list_merge_dict : 72 -> 68

```
