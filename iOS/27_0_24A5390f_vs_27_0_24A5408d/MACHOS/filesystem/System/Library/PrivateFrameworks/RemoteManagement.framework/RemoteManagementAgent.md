## RemoteManagementAgent

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/RemoteManagementAgent`

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
-  __TEXT.__text: 0x8b53c
-  __TEXT.__auth_stubs: 0x860
-  __TEXT.__objc_stubs: 0xc380
+624.2.3.0.0
+  __TEXT.__text: 0x8b460
+  __TEXT.__auth_stubs: 0x870
+  __TEXT.__objc_stubs: 0xc3c0
   __TEXT.__objc_methlist: 0x4a28
   __TEXT.__const: 0xf8
   __TEXT.__gcc_except_tab: 0x4074
-  __TEXT.__cstring: 0x301d
+  __TEXT.__cstring: 0x3048
   __TEXT.__objc_classname: 0x1032
-  __TEXT.__objc_methname: 0xf106
-  __TEXT.__objc_methtype: 0x265b
+  __TEXT.__objc_methname: 0xf16b
+  __TEXT.__objc_methtype: 0x265e
   __TEXT.__oslogstring: 0xc336
   __TEXT.__ustring: 0x2ec
-  __TEXT.__unwind_info: 0x2070
+  __TEXT.__unwind_info: 0x2068
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
-  __DATA_CONST.__got: 0x9f0
+  __DATA_CONST.__auth_got: 0x448
+  __DATA_CONST.__got: 0x9e0
   __DATA.__objc_const: 0x86a8
-  __DATA.__objc_selrefs: 0x3520
+  __DATA.__objc_selrefs: 0x3540
   __DATA.__objc_ivar: 0x2ac
   __DATA.__objc_data: 0x1db0
   __DATA.__data: 0xc68

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 2567
-  Symbols:   434
-  CStrings:  3882
+  Symbols:   433
+  CStrings:  3887
 
Symbols:
+ _notify_post
- _OBJC_CLASS_$_RMModelStatusManagementPushToken
- _RMModelStatusItemManagementPushToken
Functions:
~ sub_10000bc14 : 312 -> 284
~ sub_10000d050 -> sub_10000d034 : 684 -> 668
~ sub_100018988 -> sub_10001895c : 20 -> 68
~ sub_10002a5b0 -> sub_10002a5b4 : 204 -> 188
~ sub_10002dbec -> sub_10002dbe0 : 204 -> 188
~ sub_100054c7c -> sub_100054c60 : 836 -> 800
~ sub_100055190 -> sub_100055150 : 176 -> 48
~ sub_100055240 -> sub_100055180 : 348 -> 68
~ sub_1000640d8 -> sub_100063f00 : 272 -> 324
~ sub_1000641e8 -> sub_100064044 : 3040 -> 3176
~ sub_1000656e8 -> sub_1000655cc : 836 -> 936
~ sub_100089f60 -> sub_100089ea8 : 88 -> 52
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
