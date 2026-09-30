## analyticsd

> `/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsd`

```diff

-  __TEXT.__text: 0x126088
+  __TEXT.__text: 0x125a7c
   __TEXT.__auth_stubs: 0x1be0
   __TEXT.__objc_stubs: 0x1f20
   __TEXT.__init_offsets: 0x24
   __TEXT.__objc_methlist: 0x4ac
-  __TEXT.__gcc_except_tab: 0x12ee8
+  __TEXT.__gcc_except_tab: 0x12eb4
   __TEXT.__const: 0xa924
-  __TEXT.__cstring: 0x15089
-  __TEXT.__oslogstring: 0x199f1
+  __TEXT.__cstring: 0x14fb9
+  __TEXT.__oslogstring: 0x19781
   __TEXT.__objc_methname: 0x1b34
   __TEXT.__objc_classname: 0xda
   __TEXT.__objc_methtype: 0x8c5

   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0x14
-  __TEXT.__unwind_info: 0x7648
+  __TEXT.__unwind_info: 0x7640
   __TEXT.__eh_frame: 0x398
   __DATA_CONST.__const: 0xaa18
   __DATA_CONST.__cfstring: 0xc80

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 5804
+  Functions: 5799
   Symbols:   665
-  CStrings:  3733
+  CStrings:  3725
 
Sections:
~ __TEXT.__init_offsets : content changed
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__data : content changed
CStrings:
+ "\n      INSERT INTO sessions_new (session_id, state, start, end, params, cadence)\n      SELECT \n        CASE agg_session_period \n          WHEN 0 THEN 'com.apple.CoreAnalytics.Daily'\n          WHEN 1 THEN 'com.apple.CoreAnalytics.Weekly' \n          WHEN 2 THEN 'com.apple.CoreAnalytics.Monthly'\n          WHEN 3 THEN 'com.apple.CoreAnalytics.Quarterly'\n        END as session_id,\n        1 as state,\n        strftime('%s', agg_session_start_timestamp) as start,\n        strftime('%s', agg_session_end_boundary) as end,\n        NULL as params,\n        agg_session_period as cadence\n      FROM (\n        SELECT agg_session_period, agg_session_start_timestamp, agg_session_end_boundary\n        FROM agg_session \n        WHERE agg_session_period IN (0, 1, 2, 3)\n        GROUP BY agg_session_period\n        HAVING agg_session_id = MIN(agg_session_id)\n      ) distinct_sessions\n    "
+ "channel"
- "\n      INSERT INTO sessions_new (session_id, state, start, end, params, cadence)\n      SELECT \n        CASE agg_session_period \n          WHEN 0 THEN 'com.apple.CoreAnalytics.Daily'\n          WHEN 1 THEN 'com.apple.CoreAnalytics.Weekly' \n          WHEN 2 THEN 'com.apple.CoreAnalytics.Monthly'\n          WHEN 3 THEN 'com.apple.CoreAnalytics.Quarterly'\n        END as session_id,\n        1 as state,\n        strftime('%s', agg_session_start_timestamp) * 1000000 as start,\n        strftime('%s', agg_session_end_boundary) * 1000000 as end,\n        NULL as params,\n        agg_session_period as cadence\n      FROM (\n        SELECT agg_session_period, agg_session_start_timestamp, agg_session_end_boundary\n        FROM agg_session \n        WHERE agg_session_period IN (0, 1, 2, 3)\n        GROUP BY agg_session_period\n        HAVING agg_session_id = MIN(agg_session_id)\n      ) distinct_sessions\n    "
- "\n      UPDATE sessions SET end = end * 1000000 WHERE end > 0 AND end < 1000000000000;\n    "
- "\n      UPDATE sessions SET start = start * 1000000 WHERE start > 0 AND start < 1000000000000;\n    "
- "Channel"
- "[State Store] DATABASE INITIALIZATION: modifying for V16 schema - repairing sessions.start/end rows that V13 migration stored in seconds instead of microseconds"
- "[State Store] Failed to repair sessions.end values from seconds to microseconds; %s"
- "[State Store] Failed to repair sessions.end values from seconds to microseconds[null database]"
- "[State Store] Failed to repair sessions.start values from seconds to microseconds; %s"
- "[State Store] Failed to repair sessions.start values from seconds to microseconds[null database]"
- "[State Store] V16 repair: rewrote %d sessions.start row(s) and %d sessions.end row(s) from seconds to microseconds"

```
