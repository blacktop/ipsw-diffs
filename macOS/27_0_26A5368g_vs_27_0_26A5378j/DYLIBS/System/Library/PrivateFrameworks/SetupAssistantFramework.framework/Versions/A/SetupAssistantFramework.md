## SetupAssistantFramework

> `/System/Library/PrivateFrameworks/SetupAssistantFramework.framework/Versions/A/SetupAssistantFramework`

```diff

-  __TEXT.__text: 0xc540
+  __TEXT.__text: 0xc488
   __TEXT.__objc_methlist: 0xfe0
   __TEXT.__const: 0xb0
-  __TEXT.__cstring: 0x190f
+  __TEXT.__cstring: 0x1928
   __TEXT.__oslogstring: 0x1ba
   __TEXT.__gcc_except_tab: 0xa4
   __TEXT.__dlopen_cstrs: 0x4e
-  __TEXT.__unwind_info: 0x470
+  __TEXT.__unwind_info: 0x478
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9a8
+  __DATA_CONST.__objc_selrefs: 0x9a0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x38
-  __DATA_CONST.__got: 0x180
+  __DATA_CONST.__got: 0x188
   __AUTH_CONST.__const: 0x310
-  __AUTH_CONST.__cfstring: 0x11c0
+  __AUTH_CONST.__cfstring: 0x11e0
   __AUTH_CONST.__objc_const: 0x23d0
   __AUTH_CONST.__auth_got: 0x260
   __AUTH.__objc_data: 0x3c0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 347
-  Symbols:   971
-  CStrings:  353
+  Symbols:   970
+  CStrings:  355
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ _objc_msgSend$isUnixNameValidForNewUserAccount:
- _objc_msgSend$generateUnixNameUsingString:
- _objc_msgSend$isUnixNameValid:
Functions:
~ -[SAFacelessUserConfiguration validateWithError:] : 1308 -> 1124
CStrings:
+ "Password cannot be empty"

```
