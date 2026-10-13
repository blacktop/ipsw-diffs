## IMDPersistence

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence`

```diff

-1491.200.95.0.0
-  __TEXT.__text: 0x2f42c0
+1491.200.101.2.5
+  __TEXT.__text: 0x2f58c8
   __TEXT.__objc_methlist: 0xa584
-  __TEXT.__const: 0xc3d0
-  __TEXT.__cstring: 0x5eba4
+  __TEXT.__const: 0xc3f0
+  __TEXT.__cstring: 0x5ed44
   __TEXT.__oslogstring: 0x3c244
   __TEXT.__gcc_except_tab: 0xc5ec
   __TEXT.__ustring: 0x434

   __TEXT.__swift5_capture: 0x2044
   __TEXT.__constg_swiftt: 0x5988
   __TEXT.__swift5_builtin: 0x348
-  __TEXT.__swift5_reflstr: 0x3879
-  __TEXT.__swift5_fieldmd: 0x36c4
+  __TEXT.__swift5_reflstr: 0x38a9
+  __TEXT.__swift5_fieldmd: 0x36d0
   __TEXT.__swift5_assocty: 0x770
   __TEXT.__swift5_proto: 0x4c0
   __TEXT.__swift5_types: 0x390

   __TEXT.__swift_as_cont: 0x3a8
   __TEXT.__swift5_mpenum: 0x44
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__unwind_info: 0xd698
-  __TEXT.__eh_frame: 0x9ddc
+  __TEXT.__unwind_info: 0xd6b8
+  __TEXT.__eh_frame: 0x9de4
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x2a10
+  __AUTH_CONST.__auth_got: 0x2a18
   __AUTH.__objc_data: 0x1060
   __AUTH.__data: 0x1cb0
   __DATA.__objc_ivar: 0x56c
-  __DATA.__data: 0x3bb0
+  __DATA.__data: 0x3be0
   __DATA.__common: 0x270
   __DATA_DIRTY.__objc_data: 0x30b8
   __DATA_DIRTY.__data: 0x6560

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 13842
+  Functions: 13847
   Symbols:   2859
-  CStrings:  7543
+  CStrings:  7560
 
CStrings:
+ "\n          FROM "
+ "\n          ORDER BY "
+ "\n        )\n    )"
+ "\n      GROUP BY "
+ "\n      INNER JOIN "
+ " <= span.last_date"
+ " = (\n          SELECT "
+ " = span.conversation\n            AND "
+ " = span.conversation\n        AND "
+ " AS MATERIALIZED (\n      SELECT "
+ " AS conversation, "
+ " AS conversation, MAX("
+ " AS threshold_id\n      FROM "
+ " ASC\n          LIMIT 1 OFFSET "
+ " span\n      INNER JOIN "
+ " threshold\n      WHERE threshold.conversation = "
+ ") AS last_date\n      FROM "
+ "fl_span_conversations"
+ "fl_thresholds"
+ "ranked"
- "\n          ORDER BY threshold_date ASC, threshold_id ASC\n          LIMIT 1 OFFSET  ? \n      ) threshold\n      WHERE ("
- " AS threshold_id\n          FROM "
- "NOT EXISTS (\n      SELECT 1\n      FROM (\n          SELECT "
```
