## IMDPersistence

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence`

```diff

-1450.200.88.2.1
-  __TEXT.__text: 0x221a48
-  __TEXT.__auth_stubs: 0x4550
-  __TEXT.__objc_methlist: 0x719c
-  __TEXT.__const: 0xa218
-  __TEXT.__cstring: 0x47d3b
+1450.200.89.2.31
+  __TEXT.__text: 0x226218
+  __TEXT.__auth_stubs: 0x4560
+  __TEXT.__objc_methlist: 0x71fc
+  __TEXT.__const: 0xad28
+  __TEXT.__cstring: 0x47e8b
   __TEXT.__oslogstring: 0x1d886
-  __TEXT.__gcc_except_tab: 0xd0cc
+  __TEXT.__gcc_except_tab: 0xd0d0
   __TEXT.__ustring: 0x434
   __TEXT.__dlopen_cstrs: 0x360
   __TEXT.__constg_swiftt: 0x4cf8
-  __TEXT.__swift5_typeref: 0x3252
+  __TEXT.__swift5_typeref: 0x3282
   __TEXT.__swift5_builtin: 0x244
-  __TEXT.__swift5_reflstr: 0x2ac1
+  __TEXT.__swift5_reflstr: 0x2ad1
   __TEXT.__swift5_fieldmd: 0x2d60
   __TEXT.__swift5_assocty: 0x530
   __TEXT.__swift5_proto: 0x664
   __TEXT.__swift5_types: 0x320
   __TEXT.__swift5_protos: 0x38
-  __TEXT.__swift5_capture: 0xfb0
+  __TEXT.__swift5_capture: 0xfd4
   __TEXT.__swift_as_entry: 0x60
   __TEXT.__swift_as_ret: 0x58
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x8830
-  __TEXT.__eh_frame: 0x6de8
-  __TEXT.__objc_classname: 0x11ad
-  __TEXT.__objc_methname: 0x179a4
-  __TEXT.__objc_methtype: 0x3781
-  __TEXT.__objc_stubs: 0x11b20
+  __TEXT.__unwind_info: 0x8820
+  __TEXT.__eh_frame: 0x6df0
+  __TEXT.__objc_classname: 0x11c3
+  __TEXT.__objc_methname: 0x17a35
+  __TEXT.__objc_methtype: 0x37aa
+  __TEXT.__objc_stubs: 0x11b40
   __DATA_CONST.__got: 0x1708
   __DATA_CONST.__const: 0x8390
-  __DATA_CONST.__objc_classlist: 0x5f8
+  __DATA_CONST.__objc_classlist: 0x600
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x218
+  __DATA_CONST.__objc_protolist: 0x228
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5248
-  __DATA_CONST.__objc_protorefs: 0xe0
+  __DATA_CONST.__objc_selrefs: 0x5260
+  __DATA_CONST.__objc_protorefs: 0xe8
   __DATA_CONST.__objc_superrefs: 0x1d8
   __DATA_CONST.__objc_arraydata: 0x220
-  __AUTH_CONST.__auth_got: 0x22b8
-  __AUTH_CONST.__const: 0x9890
+  __AUTH_CONST.__auth_got: 0x22c0
+  __AUTH_CONST.__const: 0x9920
   __AUTH_CONST.__cfstring: 0x11f40
-  __AUTH_CONST.__objc_const: 0xf388
+  __AUTH_CONST.__objc_const: 0xf420
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x1bc0
-  __AUTH.__data: 0x3ea8
-  __DATA.__objc_ivar: 0x484
-  __DATA.__data: 0x2ba0
+  __AUTH.__objc_data: 0x1c30
+  __AUTH.__data: 0x3ed0
+  __DATA.__objc_ivar: 0x488
+  __DATA.__data: 0x2da8
   __DATA.__bss: 0x9fe0
   __DATA.__common: 0x168
   __DATA_DIRTY.__objc_data: 0x1620
-  __DATA_DIRTY.__data: 0x3f40
+  __DATA_DIRTY.__data: 0x3d60
   __DATA_DIRTY.__bss: 0x1ee8
   __DATA_DIRTY.__common: 0x50
   - /System/Library/Frameworks/AppIntents.framework/AppIntents

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A0D7243A-A71A-3806-9756-9B481AA80077
-  Functions: 10542
-  Symbols:   2566
-  CStrings:  12271
+  UUID: 1079CD55-A617-3129-8F8B-B52B6C1FC48A
+  Functions: 10556
+  Symbols:   2569
+  CStrings:  12282
 
Symbols:
+ _IMSharedHelperCurrentRegionRequiresKnownSenderForNickname
+ _OBJC_CLASS_$_IMDGroupNameAndPhotoHelper
+ _OBJC_CLASS_$__TtC14IMDPersistence37IMDChatQueriesGroupNameAndPhotoHelper
+ _OBJC_METACLASS_$_IMDGroupNameAndPhotoHelper
+ _OBJC_METACLASS_$__TtC14IMDPersistence37IMDChatQueriesGroupNameAndPhotoHelper
- _OBJC_CLASS_$__TtC14IMDPersistence29IMDChatQueriesKnownChatHelper
- _OBJC_METACLASS_$__TtC14IMDPersistence29IMDChatQueriesKnownChatHelper
CStrings:
+ "DROP INDEX IF EXISTS message_idx_is_scheduled_message;"
+ "IMDGroupNameAndPhotoHelper"
+ "IMDRecoverableQueries"
+ "Recoverable"
+ "SELECT 1 FROM chat_recoverable_message_join where message_id in (select rowid from message where guid =  ? )\nunion\nSELECT 1 FROM recoverable_message_part where message_id in (select rowid from message where guid =  ? )"
+ "Tq,N,V_isFilteredValue"
+ "_TtC14IMDPersistence37IMDChatQueriesGroupNameAndPhotoHelper"
+ "_isFilteredValue"
+ "_shouldDisplayGroupNameAndPhotoWithRecord:"
+ "isFilteredValue"
+ "isRecoverablyDeletedMessageGUID:completionHandler:"
+ "message(schedule_type, rowid) WHERE schedule_type=2"
+ "setIsFilteredValue:"
+ "shouldDisplayGroupNameAndPhotoWith:handles:"
+ "shouldDisplayGroupNameAndPhotoWith:participants:"
+ "v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"
- "_TtC14IMDPersistence29IMDChatQueriesKnownChatHelper"
- "_isChatConfigurationKnownWithRecord:"
- "isChatConfigurationKnownWith:handles:"
- "isChatConfigurationKnownWith:participants:"
- "message(schedule_type) WHERE schedule_type=2"

```
