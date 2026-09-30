## MediaGroups

> `/System/Library/PrivateFrameworks/MediaGroups.framework/Versions/A/MediaGroups`

```diff

-44.0.0.0.0
-  __TEXT.__text: 0xb678
+44.40.1.0.0
+  __TEXT.__text: 0xb648
   __TEXT.__auth_stubs: 0x300
-  __TEXT.__objc_methlist: 0x880
+  __TEXT.__objc_methlist: 0xb44
   __TEXT.__const: 0x80
   __TEXT.__cstring: 0x86c
   __TEXT.__gcc_except_tab: 0x2f8
   __TEXT.__oslogstring: 0x493
-  __TEXT.__unwind_info: 0x448
+  __TEXT.__unwind_info: 0x440
   __TEXT.__objc_classname: 0x250
   __TEXT.__objc_methname: 0x14ae
   __TEXT.__objc_methtype: 0x695

   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5b0
+  __DATA_CONST.__objc_selrefs: 0x630
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x38
   __AUTH_CONST.__auth_got: 0x190
   __AUTH_CONST.__const: 0x380
   __AUTH_CONST.__cfstring: 0x720
-  __AUTH_CONST.__objc_const: 0x19d0
+  __AUTH_CONST.__objc_const: 0x14f8
   __AUTH.__objc_data: 0x550
   __DATA.__objc_ivar: 0x5c
   __DATA.__data: 0x4e0

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7528F974-A25D-3A85-9090-C80B2010C448
+  UUID: A1F16A73-DB0E-3091-9FF1-F51490197C55
   Functions: 266
   Symbols:   739
   CStrings:  509
Functions:
~ -[MGGroup membersWithCompletion:] : 480 -> 476
~ -[MGClientConnectionProvider init] : 768 -> 772
~ -[MGClientConnectionProvider _unsafe_setServiceConnection:] : 812 -> 788
~ -[MGClientService startQueryWithQueryData:] : 640 -> 636
~ -[MGClientService stopQuery:completion:] : 440 -> 436
~ -[MGClientService query:didUpdate:completion:] : 608 -> 604
~ -[MGClientService connectionProvider:serviceLost:] : 544 -> 548
~ -[MGClientService connectionProviderServiceAvailable:] : 248 -> 252
~ -[MGGroupIdentifier isEqual:] : 524 -> 512
~ _MGMemberIdentifiersForMediaSystem : 720 -> 716
~ -[MGGroupQuery initWithConnectionProvider:predicate:updateHandler:] : 592 -> 588

```
