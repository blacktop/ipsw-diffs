## iMessage

> `/System/Library/Messages/PlugIns/iMessage.imservice/iMessage`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1491.300.43.0.0
-  __TEXT.__text: 0x11c14c
-  __TEXT.__auth_stubs: 0x2750
-  __TEXT.__objc_stubs: 0xfb20
+1491.300.74.0.0
+  __TEXT.__text: 0x11c87c
+  __TEXT.__auth_stubs: 0x2760
+  __TEXT.__objc_stubs: 0xfb40
   __TEXT.__objc_methlist: 0x38f8
   __TEXT.__const: 0x16c8
-  __TEXT.__gcc_except_tab: 0x9880
+  __TEXT.__gcc_except_tab: 0x98e0
   __TEXT.__cstring: 0x4479
-  __TEXT.__oslogstring: 0x1d02b
+  __TEXT.__oslogstring: 0x1d0db
   __TEXT.__objc_classname: 0x9af
-  __TEXT.__objc_methname: 0x16eaf
+  __TEXT.__objc_methname: 0x16f0f
   __TEXT.__objc_methtype: 0x3b78
   __TEXT.__ustring: 0x4
   __TEXT.__swift5_typeref: 0xf86

   __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_mpenum: 0x38
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x34c0
+  __TEXT.__unwind_info: 0x34d0
   __TEXT.__eh_frame: 0x1e48
-  __DATA_CONST.__const: 0x5730
-  __DATA_CONST.__cfstring: 0x3f60
+  __DATA_CONST.__const: 0x5760
+  __DATA_CONST.__cfstring: 0x3f80
   __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xe0

   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA_CONST.__auth_got: 0x13b8
-  __DATA_CONST.__got: 0x13a0
+  __DATA_CONST.__auth_got: 0x13c0
+  __DATA_CONST.__got: 0x13a8
   __DATA_CONST.__auth_ptr: 0x3d8
   __DATA.__objc_const: 0x4dc8
-  __DATA.__objc_selrefs: 0x46a8
+  __DATA.__objc_selrefs: 0x46b0
   __DATA.__objc_ivar: 0x29c
   __DATA.__objc_data: 0x1138
   __DATA.__data: 0x12f0

   - /System/Library/PrivateFrameworks/FTServices.framework/FTServices
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation
-  - /System/Library/PrivateFrameworks/IMCore.framework/IMCore
   - /System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence
   - /System/Library/PrivateFrameworks/IMDaemonCore.framework/IMDaemonCore
   - /System/Library/PrivateFrameworks/IMFoundation.framework/IMFoundation

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 2661
-  Symbols:   995
-  CStrings:  5659
+  Symbols:   996
+  CStrings:  5664
 
Symbols:
+ _objc_sync_enter
+ _objc_sync_exit
- _IMChatRegistryLogHandle
Functions:
~ sub_4cb0 -> sub_4c58 : 1356 -> 1372
~ __ReplaceExtensionPayloadDataWithAttachmentForIncomingMessage : 1264 -> 1268
~ sub_235e4 -> sub_235a0 : 9852 -> 9856
~ sub_2622c -> sub_261ec : 9284 -> 9288
~ sub_2d898 -> sub_2d85c : 536 -> 540
~ sub_38894 -> sub_3885c : 1884 -> 1904
~ sub_48200 -> sub_481dc : 9212 -> 9216
~ sub_55364 -> sub_55344 : 4996 -> 5016
~ sub_599f0 -> sub_599e4 : 6896 -> 7100
~ sub_663f4 -> sub_664b4 : 1980 -> 2072
~ sub_66bb0 -> sub_66ccc : 28 -> 132
~ sub_66bcc -> sub_66d50 : 28 -> 580
~ sub_67f10 -> sub_682bc : 1268 -> 1324
~ sub_68e78 -> sub_6925c : 148 -> 160
~ sub_68f0c -> sub_692fc : 440 -> 456
~ sub_6935c -> sub_6975c : 352 -> 364
~ sub_694bc -> sub_698c8 : 640 -> 800
~ sub_7b3f4 -> sub_7b8a0 : 2536 -> 2540
~ sub_acea4 -> sub_ad354 : 260 -> 284
~ sub_ad054 -> sub_ad51c : 260 -> 284
~ sub_ad158 -> sub_ad638 : 312 -> 348
~ sub_afdf0 -> sub_b02f4 : 112 -> 124
~ sub_ce124 -> sub_ce634 : 1500 -> 1556
~ sub_ce700 -> sub_cec48 : 5204 -> 5276
~ sub_d0154 -> sub_d06e4 : 1236 -> 1304
~ sub_d0628 -> sub_d0bfc : 1576 -> 1596
~ sub_d1730 -> sub_d1d18 : 1800 -> 1796
~ sub_d1e38 -> sub_d241c : 192 -> 196
~ sub_d4680 -> sub_d4c68 : 456 -> 484
~ sub_d4848 -> sub_d4e4c : 276 -> 312
~ sub_d4afc -> sub_d5124 : 256 -> 280
~ sub_d5478 -> sub_d5ab8 : 296 -> 320
~ sub_e17e8 -> sub_e1e40 : 300 -> 324
~ sub_ee4e4 -> sub_eeb54 : 1908 -> 1924
~ sub_111fb0 -> sub_112630 : 432 -> 460
~ sub_112160 -> sub_1127fc : 276 -> 312
~ sub_11aab0 -> sub_11b170 : 128 -> 152
CStrings:
+ "Acquisition failure for message %@; failing send."
+ "Not sending gradient for message %@, attachment acquisition failed. %@"
+ "Sending scheduled message update flags 0x%lx for message %@"
+ "Transfer %@ on message %@ finished acquisition without a file. %@"
+ "guidsForStoredAttachmentPayloadData:messageGUID:isIncoming:"
+ "guidsForStoredAttachmentPayloadDataURLs:messageGUID:isIncoming:"
+ "sU"
+ "scheduledMessageUpdateFlagsForDateEdited:"
- "Unrecoverable acquisition failure for message %@; failing send."
- "guidsForStoredAttachmentPayloadData:messageGUID:"
- "guidsForStoredAttachmentPayloadDataURLs:messageGUID:"
```
