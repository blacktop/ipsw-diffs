## SafariCore

> `/System/Library/PrivateFrameworks/SafariCore.framework/SafariCore`

```diff

-622.1.16.10.3
-  __TEXT.__text: 0x1183f8
-  __TEXT.__auth_stubs: 0x2d60
-  __TEXT.__objc_methlist: 0xb4d4
-  __TEXT.__const: 0x2984
-  __TEXT.__gcc_except_tab: 0x64ec
-  __TEXT.__cstring: 0x11a05
+622.1.18.10.3
+  __TEXT.__text: 0x118b94
+  __TEXT.__auth_stubs: 0x2d90
+  __TEXT.__objc_methlist: 0xb50c
+  __TEXT.__const: 0x29a4
+  __TEXT.__gcc_except_tab: 0x6560
+  __TEXT.__cstring: 0x11a65
   __TEXT.__ustring: 0x2786
   __TEXT.__oslogstring: 0x9f4d
   __TEXT.__dlopen_cstrs: 0x19b

   __TEXT.__swift5_builtin: 0x8c
   __TEXT.__swift5_reflstr: 0x619
   __TEXT.__swift5_assocty: 0x1e0
-  __TEXT.__swift5_capture: 0x568
+  __TEXT.__swift5_capture: 0x578
   __TEXT.__swift5_proto: 0x1e0
   __TEXT.__swift5_types: 0xb8
   __TEXT.__swift_as_entry: 0xd0
   __TEXT.__swift_as_ret: 0xbc
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x5ea8
-  __TEXT.__eh_frame: 0x2cc8
+  __TEXT.__unwind_info: 0x5f70
+  __TEXT.__eh_frame: 0x2cf0
   __TEXT.__objc_classname: 0x19b3
-  __TEXT.__objc_methname: 0x2383a
-  __TEXT.__objc_methtype: 0x3d68
-  __TEXT.__objc_stubs: 0x113c0
+  __TEXT.__objc_methname: 0x23983
+  __TEXT.__objc_methtype: 0x3d7e
+  __TEXT.__objc_stubs: 0x11420
   __DATA_CONST.__got: 0xde0
-  __DATA_CONST.__const: 0x4e00
+  __DATA_CONST.__const: 0x4e08
   __DATA_CONST.__objc_classlist: 0x5c8
   __DATA_CONST.__objc_catlist: 0x168
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6878
+  __DATA_CONST.__objc_selrefs: 0x68a0
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x478
   __DATA_CONST.__objc_arraydata: 0x2790
-  __AUTH_CONST.__auth_got: 0x16c8
-  __AUTH_CONST.__const: 0x4af0
-  __AUTH_CONST.__cfstring: 0x183c0
-  __AUTH_CONST.__objc_const: 0x12a10
+  __AUTH_CONST.__auth_got: 0x16e0
+  __AUTH_CONST.__const: 0x4b18
+  __AUTH_CONST.__cfstring: 0x18440
+  __AUTH_CONST.__objc_const: 0x12a20
   __AUTH_CONST.__objc_intobj: 0x390
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_arrayobj: 0x5a0

   __AUTH.__objc_data: 0x23e8
   __AUTH.__data: 0x480
   __DATA.__objc_ivar: 0xbb8
-  __DATA.__data: 0x1668
+  __DATA.__data: 0x1670
   __DATA.__bss: 0x3e90
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x1730

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F95B760D-BAA5-367A-ACDF-D3CF33942F11
-  Functions: 6719
-  Symbols:   18459
-  CStrings:  12416
+  UUID: 8C8387DF-BAF5-3F37-AE48-F377DEEDA767
+  Functions: 6730
+  Symbols:   18479
+  CStrings:  12432
 
Symbols:
+ +[NSURL(SafariCoreExtras) safari_urlWithDataAsString:]
+ +[WBSFeatureAvailability isAutoFillInternalFeedbackUIEnabled]
+ +[WBSSavedAccountStore getProtectionSpaceAndHighLevelDomainForUserTypedSite:protectionSpace:highLevelDomain:mode:]
+ -[NSFileManager(SafariNSFileManagerExtras) safari_createTemporaryDirectoryWithTemplatePrefix:]
+ -[WBSAnalyticsLogger reportSafariRecoveredWindowStateWithSuccess:]
+ GCC_except_table258
+ GCC_except_table263
+ GCC_except_table284
+ GCC_except_table343
+ GCC_except_table345
+ GCC_except_table350
+ GCC_except_table407
+ GCC_except_table412
+ GCC_except_table417
+ GCC_except_table423
+ GCC_except_table426
+ GCC_except_table429
+ GCC_except_table433
+ GCC_except_table434
+ _CFURLCreateAbsoluteURLWithBytes
+ _WBSAutoFillInternalFeedbackUIEnabledKey
+ ___112-[NSFileManager(SafariNSFileManagerExtras) safari_removeContentsOfDirectory:preservingContainerManagerMetadata:]_block_invoke.82
+ ___66-[WBSAnalyticsLogger reportSafariRecoveredWindowStateWithSuccess:]_block_invoke
+ ___block_literal_global.1014
+ ___block_literal_global.108
+ ___block_literal_global.1080
+ ___block_literal_global.116
+ ___block_literal_global.1217
+ ___block_literal_global.1219
+ ___block_literal_global.1224
+ ___block_literal_global.1226
+ ___block_literal_global.1228
+ ___block_literal_global.1230
+ ___block_literal_global.1232
+ ___block_literal_global.1234
+ ___block_literal_global.1236
+ ___block_literal_global.1238
+ ___block_literal_global.1240
+ ___block_literal_global.1242
+ ___block_literal_global.1244
+ ___block_literal_global.1246
+ ___block_literal_global.126
+ ___block_literal_global.128
+ ___block_literal_global.1310
+ ___block_literal_global.1312
+ ___block_literal_global.1314
+ ___block_literal_global.1316
+ ___block_literal_global.1318
+ ___block_literal_global.1320
+ ___block_literal_global.135
+ ___block_literal_global.140
+ ___block_literal_global.147
+ ___block_literal_global.153
+ ___block_literal_global.169
+ ___block_literal_global.174
+ ___block_literal_global.618
+ ___block_literal_global.754
+ ___block_literal_global.759
+ ___block_literal_global.774
+ ___block_literal_global.786
+ ___block_literal_global.795
+ ___block_literal_global.804
+ ___block_literal_global.811
+ ___block_literal_global.823
+ ___block_literal_global.888
+ ___block_literal_global.894
+ ___block_literal_global.978
+ ___block_literal_global.980
+ _objc_msgSend$getProtectionSpaceAndHighLevelDomainForUserTypedSite:protectionSpace:highLevelDomain:mode:
+ _objc_msgSend$safari_createTemporaryDirectoryWithTemplate:
+ _objc_msgSend$shouldShowInternalUI
+ _objectdestroy.53Tm
- GCC_except_table253
- GCC_except_table283
- GCC_except_table342
- GCC_except_table344
- GCC_except_table349
- GCC_except_table355
- GCC_except_table406
- GCC_except_table411
- GCC_except_table416
- GCC_except_table421
- GCC_except_table425
- GCC_except_table430
- GCC_except_table431
- GCC_except_table53
- ___112-[NSFileManager(SafariNSFileManagerExtras) safari_removeContentsOfDirectory:preservingContainerManagerMetadata:]_block_invoke.79
- ___block_literal_global.1011
- ___block_literal_global.102
- ___block_literal_global.107
- ___block_literal_global.1077
- ___block_literal_global.1214
- ___block_literal_global.1216
- ___block_literal_global.1221
- ___block_literal_global.1223
- ___block_literal_global.1225
- ___block_literal_global.1227
- ___block_literal_global.1229
- ___block_literal_global.123
- ___block_literal_global.1231
- ___block_literal_global.1233
- ___block_literal_global.1235
- ___block_literal_global.1237
- ___block_literal_global.1239
- ___block_literal_global.1241
- ___block_literal_global.1243
- ___block_literal_global.127
- ___block_literal_global.1307
- ___block_literal_global.1309
- ___block_literal_global.1311
- ___block_literal_global.1313
- ___block_literal_global.1315
- ___block_literal_global.1317
- ___block_literal_global.137
- ___block_literal_global.154
- ___block_literal_global.161
- ___block_literal_global.166
- ___block_literal_global.171
- ___block_literal_global.176
- ___block_literal_global.178
- ___block_literal_global.56
- ___block_literal_global.615
- ___block_literal_global.751
- ___block_literal_global.756
- ___block_literal_global.771
- ___block_literal_global.783
- ___block_literal_global.792
- ___block_literal_global.801
- ___block_literal_global.809
- ___block_literal_global.820
- ___block_literal_global.886
- ___block_literal_global.889
- ___block_literal_global.975
- ___block_literal_global.977
- _objectdestroy.48Tm
CStrings:
+ "-XXXXXXXX"
+ "B48@0:8@16^@24^@32q40"
+ "TB,R,N,GisAutoFillInternalFeedbackUIEnabled"
+ "WBSAutoFillInternalFeedbackUIEnabled"
+ "autoFillInternalFeedbackUIEnabled"
+ "com.apple.Safari.SafariRecoveredWindowState"
+ "getProtectionSpaceAndHighLevelDomainForUserTypedSite:protectionSpace:highLevelDomain:mode:"
+ "isAutoFillInternalFeedbackUIEnabled"
+ "recovered"
+ "reportSafariRecoveredWindowStateWithSuccess:"
+ "safari_createTemporaryDirectoryWithTemplatePrefix:"
+ "safari_urlWithDataAsString:"

```
