## NewsUI2

> `/System/Library/PrivateFrameworks/NewsUI2.framework/NewsUI2`

```diff

-  __TEXT.__text: 0x15c2080
-  __TEXT.__auth_stubs: 0x1f1e0
-  __TEXT.__objc_methlist: 0xdb84
+  __TEXT.__text: 0x15c0cc0
+  __TEXT.__auth_stubs: 0x1f220
+  __TEXT.__objc_methlist: 0xdba4
   __TEXT.__const: 0xd7b54
-  __TEXT.__cstring: 0x59ca8
+  __TEXT.__cstring: 0x598d8
   __TEXT.__constg_swiftt: 0x41bd8
-  __TEXT.__swift5_typeref: 0x2f136
+  __TEXT.__swift5_typeref: 0x2f16c
   __TEXT.__swift5_builtin: 0xeb0
-  __TEXT.__swift5_reflstr: 0x41ee4
-  __TEXT.__swift5_fieldmd: 0x43074
+  __TEXT.__swift5_reflstr: 0x41f44
+  __TEXT.__swift5_fieldmd: 0x4308c
   __TEXT.__swift5_assocty: 0x76d8
   __TEXT.__swift5_proto: 0xac0c
   __TEXT.__swift5_types: 0x470c
   __TEXT.__oslogstring: 0x1539b
-  __TEXT.__swift5_capture: 0x19030
+  __TEXT.__swift5_capture: 0x18ffc
   __TEXT.__swift5_mpenum: 0x6f8
   __TEXT.__swift5_protos: 0xefc
   __TEXT.__swift_as_entry: 0xda4
   __TEXT.__swift_as_ret: 0xed4
-  __TEXT.__unwind_info: 0x3c468
+  __TEXT.__unwind_info: 0x3c440
   __TEXT.__eh_frame: 0x56f58
-  __TEXT.__objc_classname: 0x163f6
-  __TEXT.__objc_methname: 0x2f231
-  __TEXT.__objc_methtype: 0x9024
+  __TEXT.__objc_classname: 0x16426
+  __TEXT.__objc_methname: 0x2f2a1
+  __TEXT.__objc_methtype: 0x9094
   __TEXT.__objc_stubs: 0x13a00
   __DATA_CONST.__got: 0xb7d0
   __DATA_CONST.__const: 0x19c8
   __DATA_CONST.__objc_classlist: 0x33b8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_catlist2: 0x30
-  __DATA_CONST.__objc_protolist: 0xb88
+  __DATA_CONST.__objc_protolist: 0xb90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8108
-  __DATA_CONST.__objc_protorefs: 0x658
-  __AUTH_CONST.__auth_got: 0xf8f8
-  __AUTH_CONST.__const: 0x868f8
+  __DATA_CONST.__objc_selrefs: 0x8118
+  __DATA_CONST.__objc_protorefs: 0x660
+  __AUTH_CONST.__auth_got: 0xf918
+  __AUTH_CONST.__const: 0x86880
   __AUTH_CONST.__cfstring: 0x80
-  __AUTH_CONST.__objc_const: 0x75450
+  __AUTH_CONST.__objc_const: 0x75510
   __AUTH.__objc_data: 0x9cc0
   __AUTH.__data: 0x1dc18
-  __DATA.__data: 0x1f3e0
+  __DATA.__data: 0x1f400
   __DATA.__objc_stublist: 0x70
   __DATA.__bss: 0xbc458
   __DATA.__common: 0xfa8

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 81871
-  Symbols:   31806
-  CStrings:  16228
+  Functions: 81861
+  Symbols:   31812
+  CStrings:  16223
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_catlist2 : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__objc_stublist : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ __PROTOCOL_FCLocalNewsSelectionCriteriaDropboxType
+ __PROTOCOL_INSTANCE_METHODS_FCLocalNewsSelectionCriteriaDropboxType
+ __PROTOCOL_METHOD_TYPES_FCLocalNewsSelectionCriteriaDropboxType
+ __PROTOCOL_PROTOCOLS_FCLocalNewsSelectionCriteriaDropboxType
+ _flat unique So39FCLocalNewsSelectionCriteriaDropboxType_p
+ _objc_msgSend$depositSelectionCriteria:
+ _symbolic ______p 8NewsCore05LocalA28SelectionCriteriaDropboxTypeP
- _objc_msgSend$bodyTextLength
CStrings:
+ "@\"FCLocalNewsSelectionCriteria\"16@0:8"
+ "FCLocalNewsSelectionCriteriaDropboxType"
+ "Rejected local headline %{public}@ because %{public}@"
+ "depositSelectionCriteria:"
+ "loadSelectionCriteria"
+ "localNewsSelectionCriteriaDropbox"
+ "v24@0:8@\"FCLocalNewsSelectionCriteria\"16"
- "No topic allow list configured"
- "Rejected local headline %{public}@ because it didn't have a topic specified in the allowed topic filter"
- "Rejected local headline %{public}@ because it had a publish date %{public}@, it has been %{public}@ seconds since then exceeding timeout of %lu"
- "Rejected local headline %{public}@ because it was filtered by the sports filter"
- "Rejected local headline %{public}@ because its bodyTextLength %lu didn't satisfy minimum %lu"
- "Rejected local headline %{public}@ because its clusterID %{public}@ is already present on a selected item"
- "Rejected local headline %{public}@ because the publish date %{public}@ exceeded configured timeout %{public}@ for topic %{public}@"
- "Rejected local headline %{public}@ because the publisher %{public}@ is forbidden"
- "Storefront %{public}@ allows sports from any publisher"
- "Storefront %{public}@ allows sports from publishers %{public}@"
- "Storefront %{public}@ doesn't allow sports"
- "Using topic allow list %{public}@"

```
