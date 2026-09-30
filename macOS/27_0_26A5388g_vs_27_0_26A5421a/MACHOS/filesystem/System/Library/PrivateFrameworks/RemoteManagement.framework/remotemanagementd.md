## remotemanagementd

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/remotemanagementd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-624.0.10.0.0
-  __TEXT.__text: 0x960d8
-  __TEXT.__auth_stubs: 0x710
-  __TEXT.__objc_stubs: 0xc320
+624.1.3.0.0
+  __TEXT.__text: 0x95fd0
+  __TEXT.__auth_stubs: 0x720
+  __TEXT.__objc_stubs: 0xc360
   __TEXT.__objc_methlist: 0x4a30
   __TEXT.__const: 0x100
   __TEXT.__gcc_except_tab: 0x4104
-  __TEXT.__cstring: 0x30c4
+  __TEXT.__cstring: 0x30ef
   __TEXT.__objc_classname: 0x1032
-  __TEXT.__objc_methname: 0xef8c
-  __TEXT.__objc_methtype: 0x265b
+  __TEXT.__objc_methname: 0xeff1
+  __TEXT.__objc_methtype: 0x265e
   __TEXT.__oslogstring: 0xc418
   __TEXT.__ustring: 0x2ec
-  __TEXT.__unwind_info: 0x20e8
+  __TEXT.__unwind_info: 0x20e0
   __DATA_CONST.__const: 0x28b8
-  __DATA_CONST.__cfstring: 0x34e0
+  __DATA_CONST.__cfstring: 0x3500
   __DATA_CONST.__objc_classlist: 0x2f8
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x108

   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0x138
-  __DATA_CONST.__auth_got: 0x398
-  __DATA_CONST.__got: 0x998
+  __DATA_CONST.__auth_got: 0x3a0
+  __DATA_CONST.__got: 0x988
   __DATA.__objc_const: 0x86a8
-  __DATA.__objc_selrefs: 0x34e0
+  __DATA.__objc_selrefs: 0x3500
   __DATA.__objc_ivar: 0x2ac
   __DATA.__objc_data: 0x1db0
   __DATA.__data: 0xc60

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 2646
-  Symbols:   401
-  CStrings:  3882
+  Symbols:   400
+  CStrings:  3887
 
Symbols:
+ _notify_post
- _OBJC_CLASS_$_RMModelStatusManagementPushToken
- _RMModelStatusItemManagementPushToken
Functions:
~ sub_10000cb24 : 340 -> 312
~ sub_10000e168 -> sub_10000e14c : 744 -> 728
~ sub_10001b03c -> sub_10001b010 : 20 -> 68
~ sub_10002e9d0 -> sub_10002e9d4 : 208 -> 192
~ sub_100032364 -> sub_100032358 : 208 -> 192
~ sub_10005b6bc -> sub_10005b6a0 : 888 -> 848
~ sub_10005bc10 -> sub_10005bbcc : 180 -> 48
~ sub_10005bcc4 -> sub_10005bbfc : 380 -> 68
~ sub_10006c0c0 -> sub_10006bec0 : 284 -> 352
~ sub_10006c1dc -> sub_10006c020 : 3272 -> 3392
~ sub_10006d894 -> sub_10006d750 : 948 -> 1048
~ sub_100094b80 -> sub_100094aa0 : 92 -> 52
CStrings:
+ "B64@0:8@16@24@32@40q48^@56"
+ "UTF8String"
+ "_storeAssetData:asset:assetKey:serverContentType:enrollmentType:error:"
+ "com.apple.remotemanagement.device.unlocked"
+ "lowercaseString"
+ "serverReportedContentType"
+ "setServerReportedContentType:"
- "B56@0:8@16@24@32q40^@48"
- "_storeAssetData:asset:assetKey:enrollmentType:error:"
```
