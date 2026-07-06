## Passbook

> `/private/var/staged_system_apps/Passbook.app/Passbook`

```diff

-  __TEXT.__text: 0xfd10
+  __TEXT.__text: 0x10008
   __TEXT.__auth_stubs: 0x630
-  __TEXT.__objc_stubs: 0x2da0
-  __TEXT.__objc_methlist: 0x9d4
+  __TEXT.__objc_stubs: 0x2f00
+  __TEXT.__objc_methlist: 0x9e4
   __TEXT.__const: 0x80
   __TEXT.__gcc_except_tab: 0x48
-  __TEXT.__objc_methname: 0x463d
-  __TEXT.__cstring: 0x6e4
+  __TEXT.__objc_methname: 0x4725
+  __TEXT.__cstring: 0x74b
   __TEXT.__oslogstring: 0x4ec
   __TEXT.__objc_classname: 0x150
   __TEXT.__objc_methtype: 0xf98
   __TEXT.__unwind_info: 0x2d0
   __DATA_CONST.__const: 0x920
-  __DATA_CONST.__cfstring: 0x420
+  __DATA_CONST.__cfstring: 0x500
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__auth_got: 0x328
-  __DATA_CONST.__got: 0x908
+  __DATA_CONST.__got: 0x918
   __DATA.__objc_const: 0xb70
-  __DATA.__objc_selrefs: 0xf78
+  __DATA.__objc_selrefs: 0xfd0
   __DATA.__objc_ivar: 0x6c
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x3c8

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 197
-  Symbols:   400
-  CStrings:  799
+  Functions: 198
+  Symbols:   401
+  CStrings:  824
 
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ _OBJC_CLASS_$_NSURLQueryItem
Functions:
~ sub_100003620 : 14044 -> 14276
+ sub_10000dad0
CStrings:
+ "DETAILS"
+ "_openRemotePassInBridge:action:"
+ "_remoteLibrary"
+ "action"
+ "bridge:%@"
+ "com.apple.NanoPassbookBridgeSettings"
+ "isRemotePass"
+ "openSensitiveURL:withOptions:"
+ "passSerialNumber"
+ "passTypeIdentifier"
+ "passWithUniqueID:"
+ "percentEncodedQuery"
+ "queryItemWithName:value:"
+ "root"
+ "serialNumber"
+ "setQueryItems:"
+ "sharedInstanceWithRemoteLibrary"

```
