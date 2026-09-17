## com.apple.driver.AppleRAID

> `com.apple.driver.AppleRAID`

```diff

-29.0.0.0.0
+29.40.4.0.0
   __TEXT.__const: 0x10
-  __TEXT.__cstring: 0x22c2
-  __TEXT_EXEC.__text: 0x1b578
+  __TEXT.__cstring: 0x250a
+  __TEXT_EXEC.__text: 0x1bc40
   __TEXT_EXEC.__auth_stubs: 0x500
   __DATA.__data: 0xc8
   __DATA.__common: 0x2d0

   __DATA_CONST.__mod_term_func: 0x70
   __DATA_CONST.__const: 0x8ae0
   __DATA_CONST.__kalloc_type: 0x440
-  __DATA_CONST.__kalloc_var: 0x460
+  __DATA_CONST.__kalloc_var: 0x3c0
   __DATA_CONST.__auth_got: 0x280
   __DATA_CONST.__got: 0xd8
   __DATA_CONST.__auth_ptr: 0x8
-  Functions: 656
-  Symbols:   1291
-  CStrings:  217
+  Functions: 660
+  Symbols:   1293
+  CStrings:  223
 
Symbols:
+ __ZN12AppleRAIDSet11lockMembersEv
+ __ZN12AppleRAIDSet13unlockMembersEv
+ __ZN12AppleRAIDSet19retainActiveMembersEPP15AppleRAIDMemberj
+ __ZN12AppleRAIDSet20releaseActiveMembersEPP15AppleRAIDMemberj
+ __ZZN12AppleRAIDSet9resizeSetEjE20kalloc_type_view_509
+ __ZZN12AppleRAIDSet9resizeSetEjE20kalloc_type_view_529
+ __ZZN13AppleLVMGroup8startSetEvE20kalloc_type_view_265
+ __ZZN13AppleLVMGroup9resizeSetEjE20kalloc_type_view_227
+ __ZZN13AppleLVMGroup9resizeSetEjE20kalloc_type_view_230
+ __ZZN23AppleRAIDStorageRequest20initWithAppleRAIDSetEP12AppleRAIDSetE19kalloc_type_view_98
- __ZZN12AppleRAIDSet9resizeSetEjE20kalloc_type_view_486
- __ZZN12AppleRAIDSet9resizeSetEjE20kalloc_type_view_492
- __ZZN13AppleLVMGroup17findFreeLVEOffsetEP14AppleLVMVolumeE21kalloc_type_view_1191
- __ZZN13AppleLVMGroup8startSetEvE20kalloc_type_view_239
- __ZZN13AppleLVMGroup9resizeSetEjE20kalloc_type_view_201
- __ZZN13AppleLVMGroup9resizeSetEjE20kalloc_type_view_204
- __ZZN18AppleRAIDMirrorSet9resizeSetEjE20kalloc_type_view_170
- __ZZN23AppleRAIDStorageRequest20initWithAppleRAIDSetEP12AppleRAIDSetE19kalloc_type_view_92
CStrings:
+ "121111121222121211121111222222222211122221122111111112"
+ "1211111212221212111211112222222222111222211221111111121111111"
+ "121111121222121211121111222222222211122221122111111112111212121"
+ "12111112122212121112111122222222221112222112211111111212"
+ "AppleLVMGroup::addMember() member index (%u) >= member count (%u) for member %s\n"
+ "AppleLVMGroup::removeMember() member index (%u) >= member count (%u) for member %s\n"
+ "AppleRAIDConcatSet::addMember() member index (%u) >= member count (%u) for member %s\n"
+ "AppleRAIDConcatSet::removeMember() member index (%u) >= member count (%u) for member %s\n"
+ "AppleRAIDMember::parseRAIDHeaderV2 - arHeaderBuffer is null\n"
+ "AppleRAIDMember::parseRAIDHeaderV2 - headerBuffer is null\n"
+ "AppleRAIDMember::parseRAIDHeaderV2 - tmpString is null\n"
+ "AppleRAIDMirrorSet::removeMember() member index (%u) >= member count (%u) for member %s\n"
- "12111112122212121112111122222222221112222112211111112"
- "121111121222121211121111222222222211122221122111111121111111"
- "12111112122212121112111122222222221112222112211111112111212121"
- "1211111212221212111211112222222222111222211221111111212"
- "site.UInt32"
- "site.UInt64"
```
