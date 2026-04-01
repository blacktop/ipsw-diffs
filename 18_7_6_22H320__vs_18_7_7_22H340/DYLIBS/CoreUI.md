## CoreUI

> `/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`

```diff

-918.3.0.0.0
-  __TEXT.__text: 0xa4ef4
+918.3.2.0.0
+  __TEXT.__text: 0xa5074
   __TEXT.__auth_stubs: 0x2630
   __TEXT.__objc_methlist: 0x8918
   __TEXT.__const: 0x49f8
-  __TEXT.__cstring: 0x23b42
+  __TEXT.__cstring: 0x23c8d
   __TEXT.__gcc_except_tab: 0x1424
   __TEXT.__oslogstring: 0x52
   __TEXT.__swift5_typeref: 0x72

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: B048BE4B-F55C-30E7-B7D5-DD72D8172087
+  UUID: F2CADFCE-1637-34B2-8E98-071E4DADA79A
   Functions: 4364
   Symbols:   13746
-  CStrings:  11356
+  CStrings:  11361
 
Functions:
~ _BOMStreamGetDataPointer : 36 -> 152
~ _CUIRenditionKeyInitializeAttributeIndexWithKeyFormat : 164 -> 280
~ __ReadPage : 512 -> 580
~ -[_CUIThemeColorRendition cgColor] : 216 -> 300
CStrings:
+ "(tree (%s) was not able to be read"
+ "BOMStreamGetDataPointer"
+ "CoreUI: %s keyidentifier is > CUIThemeKeyAttributeIndexCount not allowing over write of memory"
+ "CoreUI: INVALID COLOR #components: %d assuming black"
+ "void CUIRenditionKeyInitializeAttributeIndexWithKeyFormat(CUIRenditionKeyAttributeIndex *, const CUIRenditionKeyFormat *)"

```
