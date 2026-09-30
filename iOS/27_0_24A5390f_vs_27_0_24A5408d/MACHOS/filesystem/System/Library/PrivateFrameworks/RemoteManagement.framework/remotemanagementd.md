## remotemanagementd

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/remotemanagementd`

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
-  __TEXT.__text: 0x8b2b8
-  __TEXT.__auth_stubs: 0x860
-  __TEXT.__objc_stubs: 0xc360
+624.2.3.0.0
+  __TEXT.__text: 0x8b1dc
+  __TEXT.__auth_stubs: 0x870
+  __TEXT.__objc_stubs: 0xc3a0
   __TEXT.__objc_methlist: 0x4a28
   __TEXT.__const: 0xf0
   __TEXT.__gcc_except_tab: 0x3fe8
-  __TEXT.__cstring: 0x3019
+  __TEXT.__cstring: 0x3044
   __TEXT.__objc_classname: 0x1032
-  __TEXT.__objc_methname: 0xf0f9
-  __TEXT.__objc_methtype: 0x265b
+  __TEXT.__objc_methname: 0xf15e
+  __TEXT.__objc_methtype: 0x265e
   __TEXT.__oslogstring: 0xc31b
   __TEXT.__ustring: 0x2ec
   __TEXT.__unwind_info: 0x20a0
   __DATA_CONST.__const: 0x2760
-  __DATA_CONST.__cfstring: 0x3460
+  __DATA_CONST.__cfstring: 0x3480
   __DATA_CONST.__objc_classlist: 0x2f8
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x108

   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0x150
-  __DATA_CONST.__auth_got: 0x440
-  __DATA_CONST.__got: 0x9f8
+  __DATA_CONST.__auth_got: 0x448
+  __DATA_CONST.__got: 0x9e8
   __DATA.__objc_const: 0x86a8
-  __DATA.__objc_selrefs: 0x3518
+  __DATA.__objc_selrefs: 0x3538
   __DATA.__objc_ivar: 0x2ac
   __DATA.__objc_data: 0x1db0
   __DATA.__data: 0xc68

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 2566
-  Symbols:   434
-  CStrings:  3880
+  Symbols:   433
+  CStrings:  3885
 
Symbols:
+ _notify_post
- _OBJC_CLASS_$_RMModelStatusManagementPushToken
- _RMModelStatusItemManagementPushToken
Functions:
~ sub_10000dd88 : 312 -> 284
~ sub_10000f180 -> sub_10000f164 : 684 -> 668
~ sub_10001a278 -> sub_10001a24c : 20 -> 68
~ sub_10002b6d4 -> sub_10002b6d8 : 204 -> 188
~ sub_10002ed10 -> sub_10002ed04 : 204 -> 188
~ sub_100054b34 -> sub_100054b18 : 836 -> 800
~ sub_100055048 -> sub_100055008 : 176 -> 48
~ sub_1000550f8 -> sub_100055038 : 348 -> 68
~ sub_100063f34 -> sub_100063d5c : 272 -> 324
~ sub_100064044 -> sub_100063ea0 : 3040 -> 3176
~ sub_100065544 -> sub_100065428 : 836 -> 936
~ sub_100089d5c -> sub_100089ca4 : 88 -> 52
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
