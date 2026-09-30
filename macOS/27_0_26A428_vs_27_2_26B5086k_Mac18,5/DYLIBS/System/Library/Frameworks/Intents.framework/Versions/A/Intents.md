## Intents

> `/System/Library/Frameworks/Intents.framework/Versions/A/Intents`

```diff

-4016.0.51.1.402
-  __TEXT.__text: 0x48e3dc
-  __TEXT.__objc_methlist: 0x7ab14
-  __TEXT.__const: 0x1d40
+4016.1.8.0.0
+  __TEXT.__text: 0x48f488
+  __TEXT.__objc_methlist: 0x7ab5c
+  __TEXT.__const: 0x1d60
   __TEXT.__dlopen_cstrs: 0xb0a
-  __TEXT.__gcc_except_tab: 0x1f58
-  __TEXT.__cstring: 0x4c26b
-  __TEXT.__oslogstring: 0x5d3f
+  __TEXT.__gcc_except_tab: 0x1f80
+  __TEXT.__cstring: 0x4c376
+  __TEXT.__oslogstring: 0x613d
   __TEXT.__ustring: 0x512
-  __TEXT.__unwind_info: 0x15270
+  __TEXT.__unwind_info: 0x15298
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x9a48
+  __DATA_CONST.__const: 0x9a68
   __DATA_CONST.__objc_classlist: 0x29e0
   __DATA_CONST.__objc_catlist: 0xf8
-  __DATA_CONST.__objc_protolist: 0x19b8
+  __DATA_CONST.__objc_protolist: 0x19b0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x15560
+  __DATA_CONST.__objc_selrefs: 0x15588
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x1438
   __DATA_CONST.__objc_arraydata: 0xd128
-  __DATA_CONST.__got: 0x2910
+  __DATA_CONST.__got: 0x2918
   __AUTH_CONST.__const: 0x3e60
-  __AUTH_CONST.__cfstring: 0x455c0
-  __AUTH_CONST.__objc_const: 0xb7148
+  __AUTH_CONST.__cfstring: 0x45640
+  __AUTH_CONST.__objc_const: 0xb6878
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x798
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x53e8
   __AUTH_CONST.__objc_dictobj: 0x3b38
-  __AUTH_CONST.__auth_got: 0x750
+  __AUTH_CONST.__auth_got: 0x760
   __AUTH.__objc_data: 0x16698
-  __DATA.__objc_ivar: 0x3d2c
-  __DATA.__data: 0x13538
+  __DATA.__objc_ivar: 0x3d34
+  __DATA.__data: 0x134d8
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x3c28
   __DATA_DIRTY.__bss: 0x1d0

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /System/Library/PrivateFrameworks/TCC.framework/Versions/A/TCC
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 31221
-  Symbols:   59663
-  CStrings:  10035
+  Functions: 31231
+  Symbols:   59682
+  CStrings:  10055
 
Symbols:
+ -[INFile _setUnverifiedFileURL:securityScope:]
+ -[INFile _unverifiedFileURL]
+ -[INFile _unverifiedSecurityScope]
+ -[INSendMessageIntent _isUserConfirmationRequired]
+ -[NSURL(INSandboxExtension) _in_outgoingSecurityScope]
+ -[NSURL(INSandboxExtension) _in_setOutgoingSecurityScope:]
+ GCC_except_table10141
+ GCC_except_table10153
+ GCC_except_table10155
+ GCC_except_table10160
+ GCC_except_table10225
+ GCC_except_table10786
+ GCC_except_table10911
+ GCC_except_table10915
+ GCC_except_table11028
+ GCC_except_table11141
+ GCC_except_table11168
+ GCC_except_table11169
+ GCC_except_table11392
+ GCC_except_table11834
+ GCC_except_table1233
+ GCC_except_table12563
+ GCC_except_table12574
+ GCC_except_table12577
+ GCC_except_table12585
+ GCC_except_table12606
+ GCC_except_table13211
+ GCC_except_table1342
+ GCC_except_table1361
+ GCC_except_table1372
+ GCC_except_table13785
+ GCC_except_table13789
+ GCC_except_table14034
+ GCC_except_table14561
+ GCC_except_table15241
+ GCC_except_table15245
+ GCC_except_table16376
+ GCC_except_table1639
+ GCC_except_table16479
+ GCC_except_table16487
+ GCC_except_table16488
+ GCC_except_table16790
+ GCC_except_table18436
+ GCC_except_table19092
+ GCC_except_table19249
+ GCC_except_table19277
+ GCC_except_table20282
+ GCC_except_table20284
+ GCC_except_table20287
+ GCC_except_table20441
+ GCC_except_table21468
+ GCC_except_table21770
+ GCC_except_table22838
+ GCC_except_table22841
+ GCC_except_table22844
+ GCC_except_table23459
+ GCC_except_table23889
+ GCC_except_table24200
+ GCC_except_table2530
+ GCC_except_table2564
+ GCC_except_table25677
+ GCC_except_table25689
+ GCC_except_table27560
+ GCC_except_table27563
+ GCC_except_table27564
+ GCC_except_table27565
+ GCC_except_table27566
+ GCC_except_table2901
+ GCC_except_table29258
+ GCC_except_table29270
+ GCC_except_table29272
+ GCC_except_table29281
+ GCC_except_table2937
+ GCC_except_table2970
+ GCC_except_table30329
+ GCC_except_table30338
+ GCC_except_table30342
+ GCC_except_table30347
+ GCC_except_table30351
+ GCC_except_table30353
+ GCC_except_table30354
+ GCC_except_table30355
+ GCC_except_table30356
+ GCC_except_table30358
+ GCC_except_table30547
+ GCC_except_table3190
+ GCC_except_table3193
+ GCC_except_table3203
+ GCC_except_table3217
+ GCC_except_table4098
+ GCC_except_table4100
+ GCC_except_table4197
+ GCC_except_table4201
+ GCC_except_table4208
+ GCC_except_table4210
+ GCC_except_table4223
+ GCC_except_table4436
+ GCC_except_table5416
+ GCC_except_table5417
+ GCC_except_table5624
+ GCC_except_table5631
+ GCC_except_table5633
+ GCC_except_table5873
+ GCC_except_table5882
+ GCC_except_table6422
+ GCC_except_table6425
+ GCC_except_table6457
+ GCC_except_table6458
+ GCC_except_table6459
+ GCC_except_table6460
+ GCC_except_table6494
+ GCC_except_table7057
+ GCC_except_table7142
+ GCC_except_table7143
+ GCC_except_table7866
+ GCC_except_table8132
+ GCC_except_table824
+ GCC_except_table833
+ GCC_except_table8477
+ GCC_except_table8481
+ GCC_except_table9398
+ GCC_except_table9954
+ OBJC_IVAR_$_INFile._unverifiedFileURLString
+ OBJC_IVAR_$_INFile._unverifiedSecurityScope
+ _INSecurityScopeLogDescription
+ _SANDBOX_EXTENSION_CANONICAL
+ __INCanonicalPathForFileURL
+ __INCopySandboxExtensionWithTokenGeneratorBlock
+ __INFileURLOutgoingSecurityScopeKey
+ __INTokenHexFieldValue
+ __OBJC_$_INSTANCE_METHODS_NSURL(INJSONSerialization|INSandboxExtension)
+ ____INCanonicalPathForFileURL_block_invoke
+ _audit_token_to_pid
+ _getpid
+ _objc_msgSend$_in_outgoingSecurityScope
+ _objc_msgSend$_in_setOutgoingSecurityScope:
+ _objc_msgSend$_setUnverifiedFileURL:securityScope:
+ _objc_msgSend$_unverifiedFileURL
- GCC_except_table10135
- GCC_except_table10147
- GCC_except_table10149
- GCC_except_table10154
- GCC_except_table10219
- GCC_except_table10780
- GCC_except_table10905
- GCC_except_table10909
- GCC_except_table11022
- GCC_except_table11135
- GCC_except_table11162
- GCC_except_table11163
- GCC_except_table11385
- GCC_except_table11827
- GCC_except_table1227
- GCC_except_table12556
- GCC_except_table12567
- GCC_except_table12570
- GCC_except_table12578
- GCC_except_table12599
- GCC_except_table13204
- GCC_except_table1336
- GCC_except_table1355
- GCC_except_table1366
- GCC_except_table13778
- GCC_except_table13782
- GCC_except_table14027
- GCC_except_table14554
- GCC_except_table15234
- GCC_except_table15238
- GCC_except_table1633
- GCC_except_table16369
- GCC_except_table16472
- GCC_except_table16480
- GCC_except_table16481
- GCC_except_table16783
- GCC_except_table18429
- GCC_except_table19085
- GCC_except_table19242
- GCC_except_table19270
- GCC_except_table20275
- GCC_except_table20277
- GCC_except_table20280
- GCC_except_table20434
- GCC_except_table21461
- GCC_except_table21763
- GCC_except_table22831
- GCC_except_table22834
- GCC_except_table22837
- GCC_except_table23452
- GCC_except_table23882
- GCC_except_table24192
- GCC_except_table2524
- GCC_except_table2558
- GCC_except_table25667
- GCC_except_table25679
- GCC_except_table27550
- GCC_except_table27553
- GCC_except_table27554
- GCC_except_table27555
- GCC_except_table27556
- GCC_except_table2895
- GCC_except_table29248
- GCC_except_table29250
- GCC_except_table29252
- GCC_except_table29271
- GCC_except_table2931
- GCC_except_table2964
- GCC_except_table30319
- GCC_except_table30327
- GCC_except_table30328
- GCC_except_table30332
- GCC_except_table30333
- GCC_except_table30334
- GCC_except_table30335
- GCC_except_table30341
- GCC_except_table30346
- GCC_except_table30348
- GCC_except_table30537
- GCC_except_table3184
- GCC_except_table3187
- GCC_except_table3197
- GCC_except_table3211
- GCC_except_table4092
- GCC_except_table4094
- GCC_except_table4191
- GCC_except_table4195
- GCC_except_table4202
- GCC_except_table4204
- GCC_except_table4217
- GCC_except_table4430
- GCC_except_table5410
- GCC_except_table5411
- GCC_except_table5618
- GCC_except_table5621
- GCC_except_table5625
- GCC_except_table5867
- GCC_except_table5876
- GCC_except_table6416
- GCC_except_table6419
- GCC_except_table6451
- GCC_except_table6452
- GCC_except_table6453
- GCC_except_table6454
- GCC_except_table6488
- GCC_except_table7051
- GCC_except_table7136
- GCC_except_table7137
- GCC_except_table7860
- GCC_except_table8126
- GCC_except_table820
- GCC_except_table8471
- GCC_except_table8475
- GCC_except_table9392
- GCC_except_table9948
- __INIssueSandboxExtensionWithTokenGeneratorBlock
- __OBJC_$_CATEGORY_INSTANCE_METHODS_NSURL_$_INJSONSerialization
- __OBJC_LABEL_PROTOCOL_$_JSExport
- __OBJC_PROTOCOL_$_JSExport
CStrings:
+ "\v"
+ "%s Dropping URL value after security scope validation failure. path:%{public}@ scope:%{public}@ this_pid:%d forwarder:%d"
+ "%s INFile encoding: path:%{public}@ scope:%{public}@ this_pid:%d has_data:%d has_bookmark:%d outgoing:%d"
+ "%s INFile forwarding unverified scope: path:%{public}@ scope:%{public}@ this_pid:%d"
+ "%s INFile scope is neither usable nor self-consistent; dropping fileURL and scope. path:%{public}@ scope:%{public}@ this_pid:%d has_data:%d has_bookmark:%d will_return_nil:%d"
+ "%s INFile scope not usable here; retaining self-consistent pair for forwarding. path:%{public}@ scope:%{public}@ this_pid:%d has_data:%d has_bookmark:%d"
+ "%s Minted sandbox extension: path:%{public}@ new:%{public}@ existing:%{public}@ target_pid:%d this_pid:%d"
+ "%s Sandbox extension mint failed: %{public}s path:%{public}@ existing:%{public}@ target_pid:%d this_pid:%d"
+ "%s Sandbox extension mint skipped: existing scope not fully verifiable in this process. path:%{public}@ existing:%{public}@ target_pid:%d this_pid:%d"
+ "%s Security scope consume failed: %{public}s scope:%{public}@ this_pid:%d"
+ "-[INFile encodeWithCoder:]"
+ "-[INFile initWithCoder:]"
+ "<hmac:%s flags:0x%llx bind_pid:%lld bind_pidversion:%lld class:%@ bytes:%lu>"
+ "<malformed:empty-token>"
+ "<none>"
+ "INIntentSlotValueTransformFromURLValue"
+ "_INCopySandboxExtensionWithTokenGeneratorBlock"
+ "avci"
+ "avcs"
+ "avif"
+ "avis"
+ "com.apple.WorkflowKit.BackgroundShortcutRunner"
- "%s Security scope signature check failed: %{public}s"
- "_INIssueSandboxExtensionWithTokenGeneratorBlock"
```
