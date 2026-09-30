## RemoteManagementAgent

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/RemoteManagementAgent`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
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
-  __TEXT.__text: 0x95f8c
-  __TEXT.__auth_stubs: 0x700
-  __TEXT.__objc_stubs: 0xc300
+624.1.3.0.0
+  __TEXT.__text: 0x95e84
+  __TEXT.__auth_stubs: 0x710
+  __TEXT.__objc_stubs: 0xc340
   __TEXT.__objc_methlist: 0x4a30
   __TEXT.__const: 0x108
   __TEXT.__gcc_except_tab: 0x40e0
-  __TEXT.__cstring: 0x30b4
+  __TEXT.__cstring: 0x30df
   __TEXT.__objc_classname: 0x1032
-  __TEXT.__objc_methname: 0xef7b
-  __TEXT.__objc_methtype: 0x265b
+  __TEXT.__objc_methname: 0xefe0
+  __TEXT.__objc_methtype: 0x265e
   __TEXT.__oslogstring: 0xc3ee
   __TEXT.__ustring: 0x2ec
   __TEXT.__unwind_info: 0x20e0
   __DATA_CONST.__const: 0x28b8
-  __DATA_CONST.__cfstring: 0x34c0
+  __DATA_CONST.__cfstring: 0x34e0
   __DATA_CONST.__objc_classlist: 0x2f8
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x108

   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0x138
-  __DATA_CONST.__auth_got: 0x390
-  __DATA_CONST.__got: 0x998
+  __DATA_CONST.__auth_got: 0x398
+  __DATA_CONST.__got: 0x988
   __DATA.__objc_const: 0x86a8
-  __DATA.__objc_selrefs: 0x34d8
+  __DATA.__objc_selrefs: 0x34f8
   __DATA.__objc_ivar: 0x2ac
   __DATA.__objc_data: 0x1db0
   __DATA.__data: 0xc60

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 2645
-  Symbols:   400
-  CStrings:  3879
+  Symbols:   399
+  CStrings:  3884
 
Symbols:
+ _notify_post
- _OBJC_CLASS_$_RMModelStatusManagementPushToken
- _RMModelStatusItemManagementPushToken
Functions:
~ sub_10000c9a8 : 340 -> 312
~ sub_10000dfec -> sub_10000dfd0 : 744 -> 728
~ sub_10001aec0 -> sub_10001ae94 : 20 -> 68
~ sub_10002e860 -> sub_10002e864 : 208 -> 192
~ sub_1000321f4 -> sub_1000321e8 : 208 -> 192
~ sub_10005b54c -> sub_10005b530 : 888 -> 848
~ sub_10005baa0 -> sub_10005ba5c : 180 -> 48
~ sub_10005bb54 -> sub_10005ba8c : 380 -> 68
~ sub_10006bf50 -> sub_10006bd50 : 284 -> 352
~ sub_10006c06c -> sub_10006beb0 : 3272 -> 3392
~ sub_10006d724 -> sub_10006d5e0 : 948 -> 1048
~ sub_1000949ac -> sub_1000948cc : 92 -> 52
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
