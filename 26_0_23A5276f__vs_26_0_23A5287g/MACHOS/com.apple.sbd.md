## com.apple.sbd

> `/System/Library/PrivateFrameworks/CloudServices.framework/Helpers/com.apple.sbd`

```diff

-694.0.3.0.0
-  __TEXT.__text: 0x4e0ac
-  __TEXT.__auth_stubs: 0xff0
+694.0.4.0.0
+  __TEXT.__text: 0x4e210
+  __TEXT.__auth_stubs: 0x1000
   __TEXT.__objc_stubs: 0x6be0
   __TEXT.__objc_methlist: 0x2ea0
   __TEXT.__const: 0x150
-  __TEXT.__gcc_except_tab: 0x1bfc
-  __TEXT.__cstring: 0x3ff2
+  __TEXT.__gcc_except_tab: 0x1c44
+  __TEXT.__cstring: 0x4015
   __TEXT.__objc_methname: 0x7692
-  __TEXT.__oslogstring: 0x7d7f
+  __TEXT.__oslogstring: 0x7d72
   __TEXT.__objc_classname: 0x74c
   __TEXT.__objc_methtype: 0x10e2
   __TEXT.__unwind_info: 0xc80
-  __DATA_CONST.__auth_got: 0x808
+  __DATA_CONST.__auth_got: 0x810
   __DATA_CONST.__got: 0x6c0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x1488
-  __DATA_CONST.__cfstring: 0x3ac0
+  __DATA_CONST.__cfstring: 0x3ae0
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x78

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 88C8A5C4-89C1-34E8-AA0A-2200273152C5
+  UUID: DEFCFC01-429C-3CCB-9746-DF7BC00B9A49
   Functions: 1354
-  Symbols:   484
-  CStrings:  3337
+  Symbols:   485
+  CStrings:  3341
 
Symbols:
+ _objc_release_x2
Functions:
~ sub_10002cd78 : 1972 -> 2276
~ sub_10004c4dc -> sub_10004c60c : 60 -> 112
CStrings:
+ "%@"
+ "Attempting to update record metadata (%@)"
+ "failed to update record metadata (%@): %@"
+ "failed to update record metadata: %@"
+ "update metadata only supported for stingray and icdp records"
+ "update metadata with invalid parameters"
+ "update stingray metadata with invalid parameters"
- " metadata only supported for stingray records"
- "attempted to update stingray metadata, with incomplete metadata hash"
- "attempted to update stingray metadata, with invalid parameters: %@, %@ metadata hash"
- "update metadata only supported for stingray records"

```
