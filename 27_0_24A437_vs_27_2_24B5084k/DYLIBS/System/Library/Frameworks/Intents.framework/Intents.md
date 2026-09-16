## Intents

> `/System/Library/Frameworks/Intents.framework/Intents`

```diff

-4016.0.51.1.102
-  __TEXT.__text: 0x444290
-  __TEXT.__objc_methlist: 0x78c6c
-  __TEXT.__const: 0x1d28
+4016.1.8.0.0
+  __TEXT.__text: 0x44524c
+  __TEXT.__objc_methlist: 0x78cb4
+  __TEXT.__const: 0x1d48
   __TEXT.__dlopen_cstrs: 0xce9
-  __TEXT.__gcc_except_tab: 0x2194
-  __TEXT.__cstring: 0x47beb
-  __TEXT.__oslogstring: 0x617f
+  __TEXT.__gcc_except_tab: 0x21bc
+  __TEXT.__cstring: 0x47cf6
+  __TEXT.__oslogstring: 0x657d
   __TEXT.__ustring: 0x512
-  __TEXT.__unwind_info: 0x14c40
+  __TEXT.__unwind_info: 0x14c68
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xb850
+  __DATA_CONST.__const: 0xb870
   __DATA_CONST.__objc_classlist: 0x2930
   __DATA_CONST.__objc_catlist: 0x100
-  __DATA_CONST.__objc_protolist: 0x1940
+  __DATA_CONST.__objc_protolist: 0x1938
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x154d0
+  __DATA_CONST.__objc_selrefs: 0x154f8
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x1398
   __DATA_CONST.__objc_arraydata: 0xc820
-  __DATA_CONST.__got: 0x28d0
+  __DATA_CONST.__got: 0x28d8
   __AUTH_CONST.__const: 0x17c0
-  __AUTH_CONST.__cfstring: 0x42a40
-  __AUTH_CONST.__objc_const: 0xb4da8
+  __AUTH_CONST.__cfstring: 0x42ac0
+  __AUTH_CONST.__objc_const: 0xb4578
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x828
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x4dd0
   __AUTH_CONST.__objc_dictobj: 0x3b60
-  __AUTH_CONST.__auth_got: 0x858
+  __AUTH_CONST.__auth_got: 0x868
   __AUTH.__objc_data: 0x16a80
-  __DATA.__objc_ivar: 0x3d54
-  __DATA.__data: 0x12f98
+  __DATA.__objc_ivar: 0x3d5c
+  __DATA.__data: 0x12f38
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x3160
   __DATA_DIRTY.__bss: 0x1a0

   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 30712
-  Symbols:   58488
-  CStrings:  9706
+  Functions: 30722
+  Symbols:   58507
+  CStrings:  9726
 
Symbols:
+ -[INFile _setUnverifiedFileURL:securityScope:]
+ -[INFile _unverifiedFileURL]
+ -[INFile _unverifiedSecurityScope]
+ -[INSendMessageIntent _isUserConfirmationRequired]
+ -[NSURL(INSandboxExtension) _in_outgoingSecurityScope]
+ -[NSURL(INSandboxExtension) _in_setOutgoingSecurityScope:]
+ GCC_except_table10147
+ GCC_except_table10157
+ GCC_except_table10159
+ GCC_except_table10164
+ GCC_except_table10229
+ GCC_except_table10236
+ GCC_except_table10789
+ GCC_except_table10914
+ GCC_except_table10918
+ GCC_except_table11031
+ GCC_except_table11144
+ GCC_except_table11171
+ GCC_except_table11172
+ GCC_except_table11395
+ GCC_except_table11837
+ GCC_except_table12127
+ GCC_except_table1227
+ GCC_except_table12577
+ GCC_except_table12580
+ GCC_except_table12588
+ GCC_except_table12609
+ GCC_except_table1277
+ GCC_except_table13214
+ GCC_except_table1333
+ GCC_except_table1352
+ GCC_except_table1362
+ GCC_except_table13751
+ GCC_except_table13791
+ GCC_except_table13795
+ GCC_except_table14040
+ GCC_except_table14567
+ GCC_except_table15247
+ GCC_except_table15251
+ GCC_except_table1628
+ GCC_except_table16391
+ GCC_except_table16494
+ GCC_except_table16502
+ GCC_except_table16503
+ GCC_except_table16805
+ GCC_except_table18451
+ GCC_except_table19106
+ GCC_except_table19276
+ GCC_except_table19303
+ GCC_except_table19868
+ GCC_except_table19870
+ GCC_except_table19873
+ GCC_except_table19951
+ GCC_except_table20951
+ GCC_except_table21046
+ GCC_except_table21268
+ GCC_except_table22336
+ GCC_except_table22339
+ GCC_except_table22342
+ GCC_except_table22957
+ GCC_except_table22974
+ GCC_except_table23691
+ GCC_except_table25167
+ GCC_except_table25179
+ GCC_except_table2519
+ GCC_except_table2553
+ GCC_except_table27050
+ GCC_except_table27053
+ GCC_except_table27054
+ GCC_except_table27055
+ GCC_except_table27056
+ GCC_except_table2813
+ GCC_except_table2814
+ GCC_except_table28748
+ GCC_except_table28760
+ GCC_except_table28762
+ GCC_except_table28771
+ GCC_except_table2896
+ GCC_except_table2932
+ GCC_except_table2964
+ GCC_except_table29819
+ GCC_except_table29828
+ GCC_except_table29832
+ GCC_except_table29837
+ GCC_except_table29841
+ GCC_except_table29843
+ GCC_except_table29844
+ GCC_except_table29845
+ GCC_except_table29846
+ GCC_except_table29848
+ GCC_except_table30037
+ GCC_except_table3184
+ GCC_except_table3187
+ GCC_except_table3195
+ GCC_except_table3208
+ GCC_except_table4089
+ GCC_except_table4091
+ GCC_except_table4188
+ GCC_except_table4192
+ GCC_except_table4199
+ GCC_except_table4201
+ GCC_except_table4214
+ GCC_except_table4427
+ GCC_except_table5401
+ GCC_except_table5402
+ GCC_except_table5459
+ GCC_except_table5619
+ GCC_except_table5626
+ GCC_except_table5628
+ GCC_except_table5865
+ GCC_except_table5874
+ GCC_except_table6422
+ GCC_except_table6424
+ GCC_except_table6456
+ GCC_except_table6457
+ GCC_except_table6458
+ GCC_except_table6459
+ GCC_except_table6493
+ GCC_except_table7054
+ GCC_except_table7139
+ GCC_except_table7140
+ GCC_except_table7861
+ GCC_except_table8127
+ GCC_except_table820
+ GCC_except_table829
+ GCC_except_table8472
+ GCC_except_table8476
+ GCC_except_table8724
+ GCC_except_table8726
+ GCC_except_table9403
+ GCC_except_table9959
+ _INSecurityScopeLogDescription
+ _OBJC_IVAR_$_INFile._unverifiedFileURLString
+ _OBJC_IVAR_$_INFile._unverifiedSecurityScope
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
- GCC_except_table10141
- GCC_except_table10151
- GCC_except_table10153
- GCC_except_table10158
- GCC_except_table10223
- GCC_except_table10230
- GCC_except_table10783
- GCC_except_table10908
- GCC_except_table10912
- GCC_except_table11025
- GCC_except_table11138
- GCC_except_table11165
- GCC_except_table11166
- GCC_except_table11388
- GCC_except_table11830
- GCC_except_table12120
- GCC_except_table1221
- GCC_except_table12563
- GCC_except_table12573
- GCC_except_table12581
- GCC_except_table12602
- GCC_except_table1271
- GCC_except_table13207
- GCC_except_table1327
- GCC_except_table1346
- GCC_except_table1356
- GCC_except_table13744
- GCC_except_table13784
- GCC_except_table13788
- GCC_except_table14033
- GCC_except_table14560
- GCC_except_table15240
- GCC_except_table15244
- GCC_except_table1622
- GCC_except_table16384
- GCC_except_table16487
- GCC_except_table16495
- GCC_except_table16496
- GCC_except_table16798
- GCC_except_table18444
- GCC_except_table19099
- GCC_except_table19269
- GCC_except_table19296
- GCC_except_table19861
- GCC_except_table19863
- GCC_except_table19866
- GCC_except_table19944
- GCC_except_table20944
- GCC_except_table21039
- GCC_except_table21261
- GCC_except_table22329
- GCC_except_table22332
- GCC_except_table22335
- GCC_except_table22950
- GCC_except_table22967
- GCC_except_table23683
- GCC_except_table2513
- GCC_except_table25157
- GCC_except_table25169
- GCC_except_table2547
- GCC_except_table27040
- GCC_except_table27043
- GCC_except_table27044
- GCC_except_table27045
- GCC_except_table27046
- GCC_except_table2807
- GCC_except_table2808
- GCC_except_table28738
- GCC_except_table28740
- GCC_except_table28742
- GCC_except_table28761
- GCC_except_table2890
- GCC_except_table2926
- GCC_except_table2958
- GCC_except_table29809
- GCC_except_table29817
- GCC_except_table29818
- GCC_except_table29822
- GCC_except_table29823
- GCC_except_table29824
- GCC_except_table29825
- GCC_except_table29831
- GCC_except_table29836
- GCC_except_table29838
- GCC_except_table30027
- GCC_except_table3178
- GCC_except_table3181
- GCC_except_table3189
- GCC_except_table3202
- GCC_except_table4083
- GCC_except_table4085
- GCC_except_table4182
- GCC_except_table4186
- GCC_except_table4193
- GCC_except_table4195
- GCC_except_table4208
- GCC_except_table4421
- GCC_except_table5395
- GCC_except_table5396
- GCC_except_table5453
- GCC_except_table5613
- GCC_except_table5616
- GCC_except_table5620
- GCC_except_table5859
- GCC_except_table5868
- GCC_except_table6416
- GCC_except_table6418
- GCC_except_table6450
- GCC_except_table6451
- GCC_except_table6452
- GCC_except_table6453
- GCC_except_table6487
- GCC_except_table7048
- GCC_except_table7133
- GCC_except_table7134
- GCC_except_table7855
- GCC_except_table8121
- GCC_except_table816
- GCC_except_table8466
- GCC_except_table8470
- GCC_except_table8718
- GCC_except_table8720
- GCC_except_table9397
- GCC_except_table9953
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
