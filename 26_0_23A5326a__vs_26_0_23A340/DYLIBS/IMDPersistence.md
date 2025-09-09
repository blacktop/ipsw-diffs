## IMDPersistence

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence`

```diff

-1448.100.1.2.74
-  __TEXT.__text: 0x2228b4
-  __TEXT.__auth_stubs: 0x44d0
-  __TEXT.__objc_methlist: 0x7044
+1448.100.1.2.101
+  __TEXT.__text: 0x2237d0
+  __TEXT.__auth_stubs: 0x44e0
+  __TEXT.__objc_methlist: 0x7064
   __TEXT.__const: 0xa1c8
-  __TEXT.__cstring: 0x477ab
+  __TEXT.__cstring: 0x478eb
   __TEXT.__oslogstring: 0x1d6b6
-  __TEXT.__gcc_except_tab: 0xf824
+  __TEXT.__gcc_except_tab: 0xf848
   __TEXT.__ustring: 0x434
   __TEXT.__dlopen_cstrs: 0x360
   __TEXT.__constg_swiftt: 0x4ccc
-  __TEXT.__swift5_typeref: 0x31f0
+  __TEXT.__swift5_typeref: 0x3220
   __TEXT.__swift5_builtin: 0x244
   __TEXT.__swift5_reflstr: 0x2ac1
   __TEXT.__swift5_fieldmd: 0x2d50

   __TEXT.__swift5_proto: 0x664
   __TEXT.__swift5_types: 0x31c
   __TEXT.__swift5_protos: 0x38
-  __TEXT.__swift5_capture: 0xf1c
+  __TEXT.__swift5_capture: 0xf24
   __TEXT.__swift_as_entry: 0x60
   __TEXT.__swift_as_ret: 0x58
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x8c48
-  __TEXT.__eh_frame: 0x6db0
+  __TEXT.__unwind_info: 0x8c68
+  __TEXT.__eh_frame: 0x6de8
   __TEXT.__objc_classname: 0x11ad
-  __TEXT.__objc_methname: 0x17544
-  __TEXT.__objc_methtype: 0x369d
-  __TEXT.__objc_stubs: 0x11920
+  __TEXT.__objc_methname: 0x17582
+  __TEXT.__objc_methtype: 0x36a0
+  __TEXT.__objc_stubs: 0x11940
   __DATA_CONST.__got: 0x16f0
-  __DATA_CONST.__const: 0x8300
+  __DATA_CONST.__const: 0x8358
   __DATA_CONST.__objc_classlist: 0x5f0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5190
+  __DATA_CONST.__objc_selrefs: 0x51a8
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x1d8
   __DATA_CONST.__objc_arraydata: 0x220
-  __AUTH_CONST.__auth_got: 0x2278
-  __AUTH_CONST.__const: 0x95f0
-  __AUTH_CONST.__cfstring: 0x11e20
-  __AUTH_CONST.__objc_const: 0xf280
+  __AUTH_CONST.__auth_got: 0x2280
+  __AUTH_CONST.__const: 0x96b8
+  __AUTH_CONST.__cfstring: 0x11ee0
+  __AUTH_CONST.__objc_const: 0xf260
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x1b10
   __AUTH.__data: 0x4088
-  __DATA.__objc_ivar: 0x47c
-  __DATA.__data: 0x2bc0
+  __DATA.__objc_ivar: 0x478
+  __DATA.__data: 0x2bd0
   __DATA.__bss: 0xa2d0
   __DATA.__common: 0x178
   __DATA_DIRTY.__objc_data: 0x1620

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 44313411-00D3-3178-971F-AC295F32CF8B
-  Functions: 10446
+  UUID: AE420F1F-9455-3050-8657-0F66C22F78F5
+  Functions: 10457
   Symbols:   2554
-  CStrings:  12201
+  CStrings:  12217
 
CStrings:
+ "SELECT 1\nFROM persistent_tasks\nWHERE flag =  ?  AND flag_group =  ?  AND lane =  ?  AND reason =  ? \nLIMIT 1"
+ "attachment(ck_sync_state)"
+ "attachment_idx_ck_sync_state"
+ "cancel"
+ "chat(ck_sync_state)"
+ "chat_idx_ck_sync_state"
+ "initWithUnsignedInteger:"
+ "loadPTaskReportsForGroups:excludingReasons:loadFullReports:completionBlock:"
+ "message(ck_sync_state, service)"
+ "message_idx_ck_sync_state_service"
+ "removeObserver:forKeyPath:context:"
+ "v44@0:8@\"NSArray\"16@\"NSArray\"24B32@?<v@?@\"NSArray\">36"
- "TB,R,N,V_isThrottled"
- "loadPTaskReportsForGroups:excludingReasons:completionBlock:"
- "v40@0:8@\"NSArray\"16@\"NSArray\"24@?<v@?@\"NSArray\">32"

```
