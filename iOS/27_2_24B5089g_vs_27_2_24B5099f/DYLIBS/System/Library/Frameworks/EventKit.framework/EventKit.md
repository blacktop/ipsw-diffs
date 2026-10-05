## EventKit

> `/System/Library/Frameworks/EventKit.framework/EventKit`

```diff

-1976.1.3.0.0
-  __TEXT.__text: 0x1997a8
-  __TEXT.__objc_methlist: 0x15b9c
+1976.2.2.0.0
+  __TEXT.__text: 0x199730
+  __TEXT.__objc_methlist: 0x15bcc
   __TEXT.__cstring: 0xbdbf
   __TEXT.__const: 0x4870
-  __TEXT.__oslogstring: 0xf1b4
+  __TEXT.__oslogstring: 0xf234
   __TEXT.__gcc_except_tab: 0x3950
   __TEXT.__dlopen_cstrs: 0x400
   __TEXT.__ustring: 0x1a0

   __TEXT.__swift_as_ret: 0xec
   __TEXT.__swift_as_cont: 0x1a8
   __TEXT.__swift5_mpenum: 0x60
-  __TEXT.__unwind_info: 0x83a8
+  __TEXT.__unwind_info: 0x83b8
   __TEXT.__eh_frame: 0x261c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x258
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xaee8
+  __DATA_CONST.__objc_selrefs: 0xaef8
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x538
   __DATA_CONST.__objc_arraydata: 0x5d8

   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0x1b8
   __AUTH_CONST.__objc_doubleobj: 0x100
-  __AUTH_CONST.__auth_got: 0x1428
-  __AUTH.__objc_data: 0x3520
-  __AUTH.__data: 0xf08
+  __AUTH_CONST.__auth_got: 0x1430
+  __AUTH.__objc_data: 0x1db8
+  __AUTH.__data: 0x610
   __DATA.__objc_ivar: 0xd88
-  __DATA.__data: 0x28e0
+  __DATA.__data: 0x28f0
   __DATA.__common: 0x68
-  __DATA_DIRTY.__objc_data: 0x1bd0
-  __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x588
+  __DATA_DIRTY.__objc_data: 0x3338
+  __DATA_DIRTY.__data: 0x910
+  __DATA_DIRTY.__bss: 0x5a0
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10703
-  Symbols:   13284
-  CStrings:  2672
+  Functions: 10709
+  Symbols:   13291
+  CStrings:  2673
 
Symbols:
+ -[EKEventStore realAuthorizationStatusForEntityType:]
+ -[EKFrozenReminderObject shouldCheckExistenceBeforeRefresh]
+ -[EKPersistentObject _shouldAllowUnloadingProperties]
+ -[EKPersistentObject shouldCheckExistenceBeforeRefresh]
+ GCC_except_table100
+ GCC_except_table109
+ GCC_except_table112
+ GCC_except_table118
+ GCC_except_table123
+ GCC_except_table130
+ GCC_except_table134
+ GCC_except_table138
+ GCC_except_table140
+ GCC_except_table143
+ GCC_except_table162
+ GCC_except_table166
+ GCC_except_table175
+ GCC_except_table177
+ GCC_except_table184
+ GCC_except_table190
+ GCC_except_table193
+ GCC_except_table196
+ GCC_except_table231
+ GCC_except_table235
+ GCC_except_table237
+ GCC_except_table240
+ GCC_except_table243
+ GCC_except_table246
+ GCC_except_table248
+ GCC_except_table250
+ GCC_except_table254
+ GCC_except_table265
+ GCC_except_table267
+ GCC_except_table269
+ GCC_except_table277
+ GCC_except_table280
+ GCC_except_table286
+ GCC_except_table289
+ GCC_except_table322
+ GCC_except_table324
+ GCC_except_table327
+ GCC_except_table355
+ GCC_except_table357
+ GCC_except_table359
+ GCC_except_table361
+ GCC_except_table363
+ GCC_except_table365
+ GCC_except_table370
+ GCC_except_table378
+ GCC_except_table382
+ GCC_except_table384
+ GCC_except_table391
+ GCC_except_table394
+ GCC_except_table402
+ GCC_except_table414
+ GCC_except_table418
+ GCC_except_table423
+ GCC_except_table439
+ GCC_except_table444
+ GCC_except_table448
+ GCC_except_table450
+ GCC_except_table460
+ GCC_except_table464
+ GCC_except_table467
+ GCC_except_table470
+ GCC_except_table474
+ GCC_except_table477
+ GCC_except_table503
+ GCC_except_table505
+ GCC_except_table537
+ GCC_except_table551
+ GCC_except_table556
+ GCC_except_table574
+ GCC_except_table588
+ GCC_except_table591
+ GCC_except_table595
+ GCC_except_table610
+ GCC_except_table63
+ GCC_except_table642
+ GCC_except_table644
+ GCC_except_table646
+ GCC_except_table67
+ GCC_except_table688
+ GCC_except_table692
+ GCC_except_table694
+ GCC_except_table710
+ GCC_except_table712
+ GCC_except_table717
+ GCC_except_table720
+ GCC_except_table727
+ GCC_except_table73
+ GCC_except_table734
+ GCC_except_table742
+ GCC_except_table746
+ GCC_except_table748
+ GCC_except_table750
+ GCC_except_table756
+ GCC_except_table758
+ GCC_except_table760
+ GCC_except_table769
+ GCC_except_table773
+ GCC_except_table88
+ GCC_except_table91
+ _OUTLINED_FUNCTION_35
- GCC_except_table107
- GCC_except_table110
- GCC_except_table116
- GCC_except_table119
- GCC_except_table127
- GCC_except_table133
- GCC_except_table139
- GCC_except_table142
- GCC_except_table161
- GCC_except_table165
- GCC_except_table176
- GCC_except_table183
- GCC_except_table189
- GCC_except_table192
- GCC_except_table230
- GCC_except_table234
- GCC_except_table236
- GCC_except_table239
- GCC_except_table242
- GCC_except_table245
- GCC_except_table247
- GCC_except_table249
- GCC_except_table253
- GCC_except_table264
- GCC_except_table266
- GCC_except_table268
- GCC_except_table276
- GCC_except_table279
- GCC_except_table285
- GCC_except_table288
- GCC_except_table321
- GCC_except_table323
- GCC_except_table326
- GCC_except_table354
- GCC_except_table356
- GCC_except_table358
- GCC_except_table360
- GCC_except_table362
- GCC_except_table364
- GCC_except_table369
- GCC_except_table377
- GCC_except_table381
- GCC_except_table383
- GCC_except_table390
- GCC_except_table393
- GCC_except_table396
- GCC_except_table401
- GCC_except_table413
- GCC_except_table417
- GCC_except_table421
- GCC_except_table438
- GCC_except_table443
- GCC_except_table447
- GCC_except_table449
- GCC_except_table459
- GCC_except_table463
- GCC_except_table466
- GCC_except_table469
- GCC_except_table473
- GCC_except_table476
- GCC_except_table502
- GCC_except_table504
- GCC_except_table536
- GCC_except_table550
- GCC_except_table555
- GCC_except_table573
- GCC_except_table587
- GCC_except_table590
- GCC_except_table594
- GCC_except_table609
- GCC_except_table62
- GCC_except_table641
- GCC_except_table643
- GCC_except_table645
- GCC_except_table687
- GCC_except_table691
- GCC_except_table693
- GCC_except_table709
- GCC_except_table711
- GCC_except_table716
- GCC_except_table719
- GCC_except_table72
- GCC_except_table726
- GCC_except_table733
- GCC_except_table74
- GCC_except_table741
- GCC_except_table745
- GCC_except_table747
- GCC_except_table749
- GCC_except_table755
- GCC_except_table757
- GCC_except_table759
- GCC_except_table768
- GCC_except_table772
- GCC_except_table87
- GCC_except_table90
- GCC_except_table97
CStrings:
+ "%s: Not serializing %{public}@ to a draft because it has a never-committed co-commit sibling event that would be lost on restore"
```
