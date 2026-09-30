## IntelligencePlatform

> `/System/Library/PrivateFrameworks/IntelligencePlatform.framework/IntelligencePlatform`

```diff

-151.0.3.0.0
-  __TEXT.__text: 0x488108
-  __TEXT.__auth_stubs: 0x4c70
+153.1.0.0.0
+  __TEXT.__text: 0x485d14
+  __TEXT.__auth_stubs: 0x4c80
   __TEXT.__objc_methlist: 0xa9bc
-  __TEXT.__const: 0x49d60
-  __TEXT.__cstring: 0x1b7f2
-  __TEXT.__swift5_typeref: 0x138e4
-  __TEXT.__constg_swiftt: 0x1420c
+  __TEXT.__const: 0x49520
+  __TEXT.__cstring: 0x1ba42
+  __TEXT.__swift5_typeref: 0x137aa
+  __TEXT.__constg_swiftt: 0x140b8
   __TEXT.__swift5_reflstr: 0xb204
-  __TEXT.__swift5_fieldmd: 0x133b0
+  __TEXT.__swift5_fieldmd: 0x13204
   __TEXT.__swift5_builtin: 0x668
   __TEXT.__swift5_assocty: 0x2f48
-  __TEXT.__swift5_proto: 0x3eb4
-  __TEXT.__swift5_types: 0x1574
+  __TEXT.__swift5_proto: 0x3e20
+  __TEXT.__swift5_types: 0x1548
   __TEXT.__oslogstring: 0x8419
   __TEXT.__swift5_capture: 0x5740
   __TEXT.__swift_as_entry: 0x2f8

   __TEXT.__swift5_mpenum: 0x23c
   __TEXT.__gcc_except_tab: 0x10ec
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x14bd0
-  __TEXT.__eh_frame: 0x2bc84
+  __TEXT.__unwind_info: 0x14aa0
+  __TEXT.__eh_frame: 0x2bbd4
   __TEXT.__objc_classname: 0x1f5d
   __TEXT.__objc_methname: 0x18a69
   __TEXT.__objc_methtype: 0x342c

   __DATA_CONST.__objc_protorefs: 0x150
   __DATA_CONST.__objc_superrefs: 0x608
   __DATA_CONST.__objc_arraydata: 0xb8
-  __AUTH_CONST.__auth_got: 0x2648
-  __AUTH_CONST.__const: 0x2bef0
+  __AUTH_CONST.__auth_got: 0x2650
+  __AUTH_CONST.__const: 0x2ba98
   __AUTH_CONST.__cfstring: 0x2ea0
-  __AUTH_CONST.__objc_const: 0x2a4e8
+  __AUTH_CONST.__objc_const: 0x2a548
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH_CONST.__objc_intobj: 0xf0

   __AUTH.__objc_data: 0x3508
   __AUTH.__data: 0x7240
   __DATA.__objc_ivar: 0x1590
-  __DATA.__data: 0xec08
-  __DATA.__bss: 0x6d2e0
-  __DATA.__common: 0x5a8
+  __DATA.__data: 0xe9d8
+  __DATA.__bss: 0x6c060
+  __DATA.__common: 0x560
   __DATA_DIRTY.__objc_data: 0x4c38
-  __DATA_DIRTY.__data: 0xc3f0
+  __DATA_DIRTY.__data: 0xc360
   __DATA_DIRTY.__bss: 0x9f20
   __DATA_DIRTY.__common: 0x158
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7695068A-6A4F-3593-9C86-C93901371BFF
-  Functions: 35905
+  UUID: 81001D14-7653-331B-9F6D-509C7BFC697C
+  Functions: 35762
   Symbols:   1142
-  CStrings:  7487
+  CStrings:  7493
 
CStrings:
+ "    SELECT ci.userAlignment AS userAlignment,\n           c.uuid AS uuid,\n           c.bundleId AS bundleId\n    FROM candidateInteractions ci\n    JOIN candidates c ON c.id == ci.candidateId\n    WHERE ci.eventId = ?"
+ "    SELECT ev.id AS eventId,\n           ev.originId AS originId,\n           ev.occurredAt AS occurredAt\n    FROM events ev\n    ORDER BY ev.occurredAt DESC"
+ "    SELECT t.userAlignment AS userAlignment\n    FROM tupleInteractions t\n    WHERE t.eventId = ?"
+ "candidatesSelectStatement"
+ "eventSelectAllStatement"
+ "tupleSelectStatement"

```
