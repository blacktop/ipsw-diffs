## KoaMapper

> `/System/Library/PrivateFrameworks/KoaMapper.framework/KoaMapper`

```diff

-3500.20.1.0.0
-  __TEXT.__text: 0x1ce4c
+3500.21.1.0.0
+  __TEXT.__text: 0x1ccfc
   __TEXT.__auth_stubs: 0xfa0
   __TEXT.__objc_methlist: 0x11f4
   __TEXT.__const: 0x4a0

   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x20
   __TEXT.__swift5_types: 0x1c
-  __TEXT.__cstring: 0x1405
+  __TEXT.__cstring: 0x13f7
   __TEXT.__swift5_capture: 0x150
-  __TEXT.__oslogstring: 0xf93
+  __TEXT.__oslogstring: 0xf65
   __TEXT.__gcc_except_tab: 0x1c0
-  __TEXT.__unwind_info: 0x748
+  __TEXT.__unwind_info: 0x740
   __TEXT.__eh_frame: 0x78
   __TEXT.__objc_classname: 0x452
-  __TEXT.__objc_methname: 0x22c7
-  __TEXT.__objc_methtype: 0x8c2
-  __TEXT.__objc_stubs: 0x2120
-  __DATA_CONST.__got: 0x5f8
+  __TEXT.__objc_methname: 0x227e
+  __TEXT.__objc_methtype: 0x8c5
+  __TEXT.__objc_stubs: 0x2100
+  __DATA_CONST.__got: 0x5f0
   __DATA_CONST.__const: 0x338
   __DATA_CONST.__objc_classlist: 0x128
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb28
+  __DATA_CONST.__objc_selrefs: 0xb20
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x7e0
   __AUTH_CONST.__const: 0x568
   __AUTH_CONST.__cfstring: 0x960
-  __AUTH_CONST.__objc_const: 0x2ef0
+  __AUTH_CONST.__objc_const: 0x2ed0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x1c8
-  __DATA.__objc_ivar: 0x124
+  __DATA.__objc_ivar: 0x120
   __DATA.__data: 0x630
   __DATA.__bss: 0x300
   __DATA_DIRTY.__objc_data: 0xd38

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: AFB0A781-8D8D-3965-9D93-2B5CB3844EDF
+  UUID: 3508AFD3-59F5-3BE1-850C-9E620B0CD7BD
   Functions: 638
-  Symbols:   2692
-  CStrings:  871
+  Symbols:   2689
+  CStrings:  868
 
Symbols:
+ -[KMContactStoreBridge _checkAuthorization]
+ -[KMMapper_CNContact _addLabeledFieldsOfType:labeledValues:labelOnly:excludeDefault:error:]
+ ___Block_byref_object_copy_.1422
+ ___Block_byref_object_copy_.1714
+ ___Block_byref_object_copy_.1917
+ ___Block_byref_object_dispose_.1423
+ ___Block_byref_object_dispose_.1715
+ ___Block_byref_object_dispose_.1918
+ _objc_msgSend$_addLabeledFieldsOfType:labeledValues:labelOnly:excludeDefault:error:
+ _objc_msgSend$_checkAuthorization
- -[KMContactStoreBridge _checkAuthorizationAndFetchMeCard]
- -[KMMapper_CNContact _addLabeledFieldsOfType:labeledValues:labelOnly:error:]
- _CNContactIdentifierKey
- _OBJC_IVAR_$_KMMapper_CNContact._meCardIdentifierKey
- ___Block_byref_object_copy_.1424
- ___Block_byref_object_copy_.1713
- ___Block_byref_object_copy_.1916
- ___Block_byref_object_dispose_.1425
- ___Block_byref_object_dispose_.1714
- ___Block_byref_object_dispose_.1917
- _objc_msgSend$_addLabeledFieldsOfType:labeledValues:labelOnly:error:
- _objc_msgSend$_checkAuthorizationAndFetchMeCard
- _objc_msgSend$_crossPlatformUnifiedMeContactWithKeysToFetch:error:
Functions:
~ -[KMMapper_CNContact .cxx_destruct] : 80 -> 68
~ -[KMMapper_CNContact _addLabeledFieldsOfType:labeledValues:labelOnly:error:] -> -[KMMapper_CNContact _addLabeledFieldsOfType:labeledValues:labelOnly:excludeDefault:error:] : 660 -> 728
~ -[KMMapper_CNContact itemsFromExternalObject:additionalFields:error:] : 2560 -> 2512
~ -[KMMapper_CNContact init] : 148 -> 124
~ -[KMContactStoreBridge _checkAuthorizationAndFetchMeCard] -> -[KMContactStoreBridge _checkAuthorization] : 524 -> 204
CStrings:
+ "-[KMContactStoreBridge _checkAuthorization]"
+ "B48@0:8q16@24B32B36^@40"
+ "_addLabeledFieldsOfType:labeledValues:labelOnly:excludeDefault:error:"
+ "_checkAuthorization"
- "%s Encountered error when fetching meCard: %@"
- "-[KMContactStoreBridge _checkAuthorizationAndFetchMeCard]"
- "B44@0:8q16@24B32^@36"
- "_addLabeledFieldsOfType:labeledValues:labelOnly:error:"
- "_checkAuthorizationAndFetchMeCard"
- "_crossPlatformUnifiedMeContactWithKeysToFetch:error:"
- "_meCardIdentifierKey"

```
